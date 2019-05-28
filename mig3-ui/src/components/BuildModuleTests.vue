<template>
  <div>
    <v-list-tile :key="test.name" v-for="test of tests">
      <v-list-tile-content class="row">
        <code>{{ test.name }}</code>
        <v-divider />
        <v-icon>{{ getResultIcon(test.result) }}</v-icon>
      </v-list-tile-content>
    </v-list-tile>
  </div>
</template>
<script>
import { alphaSort } from "@/utils/sorting";

export default {
  name: "build-module-tests",
  computed: {
    tests: function() {
      const sortByName = (a, b) => alphaSort(a.name, b.name);
      return [...this.module.tests].sort(sortByName);
    }
  },
  props: {
    module: {}
  },
  methods: {
    getResultIcon(result) {
      if (result === "PASSED") {
        return "mdi-checkbox-marked-circle";
      }
    }
  }
};
</script>
<style lang="stylus" scoped>
@import '~vuetify/src/stylus/main';

code
  @extends .mr-2
  background-color inherit
  color inherit

.row
  flex-direction row !important
  justify-content space-between
  align-items center
</style>
