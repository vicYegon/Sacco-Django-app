import { useEffect, useState } from "react";
import MemberList from "./components/MemberList";
import { members as sampleMembers } from "./data/members";

function App() {
  const [members, setMembers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => {
      setMembers(sampleMembers);
      setLoading(false);
    }, 1000);

    return () => clearTimeout(timer);
  }, []);

  return (
    <main>
      <h1>SACCO Members</h1>
      {loading ? <p>Loading members...</p> : <MemberList members={members} />}
    </main>
  );
}

export default App;