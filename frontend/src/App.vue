<script setup lang="ts">
import NavigationBar from './components/NavigationBar.vue'
</script>

<template>
  <NavigationBar />
  <main class="container m-4 flex justify-center">
    <section class="text-center max-w-3xl">
      <h1 class="text-4xl">Introduction</h1>
      <p class="m-2 mt-4">
        This application allows you to record events when operators are working on a process during
        their shift. There are three main actions you can take, described below.
      </p>
      <div class="grid grid-cols-3 gap-4 grid-flow-col mt-10 divide-x">
        <section>
          <h2 class="text-3xl">Record new processes</h2>
          <p class="m-4 text-wrap">
            This functionality lets you register new processes inside the application.
          </p>
        </section>
        <section>
          <h2 class="text-3xl">Visualize processes</h2>
          <p class="m-4 text-wrap">
            This functionality lets you visualize existing processes inside the application.
          </p>
        </section>
        <section>
          <h2 class="text-3xl ml-4">Work in the fused view</h2>
          <p class="m-4 text-wrap">
            This experimental functionality gives a side-by-side view of the processes such that you
            can both record new processes and visualize them in another pane.
          </p>
        </section>
      </div>
    </section>
  </main>
</template>
