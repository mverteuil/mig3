<template>
  <v-layout column grid-list-lg tag="v-container" v-if="!$route.params.projectId">
    <v-flex>
      <span class="display-4 font-weight-black text-capitalize">Projects</span>
      <v-layout>
        <v-flex :key="project.id" v-for="project in projects" xs4>
          <v-card :to="{ name: 'Project.Targets', params: { projectId: project.id } }" dark>
            <v-sheet color="red darken-2">
              <v-card-title>
                <v-flex>
                  <v-avatar color="red" left small>
                    <span class="white--text headline text-uppercase">{{ project.name.substr(0, 1) }}</span>
                  </v-avatar>
                  <span class="headline icon-text">{{ project.name }}</span>
                </v-flex>
              </v-card-title>
            </v-sheet>
            <v-card-actions class="space-evenly">
              <div>
                <v-icon class="vertical-middle">mdi-bullseye-arrow</v-icon>
                <span class="icon-text">{{ project.statistics.target_count }}</span>
              </div>
              <div>
                <v-icon class="vertical-middle">mdi-folder</v-icon>
                <span class="icon-text">{{ project.statistics.module_count }}</span>
              </div>
              <div>
                <v-icon class="vertical-middle">mdi-test-tube</v-icon>
                <span class="icon-text">{{ project.statistics.test_count }}</span>
              </div>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-flex>
  </v-layout>
  <router-view v-else />
</template>
<script>
export default {
  name: "ProjectList",
  data: () => ({
    projects: [
      {
        id: "qL70nKe",
        name: "mig3",
        url: "http://localhost:8000/api/projects/qL70nKe/",
        repo_url: "https://github.com/mverteuil/mig3.git",
        statistics: {
          target_count: 1,
          module_count: 3,
          test_count: 20
        }
      }
    ]
  })
};
</script>
