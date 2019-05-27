import store from "@/store/store";
import { FETCH_INSTALLATION_SETUP_DETAILS } from "@/store/action-types";

export default {
  path: "/installation-setup/",
  name: "InstallationSetupWizard",
  component: () => import(/* webpackChunkName: "installationsetup" */ "@/views/InstallationSetupWizard.vue"),
  beforeEnter: async (to, from, next) => {
    let redirectTo = null;
    try {
      await store.dispatch(FETCH_INSTALLATION_SETUP_DETAILS);
      if (store.state.installationSetup.is_complete) {
        redirectTo = { name: "Projects" };
      }
    } catch (err) {
      redirectTo = { name: "Projects" };
    }
    next(redirectTo);
  }
};
