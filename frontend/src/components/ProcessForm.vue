<script setup lang="ts">
import type { PostProcess } from '@/types/api'
import { ref } from 'vue'
import EventCard from './EventCard.vue'

const commonCls =
  'bg-white border border-slate-300 rounded-md ml-3 py-2 pl-3 pr-3 shadow-sm focus:outline-none focus:border-gray-500 focus:ring-gray-500 focus:ring-1 sm:text-sm'

const process = ref<PostProcess>({
  business_date: undefined,
  working_date: undefined,
  service: undefined,
  performance: undefined,
  events: []
})

const perfChoices = ['GREEN', 'ORANGE', 'RED', 'GRAY']

const postProcess = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/processes/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(process.value)
    })

    const result = await response.json()
    console.log('Success:', result)
  } catch (error) {
    console.error('Error:', error)
  }
}

function handleSumbit() {
  process.value.working_date = process.value.business_date
  postProcess()
}
</script>

<template>
  <div class="pr-4">
    <form @submit.prevent="handleSumbit">
      <div class="mt-4">
        <label for="business_date">Business date:</label>
        <input
          v-model="process.business_date"
          type="date"
          name="business_date"
          id="business_date"
          :class="commonCls"
          required
        />
      </div>
      <div class="mt-4">
        <label for="service">Service:</label>
        <input
          v-model="process.service"
          type="text"
          name="service"
          id="service"
          :class="[commonCls, 'placeholder:italic placeholder:text-slate-400 block w-full']"
          required
          minlength="3"
        />
      </div>
      <div class="mt-4">
        <label for="performance">Performance</label>
        <select
          v-model="process.performance"
          name="performance"
          id="performance"
          :class="commonCls"
          required
        >
          <option disabled value="">Please select one</option>
          <option v-for="(perf, index) in perfChoices" :key="index" :value="perf">
            {{ perf }}
          </option>
        </select>
      </div>
      <div class="m-2">
        <h3 class="text-xl underline underline-offset-4">Events:</h3>
        <div v-for="(event, index) in process.events" :key="index" class="">
          <EventCard :event="event" />
        </div>
      </div>
      <div>
        <button
          class="bg-black hover:bg-gray-500 text-white font-bold mt-4 py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          type="submit"
        >
          Submit
        </button>
      </div>
    </form>
  </div>
</template>
