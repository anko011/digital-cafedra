import {FC} from 'react'
import {Menu, Text} from '@/share/ui'
import styles from './main-menu.module.scss'
import ToggleButtonTheme from '@/features/toggle-theme/ui'
import {TableIcon} from '@radix-ui/react-icons'
import {FaMapMarkedAlt} from 'react-icons/fa'

const MainMenu: FC = () => {
    return (
        <Menu.Root className={styles.root}>
            <ToggleButtonTheme/>
            
            <Menu.Item href="/">
                <TableIcon/>
                <Text>Реестр</Text>
            </Menu.Item>
            
            <Menu.Item href="/map">
                <FaMapMarkedAlt/>
                <Text>Карта объектов</Text>
            </Menu.Item>
            
            <Menu.Item href="/#">
                <TableIcon/>
                <Text>Реестр</Text>
            </Menu.Item>
        </Menu.Root>
    )
}

MainMenu.displayName = 'MainMenu'

export default MainMenu
