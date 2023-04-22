import os
from slack_sdk import WebClient
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

import schedule
import time

SLACK_APP_TOKEN = "xapp-1-A04T5RL41NU-4893737265558-a7548758d580fa4ad5038f2c43b37206fd1b8033fc389dafc2c3459ad9013237"
SLACK_BOT_TOKEN = "xoxb-3443467536439-4897261015397-1jPxysixDY52FEB6cPA4aoR5"
SLACK_USER_TOKEN = "xoxp-3443467536439-3489683201008-4900235325203-2c67556a1b1113d9aa45d646357afba0"
SLACK_CHANNEL_ID = "C03DUA8CE03"

app = App(token=SLACK_BOT_TOKEN)
client = WebClient(token=SLACK_USER_TOKEN)


def vote_command():
    options = [
        {"text": {"type": "plain_text", "text": "8:00 출근 ~ 5:00 퇴근"}, "value": "8-5"},
        {"text": {"type": "plain_text", "text": "8:30 출근 ~ 5:30 퇴근"}, "value": "8:30-5:30"},
        {"text": {"type": "plain_text", "text": "9:00 출근 ~ 6:00 퇴근"}, "value": "9-6"},
        {"text": {"type": "plain_text", "text": "9:30 출근 ~ 6:30 퇴근"}, "value": "9:30-6:30"},
        {"text": {"type": "plain_text", "text": "10:00 출근 ~ 7:00 퇴근"}, "value": "10-7"}
    ]
    blocks = [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "투표: 차주 출퇴근 계획을 정하셨나요?"},
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "아래 옵션 중 하나를 선택해주세요."},
            "accessory": {
                "type": "radio_buttons",
                "options": options,
                "action_id": "vote"
            }
        }
    ]
    response = client.chat_postMessage(channel=SLACK_CHANNEL_ID, blocks=blocks)
    print(f"투표가 시작되었습니다! 메시지를 확인해주세요. ({response['ts']})")

    # 사용자 응답 결과 받아오기
    @app.action("vote")
    def handle_vote(ack, body, logger):
        selected_option = body["actions"][0]["selected_option"]["value"]
        user_id = body["user"]["id"]
        user_name = client.users_info(user=user_id)["user"]["real_name"]
        print(user_name)
        ack(f"{user_name}님이 {selected_option}을(를) 선택하셨습니다!")


vote_command()  # 프로그램 실행 시 바로 투표 생성

# 매주 금요일 오전 10시에 vote_command() 함수 실행
schedule.every().friday.at("10:00").do(vote_command)

if __name__ == "__main__":
    handler = SocketModeHandler(app_token=SLACK_APP_TOKEN, app=app)
    handler.start()
    while True:
        schedule.run_pending()
        time.sleep(1)
