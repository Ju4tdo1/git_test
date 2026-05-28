# 简单的待办事项管理器
tasks = []
#ddd
def show_menu():
    print("\n--- 待办事项管理器 ---")
    print("1. 查看任务")
    print("2. 添加任务")
    print("3. 删除任务")
    print("4. 退出")

def view_tasks():
    if not tasks:
        print("当前没有任务。")
    else:
        print("\n你的任务列表：")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("请输入新任务：")
    tasks.append(task)
    print(f"已添加任务：{task}")

def delete_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("请输入要删除的任务编号："))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"已删除任务：{removed}")
            else:
                print("无效的编号。")
        except ValueError:
            print("请输入有效数字。")

def main():
    while True:
        show_menu()
        choice = input("请选择操作（1-4）：")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("再见！")
            break
        else:
            print("无效选择，请重试。")

if __name__ == "__main__":
    main()
