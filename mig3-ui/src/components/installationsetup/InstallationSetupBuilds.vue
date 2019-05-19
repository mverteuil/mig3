<template>
  <v-stepper-content :step="step">Computer says no</v-stepper-content>
</template>
<script>
export default {
  name: "InstallationSetupBuilds",
  props: ["step"]
};
</script>
<style scoped></style>
