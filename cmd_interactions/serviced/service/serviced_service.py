__author__ = 'it'

from connection.ssh_connect import SshConnection


class ServicedService:

    def service_list(self):
        """
        List the services deployed in a Control Center application
        :return service_list JSON:
        """
        service_list = {}

        with SshConnection() as _ssh_conn:
            output = _ssh_conn.run_cmd('serviced service list', 30)[1:]
        for line in output:
            l = filter(None, line.split('\t'))
            service_list[l[0].strip()] = dict(ID=l[1].strip())
        return service_list

    def service_status(self):
        """
        Get service status, ServiceID, Host, DockerID
        :return service_status JSON:
        """
        # self._ssh_conn = SshConnection()
        service_status = {}
        with SshConnection() as _ssh_conn:
            output = _ssh_conn.run_cmd('serviced service list', 30)[1:]
        for line in output:
            l = filter(None, line.split('\t'))
            if 'Running' not in line:
                service_status[l[0].strip()] = dict(ID=l[1].strip(), STATUS=l[2].strip(), HOST='', DOCKERID='')
            else:
                service_status[l[0].strip()] = dict(ID=l[1].strip(), STATUS=l[2].strip(), HOST=l[4].strip(),
                                                    DOCKERID=l[6].strip())

        return service_status

    def service_add(self):
        pass

    def service_remove(self, service):
        with SshConnection() as _ssh_conn:
            output = _ssh_conn.run_cmd('serviced service remove %s' % service)
        if service in output:
            return True
        else:
            return False

    def service_edit(self):
        pass

    def service_assign_ip(self):
        pass

    def service_start(self, service):
        with SshConnection() as _ssh_conn:
            output = _ssh_conn.run_cmd('serviced service add')
        pass

    def service_restart(self):
        pass

    def service_stop(self):
        pass

    def service_proxy(self):
        pass

    def service_shell(self):
        pass

    def service_run(self):
        pass

    def service_attach(self):
        pass

    def service_action(self):
        pass

    def service_logs(self):
        pass

    def service_list_snapshots(self):
        pass

    def service_help(self):
        pass