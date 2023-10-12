import { createBrowserRouter, RouterProvider } from "react-router-dom";

import RootPage from "./pages/root";
import WhatIsCashbackPage from "./pages/WhatIsCashbackPage";
import AboutUsPage from "./pages/AboutUsPage";
import SearchCashbackPage from "./pages/SearchCashbackPage";

function App() {
    const routes = createBrowserRouter([
        { path: "/", element: <RootPage /> },
        { path: "/sobre-nos", element: <AboutUsPage /> },
        { path: "/o-que-e-cashback", element: <WhatIsCashbackPage /> },
        { path: "/search/:companyCashback", element: <SearchCashbackPage /> },

    ]);
    return <RouterProvider router={routes} />;
}

export default App;
