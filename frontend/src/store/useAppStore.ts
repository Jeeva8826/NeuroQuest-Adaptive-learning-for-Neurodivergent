import { create } from 'zustand';

interface AppState {
  currentMission: string;
  masteryPoints: number;
  focusQuestActive: boolean;
  setFocusQuest: (active: boolean) => void;
  addMasteryPoints: (points: number) => void;
}

export const useAppStore = create<AppState>((set) => ({
  currentMission: 'Explore the Solar System',
  masteryPoints: 120,
  focusQuestActive: false,
  setFocusQuest: (active) => set({ focusQuestActive: active }),
  addMasteryPoints: (points) => set((state) => ({ masteryPoints: state.masteryPoints + points })),
}));
