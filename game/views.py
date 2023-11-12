from django.shortcuts import redirect, render

from game.utis.api import fetch_questions


def index(request):
	return redirect("game")


def game(request):
	difficulty_levels = ["easy", "medium", "hard"]
	questions = fetch_questions(difficulty_levels)
	context = {
		"questions": questions
	}
	return render(request, 'game/game_screen.html')
