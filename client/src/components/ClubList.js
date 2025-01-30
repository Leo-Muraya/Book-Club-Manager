import React from "react";
import { Link } from "react-router-dom";

function ClubList({ clubs }) {
  return (
    <ul>
      {clubs.map((club) => (
        <li key={club.id}>
          <Link to={`/clubs/${club.id}`}>{club.name}</Link>
        </li>
      ))}
    </ul>
  );
}
export default ClubList;