<template>
  <project-target-build-list v-if="!$route.params.buildId" />
  <project-target-build-detail v-else />
</template>
<script>
import ProjectTargetBuildDetail from "@/components/ProjectTargetBuildDetail";
import ProjectTargetBuildList from "@/components/ProjectTargetBuildList";

export default {
  components: {
    ProjectTargetBuildDetail,
    ProjectTargetBuildList
  }
};
</script>
