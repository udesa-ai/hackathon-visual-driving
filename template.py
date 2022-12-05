import cv2
import numpy as np


def visual_driver_group_x(image: np.ndarray):
    """Receives an image and returns linear and
    angular velocity to drive a robot"""

    # YOUR CODE HERE

    linear_vel_x = 0.1  # m/s
    angular_vel_z = 0.0  # Rad/s
    return linear_vel_x, angular_vel_z


def segment_color(
    image: np.ndarray, lower_limit=(0, 0, 0), upper_limit=(180, 255, 255)
):
    """Receives an image in BGR colorspace and two limits in HSV colorspace
    and returns amount of pixels inside box, centroid of segmented pixels
    in pixel cordinates and the segmented image"""

    # Convert image from BGR to HSV
    img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Create mask and segment image
    mask = cv2.inRange(img_hsv, lower_limit, upper_limit)
    masked = cv2.bitwise_and(image, image, mask=mask)

    # Count how many segmented pixels
    n_pixels = cv2.countNonZero(mask)

    # Calculate x,y coordinates of center of pixels
    moments = cv2.moments(mask)
    if moments["m00"] == 0:
        return 0, 0, 0, masked
    center_x = int(moments["m10"] / moments["m00"])
    center_y = int(moments["m01"] / moments["m00"])

    return n_pixels, center_x, center_y, masked


def test_driver():
    # Read test image
    img = cv2.imread("vista_turtlebot.jpg")
    # Call driver function
    print(visual_driver_group_x(img))

    # Other useful functions:
    # Segment colors
    n_pixels, cX, cY, masked = segment_color(img, (20, 20, 45), (50, 160, 150))
    print("number of pixels: ", n_pixels)
    # Draw marker in the center of segmented pixels
    cv2.circle(masked, (cX, cY), 5, (0, 0, 255), -1)
    cv2.imshow("Mask Applied to Image", masked)
    cv2.waitKey(0)


if __name__ == "__main__":
    test_driver()
