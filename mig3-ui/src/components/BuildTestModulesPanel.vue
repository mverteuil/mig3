<template>
  <v-expansion-panel v-if="modules">
    <v-expansion-panel-content v-bind:key="module.path" v-for="module in modules">
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
            <template v-for="(test, index) in module.tests">
              <v-list-tile :key="test.name">
                <v-list-tile-content>
                  <code>{{ test.name }}</code>
                </v-list-tile-content>
                <v-list-tile-action>
                  <v-icon>{{ getResultIcon(test.result) }}</v-icon>
                </v-list-tile-action>
              </v-list-tile>
              <v-divider v-if="index + 1 < module.tests.length" :key="index"></v-divider>
            </template>
          </v-list>
        </v-card-text>
      </v-card>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>
<script>
export default {
  name: "BuildTestModulesPanel",
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
    },
    getResultIcon(result) {
      if (result === "PASSED") {
        return "mdi-checkbox-marked-circle";
      }
    }
  }
};
</script>
