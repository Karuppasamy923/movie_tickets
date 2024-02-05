<template>
    <div>
        <!-- <pre>{movies.data}</pre> -->
        <h1 class="font-bold text-gray-800" >List of Movies</h1>
        <ul v-if="movies.data">
            <li v-for="movie in movies.data" :key="movie">
                <router-link :to="{name:'MovieDetails', params: { movieName: movie.name } }">
                    {{movie.title}}
                </router-link>
            </li>
        </ul>
        <!-- <h1>Hello</h1> -->
    </div>
</template>

<script setup>
import {createListResource} from 'frappe-ui';
import { RouterLink } from 'vue-router';

const movies = createListResource({
    doctype:"Movie",
    fields:['name','title','director','release_date'],
    auto:true,
})
</script>

<style lang="scss" scoped>

</style>