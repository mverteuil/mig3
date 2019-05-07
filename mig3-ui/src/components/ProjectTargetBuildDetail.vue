<template>
  <v-container>
    <v-flex>
      <router-link
        :to="{ name: 'project', params: { projectId: 'qL70nKe' } }"
        class="project-name"
      >
        <span
          class="project-name display-4 font-weight-black text-capitalize"
          >{{ projectName }}</span
        >
      </router-link>
      <span class="display-4 font-weight-thin">{{ targetName }}</span>
      <span class="display-2 text-uppercase">build {{ number }}</span>
    </v-flex>
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
