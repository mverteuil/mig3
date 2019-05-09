<template>
  <project-list v-if="!$route.params.projectId" />
  <router-view v-else />
</template>
<script>
import ProjectList from "@/sections/ProjectList";

export default {
  components: { ProjectList }
};
</script>
