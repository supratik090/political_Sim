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
  currentScreen: 'HOME', // 'HOME', 'GAME', 'ADMIN'
  setScreen: (screen) => set({ currentScreen: screen }),

  // Game Session State
  activeGameId: null,
  setActiveGame: (id) => set({ activeGameId: id }),

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
