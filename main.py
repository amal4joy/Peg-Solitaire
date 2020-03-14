import pygame
import game

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Peg Solitaire")
done = False

game.FONT = pygame.font.Font('freesansbold.ttf', 32) 

board = game.Board()
inst = game.Instruction()
score = game.ScoreBoard()
undo = game.UndoButton()
reset = game.ResetButton()


mhandler = game.MouseHandler()
driver = game.Driver(board, score, undo, reset)

for i in range(7):
    for j in range(7):
        if board.cells[i][j]:
            board.cells[i][j].driver = driver
            mhandler.add(board.cells[i][j])

undo.driver = driver
mhandler.add(undo)

reset.driver = driver
mhandler.add(reset)


while not driver.done and not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                elif event.type == pygame.MOUSEMOTION:
                    mhandler.handle_motion()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mhandler.handle_click()
            
        screen.fill(game.BLACK)

        board.draw(screen)
        inst.draw(screen)
        score.draw(screen)
        undo.draw(screen)
        reset.draw(screen)

        pygame.display.flip()

text = game.FONT.render("You Win!", True, game.WHITE)
text_rect = text.get_rect()
text_rect.center = 500, 400
        

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        screen.fill(game.BLACK)
        screen.blit(text, text_rect)
        pygame.display.flip()