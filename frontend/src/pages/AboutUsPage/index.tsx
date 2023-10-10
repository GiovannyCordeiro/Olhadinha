import Header from "../../components/Header";

export default function AboutUsPage() {
    document.title = "Sobre nós";
    function sum(a: number, b: number): number {
        return a + b;
    }
    return (
        <>
            <Header />
            <h2>Sobre nos, testing</h2>
            <p data-testid="p_sum">{sum(2, 3)}</p>
        </>
    );
}
