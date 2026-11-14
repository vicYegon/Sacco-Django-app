import StatusBadge from "./StatusBadge";

function MemberRow({ member }) {
  return (
    <tr>
      <td>{member.fullName}</td>
      <td>{member.phoneNumber}</td>
      <td>{member.email}</td>
      <td>
        <StatusBadge status={member.status}/>
      </td>
    </tr>
  );
}

export default MemberRow;