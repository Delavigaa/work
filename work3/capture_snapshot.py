import cv2
import os

def capture_snapshot(username):
    # Define the path dynamically based on username
    save_dir = os.path.expanduser(f"~/Downloads/scrfd/datasets/new_persons/{username}")
    os.makedirs(save_dir, exist_ok=True)

    # Initialize the camera
    cap = cv2.VideoCapture(0)  # Adjust '0' if you have multiple cameras and want to select a different one

    # Capture a single photo
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image.")
        return

    # Save the captured image
    file_path = os.path.join(save_dir, f"{username}.jpg")
    cv2.imwrite(file_path, frame)
    print(f"Snapshot saved at {file_path}")

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    username = "Mohamed"  # Replace 'user_name' with the actual username or modify to accept user input
    capture_snapshot(username)
