class ApiHttpError extends Error {
  constructor(message, status) {
    super(message);
    this.name = 'ApiHttpError';
    this.status = status;
    this.isHttpResponse = true;
  }
}

export function getApiBaseUrl() {
  if (typeof window !== 'undefined' && window.localStorage.getItem('CUSTOM_API_URL')) {
    return window.localStorage.getItem('CUSTOM_API_URL').replace(/\/+$/, '');
  }
  const envUrl = import.meta.env.VITE_API_URL;
  if (envUrl && envUrl.trim() !== '') {
    return envUrl.trim().replace(/\/+$/, '');
  }
  return 'http://localhost:7800';
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
  const baseUrl = getApiBaseUrl();
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
}

export async function apiPost(path, payload) {
  const baseUrl = getApiBaseUrl();
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
}

export async function apiPut(path, payload) {
  const baseUrl = getApiBaseUrl();
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
}

export async function apiDelete(path) {
  const baseUrl = getApiBaseUrl();
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
