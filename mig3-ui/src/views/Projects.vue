<template>
  <project-detail v-if="$route.params.id" />
  <project-list v-else />
</template>

<script>
import ProjectDetail from "@/components/ProjectDetail";
import ProjectList from "@/components/ProjectList";

export default {
  components: { ProjectDetail, ProjectList }
};
</script>
