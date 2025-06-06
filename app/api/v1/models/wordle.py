from pydantic import BaseModel
from typing import List, Optional


class GuessRequest(BaseModel):
    word: str


class GameResponse(BaseModel):
    game_id: str
    attempts: List[dict]
    attempts_used: int
    game_over: bool
    won: bool
    target_word: Optional[str] = None


class GuessResponse(BaseModel):
    game_id: str
    guess: str
    result: List[str]
    attempts_used: int
    game_over: bool
    won: bool
    target_word: Optional[str] = None
