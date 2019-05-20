<template>
  <v-stepper-content :step="step">
    <span class="normal">Which CI service do you use to run your tests?</span>
    <v-form>
      <v-combobox :items="ciServices" label="CI Service"></v-combobox>
      <v-btn justify-end>Create</v-btn>
    </v-form>
  </v-stepper-content>
</template>
<script>
export default {
  name: "InstallationSetupBuilder",
  props: ["step"],
  data: () => ({
    ciServices: ["CircleCI", "Gitlab", "Go.CD", "Jenkins", "TeamCity", "Travis"]
  })
};
</script>
<style scoped></style>
