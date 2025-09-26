from plyer import notification
import time

# زمان آلارم
time.sleep(5)  # 5 ثانیه منتظر بمانید

# نمایش آلارم
notification.notify(
    title='WakeUpApp',
    message='وقت بیدار شدن است!',
    timeout=10  # مدت زمانی که آلارم نمایش داده می‌شود (ثانیه)
)
