<template>
   <div class="p-8">
      <MovieDetails/>
   </div>
</template>
<!-- new change -->
<script>
   import MovieDetails from './MovieDetails.vue';
   export default {
      name:'home',
      components:{
         MovieDetails,
      },
   }
</script>

<style lang="scss" scoped>

</style>