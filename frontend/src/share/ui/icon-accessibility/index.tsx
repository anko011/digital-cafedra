'use client'
import * as Accessibility from '@radix-ui/react-accessible-icon'
import {FC} from 'react'
import {AccessibleIconProps} from '@radix-ui/react-accessible-icon'

const AccessibilityIcon: FC<AccessibleIconProps> = (props) => <Accessibility.Root {...props} />

AccessibilityIcon.displayName = 'AccessibilityIcon'

export default AccessibilityIcon
