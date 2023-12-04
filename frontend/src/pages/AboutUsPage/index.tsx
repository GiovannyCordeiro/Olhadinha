import Header from "../../components/Header";

import style from "./style.module.css";

import linkIcon from "../../assets/linkicon.png"

export default function AboutUsPage() {
    return (
        <>
            <Header />
            <main className={style.main}>
                <h2>Historia:</h2>
                <span>Lorem ipsum </span>
                <h2>Proposito:</h2>
                <span>Lorem ipsum </span>
                <h2>Equipe:</h2>
                <div className={style.wrapper_team}>
                    <div className={style.member}>
                        <div className={style.imgMember}>
                            <img src="https://github.com/GiovannyCordeiro.png" alt="Giovanny Cordeiro" />
                        </div>
                        <p>Giovanny Cordeiro</p>
                        <p className={style.office}>Dev & Idealizador</p>
                        <div className={style.links}>
                            <div>
                                <a href="https://www.linkedin.com/in/giovannycordeiro/" target="_blank">
                                    <i>LinkedIn</i>
                                    <img src={linkIcon} alt="LinkedIn Img" />
                                </a>
                            </div>
                            <div>
                                <a href="https://github.com/GiovannyCordeiro" target="_blank">
                                    <i>GitHub</i>
                                    <img src={linkIcon} alt="GitHub Img" />
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </main>
        </>
    );
}
