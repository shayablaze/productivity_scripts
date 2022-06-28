import asyncio

from mitmproxy import proxy, options, http
from mitmproxy.tools.dump import DumpMaster
import threading

from secrets_encryptor import SecretsEncryptor


class AddHeader:
    def __init__(self, stam):
        self.num = 0
        self.stam = stam
        self.a = stam
        self.b = stam

    def response(self, flow):
        self.num = self.num + 1
        self.stam = self.stam + 10
        print(self.num)
        flow.response.headers["count"] = str(self.num)


    def request(self, flow: http.HTTPFlow) -> None:
        print('i am in the second proxy')

        path_test = flow.request.data.path

        print('just  url => ')
        print(flow.request.url)
        print('just  path_test => ')
        print(path_test)

        # print('data content => ')
        # print(flow.request.data.content)
        print('just  content => ')
        print(flow.request.content)


        # content_string = flow.request.content.decode("utf-8")
        # content_string = content_string.replace('Forbidden', 'AMON_AMARTH')
        # flow.request.content = str.encode(content_string)
        print('doing the real thing')

        secrets = {
            'Taurus CLI Tool': 'USED_TO_BE_TAURUS_CLI_TOOL',
            'Status changed to TERMINATING': 'USED_TO_BE_STATUS_CHANGED',
            'Submitting json of length': 'USED_TO_BE_SUBMITTING',
            'Forbidden': 'USED_TO_BE_FORBIDDEN_NOT_ANYMORE',
        }
        if not flow.request.url.startswith('https://s3.amazonaws.com'):
            secrets_encryptor = SecretsEncryptor()
            encrypted_data_content = secrets_encryptor.encrypt_data_content(flow.request.content, secrets)
            print('returned data is ')
            print(encrypted_data_content)
            flow.request.content = encrypted_data_content
        else:
            print('skipping the thing i am s3')

def run_proxy(listen_port):

    opts = options.Options(listen_host='127.0.0.1', listen_port=listen_port)
    pconf = proxy.config.ProxyConfig(opts)
    opts.add_option("body_size_limit", int, 0, "")
    opts.add_option("keep_host_header", bool, True, "")

    m = DumpMaster(None)
    m.server = proxy.server.ProxyServer(pconf)
    m.addons.add(AddHeader(45))
    print(m.addons)
    print('before')


    def start_proxy():
        asyncio.set_event_loop(m.server.channel.loop)
        try:
            m.run()
        except KeyboardInterrupt:
            m.shutdown()
        print('after')


    m_thread = threading.Thread(target=start_proxy)
    m_thread.daemon = False
    m_thread.start()

run_proxy(4444)
# run_proxy(5559)