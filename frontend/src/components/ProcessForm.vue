<script setup lang="ts">
import { type PostEventFormContent, type PostEvent, type PostProcess } from '@/types/api'
import { ref } from 'vue'
import EventCard from './EventCard.vue'

const commonCls =
  'bg-white border border-slate-300 rounded-md ml-3 py-2 pl-3 pr-3 shadow-sm focus:outline-none focus:border-gray-500 focus:ring-gray-500 focus:ring-1 sm:text-sm'

const getInitialProcessState = () => ({
  business_date: undefined,
  working_date: undefined,
  service: undefined,
  performance: undefined,
  events: []
})

const process = ref<PostProcess>(getInitialProcessState())

const getInitialEventState = () => ({
  type: undefined,
  explanation: undefined,
  attachments: [],
  links: [],
  process_id: undefined
})

const getInitialFormEventState = () => ({
  type: '',
  explanation: '',
  attachments: '',
  links: '',
  process_id: undefined
})

const removeEvent = (index: number) => {
  process.value.events.splice(index, 1)
}

const event = ref<PostEvent>(getInitialEventState())
const formEvent = ref<PostEventFormContent>(getInitialFormEventState())

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
    alert('New process was successfully encoded!')
    process.value = getInitialProcessState()
  } catch (error) {
    alert('Something went wrong!')
    console.error('Error:', error)
  }
}

function handleEventSubmit() {
  event.value.type = formEvent.value.type
  event.value.explanation = formEvent.value.explanation
  event.value.process_id = undefined
  event.value.links = formEvent.value.links
    .split(/\s+/)
    .map((s) => ({ url: s, event_id: undefined }))
  event.value.attachments = formEvent.value.attachments
    .split(/\s+/)
    .map((s) => ({ filename: s, event_id: undefined }))
  process.value.events.push(event.value)
  event.value = getInitialEventState()
  formEvent.value = getInitialFormEventState()
}

function handleProcessSubmit() {
  process.value.working_date = process.value.business_date
  postProcess()
}
</script>

<template>
  <div class="grid md:grid-cols-2 gap-8 row-auto w-full m-4 container">
    <div class="flex flex-col">
      <div>
        <h2 class="m-4 text-xl">Events &#8631;</h2>
      </div>
      <div class="m-4 border-2 border-black p-4">
        <form @submit.prevent="handleEventSubmit">
          <div class="m-4">
            <label for="type">Type:</label>
            <input
              v-model="formEvent.type"
              type="text"
              name="type"
              id="type"
              :class="[commonCls, 'placeholder:italic placeholder:text-slate-400 block w-full']"
              required
              minlength="3"
            />
          </div>

          <div class="m-4">
            <label for="explanation">Explanation:</label>
            <textarea
              v-model="formEvent.explanation"
              name="explanation"
              id="explanation"
              rows="2"
              :class="[commonCls, 'placeholder:italic placeholder:text-slate-400 block w-full']"
            >
            </textarea>
          </div>

          <div class="m-4">
            <label for="explanation">Attachments:</label>
            <textarea
              v-model="formEvent.attachments"
              name="explanation"
              id="explanation"
              rows="2"
              :class="[commonCls, 'placeholder:italic placeholder:text-slate-400 block w-full']"
            >
            </textarea>
          </div>

          <div class="m-4">
            <label for="explanation">Links:</label>
            <textarea
              v-model="formEvent.links"
              name="explanation"
              id="explanation"
              rows="2"
              :class="[commonCls, 'placeholder:italic placeholder:text-slate-400 block w-full']"
            >
            </textarea>
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
    </div>
    <div class="m-4 border-2 border-black p-4">
      <form @submit.prevent="handleProcessSubmit">
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
          <span class="text-xl underline underline-offset-4">Events:</span>
          <div v-if="process.events.length > 0">
            <div v-for="(event, index) in process.events" :key="index" class="flex justify-between">
              <EventCard :event="event" />
              <button type="button" @click="removeEvent(index)">&#10060;</button>
            </div>
          </div>
          <div v-else>
            <p class="m-2 mt-4">No events</p>
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
  </div>
</template>
