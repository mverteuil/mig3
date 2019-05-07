<template>
  <v-layout tag="v-container" grid-list-lg column>
    <v-flex
      ><span
        class="display-4 font-weight-black text-capitalize"
        style="margin-bottom:-.7em;"
        >Projects</span
      >
      <v-layout>
        <v-flex v-for="project in projects" :key="project.id" xs4>
          <v-card dark :to="{ name: 'projects', params: { id: project.id } }">
            <v-card-actions>
              <v-spacer />
              <v-btn :href="project.repository_url" icon>
                <v-icon>mdi-github-circle</v-icon>
              </v-btn>
            </v-card-actions>
            <v-card-title
              ><span class="headline text-uppercase font-weight-medium">{{
                project.name
              }}</span>
            </v-card-title>
          </v-card>
        </v-flex>
      </v-layout>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: "ProjectList",
  data: () => ({
    projects: [
      {
        id: "0",
        name: "Barbara",
        repository_url: "https://github.com/mverteuil/barbara",
        to: "projects/0/"
      },
      {
        id: "1",
        name: "mig3-client",
        repository_url: "https://github.com/mverteuil/mig3-client"
      },
      {
        id: "2",
        name: "mig3",
        repository_url: "https://github.com/mverteuil/mig3"
      }
    ]
  })
};
</script>

<style scoped></style>
