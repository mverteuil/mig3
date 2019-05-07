<template>
  <v-layout tag="v-container" column>
    <v-flex
      ><span
        class="display-4 font-weight-black text-capitalize"
        style="margin-bottom:-.7em;"
        >{{ projectName }}</span
      ><span class="display-4 font-weight-thin">{{
        targets[$route.params.targetId].name
      }}</span>
      <v-icon x-large>mdi-bullseye-arrow</v-icon>
    </v-flex>
    <template>
      <v-container fluid grid-list-md>
        <v-data-iterator
          :items="items"
          :rows-per-page-items="rowsPerPageItems"
          :pagination.sync="pagination"
          content-tag="v-layout"
          row
          wrap
        >
          <template v-slot:item="props">
            <v-flex xs12 sm6 md4 lg3>
              <v-card>
                <v-card-title
                  ><h4>{{ props.item.name }}</h4></v-card-title
                >
                <v-divider></v-divider>
                <v-list dense>
                  <v-list-tile>
                    <v-list-tile-content>Calories:</v-list-tile-content>
                    <v-list-tile-content class="align-end">{{
                      props.item.calories
                    }}</v-list-tile-content>
                  </v-list-tile>
                  <v-list-tile>
                    <v-list-tile-content>Fat:</v-list-tile-content>
                    <v-list-tile-content class="align-end">{{
                      props.item.fat
                    }}</v-list-tile-content>
                  </v-list-tile>
                  <v-list-tile>
                    <v-list-tile-content>Carbs:</v-list-tile-content>
                    <v-list-tile-content class="align-end">{{
                      props.item.carbs
                    }}</v-list-tile-content>
                  </v-list-tile>
                  <v-list-tile>
                    <v-list-tile-content>Protein:</v-list-tile-content>
                    <v-list-tile-content class="align-end">{{
                      props.item.protein
                    }}</v-list-tile-content>
                  </v-list-tile>
                  <v-list-tile>
                    <v-list-tile-content>Sodium:</v-list-tile-content>
                    <v-list-tile-content class="align-end">{{
                      props.item.sodium
                    }}</v-list-tile-content>
                  </v-list-tile>
                  <v-list-tile>
                    <v-list-tile-content>Calcium:</v-list-tile-content>
                    <v-list-tile-content class="align-end">{{
                      props.item.calcium
                    }}</v-list-tile-content>
                  </v-list-tile>
                  <v-list-tile>
                    <v-list-tile-content>Iron:</v-list-tile-content>
                    <v-list-tile-content class="align-end">{{
                      props.item.iron
                    }}</v-list-tile-content>
                  </v-list-tile>
                </v-list>
              </v-card>
            </v-flex>
          </template>
        </v-data-iterator>
      </v-container>
    </template>
    <build-list />
  </v-layout>
</template>

<script>
import BuildList from "@/components/BuildList";

export default {
  components: { BuildList },
  data: () => ({
    projectName: "barbara",
    targets: {
      qL70nKe: {
        name: "python3.8",
        python_major_version: 3,
        python_minor_version: 8,
        python_patch_version: 0,
        additional_details: "",
        full_version: "3.8.0",
        python_version: "3.8.0"
      }
    }
  })
};
</script>
