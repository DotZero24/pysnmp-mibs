# SNMP MIB module (INFINERA-ENTITY-ORM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-ORM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:20 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(equipment,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "equipment")

(FloatHundredths,
 FloatTenths,
 InfnEnableDisable,
 InfnEqptType,
 InfnFiberType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "FloatTenths",
    "InfnEnableDisable",
    "InfnEqptType",
    "InfnFiberType")

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

ormMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OrmTable_Object = MibTable
ormTable = _OrmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1)
)
if mibBuilder.loadTexts:
    ormTable.setStatus("current")
_OrmEntry_Object = MibTableRow
ormEntry = _OrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1)
)
ormEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ormEntry.setStatus("current")
_OrmMoId_Type = DisplayString
_OrmMoId_Object = MibTableColumn
ormMoId = _OrmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 1),
    _OrmMoId_Type()
)
ormMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ormMoId.setStatus("current")
_OrmProvisonedType_Type = InfnEqptType
_OrmProvisonedType_Object = MibTableColumn
ormProvisonedType = _OrmProvisonedType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 2),
    _OrmProvisonedType_Type()
)
ormProvisonedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ormProvisonedType.setStatus("current")
_OrmRxAmpDeviceSetpoint_Type = FloatTenths
_OrmRxAmpDeviceSetpoint_Object = MibTableColumn
ormRxAmpDeviceSetpoint = _OrmRxAmpDeviceSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 3),
    _OrmRxAmpDeviceSetpoint_Type()
)
ormRxAmpDeviceSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ormRxAmpDeviceSetpoint.setStatus("current")
_OrmRxAmpDeviceTarget_Type = FloatTenths
_OrmRxAmpDeviceTarget_Object = MibTableColumn
ormRxAmpDeviceTarget = _OrmRxAmpDeviceTarget_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 4),
    _OrmRxAmpDeviceTarget_Type()
)
ormRxAmpDeviceTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ormRxAmpDeviceTarget.setStatus("current")
_OrmRxLastAmpDeviceCommitTs_Type = Integer32
_OrmRxLastAmpDeviceCommitTs_Object = MibTableColumn
ormRxLastAmpDeviceCommitTs = _OrmRxLastAmpDeviceCommitTs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 5),
    _OrmRxLastAmpDeviceCommitTs_Type()
)
ormRxLastAmpDeviceCommitTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ormRxLastAmpDeviceCommitTs.setStatus("current")
_OrmLaunchPowerOffset_Type = FloatTenths
_OrmLaunchPowerOffset_Object = MibTableColumn
ormLaunchPowerOffset = _OrmLaunchPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 6),
    _OrmLaunchPowerOffset_Type()
)
ormLaunchPowerOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ormLaunchPowerOffset.setStatus("current")
_OrmRxDampSeqNum_Type = Integer32
_OrmRxDampSeqNum_Object = MibTableColumn
ormRxDampSeqNum = _OrmRxDampSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 7),
    _OrmRxDampSeqNum_Type()
)
ormRxDampSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ormRxDampSeqNum.setStatus("current")
_OrmTilt_Type = FloatTenths
_OrmTilt_Object = MibTableColumn
ormTilt = _OrmTilt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 8),
    _OrmTilt_Type()
)
ormTilt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ormTilt.setStatus("current")
_OrmPointLossOffset_Type = FloatTenths
_OrmPointLossOffset_Object = MibTableColumn
ormPointLossOffset = _OrmPointLossOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 9),
    _OrmPointLossOffset_Type()
)
ormPointLossOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ormPointLossOffset.setStatus("current")
_OrmEnhPMRept_Type = InfnEnableDisable
_OrmEnhPMRept_Object = MibTableColumn
ormEnhPMRept = _OrmEnhPMRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 10),
    _OrmEnhPMRept_Type()
)
ormEnhPMRept.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ormEnhPMRept.setStatus("current")
_OrmRowStatus_Type = RowStatus
_OrmRowStatus_Object = MibTableColumn
ormRowStatus = _OrmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 11),
    _OrmRowStatus_Type()
)
ormRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ormRowStatus.setStatus("current")
_OrmCBandSoakCapableFW_Type = TruthValue
_OrmCBandSoakCapableFW_Object = MibTableColumn
ormCBandSoakCapableFW = _OrmCBandSoakCapableFW_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 12),
    _OrmCBandSoakCapableFW_Type()
)
ormCBandSoakCapableFW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ormCBandSoakCapableFW.setStatus("current")
_OrmAsePowerBetaCoeffX_Type = FloatHundredths
_OrmAsePowerBetaCoeffX_Object = MibTableColumn
ormAsePowerBetaCoeffX = _OrmAsePowerBetaCoeffX_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 13),
    _OrmAsePowerBetaCoeffX_Type()
)
ormAsePowerBetaCoeffX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ormAsePowerBetaCoeffX.setStatus("current")
_OrmAsePowerBetaCoeffY_Type = FloatHundredths
_OrmAsePowerBetaCoeffY_Object = MibTableColumn
ormAsePowerBetaCoeffY = _OrmAsePowerBetaCoeffY_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 14),
    _OrmAsePowerBetaCoeffY_Type()
)
ormAsePowerBetaCoeffY.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ormAsePowerBetaCoeffY.setStatus("current")
_OrmAsePowerBetaCoeffZ_Type = FloatHundredths
_OrmAsePowerBetaCoeffZ_Object = MibTableColumn
ormAsePowerBetaCoeffZ = _OrmAsePowerBetaCoeffZ_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 15),
    _OrmAsePowerBetaCoeffZ_Type()
)
ormAsePowerBetaCoeffZ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ormAsePowerBetaCoeffZ.setStatus("current")
_OrmPumpPowerBetaCoeffX_Type = FloatHundredths
_OrmPumpPowerBetaCoeffX_Object = MibTableColumn
ormPumpPowerBetaCoeffX = _OrmPumpPowerBetaCoeffX_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 16),
    _OrmPumpPowerBetaCoeffX_Type()
)
ormPumpPowerBetaCoeffX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ormPumpPowerBetaCoeffX.setStatus("current")
_OrmPumpPowerBetaCoeffY_Type = FloatHundredths
_OrmPumpPowerBetaCoeffY_Object = MibTableColumn
ormPumpPowerBetaCoeffY = _OrmPumpPowerBetaCoeffY_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 17),
    _OrmPumpPowerBetaCoeffY_Type()
)
ormPumpPowerBetaCoeffY.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ormPumpPowerBetaCoeffY.setStatus("current")
_OrmPumpPowerBetaCoeffZ_Type = FloatHundredths
_OrmPumpPowerBetaCoeffZ_Object = MibTableColumn
ormPumpPowerBetaCoeffZ = _OrmPumpPowerBetaCoeffZ_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 18),
    _OrmPumpPowerBetaCoeffZ_Type()
)
ormPumpPowerBetaCoeffZ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ormPumpPowerBetaCoeffZ.setStatus("current")
_OrmPumpRatioPump1_Type = FloatHundredths
_OrmPumpRatioPump1_Object = MibTableColumn
ormPumpRatioPump1 = _OrmPumpRatioPump1_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 19),
    _OrmPumpRatioPump1_Type()
)
ormPumpRatioPump1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ormPumpRatioPump1.setStatus("current")
_OrmPumpRatioPump2_Type = FloatHundredths
_OrmPumpRatioPump2_Object = MibTableColumn
ormPumpRatioPump2 = _OrmPumpRatioPump2_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 20),
    _OrmPumpRatioPump2_Type()
)
ormPumpRatioPump2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ormPumpRatioPump2.setStatus("current")
_OrmPumpRatioPump3_Type = FloatHundredths
_OrmPumpRatioPump3_Object = MibTableColumn
ormPumpRatioPump3 = _OrmPumpRatioPump3_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 21),
    _OrmPumpRatioPump3_Type()
)
ormPumpRatioPump3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ormPumpRatioPump3.setStatus("current")
_OrmPumpRatioPump4_Type = FloatHundredths
_OrmPumpRatioPump4_Object = MibTableColumn
ormPumpRatioPump4 = _OrmPumpRatioPump4_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 22),
    _OrmPumpRatioPump4_Type()
)
ormPumpRatioPump4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ormPumpRatioPump4.setStatus("current")
_OrmStaticRamanGain_Type = FloatHundredths
_OrmStaticRamanGain_Object = MibTableColumn
ormStaticRamanGain = _OrmStaticRamanGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 23),
    _OrmStaticRamanGain_Type()
)
ormStaticRamanGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ormStaticRamanGain.setStatus("current")
_OrmStaticEdfaGain_Type = FloatHundredths
_OrmStaticEdfaGain_Object = MibTableColumn
ormStaticEdfaGain = _OrmStaticEdfaGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 24),
    _OrmStaticEdfaGain_Type()
)
ormStaticEdfaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ormStaticEdfaGain.setStatus("current")
_OrmStaticPostEdfaVoaAttenuation_Type = FloatHundredths
_OrmStaticPostEdfaVoaAttenuation_Object = MibTableColumn
ormStaticPostEdfaVoaAttenuation = _OrmStaticPostEdfaVoaAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 25),
    _OrmStaticPostEdfaVoaAttenuation_Type()
)
ormStaticPostEdfaVoaAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ormStaticPostEdfaVoaAttenuation.setStatus("current")
_OrmFiberType_Type = InfnFiberType
_OrmFiberType_Object = MibTableColumn
ormFiberType = _OrmFiberType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 1, 1, 26),
    _OrmFiberType_Type()
)
ormFiberType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ormFiberType.setStatus("current")
_OrmConformance_ObjectIdentity = ObjectIdentity
ormConformance = _OrmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 3)
)
_OrmCompliances_ObjectIdentity = ObjectIdentity
ormCompliances = _OrmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 3, 1)
)
_OrmGroups_ObjectIdentity = ObjectIdentity
ormGroups = _OrmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 3, 2)
)

# Managed Objects groups

ormGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 3, 2, 1)
)
ormGroup.setObjects(
      *(("INFINERA-ENTITY-ORM-MIB", "ormMoId"),
        ("INFINERA-ENTITY-ORM-MIB", "ormProvisonedType"),
        ("INFINERA-ENTITY-ORM-MIB", "ormRxAmpDeviceSetpoint"),
        ("INFINERA-ENTITY-ORM-MIB", "ormRxAmpDeviceTarget"),
        ("INFINERA-ENTITY-ORM-MIB", "ormRxLastAmpDeviceCommitTs"),
        ("INFINERA-ENTITY-ORM-MIB", "ormLaunchPowerOffset"),
        ("INFINERA-ENTITY-ORM-MIB", "ormRxDampSeqNum"),
        ("INFINERA-ENTITY-ORM-MIB", "ormTilt"),
        ("INFINERA-ENTITY-ORM-MIB", "ormPointLossOffset"),
        ("INFINERA-ENTITY-ORM-MIB", "ormEnhPMRept"),
        ("INFINERA-ENTITY-ORM-MIB", "ormRowStatus"),
        ("INFINERA-ENTITY-ORM-MIB", "ormCBandSoakCapableFW"),
        ("INFINERA-ENTITY-ORM-MIB", "ormAsePowerBetaCoeffX"),
        ("INFINERA-ENTITY-ORM-MIB", "ormAsePowerBetaCoeffY"),
        ("INFINERA-ENTITY-ORM-MIB", "ormAsePowerBetaCoeffZ"),
        ("INFINERA-ENTITY-ORM-MIB", "ormPumpPowerBetaCoeffX"),
        ("INFINERA-ENTITY-ORM-MIB", "ormPumpPowerBetaCoeffY"),
        ("INFINERA-ENTITY-ORM-MIB", "ormPumpPowerBetaCoeffZ"),
        ("INFINERA-ENTITY-ORM-MIB", "ormPumpRatioPump1"),
        ("INFINERA-ENTITY-ORM-MIB", "ormPumpRatioPump2"),
        ("INFINERA-ENTITY-ORM-MIB", "ormPumpRatioPump3"),
        ("INFINERA-ENTITY-ORM-MIB", "ormPumpRatioPump4"),
        ("INFINERA-ENTITY-ORM-MIB", "ormStaticRamanGain"),
        ("INFINERA-ENTITY-ORM-MIB", "ormStaticEdfaGain"),
        ("INFINERA-ENTITY-ORM-MIB", "ormStaticPostEdfaVoaAttenuation"),
        ("INFINERA-ENTITY-ORM-MIB", "ormFiberType"))
)
if mibBuilder.loadTexts:
    ormGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ormCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 16, 3, 1, 1)
)
ormCompliance.setObjects(
    ("INFINERA-ENTITY-ORM-MIB", "ormGroup")
)
if mibBuilder.loadTexts:
    ormCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-ORM-MIB",
    **{"ormMIB": ormMIB,
       "ormTable": ormTable,
       "ormEntry": ormEntry,
       "ormMoId": ormMoId,
       "ormProvisonedType": ormProvisonedType,
       "ormRxAmpDeviceSetpoint": ormRxAmpDeviceSetpoint,
       "ormRxAmpDeviceTarget": ormRxAmpDeviceTarget,
       "ormRxLastAmpDeviceCommitTs": ormRxLastAmpDeviceCommitTs,
       "ormLaunchPowerOffset": ormLaunchPowerOffset,
       "ormRxDampSeqNum": ormRxDampSeqNum,
       "ormTilt": ormTilt,
       "ormPointLossOffset": ormPointLossOffset,
       "ormEnhPMRept": ormEnhPMRept,
       "ormRowStatus": ormRowStatus,
       "ormCBandSoakCapableFW": ormCBandSoakCapableFW,
       "ormAsePowerBetaCoeffX": ormAsePowerBetaCoeffX,
       "ormAsePowerBetaCoeffY": ormAsePowerBetaCoeffY,
       "ormAsePowerBetaCoeffZ": ormAsePowerBetaCoeffZ,
       "ormPumpPowerBetaCoeffX": ormPumpPowerBetaCoeffX,
       "ormPumpPowerBetaCoeffY": ormPumpPowerBetaCoeffY,
       "ormPumpPowerBetaCoeffZ": ormPumpPowerBetaCoeffZ,
       "ormPumpRatioPump1": ormPumpRatioPump1,
       "ormPumpRatioPump2": ormPumpRatioPump2,
       "ormPumpRatioPump3": ormPumpRatioPump3,
       "ormPumpRatioPump4": ormPumpRatioPump4,
       "ormStaticRamanGain": ormStaticRamanGain,
       "ormStaticEdfaGain": ormStaticEdfaGain,
       "ormStaticPostEdfaVoaAttenuation": ormStaticPostEdfaVoaAttenuation,
       "ormFiberType": ormFiberType,
       "ormConformance": ormConformance,
       "ormCompliances": ormCompliances,
       "ormCompliance": ormCompliance,
       "ormGroups": ormGroups,
       "ormGroup": ormGroup}
)
