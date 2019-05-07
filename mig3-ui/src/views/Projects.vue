<template>
  <project-list v-if="$route.params.projectId === undefined" />
  <router-view v-else />
</template>
<script>
import ProjectList from "@/components/ProjectList";

export default {
  components: { ProjectList }
};
</script>
