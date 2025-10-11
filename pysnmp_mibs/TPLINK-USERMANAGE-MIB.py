# SNMP MIB module (TPLINK-USERMANAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-USERMANAGE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:55:14 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkUserInfoMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 7)
)
if mibBuilder.loadTexts:
    tplinkUserInfoMIB.setRevisions(
        ("1920-09-07 09:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkUserManageMIBObjects_ObjectIdentity = ObjectIdentity
tplinkUserManageMIBObjects = _TplinkUserManageMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 7, 1)
)
_UserInfoUserTable_Object = MibTable
userInfoUserTable = _UserInfoUserTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 7, 1, 1)
)
if mibBuilder.loadTexts:
    userInfoUserTable.setStatus("current")
_UserInfoUserEntry_Object = MibTableRow
userInfoUserEntry = _UserInfoUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 7, 1, 1, 1)
)
userInfoUserEntry.setIndexNames(
    (0, "TPLINK-USERMANAGE-MIB", "userInfoUserName"),
)
if mibBuilder.loadTexts:
    userInfoUserEntry.setStatus("current")


class _UserInfoUserName_Type(OctetString):
    """Custom type userInfoUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_UserInfoUserName_Type.__name__ = "OctetString"
_UserInfoUserName_Object = MibTableColumn
userInfoUserName = _UserInfoUserName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 7, 1, 1, 1, 1),
    _UserInfoUserName_Type()
)
userInfoUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userInfoUserName.setStatus("current")


class _UserInfoUserType_Type(Integer32):
    """Custom type userInfoUserType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("user", 0),
          ("power-user", 1),
          ("operator", 2),
          ("admin", 3))
    )


_UserInfoUserType_Type.__name__ = "Integer32"
_UserInfoUserType_Object = MibTableColumn
userInfoUserType = _UserInfoUserType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 7, 1, 1, 1, 2),
    _UserInfoUserType_Type()
)
userInfoUserType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userInfoUserType.setStatus("current")


class _UserInfoPasswordSecret_Type(Integer32):
    """Custom type userInfoPasswordSecret based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cipher", 0),
          ("simple", 1))
    )


_UserInfoPasswordSecret_Type.__name__ = "Integer32"
_UserInfoPasswordSecret_Object = MibTableColumn
userInfoPasswordSecret = _UserInfoPasswordSecret_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 7, 1, 1, 1, 3),
    _UserInfoPasswordSecret_Type()
)
userInfoPasswordSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userInfoPasswordSecret.setStatus("current")


class _UserInfoOldPassword_Type(OctetString):
    """Custom type userInfoOldPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UserInfoOldPassword_Type.__name__ = "OctetString"
_UserInfoOldPassword_Object = MibTableColumn
userInfoOldPassword = _UserInfoOldPassword_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 7, 1, 1, 1, 4),
    _UserInfoOldPassword_Type()
)
userInfoOldPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userInfoOldPassword.setStatus("current")


class _UserInfoPassword_Type(OctetString):
    """Custom type userInfoPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UserInfoPassword_Type.__name__ = "OctetString"
_UserInfoPassword_Object = MibTableColumn
userInfoPassword = _UserInfoPassword_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 7, 1, 1, 1, 5),
    _UserInfoPassword_Type()
)
userInfoPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userInfoPassword.setStatus("current")


class _UserInfoConfirmedPassword_Type(OctetString):
    """Custom type userInfoConfirmedPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UserInfoConfirmedPassword_Type.__name__ = "OctetString"
_UserInfoConfirmedPassword_Object = MibTableColumn
userInfoConfirmedPassword = _UserInfoConfirmedPassword_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 7, 1, 1, 1, 6),
    _UserInfoConfirmedPassword_Type()
)
userInfoConfirmedPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userInfoConfirmedPassword.setStatus("current")
_UserInfoUserStatus_Type = TPRowStatus
_UserInfoUserStatus_Object = MibTableColumn
userInfoUserStatus = _UserInfoUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 7, 1, 1, 1, 7),
    _UserInfoUserStatus_Type()
)
userInfoUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userInfoUserStatus.setStatus("current")
_TplinkUserManageMIBNotifications_ObjectIdentity = ObjectIdentity
tplinkUserManageMIBNotifications = _TplinkUserManageMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 7, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-USERMANAGE-MIB",
    **{"tplinkUserInfoMIB": tplinkUserInfoMIB,
       "tplinkUserManageMIBObjects": tplinkUserManageMIBObjects,
       "userInfoUserTable": userInfoUserTable,
       "userInfoUserEntry": userInfoUserEntry,
       "userInfoUserName": userInfoUserName,
       "userInfoUserType": userInfoUserType,
       "userInfoPasswordSecret": userInfoPasswordSecret,
       "userInfoOldPassword": userInfoOldPassword,
       "userInfoPassword": userInfoPassword,
       "userInfoConfirmedPassword": userInfoConfirmedPassword,
       "userInfoUserStatus": userInfoUserStatus,
       "tplinkUserManageMIBNotifications": tplinkUserManageMIBNotifications}
)
