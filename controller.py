import json
from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/patinko")

class Item(BaseModel):
    yuu_time: str
    day_time: str
    dai_number: str
    model_name: str
    bonus: str
    now_roud_count: str
    total_round_count: str
    last_dedama: str
    round_per_en: str

class Item_total(BaseModel):
    today: str
    dai_number: str
    model_name: str
    total_bonus: str
    total_round_count: str
    total_last_dedama: str
    ago1_dedama: str
    ago1_round: str
    ago2_dedama: str
    ago2_round: str
    ago3_dedama: str
    ago3_round: str
    ago4_dedama: str
    ago4_round: str
    ago5_dedama: str
    ago5_round: str
    ago6_dedama: str
    ago6_round: str
    ago7_dedama: str
    ago7_round: str
    

@router.get("/akasaka_all")
def read_root():
    json_open = open('data\\akasaka_all.json', 'r',encoding="utf-8_sig")
    json_load = json.load(json_open)
    return json_load

@router.get("/akasaka_real_time")
def read_root():
    json_open = open('data\\akasaka_real_time.json', 'r',encoding="utf-8_sig")
    json_load = json.load(json_open)
    return json_load

@router.get("/akasaka_total")
def read_root():
    json_open = open('data\\akasaka_total.json', 'r',encoding="utf-8_sig")
    json_load = json.load(json_open)
    return json_load

@router.get("/boomtengin_all")
def read_root():
    json_open = open('data\\boomtengin_all.json', 'r',encoding="utf-8_sig")
    json_load = json.load(json_open)
    return json_load

@router.get("/boomtengin_real_time")
def read_root():
    json_open = open('data\\boomtengin_real_time.json', 'r',encoding="utf-8_sig")
    json_load = json.load(json_open)
    return json_load

@router.get("/boomtengin_total")
def read_root():
    json_open = open('data\\boomtengin_total.json', 'r',encoding="utf-8_sig")
    json_load = json.load(json_open)
    return json_load


@router.post("/akasaka_all")
def create_file(json_lists: List[Item]):
    new_json = []
    for json_list in json_lists:
        new_json.append({
          "yuu_time": json_list.yuu_time,
          "day_time": json_list.day_time,
          "dai_number": json_list.dai_number,
          "model_name": json_list.model_name,
          "bonus": json_list.bonus,
          "now_roud_count": json_list.now_roud_count,
          "total_round_count": json_list.total_round_count,
          "last_dedama": json_list.last_dedama,
          "round_per_en": json_list.round_per_en
        })
    output_filename = open('data\\akasaka_all.json', 'r',encoding="utf-8_sig")
    with open(output_filename.name, 'w', encoding="utf-8") as f:
        json.dump(new_json, f, ensure_ascii=False)

@router.post("/akasaka_real_time")
def create_file(json_lists: List[Item]):
    new_json = []
    for json_list in json_lists:
        new_json.append({
          "yuu_time": json_list.yuu_time,
          "day_time": json_list.day_time,
          "dai_number": json_list.dai_number,
          "model_name": json_list.model_name,
          "bonus": json_list.bonus,
          "now_roud_count": json_list.now_roud_count,
          "total_round_count": json_list.total_round_count,
          "last_dedama": json_list.last_dedama,
          "round_per_en": json_list.round_per_en
        })
    output_filename = open('data\\akasaka_real_time.json', 'r',encoding="utf-8_sig")
    with open(output_filename.name, 'w', encoding="utf-8") as f:
        json.dump(new_json, f, ensure_ascii=False)

@router.post("/akasaka_total")
def create_file(json_lists: List[Item_total]):
    new_json = []
    for json_list in json_lists:
        new_json.append({
          "today": json_list.today,
          "dai_number": json_list.dai_number,
          "model_name": json_list.model_name,
          "total_bonus": json_list.total_bonus,
          "total_round_count": json_list.total_round_count,
          "total_last_dedama": json_list.total_last_dedama,
          "ago1_dedama": json_list.ago1_dedama,
          "ago2_dedama": json_list.ago2_dedama,
          "ago3_dedama": json_list.ago3_dedama,
          "ago4_dedama": json_list.ago4_dedama,
          "ago5_dedama": json_list.ago5_dedama,
          "ago6_dedama": json_list.ago6_dedama,
          "ago7_dedama": json_list.ago7_dedama,
          "ago1_round": json_list.ago1_round,
          "ago2_round": json_list.ago2_round,
          "ago3_round": json_list.ago3_round,
          "ago4_round": json_list.ago4_round,
          "ago5_round": json_list.ago5_round,
          "ago6_round": json_list.ago6_round,
          "ago7_round": json_list.ago7_round,
        })
    output_filename = open('data\\akasaka_total.json', 'r',encoding="utf-8_sig")
    with open(output_filename.name, 'w', encoding="utf-8") as f:
        json.dump(new_json, f, ensure_ascii=False)


@router.post("/boomtengin_all")
def create_file(json_lists: List[Item]):
    new_json = []
    for json_list in json_lists:
        new_json.append({
          "yuu_time": json_list.yuu_time,
          "day_time": json_list.day_time,
          "dai_number": json_list.dai_number,
          "model_name": json_list.model_name,
          "bonus": json_list.bonus,
          "now_roud_count": json_list.now_roud_count,
          "total_round_count": json_list.total_round_count,
          "last_dedama": json_list.last_dedama,
          "round_per_en": json_list.round_per_en
        })
    output_filename = open('data\\boomtengin_all.json', 'r',encoding="utf-8_sig")
    with open(output_filename.name, 'w', encoding="utf-8") as f:
        json.dump(new_json, f, ensure_ascii=False)

@router.post("/boomtengin_real_time")
def create_file(json_lists: List[Item]):
    new_json = []
    for json_list in json_lists:
        new_json.append({
          "yuu_time": json_list.yuu_time,
          "day_time": json_list.day_time,
          "dai_number": json_list.dai_number,
          "model_name": json_list.model_name,
          "bonus": json_list.bonus,
          "now_roud_count": json_list.now_roud_count,
          "total_round_count": json_list.total_round_count,
          "last_dedama": json_list.last_dedama,
          "round_per_en": json_list.round_per_en
        })
    output_filename = open('data\\boomtengin_real_time.json', 'r',encoding="utf-8_sig")
    with open(output_filename.name, 'w', encoding="utf-8") as f:
        json.dump(new_json, f, ensure_ascii=False)

@router.post("/boomtengin_total")
def create_file(json_lists: List[Item_total]):
    new_json = []
    for json_list in json_lists:
        new_json.append({
          "today": json_list.today,
          "dai_number": json_list.dai_number,
          "model_name": json_list.model_name,
          "total_bonus": json_list.total_bonus,
          "total_round_count": json_list.total_round_count,
          "total_last_dedama": json_list.total_last_dedama,
          "ago1_dedama": json_list.ago1_dedama,
          "ago2_dedama": json_list.ago2_dedama,
          "ago3_dedama": json_list.ago3_dedama,
          "ago4_dedama": json_list.ago4_dedama,
          "ago5_dedama": json_list.ago5_dedama,
          "ago6_dedama": json_list.ago6_dedama,
          "ago7_dedama": json_list.ago7_dedama,
          "ago1_round": json_list.ago1_round,
          "ago2_round": json_list.ago2_round,
          "ago3_round": json_list.ago3_round,
          "ago4_round": json_list.ago4_round,
          "ago5_round": json_list.ago5_round,
          "ago6_round": json_list.ago6_round,
          "ago7_round": json_list.ago7_round,
        })
    output_filename = open('data\\boomtengin_total.json', 'r',encoding="utf-8_sig")
    with open(output_filename.name, 'w', encoding="utf-8") as f:
        json.dump(new_json, f, ensure_ascii=False)
