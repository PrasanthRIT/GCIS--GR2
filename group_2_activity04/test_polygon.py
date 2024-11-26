from polygon import Polygon
from pytest import approx

#Step1
def test_polygon_intialized():
    Polygon1=Polygon('square',[2,2,2,2])
    Polygon2=Polygon('triangle',[3,3,3])

    #Testing Getter Methods
    assert 'square'==Polygon1.get_name()
    assert 'triangle'==Polygon2.get_name()

    assert [2,2,2,2]==Polygon1.get_sides()
    assert [3,3,3]==Polygon2.get_sides()
    
    Polygon1.set_name('SQUARES')
    Polygon2.set_name('TRIANGLES')
    Polygon1.set_sides([3,3,3,3])
    Polygon2.set_sides([2,2,2])

    #Testing Setter Methods
    assert "SQUARES"==Polygon1.get_name()
    assert "TRIANGLES"==Polygon2.get_name()

    assert [3,3,3,3]==Polygon1.get_sides()
    assert [2,2,2]==Polygon2.get_sides()

#Step 4:
def test_calculate_circumference():
    Polygon1=Polygon('square',[2,2,2,2])
    Polygon2=Polygon('triangle',[2.5,6,1.8])
    
    assert Polygon1.calc_circumference() == 8
    assert approx(Polygon2.calc_circumference()) == 10.3