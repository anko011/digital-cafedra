'use client'

import {FC, Fragment, useEffect, useState} from 'react'
import * as NavigationMenu from '@radix-ui/react-navigation-menu'
import cs from 'classnames'
import {Text} from '@/share/ui'
import styles from './QuickAccessMenu.module.scss'

type AccessLink = {
    id: string
    label: string
}

type QuickAccessMenuProps = {
    elements: AccessLink[]
    className?: string
}

type QuickAccessMenuItemProps = {
    children: string
    forId: string
    isActive?: boolean
}

const Item: FC<QuickAccessMenuItemProps> = ({children, forId, isActive = false}) => {
    return <a href={forId} className={cs({[styles.active]: isActive})}><Text>{children}</Text></a>
}

const QuickAccessMenu: FC<QuickAccessMenuProps> = ({
    elements,
    className
}) => {
    const [activeId, setActiveId] = useState(elements[0].id)
    
    useEffect(() => {
        
        const observable = elements.map(element => document.querySelector(element.id))
        
        const callback: IntersectionObserverCallback = (entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    setActiveId(`#${entry.target.id}`)
                }
            })
        }
        
        const observer = new IntersectionObserver(callback, {
            rootMargin: '1px'
        })
        
        observable.forEach(element => element && observer.observe(element))
    }, [])
    return (
        <NavigationMenu.Root className={cs(className, styles.root)} orientation="horizontal">
            <NavigationMenu.List>
                {elements.map((element, index, arr) => (
                    <Fragment key={element.id}>
                        <Item
                            forId={element.id}
                            isActive={activeId === element.id}
                        >
                            {element.label}
                        </Item>
                        {index !== arr.length - 1 && <span> / </span>}
                    </Fragment>
                ))}
            </NavigationMenu.List>
        </NavigationMenu.Root>
    )
}

QuickAccessMenu.displayName = 'QuickAccessMenu'
Item.displayName = 'QuickAccessMenuItem'

export default QuickAccessMenu
