<template>
  <v-card @click="setSelectedProject(project)" dark width="500" z-index="0" flex>
    <v-sheet color="red darken-2">
      <v-card-title>
        <v-flex>
          <v-avatar color="red" left small>
            <span class="white--text headline text-uppercase">{{ project.name.substr(0, 1) }}</span>
          </v-avatar>
          <span class="headline icon-text">{{ project.name }}</span>
        </v-flex>
      </v-card-title>
    </v-sheet>
    <v-card-actions class="space-evenly">
      <div>
        <v-icon class="vertical-middle">mdi-bullseye-arrow</v-icon>
        <span class="icon-text">{{ project.statistics.target_count }}</span>
      </div>
      <div>
        <v-icon class="vertical-middle">mdi-folder</v-icon>
        <span class="icon-text">{{ project.statistics.module_count }}</span>
      </div>
      <div>
        <v-icon class="vertical-middle">mdi-test-tube</v-icon>
        <span class="icon-text">{{ project.statistics.test_count }}</span>
      </div>
    </v-card-actions>
  </v-card>
</template>
<script>
export default {
  name: "ProjectCard",
  props: {
    project: {
      type: Object,
      required: true
    }
  },
  methods: {
    setSelectedProject({ id }) {
      this.$store.dispatch("FETCH_PROJECT", { id });
    }
  }
};
</script>
