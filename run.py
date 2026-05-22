import os
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450
FPS = 60
WHITE = (255, 255, 255)
BASE_PATH = os.path.dirname(__file__)
IMAGE_FOLDER = os.path.join(BASE_PATH, "image")
MUSIC_FILE = os.path.join(BASE_PATH, "music.mp3")


SLIDES = [
    {
        "text": "moi sang chu nhat",
        "speed_ms": 340,
        "x": 250,
        "y": 250,
        "image_name": "img0.jpg",
    },
    {
        "text": "troi ko co may bay",
        "speed_ms": 340,
        "x": 300,
        "y": 300,
        "image_name": "img1.jpg",
    },
    {
        "text": "gio chang ri rao",
        "speed_ms": 340,
        "x": 350,
        "y": 100,
        "image_name": "img2.jpg",
    },
    {
        "text": "ma cay van lung lay",
        "speed_ms": 340,
        "x": 100,
        "y": 100,
        "image_name": "img3.jpg",
    },
    {
        "text": "len ngat thu mot",
        "speed_ms": 340,
        "x": 400,
        "y": 100,
        "image_name": "img4.jpg",
    },
    {
        "text": "nhanh hoa nam trong tay",
        "speed_ms": 300,
        "x": 400,
        "y": 100,
        "image_name": "img5.jpg",
    },
    {
        "text": "lieu anh con dang say",
        "speed_ms": 300,
        "x": 250,
        "y": 350,
        "image_name": "img6.jpg",
    },
]


def load_image(image_name):
    path = os.path.join(IMAGE_FOLDER, image_name)
    if not os.path.isfile(path):
        return None
    try:
        return pygame.image.load(path).convert_alpha()
    except pygame.error:
        return None


def load_music():
    if not os.path.isfile(MUSIC_FILE):
        print(f"Âm thanh không tìm thấy: {MUSIC_FILE}")
        return False
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(MUSIC_FILE)
        return True
    except pygame.error as error:
        print("Không thể khởi tạo âm thanh:", error)
        return False


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("code by Huynh Nhat Hoang")
    font = pygame.font.SysFont("Arial", 32)
    clock = pygame.time.Clock()

    slide_index = 0
    slide = SLIDES[slide_index]
    words = slide["text"].split()
    word_index = 0
    display_text = ""
    current_image = load_image(slide["image_name"])

    music_ready = load_music()
    if music_ready:
        pygame.mixer.music.play(1)

    current_time = pygame.time.get_ticks()
    next_word_time = current_time + slide["speed_ms"]
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_time = pygame.time.get_ticks()

        if word_index < len(words) and current_time > next_word_time:
            display_text += words[word_index] + " "
            word_index += 1
            next_word_time = current_time + slide["speed_ms"]

        elif word_index >= len(words) and slide_index < len(SLIDES) - 1 and current_time > next_word_time:
            slide_index += 1
            slide = SLIDES[slide_index]
            words = slide["text"].split()
            word_index = 0
            display_text = ""
            current_image = load_image(slide["image_name"])
            next_word_time = current_time + slide["speed_ms"]

        screen.fill((0, 0, 0))
        if current_image is not None:
            screen.blit(current_image, (0, 0))

        if display_text:
            text_surface = font.render(display_text, True, WHITE)
            screen.blit(text_surface, (slide["x"], slide["y"]))

        pygame.display.flip()
        clock.tick(FPS)




if __name__ == "__main__":
    main()