import Header from "../../components/Header";
import styles from "./index.module.css"

import LogoCuponomia from "../../assets/logos/cuponomiaLogo.png"
import LogoMeliuz from "../../assets/logos/meliuzLogo.png"
import LogoZoom from "../../assets/logos/zoomLogo.png"
import LogoInterShop from "../../assets/logos/intershopLogo.svg"

export default function WhatIsCashbackPage() {

    document.title = "O que é cashback?";

    return (
        <>
            <Header />

            <main className={styles.WhatIsMain}>
                <div className={styles.WhatIsContent}>
                    <div className={styles.WhatIs}>
                        <h1>O que é cashback?</h1>
                        <p>
                            Cashback é um programa de recompensas que devolve uma porcentagem do valor gasto em compras realizadas em determinada loja.<br />
                            Essa porcentagem é diferente para cada loja e atualiza diariamente, seja para mais ou para menos, mas geralmente existe uma porcentagem base para cada loja.
                            Independente do valor, é possível receber cashback ao realizar compras em praticamente todos os sites hoje em dia. <br />
                        </p>
                    </div>

                    <div className={styles.HowItWorks}>
                        <h1>Como funciona?</h1>
                        <p>
                            Ao decidir realizar uma compra online, você pode acessar uma das plataforma de cashback e verificar qual a porcentagem de retorno que eles oferecem. <br />
                            Você irá acessar o site da loja pelo link da plataforma escolhida e continuar a compra normalmente. <br />
                            Assim que a plataforma rastrear que uma compra foi feita pelo link e calcular a porcentagem de cashback, o valor irá constar no seu extrato na plataforma junto com o prazo para confirmar o cashback.<br />
                            Quando confirmado, você receberá o saldo na plataforma e poderá transferir para sua conta no banco.
                        </p>
                    </div>

                    <div className={styles.HowWeHelp}>
                        <h1>Onde o Olhadinha Cashback entra?</h1>
                        <p>
                            Por haver diversas plataformas de cashback, fica trabalhoso ter que buscar uma por uma para ver o cashback de uma loja, então sentimos falta de algo que facilitasse essa busca. <br />
                            Precisando apenas buscar a loja, o Olhadinha lista qual plataforma está com a maior porcentagem. <br />
                            Selecionamos as principais plataformas e que nós mesmos utilizamos e aprovamos.
                        </p>
                    </div>

                    <div className={styles.AboutPlataforms}>
                        <h1>Sobre as plataformas</h1>
                        <p>
                            Cada plataforma tem condições diferentes, seja de porcentagem, prazo para confirmação ou resgate. <br />
                            A porcentagem atualiza diariamente, então hoje pode oferecer um cashback maior em uma plataforma do que em outra e amanhã isso pode ser diferente. <br />
                            O prazo de confirmação é diferente em cada plataforma e cada loja possui um tempo médio estimado, o qual é bem difícil ultrapassar. <br />
                        </p>
                    </div>

                    <div className={styles.TheFourPlataforms}>
                        <div className={styles.AboutMeliuz}>
                            <div className={styles.LogoMeliuz}>
                                <img src={LogoMeliuz} alt="Méliuz Logo" />
                            </div>

                            <div className={styles.PlataformDetails}>
                                <span>
                                    Oferece além do cashback comum, o cashback em notas fiscais, cartão com cashback, criptomoeda, testador de cupons, etc.
                                </span>

                                <span>
                                    <strong>Prazo de confirmação:</strong> <br />
                                    Em média de 45 a 90 dias, <br />
                                    Prazo máximo é de 120 dias.
                                </span>

                                <span>
                                    <strong>Bônus de indicação:</strong> <br />
                                    Valores que alternam quase que semanalmente entre: <br />
                                    R$ 20, R$ 30, R$ 50 ou indicar 5 amigos e receber R$ 1000. <br />
                                    <strong>OBS: </strong>Consultar regulamento para entender as condições.
                                </span>
                            </div>
                        </div>

                        <div className={styles.AboutCuponomia}>
                            <div className={styles.LogoCuponomia}>
                                <img src={LogoCuponomia} alt="Cuponomia Logo" />
                            </div>

                            <div className={styles.PlataformDetails}>
                                <span>
                                    Oferece além do cashback em lojas, um catálogo de gift cards, cupons extensão de navegador, etc. <br />
                                </span>

                                <span>
                                    <strong>Prazo de confirmação:</strong> <br />
                                    Em média de 45 a 90 dias, <br />
                                    Prazo máximo é de 120 dias.
                                </span>

                                <span>
                                    <strong>Bônus de indicação:</strong> <br />
                                    Valores que alternam quase que semanalmente entre: <br />
                                    R$ 5, R$ 20 ou R$ 30. <br />
                                    <strong>OBS: </strong>Consultar regulamento para entender as condições.
                                </span>

                            </div>
                        </div>

                        <div className={styles.AboutInterShop} >
                            <div className={styles.LogoInterShop} >
                                <img src={LogoInterShop} alt="" />
                            </div>

                            <div className={styles.PlataformDetails}>
                                <span>
                                    Oferece no Super App do Banco Inter um catálogo de produtos com cashback diretamente no app ou a opção padrão de cashback via direcionamento para o site da loja. A porcentagem é diferente se comprar no Inter Shop ou pelo link de direcionamento. Também é diferente a porcentagem se o usuário já for correntista do banco ou não.
                                </span>

                                <span>
                                    <strong>Prazo de confirmação:</strong> <br />
                                    Dentro do Super App: 1 dia <br />
                                    Direcionamento por link: 30 dias para correntistas e cerca de 45 para não correntistas <br />
                                    Prazo máximo informado pela plataforma: 120 dias.
                                </span>
                            </div>
                        </div>

                        <div className={styles.AboutZoom} >
                            <div className={styles.LogoZoom} >
                                <img src={LogoZoom} alt="Zoom Logo" />
                            </div>

                            <div className={styles.PlataformDetails} >
                                <span>
                                    Também usado para busca e comparativo de preços de produtos, o Zoom oferece cashback via direcionamento para a loja, cartão com cashback, alerta de preço, cupons, etc.
                                </span>

                                <span>
                                    <strong>Prazo de confirmação:</strong>  <br />
                                    Até 10 dias para rastrear a compra e em aproximadamente 60 dias dias após a entrega do seu pedido, o saldo fica disponível, mas geralmente é aprovado bem antes.
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
            </main >
        </>
    );
}