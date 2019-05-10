import Index from "@/views/projects/Index";
import Projects from "@/views/projects/Projects";
import ProjectTarget from "@/views/projects/ProjectTarget";
import ProjectTargets from "@/views/projects/ProjectTargets";
import ProjectTargetBuilds from "@/views/projects/ProjectTargetBuilds";

export default {
  path: "/projects",
  component: Index,
  children: [
    {
      path: "",
      name: "Projects"
    },
    {
      path: ":projectId",
      name: "Project",
      component: () => import(/* webpackChunkName: "project" */ "@/views/projects/Index.vue")
    },
    {
      path: ":projectId/targets/",
      name: "Project.Targets",
      component: () => import(/* webpackChunkName: "projecttarget" */ "@/views/projects/ProjectTarget.vue")
    },
    {
      path: ":projectId/targets/:targetId",
      name: "Project.Target",
      component: () => import(/* webpackChunkName: "projecttarget" */ "@/views/projects/ProjectTarget.vue")
    },
    {
      path: ":projectId/targets/:targetId/builds/",
      name: "Project.Target.Builds",
      component: () => import(/* webpackChunkName: "projecttargetbuilds" */ "@/views/projects/ProjectTargetBuilds.vue")
    },
    {
      path: ":projectId/targets/:targetId/builds/:number",
      name: "Projects.Target.Build",
      component: () => import(/* webpackChunkName: "projecttargetbuilds" */ "@/views/projects/ProjectTargetBuilds.vue")
    }
  ]
};
