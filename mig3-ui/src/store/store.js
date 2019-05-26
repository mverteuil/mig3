import Vue from "vue";
import Vuex from "vuex";
import apiClient from "@/services/api";
import {
  SELECT_BUILDER,
  RECEIVE_BUILDERS,
  RECEIVE_BUILDS,
  RECEIVE_CURRENT_USER,
  RECEIVE_INSTALLATION_SETUP_DETAILS,
  SELECT_PROJECT,
  RECEIVE_PROJECTS,
  SELECT_TARGET,
  RECEIVE_TARGETS,
  RECEIVE_USERS,
  SELECT_BUILD,
  SELECT_NONE
} from "@/store/mutation-types";
import {
  CLEAR_SELECTED_PROJECT,
  CREATE_BUILDER,
  CREATE_PROJECT,
  CREATE_TARGET,
  FETCH_BUILD,
  FETCH_BUILDER,
  FETCH_BUILDERS,
  FETCH_CURRENT_USER,
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
    currentUser: {
      name: null,
      email: null,
      builds: 0,
      is_administrator: false
    },
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
      initial_builder: null,
      initial_project: null,
      current_requirement_index: 0,
      satisfied_requirements_percentage: 0,
      is_complete: false
    }
  },
  getters: {
    currentInstallationStep: state => {
      return state.installationSetup.current_requirement_index + 1;
    },
    initialBuilder: state => {
      return state.installationSetup.initial_builder;
    },
    initialProject: state => {
      return state.installationSetup.initial_project;
    },
    initialTargets: state => {
      return state.installationSetup.initial_project.targets;
    }
  },
  actions: {
    async [CLEAR_SELECTED_PROJECT]({ commit }) {
      commit(SELECT_BUILD, {});
    },
    async [CREATE_BUILDER]({ commit }, { name }) {
      let response = await apiClient.postBuilder({ name });
      await commit(SELECT_BUILDER, response.data);
    },
    async [CREATE_PROJECT]({ commit }, { name, repoUrl }) {
      let response = await apiClient.postProject({ name, repoUrl });
      const { ...project } = response.data;
      await commit(SELECT_PROJECT, project);
      await commit(SELECT_BUILD, { project });
    },
    async [CREATE_TARGET](
      { commit },
      { name, python_major_version, python_minor_version, python_patch_version, additional_details, project }
    ) {
      let response = await apiClient.postTarget({
        name,
        python_major_version,
        python_minor_version,
        python_patch_version,
        additional_details,
        projectId: project.id
      });
      const { ...target } = response.data;
      await commit(SELECT_TARGET, target, project);
    },
    async [FETCH_BUILD]({ commit }, { id }) {
      let response = await apiClient.getBuildDetails(id);
      const { project, target, ...build } = response.data;
      await commit(SELECT_BUILD, { project, target, build });
    },
    async [FETCH_BUILDER]({ commit }, { id }) {
      let response = await apiClient.getBuilderDetails(id);
      await commit(SELECT_BUILDER, response.data);
    },
    async [FETCH_BUILDERS]({ commit }) {
      let response = await apiClient.getBuilders();
      await commit(RECEIVE_BUILDERS, response.data);
    },
    async [FETCH_CURRENT_USER]({ commit }) {
      let response = await apiClient.getCurrentUserDetails();
      await commit(RECEIVE_CURRENT_USER, response.data);
    },
    async [FETCH_INSTALLATION_SETUP_DETAILS]({ commit }) {
      let response = await apiClient.getInstallationSetupDetails();
      await commit(RECEIVE_INSTALLATION_SETUP_DETAILS, response.data);
      return true;
    },
    async [FETCH_PROJECT]({ commit }, { id }) {
      let response = await apiClient.getProjectDetails(id);
      const { targets, ...project } = response.data;
      await commit(RECEIVE_TARGETS, targets);
      await commit(SELECT_PROJECT, project);
    },
    async [FETCH_PROJECTS]({ commit }) {
      let response = await apiClient.getProjects();
      await commit(SELECT_NONE);
      await commit(RECEIVE_PROJECTS, response.data);
    },
    async [FETCH_TARGET]({ commit }, { id }) {
      let response = await apiClient.getTargetDetails(id);
      const { builds, project, ...target } = response.data;
      await commit(RECEIVE_BUILDS, builds);
      await commit(SELECT_TARGET, { project, target });
    },
    async [FETCH_USERS]({ commit }) {
      let response = await apiClient.getUsers();
      await commit(RECEIVE_USERS, response.data);
    }
  },
  mutations: {
    [RECEIVE_BUILDS](state, payload) {
      state.builds = payload;
    },
    [RECEIVE_BUILDERS](state, payload) {
      state.builders = payload;
    },
    [RECEIVE_CURRENT_USER](state, payload) {
      state.currentUser = payload;
    },
    [RECEIVE_INSTALLATION_SETUP_DETAILS](state, payload) {
      state.installationSetup = payload;
    },
    [RECEIVE_PROJECTS](state, payload) {
      state.projects = payload;
    },
    [RECEIVE_TARGETS](state, payload) {
      state.targets = payload;
    },
    [RECEIVE_USERS](state, payload) {
      state.users = payload;
    },
    [SELECT_BUILD](state, { build, project, target }) {
      state.selected.project = project;
      state.selected.target = target;
      state.selected.build = build;
    },
    [SELECT_BUILDER](state, builder) {
      state.selected.builder = builder;
    },
    [SELECT_NONE](state) {
      state.selected = { builder: null, build: null, target: null, project: null };
    },
    [SELECT_PROJECT](state, project) {
      state.selected.project = project;
    },
    [SELECT_TARGET](state, { project, target }) {
      state.selected.project = project;
      state.selected.target = target;
    }
  }
});
