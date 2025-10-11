# SNMP MIB module (SUPERMICRO-MIPB-RSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-MIPB-RSTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:02:18 2025
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

futureMIPbRstMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134)
)
if mibBuilder.loadTexts:
    futureMIPbRstMIB.setRevisions(
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

_FutureMIPbRst_ObjectIdentity = ObjectIdentity
futureMIPbRst = _FutureMIPbRst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1)
)
_FsMIPbRstContextInfoTable_Object = MibTable
fsMIPbRstContextInfoTable = _FsMIPbRstContextInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 1)
)
if mibBuilder.loadTexts:
    fsMIPbRstContextInfoTable.setStatus("current")
_FsMIPbRstContextInfoEntry_Object = MibTableRow
fsMIPbRstContextInfoEntry = _FsMIPbRstContextInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 1, 1)
)
fsMIPbRstContextInfoEntry.setIndexNames(
    (0, "SUPERMICRO-MIPB-RSTP-MIB", "fsMIPbRstContextId"),
)
if mibBuilder.loadTexts:
    fsMIPbRstContextInfoEntry.setStatus("current")


class _FsMIPbRstContextId_Type(Integer32):
    """Custom type fsMIPbRstContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIPbRstContextId_Type.__name__ = "Integer32"
_FsMIPbRstContextId_Object = MibTableColumn
fsMIPbRstContextId = _FsMIPbRstContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 1, 1, 1),
    _FsMIPbRstContextId_Type()
)
fsMIPbRstContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPbRstContextId.setStatus("current")
_FsMIPbProviderStpStatus_Type = EnabledStatus
_FsMIPbProviderStpStatus_Object = MibTableColumn
fsMIPbProviderStpStatus = _FsMIPbProviderStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 1, 1, 2),
    _FsMIPbProviderStpStatus_Type()
)
fsMIPbProviderStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbProviderStpStatus.setStatus("current")
_FsMIPbRstCVlanBridgeTable_Object = MibTable
fsMIPbRstCVlanBridgeTable = _FsMIPbRstCVlanBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 2)
)
if mibBuilder.loadTexts:
    fsMIPbRstCVlanBridgeTable.setStatus("current")
_FsMIPbRstCVlanBridgeEntry_Object = MibTableRow
fsMIPbRstCVlanBridgeEntry = _FsMIPbRstCVlanBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 2, 1)
)
fsMIPbRstCVlanBridgeEntry.setIndexNames(
    (0, "SUPERMICRO-MIPB-RSTP-MIB", "fsMIPbRstPort"),
)
if mibBuilder.loadTexts:
    fsMIPbRstCVlanBridgeEntry.setStatus("current")


class _FsMIPbRstPort_Type(Integer32):
    """Custom type fsMIPbRstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIPbRstPort_Type.__name__ = "Integer32"
_FsMIPbRstPort_Object = MibTableColumn
fsMIPbRstPort = _FsMIPbRstPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 2, 1, 1),
    _FsMIPbRstPort_Type()
)
fsMIPbRstPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPbRstPort.setStatus("current")
_FsMIPbRstCVlanBridgeId_Type = BridgeId
_FsMIPbRstCVlanBridgeId_Object = MibTableColumn
fsMIPbRstCVlanBridgeId = _FsMIPbRstCVlanBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 2, 1, 2),
    _FsMIPbRstCVlanBridgeId_Type()
)
fsMIPbRstCVlanBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanBridgeId.setStatus("current")
_FsMIPbRstCVlanBridgeDesignatedRoot_Type = BridgeId
_FsMIPbRstCVlanBridgeDesignatedRoot_Object = MibTableColumn
fsMIPbRstCVlanBridgeDesignatedRoot = _FsMIPbRstCVlanBridgeDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 2, 1, 3),
    _FsMIPbRstCVlanBridgeDesignatedRoot_Type()
)
fsMIPbRstCVlanBridgeDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanBridgeDesignatedRoot.setStatus("current")
_FsMIPbRstCVlanBridgeRootCost_Type = Integer32
_FsMIPbRstCVlanBridgeRootCost_Object = MibTableColumn
fsMIPbRstCVlanBridgeRootCost = _FsMIPbRstCVlanBridgeRootCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 2, 1, 4),
    _FsMIPbRstCVlanBridgeRootCost_Type()
)
fsMIPbRstCVlanBridgeRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanBridgeRootCost.setStatus("current")
_FsMIPbRstCVlanBridgeMaxAge_Type = Timeout
_FsMIPbRstCVlanBridgeMaxAge_Object = MibTableColumn
fsMIPbRstCVlanBridgeMaxAge = _FsMIPbRstCVlanBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 2, 1, 5),
    _FsMIPbRstCVlanBridgeMaxAge_Type()
)
fsMIPbRstCVlanBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanBridgeMaxAge.setStatus("current")
_FsMIPbRstCVlanBridgeHelloTime_Type = Timeout
_FsMIPbRstCVlanBridgeHelloTime_Object = MibTableColumn
fsMIPbRstCVlanBridgeHelloTime = _FsMIPbRstCVlanBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 2, 1, 6),
    _FsMIPbRstCVlanBridgeHelloTime_Type()
)
fsMIPbRstCVlanBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanBridgeHelloTime.setStatus("current")
_FsMIPbRstCVlanBridgeHoldTime_Type = Integer32
_FsMIPbRstCVlanBridgeHoldTime_Object = MibTableColumn
fsMIPbRstCVlanBridgeHoldTime = _FsMIPbRstCVlanBridgeHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 2, 1, 7),
    _FsMIPbRstCVlanBridgeHoldTime_Type()
)
fsMIPbRstCVlanBridgeHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanBridgeHoldTime.setStatus("current")
_FsMIPbRstCVlanBridgeForwardDelay_Type = Timeout
_FsMIPbRstCVlanBridgeForwardDelay_Object = MibTableColumn
fsMIPbRstCVlanBridgeForwardDelay = _FsMIPbRstCVlanBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 2, 1, 8),
    _FsMIPbRstCVlanBridgeForwardDelay_Type()
)
fsMIPbRstCVlanBridgeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanBridgeForwardDelay.setStatus("current")
_FsMIPbRstCVlanBridgeTxHoldCount_Type = Integer32
_FsMIPbRstCVlanBridgeTxHoldCount_Object = MibTableColumn
fsMIPbRstCVlanBridgeTxHoldCount = _FsMIPbRstCVlanBridgeTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 2, 1, 9),
    _FsMIPbRstCVlanBridgeTxHoldCount_Type()
)
fsMIPbRstCVlanBridgeTxHoldCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanBridgeTxHoldCount.setStatus("current")
_FsMIPbRstCVlanStpHelloTime_Type = Timeout
_FsMIPbRstCVlanStpHelloTime_Object = MibTableColumn
fsMIPbRstCVlanStpHelloTime = _FsMIPbRstCVlanStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 2, 1, 10),
    _FsMIPbRstCVlanStpHelloTime_Type()
)
fsMIPbRstCVlanStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanStpHelloTime.setStatus("current")
_FsMIPbRstCVlanStpMaxAge_Type = Timeout
_FsMIPbRstCVlanStpMaxAge_Object = MibTableColumn
fsMIPbRstCVlanStpMaxAge = _FsMIPbRstCVlanStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 2, 1, 11),
    _FsMIPbRstCVlanStpMaxAge_Type()
)
fsMIPbRstCVlanStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanStpMaxAge.setStatus("current")
_FsMIPbRstCVlanStpForwardDelay_Type = Timeout
_FsMIPbRstCVlanStpForwardDelay_Object = MibTableColumn
fsMIPbRstCVlanStpForwardDelay = _FsMIPbRstCVlanStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 2, 1, 12),
    _FsMIPbRstCVlanStpForwardDelay_Type()
)
fsMIPbRstCVlanStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanStpForwardDelay.setStatus("current")
_FsMIPbRstCVlanStpTopChanges_Type = Counter32
_FsMIPbRstCVlanStpTopChanges_Object = MibTableColumn
fsMIPbRstCVlanStpTopChanges = _FsMIPbRstCVlanStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 2, 1, 13),
    _FsMIPbRstCVlanStpTopChanges_Type()
)
fsMIPbRstCVlanStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanStpTopChanges.setStatus("current")
_FsMIPbRstCVlanStpTimeSinceTopologyChange_Type = TimeTicks
_FsMIPbRstCVlanStpTimeSinceTopologyChange_Object = MibTableColumn
fsMIPbRstCVlanStpTimeSinceTopologyChange = _FsMIPbRstCVlanStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 2, 1, 14),
    _FsMIPbRstCVlanStpTimeSinceTopologyChange_Type()
)
fsMIPbRstCVlanStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanStpTimeSinceTopologyChange.setStatus("current")


class _FsMIPbRstCVlanStpDebugOption_Type(Integer32):
    """Custom type fsMIPbRstCVlanStpDebugOption based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 524287),
    )


_FsMIPbRstCVlanStpDebugOption_Type.__name__ = "Integer32"
_FsMIPbRstCVlanStpDebugOption_Object = MibTableColumn
fsMIPbRstCVlanStpDebugOption = _FsMIPbRstCVlanStpDebugOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 2, 1, 15),
    _FsMIPbRstCVlanStpDebugOption_Type()
)
fsMIPbRstCVlanStpDebugOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanStpDebugOption.setStatus("current")
_FsMIPbRstCVlanPortInfoTable_Object = MibTable
fsMIPbRstCVlanPortInfoTable = _FsMIPbRstCVlanPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 3)
)
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortInfoTable.setStatus("current")
_FsMIPbRstCVlanPortInfoEntry_Object = MibTableRow
fsMIPbRstCVlanPortInfoEntry = _FsMIPbRstCVlanPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 3, 1)
)
fsMIPbRstCVlanPortInfoEntry.setIndexNames(
    (0, "SUPERMICRO-MIPB-RSTP-MIB", "fsMIPbRstPort"),
    (0, "SUPERMICRO-MIPB-RSTP-MIB", "fsMIPbRstCepSvid"),
)
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortInfoEntry.setStatus("current")
_FsMIPbRstCepSvid_Type = VlanId
_FsMIPbRstCepSvid_Object = MibTableColumn
fsMIPbRstCepSvid = _FsMIPbRstCepSvid_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 3, 1, 1),
    _FsMIPbRstCepSvid_Type()
)
fsMIPbRstCepSvid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIPbRstCepSvid.setStatus("current")


class _FsMIPbRstCVlanPortPriority_Type(Integer32):
    """Custom type fsMIPbRstCVlanPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIPbRstCVlanPortPriority_Type.__name__ = "Integer32"
_FsMIPbRstCVlanPortPriority_Object = MibTableColumn
fsMIPbRstCVlanPortPriority = _FsMIPbRstCVlanPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 3, 1, 2),
    _FsMIPbRstCVlanPortPriority_Type()
)
fsMIPbRstCVlanPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortPriority.setStatus("current")


class _FsMIPbRstCVlanPortPathCost_Type(Integer32):
    """Custom type fsMIPbRstCVlanPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIPbRstCVlanPortPathCost_Type.__name__ = "Integer32"
_FsMIPbRstCVlanPortPathCost_Object = MibTableColumn
fsMIPbRstCVlanPortPathCost = _FsMIPbRstCVlanPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 3, 1, 3),
    _FsMIPbRstCVlanPortPathCost_Type()
)
fsMIPbRstCVlanPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortPathCost.setStatus("current")


class _FsMIPbRstCVlanPortRole_Type(Integer32):
    """Custom type fsMIPbRstCVlanPortRole based on Integer32"""
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


_FsMIPbRstCVlanPortRole_Type.__name__ = "Integer32"
_FsMIPbRstCVlanPortRole_Object = MibTableColumn
fsMIPbRstCVlanPortRole = _FsMIPbRstCVlanPortRole_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 3, 1, 4),
    _FsMIPbRstCVlanPortRole_Type()
)
fsMIPbRstCVlanPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortRole.setStatus("current")


class _FsMIPbRstCVlanPortState_Type(Integer32):
    """Custom type fsMIPbRstCVlanPortState based on Integer32"""
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


_FsMIPbRstCVlanPortState_Type.__name__ = "Integer32"
_FsMIPbRstCVlanPortState_Object = MibTableColumn
fsMIPbRstCVlanPortState = _FsMIPbRstCVlanPortState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 3, 1, 5),
    _FsMIPbRstCVlanPortState_Type()
)
fsMIPbRstCVlanPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortState.setStatus("current")
_FsMIPbRstCVlanPortAdminEdgePort_Type = TruthValue
_FsMIPbRstCVlanPortAdminEdgePort_Object = MibTableColumn
fsMIPbRstCVlanPortAdminEdgePort = _FsMIPbRstCVlanPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 3, 1, 6),
    _FsMIPbRstCVlanPortAdminEdgePort_Type()
)
fsMIPbRstCVlanPortAdminEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortAdminEdgePort.setStatus("current")
_FsMIPbRstCVlanPortOperEdgePort_Type = TruthValue
_FsMIPbRstCVlanPortOperEdgePort_Object = MibTableColumn
fsMIPbRstCVlanPortOperEdgePort = _FsMIPbRstCVlanPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 3, 1, 7),
    _FsMIPbRstCVlanPortOperEdgePort_Type()
)
fsMIPbRstCVlanPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortOperEdgePort.setStatus("current")


class _FsMIPbRstCVlanPortAdminPointToPoint_Type(Integer32):
    """Custom type fsMIPbRstCVlanPortAdminPointToPoint based on Integer32"""
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


_FsMIPbRstCVlanPortAdminPointToPoint_Type.__name__ = "Integer32"
_FsMIPbRstCVlanPortAdminPointToPoint_Object = MibTableColumn
fsMIPbRstCVlanPortAdminPointToPoint = _FsMIPbRstCVlanPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 3, 1, 8),
    _FsMIPbRstCVlanPortAdminPointToPoint_Type()
)
fsMIPbRstCVlanPortAdminPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortAdminPointToPoint.setStatus("current")
_FsMIPbRstCVlanPortOperPointToPoint_Type = TruthValue
_FsMIPbRstCVlanPortOperPointToPoint_Object = MibTableColumn
fsMIPbRstCVlanPortOperPointToPoint = _FsMIPbRstCVlanPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 3, 1, 9),
    _FsMIPbRstCVlanPortOperPointToPoint_Type()
)
fsMIPbRstCVlanPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortOperPointToPoint.setStatus("current")
_FsMIPbRstCVlanPortAutoEdge_Type = TruthValue
_FsMIPbRstCVlanPortAutoEdge_Object = MibTableColumn
fsMIPbRstCVlanPortAutoEdge = _FsMIPbRstCVlanPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 3, 1, 10),
    _FsMIPbRstCVlanPortAutoEdge_Type()
)
fsMIPbRstCVlanPortAutoEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortAutoEdge.setStatus("current")
_FsMIPbRstCVlanPortDesignatedRoot_Type = BridgeId
_FsMIPbRstCVlanPortDesignatedRoot_Object = MibTableColumn
fsMIPbRstCVlanPortDesignatedRoot = _FsMIPbRstCVlanPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 3, 1, 11),
    _FsMIPbRstCVlanPortDesignatedRoot_Type()
)
fsMIPbRstCVlanPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortDesignatedRoot.setStatus("current")
_FsMIPbRstCVlanPortDesignatedCost_Type = Integer32
_FsMIPbRstCVlanPortDesignatedCost_Object = MibTableColumn
fsMIPbRstCVlanPortDesignatedCost = _FsMIPbRstCVlanPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 3, 1, 12),
    _FsMIPbRstCVlanPortDesignatedCost_Type()
)
fsMIPbRstCVlanPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortDesignatedCost.setStatus("current")
_FsMIPbRstCVlanPortDesignatedBridge_Type = BridgeId
_FsMIPbRstCVlanPortDesignatedBridge_Object = MibTableColumn
fsMIPbRstCVlanPortDesignatedBridge = _FsMIPbRstCVlanPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 3, 1, 13),
    _FsMIPbRstCVlanPortDesignatedBridge_Type()
)
fsMIPbRstCVlanPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortDesignatedBridge.setStatus("current")


class _FsMIPbRstCVlanPortDesignatedPort_Type(OctetString):
    """Custom type fsMIPbRstCVlanPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_FsMIPbRstCVlanPortDesignatedPort_Type.__name__ = "OctetString"
_FsMIPbRstCVlanPortDesignatedPort_Object = MibTableColumn
fsMIPbRstCVlanPortDesignatedPort = _FsMIPbRstCVlanPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 3, 1, 14),
    _FsMIPbRstCVlanPortDesignatedPort_Type()
)
fsMIPbRstCVlanPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortDesignatedPort.setStatus("current")
_FsMIPbRstCVlanPortForwardTransitions_Type = Counter32
_FsMIPbRstCVlanPortForwardTransitions_Object = MibTableColumn
fsMIPbRstCVlanPortForwardTransitions = _FsMIPbRstCVlanPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 3, 1, 15),
    _FsMIPbRstCVlanPortForwardTransitions_Type()
)
fsMIPbRstCVlanPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortForwardTransitions.setStatus("current")
_FsMIPbRstCVlanPortSmTable_Object = MibTable
fsMIPbRstCVlanPortSmTable = _FsMIPbRstCVlanPortSmTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 4)
)
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortSmTable.setStatus("current")
_FsMIPbRstCVlanPortSmEntry_Object = MibTableRow
fsMIPbRstCVlanPortSmEntry = _FsMIPbRstCVlanPortSmEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 4, 1)
)
fsMIPbRstCVlanPortSmEntry.setIndexNames(
    (0, "SUPERMICRO-MIPB-RSTP-MIB", "fsMIPbRstPort"),
    (0, "SUPERMICRO-MIPB-RSTP-MIB", "fsMIPbRstCepSvid"),
)
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortSmEntry.setStatus("current")


class _FsMIPbRstCVlanPortInfoSmState_Type(Integer32):
    """Custom type fsMIPbRstCVlanPortInfoSmState based on Integer32"""
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


_FsMIPbRstCVlanPortInfoSmState_Type.__name__ = "Integer32"
_FsMIPbRstCVlanPortInfoSmState_Object = MibTableColumn
fsMIPbRstCVlanPortInfoSmState = _FsMIPbRstCVlanPortInfoSmState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 4, 1, 1),
    _FsMIPbRstCVlanPortInfoSmState_Type()
)
fsMIPbRstCVlanPortInfoSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortInfoSmState.setStatus("current")


class _FsMIPbRstCVlanPortMigSmState_Type(Integer32):
    """Custom type fsMIPbRstCVlanPortMigSmState based on Integer32"""
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


_FsMIPbRstCVlanPortMigSmState_Type.__name__ = "Integer32"
_FsMIPbRstCVlanPortMigSmState_Object = MibTableColumn
fsMIPbRstCVlanPortMigSmState = _FsMIPbRstCVlanPortMigSmState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 4, 1, 2),
    _FsMIPbRstCVlanPortMigSmState_Type()
)
fsMIPbRstCVlanPortMigSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortMigSmState.setStatus("current")


class _FsMIPbRstCVlanPortRoleTransSmState_Type(Integer32):
    """Custom type fsMIPbRstCVlanPortRoleTransSmState based on Integer32"""
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


_FsMIPbRstCVlanPortRoleTransSmState_Type.__name__ = "Integer32"
_FsMIPbRstCVlanPortRoleTransSmState_Object = MibTableColumn
fsMIPbRstCVlanPortRoleTransSmState = _FsMIPbRstCVlanPortRoleTransSmState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 4, 1, 3),
    _FsMIPbRstCVlanPortRoleTransSmState_Type()
)
fsMIPbRstCVlanPortRoleTransSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortRoleTransSmState.setStatus("current")


class _FsMIPbRstCVlanPortStateTransSmState_Type(Integer32):
    """Custom type fsMIPbRstCVlanPortStateTransSmState based on Integer32"""
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


_FsMIPbRstCVlanPortStateTransSmState_Type.__name__ = "Integer32"
_FsMIPbRstCVlanPortStateTransSmState_Object = MibTableColumn
fsMIPbRstCVlanPortStateTransSmState = _FsMIPbRstCVlanPortStateTransSmState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 4, 1, 4),
    _FsMIPbRstCVlanPortStateTransSmState_Type()
)
fsMIPbRstCVlanPortStateTransSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortStateTransSmState.setStatus("current")


class _FsMIPbRstCVlanPortTopoChSmState_Type(Integer32):
    """Custom type fsMIPbRstCVlanPortTopoChSmState based on Integer32"""
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


_FsMIPbRstCVlanPortTopoChSmState_Type.__name__ = "Integer32"
_FsMIPbRstCVlanPortTopoChSmState_Object = MibTableColumn
fsMIPbRstCVlanPortTopoChSmState = _FsMIPbRstCVlanPortTopoChSmState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 4, 1, 5),
    _FsMIPbRstCVlanPortTopoChSmState_Type()
)
fsMIPbRstCVlanPortTopoChSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortTopoChSmState.setStatus("current")


class _FsMIPbRstCVlanPortTxSmState_Type(Integer32):
    """Custom type fsMIPbRstCVlanPortTxSmState based on Integer32"""
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


_FsMIPbRstCVlanPortTxSmState_Type.__name__ = "Integer32"
_FsMIPbRstCVlanPortTxSmState_Object = MibTableColumn
fsMIPbRstCVlanPortTxSmState = _FsMIPbRstCVlanPortTxSmState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 4, 1, 6),
    _FsMIPbRstCVlanPortTxSmState_Type()
)
fsMIPbRstCVlanPortTxSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortTxSmState.setStatus("current")
_FsMIPbRstCVlanPortStatsTable_Object = MibTable
fsMIPbRstCVlanPortStatsTable = _FsMIPbRstCVlanPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 5)
)
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortStatsTable.setStatus("current")
_FsMIPbRstCVlanPortStatsEntry_Object = MibTableRow
fsMIPbRstCVlanPortStatsEntry = _FsMIPbRstCVlanPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 5, 1)
)
fsMIPbRstCVlanPortStatsEntry.setIndexNames(
    (0, "SUPERMICRO-MIPB-RSTP-MIB", "fsMIPbRstPort"),
    (0, "SUPERMICRO-MIPB-RSTP-MIB", "fsMIPbRstCepSvid"),
)
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortStatsEntry.setStatus("current")
_FsMIPbRstCVlanPortRxRstBpduCount_Type = Counter32
_FsMIPbRstCVlanPortRxRstBpduCount_Object = MibTableColumn
fsMIPbRstCVlanPortRxRstBpduCount = _FsMIPbRstCVlanPortRxRstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 5, 1, 1),
    _FsMIPbRstCVlanPortRxRstBpduCount_Type()
)
fsMIPbRstCVlanPortRxRstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortRxRstBpduCount.setStatus("current")
_FsMIPbRstCVlanPortRxConfigBpduCount_Type = Counter32
_FsMIPbRstCVlanPortRxConfigBpduCount_Object = MibTableColumn
fsMIPbRstCVlanPortRxConfigBpduCount = _FsMIPbRstCVlanPortRxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 5, 1, 2),
    _FsMIPbRstCVlanPortRxConfigBpduCount_Type()
)
fsMIPbRstCVlanPortRxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortRxConfigBpduCount.setStatus("current")
_FsMIPbRstCVlanPortRxTcnBpduCount_Type = Counter32
_FsMIPbRstCVlanPortRxTcnBpduCount_Object = MibTableColumn
fsMIPbRstCVlanPortRxTcnBpduCount = _FsMIPbRstCVlanPortRxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 5, 1, 3),
    _FsMIPbRstCVlanPortRxTcnBpduCount_Type()
)
fsMIPbRstCVlanPortRxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortRxTcnBpduCount.setStatus("current")
_FsMIPbRstCVlanPortTxRstBpduCount_Type = Counter32
_FsMIPbRstCVlanPortTxRstBpduCount_Object = MibTableColumn
fsMIPbRstCVlanPortTxRstBpduCount = _FsMIPbRstCVlanPortTxRstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 5, 1, 4),
    _FsMIPbRstCVlanPortTxRstBpduCount_Type()
)
fsMIPbRstCVlanPortTxRstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortTxRstBpduCount.setStatus("current")
_FsMIPbRstCVlanPortTxConfigBpduCount_Type = Counter32
_FsMIPbRstCVlanPortTxConfigBpduCount_Object = MibTableColumn
fsMIPbRstCVlanPortTxConfigBpduCount = _FsMIPbRstCVlanPortTxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 5, 1, 5),
    _FsMIPbRstCVlanPortTxConfigBpduCount_Type()
)
fsMIPbRstCVlanPortTxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortTxConfigBpduCount.setStatus("current")
_FsMIPbRstCVlanPortTxTcnBpduCount_Type = Counter32
_FsMIPbRstCVlanPortTxTcnBpduCount_Object = MibTableColumn
fsMIPbRstCVlanPortTxTcnBpduCount = _FsMIPbRstCVlanPortTxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 5, 1, 6),
    _FsMIPbRstCVlanPortTxTcnBpduCount_Type()
)
fsMIPbRstCVlanPortTxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortTxTcnBpduCount.setStatus("current")
_FsMIPbRstCVlanPortInvalidRstBpduRxCount_Type = Counter32
_FsMIPbRstCVlanPortInvalidRstBpduRxCount_Object = MibTableColumn
fsMIPbRstCVlanPortInvalidRstBpduRxCount = _FsMIPbRstCVlanPortInvalidRstBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 5, 1, 7),
    _FsMIPbRstCVlanPortInvalidRstBpduRxCount_Type()
)
fsMIPbRstCVlanPortInvalidRstBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortInvalidRstBpduRxCount.setStatus("current")
_FsMIPbRstCVlanPortInvalidConfigBpduRxCount_Type = Counter32
_FsMIPbRstCVlanPortInvalidConfigBpduRxCount_Object = MibTableColumn
fsMIPbRstCVlanPortInvalidConfigBpduRxCount = _FsMIPbRstCVlanPortInvalidConfigBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 5, 1, 8),
    _FsMIPbRstCVlanPortInvalidConfigBpduRxCount_Type()
)
fsMIPbRstCVlanPortInvalidConfigBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortInvalidConfigBpduRxCount.setStatus("current")
_FsMIPbRstCVlanPortInvalidTcnBpduRxCount_Type = Counter32
_FsMIPbRstCVlanPortInvalidTcnBpduRxCount_Object = MibTableColumn
fsMIPbRstCVlanPortInvalidTcnBpduRxCount = _FsMIPbRstCVlanPortInvalidTcnBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 5, 1, 9),
    _FsMIPbRstCVlanPortInvalidTcnBpduRxCount_Type()
)
fsMIPbRstCVlanPortInvalidTcnBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortInvalidTcnBpduRxCount.setStatus("current")
_FsMIPbRstCVlanPortProtocolMigrationCount_Type = Counter32
_FsMIPbRstCVlanPortProtocolMigrationCount_Object = MibTableColumn
fsMIPbRstCVlanPortProtocolMigrationCount = _FsMIPbRstCVlanPortProtocolMigrationCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 5, 1, 10),
    _FsMIPbRstCVlanPortProtocolMigrationCount_Type()
)
fsMIPbRstCVlanPortProtocolMigrationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortProtocolMigrationCount.setStatus("current")
_FsMIPbRstCVlanPortEffectivePortState_Type = TruthValue
_FsMIPbRstCVlanPortEffectivePortState_Object = MibTableColumn
fsMIPbRstCVlanPortEffectivePortState = _FsMIPbRstCVlanPortEffectivePortState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 134, 1, 5, 1, 11),
    _FsMIPbRstCVlanPortEffectivePortState_Type()
)
fsMIPbRstCVlanPortEffectivePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIPbRstCVlanPortEffectivePortState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-MIPB-RSTP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "VlanId": VlanId,
       "futureMIPbRstMIB": futureMIPbRstMIB,
       "futureMIPbRst": futureMIPbRst,
       "fsMIPbRstContextInfoTable": fsMIPbRstContextInfoTable,
       "fsMIPbRstContextInfoEntry": fsMIPbRstContextInfoEntry,
       "fsMIPbRstContextId": fsMIPbRstContextId,
       "fsMIPbProviderStpStatus": fsMIPbProviderStpStatus,
       "fsMIPbRstCVlanBridgeTable": fsMIPbRstCVlanBridgeTable,
       "fsMIPbRstCVlanBridgeEntry": fsMIPbRstCVlanBridgeEntry,
       "fsMIPbRstPort": fsMIPbRstPort,
       "fsMIPbRstCVlanBridgeId": fsMIPbRstCVlanBridgeId,
       "fsMIPbRstCVlanBridgeDesignatedRoot": fsMIPbRstCVlanBridgeDesignatedRoot,
       "fsMIPbRstCVlanBridgeRootCost": fsMIPbRstCVlanBridgeRootCost,
       "fsMIPbRstCVlanBridgeMaxAge": fsMIPbRstCVlanBridgeMaxAge,
       "fsMIPbRstCVlanBridgeHelloTime": fsMIPbRstCVlanBridgeHelloTime,
       "fsMIPbRstCVlanBridgeHoldTime": fsMIPbRstCVlanBridgeHoldTime,
       "fsMIPbRstCVlanBridgeForwardDelay": fsMIPbRstCVlanBridgeForwardDelay,
       "fsMIPbRstCVlanBridgeTxHoldCount": fsMIPbRstCVlanBridgeTxHoldCount,
       "fsMIPbRstCVlanStpHelloTime": fsMIPbRstCVlanStpHelloTime,
       "fsMIPbRstCVlanStpMaxAge": fsMIPbRstCVlanStpMaxAge,
       "fsMIPbRstCVlanStpForwardDelay": fsMIPbRstCVlanStpForwardDelay,
       "fsMIPbRstCVlanStpTopChanges": fsMIPbRstCVlanStpTopChanges,
       "fsMIPbRstCVlanStpTimeSinceTopologyChange": fsMIPbRstCVlanStpTimeSinceTopologyChange,
       "fsMIPbRstCVlanStpDebugOption": fsMIPbRstCVlanStpDebugOption,
       "fsMIPbRstCVlanPortInfoTable": fsMIPbRstCVlanPortInfoTable,
       "fsMIPbRstCVlanPortInfoEntry": fsMIPbRstCVlanPortInfoEntry,
       "fsMIPbRstCepSvid": fsMIPbRstCepSvid,
       "fsMIPbRstCVlanPortPriority": fsMIPbRstCVlanPortPriority,
       "fsMIPbRstCVlanPortPathCost": fsMIPbRstCVlanPortPathCost,
       "fsMIPbRstCVlanPortRole": fsMIPbRstCVlanPortRole,
       "fsMIPbRstCVlanPortState": fsMIPbRstCVlanPortState,
       "fsMIPbRstCVlanPortAdminEdgePort": fsMIPbRstCVlanPortAdminEdgePort,
       "fsMIPbRstCVlanPortOperEdgePort": fsMIPbRstCVlanPortOperEdgePort,
       "fsMIPbRstCVlanPortAdminPointToPoint": fsMIPbRstCVlanPortAdminPointToPoint,
       "fsMIPbRstCVlanPortOperPointToPoint": fsMIPbRstCVlanPortOperPointToPoint,
       "fsMIPbRstCVlanPortAutoEdge": fsMIPbRstCVlanPortAutoEdge,
       "fsMIPbRstCVlanPortDesignatedRoot": fsMIPbRstCVlanPortDesignatedRoot,
       "fsMIPbRstCVlanPortDesignatedCost": fsMIPbRstCVlanPortDesignatedCost,
       "fsMIPbRstCVlanPortDesignatedBridge": fsMIPbRstCVlanPortDesignatedBridge,
       "fsMIPbRstCVlanPortDesignatedPort": fsMIPbRstCVlanPortDesignatedPort,
       "fsMIPbRstCVlanPortForwardTransitions": fsMIPbRstCVlanPortForwardTransitions,
       "fsMIPbRstCVlanPortSmTable": fsMIPbRstCVlanPortSmTable,
       "fsMIPbRstCVlanPortSmEntry": fsMIPbRstCVlanPortSmEntry,
       "fsMIPbRstCVlanPortInfoSmState": fsMIPbRstCVlanPortInfoSmState,
       "fsMIPbRstCVlanPortMigSmState": fsMIPbRstCVlanPortMigSmState,
       "fsMIPbRstCVlanPortRoleTransSmState": fsMIPbRstCVlanPortRoleTransSmState,
       "fsMIPbRstCVlanPortStateTransSmState": fsMIPbRstCVlanPortStateTransSmState,
       "fsMIPbRstCVlanPortTopoChSmState": fsMIPbRstCVlanPortTopoChSmState,
       "fsMIPbRstCVlanPortTxSmState": fsMIPbRstCVlanPortTxSmState,
       "fsMIPbRstCVlanPortStatsTable": fsMIPbRstCVlanPortStatsTable,
       "fsMIPbRstCVlanPortStatsEntry": fsMIPbRstCVlanPortStatsEntry,
       "fsMIPbRstCVlanPortRxRstBpduCount": fsMIPbRstCVlanPortRxRstBpduCount,
       "fsMIPbRstCVlanPortRxConfigBpduCount": fsMIPbRstCVlanPortRxConfigBpduCount,
       "fsMIPbRstCVlanPortRxTcnBpduCount": fsMIPbRstCVlanPortRxTcnBpduCount,
       "fsMIPbRstCVlanPortTxRstBpduCount": fsMIPbRstCVlanPortTxRstBpduCount,
       "fsMIPbRstCVlanPortTxConfigBpduCount": fsMIPbRstCVlanPortTxConfigBpduCount,
       "fsMIPbRstCVlanPortTxTcnBpduCount": fsMIPbRstCVlanPortTxTcnBpduCount,
       "fsMIPbRstCVlanPortInvalidRstBpduRxCount": fsMIPbRstCVlanPortInvalidRstBpduRxCount,
       "fsMIPbRstCVlanPortInvalidConfigBpduRxCount": fsMIPbRstCVlanPortInvalidConfigBpduRxCount,
       "fsMIPbRstCVlanPortInvalidTcnBpduRxCount": fsMIPbRstCVlanPortInvalidTcnBpduRxCount,
       "fsMIPbRstCVlanPortProtocolMigrationCount": fsMIPbRstCVlanPortProtocolMigrationCount,
       "fsMIPbRstCVlanPortEffectivePortState": fsMIPbRstCVlanPortEffectivePortState}
)
