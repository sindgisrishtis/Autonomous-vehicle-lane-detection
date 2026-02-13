import cv2
import time
import argparse
from preprocess import preprocess_frame
from detect import region_of_interest, detect_lanes
from visualize import draw_lanes
from logger import log_data


def main(display=True):
    video_path = "data/road_video.mp4"

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("❌ Error: Could not open video file.")
        return

    print("✅ Video started.")

    total_frames = 0
    total_detected = 0
    fps_list = []

    while True:
        start_time = time.time()

        ret, frame = cap.read()
        if not ret:
            print("🎬 End of video reached.")
            break

        frame = cv2.resize(frame, (960, 540))

        edges = preprocess_frame(frame)
        masked = region_of_interest(edges)
        lines = detect_lanes(masked)
        output = draw_lanes(frame.copy(), lines)

        end_time = time.time()
        fps = 1 / (end_time - start_time)
        fps_list.append(fps)

        detected = 1 if lines is not None else 0
        total_frames += 1
        total_detected += detected

        log_data(int(fps), detected)

        if display:
            cv2.putText(
                output,
                f"FPS: {int(fps)}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
            )
            cv2.imshow("Lane Detection", output)

            key = cv2.waitKey(1)
            if key == ord('q') or key == 27:
                break

    cap.release()
    if display:
        cv2.destroyAllWindows()

    if total_frames > 0:
        avg_fps = sum(fps_list) / len(fps_list)
        detection_rate = (total_detected / total_frames) * 100

        print("\n📊 PERFORMANCE REPORT")
        print(f"Total Frames Processed: {total_frames}")
        print(f"Average FPS: {avg_fps:.2f}")
        print(f"Detection Success Rate: {detection_rate:.2f}%")

    print("👋 Finished successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-display", action="store_true",
                        help="Run without GUI display (for Docker)")
    args = parser.parse_args()

    main(display=not args.no_display)
