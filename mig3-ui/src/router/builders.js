import store from "@/store/store";
import { FETCH_BUILDERS } from "@/store/action-types";

export default {
  path: "/builders/",
  name: "Builders",
  component: () => import(/* webpackChunkName: "builders" */ "@/views/Builders.vue"),
  beforeEnter: async (to, from, next) => {
    await store.dispatch(FETCH_BUILDERS);
    next();
  }
};
