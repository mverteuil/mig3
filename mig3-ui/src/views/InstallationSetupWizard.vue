<template>
  <v-container>
    <v-layout row>
      <v-flex xs12>
        <span class="display-4 flex font-weight-black text-capitalize">Installation Setup</span>
      </v-flex>
    </v-layout>
    <v-layout row>
      <v-flex xs12>
        <v-stepper v-model="currentInstallationStep" vertical>
          <template v-for="index in requirements.length">
            <v-stepper-step
              :key="`${index}-step`"
              :complete="getRequirement(requirements, index).is_satisfied"
              :step="index"
            >
              {{ getRequirement(requirements, index).condition_name }}
            </v-stepper-step>
            <component
              :is="`InstallationSetup${getRequirement(requirements, index).id}`"
              :key="`${index}-content`"
              :step="index"
            ></component>
          </template>
        </v-stepper>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import { mapState } from "vuex";
import InstallationSetupAdministrator from "@/components/installationsetup/InstallationSetupAdministrator";
import InstallationSetupBuilder from "@/components/installationsetup/InstallationSetupBuilder";
import InstallationSetupBuilds from "@/components/installationsetup/InstallationSetupBuilds";
import InstallationSetupProject from "@/components/installationsetup/InstallationSetupProject";
import InstallationSetupTargets from "@/components/installationsetup/InstallationSetupTargets";
import { FETCH_INSTALLATION_SETUP_DETAILS } from "@/store/action-types";

export default {
  name: "InstallationSetupWizard",
  components: {
    InstallationSetupAdministrator,
    InstallationSetupBuilder,
    InstallationSetupBuilds,
    InstallationSetupProject,
    InstallationSetupTargets
  },
  computed: {
    currentInstallationStep: {
      get() {
        return this.$store.getters.currentInstallationStep;
      },
      set() {}
    },
    ...mapState({
      requirements: state => state.installationSetup.requirements,
      is_complete: state => state.installationSetup.is_complete
    })
  },
  methods: {
    getRequirement: (requirements, stepNumber) => requirements[stepNumber - 1]
  },
  mounted() {
    this.$store.dispatch(FETCH_INSTALLATION_SETUP_DETAILS);
  }
};
</script>
<style scoped></style>
