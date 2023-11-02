import { useParams } from "react-router-dom";
import Header from "../../components/Header";
import ResultSearchCashback from "../../components/ResultSearchCashBack";

export default function SearchCashbackPage() {
    const params = useParams();

    return (
        <>
            <Header />
            <ResultSearchCashback params={params} />
        </>
    );
}
