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
      commit("RECEIVE_BUILD", response.data);
    }
  },
  mutations: {
    RECEIVE_BUILD(state, payload) {
      const { project, target, ...build } = payload;
      state.selected = { project: project, target: target, build: build };
      router.push({
        name: "Project.Target.Build",
        params: { projectId: payload.project.id, targetId: payload.target.id, buildId: payload.id }
      });
    },
    RECEIVE_PROJECT(state, payload) {
      // eslint-disable-next-line no-console
      const { targets, ...project } = payload;
      state.selected = { project: project, target: null, build: null };
      state.targets = targets;
      router.push({ name: "Project.Targets", params: { projectId: project.id } });
    },
    RECEIVE_PROJECTS(state, payload) {
      state.projects = payload;
    },
    RECEIVE_TARGET(state, payload) {
      const { builds, project, ...target } = payload;
      state.selected = { project: project, target: target, build: null };
      state.builds = builds;
      router.push({ name: "Project.Target.Builds", params: { projectId: project.id, targetId: target.id } });
    }
  }
});
