'use client'

import {FC} from 'react'
import {Map as YMap, YMaps} from '@pbe/react-yandex-maps'
import styles from './projects-map.module.scss'

const ProjectsMap: FC = () => {
    return (
        <div className={styles.wrapper}>
            <YMaps>
                <YMap
                    className={styles.map}
                    state={{
                        center: [55.75, 37.57],
                        zoom: 9,
                    }}
                />
            </YMaps>
        </div>
    )
}

ProjectsMap.displayName = 'ProjectsMap'

export {ProjectsMap}
