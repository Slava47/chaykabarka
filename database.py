"""
Модуль базы данных для бота Ли Бо.
Содержит определение таблиц и функции инициализации.
"""

import aiosqlite
import os

DB_PATH = os.getenv("DB_PATH", "libo.db")


async def init_db():
    """Создание таблиц в базе данных."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                last_name TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS quiz_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                alcoholic TEXT,
                temperature TEXT,
                taste TEXT,
                tea_strength TEXT,
                strength TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS cocktail_ratings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                cocktail_name TEXT NOT NULL,
                rating TEXT,
                review TEXT,
                quiz_session_id INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id),
                FOREIGN KEY (quiz_session_id) REFERENCES quiz_sessions(id)
            )
        """)
        await db.commit()


async def add_user(user_id: int, username: str, first_name: str, last_name: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT OR IGNORE INTO users (user_id, username, first_name, last_name) VALUES (?, ?, ?, ?)",
            (user_id, username, first_name, last_name),
        )
        await db.commit()


async def add_quiz_session(user_id: int, answers: dict) -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            "INSERT INTO quiz_sessions (user_id, alcoholic, temperature, taste, tea_strength, strength) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (
                user_id,
                answers.get("alcoholic"),
                answers.get("temperature"),
                answers.get("taste"),
                answers.get("tea_strength"),
                answers.get("strength"),
            ),
        )
        await db.commit()
        return cursor.lastrowid


async def add_cocktail_rating(user_id: int, cocktail_name: str, rating: str, review: str, quiz_session_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO cocktail_ratings (user_id, cocktail_name, rating, review, quiz_session_id) "
            "VALUES (?, ?, ?, ?, ?)",
            (user_id, cocktail_name, rating, review, quiz_session_id),
        )
        await db.commit()


async def get_user_stats(user_id: int) -> dict:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        quiz_count = await db.execute_fetchall(
            "SELECT COUNT(*) as cnt FROM quiz_sessions WHERE user_id = ?", (user_id,)
        )
        ratings = await db.execute_fetchall(
            "SELECT cocktail_name, rating, review, created_at FROM cocktail_ratings WHERE user_id = ? ORDER BY created_at DESC",
            (user_id,),
        )
        return {
            "quiz_count": quiz_count[0][0] if quiz_count else 0,
            "ratings": [
                {"cocktail_name": r[0], "rating": r[1], "review": r[2], "created_at": r[3]}
                for r in ratings
            ],
        }
