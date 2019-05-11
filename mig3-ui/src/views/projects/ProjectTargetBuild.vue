<template>
  <v-layout column-xs tag="v-container">
    <v-flex md6 xs12>
      <v-container class="title">Test Modules</v-container>
      <build-test-modules-panel :modules="build.modules" />
    </v-flex>
    <v-flex column ml-3 xs3>
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
import BreadcrumbTitle from "@/components/BreadcrumbTitle";
import { mapGetters } from "vuex";

export default {
  name: "ProjectTargetBuildDetail",
  components: {
    BreadcrumbTitle,
    BuildTestModulesPanel,
    BuildDetailCard
  },
  computed: {
    ...mapGetters({
      build: "selected.build"
    })
  }
};
</script>
