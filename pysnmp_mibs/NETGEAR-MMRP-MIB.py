# SNMP MIB module (NETGEAR-MMRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/netgear/NETGEAR-MMRP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:27:14 2025
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

fastPathMMRP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 1)
)
if mibBuilder.loadTexts:
    fastPathMMRP.setRevisions(
        ("2011-04-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentDot1qMmrp_ObjectIdentity = ObjectIdentity
agentDot1qMmrp = _AgentDot1qMmrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 1, 1)
)
_AgentDot1qPortMmrpTable_Object = MibTable
agentDot1qPortMmrpTable = _AgentDot1qPortMmrpTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    agentDot1qPortMmrpTable.setStatus("current")
_AgentDot1qPortMmrpEntry_Object = MibTableRow
agentDot1qPortMmrpEntry = _AgentDot1qPortMmrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 1, 1, 1, 1)
)
agentDot1qPortMmrpEntry.setIndexNames(
    (0, "NETGEAR-MMRP-MIB", "agentDot1qMmrpPort"),
)
if mibBuilder.loadTexts:
    agentDot1qPortMmrpEntry.setStatus("current")


class _AgentDot1qMmrpPort_Type(Unsigned32):
    """Custom type agentDot1qMmrpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentDot1qMmrpPort_Type.__name__ = "Unsigned32"
_AgentDot1qMmrpPort_Object = MibTableColumn
agentDot1qMmrpPort = _AgentDot1qMmrpPort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 1, 1, 1, 1, 1),
    _AgentDot1qMmrpPort_Type()
)
agentDot1qMmrpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDot1qMmrpPort.setStatus("current")


class _AgentDot1qPortMmrpMode_Type(EnabledStatus):
    """Custom type agentDot1qPortMmrpMode based on EnabledStatus"""
    defaultValue = 2


_AgentDot1qPortMmrpMode_Type.__name__ = "EnabledStatus"
_AgentDot1qPortMmrpMode_Object = MibTableColumn
agentDot1qPortMmrpMode = _AgentDot1qPortMmrpMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 1, 1, 1, 1, 2),
    _AgentDot1qPortMmrpMode_Type()
)
agentDot1qPortMmrpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1qPortMmrpMode.setStatus("current")


class _AgentDot1qBridgeMmrpMode_Type(EnabledStatus):
    """Custom type agentDot1qBridgeMmrpMode based on EnabledStatus"""
    defaultValue = 2


_AgentDot1qBridgeMmrpMode_Type.__name__ = "EnabledStatus"
_AgentDot1qBridgeMmrpMode_Object = MibScalar
agentDot1qBridgeMmrpMode = _AgentDot1qBridgeMmrpMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 1, 1, 2),
    _AgentDot1qBridgeMmrpMode_Type()
)
agentDot1qBridgeMmrpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1qBridgeMmrpMode.setStatus("current")


class _AgentDot1qBridgeMrpPeriodicStateMachineForMmrp_Type(EnabledStatus):
    """Custom type agentDot1qBridgeMrpPeriodicStateMachineForMmrp based on EnabledStatus"""
    defaultValue = 2


_AgentDot1qBridgeMrpPeriodicStateMachineForMmrp_Type.__name__ = "EnabledStatus"
_AgentDot1qBridgeMrpPeriodicStateMachineForMmrp_Object = MibScalar
agentDot1qBridgeMrpPeriodicStateMachineForMmrp = _AgentDot1qBridgeMrpPeriodicStateMachineForMmrp_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 1, 1, 3),
    _AgentDot1qBridgeMrpPeriodicStateMachineForMmrp_Type()
)
agentDot1qBridgeMrpPeriodicStateMachineForMmrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1qBridgeMrpPeriodicStateMachineForMmrp.setStatus("current")
_AgentDot1qMrpMmrpStats_ObjectIdentity = ObjectIdentity
agentDot1qMrpMmrpStats = _AgentDot1qMrpMmrpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 1, 2)
)
_AgentDot1qMrpMmrpPktTx_Type = Counter32
_AgentDot1qMrpMmrpPktTx_Object = MibScalar
agentDot1qMrpMmrpPktTx = _AgentDot1qMrpMmrpPktTx_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 1, 2, 1),
    _AgentDot1qMrpMmrpPktTx_Type()
)
agentDot1qMrpMmrpPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1qMrpMmrpPktTx.setStatus("current")
_AgentDot1qMrpMmrpPktRx_Type = Counter32
_AgentDot1qMrpMmrpPktRx_Object = MibScalar
agentDot1qMrpMmrpPktRx = _AgentDot1qMrpMmrpPktRx_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 1, 2, 2),
    _AgentDot1qMrpMmrpPktRx_Type()
)
agentDot1qMrpMmrpPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1qMrpMmrpPktRx.setStatus("current")
_AgentDot1qMrpMmrpPktRxBadHeader_Type = Counter32
_AgentDot1qMrpMmrpPktRxBadHeader_Object = MibScalar
agentDot1qMrpMmrpPktRxBadHeader = _AgentDot1qMrpMmrpPktRxBadHeader_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 1, 2, 3),
    _AgentDot1qMrpMmrpPktRxBadHeader_Type()
)
agentDot1qMrpMmrpPktRxBadHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1qMrpMmrpPktRxBadHeader.setStatus("current")
_AgentDot1qMrpMmrpPktRxBadFormat_Type = Counter32
_AgentDot1qMrpMmrpPktRxBadFormat_Object = MibScalar
agentDot1qMrpMmrpPktRxBadFormat = _AgentDot1qMrpMmrpPktRxBadFormat_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 1, 2, 4),
    _AgentDot1qMrpMmrpPktRxBadFormat_Type()
)
agentDot1qMrpMmrpPktRxBadFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1qMrpMmrpPktRxBadFormat.setStatus("current")
_AgentDot1qMrpMmrpPktTxFailure_Type = Counter32
_AgentDot1qMrpMmrpPktTxFailure_Object = MibScalar
agentDot1qMrpMmrpPktTxFailure = _AgentDot1qMrpMmrpPktTxFailure_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 1, 2, 5),
    _AgentDot1qMrpMmrpPktTxFailure_Type()
)
agentDot1qMrpMmrpPktTxFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1qMrpMmrpPktTxFailure.setStatus("current")
_AgentDot1qMrpMmrpStatsTable_Object = MibTable
agentDot1qMrpMmrpStatsTable = _AgentDot1qMrpMmrpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    agentDot1qMrpMmrpStatsTable.setStatus("current")
_AgentDot1qMrpMmrpStatisticsEntry_Object = MibTableRow
agentDot1qMrpMmrpStatisticsEntry = _AgentDot1qMrpMmrpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 1, 2, 6, 1)
)
agentDot1qMrpMmrpStatisticsEntry.setIndexNames(
    (0, "NETGEAR-MMRP-MIB", "agentDot1qMrpMmrpIntf"),
)
if mibBuilder.loadTexts:
    agentDot1qMrpMmrpStatisticsEntry.setStatus("current")


class _AgentDot1qMrpMmrpIntf_Type(Integer32):
    """Custom type agentDot1qMrpMmrpIntf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentDot1qMrpMmrpIntf_Type.__name__ = "Integer32"
_AgentDot1qMrpMmrpIntf_Object = MibTableColumn
agentDot1qMrpMmrpIntf = _AgentDot1qMrpMmrpIntf_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 1, 2, 6, 1, 1),
    _AgentDot1qMrpMmrpIntf_Type()
)
agentDot1qMrpMmrpIntf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDot1qMrpMmrpIntf.setStatus("current")
_AgentDot1qMrpMmrpPortPktTx_Type = Counter32
_AgentDot1qMrpMmrpPortPktTx_Object = MibTableColumn
agentDot1qMrpMmrpPortPktTx = _AgentDot1qMrpMmrpPortPktTx_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 1, 2, 6, 1, 2),
    _AgentDot1qMrpMmrpPortPktTx_Type()
)
agentDot1qMrpMmrpPortPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1qMrpMmrpPortPktTx.setStatus("current")
_AgentDot1qMrpMmrpPortPktRx_Type = Counter32
_AgentDot1qMrpMmrpPortPktRx_Object = MibTableColumn
agentDot1qMrpMmrpPortPktRx = _AgentDot1qMrpMmrpPortPktRx_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 1, 2, 6, 1, 3),
    _AgentDot1qMrpMmrpPortPktRx_Type()
)
agentDot1qMrpMmrpPortPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1qMrpMmrpPortPktRx.setStatus("current")
_AgentDot1qMrpMmrpPortPktRxBadHeader_Type = Counter32
_AgentDot1qMrpMmrpPortPktRxBadHeader_Object = MibTableColumn
agentDot1qMrpMmrpPortPktRxBadHeader = _AgentDot1qMrpMmrpPortPktRxBadHeader_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 1, 2, 6, 1, 4),
    _AgentDot1qMrpMmrpPortPktRxBadHeader_Type()
)
agentDot1qMrpMmrpPortPktRxBadHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1qMrpMmrpPortPktRxBadHeader.setStatus("current")
_AgentDot1qMrpMmrpPortPktRxBadFormat_Type = Counter32
_AgentDot1qMrpMmrpPortPktRxBadFormat_Object = MibTableColumn
agentDot1qMrpMmrpPortPktRxBadFormat = _AgentDot1qMrpMmrpPortPktRxBadFormat_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 1, 2, 6, 1, 5),
    _AgentDot1qMrpMmrpPortPktRxBadFormat_Type()
)
agentDot1qMrpMmrpPortPktRxBadFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1qMrpMmrpPortPktRxBadFormat.setStatus("current")
_AgentDot1qMrpMmrpPortPktTxFailure_Type = Counter32
_AgentDot1qMrpMmrpPortPktTxFailure_Object = MibTableColumn
agentDot1qMrpMmrpPortPktTxFailure = _AgentDot1qMrpMmrpPortPktTxFailure_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2, 1, 2, 6, 1, 6),
    _AgentDot1qMrpMmrpPortPktTxFailure_Type()
)
agentDot1qMrpMmrpPortPktTxFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot1qMrpMmrpPortPktTxFailure.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETGEAR-MMRP-MIB",
    **{"fastPathMMRP": fastPathMMRP,
       "agentDot1qMmrp": agentDot1qMmrp,
       "agentDot1qPortMmrpTable": agentDot1qPortMmrpTable,
       "agentDot1qPortMmrpEntry": agentDot1qPortMmrpEntry,
       "agentDot1qMmrpPort": agentDot1qMmrpPort,
       "agentDot1qPortMmrpMode": agentDot1qPortMmrpMode,
       "agentDot1qBridgeMmrpMode": agentDot1qBridgeMmrpMode,
       "agentDot1qBridgeMrpPeriodicStateMachineForMmrp": agentDot1qBridgeMrpPeriodicStateMachineForMmrp,
       "agentDot1qMrpMmrpStats": agentDot1qMrpMmrpStats,
       "agentDot1qMrpMmrpPktTx": agentDot1qMrpMmrpPktTx,
       "agentDot1qMrpMmrpPktRx": agentDot1qMrpMmrpPktRx,
       "agentDot1qMrpMmrpPktRxBadHeader": agentDot1qMrpMmrpPktRxBadHeader,
       "agentDot1qMrpMmrpPktRxBadFormat": agentDot1qMrpMmrpPktRxBadFormat,
       "agentDot1qMrpMmrpPktTxFailure": agentDot1qMrpMmrpPktTxFailure,
       "agentDot1qMrpMmrpStatsTable": agentDot1qMrpMmrpStatsTable,
       "agentDot1qMrpMmrpStatisticsEntry": agentDot1qMrpMmrpStatisticsEntry,
       "agentDot1qMrpMmrpIntf": agentDot1qMrpMmrpIntf,
       "agentDot1qMrpMmrpPortPktTx": agentDot1qMrpMmrpPortPktTx,
       "agentDot1qMrpMmrpPortPktRx": agentDot1qMrpMmrpPortPktRx,
       "agentDot1qMrpMmrpPortPktRxBadHeader": agentDot1qMrpMmrpPortPktRxBadHeader,
       "agentDot1qMrpMmrpPortPktRxBadFormat": agentDot1qMrpMmrpPortPktRxBadFormat,
       "agentDot1qMrpMmrpPortPktTxFailure": agentDot1qMrpMmrpPortPktTxFailure}
)
