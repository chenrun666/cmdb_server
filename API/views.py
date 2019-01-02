import json

from django.http import HttpResponse
from repository import models


# Create your views here.

def asset(request):
    if request.method == "POST":
        # 新资产信息
        server_info = json.loads(request.body.decode("utf-8"))
        hostname = server_info['basic']['data']['hostname']
        server_obj = models.Server.objects.filter(hostname=hostname).first()
        if not server_obj:
            return HttpResponse("当前主机名在资产中未录入")
        # 发来的数据
        disk_info_dic = server_info["disk"]["data"]
        memory_info_dic = server_info["memory"]["data"]
        # 硬盘信息的集合
        disk_set_new = set(disk_info_dic.keys())
        memory_set_new = set(memory_info_dic.keys())

        # 数据库中的信息
        # 资产信息
        asset_obj = server_obj.asset

        # 硬盘，内存信息
        disk_list = server_obj.disk.all()
        memory_list = server_obj.memory.all()
        # 数据库中的硬盘与内存的集合信息
        disk_set_db = set((str(item) for item in disk_list))
        memory_set_db = set((str(item) for item in memory_list))

        # 处理 老[1,2,3,4]   新[2,3,4,5]
        # 删除
        # 老的集合差集新的集合
        delete_disk_obj = disk_set_db - disk_set_new
        for disk_obj in delete_disk_obj:
            # 删除数据库中的信息
            pass

        delete_memory_obj = memory_set_db - memory_set_new
        for memory_obj in delete_memory_obj:
            # 删除数据库中的内容
            pass

        # 更新
        update_disk_obj = disk_set_db & disk_set_new
        for disk_update in update_disk_obj:
            # 更新数据库的信息
            pass

        update_memory_obj = memory_set_new & memory_set_db
        for memory_update in update_memory_obj:
            # 更新数据库中的信息
            pass

        # 添加
        add_disk_obj = disk_set_new - disk_set_db
        for disk_add in add_disk_obj:
            # 添加信息到数据库中
            pass

        add_memory_obj = memory_set_new - memory_set_db
        for add_obj in add_memory_obj:
            # 添加信息到数据库中
            pass

        # 处理
        """
            1， 根据新资产和原资产进行比较：老[1, 5]  新[1, 2, 3, 4]
            2， 增加的槽位：老的集合差集新的集合，得到的是要删除的槽位 更新的槽位：新的槽位差集老得槽位要更新的槽位
            3， 增加：
                    server_info中根据[1,]找到资产详细：入库
                删除：
                    数据库中找到当前服务器的硬盘
                    
                更新：交集更新
                    
        """

    return HttpResponse("...")
