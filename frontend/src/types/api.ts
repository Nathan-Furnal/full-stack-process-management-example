export type Link = {
  id: number
  url: string
  event_id: number | undefined
}

export type Attachment = {
  id: number
  filename: string
  event_id: number | undefined
}

export type Event = {
  id: number
  type: string
  explanation: string
  attachements: Attachment[]
  links: Link[]
  process_id: number | undefined
}

export type ProcessPerformance = 'GREEN' | 'ORANGE' | 'RED' | 'GRAY'

export type Process = {
  id: number
  business_date: Date
  working_date: Date
  service: string
  performance: ProcessPerformance
  events: Event[]
}
