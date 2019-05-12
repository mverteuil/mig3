export default {
  path: "/users/",
  name: "Users",
  component: () => import(/* webpackChunkName: "users" */ "@/views/Users.vue")
};
