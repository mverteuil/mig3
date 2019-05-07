<template>
  <v-data-table
    :headers="headers"
    :items="builds"
    class="elevation-1"
    item-key="id"
  >
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
        <td>{{ props.items.id }}</td>
        <td>{{ props.items.number }}</td>
        <td>{{ props.items.builder["name"] }}</td>
        <td>{{ props.items.version["sha"] }}</td>
        <td>{{ props.items.version["author"]["email"] }}</td>
        <td>{{ props.items.total }}</td>
        <td>{{ props.items.passed }}</td>
        <td>{{ props.items.xfailed }}</td>
        <td>{{ props.items.failed }}</td>
        <td>{{ props.items.error }}</td>
        <td>{{ props.items.skipped }}</td>
      </router-link>
    </template>
  </v-data-table>
</template>
<script>
export default {
  name: "TargetList",
  data() {
    return {
      headers: [
        {
          text: "ID",
          value: "id"
        },
        {
          text: "Number",
          value: "number"
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
<style scoped></style>
