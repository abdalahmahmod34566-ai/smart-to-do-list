tasks = []


def show_menu():
    print("\nاختر من القائمة:")
    print("١. إضافة مهمة")
    print("٢. عرض المهام")
    print("٣. حذف مهمة")
    print("٤. خروج")


def add_task():
    task = input("اكتب المهمة الجديدة: ").strip()

    if task:
        tasks.append(task)
        print("تمت إضافة المهمة بنجاح.")
    else:
        print("لا يمكن إضافة مهمة فارغة.")


def show_tasks():
    if not tasks:
        print("لا توجد مهام حاليًا.")
        return

    print("\nالمهام الحالية:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def delete_task():
    if not tasks:
        print("لا توجد مهام لحذفها.")
        return

    show_tasks()
    task_number = input("اكتب رقم المهمة التي تريد حذفها: ").strip()

    try:
        task_index = int(task_number) - 1
        deleted_task = tasks.pop(task_index)
        print(f"تم حذف المهمة: {deleted_task}")
    except (ValueError, IndexError):
        print("رقم المهمة غير صحيح.")


def main():
    print("مرحبًا بك في Smart To-Do List!")

    while True:
        show_menu()
        choice = input("اكتب رقم الاختيار: ").strip()

        if choice in ("1", "١"):
            add_task()
        elif choice in ("2", "٢"):
            show_tasks()
        elif choice in ("3", "٣"):
            delete_task()
        elif choice in ("4", "٤"):
            print("شكرًا لاستخدام Smart To-Do List. إلى اللقاء!")
            break
        else:
            print("اختيار غير صحيح، حاول مرة أخرى.")


if __name__ == "__main__":
    main()