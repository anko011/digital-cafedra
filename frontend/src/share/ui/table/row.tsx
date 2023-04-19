import {FC} from 'react'
import cs from 'classnames'
import styles from './table.module.scss'

type RowProps = {
    children: JSX.Element[]
    className?: string
    onClick?: () => void
}

const Row: FC<RowProps> = ({
    children,
    className,
    onClick
}) => {
    
    
    return (
        <tr className={cs(className, styles.row)} onClick={onClick}>
            {children.map((child, index) => (
                <td className={styles.cell} key={index}>{child}</td>
            ))}
        </tr>
    
    )
}

Row.displayName = 'TableRow'

export {Row}
