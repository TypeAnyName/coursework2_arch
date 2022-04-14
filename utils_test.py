import pytest
from utils import get_posts_all, posts_by_user, get_comments_by_post_id, search_for_posts, get_post_by_pk
from main import app


class TestUtils:
    def test_posts(self):
        assert len(get_posts_all()) == 8, "Ошибка всех постов"
        assert type(get_posts_all()) == list, "Ошибка всех постов"

    def test_users_posts(self):
        assert len(posts_by_user("hank")) == 2, "Ошибка по юзерам"
        assert type(posts_by_user("hank")) == list, "Ошибка поюзерам"
        for i in posts_by_user("hank"):
            if i['poster_name'] == 'hank':
                assert True
                break
            else:
                assert False, "Ошибка поюзерам"

    def test_comments(self):
        assert len(get_comments_by_post_id(3)) == 4, "Ошибка по комментам"
        assert type(get_comments_by_post_id(3)) == list, "Ошибка по комментам"
        for i in get_comments_by_post_id(3):
            if i["comment"] == 'Выглядит неплохо )':
                assert True
                break
            else:
                assert False, "Ошибка по комментам"

    def test_query(self):
        assert len(search_for_posts("На")) == 8, "Ошибка по вхождениям"
        assert type(search_for_posts("На")) == list, "Ошибка по вхождениям"

    def test_pk(self):
        assert type(get_comments_by_post_id(3)) == list, "Ошибка id поста"


class TestAPI:
    def test_all_json(self):
        response = app.test_client().get('/api/posts', follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса всех постов неверный"
        assert type(response.json) == list, "Ошибка типа данных json"
        for i in response.json:
            if i['poster_name'] == 'leo':
                assert True
                break
            else:
                assert False

    def test_id_json(self):
        response = app.test_client().get('/api/posts/3', follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса всех постов неверный"
        assert type(response.json) == dict, "Ошибка типа данных json"
