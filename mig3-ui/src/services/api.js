import client from "@/services/axios-client";
import template from "lodash.template";

client.inter;

const URLS = {
  GET_BUILD_DETAILS: template("builds/${ buildId }/"),
  GET_BUILDERS: "builders/",
  GET_PROJECTS: "projects/",
  GET_PROJECT_DETAILS: template("projects/${ projectId }/"),
  GET_TARGET_DETAILS: template("targets/${ targetId }/"),
  GET_USERS: "users/"
};

export default {
  async getBuildDetails(buildId) {
    return client().get(URLS.GET_BUILD_DETAILS({ buildId }));
  },
  async getBuilders() {
    return client().get(URLS.GET_BUILDERS);
  },
  async getProjects() {
    return client().get(URLS.GET_PROJECTS);
  },
  async getProjectDetails(projectId) {
    return client().get(URLS.GET_PROJECT_DETAILS({ projectId: projectId }));
  },
  async getTargetDetails(targetId) {
    return client().get(URLS.GET_TARGET_DETAILS({ targetId }));
  },
  async getUsers() {
    return client().get(URLS.GET_USERS);
  }
};
