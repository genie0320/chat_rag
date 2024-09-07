# 매번 헤더를 ' '수정하는 것이 귀찮아서 만든 함수.
# 브러우저의 헤더를 복사해서 data에 그대로 붙여넣기 한 다음 실행하면 됨.

data = """
여기 붙여넣기
"""


def header_converter(input_str):
    # Split the input into lines
    lines = input_str.splitlines()

    # Prepare a list to store the merged lines
    merged_lines = []

    # Iterate over the lines and merge them when needed
    i = 0
    while i < len(lines):
        # If a line ends with a colon, merge it with the next line
        if lines[i].strip().endswith(":"):
            key = lines[i].strip()[:-1]  # Remove the colon from the key
            value = lines[i + 1].strip()

            # Check if value is boolean or integer, otherwise wrap in single quotes
            # if value == "True":
            #     value = True
            # elif value == "False":
            #     value = False
            # elif value.isdigit():
            #     value = int(value)
            # else:
            #     value = f"'{value}'"
            value = f"'{value}'"

            # Wrap the key in single quotes
            key = f"'{key}'"

            merged_lines.append(f"{key}: {value},")
            i += 2  # Skip the next line since it's merged
        else:
            merged_lines.append(lines[i].strip())
            i += 1

    # Return the merged lines as a single string
    return "\n".join(merged_lines)


# Call the function and print the result
output_str = header_converter(data)
print(output_str)
