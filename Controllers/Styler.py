class Styler:

    def song_on_mouse_over(elem, event):
        elem.setStyleSheet("margin-left: 4px; border: none; color: #0000FF")

    def song_on_mouse_leave(elem, event):
        elem.setStyleSheet("margin-left: 4px; border: none; color: #000000")

    def loop_on_mouse_over(elem, repeat, event):
        if not repeat:
            elem.setStyleSheet("border: none; color: #0000FF")

    def loop_on_mouse_leave(elem, repeat, event):
        if not repeat:
            elem.setStyleSheet("border: none; color: #000000")
