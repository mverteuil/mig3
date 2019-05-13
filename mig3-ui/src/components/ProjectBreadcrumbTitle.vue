<template>
  <v-layout wrap justify-left align-center>
    <v-flex :class="['project-title', projectDisplaySize()]">
      <router-link
        :to="project ? { name: 'Project.Targets', params: { projectId: project.id } } : ''"
        tag="span"
        class="flat-link"
      >
        {{ project ? project.name : "Projects" }}
      </router-link>
    </v-flex>
    <v-fade-transition>
      <router-link
        :to="target ? { name: 'Project.Target.Builds', params: { projectId: project.id, targetId: target.id } } : ''"
        class="target-title flat-link"
        v-if="project"
      >
        {{ target ? target.name : "Targets" }}
      </router-link>
    </v-fade-transition>
    <v-flex class="build-title" v-if="project && target">
      <v-fade-transition>
        <span v-if="target && build">Build {{ build.number }}</span>
        <span v-else>Builds</span>
      </v-fade-transition>
    </v-flex>
  </v-layout>
</template>
<script>
import { mapState } from "vuex";

export default {
  name: "ProjectBreadcrumbTitle",
  computed: {
    ...mapState({
      project: state => state.selected.project,
      target: state => state.selected.target,
      build: state => state.selected.build
    })
  },
  methods: {
    projectDisplaySize() {
      return this.project ? "display-3" : "display-4";
    }
  }
};
</script>
<style lang="stylus" scoped>
@import "~vuetify/src/stylus/main";

.project-title
  @extends .font-weight-black, .text-capitalize, .shrink
  transition:font-size 1s

.target-title
  @extends .display-1, .font-weight-thin, .text-uppercase, .shrink
  text-align center

.build-title
  @extends .display-1, .text-uppercase, .shrink
</style>
