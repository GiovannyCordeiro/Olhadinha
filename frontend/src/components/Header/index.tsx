import styles from "./header.module.css";
import { NavLink } from "react-router-dom";

import logo from "../../assets/logo.svg";
import cardIcon from "../../assets/cardIcon.svg"
import moneyBill from "../../assets/moneyBillIcon.svg"
import moonIcon from "../../assets/moonIcon.svg"

export default function Header() {
    return (
        <header className={styles.header}>
            <NavLink to="/">
                <img src={logo} alt="Olhadinha Logo" />
            </NavLink>
            <nav>
                <ul className={styles.list_links}>
                    <li>
                        <img src={cardIcon} alt="Card Icon" />
                        <NavLink to="/sobre-nos">Sobre nós</NavLink>
                    </li>
                    <li>
                        <img src={moneyBill} alt="Cédula Icon" />
                        <NavLink to="/o-que-e-cashback">
                            O que é cashback?
                        </NavLink>
                    </li>
                    <li>
                        <img src={moonIcon} alt="Lua Icon" />
                        Modo Escuro
                    </li>
                </ul>
            </nav>
        </header>
    );
}