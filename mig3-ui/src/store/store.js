import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    selectedProject: null,
    selectedTarget: null
  },
  mutations: {
    SET_SELECTED_PROJECT({ commit }, projectId) {
      return new Promise((resolve, reject) => {});
    }
  }
});
