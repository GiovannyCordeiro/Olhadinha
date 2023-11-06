import { useEffect, useState } from "react";
import axios from "axios";
import { UnitPlatform, ParamsProp } from "./typesSearchCashback"

import style from "./resultSearchCashback.module.css"
import arrowIcon from "../../assets/arrow.png"

export default function ResultSearchCashback(props: ParamsProp) {
    const { companyCashback } = props.params;
    const [bestPlatform, setBestPlatform] = useState<UnitPlatform[]>([]);
    const [worstPlatform, setWorstPlatform] = useState<UnitPlatform[]>([]);
    const [evenPlatform, setEvenPlatform] = useState<UnitPlatform[]>([]);
    const [platformNoCashbackPercentage, setPlatformNoCashbackPercentage] = useState<UnitPlatform[]>([])
    useEffect(() => {
        async function requestForAPI() {
            const responseAPI = await axios.get(`http://localhost:8080/platform/${companyCashback}`)
            const listPlatforms: [UnitPlatform] = responseAPI.data

            let separetedList = listPlatforms.reduce(
                (acc: {
                    platformsWithCashback: UnitPlatform[],
                    platformsNoCashbackPercentage: UnitPlatform[]
                }, cur) => {
                    if (cur.percentage === "SNF") {
                        acc.platformsNoCashbackPercentage.push(cur);
                    } else {
                        acc.platformsWithCashback.push(cur);
                    }
                    return acc;
                }, { platformsWithCashback: [], platformsNoCashbackPercentage: [] });

            setPlatformNoCashbackPercentage(separetedList.platformsNoCashbackPercentage)

            const bestPlatform = [separetedList.platformsWithCashback.reduce((max, obj) =>
                (parseInt(obj.percentage) > parseInt(max.percentage) ? obj : max), separetedList.platformsWithCashback[0]
            )];
            setBestPlatform(bestPlatform)

            let worstPlatform = [separetedList.platformsWithCashback.reduce((max, obj) =>
                (parseInt(obj.percentage) < parseInt(max.percentage) ? obj : max), separetedList.platformsWithCashback[0])];
            setWorstPlatform(worstPlatform)

            let evenPlatforms = separetedList.platformsWithCashback.filter((current) => {
                if (current.namePlatform !== bestPlatform[0].namePlatform && current.namePlatform !== worstPlatform[0].namePlatform) {
                    return current
                }
            })
            setEvenPlatform(evenPlatforms)
        }
        requestForAPI()
    }, [])


    return (
        <main className={style.main}>
            <div className={style.wrapperResults}>
                <div className={style.headerResult}>
                    <p>
                        Melhores cashback para
                        <b> {companyCashback}</b>
                    </p>
                </div>
                <div className={style.wrapperElements}>
                    {
                        bestPlatform.map((element, index) => (
                            <div className={style.topResultElement} key={index}>
                                <div className={style.detailResult} style={{ background: '#47D845' }}>
                                    <img src={arrowIcon} alt="" />
                                    <span>Maior cashback</span>
                                </div>
                                <div className={style.contentInformation}>
                                    <h2>
                                        {element.namePlatform}
                                    </h2>
                                    <span>Porcentagem: {element.percentage}%</span>
                                </div>
                            </div>
                        ))
                    }
                    {
                        evenPlatform.map((element, index) => (
                            <div className={style.intermediaryResultElement} key={index}>
                                <div className={style.contentInformation}>
                                    <h2>
                                        {element.namePlatform}
                                    </h2>
                                    <span>Porcentagem: {element.percentage}%</span>
                                </div>
                            </div>
                        )
                        )
                    }
                    {
                        worstPlatform.map((element, index) => (
                            <div className={style.lastResultElement} key={index}>
                                <div className={style.detailResult} style={{ background: '#FF7979' }}>
                                    <img src={arrowIcon} alt="" className={style.arrowLow} />
                                    <span>Menor cashback</span>
                                </div>
                                <div className={style.contentInformation}>
                                    <h2>
                                        {element.namePlatform}
                                    </h2>
                                    <span>Porcentagem: {element.percentage}%</span>
                                </div>
                            </div>
                        ))
                    }
                    {
                        platformNoCashbackPercentage.map((element, index) => (
                            <div className={style.searchNotFoundElement} key={index}>
                                <h2>{element.namePlatform}</h2>
                                <b>Loja não encontrada nesta plataforma</b>
                            </div>
                        ))
                    }

                </div>
            </div>
        </main>
    )
}