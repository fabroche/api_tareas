import React from 'react'
import { Link } from 'react-router-dom'

function Navigation() {
    return (
        <div className='justify-start mr-1'>
            <Link to='/task'>
                <h1 className='bg-slate-100 text-zinc-900 rounded-md mb-3 ml-3 mt-3 text-center hover:bg-slate-200 font-bold uppercase'>
                    Task App
                </h1>
            </Link>
            <Link to='/task-create'>
                <h1 className='bg-slate-100 hover:bg-slate-200 text-zinc-900 rounded-md text-center mb-3 ml-3 mt-3 font-bold uppercase'>
                    Create Task
                </h1>
            </Link>

        </div>
    )
}

export default Navigation;
