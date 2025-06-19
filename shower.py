import time
import os

def move_cursor(x, y):
    print(f"\033[{y};{x}H", end="")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_shower(frame):
    shower_head = [
        " ",
        " ○ ○ ○ ○ ○ ○ ○ ",
        " ○ ○ ○ ○ ○ ○ ○ ",
        " ○ ○ ○ ○ ○ ○ ○ ",
        " ",
        " "
    ]

    water_cols = [6, 8, 10, 12, 14, 16, 18]

    # Draw the shower head
    for i, line in enumerate(shower_head):
        move_cursor(1, i + 1)
        print(line)

    # Draw the water drops
    for col in water_cols:
        for row in range(15):
            y_pos = 7 + row
            drop_offset = (frame + row + col) % 4
            move_cursor(col, y_pos)
            if drop_offset == 0:
                print("💧", end="")
            else:
                print(" ", end="")

    # Move cursor below the drawing
    move_cursor(1, 25)

def main():
    frame = 0
    clear_screen()
    try:
        while True:
            clear_screen()
            draw_shower(frame)
            frame += 1
            time.sleep(0.1)
    except KeyboardInterrupt:
        clear_screen()

if __name__ == "__main__":
    main()