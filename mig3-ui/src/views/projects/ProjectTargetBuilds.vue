<template>
  <v-container>
    <breadcrumb-title :project="project" :target="this" />
    <v-data-table :headers="headers" :items="builds" class="elevation-1" header-key="text" item-key="id" hide-actions>
      <template v-slot:items="props">
        <router-link
          :to="{
            name: 'Project.Target.Build',
            params: { projectId: project.id, targetId: id, buildId: props.item.id }
          }"
          style="cursor:pointer"
          tag="tr"
        >
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
import BreadcrumbTitle from "@/components/BreadcrumbTitle";

export default {
  name: "ProjectTargetBuilds",
  components: { BreadcrumbTitle },
  data: () => ({
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
    ],
    id: "qL70nKe",
    url: "http://localhost:8000/api/targets/qL70nKe/",
    name: "python3.8",
    python_major_version: 3,
    python_minor_version: 8,
    python_patch_version: 0,
    additional_details: "",
    full_version: "3.8.0",
    python_version: "3.8.0",
    builds: [
      {
        id: "w6l2Rl5",
        url: "http://localhost:8000/api/builds/w6l2Rl5/",
        number: "2",
        version: {
          hash: "cbbab338e077b87d9fd169e63e832b7986e492f5",
          author: {
            id: "E0lrPbR",
            email: "mverteuil@github.com",
            name: "",
            build_count: 3
          }
        },
        builder: {
          id: "qL70nKe",
          name: "Travis-CI",
          statistics: {
            build_count: 3,
            version_count: 2
          }
        },
        outcome_summary: {
          error: 0,
          failed: 0,
          passed: 0,
          skipped: 0,
          xfailed: 0
        }
      },
      {
        id: "qL70nKe",
        url: "http://localhost:8000/api/builds/qL70nKe/",
        number: "1",
        version: {
          hash: "04d04ac04d62bb2952311c4e616ee96799e08592",
          author: {
            id: "E0lrPbR",
            email: "mverteuil@github.com",
            name: "",
            build_count: 3
          }
        },
        builder: {
          id: "qL70nKe",
          name: "Travis-CI",
          statistics: {
            build_count: 3,
            version_count: 2
          }
        },
        outcome_summary: {
          error: 0,
          failed: 0,
          passed: 40,
          skipped: 0,
          xfailed: 0
        }
      }
    ],
    project: {
      id: "qL70nKe",
      name: "mig3",
      url: "http://localhost:8000/api/projects/qL70nKe/",
      repo_url: "https://github.com/mverteuil/mig3.git",
      statistics: {
        target_count: 2,
        module_count: 3,
        test_count: 20
      }
    }
  }),
  methods: {
    shortHash: hash => hash.substr(0, 8)
  }
};
</script>
