import { useParams } from "react-router-dom";
import Header from "../../components/Header";

export default function SearchCashbackPage() {
    const params = useParams();
    return (
        <>
            <Header />
            <h2>Company cashback page {params.companyCashback}</h2>
        </>
    );
}
