<template>
  <v-expansion-panel v-if="modules">
    <v-expansion-panel-content v-bind:key="module.path" v-for="module in sortedModules">
      <template v-slot:actions>
        <v-layout align-center>
          <v-flex mr-1>
            <v-avatar class="grey align-center darken-2 white--text " size="30">{{
              getOtherTestResultCount(module)
            }}</v-avatar>
          </v-flex>
          <v-flex mr-3>
            <v-avatar class="green align-center darken-2 white--text" size="30">{{
              getPassedTestResultCount(module)
            }}</v-avatar>
          </v-flex>
          <v-icon color="primary">$vuetify.icons.expand</v-icon>
        </v-layout>
      </template>
      <template v-slot:header>
        <v-layout align-center>
          <v-icon class="pr-2">mdi-folder</v-icon>
          <span>{{ module.path }}</span>
        </v-layout>
      </template>
      <v-card>
        <v-card-text class="grey darken-2">
          <v-list>
            <build-module-tests :module="module" />
          </v-list>
        </v-card-text>
      </v-card>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>
<script>
import BuildModuleTests from "@/components/BuildModuleTests";
import { alphaSort } from "@/utils/sorting";

export default {
  name: "BuildTestModulesPanel",
  components: { BuildModuleTests },
  computed: {
    sortedModules: function() {
      const sortByPath = (a, b) => alphaSort(a.path, b.path);
      return [...this.modules].sort(sortByPath);
    }
  },
  props: {
    modules: {
      type: Array,
      required: true
    }
  },
  methods: {
    getOtherTestResultCount(module) {
      return module.tests.length - this.getPassedTestResultCount(module);
    },
    getPassedTestResultCount(module) {
      return module.tests.filter(t => t.result === "PASSED").length;
    }
  }
};
</script>
<style lang="stylus" scoped>
code
  background-color inherit
  color inherit
</style>
