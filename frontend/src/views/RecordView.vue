<script setup lang="ts">
import { ref } from 'vue'
import type { Process } from '@/types/api'
import ProcessCard from '@/components/ProcessCard.vue'

const processes = ref<Process[]>([])

const fetchProcesses = async () => {
  try {
    const response = await fetch(' http://127.0.0.1:8000/processes/')
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    const data = await response.json()
    processes.value = data // assigning fetched data to items
  } catch (error) {
    console.error('Failed to fetch data:', error)
  }
}
fetchProcesses()
</script>
<template>
  <div v-for="p of processes" :key="p.id">
    {{ p }}
  </div>
</template>
