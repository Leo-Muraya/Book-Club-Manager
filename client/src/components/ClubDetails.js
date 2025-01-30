import React from "react";
function ClubDetails({ club }) {
  return (
    <div>
      <h2>{club.name}</h2>
      <p>{club.description}</p>
    </div>
  );
}
export default ClubDetails;