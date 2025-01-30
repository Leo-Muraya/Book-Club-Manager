import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { fetchClubDetails } from "../api";

function ClubPage() {
  const { id } = useParams();
  const [club, setClub] = useState(null);

  useEffect(() => {
    fetchClubDetails(id).then(setClub);
  }, [id]);

  if (!club) return <p>Loading...</p>;
  return (
    <div>
      <h1>{club.name}</h1>
      <p>{club.description}</p>
    </div>
  );
}

export default ClubPage;
