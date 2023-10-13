import { useParams } from "react-router-dom";
import Header from "../../components/Header";
import axios from "axios";
import { useEffect, useState } from "react";

interface DataRootAPI {
    data: string;
    status: string;
}

export default function SearchCashbackPage() {
    const params = useParams();
    const [responseApi, setResponseApi] = useState<DataRootAPI>({ data: "", status: "" });
    useEffect(() => {
        async function responseApi() {
            const requestApi = await axios.get("http://localhost:8080/")
            const dataApi: DataRootAPI = await requestApi.data
            setResponseApi(dataApi)
        }
        responseApi()
    }, [])
    return (
        <>
            <Header />
            <h2>Company cashback page {params.companyCashback}</h2>
            <span>{responseApi.data}</span>
        </>
    );
}
