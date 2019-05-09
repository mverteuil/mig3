<template>
  <v-container column>
    <breadcrumb-title :number="number" :project="project" :target="target" />
    <v-layout column-xs tag="v-container">
      <v-flex md6 xs12>
        <v-container class="title">Test Modules</v-container>
        <build-test-modules-panel :modules="modules" />
      </v-flex>
      <v-flex column ml-3 xs3>
        <v-container class="title">Build Details</v-container>
        <build-detail-card :value="version.hash.substr(0, 8)" field="Commit Hash" />
        <build-detail-card :value="builder.name" field="Builder" />
        <build-detail-card :value="version.author.email" field="Author" />
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import BuildDetailCard from "@/components/BuildDetailCard";
import BuildTestModulesPanel from "@/components/BuildTestModulesPanel";
import BreadcrumbTitle from "@/components/BreadcrumbTitle";

export default {
  name: "ProjectTargetBuildDetail",
  components: {
    BreadcrumbTitle,
    BuildTestModulesPanel,
    BuildDetailCard
  },
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
    },
    outcome_summary: {
      error: 0,
      failed: 0,
      passed: 20,
      skipped: 0,
      xfailed: 0
    }
  })
};
</script>
