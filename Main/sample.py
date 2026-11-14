import tkinter as tk
from types import SimpleNamespace

    
def main():
    screen = SimpleNamespace()
    
    def T(x, y):
        ''' convert app coords to canvas coords
            app coords 0 to 1 '''
        x = (screen.width/1.02)*x + screen.width*(1 - 1.01/1.02)
        y = (screen.height/1.02)*y + screen.height*(1 - 1.01/1.02)
        return x, y

    def canvas_size(event):
        '''
        compute canvas max coords
        '''
        screen.width = event.width
        screen.height = event.height

    def createMarker(canvas, cx, cy):
        '''
        draw a small red circle
        '''
        r = 2
        cx, cy = T(cx, cy)
        canvas.create_oval(
            cx-r, cy-r,
            cx+r, cy+r,
            outline="red",
            fill="red",
            width=2
        )

    root = tk.Tk()
    root.attributes('-fullscreen', True)

    canvas = tk.Canvas(root)
    canvas.pack(padx=100, pady=100, fill=tk.BOTH, expand=True)
 
    # call canvas_size() after screen is rendered
    canvas.bind("<Configure>", canvas_size)

    # example calls
    def draw():
        createMarker(canvas, 0, 0)
        createMarker(canvas, 0.5, 0.5)
        createMarker(canvas, 1, 1)
        canvas.create_line(*T(0, 0), *T(0.5, 0.5))
    root.after(100, draw)

    root.bind("<Escape>", lambda e: root.destroy())
    root.mainloop()

main()