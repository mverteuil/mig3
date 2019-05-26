<template lang="pug">
  v-stepper-content(:step="step")
    v-container(fluid ma-0 pa-0)
      v-layout
        v-flex(xs12)
          v-subheader(class="pl-0") It's time to send up a build for each target to make sure everything is configured correctly.
      v-layout(column)
        v-flex(xs12)
          v-card
            v-card-title 1. Install the client
            v-card-text
              p <kbd>pip install mig3-client</kbd>
              p Add this to your development/test <code>requirements.txt</code>.
              p If you use pipenv, add it to your Pipfile's dev section:
              p <kbd>pipenv install --dev mig3-client</kbd>
          v-card
            v-card-title 2. Add py.test JSON report configuration
            v-card-text
              p Add a <code>setup.cfg</code> if you don't already have one with a py.test section to generate the report. However, if you already use <code>pytest.ini</code>, you should add it there instead.
              kbd(pl-0) [tool:pytest]<br>
                | json_report = .report.json
        v-card
          v-card-title 3. Run py.test and generate a report
          v-card-text
            p Run <code>py.test</code> for the first configuration and generate the JSON report. It will now exist as <code>.report.json</code>.
          v-card-actions TIP Add this <code>.report.json</code> to your <code>.gitignore</code> to prevent accidentally committing it.
        v-card
          v-card-title 4. Submit your report to the mig3 service
          v-card-text
            p To submit a report to the mig3 service, we'll need to tell the service which project and target we've tested and the builder's token will authenticate the submission.
            p(v-for="target in initialTargets" :key="target.name")
              v-subheader Target: {{ target.name }} <v-spacer/><v-progress-circular v-if="target.builds.length === 0" indeterminate/>
              kbd mig3 --target {{ target.id }} \<br>
                |       --build 0 \
                |       --endpoint {{ locationProtocol }}//{{ locationHostname }}/api/builds/ \
                |       --token {{ builder.token }}
          v-card-actions (TIP: Remember that the builder token is a <strong>secret</strong> and should not be displayed in plaintext to anyone but your administrators.)


</template>
<script>
import { mapGetters, mapState } from "vuex";
import apiClient from "@/services/api";

export default {
  name: "InstallationSetupBuilds",
  computed: {
    ...mapGetters(["initialTargets"]),
    ...mapState({ installationComplete: state => state.installationSetup.is_complete }),
    locationProtocol() {
      return window.location.protocol;
    },
    locationHostname() {
      return window.location.hostname + (window.location.port ? ":" + window.location.port : "");
    }
  },
  data: () => ({
    polling: null,
    builder: {
      id: null,
      name: null,
      token: null
    },
    targets: {}
  }),
  props: ["step"],
  methods: {
    updateTargetDetails() {
      Object.values(this.initialTargets).forEach(({ id }) => {
        apiClient.getTargetDetails(id).then(response => {
          this.$set(this.targets, response.data.id, response.data);
        });
      });
    }
  },
  watch: {
    initialTargets: () => {
      if (this.polling === null) this.polling = setInterval(this.updateTargetDetails, 5000);
    },
    installationComplete: newValue => {
      if (newValue && this.polling) clearInterval(this.polling);
    }
  }
};
</script>
<style lang="stylus" scoped>
@import "~vuetify/src/stylus/main";

kbd:before, kbd:after
  content ""

kbd
  @extends .pa-2
</style>
