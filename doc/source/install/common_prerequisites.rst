Prerequisites
-------------

Before you install and configure the zilong service,
you must create a database, service credentials, and API endpoints.

#. To create the database, complete these steps:

   * Use the database access client to connect to the database
     server as the ``root`` user:

     .. code-block:: console

        $ mysql -u root -p

   * Create the ``zilong`` database:

     .. code-block:: none

        CREATE DATABASE zilong;

   * Grant proper access to the ``zilong`` database:

     .. code-block:: none

        GRANT ALL PRIVILEGES ON zilong.* TO 'zilong'@'localhost' \
          IDENTIFIED BY 'ZILONG_DBPASS';
        GRANT ALL PRIVILEGES ON zilong.* TO 'zilong'@'%' \
          IDENTIFIED BY 'ZILONG_DBPASS';

     Replace ``ZILONG_DBPASS`` with a suitable password.

   * Exit the database access client.

     .. code-block:: none

        exit;

#. Source the ``admin`` credentials to gain access to
   admin-only CLI commands:

   .. code-block:: console

      $ . admin-openrc

#. To create the service credentials, complete these steps:

   * Create the ``zilong`` user:

     .. code-block:: console

        $ openstack user create --domain default --password-prompt zilong

   * Add the ``admin`` role to the ``zilong`` user:

     .. code-block:: console

        $ openstack role add --project service --user zilong admin

   * Create the zilong service entities:

     .. code-block:: console

        $ openstack service create --name zilong --description "zilong" zilong

#. Create the zilong service API endpoints:

   .. code-block:: console

      $ openstack endpoint create --region RegionOne \
        zilong public http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        zilong internal http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        zilong admin http://controller:XXXX/vY/%\(tenant_id\)s
