'use client'
import {FC} from 'react'

const ToggleButtonTheme: FC = () => {
    
    const clickHandler = () => {
        document.body.classList.toggle('dark-theme')
    }
    
    return (
        <button onClick={clickHandler}>Toggle</button>
    )
}

ToggleButtonTheme.displayName = 'ToggleButtonTheme'

export default ToggleButtonTheme
