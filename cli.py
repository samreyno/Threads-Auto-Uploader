import argparse
from threads_uploader.uploader import ThreadsUploader


def main():
    parser = argparse.ArgumentParser(description="Threads Uploader")

    parser.add_argument("--caption", help="Text content")
    parser.add_argument("--image", help="Image URL")
    parser.add_argument("--video", help="Video URL")

    args = parser.parse_args()
    uploader = ThreadsUploader()

    if args.image:
        result = uploader.post_image(args.image, args.caption)
    elif args.video:
        result = uploader.post_video(args.video, args.caption)
    elif args.caption:
        result = uploader.post_text(args.caption)
    else:
        parser.error("No content provided")

    print("Done:")
    print(result)


if __name__ == "__main__":
    main()
