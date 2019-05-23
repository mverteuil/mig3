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
              v-flex(v-for="target in targets" :key="target.name")
                v-subheader Target: {{ target.name }}
                kbd mig3 --target {{ target.id }} --build 0 --endpoint {{ locationProtocol }}//{{ locationHostname }}/api/builds/ --token {{ builder.token }}
</template>
<script>
import { mapState } from "vuex";
import apiClient from "@/services/api";

export default {
  name: "InstallationSetupBuilds",
  computed: {
    ...mapState(["selected"]),
    locationProtocol() {
      return window.location.protocol;
    },
    locationHostname() {
      return window.location.hostname + (window.location.port ? ":" + window.location.port : "");
    }
  },
  data: () => ({
    polling: null,
    builder: { id: null, name: null, token: null },
    targets: {}
  }),
  props: ["step"],
  mounted() {
    apiClient.getBuilders().then(response => {
      apiClient.getBuilderDetails(response.data[0].id).then(response => {
        this.builder = response.data;
      });
    });
    apiClient.getProjects().then(response => {
      apiClient.getProjectDetails(response.data[0].id).then(response => {
        this.targets = response.data.map(target => [target.id, target]);
      });
    });
    this.polling = setInterval(() => {
      this.targets.forEach(target => {
        apiClient.getTargetDetails(target.id).then(response => {
          this.targets[response.data.id] = response.data;
        });
      });
    });
  }
};
</script>
<style scoped></style>
