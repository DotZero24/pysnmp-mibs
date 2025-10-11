# SNMP MIB module (Aricent-MIPVRST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/Aricent-MIPVRST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:43 2025
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

futureMIPvrstMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 154)
)
if mibBuilder.loadTexts:
    futureMIPvrstMIB.setRevisions(
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

_FsMIFuturePvrst_ObjectIdentity = ObjectIdentity
fsMIFuturePvrst = _FsMIFuturePvrst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1)
)
_FsMIPvrstGlobalTrace_Type = TruthValue
_FsMIPvrstGlobalTrace_Object = MibScalar
fsMIPvrstGlobalTrace = _FsMIPvrstGlobalTrace_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 1),
    _FsMIPvrstGlobalTrace_Type()
)
fsMIPvrstGlobalTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstGlobalTrace.setStatus("current")
_FsMIPvrstGlobalDebug_Type = TruthValue
_FsMIPvrstGlobalDebug_Object = MibScalar
fsMIPvrstGlobalDebug = _FsMIPvrstGlobalDebug_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 2),
    _FsMIPvrstGlobalDebug_Type()
)
fsMIPvrstGlobalDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstGlobalDebug.setStatus("current")
_FsMIFuturePvrstTable_Object = MibTable
fsMIFuturePvrstTable = _FsMIFuturePvrstTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 3)
)
if mibBuilder.loadTexts:
    fsMIFuturePvrstTable.setStatus("current")
_FsMIFuturePvrstEntry_Object = MibTableRow
fsMIFuturePvrstEntry = _FsMIFuturePvrstEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 3, 1)
)
fsMIFuturePvrstEntry.setIndexNames(
    (0, "Aricent-MIPVRST-MIB", "fsMIFuturePvrstContextId"),
)
if mibBuilder.loadTexts:
    fsMIFuturePvrstEntry.setStatus("current")


class _FsMIFuturePvrstContextId_Type(Integer32):
    """Custom type fsMIFuturePvrstContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIFuturePvrstContextId_Type.__name__ = "Integer32"
_FsMIFuturePvrstContextId_Object = MibTableColumn
fsMIFuturePvrstContextId = _FsMIFuturePvrstContextId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 3, 1, 1),
    _FsMIFuturePvrstContextId_Type()
)
fsMIFuturePvrstContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFuturePvrstContextId.setStatus("current")


class _FsMIPvrstSystemControl_Type(Integer32):
    """Custom type fsMIPvrstSystemControl based on Integer32"""
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


_FsMIPvrstSystemControl_Type.__name__ = "Integer32"
_FsMIPvrstSystemControl_Object = MibTableColumn
fsMIPvrstSystemControl = _FsMIPvrstSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 3, 1, 2),
    _FsMIPvrstSystemControl_Type()
)
fsMIPvrstSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstSystemControl.setStatus("current")
_FsMIPvrstModuleStatus_Type = EnabledStatus
_FsMIPvrstModuleStatus_Object = MibTableColumn
fsMIPvrstModuleStatus = _FsMIPvrstModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 3, 1, 3),
    _FsMIPvrstModuleStatus_Type()
)
fsMIPvrstModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstModuleStatus.setStatus("current")
_FsMIPvrstNoOfActiveInstances_Type = Integer32
_FsMIPvrstNoOfActiveInstances_Object = MibTableColumn
fsMIPvrstNoOfActiveInstances = _FsMIPvrstNoOfActiveInstances_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 3, 1, 4),
    _FsMIPvrstNoOfActiveInstances_Type()
)
fsMIPvrstNoOfActiveInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstNoOfActiveInstances.setStatus("current")
_FsMIPvrstBrgAddress_Type = MacAddress
_FsMIPvrstBrgAddress_Object = MibTableColumn
fsMIPvrstBrgAddress = _FsMIPvrstBrgAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 3, 1, 5),
    _FsMIPvrstBrgAddress_Type()
)
fsMIPvrstBrgAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstBrgAddress.setStatus("current")
_FsMIPvrstUpCount_Type = Counter32
_FsMIPvrstUpCount_Object = MibTableColumn
fsMIPvrstUpCount = _FsMIPvrstUpCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 3, 1, 6),
    _FsMIPvrstUpCount_Type()
)
fsMIPvrstUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstUpCount.setStatus("current")
_FsMIPvrstDownCount_Type = Counter32
_FsMIPvrstDownCount_Object = MibTableColumn
fsMIPvrstDownCount = _FsMIPvrstDownCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 3, 1, 7),
    _FsMIPvrstDownCount_Type()
)
fsMIPvrstDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstDownCount.setStatus("current")


class _FsMIPvrstPathCostDefaultType_Type(Integer32):
    """Custom type fsMIPvrstPathCostDefaultType based on Integer32"""
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


_FsMIPvrstPathCostDefaultType_Type.__name__ = "Integer32"
_FsMIPvrstPathCostDefaultType_Object = MibTableColumn
fsMIPvrstPathCostDefaultType = _FsMIPvrstPathCostDefaultType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 3, 1, 8),
    _FsMIPvrstPathCostDefaultType_Type()
)
fsMIPvrstPathCostDefaultType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstPathCostDefaultType.setStatus("obsolete")


class _FsMIPvrstDynamicPathCostCalculation_Type(TruthValue):
    """Custom type fsMIPvrstDynamicPathCostCalculation based on TruthValue"""
    defaultValue = 2


_FsMIPvrstDynamicPathCostCalculation_Type.__name__ = "TruthValue"
_FsMIPvrstDynamicPathCostCalculation_Object = MibTableColumn
fsMIPvrstDynamicPathCostCalculation = _FsMIPvrstDynamicPathCostCalculation_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 3, 1, 9),
    _FsMIPvrstDynamicPathCostCalculation_Type()
)
fsMIPvrstDynamicPathCostCalculation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstDynamicPathCostCalculation.setStatus("current")


class _FsMIPvrstTrace_Type(Integer32):
    """Custom type fsMIPvrstTrace based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIPvrstTrace_Type.__name__ = "Integer32"
_FsMIPvrstTrace_Object = MibTableColumn
fsMIPvrstTrace = _FsMIPvrstTrace_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 3, 1, 10),
    _FsMIPvrstTrace_Type()
)
fsMIPvrstTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstTrace.setStatus("current")


class _FsMIPvrstDebug_Type(Integer32):
    """Custom type fsMIPvrstDebug based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131071),
    )


_FsMIPvrstDebug_Type.__name__ = "Integer32"
_FsMIPvrstDebug_Object = MibTableColumn
fsMIPvrstDebug = _FsMIPvrstDebug_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 3, 1, 11),
    _FsMIPvrstDebug_Type()
)
fsMIPvrstDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstDebug.setStatus("current")
_FsMIPvrstBufferOverFlowCount_Type = Counter32
_FsMIPvrstBufferOverFlowCount_Object = MibTableColumn
fsMIPvrstBufferOverFlowCount = _FsMIPvrstBufferOverFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 3, 1, 12),
    _FsMIPvrstBufferOverFlowCount_Type()
)
fsMIPvrstBufferOverFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstBufferOverFlowCount.setStatus("current")
_FsMIPvrstMemAllocFailureCount_Type = Counter32
_FsMIPvrstMemAllocFailureCount_Object = MibTableColumn
fsMIPvrstMemAllocFailureCount = _FsMIPvrstMemAllocFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 3, 1, 13),
    _FsMIPvrstMemAllocFailureCount_Type()
)
fsMIPvrstMemAllocFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstMemAllocFailureCount.setStatus("current")


class _FsMIPvrstContextName_Type(DisplayString):
    """Custom type fsMIPvrstContextName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsMIPvrstContextName_Type.__name__ = "DisplayString"
_FsMIPvrstContextName_Object = MibTableColumn
fsMIPvrstContextName = _FsMIPvrstContextName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 3, 1, 14),
    _FsMIPvrstContextName_Type()
)
fsMIPvrstContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstContextName.setStatus("current")


class _FsMIPvrstCalcPortPathCostOnSpeedChg_Type(TruthValue):
    """Custom type fsMIPvrstCalcPortPathCostOnSpeedChg based on TruthValue"""
    defaultValue = 2


_FsMIPvrstCalcPortPathCostOnSpeedChg_Type.__name__ = "TruthValue"
_FsMIPvrstCalcPortPathCostOnSpeedChg_Object = MibTableColumn
fsMIPvrstCalcPortPathCostOnSpeedChg = _FsMIPvrstCalcPortPathCostOnSpeedChg_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 3, 1, 15),
    _FsMIPvrstCalcPortPathCostOnSpeedChg_Type()
)
fsMIPvrstCalcPortPathCostOnSpeedChg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstCalcPortPathCostOnSpeedChg.setStatus("current")


class _FsMIPvrstGlobalBpduGuard_Type(Integer32):
    """Custom type fsMIPvrstGlobalBpduGuard based on Integer32"""
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


_FsMIPvrstGlobalBpduGuard_Type.__name__ = "Integer32"
_FsMIPvrstGlobalBpduGuard_Object = MibTableColumn
fsMIPvrstGlobalBpduGuard = _FsMIPvrstGlobalBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 3, 1, 16),
    _FsMIPvrstGlobalBpduGuard_Type()
)
fsMIPvrstGlobalBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstGlobalBpduGuard.setStatus("current")


class _FsMIPvrstForceProtocolVersion_Type(Integer32):
    """Custom type fsMIPvrstForceProtocolVersion based on Integer32"""
    defaultValue = 2

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


_FsMIPvrstForceProtocolVersion_Type.__name__ = "Integer32"
_FsMIPvrstForceProtocolVersion_Object = MibTableColumn
fsMIPvrstForceProtocolVersion = _FsMIPvrstForceProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 3, 1, 17),
    _FsMIPvrstForceProtocolVersion_Type()
)
fsMIPvrstForceProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstForceProtocolVersion.setStatus("current")
_FsMIFuturePvrstPortTable_Object = MibTable
fsMIFuturePvrstPortTable = _FsMIFuturePvrstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4)
)
if mibBuilder.loadTexts:
    fsMIFuturePvrstPortTable.setStatus("current")
_FsMIFuturePvrstPortEntry_Object = MibTableRow
fsMIFuturePvrstPortEntry = _FsMIFuturePvrstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1)
)
fsMIFuturePvrstPortEntry.setIndexNames(
    (0, "Aricent-MIPVRST-MIB", "fsMIPvrstPort"),
)
if mibBuilder.loadTexts:
    fsMIFuturePvrstPortEntry.setStatus("current")


class _FsMIPvrstPort_Type(Integer32):
    """Custom type fsMIPvrstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIPvrstPort_Type.__name__ = "Integer32"
_FsMIPvrstPort_Object = MibTableColumn
fsMIPvrstPort = _FsMIPvrstPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 1),
    _FsMIPvrstPort_Type()
)
fsMIPvrstPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPvrstPort.setStatus("current")
_FsMIPvrstPortAdminEdgeStatus_Type = TruthValue
_FsMIPvrstPortAdminEdgeStatus_Object = MibTableColumn
fsMIPvrstPortAdminEdgeStatus = _FsMIPvrstPortAdminEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 2),
    _FsMIPvrstPortAdminEdgeStatus_Type()
)
fsMIPvrstPortAdminEdgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstPortAdminEdgeStatus.setStatus("current")
_FsMIPvrstPortOperEdgePortStatus_Type = TruthValue
_FsMIPvrstPortOperEdgePortStatus_Object = MibTableColumn
fsMIPvrstPortOperEdgePortStatus = _FsMIPvrstPortOperEdgePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 3),
    _FsMIPvrstPortOperEdgePortStatus_Type()
)
fsMIPvrstPortOperEdgePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstPortOperEdgePortStatus.setStatus("current")


class _FsMIPvrstBridgeDetectionSemState_Type(Integer32):
    """Custom type fsMIPvrstBridgeDetectionSemState based on Integer32"""
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


_FsMIPvrstBridgeDetectionSemState_Type.__name__ = "Integer32"
_FsMIPvrstBridgeDetectionSemState_Object = MibTableColumn
fsMIPvrstBridgeDetectionSemState = _FsMIPvrstBridgeDetectionSemState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 4),
    _FsMIPvrstBridgeDetectionSemState_Type()
)
fsMIPvrstBridgeDetectionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstBridgeDetectionSemState.setStatus("current")
_FsMIPvrstPortEnabledStatus_Type = TruthValue
_FsMIPvrstPortEnabledStatus_Object = MibTableColumn
fsMIPvrstPortEnabledStatus = _FsMIPvrstPortEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 5),
    _FsMIPvrstPortEnabledStatus_Type()
)
fsMIPvrstPortEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstPortEnabledStatus.setStatus("current")
_FsMIPvrstRootGuard_Type = TruthValue
_FsMIPvrstRootGuard_Object = MibTableColumn
fsMIPvrstRootGuard = _FsMIPvrstRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 6),
    _FsMIPvrstRootGuard_Type()
)
fsMIPvrstRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstRootGuard.setStatus("current")


class _FsMIPvrstBpduGuard_Type(Integer32):
    """Custom type fsMIPvrstBpduGuard based on Integer32"""
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


_FsMIPvrstBpduGuard_Type.__name__ = "Integer32"
_FsMIPvrstBpduGuard_Object = MibTableColumn
fsMIPvrstBpduGuard = _FsMIPvrstBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 7),
    _FsMIPvrstBpduGuard_Type()
)
fsMIPvrstBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstBpduGuard.setStatus("current")


class _FsMIPvrstEncapType_Type(Integer32):
    """Custom type fsMIPvrstEncapType based on Integer32"""
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


_FsMIPvrstEncapType_Type.__name__ = "Integer32"
_FsMIPvrstEncapType_Object = MibTableColumn
fsMIPvrstEncapType = _FsMIPvrstEncapType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 8),
    _FsMIPvrstEncapType_Type()
)
fsMIPvrstEncapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstEncapType.setStatus("current")


class _FsMIPvrstPortAdminPointToPoint_Type(Integer32):
    """Custom type fsMIPvrstPortAdminPointToPoint based on Integer32"""
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


_FsMIPvrstPortAdminPointToPoint_Type.__name__ = "Integer32"
_FsMIPvrstPortAdminPointToPoint_Object = MibTableColumn
fsMIPvrstPortAdminPointToPoint = _FsMIPvrstPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 9),
    _FsMIPvrstPortAdminPointToPoint_Type()
)
fsMIPvrstPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstPortAdminPointToPoint.setStatus("current")
_FsMIPvrstPortOperPointToPoint_Type = TruthValue
_FsMIPvrstPortOperPointToPoint_Object = MibTableColumn
fsMIPvrstPortOperPointToPoint = _FsMIPvrstPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 10),
    _FsMIPvrstPortOperPointToPoint_Type()
)
fsMIPvrstPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstPortOperPointToPoint.setStatus("current")
_FsMIPvrstPortInvalidBpdusRcvd_Type = Counter32
_FsMIPvrstPortInvalidBpdusRcvd_Object = MibTableColumn
fsMIPvrstPortInvalidBpdusRcvd = _FsMIPvrstPortInvalidBpdusRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 11),
    _FsMIPvrstPortInvalidBpdusRcvd_Type()
)
fsMIPvrstPortInvalidBpdusRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstPortInvalidBpdusRcvd.setStatus("current")
_FsMIPvrstPortInvalidConfigBpduRxCount_Type = Counter32
_FsMIPvrstPortInvalidConfigBpduRxCount_Object = MibTableColumn
fsMIPvrstPortInvalidConfigBpduRxCount = _FsMIPvrstPortInvalidConfigBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 12),
    _FsMIPvrstPortInvalidConfigBpduRxCount_Type()
)
fsMIPvrstPortInvalidConfigBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstPortInvalidConfigBpduRxCount.setStatus("current")
_FsMIPvrstPortInvalidTcnBpduRxCount_Type = Counter32
_FsMIPvrstPortInvalidTcnBpduRxCount_Object = MibTableColumn
fsMIPvrstPortInvalidTcnBpduRxCount = _FsMIPvrstPortInvalidTcnBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 13),
    _FsMIPvrstPortInvalidTcnBpduRxCount_Type()
)
fsMIPvrstPortInvalidTcnBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstPortInvalidTcnBpduRxCount.setStatus("current")
_FsMIPvrstPortRowStatus_Type = RowStatus
_FsMIPvrstPortRowStatus_Object = MibTableColumn
fsMIPvrstPortRowStatus = _FsMIPvrstPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 14),
    _FsMIPvrstPortRowStatus_Type()
)
fsMIPvrstPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIPvrstPortRowStatus.setStatus("current")


class _FsMIPvrstRootInconsistentState_Type(TruthValue):
    """Custom type fsMIPvrstRootInconsistentState based on TruthValue"""
    defaultValue = 2


_FsMIPvrstRootInconsistentState_Type.__name__ = "TruthValue"
_FsMIPvrstRootInconsistentState_Object = MibTableColumn
fsMIPvrstRootInconsistentState = _FsMIPvrstRootInconsistentState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 15),
    _FsMIPvrstRootInconsistentState_Type()
)
fsMIPvrstRootInconsistentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstRootInconsistentState.setStatus("current")


class _FsMIPvrstPortLoopGuard_Type(TruthValue):
    """Custom type fsMIPvrstPortLoopGuard based on TruthValue"""
    defaultValue = 2


_FsMIPvrstPortLoopGuard_Type.__name__ = "TruthValue"
_FsMIPvrstPortLoopGuard_Object = MibTableColumn
fsMIPvrstPortLoopGuard = _FsMIPvrstPortLoopGuard_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 16),
    _FsMIPvrstPortLoopGuard_Type()
)
fsMIPvrstPortLoopGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstPortLoopGuard.setStatus("current")


class _FsMIPvrstPortLoopInconsistentState_Type(TruthValue):
    """Custom type fsMIPvrstPortLoopInconsistentState based on TruthValue"""
    defaultValue = 2


_FsMIPvrstPortLoopInconsistentState_Type.__name__ = "TruthValue"
_FsMIPvrstPortLoopInconsistentState_Object = MibTableColumn
fsMIPvrstPortLoopInconsistentState = _FsMIPvrstPortLoopInconsistentState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 17),
    _FsMIPvrstPortLoopInconsistentState_Type()
)
fsMIPvrstPortLoopInconsistentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstPortLoopInconsistentState.setStatus("current")


class _FsMIPvrstPortEnableBPDURx_Type(TruthValue):
    """Custom type fsMIPvrstPortEnableBPDURx based on TruthValue"""
    defaultValue = 1


_FsMIPvrstPortEnableBPDURx_Type.__name__ = "TruthValue"
_FsMIPvrstPortEnableBPDURx_Object = MibTableColumn
fsMIPvrstPortEnableBPDURx = _FsMIPvrstPortEnableBPDURx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 18),
    _FsMIPvrstPortEnableBPDURx_Type()
)
fsMIPvrstPortEnableBPDURx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstPortEnableBPDURx.setStatus("current")


class _FsMIPvrstPortEnableBPDUTx_Type(TruthValue):
    """Custom type fsMIPvrstPortEnableBPDUTx based on TruthValue"""
    defaultValue = 1


_FsMIPvrstPortEnableBPDUTx_Type.__name__ = "TruthValue"
_FsMIPvrstPortEnableBPDUTx_Object = MibTableColumn
fsMIPvrstPortEnableBPDUTx = _FsMIPvrstPortEnableBPDUTx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 19),
    _FsMIPvrstPortEnableBPDUTx_Type()
)
fsMIPvrstPortEnableBPDUTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstPortEnableBPDUTx.setStatus("current")


class _FsMIPvrstBpduFilter_Type(Integer32):
    """Custom type fsMIPvrstBpduFilter based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FsMIPvrstBpduFilter_Type.__name__ = "Integer32"
_FsMIPvrstBpduFilter_Object = MibTableColumn
fsMIPvrstBpduFilter = _FsMIPvrstBpduFilter_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 20),
    _FsMIPvrstBpduFilter_Type()
)
fsMIPvrstBpduFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstBpduFilter.setStatus("current")


class _FsMIPvrstPortAutoEdge_Type(TruthValue):
    """Custom type fsMIPvrstPortAutoEdge based on TruthValue"""
    defaultValue = 1


_FsMIPvrstPortAutoEdge_Type.__name__ = "TruthValue"
_FsMIPvrstPortAutoEdge_Object = MibTableColumn
fsMIPvrstPortAutoEdge = _FsMIPvrstPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 21),
    _FsMIPvrstPortAutoEdge_Type()
)
fsMIPvrstPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstPortAutoEdge.setStatus("current")


class _FsMIPvrstPortBpduInconsistentState_Type(TruthValue):
    """Custom type fsMIPvrstPortBpduInconsistentState based on TruthValue"""
    defaultValue = 2


_FsMIPvrstPortBpduInconsistentState_Type.__name__ = "TruthValue"
_FsMIPvrstPortBpduInconsistentState_Object = MibTableColumn
fsMIPvrstPortBpduInconsistentState = _FsMIPvrstPortBpduInconsistentState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 22),
    _FsMIPvrstPortBpduInconsistentState_Type()
)
fsMIPvrstPortBpduInconsistentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstPortBpduInconsistentState.setStatus("current")


class _FsMIPvrstPortTypeInconsistentState_Type(TruthValue):
    """Custom type fsMIPvrstPortTypeInconsistentState based on TruthValue"""
    defaultValue = 2


_FsMIPvrstPortTypeInconsistentState_Type.__name__ = "TruthValue"
_FsMIPvrstPortTypeInconsistentState_Object = MibTableColumn
fsMIPvrstPortTypeInconsistentState = _FsMIPvrstPortTypeInconsistentState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 23),
    _FsMIPvrstPortTypeInconsistentState_Type()
)
fsMIPvrstPortTypeInconsistentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstPortTypeInconsistentState.setStatus("current")


class _FsMIPvrstPortPVIDInconsistentState_Type(TruthValue):
    """Custom type fsMIPvrstPortPVIDInconsistentState based on TruthValue"""
    defaultValue = 2


_FsMIPvrstPortPVIDInconsistentState_Type.__name__ = "TruthValue"
_FsMIPvrstPortPVIDInconsistentState_Object = MibTableColumn
fsMIPvrstPortPVIDInconsistentState = _FsMIPvrstPortPVIDInconsistentState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 24),
    _FsMIPvrstPortPVIDInconsistentState_Type()
)
fsMIPvrstPortPVIDInconsistentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstPortPVIDInconsistentState.setStatus("current")


class _FsMIPvrstPortBpduGuardAction_Type(Integer32):
    """Custom type fsMIPvrstPortBpduGuardAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-discarding", 1),
          ("admin-down", 2))
    )


_FsMIPvrstPortBpduGuardAction_Type.__name__ = "Integer32"
_FsMIPvrstPortBpduGuardAction_Object = MibTableColumn
fsMIPvrstPortBpduGuardAction = _FsMIPvrstPortBpduGuardAction_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 4, 1, 25),
    _FsMIPvrstPortBpduGuardAction_Type()
)
fsMIPvrstPortBpduGuardAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstPortBpduGuardAction.setStatus("current")
_FsMIPvrstInstBridgeTable_Object = MibTable
fsMIPvrstInstBridgeTable = _FsMIPvrstInstBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 5)
)
if mibBuilder.loadTexts:
    fsMIPvrstInstBridgeTable.setStatus("current")
_FsMIPvrstInstBridgeEntry_Object = MibTableRow
fsMIPvrstInstBridgeEntry = _FsMIPvrstInstBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 5, 1)
)
fsMIPvrstInstBridgeEntry.setIndexNames(
    (0, "Aricent-MIPVRST-MIB", "fsMIFuturePvrstContextId"),
    (0, "Aricent-MIPVRST-MIB", "fsMIPvrstInstVlanId"),
)
if mibBuilder.loadTexts:
    fsMIPvrstInstBridgeEntry.setStatus("current")


class _FsMIPvrstInstVlanId_Type(Integer32):
    """Custom type fsMIPvrstInstVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsMIPvrstInstVlanId_Type.__name__ = "Integer32"
_FsMIPvrstInstVlanId_Object = MibTableColumn
fsMIPvrstInstVlanId = _FsMIPvrstInstVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 5, 1, 1),
    _FsMIPvrstInstVlanId_Type()
)
fsMIPvrstInstVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPvrstInstVlanId.setStatus("current")


class _FsMIPvrstInstBridgePriority_Type(Integer32):
    """Custom type fsMIPvrstInstBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_FsMIPvrstInstBridgePriority_Type.__name__ = "Integer32"
_FsMIPvrstInstBridgePriority_Object = MibTableColumn
fsMIPvrstInstBridgePriority = _FsMIPvrstInstBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 5, 1, 2),
    _FsMIPvrstInstBridgePriority_Type()
)
fsMIPvrstInstBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstInstBridgePriority.setStatus("current")
_FsMIPvrstInstRootCost_Type = Integer32
_FsMIPvrstInstRootCost_Object = MibTableColumn
fsMIPvrstInstRootCost = _FsMIPvrstInstRootCost_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 5, 1, 3),
    _FsMIPvrstInstRootCost_Type()
)
fsMIPvrstInstRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstRootCost.setStatus("current")
_FsMIPvrstInstRootPort_Type = Integer32
_FsMIPvrstInstRootPort_Object = MibTableColumn
fsMIPvrstInstRootPort = _FsMIPvrstInstRootPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 5, 1, 4),
    _FsMIPvrstInstRootPort_Type()
)
fsMIPvrstInstRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstRootPort.setStatus("current")
_FsMIPvrstInstBridgeMaxAge_Type = Timeout
_FsMIPvrstInstBridgeMaxAge_Object = MibTableColumn
fsMIPvrstInstBridgeMaxAge = _FsMIPvrstInstBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 5, 1, 5),
    _FsMIPvrstInstBridgeMaxAge_Type()
)
fsMIPvrstInstBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstInstBridgeMaxAge.setStatus("current")
_FsMIPvrstInstBridgeHelloTime_Type = Timeout
_FsMIPvrstInstBridgeHelloTime_Object = MibTableColumn
fsMIPvrstInstBridgeHelloTime = _FsMIPvrstInstBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 5, 1, 6),
    _FsMIPvrstInstBridgeHelloTime_Type()
)
fsMIPvrstInstBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstInstBridgeHelloTime.setStatus("current")
_FsMIPvrstInstBridgeForwardDelay_Type = Timeout
_FsMIPvrstInstBridgeForwardDelay_Object = MibTableColumn
fsMIPvrstInstBridgeForwardDelay = _FsMIPvrstInstBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 5, 1, 7),
    _FsMIPvrstInstBridgeForwardDelay_Type()
)
fsMIPvrstInstBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstInstBridgeForwardDelay.setStatus("current")
_FsMIPvrstInstHoldTime_Type = Integer32
_FsMIPvrstInstHoldTime_Object = MibTableColumn
fsMIPvrstInstHoldTime = _FsMIPvrstInstHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 5, 1, 8),
    _FsMIPvrstInstHoldTime_Type()
)
fsMIPvrstInstHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstHoldTime.setStatus("current")


class _FsMIPvrstInstTxHoldCount_Type(Integer32):
    """Custom type fsMIPvrstInstTxHoldCount based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsMIPvrstInstTxHoldCount_Type.__name__ = "Integer32"
_FsMIPvrstInstTxHoldCount_Object = MibTableColumn
fsMIPvrstInstTxHoldCount = _FsMIPvrstInstTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 5, 1, 9),
    _FsMIPvrstInstTxHoldCount_Type()
)
fsMIPvrstInstTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstInstTxHoldCount.setStatus("current")
_FsMIPvrstInstTimeSinceTopologyChange_Type = TimeTicks
_FsMIPvrstInstTimeSinceTopologyChange_Object = MibTableColumn
fsMIPvrstInstTimeSinceTopologyChange = _FsMIPvrstInstTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 5, 1, 10),
    _FsMIPvrstInstTimeSinceTopologyChange_Type()
)
fsMIPvrstInstTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstTimeSinceTopologyChange.setStatus("current")
_FsMIPvrstInstTopChanges_Type = Counter32
_FsMIPvrstInstTopChanges_Object = MibTableColumn
fsMIPvrstInstTopChanges = _FsMIPvrstInstTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 5, 1, 11),
    _FsMIPvrstInstTopChanges_Type()
)
fsMIPvrstInstTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstTopChanges.setStatus("current")
_FsMIPvrstInstNewRootCount_Type = Counter32
_FsMIPvrstInstNewRootCount_Object = MibTableColumn
fsMIPvrstInstNewRootCount = _FsMIPvrstInstNewRootCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 5, 1, 12),
    _FsMIPvrstInstNewRootCount_Type()
)
fsMIPvrstInstNewRootCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstNewRootCount.setStatus("current")
_FsMIPvrstInstInstanceUpCount_Type = Counter32
_FsMIPvrstInstInstanceUpCount_Object = MibTableColumn
fsMIPvrstInstInstanceUpCount = _FsMIPvrstInstInstanceUpCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 5, 1, 13),
    _FsMIPvrstInstInstanceUpCount_Type()
)
fsMIPvrstInstInstanceUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstInstanceUpCount.setStatus("current")
_FsMIPvrstInstInstanceDownCount_Type = Counter32
_FsMIPvrstInstInstanceDownCount_Object = MibTableColumn
fsMIPvrstInstInstanceDownCount = _FsMIPvrstInstInstanceDownCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 5, 1, 14),
    _FsMIPvrstInstInstanceDownCount_Type()
)
fsMIPvrstInstInstanceDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstInstanceDownCount.setStatus("current")


class _FsMIPvrstInstPortRoleSelSemState_Type(Integer32):
    """Custom type fsMIPvrstInstPortRoleSelSemState based on Integer32"""
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


_FsMIPvrstInstPortRoleSelSemState_Type.__name__ = "Integer32"
_FsMIPvrstInstPortRoleSelSemState_Object = MibTableColumn
fsMIPvrstInstPortRoleSelSemState = _FsMIPvrstInstPortRoleSelSemState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 5, 1, 15),
    _FsMIPvrstInstPortRoleSelSemState_Type()
)
fsMIPvrstInstPortRoleSelSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortRoleSelSemState.setStatus("current")
_FsMIPvrstInstDesignatedRoot_Type = BridgeId
_FsMIPvrstInstDesignatedRoot_Object = MibTableColumn
fsMIPvrstInstDesignatedRoot = _FsMIPvrstInstDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 5, 1, 16),
    _FsMIPvrstInstDesignatedRoot_Type()
)
fsMIPvrstInstDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstDesignatedRoot.setStatus("current")
_FsMIPvrstInstRootMaxAge_Type = Timeout
_FsMIPvrstInstRootMaxAge_Object = MibTableColumn
fsMIPvrstInstRootMaxAge = _FsMIPvrstInstRootMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 5, 1, 17),
    _FsMIPvrstInstRootMaxAge_Type()
)
fsMIPvrstInstRootMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstRootMaxAge.setStatus("current")
_FsMIPvrstInstRootHelloTime_Type = Timeout
_FsMIPvrstInstRootHelloTime_Object = MibTableColumn
fsMIPvrstInstRootHelloTime = _FsMIPvrstInstRootHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 5, 1, 18),
    _FsMIPvrstInstRootHelloTime_Type()
)
fsMIPvrstInstRootHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstRootHelloTime.setStatus("current")
_FsMIPvrstInstRootForwardDelay_Type = Timeout
_FsMIPvrstInstRootForwardDelay_Object = MibTableColumn
fsMIPvrstInstRootForwardDelay = _FsMIPvrstInstRootForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 5, 1, 19),
    _FsMIPvrstInstRootForwardDelay_Type()
)
fsMIPvrstInstRootForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstRootForwardDelay.setStatus("current")
_FsMIPvrstInstPortTable_Object = MibTable
fsMIPvrstInstPortTable = _FsMIPvrstInstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6)
)
if mibBuilder.loadTexts:
    fsMIPvrstInstPortTable.setStatus("current")
_FsMIPvrstInstPortEntry_Object = MibTableRow
fsMIPvrstInstPortEntry = _FsMIPvrstInstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1)
)
fsMIPvrstInstPortEntry.setIndexNames(
    (0, "Aricent-MIPVRST-MIB", "fsMIPvrstInstVlanId"),
    (0, "Aricent-MIPVRST-MIB", "fsMIPvrstInstPortIndex"),
)
if mibBuilder.loadTexts:
    fsMIPvrstInstPortEntry.setStatus("current")


class _FsMIPvrstInstPortIndex_Type(Integer32):
    """Custom type fsMIPvrstInstPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIPvrstInstPortIndex_Type.__name__ = "Integer32"
_FsMIPvrstInstPortIndex_Object = MibTableColumn
fsMIPvrstInstPortIndex = _FsMIPvrstInstPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 1),
    _FsMIPvrstInstPortIndex_Type()
)
fsMIPvrstInstPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortIndex.setStatus("current")


class _FsMIPvrstInstPortEnableStatus_Type(Integer32):
    """Custom type fsMIPvrstInstPortEnableStatus based on Integer32"""
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


_FsMIPvrstInstPortEnableStatus_Type.__name__ = "Integer32"
_FsMIPvrstInstPortEnableStatus_Object = MibTableColumn
fsMIPvrstInstPortEnableStatus = _FsMIPvrstInstPortEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 2),
    _FsMIPvrstInstPortEnableStatus_Type()
)
fsMIPvrstInstPortEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortEnableStatus.setStatus("current")


class _FsMIPvrstInstPortPathCost_Type(Integer32):
    """Custom type fsMIPvrstInstPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_FsMIPvrstInstPortPathCost_Type.__name__ = "Integer32"
_FsMIPvrstInstPortPathCost_Object = MibTableColumn
fsMIPvrstInstPortPathCost = _FsMIPvrstInstPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 3),
    _FsMIPvrstInstPortPathCost_Type()
)
fsMIPvrstInstPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortPathCost.setStatus("current")


class _FsMIPvrstInstPortPriority_Type(Integer32):
    """Custom type fsMIPvrstInstPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_FsMIPvrstInstPortPriority_Type.__name__ = "Integer32"
_FsMIPvrstInstPortPriority_Object = MibTableColumn
fsMIPvrstInstPortPriority = _FsMIPvrstInstPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 4),
    _FsMIPvrstInstPortPriority_Type()
)
fsMIPvrstInstPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortPriority.setStatus("current")
_FsMIPvrstInstPortDesignatedRoot_Type = BridgeId
_FsMIPvrstInstPortDesignatedRoot_Object = MibTableColumn
fsMIPvrstInstPortDesignatedRoot = _FsMIPvrstInstPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 5),
    _FsMIPvrstInstPortDesignatedRoot_Type()
)
fsMIPvrstInstPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortDesignatedRoot.setStatus("current")
_FsMIPvrstInstPortDesignatedBridge_Type = BridgeId
_FsMIPvrstInstPortDesignatedBridge_Object = MibTableColumn
fsMIPvrstInstPortDesignatedBridge = _FsMIPvrstInstPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 6),
    _FsMIPvrstInstPortDesignatedBridge_Type()
)
fsMIPvrstInstPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortDesignatedBridge.setStatus("current")


class _FsMIPvrstInstPortDesignatedPort_Type(OctetString):
    """Custom type fsMIPvrstInstPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_FsMIPvrstInstPortDesignatedPort_Type.__name__ = "OctetString"
_FsMIPvrstInstPortDesignatedPort_Object = MibTableColumn
fsMIPvrstInstPortDesignatedPort = _FsMIPvrstInstPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 7),
    _FsMIPvrstInstPortDesignatedPort_Type()
)
fsMIPvrstInstPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortDesignatedPort.setStatus("current")


class _FsMIPvrstInstPortOperVersion_Type(Integer32):
    """Custom type fsMIPvrstInstPortOperVersion based on Integer32"""
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


_FsMIPvrstInstPortOperVersion_Type.__name__ = "Integer32"
_FsMIPvrstInstPortOperVersion_Object = MibTableColumn
fsMIPvrstInstPortOperVersion = _FsMIPvrstInstPortOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 8),
    _FsMIPvrstInstPortOperVersion_Type()
)
fsMIPvrstInstPortOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortOperVersion.setStatus("current")
_FsMIPvrstInstPortProtocolMigration_Type = TruthValue
_FsMIPvrstInstPortProtocolMigration_Object = MibTableColumn
fsMIPvrstInstPortProtocolMigration = _FsMIPvrstInstPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 9),
    _FsMIPvrstInstPortProtocolMigration_Type()
)
fsMIPvrstInstPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortProtocolMigration.setStatus("current")


class _FsMIPvrstInstPortState_Type(Integer32):
    """Custom type fsMIPvrstInstPortState based on Integer32"""
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


_FsMIPvrstInstPortState_Type.__name__ = "Integer32"
_FsMIPvrstInstPortState_Object = MibTableColumn
fsMIPvrstInstPortState = _FsMIPvrstInstPortState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 10),
    _FsMIPvrstInstPortState_Type()
)
fsMIPvrstInstPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortState.setStatus("current")
_FsMIPvrstInstPortForwardTransitions_Type = Counter32
_FsMIPvrstInstPortForwardTransitions_Object = MibTableColumn
fsMIPvrstInstPortForwardTransitions = _FsMIPvrstInstPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 11),
    _FsMIPvrstInstPortForwardTransitions_Type()
)
fsMIPvrstInstPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortForwardTransitions.setStatus("current")
_FsMIPvrstInstPortReceivedBpdus_Type = Counter32
_FsMIPvrstInstPortReceivedBpdus_Object = MibTableColumn
fsMIPvrstInstPortReceivedBpdus = _FsMIPvrstInstPortReceivedBpdus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 12),
    _FsMIPvrstInstPortReceivedBpdus_Type()
)
fsMIPvrstInstPortReceivedBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortReceivedBpdus.setStatus("current")
_FsMIPvrstInstPortRxConfigBpduCount_Type = Counter32
_FsMIPvrstInstPortRxConfigBpduCount_Object = MibTableColumn
fsMIPvrstInstPortRxConfigBpduCount = _FsMIPvrstInstPortRxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 13),
    _FsMIPvrstInstPortRxConfigBpduCount_Type()
)
fsMIPvrstInstPortRxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortRxConfigBpduCount.setStatus("current")
_FsMIPvrstInstPortRxTcnBpduCount_Type = Counter32
_FsMIPvrstInstPortRxTcnBpduCount_Object = MibTableColumn
fsMIPvrstInstPortRxTcnBpduCount = _FsMIPvrstInstPortRxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 14),
    _FsMIPvrstInstPortRxTcnBpduCount_Type()
)
fsMIPvrstInstPortRxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortRxTcnBpduCount.setStatus("current")
_FsMIPvrstInstPortTransmittedBpdus_Type = Counter32
_FsMIPvrstInstPortTransmittedBpdus_Object = MibTableColumn
fsMIPvrstInstPortTransmittedBpdus = _FsMIPvrstInstPortTransmittedBpdus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 15),
    _FsMIPvrstInstPortTransmittedBpdus_Type()
)
fsMIPvrstInstPortTransmittedBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortTransmittedBpdus.setStatus("current")
_FsMIPvrstInstPortTxConfigBpduCount_Type = Counter32
_FsMIPvrstInstPortTxConfigBpduCount_Object = MibTableColumn
fsMIPvrstInstPortTxConfigBpduCount = _FsMIPvrstInstPortTxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 16),
    _FsMIPvrstInstPortTxConfigBpduCount_Type()
)
fsMIPvrstInstPortTxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortTxConfigBpduCount.setStatus("current")
_FsMIPvrstInstPortTxTcnBpduCount_Type = Counter32
_FsMIPvrstInstPortTxTcnBpduCount_Object = MibTableColumn
fsMIPvrstInstPortTxTcnBpduCount = _FsMIPvrstInstPortTxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 17),
    _FsMIPvrstInstPortTxTcnBpduCount_Type()
)
fsMIPvrstInstPortTxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortTxTcnBpduCount.setStatus("current")


class _FsMIPvrstInstPortTxSemState_Type(Integer32):
    """Custom type fsMIPvrstInstPortTxSemState based on Integer32"""
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


_FsMIPvrstInstPortTxSemState_Type.__name__ = "Integer32"
_FsMIPvrstInstPortTxSemState_Object = MibTableColumn
fsMIPvrstInstPortTxSemState = _FsMIPvrstInstPortTxSemState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 18),
    _FsMIPvrstInstPortTxSemState_Type()
)
fsMIPvrstInstPortTxSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortTxSemState.setStatus("current")


class _FsMIPvrstInstPortProtMigrationSemState_Type(Integer32):
    """Custom type fsMIPvrstInstPortProtMigrationSemState based on Integer32"""
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


_FsMIPvrstInstPortProtMigrationSemState_Type.__name__ = "Integer32"
_FsMIPvrstInstPortProtMigrationSemState_Object = MibTableColumn
fsMIPvrstInstPortProtMigrationSemState = _FsMIPvrstInstPortProtMigrationSemState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 19),
    _FsMIPvrstInstPortProtMigrationSemState_Type()
)
fsMIPvrstInstPortProtMigrationSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortProtMigrationSemState.setStatus("current")
_FsMIPvrstInstProtocolMigrationCount_Type = Counter32
_FsMIPvrstInstProtocolMigrationCount_Object = MibTableColumn
fsMIPvrstInstProtocolMigrationCount = _FsMIPvrstInstProtocolMigrationCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 20),
    _FsMIPvrstInstProtocolMigrationCount_Type()
)
fsMIPvrstInstProtocolMigrationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstProtocolMigrationCount.setStatus("current")


class _FsMIPvrstInstPortRole_Type(Integer32):
    """Custom type fsMIPvrstInstPortRole based on Integer32"""
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


_FsMIPvrstInstPortRole_Type.__name__ = "Integer32"
_FsMIPvrstInstPortRole_Object = MibTableColumn
fsMIPvrstInstPortRole = _FsMIPvrstInstPortRole_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 21),
    _FsMIPvrstInstPortRole_Type()
)
fsMIPvrstInstPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortRole.setStatus("current")


class _FsMIPvrstInstCurrentPortRole_Type(Integer32):
    """Custom type fsMIPvrstInstCurrentPortRole based on Integer32"""
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


_FsMIPvrstInstCurrentPortRole_Type.__name__ = "Integer32"
_FsMIPvrstInstCurrentPortRole_Object = MibTableColumn
fsMIPvrstInstCurrentPortRole = _FsMIPvrstInstCurrentPortRole_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 22),
    _FsMIPvrstInstCurrentPortRole_Type()
)
fsMIPvrstInstCurrentPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstCurrentPortRole.setStatus("current")


class _FsMIPvrstInstPortInfoSemState_Type(Integer32):
    """Custom type fsMIPvrstInstPortInfoSemState based on Integer32"""
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


_FsMIPvrstInstPortInfoSemState_Type.__name__ = "Integer32"
_FsMIPvrstInstPortInfoSemState_Object = MibTableColumn
fsMIPvrstInstPortInfoSemState = _FsMIPvrstInstPortInfoSemState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 23),
    _FsMIPvrstInstPortInfoSemState_Type()
)
fsMIPvrstInstPortInfoSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortInfoSemState.setStatus("current")


class _FsMIPvrstInstPortRoleTransitionSemState_Type(Integer32):
    """Custom type fsMIPvrstInstPortRoleTransitionSemState based on Integer32"""
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


_FsMIPvrstInstPortRoleTransitionSemState_Type.__name__ = "Integer32"
_FsMIPvrstInstPortRoleTransitionSemState_Object = MibTableColumn
fsMIPvrstInstPortRoleTransitionSemState = _FsMIPvrstInstPortRoleTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 24),
    _FsMIPvrstInstPortRoleTransitionSemState_Type()
)
fsMIPvrstInstPortRoleTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortRoleTransitionSemState.setStatus("current")


class _FsMIPvrstInstPortStateTransitionSemState_Type(Integer32):
    """Custom type fsMIPvrstInstPortStateTransitionSemState based on Integer32"""
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


_FsMIPvrstInstPortStateTransitionSemState_Type.__name__ = "Integer32"
_FsMIPvrstInstPortStateTransitionSemState_Object = MibTableColumn
fsMIPvrstInstPortStateTransitionSemState = _FsMIPvrstInstPortStateTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 25),
    _FsMIPvrstInstPortStateTransitionSemState_Type()
)
fsMIPvrstInstPortStateTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortStateTransitionSemState.setStatus("current")


class _FsMIPvrstInstPortTopologyChangeSemState_Type(Integer32):
    """Custom type fsMIPvrstInstPortTopologyChangeSemState based on Integer32"""
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


_FsMIPvrstInstPortTopologyChangeSemState_Type.__name__ = "Integer32"
_FsMIPvrstInstPortTopologyChangeSemState_Object = MibTableColumn
fsMIPvrstInstPortTopologyChangeSemState = _FsMIPvrstInstPortTopologyChangeSemState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 26),
    _FsMIPvrstInstPortTopologyChangeSemState_Type()
)
fsMIPvrstInstPortTopologyChangeSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortTopologyChangeSemState.setStatus("current")
_FsMIPvrstInstPortEffectivePortState_Type = TruthValue
_FsMIPvrstInstPortEffectivePortState_Object = MibTableColumn
fsMIPvrstInstPortEffectivePortState = _FsMIPvrstInstPortEffectivePortState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 27),
    _FsMIPvrstInstPortEffectivePortState_Type()
)
fsMIPvrstInstPortEffectivePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortEffectivePortState.setStatus("current")
_FsMIPvrstInstPortHelloTime_Type = Timeout
_FsMIPvrstInstPortHelloTime_Object = MibTableColumn
fsMIPvrstInstPortHelloTime = _FsMIPvrstInstPortHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 28),
    _FsMIPvrstInstPortHelloTime_Type()
)
fsMIPvrstInstPortHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortHelloTime.setStatus("current")
_FsMIPvrstInstPortMaxAge_Type = Timeout
_FsMIPvrstInstPortMaxAge_Object = MibTableColumn
fsMIPvrstInstPortMaxAge = _FsMIPvrstInstPortMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 29),
    _FsMIPvrstInstPortMaxAge_Type()
)
fsMIPvrstInstPortMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortMaxAge.setStatus("current")
_FsMIPvrstInstPortForwardDelay_Type = Timeout
_FsMIPvrstInstPortForwardDelay_Object = MibTableColumn
fsMIPvrstInstPortForwardDelay = _FsMIPvrstInstPortForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 30),
    _FsMIPvrstInstPortForwardDelay_Type()
)
fsMIPvrstInstPortForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortForwardDelay.setStatus("current")
_FsMIPvrstInstPortHoldTime_Type = Timeout
_FsMIPvrstInstPortHoldTime_Object = MibTableColumn
fsMIPvrstInstPortHoldTime = _FsMIPvrstInstPortHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 31),
    _FsMIPvrstInstPortHoldTime_Type()
)
fsMIPvrstInstPortHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortHoldTime.setStatus("current")


class _FsMIPvrstInstPortAdminPathCost_Type(Integer32):
    """Custom type fsMIPvrstInstPortAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_FsMIPvrstInstPortAdminPathCost_Type.__name__ = "Integer32"
_FsMIPvrstInstPortAdminPathCost_Object = MibTableColumn
fsMIPvrstInstPortAdminPathCost = _FsMIPvrstInstPortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 1, 6, 1, 32),
    _FsMIPvrstInstPortAdminPathCost_Type()
)
fsMIPvrstInstPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstInstPortAdminPathCost.setStatus("current")
_FsMIFsPvrstTrapsControl_ObjectIdentity = ObjectIdentity
fsMIFsPvrstTrapsControl = _FsMIFsPvrstTrapsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 154, 2)
)


class _FsMIFsPvrstSetGlobalTrapOption_Type(Integer32):
    """Custom type fsMIFsPvrstSetGlobalTrapOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsMIFsPvrstSetGlobalTrapOption_Type.__name__ = "Integer32"
_FsMIFsPvrstSetGlobalTrapOption_Object = MibScalar
fsMIFsPvrstSetGlobalTrapOption = _FsMIFsPvrstSetGlobalTrapOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 2, 1),
    _FsMIFsPvrstSetGlobalTrapOption_Type()
)
fsMIFsPvrstSetGlobalTrapOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsPvrstSetGlobalTrapOption.setStatus("current")


class _FsMIPvrstGlobalErrTrapType_Type(Integer32):
    """Custom type fsMIPvrstGlobalErrTrapType based on Integer32"""
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


_FsMIPvrstGlobalErrTrapType_Type.__name__ = "Integer32"
_FsMIPvrstGlobalErrTrapType_Object = MibScalar
fsMIPvrstGlobalErrTrapType = _FsMIPvrstGlobalErrTrapType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 2, 2),
    _FsMIPvrstGlobalErrTrapType_Type()
)
fsMIPvrstGlobalErrTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstGlobalErrTrapType.setStatus("current")
_FsMIFsPvrstTrapsControlTable_Object = MibTable
fsMIFsPvrstTrapsControlTable = _FsMIFsPvrstTrapsControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 2, 3)
)
if mibBuilder.loadTexts:
    fsMIFsPvrstTrapsControlTable.setStatus("current")
_FsMIFsPvrstTrapsControlEntry_Object = MibTableRow
fsMIFsPvrstTrapsControlEntry = _FsMIFsPvrstTrapsControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 2, 3, 1)
)
fsMIFsPvrstTrapsControlEntry.setIndexNames(
    (0, "Aricent-MIPVRST-MIB", "fsMIFuturePvrstContextId"),
)
if mibBuilder.loadTexts:
    fsMIFsPvrstTrapsControlEntry.setStatus("current")


class _FsMIPvrstSetTraps_Type(Integer32):
    """Custom type fsMIPvrstSetTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FsMIPvrstSetTraps_Type.__name__ = "Integer32"
_FsMIPvrstSetTraps_Object = MibTableColumn
fsMIPvrstSetTraps = _FsMIPvrstSetTraps_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 2, 3, 1, 1),
    _FsMIPvrstSetTraps_Type()
)
fsMIPvrstSetTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPvrstSetTraps.setStatus("current")


class _FsMIPvrstGenTrapType_Type(Integer32):
    """Custom type fsMIPvrstGenTrapType based on Integer32"""
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


_FsMIPvrstGenTrapType_Type.__name__ = "Integer32"
_FsMIPvrstGenTrapType_Object = MibTableColumn
fsMIPvrstGenTrapType = _FsMIPvrstGenTrapType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 2, 3, 1, 2),
    _FsMIPvrstGenTrapType_Type()
)
fsMIPvrstGenTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstGenTrapType.setStatus("current")
_FsMIPvrstPortTrapNotificationTable_Object = MibTable
fsMIPvrstPortTrapNotificationTable = _FsMIPvrstPortTrapNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 2, 4)
)
if mibBuilder.loadTexts:
    fsMIPvrstPortTrapNotificationTable.setStatus("current")
_FsMIPvrstPortTrapNotificationEntry_Object = MibTableRow
fsMIPvrstPortTrapNotificationEntry = _FsMIPvrstPortTrapNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 2, 4, 1)
)
fsMIPvrstPortTrapNotificationEntry.setIndexNames(
    (0, "Aricent-MIPVRST-MIB", "fsMIPvrstPortTrapIndex"),
)
if mibBuilder.loadTexts:
    fsMIPvrstPortTrapNotificationEntry.setStatus("current")


class _FsMIPvrstPortTrapIndex_Type(Integer32):
    """Custom type fsMIPvrstPortTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_FsMIPvrstPortTrapIndex_Type.__name__ = "Integer32"
_FsMIPvrstPortTrapIndex_Object = MibTableColumn
fsMIPvrstPortTrapIndex = _FsMIPvrstPortTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 2, 4, 1, 1),
    _FsMIPvrstPortTrapIndex_Type()
)
fsMIPvrstPortTrapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPvrstPortTrapIndex.setStatus("current")


class _FsMIPvrstPortMigrationType_Type(Integer32):
    """Custom type fsMIPvrstPortMigrationType based on Integer32"""
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


_FsMIPvrstPortMigrationType_Type.__name__ = "Integer32"
_FsMIPvrstPortMigrationType_Object = MibTableColumn
fsMIPvrstPortMigrationType = _FsMIPvrstPortMigrationType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 2, 4, 1, 2),
    _FsMIPvrstPortMigrationType_Type()
)
fsMIPvrstPortMigrationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstPortMigrationType.setStatus("current")


class _FsMIPvrstPktErrType_Type(Integer32):
    """Custom type fsMIPvrstPktErrType based on Integer32"""
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


_FsMIPvrstPktErrType_Type.__name__ = "Integer32"
_FsMIPvrstPktErrType_Object = MibTableColumn
fsMIPvrstPktErrType = _FsMIPvrstPktErrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 2, 4, 1, 3),
    _FsMIPvrstPktErrType_Type()
)
fsMIPvrstPktErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstPktErrType.setStatus("current")
_FsMIPvrstPktErrVal_Type = Integer32
_FsMIPvrstPktErrVal_Object = MibTableColumn
fsMIPvrstPktErrVal = _FsMIPvrstPktErrVal_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 2, 4, 1, 4),
    _FsMIPvrstPktErrVal_Type()
)
fsMIPvrstPktErrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstPktErrVal.setStatus("current")
_FsMIPvrstPortRoleTrapNotificationTable_Object = MibTable
fsMIPvrstPortRoleTrapNotificationTable = _FsMIPvrstPortRoleTrapNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 2, 5)
)
if mibBuilder.loadTexts:
    fsMIPvrstPortRoleTrapNotificationTable.setStatus("current")
_FsMIPvrstPortRoleTrapNotificationEntry_Object = MibTableRow
fsMIPvrstPortRoleTrapNotificationEntry = _FsMIPvrstPortRoleTrapNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 2, 5, 1)
)
fsMIPvrstPortRoleTrapNotificationEntry.setIndexNames(
    (0, "Aricent-MIPVRST-MIB", "fsMIPvrstPortTrapIndex"),
    (0, "Aricent-MIPVRST-MIB", "fsMIPvrstInstVlanId"),
)
if mibBuilder.loadTexts:
    fsMIPvrstPortRoleTrapNotificationEntry.setStatus("current")


class _FsMIPvrstPortRoleType_Type(Integer32):
    """Custom type fsMIPvrstPortRoleType based on Integer32"""
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


_FsMIPvrstPortRoleType_Type.__name__ = "Integer32"
_FsMIPvrstPortRoleType_Object = MibTableColumn
fsMIPvrstPortRoleType = _FsMIPvrstPortRoleType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 2, 5, 1, 1),
    _FsMIPvrstPortRoleType_Type()
)
fsMIPvrstPortRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstPortRoleType.setStatus("current")


class _FsMIPvrstOldRoleType_Type(Integer32):
    """Custom type fsMIPvrstOldRoleType based on Integer32"""
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


_FsMIPvrstOldRoleType_Type.__name__ = "Integer32"
_FsMIPvrstOldRoleType_Object = MibTableColumn
fsMIPvrstOldRoleType = _FsMIPvrstOldRoleType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 154, 2, 5, 1, 2),
    _FsMIPvrstOldRoleType_Type()
)
fsMIPvrstOldRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPvrstOldRoleType.setStatus("current")
_FsMIFuturePvrstTraps_ObjectIdentity = ObjectIdentity
fsMIFuturePvrstTraps = _FsMIFuturePvrstTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 154, 3)
)
_FsMIPvrstTraps_ObjectIdentity = ObjectIdentity
fsMIPvrstTraps = _FsMIPvrstTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 154, 3, 0)
)

# Managed Objects groups


# Notification objects

fsMIPvrstGlobalErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 154, 3, 0, 1)
)
fsMIPvrstGlobalErrTrap.setObjects(
      *(("Aricent-MIPVRST-MIB", "fsMIPvrstBrgAddress"),
        ("Aricent-MIPVRST-MIB", "fsMIPvrstGenTrapType"),
        ("Aricent-MIPVRST-MIB", "fsMIPvrstInstInstanceUpCount"),
        ("Aricent-MIPVRST-MIB", "fsMIPvrstInstInstanceDownCount"))
)
if mibBuilder.loadTexts:
    fsMIPvrstGlobalErrTrap.setStatus(
        "current"
    )

fsMIPvrstGenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 154, 3, 0, 2)
)
fsMIPvrstGenTrap.setObjects(
      *(("Aricent-MIPVRST-MIB", "fsMIPvrstBrgAddress"),
        ("Aricent-MIPVRST-MIB", "fsMIPvrstContextName"),
        ("Aricent-MIPVRST-MIB", "fsMIPvrstGenTrapType"))
)
if mibBuilder.loadTexts:
    fsMIPvrstGenTrap.setStatus(
        "current"
    )

fsMIPvrstNewRootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 154, 3, 0, 3)
)
fsMIPvrstNewRootTrap.setObjects(
      *(("Aricent-MIPVRST-MIB", "fsMIPvrstBrgAddress"),
        ("Aricent-MIPVRST-MIB", "fsMIPvrstContextName"),
        ("Aricent-MIPVRST-MIB", "fsMIPvrstInstDesignatedRoot"))
)
if mibBuilder.loadTexts:
    fsMIPvrstNewRootTrap.setStatus(
        "current"
    )

fsMIPvrstTopologyChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 154, 3, 0, 4)
)
fsMIPvrstTopologyChgTrap.setObjects(
      *(("Aricent-MIPVRST-MIB", "fsMIPvrstBrgAddress"),
        ("Aricent-MIPVRST-MIB", "fsMIPvrstContextName"),
        ("Aricent-MIPVRST-MIB", "fsMIPvrstInstTopChanges"))
)
if mibBuilder.loadTexts:
    fsMIPvrstTopologyChgTrap.setStatus(
        "current"
    )

fsMIPvrstProtocolMigrationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 154, 3, 0, 5)
)
fsMIPvrstProtocolMigrationTrap.setObjects(
      *(("Aricent-MIPVRST-MIB", "fsMIPvrstBrgAddress"),
        ("Aricent-MIPVRST-MIB", "fsMIPvrstContextName"),
        ("Aricent-MIPVRST-MIB", "fsMIPvrstPortMigrationType"))
)
if mibBuilder.loadTexts:
    fsMIPvrstProtocolMigrationTrap.setStatus(
        "current"
    )

fsMIPvrstInvalidBpduRxdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 154, 3, 0, 6)
)
fsMIPvrstInvalidBpduRxdTrap.setObjects(
      *(("Aricent-MIPVRST-MIB", "fsMIPvrstBrgAddress"),
        ("Aricent-MIPVRST-MIB", "fsMIPvrstContextName"),
        ("Aricent-MIPVRST-MIB", "fsMIPvrstPktErrType"),
        ("Aricent-MIPVRST-MIB", "fsMIPvrstPktErrVal"))
)
if mibBuilder.loadTexts:
    fsMIPvrstInvalidBpduRxdTrap.setStatus(
        "current"
    )

fsMIPvrstNewPortRoleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 154, 3, 0, 7)
)
fsMIPvrstNewPortRoleTrap.setObjects(
      *(("Aricent-MIPVRST-MIB", "fsMIPvrstBrgAddress"),
        ("Aricent-MIPVRST-MIB", "fsMIPvrstPortRoleType"),
        ("Aricent-MIPVRST-MIB", "fsMIPvrstOldRoleType"))
)
if mibBuilder.loadTexts:
    fsMIPvrstNewPortRoleTrap.setStatus(
        "current"
    )

fsMIPvrstHwFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 154, 3, 0, 8)
)
fsMIPvrstHwFailureTrap.setObjects(
      *(("Aricent-MIPVRST-MIB", "fsMIPvrstBrgAddress"),
        ("Aricent-MIPVRST-MIB", "fsMIPvrstContextName"),
        ("Aricent-MIPVRST-MIB", "fsMIPvrstInstPortState"))
)
if mibBuilder.loadTexts:
    fsMIPvrstHwFailureTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Aricent-MIPVRST-MIB",
    **{"BridgeId": BridgeId,
       "Timeout": Timeout,
       "EnabledStatus": EnabledStatus,
       "futureMIPvrstMIB": futureMIPvrstMIB,
       "fsMIFuturePvrst": fsMIFuturePvrst,
       "fsMIPvrstGlobalTrace": fsMIPvrstGlobalTrace,
       "fsMIPvrstGlobalDebug": fsMIPvrstGlobalDebug,
       "fsMIFuturePvrstTable": fsMIFuturePvrstTable,
       "fsMIFuturePvrstEntry": fsMIFuturePvrstEntry,
       "fsMIFuturePvrstContextId": fsMIFuturePvrstContextId,
       "fsMIPvrstSystemControl": fsMIPvrstSystemControl,
       "fsMIPvrstModuleStatus": fsMIPvrstModuleStatus,
       "fsMIPvrstNoOfActiveInstances": fsMIPvrstNoOfActiveInstances,
       "fsMIPvrstBrgAddress": fsMIPvrstBrgAddress,
       "fsMIPvrstUpCount": fsMIPvrstUpCount,
       "fsMIPvrstDownCount": fsMIPvrstDownCount,
       "fsMIPvrstPathCostDefaultType": fsMIPvrstPathCostDefaultType,
       "fsMIPvrstDynamicPathCostCalculation": fsMIPvrstDynamicPathCostCalculation,
       "fsMIPvrstTrace": fsMIPvrstTrace,
       "fsMIPvrstDebug": fsMIPvrstDebug,
       "fsMIPvrstBufferOverFlowCount": fsMIPvrstBufferOverFlowCount,
       "fsMIPvrstMemAllocFailureCount": fsMIPvrstMemAllocFailureCount,
       "fsMIPvrstContextName": fsMIPvrstContextName,
       "fsMIPvrstCalcPortPathCostOnSpeedChg": fsMIPvrstCalcPortPathCostOnSpeedChg,
       "fsMIPvrstGlobalBpduGuard": fsMIPvrstGlobalBpduGuard,
       "fsMIPvrstForceProtocolVersion": fsMIPvrstForceProtocolVersion,
       "fsMIFuturePvrstPortTable": fsMIFuturePvrstPortTable,
       "fsMIFuturePvrstPortEntry": fsMIFuturePvrstPortEntry,
       "fsMIPvrstPort": fsMIPvrstPort,
       "fsMIPvrstPortAdminEdgeStatus": fsMIPvrstPortAdminEdgeStatus,
       "fsMIPvrstPortOperEdgePortStatus": fsMIPvrstPortOperEdgePortStatus,
       "fsMIPvrstBridgeDetectionSemState": fsMIPvrstBridgeDetectionSemState,
       "fsMIPvrstPortEnabledStatus": fsMIPvrstPortEnabledStatus,
       "fsMIPvrstRootGuard": fsMIPvrstRootGuard,
       "fsMIPvrstBpduGuard": fsMIPvrstBpduGuard,
       "fsMIPvrstEncapType": fsMIPvrstEncapType,
       "fsMIPvrstPortAdminPointToPoint": fsMIPvrstPortAdminPointToPoint,
       "fsMIPvrstPortOperPointToPoint": fsMIPvrstPortOperPointToPoint,
       "fsMIPvrstPortInvalidBpdusRcvd": fsMIPvrstPortInvalidBpdusRcvd,
       "fsMIPvrstPortInvalidConfigBpduRxCount": fsMIPvrstPortInvalidConfigBpduRxCount,
       "fsMIPvrstPortInvalidTcnBpduRxCount": fsMIPvrstPortInvalidTcnBpduRxCount,
       "fsMIPvrstPortRowStatus": fsMIPvrstPortRowStatus,
       "fsMIPvrstRootInconsistentState": fsMIPvrstRootInconsistentState,
       "fsMIPvrstPortLoopGuard": fsMIPvrstPortLoopGuard,
       "fsMIPvrstPortLoopInconsistentState": fsMIPvrstPortLoopInconsistentState,
       "fsMIPvrstPortEnableBPDURx": fsMIPvrstPortEnableBPDURx,
       "fsMIPvrstPortEnableBPDUTx": fsMIPvrstPortEnableBPDUTx,
       "fsMIPvrstBpduFilter": fsMIPvrstBpduFilter,
       "fsMIPvrstPortAutoEdge": fsMIPvrstPortAutoEdge,
       "fsMIPvrstPortBpduInconsistentState": fsMIPvrstPortBpduInconsistentState,
       "fsMIPvrstPortTypeInconsistentState": fsMIPvrstPortTypeInconsistentState,
       "fsMIPvrstPortPVIDInconsistentState": fsMIPvrstPortPVIDInconsistentState,
       "fsMIPvrstPortBpduGuardAction": fsMIPvrstPortBpduGuardAction,
       "fsMIPvrstInstBridgeTable": fsMIPvrstInstBridgeTable,
       "fsMIPvrstInstBridgeEntry": fsMIPvrstInstBridgeEntry,
       "fsMIPvrstInstVlanId": fsMIPvrstInstVlanId,
       "fsMIPvrstInstBridgePriority": fsMIPvrstInstBridgePriority,
       "fsMIPvrstInstRootCost": fsMIPvrstInstRootCost,
       "fsMIPvrstInstRootPort": fsMIPvrstInstRootPort,
       "fsMIPvrstInstBridgeMaxAge": fsMIPvrstInstBridgeMaxAge,
       "fsMIPvrstInstBridgeHelloTime": fsMIPvrstInstBridgeHelloTime,
       "fsMIPvrstInstBridgeForwardDelay": fsMIPvrstInstBridgeForwardDelay,
       "fsMIPvrstInstHoldTime": fsMIPvrstInstHoldTime,
       "fsMIPvrstInstTxHoldCount": fsMIPvrstInstTxHoldCount,
       "fsMIPvrstInstTimeSinceTopologyChange": fsMIPvrstInstTimeSinceTopologyChange,
       "fsMIPvrstInstTopChanges": fsMIPvrstInstTopChanges,
       "fsMIPvrstInstNewRootCount": fsMIPvrstInstNewRootCount,
       "fsMIPvrstInstInstanceUpCount": fsMIPvrstInstInstanceUpCount,
       "fsMIPvrstInstInstanceDownCount": fsMIPvrstInstInstanceDownCount,
       "fsMIPvrstInstPortRoleSelSemState": fsMIPvrstInstPortRoleSelSemState,
       "fsMIPvrstInstDesignatedRoot": fsMIPvrstInstDesignatedRoot,
       "fsMIPvrstInstRootMaxAge": fsMIPvrstInstRootMaxAge,
       "fsMIPvrstInstRootHelloTime": fsMIPvrstInstRootHelloTime,
       "fsMIPvrstInstRootForwardDelay": fsMIPvrstInstRootForwardDelay,
       "fsMIPvrstInstPortTable": fsMIPvrstInstPortTable,
       "fsMIPvrstInstPortEntry": fsMIPvrstInstPortEntry,
       "fsMIPvrstInstPortIndex": fsMIPvrstInstPortIndex,
       "fsMIPvrstInstPortEnableStatus": fsMIPvrstInstPortEnableStatus,
       "fsMIPvrstInstPortPathCost": fsMIPvrstInstPortPathCost,
       "fsMIPvrstInstPortPriority": fsMIPvrstInstPortPriority,
       "fsMIPvrstInstPortDesignatedRoot": fsMIPvrstInstPortDesignatedRoot,
       "fsMIPvrstInstPortDesignatedBridge": fsMIPvrstInstPortDesignatedBridge,
       "fsMIPvrstInstPortDesignatedPort": fsMIPvrstInstPortDesignatedPort,
       "fsMIPvrstInstPortOperVersion": fsMIPvrstInstPortOperVersion,
       "fsMIPvrstInstPortProtocolMigration": fsMIPvrstInstPortProtocolMigration,
       "fsMIPvrstInstPortState": fsMIPvrstInstPortState,
       "fsMIPvrstInstPortForwardTransitions": fsMIPvrstInstPortForwardTransitions,
       "fsMIPvrstInstPortReceivedBpdus": fsMIPvrstInstPortReceivedBpdus,
       "fsMIPvrstInstPortRxConfigBpduCount": fsMIPvrstInstPortRxConfigBpduCount,
       "fsMIPvrstInstPortRxTcnBpduCount": fsMIPvrstInstPortRxTcnBpduCount,
       "fsMIPvrstInstPortTransmittedBpdus": fsMIPvrstInstPortTransmittedBpdus,
       "fsMIPvrstInstPortTxConfigBpduCount": fsMIPvrstInstPortTxConfigBpduCount,
       "fsMIPvrstInstPortTxTcnBpduCount": fsMIPvrstInstPortTxTcnBpduCount,
       "fsMIPvrstInstPortTxSemState": fsMIPvrstInstPortTxSemState,
       "fsMIPvrstInstPortProtMigrationSemState": fsMIPvrstInstPortProtMigrationSemState,
       "fsMIPvrstInstProtocolMigrationCount": fsMIPvrstInstProtocolMigrationCount,
       "fsMIPvrstInstPortRole": fsMIPvrstInstPortRole,
       "fsMIPvrstInstCurrentPortRole": fsMIPvrstInstCurrentPortRole,
       "fsMIPvrstInstPortInfoSemState": fsMIPvrstInstPortInfoSemState,
       "fsMIPvrstInstPortRoleTransitionSemState": fsMIPvrstInstPortRoleTransitionSemState,
       "fsMIPvrstInstPortStateTransitionSemState": fsMIPvrstInstPortStateTransitionSemState,
       "fsMIPvrstInstPortTopologyChangeSemState": fsMIPvrstInstPortTopologyChangeSemState,
       "fsMIPvrstInstPortEffectivePortState": fsMIPvrstInstPortEffectivePortState,
       "fsMIPvrstInstPortHelloTime": fsMIPvrstInstPortHelloTime,
       "fsMIPvrstInstPortMaxAge": fsMIPvrstInstPortMaxAge,
       "fsMIPvrstInstPortForwardDelay": fsMIPvrstInstPortForwardDelay,
       "fsMIPvrstInstPortHoldTime": fsMIPvrstInstPortHoldTime,
       "fsMIPvrstInstPortAdminPathCost": fsMIPvrstInstPortAdminPathCost,
       "fsMIFsPvrstTrapsControl": fsMIFsPvrstTrapsControl,
       "fsMIFsPvrstSetGlobalTrapOption": fsMIFsPvrstSetGlobalTrapOption,
       "fsMIPvrstGlobalErrTrapType": fsMIPvrstGlobalErrTrapType,
       "fsMIFsPvrstTrapsControlTable": fsMIFsPvrstTrapsControlTable,
       "fsMIFsPvrstTrapsControlEntry": fsMIFsPvrstTrapsControlEntry,
       "fsMIPvrstSetTraps": fsMIPvrstSetTraps,
       "fsMIPvrstGenTrapType": fsMIPvrstGenTrapType,
       "fsMIPvrstPortTrapNotificationTable": fsMIPvrstPortTrapNotificationTable,
       "fsMIPvrstPortTrapNotificationEntry": fsMIPvrstPortTrapNotificationEntry,
       "fsMIPvrstPortTrapIndex": fsMIPvrstPortTrapIndex,
       "fsMIPvrstPortMigrationType": fsMIPvrstPortMigrationType,
       "fsMIPvrstPktErrType": fsMIPvrstPktErrType,
       "fsMIPvrstPktErrVal": fsMIPvrstPktErrVal,
       "fsMIPvrstPortRoleTrapNotificationTable": fsMIPvrstPortRoleTrapNotificationTable,
       "fsMIPvrstPortRoleTrapNotificationEntry": fsMIPvrstPortRoleTrapNotificationEntry,
       "fsMIPvrstPortRoleType": fsMIPvrstPortRoleType,
       "fsMIPvrstOldRoleType": fsMIPvrstOldRoleType,
       "fsMIFuturePvrstTraps": fsMIFuturePvrstTraps,
       "fsMIPvrstTraps": fsMIPvrstTraps,
       "fsMIPvrstGlobalErrTrap": fsMIPvrstGlobalErrTrap,
       "fsMIPvrstGenTrap": fsMIPvrstGenTrap,
       "fsMIPvrstNewRootTrap": fsMIPvrstNewRootTrap,
       "fsMIPvrstTopologyChgTrap": fsMIPvrstTopologyChgTrap,
       "fsMIPvrstProtocolMigrationTrap": fsMIPvrstProtocolMigrationTrap,
       "fsMIPvrstInvalidBpduRxdTrap": fsMIPvrstInvalidBpduRxdTrap,
       "fsMIPvrstNewPortRoleTrap": fsMIPvrstNewPortRoleTrap,
       "fsMIPvrstHwFailureTrap": fsMIPvrstHwFailureTrap}
)
