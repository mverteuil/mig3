<template>
  <v-app>
    <app-navigation></app-navigation>
    <v-content>
      <router-view transition="slide-x-transition"></router-view>
    </v-content>
  </v-app>
</template>
<script>
import AppNavigation from "@/components/AppNavigation";

export default {
  name: "App",
  components: { AppNavigation }
};
</script>
<style></style>
