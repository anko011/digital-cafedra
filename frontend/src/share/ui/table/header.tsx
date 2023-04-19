import {Children, FC, ReactNode} from 'react'
import styles from './table.module.scss'

type HeaderProps = {
    children: ReactNode
}

const Header: FC<HeaderProps> = ({
    children
}) => {
    return (
        <thead>
            <tr className={styles.row}>
                {Children.toArray(children).map((child, index) => (
                    <th className={styles.cell} key={index}>{child}</th>
                ))}
            </tr>
        </thead>
    )
}

Header.displayName = 'TableHeader'

export {Header}
