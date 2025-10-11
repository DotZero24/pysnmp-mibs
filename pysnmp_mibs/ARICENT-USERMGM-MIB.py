# SNMP MIB module (ARICENT-USERMGM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-USERMGM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:07 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsusrMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70)
)
if mibBuilder.loadTexts:
    fsusrMgmt.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsusrMgmtStats_ObjectIdentity = ObjectIdentity
fsusrMgmtStats = _FsusrMgmtStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70, 1)
)
_FsusrMgmtStatsNumOfUsers_Type = Unsigned32
_FsusrMgmtStatsNumOfUsers_Object = MibScalar
fsusrMgmtStatsNumOfUsers = _FsusrMgmtStatsNumOfUsers_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70, 1, 1),
    _FsusrMgmtStatsNumOfUsers_Type()
)
fsusrMgmtStatsNumOfUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsusrMgmtStatsNumOfUsers.setStatus("current")
_FsusrMgmtStatsActiveUsers_Type = Unsigned32
_FsusrMgmtStatsActiveUsers_Object = MibScalar
fsusrMgmtStatsActiveUsers = _FsusrMgmtStatsActiveUsers_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70, 1, 2),
    _FsusrMgmtStatsActiveUsers_Type()
)
fsusrMgmtStatsActiveUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsusrMgmtStatsActiveUsers.setStatus("current")


class _FsusrMgmtMinPasswordLen_Type(Unsigned32):
    """Custom type fsusrMgmtMinPasswordLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 20),
    )


_FsusrMgmtMinPasswordLen_Type.__name__ = "Unsigned32"
_FsusrMgmtMinPasswordLen_Object = MibScalar
fsusrMgmtMinPasswordLen = _FsusrMgmtMinPasswordLen_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70, 1, 3),
    _FsusrMgmtMinPasswordLen_Type()
)
fsusrMgmtMinPasswordLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsusrMgmtMinPasswordLen.setStatus("current")


class _FsusrMgmtPasswdValidationChars_Type(Unsigned32):
    """Custom type fsusrMgmtPasswdValidationChars based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FsusrMgmtPasswdValidationChars_Type.__name__ = "Unsigned32"
_FsusrMgmtPasswdValidationChars_Object = MibScalar
fsusrMgmtPasswdValidationChars = _FsusrMgmtPasswdValidationChars_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70, 1, 4),
    _FsusrMgmtPasswdValidationChars_Type()
)
fsusrMgmtPasswdValidationChars.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsusrMgmtPasswdValidationChars.setStatus("current")


class _FsusrMgmtPasswdValidateNoOfLowerCase_Type(Unsigned32):
    """Custom type fsusrMgmtPasswdValidateNoOfLowerCase based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_FsusrMgmtPasswdValidateNoOfLowerCase_Type.__name__ = "Unsigned32"
_FsusrMgmtPasswdValidateNoOfLowerCase_Object = MibScalar
fsusrMgmtPasswdValidateNoOfLowerCase = _FsusrMgmtPasswdValidateNoOfLowerCase_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70, 1, 5),
    _FsusrMgmtPasswdValidateNoOfLowerCase_Type()
)
fsusrMgmtPasswdValidateNoOfLowerCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsusrMgmtPasswdValidateNoOfLowerCase.setStatus("current")


class _FsusrMgmtPasswdValidateNoOfUpperCase_Type(Unsigned32):
    """Custom type fsusrMgmtPasswdValidateNoOfUpperCase based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_FsusrMgmtPasswdValidateNoOfUpperCase_Type.__name__ = "Unsigned32"
_FsusrMgmtPasswdValidateNoOfUpperCase_Object = MibScalar
fsusrMgmtPasswdValidateNoOfUpperCase = _FsusrMgmtPasswdValidateNoOfUpperCase_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70, 1, 6),
    _FsusrMgmtPasswdValidateNoOfUpperCase_Type()
)
fsusrMgmtPasswdValidateNoOfUpperCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsusrMgmtPasswdValidateNoOfUpperCase.setStatus("current")


class _FsusrMgmtPasswdValidateNoOfNumericals_Type(Unsigned32):
    """Custom type fsusrMgmtPasswdValidateNoOfNumericals based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_FsusrMgmtPasswdValidateNoOfNumericals_Type.__name__ = "Unsigned32"
_FsusrMgmtPasswdValidateNoOfNumericals_Object = MibScalar
fsusrMgmtPasswdValidateNoOfNumericals = _FsusrMgmtPasswdValidateNoOfNumericals_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70, 1, 7),
    _FsusrMgmtPasswdValidateNoOfNumericals_Type()
)
fsusrMgmtPasswdValidateNoOfNumericals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsusrMgmtPasswdValidateNoOfNumericals.setStatus("current")


class _FsusrMgmtPasswdValidateNoOfSplChars_Type(Unsigned32):
    """Custom type fsusrMgmtPasswdValidateNoOfSplChars based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_FsusrMgmtPasswdValidateNoOfSplChars_Type.__name__ = "Unsigned32"
_FsusrMgmtPasswdValidateNoOfSplChars_Object = MibScalar
fsusrMgmtPasswdValidateNoOfSplChars = _FsusrMgmtPasswdValidateNoOfSplChars_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70, 1, 8),
    _FsusrMgmtPasswdValidateNoOfSplChars_Type()
)
fsusrMgmtPasswdValidateNoOfSplChars.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsusrMgmtPasswdValidateNoOfSplChars.setStatus("current")


class _FsusrMgmtPasswdMaxLifeTime_Type(Unsigned32):
    """Custom type fsusrMgmtPasswdMaxLifeTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 366),
    )


_FsusrMgmtPasswdMaxLifeTime_Type.__name__ = "Unsigned32"
_FsusrMgmtPasswdMaxLifeTime_Object = MibScalar
fsusrMgmtPasswdMaxLifeTime = _FsusrMgmtPasswdMaxLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70, 1, 9),
    _FsusrMgmtPasswdMaxLifeTime_Type()
)
fsusrMgmtPasswdMaxLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsusrMgmtPasswdMaxLifeTime.setStatus("current")
_FsusrMgmtStatsEnableUsers_Type = Unsigned32
_FsusrMgmtStatsEnableUsers_Object = MibScalar
fsusrMgmtStatsEnableUsers = _FsusrMgmtStatsEnableUsers_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70, 1, 10),
    _FsusrMgmtStatsEnableUsers_Type()
)
fsusrMgmtStatsEnableUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsusrMgmtStatsEnableUsers.setStatus("current")
_FsusrMgmtStatsDisableUsers_Type = Unsigned32
_FsusrMgmtStatsDisableUsers_Object = MibScalar
fsusrMgmtStatsDisableUsers = _FsusrMgmtStatsDisableUsers_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70, 1, 11),
    _FsusrMgmtStatsDisableUsers_Type()
)
fsusrMgmtStatsDisableUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsusrMgmtStatsDisableUsers.setStatus("current")
_FsusrMgmtUserList_ObjectIdentity = ObjectIdentity
fsusrMgmtUserList = _FsusrMgmtUserList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70, 2)
)
_FsusrMgmtTable_Object = MibTable
fsusrMgmtTable = _FsusrMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70, 2, 1)
)
if mibBuilder.loadTexts:
    fsusrMgmtTable.setStatus("current")
_FsusrMgmtEntry_Object = MibTableRow
fsusrMgmtEntry = _FsusrMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70, 2, 1, 1)
)
fsusrMgmtEntry.setIndexNames(
    (0, "ARICENT-USERMGM-MIB", "fsusrMgmtUserName"),
    (0, "ARICENT-USERMGM-MIB", "fsusrMgmtAuthString"),
)
if mibBuilder.loadTexts:
    fsusrMgmtEntry.setStatus("current")


class _FsusrMgmtUserName_Type(DisplayString):
    """Custom type fsusrMgmtUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsusrMgmtUserName_Type.__name__ = "DisplayString"
_FsusrMgmtUserName_Object = MibTableColumn
fsusrMgmtUserName = _FsusrMgmtUserName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70, 2, 1, 1, 1),
    _FsusrMgmtUserName_Type()
)
fsusrMgmtUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsusrMgmtUserName.setStatus("current")


class _FsusrMgmtAuthString_Type(DisplayString):
    """Custom type fsusrMgmtAuthString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 42),
    )


_FsusrMgmtAuthString_Type.__name__ = "DisplayString"
_FsusrMgmtAuthString_Object = MibTableColumn
fsusrMgmtAuthString = _FsusrMgmtAuthString_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70, 2, 1, 1, 2),
    _FsusrMgmtAuthString_Type()
)
fsusrMgmtAuthString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsusrMgmtAuthString.setStatus("current")


class _FsusrMgmtUserPassword_Type(DisplayString):
    """Custom type fsusrMgmtUserPassword based on DisplayString"""
    defaultValue = OctetString("Password123#")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 32),
    )


_FsusrMgmtUserPassword_Type.__name__ = "DisplayString"
_FsusrMgmtUserPassword_Object = MibTableColumn
fsusrMgmtUserPassword = _FsusrMgmtUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70, 2, 1, 1, 3),
    _FsusrMgmtUserPassword_Type()
)
fsusrMgmtUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsusrMgmtUserPassword.setStatus("current")


class _FsusrMgmtUserPrivilege_Type(Unsigned32):
    """Custom type fsusrMgmtUserPrivilege based on Unsigned32"""
    defaultValue = 1


_FsusrMgmtUserPrivilege_Type.__name__ = "Unsigned32"
_FsusrMgmtUserPrivilege_Object = MibTableColumn
fsusrMgmtUserPrivilege = _FsusrMgmtUserPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70, 2, 1, 1, 4),
    _FsusrMgmtUserPrivilege_Type()
)
fsusrMgmtUserPrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsusrMgmtUserPrivilege.setStatus("current")
_FsusrMgmtUserLoginCount_Type = Integer32
_FsusrMgmtUserLoginCount_Object = MibTableColumn
fsusrMgmtUserLoginCount = _FsusrMgmtUserLoginCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70, 2, 1, 1, 5),
    _FsusrMgmtUserLoginCount_Type()
)
fsusrMgmtUserLoginCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsusrMgmtUserLoginCount.setStatus("current")


class _FsusrMgmtUserStatus_Type(Integer32):
    """Custom type fsusrMgmtUserStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FsusrMgmtUserStatus_Type.__name__ = "Integer32"
_FsusrMgmtUserStatus_Object = MibTableColumn
fsusrMgmtUserStatus = _FsusrMgmtUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70, 2, 1, 1, 6),
    _FsusrMgmtUserStatus_Type()
)
fsusrMgmtUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsusrMgmtUserStatus.setStatus("current")


class _FsusrMgmtUserLockRelTime_Type(Unsigned32):
    """Custom type fsusrMgmtUserLockRelTime based on Unsigned32"""
    defaultValue = 0


_FsusrMgmtUserLockRelTime_Type.__name__ = "Unsigned32"
_FsusrMgmtUserLockRelTime_Object = MibTableColumn
fsusrMgmtUserLockRelTime = _FsusrMgmtUserLockRelTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70, 2, 1, 1, 7),
    _FsusrMgmtUserLockRelTime_Type()
)
fsusrMgmtUserLockRelTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsusrMgmtUserLockRelTime.setStatus("current")
_FsusrMgmtUserRowStatus_Type = RowStatus
_FsusrMgmtUserRowStatus_Object = MibTableColumn
fsusrMgmtUserRowStatus = _FsusrMgmtUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70, 2, 1, 1, 8),
    _FsusrMgmtUserRowStatus_Type()
)
fsusrMgmtUserRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsusrMgmtUserRowStatus.setStatus("current")


class _FsusrMgmtUserConfirmPwd_Type(DisplayString):
    """Custom type fsusrMgmtUserConfirmPwd based on DisplayString"""
    defaultValue = OctetString("Password123#")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 32),
    )


_FsusrMgmtUserConfirmPwd_Type.__name__ = "DisplayString"
_FsusrMgmtUserConfirmPwd_Object = MibTableColumn
fsusrMgmtUserConfirmPwd = _FsusrMgmtUserConfirmPwd_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 70, 2, 1, 1, 9),
    _FsusrMgmtUserConfirmPwd_Type()
)
fsusrMgmtUserConfirmPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsusrMgmtUserConfirmPwd.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-USERMGM-MIB",
    **{"fsusrMgmt": fsusrMgmt,
       "fsusrMgmtStats": fsusrMgmtStats,
       "fsusrMgmtStatsNumOfUsers": fsusrMgmtStatsNumOfUsers,
       "fsusrMgmtStatsActiveUsers": fsusrMgmtStatsActiveUsers,
       "fsusrMgmtMinPasswordLen": fsusrMgmtMinPasswordLen,
       "fsusrMgmtPasswdValidationChars": fsusrMgmtPasswdValidationChars,
       "fsusrMgmtPasswdValidateNoOfLowerCase": fsusrMgmtPasswdValidateNoOfLowerCase,
       "fsusrMgmtPasswdValidateNoOfUpperCase": fsusrMgmtPasswdValidateNoOfUpperCase,
       "fsusrMgmtPasswdValidateNoOfNumericals": fsusrMgmtPasswdValidateNoOfNumericals,
       "fsusrMgmtPasswdValidateNoOfSplChars": fsusrMgmtPasswdValidateNoOfSplChars,
       "fsusrMgmtPasswdMaxLifeTime": fsusrMgmtPasswdMaxLifeTime,
       "fsusrMgmtStatsEnableUsers": fsusrMgmtStatsEnableUsers,
       "fsusrMgmtStatsDisableUsers": fsusrMgmtStatsDisableUsers,
       "fsusrMgmtUserList": fsusrMgmtUserList,
       "fsusrMgmtTable": fsusrMgmtTable,
       "fsusrMgmtEntry": fsusrMgmtEntry,
       "fsusrMgmtUserName": fsusrMgmtUserName,
       "fsusrMgmtAuthString": fsusrMgmtAuthString,
       "fsusrMgmtUserPassword": fsusrMgmtUserPassword,
       "fsusrMgmtUserPrivilege": fsusrMgmtUserPrivilege,
       "fsusrMgmtUserLoginCount": fsusrMgmtUserLoginCount,
       "fsusrMgmtUserStatus": fsusrMgmtUserStatus,
       "fsusrMgmtUserLockRelTime": fsusrMgmtUserLockRelTime,
       "fsusrMgmtUserRowStatus": fsusrMgmtUserRowStatus,
       "fsusrMgmtUserConfirmPwd": fsusrMgmtUserConfirmPwd}
)
