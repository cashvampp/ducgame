import pytest
import pygame
from main import move_level, check_shot


# Тест для функции move_level
def test_move_level():
    # Создаем тестовые данные
    coords = [[(100, 200), (300, 400)], [(500, 600), (700, 800)], [(900, 1000), (1100, 1200)]]
    
    # Вызываем функцию move_level
    new_coords = move_level(coords)
    
    # Проверяем, что новые координаты изменились соответственно
    assert new_coords != coords
    # Проверяем, что длина списка новых координат равна длине списка старых координат
    assert len(new_coords) == len(coords)
    # Проверяем, что длина каждого внутреннего списка новых координат равна длине соответствующего внутреннего списка старых координат
    for new_sublist, old_sublist in zip(new_coords, coords):
        assert len(new_sublist) == len(old_sublist)

# Тест для функции check_shot
def test_check_shot():
    # Создаем тестовые данные
    targets = [[pygame.rect.Rect(100, 200, 50, 50)], [pygame.rect.Rect(300, 400, 50, 50)], [pygame.rect.Rect(500, 600, 50, 50)]]
    coords = [[(100, 200)], [(300, 400)], [(500, 600)]]
    
    # Вызываем функцию check_shot
    new_coords = check_shot(targets, coords)
    
    # Проверяем, что новые координаты изменились соответственно
    assert new_coords != coords
    # Проверяем, что длина списка новых координат равна длине списка старых координат
    assert len(new_coords) == len(coords)
    # Проверяем, что длина каждого внутреннего списка новых координат равна длине соответствующего внутреннего списка старых координат
    for new_sublist, old_sublist in zip(new_coords, coords):
        assert len(new_sublist) == len(old_sublist)

