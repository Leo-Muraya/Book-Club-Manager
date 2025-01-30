import React, { useEffect, useState } from "react";
import { fetchClubs } from "../api";
import ClubList from "../components/ClubList";

function Home() {
  const [clubs, setClubs] = useState([]);

  useEffect(() => {
    fetchClubs().then(setClubs);
  }, []);

  return <ClubList clubs={clubs} />;
}

export default Home;