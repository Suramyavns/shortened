import { useEffect, useState } from "react"
import { add } from "./api"

export default function App(){
  const [url,setUrl] = useState('')
  const [uuid,setUuid]=useState('')
  useEffect(()=>{},[])
  return(
    <div className="w-screen h-screen flex-col gap-2 flex justify-center items-center">
      <input type="url" name="url" id="url"
      className="border border-slate-400 p-2 rounded-lg"
      onChange={(e)=>{
        setUrl(e.target.value)
      }}
      placeholder="https://example.com" />
      <button
      className="p-2 bg-blue-600 rounded-lg text-white"
      type="submit"
      onClick={()=>{
        add(url,setUuid)
      }}>
        Submit
      </button>
      <a href={uuid}>your link</a>
    </div>
  )
}