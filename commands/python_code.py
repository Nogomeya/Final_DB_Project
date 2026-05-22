# من سطر 12 : 15 عباره عن بينات خاصه بجهازي ..لا تنسي تغييرها للبيانات الخاصه بك
import os
import customtkinter as ctk
from PIL import Image
import mysql.connector
from tkinter import messagebox

# 1. إعداد المظهر العام
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# 2. بيانات الاتصال بالـ MySQL
DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASSWORD = "My_mysql_password_here"  
DB_NAME = "Bank"

# ألوان هوية بنك القاهرة
PRIMARY_RED = "#8B1D1A"
HOVER_RED = "#5E110F"
ACCENT_ORANGE = "#D9661F"
TEXT_DARK = "#333333"
BG_LIGHT = "#F9F9F9"

class BankApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("سيستم بنك مصر الإلكتروني - لوحة التحكم")
        self.geometry("1050x700")
        self.resizable(False, False)
        self.configure(fg_color=BG_LIGHT)

        self.current_path = os.path.dirname(os.path.realpath(__file__))

        self.login_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.dashboard_frame = ctk.CTkFrame(self, fg_color="transparent")

        self.show_login_screen()

    # ==================== 🏛️ شاشة تسجيل الدخول ====================
    def show_login_screen(self):
        self.dashboard_frame.pack_forget()
        self.login_frame.pack(fill="both", expand=True)

        try:
            logo_image = ctk.CTkImage(light_image=Image.open(os.path.join(self.current_path, "logo.png")), size=(180, 180))
            logo_label = ctk.CTkLabel(self.login_frame, image=logo_image, text="")
            logo_label.pack(pady=(20, 10))
        except:
            logo_label = ctk.CTkLabel(self.login_frame, text="🏛️ BANK SYSTEM", font=("Helvetica", 32, "bold"), text_color=PRIMARY_RED)
            logo_label.pack(pady=(40, 10))

        self.welcome_label = ctk.CTkLabel(self.login_frame, text="🏛️ نظام الإدارة المصرفية الذكي\nمن تطوير الباشمهندس عبد الرحمن نجم", font=("Cairo", 24, "bold"), text_color=PRIMARY_RED)
        self.welcome_label.pack(pady=5)

        self.sub_label = ctk.CTkLabel(self.login_frame, text="أهلاً بسيادة الدكتورة الفاضلة \"هيام\" في واجهة التقييم النهائي 🌟\n(برجاء تسجيل الدخول لتجربة الأنظمة والربط الحي)", font=("Cairo", 15, "bold"), text_color=ACCENT_ORANGE)
        self.sub_label.pack(pady=(5, 20))

        input_card = ctk.CTkFrame(self.login_frame, fg_color="#FFFFFF", corner_radius=15, width=400, height=190)
        input_card.pack_propagate(False)
        input_card.pack(pady=5)

        self.username_input = ctk.CTkEntry(input_card, placeholder_text="رقم الموظف (Employee ID)", width=300, height=40, corner_radius=8, justify="center")
        self.username_input.pack(pady=(25, 15))

        self.password_input = ctk.CTkEntry(input_card, placeholder_text="الرقم القومي (Employee SSN)", show="*", width=300, height=40, corner_radius=8, justify="center")
        self.password_input.pack(pady=(0, 20))

        self.login_btn = ctk.CTkButton(self.login_frame, text="تسجيل الدخول آمن", font=("Cairo", 15, "bold"), fg_color=PRIMARY_RED, hover_color=HOVER_RED, width=220, height=45, corner_radius=25, command=self.login_action)
        self.login_btn.pack(pady=20)

        self.footer_label = ctk.CTkLabel(self.login_frame, text="المشروع مقدم لتقييم مادة قواعد البيانات ©️ 2026", font=("Cairo", 11), text_color="#A0AEC0")
        self.footer_label.pack(side="bottom", pady=10)

    def login_action(self):
        user_id = self.username_input.get()
        user_ssn = self.password_input.get()

        if not user_id or not user_ssn:
            messagebox.showwarning("تنبيه", "الرجاء إدخال رقم الموظف والرقم القومي!")
            return

        try:
            conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
            cursor = conn.cursor()
            cursor.execute("SELECT first_name, last_name FROM employee WHERE employee_id = %s AND employee_ssn = %s", (user_id, user_ssn))
            result = cursor.fetchone()

            if result:
                emp_name = f"{result[0]} {result[1]}"
                # تفريغ خانات الدخول عشان لو عمل تسجيل خروج يلاقيهم نضاف
                self.username_input.delete(0, 'end')
                self.password_input.delete(0, 'end')
                messagebox.showinfo("نجاح الدخول 🎯", f"مرحباً بك يا باشمهندس {emp_name}\nتم التحقق حياً من الـ MySQL بنجاح!")
                cursor.close()
                conn.close()
                self.show_dashboard_screen(emp_name)
            else:
                messagebox.showerror("خطأ في الدخول ❌", "عذراً، بيانات هذا الموظف غير مسجلة!")
                cursor.close()
                conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("فشل الاتصال", f"لم نتمكن من الوصول لقاعدة البيانات:\n{err}")

    # ==================== 🚀 3. شاشة لوحة التحكم ====================
    def show_dashboard_screen(self, emp_name):
        self.login_frame.pack_forget()
        self.dashboard_frame.pack(fill="both", expand=True)

        top_bar = ctk.CTkFrame(self.dashboard_frame, fg_color=PRIMARY_RED, height=70, corner_radius=0)
        top_bar.pack(fill="x", side="top")

        title_label = ctk.CTkLabel(top_bar, text="لوحة التحكم المصرفية الشاملة", font=("Cairo", 18, "bold"), text_color="#FFFFFF")
        title_label.pack(side="right", padx=20, pady=15)

        user_label = ctk.CTkLabel(top_bar, text=f"👤 الموظف: {emp_name}", font=("Cairo", 13, "bold"), text_color="#FBD38D")
        user_label.pack(side="left", padx=20, pady=15)

        main_content = ctk.CTkFrame(self.dashboard_frame, fg_color="transparent")
        main_content.pack(fill="both", expand=True, padx=15, pady=15)

        # --- الجانب الأيمن: استمارات إدخال البيانات ---
        form_frame = ctk.CTkFrame(main_content, fg_color="#FFFFFF", corner_radius=12, width=380)
        form_frame.pack(fill="y", side="right", padx=(10, 0))
        form_frame.pack_propagate(False)

        form_title = ctk.CTkLabel(form_frame, text="إدارة بيانات العملاء", font=("Cairo", 17, "bold"), text_color=PRIMARY_RED)
        form_title.pack(pady=15)

        self.cust_ssn = ctk.CTkEntry(form_frame, placeholder_text="الرقم القومي (SSN)", width=320, height=38, justify="center")
        self.cust_ssn.pack(pady=8)
        self.cust_first_name = ctk.CTkEntry(form_frame, placeholder_text="الاسم الأول", width=320, height=38, justify="center")
        self.cust_first_name.pack(pady=8)
        self.cust_last_name = ctk.CTkEntry(form_frame, placeholder_text="الاسم الأخير", width=320, height=38, justify="center")
        self.cust_last_name.pack(pady=8)
        self.cust_funds = ctk.CTkEntry(form_frame, placeholder_text="الرصيد ($)", width=320, height=38, justify="center")
        self.cust_funds.pack(pady=8)

        # 🌟 تنظيم جديد للأزرار لراحة العين (جنب بعض)
        buttons_row = ctk.CTkFrame(form_frame, fg_color="transparent")
        buttons_row.pack(pady=(15, 8))

        btn_insert = ctk.CTkButton(buttons_row, text="📥 إضافة", font=("Cairo", 13, "bold"), fg_color="#2F855A", hover_color="#22543D", width=155, height=40, command=self.db_insert_customer)
        btn_insert.pack(side="right", padx=5)

        btn_update = ctk.CTkButton(buttons_row, text="✏️ تعديل الرصيد", font=("Cairo", 13, "bold"), fg_color=ACCENT_ORANGE, hover_color="#B75317", width=155, height=40, command=self.db_update_customer)
        btn_update.pack(side="left", padx=5)

        btn_delete = ctk.CTkButton(form_frame, text="🗑️ حذف نهائي للعميل", font=("Cairo", 13, "bold"), fg_color="#E53E3E", hover_color="#9B2C2C", width=320, height=40, command=self.db_delete_customer)
        btn_delete.pack(pady=8)

        btn_logout = ctk.CTkButton(form_frame, text="🚪 تسجيل الخروج", font=("Cairo", 12, "bold"), fg_color="#718096", hover_color="#4A5568", width=150, command=self.show_login_screen)
        btn_logout.pack(side="bottom", pady=15)

        # --- الجانب الأيسر: شاشة العرض ---
        display_frame = ctk.CTkFrame(main_content, fg_color="#FFFFFF", corner_radius=12)
        display_frame.pack(fill="both", expand=True, side="left")

        self.status_label = ctk.CTkLabel(display_frame, text="تم الاتصال بقاعدة البيانات جاهز للعمل", font=("Cairo", 13, "bold"), text_color=TEXT_DARK)
        self.status_label.pack(pady=15)

        self.data_display = ctk.CTkTextbox(display_frame, font=("Courier New", 14), fg_color="#FFF5F5", text_color=TEXT_DARK, corner_radius=10, border_color=PRIMARY_RED, border_width=1)
        self.data_display.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        self.fetch_customers_from_db()

    # ==================== 🛠️ دوال مساعدة لراحة التفاعل (UX) ====================
    def clear_inputs(self):
        """دالة سحرية لتفريغ الخانات بعد كل عملية ووضع المؤشر في أول خانة"""
        self.cust_ssn.delete(0, 'end')
        self.cust_first_name.delete(0, 'end')
        self.cust_last_name.delete(0, 'end')
        self.cust_funds.delete(0, 'end')
        self.cust_ssn.focus() # يرجع المؤشر لخانة الـ SSN تلقائياً

    # ==================== 🛠️ دوال تنفيذ العمليات في الـ MySQL ====================
    def fetch_customers_from_db(self):
        try:
            conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
            cursor = conn.cursor()
            cursor.execute("SELECT customer_ssn, first_name, last_name, funds FROM customer")
            rows = cursor.fetchall()

            self.data_display.delete("1.0", "end")
            header = f"{'SSN':<15} | {'First Name':<15} | {'Last Name':<15} | {'Funds ($)':<12}\n"
            separator = "=" * 65 + "\n"
            self.data_display.insert("end", header + separator)

            for row in rows:
                row_str = f"{row[0]:<15} | {row[1]:<15} | {row[2]:<15} | {row[3]:<12,.2f}\n"
                self.data_display.insert("end", row_str)

            self.status_label.configure(text="آخر تحديث للبيانات تم بنجاح! ✅", text_color="#2F855A")
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("خطأ", f"فشل جلب البيانات: {err}")

    def db_insert_customer(self):
        ssn, fn, ln, funds = self.cust_ssn.get(), self.cust_first_name.get(), self.cust_last_name.get(), self.cust_funds.get()
        if not ssn or not fn or not ln or not funds:
            messagebox.showwarning("تنبيه", "برجاء ملء جميع الخانات لإضافة العميل!")
            return
        try:
            conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO customer (customer_ssn, first_name, last_name, funds) VALUES (%s, %s, %s, %s)", (ssn, fn, ln, float(funds)))
            conn.commit()
            messagebox.showinfo("نجاح", f"تم إضافة العميل {fn} بنجاح!")
            cursor.close()
            conn.close()
            self.fetch_customers_from_db()
            self.clear_inputs()  # 🌟 تفريغ الخانات فوراً
        except Exception as err:
            messagebox.showerror("خطأ", f"فشلت الإضافة:\n{err}")

    def db_update_customer(self):
        ssn, funds = self.cust_ssn.get(), self.cust_funds.get()
        if not ssn or not funds:
            messagebox.showwarning("تنبيه", "لتعديل الرصيد، اكتب الـ SSN والرصيد الجديد فقط!")
            return
        try:
            conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
            cursor = conn.cursor()
            cursor.execute("UPDATE customer SET funds = %s WHERE customer_ssn = %s", (float(funds), ssn))
            conn.commit()
            messagebox.showinfo("نجاح", "تم تحديث الرصيد بنجاح!")
            cursor.close()
            conn.close()
            self.fetch_customers_from_db()
            self.clear_inputs()  # 🌟 تفريغ الخانات
        except Exception as err:
            messagebox.showerror("خطأ", f"فشل التعديل:\n{err}")

    def db_delete_customer(self):
        ssn = self.cust_ssn.get()
        if not ssn:
            messagebox.showwarning("تنبيه", "برجاء كتابة (SSN) للعميل المراد حذفه!")
            return
        if not messagebox.askyesno("تأكيد", "هل أنت متأكد من حذف العميل؟"):
            return
        try:
            conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM customer WHERE customer_ssn = %s", (ssn,))
            conn.commit()
            messagebox.showinfo("نجاح", "تم الحذف نهائياً!")
            cursor.close()
            conn.close()
            self.fetch_customers_from_db()
            self.clear_inputs()  # 🌟 تفريغ الخانات
        except Exception as err:
            messagebox.showerror("خطأ", f"فشل الحذف:\n{err}")

if __name__ == "__main__":
    app = BankApp()
    app.mainloop()
