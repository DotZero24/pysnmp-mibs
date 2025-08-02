_AD='scPortHistorySampleIndex'
_AC='scPortHistoryIndex'
_AB='lsPortHistorySampleIndex'
_AA='lsPortHistoryIndex'
_A9='alarmMonitorStatusIndex'
_A8='ethTopBus'
_A7='ethTopLSAId'
_A6='ethTopMACFindBus'
_A5='ethTopMessageResultId'
_A4='vnsPacketMACAddress'
_A3='lseWANPortId'
_A2='lseWANGroupId'
_A1='lstIntPortId'
_A0='lstIntPortGroupId'
_z='lsHistorySampleIndex'
_y='lsHistoryIndex'
_x='hostTimeCreationOrder'
_w='hostTimeIndex'
_v='lsMatrixFilterAddress'
_u='lsHostPortFilter'
_t='lsHostFilterAddress'
_s='lsPortExtendedStatsNumber'
_r='lsPortFilter'
_q='lsPortControlIndex'
_p='lsBusStatsVirtualNet'
_o='lsBusStatsPriorityIndex'
_n='lhsPortId'
_m='lhsPortGroupId'
_l='lhsGroupId'
_k='lsePortId'
_j='lsePortGroupId'
_i='lseIntPortMACVlanLAId'
_h='lseIntPortMACVlanVlan'
_g='lseIntPortMACVlanGroupId'
_f='lseIntPortFilterLAId'
_e='lseIntPortFilterPortId'
_d='lseIntPortFilterGroupId'
_c='lseIntPortMACAddLAId'
_b='lseIntPortMACAddGroupId'
_a='obsolete'
_Z='ignore'
_Y='lseIntPortId'
_X='lseIntPortGroupId'
_W='lseGroupId'
_V='historyControlIndex'
_U='RMON-MIB'
_T='ifIndex'
_S='IF-MIB'
_R='lsPortNumber'
_Q='lseIntPortMACAddPortId'
_P='disable'
_O='enable'
_N='ok'
_M='invalid'
_L='valid'
_K='clear'
_J='idle'
_I='OctetString'
_H='off'
_G='on'
_F='APPLIC-MIB'
_E='notSupported'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lannet,=mibBuilder.importSymbols('GEN-MIB','lannet')
ifIndex,=mibBuilder.importSymbols(_S,_T)
historyControlIndex,=mibBuilder.importSymbols(_U,_V)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_LntLanSwitch_ObjectIdentity=ObjectIdentity
lntLanSwitch=_LntLanSwitch_ObjectIdentity((1,3,6,1,4,1,81,19))
_Lse_ObjectIdentity=ObjectIdentity
lse=_Lse_ObjectIdentity((1,3,6,1,4,1,81,19,1))
_LseGroupTable_Object=MibTable
lseGroupTable=_LseGroupTable_Object((1,3,6,1,4,1,81,19,1,1))
if mibBuilder.loadTexts:lseGroupTable.setStatus(_A)
_LseGroupEntry_Object=MibTableRow
lseGroupEntry=_LseGroupEntry_Object((1,3,6,1,4,1,81,19,1,1,1))
lseGroupEntry.setIndexNames((0,_F,_W))
if mibBuilder.loadTexts:lseGroupEntry.setStatus(_A)
_LseGroupId_Type=Integer32
_LseGroupId_Object=MibTableColumn
lseGroupId=_LseGroupId_Object((1,3,6,1,4,1,81,19,1,1,1,1),_LseGroupId_Type())
lseGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:lseGroupId.setStatus(_A)
class _LseGroupFastOpen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseGroupFastOpen_Type.__name__=_C
_LseGroupFastOpen_Object=MibTableColumn
lseGroupFastOpen=_LseGroupFastOpen_Object((1,3,6,1,4,1,81,19,1,1,1,2),_LseGroupFastOpen_Type())
lseGroupFastOpen.setMaxAccess(_D)
if mibBuilder.loadTexts:lseGroupFastOpen.setStatus(_A)
class _LseGroup10MSqlt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseGroup10MSqlt_Type.__name__=_C
_LseGroup10MSqlt_Object=MibTableColumn
lseGroup10MSqlt=_LseGroup10MSqlt_Object((1,3,6,1,4,1,81,19,1,1,1,3),_LseGroup10MSqlt_Type())
lseGroup10MSqlt.setMaxAccess(_D)
if mibBuilder.loadTexts:lseGroup10MSqlt.setStatus(_A)
class _LseGroupSmartSqlt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseGroupSmartSqlt_Type.__name__=_C
_LseGroupSmartSqlt_Object=MibTableColumn
lseGroupSmartSqlt=_LseGroupSmartSqlt_Object((1,3,6,1,4,1,81,19,1,1,1,4),_LseGroupSmartSqlt_Type())
lseGroupSmartSqlt.setMaxAccess(_D)
if mibBuilder.loadTexts:lseGroupSmartSqlt.setStatus('deprecated')
class _LseGroupCParameter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_LseGroupCParameter_Type.__name__=_C
_LseGroupCParameter_Object=MibTableColumn
lseGroupCParameter=_LseGroupCParameter_Object((1,3,6,1,4,1,81,19,1,1,1,5),_LseGroupCParameter_Type())
lseGroupCParameter.setMaxAccess(_D)
if mibBuilder.loadTexts:lseGroupCParameter.setStatus(_A)
class _LseGroupIPGJamLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,124))
_LseGroupIPGJamLength_Type.__name__=_C
_LseGroupIPGJamLength_Object=MibTableColumn
lseGroupIPGJamLength=_LseGroupIPGJamLength_Object((1,3,6,1,4,1,81,19,1,1,1,6),_LseGroupIPGJamLength_Type())
lseGroupIPGJamLength.setMaxAccess(_D)
if mibBuilder.loadTexts:lseGroupIPGJamLength.setStatus(_A)
class _LseGroupJamLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,120))
_LseGroupJamLength_Type.__name__=_C
_LseGroupJamLength_Object=MibTableColumn
lseGroupJamLength=_LseGroupJamLength_Object((1,3,6,1,4,1,81,19,1,1,1,7),_LseGroupJamLength_Type())
lseGroupJamLength.setMaxAccess(_D)
if mibBuilder.loadTexts:lseGroupJamLength.setStatus(_A)
class _LseGroupDataBlinderLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,124))
_LseGroupDataBlinderLength_Type.__name__=_C
_LseGroupDataBlinderLength_Object=MibTableColumn
lseGroupDataBlinderLength=_LseGroupDataBlinderLength_Object((1,3,6,1,4,1,81,19,1,1,1,8),_LseGroupDataBlinderLength_Type())
lseGroupDataBlinderLength.setMaxAccess(_D)
if mibBuilder.loadTexts:lseGroupDataBlinderLength.setStatus(_A)
class _LseGroupIPGDataLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,124))
_LseGroupIPGDataLength_Type.__name__=_C
_LseGroupIPGDataLength_Object=MibTableColumn
lseGroupIPGDataLength=_LseGroupIPGDataLength_Object((1,3,6,1,4,1,81,19,1,1,1,9),_LseGroupIPGDataLength_Type())
lseGroupIPGDataLength.setMaxAccess(_D)
if mibBuilder.loadTexts:lseGroupIPGDataLength.setStatus(_A)
class _LseGroupActiveMonitor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseGroupActiveMonitor_Type.__name__=_C
_LseGroupActiveMonitor_Object=MibTableColumn
lseGroupActiveMonitor=_LseGroupActiveMonitor_Object((1,3,6,1,4,1,81,19,1,1,1,10),_LseGroupActiveMonitor_Type())
lseGroupActiveMonitor.setMaxAccess(_B)
if mibBuilder.loadTexts:lseGroupActiveMonitor.setStatus(_A)
class _LseGroupBackbone12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseGroupBackbone12_Type.__name__=_C
_LseGroupBackbone12_Object=MibTableColumn
lseGroupBackbone12=_LseGroupBackbone12_Object((1,3,6,1,4,1,81,19,1,1,1,11),_LseGroupBackbone12_Type())
lseGroupBackbone12.setMaxAccess(_D)
if mibBuilder.loadTexts:lseGroupBackbone12.setStatus(_A)
class _LseGroupSetDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseGroupSetDefaults_Type.__name__=_C
_LseGroupSetDefaults_Object=MibTableColumn
lseGroupSetDefaults=_LseGroupSetDefaults_Object((1,3,6,1,4,1,81,19,1,1,1,12),_LseGroupSetDefaults_Type())
lseGroupSetDefaults.setMaxAccess(_D)
if mibBuilder.loadTexts:lseGroupSetDefaults.setStatus(_A)
class _LseGroupBackbone34_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseGroupBackbone34_Type.__name__=_C
_LseGroupBackbone34_Object=MibTableColumn
lseGroupBackbone34=_LseGroupBackbone34_Object((1,3,6,1,4,1,81,19,1,1,1,13),_LseGroupBackbone34_Type())
lseGroupBackbone34.setMaxAccess(_D)
if mibBuilder.loadTexts:lseGroupBackbone34.setStatus(_A)
class _LseGroupBackboneRedun12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseGroupBackboneRedun12_Type.__name__=_C
_LseGroupBackboneRedun12_Object=MibTableColumn
lseGroupBackboneRedun12=_LseGroupBackboneRedun12_Object((1,3,6,1,4,1,81,19,1,1,1,14),_LseGroupBackboneRedun12_Type())
lseGroupBackboneRedun12.setMaxAccess(_D)
if mibBuilder.loadTexts:lseGroupBackboneRedun12.setStatus(_A)
class _LseGroupBackoffFromJam_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseGroupBackoffFromJam_Type.__name__=_C
_LseGroupBackoffFromJam_Object=MibTableColumn
lseGroupBackoffFromJam=_LseGroupBackoffFromJam_Object((1,3,6,1,4,1,81,19,1,1,1,15),_LseGroupBackoffFromJam_Type())
lseGroupBackoffFromJam.setMaxAccess(_D)
if mibBuilder.loadTexts:lseGroupBackoffFromJam.setStatus(_A)
class _LseGroupCAMClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseGroupCAMClear_Type.__name__=_C
_LseGroupCAMClear_Object=MibTableColumn
lseGroupCAMClear=_LseGroupCAMClear_Object((1,3,6,1,4,1,81,19,1,1,1,16),_LseGroupCAMClear_Type())
lseGroupCAMClear.setMaxAccess(_D)
if mibBuilder.loadTexts:lseGroupCAMClear.setStatus(_A)
class _LseGroupJamPrevent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseGroupJamPrevent_Type.__name__=_C
_LseGroupJamPrevent_Object=MibTableColumn
lseGroupJamPrevent=_LseGroupJamPrevent_Object((1,3,6,1,4,1,81,19,1,1,1,17),_LseGroupJamPrevent_Type())
lseGroupJamPrevent.setMaxAccess(_D)
if mibBuilder.loadTexts:lseGroupJamPrevent.setStatus(_A)
class _LseGroupNormOpCl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('open',1),('closed',2),(_E,255)))
_LseGroupNormOpCl_Type.__name__=_C
_LseGroupNormOpCl_Object=MibTableColumn
lseGroupNormOpCl=_LseGroupNormOpCl_Object((1,3,6,1,4,1,81,19,1,1,1,18),_LseGroupNormOpCl_Type())
lseGroupNormOpCl.setMaxAccess(_D)
if mibBuilder.loadTexts:lseGroupNormOpCl.setStatus(_A)
class _LseGroupNormOpDelay_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600000))
_LseGroupNormOpDelay_Type.__name__=_C
_LseGroupNormOpDelay_Object=MibTableColumn
lseGroupNormOpDelay=_LseGroupNormOpDelay_Object((1,3,6,1,4,1,81,19,1,1,1,19),_LseGroupNormOpDelay_Type())
lseGroupNormOpDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:lseGroupNormOpDelay.setStatus(_A)
class _LseGroupAutoPartitionEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_O,1),(_P,2),(_E,255)))
_LseGroupAutoPartitionEnable_Type.__name__=_C
_LseGroupAutoPartitionEnable_Object=MibTableColumn
lseGroupAutoPartitionEnable=_LseGroupAutoPartitionEnable_Object((1,3,6,1,4,1,81,19,1,1,1,20),_LseGroupAutoPartitionEnable_Type())
lseGroupAutoPartitionEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:lseGroupAutoPartitionEnable.setStatus(_A)
class _LseGroupWorkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*(('run',1),('boot',2),('runAndBoot',3),('none',4),(_E,255)))
_LseGroupWorkState_Type.__name__=_C
_LseGroupWorkState_Object=MibTableColumn
lseGroupWorkState=_LseGroupWorkState_Object((1,3,6,1,4,1,81,19,1,1,1,21),_LseGroupWorkState_Type())
lseGroupWorkState.setMaxAccess(_B)
if mibBuilder.loadTexts:lseGroupWorkState.setStatus(_A)
class _LseGroupBITResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_N,1),('faulty',2),(_E,255)))
_LseGroupBITResult_Type.__name__=_C
_LseGroupBITResult_Object=MibTableColumn
lseGroupBITResult=_LseGroupBITResult_Object((1,3,6,1,4,1,81,19,1,1,1,22),_LseGroupBITResult_Type())
lseGroupBITResult.setMaxAccess(_B)
if mibBuilder.loadTexts:lseGroupBITResult.setStatus(_A)
class _LseGroupAssignSlots_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_LseGroupAssignSlots_Type.__name__=_I
_LseGroupAssignSlots_Object=MibTableColumn
lseGroupAssignSlots=_LseGroupAssignSlots_Object((1,3,6,1,4,1,81,19,1,1,1,23),_LseGroupAssignSlots_Type())
lseGroupAssignSlots.setMaxAccess(_D)
if mibBuilder.loadTexts:lseGroupAssignSlots.setStatus(_A)
_LseGroupHSBMonStatus_Type=Integer32
_LseGroupHSBMonStatus_Object=MibTableColumn
lseGroupHSBMonStatus=_LseGroupHSBMonStatus_Object((1,3,6,1,4,1,81,19,1,1,1,24),_LseGroupHSBMonStatus_Type())
lseGroupHSBMonStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lseGroupHSBMonStatus.setStatus(_A)
class _LseGroupEnableHSBReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_O,1),(_P,2),(_E,255)))
_LseGroupEnableHSBReset_Type.__name__=_C
_LseGroupEnableHSBReset_Object=MibTableColumn
lseGroupEnableHSBReset=_LseGroupEnableHSBReset_Object((1,3,6,1,4,1,81,19,1,1,1,25),_LseGroupEnableHSBReset_Type())
lseGroupEnableHSBReset.setMaxAccess(_D)
if mibBuilder.loadTexts:lseGroupEnableHSBReset.setStatus(_A)
_LseIntPort_ObjectIdentity=ObjectIdentity
lseIntPort=_LseIntPort_ObjectIdentity((1,3,6,1,4,1,81,19,1,2))
_LseIntPortTable_Object=MibTable
lseIntPortTable=_LseIntPortTable_Object((1,3,6,1,4,1,81,19,1,2,1))
if mibBuilder.loadTexts:lseIntPortTable.setStatus(_A)
_LseIntPortEntry_Object=MibTableRow
lseIntPortEntry=_LseIntPortEntry_Object((1,3,6,1,4,1,81,19,1,2,1,1))
lseIntPortEntry.setIndexNames((0,_F,_X),(0,_F,_Y))
if mibBuilder.loadTexts:lseIntPortEntry.setStatus(_A)
class _LseIntPortGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_LseIntPortGroupId_Type.__name__=_C
_LseIntPortGroupId_Object=MibTableColumn
lseIntPortGroupId=_LseIntPortGroupId_Object((1,3,6,1,4,1,81,19,1,2,1,1,1),_LseIntPortGroupId_Type())
lseIntPortGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:lseIntPortGroupId.setStatus(_A)
class _LseIntPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_LseIntPortId_Type.__name__=_C
_LseIntPortId_Object=MibTableColumn
lseIntPortId=_LseIntPortId_Object((1,3,6,1,4,1,81,19,1,2,1,1,2),_LseIntPortId_Type())
lseIntPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:lseIntPortId.setStatus(_A)
class _LseIntPortIOMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseIntPortIOMode_Type.__name__=_C
_LseIntPortIOMode_Object=MibTableColumn
lseIntPortIOMode=_LseIntPortIOMode_Object((1,3,6,1,4,1,81,19,1,2,1,1,3),_LseIntPortIOMode_Type())
lseIntPortIOMode.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortIOMode.setStatus(_A)
class _LseIntPortResetSwitchCAM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseIntPortResetSwitchCAM_Type.__name__=_C
_LseIntPortResetSwitchCAM_Object=MibTableColumn
lseIntPortResetSwitchCAM=_LseIntPortResetSwitchCAM_Object((1,3,6,1,4,1,81,19,1,2,1,1,4),_LseIntPortResetSwitchCAM_Type())
lseIntPortResetSwitchCAM.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortResetSwitchCAM.setStatus(_A)
class _LseIntPortVideoPacket_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseIntPortVideoPacket_Type.__name__=_C
_LseIntPortVideoPacket_Object=MibTableColumn
lseIntPortVideoPacket=_LseIntPortVideoPacket_Object((1,3,6,1,4,1,81,19,1,2,1,1,5),_LseIntPortVideoPacket_Type())
lseIntPortVideoPacket.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortVideoPacket.setStatus(_A)
class _LseIntPortPriorityStateMachine_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseIntPortPriorityStateMachine_Type.__name__=_C
_LseIntPortPriorityStateMachine_Object=MibTableColumn
lseIntPortPriorityStateMachine=_LseIntPortPriorityStateMachine_Object((1,3,6,1,4,1,81,19,1,2,1,1,6),_LseIntPortPriorityStateMachine_Type())
lseIntPortPriorityStateMachine.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortPriorityStateMachine.setStatus(_A)
class _LseIntPortActiveBroadcastPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseIntPortActiveBroadcastPriority_Type.__name__=_C
_LseIntPortActiveBroadcastPriority_Object=MibTableColumn
lseIntPortActiveBroadcastPriority=_LseIntPortActiveBroadcastPriority_Object((1,3,6,1,4,1,81,19,1,2,1,1,7),_LseIntPortActiveBroadcastPriority_Type())
lseIntPortActiveBroadcastPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortActiveBroadcastPriority.setStatus(_A)
class _LseIntPortPriorityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,255)));namedValues=NamedValues(*(('broadcast',1),('multicast',2),('video',3),('regular',4),('default',5),('mngrTerminal',6),(_E,255)))
_LseIntPortPriorityLevel_Type.__name__=_C
_LseIntPortPriorityLevel_Object=MibTableColumn
lseIntPortPriorityLevel=_LseIntPortPriorityLevel_Object((1,3,6,1,4,1,81,19,1,2,1,1,8),_LseIntPortPriorityLevel_Type())
lseIntPortPriorityLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortPriorityLevel.setStatus(_A)
class _LseIntPortSuperPriorityEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseIntPortSuperPriorityEnable_Type.__name__=_C
_LseIntPortSuperPriorityEnable_Object=MibTableColumn
lseIntPortSuperPriorityEnable=_LseIntPortSuperPriorityEnable_Object((1,3,6,1,4,1,81,19,1,2,1,1,9),_LseIntPortSuperPriorityEnable_Type())
lseIntPortSuperPriorityEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortSuperPriorityEnable.setStatus(_A)
class _LseIntPortRoutingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*(('generic',1),('net',2),('dst-port',3),('allPackets',4),(_E,255)))
_LseIntPortRoutingMode_Type.__name__=_C
_LseIntPortRoutingMode_Object=MibTableColumn
lseIntPortRoutingMode=_LseIntPortRoutingMode_Object((1,3,6,1,4,1,81,19,1,2,1,1,10),_LseIntPortRoutingMode_Type())
lseIntPortRoutingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortRoutingMode.setStatus(_A)
class _LseIntPortGlobal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseIntPortGlobal_Type.__name__=_C
_LseIntPortGlobal_Object=MibTableColumn
lseIntPortGlobal=_LseIntPortGlobal_Object((1,3,6,1,4,1,81,19,1,2,1,1,11),_LseIntPortGlobal_Type())
lseIntPortGlobal.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortGlobal.setStatus(_A)
class _LseIntPortLearnIOCAM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseIntPortLearnIOCAM_Type.__name__=_C
_LseIntPortLearnIOCAM_Object=MibTableColumn
lseIntPortLearnIOCAM=_LseIntPortLearnIOCAM_Object((1,3,6,1,4,1,81,19,1,2,1,1,12),_LseIntPortLearnIOCAM_Type())
lseIntPortLearnIOCAM.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortLearnIOCAM.setStatus(_A)
class _LseIntPortSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseIntPortSecurity_Type.__name__=_C
_LseIntPortSecurity_Object=MibTableColumn
lseIntPortSecurity=_LseIntPortSecurity_Object((1,3,6,1,4,1,81,19,1,2,1,1,13),_LseIntPortSecurity_Type())
lseIntPortSecurity.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortSecurity.setStatus(_A)
class _LseIntPortIgnoreBusy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseIntPortIgnoreBusy_Type.__name__=_C
_LseIntPortIgnoreBusy_Object=MibTableColumn
lseIntPortIgnoreBusy=_LseIntPortIgnoreBusy_Object((1,3,6,1,4,1,81,19,1,2,1,1,14),_LseIntPortIgnoreBusy_Type())
lseIntPortIgnoreBusy.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortIgnoreBusy.setStatus(_A)
class _LseIntPortRetryPriorityLevel1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_LseIntPortRetryPriorityLevel1_Type.__name__=_C
_LseIntPortRetryPriorityLevel1_Object=MibTableColumn
lseIntPortRetryPriorityLevel1=_LseIntPortRetryPriorityLevel1_Object((1,3,6,1,4,1,81,19,1,2,1,1,15),_LseIntPortRetryPriorityLevel1_Type())
lseIntPortRetryPriorityLevel1.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortRetryPriorityLevel1.setStatus(_A)
class _LseIntPortRetryPriorityLevel2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_LseIntPortRetryPriorityLevel2_Type.__name__=_C
_LseIntPortRetryPriorityLevel2_Object=MibTableColumn
lseIntPortRetryPriorityLevel2=_LseIntPortRetryPriorityLevel2_Object((1,3,6,1,4,1,81,19,1,2,1,1,16),_LseIntPortRetryPriorityLevel2_Type())
lseIntPortRetryPriorityLevel2.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortRetryPriorityLevel2.setStatus(_A)
class _LseIntPortRetryPriorityLevel3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_LseIntPortRetryPriorityLevel3_Type.__name__=_C
_LseIntPortRetryPriorityLevel3_Object=MibTableColumn
lseIntPortRetryPriorityLevel3=_LseIntPortRetryPriorityLevel3_Object((1,3,6,1,4,1,81,19,1,2,1,1,17),_LseIntPortRetryPriorityLevel3_Type())
lseIntPortRetryPriorityLevel3.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortRetryPriorityLevel3.setStatus(_A)
class _LseIntPortIgnoreProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_Z,1),('not-ignore',2),(_E,255)))
_LseIntPortIgnoreProtocolType_Type.__name__=_C
_LseIntPortIgnoreProtocolType_Object=MibTableColumn
lseIntPortIgnoreProtocolType=_LseIntPortIgnoreProtocolType_Object((1,3,6,1,4,1,81,19,1,2,1,1,18),_LseIntPortIgnoreProtocolType_Type())
lseIntPortIgnoreProtocolType.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortIgnoreProtocolType.setStatus(_A)
_LseIntPortCompanyMAC_Type=OctetString
_LseIntPortCompanyMAC_Object=MibTableColumn
lseIntPortCompanyMAC=_LseIntPortCompanyMAC_Object((1,3,6,1,4,1,81,19,1,2,1,1,19),_LseIntPortCompanyMAC_Type())
lseIntPortCompanyMAC.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortCompanyMAC.setStatus(_A)
class _LseIntPortTxSafetyZone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,510))
_LseIntPortTxSafetyZone_Type.__name__=_C
_LseIntPortTxSafetyZone_Object=MibTableColumn
lseIntPortTxSafetyZone=_LseIntPortTxSafetyZone_Object((1,3,6,1,4,1,81,19,1,2,1,1,20),_LseIntPortTxSafetyZone_Type())
lseIntPortTxSafetyZone.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortTxSafetyZone.setStatus(_A)
class _LseIntPortRxSafetyZone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,510))
_LseIntPortRxSafetyZone_Type.__name__=_C
_LseIntPortRxSafetyZone_Object=MibTableColumn
lseIntPortRxSafetyZone=_LseIntPortRxSafetyZone_Object((1,3,6,1,4,1,81,19,1,2,1,1,21),_LseIntPortRxSafetyZone_Type())
lseIntPortRxSafetyZone.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortRxSafetyZone.setStatus(_A)
class _LseIntPortTxBurstLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,510))
_LseIntPortTxBurstLength_Type.__name__=_C
_LseIntPortTxBurstLength_Object=MibTableColumn
lseIntPortTxBurstLength=_LseIntPortTxBurstLength_Object((1,3,6,1,4,1,81,19,1,2,1,1,22),_LseIntPortTxBurstLength_Type())
lseIntPortTxBurstLength.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortTxBurstLength.setStatus(_A)
class _LseIntPortSecurityIntruder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseIntPortSecurityIntruder_Type.__name__=_C
_LseIntPortSecurityIntruder_Object=MibTableColumn
lseIntPortSecurityIntruder=_LseIntPortSecurityIntruder_Object((1,3,6,1,4,1,81,19,1,2,1,1,23),_LseIntPortSecurityIntruder_Type())
lseIntPortSecurityIntruder.setMaxAccess(_B)
if mibBuilder.loadTexts:lseIntPortSecurityIntruder.setStatus(_A)
class _LseIntPortJabber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseIntPortJabber_Type.__name__=_C
_LseIntPortJabber_Object=MibTableColumn
lseIntPortJabber=_LseIntPortJabber_Object((1,3,6,1,4,1,81,19,1,2,1,1,24),_LseIntPortJabber_Type())
lseIntPortJabber.setMaxAccess(_B)
if mibBuilder.loadTexts:lseIntPortJabber.setStatus(_A)
class _LseIntPortCAM_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,112))
_LseIntPortCAM_Type.__name__=_I
_LseIntPortCAM_Object=MibTableColumn
lseIntPortCAM=_LseIntPortCAM_Object((1,3,6,1,4,1,81,19,1,2,1,1,25),_LseIntPortCAM_Type())
lseIntPortCAM.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortCAM.setStatus(_A)
class _LseIntPortVideoStateMachine_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseIntPortVideoStateMachine_Type.__name__=_C
_LseIntPortVideoStateMachine_Object=MibTableColumn
lseIntPortVideoStateMachine=_LseIntPortVideoStateMachine_Object((1,3,6,1,4,1,81,19,1,2,1,1,26),_LseIntPortVideoStateMachine_Type())
lseIntPortVideoStateMachine.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortVideoStateMachine.setStatus(_A)
class _LseIntPortTransmitWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_LseIntPortTransmitWeight_Type.__name__=_C
_LseIntPortTransmitWeight_Object=MibTableColumn
lseIntPortTransmitWeight=_LseIntPortTransmitWeight_Object((1,3,6,1,4,1,81,19,1,2,1,1,27),_LseIntPortTransmitWeight_Type())
lseIntPortTransmitWeight.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortTransmitWeight.setStatus(_A)
class _LseIntPortSuperPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseIntPortSuperPriority_Type.__name__=_C
_LseIntPortSuperPriority_Object=MibTableColumn
lseIntPortSuperPriority=_LseIntPortSuperPriority_Object((1,3,6,1,4,1,81,19,1,2,1,1,28),_LseIntPortSuperPriority_Type())
lseIntPortSuperPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortSuperPriority.setStatus(_A)
_LseIntPortAlignment_Type=Counter32
_LseIntPortAlignment_Object=MibTableColumn
lseIntPortAlignment=_LseIntPortAlignment_Object((1,3,6,1,4,1,81,19,1,2,1,1,29),_LseIntPortAlignment_Type())
lseIntPortAlignment.setMaxAccess(_B)
if mibBuilder.loadTexts:lseIntPortAlignment.setStatus(_A)
_LseIntPortRxReject_Type=Counter32
_LseIntPortRxReject_Object=MibTableColumn
lseIntPortRxReject=_LseIntPortRxReject_Object((1,3,6,1,4,1,81,19,1,2,1,1,30),_LseIntPortRxReject_Type())
lseIntPortRxReject.setMaxAccess(_B)
if mibBuilder.loadTexts:lseIntPortRxReject.setStatus(_a)
_LseIntPortTxReject_Type=Counter32
_LseIntPortTxReject_Object=MibTableColumn
lseIntPortTxReject=_LseIntPortTxReject_Object((1,3,6,1,4,1,81,19,1,2,1,1,31),_LseIntPortTxReject_Type())
lseIntPortTxReject.setMaxAccess(_B)
if mibBuilder.loadTexts:lseIntPortTxReject.setStatus(_a)
_LseIntPortRxEmpty0_Type=Integer32
_LseIntPortRxEmpty0_Object=MibTableColumn
lseIntPortRxEmpty0=_LseIntPortRxEmpty0_Object((1,3,6,1,4,1,81,19,1,2,1,1,32),_LseIntPortRxEmpty0_Type())
lseIntPortRxEmpty0.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortRxEmpty0.setStatus(_A)
_LseIntPortRxEmpty1_Type=Integer32
_LseIntPortRxEmpty1_Object=MibTableColumn
lseIntPortRxEmpty1=_LseIntPortRxEmpty1_Object((1,3,6,1,4,1,81,19,1,2,1,1,33),_LseIntPortRxEmpty1_Type())
lseIntPortRxEmpty1.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortRxEmpty1.setStatus(_A)
_LseIntPortRxEmpty2_Type=Integer32
_LseIntPortRxEmpty2_Object=MibTableColumn
lseIntPortRxEmpty2=_LseIntPortRxEmpty2_Object((1,3,6,1,4,1,81,19,1,2,1,1,34),_LseIntPortRxEmpty2_Type())
lseIntPortRxEmpty2.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortRxEmpty2.setStatus(_A)
class _LseIntPortSuperNetNumber_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14))
_LseIntPortSuperNetNumber_Type.__name__=_C
_LseIntPortSuperNetNumber_Object=MibTableColumn
lseIntPortSuperNetNumber=_LseIntPortSuperNetNumber_Object((1,3,6,1,4,1,81,19,1,2,1,1,35),_LseIntPortSuperNetNumber_Type())
lseIntPortSuperNetNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortSuperNetNumber.setStatus(_A)
class _LseIntPortGlobalSuperNet_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LseIntPortGlobalSuperNet_Type.__name__=_C
_LseIntPortGlobalSuperNet_Object=MibTableColumn
lseIntPortGlobalSuperNet=_LseIntPortGlobalSuperNet_Object((1,3,6,1,4,1,81,19,1,2,1,1,36),_LseIntPortGlobalSuperNet_Type())
lseIntPortGlobalSuperNet.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortGlobalSuperNet.setStatus(_A)
_LseIntPortMACAddress_Type=OctetString
_LseIntPortMACAddress_Object=MibTableColumn
lseIntPortMACAddress=_LseIntPortMACAddress_Object((1,3,6,1,4,1,81,19,1,2,1,1,37),_LseIntPortMACAddress_Type())
lseIntPortMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:lseIntPortMACAddress.setStatus(_A)
class _LseIntPortIgnoreRoutingMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_Z,1),('notIgnore',2),(_E,255)))
_LseIntPortIgnoreRoutingMode_Type.__name__=_C
_LseIntPortIgnoreRoutingMode_Object=MibTableColumn
lseIntPortIgnoreRoutingMode=_LseIntPortIgnoreRoutingMode_Object((1,3,6,1,4,1,81,19,1,2,1,1,38),_LseIntPortIgnoreRoutingMode_Type())
lseIntPortIgnoreRoutingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortIgnoreRoutingMode.setStatus(_A)
_LseIntPortCAMLastChange_Type=TimeTicks
_LseIntPortCAMLastChange_Object=MibTableColumn
lseIntPortCAMLastChange=_LseIntPortCAMLastChange_Object((1,3,6,1,4,1,81,19,1,2,1,1,39),_LseIntPortCAMLastChange_Type())
lseIntPortCAMLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:lseIntPortCAMLastChange.setStatus(_A)
_LseIntPortCopiedPort_Type=Integer32
_LseIntPortCopiedPort_Object=MibTableColumn
lseIntPortCopiedPort=_LseIntPortCopiedPort_Object((1,3,6,1,4,1,81,19,1,2,1,1,40),_LseIntPortCopiedPort_Type())
lseIntPortCopiedPort.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortCopiedPort.setStatus(_A)
class _LseIntPortBroadcastBehavior_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('normal',1),('selective',2),('receiveAll',3),(_E,255)))
_LseIntPortBroadcastBehavior_Type.__name__=_C
_LseIntPortBroadcastBehavior_Object=MibTableColumn
lseIntPortBroadcastBehavior=_LseIntPortBroadcastBehavior_Object((1,3,6,1,4,1,81,19,1,2,1,1,41),_LseIntPortBroadcastBehavior_Type())
lseIntPortBroadcastBehavior.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortBroadcastBehavior.setStatus(_A)
class _LseIntPortFilteringMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*(('source',1),('destination',2),('sourceOrDestination',3),('group',4),(_E,255)))
_LseIntPortFilteringMethod_Type.__name__=_C
_LseIntPortFilteringMethod_Object=MibTableColumn
lseIntPortFilteringMethod=_LseIntPortFilteringMethod_Object((1,3,6,1,4,1,81,19,1,2,1,1,42),_LseIntPortFilteringMethod_Type())
lseIntPortFilteringMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortFilteringMethod.setStatus(_A)
class _LseIntPortSetFilter_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,452))
_LseIntPortSetFilter_Type.__name__=_I
_LseIntPortSetFilter_Object=MibTableColumn
lseIntPortSetFilter=_LseIntPortSetFilter_Object((1,3,6,1,4,1,81,19,1,2,1,1,43),_LseIntPortSetFilter_Type())
lseIntPortSetFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortSetFilter.setStatus(_A)
class _LseIntPortRemoveFilter_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,452))
_LseIntPortRemoveFilter_Type.__name__=_I
_LseIntPortRemoveFilter_Object=MibTableColumn
lseIntPortRemoveFilter=_LseIntPortRemoveFilter_Object((1,3,6,1,4,1,81,19,1,2,1,1,44),_LseIntPortRemoveFilter_Type())
lseIntPortRemoveFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortRemoveFilter.setStatus(_A)
class _LseIntPortClearFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_J,1),(_K,2),(_E,255)))
_LseIntPortClearFilter_Type.__name__=_C
_LseIntPortClearFilter_Object=MibTableColumn
lseIntPortClearFilter=_LseIntPortClearFilter_Object((1,3,6,1,4,1,81,19,1,2,1,1,45),_LseIntPortClearFilter_Type())
lseIntPortClearFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:lseIntPortClearFilter.setStatus(_A)
_LseIntPortMonitorMissedEvents_Type=Counter32
_LseIntPortMonitorMissedEvents_Object=MibTableColumn
lseIntPortMonitorMissedEvents=_LseIntPortMonitorMissedEvents_Object((1,3,6,1,4,1,81,19,1,2,1,1,46),_LseIntPortMonitorMissedEvents_Type())
lseIntPortMonitorMissedEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:lseIntPortMonitorMissedEvents.setStatus(_A)
_LseIntPortMACAdd_ObjectIdentity=ObjectIdentity
lseIntPortMACAdd=_LseIntPortMACAdd_ObjectIdentity((1,3,6,1,4,1,81,19,1,2,2))
_LseIntPortMACAddTable_Object=MibTable
lseIntPortMACAddTable=_LseIntPortMACAddTable_Object((1,3,6,1,4,1,81,19,1,2,2,1))
if mibBuilder.loadTexts:lseIntPortMACAddTable.setStatus(_A)
_LseIntPortMACAddEntry_Object=MibTableRow
lseIntPortMACAddEntry=_LseIntPortMACAddEntry_Object((1,3,6,1,4,1,81,19,1,2,2,1,1))
lseIntPortMACAddEntry.setIndexNames((0,_F,_b),(0,_F,_Q),(0,_F,_c))
if mibBuilder.loadTexts:lseIntPortMACAddEntry.setStatus(_A)
class _LseIntPortMACAddGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_LseIntPortMACAddGroupId_Type.__name__=_C
_LseIntPortMACAddGroupId_Object=MibTableColumn
lseIntPortMACAddGroupId=_LseIntPortMACAddGroupId_Object((1,3,6,1,4,1,81,19,1,2,2,1,1,1),_LseIntPortMACAddGroupId_Type())
lseIntPortMACAddGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:lseIntPortMACAddGroupId.setStatus(_A)
class _LseIntPortMACAddPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_LseIntPortMACAddPortId_Type.__name__=_C
_LseIntPortMACAddPortId_Object=MibTableColumn
lseIntPortMACAddPortId=_LseIntPortMACAddPortId_Object((1,3,6,1,4,1,81,19,1,2,2,1,1,2),_LseIntPortMACAddPortId_Type())
lseIntPortMACAddPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:lseIntPortMACAddPortId.setStatus(_A)
_LseIntPortMACAddLAId_Type=Integer32
_LseIntPortMACAddLAId_Object=MibTableColumn
lseIntPortMACAddLAId=_LseIntPortMACAddLAId_Object((1,3,6,1,4,1,81,19,1,2,2,1,1,3),_LseIntPortMACAddLAId_Type())
lseIntPortMACAddLAId.setMaxAccess(_B)
if mibBuilder.loadTexts:lseIntPortMACAddLAId.setStatus(_A)
class _LseIntPortMACAddList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,452))
_LseIntPortMACAddList_Type.__name__=_I
_LseIntPortMACAddList_Object=MibTableColumn
lseIntPortMACAddList=_LseIntPortMACAddList_Object((1,3,6,1,4,1,81,19,1,2,2,1,1,4),_LseIntPortMACAddList_Type())
lseIntPortMACAddList.setMaxAccess(_B)
if mibBuilder.loadTexts:lseIntPortMACAddList.setStatus(_A)
_LseIntPortFilter_ObjectIdentity=ObjectIdentity
lseIntPortFilter=_LseIntPortFilter_ObjectIdentity((1,3,6,1,4,1,81,19,1,2,3))
_LseIntPortFilterTable_Object=MibTable
lseIntPortFilterTable=_LseIntPortFilterTable_Object((1,3,6,1,4,1,81,19,1,2,3,1))
if mibBuilder.loadTexts:lseIntPortFilterTable.setStatus(_A)
_LseIntPortFilterEntry_Object=MibTableRow
lseIntPortFilterEntry=_LseIntPortFilterEntry_Object((1,3,6,1,4,1,81,19,1,2,3,1,1))
lseIntPortFilterEntry.setIndexNames((0,_F,_d),(0,_F,_e),(0,_F,_f))
if mibBuilder.loadTexts:lseIntPortFilterEntry.setStatus(_A)
class _LseIntPortFilterGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_LseIntPortFilterGroupId_Type.__name__=_C
_LseIntPortFilterGroupId_Object=MibTableColumn
lseIntPortFilterGroupId=_LseIntPortFilterGroupId_Object((1,3,6,1,4,1,81,19,1,2,3,1,1,1),_LseIntPortFilterGroupId_Type())
lseIntPortFilterGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:lseIntPortFilterGroupId.setStatus(_A)
class _LseIntPortFilterPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_LseIntPortFilterPortId_Type.__name__=_C
_LseIntPortFilterPortId_Object=MibTableColumn
lseIntPortFilterPortId=_LseIntPortFilterPortId_Object((1,3,6,1,4,1,81,19,1,2,3,1,1,2),_LseIntPortFilterPortId_Type())
lseIntPortFilterPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:lseIntPortFilterPortId.setStatus(_A)
_LseIntPortFilterLAId_Type=Integer32
_LseIntPortFilterLAId_Object=MibTableColumn
lseIntPortFilterLAId=_LseIntPortFilterLAId_Object((1,3,6,1,4,1,81,19,1,2,3,1,1,3),_LseIntPortFilterLAId_Type())
lseIntPortFilterLAId.setMaxAccess(_B)
if mibBuilder.loadTexts:lseIntPortFilterLAId.setStatus(_A)
class _LseIntPortFilterList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,452))
_LseIntPortFilterList_Type.__name__=_I
_LseIntPortFilterList_Object=MibTableColumn
lseIntPortFilterList=_LseIntPortFilterList_Object((1,3,6,1,4,1,81,19,1,2,3,1,1,4),_LseIntPortFilterList_Type())
lseIntPortFilterList.setMaxAccess(_B)
if mibBuilder.loadTexts:lseIntPortFilterList.setStatus(_A)
_LseIntPortMACVlanTable_Object=MibTable
lseIntPortMACVlanTable=_LseIntPortMACVlanTable_Object((1,3,6,1,4,1,81,19,1,2,4))
if mibBuilder.loadTexts:lseIntPortMACVlanTable.setStatus(_A)
_LseIntPortMACVlanEntry_Object=MibTableRow
lseIntPortMACVlanEntry=_LseIntPortMACVlanEntry_Object((1,3,6,1,4,1,81,19,1,2,4,1))
lseIntPortMACVlanEntry.setIndexNames((0,_F,_g),(0,_F,_Q),(0,_F,_h),(0,_F,_i))
if mibBuilder.loadTexts:lseIntPortMACVlanEntry.setStatus(_A)
class _LseIntPortMACVlanGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_LseIntPortMACVlanGroupId_Type.__name__=_C
_LseIntPortMACVlanGroupId_Object=MibTableColumn
lseIntPortMACVlanGroupId=_LseIntPortMACVlanGroupId_Object((1,3,6,1,4,1,81,19,1,2,4,1,1),_LseIntPortMACVlanGroupId_Type())
lseIntPortMACVlanGroupId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:lseIntPortMACVlanGroupId.setStatus(_A)
class _LseIntPortMACVlanPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_LseIntPortMACVlanPortId_Type.__name__=_C
_LseIntPortMACVlanPortId_Object=MibTableColumn
lseIntPortMACVlanPortId=_LseIntPortMACVlanPortId_Object((1,3,6,1,4,1,81,19,1,2,4,1,2),_LseIntPortMACVlanPortId_Type())
lseIntPortMACVlanPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:lseIntPortMACVlanPortId.setStatus(_A)
class _LseIntPortMACVlanVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_LseIntPortMACVlanVlan_Type.__name__=_C
_LseIntPortMACVlanVlan_Object=MibTableColumn
lseIntPortMACVlanVlan=_LseIntPortMACVlanVlan_Object((1,3,6,1,4,1,81,19,1,2,4,1,3),_LseIntPortMACVlanVlan_Type())
lseIntPortMACVlanVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:lseIntPortMACVlanVlan.setStatus(_A)
class _LseIntPortMACVlanLAId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_LseIntPortMACVlanLAId_Type.__name__=_C
_LseIntPortMACVlanLAId_Object=MibTableColumn
lseIntPortMACVlanLAId=_LseIntPortMACVlanLAId_Object((1,3,6,1,4,1,81,19,1,2,4,1,4),_LseIntPortMACVlanLAId_Type())
lseIntPortMACVlanLAId.setMaxAccess(_B)
if mibBuilder.loadTexts:lseIntPortMACVlanLAId.setStatus(_A)
class _LseIntPortMACVlanMAClist_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,452))
_LseIntPortMACVlanMAClist_Type.__name__=_I
_LseIntPortMACVlanMAClist_Object=MibTableColumn
lseIntPortMACVlanMAClist=_LseIntPortMACVlanMAClist_Object((1,3,6,1,4,1,81,19,1,2,4,1,5),_LseIntPortMACVlanMAClist_Type())
lseIntPortMACVlanMAClist.setMaxAccess(_B)
if mibBuilder.loadTexts:lseIntPortMACVlanMAClist.setStatus(_A)
_LsePort_ObjectIdentity=ObjectIdentity
lsePort=_LsePort_ObjectIdentity((1,3,6,1,4,1,81,19,1,3))
_LsePortTable_Object=MibTable
lsePortTable=_LsePortTable_Object((1,3,6,1,4,1,81,19,1,3,1))
if mibBuilder.loadTexts:lsePortTable.setStatus(_A)
_LsePortEntry_Object=MibTableRow
lsePortEntry=_LsePortEntry_Object((1,3,6,1,4,1,81,19,1,3,1,1))
lsePortEntry.setIndexNames((0,_F,_j),(0,_F,_k))
if mibBuilder.loadTexts:lsePortEntry.setStatus(_A)
class _LsePortGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_LsePortGroupId_Type.__name__=_C
_LsePortGroupId_Object=MibTableColumn
lsePortGroupId=_LsePortGroupId_Object((1,3,6,1,4,1,81,19,1,3,1,1,1),_LsePortGroupId_Type())
lsePortGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:lsePortGroupId.setStatus(_A)
class _LsePortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_LsePortId_Type.__name__=_C
_LsePortId_Object=MibTableColumn
lsePortId=_LsePortId_Object((1,3,6,1,4,1,81,19,1,3,1,1,2),_LsePortId_Type())
lsePortId.setMaxAccess(_B)
if mibBuilder.loadTexts:lsePortId.setStatus(_A)
class _LsePortPolarity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LsePortPolarity_Type.__name__=_C
_LsePortPolarity_Object=MibTableColumn
lsePortPolarity=_LsePortPolarity_Object((1,3,6,1,4,1,81,19,1,3,1,1,3),_LsePortPolarity_Type())
lsePortPolarity.setMaxAccess(_D)
if mibBuilder.loadTexts:lsePortPolarity.setStatus(_A)
class _LsePortBackboneStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_N,1),('fault',2),(_E,255)))
_LsePortBackboneStatus_Type.__name__=_C
_LsePortBackboneStatus_Object=MibTableColumn
lsePortBackboneStatus=_LsePortBackboneStatus_Object((1,3,6,1,4,1,81,19,1,3,1,1,4),_LsePortBackboneStatus_Type())
lsePortBackboneStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lsePortBackboneStatus.setStatus(_A)
_Lhs_ObjectIdentity=ObjectIdentity
lhs=_Lhs_ObjectIdentity((1,3,6,1,4,1,81,19,2))
_LhsGroupTable_Object=MibTable
lhsGroupTable=_LhsGroupTable_Object((1,3,6,1,4,1,81,19,2,1))
if mibBuilder.loadTexts:lhsGroupTable.setStatus(_A)
_LhsGroupEntry_Object=MibTableRow
lhsGroupEntry=_LhsGroupEntry_Object((1,3,6,1,4,1,81,19,2,1,1))
lhsGroupEntry.setIndexNames((0,_F,_l))
if mibBuilder.loadTexts:lhsGroupEntry.setStatus(_A)
_LhsGroupId_Type=Integer32
_LhsGroupId_Object=MibTableColumn
lhsGroupId=_LhsGroupId_Object((1,3,6,1,4,1,81,19,2,1,1,1),_LhsGroupId_Type())
lhsGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:lhsGroupId.setStatus(_A)
_LhsGroupMainSWVersion_Type=DisplayString
_LhsGroupMainSWVersion_Object=MibTableColumn
lhsGroupMainSWVersion=_LhsGroupMainSWVersion_Object((1,3,6,1,4,1,81,19,2,1,1,2),_LhsGroupMainSWVersion_Type())
lhsGroupMainSWVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:lhsGroupMainSWVersion.setStatus(_A)
class _LhsGroupProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*(('other',1),('ethernet',2),('tokenring',3),('ethernet-tokenring',4),(_E,255)))
_LhsGroupProtocolType_Type.__name__=_C
_LhsGroupProtocolType_Object=MibTableColumn
lhsGroupProtocolType=_LhsGroupProtocolType_Object((1,3,6,1,4,1,81,19,2,1,1,3),_LhsGroupProtocolType_Type())
lhsGroupProtocolType.setMaxAccess(_D)
if mibBuilder.loadTexts:lhsGroupProtocolType.setStatus(_A)
_LhsPortTable_Object=MibTable
lhsPortTable=_LhsPortTable_Object((1,3,6,1,4,1,81,19,2,2))
if mibBuilder.loadTexts:lhsPortTable.setStatus(_A)
_LhsPortEntry_Object=MibTableRow
lhsPortEntry=_LhsPortEntry_Object((1,3,6,1,4,1,81,19,2,2,1))
lhsPortEntry.setIndexNames((0,_F,_m),(0,_F,_n))
if mibBuilder.loadTexts:lhsPortEntry.setStatus(_A)
_LhsPortGroupId_Type=Integer32
_LhsPortGroupId_Object=MibTableColumn
lhsPortGroupId=_LhsPortGroupId_Object((1,3,6,1,4,1,81,19,2,2,1,1),_LhsPortGroupId_Type())
lhsPortGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:lhsPortGroupId.setStatus(_A)
_LhsPortId_Type=Integer32
_LhsPortId_Object=MibTableColumn
lhsPortId=_LhsPortId_Object((1,3,6,1,4,1,81,19,2,2,1,2),_LhsPortId_Type())
lhsPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:lhsPortId.setStatus(_A)
_LhsTxUCast_Type=Counter32
_LhsTxUCast_Object=MibTableColumn
lhsTxUCast=_LhsTxUCast_Object((1,3,6,1,4,1,81,19,2,2,1,3),_LhsTxUCast_Type())
lhsTxUCast.setMaxAccess(_B)
if mibBuilder.loadTexts:lhsTxUCast.setStatus(_A)
_LhsTxBCast_Type=Counter32
_LhsTxBCast_Object=MibTableColumn
lhsTxBCast=_LhsTxBCast_Object((1,3,6,1,4,1,81,19,2,2,1,4),_LhsTxBCast_Type())
lhsTxBCast.setMaxAccess(_B)
if mibBuilder.loadTexts:lhsTxBCast.setStatus(_A)
_LhsTxMCast_Type=Counter32
_LhsTxMCast_Object=MibTableColumn
lhsTxMCast=_LhsTxMCast_Object((1,3,6,1,4,1,81,19,2,2,1,5),_LhsTxMCast_Type())
lhsTxMCast.setMaxAccess(_B)
if mibBuilder.loadTexts:lhsTxMCast.setStatus(_A)
_LhsTxUrunErr_Type=Counter32
_LhsTxUrunErr_Object=MibTableColumn
lhsTxUrunErr=_LhsTxUrunErr_Object((1,3,6,1,4,1,81,19,2,2,1,6),_LhsTxUrunErr_Type())
lhsTxUrunErr.setMaxAccess(_B)
if mibBuilder.loadTexts:lhsTxUrunErr.setStatus(_A)
_LhsTxParErr_Type=Counter32
_LhsTxParErr_Object=MibTableColumn
lhsTxParErr=_LhsTxParErr_Object((1,3,6,1,4,1,81,19,2,2,1,7),_LhsTxParErr_Type())
lhsTxParErr.setMaxAccess(_B)
if mibBuilder.loadTexts:lhsTxParErr.setStatus(_A)
_LhsRxUCast_Type=Counter32
_LhsRxUCast_Object=MibTableColumn
lhsRxUCast=_LhsRxUCast_Object((1,3,6,1,4,1,81,19,2,2,1,8),_LhsRxUCast_Type())
lhsRxUCast.setMaxAccess(_B)
if mibBuilder.loadTexts:lhsRxUCast.setStatus(_A)
_LhsRxBCast_Type=Counter32
_LhsRxBCast_Object=MibTableColumn
lhsRxBCast=_LhsRxBCast_Object((1,3,6,1,4,1,81,19,2,2,1,9),_LhsRxBCast_Type())
lhsRxBCast.setMaxAccess(_B)
if mibBuilder.loadTexts:lhsRxBCast.setStatus(_A)
_LhsRxMCast_Type=Counter32
_LhsRxMCast_Object=MibTableColumn
lhsRxMCast=_LhsRxMCast_Object((1,3,6,1,4,1,81,19,2,2,1,10),_LhsRxMCast_Type())
lhsRxMCast.setMaxAccess(_B)
if mibBuilder.loadTexts:lhsRxMCast.setStatus(_A)
_LhsRxOrunErr_Type=Counter32
_LhsRxOrunErr_Object=MibTableColumn
lhsRxOrunErr=_LhsRxOrunErr_Object((1,3,6,1,4,1,81,19,2,2,1,11),_LhsRxOrunErr_Type())
lhsRxOrunErr.setMaxAccess(_B)
if mibBuilder.loadTexts:lhsRxOrunErr.setStatus(_A)
_LhsRxParErr_Type=Counter32
_LhsRxParErr_Object=MibTableColumn
lhsRxParErr=_LhsRxParErr_Object((1,3,6,1,4,1,81,19,2,2,1,12),_LhsRxParErr_Type())
lhsRxParErr.setMaxAccess(_B)
if mibBuilder.loadTexts:lhsRxParErr.setStatus(_A)
_LhsRxRscErr_Type=Counter32
_LhsRxRscErr_Object=MibTableColumn
lhsRxRscErr=_LhsRxRscErr_Object((1,3,6,1,4,1,81,19,2,2,1,13),_LhsRxRscErr_Type())
lhsRxRscErr.setMaxAccess(_B)
if mibBuilder.loadTexts:lhsRxRscErr.setStatus(_A)
_LhsRxBadTypeErr_Type=Counter32
_LhsRxBadTypeErr_Object=MibTableColumn
lhsRxBadTypeErr=_LhsRxBadTypeErr_Object((1,3,6,1,4,1,81,19,2,2,1,14),_LhsRxBadTypeErr_Type())
lhsRxBadTypeErr.setMaxAccess(_B)
if mibBuilder.loadTexts:lhsRxBadTypeErr.setStatus(_A)
class _LhsLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_N,1),('linkFailure',2),(_E,255)))
_LhsLinkStatus_Type.__name__=_C
_LhsLinkStatus_Object=MibTableColumn
lhsLinkStatus=_LhsLinkStatus_Object((1,3,6,1,4,1,81,19,2,2,1,15),_LhsLinkStatus_Type())
lhsLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lhsLinkStatus.setStatus(_A)
_LsMonitor_ObjectIdentity=ObjectIdentity
lsMonitor=_LsMonitor_ObjectIdentity((1,3,6,1,4,1,81,19,3))
class _LsMonitorResourceAllocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('hostStats',2),('portExtendedStats',3),('hostMatrix',4)))
_LsMonitorResourceAllocation_Type.__name__=_C
_LsMonitorResourceAllocation_Object=MibScalar
lsMonitorResourceAllocation=_LsMonitorResourceAllocation_Object((1,3,6,1,4,1,81,19,3,1),_LsMonitorResourceAllocation_Type())
lsMonitorResourceAllocation.setMaxAccess(_B)
if mibBuilder.loadTexts:lsMonitorResourceAllocation.setStatus(_A)
_LsBusStats_ObjectIdentity=ObjectIdentity
lsBusStats=_LsBusStats_ObjectIdentity((1,3,6,1,4,1,81,19,3,2))
_LsBusStatsDropEvents_Type=Counter32
_LsBusStatsDropEvents_Object=MibScalar
lsBusStatsDropEvents=_LsBusStatsDropEvents_Object((1,3,6,1,4,1,81,19,3,2,1),_LsBusStatsDropEvents_Type())
lsBusStatsDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:lsBusStatsDropEvents.setStatus(_A)
_LsBusStatsPkts_Type=Counter32
_LsBusStatsPkts_Object=MibScalar
lsBusStatsPkts=_LsBusStatsPkts_Object((1,3,6,1,4,1,81,19,3,2,2),_LsBusStatsPkts_Type())
lsBusStatsPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lsBusStatsPkts.setStatus(_A)
_LsBusStatsOctets_Type=Counter32
_LsBusStatsOctets_Object=MibScalar
lsBusStatsOctets=_LsBusStatsOctets_Object((1,3,6,1,4,1,81,19,3,2,3),_LsBusStatsOctets_Type())
lsBusStatsOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:lsBusStatsOctets.setStatus(_A)
_LsBusStatsUtilization_Type=Integer32
_LsBusStatsUtilization_Object=MibScalar
lsBusStatsUtilization=_LsBusStatsUtilization_Object((1,3,6,1,4,1,81,19,3,2,4),_LsBusStatsUtilization_Type())
lsBusStatsUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:lsBusStatsUtilization.setStatus(_A)
_LsBusStatsEthBroadcastPkts_Type=Counter32
_LsBusStatsEthBroadcastPkts_Object=MibScalar
lsBusStatsEthBroadcastPkts=_LsBusStatsEthBroadcastPkts_Object((1,3,6,1,4,1,81,19,3,2,5),_LsBusStatsEthBroadcastPkts_Type())
lsBusStatsEthBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lsBusStatsEthBroadcastPkts.setStatus(_A)
_LsBusStatsMulticastPkts_Type=Counter32
_LsBusStatsMulticastPkts_Object=MibScalar
lsBusStatsMulticastPkts=_LsBusStatsMulticastPkts_Object((1,3,6,1,4,1,81,19,3,2,6),_LsBusStatsMulticastPkts_Type())
lsBusStatsMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lsBusStatsMulticastPkts.setStatus(_A)
_LsBusStatsGoodEthPkts_Type=Counter32
_LsBusStatsGoodEthPkts_Object=MibScalar
lsBusStatsGoodEthPkts=_LsBusStatsGoodEthPkts_Object((1,3,6,1,4,1,81,19,3,2,7),_LsBusStatsGoodEthPkts_Type())
lsBusStatsGoodEthPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lsBusStatsGoodEthPkts.setStatus(_A)
_LsBusStatsGoodEthOctets_Type=Counter32
_LsBusStatsGoodEthOctets_Object=MibScalar
lsBusStatsGoodEthOctets=_LsBusStatsGoodEthOctets_Object((1,3,6,1,4,1,81,19,3,2,8),_LsBusStatsGoodEthOctets_Type())
lsBusStatsGoodEthOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:lsBusStatsGoodEthOctets.setStatus(_A)
_LsBusStatsBadEthPkts_Type=Counter32
_LsBusStatsBadEthPkts_Object=MibScalar
lsBusStatsBadEthPkts=_LsBusStatsBadEthPkts_Object((1,3,6,1,4,1,81,19,3,2,9),_LsBusStatsBadEthPkts_Type())
lsBusStatsBadEthPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lsBusStatsBadEthPkts.setStatus(_A)
_LsBusStatsBadEthOctets_Type=Counter32
_LsBusStatsBadEthOctets_Object=MibScalar
lsBusStatsBadEthOctets=_LsBusStatsBadEthOctets_Object((1,3,6,1,4,1,81,19,3,2,10),_LsBusStatsBadEthOctets_Type())
lsBusStatsBadEthOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:lsBusStatsBadEthOctets.setStatus(_A)
_LsBusStatsNonEthPkts_Type=Counter32
_LsBusStatsNonEthPkts_Object=MibScalar
lsBusStatsNonEthPkts=_LsBusStatsNonEthPkts_Object((1,3,6,1,4,1,81,19,3,2,11),_LsBusStatsNonEthPkts_Type())
lsBusStatsNonEthPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lsBusStatsNonEthPkts.setStatus(_A)
_LsBusStatsNonEthOctets_Type=Counter32
_LsBusStatsNonEthOctets_Object=MibScalar
lsBusStatsNonEthOctets=_LsBusStatsNonEthOctets_Object((1,3,6,1,4,1,81,19,3,2,12),_LsBusStatsNonEthOctets_Type())
lsBusStatsNonEthOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:lsBusStatsNonEthOctets.setStatus(_A)
_LsBusStatsPriorityTable_Object=MibTable
lsBusStatsPriorityTable=_LsBusStatsPriorityTable_Object((1,3,6,1,4,1,81,19,3,2,13))
if mibBuilder.loadTexts:lsBusStatsPriorityTable.setStatus(_A)
_LsBusStatsPriorityEntry_Object=MibTableRow
lsBusStatsPriorityEntry=_LsBusStatsPriorityEntry_Object((1,3,6,1,4,1,81,19,3,2,13,1))
lsBusStatsPriorityEntry.setIndexNames((0,_F,_o))
if mibBuilder.loadTexts:lsBusStatsPriorityEntry.setStatus(_A)
class _LsBusStatsPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_LsBusStatsPriorityIndex_Type.__name__=_C
_LsBusStatsPriorityIndex_Object=MibTableColumn
lsBusStatsPriorityIndex=_LsBusStatsPriorityIndex_Object((1,3,6,1,4,1,81,19,3,2,13,1,1),_LsBusStatsPriorityIndex_Type())
lsBusStatsPriorityIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lsBusStatsPriorityIndex.setStatus(_A)
_LsBusStatsPriorityPkts_Type=Counter32
_LsBusStatsPriorityPkts_Object=MibTableColumn
lsBusStatsPriorityPkts=_LsBusStatsPriorityPkts_Object((1,3,6,1,4,1,81,19,3,2,13,1,2),_LsBusStatsPriorityPkts_Type())
lsBusStatsPriorityPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lsBusStatsPriorityPkts.setStatus(_A)
_LsBusStatsPriorityOctets_Type=Counter32
_LsBusStatsPriorityOctets_Object=MibTableColumn
lsBusStatsPriorityOctets=_LsBusStatsPriorityOctets_Object((1,3,6,1,4,1,81,19,3,2,13,1,3),_LsBusStatsPriorityOctets_Type())
lsBusStatsPriorityOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:lsBusStatsPriorityOctets.setStatus(_A)
class _LsBusStatsVirtualNetList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_LsBusStatsVirtualNetList_Type.__name__=_I
_LsBusStatsVirtualNetList_Object=MibScalar
lsBusStatsVirtualNetList=_LsBusStatsVirtualNetList_Object((1,3,6,1,4,1,81,19,3,2,14),_LsBusStatsVirtualNetList_Type())
lsBusStatsVirtualNetList.setMaxAccess(_B)
if mibBuilder.loadTexts:lsBusStatsVirtualNetList.setStatus(_A)
_LsBusStatsVirtualNetTable_Object=MibTable
lsBusStatsVirtualNetTable=_LsBusStatsVirtualNetTable_Object((1,3,6,1,4,1,81,19,3,2,15))
if mibBuilder.loadTexts:lsBusStatsVirtualNetTable.setStatus(_A)
_LsBusStatsVirtualNetEntry_Object=MibTableRow
lsBusStatsVirtualNetEntry=_LsBusStatsVirtualNetEntry_Object((1,3,6,1,4,1,81,19,3,2,15,1))
lsBusStatsVirtualNetEntry.setIndexNames((0,_F,_p))
if mibBuilder.loadTexts:lsBusStatsVirtualNetEntry.setStatus(_A)
_LsBusStatsVirtualNet_Type=Integer32
_LsBusStatsVirtualNet_Object=MibTableColumn
lsBusStatsVirtualNet=_LsBusStatsVirtualNet_Object((1,3,6,1,4,1,81,19,3,2,15,1,1),_LsBusStatsVirtualNet_Type())
lsBusStatsVirtualNet.setMaxAccess(_B)
if mibBuilder.loadTexts:lsBusStatsVirtualNet.setStatus(_A)
_LsBusStatsVirtualNetPackets_Type=Counter32
_LsBusStatsVirtualNetPackets_Object=MibTableColumn
lsBusStatsVirtualNetPackets=_LsBusStatsVirtualNetPackets_Object((1,3,6,1,4,1,81,19,3,2,15,1,2),_LsBusStatsVirtualNetPackets_Type())
lsBusStatsVirtualNetPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:lsBusStatsVirtualNetPackets.setStatus(_A)
_LsBusStatsVirtualNetOctets_Type=Counter32
_LsBusStatsVirtualNetOctets_Object=MibTableColumn
lsBusStatsVirtualNetOctets=_LsBusStatsVirtualNetOctets_Object((1,3,6,1,4,1,81,19,3,2,15,1,3),_LsBusStatsVirtualNetOctets_Type())
lsBusStatsVirtualNetOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:lsBusStatsVirtualNetOctets.setStatus(_A)
_LsPortStats_ObjectIdentity=ObjectIdentity
lsPortStats=_LsPortStats_ObjectIdentity((1,3,6,1,4,1,81,19,3,3))
_LsPortControlTable_Object=MibTable
lsPortControlTable=_LsPortControlTable_Object((1,3,6,1,4,1,81,19,3,3,1))
if mibBuilder.loadTexts:lsPortControlTable.setStatus(_A)
_LsPortControlEntry_Object=MibTableRow
lsPortControlEntry=_LsPortControlEntry_Object((1,3,6,1,4,1,81,19,3,3,1,1))
lsPortControlEntry.setIndexNames((0,_F,_q))
if mibBuilder.loadTexts:lsPortControlEntry.setStatus(_A)
class _LsPortControlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_LsPortControlIndex_Type.__name__=_C
_LsPortControlIndex_Object=MibTableColumn
lsPortControlIndex=_LsPortControlIndex_Object((1,3,6,1,4,1,81,19,3,3,1,1,1),_LsPortControlIndex_Type())
lsPortControlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortControlIndex.setStatus(_A)
_LsPortControlDataSource_Type=ObjectIdentifier
_LsPortControlDataSource_Object=MibTableColumn
lsPortControlDataSource=_LsPortControlDataSource_Object((1,3,6,1,4,1,81,19,3,3,1,1,2),_LsPortControlDataSource_Type())
lsPortControlDataSource.setMaxAccess(_D)
if mibBuilder.loadTexts:lsPortControlDataSource.setStatus(_A)
_LsPortControlTableSize_Type=Integer32
_LsPortControlTableSize_Object=MibTableColumn
lsPortControlTableSize=_LsPortControlTableSize_Object((1,3,6,1,4,1,81,19,3,3,1,1,3),_LsPortControlTableSize_Type())
lsPortControlTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortControlTableSize.setStatus(_A)
_LsPortControlLastDeleteTime_Type=TimeTicks
_LsPortControlLastDeleteTime_Object=MibTableColumn
lsPortControlLastDeleteTime=_LsPortControlLastDeleteTime_Object((1,3,6,1,4,1,81,19,3,3,1,1,4),_LsPortControlLastDeleteTime_Type())
lsPortControlLastDeleteTime.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortControlLastDeleteTime.setStatus(_A)
_LsPortControlOwner_Type=DisplayString
_LsPortControlOwner_Object=MibTableColumn
lsPortControlOwner=_LsPortControlOwner_Object((1,3,6,1,4,1,81,19,3,3,1,1,5),_LsPortControlOwner_Type())
lsPortControlOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:lsPortControlOwner.setStatus(_A)
class _LsPortControlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),('createRequest',2),('underCreation',3),(_M,4)))
_LsPortControlStatus_Type.__name__=_C
_LsPortControlStatus_Object=MibTableColumn
lsPortControlStatus=_LsPortControlStatus_Object((1,3,6,1,4,1,81,19,3,3,1,1,6),_LsPortControlStatus_Type())
lsPortControlStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lsPortControlStatus.setStatus(_A)
_LsPortFilterTable_Object=MibTable
lsPortFilterTable=_LsPortFilterTable_Object((1,3,6,1,4,1,81,19,3,3,2))
if mibBuilder.loadTexts:lsPortFilterTable.setStatus(_A)
_LsPortFilterEntry_Object=MibTableRow
lsPortFilterEntry=_LsPortFilterEntry_Object((1,3,6,1,4,1,81,19,3,3,2,1))
lsPortFilterEntry.setIndexNames((0,_F,_r))
if mibBuilder.loadTexts:lsPortFilterEntry.setStatus(_A)
_LsPortFilter_Type=Integer32
_LsPortFilter_Object=MibTableColumn
lsPortFilter=_LsPortFilter_Object((1,3,6,1,4,1,81,19,3,3,2,1,1),_LsPortFilter_Type())
lsPortFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortFilter.setStatus(_A)
class _LsPortFilterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_L,1),(_M,4)))
_LsPortFilterStatus_Type.__name__=_C
_LsPortFilterStatus_Object=MibTableColumn
lsPortFilterStatus=_LsPortFilterStatus_Object((1,3,6,1,4,1,81,19,3,3,2,1,2),_LsPortFilterStatus_Type())
lsPortFilterStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lsPortFilterStatus.setStatus(_A)
class _LsPortFilterTableClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_LsPortFilterTableClear_Type.__name__=_C
_LsPortFilterTableClear_Object=MibScalar
lsPortFilterTableClear=_LsPortFilterTableClear_Object((1,3,6,1,4,1,81,19,3,3,3),_LsPortFilterTableClear_Type())
lsPortFilterTableClear.setMaxAccess(_D)
if mibBuilder.loadTexts:lsPortFilterTableClear.setStatus(_A)
_LsPortTable_Object=MibTable
lsPortTable=_LsPortTable_Object((1,3,6,1,4,1,81,19,3,3,4))
if mibBuilder.loadTexts:lsPortTable.setStatus(_A)
_LsPortEntry_Object=MibTableRow
lsPortEntry=_LsPortEntry_Object((1,3,6,1,4,1,81,19,3,3,4,1))
lsPortEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:lsPortEntry.setStatus(_A)
_LsPortNumber_Type=Integer32
_LsPortNumber_Object=MibTableColumn
lsPortNumber=_LsPortNumber_Object((1,3,6,1,4,1,81,19,3,3,4,1,1),_LsPortNumber_Type())
lsPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortNumber.setStatus(_A)
_LsPortInPkts_Type=Counter32
_LsPortInPkts_Object=MibTableColumn
lsPortInPkts=_LsPortInPkts_Object((1,3,6,1,4,1,81,19,3,3,4,1,2),_LsPortInPkts_Type())
lsPortInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortInPkts.setStatus(_A)
_LsPortInFCSErrors_Type=Counter32
_LsPortInFCSErrors_Object=MibTableColumn
lsPortInFCSErrors=_LsPortInFCSErrors_Object((1,3,6,1,4,1,81,19,3,3,4,1,3),_LsPortInFCSErrors_Type())
lsPortInFCSErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortInFCSErrors.setStatus(_A)
_LsPortInTooLongPkts_Type=Counter32
_LsPortInTooLongPkts_Object=MibTableColumn
lsPortInTooLongPkts=_LsPortInTooLongPkts_Object((1,3,6,1,4,1,81,19,3,3,4,1,4),_LsPortInTooLongPkts_Type())
lsPortInTooLongPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortInTooLongPkts.setStatus(_A)
_LsPortInOctets_Type=Counter32
_LsPortInOctets_Object=MibTableColumn
lsPortInOctets=_LsPortInOctets_Object((1,3,6,1,4,1,81,19,3,3,4,1,5),_LsPortInOctets_Type())
lsPortInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortInOctets.setStatus(_A)
_LsPortInTotalErrors_Type=Counter32
_LsPortInTotalErrors_Object=MibTableColumn
lsPortInTotalErrors=_LsPortInTotalErrors_Object((1,3,6,1,4,1,81,19,3,3,4,1,6),_LsPortInTotalErrors_Type())
lsPortInTotalErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortInTotalErrors.setStatus(_A)
_LsPortInCollisions_Type=Counter32
_LsPortInCollisions_Object=MibTableColumn
lsPortInCollisions=_LsPortInCollisions_Object((1,3,6,1,4,1,81,19,3,3,4,1,7),_LsPortInCollisions_Type())
lsPortInCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortInCollisions.setStatus(_A)
class _LsPortExtendedReportingList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_LsPortExtendedReportingList_Type.__name__=_I
_LsPortExtendedReportingList_Object=MibScalar
lsPortExtendedReportingList=_LsPortExtendedReportingList_Object((1,3,6,1,4,1,81,19,3,3,5),_LsPortExtendedReportingList_Type())
lsPortExtendedReportingList.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortExtendedReportingList.setStatus(_A)
_LsPortExtendedStatsTable_Object=MibTable
lsPortExtendedStatsTable=_LsPortExtendedStatsTable_Object((1,3,6,1,4,1,81,19,3,3,6))
if mibBuilder.loadTexts:lsPortExtendedStatsTable.setStatus(_A)
_LsPortExtendedStatsEntry_Object=MibTableRow
lsPortExtendedStatsEntry=_LsPortExtendedStatsEntry_Object((1,3,6,1,4,1,81,19,3,3,6,1))
lsPortExtendedStatsEntry.setIndexNames((0,_F,_s))
if mibBuilder.loadTexts:lsPortExtendedStatsEntry.setStatus(_A)
_LsPortExtendedStatsNumber_Type=Integer32
_LsPortExtendedStatsNumber_Object=MibTableColumn
lsPortExtendedStatsNumber=_LsPortExtendedStatsNumber_Object((1,3,6,1,4,1,81,19,3,3,6,1,1),_LsPortExtendedStatsNumber_Type())
lsPortExtendedStatsNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortExtendedStatsNumber.setStatus(_A)
class _LsPortCreationOrder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_LsPortCreationOrder_Type.__name__=_C
_LsPortCreationOrder_Object=MibTableColumn
lsPortCreationOrder=_LsPortCreationOrder_Object((1,3,6,1,4,1,81,19,3,3,6,1,2),_LsPortCreationOrder_Type())
lsPortCreationOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortCreationOrder.setStatus(_A)
class _LsPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_LsPortIndex_Type.__name__=_C
_LsPortIndex_Object=MibTableColumn
lsPortIndex=_LsPortIndex_Object((1,3,6,1,4,1,81,19,3,3,6,1,3),_LsPortIndex_Type())
lsPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortIndex.setStatus(_A)
_LsPortOutPkts_Type=Counter32
_LsPortOutPkts_Object=MibTableColumn
lsPortOutPkts=_LsPortOutPkts_Object((1,3,6,1,4,1,81,19,3,3,6,1,4),_LsPortOutPkts_Type())
lsPortOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortOutPkts.setStatus(_A)
_LsPortInBroadcastPkts_Type=Counter32
_LsPortInBroadcastPkts_Object=MibTableColumn
lsPortInBroadcastPkts=_LsPortInBroadcastPkts_Object((1,3,6,1,4,1,81,19,3,3,6,1,5),_LsPortInBroadcastPkts_Type())
lsPortInBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortInBroadcastPkts.setStatus(_A)
_LsPortInMulticastPkts_Type=Counter32
_LsPortInMulticastPkts_Object=MibTableColumn
lsPortInMulticastPkts=_LsPortInMulticastPkts_Object((1,3,6,1,4,1,81,19,3,3,6,1,6),_LsPortInMulticastPkts_Type())
lsPortInMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortInMulticastPkts.setStatus(_A)
_LsHostFilterTable_Object=MibTable
lsHostFilterTable=_LsHostFilterTable_Object((1,3,6,1,4,1,81,19,3,4))
if mibBuilder.loadTexts:lsHostFilterTable.setStatus(_A)
_LsHostFilterEntry_Object=MibTableRow
lsHostFilterEntry=_LsHostFilterEntry_Object((1,3,6,1,4,1,81,19,3,4,1))
lsHostFilterEntry.setIndexNames((0,_F,_t))
if mibBuilder.loadTexts:lsHostFilterEntry.setStatus(_A)
_LsHostFilterAddress_Type=OctetString
_LsHostFilterAddress_Object=MibTableColumn
lsHostFilterAddress=_LsHostFilterAddress_Object((1,3,6,1,4,1,81,19,3,4,1,1),_LsHostFilterAddress_Type())
lsHostFilterAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHostFilterAddress.setStatus(_A)
class _LsHostFilterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_L,1),(_M,4)))
_LsHostFilterStatus_Type.__name__=_C
_LsHostFilterStatus_Object=MibTableColumn
lsHostFilterStatus=_LsHostFilterStatus_Object((1,3,6,1,4,1,81,19,3,4,1,2),_LsHostFilterStatus_Type())
lsHostFilterStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lsHostFilterStatus.setStatus(_A)
class _LsHostFilterTableClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_LsHostFilterTableClear_Type.__name__=_C
_LsHostFilterTableClear_Object=MibScalar
lsHostFilterTableClear=_LsHostFilterTableClear_Object((1,3,6,1,4,1,81,19,3,5),_LsHostFilterTableClear_Type())
lsHostFilterTableClear.setMaxAccess(_D)
if mibBuilder.loadTexts:lsHostFilterTableClear.setStatus(_A)
_LsHostPortFilterTable_Object=MibTable
lsHostPortFilterTable=_LsHostPortFilterTable_Object((1,3,6,1,4,1,81,19,3,6))
if mibBuilder.loadTexts:lsHostPortFilterTable.setStatus(_A)
_LsHostPortFilterEntry_Object=MibTableRow
lsHostPortFilterEntry=_LsHostPortFilterEntry_Object((1,3,6,1,4,1,81,19,3,6,1))
lsHostPortFilterEntry.setIndexNames((0,_F,_u))
if mibBuilder.loadTexts:lsHostPortFilterEntry.setStatus(_A)
_LsHostPortFilter_Type=Integer32
_LsHostPortFilter_Object=MibTableColumn
lsHostPortFilter=_LsHostPortFilter_Object((1,3,6,1,4,1,81,19,3,6,1,1),_LsHostPortFilter_Type())
lsHostPortFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHostPortFilter.setStatus(_A)
class _LsHostPortFilterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_L,1),(_M,4)))
_LsHostPortFilterStatus_Type.__name__=_C
_LsHostPortFilterStatus_Object=MibTableColumn
lsHostPortFilterStatus=_LsHostPortFilterStatus_Object((1,3,6,1,4,1,81,19,3,6,1,2),_LsHostPortFilterStatus_Type())
lsHostPortFilterStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lsHostPortFilterStatus.setStatus(_A)
class _LsHostPortFilterTableClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_LsHostPortFilterTableClear_Type.__name__=_C
_LsHostPortFilterTableClear_Object=MibScalar
lsHostPortFilterTableClear=_LsHostPortFilterTableClear_Object((1,3,6,1,4,1,81,19,3,7),_LsHostPortFilterTableClear_Type())
lsHostPortFilterTableClear.setMaxAccess(_D)
if mibBuilder.loadTexts:lsHostPortFilterTableClear.setStatus(_A)
_LsMatrixFilterTable_Object=MibTable
lsMatrixFilterTable=_LsMatrixFilterTable_Object((1,3,6,1,4,1,81,19,3,8))
if mibBuilder.loadTexts:lsMatrixFilterTable.setStatus(_A)
_LsMatrixFilterEntry_Object=MibTableRow
lsMatrixFilterEntry=_LsMatrixFilterEntry_Object((1,3,6,1,4,1,81,19,3,8,1))
lsMatrixFilterEntry.setIndexNames((0,_F,_v))
if mibBuilder.loadTexts:lsMatrixFilterEntry.setStatus(_A)
_LsMatrixFilterAddress_Type=OctetString
_LsMatrixFilterAddress_Object=MibTableColumn
lsMatrixFilterAddress=_LsMatrixFilterAddress_Object((1,3,6,1,4,1,81,19,3,8,1,1),_LsMatrixFilterAddress_Type())
lsMatrixFilterAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:lsMatrixFilterAddress.setStatus(_A)
class _LsMatrixFilterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_L,1),(_M,4)))
_LsMatrixFilterStatus_Type.__name__=_C
_LsMatrixFilterStatus_Object=MibTableColumn
lsMatrixFilterStatus=_LsMatrixFilterStatus_Object((1,3,6,1,4,1,81,19,3,8,1,2),_LsMatrixFilterStatus_Type())
lsMatrixFilterStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lsMatrixFilterStatus.setStatus(_A)
class _LsMatrixFilterTableClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_LsMatrixFilterTableClear_Type.__name__=_C
_LsMatrixFilterTableClear_Object=MibScalar
lsMatrixFilterTableClear=_LsMatrixFilterTableClear_Object((1,3,6,1,4,1,81,19,3,9),_LsMatrixFilterTableClear_Type())
lsMatrixFilterTableClear.setMaxAccess(_D)
if mibBuilder.loadTexts:lsMatrixFilterTableClear.setStatus(_A)
_LsHostTimePortCorrTable_Object=MibTable
lsHostTimePortCorrTable=_LsHostTimePortCorrTable_Object((1,3,6,1,4,1,81,19,3,10))
if mibBuilder.loadTexts:lsHostTimePortCorrTable.setStatus(_A)
_LsHostTimePortCorrEntry_Object=MibTableRow
lsHostTimePortCorrEntry=_LsHostTimePortCorrEntry_Object((1,3,6,1,4,1,81,19,3,10,1))
lsHostTimePortCorrEntry.setIndexNames((0,_F,_w),(0,_F,_x))
if mibBuilder.loadTexts:lsHostTimePortCorrEntry.setStatus(_A)
_HostTimeAddress_Type=OctetString
_HostTimeAddress_Object=MibTableColumn
hostTimeAddress=_HostTimeAddress_Object((1,3,6,1,4,1,81,19,3,10,1,1),_HostTimeAddress_Type())
hostTimeAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hostTimeAddress.setStatus(_A)
class _HostTimeCreationOrder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HostTimeCreationOrder_Type.__name__=_C
_HostTimeCreationOrder_Object=MibTableColumn
hostTimeCreationOrder=_HostTimeCreationOrder_Object((1,3,6,1,4,1,81,19,3,10,1,2),_HostTimeCreationOrder_Type())
hostTimeCreationOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:hostTimeCreationOrder.setStatus(_A)
class _HostTimeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HostTimeIndex_Type.__name__=_C
_HostTimeIndex_Object=MibTableColumn
hostTimeIndex=_HostTimeIndex_Object((1,3,6,1,4,1,81,19,3,10,1,3),_HostTimeIndex_Type())
hostTimeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hostTimeIndex.setStatus(_A)
_HostTimePortConnection_Type=Integer32
_HostTimePortConnection_Object=MibTableColumn
hostTimePortConnection=_HostTimePortConnection_Object((1,3,6,1,4,1,81,19,3,10,1,4),_HostTimePortConnection_Type())
hostTimePortConnection.setMaxAccess(_B)
if mibBuilder.loadTexts:hostTimePortConnection.setStatus(_A)
_LsHistoryTable_Object=MibTable
lsHistoryTable=_LsHistoryTable_Object((1,3,6,1,4,1,81,19,3,11))
if mibBuilder.loadTexts:lsHistoryTable.setStatus(_A)
_LsHistoryEntry_Object=MibTableRow
lsHistoryEntry=_LsHistoryEntry_Object((1,3,6,1,4,1,81,19,3,11,1))
lsHistoryEntry.setIndexNames((0,_F,_y),(0,_F,_z))
if mibBuilder.loadTexts:lsHistoryEntry.setStatus(_A)
_LsHistoryIndex_Type=Integer32
_LsHistoryIndex_Object=MibTableColumn
lsHistoryIndex=_LsHistoryIndex_Object((1,3,6,1,4,1,81,19,3,11,1,1),_LsHistoryIndex_Type())
lsHistoryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHistoryIndex.setStatus(_A)
class _LsHistorySampleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LsHistorySampleIndex_Type.__name__=_C
_LsHistorySampleIndex_Object=MibTableColumn
lsHistorySampleIndex=_LsHistorySampleIndex_Object((1,3,6,1,4,1,81,19,3,11,1,2),_LsHistorySampleIndex_Type())
lsHistorySampleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHistorySampleIndex.setStatus(_A)
_LsHistoryIntervalTime_Type=TimeTicks
_LsHistoryIntervalTime_Object=MibTableColumn
lsHistoryIntervalTime=_LsHistoryIntervalTime_Object((1,3,6,1,4,1,81,19,3,11,1,3),_LsHistoryIntervalTime_Type())
lsHistoryIntervalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHistoryIntervalTime.setStatus(_A)
_LsHistoryStatsDropEvents_Type=Counter32
_LsHistoryStatsDropEvents_Object=MibTableColumn
lsHistoryStatsDropEvents=_LsHistoryStatsDropEvents_Object((1,3,6,1,4,1,81,19,3,11,1,4),_LsHistoryStatsDropEvents_Type())
lsHistoryStatsDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHistoryStatsDropEvents.setStatus(_A)
_LsHistoryStatsPkts_Type=Counter32
_LsHistoryStatsPkts_Object=MibTableColumn
lsHistoryStatsPkts=_LsHistoryStatsPkts_Object((1,3,6,1,4,1,81,19,3,11,1,5),_LsHistoryStatsPkts_Type())
lsHistoryStatsPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHistoryStatsPkts.setStatus(_A)
_LsHistoryStatsOctets_Type=Counter32
_LsHistoryStatsOctets_Object=MibTableColumn
lsHistoryStatsOctets=_LsHistoryStatsOctets_Object((1,3,6,1,4,1,81,19,3,11,1,6),_LsHistoryStatsOctets_Type())
lsHistoryStatsOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHistoryStatsOctets.setStatus(_A)
_LsHistoryStatsEthBroadcastPkts_Type=Counter32
_LsHistoryStatsEthBroadcastPkts_Object=MibTableColumn
lsHistoryStatsEthBroadcastPkts=_LsHistoryStatsEthBroadcastPkts_Object((1,3,6,1,4,1,81,19,3,11,1,7),_LsHistoryStatsEthBroadcastPkts_Type())
lsHistoryStatsEthBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHistoryStatsEthBroadcastPkts.setStatus(_A)
_LsHistoryStatsEthMulticastPkts_Type=Counter32
_LsHistoryStatsEthMulticastPkts_Object=MibTableColumn
lsHistoryStatsEthMulticastPkts=_LsHistoryStatsEthMulticastPkts_Object((1,3,6,1,4,1,81,19,3,11,1,8),_LsHistoryStatsEthMulticastPkts_Type())
lsHistoryStatsEthMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHistoryStatsEthMulticastPkts.setStatus(_A)
_LsHistoryStatsGoodEthPkts_Type=Counter32
_LsHistoryStatsGoodEthPkts_Object=MibTableColumn
lsHistoryStatsGoodEthPkts=_LsHistoryStatsGoodEthPkts_Object((1,3,6,1,4,1,81,19,3,11,1,9),_LsHistoryStatsGoodEthPkts_Type())
lsHistoryStatsGoodEthPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHistoryStatsGoodEthPkts.setStatus(_A)
_LsHistoryStatsGoodEthOctets_Type=Counter32
_LsHistoryStatsGoodEthOctets_Object=MibTableColumn
lsHistoryStatsGoodEthOctets=_LsHistoryStatsGoodEthOctets_Object((1,3,6,1,4,1,81,19,3,11,1,10),_LsHistoryStatsGoodEthOctets_Type())
lsHistoryStatsGoodEthOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHistoryStatsGoodEthOctets.setStatus(_A)
_LsHistoryStatsBadEthPkts_Type=Counter32
_LsHistoryStatsBadEthPkts_Object=MibTableColumn
lsHistoryStatsBadEthPkts=_LsHistoryStatsBadEthPkts_Object((1,3,6,1,4,1,81,19,3,11,1,11),_LsHistoryStatsBadEthPkts_Type())
lsHistoryStatsBadEthPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHistoryStatsBadEthPkts.setStatus(_A)
_LsHistoryStatsBadEthOctets_Type=Counter32
_LsHistoryStatsBadEthOctets_Object=MibTableColumn
lsHistoryStatsBadEthOctets=_LsHistoryStatsBadEthOctets_Object((1,3,6,1,4,1,81,19,3,11,1,12),_LsHistoryStatsBadEthOctets_Type())
lsHistoryStatsBadEthOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHistoryStatsBadEthOctets.setStatus(_A)
_LsHistoryStatsNonEthPkts_Type=Counter32
_LsHistoryStatsNonEthPkts_Object=MibTableColumn
lsHistoryStatsNonEthPkts=_LsHistoryStatsNonEthPkts_Object((1,3,6,1,4,1,81,19,3,11,1,13),_LsHistoryStatsNonEthPkts_Type())
lsHistoryStatsNonEthPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHistoryStatsNonEthPkts.setStatus(_A)
_LsHistoryStatsNonEthOctets_Type=Counter32
_LsHistoryStatsNonEthOctets_Object=MibTableColumn
lsHistoryStatsNonEthOctets=_LsHistoryStatsNonEthOctets_Object((1,3,6,1,4,1,81,19,3,11,1,14),_LsHistoryStatsNonEthOctets_Type())
lsHistoryStatsNonEthOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHistoryStatsNonEthOctets.setStatus(_A)
_LsHistoryStatsPriority1Pkts_Type=Counter32
_LsHistoryStatsPriority1Pkts_Object=MibTableColumn
lsHistoryStatsPriority1Pkts=_LsHistoryStatsPriority1Pkts_Object((1,3,6,1,4,1,81,19,3,11,1,15),_LsHistoryStatsPriority1Pkts_Type())
lsHistoryStatsPriority1Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHistoryStatsPriority1Pkts.setStatus(_A)
_LsHistoryStatsPriority1Octets_Type=Counter32
_LsHistoryStatsPriority1Octets_Object=MibTableColumn
lsHistoryStatsPriority1Octets=_LsHistoryStatsPriority1Octets_Object((1,3,6,1,4,1,81,19,3,11,1,16),_LsHistoryStatsPriority1Octets_Type())
lsHistoryStatsPriority1Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHistoryStatsPriority1Octets.setStatus(_A)
_LsHistoryStatsPriority2Pkts_Type=Counter32
_LsHistoryStatsPriority2Pkts_Object=MibTableColumn
lsHistoryStatsPriority2Pkts=_LsHistoryStatsPriority2Pkts_Object((1,3,6,1,4,1,81,19,3,11,1,17),_LsHistoryStatsPriority2Pkts_Type())
lsHistoryStatsPriority2Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHistoryStatsPriority2Pkts.setStatus(_A)
_LsHistoryStatsPriority2Octets_Type=Counter32
_LsHistoryStatsPriority2Octets_Object=MibTableColumn
lsHistoryStatsPriority2Octets=_LsHistoryStatsPriority2Octets_Object((1,3,6,1,4,1,81,19,3,11,1,18),_LsHistoryStatsPriority2Octets_Type())
lsHistoryStatsPriority2Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHistoryStatsPriority2Octets.setStatus(_A)
_LsHistoryStatsPriority3Pkts_Type=Counter32
_LsHistoryStatsPriority3Pkts_Object=MibTableColumn
lsHistoryStatsPriority3Pkts=_LsHistoryStatsPriority3Pkts_Object((1,3,6,1,4,1,81,19,3,11,1,19),_LsHistoryStatsPriority3Pkts_Type())
lsHistoryStatsPriority3Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHistoryStatsPriority3Pkts.setStatus(_A)
_LsHistoryStatsPriority3Octets_Type=Counter32
_LsHistoryStatsPriority3Octets_Object=MibTableColumn
lsHistoryStatsPriority3Octets=_LsHistoryStatsPriority3Octets_Object((1,3,6,1,4,1,81,19,3,11,1,20),_LsHistoryStatsPriority3Octets_Type())
lsHistoryStatsPriority3Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHistoryStatsPriority3Octets.setStatus(_A)
_LsHistoryStatsPriority4Pkts_Type=Counter32
_LsHistoryStatsPriority4Pkts_Object=MibTableColumn
lsHistoryStatsPriority4Pkts=_LsHistoryStatsPriority4Pkts_Object((1,3,6,1,4,1,81,19,3,11,1,21),_LsHistoryStatsPriority4Pkts_Type())
lsHistoryStatsPriority4Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHistoryStatsPriority4Pkts.setStatus(_A)
_LsHistoryStatsPriority4Octets_Type=Counter32
_LsHistoryStatsPriority4Octets_Object=MibTableColumn
lsHistoryStatsPriority4Octets=_LsHistoryStatsPriority4Octets_Object((1,3,6,1,4,1,81,19,3,11,1,22),_LsHistoryStatsPriority4Octets_Type())
lsHistoryStatsPriority4Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHistoryStatsPriority4Octets.setStatus(_A)
class _LsHistoryBusUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LsHistoryBusUtilization_Type.__name__=_C
_LsHistoryBusUtilization_Object=MibTableColumn
lsHistoryBusUtilization=_LsHistoryBusUtilization_Object((1,3,6,1,4,1,81,19,3,11,1,23),_LsHistoryBusUtilization_Type())
lsHistoryBusUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:lsHistoryBusUtilization.setStatus(_A)
_Lst_ObjectIdentity=ObjectIdentity
lst=_Lst_ObjectIdentity((1,3,6,1,4,1,81,19,4))
_LstIntPort_ObjectIdentity=ObjectIdentity
lstIntPort=_LstIntPort_ObjectIdentity((1,3,6,1,4,1,81,19,4,1))
_LstIntPortTable_Object=MibTable
lstIntPortTable=_LstIntPortTable_Object((1,3,6,1,4,1,81,19,4,1,1))
if mibBuilder.loadTexts:lstIntPortTable.setStatus(_A)
_LstIntPortEntry_Object=MibTableRow
lstIntPortEntry=_LstIntPortEntry_Object((1,3,6,1,4,1,81,19,4,1,1,1))
lstIntPortEntry.setIndexNames((0,_F,_A0),(0,_F,_A1))
if mibBuilder.loadTexts:lstIntPortEntry.setStatus(_A)
class _LstIntPortGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_LstIntPortGroupId_Type.__name__=_C
_LstIntPortGroupId_Object=MibTableColumn
lstIntPortGroupId=_LstIntPortGroupId_Object((1,3,6,1,4,1,81,19,4,1,1,1,1),_LstIntPortGroupId_Type())
lstIntPortGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:lstIntPortGroupId.setStatus(_A)
class _LstIntPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_LstIntPortId_Type.__name__=_C
_LstIntPortId_Object=MibTableColumn
lstIntPortId=_LstIntPortId_Object((1,3,6,1,4,1,81,19,4,1,1,1,2),_LstIntPortId_Type())
lstIntPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:lstIntPortId.setStatus(_A)
class _LstIntPortSidebandMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LstIntPortSidebandMode_Type.__name__=_C
_LstIntPortSidebandMode_Object=MibTableColumn
lstIntPortSidebandMode=_LstIntPortSidebandMode_Object((1,3,6,1,4,1,81,19,4,1,1,1,3),_LstIntPortSidebandMode_Type())
lstIntPortSidebandMode.setMaxAccess(_D)
if mibBuilder.loadTexts:lstIntPortSidebandMode.setStatus(_A)
_LstIntPortTotalOctets_Type=Counter32
_LstIntPortTotalOctets_Object=MibTableColumn
lstIntPortTotalOctets=_LstIntPortTotalOctets_Object((1,3,6,1,4,1,81,19,4,1,1,1,4),_LstIntPortTotalOctets_Type())
lstIntPortTotalOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:lstIntPortTotalOctets.setStatus(_A)
class _LstIntPortTotalTraffic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LstIntPortTotalTraffic_Type.__name__=_C
_LstIntPortTotalTraffic_Object=MibTableColumn
lstIntPortTotalTraffic=_LstIntPortTotalTraffic_Object((1,3,6,1,4,1,81,19,4,1,1,1,5),_LstIntPortTotalTraffic_Type())
lstIntPortTotalTraffic.setMaxAccess(_B)
if mibBuilder.loadTexts:lstIntPortTotalTraffic.setStatus(_A)
_LstIntPortLocalOctets_Type=Counter32
_LstIntPortLocalOctets_Object=MibTableColumn
lstIntPortLocalOctets=_LstIntPortLocalOctets_Object((1,3,6,1,4,1,81,19,4,1,1,1,6),_LstIntPortLocalOctets_Type())
lstIntPortLocalOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:lstIntPortLocalOctets.setStatus(_A)
class _LstIntPortLocalTraffic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LstIntPortLocalTraffic_Type.__name__=_C
_LstIntPortLocalTraffic_Object=MibTableColumn
lstIntPortLocalTraffic=_LstIntPortLocalTraffic_Object((1,3,6,1,4,1,81,19,4,1,1,1,7),_LstIntPortLocalTraffic_Type())
lstIntPortLocalTraffic.setMaxAccess(_B)
if mibBuilder.loadTexts:lstIntPortLocalTraffic.setStatus(_A)
_LstIntPortInOctets_Type=Counter32
_LstIntPortInOctets_Object=MibTableColumn
lstIntPortInOctets=_LstIntPortInOctets_Object((1,3,6,1,4,1,81,19,4,1,1,1,8),_LstIntPortInOctets_Type())
lstIntPortInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:lstIntPortInOctets.setStatus(_A)
class _LstIntPortInTraffic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LstIntPortInTraffic_Type.__name__=_C
_LstIntPortInTraffic_Object=MibTableColumn
lstIntPortInTraffic=_LstIntPortInTraffic_Object((1,3,6,1,4,1,81,19,4,1,1,1,9),_LstIntPortInTraffic_Type())
lstIntPortInTraffic.setMaxAccess(_B)
if mibBuilder.loadTexts:lstIntPortInTraffic.setStatus(_A)
_LstIntPortOutOctets_Type=Counter32
_LstIntPortOutOctets_Object=MibTableColumn
lstIntPortOutOctets=_LstIntPortOutOctets_Object((1,3,6,1,4,1,81,19,4,1,1,1,10),_LstIntPortOutOctets_Type())
lstIntPortOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:lstIntPortOutOctets.setStatus(_A)
class _LstIntPortOutTraffic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LstIntPortOutTraffic_Type.__name__=_C
_LstIntPortOutTraffic_Object=MibTableColumn
lstIntPortOutTraffic=_LstIntPortOutTraffic_Object((1,3,6,1,4,1,81,19,4,1,1,1,11),_LstIntPortOutTraffic_Type())
lstIntPortOutTraffic.setMaxAccess(_B)
if mibBuilder.loadTexts:lstIntPortOutTraffic.setStatus(_A)
_LstIntPortTotalFrames_Type=Counter32
_LstIntPortTotalFrames_Object=MibTableColumn
lstIntPortTotalFrames=_LstIntPortTotalFrames_Object((1,3,6,1,4,1,81,19,4,1,1,1,12),_LstIntPortTotalFrames_Type())
lstIntPortTotalFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:lstIntPortTotalFrames.setStatus(_A)
_LstIntPortLostFrames_Type=Counter32
_LstIntPortLostFrames_Object=MibTableColumn
lstIntPortLostFrames=_LstIntPortLostFrames_Object((1,3,6,1,4,1,81,19,4,1,1,1,13),_LstIntPortLostFrames_Type())
lstIntPortLostFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:lstIntPortLostFrames.setStatus(_A)
_LstIntPortClaimFrames_Type=Counter32
_LstIntPortClaimFrames_Object=MibTableColumn
lstIntPortClaimFrames=_LstIntPortClaimFrames_Object((1,3,6,1,4,1,81,19,4,1,1,1,16),_LstIntPortClaimFrames_Type())
lstIntPortClaimFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:lstIntPortClaimFrames.setStatus(_A)
_LstIntPortPurgeFrames_Type=Counter32
_LstIntPortPurgeFrames_Object=MibTableColumn
lstIntPortPurgeFrames=_LstIntPortPurgeFrames_Object((1,3,6,1,4,1,81,19,4,1,1,1,17),_LstIntPortPurgeFrames_Type())
lstIntPortPurgeFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:lstIntPortPurgeFrames.setStatus(_A)
class _LstIntPortNormallyCloseOpen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('normallyClose',1),('normallyOpen',2),(_E,255)))
_LstIntPortNormallyCloseOpen_Type.__name__=_C
_LstIntPortNormallyCloseOpen_Object=MibTableColumn
lstIntPortNormallyCloseOpen=_LstIntPortNormallyCloseOpen_Object((1,3,6,1,4,1,81,19,4,1,1,1,18),_LstIntPortNormallyCloseOpen_Type())
lstIntPortNormallyCloseOpen.setMaxAccess(_D)
if mibBuilder.loadTexts:lstIntPortNormallyCloseOpen.setStatus(_A)
class _LstIntPortSlicingEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LstIntPortSlicingEnable_Type.__name__=_C
_LstIntPortSlicingEnable_Object=MibTableColumn
lstIntPortSlicingEnable=_LstIntPortSlicingEnable_Object((1,3,6,1,4,1,81,19,4,1,1,1,19),_LstIntPortSlicingEnable_Type())
lstIntPortSlicingEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:lstIntPortSlicingEnable.setStatus(_A)
_LstIntPortSliceLength_Type=Integer32
_LstIntPortSliceLength_Object=MibTableColumn
lstIntPortSliceLength=_LstIntPortSliceLength_Object((1,3,6,1,4,1,81,19,4,1,1,1,20),_LstIntPortSliceLength_Type())
lstIntPortSliceLength.setMaxAccess(_D)
if mibBuilder.loadTexts:lstIntPortSliceLength.setStatus(_A)
class _LstIntPortUNAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_LstIntPortUNAddr_Type.__name__=_I
_LstIntPortUNAddr_Object=MibTableColumn
lstIntPortUNAddr=_LstIntPortUNAddr_Object((1,3,6,1,4,1,81,19,4,1,1,1,21),_LstIntPortUNAddr_Type())
lstIntPortUNAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:lstIntPortUNAddr.setStatus(_A)
class _LstIntPortMACAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_LstIntPortMACAddress_Type.__name__=_I
_LstIntPortMACAddress_Object=MibTableColumn
lstIntPortMACAddress=_LstIntPortMACAddress_Object((1,3,6,1,4,1,81,19,4,1,1,1,22),_LstIntPortMACAddress_Type())
lstIntPortMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:lstIntPortMACAddress.setStatus(_A)
class _LstIntPortSMPTransmitEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LstIntPortSMPTransmitEnable_Type.__name__=_C
_LstIntPortSMPTransmitEnable_Object=MibTableColumn
lstIntPortSMPTransmitEnable=_LstIntPortSMPTransmitEnable_Object((1,3,6,1,4,1,81,19,4,1,1,1,23),_LstIntPortSMPTransmitEnable_Type())
lstIntPortSMPTransmitEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:lstIntPortSMPTransmitEnable.setStatus(_A)
class _LstIntPortIPGLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_LstIntPortIPGLength_Type.__name__=_C
_LstIntPortIPGLength_Object=MibTableColumn
lstIntPortIPGLength=_LstIntPortIPGLength_Object((1,3,6,1,4,1,81,19,4,1,1,1,24),_LstIntPortIPGLength_Type())
lstIntPortIPGLength.setMaxAccess(_D)
if mibBuilder.loadTexts:lstIntPortIPGLength.setStatus(_A)
class _LstIntPortBPDummyWindow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_LstIntPortBPDummyWindow_Type.__name__=_C
_LstIntPortBPDummyWindow_Object=MibTableColumn
lstIntPortBPDummyWindow=_LstIntPortBPDummyWindow_Object((1,3,6,1,4,1,81,19,4,1,1,1,25),_LstIntPortBPDummyWindow_Type())
lstIntPortBPDummyWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:lstIntPortBPDummyWindow.setStatus(_A)
_LstIntPortBPTokenWindow_Type=Integer32
_LstIntPortBPTokenWindow_Object=MibTableColumn
lstIntPortBPTokenWindow=_LstIntPortBPTokenWindow_Object((1,3,6,1,4,1,81,19,4,1,1,1,26),_LstIntPortBPTokenWindow_Type())
lstIntPortBPTokenWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:lstIntPortBPTokenWindow.setStatus(_A)
_LstIntPortTransmitWindow_Type=Integer32
_LstIntPortTransmitWindow_Object=MibTableColumn
lstIntPortTransmitWindow=_LstIntPortTransmitWindow_Object((1,3,6,1,4,1,81,19,4,1,1,1,27),_LstIntPortTransmitWindow_Type())
lstIntPortTransmitWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:lstIntPortTransmitWindow.setStatus(_A)
class _LstIntPortBlockingPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_LstIntPortBlockingPriority_Type.__name__=_C
_LstIntPortBlockingPriority_Object=MibTableColumn
lstIntPortBlockingPriority=_LstIntPortBlockingPriority_Object((1,3,6,1,4,1,81,19,4,1,1,1,28),_LstIntPortBlockingPriority_Type())
lstIntPortBlockingPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:lstIntPortBlockingPriority.setStatus(_A)
class _LstIntPortNormalPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_LstIntPortNormalPriority_Type.__name__=_C
_LstIntPortNormalPriority_Object=MibTableColumn
lstIntPortNormalPriority=_LstIntPortNormalPriority_Object((1,3,6,1,4,1,81,19,4,1,1,1,29),_LstIntPortNormalPriority_Type())
lstIntPortNormalPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:lstIntPortNormalPriority.setStatus(_A)
class _LstIntPortDummyMV_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_LstIntPortDummyMV_Type.__name__=_C
_LstIntPortDummyMV_Object=MibTableColumn
lstIntPortDummyMV=_LstIntPortDummyMV_Object((1,3,6,1,4,1,81,19,4,1,1,1,30),_LstIntPortDummyMV_Type())
lstIntPortDummyMV.setMaxAccess(_D)
if mibBuilder.loadTexts:lstIntPortDummyMV.setStatus(_A)
_LstIntPortTxConsecutiveBusiesThresh_Type=Integer32
_LstIntPortTxConsecutiveBusiesThresh_Object=MibTableColumn
lstIntPortTxConsecutiveBusiesThresh=_LstIntPortTxConsecutiveBusiesThresh_Object((1,3,6,1,4,1,81,19,4,1,1,1,31),_LstIntPortTxConsecutiveBusiesThresh_Type())
lstIntPortTxConsecutiveBusiesThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:lstIntPortTxConsecutiveBusiesThresh.setStatus(_A)
_LstIntPortTxBufFullThresh_Type=Integer32
_LstIntPortTxBufFullThresh_Object=MibTableColumn
lstIntPortTxBufFullThresh=_LstIntPortTxBufFullThresh_Object((1,3,6,1,4,1,81,19,4,1,1,1,32),_LstIntPortTxBufFullThresh_Type())
lstIntPortTxBufFullThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:lstIntPortTxBufFullThresh.setStatus(_A)
_LstIntPortRxEmpty0_Type=Integer32
_LstIntPortRxEmpty0_Object=MibTableColumn
lstIntPortRxEmpty0=_LstIntPortRxEmpty0_Object((1,3,6,1,4,1,81,19,4,1,1,1,33),_LstIntPortRxEmpty0_Type())
lstIntPortRxEmpty0.setMaxAccess(_D)
if mibBuilder.loadTexts:lstIntPortRxEmpty0.setStatus(_A)
_LstIntPortRxEmpty1_Type=Integer32
_LstIntPortRxEmpty1_Object=MibTableColumn
lstIntPortRxEmpty1=_LstIntPortRxEmpty1_Object((1,3,6,1,4,1,81,19,4,1,1,1,34),_LstIntPortRxEmpty1_Type())
lstIntPortRxEmpty1.setMaxAccess(_D)
if mibBuilder.loadTexts:lstIntPortRxEmpty1.setStatus(_A)
_LstIntPortRxEmpty2_Type=Integer32
_LstIntPortRxEmpty2_Object=MibTableColumn
lstIntPortRxEmpty2=_LstIntPortRxEmpty2_Object((1,3,6,1,4,1,81,19,4,1,1,1,35),_LstIntPortRxEmpty2_Type())
lstIntPortRxEmpty2.setMaxAccess(_D)
if mibBuilder.loadTexts:lstIntPortRxEmpty2.setStatus(_A)
_LstIntPortRxFull_Type=Integer32
_LstIntPortRxFull_Object=MibTableColumn
lstIntPortRxFull=_LstIntPortRxFull_Object((1,3,6,1,4,1,81,19,4,1,1,1,36),_LstIntPortRxFull_Type())
lstIntPortRxFull.setMaxAccess(_D)
if mibBuilder.loadTexts:lstIntPortRxFull.setStatus(_A)
class _LstIntPortBPEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_O,1),(_P,2),(_E,255)))
_LstIntPortBPEnable_Type.__name__=_C
_LstIntPortBPEnable_Object=MibTableColumn
lstIntPortBPEnable=_LstIntPortBPEnable_Object((1,3,6,1,4,1,81,19,4,1,1,1,37),_LstIntPortBPEnable_Type())
lstIntPortBPEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:lstIntPortBPEnable.setStatus(_A)
class _LstIntPortRouteSideband_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_G,1),(_H,2),(_E,255)))
_LstIntPortRouteSideband_Type.__name__=_C
_LstIntPortRouteSideband_Object=MibTableColumn
lstIntPortRouteSideband=_LstIntPortRouteSideband_Object((1,3,6,1,4,1,81,19,4,1,1,1,38),_LstIntPortRouteSideband_Type())
lstIntPortRouteSideband.setMaxAccess(_D)
if mibBuilder.loadTexts:lstIntPortRouteSideband.setStatus(_A)
_LseWANTable_Object=MibTable
lseWANTable=_LseWANTable_Object((1,3,6,1,4,1,81,19,5))
if mibBuilder.loadTexts:lseWANTable.setStatus(_A)
_LseWANEntry_Object=MibTableRow
lseWANEntry=_LseWANEntry_Object((1,3,6,1,4,1,81,19,5,1))
lseWANEntry.setIndexNames((0,_F,_A2),(0,_F,_A3))
if mibBuilder.loadTexts:lseWANEntry.setStatus(_A)
_LseWANGroupId_Type=Integer32
_LseWANGroupId_Object=MibTableColumn
lseWANGroupId=_LseWANGroupId_Object((1,3,6,1,4,1,81,19,5,1,1),_LseWANGroupId_Type())
lseWANGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:lseWANGroupId.setStatus(_A)
_LseWANPortId_Type=Integer32
_LseWANPortId_Object=MibTableColumn
lseWANPortId=_LseWANPortId_Object((1,3,6,1,4,1,81,19,5,1,2),_LseWANPortId_Type())
lseWANPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:lseWANPortId.setStatus(_A)
class _LseWANConnection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('connected',1),('disconnected',2)))
_LseWANConnection_Type.__name__=_C
_LseWANConnection_Object=MibTableColumn
lseWANConnection=_LseWANConnection_Object((1,3,6,1,4,1,81,19,5,1,3),_LseWANConnection_Type())
lseWANConnection.setMaxAccess(_B)
if mibBuilder.loadTexts:lseWANConnection.setStatus(_A)
_LsVNChange_ObjectIdentity=ObjectIdentity
lsVNChange=_LsVNChange_ObjectIdentity((1,3,6,1,4,1,81,19,6))
class _LsVNChangeMACAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_LsVNChangeMACAddress_Type.__name__=_I
_LsVNChangeMACAddress_Object=MibScalar
lsVNChangeMACAddress=_LsVNChangeMACAddress_Object((1,3,6,1,4,1,81,19,6,1),_LsVNChangeMACAddress_Type())
lsVNChangeMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:lsVNChangeMACAddress.setStatus(_A)
class _LsVNChangeDetected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_LsVNChangeDetected_Type.__name__=_C
_LsVNChangeDetected_Object=MibScalar
lsVNChangeDetected=_LsVNChangeDetected_Object((1,3,6,1,4,1,81,19,6,2),_LsVNChangeDetected_Type())
lsVNChangeDetected.setMaxAccess(_B)
if mibBuilder.loadTexts:lsVNChangeDetected.setStatus(_A)
class _LsVNChangeExpected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_LsVNChangeExpected_Type.__name__=_C
_LsVNChangeExpected_Object=MibScalar
lsVNChangeExpected=_LsVNChangeExpected_Object((1,3,6,1,4,1,81,19,6,3),_LsVNChangeExpected_Type())
lsVNChangeExpected.setMaxAccess(_B)
if mibBuilder.loadTexts:lsVNChangeExpected.setStatus(_A)
_LsVNChangeGroup_Type=Integer32
_LsVNChangeGroup_Object=MibScalar
lsVNChangeGroup=_LsVNChangeGroup_Object((1,3,6,1,4,1,81,19,6,4),_LsVNChangeGroup_Type())
lsVNChangeGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:lsVNChangeGroup.setStatus(_A)
_LsVNChangePort_Type=Integer32
_LsVNChangePort_Object=MibScalar
lsVNChangePort=_LsVNChangePort_Object((1,3,6,1,4,1,81,19,6,5),_LsVNChangePort_Type())
lsVNChangePort.setMaxAccess(_B)
if mibBuilder.loadTexts:lsVNChangePort.setStatus(_A)
_VnsPacket_ObjectIdentity=ObjectIdentity
vnsPacket=_VnsPacket_ObjectIdentity((1,3,6,1,4,1,81,19,7))
_VnsPacketTable_Object=MibTable
vnsPacketTable=_VnsPacketTable_Object((1,3,6,1,4,1,81,19,7,1))
if mibBuilder.loadTexts:vnsPacketTable.setStatus(_A)
_VnsPacketEntry_Object=MibTableRow
vnsPacketEntry=_VnsPacketEntry_Object((1,3,6,1,4,1,81,19,7,1,1))
vnsPacketEntry.setIndexNames((0,_F,_A4))
if mibBuilder.loadTexts:vnsPacketEntry.setStatus(_A)
class _VnsPacketMACAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_VnsPacketMACAddress_Type.__name__=_I
_VnsPacketMACAddress_Object=MibTableColumn
vnsPacketMACAddress=_VnsPacketMACAddress_Object((1,3,6,1,4,1,81,19,7,1,1,1),_VnsPacketMACAddress_Type())
vnsPacketMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:vnsPacketMACAddress.setStatus(_A)
class _VnsPacketProtocolTypeMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_VnsPacketProtocolTypeMask_Type.__name__=_I
_VnsPacketProtocolTypeMask_Object=MibTableColumn
vnsPacketProtocolTypeMask=_VnsPacketProtocolTypeMask_Object((1,3,6,1,4,1,81,19,7,1,1,2),_VnsPacketProtocolTypeMask_Type())
vnsPacketProtocolTypeMask.setMaxAccess(_B)
if mibBuilder.loadTexts:vnsPacketProtocolTypeMask.setStatus(_A)
_VnsPacketIPAddress_Type=IpAddress
_VnsPacketIPAddress_Object=MibTableColumn
vnsPacketIPAddress=_VnsPacketIPAddress_Object((1,3,6,1,4,1,81,19,7,1,1,3),_VnsPacketIPAddress_Type())
vnsPacketIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:vnsPacketIPAddress.setStatus(_A)
_VnsPacketIPNetMask_Type=IpAddress
_VnsPacketIPNetMask_Object=MibTableColumn
vnsPacketIPNetMask=_VnsPacketIPNetMask_Object((1,3,6,1,4,1,81,19,7,1,1,4),_VnsPacketIPNetMask_Type())
vnsPacketIPNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:vnsPacketIPNetMask.setStatus(_A)
class _VnsPacketIPXnetwork_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_VnsPacketIPXnetwork_Type.__name__=_I
_VnsPacketIPXnetwork_Object=MibTableColumn
vnsPacketIPXnetwork=_VnsPacketIPXnetwork_Object((1,3,6,1,4,1,81,19,7,1,1,5),_VnsPacketIPXnetwork_Type())
vnsPacketIPXnetwork.setMaxAccess(_B)
if mibBuilder.loadTexts:vnsPacketIPXnetwork.setStatus(_A)
class _VnsPacketStationType_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('unknown',1),('client',2),('server',3),(_E,255)))
_VnsPacketStationType_Type.__name__=_C
_VnsPacketStationType_Object=MibTableColumn
vnsPacketStationType=_VnsPacketStationType_Object((1,3,6,1,4,1,81,19,7,1,1,6),_VnsPacketStationType_Type())
vnsPacketStationType.setMaxAccess(_B)
if mibBuilder.loadTexts:vnsPacketStationType.setStatus(_A)
class _VnsPacketPortGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VnsPacketPortGroupId_Type.__name__=_C
_VnsPacketPortGroupId_Object=MibTableColumn
vnsPacketPortGroupId=_VnsPacketPortGroupId_Object((1,3,6,1,4,1,81,19,7,1,1,7),_VnsPacketPortGroupId_Type())
vnsPacketPortGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:vnsPacketPortGroupId.setStatus(_A)
class _VnsPacketPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VnsPacketPortId_Type.__name__=_C
_VnsPacketPortId_Object=MibTableColumn
vnsPacketPortId=_VnsPacketPortId_Object((1,3,6,1,4,1,81,19,7,1,1,8),_VnsPacketPortId_Type())
vnsPacketPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:vnsPacketPortId.setStatus(_A)
class _VnsPacketBackbonePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('unknown',1),('backbone',2),('noBackbone',3),(_E,255)))
_VnsPacketBackbonePort_Type.__name__=_C
_VnsPacketBackbonePort_Object=MibTableColumn
vnsPacketBackbonePort=_VnsPacketBackbonePort_Object((1,3,6,1,4,1,81,19,7,1,1,9),_VnsPacketBackbonePort_Type())
vnsPacketBackbonePort.setMaxAccess(_B)
if mibBuilder.loadTexts:vnsPacketBackbonePort.setStatus(_A)
_VnsPacketExpectedVLAN_Type=Integer32
_VnsPacketExpectedVLAN_Object=MibTableColumn
vnsPacketExpectedVLAN=_VnsPacketExpectedVLAN_Object((1,3,6,1,4,1,81,19,7,1,1,10),_VnsPacketExpectedVLAN_Type())
vnsPacketExpectedVLAN.setMaxAccess(_B)
if mibBuilder.loadTexts:vnsPacketExpectedVLAN.setStatus(_A)
_VnsPacketDetectedVLAN_Type=Integer32
_VnsPacketDetectedVLAN_Object=MibTableColumn
vnsPacketDetectedVLAN=_VnsPacketDetectedVLAN_Object((1,3,6,1,4,1,81,19,7,1,1,11),_VnsPacketDetectedVLAN_Type())
vnsPacketDetectedVLAN.setMaxAccess(_B)
if mibBuilder.loadTexts:vnsPacketDetectedVLAN.setStatus(_A)
_VnsPacketBoxAgentIP_Type=IpAddress
_VnsPacketBoxAgentIP_Object=MibTableColumn
vnsPacketBoxAgentIP=_VnsPacketBoxAgentIP_Object((1,3,6,1,4,1,81,19,7,1,1,12),_VnsPacketBoxAgentIP_Type())
vnsPacketBoxAgentIP.setMaxAccess(_B)
if mibBuilder.loadTexts:vnsPacketBoxAgentIP.setStatus(_A)
_VnsPacketExpectedIfName_Type=DisplayString
_VnsPacketExpectedIfName_Object=MibTableColumn
vnsPacketExpectedIfName=_VnsPacketExpectedIfName_Object((1,3,6,1,4,1,81,19,7,1,1,13),_VnsPacketExpectedIfName_Type())
vnsPacketExpectedIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:vnsPacketExpectedIfName.setStatus(_A)
_VnsPacketDetectedIfName_Type=DisplayString
_VnsPacketDetectedIfName_Object=MibTableColumn
vnsPacketDetectedIfName=_VnsPacketDetectedIfName_Object((1,3,6,1,4,1,81,19,7,1,1,14),_VnsPacketDetectedIfName_Type())
vnsPacketDetectedIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:vnsPacketDetectedIfName.setStatus(_A)
_LntTopology_ObjectIdentity=ObjectIdentity
lntTopology=_LntTopology_ObjectIdentity((1,3,6,1,4,1,81,23))
class _TopDiscovery_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*((_J,1),('topoMessages',2),('macFind',3),('swBackboneMsgMonitor',4),(_E,255)))
_TopDiscovery_Type.__name__=_C
_TopDiscovery_Object=MibScalar
topDiscovery=_TopDiscovery_Object((1,3,6,1,4,1,81,23,1),_TopDiscovery_Type())
topDiscovery.setMaxAccess(_D)
if mibBuilder.loadTexts:topDiscovery.setStatus(_A)
class _TopDiscoveryTimeOut_Type(Integer32):defaultValue=3
_TopDiscoveryTimeOut_Type.__name__=_C
_TopDiscoveryTimeOut_Object=MibScalar
topDiscoveryTimeOut=_TopDiscoveryTimeOut_Object((1,3,6,1,4,1,81,23,2),_TopDiscoveryTimeOut_Type())
topDiscoveryTimeOut.setMaxAccess(_D)
if mibBuilder.loadTexts:topDiscoveryTimeOut.setStatus(_A)
_EthTop_ObjectIdentity=ObjectIdentity
ethTop=_EthTop_ObjectIdentity((1,3,6,1,4,1,81,23,3))
class _EthTopDiscoveryTx_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),('txInterhubMsg',2),('txBridgeMsg',3),('txAckMsg',4)))
_EthTopDiscoveryTx_Type.__name__=_C
_EthTopDiscoveryTx_Object=MibScalar
ethTopDiscoveryTx=_EthTopDiscoveryTx_Object((1,3,6,1,4,1,81,23,3,1),_EthTopDiscoveryTx_Type())
ethTopDiscoveryTx.setMaxAccess(_D)
if mibBuilder.loadTexts:ethTopDiscoveryTx.setStatus(_A)
class _EthTopClearMessageResult_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_EthTopClearMessageResult_Type.__name__=_C
_EthTopClearMessageResult_Object=MibScalar
ethTopClearMessageResult=_EthTopClearMessageResult_Object((1,3,6,1,4,1,81,23,3,2),_EthTopClearMessageResult_Type())
ethTopClearMessageResult.setMaxAccess(_D)
if mibBuilder.loadTexts:ethTopClearMessageResult.setStatus(_A)
_EthTopNumOfMessageResults_Type=Integer32
_EthTopNumOfMessageResults_Object=MibScalar
ethTopNumOfMessageResults=_EthTopNumOfMessageResults_Object((1,3,6,1,4,1,81,23,3,3),_EthTopNumOfMessageResults_Type())
ethTopNumOfMessageResults.setMaxAccess(_D)
if mibBuilder.loadTexts:ethTopNumOfMessageResults.setStatus(_A)
_EthTopMessageResultTable_Object=MibTable
ethTopMessageResultTable=_EthTopMessageResultTable_Object((1,3,6,1,4,1,81,23,3,4))
if mibBuilder.loadTexts:ethTopMessageResultTable.setStatus(_A)
_EthTopMessageResultEntry_Object=MibTableRow
ethTopMessageResultEntry=_EthTopMessageResultEntry_Object((1,3,6,1,4,1,81,23,3,4,1))
ethTopMessageResultEntry.setIndexNames((0,_F,_A5))
if mibBuilder.loadTexts:ethTopMessageResultEntry.setStatus(_A)
_EthTopMessageResultId_Type=Integer32
_EthTopMessageResultId_Object=MibTableColumn
ethTopMessageResultId=_EthTopMessageResultId_Object((1,3,6,1,4,1,81,23,3,4,1,1),_EthTopMessageResultId_Type())
ethTopMessageResultId.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTopMessageResultId.setStatus(_A)
class _EthTopMessageResult_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,440))
_EthTopMessageResult_Type.__name__=_I
_EthTopMessageResult_Object=MibTableColumn
ethTopMessageResult=_EthTopMessageResult_Object((1,3,6,1,4,1,81,23,3,4,1,2),_EthTopMessageResult_Type())
ethTopMessageResult.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTopMessageResult.setStatus(_A)
class _EthTopMACFindList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,36))
_EthTopMACFindList_Type.__name__=_I
_EthTopMACFindList_Object=MibScalar
ethTopMACFindList=_EthTopMACFindList_Object((1,3,6,1,4,1,81,23,3,5),_EthTopMACFindList_Type())
ethTopMACFindList.setMaxAccess(_D)
if mibBuilder.loadTexts:ethTopMACFindList.setStatus(_A)
_EthTopMACFindResultTable_Object=MibTable
ethTopMACFindResultTable=_EthTopMACFindResultTable_Object((1,3,6,1,4,1,81,23,3,6))
if mibBuilder.loadTexts:ethTopMACFindResultTable.setStatus(_A)
_EthTopMACFindResultEntry_Object=MibTableRow
ethTopMACFindResultEntry=_EthTopMACFindResultEntry_Object((1,3,6,1,4,1,81,23,3,6,1))
ethTopMACFindResultEntry.setIndexNames((0,_F,_A6))
if mibBuilder.loadTexts:ethTopMACFindResultEntry.setStatus(_A)
_EthTopMACFindBus_Type=Integer32
_EthTopMACFindBus_Object=MibTableColumn
ethTopMACFindBus=_EthTopMACFindBus_Object((1,3,6,1,4,1,81,23,3,6,1,1),_EthTopMACFindBus_Type())
ethTopMACFindBus.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTopMACFindBus.setStatus(_A)
class _EthTopMACFindResult_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_EthTopMACFindResult_Type.__name__=_I
_EthTopMACFindResult_Object=MibTableColumn
ethTopMACFindResult=_EthTopMACFindResult_Object((1,3,6,1,4,1,81,23,3,6,1,2),_EthTopMACFindResult_Type())
ethTopMACFindResult.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTopMACFindResult.setStatus(_A)
_EthTopLSATable_Object=MibTable
ethTopLSATable=_EthTopLSATable_Object((1,3,6,1,4,1,81,23,3,7))
if mibBuilder.loadTexts:ethTopLSATable.setStatus(_A)
_EthTopLSAEntry_Object=MibTableRow
ethTopLSAEntry=_EthTopLSAEntry_Object((1,3,6,1,4,1,81,23,3,7,1))
ethTopLSAEntry.setIndexNames((0,_F,_A7))
if mibBuilder.loadTexts:ethTopLSAEntry.setStatus(_A)
_EthTopLSAId_Type=Integer32
_EthTopLSAId_Object=MibTableColumn
ethTopLSAId=_EthTopLSAId_Object((1,3,6,1,4,1,81,23,3,7,1,1),_EthTopLSAId_Type())
ethTopLSAId.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTopLSAId.setStatus(_A)
class _EthTopLSA_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(384,384));fixedLength=384
_EthTopLSA_Type.__name__=_I
_EthTopLSA_Object=MibTableColumn
ethTopLSA=_EthTopLSA_Object((1,3,6,1,4,1,81,23,3,7,1,2),_EthTopLSA_Type())
ethTopLSA.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTopLSA.setStatus(_A)
_EthTopAddressTable_Object=MibTable
ethTopAddressTable=_EthTopAddressTable_Object((1,3,6,1,4,1,81,23,3,8))
if mibBuilder.loadTexts:ethTopAddressTable.setStatus(_A)
_EthTopAddressEntry_Object=MibTableRow
ethTopAddressEntry=_EthTopAddressEntry_Object((1,3,6,1,4,1,81,23,3,8,1))
ethTopAddressEntry.setIndexNames((0,_F,_A8))
if mibBuilder.loadTexts:ethTopAddressEntry.setStatus(_A)
_EthTopBus_Type=Integer32
_EthTopBus_Object=MibTableColumn
ethTopBus=_EthTopBus_Object((1,3,6,1,4,1,81,23,3,8,1,1),_EthTopBus_Type())
ethTopBus.setMaxAccess(_B)
if mibBuilder.loadTexts:ethTopBus.setStatus(_A)
class _EthTopAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_EthTopAddress_Type.__name__=_I
_EthTopAddress_Object=MibTableColumn
ethTopAddress=_EthTopAddress_Object((1,3,6,1,4,1,81,23,3,8,1,2),_EthTopAddress_Type())
ethTopAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ethTopAddress.setStatus(_A)
class _EthTopHSBMonitor_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_J,1),('startMonitor',2),(_E,255)))
_EthTopHSBMonitor_Type.__name__=_C
_EthTopHSBMonitor_Object=MibScalar
ethTopHSBMonitor=_EthTopHSBMonitor_Object((1,3,6,1,4,1,81,23,3,9),_EthTopHSBMonitor_Type())
ethTopHSBMonitor.setMaxAccess(_D)
if mibBuilder.loadTexts:ethTopHSBMonitor.setStatus(_A)
_Smon_ObjectIdentity=ObjectIdentity
smon=_Smon_ObjectIdentity((1,3,6,1,4,1,81,30))
_Alarms_ObjectIdentity=ObjectIdentity
alarms=_Alarms_ObjectIdentity((1,3,6,1,4,1,81,30,1))
_AlarmMonitorStatusTable_Object=MibTable
alarmMonitorStatusTable=_AlarmMonitorStatusTable_Object((1,3,6,1,4,1,81,30,1,1))
if mibBuilder.loadTexts:alarmMonitorStatusTable.setStatus(_A)
_AlarmMonitorStatusEntry_Object=MibTableRow
alarmMonitorStatusEntry=_AlarmMonitorStatusEntry_Object((1,3,6,1,4,1,81,30,1,1,1))
alarmMonitorStatusEntry.setIndexNames((0,_F,_A9))
if mibBuilder.loadTexts:alarmMonitorStatusEntry.setStatus(_A)
class _AlarmMonitorStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AlarmMonitorStatusIndex_Type.__name__=_C
_AlarmMonitorStatusIndex_Object=MibTableColumn
alarmMonitorStatusIndex=_AlarmMonitorStatusIndex_Object((1,3,6,1,4,1,81,30,1,1,1,1),_AlarmMonitorStatusIndex_Type())
alarmMonitorStatusIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmMonitorStatusIndex.setStatus(_A)
class _AlarmMonitorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),('alarmState',2)))
_AlarmMonitorStatus_Type.__name__=_C
_AlarmMonitorStatus_Object=MibTableColumn
alarmMonitorStatus=_AlarmMonitorStatus_Object((1,3,6,1,4,1,81,30,1,1,1,2),_AlarmMonitorStatus_Type())
alarmMonitorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmMonitorStatus.setStatus(_A)
class _AlarmUtilitiesCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_J,1),('clearAll',2),(_E,255)))
_AlarmUtilitiesCommand_Type.__name__=_C
_AlarmUtilitiesCommand_Object=MibScalar
alarmUtilitiesCommand=_AlarmUtilitiesCommand_Object((1,3,6,1,4,1,81,30,1,2),_AlarmUtilitiesCommand_Type())
alarmUtilitiesCommand.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmUtilitiesCommand.setStatus(_A)
_PortHistory_ObjectIdentity=ObjectIdentity
portHistory=_PortHistory_ObjectIdentity((1,3,6,1,4,1,81,30,3))
_PortHistoryExtendedControlTable_Object=MibTable
portHistoryExtendedControlTable=_PortHistoryExtendedControlTable_Object((1,3,6,1,4,1,81,30,3,1))
if mibBuilder.loadTexts:portHistoryExtendedControlTable.setStatus(_A)
_PortHistoryExtendedControlEntry_Object=MibTableRow
portHistoryExtendedControlEntry=_PortHistoryExtendedControlEntry_Object((1,3,6,1,4,1,81,30,3,1,1))
portHistoryExtendedControlEntry.setIndexNames((0,_U,_V))
if mibBuilder.loadTexts:portHistoryExtendedControlEntry.setStatus(_A)
_PortHistoryExtendedControlCreateTime_Type=TimeTicks
_PortHistoryExtendedControlCreateTime_Object=MibTableColumn
portHistoryExtendedControlCreateTime=_PortHistoryExtendedControlCreateTime_Object((1,3,6,1,4,1,81,30,3,1,1,1),_PortHistoryExtendedControlCreateTime_Type())
portHistoryExtendedControlCreateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:portHistoryExtendedControlCreateTime.setStatus(_A)
_PortHistoryExtendedControlLastBucketIndex_Type=Integer32
_PortHistoryExtendedControlLastBucketIndex_Object=MibTableColumn
portHistoryExtendedControlLastBucketIndex=_PortHistoryExtendedControlLastBucketIndex_Object((1,3,6,1,4,1,81,30,3,1,1,2),_PortHistoryExtendedControlLastBucketIndex_Type())
portHistoryExtendedControlLastBucketIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:portHistoryExtendedControlLastBucketIndex.setStatus(_A)
class _PortHistoryExtendedControlNumberOfBuckets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PortHistoryExtendedControlNumberOfBuckets_Type.__name__=_C
_PortHistoryExtendedControlNumberOfBuckets_Object=MibTableColumn
portHistoryExtendedControlNumberOfBuckets=_PortHistoryExtendedControlNumberOfBuckets_Object((1,3,6,1,4,1,81,30,3,1,1,3),_PortHistoryExtendedControlNumberOfBuckets_Type())
portHistoryExtendedControlNumberOfBuckets.setMaxAccess(_B)
if mibBuilder.loadTexts:portHistoryExtendedControlNumberOfBuckets.setStatus(_A)
_PortHistoryExtendedControlName_Type=DisplayString
_PortHistoryExtendedControlName_Object=MibTableColumn
portHistoryExtendedControlName=_PortHistoryExtendedControlName_Object((1,3,6,1,4,1,81,30,3,1,1,4),_PortHistoryExtendedControlName_Type())
portHistoryExtendedControlName.setMaxAccess(_D)
if mibBuilder.loadTexts:portHistoryExtendedControlName.setStatus(_A)
_LsPortHistoryTable_Object=MibTable
lsPortHistoryTable=_LsPortHistoryTable_Object((1,3,6,1,4,1,81,30,3,2))
if mibBuilder.loadTexts:lsPortHistoryTable.setStatus(_A)
_LsPortHistoryEntry_Object=MibTableRow
lsPortHistoryEntry=_LsPortHistoryEntry_Object((1,3,6,1,4,1,81,30,3,2,1))
lsPortHistoryEntry.setIndexNames((0,_F,_AA),(0,_F,_AB),(0,_F,_R))
if mibBuilder.loadTexts:lsPortHistoryEntry.setStatus(_A)
class _LsPortHistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_LsPortHistoryIndex_Type.__name__=_C
_LsPortHistoryIndex_Object=MibTableColumn
lsPortHistoryIndex=_LsPortHistoryIndex_Object((1,3,6,1,4,1,81,30,3,2,1,1),_LsPortHistoryIndex_Type())
lsPortHistoryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortHistoryIndex.setStatus(_A)
class _LsPortHistorySampleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LsPortHistorySampleIndex_Type.__name__=_C
_LsPortHistorySampleIndex_Object=MibTableColumn
lsPortHistorySampleIndex=_LsPortHistorySampleIndex_Object((1,3,6,1,4,1,81,30,3,2,1,2),_LsPortHistorySampleIndex_Type())
lsPortHistorySampleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortHistorySampleIndex.setStatus(_A)
_LsPortHistoryIntervalTime_Type=TimeTicks
_LsPortHistoryIntervalTime_Object=MibTableColumn
lsPortHistoryIntervalTime=_LsPortHistoryIntervalTime_Object((1,3,6,1,4,1,81,30,3,2,1,3),_LsPortHistoryIntervalTime_Type())
lsPortHistoryIntervalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortHistoryIntervalTime.setStatus(_A)
_LsPortHistoryBoxConfiguration_Type=OctetString
_LsPortHistoryBoxConfiguration_Object=MibTableColumn
lsPortHistoryBoxConfiguration=_LsPortHistoryBoxConfiguration_Object((1,3,6,1,4,1,81,30,3,2,1,4),_LsPortHistoryBoxConfiguration_Type())
lsPortHistoryBoxConfiguration.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortHistoryBoxConfiguration.setStatus(_A)
_LsPortHistoryPkts_Type=Counter32
_LsPortHistoryPkts_Object=MibTableColumn
lsPortHistoryPkts=_LsPortHistoryPkts_Object((1,3,6,1,4,1,81,30,3,2,1,5),_LsPortHistoryPkts_Type())
lsPortHistoryPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortHistoryPkts.setStatus(_A)
_LsPortHistoryCollisions_Type=Counter32
_LsPortHistoryCollisions_Object=MibTableColumn
lsPortHistoryCollisions=_LsPortHistoryCollisions_Object((1,3,6,1,4,1,81,30,3,2,1,6),_LsPortHistoryCollisions_Type())
lsPortHistoryCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortHistoryCollisions.setStatus(_A)
_LsPortHistoryTotalErrors_Type=Counter32
_LsPortHistoryTotalErrors_Object=MibTableColumn
lsPortHistoryTotalErrors=_LsPortHistoryTotalErrors_Object((1,3,6,1,4,1,81,30,3,2,1,7),_LsPortHistoryTotalErrors_Type())
lsPortHistoryTotalErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:lsPortHistoryTotalErrors.setStatus(_A)
_ScPortHistoryTable_Object=MibTable
scPortHistoryTable=_ScPortHistoryTable_Object((1,3,6,1,4,1,81,30,3,3))
if mibBuilder.loadTexts:scPortHistoryTable.setStatus(_A)
_ScPortHistoryEntry_Object=MibTableRow
scPortHistoryEntry=_ScPortHistoryEntry_Object((1,3,6,1,4,1,81,30,3,3,1))
scPortHistoryEntry.setIndexNames((0,_F,_AC),(0,_F,_AD),(0,_S,_T))
if mibBuilder.loadTexts:scPortHistoryEntry.setStatus(_A)
class _ScPortHistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ScPortHistoryIndex_Type.__name__=_C
_ScPortHistoryIndex_Object=MibTableColumn
scPortHistoryIndex=_ScPortHistoryIndex_Object((1,3,6,1,4,1,81,30,3,3,1,1),_ScPortHistoryIndex_Type())
scPortHistoryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:scPortHistoryIndex.setStatus(_A)
class _ScPortHistorySampleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ScPortHistorySampleIndex_Type.__name__=_C
_ScPortHistorySampleIndex_Object=MibTableColumn
scPortHistorySampleIndex=_ScPortHistorySampleIndex_Object((1,3,6,1,4,1,81,30,3,3,1,2),_ScPortHistorySampleIndex_Type())
scPortHistorySampleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:scPortHistorySampleIndex.setStatus(_A)
_ScPortHistoryIntervalTime_Type=TimeTicks
_ScPortHistoryIntervalTime_Object=MibTableColumn
scPortHistoryIntervalTime=_ScPortHistoryIntervalTime_Object((1,3,6,1,4,1,81,30,3,3,1,3),_ScPortHistoryIntervalTime_Type())
scPortHistoryIntervalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:scPortHistoryIntervalTime.setStatus(_A)
_ScPortHistoryBoxConfiguration_Type=OctetString
_ScPortHistoryBoxConfiguration_Object=MibTableColumn
scPortHistoryBoxConfiguration=_ScPortHistoryBoxConfiguration_Object((1,3,6,1,4,1,81,30,3,3,1,4),_ScPortHistoryBoxConfiguration_Type())
scPortHistoryBoxConfiguration.setMaxAccess(_B)
if mibBuilder.loadTexts:scPortHistoryBoxConfiguration.setStatus(_A)
_ScPortHistoryGoodPktsRec_Type=Counter32
_ScPortHistoryGoodPktsRec_Object=MibTableColumn
scPortHistoryGoodPktsRec=_ScPortHistoryGoodPktsRec_Object((1,3,6,1,4,1,81,30,3,3,1,5),_ScPortHistoryGoodPktsRec_Type())
scPortHistoryGoodPktsRec.setMaxAccess(_B)
if mibBuilder.loadTexts:scPortHistoryGoodPktsRec.setStatus(_A)
_ScPortHistoryGoodNonUnicastPktsRec_Type=Counter32
_ScPortHistoryGoodNonUnicastPktsRec_Object=MibTableColumn
scPortHistoryGoodNonUnicastPktsRec=_ScPortHistoryGoodNonUnicastPktsRec_Object((1,3,6,1,4,1,81,30,3,3,1,6),_ScPortHistoryGoodNonUnicastPktsRec_Type())
scPortHistoryGoodNonUnicastPktsRec.setMaxAccess(_B)
if mibBuilder.loadTexts:scPortHistoryGoodNonUnicastPktsRec.setStatus(_A)
_ScPortHistoryCollisions_Type=Counter32
_ScPortHistoryCollisions_Object=MibTableColumn
scPortHistoryCollisions=_ScPortHistoryCollisions_Object((1,3,6,1,4,1,81,30,3,3,1,7),_ScPortHistoryCollisions_Type())
scPortHistoryCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:scPortHistoryCollisions.setStatus(_A)
_ScPortHistoryBadPkts_Type=Counter32
_ScPortHistoryBadPkts_Object=MibTableColumn
scPortHistoryBadPkts=_ScPortHistoryBadPkts_Object((1,3,6,1,4,1,81,30,3,3,1,8),_ScPortHistoryBadPkts_Type())
scPortHistoryBadPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:scPortHistoryBadPkts.setStatus(_A)
_ScPortHistoryGoodPktsSent_Type=Counter32
_ScPortHistoryGoodPktsSent_Object=MibTableColumn
scPortHistoryGoodPktsSent=_ScPortHistoryGoodPktsSent_Object((1,3,6,1,4,1,81,30,3,3,1,9),_ScPortHistoryGoodPktsSent_Type())
scPortHistoryGoodPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:scPortHistoryGoodPktsSent.setStatus(_A)
class _PortHistoryMemoryAvailability_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('standard',1),('limited1',2),('limited2',3),(_E,255)))
_PortHistoryMemoryAvailability_Type.__name__=_C
_PortHistoryMemoryAvailability_Object=MibScalar
portHistoryMemoryAvailability=_PortHistoryMemoryAvailability_Object((1,3,6,1,4,1,81,30,3,4),_PortHistoryMemoryAvailability_Type())
portHistoryMemoryAvailability.setMaxAccess(_B)
if mibBuilder.loadTexts:portHistoryMemoryAvailability.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'lntLanSwitch':lntLanSwitch,'lse':lse,'lseGroupTable':lseGroupTable,'lseGroupEntry':lseGroupEntry,_W:lseGroupId,'lseGroupFastOpen':lseGroupFastOpen,'lseGroup10MSqlt':lseGroup10MSqlt,'lseGroupSmartSqlt':lseGroupSmartSqlt,'lseGroupCParameter':lseGroupCParameter,'lseGroupIPGJamLength':lseGroupIPGJamLength,'lseGroupJamLength':lseGroupJamLength,'lseGroupDataBlinderLength':lseGroupDataBlinderLength,'lseGroupIPGDataLength':lseGroupIPGDataLength,'lseGroupActiveMonitor':lseGroupActiveMonitor,'lseGroupBackbone12':lseGroupBackbone12,'lseGroupSetDefaults':lseGroupSetDefaults,'lseGroupBackbone34':lseGroupBackbone34,'lseGroupBackboneRedun12':lseGroupBackboneRedun12,'lseGroupBackoffFromJam':lseGroupBackoffFromJam,'lseGroupCAMClear':lseGroupCAMClear,'lseGroupJamPrevent':lseGroupJamPrevent,'lseGroupNormOpCl':lseGroupNormOpCl,'lseGroupNormOpDelay':lseGroupNormOpDelay,'lseGroupAutoPartitionEnable':lseGroupAutoPartitionEnable,'lseGroupWorkState':lseGroupWorkState,'lseGroupBITResult':lseGroupBITResult,'lseGroupAssignSlots':lseGroupAssignSlots,'lseGroupHSBMonStatus':lseGroupHSBMonStatus,'lseGroupEnableHSBReset':lseGroupEnableHSBReset,'lseIntPort':lseIntPort,'lseIntPortTable':lseIntPortTable,'lseIntPortEntry':lseIntPortEntry,_X:lseIntPortGroupId,_Y:lseIntPortId,'lseIntPortIOMode':lseIntPortIOMode,'lseIntPortResetSwitchCAM':lseIntPortResetSwitchCAM,'lseIntPortVideoPacket':lseIntPortVideoPacket,'lseIntPortPriorityStateMachine':lseIntPortPriorityStateMachine,'lseIntPortActiveBroadcastPriority':lseIntPortActiveBroadcastPriority,'lseIntPortPriorityLevel':lseIntPortPriorityLevel,'lseIntPortSuperPriorityEnable':lseIntPortSuperPriorityEnable,'lseIntPortRoutingMode':lseIntPortRoutingMode,'lseIntPortGlobal':lseIntPortGlobal,'lseIntPortLearnIOCAM':lseIntPortLearnIOCAM,'lseIntPortSecurity':lseIntPortSecurity,'lseIntPortIgnoreBusy':lseIntPortIgnoreBusy,'lseIntPortRetryPriorityLevel1':lseIntPortRetryPriorityLevel1,'lseIntPortRetryPriorityLevel2':lseIntPortRetryPriorityLevel2,'lseIntPortRetryPriorityLevel3':lseIntPortRetryPriorityLevel3,'lseIntPortIgnoreProtocolType':lseIntPortIgnoreProtocolType,'lseIntPortCompanyMAC':lseIntPortCompanyMAC,'lseIntPortTxSafetyZone':lseIntPortTxSafetyZone,'lseIntPortRxSafetyZone':lseIntPortRxSafetyZone,'lseIntPortTxBurstLength':lseIntPortTxBurstLength,'lseIntPortSecurityIntruder':lseIntPortSecurityIntruder,'lseIntPortJabber':lseIntPortJabber,'lseIntPortCAM':lseIntPortCAM,'lseIntPortVideoStateMachine':lseIntPortVideoStateMachine,'lseIntPortTransmitWeight':lseIntPortTransmitWeight,'lseIntPortSuperPriority':lseIntPortSuperPriority,'lseIntPortAlignment':lseIntPortAlignment,'lseIntPortRxReject':lseIntPortRxReject,'lseIntPortTxReject':lseIntPortTxReject,'lseIntPortRxEmpty0':lseIntPortRxEmpty0,'lseIntPortRxEmpty1':lseIntPortRxEmpty1,'lseIntPortRxEmpty2':lseIntPortRxEmpty2,'lseIntPortSuperNetNumber':lseIntPortSuperNetNumber,'lseIntPortGlobalSuperNet':lseIntPortGlobalSuperNet,'lseIntPortMACAddress':lseIntPortMACAddress,'lseIntPortIgnoreRoutingMode':lseIntPortIgnoreRoutingMode,'lseIntPortCAMLastChange':lseIntPortCAMLastChange,'lseIntPortCopiedPort':lseIntPortCopiedPort,'lseIntPortBroadcastBehavior':lseIntPortBroadcastBehavior,'lseIntPortFilteringMethod':lseIntPortFilteringMethod,'lseIntPortSetFilter':lseIntPortSetFilter,'lseIntPortRemoveFilter':lseIntPortRemoveFilter,'lseIntPortClearFilter':lseIntPortClearFilter,'lseIntPortMonitorMissedEvents':lseIntPortMonitorMissedEvents,'lseIntPortMACAdd':lseIntPortMACAdd,'lseIntPortMACAddTable':lseIntPortMACAddTable,'lseIntPortMACAddEntry':lseIntPortMACAddEntry,_b:lseIntPortMACAddGroupId,_Q:lseIntPortMACAddPortId,_c:lseIntPortMACAddLAId,'lseIntPortMACAddList':lseIntPortMACAddList,'lseIntPortFilter':lseIntPortFilter,'lseIntPortFilterTable':lseIntPortFilterTable,'lseIntPortFilterEntry':lseIntPortFilterEntry,_d:lseIntPortFilterGroupId,_e:lseIntPortFilterPortId,_f:lseIntPortFilterLAId,'lseIntPortFilterList':lseIntPortFilterList,'lseIntPortMACVlanTable':lseIntPortMACVlanTable,'lseIntPortMACVlanEntry':lseIntPortMACVlanEntry,_g:lseIntPortMACVlanGroupId,'lseIntPortMACVlanPortId':lseIntPortMACVlanPortId,_h:lseIntPortMACVlanVlan,_i:lseIntPortMACVlanLAId,'lseIntPortMACVlanMAClist':lseIntPortMACVlanMAClist,'lsePort':lsePort,'lsePortTable':lsePortTable,'lsePortEntry':lsePortEntry,_j:lsePortGroupId,_k:lsePortId,'lsePortPolarity':lsePortPolarity,'lsePortBackboneStatus':lsePortBackboneStatus,'lhs':lhs,'lhsGroupTable':lhsGroupTable,'lhsGroupEntry':lhsGroupEntry,_l:lhsGroupId,'lhsGroupMainSWVersion':lhsGroupMainSWVersion,'lhsGroupProtocolType':lhsGroupProtocolType,'lhsPortTable':lhsPortTable,'lhsPortEntry':lhsPortEntry,_m:lhsPortGroupId,_n:lhsPortId,'lhsTxUCast':lhsTxUCast,'lhsTxBCast':lhsTxBCast,'lhsTxMCast':lhsTxMCast,'lhsTxUrunErr':lhsTxUrunErr,'lhsTxParErr':lhsTxParErr,'lhsRxUCast':lhsRxUCast,'lhsRxBCast':lhsRxBCast,'lhsRxMCast':lhsRxMCast,'lhsRxOrunErr':lhsRxOrunErr,'lhsRxParErr':lhsRxParErr,'lhsRxRscErr':lhsRxRscErr,'lhsRxBadTypeErr':lhsRxBadTypeErr,'lhsLinkStatus':lhsLinkStatus,'lsMonitor':lsMonitor,'lsMonitorResourceAllocation':lsMonitorResourceAllocation,'lsBusStats':lsBusStats,'lsBusStatsDropEvents':lsBusStatsDropEvents,'lsBusStatsPkts':lsBusStatsPkts,'lsBusStatsOctets':lsBusStatsOctets,'lsBusStatsUtilization':lsBusStatsUtilization,'lsBusStatsEthBroadcastPkts':lsBusStatsEthBroadcastPkts,'lsBusStatsMulticastPkts':lsBusStatsMulticastPkts,'lsBusStatsGoodEthPkts':lsBusStatsGoodEthPkts,'lsBusStatsGoodEthOctets':lsBusStatsGoodEthOctets,'lsBusStatsBadEthPkts':lsBusStatsBadEthPkts,'lsBusStatsBadEthOctets':lsBusStatsBadEthOctets,'lsBusStatsNonEthPkts':lsBusStatsNonEthPkts,'lsBusStatsNonEthOctets':lsBusStatsNonEthOctets,'lsBusStatsPriorityTable':lsBusStatsPriorityTable,'lsBusStatsPriorityEntry':lsBusStatsPriorityEntry,_o:lsBusStatsPriorityIndex,'lsBusStatsPriorityPkts':lsBusStatsPriorityPkts,'lsBusStatsPriorityOctets':lsBusStatsPriorityOctets,'lsBusStatsVirtualNetList':lsBusStatsVirtualNetList,'lsBusStatsVirtualNetTable':lsBusStatsVirtualNetTable,'lsBusStatsVirtualNetEntry':lsBusStatsVirtualNetEntry,_p:lsBusStatsVirtualNet,'lsBusStatsVirtualNetPackets':lsBusStatsVirtualNetPackets,'lsBusStatsVirtualNetOctets':lsBusStatsVirtualNetOctets,'lsPortStats':lsPortStats,'lsPortControlTable':lsPortControlTable,'lsPortControlEntry':lsPortControlEntry,_q:lsPortControlIndex,'lsPortControlDataSource':lsPortControlDataSource,'lsPortControlTableSize':lsPortControlTableSize,'lsPortControlLastDeleteTime':lsPortControlLastDeleteTime,'lsPortControlOwner':lsPortControlOwner,'lsPortControlStatus':lsPortControlStatus,'lsPortFilterTable':lsPortFilterTable,'lsPortFilterEntry':lsPortFilterEntry,_r:lsPortFilter,'lsPortFilterStatus':lsPortFilterStatus,'lsPortFilterTableClear':lsPortFilterTableClear,'lsPortTable':lsPortTable,'lsPortEntry':lsPortEntry,_R:lsPortNumber,'lsPortInPkts':lsPortInPkts,'lsPortInFCSErrors':lsPortInFCSErrors,'lsPortInTooLongPkts':lsPortInTooLongPkts,'lsPortInOctets':lsPortInOctets,'lsPortInTotalErrors':lsPortInTotalErrors,'lsPortInCollisions':lsPortInCollisions,'lsPortExtendedReportingList':lsPortExtendedReportingList,'lsPortExtendedStatsTable':lsPortExtendedStatsTable,'lsPortExtendedStatsEntry':lsPortExtendedStatsEntry,_s:lsPortExtendedStatsNumber,'lsPortCreationOrder':lsPortCreationOrder,'lsPortIndex':lsPortIndex,'lsPortOutPkts':lsPortOutPkts,'lsPortInBroadcastPkts':lsPortInBroadcastPkts,'lsPortInMulticastPkts':lsPortInMulticastPkts,'lsHostFilterTable':lsHostFilterTable,'lsHostFilterEntry':lsHostFilterEntry,_t:lsHostFilterAddress,'lsHostFilterStatus':lsHostFilterStatus,'lsHostFilterTableClear':lsHostFilterTableClear,'lsHostPortFilterTable':lsHostPortFilterTable,'lsHostPortFilterEntry':lsHostPortFilterEntry,_u:lsHostPortFilter,'lsHostPortFilterStatus':lsHostPortFilterStatus,'lsHostPortFilterTableClear':lsHostPortFilterTableClear,'lsMatrixFilterTable':lsMatrixFilterTable,'lsMatrixFilterEntry':lsMatrixFilterEntry,_v:lsMatrixFilterAddress,'lsMatrixFilterStatus':lsMatrixFilterStatus,'lsMatrixFilterTableClear':lsMatrixFilterTableClear,'lsHostTimePortCorrTable':lsHostTimePortCorrTable,'lsHostTimePortCorrEntry':lsHostTimePortCorrEntry,'hostTimeAddress':hostTimeAddress,_x:hostTimeCreationOrder,_w:hostTimeIndex,'hostTimePortConnection':hostTimePortConnection,'lsHistoryTable':lsHistoryTable,'lsHistoryEntry':lsHistoryEntry,_y:lsHistoryIndex,_z:lsHistorySampleIndex,'lsHistoryIntervalTime':lsHistoryIntervalTime,'lsHistoryStatsDropEvents':lsHistoryStatsDropEvents,'lsHistoryStatsPkts':lsHistoryStatsPkts,'lsHistoryStatsOctets':lsHistoryStatsOctets,'lsHistoryStatsEthBroadcastPkts':lsHistoryStatsEthBroadcastPkts,'lsHistoryStatsEthMulticastPkts':lsHistoryStatsEthMulticastPkts,'lsHistoryStatsGoodEthPkts':lsHistoryStatsGoodEthPkts,'lsHistoryStatsGoodEthOctets':lsHistoryStatsGoodEthOctets,'lsHistoryStatsBadEthPkts':lsHistoryStatsBadEthPkts,'lsHistoryStatsBadEthOctets':lsHistoryStatsBadEthOctets,'lsHistoryStatsNonEthPkts':lsHistoryStatsNonEthPkts,'lsHistoryStatsNonEthOctets':lsHistoryStatsNonEthOctets,'lsHistoryStatsPriority1Pkts':lsHistoryStatsPriority1Pkts,'lsHistoryStatsPriority1Octets':lsHistoryStatsPriority1Octets,'lsHistoryStatsPriority2Pkts':lsHistoryStatsPriority2Pkts,'lsHistoryStatsPriority2Octets':lsHistoryStatsPriority2Octets,'lsHistoryStatsPriority3Pkts':lsHistoryStatsPriority3Pkts,'lsHistoryStatsPriority3Octets':lsHistoryStatsPriority3Octets,'lsHistoryStatsPriority4Pkts':lsHistoryStatsPriority4Pkts,'lsHistoryStatsPriority4Octets':lsHistoryStatsPriority4Octets,'lsHistoryBusUtilization':lsHistoryBusUtilization,'lst':lst,'lstIntPort':lstIntPort,'lstIntPortTable':lstIntPortTable,'lstIntPortEntry':lstIntPortEntry,_A0:lstIntPortGroupId,_A1:lstIntPortId,'lstIntPortSidebandMode':lstIntPortSidebandMode,'lstIntPortTotalOctets':lstIntPortTotalOctets,'lstIntPortTotalTraffic':lstIntPortTotalTraffic,'lstIntPortLocalOctets':lstIntPortLocalOctets,'lstIntPortLocalTraffic':lstIntPortLocalTraffic,'lstIntPortInOctets':lstIntPortInOctets,'lstIntPortInTraffic':lstIntPortInTraffic,'lstIntPortOutOctets':lstIntPortOutOctets,'lstIntPortOutTraffic':lstIntPortOutTraffic,'lstIntPortTotalFrames':lstIntPortTotalFrames,'lstIntPortLostFrames':lstIntPortLostFrames,'lstIntPortClaimFrames':lstIntPortClaimFrames,'lstIntPortPurgeFrames':lstIntPortPurgeFrames,'lstIntPortNormallyCloseOpen':lstIntPortNormallyCloseOpen,'lstIntPortSlicingEnable':lstIntPortSlicingEnable,'lstIntPortSliceLength':lstIntPortSliceLength,'lstIntPortUNAddr':lstIntPortUNAddr,'lstIntPortMACAddress':lstIntPortMACAddress,'lstIntPortSMPTransmitEnable':lstIntPortSMPTransmitEnable,'lstIntPortIPGLength':lstIntPortIPGLength,'lstIntPortBPDummyWindow':lstIntPortBPDummyWindow,'lstIntPortBPTokenWindow':lstIntPortBPTokenWindow,'lstIntPortTransmitWindow':lstIntPortTransmitWindow,'lstIntPortBlockingPriority':lstIntPortBlockingPriority,'lstIntPortNormalPriority':lstIntPortNormalPriority,'lstIntPortDummyMV':lstIntPortDummyMV,'lstIntPortTxConsecutiveBusiesThresh':lstIntPortTxConsecutiveBusiesThresh,'lstIntPortTxBufFullThresh':lstIntPortTxBufFullThresh,'lstIntPortRxEmpty0':lstIntPortRxEmpty0,'lstIntPortRxEmpty1':lstIntPortRxEmpty1,'lstIntPortRxEmpty2':lstIntPortRxEmpty2,'lstIntPortRxFull':lstIntPortRxFull,'lstIntPortBPEnable':lstIntPortBPEnable,'lstIntPortRouteSideband':lstIntPortRouteSideband,'lseWANTable':lseWANTable,'lseWANEntry':lseWANEntry,_A2:lseWANGroupId,_A3:lseWANPortId,'lseWANConnection':lseWANConnection,'lsVNChange':lsVNChange,'lsVNChangeMACAddress':lsVNChangeMACAddress,'lsVNChangeDetected':lsVNChangeDetected,'lsVNChangeExpected':lsVNChangeExpected,'lsVNChangeGroup':lsVNChangeGroup,'lsVNChangePort':lsVNChangePort,'vnsPacket':vnsPacket,'vnsPacketTable':vnsPacketTable,'vnsPacketEntry':vnsPacketEntry,_A4:vnsPacketMACAddress,'vnsPacketProtocolTypeMask':vnsPacketProtocolTypeMask,'vnsPacketIPAddress':vnsPacketIPAddress,'vnsPacketIPNetMask':vnsPacketIPNetMask,'vnsPacketIPXnetwork':vnsPacketIPXnetwork,'vnsPacketStationType':vnsPacketStationType,'vnsPacketPortGroupId':vnsPacketPortGroupId,'vnsPacketPortId':vnsPacketPortId,'vnsPacketBackbonePort':vnsPacketBackbonePort,'vnsPacketExpectedVLAN':vnsPacketExpectedVLAN,'vnsPacketDetectedVLAN':vnsPacketDetectedVLAN,'vnsPacketBoxAgentIP':vnsPacketBoxAgentIP,'vnsPacketExpectedIfName':vnsPacketExpectedIfName,'vnsPacketDetectedIfName':vnsPacketDetectedIfName,'lntTopology':lntTopology,'topDiscovery':topDiscovery,'topDiscoveryTimeOut':topDiscoveryTimeOut,'ethTop':ethTop,'ethTopDiscoveryTx':ethTopDiscoveryTx,'ethTopClearMessageResult':ethTopClearMessageResult,'ethTopNumOfMessageResults':ethTopNumOfMessageResults,'ethTopMessageResultTable':ethTopMessageResultTable,'ethTopMessageResultEntry':ethTopMessageResultEntry,_A5:ethTopMessageResultId,'ethTopMessageResult':ethTopMessageResult,'ethTopMACFindList':ethTopMACFindList,'ethTopMACFindResultTable':ethTopMACFindResultTable,'ethTopMACFindResultEntry':ethTopMACFindResultEntry,_A6:ethTopMACFindBus,'ethTopMACFindResult':ethTopMACFindResult,'ethTopLSATable':ethTopLSATable,'ethTopLSAEntry':ethTopLSAEntry,_A7:ethTopLSAId,'ethTopLSA':ethTopLSA,'ethTopAddressTable':ethTopAddressTable,'ethTopAddressEntry':ethTopAddressEntry,_A8:ethTopBus,'ethTopAddress':ethTopAddress,'ethTopHSBMonitor':ethTopHSBMonitor,'smon':smon,'alarms':alarms,'alarmMonitorStatusTable':alarmMonitorStatusTable,'alarmMonitorStatusEntry':alarmMonitorStatusEntry,_A9:alarmMonitorStatusIndex,'alarmMonitorStatus':alarmMonitorStatus,'alarmUtilitiesCommand':alarmUtilitiesCommand,'portHistory':portHistory,'portHistoryExtendedControlTable':portHistoryExtendedControlTable,'portHistoryExtendedControlEntry':portHistoryExtendedControlEntry,'portHistoryExtendedControlCreateTime':portHistoryExtendedControlCreateTime,'portHistoryExtendedControlLastBucketIndex':portHistoryExtendedControlLastBucketIndex,'portHistoryExtendedControlNumberOfBuckets':portHistoryExtendedControlNumberOfBuckets,'portHistoryExtendedControlName':portHistoryExtendedControlName,'lsPortHistoryTable':lsPortHistoryTable,'lsPortHistoryEntry':lsPortHistoryEntry,_AA:lsPortHistoryIndex,_AB:lsPortHistorySampleIndex,'lsPortHistoryIntervalTime':lsPortHistoryIntervalTime,'lsPortHistoryBoxConfiguration':lsPortHistoryBoxConfiguration,'lsPortHistoryPkts':lsPortHistoryPkts,'lsPortHistoryCollisions':lsPortHistoryCollisions,'lsPortHistoryTotalErrors':lsPortHistoryTotalErrors,'scPortHistoryTable':scPortHistoryTable,'scPortHistoryEntry':scPortHistoryEntry,_AC:scPortHistoryIndex,_AD:scPortHistorySampleIndex,'scPortHistoryIntervalTime':scPortHistoryIntervalTime,'scPortHistoryBoxConfiguration':scPortHistoryBoxConfiguration,'scPortHistoryGoodPktsRec':scPortHistoryGoodPktsRec,'scPortHistoryGoodNonUnicastPktsRec':scPortHistoryGoodNonUnicastPktsRec,'scPortHistoryCollisions':scPortHistoryCollisions,'scPortHistoryBadPkts':scPortHistoryBadPkts,'scPortHistoryGoodPktsSent':scPortHistoryGoodPktsSent,'portHistoryMemoryAvailability':portHistoryMemoryAvailability})