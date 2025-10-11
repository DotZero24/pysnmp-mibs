# SNMP MIB module (INFINERA-ENTITY-RAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-RAM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:02 2025
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
 InfnEqptType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnEqptType")

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

ramMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RamTable_Object = MibTable
ramTable = _RamTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 12, 1)
)
if mibBuilder.loadTexts:
    ramTable.setStatus("current")
_RamEntry_Object = MibTableRow
ramEntry = _RamEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 12, 1, 1)
)
ramEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ramEntry.setStatus("current")
_RamMoId_Type = DisplayString
_RamMoId_Object = MibTableColumn
ramMoId = _RamMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 12, 1, 1, 1),
    _RamMoId_Type()
)
ramMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ramMoId.setStatus("current")
_RamProvEqptType_Type = InfnEqptType
_RamProvEqptType_Object = MibTableColumn
ramProvEqptType = _RamProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 12, 1, 1, 2),
    _RamProvEqptType_Type()
)
ramProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ramProvEqptType.setStatus("current")
_RamGainCorrection_Type = FloatTenths
_RamGainCorrection_Object = MibTableColumn
ramGainCorrection = _RamGainCorrection_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 12, 1, 1, 3),
    _RamGainCorrection_Type()
)
ramGainCorrection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ramGainCorrection.setStatus("current")
_RamMaxNumberOfChannels_Type = Unsigned32
_RamMaxNumberOfChannels_Object = MibTableColumn
ramMaxNumberOfChannels = _RamMaxNumberOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 12, 1, 1, 4),
    _RamMaxNumberOfChannels_Type()
)
ramMaxNumberOfChannels.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ramMaxNumberOfChannels.setStatus("current")
_RamPointLossOffset_Type = FloatTenths
_RamPointLossOffset_Object = MibTableColumn
ramPointLossOffset = _RamPointLossOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 12, 1, 1, 5),
    _RamPointLossOffset_Type()
)
ramPointLossOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ramPointLossOffset.setStatus("current")
_RamRowStatus_Type = RowStatus
_RamRowStatus_Object = MibTableColumn
ramRowStatus = _RamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 12, 1, 1, 6),
    _RamRowStatus_Type()
)
ramRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ramRowStatus.setStatus("current")
_RamTargetGainOffset_Type = FloatTenths
_RamTargetGainOffset_Object = MibTableColumn
ramTargetGainOffset = _RamTargetGainOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 12, 1, 1, 7),
    _RamTargetGainOffset_Type()
)
ramTargetGainOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ramTargetGainOffset.setStatus("current")
_RamPilotLaserDisable_Type = TruthValue
_RamPilotLaserDisable_Object = MibTableColumn
ramPilotLaserDisable = _RamPilotLaserDisable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 12, 1, 1, 8),
    _RamPilotLaserDisable_Type()
)
ramPilotLaserDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ramPilotLaserDisable.setStatus("current")
_RamConformance_ObjectIdentity = ObjectIdentity
ramConformance = _RamConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 12, 3)
)
_RamCompliances_ObjectIdentity = ObjectIdentity
ramCompliances = _RamCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 12, 3, 1)
)
_RamGroups_ObjectIdentity = ObjectIdentity
ramGroups = _RamGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 12, 3, 2)
)

# Managed Objects groups

ramGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 12, 3, 2, 1)
)
ramGroup.setObjects(
      *(("INFINERA-ENTITY-RAM-MIB", "ramMoId"),
        ("INFINERA-ENTITY-RAM-MIB", "ramProvEqptType"),
        ("INFINERA-ENTITY-RAM-MIB", "ramGainCorrection"),
        ("INFINERA-ENTITY-RAM-MIB", "ramMaxNumberOfChannels"),
        ("INFINERA-ENTITY-RAM-MIB", "ramPointLossOffset"),
        ("INFINERA-ENTITY-RAM-MIB", "ramRowStatus"),
        ("INFINERA-ENTITY-RAM-MIB", "ramTargetGainOffset"),
        ("INFINERA-ENTITY-RAM-MIB", "ramPilotLaserDisable"))
)
if mibBuilder.loadTexts:
    ramGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ramCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 12, 3, 1, 1)
)
ramCompliance.setObjects(
    ("INFINERA-ENTITY-RAM-MIB", "ramGroup")
)
if mibBuilder.loadTexts:
    ramCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-RAM-MIB",
    **{"ramMIB": ramMIB,
       "ramTable": ramTable,
       "ramEntry": ramEntry,
       "ramMoId": ramMoId,
       "ramProvEqptType": ramProvEqptType,
       "ramGainCorrection": ramGainCorrection,
       "ramMaxNumberOfChannels": ramMaxNumberOfChannels,
       "ramPointLossOffset": ramPointLossOffset,
       "ramRowStatus": ramRowStatus,
       "ramTargetGainOffset": ramTargetGainOffset,
       "ramPilotLaserDisable": ramPilotLaserDisable,
       "ramConformance": ramConformance,
       "ramCompliances": ramCompliances,
       "ramCompliance": ramCompliance,
       "ramGroups": ramGroups,
       "ramGroup": ramGroup}
)
