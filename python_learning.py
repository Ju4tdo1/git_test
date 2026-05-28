# 简单的待办事项管理器
import json
import os

TASKS_FILE = "tasks.json"
tasks = []


def load_tasks():
    global tasks
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r", encoding="utf-8") as f:
                tasks = json.load(f)
        except Exception:
            tasks = []
    else:
        tasks = []


def save_tasks():
    try:
        with open(TASKS_FILE, "w", encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"保存失败：{e}")


def show_menu():
    print("\n--- 待办事项管理器 ---")
    print("1. 查看任务")
    print("2. 添加任务")
    print("3. 标记任务为已完成")
    print("4. 删除任务")
    print("5. 退出")


def view_tasks():
    if not tasks:
        print("当前没有任务。")
    else:
        print("\n你的任务列表：")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task.get("done") else " "
            print(f"{i}.{task.get('title')} {status} ")


def add_task():
    title = input("请输入新任务：")
    tasks.append({"title": title, "done": False})
    save_tasks()
    print(f"已添加任务：{title}")


def mark_task_done():
    view_tasks()
    if tasks:
        try:
            num = int(input("请输入要标记为完成的任务编号："))
            if 1 <= num <= len(tasks):
                tasks[num - 1]["done"] = True
                save_tasks()
                print(f"已标记任务完成：{tasks[num - 1]['title']}")
            else:
                print("无效的编号。")
        except ValueError:
            print("请输入有效数字。")


def delete_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("请输入要删除的任务编号："))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                save_tasks()
                print(f"已删除任务：{removed.get('title')}")
            else:
                print("无效的编号。")
        except ValueError:
            print("请输入有效数字。")


def main():
    load_tasks()
    while True:
        show_menu()
        choice = input("请选择操作（1-5）：")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_task_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("再见！")
            break
        else:
            print("无效选择，请重试。")


if __name__ == "__main__":
    main()
