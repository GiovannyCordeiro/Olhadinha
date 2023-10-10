import { useParams } from "react-router-dom";
import Header from "../../components/Header";

export default function CompanyCashback() {
    const params = useParams();
    return (
        <>
            <Header />
            <h2>Company cashback page {params.companyCashback}</h2>
        </>
    );
}
