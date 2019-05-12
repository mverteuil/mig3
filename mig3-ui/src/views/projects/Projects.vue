<template>
  <v-layout row wrap>
    <ProjectCard :project="project" :key="project.id" v-for="project in projects" />
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
  },
  methods: {
    fetchProjects() {
      this.$store.dispatch("FETCH_PROJECTS");
    }
  },
  mounted() {
    this.fetchProjects();
  }
};
</script>
