<template>
  <v-toolbar color="red darken-4" app dark>
    <v-toolbar-title>MIG3</v-toolbar-title>
    <template v-slot:extension>
      <v-tabs color="transparent" icons-and-text>
        <v-tab to="/">
          Projects
          <v-icon>phone</v-icon>
        </v-tab>
        <v-tab href="admin/">
          Admin
          <v-icon>phone</v-icon>
        </v-tab>
      </v-tabs>
    </template>
  </v-toolbar>
</template>

<script>
export default {
  name: "AppNavigation"
};
</script>

<style scoped></style>
