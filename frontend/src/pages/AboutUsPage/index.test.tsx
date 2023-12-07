import "@testing-library/jest-dom";
import { render, screen } from "@testing-library/react";
import { BrowserRouter } from "react-router-dom";
import { describe } from "vitest";
import AboutUsPage from ".";

describe("App test", () => {
    it("It component to render in page?", async () => {
        render(
            <BrowserRouter>
                <AboutUsPage />
            </BrowserRouter>
        );
        expect(
            screen.getByText("História do projeto:")
            && screen.getByText("Propósito:")
            && screen.getByText("Equipe:")).toBeInTheDocument();
    });

});
