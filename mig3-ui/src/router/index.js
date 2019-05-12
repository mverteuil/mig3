import Vue from "vue";
import Router from "vue-router";

import BuilderRoutes from "@/router/builders";
import ProjectRoutes from "@/router/project";
import UserRoutes from "@/router/users";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [BuilderRoutes, ProjectRoutes, UserRoutes]
});
