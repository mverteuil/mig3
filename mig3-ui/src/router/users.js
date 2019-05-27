import { FETCH_USERS } from "@/store/action-types";
import store from "@/store/store";

export default {
  path: "/users/",
  name: "Users",
  component: () => import(/* webpackChunkName: "users" */ "@/views/Users.vue"),
  beforeEnter: async (to, from, next) => {
    await store.dispatch(FETCH_USERS);
    next();
  }
};
