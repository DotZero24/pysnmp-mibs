# SNMP MIB module (INFINERA-ENTITY-DSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-DSE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:57 2025
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

(entLPPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entLPPhysicalIndex")

(equipment,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "equipment")

(FloatTenths,
 InfnConvergenceStatus,
 InfnEqptType,
 InfnEqualizationCtrlLoop) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnConvergenceStatus",
    "InfnEqptType",
    "InfnEqualizationCtrlLoop")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

dseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DseTable_Object = MibTable
dseTable = _DseTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 1)
)
if mibBuilder.loadTexts:
    dseTable.setStatus("current")
_DseEntry_Object = MibTableRow
dseEntry = _DseEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 1, 1)
)
dseEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    dseEntry.setStatus("current")
_DseMoId_Type = DisplayString
_DseMoId_Object = MibTableColumn
dseMoId = _DseMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 1, 1, 1),
    _DseMoId_Type()
)
dseMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dseMoId.setStatus("current")
_DseProvEqptType_Type = InfnEqptType
_DseProvEqptType_Object = MibTableColumn
dseProvEqptType = _DseProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 1, 1, 2),
    _DseProvEqptType_Type()
)
dseProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dseProvEqptType.setStatus("current")
_DseSpectrumTiltOffset_Type = FloatTenths
_DseSpectrumTiltOffset_Object = MibTableColumn
dseSpectrumTiltOffset = _DseSpectrumTiltOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 1, 1, 3),
    _DseSpectrumTiltOffset_Type()
)
dseSpectrumTiltOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dseSpectrumTiltOffset.setStatus("current")
_DseEqualizationCtrlLoop_Type = InfnEqualizationCtrlLoop
_DseEqualizationCtrlLoop_Object = MibTableColumn
dseEqualizationCtrlLoop = _DseEqualizationCtrlLoop_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 1, 1, 4),
    _DseEqualizationCtrlLoop_Type()
)
dseEqualizationCtrlLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dseEqualizationCtrlLoop.setStatus("current")
_DseConvergenceStatus_Type = InfnConvergenceStatus
_DseConvergenceStatus_Object = MibTableColumn
dseConvergenceStatus = _DseConvergenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 1, 1, 5),
    _DseConvergenceStatus_Type()
)
dseConvergenceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dseConvergenceStatus.setStatus("current")
_DseRowStatus_Type = RowStatus
_DseRowStatus_Object = MibTableColumn
dseRowStatus = _DseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 1, 1, 6),
    _DseRowStatus_Type()
)
dseRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dseRowStatus.setStatus("current")
_DseCtrlLoopTimer_Type = Integer32
_DseCtrlLoopTimer_Object = MibTableColumn
dseCtrlLoopTimer = _DseCtrlLoopTimer_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 1, 1, 7),
    _DseCtrlLoopTimer_Type()
)
dseCtrlLoopTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dseCtrlLoopTimer.setStatus("current")
_DseConformance_ObjectIdentity = ObjectIdentity
dseConformance = _DseConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 3)
)
_DseCompliances_ObjectIdentity = ObjectIdentity
dseCompliances = _DseCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 3, 1)
)
_DseGroups_ObjectIdentity = ObjectIdentity
dseGroups = _DseGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 3, 2)
)

# Managed Objects groups

dseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 3, 2, 1)
)
dseGroup.setObjects(
      *(("INFINERA-ENTITY-DSE-MIB", "dseMoId"),
        ("INFINERA-ENTITY-DSE-MIB", "dseProvEqptType"),
        ("INFINERA-ENTITY-DSE-MIB", "dseSpectrumTiltOffset"),
        ("INFINERA-ENTITY-DSE-MIB", "dseEqualizationCtrlLoop"),
        ("INFINERA-ENTITY-DSE-MIB", "dseConvergenceStatus"),
        ("INFINERA-ENTITY-DSE-MIB", "dseRowStatus"),
        ("INFINERA-ENTITY-DSE-MIB", "dseCtrlLoopTimer"))
)
if mibBuilder.loadTexts:
    dseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dseCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 3, 1, 1)
)
dseCompliance.setObjects(
    ("INFINERA-ENTITY-DSE-MIB", "dseGroup")
)
if mibBuilder.loadTexts:
    dseCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-DSE-MIB",
    **{"dseMIB": dseMIB,
       "dseTable": dseTable,
       "dseEntry": dseEntry,
       "dseMoId": dseMoId,
       "dseProvEqptType": dseProvEqptType,
       "dseSpectrumTiltOffset": dseSpectrumTiltOffset,
       "dseEqualizationCtrlLoop": dseEqualizationCtrlLoop,
       "dseConvergenceStatus": dseConvergenceStatus,
       "dseRowStatus": dseRowStatus,
       "dseCtrlLoopTimer": dseCtrlLoopTimer,
       "dseConformance": dseConformance,
       "dseCompliances": dseCompliances,
       "dseCompliance": dseCompliance,
       "dseGroups": dseGroups,
       "dseGroup": dseGroup}
)
