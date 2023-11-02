import style from "./resultSearchCashback.module.css"
import arrowIcon from "../../assets/arrow.png"

export default function ResultSearchCashback() {
    return (
        <main className={style.main}>
            <div className={style.wrapperResults}>
                <div className={style.headerResult}>
                    <p>
                        Melhores cashback para
                        <b> Amazon</b>
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
                </div>
            </div>
        </main>
    )
}