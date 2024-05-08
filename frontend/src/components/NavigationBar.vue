<script setup lang="ts"></script>
<template>
  <nav class="border-b-2 border-b-black mt-5 ml-2 mr-2">
    <ol class="list-none flex justify-center mb-5">
      <li class="inline-block ml-10 text-xl">
        <a href="/processes/record" class="underline">Record</a>
      </li>
      <li class="inline-block ml-10 text-xl">
        <a href="/processes/visualize" class="underline">Visualize</a>
      </li>
      <li class="inline-block ml-10 text-xl">
        <a href="/processes/fused" class="underline">Fused View</a>
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
