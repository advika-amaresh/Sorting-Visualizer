import tkinter as tk
import random

# tried using a list class first but this is cleaner tbh
class SortingVisualizer:
    def __init__(self, root):
        self.root=root
        self.root.title("Sorting methods visualizer")
        self.root.geometry("900x500")
        self.arr=[random.randint(10, 400) for _ in range(50)]
        self.algo=None
        self.running=False

        # bubble sort state
        self.i=0
        self.j=0

        # selection sort state
        self.si=0
        self.sj=1
        self.min_idx=0

        self.canvas=tk.Canvas(root,width=800,height=400,bg="black")
        self.canvas.pack(pady=20)

        ctrl=tk.Frame(root)
        ctrl.pack()
        tk.Button(ctrl,text="Generate",command=self.generate_arr).grid(row=0,column=0,padx=4)
        tk.Button(ctrl,text="Bubble Sort",command=self.run_bubble).grid(row=0,column=1,padx=4)
        tk.Button(ctrl,text="Selection Sort",command=self.run_selection).grid(row=0,column=2,padx=4)
        self.redraw()

    def redraw(self, colors=None):
        self.canvas.delete("all")
        n=len(self.arr)
        bar_w=800/n
        if colors is None:
            colors=["white"]*n
        for idx, h in enumerate(self.arr):
            x0=idx*bar_w
            x1=x0+bar_w
            self.canvas.create_rectangle(x0,400-h,x1,400,fill=colors[idx])

    def generate_arr(self):
        if self.running:
            return  # dont regen mid-sort, causes weird state
        self.arr=[random.randint(10, 400) for _ in range(50)]
        self.redraw()

    # bubble sort part
    def run_bubble(self):
        if self.running:
            return
        self.running=True
        self.algo="bubble"
        self.i=0
        self.j=0
        self._bubble_tick()

    def _bubble_tick(self):
        n=len(self.arr)
        if self.i>=n:
            self.redraw(["green"]*n)
            self.running=False
            return

        if self.j<n-self.i-1:
            cols=["white"]*n
            cols[self.j]="red"
            cols[self.j + 1]="yellow"
            if self.arr[self.j]>self.arr[self.j+1]:
                self.arr[self.j],self.arr[self.j+1]=self.arr[self.j+1],self.arr[self.j]
            self.redraw(cols)
            self.j+=1
        else:
            self.j=0
            self.i+=1

        self.root.after(20,self._bubble_tick)

    # selection sortt part
    def run_selection(self):
        if self.running:
            return
        self.running=True
        self.si=0
        self.sj=1
        self.min_idx=0
        self._selection_tick()

    def _selection_tick(self):
        n=len(self.arr)
        if self.si>=n-1:
            self.redraw(["green"]*n)
            self.running=False
            return

        if self.sj<n:
            cols=["white"]*n
            cols[self.si]="red"
            cols[self.sj]="yellow"
            cols[self.min_idx]="green"
            if self.arr[self.sj]<self.arr[self.min_idx]:
                self.min_idx=self.sj
            self.sj+=1
            self.redraw(cols)
            self.root.after(20, self._selection_tick)
        else:
            # found min for this pass, do the swap
            self.arr[self.si],self.arr[self.min_idx]=self.arr[self.min_idx],self.arr[self.si]
            self.si+=1
            self.min_idx=self.si
            self.sj=self.si+1
            self.root.after(20,self._selection_tick)


if __name__=="__main__":
    root=tk.Tk()
    SortingVisualizer(root)
    root.mainloop()