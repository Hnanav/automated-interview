import pymysql
from skills import prober_depersonalized_skill

print(prober_depersonalized_skill)
# Giả sử bạn đã có biến recent_history
recent_history = "Đây là lịch sử trò chuyện của người dùng."

# Thay thế {{$recent_history}} bằng giá trị thực tế
prober_depersonalized_skill = prober_depersonalized_skill.replace("{{$recent_history}}", recent_history)
print(prober_depersonalized_skill)
