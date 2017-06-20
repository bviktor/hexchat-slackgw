import hexchat

__module_name__ = "slackgw"
__module_version__ = "1.0"
__module_description__ = "Format Slack gateway messages"

def chanmsg_cb(word, word_eol, userdata):
  if hexchat.nickcmp(hexchat.strip(word[0], -1, 3), "slackgateway") == 0:
    if word[1].find(">") != -1:
      nick = word[1].split(">")[0][1:]
      msg = word[1].split(">")[1][1:]
      hexchat.emit_print("Channel Message", nick, msg)
      return hexchat.EAT_HEXCHAT
  return hexchat.EAT_NONE

hexchat.hook_print("Channel Message", chanmsg_cb)
hexchat.hook_print("Channel Msg Hilight", chanmsg_cb)
