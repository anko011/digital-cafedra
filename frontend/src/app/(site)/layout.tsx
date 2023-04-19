import '@/app/styles/globals.scss'
import {ReactNode} from 'react'
import MainMenu from '@/widgets/main-menu/ui'
import styles from './layouts.module.scss'

export const metadata = {
    title: 'System of control building projects',
    description: 'System of control building projects',
}

export default function RootLayout({
    children,
}: {
    children: ReactNode
}) {
    return (
        <html lang="ru">
            <body className={styles.root}>
                <MainMenu/>
                <main className={styles.content}>
                    {children}
                </main>
            </body>
        </html>
    )
}
