# SNMP MIB module (ZTE-AN-FILE-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-FILE-SERVER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:05 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY

zxAnFileServerMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 17)
)
if mibBuilder.loadTexts:
    zxAnFileServerMib.setRevisions(
        ("2011-05-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnFileServerObjects_ObjectIdentity = ObjectIdentity
zxAnFileServerObjects = _ZxAnFileServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 17, 2)
)
_ZxAnFileServerGroupTable_Object = MibTable
zxAnFileServerGroupTable = _ZxAnFileServerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 17, 2, 2)
)
if mibBuilder.loadTexts:
    zxAnFileServerGroupTable.setStatus("current")
_ZxAnFileServerGroupEntry_Object = MibTableRow
zxAnFileServerGroupEntry = _ZxAnFileServerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 17, 2, 2, 1)
)
zxAnFileServerGroupEntry.setIndexNames(
    (0, "ZTE-AN-FILE-SERVER-MIB", "zxAnFileServerGroupUsage"),
)
if mibBuilder.loadTexts:
    zxAnFileServerGroupEntry.setStatus("current")


class _ZxAnFileServerGroupUsage_Type(Integer32):
    """Custom type zxAnFileServerGroupUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              31)
        )
    )
    namedValues = NamedValues(
        *(("autoBackupConfiguration", 1),
          ("manualBackupConfiguration", 2),
          ("autoBackupLog", 3),
          ("manualBackupLog", 4),
          ("autoBackupSoftware", 5),
          ("manualBackupSoftware", 6),
          ("downloadPerformance", 7),
          ("uploadPerformance", 8),
          ("autoUpdateSoftware", 31))
    )


_ZxAnFileServerGroupUsage_Type.__name__ = "Integer32"
_ZxAnFileServerGroupUsage_Object = MibTableColumn
zxAnFileServerGroupUsage = _ZxAnFileServerGroupUsage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 17, 2, 2, 1, 1),
    _ZxAnFileServerGroupUsage_Type()
)
zxAnFileServerGroupUsage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnFileServerGroupUsage.setStatus("current")


class _ZxAnFileServerGroupWorkMode_Type(Integer32):
    """Custom type zxAnFileServerGroupWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("roundRobin", 1)
    )


_ZxAnFileServerGroupWorkMode_Type.__name__ = "Integer32"
_ZxAnFileServerGroupWorkMode_Object = MibTableColumn
zxAnFileServerGroupWorkMode = _ZxAnFileServerGroupWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 17, 2, 2, 1, 2),
    _ZxAnFileServerGroupWorkMode_Type()
)
zxAnFileServerGroupWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileServerGroupWorkMode.setStatus("current")
_ZxAnFileServerTable_Object = MibTable
zxAnFileServerTable = _ZxAnFileServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 17, 2, 3)
)
if mibBuilder.loadTexts:
    zxAnFileServerTable.setStatus("current")
_ZxAnFileServerEntry_Object = MibTableRow
zxAnFileServerEntry = _ZxAnFileServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 17, 2, 3, 1)
)
zxAnFileServerEntry.setIndexNames(
    (0, "ZTE-AN-FILE-SERVER-MIB", "zxAnFileServerGroupUsage"),
    (0, "ZTE-AN-FILE-SERVER-MIB", "zxAnFileServerIndex"),
)
if mibBuilder.loadTexts:
    zxAnFileServerEntry.setStatus("current")


class _ZxAnFileServerIndex_Type(Integer32):
    """Custom type zxAnFileServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ZxAnFileServerIndex_Type.__name__ = "Integer32"
_ZxAnFileServerIndex_Object = MibTableColumn
zxAnFileServerIndex = _ZxAnFileServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 17, 2, 3, 1, 1),
    _ZxAnFileServerIndex_Type()
)
zxAnFileServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnFileServerIndex.setStatus("current")


class _ZxAnFileServerIpAddressType_Type(InetAddressType):
    """Custom type zxAnFileServerIpAddressType based on InetAddressType"""
    defaultValue = 1


_ZxAnFileServerIpAddressType_Type.__name__ = "InetAddressType"
_ZxAnFileServerIpAddressType_Object = MibTableColumn
zxAnFileServerIpAddressType = _ZxAnFileServerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 17, 2, 3, 1, 2),
    _ZxAnFileServerIpAddressType_Type()
)
zxAnFileServerIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileServerIpAddressType.setStatus("current")
_ZxAnFileServerIpAddress_Type = InetAddress
_ZxAnFileServerIpAddress_Object = MibTableColumn
zxAnFileServerIpAddress = _ZxAnFileServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 17, 2, 3, 1, 3),
    _ZxAnFileServerIpAddress_Type()
)
zxAnFileServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileServerIpAddress.setStatus("current")


class _ZxAnFileServerProtocolType_Type(Integer32):
    """Custom type zxAnFileServerProtocolType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("sftp", 2),
          ("none", 3))
    )


_ZxAnFileServerProtocolType_Type.__name__ = "Integer32"
_ZxAnFileServerProtocolType_Object = MibTableColumn
zxAnFileServerProtocolType = _ZxAnFileServerProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 17, 2, 3, 1, 4),
    _ZxAnFileServerProtocolType_Type()
)
zxAnFileServerProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileServerProtocolType.setStatus("current")


class _ZxAnFileServerUserName_Type(DisplayString):
    """Custom type zxAnFileServerUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnFileServerUserName_Type.__name__ = "DisplayString"
_ZxAnFileServerUserName_Object = MibTableColumn
zxAnFileServerUserName = _ZxAnFileServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 17, 2, 3, 1, 5),
    _ZxAnFileServerUserName_Type()
)
zxAnFileServerUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileServerUserName.setStatus("current")


class _ZxAnFileServerUserPwd_Type(DisplayString):
    """Custom type zxAnFileServerUserPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnFileServerUserPwd_Type.__name__ = "DisplayString"
_ZxAnFileServerUserPwd_Object = MibTableColumn
zxAnFileServerUserPwd = _ZxAnFileServerUserPwd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 17, 2, 3, 1, 6),
    _ZxAnFileServerUserPwd_Type()
)
zxAnFileServerUserPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileServerUserPwd.setStatus("current")


class _ZxAnFileServerPath_Type(DisplayString):
    """Custom type zxAnFileServerPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnFileServerPath_Type.__name__ = "DisplayString"
_ZxAnFileServerPath_Object = MibTableColumn
zxAnFileServerPath = _ZxAnFileServerPath_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 17, 2, 3, 1, 7),
    _ZxAnFileServerPath_Type()
)
zxAnFileServerPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileServerPath.setStatus("current")
_ZxAnFileServerConformance_ObjectIdentity = ObjectIdentity
zxAnFileServerConformance = _ZxAnFileServerConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 17, 4)
)
_ZxAnFileServerCompliances_ObjectIdentity = ObjectIdentity
zxAnFileServerCompliances = _ZxAnFileServerCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 17, 4, 1)
)
_ZxAnFileServerGroups_ObjectIdentity = ObjectIdentity
zxAnFileServerGroups = _ZxAnFileServerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 17, 4, 2)
)

# Managed Objects groups

zxAnFileServerGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 17, 4, 2, 1)
)
zxAnFileServerGroupGroup.setObjects(
    ("ZTE-AN-FILE-SERVER-MIB", "zxAnFileServerGroupWorkMode")
)
if mibBuilder.loadTexts:
    zxAnFileServerGroupGroup.setStatus("current")

zxAnFileServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 17, 4, 2, 2)
)
zxAnFileServerGroup.setObjects(
      *(("ZTE-AN-FILE-SERVER-MIB", "zxAnFileServerIpAddressType"),
        ("ZTE-AN-FILE-SERVER-MIB", "zxAnFileServerIpAddress"),
        ("ZTE-AN-FILE-SERVER-MIB", "zxAnFileServerProtocolType"),
        ("ZTE-AN-FILE-SERVER-MIB", "zxAnFileServerUserName"),
        ("ZTE-AN-FILE-SERVER-MIB", "zxAnFileServerUserPwd"),
        ("ZTE-AN-FILE-SERVER-MIB", "zxAnFileServerPath"))
)
if mibBuilder.loadTexts:
    zxAnFileServerGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

zxAnFileServerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 17, 4, 1, 1)
)
zxAnFileServerCompliance.setObjects(
      *(("ZTE-AN-FILE-SERVER-MIB", "zxAnFileServerGroupGroup"),
        ("ZTE-AN-FILE-SERVER-MIB", "zxAnFileServerGroup"))
)
if mibBuilder.loadTexts:
    zxAnFileServerCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-FILE-SERVER-MIB",
    **{"zxAnFileServerMib": zxAnFileServerMib,
       "zxAnFileServerObjects": zxAnFileServerObjects,
       "zxAnFileServerGroupTable": zxAnFileServerGroupTable,
       "zxAnFileServerGroupEntry": zxAnFileServerGroupEntry,
       "zxAnFileServerGroupUsage": zxAnFileServerGroupUsage,
       "zxAnFileServerGroupWorkMode": zxAnFileServerGroupWorkMode,
       "zxAnFileServerTable": zxAnFileServerTable,
       "zxAnFileServerEntry": zxAnFileServerEntry,
       "zxAnFileServerIndex": zxAnFileServerIndex,
       "zxAnFileServerIpAddressType": zxAnFileServerIpAddressType,
       "zxAnFileServerIpAddress": zxAnFileServerIpAddress,
       "zxAnFileServerProtocolType": zxAnFileServerProtocolType,
       "zxAnFileServerUserName": zxAnFileServerUserName,
       "zxAnFileServerUserPwd": zxAnFileServerUserPwd,
       "zxAnFileServerPath": zxAnFileServerPath,
       "zxAnFileServerConformance": zxAnFileServerConformance,
       "zxAnFileServerCompliances": zxAnFileServerCompliances,
       "zxAnFileServerCompliance": zxAnFileServerCompliance,
       "zxAnFileServerGroups": zxAnFileServerGroups,
       "zxAnFileServerGroupGroup": zxAnFileServerGroupGroup,
       "zxAnFileServerGroup": zxAnFileServerGroup}
)
