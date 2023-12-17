import subprocess
import os


def run_script(category, script_name):
    try:
        script_path: str = os.path.join("Scripts/Raphael", category, script_name)
        subprocess.run(args=["python", script_path], check=True)
        print(f"Script {script_name} in {category} executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the script: {e}")
    except FileNotFoundError:
        print(f"Script {script_name} in {category} not found.")


def main():
    while True:
        category: str = input(__prompt="Enter script category or 'exit' to quit: ")
        if category.lower() == "exit":
            break
        script_name: str = input(__prompt="Enter script name to run: ")
        run_script(category=category, script_name=script_name)


if __name__ == "__main__":
    main()
