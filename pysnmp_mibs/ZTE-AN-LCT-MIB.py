# SNMP MIB module (ZTE-AN-LCT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-LCT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:23 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(zxAnSysObjects,) = mibBuilder.importSymbols(
    "ZTE-AN-SYS-MIB",
    "zxAnSysObjects")


# MODULE-IDENTITY

zxAnLctMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 150)
)
if mibBuilder.loadTexts:
    zxAnLctMib.setRevisions(
        ("2011-08-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnLctGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnLctGlobalObjects = _ZxAnLctGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 150, 1)
)


class _ZxAnLctAccessHeartbeatAction_Type(Integer32):
    """Custom type zxAnLctAccessHeartbeatAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("heartbeat", 1)
    )


_ZxAnLctAccessHeartbeatAction_Type.__name__ = "Integer32"
_ZxAnLctAccessHeartbeatAction_Object = MibScalar
zxAnLctAccessHeartbeatAction = _ZxAnLctAccessHeartbeatAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 150, 1, 1),
    _ZxAnLctAccessHeartbeatAction_Type()
)
zxAnLctAccessHeartbeatAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLctAccessHeartbeatAction.setStatus("current")


class _ZxAnLctAccessHeartbeatTimeOut_Type(Integer32):
    """Custom type zxAnLctAccessHeartbeatTimeOut based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_ZxAnLctAccessHeartbeatTimeOut_Type.__name__ = "Integer32"
_ZxAnLctAccessHeartbeatTimeOut_Object = MibScalar
zxAnLctAccessHeartbeatTimeOut = _ZxAnLctAccessHeartbeatTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 150, 1, 2),
    _ZxAnLctAccessHeartbeatTimeOut_Type()
)
zxAnLctAccessHeartbeatTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLctAccessHeartbeatTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    zxAnLctAccessHeartbeatTimeOut.setUnits("seconds")
_ZxAnLctObjects_ObjectIdentity = ObjectIdentity
zxAnLctObjects = _ZxAnLctObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 150, 2)
)
_ZxAnLctAccessObjects_ObjectIdentity = ObjectIdentity
zxAnLctAccessObjects = _ZxAnLctAccessObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 150, 2, 1)
)
_ZxAnLctAccessTable_Object = MibTable
zxAnLctAccessTable = _ZxAnLctAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 150, 2, 1, 1)
)
if mibBuilder.loadTexts:
    zxAnLctAccessTable.setStatus("current")
_ZxAnLctAccessEntry_Object = MibTableRow
zxAnLctAccessEntry = _ZxAnLctAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 150, 2, 1, 1, 1)
)
zxAnLctAccessEntry.setIndexNames(
    (0, "ZTE-AN-LCT-MIB", "zxAnLctAccessSessionId"),
)
if mibBuilder.loadTexts:
    zxAnLctAccessEntry.setStatus("current")


class _ZxAnLctAccessSessionId_Type(Integer32):
    """Custom type zxAnLctAccessSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ZxAnLctAccessSessionId_Type.__name__ = "Integer32"
_ZxAnLctAccessSessionId_Object = MibTableColumn
zxAnLctAccessSessionId = _ZxAnLctAccessSessionId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 150, 2, 1, 1, 1, 1),
    _ZxAnLctAccessSessionId_Type()
)
zxAnLctAccessSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnLctAccessSessionId.setStatus("current")


class _ZxAnLctAccessDetailInfo_Type(DisplayString):
    """Custom type zxAnLctAccessDetailInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_ZxAnLctAccessDetailInfo_Type.__name__ = "DisplayString"
_ZxAnLctAccessDetailInfo_Object = MibTableColumn
zxAnLctAccessDetailInfo = _ZxAnLctAccessDetailInfo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 150, 2, 1, 1, 1, 2),
    _ZxAnLctAccessDetailInfo_Type()
)
zxAnLctAccessDetailInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnLctAccessDetailInfo.setStatus("current")


class _ZxAnLctAccessSourceIpAddress_Type(DisplayString):
    """Custom type zxAnLctAccessSourceIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ZxAnLctAccessSourceIpAddress_Type.__name__ = "DisplayString"
_ZxAnLctAccessSourceIpAddress_Object = MibTableColumn
zxAnLctAccessSourceIpAddress = _ZxAnLctAccessSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 150, 2, 1, 1, 1, 3),
    _ZxAnLctAccessSourceIpAddress_Type()
)
zxAnLctAccessSourceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnLctAccessSourceIpAddress.setStatus("current")


class _ZxAnLctAccessUserName_Type(DisplayString):
    """Custom type zxAnLctAccessUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnLctAccessUserName_Type.__name__ = "DisplayString"
_ZxAnLctAccessUserName_Object = MibTableColumn
zxAnLctAccessUserName = _ZxAnLctAccessUserName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 150, 2, 1, 1, 1, 4),
    _ZxAnLctAccessUserName_Type()
)
zxAnLctAccessUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnLctAccessUserName.setStatus("current")
_ZxAnLctAccessRowStatus_Type = RowStatus
_ZxAnLctAccessRowStatus_Object = MibTableColumn
zxAnLctAccessRowStatus = _ZxAnLctAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 150, 2, 1, 1, 1, 50),
    _ZxAnLctAccessRowStatus_Type()
)
zxAnLctAccessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnLctAccessRowStatus.setStatus("current")
_ZxAnLctNotifications_ObjectIdentity = ObjectIdentity
zxAnLctNotifications = _ZxAnLctNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 150, 3)
)
_ZxAnLctAccessTraps_ObjectIdentity = ObjectIdentity
zxAnLctAccessTraps = _ZxAnLctAccessTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 150, 3, 1)
)
_ZxAnLctConformance_ObjectIdentity = ObjectIdentity
zxAnLctConformance = _ZxAnLctConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 150, 4)
)
_ZxAnLctCompliances_ObjectIdentity = ObjectIdentity
zxAnLctCompliances = _ZxAnLctCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 150, 4, 1)
)
_ZxAnLctGroups_ObjectIdentity = ObjectIdentity
zxAnLctGroups = _ZxAnLctGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 150, 4, 2)
)

# Managed Objects groups

zxAnLctGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 150, 4, 2, 1)
)
zxAnLctGlobalGroup.setObjects(
      *(("ZTE-AN-LCT-MIB", "zxAnLctAccessHeartbeatAction"),
        ("ZTE-AN-LCT-MIB", "zxAnLctAccessHeartbeatTimeOut"))
)
if mibBuilder.loadTexts:
    zxAnLctGlobalGroup.setStatus("current")

zxAnLctAccessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 150, 4, 2, 2)
)
zxAnLctAccessGroup.setObjects(
      *(("ZTE-AN-LCT-MIB", "zxAnLctAccessDetailInfo"),
        ("ZTE-AN-LCT-MIB", "zxAnLctAccessSourceIpAddress"),
        ("ZTE-AN-LCT-MIB", "zxAnLctAccessUserName"),
        ("ZTE-AN-LCT-MIB", "zxAnLctAccessRowStatus"))
)
if mibBuilder.loadTexts:
    zxAnLctAccessGroup.setStatus("current")

zxAnLctAccessTrapsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 150, 4, 2, 3)
)
zxAnLctAccessTrapsGroup.setObjects(
      *(("ZTE-AN-LCT-MIB", "zxAnLctAccessLoginTrap"),
        ("ZTE-AN-LCT-MIB", "zxAnLctAccessLogoutTrap"))
)
if mibBuilder.loadTexts:
    zxAnLctAccessTrapsGroup.setStatus("current")


# Notification objects

zxAnLctAccessLoginTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 150, 3, 1, 1)
)
zxAnLctAccessLoginTrap.setObjects(
      *(("ZTE-AN-LCT-MIB", "zxAnLctAccessSourceIpAddress"),
        ("ZTE-AN-LCT-MIB", "zxAnLctAccessUserName"),
        ("ZTE-AN-LCT-MIB", "zxAnLctAccessDetailInfo"))
)
if mibBuilder.loadTexts:
    zxAnLctAccessLoginTrap.setStatus(
        "current"
    )

zxAnLctAccessLogoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 150, 3, 1, 2)
)
zxAnLctAccessLogoutTrap.setObjects(
      *(("ZTE-AN-LCT-MIB", "zxAnLctAccessSourceIpAddress"),
        ("ZTE-AN-LCT-MIB", "zxAnLctAccessUserName"),
        ("ZTE-AN-LCT-MIB", "zxAnLctAccessDetailInfo"))
)
if mibBuilder.loadTexts:
    zxAnLctAccessLogoutTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

zxAnLctCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 150, 4, 1, 1)
)
zxAnLctCompliance.setObjects(
      *(("ZTE-AN-LCT-MIB", "zxAnLctGlobalGroup"),
        ("ZTE-AN-LCT-MIB", "zxAnLctAccessGroup"),
        ("ZTE-AN-LCT-MIB", "zxAnLctAccessTrapsGroup"))
)
if mibBuilder.loadTexts:
    zxAnLctCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-LCT-MIB",
    **{"zxAnLctMib": zxAnLctMib,
       "zxAnLctGlobalObjects": zxAnLctGlobalObjects,
       "zxAnLctAccessHeartbeatAction": zxAnLctAccessHeartbeatAction,
       "zxAnLctAccessHeartbeatTimeOut": zxAnLctAccessHeartbeatTimeOut,
       "zxAnLctObjects": zxAnLctObjects,
       "zxAnLctAccessObjects": zxAnLctAccessObjects,
       "zxAnLctAccessTable": zxAnLctAccessTable,
       "zxAnLctAccessEntry": zxAnLctAccessEntry,
       "zxAnLctAccessSessionId": zxAnLctAccessSessionId,
       "zxAnLctAccessDetailInfo": zxAnLctAccessDetailInfo,
       "zxAnLctAccessSourceIpAddress": zxAnLctAccessSourceIpAddress,
       "zxAnLctAccessUserName": zxAnLctAccessUserName,
       "zxAnLctAccessRowStatus": zxAnLctAccessRowStatus,
       "zxAnLctNotifications": zxAnLctNotifications,
       "zxAnLctAccessTraps": zxAnLctAccessTraps,
       "zxAnLctAccessLoginTrap": zxAnLctAccessLoginTrap,
       "zxAnLctAccessLogoutTrap": zxAnLctAccessLogoutTrap,
       "zxAnLctConformance": zxAnLctConformance,
       "zxAnLctCompliances": zxAnLctCompliances,
       "zxAnLctCompliance": zxAnLctCompliance,
       "zxAnLctGroups": zxAnLctGroups,
       "zxAnLctGlobalGroup": zxAnLctGlobalGroup,
       "zxAnLctAccessGroup": zxAnLctAccessGroup,
       "zxAnLctAccessTrapsGroup": zxAnLctAccessTrapsGroup}
)
