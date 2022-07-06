from notificationcenter import *

# Get the NotifiationCenter
notificationcenter = NotificationCenter()
# Define the function you want to perform when you get the notification.
# It should have parameters of (sender, notification name, notification info)
# And return nothing (It can, but it will be thrown away)


def foo(sender, notification_name, info):

observer = notificationcenter.add_observer(with_block=foo,
for_name="bar")

notificationcenter = NotificationCenter()
notificationcenter.post_notification(sender=None,
with_name="bar")
