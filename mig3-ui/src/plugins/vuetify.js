import Vue from "vue";
import Vuetify from "vuetify";
import "vuetify/dist/vuetify.min.css";

import "@mdi/font/css/materialdesignicons.css";
import colors from "vuetify/es5/util/colors";

Vue.use(Vuetify, {
  iconfont: "mdi",
  theme: {
    primary: colors.red,
    secondary: colors.indigo.darken4,
    accent: colors.red.accent4
  }
});
