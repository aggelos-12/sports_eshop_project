<template>
    <div class="page-success">
        <div class="columns is-multiline">
            <div class="column is-12">
                <img src="../assets/success.png" class="center">
                <br>
                <br>
                
                <hr style="background-color: #bebebe; height: 4px; width: 880px; margin-left: 490px;">
                <br>
                <div class="center success">
                    <p class="text">Your order will be proccessed within 24 hours</p>
                </div>
                
            </div>
        </div>
    </div>

</template>

<script>
export default{
    name: 'Success',
    mounted() {
        document.title = 'Success | Sports Eshop'
    },
}

</script>

<style scoped>
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}

.text{
    font-size: 22px;
    color: white;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-weight: bold;
    margin-left: 40px;
    padding-top: 8px;
    
}

.rounded {
  border-radius: 25px;
  background: #333;
  padding: 20px;
  
}

.success{
    width: 550px;
    height: 50px;
    background-color: #333; 
    border-radius: 25px;
}
</style>