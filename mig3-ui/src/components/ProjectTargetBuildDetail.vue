<template>
  <v-container column>
    <v-flex>
      <router-link
        :to="{ name: 'project', params: { projectId: 'qL70nKe' } }"
        class="flat-link"
      >
        <span class="display-4 font-weight-black text-capitalize">{{
          projectName
        }}</span>
      </router-link>
      <router-link
        :to="{ name: 'target', params: { projectId: 'qL70nKe' } }"
        class="flat-link"
      >
        <span class="display-4 font-weight-thin">{{ targetName }}</span>
      </router-link>
      <span class="display-2 text-uppercase">build {{ number }}</span>
    </v-flex>
    <v-layout tag="v-container" row>
      <v-flex>
        <v-container class="title">Test Modules</v-container>
        <v-flex xs12 lg5>
          <v-expansion-panel>
            <v-expansion-panel-content>
              <template v-slot:actions>
                <v-icon color="primary">$vuetify.icons.expand</v-icon>
              </template>
              <template v-slot:header>
                <div>Item</div>
              </template>
              <v-card>
                <v-card-text class="grey lighten-3"
                  >Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                  Ut enim ad minim veniam, quis nostrud exercitation ullamco
                  laboris nisi ut aliquip ex ea commodo consequat.
                </v-card-text>
              </v-card>
            </v-expansion-panel-content>
            <v-expansion-panel-content>
              <template v-slot:actions>
                <v-icon color="teal">done</v-icon>
              </template>
              <template v-slot:header>
                <div>Item</div>
              </template>
              <v-card>
                <v-card-text class="grey lighten-3"
                  >Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                  Ut enim ad minim veniam, quis nostrud exercitation ullamco
                  laboris nisi ut aliquip ex ea commodo consequat.
                </v-card-text>
              </v-card>
            </v-expansion-panel-content>
            <v-expansion-panel-content>
              <template v-slot:actions>
                <v-icon color="error">error</v-icon>
              </template>
              <template v-slot:header>
                <div>Item</div>
              </template>
              <v-card>
                <v-card-text class="grey lighten-3"
                  >Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                  Ut enim ad minim veniam, quis nostrud exercitation ullamco
                  laboris nisi ut aliquip ex ea commodo consequat.
                </v-card-text>
              </v-card>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-flex>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
export default {
  name: "ProjectTargetBuildDetail",
  data: () => ({
    "id": "qL70nKe",
    "url": "http://localhost:8000/api/builds/qL70nKe/",
    "target": {
        "id": "qL70nKe",
        "url": "http://localhost:8000/api/targets/qL70nKe/",
        "name": "python3.8",
        "python_major_version": 3,
        "python_minor_version": 8,
        "python_patch_version": 0,
        "additional_details": "",
        "full_version": "3.8.0",
        "python_version": "3.8.0"
    },
    "number": "1",
    "version": {
        "hash": "04d04ac04d62bb2952311c4e616ee96799e08592",
        "author": {
            "id": "E0lrPbR",
            "email": "mverteuil@github.com",
            "name": ""
        }
    },
    "builder": {
        "id": "qL70nKe",
        "name": "Travis-CI"
    },
    "modules": [
        {
            "path": "tests/test_cli.py",
            "tests": [
                {
                    "name": "test_valid_report_with_dry_run",
                    "result": "PASSED"
                },
                {
                    "name": "test_valid_report_with_bad_endpoint",
                    "result": "PASSED"
                },
                {
                    "name": "test_valid_report_with_regression",
                    "result": "PASSED"
                },
                {
                    "name": "test_happy_path",
                    "result": "PASSED"
                },
                {
                    "name": "test_invalid_report",
                    "result": "PASSED"
                },
                {
                    "name": "test_no_report",
                    "result": "PASSED"
                },
                {
                    "name": "test_no_token",
                    "result": "PASSED"
                },
                {
                    "name": "test_no_endpoint",
                    "result": "PASSED"
                },
                {
                    "name": "test_no_target_configuration",
                    "result": "PASSED"
                },
                {
                    "name": "test_no_build_number",
                    "result": "PASSED"
                }
            ]
        },
        {
            "path": "tests/test_conversion.py",
            "tests": [
                {
                    "name": "test_convert_result",
                    "result": "PASSED"
                },
                {
                    "name": "test_convert_test_name",
                    "result": "PASSED"
                },
                {
                    "name": "test_convert_module_name",
                    "result": "PASSED"
                },
                {
                    "name": "test_basic_convert",
                    "result": "PASSED"
                },
                {
                    "name": "test_simple_report",
                    "result": "PASSED"
                }
            ]
        },
        {
            "path": "tests/test_submission_builder.py",
            "tests": [
                {
                    "name": "test_version_details",
                    "result": "PASSED"
                },
                {
                    "name": "test_tests",
                    "result": "PASSED"
                },
                {
                    "name": "test_build_number",
                    "result": "PASSED"
                },
                {
                    "name": "test_configuration_id",
                    "result": "PASSED"
                },
                {
                    "name": "test_minimum_viable_submission",
                    "result": "PASSED"
                }
            ]
        }
    ]
};
</script>
