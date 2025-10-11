# SNMP MIB module (SUPERMICRO-PVRST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-PVRST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:04:10 2025
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

futurePvrstMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161)
)
if mibBuilder.loadTexts:
    futurePvrstMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



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

_FsFuturePvrst_ObjectIdentity = ObjectIdentity
fsFuturePvrst = _FsFuturePvrst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1)
)


class _FsPvrstSystemControl_Type(Integer32):
    """Custom type fsPvrstSystemControl based on Integer32"""
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


_FsPvrstSystemControl_Type.__name__ = "Integer32"
_FsPvrstSystemControl_Object = MibScalar
fsPvrstSystemControl = _FsPvrstSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 1),
    _FsPvrstSystemControl_Type()
)
fsPvrstSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPvrstSystemControl.setStatus("current")
_FsPvrstModuleStatus_Type = EnabledStatus
_FsPvrstModuleStatus_Object = MibScalar
fsPvrstModuleStatus = _FsPvrstModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 2),
    _FsPvrstModuleStatus_Type()
)
fsPvrstModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPvrstModuleStatus.setStatus("current")
_FsPvrstNoOfActiveInstances_Type = Integer32
_FsPvrstNoOfActiveInstances_Object = MibScalar
fsPvrstNoOfActiveInstances = _FsPvrstNoOfActiveInstances_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 3),
    _FsPvrstNoOfActiveInstances_Type()
)
fsPvrstNoOfActiveInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstNoOfActiveInstances.setStatus("current")
_FsPvrstBrgAddress_Type = MacAddress
_FsPvrstBrgAddress_Object = MibScalar
fsPvrstBrgAddress = _FsPvrstBrgAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 4),
    _FsPvrstBrgAddress_Type()
)
fsPvrstBrgAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstBrgAddress.setStatus("current")
_FsPvrstUpCount_Type = Counter32
_FsPvrstUpCount_Object = MibScalar
fsPvrstUpCount = _FsPvrstUpCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 5),
    _FsPvrstUpCount_Type()
)
fsPvrstUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstUpCount.setStatus("current")
_FsPvrstDownCount_Type = Counter32
_FsPvrstDownCount_Object = MibScalar
fsPvrstDownCount = _FsPvrstDownCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 6),
    _FsPvrstDownCount_Type()
)
fsPvrstDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstDownCount.setStatus("current")


class _FsPvrstPathCostDefaultType_Type(Integer32):
    """Custom type fsPvrstPathCostDefaultType based on Integer32"""
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


_FsPvrstPathCostDefaultType_Type.__name__ = "Integer32"
_FsPvrstPathCostDefaultType_Object = MibScalar
fsPvrstPathCostDefaultType = _FsPvrstPathCostDefaultType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 7),
    _FsPvrstPathCostDefaultType_Type()
)
fsPvrstPathCostDefaultType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPvrstPathCostDefaultType.setStatus("obsolete")


class _FsPvrstDynamicPathCostCalculation_Type(TruthValue):
    """Custom type fsPvrstDynamicPathCostCalculation based on TruthValue"""
    defaultValue = 2


_FsPvrstDynamicPathCostCalculation_Type.__name__ = "TruthValue"
_FsPvrstDynamicPathCostCalculation_Object = MibScalar
fsPvrstDynamicPathCostCalculation = _FsPvrstDynamicPathCostCalculation_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 8),
    _FsPvrstDynamicPathCostCalculation_Type()
)
fsPvrstDynamicPathCostCalculation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPvrstDynamicPathCostCalculation.setStatus("current")


class _FsPvrstTrace_Type(Integer32):
    """Custom type fsPvrstTrace based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPvrstTrace_Type.__name__ = "Integer32"
_FsPvrstTrace_Object = MibScalar
fsPvrstTrace = _FsPvrstTrace_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 9),
    _FsPvrstTrace_Type()
)
fsPvrstTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPvrstTrace.setStatus("current")


class _FsPvrstDebug_Type(Integer32):
    """Custom type fsPvrstDebug based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 524287),
    )


_FsPvrstDebug_Type.__name__ = "Integer32"
_FsPvrstDebug_Object = MibScalar
fsPvrstDebug = _FsPvrstDebug_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 10),
    _FsPvrstDebug_Type()
)
fsPvrstDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPvrstDebug.setStatus("current")
_FsPvrstBufferOverFlowCount_Type = Counter32
_FsPvrstBufferOverFlowCount_Object = MibScalar
fsPvrstBufferOverFlowCount = _FsPvrstBufferOverFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 11),
    _FsPvrstBufferOverFlowCount_Type()
)
fsPvrstBufferOverFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstBufferOverFlowCount.setStatus("current")
_FsPvrstMemAllocFailureCount_Type = Counter32
_FsPvrstMemAllocFailureCount_Object = MibScalar
fsPvrstMemAllocFailureCount = _FsPvrstMemAllocFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 12),
    _FsPvrstMemAllocFailureCount_Type()
)
fsPvrstMemAllocFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstMemAllocFailureCount.setStatus("current")
_FsFuturePvrstPortTable_Object = MibTable
fsFuturePvrstPortTable = _FsFuturePvrstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 13)
)
if mibBuilder.loadTexts:
    fsFuturePvrstPortTable.setStatus("current")
_FsFuturePvrstPortEntry_Object = MibTableRow
fsFuturePvrstPortEntry = _FsFuturePvrstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 13, 1)
)
fsFuturePvrstPortEntry.setIndexNames(
    (0, "SUPERMICRO-PVRST-MIB", "fsPvrstPort"),
)
if mibBuilder.loadTexts:
    fsFuturePvrstPortEntry.setStatus("current")


class _FsPvrstPort_Type(Integer32):
    """Custom type fsPvrstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsPvrstPort_Type.__name__ = "Integer32"
_FsPvrstPort_Object = MibTableColumn
fsPvrstPort = _FsPvrstPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 13, 1, 1),
    _FsPvrstPort_Type()
)
fsPvrstPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPvrstPort.setStatus("current")
_FsPvrstPortAdminEdgeStatus_Type = TruthValue
_FsPvrstPortAdminEdgeStatus_Object = MibTableColumn
fsPvrstPortAdminEdgeStatus = _FsPvrstPortAdminEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 13, 1, 2),
    _FsPvrstPortAdminEdgeStatus_Type()
)
fsPvrstPortAdminEdgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPvrstPortAdminEdgeStatus.setStatus("current")
_FsPvrstPortOperEdgePortStatus_Type = TruthValue
_FsPvrstPortOperEdgePortStatus_Object = MibTableColumn
fsPvrstPortOperEdgePortStatus = _FsPvrstPortOperEdgePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 13, 1, 3),
    _FsPvrstPortOperEdgePortStatus_Type()
)
fsPvrstPortOperEdgePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstPortOperEdgePortStatus.setStatus("current")


class _FsPvrstBridgeDetectionSemState_Type(Integer32):
    """Custom type fsPvrstBridgeDetectionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("edge", 0),
          ("notedge", 1))
    )


_FsPvrstBridgeDetectionSemState_Type.__name__ = "Integer32"
_FsPvrstBridgeDetectionSemState_Object = MibTableColumn
fsPvrstBridgeDetectionSemState = _FsPvrstBridgeDetectionSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 13, 1, 4),
    _FsPvrstBridgeDetectionSemState_Type()
)
fsPvrstBridgeDetectionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstBridgeDetectionSemState.setStatus("current")
_FsPvrstPortEnabledStatus_Type = TruthValue
_FsPvrstPortEnabledStatus_Object = MibTableColumn
fsPvrstPortEnabledStatus = _FsPvrstPortEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 13, 1, 5),
    _FsPvrstPortEnabledStatus_Type()
)
fsPvrstPortEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPvrstPortEnabledStatus.setStatus("current")
_FsPvrstRootGuard_Type = TruthValue
_FsPvrstRootGuard_Object = MibTableColumn
fsPvrstRootGuard = _FsPvrstRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 13, 1, 6),
    _FsPvrstRootGuard_Type()
)
fsPvrstRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPvrstRootGuard.setStatus("current")


class _FsPvrstBpduGuard_Type(Integer32):
    """Custom type fsPvrstBpduGuard based on Integer32"""
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


_FsPvrstBpduGuard_Type.__name__ = "Integer32"
_FsPvrstBpduGuard_Object = MibTableColumn
fsPvrstBpduGuard = _FsPvrstBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 13, 1, 7),
    _FsPvrstBpduGuard_Type()
)
fsPvrstBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPvrstBpduGuard.setStatus("current")


class _FsPvrstEncapType_Type(Integer32):
    """Custom type fsPvrstEncapType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dot1Q", 0),
          ("isl", 1))
    )


_FsPvrstEncapType_Type.__name__ = "Integer32"
_FsPvrstEncapType_Object = MibTableColumn
fsPvrstEncapType = _FsPvrstEncapType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 13, 1, 8),
    _FsPvrstEncapType_Type()
)
fsPvrstEncapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPvrstEncapType.setStatus("current")


class _FsPvrstPortAdminPointToPoint_Type(Integer32):
    """Custom type fsPvrstPortAdminPointToPoint based on Integer32"""
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


_FsPvrstPortAdminPointToPoint_Type.__name__ = "Integer32"
_FsPvrstPortAdminPointToPoint_Object = MibTableColumn
fsPvrstPortAdminPointToPoint = _FsPvrstPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 13, 1, 9),
    _FsPvrstPortAdminPointToPoint_Type()
)
fsPvrstPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPvrstPortAdminPointToPoint.setStatus("current")
_FsPvrstPortOperPointToPoint_Type = TruthValue
_FsPvrstPortOperPointToPoint_Object = MibTableColumn
fsPvrstPortOperPointToPoint = _FsPvrstPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 13, 1, 10),
    _FsPvrstPortOperPointToPoint_Type()
)
fsPvrstPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstPortOperPointToPoint.setStatus("current")
_FsPvrstPortInvalidBpdusRcvd_Type = Counter32
_FsPvrstPortInvalidBpdusRcvd_Object = MibTableColumn
fsPvrstPortInvalidBpdusRcvd = _FsPvrstPortInvalidBpdusRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 13, 1, 11),
    _FsPvrstPortInvalidBpdusRcvd_Type()
)
fsPvrstPortInvalidBpdusRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstPortInvalidBpdusRcvd.setStatus("current")
_FsPvrstPortInvalidConfigBpduRxCount_Type = Counter32
_FsPvrstPortInvalidConfigBpduRxCount_Object = MibTableColumn
fsPvrstPortInvalidConfigBpduRxCount = _FsPvrstPortInvalidConfigBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 13, 1, 12),
    _FsPvrstPortInvalidConfigBpduRxCount_Type()
)
fsPvrstPortInvalidConfigBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstPortInvalidConfigBpduRxCount.setStatus("current")
_FsPvrstPortInvalidTcnBpduRxCount_Type = Counter32
_FsPvrstPortInvalidTcnBpduRxCount_Object = MibTableColumn
fsPvrstPortInvalidTcnBpduRxCount = _FsPvrstPortInvalidTcnBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 13, 1, 13),
    _FsPvrstPortInvalidTcnBpduRxCount_Type()
)
fsPvrstPortInvalidTcnBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstPortInvalidTcnBpduRxCount.setStatus("current")
_FsPvrstPortRowStatus_Type = RowStatus
_FsPvrstPortRowStatus_Object = MibTableColumn
fsPvrstPortRowStatus = _FsPvrstPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 13, 1, 14),
    _FsPvrstPortRowStatus_Type()
)
fsPvrstPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPvrstPortRowStatus.setStatus("current")
_FsPvrstInstBridgeTable_Object = MibTable
fsPvrstInstBridgeTable = _FsPvrstInstBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 14)
)
if mibBuilder.loadTexts:
    fsPvrstInstBridgeTable.setStatus("current")
_FsPvrstInstBridgeEntry_Object = MibTableRow
fsPvrstInstBridgeEntry = _FsPvrstInstBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 14, 1)
)
fsPvrstInstBridgeEntry.setIndexNames(
    (0, "SUPERMICRO-PVRST-MIB", "fsPvrstInstVlanId"),
)
if mibBuilder.loadTexts:
    fsPvrstInstBridgeEntry.setStatus("current")


class _FsPvrstInstVlanId_Type(Integer32):
    """Custom type fsPvrstInstVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsPvrstInstVlanId_Type.__name__ = "Integer32"
_FsPvrstInstVlanId_Object = MibTableColumn
fsPvrstInstVlanId = _FsPvrstInstVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 14, 1, 1),
    _FsPvrstInstVlanId_Type()
)
fsPvrstInstVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPvrstInstVlanId.setStatus("current")


class _FsPvrstInstBridgePriority_Type(Integer32):
    """Custom type fsPvrstInstBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_FsPvrstInstBridgePriority_Type.__name__ = "Integer32"
_FsPvrstInstBridgePriority_Object = MibTableColumn
fsPvrstInstBridgePriority = _FsPvrstInstBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 14, 1, 2),
    _FsPvrstInstBridgePriority_Type()
)
fsPvrstInstBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPvrstInstBridgePriority.setStatus("current")
_FsPvrstInstRootCost_Type = Integer32
_FsPvrstInstRootCost_Object = MibTableColumn
fsPvrstInstRootCost = _FsPvrstInstRootCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 14, 1, 3),
    _FsPvrstInstRootCost_Type()
)
fsPvrstInstRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstRootCost.setStatus("current")
_FsPvrstInstRootPort_Type = Integer32
_FsPvrstInstRootPort_Object = MibTableColumn
fsPvrstInstRootPort = _FsPvrstInstRootPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 14, 1, 4),
    _FsPvrstInstRootPort_Type()
)
fsPvrstInstRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstRootPort.setStatus("current")
_FsPvrstInstBridgeMaxAge_Type = Timeout
_FsPvrstInstBridgeMaxAge_Object = MibTableColumn
fsPvrstInstBridgeMaxAge = _FsPvrstInstBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 14, 1, 5),
    _FsPvrstInstBridgeMaxAge_Type()
)
fsPvrstInstBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPvrstInstBridgeMaxAge.setStatus("current")
_FsPvrstInstBridgeHelloTime_Type = Timeout
_FsPvrstInstBridgeHelloTime_Object = MibTableColumn
fsPvrstInstBridgeHelloTime = _FsPvrstInstBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 14, 1, 6),
    _FsPvrstInstBridgeHelloTime_Type()
)
fsPvrstInstBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPvrstInstBridgeHelloTime.setStatus("current")
_FsPvrstInstBridgeForwardDelay_Type = Timeout
_FsPvrstInstBridgeForwardDelay_Object = MibTableColumn
fsPvrstInstBridgeForwardDelay = _FsPvrstInstBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 14, 1, 7),
    _FsPvrstInstBridgeForwardDelay_Type()
)
fsPvrstInstBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPvrstInstBridgeForwardDelay.setStatus("current")
_FsPvrstInstHoldTime_Type = Integer32
_FsPvrstInstHoldTime_Object = MibTableColumn
fsPvrstInstHoldTime = _FsPvrstInstHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 14, 1, 8),
    _FsPvrstInstHoldTime_Type()
)
fsPvrstInstHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstHoldTime.setStatus("current")


class _FsPvrstInstTxHoldCount_Type(Integer32):
    """Custom type fsPvrstInstTxHoldCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsPvrstInstTxHoldCount_Type.__name__ = "Integer32"
_FsPvrstInstTxHoldCount_Object = MibTableColumn
fsPvrstInstTxHoldCount = _FsPvrstInstTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 14, 1, 9),
    _FsPvrstInstTxHoldCount_Type()
)
fsPvrstInstTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPvrstInstTxHoldCount.setStatus("current")
_FsPvrstInstTimeSinceTopologyChange_Type = TimeTicks
_FsPvrstInstTimeSinceTopologyChange_Object = MibTableColumn
fsPvrstInstTimeSinceTopologyChange = _FsPvrstInstTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 14, 1, 10),
    _FsPvrstInstTimeSinceTopologyChange_Type()
)
fsPvrstInstTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstTimeSinceTopologyChange.setStatus("current")
_FsPvrstInstTopChanges_Type = Counter32
_FsPvrstInstTopChanges_Object = MibTableColumn
fsPvrstInstTopChanges = _FsPvrstInstTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 14, 1, 11),
    _FsPvrstInstTopChanges_Type()
)
fsPvrstInstTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstTopChanges.setStatus("current")
_FsPvrstInstNewRootCount_Type = Counter32
_FsPvrstInstNewRootCount_Object = MibTableColumn
fsPvrstInstNewRootCount = _FsPvrstInstNewRootCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 14, 1, 12),
    _FsPvrstInstNewRootCount_Type()
)
fsPvrstInstNewRootCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstNewRootCount.setStatus("current")
_FsPvrstInstInstanceUpCount_Type = Counter32
_FsPvrstInstInstanceUpCount_Object = MibTableColumn
fsPvrstInstInstanceUpCount = _FsPvrstInstInstanceUpCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 14, 1, 13),
    _FsPvrstInstInstanceUpCount_Type()
)
fsPvrstInstInstanceUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstInstanceUpCount.setStatus("current")
_FsPvrstInstInstanceDownCount_Type = Counter32
_FsPvrstInstInstanceDownCount_Object = MibTableColumn
fsPvrstInstInstanceDownCount = _FsPvrstInstInstanceDownCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 14, 1, 14),
    _FsPvrstInstInstanceDownCount_Type()
)
fsPvrstInstInstanceDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstInstanceDownCount.setStatus("current")


class _FsPvrstInstPortRoleSelSemState_Type(Integer32):
    """Custom type fsPvrstInstPortRoleSelSemState based on Integer32"""
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


_FsPvrstInstPortRoleSelSemState_Type.__name__ = "Integer32"
_FsPvrstInstPortRoleSelSemState_Object = MibTableColumn
fsPvrstInstPortRoleSelSemState = _FsPvrstInstPortRoleSelSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 14, 1, 15),
    _FsPvrstInstPortRoleSelSemState_Type()
)
fsPvrstInstPortRoleSelSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortRoleSelSemState.setStatus("current")
_FsPvrstInstDesignatedRoot_Type = BridgeId
_FsPvrstInstDesignatedRoot_Object = MibTableColumn
fsPvrstInstDesignatedRoot = _FsPvrstInstDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 14, 1, 16),
    _FsPvrstInstDesignatedRoot_Type()
)
fsPvrstInstDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstDesignatedRoot.setStatus("current")
_FsPvrstInstRootMaxAge_Type = Timeout
_FsPvrstInstRootMaxAge_Object = MibTableColumn
fsPvrstInstRootMaxAge = _FsPvrstInstRootMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 14, 1, 17),
    _FsPvrstInstRootMaxAge_Type()
)
fsPvrstInstRootMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstRootMaxAge.setStatus("current")
_FsPvrstInstRootHelloTime_Type = Timeout
_FsPvrstInstRootHelloTime_Object = MibTableColumn
fsPvrstInstRootHelloTime = _FsPvrstInstRootHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 14, 1, 18),
    _FsPvrstInstRootHelloTime_Type()
)
fsPvrstInstRootHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstRootHelloTime.setStatus("current")
_FsPvrstInstRootForwardDelay_Type = Timeout
_FsPvrstInstRootForwardDelay_Object = MibTableColumn
fsPvrstInstRootForwardDelay = _FsPvrstInstRootForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 14, 1, 19),
    _FsPvrstInstRootForwardDelay_Type()
)
fsPvrstInstRootForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstRootForwardDelay.setStatus("current")
_FsPvrstInstPortTable_Object = MibTable
fsPvrstInstPortTable = _FsPvrstInstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15)
)
if mibBuilder.loadTexts:
    fsPvrstInstPortTable.setStatus("current")
_FsPvrstInstPortEntry_Object = MibTableRow
fsPvrstInstPortEntry = _FsPvrstInstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1)
)
fsPvrstInstPortEntry.setIndexNames(
    (0, "SUPERMICRO-PVRST-MIB", "fsPvrstInstVlanId"),
    (0, "SUPERMICRO-PVRST-MIB", "fsPvrstInstPortIndex"),
)
if mibBuilder.loadTexts:
    fsPvrstInstPortEntry.setStatus("current")


class _FsPvrstInstPortIndex_Type(Integer32):
    """Custom type fsPvrstInstPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsPvrstInstPortIndex_Type.__name__ = "Integer32"
_FsPvrstInstPortIndex_Object = MibTableColumn
fsPvrstInstPortIndex = _FsPvrstInstPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 1),
    _FsPvrstInstPortIndex_Type()
)
fsPvrstInstPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPvrstInstPortIndex.setStatus("current")


class _FsPvrstInstPortEnableStatus_Type(Integer32):
    """Custom type fsPvrstInstPortEnableStatus based on Integer32"""
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


_FsPvrstInstPortEnableStatus_Type.__name__ = "Integer32"
_FsPvrstInstPortEnableStatus_Object = MibTableColumn
fsPvrstInstPortEnableStatus = _FsPvrstInstPortEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 2),
    _FsPvrstInstPortEnableStatus_Type()
)
fsPvrstInstPortEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPvrstInstPortEnableStatus.setStatus("current")


class _FsPvrstInstPortPathCost_Type(Integer32):
    """Custom type fsPvrstInstPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_FsPvrstInstPortPathCost_Type.__name__ = "Integer32"
_FsPvrstInstPortPathCost_Object = MibTableColumn
fsPvrstInstPortPathCost = _FsPvrstInstPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 3),
    _FsPvrstInstPortPathCost_Type()
)
fsPvrstInstPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPvrstInstPortPathCost.setStatus("current")


class _FsPvrstInstPortPriority_Type(Integer32):
    """Custom type fsPvrstInstPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_FsPvrstInstPortPriority_Type.__name__ = "Integer32"
_FsPvrstInstPortPriority_Object = MibTableColumn
fsPvrstInstPortPriority = _FsPvrstInstPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 4),
    _FsPvrstInstPortPriority_Type()
)
fsPvrstInstPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPvrstInstPortPriority.setStatus("current")
_FsPvrstInstPortDesignatedRoot_Type = BridgeId
_FsPvrstInstPortDesignatedRoot_Object = MibTableColumn
fsPvrstInstPortDesignatedRoot = _FsPvrstInstPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 5),
    _FsPvrstInstPortDesignatedRoot_Type()
)
fsPvrstInstPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortDesignatedRoot.setStatus("current")
_FsPvrstInstPortDesignatedBridge_Type = BridgeId
_FsPvrstInstPortDesignatedBridge_Object = MibTableColumn
fsPvrstInstPortDesignatedBridge = _FsPvrstInstPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 6),
    _FsPvrstInstPortDesignatedBridge_Type()
)
fsPvrstInstPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortDesignatedBridge.setStatus("current")


class _FsPvrstInstPortDesignatedPort_Type(OctetString):
    """Custom type fsPvrstInstPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_FsPvrstInstPortDesignatedPort_Type.__name__ = "OctetString"
_FsPvrstInstPortDesignatedPort_Object = MibTableColumn
fsPvrstInstPortDesignatedPort = _FsPvrstInstPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 7),
    _FsPvrstInstPortDesignatedPort_Type()
)
fsPvrstInstPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortDesignatedPort.setStatus("current")


class _FsPvrstInstPortOperVersion_Type(Integer32):
    """Custom type fsPvrstInstPortOperVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stpCompatible", 0),
          ("rstp", 2))
    )


_FsPvrstInstPortOperVersion_Type.__name__ = "Integer32"
_FsPvrstInstPortOperVersion_Object = MibTableColumn
fsPvrstInstPortOperVersion = _FsPvrstInstPortOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 8),
    _FsPvrstInstPortOperVersion_Type()
)
fsPvrstInstPortOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortOperVersion.setStatus("current")
_FsPvrstInstPortProtocolMigration_Type = TruthValue
_FsPvrstInstPortProtocolMigration_Object = MibTableColumn
fsPvrstInstPortProtocolMigration = _FsPvrstInstPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 9),
    _FsPvrstInstPortProtocolMigration_Type()
)
fsPvrstInstPortProtocolMigration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortProtocolMigration.setStatus("current")


class _FsPvrstInstPortState_Type(Integer32):
    """Custom type fsPvrstInstPortState based on Integer32"""
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


_FsPvrstInstPortState_Type.__name__ = "Integer32"
_FsPvrstInstPortState_Object = MibTableColumn
fsPvrstInstPortState = _FsPvrstInstPortState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 10),
    _FsPvrstInstPortState_Type()
)
fsPvrstInstPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortState.setStatus("current")
_FsPvrstInstPortForwardTransitions_Type = Counter32
_FsPvrstInstPortForwardTransitions_Object = MibTableColumn
fsPvrstInstPortForwardTransitions = _FsPvrstInstPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 11),
    _FsPvrstInstPortForwardTransitions_Type()
)
fsPvrstInstPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortForwardTransitions.setStatus("current")
_FsPvrstInstPortReceivedBpdus_Type = Counter32
_FsPvrstInstPortReceivedBpdus_Object = MibTableColumn
fsPvrstInstPortReceivedBpdus = _FsPvrstInstPortReceivedBpdus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 12),
    _FsPvrstInstPortReceivedBpdus_Type()
)
fsPvrstInstPortReceivedBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortReceivedBpdus.setStatus("current")
_FsPvrstInstPortRxConfigBpduCount_Type = Counter32
_FsPvrstInstPortRxConfigBpduCount_Object = MibTableColumn
fsPvrstInstPortRxConfigBpduCount = _FsPvrstInstPortRxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 13),
    _FsPvrstInstPortRxConfigBpduCount_Type()
)
fsPvrstInstPortRxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortRxConfigBpduCount.setStatus("current")
_FsPvrstInstPortRxTcnBpduCount_Type = Counter32
_FsPvrstInstPortRxTcnBpduCount_Object = MibTableColumn
fsPvrstInstPortRxTcnBpduCount = _FsPvrstInstPortRxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 14),
    _FsPvrstInstPortRxTcnBpduCount_Type()
)
fsPvrstInstPortRxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortRxTcnBpduCount.setStatus("current")
_FsPvrstInstPortTransmittedBpdus_Type = Counter32
_FsPvrstInstPortTransmittedBpdus_Object = MibTableColumn
fsPvrstInstPortTransmittedBpdus = _FsPvrstInstPortTransmittedBpdus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 15),
    _FsPvrstInstPortTransmittedBpdus_Type()
)
fsPvrstInstPortTransmittedBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortTransmittedBpdus.setStatus("current")
_FsPvrstInstPortTxConfigBpduCount_Type = Counter32
_FsPvrstInstPortTxConfigBpduCount_Object = MibTableColumn
fsPvrstInstPortTxConfigBpduCount = _FsPvrstInstPortTxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 16),
    _FsPvrstInstPortTxConfigBpduCount_Type()
)
fsPvrstInstPortTxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortTxConfigBpduCount.setStatus("current")
_FsPvrstInstPortTxTcnBpduCount_Type = Counter32
_FsPvrstInstPortTxTcnBpduCount_Object = MibTableColumn
fsPvrstInstPortTxTcnBpduCount = _FsPvrstInstPortTxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 17),
    _FsPvrstInstPortTxTcnBpduCount_Type()
)
fsPvrstInstPortTxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortTxTcnBpduCount.setStatus("current")


class _FsPvrstInstPortTxSemState_Type(Integer32):
    """Custom type fsPvrstInstPortTxSemState based on Integer32"""
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


_FsPvrstInstPortTxSemState_Type.__name__ = "Integer32"
_FsPvrstInstPortTxSemState_Object = MibTableColumn
fsPvrstInstPortTxSemState = _FsPvrstInstPortTxSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 18),
    _FsPvrstInstPortTxSemState_Type()
)
fsPvrstInstPortTxSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortTxSemState.setStatus("current")


class _FsPvrstInstPortProtMigrationSemState_Type(Integer32):
    """Custom type fsPvrstInstPortProtMigrationSemState based on Integer32"""
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


_FsPvrstInstPortProtMigrationSemState_Type.__name__ = "Integer32"
_FsPvrstInstPortProtMigrationSemState_Object = MibTableColumn
fsPvrstInstPortProtMigrationSemState = _FsPvrstInstPortProtMigrationSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 19),
    _FsPvrstInstPortProtMigrationSemState_Type()
)
fsPvrstInstPortProtMigrationSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortProtMigrationSemState.setStatus("current")
_FsPvrstInstProtocolMigrationCount_Type = Counter32
_FsPvrstInstProtocolMigrationCount_Object = MibTableColumn
fsPvrstInstProtocolMigrationCount = _FsPvrstInstProtocolMigrationCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 20),
    _FsPvrstInstProtocolMigrationCount_Type()
)
fsPvrstInstProtocolMigrationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstProtocolMigrationCount.setStatus("current")


class _FsPvrstInstPortRole_Type(Integer32):
    """Custom type fsPvrstInstPortRole based on Integer32"""
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


_FsPvrstInstPortRole_Type.__name__ = "Integer32"
_FsPvrstInstPortRole_Object = MibTableColumn
fsPvrstInstPortRole = _FsPvrstInstPortRole_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 21),
    _FsPvrstInstPortRole_Type()
)
fsPvrstInstPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortRole.setStatus("current")


class _FsPvrstInstCurrentPortRole_Type(Integer32):
    """Custom type fsPvrstInstCurrentPortRole based on Integer32"""
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


_FsPvrstInstCurrentPortRole_Type.__name__ = "Integer32"
_FsPvrstInstCurrentPortRole_Object = MibTableColumn
fsPvrstInstCurrentPortRole = _FsPvrstInstCurrentPortRole_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 22),
    _FsPvrstInstCurrentPortRole_Type()
)
fsPvrstInstCurrentPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstCurrentPortRole.setStatus("current")


class _FsPvrstInstPortInfoSemState_Type(Integer32):
    """Custom type fsPvrstInstPortInfoSemState based on Integer32"""
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
        *(("disabled", 0),
          ("aged", 1),
          ("update", 2),
          ("superior", 3),
          ("repeat", 4),
          ("agreement", 5),
          ("present", 6),
          ("receive", 7))
    )


_FsPvrstInstPortInfoSemState_Type.__name__ = "Integer32"
_FsPvrstInstPortInfoSemState_Object = MibTableColumn
fsPvrstInstPortInfoSemState = _FsPvrstInstPortInfoSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 23),
    _FsPvrstInstPortInfoSemState_Type()
)
fsPvrstInstPortInfoSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortInfoSemState.setStatus("current")


class _FsPvrstInstPortRoleTransitionSemState_Type(Integer32):
    """Custom type fsPvrstInstPortRoleTransitionSemState based on Integer32"""
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
          ("blockport", 1),
          ("blockedport", 2),
          ("rootport", 3),
          ("designatedport", 4))
    )


_FsPvrstInstPortRoleTransitionSemState_Type.__name__ = "Integer32"
_FsPvrstInstPortRoleTransitionSemState_Object = MibTableColumn
fsPvrstInstPortRoleTransitionSemState = _FsPvrstInstPortRoleTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 24),
    _FsPvrstInstPortRoleTransitionSemState_Type()
)
fsPvrstInstPortRoleTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortRoleTransitionSemState.setStatus("current")


class _FsPvrstInstPortStateTransitionSemState_Type(Integer32):
    """Custom type fsPvrstInstPortStateTransitionSemState based on Integer32"""
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


_FsPvrstInstPortStateTransitionSemState_Type.__name__ = "Integer32"
_FsPvrstInstPortStateTransitionSemState_Object = MibTableColumn
fsPvrstInstPortStateTransitionSemState = _FsPvrstInstPortStateTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 25),
    _FsPvrstInstPortStateTransitionSemState_Type()
)
fsPvrstInstPortStateTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortStateTransitionSemState.setStatus("current")


class _FsPvrstInstPortTopologyChangeSemState_Type(Integer32):
    """Custom type fsPvrstInstPortTopologyChangeSemState based on Integer32"""
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
        *(("init", 0),
          ("inactive", 1),
          ("active", 2),
          ("detected", 3),
          ("notifiedtcn", 4),
          ("notifiedtc", 5),
          ("propagating", 6),
          ("acknowledged", 7))
    )


_FsPvrstInstPortTopologyChangeSemState_Type.__name__ = "Integer32"
_FsPvrstInstPortTopologyChangeSemState_Object = MibTableColumn
fsPvrstInstPortTopologyChangeSemState = _FsPvrstInstPortTopologyChangeSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 26),
    _FsPvrstInstPortTopologyChangeSemState_Type()
)
fsPvrstInstPortTopologyChangeSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortTopologyChangeSemState.setStatus("current")
_FsPvrstInstPortEffectivePortState_Type = TruthValue
_FsPvrstInstPortEffectivePortState_Object = MibTableColumn
fsPvrstInstPortEffectivePortState = _FsPvrstInstPortEffectivePortState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 27),
    _FsPvrstInstPortEffectivePortState_Type()
)
fsPvrstInstPortEffectivePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortEffectivePortState.setStatus("current")
_FsPvrstInstPortHelloTime_Type = Timeout
_FsPvrstInstPortHelloTime_Object = MibTableColumn
fsPvrstInstPortHelloTime = _FsPvrstInstPortHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 28),
    _FsPvrstInstPortHelloTime_Type()
)
fsPvrstInstPortHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortHelloTime.setStatus("current")
_FsPvrstInstPortMaxAge_Type = Timeout
_FsPvrstInstPortMaxAge_Object = MibTableColumn
fsPvrstInstPortMaxAge = _FsPvrstInstPortMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 29),
    _FsPvrstInstPortMaxAge_Type()
)
fsPvrstInstPortMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortMaxAge.setStatus("current")
_FsPvrstInstPortForwardDelay_Type = Timeout
_FsPvrstInstPortForwardDelay_Object = MibTableColumn
fsPvrstInstPortForwardDelay = _FsPvrstInstPortForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 30),
    _FsPvrstInstPortForwardDelay_Type()
)
fsPvrstInstPortForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortForwardDelay.setStatus("current")
_FsPvrstInstPortHoldTime_Type = Timeout
_FsPvrstInstPortHoldTime_Object = MibTableColumn
fsPvrstInstPortHoldTime = _FsPvrstInstPortHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 31),
    _FsPvrstInstPortHoldTime_Type()
)
fsPvrstInstPortHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstInstPortHoldTime.setStatus("current")


class _FsPvrstInstPortAdminPathCost_Type(Integer32):
    """Custom type fsPvrstInstPortAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_FsPvrstInstPortAdminPathCost_Type.__name__ = "Integer32"
_FsPvrstInstPortAdminPathCost_Object = MibTableColumn
fsPvrstInstPortAdminPathCost = _FsPvrstInstPortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 15, 1, 32),
    _FsPvrstInstPortAdminPathCost_Type()
)
fsPvrstInstPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPvrstInstPortAdminPathCost.setStatus("current")


class _FsPvrstCalcPortPathCostOnSpeedChg_Type(TruthValue):
    """Custom type fsPvrstCalcPortPathCostOnSpeedChg based on TruthValue"""
    defaultValue = 2


_FsPvrstCalcPortPathCostOnSpeedChg_Type.__name__ = "TruthValue"
_FsPvrstCalcPortPathCostOnSpeedChg_Object = MibScalar
fsPvrstCalcPortPathCostOnSpeedChg = _FsPvrstCalcPortPathCostOnSpeedChg_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 16),
    _FsPvrstCalcPortPathCostOnSpeedChg_Type()
)
fsPvrstCalcPortPathCostOnSpeedChg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPvrstCalcPortPathCostOnSpeedChg.setStatus("current")


class _FsPvrstGlobalBpduGuard_Type(Integer32):
    """Custom type fsPvrstGlobalBpduGuard based on Integer32"""
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


_FsPvrstGlobalBpduGuard_Type.__name__ = "Integer32"
_FsPvrstGlobalBpduGuard_Object = MibScalar
fsPvrstGlobalBpduGuard = _FsPvrstGlobalBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 1, 17),
    _FsPvrstGlobalBpduGuard_Type()
)
fsPvrstGlobalBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPvrstGlobalBpduGuard.setStatus("current")
_FsPvrstTrapsControl_ObjectIdentity = ObjectIdentity
fsPvrstTrapsControl = _FsPvrstTrapsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 2)
)


class _FsPvrstSetTraps_Type(Integer32):
    """Custom type fsPvrstSetTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FsPvrstSetTraps_Type.__name__ = "Integer32"
_FsPvrstSetTraps_Object = MibScalar
fsPvrstSetTraps = _FsPvrstSetTraps_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 2, 1),
    _FsPvrstSetTraps_Type()
)
fsPvrstSetTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPvrstSetTraps.setStatus("current")


class _FsPvrstGenTrapType_Type(Integer32):
    """Custom type fsPvrstGenTrapType based on Integer32"""
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


_FsPvrstGenTrapType_Type.__name__ = "Integer32"
_FsPvrstGenTrapType_Object = MibScalar
fsPvrstGenTrapType = _FsPvrstGenTrapType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 2, 2),
    _FsPvrstGenTrapType_Type()
)
fsPvrstGenTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstGenTrapType.setStatus("current")


class _FsPvrstErrTrapType_Type(Integer32):
    """Custom type fsPvrstErrTrapType based on Integer32"""
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


_FsPvrstErrTrapType_Type.__name__ = "Integer32"
_FsPvrstErrTrapType_Object = MibScalar
fsPvrstErrTrapType = _FsPvrstErrTrapType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 2, 3),
    _FsPvrstErrTrapType_Type()
)
fsPvrstErrTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstErrTrapType.setStatus("current")
_FsPvrstPortTrapNotificationTable_Object = MibTable
fsPvrstPortTrapNotificationTable = _FsPvrstPortTrapNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 2, 4)
)
if mibBuilder.loadTexts:
    fsPvrstPortTrapNotificationTable.setStatus("current")
_FsPvrstPortTrapNotificationEntry_Object = MibTableRow
fsPvrstPortTrapNotificationEntry = _FsPvrstPortTrapNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 2, 4, 1)
)
fsPvrstPortTrapNotificationEntry.setIndexNames(
    (0, "SUPERMICRO-PVRST-MIB", "fsPvrstPortTrapIndex"),
)
if mibBuilder.loadTexts:
    fsPvrstPortTrapNotificationEntry.setStatus("current")


class _FsPvrstPortTrapIndex_Type(Integer32):
    """Custom type fsPvrstPortTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_FsPvrstPortTrapIndex_Type.__name__ = "Integer32"
_FsPvrstPortTrapIndex_Object = MibTableColumn
fsPvrstPortTrapIndex = _FsPvrstPortTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 2, 4, 1, 1),
    _FsPvrstPortTrapIndex_Type()
)
fsPvrstPortTrapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPvrstPortTrapIndex.setStatus("current")


class _FsPvrstPortMigrationType_Type(Integer32):
    """Custom type fsPvrstPortMigrationType based on Integer32"""
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


_FsPvrstPortMigrationType_Type.__name__ = "Integer32"
_FsPvrstPortMigrationType_Object = MibTableColumn
fsPvrstPortMigrationType = _FsPvrstPortMigrationType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 2, 4, 1, 2),
    _FsPvrstPortMigrationType_Type()
)
fsPvrstPortMigrationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstPortMigrationType.setStatus("current")


class _FsPvrstPktErrType_Type(Integer32):
    """Custom type fsPvrstPktErrType based on Integer32"""
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
          ("pvrstLengthErr", 8))
    )


_FsPvrstPktErrType_Type.__name__ = "Integer32"
_FsPvrstPktErrType_Object = MibTableColumn
fsPvrstPktErrType = _FsPvrstPktErrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 2, 4, 1, 3),
    _FsPvrstPktErrType_Type()
)
fsPvrstPktErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstPktErrType.setStatus("current")
_FsPvrstPktErrVal_Type = Integer32
_FsPvrstPktErrVal_Object = MibTableColumn
fsPvrstPktErrVal = _FsPvrstPktErrVal_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 2, 4, 1, 4),
    _FsPvrstPktErrVal_Type()
)
fsPvrstPktErrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstPktErrVal.setStatus("current")
_FsPvrstPortRoleTrapNotificationTable_Object = MibTable
fsPvrstPortRoleTrapNotificationTable = _FsPvrstPortRoleTrapNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 2, 5)
)
if mibBuilder.loadTexts:
    fsPvrstPortRoleTrapNotificationTable.setStatus("current")
_FsPvrstPortRoleTrapNotificationEntry_Object = MibTableRow
fsPvrstPortRoleTrapNotificationEntry = _FsPvrstPortRoleTrapNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 2, 5, 1)
)
fsPvrstPortRoleTrapNotificationEntry.setIndexNames(
    (0, "SUPERMICRO-PVRST-MIB", "fsPvrstPortTrapIndex"),
    (0, "SUPERMICRO-PVRST-MIB", "fsPvrstInstVlanId"),
)
if mibBuilder.loadTexts:
    fsPvrstPortRoleTrapNotificationEntry.setStatus("current")


class _FsPvrstPortRoleType_Type(Integer32):
    """Custom type fsPvrstPortRoleType based on Integer32"""
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
        *(("disabledPort", 0),
          ("alternatePort", 1),
          ("backupPort", 2),
          ("rootPort", 3),
          ("designatedPort", 4))
    )


_FsPvrstPortRoleType_Type.__name__ = "Integer32"
_FsPvrstPortRoleType_Object = MibTableColumn
fsPvrstPortRoleType = _FsPvrstPortRoleType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 2, 5, 1, 1),
    _FsPvrstPortRoleType_Type()
)
fsPvrstPortRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstPortRoleType.setStatus("current")


class _FsPvrstOldRoleType_Type(Integer32):
    """Custom type fsPvrstOldRoleType based on Integer32"""
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
        *(("disabledPort", 0),
          ("alternatePort", 1),
          ("backupPort", 2),
          ("rootPort", 3),
          ("designatedPort", 4))
    )


_FsPvrstOldRoleType_Type.__name__ = "Integer32"
_FsPvrstOldRoleType_Object = MibTableColumn
fsPvrstOldRoleType = _FsPvrstOldRoleType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 2, 5, 1, 2),
    _FsPvrstOldRoleType_Type()
)
fsPvrstOldRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPvrstOldRoleType.setStatus("current")
_FsFuturePvrstTraps_ObjectIdentity = ObjectIdentity
fsFuturePvrstTraps = _FsFuturePvrstTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 3)
)
_FsPvrstTraps_ObjectIdentity = ObjectIdentity
fsPvrstTraps = _FsPvrstTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 3, 0)
)

# Managed Objects groups


# Notification objects

fsPvrstGenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 3, 0, 1)
)
fsPvrstGenTrap.setObjects(
      *(("SUPERMICRO-PVRST-MIB", "fsPvrstBrgAddress"),
        ("SUPERMICRO-PVRST-MIB", "fsPvrstGenTrapType"),
        ("SUPERMICRO-PVRST-MIB", "fsPvrstInstInstanceUpCount"),
        ("SUPERMICRO-PVRST-MIB", "fsPvrstInstInstanceDownCount"))
)
if mibBuilder.loadTexts:
    fsPvrstGenTrap.setStatus(
        "current"
    )

fsPvrstErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 3, 0, 2)
)
fsPvrstErrTrap.setObjects(
      *(("SUPERMICRO-PVRST-MIB", "fsPvrstBrgAddress"),
        ("SUPERMICRO-PVRST-MIB", "fsPvrstErrTrapType"))
)
if mibBuilder.loadTexts:
    fsPvrstErrTrap.setStatus(
        "current"
    )

fsPvrstNewRootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 3, 0, 3)
)
fsPvrstNewRootTrap.setObjects(
      *(("SUPERMICRO-PVRST-MIB", "fsPvrstBrgAddress"),
        ("SUPERMICRO-PVRST-MIB", "fsPvrstInstDesignatedRoot"))
)
if mibBuilder.loadTexts:
    fsPvrstNewRootTrap.setStatus(
        "current"
    )

fsPvrstTopologyChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 3, 0, 4)
)
fsPvrstTopologyChgTrap.setObjects(
      *(("SUPERMICRO-PVRST-MIB", "fsPvrstBrgAddress"),
        ("SUPERMICRO-PVRST-MIB", "fsPvrstInstTopChanges"))
)
if mibBuilder.loadTexts:
    fsPvrstTopologyChgTrap.setStatus(
        "current"
    )

fsPvrstProtocolMigrationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 3, 0, 5)
)
fsPvrstProtocolMigrationTrap.setObjects(
      *(("SUPERMICRO-PVRST-MIB", "fsPvrstBrgAddress"),
        ("SUPERMICRO-PVRST-MIB", "fsPvrstPortMigrationType"))
)
if mibBuilder.loadTexts:
    fsPvrstProtocolMigrationTrap.setStatus(
        "current"
    )

fsPvrstInvalidBpduRxdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 3, 0, 6)
)
fsPvrstInvalidBpduRxdTrap.setObjects(
      *(("SUPERMICRO-PVRST-MIB", "fsPvrstBrgAddress"),
        ("SUPERMICRO-PVRST-MIB", "fsPvrstPktErrType"),
        ("SUPERMICRO-PVRST-MIB", "fsPvrstPktErrVal"))
)
if mibBuilder.loadTexts:
    fsPvrstInvalidBpduRxdTrap.setStatus(
        "current"
    )

fsPvrstNewPortRoleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 3, 0, 7)
)
fsPvrstNewPortRoleTrap.setObjects(
      *(("SUPERMICRO-PVRST-MIB", "fsPvrstBrgAddress"),
        ("SUPERMICRO-PVRST-MIB", "fsPvrstPortRoleType"),
        ("SUPERMICRO-PVRST-MIB", "fsPvrstOldRoleType"))
)
if mibBuilder.loadTexts:
    fsPvrstNewPortRoleTrap.setStatus(
        "current"
    )

fsPvrstHwFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 161, 3, 0, 8)
)
fsPvrstHwFailureTrap.setObjects(
      *(("SUPERMICRO-PVRST-MIB", "fsPvrstBrgAddress"),
        ("SUPERMICRO-PVRST-MIB", "fsPvrstInstPortState"))
)
if mibBuilder.loadTexts:
    fsPvrstHwFailureTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-PVRST-MIB",
    **{"BridgeId": BridgeId,
       "Timeout": Timeout,
       "EnabledStatus": EnabledStatus,
       "futurePvrstMIB": futurePvrstMIB,
       "fsFuturePvrst": fsFuturePvrst,
       "fsPvrstSystemControl": fsPvrstSystemControl,
       "fsPvrstModuleStatus": fsPvrstModuleStatus,
       "fsPvrstNoOfActiveInstances": fsPvrstNoOfActiveInstances,
       "fsPvrstBrgAddress": fsPvrstBrgAddress,
       "fsPvrstUpCount": fsPvrstUpCount,
       "fsPvrstDownCount": fsPvrstDownCount,
       "fsPvrstPathCostDefaultType": fsPvrstPathCostDefaultType,
       "fsPvrstDynamicPathCostCalculation": fsPvrstDynamicPathCostCalculation,
       "fsPvrstTrace": fsPvrstTrace,
       "fsPvrstDebug": fsPvrstDebug,
       "fsPvrstBufferOverFlowCount": fsPvrstBufferOverFlowCount,
       "fsPvrstMemAllocFailureCount": fsPvrstMemAllocFailureCount,
       "fsFuturePvrstPortTable": fsFuturePvrstPortTable,
       "fsFuturePvrstPortEntry": fsFuturePvrstPortEntry,
       "fsPvrstPort": fsPvrstPort,
       "fsPvrstPortAdminEdgeStatus": fsPvrstPortAdminEdgeStatus,
       "fsPvrstPortOperEdgePortStatus": fsPvrstPortOperEdgePortStatus,
       "fsPvrstBridgeDetectionSemState": fsPvrstBridgeDetectionSemState,
       "fsPvrstPortEnabledStatus": fsPvrstPortEnabledStatus,
       "fsPvrstRootGuard": fsPvrstRootGuard,
       "fsPvrstBpduGuard": fsPvrstBpduGuard,
       "fsPvrstEncapType": fsPvrstEncapType,
       "fsPvrstPortAdminPointToPoint": fsPvrstPortAdminPointToPoint,
       "fsPvrstPortOperPointToPoint": fsPvrstPortOperPointToPoint,
       "fsPvrstPortInvalidBpdusRcvd": fsPvrstPortInvalidBpdusRcvd,
       "fsPvrstPortInvalidConfigBpduRxCount": fsPvrstPortInvalidConfigBpduRxCount,
       "fsPvrstPortInvalidTcnBpduRxCount": fsPvrstPortInvalidTcnBpduRxCount,
       "fsPvrstPortRowStatus": fsPvrstPortRowStatus,
       "fsPvrstInstBridgeTable": fsPvrstInstBridgeTable,
       "fsPvrstInstBridgeEntry": fsPvrstInstBridgeEntry,
       "fsPvrstInstVlanId": fsPvrstInstVlanId,
       "fsPvrstInstBridgePriority": fsPvrstInstBridgePriority,
       "fsPvrstInstRootCost": fsPvrstInstRootCost,
       "fsPvrstInstRootPort": fsPvrstInstRootPort,
       "fsPvrstInstBridgeMaxAge": fsPvrstInstBridgeMaxAge,
       "fsPvrstInstBridgeHelloTime": fsPvrstInstBridgeHelloTime,
       "fsPvrstInstBridgeForwardDelay": fsPvrstInstBridgeForwardDelay,
       "fsPvrstInstHoldTime": fsPvrstInstHoldTime,
       "fsPvrstInstTxHoldCount": fsPvrstInstTxHoldCount,
       "fsPvrstInstTimeSinceTopologyChange": fsPvrstInstTimeSinceTopologyChange,
       "fsPvrstInstTopChanges": fsPvrstInstTopChanges,
       "fsPvrstInstNewRootCount": fsPvrstInstNewRootCount,
       "fsPvrstInstInstanceUpCount": fsPvrstInstInstanceUpCount,
       "fsPvrstInstInstanceDownCount": fsPvrstInstInstanceDownCount,
       "fsPvrstInstPortRoleSelSemState": fsPvrstInstPortRoleSelSemState,
       "fsPvrstInstDesignatedRoot": fsPvrstInstDesignatedRoot,
       "fsPvrstInstRootMaxAge": fsPvrstInstRootMaxAge,
       "fsPvrstInstRootHelloTime": fsPvrstInstRootHelloTime,
       "fsPvrstInstRootForwardDelay": fsPvrstInstRootForwardDelay,
       "fsPvrstInstPortTable": fsPvrstInstPortTable,
       "fsPvrstInstPortEntry": fsPvrstInstPortEntry,
       "fsPvrstInstPortIndex": fsPvrstInstPortIndex,
       "fsPvrstInstPortEnableStatus": fsPvrstInstPortEnableStatus,
       "fsPvrstInstPortPathCost": fsPvrstInstPortPathCost,
       "fsPvrstInstPortPriority": fsPvrstInstPortPriority,
       "fsPvrstInstPortDesignatedRoot": fsPvrstInstPortDesignatedRoot,
       "fsPvrstInstPortDesignatedBridge": fsPvrstInstPortDesignatedBridge,
       "fsPvrstInstPortDesignatedPort": fsPvrstInstPortDesignatedPort,
       "fsPvrstInstPortOperVersion": fsPvrstInstPortOperVersion,
       "fsPvrstInstPortProtocolMigration": fsPvrstInstPortProtocolMigration,
       "fsPvrstInstPortState": fsPvrstInstPortState,
       "fsPvrstInstPortForwardTransitions": fsPvrstInstPortForwardTransitions,
       "fsPvrstInstPortReceivedBpdus": fsPvrstInstPortReceivedBpdus,
       "fsPvrstInstPortRxConfigBpduCount": fsPvrstInstPortRxConfigBpduCount,
       "fsPvrstInstPortRxTcnBpduCount": fsPvrstInstPortRxTcnBpduCount,
       "fsPvrstInstPortTransmittedBpdus": fsPvrstInstPortTransmittedBpdus,
       "fsPvrstInstPortTxConfigBpduCount": fsPvrstInstPortTxConfigBpduCount,
       "fsPvrstInstPortTxTcnBpduCount": fsPvrstInstPortTxTcnBpduCount,
       "fsPvrstInstPortTxSemState": fsPvrstInstPortTxSemState,
       "fsPvrstInstPortProtMigrationSemState": fsPvrstInstPortProtMigrationSemState,
       "fsPvrstInstProtocolMigrationCount": fsPvrstInstProtocolMigrationCount,
       "fsPvrstInstPortRole": fsPvrstInstPortRole,
       "fsPvrstInstCurrentPortRole": fsPvrstInstCurrentPortRole,
       "fsPvrstInstPortInfoSemState": fsPvrstInstPortInfoSemState,
       "fsPvrstInstPortRoleTransitionSemState": fsPvrstInstPortRoleTransitionSemState,
       "fsPvrstInstPortStateTransitionSemState": fsPvrstInstPortStateTransitionSemState,
       "fsPvrstInstPortTopologyChangeSemState": fsPvrstInstPortTopologyChangeSemState,
       "fsPvrstInstPortEffectivePortState": fsPvrstInstPortEffectivePortState,
       "fsPvrstInstPortHelloTime": fsPvrstInstPortHelloTime,
       "fsPvrstInstPortMaxAge": fsPvrstInstPortMaxAge,
       "fsPvrstInstPortForwardDelay": fsPvrstInstPortForwardDelay,
       "fsPvrstInstPortHoldTime": fsPvrstInstPortHoldTime,
       "fsPvrstInstPortAdminPathCost": fsPvrstInstPortAdminPathCost,
       "fsPvrstCalcPortPathCostOnSpeedChg": fsPvrstCalcPortPathCostOnSpeedChg,
       "fsPvrstGlobalBpduGuard": fsPvrstGlobalBpduGuard,
       "fsPvrstTrapsControl": fsPvrstTrapsControl,
       "fsPvrstSetTraps": fsPvrstSetTraps,
       "fsPvrstGenTrapType": fsPvrstGenTrapType,
       "fsPvrstErrTrapType": fsPvrstErrTrapType,
       "fsPvrstPortTrapNotificationTable": fsPvrstPortTrapNotificationTable,
       "fsPvrstPortTrapNotificationEntry": fsPvrstPortTrapNotificationEntry,
       "fsPvrstPortTrapIndex": fsPvrstPortTrapIndex,
       "fsPvrstPortMigrationType": fsPvrstPortMigrationType,
       "fsPvrstPktErrType": fsPvrstPktErrType,
       "fsPvrstPktErrVal": fsPvrstPktErrVal,
       "fsPvrstPortRoleTrapNotificationTable": fsPvrstPortRoleTrapNotificationTable,
       "fsPvrstPortRoleTrapNotificationEntry": fsPvrstPortRoleTrapNotificationEntry,
       "fsPvrstPortRoleType": fsPvrstPortRoleType,
       "fsPvrstOldRoleType": fsPvrstOldRoleType,
       "fsFuturePvrstTraps": fsFuturePvrstTraps,
       "fsPvrstTraps": fsPvrstTraps,
       "fsPvrstGenTrap": fsPvrstGenTrap,
       "fsPvrstErrTrap": fsPvrstErrTrap,
       "fsPvrstNewRootTrap": fsPvrstNewRootTrap,
       "fsPvrstTopologyChgTrap": fsPvrstTopologyChgTrap,
       "fsPvrstProtocolMigrationTrap": fsPvrstProtocolMigrationTrap,
       "fsPvrstInvalidBpduRxdTrap": fsPvrstInvalidBpduRxdTrap,
       "fsPvrstNewPortRoleTrap": fsPvrstNewPortRoleTrap,
       "fsPvrstHwFailureTrap": fsPvrstHwFailureTrap}
)
