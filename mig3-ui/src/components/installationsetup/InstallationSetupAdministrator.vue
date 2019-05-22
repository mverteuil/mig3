<template lang="pug">
  v-stepper-content(:step="step")
    v-container(fluid)
      v-layout
        v-flex(xs12)
          v-subheader You are logged into an administrator account.
      v-layout(row)
        v-flex(xs4)
          v-container
            v-layout
              v-flex(xs12)
                v-subheader(class="text-uppercase pl-0") {{ currentUser.name }} &lt;{{ currentUser.email }}&gt;
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
