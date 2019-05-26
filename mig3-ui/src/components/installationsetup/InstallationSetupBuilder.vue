<template>
  <v-stepper-content :step="step">
    <span class="normal">Which CI service do you use to run your tests?</span>
    <v-form>
      <v-combobox v-model="builderName" :items="ciServices" label="CI Service"></v-combobox>
      <v-btn @click="createBuilder()">Create Builder</v-btn>
    </v-form>
  </v-stepper-content>
</template>
<script>
import { CREATE_BUILDER, FETCH_INSTALLATION_SETUP_DETAILS } from "@/store/action-types";

export default {
  name: "InstallationSetupBuilder",
  props: ["step"],
  data: () => ({
    builderName: "",
    ciServices: ["CircleCI", "Gitlab", "Go.CD", "Jenkins", "TeamCity", "Travis"]
  }),
  methods: {
    async createBuilder() {
      await this.$store.dispatch(CREATE_BUILDER, { name: this.builderName });
      await this.$store.dispatch(FETCH_INSTALLATION_SETUP_DETAILS);
    }
  }
};
</script>
