# SNMP MIB module (INFINERA-TP-OSCCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-OSCCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:19 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(InfnAdminState,) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnAdminState")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

oscCtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 13)
)
if mibBuilder.loadTexts:
    oscCtpMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OscCtpTable_Object = MibTable
oscCtpTable = _OscCtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 13, 1)
)
if mibBuilder.loadTexts:
    oscCtpTable.setStatus("current")
_OscCtpEntry_Object = MibTableRow
oscCtpEntry = _OscCtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 13, 1, 1)
)
oscCtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oscCtpEntry.setStatus("current")
_OscCtpOscIpAddressType_Type = InetAddressType
_OscCtpOscIpAddressType_Object = MibTableColumn
oscCtpOscIpAddressType = _OscCtpOscIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 13, 1, 1, 1),
    _OscCtpOscIpAddressType_Type()
)
oscCtpOscIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oscCtpOscIpAddressType.setStatus("current")
_OscCtpOscIpAddress_Type = InetAddress
_OscCtpOscIpAddress_Object = MibTableColumn
oscCtpOscIpAddress = _OscCtpOscIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 13, 1, 1, 2),
    _OscCtpOscIpAddress_Type()
)
oscCtpOscIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oscCtpOscIpAddress.setStatus("current")
_OscCtpOscNetmask_Type = InetAddress
_OscCtpOscNetmask_Object = MibTableColumn
oscCtpOscNetmask = _OscCtpOscNetmask_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 13, 1, 1, 3),
    _OscCtpOscNetmask_Type()
)
oscCtpOscNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oscCtpOscNetmask.setStatus("current")
_OscCtpOscIpIfAdminState_Type = InfnAdminState
_OscCtpOscIpIfAdminState_Object = MibTableColumn
oscCtpOscIpIfAdminState = _OscCtpOscIpIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 13, 1, 1, 4),
    _OscCtpOscIpIfAdminState_Type()
)
oscCtpOscIpIfAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oscCtpOscIpIfAdminState.setStatus("current")


class _OscCtpOspfCost_Type(Integer32):
    """Custom type oscCtpOspfCost based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OscCtpOspfCost_Type.__name__ = "Integer32"
_OscCtpOspfCost_Object = MibTableColumn
oscCtpOspfCost = _OscCtpOspfCost_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 13, 1, 1, 5),
    _OscCtpOspfCost_Type()
)
oscCtpOspfCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oscCtpOspfCost.setStatus("obsolete")


class _OscCtpTECost_Type(Integer32):
    """Custom type oscCtpTECost based on Integer32"""
    defaultValue = 100


_OscCtpTECost_Type.__name__ = "Integer32"
_OscCtpTECost_Object = MibTableColumn
oscCtpTECost = _OscCtpTECost_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 13, 1, 1, 6),
    _OscCtpTECost_Type()
)
oscCtpTECost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oscCtpTECost.setStatus("obsolete")


class _OscCtpOspfHelloInterval_Type(Integer32):
    """Custom type oscCtpOspfHelloInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1200),
    )


_OscCtpOspfHelloInterval_Type.__name__ = "Integer32"
_OscCtpOspfHelloInterval_Object = MibTableColumn
oscCtpOspfHelloInterval = _OscCtpOspfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 13, 1, 1, 7),
    _OscCtpOspfHelloInterval_Type()
)
oscCtpOspfHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oscCtpOspfHelloInterval.setStatus("obsolete")
if mibBuilder.loadTexts:
    oscCtpOspfHelloInterval.setUnits("seconds")
_OscCtpOspfArea_Type = InetAddress
_OscCtpOspfArea_Object = MibTableColumn
oscCtpOspfArea = _OscCtpOspfArea_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 13, 1, 1, 8),
    _OscCtpOspfArea_Type()
)
oscCtpOspfArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscCtpOspfArea.setStatus("obsolete")


class _OscCtpOspfDeadInterval_Type(Integer32):
    """Custom type oscCtpOspfDeadInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_OscCtpOspfDeadInterval_Type.__name__ = "Integer32"
_OscCtpOspfDeadInterval_Object = MibTableColumn
oscCtpOspfDeadInterval = _OscCtpOspfDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 13, 1, 1, 9),
    _OscCtpOspfDeadInterval_Type()
)
oscCtpOspfDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oscCtpOspfDeadInterval.setStatus("obsolete")
if mibBuilder.loadTexts:
    oscCtpOspfDeadInterval.setUnits("seconds")
_OscCtpOspfInstanceId_Type = Integer32
_OscCtpOspfInstanceId_Object = MibTableColumn
oscCtpOspfInstanceId = _OscCtpOspfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 13, 1, 1, 10),
    _OscCtpOspfInstanceId_Type()
)
oscCtpOspfInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscCtpOspfInstanceId.setStatus("obsolete")


class _OscCtpOspfRoutingEnabled_Type(TruthValue):
    """Custom type oscCtpOspfRoutingEnabled based on TruthValue"""
    defaultValue = 2


_OscCtpOspfRoutingEnabled_Type.__name__ = "TruthValue"
_OscCtpOspfRoutingEnabled_Object = MibTableColumn
oscCtpOspfRoutingEnabled = _OscCtpOspfRoutingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 13, 1, 1, 11),
    _OscCtpOspfRoutingEnabled_Type()
)
oscCtpOspfRoutingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oscCtpOspfRoutingEnabled.setStatus("obsolete")


class _OscCtpPmHistStatsEnable_Type(Integer32):
    """Custom type oscCtpPmHistStatsEnable based on Integer32"""
    defaultValue = 1

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


_OscCtpPmHistStatsEnable_Type.__name__ = "Integer32"
_OscCtpPmHistStatsEnable_Object = MibTableColumn
oscCtpPmHistStatsEnable = _OscCtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 13, 1, 1, 12),
    _OscCtpPmHistStatsEnable_Type()
)
oscCtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oscCtpPmHistStatsEnable.setStatus("current")
_OscCtpConformance_ObjectIdentity = ObjectIdentity
oscCtpConformance = _OscCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 13, 3)
)
_OscCtpCompliances_ObjectIdentity = ObjectIdentity
oscCtpCompliances = _OscCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 13, 3, 1)
)
_OscCtpGroups_ObjectIdentity = ObjectIdentity
oscCtpGroups = _OscCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 13, 3, 2)
)

# Managed Objects groups

oscCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 13, 3, 2, 1)
)
oscCtpGroup.setObjects(
      *(("INFINERA-TP-OSCCTP-MIB", "oscCtpOscIpAddressType"),
        ("INFINERA-TP-OSCCTP-MIB", "oscCtpOscIpAddress"),
        ("INFINERA-TP-OSCCTP-MIB", "oscCtpOscNetmask"),
        ("INFINERA-TP-OSCCTP-MIB", "oscCtpOspfCost"),
        ("INFINERA-TP-OSCCTP-MIB", "oscCtpTECost"),
        ("INFINERA-TP-OSCCTP-MIB", "oscCtpOspfHelloInterval"),
        ("INFINERA-TP-OSCCTP-MIB", "oscCtpOspfArea"),
        ("INFINERA-TP-OSCCTP-MIB", "oscCtpOspfDeadInterval"),
        ("INFINERA-TP-OSCCTP-MIB", "oscCtpOspfInstanceId"),
        ("INFINERA-TP-OSCCTP-MIB", "oscCtpOspfRoutingEnabled"),
        ("INFINERA-TP-OSCCTP-MIB", "oscCtpPmHistStatsEnable"))
)
if mibBuilder.loadTexts:
    oscCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oscCtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 13, 3, 1, 1)
)
oscCtpCompliance.setObjects(
    ("INFINERA-TP-OSCCTP-MIB", "oscCtpGroup")
)
if mibBuilder.loadTexts:
    oscCtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-OSCCTP-MIB",
    **{"oscCtpMIB": oscCtpMIB,
       "oscCtpTable": oscCtpTable,
       "oscCtpEntry": oscCtpEntry,
       "oscCtpOscIpAddressType": oscCtpOscIpAddressType,
       "oscCtpOscIpAddress": oscCtpOscIpAddress,
       "oscCtpOscNetmask": oscCtpOscNetmask,
       "oscCtpOscIpIfAdminState": oscCtpOscIpIfAdminState,
       "oscCtpOspfCost": oscCtpOspfCost,
       "oscCtpTECost": oscCtpTECost,
       "oscCtpOspfHelloInterval": oscCtpOspfHelloInterval,
       "oscCtpOspfArea": oscCtpOspfArea,
       "oscCtpOspfDeadInterval": oscCtpOspfDeadInterval,
       "oscCtpOspfInstanceId": oscCtpOspfInstanceId,
       "oscCtpOspfRoutingEnabled": oscCtpOspfRoutingEnabled,
       "oscCtpPmHistStatsEnable": oscCtpPmHistStatsEnable,
       "oscCtpConformance": oscCtpConformance,
       "oscCtpCompliances": oscCtpCompliances,
       "oscCtpCompliance": oscCtpCompliance,
       "oscCtpGroups": oscCtpGroups,
       "oscCtpGroup": oscCtpGroup}
)
