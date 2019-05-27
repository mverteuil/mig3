<template>
  <v-layout fluid row>
    <v-flex xs12>
      <v-data-table :headers="headers" :items="builds" class="elevation-1" header-key="text" hide-actions item-key="id">
        <template v-slot:items="props">
          <tr @click="navigateToBuild(props.item.id)" style="cursor:pointer">
            <td align="center">
              <v-icon color="green">mdi-shield-check</v-icon>
            </td>
            <td class="flow">
              {{ props.item.number }}
              <br />
              <span class="font-weight-light">{{ props.item.id }}</span>
            </td>
            <td>{{ props.item.builder.name }}</td>
            <td>{{ shortHash(props.item.version.hash) }}</td>
            <td>{{ props.item.version.author.email }}</td>
            <td>{{ props.item.outcome_summary.passed }}</td>
            <td>{{ props.item.outcome_summary.xfailed }}</td>
            <td>{{ props.item.outcome_summary.failed }}</td>
            <td>{{ props.item.outcome_summary.error }}</td>
            <td>{{ props.item.outcome_summary.skipped }}</td>
          </tr>
        </template>
      </v-data-table>
    </v-flex>
  </v-layout>
</template>
<script>
import { mapState } from "vuex";

export default {
  name: "ProjectTargetBuilds",
  computed: {
    ...mapState(["builds"]),
    ...mapState({
      project: state => state.selected.project,
      target: state => state.selected.target
    })
  },
  data() {
    return {
      headers: [
        { text: "", sortable: false },
        { text: "Build", value: "number" },
        { text: "Builder", value: "builder.name" },
        { text: "Commit", value: "version.hash" },
        { text: "Author", value: "version.author.email" },
        { text: "Passed", value: "statistics.passed" },
        { text: "Xfailed", value: "statistics.xfailed" },
        { text: "Failed", value: "statistics.failed" },
        { text: "Error", value: "statistics.error" },
        { text: "Skipped", value: "statistics.skipped" }
      ]
    };
  },
  methods: {
    navigateToBuild(buildId) {
      this.$router.push({
        name: "Project.Target.Build",
        params: { projectId: this.project.id, targetId: this.target.id, buildId: buildId }
      });
    },
    shortHash: hash => hash.substr(0, 8)
  }
};
</script>
