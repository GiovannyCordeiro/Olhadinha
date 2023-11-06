import { useEffect, useState } from "react";
import axios from "axios";
import { UnitPlatform, ParamsProp } from "./typesSearchCashback"

import style from "./resultSearchCashback.module.css"
import arrowIcon from "../../assets/arrow.png"

export default function ResultSearchCashback(props: ParamsProp) {
    const { companyCashback } = props.params;
    const [listCashback, setListCashback] = useState<Array<UnitPlatform>>([]);
    useEffect(() => {
        async function requestForAPI() {
            const responseAPI = await axios.get(`http://localhost:8080/platform/${companyCashback}`)
            const listPlatforms: [UnitPlatform] = responseAPI.data
            setListCashback(listPlatforms)

        }
        requestForAPI()
    }, [])

    let separetedList = listCashback.reduce(
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
        }, { platformsWithCashback: [], platformsNoCashbackPercentage: [] })


    let bestPlatform = separetedList.platformsWithCashback.reduce((max, obj) =>
        (parseInt(obj.percentage) > parseInt(max.percentage) ? obj : max), separetedList.platformsWithCashback[0]
    );

    let worstPlatform = separetedList.platformsWithCashback.reduce((max, obj) =>
        (parseInt(obj.percentage) < parseInt(max.percentage) ? obj : max), separetedList.platformsWithCashback[0]
    );

    let evenPlatforms = separetedList.platformsWithCashback.filter((current) => {
        if (current.namePlatform !== bestPlatform.namePlatform && current.namePlatform !== worstPlatform.namePlatform) {
            return current
        }
    })

    console.log("best platform", bestPlatform)

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
                    {<div className={style.topResultElement}>
                        <div className={style.detailResult} style={{ background: '#47D845' }}>
                            <img src={arrowIcon} alt="" />
                            <span>Maior cashback</span>
                        </div>
                        <div className={style.contentInformation}>
                            <h2>
                                lorem ipsum
                            </h2>
                            <span>Porcentagem: 000%</span>
                        </div>
                    </div>}
                    {
                        evenPlatforms.map((element, index) => (
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
                    {/* <div className={style.lastResultElement}>
                        <div className={style.detailResult} style={{ background: '#FF7979' }}>
                            <img src={arrowIcon} alt="" className={style.arrowLow} />
                            <span>Menor cashback</span>
                        </div>
                        <div className={style.contentInformation}>
                            <h2>
                                {worstPlatform.namePlatform}
                            </h2>
                            <span>Porcentagem: {worstPlatform.percentage}%</span>
                        </div>
                    </div> */}

                    {/* <div className={style.searchNotFoundElement}>
                        <b>Loja não encontrada nesta plataforma</b>
                    </div> */}
                </div>
            </div>
        </main>
    )
}