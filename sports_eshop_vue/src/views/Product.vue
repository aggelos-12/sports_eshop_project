<template>
    <div class="page-product">
        <div class="columns is-multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                    <img :src="product.get_image">
                </figure>

                <h1 class="title">{{ product.name  }}</h1>
                
                <hr style="background-color: #bebebe; height: 3px;">
                <p style="font-size: 22px; font-weight: 600;">Description: </p>
                <p style="font-size: 20px;">{{ product.description }}</p>
                <hr style="background-color: #bebebe; height: 3px;">
            </div>

            <div class="collumn is-3">
                <h2 class="title mb-6" style="font-family: Verdana;font-size: 20px;">Features: {{ product.information }}</h2>
                <hr style="background-color: #bebebe; height: 3px;">
                <p><strong>Price: </strong>${{ product.price }}</p>

                <div class="filed has-addons mt-6">
                    <div class="control">
                        <input type="number" class="input" min="1" v-model="quantity">
                    </div>

                    <div class="control">
                        <br>
                        <a class="button is-dark" @click="addToCart">Add to cart</a>
                    </div>
                </div>

            </div>
        </div>
    </div>

</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
import ProductBox from '@/components/ProductBox.vue'

export default {
    name: 'Product',
    data() {
        return{
            product: {},
            quantity: 1
        }
    },

    mounted() {
        this.getProduct()
    },

    methods:{
        async getProduct() {
            this.$store.commit('setIsLoading', true)

            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug

           await axios.get(`/api/v1/products/${category_slug}/${product_slug}`)
            .then(response => { this.product = response.data
                                document.title = this.product.name +  ' | Sports Eshop'})
            .catch(error => { console.log(error) })
            this.$store.commit('setIsLoading', false)
        },

        addToCart () {
            if (isNaN(this.quantity) || this.quantity < 1){
                this.quantity = 1
            }

            const item = {
                product: this.product,
                quantity: this.quantity
            }
            this.$store.commit('addToCart', item)
            toast({
                message: 'The product was added to the cart',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        }
    }

}
</script>