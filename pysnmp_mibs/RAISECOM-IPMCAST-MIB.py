# SNMP MIB module (RAISECOM-IPMCAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-IPMCAST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:33 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressType")

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(rcPortIndex,) = mibBuilder.importSymbols(
    "SWITCH-SYSTEM-MIB",
    "rcPortIndex")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

raisecomIpmcast = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 71)
)
if mibBuilder.loadTexts:
    raisecomIpmcast.setRevisions(
        ("2012-01-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaisecomIpmcastNotifications_ObjectIdentity = ObjectIdentity
raisecomIpmcastNotifications = _RaisecomIpmcastNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 71, 1)
)
_RaisecomIpmcastObjects_ObjectIdentity = ObjectIdentity
raisecomIpmcastObjects = _RaisecomIpmcastObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 71, 2)
)
_RaisecomIpMcastScalar_ObjectIdentity = ObjectIdentity
raisecomIpMcastScalar = _RaisecomIpMcastScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 71, 2, 1)
)
_RaisecomIpMcastRouteLimit_Type = Integer32
_RaisecomIpMcastRouteLimit_Object = MibScalar
raisecomIpMcastRouteLimit = _RaisecomIpMcastRouteLimit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 71, 2, 1, 1),
    _RaisecomIpMcastRouteLimit_Type()
)
raisecomIpMcastRouteLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIpMcastRouteLimit.setStatus("current")
_RaisecomIpMcastOifLimitPerRoute_Type = Integer32
_RaisecomIpMcastOifLimitPerRoute_Object = MibScalar
raisecomIpMcastOifLimitPerRoute = _RaisecomIpMcastOifLimitPerRoute_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 71, 2, 1, 2),
    _RaisecomIpMcastOifLimitPerRoute_Type()
)
raisecomIpMcastOifLimitPerRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIpMcastOifLimitPerRoute.setStatus("current")
_RaisecomIpMcastStaticTable_Object = MibTable
raisecomIpMcastStaticTable = _RaisecomIpMcastStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 71, 2, 2)
)
if mibBuilder.loadTexts:
    raisecomIpMcastStaticTable.setStatus("current")
_RaisecomIpMcastStaticEntry_Object = MibTableRow
raisecomIpMcastStaticEntry = _RaisecomIpMcastStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 71, 2, 2, 1)
)
raisecomIpMcastStaticEntry.setIndexNames(
    (0, "RAISECOM-IPMCAST-MIB", "raisecomIpMcastStaticSAddressType"),
    (0, "RAISECOM-IPMCAST-MIB", "raisecomIpMcastStaticSAddress"),
    (0, "RAISECOM-IPMCAST-MIB", "raisecomIpMcastStaticSAddressPrefix"),
)
if mibBuilder.loadTexts:
    raisecomIpMcastStaticEntry.setStatus("current")
_RaisecomIpMcastStaticSAddressType_Type = InetAddressType
_RaisecomIpMcastStaticSAddressType_Object = MibTableColumn
raisecomIpMcastStaticSAddressType = _RaisecomIpMcastStaticSAddressType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 71, 2, 2, 1, 1),
    _RaisecomIpMcastStaticSAddressType_Type()
)
raisecomIpMcastStaticSAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIpMcastStaticSAddressType.setStatus("current")
_RaisecomIpMcastStaticSAddress_Type = InetAddress
_RaisecomIpMcastStaticSAddress_Object = MibTableColumn
raisecomIpMcastStaticSAddress = _RaisecomIpMcastStaticSAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 71, 2, 2, 1, 2),
    _RaisecomIpMcastStaticSAddress_Type()
)
raisecomIpMcastStaticSAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIpMcastStaticSAddress.setStatus("current")
_RaisecomIpMcastStaticSAddressPrefix_Type = Integer32
_RaisecomIpMcastStaticSAddressPrefix_Object = MibTableColumn
raisecomIpMcastStaticSAddressPrefix = _RaisecomIpMcastStaticSAddressPrefix_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 71, 2, 2, 1, 3),
    _RaisecomIpMcastStaticSAddressPrefix_Type()
)
raisecomIpMcastStaticSAddressPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIpMcastStaticSAddressPrefix.setStatus("current")
_RaisecomIpMcastStaticNAddressType_Type = InetAddressType
_RaisecomIpMcastStaticNAddressType_Object = MibTableColumn
raisecomIpMcastStaticNAddressType = _RaisecomIpMcastStaticNAddressType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 71, 2, 2, 1, 4),
    _RaisecomIpMcastStaticNAddressType_Type()
)
raisecomIpMcastStaticNAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIpMcastStaticNAddressType.setStatus("current")
_RaisecomIpMcastStaticNAddress_Type = InetAddress
_RaisecomIpMcastStaticNAddress_Object = MibTableColumn
raisecomIpMcastStaticNAddress = _RaisecomIpMcastStaticNAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 71, 2, 2, 1, 5),
    _RaisecomIpMcastStaticNAddress_Type()
)
raisecomIpMcastStaticNAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIpMcastStaticNAddress.setStatus("current")
_RaisecomIpMcastStaticIfIndex_Type = InterfaceIndexOrZero
_RaisecomIpMcastStaticIfIndex_Object = MibTableColumn
raisecomIpMcastStaticIfIndex = _RaisecomIpMcastStaticIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 71, 2, 2, 1, 6),
    _RaisecomIpMcastStaticIfIndex_Type()
)
raisecomIpMcastStaticIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIpMcastStaticIfIndex.setStatus("current")


class _RaisecomIpMcastStaticPreference_Type(Integer32):
    """Custom type raisecomIpMcastStaticPreference based on Integer32"""
    defaultValue = 0


_RaisecomIpMcastStaticPreference_Type.__name__ = "Integer32"
_RaisecomIpMcastStaticPreference_Object = MibTableColumn
raisecomIpMcastStaticPreference = _RaisecomIpMcastStaticPreference_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 71, 2, 2, 1, 7),
    _RaisecomIpMcastStaticPreference_Type()
)
raisecomIpMcastStaticPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomIpMcastStaticPreference.setStatus("current")
_RaisecomIpMcastStaticRowStatus_Type = RowStatus
_RaisecomIpMcastStaticRowStatus_Object = MibTableColumn
raisecomIpMcastStaticRowStatus = _RaisecomIpMcastStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 71, 2, 2, 1, 8),
    _RaisecomIpMcastStaticRowStatus_Type()
)
raisecomIpMcastStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIpMcastStaticRowStatus.setStatus("current")
_RaisecomIpmcastConformance_ObjectIdentity = ObjectIdentity
raisecomIpmcastConformance = _RaisecomIpmcastConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 71, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-IPMCAST-MIB",
    **{"raisecomIpmcast": raisecomIpmcast,
       "raisecomIpmcastNotifications": raisecomIpmcastNotifications,
       "raisecomIpmcastObjects": raisecomIpmcastObjects,
       "raisecomIpMcastScalar": raisecomIpMcastScalar,
       "raisecomIpMcastRouteLimit": raisecomIpMcastRouteLimit,
       "raisecomIpMcastOifLimitPerRoute": raisecomIpMcastOifLimitPerRoute,
       "raisecomIpMcastStaticTable": raisecomIpMcastStaticTable,
       "raisecomIpMcastStaticEntry": raisecomIpMcastStaticEntry,
       "raisecomIpMcastStaticSAddressType": raisecomIpMcastStaticSAddressType,
       "raisecomIpMcastStaticSAddress": raisecomIpMcastStaticSAddress,
       "raisecomIpMcastStaticSAddressPrefix": raisecomIpMcastStaticSAddressPrefix,
       "raisecomIpMcastStaticNAddressType": raisecomIpMcastStaticNAddressType,
       "raisecomIpMcastStaticNAddress": raisecomIpMcastStaticNAddress,
       "raisecomIpMcastStaticIfIndex": raisecomIpMcastStaticIfIndex,
       "raisecomIpMcastStaticPreference": raisecomIpMcastStaticPreference,
       "raisecomIpMcastStaticRowStatus": raisecomIpMcastStaticRowStatus,
       "raisecomIpmcastConformance": raisecomIpmcastConformance}
)
