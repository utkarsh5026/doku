import React from "react";
import { IMAGE_URL } from "../../urls";
import server from "../../server";

export default function Images() {
  const [images, setImages] = React.useState([]);
  const [loading, setLoading] = React.useState(true);

  React.useEffect(() => {
    const fetchImages = async () => {
      try {
        const response = await server.get(IMAGE_URL);
        const data = response.data;
        setImages(data);
        setLoading(false);
      } catch (error) {
        console.error(error);
      }
    };

    fetchImages();
  }, []);

  return (
    <div>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <ul>
          {images.map((image) => (
            <li key={image.id}>
              <img src={image.url} alt={image.name} />
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
