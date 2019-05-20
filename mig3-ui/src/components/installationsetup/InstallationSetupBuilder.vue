<template>
  <v-stepper-content :step="step">
    <v-form>
      <v-text-field v-model="builderName"></v-text-field>
    </v-form>
  </v-stepper-content>
</template>
<script>
export default {
  name: "InstallationSetupBuilder",
  props: ["step"],
  data: () => ({
    builderName: ""
  })
};
</script>
<style scoped></style>
