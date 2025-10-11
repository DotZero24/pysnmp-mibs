# SNMP MIB module (DES7200-PROCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DES7200-PROCESS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:48:46 2025
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

(myMgmt,) = mibBuilder.importSymbols(
    "DES7200-SMI",
    "myMgmt")

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


# MODULE-IDENTITY

myProcessMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36)
)
if mibBuilder.loadTexts:
    myProcessMIB.setRevisions(
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

_MyCPUMIBObjects_ObjectIdentity = ObjectIdentity
myCPUMIBObjects = _MyCPUMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1)
)
_MyCpuGeneralMibsGroup_ObjectIdentity = ObjectIdentity
myCpuGeneralMibsGroup = _MyCpuGeneralMibsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 1)
)
_MyCPUUtilization5Sec_Type = Percent
_MyCPUUtilization5Sec_Object = MibScalar
myCPUUtilization5Sec = _MyCPUUtilization5Sec_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 1, 1),
    _MyCPUUtilization5Sec_Type()
)
myCPUUtilization5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myCPUUtilization5Sec.setStatus("current")
_MyCPUUtilization1Min_Type = Percent
_MyCPUUtilization1Min_Object = MibScalar
myCPUUtilization1Min = _MyCPUUtilization1Min_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 1, 2),
    _MyCPUUtilization1Min_Type()
)
myCPUUtilization1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myCPUUtilization1Min.setStatus("current")
_MyCPUUtilization5Min_Type = Percent
_MyCPUUtilization5Min_Object = MibScalar
myCPUUtilization5Min = _MyCPUUtilization5Min_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 1, 3),
    _MyCPUUtilization5Min_Type()
)
myCPUUtilization5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myCPUUtilization5Min.setStatus("current")
_MyCPUUtilizationWarning_Type = Percent
_MyCPUUtilizationWarning_Object = MibScalar
myCPUUtilizationWarning = _MyCPUUtilizationWarning_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 1, 4),
    _MyCPUUtilizationWarning_Type()
)
myCPUUtilizationWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myCPUUtilizationWarning.setStatus("current")
_MyCPUUtilizationCritical_Type = Percent
_MyCPUUtilizationCritical_Object = MibScalar
myCPUUtilizationCritical = _MyCPUUtilizationCritical_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 1, 5),
    _MyCPUUtilizationCritical_Type()
)
myCPUUtilizationCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myCPUUtilizationCritical.setStatus("current")
_MyNodeCPUTotalTable_Object = MibTable
myNodeCPUTotalTable = _MyNodeCPUTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2)
)
if mibBuilder.loadTexts:
    myNodeCPUTotalTable.setStatus("current")
_MyNodeCPUTotalEntry_Object = MibTableRow
myNodeCPUTotalEntry = _MyNodeCPUTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1)
)
myNodeCPUTotalEntry.setIndexNames(
    (0, "DES7200-PROCESS-MIB", "myNodeCPUTotalIndex"),
)
if mibBuilder.loadTexts:
    myNodeCPUTotalEntry.setStatus("current")
_MyNodeCPUTotalIndex_Type = Integer32
_MyNodeCPUTotalIndex_Object = MibTableColumn
myNodeCPUTotalIndex = _MyNodeCPUTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 1),
    _MyNodeCPUTotalIndex_Type()
)
myNodeCPUTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myNodeCPUTotalIndex.setStatus("current")
_MyNodeCPUTotalName_Type = DisplayString
_MyNodeCPUTotalName_Object = MibTableColumn
myNodeCPUTotalName = _MyNodeCPUTotalName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 2),
    _MyNodeCPUTotalName_Type()
)
myNodeCPUTotalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myNodeCPUTotalName.setStatus("current")
_MyNodeCPUTotal5sec_Type = Percent
_MyNodeCPUTotal5sec_Object = MibTableColumn
myNodeCPUTotal5sec = _MyNodeCPUTotal5sec_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 3),
    _MyNodeCPUTotal5sec_Type()
)
myNodeCPUTotal5sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myNodeCPUTotal5sec.setStatus("current")
_MyNodeCPUTotal1min_Type = Percent
_MyNodeCPUTotal1min_Object = MibTableColumn
myNodeCPUTotal1min = _MyNodeCPUTotal1min_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 4),
    _MyNodeCPUTotal1min_Type()
)
myNodeCPUTotal1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myNodeCPUTotal1min.setStatus("current")
_MyNodeCPUTotal5min_Type = Percent
_MyNodeCPUTotal5min_Object = MibTableColumn
myNodeCPUTotal5min = _MyNodeCPUTotal5min_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 5),
    _MyNodeCPUTotal5min_Type()
)
myNodeCPUTotal5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myNodeCPUTotal5min.setStatus("current")
_MyNodeCPUTotalWarning_Type = Percent
_MyNodeCPUTotalWarning_Object = MibTableColumn
myNodeCPUTotalWarning = _MyNodeCPUTotalWarning_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 6),
    _MyNodeCPUTotalWarning_Type()
)
myNodeCPUTotalWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myNodeCPUTotalWarning.setStatus("current")
_MyNodeCPUTotalCritical_Type = Percent
_MyNodeCPUTotalCritical_Object = MibTableColumn
myNodeCPUTotalCritical = _MyNodeCPUTotalCritical_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 7),
    _MyNodeCPUTotalCritical_Type()
)
myNodeCPUTotalCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myNodeCPUTotalCritical.setStatus("current")
_MyProcessMIBConformance_ObjectIdentity = ObjectIdentity
myProcessMIBConformance = _MyProcessMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 2)
)
_MyProcessMIBCompliances_ObjectIdentity = ObjectIdentity
myProcessMIBCompliances = _MyProcessMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 2, 1)
)
_MyProcessMIBGroups_ObjectIdentity = ObjectIdentity
myProcessMIBGroups = _MyProcessMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 2, 2)
)

# Managed Objects groups

myCPUUtilizationMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 2, 2, 1)
)
myCPUUtilizationMIBGroup.setObjects(
      *(("DES7200-PROCESS-MIB", "myCPUUtilization5Sec"),
        ("DES7200-PROCESS-MIB", "myCPUUtilization1Min"),
        ("DES7200-PROCESS-MIB", "myCPUUtilization5Min"))
)
if mibBuilder.loadTexts:
    myCPUUtilizationMIBGroup.setStatus("current")

myNodeCPUTotalGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 2, 2, 2)
)
myNodeCPUTotalGroups.setObjects(
      *(("DES7200-PROCESS-MIB", "myNodeCPUTotalIndex"),
        ("DES7200-PROCESS-MIB", "myNodeCPUTotalName"),
        ("DES7200-PROCESS-MIB", "myNodeCPUTotal5sec"),
        ("DES7200-PROCESS-MIB", "myNodeCPUTotal1min"),
        ("DES7200-PROCESS-MIB", "myNodeCPUTotal5min"),
        ("DES7200-PROCESS-MIB", "myNodeCPUTotalWarning"),
        ("DES7200-PROCESS-MIB", "myNodeCPUTotalCritical"))
)
if mibBuilder.loadTexts:
    myNodeCPUTotalGroups.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myProcessMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 2, 1, 1)
)
myProcessMIBCompliance.setObjects(
    ("DES7200-PROCESS-MIB", "myCPUUtilizationMIBGroup")
)
if mibBuilder.loadTexts:
    myProcessMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DES7200-PROCESS-MIB",
    **{"Percent": Percent,
       "myProcessMIB": myProcessMIB,
       "myCPUMIBObjects": myCPUMIBObjects,
       "myCpuGeneralMibsGroup": myCpuGeneralMibsGroup,
       "myCPUUtilization5Sec": myCPUUtilization5Sec,
       "myCPUUtilization1Min": myCPUUtilization1Min,
       "myCPUUtilization5Min": myCPUUtilization5Min,
       "myCPUUtilizationWarning": myCPUUtilizationWarning,
       "myCPUUtilizationCritical": myCPUUtilizationCritical,
       "myNodeCPUTotalTable": myNodeCPUTotalTable,
       "myNodeCPUTotalEntry": myNodeCPUTotalEntry,
       "myNodeCPUTotalIndex": myNodeCPUTotalIndex,
       "myNodeCPUTotalName": myNodeCPUTotalName,
       "myNodeCPUTotal5sec": myNodeCPUTotal5sec,
       "myNodeCPUTotal1min": myNodeCPUTotal1min,
       "myNodeCPUTotal5min": myNodeCPUTotal5min,
       "myNodeCPUTotalWarning": myNodeCPUTotalWarning,
       "myNodeCPUTotalCritical": myNodeCPUTotalCritical,
       "myProcessMIBConformance": myProcessMIBConformance,
       "myProcessMIBCompliances": myProcessMIBCompliances,
       "myProcessMIBCompliance": myProcessMIBCompliance,
       "myProcessMIBGroups": myProcessMIBGroups,
       "myCPUUtilizationMIBGroup": myCPUUtilizationMIBGroup,
       "myNodeCPUTotalGroups": myNodeCPUTotalGroups}
)
