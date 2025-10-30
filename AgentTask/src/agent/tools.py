import re, io, contextlib

from langchain.tools import tool

@tool
def read_file(filepath: str) -> str:
    """
    Return the contents of a file provided by the filepath.

    :param filepath: Path to the file
    :return: Contents of the file
    """

    with open(filepath,"r") as f:
        content = f.read()

    return content

@tool
def write_file(filepath: str,data: str) -> str:
    """
    Write data to a file provided by the filepath.

    :param filepath: Path to the file
    :param data: Content to write
    :return: Contents of the file
    """

    with open(filepath,"w") as f:
        f.write(data)

    return data

def _clean_code(code: str) -> str:
    cleaned = re.sub(r"```(?:python)?", "", code, flags=re.IGNORECASE)
    cleaned = cleaned.replace("```", "").strip()
    return cleaned

@tool
def clean_code(code: str) -> str:
    """
    Remove Markdown code fences (```python ... ```) from a code block.

    :param code: The python code to clean
    :return:
    """
    return _clean_code(code)

@tool
def test_code(code: str) -> str:
    """
    Safely execute Python code and report whether all tests pass.

    :param code: The python code to execute and test
    :return:
    """
    code = _clean_code(code)
    output = io.StringIO()

    try:
        with contextlib.redirect_stdout(output):
            exec(code)

        print("✅ All tests passed!")
        return f"✅ All tests passed!\n{output.getvalue()}"
    except AssertionError as e:
        print("❌ Test failed. Refining the code...")
        return f"❌ Test failed: {e}\nOutput:\n{output.getvalue()}"
    except Exception as e:
        print("❌ Test failed. Refining the code...")
        return f"💥 Runtime error: {e}\nOutput:\n{output.getvalue()}"
