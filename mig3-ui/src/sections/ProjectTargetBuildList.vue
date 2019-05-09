<template>
  <v-container>
    <breadcrumb-title :project="project" :target="target" />
    <v-data-table :headers="headers" :items="builds" class="elevation-1" header-key="text" item-key="id">
      <template v-slot:headers="props">
        <th width="100">
          <v-icon color="green">mdi-shield-check</v-icon>
        </th>
        <th :key="header.text" align="left" v-for="header in props.headers">
          {{ header.text }}
        </th>
      </template>
      <template v-slot:items="props">
        <router-link
          :style="{ cursor: 'pointer' }"
          :to="{ name: 'builds', params: { buildId: props.item.id } }"
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
          <td>{{ props.item.version.hash }}</td>
          <td>{{ props.item.version.author.email }}</td>
          <td>{{ props.item.total }}</td>
          <td>{{ props.item.passed }}</td>
          <td>{{ props.item.xfailed }}</td>
          <td>{{ props.item.failed }}</td>
          <td>{{ props.item.error }}</td>
          <td>{{ props.item.skipped }}</td>
        </router-link>
      </template>
    </v-data-table>
  </v-container>
</template>
<script>
import BreadcrumbTitle from "@/components/BreadcrumbTitle";
export default {
  name: "ProjectTargetBuildList",
  components: { BreadcrumbTitle },
  data: () => ({
    headers: [],
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
        id: "qL70nKe",
        url: "http://localhost:8000/api/builds/qL70nKe/",
        target: "qL70nKe",
        number: "1",
        version: {
          hash: "04d04ac04d62bb2952311c4e616ee96799e08592",
          author: {
            id: "E0lrPbR",
            email: "onceuponajooks@gmail.com",
            name: ""
          }
        },
        builder: {
          id: "qL70nKe",
          name: "Travis-CI"
        }
      }
    ],
    project: {
      id: "qL70nKe",
      name: "mig3",
      url: "http://localhost:8000/api/projects/qL70nKe/",
      repo_url: "https://github.com/mverteuil/mig3.git"
    }
  })
};
</script>
