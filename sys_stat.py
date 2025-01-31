import time
import subprocess

def run_bash_script():
    # Run the bash script and capture the output

    result = subprocess.run(["./sys_stat.sh"],stdout=subprocess.PIPE,text=True)
    return result.stdout

def display_stats():
    # Run the bash script after every 5 seconds and display the results.
    
    while True:
        stats = run_bash_script()

        print("=====System Statistics====")
        print(stats)
        time.sleep(5)


if __name__ == "__main__":
    display_stats()