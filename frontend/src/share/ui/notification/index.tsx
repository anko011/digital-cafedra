import {FC} from 'react'
import styles from './notification.module.scss'
import {Text} from '@/share/ui'
import {CheckIcon, ExclamationTriangleIcon} from '@radix-ui/react-icons'

type NotificationProps = {
    children?: string
    variant?: 'success' | 'error'
}

const Notification: FC<NotificationProps> = ({
    children,
    variant = 'success'
}) => {
    return (
        <div className={styles.root}>
            {variant === 'success'
                ? <CheckIcon className={styles.successIcon} width={24} height={24}/>
                : <ExclamationTriangleIcon className={styles.errorIcon} width={20} height={20}/>}
            <Text className={styles.text}>{children}</Text>
        </div>)
    
}

Notification.displayName = 'Notification'

export default Notification
