<template>
    <div class="page-category">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="rounded">
                    <h2 class="is-size-2 has-text-centered" style="font-family: Verdana ">
                    {{ category.name }}
                    

                    </h2>

                </div>
                
                <br>
                    <hr style="background-color: black; height: 3px;">    
                    <br>
            </div>


            <ProductBox
                v-for="product in category.products"
                :key="product.id"
                :product="product"
            />
        </div>


    </div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'
import ProductBox from '@/components/ProductBox.vue'

export default {
    name: 'Category',
    data() {
        return {
            category:{
                products: []
            }
        }
    },
    components: {
        ProductBox
    },
    mounted() {
        this.getCategory()
    },
    watch: {
        $route(to, from){
            if (to.name === 'Category'){
                this.getCategory()
            }
        }
    },
    methods:{
        async getCategory() {
            const categorySlug = this.$route.params.category_slug

            this.$store.commit('setIsLoading', true)

            axios.get(`/api/v1/products/${categorySlug}/`)
                .then(response => { this.category = response.data
                                    document.title = this.category.name +  ' | Sports Eshop'
                                })
                .catch(error => { console.log(error)
                                    toast({
                                        message: 'Error. Try again',
                                        type: 'is-danger',
                                        dismissible: true,
                                        pauseOnHover: true,
                                        duration: 2000,
                                        position: 'bottom-right',
                                        })
                                }
                    )

                this.$store.commit('setIsLoading', false)
        }
    }
}
</script>


<style scoped>

  .rounded {
  border-radius: 25px;
  background: #ececec;
  padding: 20px;
  
}
</style>
