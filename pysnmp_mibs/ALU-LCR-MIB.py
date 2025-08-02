_u='aluLcrNotificationsGroup'
_t='aluLcrMdaStatusGroup'
_s='aluLcrStatusGroup'
_r='aluLcrCommandSwitchGroup'
_q='aluLcrMdaConfigGroup'
_p='aluLcrConfigGroup'
_o='aluLcrScalarLastChangedGroup'
_n='aluLcrCommandSwitchClear'
_m='aluLcrCommandSwitchSet'
_l='aluLcrEventSwitchover'
_k='aluLcrStatusMcCtlLinkStateChange'
_j='aluLcrMdaStatusDiscontinuityTime'
_i='aluLcrMdaStatusSwitchoverSeconds'
_h='aluLcrMdaStatusLastSwitchover'
_g='aluLcrStatusSwitchedMda'
_f='aluLcrStatusRequest'
_e='aluLcrMdaConfigHwIndex'
_d='aluLcrMdaConfigRowStatus'
_c='aluLcrConfigMcHoldTime'
_b='aluLcrConfigMcAdvertiseInterval'
_a='aluLcrConfigMcNeighborAddr'
_Z='aluLcrConfigMcNeighborAddrType'
_Y='aluLcrConfigWaitToRestore'
_X='aluLcrConfigRevert'
_W='aluLcrConfigDescription'
_V='aluLcrConfigRowStatus'
_U='aluLcrMdaConfigTableLastChanged'
_T='aluLcrConfigTableLastChanged'
_S='aluLcrMdaStatusEntry'
_R='aluLcrStatusEntry'
_Q='100s of milliseconds'
_P='not-accessible'
_O='TItemDescription'
_N='InetAddress'
_M='OctetString'
_L='aluLcrMdaStatusSwitchovers'
_K='aluLcrMdaStatusCurrent'
_J='aluLcrStatusMcCtlLinkState'
_I='aluLcrMdaConfigNumber'
_H='aluLcrCommandSwitch'
_G='aluLcrConfigName'
_F='Integer32'
_E='Unsigned32'
_D='read-create'
_C='read-only'
_B='ALU-LCR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aluSARConfs,aluSARMIBModules,aluSARNotifyPrefix,aluSARObjs=mibBuilder.importSymbols('ALU-SAR-GLOBAL-MIB','aluSARConfs','aluSARMIBModules','aluSARNotifyPrefix','aluSARObjs')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_N,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
TmnxHwIndex,=mibBuilder.importSymbols('TIMETRA-CHASSIS-MIB','TmnxHwIndex')
TItemDescription,TNamedItem=mibBuilder.importSymbols('TIMETRA-TC-MIB',_O,'TNamedItem')
aluLcrMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,6,1,1,1,3,21))
if mibBuilder.loadTexts:aluLcrMIBModule.setRevisions(('2018-09-26 00:00',))
_AluLcrConformance_ObjectIdentity=ObjectIdentity
aluLcrConformance=_AluLcrConformance_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,23))
_AluLcrCompliances_ObjectIdentity=ObjectIdentity
aluLcrCompliances=_AluLcrCompliances_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,23,1))
_AluLcrGroups_ObjectIdentity=ObjectIdentity
aluLcrGroups=_AluLcrGroups_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,23,2))
_AluLcrV9v0Groups_ObjectIdentity=ObjectIdentity
aluLcrV9v0Groups=_AluLcrV9v0Groups_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,23,2,1))
_AluLcrObjs_ObjectIdentity=ObjectIdentity
aluLcrObjs=_AluLcrObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,23))
_AluLcrScalarObjs_ObjectIdentity=ObjectIdentity
aluLcrScalarObjs=_AluLcrScalarObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,23,1))
_AluLcrScalarLastChangedObjs_ObjectIdentity=ObjectIdentity
aluLcrScalarLastChangedObjs=_AluLcrScalarLastChangedObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,23,1,1))
_AluLcrConfigTableLastChanged_Type=TimeStamp
_AluLcrConfigTableLastChanged_Object=MibScalar
aluLcrConfigTableLastChanged=_AluLcrConfigTableLastChanged_Object((1,3,6,1,4,1,6527,6,1,2,2,23,1,1,1),_AluLcrConfigTableLastChanged_Type())
aluLcrConfigTableLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:aluLcrConfigTableLastChanged.setStatus(_A)
_AluLcrMdaConfigTableLastChanged_Type=TimeStamp
_AluLcrMdaConfigTableLastChanged_Object=MibScalar
aluLcrMdaConfigTableLastChanged=_AluLcrMdaConfigTableLastChanged_Object((1,3,6,1,4,1,6527,6,1,2,2,23,1,1,2),_AluLcrMdaConfigTableLastChanged_Type())
aluLcrMdaConfigTableLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:aluLcrMdaConfigTableLastChanged.setStatus(_A)
_AluLcrConfigurations_ObjectIdentity=ObjectIdentity
aluLcrConfigurations=_AluLcrConfigurations_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,23,2))
_AluLcrConfigTable_Object=MibTable
aluLcrConfigTable=_AluLcrConfigTable_Object((1,3,6,1,4,1,6527,6,1,2,2,23,2,1))
if mibBuilder.loadTexts:aluLcrConfigTable.setStatus(_A)
_AluLcrConfigEntry_Object=MibTableRow
aluLcrConfigEntry=_AluLcrConfigEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,23,2,1,1))
aluLcrConfigEntry.setIndexNames((1,_B,_G))
if mibBuilder.loadTexts:aluLcrConfigEntry.setStatus(_A)
_AluLcrConfigName_Type=TNamedItem
_AluLcrConfigName_Object=MibTableColumn
aluLcrConfigName=_AluLcrConfigName_Object((1,3,6,1,4,1,6527,6,1,2,2,23,2,1,1,1),_AluLcrConfigName_Type())
aluLcrConfigName.setMaxAccess(_P)
if mibBuilder.loadTexts:aluLcrConfigName.setStatus(_A)
_AluLcrConfigRowStatus_Type=RowStatus
_AluLcrConfigRowStatus_Object=MibTableColumn
aluLcrConfigRowStatus=_AluLcrConfigRowStatus_Object((1,3,6,1,4,1,6527,6,1,2,2,23,2,1,1,2),_AluLcrConfigRowStatus_Type())
aluLcrConfigRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aluLcrConfigRowStatus.setStatus(_A)
class _AluLcrConfigDescription_Type(TItemDescription):defaultHexValue=''
_AluLcrConfigDescription_Type.__name__=_O
_AluLcrConfigDescription_Object=MibTableColumn
aluLcrConfigDescription=_AluLcrConfigDescription_Object((1,3,6,1,4,1,6527,6,1,2,2,23,2,1,1,3),_AluLcrConfigDescription_Type())
aluLcrConfigDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:aluLcrConfigDescription.setStatus(_A)
class _AluLcrConfigRevert_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonRevertive',1),('revertive',2)))
_AluLcrConfigRevert_Type.__name__=_F
_AluLcrConfigRevert_Object=MibTableColumn
aluLcrConfigRevert=_AluLcrConfigRevert_Object((1,3,6,1,4,1,6527,6,1,2,2,23,2,1,1,4),_AluLcrConfigRevert_Type())
aluLcrConfigRevert.setMaxAccess(_D)
if mibBuilder.loadTexts:aluLcrConfigRevert.setStatus(_A)
class _AluLcrConfigWaitToRestore_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(60,3600))
_AluLcrConfigWaitToRestore_Type.__name__=_E
_AluLcrConfigWaitToRestore_Object=MibTableColumn
aluLcrConfigWaitToRestore=_AluLcrConfigWaitToRestore_Object((1,3,6,1,4,1,6527,6,1,2,2,23,2,1,1,5),_AluLcrConfigWaitToRestore_Type())
aluLcrConfigWaitToRestore.setMaxAccess(_D)
if mibBuilder.loadTexts:aluLcrConfigWaitToRestore.setStatus(_A)
if mibBuilder.loadTexts:aluLcrConfigWaitToRestore.setUnits('seconds')
_AluLcrConfigMcNeighborAddrType_Type=InetAddressType
_AluLcrConfigMcNeighborAddrType_Object=MibTableColumn
aluLcrConfigMcNeighborAddrType=_AluLcrConfigMcNeighborAddrType_Object((1,3,6,1,4,1,6527,6,1,2,2,23,2,1,1,6),_AluLcrConfigMcNeighborAddrType_Type())
aluLcrConfigMcNeighborAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:aluLcrConfigMcNeighborAddrType.setStatus(_A)
class _AluLcrConfigMcNeighborAddr_Type(InetAddress):defaultHexValue='00000000000000000000000000000000';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_AluLcrConfigMcNeighborAddr_Type.__name__=_N
_AluLcrConfigMcNeighborAddr_Object=MibTableColumn
aluLcrConfigMcNeighborAddr=_AluLcrConfigMcNeighborAddr_Object((1,3,6,1,4,1,6527,6,1,2,2,23,2,1,1,7),_AluLcrConfigMcNeighborAddr_Type())
aluLcrConfigMcNeighborAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:aluLcrConfigMcNeighborAddr.setStatus(_A)
class _AluLcrConfigMcAdvertiseInterval_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,650))
_AluLcrConfigMcAdvertiseInterval_Type.__name__=_E
_AluLcrConfigMcAdvertiseInterval_Object=MibTableColumn
aluLcrConfigMcAdvertiseInterval=_AluLcrConfigMcAdvertiseInterval_Object((1,3,6,1,4,1,6527,6,1,2,2,23,2,1,1,8),_AluLcrConfigMcAdvertiseInterval_Type())
aluLcrConfigMcAdvertiseInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:aluLcrConfigMcAdvertiseInterval.setStatus(_A)
if mibBuilder.loadTexts:aluLcrConfigMcAdvertiseInterval.setUnits(_Q)
class _AluLcrConfigMcHoldTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,650))
_AluLcrConfigMcHoldTime_Type.__name__=_E
_AluLcrConfigMcHoldTime_Object=MibTableColumn
aluLcrConfigMcHoldTime=_AluLcrConfigMcHoldTime_Object((1,3,6,1,4,1,6527,6,1,2,2,23,2,1,1,9),_AluLcrConfigMcHoldTime_Type())
aluLcrConfigMcHoldTime.setMaxAccess(_D)
if mibBuilder.loadTexts:aluLcrConfigMcHoldTime.setStatus(_A)
if mibBuilder.loadTexts:aluLcrConfigMcHoldTime.setUnits(_Q)
_AluLcrMdaConfigTable_Object=MibTable
aluLcrMdaConfigTable=_AluLcrMdaConfigTable_Object((1,3,6,1,4,1,6527,6,1,2,2,23,2,2))
if mibBuilder.loadTexts:aluLcrMdaConfigTable.setStatus(_A)
_AluLcrMdaConfigEntry_Object=MibTableRow
aluLcrMdaConfigEntry=_AluLcrMdaConfigEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,23,2,2,1))
aluLcrMdaConfigEntry.setIndexNames((0,_B,_G),(0,_B,_I))
if mibBuilder.loadTexts:aluLcrMdaConfigEntry.setStatus(_A)
class _AluLcrMdaConfigNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AluLcrMdaConfigNumber_Type.__name__=_E
_AluLcrMdaConfigNumber_Object=MibTableColumn
aluLcrMdaConfigNumber=_AluLcrMdaConfigNumber_Object((1,3,6,1,4,1,6527,6,1,2,2,23,2,2,1,1),_AluLcrMdaConfigNumber_Type())
aluLcrMdaConfigNumber.setMaxAccess(_P)
if mibBuilder.loadTexts:aluLcrMdaConfigNumber.setStatus(_A)
_AluLcrMdaConfigRowStatus_Type=RowStatus
_AluLcrMdaConfigRowStatus_Object=MibTableColumn
aluLcrMdaConfigRowStatus=_AluLcrMdaConfigRowStatus_Object((1,3,6,1,4,1,6527,6,1,2,2,23,2,2,1,2),_AluLcrMdaConfigRowStatus_Type())
aluLcrMdaConfigRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aluLcrMdaConfigRowStatus.setStatus(_A)
_AluLcrMdaConfigHwIndex_Type=TmnxHwIndex
_AluLcrMdaConfigHwIndex_Object=MibTableColumn
aluLcrMdaConfigHwIndex=_AluLcrMdaConfigHwIndex_Object((1,3,6,1,4,1,6527,6,1,2,2,23,2,2,1,3),_AluLcrMdaConfigHwIndex_Type())
aluLcrMdaConfigHwIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:aluLcrMdaConfigHwIndex.setStatus(_A)
_AluLcrCommandTable_Object=MibTable
aluLcrCommandTable=_AluLcrCommandTable_Object((1,3,6,1,4,1,6527,6,1,2,2,23,2,3))
if mibBuilder.loadTexts:aluLcrCommandTable.setStatus(_A)
_AluLcrCommandEntry_Object=MibTableRow
aluLcrCommandEntry=_AluLcrCommandEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,23,2,3,1))
aluLcrCommandEntry.setIndexNames((0,_B,_G),(0,_B,_I))
if mibBuilder.loadTexts:aluLcrCommandEntry.setStatus(_A)
class _AluLcrCommandSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('noCmd',1),('clear',2),('lockoutOfProtection',3),('forcedSwitchWorkToProtect',4),('forcedSwitchProtectToWork',5)))
_AluLcrCommandSwitch_Type.__name__=_F
_AluLcrCommandSwitch_Object=MibTableColumn
aluLcrCommandSwitch=_AluLcrCommandSwitch_Object((1,3,6,1,4,1,6527,6,1,2,2,23,2,3,1,1),_AluLcrCommandSwitch_Type())
aluLcrCommandSwitch.setMaxAccess('read-write')
if mibBuilder.loadTexts:aluLcrCommandSwitch.setStatus(_A)
_AluLcrStatus_ObjectIdentity=ObjectIdentity
aluLcrStatus=_AluLcrStatus_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,23,3))
_AluLcrStatusTable_Object=MibTable
aluLcrStatusTable=_AluLcrStatusTable_Object((1,3,6,1,4,1,6527,6,1,2,2,23,3,1))
if mibBuilder.loadTexts:aluLcrStatusTable.setStatus(_A)
_AluLcrStatusEntry_Object=MibTableRow
aluLcrStatusEntry=_AluLcrStatusEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,23,3,1,1))
if mibBuilder.loadTexts:aluLcrStatusEntry.setStatus(_A)
class _AluLcrStatusRequest_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_AluLcrStatusRequest_Type.__name__=_M
_AluLcrStatusRequest_Object=MibTableColumn
aluLcrStatusRequest=_AluLcrStatusRequest_Object((1,3,6,1,4,1,6527,6,1,2,2,23,3,1,1,1),_AluLcrStatusRequest_Type())
aluLcrStatusRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:aluLcrStatusRequest.setStatus(_A)
_AluLcrStatusSwitchedMda_Type=Integer32
_AluLcrStatusSwitchedMda_Object=MibTableColumn
aluLcrStatusSwitchedMda=_AluLcrStatusSwitchedMda_Object((1,3,6,1,4,1,6527,6,1,2,2,23,3,1,1,2),_AluLcrStatusSwitchedMda_Type())
aluLcrStatusSwitchedMda.setMaxAccess(_C)
if mibBuilder.loadTexts:aluLcrStatusSwitchedMda.setStatus(_A)
class _AluLcrStatusMcCtlLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('up',0),('downSignalingFailure',1),('downIncompatibleNbr',2)))
_AluLcrStatusMcCtlLinkState_Type.__name__=_F
_AluLcrStatusMcCtlLinkState_Object=MibTableColumn
aluLcrStatusMcCtlLinkState=_AluLcrStatusMcCtlLinkState_Object((1,3,6,1,4,1,6527,6,1,2,2,23,3,1,1,3),_AluLcrStatusMcCtlLinkState_Type())
aluLcrStatusMcCtlLinkState.setMaxAccess(_C)
if mibBuilder.loadTexts:aluLcrStatusMcCtlLinkState.setStatus(_A)
_AluLcrMdaStatusTable_Object=MibTable
aluLcrMdaStatusTable=_AluLcrMdaStatusTable_Object((1,3,6,1,4,1,6527,6,1,2,2,23,3,2))
if mibBuilder.loadTexts:aluLcrMdaStatusTable.setStatus(_A)
_AluLcrMdaStatusEntry_Object=MibTableRow
aluLcrMdaStatusEntry=_AluLcrMdaStatusEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,23,3,2,1))
if mibBuilder.loadTexts:aluLcrMdaStatusEntry.setStatus(_A)
class _AluLcrMdaStatusCurrent_Type(Bits):namedValues=NamedValues(*(('lockedOut',0),('sd',1),('sf',2),('switched',3),('wtr',4)))
_AluLcrMdaStatusCurrent_Type.__name__='Bits'
_AluLcrMdaStatusCurrent_Object=MibTableColumn
aluLcrMdaStatusCurrent=_AluLcrMdaStatusCurrent_Object((1,3,6,1,4,1,6527,6,1,2,2,23,3,2,1,1),_AluLcrMdaStatusCurrent_Type())
aluLcrMdaStatusCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:aluLcrMdaStatusCurrent.setStatus(_A)
_AluLcrMdaStatusSwitchovers_Type=Counter32
_AluLcrMdaStatusSwitchovers_Object=MibTableColumn
aluLcrMdaStatusSwitchovers=_AluLcrMdaStatusSwitchovers_Object((1,3,6,1,4,1,6527,6,1,2,2,23,3,2,1,2),_AluLcrMdaStatusSwitchovers_Type())
aluLcrMdaStatusSwitchovers.setMaxAccess(_C)
if mibBuilder.loadTexts:aluLcrMdaStatusSwitchovers.setStatus(_A)
_AluLcrMdaStatusLastSwitchover_Type=TimeStamp
_AluLcrMdaStatusLastSwitchover_Object=MibTableColumn
aluLcrMdaStatusLastSwitchover=_AluLcrMdaStatusLastSwitchover_Object((1,3,6,1,4,1,6527,6,1,2,2,23,3,2,1,3),_AluLcrMdaStatusLastSwitchover_Type())
aluLcrMdaStatusLastSwitchover.setMaxAccess(_C)
if mibBuilder.loadTexts:aluLcrMdaStatusLastSwitchover.setStatus(_A)
_AluLcrMdaStatusSwitchoverSeconds_Type=Counter32
_AluLcrMdaStatusSwitchoverSeconds_Object=MibTableColumn
aluLcrMdaStatusSwitchoverSeconds=_AluLcrMdaStatusSwitchoverSeconds_Object((1,3,6,1,4,1,6527,6,1,2,2,23,3,2,1,4),_AluLcrMdaStatusSwitchoverSeconds_Type())
aluLcrMdaStatusSwitchoverSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:aluLcrMdaStatusSwitchoverSeconds.setStatus(_A)
_AluLcrMdaStatusDiscontinuityTime_Type=TimeStamp
_AluLcrMdaStatusDiscontinuityTime_Object=MibTableColumn
aluLcrMdaStatusDiscontinuityTime=_AluLcrMdaStatusDiscontinuityTime_Object((1,3,6,1,4,1,6527,6,1,2,2,23,3,2,1,5),_AluLcrMdaStatusDiscontinuityTime_Type())
aluLcrMdaStatusDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aluLcrMdaStatusDiscontinuityTime.setStatus(_A)
_AluLcrNotifyPrefix_ObjectIdentity=ObjectIdentity
aluLcrNotifyPrefix=_AluLcrNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,3,19))
_AluLcrNotifications_ObjectIdentity=ObjectIdentity
aluLcrNotifications=_AluLcrNotifications_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,3,19,0))
aluLcrConfigEntry.registerAugmentions((_B,_R))
aluLcrStatusEntry.setIndexNames(*aluLcrConfigEntry.getIndexNames())
aluLcrMdaConfigEntry.registerAugmentions((_B,_S))
aluLcrMdaStatusEntry.setIndexNames(*aluLcrMdaConfigEntry.getIndexNames())
aluLcrScalarLastChangedGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,23,2,1,1))
aluLcrScalarLastChangedGroup.setObjects(*((_B,_T),(_B,_U)))
if mibBuilder.loadTexts:aluLcrScalarLastChangedGroup.setStatus(_A)
aluLcrConfigGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,23,2,1,2))
aluLcrConfigGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:aluLcrConfigGroup.setStatus(_A)
aluLcrMdaConfigGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,23,2,1,3))
aluLcrMdaConfigGroup.setObjects(*((_B,_d),(_B,_e)))
if mibBuilder.loadTexts:aluLcrMdaConfigGroup.setStatus(_A)
aluLcrCommandSwitchGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,23,2,1,4))
aluLcrCommandSwitchGroup.setObjects((_B,_H))
if mibBuilder.loadTexts:aluLcrCommandSwitchGroup.setStatus(_A)
aluLcrStatusGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,23,2,1,5))
aluLcrStatusGroup.setObjects(*((_B,_f),(_B,_g),(_B,_J)))
if mibBuilder.loadTexts:aluLcrStatusGroup.setStatus(_A)
aluLcrMdaStatusGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,23,2,1,6))
aluLcrMdaStatusGroup.setObjects(*((_B,_K),(_B,_L),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:aluLcrMdaStatusGroup.setStatus(_A)
aluLcrStatusMcCtlLinkStateChange=NotificationType((1,3,6,1,4,1,6527,6,1,2,3,19,0,1))
aluLcrStatusMcCtlLinkStateChange.setObjects((_B,_J))
if mibBuilder.loadTexts:aluLcrStatusMcCtlLinkStateChange.setStatus(_A)
aluLcrEventSwitchover=NotificationType((1,3,6,1,4,1,6527,6,1,2,3,19,0,2))
aluLcrEventSwitchover.setObjects(*((_B,_L),(_B,_K)))
if mibBuilder.loadTexts:aluLcrEventSwitchover.setStatus(_A)
aluLcrCommandSwitchSet=NotificationType((1,3,6,1,4,1,6527,6,1,2,3,19,0,3))
aluLcrCommandSwitchSet.setObjects((_B,_H))
if mibBuilder.loadTexts:aluLcrCommandSwitchSet.setStatus(_A)
aluLcrCommandSwitchClear=NotificationType((1,3,6,1,4,1,6527,6,1,2,3,19,0,4))
aluLcrCommandSwitchClear.setObjects((_B,_H))
if mibBuilder.loadTexts:aluLcrCommandSwitchClear.setStatus(_A)
aluLcrNotificationsGroup=NotificationGroup((1,3,6,1,4,1,6527,6,1,2,1,23,2,1,7))
aluLcrNotificationsGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:aluLcrNotificationsGroup.setStatus(_A)
aluLcrCompliance=ModuleCompliance((1,3,6,1,4,1,6527,6,1,2,1,23,1,1))
aluLcrCompliance.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:aluLcrCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'aluLcrMIBModule':aluLcrMIBModule,'aluLcrConformance':aluLcrConformance,'aluLcrCompliances':aluLcrCompliances,'aluLcrCompliance':aluLcrCompliance,'aluLcrGroups':aluLcrGroups,'aluLcrV9v0Groups':aluLcrV9v0Groups,_o:aluLcrScalarLastChangedGroup,_p:aluLcrConfigGroup,_q:aluLcrMdaConfigGroup,_r:aluLcrCommandSwitchGroup,_s:aluLcrStatusGroup,_t:aluLcrMdaStatusGroup,_u:aluLcrNotificationsGroup,'aluLcrObjs':aluLcrObjs,'aluLcrScalarObjs':aluLcrScalarObjs,'aluLcrScalarLastChangedObjs':aluLcrScalarLastChangedObjs,_T:aluLcrConfigTableLastChanged,_U:aluLcrMdaConfigTableLastChanged,'aluLcrConfigurations':aluLcrConfigurations,'aluLcrConfigTable':aluLcrConfigTable,'aluLcrConfigEntry':aluLcrConfigEntry,_G:aluLcrConfigName,_V:aluLcrConfigRowStatus,_W:aluLcrConfigDescription,_X:aluLcrConfigRevert,_Y:aluLcrConfigWaitToRestore,_Z:aluLcrConfigMcNeighborAddrType,_a:aluLcrConfigMcNeighborAddr,_b:aluLcrConfigMcAdvertiseInterval,_c:aluLcrConfigMcHoldTime,'aluLcrMdaConfigTable':aluLcrMdaConfigTable,'aluLcrMdaConfigEntry':aluLcrMdaConfigEntry,_I:aluLcrMdaConfigNumber,_d:aluLcrMdaConfigRowStatus,_e:aluLcrMdaConfigHwIndex,'aluLcrCommandTable':aluLcrCommandTable,'aluLcrCommandEntry':aluLcrCommandEntry,_H:aluLcrCommandSwitch,'aluLcrStatus':aluLcrStatus,'aluLcrStatusTable':aluLcrStatusTable,_R:aluLcrStatusEntry,_f:aluLcrStatusRequest,_g:aluLcrStatusSwitchedMda,_J:aluLcrStatusMcCtlLinkState,'aluLcrMdaStatusTable':aluLcrMdaStatusTable,_S:aluLcrMdaStatusEntry,_K:aluLcrMdaStatusCurrent,_L:aluLcrMdaStatusSwitchovers,_h:aluLcrMdaStatusLastSwitchover,_i:aluLcrMdaStatusSwitchoverSeconds,_j:aluLcrMdaStatusDiscontinuityTime,'aluLcrNotifyPrefix':aluLcrNotifyPrefix,'aluLcrNotifications':aluLcrNotifications,_k:aluLcrStatusMcCtlLinkStateChange,_l:aluLcrEventSwitchover,_m:aluLcrCommandSwitchSet,_n:aluLcrCommandSwitchClear})