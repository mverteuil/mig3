<template>
  <v-stepper v-model="currentRequirementIndex">
    <v-stepper-header>
      <v-progress-circular :value="satisfiedRequirementsPercentage" />
      <v-stepper-step v-for="item in requirements" :key="item.condition_name" :complete="item.is_satisfied">{{
        item.condition_name
      }}</v-stepper-step>
    </v-stepper-header>
  </v-stepper>
</template>
<script>
import { mapState } from "vuex";

export default {
  name: "InstallationSetupWizard",
  computed: {
    ...mapState({
      requirements: state => state.installationSetup.requirements,
      currentRequirementIndex: state => state.installationSetup.current_requirement_index,
      satisfiedRequirementsPercentage: state => state.installationSetup.satisfied_requirements_percentage,
      is_complete: state => state.installationSetup.is_complete
    })
  },
  mounted() {
    this.$store.dispatch("FETCH_INSTALLATION_SETUP_DETAILS");
  }
};
</script>
<style scoped></style>
