import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { fetchClubs } from "../api";

const ClubList = () => {
  const [clubs, setClubs] = useState([]);

  useEffect(() => {
    fetchClubs().then(setClubs);
  }, []);

  return (
    <div>
      <h2>My Book Clubs</h2>
      <ul>
        {clubs.map((club) => (
          <li key={club.id}>
            <Link to={`/clubs/${club.id}`}>{club.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ClubList;
