#! /usr/bin/env python3

import init
import solution
from tkinter import * 
from tkinter import messagebox, filedialog
from tkinter.ttk import Combobox
from conveyor import Conveyor
from math import factorial
from datetime import datetime
from ttkthemes import ThemedStyle

class Application:
    
    def __init__(self, window):
        self.window = window
        self.l1 = Label(window, text="Оберіть алгоритм")
        self.l2 = Label(window, text="Ініціалізація")

        self.algo_choice = Combobox(window)
        self.algo_choice['values'] = ("Жадібний", "Бджолиний", "Жадібна Бджілка")

        self.init_choice = Combobox(window)
        self.init_choice['values'] = ("Приклад", "Вручну", "Випадкова",
                                      "Файл MS Excel")

        self.start_button = Button(window, text="Почати",
                                   command=self.choice_exec_way)

        self.l1.grid(row=0, column=0)
        self.l2.grid(row=0, column=1)
        self.algo_choice.grid(row=1, column=0)
        self.init_choice.grid(row=1, column=1)
        self.start_button.grid(row=1, column=3)

    def choice_exec_way(self):
        if self.algo_choice.get() != "Жадібний" and self.algo_choice.get() != "Бджолиний" and self.algo_choice.get() != "Жадібна Бджілка":
            self.error_handler("error0")
        else:

            if self.init_choice.get() == "Приклад":
                self.clear_window("start")
                self.Job = init.example()
                self.draw_input_sheet()
            elif self.init_choice.get() == "Вручну":
                self.clear_window("start")
                self.Job = init.keyboard()
                self.draw_input_sheet()
            elif self.init_choice.get() == "Випадкова":
                mess = messagebox.askyesno("rand_init()",
                                       "Использовать конфигурацию по умолчанию?")
                if mess == True:
                    self.clear_window("start")
                    self.Job = init.rand_init(3, 100, 0, 10000)
                    self.Job.info()
                    self.draw_input_sheet()
                else:
                    self.clear_window("start")

                    self.l1.configure(text="Мінімальна кількість деталей")
                    self.l2.configure(text="Максимальна кількість деталей")
                    self.l3 = Label(self.window,
                                    text="Мінімальні час обробки деталі та час перенаголадження верстату")
                    self.l4 = Label(self.window,
                                    text="Максимальні час обробки деталі та час перенаголадження верстату")
                    self.details_min = Spinbox(self.window, from_=3, to=100, 
                                            width=2)
                    self.details_max = Spinbox(self.window, from_=3, to=100,
                                            width=2)
                    self.time_min = Spinbox(self.window, from_=0, to=9999,
                                            width=4)
                    self.time_max = Spinbox(self.window, from_=0, to=9999,
                                            width=4)
                    self.next_button = Button(self.window, text="Далі",
                                            command=self.valid_rand_conf)

                    self.l1.grid(row=0, column=0)
                    self.l2.grid(row=1, column=0)
                    self.l3.grid(row=2, column=0)
                    self.l4.grid(row=3, column=0)
                    self.details_min.grid(row=0, column=1)
                    self.details_max.grid(row=1, column=1)
                    self.time_min.grid(row=2, column=1)
                    self.time_max.grid(row=3, column=1)
                    self.next_button.grid(row=4, column = 1)

            elif self.init_choice.get() == "Файл MS Excel":
                self.clear_window("start")
            
                file = filedialog.askopenfilename(filetypes=(("Файл MS Excel 97-2003",
                                                "*.xls"), 
                                                ("Файл MS Excel 2007-2013",
                                                "*.xlsx"),
                                                ("All files", "*")))

                self.Job = init.excel_file(file)

                if self.Job == "SizeError":
                    self.error_handler("error4")
                    self.choice_exec_way()
                elif self.Job == "ValueError":
                    self.error_handler("error5")
                    self.choice_exec_way()
                else:
                    self.draw_input_sheet()
                    self.Job.info()
            else:
                self.error_handler("error1")

    def error_handler(self, error):
        if error == "error0":
            messagebox.showerror("Error", "Нема такого алгоритму")
        elif error == "error1":
            messagebox.showerror("Error", "Нема такого способа ініціалізації")
        elif error == "error2":
            messagebox.showerror("Error", "Нема такого алгоритму")
        elif error == "error3":
            messagebox.showerror("Error",
                                 "Мінімальна кількість деталей більша за максимальну")
        elif error == "error4":
            messagebox.showerror("Error",
                                 "Мінімальний час більший за максимальний")
        elif error == "error5":
            messagebox.showerror("Error",
                                 "Вектр та матриця у файлі мают різну розмірність")
        elif error == "error6":
            messagebox.showerror("Error",
                                 "В комірці не цілочисельного значення")
        elif error == "error7":
            messagebox.showerror("Error", "На головній діагоналі я не нулі")
        else:
            messagebox.showerror("Error", "Будь ласка вікористовуйте цілі числа")

    
    def valid_rand_conf(self):
        if self.details_min.get() > self.details_max.get():
            self.error_handler("error2")
        elif self.time_min.get() > self.time_max.get():
            self.error_handler("error3")
        else:
            self.Job = init.rand_init(int(self.details_min.get()),
                                 int(self.details_max.get()),
                                 int(self.time_min.get()), 
                                 int(self.time_max.get()))
            self.clear_window("rand")
            self.draw_input_sheet()

    def draw_input_sheet(self):
        self.l1.configure(text="Кількість деталей\n(Після зміни значеня натисніть R)")
        self.l2.configure(text="Час віготовлення деталей")
        self.l3 = Label(self.window, text="Матриця перенаголадження")
        
        details_var = IntVar()
        details_var.set(self.Job.number_of_details)
        self.number_of_details = Spinbox(self.window, from_=3, to=1000, width=4, textvariable=details_var)

        self.present_size = int(self.number_of_details.get())


        self.time_vector = []
        for i in range(int(self.number_of_details.get())):
            if i < len(self.Job.spent_time):
                vector_var = IntVar()
                vector_var.set(self.Job.spent_time[i])
                self.time_vector.append(Spinbox(self.window, from_=0, to=9999, width=4, textvariable=vector_var))
            else:
                vector_var = IntVar()
                vector_var.set(0)
                self.time_vector.append(Spinbox(self.window, from_=0, to=9999, width=4, textvariable=vector_var))

        self.time_matrix = []
        for i in range(int(self.number_of_details.get())):
            vector = []
            for j in range(int(self.number_of_details.get())):
                if i < len(self.Job.reload_time) and j < len(self.Job.reload_time):
                    matrix_var = IntVar()
                    matrix_var.set(self.Job.reload_time[i][j])
                    spin = Spinbox(self.window, from_=0, to=9999, width=4, textvariable=matrix_var)
                    vector.append(spin)
                else:
                    matrix_var = IntVar()
                    matrix_var.set(0)
                    spin = Spinbox(self.window, from_=0, to=9999, width=4, textvariable=matrix_var)
                    vector.append(spin)
            self.time_matrix.append(vector)

        if self.algo_choice.get() != "Жадібний":
            self.l4 = Label(text="Кількість напрямків")
            self.choice_transit = Spinbox(self.window, from_=1, to=factorial(self.Job.number_of_details), width=4)

        self.window.bind("<r>", self.reload_page)
        self.window.bind("<Return>", self.valid_sheet)

        self.l1.grid(row=0, column=0, columnspan=int(self.number_of_details.get()))
        self.l2.grid(row=2, column=0, columnspan=int(self.number_of_details.get()))
        self.number_of_details.grid(row=1, column=0)   
            
        if int(self.number_of_details.get()) <= 50:    
            self.l3.grid(row=4, column=0, columnspan=int(self.number_of_details.get()))
            for i in range(int(self.number_of_details.get())):
                for j in range(int(self.number_of_details.get())):
                    self.time_vector[i].grid(row=3, column=i)
                    self.time_matrix[i][j].grid(row=i+5, column=j)

        if self.algo_choice.get() != "Жадібний":
            self.l4.grid(row=6+self.Job.number_of_details, column=0, columnspan=int(self.number_of_details.get()))
            self.choice_transit.grid(row=7+self.Job.number_of_details, column=0)

                

    def reload_page(self, event):
        self.Job.number_of_details = int(self.number_of_details.get())
        self.l1.grid_forget()
        self.l2.grid_forget()
        self.l3.grid_forget()
        self.number_of_details.grid_forget()
        for i in range(self.present_size):
            for j in range(self.present_size):
                self.time_vector[i].grid_forget()
                self.time_matrix[i][j].grid_forget()
        if self.algo_choice.get() != "Жадібний":
            self.l4.grid_forget()
            self.choice_transit.grid_forget()
        self.draw_input_sheet()

    def valid_sheet(self, event):
        for i in range(len(self.time_matrix)):
            if int(self.time_matrix[i][i].get()) != 0:
                self.error_handler("error7")

        try:
            number_of_details = int(self.number_of_details.get())
            spent_time = [int(self.time_vector[i].get()) for i in range(number_of_details)]
            reload_time = [[int(self.time_matrix[i][j].get()) for j in range(number_of_details)] for i in range(number_of_details)]

            self.Job = Conveyor(number_of_details, spent_time, reload_time)
            if self.algo_choice.get() == "Жадібний":
                start_time = datetime.now()
                S_greedy, zmax_greedy = solution.greedy(self.Job)
                greedy_time = datetime.now() - start_time
                self.output_page(S_greedy, zmax_greedy, None, None, greedy_time, None)
            elif self.algo_choice.get() == "Жадібна Бджілка":
                choice_transit = int(self.choice_transit.get())
                start_time = datetime.now()
                S1, z_max1 = solution.bee(self.Job, choice_transit)
                bee_time = datetime.now() - start_time

                start_time = datetime.now()
                S2, z_max2 = solution.greedy(self.Job)
                greedy_time = datetime.now() - start_time
                self.output_page(S1, z_max1, S2, z_max2, greedy_time, bee_time)
            else:
                choice_transit = int(self.choice_transit.get())
                start_time = datetime.now()
                S_bee, zmax_bee = solution.bee(self.Job, choice_transit)
                bee_time = datetime.now() - start_time
                self.output_page(None, None, S_bee, zmax_bee, None, bee_time)
        except ValueError:
            self.error_handler("error8")

    def output_page(self, S_greedy, zmax_greedy, S_bee, zmax_bee, greedy_time, bee_time):
        self.Job.number_of_details = int(self.number_of_details.get())
        self.l1.grid_forget()
        self.l2.grid_forget()
        self.l3.grid_forget()
        self.number_of_details.grid_forget()
        for i in range(self.present_size):
            for j in range(self.present_size):
                self.time_vector[i].grid_forget()
                self.time_matrix[i][j].grid_forget()

        if self.algo_choice.get() != "Жадібний":
            self.l4.grid_forget()
            self.choice_transit.grid_forget()

        
        if S_bee == None and zmax_bee == None:
            self.l1.configure(text="Найкращий росклад:")
            self.l2.configure(text="Цільова функція:")
            self.l3.configure(text="Час виконання алгоритму:")
            self.S = Label(self.window, text=str(S_greedy))
            self.z_max = Label(self.window, text=str(zmax_greedy))
            self.greedy_time = Label(self.window, text= str(greedy_time))
            self.end_button = Button(self.window, text="Ще")
            self.end_button.bind("<Button-1>", self.restart)

            self.l1.grid(row=0, column=0)
            self.S.grid(row=0, column=1)
            self.l2.grid(row=1, column=0)
            self.z_max.grid(row=1, column=1)
            self.l3.grid(row=2, column=0)
            self.greedy_time.grid(row=2, column=1)
            self.end_button.grid(row=3, column=1)
        elif S_greedy == None and zmax_greedy == None:
            self.l1.configure(text="Найкращий росклад:")
            self.l2.configure(text="Цільова функція:")
            self.S = Label(self.window, text=str(S_bee))
            self.z_max = Label(self.window, text=str(zmax_bee))
            self.l3.configure(text="Час виконання алгоритму:")
            self.bee_time = Label(self.window, text=str(bee_time))
            self.end_button = Button(self.window, text="Ще")
            self.end_button.bind("<Button-1>", self.restart)

            self.l1.grid(row=0, column=0)
            self.S.grid(row=0, column=1)
            self.l2.grid(row=1, column=0)
            self.z_max.grid(row=1, column=1)
            self.l3.grid(row=2, column=0)
            self.bee_time.grid(row=2, column=1)
            self.end_button.grid(row=3, column=1)
        else:
            self.l1.configure(text="Найкращий розклад після жадібного алгоритму:")
            self.l2.configure(text="Цільова функція після жадібного алгоритму:")
            self.l3.configure(text="Найкращий розклад після бджолиного алгоритму:")
            self.l4.configure(text="Цільва функція після бджолиного алгоритму:")
            self.l5 = Label(self.window, text="Час виконання жадібного алгоритму")
            self.l6 = Label(self.window, text="Час виконання бджолиного алгоритму")
            self.S_greedy = Label(self.window, text=str(S_greedy))
            self.S_bee = Label(self.window, text=str(S_bee))
            self.zmax_greedy = Label(self.window, text=str(zmax_greedy))
            self.zmax_bee = Label(self.window, text=str(zmax_bee))
            self.greedy_time = Label(self.window, text=str(greedy_time))
            self.bee_time = Label(self.window, text=str(bee_time))
            self.end_button = Button(self.window, text="Ще")
            self.end_button.bind("<Button-1>", self.restart)

            self.l1.grid(row=0, column=0)
            self.S_greedy.grid(row=0, column=1)
            self.l2.grid(row=1, column=0)
            self.zmax_greedy.grid(row=1, column=1)
            self.l3.grid(row=2, column=0)
            self.S_bee.grid(row=2, column=1)
            self.l4.grid(row=3, column=0)
            self.zmax_bee.grid(row=3, column=1)
            self.l5.grid(row=4, column=0)
            self.greedy_time.grid(row=4, column=1)
            self.l6.grid(row=5, column=0)
            self.bee_time.grid(row=5, column=1)
            self.end_button.grid(row=6, column=1)


    def clear_window(self, ivent):
        if ivent == "start":
            self.l1.grid_forget()
            self.l2.grid_forget()
            self.init_choice.grid_forget()
            self.algo_choice.grid_forget()
            self.start_button.grid_forget()
        elif ivent == "rand":
            self.l1.grid_forget()
            self.l2.grid_forget()
            self.l3.grid_forget()
            self.l4.grid_forget()
            self.details_min.grid_forget()
            self.details_max.grid_forget()
            self.time_min.grid_forget()
            self.time_max.grid_forget()
            self.next_button.grid_forget()

    def restart(self, event):
        if self.algo_choice.get() == "Жадібний":
            self.l1.grid_forget()
            self.S.grid_forget()
            self.l2.grid_forget()
            self.z_max.grid_forget()
            self.l3.grid_forget()
            self.greedy_time.grid_forget()
            self.end_button.grid_forget()
        elif self.algo_choice.get() == "Бджолиний":
            self.l1.grid_forget()
            self.S.grid_forget()
            self.l2.grid_forget()
            self.z_max.grid_forget()
            self.l3.grid_forget()
            self.bee_time.grid_forget()
            self.end_button.grid_forget()
        else:
            self.l1.grid_forget()
            self.S_greedy.grid_forget()
            self.l2.grid_forget()
            self.zmax_greedy.grid_forget()
            self.l3.grid_forget()
            self.S_bee.grid_forget()
            self.l4.grid_forget()
            self.zmax_bee.grid_forget()
            self.l5.grid_forget()
            self.greedy_time.grid_forget()
            self.l6.grid_forget()
            self.bee_time.grid_forget()
            self.end_button.grid_forget()

        self.__init__(self.window)


def main():
    window = Tk()
    window.title("Greedy Bee")
    style = ThemedStyle(window)
    style.set_theme("arc")

    App = Application(window)
    window.mainloop()

if __name__ == "__main__":
    main()