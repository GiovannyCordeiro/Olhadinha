import Header from "../../components/Header";

import style from "./style.module.css";

import linkIcon from "../../assets/linkicon.png"

export default function AboutUsPage() {
    return (
        <>
            <Header />
            <main className={style.main}>
                <h2>História do projeto:</h2>
                <span>
                    O projeto do Olhadinha surgiu quando Giovanny Cordeiro decidiou participar do Hackaton do GitHub e convidou
                    outros amigos para desenvolver um projet para o hackaton com ele, dentre eles o Williams Souza. Em uma sessão
                    de Brainstorming para desenvolvimento de ideias para o projeto, o Williams sugeriu a ideia de um centralizador
                    informações de cashback, onde o usuário encontraria a melhor opção do cashback para a sua compra no dia.
                    Foi nesse momento que surge a ideia do OlhadinhaCashBack.

                    Muitos dos integrantes acabaram desistindo do projeto, que continou sendo desenvolvido pelo
                    Giovanny Cordeiro com ajuda do Williams Souza.
                </span>
                <h2>Propósito:</h2>
                <span>
                    O projeto primordialmente nasceu com o proposito do desenvolvimento de habilidades tecnicas dos amigos e
                    então estudantes universitarios, sem nenhuma pretenção de prejudicar ou denegrir nenhuma informação das
                    respectivas empresas envolvidas.
                </span>
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
                    <div className={style.member}>
                        <div className={style.imgMember}>
                            <img src="https://github.com/willfsouz.png" alt="Giovanny Cordeiro" />
                        </div>
                        <p>Williams Souza</p>
                        <p className={style.office}>Dev & Idealizador</p>
                        <div className={style.links}>
                            <div>
                                <a href="https://www.linkedin.com/in/willfsouz/" target="_blank">
                                    <i>LinkedIn</i>
                                    <img src={linkIcon} alt="LinkedIn Img" />
                                </a>
                            </div>
                            <div>
                                <a href="https://github.com/willfsouz" target="_blank">
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
