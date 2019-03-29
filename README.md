# DDclient

Ansible role to install configure
[ddclient](https://sourceforge.net/projects/ddclient/).

## Compatibility

Tested on debian stretch.

## Requirements

None.

## Role Variables

* `ddclient_daemon_period`: Period to check the external IP in seconds.
* `ddclient_enable_syslog`: Enable ddclient syslog, 'yes' or 'no'.
* `ddclient_web`: Web URL to get the external IP.
* `ddclient_protocol`: DDclient protocol. Check
  [ddclient-wiki](https://sourceforge.net/p/ddclient/wiki/protocols/).
* `ddclient_server`: Server to send the updates to, depends on the protocol.
* `ddclient_login`: Your user to login to that server.
* `ddclient_pass`: Your password to login to that server.
* `ddclient_updated_domain`: Domain to update.

**Note**: You should define at least all the variables that don't have a
default value in *defaults/main.yml*.

## Dependencies

None.

## Example Playbook

```yaml
- name: Deploy ddclient
  hosts: all
  roles:
    - role: ddclient
      ddclient_web: dynamicdns.park-your-domain.com/getip
      ddclient_protocol: freedns
      ddclient_server: freedns.afraid.org
      ddclient_login: user
      ddclient_pass: pass
      ddclient_updated_domain: somedomain.mooo.com
```

## Testing

To test the project you need [molecule](http://molecule.readthedocs.io/en/latest/)
.

```bash
molecule test
```

## License

GPLv3

## Author Information

m0wer (at) autistici.org
