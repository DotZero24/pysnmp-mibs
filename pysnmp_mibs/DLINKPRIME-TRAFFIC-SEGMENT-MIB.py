# SNMP MIB module (DLINKPRIME-TRAFFIC-SEGMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-TRAFFIC-SEGMENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:52:10 2025
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

(dlinkPrimeCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkPrimeCommon")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

dlinkPrimeTrafficSegMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 25)
)
if mibBuilder.loadTexts:
    dlinkPrimeTrafficSegMIB.setRevisions(
        ("2014-04-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpTrafficSegNotifications_ObjectIdentity = ObjectIdentity
dpTrafficSegNotifications = _DpTrafficSegNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 25, 0)
)
_DpTrafficSegObjects_ObjectIdentity = ObjectIdentity
dpTrafficSegObjects = _DpTrafficSegObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 25, 1)
)
_DpTrafficSegForwardDomainTable_Object = MibTable
dpTrafficSegForwardDomainTable = _DpTrafficSegForwardDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 25, 1, 1)
)
if mibBuilder.loadTexts:
    dpTrafficSegForwardDomainTable.setStatus("current")
_DpTrafficSegForwardDomainEntry_Object = MibTableRow
dpTrafficSegForwardDomainEntry = _DpTrafficSegForwardDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 25, 1, 1, 1)
)
dpTrafficSegForwardDomainEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dpTrafficSegForwardDomainEntry.setStatus("current")
_DpTrafficSegForwardPorts_Type = PortList
_DpTrafficSegForwardPorts_Object = MibTableColumn
dpTrafficSegForwardPorts = _DpTrafficSegForwardPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 25, 1, 1, 1, 1),
    _DpTrafficSegForwardPorts_Type()
)
dpTrafficSegForwardPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpTrafficSegForwardPorts.setStatus("current")
_DpTrafficSegConformance_ObjectIdentity = ObjectIdentity
dpTrafficSegConformance = _DpTrafficSegConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 25, 2)
)
_DpTrafficSegMIBCompliances_ObjectIdentity = ObjectIdentity
dpTrafficSegMIBCompliances = _DpTrafficSegMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 25, 2, 1)
)
_DpTrafficSegMIBGroups_ObjectIdentity = ObjectIdentity
dpTrafficSegMIBGroups = _DpTrafficSegMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 25, 2, 2)
)

# Managed Objects groups

dpTrafficSegIfCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 25, 2, 2, 1)
)
dpTrafficSegIfCfgGroup.setObjects(
    ("DLINKPRIME-TRAFFIC-SEGMENT-MIB", "dpTrafficSegForwardPorts")
)
if mibBuilder.loadTexts:
    dpTrafficSegIfCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dpTrafficSegMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 15, 25, 2, 1, 1)
)
dpTrafficSegMIBCompliance.setObjects(
    ("DLINKPRIME-TRAFFIC-SEGMENT-MIB", "dpTrafficSegIfCfgGroup")
)
if mibBuilder.loadTexts:
    dpTrafficSegMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-TRAFFIC-SEGMENT-MIB",
    **{"dlinkPrimeTrafficSegMIB": dlinkPrimeTrafficSegMIB,
       "dpTrafficSegNotifications": dpTrafficSegNotifications,
       "dpTrafficSegObjects": dpTrafficSegObjects,
       "dpTrafficSegForwardDomainTable": dpTrafficSegForwardDomainTable,
       "dpTrafficSegForwardDomainEntry": dpTrafficSegForwardDomainEntry,
       "dpTrafficSegForwardPorts": dpTrafficSegForwardPorts,
       "dpTrafficSegConformance": dpTrafficSegConformance,
       "dpTrafficSegMIBCompliances": dpTrafficSegMIBCompliances,
       "dpTrafficSegMIBCompliance": dpTrafficSegMIBCompliance,
       "dpTrafficSegMIBGroups": dpTrafficSegMIBGroups,
       "dpTrafficSegIfCfgGroup": dpTrafficSegIfCfgGroup}
)
