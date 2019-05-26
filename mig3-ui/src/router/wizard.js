import store from "@/store/store";
import { FETCH_INSTALLATION_SETUP_DETAILS } from "@/store/action-types";

export default {
  path: "/installation-setup/",
  name: "InstallationSetupWizard",
  component: () => import(/* webpackChunkName: "installationsetup" */ "@/views/InstallationSetupWizard.vue"),
  beforeEnter: async (to, from, next) => {
    await store.dispatch(FETCH_INSTALLATION_SETUP_DETAILS);
    if (!store.state.installationSetup.is_complete) {
      next();
    } else {
      next({ name: "Projects" });
    }
  }
};
