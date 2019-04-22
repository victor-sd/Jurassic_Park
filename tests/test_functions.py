import pytest

from jp.dino import dinosaurs,detailDinosaur

def test_dinosaurs():
    assert dinosaurs() is not None
    assert len(dinosaurs().json())==7
    assert len(dinosaurs().json())>0

def test_detailDinosaur():
    assert detailDinosaur("velociraptor") is not None
    assert len(detailDinosaur("velociraptor").json())==10
    assert len(detailDinosaur("velociraptor").json())>0