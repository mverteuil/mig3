<template>
  <v-container>
    <v-flex>
      <span class="display-4 font-weight-black">{{
        projects[$route.params.id].name
      }}</span>
      <v-icon x-large>mdi-github-circle</v-icon>
    </v-flex>
    <target-list />
  </v-container>
</template>

<script>
import TargetList from "@/components/TargetList";

export default {
  name: "ProjectDetail",
  components: { TargetList },
  data: () => ({
    projects: {
      "0": {
        name: "Barbara",
        repository_url: "https://github.com/mverteuil/barbara"
      },
      "1": {
        name: "mig3-client",
        repository_url: "https://github.com/mverteuil/mig3-client"
      },
      "2": {
        name: "mig3",
        repository_url: "https://github.com/mverteuil/mig3"
      }
    }
  })
};
</script>

<style scoped></style>
