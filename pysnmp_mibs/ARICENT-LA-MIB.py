_n='fsLaDLAGTrapType'
_m='fsLaHwFailTrapType'
_l='fsLaMCLAGRemotePortIndex'
_k='outofSync'
_j='inSync'
_i='fsLaDLAGRemotePortIndex'
_h='fsLaDLAGTrapPortChannelIndex'
_g='fsLaTrapPortIndex'
_f='fsLaTrapPortChannelIndex'
_e='fsLaPortIndex'
_d='backupmaster'
_c='milliseconds'
_b='dynamic'
_a='deprecated'
_Z='000000000000'
_Y='seconds'
_X='shutdown'
_W='TruthValue'
_V='TimeTicks'
_U='InterfaceIndexOrZero'
_T='fsLaMCLAGRemotePortChannelSystemID'
_S='fsLaDLAGRemotePortChannelSystemID'
_R='upIndividual'
_Q='down'
_P='standby'
_O='upInBndl'
_N='MacAddress'
_M='slave'
_L='master'
_K='fsLaPortChannelIfIndex'
_J='none'
_I='disabled'
_H='enabled'
_G='not-accessible'
_F='Unsigned32'
_E='ARICENT-LA-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex',_U)
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_V,_F,'enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_N,'PhysAddress','TextualConvention',_W)
fsla=ModuleIdentity((1,3,6,1,4,1,2076,63))
if mibBuilder.loadTexts:fsla.setRevisions(('2014-03-01 00:00',))
class PortLaMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('lacp',1),('manual',2),('disable',3)))
class LacpKey(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class LacpState(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('lacpActivity',0),('lacpTimeout',1),('aggregation',2),('synchronization',3),('collecting',4),('distributing',5),('defaulted',6),('expired',7)))
_FsLaSystem_ObjectIdentity=ObjectIdentity
fsLaSystem=_FsLaSystem_ObjectIdentity((1,3,6,1,4,1,2076,63,1))
class _FsLaSystemControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),(_X,2)))
_FsLaSystemControl_Type.__name__=_D
_FsLaSystemControl_Object=MibScalar
fsLaSystemControl=_FsLaSystemControl_Object((1,3,6,1,4,1,2076,63,1,1),_FsLaSystemControl_Type())
fsLaSystemControl.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaSystemControl.setStatus(_A)
class _FsLaStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsLaStatus_Type.__name__=_D
_FsLaStatus_Object=MibScalar
fsLaStatus=_FsLaStatus_Object((1,3,6,1,4,1,2076,63,1,2),_FsLaStatus_Type())
fsLaStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaStatus.setStatus(_A)
class _FsLaTraceOption_Type(Integer32):defaultValue=0
_FsLaTraceOption_Type.__name__=_D
_FsLaTraceOption_Object=MibScalar
fsLaTraceOption=_FsLaTraceOption_Object((1,3,6,1,4,1,2076,63,1,3),_FsLaTraceOption_Type())
fsLaTraceOption.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaTraceOption.setStatus(_A)
_FsLaMaxPortsPerPortChannel_Type=Integer32
_FsLaMaxPortsPerPortChannel_Object=MibScalar
fsLaMaxPortsPerPortChannel=_FsLaMaxPortsPerPortChannel_Object((1,3,6,1,4,1,2076,63,1,4),_FsLaMaxPortsPerPortChannel_Type())
fsLaMaxPortsPerPortChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaMaxPortsPerPortChannel.setStatus(_A)
_FsLaMaxPortChannels_Type=Integer32
_FsLaMaxPortChannels_Object=MibScalar
fsLaMaxPortChannels=_FsLaMaxPortChannels_Object((1,3,6,1,4,1,2076,63,1,5),_FsLaMaxPortChannels_Type())
fsLaMaxPortChannels.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaMaxPortChannels.setStatus(_A)
class _FsLaOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsLaOperStatus_Type.__name__=_D
_FsLaOperStatus_Object=MibScalar
fsLaOperStatus=_FsLaOperStatus_Object((1,3,6,1,4,1,2076,63,1,6),_FsLaOperStatus_Type())
fsLaOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaOperStatus.setStatus(_A)
_FsLaActorSystemID_Type=MacAddress
_FsLaActorSystemID_Object=MibScalar
fsLaActorSystemID=_FsLaActorSystemID_Object((1,3,6,1,4,1,2076,63,1,7),_FsLaActorSystemID_Type())
fsLaActorSystemID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaActorSystemID.setStatus(_A)
class _FsLaNoPartnerIndep_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsLaNoPartnerIndep_Type.__name__=_D
_FsLaNoPartnerIndep_Object=MibScalar
fsLaNoPartnerIndep=_FsLaNoPartnerIndep_Object((1,3,6,1,4,1,2076,63,1,8),_FsLaNoPartnerIndep_Type())
fsLaNoPartnerIndep.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaNoPartnerIndep.setStatus(_A)
class _FsLaDLAGSystemStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsLaDLAGSystemStatus_Type.__name__=_D
_FsLaDLAGSystemStatus_Object=MibScalar
fsLaDLAGSystemStatus=_FsLaDLAGSystemStatus_Object((1,3,6,1,4,1,2076,63,1,9),_FsLaDLAGSystemStatus_Type())
fsLaDLAGSystemStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaDLAGSystemStatus.setStatus(_A)
_FsLaDLAGSystemID_Type=MacAddress
_FsLaDLAGSystemID_Object=MibScalar
fsLaDLAGSystemID=_FsLaDLAGSystemID_Object((1,3,6,1,4,1,2076,63,1,10),_FsLaDLAGSystemID_Type())
fsLaDLAGSystemID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaDLAGSystemID.setStatus(_A)
class _FsLaDLAGSystemPriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsLaDLAGSystemPriority_Type.__name__=_D
_FsLaDLAGSystemPriority_Object=MibScalar
fsLaDLAGSystemPriority=_FsLaDLAGSystemPriority_Object((1,3,6,1,4,1,2076,63,1,11),_FsLaDLAGSystemPriority_Type())
fsLaDLAGSystemPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaDLAGSystemPriority.setStatus(_A)
class _FsLaDLAGPeriodicSyncTime_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,90))
_FsLaDLAGPeriodicSyncTime_Type.__name__=_F
_FsLaDLAGPeriodicSyncTime_Object=MibScalar
fsLaDLAGPeriodicSyncTime=_FsLaDLAGPeriodicSyncTime_Object((1,3,6,1,4,1,2076,63,1,12),_FsLaDLAGPeriodicSyncTime_Type())
fsLaDLAGPeriodicSyncTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaDLAGPeriodicSyncTime.setStatus(_A)
if mibBuilder.loadTexts:fsLaDLAGPeriodicSyncTime.setUnits(_Y)
class _FsLaDLAGRolePlayed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_L,1),(_M,2)))
_FsLaDLAGRolePlayed_Type.__name__=_D
_FsLaDLAGRolePlayed_Object=MibScalar
fsLaDLAGRolePlayed=_FsLaDLAGRolePlayed_Object((1,3,6,1,4,1,2076,63,1,13),_FsLaDLAGRolePlayed_Type())
fsLaDLAGRolePlayed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaDLAGRolePlayed.setStatus(_A)
_FsLaDLAGDistributingPortIndex_Type=InterfaceIndexOrZero
_FsLaDLAGDistributingPortIndex_Object=MibScalar
fsLaDLAGDistributingPortIndex=_FsLaDLAGDistributingPortIndex_Object((1,3,6,1,4,1,2076,63,1,14),_FsLaDLAGDistributingPortIndex_Type())
fsLaDLAGDistributingPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaDLAGDistributingPortIndex.setStatus(_A)
_FsLaDLAGDistributingPortList_Type=PortList
_FsLaDLAGDistributingPortList_Object=MibScalar
fsLaDLAGDistributingPortList=_FsLaDLAGDistributingPortList_Object((1,3,6,1,4,1,2076,63,1,15),_FsLaDLAGDistributingPortList_Type())
fsLaDLAGDistributingPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaDLAGDistributingPortList.setStatus(_A)
class _FsLaMCLAGSystemStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsLaMCLAGSystemStatus_Type.__name__=_D
_FsLaMCLAGSystemStatus_Object=MibScalar
fsLaMCLAGSystemStatus=_FsLaMCLAGSystemStatus_Object((1,3,6,1,4,1,2076,63,1,16),_FsLaMCLAGSystemStatus_Type())
fsLaMCLAGSystemStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaMCLAGSystemStatus.setStatus(_A)
class _FsLaMCLAGSystemID_Type(MacAddress):defaultHexValue=_Z
_FsLaMCLAGSystemID_Type.__name__=_N
_FsLaMCLAGSystemID_Object=MibScalar
fsLaMCLAGSystemID=_FsLaMCLAGSystemID_Object((1,3,6,1,4,1,2076,63,1,17),_FsLaMCLAGSystemID_Type())
fsLaMCLAGSystemID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaMCLAGSystemID.setStatus(_A)
class _FsLaMCLAGSystemPriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsLaMCLAGSystemPriority_Type.__name__=_D
_FsLaMCLAGSystemPriority_Object=MibScalar
fsLaMCLAGSystemPriority=_FsLaMCLAGSystemPriority_Object((1,3,6,1,4,1,2076,63,1,18),_FsLaMCLAGSystemPriority_Type())
fsLaMCLAGSystemPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaMCLAGSystemPriority.setStatus(_A)
class _FsLaMCLAGPeriodicSyncTime_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,90))
_FsLaMCLAGPeriodicSyncTime_Type.__name__=_F
_FsLaMCLAGPeriodicSyncTime_Object=MibScalar
fsLaMCLAGPeriodicSyncTime=_FsLaMCLAGPeriodicSyncTime_Object((1,3,6,1,4,1,2076,63,1,19),_FsLaMCLAGPeriodicSyncTime_Type())
fsLaMCLAGPeriodicSyncTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaMCLAGPeriodicSyncTime.setStatus(_A)
if mibBuilder.loadTexts:fsLaMCLAGPeriodicSyncTime.setUnits(_Y)
class _FsLaRecTmrDuration_Type(Unsigned32):defaultValue=90;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_FsLaRecTmrDuration_Type.__name__=_F
_FsLaRecTmrDuration_Object=MibScalar
fsLaRecTmrDuration=_FsLaRecTmrDuration_Object((1,3,6,1,4,1,2076,63,1,20),_FsLaRecTmrDuration_Type())
fsLaRecTmrDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaRecTmrDuration.setStatus(_A)
class _FsLaRecThreshold_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_FsLaRecThreshold_Type.__name__=_F
_FsLaRecThreshold_Object=MibScalar
fsLaRecThreshold=_FsLaRecThreshold_Object((1,3,6,1,4,1,2076,63,1,21),_FsLaRecThreshold_Type())
fsLaRecThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaRecThreshold.setStatus(_A)
_FsLaTotalErrRecCount_Type=Counter32
_FsLaTotalErrRecCount_Object=MibScalar
fsLaTotalErrRecCount=_FsLaTotalErrRecCount_Object((1,3,6,1,4,1,2076,63,1,22),_FsLaTotalErrRecCount_Type())
fsLaTotalErrRecCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaTotalErrRecCount.setStatus(_A)
class _FsLaDefaultedStateThreshold_Type(Unsigned32):defaultValue=5
_FsLaDefaultedStateThreshold_Type.__name__=_F
_FsLaDefaultedStateThreshold_Object=MibScalar
fsLaDefaultedStateThreshold=_FsLaDefaultedStateThreshold_Object((1,3,6,1,4,1,2076,63,1,23),_FsLaDefaultedStateThreshold_Type())
fsLaDefaultedStateThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaDefaultedStateThreshold.setStatus(_A)
class _FsLaHardwareFailureRecThreshold_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_FsLaHardwareFailureRecThreshold_Type.__name__=_F
_FsLaHardwareFailureRecThreshold_Object=MibScalar
fsLaHardwareFailureRecThreshold=_FsLaHardwareFailureRecThreshold_Object((1,3,6,1,4,1,2076,63,1,24),_FsLaHardwareFailureRecThreshold_Type())
fsLaHardwareFailureRecThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaHardwareFailureRecThreshold.setStatus(_A)
class _FsLaSameStateRecThreshold_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_FsLaSameStateRecThreshold_Type.__name__=_F
_FsLaSameStateRecThreshold_Object=MibScalar
fsLaSameStateRecThreshold=_FsLaSameStateRecThreshold_Object((1,3,6,1,4,1,2076,63,1,25),_FsLaSameStateRecThreshold_Type())
fsLaSameStateRecThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaSameStateRecThreshold.setStatus(_A)
class _FsLaRecThresholdExceedAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_X,2)))
_FsLaRecThresholdExceedAction_Type.__name__=_D
_FsLaRecThresholdExceedAction_Object=MibScalar
fsLaRecThresholdExceedAction=_FsLaRecThresholdExceedAction_Object((1,3,6,1,4,1,2076,63,1,26),_FsLaRecThresholdExceedAction_Type())
fsLaRecThresholdExceedAction.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaRecThresholdExceedAction.setStatus(_A)
class _FsLaMCLAGClearCounters_Type(TruthValue):defaultValue=2
_FsLaMCLAGClearCounters_Type.__name__=_W
_FsLaMCLAGClearCounters_Object=MibScalar
fsLaMCLAGClearCounters=_FsLaMCLAGClearCounters_Object((1,3,6,1,4,1,2076,63,1,27),_FsLaMCLAGClearCounters_Type())
fsLaMCLAGClearCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaMCLAGClearCounters.setStatus(_A)
_FsLaPortChannel_ObjectIdentity=ObjectIdentity
fsLaPortChannel=_FsLaPortChannel_ObjectIdentity((1,3,6,1,4,1,2076,63,2))
_FsLaPortChannelTable_Object=MibTable
fsLaPortChannelTable=_FsLaPortChannelTable_Object((1,3,6,1,4,1,2076,63,2,1))
if mibBuilder.loadTexts:fsLaPortChannelTable.setStatus(_A)
_FsLaPortChannelEntry_Object=MibTableRow
fsLaPortChannelEntry=_FsLaPortChannelEntry_Object((1,3,6,1,4,1,2076,63,2,1,1))
fsLaPortChannelEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:fsLaPortChannelEntry.setStatus(_A)
_FsLaPortChannelIfIndex_Type=InterfaceIndex
_FsLaPortChannelIfIndex_Object=MibTableColumn
fsLaPortChannelIfIndex=_FsLaPortChannelIfIndex_Object((1,3,6,1,4,1,2076,63,2,1,1,1),_FsLaPortChannelIfIndex_Type())
fsLaPortChannelIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fsLaPortChannelIfIndex.setStatus(_A)
_FsLaPortChannelGroup_Type=LacpKey
_FsLaPortChannelGroup_Object=MibTableColumn
fsLaPortChannelGroup=_FsLaPortChannelGroup_Object((1,3,6,1,4,1,2076,63,2,1,1,2),_FsLaPortChannelGroup_Type())
fsLaPortChannelGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaPortChannelGroup.setStatus(_A)
_FsLaPortChannelAdminMacAddress_Type=MacAddress
_FsLaPortChannelAdminMacAddress_Object=MibTableColumn
fsLaPortChannelAdminMacAddress=_FsLaPortChannelAdminMacAddress_Object((1,3,6,1,4,1,2076,63,2,1,1,3),_FsLaPortChannelAdminMacAddress_Type())
fsLaPortChannelAdminMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortChannelAdminMacAddress.setStatus(_a)
class _FsLaPortChannelMacSelection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),('force',2)))
_FsLaPortChannelMacSelection_Type.__name__=_D
_FsLaPortChannelMacSelection_Object=MibTableColumn
fsLaPortChannelMacSelection=_FsLaPortChannelMacSelection_Object((1,3,6,1,4,1,2076,63,2,1,1,4),_FsLaPortChannelMacSelection_Type())
fsLaPortChannelMacSelection.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortChannelMacSelection.setStatus(_a)
_FsLaPortChannelMode_Type=PortLaMode
_FsLaPortChannelMode_Object=MibTableColumn
fsLaPortChannelMode=_FsLaPortChannelMode_Object((1,3,6,1,4,1,2076,63,2,1,1,5),_FsLaPortChannelMode_Type())
fsLaPortChannelMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaPortChannelMode.setStatus(_A)
_FsLaPortChannelPortCount_Type=Integer32
_FsLaPortChannelPortCount_Object=MibTableColumn
fsLaPortChannelPortCount=_FsLaPortChannelPortCount_Object((1,3,6,1,4,1,2076,63,2,1,1,6),_FsLaPortChannelPortCount_Type())
fsLaPortChannelPortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaPortChannelPortCount.setStatus(_A)
_FsLaPortChannelActivePortCount_Type=Integer32
_FsLaPortChannelActivePortCount_Object=MibTableColumn
fsLaPortChannelActivePortCount=_FsLaPortChannelActivePortCount_Object((1,3,6,1,4,1,2076,63,2,1,1,7),_FsLaPortChannelActivePortCount_Type())
fsLaPortChannelActivePortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaPortChannelActivePortCount.setStatus(_A)
class _FsLaPortChannelSelectionPolicy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('macSrc',1),('macDst',2),('macSrcDst',3),('ipSrc',4),('ipDst',5),('ipSrcDst',6),('vlanId',7),('isid',8),('macSrcVid',9),('macDstVid',10),('macSrcDstVid',11),('mplsVcLabel',12),('mplsTunnelLabel',13),('mplsVcTunnelLabel',14)))
_FsLaPortChannelSelectionPolicy_Type.__name__=_D
_FsLaPortChannelSelectionPolicy_Object=MibTableColumn
fsLaPortChannelSelectionPolicy=_FsLaPortChannelSelectionPolicy_Object((1,3,6,1,4,1,2076,63,2,1,1,8),_FsLaPortChannelSelectionPolicy_Type())
fsLaPortChannelSelectionPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortChannelSelectionPolicy.setStatus(_A)
class _FsLaPortChannelDefaultPortIndex_Type(InterfaceIndexOrZero):defaultValue=0
_FsLaPortChannelDefaultPortIndex_Type.__name__=_U
_FsLaPortChannelDefaultPortIndex_Object=MibTableColumn
fsLaPortChannelDefaultPortIndex=_FsLaPortChannelDefaultPortIndex_Object((1,3,6,1,4,1,2076,63,2,1,1,9),_FsLaPortChannelDefaultPortIndex_Type())
fsLaPortChannelDefaultPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortChannelDefaultPortIndex.setStatus(_A)
class _FsLaPortChannelMaxPorts_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,8))
_FsLaPortChannelMaxPorts_Type.__name__=_D
_FsLaPortChannelMaxPorts_Object=MibTableColumn
fsLaPortChannelMaxPorts=_FsLaPortChannelMaxPorts_Object((1,3,6,1,4,1,2076,63,2,1,1,10),_FsLaPortChannelMaxPorts_Type())
fsLaPortChannelMaxPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortChannelMaxPorts.setStatus(_A)
_FsLaPortChannelSelectionPolicyBitList_Type=Integer32
_FsLaPortChannelSelectionPolicyBitList_Object=MibTableColumn
fsLaPortChannelSelectionPolicyBitList=_FsLaPortChannelSelectionPolicyBitList_Object((1,3,6,1,4,1,2076,63,2,1,1,11),_FsLaPortChannelSelectionPolicyBitList_Type())
fsLaPortChannelSelectionPolicyBitList.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortChannelSelectionPolicyBitList.setStatus(_A)
_FsLaPortChannelDLAGDistributingPortIndex_Type=InterfaceIndexOrZero
_FsLaPortChannelDLAGDistributingPortIndex_Object=MibTableColumn
fsLaPortChannelDLAGDistributingPortIndex=_FsLaPortChannelDLAGDistributingPortIndex_Object((1,3,6,1,4,1,2076,63,2,1,1,12),_FsLaPortChannelDLAGDistributingPortIndex_Type())
fsLaPortChannelDLAGDistributingPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortChannelDLAGDistributingPortIndex.setStatus(_A)
_FsLaPortChannelDLAGSystemID_Type=MacAddress
_FsLaPortChannelDLAGSystemID_Object=MibTableColumn
fsLaPortChannelDLAGSystemID=_FsLaPortChannelDLAGSystemID_Object((1,3,6,1,4,1,2076,63,2,1,1,13),_FsLaPortChannelDLAGSystemID_Type())
fsLaPortChannelDLAGSystemID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortChannelDLAGSystemID.setStatus(_A)
class _FsLaPortChannelDLAGSystemPriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsLaPortChannelDLAGSystemPriority_Type.__name__=_D
_FsLaPortChannelDLAGSystemPriority_Object=MibTableColumn
fsLaPortChannelDLAGSystemPriority=_FsLaPortChannelDLAGSystemPriority_Object((1,3,6,1,4,1,2076,63,2,1,1,14),_FsLaPortChannelDLAGSystemPriority_Type())
fsLaPortChannelDLAGSystemPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortChannelDLAGSystemPriority.setStatus(_A)
class _FsLaPortChannelDLAGPeriodicSyncTime_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,90000))
_FsLaPortChannelDLAGPeriodicSyncTime_Type.__name__=_F
_FsLaPortChannelDLAGPeriodicSyncTime_Object=MibTableColumn
fsLaPortChannelDLAGPeriodicSyncTime=_FsLaPortChannelDLAGPeriodicSyncTime_Object((1,3,6,1,4,1,2076,63,2,1,1,15),_FsLaPortChannelDLAGPeriodicSyncTime_Type())
fsLaPortChannelDLAGPeriodicSyncTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortChannelDLAGPeriodicSyncTime.setStatus(_A)
if mibBuilder.loadTexts:fsLaPortChannelDLAGPeriodicSyncTime.setUnits(_c)
class _FsLaPortChannelDLAGMSSelectionWaitTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,90000))
_FsLaPortChannelDLAGMSSelectionWaitTime_Type.__name__=_F
_FsLaPortChannelDLAGMSSelectionWaitTime_Object=MibTableColumn
fsLaPortChannelDLAGMSSelectionWaitTime=_FsLaPortChannelDLAGMSSelectionWaitTime_Object((1,3,6,1,4,1,2076,63,2,1,1,16),_FsLaPortChannelDLAGMSSelectionWaitTime_Type())
fsLaPortChannelDLAGMSSelectionWaitTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortChannelDLAGMSSelectionWaitTime.setStatus(_A)
if mibBuilder.loadTexts:fsLaPortChannelDLAGMSSelectionWaitTime.setUnits(_c)
class _FsLaPortChannelDLAGRolePlayed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_J,0),(_L,1),(_M,2),(_d,3)))
_FsLaPortChannelDLAGRolePlayed_Type.__name__=_D
_FsLaPortChannelDLAGRolePlayed_Object=MibTableColumn
fsLaPortChannelDLAGRolePlayed=_FsLaPortChannelDLAGRolePlayed_Object((1,3,6,1,4,1,2076,63,2,1,1,17),_FsLaPortChannelDLAGRolePlayed_Type())
fsLaPortChannelDLAGRolePlayed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaPortChannelDLAGRolePlayed.setStatus(_A)
class _FsLaPortChannelDLAGStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsLaPortChannelDLAGStatus_Type.__name__=_D
_FsLaPortChannelDLAGStatus_Object=MibTableColumn
fsLaPortChannelDLAGStatus=_FsLaPortChannelDLAGStatus_Object((1,3,6,1,4,1,2076,63,2,1,1,18),_FsLaPortChannelDLAGStatus_Type())
fsLaPortChannelDLAGStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortChannelDLAGStatus.setStatus(_A)
class _FsLaPortChannelDLAGRedundancy_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_FsLaPortChannelDLAGRedundancy_Type.__name__=_D
_FsLaPortChannelDLAGRedundancy_Object=MibTableColumn
fsLaPortChannelDLAGRedundancy=_FsLaPortChannelDLAGRedundancy_Object((1,3,6,1,4,1,2076,63,2,1,1,19),_FsLaPortChannelDLAGRedundancy_Type())
fsLaPortChannelDLAGRedundancy.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortChannelDLAGRedundancy.setStatus(_A)
class _FsLaPortChannelDLAGMaxKeepAliveCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_FsLaPortChannelDLAGMaxKeepAliveCount_Type.__name__=_D
_FsLaPortChannelDLAGMaxKeepAliveCount_Object=MibTableColumn
fsLaPortChannelDLAGMaxKeepAliveCount=_FsLaPortChannelDLAGMaxKeepAliveCount_Object((1,3,6,1,4,1,2076,63,2,1,1,20),_FsLaPortChannelDLAGMaxKeepAliveCount_Type())
fsLaPortChannelDLAGMaxKeepAliveCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaPortChannelDLAGMaxKeepAliveCount.setStatus(_A)
_FsLaPortChannelDLAGPeriodicSyncPduTxCount_Type=Counter32
_FsLaPortChannelDLAGPeriodicSyncPduTxCount_Object=MibTableColumn
fsLaPortChannelDLAGPeriodicSyncPduTxCount=_FsLaPortChannelDLAGPeriodicSyncPduTxCount_Object((1,3,6,1,4,1,2076,63,2,1,1,21),_FsLaPortChannelDLAGPeriodicSyncPduTxCount_Type())
fsLaPortChannelDLAGPeriodicSyncPduTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaPortChannelDLAGPeriodicSyncPduTxCount.setStatus(_A)
_FsLaPortChannelDLAGPeriodicSyncPduRxCount_Type=Counter32
_FsLaPortChannelDLAGPeriodicSyncPduRxCount_Object=MibTableColumn
fsLaPortChannelDLAGPeriodicSyncPduRxCount=_FsLaPortChannelDLAGPeriodicSyncPduRxCount_Object((1,3,6,1,4,1,2076,63,2,1,1,22),_FsLaPortChannelDLAGPeriodicSyncPduRxCount_Type())
fsLaPortChannelDLAGPeriodicSyncPduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaPortChannelDLAGPeriodicSyncPduRxCount.setStatus(_A)
_FsLaPortChannelDLAGEventUpdatePduTxCount_Type=Counter32
_FsLaPortChannelDLAGEventUpdatePduTxCount_Object=MibTableColumn
fsLaPortChannelDLAGEventUpdatePduTxCount=_FsLaPortChannelDLAGEventUpdatePduTxCount_Object((1,3,6,1,4,1,2076,63,2,1,1,23),_FsLaPortChannelDLAGEventUpdatePduTxCount_Type())
fsLaPortChannelDLAGEventUpdatePduTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaPortChannelDLAGEventUpdatePduTxCount.setStatus(_A)
_FsLaPortChannelDLAGEventUpdatePduRxCount_Type=Counter32
_FsLaPortChannelDLAGEventUpdatePduRxCount_Object=MibTableColumn
fsLaPortChannelDLAGEventUpdatePduRxCount=_FsLaPortChannelDLAGEventUpdatePduRxCount_Object((1,3,6,1,4,1,2076,63,2,1,1,24),_FsLaPortChannelDLAGEventUpdatePduRxCount_Type())
fsLaPortChannelDLAGEventUpdatePduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaPortChannelDLAGEventUpdatePduRxCount.setStatus(_A)
_FsLaPortChannelDLAGElectedAsMasterCount_Type=Counter32
_FsLaPortChannelDLAGElectedAsMasterCount_Object=MibTableColumn
fsLaPortChannelDLAGElectedAsMasterCount=_FsLaPortChannelDLAGElectedAsMasterCount_Object((1,3,6,1,4,1,2076,63,2,1,1,25),_FsLaPortChannelDLAGElectedAsMasterCount_Type())
fsLaPortChannelDLAGElectedAsMasterCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaPortChannelDLAGElectedAsMasterCount.setStatus(_A)
_FsLaPortChannelDLAGElectedAsSlaveCount_Type=Counter32
_FsLaPortChannelDLAGElectedAsSlaveCount_Object=MibTableColumn
fsLaPortChannelDLAGElectedAsSlaveCount=_FsLaPortChannelDLAGElectedAsSlaveCount_Object((1,3,6,1,4,1,2076,63,2,1,1,26),_FsLaPortChannelDLAGElectedAsSlaveCount_Type())
fsLaPortChannelDLAGElectedAsSlaveCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaPortChannelDLAGElectedAsSlaveCount.setStatus(_A)
_FsLaPortChannelTrapTxCount_Type=Counter32
_FsLaPortChannelTrapTxCount_Object=MibTableColumn
fsLaPortChannelTrapTxCount=_FsLaPortChannelTrapTxCount_Object((1,3,6,1,4,1,2076,63,2,1,1,27),_FsLaPortChannelTrapTxCount_Type())
fsLaPortChannelTrapTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaPortChannelTrapTxCount.setStatus(_A)
_FsLaPortChannelDLAGDistributingPortList_Type=PortList
_FsLaPortChannelDLAGDistributingPortList_Object=MibTableColumn
fsLaPortChannelDLAGDistributingPortList=_FsLaPortChannelDLAGDistributingPortList_Object((1,3,6,1,4,1,2076,63,2,1,1,28),_FsLaPortChannelDLAGDistributingPortList_Type())
fsLaPortChannelDLAGDistributingPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortChannelDLAGDistributingPortList.setStatus(_A)
class _FsLaPortChannelMCLAGStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsLaPortChannelMCLAGStatus_Type.__name__=_D
_FsLaPortChannelMCLAGStatus_Object=MibTableColumn
fsLaPortChannelMCLAGStatus=_FsLaPortChannelMCLAGStatus_Object((1,3,6,1,4,1,2076,63,2,1,1,29),_FsLaPortChannelMCLAGStatus_Type())
fsLaPortChannelMCLAGStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortChannelMCLAGStatus.setStatus(_A)
class _FsLaPortChannelMCLAGSystemID_Type(MacAddress):defaultHexValue=_Z
_FsLaPortChannelMCLAGSystemID_Type.__name__=_N
_FsLaPortChannelMCLAGSystemID_Object=MibTableColumn
fsLaPortChannelMCLAGSystemID=_FsLaPortChannelMCLAGSystemID_Object((1,3,6,1,4,1,2076,63,2,1,1,30),_FsLaPortChannelMCLAGSystemID_Type())
fsLaPortChannelMCLAGSystemID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortChannelMCLAGSystemID.setStatus(_A)
class _FsLaPortChannelMCLAGSystemPriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsLaPortChannelMCLAGSystemPriority_Type.__name__=_D
_FsLaPortChannelMCLAGSystemPriority_Object=MibTableColumn
fsLaPortChannelMCLAGSystemPriority=_FsLaPortChannelMCLAGSystemPriority_Object((1,3,6,1,4,1,2076,63,2,1,1,31),_FsLaPortChannelMCLAGSystemPriority_Type())
fsLaPortChannelMCLAGSystemPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortChannelMCLAGSystemPriority.setStatus(_A)
class _FsLaPortChannelMCLAGRolePlayed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_L,1),(_M,2)))
_FsLaPortChannelMCLAGRolePlayed_Type.__name__=_D
_FsLaPortChannelMCLAGRolePlayed_Object=MibTableColumn
fsLaPortChannelMCLAGRolePlayed=_FsLaPortChannelMCLAGRolePlayed_Object((1,3,6,1,4,1,2076,63,2,1,1,32),_FsLaPortChannelMCLAGRolePlayed_Type())
fsLaPortChannelMCLAGRolePlayed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaPortChannelMCLAGRolePlayed.setStatus(_A)
class _FsLaPortChannelMCLAGMaxKeepAliveCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_FsLaPortChannelMCLAGMaxKeepAliveCount_Type.__name__=_D
_FsLaPortChannelMCLAGMaxKeepAliveCount_Object=MibTableColumn
fsLaPortChannelMCLAGMaxKeepAliveCount=_FsLaPortChannelMCLAGMaxKeepAliveCount_Object((1,3,6,1,4,1,2076,63,2,1,1,33),_FsLaPortChannelMCLAGMaxKeepAliveCount_Type())
fsLaPortChannelMCLAGMaxKeepAliveCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaPortChannelMCLAGMaxKeepAliveCount.setStatus(_A)
_FsLaPortChannelMCLAGPeriodicSyncPduTxCount_Type=Counter32
_FsLaPortChannelMCLAGPeriodicSyncPduTxCount_Object=MibTableColumn
fsLaPortChannelMCLAGPeriodicSyncPduTxCount=_FsLaPortChannelMCLAGPeriodicSyncPduTxCount_Object((1,3,6,1,4,1,2076,63,2,1,1,34),_FsLaPortChannelMCLAGPeriodicSyncPduTxCount_Type())
fsLaPortChannelMCLAGPeriodicSyncPduTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaPortChannelMCLAGPeriodicSyncPduTxCount.setStatus(_A)
_FsLaPortChannelMCLAGPeriodicSyncPduRxCount_Type=Counter32
_FsLaPortChannelMCLAGPeriodicSyncPduRxCount_Object=MibTableColumn
fsLaPortChannelMCLAGPeriodicSyncPduRxCount=_FsLaPortChannelMCLAGPeriodicSyncPduRxCount_Object((1,3,6,1,4,1,2076,63,2,1,1,35),_FsLaPortChannelMCLAGPeriodicSyncPduRxCount_Type())
fsLaPortChannelMCLAGPeriodicSyncPduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaPortChannelMCLAGPeriodicSyncPduRxCount.setStatus(_A)
_FsLaPortChannelMCLAGEventUpdatePduTxCount_Type=Counter32
_FsLaPortChannelMCLAGEventUpdatePduTxCount_Object=MibTableColumn
fsLaPortChannelMCLAGEventUpdatePduTxCount=_FsLaPortChannelMCLAGEventUpdatePduTxCount_Object((1,3,6,1,4,1,2076,63,2,1,1,36),_FsLaPortChannelMCLAGEventUpdatePduTxCount_Type())
fsLaPortChannelMCLAGEventUpdatePduTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaPortChannelMCLAGEventUpdatePduTxCount.setStatus(_A)
_FsLaPortChannelMCLAGEventUpdatePduRxCount_Type=Counter32
_FsLaPortChannelMCLAGEventUpdatePduRxCount_Object=MibTableColumn
fsLaPortChannelMCLAGEventUpdatePduRxCount=_FsLaPortChannelMCLAGEventUpdatePduRxCount_Object((1,3,6,1,4,1,2076,63,2,1,1,37),_FsLaPortChannelMCLAGEventUpdatePduRxCount_Type())
fsLaPortChannelMCLAGEventUpdatePduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaPortChannelMCLAGEventUpdatePduRxCount.setStatus(_A)
_FsLaPort_ObjectIdentity=ObjectIdentity
fsLaPort=_FsLaPort_ObjectIdentity((1,3,6,1,4,1,2076,63,3))
_FsLaPortTable_Object=MibTable
fsLaPortTable=_FsLaPortTable_Object((1,3,6,1,4,1,2076,63,3,1))
if mibBuilder.loadTexts:fsLaPortTable.setStatus(_A)
_FsLaPortEntry_Object=MibTableRow
fsLaPortEntry=_FsLaPortEntry_Object((1,3,6,1,4,1,2076,63,3,1,1))
fsLaPortEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:fsLaPortEntry.setStatus(_A)
_FsLaPortIndex_Type=InterfaceIndex
_FsLaPortIndex_Object=MibTableColumn
fsLaPortIndex=_FsLaPortIndex_Object((1,3,6,1,4,1,2076,63,3,1,1,1),_FsLaPortIndex_Type())
fsLaPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fsLaPortIndex.setStatus(_A)
_FsLaPortMode_Type=PortLaMode
_FsLaPortMode_Object=MibTableColumn
fsLaPortMode=_FsLaPortMode_Object((1,3,6,1,4,1,2076,63,3,1,1,2),_FsLaPortMode_Type())
fsLaPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortMode.setStatus(_A)
class _FsLaPortBundleState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_O,0),(_P,1),(_Q,2),(_R,3)))
_FsLaPortBundleState_Type.__name__=_D
_FsLaPortBundleState_Object=MibTableColumn
fsLaPortBundleState=_FsLaPortBundleState_Object((1,3,6,1,4,1,2076,63,3,1,1,3),_FsLaPortBundleState_Type())
fsLaPortBundleState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaPortBundleState.setStatus(_A)
_FsLaPortActorResetAdminState_Type=LacpState
_FsLaPortActorResetAdminState_Object=MibTableColumn
fsLaPortActorResetAdminState=_FsLaPortActorResetAdminState_Object((1,3,6,1,4,1,2076,63,3,1,1,4),_FsLaPortActorResetAdminState_Type())
fsLaPortActorResetAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortActorResetAdminState.setStatus(_A)
class _FsLaPortAggregateWaitTime_Type(TimeTicks):defaultValue=2
_FsLaPortAggregateWaitTime_Type.__name__=_V
_FsLaPortAggregateWaitTime_Object=MibTableColumn
fsLaPortAggregateWaitTime=_FsLaPortAggregateWaitTime_Object((1,3,6,1,4,1,2076,63,3,1,1,5),_FsLaPortAggregateWaitTime_Type())
fsLaPortAggregateWaitTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortAggregateWaitTime.setStatus(_A)
_FsLaPortPartnerResetAdminState_Type=LacpState
_FsLaPortPartnerResetAdminState_Object=MibTableColumn
fsLaPortPartnerResetAdminState=_FsLaPortPartnerResetAdminState_Object((1,3,6,1,4,1,2076,63,3,1,1,6),_FsLaPortPartnerResetAdminState_Type())
fsLaPortPartnerResetAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortPartnerResetAdminState.setStatus(_A)
class _FsLaPortActorAdminPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsLaPortActorAdminPort_Type.__name__=_D
_FsLaPortActorAdminPort_Object=MibTableColumn
fsLaPortActorAdminPort=_FsLaPortActorAdminPort_Object((1,3,6,1,4,1,2076,63,3,1,1,7),_FsLaPortActorAdminPort_Type())
fsLaPortActorAdminPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortActorAdminPort.setStatus(_A)
_FsLaPortRestoreMtu_Type=Integer32
_FsLaPortRestoreMtu_Object=MibTableColumn
fsLaPortRestoreMtu=_FsLaPortRestoreMtu_Object((1,3,6,1,4,1,2076,63,3,1,1,8),_FsLaPortRestoreMtu_Type())
fsLaPortRestoreMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortRestoreMtu.setStatus(_A)
class _FsLaPortSelectAggregator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('static',0),(_b,1)))
_FsLaPortSelectAggregator_Type.__name__=_D
_FsLaPortSelectAggregator_Object=MibTableColumn
fsLaPortSelectAggregator=_FsLaPortSelectAggregator_Object((1,3,6,1,4,1,2076,63,3,1,1,9),_FsLaPortSelectAggregator_Type())
fsLaPortSelectAggregator.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaPortSelectAggregator.setStatus(_A)
_FsLaPortErrStateDetCount_Type=Counter32
_FsLaPortErrStateDetCount_Object=MibTableColumn
fsLaPortErrStateDetCount=_FsLaPortErrStateDetCount_Object((1,3,6,1,4,1,2076,63,3,1,1,10),_FsLaPortErrStateDetCount_Type())
fsLaPortErrStateDetCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaPortErrStateDetCount.setStatus(_A)
_FsLaPortErrStateRecCount_Type=Counter32
_FsLaPortErrStateRecCount_Object=MibTableColumn
fsLaPortErrStateRecCount=_FsLaPortErrStateRecCount_Object((1,3,6,1,4,1,2076,63,3,1,1,11),_FsLaPortErrStateRecCount_Type())
fsLaPortErrStateRecCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaPortErrStateRecCount.setStatus(_A)
class _FsLaPortDefaultedStateThreshold_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_FsLaPortDefaultedStateThreshold_Type.__name__=_F
_FsLaPortDefaultedStateThreshold_Object=MibTableColumn
fsLaPortDefaultedStateThreshold=_FsLaPortDefaultedStateThreshold_Object((1,3,6,1,4,1,2076,63,3,1,1,12),_FsLaPortDefaultedStateThreshold_Type())
fsLaPortDefaultedStateThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortDefaultedStateThreshold.setStatus(_A)
class _FsLaPortHardwareFailureRecThreshold_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_FsLaPortHardwareFailureRecThreshold_Type.__name__=_F
_FsLaPortHardwareFailureRecThreshold_Object=MibTableColumn
fsLaPortHardwareFailureRecThreshold=_FsLaPortHardwareFailureRecThreshold_Object((1,3,6,1,4,1,2076,63,3,1,1,13),_FsLaPortHardwareFailureRecThreshold_Type())
fsLaPortHardwareFailureRecThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortHardwareFailureRecThreshold.setStatus(_A)
class _FsLaPortSameStateRecThreshold_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_FsLaPortSameStateRecThreshold_Type.__name__=_F
_FsLaPortSameStateRecThreshold_Object=MibTableColumn
fsLaPortSameStateRecThreshold=_FsLaPortSameStateRecThreshold_Object((1,3,6,1,4,1,2076,63,3,1,1,14),_FsLaPortSameStateRecThreshold_Type())
fsLaPortSameStateRecThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLaPortSameStateRecThreshold.setStatus(_A)
_FsLaTrapObjects_ObjectIdentity=ObjectIdentity
fsLaTrapObjects=_FsLaTrapObjects_ObjectIdentity((1,3,6,1,4,1,2076,63,4))
_FsLaHwFailTrapObjectsTable_Object=MibTable
fsLaHwFailTrapObjectsTable=_FsLaHwFailTrapObjectsTable_Object((1,3,6,1,4,1,2076,63,4,1))
if mibBuilder.loadTexts:fsLaHwFailTrapObjectsTable.setStatus(_A)
_FsLaHwFailTrapObjectsEntry_Object=MibTableRow
fsLaHwFailTrapObjectsEntry=_FsLaHwFailTrapObjectsEntry_Object((1,3,6,1,4,1,2076,63,4,1,1))
fsLaHwFailTrapObjectsEntry.setIndexNames((0,_E,_f),(0,_E,_g))
if mibBuilder.loadTexts:fsLaHwFailTrapObjectsEntry.setStatus(_A)
_FsLaTrapPortChannelIndex_Type=InterfaceIndex
_FsLaTrapPortChannelIndex_Object=MibTableColumn
fsLaTrapPortChannelIndex=_FsLaTrapPortChannelIndex_Object((1,3,6,1,4,1,2076,63,4,1,1,1),_FsLaTrapPortChannelIndex_Type())
fsLaTrapPortChannelIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fsLaTrapPortChannelIndex.setStatus(_A)
_FsLaTrapPortIndex_Type=InterfaceIndexOrZero
_FsLaTrapPortIndex_Object=MibTableColumn
fsLaTrapPortIndex=_FsLaTrapPortIndex_Object((1,3,6,1,4,1,2076,63,4,1,1,2),_FsLaTrapPortIndex_Type())
fsLaTrapPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fsLaTrapPortIndex.setStatus(_A)
class _FsLaHwFailTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('createAgg',0),('addLinkToAgg',1),('deleteAgg',2),('removeLinkFromAgg',3),('setSelectionPolicy',4),('enableCollection',5),('disableCollection',6),('enableDistribution',7)))
_FsLaHwFailTrapType_Type.__name__=_D
_FsLaHwFailTrapType_Object=MibTableColumn
fsLaHwFailTrapType=_FsLaHwFailTrapType_Object((1,3,6,1,4,1,2076,63,4,1,1,3),_FsLaHwFailTrapType_Type())
fsLaHwFailTrapType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaHwFailTrapType.setStatus(_A)
_FsLaDLAGTrapObjectsTable_Object=MibTable
fsLaDLAGTrapObjectsTable=_FsLaDLAGTrapObjectsTable_Object((1,3,6,1,4,1,2076,63,4,2))
if mibBuilder.loadTexts:fsLaDLAGTrapObjectsTable.setStatus(_A)
_FsLaDLAGTrapObjectsEntry_Object=MibTableRow
fsLaDLAGTrapObjectsEntry=_FsLaDLAGTrapObjectsEntry_Object((1,3,6,1,4,1,2076,63,4,2,1))
fsLaDLAGTrapObjectsEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:fsLaDLAGTrapObjectsEntry.setStatus(_A)
_FsLaDLAGTrapPortChannelIndex_Type=InterfaceIndex
_FsLaDLAGTrapPortChannelIndex_Object=MibTableColumn
fsLaDLAGTrapPortChannelIndex=_FsLaDLAGTrapPortChannelIndex_Object((1,3,6,1,4,1,2076,63,4,2,1,1),_FsLaDLAGTrapPortChannelIndex_Type())
fsLaDLAGTrapPortChannelIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fsLaDLAGTrapPortChannelIndex.setStatus(_A)
class _FsLaDLAGTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('mastertobackupmaster',0),('backupmastertomaster',1),('slavetobackupmaster',2),('backupmastertoslave',3),('mastertoslave',4),('slavetomaster',5)))
_FsLaDLAGTrapType_Type.__name__=_D
_FsLaDLAGTrapType_Object=MibTableColumn
fsLaDLAGTrapType=_FsLaDLAGTrapType_Object((1,3,6,1,4,1,2076,63,4,2,1,2),_FsLaDLAGTrapType_Type())
fsLaDLAGTrapType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaDLAGTrapType.setStatus(_A)
_FsFutureLaTraps_ObjectIdentity=ObjectIdentity
fsFutureLaTraps=_FsFutureLaTraps_ObjectIdentity((1,3,6,1,4,1,2076,63,5))
_FsLaTraps_ObjectIdentity=ObjectIdentity
fsLaTraps=_FsLaTraps_ObjectIdentity((1,3,6,1,4,1,2076,63,5,0))
_FsLaDLAGRemotePortChannel_ObjectIdentity=ObjectIdentity
fsLaDLAGRemotePortChannel=_FsLaDLAGRemotePortChannel_ObjectIdentity((1,3,6,1,4,1,2076,63,6))
_FsLaDLAGRemotePortChannelTable_Object=MibTable
fsLaDLAGRemotePortChannelTable=_FsLaDLAGRemotePortChannelTable_Object((1,3,6,1,4,1,2076,63,6,1))
if mibBuilder.loadTexts:fsLaDLAGRemotePortChannelTable.setStatus(_A)
_FsLaDLAGRemotePortChannelEntry_Object=MibTableRow
fsLaDLAGRemotePortChannelEntry=_FsLaDLAGRemotePortChannelEntry_Object((1,3,6,1,4,1,2076,63,6,1,1))
fsLaDLAGRemotePortChannelEntry.setIndexNames((0,_E,_K),(0,_E,_S))
if mibBuilder.loadTexts:fsLaDLAGRemotePortChannelEntry.setStatus(_A)
_FsLaDLAGRemotePortChannelSystemID_Type=MacAddress
_FsLaDLAGRemotePortChannelSystemID_Object=MibTableColumn
fsLaDLAGRemotePortChannelSystemID=_FsLaDLAGRemotePortChannelSystemID_Object((1,3,6,1,4,1,2076,63,6,1,1,1),_FsLaDLAGRemotePortChannelSystemID_Type())
fsLaDLAGRemotePortChannelSystemID.setMaxAccess(_G)
if mibBuilder.loadTexts:fsLaDLAGRemotePortChannelSystemID.setStatus(_A)
class _FsLaDLAGRemotePortChannelSystemPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsLaDLAGRemotePortChannelSystemPriority_Type.__name__=_D
_FsLaDLAGRemotePortChannelSystemPriority_Object=MibTableColumn
fsLaDLAGRemotePortChannelSystemPriority=_FsLaDLAGRemotePortChannelSystemPriority_Object((1,3,6,1,4,1,2076,63,6,1,1,2),_FsLaDLAGRemotePortChannelSystemPriority_Type())
fsLaDLAGRemotePortChannelSystemPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaDLAGRemotePortChannelSystemPriority.setStatus(_A)
class _FsLaDLAGRemotePortChannelRolePlayed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_J,0),(_L,1),(_M,2),(_d,3)))
_FsLaDLAGRemotePortChannelRolePlayed_Type.__name__=_D
_FsLaDLAGRemotePortChannelRolePlayed_Object=MibTableColumn
fsLaDLAGRemotePortChannelRolePlayed=_FsLaDLAGRemotePortChannelRolePlayed_Object((1,3,6,1,4,1,2076,63,6,1,1,3),_FsLaDLAGRemotePortChannelRolePlayed_Type())
fsLaDLAGRemotePortChannelRolePlayed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaDLAGRemotePortChannelRolePlayed.setStatus(_A)
_FsLaDLAGRemotePortChannelKeepAliveCount_Type=Integer32
_FsLaDLAGRemotePortChannelKeepAliveCount_Object=MibTableColumn
fsLaDLAGRemotePortChannelKeepAliveCount=_FsLaDLAGRemotePortChannelKeepAliveCount_Object((1,3,6,1,4,1,2076,63,6,1,1,4),_FsLaDLAGRemotePortChannelKeepAliveCount_Type())
fsLaDLAGRemotePortChannelKeepAliveCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaDLAGRemotePortChannelKeepAliveCount.setStatus(_A)
_FsLaDLAGRemotePortChannelSpeed_Type=Gauge32
_FsLaDLAGRemotePortChannelSpeed_Object=MibTableColumn
fsLaDLAGRemotePortChannelSpeed=_FsLaDLAGRemotePortChannelSpeed_Object((1,3,6,1,4,1,2076,63,6,1,1,5),_FsLaDLAGRemotePortChannelSpeed_Type())
fsLaDLAGRemotePortChannelSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaDLAGRemotePortChannelSpeed.setStatus(_A)
_FsLaDLAGRemotePortChannelHighSpeed_Type=Gauge32
_FsLaDLAGRemotePortChannelHighSpeed_Object=MibTableColumn
fsLaDLAGRemotePortChannelHighSpeed=_FsLaDLAGRemotePortChannelHighSpeed_Object((1,3,6,1,4,1,2076,63,6,1,1,6),_FsLaDLAGRemotePortChannelHighSpeed_Type())
fsLaDLAGRemotePortChannelHighSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaDLAGRemotePortChannelHighSpeed.setStatus(_A)
_FsLaDLAGRemotePortChannelMtu_Type=Integer32
_FsLaDLAGRemotePortChannelMtu_Object=MibTableColumn
fsLaDLAGRemotePortChannelMtu=_FsLaDLAGRemotePortChannelMtu_Object((1,3,6,1,4,1,2076,63,6,1,1,7),_FsLaDLAGRemotePortChannelMtu_Type())
fsLaDLAGRemotePortChannelMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaDLAGRemotePortChannelMtu.setStatus(_A)
_FsLaDLAGRemotePort_ObjectIdentity=ObjectIdentity
fsLaDLAGRemotePort=_FsLaDLAGRemotePort_ObjectIdentity((1,3,6,1,4,1,2076,63,7))
_FsLaDLAGRemotePortTable_Object=MibTable
fsLaDLAGRemotePortTable=_FsLaDLAGRemotePortTable_Object((1,3,6,1,4,1,2076,63,7,1))
if mibBuilder.loadTexts:fsLaDLAGRemotePortTable.setStatus(_A)
_FsLaDLAGRemotePortEntry_Object=MibTableRow
fsLaDLAGRemotePortEntry=_FsLaDLAGRemotePortEntry_Object((1,3,6,1,4,1,2076,63,7,1,1))
fsLaDLAGRemotePortEntry.setIndexNames((0,_E,_K),(0,_E,_S),(0,_E,_i))
if mibBuilder.loadTexts:fsLaDLAGRemotePortEntry.setStatus(_A)
_FsLaDLAGRemotePortIndex_Type=InterfaceIndex
_FsLaDLAGRemotePortIndex_Object=MibTableColumn
fsLaDLAGRemotePortIndex=_FsLaDLAGRemotePortIndex_Object((1,3,6,1,4,1,2076,63,7,1,1,1),_FsLaDLAGRemotePortIndex_Type())
fsLaDLAGRemotePortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fsLaDLAGRemotePortIndex.setStatus(_A)
class _FsLaDLAGRemotePortBundleState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_O,0),(_P,1),(_Q,2),(_R,3)))
_FsLaDLAGRemotePortBundleState_Type.__name__=_D
_FsLaDLAGRemotePortBundleState_Object=MibTableColumn
fsLaDLAGRemotePortBundleState=_FsLaDLAGRemotePortBundleState_Object((1,3,6,1,4,1,2076,63,7,1,1,2),_FsLaDLAGRemotePortBundleState_Type())
fsLaDLAGRemotePortBundleState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaDLAGRemotePortBundleState.setStatus(_A)
class _FsLaDLAGRemotePortSyncStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_j,1),(_k,2)))
_FsLaDLAGRemotePortSyncStatus_Type.__name__=_D
_FsLaDLAGRemotePortSyncStatus_Object=MibTableColumn
fsLaDLAGRemotePortSyncStatus=_FsLaDLAGRemotePortSyncStatus_Object((1,3,6,1,4,1,2076,63,7,1,1,3),_FsLaDLAGRemotePortSyncStatus_Type())
fsLaDLAGRemotePortSyncStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaDLAGRemotePortSyncStatus.setStatus(_A)
class _FsLaDLAGRemotePortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsLaDLAGRemotePortPriority_Type.__name__=_D
_FsLaDLAGRemotePortPriority_Object=MibTableColumn
fsLaDLAGRemotePortPriority=_FsLaDLAGRemotePortPriority_Object((1,3,6,1,4,1,2076,63,7,1,1,4),_FsLaDLAGRemotePortPriority_Type())
fsLaDLAGRemotePortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaDLAGRemotePortPriority.setStatus(_A)
_FsLaMCLAGRemotePortChannel_ObjectIdentity=ObjectIdentity
fsLaMCLAGRemotePortChannel=_FsLaMCLAGRemotePortChannel_ObjectIdentity((1,3,6,1,4,1,2076,63,8))
_FsLaMCLAGRemotePortChannelTable_Object=MibTable
fsLaMCLAGRemotePortChannelTable=_FsLaMCLAGRemotePortChannelTable_Object((1,3,6,1,4,1,2076,63,8,1))
if mibBuilder.loadTexts:fsLaMCLAGRemotePortChannelTable.setStatus(_A)
_FsLaMCLAGRemotePortChannelEntry_Object=MibTableRow
fsLaMCLAGRemotePortChannelEntry=_FsLaMCLAGRemotePortChannelEntry_Object((1,3,6,1,4,1,2076,63,8,1,1))
fsLaMCLAGRemotePortChannelEntry.setIndexNames((0,_E,_K),(0,_E,_T))
if mibBuilder.loadTexts:fsLaMCLAGRemotePortChannelEntry.setStatus(_A)
_FsLaMCLAGRemotePortChannelSystemID_Type=MacAddress
_FsLaMCLAGRemotePortChannelSystemID_Object=MibTableColumn
fsLaMCLAGRemotePortChannelSystemID=_FsLaMCLAGRemotePortChannelSystemID_Object((1,3,6,1,4,1,2076,63,8,1,1,1),_FsLaMCLAGRemotePortChannelSystemID_Type())
fsLaMCLAGRemotePortChannelSystemID.setMaxAccess(_G)
if mibBuilder.loadTexts:fsLaMCLAGRemotePortChannelSystemID.setStatus(_A)
class _FsLaMCLAGRemotePortChannelSystemPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsLaMCLAGRemotePortChannelSystemPriority_Type.__name__=_D
_FsLaMCLAGRemotePortChannelSystemPriority_Object=MibTableColumn
fsLaMCLAGRemotePortChannelSystemPriority=_FsLaMCLAGRemotePortChannelSystemPriority_Object((1,3,6,1,4,1,2076,63,8,1,1,2),_FsLaMCLAGRemotePortChannelSystemPriority_Type())
fsLaMCLAGRemotePortChannelSystemPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaMCLAGRemotePortChannelSystemPriority.setStatus(_A)
class _FsLaMCLAGRemotePortChannelRolePlayed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_L,1),(_M,2)))
_FsLaMCLAGRemotePortChannelRolePlayed_Type.__name__=_D
_FsLaMCLAGRemotePortChannelRolePlayed_Object=MibTableColumn
fsLaMCLAGRemotePortChannelRolePlayed=_FsLaMCLAGRemotePortChannelRolePlayed_Object((1,3,6,1,4,1,2076,63,8,1,1,3),_FsLaMCLAGRemotePortChannelRolePlayed_Type())
fsLaMCLAGRemotePortChannelRolePlayed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaMCLAGRemotePortChannelRolePlayed.setStatus(_A)
_FsLaMCLAGRemotePortChannelKeepAliveCount_Type=Integer32
_FsLaMCLAGRemotePortChannelKeepAliveCount_Object=MibTableColumn
fsLaMCLAGRemotePortChannelKeepAliveCount=_FsLaMCLAGRemotePortChannelKeepAliveCount_Object((1,3,6,1,4,1,2076,63,8,1,1,4),_FsLaMCLAGRemotePortChannelKeepAliveCount_Type())
fsLaMCLAGRemotePortChannelKeepAliveCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaMCLAGRemotePortChannelKeepAliveCount.setStatus(_A)
_FsLaMCLAGRemotePortChannelSpeed_Type=Gauge32
_FsLaMCLAGRemotePortChannelSpeed_Object=MibTableColumn
fsLaMCLAGRemotePortChannelSpeed=_FsLaMCLAGRemotePortChannelSpeed_Object((1,3,6,1,4,1,2076,63,8,1,1,5),_FsLaMCLAGRemotePortChannelSpeed_Type())
fsLaMCLAGRemotePortChannelSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaMCLAGRemotePortChannelSpeed.setStatus(_A)
_FsLaMCLAGRemotePortChannelHighSpeed_Type=Gauge32
_FsLaMCLAGRemotePortChannelHighSpeed_Object=MibTableColumn
fsLaMCLAGRemotePortChannelHighSpeed=_FsLaMCLAGRemotePortChannelHighSpeed_Object((1,3,6,1,4,1,2076,63,8,1,1,6),_FsLaMCLAGRemotePortChannelHighSpeed_Type())
fsLaMCLAGRemotePortChannelHighSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaMCLAGRemotePortChannelHighSpeed.setStatus(_A)
_FsLaMCLAGRemotePortChannelMtu_Type=Integer32
_FsLaMCLAGRemotePortChannelMtu_Object=MibTableColumn
fsLaMCLAGRemotePortChannelMtu=_FsLaMCLAGRemotePortChannelMtu_Object((1,3,6,1,4,1,2076,63,8,1,1,7),_FsLaMCLAGRemotePortChannelMtu_Type())
fsLaMCLAGRemotePortChannelMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaMCLAGRemotePortChannelMtu.setStatus(_A)
_FsLaMCLAGRemotePort_ObjectIdentity=ObjectIdentity
fsLaMCLAGRemotePort=_FsLaMCLAGRemotePort_ObjectIdentity((1,3,6,1,4,1,2076,63,9))
_FsLaMCLAGRemotePortTable_Object=MibTable
fsLaMCLAGRemotePortTable=_FsLaMCLAGRemotePortTable_Object((1,3,6,1,4,1,2076,63,9,1))
if mibBuilder.loadTexts:fsLaMCLAGRemotePortTable.setStatus(_A)
_FsLaMCLAGRemotePortEntry_Object=MibTableRow
fsLaMCLAGRemotePortEntry=_FsLaMCLAGRemotePortEntry_Object((1,3,6,1,4,1,2076,63,9,1,1))
fsLaMCLAGRemotePortEntry.setIndexNames((0,_E,_K),(0,_E,_T),(0,_E,_l))
if mibBuilder.loadTexts:fsLaMCLAGRemotePortEntry.setStatus(_A)
_FsLaMCLAGRemotePortIndex_Type=InterfaceIndex
_FsLaMCLAGRemotePortIndex_Object=MibTableColumn
fsLaMCLAGRemotePortIndex=_FsLaMCLAGRemotePortIndex_Object((1,3,6,1,4,1,2076,63,9,1,1,1),_FsLaMCLAGRemotePortIndex_Type())
fsLaMCLAGRemotePortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fsLaMCLAGRemotePortIndex.setStatus(_A)
class _FsLaMCLAGRemotePortSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsLaMCLAGRemotePortSlotIndex_Type.__name__=_D
_FsLaMCLAGRemotePortSlotIndex_Object=MibTableColumn
fsLaMCLAGRemotePortSlotIndex=_FsLaMCLAGRemotePortSlotIndex_Object((1,3,6,1,4,1,2076,63,9,1,1,2),_FsLaMCLAGRemotePortSlotIndex_Type())
fsLaMCLAGRemotePortSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaMCLAGRemotePortSlotIndex.setStatus(_A)
class _FsLaMCLAGRemotePortBundleState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_O,0),(_P,1),(_Q,2),(_R,3)))
_FsLaMCLAGRemotePortBundleState_Type.__name__=_D
_FsLaMCLAGRemotePortBundleState_Object=MibTableColumn
fsLaMCLAGRemotePortBundleState=_FsLaMCLAGRemotePortBundleState_Object((1,3,6,1,4,1,2076,63,9,1,1,3),_FsLaMCLAGRemotePortBundleState_Type())
fsLaMCLAGRemotePortBundleState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaMCLAGRemotePortBundleState.setStatus(_A)
class _FsLaMCLAGRemotePortSyncStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_j,1),(_k,2)))
_FsLaMCLAGRemotePortSyncStatus_Type.__name__=_D
_FsLaMCLAGRemotePortSyncStatus_Object=MibTableColumn
fsLaMCLAGRemotePortSyncStatus=_FsLaMCLAGRemotePortSyncStatus_Object((1,3,6,1,4,1,2076,63,9,1,1,4),_FsLaMCLAGRemotePortSyncStatus_Type())
fsLaMCLAGRemotePortSyncStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaMCLAGRemotePortSyncStatus.setStatus(_A)
class _FsLaMCLAGRemotePortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsLaMCLAGRemotePortPriority_Type.__name__=_D
_FsLaMCLAGRemotePortPriority_Object=MibTableColumn
fsLaMCLAGRemotePortPriority=_FsLaMCLAGRemotePortPriority_Object((1,3,6,1,4,1,2076,63,9,1,1,5),_FsLaMCLAGRemotePortPriority_Type())
fsLaMCLAGRemotePortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLaMCLAGRemotePortPriority.setStatus(_A)
fsLaHwFailureTrap=NotificationType((1,3,6,1,4,1,2076,63,5,0,1))
fsLaHwFailureTrap.setObjects((_E,_m))
if mibBuilder.loadTexts:fsLaHwFailureTrap.setStatus(_A)
fsLaDLAGTrap=NotificationType((1,3,6,1,4,1,2076,63,5,0,2))
fsLaDLAGTrap.setObjects((_E,_n))
if mibBuilder.loadTexts:fsLaDLAGTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'PortLaMode':PortLaMode,'LacpKey':LacpKey,'LacpState':LacpState,'fsla':fsla,'fsLaSystem':fsLaSystem,'fsLaSystemControl':fsLaSystemControl,'fsLaStatus':fsLaStatus,'fsLaTraceOption':fsLaTraceOption,'fsLaMaxPortsPerPortChannel':fsLaMaxPortsPerPortChannel,'fsLaMaxPortChannels':fsLaMaxPortChannels,'fsLaOperStatus':fsLaOperStatus,'fsLaActorSystemID':fsLaActorSystemID,'fsLaNoPartnerIndep':fsLaNoPartnerIndep,'fsLaDLAGSystemStatus':fsLaDLAGSystemStatus,'fsLaDLAGSystemID':fsLaDLAGSystemID,'fsLaDLAGSystemPriority':fsLaDLAGSystemPriority,'fsLaDLAGPeriodicSyncTime':fsLaDLAGPeriodicSyncTime,'fsLaDLAGRolePlayed':fsLaDLAGRolePlayed,'fsLaDLAGDistributingPortIndex':fsLaDLAGDistributingPortIndex,'fsLaDLAGDistributingPortList':fsLaDLAGDistributingPortList,'fsLaMCLAGSystemStatus':fsLaMCLAGSystemStatus,'fsLaMCLAGSystemID':fsLaMCLAGSystemID,'fsLaMCLAGSystemPriority':fsLaMCLAGSystemPriority,'fsLaMCLAGPeriodicSyncTime':fsLaMCLAGPeriodicSyncTime,'fsLaRecTmrDuration':fsLaRecTmrDuration,'fsLaRecThreshold':fsLaRecThreshold,'fsLaTotalErrRecCount':fsLaTotalErrRecCount,'fsLaDefaultedStateThreshold':fsLaDefaultedStateThreshold,'fsLaHardwareFailureRecThreshold':fsLaHardwareFailureRecThreshold,'fsLaSameStateRecThreshold':fsLaSameStateRecThreshold,'fsLaRecThresholdExceedAction':fsLaRecThresholdExceedAction,'fsLaMCLAGClearCounters':fsLaMCLAGClearCounters,'fsLaPortChannel':fsLaPortChannel,'fsLaPortChannelTable':fsLaPortChannelTable,'fsLaPortChannelEntry':fsLaPortChannelEntry,_K:fsLaPortChannelIfIndex,'fsLaPortChannelGroup':fsLaPortChannelGroup,'fsLaPortChannelAdminMacAddress':fsLaPortChannelAdminMacAddress,'fsLaPortChannelMacSelection':fsLaPortChannelMacSelection,'fsLaPortChannelMode':fsLaPortChannelMode,'fsLaPortChannelPortCount':fsLaPortChannelPortCount,'fsLaPortChannelActivePortCount':fsLaPortChannelActivePortCount,'fsLaPortChannelSelectionPolicy':fsLaPortChannelSelectionPolicy,'fsLaPortChannelDefaultPortIndex':fsLaPortChannelDefaultPortIndex,'fsLaPortChannelMaxPorts':fsLaPortChannelMaxPorts,'fsLaPortChannelSelectionPolicyBitList':fsLaPortChannelSelectionPolicyBitList,'fsLaPortChannelDLAGDistributingPortIndex':fsLaPortChannelDLAGDistributingPortIndex,'fsLaPortChannelDLAGSystemID':fsLaPortChannelDLAGSystemID,'fsLaPortChannelDLAGSystemPriority':fsLaPortChannelDLAGSystemPriority,'fsLaPortChannelDLAGPeriodicSyncTime':fsLaPortChannelDLAGPeriodicSyncTime,'fsLaPortChannelDLAGMSSelectionWaitTime':fsLaPortChannelDLAGMSSelectionWaitTime,'fsLaPortChannelDLAGRolePlayed':fsLaPortChannelDLAGRolePlayed,'fsLaPortChannelDLAGStatus':fsLaPortChannelDLAGStatus,'fsLaPortChannelDLAGRedundancy':fsLaPortChannelDLAGRedundancy,'fsLaPortChannelDLAGMaxKeepAliveCount':fsLaPortChannelDLAGMaxKeepAliveCount,'fsLaPortChannelDLAGPeriodicSyncPduTxCount':fsLaPortChannelDLAGPeriodicSyncPduTxCount,'fsLaPortChannelDLAGPeriodicSyncPduRxCount':fsLaPortChannelDLAGPeriodicSyncPduRxCount,'fsLaPortChannelDLAGEventUpdatePduTxCount':fsLaPortChannelDLAGEventUpdatePduTxCount,'fsLaPortChannelDLAGEventUpdatePduRxCount':fsLaPortChannelDLAGEventUpdatePduRxCount,'fsLaPortChannelDLAGElectedAsMasterCount':fsLaPortChannelDLAGElectedAsMasterCount,'fsLaPortChannelDLAGElectedAsSlaveCount':fsLaPortChannelDLAGElectedAsSlaveCount,'fsLaPortChannelTrapTxCount':fsLaPortChannelTrapTxCount,'fsLaPortChannelDLAGDistributingPortList':fsLaPortChannelDLAGDistributingPortList,'fsLaPortChannelMCLAGStatus':fsLaPortChannelMCLAGStatus,'fsLaPortChannelMCLAGSystemID':fsLaPortChannelMCLAGSystemID,'fsLaPortChannelMCLAGSystemPriority':fsLaPortChannelMCLAGSystemPriority,'fsLaPortChannelMCLAGRolePlayed':fsLaPortChannelMCLAGRolePlayed,'fsLaPortChannelMCLAGMaxKeepAliveCount':fsLaPortChannelMCLAGMaxKeepAliveCount,'fsLaPortChannelMCLAGPeriodicSyncPduTxCount':fsLaPortChannelMCLAGPeriodicSyncPduTxCount,'fsLaPortChannelMCLAGPeriodicSyncPduRxCount':fsLaPortChannelMCLAGPeriodicSyncPduRxCount,'fsLaPortChannelMCLAGEventUpdatePduTxCount':fsLaPortChannelMCLAGEventUpdatePduTxCount,'fsLaPortChannelMCLAGEventUpdatePduRxCount':fsLaPortChannelMCLAGEventUpdatePduRxCount,'fsLaPort':fsLaPort,'fsLaPortTable':fsLaPortTable,'fsLaPortEntry':fsLaPortEntry,_e:fsLaPortIndex,'fsLaPortMode':fsLaPortMode,'fsLaPortBundleState':fsLaPortBundleState,'fsLaPortActorResetAdminState':fsLaPortActorResetAdminState,'fsLaPortAggregateWaitTime':fsLaPortAggregateWaitTime,'fsLaPortPartnerResetAdminState':fsLaPortPartnerResetAdminState,'fsLaPortActorAdminPort':fsLaPortActorAdminPort,'fsLaPortRestoreMtu':fsLaPortRestoreMtu,'fsLaPortSelectAggregator':fsLaPortSelectAggregator,'fsLaPortErrStateDetCount':fsLaPortErrStateDetCount,'fsLaPortErrStateRecCount':fsLaPortErrStateRecCount,'fsLaPortDefaultedStateThreshold':fsLaPortDefaultedStateThreshold,'fsLaPortHardwareFailureRecThreshold':fsLaPortHardwareFailureRecThreshold,'fsLaPortSameStateRecThreshold':fsLaPortSameStateRecThreshold,'fsLaTrapObjects':fsLaTrapObjects,'fsLaHwFailTrapObjectsTable':fsLaHwFailTrapObjectsTable,'fsLaHwFailTrapObjectsEntry':fsLaHwFailTrapObjectsEntry,_f:fsLaTrapPortChannelIndex,_g:fsLaTrapPortIndex,_m:fsLaHwFailTrapType,'fsLaDLAGTrapObjectsTable':fsLaDLAGTrapObjectsTable,'fsLaDLAGTrapObjectsEntry':fsLaDLAGTrapObjectsEntry,_h:fsLaDLAGTrapPortChannelIndex,_n:fsLaDLAGTrapType,'fsFutureLaTraps':fsFutureLaTraps,'fsLaTraps':fsLaTraps,'fsLaHwFailureTrap':fsLaHwFailureTrap,'fsLaDLAGTrap':fsLaDLAGTrap,'fsLaDLAGRemotePortChannel':fsLaDLAGRemotePortChannel,'fsLaDLAGRemotePortChannelTable':fsLaDLAGRemotePortChannelTable,'fsLaDLAGRemotePortChannelEntry':fsLaDLAGRemotePortChannelEntry,_S:fsLaDLAGRemotePortChannelSystemID,'fsLaDLAGRemotePortChannelSystemPriority':fsLaDLAGRemotePortChannelSystemPriority,'fsLaDLAGRemotePortChannelRolePlayed':fsLaDLAGRemotePortChannelRolePlayed,'fsLaDLAGRemotePortChannelKeepAliveCount':fsLaDLAGRemotePortChannelKeepAliveCount,'fsLaDLAGRemotePortChannelSpeed':fsLaDLAGRemotePortChannelSpeed,'fsLaDLAGRemotePortChannelHighSpeed':fsLaDLAGRemotePortChannelHighSpeed,'fsLaDLAGRemotePortChannelMtu':fsLaDLAGRemotePortChannelMtu,'fsLaDLAGRemotePort':fsLaDLAGRemotePort,'fsLaDLAGRemotePortTable':fsLaDLAGRemotePortTable,'fsLaDLAGRemotePortEntry':fsLaDLAGRemotePortEntry,_i:fsLaDLAGRemotePortIndex,'fsLaDLAGRemotePortBundleState':fsLaDLAGRemotePortBundleState,'fsLaDLAGRemotePortSyncStatus':fsLaDLAGRemotePortSyncStatus,'fsLaDLAGRemotePortPriority':fsLaDLAGRemotePortPriority,'fsLaMCLAGRemotePortChannel':fsLaMCLAGRemotePortChannel,'fsLaMCLAGRemotePortChannelTable':fsLaMCLAGRemotePortChannelTable,'fsLaMCLAGRemotePortChannelEntry':fsLaMCLAGRemotePortChannelEntry,_T:fsLaMCLAGRemotePortChannelSystemID,'fsLaMCLAGRemotePortChannelSystemPriority':fsLaMCLAGRemotePortChannelSystemPriority,'fsLaMCLAGRemotePortChannelRolePlayed':fsLaMCLAGRemotePortChannelRolePlayed,'fsLaMCLAGRemotePortChannelKeepAliveCount':fsLaMCLAGRemotePortChannelKeepAliveCount,'fsLaMCLAGRemotePortChannelSpeed':fsLaMCLAGRemotePortChannelSpeed,'fsLaMCLAGRemotePortChannelHighSpeed':fsLaMCLAGRemotePortChannelHighSpeed,'fsLaMCLAGRemotePortChannelMtu':fsLaMCLAGRemotePortChannelMtu,'fsLaMCLAGRemotePort':fsLaMCLAGRemotePort,'fsLaMCLAGRemotePortTable':fsLaMCLAGRemotePortTable,'fsLaMCLAGRemotePortEntry':fsLaMCLAGRemotePortEntry,_l:fsLaMCLAGRemotePortIndex,'fsLaMCLAGRemotePortSlotIndex':fsLaMCLAGRemotePortSlotIndex,'fsLaMCLAGRemotePortBundleState':fsLaMCLAGRemotePortBundleState,'fsLaMCLAGRemotePortSyncStatus':fsLaMCLAGRemotePortSyncStatus,'fsLaMCLAGRemotePortPriority':fsLaMCLAGRemotePortPriority})