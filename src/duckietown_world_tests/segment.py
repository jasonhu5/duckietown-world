# coding=utf-8

from comptests import comptest, get_comptests_output_dir, run_module_tests

from duckietown_world import get_object_tree
from duckietown_world.svg_drawing import draw_static
from duckietown_world.world_duckietown.map_loading import load_map
from duckietown_world.world_duckietown.segmentify import get_skeleton_graph


@comptest
def lane_pose_segment1():
    outdir = get_comptests_output_dir()

    dm = load_map("udem1")

    _ = get_object_tree(dm, attributes=True)

    res = get_skeleton_graph(dm)

    # area = RectangularArea((0, 0), (3, 3))
    draw_static(res.root2, outdir + "/root2")

    # draw_static(dm, outdir + '/orig')

    _ = get_object_tree(res.root2, attributes=True)


if __name__ == "__main__":
    run_module_tests()
