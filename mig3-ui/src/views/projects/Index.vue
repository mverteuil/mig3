<template>
  <v-container fluid>
    <project-breadcrumb-title />
    <router-view />
  </v-container>
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
