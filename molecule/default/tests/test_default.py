def test_account_present(host):
    group = host.group("ctfd")
    user = host.user("ctfd")
    assert group.exists
    assert user.exists

def test_directory(host):
    # check owner and permission 0755
    dirs = [
        "/opt/ctfd",
    ]

    for folder in dirs:
        d = host.file(folder)
        assert d.is_directory
        assert d.user == "ctfd"
        assert d.group == "ctfd"
        assert oct(d.mode) == "0o755"

def test_service_file(host):
    service_file = host.file("/etc/systemd/system/ctfd.service")
    assert service_file.exists

def test_service(host):
    service = host.service("ctfd")
    assert service.is_enabled
    assert service.is_running

#def test_socket(host):
#    socket = host.socket("tcp://0.0.0.0:4000")
#    assert socket.is_listening
