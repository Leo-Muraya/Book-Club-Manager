import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { fetchClubDetails } from "../api";

const ClubDetails = () => {
  const { id } = useParams();
  const [club, setClub] = useState(null);

  useEffect(() => {
    fetchClubDetails(id).then(setClub);
  }, [id]);

  if (!club) return <p>Loading...</p>;

  return (
    <div>
      <h2>{club.name}</h2>
      <p>{club.description}</p>
      <h3>Books:</h3>
      <ul>
        {club.books.map((book) => (
          <li key={book.id}>{book.title}</li>
        ))}
      </ul>
    </div>
  );
};

export default ClubDetails;
