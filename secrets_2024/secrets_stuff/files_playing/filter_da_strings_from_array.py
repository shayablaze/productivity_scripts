
exclusion_files = ['/tmp/artifacts/admin/atop.binlog', '/tmp/artifacts/libpolkit-gobject-1-0_0.105-33_amd64.deb', '/tmp/artifacts/policykit-1_0.105-33_amd64.deb', '/tmp/artifacts/libpolkit-agent-1-0_0.105-33_amd64.deb']
secrets_list = ['really' ,'dont', '/tmp/artifacts/admin/atop.binlog', '/tmp/artifacts/libpolkit-gobject-1-0_0.105-33_amd64.deb', 'mind', 'if', 'you', '/tmp/artifacts/libpolkit-agent-1-0_0.105-33_amd64.deb', 'sit']
print ([string for string in secrets_list if string not in exclusion_files])