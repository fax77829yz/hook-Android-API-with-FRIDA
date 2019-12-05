import frida, sys, os

packageName = "$PACKAGENAME"

def messagesCallback(message, data):
    if message['type'] == 'send':
        print(message['payload'])
    elif message['type'] == 'error':
        print(message['stack'])

hookCode = None
with open(os.path.dirname(os.path.realpath(__file__)) + '/hookAPI.js') as f:
    hookCode = f.read()
process=frida.get_remote_device().attach(packageName) # attach target app
print(process)
process.enable_debugger()
script = process.create_script(hookCode) # load script in 'script'
script.on('message', messagesCallback) # bug report
script.load() # inject script
print(process) # check the load is successful
sys.stdin.read() # pause this python file