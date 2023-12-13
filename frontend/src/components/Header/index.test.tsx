import '@testing-library/jest-dom';
import { render, screen } from "@testing-library/react";
import { BrowserRouter } from "react-router-dom";
import { describe } from "vitest";

import Header from ".";

describe("Test Header", () => {
    it("All links rendering", async () => {
        render(
            <BrowserRouter>
                <Header />
            </BrowserRouter>
        )
        expect(
            screen.getByText('O que é cashback?')
            && screen.getByText('Sobre nós')
            && screen.getByText('Modo Escuro')).toBeInTheDocument();
    }),
        it("Redirect to home page", () => {
            render(
                <BrowserRouter>
                    <Header />
                </BrowserRouter>
            )
            expect(screen.getByTestId("logo")).toHaveAttribute("href", "/")
        })
})