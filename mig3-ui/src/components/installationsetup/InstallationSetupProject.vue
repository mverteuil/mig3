<template lang="pug">
  v-stepper-content(:step="step")
    v-container(fluid)
      v-layout
        v-flex(xs12)
          v-subheader Let's get started by creating a project.
      v-layout(row)
        v-flex(xs4)
          v-container
            v-layout(row wrap)
              v-flex(xs12)
                v-text-field(label="Project Name" v-model="projectName")
                v-text-field(label="Repository URL" v-model="repoUrl" clearable optional)
                v-btn(@click="createProject()" class="ml-0" v-if="!loading") Create Project
                v-progress-circular(indeterminate v-else)
</template>
<script>
import { CREATE_PROJECT, FETCH_INSTALLATION_SETUP_DETAILS } from "@/store/action-types";

export default {
  name: "InstallationSetupBuilder",
  props: ["step"],
  data: () => ({
    projectName: "",
    repoUrl: "https://github.com/you/yourproject/",
    progress: false
  }),
  methods: {
    createProject() {
      this.progress = true;
      this.$store
        .dispatch(CREATE_PROJECT, { name: this.projectName, repoUrl: this.repoUrl })
        .then(() => {
          this.$store.dispatch(FETCH_INSTALLATION_SETUP_DETAILS).finally(() => {
            this.progress = false;
          });
        })
        .finally(() => {
          this.progress = false;
        });
    }
  }
};
</script>
<style scoped></style>
