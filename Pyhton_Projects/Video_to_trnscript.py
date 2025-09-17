import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import whisper
import os

def transcribe_video():
    # Ask user for video file
    video_path = filedialog.askopenfilename(
        title="Select Video File",
        filetypes=[("Video Files", "*.mp4 *.mkv *.avi *.mov *.flv *.wmv")]
    )
    if not video_path:
        return

    # Ask user where to save transcript
    save_path = filedialog.asksaveasfilename(
        title="Save Transcript As",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if not save_path:
        return

    try:
        # Extract audio using ffmpeg
        audio_path = "temp_audio.wav"
        subprocess.run(
            ["ffmpeg", "-i", video_path, "-ar", "16000", "-ac", "1", "-y", audio_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        # Load whisper model
        model = whisper.load_model("base")  # you can use "small" / "medium" for more accuracy

        # Transcribe
        result = model.transcribe(audio_path)

        # Save transcript
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(result["text"])

        # Cleanup
        os.remove(audio_path)

        messagebox.showinfo("Success", f"Transcript saved to:\n{save_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI setup
root = tk.Tk()
root.title("Video to Transcript")
root.geometry("300x150")

label = tk.Label(root, text="Extract transcript from video", font=("Arial", 12))
label.pack(pady=20)

btn = tk.Button(root, text="Select Video & Transcribe", command=transcribe_video)
btn.pack(pady=10)

root.mainloop()
