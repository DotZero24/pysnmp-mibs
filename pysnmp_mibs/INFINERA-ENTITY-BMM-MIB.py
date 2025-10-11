# SNMP MIB module (INFINERA-ENTITY-BMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-BMM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:08 2025
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

(FloatTenths,
 InfnEqptType,
 InfnMaxChRatePlan) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnEqptType",
    "InfnMaxChRatePlan")

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

bmmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BmmTable_Object = MibTable
bmmTable = _BmmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    bmmTable.setStatus("current")
_BmmEntry_Object = MibTableRow
bmmEntry = _BmmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3, 1, 1)
)
bmmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    bmmEntry.setStatus("current")
_BmmMoId_Type = DisplayString
_BmmMoId_Object = MibTableColumn
bmmMoId = _BmmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3, 1, 1, 1),
    _BmmMoId_Type()
)
bmmMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bmmMoId.setStatus("current")


class _BmmProvisonedType_Type(InfnEqptType):
    """Custom type bmmProvisonedType based on InfnEqptType"""
    defaultValue = 47


_BmmProvisonedType_Type.__name__ = "InfnEqptType"
_BmmProvisonedType_Object = MibTableColumn
bmmProvisonedType = _BmmProvisonedType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3, 1, 1, 2),
    _BmmProvisonedType_Type()
)
bmmProvisonedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bmmProvisonedType.setStatus("current")
_BmmRxAmpDeviceSetpoint_Type = FloatTenths
_BmmRxAmpDeviceSetpoint_Object = MibTableColumn
bmmRxAmpDeviceSetpoint = _BmmRxAmpDeviceSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3, 1, 1, 3),
    _BmmRxAmpDeviceSetpoint_Type()
)
bmmRxAmpDeviceSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmmRxAmpDeviceSetpoint.setStatus("current")
_BmmRxAmpDeviceTarget_Type = FloatTenths
_BmmRxAmpDeviceTarget_Object = MibTableColumn
bmmRxAmpDeviceTarget = _BmmRxAmpDeviceTarget_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3, 1, 1, 4),
    _BmmRxAmpDeviceTarget_Type()
)
bmmRxAmpDeviceTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmmRxAmpDeviceTarget.setStatus("current")
_BmmRxLastAmpDeviceCommitTs_Type = Integer32
_BmmRxLastAmpDeviceCommitTs_Object = MibTableColumn
bmmRxLastAmpDeviceCommitTs = _BmmRxLastAmpDeviceCommitTs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3, 1, 1, 5),
    _BmmRxLastAmpDeviceCommitTs_Type()
)
bmmRxLastAmpDeviceCommitTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmmRxLastAmpDeviceCommitTs.setStatus("current")


class _BmmDisableGainControlLoop_Type(TruthValue):
    """Custom type bmmDisableGainControlLoop based on TruthValue"""
    defaultValue = 2


_BmmDisableGainControlLoop_Type.__name__ = "TruthValue"
_BmmDisableGainControlLoop_Object = MibTableColumn
bmmDisableGainControlLoop = _BmmDisableGainControlLoop_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3, 1, 1, 6),
    _BmmDisableGainControlLoop_Type()
)
bmmDisableGainControlLoop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bmmDisableGainControlLoop.setStatus("current")
_BmmLaunchPowerOffset_Type = FloatTenths
_BmmLaunchPowerOffset_Object = MibTableColumn
bmmLaunchPowerOffset = _BmmLaunchPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3, 1, 1, 7),
    _BmmLaunchPowerOffset_Type()
)
bmmLaunchPowerOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bmmLaunchPowerOffset.setStatus("current")
_BmmNumberOfChannel_Type = Integer32
_BmmNumberOfChannel_Object = MibTableColumn
bmmNumberOfChannel = _BmmNumberOfChannel_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3, 1, 1, 8),
    _BmmNumberOfChannel_Type()
)
bmmNumberOfChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bmmNumberOfChannel.setStatus("current")
_BmmTxDampSeqNum_Type = Integer32
_BmmTxDampSeqNum_Object = MibTableColumn
bmmTxDampSeqNum = _BmmTxDampSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3, 1, 1, 9),
    _BmmTxDampSeqNum_Type()
)
bmmTxDampSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmmTxDampSeqNum.setStatus("current")
_BmmRxDampSeqNum_Type = Integer32
_BmmRxDampSeqNum_Object = MibTableColumn
bmmRxDampSeqNum = _BmmRxDampSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3, 1, 1, 10),
    _BmmRxDampSeqNum_Type()
)
bmmRxDampSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmmRxDampSeqNum.setStatus("current")
_BmmTilt_Type = FloatTenths
_BmmTilt_Object = MibTableColumn
bmmTilt = _BmmTilt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3, 1, 1, 11),
    _BmmTilt_Type()
)
bmmTilt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bmmTilt.setStatus("current")


class _BmmOperatingMode_Type(Integer32):
    """Custom type bmmOperatingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("nativeAutomated", 1),
          ("slteMode1", 2),
          ("thirdPartyAmp", 3),
          ("static", 4))
    )


_BmmOperatingMode_Type.__name__ = "Integer32"
_BmmOperatingMode_Object = MibTableColumn
bmmOperatingMode = _BmmOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3, 1, 1, 12),
    _BmmOperatingMode_Type()
)
bmmOperatingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bmmOperatingMode.setStatus("current")
_BmmGain_Type = FloatTenths
_BmmGain_Object = MibTableColumn
bmmGain = _BmmGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3, 1, 1, 13),
    _BmmGain_Type()
)
bmmGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bmmGain.setStatus("current")
_BmmRowStatus_Type = RowStatus
_BmmRowStatus_Object = MibTableColumn
bmmRowStatus = _BmmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3, 1, 1, 14),
    _BmmRowStatus_Type()
)
bmmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bmmRowStatus.setStatus("current")
_BmmMaxChanRatePlan_Type = InfnMaxChRatePlan
_BmmMaxChanRatePlan_Object = MibTableColumn
bmmMaxChanRatePlan = _BmmMaxChanRatePlan_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3, 1, 1, 15),
    _BmmMaxChanRatePlan_Type()
)
bmmMaxChanRatePlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bmmMaxChanRatePlan.setStatus("current")
_BmmCBandSoakCapableFW_Type = TruthValue
_BmmCBandSoakCapableFW_Object = MibTableColumn
bmmCBandSoakCapableFW = _BmmCBandSoakCapableFW_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3, 1, 1, 16),
    _BmmCBandSoakCapableFW_Type()
)
bmmCBandSoakCapableFW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmmCBandSoakCapableFW.setStatus("current")
_BmmSuccessfulACGRunTime_Type = Integer32
_BmmSuccessfulACGRunTime_Object = MibTableColumn
bmmSuccessfulACGRunTime = _BmmSuccessfulACGRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3, 1, 1, 17),
    _BmmSuccessfulACGRunTime_Type()
)
bmmSuccessfulACGRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmmSuccessfulACGRunTime.setStatus("current")
_BmmConformance_ObjectIdentity = ObjectIdentity
bmmConformance = _BmmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3, 3)
)
_BmmCompliances_ObjectIdentity = ObjectIdentity
bmmCompliances = _BmmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3, 3, 1)
)
_BmmGroups_ObjectIdentity = ObjectIdentity
bmmGroups = _BmmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3, 3, 2)
)

# Managed Objects groups

bmmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3, 3, 2, 1)
)
bmmGroup.setObjects(
      *(("INFINERA-ENTITY-BMM-MIB", "bmmMoId"),
        ("INFINERA-ENTITY-BMM-MIB", "bmmProvisonedType"),
        ("INFINERA-ENTITY-BMM-MIB", "bmmRxAmpDeviceSetpoint"),
        ("INFINERA-ENTITY-BMM-MIB", "bmmRxAmpDeviceTarget"),
        ("INFINERA-ENTITY-BMM-MIB", "bmmRxLastAmpDeviceCommitTs"),
        ("INFINERA-ENTITY-BMM-MIB", "bmmDisableGainControlLoop"),
        ("INFINERA-ENTITY-BMM-MIB", "bmmLaunchPowerOffset"),
        ("INFINERA-ENTITY-BMM-MIB", "bmmNumberOfChannel"),
        ("INFINERA-ENTITY-BMM-MIB", "bmmTxDampSeqNum"),
        ("INFINERA-ENTITY-BMM-MIB", "bmmRxDampSeqNum"),
        ("INFINERA-ENTITY-BMM-MIB", "bmmTilt"),
        ("INFINERA-ENTITY-BMM-MIB", "bmmOperatingMode"),
        ("INFINERA-ENTITY-BMM-MIB", "bmmGain"),
        ("INFINERA-ENTITY-BMM-MIB", "bmmRowStatus"),
        ("INFINERA-ENTITY-BMM-MIB", "bmmMaxChanRatePlan"),
        ("INFINERA-ENTITY-BMM-MIB", "bmmCBandSoakCapableFW"),
        ("INFINERA-ENTITY-BMM-MIB", "bmmSuccessfulACGRunTime"))
)
if mibBuilder.loadTexts:
    bmmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bmmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 3, 3, 1, 1)
)
bmmCompliance.setObjects(
    ("INFINERA-ENTITY-BMM-MIB", "bmmGroup")
)
if mibBuilder.loadTexts:
    bmmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-BMM-MIB",
    **{"bmmMIB": bmmMIB,
       "bmmTable": bmmTable,
       "bmmEntry": bmmEntry,
       "bmmMoId": bmmMoId,
       "bmmProvisonedType": bmmProvisonedType,
       "bmmRxAmpDeviceSetpoint": bmmRxAmpDeviceSetpoint,
       "bmmRxAmpDeviceTarget": bmmRxAmpDeviceTarget,
       "bmmRxLastAmpDeviceCommitTs": bmmRxLastAmpDeviceCommitTs,
       "bmmDisableGainControlLoop": bmmDisableGainControlLoop,
       "bmmLaunchPowerOffset": bmmLaunchPowerOffset,
       "bmmNumberOfChannel": bmmNumberOfChannel,
       "bmmTxDampSeqNum": bmmTxDampSeqNum,
       "bmmRxDampSeqNum": bmmRxDampSeqNum,
       "bmmTilt": bmmTilt,
       "bmmOperatingMode": bmmOperatingMode,
       "bmmGain": bmmGain,
       "bmmRowStatus": bmmRowStatus,
       "bmmMaxChanRatePlan": bmmMaxChanRatePlan,
       "bmmCBandSoakCapableFW": bmmCBandSoakCapableFW,
       "bmmSuccessfulACGRunTime": bmmSuccessfulACGRunTime,
       "bmmConformance": bmmConformance,
       "bmmCompliances": bmmCompliances,
       "bmmCompliance": bmmCompliance,
       "bmmGroups": bmmGroups,
       "bmmGroup": bmmGroup}
)
