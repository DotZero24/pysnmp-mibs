# SNMP MIB module (AT-USER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/allied-old/AT-USER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:23:38 2025
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

(sysinfo,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "sysinfo")

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


# MODULE-IDENTITY

user = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20)
)
if mibBuilder.loadTexts:
    user.setRevisions(
        ("2008-10-16 12:00",
         "2008-08-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UserInfoTable_Object = MibTable
userInfoTable = _UserInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1)
)
if mibBuilder.loadTexts:
    userInfoTable.setStatus("current")
_UserInfoEntry_Object = MibTableRow
userInfoEntry = _UserInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1)
)
userInfoEntry.setIndexNames(
    (0, "AT-USER-MIB", "userInfoType"),
    (0, "AT-USER-MIB", "userInfoIndex"),
)
if mibBuilder.loadTexts:
    userInfoEntry.setStatus("current")


class _UserInfoType_Type(Integer32):
    """Custom type userInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("console", 1),
          ("aux", 2),
          ("telnet", 3),
          ("script", 4),
          ("stack", 5))
    )


_UserInfoType_Type.__name__ = "Integer32"
_UserInfoType_Object = MibTableColumn
userInfoType = _UserInfoType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 1),
    _UserInfoType_Type()
)
userInfoType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userInfoType.setStatus("current")


class _UserInfoIndex_Type(Unsigned32):
    """Custom type userInfoIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_UserInfoIndex_Type.__name__ = "Unsigned32"
_UserInfoIndex_Object = MibTableColumn
userInfoIndex = _UserInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 2),
    _UserInfoIndex_Type()
)
userInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userInfoIndex.setStatus("current")
_UserInfoUserName_Type = DisplayString
_UserInfoUserName_Object = MibTableColumn
userInfoUserName = _UserInfoUserName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 3),
    _UserInfoUserName_Type()
)
userInfoUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userInfoUserName.setStatus("current")


class _UserInfoPrivilegeLevel_Type(Unsigned32):
    """Custom type userInfoPrivilegeLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_UserInfoPrivilegeLevel_Type.__name__ = "Unsigned32"
_UserInfoPrivilegeLevel_Object = MibTableColumn
userInfoPrivilegeLevel = _UserInfoPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 4),
    _UserInfoPrivilegeLevel_Type()
)
userInfoPrivilegeLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userInfoPrivilegeLevel.setStatus("current")
_UserInfoIdleTime_Type = DisplayString
_UserInfoIdleTime_Object = MibTableColumn
userInfoIdleTime = _UserInfoIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 5),
    _UserInfoIdleTime_Type()
)
userInfoIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userInfoIdleTime.setStatus("current")
_UserInfoLocation_Type = DisplayString
_UserInfoLocation_Object = MibTableColumn
userInfoLocation = _UserInfoLocation_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 6),
    _UserInfoLocation_Type()
)
userInfoLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userInfoLocation.setStatus("current")
_UserConfigTable_Object = MibTable
userConfigTable = _UserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 2)
)
if mibBuilder.loadTexts:
    userConfigTable.setStatus("current")
_UserConfigEntry_Object = MibTableRow
userConfigEntry = _UserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 2, 1)
)
userConfigEntry.setIndexNames(
    (0, "AT-USER-MIB", "userConfigIndex"),
)
if mibBuilder.loadTexts:
    userConfigEntry.setStatus("current")
_UserConfigIndex_Type = Unsigned32
_UserConfigIndex_Object = MibTableColumn
userConfigIndex = _UserConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 2, 1, 1),
    _UserConfigIndex_Type()
)
userConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userConfigIndex.setStatus("current")
_UserConfigUsername_Type = DisplayString
_UserConfigUsername_Object = MibTableColumn
userConfigUsername = _UserConfigUsername_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 2, 1, 2),
    _UserConfigUsername_Type()
)
userConfigUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userConfigUsername.setStatus("current")


class _UserConfigPrivilegeLevel_Type(Unsigned32):
    """Custom type userConfigPrivilegeLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_UserConfigPrivilegeLevel_Type.__name__ = "Unsigned32"
_UserConfigPrivilegeLevel_Object = MibTableColumn
userConfigPrivilegeLevel = _UserConfigPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 2, 1, 3),
    _UserConfigPrivilegeLevel_Type()
)
userConfigPrivilegeLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userConfigPrivilegeLevel.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-USER-MIB",
    **{"user": user,
       "userInfoTable": userInfoTable,
       "userInfoEntry": userInfoEntry,
       "userInfoType": userInfoType,
       "userInfoIndex": userInfoIndex,
       "userInfoUserName": userInfoUserName,
       "userInfoPrivilegeLevel": userInfoPrivilegeLevel,
       "userInfoIdleTime": userInfoIdleTime,
       "userInfoLocation": userInfoLocation,
       "userConfigTable": userConfigTable,
       "userConfigEntry": userConfigEntry,
       "userConfigIndex": userConfigIndex,
       "userConfigUsername": userConfigUsername,
       "userConfigPrivilegeLevel": userConfigPrivilegeLevel}
)
