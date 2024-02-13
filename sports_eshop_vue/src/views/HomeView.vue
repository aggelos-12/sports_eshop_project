<template>

  <div class="home">

    <section class="hero is-medium is-dark mn-6 rounded">
      <div class="hero-body has-text-centered" style="height: 100px;">
      <p class="title mb-6" style="font-family: Verdana;">
        What Streetwear Should Be
      </p>
      <p class="subtitle" style="font-family: Verdana;">
          Be One of Us
      </p>
      </div>
    </section>


    <div class="columns is-multiline">
      <div class="column is-12">
          <br>
          <h2 class="is-size-2 has-text-centered" style="font-family: Verdana;" >Latest products</h2>
          <br>

      </div>

      <ProductBox
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product" />
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox.vue'

export default {
  name: 'Home',
  data(){
    return{
      latestProducts: []
    }
  },
  components: {
    ProductBox
  },
  mounted() {
    this.getLatestProducts()

    document.title = 'Home | Sports Eshop'
  },
  methods: {
    async getLatestProducts(){
      this.$store.commit('setIsLoading', true)
      await  axios
        .get('/api/v1/latest-products/').then(response => { this.latestProducts = response.data})
        .catch(error => { console.log(error) })
        this.$store.commit('setIsLoading', false)
    }
  },

}
</script>

<style scoped>
  .image{
    margin-top:-1.25rem;
    margin-left:-1.25rem;
    margin-right:-1.25rem;
  }

  .rounded {
  border-radius: 25px;
  height: 350px;
  background: #333;
  padding: 20px;
  
}
</style>
