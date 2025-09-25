import subprocess
from pathlib import Path

def run_solution(num: int) -> str:
    task_dir = Path("/app")
    input_file = task_dir / "input.txt"
    output_file = task_dir / "output.txt"

    # Write input
    input_file.write_text(str(num) + "\n")

    # Run solution
    subprocess.run(["/bin/bash", str(task_dir / "solution.sh")], check=True)

    # Read output
    return output_file.read_text()

def test_even_odd():
    test_cases = {
        0: "even",
        1: "odd",
        2: "even",
        7: "odd",
        10: "even",
        9999: "odd",
    }

    for num, expected in test_cases.items():
        assert run_solution(num) == expected
