import client from "@/services/axios-client";
import template from "lodash.template";

const URLS = {
  BUILD_DETAIL: template("builds/${ buildId }/"),
  BUILDER_LIST: "builders/",
  INSTALLATION_SETUP_DETAIL: "installation-setup/",
  PROJECT_DETAIL: template("projects/${ projectId }/"),
  PROJECT_LIST: "projects/",
  TARGET_DETAIL: template("targets/${ targetId }/"),
  USER_LIST: "users/"
};

export default {
  async getBuildDetails(buildId) {
    return client().get(URLS.BUILD_DETAIL({ buildId }));
  },
  async getBuilders() {
    return client().get(URLS.BUILDER_LIST);
  },
  async getInstallationSetupDetails() {
    return client().get(URLS.INSTALLATION_SETUP_DETAIL);
  },
  async getProjects() {
    return client().get(URLS.PROJECT_LIST);
  },
  async getProjectDetails(projectId) {
    return client().get(URLS.PROJECT_DETAIL({ projectId: projectId }));
  },
  async getTargetDetails(targetId) {
    return client().get(URLS.TARGET_DETAIL({ targetId }));
  },
  async getUsers() {
    return client().get(URLS.USER_LIST);
  }
};
