from polygon import Polygon

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
