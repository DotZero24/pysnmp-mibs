# SNMP MIB module (ARICENT-PB-RSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-PB-RSTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:38 2025
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

(BridgeId,
 Timeout) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

futurePbRstMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 123)
)
if mibBuilder.loadTexts:
    futurePbRstMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



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



class VlanId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )



# MIB Managed Objects in the order of their OIDs

_FuturePbRst_ObjectIdentity = ObjectIdentity
futurePbRst = _FuturePbRst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1)
)
_FsPbProviderStpStatus_Type = EnabledStatus
_FsPbProviderStpStatus_Object = MibScalar
fsPbProviderStpStatus = _FsPbProviderStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 1),
    _FsPbProviderStpStatus_Type()
)
fsPbProviderStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbProviderStpStatus.setStatus("current")
_FsPbRstCVlanBridgeTable_Object = MibTable
fsPbRstCVlanBridgeTable = _FsPbRstCVlanBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 2)
)
if mibBuilder.loadTexts:
    fsPbRstCVlanBridgeTable.setStatus("current")
_FsPbRstCVlanBridgeEntry_Object = MibTableRow
fsPbRstCVlanBridgeEntry = _FsPbRstCVlanBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 2, 1)
)
fsPbRstCVlanBridgeEntry.setIndexNames(
    (0, "ARICENT-PB-RSTP-MIB", "fsPbRstPort"),
)
if mibBuilder.loadTexts:
    fsPbRstCVlanBridgeEntry.setStatus("current")


class _FsPbRstPort_Type(Integer32):
    """Custom type fsPbRstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPbRstPort_Type.__name__ = "Integer32"
_FsPbRstPort_Object = MibTableColumn
fsPbRstPort = _FsPbRstPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 2, 1, 1),
    _FsPbRstPort_Type()
)
fsPbRstPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbRstPort.setStatus("current")
_FsPbRstCVlanBridgeId_Type = BridgeId
_FsPbRstCVlanBridgeId_Object = MibTableColumn
fsPbRstCVlanBridgeId = _FsPbRstCVlanBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 2, 1, 2),
    _FsPbRstCVlanBridgeId_Type()
)
fsPbRstCVlanBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanBridgeId.setStatus("current")
_FsPbRstCVlanBridgeDesignatedRoot_Type = BridgeId
_FsPbRstCVlanBridgeDesignatedRoot_Object = MibTableColumn
fsPbRstCVlanBridgeDesignatedRoot = _FsPbRstCVlanBridgeDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 2, 1, 3),
    _FsPbRstCVlanBridgeDesignatedRoot_Type()
)
fsPbRstCVlanBridgeDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanBridgeDesignatedRoot.setStatus("current")
_FsPbRstCVlanBridgeRootCost_Type = Integer32
_FsPbRstCVlanBridgeRootCost_Object = MibTableColumn
fsPbRstCVlanBridgeRootCost = _FsPbRstCVlanBridgeRootCost_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 2, 1, 4),
    _FsPbRstCVlanBridgeRootCost_Type()
)
fsPbRstCVlanBridgeRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanBridgeRootCost.setStatus("current")
_FsPbRstCVlanBridgeMaxAge_Type = Timeout
_FsPbRstCVlanBridgeMaxAge_Object = MibTableColumn
fsPbRstCVlanBridgeMaxAge = _FsPbRstCVlanBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 2, 1, 5),
    _FsPbRstCVlanBridgeMaxAge_Type()
)
fsPbRstCVlanBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanBridgeMaxAge.setStatus("current")
_FsPbRstCVlanBridgeHelloTime_Type = Timeout
_FsPbRstCVlanBridgeHelloTime_Object = MibTableColumn
fsPbRstCVlanBridgeHelloTime = _FsPbRstCVlanBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 2, 1, 6),
    _FsPbRstCVlanBridgeHelloTime_Type()
)
fsPbRstCVlanBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanBridgeHelloTime.setStatus("current")
_FsPbRstCVlanBridgeHoldTime_Type = Integer32
_FsPbRstCVlanBridgeHoldTime_Object = MibTableColumn
fsPbRstCVlanBridgeHoldTime = _FsPbRstCVlanBridgeHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 2, 1, 7),
    _FsPbRstCVlanBridgeHoldTime_Type()
)
fsPbRstCVlanBridgeHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanBridgeHoldTime.setStatus("current")
_FsPbRstCVlanBridgeForwardDelay_Type = Timeout
_FsPbRstCVlanBridgeForwardDelay_Object = MibTableColumn
fsPbRstCVlanBridgeForwardDelay = _FsPbRstCVlanBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 2, 1, 8),
    _FsPbRstCVlanBridgeForwardDelay_Type()
)
fsPbRstCVlanBridgeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanBridgeForwardDelay.setStatus("current")
_FsPbRstCVlanBridgeTxHoldCount_Type = Integer32
_FsPbRstCVlanBridgeTxHoldCount_Object = MibTableColumn
fsPbRstCVlanBridgeTxHoldCount = _FsPbRstCVlanBridgeTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 2, 1, 9),
    _FsPbRstCVlanBridgeTxHoldCount_Type()
)
fsPbRstCVlanBridgeTxHoldCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanBridgeTxHoldCount.setStatus("current")
_FsPbRstCVlanStpHelloTime_Type = Timeout
_FsPbRstCVlanStpHelloTime_Object = MibTableColumn
fsPbRstCVlanStpHelloTime = _FsPbRstCVlanStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 2, 1, 10),
    _FsPbRstCVlanStpHelloTime_Type()
)
fsPbRstCVlanStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanStpHelloTime.setStatus("current")
_FsPbRstCVlanStpMaxAge_Type = Timeout
_FsPbRstCVlanStpMaxAge_Object = MibTableColumn
fsPbRstCVlanStpMaxAge = _FsPbRstCVlanStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 2, 1, 11),
    _FsPbRstCVlanStpMaxAge_Type()
)
fsPbRstCVlanStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanStpMaxAge.setStatus("current")
_FsPbRstCVlanStpForwardDelay_Type = Timeout
_FsPbRstCVlanStpForwardDelay_Object = MibTableColumn
fsPbRstCVlanStpForwardDelay = _FsPbRstCVlanStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 2, 1, 12),
    _FsPbRstCVlanStpForwardDelay_Type()
)
fsPbRstCVlanStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanStpForwardDelay.setStatus("current")
_FsPbRstCVlanStpTopChanges_Type = Counter32
_FsPbRstCVlanStpTopChanges_Object = MibTableColumn
fsPbRstCVlanStpTopChanges = _FsPbRstCVlanStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 2, 1, 13),
    _FsPbRstCVlanStpTopChanges_Type()
)
fsPbRstCVlanStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanStpTopChanges.setStatus("current")
_FsPbRstCVlanStpTimeSinceTopologyChange_Type = TimeTicks
_FsPbRstCVlanStpTimeSinceTopologyChange_Object = MibTableColumn
fsPbRstCVlanStpTimeSinceTopologyChange = _FsPbRstCVlanStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 2, 1, 14),
    _FsPbRstCVlanStpTimeSinceTopologyChange_Type()
)
fsPbRstCVlanStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanStpTimeSinceTopologyChange.setStatus("current")
_FsPbRstCVlanPortInfoTable_Object = MibTable
fsPbRstCVlanPortInfoTable = _FsPbRstCVlanPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 3)
)
if mibBuilder.loadTexts:
    fsPbRstCVlanPortInfoTable.setStatus("current")
_FsPbRstCVlanPortInfoEntry_Object = MibTableRow
fsPbRstCVlanPortInfoEntry = _FsPbRstCVlanPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 3, 1)
)
fsPbRstCVlanPortInfoEntry.setIndexNames(
    (0, "ARICENT-PB-RSTP-MIB", "fsPbRstPort"),
    (0, "ARICENT-PB-RSTP-MIB", "fsPbRstCepSvid"),
)
if mibBuilder.loadTexts:
    fsPbRstCVlanPortInfoEntry.setStatus("current")
_FsPbRstCepSvid_Type = VlanId
_FsPbRstCepSvid_Object = MibTableColumn
fsPbRstCepSvid = _FsPbRstCepSvid_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 3, 1, 1),
    _FsPbRstCepSvid_Type()
)
fsPbRstCepSvid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbRstCepSvid.setStatus("current")


class _FsPbRstCVlanPortPriority_Type(Integer32):
    """Custom type fsPbRstCVlanPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPbRstCVlanPortPriority_Type.__name__ = "Integer32"
_FsPbRstCVlanPortPriority_Object = MibTableColumn
fsPbRstCVlanPortPriority = _FsPbRstCVlanPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 3, 1, 2),
    _FsPbRstCVlanPortPriority_Type()
)
fsPbRstCVlanPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortPriority.setStatus("current")


class _FsPbRstCVlanPortPathCost_Type(Integer32):
    """Custom type fsPbRstCVlanPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsPbRstCVlanPortPathCost_Type.__name__ = "Integer32"
_FsPbRstCVlanPortPathCost_Object = MibTableColumn
fsPbRstCVlanPortPathCost = _FsPbRstCVlanPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 3, 1, 3),
    _FsPbRstCVlanPortPathCost_Type()
)
fsPbRstCVlanPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortPathCost.setStatus("current")


class _FsPbRstCVlanPortRole_Type(Integer32):
    """Custom type fsPbRstCVlanPortRole based on Integer32"""
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


_FsPbRstCVlanPortRole_Type.__name__ = "Integer32"
_FsPbRstCVlanPortRole_Object = MibTableColumn
fsPbRstCVlanPortRole = _FsPbRstCVlanPortRole_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 3, 1, 4),
    _FsPbRstCVlanPortRole_Type()
)
fsPbRstCVlanPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortRole.setStatus("current")


class _FsPbRstCVlanPortState_Type(Integer32):
    """Custom type fsPbRstCVlanPortState based on Integer32"""
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
        *(("disabled", 1),
          ("blocking", 2),
          ("listening", 3),
          ("learning", 4),
          ("forwarding", 5),
          ("broken", 6))
    )


_FsPbRstCVlanPortState_Type.__name__ = "Integer32"
_FsPbRstCVlanPortState_Object = MibTableColumn
fsPbRstCVlanPortState = _FsPbRstCVlanPortState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 3, 1, 5),
    _FsPbRstCVlanPortState_Type()
)
fsPbRstCVlanPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortState.setStatus("current")
_FsPbRstCVlanPortAdminEdgePort_Type = TruthValue
_FsPbRstCVlanPortAdminEdgePort_Object = MibTableColumn
fsPbRstCVlanPortAdminEdgePort = _FsPbRstCVlanPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 3, 1, 6),
    _FsPbRstCVlanPortAdminEdgePort_Type()
)
fsPbRstCVlanPortAdminEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortAdminEdgePort.setStatus("current")
_FsPbRstCVlanPortOperEdgePort_Type = TruthValue
_FsPbRstCVlanPortOperEdgePort_Object = MibTableColumn
fsPbRstCVlanPortOperEdgePort = _FsPbRstCVlanPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 3, 1, 7),
    _FsPbRstCVlanPortOperEdgePort_Type()
)
fsPbRstCVlanPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortOperEdgePort.setStatus("current")


class _FsPbRstCVlanPortAdminPointToPoint_Type(Integer32):
    """Custom type fsPbRstCVlanPortAdminPointToPoint based on Integer32"""
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


_FsPbRstCVlanPortAdminPointToPoint_Type.__name__ = "Integer32"
_FsPbRstCVlanPortAdminPointToPoint_Object = MibTableColumn
fsPbRstCVlanPortAdminPointToPoint = _FsPbRstCVlanPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 3, 1, 8),
    _FsPbRstCVlanPortAdminPointToPoint_Type()
)
fsPbRstCVlanPortAdminPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortAdminPointToPoint.setStatus("current")
_FsPbRstCVlanPortOperPointToPoint_Type = TruthValue
_FsPbRstCVlanPortOperPointToPoint_Object = MibTableColumn
fsPbRstCVlanPortOperPointToPoint = _FsPbRstCVlanPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 3, 1, 9),
    _FsPbRstCVlanPortOperPointToPoint_Type()
)
fsPbRstCVlanPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortOperPointToPoint.setStatus("current")
_FsPbRstCVlanPortAutoEdge_Type = TruthValue
_FsPbRstCVlanPortAutoEdge_Object = MibTableColumn
fsPbRstCVlanPortAutoEdge = _FsPbRstCVlanPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 3, 1, 10),
    _FsPbRstCVlanPortAutoEdge_Type()
)
fsPbRstCVlanPortAutoEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortAutoEdge.setStatus("current")
_FsPbRstCVlanPortDesignatedRoot_Type = BridgeId
_FsPbRstCVlanPortDesignatedRoot_Object = MibTableColumn
fsPbRstCVlanPortDesignatedRoot = _FsPbRstCVlanPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 3, 1, 11),
    _FsPbRstCVlanPortDesignatedRoot_Type()
)
fsPbRstCVlanPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortDesignatedRoot.setStatus("current")
_FsPbRstCVlanPortDesignatedCost_Type = Integer32
_FsPbRstCVlanPortDesignatedCost_Object = MibTableColumn
fsPbRstCVlanPortDesignatedCost = _FsPbRstCVlanPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 3, 1, 12),
    _FsPbRstCVlanPortDesignatedCost_Type()
)
fsPbRstCVlanPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortDesignatedCost.setStatus("current")
_FsPbRstCVlanPortDesignatedBridge_Type = BridgeId
_FsPbRstCVlanPortDesignatedBridge_Object = MibTableColumn
fsPbRstCVlanPortDesignatedBridge = _FsPbRstCVlanPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 3, 1, 13),
    _FsPbRstCVlanPortDesignatedBridge_Type()
)
fsPbRstCVlanPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortDesignatedBridge.setStatus("current")


class _FsPbRstCVlanPortDesignatedPort_Type(OctetString):
    """Custom type fsPbRstCVlanPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_FsPbRstCVlanPortDesignatedPort_Type.__name__ = "OctetString"
_FsPbRstCVlanPortDesignatedPort_Object = MibTableColumn
fsPbRstCVlanPortDesignatedPort = _FsPbRstCVlanPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 3, 1, 14),
    _FsPbRstCVlanPortDesignatedPort_Type()
)
fsPbRstCVlanPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortDesignatedPort.setStatus("current")
_FsPbRstCVlanPortForwardTransitions_Type = Counter32
_FsPbRstCVlanPortForwardTransitions_Object = MibTableColumn
fsPbRstCVlanPortForwardTransitions = _FsPbRstCVlanPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 3, 1, 15),
    _FsPbRstCVlanPortForwardTransitions_Type()
)
fsPbRstCVlanPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortForwardTransitions.setStatus("current")
_FsPbRstCVlanPortSmTable_Object = MibTable
fsPbRstCVlanPortSmTable = _FsPbRstCVlanPortSmTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 4)
)
if mibBuilder.loadTexts:
    fsPbRstCVlanPortSmTable.setStatus("current")
_FsPbRstCVlanPortSmEntry_Object = MibTableRow
fsPbRstCVlanPortSmEntry = _FsPbRstCVlanPortSmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 4, 1)
)
fsPbRstCVlanPortSmEntry.setIndexNames(
    (0, "ARICENT-PB-RSTP-MIB", "fsPbRstPort"),
    (0, "ARICENT-PB-RSTP-MIB", "fsPbRstCepSvid"),
)
if mibBuilder.loadTexts:
    fsPbRstCVlanPortSmEntry.setStatus("current")


class _FsPbRstCVlanPortInfoSmState_Type(Integer32):
    """Custom type fsPbRstCVlanPortInfoSmState based on Integer32"""
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
        *(("disabled", 0),
          ("aged", 1),
          ("update", 2),
          ("superior", 3),
          ("repeat", 4),
          ("notdesignated", 5),
          ("present", 6),
          ("receive", 7),
          ("inferiordesignated", 8))
    )


_FsPbRstCVlanPortInfoSmState_Type.__name__ = "Integer32"
_FsPbRstCVlanPortInfoSmState_Object = MibTableColumn
fsPbRstCVlanPortInfoSmState = _FsPbRstCVlanPortInfoSmState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 4, 1, 1),
    _FsPbRstCVlanPortInfoSmState_Type()
)
fsPbRstCVlanPortInfoSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortInfoSmState.setStatus("current")


class _FsPbRstCVlanPortMigSmState_Type(Integer32):
    """Custom type fsPbRstCVlanPortMigSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("checkingrstp", 0),
          ("selectingstp", 1),
          ("sensing", 2))
    )


_FsPbRstCVlanPortMigSmState_Type.__name__ = "Integer32"
_FsPbRstCVlanPortMigSmState_Object = MibTableColumn
fsPbRstCVlanPortMigSmState = _FsPbRstCVlanPortMigSmState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 4, 1, 2),
    _FsPbRstCVlanPortMigSmState_Type()
)
fsPbRstCVlanPortMigSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortMigSmState.setStatus("current")


class _FsPbRstCVlanPortRoleTransSmState_Type(Integer32):
    """Custom type fsPbRstCVlanPortRoleTransSmState based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("init", 0),
          ("disableport", 1),
          ("disabledport", 2),
          ("rootport", 3),
          ("designatedport", 4),
          ("backupport", 5),
          ("rootproposed", 6),
          ("rootagreed", 7),
          ("reroot", 8),
          ("rootforward", 9),
          ("rootlearn", 10),
          ("rerooted", 11),
          ("designatedpropose", 12),
          ("designatedsynced", 13),
          ("designatedretired", 14),
          ("designatedforward", 15),
          ("designatedlearn", 16),
          ("designatedlisten", 17))
    )


_FsPbRstCVlanPortRoleTransSmState_Type.__name__ = "Integer32"
_FsPbRstCVlanPortRoleTransSmState_Object = MibTableColumn
fsPbRstCVlanPortRoleTransSmState = _FsPbRstCVlanPortRoleTransSmState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 4, 1, 3),
    _FsPbRstCVlanPortRoleTransSmState_Type()
)
fsPbRstCVlanPortRoleTransSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortRoleTransSmState.setStatus("current")


class _FsPbRstCVlanPortStateTransSmState_Type(Integer32):
    """Custom type fsPbRstCVlanPortStateTransSmState based on Integer32"""
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


_FsPbRstCVlanPortStateTransSmState_Type.__name__ = "Integer32"
_FsPbRstCVlanPortStateTransSmState_Object = MibTableColumn
fsPbRstCVlanPortStateTransSmState = _FsPbRstCVlanPortStateTransSmState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 4, 1, 4),
    _FsPbRstCVlanPortStateTransSmState_Type()
)
fsPbRstCVlanPortStateTransSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortStateTransSmState.setStatus("current")


class _FsPbRstCVlanPortTopoChSmState_Type(Integer32):
    """Custom type fsPbRstCVlanPortTopoChSmState based on Integer32"""
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


_FsPbRstCVlanPortTopoChSmState_Type.__name__ = "Integer32"
_FsPbRstCVlanPortTopoChSmState_Object = MibTableColumn
fsPbRstCVlanPortTopoChSmState = _FsPbRstCVlanPortTopoChSmState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 4, 1, 5),
    _FsPbRstCVlanPortTopoChSmState_Type()
)
fsPbRstCVlanPortTopoChSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortTopoChSmState.setStatus("current")


class _FsPbRstCVlanPortTxSmState_Type(Integer32):
    """Custom type fsPbRstCVlanPortTxSmState based on Integer32"""
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


_FsPbRstCVlanPortTxSmState_Type.__name__ = "Integer32"
_FsPbRstCVlanPortTxSmState_Object = MibTableColumn
fsPbRstCVlanPortTxSmState = _FsPbRstCVlanPortTxSmState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 4, 1, 6),
    _FsPbRstCVlanPortTxSmState_Type()
)
fsPbRstCVlanPortTxSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortTxSmState.setStatus("current")
_FsPbRstCVlanPortStatsTable_Object = MibTable
fsPbRstCVlanPortStatsTable = _FsPbRstCVlanPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 5)
)
if mibBuilder.loadTexts:
    fsPbRstCVlanPortStatsTable.setStatus("current")
_FsPbRstCVlanPortStatsEntry_Object = MibTableRow
fsPbRstCVlanPortStatsEntry = _FsPbRstCVlanPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 5, 1)
)
fsPbRstCVlanPortStatsEntry.setIndexNames(
    (0, "ARICENT-PB-RSTP-MIB", "fsPbRstPort"),
    (0, "ARICENT-PB-RSTP-MIB", "fsPbRstCepSvid"),
)
if mibBuilder.loadTexts:
    fsPbRstCVlanPortStatsEntry.setStatus("current")
_FsPbRstCVlanPortRxRstBpduCount_Type = Counter32
_FsPbRstCVlanPortRxRstBpduCount_Object = MibTableColumn
fsPbRstCVlanPortRxRstBpduCount = _FsPbRstCVlanPortRxRstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 5, 1, 1),
    _FsPbRstCVlanPortRxRstBpduCount_Type()
)
fsPbRstCVlanPortRxRstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortRxRstBpduCount.setStatus("current")
_FsPbRstCVlanPortRxConfigBpduCount_Type = Counter32
_FsPbRstCVlanPortRxConfigBpduCount_Object = MibTableColumn
fsPbRstCVlanPortRxConfigBpduCount = _FsPbRstCVlanPortRxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 5, 1, 2),
    _FsPbRstCVlanPortRxConfigBpduCount_Type()
)
fsPbRstCVlanPortRxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortRxConfigBpduCount.setStatus("current")
_FsPbRstCVlanPortRxTcnBpduCount_Type = Counter32
_FsPbRstCVlanPortRxTcnBpduCount_Object = MibTableColumn
fsPbRstCVlanPortRxTcnBpduCount = _FsPbRstCVlanPortRxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 5, 1, 3),
    _FsPbRstCVlanPortRxTcnBpduCount_Type()
)
fsPbRstCVlanPortRxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortRxTcnBpduCount.setStatus("current")
_FsPbRstCVlanPortTxRstBpduCount_Type = Counter32
_FsPbRstCVlanPortTxRstBpduCount_Object = MibTableColumn
fsPbRstCVlanPortTxRstBpduCount = _FsPbRstCVlanPortTxRstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 5, 1, 4),
    _FsPbRstCVlanPortTxRstBpduCount_Type()
)
fsPbRstCVlanPortTxRstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortTxRstBpduCount.setStatus("current")
_FsPbRstCVlanPortTxConfigBpduCount_Type = Counter32
_FsPbRstCVlanPortTxConfigBpduCount_Object = MibTableColumn
fsPbRstCVlanPortTxConfigBpduCount = _FsPbRstCVlanPortTxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 5, 1, 5),
    _FsPbRstCVlanPortTxConfigBpduCount_Type()
)
fsPbRstCVlanPortTxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortTxConfigBpduCount.setStatus("current")
_FsPbRstCVlanPortTxTcnBpduCount_Type = Counter32
_FsPbRstCVlanPortTxTcnBpduCount_Object = MibTableColumn
fsPbRstCVlanPortTxTcnBpduCount = _FsPbRstCVlanPortTxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 5, 1, 6),
    _FsPbRstCVlanPortTxTcnBpduCount_Type()
)
fsPbRstCVlanPortTxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortTxTcnBpduCount.setStatus("current")
_FsPbRstCVlanPortInvalidRstBpduRxCount_Type = Counter32
_FsPbRstCVlanPortInvalidRstBpduRxCount_Object = MibTableColumn
fsPbRstCVlanPortInvalidRstBpduRxCount = _FsPbRstCVlanPortInvalidRstBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 5, 1, 7),
    _FsPbRstCVlanPortInvalidRstBpduRxCount_Type()
)
fsPbRstCVlanPortInvalidRstBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortInvalidRstBpduRxCount.setStatus("current")
_FsPbRstCVlanPortInvalidConfigBpduRxCount_Type = Counter32
_FsPbRstCVlanPortInvalidConfigBpduRxCount_Object = MibTableColumn
fsPbRstCVlanPortInvalidConfigBpduRxCount = _FsPbRstCVlanPortInvalidConfigBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 5, 1, 8),
    _FsPbRstCVlanPortInvalidConfigBpduRxCount_Type()
)
fsPbRstCVlanPortInvalidConfigBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortInvalidConfigBpduRxCount.setStatus("current")
_FsPbRstCVlanPortInvalidTcnBpduRxCount_Type = Counter32
_FsPbRstCVlanPortInvalidTcnBpduRxCount_Object = MibTableColumn
fsPbRstCVlanPortInvalidTcnBpduRxCount = _FsPbRstCVlanPortInvalidTcnBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 5, 1, 9),
    _FsPbRstCVlanPortInvalidTcnBpduRxCount_Type()
)
fsPbRstCVlanPortInvalidTcnBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortInvalidTcnBpduRxCount.setStatus("current")
_FsPbRstCVlanPortProtocolMigrationCount_Type = Counter32
_FsPbRstCVlanPortProtocolMigrationCount_Object = MibTableColumn
fsPbRstCVlanPortProtocolMigrationCount = _FsPbRstCVlanPortProtocolMigrationCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 5, 1, 10),
    _FsPbRstCVlanPortProtocolMigrationCount_Type()
)
fsPbRstCVlanPortProtocolMigrationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortProtocolMigrationCount.setStatus("current")
_FsPbRstCVlanPortEffectivePortState_Type = TruthValue
_FsPbRstCVlanPortEffectivePortState_Object = MibTableColumn
fsPbRstCVlanPortEffectivePortState = _FsPbRstCVlanPortEffectivePortState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 123, 1, 5, 1, 11),
    _FsPbRstCVlanPortEffectivePortState_Type()
)
fsPbRstCVlanPortEffectivePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbRstCVlanPortEffectivePortState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-PB-RSTP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "VlanId": VlanId,
       "futurePbRstMIB": futurePbRstMIB,
       "futurePbRst": futurePbRst,
       "fsPbProviderStpStatus": fsPbProviderStpStatus,
       "fsPbRstCVlanBridgeTable": fsPbRstCVlanBridgeTable,
       "fsPbRstCVlanBridgeEntry": fsPbRstCVlanBridgeEntry,
       "fsPbRstPort": fsPbRstPort,
       "fsPbRstCVlanBridgeId": fsPbRstCVlanBridgeId,
       "fsPbRstCVlanBridgeDesignatedRoot": fsPbRstCVlanBridgeDesignatedRoot,
       "fsPbRstCVlanBridgeRootCost": fsPbRstCVlanBridgeRootCost,
       "fsPbRstCVlanBridgeMaxAge": fsPbRstCVlanBridgeMaxAge,
       "fsPbRstCVlanBridgeHelloTime": fsPbRstCVlanBridgeHelloTime,
       "fsPbRstCVlanBridgeHoldTime": fsPbRstCVlanBridgeHoldTime,
       "fsPbRstCVlanBridgeForwardDelay": fsPbRstCVlanBridgeForwardDelay,
       "fsPbRstCVlanBridgeTxHoldCount": fsPbRstCVlanBridgeTxHoldCount,
       "fsPbRstCVlanStpHelloTime": fsPbRstCVlanStpHelloTime,
       "fsPbRstCVlanStpMaxAge": fsPbRstCVlanStpMaxAge,
       "fsPbRstCVlanStpForwardDelay": fsPbRstCVlanStpForwardDelay,
       "fsPbRstCVlanStpTopChanges": fsPbRstCVlanStpTopChanges,
       "fsPbRstCVlanStpTimeSinceTopologyChange": fsPbRstCVlanStpTimeSinceTopologyChange,
       "fsPbRstCVlanPortInfoTable": fsPbRstCVlanPortInfoTable,
       "fsPbRstCVlanPortInfoEntry": fsPbRstCVlanPortInfoEntry,
       "fsPbRstCepSvid": fsPbRstCepSvid,
       "fsPbRstCVlanPortPriority": fsPbRstCVlanPortPriority,
       "fsPbRstCVlanPortPathCost": fsPbRstCVlanPortPathCost,
       "fsPbRstCVlanPortRole": fsPbRstCVlanPortRole,
       "fsPbRstCVlanPortState": fsPbRstCVlanPortState,
       "fsPbRstCVlanPortAdminEdgePort": fsPbRstCVlanPortAdminEdgePort,
       "fsPbRstCVlanPortOperEdgePort": fsPbRstCVlanPortOperEdgePort,
       "fsPbRstCVlanPortAdminPointToPoint": fsPbRstCVlanPortAdminPointToPoint,
       "fsPbRstCVlanPortOperPointToPoint": fsPbRstCVlanPortOperPointToPoint,
       "fsPbRstCVlanPortAutoEdge": fsPbRstCVlanPortAutoEdge,
       "fsPbRstCVlanPortDesignatedRoot": fsPbRstCVlanPortDesignatedRoot,
       "fsPbRstCVlanPortDesignatedCost": fsPbRstCVlanPortDesignatedCost,
       "fsPbRstCVlanPortDesignatedBridge": fsPbRstCVlanPortDesignatedBridge,
       "fsPbRstCVlanPortDesignatedPort": fsPbRstCVlanPortDesignatedPort,
       "fsPbRstCVlanPortForwardTransitions": fsPbRstCVlanPortForwardTransitions,
       "fsPbRstCVlanPortSmTable": fsPbRstCVlanPortSmTable,
       "fsPbRstCVlanPortSmEntry": fsPbRstCVlanPortSmEntry,
       "fsPbRstCVlanPortInfoSmState": fsPbRstCVlanPortInfoSmState,
       "fsPbRstCVlanPortMigSmState": fsPbRstCVlanPortMigSmState,
       "fsPbRstCVlanPortRoleTransSmState": fsPbRstCVlanPortRoleTransSmState,
       "fsPbRstCVlanPortStateTransSmState": fsPbRstCVlanPortStateTransSmState,
       "fsPbRstCVlanPortTopoChSmState": fsPbRstCVlanPortTopoChSmState,
       "fsPbRstCVlanPortTxSmState": fsPbRstCVlanPortTxSmState,
       "fsPbRstCVlanPortStatsTable": fsPbRstCVlanPortStatsTable,
       "fsPbRstCVlanPortStatsEntry": fsPbRstCVlanPortStatsEntry,
       "fsPbRstCVlanPortRxRstBpduCount": fsPbRstCVlanPortRxRstBpduCount,
       "fsPbRstCVlanPortRxConfigBpduCount": fsPbRstCVlanPortRxConfigBpduCount,
       "fsPbRstCVlanPortRxTcnBpduCount": fsPbRstCVlanPortRxTcnBpduCount,
       "fsPbRstCVlanPortTxRstBpduCount": fsPbRstCVlanPortTxRstBpduCount,
       "fsPbRstCVlanPortTxConfigBpduCount": fsPbRstCVlanPortTxConfigBpduCount,
       "fsPbRstCVlanPortTxTcnBpduCount": fsPbRstCVlanPortTxTcnBpduCount,
       "fsPbRstCVlanPortInvalidRstBpduRxCount": fsPbRstCVlanPortInvalidRstBpduRxCount,
       "fsPbRstCVlanPortInvalidConfigBpduRxCount": fsPbRstCVlanPortInvalidConfigBpduRxCount,
       "fsPbRstCVlanPortInvalidTcnBpduRxCount": fsPbRstCVlanPortInvalidTcnBpduRxCount,
       "fsPbRstCVlanPortProtocolMigrationCount": fsPbRstCVlanPortProtocolMigrationCount,
       "fsPbRstCVlanPortEffectivePortState": fsPbRstCVlanPortEffectivePortState}
)
