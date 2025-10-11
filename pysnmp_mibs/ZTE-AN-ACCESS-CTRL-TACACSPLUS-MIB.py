# SNMP MIB module (ZTE-AN-ACCESS-CTRL-TACACSPLUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-ACCESS-CTRL-TACACSPLUS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:54 2025
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

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY

zxAnAccessCtrlTacacsplusMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92)
)
if mibBuilder.loadTexts:
    zxAnAccessCtrlTacacsplusMib.setRevisions(
        ("2012-11-07 10:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnTacacsPlusGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnTacacsPlusGlobalObjects = _ZxAnTacacsPlusGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 1)
)


class _ZxAnTacacsPlusEnable_Type(Integer32):
    """Custom type zxAnTacacsPlusEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ZxAnTacacsPlusEnable_Type.__name__ = "Integer32"
_ZxAnTacacsPlusEnable_Object = MibScalar
zxAnTacacsPlusEnable = _ZxAnTacacsPlusEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 1, 1),
    _ZxAnTacacsPlusEnable_Type()
)
zxAnTacacsPlusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnTacacsPlusEnable.setStatus("current")


class _ZxAnTacacsPlusMaxPacketSize_Type(Integer32):
    """Custom type zxAnTacacsPlusMaxPacketSize based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 4096),
    )


_ZxAnTacacsPlusMaxPacketSize_Type.__name__ = "Integer32"
_ZxAnTacacsPlusMaxPacketSize_Object = MibScalar
zxAnTacacsPlusMaxPacketSize = _ZxAnTacacsPlusMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 1, 2),
    _ZxAnTacacsPlusMaxPacketSize_Type()
)
zxAnTacacsPlusMaxPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnTacacsPlusMaxPacketSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnTacacsPlusMaxPacketSize.setUnits("bytes")
_ZxAnTacacsPlusServerObjects_ObjectIdentity = ObjectIdentity
zxAnTacacsPlusServerObjects = _ZxAnTacacsPlusServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 2)
)
_ZxAnTacacsPlusSvrGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnTacacsPlusSvrGlobalObjects = _ZxAnTacacsPlusSvrGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 2, 1)
)


class _ZxAnTacacsPlusGlobalServerKey_Type(DisplayString):
    """Custom type zxAnTacacsPlusGlobalServerKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnTacacsPlusGlobalServerKey_Type.__name__ = "DisplayString"
_ZxAnTacacsPlusGlobalServerKey_Object = MibScalar
zxAnTacacsPlusGlobalServerKey = _ZxAnTacacsPlusGlobalServerKey_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 2, 1, 1),
    _ZxAnTacacsPlusGlobalServerKey_Type()
)
zxAnTacacsPlusGlobalServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnTacacsPlusGlobalServerKey.setStatus("current")


class _ZxAnTacacsPlusTimeout_Type(Integer32):
    """Custom type zxAnTacacsPlusTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ZxAnTacacsPlusTimeout_Type.__name__ = "Integer32"
_ZxAnTacacsPlusTimeout_Object = MibScalar
zxAnTacacsPlusTimeout = _ZxAnTacacsPlusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 2, 1, 2),
    _ZxAnTacacsPlusTimeout_Type()
)
zxAnTacacsPlusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnTacacsPlusTimeout.setStatus("current")
if mibBuilder.loadTexts:
    zxAnTacacsPlusTimeout.setUnits("seconds")
_ZxAnTacacsPlusServer_ObjectIdentity = ObjectIdentity
zxAnTacacsPlusServer = _ZxAnTacacsPlusServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 2, 2)
)
_ZxAnTacacsPlusServerTable_Object = MibTable
zxAnTacacsPlusServerTable = _ZxAnTacacsPlusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 2, 2, 2)
)
if mibBuilder.loadTexts:
    zxAnTacacsPlusServerTable.setStatus("current")
_ZxAnTacacsPlusServerEntry_Object = MibTableRow
zxAnTacacsPlusServerEntry = _ZxAnTacacsPlusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 2, 2, 2, 1)
)
zxAnTacacsPlusServerEntry.setIndexNames(
    (0, "ZTE-AN-ACCESS-CTRL-TACACSPLUS-MIB", "zxAnTacacsPlusServerIpType"),
    (0, "ZTE-AN-ACCESS-CTRL-TACACSPLUS-MIB", "zxAnTacacsPlusServerIpAddress"),
    (0, "ZTE-AN-ACCESS-CTRL-TACACSPLUS-MIB", "zxAnTacacsPlusServerPort"),
)
if mibBuilder.loadTexts:
    zxAnTacacsPlusServerEntry.setStatus("current")
_ZxAnTacacsPlusServerIpType_Type = InetAddressType
_ZxAnTacacsPlusServerIpType_Object = MibTableColumn
zxAnTacacsPlusServerIpType = _ZxAnTacacsPlusServerIpType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 2, 2, 2, 1, 1),
    _ZxAnTacacsPlusServerIpType_Type()
)
zxAnTacacsPlusServerIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnTacacsPlusServerIpType.setStatus("current")
_ZxAnTacacsPlusServerIpAddress_Type = InetAddress
_ZxAnTacacsPlusServerIpAddress_Object = MibTableColumn
zxAnTacacsPlusServerIpAddress = _ZxAnTacacsPlusServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 2, 2, 2, 1, 2),
    _ZxAnTacacsPlusServerIpAddress_Type()
)
zxAnTacacsPlusServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnTacacsPlusServerIpAddress.setStatus("current")


class _ZxAnTacacsPlusServerPort_Type(Integer32):
    """Custom type zxAnTacacsPlusServerPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(49, 49),
        ValueRangeConstraint(1025, 65535),
    )


_ZxAnTacacsPlusServerPort_Type.__name__ = "Integer32"
_ZxAnTacacsPlusServerPort_Object = MibTableColumn
zxAnTacacsPlusServerPort = _ZxAnTacacsPlusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 2, 2, 2, 1, 3),
    _ZxAnTacacsPlusServerPort_Type()
)
zxAnTacacsPlusServerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnTacacsPlusServerPort.setStatus("current")


class _ZxAnTacacsPlusServerKey_Type(DisplayString):
    """Custom type zxAnTacacsPlusServerKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnTacacsPlusServerKey_Type.__name__ = "DisplayString"
_ZxAnTacacsPlusServerKey_Object = MibTableColumn
zxAnTacacsPlusServerKey = _ZxAnTacacsPlusServerKey_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 2, 2, 2, 1, 4),
    _ZxAnTacacsPlusServerKey_Type()
)
zxAnTacacsPlusServerKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnTacacsPlusServerKey.setStatus("current")


class _ZxAnTacacsPlusServerTimeout_Type(Integer32):
    """Custom type zxAnTacacsPlusServerTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ZxAnTacacsPlusServerTimeout_Type.__name__ = "Integer32"
_ZxAnTacacsPlusServerTimeout_Object = MibTableColumn
zxAnTacacsPlusServerTimeout = _ZxAnTacacsPlusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 2, 2, 2, 1, 5),
    _ZxAnTacacsPlusServerTimeout_Type()
)
zxAnTacacsPlusServerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnTacacsPlusServerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    zxAnTacacsPlusServerTimeout.setUnits("seconds")
_ZxAnTacacsPlusServerRowStatus_Type = RowStatus
_ZxAnTacacsPlusServerRowStatus_Object = MibTableColumn
zxAnTacacsPlusServerRowStatus = _ZxAnTacacsPlusServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 2, 2, 2, 1, 50),
    _ZxAnTacacsPlusServerRowStatus_Type()
)
zxAnTacacsPlusServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnTacacsPlusServerRowStatus.setStatus("current")
_ZxAnTacacsPlusServerGroupTable_Object = MibTable
zxAnTacacsPlusServerGroupTable = _ZxAnTacacsPlusServerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 2, 2, 3)
)
if mibBuilder.loadTexts:
    zxAnTacacsPlusServerGroupTable.setStatus("current")
_ZxAnTacacsPlusServerGroupEntry_Object = MibTableRow
zxAnTacacsPlusServerGroupEntry = _ZxAnTacacsPlusServerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 2, 2, 3, 1)
)
zxAnTacacsPlusServerGroupEntry.setIndexNames(
    (0, "ZTE-AN-ACCESS-CTRL-TACACSPLUS-MIB", "zxAnTacacsPlusServerGrpName"),
    (0, "ZTE-AN-ACCESS-CTRL-TACACSPLUS-MIB", "zxAnTacacsPlusServerIpType"),
    (0, "ZTE-AN-ACCESS-CTRL-TACACSPLUS-MIB", "zxAnTacacsPlusServerIpAddress"),
    (0, "ZTE-AN-ACCESS-CTRL-TACACSPLUS-MIB", "zxAnTacacsPlusServerPort"),
)
if mibBuilder.loadTexts:
    zxAnTacacsPlusServerGroupEntry.setStatus("current")


class _ZxAnTacacsPlusServerGrpName_Type(DisplayString):
    """Custom type zxAnTacacsPlusServerGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnTacacsPlusServerGrpName_Type.__name__ = "DisplayString"
_ZxAnTacacsPlusServerGrpName_Object = MibTableColumn
zxAnTacacsPlusServerGrpName = _ZxAnTacacsPlusServerGrpName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 2, 2, 3, 1, 1),
    _ZxAnTacacsPlusServerGrpName_Type()
)
zxAnTacacsPlusServerGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnTacacsPlusServerGrpName.setStatus("current")
_ZxAnTacacsPlusServerGrpRowStatus_Type = RowStatus
_ZxAnTacacsPlusServerGrpRowStatus_Object = MibTableColumn
zxAnTacacsPlusServerGrpRowStatus = _ZxAnTacacsPlusServerGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 2, 2, 3, 1, 50),
    _ZxAnTacacsPlusServerGrpRowStatus_Type()
)
zxAnTacacsPlusServerGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnTacacsPlusServerGrpRowStatus.setStatus("current")
_ZxAnTacacsPlusClientObjects_ObjectIdentity = ObjectIdentity
zxAnTacacsPlusClientObjects = _ZxAnTacacsPlusClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 3)
)
_ZxAnTacacsPlusClntGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnTacacsPlusClntGlobalObjects = _ZxAnTacacsPlusClntGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 3, 1)
)
_ZxAnTacacsPlusClientIpType_Type = InetAddressType
_ZxAnTacacsPlusClientIpType_Object = MibScalar
zxAnTacacsPlusClientIpType = _ZxAnTacacsPlusClientIpType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 3, 1, 1),
    _ZxAnTacacsPlusClientIpType_Type()
)
zxAnTacacsPlusClientIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnTacacsPlusClientIpType.setStatus("current")
_ZxAnTacacsPlusClientIpAddr_Type = InetAddress
_ZxAnTacacsPlusClientIpAddr_Object = MibScalar
zxAnTacacsPlusClientIpAddr = _ZxAnTacacsPlusClientIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 3, 1, 2),
    _ZxAnTacacsPlusClientIpAddr_Type()
)
zxAnTacacsPlusClientIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnTacacsPlusClientIpAddr.setStatus("current")


class _ZxAnTacacsPlusClientPort_Type(Integer32):
    """Custom type zxAnTacacsPlusClientPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1025, 65535),
    )


_ZxAnTacacsPlusClientPort_Type.__name__ = "Integer32"
_ZxAnTacacsPlusClientPort_Object = MibScalar
zxAnTacacsPlusClientPort = _ZxAnTacacsPlusClientPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 92, 3, 1, 3),
    _ZxAnTacacsPlusClientPort_Type()
)
zxAnTacacsPlusClientPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnTacacsPlusClientPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-ACCESS-CTRL-TACACSPLUS-MIB",
    **{"zxAnAccessCtrlTacacsplusMib": zxAnAccessCtrlTacacsplusMib,
       "zxAnTacacsPlusGlobalObjects": zxAnTacacsPlusGlobalObjects,
       "zxAnTacacsPlusEnable": zxAnTacacsPlusEnable,
       "zxAnTacacsPlusMaxPacketSize": zxAnTacacsPlusMaxPacketSize,
       "zxAnTacacsPlusServerObjects": zxAnTacacsPlusServerObjects,
       "zxAnTacacsPlusSvrGlobalObjects": zxAnTacacsPlusSvrGlobalObjects,
       "zxAnTacacsPlusGlobalServerKey": zxAnTacacsPlusGlobalServerKey,
       "zxAnTacacsPlusTimeout": zxAnTacacsPlusTimeout,
       "zxAnTacacsPlusServer": zxAnTacacsPlusServer,
       "zxAnTacacsPlusServerTable": zxAnTacacsPlusServerTable,
       "zxAnTacacsPlusServerEntry": zxAnTacacsPlusServerEntry,
       "zxAnTacacsPlusServerIpType": zxAnTacacsPlusServerIpType,
       "zxAnTacacsPlusServerIpAddress": zxAnTacacsPlusServerIpAddress,
       "zxAnTacacsPlusServerPort": zxAnTacacsPlusServerPort,
       "zxAnTacacsPlusServerKey": zxAnTacacsPlusServerKey,
       "zxAnTacacsPlusServerTimeout": zxAnTacacsPlusServerTimeout,
       "zxAnTacacsPlusServerRowStatus": zxAnTacacsPlusServerRowStatus,
       "zxAnTacacsPlusServerGroupTable": zxAnTacacsPlusServerGroupTable,
       "zxAnTacacsPlusServerGroupEntry": zxAnTacacsPlusServerGroupEntry,
       "zxAnTacacsPlusServerGrpName": zxAnTacacsPlusServerGrpName,
       "zxAnTacacsPlusServerGrpRowStatus": zxAnTacacsPlusServerGrpRowStatus,
       "zxAnTacacsPlusClientObjects": zxAnTacacsPlusClientObjects,
       "zxAnTacacsPlusClntGlobalObjects": zxAnTacacsPlusClntGlobalObjects,
       "zxAnTacacsPlusClientIpType": zxAnTacacsPlusClientIpType,
       "zxAnTacacsPlusClientIpAddr": zxAnTacacsPlusClientIpAddr,
       "zxAnTacacsPlusClientPort": zxAnTacacsPlusClientPort}
)
