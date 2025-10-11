# SNMP MIB module (IPI-TCAM-UTILIZATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ipinfusion/IPI-TCAM-UTILIZATION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:34:15 2025
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

(ipi,) = mibBuilder.importSymbols(
    "OCNOS-IPI-MODULE-MIB",
    "ipi")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ipiTCAMutilization = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 108)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CodeType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "x"


class UnitType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "x"


# MIB Managed Objects in the order of their OIDs

_TCAMUtilizationObjects_ObjectIdentity = ObjectIdentity
TCAMUtilizationObjects = _TCAMUtilizationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 108, 1)
)
_IngressTCAMUtilizationTable_Object = MibTable
ingressTCAMUtilizationTable = _IngressTCAMUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 108, 1, 1)
)
if mibBuilder.loadTexts:
    ingressTCAMUtilizationTable.setStatus("current")
_IngressTCAMUtilizationEntry_Object = MibTableRow
ingressTCAMUtilizationEntry = _IngressTCAMUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 108, 1, 1, 1)
)
ingressTCAMUtilizationEntry.setIndexNames(
    (0, "IPI-TCAM-UTILIZATION-MIB", "ingTCAMGroupName"),
)
if mibBuilder.loadTexts:
    ingressTCAMUtilizationEntry.setStatus("current")
_IngTCAMGroupName_Type = DisplayString
_IngTCAMGroupName_Object = MibTableColumn
ingTCAMGroupName = _IngTCAMGroupName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 108, 1, 1, 1, 1),
    _IngTCAMGroupName_Type()
)
ingTCAMGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingTCAMGroupName.setStatus("current")
_IngFreeTCAMEntries_Type = Integer
_IngFreeTCAMEntries_Object = MibTableColumn
ingFreeTCAMEntries = _IngFreeTCAMEntries_Object(
    (1, 3, 6, 1, 4, 1, 36673, 108, 1, 1, 1, 2),
    _IngFreeTCAMEntries_Type()
)
ingFreeTCAMEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingFreeTCAMEntries.setStatus("current")
_IngUsedTCAMPercent_Type = Integer
_IngUsedTCAMPercent_Object = MibTableColumn
ingUsedTCAMPercent = _IngUsedTCAMPercent_Object(
    (1, 3, 6, 1, 4, 1, 36673, 108, 1, 1, 1, 3),
    _IngUsedTCAMPercent_Type()
)
ingUsedTCAMPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingUsedTCAMPercent.setStatus("current")
_IngUsedTCAMEntries_Type = Integer
_IngUsedTCAMEntries_Object = MibTableColumn
ingUsedTCAMEntries = _IngUsedTCAMEntries_Object(
    (1, 3, 6, 1, 4, 1, 36673, 108, 1, 1, 1, 4),
    _IngUsedTCAMEntries_Type()
)
ingUsedTCAMEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingUsedTCAMEntries.setStatus("current")
_IngTotalTCAMEntries_Type = Integer
_IngTotalTCAMEntries_Object = MibTableColumn
ingTotalTCAMEntries = _IngTotalTCAMEntries_Object(
    (1, 3, 6, 1, 4, 1, 36673, 108, 1, 1, 1, 5),
    _IngTotalTCAMEntries_Type()
)
ingTotalTCAMEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingTotalTCAMEntries.setStatus("current")
_IngDedicatedTCAMEntries_Type = Integer
_IngDedicatedTCAMEntries_Object = MibTableColumn
ingDedicatedTCAMEntries = _IngDedicatedTCAMEntries_Object(
    (1, 3, 6, 1, 4, 1, 36673, 108, 1, 1, 1, 6),
    _IngDedicatedTCAMEntries_Type()
)
ingDedicatedTCAMEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingDedicatedTCAMEntries.setStatus("current")
_IngSharedTCAMEntries_Type = Integer
_IngSharedTCAMEntries_Object = MibTableColumn
ingSharedTCAMEntries = _IngSharedTCAMEntries_Object(
    (1, 3, 6, 1, 4, 1, 36673, 108, 1, 1, 1, 7),
    _IngSharedTCAMEntries_Type()
)
ingSharedTCAMEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingSharedTCAMEntries.setStatus("current")
_EgressTCAMUtilizationTable_Object = MibTable
egressTCAMUtilizationTable = _EgressTCAMUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 108, 1, 2)
)
if mibBuilder.loadTexts:
    egressTCAMUtilizationTable.setStatus("current")
_EgressTCAMUtilizationEntry_Object = MibTableRow
egressTCAMUtilizationEntry = _EgressTCAMUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 108, 1, 2, 1)
)
egressTCAMUtilizationEntry.setIndexNames(
    (0, "IPI-TCAM-UTILIZATION-MIB", "egrTCAMGroupName"),
)
if mibBuilder.loadTexts:
    egressTCAMUtilizationEntry.setStatus("current")
_EgrTCAMGroupName_Type = DisplayString
_EgrTCAMGroupName_Object = MibTableColumn
egrTCAMGroupName = _EgrTCAMGroupName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 108, 1, 2, 1, 1),
    _EgrTCAMGroupName_Type()
)
egrTCAMGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egrTCAMGroupName.setStatus("current")
_EgrFreeTCAMEntries_Type = Integer
_EgrFreeTCAMEntries_Object = MibTableColumn
egrFreeTCAMEntries = _EgrFreeTCAMEntries_Object(
    (1, 3, 6, 1, 4, 1, 36673, 108, 1, 2, 1, 2),
    _EgrFreeTCAMEntries_Type()
)
egrFreeTCAMEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egrFreeTCAMEntries.setStatus("current")
_EgrUsedTCAMPercent_Type = Integer
_EgrUsedTCAMPercent_Object = MibTableColumn
egrUsedTCAMPercent = _EgrUsedTCAMPercent_Object(
    (1, 3, 6, 1, 4, 1, 36673, 108, 1, 2, 1, 3),
    _EgrUsedTCAMPercent_Type()
)
egrUsedTCAMPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egrUsedTCAMPercent.setStatus("current")
_EgrUsedTCAMEntries_Type = Integer
_EgrUsedTCAMEntries_Object = MibTableColumn
egrUsedTCAMEntries = _EgrUsedTCAMEntries_Object(
    (1, 3, 6, 1, 4, 1, 36673, 108, 1, 2, 1, 4),
    _EgrUsedTCAMEntries_Type()
)
egrUsedTCAMEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egrUsedTCAMEntries.setStatus("current")
_EgrTotalTCAMEntries_Type = Integer
_EgrTotalTCAMEntries_Object = MibTableColumn
egrTotalTCAMEntries = _EgrTotalTCAMEntries_Object(
    (1, 3, 6, 1, 4, 1, 36673, 108, 1, 2, 1, 5),
    _EgrTotalTCAMEntries_Type()
)
egrTotalTCAMEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egrTotalTCAMEntries.setStatus("current")
_EgrDedicatedTCAMEntries_Type = Integer
_EgrDedicatedTCAMEntries_Object = MibTableColumn
egrDedicatedTCAMEntries = _EgrDedicatedTCAMEntries_Object(
    (1, 3, 6, 1, 4, 1, 36673, 108, 1, 2, 1, 6),
    _EgrDedicatedTCAMEntries_Type()
)
egrDedicatedTCAMEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egrDedicatedTCAMEntries.setStatus("current")
_EgrSharedTCAMEntries_Type = Integer
_EgrSharedTCAMEntries_Object = MibTableColumn
egrSharedTCAMEntries = _EgrSharedTCAMEntries_Object(
    (1, 3, 6, 1, 4, 1, 36673, 108, 1, 2, 1, 7),
    _EgrSharedTCAMEntries_Type()
)
egrSharedTCAMEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egrSharedTCAMEntries.setStatus("current")
_TCAMWarningThresholdLevel_Type = Integer
_TCAMWarningThresholdLevel_Object = MibScalar
tCAMWarningThresholdLevel = _TCAMWarningThresholdLevel_Object(
    (1, 3, 6, 1, 4, 1, 36673, 108, 1, 3),
    _TCAMWarningThresholdLevel_Type()
)
tCAMWarningThresholdLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCAMWarningThresholdLevel.setStatus("current")
_TCAMAlertThresholdLevel_Type = Integer
_TCAMAlertThresholdLevel_Object = MibScalar
tCAMAlertThresholdLevel = _TCAMAlertThresholdLevel_Object(
    (1, 3, 6, 1, 4, 1, 36673, 108, 1, 4),
    _TCAMAlertThresholdLevel_Type()
)
tCAMAlertThresholdLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCAMAlertThresholdLevel.setStatus("current")
_TCAMUtilizationAlarmObjects_ObjectIdentity = ObjectIdentity
TCAMUtilizationAlarmObjects = _TCAMUtilizationAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 108, 2)
)
_TCAMUtilizationAlarmNotifications_ObjectIdentity = ObjectIdentity
TCAMUtilizationAlarmNotifications = _TCAMUtilizationAlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 108, 2, 1)
)

# Managed Objects groups


# Notification objects

ingTCAMWarningThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 108, 2, 1, 1)
)
ingTCAMWarningThresholdTrap.setObjects(
      *(("IPI-TCAM-UTILIZATION-MIB", "ingTCAMGroupName"),
        ("IPI-TCAM-UTILIZATION-MIB", "ingUsedTCAMPercent"),
        ("IPI-TCAM-UTILIZATION-MIB", "ingUsedTCAMEntries"))
)
if mibBuilder.loadTexts:
    ingTCAMWarningThresholdTrap.setStatus(
        "current"
    )

ingTCAMCriticalThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 108, 2, 1, 2)
)
ingTCAMCriticalThresholdTrap.setObjects(
      *(("IPI-TCAM-UTILIZATION-MIB", "ingTCAMGroupName"),
        ("IPI-TCAM-UTILIZATION-MIB", "ingUsedTCAMPercent"),
        ("IPI-TCAM-UTILIZATION-MIB", "ingUsedTCAMEntries"))
)
if mibBuilder.loadTexts:
    ingTCAMCriticalThresholdTrap.setStatus(
        "current"
    )

egrTCAMWarningThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 108, 2, 1, 3)
)
egrTCAMWarningThresholdTrap.setObjects(
      *(("IPI-TCAM-UTILIZATION-MIB", "egrTCAMGroupName"),
        ("IPI-TCAM-UTILIZATION-MIB", "egrUsedTCAMPercent"),
        ("IPI-TCAM-UTILIZATION-MIB", "egrUsedTCAMEntries"))
)
if mibBuilder.loadTexts:
    egrTCAMWarningThresholdTrap.setStatus(
        "current"
    )

egrTCAMCriticalThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 108, 2, 1, 4)
)
egrTCAMCriticalThresholdTrap.setObjects(
      *(("IPI-TCAM-UTILIZATION-MIB", "egrTCAMGroupName"),
        ("IPI-TCAM-UTILIZATION-MIB", "egrUsedTCAMPercent"),
        ("IPI-TCAM-UTILIZATION-MIB", "egrUsedTCAMEntries"))
)
if mibBuilder.loadTexts:
    egrTCAMCriticalThresholdTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPI-TCAM-UTILIZATION-MIB",
    **{"CodeType": CodeType,
       "UnitType": UnitType,
       "ipiTCAMutilization": ipiTCAMutilization,
       "TCAMUtilizationObjects": TCAMUtilizationObjects,
       "ingressTCAMUtilizationTable": ingressTCAMUtilizationTable,
       "ingressTCAMUtilizationEntry": ingressTCAMUtilizationEntry,
       "ingTCAMGroupName": ingTCAMGroupName,
       "ingFreeTCAMEntries": ingFreeTCAMEntries,
       "ingUsedTCAMPercent": ingUsedTCAMPercent,
       "ingUsedTCAMEntries": ingUsedTCAMEntries,
       "ingTotalTCAMEntries": ingTotalTCAMEntries,
       "ingDedicatedTCAMEntries": ingDedicatedTCAMEntries,
       "ingSharedTCAMEntries": ingSharedTCAMEntries,
       "egressTCAMUtilizationTable": egressTCAMUtilizationTable,
       "egressTCAMUtilizationEntry": egressTCAMUtilizationEntry,
       "egrTCAMGroupName": egrTCAMGroupName,
       "egrFreeTCAMEntries": egrFreeTCAMEntries,
       "egrUsedTCAMPercent": egrUsedTCAMPercent,
       "egrUsedTCAMEntries": egrUsedTCAMEntries,
       "egrTotalTCAMEntries": egrTotalTCAMEntries,
       "egrDedicatedTCAMEntries": egrDedicatedTCAMEntries,
       "egrSharedTCAMEntries": egrSharedTCAMEntries,
       "tCAMWarningThresholdLevel": tCAMWarningThresholdLevel,
       "tCAMAlertThresholdLevel": tCAMAlertThresholdLevel,
       "TCAMUtilizationAlarmObjects": TCAMUtilizationAlarmObjects,
       "TCAMUtilizationAlarmNotifications": TCAMUtilizationAlarmNotifications,
       "ingTCAMWarningThresholdTrap": ingTCAMWarningThresholdTrap,
       "ingTCAMCriticalThresholdTrap": ingTCAMCriticalThresholdTrap,
       "egrTCAMWarningThresholdTrap": egrTCAMWarningThresholdTrap,
       "egrTCAMCriticalThresholdTrap": egrTCAMCriticalThresholdTrap}
)
