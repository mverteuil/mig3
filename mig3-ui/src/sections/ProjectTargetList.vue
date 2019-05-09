<template>
  <v-container>
    <breadcrumb-title :project="{ id, name }" />
    <v-data-table :headers="headers" :items="targets" class="elevation-1" item-key="name">
      <template v-slot:headers="props">
        <th style="text-align:left" v-for="header in props.headers" v-bind:key="header" v-html="header"></th>
      </template>
      <template v-slot:items="props">
        <router-link
          :style="{ cursor: 'pointer' }"
          :to="{
            name: 'target',
            params: { projectId: id, targetId: props.item.id }
          }"
          tag="tr"
        >
          <td align="center">
            <v-icon>mdi-bullseye-arrow</v-icon>
          </td>
          <td>
            {{ props.item.name }}
            <span class="font-weight-light">{{ props.item.id }}</span>
          </td>
          <td>{{ props.item.python_version }}</td>
          <td>{{ props.item.full_version }}</td>
        </router-link>
      </template>
    </v-data-table>
  </v-container>
</template>
<script>
import BreadcrumbTitle from "@/components/BreadcrumbTitle";
export default {
  name: "ProjectTargetList",
  components: { BreadcrumbTitle },
  data: () => ({
    headers: ["", "Target Name", "Python Version", "Full Version"],
    id: "qL70nKe",
    name: "mig3",
    url: "http://localhost:8000/api/projects/qL70nKe/",
    repo_url: "https://github.com/mverteuil/mig3.git",
    targets: [
      {
        id: "qL70nKe",
        url: "http://localhost:8000/api/targets/qL70nKe/",
        name: "python3.8",
        python_major_version: 3,
        python_minor_version: 8,
        python_patch_version: 0,
        additional_details: "",
        full_version: "3.8.0",
        python_version: "3.8.0"
      }
    ]
  })
};
</script>
