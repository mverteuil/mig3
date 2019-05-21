<template>
  <v-stepper-content :step="step">
    <span class="normal">Let's create your first project.</span>
    <v-form ref="form">
      <v-text-field label="Project Name" v-model="projectName"></v-text-field>
      <v-text-field label="Repository URL" v-model="repoUrl" clearable optional></v-text-field>
      <v-btn @click="createProject()">Create Project</v-btn>
    </v-form>
  </v-stepper-content>
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
