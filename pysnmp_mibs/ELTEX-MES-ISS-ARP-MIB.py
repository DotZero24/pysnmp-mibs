# SNMP MIB module (ELTEX-MES-ISS-ARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-ARP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:48:50 2025
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

(eltMesIss,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-MIB",
    "eltMesIss")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltMesIssArpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 26)
)
if mibBuilder.loadTexts:
    eltMesIssArpMIB.setRevisions(
        ("1970-01-01 00:00",
         "2021-03-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesIssArpObjects_ObjectIdentity = ObjectIdentity
eltMesIssArpObjects = _EltMesIssArpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 26, 1)
)
_EltMesIssArpInterfaceConfigs_ObjectIdentity = ObjectIdentity
eltMesIssArpInterfaceConfigs = _EltMesIssArpInterfaceConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 26, 1, 1)
)
_EltMesIssArpInterfaceTable_Object = MibTable
eltMesIssArpInterfaceTable = _EltMesIssArpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 26, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eltMesIssArpInterfaceTable.setStatus("current")
_EltMesIssArpInterfaceEntry_Object = MibTableRow
eltMesIssArpInterfaceEntry = _EltMesIssArpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 26, 1, 1, 1, 1)
)
eltMesIssArpInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltMesIssArpInterfaceEntry.setStatus("current")


class _EltMesIssArpGratuitousPeriodicEnable_Type(TruthValue):
    """Custom type eltMesIssArpGratuitousPeriodicEnable based on TruthValue"""
    defaultValue = 1


_EltMesIssArpGratuitousPeriodicEnable_Type.__name__ = "TruthValue"
_EltMesIssArpGratuitousPeriodicEnable_Object = MibTableColumn
eltMesIssArpGratuitousPeriodicEnable = _EltMesIssArpGratuitousPeriodicEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 26, 1, 1, 1, 1, 1),
    _EltMesIssArpGratuitousPeriodicEnable_Type()
)
eltMesIssArpGratuitousPeriodicEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssArpGratuitousPeriodicEnable.setStatus("current")
_EltMesIssArpGlobals_ObjectIdentity = ObjectIdentity
eltMesIssArpGlobals = _EltMesIssArpGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 26, 1, 2)
)


class _EltMesIssArpGratuitousInterval_Type(Integer32):
    """Custom type eltMesIssArpGratuitousInterval based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 86400),
    )


_EltMesIssArpGratuitousInterval_Type.__name__ = "Integer32"
_EltMesIssArpGratuitousInterval_Object = MibScalar
eltMesIssArpGratuitousInterval = _EltMesIssArpGratuitousInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 26, 1, 2, 1),
    _EltMesIssArpGratuitousInterval_Type()
)
eltMesIssArpGratuitousInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssArpGratuitousInterval.setStatus("current")
_EltMesIssArpInspection_ObjectIdentity = ObjectIdentity
eltMesIssArpInspection = _EltMesIssArpInspection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 26, 1, 3)
)
_EltMesIssArpInspectionStats_ObjectIdentity = ObjectIdentity
eltMesIssArpInspectionStats = _EltMesIssArpInspectionStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 26, 1, 3, 1)
)
_EltMesIssArpInspectionIfStatsTable_Object = MibTable
eltMesIssArpInspectionIfStatsTable = _EltMesIssArpInspectionIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 26, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    eltMesIssArpInspectionIfStatsTable.setStatus("current")
_EltMesIssArpInspectionIfStatsEntry_Object = MibTableRow
eltMesIssArpInspectionIfStatsEntry = _EltMesIssArpInspectionIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 26, 1, 3, 1, 1, 1)
)
eltMesIssArpInspectionIfStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltMesIssArpInspectionIfStatsEntry.setStatus("current")
_EltMesIssArpInspectionIfForwardedPackets_Type = Integer32
_EltMesIssArpInspectionIfForwardedPackets_Object = MibTableColumn
eltMesIssArpInspectionIfForwardedPackets = _EltMesIssArpInspectionIfForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 26, 1, 3, 1, 1, 1, 1),
    _EltMesIssArpInspectionIfForwardedPackets_Type()
)
eltMesIssArpInspectionIfForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssArpInspectionIfForwardedPackets.setStatus("current")
_EltMesIssArpInspectionIfDroppedPackets_Type = Integer32
_EltMesIssArpInspectionIfDroppedPackets_Object = MibTableColumn
eltMesIssArpInspectionIfDroppedPackets = _EltMesIssArpInspectionIfDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 26, 1, 3, 1, 1, 1, 2),
    _EltMesIssArpInspectionIfDroppedPackets_Type()
)
eltMesIssArpInspectionIfDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssArpInspectionIfDroppedPackets.setStatus("current")
_EltMesIssArpInspectionIfIPValidFailures_Type = Integer32
_EltMesIssArpInspectionIfIPValidFailures_Object = MibTableColumn
eltMesIssArpInspectionIfIPValidFailures = _EltMesIssArpInspectionIfIPValidFailures_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 26, 1, 3, 1, 1, 1, 3),
    _EltMesIssArpInspectionIfIPValidFailures_Type()
)
eltMesIssArpInspectionIfIPValidFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssArpInspectionIfIPValidFailures.setStatus("current")
_EltMesIssArpInspectionIfDestMacFailures_Type = Integer32
_EltMesIssArpInspectionIfDestMacFailures_Object = MibTableColumn
eltMesIssArpInspectionIfDestMacFailures = _EltMesIssArpInspectionIfDestMacFailures_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 26, 1, 3, 1, 1, 1, 4),
    _EltMesIssArpInspectionIfDestMacFailures_Type()
)
eltMesIssArpInspectionIfDestMacFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssArpInspectionIfDestMacFailures.setStatus("current")
_EltMesIssArpInspectionIfSrcMacFailures_Type = Integer32
_EltMesIssArpInspectionIfSrcMacFailures_Object = MibTableColumn
eltMesIssArpInspectionIfSrcMacFailures = _EltMesIssArpInspectionIfSrcMacFailures_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 26, 1, 3, 1, 1, 1, 5),
    _EltMesIssArpInspectionIfSrcMacFailures_Type()
)
eltMesIssArpInspectionIfSrcMacFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssArpInspectionIfSrcMacFailures.setStatus("current")


class _EltMesIssArpInsectionIfStatsClear_Type(TruthValue):
    """Custom type eltMesIssArpInsectionIfStatsClear based on TruthValue"""
    defaultValue = 2


_EltMesIssArpInsectionIfStatsClear_Type.__name__ = "TruthValue"
_EltMesIssArpInsectionIfStatsClear_Object = MibTableColumn
eltMesIssArpInsectionIfStatsClear = _EltMesIssArpInsectionIfStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 26, 1, 3, 1, 1, 1, 6),
    _EltMesIssArpInsectionIfStatsClear_Type()
)
eltMesIssArpInsectionIfStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssArpInsectionIfStatsClear.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-ARP-MIB",
    **{"eltMesIssArpMIB": eltMesIssArpMIB,
       "eltMesIssArpObjects": eltMesIssArpObjects,
       "eltMesIssArpInterfaceConfigs": eltMesIssArpInterfaceConfigs,
       "eltMesIssArpInterfaceTable": eltMesIssArpInterfaceTable,
       "eltMesIssArpInterfaceEntry": eltMesIssArpInterfaceEntry,
       "eltMesIssArpGratuitousPeriodicEnable": eltMesIssArpGratuitousPeriodicEnable,
       "eltMesIssArpGlobals": eltMesIssArpGlobals,
       "eltMesIssArpGratuitousInterval": eltMesIssArpGratuitousInterval,
       "eltMesIssArpInspection": eltMesIssArpInspection,
       "eltMesIssArpInspectionStats": eltMesIssArpInspectionStats,
       "eltMesIssArpInspectionIfStatsTable": eltMesIssArpInspectionIfStatsTable,
       "eltMesIssArpInspectionIfStatsEntry": eltMesIssArpInspectionIfStatsEntry,
       "eltMesIssArpInspectionIfForwardedPackets": eltMesIssArpInspectionIfForwardedPackets,
       "eltMesIssArpInspectionIfDroppedPackets": eltMesIssArpInspectionIfDroppedPackets,
       "eltMesIssArpInspectionIfIPValidFailures": eltMesIssArpInspectionIfIPValidFailures,
       "eltMesIssArpInspectionIfDestMacFailures": eltMesIssArpInspectionIfDestMacFailures,
       "eltMesIssArpInspectionIfSrcMacFailures": eltMesIssArpInspectionIfSrcMacFailures,
       "eltMesIssArpInsectionIfStatsClear": eltMesIssArpInsectionIfStatsClear}
)
