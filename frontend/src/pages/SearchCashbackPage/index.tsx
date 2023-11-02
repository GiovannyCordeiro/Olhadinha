import { useParams } from "react-router-dom";
import Header from "../../components/Header";
import axios from "axios";
import { useEffect, useState } from "react";
import ResultSearchCashback from "../../components/ResultSearchCashBack";

interface DataRootAPI {
    data: string;
    status: string;
    origin: string;
}

export default function SearchCashbackPage() {
    const params = useParams();
    const [responseApi, setResponseApi] = useState<DataRootAPI>({ data: "", status: "", origin: "" });
    useEffect(() => {
        async function responseApi() {
            const requestApi = await axios.get(`${import.meta.env.VITE_CONNECTION_BACK || "http://localhost:8080/"}`)
            const dataApi: DataRootAPI = await requestApi.data
            setResponseApi(dataApi)
        }
        responseApi()
    }, [])
    return (
        <>
            <Header />
            <ResultSearchCashback />
        </>
    );
}
