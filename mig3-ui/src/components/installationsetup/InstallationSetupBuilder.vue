<template>
  <v-stepper-content :step="step">
    <span class="normal">Which CI service do you use to run your tests?</span>
    <v-form>
      <v-combobox v-model="builderName" :items="ciServices" label="CI Service"></v-combobox>
      <v-btn @click="createBuilder()">Create</v-btn>
    </v-form>
  </v-stepper-content>
</template>
<script>
import { CREATE_BUILDER } from "@/store/action-types";

export default {
  name: "InstallationSetupBuilder",
  props: ["step"],
  data: () => ({
    builderName: "",
    ciServices: ["CircleCI", "Gitlab", "Go.CD", "Jenkins", "TeamCity", "Travis"]
  }),
  methods: {
    createBuilder() {
      this.$store.dispatch(CREATE_BUILDER, { name: this.builderName });
    }
  }
};
</script>
<style scoped></style>
