from pypylon import pylon
import cv2

# Initialize the pylon runtime system
pylon.Initialize()

# Replace with the actual IP address of your Basler camera
camera_ip_address = "169.254.9.7"

# Create an InstantCamera object
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateDeviceByIPAddress(camera_ip_address))
camera.Open()

try:
    # Set camera properties if needed
    # For example, setting exposure time
    camera.ExposureTime.SetValue(10000)  # Set exposure time to 10000 microseconds

    # Start grabbing images
    camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

    while camera.IsGrabbing():
        grab_result = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

        if grab_result.GrabSucceeded():
            image = grab_result.Array

            # Display the image using OpenCV
            cv2.imshow("Camera Image", image)
            key = cv2.waitKey(1)
            if key == 27:  # Press ESC to exit
                break

        grab_result.Release()

finally:
    # Stop grabbing and close the camera
    camera.StopGrabbing()
    camera.Close()

    # Terminate the pylon runtime system
    pylon.Terminate()

    # Close OpenCV windows
    cv2.destroyAllWindows()
