<template>
  <v-layout
    tag="v-container"
    grid-list-lg
    column
    v-if="!$route.params.projectId"
  >
    <v-flex
      ><span class="display-4 font-weight-black text-capitalize">Projects</span>
      <v-layout>
        <v-flex v-for="project in projects" :key="project.id" xs4>
          <v-card
            dark
            :to="{ name: 'project', params: { projectId: project.id } }"
          >
            <v-sheet color="red darken-2">
              <v-card-title>
                <v-flex>
                  <v-avatar left small color="red">
                    <span class="white--text headline text-uppercase">{{
                      project.name.substr(0, 1)
                    }}</span>
                  </v-avatar>
                  <span class="headline icon-text">{{
                    project.name
                  }}</span></v-flex
                >
              </v-card-title>
            </v-sheet>
            <v-card-actions class="space-evenly">
              <div>
                <v-icon class="vertical-middle">mdi-bullseye-arrow</v-icon>
                <span class="icon-text">2</span>
              </div>
              <div>
                <v-icon class="vertical-middle">mdi-folder</v-icon>
                <span class="icon-text">10</span>
              </div>
              <div>
                <v-icon class="vertical-middle">mdi-test-tube</v-icon>
                <span class="icon-text">60</span>
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
        name: "Barbara",
        repository_url: "https://github.com/mverteuil/barbara",
        to: "projects/0/"
      },
      {
        id: "E0lrPbR",
        name: "mig3-client",
        repository_url: "https://github.com/mverteuil/mig3-client"
      },
      {
        id: "vJ7v5lA",
        name: "mig3",
        repository_url: "https://github.com/mverteuil/mig3"
      }
    ]
  })
};
</script>

<style lang="stylus" scoped>
.vertical-middle
  vertical-align middle

.icon-text
  @extend .vertical-middle
  padding-left 1em

.space-evenly
  justify-content: space-evenly
</style>
