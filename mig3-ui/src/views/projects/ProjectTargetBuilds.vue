<template>
  <v-container>
    <v-data-table
      :headers="headers"
      :items="target.builds"
      class="elevation-1"
      header-key="text"
      item-key="id"
      hide-actions
    >
      <template v-slot:items="props">
        <router-link @click="setSelectedBuild(props.item)" style="cursor:pointer" tag="tr">
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
        </router-link>
      </template>
    </v-data-table>
  </v-container>
</template>
<script>
import { mapGetters } from "vuex";

export default {
  name: "ProjectTargetBuilds",
  computed: {
    ...mapGetters({
      target: "selected.target"
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
    setSelectedBuild({ id }) {
      this.$store.dispatch("FETCH_BUILD", { id });
    },
    shortHash: hash => hash.substr(0, 8)
  }
};
</script>
