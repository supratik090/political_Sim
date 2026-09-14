class ApiHttpError extends Error {
  constructor(message, status) {
    super(message);
    this.name = 'ApiHttpError';
    this.status = status;
    this.isHttpResponse = true;
  }
}

const FALLBACK_CANDIDATES = [
  'https://political-sim-279311597920.asia-south1.run.app',
  'http://192.168.29.219:7810',
  'http://10.0.2.2:7810',
  'http://localhost:7810'
];

export function getApiBaseUrl() {
  if (typeof window !== 'undefined' && window.localStorage.getItem('CUSTOM_API_URL')) {
    return window.localStorage.getItem('CUSTOM_API_URL').replace(/\/+$/, '');
  }
  const envUrl = import.meta.env.VITE_API_URL;
  const isCapacitor = typeof window !== 'undefined' && (
    window.Capacitor?.isNativePlatform() ||
    (window.location.hostname === 'localhost' && window.location.port === '')
  );

  if (isCapacitor) {
    if (!envUrl || envUrl.includes('localhost') || envUrl.includes('127.0.0.1')) {
      return FALLBACK_CANDIDATES[0];
    }
    return envUrl.replace(/\/+$/, '');
  }

  if (envUrl && envUrl.trim() !== '') {
    return envUrl.replace(/\/+$/, '');
  }

  return FALLBACK_CANDIDATES[0];
}

async function fetchWithAutoFallback(fetchFn) {
  try {
    return await fetchFn(getApiBaseUrl());
  } catch (initialErr) {
    // If backend responded with an HTTP status code (e.g. 400, 401, 404, 500),
    // the backend IS reachable! Do NOT trigger candidate fallback timeouts.
    if (initialErr.isHttpResponse) {
      throw initialErr;
    }
    if (typeof window !== 'undefined' && window.localStorage.getItem('CUSTOM_API_URL')) {
      throw initialErr;
    }
    const currentBase = getApiBaseUrl();
    for (const candidate of FALLBACK_CANDIDATES) {
      if (candidate === currentBase) continue;
      try {
        const result = await fetchFn(candidate);
        if (typeof window !== 'undefined') {
          console.log(`[API] Auto-discovered working backend URL: ${candidate}`);
          window.localStorage.setItem('CUSTOM_API_URL', candidate);
        }
        return result;
      } catch (err) {
        if (err.isHttpResponse) {
          if (typeof window !== 'undefined') {
            window.localStorage.setItem('CUSTOM_API_URL', candidate);
          }
          throw err;
        }
      }
    }
    throw initialErr;
  }
}

function buildUrl(baseUrl, path, params = {}) {
  const cleanBase = baseUrl.replace(/\/+$/, '');
  const cleanPath = path.startsWith('/') ? path : `/${path}`;
  const url = new URL(`${cleanBase}${cleanPath}`);
  Object.keys(params).forEach(key => {
    if (params[key] !== undefined && params[key] !== null) {
      url.searchParams.append(key, params[key]);
    }
  });
  return url.toString();
}

export async function apiGet(path, params = {}) {
  return fetchWithAutoFallback(async (baseUrl) => {
    const fullUrl = buildUrl(baseUrl, path, params);
    const response = await fetch(fullUrl);
    if (!response.ok) {
      let errMsg = `API GET request failed (${response.status} ${response.statusText})`;
      try {
        const errData = await response.json();
        if (errData && errData.error) errMsg = errData.error;
        else if (errData && errData.message) errMsg = errData.message;
      } catch (_) {}
      throw new ApiHttpError(errMsg, response.status);
    }
    return response.json();
  });
}

export async function apiPost(path, payload) {
  return fetchWithAutoFallback(async (baseUrl) => {
    const fullUrl = buildUrl(baseUrl, path);
    const response = await fetch(fullUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: payload !== undefined ? JSON.stringify(payload) : undefined,
    });
    if (!response.ok) {
      let errMsg = `API POST request failed (${response.status} ${response.statusText})`;
      try {
        const errData = await response.json();
        if (errData && errData.error) errMsg = errData.error;
        else if (errData && errData.message) errMsg = errData.message;
      } catch (_) {}
      throw new ApiHttpError(errMsg, response.status);
    }
    return response.json();
  });
}

export async function apiPut(path, payload) {
  return fetchWithAutoFallback(async (baseUrl) => {
    const fullUrl = buildUrl(baseUrl, path);
    const response = await fetch(fullUrl, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: payload !== undefined ? JSON.stringify(payload) : undefined,
    });
    if (!response.ok) {
      let errMsg = `API PUT request failed (${response.status} ${response.statusText})`;
      try {
        const errData = await response.json();
        if (errData && errData.error) errMsg = errData.error;
        else if (errData && errData.message) errMsg = errData.message;
      } catch (_) {}
      throw new ApiHttpError(errMsg, response.status);
    }
    return response.json();
  });
}

export async function apiDelete(path) {
  return fetchWithAutoFallback(async (baseUrl) => {
    const fullUrl = buildUrl(baseUrl, path);
    const response = await fetch(fullUrl, {
      method: 'DELETE',
    });
    if (!response.ok) {
      let errMsg = `API DELETE request failed (${response.status} ${response.statusText})`;
      try {
        const errData = await response.json();
        if (errData && errData.error) errMsg = errData.error;
        else if (errData && errData.message) errMsg = errData.message;
      } catch (_) {}
      throw new ApiHttpError(errMsg, response.status);
    }
    if (response.status === 204) return null;
    const text = await response.text();
    return text ? JSON.parse(text) : null;
  });
}

// Game API bindings
export const createGame = (payload) => apiPost('/api/games', payload);
export const fetchTurnView = (gameId) => apiGet(`/api/games/${gameId}/turn-view`);
export const getGame = (gameId) => apiGet(`/api/games/${gameId}`);
export const getGameByJoinCode = (joinCode) => apiGet(`/api/games/join-code/${joinCode}`);
export const joinGameLobby = (userId, joinCode, partyId) => 
  apiPost(`/api/games/join`, null, { userId, joinCode, partyId });
export const startGame = (gameId, userId) => 
  apiPost(`/api/games/${gameId}/start?userId=${userId}`);
export const fetchBuildingProjects = () => apiGet('/api/games/building-projects/definitions');
export const fetchPostDefinitions = () => apiGet('/api/games/posts/definitions');
export const listGames = (userId) => apiGet('/api/games/summaries', userId ? { userId } : {});
export const advanceTurn = (gameId, payload) => apiPost(`/api/games/${gameId}/turn/advance`, payload);
export const forfeitGame = (gameId) => apiPost(`/api/games/${gameId}/forfeit`);
export const deleteGame = (gameId) => apiDelete(`/api/games/${gameId}`);
export const fundProject = (gameId, partyId, projectKey, progress) => 
  apiPost(`/api/games/${gameId}/parties/${partyId}/projects/fund?projectKey=${projectKey}&progress=${progress}`);
export const destroyProject = (gameId, partyId, projectKey) => 
  apiPost(`/api/games/${gameId}/parties/${partyId}/projects/destroy?projectKey=${projectKey}`);
export const setProjectTarget = (gameId, partyId, projectKey, targetPartyId) => 
  apiPost(`/api/games/${gameId}/parties/${partyId}/projects/${projectKey}/target?targetPartyId=${targetPartyId}`);
export const createCooperationOffer = (gameId, payload) => apiPost(`/api/games/${gameId}/cooperation/offer`, payload);
export const respondToCooperationOffer = (gameId, offerId, accept) => 
  apiPost(`/api/games/${gameId}/cooperation/respond?offerId=${offerId}&accept=${accept}`);
export const bribeFaction = (gameId, targetPartyId, factionKey, coins) =>
  apiPost(`/api/games/${gameId}/bribe?targetPartyId=${targetPartyId}&factionKey=${factionKey}&coins=${coins}`);

export const lockPartyManagement = (gameId, partyId, payload) =>
  apiPost(`/api/games/${gameId}/party-management/lock?partyId=${partyId}`, payload);

export const takeLoan = (gameId, partyId) =>
  apiPost(`/api/games/${gameId}/parties/${partyId}/take-loan`);

export const buyRecoveryPack = (gameId, partyId) =>
  apiPost(`/api/games/${gameId}/parties/${partyId}/buy-recovery-pack`);

export const fetchBillsForGameplay = (scenarioKey) => apiGet(`/api/games/bills/scenario/${scenarioKey}`);

// Admin API bindings
export const fetchScenarios = () => apiGet('/api/admin/scenarios');
export const fetchCards = (scenarioKey) => apiGet('/api/admin/cards', scenarioKey ? { scenarioKey } : {});
export const fetchNews = (scenarioKey) => apiGet('/api/admin/news', scenarioKey ? { scenarioKey } : {});
export const fetchBills = (scenarioKey) => apiGet('/api/admin/bills', scenarioKey ? { scenarioKey } : {});
export const fetchFactions = () => apiGet('/api/admin/factions');
export const fetchScenarioProgress = (userId) => apiGet('/api/scenarios/progress', userId ? { userId } : {});
export const getFaction = (id) => apiGet(`/api/admin/factions/${id}`);
export const createFaction = (payload) => apiPost('/api/admin/factions', payload);
export const updateFaction = (id, payload) => apiPut(`/api/admin/factions/${id}`, payload);
export const deleteFaction = (id) => apiDelete(`/api/admin/factions/${id}`);

// Auth API bindings
export const registerUser = (payload) => apiPost('/api/auth/register', payload);
export const loginUser = (payload) => apiPost('/api/auth/login', payload);
