<template>
  <v-data-table :headers="headers" :items="targets" class="elevation-1" item-key="name">
    <template v-slot:items="props">
      <tr :style="{ cursor: 'pointer' }" @click="navigateToTarget(props.item.id)">
        <td align="center">
          <v-icon>mdi-bullseye-arrow</v-icon>
        </td>
        <td>
          {{ props.item.name }}
          <span class="font-weight-light">{{ props.item.id }}</span>
        </td>
        <td>{{ props.item.python_version }}</td>
        <td>{{ props.item.full_version }}</td>
      </tr>
    </template>
  </v-data-table>
</template>
<script>
import { mapState } from "vuex";

export default {
  name: "ProjectTargetList",
  computed: {
    ...mapState(["targets"]),
    ...mapState({
      project: state => state.selected.project
    })
  },
  data() {
    return {
      headers: [
        {
          text: null,
          sortable: false
        },
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
      ]
    };
  },
  methods: {
    navigateToTarget(targetId) {
      this.$router.push({ name: "Project.Target.Builds", params: { projectId: this.project.id, targetId: targetId } });
    }
  }
};
</script>
