# SNMP MIB module (ALU-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/ALU-CHASSIS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:02:29 2025
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

(AluSecQueueId,) = mibBuilder.importSymbols(
    "ALU-QOS-MIB",
    "AluSecQueueId")

(aluSARConfs,
 aluSARMIBModules,
 aluSARNotifyPrefix,
 aluSARObjs) = mibBuilder.importSymbols(
    "ALU-SAR-GLOBAL-MIB",
    "aluSARConfs",
    "aluSARMIBModules",
    "aluSARNotifyPrefix",
    "aluSARObjs")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(TmnxDeviceState,
 TmnxHwIndex,
 TmnxPortAdminStatus,
 TmnxRefInState,
 TmnxSETSRefAlarm,
 TmnxSETSRefQualified,
 TmnxSSMQualityLevel,
 tSyncIfTimingAdmEntry,
 tmnxCardSlotNum,
 tmnxChassisIndex,
 tmnxChassisNotifyChassisId,
 tmnxChassisNotifyHwIndex,
 tmnxCpmCardEntry,
 tmnxHwClass,
 tmnxHwID,
 tmnxHwIndex,
 tmnxMDAEntry,
 tmnxMDASlotNum,
 tmnxSyncIfTimingEntry,
 tmnxSyncIfTimingNotifyAlarm,
 tmnxSyncIfTimingRef1InUse,
 tmnxSyncIfTimingRef2InUse) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxDeviceState",
    "TmnxHwIndex",
    "TmnxPortAdminStatus",
    "TmnxRefInState",
    "TmnxSETSRefAlarm",
    "TmnxSETSRefQualified",
    "TmnxSSMQualityLevel",
    "tSyncIfTimingAdmEntry",
    "tmnxCardSlotNum",
    "tmnxChassisIndex",
    "tmnxChassisNotifyChassisId",
    "tmnxChassisNotifyHwIndex",
    "tmnxCpmCardEntry",
    "tmnxHwClass",
    "tmnxHwID",
    "tmnxHwIndex",
    "tmnxMDAEntry",
    "tmnxMDASlotNum",
    "tmnxSyncIfTimingEntry",
    "tmnxSyncIfTimingNotifyAlarm",
    "tmnxSyncIfTimingRef1InUse",
    "tmnxSyncIfTimingRef2InUse")

(TNamedItem,
 TNamedItemOrEmpty,
 TPolicyID,
 TPortSchedulerPIR,
 TQueueMode,
 TmnxActionType,
 TmnxEnabledDisabled,
 TmnxPortID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPolicyID",
    "TPortSchedulerPIR",
    "TQueueMode",
    "TmnxActionType",
    "TmnxEnabledDisabled",
    "TmnxPortID")


# MODULE-IDENTITY

aluChassisMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    aluChassisMIBModule.setRevisions(
        ("1908-09-17 00:00",
         "1908-01-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluFamType(TextualConvention, Unsigned32):
    status = "current"


class AluExtAlarmState(TextualConvention, Integer32):
    status = "current"
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
        *(("extAlarmStateUnknown", 1),
          ("extAlarmNotEquipped", 2),
          ("extAlarmOk", 3),
          ("extAlarmDetected", 4))
    )



class AluExtAlarmEvent(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("extAlarmSuppressed", 1),
          ("extAlarmCritical", 2),
          ("extAlarmMajor", 3),
          ("extAlarmMinor", 4),
          ("extAlarmWarning", 5),
          ("extAlarmIndeterminate", 6))
    )



class AluPlatformHwClass(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("fam", 1),
          ("extAlarmInput", 2))
    )



class AluHwBgDiagsState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("unknown", 1),
          ("ok", 2),
          ("faultDetected", 3),
          ("criticalFaultDetected", 4))
    )



class AluSETSRefSource(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("reference1", 1),
          ("reference2", 2),
          ("bits", 3),
          ("bits2", 4),
          ("external", 5),
          ("noReference", 7))
    )



class AluExternalIfType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("two-mhz-square", 1),
          ("five-mhz-sine", 2),
          ("ten-mhz-sine", 3))
    )



class AluExternalInputImpedanceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high-impedance", 0),
          ("seventyfive-ohm", 1),
          ("fifty-ohm", 2))
    )



class AluSyncIfTimingIeee1588PtpType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("boundary", 1),
          ("ordinary", 2),
          ("end-to-end-transparent", 3),
          ("peer-to-peer-transparent", 4),
          ("management-node", 5))
    )



class AluSecType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notUsed", 0),
          ("ipsec-decrypt", 1),
          ("ipsec-encrypt", 2),
          ("firewall-network-ingress", 3),
          ("firewall-access-ingress", 4))
    )



# MIB Managed Objects in the order of their OIDs

_AluHwConformance_ObjectIdentity = ObjectIdentity
aluHwConformance = _AluHwConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2)
)
_AluChassisConformance_ObjectIdentity = ObjectIdentity
aluChassisConformance = _AluChassisConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1)
)
_AluChassisCompliances_ObjectIdentity = ObjectIdentity
aluChassisCompliances = _AluChassisCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 1)
)
_AluChassisGroups_ObjectIdentity = ObjectIdentity
aluChassisGroups = _AluChassisGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2)
)
_AluSetsMIBConformance_ObjectIdentity = ObjectIdentity
aluSetsMIBConformance = _AluSetsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 4)
)
_AluHwObjs_ObjectIdentity = ObjectIdentity
aluHwObjs = _AluHwObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2)
)
_AluChassisObjs_ObjectIdentity = ObjectIdentity
aluChassisObjs = _AluChassisObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1)
)
_AluFamTable_Object = MibTable
aluFamTable = _AluFamTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    aluFamTable.setStatus("current")
_AluFamEntry_Object = MibTableRow
aluFamEntry = _AluFamEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 1, 1)
)
aluFamEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-CHASSIS-MIB", "aluFamIndex"),
)
if mibBuilder.loadTexts:
    aluFamEntry.setStatus("current")


class _AluFamIndex_Type(Unsigned32):
    """Custom type aluFamIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AluFamIndex_Type.__name__ = "Unsigned32"
_AluFamIndex_Object = MibTableColumn
aluFamIndex = _AluFamIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 1, 1, 1),
    _AluFamIndex_Type()
)
aluFamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluFamIndex.setStatus("current")
_AluFamOperStatus_Type = TmnxDeviceState
_AluFamOperStatus_Object = MibTableColumn
aluFamOperStatus = _AluFamOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 1, 1, 2),
    _AluFamOperStatus_Type()
)
aluFamOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFamOperStatus.setStatus("current")
_AluFamHwIndex_Type = TmnxHwIndex
_AluFamHwIndex_Object = MibTableColumn
aluFamHwIndex = _AluFamHwIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 1, 1, 3),
    _AluFamHwIndex_Type()
)
aluFamHwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFamHwIndex.setStatus("current")
_AluFamEquippedType_Type = AluFamType
_AluFamEquippedType_Object = MibTableColumn
aluFamEquippedType = _AluFamEquippedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 1, 1, 4),
    _AluFamEquippedType_Type()
)
aluFamEquippedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFamEquippedType.setStatus("current")
_AluChassisExtAlarmTable_Object = MibTable
aluChassisExtAlarmTable = _AluChassisExtAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    aluChassisExtAlarmTable.setStatus("current")
_AluChassisExtAlarmEntry_Object = MibTableRow
aluChassisExtAlarmEntry = _AluChassisExtAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 2, 1)
)
aluChassisExtAlarmEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-CHASSIS-MIB", "aluChassisExtAlarmIndex"),
)
if mibBuilder.loadTexts:
    aluChassisExtAlarmEntry.setStatus("current")


class _AluChassisExtAlarmIndex_Type(Unsigned32):
    """Custom type aluChassisExtAlarmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AluChassisExtAlarmIndex_Type.__name__ = "Unsigned32"
_AluChassisExtAlarmIndex_Object = MibTableColumn
aluChassisExtAlarmIndex = _AluChassisExtAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 2, 1, 1),
    _AluChassisExtAlarmIndex_Type()
)
aluChassisExtAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluChassisExtAlarmIndex.setStatus("current")
_AluChassisExtAlarmState_Type = AluExtAlarmState
_AluChassisExtAlarmState_Object = MibTableColumn
aluChassisExtAlarmState = _AluChassisExtAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 2, 1, 2),
    _AluChassisExtAlarmState_Type()
)
aluChassisExtAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluChassisExtAlarmState.setStatus("current")
_AluChassisExtAlarmEvent_Type = AluExtAlarmEvent
_AluChassisExtAlarmEvent_Object = MibTableColumn
aluChassisExtAlarmEvent = _AluChassisExtAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 2, 1, 3),
    _AluChassisExtAlarmEvent_Type()
)
aluChassisExtAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluChassisExtAlarmEvent.setStatus("current")


class _AluChassisExtAlarmPin_Type(Unsigned32):
    """Custom type aluChassisExtAlarmPin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_AluChassisExtAlarmPin_Type.__name__ = "Unsigned32"
_AluChassisExtAlarmPin_Object = MibTableColumn
aluChassisExtAlarmPin = _AluChassisExtAlarmPin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 2, 1, 4),
    _AluChassisExtAlarmPin_Type()
)
aluChassisExtAlarmPin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluChassisExtAlarmPin.setStatus("current")
_AluExtTmnxHwTable_Object = MibTable
aluExtTmnxHwTable = _AluExtTmnxHwTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    aluExtTmnxHwTable.setStatus("current")
_AluExtTmnxHwEntry_Object = MibTableRow
aluExtTmnxHwEntry = _AluExtTmnxHwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 3, 1)
)
aluExtTmnxHwEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxHwIndex"),
)
if mibBuilder.loadTexts:
    aluExtTmnxHwEntry.setStatus("current")
_AluExtPlatformHwClass_Type = AluPlatformHwClass
_AluExtPlatformHwClass_Object = MibTableColumn
aluExtPlatformHwClass = _AluExtPlatformHwClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 3, 1, 1),
    _AluExtPlatformHwClass_Type()
)
aluExtPlatformHwClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtPlatformHwClass.setStatus("current")


class _AluExtHwBgDiagsState_Type(AluHwBgDiagsState):
    """Custom type aluExtHwBgDiagsState based on AluHwBgDiagsState"""
    defaultValue = 1


_AluExtHwBgDiagsState_Type.__name__ = "AluHwBgDiagsState"
_AluExtHwBgDiagsState_Object = MibTableColumn
aluExtHwBgDiagsState = _AluExtHwBgDiagsState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 3, 1, 2),
    _AluExtHwBgDiagsState_Type()
)
aluExtHwBgDiagsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtHwBgDiagsState.setStatus("current")
_AluExtHwBgDiagsFaultReason_Type = DisplayString
_AluExtHwBgDiagsFaultReason_Object = MibTableColumn
aluExtHwBgDiagsFaultReason = _AluExtHwBgDiagsFaultReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 3, 1, 3),
    _AluExtHwBgDiagsFaultReason_Type()
)
aluExtHwBgDiagsFaultReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtHwBgDiagsFaultReason.setStatus("current")
_AluExtHwMfgVariant_Type = DisplayString
_AluExtHwMfgVariant_Object = MibTableColumn
aluExtHwMfgVariant = _AluExtHwMfgVariant_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 3, 1, 4),
    _AluExtHwMfgVariant_Type()
)
aluExtHwMfgVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtHwMfgVariant.setStatus("current")
_AluExtTmnxMDATable_Object = MibTable
aluExtTmnxMDATable = _AluExtTmnxMDATable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    aluExtTmnxMDATable.setStatus("current")
_AluExtTmnxMDAEntry_Object = MibTableRow
aluExtTmnxMDAEntry = _AluExtTmnxMDAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    aluExtTmnxMDAEntry.setStatus("current")


class _AluExtTmnxMDANetworkIngFabricPolicy_Type(TPolicyID):
    """Custom type aluExtTmnxMDANetworkIngFabricPolicy based on TPolicyID"""
    defaultValue = 1

    subtypeSpec = TPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AluExtTmnxMDANetworkIngFabricPolicy_Type.__name__ = "TPolicyID"
_AluExtTmnxMDANetworkIngFabricPolicy_Object = MibTableColumn
aluExtTmnxMDANetworkIngFabricPolicy = _AluExtTmnxMDANetworkIngFabricPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 1),
    _AluExtTmnxMDANetworkIngFabricPolicy_Type()
)
aluExtTmnxMDANetworkIngFabricPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtTmnxMDANetworkIngFabricPolicy.setStatus("current")


class _AluExtTmnxMDAAccessIngFabricPolicy_Type(TPolicyID):
    """Custom type aluExtTmnxMDAAccessIngFabricPolicy based on TPolicyID"""
    defaultValue = 1

    subtypeSpec = TPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AluExtTmnxMDAAccessIngFabricPolicy_Type.__name__ = "TPolicyID"
_AluExtTmnxMDAAccessIngFabricPolicy_Object = MibTableColumn
aluExtTmnxMDAAccessIngFabricPolicy = _AluExtTmnxMDAAccessIngFabricPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 2),
    _AluExtTmnxMDAAccessIngFabricPolicy_Type()
)
aluExtTmnxMDAAccessIngFabricPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtTmnxMDAAccessIngFabricPolicy.setStatus("current")


class _AluExtTmnxMDAFabricStatsEnabled_Type(TruthValue):
    """Custom type aluExtTmnxMDAFabricStatsEnabled based on TruthValue"""
    defaultValue = 2


_AluExtTmnxMDAFabricStatsEnabled_Type.__name__ = "TruthValue"
_AluExtTmnxMDAFabricStatsEnabled_Object = MibTableColumn
aluExtTmnxMDAFabricStatsEnabled = _AluExtTmnxMDAFabricStatsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 3),
    _AluExtTmnxMDAFabricStatsEnabled_Type()
)
aluExtTmnxMDAFabricStatsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtTmnxMDAFabricStatsEnabled.setStatus("current")


class _AluExtTmnxMDAVoiceCompandingLaw_Type(Integer32):
    """Custom type aluExtTmnxMDAVoiceCompandingLaw based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("aLaw", 1),
          ("muLaw", 2))
    )


_AluExtTmnxMDAVoiceCompandingLaw_Type.__name__ = "Integer32"
_AluExtTmnxMDAVoiceCompandingLaw_Object = MibTableColumn
aluExtTmnxMDAVoiceCompandingLaw = _AluExtTmnxMDAVoiceCompandingLaw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 4),
    _AluExtTmnxMDAVoiceCompandingLaw_Type()
)
aluExtTmnxMDAVoiceCompandingLaw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtTmnxMDAVoiceCompandingLaw.setStatus("current")


class _AluExtTmnxMDAVoiceSignalingType_Type(Integer32):
    """Custom type aluExtTmnxMDAVoiceSignalingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("typeI", 1),
          ("typeII", 2),
          ("typeIII", 3),
          ("typeIV", 4),
          ("typeV", 5))
    )


_AluExtTmnxMDAVoiceSignalingType_Type.__name__ = "Integer32"
_AluExtTmnxMDAVoiceSignalingType_Object = MibTableColumn
aluExtTmnxMDAVoiceSignalingType = _AluExtTmnxMDAVoiceSignalingType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 5),
    _AluExtTmnxMDAVoiceSignalingType_Type()
)
aluExtTmnxMDAVoiceSignalingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtTmnxMDAVoiceSignalingType.setStatus("current")
_AluExtTmnxMDANumOfDigitalAlarmInputs_Type = Integer32
_AluExtTmnxMDANumOfDigitalAlarmInputs_Object = MibTableColumn
aluExtTmnxMDANumOfDigitalAlarmInputs = _AluExtTmnxMDANumOfDigitalAlarmInputs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 6),
    _AluExtTmnxMDANumOfDigitalAlarmInputs_Type()
)
aluExtTmnxMDANumOfDigitalAlarmInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtTmnxMDANumOfDigitalAlarmInputs.setStatus("current")
_AluExtTmnxMDANumOfAnalogAlarmInputs_Type = Integer32
_AluExtTmnxMDANumOfAnalogAlarmInputs_Object = MibTableColumn
aluExtTmnxMDANumOfAnalogAlarmInputs = _AluExtTmnxMDANumOfAnalogAlarmInputs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 7),
    _AluExtTmnxMDANumOfAnalogAlarmInputs_Type()
)
aluExtTmnxMDANumOfAnalogAlarmInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtTmnxMDANumOfAnalogAlarmInputs.setStatus("current")
_AluExtTmnxMDANumOfDigitalOutputRelays_Type = Integer32
_AluExtTmnxMDANumOfDigitalOutputRelays_Object = MibTableColumn
aluExtTmnxMDANumOfDigitalOutputRelays = _AluExtTmnxMDANumOfDigitalOutputRelays_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 8),
    _AluExtTmnxMDANumOfDigitalOutputRelays_Type()
)
aluExtTmnxMDANumOfDigitalOutputRelays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtTmnxMDANumOfDigitalOutputRelays.setStatus("current")


class _AluExtTmnxMDACapabilityMode_Type(Integer32):
    """Custom type aluExtTmnxMDACapabilityMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("modeA", 1),
          ("modeB", 2),
          ("modeC", 3))
    )


_AluExtTmnxMDACapabilityMode_Type.__name__ = "Integer32"
_AluExtTmnxMDACapabilityMode_Object = MibTableColumn
aluExtTmnxMDACapabilityMode = _AluExtTmnxMDACapabilityMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 9),
    _AluExtTmnxMDACapabilityMode_Type()
)
aluExtTmnxMDACapabilityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtTmnxMDACapabilityMode.setStatus("current")


class _AluExtTmnxMDANetworkRingQueuePolicy_Type(TNamedItemOrEmpty):
    """Custom type aluExtTmnxMDANetworkRingQueuePolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_AluExtTmnxMDANetworkRingQueuePolicy_Type.__name__ = "TNamedItemOrEmpty"
_AluExtTmnxMDANetworkRingQueuePolicy_Object = MibTableColumn
aluExtTmnxMDANetworkRingQueuePolicy = _AluExtTmnxMDANetworkRingQueuePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 10),
    _AluExtTmnxMDANetworkRingQueuePolicy_Type()
)
aluExtTmnxMDANetworkRingQueuePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtTmnxMDANetworkRingQueuePolicy.setStatus("current")


class _AluExtTmnxMDANetworkRingQosPolicy_Type(TPolicyID):
    """Custom type aluExtTmnxMDANetworkRingQosPolicy based on TPolicyID"""
    defaultValue = 0

    subtypeSpec = TPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluExtTmnxMDANetworkRingQosPolicy_Type.__name__ = "TPolicyID"
_AluExtTmnxMDANetworkRingQosPolicy_Object = MibTableColumn
aluExtTmnxMDANetworkRingQosPolicy = _AluExtTmnxMDANetworkRingQosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 11),
    _AluExtTmnxMDANetworkRingQosPolicy_Type()
)
aluExtTmnxMDANetworkRingQosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtTmnxMDANetworkRingQosPolicy.setStatus("current")


class _AluExtTmnxMDAPwrEthPsPowerMode_Type(Integer32):
    """Custom type aluExtTmnxMDAPwrEthPsPowerMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("internal", 1),
          ("external", 2))
    )


_AluExtTmnxMDAPwrEthPsPowerMode_Type.__name__ = "Integer32"
_AluExtTmnxMDAPwrEthPsPowerMode_Object = MibTableColumn
aluExtTmnxMDAPwrEthPsPowerMode = _AluExtTmnxMDAPwrEthPsPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 12),
    _AluExtTmnxMDAPwrEthPsPowerMode_Type()
)
aluExtTmnxMDAPwrEthPsPowerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtTmnxMDAPwrEthPsPowerMode.setStatus("current")


class _AluExtTmnxMDAPwrEthPsPowerSupplyStatus_Type(Integer32):
    """Custom type aluExtTmnxMDAPwrEthPsPowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("bad", 1),
          ("good", 2))
    )


_AluExtTmnxMDAPwrEthPsPowerSupplyStatus_Type.__name__ = "Integer32"
_AluExtTmnxMDAPwrEthPsPowerSupplyStatus_Object = MibTableColumn
aluExtTmnxMDAPwrEthPsPowerSupplyStatus = _AluExtTmnxMDAPwrEthPsPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 13),
    _AluExtTmnxMDAPwrEthPsPowerSupplyStatus_Type()
)
aluExtTmnxMDAPwrEthPsPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtTmnxMDAPwrEthPsPowerSupplyStatus.setStatus("current")


class _AluExtTmnxMDAPwrEthPsExternalPowerSupplyStatus_Type(Integer32):
    """Custom type aluExtTmnxMDAPwrEthPsExternalPowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("absent", 0),
          ("present", 1))
    )


_AluExtTmnxMDAPwrEthPsExternalPowerSupplyStatus_Type.__name__ = "Integer32"
_AluExtTmnxMDAPwrEthPsExternalPowerSupplyStatus_Object = MibTableColumn
aluExtTmnxMDAPwrEthPsExternalPowerSupplyStatus = _AluExtTmnxMDAPwrEthPsExternalPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 14),
    _AluExtTmnxMDAPwrEthPsExternalPowerSupplyStatus_Type()
)
aluExtTmnxMDAPwrEthPsExternalPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtTmnxMDAPwrEthPsExternalPowerSupplyStatus.setStatus("current")


class _AluExtTmnxMDATuAisEnabled_Type(TruthValue):
    """Custom type aluExtTmnxMDATuAisEnabled based on TruthValue"""
    defaultValue = 2


_AluExtTmnxMDATuAisEnabled_Type.__name__ = "TruthValue"
_AluExtTmnxMDATuAisEnabled_Object = MibTableColumn
aluExtTmnxMDATuAisEnabled = _AluExtTmnxMDATuAisEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 15),
    _AluExtTmnxMDATuAisEnabled_Type()
)
aluExtTmnxMDATuAisEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtTmnxMDATuAisEnabled.setStatus("current")


class _AluExtTmnxMDANetworkIngSecQueuePolicy_Type(TPolicyID):
    """Custom type aluExtTmnxMDANetworkIngSecQueuePolicy based on TPolicyID"""
    defaultValue = 1


_AluExtTmnxMDANetworkIngSecQueuePolicy_Type.__name__ = "TPolicyID"
_AluExtTmnxMDANetworkIngSecQueuePolicy_Object = MibTableColumn
aluExtTmnxMDANetworkIngSecQueuePolicy = _AluExtTmnxMDANetworkIngSecQueuePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 16),
    _AluExtTmnxMDANetworkIngSecQueuePolicy_Type()
)
aluExtTmnxMDANetworkIngSecQueuePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtTmnxMDANetworkIngSecQueuePolicy.setStatus("current")


class _AluExtTmnxMDAAccessIngSecQueuePolicy_Type(TPolicyID):
    """Custom type aluExtTmnxMDAAccessIngSecQueuePolicy based on TPolicyID"""
    defaultValue = 1


_AluExtTmnxMDAAccessIngSecQueuePolicy_Type.__name__ = "TPolicyID"
_AluExtTmnxMDAAccessIngSecQueuePolicy_Object = MibTableColumn
aluExtTmnxMDAAccessIngSecQueuePolicy = _AluExtTmnxMDAAccessIngSecQueuePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 17),
    _AluExtTmnxMDAAccessIngSecQueuePolicy_Type()
)
aluExtTmnxMDAAccessIngSecQueuePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtTmnxMDAAccessIngSecQueuePolicy.setStatus("current")


class _AluExtTmnxMDASptSecAggRate_Type(TPortSchedulerPIR):
    """Custom type aluExtTmnxMDASptSecAggRate based on TPortSchedulerPIR"""
    defaultValue = 50000


_AluExtTmnxMDASptSecAggRate_Type.__name__ = "TPortSchedulerPIR"
_AluExtTmnxMDASptSecAggRate_Object = MibTableColumn
aluExtTmnxMDASptSecAggRate = _AluExtTmnxMDASptSecAggRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 18),
    _AluExtTmnxMDASptSecAggRate_Type()
)
aluExtTmnxMDASptSecAggRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtTmnxMDASptSecAggRate.setStatus("current")


class _AluExtTmnxMDAAccessIngShaperPolicy_Type(TNamedItemOrEmpty):
    """Custom type aluExtTmnxMDAAccessIngShaperPolicy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_AluExtTmnxMDAAccessIngShaperPolicy_Type.__name__ = "TNamedItemOrEmpty"
_AluExtTmnxMDAAccessIngShaperPolicy_Object = MibTableColumn
aluExtTmnxMDAAccessIngShaperPolicy = _AluExtTmnxMDAAccessIngShaperPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 19),
    _AluExtTmnxMDAAccessIngShaperPolicy_Type()
)
aluExtTmnxMDAAccessIngShaperPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtTmnxMDAAccessIngShaperPolicy.setStatus("current")


class _AluExtTmnxMDAVcbApplication_Type(Integer32):
    """Custom type aluExtTmnxMDAVcbApplication based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("broadcast", 1),
          ("teleprotection", 2),
          ("vcb", 3),
          ("vcbBranchInitiate", 4))
    )


_AluExtTmnxMDAVcbApplication_Type.__name__ = "Integer32"
_AluExtTmnxMDAVcbApplication_Object = MibTableColumn
aluExtTmnxMDAVcbApplication = _AluExtTmnxMDAVcbApplication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 4, 1, 20),
    _AluExtTmnxMDAVcbApplication_Type()
)
aluExtTmnxMDAVcbApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtTmnxMDAVcbApplication.setStatus("current")
_AluFabricDeviceStatsTable_Object = MibTable
aluFabricDeviceStatsTable = _AluFabricDeviceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    aluFabricDeviceStatsTable.setStatus("current")
_AluFabricDeviceStatsEntry_Object = MibTableRow
aluFabricDeviceStatsEntry = _AluFabricDeviceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 5, 1)
)
aluFabricDeviceStatsEntry.setIndexNames(
    (0, "ALU-CHASSIS-MIB", "aluFabricDeviceStatsIndex"),
)
if mibBuilder.loadTexts:
    aluFabricDeviceStatsEntry.setStatus("current")
_AluFabricDeviceStatsIndex_Type = Unsigned32
_AluFabricDeviceStatsIndex_Object = MibTableColumn
aluFabricDeviceStatsIndex = _AluFabricDeviceStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 5, 1, 1),
    _AluFabricDeviceStatsIndex_Type()
)
aluFabricDeviceStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluFabricDeviceStatsIndex.setStatus("current")
_AluFabricDeviceStatsFwdPkts_Type = Counter64
_AluFabricDeviceStatsFwdPkts_Object = MibTableColumn
aluFabricDeviceStatsFwdPkts = _AluFabricDeviceStatsFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 5, 1, 2),
    _AluFabricDeviceStatsFwdPkts_Type()
)
aluFabricDeviceStatsFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFabricDeviceStatsFwdPkts.setStatus("current")
_AluFabricDeviceStatsDroPkts_Type = Counter64
_AluFabricDeviceStatsDroPkts_Object = MibTableColumn
aluFabricDeviceStatsDroPkts = _AluFabricDeviceStatsDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 5, 1, 3),
    _AluFabricDeviceStatsDroPkts_Type()
)
aluFabricDeviceStatsDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFabricDeviceStatsDroPkts.setStatus("current")
_AluFabricDeviceStatsFwdOcts_Type = Counter64
_AluFabricDeviceStatsFwdOcts_Object = MibTableColumn
aluFabricDeviceStatsFwdOcts = _AluFabricDeviceStatsFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 5, 1, 4),
    _AluFabricDeviceStatsFwdOcts_Type()
)
aluFabricDeviceStatsFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFabricDeviceStatsFwdOcts.setStatus("current")
_AluFabricDeviceStatsUcastFwdPkts_Type = Counter64
_AluFabricDeviceStatsUcastFwdPkts_Object = MibTableColumn
aluFabricDeviceStatsUcastFwdPkts = _AluFabricDeviceStatsUcastFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 5, 1, 5),
    _AluFabricDeviceStatsUcastFwdPkts_Type()
)
aluFabricDeviceStatsUcastFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFabricDeviceStatsUcastFwdPkts.setStatus("current")
_AluFabricDeviceStatsMcastFwdPkts_Type = Counter64
_AluFabricDeviceStatsMcastFwdPkts_Object = MibTableColumn
aluFabricDeviceStatsMcastFwdPkts = _AluFabricDeviceStatsMcastFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 5, 1, 6),
    _AluFabricDeviceStatsMcastFwdPkts_Type()
)
aluFabricDeviceStatsMcastFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFabricDeviceStatsMcastFwdPkts.setStatus("current")
_AluFabricDeviceStatsDroOcts_Type = Counter64
_AluFabricDeviceStatsDroOcts_Object = MibTableColumn
aluFabricDeviceStatsDroOcts = _AluFabricDeviceStatsDroOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 5, 1, 7),
    _AluFabricDeviceStatsDroOcts_Type()
)
aluFabricDeviceStatsDroOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFabricDeviceStatsDroOcts.setStatus("current")
_AluFabricDeviceStatsMdaDroEvents_Type = Counter64
_AluFabricDeviceStatsMdaDroEvents_Object = MibTableColumn
aluFabricDeviceStatsMdaDroEvents = _AluFabricDeviceStatsMdaDroEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 5, 1, 8),
    _AluFabricDeviceStatsMdaDroEvents_Type()
)
aluFabricDeviceStatsMdaDroEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluFabricDeviceStatsMdaDroEvents.setStatus("current")
_AluSourceMDAStatsTable_Object = MibTable
aluSourceMDAStatsTable = _AluSourceMDAStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6)
)
if mibBuilder.loadTexts:
    aluSourceMDAStatsTable.setStatus("current")
_AluSourceMDAStatsEntry_Object = MibTableRow
aluSourceMDAStatsEntry = _AluSourceMDAStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1)
)
aluSourceMDAStatsEntry.setIndexNames(
    (0, "ALU-CHASSIS-MIB", "aluSourceMDASrcMdaId"),
    (0, "ALU-CHASSIS-MIB", "aluSourceMDADestMdaId"),
)
if mibBuilder.loadTexts:
    aluSourceMDAStatsEntry.setStatus("current")
_AluSourceMDASrcMdaId_Type = Unsigned32
_AluSourceMDASrcMdaId_Object = MibTableColumn
aluSourceMDASrcMdaId = _AluSourceMDASrcMdaId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 1),
    _AluSourceMDASrcMdaId_Type()
)
aluSourceMDASrcMdaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSourceMDASrcMdaId.setStatus("current")
_AluSourceMDADestMdaId_Type = Unsigned32
_AluSourceMDADestMdaId_Object = MibTableColumn
aluSourceMDADestMdaId = _AluSourceMDADestMdaId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 2),
    _AluSourceMDADestMdaId_Type()
)
aluSourceMDADestMdaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSourceMDADestMdaId.setStatus("current")
_AluSourceMDAStatsFwdInProfPkts_Type = Counter64
_AluSourceMDAStatsFwdInProfPkts_Object = MibTableColumn
aluSourceMDAStatsFwdInProfPkts = _AluSourceMDAStatsFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 3),
    _AluSourceMDAStatsFwdInProfPkts_Type()
)
aluSourceMDAStatsFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsFwdInProfPkts.setStatus("current")
_AluSourceMDAStatsFwdOutProfPkts_Type = Counter64
_AluSourceMDAStatsFwdOutProfPkts_Object = MibTableColumn
aluSourceMDAStatsFwdOutProfPkts = _AluSourceMDAStatsFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 4),
    _AluSourceMDAStatsFwdOutProfPkts_Type()
)
aluSourceMDAStatsFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsFwdOutProfPkts.setStatus("current")
_AluSourceMDAStatsFwdInProfOcts_Type = Counter64
_AluSourceMDAStatsFwdInProfOcts_Object = MibTableColumn
aluSourceMDAStatsFwdInProfOcts = _AluSourceMDAStatsFwdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 5),
    _AluSourceMDAStatsFwdInProfOcts_Type()
)
aluSourceMDAStatsFwdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsFwdInProfOcts.setStatus("current")
_AluSourceMDAStatsFwdOutProfOcts_Type = Counter64
_AluSourceMDAStatsFwdOutProfOcts_Object = MibTableColumn
aluSourceMDAStatsFwdOutProfOcts = _AluSourceMDAStatsFwdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 6),
    _AluSourceMDAStatsFwdOutProfOcts_Type()
)
aluSourceMDAStatsFwdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsFwdOutProfOcts.setStatus("current")
_AluSourceMDAStatsDroInProfPkts_Type = Counter64
_AluSourceMDAStatsDroInProfPkts_Object = MibTableColumn
aluSourceMDAStatsDroInProfPkts = _AluSourceMDAStatsDroInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 7),
    _AluSourceMDAStatsDroInProfPkts_Type()
)
aluSourceMDAStatsDroInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsDroInProfPkts.setStatus("current")
_AluSourceMDAStatsDroOutProfPkts_Type = Counter64
_AluSourceMDAStatsDroOutProfPkts_Object = MibTableColumn
aluSourceMDAStatsDroOutProfPkts = _AluSourceMDAStatsDroOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 8),
    _AluSourceMDAStatsDroOutProfPkts_Type()
)
aluSourceMDAStatsDroOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsDroOutProfPkts.setStatus("current")
_AluSourceMDAStatsDroInProfOcts_Type = Counter64
_AluSourceMDAStatsDroInProfOcts_Object = MibTableColumn
aluSourceMDAStatsDroInProfOcts = _AluSourceMDAStatsDroInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 9),
    _AluSourceMDAStatsDroInProfOcts_Type()
)
aluSourceMDAStatsDroInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsDroInProfOcts.setStatus("current")
_AluSourceMDAStatsDroOutProfOcts_Type = Counter64
_AluSourceMDAStatsDroOutProfOcts_Object = MibTableColumn
aluSourceMDAStatsDroOutProfOcts = _AluSourceMDAStatsDroOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 10),
    _AluSourceMDAStatsDroOutProfOcts_Type()
)
aluSourceMDAStatsDroOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsDroOutProfOcts.setStatus("current")
_AluSourceMDAStatsAccessFwdInProfPkts_Type = Counter64
_AluSourceMDAStatsAccessFwdInProfPkts_Object = MibTableColumn
aluSourceMDAStatsAccessFwdInProfPkts = _AluSourceMDAStatsAccessFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 11),
    _AluSourceMDAStatsAccessFwdInProfPkts_Type()
)
aluSourceMDAStatsAccessFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsAccessFwdInProfPkts.setStatus("current")
_AluSourceMDAStatsAccessFwdOutProfPkts_Type = Counter64
_AluSourceMDAStatsAccessFwdOutProfPkts_Object = MibTableColumn
aluSourceMDAStatsAccessFwdOutProfPkts = _AluSourceMDAStatsAccessFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 12),
    _AluSourceMDAStatsAccessFwdOutProfPkts_Type()
)
aluSourceMDAStatsAccessFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsAccessFwdOutProfPkts.setStatus("current")
_AluSourceMDAStatsAccessFwdInProfOcts_Type = Counter64
_AluSourceMDAStatsAccessFwdInProfOcts_Object = MibTableColumn
aluSourceMDAStatsAccessFwdInProfOcts = _AluSourceMDAStatsAccessFwdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 13),
    _AluSourceMDAStatsAccessFwdInProfOcts_Type()
)
aluSourceMDAStatsAccessFwdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsAccessFwdInProfOcts.setStatus("current")
_AluSourceMDAStatsAccessFwdOutProfOcts_Type = Counter64
_AluSourceMDAStatsAccessFwdOutProfOcts_Object = MibTableColumn
aluSourceMDAStatsAccessFwdOutProfOcts = _AluSourceMDAStatsAccessFwdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 14),
    _AluSourceMDAStatsAccessFwdOutProfOcts_Type()
)
aluSourceMDAStatsAccessFwdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsAccessFwdOutProfOcts.setStatus("current")
_AluSourceMDAStatsAccessDroPkts_Type = Counter64
_AluSourceMDAStatsAccessDroPkts_Object = MibTableColumn
aluSourceMDAStatsAccessDroPkts = _AluSourceMDAStatsAccessDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 15),
    _AluSourceMDAStatsAccessDroPkts_Type()
)
aluSourceMDAStatsAccessDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsAccessDroPkts.setStatus("current")
_AluSourceMDAStatsAccessDroOcts_Type = Counter64
_AluSourceMDAStatsAccessDroOcts_Object = MibTableColumn
aluSourceMDAStatsAccessDroOcts = _AluSourceMDAStatsAccessDroOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 6, 1, 16),
    _AluSourceMDAStatsAccessDroOcts_Type()
)
aluSourceMDAStatsAccessDroOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSourceMDAStatsAccessDroOcts.setStatus("current")
_AluDestMDAStatsTable_Object = MibTable
aluDestMDAStatsTable = _AluDestMDAStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7)
)
if mibBuilder.loadTexts:
    aluDestMDAStatsTable.setStatus("current")
_AluDestMDAStatsEntry_Object = MibTableRow
aluDestMDAStatsEntry = _AluDestMDAStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1)
)
aluDestMDAStatsEntry.setIndexNames(
    (0, "ALU-CHASSIS-MIB", "aluDestMDADestMdaId"),
    (0, "ALU-CHASSIS-MIB", "aluDestMDASrcMdaId"),
)
if mibBuilder.loadTexts:
    aluDestMDAStatsEntry.setStatus("current")
_AluDestMDADestMdaId_Type = Unsigned32
_AluDestMDADestMdaId_Object = MibTableColumn
aluDestMDADestMdaId = _AluDestMDADestMdaId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 1),
    _AluDestMDADestMdaId_Type()
)
aluDestMDADestMdaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluDestMDADestMdaId.setStatus("current")
_AluDestMDASrcMdaId_Type = Unsigned32
_AluDestMDASrcMdaId_Object = MibTableColumn
aluDestMDASrcMdaId = _AluDestMDASrcMdaId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 2),
    _AluDestMDASrcMdaId_Type()
)
aluDestMDASrcMdaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluDestMDASrcMdaId.setStatus("current")
_AluDestMDAStatsFwdInProfPkts_Type = Counter64
_AluDestMDAStatsFwdInProfPkts_Object = MibTableColumn
aluDestMDAStatsFwdInProfPkts = _AluDestMDAStatsFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 3),
    _AluDestMDAStatsFwdInProfPkts_Type()
)
aluDestMDAStatsFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsFwdInProfPkts.setStatus("current")
_AluDestMDAStatsFwdOutProfPkts_Type = Counter64
_AluDestMDAStatsFwdOutProfPkts_Object = MibTableColumn
aluDestMDAStatsFwdOutProfPkts = _AluDestMDAStatsFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 4),
    _AluDestMDAStatsFwdOutProfPkts_Type()
)
aluDestMDAStatsFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsFwdOutProfPkts.setStatus("current")
_AluDestMDAStatsFwdInProfOcts_Type = Counter64
_AluDestMDAStatsFwdInProfOcts_Object = MibTableColumn
aluDestMDAStatsFwdInProfOcts = _AluDestMDAStatsFwdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 5),
    _AluDestMDAStatsFwdInProfOcts_Type()
)
aluDestMDAStatsFwdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsFwdInProfOcts.setStatus("current")
_AluDestMDAStatsFwdOutProfOcts_Type = Counter64
_AluDestMDAStatsFwdOutProfOcts_Object = MibTableColumn
aluDestMDAStatsFwdOutProfOcts = _AluDestMDAStatsFwdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 6),
    _AluDestMDAStatsFwdOutProfOcts_Type()
)
aluDestMDAStatsFwdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsFwdOutProfOcts.setStatus("current")
_AluDestMDAStatsDroInProfPkts_Type = Counter64
_AluDestMDAStatsDroInProfPkts_Object = MibTableColumn
aluDestMDAStatsDroInProfPkts = _AluDestMDAStatsDroInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 7),
    _AluDestMDAStatsDroInProfPkts_Type()
)
aluDestMDAStatsDroInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsDroInProfPkts.setStatus("current")
_AluDestMDAStatsDroOutProfPkts_Type = Counter64
_AluDestMDAStatsDroOutProfPkts_Object = MibTableColumn
aluDestMDAStatsDroOutProfPkts = _AluDestMDAStatsDroOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 8),
    _AluDestMDAStatsDroOutProfPkts_Type()
)
aluDestMDAStatsDroOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsDroOutProfPkts.setStatus("current")
_AluDestMDAStatsDroInProfOcts_Type = Counter64
_AluDestMDAStatsDroInProfOcts_Object = MibTableColumn
aluDestMDAStatsDroInProfOcts = _AluDestMDAStatsDroInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 9),
    _AluDestMDAStatsDroInProfOcts_Type()
)
aluDestMDAStatsDroInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsDroInProfOcts.setStatus("current")
_AluDestMDAStatsDroOutProfOcts_Type = Counter64
_AluDestMDAStatsDroOutProfOcts_Object = MibTableColumn
aluDestMDAStatsDroOutProfOcts = _AluDestMDAStatsDroOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 10),
    _AluDestMDAStatsDroOutProfOcts_Type()
)
aluDestMDAStatsDroOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsDroOutProfOcts.setStatus("current")
_AluDestMDAStatsAccessFwdInProfPkts_Type = Counter64
_AluDestMDAStatsAccessFwdInProfPkts_Object = MibTableColumn
aluDestMDAStatsAccessFwdInProfPkts = _AluDestMDAStatsAccessFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 11),
    _AluDestMDAStatsAccessFwdInProfPkts_Type()
)
aluDestMDAStatsAccessFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsAccessFwdInProfPkts.setStatus("current")
_AluDestMDAStatsAccessFwdOutProfPkts_Type = Counter64
_AluDestMDAStatsAccessFwdOutProfPkts_Object = MibTableColumn
aluDestMDAStatsAccessFwdOutProfPkts = _AluDestMDAStatsAccessFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 12),
    _AluDestMDAStatsAccessFwdOutProfPkts_Type()
)
aluDestMDAStatsAccessFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsAccessFwdOutProfPkts.setStatus("current")
_AluDestMDAStatsAccessFwdInProfOcts_Type = Counter64
_AluDestMDAStatsAccessFwdInProfOcts_Object = MibTableColumn
aluDestMDAStatsAccessFwdInProfOcts = _AluDestMDAStatsAccessFwdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 13),
    _AluDestMDAStatsAccessFwdInProfOcts_Type()
)
aluDestMDAStatsAccessFwdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsAccessFwdInProfOcts.setStatus("current")
_AluDestMDAStatsAccessFwdOutProfOcts_Type = Counter64
_AluDestMDAStatsAccessFwdOutProfOcts_Object = MibTableColumn
aluDestMDAStatsAccessFwdOutProfOcts = _AluDestMDAStatsAccessFwdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 14),
    _AluDestMDAStatsAccessFwdOutProfOcts_Type()
)
aluDestMDAStatsAccessFwdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsAccessFwdOutProfOcts.setStatus("current")
_AluDestMDAStatsAccessDroPkts_Type = Counter64
_AluDestMDAStatsAccessDroPkts_Object = MibTableColumn
aluDestMDAStatsAccessDroPkts = _AluDestMDAStatsAccessDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 15),
    _AluDestMDAStatsAccessDroPkts_Type()
)
aluDestMDAStatsAccessDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsAccessDroPkts.setStatus("current")
_AluDestMDAStatsAccessDroOcts_Type = Counter64
_AluDestMDAStatsAccessDroOcts_Object = MibTableColumn
aluDestMDAStatsAccessDroOcts = _AluDestMDAStatsAccessDroOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 7, 1, 16),
    _AluDestMDAStatsAccessDroOcts_Type()
)
aluDestMDAStatsAccessDroOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDestMDAStatsAccessDroOcts.setStatus("current")
_AluMdaMacFdbMgmtTable_Object = MibTable
aluMdaMacFdbMgmtTable = _AluMdaMacFdbMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 8)
)
if mibBuilder.loadTexts:
    aluMdaMacFdbMgmtTable.setStatus("current")
_AluMdaMacFdbMgmtEntry_Object = MibTableRow
aluMdaMacFdbMgmtEntry = _AluMdaMacFdbMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 8, 1)
)
aluMdaMacFdbMgmtEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    aluMdaMacFdbMgmtEntry.setStatus("current")


class _AluMdaMacFdbMacLearning_Type(TmnxEnabledDisabled):
    """Custom type aluMdaMacFdbMacLearning based on TmnxEnabledDisabled"""
    defaultValue = 1


_AluMdaMacFdbMacLearning_Type.__name__ = "TmnxEnabledDisabled"
_AluMdaMacFdbMacLearning_Object = MibTableColumn
aluMdaMacFdbMacLearning = _AluMdaMacFdbMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 8, 1, 1),
    _AluMdaMacFdbMacLearning_Type()
)
aluMdaMacFdbMacLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluMdaMacFdbMacLearning.setStatus("current")


class _AluMdaMacFdbMacAgeing_Type(TmnxEnabledDisabled):
    """Custom type aluMdaMacFdbMacAgeing based on TmnxEnabledDisabled"""
    defaultValue = 1


_AluMdaMacFdbMacAgeing_Type.__name__ = "TmnxEnabledDisabled"
_AluMdaMacFdbMacAgeing_Object = MibTableColumn
aluMdaMacFdbMacAgeing = _AluMdaMacFdbMacAgeing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 8, 1, 2),
    _AluMdaMacFdbMacAgeing_Type()
)
aluMdaMacFdbMacAgeing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluMdaMacFdbMacAgeing.setStatus("current")


class _AluMdaMacFdbFlushTable_Type(TmnxActionType):
    """Custom type aluMdaMacFdbFlushTable based on TmnxActionType"""
    defaultValue = 2


_AluMdaMacFdbFlushTable_Type.__name__ = "TmnxActionType"
_AluMdaMacFdbFlushTable_Object = MibTableColumn
aluMdaMacFdbFlushTable = _AluMdaMacFdbFlushTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 8, 1, 3),
    _AluMdaMacFdbFlushTable_Type()
)
aluMdaMacFdbFlushTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluMdaMacFdbFlushTable.setStatus("current")
_AluMdaMacFdbFlushPortID_Type = TmnxPortID
_AluMdaMacFdbFlushPortID_Object = MibTableColumn
aluMdaMacFdbFlushPortID = _AluMdaMacFdbFlushPortID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 8, 1, 4),
    _AluMdaMacFdbFlushPortID_Type()
)
aluMdaMacFdbFlushPortID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluMdaMacFdbFlushPortID.setStatus("current")
_AluMdaMacFdbFlushMac_Type = MacAddress
_AluMdaMacFdbFlushMac_Object = MibTableColumn
aluMdaMacFdbFlushMac = _AluMdaMacFdbFlushMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 8, 1, 5),
    _AluMdaMacFdbFlushMac_Type()
)
aluMdaMacFdbFlushMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluMdaMacFdbFlushMac.setStatus("current")


class _AluMdaMacFdbRemoteAgeTime_Type(Integer32):
    """Custom type aluMdaMacFdbRemoteAgeTime based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_AluMdaMacFdbRemoteAgeTime_Type.__name__ = "Integer32"
_AluMdaMacFdbRemoteAgeTime_Object = MibTableColumn
aluMdaMacFdbRemoteAgeTime = _AluMdaMacFdbRemoteAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 8, 1, 6),
    _AluMdaMacFdbRemoteAgeTime_Type()
)
aluMdaMacFdbRemoteAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluMdaMacFdbRemoteAgeTime.setStatus("current")


class _AluMdaMacFdbTableSize_Type(Integer32):
    """Custom type aluMdaMacFdbTableSize based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 512),
    )


_AluMdaMacFdbTableSize_Type.__name__ = "Integer32"
_AluMdaMacFdbTableSize_Object = MibTableColumn
aluMdaMacFdbTableSize = _AluMdaMacFdbTableSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 8, 1, 7),
    _AluMdaMacFdbTableSize_Type()
)
aluMdaMacFdbTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluMdaMacFdbTableSize.setStatus("current")
_AluMdaMacFdbNumEntries_Type = Integer32
_AluMdaMacFdbNumEntries_Object = MibTableColumn
aluMdaMacFdbNumEntries = _AluMdaMacFdbNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 8, 1, 8),
    _AluMdaMacFdbNumEntries_Type()
)
aluMdaMacFdbNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMdaMacFdbNumEntries.setStatus("current")
_AluMdaMacFdbNumStaticEntries_Type = Integer32
_AluMdaMacFdbNumStaticEntries_Object = MibTableColumn
aluMdaMacFdbNumStaticEntries = _AluMdaMacFdbNumStaticEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 8, 1, 9),
    _AluMdaMacFdbNumStaticEntries_Type()
)
aluMdaMacFdbNumStaticEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMdaMacFdbNumStaticEntries.setStatus("current")


class _AluMdaMacFdbDiscardUnknownSource_Type(TmnxEnabledDisabled):
    """Custom type aluMdaMacFdbDiscardUnknownSource based on TmnxEnabledDisabled"""
    defaultValue = 2


_AluMdaMacFdbDiscardUnknownSource_Type.__name__ = "TmnxEnabledDisabled"
_AluMdaMacFdbDiscardUnknownSource_Object = MibTableColumn
aluMdaMacFdbDiscardUnknownSource = _AluMdaMacFdbDiscardUnknownSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 8, 1, 10),
    _AluMdaMacFdbDiscardUnknownSource_Type()
)
aluMdaMacFdbDiscardUnknownSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluMdaMacFdbDiscardUnknownSource.setStatus("current")


class _AluMdaMacFdbMacPinningValue1_Type(TmnxEnabledDisabled):
    """Custom type aluMdaMacFdbMacPinningValue1 based on TmnxEnabledDisabled"""
    defaultValue = 2


_AluMdaMacFdbMacPinningValue1_Type.__name__ = "TmnxEnabledDisabled"
_AluMdaMacFdbMacPinningValue1_Object = MibTableColumn
aluMdaMacFdbMacPinningValue1 = _AluMdaMacFdbMacPinningValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 8, 1, 11),
    _AluMdaMacFdbMacPinningValue1_Type()
)
aluMdaMacFdbMacPinningValue1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluMdaMacFdbMacPinningValue1.setStatus("current")


class _AluMdaMacFdbMacPinningValue2_Type(TmnxEnabledDisabled):
    """Custom type aluMdaMacFdbMacPinningValue2 based on TmnxEnabledDisabled"""
    defaultValue = 2


_AluMdaMacFdbMacPinningValue2_Type.__name__ = "TmnxEnabledDisabled"
_AluMdaMacFdbMacPinningValue2_Object = MibTableColumn
aluMdaMacFdbMacPinningValue2 = _AluMdaMacFdbMacPinningValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 8, 1, 12),
    _AluMdaMacFdbMacPinningValue2_Type()
)
aluMdaMacFdbMacPinningValue2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluMdaMacFdbMacPinningValue2.setStatus("current")


class _AluMdaMacFdbHighWaterMark_Type(Integer32):
    """Custom type aluMdaMacFdbHighWaterMark based on Integer32"""
    defaultValue = 95

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluMdaMacFdbHighWaterMark_Type.__name__ = "Integer32"
_AluMdaMacFdbHighWaterMark_Object = MibTableColumn
aluMdaMacFdbHighWaterMark = _AluMdaMacFdbHighWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 8, 1, 13),
    _AluMdaMacFdbHighWaterMark_Type()
)
aluMdaMacFdbHighWaterMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluMdaMacFdbHighWaterMark.setStatus("current")
_AluMdaMacFdbTable_Object = MibTable
aluMdaMacFdbTable = _AluMdaMacFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 9)
)
if mibBuilder.loadTexts:
    aluMdaMacFdbTable.setStatus("current")
_AluMdaMacFdbEntry_Object = MibTableRow
aluMdaMacFdbEntry = _AluMdaMacFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 9, 1)
)
aluMdaMacFdbEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
    (0, "ALU-CHASSIS-MIB", "aluMdaMacFdbMacAddr"),
)
if mibBuilder.loadTexts:
    aluMdaMacFdbEntry.setStatus("current")
_AluMdaMacFdbMacAddr_Type = MacAddress
_AluMdaMacFdbMacAddr_Object = MibTableColumn
aluMdaMacFdbMacAddr = _AluMdaMacFdbMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 9, 1, 1),
    _AluMdaMacFdbMacAddr_Type()
)
aluMdaMacFdbMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMdaMacFdbMacAddr.setStatus("current")
_AluMdaMacFdbRowStatus_Type = RowStatus
_AluMdaMacFdbRowStatus_Object = MibTableColumn
aluMdaMacFdbRowStatus = _AluMdaMacFdbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 9, 1, 2),
    _AluMdaMacFdbRowStatus_Type()
)
aluMdaMacFdbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMdaMacFdbRowStatus.setStatus("current")


class _AluMdaMacFdbType_Type(Integer32):
    """Custom type aluMdaMacFdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("learned", 2),
          ("host", 3))
    )


_AluMdaMacFdbType_Type.__name__ = "Integer32"
_AluMdaMacFdbType_Object = MibTableColumn
aluMdaMacFdbType = _AluMdaMacFdbType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 9, 1, 3),
    _AluMdaMacFdbType_Type()
)
aluMdaMacFdbType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMdaMacFdbType.setStatus("current")
_AluMdaMacFdbPortID_Type = TmnxPortID
_AluMdaMacFdbPortID_Object = MibTableColumn
aluMdaMacFdbPortID = _AluMdaMacFdbPortID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 9, 1, 4),
    _AluMdaMacFdbPortID_Type()
)
aluMdaMacFdbPortID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMdaMacFdbPortID.setStatus("current")
_AluSecQueueStatsTable_Object = MibTable
aluSecQueueStatsTable = _AluSecQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 10)
)
if mibBuilder.loadTexts:
    aluSecQueueStatsTable.setStatus("current")
_AluSecQueueStatsEntry_Object = MibTableRow
aluSecQueueStatsEntry = _AluSecQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 10, 1)
)
aluSecQueueStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
    (0, "ALU-CHASSIS-MIB", "aluSecQueueId"),
    (0, "ALU-CHASSIS-MIB", "aluSecType"),
)
if mibBuilder.loadTexts:
    aluSecQueueStatsEntry.setStatus("current")
_AluSecQueueId_Type = AluSecQueueId
_AluSecQueueId_Object = MibTableColumn
aluSecQueueId = _AluSecQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 10, 1, 1),
    _AluSecQueueId_Type()
)
aluSecQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecQueueId.setStatus("current")
_AluSecQueueMode_Type = TQueueMode
_AluSecQueueMode_Object = MibTableColumn
aluSecQueueMode = _AluSecQueueMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 10, 1, 2),
    _AluSecQueueMode_Type()
)
aluSecQueueMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecQueueMode.setStatus("current")
_AluSecQueueFwdHiPrioPkts_Type = Counter64
_AluSecQueueFwdHiPrioPkts_Object = MibTableColumn
aluSecQueueFwdHiPrioPkts = _AluSecQueueFwdHiPrioPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 10, 1, 3),
    _AluSecQueueFwdHiPrioPkts_Type()
)
aluSecQueueFwdHiPrioPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecQueueFwdHiPrioPkts.setStatus("current")
_AluSecQueueFwdLowPrioPkts_Type = Counter64
_AluSecQueueFwdLowPrioPkts_Object = MibTableColumn
aluSecQueueFwdLowPrioPkts = _AluSecQueueFwdLowPrioPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 10, 1, 4),
    _AluSecQueueFwdLowPrioPkts_Type()
)
aluSecQueueFwdLowPrioPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecQueueFwdLowPrioPkts.setStatus("current")
_AluSecQueueFwdHiPrioBytes_Type = Counter64
_AluSecQueueFwdHiPrioBytes_Object = MibTableColumn
aluSecQueueFwdHiPrioBytes = _AluSecQueueFwdHiPrioBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 10, 1, 5),
    _AluSecQueueFwdHiPrioBytes_Type()
)
aluSecQueueFwdHiPrioBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecQueueFwdHiPrioBytes.setStatus("current")
_AluSecQueueFwdLowPrioBytes_Type = Counter64
_AluSecQueueFwdLowPrioBytes_Object = MibTableColumn
aluSecQueueFwdLowPrioBytes = _AluSecQueueFwdLowPrioBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 10, 1, 6),
    _AluSecQueueFwdLowPrioBytes_Type()
)
aluSecQueueFwdLowPrioBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecQueueFwdLowPrioBytes.setStatus("current")
_AluSecQueueDroHiPrioPkts_Type = Counter64
_AluSecQueueDroHiPrioPkts_Object = MibTableColumn
aluSecQueueDroHiPrioPkts = _AluSecQueueDroHiPrioPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 10, 1, 7),
    _AluSecQueueDroHiPrioPkts_Type()
)
aluSecQueueDroHiPrioPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecQueueDroHiPrioPkts.setStatus("current")
_AluSecQueueDroLowPrioPkts_Type = Counter64
_AluSecQueueDroLowPrioPkts_Object = MibTableColumn
aluSecQueueDroLowPrioPkts = _AluSecQueueDroLowPrioPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 10, 1, 8),
    _AluSecQueueDroLowPrioPkts_Type()
)
aluSecQueueDroLowPrioPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecQueueDroLowPrioPkts.setStatus("current")
_AluSecQueueDroHiPrioBytes_Type = Counter64
_AluSecQueueDroHiPrioBytes_Object = MibTableColumn
aluSecQueueDroHiPrioBytes = _AluSecQueueDroHiPrioBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 10, 1, 9),
    _AluSecQueueDroHiPrioBytes_Type()
)
aluSecQueueDroHiPrioBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecQueueDroHiPrioBytes.setStatus("current")
_AluSecQueueDroLowPrioBytes_Type = Counter64
_AluSecQueueDroLowPrioBytes_Object = MibTableColumn
aluSecQueueDroLowPrioBytes = _AluSecQueueDroLowPrioBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 10, 1, 10),
    _AluSecQueueDroLowPrioBytes_Type()
)
aluSecQueueDroLowPrioBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecQueueDroLowPrioBytes.setStatus("current")
_AluSecQueueFwdInProfPkts_Type = Counter64
_AluSecQueueFwdInProfPkts_Object = MibTableColumn
aluSecQueueFwdInProfPkts = _AluSecQueueFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 10, 1, 11),
    _AluSecQueueFwdInProfPkts_Type()
)
aluSecQueueFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecQueueFwdInProfPkts.setStatus("current")
_AluSecQueueFwdOutProfPkts_Type = Counter64
_AluSecQueueFwdOutProfPkts_Object = MibTableColumn
aluSecQueueFwdOutProfPkts = _AluSecQueueFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 10, 1, 12),
    _AluSecQueueFwdOutProfPkts_Type()
)
aluSecQueueFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecQueueFwdOutProfPkts.setStatus("current")
_AluSecQueueFwdInProfBytes_Type = Counter64
_AluSecQueueFwdInProfBytes_Object = MibTableColumn
aluSecQueueFwdInProfBytes = _AluSecQueueFwdInProfBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 10, 1, 13),
    _AluSecQueueFwdInProfBytes_Type()
)
aluSecQueueFwdInProfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecQueueFwdInProfBytes.setStatus("current")
_AluSecQueueFwdOutProfBytes_Type = Counter64
_AluSecQueueFwdOutProfBytes_Object = MibTableColumn
aluSecQueueFwdOutProfBytes = _AluSecQueueFwdOutProfBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 10, 1, 14),
    _AluSecQueueFwdOutProfBytes_Type()
)
aluSecQueueFwdOutProfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecQueueFwdOutProfBytes.setStatus("current")
_AluSecQueueDroInProfPkts_Type = Counter64
_AluSecQueueDroInProfPkts_Object = MibTableColumn
aluSecQueueDroInProfPkts = _AluSecQueueDroInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 10, 1, 15),
    _AluSecQueueDroInProfPkts_Type()
)
aluSecQueueDroInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecQueueDroInProfPkts.setStatus("current")
_AluSecQueueDroOutProfPkts_Type = Counter64
_AluSecQueueDroOutProfPkts_Object = MibTableColumn
aluSecQueueDroOutProfPkts = _AluSecQueueDroOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 10, 1, 16),
    _AluSecQueueDroOutProfPkts_Type()
)
aluSecQueueDroOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecQueueDroOutProfPkts.setStatus("current")
_AluSecQueueDroInProfBytes_Type = Counter64
_AluSecQueueDroInProfBytes_Object = MibTableColumn
aluSecQueueDroInProfBytes = _AluSecQueueDroInProfBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 10, 1, 17),
    _AluSecQueueDroInProfBytes_Type()
)
aluSecQueueDroInProfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecQueueDroInProfBytes.setStatus("current")
_AluSecQueueDroOutProfBytes_Type = Counter64
_AluSecQueueDroOutProfBytes_Object = MibTableColumn
aluSecQueueDroOutProfBytes = _AluSecQueueDroOutProfBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 10, 1, 18),
    _AluSecQueueDroOutProfBytes_Type()
)
aluSecQueueDroOutProfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSecQueueDroOutProfBytes.setStatus("current")
_AluSecType_Type = AluSecType
_AluSecType_Object = MibTableColumn
aluSecType = _AluSecType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 10, 1, 19),
    _AluSecType_Type()
)
aluSecType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSecType.setStatus("current")
_AluIPsecCtrlQueueStatsTable_Object = MibTable
aluIPsecCtrlQueueStatsTable = _AluIPsecCtrlQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 11)
)
if mibBuilder.loadTexts:
    aluIPsecCtrlQueueStatsTable.setStatus("current")
_AluIPsecCtrlQueueStatsEntry_Object = MibTableRow
aluIPsecCtrlQueueStatsEntry = _AluIPsecCtrlQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 11, 1)
)
aluIPsecCtrlQueueStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    aluIPsecCtrlQueueStatsEntry.setStatus("current")
_AluIPsecCtrlQueueFwdPkts_Type = Counter64
_AluIPsecCtrlQueueFwdPkts_Object = MibTableColumn
aluIPsecCtrlQueueFwdPkts = _AluIPsecCtrlQueueFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 11, 1, 1),
    _AluIPsecCtrlQueueFwdPkts_Type()
)
aluIPsecCtrlQueueFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIPsecCtrlQueueFwdPkts.setStatus("current")
_AluIPsecCtrlQueueFwdBytes_Type = Counter64
_AluIPsecCtrlQueueFwdBytes_Object = MibTableColumn
aluIPsecCtrlQueueFwdBytes = _AluIPsecCtrlQueueFwdBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 11, 1, 2),
    _AluIPsecCtrlQueueFwdBytes_Type()
)
aluIPsecCtrlQueueFwdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIPsecCtrlQueueFwdBytes.setStatus("current")
_AluIPsecCtrlQueueDroPkts_Type = Counter64
_AluIPsecCtrlQueueDroPkts_Object = MibTableColumn
aluIPsecCtrlQueueDroPkts = _AluIPsecCtrlQueueDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 11, 1, 3),
    _AluIPsecCtrlQueueDroPkts_Type()
)
aluIPsecCtrlQueueDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIPsecCtrlQueueDroPkts.setStatus("current")
_AluIPsecCtrlQueueDroBytes_Type = Counter64
_AluIPsecCtrlQueueDroBytes_Object = MibTableColumn
aluIPsecCtrlQueueDroBytes = _AluIPsecCtrlQueueDroBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 11, 1, 4),
    _AluIPsecCtrlQueueDroBytes_Type()
)
aluIPsecCtrlQueueDroBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIPsecCtrlQueueDroBytes.setStatus("current")
_AluPwrEthSystemPowerInfoTable_Object = MibTable
aluPwrEthSystemPowerInfoTable = _AluPwrEthSystemPowerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 12)
)
if mibBuilder.loadTexts:
    aluPwrEthSystemPowerInfoTable.setStatus("current")
_AluPwrEthSystemPowerInfoEntry_Object = MibTableRow
aluPwrEthSystemPowerInfoEntry = _AluPwrEthSystemPowerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 12, 1)
)
aluPwrEthSystemPowerInfoEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
)
if mibBuilder.loadTexts:
    aluPwrEthSystemPowerInfoEntry.setStatus("current")
_AluPwrEthSystemMaxPowerBudget_Type = Unsigned32
_AluPwrEthSystemMaxPowerBudget_Object = MibTableColumn
aluPwrEthSystemMaxPowerBudget = _AluPwrEthSystemMaxPowerBudget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 12, 1, 1),
    _AluPwrEthSystemMaxPowerBudget_Type()
)
aluPwrEthSystemMaxPowerBudget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPwrEthSystemMaxPowerBudget.setStatus("current")
if mibBuilder.loadTexts:
    aluPwrEthSystemMaxPowerBudget.setUnits("Milliwatts")
_AluPwrEthSystemPowerCommitted_Type = Unsigned32
_AluPwrEthSystemPowerCommitted_Object = MibTableColumn
aluPwrEthSystemPowerCommitted = _AluPwrEthSystemPowerCommitted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 12, 1, 2),
    _AluPwrEthSystemPowerCommitted_Type()
)
aluPwrEthSystemPowerCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPwrEthSystemPowerCommitted.setStatus("current")
if mibBuilder.loadTexts:
    aluPwrEthSystemPowerCommitted.setUnits("Milliwatts")
_AluPwrEthSystemPowerAvailable_Type = Unsigned32
_AluPwrEthSystemPowerAvailable_Object = MibTableColumn
aluPwrEthSystemPowerAvailable = _AluPwrEthSystemPowerAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 12, 1, 3),
    _AluPwrEthSystemPowerAvailable_Type()
)
aluPwrEthSystemPowerAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPwrEthSystemPowerAvailable.setStatus("current")
if mibBuilder.loadTexts:
    aluPwrEthSystemPowerAvailable.setUnits("Milliwatts")
_AluPwrEthSystemPowerInUse_Type = Unsigned32
_AluPwrEthSystemPowerInUse_Object = MibTableColumn
aluPwrEthSystemPowerInUse = _AluPwrEthSystemPowerInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 12, 1, 4),
    _AluPwrEthSystemPowerInUse_Type()
)
aluPwrEthSystemPowerInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluPwrEthSystemPowerInUse.setStatus("current")
if mibBuilder.loadTexts:
    aluPwrEthSystemPowerInUse.setUnits("Milliwatts")
_AluChassisPowerFeedInfoTable_Object = MibTable
aluChassisPowerFeedInfoTable = _AluChassisPowerFeedInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 13)
)
if mibBuilder.loadTexts:
    aluChassisPowerFeedInfoTable.setStatus("current")
_AluChassisPowerFeedInfoEntry_Object = MibTableRow
aluChassisPowerFeedInfoEntry = _AluChassisPowerFeedInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 13, 1)
)
aluChassisPowerFeedInfoEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-CHASSIS-MIB", "aluChassisPowerSupplyId"),
)
if mibBuilder.loadTexts:
    aluChassisPowerFeedInfoEntry.setStatus("current")


class _AluChassisPowerSupplyId_Type(Unsigned32):
    """Custom type aluChassisPowerSupplyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AluChassisPowerSupplyId_Type.__name__ = "Unsigned32"
_AluChassisPowerSupplyId_Object = MibTableColumn
aluChassisPowerSupplyId = _AluChassisPowerSupplyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 13, 1, 1),
    _AluChassisPowerSupplyId_Type()
)
aluChassisPowerSupplyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluChassisPowerSupplyId.setStatus("current")


class _AluChassisPowerFeedMonitoring_Type(TmnxEnabledDisabled):
    """Custom type aluChassisPowerFeedMonitoring based on TmnxEnabledDisabled"""
    defaultValue = 1


_AluChassisPowerFeedMonitoring_Type.__name__ = "TmnxEnabledDisabled"
_AluChassisPowerFeedMonitoring_Object = MibTableColumn
aluChassisPowerFeedMonitoring = _AluChassisPowerFeedMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 13, 1, 2),
    _AluChassisPowerFeedMonitoring_Type()
)
aluChassisPowerFeedMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluChassisPowerFeedMonitoring.setStatus("current")
_AluChassisSystemIdTable_Object = MibTable
aluChassisSystemIdTable = _AluChassisSystemIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 14)
)
if mibBuilder.loadTexts:
    aluChassisSystemIdTable.setStatus("current")
_AluChassisSystemIdEntry_Object = MibTableRow
aluChassisSystemIdEntry = _AluChassisSystemIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 14, 1)
)
aluChassisSystemIdEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
)
if mibBuilder.loadTexts:
    aluChassisSystemIdEntry.setStatus("current")
_AluChassisSysId_Type = IpAddress
_AluChassisSysId_Object = MibTableColumn
aluChassisSysId = _AluChassisSysId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 14, 1, 1),
    _AluChassisSysId_Type()
)
aluChassisSysId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluChassisSysId.setStatus("current")
_AluMirrorQueueStatsTable_Object = MibTable
aluMirrorQueueStatsTable = _AluMirrorQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 15)
)
if mibBuilder.loadTexts:
    aluMirrorQueueStatsTable.setStatus("current")
_AluMirrorQueueStatsEntry_Object = MibTableRow
aluMirrorQueueStatsEntry = _AluMirrorQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 15, 1)
)
aluMirrorQueueStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
    (0, "ALU-CHASSIS-MIB", "aluMirrorQueueId"),
)
if mibBuilder.loadTexts:
    aluMirrorQueueStatsEntry.setStatus("current")


class _AluMirrorQueueId_Type(Integer32):
    """Custom type aluMirrorQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AluMirrorQueueId_Type.__name__ = "Integer32"
_AluMirrorQueueId_Object = MibTableColumn
aluMirrorQueueId = _AluMirrorQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 15, 1, 1),
    _AluMirrorQueueId_Type()
)
aluMirrorQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluMirrorQueueId.setStatus("current")
_AluMirrorQueueFwdInProfPkts_Type = Counter64
_AluMirrorQueueFwdInProfPkts_Object = MibTableColumn
aluMirrorQueueFwdInProfPkts = _AluMirrorQueueFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 15, 1, 2),
    _AluMirrorQueueFwdInProfPkts_Type()
)
aluMirrorQueueFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMirrorQueueFwdInProfPkts.setStatus("current")
_AluMirrorQueueFwdOutProfPkts_Type = Counter64
_AluMirrorQueueFwdOutProfPkts_Object = MibTableColumn
aluMirrorQueueFwdOutProfPkts = _AluMirrorQueueFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 15, 1, 3),
    _AluMirrorQueueFwdOutProfPkts_Type()
)
aluMirrorQueueFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMirrorQueueFwdOutProfPkts.setStatus("current")
_AluMirrorQueueFwdInProfBytes_Type = Counter64
_AluMirrorQueueFwdInProfBytes_Object = MibTableColumn
aluMirrorQueueFwdInProfBytes = _AluMirrorQueueFwdInProfBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 15, 1, 4),
    _AluMirrorQueueFwdInProfBytes_Type()
)
aluMirrorQueueFwdInProfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMirrorQueueFwdInProfBytes.setStatus("current")
_AluMirrorQueueFwdOutProfBytes_Type = Counter64
_AluMirrorQueueFwdOutProfBytes_Object = MibTableColumn
aluMirrorQueueFwdOutProfBytes = _AluMirrorQueueFwdOutProfBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 15, 1, 5),
    _AluMirrorQueueFwdOutProfBytes_Type()
)
aluMirrorQueueFwdOutProfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMirrorQueueFwdOutProfBytes.setStatus("current")
_AluMirrorQueueDroInProfPkts_Type = Counter64
_AluMirrorQueueDroInProfPkts_Object = MibTableColumn
aluMirrorQueueDroInProfPkts = _AluMirrorQueueDroInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 15, 1, 6),
    _AluMirrorQueueDroInProfPkts_Type()
)
aluMirrorQueueDroInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMirrorQueueDroInProfPkts.setStatus("current")
_AluMirrorQueueDroOutProfPkts_Type = Counter64
_AluMirrorQueueDroOutProfPkts_Object = MibTableColumn
aluMirrorQueueDroOutProfPkts = _AluMirrorQueueDroOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 15, 1, 7),
    _AluMirrorQueueDroOutProfPkts_Type()
)
aluMirrorQueueDroOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMirrorQueueDroOutProfPkts.setStatus("current")
_AluMirrorQueueDroInProfBytes_Type = Counter64
_AluMirrorQueueDroInProfBytes_Object = MibTableColumn
aluMirrorQueueDroInProfBytes = _AluMirrorQueueDroInProfBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 15, 1, 8),
    _AluMirrorQueueDroInProfBytes_Type()
)
aluMirrorQueueDroInProfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMirrorQueueDroInProfBytes.setStatus("current")
_AluMirrorQueueDroOutProfBytes_Type = Counter64
_AluMirrorQueueDroOutProfBytes_Object = MibTableColumn
aluMirrorQueueDroOutProfBytes = _AluMirrorQueueDroOutProfBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 15, 1, 9),
    _AluMirrorQueueDroOutProfBytes_Type()
)
aluMirrorQueueDroOutProfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMirrorQueueDroOutProfBytes.setStatus("current")
_AluIpTransportQueueStatsTable_Object = MibTable
aluIpTransportQueueStatsTable = _AluIpTransportQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 16)
)
if mibBuilder.loadTexts:
    aluIpTransportQueueStatsTable.setStatus("current")
_AluIpTransportQueueStatsEntry_Object = MibTableRow
aluIpTransportQueueStatsEntry = _AluIpTransportQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 16, 1)
)
aluIpTransportQueueStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
    (0, "ALU-CHASSIS-MIB", "aluIpTransportQueueId"),
)
if mibBuilder.loadTexts:
    aluIpTransportQueueStatsEntry.setStatus("current")


class _AluIpTransportQueueId_Type(Integer32):
    """Custom type aluIpTransportQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("networkIngress", 1),
          ("accessIngress", 2),
          ("serialAccessIngress", 3))
    )


_AluIpTransportQueueId_Type.__name__ = "Integer32"
_AluIpTransportQueueId_Object = MibTableColumn
aluIpTransportQueueId = _AluIpTransportQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 16, 1, 1),
    _AluIpTransportQueueId_Type()
)
aluIpTransportQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluIpTransportQueueId.setStatus("current")
_AluIpTransportQueueFwdPkts_Type = Counter64
_AluIpTransportQueueFwdPkts_Object = MibTableColumn
aluIpTransportQueueFwdPkts = _AluIpTransportQueueFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 16, 1, 2),
    _AluIpTransportQueueFwdPkts_Type()
)
aluIpTransportQueueFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportQueueFwdPkts.setStatus("current")
_AluIpTransportQueueFwdBytes_Type = Counter64
_AluIpTransportQueueFwdBytes_Object = MibTableColumn
aluIpTransportQueueFwdBytes = _AluIpTransportQueueFwdBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 16, 1, 3),
    _AluIpTransportQueueFwdBytes_Type()
)
aluIpTransportQueueFwdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportQueueFwdBytes.setStatus("current")
_AluIpTransportQueueDroPkts_Type = Counter64
_AluIpTransportQueueDroPkts_Object = MibTableColumn
aluIpTransportQueueDroPkts = _AluIpTransportQueueDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 16, 1, 4),
    _AluIpTransportQueueDroPkts_Type()
)
aluIpTransportQueueDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportQueueDroPkts.setStatus("current")
_AluIpTransportQueueDroBytes_Type = Counter64
_AluIpTransportQueueDroBytes_Object = MibTableColumn
aluIpTransportQueueDroBytes = _AluIpTransportQueueDroBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 16, 1, 5),
    _AluIpTransportQueueDroBytes_Type()
)
aluIpTransportQueueDroBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIpTransportQueueDroBytes.setStatus("current")
_AluCflowdQueueStatsTable_Object = MibTable
aluCflowdQueueStatsTable = _AluCflowdQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 17)
)
if mibBuilder.loadTexts:
    aluCflowdQueueStatsTable.setStatus("current")
_AluCflowdQueueStatsEntry_Object = MibTableRow
aluCflowdQueueStatsEntry = _AluCflowdQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 17, 1)
)
aluCflowdQueueStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    aluCflowdQueueStatsEntry.setStatus("current")
_AluCflowdQueueForwardPackets_Type = Counter64
_AluCflowdQueueForwardPackets_Object = MibTableColumn
aluCflowdQueueForwardPackets = _AluCflowdQueueForwardPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 17, 1, 1),
    _AluCflowdQueueForwardPackets_Type()
)
aluCflowdQueueForwardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluCflowdQueueForwardPackets.setStatus("current")
_AluCflowdQueueForwardBytes_Type = Counter64
_AluCflowdQueueForwardBytes_Object = MibTableColumn
aluCflowdQueueForwardBytes = _AluCflowdQueueForwardBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 17, 1, 2),
    _AluCflowdQueueForwardBytes_Type()
)
aluCflowdQueueForwardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluCflowdQueueForwardBytes.setStatus("current")
_AluCflowdQueueDropPackets_Type = Counter64
_AluCflowdQueueDropPackets_Object = MibTableColumn
aluCflowdQueueDropPackets = _AluCflowdQueueDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 17, 1, 3),
    _AluCflowdQueueDropPackets_Type()
)
aluCflowdQueueDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluCflowdQueueDropPackets.setStatus("current")
_AluCflowdQueueDropBytes_Type = Counter64
_AluCflowdQueueDropBytes_Object = MibTableColumn
aluCflowdQueueDropBytes = _AluCflowdQueueDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 1, 17, 1, 4),
    _AluCflowdQueueDropBytes_Type()
)
aluCflowdQueueDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluCflowdQueueDropBytes.setStatus("current")
_AluCardObjs_ObjectIdentity = ObjectIdentity
aluCardObjs = _AluCardObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 3)
)
_AluExtTmnxCpmCardTable_Object = MibTable
aluExtTmnxCpmCardTable = _AluExtTmnxCpmCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 3, 4)
)
if mibBuilder.loadTexts:
    aluExtTmnxCpmCardTable.setStatus("current")
_AluExtTmnxCpmCardEntry_Object = MibTableRow
aluExtTmnxCpmCardEntry = _AluExtTmnxCpmCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 3, 4, 1)
)
if mibBuilder.loadTexts:
    aluExtTmnxCpmCardEntry.setStatus("current")


class _AluExtCpmCardUpgrade_Type(TmnxActionType):
    """Custom type aluExtCpmCardUpgrade based on TmnxActionType"""
    defaultValue = 2


_AluExtCpmCardUpgrade_Type.__name__ = "TmnxActionType"
_AluExtCpmCardUpgrade_Object = MibTableColumn
aluExtCpmCardUpgrade = _AluExtCpmCardUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 3, 4, 1, 1),
    _AluExtCpmCardUpgrade_Type()
)
aluExtCpmCardUpgrade.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluExtCpmCardUpgrade.setStatus("current")
_AluChassisNotificationObjects_ObjectIdentity = ObjectIdentity
aluChassisNotificationObjects = _AluChassisNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 6)
)
_AluChassisNotifyMdaRuntimeStatusContext_Type = DisplayString
_AluChassisNotifyMdaRuntimeStatusContext_Object = MibScalar
aluChassisNotifyMdaRuntimeStatusContext = _AluChassisNotifyMdaRuntimeStatusContext_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 6, 1),
    _AluChassisNotifyMdaRuntimeStatusContext_Type()
)
aluChassisNotifyMdaRuntimeStatusContext.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluChassisNotifyMdaRuntimeStatusContext.setStatus("current")
_AluSyncObjs_ObjectIdentity = ObjectIdentity
aluSyncObjs = _AluSyncObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4)
)
_AluSyncExtensionObjs_ObjectIdentity = ObjectIdentity
aluSyncExtensionObjs = _AluSyncExtensionObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1)
)
_AluExtIfSyncIfTimingExtensionTable_Object = MibTable
aluExtIfSyncIfTimingExtensionTable = _AluExtIfSyncIfTimingExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    aluExtIfSyncIfTimingExtensionTable.setStatus("current")
_AluExtIfSyncIfTimingExtensionEntry_Object = MibTableRow
aluExtIfSyncIfTimingExtensionEntry = _AluExtIfSyncIfTimingExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    aluExtIfSyncIfTimingExtensionEntry.setStatus("current")
_AluSyncIfTimingExternInIfType_Type = AluExternalIfType
_AluSyncIfTimingExternInIfType_Object = MibTableColumn
aluSyncIfTimingExternInIfType = _AluSyncIfTimingExternInIfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 1),
    _AluSyncIfTimingExternInIfType_Type()
)
aluSyncIfTimingExternInIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingExternInIfType.setStatus("current")
_AluSyncIfTimingExternInImpedType_Type = AluExternalInputImpedanceType
_AluSyncIfTimingExternInImpedType_Object = MibTableColumn
aluSyncIfTimingExternInImpedType = _AluSyncIfTimingExternInImpedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 2),
    _AluSyncIfTimingExternInImpedType_Type()
)
aluSyncIfTimingExternInImpedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingExternInImpedType.setStatus("current")
_AluSyncIfTimingExternOutIfType_Type = AluExternalIfType
_AluSyncIfTimingExternOutIfType_Object = MibTableColumn
aluSyncIfTimingExternOutIfType = _AluSyncIfTimingExternOutIfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 3),
    _AluSyncIfTimingExternOutIfType_Type()
)
aluSyncIfTimingExternOutIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingExternOutIfType.setStatus("current")
_AluSyncIfTimingExternInIfAdminStatus_Type = TmnxPortAdminStatus
_AluSyncIfTimingExternInIfAdminStatus_Object = MibTableColumn
aluSyncIfTimingExternInIfAdminStatus = _AluSyncIfTimingExternInIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 4),
    _AluSyncIfTimingExternInIfAdminStatus_Type()
)
aluSyncIfTimingExternInIfAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingExternInIfAdminStatus.setStatus("current")
_AluSyncIfTimingExternInIfInUse_Type = TruthValue
_AluSyncIfTimingExternInIfInUse_Object = MibTableColumn
aluSyncIfTimingExternInIfInUse = _AluSyncIfTimingExternInIfInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 5),
    _AluSyncIfTimingExternInIfInUse_Type()
)
aluSyncIfTimingExternInIfInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingExternInIfInUse.setStatus("current")
_AluSyncIfTimingExternInIfQualified_Type = TmnxSETSRefQualified
_AluSyncIfTimingExternInIfQualified_Object = MibTableColumn
aluSyncIfTimingExternInIfQualified = _AluSyncIfTimingExternInIfQualified_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 6),
    _AluSyncIfTimingExternInIfQualified_Type()
)
aluSyncIfTimingExternInIfQualified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingExternInIfQualified.setStatus("current")
_AluSyncIfTimingExternInIfAlarm_Type = TmnxSETSRefAlarm
_AluSyncIfTimingExternInIfAlarm_Object = MibTableColumn
aluSyncIfTimingExternInIfAlarm = _AluSyncIfTimingExternInIfAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 7),
    _AluSyncIfTimingExternInIfAlarm_Type()
)
aluSyncIfTimingExternInIfAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingExternInIfAlarm.setStatus("current")
_AluSyncIfTimingRef1Ieee1588PtpSrc_Type = TNamedItemOrEmpty
_AluSyncIfTimingRef1Ieee1588PtpSrc_Object = MibTableColumn
aluSyncIfTimingRef1Ieee1588PtpSrc = _AluSyncIfTimingRef1Ieee1588PtpSrc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 8),
    _AluSyncIfTimingRef1Ieee1588PtpSrc_Type()
)
aluSyncIfTimingRef1Ieee1588PtpSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingRef1Ieee1588PtpSrc.setStatus("obsolete")
_AluSyncIfTimingRef2Ieee1588PtpSrc_Type = TNamedItemOrEmpty
_AluSyncIfTimingRef2Ieee1588PtpSrc_Object = MibTableColumn
aluSyncIfTimingRef2Ieee1588PtpSrc = _AluSyncIfTimingRef2Ieee1588PtpSrc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 9),
    _AluSyncIfTimingRef2Ieee1588PtpSrc_Type()
)
aluSyncIfTimingRef2Ieee1588PtpSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingRef2Ieee1588PtpSrc.setStatus("obsolete")
_AluSyncIfTimingIeee1588PtpType_Type = AluSyncIfTimingIeee1588PtpType
_AluSyncIfTimingIeee1588PtpType_Object = MibTableColumn
aluSyncIfTimingIeee1588PtpType = _AluSyncIfTimingIeee1588PtpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 10),
    _AluSyncIfTimingIeee1588PtpType_Type()
)
aluSyncIfTimingIeee1588PtpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingIeee1588PtpType.setStatus("obsolete")
_AluSyncIfTimingExternInCfgQltyLevel_Type = TmnxSSMQualityLevel
_AluSyncIfTimingExternInCfgQltyLevel_Object = MibTableColumn
aluSyncIfTimingExternInCfgQltyLevel = _AluSyncIfTimingExternInCfgQltyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 11),
    _AluSyncIfTimingExternInCfgQltyLevel_Type()
)
aluSyncIfTimingExternInCfgQltyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingExternInCfgQltyLevel.setStatus("current")
_AluSyncIfTimingExternInState_Type = TmnxRefInState
_AluSyncIfTimingExternInState_Object = MibTableColumn
aluSyncIfTimingExternInState = _AluSyncIfTimingExternInState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 12),
    _AluSyncIfTimingExternInState_Type()
)
aluSyncIfTimingExternInState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingExternInState.setStatus("current")


class _AluSyncIfTimingRef1SrcPtpClock_Type(Unsigned32):
    """Custom type aluSyncIfTimingRef1SrcPtpClock based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AluSyncIfTimingRef1SrcPtpClock_Type.__name__ = "Unsigned32"
_AluSyncIfTimingRef1SrcPtpClock_Object = MibTableColumn
aluSyncIfTimingRef1SrcPtpClock = _AluSyncIfTimingRef1SrcPtpClock_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 13),
    _AluSyncIfTimingRef1SrcPtpClock_Type()
)
aluSyncIfTimingRef1SrcPtpClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingRef1SrcPtpClock.setStatus("current")


class _AluSyncIfTimingRef2SrcPtpClock_Type(Unsigned32):
    """Custom type aluSyncIfTimingRef2SrcPtpClock based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AluSyncIfTimingRef2SrcPtpClock_Type.__name__ = "Unsigned32"
_AluSyncIfTimingRef2SrcPtpClock_Object = MibTableColumn
aluSyncIfTimingRef2SrcPtpClock = _AluSyncIfTimingRef2SrcPtpClock_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 1, 1, 14),
    _AluSyncIfTimingRef2SrcPtpClock_Type()
)
aluSyncIfTimingRef2SrcPtpClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingRef2SrcPtpClock.setStatus("current")
_AluExtIfSyncIfTimingAdmExtensionTable_Object = MibTable
aluExtIfSyncIfTimingAdmExtensionTable = _AluExtIfSyncIfTimingAdmExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    aluExtIfSyncIfTimingAdmExtensionTable.setStatus("current")
_AluExtIfSyncIfTimingAdmExtensionEntry_Object = MibTableRow
aluExtIfSyncIfTimingAdmExtensionEntry = _AluExtIfSyncIfTimingAdmExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aluExtIfSyncIfTimingAdmExtensionEntry.setStatus("current")


class _AluSyncIfTimingAdmExternInIfType_Type(AluExternalIfType):
    """Custom type aluSyncIfTimingAdmExternInIfType based on AluExternalIfType"""
    defaultValue = 1


_AluSyncIfTimingAdmExternInIfType_Type.__name__ = "AluExternalIfType"
_AluSyncIfTimingAdmExternInIfType_Object = MibTableColumn
aluSyncIfTimingAdmExternInIfType = _AluSyncIfTimingAdmExternInIfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 2, 1, 1),
    _AluSyncIfTimingAdmExternInIfType_Type()
)
aluSyncIfTimingAdmExternInIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSyncIfTimingAdmExternInIfType.setStatus("current")


class _AluSyncIfTimingAdmExternInImpedType_Type(AluExternalInputImpedanceType):
    """Custom type aluSyncIfTimingAdmExternInImpedType based on AluExternalInputImpedanceType"""
    defaultValue = 2


_AluSyncIfTimingAdmExternInImpedType_Type.__name__ = "AluExternalInputImpedanceType"
_AluSyncIfTimingAdmExternInImpedType_Object = MibTableColumn
aluSyncIfTimingAdmExternInImpedType = _AluSyncIfTimingAdmExternInImpedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 2, 1, 2),
    _AluSyncIfTimingAdmExternInImpedType_Type()
)
aluSyncIfTimingAdmExternInImpedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSyncIfTimingAdmExternInImpedType.setStatus("current")


class _AluSyncIfTimingAdmExternOutIfType_Type(AluExternalIfType):
    """Custom type aluSyncIfTimingAdmExternOutIfType based on AluExternalIfType"""
    defaultValue = 1


_AluSyncIfTimingAdmExternOutIfType_Type.__name__ = "AluExternalIfType"
_AluSyncIfTimingAdmExternOutIfType_Object = MibTableColumn
aluSyncIfTimingAdmExternOutIfType = _AluSyncIfTimingAdmExternOutIfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 2, 1, 3),
    _AluSyncIfTimingAdmExternOutIfType_Type()
)
aluSyncIfTimingAdmExternOutIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSyncIfTimingAdmExternOutIfType.setStatus("current")


class _AluSyncIfTimingAdmExternInIfAdminStatus_Type(TmnxPortAdminStatus):
    """Custom type aluSyncIfTimingAdmExternInIfAdminStatus based on TmnxPortAdminStatus"""
    defaultValue = 3


_AluSyncIfTimingAdmExternInIfAdminStatus_Type.__name__ = "TmnxPortAdminStatus"
_AluSyncIfTimingAdmExternInIfAdminStatus_Object = MibTableColumn
aluSyncIfTimingAdmExternInIfAdminStatus = _AluSyncIfTimingAdmExternInIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 2, 1, 4),
    _AluSyncIfTimingAdmExternInIfAdminStatus_Type()
)
aluSyncIfTimingAdmExternInIfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSyncIfTimingAdmExternInIfAdminStatus.setStatus("current")


class _AluSyncIfTimingAdmRef1Ieee1588PtpSrc_Type(TNamedItemOrEmpty):
    """Custom type aluSyncIfTimingAdmRef1Ieee1588PtpSrc based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_AluSyncIfTimingAdmRef1Ieee1588PtpSrc_Type.__name__ = "TNamedItemOrEmpty"
_AluSyncIfTimingAdmRef1Ieee1588PtpSrc_Object = MibTableColumn
aluSyncIfTimingAdmRef1Ieee1588PtpSrc = _AluSyncIfTimingAdmRef1Ieee1588PtpSrc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 2, 1, 5),
    _AluSyncIfTimingAdmRef1Ieee1588PtpSrc_Type()
)
aluSyncIfTimingAdmRef1Ieee1588PtpSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSyncIfTimingAdmRef1Ieee1588PtpSrc.setStatus("obsolete")


class _AluSyncIfTimingAdmRef2Ieee1588PtpSrc_Type(TNamedItemOrEmpty):
    """Custom type aluSyncIfTimingAdmRef2Ieee1588PtpSrc based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_AluSyncIfTimingAdmRef2Ieee1588PtpSrc_Type.__name__ = "TNamedItemOrEmpty"
_AluSyncIfTimingAdmRef2Ieee1588PtpSrc_Object = MibTableColumn
aluSyncIfTimingAdmRef2Ieee1588PtpSrc = _AluSyncIfTimingAdmRef2Ieee1588PtpSrc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 2, 1, 6),
    _AluSyncIfTimingAdmRef2Ieee1588PtpSrc_Type()
)
aluSyncIfTimingAdmRef2Ieee1588PtpSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSyncIfTimingAdmRef2Ieee1588PtpSrc.setStatus("obsolete")


class _AluSyncIfTimingAdmExternInCfgQltyLevel_Type(TmnxSSMQualityLevel):
    """Custom type aluSyncIfTimingAdmExternInCfgQltyLevel based on TmnxSSMQualityLevel"""
    defaultValue = 2


_AluSyncIfTimingAdmExternInCfgQltyLevel_Type.__name__ = "TmnxSSMQualityLevel"
_AluSyncIfTimingAdmExternInCfgQltyLevel_Object = MibTableColumn
aluSyncIfTimingAdmExternInCfgQltyLevel = _AluSyncIfTimingAdmExternInCfgQltyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 2, 1, 7),
    _AluSyncIfTimingAdmExternInCfgQltyLevel_Type()
)
aluSyncIfTimingAdmExternInCfgQltyLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSyncIfTimingAdmExternInCfgQltyLevel.setStatus("current")


class _AluSyncIfTimingAdmRef1SrcPtpClock_Type(Unsigned32):
    """Custom type aluSyncIfTimingAdmRef1SrcPtpClock based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AluSyncIfTimingAdmRef1SrcPtpClock_Type.__name__ = "Unsigned32"
_AluSyncIfTimingAdmRef1SrcPtpClock_Object = MibTableColumn
aluSyncIfTimingAdmRef1SrcPtpClock = _AluSyncIfTimingAdmRef1SrcPtpClock_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 2, 1, 8),
    _AluSyncIfTimingAdmRef1SrcPtpClock_Type()
)
aluSyncIfTimingAdmRef1SrcPtpClock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSyncIfTimingAdmRef1SrcPtpClock.setStatus("current")


class _AluSyncIfTimingAdmRef2SrcPtpClock_Type(Unsigned32):
    """Custom type aluSyncIfTimingAdmRef2SrcPtpClock based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AluSyncIfTimingAdmRef2SrcPtpClock_Type.__name__ = "Unsigned32"
_AluSyncIfTimingAdmRef2SrcPtpClock_Object = MibTableColumn
aluSyncIfTimingAdmRef2SrcPtpClock = _AluSyncIfTimingAdmRef2SrcPtpClock_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 2, 1, 9),
    _AluSyncIfTimingAdmRef2SrcPtpClock_Type()
)
aluSyncIfTimingAdmRef2SrcPtpClock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSyncIfTimingAdmRef2SrcPtpClock.setStatus("current")


class _AluSyncIfTimingAdmChangedMask_Type(Bits):
    """Custom type aluSyncIfTimingAdmChangedMask based on Bits"""
    namedValues = NamedValues(
        *(("aluSyncIfTimingAdmExternInIfType", 0),
          ("aluSyncIfTimingAdmExternInImpedType", 1),
          ("aluSyncIfTimingAdmExternOutIfType", 2),
          ("aluSyncIfTimingAdmExternInIfAdminStatus", 3),
          ("aluSyncIfTimingAdmRef1Ieee1588PtpSrc", 4),
          ("aluSyncIfTimingAdmRef2Ieee1588PtpSrc", 5),
          ("aluSyncIfTimingAdmExternInCfgQltyLevel", 6),
          ("aluSyncIfTimingAdmRef1SrcPtpClock", 7),
          ("aluSyncIfTimingAdmRef2SrcPtpClock", 8),
          ("aluSyncIfTimingAdmChangedMask", 9))
    )

_AluSyncIfTimingAdmChangedMask_Type.__name__ = "Bits"
_AluSyncIfTimingAdmChangedMask_Object = MibTableColumn
aluSyncIfTimingAdmChangedMask = _AluSyncIfTimingAdmChangedMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 4, 1, 2, 1, 10),
    _AluSyncIfTimingAdmChangedMask_Type()
)
aluSyncIfTimingAdmChangedMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSyncIfTimingAdmChangedMask.setStatus("current")
_AluHwNotification_ObjectIdentity = ObjectIdentity
aluHwNotification = _AluHwNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2)
)
_AluChassisNotifyPrefix_ObjectIdentity = ObjectIdentity
aluChassisNotifyPrefix = _AluChassisNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1)
)
_AluChassisNotification_ObjectIdentity = ObjectIdentity
aluChassisNotification = _AluChassisNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0)
)
_AluSetsNotifyPrefix_ObjectIdentity = ObjectIdentity
aluSetsNotifyPrefix = _AluSetsNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 4)
)
tmnxMDAEntry.registerAugmentions(
    ("ALU-CHASSIS-MIB",
     "aluExtTmnxMDAEntry")
)
aluExtTmnxMDAEntry.setIndexNames(*tmnxMDAEntry.getIndexNames())
tmnxCpmCardEntry.registerAugmentions(
    ("ALU-CHASSIS-MIB",
     "aluExtTmnxCpmCardEntry")
)
aluExtTmnxCpmCardEntry.setIndexNames(*tmnxCpmCardEntry.getIndexNames())
tmnxCpmCardEntry.registerAugmentions(
    ("ALU-CHASSIS-MIB",
     "aluExtIfSyncIfTimingExtensionEntry")
)
aluExtIfSyncIfTimingExtensionEntry.setIndexNames(*tmnxCpmCardEntry.getIndexNames())
tSyncIfTimingAdmEntry.registerAugmentions(
    ("ALU-CHASSIS-MIB",
     "aluExtIfSyncIfTimingAdmExtensionEntry")
)
aluExtIfSyncIfTimingAdmExtensionEntry.setIndexNames(*tSyncIfTimingAdmEntry.getIndexNames())

# Managed Objects groups

aluFamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 1)
)
aluFamGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluFamOperStatus"),
        ("ALU-CHASSIS-MIB", "aluFamHwIndex"),
        ("ALU-CHASSIS-MIB", "aluFamEquippedType"))
)
if mibBuilder.loadTexts:
    aluFamGroup.setStatus("current")

aluExtAlarmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 2)
)
aluExtAlarmsGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluChassisExtAlarmState"),
        ("ALU-CHASSIS-MIB", "aluChassisExtAlarmEvent"),
        ("ALU-CHASSIS-MIB", "aluChassisExtAlarmPin"))
)
if mibBuilder.loadTexts:
    aluExtAlarmsGroup.setStatus("current")

aluPlatformHwClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 4)
)
aluPlatformHwClassGroup.setObjects(
    ("ALU-CHASSIS-MIB", "aluExtPlatformHwClass")
)
if mibBuilder.loadTexts:
    aluPlatformHwClassGroup.setStatus("current")

aluHwBgDiagsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 5)
)
aluHwBgDiagsGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluExtHwBgDiagsState"),
        ("ALU-CHASSIS-MIB", "aluExtHwBgDiagsFaultReason"))
)
if mibBuilder.loadTexts:
    aluHwBgDiagsGroup.setStatus("current")

aluExternalTimingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 7)
)
aluExternalTimingGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluSyncIfTimingExternInIfType"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingExternInImpedType"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingExternOutIfType"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingExternInIfAdminStatus"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingExternInIfInUse"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingExternInIfQualified"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingExternInIfAlarm"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingAdmExternInIfType"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingAdmExternInImpedType"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingAdmExternOutIfType"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingAdmExternInIfAdminStatus"))
)
if mibBuilder.loadTexts:
    aluExternalTimingGroup.setStatus("current")

aluExtCpmCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 9)
)
aluExtCpmCardGroup.setObjects(
    ("ALU-CHASSIS-MIB", "aluExtCpmCardUpgrade")
)
if mibBuilder.loadTexts:
    aluExtCpmCardGroup.setStatus("current")

aluExtMDAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 11)
)
aluExtMDAGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluExtTmnxMDANetworkIngFabricPolicy"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAAccessIngFabricPolicy"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAFabricStatsEnabled"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAVoiceCompandingLaw"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAVoiceSignalingType"))
)
if mibBuilder.loadTexts:
    aluExtMDAGroup.setStatus("obsolete")

aluFabricDeviceStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 12)
)
aluFabricDeviceStatsGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluFabricDeviceStatsFwdPkts"),
        ("ALU-CHASSIS-MIB", "aluFabricDeviceStatsDroPkts"),
        ("ALU-CHASSIS-MIB", "aluFabricDeviceStatsFwdOcts"))
)
if mibBuilder.loadTexts:
    aluFabricDeviceStatsGroup.setStatus("obsolete")

aluSourceMDAStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 13)
)
aluSourceMDAStatsGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluSourceMDAStatsFwdInProfPkts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsFwdOutProfPkts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsFwdInProfOcts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsFwdOutProfOcts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsDroInProfPkts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsDroOutProfPkts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsDroInProfOcts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsDroOutProfOcts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsAccessFwdInProfPkts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsAccessFwdOutProfPkts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsAccessFwdInProfOcts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsAccessFwdOutProfOcts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsAccessDroPkts"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsAccessDroOcts"))
)
if mibBuilder.loadTexts:
    aluSourceMDAStatsGroup.setStatus("current")

aluDestMDAStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 14)
)
aluDestMDAStatsGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluDestMDAStatsFwdInProfPkts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsFwdOutProfPkts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsFwdInProfOcts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsFwdOutProfOcts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsDroInProfPkts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsDroOutProfPkts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsDroInProfOcts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsDroOutProfOcts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsAccessFwdInProfPkts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsAccessFwdOutProfPkts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsAccessFwdInProfOcts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsAccessFwdOutProfOcts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsAccessDroPkts"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsAccessDroOcts"))
)
if mibBuilder.loadTexts:
    aluDestMDAStatsGroup.setStatus("current")

alu1588PtpTimingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 16)
)
alu1588PtpTimingGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluSyncIfTimingIeee1588PtpType"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingRef1Ieee1588PtpSrc"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingRef2Ieee1588PtpSrc"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingAdmRef1Ieee1588PtpSrc"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingAdmRef2Ieee1588PtpSrc"))
)
if mibBuilder.loadTexts:
    alu1588PtpTimingGroup.setStatus("obsolete")

aluEqMdaRuntimeNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 17)
)
aluEqMdaRuntimeNotifyObjsGroup.setObjects(
    ("ALU-CHASSIS-MIB", "aluChassisNotifyMdaRuntimeStatusContext")
)
if mibBuilder.loadTexts:
    aluEqMdaRuntimeNotifyObjsGroup.setStatus("current")

aluQLRefSelectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 19)
)
aluQLRefSelectionGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluSyncIfTimingAdmExternInCfgQltyLevel"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingExternInCfgQltyLevel"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingExternInState"))
)
if mibBuilder.loadTexts:
    aluQLRefSelectionGroup.setStatus("current")

aluMDAAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 21)
)
aluMDAAlarmGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluExtTmnxMDANumOfDigitalAlarmInputs"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDANumOfAnalogAlarmInputs"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDANumOfDigitalOutputRelays"))
)
if mibBuilder.loadTexts:
    aluMDAAlarmGroup.setStatus("current")

aluFabricDeviceStatsV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 22)
)
aluFabricDeviceStatsV4v0Group.setObjects(
      *(("ALU-CHASSIS-MIB", "aluFabricDeviceStatsFwdPkts"),
        ("ALU-CHASSIS-MIB", "aluFabricDeviceStatsDroPkts"),
        ("ALU-CHASSIS-MIB", "aluFabricDeviceStatsFwdOcts"),
        ("ALU-CHASSIS-MIB", "aluFabricDeviceStatsUcastFwdPkts"),
        ("ALU-CHASSIS-MIB", "aluFabricDeviceStatsMcastFwdPkts"),
        ("ALU-CHASSIS-MIB", "aluFabricDeviceStatsDroOcts"))
)
if mibBuilder.loadTexts:
    aluFabricDeviceStatsV4v0Group.setStatus("current")

alu1588PtpTimingV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 23)
)
alu1588PtpTimingV4v0Group.setObjects(
      *(("ALU-CHASSIS-MIB", "aluSyncIfTimingRef1SrcPtpClock"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingRef2SrcPtpClock"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingAdmRef1SrcPtpClock"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingAdmRef2SrcPtpClock"))
)
if mibBuilder.loadTexts:
    alu1588PtpTimingV4v0Group.setStatus("current")

alu1588PtpTimingObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 24)
)
alu1588PtpTimingObsoleteGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluSyncIfTimingIeee1588PtpType"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingRef1Ieee1588PtpSrc"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingRef2Ieee1588PtpSrc"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingAdmRef1Ieee1588PtpSrc"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingAdmRef2Ieee1588PtpSrc"))
)
if mibBuilder.loadTexts:
    alu1588PtpTimingObsoleteGroup.setStatus("current")

aluExtMDAV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 25)
)
aluExtMDAV5v0Group.setObjects(
      *(("ALU-CHASSIS-MIB", "aluExtTmnxMDANetworkIngFabricPolicy"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAAccessIngFabricPolicy"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAFabricStatsEnabled"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAVoiceCompandingLaw"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAVoiceSignalingType"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDACapabilityMode"))
)
if mibBuilder.loadTexts:
    aluExtMDAV5v0Group.setStatus("obsolete")

aluMDAEventStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 26)
)
aluMDAEventStatsGroup.setObjects(
    ("ALU-CHASSIS-MIB", "aluFabricDeviceStatsMdaDroEvents")
)
if mibBuilder.loadTexts:
    aluMDAEventStatsGroup.setStatus("current")

aluExtHwMfgVariantGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 27)
)
aluExtHwMfgVariantGroup.setObjects(
    ("ALU-CHASSIS-MIB", "aluExtHwMfgVariant")
)
if mibBuilder.loadTexts:
    aluExtHwMfgVariantGroup.setStatus("current")

aluExtMDAV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 29)
)
aluExtMDAV6v0Group.setObjects(
      *(("ALU-CHASSIS-MIB", "aluExtTmnxMDANetworkIngFabricPolicy"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAAccessIngFabricPolicy"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAFabricStatsEnabled"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAVoiceCompandingLaw"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAVoiceSignalingType"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDACapabilityMode"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDANetworkRingQueuePolicy"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDANetworkRingQosPolicy"))
)
if mibBuilder.loadTexts:
    aluExtMDAV6v0Group.setStatus("current")

aluRingMdaV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 30)
)
aluRingMdaV6v0Group.setObjects(
      *(("ALU-CHASSIS-MIB", "aluMdaMacFdbMacLearning"),
        ("ALU-CHASSIS-MIB", "aluMdaMacFdbMacAgeing"),
        ("ALU-CHASSIS-MIB", "aluMdaMacFdbFlushTable"),
        ("ALU-CHASSIS-MIB", "aluMdaMacFdbFlushPortID"),
        ("ALU-CHASSIS-MIB", "aluMdaMacFdbFlushMac"),
        ("ALU-CHASSIS-MIB", "aluMdaMacFdbRemoteAgeTime"),
        ("ALU-CHASSIS-MIB", "aluMdaMacFdbTableSize"),
        ("ALU-CHASSIS-MIB", "aluMdaMacFdbNumEntries"),
        ("ALU-CHASSIS-MIB", "aluMdaMacFdbNumStaticEntries"),
        ("ALU-CHASSIS-MIB", "aluMdaMacFdbDiscardUnknownSource"),
        ("ALU-CHASSIS-MIB", "aluMdaMacFdbMacPinningValue1"),
        ("ALU-CHASSIS-MIB", "aluMdaMacFdbMacPinningValue2"),
        ("ALU-CHASSIS-MIB", "aluMdaMacFdbHighWaterMark"),
        ("ALU-CHASSIS-MIB", "aluMdaMacFdbMacAddr"),
        ("ALU-CHASSIS-MIB", "aluMdaMacFdbRowStatus"),
        ("ALU-CHASSIS-MIB", "aluMdaMacFdbType"),
        ("ALU-CHASSIS-MIB", "aluMdaMacFdbPortID"))
)
if mibBuilder.loadTexts:
    aluRingMdaV6v0Group.setStatus("current")

aluPwrEthPowerSupplyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 32)
)
aluPwrEthPowerSupplyGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluExtTmnxMDAPwrEthPsPowerMode"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAPwrEthPsPowerSupplyStatus"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAPwrEthPsExternalPowerSupplyStatus"))
)
if mibBuilder.loadTexts:
    aluPwrEthPowerSupplyGroup.setStatus("current")

aluSecurityStatsV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 33)
)
aluSecurityStatsV6v1Group.setObjects(
      *(("ALU-CHASSIS-MIB", "aluSecQueueMode"),
        ("ALU-CHASSIS-MIB", "aluSecQueueFwdHiPrioPkts"),
        ("ALU-CHASSIS-MIB", "aluSecQueueFwdLowPrioPkts"),
        ("ALU-CHASSIS-MIB", "aluSecQueueFwdHiPrioBytes"),
        ("ALU-CHASSIS-MIB", "aluSecQueueFwdLowPrioBytes"),
        ("ALU-CHASSIS-MIB", "aluSecQueueDroHiPrioPkts"),
        ("ALU-CHASSIS-MIB", "aluSecQueueDroLowPrioPkts"),
        ("ALU-CHASSIS-MIB", "aluSecQueueDroHiPrioBytes"),
        ("ALU-CHASSIS-MIB", "aluSecQueueDroLowPrioBytes"),
        ("ALU-CHASSIS-MIB", "aluSecQueueFwdInProfPkts"),
        ("ALU-CHASSIS-MIB", "aluSecQueueFwdOutProfPkts"),
        ("ALU-CHASSIS-MIB", "aluSecQueueFwdInProfBytes"),
        ("ALU-CHASSIS-MIB", "aluSecQueueFwdOutProfBytes"),
        ("ALU-CHASSIS-MIB", "aluSecQueueDroInProfPkts"),
        ("ALU-CHASSIS-MIB", "aluSecQueueDroOutProfPkts"),
        ("ALU-CHASSIS-MIB", "aluSecQueueDroInProfBytes"),
        ("ALU-CHASSIS-MIB", "aluSecQueueDroOutProfBytes"),
        ("ALU-CHASSIS-MIB", "aluIPsecCtrlQueueFwdPkts"),
        ("ALU-CHASSIS-MIB", "aluIPsecCtrlQueueFwdBytes"),
        ("ALU-CHASSIS-MIB", "aluIPsecCtrlQueueDroPkts"),
        ("ALU-CHASSIS-MIB", "aluIPsecCtrlQueueDroBytes"))
)
if mibBuilder.loadTexts:
    aluSecurityStatsV6v1Group.setStatus("current")

aluPwrEthSystemPowerV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 34)
)
aluPwrEthSystemPowerV6v1Group.setObjects(
      *(("ALU-CHASSIS-MIB", "aluPwrEthSystemMaxPowerBudget"),
        ("ALU-CHASSIS-MIB", "aluPwrEthSystemPowerCommitted"),
        ("ALU-CHASSIS-MIB", "aluPwrEthSystemPowerAvailable"),
        ("ALU-CHASSIS-MIB", "aluPwrEthSystemPowerInUse"))
)
if mibBuilder.loadTexts:
    aluPwrEthSystemPowerV6v1Group.setStatus("current")

aluChassisPowerFeedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 36)
)
aluChassisPowerFeedGroup.setObjects(
    ("ALU-CHASSIS-MIB", "aluChassisPowerFeedMonitoring")
)
if mibBuilder.loadTexts:
    aluChassisPowerFeedGroup.setStatus("current")

aluExtMDAV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 37)
)
aluExtMDAV7v0Group.setObjects(
      *(("ALU-CHASSIS-MIB", "aluExtTmnxMDANetworkIngSecQueuePolicy"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAAccessIngSecQueuePolicy"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDASptSecAggRate"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDATuAisEnabled"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAAccessIngShaperPolicy"))
)
if mibBuilder.loadTexts:
    aluExtMDAV7v0Group.setStatus("current")

aluChassisSysIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 38)
)
aluChassisSysIdGroup.setObjects(
    ("ALU-CHASSIS-MIB", "aluChassisSysId")
)
if mibBuilder.loadTexts:
    aluChassisSysIdGroup.setStatus("current")

aluStatsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 39)
)
aluStatsV8v0Group.setObjects(
      *(("ALU-CHASSIS-MIB", "aluMirrorQueueFwdInProfPkts"),
        ("ALU-CHASSIS-MIB", "aluMirrorQueueFwdOutProfPkts"),
        ("ALU-CHASSIS-MIB", "aluMirrorQueueFwdInProfBytes"),
        ("ALU-CHASSIS-MIB", "aluMirrorQueueFwdOutProfBytes"),
        ("ALU-CHASSIS-MIB", "aluMirrorQueueDroInProfPkts"),
        ("ALU-CHASSIS-MIB", "aluMirrorQueueDroOutProfPkts"),
        ("ALU-CHASSIS-MIB", "aluMirrorQueueDroInProfBytes"),
        ("ALU-CHASSIS-MIB", "aluMirrorQueueDroOutProfBytes"))
)
if mibBuilder.loadTexts:
    aluStatsV8v0Group.setStatus("current")

aluIpTransportQueueStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 40)
)
aluIpTransportQueueStatsGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluIpTransportQueueFwdPkts"),
        ("ALU-CHASSIS-MIB", "aluIpTransportQueueFwdBytes"),
        ("ALU-CHASSIS-MIB", "aluIpTransportQueueDroPkts"),
        ("ALU-CHASSIS-MIB", "aluIpTransportQueueDroBytes"))
)
if mibBuilder.loadTexts:
    aluIpTransportQueueStatsGroup.setStatus("current")

aluExtMDAV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 41)
)
aluExtMDAV8v0Group.setObjects(
    ("ALU-CHASSIS-MIB", "aluExtTmnxMDAVcbApplication")
)
if mibBuilder.loadTexts:
    aluExtMDAV8v0Group.setStatus("current")

aluSyncIfTimingV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 42)
)
aluSyncIfTimingV9v0Group.setObjects(
    ("ALU-CHASSIS-MIB", "aluSyncIfTimingAdmChangedMask")
)
if mibBuilder.loadTexts:
    aluSyncIfTimingV9v0Group.setStatus("current")


# Notification objects

aluEqExtAlarmDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 1)
)
aluEqExtAlarmDetected.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALU-CHASSIS-MIB", "aluChassisExtAlarmState"),
        ("ALU-CHASSIS-MIB", "aluChassisExtAlarmEvent"),
        ("ALU-CHASSIS-MIB", "aluChassisExtAlarmPin"))
)
if mibBuilder.loadTexts:
    aluEqExtAlarmDetected.setStatus(
        "current"
    )

aluEqExtAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 2)
)
aluEqExtAlarmCleared.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALU-CHASSIS-MIB", "aluChassisExtAlarmState"),
        ("ALU-CHASSIS-MIB", "aluChassisExtAlarmEvent"),
        ("ALU-CHASSIS-MIB", "aluChassisExtAlarmPin"))
)
if mibBuilder.loadTexts:
    aluEqExtAlarmCleared.setStatus(
        "current"
    )

aluEqBgDiagsFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 3)
)
aluEqBgDiagsFault.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALU-CHASSIS-MIB", "aluExtHwBgDiagsState"),
        ("ALU-CHASSIS-MIB", "aluExtHwBgDiagsFaultReason"))
)
if mibBuilder.loadTexts:
    aluEqBgDiagsFault.setStatus(
        "current"
    )

aluEqSyncIfTimingExternAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 4)
)
aluEqSyncIfTimingExternAlarm.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingNotifyAlarm"))
)
if mibBuilder.loadTexts:
    aluEqSyncIfTimingExternAlarm.setStatus(
        "current"
    )

aluEqSyncIfTimingExternAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 5)
)
aluEqSyncIfTimingExternAlarmClear.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingNotifyAlarm"))
)
if mibBuilder.loadTexts:
    aluEqSyncIfTimingExternAlarmClear.setStatus(
        "current"
    )

aluEqFanMinorFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 6)
)
aluEqFanMinorFailure.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    aluEqFanMinorFailure.setStatus(
        "current"
    )

aluEqFIBOutOfSynch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 7)
)
aluEqFIBOutOfSynch.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    aluEqFIBOutOfSynch.setStatus(
        "current"
    )

aluEqFIBOutOfSynchClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 8)
)
aluEqFIBOutOfSynchClr.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    aluEqFIBOutOfSynchClr.setStatus(
        "current"
    )

aluEqMdaRuntimeStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 9)
)
aluEqMdaRuntimeStatus.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALU-CHASSIS-MIB", "aluChassisNotifyMdaRuntimeStatusContext"))
)
if mibBuilder.loadTexts:
    aluEqMdaRuntimeStatus.setStatus(
        "current"
    )

aluSyncIfTimingRefSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 10)
)
aluSyncIfTimingRefSwitch.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef1InUse"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef2InUse"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingExternInIfInUse"))
)
if mibBuilder.loadTexts:
    aluSyncIfTimingRefSwitch.setStatus(
        "current"
    )

aluChassisConsoleAccessed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 11)
)
if mibBuilder.loadTexts:
    aluChassisConsoleAccessed.setStatus(
        "current"
    )

aluChassisMgmtPortAccessed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 12)
)
if mibBuilder.loadTexts:
    aluChassisMgmtPortAccessed.setStatus(
        "current"
    )

aluEqMdaCriticalRuntimeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 13)
)
aluEqMdaCriticalRuntimeError.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALU-CHASSIS-MIB", "aluChassisNotifyMdaRuntimeStatusContext"))
)
if mibBuilder.loadTexts:
    aluEqMdaCriticalRuntimeError.setStatus(
        "current"
    )

aluSyncIfTimingRef1Ref2Switch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 14)
)
aluSyncIfTimingRef1Ref2Switch.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef1InUse"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef2InUse"))
)
if mibBuilder.loadTexts:
    aluSyncIfTimingRef1Ref2Switch.setStatus(
        "current"
    )

aluPwrEthPowerSupplyStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 15)
)
aluPwrEthPowerSupplyStatus.setObjects(
      *(("ALU-CHASSIS-MIB", "aluExtTmnxMDAPwrEthPsPowerMode"),
        ("ALU-CHASSIS-MIB", "aluExtTmnxMDAPwrEthPsPowerSupplyStatus"))
)
if mibBuilder.loadTexts:
    aluPwrEthPowerSupplyStatus.setStatus(
        "current"
    )

aluPwrEthExternPsStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 16)
)
aluPwrEthExternPsStatus.setObjects(
    ("ALU-CHASSIS-MIB", "aluExtTmnxMDAPwrEthPsExternalPowerSupplyStatus")
)
if mibBuilder.loadTexts:
    aluPwrEthExternPsStatus.setStatus(
        "current"
    )

aluInvalidDcPowerInput = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 17)
)
aluInvalidDcPowerInput.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    aluInvalidDcPowerInput.setStatus(
        "current"
    )

aluChassisSystemId = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 19)
)
aluChassisSystemId.setObjects(
    ("ALU-CHASSIS-MIB", "aluChassisSysId")
)
if mibBuilder.loadTexts:
    aluChassisSystemId.setStatus(
        "current"
    )


# Notifications groups

aluExtAlarmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 3)
)
aluExtAlarmNotificationGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluEqExtAlarmDetected"),
        ("ALU-CHASSIS-MIB", "aluEqExtAlarmCleared"))
)
if mibBuilder.loadTexts:
    aluExtAlarmNotificationGroup.setStatus(
        "current"
    )

aluHwBgDiagsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 6)
)
aluHwBgDiagsNotificationGroup.setObjects(
    ("ALU-CHASSIS-MIB", "aluEqBgDiagsFault")
)
if mibBuilder.loadTexts:
    aluHwBgDiagsNotificationGroup.setStatus(
        "current"
    )

aluExternalTimingNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 8)
)
aluExternalTimingNotificationGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluEqSyncIfTimingExternAlarm"),
        ("ALU-CHASSIS-MIB", "aluEqSyncIfTimingExternAlarmClear"))
)
if mibBuilder.loadTexts:
    aluExternalTimingNotificationGroup.setStatus(
        "current"
    )

aluEqFanMinorFailGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 10)
)
aluEqFanMinorFailGroup.setObjects(
    ("ALU-CHASSIS-MIB", "aluEqFanMinorFailure")
)
if mibBuilder.loadTexts:
    aluEqFanMinorFailGroup.setStatus(
        "current"
    )

aluEqFIBSynchGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 15)
)
aluEqFIBSynchGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluEqFIBOutOfSynch"),
        ("ALU-CHASSIS-MIB", "aluEqFIBOutOfSynchClr"))
)
if mibBuilder.loadTexts:
    aluEqFIBSynchGroup.setStatus(
        "current"
    )

aluEqMdaRuntimeNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 18)
)
aluEqMdaRuntimeNotificationGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluEqMdaRuntimeStatus"),
        ("ALU-CHASSIS-MIB", "aluEqMdaCriticalRuntimeError"))
)
if mibBuilder.loadTexts:
    aluEqMdaRuntimeNotificationGroup.setStatus(
        "current"
    )

aluSyncIfTimingNotifV3v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 20)
)
aluSyncIfTimingNotifV3v0Group.setObjects(
    ("ALU-CHASSIS-MIB", "aluSyncIfTimingRefSwitch")
)
if mibBuilder.loadTexts:
    aluSyncIfTimingNotifV3v0Group.setStatus(
        "current"
    )

aluChassisSecurityGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 28)
)
aluChassisSecurityGroup.setObjects(
      *(("ALU-CHASSIS-MIB", "aluChassisConsoleAccessed"),
        ("ALU-CHASSIS-MIB", "aluChassisMgmtPortAccessed"))
)
if mibBuilder.loadTexts:
    aluChassisSecurityGroup.setStatus(
        "current"
    )

aluSyncV6v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 31)
)
aluSyncV6v0Group.setObjects(
    ("ALU-CHASSIS-MIB", "aluSyncIfTimingRef1Ref2Switch")
)
if mibBuilder.loadTexts:
    aluSyncV6v0Group.setStatus(
        "current"
    )

aluPwrEthPowerSupplyV6v1Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 2, 35)
)
aluPwrEthPowerSupplyV6v1Group.setObjects(
      *(("ALU-CHASSIS-MIB", "aluPwrEthPowerSupplyStatus"),
        ("ALU-CHASSIS-MIB", "aluPwrEthExternPsStatus"),
        ("ALU-CHASSIS-MIB", "aluInvalidDcPowerInput"))
)
if mibBuilder.loadTexts:
    aluPwrEthPowerSupplyV6v1Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aluChassisV1v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 1, 1)
)
aluChassisV1v0Compliance.setObjects(
      *(("ALU-CHASSIS-MIB", "aluFamGroup"),
        ("ALU-CHASSIS-MIB", "aluExtAlarmsGroup"),
        ("ALU-CHASSIS-MIB", "aluExtAlarmNotificationGroup"),
        ("ALU-CHASSIS-MIB", "aluPlatformHwClassGroup"),
        ("ALU-CHASSIS-MIB", "aluHwBgDiagsGroup"),
        ("ALU-CHASSIS-MIB", "aluHwBgDiagsNotificationGroup"),
        ("ALU-CHASSIS-MIB", "aluExternalTimingGroup"),
        ("ALU-CHASSIS-MIB", "aluExternalTimingNotificationGroup"),
        ("ALU-CHASSIS-MIB", "aluExtCpmCardGroup"),
        ("ALU-CHASSIS-MIB", "aluFabricDeviceStatsGroup"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsGroup"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsGroup"))
)
if mibBuilder.loadTexts:
    aluChassisV1v0Compliance.setStatus(
        "obsolete"
    )

aluChassisV4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 1, 2)
)
aluChassisV4v0Compliance.setObjects(
      *(("ALU-CHASSIS-MIB", "aluFamGroup"),
        ("ALU-CHASSIS-MIB", "aluExtAlarmsGroup"),
        ("ALU-CHASSIS-MIB", "aluExtAlarmNotificationGroup"),
        ("ALU-CHASSIS-MIB", "aluPlatformHwClassGroup"),
        ("ALU-CHASSIS-MIB", "aluHwBgDiagsGroup"),
        ("ALU-CHASSIS-MIB", "aluHwBgDiagsNotificationGroup"),
        ("ALU-CHASSIS-MIB", "aluExternalTimingGroup"),
        ("ALU-CHASSIS-MIB", "aluExternalTimingNotificationGroup"),
        ("ALU-CHASSIS-MIB", "aluExtCpmCardGroup"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsGroup"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsGroup"),
        ("ALU-CHASSIS-MIB", "aluEqFIBSynchGroup"),
        ("ALU-CHASSIS-MIB", "aluEqFanMinorFailGroup"),
        ("ALU-CHASSIS-MIB", "aluEqMdaRuntimeNotificationGroup"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingNotifV3v0Group"),
        ("ALU-CHASSIS-MIB", "aluFabricDeviceStatsV4v0Group"))
)
if mibBuilder.loadTexts:
    aluChassisV4v0Compliance.setStatus(
        "current"
    )

aluChassisV6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 1, 3)
)
aluChassisV6v1Compliance.setObjects(
      *(("ALU-CHASSIS-MIB", "aluFamGroup"),
        ("ALU-CHASSIS-MIB", "aluExtAlarmsGroup"),
        ("ALU-CHASSIS-MIB", "aluExtAlarmNotificationGroup"),
        ("ALU-CHASSIS-MIB", "aluPlatformHwClassGroup"),
        ("ALU-CHASSIS-MIB", "aluHwBgDiagsGroup"),
        ("ALU-CHASSIS-MIB", "aluHwBgDiagsNotificationGroup"),
        ("ALU-CHASSIS-MIB", "aluExternalTimingGroup"),
        ("ALU-CHASSIS-MIB", "aluExternalTimingNotificationGroup"),
        ("ALU-CHASSIS-MIB", "aluExtCpmCardGroup"),
        ("ALU-CHASSIS-MIB", "aluSourceMDAStatsGroup"),
        ("ALU-CHASSIS-MIB", "aluDestMDAStatsGroup"),
        ("ALU-CHASSIS-MIB", "aluEqFIBSynchGroup"),
        ("ALU-CHASSIS-MIB", "aluEqFanMinorFailGroup"),
        ("ALU-CHASSIS-MIB", "aluEqMdaRuntimeNotificationGroup"),
        ("ALU-CHASSIS-MIB", "aluSyncIfTimingNotifV3v0Group"),
        ("ALU-CHASSIS-MIB", "aluFabricDeviceStatsV4v0Group"),
        ("ALU-CHASSIS-MIB", "aluChassisSecurityGroup"),
        ("ALU-CHASSIS-MIB", "aluRingMdaV6v0Group"),
        ("ALU-CHASSIS-MIB", "aluPwrEthPowerSupplyGroup"),
        ("ALU-CHASSIS-MIB", "aluPwrEthSystemPowerV6v1Group"),
        ("ALU-CHASSIS-MIB", "aluPwrEthPowerSupplyV6v1Group"),
        ("ALU-CHASSIS-MIB", "aluSyncV6v0Group"),
        ("ALU-CHASSIS-MIB", "aluSecurityStatsV6v1Group"))
)
if mibBuilder.loadTexts:
    aluChassisV6v1Compliance.setStatus(
        "current"
    )

aluChassisV7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 1, 4)
)
aluChassisV7v0Compliance.setObjects(
    ("ALU-CHASSIS-MIB", "aluExtMDAV7v0Group")
)
if mibBuilder.loadTexts:
    aluChassisV7v0Compliance.setStatus(
        "current"
    )

aluChassisV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 1, 5)
)
aluChassisV8v0Compliance.setObjects(
      *(("ALU-CHASSIS-MIB", "aluStatsV8v0Group"),
        ("ALU-CHASSIS-MIB", "aluExtMDAV8v0Group"))
)
if mibBuilder.loadTexts:
    aluChassisV8v0Compliance.setStatus(
        "current"
    )

aluChassisV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 2, 1, 1, 6)
)
aluChassisV9v0Compliance.setObjects(
    ("ALU-CHASSIS-MIB", "aluSyncIfTimingV9v0Group")
)
if mibBuilder.loadTexts:
    aluChassisV9v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-CHASSIS-MIB",
    **{"AluFamType": AluFamType,
       "AluExtAlarmState": AluExtAlarmState,
       "AluExtAlarmEvent": AluExtAlarmEvent,
       "AluPlatformHwClass": AluPlatformHwClass,
       "AluHwBgDiagsState": AluHwBgDiagsState,
       "AluSETSRefSource": AluSETSRefSource,
       "AluExternalIfType": AluExternalIfType,
       "AluExternalInputImpedanceType": AluExternalInputImpedanceType,
       "AluSyncIfTimingIeee1588PtpType": AluSyncIfTimingIeee1588PtpType,
       "AluSecType": AluSecType,
       "aluChassisMIBModule": aluChassisMIBModule,
       "aluHwConformance": aluHwConformance,
       "aluChassisConformance": aluChassisConformance,
       "aluChassisCompliances": aluChassisCompliances,
       "aluChassisV1v0Compliance": aluChassisV1v0Compliance,
       "aluChassisV4v0Compliance": aluChassisV4v0Compliance,
       "aluChassisV6v1Compliance": aluChassisV6v1Compliance,
       "aluChassisV7v0Compliance": aluChassisV7v0Compliance,
       "aluChassisV8v0Compliance": aluChassisV8v0Compliance,
       "aluChassisV9v0Compliance": aluChassisV9v0Compliance,
       "aluChassisGroups": aluChassisGroups,
       "aluFamGroup": aluFamGroup,
       "aluExtAlarmsGroup": aluExtAlarmsGroup,
       "aluExtAlarmNotificationGroup": aluExtAlarmNotificationGroup,
       "aluPlatformHwClassGroup": aluPlatformHwClassGroup,
       "aluHwBgDiagsGroup": aluHwBgDiagsGroup,
       "aluHwBgDiagsNotificationGroup": aluHwBgDiagsNotificationGroup,
       "aluExternalTimingGroup": aluExternalTimingGroup,
       "aluExternalTimingNotificationGroup": aluExternalTimingNotificationGroup,
       "aluExtCpmCardGroup": aluExtCpmCardGroup,
       "aluEqFanMinorFailGroup": aluEqFanMinorFailGroup,
       "aluExtMDAGroup": aluExtMDAGroup,
       "aluFabricDeviceStatsGroup": aluFabricDeviceStatsGroup,
       "aluSourceMDAStatsGroup": aluSourceMDAStatsGroup,
       "aluDestMDAStatsGroup": aluDestMDAStatsGroup,
       "aluEqFIBSynchGroup": aluEqFIBSynchGroup,
       "alu1588PtpTimingGroup": alu1588PtpTimingGroup,
       "aluEqMdaRuntimeNotifyObjsGroup": aluEqMdaRuntimeNotifyObjsGroup,
       "aluEqMdaRuntimeNotificationGroup": aluEqMdaRuntimeNotificationGroup,
       "aluQLRefSelectionGroup": aluQLRefSelectionGroup,
       "aluSyncIfTimingNotifV3v0Group": aluSyncIfTimingNotifV3v0Group,
       "aluMDAAlarmGroup": aluMDAAlarmGroup,
       "aluFabricDeviceStatsV4v0Group": aluFabricDeviceStatsV4v0Group,
       "alu1588PtpTimingV4v0Group": alu1588PtpTimingV4v0Group,
       "alu1588PtpTimingObsoleteGroup": alu1588PtpTimingObsoleteGroup,
       "aluExtMDAV5v0Group": aluExtMDAV5v0Group,
       "aluMDAEventStatsGroup": aluMDAEventStatsGroup,
       "aluExtHwMfgVariantGroup": aluExtHwMfgVariantGroup,
       "aluChassisSecurityGroup": aluChassisSecurityGroup,
       "aluExtMDAV6v0Group": aluExtMDAV6v0Group,
       "aluRingMdaV6v0Group": aluRingMdaV6v0Group,
       "aluSyncV6v0Group": aluSyncV6v0Group,
       "aluPwrEthPowerSupplyGroup": aluPwrEthPowerSupplyGroup,
       "aluSecurityStatsV6v1Group": aluSecurityStatsV6v1Group,
       "aluPwrEthSystemPowerV6v1Group": aluPwrEthSystemPowerV6v1Group,
       "aluPwrEthPowerSupplyV6v1Group": aluPwrEthPowerSupplyV6v1Group,
       "aluChassisPowerFeedGroup": aluChassisPowerFeedGroup,
       "aluExtMDAV7v0Group": aluExtMDAV7v0Group,
       "aluChassisSysIdGroup": aluChassisSysIdGroup,
       "aluStatsV8v0Group": aluStatsV8v0Group,
       "aluIpTransportQueueStatsGroup": aluIpTransportQueueStatsGroup,
       "aluExtMDAV8v0Group": aluExtMDAV8v0Group,
       "aluSyncIfTimingV9v0Group": aluSyncIfTimingV9v0Group,
       "aluSetsMIBConformance": aluSetsMIBConformance,
       "aluHwObjs": aluHwObjs,
       "aluChassisObjs": aluChassisObjs,
       "aluFamTable": aluFamTable,
       "aluFamEntry": aluFamEntry,
       "aluFamIndex": aluFamIndex,
       "aluFamOperStatus": aluFamOperStatus,
       "aluFamHwIndex": aluFamHwIndex,
       "aluFamEquippedType": aluFamEquippedType,
       "aluChassisExtAlarmTable": aluChassisExtAlarmTable,
       "aluChassisExtAlarmEntry": aluChassisExtAlarmEntry,
       "aluChassisExtAlarmIndex": aluChassisExtAlarmIndex,
       "aluChassisExtAlarmState": aluChassisExtAlarmState,
       "aluChassisExtAlarmEvent": aluChassisExtAlarmEvent,
       "aluChassisExtAlarmPin": aluChassisExtAlarmPin,
       "aluExtTmnxHwTable": aluExtTmnxHwTable,
       "aluExtTmnxHwEntry": aluExtTmnxHwEntry,
       "aluExtPlatformHwClass": aluExtPlatformHwClass,
       "aluExtHwBgDiagsState": aluExtHwBgDiagsState,
       "aluExtHwBgDiagsFaultReason": aluExtHwBgDiagsFaultReason,
       "aluExtHwMfgVariant": aluExtHwMfgVariant,
       "aluExtTmnxMDATable": aluExtTmnxMDATable,
       "aluExtTmnxMDAEntry": aluExtTmnxMDAEntry,
       "aluExtTmnxMDANetworkIngFabricPolicy": aluExtTmnxMDANetworkIngFabricPolicy,
       "aluExtTmnxMDAAccessIngFabricPolicy": aluExtTmnxMDAAccessIngFabricPolicy,
       "aluExtTmnxMDAFabricStatsEnabled": aluExtTmnxMDAFabricStatsEnabled,
       "aluExtTmnxMDAVoiceCompandingLaw": aluExtTmnxMDAVoiceCompandingLaw,
       "aluExtTmnxMDAVoiceSignalingType": aluExtTmnxMDAVoiceSignalingType,
       "aluExtTmnxMDANumOfDigitalAlarmInputs": aluExtTmnxMDANumOfDigitalAlarmInputs,
       "aluExtTmnxMDANumOfAnalogAlarmInputs": aluExtTmnxMDANumOfAnalogAlarmInputs,
       "aluExtTmnxMDANumOfDigitalOutputRelays": aluExtTmnxMDANumOfDigitalOutputRelays,
       "aluExtTmnxMDACapabilityMode": aluExtTmnxMDACapabilityMode,
       "aluExtTmnxMDANetworkRingQueuePolicy": aluExtTmnxMDANetworkRingQueuePolicy,
       "aluExtTmnxMDANetworkRingQosPolicy": aluExtTmnxMDANetworkRingQosPolicy,
       "aluExtTmnxMDAPwrEthPsPowerMode": aluExtTmnxMDAPwrEthPsPowerMode,
       "aluExtTmnxMDAPwrEthPsPowerSupplyStatus": aluExtTmnxMDAPwrEthPsPowerSupplyStatus,
       "aluExtTmnxMDAPwrEthPsExternalPowerSupplyStatus": aluExtTmnxMDAPwrEthPsExternalPowerSupplyStatus,
       "aluExtTmnxMDATuAisEnabled": aluExtTmnxMDATuAisEnabled,
       "aluExtTmnxMDANetworkIngSecQueuePolicy": aluExtTmnxMDANetworkIngSecQueuePolicy,
       "aluExtTmnxMDAAccessIngSecQueuePolicy": aluExtTmnxMDAAccessIngSecQueuePolicy,
       "aluExtTmnxMDASptSecAggRate": aluExtTmnxMDASptSecAggRate,
       "aluExtTmnxMDAAccessIngShaperPolicy": aluExtTmnxMDAAccessIngShaperPolicy,
       "aluExtTmnxMDAVcbApplication": aluExtTmnxMDAVcbApplication,
       "aluFabricDeviceStatsTable": aluFabricDeviceStatsTable,
       "aluFabricDeviceStatsEntry": aluFabricDeviceStatsEntry,
       "aluFabricDeviceStatsIndex": aluFabricDeviceStatsIndex,
       "aluFabricDeviceStatsFwdPkts": aluFabricDeviceStatsFwdPkts,
       "aluFabricDeviceStatsDroPkts": aluFabricDeviceStatsDroPkts,
       "aluFabricDeviceStatsFwdOcts": aluFabricDeviceStatsFwdOcts,
       "aluFabricDeviceStatsUcastFwdPkts": aluFabricDeviceStatsUcastFwdPkts,
       "aluFabricDeviceStatsMcastFwdPkts": aluFabricDeviceStatsMcastFwdPkts,
       "aluFabricDeviceStatsDroOcts": aluFabricDeviceStatsDroOcts,
       "aluFabricDeviceStatsMdaDroEvents": aluFabricDeviceStatsMdaDroEvents,
       "aluSourceMDAStatsTable": aluSourceMDAStatsTable,
       "aluSourceMDAStatsEntry": aluSourceMDAStatsEntry,
       "aluSourceMDASrcMdaId": aluSourceMDASrcMdaId,
       "aluSourceMDADestMdaId": aluSourceMDADestMdaId,
       "aluSourceMDAStatsFwdInProfPkts": aluSourceMDAStatsFwdInProfPkts,
       "aluSourceMDAStatsFwdOutProfPkts": aluSourceMDAStatsFwdOutProfPkts,
       "aluSourceMDAStatsFwdInProfOcts": aluSourceMDAStatsFwdInProfOcts,
       "aluSourceMDAStatsFwdOutProfOcts": aluSourceMDAStatsFwdOutProfOcts,
       "aluSourceMDAStatsDroInProfPkts": aluSourceMDAStatsDroInProfPkts,
       "aluSourceMDAStatsDroOutProfPkts": aluSourceMDAStatsDroOutProfPkts,
       "aluSourceMDAStatsDroInProfOcts": aluSourceMDAStatsDroInProfOcts,
       "aluSourceMDAStatsDroOutProfOcts": aluSourceMDAStatsDroOutProfOcts,
       "aluSourceMDAStatsAccessFwdInProfPkts": aluSourceMDAStatsAccessFwdInProfPkts,
       "aluSourceMDAStatsAccessFwdOutProfPkts": aluSourceMDAStatsAccessFwdOutProfPkts,
       "aluSourceMDAStatsAccessFwdInProfOcts": aluSourceMDAStatsAccessFwdInProfOcts,
       "aluSourceMDAStatsAccessFwdOutProfOcts": aluSourceMDAStatsAccessFwdOutProfOcts,
       "aluSourceMDAStatsAccessDroPkts": aluSourceMDAStatsAccessDroPkts,
       "aluSourceMDAStatsAccessDroOcts": aluSourceMDAStatsAccessDroOcts,
       "aluDestMDAStatsTable": aluDestMDAStatsTable,
       "aluDestMDAStatsEntry": aluDestMDAStatsEntry,
       "aluDestMDADestMdaId": aluDestMDADestMdaId,
       "aluDestMDASrcMdaId": aluDestMDASrcMdaId,
       "aluDestMDAStatsFwdInProfPkts": aluDestMDAStatsFwdInProfPkts,
       "aluDestMDAStatsFwdOutProfPkts": aluDestMDAStatsFwdOutProfPkts,
       "aluDestMDAStatsFwdInProfOcts": aluDestMDAStatsFwdInProfOcts,
       "aluDestMDAStatsFwdOutProfOcts": aluDestMDAStatsFwdOutProfOcts,
       "aluDestMDAStatsDroInProfPkts": aluDestMDAStatsDroInProfPkts,
       "aluDestMDAStatsDroOutProfPkts": aluDestMDAStatsDroOutProfPkts,
       "aluDestMDAStatsDroInProfOcts": aluDestMDAStatsDroInProfOcts,
       "aluDestMDAStatsDroOutProfOcts": aluDestMDAStatsDroOutProfOcts,
       "aluDestMDAStatsAccessFwdInProfPkts": aluDestMDAStatsAccessFwdInProfPkts,
       "aluDestMDAStatsAccessFwdOutProfPkts": aluDestMDAStatsAccessFwdOutProfPkts,
       "aluDestMDAStatsAccessFwdInProfOcts": aluDestMDAStatsAccessFwdInProfOcts,
       "aluDestMDAStatsAccessFwdOutProfOcts": aluDestMDAStatsAccessFwdOutProfOcts,
       "aluDestMDAStatsAccessDroPkts": aluDestMDAStatsAccessDroPkts,
       "aluDestMDAStatsAccessDroOcts": aluDestMDAStatsAccessDroOcts,
       "aluMdaMacFdbMgmtTable": aluMdaMacFdbMgmtTable,
       "aluMdaMacFdbMgmtEntry": aluMdaMacFdbMgmtEntry,
       "aluMdaMacFdbMacLearning": aluMdaMacFdbMacLearning,
       "aluMdaMacFdbMacAgeing": aluMdaMacFdbMacAgeing,
       "aluMdaMacFdbFlushTable": aluMdaMacFdbFlushTable,
       "aluMdaMacFdbFlushPortID": aluMdaMacFdbFlushPortID,
       "aluMdaMacFdbFlushMac": aluMdaMacFdbFlushMac,
       "aluMdaMacFdbRemoteAgeTime": aluMdaMacFdbRemoteAgeTime,
       "aluMdaMacFdbTableSize": aluMdaMacFdbTableSize,
       "aluMdaMacFdbNumEntries": aluMdaMacFdbNumEntries,
       "aluMdaMacFdbNumStaticEntries": aluMdaMacFdbNumStaticEntries,
       "aluMdaMacFdbDiscardUnknownSource": aluMdaMacFdbDiscardUnknownSource,
       "aluMdaMacFdbMacPinningValue1": aluMdaMacFdbMacPinningValue1,
       "aluMdaMacFdbMacPinningValue2": aluMdaMacFdbMacPinningValue2,
       "aluMdaMacFdbHighWaterMark": aluMdaMacFdbHighWaterMark,
       "aluMdaMacFdbTable": aluMdaMacFdbTable,
       "aluMdaMacFdbEntry": aluMdaMacFdbEntry,
       "aluMdaMacFdbMacAddr": aluMdaMacFdbMacAddr,
       "aluMdaMacFdbRowStatus": aluMdaMacFdbRowStatus,
       "aluMdaMacFdbType": aluMdaMacFdbType,
       "aluMdaMacFdbPortID": aluMdaMacFdbPortID,
       "aluSecQueueStatsTable": aluSecQueueStatsTable,
       "aluSecQueueStatsEntry": aluSecQueueStatsEntry,
       "aluSecQueueId": aluSecQueueId,
       "aluSecQueueMode": aluSecQueueMode,
       "aluSecQueueFwdHiPrioPkts": aluSecQueueFwdHiPrioPkts,
       "aluSecQueueFwdLowPrioPkts": aluSecQueueFwdLowPrioPkts,
       "aluSecQueueFwdHiPrioBytes": aluSecQueueFwdHiPrioBytes,
       "aluSecQueueFwdLowPrioBytes": aluSecQueueFwdLowPrioBytes,
       "aluSecQueueDroHiPrioPkts": aluSecQueueDroHiPrioPkts,
       "aluSecQueueDroLowPrioPkts": aluSecQueueDroLowPrioPkts,
       "aluSecQueueDroHiPrioBytes": aluSecQueueDroHiPrioBytes,
       "aluSecQueueDroLowPrioBytes": aluSecQueueDroLowPrioBytes,
       "aluSecQueueFwdInProfPkts": aluSecQueueFwdInProfPkts,
       "aluSecQueueFwdOutProfPkts": aluSecQueueFwdOutProfPkts,
       "aluSecQueueFwdInProfBytes": aluSecQueueFwdInProfBytes,
       "aluSecQueueFwdOutProfBytes": aluSecQueueFwdOutProfBytes,
       "aluSecQueueDroInProfPkts": aluSecQueueDroInProfPkts,
       "aluSecQueueDroOutProfPkts": aluSecQueueDroOutProfPkts,
       "aluSecQueueDroInProfBytes": aluSecQueueDroInProfBytes,
       "aluSecQueueDroOutProfBytes": aluSecQueueDroOutProfBytes,
       "aluSecType": aluSecType,
       "aluIPsecCtrlQueueStatsTable": aluIPsecCtrlQueueStatsTable,
       "aluIPsecCtrlQueueStatsEntry": aluIPsecCtrlQueueStatsEntry,
       "aluIPsecCtrlQueueFwdPkts": aluIPsecCtrlQueueFwdPkts,
       "aluIPsecCtrlQueueFwdBytes": aluIPsecCtrlQueueFwdBytes,
       "aluIPsecCtrlQueueDroPkts": aluIPsecCtrlQueueDroPkts,
       "aluIPsecCtrlQueueDroBytes": aluIPsecCtrlQueueDroBytes,
       "aluPwrEthSystemPowerInfoTable": aluPwrEthSystemPowerInfoTable,
       "aluPwrEthSystemPowerInfoEntry": aluPwrEthSystemPowerInfoEntry,
       "aluPwrEthSystemMaxPowerBudget": aluPwrEthSystemMaxPowerBudget,
       "aluPwrEthSystemPowerCommitted": aluPwrEthSystemPowerCommitted,
       "aluPwrEthSystemPowerAvailable": aluPwrEthSystemPowerAvailable,
       "aluPwrEthSystemPowerInUse": aluPwrEthSystemPowerInUse,
       "aluChassisPowerFeedInfoTable": aluChassisPowerFeedInfoTable,
       "aluChassisPowerFeedInfoEntry": aluChassisPowerFeedInfoEntry,
       "aluChassisPowerSupplyId": aluChassisPowerSupplyId,
       "aluChassisPowerFeedMonitoring": aluChassisPowerFeedMonitoring,
       "aluChassisSystemIdTable": aluChassisSystemIdTable,
       "aluChassisSystemIdEntry": aluChassisSystemIdEntry,
       "aluChassisSysId": aluChassisSysId,
       "aluMirrorQueueStatsTable": aluMirrorQueueStatsTable,
       "aluMirrorQueueStatsEntry": aluMirrorQueueStatsEntry,
       "aluMirrorQueueId": aluMirrorQueueId,
       "aluMirrorQueueFwdInProfPkts": aluMirrorQueueFwdInProfPkts,
       "aluMirrorQueueFwdOutProfPkts": aluMirrorQueueFwdOutProfPkts,
       "aluMirrorQueueFwdInProfBytes": aluMirrorQueueFwdInProfBytes,
       "aluMirrorQueueFwdOutProfBytes": aluMirrorQueueFwdOutProfBytes,
       "aluMirrorQueueDroInProfPkts": aluMirrorQueueDroInProfPkts,
       "aluMirrorQueueDroOutProfPkts": aluMirrorQueueDroOutProfPkts,
       "aluMirrorQueueDroInProfBytes": aluMirrorQueueDroInProfBytes,
       "aluMirrorQueueDroOutProfBytes": aluMirrorQueueDroOutProfBytes,
       "aluIpTransportQueueStatsTable": aluIpTransportQueueStatsTable,
       "aluIpTransportQueueStatsEntry": aluIpTransportQueueStatsEntry,
       "aluIpTransportQueueId": aluIpTransportQueueId,
       "aluIpTransportQueueFwdPkts": aluIpTransportQueueFwdPkts,
       "aluIpTransportQueueFwdBytes": aluIpTransportQueueFwdBytes,
       "aluIpTransportQueueDroPkts": aluIpTransportQueueDroPkts,
       "aluIpTransportQueueDroBytes": aluIpTransportQueueDroBytes,
       "aluCflowdQueueStatsTable": aluCflowdQueueStatsTable,
       "aluCflowdQueueStatsEntry": aluCflowdQueueStatsEntry,
       "aluCflowdQueueForwardPackets": aluCflowdQueueForwardPackets,
       "aluCflowdQueueForwardBytes": aluCflowdQueueForwardBytes,
       "aluCflowdQueueDropPackets": aluCflowdQueueDropPackets,
       "aluCflowdQueueDropBytes": aluCflowdQueueDropBytes,
       "aluCardObjs": aluCardObjs,
       "aluExtTmnxCpmCardTable": aluExtTmnxCpmCardTable,
       "aluExtTmnxCpmCardEntry": aluExtTmnxCpmCardEntry,
       "aluExtCpmCardUpgrade": aluExtCpmCardUpgrade,
       "aluChassisNotificationObjects": aluChassisNotificationObjects,
       "aluChassisNotifyMdaRuntimeStatusContext": aluChassisNotifyMdaRuntimeStatusContext,
       "aluSyncObjs": aluSyncObjs,
       "aluSyncExtensionObjs": aluSyncExtensionObjs,
       "aluExtIfSyncIfTimingExtensionTable": aluExtIfSyncIfTimingExtensionTable,
       "aluExtIfSyncIfTimingExtensionEntry": aluExtIfSyncIfTimingExtensionEntry,
       "aluSyncIfTimingExternInIfType": aluSyncIfTimingExternInIfType,
       "aluSyncIfTimingExternInImpedType": aluSyncIfTimingExternInImpedType,
       "aluSyncIfTimingExternOutIfType": aluSyncIfTimingExternOutIfType,
       "aluSyncIfTimingExternInIfAdminStatus": aluSyncIfTimingExternInIfAdminStatus,
       "aluSyncIfTimingExternInIfInUse": aluSyncIfTimingExternInIfInUse,
       "aluSyncIfTimingExternInIfQualified": aluSyncIfTimingExternInIfQualified,
       "aluSyncIfTimingExternInIfAlarm": aluSyncIfTimingExternInIfAlarm,
       "aluSyncIfTimingRef1Ieee1588PtpSrc": aluSyncIfTimingRef1Ieee1588PtpSrc,
       "aluSyncIfTimingRef2Ieee1588PtpSrc": aluSyncIfTimingRef2Ieee1588PtpSrc,
       "aluSyncIfTimingIeee1588PtpType": aluSyncIfTimingIeee1588PtpType,
       "aluSyncIfTimingExternInCfgQltyLevel": aluSyncIfTimingExternInCfgQltyLevel,
       "aluSyncIfTimingExternInState": aluSyncIfTimingExternInState,
       "aluSyncIfTimingRef1SrcPtpClock": aluSyncIfTimingRef1SrcPtpClock,
       "aluSyncIfTimingRef2SrcPtpClock": aluSyncIfTimingRef2SrcPtpClock,
       "aluExtIfSyncIfTimingAdmExtensionTable": aluExtIfSyncIfTimingAdmExtensionTable,
       "aluExtIfSyncIfTimingAdmExtensionEntry": aluExtIfSyncIfTimingAdmExtensionEntry,
       "aluSyncIfTimingAdmExternInIfType": aluSyncIfTimingAdmExternInIfType,
       "aluSyncIfTimingAdmExternInImpedType": aluSyncIfTimingAdmExternInImpedType,
       "aluSyncIfTimingAdmExternOutIfType": aluSyncIfTimingAdmExternOutIfType,
       "aluSyncIfTimingAdmExternInIfAdminStatus": aluSyncIfTimingAdmExternInIfAdminStatus,
       "aluSyncIfTimingAdmRef1Ieee1588PtpSrc": aluSyncIfTimingAdmRef1Ieee1588PtpSrc,
       "aluSyncIfTimingAdmRef2Ieee1588PtpSrc": aluSyncIfTimingAdmRef2Ieee1588PtpSrc,
       "aluSyncIfTimingAdmExternInCfgQltyLevel": aluSyncIfTimingAdmExternInCfgQltyLevel,
       "aluSyncIfTimingAdmRef1SrcPtpClock": aluSyncIfTimingAdmRef1SrcPtpClock,
       "aluSyncIfTimingAdmRef2SrcPtpClock": aluSyncIfTimingAdmRef2SrcPtpClock,
       "aluSyncIfTimingAdmChangedMask": aluSyncIfTimingAdmChangedMask,
       "aluHwNotification": aluHwNotification,
       "aluChassisNotifyPrefix": aluChassisNotifyPrefix,
       "aluChassisNotification": aluChassisNotification,
       "aluEqExtAlarmDetected": aluEqExtAlarmDetected,
       "aluEqExtAlarmCleared": aluEqExtAlarmCleared,
       "aluEqBgDiagsFault": aluEqBgDiagsFault,
       "aluEqSyncIfTimingExternAlarm": aluEqSyncIfTimingExternAlarm,
       "aluEqSyncIfTimingExternAlarmClear": aluEqSyncIfTimingExternAlarmClear,
       "aluEqFanMinorFailure": aluEqFanMinorFailure,
       "aluEqFIBOutOfSynch": aluEqFIBOutOfSynch,
       "aluEqFIBOutOfSynchClr": aluEqFIBOutOfSynchClr,
       "aluEqMdaRuntimeStatus": aluEqMdaRuntimeStatus,
       "aluSyncIfTimingRefSwitch": aluSyncIfTimingRefSwitch,
       "aluChassisConsoleAccessed": aluChassisConsoleAccessed,
       "aluChassisMgmtPortAccessed": aluChassisMgmtPortAccessed,
       "aluEqMdaCriticalRuntimeError": aluEqMdaCriticalRuntimeError,
       "aluSyncIfTimingRef1Ref2Switch": aluSyncIfTimingRef1Ref2Switch,
       "aluPwrEthPowerSupplyStatus": aluPwrEthPowerSupplyStatus,
       "aluPwrEthExternPsStatus": aluPwrEthExternPsStatus,
       "aluInvalidDcPowerInput": aluInvalidDcPowerInput,
       "aluChassisSystemId": aluChassisSystemId,
       "aluSetsNotifyPrefix": aluSetsNotifyPrefix}
)
