'use client'

import {FC, ReactNode, useLayoutEffect, useRef} from 'react'
import cs from 'classnames'
import styles from './table.module.scss'

type RootProps = {
    children?: ReactNode
}


const Root: FC<RootProps> = ({
    children
}) => {
    const ref = useRef<HTMLTableElement>(null)
    
    useLayoutEffect(() => {
        if (!ref.current) return
        ref.current.classList.remove(styles.tableInvalidPosition)
    }, [])
    
    return (
        <table ref={ref} className={cs(styles.table, styles.tableInvalidPosition)}>
            {children}
        </table>
    )
}

Root.displayName = 'TableRoot'

export {Root}
