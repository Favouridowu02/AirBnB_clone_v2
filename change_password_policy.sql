-- This script is to change the password policy of the roor use  on the localhost to something
-- that complies with the set_up files for the testing and developing

SET GLOBAL validate_password.mixed_case_count=0;
SET GLOBAL validate_password.number_count=0;
SET GLOBAL validate_password.special_char_count=0;
SET GLOBAL validate_password_mixed_case_count=0;
SET GLOBAL validate_password_number_count=0;
SET GLOBAL validate_password_special_char_count=0;

SHOW variables LIKE 'validate_password%';
