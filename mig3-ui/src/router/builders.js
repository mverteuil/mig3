export default {
  path: "/builders/",
  name: "Builders",
  component: () => import(/* webpackChunkName: "builders" */ "@/views/Builders.vue")
};
