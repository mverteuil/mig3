import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: "",
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/targets/:id?",
      name: "targets",
      component: () =>
        import(/* webpackChunkName: "project" */ "./views/Target.vue")
    },
    {
      path: "/projects/:id?",
      name: "projects",
      component: () =>
        import(/* webpackChunkName: "project" */ "./views/Project.vue")
    }
  ]
});
