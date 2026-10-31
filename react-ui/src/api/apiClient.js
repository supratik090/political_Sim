import { isAndroidApp } from '../utils/platform';

class ApiHttpError extends Error {
  constructor(message, status) {
    super(message);
    this.name = 'ApiHttpError';
    this.status = status;
    this.isHttpResponse = true;
  }
}

export function getApiBaseUrl() {
  if (typeof window !== 'undefined') {
    // 1. Explicit user override from Settings / Auth screen
    const customUrl = window.localStorage.getItem('CUSTOM_API_URL');
    if (customUrl && customUrl.trim() !== '') {
      return customUrl.trim().replace(/\/+$/, '');
    }
  }

  // 2. Build-time environment variable (e.g. Cloud Run in .env, .env.android, .env.production)
  const envUrl = import.meta.env.VITE_API_URL;
  if (envUrl && envUrl.trim() !== '') {
    return envUrl.trim().replace(/\/+$/, '');
  }

  // 3. Fallback for local browser dev (outside Android Capacitor webview)
  if (typeof window !== 'undefined' && !isAndroidApp()) {
    const isLocalBrowser =
      (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') &&
      window.location.port !== '';
    if (isLocalBrowser) {
      return 'http://localhost:7810';
    }
  }

  // 4. Default fallback: Cloud Run URL
  return 'https://political-sim-279311597920.asia-south1.run.app';
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

// ──────────────────────────────────────────
// DUAL-MODE BRIDGE HELPER
// ──────────────────────────────────────────

const getBridge = () => {
  if (typeof window !== 'undefined' && window.Capacitor?.Plugins?.NativeGameBridge) {
    return window.Capacitor.Plugins.NativeGameBridge;
  }
  return null;
};

const isNative = () => isAndroidApp() && Boolean(getBridge());

// ──────────────────────────────────────────
// GAME API BINDINGS (DUAL-MODE)
// ──────────────────────────────────────────

export const createGame = async (payload) => {
  if (isNative()) return getBridge().createGame(payload);
  return apiPost('/api/games', payload);
};

export const fetchTurnView = async (gameId) => {
  if (isNative()) return getBridge().fetchTurnView({ gameId });
  return apiGet(`/api/games/${gameId}/turn-view`);
};

export const getGame = async (gameId) => {
  if (isNative()) return getBridge().getGame({ gameId });
  return apiGet(`/api/games/${gameId}`);
};

export const getGameByJoinCode = async (joinCode) => {
  if (isNative()) return getBridge().getGame({ gameId: joinCode });
  return apiGet(`/api/games/join-code/${joinCode}`);
};

export const joinGameLobby = (userId, joinCode, partyId) => 
  apiPost(`/api/games/join`, null, { userId, joinCode, partyId });

export const startGame = (gameId, userId) => 
  apiPost(`/api/games/${gameId}/start?userId=${userId}`);

export const fetchBuildingProjects = async () => {
  if (isNative()) return getBridge().getBuildingProjects();
  return apiGet('/api/games/building-projects/definitions');
};

export const fetchPostDefinitions = async () => {
  if (isNative()) {
    const res = await getBridge().getPosts();
    return res.data || [];
  }
  return apiGet('/api/games/posts/definitions');
};

export const listGames = async (userId) => {
  if (isNative()) {
    const res = await getBridge().listGames({ userId: userId || '' });
    return res.data || [];
  }
  return apiGet('/api/games/summaries', userId ? { userId } : {});
};

export const advanceTurn = async (gameId, payload) => {
  if (isNative()) return getBridge().advanceTurn({ gameId, payload });
  return apiPost(`/api/games/${gameId}/turn/advance`, payload);
};

export const forfeitGame = async (gameId) => {
  if (isNative()) return getBridge().forfeitGame({ gameId });
  return apiPost(`/api/games/${gameId}/forfeit`);
};

export const deleteGame = async (gameId) => {
  if (isNative()) return getBridge().deleteGame({ gameId });
  return apiDelete(`/api/games/${gameId}`);
};

export const fundProject = async (gameId, partyId, projectKey, progress) => {
  if (isNative()) return getBridge().fundProject({ gameId, partyId, projectKey, progress: parseInt(progress, 10) || 0 });
  return apiPost(`/api/games/${gameId}/parties/${partyId}/projects/fund?projectKey=${projectKey}&progress=${progress}`);
};

export const destroyProject = async (gameId, partyId, projectKey) => {
  if (isNative()) return getBridge().destroyProject({ gameId, partyId, projectKey });
  return apiPost(`/api/games/${gameId}/parties/${partyId}/projects/destroy?projectKey=${projectKey}`);
};

export const setProjectTarget = async (gameId, partyId, projectKey, targetPartyId) => {
  if (isNative()) return getBridge().setProjectTarget({ gameId, partyId, projectKey, targetPartyId });
  return apiPost(`/api/games/${gameId}/parties/${partyId}/projects/${projectKey}/target?targetPartyId=${targetPartyId}`);
};

export const createCooperationOffer = (gameId, payload) => apiPost(`/api/games/${gameId}/cooperation/offer`, payload);
export const respondToCooperationOffer = (gameId, offerId, accept) => 
  apiPost(`/api/games/${gameId}/cooperation/respond?offerId=${offerId}&accept=${accept}`);
export const bribeFaction = (gameId, targetPartyId, factionKey, coins) =>
  apiPost(`/api/games/${gameId}/bribe?targetPartyId=${targetPartyId}&factionKey=${factionKey}&coins=${coins}`);

export const lockPartyManagement = async (gameId, partyId, payload) => {
  if (isNative()) return getBridge().lockPartyManagement({ gameId, partyId, payload });
  return apiPost(`/api/games/${gameId}/party-management/lock?partyId=${partyId}`, payload);
};

export const takeLoan = async (gameId, partyId) => {
  if (isNative()) return getBridge().takeLoan({ gameId, partyId });
  return apiPost(`/api/games/${gameId}/parties/${partyId}/take-loan`);
};

export const buyRecoveryPack = async (gameId, partyId) => {
  if (isNative()) return getBridge().buyRecoveryPack({ gameId, partyId });
  return apiPost(`/api/games/${gameId}/parties/${partyId}/buy-recovery-pack`);
};

export const fetchBillsForGameplay = async (scenarioKey) => {
  if (isNative()) {
    const res = await getBridge().getBills({ scenarioKey: scenarioKey || 'default' });
    return res.data || [];
  }
  return apiGet(`/api/games/bills/scenario/${scenarioKey}`);
};

export const fetchEventsForGameplay = async (scenarioKey) => {
  if (isNative()) {
    const res = await getBridge().getNews({ scenarioKey: scenarioKey || '' });
    return res.data || [];
  }
  return apiGet('/api/admin/news', scenarioKey ? { scenarioKey } : {});
};

// V2 Feedback API bindings
export const fetchNewsFeedback = async (gameId, payload) => {
  if (isNative()) return getBridge().fetchNewsFeedback({ gameId, payload });
  return apiPost(`/api/v2/games/${gameId}/feedback/news`, payload);
};

export const fetchBatchNewsFeedback = async (gameId, payload) => {
  if (isNative()) return getBridge().fetchBatchNewsFeedback({ gameId, payload });
  return apiPost(`/api/v2/games/${gameId}/feedback/news/batch`, payload);
};

export const fetchCardFeedback = async (gameId, payload) => {
  if (isNative()) return getBridge().fetchCardFeedback({ gameId, payload });
  return apiPost(`/api/v2/games/${gameId}/feedback/card`, payload);
};

export const fetchTurnFeedbackCache = async (gameId, partyId) => {
  if (isNative()) return getBridge().fetchTurnFeedbackCache({ gameId, partyId: partyId || '' });
  return apiGet(`/api/v2/games/${gameId}/feedback/turn-cache`, partyId ? { partyId } : {});
};

// Admin & Definitions API bindings
export const fetchScenarios = async () => {
  if (isNative()) {
    const res = await getBridge().getScenarios();
    return res.data || [];
  }
  return apiGet('/api/admin/scenarios');
};

export const fetchCards = async (scenarioKey) => {
  if (isNative()) {
    const res = await getBridge().getCards({ scenarioKey: scenarioKey || '' });
    return res.data || [];
  }
  return apiGet('/api/admin/cards', scenarioKey ? { scenarioKey } : {});
};

export const fetchNews = async (scenarioKey) => {
  if (isNative()) {
    const res = await getBridge().getNews({ scenarioKey: scenarioKey || '' });
    return res.data || [];
  }
  return apiGet('/api/admin/news', scenarioKey ? { scenarioKey } : {});
};

export const fetchBills = async (scenarioKey) => {
  if (isNative()) {
    const res = await getBridge().getBills({ scenarioKey: scenarioKey || '' });
    return res.data || [];
  }
  return apiGet('/api/admin/bills', scenarioKey ? { scenarioKey } : {});
};

export const fetchFactions = async () => {
  if (isNative()) {
    const res = await getBridge().getFactions();
    return res.data || [];
  }
  return apiGet('/api/admin/factions');
};

export const fetchScenarioProgress = async (userId) => {
  if (isNative()) {
    return getBridge().getScenarioProgress({ userId: userId || '' });
  }
  return apiGet('/api/scenarios/progress', userId ? { userId } : {});
};

export const getFaction = (id) => apiGet(`/api/admin/factions/${id}`);
export const createFaction = (payload) => apiPost('/api/admin/factions', payload);
export const updateFaction = (id, payload) => apiPut(`/api/admin/factions/${id}`, payload);
export const deleteFaction = (id) => apiDelete(`/api/admin/factions/${id}`);

// Auth API bindings (Dual-Mode: Local Room with Secret Question on Native, REST OTP on Web)
export const registerUser = async (payload) => {
  if (isNative()) {
    return getBridge().register(payload);
  }
  return apiPost('/api/auth/register', payload);
};

export const loginUser = async (payload) => {
  if (isNative()) {
    return getBridge().login(payload);
  }
  return apiPost('/api/auth/login', payload);
};

export const getSecretQuestion = async (payload) => {
  if (isNative()) {
    return getBridge().getSecretQuestion(payload);
  }
  return { secretQuestion: 'What is your security question?' };
};

export const resetPasswordWithSecretQuestion = async (payload) => {
  if (isNative()) {
    return getBridge().resetPasswordWithSecretQuestion(payload);
  }
  return { success: true, message: 'Password reset successfully!' };
};

export const requestForgotPasswordOtp = async (payload) => {
  if (isNative()) {
    return getBridge().getSecretQuestion(payload);
  }
  return apiPost('/api/auth/forgot-password', payload);
};

export const resetPasswordWithOtp = async (payload) => {
  if (isNative()) {
    return getBridge().resetPasswordWithSecretQuestion(payload);
  }
  return apiPost('/api/auth/reset-password', payload);
};
