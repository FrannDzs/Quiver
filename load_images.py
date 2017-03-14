import tkinter as tk

class LoadImages:
    def __init__(self):
        self.icon = tk.PhotoImage(data="iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAeklEQVR42mNgGLRAx9j0Pwijiz948OA/UZqxsUGajx079p+gIdgMCFEX+28qwfefoCHozgZphGlGNsTe3p6wASANx2JMwRjdEILOR9aMbghB/2PTPM9T67+tjADhGBg4zSBFIMVkaUY2AGYISZrRDSBZM7IhMEy3TAcADJKjp8RcMjQAAAAASUVORK5CYII=")

        self.image_folder_close = tk.PhotoImage(data="iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAALGPC/xhBQAAAAlwSFlzAAAOwQAADsEBuJFr7QAAABl0RVh0U29mdHdhcmUAcGFpbnQubmV0IDQuMC4xMzQDW3oAAABNSURBVDhP7YzbCQAgDAO7/2zdqYov1MZi8NfAKVxDxMyegJIBSgYoGeqTv51RCG7l3kuqujCVlxwHECjN+4Hb/IFggMENvAAlA5T3mCSy2+PSrwjh8wAAAABJRU5ErkJggg==")
        self.image_folder_open = tk.PhotoImage(data="iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAALGPC/xhBQAAAAlwSFlzAAAOwgAADsIBFShKgAAAABh0RVh0U29mdHdhcmUAcGFpbnQubmV0IDQuMC45bDN+TgAAAGtJREFUOE+ljgEOwCAIA/3/2/gTU5hJNR2hGcmBVlsd7v4LKipQUYGKCtnmuMFLFdnmMLODbkg2ErBDGO0AhhSw9AoagBcWX/WeRZ/rDKgMWNscy9zXr2GhObapnd+uQHN4b0GFigpU7OPjARHQwCni2pyrAAAAAElFTkSuQmCC")
        self.image_painting = tk.PhotoImage(data="iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAALGPC/xhBQAAAAlwSFlzAAAOwgAADsIBFShKgAAAABl0RVh0U29mdHdhcmUAcGFpbnQubmV0IDQuMC4xMzQDW3oAAABlSURBVDhPxZBBDsAgCAT9/9v4E3UPGJBtrXhwkzEKOIk2VT2CFo0eLH3L+4AXp4vz2RMPH4OA9UPT9iv87ChUCAIRCaxCBTtJgt3cFeC5ScD+wD6UQQXA4ocZr4K/JEGFIaij7QGG7derbF7cRwAAAABJRU5ErkJggg==")
        self.image_paper_text = tk.PhotoImage(data="iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAYdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuOWwzfk4AAAB1SURBVDhPtYwBCsAwCAP7/0+7xaqYIs4xJhwxNc0SkU+wuW1Fzpyw2WGapxI2VpA+naq5DBsL58lvVQkbC0PPPYNnJxY1+9jOqABa4TeIE4saC3UzKoBW+A3ixKLGQt2MCqAVfoM4saixUDf/F0ygP9m8R9YFZ1GwbMr1dgIAAAAASUVORK5CYII=")
        self.image_paper_json = tk.PhotoImage(data="iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAALGPC/xhBQAAAAlwSFlzAAAOwQAADsEBuJFr7QAAABl0RVh0U29mdHdhcmUAcGFpbnQubmV0IDQuMC4xMzQDW3oAAABxSURBVDhPzYxRDoAwCEN3/0vj6IK2hAWNftikGW+UDjN7ZYWJlTmTrbDCoq5EgQpiTi9ybIV05CpmZMMKm4Js/w6fA2AtIyRKO+SBAhOr4xDtrxuBLwpcVUnaIQ8U+E2Bq5mRBwpQcKe24I7lhuG5bRz2S79dRRFJSgAAAABJRU5ErkJggg==")
        self.image_paper_binary = tk.PhotoImage(data="iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAALGPC/xhBQAAAAlwSFlzAAAOwQAADsEBuJFr7QAAABl0RVh0U29mdHdhcmUAcGFpbnQubmV0IDQuMC4xMzQDW3oAAACCSURBVDhPpYwLDoRADEK9/6VHwTIpzfyMJGx5K8PVWvtlhwdHzp1qh7ds2o04pAHlctnLdlgMQKMRh8lANf6WeyC8H5c6GsCVxVJk9okG5UG9UGT80D0Q0gNZLEVmn2iQijMdDyjjymIcuQdClKD8QBbjyD0QorTSduDE9ibDd7frBh80sGwTGiRKAAAAAElFTkSuQmCC")
        self.image_paper_language = tk.PhotoImage(data="iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAALGPC/xhBQAAAAlwSFlzAAAOwQAADsEBuJFr7QAAABl0RVh0U29mdHdhcmUAcGFpbnQubmV0IDQuMC4xMzQDW3oAAACCSURBVDhPpYyJDcAwCAOz/9JpeUwwSvOoSBY+MLTe+y8xvDhTzlQxWJhq94TBH+AIwkxaFQOHtcNLudcsxFAOvyQRKIyCLZd19KA+Es6SERRGwZY1HF3KveYVCdIBVNln44bAlsu6egCWnr00KIxCOZixz8YNgS2XtX1wIrrJcK/eHju+lYdncJJwAAAAAElFTkSuQmCC")
        self.image_cube = tk.PhotoImage(data="iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAZdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuMTM0A1t6AAAAhElEQVQ4T6WMgQ3AIAgE3X8Dd3InKrSvgJRqSvKNfLkrRPQrYcnpw58R/x9ZiwmYeRPZJQD9eMl8bMAYLTmGMZAMwYlE3U9Ba21Lwje11ljwJQGcCiB5DmSwA14E942VaJEGNWwEsgSSDBZGL1I4SQbLvS+k7DVEACOYsxQ6GYiE5X6oXBY64NXWXzXnAAAAAElFTkSuQmCC")
        self.image_fragment = tk.PhotoImage(data="iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAZdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuMTM0A1t6AAAAjUlEQVQ4T6WRAQ6AIAwD+f8P+BN/mhRWrDJR4pLLsF0nxmRmvwhFUqu22COhCDyMQ2tPxKKHSyn7CzSM2lqwGwbnwcM559ZXYfVUGOHVt0NXf4gMo9OMcG9egPoa1rlh8AY0FGiuT3NjoD91UYHGv8JweAMKCjSG70s4fwkoGtY3s78uABha0WY0sI+lA38iui/by1gmAAAAAElFTkSuQmCC")
        self.image_vertex = tk.PhotoImage(data="iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAZdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuMTM0A1t6AAAAcElEQVQ4T6WMgQ3AIAgE3X8DdmInCqS0qK+RaHKiB3wTkSugrABloMcufeK+AaXxLvrZhWCpegxYhcwiDcebiLyGz/SfNGRLY0Uh/yM1mdlrLOf/GLJc3tU8/wVE87R2ATdAWQHKClBWgLIClOdIewBnAc1P/9ZTAAAAAABJRU5ErkJggg==")
        self.image_nbt = tk.PhotoImage(data="iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAZdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuMTM0A1t6AAAAn0lEQVQ4T6WQgQ3EIAwDu/8G7MROlBicGnBf//pIbpOLHVW9Wmt/yUKqVzx66/chC0MziPp0xEMJs96OHACwYz0i8+ILHQCw41prBksp2R/eHQBOcxxhmLUfyWaBMxxvDbP0SIZUDLojMg8vmwTG7P5HrGFhg2EslmJQ/8f0jQwbDM8SxfmnL3Bm8j2MjA4Am5kB7VXLkPDF7GTh92rXDT6fn+OjXcFtAAAAAElFTkSuQmCC")

        self.image_exit = tk.PhotoImage(data="iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAYdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuOWwzfk4AAAB2SURBVDhPpUwJDoAwCNv/P40C6UQoGDOSbvRiicgR/Lk/IJoMObtFDAwGliuGDsyILvMZ8HXwsBghwalsNBITUiFOLpuUBRPJEVZWFMHEkwOsjGFH3iSVlTNNP+BZhuDoOe8DQJcpJgwGltsGoHxCzpbAP8i6ANcb1Uc6RuL/AAAAAElFTkSuQmCC")

        self.image_refresh = tk.PhotoImage(data="iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAZdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuMTJDBGvsAAAAfklEQVQ4T6VMCQ7AIAjz/59mglY6B45lTapAjyYiv+hDHyuEf+XscfGIqGQVVFEq0J3JmLvlbB03N1HI7rQbtpu9fb4b9Buj33fA9zBCAFkD2PMwsQie9FcDqPdIWyKQGTOOhwoUKMmoFjAsOCEtqJaEBTbMkgqRsRwv3yntAi21r22c8JTGAAAAAElFTkSuQmCC")

        self.image_find = tk.PhotoImage(data="iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAZdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuMTJDBGvsAAAAW0lEQVQ4T+2MWxJAEQxD7X/TvV4lrqD4ZeaMJG3jROQKGu7QGm//4JxRRVru3qqkileQjLcjcA+hIZKPhyVdwJiVNGYGlmBRWbCAJeGLUoWFcKiUTMUpNLQj7gMnkNZG4QMzqgAAAABJRU5ErkJggg==")
