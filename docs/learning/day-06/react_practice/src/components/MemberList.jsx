import { useState } from "react";
import MemberRow from "./MemberRow";

function MemberList({ members }) {
  const [search, setSearch] = useState("");
  const[statusFilter, setStatusFilter] = useState("all");

  const filteredMembers = members.filter((member) =>{
    const matchesName = member.fullName.toLowerCase().includes(search.toLowerCase());
    const matchesStatus = statusFilter === "all" || member.status === statusFilter;

    return matchesName && matchesStatus;
  });

  return (
    <section>
        <input 
            type="text" 
            placeholder="Search by name" 
            value={search}
            onChange={(event) => setSearch(event.target.value)}
        />

        <select value = {statusFilter} onChange = {(event) => setStatusFilter(event.target.value)}>
            <option value="all">All statuses</option>
            <option value="active">Active</option>
            <option value="pending">Pending</option>
            <option value="suspended">Suspended</option>
        </select>

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