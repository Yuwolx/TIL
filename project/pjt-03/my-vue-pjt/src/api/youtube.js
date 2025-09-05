import axios from 'axios'

const youtube = axios.create({
  baseURL: 'https://www.googleapis.com/youtube/v3',
  params: {
    key: import.meta.env.VITE_YOUTUBE_API_KEY,
    part: 'snippet',
    maxResults: 6,
    type: 'video'
  }
})

export default youtube
