export type Link = {
  id: number
  url: string
  event_id: number | undefined
}

export type PostLink = {
  url: string | undefined
  event_id: number | undefined
}

export type Attachment = {
  id: number
  filename: string
  event_id: number | undefined
}

export type PostAttachment = {
  filename: string | undefined
  event_id: number | undefined
}

export type Event = {
  id: number
  type: string
  explanation: string
  attachments: PostAttachment[]
  links: PostLink[]
  process_id: number | undefined
}

export type PostEvent = {
  type: string | undefined
  explanation: string | undefined
  attachments: PostAttachment[]
  links: PostLink[]
  process_id: number | undefined
}

export type PostEventFormContent = {
  type: string | undefined
  explanation: string | undefined
  attachments: string
  links: string
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

export type PostProcess = {
  business_date: Date | undefined
  working_date: Date | undefined
  service: string | undefined
  performance: ProcessPerformance | undefined
  events: PostEvent[]
}
