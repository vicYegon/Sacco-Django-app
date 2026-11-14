import { useState } from "react";
import MemberRow from "./MemberRow";

function MemberList({ members }) {
  const [search, setSearch] = useState("");

  const filteredMembers = members.filter((member) =>
    member.fullName.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <section>
      <input
        type="text"
        placeholder="Search by name"
        value={search}
        onChange={(event) => setSearch(event.target.value)}
      />

      <p>
        Showing {filteredMembers.length} of {members.length} members
      </p>

      {filteredMembers.length === 0 ? (
        <p>No members match "{search}".</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Phone</th>
              <th>Email</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {filteredMembers.map((member) => (
              <MemberRow key={member.id} member={member} />
            ))}
          </tbody>
        </table>
      )}
    </section>
  );
}

export default MemberList;