<template>
  <v-container>
    <v-flex>
      <span class="display-4 font-weight-black">{{
        projects[$route.params.projectId].name
      }}</span>

      <span
        class="display-4 font-weight-black text-capitalize"
        style="margin-bottom:-.7em;"
        >{{ projectName }}</span
      ><span class="display-4 font-weight-thin">targets</span>
    </v-flex>
    <target-list />
  </v-container>
</template>

<script>
import TargetList from "@/components/TargetList";

export default {
  name: "Project",
  components: { TargetList },
  data: () => ({
    projects: {
      qL70nKe: {
        name: "Barbara",
        repository_url: "https://github.com/mverteuil/barbara"
      },
      E0lrPbR: {
        name: "mig3-client",
        repository_url: "https://github.com/mverteuil/mig3-client"
      },
      vJ7v5lA: {
        name: "mig3",
        repository_url: "https://github.com/mverteuil/mig3"
      }
    }
  })
};
</script>

<style scoped></style>
