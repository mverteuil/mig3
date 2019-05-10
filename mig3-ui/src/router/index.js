import Vue from "vue";
import Router from "vue-router";

import BuilderAccountRoutes from "@/router/builder-account";
import ProjectRoutes from "@/router/project";
import UserAccountRoutes from "@/router/user-account";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [BuilderAccountRoutes, ProjectRoutes, UserAccountRoutes]
});
