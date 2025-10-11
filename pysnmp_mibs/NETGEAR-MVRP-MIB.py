# SNMP MIB module (NETGEAR-MVRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/netgear/NETGEAR-MVRP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:27:12 2025
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

(agentDot1qMrpMxrp,) = mibBuilder.importSymbols(
    "NETGEAR-MRP-MIB",
    "agentDot1qMrpMxrp")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

fastPathMVRP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 2)
)
if mibBuilder.loadTexts:
    fastPathMVRP.setRevisions(
        ("2011-04-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentDot1qMvrp_ObjectIdentity = ObjectIdentity
agentDot1qMvrp = _AgentDot1qMvrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 2, 1)
)
_AgentDot1qPortMvrpTable_Object = MibTable
agentDot1qPortMvrpTable = _AgentDot1qPortMvrpTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    agentDot1qPortMvrpTable.setStatus("current")
_AgentDot1qPortMvrpEntry_Object = MibTableRow
agentDot1qPortMvrpEntry = _AgentDot1qPortMvrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 2, 1, 1, 1)
)
agentDot1qPortMvrpEntry.setIndexNames(
    (0, "NETGEAR-MVRP-MIB", "agentDot1qMvrpPort"),
)
if mibBuilder.loadTexts:
    agentDot1qPortMvrpEntry.setStatus("current")


class _AgentDot1qMvrpPort_Type(Unsigned32):
    """Custom type agentDot1qMvrpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentDot1qMvrpPort_Type.__name__ = "Unsigned32"
_AgentDot1qMvrpPort_Object = MibTableColumn
agentDot1qMvrpPort = _AgentDot1qMvrpPort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 2, 1, 1, 1, 1),
    _AgentDot1qMvrpPort_Type()
)
agentDot1qMvrpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDot1qMvrpPort.setStatus("current")


class _AgentDot1qPortMvrpMode_Type(EnabledStatus):
    """Custom type agentDot1qPortMvrpMode based on EnabledStatus"""
    defaultValue = 2


_AgentDot1qPortMvrpMode_Type.__name__ = "EnabledStatus"
_AgentDot1qPortMvrpMode_Object = MibTableColumn
agentDot1qPortMvrpMode = _AgentDot1qPortMvrpMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 2, 1, 1, 1, 10),
    _AgentDot1qPortMvrpMode_Type()
)
agentDot1qPortMvrpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1qPortMvrpMode.setStatus("current")


class _AgentDot1qBridgeMvrpMode_Type(EnabledStatus):
    """Custom type agentDot1qBridgeMvrpMode based on EnabledStatus"""
    defaultValue = 2


_AgentDot1qBridgeMvrpMode_Type.__name__ = "EnabledStatus"
_AgentDot1qBridgeMvrpMode_Object = MibScalar
agentDot1qBridgeMvrpMode = _AgentDot1qBridgeMvrpMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 2, 1, 2),
    _AgentDot1qBridgeMvrpMode_Type()
)
agentDot1qBridgeMvrpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1qBridgeMvrpMode.setStatus("current")


class _AgentDot1qBridgeMrpPeriodicStateMachineForMvrp_Type(EnabledStatus):
    """Custom type agentDot1qBridgeMrpPeriodicStateMachineForMvrp based on EnabledStatus"""
    defaultValue = 2


_AgentDot1qBridgeMrpPeriodicStateMachineForMvrp_Type.__name__ = "EnabledStatus"
_AgentDot1qBridgeMrpPeriodicStateMachineForMvrp_Object = MibScalar
agentDot1qBridgeMrpPeriodicStateMachineForMvrp = _AgentDot1qBridgeMrpPeriodicStateMachineForMvrp_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 2, 1, 3),
    _AgentDot1qBridgeMrpPeriodicStateMachineForMvrp_Type()
)
agentDot1qBridgeMrpPeriodicStateMachineForMvrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1qBridgeMrpPeriodicStateMachineForMvrp.setStatus("current")
_AgentDot1qMrpMvrpStats_ObjectIdentity = ObjectIdentity
agentDot1qMrpMvrpStats = _AgentDot1qMrpMvrpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 2, 2)
)
_AgentDot1qMrpMvrpPktTx_Type = Counter32
_AgentDot1qMrpMvrpPktTx_Object = MibScalar
agentDot1qMrpMvrpPktTx = _AgentDot1qMrpMvrpPktTx_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 2, 2, 1),
    _AgentDot1qMrpMvrpPktTx_Type()
)
agentDot1qMrpMvrpPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1qMrpMvrpPktTx.setStatus("current")
_AgentDot1qMrpMvrpPktRx_Type = Counter32
_AgentDot1qMrpMvrpPktRx_Object = MibScalar
agentDot1qMrpMvrpPktRx = _AgentDot1qMrpMvrpPktRx_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 2, 2, 2),
    _AgentDot1qMrpMvrpPktRx_Type()
)
agentDot1qMrpMvrpPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1qMrpMvrpPktRx.setStatus("current")
_AgentDot1qMrpMvrpPktRxBadHeader_Type = Counter32
_AgentDot1qMrpMvrpPktRxBadHeader_Object = MibScalar
agentDot1qMrpMvrpPktRxBadHeader = _AgentDot1qMrpMvrpPktRxBadHeader_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 2, 2, 3),
    _AgentDot1qMrpMvrpPktRxBadHeader_Type()
)
agentDot1qMrpMvrpPktRxBadHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1qMrpMvrpPktRxBadHeader.setStatus("current")
_AgentDot1qMrpMvrpPktRxBadFormat_Type = Counter32
_AgentDot1qMrpMvrpPktRxBadFormat_Object = MibScalar
agentDot1qMrpMvrpPktRxBadFormat = _AgentDot1qMrpMvrpPktRxBadFormat_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 2, 2, 4),
    _AgentDot1qMrpMvrpPktRxBadFormat_Type()
)
agentDot1qMrpMvrpPktRxBadFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1qMrpMvrpPktRxBadFormat.setStatus("current")
_AgentDot1qMrpMvrpPktTxFailure_Type = Counter32
_AgentDot1qMrpMvrpPktTxFailure_Object = MibScalar
agentDot1qMrpMvrpPktTxFailure = _AgentDot1qMrpMvrpPktTxFailure_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 2, 2, 5),
    _AgentDot1qMrpMvrpPktTxFailure_Type()
)
agentDot1qMrpMvrpPktTxFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1qMrpMvrpPktTxFailure.setStatus("current")
_AgentDot1qMrpMvrpStatsTable_Object = MibTable
agentDot1qMrpMvrpStatsTable = _AgentDot1qMrpMvrpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 2, 2, 6)
)
if mibBuilder.loadTexts:
    agentDot1qMrpMvrpStatsTable.setStatus("current")
_AgentDot1qMrpMvrpStatisticsEntry_Object = MibTableRow
agentDot1qMrpMvrpStatisticsEntry = _AgentDot1qMrpMvrpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 2, 2, 6, 1)
)
agentDot1qMrpMvrpStatisticsEntry.setIndexNames(
    (0, "NETGEAR-MVRP-MIB", "agentDot1qMrpMvrpIntf"),
)
if mibBuilder.loadTexts:
    agentDot1qMrpMvrpStatisticsEntry.setStatus("current")


class _AgentDot1qMrpMvrpIntf_Type(Integer32):
    """Custom type agentDot1qMrpMvrpIntf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentDot1qMrpMvrpIntf_Type.__name__ = "Integer32"
_AgentDot1qMrpMvrpIntf_Object = MibTableColumn
agentDot1qMrpMvrpIntf = _AgentDot1qMrpMvrpIntf_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 2, 2, 6, 1, 1),
    _AgentDot1qMrpMvrpIntf_Type()
)
agentDot1qMrpMvrpIntf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDot1qMrpMvrpIntf.setStatus("current")
_AgentDot1qMrpMvrpPortPktTx_Type = Counter32
_AgentDot1qMrpMvrpPortPktTx_Object = MibTableColumn
agentDot1qMrpMvrpPortPktTx = _AgentDot1qMrpMvrpPortPktTx_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 2, 2, 6, 1, 2),
    _AgentDot1qMrpMvrpPortPktTx_Type()
)
agentDot1qMrpMvrpPortPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1qMrpMvrpPortPktTx.setStatus("current")
_AgentDot1qMrpMvrpPortPktRx_Type = Counter32
_AgentDot1qMrpMvrpPortPktRx_Object = MibTableColumn
agentDot1qMrpMvrpPortPktRx = _AgentDot1qMrpMvrpPortPktRx_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 2, 2, 6, 1, 3),
    _AgentDot1qMrpMvrpPortPktRx_Type()
)
agentDot1qMrpMvrpPortPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1qMrpMvrpPortPktRx.setStatus("current")
_AgentDot1qMrpMvrpPortPktRxBadHeader_Type = Counter32
_AgentDot1qMrpMvrpPortPktRxBadHeader_Object = MibTableColumn
agentDot1qMrpMvrpPortPktRxBadHeader = _AgentDot1qMrpMvrpPortPktRxBadHeader_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 2, 2, 6, 1, 4),
    _AgentDot1qMrpMvrpPortPktRxBadHeader_Type()
)
agentDot1qMrpMvrpPortPktRxBadHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1qMrpMvrpPortPktRxBadHeader.setStatus("current")
_AgentDot1qMrpMvrpPortPktRxBadFormat_Type = Counter32
_AgentDot1qMrpMvrpPortPktRxBadFormat_Object = MibTableColumn
agentDot1qMrpMvrpPortPktRxBadFormat = _AgentDot1qMrpMvrpPortPktRxBadFormat_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 2, 2, 6, 1, 5),
    _AgentDot1qMrpMvrpPortPktRxBadFormat_Type()
)
agentDot1qMrpMvrpPortPktRxBadFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1qMrpMvrpPortPktRxBadFormat.setStatus("current")
_AgentDot1qMrpMvrpPortPktTxFailure_Type = Counter32
_AgentDot1qMrpMvrpPortPktTxFailure_Object = MibTableColumn
agentDot1qMrpMvrpPortPktTxFailure = _AgentDot1qMrpMvrpPortPktTxFailure_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 2, 2, 6, 1, 6),
    _AgentDot1qMrpMvrpPortPktTxFailure_Type()
)
agentDot1qMrpMvrpPortPktTxFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1qMrpMvrpPortPktTxFailure.setStatus("current")
_AgentDot1qMrpMvrpPortPktRegFailure_Type = Counter32
_AgentDot1qMrpMvrpPortPktRegFailure_Object = MibTableColumn
agentDot1qMrpMvrpPortPktRegFailure = _AgentDot1qMrpMvrpPortPktRegFailure_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 2, 2, 6, 1, 7),
    _AgentDot1qMrpMvrpPortPktRegFailure_Type()
)
agentDot1qMrpMvrpPortPktRegFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1qMrpMvrpPortPktRegFailure.setStatus("current")
_AgentDot1qMrpMvrpPktMessageFailure_Type = Counter32
_AgentDot1qMrpMvrpPktMessageFailure_Object = MibScalar
agentDot1qMrpMvrpPktMessageFailure = _AgentDot1qMrpMvrpPktMessageFailure_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 2, 2, 7),
    _AgentDot1qMrpMvrpPktMessageFailure_Type()
)
agentDot1qMrpMvrpPktMessageFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1qMrpMvrpPktMessageFailure.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETGEAR-MVRP-MIB",
    **{"fastPathMVRP": fastPathMVRP,
       "agentDot1qMvrp": agentDot1qMvrp,
       "agentDot1qPortMvrpTable": agentDot1qPortMvrpTable,
       "agentDot1qPortMvrpEntry": agentDot1qPortMvrpEntry,
       "agentDot1qMvrpPort": agentDot1qMvrpPort,
       "agentDot1qPortMvrpMode": agentDot1qPortMvrpMode,
       "agentDot1qBridgeMvrpMode": agentDot1qBridgeMvrpMode,
       "agentDot1qBridgeMrpPeriodicStateMachineForMvrp": agentDot1qBridgeMrpPeriodicStateMachineForMvrp,
       "agentDot1qMrpMvrpStats": agentDot1qMrpMvrpStats,
       "agentDot1qMrpMvrpPktTx": agentDot1qMrpMvrpPktTx,
       "agentDot1qMrpMvrpPktRx": agentDot1qMrpMvrpPktRx,
       "agentDot1qMrpMvrpPktRxBadHeader": agentDot1qMrpMvrpPktRxBadHeader,
       "agentDot1qMrpMvrpPktRxBadFormat": agentDot1qMrpMvrpPktRxBadFormat,
       "agentDot1qMrpMvrpPktTxFailure": agentDot1qMrpMvrpPktTxFailure,
       "agentDot1qMrpMvrpStatsTable": agentDot1qMrpMvrpStatsTable,
       "agentDot1qMrpMvrpStatisticsEntry": agentDot1qMrpMvrpStatisticsEntry,
       "agentDot1qMrpMvrpIntf": agentDot1qMrpMvrpIntf,
       "agentDot1qMrpMvrpPortPktTx": agentDot1qMrpMvrpPortPktTx,
       "agentDot1qMrpMvrpPortPktRx": agentDot1qMrpMvrpPortPktRx,
       "agentDot1qMrpMvrpPortPktRxBadHeader": agentDot1qMrpMvrpPortPktRxBadHeader,
       "agentDot1qMrpMvrpPortPktRxBadFormat": agentDot1qMrpMvrpPortPktRxBadFormat,
       "agentDot1qMrpMvrpPortPktTxFailure": agentDot1qMrpMvrpPortPktTxFailure,
       "agentDot1qMrpMvrpPortPktRegFailure": agentDot1qMrpMvrpPortPktRegFailure,
       "agentDot1qMrpMvrpPktMessageFailure": agentDot1qMrpMvrpPktMessageFailure}
)
