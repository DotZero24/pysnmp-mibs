# SNMP MIB module (SupermicroMIMst-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SupermicroMIMst-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:02:01 2025
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

futureMIMstMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118)
)
if mibBuilder.loadTexts:
    futureMIMstMIB.setRevisions(
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

_FsMIDot1sFutureMst_ObjectIdentity = ObjectIdentity
fsMIDot1sFutureMst = _FsMIDot1sFutureMst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1)
)
_FsMIMstGlobalTrace_Type = TruthValue
_FsMIMstGlobalTrace_Object = MibScalar
fsMIMstGlobalTrace = _FsMIMstGlobalTrace_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 1),
    _FsMIMstGlobalTrace_Type()
)
fsMIMstGlobalTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstGlobalTrace.setStatus("current")
_FsMIMstGlobalDebug_Type = TruthValue
_FsMIMstGlobalDebug_Object = MibScalar
fsMIMstGlobalDebug = _FsMIMstGlobalDebug_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 2),
    _FsMIMstGlobalDebug_Type()
)
fsMIMstGlobalDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstGlobalDebug.setStatus("current")
_FsMIDot1sFutureMstTable_Object = MibTable
fsMIDot1sFutureMstTable = _FsMIDot1sFutureMstTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3)
)
if mibBuilder.loadTexts:
    fsMIDot1sFutureMstTable.setStatus("current")
_FsMIDot1sFutureMstEntry_Object = MibTableRow
fsMIDot1sFutureMstEntry = _FsMIDot1sFutureMstEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1)
)
fsMIDot1sFutureMstEntry.setIndexNames(
    (0, "SupermicroMIMst-MIB", "fsMIDot1sFutureMstContextId"),
)
if mibBuilder.loadTexts:
    fsMIDot1sFutureMstEntry.setStatus("current")


class _FsMIDot1sFutureMstContextId_Type(Integer32):
    """Custom type fsMIDot1sFutureMstContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIDot1sFutureMstContextId_Type.__name__ = "Integer32"
_FsMIDot1sFutureMstContextId_Object = MibTableColumn
fsMIDot1sFutureMstContextId = _FsMIDot1sFutureMstContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 1),
    _FsMIDot1sFutureMstContextId_Type()
)
fsMIDot1sFutureMstContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIDot1sFutureMstContextId.setStatus("current")


class _FsMIMstSystemControl_Type(Integer32):
    """Custom type fsMIMstSystemControl based on Integer32"""
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


_FsMIMstSystemControl_Type.__name__ = "Integer32"
_FsMIMstSystemControl_Object = MibTableColumn
fsMIMstSystemControl = _FsMIMstSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 2),
    _FsMIMstSystemControl_Type()
)
fsMIMstSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstSystemControl.setStatus("current")
_FsMIMstModuleStatus_Type = EnabledStatus
_FsMIMstModuleStatus_Object = MibTableColumn
fsMIMstModuleStatus = _FsMIMstModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 3),
    _FsMIMstModuleStatus_Type()
)
fsMIMstModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstModuleStatus.setStatus("current")


class _FsMIMstMaxMstInstanceNumber_Type(Integer32):
    """Custom type fsMIMstMaxMstInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_FsMIMstMaxMstInstanceNumber_Type.__name__ = "Integer32"
_FsMIMstMaxMstInstanceNumber_Object = MibTableColumn
fsMIMstMaxMstInstanceNumber = _FsMIMstMaxMstInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 4),
    _FsMIMstMaxMstInstanceNumber_Type()
)
fsMIMstMaxMstInstanceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstMaxMstInstanceNumber.setStatus("current")
_FsMIMstNoOfMstiSupported_Type = Integer32
_FsMIMstNoOfMstiSupported_Object = MibTableColumn
fsMIMstNoOfMstiSupported = _FsMIMstNoOfMstiSupported_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 5),
    _FsMIMstNoOfMstiSupported_Type()
)
fsMIMstNoOfMstiSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstNoOfMstiSupported.setStatus("current")


class _FsMIMstMaxHopCount_Type(Integer32):
    """Custom type fsMIMstMaxHopCount based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_FsMIMstMaxHopCount_Type.__name__ = "Integer32"
_FsMIMstMaxHopCount_Object = MibTableColumn
fsMIMstMaxHopCount = _FsMIMstMaxHopCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 6),
    _FsMIMstMaxHopCount_Type()
)
fsMIMstMaxHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstMaxHopCount.setStatus("current")
_FsMIMstBrgAddress_Type = MacAddress
_FsMIMstBrgAddress_Object = MibTableColumn
fsMIMstBrgAddress = _FsMIMstBrgAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 7),
    _FsMIMstBrgAddress_Type()
)
fsMIMstBrgAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstBrgAddress.setStatus("current")
_FsMIMstCistRoot_Type = BridgeId
_FsMIMstCistRoot_Object = MibTableColumn
fsMIMstCistRoot = _FsMIMstCistRoot_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 8),
    _FsMIMstCistRoot_Type()
)
fsMIMstCistRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistRoot.setStatus("current")
_FsMIMstCistRegionalRoot_Type = BridgeId
_FsMIMstCistRegionalRoot_Object = MibTableColumn
fsMIMstCistRegionalRoot = _FsMIMstCistRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 9),
    _FsMIMstCistRegionalRoot_Type()
)
fsMIMstCistRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistRegionalRoot.setStatus("current")
_FsMIMstCistRootCost_Type = Integer32
_FsMIMstCistRootCost_Object = MibTableColumn
fsMIMstCistRootCost = _FsMIMstCistRootCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 10),
    _FsMIMstCistRootCost_Type()
)
fsMIMstCistRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistRootCost.setStatus("current")
_FsMIMstCistRegionalRootCost_Type = Integer32
_FsMIMstCistRegionalRootCost_Object = MibTableColumn
fsMIMstCistRegionalRootCost = _FsMIMstCistRegionalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 11),
    _FsMIMstCistRegionalRootCost_Type()
)
fsMIMstCistRegionalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistRegionalRootCost.setStatus("current")
_FsMIMstCistRootPort_Type = Integer32
_FsMIMstCistRootPort_Object = MibTableColumn
fsMIMstCistRootPort = _FsMIMstCistRootPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 12),
    _FsMIMstCistRootPort_Type()
)
fsMIMstCistRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistRootPort.setStatus("current")


class _FsMIMstCistBridgePriority_Type(Integer32):
    """Custom type fsMIMstCistBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_FsMIMstCistBridgePriority_Type.__name__ = "Integer32"
_FsMIMstCistBridgePriority_Object = MibTableColumn
fsMIMstCistBridgePriority = _FsMIMstCistBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 13),
    _FsMIMstCistBridgePriority_Type()
)
fsMIMstCistBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCistBridgePriority.setStatus("current")


class _FsMIMstCistBridgeMaxAge_Type(Timeout):
    """Custom type fsMIMstCistBridgeMaxAge based on Timeout"""
    defaultValue = 2000

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_FsMIMstCistBridgeMaxAge_Type.__name__ = "Timeout"
_FsMIMstCistBridgeMaxAge_Object = MibTableColumn
fsMIMstCistBridgeMaxAge = _FsMIMstCistBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 14),
    _FsMIMstCistBridgeMaxAge_Type()
)
fsMIMstCistBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCistBridgeMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    fsMIMstCistBridgeMaxAge.setUnits("centi-seconds")


class _FsMIMstCistBridgeForwardDelay_Type(Timeout):
    """Custom type fsMIMstCistBridgeForwardDelay based on Timeout"""
    defaultValue = 1500

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_FsMIMstCistBridgeForwardDelay_Type.__name__ = "Timeout"
_FsMIMstCistBridgeForwardDelay_Object = MibTableColumn
fsMIMstCistBridgeForwardDelay = _FsMIMstCistBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 15),
    _FsMIMstCistBridgeForwardDelay_Type()
)
fsMIMstCistBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCistBridgeForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    fsMIMstCistBridgeForwardDelay.setUnits("centi-seconds")
_FsMIMstCistHoldTime_Type = Integer32
_FsMIMstCistHoldTime_Object = MibTableColumn
fsMIMstCistHoldTime = _FsMIMstCistHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 16),
    _FsMIMstCistHoldTime_Type()
)
fsMIMstCistHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    fsMIMstCistHoldTime.setUnits("centi-seconds")
_FsMIMstCistMaxAge_Type = Timeout
_FsMIMstCistMaxAge_Object = MibTableColumn
fsMIMstCistMaxAge = _FsMIMstCistMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 17),
    _FsMIMstCistMaxAge_Type()
)
fsMIMstCistMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    fsMIMstCistMaxAge.setUnits("centi-seconds")
_FsMIMstCistForwardDelay_Type = Timeout
_FsMIMstCistForwardDelay_Object = MibTableColumn
fsMIMstCistForwardDelay = _FsMIMstCistForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 18),
    _FsMIMstCistForwardDelay_Type()
)
fsMIMstCistForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    fsMIMstCistForwardDelay.setUnits("centi-seconds")
_FsMIMstMstpUpCount_Type = Counter32
_FsMIMstMstpUpCount_Object = MibTableColumn
fsMIMstMstpUpCount = _FsMIMstMstpUpCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 19),
    _FsMIMstMstpUpCount_Type()
)
fsMIMstMstpUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstpUpCount.setStatus("current")
_FsMIMstMstpDownCount_Type = Counter32
_FsMIMstMstpDownCount_Object = MibTableColumn
fsMIMstMstpDownCount = _FsMIMstMstpDownCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 20),
    _FsMIMstMstpDownCount_Type()
)
fsMIMstMstpDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstpDownCount.setStatus("current")


class _FsMIMstPathCostDefaultType_Type(Integer32):
    """Custom type fsMIMstPathCostDefaultType based on Integer32"""
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


_FsMIMstPathCostDefaultType_Type.__name__ = "Integer32"
_FsMIMstPathCostDefaultType_Object = MibTableColumn
fsMIMstPathCostDefaultType = _FsMIMstPathCostDefaultType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 21),
    _FsMIMstPathCostDefaultType_Type()
)
fsMIMstPathCostDefaultType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstPathCostDefaultType.setStatus("obsolete")


class _FsMIMstTrace_Type(Integer32):
    """Custom type fsMIMstTrace based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIMstTrace_Type.__name__ = "Integer32"
_FsMIMstTrace_Object = MibTableColumn
fsMIMstTrace = _FsMIMstTrace_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 22),
    _FsMIMstTrace_Type()
)
fsMIMstTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstTrace.setStatus("current")


class _FsMIMstDebug_Type(Integer32):
    """Custom type fsMIMstDebug based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 524287),
    )


_FsMIMstDebug_Type.__name__ = "Integer32"
_FsMIMstDebug_Object = MibTableColumn
fsMIMstDebug = _FsMIMstDebug_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 23),
    _FsMIMstDebug_Type()
)
fsMIMstDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstDebug.setStatus("current")


class _FsMIMstForceProtocolVersion_Type(Integer32):
    """Custom type fsMIMstForceProtocolVersion based on Integer32"""
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


_FsMIMstForceProtocolVersion_Type.__name__ = "Integer32"
_FsMIMstForceProtocolVersion_Object = MibTableColumn
fsMIMstForceProtocolVersion = _FsMIMstForceProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 24),
    _FsMIMstForceProtocolVersion_Type()
)
fsMIMstForceProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstForceProtocolVersion.setStatus("current")


class _FsMIMstTxHoldCount_Type(Integer32):
    """Custom type fsMIMstTxHoldCount based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsMIMstTxHoldCount_Type.__name__ = "Integer32"
_FsMIMstTxHoldCount_Object = MibTableColumn
fsMIMstTxHoldCount = _FsMIMstTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 25),
    _FsMIMstTxHoldCount_Type()
)
fsMIMstTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstTxHoldCount.setStatus("current")


class _FsMIMstMstiConfigIdSel_Type(Integer32):
    """Custom type fsMIMstMstiConfigIdSel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIMstMstiConfigIdSel_Type.__name__ = "Integer32"
_FsMIMstMstiConfigIdSel_Object = MibTableColumn
fsMIMstMstiConfigIdSel = _FsMIMstMstiConfigIdSel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 26),
    _FsMIMstMstiConfigIdSel_Type()
)
fsMIMstMstiConfigIdSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstMstiConfigIdSel.setStatus("current")


class _FsMIMstMstiRegionName_Type(OctetString):
    """Custom type fsMIMstMstiRegionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsMIMstMstiRegionName_Type.__name__ = "OctetString"
_FsMIMstMstiRegionName_Object = MibTableColumn
fsMIMstMstiRegionName = _FsMIMstMstiRegionName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 27),
    _FsMIMstMstiRegionName_Type()
)
fsMIMstMstiRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstMstiRegionName.setStatus("current")


class _FsMIMstMstiRegionVersion_Type(Integer32):
    """Custom type fsMIMstMstiRegionVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIMstMstiRegionVersion_Type.__name__ = "Integer32"
_FsMIMstMstiRegionVersion_Object = MibTableColumn
fsMIMstMstiRegionVersion = _FsMIMstMstiRegionVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 28),
    _FsMIMstMstiRegionVersion_Type()
)
fsMIMstMstiRegionVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstMstiRegionVersion.setStatus("current")


class _FsMIMstMstiConfigDigest_Type(OctetString):
    """Custom type fsMIMstMstiConfigDigest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsMIMstMstiConfigDigest_Type.__name__ = "OctetString"
_FsMIMstMstiConfigDigest_Object = MibTableColumn
fsMIMstMstiConfigDigest = _FsMIMstMstiConfigDigest_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 29),
    _FsMIMstMstiConfigDigest_Type()
)
fsMIMstMstiConfigDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiConfigDigest.setStatus("current")
_FsMIMstBufferOverFlowCount_Type = Counter32
_FsMIMstBufferOverFlowCount_Object = MibTableColumn
fsMIMstBufferOverFlowCount = _FsMIMstBufferOverFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 30),
    _FsMIMstBufferOverFlowCount_Type()
)
fsMIMstBufferOverFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstBufferOverFlowCount.setStatus("current")
_FsMIMstMemAllocFailureCount_Type = Counter32
_FsMIMstMemAllocFailureCount_Object = MibTableColumn
fsMIMstMemAllocFailureCount = _FsMIMstMemAllocFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 31),
    _FsMIMstMemAllocFailureCount_Type()
)
fsMIMstMemAllocFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMemAllocFailureCount.setStatus("current")
_FsMIMstRegionConfigChangeCount_Type = Counter32
_FsMIMstRegionConfigChangeCount_Object = MibTableColumn
fsMIMstRegionConfigChangeCount = _FsMIMstRegionConfigChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 32),
    _FsMIMstRegionConfigChangeCount_Type()
)
fsMIMstRegionConfigChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstRegionConfigChangeCount.setStatus("current")


class _FsMIMstCistBridgeRoleSelectionSemState_Type(Integer32):
    """Custom type fsMIMstCistBridgeRoleSelectionSemState based on Integer32"""
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


_FsMIMstCistBridgeRoleSelectionSemState_Type.__name__ = "Integer32"
_FsMIMstCistBridgeRoleSelectionSemState_Object = MibTableColumn
fsMIMstCistBridgeRoleSelectionSemState = _FsMIMstCistBridgeRoleSelectionSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 33),
    _FsMIMstCistBridgeRoleSelectionSemState_Type()
)
fsMIMstCistBridgeRoleSelectionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistBridgeRoleSelectionSemState.setStatus("current")
_FsMIMstCistTimeSinceTopologyChange_Type = TimeTicks
_FsMIMstCistTimeSinceTopologyChange_Object = MibTableColumn
fsMIMstCistTimeSinceTopologyChange = _FsMIMstCistTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 34),
    _FsMIMstCistTimeSinceTopologyChange_Type()
)
fsMIMstCistTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistTimeSinceTopologyChange.setStatus("current")
if mibBuilder.loadTexts:
    fsMIMstCistTimeSinceTopologyChange.setUnits("centi-seconds")
_FsMIMstCistTopChanges_Type = Counter32
_FsMIMstCistTopChanges_Object = MibTableColumn
fsMIMstCistTopChanges = _FsMIMstCistTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 35),
    _FsMIMstCistTopChanges_Type()
)
fsMIMstCistTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistTopChanges.setStatus("current")
_FsMIMstCistNewRootBridgeCount_Type = Counter32
_FsMIMstCistNewRootBridgeCount_Object = MibTableColumn
fsMIMstCistNewRootBridgeCount = _FsMIMstCistNewRootBridgeCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 36),
    _FsMIMstCistNewRootBridgeCount_Type()
)
fsMIMstCistNewRootBridgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistNewRootBridgeCount.setStatus("current")
_FsMIMstCistHelloTime_Type = Timeout
_FsMIMstCistHelloTime_Object = MibTableColumn
fsMIMstCistHelloTime = _FsMIMstCistHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 37),
    _FsMIMstCistHelloTime_Type()
)
fsMIMstCistHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    fsMIMstCistHelloTime.setUnits("centi-seconds")


class _FsMIMstCistBridgeHelloTime_Type(Timeout):
    """Custom type fsMIMstCistBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(200, 200),
    )


_FsMIMstCistBridgeHelloTime_Type.__name__ = "Timeout"
_FsMIMstCistBridgeHelloTime_Object = MibTableColumn
fsMIMstCistBridgeHelloTime = _FsMIMstCistBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 38),
    _FsMIMstCistBridgeHelloTime_Type()
)
fsMIMstCistBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCistBridgeHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    fsMIMstCistBridgeHelloTime.setUnits("centi-seconds")


class _FsMIMstCistDynamicPathcostCalculation_Type(TruthValue):
    """Custom type fsMIMstCistDynamicPathcostCalculation based on TruthValue"""
    defaultValue = 2


_FsMIMstCistDynamicPathcostCalculation_Type.__name__ = "TruthValue"
_FsMIMstCistDynamicPathcostCalculation_Object = MibTableColumn
fsMIMstCistDynamicPathcostCalculation = _FsMIMstCistDynamicPathcostCalculation_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 39),
    _FsMIMstCistDynamicPathcostCalculation_Type()
)
fsMIMstCistDynamicPathcostCalculation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCistDynamicPathcostCalculation.setStatus("current")


class _FsMIMstContextName_Type(DisplayString):
    """Custom type fsMIMstContextName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsMIMstContextName_Type.__name__ = "DisplayString"
_FsMIMstContextName_Object = MibTableColumn
fsMIMstContextName = _FsMIMstContextName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 40),
    _FsMIMstContextName_Type()
)
fsMIMstContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstContextName.setStatus("current")


class _FsMIMstCalcPortPathCostOnSpeedChg_Type(TruthValue):
    """Custom type fsMIMstCalcPortPathCostOnSpeedChg based on TruthValue"""
    defaultValue = 2


_FsMIMstCalcPortPathCostOnSpeedChg_Type.__name__ = "TruthValue"
_FsMIMstCalcPortPathCostOnSpeedChg_Object = MibTableColumn
fsMIMstCalcPortPathCostOnSpeedChg = _FsMIMstCalcPortPathCostOnSpeedChg_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 41),
    _FsMIMstCalcPortPathCostOnSpeedChg_Type()
)
fsMIMstCalcPortPathCostOnSpeedChg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCalcPortPathCostOnSpeedChg.setStatus("current")
_FsMIMstClearBridgeStats_Type = TruthValue
_FsMIMstClearBridgeStats_Object = MibTableColumn
fsMIMstClearBridgeStats = _FsMIMstClearBridgeStats_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 42),
    _FsMIMstClearBridgeStats_Type()
)
fsMIMstClearBridgeStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstClearBridgeStats.setStatus("current")


class _FsMIMstRcvdEvent_Type(Integer32):
    """Custom type fsMIMstRcvdEvent based on Integer32"""
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


_FsMIMstRcvdEvent_Type.__name__ = "Integer32"
_FsMIMstRcvdEvent_Object = MibTableColumn
fsMIMstRcvdEvent = _FsMIMstRcvdEvent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 43),
    _FsMIMstRcvdEvent_Type()
)
fsMIMstRcvdEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstRcvdEvent.setStatus("current")
_FsMIMstRcvdEventSubType_Type = Integer32
_FsMIMstRcvdEventSubType_Object = MibTableColumn
fsMIMstRcvdEventSubType = _FsMIMstRcvdEventSubType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 44),
    _FsMIMstRcvdEventSubType_Type()
)
fsMIMstRcvdEventSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstRcvdEventSubType.setStatus("current")
_FsMIMstRcvdEventTimeStamp_Type = Unsigned32
_FsMIMstRcvdEventTimeStamp_Object = MibTableColumn
fsMIMstRcvdEventTimeStamp = _FsMIMstRcvdEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 45),
    _FsMIMstRcvdEventTimeStamp_Type()
)
fsMIMstRcvdEventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstRcvdEventTimeStamp.setStatus("current")
_FsMIMstPortStateChangeTimeStamp_Type = Unsigned32
_FsMIMstPortStateChangeTimeStamp_Object = MibTableColumn
fsMIMstPortStateChangeTimeStamp = _FsMIMstPortStateChangeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 46),
    _FsMIMstPortStateChangeTimeStamp_Type()
)
fsMIMstPortStateChangeTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstPortStateChangeTimeStamp.setStatus("current")


class _FsMIMstFlushInterval_Type(Timeout):
    """Custom type fsMIMstFlushInterval based on Timeout"""
    defaultValue = 0

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_FsMIMstFlushInterval_Type.__name__ = "Timeout"
_FsMIMstFlushInterval_Object = MibTableColumn
fsMIMstFlushInterval = _FsMIMstFlushInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 47),
    _FsMIMstFlushInterval_Type()
)
fsMIMstFlushInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstFlushInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsMIMstFlushInterval.setUnits("centi-seconds")


class _FsMIMstCistFlushIndicationThreshold_Type(Integer32):
    """Custom type fsMIMstCistFlushIndicationThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIMstCistFlushIndicationThreshold_Type.__name__ = "Integer32"
_FsMIMstCistFlushIndicationThreshold_Object = MibTableColumn
fsMIMstCistFlushIndicationThreshold = _FsMIMstCistFlushIndicationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 48),
    _FsMIMstCistFlushIndicationThreshold_Type()
)
fsMIMstCistFlushIndicationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCistFlushIndicationThreshold.setStatus("current")
_FsMIMstCistTotalFlushCount_Type = Counter32
_FsMIMstCistTotalFlushCount_Object = MibTableColumn
fsMIMstCistTotalFlushCount = _FsMIMstCistTotalFlushCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 49),
    _FsMIMstCistTotalFlushCount_Type()
)
fsMIMstCistTotalFlushCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistTotalFlushCount.setStatus("current")


class _FsMIMstBpduGuard_Type(Integer32):
    """Custom type fsMIMstBpduGuard based on Integer32"""
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


_FsMIMstBpduGuard_Type.__name__ = "Integer32"
_FsMIMstBpduGuard_Object = MibTableColumn
fsMIMstBpduGuard = _FsMIMstBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 3, 1, 50),
    _FsMIMstBpduGuard_Type()
)
fsMIMstBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstBpduGuard.setStatus("current")
_FsMIMstMstiBridgeTable_Object = MibTable
fsMIMstMstiBridgeTable = _FsMIMstMstiBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 4)
)
if mibBuilder.loadTexts:
    fsMIMstMstiBridgeTable.setStatus("current")
_FsMIMstMstiBridgeEntry_Object = MibTableRow
fsMIMstMstiBridgeEntry = _FsMIMstMstiBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 4, 1)
)
fsMIMstMstiBridgeEntry.setIndexNames(
    (0, "SupermicroMIMst-MIB", "fsMIDot1sFutureMstContextId"),
    (0, "SupermicroMIMst-MIB", "fsMIMstMstiInstanceIndex"),
)
if mibBuilder.loadTexts:
    fsMIMstMstiBridgeEntry.setStatus("current")


class _FsMIMstMstiInstanceIndex_Type(Integer32):
    """Custom type fsMIMstMstiInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
        ValueRangeConstraint(4094, 4094),
    )


_FsMIMstMstiInstanceIndex_Type.__name__ = "Integer32"
_FsMIMstMstiInstanceIndex_Object = MibTableColumn
fsMIMstMstiInstanceIndex = _FsMIMstMstiInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 4, 1, 1),
    _FsMIMstMstiInstanceIndex_Type()
)
fsMIMstMstiInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIMstMstiInstanceIndex.setStatus("current")
_FsMIMstMstiBridgeRegionalRoot_Type = BridgeId
_FsMIMstMstiBridgeRegionalRoot_Object = MibTableColumn
fsMIMstMstiBridgeRegionalRoot = _FsMIMstMstiBridgeRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 4, 1, 2),
    _FsMIMstMstiBridgeRegionalRoot_Type()
)
fsMIMstMstiBridgeRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiBridgeRegionalRoot.setStatus("current")


class _FsMIMstMstiBridgePriority_Type(Integer32):
    """Custom type fsMIMstMstiBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_FsMIMstMstiBridgePriority_Type.__name__ = "Integer32"
_FsMIMstMstiBridgePriority_Object = MibTableColumn
fsMIMstMstiBridgePriority = _FsMIMstMstiBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 4, 1, 3),
    _FsMIMstMstiBridgePriority_Type()
)
fsMIMstMstiBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstMstiBridgePriority.setStatus("current")
_FsMIMstMstiRootCost_Type = Integer32
_FsMIMstMstiRootCost_Object = MibTableColumn
fsMIMstMstiRootCost = _FsMIMstMstiRootCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 4, 1, 4),
    _FsMIMstMstiRootCost_Type()
)
fsMIMstMstiRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiRootCost.setStatus("current")
_FsMIMstMstiRootPort_Type = Integer32
_FsMIMstMstiRootPort_Object = MibTableColumn
fsMIMstMstiRootPort = _FsMIMstMstiRootPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 4, 1, 5),
    _FsMIMstMstiRootPort_Type()
)
fsMIMstMstiRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiRootPort.setStatus("current")
_FsMIMstMstiTimeSinceTopologyChange_Type = TimeTicks
_FsMIMstMstiTimeSinceTopologyChange_Object = MibTableColumn
fsMIMstMstiTimeSinceTopologyChange = _FsMIMstMstiTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 4, 1, 6),
    _FsMIMstMstiTimeSinceTopologyChange_Type()
)
fsMIMstMstiTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiTimeSinceTopologyChange.setStatus("current")
if mibBuilder.loadTexts:
    fsMIMstMstiTimeSinceTopologyChange.setUnits("centi-seconds")
_FsMIMstMstiTopChanges_Type = Counter32
_FsMIMstMstiTopChanges_Object = MibTableColumn
fsMIMstMstiTopChanges = _FsMIMstMstiTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 4, 1, 7),
    _FsMIMstMstiTopChanges_Type()
)
fsMIMstMstiTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiTopChanges.setStatus("current")
_FsMIMstMstiNewRootBridgeCount_Type = Counter32
_FsMIMstMstiNewRootBridgeCount_Object = MibTableColumn
fsMIMstMstiNewRootBridgeCount = _FsMIMstMstiNewRootBridgeCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 4, 1, 8),
    _FsMIMstMstiNewRootBridgeCount_Type()
)
fsMIMstMstiNewRootBridgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiNewRootBridgeCount.setStatus("current")


class _FsMIMstMstiBridgeRoleSelectionSemState_Type(Integer32):
    """Custom type fsMIMstMstiBridgeRoleSelectionSemState based on Integer32"""
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


_FsMIMstMstiBridgeRoleSelectionSemState_Type.__name__ = "Integer32"
_FsMIMstMstiBridgeRoleSelectionSemState_Object = MibTableColumn
fsMIMstMstiBridgeRoleSelectionSemState = _FsMIMstMstiBridgeRoleSelectionSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 4, 1, 9),
    _FsMIMstMstiBridgeRoleSelectionSemState_Type()
)
fsMIMstMstiBridgeRoleSelectionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiBridgeRoleSelectionSemState.setStatus("current")
_FsMIMstInstanceUpCount_Type = Counter32
_FsMIMstInstanceUpCount_Object = MibTableColumn
fsMIMstInstanceUpCount = _FsMIMstInstanceUpCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 4, 1, 10),
    _FsMIMstInstanceUpCount_Type()
)
fsMIMstInstanceUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstInstanceUpCount.setStatus("current")
_FsMIMstInstanceDownCount_Type = Counter32
_FsMIMstInstanceDownCount_Object = MibTableColumn
fsMIMstInstanceDownCount = _FsMIMstInstanceDownCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 4, 1, 11),
    _FsMIMstInstanceDownCount_Type()
)
fsMIMstInstanceDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstInstanceDownCount.setStatus("current")
_FsMIMstOldDesignatedRoot_Type = BridgeId
_FsMIMstOldDesignatedRoot_Object = MibTableColumn
fsMIMstOldDesignatedRoot = _FsMIMstOldDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 4, 1, 12),
    _FsMIMstOldDesignatedRoot_Type()
)
fsMIMstOldDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstOldDesignatedRoot.setStatus("current")
_FsMIMstMstiClearBridgeStats_Type = TruthValue
_FsMIMstMstiClearBridgeStats_Object = MibTableColumn
fsMIMstMstiClearBridgeStats = _FsMIMstMstiClearBridgeStats_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 4, 1, 13),
    _FsMIMstMstiClearBridgeStats_Type()
)
fsMIMstMstiClearBridgeStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstMstiClearBridgeStats.setStatus("current")


class _FsMIMstMstiFlushIndicationThreshold_Type(Integer32):
    """Custom type fsMIMstMstiFlushIndicationThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIMstMstiFlushIndicationThreshold_Type.__name__ = "Integer32"
_FsMIMstMstiFlushIndicationThreshold_Object = MibTableColumn
fsMIMstMstiFlushIndicationThreshold = _FsMIMstMstiFlushIndicationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 4, 1, 14),
    _FsMIMstMstiFlushIndicationThreshold_Type()
)
fsMIMstMstiFlushIndicationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstMstiFlushIndicationThreshold.setStatus("current")
_FsMIMstMstiTotalFlushCount_Type = Counter32
_FsMIMstMstiTotalFlushCount_Object = MibTableColumn
fsMIMstMstiTotalFlushCount = _FsMIMstMstiTotalFlushCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 4, 1, 15),
    _FsMIMstMstiTotalFlushCount_Type()
)
fsMIMstMstiTotalFlushCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiTotalFlushCount.setStatus("current")
_FsMIMstVlanInstanceMappingTable_Object = MibTable
fsMIMstVlanInstanceMappingTable = _FsMIMstVlanInstanceMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 5)
)
if mibBuilder.loadTexts:
    fsMIMstVlanInstanceMappingTable.setStatus("current")
_FsMIMstVlanInstanceMappingEntry_Object = MibTableRow
fsMIMstVlanInstanceMappingEntry = _FsMIMstVlanInstanceMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 5, 1)
)
fsMIMstVlanInstanceMappingEntry.setIndexNames(
    (0, "SupermicroMIMst-MIB", "fsMIDot1sFutureMstContextId"),
    (0, "SupermicroMIMst-MIB", "fsMIMstInstanceIndex"),
)
if mibBuilder.loadTexts:
    fsMIMstVlanInstanceMappingEntry.setStatus("current")


class _FsMIMstInstanceIndex_Type(Integer32):
    """Custom type fsMIMstInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
        ValueRangeConstraint(4094, 4094),
    )


_FsMIMstInstanceIndex_Type.__name__ = "Integer32"
_FsMIMstInstanceIndex_Object = MibTableColumn
fsMIMstInstanceIndex = _FsMIMstInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 5, 1, 1),
    _FsMIMstInstanceIndex_Type()
)
fsMIMstInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIMstInstanceIndex.setStatus("current")
_FsMIMstMapVlanIndex_Type = VlanId
_FsMIMstMapVlanIndex_Object = MibTableColumn
fsMIMstMapVlanIndex = _FsMIMstMapVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 5, 1, 2),
    _FsMIMstMapVlanIndex_Type()
)
fsMIMstMapVlanIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstMapVlanIndex.setStatus("current")
_FsMIMstUnMapVlanIndex_Type = VlanId
_FsMIMstUnMapVlanIndex_Object = MibTableColumn
fsMIMstUnMapVlanIndex = _FsMIMstUnMapVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 5, 1, 3),
    _FsMIMstUnMapVlanIndex_Type()
)
fsMIMstUnMapVlanIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstUnMapVlanIndex.setStatus("current")


class _FsMIMstSetVlanList_Type(OctetString):
    """Custom type fsMIMstSetVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_FsMIMstSetVlanList_Type.__name__ = "OctetString"
_FsMIMstSetVlanList_Object = MibTableColumn
fsMIMstSetVlanList = _FsMIMstSetVlanList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 5, 1, 4),
    _FsMIMstSetVlanList_Type()
)
fsMIMstSetVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstSetVlanList.setStatus("current")


class _FsMIMstResetVlanList_Type(OctetString):
    """Custom type fsMIMstResetVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_FsMIMstResetVlanList_Type.__name__ = "OctetString"
_FsMIMstResetVlanList_Object = MibTableColumn
fsMIMstResetVlanList = _FsMIMstResetVlanList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 5, 1, 5),
    _FsMIMstResetVlanList_Type()
)
fsMIMstResetVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstResetVlanList.setStatus("current")


class _FsMIMstInstanceVlanMapped_Type(OctetString):
    """Custom type fsMIMstInstanceVlanMapped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FsMIMstInstanceVlanMapped_Type.__name__ = "OctetString"
_FsMIMstInstanceVlanMapped_Object = MibTableColumn
fsMIMstInstanceVlanMapped = _FsMIMstInstanceVlanMapped_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 5, 1, 6),
    _FsMIMstInstanceVlanMapped_Type()
)
fsMIMstInstanceVlanMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstInstanceVlanMapped.setStatus("current")


class _FsMIMstInstanceVlanMapped2k_Type(OctetString):
    """Custom type fsMIMstInstanceVlanMapped2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FsMIMstInstanceVlanMapped2k_Type.__name__ = "OctetString"
_FsMIMstInstanceVlanMapped2k_Object = MibTableColumn
fsMIMstInstanceVlanMapped2k = _FsMIMstInstanceVlanMapped2k_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 5, 1, 7),
    _FsMIMstInstanceVlanMapped2k_Type()
)
fsMIMstInstanceVlanMapped2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstInstanceVlanMapped2k.setStatus("current")


class _FsMIMstInstanceVlanMapped3k_Type(OctetString):
    """Custom type fsMIMstInstanceVlanMapped3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FsMIMstInstanceVlanMapped3k_Type.__name__ = "OctetString"
_FsMIMstInstanceVlanMapped3k_Object = MibTableColumn
fsMIMstInstanceVlanMapped3k = _FsMIMstInstanceVlanMapped3k_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 5, 1, 8),
    _FsMIMstInstanceVlanMapped3k_Type()
)
fsMIMstInstanceVlanMapped3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstInstanceVlanMapped3k.setStatus("current")


class _FsMIMstInstanceVlanMapped4k_Type(OctetString):
    """Custom type fsMIMstInstanceVlanMapped4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FsMIMstInstanceVlanMapped4k_Type.__name__ = "OctetString"
_FsMIMstInstanceVlanMapped4k_Object = MibTableColumn
fsMIMstInstanceVlanMapped4k = _FsMIMstInstanceVlanMapped4k_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 5, 1, 9),
    _FsMIMstInstanceVlanMapped4k_Type()
)
fsMIMstInstanceVlanMapped4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstInstanceVlanMapped4k.setStatus("current")
_FsMIMstCistPortTable_Object = MibTable
fsMIMstCistPortTable = _FsMIMstCistPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6)
)
if mibBuilder.loadTexts:
    fsMIMstCistPortTable.setStatus("current")
_FsMIMstCistPortEntry_Object = MibTableRow
fsMIMstCistPortEntry = _FsMIMstCistPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1)
)
fsMIMstCistPortEntry.setIndexNames(
    (0, "SupermicroMIMst-MIB", "fsMIMstCistPort"),
)
if mibBuilder.loadTexts:
    fsMIMstCistPortEntry.setStatus("current")


class _FsMIMstCistPort_Type(Integer32):
    """Custom type fsMIMstCistPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIMstCistPort_Type.__name__ = "Integer32"
_FsMIMstCistPort_Object = MibTableColumn
fsMIMstCistPort = _FsMIMstCistPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 1),
    _FsMIMstCistPort_Type()
)
fsMIMstCistPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIMstCistPort.setStatus("current")


class _FsMIMstCistPortPathCost_Type(Integer32):
    """Custom type fsMIMstCistPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_FsMIMstCistPortPathCost_Type.__name__ = "Integer32"
_FsMIMstCistPortPathCost_Object = MibTableColumn
fsMIMstCistPortPathCost = _FsMIMstCistPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 2),
    _FsMIMstCistPortPathCost_Type()
)
fsMIMstCistPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCistPortPathCost.setStatus("current")


class _FsMIMstCistPortPriority_Type(Integer32):
    """Custom type fsMIMstCistPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_FsMIMstCistPortPriority_Type.__name__ = "Integer32"
_FsMIMstCistPortPriority_Object = MibTableColumn
fsMIMstCistPortPriority = _FsMIMstCistPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 3),
    _FsMIMstCistPortPriority_Type()
)
fsMIMstCistPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCistPortPriority.setStatus("current")
_FsMIMstCistPortDesignatedRoot_Type = BridgeId
_FsMIMstCistPortDesignatedRoot_Object = MibTableColumn
fsMIMstCistPortDesignatedRoot = _FsMIMstCistPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 4),
    _FsMIMstCistPortDesignatedRoot_Type()
)
fsMIMstCistPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortDesignatedRoot.setStatus("current")
_FsMIMstCistPortDesignatedBridge_Type = BridgeId
_FsMIMstCistPortDesignatedBridge_Object = MibTableColumn
fsMIMstCistPortDesignatedBridge = _FsMIMstCistPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 5),
    _FsMIMstCistPortDesignatedBridge_Type()
)
fsMIMstCistPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortDesignatedBridge.setStatus("current")


class _FsMIMstCistPortDesignatedPort_Type(OctetString):
    """Custom type fsMIMstCistPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_FsMIMstCistPortDesignatedPort_Type.__name__ = "OctetString"
_FsMIMstCistPortDesignatedPort_Object = MibTableColumn
fsMIMstCistPortDesignatedPort = _FsMIMstCistPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 6),
    _FsMIMstCistPortDesignatedPort_Type()
)
fsMIMstCistPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortDesignatedPort.setStatus("current")


class _FsMIMstCistPortAdminP2P_Type(Integer32):
    """Custom type fsMIMstCistPortAdminP2P based on Integer32"""
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


_FsMIMstCistPortAdminP2P_Type.__name__ = "Integer32"
_FsMIMstCistPortAdminP2P_Object = MibTableColumn
fsMIMstCistPortAdminP2P = _FsMIMstCistPortAdminP2P_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 7),
    _FsMIMstCistPortAdminP2P_Type()
)
fsMIMstCistPortAdminP2P.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCistPortAdminP2P.setStatus("current")
_FsMIMstCistPortOperP2P_Type = TruthValue
_FsMIMstCistPortOperP2P_Object = MibTableColumn
fsMIMstCistPortOperP2P = _FsMIMstCistPortOperP2P_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 8),
    _FsMIMstCistPortOperP2P_Type()
)
fsMIMstCistPortOperP2P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortOperP2P.setStatus("current")
_FsMIMstCistPortAdminEdgeStatus_Type = TruthValue
_FsMIMstCistPortAdminEdgeStatus_Object = MibTableColumn
fsMIMstCistPortAdminEdgeStatus = _FsMIMstCistPortAdminEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 9),
    _FsMIMstCistPortAdminEdgeStatus_Type()
)
fsMIMstCistPortAdminEdgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCistPortAdminEdgeStatus.setStatus("current")
_FsMIMstCistPortOperEdgeStatus_Type = TruthValue
_FsMIMstCistPortOperEdgeStatus_Object = MibTableColumn
fsMIMstCistPortOperEdgeStatus = _FsMIMstCistPortOperEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 10),
    _FsMIMstCistPortOperEdgeStatus_Type()
)
fsMIMstCistPortOperEdgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortOperEdgeStatus.setStatus("current")
_FsMIMstCistPortProtocolMigration_Type = TruthValue
_FsMIMstCistPortProtocolMigration_Object = MibTableColumn
fsMIMstCistPortProtocolMigration = _FsMIMstCistPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 11),
    _FsMIMstCistPortProtocolMigration_Type()
)
fsMIMstCistPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCistPortProtocolMigration.setStatus("current")


class _FsMIMstCistPortState_Type(Integer32):
    """Custom type fsMIMstCistPortState based on Integer32"""
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


_FsMIMstCistPortState_Type.__name__ = "Integer32"
_FsMIMstCistPortState_Object = MibTableColumn
fsMIMstCistPortState = _FsMIMstCistPortState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 12),
    _FsMIMstCistPortState_Type()
)
fsMIMstCistPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortState.setStatus("current")


class _FsMIMstCistForcePortState_Type(Integer32):
    """Custom type fsMIMstCistForcePortState based on Integer32"""
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


_FsMIMstCistForcePortState_Type.__name__ = "Integer32"
_FsMIMstCistForcePortState_Object = MibTableColumn
fsMIMstCistForcePortState = _FsMIMstCistForcePortState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 13),
    _FsMIMstCistForcePortState_Type()
)
fsMIMstCistForcePortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCistForcePortState.setStatus("current")
_FsMIMstCistPortForwardTransitions_Type = Counter32
_FsMIMstCistPortForwardTransitions_Object = MibTableColumn
fsMIMstCistPortForwardTransitions = _FsMIMstCistPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 14),
    _FsMIMstCistPortForwardTransitions_Type()
)
fsMIMstCistPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortForwardTransitions.setStatus("current")
_FsMIMstCistPortRxMstBpduCount_Type = Counter32
_FsMIMstCistPortRxMstBpduCount_Object = MibTableColumn
fsMIMstCistPortRxMstBpduCount = _FsMIMstCistPortRxMstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 15),
    _FsMIMstCistPortRxMstBpduCount_Type()
)
fsMIMstCistPortRxMstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortRxMstBpduCount.setStatus("current")
_FsMIMstCistPortRxRstBpduCount_Type = Counter32
_FsMIMstCistPortRxRstBpduCount_Object = MibTableColumn
fsMIMstCistPortRxRstBpduCount = _FsMIMstCistPortRxRstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 16),
    _FsMIMstCistPortRxRstBpduCount_Type()
)
fsMIMstCistPortRxRstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortRxRstBpduCount.setStatus("current")
_FsMIMstCistPortRxConfigBpduCount_Type = Counter32
_FsMIMstCistPortRxConfigBpduCount_Object = MibTableColumn
fsMIMstCistPortRxConfigBpduCount = _FsMIMstCistPortRxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 17),
    _FsMIMstCistPortRxConfigBpduCount_Type()
)
fsMIMstCistPortRxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortRxConfigBpduCount.setStatus("current")
_FsMIMstCistPortRxTcnBpduCount_Type = Counter32
_FsMIMstCistPortRxTcnBpduCount_Object = MibTableColumn
fsMIMstCistPortRxTcnBpduCount = _FsMIMstCistPortRxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 18),
    _FsMIMstCistPortRxTcnBpduCount_Type()
)
fsMIMstCistPortRxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortRxTcnBpduCount.setStatus("current")
_FsMIMstCistPortTxMstBpduCount_Type = Counter32
_FsMIMstCistPortTxMstBpduCount_Object = MibTableColumn
fsMIMstCistPortTxMstBpduCount = _FsMIMstCistPortTxMstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 19),
    _FsMIMstCistPortTxMstBpduCount_Type()
)
fsMIMstCistPortTxMstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortTxMstBpduCount.setStatus("current")
_FsMIMstCistPortTxRstBpduCount_Type = Counter32
_FsMIMstCistPortTxRstBpduCount_Object = MibTableColumn
fsMIMstCistPortTxRstBpduCount = _FsMIMstCistPortTxRstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 20),
    _FsMIMstCistPortTxRstBpduCount_Type()
)
fsMIMstCistPortTxRstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortTxRstBpduCount.setStatus("current")
_FsMIMstCistPortTxConfigBpduCount_Type = Counter32
_FsMIMstCistPortTxConfigBpduCount_Object = MibTableColumn
fsMIMstCistPortTxConfigBpduCount = _FsMIMstCistPortTxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 21),
    _FsMIMstCistPortTxConfigBpduCount_Type()
)
fsMIMstCistPortTxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortTxConfigBpduCount.setStatus("current")
_FsMIMstCistPortTxTcnBpduCount_Type = Counter32
_FsMIMstCistPortTxTcnBpduCount_Object = MibTableColumn
fsMIMstCistPortTxTcnBpduCount = _FsMIMstCistPortTxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 22),
    _FsMIMstCistPortTxTcnBpduCount_Type()
)
fsMIMstCistPortTxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortTxTcnBpduCount.setStatus("current")
_FsMIMstCistPortInvalidMstBpduRxCount_Type = Counter32
_FsMIMstCistPortInvalidMstBpduRxCount_Object = MibTableColumn
fsMIMstCistPortInvalidMstBpduRxCount = _FsMIMstCistPortInvalidMstBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 23),
    _FsMIMstCistPortInvalidMstBpduRxCount_Type()
)
fsMIMstCistPortInvalidMstBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortInvalidMstBpduRxCount.setStatus("current")
_FsMIMstCistPortInvalidRstBpduRxCount_Type = Counter32
_FsMIMstCistPortInvalidRstBpduRxCount_Object = MibTableColumn
fsMIMstCistPortInvalidRstBpduRxCount = _FsMIMstCistPortInvalidRstBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 24),
    _FsMIMstCistPortInvalidRstBpduRxCount_Type()
)
fsMIMstCistPortInvalidRstBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortInvalidRstBpduRxCount.setStatus("current")
_FsMIMstCistPortInvalidConfigBpduRxCount_Type = Counter32
_FsMIMstCistPortInvalidConfigBpduRxCount_Object = MibTableColumn
fsMIMstCistPortInvalidConfigBpduRxCount = _FsMIMstCistPortInvalidConfigBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 25),
    _FsMIMstCistPortInvalidConfigBpduRxCount_Type()
)
fsMIMstCistPortInvalidConfigBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortInvalidConfigBpduRxCount.setStatus("current")
_FsMIMstCistPortInvalidTcnBpduRxCount_Type = Counter32
_FsMIMstCistPortInvalidTcnBpduRxCount_Object = MibTableColumn
fsMIMstCistPortInvalidTcnBpduRxCount = _FsMIMstCistPortInvalidTcnBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 26),
    _FsMIMstCistPortInvalidTcnBpduRxCount_Type()
)
fsMIMstCistPortInvalidTcnBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortInvalidTcnBpduRxCount.setStatus("current")


class _FsMIMstCistPortTransmitSemState_Type(Integer32):
    """Custom type fsMIMstCistPortTransmitSemState based on Integer32"""
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


_FsMIMstCistPortTransmitSemState_Type.__name__ = "Integer32"
_FsMIMstCistPortTransmitSemState_Object = MibTableColumn
fsMIMstCistPortTransmitSemState = _FsMIMstCistPortTransmitSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 27),
    _FsMIMstCistPortTransmitSemState_Type()
)
fsMIMstCistPortTransmitSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortTransmitSemState.setStatus("current")


class _FsMIMstCistPortReceiveSemState_Type(Integer32):
    """Custom type fsMIMstCistPortReceiveSemState based on Integer32"""
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


_FsMIMstCistPortReceiveSemState_Type.__name__ = "Integer32"
_FsMIMstCistPortReceiveSemState_Object = MibTableColumn
fsMIMstCistPortReceiveSemState = _FsMIMstCistPortReceiveSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 28),
    _FsMIMstCistPortReceiveSemState_Type()
)
fsMIMstCistPortReceiveSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortReceiveSemState.setStatus("current")


class _FsMIMstCistPortProtMigrationSemState_Type(Integer32):
    """Custom type fsMIMstCistPortProtMigrationSemState based on Integer32"""
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


_FsMIMstCistPortProtMigrationSemState_Type.__name__ = "Integer32"
_FsMIMstCistPortProtMigrationSemState_Object = MibTableColumn
fsMIMstCistPortProtMigrationSemState = _FsMIMstCistPortProtMigrationSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 29),
    _FsMIMstCistPortProtMigrationSemState_Type()
)
fsMIMstCistPortProtMigrationSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortProtMigrationSemState.setStatus("current")
_FsMIMstCistProtocolMigrationCount_Type = Counter32
_FsMIMstCistProtocolMigrationCount_Object = MibTableColumn
fsMIMstCistProtocolMigrationCount = _FsMIMstCistProtocolMigrationCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 30),
    _FsMIMstCistProtocolMigrationCount_Type()
)
fsMIMstCistProtocolMigrationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistProtocolMigrationCount.setStatus("current")
_FsMIMstCistPortDesignatedCost_Type = Integer32
_FsMIMstCistPortDesignatedCost_Object = MibTableColumn
fsMIMstCistPortDesignatedCost = _FsMIMstCistPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 31),
    _FsMIMstCistPortDesignatedCost_Type()
)
fsMIMstCistPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortDesignatedCost.setStatus("current")
_FsMIMstCistPortRegionalRoot_Type = BridgeId
_FsMIMstCistPortRegionalRoot_Object = MibTableColumn
fsMIMstCistPortRegionalRoot = _FsMIMstCistPortRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 32),
    _FsMIMstCistPortRegionalRoot_Type()
)
fsMIMstCistPortRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortRegionalRoot.setStatus("current")
_FsMIMstCistPortRegionalPathCost_Type = Integer32
_FsMIMstCistPortRegionalPathCost_Object = MibTableColumn
fsMIMstCistPortRegionalPathCost = _FsMIMstCistPortRegionalPathCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 33),
    _FsMIMstCistPortRegionalPathCost_Type()
)
fsMIMstCistPortRegionalPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortRegionalPathCost.setStatus("current")


class _FsMIMstCistSelectedPortRole_Type(Integer32):
    """Custom type fsMIMstCistSelectedPortRole based on Integer32"""
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


_FsMIMstCistSelectedPortRole_Type.__name__ = "Integer32"
_FsMIMstCistSelectedPortRole_Object = MibTableColumn
fsMIMstCistSelectedPortRole = _FsMIMstCistSelectedPortRole_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 34),
    _FsMIMstCistSelectedPortRole_Type()
)
fsMIMstCistSelectedPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistSelectedPortRole.setStatus("current")


class _FsMIMstCistCurrentPortRole_Type(Integer32):
    """Custom type fsMIMstCistCurrentPortRole based on Integer32"""
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


_FsMIMstCistCurrentPortRole_Type.__name__ = "Integer32"
_FsMIMstCistCurrentPortRole_Object = MibTableColumn
fsMIMstCistCurrentPortRole = _FsMIMstCistCurrentPortRole_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 35),
    _FsMIMstCistCurrentPortRole_Type()
)
fsMIMstCistCurrentPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistCurrentPortRole.setStatus("current")


class _FsMIMstCistPortInfoSemState_Type(Integer32):
    """Custom type fsMIMstCistPortInfoSemState based on Integer32"""
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


_FsMIMstCistPortInfoSemState_Type.__name__ = "Integer32"
_FsMIMstCistPortInfoSemState_Object = MibTableColumn
fsMIMstCistPortInfoSemState = _FsMIMstCistPortInfoSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 36),
    _FsMIMstCistPortInfoSemState_Type()
)
fsMIMstCistPortInfoSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortInfoSemState.setStatus("current")


class _FsMIMstCistPortRoleTransitionSemState_Type(Integer32):
    """Custom type fsMIMstCistPortRoleTransitionSemState based on Integer32"""
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


_FsMIMstCistPortRoleTransitionSemState_Type.__name__ = "Integer32"
_FsMIMstCistPortRoleTransitionSemState_Object = MibTableColumn
fsMIMstCistPortRoleTransitionSemState = _FsMIMstCistPortRoleTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 37),
    _FsMIMstCistPortRoleTransitionSemState_Type()
)
fsMIMstCistPortRoleTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortRoleTransitionSemState.setStatus("current")


class _FsMIMstCistPortStateTransitionSemState_Type(Integer32):
    """Custom type fsMIMstCistPortStateTransitionSemState based on Integer32"""
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


_FsMIMstCistPortStateTransitionSemState_Type.__name__ = "Integer32"
_FsMIMstCistPortStateTransitionSemState_Object = MibTableColumn
fsMIMstCistPortStateTransitionSemState = _FsMIMstCistPortStateTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 38),
    _FsMIMstCistPortStateTransitionSemState_Type()
)
fsMIMstCistPortStateTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortStateTransitionSemState.setStatus("current")


class _FsMIMstCistPortTopologyChangeSemState_Type(Integer32):
    """Custom type fsMIMstCistPortTopologyChangeSemState based on Integer32"""
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


_FsMIMstCistPortTopologyChangeSemState_Type.__name__ = "Integer32"
_FsMIMstCistPortTopologyChangeSemState_Object = MibTableColumn
fsMIMstCistPortTopologyChangeSemState = _FsMIMstCistPortTopologyChangeSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 39),
    _FsMIMstCistPortTopologyChangeSemState_Type()
)
fsMIMstCistPortTopologyChangeSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortTopologyChangeSemState.setStatus("current")


class _FsMIMstCistPortHelloTime_Type(Timeout):
    """Custom type fsMIMstCistPortHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(200, 200),
    )


_FsMIMstCistPortHelloTime_Type.__name__ = "Timeout"
_FsMIMstCistPortHelloTime_Object = MibTableColumn
fsMIMstCistPortHelloTime = _FsMIMstCistPortHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 40),
    _FsMIMstCistPortHelloTime_Type()
)
fsMIMstCistPortHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCistPortHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    fsMIMstCistPortHelloTime.setUnits("centi-seconds")


class _FsMIMstCistPortOperVersion_Type(Integer32):
    """Custom type fsMIMstCistPortOperVersion based on Integer32"""
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


_FsMIMstCistPortOperVersion_Type.__name__ = "Integer32"
_FsMIMstCistPortOperVersion_Object = MibTableColumn
fsMIMstCistPortOperVersion = _FsMIMstCistPortOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 41),
    _FsMIMstCistPortOperVersion_Type()
)
fsMIMstCistPortOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortOperVersion.setStatus("current")
_FsMIMstCistPortEffectivePortState_Type = TruthValue
_FsMIMstCistPortEffectivePortState_Object = MibTableColumn
fsMIMstCistPortEffectivePortState = _FsMIMstCistPortEffectivePortState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 42),
    _FsMIMstCistPortEffectivePortState_Type()
)
fsMIMstCistPortEffectivePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortEffectivePortState.setStatus("current")
_FsMIMstCistPortAutoEdgeStatus_Type = TruthValue
_FsMIMstCistPortAutoEdgeStatus_Object = MibTableColumn
fsMIMstCistPortAutoEdgeStatus = _FsMIMstCistPortAutoEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 43),
    _FsMIMstCistPortAutoEdgeStatus_Type()
)
fsMIMstCistPortAutoEdgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCistPortAutoEdgeStatus.setStatus("current")
_FsMIMstCistPortRestrictedRole_Type = TruthValue
_FsMIMstCistPortRestrictedRole_Object = MibTableColumn
fsMIMstCistPortRestrictedRole = _FsMIMstCistPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 44),
    _FsMIMstCistPortRestrictedRole_Type()
)
fsMIMstCistPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCistPortRestrictedRole.setStatus("current")
_FsMIMstCistPortRestrictedTCN_Type = TruthValue
_FsMIMstCistPortRestrictedTCN_Object = MibTableColumn
fsMIMstCistPortRestrictedTCN = _FsMIMstCistPortRestrictedTCN_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 45),
    _FsMIMstCistPortRestrictedTCN_Type()
)
fsMIMstCistPortRestrictedTCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCistPortRestrictedTCN.setStatus("current")


class _FsMIMstCistPortAdminPathCost_Type(Integer32):
    """Custom type fsMIMstCistPortAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_FsMIMstCistPortAdminPathCost_Type.__name__ = "Integer32"
_FsMIMstCistPortAdminPathCost_Object = MibTableColumn
fsMIMstCistPortAdminPathCost = _FsMIMstCistPortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 46),
    _FsMIMstCistPortAdminPathCost_Type()
)
fsMIMstCistPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCistPortAdminPathCost.setStatus("current")


class _FsMIMstCistPortEnableBPDURx_Type(TruthValue):
    """Custom type fsMIMstCistPortEnableBPDURx based on TruthValue"""
    defaultValue = 1


_FsMIMstCistPortEnableBPDURx_Type.__name__ = "TruthValue"
_FsMIMstCistPortEnableBPDURx_Object = MibTableColumn
fsMIMstCistPortEnableBPDURx = _FsMIMstCistPortEnableBPDURx_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 47),
    _FsMIMstCistPortEnableBPDURx_Type()
)
fsMIMstCistPortEnableBPDURx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCistPortEnableBPDURx.setStatus("current")


class _FsMIMstCistPortEnableBPDUTx_Type(TruthValue):
    """Custom type fsMIMstCistPortEnableBPDUTx based on TruthValue"""
    defaultValue = 1


_FsMIMstCistPortEnableBPDUTx_Type.__name__ = "TruthValue"
_FsMIMstCistPortEnableBPDUTx_Object = MibTableColumn
fsMIMstCistPortEnableBPDUTx = _FsMIMstCistPortEnableBPDUTx_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 48),
    _FsMIMstCistPortEnableBPDUTx_Type()
)
fsMIMstCistPortEnableBPDUTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCistPortEnableBPDUTx.setStatus("current")
_FsMIMstCistPortPseudoRootId_Type = BridgeId
_FsMIMstCistPortPseudoRootId_Object = MibTableColumn
fsMIMstCistPortPseudoRootId = _FsMIMstCistPortPseudoRootId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 49),
    _FsMIMstCistPortPseudoRootId_Type()
)
fsMIMstCistPortPseudoRootId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCistPortPseudoRootId.setStatus("current")


class _FsMIMstCistPortIsL2Gp_Type(TruthValue):
    """Custom type fsMIMstCistPortIsL2Gp based on TruthValue"""
    defaultValue = 2


_FsMIMstCistPortIsL2Gp_Type.__name__ = "TruthValue"
_FsMIMstCistPortIsL2Gp_Object = MibTableColumn
fsMIMstCistPortIsL2Gp = _FsMIMstCistPortIsL2Gp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 50),
    _FsMIMstCistPortIsL2Gp_Type()
)
fsMIMstCistPortIsL2Gp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCistPortIsL2Gp.setStatus("current")


class _FsMIMstCistPortLoopGuard_Type(TruthValue):
    """Custom type fsMIMstCistPortLoopGuard based on TruthValue"""
    defaultValue = 2


_FsMIMstCistPortLoopGuard_Type.__name__ = "TruthValue"
_FsMIMstCistPortLoopGuard_Object = MibTableColumn
fsMIMstCistPortLoopGuard = _FsMIMstCistPortLoopGuard_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 51),
    _FsMIMstCistPortLoopGuard_Type()
)
fsMIMstCistPortLoopGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCistPortLoopGuard.setStatus("current")
_FsMIMstCistPortClearStats_Type = TruthValue
_FsMIMstCistPortClearStats_Object = MibTableColumn
fsMIMstCistPortClearStats = _FsMIMstCistPortClearStats_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 52),
    _FsMIMstCistPortClearStats_Type()
)
fsMIMstCistPortClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCistPortClearStats.setStatus("current")


class _FsMIMstCistPortRcvdEvent_Type(Integer32):
    """Custom type fsMIMstCistPortRcvdEvent based on Integer32"""
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


_FsMIMstCistPortRcvdEvent_Type.__name__ = "Integer32"
_FsMIMstCistPortRcvdEvent_Object = MibTableColumn
fsMIMstCistPortRcvdEvent = _FsMIMstCistPortRcvdEvent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 53),
    _FsMIMstCistPortRcvdEvent_Type()
)
fsMIMstCistPortRcvdEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortRcvdEvent.setStatus("current")
_FsMIMstCistPortRcvdEventSubType_Type = Integer32
_FsMIMstCistPortRcvdEventSubType_Object = MibTableColumn
fsMIMstCistPortRcvdEventSubType = _FsMIMstCistPortRcvdEventSubType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 54),
    _FsMIMstCistPortRcvdEventSubType_Type()
)
fsMIMstCistPortRcvdEventSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortRcvdEventSubType.setStatus("current")
_FsMIMstCistPortRcvdEventTimeStamp_Type = Unsigned32
_FsMIMstCistPortRcvdEventTimeStamp_Object = MibTableColumn
fsMIMstCistPortRcvdEventTimeStamp = _FsMIMstCistPortRcvdEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 55),
    _FsMIMstCistPortRcvdEventTimeStamp_Type()
)
fsMIMstCistPortRcvdEventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistPortRcvdEventTimeStamp.setStatus("current")


class _FsMIMstCistLoopInconsistentState_Type(TruthValue):
    """Custom type fsMIMstCistLoopInconsistentState based on TruthValue"""
    defaultValue = 2


_FsMIMstCistLoopInconsistentState_Type.__name__ = "TruthValue"
_FsMIMstCistLoopInconsistentState_Object = MibTableColumn
fsMIMstCistLoopInconsistentState = _FsMIMstCistLoopInconsistentState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 56),
    _FsMIMstCistLoopInconsistentState_Type()
)
fsMIMstCistLoopInconsistentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstCistLoopInconsistentState.setStatus("current")


class _FsMIMstCistPortBpduGuard_Type(Integer32):
    """Custom type fsMIMstCistPortBpduGuard based on Integer32"""
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


_FsMIMstCistPortBpduGuard_Type.__name__ = "Integer32"
_FsMIMstCistPortBpduGuard_Object = MibTableColumn
fsMIMstCistPortBpduGuard = _FsMIMstCistPortBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 6, 1, 57),
    _FsMIMstCistPortBpduGuard_Type()
)
fsMIMstCistPortBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstCistPortBpduGuard.setStatus("current")
_FsMIMstMstiPortTable_Object = MibTable
fsMIMstMstiPortTable = _FsMIMstMstiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7)
)
if mibBuilder.loadTexts:
    fsMIMstMstiPortTable.setStatus("current")
_FsMIMstMstiPortEntry_Object = MibTableRow
fsMIMstMstiPortEntry = _FsMIMstMstiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1)
)
fsMIMstMstiPortEntry.setIndexNames(
    (0, "SupermicroMIMst-MIB", "fsMIMstMstiPort"),
    (0, "SupermicroMIMst-MIB", "fsMIMstInstanceIndex"),
)
if mibBuilder.loadTexts:
    fsMIMstMstiPortEntry.setStatus("current")


class _FsMIMstMstiPort_Type(Integer32):
    """Custom type fsMIMstMstiPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIMstMstiPort_Type.__name__ = "Integer32"
_FsMIMstMstiPort_Object = MibTableColumn
fsMIMstMstiPort = _FsMIMstMstiPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1, 1),
    _FsMIMstMstiPort_Type()
)
fsMIMstMstiPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIMstMstiPort.setStatus("current")


class _FsMIMstMstiPortPathCost_Type(Integer32):
    """Custom type fsMIMstMstiPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_FsMIMstMstiPortPathCost_Type.__name__ = "Integer32"
_FsMIMstMstiPortPathCost_Object = MibTableColumn
fsMIMstMstiPortPathCost = _FsMIMstMstiPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1, 2),
    _FsMIMstMstiPortPathCost_Type()
)
fsMIMstMstiPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstMstiPortPathCost.setStatus("current")


class _FsMIMstMstiPortPriority_Type(Integer32):
    """Custom type fsMIMstMstiPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_FsMIMstMstiPortPriority_Type.__name__ = "Integer32"
_FsMIMstMstiPortPriority_Object = MibTableColumn
fsMIMstMstiPortPriority = _FsMIMstMstiPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1, 3),
    _FsMIMstMstiPortPriority_Type()
)
fsMIMstMstiPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstMstiPortPriority.setStatus("current")
_FsMIMstMstiPortDesignatedRoot_Type = BridgeId
_FsMIMstMstiPortDesignatedRoot_Object = MibTableColumn
fsMIMstMstiPortDesignatedRoot = _FsMIMstMstiPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1, 4),
    _FsMIMstMstiPortDesignatedRoot_Type()
)
fsMIMstMstiPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiPortDesignatedRoot.setStatus("current")
_FsMIMstMstiPortDesignatedBridge_Type = BridgeId
_FsMIMstMstiPortDesignatedBridge_Object = MibTableColumn
fsMIMstMstiPortDesignatedBridge = _FsMIMstMstiPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1, 5),
    _FsMIMstMstiPortDesignatedBridge_Type()
)
fsMIMstMstiPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiPortDesignatedBridge.setStatus("current")


class _FsMIMstMstiPortDesignatedPort_Type(OctetString):
    """Custom type fsMIMstMstiPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_FsMIMstMstiPortDesignatedPort_Type.__name__ = "OctetString"
_FsMIMstMstiPortDesignatedPort_Object = MibTableColumn
fsMIMstMstiPortDesignatedPort = _FsMIMstMstiPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1, 6),
    _FsMIMstMstiPortDesignatedPort_Type()
)
fsMIMstMstiPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiPortDesignatedPort.setStatus("current")


class _FsMIMstMstiPortState_Type(Integer32):
    """Custom type fsMIMstMstiPortState based on Integer32"""
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


_FsMIMstMstiPortState_Type.__name__ = "Integer32"
_FsMIMstMstiPortState_Object = MibTableColumn
fsMIMstMstiPortState = _FsMIMstMstiPortState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1, 7),
    _FsMIMstMstiPortState_Type()
)
fsMIMstMstiPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiPortState.setStatus("current")


class _FsMIMstMstiForcePortState_Type(Integer32):
    """Custom type fsMIMstMstiForcePortState based on Integer32"""
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


_FsMIMstMstiForcePortState_Type.__name__ = "Integer32"
_FsMIMstMstiForcePortState_Object = MibTableColumn
fsMIMstMstiForcePortState = _FsMIMstMstiForcePortState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1, 8),
    _FsMIMstMstiForcePortState_Type()
)
fsMIMstMstiForcePortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstMstiForcePortState.setStatus("current")
_FsMIMstMstiPortForwardTransitions_Type = Counter32
_FsMIMstMstiPortForwardTransitions_Object = MibTableColumn
fsMIMstMstiPortForwardTransitions = _FsMIMstMstiPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1, 9),
    _FsMIMstMstiPortForwardTransitions_Type()
)
fsMIMstMstiPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiPortForwardTransitions.setStatus("current")
_FsMIMstMstiPortReceivedBPDUs_Type = Counter32
_FsMIMstMstiPortReceivedBPDUs_Object = MibTableColumn
fsMIMstMstiPortReceivedBPDUs = _FsMIMstMstiPortReceivedBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1, 10),
    _FsMIMstMstiPortReceivedBPDUs_Type()
)
fsMIMstMstiPortReceivedBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiPortReceivedBPDUs.setStatus("current")
_FsMIMstMstiPortTransmittedBPDUs_Type = Counter32
_FsMIMstMstiPortTransmittedBPDUs_Object = MibTableColumn
fsMIMstMstiPortTransmittedBPDUs = _FsMIMstMstiPortTransmittedBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1, 11),
    _FsMIMstMstiPortTransmittedBPDUs_Type()
)
fsMIMstMstiPortTransmittedBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiPortTransmittedBPDUs.setStatus("current")
_FsMIMstMstiPortInvalidBPDUsRcvd_Type = Counter32
_FsMIMstMstiPortInvalidBPDUsRcvd_Object = MibTableColumn
fsMIMstMstiPortInvalidBPDUsRcvd = _FsMIMstMstiPortInvalidBPDUsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1, 12),
    _FsMIMstMstiPortInvalidBPDUsRcvd_Type()
)
fsMIMstMstiPortInvalidBPDUsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiPortInvalidBPDUsRcvd.setStatus("current")
_FsMIMstMstiPortDesignatedCost_Type = Integer32
_FsMIMstMstiPortDesignatedCost_Object = MibTableColumn
fsMIMstMstiPortDesignatedCost = _FsMIMstMstiPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1, 13),
    _FsMIMstMstiPortDesignatedCost_Type()
)
fsMIMstMstiPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiPortDesignatedCost.setStatus("current")


class _FsMIMstMstiSelectedPortRole_Type(Integer32):
    """Custom type fsMIMstMstiSelectedPortRole based on Integer32"""
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


_FsMIMstMstiSelectedPortRole_Type.__name__ = "Integer32"
_FsMIMstMstiSelectedPortRole_Object = MibTableColumn
fsMIMstMstiSelectedPortRole = _FsMIMstMstiSelectedPortRole_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1, 14),
    _FsMIMstMstiSelectedPortRole_Type()
)
fsMIMstMstiSelectedPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiSelectedPortRole.setStatus("current")


class _FsMIMstMstiCurrentPortRole_Type(Integer32):
    """Custom type fsMIMstMstiCurrentPortRole based on Integer32"""
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


_FsMIMstMstiCurrentPortRole_Type.__name__ = "Integer32"
_FsMIMstMstiCurrentPortRole_Object = MibTableColumn
fsMIMstMstiCurrentPortRole = _FsMIMstMstiCurrentPortRole_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1, 15),
    _FsMIMstMstiCurrentPortRole_Type()
)
fsMIMstMstiCurrentPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiCurrentPortRole.setStatus("current")


class _FsMIMstMstiPortInfoSemState_Type(Integer32):
    """Custom type fsMIMstMstiPortInfoSemState based on Integer32"""
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


_FsMIMstMstiPortInfoSemState_Type.__name__ = "Integer32"
_FsMIMstMstiPortInfoSemState_Object = MibTableColumn
fsMIMstMstiPortInfoSemState = _FsMIMstMstiPortInfoSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1, 16),
    _FsMIMstMstiPortInfoSemState_Type()
)
fsMIMstMstiPortInfoSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiPortInfoSemState.setStatus("current")


class _FsMIMstMstiPortRoleTransitionSemState_Type(Integer32):
    """Custom type fsMIMstMstiPortRoleTransitionSemState based on Integer32"""
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


_FsMIMstMstiPortRoleTransitionSemState_Type.__name__ = "Integer32"
_FsMIMstMstiPortRoleTransitionSemState_Object = MibTableColumn
fsMIMstMstiPortRoleTransitionSemState = _FsMIMstMstiPortRoleTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1, 17),
    _FsMIMstMstiPortRoleTransitionSemState_Type()
)
fsMIMstMstiPortRoleTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiPortRoleTransitionSemState.setStatus("current")


class _FsMIMstMstiPortStateTransitionSemState_Type(Integer32):
    """Custom type fsMIMstMstiPortStateTransitionSemState based on Integer32"""
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


_FsMIMstMstiPortStateTransitionSemState_Type.__name__ = "Integer32"
_FsMIMstMstiPortStateTransitionSemState_Object = MibTableColumn
fsMIMstMstiPortStateTransitionSemState = _FsMIMstMstiPortStateTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1, 18),
    _FsMIMstMstiPortStateTransitionSemState_Type()
)
fsMIMstMstiPortStateTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiPortStateTransitionSemState.setStatus("current")


class _FsMIMstMstiPortTopologyChangeSemState_Type(Integer32):
    """Custom type fsMIMstMstiPortTopologyChangeSemState based on Integer32"""
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


_FsMIMstMstiPortTopologyChangeSemState_Type.__name__ = "Integer32"
_FsMIMstMstiPortTopologyChangeSemState_Object = MibTableColumn
fsMIMstMstiPortTopologyChangeSemState = _FsMIMstMstiPortTopologyChangeSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1, 19),
    _FsMIMstMstiPortTopologyChangeSemState_Type()
)
fsMIMstMstiPortTopologyChangeSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiPortTopologyChangeSemState.setStatus("current")
_FsMIMstMstiPortEffectivePortState_Type = TruthValue
_FsMIMstMstiPortEffectivePortState_Object = MibTableColumn
fsMIMstMstiPortEffectivePortState = _FsMIMstMstiPortEffectivePortState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1, 20),
    _FsMIMstMstiPortEffectivePortState_Type()
)
fsMIMstMstiPortEffectivePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiPortEffectivePortState.setStatus("current")


class _FsMIMstMstiPortAdminPathCost_Type(Integer32):
    """Custom type fsMIMstMstiPortAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_FsMIMstMstiPortAdminPathCost_Type.__name__ = "Integer32"
_FsMIMstMstiPortAdminPathCost_Object = MibTableColumn
fsMIMstMstiPortAdminPathCost = _FsMIMstMstiPortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1, 21),
    _FsMIMstMstiPortAdminPathCost_Type()
)
fsMIMstMstiPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstMstiPortAdminPathCost.setStatus("current")
_FsMIMstMstiPortPseudoRootId_Type = BridgeId
_FsMIMstMstiPortPseudoRootId_Object = MibTableColumn
fsMIMstMstiPortPseudoRootId = _FsMIMstMstiPortPseudoRootId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1, 22),
    _FsMIMstMstiPortPseudoRootId_Type()
)
fsMIMstMstiPortPseudoRootId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstMstiPortPseudoRootId.setStatus("current")
_FsMIMstMstiPortClearStats_Type = TruthValue
_FsMIMstMstiPortClearStats_Object = MibTableColumn
fsMIMstMstiPortClearStats = _FsMIMstMstiPortClearStats_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1, 23),
    _FsMIMstMstiPortClearStats_Type()
)
fsMIMstMstiPortClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstMstiPortClearStats.setStatus("current")
_FsMIMstMstiPortStateChangeTimeStamp_Type = Unsigned32
_FsMIMstMstiPortStateChangeTimeStamp_Object = MibTableColumn
fsMIMstMstiPortStateChangeTimeStamp = _FsMIMstMstiPortStateChangeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 7, 1, 24),
    _FsMIMstMstiPortStateChangeTimeStamp_Type()
)
fsMIMstMstiPortStateChangeTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstMstiPortStateChangeTimeStamp.setStatus("current")
_FsMIMstPortExtTable_Object = MibTable
fsMIMstPortExtTable = _FsMIMstPortExtTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 8)
)
if mibBuilder.loadTexts:
    fsMIMstPortExtTable.setStatus("current")
_FsMIMstPortExtEntry_Object = MibTableRow
fsMIMstPortExtEntry = _FsMIMstPortExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 8, 1)
)
fsMIMstPortExtEntry.setIndexNames(
    (0, "SupermicroMIMst-MIB", "fsMIMstPort"),
)
if mibBuilder.loadTexts:
    fsMIMstPortExtEntry.setStatus("current")


class _FsMIMstPort_Type(Integer32):
    """Custom type fsMIMstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_FsMIMstPort_Type.__name__ = "Integer32"
_FsMIMstPort_Object = MibTableColumn
fsMIMstPort = _FsMIMstPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 8, 1, 1),
    _FsMIMstPort_Type()
)
fsMIMstPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIMstPort.setStatus("current")
_FsMIMstPortRowStatus_Type = RowStatus
_FsMIMstPortRowStatus_Object = MibTableColumn
fsMIMstPortRowStatus = _FsMIMstPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 1, 8, 1, 2),
    _FsMIMstPortRowStatus_Type()
)
fsMIMstPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIMstPortRowStatus.setStatus("current")
_FsMIDot1sFsMstTrapsControl_ObjectIdentity = ObjectIdentity
fsMIDot1sFsMstTrapsControl = _FsMIDot1sFsMstTrapsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 2)
)


class _FsMIDot1sFsMstSetGlobalTrapOption_Type(Integer32):
    """Custom type fsMIDot1sFsMstSetGlobalTrapOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsMIDot1sFsMstSetGlobalTrapOption_Type.__name__ = "Integer32"
_FsMIDot1sFsMstSetGlobalTrapOption_Object = MibScalar
fsMIDot1sFsMstSetGlobalTrapOption = _FsMIDot1sFsMstSetGlobalTrapOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 2, 1),
    _FsMIDot1sFsMstSetGlobalTrapOption_Type()
)
fsMIDot1sFsMstSetGlobalTrapOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1sFsMstSetGlobalTrapOption.setStatus("current")


class _FsMIMstGlobalErrTrapType_Type(Integer32):
    """Custom type fsMIMstGlobalErrTrapType based on Integer32"""
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


_FsMIMstGlobalErrTrapType_Type.__name__ = "Integer32"
_FsMIMstGlobalErrTrapType_Object = MibScalar
fsMIMstGlobalErrTrapType = _FsMIMstGlobalErrTrapType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 2, 2),
    _FsMIMstGlobalErrTrapType_Type()
)
fsMIMstGlobalErrTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstGlobalErrTrapType.setStatus("current")
_FsMIDot1sFsMstTrapsControlTable_Object = MibTable
fsMIDot1sFsMstTrapsControlTable = _FsMIDot1sFsMstTrapsControlTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 2, 3)
)
if mibBuilder.loadTexts:
    fsMIDot1sFsMstTrapsControlTable.setStatus("current")
_FsMIDot1sFsMstTrapsControlEntry_Object = MibTableRow
fsMIDot1sFsMstTrapsControlEntry = _FsMIDot1sFsMstTrapsControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 2, 3, 1)
)
fsMIDot1sFsMstTrapsControlEntry.setIndexNames(
    (0, "SupermicroMIMst-MIB", "fsMIDot1sFutureMstContextId"),
)
if mibBuilder.loadTexts:
    fsMIDot1sFsMstTrapsControlEntry.setStatus("current")


class _FsMIMstSetTraps_Type(Integer32):
    """Custom type fsMIMstSetTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FsMIMstSetTraps_Type.__name__ = "Integer32"
_FsMIMstSetTraps_Object = MibTableColumn
fsMIMstSetTraps = _FsMIMstSetTraps_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 2, 3, 1, 1),
    _FsMIMstSetTraps_Type()
)
fsMIMstSetTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIMstSetTraps.setStatus("current")


class _FsMIMstGenTrapType_Type(Integer32):
    """Custom type fsMIMstGenTrapType based on Integer32"""
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


_FsMIMstGenTrapType_Type.__name__ = "Integer32"
_FsMIMstGenTrapType_Object = MibTableColumn
fsMIMstGenTrapType = _FsMIMstGenTrapType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 2, 3, 1, 2),
    _FsMIMstGenTrapType_Type()
)
fsMIMstGenTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstGenTrapType.setStatus("current")
_FsMIMstPortTrapNotificationTable_Object = MibTable
fsMIMstPortTrapNotificationTable = _FsMIMstPortTrapNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 2, 4)
)
if mibBuilder.loadTexts:
    fsMIMstPortTrapNotificationTable.setStatus("current")
_FsMIMstPortTrapNotificationEntry_Object = MibTableRow
fsMIMstPortTrapNotificationEntry = _FsMIMstPortTrapNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 2, 4, 1)
)
fsMIMstPortTrapNotificationEntry.setIndexNames(
    (0, "SupermicroMIMst-MIB", "fsMIMstPortTrapIndex"),
)
if mibBuilder.loadTexts:
    fsMIMstPortTrapNotificationEntry.setStatus("current")


class _FsMIMstPortTrapIndex_Type(Integer32):
    """Custom type fsMIMstPortTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_FsMIMstPortTrapIndex_Type.__name__ = "Integer32"
_FsMIMstPortTrapIndex_Object = MibTableColumn
fsMIMstPortTrapIndex = _FsMIMstPortTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 2, 4, 1, 1),
    _FsMIMstPortTrapIndex_Type()
)
fsMIMstPortTrapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIMstPortTrapIndex.setStatus("current")


class _FsMIMstPortMigrationType_Type(Integer32):
    """Custom type fsMIMstPortMigrationType based on Integer32"""
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


_FsMIMstPortMigrationType_Type.__name__ = "Integer32"
_FsMIMstPortMigrationType_Object = MibTableColumn
fsMIMstPortMigrationType = _FsMIMstPortMigrationType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 2, 4, 1, 2),
    _FsMIMstPortMigrationType_Type()
)
fsMIMstPortMigrationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstPortMigrationType.setStatus("current")


class _FsMIMstPktErrType_Type(Integer32):
    """Custom type fsMIMstPktErrType based on Integer32"""
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


_FsMIMstPktErrType_Type.__name__ = "Integer32"
_FsMIMstPktErrType_Object = MibTableColumn
fsMIMstPktErrType = _FsMIMstPktErrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 2, 4, 1, 3),
    _FsMIMstPktErrType_Type()
)
fsMIMstPktErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstPktErrType.setStatus("current")
_FsMIMstPktErrVal_Type = Integer32
_FsMIMstPktErrVal_Object = MibTableColumn
fsMIMstPktErrVal = _FsMIMstPktErrVal_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 2, 4, 1, 4),
    _FsMIMstPktErrVal_Type()
)
fsMIMstPktErrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstPktErrVal.setStatus("current")
_FsMIMstPortRoleTrapNotificationTable_Object = MibTable
fsMIMstPortRoleTrapNotificationTable = _FsMIMstPortRoleTrapNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 2, 5)
)
if mibBuilder.loadTexts:
    fsMIMstPortRoleTrapNotificationTable.setStatus("current")
_FsMIMstPortRoleTrapNotificationEntry_Object = MibTableRow
fsMIMstPortRoleTrapNotificationEntry = _FsMIMstPortRoleTrapNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 2, 5, 1)
)
fsMIMstPortRoleTrapNotificationEntry.setIndexNames(
    (0, "SupermicroMIMst-MIB", "fsMIMstPortTrapIndex"),
    (0, "SupermicroMIMst-MIB", "fsMIMstMstiInstanceIndex"),
)
if mibBuilder.loadTexts:
    fsMIMstPortRoleTrapNotificationEntry.setStatus("current")


class _FsMIMstPortRoleType_Type(Integer32):
    """Custom type fsMIMstPortRoleType based on Integer32"""
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


_FsMIMstPortRoleType_Type.__name__ = "Integer32"
_FsMIMstPortRoleType_Object = MibTableColumn
fsMIMstPortRoleType = _FsMIMstPortRoleType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 2, 5, 1, 1),
    _FsMIMstPortRoleType_Type()
)
fsMIMstPortRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstPortRoleType.setStatus("current")


class _FsMIMstOldRoleType_Type(Integer32):
    """Custom type fsMIMstOldRoleType based on Integer32"""
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


_FsMIMstOldRoleType_Type.__name__ = "Integer32"
_FsMIMstOldRoleType_Object = MibTableColumn
fsMIMstOldRoleType = _FsMIMstOldRoleType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 2, 5, 1, 2),
    _FsMIMstOldRoleType_Type()
)
fsMIMstOldRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIMstOldRoleType.setStatus("current")
_FsMIDot1sFutureMstTraps_ObjectIdentity = ObjectIdentity
fsMIDot1sFutureMstTraps = _FsMIDot1sFutureMstTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 3)
)
_FsMIMstTraps_ObjectIdentity = ObjectIdentity
fsMIMstTraps = _FsMIMstTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 3, 0)
)

# Managed Objects groups


# Notification objects

fsMIMstGlobalErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 3, 0, 1)
)
fsMIMstGlobalErrTrap.setObjects(
      *(("SupermicroMIMst-MIB", "fsMIMstBrgAddress"),
        ("SupermicroMIMst-MIB", "fsMIMstGlobalErrTrapType"))
)
if mibBuilder.loadTexts:
    fsMIMstGlobalErrTrap.setStatus(
        "current"
    )

fsMIMstGenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 3, 0, 2)
)
fsMIMstGenTrap.setObjects(
      *(("SupermicroMIMst-MIB", "fsMIMstBrgAddress"),
        ("SupermicroMIMst-MIB", "fsMIMstContextName"),
        ("SupermicroMIMst-MIB", "fsMIMstGenTrapType"))
)
if mibBuilder.loadTexts:
    fsMIMstGenTrap.setStatus(
        "current"
    )

fsMIMstNewRootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 3, 0, 3)
)
fsMIMstNewRootTrap.setObjects(
      *(("SupermicroMIMst-MIB", "fsMIMstBrgAddress"),
        ("SupermicroMIMst-MIB", "fsMIMstContextName"),
        ("SupermicroMIMst-MIB", "fsMIMstOldDesignatedRoot"),
        ("SupermicroMIMst-MIB", "fsMIMstMstiBridgeRegionalRoot"))
)
if mibBuilder.loadTexts:
    fsMIMstNewRootTrap.setStatus(
        "current"
    )

fsMIMstTopologyChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 3, 0, 4)
)
fsMIMstTopologyChgTrap.setObjects(
      *(("SupermicroMIMst-MIB", "fsMIMstBrgAddress"),
        ("SupermicroMIMst-MIB", "fsMIMstContextName"),
        ("SupermicroMIMst-MIB", "fsMIMstMstiTopChanges"))
)
if mibBuilder.loadTexts:
    fsMIMstTopologyChgTrap.setStatus(
        "current"
    )

fsMIMstProtocolMigrationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 3, 0, 5)
)
fsMIMstProtocolMigrationTrap.setObjects(
      *(("SupermicroMIMst-MIB", "fsMIMstBrgAddress"),
        ("SupermicroMIMst-MIB", "fsMIMstContextName"),
        ("SupermicroMIMst-MIB", "fsMIMstForceProtocolVersion"),
        ("SupermicroMIMst-MIB", "fsMIMstPortMigrationType"))
)
if mibBuilder.loadTexts:
    fsMIMstProtocolMigrationTrap.setStatus(
        "current"
    )

fsMIMstInvalidBpduRxdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 3, 0, 6)
)
fsMIMstInvalidBpduRxdTrap.setObjects(
      *(("SupermicroMIMst-MIB", "fsMIMstBrgAddress"),
        ("SupermicroMIMst-MIB", "fsMIMstContextName"),
        ("SupermicroMIMst-MIB", "fsMIMstPktErrType"),
        ("SupermicroMIMst-MIB", "fsMIMstPktErrVal"))
)
if mibBuilder.loadTexts:
    fsMIMstInvalidBpduRxdTrap.setStatus(
        "current"
    )

fsMIMstRegionConfigChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 3, 0, 7)
)
fsMIMstRegionConfigChangeTrap.setObjects(
      *(("SupermicroMIMst-MIB", "fsMIMstBrgAddress"),
        ("SupermicroMIMst-MIB", "fsMIMstContextName"),
        ("SupermicroMIMst-MIB", "fsMIMstMstiConfigIdSel"),
        ("SupermicroMIMst-MIB", "fsMIMstMstiRegionName"),
        ("SupermicroMIMst-MIB", "fsMIMstMstiRegionVersion"),
        ("SupermicroMIMst-MIB", "fsMIMstMstiConfigDigest"))
)
if mibBuilder.loadTexts:
    fsMIMstRegionConfigChangeTrap.setStatus(
        "current"
    )

fsMIMstNewPortRoleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 3, 0, 8)
)
fsMIMstNewPortRoleTrap.setObjects(
      *(("SupermicroMIMst-MIB", "fsMIMstBrgAddress"),
        ("SupermicroMIMst-MIB", "fsMIMstPortRoleType"),
        ("SupermicroMIMst-MIB", "fsMIMstOldRoleType"))
)
if mibBuilder.loadTexts:
    fsMIMstNewPortRoleTrap.setStatus(
        "current"
    )

fsMIMstCistHwFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 3, 0, 9)
)
fsMIMstCistHwFailureTrap.setObjects(
      *(("SupermicroMIMst-MIB", "fsMIMstBrgAddress"),
        ("SupermicroMIMst-MIB", "fsMIMstContextName"),
        ("SupermicroMIMst-MIB", "fsMIMstCistPortState"))
)
if mibBuilder.loadTexts:
    fsMIMstCistHwFailureTrap.setStatus(
        "current"
    )

fsMIMstMstiHwFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 118, 3, 0, 10)
)
fsMIMstMstiHwFailureTrap.setObjects(
      *(("SupermicroMIMst-MIB", "fsMIMstBrgAddress"),
        ("SupermicroMIMst-MIB", "fsMIMstContextName"),
        ("SupermicroMIMst-MIB", "fsMIMstMstiPortState"))
)
if mibBuilder.loadTexts:
    fsMIMstMstiHwFailureTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SupermicroMIMst-MIB",
    **{"VlanId": VlanId,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "EnabledStatus": EnabledStatus,
       "futureMIMstMIB": futureMIMstMIB,
       "fsMIDot1sFutureMst": fsMIDot1sFutureMst,
       "fsMIMstGlobalTrace": fsMIMstGlobalTrace,
       "fsMIMstGlobalDebug": fsMIMstGlobalDebug,
       "fsMIDot1sFutureMstTable": fsMIDot1sFutureMstTable,
       "fsMIDot1sFutureMstEntry": fsMIDot1sFutureMstEntry,
       "fsMIDot1sFutureMstContextId": fsMIDot1sFutureMstContextId,
       "fsMIMstSystemControl": fsMIMstSystemControl,
       "fsMIMstModuleStatus": fsMIMstModuleStatus,
       "fsMIMstMaxMstInstanceNumber": fsMIMstMaxMstInstanceNumber,
       "fsMIMstNoOfMstiSupported": fsMIMstNoOfMstiSupported,
       "fsMIMstMaxHopCount": fsMIMstMaxHopCount,
       "fsMIMstBrgAddress": fsMIMstBrgAddress,
       "fsMIMstCistRoot": fsMIMstCistRoot,
       "fsMIMstCistRegionalRoot": fsMIMstCistRegionalRoot,
       "fsMIMstCistRootCost": fsMIMstCistRootCost,
       "fsMIMstCistRegionalRootCost": fsMIMstCistRegionalRootCost,
       "fsMIMstCistRootPort": fsMIMstCistRootPort,
       "fsMIMstCistBridgePriority": fsMIMstCistBridgePriority,
       "fsMIMstCistBridgeMaxAge": fsMIMstCistBridgeMaxAge,
       "fsMIMstCistBridgeForwardDelay": fsMIMstCistBridgeForwardDelay,
       "fsMIMstCistHoldTime": fsMIMstCistHoldTime,
       "fsMIMstCistMaxAge": fsMIMstCistMaxAge,
       "fsMIMstCistForwardDelay": fsMIMstCistForwardDelay,
       "fsMIMstMstpUpCount": fsMIMstMstpUpCount,
       "fsMIMstMstpDownCount": fsMIMstMstpDownCount,
       "fsMIMstPathCostDefaultType": fsMIMstPathCostDefaultType,
       "fsMIMstTrace": fsMIMstTrace,
       "fsMIMstDebug": fsMIMstDebug,
       "fsMIMstForceProtocolVersion": fsMIMstForceProtocolVersion,
       "fsMIMstTxHoldCount": fsMIMstTxHoldCount,
       "fsMIMstMstiConfigIdSel": fsMIMstMstiConfigIdSel,
       "fsMIMstMstiRegionName": fsMIMstMstiRegionName,
       "fsMIMstMstiRegionVersion": fsMIMstMstiRegionVersion,
       "fsMIMstMstiConfigDigest": fsMIMstMstiConfigDigest,
       "fsMIMstBufferOverFlowCount": fsMIMstBufferOverFlowCount,
       "fsMIMstMemAllocFailureCount": fsMIMstMemAllocFailureCount,
       "fsMIMstRegionConfigChangeCount": fsMIMstRegionConfigChangeCount,
       "fsMIMstCistBridgeRoleSelectionSemState": fsMIMstCistBridgeRoleSelectionSemState,
       "fsMIMstCistTimeSinceTopologyChange": fsMIMstCistTimeSinceTopologyChange,
       "fsMIMstCistTopChanges": fsMIMstCistTopChanges,
       "fsMIMstCistNewRootBridgeCount": fsMIMstCistNewRootBridgeCount,
       "fsMIMstCistHelloTime": fsMIMstCistHelloTime,
       "fsMIMstCistBridgeHelloTime": fsMIMstCistBridgeHelloTime,
       "fsMIMstCistDynamicPathcostCalculation": fsMIMstCistDynamicPathcostCalculation,
       "fsMIMstContextName": fsMIMstContextName,
       "fsMIMstCalcPortPathCostOnSpeedChg": fsMIMstCalcPortPathCostOnSpeedChg,
       "fsMIMstClearBridgeStats": fsMIMstClearBridgeStats,
       "fsMIMstRcvdEvent": fsMIMstRcvdEvent,
       "fsMIMstRcvdEventSubType": fsMIMstRcvdEventSubType,
       "fsMIMstRcvdEventTimeStamp": fsMIMstRcvdEventTimeStamp,
       "fsMIMstPortStateChangeTimeStamp": fsMIMstPortStateChangeTimeStamp,
       "fsMIMstFlushInterval": fsMIMstFlushInterval,
       "fsMIMstCistFlushIndicationThreshold": fsMIMstCistFlushIndicationThreshold,
       "fsMIMstCistTotalFlushCount": fsMIMstCistTotalFlushCount,
       "fsMIMstBpduGuard": fsMIMstBpduGuard,
       "fsMIMstMstiBridgeTable": fsMIMstMstiBridgeTable,
       "fsMIMstMstiBridgeEntry": fsMIMstMstiBridgeEntry,
       "fsMIMstMstiInstanceIndex": fsMIMstMstiInstanceIndex,
       "fsMIMstMstiBridgeRegionalRoot": fsMIMstMstiBridgeRegionalRoot,
       "fsMIMstMstiBridgePriority": fsMIMstMstiBridgePriority,
       "fsMIMstMstiRootCost": fsMIMstMstiRootCost,
       "fsMIMstMstiRootPort": fsMIMstMstiRootPort,
       "fsMIMstMstiTimeSinceTopologyChange": fsMIMstMstiTimeSinceTopologyChange,
       "fsMIMstMstiTopChanges": fsMIMstMstiTopChanges,
       "fsMIMstMstiNewRootBridgeCount": fsMIMstMstiNewRootBridgeCount,
       "fsMIMstMstiBridgeRoleSelectionSemState": fsMIMstMstiBridgeRoleSelectionSemState,
       "fsMIMstInstanceUpCount": fsMIMstInstanceUpCount,
       "fsMIMstInstanceDownCount": fsMIMstInstanceDownCount,
       "fsMIMstOldDesignatedRoot": fsMIMstOldDesignatedRoot,
       "fsMIMstMstiClearBridgeStats": fsMIMstMstiClearBridgeStats,
       "fsMIMstMstiFlushIndicationThreshold": fsMIMstMstiFlushIndicationThreshold,
       "fsMIMstMstiTotalFlushCount": fsMIMstMstiTotalFlushCount,
       "fsMIMstVlanInstanceMappingTable": fsMIMstVlanInstanceMappingTable,
       "fsMIMstVlanInstanceMappingEntry": fsMIMstVlanInstanceMappingEntry,
       "fsMIMstInstanceIndex": fsMIMstInstanceIndex,
       "fsMIMstMapVlanIndex": fsMIMstMapVlanIndex,
       "fsMIMstUnMapVlanIndex": fsMIMstUnMapVlanIndex,
       "fsMIMstSetVlanList": fsMIMstSetVlanList,
       "fsMIMstResetVlanList": fsMIMstResetVlanList,
       "fsMIMstInstanceVlanMapped": fsMIMstInstanceVlanMapped,
       "fsMIMstInstanceVlanMapped2k": fsMIMstInstanceVlanMapped2k,
       "fsMIMstInstanceVlanMapped3k": fsMIMstInstanceVlanMapped3k,
       "fsMIMstInstanceVlanMapped4k": fsMIMstInstanceVlanMapped4k,
       "fsMIMstCistPortTable": fsMIMstCistPortTable,
       "fsMIMstCistPortEntry": fsMIMstCistPortEntry,
       "fsMIMstCistPort": fsMIMstCistPort,
       "fsMIMstCistPortPathCost": fsMIMstCistPortPathCost,
       "fsMIMstCistPortPriority": fsMIMstCistPortPriority,
       "fsMIMstCistPortDesignatedRoot": fsMIMstCistPortDesignatedRoot,
       "fsMIMstCistPortDesignatedBridge": fsMIMstCistPortDesignatedBridge,
       "fsMIMstCistPortDesignatedPort": fsMIMstCistPortDesignatedPort,
       "fsMIMstCistPortAdminP2P": fsMIMstCistPortAdminP2P,
       "fsMIMstCistPortOperP2P": fsMIMstCistPortOperP2P,
       "fsMIMstCistPortAdminEdgeStatus": fsMIMstCistPortAdminEdgeStatus,
       "fsMIMstCistPortOperEdgeStatus": fsMIMstCistPortOperEdgeStatus,
       "fsMIMstCistPortProtocolMigration": fsMIMstCistPortProtocolMigration,
       "fsMIMstCistPortState": fsMIMstCistPortState,
       "fsMIMstCistForcePortState": fsMIMstCistForcePortState,
       "fsMIMstCistPortForwardTransitions": fsMIMstCistPortForwardTransitions,
       "fsMIMstCistPortRxMstBpduCount": fsMIMstCistPortRxMstBpduCount,
       "fsMIMstCistPortRxRstBpduCount": fsMIMstCistPortRxRstBpduCount,
       "fsMIMstCistPortRxConfigBpduCount": fsMIMstCistPortRxConfigBpduCount,
       "fsMIMstCistPortRxTcnBpduCount": fsMIMstCistPortRxTcnBpduCount,
       "fsMIMstCistPortTxMstBpduCount": fsMIMstCistPortTxMstBpduCount,
       "fsMIMstCistPortTxRstBpduCount": fsMIMstCistPortTxRstBpduCount,
       "fsMIMstCistPortTxConfigBpduCount": fsMIMstCistPortTxConfigBpduCount,
       "fsMIMstCistPortTxTcnBpduCount": fsMIMstCistPortTxTcnBpduCount,
       "fsMIMstCistPortInvalidMstBpduRxCount": fsMIMstCistPortInvalidMstBpduRxCount,
       "fsMIMstCistPortInvalidRstBpduRxCount": fsMIMstCistPortInvalidRstBpduRxCount,
       "fsMIMstCistPortInvalidConfigBpduRxCount": fsMIMstCistPortInvalidConfigBpduRxCount,
       "fsMIMstCistPortInvalidTcnBpduRxCount": fsMIMstCistPortInvalidTcnBpduRxCount,
       "fsMIMstCistPortTransmitSemState": fsMIMstCistPortTransmitSemState,
       "fsMIMstCistPortReceiveSemState": fsMIMstCistPortReceiveSemState,
       "fsMIMstCistPortProtMigrationSemState": fsMIMstCistPortProtMigrationSemState,
       "fsMIMstCistProtocolMigrationCount": fsMIMstCistProtocolMigrationCount,
       "fsMIMstCistPortDesignatedCost": fsMIMstCistPortDesignatedCost,
       "fsMIMstCistPortRegionalRoot": fsMIMstCistPortRegionalRoot,
       "fsMIMstCistPortRegionalPathCost": fsMIMstCistPortRegionalPathCost,
       "fsMIMstCistSelectedPortRole": fsMIMstCistSelectedPortRole,
       "fsMIMstCistCurrentPortRole": fsMIMstCistCurrentPortRole,
       "fsMIMstCistPortInfoSemState": fsMIMstCistPortInfoSemState,
       "fsMIMstCistPortRoleTransitionSemState": fsMIMstCistPortRoleTransitionSemState,
       "fsMIMstCistPortStateTransitionSemState": fsMIMstCistPortStateTransitionSemState,
       "fsMIMstCistPortTopologyChangeSemState": fsMIMstCistPortTopologyChangeSemState,
       "fsMIMstCistPortHelloTime": fsMIMstCistPortHelloTime,
       "fsMIMstCistPortOperVersion": fsMIMstCistPortOperVersion,
       "fsMIMstCistPortEffectivePortState": fsMIMstCistPortEffectivePortState,
       "fsMIMstCistPortAutoEdgeStatus": fsMIMstCistPortAutoEdgeStatus,
       "fsMIMstCistPortRestrictedRole": fsMIMstCistPortRestrictedRole,
       "fsMIMstCistPortRestrictedTCN": fsMIMstCistPortRestrictedTCN,
       "fsMIMstCistPortAdminPathCost": fsMIMstCistPortAdminPathCost,
       "fsMIMstCistPortEnableBPDURx": fsMIMstCistPortEnableBPDURx,
       "fsMIMstCistPortEnableBPDUTx": fsMIMstCistPortEnableBPDUTx,
       "fsMIMstCistPortPseudoRootId": fsMIMstCistPortPseudoRootId,
       "fsMIMstCistPortIsL2Gp": fsMIMstCistPortIsL2Gp,
       "fsMIMstCistPortLoopGuard": fsMIMstCistPortLoopGuard,
       "fsMIMstCistPortClearStats": fsMIMstCistPortClearStats,
       "fsMIMstCistPortRcvdEvent": fsMIMstCistPortRcvdEvent,
       "fsMIMstCistPortRcvdEventSubType": fsMIMstCistPortRcvdEventSubType,
       "fsMIMstCistPortRcvdEventTimeStamp": fsMIMstCistPortRcvdEventTimeStamp,
       "fsMIMstCistLoopInconsistentState": fsMIMstCistLoopInconsistentState,
       "fsMIMstCistPortBpduGuard": fsMIMstCistPortBpduGuard,
       "fsMIMstMstiPortTable": fsMIMstMstiPortTable,
       "fsMIMstMstiPortEntry": fsMIMstMstiPortEntry,
       "fsMIMstMstiPort": fsMIMstMstiPort,
       "fsMIMstMstiPortPathCost": fsMIMstMstiPortPathCost,
       "fsMIMstMstiPortPriority": fsMIMstMstiPortPriority,
       "fsMIMstMstiPortDesignatedRoot": fsMIMstMstiPortDesignatedRoot,
       "fsMIMstMstiPortDesignatedBridge": fsMIMstMstiPortDesignatedBridge,
       "fsMIMstMstiPortDesignatedPort": fsMIMstMstiPortDesignatedPort,
       "fsMIMstMstiPortState": fsMIMstMstiPortState,
       "fsMIMstMstiForcePortState": fsMIMstMstiForcePortState,
       "fsMIMstMstiPortForwardTransitions": fsMIMstMstiPortForwardTransitions,
       "fsMIMstMstiPortReceivedBPDUs": fsMIMstMstiPortReceivedBPDUs,
       "fsMIMstMstiPortTransmittedBPDUs": fsMIMstMstiPortTransmittedBPDUs,
       "fsMIMstMstiPortInvalidBPDUsRcvd": fsMIMstMstiPortInvalidBPDUsRcvd,
       "fsMIMstMstiPortDesignatedCost": fsMIMstMstiPortDesignatedCost,
       "fsMIMstMstiSelectedPortRole": fsMIMstMstiSelectedPortRole,
       "fsMIMstMstiCurrentPortRole": fsMIMstMstiCurrentPortRole,
       "fsMIMstMstiPortInfoSemState": fsMIMstMstiPortInfoSemState,
       "fsMIMstMstiPortRoleTransitionSemState": fsMIMstMstiPortRoleTransitionSemState,
       "fsMIMstMstiPortStateTransitionSemState": fsMIMstMstiPortStateTransitionSemState,
       "fsMIMstMstiPortTopologyChangeSemState": fsMIMstMstiPortTopologyChangeSemState,
       "fsMIMstMstiPortEffectivePortState": fsMIMstMstiPortEffectivePortState,
       "fsMIMstMstiPortAdminPathCost": fsMIMstMstiPortAdminPathCost,
       "fsMIMstMstiPortPseudoRootId": fsMIMstMstiPortPseudoRootId,
       "fsMIMstMstiPortClearStats": fsMIMstMstiPortClearStats,
       "fsMIMstMstiPortStateChangeTimeStamp": fsMIMstMstiPortStateChangeTimeStamp,
       "fsMIMstPortExtTable": fsMIMstPortExtTable,
       "fsMIMstPortExtEntry": fsMIMstPortExtEntry,
       "fsMIMstPort": fsMIMstPort,
       "fsMIMstPortRowStatus": fsMIMstPortRowStatus,
       "fsMIDot1sFsMstTrapsControl": fsMIDot1sFsMstTrapsControl,
       "fsMIDot1sFsMstSetGlobalTrapOption": fsMIDot1sFsMstSetGlobalTrapOption,
       "fsMIMstGlobalErrTrapType": fsMIMstGlobalErrTrapType,
       "fsMIDot1sFsMstTrapsControlTable": fsMIDot1sFsMstTrapsControlTable,
       "fsMIDot1sFsMstTrapsControlEntry": fsMIDot1sFsMstTrapsControlEntry,
       "fsMIMstSetTraps": fsMIMstSetTraps,
       "fsMIMstGenTrapType": fsMIMstGenTrapType,
       "fsMIMstPortTrapNotificationTable": fsMIMstPortTrapNotificationTable,
       "fsMIMstPortTrapNotificationEntry": fsMIMstPortTrapNotificationEntry,
       "fsMIMstPortTrapIndex": fsMIMstPortTrapIndex,
       "fsMIMstPortMigrationType": fsMIMstPortMigrationType,
       "fsMIMstPktErrType": fsMIMstPktErrType,
       "fsMIMstPktErrVal": fsMIMstPktErrVal,
       "fsMIMstPortRoleTrapNotificationTable": fsMIMstPortRoleTrapNotificationTable,
       "fsMIMstPortRoleTrapNotificationEntry": fsMIMstPortRoleTrapNotificationEntry,
       "fsMIMstPortRoleType": fsMIMstPortRoleType,
       "fsMIMstOldRoleType": fsMIMstOldRoleType,
       "fsMIDot1sFutureMstTraps": fsMIDot1sFutureMstTraps,
       "fsMIMstTraps": fsMIMstTraps,
       "fsMIMstGlobalErrTrap": fsMIMstGlobalErrTrap,
       "fsMIMstGenTrap": fsMIMstGenTrap,
       "fsMIMstNewRootTrap": fsMIMstNewRootTrap,
       "fsMIMstTopologyChgTrap": fsMIMstTopologyChgTrap,
       "fsMIMstProtocolMigrationTrap": fsMIMstProtocolMigrationTrap,
       "fsMIMstInvalidBpduRxdTrap": fsMIMstInvalidBpduRxdTrap,
       "fsMIMstRegionConfigChangeTrap": fsMIMstRegionConfigChangeTrap,
       "fsMIMstNewPortRoleTrap": fsMIMstNewPortRoleTrap,
       "fsMIMstCistHwFailureTrap": fsMIMstCistHwFailureTrap,
       "fsMIMstMstiHwFailureTrap": fsMIMstMstiHwFailureTrap}
)
