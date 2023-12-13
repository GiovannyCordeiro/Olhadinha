import "@testing-library/jest-dom";
import { render, screen } from "@testing-library/react";
import { BrowserRouter } from "react-router-dom";
import { describe } from "vitest";
import WhatIsCashbackPage from ".";

describe("WhatIsCashBack Component Test", () => {
    it("Confirming if rendered main topics", async () => {
        render(
            <BrowserRouter>
                <WhatIsCashbackPage />
            </BrowserRouter>
        )
        expect(
            screen.getByText("Como funciona?")
            && screen.getByText("Sobre as plataformas")
            && screen.getByText("Onde o Olhadinha Cashback entra?")).toBeInTheDocument();
    })
})