from main import check_shot, move_level
import pygame

def test_move_level():
    # Test the move_level function
    coords = [[(100, 100), (200, 200)], [(300, 300), (400, 400)], [(500, 500), (600, 600)]]
    new_coords = move_level(coords)
    expected_new_coords = [[(98, 100), (198, 200)], [(296, 300), (396, 400)], [(492, 500), (592, 600)]]
    assert new_coords == expected_new_coords

def test_check_shot():
    # Test the check_shot function
    targets = [
        [pygame.rect.Rect(100, 100, 50, 50), pygame.rect.Rect(200, 200, 50, 50)],
        [pygame.rect.Rect(300, 300, 50, 50), pygame.rect.Rect(400, 400, 50, 50)],
        [pygame.rect.Rect(500, 500, 50, 50), pygame.rect.Rect(600, 600, 50, 50)]
    ]
    coords = [[(100, 100), (200, 200)], [(300, 300), (400, 400)], [(500, 500), (600, 600)]]
    new_coords = check_shot(targets, coords)
    expected_new_coords = [[(100, 100)], [(300, 300), (400, 400)], [(500, 500), (600, 600)]]
    assert new_coords == expected_new_coords

# Add more test cases for other functions
