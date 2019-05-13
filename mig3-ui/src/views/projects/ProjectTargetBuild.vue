<template>
  <v-layout row>
    <v-flex xs12 lg6 v-if="build && build.modules">
      <v-container class="title">Test Modules</v-container>
      <build-test-modules-panel :modules="build.modules" />
    </v-flex>
    <v-flex xs12 lg5 offset-lg1 v-if="build">
      <v-container class="title">Build Details</v-container>
      <build-detail-card :value="build.version.hash.substr(0, 8)" field="Commit Hash" />
      <build-detail-card :value="build.builder.name" field="Builder" />
      <build-detail-card :value="build.version.author.email" field="Author" />
    </v-flex>
  </v-layout>
</template>
<script>
import BuildDetailCard from "@/components/BuildDetailCard";
import BuildTestModulesPanel from "@/components/BuildTestModulesPanel";
import { mapState } from "vuex";

export default {
  name: "ProjectTargetBuild",
  components: {
    BuildTestModulesPanel,
    BuildDetailCard
  },
  computed: {
    ...mapState({
      build: state => state.selected.build
    })
  },
  methods: {
    fetchBuild() {
      this.$store.dispatch("FETCH_BUILD", { id: this.$route.params.buildId });
    },
    shortHash: hash => hash.substr(0, 8)
  },
  mounted() {
    this.fetchBuild();
  }
};
</script>
