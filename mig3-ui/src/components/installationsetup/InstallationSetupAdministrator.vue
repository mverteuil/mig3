<template>
  <v-stepper-content :step="step" tag="v-container">You are {{ currentUser.name }}</v-stepper-content>
</template>
<script>
import { mapState } from "vuex";

export default {
  name: "InstallationWizardAdministrator",
  computed: {
    ...mapState(["currentUser"])
  },
  props: ["step"]
};
</script>
<style scoped></style>
