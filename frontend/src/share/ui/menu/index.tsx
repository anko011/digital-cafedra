'use client'

import {FC, ReactNode} from 'react'
import NextLink from 'next/link'
import {usePathname} from 'next/navigation'
import * as NavigationMenu from '@radix-ui/react-navigation-menu'
import cs from 'classnames'
import styles from './menu.module.scss'

type ItemProps = {
    href: string
    children?: ReactNode
    active?: boolean
    className?: string
}

type RootProps = {
    children?: ReactNode
    className?: string
}

const Item: FC<ItemProps> = ({
    children,
    href,
    active,
    className
}) => {
    const pathname = usePathname()
    const isActive = active === undefined ? pathname === href : active
    
    return (
        <NavigationMenu.Item className={cs(className, styles.item)}>
            <NextLink href={href} passHref legacyBehavior>
                <NavigationMenu.Link className={styles.link} active={isActive}>{children}</NavigationMenu.Link>
            </NextLink>
        </NavigationMenu.Item>
    )
}

const Root: FC<RootProps> = ({
    children,
    className
}) => {
    return (
        <NavigationMenu.Root orientation="vertical" className={cs(className, styles.root)}>
            <NavigationMenu.List className={styles.list}>
                {children}
            </NavigationMenu.List>
        </NavigationMenu.Root>
    )
}


Root.displayName = 'Root'
Item.displayName = 'Item'

export {Root, Item}
