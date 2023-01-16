def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    return {'name': grades['name'], 'top_grade': max(grades['grades'])}

info = {'name': 'Roman', 'grades': '30'}

print(top_grade(info))