import Vue from "vue";
import Router from "vue-router";

import BuilderRoutes from "@/router/builders";
import ProjectRoutes from "@/router/project";
import UserRoutes from "@/router/users";
import WizardRoutes from "@/router/wizard";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "root",
      redirect: { name: "InstallationSetupWizard" }
    },
    BuilderRoutes,
    ProjectRoutes,
    UserRoutes,
    WizardRoutes,
    {
      path: "*",
      name: "catch-all",
      redirect: { name: "root" }
    }
  ]
});
