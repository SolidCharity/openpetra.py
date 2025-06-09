# this is a generated file.
# do not edit manually, but run: python manage.py createmodel
from django.db import models


class SUser(models.Model):
  """
  List of users
  """

  # This identifies who the current user is
  UserId = models.CharField(max_length=10, null=False, blank=False, unique=True)
  EmailAddress = models.CharField(max_length=50)
  FirstName = models.CharField(max_length=32)
  LastName = models.CharField(max_length=32)
  # Hash value of the user's Salted password
  PasswordHash = models.CharField(max_length=32)
  # The Salt value used for hashing the password (two identical passwords will not yield the same Hash value with different Salt values)
  PasswordSalt = models.CharField(max_length=32)
  # Version Number of the password hashing scheme (source code gives details about what algorithm/parameters combination is used for each number).
  PwdSchemeVersion = models.IntegerField(default=1)
  # Forces change of password at next login. Set when the SYSADMIN changes a password for a user. Also, data migration from legacy system will set this. Further to this it can *optionally* be set if a new password hashing scheme got introduced and the user should be forced to change to it by means of an enforced password change.
  PasswordNeedsChange = models.BooleanField(default=False)
  FailedLogins = models.IntegerField(default=0)
  AccountLocked = models.BooleanField(default=False)
  Retired = models.BooleanField(default=False)
  LastLoginTime = models.IntegerField(default=0)
  # The date the user last logged in.
  LastLoginDate = models.DateTimeField()
  # This is the code used to identify a language.
  LanguageCode = models.CharField(max_length=10, default='99')
  # This defines if the code can be modified
  CanModify = models.BooleanField(default=True)
  RecordDelete = models.BooleanField(default=False)
  # This code identifies the method of aquisition.
  AcquisitionCode = models.CharField(max_length=8)
  # This is used as a key field in most of the accounting system files
  DefaultLedgerNumber = models.IntegerField(default=0)
  # The last time a user failed to log in
  FailedLoginTime = models.IntegerField(default=0)
  # The last date a user failed to log in.
  FailedLoginDate = models.DateTimeField()
  # If the user has a Partner record this is the key to it
  PartnerKey = models.IntegerField()
  # If this token is set and it is still valid, then the user can reset his password using this token
  PasswordResetToken = models.CharField(max_length=32)
  # The date until the password reset token is valid
  PasswordResetValidUntil = models.DateTimeField()


class PLanguage(models.Model):
  """
  List of language codes
  """

  # This is the code used to identify a language.
  Code = models.CharField(max_length=10, null=False, blank=False, unique=True)
  LanguageDescription = models.CharField(max_length=40, null=False, blank=False)
  # This field indicates whether or not the language is one that is 'officially' used at conferences. These are the languages for which translation could be provided.
  CongressLanguage = models.BooleanField(default=False)
  # This defines if the language code can be deleted.
  Deletable = models.BooleanField(default=True)


class AFrequency(models.Model):
  """
  Units of time. Used in partner letters.  Also used to indicate how often a publication is produced or a receipt is sent to a donor.
  """

  Code = models.CharField(max_length=12, null=False, blank=False, unique=True)
  FrequencyDescription = models.CharField(max_length=32, null=False, blank=False)
  NumberOfYears = models.IntegerField(default=0, null=False, blank=False)
  NumberOfMonths = models.IntegerField(default=0)
  NumberOfDays = models.IntegerField(default=0)
  NumberOfHours = models.IntegerField(default=0)
  NumberOfMinutes = models.IntegerField(default=0)


class PInternationalPostalType(models.Model):
  """
  Post office mailing zone classification
  """

  InternatPostalTypeCode = models.CharField(max_length=8, null=False, blank=False, unique=True)
  Description = models.CharField(max_length=32, null=False, blank=False)
  # This defines if the international postal type code can be deleted. <br/>This can only be updated by the system manager. <br/>At the risk of serious operational integrity. <br/>Default to Yes
  Deletable = models.BooleanField(default=True, null=False, blank=False)


class PCountry(models.Model):
  """
  List of countries with their codes
  """

  # This is a code which identifies a country. <br/>It is the ISO code (ISO 3166)
  Code = models.CharField(max_length=4, null=False, blank=False, unique=True)
  # The name of the country
  Name = models.CharField(max_length=40, null=False, blank=False)
  # Describes if the country is politically sensitive.
  Undercover = models.BooleanField(default=False)
  # The telephone code needed to dial into a country
  InternatTelephoneCode = models.IntegerField(default=0)
  InternatPostalType = models.ForeignKey(PInternationalPostalType, related_name="PCountry_InternatPostalType", on_delete=models.CASCADE)
  # The code needed to dial out of a country.
  InternatAccessCode = models.CharField(max_length=4)
  # Number of hours +/- GMT
  TimeZoneMinimum = models.DecimalField(max_digits=6, decimal_places=2, default=0)
  # Number of hours +/- GMT
  TimeZoneMaximum = models.DecimalField(max_digits=6, decimal_places=2, default=0)
  # This defines if the country code can be deleted. <br/>This can only be updated by the system manager. <br/>At the risk of serious operational integrity. <br/>Default to Yes
  Deletable = models.BooleanField(default=True, null=False, blank=False)
  # Tab order of the city, county, and post code fields on the Partner Edit screen
  AddressOrder = models.IntegerField(default=0)
  # The name of the country in the Local language
  CountryNameLocal = models.CharField(max_length=40)


class ACurrency(models.Model):
  """
  Unit of money for various countries.
  """

  # This defines which currency is being used
  Code = models.CharField(max_length=8, null=False, blank=False, unique=True)
  # This is the name of the currency
  Name = models.CharField(max_length=32, null=False, blank=False)
  # This is the symbol used to show a currency. Eg $US or £
  CurrencySymbol = models.CharField(max_length=4, null=False, blank=False)
  # Country code
  Country = models.ForeignKey(PCountry, null=False, blank=False, related_name="ACurrency_Country", on_delete=models.CASCADE)
  # The format in which to display and accept input on a currency (decimal values)
  DisplayFormat = models.CharField(max_length=20, default='->>>,>>>,>>>,>>9.99', null=False, blank=False)
  # Indicates whether currency is part of the european exchange rate mechanism/ European Monetary Union
  InEmu = models.BooleanField(default=False, null=False, blank=False)


class SSession(models.Model):
  """
  Sessions
  """

  # This is the identifier of the session
  SessionId = models.CharField(max_length=64, null=False, blank=False, unique=True)
  # This session is valid till this point in time
  ValidUntil = models.DateTimeField(null=False, blank=False)
  # JSON encoded list of session values.
  SessionValues = models.CharField(max_length=20)
  # This is the system user id. Each user of the system is allocated one
  UserId = models.CharField(max_length=10)


class SReportResult(models.Model):
  """
  Report Results
  """

  # This is the identifier of the report result
  ReportId = models.CharField(max_length=96, null=False, blank=False, unique=True)
  # This is the identifier of the session
  SessionId = models.CharField(max_length=64, null=False, blank=False)
  # This session is valid till this point in time
  ValidUntil = models.DateTimeField(null=False, blank=False)
  # Parameters list in json
  ParameterList = models.CharField(max_length=20)
  # result represented in HTML
  # Did the report finish successfully to be calculated?
  Success = models.BooleanField(default=False)
  # in case of failure, this contains the error message
  ErrorMessage = models.CharField(max_length=20)


class SUserAccountActivity(models.Model):
  """
  Logs activity on user accounts themselves (user logins and logouts are recorded in s_login)
  """

  # User for which the user account activity got recorded.
  UserId = models.CharField(max_length=10, null=False, blank=False)
  # Date of the recorded user account activity.
  ActivityDate = models.DateTimeField(null=False, blank=False)
  # Time of the recorded user account activity.
  ActivityTime = models.IntegerField(default=0, null=False, blank=False)
  # Type of the recorded account activity. This is a hard-coded constant value (there's no 'lookup table' for it); for available values and their meaning please check program code (TUserAccountActivityLog Class).
  ActivityType = models.CharField(max_length=25, null=False, blank=False)
  # Details/description of the recorded account activity. This is a localised string, i.e. it can be recorded in the language of the Site! Refer to s_activity_type_c for exact identification of what the recorded account activity is about if text in here can't be understood because it is recorded in a foreign language.
  ActivityDetails = models.CharField(max_length=500)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_user_account_activity_pk', fields=['UserId', 'ActivityDate', 'ActivityTime', 'ActivityType']),
    ]

class SForm(models.Model):
  """
  List of forms for printers
  """

  # This identifies the form
  Name = models.CharField(max_length=10, null=False, blank=False, unique=True)
  # This is a description of the form
  FormDescription = models.CharField(max_length=40, null=False, blank=False)
  DefaultFont = models.CharField(max_length=32)
  # Default font size (points)
  DefaultFontSize = models.IntegerField(default=0, null=False, blank=False)
  # Number of lines per unit of measure
  DefaultLpi = models.IntegerField(default=0, null=False, blank=False)
  # Number of characters per unit of measure
  DefaultCpi = models.IntegerField(default=0, null=False, blank=False)
  # Height of the page
  FormLength = models.DecimalField(max_digits=6, decimal_places=3, default=0, null=False, blank=False)
  # Width of the page
  FormWidth = models.DecimalField(max_digits=6, decimal_places=3, default=0, null=False, blank=False)
  FormOrientation = models.CharField(max_length=20, default='P')
  # Unit of measure for the form.  True if inches, false if centimeters.
  UnitOfMeasure = models.BooleanField()
  # Top margin
  TopMargin = models.DecimalField(max_digits=6, decimal_places=3, default=0)
  # Bottom margin
  BottomMargin = models.DecimalField(max_digits=6, decimal_places=3, default=0)
  # Left margin
  LeftMargin = models.DecimalField(max_digits=6, decimal_places=3, default=0)
  # Right margin
  RightMargin = models.DecimalField(max_digits=6, decimal_places=3, default=0)


class SGroup(models.Model):
  """
  List of groups to which users can belong
  """

  # identifies a system group
  GroupId = models.CharField(max_length=10, null=False, blank=False)
  # Field that the group belongs to
  UnitKey = models.IntegerField(default=0, null=False, blank=False)
  # Describes a group
  Name = models.CharField(max_length=50)
  # This defines if the code can be modified
  CanModify = models.BooleanField(default=True)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_group_pk', fields=['GroupId', 'UnitKey']),
    ]

class SUserGroup(models.Model):
  """
  Security mappings of users to groups
  """

  # This is the system user id. Each user of the system is allocated one
  User = models.ForeignKey(SUser, null=False, blank=False, related_name="SUserGroup_User", on_delete=models.CASCADE)
  Group = models.ForeignKey(SGroup, null=False, blank=False, related_name="SUserGroup_Group", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_user_group_pk', fields=['User', 'Group']),
    ]

class SModule(models.Model):
  """
  List of Petra software modules
  """

  # Identifies a module. A module is any part of aprogram which is related to each menu entry or to the sub-system. Eg, partner administration, AP, AR etc.
  ModuleId = models.CharField(max_length=10, null=False, blank=False, unique=True)
  # This is the name of the module
  Name = models.CharField(max_length=32)


class SValidOutputForm(models.Model):
  """
  Lists printer forms that are valid for each Petra module.
  """

  Module = models.ForeignKey(SModule, null=False, blank=False, related_name="SValidOutputForm_Module", on_delete=models.CASCADE)
  Form = models.ForeignKey(SForm, null=False, blank=False, related_name="SValidOutputForm_Form", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_valid_output_form_pk', fields=['Module', 'Form']),
    ]

class SGroupModuleAccessPermission(models.Model):
  """
  Security mappings from groups to Petra modules
  """

  Group = models.ForeignKey(SGroup, null=False, blank=False, related_name="SGroupModuleAccessPermission_Group", on_delete=models.CASCADE)
  Module = models.ForeignKey(SModule, null=False, blank=False, related_name="SGroupModuleAccessPermission_Module", on_delete=models.CASCADE)
  # Permission to access this module
  CanAccess = models.BooleanField(default=True)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_group_module_acc_perm_pk', fields=['Group', 'Module']),
    ]

class SGroupTableAccessPermission(models.Model):
  """
  Security mappings from groups to Petra database
  """

  Group = models.ForeignKey(SGroup, null=False, blank=False, related_name="SGroupTableAccessPermission_Group", on_delete=models.CASCADE)
  TableName = models.CharField(max_length=32, null=False, blank=False)
  # Permission to allow creation.
  CanCreate = models.BooleanField(default=True)
  # Permission to allow modification.
  CanModify = models.BooleanField(default=True)
  # Permission to allow deletion.
  CanDelete = models.BooleanField(default=True)
  # Permission to allow inquiry.
  CanInquire = models.BooleanField(default=True)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_group_table_acc_perm_pk', fields=['Group', 'TableName']),
    ]

class SModuleTableAccessPermission(models.Model):
  """
  Security mappings from modules to Petra database
  """

  Module = models.ForeignKey(SModule, null=False, blank=False, related_name="SModuleTableAccessPermission_Module", on_delete=models.CASCADE)
  TableName = models.CharField(max_length=32, null=False, blank=False)
  # Permission to allow creation.
  CanCreate = models.BooleanField(default=True)
  # Permission to allow modification.
  CanModify = models.BooleanField(default=True)
  # Permission to allow deletion.
  CanDelete = models.BooleanField(default=True)
  # Permission to allow inquiry.
  CanInquire = models.BooleanField(default=True)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_module_table_acc_perm_pk', fields=['Module', 'TableName']),
    ]

class SUserModuleAccessPermission(models.Model):
  """
  Security mappings of users to Petra modules
  """

  # This is the system user id. Each user of the system is allocated one
  User = models.ForeignKey(SUser, null=False, blank=False, related_name="SUserModuleAccessPermission_User", on_delete=models.CASCADE)
  Module = models.ForeignKey(SModule, null=False, blank=False, related_name="SUserModuleAccessPermission_Module", on_delete=models.CASCADE)
  # Permission to access this module
  CanAccess = models.BooleanField(default=True)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_user_module_acc_perm_pk', fields=['User', 'Module']),
    ]

class SUserTableAccessPermission(models.Model):
  """
  Security mappings of users to Petra database
  """

  # This is the system user id. Each user of the system is allocated one
  User = models.ForeignKey(SUser, null=False, blank=False, related_name="SUserTableAccessPermission_User", on_delete=models.CASCADE)
  TableName = models.CharField(max_length=32, null=False, blank=False)
  # Permission to allow creation.
  CanCreate = models.BooleanField(default=True)
  # Permission to allow modification.
  CanModify = models.BooleanField(default=True)
  # Permission to allow deletion.
  CanDelete = models.BooleanField(default=True)
  # Permission to allow inquiry.
  CanInquire = models.BooleanField(default=True)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_user_table_acc_perm_pk', fields=['User', 'TableName']),
    ]

class SLanguageSpecific(models.Model):
  """
  Definitions of fields that are language specific.
  """

  # This is the code used to identify a language.
  Language = models.ForeignKey(PLanguage, null=False, blank=False, related_name="SLanguageSpecific_Language", on_delete=models.CASCADE)
  # The language specific month name 1.
  MonthNameC = models.CharField(max_length=20, null=False, blank=False)
  # The language specific month name 2.
  MonthNameC = models.CharField(max_length=20, null=False, blank=False)
  # The language specific month name 3.
  MonthNameC = models.CharField(max_length=20, null=False, blank=False)
  # The language specific month name 4.
  MonthNameC = models.CharField(max_length=20, null=False, blank=False)
  # The language specific month name 5.
  MonthNameC = models.CharField(max_length=20, null=False, blank=False)
  # The language specific month name 6.
  MonthNameC = models.CharField(max_length=20, null=False, blank=False)
  # The language specific month name 7.
  MonthNameC = models.CharField(max_length=20, null=False, blank=False)
  # The language specific month name 8.
  MonthNameC = models.CharField(max_length=20, null=False, blank=False)
  # The language specific month name 9.
  MonthNameC = models.CharField(max_length=20, null=False, blank=False)
  # The language specific month name 10.
  MonthNameC = models.CharField(max_length=20, null=False, blank=False)
  # The language specific month name 11.
  MonthNameC = models.CharField(max_length=20, null=False, blank=False)
  # The language specific month name 12.
  MonthNameC = models.CharField(max_length=20, null=False, blank=False)
  # The language specific short month name 1.
  MonthNameShortC = models.CharField(max_length=3, null=False, blank=False)
  # The language specific short month name 2.
  MonthNameShortC = models.CharField(max_length=3, null=False, blank=False)
  # The language specific short month name 3.
  MonthNameShortC = models.CharField(max_length=3, null=False, blank=False)
  # The language specific short month name 4.
  MonthNameShortC = models.CharField(max_length=3, null=False, blank=False)
  # The language specific short month name 5.
  MonthNameShortC = models.CharField(max_length=3, null=False, blank=False)
  # The language specific short month name 6.
  MonthNameShortC = models.CharField(max_length=3, null=False, blank=False)
  # The language specific short month name 7.
  MonthNameShortC = models.CharField(max_length=3, null=False, blank=False)
  # The language specific short month name 8.
  MonthNameShortC = models.CharField(max_length=3, null=False, blank=False)
  # The language specific short month name 9.
  MonthNameShortC = models.CharField(max_length=3, null=False, blank=False)
  # The language specific short month name 10.
  MonthNameShortC = models.CharField(max_length=3, null=False, blank=False)
  # The language specific short month name 11.
  MonthNameShortC = models.CharField(max_length=3, null=False, blank=False)
  # The language specific short month name 12.
  MonthNameShortC = models.CharField(max_length=3, null=False, blank=False)


class SLogin(models.Model):
  """
  Log of all the log-ins/log-in attempts to the system, and of log-outs from the system (activities on user accounts themselves are recorded in s_user_account_activity).
  """

  # OpenPetra process ID; this is a unique key
  LoginProcessId = models.IntegerField(null=False, blank=False, unique=True)
  # This is the system user id. Each user of the system is allocated one.
  UserId = models.CharField(max_length=10, null=False, blank=False)
  # Time of the login/login attempt/logout.
  Time = models.IntegerField(default=0, null=False, blank=False)
  # Date of the login/login attempt/logout.
  Date = models.DateTimeField(null=False, blank=False)
  # Type of the login/logout record. This is a hard-coded constant value (there's no 'lookup table' for it); for available values and their meaning please check program code (TLoginLog Class).
  LoginType = models.CharField(max_length=25, null=False, blank=False)
  # Details/description of the login/login attempt/logout. This is a localised string, i.e. it can be recorded in the language of the Site! Refer to s_login_type_c for exact identification of what the recorded account activity is about if text in here can't be understood because it is recorded in a foreign language.
  LoginDetails = models.CharField(max_length=250)
  # Reference to s_login_process_id_r (OpenPetra process ID of the login record) - only set for a record of s_login_status_type_c 'LOGOUT' (connects the logout log entry with the corresponding login log entry.)
  LoginProcessIdRef = models.IntegerField()


class SLogonMessage(models.Model):
  """
  List of logon messages by language
  """

  # This is the code used to identify a language.
  Language = models.ForeignKey(PLanguage, null=False, blank=False, related_name="SLogonMessage_Language", on_delete=models.CASCADE)
  # Message displayed when a user logs onto to the system
  LogonMessage = models.CharField(max_length=150)


class SPatchLog(models.Model):
  """
  Logs each patch procedure that is run
  """

  PatchName = models.CharField(max_length=12, null=False, blank=False, unique=True)
  # The user who ran the patch
  User = models.ForeignKey(SUser, related_name="SPatchLog_User", on_delete=models.CASCADE)
  # The date the patch was run.
  DateRun = models.DateTimeField(null=False, blank=False)


class SReportTemplate(models.Model):
  """
  filesystem for storage of XML report templates - those provided initially and also tweaks saved by users.
  """

  # Template Id
  TemplateId = models.IntegerField(null=False, blank=False, unique=True)
  # Report Type
  ReportType = models.CharField(max_length=50, null=False, blank=False)
  # Report Title
  ReportVariant = models.CharField(max_length=50, null=False, blank=False)
  # Tempate author
  Author = models.CharField(max_length=50, null=False, blank=False)
  # Template will be selected by default
  Default = models.BooleanField(default=False, null=False, blank=False)
  # Template only available to me
  Private = models.BooleanField(default=False, null=False, blank=False)
  # Private template will be selected over public default
  PrivateDefault = models.BooleanField(default=False, null=False, blank=False)
  # Template cannot be modified
  Readonly = models.BooleanField(default=False, null=False, blank=False)
  # Compressed XML text
  XmlText = models.CharField(max_length=20, null=False, blank=False)


class SReportsToArchive(models.Model):
  """
  Contains the titles of reports that should be archived, not deleted, when Purge Reports is run.
  """

  # Title of the Report
  ReportTitle = models.CharField(max_length=50, null=False, blank=False, unique=True)


class SSystemStatus(models.Model):
  """
  Records current status of system (up, maintenance etc.)
  """

  # This is the system user id. Each user of the system is allocated one
  User = models.ForeignKey(SUser, null=False, blank=False, related_name="SSystemStatus_User", on_delete=models.CASCADE)
  SystemDisabledDate = models.DateTimeField()
  SystemDisabledTime = models.IntegerField(default=0)
  SystemDisabledReason = models.CharField(max_length=80)
  SystemAvailableDate = models.DateTimeField()
  SystemAvailableTime = models.IntegerField(default=0)
  # The log in status of the system.
  SystemLoginStatus = models.BooleanField(default=False)


class SUserDefaults(models.Model):
  """
  Stores various default values and options for each user.
  """

  # This identifies who the current user is
  User = models.ForeignKey(SUser, null=False, blank=False, related_name="SUserDefaults_User", on_delete=models.CASCADE)
  # The name of the default
  DefaultCode = models.CharField(max_length=50, null=False, blank=False)
  # The value of the default
  DefaultValue = models.CharField(max_length=250)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_user_defaults_pk', fields=['User', 'DefaultCode']),
    ]

class SSystemDefaults(models.Model):
  """
  The settings that are system wide (iso per user)
  """

  DefaultCode = models.CharField(max_length=50, null=False, blank=False, unique=True)
  # Default Code in easy to read format
  DefaultCodeLocal = models.CharField(max_length=50)
  # Default Code in easy to read format in English
  DefaultCodeIntl = models.CharField(max_length=50)
  # Description of what this code does
  DefaultDescription = models.CharField(max_length=250)
  # Category of code (e.g. Partner, Gift)
  Category = models.CharField(max_length=50)
  DefaultValue = models.CharField(max_length=250)
  # Determines if the value can be edited in the GUI
  ReadOnly = models.BooleanField(default=True, null=False, blank=False)


class SSystemDefaultsGui(models.Model):
  """
  Describes the GUI controls for editing the default values
  """

  Default = models.ForeignKey(SSystemDefaults, null=False, blank=False, related_name="SSystemDefaultsGui_Default", on_delete=models.CASCADE)
  # An ID for the control array that determines the display order
  ControlId = models.IntegerField(null=False, blank=False)
  # Label to display
  ControlLabel = models.CharField(max_length=50, null=False, blank=False)
  # Type of control (e.g. txt, cmb, dtp)
  ControlType = models.CharField(max_length=10, null=False, blank=False)
  # Optional values that apply to a control of type cmb
  ControlOptionalValues = models.CharField(max_length=100)
  # List of comma separated additional control attributes, e.g. Width, Type etc.
  ControlAttributes = models.CharField(max_length=250)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_system_defaults_gui_pk', fields=['Default', 'ControlId']),
    ]

class SErrorLog(models.Model):
  """
  Log of captured runtime errors
  """

  ErrorCode = models.CharField(max_length=20, null=False, blank=False)
  # This is the system user id. Each user of the system is allocated one
  User = models.ForeignKey(SUser, null=False, blank=False, related_name="SErrorLog_User", on_delete=models.CASCADE)
  Date = models.DateTimeField(null=False, blank=False)
  Time = models.IntegerField(default=0, null=False, blank=False)
  # This is the software release number
  ReleaseNumber = models.CharField(max_length=12, null=False, blank=False)
  FileName = models.CharField(max_length=40, null=False, blank=False)
  ProcessId = models.CharField(max_length=8)
  MessageLine1 = models.CharField(max_length=60, null=False, blank=False)
  MessageLine2 = models.CharField(max_length=40)
  MessageLine3 = models.CharField(max_length=40)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_error_log_pk', fields=['ErrorCode', 'User', 'Date', 'Time']),
    ]

class PPartnerStatus(models.Model):
  """
  List of statuses for partners
  """

  # This code describes the status of a partner. <br/>Eg,  Active, Deceased etc
  StatusCode = models.CharField(max_length=8, null=False, blank=False, unique=True)
  PartnerStatusDescription = models.CharField(max_length=60, null=False, blank=False)
  # If set to yes, then Partners with this status are considered as active Partners
  PartnerIsActive = models.BooleanField(default=True)
  IncludePartnerOnReport = models.BooleanField(default=False)
  # This defines if the partner status code can be deleted. <br/>This can only be updated by the system manager. <br/>At the risk of serious operational integrity. <br/>Default to Yes
  Deletable = models.BooleanField(default=True, null=False, blank=False)


class PAcquisition(models.Model):
  """
  This table is used to describe how a partner first came into contact with the organisation.  Which department entered them.
  """

  # This code identifies the method of aquisition.
  Code = models.CharField(max_length=8, null=False, blank=False, unique=True)
  # This describes the method of aquisition.
  AcquisitionDescription = models.CharField(max_length=80, null=False, blank=False)
  # Defines if the acquisition code is still for use
  ValidAcquisition = models.BooleanField(default=True)
  # This defines if the acquisition code can be deleted. <br/>This can only be updated by the system manager. <br/>At the risk of serious operational integrity. <br/>Default to Yes
  Deletable = models.BooleanField(default=True, null=False, blank=False)
  # This defines if the acquisition code listed represents a recruiting effort.
  RecruitingEffort = models.BooleanField(default=False)


class PAddresseeType(models.Model):
  """
  Ex. Fam - Family, SM - Single Male, etc.
  """

  Code = models.CharField(max_length=12, null=False, blank=False, unique=True)
  Description = models.CharField(max_length=32, null=False, blank=False)
  # This defines if the addressee type code can be deleted. <br/>This can only be updated by the system manager. <br/>At the risk of serious operational integrity. <br/>Default to Yes
  Deletable = models.BooleanField(default=True, null=False, blank=False)


class PTitle(models.Model):
  """
  Titles available for use
  """

  # Title
  Title = models.CharField(max_length=32, null=False, blank=False, unique=True)
  # Default addressee type code to be used for this title
  DefaultAddresseeType = models.ForeignKey(PAddresseeType, related_name="PTitle_DefaultAddresseeType", on_delete=models.CASCADE)
  # This defines if the title is a common one to be used more often in this system
  CommonTitle = models.BooleanField(default=True)


class PPartnerClasses(models.Model):
  """
  The class a partner is (PERSON, UNIT, etc.
  """

  PartnerClass = models.CharField(max_length=12, null=False, blank=False, unique=True)
  Description = models.CharField(max_length=50)


class PLocation(models.Model):
  """
  Address and other data related to that address.
  """

  # This is the key that tell what site created this location, it will help to merge addresses when doing imports
  SiteKey = models.IntegerField(default=0, null=False, blank=False)
  LocationKey = models.IntegerField(default=0, null=False, blank=False)
  # The name of the building
  Building1 = models.CharField(max_length=50)
  # The name of the building (continued)
  Building2 = models.CharField(max_length=50)
  # The name of the street that the house is located on
  StreetName = models.CharField(max_length=50)
  # This is the first element of an address
  Locality = models.CharField(max_length=50)
  # The name of the suburb
  Suburb = models.CharField(max_length=50)
  # This can be a post town or city
  City = models.CharField(max_length=32)
  # This can be a county (UK), a state (US), province (CDN), canton (CH) etc.
  County = models.CharField(max_length=32)
  # This is the national post code
  PostalCode = models.CharField(max_length=20)
  # This is a code which identifies a country. <br/>It is taken from the ISO 3166-1-alpha-2 code elements.
  Country = models.ForeignKey(PCountry, related_name="PLocation_Country", on_delete=models.CASCADE)
  # This is the third element of an address (if required)
  Address3 = models.CharField(max_length=50)
  # The latitude of the location; a number between -90 and +90; precision is 6 digits (11cm)
  GeoLatitude = models.DecimalField(max_digits=9, decimal_places=6)
  # The longitude of the location; a number between -180 and +180; precision is 6 digits (11cm)
  GeoLongitude = models.DecimalField(max_digits=9, decimal_places=6)
  # The distance in km of this location to the location 0 if location 0 was on the same longitude; this is for improving query performance
  GeoKmX = models.IntegerField()
  # The distance in km of this location to the location 0 if location 0 was on the same latitude; this is for improving query performance
  GeoKmY = models.IntegerField()
  # The accuracy of the stored geo data;                 -2: server did not respond;                 -1: not processed yet;                 0: Unknown Location;                 1: Country level accuracy;                 2: Region;                 3: Sub-Region;                 4: Town/City/Village;                 5: Post code;                 6: Street;                 7: Intersection;                 8: Address level accuracy
  GeoAccuracy = models.IntegerField(default=-1)
  # Indicates whether or not the location has restricted access. If it does then the access will be controlled by s_group_location.
  Restricted = models.BooleanField(default=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_location_pk', fields=['SiteKey', 'LocationKey']),
    ]

class PLocationType(models.Model):
  """
  Types of address e.g. home, business
  """

  Code = models.CharField(max_length=10, null=False, blank=False, unique=True)
  Description = models.CharField(max_length=30, null=False, blank=False)
  Deletable = models.BooleanField(default=True, null=False, blank=False)
  Assignable = models.BooleanField(default=True, null=False, blank=False)


class PPartnerAttributeCategory(models.Model):
  """
  Holds categories that categorise Partner Attributes Types, thus allowing logical grouping of the latter (e.g. to have all Partner Attributes Types that are to do with phone numbers in one category).
  """

  # Code for Partner Attribute Category. Use plural words/phrases (e.g. 'Phone Numbers' and not 'Phone Number')
  CategoryCode = models.CharField(max_length=30, null=False, blank=False, unique=True)
  # Description for Partner Attribute Category.
  CategoryDesc = models.CharField(max_length=100, null=False, blank=False)
  # Allows for manual ordering of Partner Attribute Categories by the user (e.g. list Partner Attribute Types for 'phone numbers' first, then list all for 'mobile numbers').
  Index = models.IntegerField(default=0, null=False, blank=False)
  # Flag to indicate whether Partner Attribute Types that are linked to this Partner Attribute Category are 'Partner Contact Detail' Attributes or not.
  PartnerContactCategory = models.BooleanField(null=False, blank=False)
  # Flag to indicate whether this Partner Attribute Category is one that is internally used by OpenPetra. Records that have this Flag set will be hidden from the user altogether (and so will p_partner_attribute records that are linked to such a Category through a p_partner_attribute_type!!!).
  SystemCategory = models.BooleanField(default=False, null=False, blank=False)
  # Flag to indicate whether this Partner Attribute Category is deletable by a user or not. Should be set to be true for records where p_system_category_l is true.
  Deletable = models.BooleanField(default=False, null=False, blank=False)


class PPartnerAttributeType(models.Model):
  """
  Holds various Partner Attribute Types.
  """

  # Attribute Type. This can be anything really: Phone Number, Mobile Number, Email Address, etc (not limited to Partner Contact Details, though). Use singular words/phrases (e.g. 'Phone Number' and not 'Phone Numbers').
  AttributeType = models.CharField(max_length=30, null=False, blank=False, unique=True)
  # Category of the Partner Attribute Type.
  Category = models.ForeignKey(PPartnerAttributeCategory, null=False, blank=False, related_name="PPartnerAttributeType_Category", on_delete=models.CASCADE)
  # Description of what this Partner Attribute Type is all about.
  Description = models.CharField(max_length=50, null=False, blank=False)
  # Allows for manual ordering of Partner Attribute Types by the user (e.g. to list all Partner Attributes that have a Partner Attribute Type of 'phone number' *grouped together* first, then list all that have a Partner Attribute Type of 'assistant phone number' *grouped together*).
  Index = models.IntegerField(default=0, null=False, blank=False)
  # Describes the kind (type) of Value that the Partner Attributes that are linked to this Partner Attribute Type are. Valid values for Contact Detail Attributes: 'CONTACTDETAIL_GENERAL', 'CONTACTDETAIL_HYPERLINK', 'CONTACTDETAIL_HYPERLINK_WITHVALUE', 'CONTACTDETAIL_EMAILADDRESS', 'CONTACTDETAIL_SKYPEID'.
  AttributeTypeValueKind = models.CharField(max_length=40, null=False, blank=False)
  # For use with p_attribute_type_value_kind_c 'CONTACTDETAIL_HYPERLINK_WITHVALUE' only. Specifies how to 'construct' a hyperlink where the Value of a Partner Attribute is part of the URL.
  HyperlinkFormat = models.CharField(max_length=60)
  # Label that should be displayed/printed instead of p_code_c if a Partner Attribute's 'specialised' Flag is set.
  SpecialLabel = models.CharField(max_length=50)
  # Can this Partner Attribute Type be assigned?
  Unassignable = models.BooleanField(default=False, null=False, blank=False)
  # This is the date where the record was set to unassignable.
  UnassignableDate = models.DateTimeField()
  # Flag to indicate whether this Partner Attribute Type is deletable by a user or not.
  Deletable = models.BooleanField(default=False, null=False, blank=False)


class UUnitType(models.Model):
  """
  General information about the unit such as unit type and entry conference. 
  """

  Code = models.CharField(max_length=12, null=False, blank=False, unique=True)
  Name = models.CharField(max_length=32, null=False, blank=False)
  # This defines if the type code can be deleted. <br/>This can only be updated by the system manager.
  TypeDeletable = models.BooleanField(default=False, null=False, blank=False)


class PtMaritalStatus(models.Model):
  """
  This table contains the codes indicating someones marital status.
  """

  # This code indicates the different marital statuses.
  Code = models.CharField(max_length=1, null=False, blank=False, unique=True)
  # This describes the marital statuses.
  Description = models.CharField(max_length=40, null=False, blank=False)
  # Indicates if this code can still be assigned?
  Assignable = models.BooleanField(default=True, null=False, blank=False)
  # Date from which this code was made unassignable.
  AssignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True, null=False, blank=False)


class POccupation(models.Model):
  """
  List of occupations with codes
  """

  Code = models.CharField(max_length=16, default='UNKNOWN', null=False, blank=False, unique=True)
  OccupationDescription = models.CharField(max_length=40, null=False, blank=False)
  ValidOccupation = models.BooleanField(default=True)
  # This defines if the occupation code can be deleted. <br/>This can only be updated by the system manager. <br/>At the risk of serious operational integrity. <br/>Default to Yes
  Deletable = models.BooleanField(default=True, null=False, blank=False)


class PDenomination(models.Model):
  """
  List of denomination codes for churches
  """

  Code = models.CharField(max_length=8, null=False, blank=False, unique=True)
  Name = models.CharField(max_length=40, null=False, blank=False)
  # Defines if a denomination is still valid for use
  ValidDenomination = models.BooleanField(default=True, null=False, blank=False)
  # This defines if the denomination code can be deleted. <br/>This can only be updated by the system manager. <br/>At the risk of serious operational integrity. <br/>Default to Yes
  Deletable = models.BooleanField(default=True, null=False, blank=False)


class PBusiness(models.Model):
  """
  List of businesses with codes
  """

  Code = models.CharField(max_length=8, null=False, blank=False, unique=True)
  BusinessDescription = models.CharField(max_length=40, null=False, blank=False)
  # This defines if the business code can be deleted. <br/>This can only be updated by the system manager. <br/>At the risk of serious operational integrity. <br/>Default to Yes
  Deletable = models.BooleanField(default=True, null=False, blank=False)


class PBankingType(models.Model):
  """
  Tells of what type this banking-detail is (bank-account, visa, mastercard, etc.
  """

  # Human readable form of this type
  Type = models.CharField(max_length=12, null=False, blank=False, unique=True)
  # What it means
  Description = models.CharField(max_length=25)
  # A procedure to check the fields...
  Check = models.CharField(max_length=25)


class PBankingDetailsUsageType(models.Model):
  """
  Usage type information for Banking Details.
  """

  # This identifies the usage type.
  Type = models.CharField(max_length=16, null=False, blank=False, unique=True)
  # This describes the usage type.
  TypeDescription = models.CharField(max_length=60, null=False, blank=False)
  # Can this usage type be assigned?
  Unassignable = models.BooleanField(default=False, null=False, blank=False)
  # This is the date where the record was set to unassignable.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True, null=False, blank=False)


class PTypeCategory(models.Model):
  """
  This table contains the codes that indicate the categories of partner (special) types
  """

  # This code indicates the category of a type.
  Code = models.CharField(max_length=20, null=False, blank=False, unique=True)
  # This describes the type category.
  Description = models.CharField(max_length=50)
  # Indicates if this code can still be assigned?
  Unassignable = models.BooleanField(default=False)
  # Date from which this code was made unassignable.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PType(models.Model):
  """
  List of all possible special types for a partner.
  """

  # This code identifies the type
  Code = models.CharField(max_length=10, null=False, blank=False, unique=True)
  # This describes the method of aquisition.
  TypeDescription = models.CharField(max_length=60, null=False, blank=False)
  # This is a category, by which partner types can be grouped.
  Category = models.ForeignKey(PTypeCategory, related_name="PType_Category", on_delete=models.CASCADE)
  # Defines if the type code is still for use
  ValidType = models.BooleanField(default=True)
  # This type can only be assigned by the system
  SystemType = models.BooleanField(default=False)
  # This defines if the type code can be deleted. <br/>This can only be updated by the system manager.
  TypeDeletable = models.BooleanField(default=True)
  # This Mot Group will be selected by default when entering gifts for Partners with this Special Type
  TypeMotivationGroup = models.CharField(max_length=8)
  # This Mot Detail will be selected by default when entering gifts for Partners with this Special Type
  TypeMotivationDetail = models.CharField(max_length=8)


class PRelationCategory(models.Model):
  """
  This table contains the codes that indicate the categories of relations (grouping). 
  """

  # This code indicates the category of a relation.
  Code = models.CharField(max_length=20, null=False, blank=False, unique=True)
  # This describes the relation category.
  Description = models.CharField(max_length=50)
  # Indicates if this code can still be assigned?
  Unassignable = models.BooleanField(default=False)
  # Date from which this code was made unassignable.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PRelation(models.Model):
  """
  List of relationships between partners.  Relations occur in one direction only.   The relation code is used in the p_partner_relationship record. 
  """

  # This code identifies the relation
  Name = models.CharField(max_length=10, null=False, blank=False, unique=True)
  # This describes the relation.
  RelationDescription = models.CharField(max_length=50, null=False, blank=False)
  # This is a category, by which relations can be grouped.
  RelationCategory = models.ForeignKey(PRelationCategory, related_name="PRelation_RelationCategory", on_delete=models.CASCADE)
  # This defines if the relation name can be deleted. <br/>This can only be updated by the system manager. <br/>It default to Yes.
  Deletable = models.BooleanField(default=True, null=False, blank=False)
  # This describes the relation in the reverse direction, eg Husband and Wife.
  ReciprocalDescription = models.CharField(max_length=50, null=False, blank=False)
  # Determines whether the record is still assignable
  ValidRelation = models.BooleanField(default=True)


class MExtractType(models.Model):
  """
  Contains a list of extract type which is needed when extracts need to be rerun
  """

  # Extract Type Code
  Code = models.CharField(max_length=25, null=False, blank=False, unique=True)
  # Function that is run to create the extract (4GL function, Delphi, etc.)
  Function = models.CharField(max_length=250)
  # Description of Extract Type
  Description = models.CharField(max_length=100)


class MExtractMaster(models.Model):
  """
  Master file for extracts.  Contains names for the extract id
  """

  # Identifier for the extract
  ExtractId = models.IntegerField(default=0, null=False, blank=False, unique=True)
  # Short name for the extract to be used in filenames
  ExtractName = models.CharField(max_length=25, null=False, blank=False)
  # This is a long description for the extract
  ExtractDesc = models.CharField(max_length=80)
  LastRef = models.DateTimeField()
  Deletable = models.BooleanField(default=True, null=False, blank=False)
  # The user can set the frozen field when the extract should not be updated.
  Frozen = models.BooleanField(default=False, null=False, blank=False)
  KeyCount = models.IntegerField(default=0)
  Public = models.BooleanField(default=True, null=False, blank=False)
  # Indicates that the extract has been edited by a user
  ManualMod = models.BooleanField(default=False, null=False, blank=False)
  # Date the extract was manually modified
  ManualMod = models.DateTimeField()
  # Who made the last manual modification ?
  ManualModBy = models.ForeignKey(SUser, related_name="MExtractMaster_ManualModBy", on_delete=models.CASCADE)
  # Indicate the extract type. Which function was the extract created through?
  ExtractType = models.ForeignKey(MExtractType, related_name="MExtractMaster_ExtractType", on_delete=models.CASCADE)
  # Is this extract just a template that has not yet been run?
  Template = models.BooleanField(default=False)
  # Indicates whether or not the extract has restricted access. If it does then the access will be controlled by s_group_extract
  Restricted = models.BooleanField(default=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='m_extract_master_uk', fields=['ExtractName']),
    ]

class MExtractParameter(models.Model):
  """
  Contains a list of parameters that an extract was run with (so it can be rerun)
  """

  # Identifier for the extract
  Extract = models.ForeignKey(MExtractMaster, null=False, blank=False, related_name="MExtractParameter_Extract", on_delete=models.CASCADE)
  # Extract Parameter Code
  ParameterCode = models.CharField(max_length=25, null=False, blank=False)
  # Index for Parameter Value. Only relevant if a parameter is a list of values in which case a new index is used for each list item.
  ValueIndex = models.IntegerField(default=0, null=False, blank=False)
  # Extract Parameter Value
  ParameterValue = models.CharField(max_length=100)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='m_extract_parameter_pk', fields=['Extract', 'ParameterCode', 'ValueIndex']),
    ]

class PMailing(models.Model):
  """
  Lists mailings that are being tracked.   When entering gifts, the mailing that motivated the gift can be indicated.
  """

  # Mailing Code
  Code = models.CharField(max_length=25, null=False, blank=False, unique=True)
  # Mailing Description
  MailingDescription = models.CharField(max_length=80)
  # Date Of Mailing
  MailingDate = models.DateTimeField()
  # This defines a motivation group.
  MotivationGroupCode = models.CharField(max_length=8)
  # This defines the motivation detail within a motivation group.
  MotivationDetailCode = models.CharField(max_length=8)
  # Cost of Mailing
  MailingCost = models.DecimalField(max_digits=19, decimal_places=2, default=0)
  # Gift amount attributed to this mailing
  MailingAttributedAmount = models.DecimalField(max_digits=19, decimal_places=2, default=0)
  # Indicates if the mailing is viewable in comboboxes where the user can select it
  Viewable = models.BooleanField(default=True)
  # Date until this mailing is viewable for users (if p_viewable_l is set)
  ViewableUntil = models.DateTimeField()


class PAddressLayoutCode(models.Model):
  """
  This table contains the address layouts generally available for the user.
  """

  # Address Layout Code
  Code = models.CharField(max_length=16, null=False, blank=False, unique=True)
  # Description for Address Layout Code
  Description = models.CharField(max_length=50)
  # Index for Display Order (to determine the display position of the layout in a list)
  DisplayIndex = models.IntegerField(null=False, blank=False)
  # Comment for Address Layout Code
  Comment = models.CharField(max_length=300)
  # Can this layout code be deleted by the user?
  Deletable = models.BooleanField(default=True, null=False, blank=False)


class PAddressLayout(models.Model):
  """
  This table contains the address lines used in laying out an address. Eg a form letter address layout
  """

  Country = models.ForeignKey(PCountry, null=False, blank=False, related_name="PAddressLayout_Country", on_delete=models.CASCADE)
  AddressLayout = models.ForeignKey(PAddressLayoutCode, null=False, blank=False, related_name="PAddressLayout_AddressLayout", on_delete=models.CASCADE)
  AddressLineNumber = models.IntegerField(default=0, null=False, blank=False)
  AddressLineCode = models.CharField(max_length=8, null=False, blank=False)
  # This field is a short description of the Address Line Code record
  AddressPrompt = models.CharField(max_length=15)
  # System flag indicates a lock is on the record
  Locked = models.BooleanField(default=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_address_layout_pk', fields=['Country', 'AddressLayout', 'AddressLineNumber', 'AddressLineCode']),
    ]

class PAddressBlock(models.Model):
  """
  This table contains the address lines used in laying out an address. Eg a form letter address layout
  """

  Country = models.ForeignKey(PCountry, null=False, blank=False, related_name="PAddressBlock_Country", on_delete=models.CASCADE)
  AddressLayout = models.ForeignKey(PAddressLayoutCode, null=False, blank=False, related_name="PAddressBlock_AddressLayout", on_delete=models.CASCADE)
  # The complete set of address lines, including replaceable parameters
  AddressBlockText = models.CharField(max_length=256, null=False, blank=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_address_block_pk', fields=['Country', 'AddressLayout']),
    ]

class PAddressElement(models.Model):
  """
  This contains the elements which make up an address. Eg Name etc
  """

  # This Code is used to identify the address element.
  Code = models.CharField(max_length=12, null=False, blank=False, unique=True)
  AddressElementDescription = models.CharField(max_length=80)
  # Address element field name
  FieldName = models.CharField(max_length=30)
  # This is usually a ""."" or a "";"" or a "","" etc
  AddressElementText = models.CharField(max_length=1)


class PAddressBlockElement(models.Model):
  """
  This contains the elements which make up an address. Eg Name etc
  """

  # This Code is used to identify the address element.
  AddressElementCode = models.CharField(max_length=24, null=False, blank=False, unique=True)
  AddressElementDescription = models.CharField(max_length=80)
  # System flag indicates the element is a print directive and not a data placeholder
  IsDirective = models.BooleanField(null=False, blank=False)


class PAddressLine(models.Model):
  """
  This is an address line which consists of address elements.  Used along with p_address_layout and p_address_element to define layout of an address for different countries.
  """

  Code = models.CharField(max_length=8, null=False, blank=False)
  # This is the column number where the element field or text should be placed.
  AddressElementPosition = models.IntegerField(default=0, null=False, blank=False)
  # This Code is used to identify the address element.
  AddressElement = models.ForeignKey(PAddressElement, null=False, blank=False, related_name="PAddressLine_AddressElement", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_address_line_pk', fields=['Code', 'AddressElementPosition']),
    ]

class PAddresseeTitleOverride(models.Model):
  """
  This is used to override titles that might be different in the address than that in the letter. <br/>Eg      German     Herr   Herrn <br/>""Sehr geehrter Herr Starling"" in the letter and ""Herrn Starling"" in the address.
  """

  # This is the code used to identify a language.
  Language = models.ForeignKey(PLanguage, null=False, blank=False, related_name="PAddresseeTitleOverride_Language", on_delete=models.CASCADE)
  # The partner's title
  Title = models.CharField(max_length=32, null=False, blank=False)
  # The title to override the partner
  TitleOverride = models.CharField(max_length=32, null=False, blank=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_addressee_title_override_pk', fields=['Language', 'Title']),
    ]

class PFormality(models.Model):
  """
  Contains the text used in letters
  """

  # This is the code used to identify a language.
  Language = models.ForeignKey(PLanguage, null=False, blank=False, related_name="PFormality_Language", on_delete=models.CASCADE)
  # This is a code which identifies a country. <br/>It is taken from the ISO 3166-1-alpha-2 code elements.
  Country = models.ForeignKey(PCountry, null=False, blank=False, related_name="PFormality_Country", on_delete=models.CASCADE)
  AddresseeType = models.ForeignKey(PAddresseeType, null=False, blank=False, related_name="PFormality_AddresseeType", on_delete=models.CASCADE)
  FormalityLevel = models.IntegerField(default=1, null=False, blank=False)
  SalutationText = models.CharField(max_length=32)
  Title = models.CharField(max_length=12)
  ComplimentaryClosingText = models.CharField(max_length=32)
  PersonalPronoun = models.CharField(max_length=12)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_formality_pk', fields=['Language', 'Country', 'AddresseeType', 'FormalityLevel']),
    ]

class PLabel(models.Model):
  """
  Defines the attributes of different label types.  Eg: for address labels.
  """

  Code = models.CharField(max_length=8, null=False, blank=False, unique=True)
  # This identifies the form
  Form = models.ForeignKey(SForm, null=False, blank=False, related_name="PLabel_Form", on_delete=models.CASCADE)
  GapLines = models.IntegerField(default=0)
  Height = models.IntegerField(default=0, null=False, blank=False)
  Width = models.IntegerField(default=0, null=False, blank=False)
  GapColumns = models.IntegerField(default=0)
  LabelsAcross = models.IntegerField(default=0, null=False, blank=False)
  LabelsDown = models.IntegerField(default=0, null=False, blank=False)
  Description = models.CharField(max_length=35, null=False, blank=False)
  StartColumn = models.IntegerField(default=0)
  StartLine = models.IntegerField(default=0)


class PMergeForm(models.Model):
  """
  Master record for Mail Merge output creation
  """

  # Name of Merge Form
  Name = models.CharField(max_length=8, null=False, blank=False, unique=True)
  # Form description
  MergeFormDescription = models.CharField(max_length=32)


class PMergeField(models.Model):
  """
  Fields within a Mail Merge Form
  """

  # Name of Merge Form
  MergeForm = models.ForeignKey(PMergeForm, null=False, blank=False, related_name="PMergeField_MergeForm", on_delete=models.CASCADE)
  # Name of the field in the Word document which will be filled with the data
  Name = models.CharField(max_length=16, null=False, blank=False)
  # Position to define order of merge fields
  MergeFieldPosition = models.IntegerField(default=0)
  # Type of this field.  This defines the parameters which are required to generate the insert
  MergeType = models.CharField(max_length=16)
  # List of parameters required to create the actual insert
  MergeParameters = models.CharField(max_length=256)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_merge_field_pk', fields=['MergeForm', 'Name']),
    ]

class PPostcodeRange(models.Model):
  """
  Postcode ranges for each region
  """

  # Name of the postcode range
  Range = models.CharField(max_length=32, null=False, blank=False, unique=True)
  # Start of postcode range
  From = models.CharField(max_length=20)
  # End of postcode range
  To = models.CharField(max_length=20)


class PPostcodeRegion(models.Model):
  """
  List postcode regions
  """

  # Name of a postcode region
  Region = models.CharField(max_length=32, null=False, blank=False, unique=True)
  # This describes the region.
  Description = models.CharField(max_length=50)


class PPostcodeRegionRange(models.Model):
  """
  Links ranges to a region.
  """

  # Name of a postcode region
  Region = models.ForeignKey(PPostcodeRegion, null=False, blank=False, related_name="PPostcodeRegionRange_Region", on_delete=models.CASCADE)
  # A range for a postcode region
  Range = models.ForeignKey(PPostcodeRange, null=False, blank=False, related_name="PPostcodeRegionRange_Range", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_postcode_region_range_pk', fields=['Region', 'Range']),
    ]

class PPublication(models.Model):
  """
  Details of a publication
  """

  # This is the key to the publication table
  Code = models.CharField(max_length=10, null=False, blank=False, unique=True)
  NumberOfIssues = models.IntegerField(default=0)
  # The number of free issues and reminders to send out.
  NumberOfReminders = models.IntegerField(default=1)
  # A short description of the publication
  PublicationDescription = models.CharField(max_length=40)
  ValidPublication = models.BooleanField(default=True)
  Frequency = models.ForeignKey(AFrequency, null=False, blank=False, related_name="PPublication_Frequency", on_delete=models.CASCADE)
  # The publication short code that is used on an address label
  LabelCode = models.CharField(max_length=3)
  PublicationLanguage = models.ForeignKey(PLanguage, related_name="PPublication_PublicationLanguage", on_delete=models.CASCADE)


class PPublicationCost(models.Model):
  """
  Cost of a publication
  """

  # The is the key to the publication table
  Publication = models.ForeignKey(PPublication, null=False, blank=False, related_name="PPublicationCost_Publication", on_delete=models.CASCADE)
  DateEffective = models.DateTimeField(null=False, blank=False)
  # This is a number of currency units
  PublicationCost = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # The cost of posting each item
  PostageCost = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # This defines which currency is being used
  Currency = models.ForeignKey(ACurrency, null=False, blank=False, related_name="PPublicationCost_Currency", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_publication_cost_pk', fields=['Publication', 'DateEffective']),
    ]

class PReasonSubscriptionGiven(models.Model):
  """
  List of reasons for giving a subscription
  """

  Code = models.CharField(max_length=12, null=False, blank=False, unique=True)
  Description = models.CharField(max_length=80, null=False, blank=False)


class PReasonSubscriptionCancelled(models.Model):
  """
  List of reasons for cancelling a subscription
  """

  Code = models.CharField(max_length=12, null=False, blank=False, unique=True)
  Description = models.CharField(max_length=80, null=False, blank=False)


class PContactAttribute(models.Model):
  """
  Possible attributes for partner contacts.  Gives the description of each attribute code.  An attribute is a type of contact that was made or which occurred with a partner.
  """

  # Contact Attribute Code
  Code = models.CharField(max_length=16, null=False, blank=False, unique=True)
  # This is a contact attribute description.
  Descr = models.CharField(max_length=32)
  # allowed to use this attribute for new contacts?
  Active = models.BooleanField(default=True, null=False, blank=False)


class PContactAttributeDetail(models.Model):
  """
  Possible attribute details for each contact attribute.  Breaks down the attribute into more specifice information that applies to a contact with a partner.
  """

  # Contact Attribute Code
  ContactAttribute = models.ForeignKey(PContactAttribute, null=False, blank=False, related_name="PContactAttributeDetail_ContactAttribute", on_delete=models.CASCADE)
  # code for attribute detail
  ContactAttrDetailCode = models.CharField(max_length=16, null=False, blank=False)
  # This is a contact attribute detail description.
  ContactAttrDetailDescr = models.CharField(max_length=32)
  # allowed to use this attribute detail for new contacts?
  Active = models.BooleanField(default=True, null=False, blank=False)
  # Contact attribute detail comment
  Comment = models.CharField(max_length=4000)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_contact_attribute_detail_pk', fields=['ContactAttribute', 'ContactAttrDetailCode']),
    ]

class PMethodOfContact(models.Model):
  """
  How contacts are made
  """

  Code = models.CharField(max_length=8, null=False, blank=False, unique=True)
  Description = models.CharField(max_length=32)
  ContactType = models.CharField(max_length=8)
  ValidMethod = models.BooleanField(default=True, null=False, blank=False)
  # This defines if the method of contact code can be deleted. <br/>This can only be updated by the system manager. <br/>At the risk of serious operational integrity. <br/>Default to Yes
  Deletable = models.BooleanField(default=True, null=False, blank=False)


class PContactLog(models.Model):
  """
  Details of contacts with partners
  """

  # identifying key for p_contact_log
  ContactLogId = models.IntegerField(default=0, null=False, blank=False, unique=True)
  # Date of contact
  ContactDate = models.DateTimeField(null=False, blank=False)
  # Time of contact
  ContactTime = models.IntegerField(default=0)
  # Contact code
  Contact = models.ForeignKey(PMethodOfContact, null=False, blank=False, related_name="PContactLog_Contact", on_delete=models.CASCADE)
  # User who made the contact
  Contactor = models.CharField(max_length=10)
  # The Message ID (only applies if the type of contact is an email); this helps to identify the email and to interface with the EMail application
  ContactMessageId = models.CharField(max_length=100)
  # Contact Comment (also used to hold contents of emails)
  ContactComment = models.CharField(max_length=15000)
  # Identifies a module. A module is any part of aprogram which is related to each menu entry or to the sub-system. Eg, partner administration, AP, AR etc.
  Module = models.ForeignKey(SModule, related_name="PContactLog_Module", on_delete=models.CASCADE)
  # If set, this contact is restricted to one user.
  User = models.ForeignKey(SUser, related_name="PContactLog_User", on_delete=models.CASCADE)
  # The mailing code associated with the contact
  Mailing = models.ForeignKey(PMailing, related_name="PContactLog_Mailing", on_delete=models.CASCADE)
  # Indicates whether or not the contact has restricted access. If it does then the access will be controlled by s_group_partner_contact
  Restricted = models.BooleanField(default=False)
  # Location of contact
  ContactLocation = models.CharField(max_length=4000)


class PPartnerContactAttribute(models.Model):
  """
  Associates a p_contact_attribute_detail with a p_contact_log.  A contact log may have more than one p_contact_attribute_detail associated with it.
  """

  # identifying key for p_contact_log
  Contact = models.ForeignKey(PContactLog, null=False, blank=False, related_name="PPartnerContactAttribute_Contact", on_delete=models.CASCADE)
  ContactAttributeDetail = models.ForeignKey(PContactAttributeDetail, null=False, blank=False, related_name="PPartnerContactAttribute_ContactAttributeDetail", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_partner_contact_attribute_pk', fields=['Contact', 'ContactAttributeDetail']),
    ]

class PForm(models.Model):
  """
  The form description for user definable forms such as receipts
  """

  # The code which defines the type of form described in the table
  Code = models.CharField(max_length=10, null=False, blank=False)
  # The name of the form being created for the form code.
  Name = models.CharField(max_length=10, null=False, blank=False)
  # The language that this form is written in.  Use 99 if the form can be used for unspecified languages.
  FormLanguage = models.ForeignKey(PLanguage, null=False, blank=False, related_name="PForm_FormLanguage", on_delete=models.CASCADE)
  # Description of the form
  FormDescription = models.CharField(max_length=50)
  # If there are several types of form then it can be specified here.  Eg an annual receipt and an individual receipt.
  TypeCode = models.CharField(max_length=12, null=False, blank=False)
  # The address layout code that defines the address block content.
  AddressLayout = models.ForeignKey(PAddressLayoutCode, related_name="PForm_AddressLayout", on_delete=models.CASCADE)
  # The formality level to use if the template contains greetings or salutations. 1=Informal, 6=Very formal
  FormalityLevel = models.IntegerField(default=1, null=False, blank=False)
  # Is the template available in the database.
  TemplateAvailable = models.BooleanField(default=False, null=False, blank=False)
  # The binary template file encoded as Base64 text
  # The file type associated with the template.
  TemplateFileExtension = models.CharField(max_length=8)
  # Date the template was uploaded to the database
  TemplateUploadDate = models.DateTimeField()
  # Time the template was uploaded to the database
  TemplateUploadTime = models.IntegerField()
  TemplateUploadedByUser = models.ForeignKey(SUser, related_name="PForm_TemplateUploadedByUser", on_delete=models.CASCADE)
  # The minimum amount that is acceptable on a receipt
  MinimumAmount = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # Allows the exclusion of certain records from a report
  Options = models.CharField(max_length=32)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_form_pk', fields=['Code', 'Name', 'FormLanguage']),
    ]

class ASubSystem(models.Model):
  """
  Subsystems to the general ledger which can be added and removed independantly.  Eg GL, AP, AR, GR
  """

  # Defines a sub system of accounts
  Code = models.CharField(max_length=12, null=False, blank=False, unique=True)
  # Name of a sub system
  Name = models.CharField(max_length=32, null=False, blank=False)
  # The filename of the process to call
  SetupSubSystemProcess = models.CharField(max_length=12, null=False, blank=False)
  # The filename of the process to call
  SubSystemToCall = models.CharField(max_length=12)


class ATaxType(models.Model):
  """
  used for invoicing
  """

  # This is whether it is GST, VAT
  Code = models.CharField(max_length=8, null=False, blank=False, unique=True)
  # This is a short description which is 32 characters long
  TaxTypeDescription = models.CharField(max_length=32)


class ALedger(models.Model):
  """
  Basic information for each general ledger on the system. Also counters for ledger-specific variables (such as last receipt number).
  """

  # This is used as a key field in most of the accounting system files .It is created from the first 4 digits of a partner key of type ""ledger"".
  LedgerNumber = models.IntegerField(default=0, null=False, blank=False, unique=True)
  # This is the ledger name
  Name = models.CharField(max_length=32)
  # Defines if the ledger is in use
  LedgerStatus = models.BooleanField(null=False, blank=False)
  # This is the last batch number used within a ledger
  LastBatchNumber = models.IntegerField(default=0, null=False, blank=False)
  LastRecurringBatchNumber = models.IntegerField(default=0, null=False, blank=False)
  LastGiftNumber = models.IntegerField(default=0, null=False, blank=False)
  LastApInvNumber = models.IntegerField(default=0, null=False, blank=False)
  LastHeaderRNumber = models.IntegerField(default=0, null=False, blank=False)
  LastPoNumber = models.IntegerField(default=0, null=False, blank=False)
  LastSoNumber = models.IntegerField(default=0, null=False, blank=False)
  # This is a number of currency units
  MaxGiftAidAmount = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # This is a number of currency units
  MinGiftAidAmount = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  NumberOfGiftsToDisplay = models.IntegerField(default=0, null=False, blank=False)
  TaxType = models.ForeignKey(ATaxType, related_name="ALedger_TaxType", on_delete=models.CASCADE)
  # The account for inter-ledger transfers.
  IltGlAccountCode = models.CharField(max_length=8)
  # This identifies the account the financial transaction must be stored against
  ProfitLossGlAccountCode = models.CharField(max_length=8)
  # This defines which accounting period is being used
  NumberOfAccountingPeriods = models.IntegerField(default=0, null=False, blank=False)
  # This identifies a country. It uses the ISO 3166-1-alpha-2 code elements.
  Country = models.ForeignKey(PCountry, related_name="ALedger_Country", on_delete=models.CASCADE)
  # This defines which currency is being used
  BaseCurrency = models.ForeignKey(ACurrency, related_name="ALedger_BaseCurrency", on_delete=models.CASCADE)
  # Used to get a yes no response from the user
  TransactionAccount = models.BooleanField(default=False, null=False, blank=False)
  # Used to get a yes no response from the user
  YearEnd = models.BooleanField(default=False, null=False, blank=False)
  # The account for foreign exchange gains or losses
  ForexGainsLossesAccount = models.CharField(max_length=8, null=False, blank=False)
  # Used to get a yes no response from the user
  SystemInterface = models.BooleanField(default=False, null=False, blank=False)
  # Used to get a yes no response from the user
  SuspenseAccount = models.BooleanField(default=False, null=False, blank=False)
  # Used to get a yes no response from the user
  BankAccounts = models.BooleanField(default=False, null=False, blank=False)
  # Used to get a yes no response from the user
  DeleteLedger = models.BooleanField(default=False, null=False, blank=False)
  # Used to get a yes no response from the user
  NewFinancialYear = models.BooleanField(default=False, null=False, blank=False)
  # Used to get a yes no response from the user
  RecalculateGlMaster = models.BooleanField(default=False, null=False, blank=False)
  # Defines which installation is running on this database
  InstallationId = models.CharField(max_length=8)
  BudgetControl = models.BooleanField(default=False)
  BudgetDataRetention = models.IntegerField(default=0)
  CostOfSalesGlAccount = models.CharField(max_length=8)
  CreditorGlAccountCode = models.CharField(max_length=8)
  CurrentFinancialYear = models.IntegerField(default=0)
  CurrentPeriod = models.IntegerField(default=0)
  DateCrDrBalances = models.DateTimeField()
  DebtorGlAccountCode = models.CharField(max_length=8)
  FaDepreciationGlAccount = models.CharField(max_length=8)
  FaGlAccountCode = models.CharField(max_length=8)
  FaPlOnSaleGlAccount = models.CharField(max_length=8)
  FaProvForDepnGlAccount = models.CharField(max_length=8)
  IltAccount = models.BooleanField(default=False)
  LastApDnNumber = models.IntegerField(default=0)
  LastPoRetNumber = models.IntegerField(default=0)
  LastSoDelNumber = models.IntegerField(default=0)
  LastSoRetNumber = models.IntegerField(default=0)
  LastSpecialGiftNumber = models.IntegerField(default=0)
  NumberFwdPostingPeriods = models.IntegerField(default=0)
  DiscountAllowedPct = models.DecimalField(max_digits=5, decimal_places=2, default=0)
  DiscountReceivedPct = models.DecimalField(max_digits=5, decimal_places=2, default=0)
  PoAccrualGlAccountCode = models.CharField(max_length=8)
  # This flag is set between the completion of the last month of the year and the year itself. In this state some activities are disabled and some others are enabled.
  ProvisionalYearEnd = models.BooleanField(default=False)
  PurchaseGlAccountCode = models.CharField(max_length=8)
  RetEarningsGlAccount = models.CharField(max_length=8)
  SalesGlAccountCode = models.CharField(max_length=8)
  SoAccrualGlAccountCode = models.CharField(max_length=8)
  StockAccrualGlAccount = models.CharField(max_length=8)
  StockAdjGlAccountCode = models.CharField(max_length=8)
  StockGlAccountCode = models.CharField(max_length=8)
  TaxExclIncl = models.BooleanField()
  TaxExclInclIndicator = models.BooleanField(default=False)
  TaxInputGlAccountCode = models.CharField(max_length=8)
  TaxInputGlCcCode = models.CharField(max_length=8)
  TaxOutputGlAccountCode = models.CharField(max_length=8)
  TermsOfPaymentCode = models.CharField(max_length=8)
  LastPoRecNumber = models.IntegerField(default=0)
  TaxGlAccountNumber = models.IntegerField(default=0)
  ActualsDataRetention = models.IntegerField(default=11)
  # Partner key which links the ledger to the partner type record where the type is a ledger.
  PartnerKey = models.IntegerField(default=0)
  CalendarMode = models.BooleanField()
  # How far along is the year end process.
  YearEndProcessStatus = models.IntegerField(default=0)
  # last used cashbook payment header number
  LastHeaderPNumber = models.IntegerField(default=0, null=False, blank=False)
  # Is this ledger an ILT processing centre (ie, clearinghouse status)
  IltProcessingCentre = models.BooleanField(default=False)
  # The number of the last gift batch to be created.
  LastGiftBatchNumber = models.IntegerField(default=0)
  # This defines which currency to use as a second ('international') base currency.
  IntlCurrency = models.ForeignKey(ACurrency, related_name="ALedger_IntlCurrency", on_delete=models.CASCADE)
  # The number of the last gift batch to be created.
  LastRecGiftBatchNumber = models.IntegerField(default=0)
  # How many years to retain gift data.
  GiftDataRetention = models.IntegerField(default=2)
  # When recalculating the account report structure this indicates that all periods should be recalculated.
  RecalculateAllPeriods = models.BooleanField(default=False)
  # identifes the Last used ICH process number
  LastIchNumber = models.IntegerField(default=0, null=False, blank=False)
  # Indicates whether the ledger is just for storing consolidated accounts (rather than a 'real' ledger).
  ConsolidationLedger = models.BooleanField(default=False)


class ATaxTable(models.Model):
  """
  This is used by the invoicing
  """

  # This is used as a key field in most of the accounting system files
  Ledger = models.ForeignKey(ALedger, null=False, blank=False, related_name="ATaxTable_Ledger", on_delete=models.CASCADE)
  # The tax type is always the same, e.g. VAT
  TaxType = models.ForeignKey(ATaxType, null=False, blank=False, related_name="ATaxTable_TaxType", on_delete=models.CASCADE)
  # this describes whether it is e.g. the standard, reduced or zero rate of VAT
  TaxRateCode = models.CharField(max_length=8, null=False, blank=False)
  # this describes when this particular percentage rate has become valid by law
  TaxValidFrom = models.DateTimeField(null=False, blank=False)
  # This is a short description which is 32 charcters long
  TaxRateDescription = models.CharField(max_length=32)
  # Tax rate
  TaxRate = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # flag that prevents this rate from being used, e.g. if it has been replaced by another rate
  Active = models.BooleanField(default=True)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_tax_table_pk', fields=['Ledger', 'TaxType', 'TaxRateCode', 'TaxValidFrom']),
    ]

class ALedgerInitFlag(models.Model):
  """
  Ledger Init Flags
  """

  Ledger = models.ForeignKey(ALedger, null=False, blank=False, related_name="ALedgerInitFlag_Ledger", on_delete=models.CASCADE)
  InitOptionName = models.CharField(max_length=32, null=False, blank=False)
  Value = models.CharField(max_length=64, default='IsSet', null=False, blank=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_ledger_init_flag_pk', fields=['Ledger', 'InitOptionName']),
    ]

class ABudgetType(models.Model):
  """
  Used for initial set up of budgets, for how to calculate amounts for each period.  Some possible types are adhoc,same,percentage of annual.
  """

  # The type. Adhoc, Split, Same, Inflate.
  Code = models.CharField(max_length=8, null=False, blank=False, unique=True)
  BudgetTypeDescription = models.CharField(max_length=32, null=False, blank=False)
  # The Petra programme filename of the process to call
  BudgetProcessToCall = models.CharField(max_length=20, null=False, blank=False)


class AAccountPropertyCode(models.Model):
  """
  Extra properties that might want to be saved with an account can be defined in this table.
  """

  # Code for the property
  PropertyCode = models.CharField(max_length=20, null=False, blank=False, unique=True)
  # Description of this property
  Description = models.CharField(max_length=200)


class ACostCentreTypes(models.Model):
  """
  Stores standard and user-defined cost centre types.  For example: Foreign, Local.
  """

  # This is used as a key field in most of the accounting system files
  Ledger = models.ForeignKey(ALedger, null=False, blank=False, related_name="ACostCentreTypes_Ledger", on_delete=models.CASCADE)
  # Type of cost centre (Defaults: Foreign or Local)
  CostCentreType = models.CharField(max_length=8, default='Local', null=False, blank=False)
  # The description of the cost centre type
  CcDescription = models.CharField(max_length=30)
  # Can this cost centre type be deleted by the user?
  Deletable = models.BooleanField(default=True)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_cost_centre_types_pk', fields=['Ledger', 'CostCentreType']),
    ]

class ACostCentre(models.Model):
  """
  Master cost centre records which contain details of each cost centre and their relationship to each other; determines the cost centre structure.
  """

  # The ledger in which the cost centre is used.
  Ledger = models.ForeignKey(ALedger, null=False, blank=False, related_name="ACostCentre_Ledger", on_delete=models.CASCADE)
  # This identifies which cost centre an account is applied to. A cost centre can be a partner but reflected as a character rather than a numeric
  Code = models.CharField(max_length=12, null=False, blank=False)
  # This identifies which cost centre the cost centre summarises to.
  CostCentreToReportTo = models.CharField(max_length=12)
  Name = models.CharField(max_length=32, null=False, blank=False)
  PostingCostCentre = models.BooleanField(null=False, blank=False)
  CostCentreActive = models.BooleanField(default=True)
  ProjectStatus = models.BooleanField(default=False)
  ProjectConstraintDate = models.DateTimeField()
  ProjectConstraintAmount = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  SystemCostCentre = models.BooleanField(default=False)
  # ICH or non-ICH clearing
  ClearingAccount = models.CharField(max_length=12, default='8500')
  # At Year End, Balance in this Cost Centre will roll up to this account
  RetEarningsAccountCode = models.CharField(max_length=12, default='9700')
  # Determine how to roll up the balance in this Cost Centre
  RollupStyle = models.CharField(max_length=12, default='Always')
  CostCentreTypes = models.ForeignKey(ACostCentreTypes, null=False, blank=False, related_name="ACostCentre_CostCentreTypes", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_cost_centre_pk', fields=['Code']),
    ]

class ABudgetRevision(models.Model):
  """
  This defines a certain revision of a budget in a ledger in a year.
  """

  # This is used as a key field in most of the accounting system files
  Ledger = models.ForeignKey(ALedger, null=False, blank=False, related_name="ABudgetRevision_Ledger", on_delete=models.CASCADE)
  # The year that this budget applies to
  Year = models.IntegerField(null=False, blank=False)
  # A budget can have several revisions per year
  Revision = models.IntegerField(default=0, null=False, blank=False)
  # A description of this revision of the budget
  Description = models.CharField(max_length=100)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_budget_revision_pk', fields=['Ledger', 'Year', 'Revision']),
    ]

class AAccountingPeriod(models.Model):
  """
  Information about each financial period in a ledger.
  """

  # The ledger that the period applies to.
  Ledger = models.ForeignKey(ALedger, null=False, blank=False, related_name="AAccountingPeriod_Ledger", on_delete=models.CASCADE)
  # The accounting period number.  Must be <= 20
  AccountingPeriodNumber = models.IntegerField(default=0, null=False, blank=False)
  # This is a short description which is 32 charcters long
  Desc = models.CharField(max_length=32, null=False, blank=False)
  PeriodStartDate = models.DateTimeField(null=False, blank=False)
  PeriodEndDate = models.DateTimeField(null=False, blank=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_accounting_period_pk', fields=['Ledger', 'AccountingPeriodNumber']),
    ]

class AAccountingSystemParameter(models.Model):
  """
  One record describing the limitations imposed on the accounting system.
  """

  Ledger = models.ForeignKey(ALedger, null=False, blank=False, related_name="AAccountingSystemParameter_Ledger", on_delete=models.CASCADE)
  NumberOfAccountingPeriods = models.IntegerField(default=0)
  ActualsDataRetention = models.IntegerField(default=0)
  BudgetDataRetention = models.IntegerField(default=0)
  NumberFwdPostingPeriods = models.IntegerField(default=0)
  # Recipient gift statement text
  RecipientGiftStatementTxt = models.CharField(max_length=132)
  # Recipient gift statement text 2
  RecipientGiftStatementTx2 = models.CharField(max_length=132)
  # Donor gift statement text
  DonorGiftStatementTxt = models.CharField(max_length=132)
  # Donor gift statement text 2
  DonorGiftStatementTx2 = models.CharField(max_length=132)
  # Hosa statement text
  HosaStatementTxt = models.CharField(max_length=132)
  # Hosa (Home Office Statement of Accounts) statement text 2
  HosaStatementTx2 = models.CharField(max_length=132)
  # Hosa statement text 3
  HosaStatementTx3 = models.CharField(max_length=132)
  # Hosa statement text 4
  HosaStatementTx4 = models.CharField(max_length=132)
  # Text for the donor receipt heading.
  DonorReceiptTxt = models.CharField(max_length=32)
  # Stewardship Report  text
  StewardshipReportTxt = models.CharField(max_length=132)
  # Stewardship Report  text
  StewardshipReportTx2 = models.CharField(max_length=132)
  # Text for the yearly donor receipt heading.
  DonorYearlyReceiptTxt = models.CharField(max_length=32)
  # How many years to retain gift data.
  GiftDataRetention = models.IntegerField(default=2)
  # Text to put on receipt when addressing a deceased donor
  DeceasedAddressText = models.CharField(max_length=200)


class AAnalysisStoreTable(models.Model):
  """
  List of tables in the financial system, meant to be used with analysis attributes. Not available.
  """

  StoreName = models.CharField(max_length=32, null=False, blank=False, unique=True)


class AAnalysisType(models.Model):
  """
  Types of analysis attributes.
  """

  # The number of the ledger in which the analysis type is used.
  Ledger = models.ForeignKey(ALedger, null=False, blank=False, related_name="AAnalysisType_Ledger", on_delete=models.CASCADE)
  Code = models.CharField(max_length=8, null=False, blank=False)
  # This is a short description which is 32 charcters long
  AnalysisTypeDescription = models.CharField(max_length=32, null=False, blank=False)
  # Shows what type of analysis attribute it is
  AnalysisMode = models.BooleanField(null=False, blank=False)
  AnalysisStore = models.CharField(max_length=32)
  # The name of the field within a table which will be used as the analysis attribute
  AnalysisElement = models.CharField(max_length=32)
  # To indicate whether the user or system has set up the analysis type.
  SystemAnalysisType = models.BooleanField(default=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_analysis_type_pk', fields=['Ledger', 'Code']),
    ]

class ACorporateExchangeRate(models.Model):
  """
  Hold (monthly) corporate rates.
  """

  # Defines the currency being exchanged
  FromCurrency = models.ForeignKey(ACurrency, null=False, blank=False, related_name="ACorporateExchangeRate_FromCurrency", on_delete=models.CASCADE)
  # Defines which currency is being changed to
  ToCurrency = models.ForeignKey(ACurrency, null=False, blank=False, related_name="ACorporateExchangeRate_ToCurrency", on_delete=models.CASCADE)
  # Date the exchange rate becomes effective
  DateEffectiveFrom = models.DateTimeField(null=False, blank=False)
  # The rate of exchange
  RateOfExchange = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # System generated time stamp.
  TimeEffectiveFrom = models.IntegerField(default=0, null=False, blank=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_corporate_exchange_rate_pk', fields=['FromCurrency', 'ToCurrency', 'DateEffectiveFrom']),
    ]

class ADailyExchangeRate(models.Model):
  """
  Ad hoc exchange rates.
  """

  # Defines the currency being exchanged
  FromCurrency = models.ForeignKey(ACurrency, null=False, blank=False, related_name="ADailyExchangeRate_FromCurrency", on_delete=models.CASCADE)
  # Defines which currency is being changed to
  ToCurrency = models.ForeignKey(ACurrency, null=False, blank=False, related_name="ADailyExchangeRate_ToCurrency", on_delete=models.CASCADE)
  # Date the exchange rate becomes effective
  DateEffectiveFrom = models.DateTimeField(null=False, blank=False)
  # The date and time
  TimeEffectiveFrom = models.IntegerField(default=0, null=False, blank=False)
  # The rate of exchange
  RateOfExchange = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_daily_exchange_rate_pk', fields=['FromCurrency', 'ToCurrency', 'DateEffectiveFrom', 'TimeEffectiveFrom']),
    ]

class PEmail(models.Model):
  """
  email addresses of our organisation
  """

  EmailAddress = models.CharField(max_length=40, default='first.last@field.om.org', null=False, blank=False, unique=True)
  Description = models.CharField(max_length=80)
  Valid = models.BooleanField(default=True)
  # This defines if the email code can be deleted. <br/>This can only be updated by the system manager. <br/>At the risk of serious operational integrity. <br/>Default to Yes
  Deletable = models.BooleanField(default=True, null=False, blank=False)


class AForm(models.Model):
  """
  The form description for user definable forms such as receipts
  """

  # The code which defines the type of form described in the table
  Code = models.CharField(max_length=10, null=False, blank=False)
  # The name of the form being created for the form code.
  Name = models.CharField(max_length=10, null=False, blank=False)
  # Description of the form
  FormDescription = models.CharField(max_length=50)
  # File name used for the form. Includes path information.
  FileName = models.CharField(max_length=1000)
  # If there are several types of form then it can be specified here.  Eg an annual receipt and an individual receipt.
  TypeCode = models.CharField(max_length=12, null=False, blank=False)
  # The number of repeating lines that will be displayed on each page of a form.
  NumberOfDetails = models.IntegerField(default=0)
  # Is the report to be formatted to print in bold or not.
  PrintInBold = models.BooleanField(default=False, null=False, blank=False)
  # The total number of lines that can be displayed on the page
  LinesOnPage = models.IntegerField(default=66, null=False, blank=False)
  # The minimum amount that is acceptable on a receipt
  MinimumAmount = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Allows the exclusion of certain records from a report
  Options = models.CharField(max_length=32)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_form_pk', fields=['Code', 'Name']),
    ]

class AFormElementType(models.Model):
  """
  The element types that are available for placing in forms.
  """

  # The code which defines the type of form described in the table
  FormCode = models.CharField(max_length=10, null=False, blank=False)
  # The code of an element type that can be positioned for use on a form.
  Code = models.CharField(max_length=20, null=False, blank=False)
  # Description of Element Type
  Desc = models.CharField(max_length=80)
  DefaultLength = models.IntegerField(default=1)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_form_element_type_pk', fields=['FormCode', 'Code']),
    ]

class AFormElement(models.Model):
  """
  Each element that can be displayed on a form is defined on this table.
  """

  Form = models.ForeignKey(AForm, null=False, blank=False, related_name="AFormElement_Form", on_delete=models.CASCADE)
  # Unique identifier of each form element within a form
  FormSequence = models.IntegerField(default=0, null=False, blank=False)
  # The column that the element is to be displayed at on the form.
  Column = models.IntegerField(default=1, null=False, blank=False)
  # The row on the page that the element is to be displayed at.
  Row = models.IntegerField(default=1, null=False, blank=False)
  # The display length for the element.  e.g. it may be necessary to truncate fields.
  Length = models.IntegerField(default=1, null=False, blank=False)
  # This stores the number of characters to skip prior to printing.  It can be used to spread a description over two lines.
  Skip = models.IntegerField(default=0)
  # Indicates when the element is printed.  This would indicate detail lines, first, last page etc.
  WhenPrint = models.CharField(max_length=20, null=False, blank=False)
  # Text to be displayed if the element is defined as a literal.
  LiteralText = models.CharField(max_length=132)
  FormElementType = models.ForeignKey(AFormElementType, null=False, blank=False, related_name="AFormElement_FormElementType", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_form_element_pk', fields=['Form', 'FormSequence']),
    ]

class AFreeformAnalysis(models.Model):
  """
  Available analysis values that may be given to a transaction for each analysis type.
  """

  AnalysisType = models.ForeignKey(AAnalysisType, null=False, blank=False, related_name="AFreeformAnalysis_AnalysisType", on_delete=models.CASCADE)
  # Value of analysis code
  AnalysisValue = models.CharField(max_length=80, null=False, blank=False)
  # Analysis attribute values cannot be deleted, because they are needed for existing transaction analysis attributes. But they can be deactivated.
  Active = models.BooleanField(default=True)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_freeform_analysis_pk', fields=['AnalysisType', 'AnalysisValue']),
    ]

class AIchStewardship(models.Model):
  """
  Contains the calculation for the stewardship for a particular run.  Files and reports can be recreated from this.  ICH = International Clearing House (Handles transfering of funds and admin grant fees among offices.)
  """

  AccountingPeriod = models.ForeignKey(AAccountingPeriod, null=False, blank=False, related_name="AIchStewardship_AccountingPeriod", on_delete=models.CASCADE)
  # identifes the ICH process number
  IchNumber = models.IntegerField(default=0, null=False, blank=False)
  # This identifies which cost centre an account is applied to. A cost centre can be a partner but reflected as a character rather than a numeric
  CostCentreCode = models.CharField(max_length=12, null=False, blank=False)
  # Accounting Year
  Year = models.IntegerField(default=0, null=False, blank=False)
  # This is the date the stewardship was processed.
  DateProcessed = models.DateTimeField(null=False, blank=False)
  # Income amount for foreign cost centre's stewardship
  IncomeAmount = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Expense amount for foreign cost centre's stewardship
  ExpenseAmount = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Direct Transfer amount for foreign cost centre's stewardship
  DirectXferAmount = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Income amount for foreign cost centre's stewardship in International Currency
  IncomeAmountIntl = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Expense amount for foreign cost centre's stewardship in international currency
  ExpenseAmountIntl = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Direct Transfer amount for foreign cost centre's stewardship in international currency.
  DirectXferAmountIntl = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  CostCentre = models.ForeignKey(ACostCentre, null=False, blank=False, related_name="AIchStewardship_CostCentre", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_ich_stewardship_pk', fields=['AccountingPeriod', 'IchNumber']),
    ]

class AMethodOfGiving(models.Model):
  """
  Special payment programs the donor may give money through. (ie, Gift Aid in the UK). Currently not used in Petra release 1.
  """

  # Defines how a gift is given
  Code = models.CharField(max_length=12, null=False, blank=False, unique=True)
  # This is a short description which is 32 charcters long
  Desc = models.CharField(max_length=32, null=False, blank=False)
  # Shows if the method of giving involves a trust
  Trust = models.BooleanField(default=False, null=False, blank=False)
  # Shows if this method of giving involves a tax rebate
  TaxRebate = models.BooleanField(default=False, null=False, blank=False)
  # Shows if this method of giving is used by recurring gifts
  RecurringMethod = models.BooleanField(default=False, null=False, blank=False)
  # Shows whether this code is active
  Active = models.BooleanField(default=True)


class AMethodOfPayment(models.Model):
  """
  Media types of money received. Eg: Cash, Check Credit Card
  """

  # This is how the partner paid. EgCash, Cheque etc
  Code = models.CharField(max_length=8, null=False, blank=False, unique=True)
  # This is a short description which is 32 charcters long
  Desc = models.CharField(max_length=32, null=False, blank=False)
  MethodOfPaymentType = models.CharField(max_length=8)
  # The filename of the process to call
  ProcessToCall = models.CharField(max_length=12)
  SpecialMethodOfPmt = models.BooleanField(default=False, null=False, blank=False)
  # Shows whether this code is active
  Active = models.BooleanField(default=True)


class AMotivationGroup(models.Model):
  """
  This is used to track a partner's reason for contacting the organisation/sending money. Divided into Motivation Detail codes.
  """

  # This is used as a key field in most of the accounting system files
  Ledger = models.ForeignKey(ALedger, null=False, blank=False, related_name="AMotivationGroup_Ledger", on_delete=models.CASCADE)
  # This defines a motivation group.
  Code = models.CharField(max_length=8, null=False, blank=False)
  # This is a long description and is 80 characters long.
  MotivationGroupDescription = models.CharField(max_length=50, null=False, blank=False)
  # Defines whether the motivation group is still in use
  GroupStatus = models.BooleanField(null=False, blank=False)
  # This is a long description and is 80 characters long in the local language.
  MotivationGroupDescLocal = models.CharField(max_length=50)
  # Indicates whether or not the motivation has restricted access. If it does then the access will be controlled by s_group_motivation
  Restricted = models.BooleanField(default=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_motivation_group_pk', fields=['Ledger', 'Code']),
    ]

class ARecurringBatch(models.Model):
  """
  Templates of general ledger batches which can be copied into the ledger.
  """

  # This is used as a key field in most of the accounting system files
  Ledger = models.ForeignKey(ALedger, null=False, blank=False, related_name="ARecurringBatch_Ledger", on_delete=models.CASCADE)
  # identifes which batch a transaction belongs to
  BatchNumber = models.IntegerField(default=0, null=False, blank=False)
  # This is a long description and is 80 characters long.
  BatchDescription = models.CharField(max_length=80)
  # This is a number of currency units
  BatchControlTotal = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # identifies the status of a batch
  BatchStatus = models.CharField(max_length=12, default='Unposted', null=False, blank=False)
  # This is a number of currency units
  BatchRunningTotal = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # This is a number of currency units
  BatchDebitTotal = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # This is a number of currency units
  BatchCreditTotal = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # This defines which accounting period is being used
  BatchPeriod = models.IntegerField(default=0)
  # Date the  batch comes into effect
  DateEffective = models.DateTimeField(null=False, blank=False)
  # This identifies who the current user is
  User = models.ForeignKey(SUser, related_name="ARecurringBatch_User", on_delete=models.CASCADE)
  DateOfEntry = models.DateTimeField()
  Frequency = models.ForeignKey(AFrequency, related_name="ARecurringBatch_Frequency", on_delete=models.CASCADE)
  DateBatchLastRun = models.DateTimeField()
  # Identifies a journal within a batch
  LastJournal = models.IntegerField(default=0, null=False, blank=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_recurring_batch_pk', fields=['Ledger', 'BatchNumber']),
    ]

class ABatch(models.Model):
  """
  Store current and forward period general ledger batches for a ledger.
  """

  # The ledger that the batch belongs to.
  Ledger = models.ForeignKey(ALedger, null=False, blank=False, related_name="ABatch_Ledger", on_delete=models.CASCADE)
  # Identifies the batch.
  BatchNumber = models.IntegerField(default=0, null=False, blank=False)
  # This is a long description and is 80 characters long.
  BatchDescription = models.CharField(max_length=80)
  # Raw total amount of the batch.  If the journals within the batch have different currencies, this is just a raw numeric sum of all the journal amounts.  It does not reflect a monetary value in a specific currency.  Entered by the user.
  BatchControlTotal = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Running total amount of the batch calculated as transactions are enterd.  If the journals within the batch have different currencies, this is just a raw numeric sum of all the journal amounts.  It does not reflect a monetary value in a specific currency.
  BatchRunningTotal = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # Raw debit total amount of the batch.  If the journals within the batch have different currencies, this is just a raw numeric sum of all the journal amounts.  It does not reflect a monetary value in a specific currency.
  BatchDebitTotal = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # Raw credit total amount of the batch.  If the journals within the batch have different currencies, this is just a raw numeric sum of all the journal amounts.  It does not reflect a monetary value in a specific currency.
  BatchCreditTotal = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # This identifies which accounting period that the batch belongs to.
  BatchPeriod = models.IntegerField(default=0, null=False, blank=False)
  # The number of the accounting year
  BatchYear = models.IntegerField(default=0)
  # Date the  batch comes into effect
  DateEffective = models.DateTimeField(null=False, blank=False)
  # Date the  batch was created.
  DateOfEntry = models.DateTimeField(null=False, blank=False)
  # Has this batch been posted yet?
  BatchStatus = models.CharField(max_length=12, default='Unposted')
  # Identifies a journal within a batch
  LastJournal = models.IntegerField(default=0, null=False, blank=False)
  # Number of the originating gift batch that generated this GL batch.
  GiftBatchNumber = models.IntegerField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_batch_pk', fields=['Ledger', 'BatchNumber']),
    ]

class ARevaluation(models.Model):
  """
  Holds information used specifically in revaluations. The table extends the a_journal table.
  """

  Batch = models.ForeignKey(ABatch, null=False, blank=False, related_name="ARevaluation_Batch", on_delete=models.CASCADE)
  # Identifies the revaluation journal within a batch (usually 1)
  JournalNumber = models.IntegerField(null=False, blank=False)
  # This defines which revaluation currency the rate applies to
  RevaluationCurrency = models.CharField(max_length=8, null=False, blank=False)
  # The rate of exchange from the revaluation currency (in a_revaluation_currency_c) to the ledger base currency.
  ExchangeRateToBase = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_revaluation_pk', fields=['Batch', 'JournalNumber']),
    ]

class ASpecialTransType(models.Model):
  """
  Transaction types which have special processing. Eg. Allocation, Reallocation, Gift, Revaluation.
  """

  # Defines a sub system of accounts
  SubSystem = models.ForeignKey(ASubSystem, null=False, blank=False, related_name="ASpecialTransType_SubSystem", on_delete=models.CASCADE)
  TransactionTypeCode = models.CharField(max_length=8, null=False, blank=False)
  # This is a short description which is 32 charcters long
  TransactionTypeDescription = models.CharField(max_length=32, null=False, blank=False)
  # The filename of the process to call
  SpecTransProcessToCall = models.CharField(max_length=12, null=False, blank=False)
  # Process to call to undo the work of the special transaction process, if needed
  SpecTransUndoProcess = models.CharField(max_length=8)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_special_trans_type_pk', fields=['SubSystem', 'TransactionTypeCode']),
    ]

class ASystemInterface(models.Model):
  """
  Shows which systems are interfaced (have been added) to each general ledger.
  """

  # This is used as a key field in most of the accounting system files
  Ledger = models.ForeignKey(ALedger, null=False, blank=False, related_name="ASystemInterface_Ledger", on_delete=models.CASCADE)
  # Defines a sub system of accounts
  SubSystem = models.ForeignKey(ASubSystem, null=False, blank=False, related_name="ASystemInterface_SubSystem", on_delete=models.CASCADE)
  SetUpComplete = models.BooleanField(default=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_system_interface_pk', fields=['Ledger', 'SubSystem']),
    ]

class ACurrencyLanguage(models.Model):
  """
  Describes what is to be displayed for a currency and language combination when displaying the amount as text.
  """

  # This defines which currency is being used
  Currency = models.ForeignKey(ACurrency, null=False, blank=False, related_name="ACurrencyLanguage_Currency", on_delete=models.CASCADE)
  # This is the code used to identify a language.
  Language = models.ForeignKey(PLanguage, null=False, blank=False, related_name="ACurrencyLanguage_Language", on_delete=models.CASCADE)
  # The currency unit label when the amount is 1
  UnitLabelSingular = models.CharField(max_length=16)
  # The currency unit label when the amount is > 1
  UnitLabelPlural = models.CharField(max_length=16)
  # This is needed to determine the gender in some languages.
  SpecialCode = models.CharField(max_length=16)
  # Describes what to do with the decimal when representing it as text.  Not to display, display as text or as a numeric
  DecimalOptions = models.CharField(max_length=12)
  # The currency decimal label when the amount is 1
  DecimalLabelSingular = models.CharField(max_length=16)
  # The currency decimal label when the amount is > 1
  DecimalLabelPlural = models.CharField(max_length=16)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_currency_language_pk', fields=['Currency', 'Language']),
    ]

class AArCategory(models.Model):
  """
  there are several categories that are can use invoicing: catering, hospitality, store and fees
  """

  # categories help to specify certain discounts and group articles etc
  Code = models.CharField(max_length=50, null=False, blank=False, unique=True)
  # description of this category
  ArDescription = models.CharField(max_length=150)
  # description of this category in the local language
  ArLocalDescription = models.CharField(max_length=150)


class AArArticle(models.Model):
  """
  defines an item that can be sold or a service that can be charged for; this can be used for catering, hospitality, store and fees; it can describe a specific book, or a group of equally priced books
  """

  # code that uniquely identifies the item; can also be a code of a group of equally priced items
  Code = models.CharField(max_length=50, null=False, blank=False, unique=True)
  # this article belongs to a certain category (catering, hospitality, store, fees)
  ArCategory = models.ForeignKey(AArCategory, null=False, blank=False, related_name="AArArticle_ArCategory", on_delete=models.CASCADE)
  # this article falls into a special tax/VAT category
  TaxType = models.ForeignKey(ATaxType, null=False, blank=False, related_name="AArArticle_TaxType", on_delete=models.CASCADE)
  # describes whether this describes a specific item, e.g. book, or a group of equally priced items
  ArSpecificArticle = models.BooleanField()
  # description of this article
  ArDescription = models.CharField(max_length=150)
  # description of this article in the local language
  ArLocalDescription = models.CharField(max_length=150)


class AArArticlePrice(models.Model):
  """
  assign a price to an article, which can be updated by time
  """

  # code that identifies the item to be sold or service to be charged
  ArArticle = models.ForeignKey(AArArticle, null=False, blank=False, related_name="AArArticlePrice_ArArticle", on_delete=models.CASCADE)
  # date from which this price is valid
  ArDateValidFrom = models.DateTimeField(null=False, blank=False)
  # the value of the item in base currency
  ArAmount = models.DecimalField(max_digits=24, decimal_places=10, null=False, blank=False)
  # the currency in which the price is given
  Currency = models.ForeignKey(ACurrency, null=False, blank=False, related_name="AArArticlePrice_Currency", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='ar_article_price_pk', fields=['ArArticle', 'ArDateValidFrom']),
    ]

class AArDiscount(models.Model):
  """
  defines a discount that depends on other conditions or can just be assigned to an invoice or article
  """

  # code that identifies the discount
  Code = models.CharField(max_length=50, null=False, blank=False)
  # date from which this discount is valid
  ArDateValidFrom = models.DateTimeField(null=False, blank=False)
  # this discount has only be created on the fly and should not be reusable elsewhere
  ArAdhoc = models.BooleanField(default=False)
  # flag that prevents this discount from being used, to avoid too long lists in comboboxes etc
  Active = models.BooleanField(default=True)
  # discount percentage; can be negative for expensive rooms etc
  ArDiscountPercentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
  # the absolute discount that is substracted from the article price; can be negative as well
  ArDiscountAbsolute = models.DecimalField(max_digits=24, decimal_places=10)
  # the absolute amount that is charged if this discount applies; e.g. 3 books for 5 Pound
  ArAbsoluteAmount = models.DecimalField(max_digits=24, decimal_places=10)
  # the currency in which the absolute discount or amount is given
  Currency = models.ForeignKey(ACurrency, null=False, blank=False, related_name="AArDiscount_Currency", on_delete=models.CASCADE)
  # this discount applies for this number of items that are bought at the same time
  ArNumberOfItems = models.IntegerField()
  # this discount applies for all of the items if at least this number of items is bought at the same time
  ArMinimumNumberOfItems = models.IntegerField()
  # this discount applies for this number of nights that the individual or group stays; this is needed because 100 people staying for one night do cost more than 50 people staying for 2 nights
  ArNumberOfNights = models.IntegerField()
  # this discount applies for all of the nights if the individual or group stays at least for the given amount of nights; this is needed because 100 people staying for one night do cost more than 50 people staying for 2 nights
  ArMinimumNumberOfNights = models.IntegerField()
  # this discount applies when a whole room is booked rather than just a bed
  ArWholeRoom = models.BooleanField()
  # this discount applies for a children (e.g. meals)
  ArChildren = models.BooleanField()
  # this discount applies when the booking has been done so many days before the stay (using ph_booking.ph_confirmed_d and ph_in_d)
  ArEarlyBookingDays = models.IntegerField()
  # this discount applies when the payment has been received within the given number of days after the invoice has been charged
  ArEarlyPaymentDays = models.IntegerField()
  # this discount applies if the article code matches
  ArArticle = models.ForeignKey(AArArticle, related_name="AArDiscount_ArArticle", on_delete=models.CASCADE)
  # this discounts applies to partners of this type
  PartnerType = models.ForeignKey(PType, related_name="AArDiscount_PartnerType", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='ar_discount_pk', fields=['Code', 'ArDateValidFrom']),
    ]

class AArDiscountPerCategory(models.Model):
  """
  defines which discount applies to which category to limit the options in the UI
  """

  # refers to a certain category (catering, hospitality, store, fees)
  ArCategory = models.ForeignKey(AArCategory, null=False, blank=False, related_name="AArDiscountPerCategory_ArCategory", on_delete=models.CASCADE)
  # code that identifies the discount
  ArDiscountCode = models.CharField(max_length=50, null=False, blank=False)
  ArDiscount = models.ForeignKey(AArDiscount, null=False, blank=False, related_name="AArDiscountPerCategory_ArDiscount", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='ar_discount_per_category_pk', fields=['ArCategory']),
    ]

class AArDefaultDiscount(models.Model):
  """
  defines which discounts should be applied by default during a certain event or time period to articles from a certain category
  """

  # refers to a certain category (catering, hospitality, store, fees)
  ArCategory = models.ForeignKey(AArCategory, null=False, blank=False, related_name="AArDefaultDiscount_ArCategory", on_delete=models.CASCADE)
  ArDiscount = models.ForeignKey(AArDiscount, null=False, blank=False, related_name="AArDefaultDiscount_ArDiscount", on_delete=models.CASCADE)
  # this clearly specifies which version of the discount is meant
  ArDiscountDateValidFrom = models.DateTimeField(null=False, blank=False)
  # this default discount is only applied during this time period; can be null for ongoing default discounts
  ArDateValidTo = models.DateTimeField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='ar_default_discount_pk', fields=['ArCategory', 'ArDiscount']),
    ]

class PtApplicantStatus(models.Model):
  """
  This table contains the different codes that indicate where an applicant is in the application continuum.
  """

  # This code indicates the status of an applicant.
  Code = models.CharField(max_length=16, null=False, blank=False, unique=True)
  # This describes the applicant status code.
  Description = models.CharField(max_length=40)
  # Indicates if this code can still be assigned?
  Unassignable = models.BooleanField(default=False)
  # Date from which this code was made unassignable.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PtApplicationType(models.Model):
  """
  This decribes the type of application a person has submitted, e.g, Short-Term, Long-Term, or 2 years.
  """

  # Name of the application type, e.g. Short-Term, Long-Term.
  AppTypeName = models.CharField(max_length=16, null=False, blank=False, unique=True)
  # Describes the application type.
  AppTypeDescr = models.CharField(max_length=40)
  # Can this application type be assigned?
  Unassignable = models.BooleanField(default=False)
  # This is the date the record was last updated.
  UnassignableDate = models.DateTimeField()
  # This field lists the different forms that are used for the various application types.
  AppFormType = models.CharField(max_length=16)
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PtContact(models.Model):
  """
  This list the various methods by which a person learns of this organisation. This table can be changed to fit any field's particular awareness programs.
  """

  # Name of the contact, e.g.  Friend, Program, Church.
  Name = models.CharField(max_length=20, null=False, blank=False, unique=True)
  # Describes the contact.
  Descr = models.CharField(max_length=40)
  # Can this position be assigned?
  Unassignable = models.BooleanField(default=False, null=False, blank=False)
  # This is the date the record was last updated.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PtSpecialApplicant(models.Model):
  """
  This table contains the codes that indicate special situations of applicants. 
  """

  # This code indicates a special status an applicant could have.
  Code = models.CharField(max_length=16, null=False, blank=False, unique=True)
  # This describes the special applicant status code.
  Description = models.CharField(max_length=40)
  # Indicates if this code can still be assigned?
  Unassignable = models.BooleanField(default=False)
  # Date from which this code was made unassignable.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PtLeadershipRating(models.Model):
  """
  This table contains the codes indicating the leadership potential of someone.
  """

  # This code indicates the leadership rating of an applicant.
  Code = models.CharField(max_length=20, null=False, blank=False, unique=True)
  # This describes the Leadership Rating code.
  Description = models.CharField(max_length=40)
  # Indicates if this code can still be assigned?
  Unassignable = models.BooleanField(default=False)
  # Date from which this code was made unassignable.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PtArrivalPoint(models.Model):
  """
  This table contains the codes used to indicate where the conferee is arriving or departing.
  """

  # This code indicates the arrival point of the congress attendee.
  Code = models.CharField(max_length=16, null=False, blank=False, unique=True)
  # This describes the arrival point.
  Description = models.CharField(max_length=40)
  # Indicates if this code can still be assigned?
  Unassignable = models.BooleanField(default=False)
  # Date from which this code was made unassignable.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PtOutreachPreferenceLevel(models.Model):
  """
  Describes the importance of the country and activity choices. 
  """

  # This code indicates the level of importance of the country and activity choice on outreachs.
  Code = models.CharField(max_length=20, null=False, blank=False, unique=True)
  # This describes the preference level code.
  Description = models.CharField(max_length=40)
  # Indicates if this code can still be assigned?
  Unassignable = models.BooleanField(default=False)
  # Date from which this code was made unassignable.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PtCongressCode(models.Model):
  """
  This table contains the codes that indicate a person's role and/or position at conferences and outreachs.
  """

  # This code indicates the role of the event attendee.
  Code = models.CharField(max_length=16, null=False, blank=False, unique=True)
  # This describes the Event Role.
  Description = models.CharField(max_length=40)
  # Indicates if this is valid pre-Conference Role.
  PreCongress = models.BooleanField(default=False)
  # Indicates if this role can still be assigned?
  Unassignable = models.BooleanField(default=False)
  # Date from which this role was made unassignable.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)
  Discounted = models.BooleanField(default=False)
  # Indicates if this is a valid role during a outreach.
  Outreach = models.BooleanField(default=False)
  # Indicates if this is valid Conference Role.
  Conference = models.BooleanField(default=False)
  # Indicates if this role is considered as a normal participant (e.g. in reports)
  Participant = models.BooleanField(default=False)


class PtTravelType(models.Model):
  """
  This table contains the codes that indicate the mode of travel being used. 
  """

  # This code indicates the different types of travel.
  Code = models.CharField(max_length=16, null=False, blank=False, unique=True)
  # This describes the types of travel .
  Description = models.CharField(max_length=40)
  # Indicates if this code can still be assigned?
  Unassignable = models.BooleanField(default=False)
  # Date from which this code was made unassignable.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PmDocumentCategory(models.Model):
  """
  This table contains the codes that indicate the categories of document types (grouping). 
  """

  # This code indicates the category of a document type.
  Code = models.CharField(max_length=32, null=False, blank=False, unique=True)
  # This describes the document type category.
  Description = models.CharField(max_length=50)
  # Indicates if document types for this category can be added on the fly
  Extendable = models.BooleanField(default=False)
  # Indicates if this code can still be assigned?
  Unassignable = models.BooleanField(default=False)
  # Date from which this code was made unassignable.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PmDocumentType(models.Model):
  """
  This table contains the codes that indicate the types of documents for a person. 
  """

  # This code indicates the type of document for a person.
  DocCode = models.CharField(max_length=20, null=False, blank=False, unique=True)
  # This code indicates the category of a document type.
  DocCategory = models.ForeignKey(PmDocumentCategory, null=False, blank=False, related_name="PmDocumentType_DocCategory", on_delete=models.CASCADE)
  # This describes the document type.
  Description = models.CharField(max_length=40)
  # Indicates if this code can still be assigned?
  Unassignable = models.BooleanField(default=False)
  # Date from which this code was made unassignable.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PtPassportType(models.Model):
  """
  This table contains the codes that indicate the type of passport a person holds. 
  """

  # This code indicates the type of passport a person holds.
  Code = models.CharField(max_length=16, null=False, blank=False, unique=True)
  # This describes the passport type.
  Description = models.CharField(max_length=40)
  # Indicates if this code can still be assigned?
  Unassignable = models.BooleanField(default=False)
  # Date from which this code was made unassignable.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PtLanguageLevel(models.Model):
  """
  This is the degree to which a language is spoken, e.g. a little, phrases, fluent.
  """

  # This field is a numeric representation of level of language.
  LanguageLevel = models.IntegerField(default=0, null=False, blank=False, unique=True)
  # Describes the level of fluency in a language.
  Descr = models.CharField(max_length=35, null=False, blank=False)
  # Can this contact still be listed?
  Unassignable = models.BooleanField(default=False)
  # This is the date from which this contact can no longer be assigned.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)
  # Exhaustive explanation of the Language Level.
  LanguageComment = models.CharField(max_length=400)


class PtAbilityArea(models.Model):
  """
  Defines the areas in which a person may possess an ability, e.g. plays the guitar.
  """

  # Name of the area of ability
  Name = models.CharField(max_length=20, null=False, blank=False, unique=True)
  # Describes the area of ability.
  Descr = models.CharField(max_length=45, null=False, blank=False)
  # Describes the area of ability
  RequirementAreaDescr = models.CharField(max_length=45, null=False, blank=False)
  # Can this ability be assigned?
  Unassignable = models.BooleanField(default=False, null=False, blank=False)
  # This is the date the record was last updated.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PtAbilityLevel(models.Model):
  """
  This is the degree to which an ability <br/>is possessed, e.g. a little. professional.
  """

  # This field is a numeric representation of level of ability.
  AbilityLevel = models.IntegerField(default=0, null=False, blank=False, unique=True)
  # Describes the level of ability.
  Descr = models.CharField(max_length=45, null=False, blank=False)
  # Can this ability level be assigned?
  Unassignable = models.BooleanField(default=False, null=False, blank=False)
  # This is the date the record was last updated.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PtQualificationArea(models.Model):
  """
  This defines the areas in which a person may posess a qualification, e.g. computing or accountancy. 
  """

  # Name of the area of qualification.
  Name = models.CharField(max_length=16, null=False, blank=False, unique=True)
  # Describes the area of qualification.
  Descr = models.CharField(max_length=40, null=False, blank=False)
  # Can this qualification be assigned?
  Qualification = models.BooleanField(default=False, null=False, blank=False)
  # This is the date the record was last updated.
  QualificationDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PtQualificationLevel(models.Model):
  """
  This is the level to which a qualifications is possessed, e.g. Secondary education, Master's Degree.
  """

  # This field is a numeric representation of level of qualification.
  QualificationLevel = models.IntegerField(default=0, null=False, blank=False, unique=True)
  # Describes the level of qualification.
  Descr = models.CharField(max_length=40, null=False, blank=False)
  # Can this qualification level be assigned?
  Unassignable = models.BooleanField(default=False, null=False, blank=False)
  # This is the date the record was last updated.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PtSkillCategory(models.Model):
  """
  This is the category that will be used for a person's skill
  """

  # Code for the Skill Category
  Code = models.CharField(max_length=30, null=False, blank=False, unique=True)
  # Describes the Category used for skills
  Description = models.CharField(max_length=80)
  # Can this category be assigned?
  Unassignable = models.BooleanField(default=False, null=False, blank=False)
  # This is the date the record was last updated.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PtSkillLevel(models.Model):
  """
  This is the level to which a skill is possessed
  """

  # This field is a numeric representation of level of skill.
  Level = models.IntegerField(default=0, null=False, blank=False, unique=True)
  # Describes the level of skill.
  Description = models.CharField(max_length=50, null=False, blank=False)
  # Can this skill level be assigned?
  Unassignable = models.BooleanField(default=False, null=False, blank=False)
  # This is the date the record was last updated.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PDataLabelLookupCategory(models.Model):
  """
  This table holds the categories that can be used for data label values.
  """

  # Code for Lookup Category
  CategoryCode = models.CharField(max_length=30, null=False, blank=False, unique=True)
  # Description for Lookup Category
  CategoryDesc = models.CharField(max_length=60)
  # Indicates if values for this category can be added on the fly
  Extendable = models.BooleanField(default=False)


class PDataLabel(models.Model):
  """
  This table is used to define data labels for individual use in each office.
  """

  # A sequence key for data labels.
  Key = models.IntegerField(null=False, blank=False, unique=True)
  # Label Text
  Text = models.CharField(max_length=50)
  # Data Label Group
  Group = models.CharField(max_length=50)
  # Description (Help Text) for the label that the user will see
  Description = models.CharField(max_length=200)
  # Data Type (char | integer | float | currency | boolean | date | time | partnerkey | lookup)
  DataType = models.CharField(max_length=20, null=False, blank=False)
  # Maximum length of data string if data type is set to character.
  CharLength = models.IntegerField()
  # Number of decimal places if data type is set to numeric.
  NumDecimalPlaces = models.IntegerField()
  # This defines which currency is being used (if data type is currency)
  Currency = models.ForeignKey(ACurrency, related_name="PDataLabel_Currency", on_delete=models.CASCADE)
  # If a lookup category is selected then the values can be chosen from a drop down box
  LookupCategory = models.ForeignKey(PDataLabelLookupCategory, related_name="PDataLabel_LookupCategory", on_delete=models.CASCADE)
  # If TRUE then a value for this label has to be set
  EntryMandatory = models.BooleanField(default=False)
  # If TRUE then this data label will be displayed. Gives a chance to hide but keep labels for historical reasons.
  Displayed = models.BooleanField(default=True)
  # Data label will not be displayed any longer from this date on.
  NotDisplayedFrom = models.DateTimeField()
  # if FALSE then the values will be displayed but are not editable.
  Editable = models.BooleanField(default=True)
  # Data label values will not be editable any longer from this date on.
  NotEditableFrom = models.DateTimeField()
  # Indicates whether or not the data label has restricted access. If it does then the access will be controlled by s_group_data_label
  Restricted = models.BooleanField(default=False)


class PDataLabelUse(models.Model):
  """
  This table defines where a data label is used and the order the labels appear in.
  """

  # A sequence key for data labels.
  DataLabel = models.ForeignKey(PDataLabel, null=False, blank=False, related_name="PDataLabelUse_DataLabel", on_delete=models.CASCADE)
  # Use of Data Label ( Person | Family | Church | Organisation | Bank | Unit | Venue | Personnel | LongTermApp | ShortTermApp )
  Use = models.CharField(max_length=20, null=False, blank=False)
  # Label Index (for sorting of labels).
  Idx1 = models.IntegerField(null=False, blank=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_data_label_use_pk', fields=['DataLabel', 'Use']),
    ]

class PDataLabelLookup(models.Model):
  """
  This table holds all lookup values that can be used for data label values.
  """

  # Code for Lookup Category
  Category = models.ForeignKey(PDataLabelLookupCategory, null=False, blank=False, related_name="PDataLabelLookup_Category", on_delete=models.CASCADE)
  # Code for Lookup Value
  ValueCode = models.CharField(max_length=40, null=False, blank=False)
  # Description for Lookup Value
  ValueDesc = models.CharField(max_length=60)
  # Indicates if this value is active (i.e. can be used)
  Active = models.BooleanField(default=True)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_data_label_lookup_pk', fields=['Category', 'ValueCode']),
    ]

class PmCommitmentStatus(models.Model):
  """
  This table holds the statuses that are be used for commitments.
  """

  # Code for Status
  Code = models.CharField(max_length=20, null=False, blank=False, unique=True)
  # Description for Status
  Desc = models.CharField(max_length=50)
  # Detailed Explanation for the Status
  Explanation = models.CharField(max_length=500)
  # Indicates if the person with this status is generally supposed to have access to the worldwide intranet of the organisation
  IntranetAccess = models.BooleanField(default=True)
  # Display Index (for sorting other than alphabetically).
  DisplayIdx1 = models.IntegerField()
  # Indicates if this code can still be assigned?
  Unassignable = models.BooleanField(default=False)
  # Date from which this code was made unassignable.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PtPosition(models.Model):
  """
  This is a listing of the different position which exist within our organisation, e.g. Field Leader, Book Keeper, Computer support.
  """

  # Name of the position.
  Name = models.CharField(max_length=30, null=False, blank=False)
  # Scope of this position.
  PositionScope = models.ForeignKey(UUnitType, null=False, blank=False, related_name="PtPosition_PositionScope", on_delete=models.CASCADE)
  # Describes the position.
  Descr = models.CharField(max_length=80)
  # Can this position be assigned?
  Unassignable = models.BooleanField(default=False, null=False, blank=False)
  # This is the date the record was last updated.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pt_position_pk', fields=['Name', 'PositionScope']),
    ]

class PtAssignmentType(models.Model):
  """
  Describes whether a person is full-time, part-time, etc.
  """

  # Indicates the type of assignment .
  Code = models.CharField(max_length=20, null=False, blank=False, unique=True)
  # This describes the one-letter assignment code.
  AssignmentCodeDescr = models.CharField(max_length=35, null=False, blank=False)
  # Can this qualification level be assigned?
  Unassignable = models.BooleanField(default=False, null=False, blank=False)
  # This is the date the record was last updated.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PcCostType(models.Model):
  """
  Cost types to be used for conference (extra) charges
  """

  # Unique name of the cost type
  Code = models.CharField(max_length=16, null=False, blank=False, unique=True)
  # Description of the cost type
  CostTypeDescription = models.CharField(max_length=40)
  # Can this cost type be assigned?
  Unassignable = models.BooleanField(default=False, null=False, blank=False)
  # This is the date the record was last updated.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PcConferenceOptionType(models.Model):
  """
  Lists types of options that can be used for a conference
  """

  # Unique name of the cost type
  OptionTypeCode = models.CharField(max_length=16, null=False, blank=False, unique=True)
  # Description of the option type
  OptionTypeDescription = models.CharField(max_length=40)
  OptionTypeComment = models.CharField(max_length=256)
  # Can this option type be assigned?
  Unassignable = models.BooleanField(default=False, null=False, blank=False)
  # This is the date the record was last updated.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PcDiscountCriteria(models.Model):
  """
  Lists possible criterias that must be met for discounts to be applied
  """

  # Unique name of the discount criteria
  Code = models.CharField(max_length=8, null=False, blank=False, unique=True)
  # Description of the discount criteria
  Desc = models.CharField(max_length=40)
  # Can this discount criteria be assigned?
  Unassignable = models.BooleanField(default=False, null=False, blank=False)
  # This is the date the record was last updated.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PcRoomAttributeType(models.Model):
  """
  Contains type of attributes that can be assigned to a room
  """

  Code = models.CharField(max_length=20, null=False, blank=False, unique=True)
  Desc = models.CharField(max_length=50)
  Valid = models.BooleanField(default=True)
  Deletable = models.BooleanField(default=True)


class PInterestCategory(models.Model):
  """
  Categories for Area of Interest
  """

  # Unique key for the table
  Category = models.CharField(max_length=10, null=False, blank=False, unique=True)
  Description = models.CharField(max_length=50)
  # Description of all the interest intensity levels.  Leave empty if levels not needed.
  LevelDescriptions = models.CharField(max_length=256)
  LevelRangeLow = models.IntegerField()
  LevelRangeHigh = models.IntegerField()


class PInterest(models.Model):
  """
  Area of Interest
  """

  # Unique key for the table
  Interest = models.CharField(max_length=10, null=False, blank=False, unique=True)
  # Interest category
  Category = models.ForeignKey(PInterestCategory, related_name="PInterest_Category", on_delete=models.CASCADE)
  Description = models.CharField(max_length=50)


class PReminderCategory(models.Model):
  """
  This table contains the codes that indicate the categories of reminders
  """

  # This code indicates the category of a reminder
  Code = models.CharField(max_length=20, null=False, blank=False, unique=True)
  # This describes the reminder category.
  Description = models.CharField(max_length=50)
  # Indicates if this code can still be assigned?
  Unassignable = models.BooleanField(default=False)
  # Date from which this code was made unassignable.
  UnassignableDate = models.DateTimeField()
  # Indicates if a record can be deleted.
  Deletable = models.BooleanField(default=True)


class PProcess(models.Model):
  """
  Refers to a process through which a Partner may go (eg. application, different status of donor - small->medium->big, etc)
  """

  # Code for the process
  Code = models.CharField(max_length=30, null=False, blank=False, unique=True)
  # Description of the process
  Descr = models.CharField(max_length=200)
  # Comma separated list of Partner Classes for which this process is valid. Null implies all Classes
  ProcessPartnerClasses = models.CharField(max_length=200)


class PState(models.Model):
  """
  A particular state within a process which can apply to a Partner. Each state will probably need to have an Idle state to indicate when no state applies.
  """

  # Process that this state belongs to
  Process = models.ForeignKey(PProcess, null=False, blank=False, related_name="PState_Process", on_delete=models.CASCADE)
  # Code for the state
  Code = models.CharField(max_length=30, null=False, blank=False)
  # Description of the state
  Descr = models.CharField(max_length=200)
  # Is this a currently active state?
  Active = models.BooleanField()
  # Is this a system defined state (as opposed to a user defined one)?
  SystemState = models.BooleanField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_state_pk', fields=['Process', 'Code']),
    ]

class PAction(models.Model):
  """
  A particular action within a process which can be performed on a Partner
  """

  # Process that this action is part of
  Process = models.ForeignKey(PProcess, null=False, blank=False, related_name="PAction_Process", on_delete=models.CASCADE)
  # Code for the action
  Code = models.CharField(max_length=30, null=False, blank=False)
  # Description of the action
  Descr = models.CharField(max_length=200)
  # Is this action currently in progress?
  Active = models.BooleanField()
  # Is this a system defined action (as opposed to a user defined one)?
  SystemAction = models.BooleanField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_action_pk', fields=['Process', 'Code']),
    ]

class PFirstContact(models.Model):
  """
  Lookup table for First Contact Codes (ie. how did person first hear about us)
  """

  Code = models.CharField(max_length=30, null=False, blank=False, unique=True)
  Descr = models.CharField(max_length=200)
  # Is this contact code still active (ie. should it be shown on picklists)?
  Active = models.BooleanField()


class PPartner(models.Model):
  """
  This is the main table of the partner system.  Partners can be individuals, families, organisations (churches, businesses), fields, cost centers, and others.  These represent various classes of partners.
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  PartnerKey = models.IntegerField(default=0, null=False, blank=False, unique=True)
  # This defines what type of partner this is. The classes that may be assigned are PERSON, FAMILY, CHURCH, ORGANISATION, UNIT, VENUE and BANK.
  PartnerClass = models.ForeignKey(PPartnerClasses, related_name="PPartner_PartnerClass", on_delete=models.CASCADE)
  # This is a sub-class of the partner class.
  AddresseeType = models.ForeignKey(PAddresseeType, related_name="PPartner_AddresseeType", on_delete=models.CASCADE)
  # Name of the person or organisation.  If a person, more name info is stored in p_person.
  ShortName = models.CharField(max_length=80)
  # An alternative name for a partner - mainly for entering the local language equivalent.
  PartnerShortNameLoc = models.CharField(max_length=80)
  # Partner name how it should appear as printed version (to be used if mechanism <br/>to build short name from first and last name does not work e.g. in case of different surnames for husband and wife)
  PrintedName = models.CharField(max_length=80)
  # Identifies the preferred language of the partner.
  Language = models.ForeignKey(PLanguage, related_name="PPartner_Language", on_delete=models.CASCADE)
  # Important information about this partner that users need to be aware of.
  KeyInformation = models.CharField(max_length=250)
  # Additional information about the partner that is important to store in the database.
  Comment = models.CharField(max_length=5000)
  # This code identifies the method of aquisition.
  Acquisition = models.ForeignKey(PAcquisition, related_name="PPartner_Acquisition", on_delete=models.CASCADE)
  # This code describes the status of a partner. <br/>Eg,  Active, Deceased etc
  Status = models.ForeignKey(PPartnerStatus, related_name="PPartner_Status", on_delete=models.CASCADE)
  # This is the date the status of the partner was last updated.
  StatusChange = models.DateTimeField()
  # Why was the status changed?
  StatusChangeReason = models.CharField(max_length=200)
  # Yes if this partner has been ""deleted.""
  DeletedPartner = models.BooleanField(default=False)
  # This is the finance details comment.
  FinanceComment = models.CharField(max_length=255)
  # How often the partner receives a receipt letter.
  ReceiptLetterFrequency = models.CharField(max_length=12)
  # Flags whether each gift given by a user is receipted
  ReceiptEachGift = models.BooleanField(default=True)
  # Flag whether to include this partner when running the Recipient Gift Email report
  EmailGiftStatement = models.BooleanField(default=False)
  # Yes if the donor wants to remain anonymous.  Names of anonymous donors will not appear on recipient gift statements.
  AnonymousDonor = models.BooleanField(default=False)
  # Yes if not ok to solicit the partner for funds.
  NoSolicitations = models.BooleanField(default=False)
  # Inicates if this partner has been assigned as a child unit to another unit.
  ChildIndicator = models.BooleanField(default=False)
  # Restricts use of the partner record to the user in p_user_id_c if 2 or the group in p_group_id_c if 1.
  Restricted = models.IntegerField(default=0)
  # The Petra user that the partner record is restricted to if p_restricted_i is 2.
  UserId = models.CharField(max_length=20)
  # The group of Petra users that the partner record is restricted to if p_restricted_i is 1.
  GroupId = models.CharField(max_length=20)
  PreviousName = models.CharField(max_length=256)
  # How did this Partner first hear about us?
  FirstContact = models.ForeignKey(PFirstContact, related_name="PPartner_FirstContact", on_delete=models.CASCADE)
  # How did this Partner first hear about us (freetext)?
  FirstContactFreeform = models.CharField(max_length=200)
  # Intranet ID. Needed for making the link to the International Website, e.g. for using the Online Address Book.
  IntranetId = models.CharField(max_length=100)
  # Timezone that applies to the partner (address does not necessarily determine that). <br/>This refers to data in the International Address Book.
  Timezone = models.CharField(max_length=50)


class PRecentPartners(models.Model):
  """
  The partners a user has been working with recently
  """

  # Who is this for
  User = models.ForeignKey(SUser, null=False, blank=False, related_name="PRecentPartners_User", on_delete=models.CASCADE)
  # What partner is it about?
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PRecentPartners_Partner", on_delete=models.CASCADE)
  # When was this partner edited by this user?
  When = models.DateTimeField()
  When = models.IntegerField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_recent_partners_pk', fields=['User', 'Partner']),
    ]

class PPartnerLocation(models.Model):
  """
  Links partners with locations (addresses) and has specific info about the link (e.g. date effective)
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PPartnerLocation_Partner", on_delete=models.CASCADE)
  Location = models.ForeignKey(PLocation, null=False, blank=False, related_name="PPartnerLocation_Location", on_delete=models.CASCADE)
  DateEffective = models.DateTimeField()
  DateGoodUntil = models.DateTimeField()
  LocationType = models.ForeignKey(PLocationType, related_name="PPartnerLocation_LocationType", on_delete=models.CASCADE)
  SendMail = models.BooleanField(default=False)
  LocationDetailComment = models.CharField(max_length=256)
  # Indicates whether or not the partner location has restricted access. If it does then the access will be controlled by s_group_partner_location.
  Restricted = models.BooleanField(default=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_partner_location_pk', fields=['Partner', 'Location']),
    ]

class PPartnerAttribute(models.Model):
  """
  Mainly introduced for Partner Contact Details like email addresses and (mobile) phone numbers, but can be used for any attribute we might want to save for a Partner.
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PPartnerAttribute_Partner", on_delete=models.CASCADE)
  # The Partner Attribute Type that the Partner Attribute that is assigned here has got.
  AttributeType = models.ForeignKey(PPartnerAttributeType, null=False, blank=False, related_name="PPartnerAttribute_AttributeType", on_delete=models.CASCADE)
  # A normal sequence so that each partner can have more than one value for any particular attribute type.
  Sequence = models.IntegerField(default=0, null=False, blank=False)
  # Allows for manual ordering of Partner Attributes within a Partner Attribute Type by the user (e.g. re-ordering of phone numbers within the 'Phone Number' Partner Attribute Type).
  Index = models.IntegerField(null=False, blank=False)
  # The value of the attribute.
  Value = models.CharField(max_length=200, null=False, blank=False)
  # The country of the value of the attribute (only relevant for Telephone and Fax Numbers).
  ValueCountry = models.ForeignKey(PCountry, related_name="PPartnerAttribute_ValueCountry", on_delete=models.CASCADE)
  # Any comment to explain this attribute value, or some additional info that may be required.
  Comment = models.CharField(max_length=200)
  # Flag to indicate whether this Partner Attribute is the primary one among several that have the same Partner Attribute Type.
  Primary = models.BooleanField(default=False, null=False, blank=False)
  # Flag to indicate whether this Partner Attribute is for use within The Organisation.
  WithinOrganisation = models.BooleanField(default=False, null=False, blank=False)
  # Flag to indicate whether this Partner Attribute is specialised. For Partner Contact Details this flag is set for work-related Partner Attribute Types. The label is set in p_partner_attribute_type.p_special_label_c, eg. Business
  Specialised = models.BooleanField(default=False, null=False, blank=False)
  # Flag to indicate whether this Partner Attribute is confidential.
  Confidential = models.BooleanField(default=False, null=False, blank=False)
  # Flag to indicate whether this Partner Attribute is current.
  Current = models.BooleanField(default=True, null=False, blank=False)
  # When this Partner Attribute value is no longer current from.
  NoLongerCurrentFrom = models.DateTimeField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_partner_attribute_pk', fields=['Partner', 'AttributeType', 'Sequence']),
    ]

class PUnit(models.Model):
  """
  Details of a unit.  This is an organizational unit such as an om field, department, local cost center, etc.
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PUnit_Partner", on_delete=models.CASCADE)
  Name = models.CharField(max_length=80)
  Description = models.CharField(max_length=500)
  UnitType = models.ForeignKey(UUnitType, related_name="PUnit_UnitType", on_delete=models.CASCADE)
  # Indicates the minimum number of staff required. <br/>(Computed from um_jobs.)
  Minimum = models.IntegerField(default=0)
  # Indicates the maximum number of staff required. <br/>(Computed from um_jobs.)
  Maximum = models.IntegerField(default=0)
  # Indicates the present number on staff. <br/>(Computed from um_jobs.)
  Present = models.IntegerField(default=0)
  # Number of part-timers acceptable. <br/>(Computed from um_jobs.)
  PartTimers = models.IntegerField(default=0)
  # todo
  OutreachCode = models.CharField(max_length=13)
  # This is the cost of the outreach/Event
  OutreachCost = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # This is the currency that is used for the outreach cost.
  OutreachCostCurrency = models.ForeignKey(ACurrency, related_name="PUnit_OutreachCostCurrency", on_delete=models.CASCADE)
  # This is a code which identifies a country. <br/>It is the ISO code
  Country = models.ForeignKey(PCountry, related_name="PUnit_Country", on_delete=models.CASCADE)
  # The partner key of the office that will be this field's primary office..
  PrimaryOffice = models.ForeignKey(PPartner, null=False, blank=False, related_name="PUnit_PrimaryOffice", on_delete=models.CASCADE)


class UmUnitStructure(models.Model):
  """
  This contains parent/child relationships.
  """

  # This is an alias of the partner key. This is used to identify parent-child relationships. It consists of the fund id followed <br/>by a computer generated six digit number.
  ParentUnit = models.ForeignKey(PUnit, null=False, blank=False, related_name="UmUnitStructure_ParentUnit", on_delete=models.CASCADE)
  # This is an alias of the partner key. This is used to identify parent-child relationships. It consists of the fund id followed <br/>by a computer generated six digit number.
  ChildUnit = models.ForeignKey(PUnit, null=False, blank=False, related_name="UmUnitStructure_ChildUnit", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='um_unit_structure_pk', fields=['ParentUnit', 'ChildUnit']),
    ]

class PFamily(models.Model):
  """
  Contains details about a family in Partnership with us.  May have P_Person records linked to it.
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PFamily_Partner", on_delete=models.CASCADE)
  # Flag is set if there are family members with their own records in the p_person table. IMPORTANT: Don't rely on this flag anymore but determine this state on-the-fly! Reason: The value of this field isn't maintained reliably any more and the field will be removed in a future version of the DB!
  FamilyMembers = models.BooleanField(default=False)
  # How the family is to be addressed
  Title = models.CharField(max_length=32)
  FirstName = models.CharField(max_length=48)
  Name = models.CharField(max_length=60)
  # Flag is set if there are different surnames entered for husband and wife
  DifferentSurnames = models.BooleanField(default=False)
  MaritalStatus = models.ForeignKey(PtMaritalStatus, related_name="PFamily_MaritalStatus", on_delete=models.CASCADE)
  MaritalStatusSince = models.DateTimeField()
  MaritalStatusComment = models.CharField(max_length=256)
  # This is the date the person was born
  DateOfBirth = models.DateTimeField()
  Gender = models.CharField(max_length=8, default='Unknown')
  # A photo of the person, encoded with Base64, and prefixed with the file type


class PPerson(models.Model):
  """
  DEPRECATED. USE P_FAMILY INSTEAD. Details of a person. A person must also have a related FAMILY class p_partner record.
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PPerson_Partner", on_delete=models.CASCADE)
  Title = models.CharField(max_length=32)
  FirstName = models.CharField(max_length=32)
  PreferedName = models.CharField(max_length=32)
  MiddleName1 = models.CharField(max_length=32)
  MiddleName2 = models.CharField(max_length=32)
  MiddleName3 = models.CharField(max_length=32)
  FamilyName = models.CharField(max_length=32)
  Decorations = models.CharField(max_length=32)
  # This is the date the person was born
  DateOfBirth = models.DateTimeField()
  Gender = models.CharField(max_length=8, default='Unknown')
  MaritalStatus = models.ForeignKey(PtMaritalStatus, related_name="PPerson_MaritalStatus", on_delete=models.CASCADE)
  Occupation = models.ForeignKey(POccupation, related_name="PPerson_Occupation", on_delete=models.CASCADE)
  # A cross reference to the family record of this person. <br/>It should be set to ? (not 0 because such a record does not exist!) when there is no family record.
  Family = models.ForeignKey(PFamily, related_name="PPerson_Family", on_delete=models.CASCADE)
  # This field indicates the family id of the individual. <br/>ID's 0 and 1 are used for parents; 2, 3, 4 ... 9 are used for children.
  FamilyId = models.IntegerField(default=0, null=False, blank=False)
  # A person's academic title such as BSc(Hons) or Prof. (eg. Herr Prof. Klaus Shmitt)
  AcademicTitle = models.CharField(max_length=24)
  MaritalStatusSince = models.DateTimeField()
  MaritalStatusComment = models.CharField(max_length=256)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_person_uq', fields=['Family', 'FamilyId']),
    ]

class PChurch(models.Model):
  """
  Specific information about a church which is a partner
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PChurch_Partner", on_delete=models.CASCADE)
  Name = models.CharField(max_length=80)
  # Number of people in regular attendance.
  ApproximateSize = models.IntegerField(default=0)
  Denomination = models.ForeignKey(PDenomination, related_name="PChurch_Denomination", on_delete=models.CASCADE)
  Accomodation = models.BooleanField(default=False)
  PrayerGroup = models.BooleanField(default=False)
  # Paper (Digital?) Map of church is on file at Site
  MapOnFile = models.BooleanField(default=False)
  AccomodationType = models.CharField(max_length=8, default='OTHER')
  AccomodationSize = models.IntegerField(default=0)
  # Generally the contact person for the unit who will be addressed in any correspondence
  ContactPartner = models.ForeignKey(PPartner, related_name="PChurch_ContactPartner", on_delete=models.CASCADE)


class POrganisation(models.Model):
  """
  Details of an organisation
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="POrganisation_Partner", on_delete=models.CASCADE)
  Name = models.CharField(max_length=80)
  Business = models.ForeignKey(PBusiness, related_name="POrganisation_Business", on_delete=models.CASCADE)
  Religious = models.BooleanField(default=False)
  # Generally the contact person for the unit who will be addressed in any correspondence
  ContactPartner = models.ForeignKey(PPartner, related_name="POrganisation_ContactPartner", on_delete=models.CASCADE)
  Foundation = models.BooleanField(default=False)


class PBank(models.Model):
  """
  Details of an bank
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PBank_Partner", on_delete=models.CASCADE)
  BranchName = models.CharField(max_length=80)
  # Generally the contact person for the unit who will be addressed in any correspondence
  ContactPartner = models.ForeignKey(PPartner, related_name="PBank_ContactPartner", on_delete=models.CASCADE)
  # The bank code/branch code/sort code (synonymous country-specific terms) for identifying a bank branch with a number/code.
  BranchCode = models.CharField(max_length=10)
  # BIC (Bank Identifier Code)/SWIFT code. The Bank Identifier Code is a unique address which, in telecommunication messages, identifies precisely the financial institutions involved in financial transactions. BICs either have 8 or 11 characters.
  Bic = models.CharField(max_length=11)
  # The format file to be used for electronic payment
  EpFormatFile = models.CharField(max_length=48)
  # Is this a credit card type (eg. VISA)?
  CreditCard = models.BooleanField(default=False)


class PVenue(models.Model):
  """
  Details of a venue
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PVenue_Partner", on_delete=models.CASCADE)
  Name = models.CharField(max_length=80)
  Code = models.CharField(max_length=8, null=False, blank=False)
  # This is the currency that is used for the venue.
  Currency = models.ForeignKey(ACurrency, related_name="PVenue_Currency", on_delete=models.CASCADE)
  # Generally the contact person for the unit who will be addressed in any correspondence
  ContactPartner = models.ForeignKey(PPartner, related_name="PVenue_ContactPartner", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_venue_uk', fields=['Code']),
    ]

class PBankingDetails(models.Model):
  """
  Any bank details for a partner can be stored in this table
  """

  # A sequence key for the banking details.
  BankingDetailsKey = models.IntegerField(null=False, blank=False, unique=True)
  # The type of banking: BANK ACCOUNT, CREDIT CARD, etc.
  BankingType = models.ForeignKey(PBankingType, null=False, blank=False, related_name="PBankingDetails_BankingType", on_delete=models.CASCADE)
  # The full name used for authorizing a transaction with this banking entity.
  AccountName = models.CharField(max_length=80)
  Title = models.CharField(max_length=32)
  FirstName = models.CharField(max_length=32)
  MiddleName = models.CharField(max_length=32)
  LastName = models.CharField(max_length=32)
  # Link to p_bank to see what details the bank has.
  Bank = models.ForeignKey(PBank, null=False, blank=False, related_name="PBankingDetails_Bank", on_delete=models.CASCADE)
  # The account number in the bank
  BankAccountNumber = models.CharField(max_length=20)
  # The IBAN (International Bank Account Number). IBAN is a standardised international format for entering account details which consists of the country code, the local bank code, the (payee) account number and a control number.
  Iban = models.CharField(max_length=64)
  # Credit Card Security Code
  SecurityCode = models.CharField(max_length=12)
  # When the credit card is valid from
  ValidFromDate = models.DateTimeField()
  # When this expires
  ExpiryDate = models.DateTimeField()
  # This is the finance details comment.
  Comment = models.CharField(max_length=255)


class PPartnerBankingDetails(models.Model):
  """
  Links p_partner table with p_banking_details table for many to many relationship
  """

  # The partner to link with
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PPartnerBankingDetails_Partner", on_delete=models.CASCADE)
  # The banking details to link with
  BankingDetails = models.ForeignKey(PBankingDetails, null=False, blank=False, related_name="PPartnerBankingDetails_BankingDetails", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_partner_banking_link_pk', fields=['Partner', 'BankingDetails']),
    ]

class PBankingDetailsUsage(models.Model):
  """
  Links p_partner - p_banking_details combination to a usage type
  """

  PartnerBankingDetails = models.ForeignKey(PPartnerBankingDetails, null=False, blank=False, related_name="PBankingDetailsUsage_PartnerBankingDetails", on_delete=models.CASCADE)
  # Reference to the usage type.
  Type = models.ForeignKey(PBankingDetailsUsageType, null=False, blank=False, related_name="PBankingDetailsUsage_Type", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_banking_details_usage_pk', fields=['PartnerBankingDetails', 'Type']),
    ]

class PPartnerTaxDeductiblePct(models.Model):
  """
  Specifies the percentage of incoming gifts to this recipient that can be considered tax deductible
  """

  # Partner Key of recipient to which this percentage applies
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PPartnerTaxDeductiblePct_Partner", on_delete=models.CASCADE)
  # The date from which this percentage is valid
  DateValidFrom = models.DateTimeField(null=False, blank=False)
  # The percentage of incoming gifts to this recipient that should be considered tax deductible
  PercentageTaxDeductible = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_partner_tax_deductible_pct_pk', fields=['Partner', 'DateValidFrom']),
    ]

class PPartnerType(models.Model):
  """
  Types assigned to each partner.  Also known as special types.
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PPartnerType_Partner", on_delete=models.CASCADE)
  # This code identifies the type
  Type = models.ForeignKey(PType, null=False, blank=False, related_name="PPartnerType_Type", on_delete=models.CASCADE)
  # The date the special type is valid from. Can be NULL if there is no relevant start date.
  ValidFrom = models.DateTimeField()
  # The date the special type is valid to. Can be NULL if there is no end date.
  ValidUntil = models.DateTimeField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_partner_type_pk', fields=['Partner', 'Type']),
    ]

class PPartnerRelationship(models.Model):
  """
  Relationships between pairs of partners.  Among other relationships, this also relates the FAMILY class partners to the PERSON class partners to indicate members of a family.
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PPartnerRelationship_Partner", on_delete=models.CASCADE)
  # This code identifies the relation
  Relation = models.ForeignKey(PRelation, null=False, blank=False, related_name="PPartnerRelationship_Relation", on_delete=models.CASCADE)
  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Relation = models.ForeignKey(PPartner, null=False, blank=False, related_name="PPartnerRelationship_Relation", on_delete=models.CASCADE)
  Comment = models.CharField(max_length=1000)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_partner_relationship_pk', fields=['Partner', 'Relation', 'Relation']),
    ]

class PPartnerLedger(models.Model):
  """
  Used to keep track of partner keys
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PUnit, null=False, blank=False, related_name="PPartnerLedger_Partner", on_delete=models.CASCADE)
  LastPartnerId = models.IntegerField(default=0, null=False, blank=False)


class MExtract(models.Model):
  """
  Contains the list of partners in each mailing extract
  """

  # Identifier for the extract
  Extract = models.ForeignKey(MExtractMaster, null=False, blank=False, related_name="MExtract_Extract", on_delete=models.CASCADE)
  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="MExtract_Partner", on_delete=models.CASCADE)
  # This is the key that tell what site created the linked location
  SiteKey = models.IntegerField(default=0, null=False, blank=False)
  Location = models.ForeignKey(PLocation, null=False, blank=False, related_name="MExtract_Location", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='m_extract_pk', fields=['Extract', 'Partner']),
    ]

class PCustomisedGreeting(models.Model):
  """
  Specific greetings from a user to a partner
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PCustomisedGreeting_Partner", on_delete=models.CASCADE)
  # This is the system user id. Each user of the system is allocated one
  User = models.ForeignKey(SUser, null=False, blank=False, related_name="PCustomisedGreeting_User", on_delete=models.CASCADE)
  CustomisedGreetingText = models.CharField(max_length=32)
  CustomisedClosingText = models.CharField(max_length=32)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_customised_greeting_pk', fields=['Partner', 'User']),
    ]

class PSubscription(models.Model):
  """
  Details of which partners receive which publications.
  """

  # The is the key to the publication table
  Publication = models.ForeignKey(PPublication, null=False, blank=False, related_name="PSubscription_Publication", on_delete=models.CASCADE)
  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PSubscription_Partner", on_delete=models.CASCADE)
  PublicationCopies = models.IntegerField(default=1)
  ReasonSubsGiven = models.ForeignKey(PReasonSubscriptionGiven, null=False, blank=False, related_name="PSubscription_ReasonSubsGiven", on_delete=models.CASCADE)
  ReasonSubsCancelled = models.ForeignKey(PReasonSubscriptionCancelled, related_name="PSubscription_ReasonSubsCancelled", on_delete=models.CASCADE)
  # Date the subscription expires
  ExpiryDate = models.DateTimeField()
  # Provisional date on which the subscription may expire
  ProvisionalExpiryDate = models.DateTimeField()
  GratisSubscription = models.BooleanField(default=True, null=False, blank=False)
  DateNoticeSent = models.DateTimeField()
  DateCancelled = models.DateTimeField()
  StartDate = models.DateTimeField(null=False, blank=False)
  NumberIssuesReceived = models.IntegerField(default=0, null=False, blank=False)
  # The number of issues sent after a subscription has ceased
  NumberComplimentary = models.IntegerField(default=1, null=False, blank=False)
  SubscriptionRenewalDate = models.DateTimeField()
  SubscriptionStatus = models.CharField(max_length=12, default='PERMANENT')
  FirstIssue = models.DateTimeField()
  LastIssue = models.DateTimeField()
  GiftFrom = models.ForeignKey(PPartner, related_name="PSubscription_GiftFrom", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_subscription_pk', fields=['Publication', 'Partner']),
    ]

class PPartnerContact(models.Model):
  """
  Link between Partners and Contacts
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PPartnerContact_Partner", on_delete=models.CASCADE)
  # This is the contact log id.
  ContactLog = models.ForeignKey(PContactLog, null=False, blank=False, related_name="PPartnerContact_ContactLog", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_partner_contact_pk', fields=['Partner', 'ContactLog']),
    ]

class AAccount(models.Model):
  """
  Details about each account code within a ledger. Also holds information on the summary account structure for reporting.
  """

  # This is used as a key field in most of the accounting system files
  Ledger = models.ForeignKey(ALedger, null=False, blank=False, related_name="AAccount_Ledger", on_delete=models.CASCADE)
  # This identifies the account the financial transaction must be stored against
  Code = models.CharField(max_length=8, null=False, blank=False)
  # Income, Expense, Asset, Liability, Equity.  Suspense accounts are in a_suspense_account.
  AccountType = models.CharField(max_length=10)
  # This is a long description and is 80 characters long.
  CodeLongDesc = models.CharField(max_length=80)
  # This is a short description which is 32 charcters long
  CodeShortDesc = models.CharField(max_length=32)
  # This is a short description which is 32 charcters long
  EngAccountCodeShortDesc = models.CharField(max_length=32)
  # This is a long description and is 80 characters long.
  EngAccountCodeLongDesc = models.CharField(max_length=80)
  # Defines if the the transcation is a debit or credit transaction
  DebitCreditIndicator = models.BooleanField()
  # Defines whether the acount is active or not
  AccountActive = models.BooleanField()
  # Yes if the account has any analysis attributes.
  AnalysisAttribute = models.BooleanField(default=False)
  StandardAccount = models.BooleanField(default=False)
  ConsolidationAccount = models.BooleanField(default=False)
  IntercompanyAccount = models.BooleanField(default=False)
  # The type of budget.  See the a_budget_type table.
  BudgetType = models.ForeignKey(ABudgetType, related_name="AAccount_BudgetType", on_delete=models.CASCADE)
  PostingStatus = models.BooleanField()
  SystemAccount = models.BooleanField(default=False)
  BudgetControl = models.BooleanField(default=False)
  # Which type of cost centres may be combined with this account.
  ValidCcCombo = models.CharField(max_length=8, default='All')
  UseForeignCurrency = models.BooleanField(default=False)
  # This defines which currency is being used
  ForeignCurrency = models.ForeignKey(ACurrency, related_name="AAccount_ForeignCurrency", on_delete=models.CASCADE)
  # Link to banking details to use for this account - only really used if this account is a bank account
  BankingDetails = models.ForeignKey(PBankingDetails, related_name="AAccount_BankingDetails", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_account_pk', fields=['Ledger', 'Code']),
    ]

class AEpStatement(models.Model):
  """
  List of recently imported bank statements
  """

  # auto generated unique identifier for bank statements
  StatementKey = models.IntegerField(null=False, blank=False, unique=True)
  # this is the bank account that this statement is for; this is necessary because you can have several accounts at the same bank
  BankAccount = models.ForeignKey(PBankingDetails, related_name="AEpStatement_BankAccount", on_delete=models.CASCADE)
  # The date of this statement
  Date = models.DateTimeField(null=False, blank=False)
  # This is the ID that the bank uses for this statement; it can be used to find the paper version of the bank statement
  IdFromBank = models.CharField(max_length=20)
  # This is the name of the file that this statement was read from; this can be used to prevent duplicate import of bank statements
  Filename = models.CharField(max_length=20)
  # The start balance of the bank account at the beginning of the statement
  StartBalance = models.DecimalField(max_digits=24, decimal_places=10)
  # The end balance of the bank account after the statement
  EndBalance = models.DecimalField(max_digits=24, decimal_places=10)
  # This defines the currency of the transactions on this statement
  Currency = models.ForeignKey(ACurrency, null=False, blank=False, related_name="AEpStatement_Currency", on_delete=models.CASCADE)
  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="AEpStatement_Account", on_delete=models.CASCADE)


class AAccountProperty(models.Model):
  """
  Properties and optional values for an account can be saved in this table.
  """

  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="AAccountProperty_Account", on_delete=models.CASCADE)
  # Code for the property
  Property = models.ForeignKey(AAccountPropertyCode, null=False, blank=False, related_name="AAccountProperty_Property", on_delete=models.CASCADE)
  # value of this property
  PropertyValue = models.CharField(max_length=100, null=False, blank=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_account_property_pk', fields=['Account', 'Property', 'PropertyValue']),
    ]

class AAccountHierarchy(models.Model):
  """
  hierarchy of accounts; what is the root account of the hierarchy
  """

  LedgerNumber = models.IntegerField(null=False, blank=False)
  # The code for the hierarchy
  Code = models.CharField(max_length=8, null=False, blank=False)
  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="AAccountHierarchy_Account", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_account_hierarchy_pk', fields=['Code']),
    ]

class AAccountHierarchyDetail(models.Model):
  """
  the elements of the hierarchy of accounts; which account is reporting to which other account
  """

  AccountHierarchy = models.ForeignKey(AAccountHierarchy, null=False, blank=False, related_name="AAccountHierarchyDetail_AccountHierarchy", on_delete=models.CASCADE)
  # The reporting account
  ReportingAccountCode = models.CharField(max_length=8, null=False, blank=False)
  # Order to display the account or heading on the Balance Sheet & Income Statement report.
  ReportOrder = models.IntegerField(default=0, null=False, blank=False)
  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="AAccountHierarchyDetail_Account", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_account_hierarchy_detail_pk', fields=['AccountHierarchy']),
    ]

class AValidLedgerNumber(models.Model):
  """
  List of foreign ledgers (eg, other fields) which the local ledger may send transctions to.
  """

  # This is used as a key field in most of the accounting system files .It is created from the first 4 digits of a partner key of type ""ledger"".
  Ledger = models.ForeignKey(ALedger, null=False, blank=False, related_name="AValidLedgerNumber_Ledger", on_delete=models.CASCADE)
  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="AValidLedgerNumber_Partner", on_delete=models.CASCADE)
  # The ledger through which inter ledger transactions are routed for processing.
  IltProcessingCentre = models.ForeignKey(PPartner, related_name="AValidLedgerNumber_IltProcessingCentre", on_delete=models.CASCADE)
  CostCentre = models.ForeignKey(ACostCentre, null=False, blank=False, related_name="AValidLedgerNumber_CostCentre", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_valid_ledger_number_pk', fields=['Partner']),
    ]

class ABudget(models.Model):
  """
  Budget information for cost centre-account combinations.
  """

  BudgetSequence = models.IntegerField(null=False, blank=False, unique=True)
  # See a_budget_type table.  Indicates the method used for creating the budget.
  BudgetType = models.ForeignKey(ABudgetType, null=False, blank=False, related_name="ABudget_BudgetType", on_delete=models.CASCADE)
  # Has the budget been ""posted"" to the general ledger master <br/>and account files.
  BudgetStatus = models.BooleanField()
  # A comment for this specific budget item and revision
  Comment = models.CharField(max_length=100)
  CostCentre = models.ForeignKey(ACostCentre, null=False, blank=False, related_name="ABudget_CostCentre", on_delete=models.CASCADE)
  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="ABudget_Account", on_delete=models.CASCADE)
  BudgetRevision = models.ForeignKey(ABudgetRevision, null=False, blank=False, related_name="ABudget_BudgetRevision", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_budget_uc1', fields=['BudgetRevision']),
    ]

class ABudgetPeriod(models.Model):
  """
  This is the budget data for one period (e.g. a month)
  """

  BudgetSequence = models.ForeignKey(ABudget, null=False, blank=False, related_name="ABudgetPeriod_BudgetSequence", on_delete=models.CASCADE)
  PeriodNumber = models.IntegerField(default=0, null=False, blank=False)
  # Budget amount in base currency
  BudgetBase = models.DecimalField(max_digits=24, decimal_places=10, default=0)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_budget_period_pk', fields=['BudgetSequence', 'PeriodNumber']),
    ]

class AAnalysisAttribute(models.Model):
  """
  Indicates which accounts use analysis attributes and what attribute types may be used with the account.   Analysis attributes are user-definable extra information to be stored against an account.
  """

  AnalysisType = models.ForeignKey(AAnalysisType, null=False, blank=False, related_name="AAnalysisAttribute_AnalysisType", on_delete=models.CASCADE)
  # This identifies the account the financial transaction analysis information must be stored against.
  AccountCode = models.CharField(max_length=8, null=False, blank=False)
  # Analysis attributes cannot be deleted, because they are needed for existing transaction analysis attributes. But they can be deactivated.
  Active = models.BooleanField(default=True)
  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="AAnalysisAttribute_Account", on_delete=models.CASCADE)
  CostCentre = models.ForeignKey(ACostCentre, null=False, blank=False, related_name="AAnalysisAttribute_CostCentre", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_analysis_attribute_pk', fields=['AnalysisType']),
    ]

class AEmailDestination(models.Model):
  """
  Where Petra supports it a cross reference between a file and destination can be established for automatic distribution.
  """

  # A code to describe the file which is to be distributed via email.
  FileCode = models.CharField(max_length=20, null=False, blank=False)
  # Foriegn Cost Centre Code.
  ConditionalValue = models.CharField(max_length=20, null=False, blank=False)
  # HOSA partner.
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="AEmailDestination_Partner", on_delete=models.CASCADE)
  EmailAddress = models.CharField(max_length=318)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_email_destination_pk', fields=['FileCode', 'ConditionalValue', 'Partner']),
    ]

class AFeesPayable(models.Model):
  """
  Fees owed to another ledger. (e.g. admin grant)
  """

  # This is used as a key field in most of the accounting system files
  LedgerNumber = models.IntegerField(default=0, null=False, blank=False)
  # Identifies a specific fee.
  FeeCode = models.CharField(max_length=8, null=False, blank=False)
  ChargeOption = models.CharField(max_length=20, null=False, blank=False)
  ChargePercentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
  # This is a the max or min amount charged dependent on the charge option.  The value is the number of currency units.
  ChargeAmount = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # explain what this fee is for.
  FeeDescription = models.CharField(max_length=24)
  CostCentre = models.ForeignKey(ACostCentre, null=False, blank=False, related_name="AFeesPayable_CostCentre", on_delete=models.CASCADE)
  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="AFeesPayable_Account", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_fees_payable_pk', fields=['FeeCode']),
    ]

class AFeesReceivable(models.Model):
  """
  Charges to collect from other ledgers. (e.g. office admin fee)
  """

  # This is used as a key field in most of the accounting system files
  LedgerNumber = models.IntegerField(default=0, null=False, blank=False)
  # Identifies a specific fee.
  FeeCode = models.CharField(max_length=8, null=False, blank=False)
  ChargeOption = models.CharField(max_length=20, null=False, blank=False)
  ChargePercentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
  # This is a the max or min amount charged dependent on the charge option in number of currency units
  ChargeAmount = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Description of what this admin charge is for.
  FeeDescription = models.CharField(max_length=24)
  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="AFeesReceivable_Account", on_delete=models.CASCADE)
  CostCentre = models.ForeignKey(ACostCentre, null=False, blank=False, related_name="AFeesReceivable_CostCentre", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_fees_receivable_pk', fields=['FeeCode']),
    ]

class AGeneralLedgerMaster(models.Model):
  """
  All balances on accounts, including summary information is stored here.
  """

  GlmSequence = models.IntegerField(null=False, blank=False, unique=True)
  # The year is a number starting from 0 (the year of the installation and first accountings).
  Year = models.IntegerField(null=False, blank=False)
  YtdActualBase = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Special period for the year end close journal.
  ClosingPeriodActualBase = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Starting Balance in the ledger currency
  StartBalanceBase = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Total for the current year, 2nd (int'l) base currency.
  YtdActualIntl = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Special period for the year end close journal.
  ClosingPeriodActualIntl = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Starting Balance (Int'l)
  StartBalanceIntl = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  YtdActualForeign = models.DecimalField(max_digits=24, decimal_places=10)
  StartBalanceForeign = models.DecimalField(max_digits=24, decimal_places=10)
  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="AGeneralLedgerMaster_Account", on_delete=models.CASCADE)
  CostCentre = models.ForeignKey(ACostCentre, null=False, blank=False, related_name="AGeneralLedgerMaster_CostCentre", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_general_ledger_master_uc1', fields=['Year']),
    ]

class AGeneralLedgerMasterPeriod(models.Model):
  """
  The General Ledger Master data for one period (e.g. a month)
  """

  GlmSequence = models.ForeignKey(AGeneralLedgerMaster, null=False, blank=False, related_name="AGeneralLedgerMasterPeriod_GlmSequence", on_delete=models.CASCADE)
  PeriodNumber = models.IntegerField(null=False, blank=False)
  # This is a number of ledger currency units
  ActualBase = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # This is a number of ledger currency units
  BudgetBase = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Not supported in Openpetra anymore ...
  ActualIntl = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Not supported in Openpetra anymore ...
  BudgetIntl = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  ActualForeign = models.DecimalField(max_digits=24, decimal_places=10)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_glm_period_pk', fields=['GlmSequence', 'PeriodNumber']),
    ]

class AMotivationDetail(models.Model):
  """
  Used as a subdvision of motivation group. Details of the reason money has been received, where it is going (cost centre and account), and fees to be charged on it.
  """

  MotivationGroup = models.ForeignKey(AMotivationGroup, null=False, blank=False, related_name="AMotivationDetail_MotivationGroup", on_delete=models.CASCADE)
  # This defines the motivation detail within a motivation group.
  Code = models.CharField(max_length=8, null=False, blank=False)
  # This is a long description and is 80 characters long.
  MotivationDetailAudience = models.CharField(max_length=80)
  # This is a long description and is 80 characters long.
  Desc = models.CharField(max_length=80, null=False, blank=False)
  # Defines whether the motivation code is still in use
  MotivationStatus = models.BooleanField(null=False, blank=False)
  # This is a number of currency units
  MailingCost = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Used to get a yes no response from the user
  BulkRate = models.BooleanField(default=False, null=False, blank=False)
  # This defines what should happen next
  NextResponseStatus = models.CharField(max_length=12)
  # Used to get a yes no response from the user
  ActivatePartner = models.BooleanField(default=False, null=False, blank=False)
  # The number of items sent out in a mailing
  NumberSent = models.IntegerField(default=0)
  # The number of items returned from a mailing
  NumberOfResponses = models.IntegerField(default=0)
  # The target number of items returned from a mailing
  TargetNumberOfResponses = models.IntegerField(default=0)
  # This is a number of currency units
  TargetAmount = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # This is a number of currency units
  AmountReceived = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # This is the partner key assigned to each partner. It consists of the ledger id followed by a computer generated six digit number.
  Recipient = models.ForeignKey(PPartner, null=False, blank=False, related_name="AMotivationDetail_Recipient", on_delete=models.CASCADE)
  # A flag to automatically populate the description in the gift comment
  Autopopdesc = models.BooleanField(default=False)
  # Whether receipts should be printed
  Receipt = models.BooleanField(default=True)
  # Don't include these gifts in reporting
  DontReport = models.BooleanField(default=False)
  # Whether this gift is tax deductible
  TaxDeductible = models.BooleanField(default=True)
  # This is a long description and is 80 characters long in the local language.
  MotivationDetailDescLocal = models.CharField(max_length=80)
  # A short code for the motivation which can then be used on receipts
  ShortCode = models.CharField(max_length=4)
  # Indicates whether or not the motivation has restricted access. If it does then the access will be controlled by s_group_motivation
  Restricted = models.BooleanField(default=False)
  # Whether or not gifts with this motivation should be exported to the worldwide Intranet (to help distinguish non-gifts like sales)
  ExportToIntranet = models.BooleanField(default=True)
  # Which column should these gifts be reported in?
  ReportColumn = models.CharField(max_length=20)
  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="AMotivationDetail_Account", on_delete=models.CASCADE)
  CostCentre = models.ForeignKey(ACostCentre, null=False, blank=False, related_name="AMotivationDetail_CostCentre", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_motivation_detail_pk', fields=['MotivationGroup', 'Code']),
    ]

class AEpAccount(models.Model):
  """
  This contains the settings for one specific bank account
  """

  # The bank account whose settings are defined here
  BankingDetails = models.ForeignKey(PBankingDetails, null=False, blank=False, related_name="AEpAccount_BankingDetails", on_delete=models.CASCADE)
  # This tells the plugin where to find the statement files for this bank account
  ImportfilePath = models.CharField(max_length=100)
  # This tells the plugin where to write any generated files for this bank account
  ExportfilePath = models.CharField(max_length=100)
  # This can be either the name of an executable or a DLL that is able to process the country (or bank) specific bank statements
  PluginFilename = models.CharField(max_length=100)
  # Other parameters for the plugin can be stored here
  PluginParameters = models.CharField(max_length=250)
  # if this is true, all gifts to this bank account get this flag set
  ConfidentialGift = models.BooleanField()
  # Whether the gifts to this bank account are tax deductible
  TaxDeductible = models.BooleanField(default=True)
  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="AEpAccount_Account", on_delete=models.CASCADE)
  MotivationDetail = models.ForeignKey(AMotivationDetail, null=False, blank=False, related_name="AEpAccount_MotivationDetail", on_delete=models.CASCADE)


class AEpMatch(models.Model):
  """
  the matches that can be used to identify recurring gift or GL transactions
  """

  # this is a sequence to easily identify which transaction has been matched and how
  EpMatchKey = models.IntegerField(null=False, blank=False, unique=True)
  # this is a separated list of all the recurring details of a_ep_transaction (ie. name, bank account, sort code, IBAN, amount, description)
  MatchText = models.CharField(max_length=100, null=False, blank=False)
  # the match can be applied to split gifts as well
  Detail = models.IntegerField(default=0, null=False, blank=False)
  # What to do with this match: gift, GL, or discard
  Action = models.CharField(max_length=20, null=False, blank=False)
  # The date when this match was recently applied; useful for purging old entries
  RecentMatch = models.DateTimeField(null=False, blank=False)
  # The partner key of the commitment field (the unit) of the recipient of the gift.  This is not the ledger number but rather the partner key of the unit associated with the ledger.
  RecipientLedgerNumber = models.ForeignKey(PPartner, related_name="AEpMatch_RecipientLedgerNumber", on_delete=models.CASCADE)
  # Used to decide whose reports will see this comment
  CommentOneType = models.CharField(max_length=12)
  # This is a long description and is 80 characters long.
  GiftCommentOne = models.CharField(max_length=80)
  # Defines whether the donor wishes the recipient to know who gave the gift
  ConfidentialGift = models.BooleanField(null=False, blank=False)
  # Whether this gift is tax deductaible
  TaxDeductible = models.BooleanField(default=True)
  # The partner key of the recipient of the gift.
  Recipient = models.ForeignKey(PPartner, null=False, blank=False, related_name="AEpMatch_Recipient", on_delete=models.CASCADE)
  # To determine whether an admin fee on the transaction should be overwritten if it normally has a charge associated with it. Used for both local and ilt transaction.
  Charge = models.BooleanField(default=True)
  # Mailing Code of the mailing that the gift was a response to.
  Mailing = models.ForeignKey(PMailing, related_name="AEpMatch_Mailing", on_delete=models.CASCADE)
  # Used to decide whose reports will see this comment
  CommentTwoType = models.CharField(max_length=12)
  # This is a long description and is 80 characters long.
  GiftCommentTwo = models.CharField(max_length=80)
  # Used to decide whose reports will see this comment
  CommentThreeType = models.CharField(max_length=12)
  # This is a long description and is 80 characters long.
  GiftCommentThree = models.CharField(max_length=80)
  # This is a number of currency units in the entered Currency
  GiftTransactionAmount = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # Used to get a yes no response from the user
  HomeAdminCharges = models.BooleanField(null=False, blank=False)
  # Used to get a yes no response from the user
  IltAdminCharges = models.BooleanField(null=False, blank=False)
  ReceiptLetterCode = models.CharField(max_length=10)
  # Defines how a gift is given.
  MethodOfGiving = models.ForeignKey(AMethodOfGiving, related_name="AEpMatch_MethodOfGiving", on_delete=models.CASCADE)
  # This is how the partner paid. Eg cash, Cheque etc
  MethodOfPayment = models.ForeignKey(AMethodOfPayment, related_name="AEpMatch_MethodOfPayment", on_delete=models.CASCADE)
  # This is the partner key of the donor.
  Donor = models.ForeignKey(PPartner, null=False, blank=False, related_name="AEpMatch_Donor", on_delete=models.CASCADE)
  # NOT USED AT ALL
  AdminCharge = models.BooleanField(default=False)
  Narrative = models.CharField(max_length=120)
  # Reference number/code for the transaction
  Reference = models.CharField(max_length=10)
  # short name of the donor; will be used for generating export files
  DonorShortName = models.CharField(max_length=250)
  # short name of recipient
  RecipientShortName = models.CharField(max_length=250)
  # Indicates whether or not the gift has restricted access. If it does then the access will be controlled by s_group_gift
  Restricted = models.BooleanField(default=False)
  # Key ministry to which this transaction applies (just for fund transfers)
  KeyMinistry = models.ForeignKey(PUnit, related_name="AEpMatch_KeyMinistry", on_delete=models.CASCADE)
  MotivationDetail = models.ForeignKey(AMotivationDetail, null=False, blank=False, related_name="AEpMatch_MotivationDetail", on_delete=models.CASCADE)
  CostCentre = models.ForeignKey(ACostCentre, null=False, blank=False, related_name="AEpMatch_CostCentre", on_delete=models.CASCADE)
  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="AEpMatch_Account", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_ep_match_uk', fields=['MatchText', 'Detail']),
    ]

class AEpTransaction(models.Model):
  """
  the transactions from the recently imported bank statements; they should help to identify the other party of the transaction (donor, etc) and the purpose of the transaction
  """

  # this transaction belongs to that statement
  Statement = models.ForeignKey(AEpStatement, null=False, blank=False, related_name="AEpTransaction_Statement", on_delete=models.CASCADE)
  # to complete the primary key
  Order = models.IntegerField(null=False, blank=False)
  # a transaction can be split in order to support mixed GL and Gift records
  DetailKey = models.IntegerField(default=-1, null=False, blank=False)
  # can be different from order, since the paper statements can have different order than the electronic statement
  NumberOnPaperStatement = models.IntegerField(default=-1)
  # this is a calculated text that uniquely identifies this transaction so that it can be recognised next month. TODO: should have a link table a_ep_match between a_ep_transaction and a_ep_match_detail
  MatchText = models.CharField(max_length=100)
  # This can be a summary of title, first name, last name etc. of the other party
  AccountName = models.CharField(max_length=80)
  Title = models.CharField(max_length=32)
  FirstName = models.CharField(max_length=32)
  MiddleName = models.CharField(max_length=32)
  # the name of the other party
  LastName = models.CharField(max_length=32)
  # The bank code/branch code/sort code of the other party.
  BranchCode = models.CharField(max_length=10)
  # BIC (Bank Identifier Code)/SWIFT code of the other party
  Bic = models.CharField(max_length=11)
  # The account number in the bank of the other party
  BankAccountNumber = models.CharField(max_length=20)
  # The IBAN (International Bank Account Number) of the other party.
  Iban = models.CharField(max_length=64)
  # This can be recurring income, recurring payment, income, payment, direct debit, etc.
  TransactionTypeCode = models.CharField(max_length=20)
  # The amount in the currency of the bank account
  TransactionAmount = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # This description was given when the transfer was initiated
  Description = models.CharField(max_length=256)
  # The date when this transaction became valid or available
  DateEffective = models.DateTimeField(null=False, blank=False)
  # set this value to the match (either new match or set automatically)
  EpMatch = models.ForeignKey(AEpMatch, related_name="AEpTransaction_EpMatch", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_ep_transaction_pk', fields=['Statement', 'Order', 'DetailKey']),
    ]

class AMotivationDetailFee(models.Model):
  """
  motivation details can have several fees
  """

  MotivationDetail = models.ForeignKey(AMotivationDetail, null=False, blank=False, related_name="AMotivationDetailFee_MotivationDetail", on_delete=models.CASCADE)
  FeeCode = models.CharField(max_length=8, null=False, blank=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_motivation_detail_fee_pk', fields=['MotivationDetail', 'FeeCode']),
    ]

class ATransactionType(models.Model):
  """
  Various ways a transaction may originate, depending on the subsystem.
  """

  # This is used as a key field in most of the accounting system files
  LedgerNumber = models.IntegerField(default=0, null=False, blank=False)
  # Defines a sub system of accounts
  SubSystem = models.ForeignKey(ASubSystem, null=False, blank=False, related_name="ATransactionType_SubSystem", on_delete=models.CASCADE)
  Code = models.CharField(max_length=8, null=False, blank=False)
  # Identifies a journal within a batch
  LastJournal = models.IntegerField(default=0, null=False, blank=False)
  # Identifies a journal within a batch
  LastRecurringJournal = models.IntegerField(default=0, null=False, blank=False)
  # This is a short description which is 32 charcters long
  TransactionTypeDescription = models.CharField(max_length=32, null=False, blank=False)
  BalancingAccountCode = models.CharField(max_length=12)
  # Is this transaction type a special transaction type or not?
  SpecialTransactionType = models.BooleanField(default=False)
  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="ATransactionType_Account", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_transaction_type_pk', fields=['SubSystem', 'Code']),
    ]

class ARecurringJournal(models.Model):
  """
  Templates of general ledger journals which are copied into the ledger with recurring general ledger batches.
  """

  RecurringBatch = models.ForeignKey(ARecurringBatch, null=False, blank=False, related_name="ARecurringJournal_RecurringBatch", on_delete=models.CASCADE)
  # Identifies a journal within a batch
  JournalNumber = models.IntegerField(default=0, null=False, blank=False)
  # This is a long description and is 80 characters long.
  JournalDescription = models.CharField(max_length=80, null=False, blank=False)
  # identifies the status of a batch
  JournalStatus = models.CharField(max_length=20, default='Unposted', null=False, blank=False)
  # This is a number of currency units
  JournalDebitTotal = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # This is a number of currency units
  JournalCreditTotal = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # This defines which accounting period is being used
  JournalPeriod = models.IntegerField(default=0)
  # Date the  batch comes into effect
  DateEffective = models.DateTimeField(null=False, blank=False)
  # This is how the partner paid. Eg cash, Cheque etc
  MethodOfPayment = models.ForeignKey(AMethodOfPayment, related_name="ARecurringJournal_MethodOfPayment", on_delete=models.CASCADE)
  LastTransactionNumber = models.IntegerField(default=0, null=False, blank=False)
  # The rate of exchange
  ExchangeRateToBase = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # This defines which currency is being used
  TransactionCurrency = models.ForeignKey(ACurrency, null=False, blank=False, related_name="ARecurringJournal_TransactionCurrency", on_delete=models.CASCADE)
  TransactionType = models.ForeignKey(ATransactionType, null=False, blank=False, related_name="ARecurringJournal_TransactionType", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_recurring_journal_pk', fields=['RecurringBatch', 'JournalNumber']),
    ]

class ARecurringTransaction(models.Model):
  """
  Templates of general ledger transactions which are copied into the ledger with general ledger batches.
  """

  RecurringJournal = models.ForeignKey(ARecurringJournal, null=False, blank=False, related_name="ARecurringTransaction_RecurringJournal", on_delete=models.CASCADE)
  # Identifies a transaction within a journal within a batch within a ledger
  TransactionNumber = models.IntegerField(default=0, null=False, blank=False)
  # Date the transaction took place
  TransactionDate = models.DateTimeField(null=False, blank=False)
  # This defines which currency is being used
  TransactionCurrency = models.ForeignKey(ACurrency, related_name="ARecurringTransaction_TransactionCurrency", on_delete=models.CASCADE)
  # This is a number of currency units
  TransactionAmount = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # This defines which currency is being used
  BaseCurrency = models.ForeignKey(ACurrency, related_name="ARecurringTransaction_BaseCurrency", on_delete=models.CASCADE)
  # The rate of exchange
  ExchangeRateToBase = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # This is a number of currency units
  AmountInBaseCurrency = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  AnalysisIndicator = models.BooleanField(default=False, null=False, blank=False)
  MethodOfPayment = models.ForeignKey(AMethodOfPayment, related_name="ARecurringTransaction_MethodOfPayment", on_delete=models.CASCADE)
  # This defines which accounting period is being used
  PeriodNumber = models.IntegerField(default=0)
  # Shows if the transaction has been reconciled or not
  Reconciled = models.BooleanField(default=False, null=False, blank=False)
  # Defines a sub system of accounts
  SubSystemCode = models.CharField(max_length=12)
  TransactionTypeCode = models.CharField(max_length=8)
  Narrative = models.CharField(max_length=120)
  Reference = models.CharField(max_length=8, null=False, blank=False)
  DateOfEntry = models.DateTimeField()
  User = models.ForeignKey(SUser, related_name="ARecurringTransaction_User", on_delete=models.CASCADE)
  DebitCreditIndicator = models.BooleanField(null=False, blank=False)
  # Has a transaction been posted yet
  TransactionStatus = models.BooleanField(default=False)
  # The header (eg, cashbook #) that the transaction is associated with.
  HeaderNumber = models.IntegerField(default=0)
  # The detail (within the header) that the transaction is associated with.
  DetailNumber = models.IntegerField(default=0)
  SubType = models.CharField(max_length=8)
  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="ARecurringTransaction_Account", on_delete=models.CASCADE)
  CostCentre = models.ForeignKey(ACostCentre, null=False, blank=False, related_name="ARecurringTransaction_CostCentre", on_delete=models.CASCADE)
  RecurringBatch = models.ForeignKey(ARecurringBatch, null=False, blank=False, related_name="ARecurringTransaction_RecurringBatch", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_recurring_transaction_pk', fields=['RecurringJournal', 'TransactionNumber']),
    ]

class ARecurringTransAnalAttrib(models.Model):
  """
  Detailed analysis information stored along with the recurring transaction template.
  """

  RecurringTransaction = models.ForeignKey(ARecurringTransaction, null=False, blank=False, related_name="ARecurringTransAnalAttrib_RecurringTransaction", on_delete=models.CASCADE)
  AnalysisTypeCode = models.CharField(max_length=8, null=False, blank=False)
  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="ARecurringTransAnalAttrib_Account", on_delete=models.CASCADE)
  AnalysisAttribute = models.ForeignKey(AAnalysisAttribute, null=False, blank=False, related_name="ARecurringTransAnalAttrib_AnalysisAttribute", on_delete=models.CASCADE)
  FreeformAnalysis = models.ForeignKey(AFreeformAnalysis, null=False, blank=False, related_name="ARecurringTransAnalAttrib_FreeformAnalysis", on_delete=models.CASCADE)
  CostCentre = models.ForeignKey(ACostCentre, null=False, blank=False, related_name="ARecurringTransAnalAttrib_CostCentre", on_delete=models.CASCADE)
  RecurringBatch = models.ForeignKey(ARecurringBatch, null=False, blank=False, related_name="ARecurringTransAnalAttrib_RecurringBatch", on_delete=models.CASCADE)
  RecurringJournal = models.ForeignKey(ARecurringJournal, null=False, blank=False, related_name="ARecurringTransAnalAttrib_RecurringJournal", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_recurring_trans_anal_attr_pk', fields=['RecurringTransaction']),
    ]

class ARecurringGiftBatch(models.Model):
  """
  Templates of gift batches which can be copied into the gift system.
  """

  # ledger number
  Ledger = models.ForeignKey(ALedger, null=False, blank=False, related_name="ARecurringGiftBatch_Ledger", on_delete=models.CASCADE)
  # Gift batch number
  BatchNumber = models.IntegerField(default=0, null=False, blank=False)
  # gift batch description
  BatchDescription = models.CharField(max_length=40)
  # hash total for the gift batch
  HashTotal = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # total for the gift batch
  BatchTotal = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # last gift number of the batch
  LastGiftNumber = models.IntegerField(default=0)
  # This defines which currency is being used
  Currency = models.ForeignKey(ACurrency, null=False, blank=False, related_name="ARecurringGiftBatch_Currency", on_delete=models.CASCADE)
  # What type of gift is this? a gift or a gift in kind generally
  GiftType = models.CharField(max_length=8, default='Gift', null=False, blank=False)
  # This is how the partner paid. EgCash, Cheque etc
  MethodOfPaymentCode = models.CharField(max_length=8)
  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="ARecurringGiftBatch_Account", on_delete=models.CASCADE)
  CostCentre = models.ForeignKey(ACostCentre, null=False, blank=False, related_name="ARecurringGiftBatch_CostCentre", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_recurring_gift_batch_pk', fields=['BatchNumber']),
    ]

class ARecurringGift(models.Model):
  """
  Templates of donor gift information which can be copied into the gift system with recurring gift batches.
  """

  RecurringGiftBatch = models.ForeignKey(ARecurringGiftBatch, null=False, blank=False, related_name="ARecurringGift_RecurringGiftBatch", on_delete=models.CASCADE)
  # Identifies a transaction within a journal within a batch within a ledger
  GiftTransactionNumber = models.IntegerField(default=0, null=False, blank=False)
  ReceiptLetterCode = models.CharField(max_length=8)
  # Defines how a gift is given
  MethodOfGiving = models.ForeignKey(AMethodOfGiving, related_name="ARecurringGift_MethodOfGiving", on_delete=models.CASCADE)
  # This is how the partner paid. Eg cash, Cheque etc
  MethodOfPayment = models.ForeignKey(AMethodOfPayment, related_name="ARecurringGift_MethodOfPayment", on_delete=models.CASCADE)
  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Donor = models.ForeignKey(PPartner, null=False, blank=False, related_name="ARecurringGift_Donor", on_delete=models.CASCADE)
  # Identifies the last gift detail entered
  LastDetailNumber = models.IntegerField(default=0, null=False, blank=False)
  # Reference number/code for the transaction
  Reference = models.CharField(max_length=8)
  # Bank or credit card account to use for making this gift transaction.
  BankingDetailsKey = models.IntegerField(default=0, null=False, blank=False)
  # This reference is a unique string that reflects the customer or contract and the date of the SEPA mandate
  SepaMandateReference = models.CharField(max_length=35)
  # The date the SEPA Mandate was given
  SepaMandateGiven = models.DateTimeField()
  # Status of the credit card transaction
  ChargeStatus = models.CharField(max_length=10)
  # The last date that a successfull direct debit or credit card charge occurred for this gift
  LastDebit = models.DateTimeField()
  # The day of the month to make the recurring gift
  DebitDay = models.IntegerField(default=0)
  # Whether the recurring gift should be made
  Active = models.BooleanField(default=True, null=False, blank=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_recurring_gift_pk', fields=['RecurringGiftBatch', 'GiftTransactionNumber']),
    ]

class ARecurringGiftDetail(models.Model):
  """
  Store recipient information for the recurring gift.
  """

  RecurringGift = models.ForeignKey(ARecurringGift, null=False, blank=False, related_name="ARecurringGiftDetail_RecurringGift", on_delete=models.CASCADE)
  # Identifies a gift
  DetailNumber = models.IntegerField(default=0, null=False, blank=False)
  # This is used as a key field in most of the accounting system files
  RecipientLedgerNumber = models.ForeignKey(PPartner, related_name="ARecurringGiftDetail_RecipientLedgerNumber", on_delete=models.CASCADE)
  # This is the amount in transaction currency. This field should be renamed to a_gift_transaction_amount_n, to be in analogy to a_gift_detail.a_gift_transaction_amount_n
  GiftAmount = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Used to decide whose reports will see this comment
  CommentOneType = models.CharField(max_length=12)
  # This is a long description and is 80 characters long.
  GiftCommentOne = models.CharField(max_length=80)
  # Defines whether the donor wishes the recipient to know who gave the gift
  ConfidentialGift = models.BooleanField(null=False, blank=False)
  # Whether this gift is tax deductible
  TaxDeductible = models.BooleanField(default=True)
  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Recipient = models.ForeignKey(PPartner, null=False, blank=False, related_name="ARecurringGiftDetail_Recipient", on_delete=models.CASCADE)
  # To determine whether an admin fee on the transaction should be overwritten if it normally has a charge associated with it. Used for both local and ilt transaction.
  Charge = models.BooleanField(default=True)
  # Mailing Code
  Mailing = models.ForeignKey(PMailing, related_name="ARecurringGiftDetail_Mailing", on_delete=models.CASCADE)
  # Used to decide whose reports will see this comment
  CommentTwoType = models.CharField(max_length=12)
  # This is a long description and is 80 characters long.
  GiftCommentTwo = models.CharField(max_length=80)
  # Used to decide whose reports will see this comment
  CommentThreeType = models.CharField(max_length=12)
  # This is a long description and is 80 characters long.
  GiftCommentThree = models.CharField(max_length=80)
  # Date that donor wants to begin giving this recurring donation
  StartDonations = models.DateTimeField()
  # Date that donor wants to stop giving this recurring donation
  EndDonations = models.DateTimeField()
  MotivationDetail = models.ForeignKey(AMotivationDetail, null=False, blank=False, related_name="ARecurringGiftDetail_MotivationDetail", on_delete=models.CASCADE)
  RecurringGiftBatch = models.ForeignKey(ARecurringGiftBatch, null=False, blank=False, related_name="ARecurringGiftDetail_RecurringGiftBatch", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_recurring_gift_detail_pk', fields=['RecurringGift', 'DetailNumber']),
    ]

class AGiftBatch(models.Model):
  """
  Information describing groups (batches) of gifts.
  """

  # ledger number
  Ledger = models.ForeignKey(ALedger, null=False, blank=False, related_name="AGiftBatch_Ledger", on_delete=models.CASCADE)
  # Gift batch number
  BatchNumber = models.IntegerField(default=0, null=False, blank=False)
  # gift batch description
  BatchDescription = models.CharField(max_length=40, null=False, blank=False)
  # date of user entry or last modification.
  ModificationDate = models.DateTimeField()
  # hash total for the gift batch
  HashTotal = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # total for the gift batch
  BatchTotal = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # last gift number of the batch
  LastGiftNumber = models.IntegerField(default=0)
  # Status of a gift batch: Unposted, Posted, Cancelled.
  BatchStatus = models.CharField(max_length=8, default='Unposted')
  # The accounting period that the batch belongs to.  Must be <= 20.
  BatchPeriod = models.IntegerField(default=0, null=False, blank=False)
  # The financial year that the batch belongs to.
  BatchYear = models.IntegerField(null=False, blank=False)
  # Effective date when posted to the general ledger.
  GlEffectiveDate = models.DateTimeField(null=False, blank=False)
  # This defines which currency is being used
  Currency = models.ForeignKey(ACurrency, null=False, blank=False, related_name="AGiftBatch_Currency", on_delete=models.CASCADE)
  # The rate of exchange
  ExchangeRateToBase = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # What type of gift is this? a gift or a gift in kind generally
  GiftType = models.CharField(max_length=8, default='Gift', null=False, blank=False)
  # This is how the partner paid. EgCash, Cheque etc
  MethodOfPaymentCode = models.CharField(max_length=8)
  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="AGiftBatch_Account", on_delete=models.CASCADE)
  CostCentre = models.ForeignKey(ACostCentre, null=False, blank=False, related_name="AGiftBatch_CostCentre", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_gift_batch_pk', fields=['BatchNumber']),
    ]

class AGift(models.Model):
  """
  Information on the donor's giving. Points to the gift detail records.
  """

  GiftBatch = models.ForeignKey(AGiftBatch, null=False, blank=False, related_name="AGift_GiftBatch", on_delete=models.CASCADE)
  # Identifies a transaction within a journal within a batch within a ledger
  GiftTransactionNumber = models.IntegerField(default=0, null=False, blank=False)
  GiftStatus = models.CharField(max_length=12)
  DateEntered = models.DateTimeField(null=False, blank=False)
  # Used to get a yes no response from the user
  HomeAdminCharges = models.BooleanField(null=False, blank=False)
  # Used to get a yes no response from the user
  IltAdminCharges = models.BooleanField(null=False, blank=False)
  # Indicates that this gift is linked to the previous gift transaction number. For adjustments this links the new transaction to the reversal one.  Set by the system.
  LinkToPreviousGift = models.BooleanField(default=False, null=False, blank=False)
  # Indicates whether this gift should be included on receipts. For adjustments this field can be set to No to suppress printing.
  PrintReceipt = models.BooleanField(default=True, null=False, blank=False)
  ReceiptLetterCode = models.CharField(max_length=8)
  # Defines how a gift is given.
  MethodOfGiving = models.ForeignKey(AMethodOfGiving, related_name="AGift_MethodOfGiving", on_delete=models.CASCADE)
  # This is how the partner paid. Eg cash, Cheque etc
  MethodOfPayment = models.ForeignKey(AMethodOfPayment, related_name="AGift_MethodOfPayment", on_delete=models.CASCADE)
  # This is the partner key of the donor.
  Donor = models.ForeignKey(PPartner, null=False, blank=False, related_name="AGift_Donor", on_delete=models.CASCADE)
  # NOT USED AT ALL
  AdminCharge = models.BooleanField(default=False)
  # Gift Receipt Number
  ReceiptNumber = models.IntegerField(default=0)
  # Identifies the last gift detail entered
  LastDetailNumber = models.IntegerField(default=0, null=False, blank=False)
  # Reference number/code for the transaction
  Reference = models.CharField(max_length=10)
  # Flag to indicate Donors first gift
  FirstTimeGift = models.BooleanField(default=False)
  # Indicates whether or not the receipt has been printed for this gift
  ReceiptPrinted = models.BooleanField(default=False, null=False, blank=False)
  # Indicates whether or not the gift has restricted access. If it does then the access will be controlled by s_group_gift
  Restricted = models.BooleanField(default=False)
  # Bank or credit card account used for making this gift transaction.
  BankingDetailsKey = models.IntegerField(default=0, null=False, blank=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_gift_pk', fields=['GiftBatch', 'GiftTransactionNumber']),
    ]

class AGiftDetail(models.Model):
  """
  The gift recipient information for a gift.  A single gift can be split among more than one recipient.  A gift detail record is created for each recipient.
  """

  Gift = models.ForeignKey(AGift, null=False, blank=False, related_name="AGiftDetail_Gift", on_delete=models.CASCADE)
  # Identifies a gift detail within a gift transaction.   When a donor gives a donation to multiple recipients (a split gift), a gift detail record is created for each recipient.
  DetailNumber = models.IntegerField(default=0, null=False, blank=False)
  # The partner key of the commitment field (the unit) of the recipient of the gift.  This is not the ledger number but rather the partner key of the unit associated with the ledger.
  RecipientLedgerNumber = models.ForeignKey(PPartner, null=False, blank=False, related_name="AGiftDetail_RecipientLedgerNumber", on_delete=models.CASCADE)
  # This is a number of currency units of the ledger base currency.
  GiftAmount = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Used to decide whose reports will see this comment
  CommentOneType = models.CharField(max_length=12)
  # This is a long description and is 80 characters long.
  GiftCommentOne = models.CharField(max_length=80)
  # Defines whether the donor wishes the recipient to know who gave the gift
  ConfidentialGift = models.BooleanField(null=False, blank=False)
  # Whether this gift is tax deductible
  TaxDeductible = models.BooleanField(default=True)
  # The partner key of the recipient of the gift.
  Recipient = models.ForeignKey(PPartner, null=False, blank=False, related_name="AGiftDetail_Recipient", on_delete=models.CASCADE)
  # To determine whether an admin fee on the transaction should be overwritten if it normally has a charge associated with it. Used for both local and ilt transaction.
  Charge = models.BooleanField(default=True)
  # This is a number of currency units in the International Currency
  GiftAmountIntl = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Indicates whether this gift detail has a matching inverse detail record because a modification was made
  ModifiedDetail = models.BooleanField(default=False)
  # Stores the concatenated primary key fields of the originating gift detail, of which this gift detail is the inverse.
  ModifiedDetailKey = models.CharField(max_length=24)
  # Indicates whether this gift detail's gift destination can be changed. Used for gift adjustments with family recipients.
  FixedGiftDestination = models.BooleanField(default=False)
  # This is a number of currency units in the entered Currency
  GiftTransactionAmount = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # identifes the ICH process number
  IchNumber = models.IntegerField(default=0, null=False, blank=False)
  # Mailing Code of the mailing that the gift was a response to.
  Mailing = models.ForeignKey(PMailing, related_name="AGiftDetail_Mailing", on_delete=models.CASCADE)
  # Used to decide whose reports will see this comment
  CommentTwoType = models.CharField(max_length=12)
  # This is a long description and is 80 characters long.
  GiftCommentTwo = models.CharField(max_length=80)
  # Used to decide whose reports will see this comment
  CommentThreeType = models.CharField(max_length=12)
  # This is a long description and is 80 characters long.
  GiftCommentThree = models.CharField(max_length=80)
  # Percentage of gift amount that is tax-deductible
  TaxDeductiblePct = models.DecimalField(max_digits=5, decimal_places=2)
  # Tax deductible portion of gift
  TaxDeductibleAmount = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Tax deductible portion of gift (Base Currency)
  TaxDeductibleAmountBase = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Tax deductible portion of gift (Intl Currency)
  TaxDeductibleAmountIntl = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Non tax-deductible portion of gift
  NonDeductibleAmount = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Non tax-deductible portion of gift (Base Currency)
  NonDeductibleAmountBase = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Non tax-deductible portion of gift (Intl Currency)
  NonDeductibleAmountIntl = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  MotivationDetail = models.ForeignKey(AMotivationDetail, null=False, blank=False, related_name="AGiftDetail_MotivationDetail", on_delete=models.CASCADE)
  CostCentre = models.ForeignKey(ACostCentre, null=False, blank=False, related_name="AGiftDetail_CostCentre", on_delete=models.CASCADE)
  GiftBatch = models.ForeignKey(AGiftBatch, null=False, blank=False, related_name="AGiftDetail_GiftBatch", on_delete=models.CASCADE)
  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="AGiftDetail_Account", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_gift_detail_pk', fields=['Gift', 'DetailNumber']),
    ]

class AProcessedFee(models.Model):
  """
  Stores administrative fees and grants which have been calculated on gifts.
  """

  GiftDetail = models.ForeignKey(AGiftDetail, null=False, blank=False, related_name="AProcessedFee_GiftDetail", on_delete=models.CASCADE)
  # the fee which the calculated amounts are stored against.
  FeeCode = models.CharField(max_length=8, null=False, blank=False)
  # Total Amount of the fee for the given period.
  PeriodicAmount = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # Date ""admin fee calculations"" have been run to fee total has been created as a transaction in the general ledger.
  ProcessedDate = models.DateTimeField()
  # System generated time stamp.
  Timestamp = models.IntegerField()
  CostCentre = models.ForeignKey(ACostCentre, null=False, blank=False, related_name="AProcessedFee_CostCentre", on_delete=models.CASCADE)
  AccountingPeriod = models.ForeignKey(AAccountingPeriod, null=False, blank=False, related_name="AProcessedFee_AccountingPeriod", on_delete=models.CASCADE)
  GiftBatch = models.ForeignKey(AGiftBatch, null=False, blank=False, related_name="AProcessedFee_GiftBatch", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_processed_fee_pk', fields=['GiftDetail', 'FeeCode']),
    ]

class AJournal(models.Model):
  """
  Holds details of each general ledger journal, which contains a group of transactions.
  """

  Batch = models.ForeignKey(ABatch, null=False, blank=False, related_name="AJournal_Batch", on_delete=models.CASCADE)
  # Identifies a journal within a batch
  JournalNumber = models.IntegerField(null=False, blank=False)
  # This is a long description and is 80 characters long.
  JournalDescription = models.CharField(max_length=80, null=False, blank=False)
  # This is a number of currency units in the currency of the transaction.
  JournalDebitTotal = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # This is the number of currency units in the currency of the transaction.
  JournalCreditTotal = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # This defines which accounting period is being used
  JournalPeriod = models.IntegerField(default=0, null=False, blank=False)
  # Date the journal comes into effect.
  DateEffective = models.DateTimeField(null=False, blank=False)
  # The number of the last transaction within the journal.
  LastTransactionNumber = models.IntegerField(default=0, null=False, blank=False)
  # Has a journal been posted yet
  JournalStatus = models.CharField(max_length=12, default='Unposted')
  # This defines which currency is being used
  TransactionCurrency = models.ForeignKey(ACurrency, null=False, blank=False, related_name="AJournal_TransactionCurrency", on_delete=models.CASCADE)
  BaseCurrency = models.ForeignKey(ACurrency, related_name="AJournal_BaseCurrency", on_delete=models.CASCADE)
  # The rate of exchange from the transaction currency (in a_transaction_currency_c) to the ledger base currency.
  ExchangeRateToBase = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # The time component of the exchange rate.
  ExchangeRateTime = models.IntegerField(default=0, null=False, blank=False)
  # Date the journal was created.
  DateOfEntry = models.DateTimeField(null=False, blank=False)
  # Indicates whether or not a journal has been reversed.
  Reversed = models.BooleanField(default=False)
  TransactionType = models.ForeignKey(ATransactionType, null=False, blank=False, related_name="AJournal_TransactionType", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_journal_pk', fields=['Batch', 'JournalNumber']),
    ]

class ATransaction(models.Model):
  """
  Detailed information for each debit and credit in a general ledger journal.
  """

  Journal = models.ForeignKey(AJournal, null=False, blank=False, related_name="ATransaction_Journal", on_delete=models.CASCADE)
  # Identifies a transaction within a journal within a batch within a ledger
  TransactionNumber = models.IntegerField(default=0, null=False, blank=False)
  # This identifies the account the financial transaction must be stored against [NOT USED]
  PrimaryAccountCode = models.CharField(max_length=8)
  # This identifies which cost centre an account is applied to [NOT USED]
  PrimaryCostCentreCode = models.CharField(max_length=12)
  # Date the transaction took place
  TransactionDate = models.DateTimeField(null=False, blank=False)
  # This is a number of currency units
  TransactionAmount = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # This is a number of currency units
  AmountInBaseCurrency = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # Used to get a yes no response from the user
  AnalysisIndicator = models.BooleanField(default=False, null=False, blank=False)
  # shows if the transaction has been reconciled or not
  ReconciledStatus = models.BooleanField(default=False, null=False, blank=False)
  Narrative = models.CharField(max_length=250)
  DebitCreditIndicator = models.BooleanField(null=False, blank=False)
  # Has a transaction been posted yet
  TransactionStatus = models.BooleanField()
  # The header (eg, cashbook #) that the transaction is associated with. [NOT USED]
  HeaderNumber = models.IntegerField(default=0)
  # The detail (within the header) that the transaction is associated with. [NOT USED]
  DetailNumber = models.IntegerField(default=0)
  SubType = models.CharField(max_length=8)
  # Indicates whether the ILT transaction has been transferred to transaction for ILT file.
  ToIlt = models.BooleanField(default=False)
  # To flag a transaction as having come from a source ledger and been processed in an ilt processing centre
  Source = models.BooleanField(default=False)
  # Reference number/code for the transaction
  Reference = models.CharField(max_length=50, null=False, blank=False)
  # Transaction key which initiated an ILT transaction
  SourceReference = models.CharField(max_length=50)
  # Was this transaction generated automatically by the system?
  SystemGenerated = models.BooleanField(default=False)
  # The transaction amount in the second base currency.
  AmountInIntlCurrency = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # identifes the ICH process number
  IchNumber = models.IntegerField(default=0, null=False, blank=False)
  # Key ministry to which this transaction applies (just for fund transfers)
  KeyMinistry = models.ForeignKey(PUnit, related_name="ATransaction_KeyMinistry", on_delete=models.CASCADE)
  Batch = models.ForeignKey(ABatch, null=False, blank=False, related_name="ATransaction_Batch", on_delete=models.CASCADE)
  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="ATransaction_Account", on_delete=models.CASCADE)
  CostCentre = models.ForeignKey(ACostCentre, null=False, blank=False, related_name="ATransaction_CostCentre", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_transaction_pk', fields=['Journal', 'TransactionNumber']),
    ]

class ATransAnalAttrib(models.Model):
  """
  Analysis information entered by the user for a general ledger transaction.
  """

  Transaction = models.ForeignKey(ATransaction, null=False, blank=False, related_name="ATransAnalAttrib_Transaction", on_delete=models.CASCADE)
  AnalysisTypeCode = models.CharField(max_length=8, null=False, blank=False)
  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="ATransAnalAttrib_Account", on_delete=models.CASCADE)
  AnalysisAttribute = models.ForeignKey(AAnalysisAttribute, null=False, blank=False, related_name="ATransAnalAttrib_AnalysisAttribute", on_delete=models.CASCADE)
  FreeformAnalysis = models.ForeignKey(AFreeformAnalysis, null=False, blank=False, related_name="ATransAnalAttrib_FreeformAnalysis", on_delete=models.CASCADE)
  CostCentre = models.ForeignKey(ACostCentre, null=False, blank=False, related_name="ATransAnalAttrib_CostCentre", on_delete=models.CASCADE)
  Batch = models.ForeignKey(ABatch, null=False, blank=False, related_name="ATransAnalAttrib_Batch", on_delete=models.CASCADE)
  Journal = models.ForeignKey(AJournal, null=False, blank=False, related_name="ATransAnalAttrib_Journal", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_trans_anal_attrib_pk', fields=['Transaction']),
    ]

class ASuspenseAccount(models.Model):
  """
  Lists the suspense accounts of each ledger.
  """

  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="ASuspenseAccount_Account", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_suspense_account_pk', fields=['Account']),
    ]

class AApSupplier(models.Model):
  """
  This table defines the concept of a supplier in the AP system and is the centre of the AP system.
  """

  # Reference to the partner key for this supplier
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="AApSupplier_Partner", on_delete=models.CASCADE)
  # Number of months to display invoices and credit notes
  PreferredScreenDisplay = models.IntegerField()
  # Reference to default bank account to use to pay supplier with.
  DefaultBankAccount = models.CharField(max_length=8)
  # The default type of payment to use when paying this supplier.
  PaymentType = models.CharField(max_length=12)
  # The currency code to use for this supplier.
  Currency = models.ForeignKey(ACurrency, null=False, blank=False, related_name="AApSupplier_Currency", on_delete=models.CASCADE)
  # The default AP Account to use when paying this supplier.
  DefaultApAccount = models.CharField(max_length=8)
  # Default credit terms to use for invoices from this supplier.
  DefaultCreditTerms = models.IntegerField()
  # Default percentage discount to receive for early payments.
  DefaultDiscountPercentage = models.DecimalField(max_digits=24, decimal_places=10)
  # Default number of days in which the discount percentage has effect.
  DefaultDiscountDays = models.IntegerField()
  # What type of supplier this is - normal, credit card, maybe something else.
  SupplierType = models.CharField(max_length=12)
  # Reference to the default expense Account to use for invoice details.
  DefaultExpAccount = models.CharField(max_length=8)
  # Reference to the default cost centre to use for invoice details.
  DefaultCostCentre = models.CharField(max_length=8)
  # This reference identifies us to the supplier
  OurReference = models.CharField(max_length=50)


class AApDocument(models.Model):
  """
  Either an invoice or a credit note in the Accounts Payable system.
  """

  # Unique key for this record
  ApDocumentId = models.IntegerField(default=0, null=False, blank=False, unique=True)
  # A unique key (together with the ledger number) to identify this document.
  ApNumber = models.IntegerField(null=False, blank=False)
  # Reference to the supplier that sent this invoice.
  Partner = models.ForeignKey(AApSupplier, null=False, blank=False, related_name="AApDocument_Partner", on_delete=models.CASCADE)
  # A flag to indicate if this document is an invoice or a credit note.
  CreditNote = models.BooleanField(default=False, null=False, blank=False)
  # The code given on the document itself (be it invoice or credit note). This will have to be unique for each supplier.
  DocumentCode = models.CharField(max_length=15)
  # Some kind of other reference needed.
  Reference = models.CharField(max_length=50)
  # The date when this document was issued.
  DateIssued = models.DateTimeField(null=False, blank=False)
  # The date when this document was entered into the system.
  DateEntered = models.DateTimeField(null=False, blank=False)
  # Credit terms allowed for this invoice.
  CreditTerms = models.IntegerField(default=0)
  # The total amount of money that this document is worth.
  TotalAmount = models.DecimalField(max_digits=24, decimal_places=10, default=0, null=False, blank=False)
  # the currency of the document
  CurrencyCode = models.CharField(max_length=8, null=False, blank=False)
  # The exchange rate to the base currency at the time that the document was issued.
  ExchangeRateToBase = models.DecimalField(max_digits=24, decimal_places=10)
  # The percentage discount you get for early payment of this document in the case that it is an invoice.
  DiscountPercentage = models.DecimalField(max_digits=24, decimal_places=10)
  # The number of days that the discount is valid for (0 for none).
  DiscountDays = models.IntegerField()
  # The number of the last item for this document. This is used simply to quickly get the next number if items are added.
  LastDetailNumber = models.IntegerField(default=0, null=False, blank=False)
  # The current status of the invoice. The value can (for now) be one of: OPEN, APPROVED, POSTED, PARTPAID, or PAID.
  DocumentStatus = models.CharField(max_length=8)
  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="AApDocument_Account", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_ap_document_uk', fields=['ApNumber']),
    ]

class ACrdtNoteInvoiceLink(models.Model):
  """
  This table receives a new entry when a credit note is applied to an invoice. Since the invoices and credit notes share the same table, we need a way to link the two, and this is the role of this table.
  """

  # Reference to the credit note.
  CreditNoteDocument = models.ForeignKey(AApDocument, null=False, blank=False, related_name="ACrdtNoteInvoiceLink_CreditNoteDocument", on_delete=models.CASCADE)
  # Reference to the invoice.
  InvoiceDocument = models.ForeignKey(AApDocument, null=False, blank=False, related_name="ACrdtNoteInvoiceLink_InvoiceDocument", on_delete=models.CASCADE)
  # Reference to the ledger number.
  LedgerNumber = models.IntegerField(null=False, blank=False)
  AppliedDate = models.DateTimeField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_crdt_note_invoice_link_pk', fields=['CreditNoteDocument', 'InvoiceDocument']),
    ]

class AApDocumentDetail(models.Model):
  """
  An invoice or credit note consists out of several items, or details. This table contains all these details.
  """

  # Reference to the document
  ApDocument = models.ForeignKey(AApDocument, null=False, blank=False, related_name="AApDocumentDetail_ApDocument", on_delete=models.CASCADE)
  # A unique number for this detail for its document.
  DetailNumber = models.IntegerField(null=False, blank=False)
  # Indicates if this detail has been approved or not.
  DetailApproved = models.BooleanField(default=False, null=False, blank=False)
  # Some other reference to the item.
  ItemRef = models.CharField(max_length=50)
  # A narrative about what this is.
  Narrative = models.CharField(max_length=100)
  # The amount of money this detail is worth.
  Amount = models.DecimalField(max_digits=24, decimal_places=10)
  # The date when this detail was approved.
  ApprovalDate = models.DateTimeField()
  CostCentre = models.ForeignKey(ACostCentre, null=False, blank=False, related_name="AApDocumentDetail_CostCentre", on_delete=models.CASCADE)
  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="AApDocumentDetail_Account", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_ap_document_detail_pk', fields=['ApDocument', 'DetailNumber']),
    ]

class AApPayment(models.Model):
  """
  Records all payments that have been made against an accounts payable detail.
  """

  # This is used as a key field in most of the accounting system files
  Ledger = models.ForeignKey(ALedger, null=False, blank=False, related_name="AApPayment_Ledger", on_delete=models.CASCADE)
  # Unique number to identify each payment batch.
  PaymentNumber = models.IntegerField(default=0, null=False, blank=False)
  # The amount of money that was paid
  Amount = models.DecimalField(max_digits=24, decimal_places=10)
  # the currency of the document
  CurrencyCode = models.CharField(max_length=8, null=False, blank=False)
  # The exchange rate to the base currency at the time of payment.
  ExchangeRateToBase = models.DecimalField(max_digits=24, decimal_places=10)
  # Date that the payment for an accounts payable was made.
  PaymentDate = models.DateTimeField()
  # This is the system user id of the person who made the payment.
  User = models.ForeignKey(SUser, related_name="AApPayment_User", on_delete=models.CASCADE)
  # Method that was used to make the payment - cheque, cash, ep, credit card, etc.
  MethodOfPayment = models.CharField(max_length=10)
  # The source or reference for the accounts payable payment.  This could be a cheque number.
  Reference = models.CharField(max_length=50)
  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="AApPayment_Account", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_ap_payment_pk', fields=['PaymentNumber']),
    ]

class AApDocumentPayment(models.Model):
  """
  This table links the different payments to actual invoices and credit notes.
  """

  # AP document ref
  ApDocument = models.ForeignKey(AApDocument, null=False, blank=False, related_name="AApDocumentPayment_ApDocument", on_delete=models.CASCADE)
  # Unique number to identify each payment batch.
  PaymentNumber = models.IntegerField(default=0, null=False, blank=False)
  # The amount of money that was paid
  Amount = models.DecimalField(max_digits=24, decimal_places=10)
  ApPayment = models.ForeignKey(AApPayment, null=False, blank=False, related_name="AApDocumentPayment_ApPayment", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_ap_document_payment_pk', fields=['ApDocument']),
    ]

class AEpPayment(models.Model):
  """
  This table acts as a queue for electronic payments. If an invoice is paid electronically, the payment is added to this table. A EP program will go through this table paying all entries to GL and moving them to the a_ap_payment table.
  """

  # This is used as a key field in most of the accounting system files
  Ledger = models.ForeignKey(ALedger, null=False, blank=False, related_name="AEpPayment_Ledger", on_delete=models.CASCADE)
  # Unique number to identify each payment batch.
  PaymentNumber = models.IntegerField(default=0, null=False, blank=False)
  # The amount of money that was paid
  Amount = models.DecimalField(max_digits=24, decimal_places=10)
  # This is the system user id of the person who made the payment.
  User = models.ForeignKey(SUser, related_name="AEpPayment_User", on_delete=models.CASCADE)
  # The source or reference for the accounts payable payment.  This could be a cheque number.
  Reference = models.CharField(max_length=50)
  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="AEpPayment_Account", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_ep_payment_pk', fields=['PaymentNumber']),
    ]

class AEpDocumentPayment(models.Model):
  """
  This table links the different EP payments to actual invoices and credit notes.
  """

  # AP Document ref
  ApDocument = models.ForeignKey(AApDocument, null=False, blank=False, related_name="AEpDocumentPayment_ApDocument", on_delete=models.CASCADE)
  # The amount of money that was paid
  Amount = models.DecimalField(max_digits=24, decimal_places=10)
  EpPayment = models.ForeignKey(AEpPayment, null=False, blank=False, related_name="AEpDocumentPayment_EpPayment", on_delete=models.CASCADE)


class AApAnalAttrib(models.Model):
  """
  Analysis Attributes applied to an AP for posting to the GL.
  """

  ApDocumentDetail = models.ForeignKey(AApDocumentDetail, null=False, blank=False, related_name="AApAnalAttrib_ApDocumentDetail", on_delete=models.CASCADE)
  AnalysisTypeCode = models.CharField(max_length=8, null=False, blank=False)
  AnalysisAttribute = models.ForeignKey(AAnalysisAttribute, null=False, blank=False, related_name="AApAnalAttrib_AnalysisAttribute", on_delete=models.CASCADE)
  Account = models.ForeignKey(AAccount, null=False, blank=False, related_name="AApAnalAttrib_Account", on_delete=models.CASCADE)
  FreeformAnalysis = models.ForeignKey(AFreeformAnalysis, null=False, blank=False, related_name="AApAnalAttrib_FreeformAnalysis", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_ap_anal_attrib_pk', fields=['ApDocumentDetail']),
    ]

class AArInvoice(models.Model):
  """
  the invoice (which is also an offer at a certain stage)
  """

  # This is used as a key field in most of the accounting system files
  LedgerNumber = models.IntegerField(default=0, null=False, blank=False)
  # Key to uniquely identify invoice
  Key = models.IntegerField(null=False, blank=False)
  # an invoice can have these states: OFFER, CHARGED, PARTIALLYPAID, PAID
  Status = models.CharField(max_length=16, null=False, blank=False)
  # This is the partner who has to pay the bill; can be null for cash payments; could also be another field
  Partner = models.ForeignKey(PPartner, related_name="AArInvoice_Partner", on_delete=models.CASCADE)
  # this is the date when the invoice was charged
  DateEffective = models.DateTimeField()
  # refers to the offer that was created for this invoice; it is basically an archived copy of the invoice, and the invoice might actually be different from the offer (e.g. hospitality: different number of people, etc.); table ph_booking always refers to the invoice, and the invoice refers to the offer; there is no requirement for an offer to exist, it can be null
  Offer = models.IntegerField()
  # this defines whether no tax is applied to this invoice (NONE), or if a SPECIAL tax is applied, or if the DEFAULT tax defined for each article; this should work around issues of selling to businesses or customers abroad
  Taxing = models.CharField(max_length=10, default='DEFAULT', null=False, blank=False)
  # The total amount of money that this invoice is worth; this includes all discounts, even the early payment discount; if the early payment discount does not apply anymore at the time of payment, this total amount needs to be updated
  TotalAmount = models.DecimalField(max_digits=24, decimal_places=10)
  # the currency of the total amount
  Currency = models.ForeignKey(ACurrency, null=False, blank=False, related_name="AArInvoice_Currency", on_delete=models.CASCADE)
  TaxTable = models.ForeignKey(ATaxTable, null=False, blank=False, related_name="AArInvoice_TaxTable", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_ar_invoice_pk', fields=['Key']),
    ]

class AArInvoiceDetail(models.Model):
  """
  an invoice consists of one or more details
  """

  ArInvoice = models.ForeignKey(AArInvoice, null=False, blank=False, related_name="AArInvoiceDetail_ArInvoice", on_delete=models.CASCADE)
  # A unique number for this detail for its invoice.
  DetailNumber = models.IntegerField(null=False, blank=False)
  # Reference for this invoice detail; for a non specific article that could give more details (e.g. which book of type small book)
  ArReference = models.CharField(max_length=50)
  # defines the number of the article items that is bought
  ArNumberOfItem = models.IntegerField(null=False, blank=False)
  # The total amount of money that this invoice detail is worth; includes the discounts
  CalculatedAmount = models.DecimalField(max_digits=24, decimal_places=10)
  # the currency of the total amount
  Currency = models.ForeignKey(ACurrency, null=False, blank=False, related_name="AArInvoiceDetail_Currency", on_delete=models.CASCADE)
  TaxTable = models.ForeignKey(ATaxTable, null=False, blank=False, related_name="AArInvoiceDetail_TaxTable", on_delete=models.CASCADE)
  ArArticlePrice = models.ForeignKey(AArArticlePrice, null=False, blank=False, related_name="AArInvoiceDetail_ArArticlePrice", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_ar_invoice_detail_pk', fields=['ArInvoice', 'DetailNumber']),
    ]

class AArInvoiceDiscount(models.Model):
  """
  defines which discounts apply directly to the invoice rather than the invoice items; this can depend on the customer etc
  """

  ArInvoice = models.ForeignKey(AArInvoice, null=False, blank=False, related_name="AArInvoiceDiscount_ArInvoice", on_delete=models.CASCADE)
  ArDiscount = models.ForeignKey(AArDiscount, null=False, blank=False, related_name="AArInvoiceDiscount_ArDiscount", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_ar_invoice_discount_pk', fields=['ArInvoice', 'ArDiscount']),
    ]

class AArInvoiceDetailDiscount(models.Model):
  """
  defines which discounts apply one invoice item
  """

  ArInvoiceDetail = models.ForeignKey(AArInvoiceDetail, null=False, blank=False, related_name="AArInvoiceDetailDiscount_ArInvoiceDetail", on_delete=models.CASCADE)
  ArDiscount = models.ForeignKey(AArDiscount, null=False, blank=False, related_name="AArInvoiceDetailDiscount_ArDiscount", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='a_ar_invoice_detail_discount_pk', fields=['ArInvoiceDetail', 'ArDiscount']),
    ]

class PmGeneralApplication(models.Model):
  """
  The first part of any application which contains data common to either short term or long term applications. 
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPerson, null=False, blank=False, related_name="PmGeneralApplication_Partner", on_delete=models.CASCADE)
  # Key to uniquely identify application
  ApplicationKey = models.IntegerField(default=0, null=False, blank=False)
  # Partner key of office by which application was entered.
  RegistrationOffice = models.ForeignKey(PUnit, null=False, blank=False, related_name="PmGeneralApplication_RegistrationOffice", on_delete=models.CASCADE)
  # Date of application.
  GenAppDate = models.DateTimeField(null=False, blank=False)
  # Describes what the application is for, eg. conference, year program.
  AppType = models.ForeignKey(PtApplicationType, null=False, blank=False, related_name="PmGeneralApplication_AppType", on_delete=models.CASCADE)
  # TODO: this field is a combination of registration office and application number. might not be needed???
  OldLink = models.CharField(max_length=16, null=False, blank=False)
  # This is the possible field or team of service.
  GenAppPossSrvUnit = models.ForeignKey(PUnit, related_name="PmGeneralApplication_GenAppPossSrvUnit", on_delete=models.CASCADE)
  # This field will not appear on the screen but will be updated when someone chooses to delete a record. Rather that an actual deletion, the record will be 'marked' for deletion after an agreed upon interval.
  GenAppDelete = models.BooleanField(default=False)
  # Describes the applicant, eg. volunteer, staff, speaker.
  GenApplicantType = models.CharField(max_length=15, null=False, blank=False)
  # Indicates the status of the application.
  GenApplicationStatus = models.ForeignKey(PtApplicantStatus, related_name="PmGeneralApplication_GenApplicationStatus", on_delete=models.CASCADE)
  # Indicates if the application is closed.
  Closed = models.BooleanField(default=False)
  # This identifies the user that closed the application
  ClosedBy = models.ForeignKey(SUser, related_name="PmGeneralApplication_ClosedBy", on_delete=models.CASCADE)
  # This is the date the application was closed.
  DateClosed = models.DateTimeField()
  # Indicates if the application is on hold.
  GenApplicationOnHold = models.BooleanField(default=False)
  # Comment on why the application is on hold.
  GenApplicationHoldReason = models.CharField(max_length=50)
  # Indicates if the application process has been cancelled.
  GenCancelledApp = models.BooleanField(default=False)
  # Comment on why the application is on hold.
  GenAppCancelReason = models.CharField(max_length=27)
  # This is the date the application was cancelled.
  GenAppCancelled = models.DateTimeField()
  # Describes if the applicant has been accepted by the serving field.
  GenAppSrvFldAccept = models.BooleanField(default=False)
  # This is the date the receiving field accepted the applicant.
  GenAppRecvgFldAccept = models.DateTimeField()
  # Describes if the applicant has been accepted by the sending field.
  GenAppSendFldAccept = models.BooleanField(default=False)
  # This is the date the sending field accepted the applicant.
  GenAppSendFldAccept = models.DateTimeField()
  # This field indicates how they were influenced to apply with us.
  GenContact1 = models.ForeignKey(PtContact, related_name="PmGeneralApplication_GenContact1", on_delete=models.CASCADE)
  # This field indicates how they were influenced to apply with us.
  GenContact2 = models.ForeignKey(PtContact, related_name="PmGeneralApplication_GenContact2", on_delete=models.CASCADE)
  # Indicates the date the record was last updated.
  GenAppUpdate = models.DateTimeField()
  # Sometimes there are extra comments of preferences that are related to an application.  These can be entered here.
  Comment = models.CharField(max_length=1000)
  # This is the currency that is used for amounts listed in this application
  GenAppCurrency = models.ForeignKey(ACurrency, related_name="PmGeneralApplication_GenAppCurrency", on_delete=models.CASCADE)
  # This is the placement person handling this application.
  PlacementPartner = models.ForeignKey(PPerson, related_name="PmGeneralApplication_PlacementPartner", on_delete=models.CASCADE)
  # stores the plain data received from the browser in JSON format
  RawApplicationData = models.CharField(max_length=15000)
  # the person partner key of the applicant in the local database of the registration office. no foreign key since the person partner is in another database
  LocalPartnerKey = models.IntegerField()
  # true if the applicant has already been imported into the local database of the registration office.
  ImportedLocalPetra = models.BooleanField(default=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pm_general_application_pk', fields=['Partner', 'ApplicationKey', 'RegistrationOffice']),
      models.UniqueConstraint(name='pm_general_application_nk', fields=['Partner', 'GenAppDate', 'AppType', 'OldLink']),
    ]

class PmApplicationStatusHistory(models.Model):
  """
  Keeps a history of the application status for short and long term applications.
  """

  # Key to make editing these records easier
  Key = models.IntegerField(null=False, blank=False, unique=True)
  # Indicates the status of the application.
  Status = models.ForeignKey(PtApplicantStatus, related_name="PmApplicationStatusHistory_Status", on_delete=models.CASCADE)
  # Effective Date of the chosen Application Status
  StatusDateEffective = models.DateTimeField()
  # Gives further comments about application status.
  Comment = models.CharField(max_length=250)
  GeneralApplication = models.ForeignKey(PmGeneralApplication, null=False, blank=False, related_name="PmApplicationStatusHistory_GeneralApplication", on_delete=models.CASCADE)


class PmShortTermApplication(models.Model):
  """
  Table for short term applications.
  """

  GeneralApplication = models.ForeignKey(PmGeneralApplication, null=False, blank=False, related_name="PmShortTermApplication_GeneralApplication", on_delete=models.CASCADE)
  # Date of application
  StAppDate = models.DateTimeField(null=False, blank=False)
  StApplicationType = models.CharField(max_length=16, null=False, blank=False)
  # TODO: this field is a combination of registration office and application number. might not be needed???
  StBasicOutreachId = models.CharField(max_length=16, null=False, blank=False)
  # This field will not appear on the screen but will be updated when someone chooses to delete a record. Rather that an actual deletion, the record will be 'marked' for deletion after an agreed upon interval.
  StBasicDelete = models.BooleanField(default=False)
  # Indicates if the application is on hold.
  StApplicationOnHold = models.BooleanField(default=False)
  # Comment on why the application is on hold.
  StApplicationHoldReason = models.CharField(max_length=20)
  # Indicates the outreach code of the confirmed option.
  ConfirmedOptionCode = models.CharField(max_length=13)
  # Indicates if for outreach only.
  StOutreachOnly = models.BooleanField(default=False)
  # Indicates the confirmed outreach option.
  StConfirmedOption = models.ForeignKey(PUnit, related_name="PmShortTermApplication_StConfirmedOption", on_delete=models.CASCADE)
  # Indicates the current field.
  StCurrentField = models.ForeignKey(PUnit, related_name="PmShortTermApplication_StCurrentField", on_delete=models.CASCADE)
  # Indicates the status of given arrival details (not known, being planned,...).
  ArrivalDetailsStatus = models.CharField(max_length=12, default='no')
  # This code indicates the arrival point of the congress attendee.
  ArrivalPoint = models.ForeignKey(PtArrivalPoint, related_name="PmShortTermApplication_ArrivalPoint", on_delete=models.CASCADE)
  # This code indicates the type of travel to the congress..
  TravelTypeToCong = models.ForeignKey(PtTravelType, related_name="PmShortTermApplication_TravelTypeToCong", on_delete=models.CASCADE)
  # Date of arrival at the conference.
  Arrival = models.DateTimeField()
  # The hour of arrival.
  ArrivalHour = models.IntegerField(default=00)
  # The minutes of arrival.
  ArrivalMinute = models.IntegerField(default=00)
  # Information concerning flight or bus numbers.
  ToCongTravelInfo = models.CharField(max_length=16)
  # Indicates if transport from arrival point to congress needs to be arranged by Registrar.
  ArrivalTransportNeeded = models.BooleanField(default=False)
  # Gives further comments on arrival information.
  ArrivalComments = models.CharField(max_length=80)
  # Indicates the status of given departure details (undetermined, being planned,...).
  DepartureDetailsStatus = models.CharField(max_length=12, default='no')
  # This code indicates the departure point of the congress attendee.
  DeparturePoint = models.ForeignKey(PtArrivalPoint, related_name="PmShortTermApplication_DeparturePoint", on_delete=models.CASCADE)
  # This code indicates the type of travel from the congress.
  TravelTypeFromCong = models.ForeignKey(PtTravelType, related_name="PmShortTermApplication_TravelTypeFromCong", on_delete=models.CASCADE)
  # Date of departure from the conference.
  Departure = models.DateTimeField()
  # The hour of departure.
  DepartureHour = models.IntegerField(default=00)
  # The minutes of departure.
  DepartureMinute = models.IntegerField(default=00)
  # Information concerning flight or bus numbers.
  FromCongTravelInfo = models.CharField(max_length=16)
  # Indicates if transport from congress to departure point needs to be arranged by Registrar.
  DepartureTransportNeeded = models.BooleanField(default=False)
  # Gives further comments on departure information.
  DepartureComments = models.CharField(max_length=80)
  # Applicant is interested if there would be a transport possibility from/to arrival/departure point.
  TransportInterest = models.BooleanField(default=False)
  # This code indicates what role they have during pre-congress.
  StPreCongress = models.ForeignKey(PtCongressCode, related_name="PmShortTermApplication_StPreCongress", on_delete=models.CASCADE)
  # Indicates the role for the Congress.
  StCongress = models.ForeignKey(PtCongressCode, related_name="PmShortTermApplication_StCongress", on_delete=models.CASCADE)
  # Indicates any special information about the applicant.
  StSpecialApplicant = models.ForeignKey(PtSpecialApplicant, related_name="PmShortTermApplication_StSpecialApplicant", on_delete=models.CASCADE)
  # The role a participant has during a outreach
  OutreachRole = models.ForeignKey(PtCongressCode, related_name="PmShortTermApplication_OutreachRole", on_delete=models.CASCADE)
  # Indicates if the person is a leader of a fellowship group.
  StFgLeader = models.BooleanField(default=False)
  # A free form field for group codes.
  StFgCode = models.CharField(max_length=16)
  # Special Costs related to the outreach.
  StOutreachSpecialCost = models.IntegerField(default=0)
  # Special Costs related to the congress.
  StCngrssSpecialCost = models.IntegerField(default=0)
  # This field idenifies the field to be charged for the costs.
  StFieldCharged = models.ForeignKey(PUnit, related_name="PmShortTermApplication_StFieldCharged", on_delete=models.CASCADE)
  # This is the language spoken by the applicant at the Congress.
  StCongressLanguage = models.ForeignKey(PLanguage, related_name="PmShortTermApplication_StCongressLanguage", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pm_short_term_application_pk', fields=['GeneralApplication']),
      models.UniqueConstraint(name='pm_short_term_application_nk', fields=['StAppDate', 'StApplicationType', 'StBasicOutreachId']),
    ]

class PmYearProgramApplication(models.Model):
  """
  This table contains information pertaining to the application process.
  """

  GeneralApplication = models.ForeignKey(PmGeneralApplication, null=False, blank=False, related_name="PmYearProgramApplication_GeneralApplication", on_delete=models.CASCADE)
  # Date of application
  YpAppDate = models.DateTimeField(null=False, blank=False)
  # Describes what the application is for, eg. conference, year program.
  YpBasicAppType = models.CharField(max_length=16, null=False, blank=False)
  # This field will not appear on the screen but will be updated when someone chooses to delete a record. Rather that an actual deletion, the record will be 'marked' for deletion after an agreed upon interval.
  YpBasicDelete = models.BooleanField(default=False)
  # Indicates booking at an orientation session.
  HoOrientConfBookingKey = models.CharField(max_length=8)
  # The agreed support figure.
  YpAgreedSupportFigure = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Indicates the agreed upon joining charge for the conference <br/>and / or the summer outreach.
  YpAgreedJoiningCharge = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Period of time the support covers..
  YpSupportPeriod = models.CharField(max_length=12)
  # Indicates which New Recruits Conference the applicant plans to attend.
  YpJoiningConf = models.IntegerField(default=1)
  # This is the expected date their commitment starts.
  StartOfCommitment = models.DateTimeField()
  # This is the expected date their commitment ends.
  EndOfCommitment = models.DateTimeField()
  # Indicates how long the applicant intends to stay with us
  IntendedComLengthMonths = models.IntegerField()
  # Indicates if the assignment is in assistance to the given position.
  AssistantTo = models.BooleanField(default=False)
  Position = models.ForeignKey(PtPosition, related_name="PmYearProgramApplication_Position", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pm_year_program_application_pk', fields=['GeneralApplication']),
    ]

class PmDocument(models.Model):
  """
  Document
  """

  # This is the key that tell what site created this document
  SiteKey = models.IntegerField(default=0, null=False, blank=False)
  # Key to identify the document
  DocumentKey = models.IntegerField(default=0, null=False, blank=False)
  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPerson, null=False, blank=False, related_name="PmDocument_Partner", on_delete=models.CASCADE)
  # This code indicates the type of document for a person.
  Doc = models.ForeignKey(PmDocumentType, null=False, blank=False, related_name="PmDocument_Doc", on_delete=models.CASCADE)
  # Document ID
  DocumentId = models.CharField(max_length=30)
  # Place the document was issued.
  PlaceOfIssue = models.CharField(max_length=40)
  # The date the document was issued.
  DateOfIssue = models.DateTimeField()
  # Date the document takes effect.
  DateOfStart = models.DateTimeField()
  # Date the document expires
  DateOfExpiration = models.DateTimeField()
  # Comments and details
  DocComment = models.CharField(max_length=500)
  # ID of associated document
  AssocDocId = models.CharField(max_length=20)
  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  ContactPartner = models.ForeignKey(PPartner, related_name="PmDocument_ContactPartner", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pm_document_pk', fields=['SiteKey', 'DocumentKey']),
    ]

class PmPassportDetails(models.Model):
  """
  Passport Details
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPerson, null=False, blank=False, related_name="PmPassportDetails_Partner", on_delete=models.CASCADE)
  # Passport Number
  PassportNumber = models.CharField(max_length=20, null=False, blank=False)
  # Is this the main passport?
  MainPassport = models.BooleanField(default=False)
  # Indicates whether the passport is active or not.
  ActiveFlag = models.CharField(max_length=3)
  # Full passport name.
  FullPassportName = models.CharField(max_length=40)
  # Date of Birth
  PassportDob = models.DateTimeField()
  # Location of birth, eg. Cleveland, Ohio, USA, or Oswestry,Shropshire, England.
  PlaceOfBirth = models.CharField(max_length=30)
  # Nationality of the passport holder.
  PassportNationality = models.ForeignKey(PCountry, related_name="PmPassportDetails_PassportNationality", on_delete=models.CASCADE)
  # Date the passport expires
  DateOfExpiration = models.DateTimeField()
  # Place the passport was issued.
  PlaceOfIssue = models.CharField(max_length=20)
  # Country the passport was issued.
  CountryOfIssue = models.ForeignKey(PCountry, related_name="PmPassportDetails_CountryOfIssue", on_delete=models.CASCADE)
  # The date the passport was issued.
  DateOfIssue = models.DateTimeField()
  # Details the type of passport, e.g. Residence, Diplomatic, etc.
  PassportDetailsType = models.ForeignKey(PtPassportType, related_name="PmPassportDetails_PassportDetailsType", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pm_passport_details_pk', fields=['Partner', 'PassportNumber']),
    ]

class PmPersonLanguage(models.Model):
  """
  This table contains detail about the <br/>language the person speaks.
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPerson, null=False, blank=False, related_name="PmPersonLanguage_Partner", on_delete=models.CASCADE)
  # Name of the language(s) spoken.
  Language = models.ForeignKey(PLanguage, null=False, blank=False, related_name="PmPersonLanguage_Language", on_delete=models.CASCADE)
  # Years of experience this person has spoken this language.
  YearsOfExperience = models.IntegerField(default=99, null=False, blank=False)
  # The date the years of experience were up to date.
  YearsOfExperienceAsOf = models.DateTimeField()
  # This field is a numeric representation of level of language.
  LanguageLevel = models.ForeignKey(PtLanguageLevel, null=False, blank=False, related_name="PmPersonLanguage_LanguageLevel", on_delete=models.CASCADE)
  Comment = models.CharField(max_length=256)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pm_person_language_pk', fields=['Partner', 'Language']),
    ]

class PmPastExperience(models.Model):
  """
  This details any previous ministry experience the individual has. 
  """

  # The connection to the site
  SiteKey = models.IntegerField(default=0, null=False, blank=False)
  # Key to make editing these records easier
  Key = models.IntegerField(null=False, blank=False)
  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPerson, null=False, blank=False, related_name="PmPastExperience_Partner", on_delete=models.CASCADE)
  # Start date of previous experience.
  StartDate = models.DateTimeField()
  # End date of previous experience.
  EndDate = models.DateTimeField()
  # Location of previous work .
  PrevLocation = models.CharField(max_length=30, null=False, blank=False)
  # Describes role played in previous work.
  PrevRole = models.CharField(max_length=30)
  # Category/area of previous work
  Category = models.CharField(max_length=30)
  # Worked with which organisation before (if other than our organisation).
  OtherOrganisation = models.CharField(max_length=25)
  # Comments on previous experience.
  PastExpComments = models.CharField(max_length=320)
  # Indicates if past experience was with this organisation.
  PrevWorkHere = models.BooleanField(default=False)
  # Indicates whether the individual has previous worked with similar organisations.
  PrevWork = models.BooleanField(default=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pm_past_experience_pk', fields=['SiteKey', 'Key']),
      models.UniqueConstraint(name='pm_past_experience_uk', fields=['Partner', 'EndDate', 'StartDate', 'PrevLocation']),
    ]

class PmPersonAbility(models.Model):
  """
  This table describes the ability or <br/>abilities one possesses.
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPerson, null=False, blank=False, related_name="PmPersonAbility_Partner", on_delete=models.CASCADE)
  # Name of the area of ability
  AbilityArea = models.ForeignKey(PtAbilityArea, null=False, blank=False, related_name="PmPersonAbility_AbilityArea", on_delete=models.CASCADE)
  # This field is a numeric representation of level of ability.
  AbilityLevel = models.ForeignKey(PtAbilityLevel, null=False, blank=False, related_name="PmPersonAbility_AbilityLevel", on_delete=models.CASCADE)
  # Years of experience this person has had this ability.
  YearsOfExperience = models.IntegerField(default=99, null=False, blank=False)
  # The date the years of experience were up to date.
  YearsOfExperienceAsOf = models.DateTimeField()
  # Indicates whether the applicant is bringing his instrument.
  BringingInstrument = models.BooleanField(default=False)
  Comment = models.CharField(max_length=256)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pm_person_ability_pk', fields=['Partner', 'AbilityArea']),
    ]

class PmPersonQualification(models.Model):
  """
  This table provides detail on qualifications someone may possess.
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPerson, null=False, blank=False, related_name="PmPersonQualification_Partner", on_delete=models.CASCADE)
  # Name of the area of qualification.
  QualificationArea = models.ForeignKey(PtQualificationArea, null=False, blank=False, related_name="PmPersonQualification_QualificationArea", on_delete=models.CASCADE)
  # Years of experience this person has had this qualification.
  YearsOfExperience = models.IntegerField(default=99, null=False, blank=False)
  # The date the years of experience were up to date.
  YearsOfExperienceAsOf = models.DateTimeField()
  # This field indicate whether the qualifications are the result of <br/>informal training.
  Informal = models.BooleanField(default=False, null=False, blank=False)
  # This field is a numeric representation of level of qualification.
  QualificationLevel = models.ForeignKey(PtQualificationLevel, null=False, blank=False, related_name="PmPersonQualification_QualificationLevel", on_delete=models.CASCADE)
  Comment = models.CharField(max_length=256)
  # The date the person qualified.
  QualificationDate = models.DateTimeField()
  # The date the qualification expires.
  QualificationExpiry = models.DateTimeField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pm_person_qualification_pk', fields=['Partner', 'QualificationArea']),
    ]

class PmPersonSkill(models.Model):
  """
  This table describes the skills that a person has (including professional skills but also other ones).
  """

  PersonSkillKey = models.IntegerField(null=False, blank=False, unique=True)
  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPerson, null=False, blank=False, related_name="PmPersonSkill_Partner", on_delete=models.CASCADE)
  # Skill Category
  SkillCategory = models.ForeignKey(PtSkillCategory, null=False, blank=False, related_name="PmPersonSkill_SkillCategory", on_delete=models.CASCADE)
  # Description of skill in english language
  DescriptionEnglish = models.CharField(max_length=80, null=False, blank=False)
  # Description of skill in local language
  DescriptionLocal = models.CharField(max_length=80)
  # Language that is used in field pm_description_local_c
  DescriptionLanguage = models.ForeignKey(PLanguage, related_name="PmPersonSkill_DescriptionLanguage", on_delete=models.CASCADE)
  # This field is a numeric representation of level of skill.
  SkillLevel = models.ForeignKey(PtSkillLevel, null=False, blank=False, related_name="PmPersonSkill_SkillLevel", on_delete=models.CASCADE)
  # Years of experience this person has had this skill.
  YearsOfExperience = models.IntegerField(default=99)
  # The date the years of experience were up to date.
  YearsOfExperienceAsOf = models.DateTimeField()
  # Indicates if this is a professional skill
  ProfessionalSkill = models.BooleanField(default=False)
  # Indicates if this is the person's current occupation
  CurrentOccupation = models.BooleanField(default=False)
  # Degree that is linked with the skill (if applicable)
  Degree = models.CharField(max_length=80)
  # Year the degree was obtained.
  YearOfDegree = models.IntegerField()
  Comment = models.CharField(max_length=500)


class PmFormalEducation(models.Model):
  """
  This table records the formal education that a person has
  """

  FormalEducationKey = models.IntegerField(null=False, blank=False, unique=True)
  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPerson, null=False, blank=False, related_name="PmFormalEducation_Partner", on_delete=models.CASCADE)
  # Education Category
  EducationCategory = models.CharField(max_length=30)
  # Description of degree (incl. title and subject)
  Degree = models.CharField(max_length=80)
  # Year the degree was obtained.
  YearOfDegree = models.IntegerField(default=99)
  # Institution the degree was obtained from
  Institution = models.CharField(max_length=80)
  # Code of country in which the degree was obtained
  Country = models.ForeignKey(PCountry, related_name="PmFormalEducation_Country", on_delete=models.CASCADE)
  Comment = models.CharField(max_length=1000)


class PmPersonalData(models.Model):
  """
  This table contains personal data about our staff, eg. tax id.
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPerson, null=False, blank=False, related_name="PmPersonalData_Partner", on_delete=models.CASCADE)
  # The person's height in cm
  HeightCm = models.IntegerField()
  # The person's weight in kg
  WeightKg = models.DecimalField(max_digits=5, decimal_places=2)
  # The person's eye colour
  EyeColour = models.CharField(max_length=20)
  # The person's hair colour
  HairColour = models.CharField(max_length=20)
  # Information about the person's facial hair, e.g. beard, mustache
  FacialHair = models.CharField(max_length=30)
  # Further physical information about the person like tatoos, piercings, scars or marks
  PhysicalDesc = models.CharField(max_length=250)
  # The person's blood type
  BloodType = models.CharField(max_length=10)
  # Ethnic Origin
  EthnicOrigin = models.CharField(max_length=30)
  # Proof of life question 1
  LifeQuestion1 = models.CharField(max_length=100)
  # Answer to proof of life question 1
  LifeAnswer1 = models.CharField(max_length=100)
  # Proof of life question 2
  LifeQuestion2 = models.CharField(max_length=100)
  # Answer to proof of life question 2
  LifeAnswer2 = models.CharField(max_length=100)
  # Proof of life question 3
  LifeQuestion3 = models.CharField(max_length=100)
  # Answer to proof of life question 3
  LifeAnswer3 = models.CharField(max_length=100)
  # Proof of life question 4
  LifeQuestion4 = models.CharField(max_length=100)
  # Answer to proof of life question 4
  LifeAnswer4 = models.CharField(max_length=100)
  # User defined field-1 for personal information (not in use any longer, replaced by p_data_label_value_partner)
  PersonalFld1 = models.CharField(max_length=25)
  # User defined field-2 for personal information (not in use any longer, replaced by p_data_label_value_partner)
  PersonalFld2 = models.CharField(max_length=25)
  # User defined field-3 for personal information (not in use any longer, replaced by p_data_label_value_partner)
  PersonalFld3 = models.CharField(max_length=25)
  # User defined field-4 for personal information (not in use any longer, replaced by p_data_label_value_partner)
  PersonalFld4 = models.CharField(max_length=25)
  # User defined field-5 for personal information (not in use any longer, replaced by p_data_label_value_partner)
  PersonalFld5 = models.CharField(max_length=25)
  # User defined field-6 for personal information (not in use any longer, replaced by p_data_label_value_partner)
  PersonalFld6 = models.CharField(max_length=25)
  # Name of the person's first language.
  Language = models.ForeignKey(PLanguage, related_name="PmPersonalData_Language", on_delete=models.CASCADE)
  # This is the year the person became a Believer.
  BelieverSinceYear = models.IntegerField()
  # Comment about the year or how the person became a believer
  BelieverSinceComment = models.CharField(max_length=500)


class PDataLabelValuePartner(models.Model):
  """
  This table holds the label values for partner related data.
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PDataLabelValuePartner_Partner", on_delete=models.CASCADE)
  # A sequence key for data labels.
  DataLabel = models.ForeignKey(PDataLabel, null=False, blank=False, related_name="PDataLabelValuePartner_DataLabel", on_delete=models.CASCADE)
  # Label value for type Character.
  ValueChar = models.CharField(max_length=4096)
  # Label value for type Numeric.
  ValueNum = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Label value for type Currency.
  ValueCurrency = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Label value for type Integer.
  ValueInt = models.IntegerField(default=0)
  # Label value for type Boolean.
  ValueBool = models.BooleanField(default=False)
  # Label value for type Date.
  ValueDate = models.DateTimeField()
  # Label value for type Time.
  ValueTime = models.IntegerField(default=0)
  # Label value for type Partner Key.
  ValuePartner = models.ForeignKey(PPartner, related_name="PDataLabelValuePartner_ValuePartner", on_delete=models.CASCADE)
  # Label value for type Lookup Value.
  ValueLookup = models.CharField(max_length=40)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_data_label_value_partner_pk', fields=['Partner', 'DataLabel']),
    ]

class PDataLabelValueApplication(models.Model):
  """
  This table holds the label values for application related data.
  """

  GeneralApplication = models.ForeignKey(PmGeneralApplication, null=False, blank=False, related_name="PDataLabelValueApplication_GeneralApplication", on_delete=models.CASCADE)
  # A sequence key for data labels.
  DataLabel = models.ForeignKey(PDataLabel, null=False, blank=False, related_name="PDataLabelValueApplication_DataLabel", on_delete=models.CASCADE)
  # Label value for type Character.
  ValueChar = models.CharField(max_length=4096)
  # Label value for type Numeric.
  ValueNum = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Label value for type Currency.
  ValueCurrency = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Label value for type Integer.
  ValueInt = models.IntegerField(default=0)
  # Label value for type Boolean.
  ValueBool = models.BooleanField(default=False)
  # Label value for type Date.
  ValueDate = models.DateTimeField()
  # Label value for type Time.
  ValueTime = models.IntegerField(default=0)
  # Label value for type Partner Key.
  ValuePartner = models.ForeignKey(PPartner, related_name="PDataLabelValueApplication_ValuePartner", on_delete=models.CASCADE)
  # Label value for type Lookup Value.
  ValueLookup = models.CharField(max_length=40)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_data_label_value_application_pk', fields=['GeneralApplication', 'DataLabel']),
    ]

class PmPersonEvaluation(models.Model):
  """
  This table contains information regarding personal progress reports.
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPerson, null=False, blank=False, related_name="PmPersonEvaluation_Partner", on_delete=models.CASCADE)
  # The date the evaluation was conducted.
  EvaluationDate = models.DateTimeField(null=False, blank=False)
  # Describes the person who conducted the progress report.
  Evaluator = models.CharField(max_length=30, null=False, blank=False)
  # This field describes the timing of the progress report, eg.  Semi-Annual, Annual, or Leaving.
  EvaluationType = models.CharField(max_length=12, null=False, blank=False)
  # Comments on the progress report.
  EvaluationComments = models.CharField(max_length=500)
  # Describe possible actions to take.
  PersonEvalAction = models.CharField(max_length=500)
  # Date of next evaluation.
  NextEvaluationDate = models.DateTimeField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pm_person_evaluation_pk', fields=['Partner', 'EvaluationDate', 'Evaluator']),
    ]

class PmPersonAbsence(models.Model):
  """
  This table records the absence of a person (holiday, sickness, etc.)
  """

  PersonAbsenceKey = models.IntegerField(null=False, blank=False, unique=True)
  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPerson, null=False, blank=False, related_name="PmPersonAbsence_Partner", on_delete=models.CASCADE)
  # First day of abscence
  AbsenceFrom = models.DateTimeField()
  # Last day of abscence
  AbsenceTo = models.DateTimeField()
  # Total number of working days absent
  AbsenceDays = models.IntegerField()
  # Type of Absence
  AbsenceType = models.CharField(max_length=30)
  Comment = models.CharField(max_length=500)


class PmSpecialNeed(models.Model):
  """
  This table includes special medical or dietary needs someone may have.
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPerson, null=False, blank=False, related_name="PmSpecialNeed_Partner", on_delete=models.CASCADE)
  # Contains special medical information if needed.
  MedicalComment = models.CharField(max_length=2500)
  # Contains special dietary information if needed.
  DietaryComment = models.CharField(max_length=2500)
  # Contains any other special need that may be applicable.
  OtherSpecialNeed = models.CharField(max_length=2500)
  # Indicates if there are vegetarian needs.
  Vegetarian = models.BooleanField(default=False)


class PmStaffData(models.Model):
  """
  This table contains information regarding recruitment, home office, field office, etc. .
  """

  # The connection to the site
  SiteKey = models.IntegerField(default=0, null=False, blank=False)
  # Key to make editing these records easier
  Key = models.IntegerField(null=False, blank=False)
  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPerson, null=False, blank=False, related_name="PmStaffData_Partner", on_delete=models.CASCADE)
  # This is a field indicating the status of the commitment
  Status = models.ForeignKey(PmCommitmentStatus, related_name="PmStaffData_Status", on_delete=models.CASCADE)
  # This is the expected date their commitment starts.
  StartOfCommitment = models.DateTimeField(null=False, blank=False)
  # Is the commitment start date an approximate date?
  StartDateApprox = models.BooleanField(default=False)
  # This is the expected date their commitment ends.
  EndOfCommitment = models.DateTimeField()
  # The office that recruited the partner. This is a unit of type field, not of type office.
  OfficeRecruitedBy = models.ForeignKey(PUnit, null=False, blank=False, related_name="PmStaffData_OfficeRecruitedBy", on_delete=models.CASCADE)
  # The home office of the person. This is a unit of type field, not of type office.
  HomeOffice = models.ForeignKey(PUnit, null=False, blank=False, related_name="PmStaffData_HomeOffice", on_delete=models.CASCADE)
  # The person's is serving for that field.
  ReceivingField = models.ForeignKey(PUnit, null=False, blank=False, related_name="PmStaffData_ReceivingField", on_delete=models.CASCADE)
  # The office they work at in the receiving field.
  ReceivingFieldOffice = models.ForeignKey(PUnit, related_name="PmStaffData_ReceivingFieldOffice", on_delete=models.CASCADE)
  # Comments on commitment record.
  StaffDataComments = models.CharField(max_length=320)
  # A free text field for a job title for a person. This is not the same as the person's role, however it may be auto generated from the roles.
  JobTitle = models.CharField(max_length=200)
  # Phone extension of the person at this office
  OfficePhoneExt = models.CharField(max_length=25)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pm_staff_data_pk', fields=['SiteKey', 'Key']),
    ]

class PmPersonCommitmentStatus(models.Model):
  """
  This table holds the commitment type history of a person
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPerson, null=False, blank=False, related_name="PmPersonCommitmentStatus_Partner", on_delete=models.CASCADE)
  # Code for Status
  Status = models.ForeignKey(PmCommitmentStatus, null=False, blank=False, related_name="PmPersonCommitmentStatus_Status", on_delete=models.CASCADE)
  # This is the date since the status is valid
  StatusSince = models.DateTimeField(null=False, blank=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pm_person_commitment_status_pk', fields=['Partner', 'Status', 'StatusSince']),
    ]

class UmJob(models.Model):
  """
  This table contains information concerning jobs within the unit.
  """

  # This is the partner key of the unit. It consists of the fund id followed by a computer generated six digit number.
  Unit = models.ForeignKey(PUnit, null=False, blank=False, related_name="UmJob_Unit", on_delete=models.CASCADE)
  Position = models.ForeignKey(PtPosition, null=False, blank=False, related_name="UmJob_Position", on_delete=models.CASCADE)
  # To make sure we can have two jobs in difference time-frames
  JobKey = models.IntegerField(null=False, blank=False)
  # Indicates the normal length of commitment, eg. short-term.
  JobType = models.CharField(max_length=20, default='Short Term', null=False, blank=False)
  # Date from um_training_period.
  FromDate = models.DateTimeField()
  # Date the job posting is to.
  ToDate = models.DateTimeField()
  # Indicates the minimum number of staff required.
  Minimum = models.IntegerField(default=0)
  # Indicates the maximum number of staff required.
  Maximum = models.IntegerField(default=0)
  # Indicates the present number on staff.
  Present = models.IntegerField(default=0)
  # Number of part-timers acceptable.
  PartTimers = models.IntegerField(default=0)
  # Number of applications on file for this position. This field is driven from the pm_job_assignment.
  Applications = models.IntegerField(default=0)
  # Indicates if part-timers can be accepted for this position.
  PartTime = models.BooleanField(default=False)
  # Length of training required for this position.
  TrainingPeriod = models.CharField(max_length=15, default='One month', null=False, blank=False)
  # Length of commitment required for this position.
  CommitmentPeriod = models.CharField(max_length=15, default='Three months', null=False, blank=False)
  # Is this position available to other systems.
  Public = models.BooleanField(default=False)
  # Describes where you want to advertise about a job opening, only within the Unit, to the whole organisation, or outside our organisation.
  JobPublicity = models.IntegerField(default=0)
  # Indicates whether previous experience with our organisation is required for this job.
  PreviousInternalExpReq = models.BooleanField(default=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='um_job_pk', fields=['Unit', 'Position', 'JobKey']),
    ]

class UmJobRequirement(models.Model):
  """
  Lists abilities and experience required for various positions.
  """

  Job = models.ForeignKey(UmJob, null=False, blank=False, related_name="UmJobRequirement_Job", on_delete=models.CASCADE)
  # Name of the area of ability
  AbilityArea = models.ForeignKey(PtAbilityArea, null=False, blank=False, related_name="UmJobRequirement_AbilityArea", on_delete=models.CASCADE)
  # Years of experience required for this position..
  YearsOfExperience = models.IntegerField(default=99, null=False, blank=False)
  # This field is a numeric representation of level of ability.
  AbilityLevel = models.ForeignKey(PtAbilityLevel, related_name="UmJobRequirement_AbilityLevel", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='um_job_requirement_pk', fields=['Job', 'AbilityArea']),
    ]

class UmJobLanguage(models.Model):
  """
  Language used on this job.
  """

  Job = models.ForeignKey(UmJob, null=False, blank=False, related_name="UmJobLanguage_Job", on_delete=models.CASCADE)
  # Name of the language(s) spoken.
  Language = models.ForeignKey(PLanguage, null=False, blank=False, related_name="UmJobLanguage_Language", on_delete=models.CASCADE)
  # Years of experience required using this language.
  YearsOfExperience = models.IntegerField(default=99, null=False, blank=False)
  # This field is a numeric representation of level of language.
  LanguageLevel = models.ForeignKey(PtLanguageLevel, related_name="UmJobLanguage_LanguageLevel", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='um_job_language_pk', fields=['Job', 'Language']),
    ]

class UmJobQualification(models.Model):
  """
  Details of qualifications required for individual jobs.
  """

  Job = models.ForeignKey(UmJob, null=False, blank=False, related_name="UmJobQualification_Job", on_delete=models.CASCADE)
  # Name of the area of qualification.
  QualificationArea = models.ForeignKey(PtQualificationArea, null=False, blank=False, related_name="UmJobQualification_QualificationArea", on_delete=models.CASCADE)
  # Years of experience required using this qualification.
  YearsOfExperience = models.IntegerField(default=99)
  # This field indicate whether the qualifications can be the result of <br/>informal training.
  Informal = models.BooleanField(default=False)
  # This field is a numeric representation of level of qualification.
  QualificationLevel = models.ForeignKey(PtQualificationLevel, related_name="UmJobQualification_QualificationLevel", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='um_job_qualification_pk', fields=['Job', 'QualificationArea']),
    ]

class PmJobAssignment(models.Model):
  """
  This defines the position one fills.
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PmJobAssignment_Partner", on_delete=models.CASCADE)
  Job = models.ForeignKey(UmJob, null=False, blank=False, related_name="PmJobAssignment_Job", on_delete=models.CASCADE)
  # A number to make this unique as other wise we would need to add date from/to
  JobAssignmentKey = models.IntegerField(null=False, blank=False)
  # Indicates if the assignment is in assistance to the given position.
  AssistantTo = models.BooleanField(default=False)
  # This defines the type of assignment.
  AssignmentType = models.ForeignKey(PtAssignmentType, related_name="PmJobAssignment_AssignmentType", on_delete=models.CASCADE)
  # Can these costs be changed?
  CostsChanged = models.BooleanField(default=False)
  # This is the date from which this job is assigned.
  FromDate = models.DateTimeField(null=False, blank=False)
  # This is the date to which a job is expected to be filled.
  ToDate = models.DateTimeField()
  # This field indicates if the hard copy details have been changed.
  HrdCpyDetailChange = models.BooleanField(default=False)
  # This field indicates if the record is deletable.
  Deleteable = models.BooleanField(default=False)
  # The office that entered this assignment
  RegistrationOffice = models.IntegerField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pm_job_assignment_pk', fields=['Partner', 'Job', 'JobAssignmentKey']),
    ]

class UmUnitAbility(models.Model):
  """
  Details of  the abilities within the unit.
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PUnit, null=False, blank=False, related_name="UmUnitAbility_Partner", on_delete=models.CASCADE)
  # Name of the area of ability
  AbilityArea = models.ForeignKey(PtAbilityArea, null=False, blank=False, related_name="UmUnitAbility_AbilityArea", on_delete=models.CASCADE)
  # Years of experience this required for this ability.
  YearsOfExperience = models.IntegerField(default=99, null=False, blank=False)
  # This field is a numeric representation of level of ability.
  AbilityLevel = models.ForeignKey(PtAbilityLevel, null=False, blank=False, related_name="UmUnitAbility_AbilityLevel", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='um_unit_ability_pk', fields=['Partner', 'AbilityArea']),
    ]

class UmUnitLanguage(models.Model):
  """
  Details of the language used within this unit.
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PUnit, null=False, blank=False, related_name="UmUnitLanguage_Partner", on_delete=models.CASCADE)
  # Name of the language(s) spoken.
  Language = models.ForeignKey(PLanguage, null=False, blank=False, related_name="UmUnitLanguage_Language", on_delete=models.CASCADE)
  # This field is a numeric representation of level of language.
  LanguageLevel = models.ForeignKey(PtLanguageLevel, null=False, blank=False, related_name="UmUnitLanguage_LanguageLevel", on_delete=models.CASCADE)
  # Years of experience required using this language.
  YearsOfExperience = models.IntegerField(default=99, null=False, blank=False)
  # Contains comments pertaining to the language of the unit.
  UnitLangComment = models.CharField(max_length=40)
  # Lists whether the languare is required or desired.
  UnitLanguageReq = models.CharField(max_length=8)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='um_unit_language_pk', fields=['Partner', 'Language', 'LanguageLevel']),
    ]

class UmUnitCost(models.Model):
  """
  Details pertaining to the costs of being on in the unit.
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PUnit, null=False, blank=False, related_name="UmUnitCost_Partner", on_delete=models.CASCADE)
  # Date from which these costs are applicable.
  ValidFromDate = models.DateTimeField(null=False, blank=False)
  # Indicates amount it costs a single to be on the team.
  SingleCostsPeriodIntl = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Indicates amount it costs a couple to be on the team.
  CoupleCostsPeriodIntl = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Indicates amount it costs a child to be on the team.
  Child1CostsPeriodIntl = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Indicates amount it costs a child to be on the team.
  Child2CostsPeriodIntl = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Indicates amount it costs a child to be on the team.
  Child3CostsPeriodIntl = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Indicates the joining charge for adults.
  AdultJoiningChargeIntl = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Indicates the joining charge for couples.
  CoupleJoiningChargeIntl = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Indicates the joining charge for a child.
  ChildJoiningChargeIntl = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Indicates the local currency.
  LocalCurrency = models.ForeignKey(ACurrency, related_name="UmUnitCost_LocalCurrency", on_delete=models.CASCADE)
  # The charge period for the unit, eg. monthly, quarterly.
  ChargePeriod = models.CharField(max_length=12, null=False, blank=False)
  # Indicates amount it costs a single to be on the team.
  SingleCostsPeriodBase = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Indicates amount it costs a couple to be on the team.
  CoupleCostsPeriodBase = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Indicates amount it costs a child to be on the team.
  Child1CostsPeriodBase = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Indicates amount it costs a child to be on the team.
  Child2CostsPeriodBase = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Indicates amount it costs a child to be on the team.
  Child3CostsPeriodBase = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Indicates the joining charge for adults.
  AdultJoiningChargeBase = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Indicates the joining charge for couples.
  CoupleJoiningChargeBase = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Indicates the joining charge for a child.
  ChildJoiningChargeBase = models.DecimalField(max_digits=24, decimal_places=10, default=0)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='um_unit_cost_pk', fields=['Partner', 'ValidFromDate']),
    ]

class UmUnitEvaluation(models.Model):
  """
  Details pertaining to evaluation of the unit.
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PUnit, null=False, blank=False, related_name="UmUnitEvaluation_Partner", on_delete=models.CASCADE)
  # Indicates the date of the evaluation.
  DateOfEvaluation = models.DateTimeField(null=False, blank=False)
  # The evaluation number is generated from a database sequence
  EvaluationNumber = models.IntegerField(default=0, null=False, blank=False)
  # Indicates whether the evaluator is married, single, etc.
  EvaluatorFamilyStatus = models.CharField(max_length=20, null=False, blank=False)
  # The name of the evaluator's home country.
  EvaluatorHomeCountry = models.CharField(max_length=20, null=False, blank=False)
  # Age of the person conduction the unit evaluation.
  EvaluatorAge = models.IntegerField(default=0, null=False, blank=False)
  EvaluatorSex = models.CharField(max_length=20, null=False, blank=False)
  # Data regarding the unit evaluation.
  UnitEvaluationData = models.CharField(max_length=80)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='um_unit_evaluation_pk', fields=['Partner', 'DateOfEvaluation', 'EvaluationNumber']),
    ]

class PcConference(models.Model):
  """
  Basic details about a conference
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Conference = models.ForeignKey(PUnit, null=False, blank=False, related_name="PcConference_Conference", on_delete=models.CASCADE)
  OutreachPrefix = models.CharField(max_length=5)
  Start = models.DateTimeField()
  End = models.DateTimeField()
  # This defines which currency is being used
  Currency = models.ForeignKey(ACurrency, null=False, blank=False, related_name="PcConference_Currency", on_delete=models.CASCADE)


class PcConferenceOption(models.Model):
  """
  Lists options that are set for a conference
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Conference = models.ForeignKey(PcConference, null=False, blank=False, related_name="PcConferenceOption_Conference", on_delete=models.CASCADE)
  # Unique name of the cost type
  OptionType = models.ForeignKey(PcConferenceOptionType, null=False, blank=False, related_name="PcConferenceOption_OptionType", on_delete=models.CASCADE)
  # Description of the option type
  OptionSet = models.BooleanField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pc_conference_option_pk', fields=['Conference', 'OptionType']),
    ]

class PcDiscount(models.Model):
  """
  Lists optional discounts for a conference
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Conference = models.ForeignKey(PcConference, null=False, blank=False, related_name="PcDiscount_Conference", on_delete=models.CASCADE)
  # Unique name of the criteria that a person has to meet to get the discount
  DiscountCriteria = models.ForeignKey(PcDiscountCriteria, null=False, blank=False, related_name="PcDiscount_DiscountCriteria", on_delete=models.CASCADE)
  # Unique name of the cost type
  CostType = models.ForeignKey(PcCostType, null=False, blank=False, related_name="PcDiscount_CostType", on_delete=models.CASCADE)
  # When is this discount valid (PRE, CONF, POST, ALWAYS)
  Validity = models.CharField(max_length=3, null=False, blank=False)
  # For discounts up to a certain age (mainly child discount). If age does not matter, set to -1.
  UpToAge = models.IntegerField(null=False, blank=False)
  # Is the discount value given in percent (or total otherwise)
  Percentage = models.BooleanField()
  # Amount of discount (in percent or total)
  Discount = models.DecimalField(max_digits=24, decimal_places=10)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pc_discount_pk', fields=['Conference', 'DiscountCriteria', 'CostType', 'Validity', 'UpToAge']),
    ]

class PcAttendee(models.Model):
  """
  Lists the attendees at a conference
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Conference = models.ForeignKey(PcConference, null=False, blank=False, related_name="PcAttendee_Conference", on_delete=models.CASCADE)
  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPerson, null=False, blank=False, related_name="PcAttendee_Partner", on_delete=models.CASCADE)
  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  HomeOffice = models.ForeignKey(PUnit, null=False, blank=False, related_name="PcAttendee_HomeOffice", on_delete=models.CASCADE)
  OutreachType = models.CharField(max_length=6)
  ActualArr = models.DateTimeField()
  ActualDep = models.DateTimeField()
  BadgePrint = models.DateTimeField()
  DetailsPrint = models.DateTimeField()
  Comments = models.CharField(max_length=500)
  DiscoveryGroup = models.CharField(max_length=16)
  WorkGroup = models.CharField(max_length=16)
  Registered = models.DateTimeField()
  ArrivalGroup = models.CharField(max_length=20)
  DepartureGroup = models.CharField(max_length=20)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pc_attendee_pk', fields=['Conference', 'Partner']),
    ]

class PcConferenceCost(models.Model):
  """
  Charges for the various outreach options from a conference (currency held in conference master)
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Conference = models.ForeignKey(PcConference, null=False, blank=False, related_name="PcConferenceCost_Conference", on_delete=models.CASCADE)
  # 9999999999
  OptionDays = models.IntegerField(default=0, null=False, blank=False)
  Charge = models.DecimalField(max_digits=24, decimal_places=10, default=0)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pc_conference_cost_pk', fields=['Conference', 'OptionDays']),
    ]

class PcExtraCost(models.Model):
  """
  Contains extra conference costs for individual attendees
  """

  Attendee = models.ForeignKey(PcAttendee, null=False, blank=False, related_name="PcExtraCost_Attendee", on_delete=models.CASCADE)
  # Key to identify the extra cost, along with conference and partner key
  ExtraCostKey = models.IntegerField(default=0, null=False, blank=False)
  CostType = models.ForeignKey(PcCostType, related_name="PcExtraCost_CostType", on_delete=models.CASCADE)
  CostAmount = models.DecimalField(max_digits=24, decimal_places=10)
  Comment = models.CharField(max_length=256)
  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  AuthorisingField = models.ForeignKey(PUnit, related_name="PcExtraCost_AuthorisingField", on_delete=models.CASCADE)
  # Indicate who authorised the extra cost.
  AuthorisingPerson = models.CharField(max_length=20)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pc_extra_cost_pk', fields=['Attendee', 'ExtraCostKey']),
    ]

class PcEarlyLate(models.Model):
  """
  Discounts and Supplements for early or late registration
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Conference = models.ForeignKey(PcConference, null=False, blank=False, related_name="PcEarlyLate_Conference", on_delete=models.CASCADE)
  Applicable = models.DateTimeField(null=False, blank=False)
  Type = models.BooleanField()
  AmountPercent = models.BooleanField()
  Amount = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  Percent = models.IntegerField(default=0)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pc_early_late_pk', fields=['Conference', 'Applicable']),
    ]

class PcGroup(models.Model):
  """
  Contains information about which groups individual attendees are assigned to
  """

  Attendee = models.ForeignKey(PcAttendee, null=False, blank=False, related_name="PcGroup_Attendee", on_delete=models.CASCADE)
  GroupType = models.CharField(max_length=20, null=False, blank=False)
  Name = models.CharField(max_length=40, null=False, blank=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pc_group_pk', fields=['Attendee', 'GroupType', 'Name']),
    ]

class PcSupplement(models.Model):
  """
  outreach travel supplements (by outreach ID)
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Conference = models.ForeignKey(PcConference, null=False, blank=False, related_name="PcSupplement_Conference", on_delete=models.CASCADE)
  OutreachType = models.CharField(max_length=6, null=False, blank=False)
  Supplement = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  # Apply conference fee discounts to this supplement
  ApplyDiscounts = models.BooleanField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pc_supplement_pk', fields=['Conference', 'OutreachType']),
    ]

class PcBuilding(models.Model):
  """
  Details of building used for accomodation at a conference
  """

  Venue = models.ForeignKey(PVenue, null=False, blank=False, related_name="PcBuilding_Venue", on_delete=models.CASCADE)
  Code = models.CharField(max_length=8, null=False, blank=False)
  # This is a long description and is 80 characters long.
  Desc = models.CharField(max_length=80)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pc_building_pk', fields=['Venue', 'Code']),
    ]

class PcRoom(models.Model):
  """
  Details of rooms used for accommodation at a conference
  """

  Building = models.ForeignKey(PcBuilding, null=False, blank=False, related_name="PcRoom_Building", on_delete=models.CASCADE)
  RoomNumber = models.CharField(max_length=8, null=False, blank=False)
  Name = models.CharField(max_length=50)
  Beds = models.IntegerField(default=0)
  MaxOccupancy = models.IntegerField(default=0)
  BedCharge = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  BedCost = models.DecimalField(max_digits=24, decimal_places=10, default=0)
  Usage = models.CharField(max_length=16)
  # Gender that is preferred to use that room
  GenderPreference = models.CharField(max_length=3)
  # X Position for the room layout designer in pixels
  LayoutXpos = models.IntegerField()
  # Y Position for the room layout designer in pixels
  LayoutYpos = models.IntegerField()
  # Width for the room layout designer in pixels
  LayoutWidth = models.IntegerField()
  # Height for the room layout designer in pixels
  LayoutHeight = models.IntegerField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pc_room_pk', fields=['Building', 'RoomNumber']),
    ]

class PcRoomAlloc(models.Model):
  """
  Links rooms to attendees of a conference or a booking in the hospitality module
  """

  # Surrogate Primary Key; required because there can be several bookings per room, and not all guests might be linked to a partner
  Key = models.IntegerField(null=False, blank=False, unique=True)
  # This makes the room unavailable for other guests even if not all beds are used
  BookWholeRoom = models.BooleanField(default=True, null=False, blank=False)
  # number of beds required by this allocation
  NumberOfBeds = models.IntegerField(default=1)
  # number of additional beds (e.g. mattrass, childrens cot, etc) required by this allocation
  NumberOfOverflowBeds = models.IntegerField(default=0)
  # possible values: couple, family, male, female
  Gender = models.CharField(max_length=20)
  In = models.DateTimeField(null=False, blank=False)
  Out = models.DateTimeField()
  Attendee = models.ForeignKey(PcAttendee, related_name="PcRoomAlloc_Attendee", on_delete=models.CASCADE)
  Room = models.ForeignKey(PcRoom, null=False, blank=False, related_name="PcRoomAlloc_Room", on_delete=models.CASCADE)


class PcRoomAttribute(models.Model):
  """
  Attributes assigned to rooms used for accommodation at a conference
  """

  Room = models.ForeignKey(PcRoom, null=False, blank=False, related_name="PcRoomAttribute_Room", on_delete=models.CASCADE)
  RoomAttrType = models.ForeignKey(PcRoomAttributeType, null=False, blank=False, related_name="PcRoomAttribute_RoomAttrType", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pc_room_attribute_pk', fields=['Room', 'RoomAttrType']),
    ]

class PcConferenceVenue(models.Model):
  """
  Links venues to conferences
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Conference = models.ForeignKey(PcConference, null=False, blank=False, related_name="PcConferenceVenue_Conference", on_delete=models.CASCADE)
  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Venue = models.ForeignKey(PVenue, null=False, blank=False, related_name="PcConferenceVenue_Venue", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='pc_conference_venue_pk', fields=['Conference', 'Venue']),
    ]

class PhBooking(models.Model):
  """
  make sure charging works for a group or an individual; this summarises all the hospitality services that have to be paid for; also useful for planning meals in the kitchen and room preparation
  """

  # Surrogate Primary Key; required because there can be several bookings per room and per group
  Key = models.IntegerField(null=False, blank=False, unique=True)
  # the partner key of the visitor or the partner key of the organisation or group that is visiting; each room allocation can refer to the individual guest as well; this can be different from the partner that is charged in the invoice
  Contact = models.ForeignKey(PPartner, related_name="PhBooking_Contact", on_delete=models.CASCADE)
  # This is a booking for n adults
  NumberOfAdults = models.IntegerField(default=0)
  # This is a booking for n children
  NumberOfChildren = models.IntegerField(default=0)
  # The people that are part of this booking had n breakfasts; also useful for the kitchen
  NumberOfBreakfast = models.IntegerField(default=0)
  # The people that are part of this booking had n lunches
  NumberOfLunch = models.IntegerField(default=0)
  # The people that are part of this booking had n suppers
  NumberOfSupper = models.IntegerField(default=0)
  # The number of linen that have been provided for this booking
  NumberOfLinenNeeded = models.IntegerField(default=0)
  # this should be set to the date when the booking has been confirmed; required for early booking discounts
  Confirmed = models.DateTimeField()
  In = models.DateTimeField(null=False, blank=False)
  Out = models.DateTimeField()
  TimeArrival = models.IntegerField()
  TimeDeparture = models.IntegerField()
  # Add notes about the stay or special requests by the guest
  Notes = models.CharField(max_length=500)
  ArInvoice = models.ForeignKey(AArInvoice, related_name="PhBooking_ArInvoice", on_delete=models.CASCADE)


class PhRoomBooking(models.Model):
  """
  Links room allocations and a booking
  """

  # details of the booking
  Booking = models.ForeignKey(PhBooking, null=False, blank=False, related_name="PhRoomBooking_Booking", on_delete=models.CASCADE)
  # which room/beds are booked
  RoomAlloc = models.ForeignKey(PcRoomAlloc, null=False, blank=False, related_name="PhRoomBooking_RoomAlloc", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='ph_room_booking_pk', fields=['Booking', 'RoomAlloc']),
    ]

class PTax(models.Model):
  """
  Tax reference numbers
  """

  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PTax_Partner", on_delete=models.CASCADE)
  # Tax or VAT
  TaxType = models.CharField(max_length=8, null=False, blank=False)
  # Tax Reference
  TaxRef = models.CharField(max_length=50, null=False, blank=False)
  ValidFrom = models.DateTimeField()
  ValidUntil = models.DateTimeField()
  Comment = models.CharField(max_length=256)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_tax_pk', fields=['Partner', 'TaxType', 'TaxRef']),
    ]

class PPartnerInterest(models.Model):
  """
  Partner Area of Interest
  """

  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PPartnerInterest_Partner", on_delete=models.CASCADE)
  # Sequence number per Partner (required to make PK)
  InterestNumber = models.IntegerField(null=False, blank=False)
  # The Field the Partner is interested in
  Field = models.ForeignKey(PUnit, related_name="PPartnerInterest_Field", on_delete=models.CASCADE)
  # The Country the Partner is interested in
  Country = models.ForeignKey(PCountry, related_name="PPartnerInterest_Country", on_delete=models.CASCADE)
  # The Interest the Partner is interested in
  Interest = models.ForeignKey(PInterest, related_name="PPartnerInterest_Interest", on_delete=models.CASCADE)
  # The level of interest
  Level = models.IntegerField()
  Comment = models.CharField(max_length=256)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_partner_interest_pk', fields=['Partner', 'InterestNumber']),
    ]

class PPartnerMerge(models.Model):
  """
  Partner merge history
  """

  # The partner that was merged.
  MergeFrom = models.ForeignKey(PPartner, null=False, blank=False, related_name="PPartnerMerge_MergeFrom", on_delete=models.CASCADE)
  # The partner they were merged into.
  MergeTo = models.ForeignKey(PPartner, related_name="PPartnerMerge_MergeTo", on_delete=models.CASCADE)
  # The user who did the merge.
  MergedBy = models.ForeignKey(SUser, related_name="PPartnerMerge_MergedBy", on_delete=models.CASCADE)
  # Date of merge.
  MergeDate = models.DateTimeField()


class PPartnerReminder(models.Model):
  """
  A reminder that can be linked to a Partner or Partner contact
  """

  # Primary Key of this reminder
  PartnerReminderId = models.IntegerField(null=False, blank=False, unique=True)
  # Partner key of Partner to which the reminder is related
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PPartnerReminder_Partner", on_delete=models.CASCADE)
  # ID of Contact to which reminder relates. Null means that reminder relates just to a Partner
  Contact = models.ForeignKey(PContactLog, related_name="PPartnerReminder_Contact", on_delete=models.CASCADE)
  # ID of this reminder (only unique per Partner/Contact)
  ReminderId = models.IntegerField(default=0, null=False, blank=False)
  # The user that requires this reminder
  User = models.ForeignKey(SUser, related_name="PPartnerReminder_User", on_delete=models.CASCADE)
  # This is a category, by which reminders can be grouped.
  Category = models.ForeignKey(PReminderCategory, related_name="PPartnerReminder_Category", on_delete=models.CASCADE)
  # Type of action to take on getting the reminder (eg. Email etc)
  ActionType = models.CharField(max_length=8)
  # Reason for the reminder (eg. birthday, etc.)
  ReminderReason = models.CharField(max_length=300)
  # Additional Comments
  Comment = models.CharField(max_length=2500)
  # Date of event that reminder is about (if the reminder relates to a specific event like a birthday).
  EventDate = models.DateTimeField(null=False, blank=False)
  # Date on which to send/display first reminder.
  FirstReminderDate = models.DateTimeField()
  # Frequency (in days) with which re-reminders should be sent.
  ReminderFrequency = models.IntegerField(default=0)
  # Date on which the last reminder was sent
  LastReminderSent = models.DateTimeField()
  # Date on which the next reminder will be sent
  NextReminderDate = models.DateTimeField()
  # Is this reminder still active?
  ReminderActive = models.BooleanField(default=True, null=False, blank=False)
  # Email address to which reminder should be sent
  EmailAddress = models.CharField(max_length=500)
  # Indicates whether or not the contact has restricted access. If it does then the access will be controlled by s_group_partner_reminder
  Restricted = models.BooleanField(default=False)
  # Identifies a module. A module is any part of aprogram which is related to each menu entry or to the sub-system. Eg, partner administration, AP, AR etc.
  Module = models.ForeignKey(SModule, related_name="PPartnerReminder_Module", on_delete=models.CASCADE)
  # If set, this contact is restricted to one user.
  UserRestriction = models.ForeignKey(SUser, related_name="PPartnerReminder_UserRestriction", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_partner_reminder_uk', fields=['Partner', 'Contact', 'ReminderId']),
    ]

class PPartnerGiftDestination(models.Model):
  """
  Tracks the current gift destination for the Partner and maintains a history
  """

  # Surrogate Primary Key
  Key = models.IntegerField(null=False, blank=False, unique=True)
  # Partner key of Partner to which the field is assigned
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PPartnerGiftDestination_Partner", on_delete=models.CASCADE)
  # Field to which Partner is assigned
  Field = models.ForeignKey(PUnit, null=False, blank=False, related_name="PPartnerGiftDestination_Field", on_delete=models.CASCADE)
  # Date from which field assignment is valid
  DateEffective = models.DateTimeField(null=False, blank=False)
  # Date on which field assignment expires
  DateExpires = models.DateTimeField()
  # Is the field assignment currently valid
  Active = models.BooleanField()
  # Is this field the default gift destination?
  DefaultGiftDestination = models.BooleanField()
  # Is this the field for a person or a family?
  PartnerClass = models.ForeignKey(PPartnerClasses, related_name="PPartnerGiftDestination_PartnerClass", on_delete=models.CASCADE)
  # Any comments relating to this field assignment
  Comment = models.CharField(max_length=200)
  StaffData = models.ForeignKey(PmStaffData, related_name="PPartnerGiftDestination_StaffData", on_delete=models.CASCADE)


class PPartnerShortCode(models.Model):
  """
  Stores one or more short codes for a Partner (eg. a donor or recipient code for online giving system)
  """

  # Partner key of Partner to which short code applies
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PPartnerShortCode_Partner", on_delete=models.CASCADE)
  # The short code which applies to the Partner
  C = models.CharField(max_length=15, null=False, blank=False)
  # Field to which Partner is assigned
  FieldKey = models.IntegerField(null=False, blank=False)
  # Is this a short code to identify a recipient?
  Recipient = models.BooleanField()
  # Is this a short code to identify a donor?
  Donor = models.BooleanField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_partner_short_code_pk', fields=['Partner', 'C']),
    ]

class PPartnerState(models.Model):
  """
  A particular state in which the Partner is or has been. The Partner may be in more than one state at one time if there are two different processes relating to them.
  """

  # Partner key of Partner to which state applies
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PPartnerState_Partner", on_delete=models.CASCADE)
  # Unique identifier of this state for this partner
  StateIndex = models.IntegerField(null=False, blank=False)
  # State of the Partner (freetext)
  StateFreeform = models.CharField(max_length=200)
  # When did the Partner enter this state?
  StateStartDate = models.DateTimeField()
  # When will/did the Partner exit this state?
  StateEndDate = models.DateTimeField()
  # Has the Partner left this state?
  StateComplete = models.BooleanField()
  State = models.ForeignKey(PState, related_name="PPartnerState_State", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_partner_state_pk', fields=['Partner', 'StateIndex']),
    ]

class PPartnerAction(models.Model):
  """
  A particular action which has been or needs to be applied to a Partner
  """

  # Partner key of Partner to which action applies
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PPartnerAction_Partner", on_delete=models.CASCADE)
  # Sequential identifier for this action for this partner
  ActionNumber = models.IntegerField(null=False, blank=False)
  # Action to be applied to Partner (freetext)
  ActionFreeform = models.CharField(max_length=200)
  # Date by which action should be performed. Reminders could be set up based on this
  PerformByDate = models.DateTimeField()
  # Has the action already been completed?
  ActionComplete = models.BooleanField()
  # When was the action completed?
  ActionCompleteDate = models.DateTimeField()
  # Who should perform this action?
  UserToPerformAction = models.ForeignKey(SUser, related_name="PPartnerAction_UserToPerformAction", on_delete=models.CASCADE)
  # Who actually performed this action?
  UserThatPerformedAction = models.ForeignKey(SUser, related_name="PPartnerAction_UserThatPerformedAction", on_delete=models.CASCADE)
  Action = models.ForeignKey(PAction, related_name="PPartnerAction_Action", on_delete=models.CASCADE)
  Group = models.ForeignKey(SGroup, related_name="PPartnerAction_Group", on_delete=models.CASCADE)
  PartnerReminder = models.ForeignKey(PPartnerReminder, null=False, blank=False, related_name="PPartnerAction_PartnerReminder", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_partner_action_pk', fields=['ActionNumber']),
    ]

class SFunction(models.Model):
  """
  Contains all Petra functions to which access can be granted or denied
  """

  # Identifier for the particular function
  FunctionId = models.CharField(max_length=15, null=False, blank=False, unique=True)
  # Petra Module which contains the function
  ModuleName = models.CharField(max_length=100, null=False, blank=False)
  # Petra Sub-Module which contains the function
  SubModuleName = models.CharField(max_length=100)
  # Function name
  Name = models.CharField(max_length=100, null=False, blank=False)
  # Filename associated with the function
  Filename = models.CharField(max_length=100)


class SGroupFunction(models.Model):
  """
  Gives the group access to a particular function
  """

  Group = models.ForeignKey(SGroup, null=False, blank=False, related_name="SGroupFunction_Group", on_delete=models.CASCADE)
  # Identifier for the particular function
  Function = models.ForeignKey(SFunction, null=False, blank=False, related_name="SGroupFunction_Function", on_delete=models.CASCADE)
  # Does the group have access to this function?
  CanAccess = models.BooleanField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_group_function_pk', fields=['Group', 'Function']),
    ]

class SJobGroup(models.Model):
  """
  Associates groups with roles
  """

  # Name of the position.
  PositionName = models.CharField(max_length=30, null=False, blank=False)
  # Scope of the position.
  PositionScope = models.CharField(max_length=12, null=False, blank=False)
  # Position record identifier
  JobKey = models.IntegerField(null=False, blank=False)
  Group = models.ForeignKey(SGroup, null=False, blank=False, related_name="SJobGroup_Group", on_delete=models.CASCADE)
  Job = models.ForeignKey(UmJob, null=False, blank=False, related_name="SJobGroup_Job", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_job_group_pk', fields=['Group']),
    ]

class PPartnerSet(models.Model):
  """
  Defines a Partner set
  """

  # Identifier for the Partner Set
  PartnerSetId = models.CharField(max_length=20, null=False, blank=False)
  # Field that the Partner Set relates to
  Unit = models.ForeignKey(PUnit, null=False, blank=False, related_name="PPartnerSet_Unit", on_delete=models.CASCADE)
  # Name of the Partner set
  Name = models.CharField(max_length=100)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_partner_set_pk', fields=['PartnerSetId', 'Unit']),
    ]

class SGroupPartnerSet(models.Model):
  """
  Associates a Group with a Partner Set. This may be an inclusive or exclusive association and may be read, write, delete
  """

  Group = models.ForeignKey(SGroup, null=False, blank=False, related_name="SGroupPartnerSet_Group", on_delete=models.CASCADE)
  PartnerSet = models.ForeignKey(PPartnerSet, null=False, blank=False, related_name="SGroupPartnerSet_PartnerSet", on_delete=models.CASCADE)
  # Is the association between the Group and Partner Set inclusive or exclusive
  InclusiveOrExclusive = models.BooleanField(null=False, blank=False)
  # If the association is inclusive this will grant read access to the Partners, otherwise it will deny read access to the Partners
  ReadAccess = models.BooleanField()
  # If the association is inclusive this will grant write access to the Partners, otherwise it will deny write access to the Partners
  WriteAccess = models.BooleanField()
  # If the association is inclusive this will grant delete access to the Partners, otherwise it will deny delete access to the Partners
  DeleteAccess = models.BooleanField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_group_partner_set_pk', fields=['Group', 'PartnerSet']),
    ]

class PPartnerSetPartner(models.Model):
  """
  Places Partners in a Partner set
  """

  PartnerSet = models.ForeignKey(PPartnerSet, null=False, blank=False, related_name="PPartnerSetPartner_PartnerSet", on_delete=models.CASCADE)
  # Partner Key
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PPartnerSetPartner_Partner", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_partner_set_partner_pk', fields=['PartnerSet', 'Partner']),
    ]

class SGroupGift(models.Model):
  """
  Controls the access that a group has to a specific gift, if the gift is restricted
  """

  Group = models.ForeignKey(SGroup, null=False, blank=False, related_name="SGroupGift_Group", on_delete=models.CASCADE)
  Gift = models.ForeignKey(AGift, null=False, blank=False, related_name="SGroupGift_Gift", on_delete=models.CASCADE)
  # Control read access to the gift
  ReadAccess = models.BooleanField()
  # Control write access to the gift
  WriteAccess = models.BooleanField()
  # Control delete access to the gift
  DeleteAccess = models.BooleanField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_group_gift_pk', fields=['Group', 'Gift']),
    ]

class SGroupMotivation(models.Model):
  """
  Controls the access that a group has to gifts with a specific motivation
  """

  Group = models.ForeignKey(SGroup, null=False, blank=False, related_name="SGroupMotivation_Group", on_delete=models.CASCADE)
  MotivationDetail = models.ForeignKey(AMotivationDetail, null=False, blank=False, related_name="SGroupMotivation_MotivationDetail", on_delete=models.CASCADE)
  # Control read access to gifts with this motivation
  ReadAccess = models.BooleanField()
  # Control write access to gifts with this motivation
  WriteAccess = models.BooleanField()
  # Control delete access to gifts with this motivation
  DeleteAccess = models.BooleanField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_group_motivation_pk', fields=['Group', 'MotivationDetail']),
    ]

class SGroupPartnerContact(models.Model):
  """
  Controls the access that a group has to a specific Partner contact, if the contact is restricted
  """

  Group = models.ForeignKey(SGroup, null=False, blank=False, related_name="SGroupPartnerContact_Group", on_delete=models.CASCADE)
  # identifying key for p_contact_log
  Contact = models.ForeignKey(PContactLog, null=False, blank=False, related_name="SGroupPartnerContact_Contact", on_delete=models.CASCADE)
  # Control read access to the contact
  ReadAccess = models.BooleanField()
  # Control write access to the contact
  WriteAccess = models.BooleanField()
  # Control delete access to the contact
  DeleteAccess = models.BooleanField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_group_partner_contact_pk', fields=['Group', 'Contact']),
    ]

class SGroupPartnerReminder(models.Model):
  """
  Controls the access that a group has to a specific Partner reminder, if the reminder is restricted
  """

  Group = models.ForeignKey(SGroup, null=False, blank=False, related_name="SGroupPartnerReminder_Group", on_delete=models.CASCADE)
  # Primary Key of this reminder
  PartnerReminder = models.ForeignKey(PPartnerReminder, null=False, blank=False, related_name="SGroupPartnerReminder_PartnerReminder", on_delete=models.CASCADE)
  # Control read access to the reminder
  ReadAccess = models.BooleanField()
  # Control write access to the reminder
  WriteAccess = models.BooleanField()
  # Control delete access to the reminder
  DeleteAccess = models.BooleanField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_group_partner_reminder_pk', fields=['Group', 'PartnerReminder']),
    ]

class SGroupLocation(models.Model):
  """
  Controls the access that a group has to a specific location, if the Location is restricted
  """

  Group = models.ForeignKey(SGroup, null=False, blank=False, related_name="SGroupLocation_Group", on_delete=models.CASCADE)
  Location = models.ForeignKey(PLocation, null=False, blank=False, related_name="SGroupLocation_Location", on_delete=models.CASCADE)
  # Control read access to the location
  ReadAccess = models.BooleanField()
  # Control write access to the location
  WriteAccess = models.BooleanField()
  # Control delete access to the location
  DeleteAccess = models.BooleanField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_group_location_pk', fields=['Group', 'Location']),
    ]

class SGroupPartnerLocation(models.Model):
  """
  Controls the access that a group has to a specific partner location, if the Partner Location is restricted
  """

  Group = models.ForeignKey(SGroup, null=False, blank=False, related_name="SGroupPartnerLocation_Group", on_delete=models.CASCADE)
  PartnerLocation = models.ForeignKey(PPartnerLocation, null=False, blank=False, related_name="SGroupPartnerLocation_PartnerLocation", on_delete=models.CASCADE)
  # Control read access to the partner location
  ReadAccess = models.BooleanField()
  # Control write access to the partner location
  WriteAccess = models.BooleanField()
  # Control delete access to the partner location
  DeleteAccess = models.BooleanField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_group_partner_location_pk', fields=['Group', 'PartnerLocation']),
    ]

class SGroupDataLabel(models.Model):
  """
  Controls the access that a group has to a specific Data Label, if the Data Label is restricted
  """

  Group = models.ForeignKey(SGroup, null=False, blank=False, related_name="SGroupDataLabel_Group", on_delete=models.CASCADE)
  # Identifying key for p_data_label
  DataLabel = models.ForeignKey(PDataLabel, null=False, blank=False, related_name="SGroupDataLabel_DataLabel", on_delete=models.CASCADE)
  # Control read access to the data label
  ReadAccess = models.BooleanField()
  # Control write access to the data label
  WriteAccess = models.BooleanField()
  # Control delete access to the data label
  DeleteAccess = models.BooleanField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_group_data_label_pk', fields=['Group', 'DataLabel']),
    ]

class SGroupLedger(models.Model):
  """
  Gives a group access to a specific ledger
  """

  Group = models.ForeignKey(SGroup, null=False, blank=False, related_name="SGroupLedger_Group", on_delete=models.CASCADE)
  # Ledger Number
  Ledger = models.ForeignKey(ALedger, null=False, blank=False, related_name="SGroupLedger_Ledger", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_group_ledger_pk', fields=['Group', 'Ledger']),
    ]

class SGroupCostCentre(models.Model):
  """
  Gives a group access to a specific cost centre (so that people without other finance access can access data on their own department)
  """

  Group = models.ForeignKey(SGroup, null=False, blank=False, related_name="SGroupCostCentre_Group", on_delete=models.CASCADE)
  CostCentre = models.ForeignKey(ACostCentre, null=False, blank=False, related_name="SGroupCostCentre_CostCentre", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_group_cost_centre_pk', fields=['Group', 'CostCentre']),
    ]

class SGroupExtract(models.Model):
  """
  Gives a group access to a specific extract
  """

  Group = models.ForeignKey(SGroup, null=False, blank=False, related_name="SGroupExtract_Group", on_delete=models.CASCADE)
  # Identifier for the extract
  Extract = models.ForeignKey(MExtractMaster, null=False, blank=False, related_name="SGroupExtract_Extract", on_delete=models.CASCADE)
  # Control read access to the extract
  ReadAccess = models.BooleanField()
  # Control write access to the extract
  WriteAccess = models.BooleanField()
  # Control delete access to the extract
  DeleteAccess = models.BooleanField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_group_extract_pk', fields=['Group', 'Extract']),
    ]

class SChangeEvent(models.Model):
  """
  Records all database events (ie. insert, update, delete). Gets purged after each export
  """

  # Name of the database table where the event occurred
  TableName = models.CharField(max_length=32, null=False, blank=False)
  # Rowid of the record that the event applied to
  Rowid = models.CharField(max_length=20, null=False, blank=False)
  # Type of event (I, U or D - Insert, Update, Delete)
  ChangeType = models.CharField(max_length=1, null=False, blank=False)
  # Concatenation of the natural key values for the affected record (the primary key is not enough where a surrogate key is used as this is not meaningful across sites)
  NaturalKey = models.CharField(max_length=1000, null=False, blank=False)
  # Date on which the event took place
  Date = models.DateTimeField(null=False, blank=False)
  # Time at which event took place
  Time = models.IntegerField(null=False, blank=False)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_change_event_pk', fields=['TableName', 'Rowid']),
    ]

class SLabel(models.Model):
  """
  Attributes for label paper
  """

  LabelName = models.CharField(max_length=10, null=False, blank=False, unique=True)
  LabelDescription = models.CharField(max_length=40)
  # The form the label is designed for
  Form = models.ForeignKey(SForm, null=False, blank=False, related_name="SLabel_Form", on_delete=models.CASCADE)
  # The disance from the top of the page to the top of the first label.
  TopMargin = models.DecimalField(max_digits=6, decimal_places=2, default=0, null=False, blank=False)
  # The distance from the left edge of the page to the left edge of the first label.
  SideMargin = models.DecimalField(max_digits=6, decimal_places=2, default=0, null=False, blank=False)
  # The distance from the top of the first label to the top of the next label.
  VerticalPitch = models.DecimalField(max_digits=6, decimal_places=2, default=0, null=False, blank=False)
  # The distance from the left edge of the first label to the left edge of the next label.
  HorizontalPitch = models.DecimalField(max_digits=6, decimal_places=2, default=0, null=False, blank=False)
  # The height of each label.
  LabelHeight = models.DecimalField(max_digits=6, decimal_places=2, default=0, null=False, blank=False)
  # The width of each label.
  LabelWidth = models.DecimalField(max_digits=6, decimal_places=2, default=0, null=False, blank=False)
  # The number of labels across a page.
  LabelsAcross = models.IntegerField(default=0, null=False, blank=False)
  # The number of labels down a page.
  LabelsDown = models.IntegerField(default=0, null=False, blank=False)


class PPartnerComment(models.Model):
  """
  Allows multiple as well as arbitrary-length partner comments.
  """

  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PPartnerComment_Partner", on_delete=models.CASCADE)
  # Record Index that enables multiple comments per Partner
  Index = models.IntegerField(null=False, blank=False)
  # Sequence number (is necessary to concatenate records to one comment)
  Sequence = models.IntegerField(null=False, blank=False)
  # Comment
  Comment = models.CharField(max_length=5000)
  # Comment Type
  CommentType = models.CharField(max_length=20)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_partner_comment_pk', fields=['Partner', 'Index', 'Sequence']),
    ]

class PProposalSubmissionType(models.Model):
  """
  Submission type for foundation proposals e.g. EMAIL, LETTER.
  """

  SubmissionTypeCode = models.CharField(max_length=15, null=False, blank=False, unique=True)
  SubmissionTypeDescription = models.CharField(max_length=40)


class PFoundation(models.Model):
  """
  Foundations - a type of ORGANISATION for fundraising proposals.
  """

  # ORGANISATION key of the foundation.
  Partner = models.ForeignKey(POrganisation, null=False, blank=False, related_name="PFoundation_Partner", on_delete=models.CASCADE)
  # The Financial Development person who handles appeals to this foundation. Anyone else must get permission from the owner to contact the foundation.
  Owner1 = models.ForeignKey(PPartner, related_name="PFoundation_Owner1", on_delete=models.CASCADE)
  # A second F.D. person who may do business with the foundation.
  Owner2 = models.ForeignKey(PPartner, related_name="PFoundation_Owner2", on_delete=models.CASCADE)
  # Name of the contact for this Foundation
  KeyContactName = models.CharField(max_length=35)
  # The contact person's title.
  KeyContactTitle = models.CharField(max_length=35)
  # Contact email address
  KeyContactEmail = models.CharField(max_length=60)
  # Contact's phone number
  KeyContactPhone = models.CharField(max_length=20)
  # Not part of original specification - provided in case contact does ever need to be a full Partner.
  ContactPartner = models.ForeignKey(PPartner, related_name="PFoundation_ContactPartner", on_delete=models.CASCADE)
  SpecialRequirements = models.CharField(max_length=350)
  ProposalFormatting = models.CharField(max_length=350)
  # A lookup table would go with this. e.g. EMAIL, LETTER.
  ProposalSubmissionType = models.ForeignKey(PProposalSubmissionType, related_name="PFoundation_ProposalSubmissionType", on_delete=models.CASCADE)
  SpecialInstructions = models.CharField(max_length=350)
  # (Monthly | Quarterly | Annually)  These are the only ones we use now.
  ReviewFrequency = models.CharField(max_length=10)
  # (Annually | Bi-Annually | No Restrictions)  This is a static list.
  SubmitFrequency = models.CharField(max_length=15)


class PFoundationProposalStatus(models.Model):
  """
  Foundation proposal status codes and descriptions
  """

  StatusCode = models.CharField(max_length=15, null=False, blank=False, unique=True)
  StatusDescription = models.CharField(max_length=40)


class PFoundationProposal(models.Model):
  """
  Proposals submitted to a Foundation
  """

  FoundationPartner = models.ForeignKey(PFoundation, null=False, blank=False, related_name="PFoundationProposal_FoundationPartner", on_delete=models.CASCADE)
  FoundationProposalKey = models.IntegerField(null=False, blank=False)
  ProposalStatus = models.ForeignKey(PFoundationProposalStatus, related_name="PFoundationProposal_ProposalStatus", on_delete=models.CASCADE)
  ProposalNotes = models.CharField(max_length=350)
  SubmittedDate = models.DateTimeField()
  AmountRequested = models.DecimalField(max_digits=19, decimal_places=2)
  AmountApproved = models.DecimalField(max_digits=19, decimal_places=2)
  AmountGranted = models.DecimalField(max_digits=19, decimal_places=2)
  DateGranted = models.DateTimeField()
  # The F.D. person who sent the proposal
  PartnerSubmittedBy = models.ForeignKey(PPartner, related_name="PFoundationProposal_PartnerSubmittedBy", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_proposal_pk', fields=['FoundationPartner', 'FoundationProposalKey']),
    ]

class PFoundationProposalDetail(models.Model):
  """
  A proposal may be for more than one project or key ministry.
  """

  FoundationProposal = models.ForeignKey(PFoundationProposal, null=False, blank=False, related_name="PFoundationProposalDetail_FoundationProposal", on_delete=models.CASCADE)
  ProposalDetailId = models.IntegerField(null=False, blank=False)
  # Used when the proposal is for a key ministry
  KeyMinistry = models.ForeignKey(PUnit, related_name="PFoundationProposalDetail_KeyMinistry", on_delete=models.CASCADE)
  # The area that the project or key ministry is for
  AreaPartner = models.ForeignKey(PUnit, related_name="PFoundationProposalDetail_AreaPartner", on_delete=models.CASCADE)
  # The field that the project or key ministry is for if it applies
  FieldPartner = models.ForeignKey(PUnit, related_name="PFoundationProposalDetail_FieldPartner", on_delete=models.CASCADE)
  MotivationDetail = models.ForeignKey(AMotivationDetail, related_name="PFoundationProposalDetail_MotivationDetail", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_proposal_detail_pk', fields=['FoundationProposal', 'ProposalDetailId']),
    ]

class PFoundationDeadline(models.Model):
  """
  The month and day of reviews so that proposals can be sent in time
  """

  FoundationPartner = models.ForeignKey(PFoundation, null=False, blank=False, related_name="PFoundationDeadline_FoundationPartner", on_delete=models.CASCADE)
  FoundationDeadlineKey = models.IntegerField(null=False, blank=False)
  # The month number
  DeadlineMonth = models.IntegerField()
  # The day number
  DeadlineDay = models.IntegerField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_deadline_pk', fields=['FoundationPartner', 'FoundationDeadlineKey']),
    ]

class SWorkflowDefinition(models.Model):
  """
  Stores the definition of each workflow. These may be pre-created, or created by the user.
  """

  # Workflow ID
  WorkflowId = models.IntegerField(null=False, blank=False, unique=True)
  Name = models.CharField(max_length=30, null=False, blank=False)
  Description = models.CharField(max_length=300)
  # List of all modules within which workflow should be available
  ModuleList = models.CharField(max_length=100)
  # If workflow is dependent on a particular data item what sort of data item is it (eg. partner key, application, extract).
  TypeOfSharedData = models.CharField(max_length=100)


class SWorkflowUser(models.Model):
  """
  Which users have access to this workflow
  """

  # Workflow ID
  Workflow = models.ForeignKey(SWorkflowDefinition, null=False, blank=False, related_name="SWorkflowUser_Workflow", on_delete=models.CASCADE)
  # The user that has access to the workflow
  User = models.ForeignKey(SUser, null=False, blank=False, related_name="SWorkflowUser_User", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_workflow_user_pk', fields=['Workflow', 'User']),
    ]

class SWorkflowGroup(models.Model):
  """
  Which groups have access to this workflow
  """

  # Workflow ID
  Workflow = models.ForeignKey(SWorkflowDefinition, null=False, blank=False, related_name="SWorkflowGroup_Workflow", on_delete=models.CASCADE)
  Group = models.ForeignKey(SGroup, null=False, blank=False, related_name="SWorkflowGroup_Group", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_workflow_group_pk', fields=['Workflow', 'Group']),
    ]

class SWorkflowStep(models.Model):
  """
  Stores each step of the workflow
  """

  # Workflow ID
  Workflow = models.ForeignKey(SWorkflowDefinition, null=False, blank=False, related_name="SWorkflowStep_Workflow", on_delete=models.CASCADE)
  # Indicates position within workflow (ie. 1 means first step, etc)
  StepNumber = models.IntegerField(null=False, blank=False)
  # Identifier for the particular function
  Function = models.ForeignKey(SFunction, null=False, blank=False, related_name="SWorkflowStep_Function", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_workflow_step_pk', fields=['Workflow', 'StepNumber']),
    ]

class SFunctionRelationship(models.Model):
  """
  Represents a relationship between two particular functions. Eg. Partner Find and Partner Edit
  """

  # Identifier for one particular function
  Function1 = models.ForeignKey(SFunction, null=False, blank=False, related_name="SFunctionRelationship_Function1", on_delete=models.CASCADE)
  # Identifier for related function
  Function2 = models.ForeignKey(SFunction, null=False, blank=False, related_name="SFunctionRelationship_Function2", on_delete=models.CASCADE)
  # Code to run if a workflow contains function_1 and function_2 as adjacent steps. This code will provide the glue to connect the two steps.
  CodeToRun = models.CharField(max_length=200)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_function_relationship_pk', fields=['Function1', 'Function2']),
    ]

class SWorkflowInstance(models.Model):
  """
  A running instance of a defined workflow
  """

  # Workflow Instance ID
  WorkflowInstanceId = models.IntegerField(null=False, blank=False, unique=True)
  # Workflow ID
  Workflow = models.ForeignKey(SWorkflowDefinition, null=False, blank=False, related_name="SWorkflowInstance_Workflow", on_delete=models.CASCADE)
  # If there is a particular data item required through the workflow what is it. Eg. if a Partner Key is required what is that Partner Key
  KeyDataItem = models.CharField(max_length=100)
  # The type of the shared data item (eg. Partner Key)
  KeyDataItemType = models.CharField(max_length=100)
  # Was this instance generated by the System rather than the user
  SystemGenerated = models.BooleanField()
  # Has the workflow been completed
  Complete = models.BooleanField()
  # User entered comment or note attached to the workflow
  Note = models.CharField(max_length=300)


class SWorkflowInstanceStep(models.Model):
  """
  Each step of the running workflow, including the status of that step
  """

  # Workflow Instance ID
  WorkflowInstance = models.ForeignKey(SWorkflowInstance, null=False, blank=False, related_name="SWorkflowInstanceStep_WorkflowInstance", on_delete=models.CASCADE)
  # Indicates current position within workflow instance
  StepNumber = models.IntegerField(null=False, blank=False)
  # Has this step been completed
  Complete = models.BooleanField()
  # User who ran or is running this step
  User = models.ForeignKey(SUser, null=False, blank=False, related_name="SWorkflowInstanceStep_User", on_delete=models.CASCADE)
  # Any output parameters from this step
  OutputParameters = models.CharField(max_length=100)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_workflow_instance_step_pk', fields=['WorkflowInstance', 'StepNumber']),
    ]

class SVolume(models.Model):
  """
  Volume to either represent a file directory or a volume relative to a parent volume
  """

  # Name (Identifier) for the volume
  Name = models.CharField(max_length=80, null=False, blank=False, unique=True)
  # Name of the parent volume (use either Path or Parent Volume)
  ParentVolume = models.ForeignKey('self', related_name="SVolume_ParentVolume", on_delete=models.CASCADE)
  # Path information (use either Path or Parent Volume)
  Path = models.CharField(max_length=2048)
  # Comment for the user
  Comment = models.CharField(max_length=500)


class PFileInfo(models.Model):
  """
  Store information about the physical location of a file linked into Petra
  """

  Key = models.IntegerField(null=False, blank=False, unique=True)
  # Partner key that the file is linked with (needed for performance reasons)
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PFileInfo_Partner", on_delete=models.CASCADE)
  # Volume this file can be found in (use either volume or path)
  Volume = models.ForeignKey(SVolume, related_name="PFileInfo_Volume", on_delete=models.CASCADE)
  # Path this file can be found in (use either volume or path)
  Path = models.CharField(max_length=2048)
  # File name this file can be found under in given volume or path
  FileName = models.CharField(max_length=512)
  # Internal name of the file, different from actual file name
  Name = models.CharField(max_length=80)
  # Information about the file type
  FileType = models.CharField(max_length=50)
  # Comment for the user
  Comment = models.CharField(max_length=500)
  # Indicates whether or not the file info has restricted access. If it does then the access will be controlled by s_group_file_info.
  Restricted = models.BooleanField(default=False)


class PPartnerGraphic(models.Model):
  """
  Any graphic associated to a partner can be stored here.
  """

  FileInfo = models.ForeignKey(PFileInfo, null=False, blank=False, related_name="PPartnerGraphic_FileInfo", on_delete=models.CASCADE)
  # This is the partner key assigned to each partner. It consists of the fund id followed by a computer generated six digit number.
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PPartnerGraphic_Partner", on_delete=models.CASCADE)
  # The label for the graphic related to the partner.
  GraphicLabel = models.CharField(max_length=32)


class PPartnerFile(models.Model):
  """
  Link file with a partner
  """

  FileInfo = models.ForeignKey(PFileInfo, null=False, blank=False, related_name="PPartnerFile_FileInfo", on_delete=models.CASCADE)
  # Partner key that the file is linked with (needed for performance reasons)
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PPartnerFile_Partner", on_delete=models.CASCADE)


class PmPersonFile(models.Model):
  """
  Link file with a person
  """

  FileInfo = models.ForeignKey(PFileInfo, null=False, blank=False, related_name="PmPersonFile_FileInfo", on_delete=models.CASCADE)
  # Partner key that the file is linked with (needed for performance reasons)
  Partner = models.ForeignKey(PPerson, null=False, blank=False, related_name="PmPersonFile_Partner", on_delete=models.CASCADE)


class PPartnerContactFile(models.Model):
  """
  Link file with a partner contact
  """

  FileInfo = models.ForeignKey(PFileInfo, null=False, blank=False, related_name="PPartnerContactFile_FileInfo", on_delete=models.CASCADE)
  # Partner key that the file is linked with (needed for performance reasons)
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PPartnerContactFile_Partner", on_delete=models.CASCADE)
  # identifying key for Partner Contact
  Contact = models.ForeignKey(PContactLog, null=False, blank=False, related_name="PPartnerContactFile_Contact", on_delete=models.CASCADE)


class PmDocumentFile(models.Model):
  """
  Link file with a personal document
  """

  FileInfo = models.ForeignKey(PFileInfo, null=False, blank=False, related_name="PmDocumentFile_FileInfo", on_delete=models.CASCADE)
  # Partner key that the file is linked with (needed for performance reasons to find all records linked with a partner)
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PmDocumentFile_Partner", on_delete=models.CASCADE)
  Document = models.ForeignKey(PmDocument, null=False, blank=False, related_name="PmDocumentFile_Document", on_delete=models.CASCADE)


class PmApplicationFile(models.Model):
  """
  Link file with an application
  """

  FileInfo = models.ForeignKey(PFileInfo, null=False, blank=False, related_name="PmApplicationFile_FileInfo", on_delete=models.CASCADE)
  GeneralApplication = models.ForeignKey(PmGeneralApplication, null=False, blank=False, related_name="PmApplicationFile_GeneralApplication", on_delete=models.CASCADE)


class SVolumePartnerGroup(models.Model):
  """
  Set up a Group for use in Default Volumes
  """

  # Group Name this default volume applies to
  Name = models.CharField(max_length=30, null=False, blank=False, unique=True)
  # Description
  Description = models.CharField(max_length=80)
  # Comment field
  Comment = models.CharField(max_length=300)


class SDefaultFileVolume(models.Model):
  """
  Set Default Volume for a user group in a specific area
  """

  # Group Name this default volume applies to
  Group = models.ForeignKey(SVolumePartnerGroup, null=False, blank=False, related_name="SDefaultFileVolume_Group", on_delete=models.CASCADE)
  # Area this default volume applies to (e.g. Partner, Application, Contacts, ...)
  Area = models.CharField(max_length=30, null=False, blank=False)
  # Default Volume for combination of group and area
  Volume = models.ForeignKey(SVolume, related_name="SDefaultFileVolume_Volume", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_default_file_volume_pk', fields=['Group', 'Area']),
    ]

class SVolumePartnerGroupPartner(models.Model):
  """
  Assign Partners to a Group for use in Default Volumes
  """

  # Group Name this default volume applies to
  Group = models.ForeignKey(SVolumePartnerGroup, null=False, blank=False, related_name="SVolumePartnerGroupPartner_Group", on_delete=models.CASCADE)
  # Partner key (one partner can be in several groups)
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="SVolumePartnerGroupPartner_Partner", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_volume_partner_group_ptn_pk', fields=['Group', 'Partner']),
    ]

class SGroupFileInfo(models.Model):
  """
  Associates a Group with an external document (file info). This may be read, write, delete
  """

  Group = models.ForeignKey(SGroup, null=False, blank=False, related_name="SGroupFileInfo_Group", on_delete=models.CASCADE)
  FileInfo = models.ForeignKey(PFileInfo, null=False, blank=False, related_name="SGroupFileInfo_FileInfo", on_delete=models.CASCADE)
  # Control read access to the file information
  ReadAccess = models.BooleanField()
  # Control write access to the file information
  WriteAccess = models.BooleanField()
  # Control delete access to the file information
  DeleteAccess = models.BooleanField()

  class Meta:
    constraints = [
      models.UniqueConstraint(name='s_group_file_info_pk', fields=['Group', 'FileInfo']),
    ]

class PConsentChannel(models.Model):
  """
  All possible channels to get data changes and consent
  """

  # Unique key for channel
  ChannelCode = models.CharField(max_length=20, null=False, blank=False, unique=True)
  # international name for i18n translation
  Name = models.CharField(max_length=64, default='0', null=False, blank=False)
  # comment for a channel
  Comment = models.CharField(max_length=256)


class PConsentHistory(models.Model):
  """
  Keeps track of all data changes for GDPR
  """

  # Incremental key for entrys
  EntryId = models.IntegerField(default=0, null=False, blank=False, unique=True)
  # Key for partner
  Partner = models.ForeignKey(PPartner, null=False, blank=False, related_name="PConsentHistory_Partner", on_delete=models.CASCADE)
  # Type for Data saved
  Type = models.CharField(max_length=64, null=False, blank=False)
  # Value for type key
  Value = models.CharField(max_length=512)
  # Date the consent was given
  ConsentDate = models.DateTimeField(null=False, blank=False)
  # Code of channel
  Channel = models.ForeignKey(PConsentChannel, null=False, blank=False, related_name="PConsentHistory_Channel", on_delete=models.CASCADE)


class PConsentPurpose(models.Model):
  """
  Purposes for consent, for which the data may be used
  """

  # Unique key for purpose
  PurposeCode = models.CharField(max_length=20, null=False, blank=False, unique=True)
  # international name for i18n translation
  Name = models.CharField(max_length=64, default='0', null=False, blank=False)
  # comment for a purpose
  Comment = models.CharField(max_length=256)


class PConsentHistoryPermission(models.Model):
  """
  The history of consent for personal data
  """

  # ID for entrys
  ConsentHistoryEntry = models.ForeignKey(PConsentHistory, null=False, blank=False, related_name="PConsentHistoryPermission_ConsentHistoryEntry", on_delete=models.CASCADE)
  # Code for purpose
  Purpose = models.ForeignKey(PConsentPurpose, null=False, blank=False, related_name="PConsentHistoryPermission_Purpose", on_delete=models.CASCADE)

  class Meta:
    constraints = [
      models.UniqueConstraint(name='p_consent_history_permission_pk', fields=['ConsentHistoryEntry', 'Purpose']),
    ]