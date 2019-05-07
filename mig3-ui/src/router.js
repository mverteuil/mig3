import Vue from "vue";
import Router from "vue-router";
import Projects from "./views/Projects";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: "",
  routes: [
    {
      path: "/",
      name: "home",
      component: Projects
    },
    {
      path: "/builder-accounts/:builderAccountId?",
      name: "builderAccounts",
      component: () =>
        import(
          /* webpackChunkName: "builderaccounts" */ "@/views/BuilderAccounts.vue"
        )
    },
    {
      path: "/projects",
      name: "projects",
      component: () =>
        import(/* webpackChunkName: "projects" */ "@/views/Projects.vue"),
      children: [
        {
          path: ":projectId",
          name: "project",
          component: () =>
            import(/* webpackChunkName: "project" */ "@/views/Project.vue")
        },
        {
          path: ":projectId/targets",
          name: "targets",
          component: () =>
            import(
              /* webpackChunkName: "projecttargets" */ "@/views/ProjectTargets.vue"
            ),
          children: [
            {
              path: ":targetId",
              name: "target",
              component: () =>
                import(
                  /* webpackChunkName: "projecttarget" */ "@/views/ProjectTarget.vue"
                )
            },
            {
              path: ":targetId/builds",
              name: "builds",
              component: () =>
                import(
                  /* webpackChunkName: "projecttargetbuilds" */ "@/views/ProjectTarget.vue"
                )
            },
            {
              path: ":targetId/builds/:buildId",
              name: "build",
              component: () =>
                import(
                  /* webpackChunkName: "projecttargetbuild" */ "@/views/ProjectTargetBuild.vue"
                )
            }
          ]
        }
      ]
    },
    {
      path: "/user-accounts/:userAccountId?",
      name: "userAccounts",
      component: () =>
        import(
          /* webpackChunkName: "useraccounts" */ "@/views/UserAccounts.vue"
        )
    }
  ]
});
