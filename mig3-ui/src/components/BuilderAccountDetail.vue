<template>
  <v-container>
    <v-flex>
      <span class="display-4 font-weight-black">{{
        projects[$route.params.builderAccountId].name
      }}</span>
      <span class="display-4 font-weight-black text-capitalize">{{
        projectName
      }}</span>
      <span class="display-4 font-weight-thin">targets</span>
      <v-icon x-large>mdi-github-circle</v-icon>
    </v-flex>
    <target-list />
  </v-container>
</template>
<script>
export default {
  name: "BuilderAccountDetail"
};
</script>
