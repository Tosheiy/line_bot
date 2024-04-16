from line_bot_pushNotion.pushToNotion import pushToNotion

def create_single_text_message(message):
    if message == 'Notion':
        status = pushToNotion('LINEに動きがありました')
        if(status!="success"):
            print(status)
            message = '[エラーメッセージ]' + status + '\n送信に失敗しました。'
        else:
            message = '送信完了'
    test_message = [
                {
                    'type': 'text',
                    'text': message
                }
            ]
    return test_message
