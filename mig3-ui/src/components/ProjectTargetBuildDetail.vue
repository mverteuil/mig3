<template>
  <v-container column>
    <v-flex>
      <router-link
        :to="{ name: 'project', params: { projectId: 'qL70nKe' } }"
        class="flat-link"
      >
        <span class="display-4 font-weight-black text-capitalize">{{
          projectName
        }}</span>
      </router-link>
      <router-link
        :to="{ name: 'target', params: { projectId: 'qL70nKe' } }"
        class="flat-link"
      >
        <span class="display-4 font-weight-thin">{{ targetName }}</span>
      </router-link>
      <span class="display-2 text-uppercase">build {{ number }}</span>
    </v-flex>
    <v-layout tag="v-container" row>
      <v-flex>
        <v-container class="title">Test Modules</v-container>
        <v-flex xs12 lg5>
          <v-expansion-panel>
            <v-expansion-panel-content>
              <template v-slot:actions>
                <v-icon color="primary">$vuetify.icons.expand</v-icon>
              </template>
              <template v-slot:header>
                <div>Item</div>
              </template>
              <v-card>
                <v-card-text class="grey lighten-3"
                  >Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                  Ut enim ad minim veniam, quis nostrud exercitation ullamco
                  laboris nisi ut aliquip ex ea commodo consequat.
                </v-card-text>
              </v-card>
            </v-expansion-panel-content>
            <v-expansion-panel-content>
              <template v-slot:actions>
                <v-icon color="teal">done</v-icon>
              </template>
              <template v-slot:header>
                <div>Item</div>
              </template>
              <v-card>
                <v-card-text class="grey lighten-3"
                  >Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                  Ut enim ad minim veniam, quis nostrud exercitation ullamco
                  laboris nisi ut aliquip ex ea commodo consequat.
                </v-card-text>
              </v-card>
            </v-expansion-panel-content>
            <v-expansion-panel-content>
              <template v-slot:actions>
                <v-icon color="error">error</v-icon>
              </template>
              <template v-slot:header>
                <div>Item</div>
              </template>
              <v-card>
                <v-card-text class="grey lighten-3"
                  >Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                  Ut enim ad minim veniam, quis nostrud exercitation ullamco
                  laboris nisi ut aliquip ex ea commodo consequat.
                </v-card-text>
              </v-card>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-flex>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
export default {
  name: "ProjectTargetBuildDetail",
  data: () => ({
    projectName: "barbara",
    targetName: "python3.8",
    id: "qL70nKe",
    number: "1",
    builder: {
      id: "qL70nKe",
      name: "Travis CI"
    },
    version: {
      sha: "a1a1a1a1",
      author: {
        id: "qL70nKe",
        email: "mverteuil@github.com"
      }
    },
    total: 100,
    passed: 50,
    failed: 10,
    error: 10,
    xfailed: 10,
    skipped: 10
  })
};
</script>
