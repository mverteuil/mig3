<template>
  <v-app dark>
    <app-navigation></app-navigation>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>
<script>
import AppNavigation from "@/components/AppNavigation";
import { FETCH_CURRENT_USER, FETCH_INSTALLATION_SETUP_DETAILS } from "@/store/action-types";

export default {
  name: "App",
  components: { AppNavigation },
  mounted() {
    this.$store.dispatch(FETCH_INSTALLATION_SETUP_DETAILS).then(() => this.$store.dispatch(FETCH_CURRENT_USER));
  }
};
</script>
<style></style>
