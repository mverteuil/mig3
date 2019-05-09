<template>
  <v-container>
    <v-flex>
      <span class="display-4 font-weight-black text-capitalize">{{ projectName }}</span>
      <span class="display-4 font-weight-thin">{{ targetName }}</span>
      <span class="display-2 text-uppercase">builds</span>
    </v-flex>
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
          <td>{{ props.item.version.sha }}</td>
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
export default {
  name: "ProjectTargetBuildList",
  data() {
    return {
      projectName: "barbara",
      targetName: "python3.8",
      headers: [
        {
          text: "ID",
          value: "id"
        },
        {
          text: "Builder",
          value: "builder"
        },
        {
          text: "Version",
          value: "version"
        },
        {
          text: "Author",
          value: "author"
        },
        {
          text: "Total",
          value: "total"
        },
        {
          text: "Passed",
          value: "passed"
        },
        {
          text: "XFailed",
          value: "xfailed"
        },
        {
          text: "Failed",
          value: "failed"
        },
        {
          text: "Error",
          value: "error"
        },
        {
          text: "Skipped",
          value: "skipped"
        }
      ],
      builds: [
        {
          id: "qL70nKe",
          number: "1",
          builder: {
            id: "qL70nKe",
            name: "Travis CI"
          },
          version: {
            sha: "a1a1a1a1",
            author: {
              id: "qL70nKe",
              email: "mverteuil@github.com"
            }
          },
          total: 100,
          passed: 50,
          failed: 10,
          error: 10,
          xfailed: 10,
          skipped: 10
        }
      ]
    };
  }
};
</script>
