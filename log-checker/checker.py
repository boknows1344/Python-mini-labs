keywords = ["error", "failed", "timeout"]

# track counts
counts = {
    "Error": 0,
    "failed": 0,
    "timeout": 0
}

with open("sample_logs.txt", "r") as file:
    for line in file:
        line_lower = line.lower  # make matching consistent

        for word in keywords:
            if word in line_lower:
                counts[word] = counts[word] + 1

print("log summary")
print("-----------")

for word in keywords:
    print(word + ": " + str(counts[word]))

