import Index from "@/views/projects/Index";
import store from "@/store/store";
import { FETCH_PROJECTS, FETCH_USERS } from "@/store/action-types";

export default {
  path: "/projects/",
  component: Index,
  children: [
    {
      path: "",
      name: "Projects",
      component: () => import(/* webpackChunkName: "projects" */ "@/views/projects/Projects.vue"),
      beforeEnter: async (to, from, next) => {
        await store.dispatch(FETCH_PROJECTS);
        next();
      }
    },
    {
      path: ":projectId/targets/",
      name: "Project.Targets",
      component: () => import(/* webpackChunkName: "projecttargets" */ "@/views/projects/ProjectTargets.vue")
    },
    {
      path: ":projectId/targets/:targetId/builds/",
      name: "Project.Target.Builds",
      component: () => import(/* webpackChunkName: "projecttargetbuilds" */ "@/views/projects/ProjectTargetBuilds.vue")
    },
    {
      path: ":projectId/targets/:targetId/builds/:buildId/",
      name: "Project.Target.Build",
      component: () => import(/* webpackChunkName: "projecttargetbuild" */ "@/views/projects/ProjectTargetBuild.vue")
    }
  ]
};
