# **simpleTimer** ⏳  
*A minimalist, Vim-inspired timer with command-based control.*

## **Features**
- Simple timer with **Vim-like commands** (hidden input, no popups).
- Minimalistic design with **mode-based control**.
- Color-coded time display to indicate urgency.
- **Flashing effect** for invalid commands (inspired by the terminal's visual bell).
- Optional **caption toggle** for a cleaner interface.

---

## **Usage**
### **Modes**
- `NORMAL` – Default state, can set the timer.
- `COUNTDOWN` – Active countdown state.

### **Commands** (Press `:` to enter command mode)
| Command       | Description | Available in Mode |
|--------------|------------|------------------|
| `:set [time]` | Set timer (e.g., `:set 5m30s`) | NORMAL |
| `:start`     | Start countdown | NORMAL |
| `:stop`      | Pause countdown | COUNTDOWN |
| `:reset`     | Reset timer to last set value | NORMAL, COUNTDOWN |
| `:caption`   | Show window title | Any |
| `:nocaption` | Hide window title | Any |
| `:exit`      | Quit app | Any |

---

## **Additional Notes**
- Supports time format: **`h`, `m`, `s`** (e.g., `:set 1h30m20s`).
- Invalid commands trigger a **visual flash** effect.
- Timer color changes dynamically based on remaining time.

---

## **Why?**
This app was created as a **personal experiment** in minimal design and command-based UI, inspired by Vim.  

Even though it's small, I wanted to make something **efficient, clean, and functional** without unnecessary UI clutter. 🚀

