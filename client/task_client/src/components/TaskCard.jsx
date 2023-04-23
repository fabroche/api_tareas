import { useNavigate } from "react-router-dom"

export default function TaskCard({ task }) {
    const navigate = useNavigate()

    return (
        <div className="bg-slate-100 hover:bg-slate-200 mx-3 hover:cursor-pointer w-80 rounded-sm shadow-md text-justify"
            onClick={() => {
                navigate(`/task/${task.id}`)
            }}
        >
            <h1 
            className="font-bold uppercase text-zinc-600 p-1">{task.title}</h1>
            <p 
            className="text-zinc-600 p-2"
            >{task.description}</p>
        </div>
    )
}
