<template>
  <v-container>
    <v-flex>
      <span class="display-4 font-weight-black text-capitalize">{{
        projectName
      }}</span>
      <span class="display-4 font-weight-thin">targets</span>
    </v-flex>
    <v-data-table
      :headers="headers"
      :items="targets"
      class="elevation-1"
      item-key="name"
    >
      <template v-slot:headers="props">
        <th width="100">
          <v-icon>mdi-bullseye-arrow</v-icon>
        </th>
        <th :key="header.text" align="left" v-for="header in props.headers">
          {{ header.text }}
        </th>
      </template>
      <template v-slot:items="props">
        <router-link
          :style="{ cursor: 'pointer' }"
          :to="{
            name: 'target',
            params: { projectId: projectId, targetId: props.item.id }
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
export default {
  name: "ProjectTargetList",
  data() {
    return {
      projectId: "qL70nKe",
      projectName: "Barbara",
      headers: [
        {
          text: "Target Name",
          value: "name"
        },
        {
          text: "Python Version",
          value: "python_version"
        },
        {
          text: "Full Version",
          value: "full_version"
        }
      ],
      targets: [
        {
          id: "qL70nKe",
          name: "python3.8",
          python_major_version: 3,
          python_minor_version: 8,
          python_patch_version: 0,
          additional_details: "",
          full_version: "3.8.0",
          python_version: "3.8.0"
        }
      ]
    };
  }
};
</script>
