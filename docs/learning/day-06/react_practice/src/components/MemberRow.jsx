function MemberRow({ member }) {
  return (
    <tr>
      <td>{member.fullName}</td>
      <td>{member.phoneNumber}</td>
      <td>{member.email}</td>
      <td>{member.status}</td>
    </tr>
  );
}

export default MemberRow;