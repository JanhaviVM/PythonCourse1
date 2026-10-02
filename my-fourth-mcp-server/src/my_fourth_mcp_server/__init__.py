from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Employee Leave Management")

# Dummy in-memory database without total quota
EMPLOYEES = {
    "EMP001": {
        "name": "Alice Johnson",
        "Leave Balance": 18,
        "Leave History": ["2026-01-15", "2026-02-10"],
    },
    "EMP002": {
        "name": "Bob Smith",
        "Leave Balance": 19,
        "Leave History": ["2026-03-01"],
    },
    "EMP003": {
        "name": "Charlie Brown",
        "Leave Balance": 25,
        "Leave History": [],
    },
}

@mcp.tool()
def get_leave_summary(employee_id: str) -> str:
    """Get leaves taken, remaining leave balance, and leave history for a specific employee."""
    emp = EMPLOYEES.get(employee_id)
    if not emp:
        return f"Error: Employee ID '{employee_id}' not found."

    history = emp["Leave History"]
    balance = emp["Leave Balance"]
    leaves_taken = len(history)
    formatted_history = ", ".join(history) if history else "No leaves taken"

    return (
        f"Employee: {emp['name']} ({employee_id})\n\n"
        f"--- Leave Balance ---\n"
        f"Leaves Left: {balance} day(s)\n"
        f"Leaves Taken: {leaves_taken} day(s)\n\n"
        f"--- Leave History ---\n"
        f"Dates: {formatted_history}"
    )

@mcp.tool()
def apply_leave(employee_id: str, date: str) -> str:
    """Apply leave for an employee on a specific date (format: YYYY-MM-DD)."""
    emp = EMPLOYEES.get(employee_id)
    if not emp:
        return f"Error: Employee ID '{employee_id}' not found."
    
    if date in emp["Leave History"]:
        return f"Notice: Leave on {date} is already recorded in Leave History for {emp['name']}."
    if emp["Leave Balance"] <= 0:
        return f"Error: {emp['name']} has zero Leave Balance left."

    emp["Leave Balance"] -= 1
    emp["Leave History"].append(date)
    return (
        f"Success: Applied leave for {emp['name']} on {date}.\n"
        f"Updated Leave Balance: {emp['Leave Balance']} day(s) remaining."
    )

if __name__ == "__main__":
    mcp.run()