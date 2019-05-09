<template>
  <v-layout align-baseline>
    <v-flex class="shrink">
      <router-link
        :to="{ name: 'project', params: { projectId: project.id } }"
        class="display-4 font-weight-black text-capitalize flat-link"
        v-if="project"
      >
        {{ project.name }}
      </router-link>
    </v-flex>
    <v-flex class="shrink">
      <router-link
        :to="{ name: 'target', params: { targetId: target.id } }"
        class="display-4 font-weight-thin flat-link"
      >
        {{ target.name }}
      </router-link>
    </v-flex>
    <v-flex class="display-2 shrink text-uppercase">build {{ number }}</v-flex>
  </v-layout>
</template>
<script>
export default {
  name: "breadcrumb-title",
  props: {
    number: {},
    project: {},
    target: {}
  }
};
</script>
