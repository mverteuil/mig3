<template>
  <v-expansion-panel>
    <v-expansion-panel-content v-bind:key="module.path" v-for="module in modules">
      <template v-slot:actions>
        <v-layout align-center>
          <v-avatar class="green align-center darken-3 white--text" size="25">10</v-avatar>
          <v-spacer />
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
        <v-card-text class="grey lighten-3">
          <v-list>
            <v-list-tile v-bind:key="test.name" v-for="test in module.tests">
              <code>{{ test.name }}</code>
              <v-icon>{{ getResultIcon(test.result) }}</v-icon>
            </v-list-tile>
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
    getResultIcon(result) {
      if (result === "PASSED") {
        return "mdi-checkbox-marked-circle";
      }
    }
  }
};
</script>
<style scoped></style>
