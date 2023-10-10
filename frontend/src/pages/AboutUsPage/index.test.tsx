import "@testing-library/jest-dom";
import { render, screen } from "@testing-library/react";
import { BrowserRouter } from "react-router-dom";
import { describe, test } from "vitest";
import AboutUsPage from ".";

describe("App test", () => {
    test("It component to render in page?", () => {
        render(
            <BrowserRouter>
                <AboutUsPage />
            </BrowserRouter>
        );
        expect(screen.getByText("Sobre nos, testing")).toBeInTheDocument();
    });

    test("testing text element create dinamic", () => {
        render(
            <BrowserRouter>
                <AboutUsPage />
            </BrowserRouter>
        );
        expect(screen.getByTestId("p_sum")).toHaveTextContent("5");
    });
});
