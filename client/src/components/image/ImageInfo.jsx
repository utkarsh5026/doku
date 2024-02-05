import React from "react";
import server from "../../server";
import JsonView from "@uiw/react-json-view/editor";
import { githubDarkTheme } from "@uiw/react-json-view/githubDark";
import { IMAGE_URL } from "../../urls";
import { useQuery } from "../../utils";

export default function ImageInfo() {
  const imageId = useQuery().get("id");
  const [imageInfo, setImageInfo] = React.useState({});

  React.useEffect(() => {
    const fetchImageInfo = async () => {
      try {
        const response = await server.get(`${IMAGE_URL}/`, {
          params: {
            id: imageId,
          },
        });
        const data = response.data;
        setImageInfo(data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchImageInfo();
  }, [imageId]);

  return (
    <div>
      <JsonView value={imageInfo} style={githubDarkTheme} />
    </div>
  );
}
