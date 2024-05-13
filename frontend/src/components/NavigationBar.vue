<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>
  <nav class="border-b-2 border-b-black mt-5 ml-2 mr-2">
    <ol class="list-none flex justify-center mb-5">
      <li class="inline-block ml-10 text-xl">
        <RouterLink to="/processes/visualize" class="underline">Visualize</RouterLink>
      </li>
      <li class="inline-block ml-10 text-xl">
        <RouterLink to="/processes/record" class="underline">Record</RouterLink>
      </li>
      <li class="inline-block ml-10 text-xl">
        <RouterLink to="/processes/fused" class="underline">Fused View</RouterLink>
      </li>
    </ol>
  </nav>
</template>
<style scoped>
nav > ol > li > a:hover {
  background-color: black;
  color: white;
}
</style>
