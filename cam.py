from cv2 import cv2
import numpy as np


def main():
    video_capture = cv2.VideoCapture(0)

    if video_capture.isOpened():
        rval, frame = video_capture.read()
    else:
        rval = False

    while rval:
        rval, frame = video_capture.read()
        print(to_ascii(frame))

        # Refresh every 50ms -> ~20fps
        key = cv2.waitKey(50)

        # Press escape to end
        if key == 27:
            break


def to_ascii(frame, cols=240, rows=70):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    height, width = frame.shape
    cell_width = width / cols
    cell_height = height / rows
    if cols > width or rows > height:
        raise ValueError("Too many cols or rows.")
    result = ""
    for i in range(rows):
        for j in range(cols):
            gray = np.mean(
                frame[
                    int(i * cell_height) : min(int((i + 1) * cell_height), height),
                    int(j * cell_width) : min(int((j + 1) * cell_width), width),
                ]
            )
            result += gray_to_char(gray)
        result += "\n"
    return result


def gray_to_char(gray):
    char_list = " .:-=+#%@"
    num_chars = len(char_list)
    return char_list[min(int(gray * num_chars / 255), num_chars - 1)]


if __name__ == "__main__":
    main()
