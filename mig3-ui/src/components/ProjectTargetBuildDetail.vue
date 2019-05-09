<template>
  <v-container column>
    <v-layout align-baseline>
      <router-link :to="{ name: 'project', params: { projectId: project.id } }" class="flat-link">
        <span class="display-4 font-weight-black text-capitalize">{{ project.name }}</span>
      </router-link>
      <router-link :to="{ name: 'target', params: { targetId: target.id } }" class="flat-link">
        <span class="display-4 font-weight-thin">{{ target.name }}</span>
      </router-link>
      <v-flex class="display-2 text-uppercase">build {{ number }}</v-flex>
    </v-layout>
    <v-layout column-xs tag="v-container">
      <v-flex md6 xs12>
        <v-container class="title">Test Modules</v-container>
        <v-expansion-panel>
          <v-expansion-panel-content v-bind:key="module.path" v-for="module in modules">
            <template v-slot:actions>
              <v-layout align-center>
                <v-avatar class="green align-center darken-3 white--text" size="25">10</v-avatar>
                <v-spacer />
                <v-icon color="primary">$vuetify.icons.expand</v-icon>
              </v-layout>
            </template>
            <template v-slot:header>
              <v-layout align-center
                ><v-icon class="pr-2">mdi-folder</v-icon><span>{{ module.path }}</span></v-layout
              >
            </template>
            <v-card>
              <v-card-text class="grey lighten-3">
                <v-list>
                  <v-list-tile v-bind:key="test.name" v-for="test in module.tests">
                    <code>{{ test.name }}</code
                    >: {{ test.result }}
                  </v-list-tile>
                </v-list>
              </v-card-text>
            </v-card>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-flex>
      <v-flex gridlist-xs offset-md1 md4 xs12>
        <v-container class="title">Build Details</v-container>
        <v-card dark dense>
          <v-sheet color="red darken-2 elevation-5">
            <v-card-text class="white--text headline text-uppercase">{{ version.hash.substr(0, 8) }}</v-card-text>
          </v-sheet>
          <v-card-title class="text-uppercase body-2">Commit Hash</v-card-title>
        </v-card>
        <v-card dark>
          <v-sheet color="red darken-2 elevation-5">
            <v-card-text class="white--text headline">{{ version.author.email }}</v-card-text>
          </v-sheet>
          <v-card-title>
            <span class="text-uppercase">Author</span>
          </v-card-title>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
export default {
  name: "ProjectTargetBuildDetail",
  data: () => ({
    id: "qL70nKe",
    url: "http://localhost:8000/api/builds/qL70nKe/",
    target: {
      id: "qL70nKe",
      url: "http://localhost:8000/api/targets/qL70nKe/",
      name: "python3.8",
      python_major_version: 3,
      python_minor_version: 8,
      python_patch_version: 0,
      additional_details: "",
      full_version: "3.8.0",
      python_version: "3.8.0"
    },
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
    },
    modules: [
      {
        path: "tests/test_cli.py",
        tests: [
          {
            name: "test_valid_report_with_dry_run",
            result: "PASSED"
          },
          {
            name: "test_valid_report_with_bad_endpoint",
            result: "PASSED"
          },
          {
            name: "test_valid_report_with_regression",
            result: "PASSED"
          },
          {
            name: "test_happy_path",
            result: "PASSED"
          },
          {
            name: "test_invalid_report",
            result: "PASSED"
          },
          {
            name: "test_no_report",
            result: "PASSED"
          },
          {
            name: "test_no_token",
            result: "PASSED"
          },
          {
            name: "test_no_endpoint",
            result: "PASSED"
          },
          {
            name: "test_no_target_configuration",
            result: "PASSED"
          },
          {
            name: "test_no_build_number",
            result: "PASSED"
          }
        ]
      },
      {
        path: "tests/test_conversion.py",
        tests: [
          {
            name: "test_convert_result",
            result: "PASSED"
          },
          {
            name: "test_convert_test_name",
            result: "PASSED"
          },
          {
            name: "test_convert_module_name",
            result: "PASSED"
          },
          {
            name: "test_basic_convert",
            result: "PASSED"
          },
          {
            name: "test_simple_report",
            result: "PASSED"
          }
        ]
      },
      {
        path: "tests/test_submission_builder.py",
        tests: [
          {
            name: "test_version_details",
            result: "PASSED"
          },
          {
            name: "test_tests",
            result: "PASSED"
          },
          {
            name: "test_build_number",
            result: "PASSED"
          },
          {
            name: "test_configuration_id",
            result: "PASSED"
          },
          {
            name: "test_minimum_viable_submission",
            result: "PASSED"
          }
        ]
      }
    ],
    project: {
      id: "qL70nKe",
      name: "mig3",
      url: "http://localhost:8000/api/projects/qL70nKe/",
      repo_url: "https://github.com/mverteuil/mig3.git"
    }
  }),
  methods: {
    getResultIcon(result) {
      switch (result) {
        case "PASSED":
          return "checked-";
      }
    }
  }
};
</script>
