import pytest

from jp.dino import dinosaurs

def test_dinosaurs():
    assert dinosaurs() is not None
    assert len(dinosaurs().json())==7
    assert len(dinosaurs().json())>0