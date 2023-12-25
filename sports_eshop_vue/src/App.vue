<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link :to="{ path: '/about' }" class="navbar-item"><strong>Sports Eshop</strong></router-link>
      </div>

      <div class="navbar-menu" id="mavbar-menu">
        <div class="navbar-end">
          <router-link to="{ path: '/summer' }">Suummer</router-link>
          <router-link to="{ path: '/winter' }">winter</router-link>

          <div class="navbar-item">
            <div class="buttons">
              <router-link to="{ path: '/login' }" class="button is-light">Log in</router-link>
              <router-link to="{ path: '/cart' }" class="button is-success">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart</span>
              </router-link>

            </div>
          </div>

        </div>
      </div>
    </nav>

    <section class="section">
      <routet-view/>
    </section>

  </div>


</template>

<style lang="scss">
@import '../node_modules/bulma';
</style>
