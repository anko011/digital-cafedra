import {FC, ReactNode} from 'react'
import styles from './icon-card.module.scss'

type IconCardProps = {
    icon: ReactNode
    children: ReactNode
}

const IconCard: FC<IconCardProps> = ({
    icon,
    children,
}) => {
    return (
        <div className={styles.root}>
            <div className={styles.icon}>{icon}</div>
            <div className={styles.content}>{children}</div>
        </div>
    )
}

IconCard.displayName = 'IconCard'

export default IconCard
