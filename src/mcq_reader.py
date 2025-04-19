def read_mcqs(file_path):
    """Reads MCQs from the input file and returns them as a list of dictionaries."""
    import re
    mcqs = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        question = None
        options = []
        answer = None

        for line in lines:
            line = line.strip()
            if line.startswith("//") or not line:
                continue  # Skip comments and empty lines
            if line.startswith("Answer:"):
                answer = line.split(":")[1].strip()
                mcqs.append({"question": question, "options": options, "answer": answer})
                question = None
                options = []
            elif re.match(r"^\d+\.", line):
                question = line
            elif line[0] in "ABCD" and line[1] == ".":
                options.append(line)
    return mcqs