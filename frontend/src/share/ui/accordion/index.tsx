'use client'

import {Children, FC, ReactNode} from 'react'
import * as RadixAccordion from '@radix-ui/react-accordion'
import styles from './accordion.module.scss'
import {TriangleRightIcon} from '@radix-ui/react-icons'

type AccordionProps = {
    children?: ReactNode
}

type AccordionItemProps = {
    children?: ReactNode
    header?: ReactNode
}

const Item: FC<AccordionItemProps> = ({
    children,
    header
}) => {
    return (
        <>
            <RadixAccordion.Header>
                <RadixAccordion.Trigger className={styles.trigger}>
                    {header}
                    <TriangleRightIcon
                        className={styles.triangleIcon}
                    />
                </RadixAccordion.Trigger>
            </RadixAccordion.Header>
            <RadixAccordion.Content className={styles.content}>{children}</RadixAccordion.Content>
        </>
    )
}


const Root: FC<AccordionProps> = ({
    children,
}) => {
    return (
        <RadixAccordion.Root type="single" collapsible className={styles.root}>
            {Children.toArray(children).map((item, index) => (
                <RadixAccordion.Item key={index} value={`item-${index}`}>
                    {item}
                </RadixAccordion.Item>
            ))}
        </RadixAccordion.Root>
    )
}

Root.displayName = 'Accordion.Root'
Item.displayName = 'Accordion.Item'

export {Root, Item}
