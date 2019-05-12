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
export default {
  components: { ProjectBreadcrumbTitle }
};
</script>
