<template lang="pug">
  v-stepper-content(:step="step")
    v-container(fluid)
      v-layout
        v-flex(xs12)
          v-subheader It's time to send up a build for each target to make sure everything is configured correctly.
      v-layout(row)
        v-flex(xs4)
          v-container
            v-layout(column)
              v-flex To install the client <kbd>pip install mig3-client</kbd>, add this to your development/test requirements.txt. If you use pipenv.
              v-flex Add a <code>setup.cfg</code> if you don't already have one with a py.test section to generate the report. If you use <code>pytest.ini</code>, you should add it there instead.
                code
                  | [tool:pytest]
                  | json_report = .report.json
              v-flex Run py.test for the first configuration and generate the JSON report. It will now exist as .report.json. (TIP: Add this file to your <code>.gitignore</code> to prevent accidentally committing it.)
              v-flex To submit a report to the mig3 service, we'll need to tell the service which project and target we've tested and the builder's token will authenticate the submission.
                | (TIP: Remember that the builder token is a <b>secret</b> and should not be displayed in plaintext to anyone but your administrators.)
              v-flex

</template>
<script>
import { mapState } from "vuex";
import { FETCH_BUILDER, FETCH_BUILDERS, FETCH_PROJECT, FETCH_PROJECTS } from "@/store/action-types";

export default {
  name: "InstallationSetupBuilds",
  computed: {
    ...mapState(["selected"])
  },
  data: () => ({
    progress: false
  }),
  props: ["step"],
  mounted() {
    this.$store
      .dispatch(FETCH_BUILDERS)
      .then(response => {
        this.$store.dispatch(FETCH_BUILDER, response.data[0].id).finally(() => {
          this.progress = false;
        });
      })
      .finally(() => {
        this.progress = false;
      });
    this.$store.dispatch(FETCH_PROJECTS).then(response => {
      this.$store.dispatch(FETCH_PROJECT, response.data[0].id);
    });
  }
};
</script>
<style scoped></style>
