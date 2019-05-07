<template>
  <v-navigation-drawer app dark permanent width="260">
    <v-layout class="fill-height" column tag="v-list">
      <v-list-tile :to="{ name: 'home' }" xs4>
        <v-list-tile-action></v-list-tile-action>
        <v-list-tile-title class="title font-weight-black"
          >MIG3
          <v-icon>mdi-shield-airplane</v-icon>
        </v-list-tile-title>
      </v-list-tile>
      <v-list-tile
        :href="link.href ? link.href : '#'"
        :to="link.route ? link.route : null"
        v-bind:key="link.name"
        v-for="link in links"
      >
        <v-list-tile-action>
          <v-icon color="red">{{ link.icon }}</v-icon>
        </v-list-tile-action>
        <v-list-tile-content>
          <v-list-tile-title>{{ link.name }}</v-list-tile-title>
        </v-list-tile-content>
      </v-list-tile>
      <v-spacer class="fill-height" />
      <v-btn>Logout</v-btn>
    </v-layout>
  </v-navigation-drawer>
</template>
<script>
export default {
  name: "AppNavigation",
  data: () => ({
    links: [
      {
        icon: "mdi-code-braces",
        name: "Projects",
        href: null,
        route: { name: "projects" }
      },
      {
        icon: "mdi-account-box-multiple",
        name: "User Accounts",
        href: null,
        route: { name: "userAccounts" }
      },
      {
        icon: "mdi-application-export",
        name: "Builder Registration",
        href: null,
        route: { name: "builderAccounts" }
      },
      {
        icon: "mdi-chef-hat",
        name: "Admin",
        href: "/admin",
        route: null
      }
    ]
  })
};
</script>
