查询IP示范代码

111.txt为实际要查询的ip文件，dict.txt为格式为xxx.xxx.xxx.xxx/24或者xxx.xxx.xxx.xxx/17等的IP子网掩码格式文件。
要求根据给出的ip，查询落在哪个掩码范围里，以及统计个数。

返回结果

223.27.116.11 is in 223.27.116.0/22

223.27.116.11 is in 223.27.116.0/22

223.27.116.11 is in 223.27.116.0/22

223.27.116.11 is in 223.27.116.0/22

223.27.116.11 is in 223.27.116.0/22

223.27.116.11 is in 223.27.116.0/22

223.27.116.11 is in 223.27.116.0/22

27.111.128.1 is in 27.111.128.0/19

[('223.27.116.0/22', 528), ('27.111.128.0/19', 1)]

done

倒数二行是统计，也可用awk匹配结果得出总计。