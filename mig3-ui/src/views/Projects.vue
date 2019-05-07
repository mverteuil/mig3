<template>
  <project-list v-if="!$route.params.projectId" />
  <router-view v-else />
</template>
<script>
import ProjectList from "@/components/ProjectList";

export default {
  components: { ProjectList }
};
</script>
