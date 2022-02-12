import os
import json
from typing import Optional
from typing import List

from fastapi import APIRouter
from pydantic import BaseModel



router = APIRouter(prefix="/patinko")

class Item(BaseModel):
    day_time: Optional[str] = None
    dai_number: Optional[str] = None
    model_name: Optional[str] = None
    bonus: Optional[str] = None
    now_roud_count: Optional[str] = None
    total_round_count: Optional[str] = None
    last_dedama: Optional[str] = None
    round_per_en: Optional[str] = None
    first_bonus_round: Optional[str] = None

class Item_total(BaseModel):
    day_time: Optional[str] = None
    dai_number: Optional[str] = None
    model_name: Optional[str] = None
    total_bonus: Optional[str] = None
    total_round_count: Optional[str] = None
    total_last_dedama: Optional[str] = None
    ago1_dedama: Optional[str] = None
    ago1_round: Optional[str] = None
    ago2_dedama: Optional[str] = None
    ago2_round: Optional[str] = None
    ago3_dedama: Optional[str] = None
    ago3_round: Optional[str] = None
    ago4_dedama: Optional[str] = None
    ago4_round: Optional[str] = None
    ago5_dedama: Optional[str] = None
    ago5_round: Optional[str] = None
    ago6_dedama: Optional[str] = None
    ago6_round: Optional[str] = None
    ago7_dedama: Optional[str] = None
    ago7_round: Optional[str] = None
    

@router.get("/akasaka_detail_url_list")
def read_root():
    files = os.listdir("./data/dai_detail/akasaka")
    
    list = ['a', 1, 'b', 2, 'c', 3]
    dict = {"url": list[i + 1] for i in range(0, len(files))}
    json_load = json.load(dict)
    return json_load

@router.get("/boomtengin_detail_url_list")
def read_root():
    files = os.listdir("./data/dai_detail/boomtengin")
    json_load = json.load(files)
    return json_load

@router.get("/akasaka_detail/{dai_number}")
def read_root(dai_number):
    json_open = open(f'data/dai_detail/akasaka/{dai_number}', 'r',encoding="utf-8_sig")
    json_load = json.load(json_open)
    return json_load

@router.get("/boomtengin_detail/{dai_number}")
def read_root(dai_number):
    json_open = open(f'data/dai_detail/boomtengin/{dai_number}', 'r',encoding="utf-8_sig")
    json_load = json.load(json_open)
    return json_load

@router.get("/akasaka_all")
def read_root():
    json_open = open('data/akasaka_all.json', 'r',encoding="utf-8_sig")
    json_load = json.load(json_open)
    return json_load

@router.get("/akasaka_total")
def read_root():
    json_open = open('data/akasaka_total.json', 'r',encoding="utf-8_sig")
    json_load = json.load(json_open)
    return json_load

@router.get("/boomtengin_all")
def read_root():
    json_open = open('data/boomtengin_all.json', 'r',encoding="utf-8_sig")
    json_load = json.load(json_open)
    return json_load

@router.get("/boomtengin_total")
def read_root():
    json_open = open('data/boomtengin_total.json', 'r',encoding="utf-8_sig")
    json_load = json.load(json_open)
    return json_load


@router.post("/boomtengin_detail/{dai_number}")
def create_file(dai_number, json_lists: List[Item]):
    new_json = []
    for json_list in json_lists:
        new_json.append({
          "day_time": json_list.day_time,
          "dai_number": json_list.dai_number,
          "model_name": json_list.model_name,
          "bonus": json_list.bonus,
          "now_roud_count": json_list.now_roud_count,
          "total_round_count": json_list.total_round_count,
          "last_dedama": json_list.last_dedama,
          "round_per_en": json_list.round_per_en,
          "first_bonus_round": json_list.first_bonus_round
        })
    with open(f'data/dai_detail/boomtengin/{dai_number}', 'w', encoding="utf-8_sig") as f:
        json.dump(new_json, f, ensure_ascii=False)
        

@router.post("/akasaka_detail/{dai_number}")
def create_file(dai_number, json_lists: List[Item]):
    new_json = []
    for json_list in json_lists:
        new_json.append({
          "day_time": json_list.day_time,
          "dai_number": json_list.dai_number,
          "model_name": json_list.model_name,
          "bonus": json_list.bonus,
          "now_roud_count": json_list.now_roud_count,
          "total_round_count": json_list.total_round_count,
          "last_dedama": json_list.last_dedama,
          "round_per_en": json_list.round_per_en,
          "first_bonus_round": json_list.first_bonus_round
        })
    with open(f'data/dai_detail/akasaka/{dai_number}', 'w', encoding="utf-8_sig") as f:
        json.dump(new_json, f, ensure_ascii=False)


@router.post("/akasaka_all")
def create_file(json_lists: List[Item]):
    new_json = []
    for json_list in json_lists:
        new_json.append({
          "day_time": json_list.day_time,
          "dai_number": json_list.dai_number,
          "model_name": json_list.model_name,
          "bonus": json_list.bonus,
          "now_roud_count": json_list.now_roud_count,
          "total_round_count": json_list.total_round_count,
          "last_dedama": json_list.last_dedama,
          "round_per_en": json_list.round_per_en
        })
    with open('data/akasaka_all.json', 'w', encoding="utf-8_sig") as f:
        json.dump(new_json, f, ensure_ascii=False)


@router.post("/akasaka_total")
def create_file(json_lists: List[Item_total]):
    new_json = []
    for json_list in json_lists:
        new_json.append({
          "day_time": json_list.day_time,
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
    with open('data/akasaka_total.json', 'w', encoding="utf-8_sig") as f:
        json.dump(new_json, f, ensure_ascii=False)


@router.post("/boomtengin_all")
def create_file(json_lists: List[Item]):
    new_json = []
    for json_list in json_lists:
        new_json.append({
          "day_time": json_list.day_time,
          "dai_number": json_list.dai_number,
          "model_name": json_list.model_name,
          "bonus": json_list.bonus,
          "now_roud_count": json_list.now_roud_count,
          "total_round_count": json_list.total_round_count,
          "last_dedama": json_list.last_dedama,
          "round_per_en": json_list.round_per_en,
          "first_bonus_round": json_list.first_bonus_round
        })
    with open('data/boomtengin_all.json', 'w', encoding="utf-8_sig") as f:
        json.dump(new_json, f, ensure_ascii=False)


@router.post("/boomtengin_total")
def create_file(json_lists: List[Item_total]):
    new_json = []
    for json_list in json_lists:
        new_json.append({
          "day_time": json_list.day_time,
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
    with open('data/boomtengin_total.json', 'w', encoding="utf-8_sig") as f:
        json.dump(new_json, f, ensure_ascii=False)
