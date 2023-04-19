import {FC} from 'react'
import {Inter} from 'next/font/google'
import cs from 'classnames'
import styles from './text.module.scss'

const inter = Inter({
    subsets: ['cyrillic']
})

type TextProps = {
    children?: string
    as?: 'span' | 'h1' | 'h2' | 'h3' | 'h4' | 'p'
    size?: number
    bolder?: boolean
    className?: string
}

const Text: FC<TextProps> = ({
    children,
    as = 'span',
    size = 1,
    bolder = false,
    className
}) => {
    const Tag = as
    
    return (
        <Tag
            className={cs(
                className,
                inter.className,
                styles.root,
                styles[`size${size}`],
                {[styles.bold]: bolder})
            }
        >{children}</Tag>
    )
}

Text.displayName = 'Text'

export default Text
