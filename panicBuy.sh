# 定时抢单,Android shell获取和模拟点击事件
echo "开始定时抢单程序"
# 天猫到点抢购时间，精确到毫秒, 2022-05-15 20:00:00
startTime=1652616000000
echo "startTime:$startTime"

while :
do
# 获取当前时间
curTime=`date +%s%N`
curTime=`expr $curTime / 1000000`
if [ $curTime -gt $startTime ]
then
    # 结算
    input tap 908 2054 
    # 提交订单
    input tap 913 2185 
    # 确认交易
    input tap 908 2090
    echo "$curTime -gt $startTime"
    echo "定时抢单成功"
    exit 1
else
   sleep 0.001
fi

done

echo "退出定时抢单程序"