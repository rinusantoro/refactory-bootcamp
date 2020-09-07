<template>
  <div class="container">
    <Main>
      <!-- <HomePage /> -->
      <Navbar />
      <div class="row">
        <router-view class="col-8 justify-content-center"></router-view>
        <router-view class="col-4" name="sidebarB"></router-view>
      </div>
    </Main>

  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
</style>
