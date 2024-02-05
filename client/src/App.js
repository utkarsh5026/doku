import "./App.css";
import { createBrowserRouter } from "react-router-dom";
import ImageInfo from "./components/image/ImageInfo";
const router = createBrowserRouter([
  {
    path: "/images",
    element: <ImageInfo />,
  },
]);

export default router;
