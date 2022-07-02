from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_main_resource():
    response_auth = client.get(f"/")
    assert response_auth.status_code == 200

def test_child_resource():
    response_auth = client.get(f"/api/v1/test")
    assert response_auth.status_code == 200

def test_child_users_resource():
    response_auth = client.get(f"/api/v1/users")
    assert response_auth.status_code == 200

def test_child_posts_resource():
    response_auth = client.get(f"/api/v1/posts")
    assert response_auth.status_code == 200

def test_child_root_kevin_resource():
    response_auth = client.get(f"/kevin/34")
    assert response_auth.status_code == 200