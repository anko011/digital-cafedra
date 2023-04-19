'use client'

import {FC, ReactNode, useLayoutEffect, useRef} from 'react'
import {Row} from './row'
import styles from './table.module.scss'

type AccordionRowProps = {
    children: JSX.Element[]
    content: ReactNode
}


const AccordionRow: FC<AccordionRowProps> = ({
    children,
    content
}) => {
    
    const ref = useRef<HTMLDivElement>(null)
    
    
    const clickHandler = () => {
        if (!ref.current) return
        
        if (ref.current.classList.contains(styles.accordionContentHide)) {
            ref.current.classList.replace(styles.accordionContentHide, styles.accordionContentShow)
        } else {
            ref.current.classList.replace(styles.accordionContentShow, styles.accordionContentHide)
        }
    }
    
    useLayoutEffect(() => {
        if (!ref.current) return
        const table = ref.current.closest('table') as HTMLTableElement
        const td = ref.current.closest('td') as HTMLTableDataCellElement
        
        const columns = table.tHead?.querySelectorAll('th').length
        td.colSpan = columns ?? 0
        ref.current.classList.add(styles.accordionContentHide)
        setTimeout(() => ref.current?.classList.add(styles.accordionContentAnimation), 0)
    }, [])
    
    return (
        <>
            <Row onClick={clickHandler} className={styles.accordionRowHeader}>
                {children}
            </Row>
            <tr>
                <td>
                    <div
                        ref={ref}
                        className={styles.accordionContent}
                    >
                        {content}
                    </div>
                </td>
            </tr>
        </>
    )
}


AccordionRow.displayName = 'TableAccordionRow'

export {AccordionRow}
