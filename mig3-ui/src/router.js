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
      path: "/targets/:id",
      name: "targets",
      component: () =>
        import(/* webpackChunkName: "targets" */ "@/views/Targets.vue")
    },
    {
      path: "/projects/:id?",
      name: "projects",
      component: () =>
        import(/* webpackChunkName: "projects" */ "@/views/Projects.vue")
    },
    {
      path: "/users/:id?",
      name: "users",
      component: () =>
        import(
          /* webpackChunkName: "useraccounts" */ "@/views/UserAccounts.vue"
        )
    }
  ]
});
