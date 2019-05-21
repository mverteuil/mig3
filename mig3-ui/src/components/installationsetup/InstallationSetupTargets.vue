<template lang="pug">
  v-stepper-content(:step="step")
    v-container(fluid)
      v-layout
        v-flex(xs12)
          v-subheader Determine where you are and where you want to be.
      v-layout(row)
        v-flex(xs4)
          v-container
            v-layout
              v-flex(xs12)
                v-text-field(label="Source Name", v-model="source.name")
            v-layout
              v-flex(xs12)
                v-subheader(class="text-uppercase pl-0") Python Version
            v-layout
              v-flex(xs4 mr-3)
                v-combobox(label="Major" :items="majorVersionItems" v-model="source.python_major_version")
              v-flex(xs4 mr-3)
                v-combobox(label="Minor" :items="sourceMinorVersions" v-model="source.python_minor_version")
              v-flex(xs4)
                v-combobox(label="Patch" :items="patchVersions" v-model="source.python_patch_version")
        v-flex(xs4)
          v-container
            v-layout
              v-flex(xs12)
                v-text-field(label="Destination Name", v-model="destination.name")
            v-layout
              v-flex(xs12)
                v-subheader(class="text-uppercase pl-0") Python Version
            v-layout
              v-flex(xs4 mr-3)
                v-combobox(label="Major" :items="majorVersionItems" v-model="destination.python_major_version")
              v-flex(xs4 mr-3)
                v-combobox(label="Minor" :items="destinationMinorVersions" v-model="destination.python_minor_version")
              v-flex(xs4)
                v-combobox(label="Patch" :items="patchVersions" v-model="destination.python_patch_version")
      v-layout(row)
        v-flex(xs12)
          v-btn(@click="createTargets()") Create Targets
</template>
<script>
import { CREATE_TARGET } from "@/store/action-types";

export default {
  name: "InstallationSetupTargets",
  props: ["step"],
  computed: {
    destinationMinorVersions() {
      return this.majorAndMinorVersions[this.destination.python_major_version];
    },
    majorVersionItems() {
      return Object.keys(this.majorAndMinorVersions);
    },
    sourceMinorVersions() {
      return this.majorAndMinorVersions[this.source.python_major_version];
    }
  },
  data: () => ({
    destination: {
      name: "python3.7",
      python_major_version: 3,
      python_minor_version: 7,
      python_patch_version: 3
    },
    source: {
      name: "python2.7",
      python_major_version: 2,
      python_minor_version: 7,
      python_patch_version: 14
    },
    majorAndMinorVersions: {
      2: [7],
      3: [4, 5, 6, 7, 8, 9]
    },
    patchVersions: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
  }),
  methods: {
    async createTargets() {
      await this.$store.dispatch(CREATE_TARGET, { ...this.source });
      await this.$store.dispatch(CREATE_TARGET, { ...this.destination });
    }
  },
  watch: {
    "destination.python_major_version": function(newValue) {
      this.destinationMinorVersions = this.majorAndMinorVersions[newValue];
    },
    "source.python_major_version": function(newValue) {
      this.sourceMinorVersions = this.majorAndMinorVersions[newValue];
    }
  }
};
</script>
<style scoped></style>
