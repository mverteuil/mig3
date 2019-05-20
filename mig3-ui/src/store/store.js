import Vue from "vue";
import Vuex from "vuex";
import apiClient from "@/services/api";
import {
  RECEIVE_BUILDER,
  RECEIVE_BUILDERS,
  RECEIVE_BUILDS,
  RECEIVE_INSTALLATION_SETUP_DETAILS,
  RECEIVE_PROJECT,
  RECEIVE_PROJECTS,
  RECEIVE_TARGET,
  RECEIVE_TARGETS,
  RECEIVE_USERS,
  SET_SELECTED
} from "@/store/mutation-types";
import {
  CLEAR_SELECTED_PROJECT,
  CREATE_BUILDER,
  FETCH_BUILD,
  FETCH_BUILDERS,
  FETCH_INSTALLATION_SETUP_DETAILS,
  FETCH_PROJECT,
  FETCH_PROJECTS,
  FETCH_TARGET,
  FETCH_USERS
} from "@/store/action-types";

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
    },
    installationSetup: {
      requirements: [{ condition_name: "Active Administrator", is_satisfied: false, id: "Administrator" }],
      current_requirement_index: 0,
      satisfied_requirements_percentage: 0,
      is_complete: false
    }
  },
  actions: {
    [CLEAR_SELECTED_PROJECT]({ commit }) {
      commit(SET_SELECTED, {});
    },
    async [CREATE_BUILDER]({ commit }, { name }) {
      let response = await apiClient.postBuilder({ name });
      commit(RECEIVE_BUILDER, response.data);
    },
    async [FETCH_BUILD]({ commit }, { id }) {
      let response = await apiClient.getBuildDetails(id);
      const { project, target, ...build } = response.data;
      commit(SET_SELECTED, { project, target, build });
    },
    async [FETCH_BUILDERS]({ commit }) {
      let response = await apiClient.getBuilders();
      commit(RECEIVE_BUILDERS, response.data);
    },
    async [FETCH_INSTALLATION_SETUP_DETAILS]({ commit }) {
      let response = await apiClient.getInstallationSetupDetails();
      commit(RECEIVE_INSTALLATION_SETUP_DETAILS, response.data);
    },
    async [FETCH_PROJECT]({ commit }, { id }) {
      let response = await apiClient.getProjectDetails(id);
      const { targets, ...project } = response.data;
      commit(RECEIVE_TARGETS, targets);
      commit(SET_SELECTED, { project });
    },
    async [FETCH_PROJECTS]({ commit }) {
      let response = await apiClient.getProjects();
      commit(SET_SELECTED, {});
      commit(RECEIVE_PROJECTS, response.data);
    },
    async [FETCH_TARGET]({ commit }, { id }) {
      let response = await apiClient.getTargetDetails(id);
      const { builds, project, ...target } = response.data;
      commit(RECEIVE_BUILDS, builds);
      commit(SET_SELECTED, { project, target });
    },
    async [FETCH_USERS]({ commit }) {
      let response = await apiClient.getUsers();
      commit(RECEIVE_USERS, response.data);
    }
  },
  mutations: {
    [RECEIVE_BUILDS](state, payload) {
      state.builds = payload;
    },
    [RECEIVE_BUILDER](state, payload) {
      state.builders.append(payload);
    },
    [RECEIVE_BUILDERS](state, payload) {
      state.builders = payload;
    },
    [RECEIVE_INSTALLATION_SETUP_DETAILS](state, payload) {
      state.installationSetup = payload;
    },
    [RECEIVE_PROJECT](state, payload) {
      state.projects.append(payload);
    },
    [RECEIVE_PROJECTS](state, payload) {
      state.projects = payload;
    },
    [RECEIVE_TARGET](state, payload) {
      state.targets.append(payload);
    },
    [RECEIVE_TARGETS](state, payload) {
      state.targets = payload;
    },
    [RECEIVE_USERS](state, payload) {
      state.users = payload;
    },
    [SET_SELECTED](state, { project, target, build }) {
      state.selected = { project: project, target: target, build: build };
    }
  }
});
