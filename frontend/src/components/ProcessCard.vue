<script setup lang="ts">
import { ref } from 'vue'
import type { Process } from '../types/api'

const process = ref<Process>()
</script>

<template>
  <div class="container">
    {{ process }}
  </div>
</template>
