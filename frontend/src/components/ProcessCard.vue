<script setup lang="ts">
import type { Process, ProcessPerformance } from '@/types/api'
import EventCard from '@/components/EventCard.vue'

const circle = 'rounded-full w-4 h-4 border border-black'
const divCircle = `<div class='${circle}'></div>`

function bullets(color: ProcessPerformance) {
  switch (color) {
    case 'GREEN':
      return `<div class='${circle} bg-green-400'></div>${divCircle}${divCircle}${divCircle}`
    case 'ORANGE':
      return `${divCircle}<div class='${circle} bg-orange-400'></div>${divCircle}${divCircle}`
    case 'RED':
      return `${divCircle}${divCircle}<div class='${circle} bg-red-600'></div>${divCircle}`
    case 'GRAY':
      return `${divCircle}${divCircle}${divCircle}<div class='${circle} bg-gray-400'></div>`
  }
}

defineProps<{ process: Process }>()
</script>

<template>
  <div class="flex-row">
    <div class="flex justify-between">
      <p>{{ process.business_date }}</p>
      <p class="flex space-x-1" v-html="bullets(process.performance)"></p>
    </div>
    <div class="flex border-b-2 border-b-gray-300">
      <h3 class="text-xl">{{ process.service }}</h3>
    </div>
  </div>
  <div v-for="event in process.events" :key="event.id" class="m-4">
    <EventCard :event="event" />
  </div>
</template>
