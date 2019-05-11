<template>
  <v-layout align-baseline>
    <v-flex class="shrink display-4 font-weight-black text-capitalize">
      <router-link
        :to="{ name: 'Project.Targets', params: { projectId: project.id } }"
        class="flat-link"
        v-if="project"
      >
        {{ project.name }}
      </router-link>
      <span v-else>Projects</span>
    </v-flex>
    <v-flex class="shrink display-4 font-weight-thin" v-if="project">
      <router-link
        :to="{ name: 'Project.Target.Builds', params: { projectId: project.id, targetId: target.id } }"
        class="flat-link"
        v-if="project && target"
      >
        {{ target.name }}
      </router-link>
      <span v-else>Targets</span>
    </v-flex>
    <v-flex class="display-2 shrink text-uppercase" v-if="project && target">
      <span v-if="target && number === null">Builds</span>
      <span v-else>Build {{ number }}</span>
    </v-flex>
  </v-layout>
</template>
<script>
export default {
  name: "breadcrumb-title",
  props: {
    number: {
      required: false,
      type: String,
      default: null
    },
    project: {
      required: false,
      type: Object,
      default: null
    },
    target: {
      required: false,
      type: Object,
      default: null
    }
  }
};
</script>
