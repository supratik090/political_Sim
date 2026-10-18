import { create } from 'zustand';

export const useGameStore = create((set, get) => ({
  // Authentication State
  user: JSON.parse(localStorage.getItem('political_sim_user_cache') || 'null')?.user || null,
  login: (userData) => {
    const payload = { user: userData, expiresAt: Date.now() + 5 * 24 * 60 * 60 * 1000 };
    localStorage.setItem('political_sim_user_cache', JSON.stringify(payload));
    set({ user: userData });
  },
  logout: () => {
    localStorage.removeItem('political_sim_user_cache');
    set({ user: null, activeGameId: null, turnData: null });
  },

  // Application Routing State
  currentScreen: 'HOME', // 'HOME', 'GAME', 'ADMIN', 'NATIONAL'
  setScreen: (screen) => set({ currentScreen: screen }),
  activeGameView: 'ACTION', // 'ACTION', 'INFO', 'HINTS'
  setActiveGameView: (view) => set({ activeGameView: view }),

  // National Politics Mode Navigation
  activeNationalTab: 'intelligence', // 'intelligence', 'operations', 'hints'
  setActiveNationalTab: (tab) => set({ activeNationalTab: tab }),
  nationalView: 'HEADQUARTERS', // 'HEADQUARTERS', 'CREATE_GAME', 'WAR_ROOM'
  setNationalView: (view) => set({ nationalView: view }),

  // Game Session State
  activeGameId: null,
  setActiveGame: (id) => set({ activeGameId: id }),

  // National Politics Mode Game State (Scoped per game ID)
  activeNationalGame: (() => {
    try {
      const activeGameId = localStorage.getItem('political_sim_active_national_game_id');
      if (activeGameId) {
        const gameById = localStorage.getItem(`political_sim_national_game_${activeGameId}`);
        if (gameById) return JSON.parse(gameById);
      }
      return JSON.parse(localStorage.getItem('political_sim_national_game_cache') || 'null');
    } catch (e) {
      return null;
    }
  })(),
  setActiveNationalGame: (gameData) => {
    if (!gameData) {
      localStorage.removeItem('political_sim_active_national_game_id');
      localStorage.removeItem('political_sim_national_game_cache');
      set({ activeNationalGame: null });
      return;
    }
    const gameId = gameData.id || gameData._id;
    if (gameId) {
      localStorage.setItem(`political_sim_national_game_${gameId}`, JSON.stringify(gameData));
      localStorage.setItem('political_sim_active_national_game_id', gameId);
    }
    localStorage.setItem('political_sim_national_game_cache', JSON.stringify(gameData));
    set({ activeNationalGame: gameData });
  },
  clearActiveNationalGame: (gameId) => {
    if (gameId) {
      localStorage.removeItem(`political_sim_national_game_${gameId}`);
    }
    const currentActiveId = localStorage.getItem('political_sim_active_national_game_id');
    if (!gameId || currentActiveId === gameId) {
      localStorage.removeItem('political_sim_active_national_game_id');
      localStorage.removeItem('political_sim_national_game_cache');
    }
    set({ activeNationalGame: null });
  },

  // Turn State
  turnData: null,          // Fetched once at the start of the turn
  localDecisions: {        // User interactions tracked locally
    selectedNewsOptions: {}, // { newsKey: optionKey }
    selectedCard: null,
    targetPartyId: null,
    bidAmount: 0,
    isDone: false,           // To show "Done" tick on actions
  },
  
  // Actions to mutate local turn state
  setTurnData: (data) => set({ turnData: data, localDecisions: { selectedNewsOptions: {}, selectedCard: null, targetPartyId: null, bidAmount: 0, isDone: false } }),

  // Multiplayer timer (shared so top-nav can display countdown)
  timeLeft: null,
  setTimeLeft: (t) => set({ timeLeft: t }),

  
  selectNewsOption: (newsKey, optionKey) => set((state) => ({
    localDecisions: {
      ...state.localDecisions,
      selectedNewsOptions: {
        ...state.localDecisions.selectedNewsOptions,
        [newsKey]: optionKey
      }
    }
  })),

  selectCard: (cardKey, targetPartyId = null) => set((state) => ({
    localDecisions: { ...state.localDecisions, selectedCard: cardKey, targetPartyId }
  })),

  setBidAmount: (amount) => set((state) => ({
    localDecisions: { ...state.localDecisions, bidAmount: amount }
  })),

  markTurnDone: () => set((state) => ({
    localDecisions: { ...state.localDecisions, isDone: true }
  })),
  
  submitTurn: async () => {
    const { activeGameId, localDecisions } = get();
    // In real app, make REST POST call here
    console.log("Submitting Turn Data", { activeGameId, localDecisions });
    // After successful submit, maybe clear local decisions and wait for next turnData fetch
  }
}));
