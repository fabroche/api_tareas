import { useForm } from 'react-hook-form'
import { useNavigate, useParams } from 'react-router-dom'

// Apis
import { createTask, deleteTask, updateTask, getTask } from '../api/TaskApi'
import { useEffect } from 'react';
import { toast } from 'react-hot-toast';

// Toast Styles
import { toastDelete, toastCreate, toastUpdate } from '../styles/Toast.styles';

function TaskFormPage() {
	const { register, handleSubmit, formState: { errors }, setValue } = useForm()

	const navigate = useNavigate();

	const params = useParams()

	const onSubmit = handleSubmit(async data => {

		if (params.id) {
			await updateTask(params.id, data)
			toast.success('Tarea Actualizada', ...toastUpdate)
		}
		else {
			await createTask(data);
			toast.success('Tarea Creada', ...toastCreate)
		}

		navigate('/task');
	})

	useEffect(() => {
		async function loadTask() {
			if (params.id) {
				const response = await getTask(params.id);
				setValue('title', response.data.title)
				setValue('description', response.data.description)
			}
		}
		loadTask();
	}, [])

	return (
		<div className='ml-3 max-w-xl mx-auto bg-slate-100 shadow-md p-3 h-96'>
			<form onSubmit={onSubmit}
				className='flex flex-wrap justify-center'
			>
				<input
					type="text"
					placeholder="title"
					className='text-zinc-600 p-3 rounded-lg block shadow-sm'
					{...register("title", { required: true })}
				/>

				{errors.title && <span className='text-red-500'>title is required </span>}


				<textarea
					rows="3"
					placeholder="Description"
					className='text-zinc-600 p-3 rounded-lg block shadow-sm mt-3'
					{...register("description", { required: true })}

				></textarea>

				{errors.description && <span className='text-red-500'>description is required</span>}


				<button className='bg-slate-200 rounded-sm w-3/4 text-zinc-600 font-bold hover:bg-sky-600 hover:text-slate-50 mt-3 shadow-md hover:shadow-lg'>Save</button>
			</form>
			{
				params.id && <button 
				onClick={async () => {
					const accepted = window.confirm('are you sure?')
					if (accepted) {
						await deleteTask(params.id)
						toast.success('Tarea Eliminada', ...toastDelete)
						navigate('/task')
					}
				}}
				className='ml-8 bg-slate-200 rounded-sm w-3/4 text-zinc-600 font-bold hover:bg-red-800 hover:text-slate-50 mt-3 shadow-md hover:shadow-lg'
				>
					Delete
				</button>
			}
		</div>
	)


}

export default TaskFormPage;