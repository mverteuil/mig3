<template>
  <v-layout tag="v-container" grid-list-lg column>
    <v-flex
      ><span class="display-4 font-weight-black text-capitalize">Users</span>
      <v-layout>
        <v-flex v-for="user in users" :key="user.email" md10 lg8 xl6>
          <v-card dark :to="{ name: 'users', params: { id: user.email } }">
            <v-sheet color="red darken-4">
              <v-card-title>
                <v-flex>
                  <v-avatar left small color="red">
                    <span class="white--text headline">{{
                      user.name.substr(0, 1)
                    }}</span>
                  </v-avatar>
                  <span class="headline icon-text">{{
                    user.name
                  }}</span></v-flex
                >
              </v-card-title>
            </v-sheet>
            <v-card-text>
              <v-icon class="mdi-at vertical-middle">mdi-at</v-icon>
              <span class="icon-text">{{ user.email }}</span>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: "UserAccountList",
  data: () => ({
    users: [
      {
        email: "mverteuil@gmail.com",
        name: "Matthew de Verteuil"
      }
    ]
  })
};
</script>

<style lang="stylus" scoped>
.icon-text
  //@extend vertical-middle
  padding-left 1em

.vertical-middle
  vertical-align middle
</style>
