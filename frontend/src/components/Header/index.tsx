import { NavLink } from "react-router-dom";
import { useState } from "react";

import styles from "./header.module.css";

import logo from "../../assets/logo.svg";
import cardIcon from "../../assets/cardIcon.svg"
import moneyBill from "../../assets/moneyBillIcon.svg"
import moonIcon from "../../assets/moonIcon.svg"
import closeIcon from "../../assets/closeIcon.svg"
import menuHamburguer from "../../assets/menuHamburguer.svg"

export default function Header() {
    const [sideMenu, setSideMenu] = useState(false);

    function clickButton() {
        !sideMenu ? setSideMenu(true) : setSideMenu(false)
    }

    function handlerResize() {
        if (window.innerWidth <= 1300) {
            setSideMenu(false);
        }
    }

    window.addEventListener("resize", handlerResize);

    return (
        <header className={styles.header}>
            <div className={styles.wrapper_header}>
                <NavLink to="/">
                    <img src={logo} alt="Olhadinha Logo" />
                </NavLink>
                <div className={styles.wrapper_hambunguer} onClick={clickButton}>
                    <img src={menuHamburguer} alt="menu hamburguer" />
                </div>
                <div className={!sideMenu ? styles.wrapper_nav_off : styles.wrapper_nav_on}>
                    <nav>
                        <div className={styles.closedButtonMobile} onClick={clickButton}>
                            <img src={closeIcon} alt="close icon" />
                        </div>
                        <ul className={styles.list_links}>
                            <li>
                                <img src={cardIcon} alt="Card Icon" />
                                <NavLink to="/sobre-nos">Sobre nós</NavLink>
                            </li>
                            <li>
                                <img src={moneyBill} alt="Cédula Icon" />
                                <NavLink to="/o-que-e-cashback">
                                    O que é cashback? test
                                </NavLink>
                            </li>
                            <li>
                                <img src={moonIcon} alt="Lua Icon" />
                                <span>
                                    Modo Escuro
                                </span>
                            </li>
                        </ul>
                    </nav>
                </div>
            </div>
        </header>
    );
}