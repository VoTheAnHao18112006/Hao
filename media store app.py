import tkinter as tk
from tkinter import messagebox
import sqlite3

#tạo bảng Media (chứa sách, phim, nhạc)
def create_table():
    with sqlite3.connect("library.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS Media (
                MediaId INTEGER PRIMARY KEY AUTOINCREMENT,
                Title TEXT NOT NULL,
                Author TEXT NOT NULL,
                Category TEXT NOT NULL, -- Sách, Phim, Nhạc
                Genre TEXT NOT NULL,
                CreateAt DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

#thêm mục mới
def add_media():
    title = entry_title.get()
    author = entry_author.get()
    genre = entry_genre.get()
    category = selected_category.get()

    if title and author and genre:
        with sqlite3.connect("library.db") as conn:
            conn.execute("INSERT INTO Media (Title, Author, Category, Genre) VALUES (?, ?, ?, ?)",
                         (title, author, category, genre))
        messagebox.showinfo("✅ Thành công", f"Đã thêm {category.lower()} vào thư viện!")
        show_media()
        entry_title.delete(0, tk.END)
        entry_author.delete(0, tk.END)
        entry_genre.delete(0, tk.END)
    else:
        messagebox.showwarning("⚠️ Thiếu thông tin", "Vui lòng điền đầy đủ các trường!")

#hiển thị danh sách
def show_media():
    listbox.delete(0, tk.END)
    with sqlite3.connect("library.db") as conn:
        cursor = conn.execute("SELECT * FROM Media")
        for row in cursor:
            info = f"ID:{row[0]} | {row[1]} - {row[2]} [{row[3]} / {row[4]}]"
            listbox.insert(tk.END, info)

#xóa mục được chọn
def delete_selected():
    selected = listbox.curselection()
    if selected:
        item = listbox.get(selected[0])
        media_id = int(item.split('|')[0].replace("ID:", "").strip())

        confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa mục này?")
        if confirm:
            with sqlite3.connect("library.db") as conn:
                conn.execute("DELETE FROM Media WHERE MediaId = ?", (media_id,))
            messagebox.showinfo("🗑 Đã xóa", "Mục đã được xóa khỏi thư viện.")
            show_media()
    else:
        messagebox.showwarning("Chưa chọn mục", "Vui lòng chọn mục muốn xóa.")

#thống kê số lượng theo loại
def show_stats():
    with sqlite3.connect("library.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT Category, COUNT(*) FROM Media GROUP BY Category")
        results = cursor.fetchall()

    if results:
        stat_text = "Thống kê số lượng:\n"
        for category, count in results:
            stat_text += f"• {category}: {count} mục\n"
        messagebox.showinfo("Thống kê", stat_text)
    else:
        messagebox.showinfo("Thống kê", "Không có dữ liệu để thống kê.")

create_table()
root = tk.Tk()
root.title("🎶 Quản Lý Thư Viện Đa Phương Tiện")
root.geometry("600x550")

#loại dữ liệu
selected_category = tk.StringVar()
selected_category.set("Sách")  # mặc định
tk.Label(root, text="Chọn loại:").pack()
tk.OptionMenu(root, selected_category, "Sách", "Phim", "Nhạc").pack()

#nhập dữ liệu
tk.Label(root, text="Tên (tiêu đề):").pack()
entry_title = tk.Entry(root, width=50)
entry_title.pack()

tk.Label(root, text="Tác giả / Đạo diễn / Ca sĩ:").pack()
entry_author = tk.Entry(root, width=50)
entry_author.pack()

tk.Label(root, text="Thể loại:").pack()
entry_genre = tk.Entry(root, width=50)
entry_genre.pack()

tk.Button(root, text="➕ Thêm", command=add_media, bg="#4CAF50", fg="white").pack(pady=8)
tk.Button(root, text="🗑 Xóa", command=delete_selected, bg="#f44336", fg="white").pack(pady=4)
tk.Button(root, text="📊 Thống kê", command=show_stats, bg="#2196F3", fg="white").pack(pady=4)

#hiển thị danh sách
listbox = tk.Listbox(root, width=85, height=15)
listbox.pack(pady=10)

show_media()
root.mainloop()

