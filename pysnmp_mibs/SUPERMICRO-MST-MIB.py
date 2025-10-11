# SNMP MIB module (SUPERMICRO-MST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-MST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:04:30 2025
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


# MODULE-IDENTITY

futureMstMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80)
)
if mibBuilder.loadTexts:
    futureMstMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanId(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class BridgeId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class Timeout(TextualConvention, Integer32):
    status = "current"
    displayHint = "d4"


class EnabledStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Dot1sFutureMst_ObjectIdentity = ObjectIdentity
dot1sFutureMst = _Dot1sFutureMst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1)
)


class _FsMstSystemControl_Type(Integer32):
    """Custom type fsMstSystemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_FsMstSystemControl_Type.__name__ = "Integer32"
_FsMstSystemControl_Object = MibScalar
fsMstSystemControl = _FsMstSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 1),
    _FsMstSystemControl_Type()
)
fsMstSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstSystemControl.setStatus("current")
_FsMstModuleStatus_Type = EnabledStatus
_FsMstModuleStatus_Object = MibScalar
fsMstModuleStatus = _FsMstModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 2),
    _FsMstModuleStatus_Type()
)
fsMstModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstModuleStatus.setStatus("current")


class _FsMstMaxMstInstanceNumber_Type(Integer32):
    """Custom type fsMstMaxMstInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_FsMstMaxMstInstanceNumber_Type.__name__ = "Integer32"
_FsMstMaxMstInstanceNumber_Object = MibScalar
fsMstMaxMstInstanceNumber = _FsMstMaxMstInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 3),
    _FsMstMaxMstInstanceNumber_Type()
)
fsMstMaxMstInstanceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstMaxMstInstanceNumber.setStatus("current")
_FsMstNoOfMstiSupported_Type = Integer32
_FsMstNoOfMstiSupported_Object = MibScalar
fsMstNoOfMstiSupported = _FsMstNoOfMstiSupported_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 4),
    _FsMstNoOfMstiSupported_Type()
)
fsMstNoOfMstiSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstNoOfMstiSupported.setStatus("current")


class _FsMstMaxHopCount_Type(Integer32):
    """Custom type fsMstMaxHopCount based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_FsMstMaxHopCount_Type.__name__ = "Integer32"
_FsMstMaxHopCount_Object = MibScalar
fsMstMaxHopCount = _FsMstMaxHopCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 5),
    _FsMstMaxHopCount_Type()
)
fsMstMaxHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstMaxHopCount.setStatus("current")
_FsMstBrgAddress_Type = MacAddress
_FsMstBrgAddress_Object = MibScalar
fsMstBrgAddress = _FsMstBrgAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 6),
    _FsMstBrgAddress_Type()
)
fsMstBrgAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstBrgAddress.setStatus("current")
_FsMstCistRoot_Type = BridgeId
_FsMstCistRoot_Object = MibScalar
fsMstCistRoot = _FsMstCistRoot_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 7),
    _FsMstCistRoot_Type()
)
fsMstCistRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistRoot.setStatus("current")
_FsMstCistRegionalRoot_Type = BridgeId
_FsMstCistRegionalRoot_Object = MibScalar
fsMstCistRegionalRoot = _FsMstCistRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 8),
    _FsMstCistRegionalRoot_Type()
)
fsMstCistRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistRegionalRoot.setStatus("current")
_FsMstCistRootCost_Type = Integer32
_FsMstCistRootCost_Object = MibScalar
fsMstCistRootCost = _FsMstCistRootCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 9),
    _FsMstCistRootCost_Type()
)
fsMstCistRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistRootCost.setStatus("current")
_FsMstCistRegionalRootCost_Type = Integer32
_FsMstCistRegionalRootCost_Object = MibScalar
fsMstCistRegionalRootCost = _FsMstCistRegionalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 10),
    _FsMstCistRegionalRootCost_Type()
)
fsMstCistRegionalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistRegionalRootCost.setStatus("current")
_FsMstCistRootPort_Type = Integer32
_FsMstCistRootPort_Object = MibScalar
fsMstCistRootPort = _FsMstCistRootPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 11),
    _FsMstCistRootPort_Type()
)
fsMstCistRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistRootPort.setStatus("current")


class _FsMstCistBridgePriority_Type(Integer32):
    """Custom type fsMstCistBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_FsMstCistBridgePriority_Type.__name__ = "Integer32"
_FsMstCistBridgePriority_Object = MibScalar
fsMstCistBridgePriority = _FsMstCistBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 12),
    _FsMstCistBridgePriority_Type()
)
fsMstCistBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstCistBridgePriority.setStatus("current")


class _FsMstCistBridgeMaxAge_Type(Timeout):
    """Custom type fsMstCistBridgeMaxAge based on Timeout"""
    defaultValue = 2000

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_FsMstCistBridgeMaxAge_Type.__name__ = "Timeout"
_FsMstCistBridgeMaxAge_Object = MibScalar
fsMstCistBridgeMaxAge = _FsMstCistBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 13),
    _FsMstCistBridgeMaxAge_Type()
)
fsMstCistBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstCistBridgeMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    fsMstCistBridgeMaxAge.setUnits("centi-seconds")


class _FsMstCistBridgeForwardDelay_Type(Timeout):
    """Custom type fsMstCistBridgeForwardDelay based on Timeout"""
    defaultValue = 1500

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_FsMstCistBridgeForwardDelay_Type.__name__ = "Timeout"
_FsMstCistBridgeForwardDelay_Object = MibScalar
fsMstCistBridgeForwardDelay = _FsMstCistBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 14),
    _FsMstCistBridgeForwardDelay_Type()
)
fsMstCistBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstCistBridgeForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    fsMstCistBridgeForwardDelay.setUnits("centi-seconds")
_FsMstCistHoldTime_Type = Integer32
_FsMstCistHoldTime_Object = MibScalar
fsMstCistHoldTime = _FsMstCistHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 15),
    _FsMstCistHoldTime_Type()
)
fsMstCistHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    fsMstCistHoldTime.setUnits("centi-seconds")
_FsMstCistMaxAge_Type = Timeout
_FsMstCistMaxAge_Object = MibScalar
fsMstCistMaxAge = _FsMstCistMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 16),
    _FsMstCistMaxAge_Type()
)
fsMstCistMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    fsMstCistMaxAge.setUnits("centi-seconds")
_FsMstCistForwardDelay_Type = Timeout
_FsMstCistForwardDelay_Object = MibScalar
fsMstCistForwardDelay = _FsMstCistForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 17),
    _FsMstCistForwardDelay_Type()
)
fsMstCistForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    fsMstCistForwardDelay.setUnits("centi-seconds")
_FsMstMstpUpCount_Type = Counter32
_FsMstMstpUpCount_Object = MibScalar
fsMstMstpUpCount = _FsMstMstpUpCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 18),
    _FsMstMstpUpCount_Type()
)
fsMstMstpUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstpUpCount.setStatus("current")
_FsMstMstpDownCount_Type = Counter32
_FsMstMstpDownCount_Object = MibScalar
fsMstMstpDownCount = _FsMstMstpDownCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 19),
    _FsMstMstpDownCount_Type()
)
fsMstMstpDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstpDownCount.setStatus("current")


class _FsMstPathCostDefaultType_Type(Integer32):
    """Custom type fsMstPathCostDefaultType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stp8021d1998", 1),
          ("stp8021t2001", 2))
    )


_FsMstPathCostDefaultType_Type.__name__ = "Integer32"
_FsMstPathCostDefaultType_Object = MibScalar
fsMstPathCostDefaultType = _FsMstPathCostDefaultType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 20),
    _FsMstPathCostDefaultType_Type()
)
fsMstPathCostDefaultType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstPathCostDefaultType.setStatus("obsolete")


class _FsMstTrace_Type(Integer32):
    """Custom type fsMstTrace based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMstTrace_Type.__name__ = "Integer32"
_FsMstTrace_Object = MibScalar
fsMstTrace = _FsMstTrace_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 21),
    _FsMstTrace_Type()
)
fsMstTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstTrace.setStatus("current")


class _FsMstDebug_Type(Integer32):
    """Custom type fsMstDebug based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 524287),
    )


_FsMstDebug_Type.__name__ = "Integer32"
_FsMstDebug_Object = MibScalar
fsMstDebug = _FsMstDebug_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 22),
    _FsMstDebug_Type()
)
fsMstDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstDebug.setStatus("current")


class _FsMstForceProtocolVersion_Type(Integer32):
    """Custom type fsMstForceProtocolVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stpCompatible", 0),
          ("rstp", 2),
          ("mstp", 3))
    )


_FsMstForceProtocolVersion_Type.__name__ = "Integer32"
_FsMstForceProtocolVersion_Object = MibScalar
fsMstForceProtocolVersion = _FsMstForceProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 23),
    _FsMstForceProtocolVersion_Type()
)
fsMstForceProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstForceProtocolVersion.setStatus("current")


class _FsMstTxHoldCount_Type(Integer32):
    """Custom type fsMstTxHoldCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsMstTxHoldCount_Type.__name__ = "Integer32"
_FsMstTxHoldCount_Object = MibScalar
fsMstTxHoldCount = _FsMstTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 24),
    _FsMstTxHoldCount_Type()
)
fsMstTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstTxHoldCount.setStatus("current")


class _FsMstMstiConfigIdSel_Type(Integer32):
    """Custom type fsMstMstiConfigIdSel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMstMstiConfigIdSel_Type.__name__ = "Integer32"
_FsMstMstiConfigIdSel_Object = MibScalar
fsMstMstiConfigIdSel = _FsMstMstiConfigIdSel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 25),
    _FsMstMstiConfigIdSel_Type()
)
fsMstMstiConfigIdSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstMstiConfigIdSel.setStatus("current")


class _FsMstMstiRegionName_Type(OctetString):
    """Custom type fsMstMstiRegionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsMstMstiRegionName_Type.__name__ = "OctetString"
_FsMstMstiRegionName_Object = MibScalar
fsMstMstiRegionName = _FsMstMstiRegionName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 26),
    _FsMstMstiRegionName_Type()
)
fsMstMstiRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstMstiRegionName.setStatus("current")


class _FsMstMstiRegionVersion_Type(Integer32):
    """Custom type fsMstMstiRegionVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMstMstiRegionVersion_Type.__name__ = "Integer32"
_FsMstMstiRegionVersion_Object = MibScalar
fsMstMstiRegionVersion = _FsMstMstiRegionVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 27),
    _FsMstMstiRegionVersion_Type()
)
fsMstMstiRegionVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstMstiRegionVersion.setStatus("current")


class _FsMstMstiConfigDigest_Type(OctetString):
    """Custom type fsMstMstiConfigDigest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsMstMstiConfigDigest_Type.__name__ = "OctetString"
_FsMstMstiConfigDigest_Object = MibScalar
fsMstMstiConfigDigest = _FsMstMstiConfigDigest_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 28),
    _FsMstMstiConfigDigest_Type()
)
fsMstMstiConfigDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiConfigDigest.setStatus("current")
_FsMstBufferOverFlowCount_Type = Counter32
_FsMstBufferOverFlowCount_Object = MibScalar
fsMstBufferOverFlowCount = _FsMstBufferOverFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 29),
    _FsMstBufferOverFlowCount_Type()
)
fsMstBufferOverFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstBufferOverFlowCount.setStatus("current")
_FsMstMemAllocFailureCount_Type = Counter32
_FsMstMemAllocFailureCount_Object = MibScalar
fsMstMemAllocFailureCount = _FsMstMemAllocFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 30),
    _FsMstMemAllocFailureCount_Type()
)
fsMstMemAllocFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMemAllocFailureCount.setStatus("current")
_FsMstRegionConfigChangeCount_Type = Counter32
_FsMstRegionConfigChangeCount_Object = MibScalar
fsMstRegionConfigChangeCount = _FsMstRegionConfigChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 31),
    _FsMstRegionConfigChangeCount_Type()
)
fsMstRegionConfigChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstRegionConfigChangeCount.setStatus("current")


class _FsMstCistBridgeRoleSelectionSemState_Type(Integer32):
    """Custom type fsMstCistBridgeRoleSelectionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("initbridge", 0),
          ("roleselection", 1))
    )


_FsMstCistBridgeRoleSelectionSemState_Type.__name__ = "Integer32"
_FsMstCistBridgeRoleSelectionSemState_Object = MibScalar
fsMstCistBridgeRoleSelectionSemState = _FsMstCistBridgeRoleSelectionSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 32),
    _FsMstCistBridgeRoleSelectionSemState_Type()
)
fsMstCistBridgeRoleSelectionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistBridgeRoleSelectionSemState.setStatus("current")
_FsMstCistTimeSinceTopologyChange_Type = TimeTicks
_FsMstCistTimeSinceTopologyChange_Object = MibScalar
fsMstCistTimeSinceTopologyChange = _FsMstCistTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 33),
    _FsMstCistTimeSinceTopologyChange_Type()
)
fsMstCistTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistTimeSinceTopologyChange.setStatus("current")
if mibBuilder.loadTexts:
    fsMstCistTimeSinceTopologyChange.setUnits("centi-seconds")
_FsMstCistTopChanges_Type = Counter32
_FsMstCistTopChanges_Object = MibScalar
fsMstCistTopChanges = _FsMstCistTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 34),
    _FsMstCistTopChanges_Type()
)
fsMstCistTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistTopChanges.setStatus("current")
_FsMstCistNewRootBridgeCount_Type = Counter32
_FsMstCistNewRootBridgeCount_Object = MibScalar
fsMstCistNewRootBridgeCount = _FsMstCistNewRootBridgeCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 35),
    _FsMstCistNewRootBridgeCount_Type()
)
fsMstCistNewRootBridgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistNewRootBridgeCount.setStatus("current")
_FsMstCistHelloTime_Type = Timeout
_FsMstCistHelloTime_Object = MibScalar
fsMstCistHelloTime = _FsMstCistHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 36),
    _FsMstCistHelloTime_Type()
)
fsMstCistHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    fsMstCistHelloTime.setUnits("centi-seconds")


class _FsMstCistBridgeHelloTime_Type(Timeout):
    """Custom type fsMstCistBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(200, 200),
    )


_FsMstCistBridgeHelloTime_Type.__name__ = "Timeout"
_FsMstCistBridgeHelloTime_Object = MibScalar
fsMstCistBridgeHelloTime = _FsMstCistBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 37),
    _FsMstCistBridgeHelloTime_Type()
)
fsMstCistBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstCistBridgeHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    fsMstCistBridgeHelloTime.setUnits("centi-seconds")
_FsMstMstiBridgeTable_Object = MibTable
fsMstMstiBridgeTable = _FsMstMstiBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 38)
)
if mibBuilder.loadTexts:
    fsMstMstiBridgeTable.setStatus("current")
_FsMstMstiBridgeEntry_Object = MibTableRow
fsMstMstiBridgeEntry = _FsMstMstiBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 38, 1)
)
fsMstMstiBridgeEntry.setIndexNames(
    (0, "SUPERMICRO-MST-MIB", "fsMstMstiInstanceIndex"),
)
if mibBuilder.loadTexts:
    fsMstMstiBridgeEntry.setStatus("current")


class _FsMstMstiInstanceIndex_Type(Integer32):
    """Custom type fsMstMstiInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
        ValueRangeConstraint(4094, 4094),
    )


_FsMstMstiInstanceIndex_Type.__name__ = "Integer32"
_FsMstMstiInstanceIndex_Object = MibTableColumn
fsMstMstiInstanceIndex = _FsMstMstiInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 38, 1, 1),
    _FsMstMstiInstanceIndex_Type()
)
fsMstMstiInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMstMstiInstanceIndex.setStatus("current")
_FsMstMstiBridgeRegionalRoot_Type = BridgeId
_FsMstMstiBridgeRegionalRoot_Object = MibTableColumn
fsMstMstiBridgeRegionalRoot = _FsMstMstiBridgeRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 38, 1, 2),
    _FsMstMstiBridgeRegionalRoot_Type()
)
fsMstMstiBridgeRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiBridgeRegionalRoot.setStatus("current")


class _FsMstMstiBridgePriority_Type(Integer32):
    """Custom type fsMstMstiBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_FsMstMstiBridgePriority_Type.__name__ = "Integer32"
_FsMstMstiBridgePriority_Object = MibTableColumn
fsMstMstiBridgePriority = _FsMstMstiBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 38, 1, 3),
    _FsMstMstiBridgePriority_Type()
)
fsMstMstiBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstMstiBridgePriority.setStatus("current")
_FsMstMstiRootCost_Type = Integer32
_FsMstMstiRootCost_Object = MibTableColumn
fsMstMstiRootCost = _FsMstMstiRootCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 38, 1, 4),
    _FsMstMstiRootCost_Type()
)
fsMstMstiRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiRootCost.setStatus("current")
_FsMstMstiRootPort_Type = Integer32
_FsMstMstiRootPort_Object = MibTableColumn
fsMstMstiRootPort = _FsMstMstiRootPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 38, 1, 5),
    _FsMstMstiRootPort_Type()
)
fsMstMstiRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiRootPort.setStatus("current")
_FsMstMstiTimeSinceTopologyChange_Type = TimeTicks
_FsMstMstiTimeSinceTopologyChange_Object = MibTableColumn
fsMstMstiTimeSinceTopologyChange = _FsMstMstiTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 38, 1, 6),
    _FsMstMstiTimeSinceTopologyChange_Type()
)
fsMstMstiTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiTimeSinceTopologyChange.setStatus("current")
if mibBuilder.loadTexts:
    fsMstMstiTimeSinceTopologyChange.setUnits("centi-seconds")
_FsMstMstiTopChanges_Type = Counter32
_FsMstMstiTopChanges_Object = MibTableColumn
fsMstMstiTopChanges = _FsMstMstiTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 38, 1, 7),
    _FsMstMstiTopChanges_Type()
)
fsMstMstiTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiTopChanges.setStatus("current")
_FsMstMstiNewRootBridgeCount_Type = Counter32
_FsMstMstiNewRootBridgeCount_Object = MibTableColumn
fsMstMstiNewRootBridgeCount = _FsMstMstiNewRootBridgeCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 38, 1, 8),
    _FsMstMstiNewRootBridgeCount_Type()
)
fsMstMstiNewRootBridgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiNewRootBridgeCount.setStatus("current")


class _FsMstMstiBridgeRoleSelectionSemState_Type(Integer32):
    """Custom type fsMstMstiBridgeRoleSelectionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("initbridge", 0),
          ("roleselection", 1))
    )


_FsMstMstiBridgeRoleSelectionSemState_Type.__name__ = "Integer32"
_FsMstMstiBridgeRoleSelectionSemState_Object = MibTableColumn
fsMstMstiBridgeRoleSelectionSemState = _FsMstMstiBridgeRoleSelectionSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 38, 1, 9),
    _FsMstMstiBridgeRoleSelectionSemState_Type()
)
fsMstMstiBridgeRoleSelectionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiBridgeRoleSelectionSemState.setStatus("current")
_FsMstInstanceUpCount_Type = Counter32
_FsMstInstanceUpCount_Object = MibTableColumn
fsMstInstanceUpCount = _FsMstInstanceUpCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 38, 1, 10),
    _FsMstInstanceUpCount_Type()
)
fsMstInstanceUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstInstanceUpCount.setStatus("current")
_FsMstInstanceDownCount_Type = Counter32
_FsMstInstanceDownCount_Object = MibTableColumn
fsMstInstanceDownCount = _FsMstInstanceDownCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 38, 1, 11),
    _FsMstInstanceDownCount_Type()
)
fsMstInstanceDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstInstanceDownCount.setStatus("current")
_FsMstOldDesignatedRoot_Type = BridgeId
_FsMstOldDesignatedRoot_Object = MibTableColumn
fsMstOldDesignatedRoot = _FsMstOldDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 38, 1, 12),
    _FsMstOldDesignatedRoot_Type()
)
fsMstOldDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstOldDesignatedRoot.setStatus("current")
_FsMstVlanInstanceMappingTable_Object = MibTable
fsMstVlanInstanceMappingTable = _FsMstVlanInstanceMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 39)
)
if mibBuilder.loadTexts:
    fsMstVlanInstanceMappingTable.setStatus("current")
_FsMstVlanInstanceMappingEntry_Object = MibTableRow
fsMstVlanInstanceMappingEntry = _FsMstVlanInstanceMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 39, 1)
)
fsMstVlanInstanceMappingEntry.setIndexNames(
    (0, "SUPERMICRO-MST-MIB", "fsMstInstanceIndex"),
)
if mibBuilder.loadTexts:
    fsMstVlanInstanceMappingEntry.setStatus("current")


class _FsMstInstanceIndex_Type(Integer32):
    """Custom type fsMstInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
        ValueRangeConstraint(4094, 4094),
    )


_FsMstInstanceIndex_Type.__name__ = "Integer32"
_FsMstInstanceIndex_Object = MibTableColumn
fsMstInstanceIndex = _FsMstInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 39, 1, 1),
    _FsMstInstanceIndex_Type()
)
fsMstInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMstInstanceIndex.setStatus("current")
_FsMstMapVlanIndex_Type = VlanId
_FsMstMapVlanIndex_Object = MibTableColumn
fsMstMapVlanIndex = _FsMstMapVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 39, 1, 2),
    _FsMstMapVlanIndex_Type()
)
fsMstMapVlanIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstMapVlanIndex.setStatus("current")
_FsMstUnMapVlanIndex_Type = VlanId
_FsMstUnMapVlanIndex_Object = MibTableColumn
fsMstUnMapVlanIndex = _FsMstUnMapVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 39, 1, 3),
    _FsMstUnMapVlanIndex_Type()
)
fsMstUnMapVlanIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstUnMapVlanIndex.setStatus("current")


class _FsMstSetVlanList_Type(OctetString):
    """Custom type fsMstSetVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_FsMstSetVlanList_Type.__name__ = "OctetString"
_FsMstSetVlanList_Object = MibTableColumn
fsMstSetVlanList = _FsMstSetVlanList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 39, 1, 4),
    _FsMstSetVlanList_Type()
)
fsMstSetVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstSetVlanList.setStatus("current")


class _FsMstResetVlanList_Type(OctetString):
    """Custom type fsMstResetVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_FsMstResetVlanList_Type.__name__ = "OctetString"
_FsMstResetVlanList_Object = MibTableColumn
fsMstResetVlanList = _FsMstResetVlanList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 39, 1, 5),
    _FsMstResetVlanList_Type()
)
fsMstResetVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstResetVlanList.setStatus("current")


class _FsMstInstanceVlanMapped_Type(OctetString):
    """Custom type fsMstInstanceVlanMapped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FsMstInstanceVlanMapped_Type.__name__ = "OctetString"
_FsMstInstanceVlanMapped_Object = MibTableColumn
fsMstInstanceVlanMapped = _FsMstInstanceVlanMapped_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 39, 1, 6),
    _FsMstInstanceVlanMapped_Type()
)
fsMstInstanceVlanMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstInstanceVlanMapped.setStatus("current")


class _FsMstInstanceVlanMapped2k_Type(OctetString):
    """Custom type fsMstInstanceVlanMapped2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FsMstInstanceVlanMapped2k_Type.__name__ = "OctetString"
_FsMstInstanceVlanMapped2k_Object = MibTableColumn
fsMstInstanceVlanMapped2k = _FsMstInstanceVlanMapped2k_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 39, 1, 7),
    _FsMstInstanceVlanMapped2k_Type()
)
fsMstInstanceVlanMapped2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstInstanceVlanMapped2k.setStatus("current")


class _FsMstInstanceVlanMapped3k_Type(OctetString):
    """Custom type fsMstInstanceVlanMapped3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FsMstInstanceVlanMapped3k_Type.__name__ = "OctetString"
_FsMstInstanceVlanMapped3k_Object = MibTableColumn
fsMstInstanceVlanMapped3k = _FsMstInstanceVlanMapped3k_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 39, 1, 8),
    _FsMstInstanceVlanMapped3k_Type()
)
fsMstInstanceVlanMapped3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstInstanceVlanMapped3k.setStatus("current")


class _FsMstInstanceVlanMapped4k_Type(OctetString):
    """Custom type fsMstInstanceVlanMapped4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FsMstInstanceVlanMapped4k_Type.__name__ = "OctetString"
_FsMstInstanceVlanMapped4k_Object = MibTableColumn
fsMstInstanceVlanMapped4k = _FsMstInstanceVlanMapped4k_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 39, 1, 9),
    _FsMstInstanceVlanMapped4k_Type()
)
fsMstInstanceVlanMapped4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstInstanceVlanMapped4k.setStatus("current")
_FsMstCistPortTable_Object = MibTable
fsMstCistPortTable = _FsMstCistPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40)
)
if mibBuilder.loadTexts:
    fsMstCistPortTable.setStatus("current")
_FsMstCistPortEntry_Object = MibTableRow
fsMstCistPortEntry = _FsMstCistPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1)
)
fsMstCistPortEntry.setIndexNames(
    (0, "SUPERMICRO-MST-MIB", "fsMstCistPort"),
)
if mibBuilder.loadTexts:
    fsMstCistPortEntry.setStatus("current")


class _FsMstCistPort_Type(Integer32):
    """Custom type fsMstCistPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMstCistPort_Type.__name__ = "Integer32"
_FsMstCistPort_Object = MibTableColumn
fsMstCistPort = _FsMstCistPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 1),
    _FsMstCistPort_Type()
)
fsMstCistPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMstCistPort.setStatus("current")


class _FsMstCistPortPathCost_Type(Integer32):
    """Custom type fsMstCistPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_FsMstCistPortPathCost_Type.__name__ = "Integer32"
_FsMstCistPortPathCost_Object = MibTableColumn
fsMstCistPortPathCost = _FsMstCistPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 2),
    _FsMstCistPortPathCost_Type()
)
fsMstCistPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstCistPortPathCost.setStatus("current")


class _FsMstCistPortPriority_Type(Integer32):
    """Custom type fsMstCistPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_FsMstCistPortPriority_Type.__name__ = "Integer32"
_FsMstCistPortPriority_Object = MibTableColumn
fsMstCistPortPriority = _FsMstCistPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 3),
    _FsMstCistPortPriority_Type()
)
fsMstCistPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstCistPortPriority.setStatus("current")
_FsMstCistPortDesignatedRoot_Type = BridgeId
_FsMstCistPortDesignatedRoot_Object = MibTableColumn
fsMstCistPortDesignatedRoot = _FsMstCistPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 4),
    _FsMstCistPortDesignatedRoot_Type()
)
fsMstCistPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortDesignatedRoot.setStatus("current")
_FsMstCistPortDesignatedBridge_Type = BridgeId
_FsMstCistPortDesignatedBridge_Object = MibTableColumn
fsMstCistPortDesignatedBridge = _FsMstCistPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 5),
    _FsMstCistPortDesignatedBridge_Type()
)
fsMstCistPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortDesignatedBridge.setStatus("current")


class _FsMstCistPortDesignatedPort_Type(OctetString):
    """Custom type fsMstCistPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_FsMstCistPortDesignatedPort_Type.__name__ = "OctetString"
_FsMstCistPortDesignatedPort_Object = MibTableColumn
fsMstCistPortDesignatedPort = _FsMstCistPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 6),
    _FsMstCistPortDesignatedPort_Type()
)
fsMstCistPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortDesignatedPort.setStatus("current")


class _FsMstCistPortAdminP2P_Type(Integer32):
    """Custom type fsMstCistPortAdminP2P based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceTrue", 0),
          ("forceFalse", 1),
          ("auto", 2))
    )


_FsMstCistPortAdminP2P_Type.__name__ = "Integer32"
_FsMstCistPortAdminP2P_Object = MibTableColumn
fsMstCistPortAdminP2P = _FsMstCistPortAdminP2P_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 7),
    _FsMstCistPortAdminP2P_Type()
)
fsMstCistPortAdminP2P.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstCistPortAdminP2P.setStatus("current")
_FsMstCistPortOperP2P_Type = TruthValue
_FsMstCistPortOperP2P_Object = MibTableColumn
fsMstCistPortOperP2P = _FsMstCistPortOperP2P_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 8),
    _FsMstCistPortOperP2P_Type()
)
fsMstCistPortOperP2P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortOperP2P.setStatus("current")
_FsMstCistPortAdminEdgeStatus_Type = TruthValue
_FsMstCistPortAdminEdgeStatus_Object = MibTableColumn
fsMstCistPortAdminEdgeStatus = _FsMstCistPortAdminEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 9),
    _FsMstCistPortAdminEdgeStatus_Type()
)
fsMstCistPortAdminEdgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstCistPortAdminEdgeStatus.setStatus("current")
_FsMstCistPortOperEdgeStatus_Type = TruthValue
_FsMstCistPortOperEdgeStatus_Object = MibTableColumn
fsMstCistPortOperEdgeStatus = _FsMstCistPortOperEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 10),
    _FsMstCistPortOperEdgeStatus_Type()
)
fsMstCistPortOperEdgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortOperEdgeStatus.setStatus("current")
_FsMstCistPortProtocolMigration_Type = TruthValue
_FsMstCistPortProtocolMigration_Object = MibTableColumn
fsMstCistPortProtocolMigration = _FsMstCistPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 11),
    _FsMstCistPortProtocolMigration_Type()
)
fsMstCistPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstCistPortProtocolMigration.setStatus("current")


class _FsMstCistPortState_Type(Integer32):
    """Custom type fsMstCistPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discarding", 2),
          ("learning", 4),
          ("forwarding", 5))
    )


_FsMstCistPortState_Type.__name__ = "Integer32"
_FsMstCistPortState_Object = MibTableColumn
fsMstCistPortState = _FsMstCistPortState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 12),
    _FsMstCistPortState_Type()
)
fsMstCistPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortState.setStatus("current")


class _FsMstCistForcePortState_Type(Integer32):
    """Custom type fsMstCistForcePortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_FsMstCistForcePortState_Type.__name__ = "Integer32"
_FsMstCistForcePortState_Object = MibTableColumn
fsMstCistForcePortState = _FsMstCistForcePortState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 13),
    _FsMstCistForcePortState_Type()
)
fsMstCistForcePortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstCistForcePortState.setStatus("current")
_FsMstCistPortForwardTransitions_Type = Counter32
_FsMstCistPortForwardTransitions_Object = MibTableColumn
fsMstCistPortForwardTransitions = _FsMstCistPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 14),
    _FsMstCistPortForwardTransitions_Type()
)
fsMstCistPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortForwardTransitions.setStatus("current")
_FsMstCistPortRxMstBpduCount_Type = Counter32
_FsMstCistPortRxMstBpduCount_Object = MibTableColumn
fsMstCistPortRxMstBpduCount = _FsMstCistPortRxMstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 15),
    _FsMstCistPortRxMstBpduCount_Type()
)
fsMstCistPortRxMstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortRxMstBpduCount.setStatus("current")
_FsMstCistPortRxRstBpduCount_Type = Counter32
_FsMstCistPortRxRstBpduCount_Object = MibTableColumn
fsMstCistPortRxRstBpduCount = _FsMstCistPortRxRstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 16),
    _FsMstCistPortRxRstBpduCount_Type()
)
fsMstCistPortRxRstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortRxRstBpduCount.setStatus("current")
_FsMstCistPortRxConfigBpduCount_Type = Counter32
_FsMstCistPortRxConfigBpduCount_Object = MibTableColumn
fsMstCistPortRxConfigBpduCount = _FsMstCistPortRxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 17),
    _FsMstCistPortRxConfigBpduCount_Type()
)
fsMstCistPortRxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortRxConfigBpduCount.setStatus("current")
_FsMstCistPortRxTcnBpduCount_Type = Counter32
_FsMstCistPortRxTcnBpduCount_Object = MibTableColumn
fsMstCistPortRxTcnBpduCount = _FsMstCistPortRxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 18),
    _FsMstCistPortRxTcnBpduCount_Type()
)
fsMstCistPortRxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortRxTcnBpduCount.setStatus("current")
_FsMstCistPortTxMstBpduCount_Type = Counter32
_FsMstCistPortTxMstBpduCount_Object = MibTableColumn
fsMstCistPortTxMstBpduCount = _FsMstCistPortTxMstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 19),
    _FsMstCistPortTxMstBpduCount_Type()
)
fsMstCistPortTxMstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortTxMstBpduCount.setStatus("current")
_FsMstCistPortTxRstBpduCount_Type = Counter32
_FsMstCistPortTxRstBpduCount_Object = MibTableColumn
fsMstCistPortTxRstBpduCount = _FsMstCistPortTxRstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 20),
    _FsMstCistPortTxRstBpduCount_Type()
)
fsMstCistPortTxRstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortTxRstBpduCount.setStatus("current")
_FsMstCistPortTxConfigBpduCount_Type = Counter32
_FsMstCistPortTxConfigBpduCount_Object = MibTableColumn
fsMstCistPortTxConfigBpduCount = _FsMstCistPortTxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 21),
    _FsMstCistPortTxConfigBpduCount_Type()
)
fsMstCistPortTxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortTxConfigBpduCount.setStatus("current")
_FsMstCistPortTxTcnBpduCount_Type = Counter32
_FsMstCistPortTxTcnBpduCount_Object = MibTableColumn
fsMstCistPortTxTcnBpduCount = _FsMstCistPortTxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 22),
    _FsMstCistPortTxTcnBpduCount_Type()
)
fsMstCistPortTxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortTxTcnBpduCount.setStatus("current")
_FsMstCistPortInvalidMstBpduRxCount_Type = Counter32
_FsMstCistPortInvalidMstBpduRxCount_Object = MibTableColumn
fsMstCistPortInvalidMstBpduRxCount = _FsMstCistPortInvalidMstBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 23),
    _FsMstCistPortInvalidMstBpduRxCount_Type()
)
fsMstCistPortInvalidMstBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortInvalidMstBpduRxCount.setStatus("current")
_FsMstCistPortInvalidRstBpduRxCount_Type = Counter32
_FsMstCistPortInvalidRstBpduRxCount_Object = MibTableColumn
fsMstCistPortInvalidRstBpduRxCount = _FsMstCistPortInvalidRstBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 24),
    _FsMstCistPortInvalidRstBpduRxCount_Type()
)
fsMstCistPortInvalidRstBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortInvalidRstBpduRxCount.setStatus("current")
_FsMstCistPortInvalidConfigBpduRxCount_Type = Counter32
_FsMstCistPortInvalidConfigBpduRxCount_Object = MibTableColumn
fsMstCistPortInvalidConfigBpduRxCount = _FsMstCistPortInvalidConfigBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 25),
    _FsMstCistPortInvalidConfigBpduRxCount_Type()
)
fsMstCistPortInvalidConfigBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortInvalidConfigBpduRxCount.setStatus("current")
_FsMstCistPortInvalidTcnBpduRxCount_Type = Counter32
_FsMstCistPortInvalidTcnBpduRxCount_Object = MibTableColumn
fsMstCistPortInvalidTcnBpduRxCount = _FsMstCistPortInvalidTcnBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 26),
    _FsMstCistPortInvalidTcnBpduRxCount_Type()
)
fsMstCistPortInvalidTcnBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortInvalidTcnBpduRxCount.setStatus("current")


class _FsMstCistPortTransmitSemState_Type(Integer32):
    """Custom type fsMstCistPortTransmitSemState based on Integer32"""
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
        *(("transmitinit", 0),
          ("transmitperiodic", 1),
          ("transmitconfig", 2),
          ("transmittcn", 3),
          ("transmitrstp", 4),
          ("idle", 5))
    )


_FsMstCistPortTransmitSemState_Type.__name__ = "Integer32"
_FsMstCistPortTransmitSemState_Object = MibTableColumn
fsMstCistPortTransmitSemState = _FsMstCistPortTransmitSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 27),
    _FsMstCistPortTransmitSemState_Type()
)
fsMstCistPortTransmitSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortTransmitSemState.setStatus("current")


class _FsMstCistPortReceiveSemState_Type(Integer32):
    """Custom type fsMstCistPortReceiveSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("discard", 0),
          ("receive", 1))
    )


_FsMstCistPortReceiveSemState_Type.__name__ = "Integer32"
_FsMstCistPortReceiveSemState_Object = MibTableColumn
fsMstCistPortReceiveSemState = _FsMstCistPortReceiveSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 28),
    _FsMstCistPortReceiveSemState_Type()
)
fsMstCistPortReceiveSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortReceiveSemState.setStatus("current")


class _FsMstCistPortProtMigrationSemState_Type(Integer32):
    """Custom type fsMstCistPortProtMigrationSemState based on Integer32"""
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
        *(("init", 0),
          ("sendrstp", 1),
          ("sendingrstp", 2),
          ("sendstp", 3),
          ("sendingstp", 4))
    )


_FsMstCistPortProtMigrationSemState_Type.__name__ = "Integer32"
_FsMstCistPortProtMigrationSemState_Object = MibTableColumn
fsMstCistPortProtMigrationSemState = _FsMstCistPortProtMigrationSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 29),
    _FsMstCistPortProtMigrationSemState_Type()
)
fsMstCistPortProtMigrationSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortProtMigrationSemState.setStatus("current")
_FsMstCistProtocolMigrationCount_Type = Counter32
_FsMstCistProtocolMigrationCount_Object = MibTableColumn
fsMstCistProtocolMigrationCount = _FsMstCistProtocolMigrationCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 30),
    _FsMstCistProtocolMigrationCount_Type()
)
fsMstCistProtocolMigrationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistProtocolMigrationCount.setStatus("current")
_FsMstCistPortDesignatedCost_Type = Integer32
_FsMstCistPortDesignatedCost_Object = MibTableColumn
fsMstCistPortDesignatedCost = _FsMstCistPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 31),
    _FsMstCistPortDesignatedCost_Type()
)
fsMstCistPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortDesignatedCost.setStatus("current")
_FsMstCistPortRegionalRoot_Type = BridgeId
_FsMstCistPortRegionalRoot_Object = MibTableColumn
fsMstCistPortRegionalRoot = _FsMstCistPortRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 32),
    _FsMstCistPortRegionalRoot_Type()
)
fsMstCistPortRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortRegionalRoot.setStatus("current")
_FsMstCistPortRegionalPathCost_Type = Integer32
_FsMstCistPortRegionalPathCost_Object = MibTableColumn
fsMstCistPortRegionalPathCost = _FsMstCistPortRegionalPathCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 33),
    _FsMstCistPortRegionalPathCost_Type()
)
fsMstCistPortRegionalPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortRegionalPathCost.setStatus("current")


class _FsMstCistSelectedPortRole_Type(Integer32):
    """Custom type fsMstCistSelectedPortRole based on Integer32"""
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
        *(("disabled", 0),
          ("alternate", 1),
          ("backup", 2),
          ("root", 3),
          ("designated", 4))
    )


_FsMstCistSelectedPortRole_Type.__name__ = "Integer32"
_FsMstCistSelectedPortRole_Object = MibTableColumn
fsMstCistSelectedPortRole = _FsMstCistSelectedPortRole_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 34),
    _FsMstCistSelectedPortRole_Type()
)
fsMstCistSelectedPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistSelectedPortRole.setStatus("current")


class _FsMstCistCurrentPortRole_Type(Integer32):
    """Custom type fsMstCistCurrentPortRole based on Integer32"""
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
        *(("disabled", 0),
          ("alternate", 1),
          ("backup", 2),
          ("root", 3),
          ("designated", 4))
    )


_FsMstCistCurrentPortRole_Type.__name__ = "Integer32"
_FsMstCistCurrentPortRole_Object = MibTableColumn
fsMstCistCurrentPortRole = _FsMstCistCurrentPortRole_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 35),
    _FsMstCistCurrentPortRole_Type()
)
fsMstCistCurrentPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistCurrentPortRole.setStatus("current")


class _FsMstCistPortInfoSemState_Type(Integer32):
    """Custom type fsMstCistPortInfoSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("aged", 1),
          ("update", 2),
          ("superiordesg", 3),
          ("repeatdesg", 4),
          ("inferiordesg", 5),
          ("notdesg", 6),
          ("present", 7),
          ("receive", 8),
          ("other", 9))
    )


_FsMstCistPortInfoSemState_Type.__name__ = "Integer32"
_FsMstCistPortInfoSemState_Object = MibTableColumn
fsMstCistPortInfoSemState = _FsMstCistPortInfoSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 36),
    _FsMstCistPortInfoSemState_Type()
)
fsMstCistPortInfoSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortInfoSemState.setStatus("current")


class _FsMstCistPortRoleTransitionSemState_Type(Integer32):
    """Custom type fsMstCistPortRoleTransitionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("init", 0),
          ("disableport", 1),
          ("disabledport", 2),
          ("rootport", 3),
          ("designatedport", 4),
          ("alternateport", 5),
          ("masterport", 6))
    )


_FsMstCistPortRoleTransitionSemState_Type.__name__ = "Integer32"
_FsMstCistPortRoleTransitionSemState_Object = MibTableColumn
fsMstCistPortRoleTransitionSemState = _FsMstCistPortRoleTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 37),
    _FsMstCistPortRoleTransitionSemState_Type()
)
fsMstCistPortRoleTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortRoleTransitionSemState.setStatus("current")


class _FsMstCistPortStateTransitionSemState_Type(Integer32):
    """Custom type fsMstCistPortStateTransitionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 0),
          ("learning", 1),
          ("forwarding", 2))
    )


_FsMstCistPortStateTransitionSemState_Type.__name__ = "Integer32"
_FsMstCistPortStateTransitionSemState_Object = MibTableColumn
fsMstCistPortStateTransitionSemState = _FsMstCistPortStateTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 38),
    _FsMstCistPortStateTransitionSemState_Type()
)
fsMstCistPortStateTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortStateTransitionSemState.setStatus("current")


class _FsMstCistPortTopologyChangeSemState_Type(Integer32):
    """Custom type fsMstCistPortTopologyChangeSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("learning", 1),
          ("detected", 2),
          ("active", 3),
          ("notifiedtcn", 4),
          ("notifiedtc", 5),
          ("propagating", 6),
          ("acknowledged", 7))
    )


_FsMstCistPortTopologyChangeSemState_Type.__name__ = "Integer32"
_FsMstCistPortTopologyChangeSemState_Object = MibTableColumn
fsMstCistPortTopologyChangeSemState = _FsMstCistPortTopologyChangeSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 39),
    _FsMstCistPortTopologyChangeSemState_Type()
)
fsMstCistPortTopologyChangeSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortTopologyChangeSemState.setStatus("current")


class _FsMstCistPortHelloTime_Type(Timeout):
    """Custom type fsMstCistPortHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(200, 200),
    )


_FsMstCistPortHelloTime_Type.__name__ = "Timeout"
_FsMstCistPortHelloTime_Object = MibTableColumn
fsMstCistPortHelloTime = _FsMstCistPortHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 40),
    _FsMstCistPortHelloTime_Type()
)
fsMstCistPortHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstCistPortHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    fsMstCistPortHelloTime.setUnits("centi-seconds")


class _FsMstCistPortOperVersion_Type(Integer32):
    """Custom type fsMstCistPortOperVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stpCompatible", 0),
          ("rstp", 2),
          ("mstp", 3))
    )


_FsMstCistPortOperVersion_Type.__name__ = "Integer32"
_FsMstCistPortOperVersion_Object = MibTableColumn
fsMstCistPortOperVersion = _FsMstCistPortOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 41),
    _FsMstCistPortOperVersion_Type()
)
fsMstCistPortOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortOperVersion.setStatus("current")
_FsMstCistPortEffectivePortState_Type = TruthValue
_FsMstCistPortEffectivePortState_Object = MibTableColumn
fsMstCistPortEffectivePortState = _FsMstCistPortEffectivePortState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 42),
    _FsMstCistPortEffectivePortState_Type()
)
fsMstCistPortEffectivePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortEffectivePortState.setStatus("current")
_FsMstCistPortAutoEdgeStatus_Type = TruthValue
_FsMstCistPortAutoEdgeStatus_Object = MibTableColumn
fsMstCistPortAutoEdgeStatus = _FsMstCistPortAutoEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 43),
    _FsMstCistPortAutoEdgeStatus_Type()
)
fsMstCistPortAutoEdgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstCistPortAutoEdgeStatus.setStatus("current")
_FsMstCistPortRestrictedRole_Type = TruthValue
_FsMstCistPortRestrictedRole_Object = MibTableColumn
fsMstCistPortRestrictedRole = _FsMstCistPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 44),
    _FsMstCistPortRestrictedRole_Type()
)
fsMstCistPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstCistPortRestrictedRole.setStatus("current")
_FsMstCistPortRestrictedTCN_Type = TruthValue
_FsMstCistPortRestrictedTCN_Object = MibTableColumn
fsMstCistPortRestrictedTCN = _FsMstCistPortRestrictedTCN_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 45),
    _FsMstCistPortRestrictedTCN_Type()
)
fsMstCistPortRestrictedTCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstCistPortRestrictedTCN.setStatus("current")


class _FsMstCistPortAdminPathCost_Type(Integer32):
    """Custom type fsMstCistPortAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_FsMstCistPortAdminPathCost_Type.__name__ = "Integer32"
_FsMstCistPortAdminPathCost_Object = MibTableColumn
fsMstCistPortAdminPathCost = _FsMstCistPortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 46),
    _FsMstCistPortAdminPathCost_Type()
)
fsMstCistPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstCistPortAdminPathCost.setStatus("current")


class _FsMstCistPortEnableBPDURx_Type(TruthValue):
    """Custom type fsMstCistPortEnableBPDURx based on TruthValue"""
    defaultValue = 1


_FsMstCistPortEnableBPDURx_Type.__name__ = "TruthValue"
_FsMstCistPortEnableBPDURx_Object = MibTableColumn
fsMstCistPortEnableBPDURx = _FsMstCistPortEnableBPDURx_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 47),
    _FsMstCistPortEnableBPDURx_Type()
)
fsMstCistPortEnableBPDURx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstCistPortEnableBPDURx.setStatus("current")


class _FsMstCistPortEnableBPDUTx_Type(TruthValue):
    """Custom type fsMstCistPortEnableBPDUTx based on TruthValue"""
    defaultValue = 1


_FsMstCistPortEnableBPDUTx_Type.__name__ = "TruthValue"
_FsMstCistPortEnableBPDUTx_Object = MibTableColumn
fsMstCistPortEnableBPDUTx = _FsMstCistPortEnableBPDUTx_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 48),
    _FsMstCistPortEnableBPDUTx_Type()
)
fsMstCistPortEnableBPDUTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstCistPortEnableBPDUTx.setStatus("current")
_FsMstCistPortPseudoRootId_Type = BridgeId
_FsMstCistPortPseudoRootId_Object = MibTableColumn
fsMstCistPortPseudoRootId = _FsMstCistPortPseudoRootId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 49),
    _FsMstCistPortPseudoRootId_Type()
)
fsMstCistPortPseudoRootId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstCistPortPseudoRootId.setStatus("current")


class _FsMstCistPortIsL2Gp_Type(TruthValue):
    """Custom type fsMstCistPortIsL2Gp based on TruthValue"""
    defaultValue = 2


_FsMstCistPortIsL2Gp_Type.__name__ = "TruthValue"
_FsMstCistPortIsL2Gp_Object = MibTableColumn
fsMstCistPortIsL2Gp = _FsMstCistPortIsL2Gp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 50),
    _FsMstCistPortIsL2Gp_Type()
)
fsMstCistPortIsL2Gp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstCistPortIsL2Gp.setStatus("current")


class _FsMstCistPortLoopGuard_Type(TruthValue):
    """Custom type fsMstCistPortLoopGuard based on TruthValue"""
    defaultValue = 2


_FsMstCistPortLoopGuard_Type.__name__ = "TruthValue"
_FsMstCistPortLoopGuard_Object = MibTableColumn
fsMstCistPortLoopGuard = _FsMstCistPortLoopGuard_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 51),
    _FsMstCistPortLoopGuard_Type()
)
fsMstCistPortLoopGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstCistPortLoopGuard.setStatus("current")


class _FsMstCistPortRcvdEvent_Type(Integer32):
    """Custom type fsMstCistPortRcvdEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configurationEvent", 1),
          ("bpduEvent", 2),
          ("timerExpiryEvent", 3))
    )


_FsMstCistPortRcvdEvent_Type.__name__ = "Integer32"
_FsMstCistPortRcvdEvent_Object = MibTableColumn
fsMstCistPortRcvdEvent = _FsMstCistPortRcvdEvent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 52),
    _FsMstCistPortRcvdEvent_Type()
)
fsMstCistPortRcvdEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortRcvdEvent.setStatus("current")
_FsMstCistPortRcvdEventSubType_Type = Integer32
_FsMstCistPortRcvdEventSubType_Object = MibTableColumn
fsMstCistPortRcvdEventSubType = _FsMstCistPortRcvdEventSubType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 53),
    _FsMstCistPortRcvdEventSubType_Type()
)
fsMstCistPortRcvdEventSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortRcvdEventSubType.setStatus("current")
_FsMstCistPortRcvdEventTimeStamp_Type = Unsigned32
_FsMstCistPortRcvdEventTimeStamp_Object = MibTableColumn
fsMstCistPortRcvdEventTimeStamp = _FsMstCistPortRcvdEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 54),
    _FsMstCistPortRcvdEventTimeStamp_Type()
)
fsMstCistPortRcvdEventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstCistPortRcvdEventTimeStamp.setStatus("current")


class _FsMstCistPortBpduGuard_Type(Integer32):
    """Custom type fsMstCistPortBpduGuard based on Integer32"""
    defaultValue = 0

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
          ("enable", 1),
          ("disable", 2))
    )


_FsMstCistPortBpduGuard_Type.__name__ = "Integer32"
_FsMstCistPortBpduGuard_Object = MibTableColumn
fsMstCistPortBpduGuard = _FsMstCistPortBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 40, 1, 55),
    _FsMstCistPortBpduGuard_Type()
)
fsMstCistPortBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstCistPortBpduGuard.setStatus("current")
_FsMstMstiPortTable_Object = MibTable
fsMstMstiPortTable = _FsMstMstiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41)
)
if mibBuilder.loadTexts:
    fsMstMstiPortTable.setStatus("current")
_FsMstMstiPortEntry_Object = MibTableRow
fsMstMstiPortEntry = _FsMstMstiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41, 1)
)
fsMstMstiPortEntry.setIndexNames(
    (0, "SUPERMICRO-MST-MIB", "fsMstMstiPort"),
    (0, "SUPERMICRO-MST-MIB", "fsMstInstanceIndex"),
)
if mibBuilder.loadTexts:
    fsMstMstiPortEntry.setStatus("current")


class _FsMstMstiPort_Type(Integer32):
    """Custom type fsMstMstiPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMstMstiPort_Type.__name__ = "Integer32"
_FsMstMstiPort_Object = MibTableColumn
fsMstMstiPort = _FsMstMstiPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41, 1, 1),
    _FsMstMstiPort_Type()
)
fsMstMstiPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMstMstiPort.setStatus("current")


class _FsMstMstiPortPathCost_Type(Integer32):
    """Custom type fsMstMstiPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_FsMstMstiPortPathCost_Type.__name__ = "Integer32"
_FsMstMstiPortPathCost_Object = MibTableColumn
fsMstMstiPortPathCost = _FsMstMstiPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41, 1, 2),
    _FsMstMstiPortPathCost_Type()
)
fsMstMstiPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstMstiPortPathCost.setStatus("current")


class _FsMstMstiPortPriority_Type(Integer32):
    """Custom type fsMstMstiPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_FsMstMstiPortPriority_Type.__name__ = "Integer32"
_FsMstMstiPortPriority_Object = MibTableColumn
fsMstMstiPortPriority = _FsMstMstiPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41, 1, 3),
    _FsMstMstiPortPriority_Type()
)
fsMstMstiPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstMstiPortPriority.setStatus("current")
_FsMstMstiPortDesignatedRoot_Type = BridgeId
_FsMstMstiPortDesignatedRoot_Object = MibTableColumn
fsMstMstiPortDesignatedRoot = _FsMstMstiPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41, 1, 4),
    _FsMstMstiPortDesignatedRoot_Type()
)
fsMstMstiPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiPortDesignatedRoot.setStatus("current")
_FsMstMstiPortDesignatedBridge_Type = BridgeId
_FsMstMstiPortDesignatedBridge_Object = MibTableColumn
fsMstMstiPortDesignatedBridge = _FsMstMstiPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41, 1, 5),
    _FsMstMstiPortDesignatedBridge_Type()
)
fsMstMstiPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiPortDesignatedBridge.setStatus("current")


class _FsMstMstiPortDesignatedPort_Type(OctetString):
    """Custom type fsMstMstiPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_FsMstMstiPortDesignatedPort_Type.__name__ = "OctetString"
_FsMstMstiPortDesignatedPort_Object = MibTableColumn
fsMstMstiPortDesignatedPort = _FsMstMstiPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41, 1, 6),
    _FsMstMstiPortDesignatedPort_Type()
)
fsMstMstiPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiPortDesignatedPort.setStatus("current")


class _FsMstMstiPortState_Type(Integer32):
    """Custom type fsMstMstiPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discarding", 2),
          ("learning", 4),
          ("forwarding", 5))
    )


_FsMstMstiPortState_Type.__name__ = "Integer32"
_FsMstMstiPortState_Object = MibTableColumn
fsMstMstiPortState = _FsMstMstiPortState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41, 1, 7),
    _FsMstMstiPortState_Type()
)
fsMstMstiPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiPortState.setStatus("current")


class _FsMstMstiForcePortState_Type(Integer32):
    """Custom type fsMstMstiForcePortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_FsMstMstiForcePortState_Type.__name__ = "Integer32"
_FsMstMstiForcePortState_Object = MibTableColumn
fsMstMstiForcePortState = _FsMstMstiForcePortState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41, 1, 8),
    _FsMstMstiForcePortState_Type()
)
fsMstMstiForcePortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstMstiForcePortState.setStatus("current")
_FsMstMstiPortForwardTransitions_Type = Counter32
_FsMstMstiPortForwardTransitions_Object = MibTableColumn
fsMstMstiPortForwardTransitions = _FsMstMstiPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41, 1, 9),
    _FsMstMstiPortForwardTransitions_Type()
)
fsMstMstiPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiPortForwardTransitions.setStatus("current")
_FsMstMstiPortReceivedBPDUs_Type = Counter32
_FsMstMstiPortReceivedBPDUs_Object = MibTableColumn
fsMstMstiPortReceivedBPDUs = _FsMstMstiPortReceivedBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41, 1, 10),
    _FsMstMstiPortReceivedBPDUs_Type()
)
fsMstMstiPortReceivedBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiPortReceivedBPDUs.setStatus("current")
_FsMstMstiPortTransmittedBPDUs_Type = Counter32
_FsMstMstiPortTransmittedBPDUs_Object = MibTableColumn
fsMstMstiPortTransmittedBPDUs = _FsMstMstiPortTransmittedBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41, 1, 11),
    _FsMstMstiPortTransmittedBPDUs_Type()
)
fsMstMstiPortTransmittedBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiPortTransmittedBPDUs.setStatus("current")
_FsMstMstiPortInvalidBPDUsRcvd_Type = Counter32
_FsMstMstiPortInvalidBPDUsRcvd_Object = MibTableColumn
fsMstMstiPortInvalidBPDUsRcvd = _FsMstMstiPortInvalidBPDUsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41, 1, 12),
    _FsMstMstiPortInvalidBPDUsRcvd_Type()
)
fsMstMstiPortInvalidBPDUsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiPortInvalidBPDUsRcvd.setStatus("current")
_FsMstMstiPortDesignatedCost_Type = Integer32
_FsMstMstiPortDesignatedCost_Object = MibTableColumn
fsMstMstiPortDesignatedCost = _FsMstMstiPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41, 1, 13),
    _FsMstMstiPortDesignatedCost_Type()
)
fsMstMstiPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiPortDesignatedCost.setStatus("current")


class _FsMstMstiSelectedPortRole_Type(Integer32):
    """Custom type fsMstMstiSelectedPortRole based on Integer32"""
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
        *(("disabled", 0),
          ("alternate", 1),
          ("backup", 2),
          ("root", 3),
          ("designated", 4),
          ("master", 5))
    )


_FsMstMstiSelectedPortRole_Type.__name__ = "Integer32"
_FsMstMstiSelectedPortRole_Object = MibTableColumn
fsMstMstiSelectedPortRole = _FsMstMstiSelectedPortRole_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41, 1, 14),
    _FsMstMstiSelectedPortRole_Type()
)
fsMstMstiSelectedPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiSelectedPortRole.setStatus("current")


class _FsMstMstiCurrentPortRole_Type(Integer32):
    """Custom type fsMstMstiCurrentPortRole based on Integer32"""
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
        *(("disabled", 0),
          ("alternate", 1),
          ("backup", 2),
          ("root", 3),
          ("designated", 4),
          ("master", 5))
    )


_FsMstMstiCurrentPortRole_Type.__name__ = "Integer32"
_FsMstMstiCurrentPortRole_Object = MibTableColumn
fsMstMstiCurrentPortRole = _FsMstMstiCurrentPortRole_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41, 1, 15),
    _FsMstMstiCurrentPortRole_Type()
)
fsMstMstiCurrentPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiCurrentPortRole.setStatus("current")


class _FsMstMstiPortInfoSemState_Type(Integer32):
    """Custom type fsMstMstiPortInfoSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("aged", 1),
          ("update", 2),
          ("superiordesg", 3),
          ("repeatdesg", 4),
          ("inferiordesg", 5),
          ("notdesg", 6),
          ("present", 7),
          ("receive", 8),
          ("other", 9))
    )


_FsMstMstiPortInfoSemState_Type.__name__ = "Integer32"
_FsMstMstiPortInfoSemState_Object = MibTableColumn
fsMstMstiPortInfoSemState = _FsMstMstiPortInfoSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41, 1, 16),
    _FsMstMstiPortInfoSemState_Type()
)
fsMstMstiPortInfoSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiPortInfoSemState.setStatus("current")


class _FsMstMstiPortRoleTransitionSemState_Type(Integer32):
    """Custom type fsMstMstiPortRoleTransitionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("init", 0),
          ("disableport", 1),
          ("disabledport", 2),
          ("rootport", 3),
          ("designatedport", 4),
          ("alternateport", 5),
          ("masterport", 6))
    )


_FsMstMstiPortRoleTransitionSemState_Type.__name__ = "Integer32"
_FsMstMstiPortRoleTransitionSemState_Object = MibTableColumn
fsMstMstiPortRoleTransitionSemState = _FsMstMstiPortRoleTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41, 1, 17),
    _FsMstMstiPortRoleTransitionSemState_Type()
)
fsMstMstiPortRoleTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiPortRoleTransitionSemState.setStatus("current")


class _FsMstMstiPortStateTransitionSemState_Type(Integer32):
    """Custom type fsMstMstiPortStateTransitionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 0),
          ("learning", 1),
          ("forwarding", 2))
    )


_FsMstMstiPortStateTransitionSemState_Type.__name__ = "Integer32"
_FsMstMstiPortStateTransitionSemState_Object = MibTableColumn
fsMstMstiPortStateTransitionSemState = _FsMstMstiPortStateTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41, 1, 18),
    _FsMstMstiPortStateTransitionSemState_Type()
)
fsMstMstiPortStateTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiPortStateTransitionSemState.setStatus("current")


class _FsMstMstiPortTopologyChangeSemState_Type(Integer32):
    """Custom type fsMstMstiPortTopologyChangeSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("learning", 1),
          ("detected", 2),
          ("active", 3),
          ("notifiedtcn", 4),
          ("notifiedtc", 5),
          ("propagating", 6),
          ("acknowledged", 7))
    )


_FsMstMstiPortTopologyChangeSemState_Type.__name__ = "Integer32"
_FsMstMstiPortTopologyChangeSemState_Object = MibTableColumn
fsMstMstiPortTopologyChangeSemState = _FsMstMstiPortTopologyChangeSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41, 1, 19),
    _FsMstMstiPortTopologyChangeSemState_Type()
)
fsMstMstiPortTopologyChangeSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiPortTopologyChangeSemState.setStatus("current")
_FsMstMstiPortEffectivePortState_Type = TruthValue
_FsMstMstiPortEffectivePortState_Object = MibTableColumn
fsMstMstiPortEffectivePortState = _FsMstMstiPortEffectivePortState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41, 1, 20),
    _FsMstMstiPortEffectivePortState_Type()
)
fsMstMstiPortEffectivePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiPortEffectivePortState.setStatus("current")


class _FsMstMstiPortAdminPathCost_Type(Integer32):
    """Custom type fsMstMstiPortAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_FsMstMstiPortAdminPathCost_Type.__name__ = "Integer32"
_FsMstMstiPortAdminPathCost_Object = MibTableColumn
fsMstMstiPortAdminPathCost = _FsMstMstiPortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41, 1, 21),
    _FsMstMstiPortAdminPathCost_Type()
)
fsMstMstiPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstMstiPortAdminPathCost.setStatus("current")
_FsMstMstiPortPseudoRootId_Type = BridgeId
_FsMstMstiPortPseudoRootId_Object = MibTableColumn
fsMstMstiPortPseudoRootId = _FsMstMstiPortPseudoRootId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41, 1, 22),
    _FsMstMstiPortPseudoRootId_Type()
)
fsMstMstiPortPseudoRootId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstMstiPortPseudoRootId.setStatus("current")
_FsMstMstiPortStateChangeTimeStamp_Type = Unsigned32
_FsMstMstiPortStateChangeTimeStamp_Object = MibTableColumn
fsMstMstiPortStateChangeTimeStamp = _FsMstMstiPortStateChangeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 41, 1, 23),
    _FsMstMstiPortStateChangeTimeStamp_Type()
)
fsMstMstiPortStateChangeTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstMstiPortStateChangeTimeStamp.setStatus("current")


class _FsMstCistDynamicPathcostCalculation_Type(TruthValue):
    """Custom type fsMstCistDynamicPathcostCalculation based on TruthValue"""
    defaultValue = 2


_FsMstCistDynamicPathcostCalculation_Type.__name__ = "TruthValue"
_FsMstCistDynamicPathcostCalculation_Object = MibScalar
fsMstCistDynamicPathcostCalculation = _FsMstCistDynamicPathcostCalculation_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 42),
    _FsMstCistDynamicPathcostCalculation_Type()
)
fsMstCistDynamicPathcostCalculation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstCistDynamicPathcostCalculation.setStatus("current")


class _FsMstCalcPortPathCostOnSpeedChg_Type(TruthValue):
    """Custom type fsMstCalcPortPathCostOnSpeedChg based on TruthValue"""
    defaultValue = 2


_FsMstCalcPortPathCostOnSpeedChg_Type.__name__ = "TruthValue"
_FsMstCalcPortPathCostOnSpeedChg_Object = MibScalar
fsMstCalcPortPathCostOnSpeedChg = _FsMstCalcPortPathCostOnSpeedChg_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 43),
    _FsMstCalcPortPathCostOnSpeedChg_Type()
)
fsMstCalcPortPathCostOnSpeedChg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstCalcPortPathCostOnSpeedChg.setStatus("current")


class _FsMstRcvdEvent_Type(Integer32):
    """Custom type fsMstRcvdEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configurationEvent", 1),
          ("bpduEvent", 2),
          ("timerExpiryEvent", 3))
    )


_FsMstRcvdEvent_Type.__name__ = "Integer32"
_FsMstRcvdEvent_Object = MibScalar
fsMstRcvdEvent = _FsMstRcvdEvent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 44),
    _FsMstRcvdEvent_Type()
)
fsMstRcvdEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstRcvdEvent.setStatus("current")
_FsMstRcvdEventSubType_Type = Integer32
_FsMstRcvdEventSubType_Object = MibScalar
fsMstRcvdEventSubType = _FsMstRcvdEventSubType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 45),
    _FsMstRcvdEventSubType_Type()
)
fsMstRcvdEventSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstRcvdEventSubType.setStatus("current")
_FsMstRcvdEventTimeStamp_Type = Unsigned32
_FsMstRcvdEventTimeStamp_Object = MibScalar
fsMstRcvdEventTimeStamp = _FsMstRcvdEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 46),
    _FsMstRcvdEventTimeStamp_Type()
)
fsMstRcvdEventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstRcvdEventTimeStamp.setStatus("current")
_FsMstPortStateChangeTimeStamp_Type = Unsigned32
_FsMstPortStateChangeTimeStamp_Object = MibScalar
fsMstPortStateChangeTimeStamp = _FsMstPortStateChangeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 47),
    _FsMstPortStateChangeTimeStamp_Type()
)
fsMstPortStateChangeTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstPortStateChangeTimeStamp.setStatus("current")
_FsMstPortExtTable_Object = MibTable
fsMstPortExtTable = _FsMstPortExtTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 48)
)
if mibBuilder.loadTexts:
    fsMstPortExtTable.setStatus("current")
_FsMstPortExtEntry_Object = MibTableRow
fsMstPortExtEntry = _FsMstPortExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 48, 1)
)
fsMstPortExtEntry.setIndexNames(
    (0, "SUPERMICRO-MST-MIB", "fsMstPort"),
)
if mibBuilder.loadTexts:
    fsMstPortExtEntry.setStatus("current")


class _FsMstPort_Type(Integer32):
    """Custom type fsMstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_FsMstPort_Type.__name__ = "Integer32"
_FsMstPort_Object = MibTableColumn
fsMstPort = _FsMstPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 48, 1, 1),
    _FsMstPort_Type()
)
fsMstPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMstPort.setStatus("current")
_FsMstPortRowStatus_Type = RowStatus
_FsMstPortRowStatus_Object = MibTableColumn
fsMstPortRowStatus = _FsMstPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 48, 1, 2),
    _FsMstPortRowStatus_Type()
)
fsMstPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMstPortRowStatus.setStatus("current")


class _FsMstBpduGuard_Type(Integer32):
    """Custom type fsMstBpduGuard based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FsMstBpduGuard_Type.__name__ = "Integer32"
_FsMstBpduGuard_Object = MibScalar
fsMstBpduGuard = _FsMstBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 1, 49),
    _FsMstBpduGuard_Type()
)
fsMstBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstBpduGuard.setStatus("current")
_Dot1sFsMstTrapsControl_ObjectIdentity = ObjectIdentity
dot1sFsMstTrapsControl = _Dot1sFsMstTrapsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 2)
)


class _FsMstSetTraps_Type(Integer32):
    """Custom type fsMstSetTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMstSetTraps_Type.__name__ = "Integer32"
_FsMstSetTraps_Object = MibScalar
fsMstSetTraps = _FsMstSetTraps_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 2, 1),
    _FsMstSetTraps_Type()
)
fsMstSetTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMstSetTraps.setStatus("current")


class _FsMstGenTrapType_Type(Integer32):
    """Custom type fsMstGenTrapType based on Integer32"""
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
          ("up", 1),
          ("down", 2))
    )


_FsMstGenTrapType_Type.__name__ = "Integer32"
_FsMstGenTrapType_Object = MibScalar
fsMstGenTrapType = _FsMstGenTrapType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 2, 2),
    _FsMstGenTrapType_Type()
)
fsMstGenTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstGenTrapType.setStatus("current")


class _FsMstErrTrapType_Type(Integer32):
    """Custom type fsMstErrTrapType based on Integer32"""
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
          ("memfail", 1),
          ("bufffail", 2))
    )


_FsMstErrTrapType_Type.__name__ = "Integer32"
_FsMstErrTrapType_Object = MibScalar
fsMstErrTrapType = _FsMstErrTrapType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 2, 3),
    _FsMstErrTrapType_Type()
)
fsMstErrTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstErrTrapType.setStatus("current")
_FsMstPortTrapNotificationTable_Object = MibTable
fsMstPortTrapNotificationTable = _FsMstPortTrapNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 2, 4)
)
if mibBuilder.loadTexts:
    fsMstPortTrapNotificationTable.setStatus("current")
_FsMstPortTrapNotificationEntry_Object = MibTableRow
fsMstPortTrapNotificationEntry = _FsMstPortTrapNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 2, 4, 1)
)
fsMstPortTrapNotificationEntry.setIndexNames(
    (0, "SUPERMICRO-MST-MIB", "fsMstPortTrapIndex"),
)
if mibBuilder.loadTexts:
    fsMstPortTrapNotificationEntry.setStatus("current")


class _FsMstPortTrapIndex_Type(Integer32):
    """Custom type fsMstPortTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_FsMstPortTrapIndex_Type.__name__ = "Integer32"
_FsMstPortTrapIndex_Object = MibTableColumn
fsMstPortTrapIndex = _FsMstPortTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 2, 4, 1, 1),
    _FsMstPortTrapIndex_Type()
)
fsMstPortTrapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMstPortTrapIndex.setStatus("current")


class _FsMstPortMigrationType_Type(Integer32):
    """Custom type fsMstPortMigrationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sendstp", 0),
          ("sendrstp", 1))
    )


_FsMstPortMigrationType_Type.__name__ = "Integer32"
_FsMstPortMigrationType_Object = MibTableColumn
fsMstPortMigrationType = _FsMstPortMigrationType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 2, 4, 1, 2),
    _FsMstPortMigrationType_Type()
)
fsMstPortMigrationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstPortMigrationType.setStatus("current")


class _FsMstPktErrType_Type(Integer32):
    """Custom type fsMstPktErrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("protocolIdErr", 0),
          ("invalidBpdu", 1),
          ("configLengthErr", 2),
          ("tcnLengthErr", 3),
          ("rstpLengthErr", 4),
          ("maxAgeErr", 5),
          ("fwdDelayErr", 6),
          ("helloTimeErr", 7),
          ("mstpLengthErr", 8))
    )


_FsMstPktErrType_Type.__name__ = "Integer32"
_FsMstPktErrType_Object = MibTableColumn
fsMstPktErrType = _FsMstPktErrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 2, 4, 1, 3),
    _FsMstPktErrType_Type()
)
fsMstPktErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstPktErrType.setStatus("current")
_FsMstPktErrVal_Type = Integer32
_FsMstPktErrVal_Object = MibTableColumn
fsMstPktErrVal = _FsMstPktErrVal_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 2, 4, 1, 4),
    _FsMstPktErrVal_Type()
)
fsMstPktErrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstPktErrVal.setStatus("current")
_FsMstPortRoleTrapNotificationTable_Object = MibTable
fsMstPortRoleTrapNotificationTable = _FsMstPortRoleTrapNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 2, 5)
)
if mibBuilder.loadTexts:
    fsMstPortRoleTrapNotificationTable.setStatus("current")
_FsMstPortRoleTrapNotificationEntry_Object = MibTableRow
fsMstPortRoleTrapNotificationEntry = _FsMstPortRoleTrapNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 2, 5, 1)
)
fsMstPortRoleTrapNotificationEntry.setIndexNames(
    (0, "SUPERMICRO-MST-MIB", "fsMstPortTrapIndex"),
    (0, "SUPERMICRO-MST-MIB", "fsMstMstiInstanceIndex"),
)
if mibBuilder.loadTexts:
    fsMstPortRoleTrapNotificationEntry.setStatus("current")


class _FsMstPortRoleType_Type(Integer32):
    """Custom type fsMstPortRoleType based on Integer32"""
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
        *(("disabledPort", 0),
          ("alternatePort", 1),
          ("backupPort", 2),
          ("rootPort", 3),
          ("designatedPort", 4),
          ("masterport", 5))
    )


_FsMstPortRoleType_Type.__name__ = "Integer32"
_FsMstPortRoleType_Object = MibTableColumn
fsMstPortRoleType = _FsMstPortRoleType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 2, 5, 1, 1),
    _FsMstPortRoleType_Type()
)
fsMstPortRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstPortRoleType.setStatus("current")


class _FsMstOldRoleType_Type(Integer32):
    """Custom type fsMstOldRoleType based on Integer32"""
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
        *(("disabledPort", 0),
          ("alternatePort", 1),
          ("backupPort", 2),
          ("rootPort", 3),
          ("designatedPort", 4),
          ("masterport", 5))
    )


_FsMstOldRoleType_Type.__name__ = "Integer32"
_FsMstOldRoleType_Object = MibTableColumn
fsMstOldRoleType = _FsMstOldRoleType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 2, 5, 1, 2),
    _FsMstOldRoleType_Type()
)
fsMstOldRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMstOldRoleType.setStatus("current")
_Dot1sFutureMstTraps_ObjectIdentity = ObjectIdentity
dot1sFutureMstTraps = _Dot1sFutureMstTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 3)
)
_FsMstTraps_ObjectIdentity = ObjectIdentity
fsMstTraps = _FsMstTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 3, 0)
)

# Managed Objects groups


# Notification objects

fsMstGenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 3, 0, 1)
)
fsMstGenTrap.setObjects(
      *(("SUPERMICRO-MST-MIB", "fsMstBrgAddress"),
        ("SUPERMICRO-MST-MIB", "fsMstGenTrapType"),
        ("SUPERMICRO-MST-MIB", "fsMstInstanceUpCount"),
        ("SUPERMICRO-MST-MIB", "fsMstInstanceDownCount"))
)
if mibBuilder.loadTexts:
    fsMstGenTrap.setStatus(
        "current"
    )

fsMstErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 3, 0, 2)
)
fsMstErrTrap.setObjects(
      *(("SUPERMICRO-MST-MIB", "fsMstBrgAddress"),
        ("SUPERMICRO-MST-MIB", "fsMstErrTrapType"))
)
if mibBuilder.loadTexts:
    fsMstErrTrap.setStatus(
        "current"
    )

fsMstNewRootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 3, 0, 3)
)
fsMstNewRootTrap.setObjects(
      *(("SUPERMICRO-MST-MIB", "fsMstBrgAddress"),
        ("SUPERMICRO-MST-MIB", "fsMstOldDesignatedRoot"),
        ("SUPERMICRO-MST-MIB", "fsMstMstiBridgeRegionalRoot"))
)
if mibBuilder.loadTexts:
    fsMstNewRootTrap.setStatus(
        "current"
    )

fsMstTopologyChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 3, 0, 4)
)
fsMstTopologyChgTrap.setObjects(
      *(("SUPERMICRO-MST-MIB", "fsMstBrgAddress"),
        ("SUPERMICRO-MST-MIB", "fsMstMstiTopChanges"))
)
if mibBuilder.loadTexts:
    fsMstTopologyChgTrap.setStatus(
        "current"
    )

fsMstProtocolMigrationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 3, 0, 5)
)
fsMstProtocolMigrationTrap.setObjects(
      *(("SUPERMICRO-MST-MIB", "fsMstBrgAddress"),
        ("SUPERMICRO-MST-MIB", "fsMstForceProtocolVersion"),
        ("SUPERMICRO-MST-MIB", "fsMstPortMigrationType"))
)
if mibBuilder.loadTexts:
    fsMstProtocolMigrationTrap.setStatus(
        "current"
    )

fsMstInvalidBpduRxdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 3, 0, 6)
)
fsMstInvalidBpduRxdTrap.setObjects(
      *(("SUPERMICRO-MST-MIB", "fsMstBrgAddress"),
        ("SUPERMICRO-MST-MIB", "fsMstPktErrType"),
        ("SUPERMICRO-MST-MIB", "fsMstPktErrVal"))
)
if mibBuilder.loadTexts:
    fsMstInvalidBpduRxdTrap.setStatus(
        "current"
    )

fsMstRegionConfigChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 3, 0, 7)
)
fsMstRegionConfigChangeTrap.setObjects(
      *(("SUPERMICRO-MST-MIB", "fsMstBrgAddress"),
        ("SUPERMICRO-MST-MIB", "fsMstMstiConfigIdSel"),
        ("SUPERMICRO-MST-MIB", "fsMstMstiRegionName"),
        ("SUPERMICRO-MST-MIB", "fsMstMstiRegionVersion"),
        ("SUPERMICRO-MST-MIB", "fsMstMstiConfigDigest"))
)
if mibBuilder.loadTexts:
    fsMstRegionConfigChangeTrap.setStatus(
        "current"
    )

fsMstNewPortRoleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 3, 0, 8)
)
fsMstNewPortRoleTrap.setObjects(
      *(("SUPERMICRO-MST-MIB", "fsMstBrgAddress"),
        ("SUPERMICRO-MST-MIB", "fsMstPortRoleType"),
        ("SUPERMICRO-MST-MIB", "fsMstOldRoleType"))
)
if mibBuilder.loadTexts:
    fsMstNewPortRoleTrap.setStatus(
        "current"
    )

fsMstCistHwFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 3, 0, 9)
)
fsMstCistHwFailureTrap.setObjects(
      *(("SUPERMICRO-MST-MIB", "fsMstBrgAddress"),
        ("SUPERMICRO-MST-MIB", "fsMstCistPortState"))
)
if mibBuilder.loadTexts:
    fsMstCistHwFailureTrap.setStatus(
        "current"
    )

fsMstMstiHwFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 80, 3, 0, 10)
)
fsMstMstiHwFailureTrap.setObjects(
      *(("SUPERMICRO-MST-MIB", "fsMstBrgAddress"),
        ("SUPERMICRO-MST-MIB", "fsMstMstiPortState"))
)
if mibBuilder.loadTexts:
    fsMstMstiHwFailureTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-MST-MIB",
    **{"VlanId": VlanId,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "EnabledStatus": EnabledStatus,
       "futureMstMIB": futureMstMIB,
       "dot1sFutureMst": dot1sFutureMst,
       "fsMstSystemControl": fsMstSystemControl,
       "fsMstModuleStatus": fsMstModuleStatus,
       "fsMstMaxMstInstanceNumber": fsMstMaxMstInstanceNumber,
       "fsMstNoOfMstiSupported": fsMstNoOfMstiSupported,
       "fsMstMaxHopCount": fsMstMaxHopCount,
       "fsMstBrgAddress": fsMstBrgAddress,
       "fsMstCistRoot": fsMstCistRoot,
       "fsMstCistRegionalRoot": fsMstCistRegionalRoot,
       "fsMstCistRootCost": fsMstCistRootCost,
       "fsMstCistRegionalRootCost": fsMstCistRegionalRootCost,
       "fsMstCistRootPort": fsMstCistRootPort,
       "fsMstCistBridgePriority": fsMstCistBridgePriority,
       "fsMstCistBridgeMaxAge": fsMstCistBridgeMaxAge,
       "fsMstCistBridgeForwardDelay": fsMstCistBridgeForwardDelay,
       "fsMstCistHoldTime": fsMstCistHoldTime,
       "fsMstCistMaxAge": fsMstCistMaxAge,
       "fsMstCistForwardDelay": fsMstCistForwardDelay,
       "fsMstMstpUpCount": fsMstMstpUpCount,
       "fsMstMstpDownCount": fsMstMstpDownCount,
       "fsMstPathCostDefaultType": fsMstPathCostDefaultType,
       "fsMstTrace": fsMstTrace,
       "fsMstDebug": fsMstDebug,
       "fsMstForceProtocolVersion": fsMstForceProtocolVersion,
       "fsMstTxHoldCount": fsMstTxHoldCount,
       "fsMstMstiConfigIdSel": fsMstMstiConfigIdSel,
       "fsMstMstiRegionName": fsMstMstiRegionName,
       "fsMstMstiRegionVersion": fsMstMstiRegionVersion,
       "fsMstMstiConfigDigest": fsMstMstiConfigDigest,
       "fsMstBufferOverFlowCount": fsMstBufferOverFlowCount,
       "fsMstMemAllocFailureCount": fsMstMemAllocFailureCount,
       "fsMstRegionConfigChangeCount": fsMstRegionConfigChangeCount,
       "fsMstCistBridgeRoleSelectionSemState": fsMstCistBridgeRoleSelectionSemState,
       "fsMstCistTimeSinceTopologyChange": fsMstCistTimeSinceTopologyChange,
       "fsMstCistTopChanges": fsMstCistTopChanges,
       "fsMstCistNewRootBridgeCount": fsMstCistNewRootBridgeCount,
       "fsMstCistHelloTime": fsMstCistHelloTime,
       "fsMstCistBridgeHelloTime": fsMstCistBridgeHelloTime,
       "fsMstMstiBridgeTable": fsMstMstiBridgeTable,
       "fsMstMstiBridgeEntry": fsMstMstiBridgeEntry,
       "fsMstMstiInstanceIndex": fsMstMstiInstanceIndex,
       "fsMstMstiBridgeRegionalRoot": fsMstMstiBridgeRegionalRoot,
       "fsMstMstiBridgePriority": fsMstMstiBridgePriority,
       "fsMstMstiRootCost": fsMstMstiRootCost,
       "fsMstMstiRootPort": fsMstMstiRootPort,
       "fsMstMstiTimeSinceTopologyChange": fsMstMstiTimeSinceTopologyChange,
       "fsMstMstiTopChanges": fsMstMstiTopChanges,
       "fsMstMstiNewRootBridgeCount": fsMstMstiNewRootBridgeCount,
       "fsMstMstiBridgeRoleSelectionSemState": fsMstMstiBridgeRoleSelectionSemState,
       "fsMstInstanceUpCount": fsMstInstanceUpCount,
       "fsMstInstanceDownCount": fsMstInstanceDownCount,
       "fsMstOldDesignatedRoot": fsMstOldDesignatedRoot,
       "fsMstVlanInstanceMappingTable": fsMstVlanInstanceMappingTable,
       "fsMstVlanInstanceMappingEntry": fsMstVlanInstanceMappingEntry,
       "fsMstInstanceIndex": fsMstInstanceIndex,
       "fsMstMapVlanIndex": fsMstMapVlanIndex,
       "fsMstUnMapVlanIndex": fsMstUnMapVlanIndex,
       "fsMstSetVlanList": fsMstSetVlanList,
       "fsMstResetVlanList": fsMstResetVlanList,
       "fsMstInstanceVlanMapped": fsMstInstanceVlanMapped,
       "fsMstInstanceVlanMapped2k": fsMstInstanceVlanMapped2k,
       "fsMstInstanceVlanMapped3k": fsMstInstanceVlanMapped3k,
       "fsMstInstanceVlanMapped4k": fsMstInstanceVlanMapped4k,
       "fsMstCistPortTable": fsMstCistPortTable,
       "fsMstCistPortEntry": fsMstCistPortEntry,
       "fsMstCistPort": fsMstCistPort,
       "fsMstCistPortPathCost": fsMstCistPortPathCost,
       "fsMstCistPortPriority": fsMstCistPortPriority,
       "fsMstCistPortDesignatedRoot": fsMstCistPortDesignatedRoot,
       "fsMstCistPortDesignatedBridge": fsMstCistPortDesignatedBridge,
       "fsMstCistPortDesignatedPort": fsMstCistPortDesignatedPort,
       "fsMstCistPortAdminP2P": fsMstCistPortAdminP2P,
       "fsMstCistPortOperP2P": fsMstCistPortOperP2P,
       "fsMstCistPortAdminEdgeStatus": fsMstCistPortAdminEdgeStatus,
       "fsMstCistPortOperEdgeStatus": fsMstCistPortOperEdgeStatus,
       "fsMstCistPortProtocolMigration": fsMstCistPortProtocolMigration,
       "fsMstCistPortState": fsMstCistPortState,
       "fsMstCistForcePortState": fsMstCistForcePortState,
       "fsMstCistPortForwardTransitions": fsMstCistPortForwardTransitions,
       "fsMstCistPortRxMstBpduCount": fsMstCistPortRxMstBpduCount,
       "fsMstCistPortRxRstBpduCount": fsMstCistPortRxRstBpduCount,
       "fsMstCistPortRxConfigBpduCount": fsMstCistPortRxConfigBpduCount,
       "fsMstCistPortRxTcnBpduCount": fsMstCistPortRxTcnBpduCount,
       "fsMstCistPortTxMstBpduCount": fsMstCistPortTxMstBpduCount,
       "fsMstCistPortTxRstBpduCount": fsMstCistPortTxRstBpduCount,
       "fsMstCistPortTxConfigBpduCount": fsMstCistPortTxConfigBpduCount,
       "fsMstCistPortTxTcnBpduCount": fsMstCistPortTxTcnBpduCount,
       "fsMstCistPortInvalidMstBpduRxCount": fsMstCistPortInvalidMstBpduRxCount,
       "fsMstCistPortInvalidRstBpduRxCount": fsMstCistPortInvalidRstBpduRxCount,
       "fsMstCistPortInvalidConfigBpduRxCount": fsMstCistPortInvalidConfigBpduRxCount,
       "fsMstCistPortInvalidTcnBpduRxCount": fsMstCistPortInvalidTcnBpduRxCount,
       "fsMstCistPortTransmitSemState": fsMstCistPortTransmitSemState,
       "fsMstCistPortReceiveSemState": fsMstCistPortReceiveSemState,
       "fsMstCistPortProtMigrationSemState": fsMstCistPortProtMigrationSemState,
       "fsMstCistProtocolMigrationCount": fsMstCistProtocolMigrationCount,
       "fsMstCistPortDesignatedCost": fsMstCistPortDesignatedCost,
       "fsMstCistPortRegionalRoot": fsMstCistPortRegionalRoot,
       "fsMstCistPortRegionalPathCost": fsMstCistPortRegionalPathCost,
       "fsMstCistSelectedPortRole": fsMstCistSelectedPortRole,
       "fsMstCistCurrentPortRole": fsMstCistCurrentPortRole,
       "fsMstCistPortInfoSemState": fsMstCistPortInfoSemState,
       "fsMstCistPortRoleTransitionSemState": fsMstCistPortRoleTransitionSemState,
       "fsMstCistPortStateTransitionSemState": fsMstCistPortStateTransitionSemState,
       "fsMstCistPortTopologyChangeSemState": fsMstCistPortTopologyChangeSemState,
       "fsMstCistPortHelloTime": fsMstCistPortHelloTime,
       "fsMstCistPortOperVersion": fsMstCistPortOperVersion,
       "fsMstCistPortEffectivePortState": fsMstCistPortEffectivePortState,
       "fsMstCistPortAutoEdgeStatus": fsMstCistPortAutoEdgeStatus,
       "fsMstCistPortRestrictedRole": fsMstCistPortRestrictedRole,
       "fsMstCistPortRestrictedTCN": fsMstCistPortRestrictedTCN,
       "fsMstCistPortAdminPathCost": fsMstCistPortAdminPathCost,
       "fsMstCistPortEnableBPDURx": fsMstCistPortEnableBPDURx,
       "fsMstCistPortEnableBPDUTx": fsMstCistPortEnableBPDUTx,
       "fsMstCistPortPseudoRootId": fsMstCistPortPseudoRootId,
       "fsMstCistPortIsL2Gp": fsMstCistPortIsL2Gp,
       "fsMstCistPortLoopGuard": fsMstCistPortLoopGuard,
       "fsMstCistPortRcvdEvent": fsMstCistPortRcvdEvent,
       "fsMstCistPortRcvdEventSubType": fsMstCistPortRcvdEventSubType,
       "fsMstCistPortRcvdEventTimeStamp": fsMstCistPortRcvdEventTimeStamp,
       "fsMstCistPortBpduGuard": fsMstCistPortBpduGuard,
       "fsMstMstiPortTable": fsMstMstiPortTable,
       "fsMstMstiPortEntry": fsMstMstiPortEntry,
       "fsMstMstiPort": fsMstMstiPort,
       "fsMstMstiPortPathCost": fsMstMstiPortPathCost,
       "fsMstMstiPortPriority": fsMstMstiPortPriority,
       "fsMstMstiPortDesignatedRoot": fsMstMstiPortDesignatedRoot,
       "fsMstMstiPortDesignatedBridge": fsMstMstiPortDesignatedBridge,
       "fsMstMstiPortDesignatedPort": fsMstMstiPortDesignatedPort,
       "fsMstMstiPortState": fsMstMstiPortState,
       "fsMstMstiForcePortState": fsMstMstiForcePortState,
       "fsMstMstiPortForwardTransitions": fsMstMstiPortForwardTransitions,
       "fsMstMstiPortReceivedBPDUs": fsMstMstiPortReceivedBPDUs,
       "fsMstMstiPortTransmittedBPDUs": fsMstMstiPortTransmittedBPDUs,
       "fsMstMstiPortInvalidBPDUsRcvd": fsMstMstiPortInvalidBPDUsRcvd,
       "fsMstMstiPortDesignatedCost": fsMstMstiPortDesignatedCost,
       "fsMstMstiSelectedPortRole": fsMstMstiSelectedPortRole,
       "fsMstMstiCurrentPortRole": fsMstMstiCurrentPortRole,
       "fsMstMstiPortInfoSemState": fsMstMstiPortInfoSemState,
       "fsMstMstiPortRoleTransitionSemState": fsMstMstiPortRoleTransitionSemState,
       "fsMstMstiPortStateTransitionSemState": fsMstMstiPortStateTransitionSemState,
       "fsMstMstiPortTopologyChangeSemState": fsMstMstiPortTopologyChangeSemState,
       "fsMstMstiPortEffectivePortState": fsMstMstiPortEffectivePortState,
       "fsMstMstiPortAdminPathCost": fsMstMstiPortAdminPathCost,
       "fsMstMstiPortPseudoRootId": fsMstMstiPortPseudoRootId,
       "fsMstMstiPortStateChangeTimeStamp": fsMstMstiPortStateChangeTimeStamp,
       "fsMstCistDynamicPathcostCalculation": fsMstCistDynamicPathcostCalculation,
       "fsMstCalcPortPathCostOnSpeedChg": fsMstCalcPortPathCostOnSpeedChg,
       "fsMstRcvdEvent": fsMstRcvdEvent,
       "fsMstRcvdEventSubType": fsMstRcvdEventSubType,
       "fsMstRcvdEventTimeStamp": fsMstRcvdEventTimeStamp,
       "fsMstPortStateChangeTimeStamp": fsMstPortStateChangeTimeStamp,
       "fsMstPortExtTable": fsMstPortExtTable,
       "fsMstPortExtEntry": fsMstPortExtEntry,
       "fsMstPort": fsMstPort,
       "fsMstPortRowStatus": fsMstPortRowStatus,
       "fsMstBpduGuard": fsMstBpduGuard,
       "dot1sFsMstTrapsControl": dot1sFsMstTrapsControl,
       "fsMstSetTraps": fsMstSetTraps,
       "fsMstGenTrapType": fsMstGenTrapType,
       "fsMstErrTrapType": fsMstErrTrapType,
       "fsMstPortTrapNotificationTable": fsMstPortTrapNotificationTable,
       "fsMstPortTrapNotificationEntry": fsMstPortTrapNotificationEntry,
       "fsMstPortTrapIndex": fsMstPortTrapIndex,
       "fsMstPortMigrationType": fsMstPortMigrationType,
       "fsMstPktErrType": fsMstPktErrType,
       "fsMstPktErrVal": fsMstPktErrVal,
       "fsMstPortRoleTrapNotificationTable": fsMstPortRoleTrapNotificationTable,
       "fsMstPortRoleTrapNotificationEntry": fsMstPortRoleTrapNotificationEntry,
       "fsMstPortRoleType": fsMstPortRoleType,
       "fsMstOldRoleType": fsMstOldRoleType,
       "dot1sFutureMstTraps": dot1sFutureMstTraps,
       "fsMstTraps": fsMstTraps,
       "fsMstGenTrap": fsMstGenTrap,
       "fsMstErrTrap": fsMstErrTrap,
       "fsMstNewRootTrap": fsMstNewRootTrap,
       "fsMstTopologyChgTrap": fsMstTopologyChgTrap,
       "fsMstProtocolMigrationTrap": fsMstProtocolMigrationTrap,
       "fsMstInvalidBpduRxdTrap": fsMstInvalidBpduRxdTrap,
       "fsMstRegionConfigChangeTrap": fsMstRegionConfigChangeTrap,
       "fsMstNewPortRoleTrap": fsMstNewPortRoleTrap,
       "fsMstCistHwFailureTrap": fsMstCistHwFailureTrap,
       "fsMstMstiHwFailureTrap": fsMstMstiHwFailureTrap}
)
