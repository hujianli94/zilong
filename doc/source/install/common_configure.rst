2. Edit the ``/etc/zilong/zilong.conf`` file and complete the following
   actions:

   * In the ``[database]`` section, configure database access:

     .. code-block:: ini

        [database]
        ...
        connection = mysql+pymysql://zilong:ZILONG_DBPASS@controller/zilong
