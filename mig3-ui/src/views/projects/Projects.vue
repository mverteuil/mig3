<template>
  <v-layout row wrap>
    <v-container fluid grid-list-lg align-content-start pl-1>
      <v-layout row wrap>
        <ProjectCard :project="project" :key="project.id" v-for="project in projects" />
      </v-layout>
    </v-container>
  </v-layout>
</template>
<script>
import { mapState } from "vuex";
import ProjectCard from "@/components/ProjectCard";

export default {
  name: "ProjectList",
  components: { ProjectCard },
  computed: {
    ...mapState({ projects: "projects" })
  }
};
</script>
