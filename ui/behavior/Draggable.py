class Draggable():
    def __init__(self, widget, my_frame, x=0, y=0, update_canvas_callback=None):
        self.start_x = 0
        self.start_y = 0
        self.update_canvas_callback = update_canvas_callback
        
        widget.place(x=x, y=y)
        widget.bind("<ButtonPress-1>", self.drag_start)
        widget.bind("<B1-Motion>", lambda event: self.drag(my_frame, event))

    def drag_start(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def drag(self, my_frame, event):
        delta_x = event.x - self.start_x
        delta_y = event.y - self.start_y

        # move the widget to the new position
        x = event.widget.winfo_x() + delta_x
        y = event.widget.winfo_y() + delta_y

        event.widget.place(x=x, y=y)

        # Update canvas in my_frame
        self.update_canvas_callback()