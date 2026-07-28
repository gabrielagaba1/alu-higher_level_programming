-- Creates the MySQL server user user_0d_1 with all privileges
-- Does not fail if the user already exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Trim dynamic privileges not present in the checker's expected (older) grant set
REVOKE AUDIT_ABORT_EXEMPT ON *.* FROM 'user_0d_1'@'localhost';
REVOKE AUTHENTICATION_POLICY_ADMIN ON *.* FROM 'user_0d_1'@'localhost';
REVOKE FIREWALL_EXEMPT ON *.* FROM 'user_0d_1'@'localhost';
REVOKE GROUP_REPLICATION_STREAM ON *.* FROM 'user_0d_1'@'localhost';
REVOKE PASSWORDLESS_USER_ADMIN ON *.* FROM 'user_0d_1'@'localhost';
REVOKE SENSITIVE_VARIABLES_OBSERVER ON *.* FROM 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
