<template>
  <div class="home">
    <div class="row height d-flex justify-content-center align-items-center">
      <div class="col-md-8" style="background-color: #ffffff;">
        <div class="search">
          <i class="fa fa-search"></i>
          <input
            type="text"
            class="form-control"
            placeholder="Search here"
            style="border-radius: 30px;"
          />
          <button class="btn btn-primary" style="border-radius: 30px;">Search</button>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-sm-3">
        <h5>Filter based on Date:</h5>
      </div>
      <div class="col-sm-3">
        <v-row justify="center">
          <v-breadcrumbs
          :items="items"
          divider="-"
        ></v-breadcrumbs>
        </v-row>
      </div>
      </div>
    </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "Home",
  data () {
    return {
      items: [
        {
          text: 'Dashboard',
          disabled: false,
          href: 'breadcrumbs_dashboard',
        },
        {
          text: 'Link 1',
          disabled: false,
          href: 'breadcrumbs_link_1',
        },
        {
          text: 'Link 2',
          disabled: true,
          href: 'breadcrumbs_link_2',
        },
      ]
    }
  },
  components: {},
};
</script>
<style scoped>
.height {
  height: 50vh;
}

.search {
  position: relative;
  box-shadow: 0 0 40px rgba(51, 51, 51, 0.1);
}

.search input {
  height: 60px;
  text-indent: 25px;
  border: 2px solid #d6d4d4;
}

.search input:focus {
  box-shadow: none;
  border: 2px solid blue;
}

.search .fa-search {
  position: absolute;
  top: 20px;
  left: 16px;
}

.search button {
  position: absolute;
  top: 5px;
  right: 5px;
  height: 50px;
  width: 110px;
  background: blue;
}
</style>
