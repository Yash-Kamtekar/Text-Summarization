<template>
  <div id="nav">
    <nav class="navbar navbar-expand-lg navbar-light bg-light" style="background-color: black!important;color:white!important;">
      <a class="navbar-brand">Data Mining Assignment</a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link" @click="openLink('home')" style="cursor: pointer;">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" @click="openLink('about')" style="cursor: pointer;">About</a>
          </li>
        </ul>
      </div>
    </nav>
    <router-view />
  </div>
</template>
<script>
export default {
  name: 'App',
  components: {
  },
  methods: {
    openLink(value) {
      this.$router.push(value)
    }
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav a {
  font-weight: bold;
  color: white;
  margin-left: 30px;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
