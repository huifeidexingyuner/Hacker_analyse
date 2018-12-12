'''
主文件
'''
from get_actions import get_actions
from get_ability import get_ability
from get_area import get_area
from get_active import get_active


def main(jsoname):
    print("该黑客画像如下：")
    get_area(jsoname)
    activite_scores=get_active(jsoname)
    action_scores = get_actions(jsoname)
    get_ability(activite_scores,action_scores)

#名为alco黑客的人物画像
#main("./data/user/alco.json")
#名为0x00pf黑客的人物画像
main("./data/user/0x00pf.json")
