import client from "@/services/axios-client";
import template from "lodash.template";

const URLS = {
  BUILD_DETAIL: template("builds/${ buildId }/"),
  BUILDER_DETAIL: template("builders/${ builderId }"),
  BUILDER_LIST: "builders/",
  CURRENT_USER_DETAIL: "users/whoami/",
  INSTALLATION_SETUP_DETAIL: "wizard/installation-setup/",
  PROJECT_DETAIL: template("projects/${ projectId }/"),
  PROJECT_LIST: "projects/",
  PROJECT_TARGET_LIST: template("projects/${ projectId }/targets/"),
  TARGET_DETAIL: template("targets/${ targetId }/"),
  TARGET_LIST: template("targets/"),
  USER_LIST: "users/"
};

export default {
  async getBuildDetails(buildId) {
    return client().get(URLS.BUILD_DETAIL({ buildId }));
  },
  async getBuilderDetails(builderId) {
    return client().get(URLS.BUILDER_DETAIL({ builderId }));
  },
  async getBuilders() {
    return client().get(URLS.BUILDER_LIST);
  },
  async getCurrentUserDetails() {
    return client().get(URLS.CURRENT_USER_DETAIL);
  },
  async getInstallationSetupDetails() {
    return client().get(URLS.INSTALLATION_SETUP_DETAIL);
  },
  async getProjects() {
    return client().get(URLS.PROJECT_LIST);
  },
  async getProjectDetails(projectId) {
    return client().get(URLS.PROJECT_DETAIL({ projectId }));
  },
  async getTargetDetails(targetId) {
    return client().get(URLS.TARGET_DETAIL({ targetId }));
  },
  async getUsers() {
    return client().get(URLS.USER_LIST);
  },
  async postBuilder({ name }) {
    return client().post(URLS.BUILDER_LIST, { name });
  },
  async postProject({ name, repoUrl }) {
    return client().post(URLS.PROJECT_LIST, { name, repo_url: repoUrl });
  },
  async postTarget({
    name,
    projectId,
    python_major_version,
    python_minor_version,
    python_patch_version,
    additional_details
  }) {
    return client().post(URLS.PROJECT_TARGET_LIST({ projectId }), {
      name,
      python_major_version,
      python_minor_version,
      python_patch_version,
      additional_details
    });
  }
};
