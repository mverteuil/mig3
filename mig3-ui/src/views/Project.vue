<template>
  <project-target-list v-if="$route.params.targetId === undefined" />
  <router-view v-else />
</template>
<script>
import ProjectTargetList from "../sections/ProjectTargetList";

export default {
  name: "Project",
  components: { ProjectTargetList },
  data: () => ({
    projects: {
      qL70nKe: {
        name: "Barbara",
        repository_url: "https://github.com/mverteuil/barbara"
      },
      E0lrPbR: {
        name: "mig3-client",
        repository_url: "https://github.com/mverteuil/mig3-client"
      },
      vJ7v5lA: {
        name: "mig3",
        repository_url: "https://github.com/mverteuil/mig3"
      }
    }
  })
};
</script>
