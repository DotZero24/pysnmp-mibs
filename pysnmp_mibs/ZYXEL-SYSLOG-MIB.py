# SNMP MIB module (ZYXEL-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zyxel/ZYXEL-SYSLOG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:02:32 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelSysLog = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelSysLogSetup_ObjectIdentity = ObjectIdentity
zyxelSysLogSetup = _ZyxelSysLogSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1)
)
_ZySysLogState_Type = EnabledStatus
_ZySysLogState_Object = MibScalar
zySysLogState = _ZySysLogState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 1),
    _ZySysLogState_Type()
)
zySysLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysLogState.setStatus("current")
_ZyxelSysLogTypeTable_Object = MibTable
zyxelSysLogTypeTable = _ZyxelSysLogTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelSysLogTypeTable.setStatus("current")
_ZyxelSysLogTypeEntry_Object = MibTableRow
zyxelSysLogTypeEntry = _ZyxelSysLogTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 2, 1)
)
zyxelSysLogTypeEntry.setIndexNames(
    (0, "ZYXEL-SYSLOG-MIB", "zySysLogTypeIndex"),
)
if mibBuilder.loadTexts:
    zyxelSysLogTypeEntry.setStatus("current")
_ZySysLogTypeIndex_Type = Integer32
_ZySysLogTypeIndex_Object = MibTableColumn
zySysLogTypeIndex = _ZySysLogTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 2, 1, 1),
    _ZySysLogTypeIndex_Type()
)
zySysLogTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zySysLogTypeIndex.setStatus("current")
_ZySysLogTypeName_Type = DisplayString
_ZySysLogTypeName_Object = MibTableColumn
zySysLogTypeName = _ZySysLogTypeName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 2, 1, 2),
    _ZySysLogTypeName_Type()
)
zySysLogTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysLogTypeName.setStatus("current")
_ZySysLogTypeState_Type = EnabledStatus
_ZySysLogTypeState_Object = MibTableColumn
zySysLogTypeState = _ZySysLogTypeState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 2, 1, 3),
    _ZySysLogTypeState_Type()
)
zySysLogTypeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysLogTypeState.setStatus("current")


class _ZySysLogTypeFacility_Type(Integer32):
    """Custom type zySysLogTypeFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("localUser0", 0),
          ("localUser1", 1),
          ("localUser2", 2),
          ("localUser3", 3),
          ("localUser4", 4),
          ("localUser5", 5),
          ("localUser6", 6),
          ("localUser7", 7))
    )


_ZySysLogTypeFacility_Type.__name__ = "Integer32"
_ZySysLogTypeFacility_Object = MibTableColumn
zySysLogTypeFacility = _ZySysLogTypeFacility_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 2, 1, 4),
    _ZySysLogTypeFacility_Type()
)
zySysLogTypeFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysLogTypeFacility.setStatus("current")
_ZySysLogMaxNumberOfServers_Type = Integer32
_ZySysLogMaxNumberOfServers_Object = MibScalar
zySysLogMaxNumberOfServers = _ZySysLogMaxNumberOfServers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 3),
    _ZySysLogMaxNumberOfServers_Type()
)
zySysLogMaxNumberOfServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysLogMaxNumberOfServers.setStatus("current")
_ZyxelSysLogServerInetTable_Object = MibTable
zyxelSysLogServerInetTable = _ZyxelSysLogServerInetTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 5)
)
if mibBuilder.loadTexts:
    zyxelSysLogServerInetTable.setStatus("current")
_ZyxelSysLogServerInetEntry_Object = MibTableRow
zyxelSysLogServerInetEntry = _ZyxelSysLogServerInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 5, 1)
)
zyxelSysLogServerInetEntry.setIndexNames(
    (0, "ZYXEL-SYSLOG-MIB", "zySysLogServerInetAddressType"),
    (0, "ZYXEL-SYSLOG-MIB", "zySysLogServerInetAddress"),
)
if mibBuilder.loadTexts:
    zyxelSysLogServerInetEntry.setStatus("current")
_ZySysLogServerInetAddressType_Type = InetAddressType
_ZySysLogServerInetAddressType_Object = MibTableColumn
zySysLogServerInetAddressType = _ZySysLogServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 5, 1, 1),
    _ZySysLogServerInetAddressType_Type()
)
zySysLogServerInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zySysLogServerInetAddressType.setStatus("current")


class _ZySysLogServerInetAddress_Type(InetAddress):
    """Custom type zySysLogServerInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZySysLogServerInetAddress_Type.__name__ = "InetAddress"
_ZySysLogServerInetAddress_Object = MibTableColumn
zySysLogServerInetAddress = _ZySysLogServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 5, 1, 2),
    _ZySysLogServerInetAddress_Type()
)
zySysLogServerInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zySysLogServerInetAddress.setStatus("current")


class _ZySysLogServerInetLogLevel_Type(Integer32):
    """Custom type zySysLogServerInetLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("level0", 0),
          ("level0To1", 1),
          ("level0To2", 2),
          ("level0To3", 3),
          ("level0To4", 4),
          ("level0To5", 5),
          ("level0To6", 6),
          ("level0To7", 7))
    )


_ZySysLogServerInetLogLevel_Type.__name__ = "Integer32"
_ZySysLogServerInetLogLevel_Object = MibTableColumn
zySysLogServerInetLogLevel = _ZySysLogServerInetLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 5, 1, 3),
    _ZySysLogServerInetLogLevel_Type()
)
zySysLogServerInetLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysLogServerInetLogLevel.setStatus("current")


class _ZySysLogServerInetUdpPort_Type(Integer32):
    """Custom type zySysLogServerInetUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZySysLogServerInetUdpPort_Type.__name__ = "Integer32"
_ZySysLogServerInetUdpPort_Object = MibTableColumn
zySysLogServerInetUdpPort = _ZySysLogServerInetUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 5, 1, 4),
    _ZySysLogServerInetUdpPort_Type()
)
zySysLogServerInetUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysLogServerInetUdpPort.setStatus("current")
_ZySysLogServerInetRowStatus_Type = RowStatus
_ZySysLogServerInetRowStatus_Object = MibTableColumn
zySysLogServerInetRowStatus = _ZySysLogServerInetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 5, 1, 5),
    _ZySysLogServerInetRowStatus_Type()
)
zySysLogServerInetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zySysLogServerInetRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-SYSLOG-MIB",
    **{"zyxelSysLog": zyxelSysLog,
       "zyxelSysLogSetup": zyxelSysLogSetup,
       "zySysLogState": zySysLogState,
       "zyxelSysLogTypeTable": zyxelSysLogTypeTable,
       "zyxelSysLogTypeEntry": zyxelSysLogTypeEntry,
       "zySysLogTypeIndex": zySysLogTypeIndex,
       "zySysLogTypeName": zySysLogTypeName,
       "zySysLogTypeState": zySysLogTypeState,
       "zySysLogTypeFacility": zySysLogTypeFacility,
       "zySysLogMaxNumberOfServers": zySysLogMaxNumberOfServers,
       "zyxelSysLogServerInetTable": zyxelSysLogServerInetTable,
       "zyxelSysLogServerInetEntry": zyxelSysLogServerInetEntry,
       "zySysLogServerInetAddressType": zySysLogServerInetAddressType,
       "zySysLogServerInetAddress": zySysLogServerInetAddress,
       "zySysLogServerInetLogLevel": zySysLogServerInetLogLevel,
       "zySysLogServerInetUdpPort": zySysLogServerInetUdpPort,
       "zySysLogServerInetRowStatus": zySysLogServerInetRowStatus}
)
