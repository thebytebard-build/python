# Dictionary of members (member_id -> name)
members = {
    101: "Alice",
    102: "Bob",
    103: "Charlie"
}

# Function to show all members
def list_members():
    for member_id, name in members.items():
        print(f"{member_id}: {name}")

# Function to check if a member exists
def member_exists(member_id):
    return member_id in members
