_L='agentSflowFsEntry'
_K='AgentSflowRemoteAgentReceiver'
_J='agentSflowFsRemoteAgentInstance'
_I='agentSflowFsRemoteAgentDataSource'
_H='agentSflowRemoteAgentIndex'
_G='InetAddressType'
_F='InetAddress'
_E='not-accessible'
_D='DNOS-SFLOW-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dnOS,=mibBuilder.importSymbols('DELL-REF-MIB','dnOS')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_F,_G)
SFlowDataSource,SFlowInstance,sFlowFsEntry=mibBuilder.importSymbols('SFLOW-MIB','SFlowDataSource','SFlowInstance','sFlowFsEntry')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fastPathSflow=ModuleIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59))
if mibBuilder.loadTexts:fastPathSflow.setRevisions(('2021-12-10 00:00','2017-08-11 00:00'))
class AgentSflowRemoteAgentReceiver(TextualConvention,Integer32):status=_A
_AgentFastPathSflowObjects_ObjectIdentity=ObjectIdentity
agentFastPathSflowObjects=_AgentFastPathSflowObjects_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59,1))
_AgentSflowSourceInterface_Type=InterfaceIndexOrZero
_AgentSflowSourceInterface_Object=MibScalar
agentSflowSourceInterface=_AgentSflowSourceInterface_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59,1,1),_AgentSflowSourceInterface_Type())
agentSflowSourceInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSflowSourceInterface.setStatus(_A)
class _AgentSflowServicePortSrcInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('servicePortEnable',1),('servicePortDisable',2)))
_AgentSflowServicePortSrcInterface_Type.__name__=_C
_AgentSflowServicePortSrcInterface_Object=MibScalar
agentSflowServicePortSrcInterface=_AgentSflowServicePortSrcInterface_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59,1,2),_AgentSflowServicePortSrcInterface_Type())
agentSflowServicePortSrcInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSflowServicePortSrcInterface.setStatus(_A)
_AgentSflowRemoteAgentTable_Object=MibTable
agentSflowRemoteAgentTable=_AgentSflowRemoteAgentTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59,1,3))
if mibBuilder.loadTexts:agentSflowRemoteAgentTable.setStatus(_A)
_AgentSflowRemoteAgentEntry_Object=MibTableRow
agentSflowRemoteAgentEntry=_AgentSflowRemoteAgentEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59,1,3,1))
agentSflowRemoteAgentEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:agentSflowRemoteAgentEntry.setStatus(_A)
class _AgentSflowRemoteAgentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentSflowRemoteAgentIndex_Type.__name__=_C
_AgentSflowRemoteAgentIndex_Object=MibTableColumn
agentSflowRemoteAgentIndex=_AgentSflowRemoteAgentIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59,1,3,1,1),_AgentSflowRemoteAgentIndex_Type())
agentSflowRemoteAgentIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:agentSflowRemoteAgentIndex.setStatus(_A)
class _AgentSflowRemoteAgentMonitorSession_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AgentSflowRemoteAgentMonitorSession_Type.__name__=_C
_AgentSflowRemoteAgentMonitorSession_Object=MibTableColumn
agentSflowRemoteAgentMonitorSession=_AgentSflowRemoteAgentMonitorSession_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59,1,3,1,2),_AgentSflowRemoteAgentMonitorSession_Type())
agentSflowRemoteAgentMonitorSession.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSflowRemoteAgentMonitorSession.setStatus(_A)
_AgentSflowRemoteAgentMonitorSessionDestPort_Type=InterfaceIndexOrZero
_AgentSflowRemoteAgentMonitorSessionDestPort_Object=MibTableColumn
agentSflowRemoteAgentMonitorSessionDestPort=_AgentSflowRemoteAgentMonitorSessionDestPort_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59,1,3,1,3),_AgentSflowRemoteAgentMonitorSessionDestPort_Type())
agentSflowRemoteAgentMonitorSessionDestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSflowRemoteAgentMonitorSessionDestPort.setStatus(_A)
class _AgentSflowRemoteAgentAddressType_Type(InetAddressType):defaultValue=1
_AgentSflowRemoteAgentAddressType_Type.__name__=_G
_AgentSflowRemoteAgentAddressType_Object=MibTableColumn
agentSflowRemoteAgentAddressType=_AgentSflowRemoteAgentAddressType_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59,1,3,1,4),_AgentSflowRemoteAgentAddressType_Type())
agentSflowRemoteAgentAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSflowRemoteAgentAddressType.setStatus(_A)
class _AgentSflowRemoteAgentAddress_Type(InetAddress):defaultHexValue='00000000'
_AgentSflowRemoteAgentAddress_Type.__name__=_F
_AgentSflowRemoteAgentAddress_Object=MibTableColumn
agentSflowRemoteAgentAddress=_AgentSflowRemoteAgentAddress_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59,1,3,1,5),_AgentSflowRemoteAgentAddress_Type())
agentSflowRemoteAgentAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSflowRemoteAgentAddress.setStatus(_A)
class _AgentSflowRemoteAgentUdpPort_Type(Integer32):defaultValue=16343
_AgentSflowRemoteAgentUdpPort_Type.__name__=_C
_AgentSflowRemoteAgentUdpPort_Object=MibTableColumn
agentSflowRemoteAgentUdpPort=_AgentSflowRemoteAgentUdpPort_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59,1,3,1,6),_AgentSflowRemoteAgentUdpPort_Type())
agentSflowRemoteAgentUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSflowRemoteAgentUdpPort.setStatus(_A)
_AgentSflowFsRemoteAgentTable_Object=MibTable
agentSflowFsRemoteAgentTable=_AgentSflowFsRemoteAgentTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59,1,4))
if mibBuilder.loadTexts:agentSflowFsRemoteAgentTable.setStatus(_A)
_AgentSflowFsRemoteAgentEntry_Object=MibTableRow
agentSflowFsRemoteAgentEntry=_AgentSflowFsRemoteAgentEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59,1,4,1))
agentSflowFsRemoteAgentEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:agentSflowFsRemoteAgentEntry.setStatus(_A)
_AgentSflowFsRemoteAgentDataSource_Type=SFlowDataSource
_AgentSflowFsRemoteAgentDataSource_Object=MibTableColumn
agentSflowFsRemoteAgentDataSource=_AgentSflowFsRemoteAgentDataSource_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59,1,4,1,1),_AgentSflowFsRemoteAgentDataSource_Type())
agentSflowFsRemoteAgentDataSource.setMaxAccess(_E)
if mibBuilder.loadTexts:agentSflowFsRemoteAgentDataSource.setStatus(_A)
_AgentSflowFsRemoteAgentInstance_Type=SFlowInstance
_AgentSflowFsRemoteAgentInstance_Object=MibTableColumn
agentSflowFsRemoteAgentInstance=_AgentSflowFsRemoteAgentInstance_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59,1,4,1,2),_AgentSflowFsRemoteAgentInstance_Type())
agentSflowFsRemoteAgentInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:agentSflowFsRemoteAgentInstance.setStatus(_A)
class _AgentSflowFsRemoteAgentReceiver_Type(AgentSflowRemoteAgentReceiver):defaultValue=0
_AgentSflowFsRemoteAgentReceiver_Type.__name__=_K
_AgentSflowFsRemoteAgentReceiver_Object=MibTableColumn
agentSflowFsRemoteAgentReceiver=_AgentSflowFsRemoteAgentReceiver_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59,1,4,1,3),_AgentSflowFsRemoteAgentReceiver_Type())
agentSflowFsRemoteAgentReceiver.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSflowFsRemoteAgentReceiver.setStatus(_A)
class _AgentSflowFsRemoteAgentPacketIngressSamplingRate_Type(Integer32):defaultValue=0
_AgentSflowFsRemoteAgentPacketIngressSamplingRate_Type.__name__=_C
_AgentSflowFsRemoteAgentPacketIngressSamplingRate_Object=MibTableColumn
agentSflowFsRemoteAgentPacketIngressSamplingRate=_AgentSflowFsRemoteAgentPacketIngressSamplingRate_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59,1,4,1,4),_AgentSflowFsRemoteAgentPacketIngressSamplingRate_Type())
agentSflowFsRemoteAgentPacketIngressSamplingRate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSflowFsRemoteAgentPacketIngressSamplingRate.setStatus(_A)
class _AgentSflowFsRemoteAgentPacketEgressSamplingRate_Type(Integer32):defaultValue=0
_AgentSflowFsRemoteAgentPacketEgressSamplingRate_Type.__name__=_C
_AgentSflowFsRemoteAgentPacketEgressSamplingRate_Object=MibTableColumn
agentSflowFsRemoteAgentPacketEgressSamplingRate=_AgentSflowFsRemoteAgentPacketEgressSamplingRate_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59,1,4,1,5),_AgentSflowFsRemoteAgentPacketEgressSamplingRate_Type())
agentSflowFsRemoteAgentPacketEgressSamplingRate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSflowFsRemoteAgentPacketEgressSamplingRate.setStatus(_A)
class _AgentSflowFsRemoteAgentPacketFlowBasedSamplingRate_Type(Integer32):defaultValue=0
_AgentSflowFsRemoteAgentPacketFlowBasedSamplingRate_Type.__name__=_C
_AgentSflowFsRemoteAgentPacketFlowBasedSamplingRate_Object=MibTableColumn
agentSflowFsRemoteAgentPacketFlowBasedSamplingRate=_AgentSflowFsRemoteAgentPacketFlowBasedSamplingRate_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59,1,4,1,6),_AgentSflowFsRemoteAgentPacketFlowBasedSamplingRate_Type())
agentSflowFsRemoteAgentPacketFlowBasedSamplingRate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSflowFsRemoteAgentPacketFlowBasedSamplingRate.setStatus(_A)
_AgentSflowRemoteAgentSourceInterface_Type=InterfaceIndexOrZero
_AgentSflowRemoteAgentSourceInterface_Object=MibScalar
agentSflowRemoteAgentSourceInterface=_AgentSflowRemoteAgentSourceInterface_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59,1,5),_AgentSflowRemoteAgentSourceInterface_Type())
agentSflowRemoteAgentSourceInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSflowRemoteAgentSourceInterface.setStatus(_A)
_AgentSflowFlowFsTable_Object=MibTable
agentSflowFlowFsTable=_AgentSflowFlowFsTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59,1,6))
if mibBuilder.loadTexts:agentSflowFlowFsTable.setStatus(_A)
_AgentSflowFsEntry_Object=MibTableRow
agentSflowFsEntry=_AgentSflowFsEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59,1,6,1))
if mibBuilder.loadTexts:agentSflowFsEntry.setStatus(_A)
class _AgentSflowFsPacketSamplingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ingress',1),('egress',2),('both',3)))
_AgentSflowFsPacketSamplingType_Type.__name__=_C
_AgentSflowFsPacketSamplingType_Object=MibTableColumn
agentSflowFsPacketSamplingType=_AgentSflowFsPacketSamplingType_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59,1,6,1,1),_AgentSflowFsPacketSamplingType_Type())
agentSflowFsPacketSamplingType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSflowFsPacketSamplingType.setStatus(_A)
_AgentSflowFsPacketSamplingRate_Type=Integer32
_AgentSflowFsPacketSamplingRate_Object=MibTableColumn
agentSflowFsPacketSamplingRate=_AgentSflowFsPacketSamplingRate_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,59,1,6,1,2),_AgentSflowFsPacketSamplingRate_Type())
agentSflowFsPacketSamplingRate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSflowFsPacketSamplingRate.setStatus(_A)
sFlowFsEntry.registerAugmentions((_D,_L))
agentSflowFsEntry.setIndexNames(*sFlowFsEntry.getIndexNames())
mibBuilder.exportSymbols(_D,**{_K:AgentSflowRemoteAgentReceiver,'fastPathSflow':fastPathSflow,'agentFastPathSflowObjects':agentFastPathSflowObjects,'agentSflowSourceInterface':agentSflowSourceInterface,'agentSflowServicePortSrcInterface':agentSflowServicePortSrcInterface,'agentSflowRemoteAgentTable':agentSflowRemoteAgentTable,'agentSflowRemoteAgentEntry':agentSflowRemoteAgentEntry,_H:agentSflowRemoteAgentIndex,'agentSflowRemoteAgentMonitorSession':agentSflowRemoteAgentMonitorSession,'agentSflowRemoteAgentMonitorSessionDestPort':agentSflowRemoteAgentMonitorSessionDestPort,'agentSflowRemoteAgentAddressType':agentSflowRemoteAgentAddressType,'agentSflowRemoteAgentAddress':agentSflowRemoteAgentAddress,'agentSflowRemoteAgentUdpPort':agentSflowRemoteAgentUdpPort,'agentSflowFsRemoteAgentTable':agentSflowFsRemoteAgentTable,'agentSflowFsRemoteAgentEntry':agentSflowFsRemoteAgentEntry,_I:agentSflowFsRemoteAgentDataSource,_J:agentSflowFsRemoteAgentInstance,'agentSflowFsRemoteAgentReceiver':agentSflowFsRemoteAgentReceiver,'agentSflowFsRemoteAgentPacketIngressSamplingRate':agentSflowFsRemoteAgentPacketIngressSamplingRate,'agentSflowFsRemoteAgentPacketEgressSamplingRate':agentSflowFsRemoteAgentPacketEgressSamplingRate,'agentSflowFsRemoteAgentPacketFlowBasedSamplingRate':agentSflowFsRemoteAgentPacketFlowBasedSamplingRate,'agentSflowRemoteAgentSourceInterface':agentSflowRemoteAgentSourceInterface,'agentSflowFlowFsTable':agentSflowFlowFsTable,_L:agentSflowFsEntry,'agentSflowFsPacketSamplingType':agentSflowFsPacketSamplingType,'agentSflowFsPacketSamplingRate':agentSflowFsPacketSamplingRate})