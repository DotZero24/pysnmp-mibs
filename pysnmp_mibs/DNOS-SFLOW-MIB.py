# SNMP MIB module (DNOS-SFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/dell/DNOS-SFLOW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:09:22 2025
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

(dnOS,) = mibBuilder.importSymbols(
    "DELL-REF-MIB",
    "dnOS")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SFlowDataSource,
 SFlowInstance,
 sFlowFsEntry) = mibBuilder.importSymbols(
    "SFLOW-MIB",
    "SFlowDataSource",
    "SFlowInstance",
    "sFlowFsEntry")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fastPathSflow = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59)
)
if mibBuilder.loadTexts:
    fastPathSflow.setRevisions(
        ("2021-12-10 00:00",
         "2017-08-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AgentSflowRemoteAgentReceiver(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_AgentFastPathSflowObjects_ObjectIdentity = ObjectIdentity
agentFastPathSflowObjects = _AgentFastPathSflowObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1)
)
_AgentSflowSourceInterface_Type = InterfaceIndexOrZero
_AgentSflowSourceInterface_Object = MibScalar
agentSflowSourceInterface = _AgentSflowSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1, 1),
    _AgentSflowSourceInterface_Type()
)
agentSflowSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSflowSourceInterface.setStatus("current")


class _AgentSflowServicePortSrcInterface_Type(Integer32):
    """Custom type agentSflowServicePortSrcInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("servicePortEnable", 1),
          ("servicePortDisable", 2))
    )


_AgentSflowServicePortSrcInterface_Type.__name__ = "Integer32"
_AgentSflowServicePortSrcInterface_Object = MibScalar
agentSflowServicePortSrcInterface = _AgentSflowServicePortSrcInterface_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1, 2),
    _AgentSflowServicePortSrcInterface_Type()
)
agentSflowServicePortSrcInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSflowServicePortSrcInterface.setStatus("current")
_AgentSflowRemoteAgentTable_Object = MibTable
agentSflowRemoteAgentTable = _AgentSflowRemoteAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1, 3)
)
if mibBuilder.loadTexts:
    agentSflowRemoteAgentTable.setStatus("current")
_AgentSflowRemoteAgentEntry_Object = MibTableRow
agentSflowRemoteAgentEntry = _AgentSflowRemoteAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1, 3, 1)
)
agentSflowRemoteAgentEntry.setIndexNames(
    (0, "DNOS-SFLOW-MIB", "agentSflowRemoteAgentIndex"),
)
if mibBuilder.loadTexts:
    agentSflowRemoteAgentEntry.setStatus("current")


class _AgentSflowRemoteAgentIndex_Type(Integer32):
    """Custom type agentSflowRemoteAgentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentSflowRemoteAgentIndex_Type.__name__ = "Integer32"
_AgentSflowRemoteAgentIndex_Object = MibTableColumn
agentSflowRemoteAgentIndex = _AgentSflowRemoteAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1, 3, 1, 1),
    _AgentSflowRemoteAgentIndex_Type()
)
agentSflowRemoteAgentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSflowRemoteAgentIndex.setStatus("current")


class _AgentSflowRemoteAgentMonitorSession_Type(Integer32):
    """Custom type agentSflowRemoteAgentMonitorSession based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentSflowRemoteAgentMonitorSession_Type.__name__ = "Integer32"
_AgentSflowRemoteAgentMonitorSession_Object = MibTableColumn
agentSflowRemoteAgentMonitorSession = _AgentSflowRemoteAgentMonitorSession_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1, 3, 1, 2),
    _AgentSflowRemoteAgentMonitorSession_Type()
)
agentSflowRemoteAgentMonitorSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSflowRemoteAgentMonitorSession.setStatus("current")
_AgentSflowRemoteAgentMonitorSessionDestPort_Type = InterfaceIndexOrZero
_AgentSflowRemoteAgentMonitorSessionDestPort_Object = MibTableColumn
agentSflowRemoteAgentMonitorSessionDestPort = _AgentSflowRemoteAgentMonitorSessionDestPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1, 3, 1, 3),
    _AgentSflowRemoteAgentMonitorSessionDestPort_Type()
)
agentSflowRemoteAgentMonitorSessionDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSflowRemoteAgentMonitorSessionDestPort.setStatus("current")


class _AgentSflowRemoteAgentAddressType_Type(InetAddressType):
    """Custom type agentSflowRemoteAgentAddressType based on InetAddressType"""
    defaultValue = 1


_AgentSflowRemoteAgentAddressType_Type.__name__ = "InetAddressType"
_AgentSflowRemoteAgentAddressType_Object = MibTableColumn
agentSflowRemoteAgentAddressType = _AgentSflowRemoteAgentAddressType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1, 3, 1, 4),
    _AgentSflowRemoteAgentAddressType_Type()
)
agentSflowRemoteAgentAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSflowRemoteAgentAddressType.setStatus("current")


class _AgentSflowRemoteAgentAddress_Type(InetAddress):
    """Custom type agentSflowRemoteAgentAddress based on InetAddress"""
    defaultHexValue = "00000000"


_AgentSflowRemoteAgentAddress_Type.__name__ = "InetAddress"
_AgentSflowRemoteAgentAddress_Object = MibTableColumn
agentSflowRemoteAgentAddress = _AgentSflowRemoteAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1, 3, 1, 5),
    _AgentSflowRemoteAgentAddress_Type()
)
agentSflowRemoteAgentAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSflowRemoteAgentAddress.setStatus("current")


class _AgentSflowRemoteAgentUdpPort_Type(Integer32):
    """Custom type agentSflowRemoteAgentUdpPort based on Integer32"""
    defaultValue = 16343


_AgentSflowRemoteAgentUdpPort_Type.__name__ = "Integer32"
_AgentSflowRemoteAgentUdpPort_Object = MibTableColumn
agentSflowRemoteAgentUdpPort = _AgentSflowRemoteAgentUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1, 3, 1, 6),
    _AgentSflowRemoteAgentUdpPort_Type()
)
agentSflowRemoteAgentUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSflowRemoteAgentUdpPort.setStatus("current")
_AgentSflowFsRemoteAgentTable_Object = MibTable
agentSflowFsRemoteAgentTable = _AgentSflowFsRemoteAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1, 4)
)
if mibBuilder.loadTexts:
    agentSflowFsRemoteAgentTable.setStatus("current")
_AgentSflowFsRemoteAgentEntry_Object = MibTableRow
agentSflowFsRemoteAgentEntry = _AgentSflowFsRemoteAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1, 4, 1)
)
agentSflowFsRemoteAgentEntry.setIndexNames(
    (0, "DNOS-SFLOW-MIB", "agentSflowFsRemoteAgentDataSource"),
    (0, "DNOS-SFLOW-MIB", "agentSflowFsRemoteAgentInstance"),
)
if mibBuilder.loadTexts:
    agentSflowFsRemoteAgentEntry.setStatus("current")
_AgentSflowFsRemoteAgentDataSource_Type = SFlowDataSource
_AgentSflowFsRemoteAgentDataSource_Object = MibTableColumn
agentSflowFsRemoteAgentDataSource = _AgentSflowFsRemoteAgentDataSource_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1, 4, 1, 1),
    _AgentSflowFsRemoteAgentDataSource_Type()
)
agentSflowFsRemoteAgentDataSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSflowFsRemoteAgentDataSource.setStatus("current")
_AgentSflowFsRemoteAgentInstance_Type = SFlowInstance
_AgentSflowFsRemoteAgentInstance_Object = MibTableColumn
agentSflowFsRemoteAgentInstance = _AgentSflowFsRemoteAgentInstance_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1, 4, 1, 2),
    _AgentSflowFsRemoteAgentInstance_Type()
)
agentSflowFsRemoteAgentInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSflowFsRemoteAgentInstance.setStatus("current")


class _AgentSflowFsRemoteAgentReceiver_Type(AgentSflowRemoteAgentReceiver):
    """Custom type agentSflowFsRemoteAgentReceiver based on AgentSflowRemoteAgentReceiver"""
    defaultValue = 0


_AgentSflowFsRemoteAgentReceiver_Type.__name__ = "AgentSflowRemoteAgentReceiver"
_AgentSflowFsRemoteAgentReceiver_Object = MibTableColumn
agentSflowFsRemoteAgentReceiver = _AgentSflowFsRemoteAgentReceiver_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1, 4, 1, 3),
    _AgentSflowFsRemoteAgentReceiver_Type()
)
agentSflowFsRemoteAgentReceiver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSflowFsRemoteAgentReceiver.setStatus("current")


class _AgentSflowFsRemoteAgentPacketIngressSamplingRate_Type(Integer32):
    """Custom type agentSflowFsRemoteAgentPacketIngressSamplingRate based on Integer32"""
    defaultValue = 0


_AgentSflowFsRemoteAgentPacketIngressSamplingRate_Type.__name__ = "Integer32"
_AgentSflowFsRemoteAgentPacketIngressSamplingRate_Object = MibTableColumn
agentSflowFsRemoteAgentPacketIngressSamplingRate = _AgentSflowFsRemoteAgentPacketIngressSamplingRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1, 4, 1, 4),
    _AgentSflowFsRemoteAgentPacketIngressSamplingRate_Type()
)
agentSflowFsRemoteAgentPacketIngressSamplingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSflowFsRemoteAgentPacketIngressSamplingRate.setStatus("current")


class _AgentSflowFsRemoteAgentPacketEgressSamplingRate_Type(Integer32):
    """Custom type agentSflowFsRemoteAgentPacketEgressSamplingRate based on Integer32"""
    defaultValue = 0


_AgentSflowFsRemoteAgentPacketEgressSamplingRate_Type.__name__ = "Integer32"
_AgentSflowFsRemoteAgentPacketEgressSamplingRate_Object = MibTableColumn
agentSflowFsRemoteAgentPacketEgressSamplingRate = _AgentSflowFsRemoteAgentPacketEgressSamplingRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1, 4, 1, 5),
    _AgentSflowFsRemoteAgentPacketEgressSamplingRate_Type()
)
agentSflowFsRemoteAgentPacketEgressSamplingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSflowFsRemoteAgentPacketEgressSamplingRate.setStatus("current")


class _AgentSflowFsRemoteAgentPacketFlowBasedSamplingRate_Type(Integer32):
    """Custom type agentSflowFsRemoteAgentPacketFlowBasedSamplingRate based on Integer32"""
    defaultValue = 0


_AgentSflowFsRemoteAgentPacketFlowBasedSamplingRate_Type.__name__ = "Integer32"
_AgentSflowFsRemoteAgentPacketFlowBasedSamplingRate_Object = MibTableColumn
agentSflowFsRemoteAgentPacketFlowBasedSamplingRate = _AgentSflowFsRemoteAgentPacketFlowBasedSamplingRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1, 4, 1, 6),
    _AgentSflowFsRemoteAgentPacketFlowBasedSamplingRate_Type()
)
agentSflowFsRemoteAgentPacketFlowBasedSamplingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSflowFsRemoteAgentPacketFlowBasedSamplingRate.setStatus("current")
_AgentSflowRemoteAgentSourceInterface_Type = InterfaceIndexOrZero
_AgentSflowRemoteAgentSourceInterface_Object = MibScalar
agentSflowRemoteAgentSourceInterface = _AgentSflowRemoteAgentSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1, 5),
    _AgentSflowRemoteAgentSourceInterface_Type()
)
agentSflowRemoteAgentSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSflowRemoteAgentSourceInterface.setStatus("current")
_AgentSflowFlowFsTable_Object = MibTable
agentSflowFlowFsTable = _AgentSflowFlowFsTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1, 6)
)
if mibBuilder.loadTexts:
    agentSflowFlowFsTable.setStatus("current")
_AgentSflowFsEntry_Object = MibTableRow
agentSflowFsEntry = _AgentSflowFsEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1, 6, 1)
)
if mibBuilder.loadTexts:
    agentSflowFsEntry.setStatus("current")


class _AgentSflowFsPacketSamplingType_Type(Integer32):
    """Custom type agentSflowFsPacketSamplingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2),
          ("both", 3))
    )


_AgentSflowFsPacketSamplingType_Type.__name__ = "Integer32"
_AgentSflowFsPacketSamplingType_Object = MibTableColumn
agentSflowFsPacketSamplingType = _AgentSflowFsPacketSamplingType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1, 6, 1, 1),
    _AgentSflowFsPacketSamplingType_Type()
)
agentSflowFsPacketSamplingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSflowFsPacketSamplingType.setStatus("current")
_AgentSflowFsPacketSamplingRate_Type = Integer32
_AgentSflowFsPacketSamplingRate_Object = MibTableColumn
agentSflowFsPacketSamplingRate = _AgentSflowFsPacketSamplingRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1, 6, 1, 2),
    _AgentSflowFsPacketSamplingRate_Type()
)
agentSflowFsPacketSamplingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSflowFsPacketSamplingRate.setStatus("current")
sFlowFsEntry.registerAugmentions(
    ("DNOS-SFLOW-MIB",
     "agentSflowFsEntry")
)
agentSflowFsEntry.setIndexNames(*sFlowFsEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-SFLOW-MIB",
    **{"AgentSflowRemoteAgentReceiver": AgentSflowRemoteAgentReceiver,
       "fastPathSflow": fastPathSflow,
       "agentFastPathSflowObjects": agentFastPathSflowObjects,
       "agentSflowSourceInterface": agentSflowSourceInterface,
       "agentSflowServicePortSrcInterface": agentSflowServicePortSrcInterface,
       "agentSflowRemoteAgentTable": agentSflowRemoteAgentTable,
       "agentSflowRemoteAgentEntry": agentSflowRemoteAgentEntry,
       "agentSflowRemoteAgentIndex": agentSflowRemoteAgentIndex,
       "agentSflowRemoteAgentMonitorSession": agentSflowRemoteAgentMonitorSession,
       "agentSflowRemoteAgentMonitorSessionDestPort": agentSflowRemoteAgentMonitorSessionDestPort,
       "agentSflowRemoteAgentAddressType": agentSflowRemoteAgentAddressType,
       "agentSflowRemoteAgentAddress": agentSflowRemoteAgentAddress,
       "agentSflowRemoteAgentUdpPort": agentSflowRemoteAgentUdpPort,
       "agentSflowFsRemoteAgentTable": agentSflowFsRemoteAgentTable,
       "agentSflowFsRemoteAgentEntry": agentSflowFsRemoteAgentEntry,
       "agentSflowFsRemoteAgentDataSource": agentSflowFsRemoteAgentDataSource,
       "agentSflowFsRemoteAgentInstance": agentSflowFsRemoteAgentInstance,
       "agentSflowFsRemoteAgentReceiver": agentSflowFsRemoteAgentReceiver,
       "agentSflowFsRemoteAgentPacketIngressSamplingRate": agentSflowFsRemoteAgentPacketIngressSamplingRate,
       "agentSflowFsRemoteAgentPacketEgressSamplingRate": agentSflowFsRemoteAgentPacketEgressSamplingRate,
       "agentSflowFsRemoteAgentPacketFlowBasedSamplingRate": agentSflowFsRemoteAgentPacketFlowBasedSamplingRate,
       "agentSflowRemoteAgentSourceInterface": agentSflowRemoteAgentSourceInterface,
       "agentSflowFlowFsTable": agentSflowFlowFsTable,
       "agentSflowFsEntry": agentSflowFsEntry,
       "agentSflowFsPacketSamplingType": agentSflowFsPacketSamplingType,
       "agentSflowFsPacketSamplingRate": agentSflowFsPacketSamplingRate}
)
