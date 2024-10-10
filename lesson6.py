file_system = [
    [
        "nothing.txt",
        "dog_pic.png",
        [
            "secret_plan.pdf"
        ]
    ],
    "notion.app",
    "slack.app",
    [
        "fun.txt",
        [
            "meaningless_file.txt",
            "chicken_dinner.txt"
        ],
        "not_fun.txt"
    ],
    "zoom.app"
]

target = "chicken_dinner.txt"




def file_search(file_system, target):
    for item in file_system:
        if isinstance (item, list):
            result = file_search(item, target)
            if result:
                return result
        elif item == target:
            print("HOORAY!")
            return True
    return False



file_search(file_system, target)