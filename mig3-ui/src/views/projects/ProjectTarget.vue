<template>
  <router-view v-else />
</template>
<script>
import ProjectTargetBuildList from "../../sections/ProjectTargetBuildList";

export default {
  components: { ProjectTargetBuildList },
  data: () => ({
    projectName: "barbara",
    targets: {
      qL70nKe: {
        name: "python3.8",
        python_major_version: 3,
        python_minor_version: 8,
        python_patch_version: 0,
        additional_details: "",
        full_version: "3.8.0",
        python_version: "3.8.0"
      }
    }
  })
};
</script>
