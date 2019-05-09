<template>
  <v-layout align-baseline>
    <v-flex class="shrink">
      <router-link
        :to="{ name: 'project', params: { projectId: project.id } }"
        class="display-4 font-weight-black text-capitalize flat-link"
        v-if="project && target"
      >
        <span v-if="project === null">Projects</span>
        <span v-else>{{ project.name }}</span>
      </router-link>
    </v-flex>
    <v-flex class="shrink" v-if="target">
      <router-link
        :to="{ name: 'target', params: { targetId: target.id } }"
        class="display-4 font-weight-thin flat-link"
        v-if="target && number"
      >
        <span v-if="project && target === null">Targets</span>
        <span v-else>{{ target.name }}</span>
      </router-link>
    </v-flex>
    <v-flex class="display-2 shrink text-uppercase">
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
