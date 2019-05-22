<template lang="pug">
  v-stepper-content(:step="step")
    v-container(fluid)
      v-layout
        v-flex(xs12)
          v-subheader Let's get started by creating a project.
      v-layout(row)
        v-flex(xs4)
          v-container
            v-layout row wrap
              v-flex(xs12)
                v-text-field(label="Project Name" v-model="projectName")
                v-text-field(label="Repository URL" v-model="repoUrl" clearable optional)
</template>
<script>
import { CREATE_PROJECT } from "@/store/action-types";

export default {
  name: "InstallationSetupBuilder",
  props: ["step"],
  data: () => ({
    projectName: "",
    repoUrl: "https://github.com/you/yourproject/"
  }),
  methods: {
    createProject() {
      this.$store.dispatch(CREATE_PROJECT, { name: this.projectName, repoUrl: this.repoUrl });
    }
  }
};
</script>
<style scoped></style>
