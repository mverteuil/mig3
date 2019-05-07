<template>
  <v-layout tag="v-container" grid-list-lg column>
    <v-flex
      ><span class="display-4 font-weight-black text-capitalize">Builders</span>
      <v-layout>
        <v-flex v-for="builder in builders" :key="builder.email" xs4>
          <v-card dark :to="{ name: 'builders', params: { id: builder.id } }">
            <v-sheet color="indigo darken-4">
              <v-card-title>
                <v-flex>
                  <v-avatar left small color="indigo">
                    <span class="white--text headline">{{
                      builder.name.substr(0, 1)
                    }}</span>
                  </v-avatar>
                  <span class="headline icon-text">{{
                    builder.name
                  }}</span></v-flex
                >
              </v-card-title>
            </v-sheet>
            <v-card-actions>
              <v-flex>
                <v-icon class="vertical-middle" color="green"
                  >mdi-shield-check</v-icon
                >
                <span class="icon-text">{{ builder.successes }}</span>
              </v-flex>
              <v-flex>
                <v-icon class="mdi-at vertical-middle"
                  >mdi-upload-network</v-icon
                >
                <span class="icon-text">{{ builder.builds }}</span>
              </v-flex>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: "BuilderAccountList",
  data: () => ({
    builders: [
      {
        id: "qL70nKe",
        name: "Travis CI",
        builds: 10,
        successes: 1
      },
      {
        id: "E0lrPbR",
        name: "CircleCI",
        builds: 143,
        successes: 1
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
</style>
