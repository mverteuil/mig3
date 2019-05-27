import Index from "@/views/projects/Index";
import store from "@/store/store";
import { FETCH_BUILD, FETCH_PROJECT, FETCH_PROJECTS, FETCH_TARGET } from "@/store/action-types";

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
      component: () => import(/* webpackChunkName: "projecttargets" */ "@/views/projects/ProjectTargets.vue"),
      beforeEnter: async (to, from, next) => {
        await store.dispatch(FETCH_PROJECT, { id: to.params.projectId });
        next();
      }
    },
    {
      path: ":projectId/targets/:targetId/builds/",
      name: "Project.Target.Builds",
      component: () => import(/* webpackChunkName: "projecttargetbuilds" */ "@/views/projects/ProjectTargetBuilds.vue"),
      beforeEnter: async (to, from, next) => {
        await store.dispatch(FETCH_TARGET, { id: to.params.targetId });
        next();
      }
    },
    {
      path: ":projectId/targets/:targetId/builds/:buildId/",
      name: "Project.Target.Build",
      component: () => import(/* webpackChunkName: "projecttargetbuild" */ "@/views/projects/ProjectTargetBuild.vue"),
      beforeEnter: async (to, from, next) => {
        await store.dispatch(FETCH_BUILD, { id: to.params.buildId });
        next();
      }
    }
  ]
};
