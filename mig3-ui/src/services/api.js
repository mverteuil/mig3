import client from "@/services/axios-client";
import template from "lodash.template";

const URLS = {
  GET_BUILD_DETAILS: template("builds/${ buildId }/"),
  GET_PROJECTS: "projects/",
  GET_PROJECT_DETAILS: template("projects/${ projectId }/"),
  GET_TARGET_DETAILS: template("targets/${ targetId }/")
};

export default {
  async getBuildDetails(buildId) {
    return client().get(URLS.GET_BUILD_DETAILS({ buildId }));
  },
  async getTargetDetails(targetId) {
    return client().get(URLS.GET_TARGET_DETAILS({ targetId }));
  },
  async getProjects() {
    return client().get(URLS.GET_PROJECTS);
  },
  async getProjectDetails(projectId) {
    return client().get(URLS.GET_PROJECT_DETAILS({ projectId: projectId }));
  }
};
