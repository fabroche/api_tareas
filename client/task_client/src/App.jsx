import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import './App.css'
import TaskPage from './pages/TaskPage'
import TaskFormPage from './pages/TaskFormPage'
import Navigation from './components/Navigation'
import { Toaster } from 'react-hot-toast'


function App() {

  return (
    <BrowserRouter>
      <div 
      className='container flex flex-1 w-max h-fit mx-auto m-3 p-3'>
        <div className='container grid grid-cols-5 shadow-md bg-slate-50 max-w-md rounded-md'>
        <Navigation />

        <Routes>
          <Route path='/' element={<Navigate to='/task' />} />
          <Route path='/task' element={<TaskPage />} />
          <Route path='/task-create' element={<TaskFormPage />} />
          <Route path='/task/:id' element={<TaskFormPage />} />

        </Routes>
        <Toaster />
        </div>
        {/* <div 
        className='container shadow-md bg-slate-50 grid grid-cols-7 content-center text-zinc-900 min-w-sm rounded-md ml-9'>
          <h1>Preview</h1>
        </div> */}
      </div>
    </BrowserRouter>
  )
}

export default App;