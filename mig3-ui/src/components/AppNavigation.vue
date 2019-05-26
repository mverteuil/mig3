<template>
  <v-navigation-drawer app dark permanent width="260">
    <v-layout class="fill-height" column tag="v-list">
      <v-list-tile :to="{ name: 'Projects' }" xs4>
        <v-list-tile-action></v-list-tile-action>
        <v-list-tile-title class="title font-weight-black"
          >MIG3
          <v-icon>mdi-shield-airplane</v-icon>
        </v-list-tile-title>
      </v-list-tile>
      <v-list-tile
        :to="{ name: 'InstallationSetupWizard' }"
        v-if="currentUser.is_administrator && !installationSetup.is_complete"
      >
        <v-list-tile-action>
          <v-icon color="red">mdi-auto-fix</v-icon>
        </v-list-tile-action>
        <v-list-tile-content>
          <v-list-tile-title
            >Installation Setup ({{ installationSetup.satisfied_requirements_percentage }}%)</v-list-tile-title
          >
        </v-list-tile-content>
      </v-list-tile>
      <template v-if="installationSetup.is_complete">
        <v-list-tile :to="link.route" :key="link.name" v-for="link in links">
          <v-list-tile-action>
            <v-icon color="red">{{ link.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>{{ link.name }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </template>
      <v-list-tile href="/admin/" v-if="currentUser.is_administrator">
        <v-list-tile-action>
          <v-icon color="red">mdi-chef-hat</v-icon>
        </v-list-tile-action>
        <v-list-tile-content>
          <v-list-tile-title>Admin Portal</v-list-tile-title>
        </v-list-tile-content>
      </v-list-tile>
      <v-spacer class="fill-height" />
      <v-btn href="/accounts/logout/">Logout</v-btn>
    </v-layout>
  </v-navigation-drawer>
</template>
<script>
import { mapState } from "vuex";

export default {
  name: "AppNavigation",
  computed: {
    ...mapState(["currentUser", "installationSetup"])
  },
  data: () => ({
    links: [
      {
        icon: "mdi-code-braces",
        name: "Projects",
        route: { name: "Projects" }
      },
      {
        icon: "mdi-account-box-multiple",
        name: "User Accounts",
        route: { name: "Users" }
      },
      {
        icon: "mdi-application-export",
        name: "Builders",
        route: { name: "Builders" }
      }
    ]
  })
};
</script>
