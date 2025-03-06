import csv
import os

def handle_submission(name, email):
    """
    Handles a workshop submission by writing the data to a CSV file.
    """
    data_dir = "data"
    csv_file = os.path.join(data_dir, "submissions.csv")

    # Create the data directory if it doesn't exist
    os.makedirs(data_dir, exist_ok=True)

    file_exists = os.path.isfile(csv_file)

    with open(csv_file, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Name", "Email"])  # Write header if the file is new
        writer.writerow([name, email])

    print(f"Submission recorded: Name={name}, Email={email}")


if __name__ == "__main__":
    # Simulate form submission
    # Replace these values with actual data from your form (if you had a dynamic backend)
    name = "John Doe"
    email = "john.doe@example.com"

    handle_submission(name, email)