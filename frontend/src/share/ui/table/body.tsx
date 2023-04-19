import {FC, ReactNode} from 'react'

type BodyProps = {
    children?: ReactNode
}
const Body: FC<BodyProps> = ({
    children
}) => {
    return (
        <tbody>
            {children}
        </tbody>
    )
}

Body.displayName = 'TableBody'

export {Body}
