import { useEffect, useState } from "react"
import { getAllTask } from "../api/TaskApi"
import TaskCard from "./TaskCard";
import { toast } from "react-hot-toast";

export function TaskList() {
	const [tasks, setTasks] = useState([])

	useEffect(() => {
		async function loadTask() {
			const response = await getAllTask();
			setTasks(response.data);
		}
		
		loadTask();
	}, [tasks]);

	return (
		<div className="grid grid-flow-row gap-2 my-3">
			{
				tasks.map(task => (
					<TaskCard key={task.id} task={task} />
				))
			}
		</div>

	)
}
