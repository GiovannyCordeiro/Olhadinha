import { useEffect, useState } from "react";
import axios from "axios";
import { DataRootAPI, ParamsProp } from "./typesSearchCashback"
import style from "./resultSearchCashback.module.css"
import arrowIcon from "../../assets/arrow.png"

export default function ResultSearchCashback(props: ParamsProp) {
    const { companyCashback } = props.params;
    const [responseApi, setResponseApi] = useState<DataRootAPI>({ cuponomia: "", intershop: "", meudimdim: "", zoom: "" });
    useEffect(() => {
        async function responseApi() {
            const requestApi = await axios.get(`http://localhost:8080/platform/${companyCashback}`)
            console.log("respostas", requestApi.data)
            const dataApi: DataRootAPI = await requestApi.data
            setResponseApi(dataApi)
        }
        responseApi()
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
                    <div className={style.topResultElement}>
                        <div className={style.detailResult} style={{ background: '#47D845' }}>
                            <img src={arrowIcon} alt="" />
                            <span>Maior cashback</span>
                        </div>
                    </div>
                    <div className={style.intermediaryResultElement}></div>
                    <div className={style.intermediaryResultElement}></div>
                    <div className={style.intermediaryResultElement}></div>
                    <div className={style.lastResultElement}>
                        <div className={style.detailResult} style={{ background: '#FF7979' }}>
                            <img src={arrowIcon} alt="" className={style.arrowLow} />
                            <span>Menor cashback</span>
                        </div>
                    </div>
                    <div className={style.searchNotFoundElement}>
                        <b>Loja não encontrada nesta plataforma</b>
                    </div>
                </div>
            </div>
        </main>
    )
}