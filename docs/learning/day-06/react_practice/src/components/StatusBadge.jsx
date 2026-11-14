const STATUS_COLORS = {active: "green", pending: "orange", suspended: "red",};

function StatusBadge({ status }) {
  const color = STATUS_COLORS[status] ?? "gray";

  return (
    <span style={{ color, fontWeight: "bold", textTransform: "capitalize" }}>
      {status}
    </span>
  );
}

export default StatusBadge;