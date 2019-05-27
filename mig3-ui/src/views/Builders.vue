<template>
  <v-container fluid>
    <v-layout column>
      <v-flex wrap justify-left align-center>
        <span class="display-4 font-weight-black text-capitalize">Builders</span>
      </v-flex>
      <v-layout row wrap>
        <v-container fluid grid-list-lg align-content-start pl-1>
          <v-layout>
            <v-flex :key="builder.name" v-for="builder in builders" xs4>
              <v-card dark>
                <v-sheet color="indigo darken-4">
                  <v-card-title>
                    <v-flex>
                      <v-avatar color="indigo" left small>
                        <span class="white--text headline">{{ builder.name.substr(0, 1) }}</span>
                      </v-avatar>
                      <span class="headline icon-text">{{ builder.name }}</span>
                    </v-flex>
                  </v-card-title>
                </v-sheet>
                <v-card-actions class="space-evenly">
                  <div>
                    <v-icon class="vertical-middle" color="green">mdi-shield-check</v-icon>
                    <span class="icon-text">{{ builder.statistics.build_count }}</span>
                  </div>
                  <div>
                    <v-icon class="vertical-middle">mdi-upload-network</v-icon>
                    <span class="icon-text">{{ builder.statistics.version_count }}</span>
                  </div>
                </v-card-actions>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-layout>
    </v-layout>
  </v-container>
</template>
<script>
import { mapState } from "vuex";

export default {
  name: "Builders",
  computed: {
    ...mapState({
      builders: "builders"
    })
  }
};
</script>
