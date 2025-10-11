# SNMP MIB module (QTECH-PROCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-PROCESS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:01 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

qtechProcessMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36)
)
if mibBuilder.loadTexts:
    qtechProcessMIB.setRevisions(
        ("2003-10-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Percent(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



# MIB Managed Objects in the order of their OIDs

_QtechCPUMIBObjects_ObjectIdentity = ObjectIdentity
qtechCPUMIBObjects = _QtechCPUMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1)
)
_QtechCpuGeneralMibsGroup_ObjectIdentity = ObjectIdentity
qtechCpuGeneralMibsGroup = _QtechCpuGeneralMibsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 1)
)
_QtechCPUUtilization5Sec_Type = Percent
_QtechCPUUtilization5Sec_Object = MibScalar
qtechCPUUtilization5Sec = _QtechCPUUtilization5Sec_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 1, 1),
    _QtechCPUUtilization5Sec_Type()
)
qtechCPUUtilization5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCPUUtilization5Sec.setStatus("current")
_QtechCPUUtilization1Min_Type = Percent
_QtechCPUUtilization1Min_Object = MibScalar
qtechCPUUtilization1Min = _QtechCPUUtilization1Min_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 1, 2),
    _QtechCPUUtilization1Min_Type()
)
qtechCPUUtilization1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCPUUtilization1Min.setStatus("current")
_QtechCPUUtilization5Min_Type = Percent
_QtechCPUUtilization5Min_Object = MibScalar
qtechCPUUtilization5Min = _QtechCPUUtilization5Min_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 1, 3),
    _QtechCPUUtilization5Min_Type()
)
qtechCPUUtilization5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCPUUtilization5Min.setStatus("current")
_QtechCPUUtilizationWarning_Type = Percent
_QtechCPUUtilizationWarning_Object = MibScalar
qtechCPUUtilizationWarning = _QtechCPUUtilizationWarning_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 1, 4),
    _QtechCPUUtilizationWarning_Type()
)
qtechCPUUtilizationWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechCPUUtilizationWarning.setStatus("current")
_QtechCPUUtilizationCritical_Type = Percent
_QtechCPUUtilizationCritical_Object = MibScalar
qtechCPUUtilizationCritical = _QtechCPUUtilizationCritical_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 1, 5),
    _QtechCPUUtilizationCritical_Type()
)
qtechCPUUtilizationCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechCPUUtilizationCritical.setStatus("current")
_QtechCPUMaxUtilization5Sec_Type = Percent
_QtechCPUMaxUtilization5Sec_Object = MibScalar
qtechCPUMaxUtilization5Sec = _QtechCPUMaxUtilization5Sec_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 1, 6),
    _QtechCPUMaxUtilization5Sec_Type()
)
qtechCPUMaxUtilization5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCPUMaxUtilization5Sec.setStatus("current")
_QtechCPUMaxUtilization1Min_Type = Percent
_QtechCPUMaxUtilization1Min_Object = MibScalar
qtechCPUMaxUtilization1Min = _QtechCPUMaxUtilization1Min_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 1, 7),
    _QtechCPUMaxUtilization1Min_Type()
)
qtechCPUMaxUtilization1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCPUMaxUtilization1Min.setStatus("current")
_QtechCPUMaxUtilization5Min_Type = Percent
_QtechCPUMaxUtilization5Min_Object = MibScalar
qtechCPUMaxUtilization5Min = _QtechCPUMaxUtilization5Min_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 1, 8),
    _QtechCPUMaxUtilization5Min_Type()
)
qtechCPUMaxUtilization5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCPUMaxUtilization5Min.setStatus("current")
_QtechCPUUtilizationCollectSwitch_Type = Integer32
_QtechCPUUtilizationCollectSwitch_Object = MibScalar
qtechCPUUtilizationCollectSwitch = _QtechCPUUtilizationCollectSwitch_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 1, 9),
    _QtechCPUUtilizationCollectSwitch_Type()
)
qtechCPUUtilizationCollectSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechCPUUtilizationCollectSwitch.setStatus("current")
_QtechCPUUtilizationCurrent_Type = Percent
_QtechCPUUtilizationCurrent_Object = MibScalar
qtechCPUUtilizationCurrent = _QtechCPUUtilizationCurrent_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 1, 10),
    _QtechCPUUtilizationCurrent_Type()
)
qtechCPUUtilizationCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCPUUtilizationCurrent.setStatus("current")
_QtechNodeCPUTotalTable_Object = MibTable
qtechNodeCPUTotalTable = _QtechNodeCPUTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 2)
)
if mibBuilder.loadTexts:
    qtechNodeCPUTotalTable.setStatus("current")
_QtechNodeCPUTotalEntry_Object = MibTableRow
qtechNodeCPUTotalEntry = _QtechNodeCPUTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 2, 1)
)
qtechNodeCPUTotalEntry.setIndexNames(
    (0, "QTECH-PROCESS-MIB", "qtechNodeCPUTotalIndex"),
)
if mibBuilder.loadTexts:
    qtechNodeCPUTotalEntry.setStatus("current")
_QtechNodeCPUTotalIndex_Type = Integer32
_QtechNodeCPUTotalIndex_Object = MibTableColumn
qtechNodeCPUTotalIndex = _QtechNodeCPUTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 2, 1, 1),
    _QtechNodeCPUTotalIndex_Type()
)
qtechNodeCPUTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechNodeCPUTotalIndex.setStatus("current")
_QtechNodeCPUTotalName_Type = DisplayString
_QtechNodeCPUTotalName_Object = MibTableColumn
qtechNodeCPUTotalName = _QtechNodeCPUTotalName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 2, 1, 2),
    _QtechNodeCPUTotalName_Type()
)
qtechNodeCPUTotalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechNodeCPUTotalName.setStatus("current")
_QtechNodeCPUTotal5sec_Type = Percent
_QtechNodeCPUTotal5sec_Object = MibTableColumn
qtechNodeCPUTotal5sec = _QtechNodeCPUTotal5sec_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 2, 1, 3),
    _QtechNodeCPUTotal5sec_Type()
)
qtechNodeCPUTotal5sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechNodeCPUTotal5sec.setStatus("current")
_QtechNodeCPUTotal1min_Type = Percent
_QtechNodeCPUTotal1min_Object = MibTableColumn
qtechNodeCPUTotal1min = _QtechNodeCPUTotal1min_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 2, 1, 4),
    _QtechNodeCPUTotal1min_Type()
)
qtechNodeCPUTotal1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechNodeCPUTotal1min.setStatus("current")
_QtechNodeCPUTotal5min_Type = Percent
_QtechNodeCPUTotal5min_Object = MibTableColumn
qtechNodeCPUTotal5min = _QtechNodeCPUTotal5min_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 2, 1, 5),
    _QtechNodeCPUTotal5min_Type()
)
qtechNodeCPUTotal5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechNodeCPUTotal5min.setStatus("current")
_QtechNodeCPUTotalWarning_Type = Percent
_QtechNodeCPUTotalWarning_Object = MibTableColumn
qtechNodeCPUTotalWarning = _QtechNodeCPUTotalWarning_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 2, 1, 6),
    _QtechNodeCPUTotalWarning_Type()
)
qtechNodeCPUTotalWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNodeCPUTotalWarning.setStatus("current")
_QtechNodeCPUTotalCritical_Type = Percent
_QtechNodeCPUTotalCritical_Object = MibTableColumn
qtechNodeCPUTotalCritical = _QtechNodeCPUTotalCritical_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 2, 1, 7),
    _QtechNodeCPUTotalCritical_Type()
)
qtechNodeCPUTotalCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNodeCPUTotalCritical.setStatus("current")
_QtechLankApCPUTotalTable_Object = MibTable
qtechLankApCPUTotalTable = _QtechLankApCPUTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 3)
)
if mibBuilder.loadTexts:
    qtechLankApCPUTotalTable.setStatus("current")
_QtechLankApCPUTotalEntry_Object = MibTableRow
qtechLankApCPUTotalEntry = _QtechLankApCPUTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 3, 1)
)
qtechLankApCPUTotalEntry.setIndexNames(
    (0, "QTECH-PROCESS-MIB", "qtechLankApCPUMacAddr"),
)
if mibBuilder.loadTexts:
    qtechLankApCPUTotalEntry.setStatus("current")
_QtechLankApCPUMacAddr_Type = MacAddress
_QtechLankApCPUMacAddr_Object = MibTableColumn
qtechLankApCPUMacAddr = _QtechLankApCPUMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 3, 1, 1),
    _QtechLankApCPUMacAddr_Type()
)
qtechLankApCPUMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLankApCPUMacAddr.setStatus("current")
_QtechLankApCPUUtilizationCollectSwitch_Type = Integer32
_QtechLankApCPUUtilizationCollectSwitch_Object = MibTableColumn
qtechLankApCPUUtilizationCollectSwitch = _QtechLankApCPUUtilizationCollectSwitch_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 3, 1, 2),
    _QtechLankApCPUUtilizationCollectSwitch_Type()
)
qtechLankApCPUUtilizationCollectSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLankApCPUUtilizationCollectSwitch.setStatus("current")
_QtechLankApCPUUtilizationWarning_Type = Percent
_QtechLankApCPUUtilizationWarning_Object = MibTableColumn
qtechLankApCPUUtilizationWarning = _QtechLankApCPUUtilizationWarning_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 3, 1, 3),
    _QtechLankApCPUUtilizationWarning_Type()
)
qtechLankApCPUUtilizationWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLankApCPUUtilizationWarning.setStatus("current")
_QtechLankApCPUUtilizationCritical_Type = Percent
_QtechLankApCPUUtilizationCritical_Object = MibTableColumn
qtechLankApCPUUtilizationCritical = _QtechLankApCPUUtilizationCritical_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 3, 1, 4),
    _QtechLankApCPUUtilizationCritical_Type()
)
qtechLankApCPUUtilizationCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLankApCPUUtilizationCritical.setStatus("current")
_QtechLankApCPUUtilizationCurrent_Type = Percent
_QtechLankApCPUUtilizationCurrent_Object = MibTableColumn
qtechLankApCPUUtilizationCurrent = _QtechLankApCPUUtilizationCurrent_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 3, 1, 5),
    _QtechLankApCPUUtilizationCurrent_Type()
)
qtechLankApCPUUtilizationCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLankApCPUUtilizationCurrent.setStatus("current")
_QtechLankApCPUUtilization5Min_Type = Percent
_QtechLankApCPUUtilization5Min_Object = MibTableColumn
qtechLankApCPUUtilization5Min = _QtechLankApCPUUtilization5Min_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 1, 3, 1, 6),
    _QtechLankApCPUUtilization5Min_Type()
)
qtechLankApCPUUtilization5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLankApCPUUtilization5Min.setStatus("current")
_QtechProcessMIBConformance_ObjectIdentity = ObjectIdentity
qtechProcessMIBConformance = _QtechProcessMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 2)
)
_QtechProcessMIBCompliances_ObjectIdentity = ObjectIdentity
qtechProcessMIBCompliances = _QtechProcessMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 2, 1)
)
_QtechProcessMIBGroups_ObjectIdentity = ObjectIdentity
qtechProcessMIBGroups = _QtechProcessMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 2, 2)
)

# Managed Objects groups

qtechCPUUtilizationMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 2, 2, 1)
)
qtechCPUUtilizationMIBGroup.setObjects(
      *(("QTECH-PROCESS-MIB", "qtechCPUUtilization5Sec"),
        ("QTECH-PROCESS-MIB", "qtechCPUUtilization1Min"),
        ("QTECH-PROCESS-MIB", "qtechCPUUtilization5Min"),
        ("QTECH-PROCESS-MIB", "qtechCPUMaxUtilization5Sec"),
        ("QTECH-PROCESS-MIB", "qtechCPUMaxUtilization1Min"),
        ("QTECH-PROCESS-MIB", "qtechCPUMaxUtilization5Min"),
        ("QTECH-PROCESS-MIB", "qtechCPUUtilizationCollectSwitch"),
        ("QTECH-PROCESS-MIB", "qtechCPUUtilizationCurrent"))
)
if mibBuilder.loadTexts:
    qtechCPUUtilizationMIBGroup.setStatus("current")

qtechNodeCPUTotalGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 2, 2, 2)
)
qtechNodeCPUTotalGroups.setObjects(
      *(("QTECH-PROCESS-MIB", "qtechNodeCPUTotalIndex"),
        ("QTECH-PROCESS-MIB", "qtechNodeCPUTotalName"),
        ("QTECH-PROCESS-MIB", "qtechNodeCPUTotal5sec"),
        ("QTECH-PROCESS-MIB", "qtechNodeCPUTotal1min"),
        ("QTECH-PROCESS-MIB", "qtechNodeCPUTotal5min"),
        ("QTECH-PROCESS-MIB", "qtechNodeCPUTotalWarning"),
        ("QTECH-PROCESS-MIB", "qtechNodeCPUTotalCritical"))
)
if mibBuilder.loadTexts:
    qtechNodeCPUTotalGroups.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechProcessMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 36, 2, 1, 1)
)
qtechProcessMIBCompliance.setObjects(
    ("QTECH-PROCESS-MIB", "qtechCPUUtilizationMIBGroup")
)
if mibBuilder.loadTexts:
    qtechProcessMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-PROCESS-MIB",
    **{"Percent": Percent,
       "qtechProcessMIB": qtechProcessMIB,
       "qtechCPUMIBObjects": qtechCPUMIBObjects,
       "qtechCpuGeneralMibsGroup": qtechCpuGeneralMibsGroup,
       "qtechCPUUtilization5Sec": qtechCPUUtilization5Sec,
       "qtechCPUUtilization1Min": qtechCPUUtilization1Min,
       "qtechCPUUtilization5Min": qtechCPUUtilization5Min,
       "qtechCPUUtilizationWarning": qtechCPUUtilizationWarning,
       "qtechCPUUtilizationCritical": qtechCPUUtilizationCritical,
       "qtechCPUMaxUtilization5Sec": qtechCPUMaxUtilization5Sec,
       "qtechCPUMaxUtilization1Min": qtechCPUMaxUtilization1Min,
       "qtechCPUMaxUtilization5Min": qtechCPUMaxUtilization5Min,
       "qtechCPUUtilizationCollectSwitch": qtechCPUUtilizationCollectSwitch,
       "qtechCPUUtilizationCurrent": qtechCPUUtilizationCurrent,
       "qtechNodeCPUTotalTable": qtechNodeCPUTotalTable,
       "qtechNodeCPUTotalEntry": qtechNodeCPUTotalEntry,
       "qtechNodeCPUTotalIndex": qtechNodeCPUTotalIndex,
       "qtechNodeCPUTotalName": qtechNodeCPUTotalName,
       "qtechNodeCPUTotal5sec": qtechNodeCPUTotal5sec,
       "qtechNodeCPUTotal1min": qtechNodeCPUTotal1min,
       "qtechNodeCPUTotal5min": qtechNodeCPUTotal5min,
       "qtechNodeCPUTotalWarning": qtechNodeCPUTotalWarning,
       "qtechNodeCPUTotalCritical": qtechNodeCPUTotalCritical,
       "qtechLankApCPUTotalTable": qtechLankApCPUTotalTable,
       "qtechLankApCPUTotalEntry": qtechLankApCPUTotalEntry,
       "qtechLankApCPUMacAddr": qtechLankApCPUMacAddr,
       "qtechLankApCPUUtilizationCollectSwitch": qtechLankApCPUUtilizationCollectSwitch,
       "qtechLankApCPUUtilizationWarning": qtechLankApCPUUtilizationWarning,
       "qtechLankApCPUUtilizationCritical": qtechLankApCPUUtilizationCritical,
       "qtechLankApCPUUtilizationCurrent": qtechLankApCPUUtilizationCurrent,
       "qtechLankApCPUUtilization5Min": qtechLankApCPUUtilization5Min,
       "qtechProcessMIBConformance": qtechProcessMIBConformance,
       "qtechProcessMIBCompliances": qtechProcessMIBCompliances,
       "qtechProcessMIBCompliance": qtechProcessMIBCompliance,
       "qtechProcessMIBGroups": qtechProcessMIBGroups,
       "qtechCPUUtilizationMIBGroup": qtechCPUUtilizationMIBGroup,
       "qtechNodeCPUTotalGroups": qtechNodeCPUTotalGroups}
)
