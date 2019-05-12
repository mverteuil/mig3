<template>
  <v-layout column grid-list-lg tag="v-container">
    <v-flex>
      <project-breadcrumb-title />
      <router-view />
    </v-flex>
  </v-layout>
</template>
<script>
import ProjectBreadcrumbTitle from "@/components/ProjectBreadcrumbTitle";
import store from "@/store/store";

export default {
  components: { ProjectBreadcrumbTitle },
  beforeRouteLeave: (to, from, next) => {
    store.dispatch("CLEAR_SELECTED_PROJECT");
    next();
  }
};
</script>
