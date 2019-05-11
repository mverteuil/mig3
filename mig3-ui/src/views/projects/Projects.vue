<template>
  <v-flex column grid-list-lg>
    <v-layout>
      <ProjectCard :project="project" :key="project.id" v-for="project in projects" />
    </v-layout>
  </v-flex>
</template>
<script>
import { mapState } from "vuex";
import ProjectCard from "@/views/projects/ProjectCard";

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
