<template>
  <v-layout column grid-list-lg tag="v-container">
    <v-flex>
      <span class="display-4 font-weight-black text-capitalize">Builders</span>
      <v-layout>
        <v-flex :key="builder.email" v-for="builder in builders" xs4>
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
    </v-flex>
  </v-layout>
</template>
<script>
import { mapState } from "vuex";

export default {
  name: "Builders",
  computed: {
    ...mapState({
      builders: "builders"
    })
  },
  methods: {
    fetchBuilders() {
      return this.$store.dispatch("FETCH_BUILDERS");
    }
  },
  mounted() {
    this.fetchBuilders();
  }
};
</script>
