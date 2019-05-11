import Index from "@/views/projects/Index";

export default {
  path: "/projects/",
  component: Index,
  children: [
    {
      path: "",
      name: "Projects",
      component: () => import(/* webpackChunkName: "projects" */ "@/views/projects/Projects.vue")
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
