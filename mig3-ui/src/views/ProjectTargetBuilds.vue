<template>
  <project-target-build-list v-if="!$route.params.buildId" />
  <project-target-build-detail v-else />
</template>
<script>
import ProjectTargetBuildDetail from "@/sections/ProjectTargetBuildDetail";
import ProjectTargetBuildList from "@/sections/ProjectTargetBuildList";

export default {
  components: {
    ProjectTargetBuildDetail,
    ProjectTargetBuildList
  }
};
</script>
