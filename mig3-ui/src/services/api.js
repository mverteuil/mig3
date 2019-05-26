import client from "@/services/axios-client";
import template from "lodash.template";

const URLS = {
  BUILD_DETAIL: template("builds/${ buildId }/"),
  BUILDER_DETAIL: template("builders/${ builderId }/"),
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
    return await client().get(URLS.BUILD_DETAIL({ buildId }));
  },
  async getBuilderDetails(builderId) {
    return await client().get(URLS.BUILDER_DETAIL({ builderId }));
  },
  async getBuilders() {
    return await client().get(URLS.BUILDER_LIST);
  },
  async getCurrentUserDetails() {
    return await client().get(URLS.CURRENT_USER_DETAIL);
  },
  async getInstallationSetupDetails() {
    return await client().get(URLS.INSTALLATION_SETUP_DETAIL);
  },
  async getProjects() {
    return await client().get(URLS.PROJECT_LIST);
  },
  async getProjectDetails(projectId) {
    return await client().get(URLS.PROJECT_DETAIL({ projectId }));
  },
  async getTargetDetails(targetId) {
    return await client().get(URLS.TARGET_DETAIL({ targetId }));
  },
  async getUsers() {
    return await client().get(URLS.USER_LIST);
  },
  async postBuilder({ name }) {
    return await client().post(URLS.BUILDER_LIST, { name });
  },
  async postProject({ name, repoUrl }) {
    return await client().post(URLS.PROJECT_LIST, { name, repo_url: repoUrl });
  },
  async postTarget({
    name,
    projectId,
    python_major_version,
    python_minor_version,
    python_patch_version,
    additional_details
  }) {
    return await client().post(URLS.PROJECT_TARGET_LIST({ projectId }), {
      name,
      python_major_version,
      python_minor_version,
      python_patch_version,
      additional_details
    });
  }
};
