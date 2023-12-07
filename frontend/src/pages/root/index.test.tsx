import "@testing-library/jest-dom";
import { render, screen, fireEvent } from "@testing-library/react";
import { BrowserRouter } from "react-router-dom";
import { describe } from "vitest";


import RootPage from ".";


describe("Root component", () => {
    it("Mock input data and confirming if this same mock in href attribute", async () => {
        render(
            <BrowserRouter>
                <RootPage />
            </BrowserRouter>
        );
        const inputSearch = screen.getByPlaceholderText<HTMLInputElement>("Procurar loja...");
        fireEvent.change(inputSearch, { target: { value: "platform" } });
        const link = screen.getByTestId("RedirectPage");
        expect(link.getAttribute("href")).toBe("/search/platform");
    });

    it("Confirming if rendered text content", async () => {
        render(
            <BrowserRouter>
                <RootPage />
            </BrowserRouter>
        );
        const wrapperText = screen.getByTestId("MainContentUser");
        const listElements = wrapperText.querySelectorAll("span");
        expect(listElements.length).toBe(2);
    })
})