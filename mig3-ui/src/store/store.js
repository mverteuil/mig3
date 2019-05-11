import Vue from "vue";
import Vuex from "vuex";
import router from "@/router/index";
import apiClient from "@/services/api";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    builds: [],
    builders: [],
    projects: [],
    targets: [],
    users: [],
    selected: {
      project: null,
      target: null,
      build: null
    }
  },
  actions: {
    async FETCH_PROJECTS({ commit }) {
      let response = await apiClient.getProjects();
      commit("RECEIVE_PROJECTS", response.data);
    },
    async FETCH_PROJECT({ commit }, { id }) {
      let response = await apiClient.getProjectDetails(id);
      commit("RECEIVE_PROJECT", response.data);
    },
    async FETCH_TARGET({ commit }, { id }) {
      let response = await apiClient.getTargetDetails(id);
      commit("RECEIVE_TARGET", response.data);
    },
    async FETCH_BUILD({ commit }, { id }) {
      let response = await apiClient.getBuildDetails(id);
      commit("RECEIVE_TARGET", response.data);
    }
  },
  mutations: {
    RECEIVE_BUILD(state, payload) {
      state.selected = { project: payload.project, target: payload.target, build: payload };
      router.push({
        name: "Project.Target.Build",
        params: { projectId: payload.project.id, targetId: payload.target.id, buildId: payload.id }
      });
    },
    RECEIVE_PROJECT(state, payload) {
      // eslint-disable-next-line no-console
      console.log(payload);
      state.selected = { project: payload, target: null, build: null };
      state.targets = payload.targets;
      router.push({ name: "Project.Targets", params: { projectId: payload.id } });
    },
    RECEIVE_PROJECTS(state, payload) {
      state.projects = payload;
    },
    RECEIVE_TARGET(state, payload) {
      state.selected = { project: payload.project, target: payload, build: null };
      state.builds = payload.builds;
      router.push({ name: "Project.Target.Builds", params: { projectId: payload.project.id, targetId: payload.id } });
    }
  }
});
