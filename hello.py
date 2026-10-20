
import tkinter as tk

# ---------- Colours ----------
BG = "#20232B"
PANEL = "#2A2E39"
TRACK = "#414654"
BLUE = "#65B9FF"
TEXT = "#E6E8EF"
MUTED = "#9AA3B5"

# ---------- Main window ----------
window = tk.Tk()
window.title("My Compressor")
window.geometry("440x440")
window.configure(bg=BG)
window.resizable(False, False)

# ---------- Header ----------
tk.Label(
    window,
    text="MY COMPRESSOR",
    font=("Arial", 17, "bold"),
    bg=BG,
    fg=TEXT
).pack(pady=(22, 3))

tk.Label(
    window,
    text="AUDIO CONTROL",
    font=("Arial", 9, "bold"),
    bg=BG,
    fg=BLUE
).pack(pady=(0, 18))


# ---------- Custom slider ----------
class CustomSlider(tk.Canvas):
    def __init__(
        self, parent, label, minimum, maximum, initial,
        callback, suffix="", **kwargs
    ):
        super().__init__(
            parent,
            width=340,
            height=76,
            bg=PANEL,
            highlightthickness=0,
            **kwargs
        )

        self.minimum = minimum
        self.maximum = maximum
        self.value = initial
        self.callback = callback
        self.suffix = suffix
        self.label = label

        self.create_text(
            10, 15,
            text=label,
            anchor="w",
            fill=MUTED,
            font=("Arial", 10)
        )

        self.value_text = self.create_text(
            330, 15,
            text=self.format_value(),
            anchor="e",
            fill=TEXT,
            font=("Arial", 10, "bold")
        )

        self.track_start = 12
        self.track_end = 328
        self.track_y = 48

        self.create_line(
            self.track_start, self.track_y,
            self.track_end, self.track_y,
            fill=TRACK, width=5, capstyle="round"
        )

        self.progress = self.create_line(
            self.track_start, self.track_y,
            self.track_start, self.track_y,
            fill=BLUE, width=5, capstyle="round"
        )

        self.knob = self.create_oval(
            0, 0, 14, 14,
            fill=TEXT,
            outline=BLUE,
            width=2
        )

        self.bind("<Button-1>", self.move_slider)
        self.bind("<B1-Motion>", self.move_slider)
        self.draw_slider()

    def format_value(self):
        return f"{self.value:g}{self.suffix}"

    def move_slider(self, event):
        position = max(
            self.track_start,
            min(self.track_end, event.x)
        )

        fraction = (
            (position - self.track_start)
            / (self.track_end - self.track_start)
        )

        self.value = round(
            self.minimum
            + fraction * (self.maximum - self.minimum),
            1
        )

        self.draw_slider()
        self.callback(self.value)

    def draw_slider(self):
        fraction = (
            (self.value - self.minimum)
            / (self.maximum - self.minimum)
        )

        position = (
            self.track_start
            + fraction * (self.track_end - self.track_start)
        )

        self.coords(
            self.progress,
            self.track_start, self.track_y,
            position, self.track_y
        )

        self.coords(
            self.knob,
            position - 7, self.track_y - 7,
            position + 7, self.track_y + 7
        )

        self.itemconfigure(
            self.value_text,
            text=self.format_value()
        )


# ---------- Controls ----------
volume_display = tk.Label(
    window,
    text="Output level: 75%",
    bg=PANEL,
    fg=TEXT,
    font=("Arial", 10)
)

threshold_display = tk.Label(
    window,
    text="Threshold: -20 dB",
    bg=PANEL,
    fg=TEXT,
    font=("Arial", 10)
)
def update_volume(value):
    volume_display.config(
        text=f"Output level: {value:.0f}%"
    )

def update_threshold(value):
    threshold_display.config(
        text=f"Threshold: {value:.1f} dB"
    )
    update_meter(value)


def update_threshold(value):
    threshold_display.config(
        text=f"Threshold: {value:.1f} dB"
    )

volume_slider = CustomSlider(
    window, "OUTPUT VOLUME", 0, 100, 75,
    update_volume, "%"
)
volume_slider.pack(pady=(0, 10))

threshold_slider = CustomSlider(
    window, "THRESHOLD", -60, 0, -20,
    update_threshold, " dB"
)
threshold_slider.pack(pady=(0, 12))


# ---------- Gain reduction meter ----------
meter_frame = tk.Frame(window, bg=PANEL, padx=12, pady=10)
meter_frame.pack(pady=(0, 12), fill="x", padx=50)

meter_title = tk.Label(
    meter_frame,
    text="GAIN REDUCTION",
    bg=PANEL,
    fg=MUTED,
    font=("Arial", 9, "bold")
)
meter_title.pack(anchor="w")

meter_canvas = tk.Canvas(
    meter_frame,
    width=300,
    height=18,
    bg=TRACK,
    highlightthickness=0
)
meter_canvas.pack(pady=(6, 0))

meter_bar = meter_canvas.create_rectangle(
    0, 0, 0, 18,
    fill=BLUE,
    outline=""
)

def update_meter(threshold):
    # Simulated response: lower threshold = more reduction
    reduction = max(0, min(18, (0 - threshold) * 0.3))
    width = 300 * reduction / 18

    meter_canvas.coords(
        meter_bar, 0, 0, width, 18
    )

# ---------- Bypass button ----------
compressor_on = True

def toggle_compressor():
    global compressor_on
    compressor_on = not compressor_on

    if compressor_on:
        power_button.config(
            text="●  COMPRESSOR ON",
            bg=BLUE,
            fg=BG
        )
        status.config(text="PROCESSING ENABLED", fg=BLUE)
    else:
        power_button.config(
            text="○  COMPRESSOR BYPASSED",
            bg=TRACK,
            fg=TEXT
        )
        status.config(text="BYPASS ACTIVE", fg=MUTED)

power_button = tk.Button(
    window,
    text="●  COMPRESSOR ON",
    command=toggle_compressor,
    bg=BLUE,
    fg=BG,
    activebackground="#8BCBFF",
    activeforeground=BG,
    font=("Arial", 10, "bold"),
    relief="flat",
    bd=0,
    padx=18,
    pady=10,
    cursor="hand2"
)
power_button.pack(pady=(0, 10))

status = tk.Label(
    window,
    text="PROCESSING ENABLED",
    bg=BG,
    fg=BLUE,
    font=("Arial", 9, "bold")
)
status.pack()

window.mainloop()
