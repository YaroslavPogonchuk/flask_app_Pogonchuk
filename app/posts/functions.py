from . import post_bp
import os, json

def get_posts_file_path():
    """Повертає шлях до файлу posts.json відносно кореня блюпринта."""
    return os.path.join(post_bp.root_path, 'posts.json')

def read_posts():
    """Зчитує всі пости з JSON-файлу."""
    posts_file = get_posts_file_path()
    if os.path.exists(posts_file):
        with open(posts_file, 'r') as file:
            return json.load(file)
    return []

def write_posts(posts):
    """Записує список постів у JSON-файл."""
    posts_file = get_posts_file_path()
    with open(posts_file, 'w') as file:
        json.dump(posts, file, indent=4)


def get_new_id():
    """Генерує новий унікальний ID для поста"""
    posts = read_posts()
    if posts:
        return max(post['id'] for post in posts) + 1
    return 1