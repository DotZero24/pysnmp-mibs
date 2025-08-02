_AB='hpicfSmartLinkNotificationGroup1'
_AA='hpicfSmartLinkGroupsGroup1'
_A9='hpicfSmartLinkNotificationGroup'
_A8='hpicfSmartLinkGroupsGroup'
_A7='hpicfSmartLinkPortStateChangeNotification1'
_A6='hpicfSmartLinkPortStateChangeNotification'
_A5='hpicfSmartLinkSecondaryFlushPktLastUpdate'
_A4='hpicfSmartLinkSecondaryFlushPktTx'
_A3='hpicfSmartLinkGroupSecondaryPort'
_A2='hpicfSmartLinkPrimaryFlushPktLastUpdate'
_A1='hpicfSmartLinkPrimaryFlushPktTx'
_A0='hpicfSmartLinkGroupPrimaryPort'
_z='hpicfSmartLinkPortRowStatus'
_y='hpicfSmartLinkRecvControlVlans4k'
_x='hpicfSmartLinkRecvControlVlans3k'
_w='hpicfSmartLinkRecvControlVlans2k'
_v='hpicfSmartLinkRecvControlVlans1k'
_u='hpicfSmartLinkResetFlushStatistics'
_t='hpicfSmartLinkLastFlushVlan'
_s='hpicfSmartLinkLastFlushDeviceId'
_r='hpicfSmartLinkLastFlushTime'
_q='hpicfSmartLinkLastFlushPort'
_p='hpicfSmartLinkTotalFlushPktsRx'
_o='hpicfSmartLinkExtendedGroupEntry'
_n='hpicfSmartLinkPortIndex'
_m='not-accessible'
_l='hpicfSmartLinkGroupIndex'
_k='hpicfSmartLinkNotificationObjectsGroup'
_j='hpicfSmartLinkPortGroup'
_i='hpicfSmartLinkGlobalGroup'
_h='hpicfSmartLinkGroupSecondaryPortState'
_g='hpicfSmartLinkGroupPrimaryPortState'
_f='hpicfSmartLinkGroupRowStatus'
_e='hpicfSmartLinkSlaveFlushPktLastUpdate'
_d='hpicfSmartLinkSlaveFlushPktTx'
_c='hpicfSmartLinkMasterFlushPktLastUpdate'
_b='hpicfSmartLinkMasterFlushPktTx'
_a='hpicfSmartLinkGroupClearStats'
_Z='hpicfSmartLinkGroupTrapControl'
_Y='hpicfSmartLinkGroupProtectedVlan4k'
_X='hpicfSmartLinkGroupProtectedVlan3k'
_W='hpicfSmartLinkGroupProtectedVlan2k'
_V='hpicfSmartLinkGroupProtectedVlan1k'
_U='hpicfSmartLinkGroupPreemptionDelay'
_T='hpicfSmartLinkGroupPreemptionMode'
_S='hpicfSmartLinkGroupSendControlVlan'
_R='hpicfSmartLinkGroupSlavePort'
_Q='hpicfSmartLinkGroupMasterPort'
_P='VlanIndex'
_O='hpicfSmartLinkNotifyGroupIndex'
_N='deprecated'
_M='down'
_L='standby'
_K='active'
_J='uninitialized'
_I='TruthValue'
_H='hpicfSmartLinkGroupSlavePortState'
_G='hpicfSmartLinkGroupMasterPortState'
_F='OctetString'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='current'
_A='HP-ICF-SMART-LINK-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_P)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_I)
hpicfSmartLinkMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,96))
if mibBuilder.loadTexts:hpicfSmartLinkMIB.setRevisions(('2021-06-10 00:00','2013-03-20 00:00'))
_HpicfSmartLinkNotifications_ObjectIdentity=ObjectIdentity
hpicfSmartLinkNotifications=_HpicfSmartLinkNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,96,0))
class _HpicfSmartLinkNotifyGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpicfSmartLinkNotifyGroupIndex_Type.__name__=_E
_HpicfSmartLinkNotifyGroupIndex_Object=MibScalar
hpicfSmartLinkNotifyGroupIndex=_HpicfSmartLinkNotifyGroupIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,0,1),_HpicfSmartLinkNotifyGroupIndex_Type())
hpicfSmartLinkNotifyGroupIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:hpicfSmartLinkNotifyGroupIndex.setStatus(_B)
_HpicfSmartLinkObjects_ObjectIdentity=ObjectIdentity
hpicfSmartLinkObjects=_HpicfSmartLinkObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,96,1))
_HpicfSmartLinkFlushStatistics_ObjectIdentity=ObjectIdentity
hpicfSmartLinkFlushStatistics=_HpicfSmartLinkFlushStatistics_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,96,1,1))
_HpicfSmartLinkLastFlushTime_Type=DateAndTime
_HpicfSmartLinkLastFlushTime_Object=MibScalar
hpicfSmartLinkLastFlushTime=_HpicfSmartLinkLastFlushTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,1,1),_HpicfSmartLinkLastFlushTime_Type())
hpicfSmartLinkLastFlushTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSmartLinkLastFlushTime.setStatus(_B)
_HpicfSmartLinkTotalFlushPktsRx_Type=Counter64
_HpicfSmartLinkTotalFlushPktsRx_Object=MibScalar
hpicfSmartLinkTotalFlushPktsRx=_HpicfSmartLinkTotalFlushPktsRx_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,1,2),_HpicfSmartLinkTotalFlushPktsRx_Type())
hpicfSmartLinkTotalFlushPktsRx.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSmartLinkTotalFlushPktsRx.setStatus(_B)
class _HpicfSmartLinkLastFlushPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfSmartLinkLastFlushPort_Type.__name__=_E
_HpicfSmartLinkLastFlushPort_Object=MibScalar
hpicfSmartLinkLastFlushPort=_HpicfSmartLinkLastFlushPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,1,3),_HpicfSmartLinkLastFlushPort_Type())
hpicfSmartLinkLastFlushPort.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSmartLinkLastFlushPort.setStatus(_B)
_HpicfSmartLinkLastFlushDeviceId_Type=MacAddress
_HpicfSmartLinkLastFlushDeviceId_Object=MibScalar
hpicfSmartLinkLastFlushDeviceId=_HpicfSmartLinkLastFlushDeviceId_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,1,4),_HpicfSmartLinkLastFlushDeviceId_Type())
hpicfSmartLinkLastFlushDeviceId.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSmartLinkLastFlushDeviceId.setStatus(_B)
class _HpicfSmartLinkLastFlushVlan_Type(VlanIndex):defaultValue=0
_HpicfSmartLinkLastFlushVlan_Type.__name__=_P
_HpicfSmartLinkLastFlushVlan_Object=MibScalar
hpicfSmartLinkLastFlushVlan=_HpicfSmartLinkLastFlushVlan_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,1,5),_HpicfSmartLinkLastFlushVlan_Type())
hpicfSmartLinkLastFlushVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSmartLinkLastFlushVlan.setStatus(_B)
class _HpicfSmartLinkResetFlushStatistics_Type(TruthValue):defaultValue=2
_HpicfSmartLinkResetFlushStatistics_Type.__name__=_I
_HpicfSmartLinkResetFlushStatistics_Object=MibScalar
hpicfSmartLinkResetFlushStatistics=_HpicfSmartLinkResetFlushStatistics_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,2),_HpicfSmartLinkResetFlushStatistics_Type())
hpicfSmartLinkResetFlushStatistics.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpicfSmartLinkResetFlushStatistics.setStatus(_B)
_HpicfSmartLinkGroupTable_Object=MibTable
hpicfSmartLinkGroupTable=_HpicfSmartLinkGroupTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,3))
if mibBuilder.loadTexts:hpicfSmartLinkGroupTable.setStatus(_B)
_HpicfSmartLinkGroupEntry_Object=MibTableRow
hpicfSmartLinkGroupEntry=_HpicfSmartLinkGroupEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,3,1))
hpicfSmartLinkGroupEntry.setIndexNames((0,_A,_l))
if mibBuilder.loadTexts:hpicfSmartLinkGroupEntry.setStatus(_B)
class _HpicfSmartLinkGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpicfSmartLinkGroupIndex_Type.__name__=_E
_HpicfSmartLinkGroupIndex_Object=MibTableColumn
hpicfSmartLinkGroupIndex=_HpicfSmartLinkGroupIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,3,1,1),_HpicfSmartLinkGroupIndex_Type())
hpicfSmartLinkGroupIndex.setMaxAccess(_m)
if mibBuilder.loadTexts:hpicfSmartLinkGroupIndex.setStatus(_B)
class _HpicfSmartLinkGroupMasterPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfSmartLinkGroupMasterPort_Type.__name__=_E
_HpicfSmartLinkGroupMasterPort_Object=MibTableColumn
hpicfSmartLinkGroupMasterPort=_HpicfSmartLinkGroupMasterPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,3,1,2),_HpicfSmartLinkGroupMasterPort_Type())
hpicfSmartLinkGroupMasterPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSmartLinkGroupMasterPort.setStatus(_B)
class _HpicfSmartLinkGroupSlavePort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfSmartLinkGroupSlavePort_Type.__name__=_E
_HpicfSmartLinkGroupSlavePort_Object=MibTableColumn
hpicfSmartLinkGroupSlavePort=_HpicfSmartLinkGroupSlavePort_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,3,1,3),_HpicfSmartLinkGroupSlavePort_Type())
hpicfSmartLinkGroupSlavePort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSmartLinkGroupSlavePort.setStatus(_B)
class _HpicfSmartLinkGroupSendControlVlan_Type(VlanIndex):defaultValue=1
_HpicfSmartLinkGroupSendControlVlan_Type.__name__=_P
_HpicfSmartLinkGroupSendControlVlan_Object=MibTableColumn
hpicfSmartLinkGroupSendControlVlan=_HpicfSmartLinkGroupSendControlVlan_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,3,1,4),_HpicfSmartLinkGroupSendControlVlan_Type())
hpicfSmartLinkGroupSendControlVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSmartLinkGroupSendControlVlan.setStatus(_B)
class _HpicfSmartLinkGroupPreemptionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('role',2)))
_HpicfSmartLinkGroupPreemptionMode_Type.__name__=_E
_HpicfSmartLinkGroupPreemptionMode_Object=MibTableColumn
hpicfSmartLinkGroupPreemptionMode=_HpicfSmartLinkGroupPreemptionMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,3,1,5),_HpicfSmartLinkGroupPreemptionMode_Type())
hpicfSmartLinkGroupPreemptionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSmartLinkGroupPreemptionMode.setStatus(_B)
class _HpicfSmartLinkGroupPreemptionDelay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_HpicfSmartLinkGroupPreemptionDelay_Type.__name__=_E
_HpicfSmartLinkGroupPreemptionDelay_Object=MibTableColumn
hpicfSmartLinkGroupPreemptionDelay=_HpicfSmartLinkGroupPreemptionDelay_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,3,1,6),_HpicfSmartLinkGroupPreemptionDelay_Type())
hpicfSmartLinkGroupPreemptionDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSmartLinkGroupPreemptionDelay.setStatus(_B)
class _HpicfSmartLinkGroupProtectedVlan1k_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HpicfSmartLinkGroupProtectedVlan1k_Type.__name__=_F
_HpicfSmartLinkGroupProtectedVlan1k_Object=MibTableColumn
hpicfSmartLinkGroupProtectedVlan1k=_HpicfSmartLinkGroupProtectedVlan1k_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,3,1,7),_HpicfSmartLinkGroupProtectedVlan1k_Type())
hpicfSmartLinkGroupProtectedVlan1k.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSmartLinkGroupProtectedVlan1k.setStatus(_B)
class _HpicfSmartLinkGroupProtectedVlan2k_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HpicfSmartLinkGroupProtectedVlan2k_Type.__name__=_F
_HpicfSmartLinkGroupProtectedVlan2k_Object=MibTableColumn
hpicfSmartLinkGroupProtectedVlan2k=_HpicfSmartLinkGroupProtectedVlan2k_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,3,1,8),_HpicfSmartLinkGroupProtectedVlan2k_Type())
hpicfSmartLinkGroupProtectedVlan2k.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSmartLinkGroupProtectedVlan2k.setStatus(_B)
class _HpicfSmartLinkGroupProtectedVlan3k_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HpicfSmartLinkGroupProtectedVlan3k_Type.__name__=_F
_HpicfSmartLinkGroupProtectedVlan3k_Object=MibTableColumn
hpicfSmartLinkGroupProtectedVlan3k=_HpicfSmartLinkGroupProtectedVlan3k_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,3,1,9),_HpicfSmartLinkGroupProtectedVlan3k_Type())
hpicfSmartLinkGroupProtectedVlan3k.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSmartLinkGroupProtectedVlan3k.setStatus(_B)
class _HpicfSmartLinkGroupProtectedVlan4k_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HpicfSmartLinkGroupProtectedVlan4k_Type.__name__=_F
_HpicfSmartLinkGroupProtectedVlan4k_Object=MibTableColumn
hpicfSmartLinkGroupProtectedVlan4k=_HpicfSmartLinkGroupProtectedVlan4k_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,3,1,10),_HpicfSmartLinkGroupProtectedVlan4k_Type())
hpicfSmartLinkGroupProtectedVlan4k.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSmartLinkGroupProtectedVlan4k.setStatus(_B)
class _HpicfSmartLinkGroupTrapControl_Type(TruthValue):defaultValue=2
_HpicfSmartLinkGroupTrapControl_Type.__name__=_I
_HpicfSmartLinkGroupTrapControl_Object=MibTableColumn
hpicfSmartLinkGroupTrapControl=_HpicfSmartLinkGroupTrapControl_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,3,1,11),_HpicfSmartLinkGroupTrapControl_Type())
hpicfSmartLinkGroupTrapControl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSmartLinkGroupTrapControl.setStatus(_B)
class _HpicfSmartLinkGroupClearStats_Type(TruthValue):defaultValue=2
_HpicfSmartLinkGroupClearStats_Type.__name__=_I
_HpicfSmartLinkGroupClearStats_Object=MibTableColumn
hpicfSmartLinkGroupClearStats=_HpicfSmartLinkGroupClearStats_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,3,1,12),_HpicfSmartLinkGroupClearStats_Type())
hpicfSmartLinkGroupClearStats.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSmartLinkGroupClearStats.setStatus(_B)
_HpicfSmartLinkGroupRowStatus_Type=RowStatus
_HpicfSmartLinkGroupRowStatus_Object=MibTableColumn
hpicfSmartLinkGroupRowStatus=_HpicfSmartLinkGroupRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,3,1,13),_HpicfSmartLinkGroupRowStatus_Type())
hpicfSmartLinkGroupRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSmartLinkGroupRowStatus.setStatus(_B)
class _HpicfSmartLinkGroupPrimaryPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfSmartLinkGroupPrimaryPort_Type.__name__=_E
_HpicfSmartLinkGroupPrimaryPort_Object=MibTableColumn
hpicfSmartLinkGroupPrimaryPort=_HpicfSmartLinkGroupPrimaryPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,3,1,14),_HpicfSmartLinkGroupPrimaryPort_Type())
hpicfSmartLinkGroupPrimaryPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSmartLinkGroupPrimaryPort.setStatus(_B)
class _HpicfSmartLinkGroupSecondaryPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfSmartLinkGroupSecondaryPort_Type.__name__=_E
_HpicfSmartLinkGroupSecondaryPort_Object=MibTableColumn
hpicfSmartLinkGroupSecondaryPort=_HpicfSmartLinkGroupSecondaryPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,3,1,15),_HpicfSmartLinkGroupSecondaryPort_Type())
hpicfSmartLinkGroupSecondaryPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSmartLinkGroupSecondaryPort.setStatus(_B)
_HpicfSmartLinkExtendedGroupTable_Object=MibTable
hpicfSmartLinkExtendedGroupTable=_HpicfSmartLinkExtendedGroupTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,4))
if mibBuilder.loadTexts:hpicfSmartLinkExtendedGroupTable.setStatus(_B)
_HpicfSmartLinkExtendedGroupEntry_Object=MibTableRow
hpicfSmartLinkExtendedGroupEntry=_HpicfSmartLinkExtendedGroupEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,4,1))
if mibBuilder.loadTexts:hpicfSmartLinkExtendedGroupEntry.setStatus(_B)
class _HpicfSmartLinkGroupMasterPortState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4)))
_HpicfSmartLinkGroupMasterPortState_Type.__name__=_E
_HpicfSmartLinkGroupMasterPortState_Object=MibTableColumn
hpicfSmartLinkGroupMasterPortState=_HpicfSmartLinkGroupMasterPortState_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,4,1,1),_HpicfSmartLinkGroupMasterPortState_Type())
hpicfSmartLinkGroupMasterPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSmartLinkGroupMasterPortState.setStatus(_B)
class _HpicfSmartLinkGroupSlavePortState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4)))
_HpicfSmartLinkGroupSlavePortState_Type.__name__=_E
_HpicfSmartLinkGroupSlavePortState_Object=MibTableColumn
hpicfSmartLinkGroupSlavePortState=_HpicfSmartLinkGroupSlavePortState_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,4,1,2),_HpicfSmartLinkGroupSlavePortState_Type())
hpicfSmartLinkGroupSlavePortState.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSmartLinkGroupSlavePortState.setStatus(_B)
_HpicfSmartLinkMasterFlushPktTx_Type=Counter64
_HpicfSmartLinkMasterFlushPktTx_Object=MibTableColumn
hpicfSmartLinkMasterFlushPktTx=_HpicfSmartLinkMasterFlushPktTx_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,4,1,3),_HpicfSmartLinkMasterFlushPktTx_Type())
hpicfSmartLinkMasterFlushPktTx.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSmartLinkMasterFlushPktTx.setStatus(_B)
_HpicfSmartLinkMasterFlushPktLastUpdate_Type=DateAndTime
_HpicfSmartLinkMasterFlushPktLastUpdate_Object=MibTableColumn
hpicfSmartLinkMasterFlushPktLastUpdate=_HpicfSmartLinkMasterFlushPktLastUpdate_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,4,1,4),_HpicfSmartLinkMasterFlushPktLastUpdate_Type())
hpicfSmartLinkMasterFlushPktLastUpdate.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSmartLinkMasterFlushPktLastUpdate.setStatus(_B)
_HpicfSmartLinkSlaveFlushPktTx_Type=Counter64
_HpicfSmartLinkSlaveFlushPktTx_Object=MibTableColumn
hpicfSmartLinkSlaveFlushPktTx=_HpicfSmartLinkSlaveFlushPktTx_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,4,1,5),_HpicfSmartLinkSlaveFlushPktTx_Type())
hpicfSmartLinkSlaveFlushPktTx.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSmartLinkSlaveFlushPktTx.setStatus(_B)
_HpicfSmartLinkSlaveFlushPktLastUpdate_Type=DateAndTime
_HpicfSmartLinkSlaveFlushPktLastUpdate_Object=MibTableColumn
hpicfSmartLinkSlaveFlushPktLastUpdate=_HpicfSmartLinkSlaveFlushPktLastUpdate_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,4,1,6),_HpicfSmartLinkSlaveFlushPktLastUpdate_Type())
hpicfSmartLinkSlaveFlushPktLastUpdate.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSmartLinkSlaveFlushPktLastUpdate.setStatus(_B)
class _HpicfSmartLinkGroupPrimaryPortState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4)))
_HpicfSmartLinkGroupPrimaryPortState_Type.__name__=_E
_HpicfSmartLinkGroupPrimaryPortState_Object=MibTableColumn
hpicfSmartLinkGroupPrimaryPortState=_HpicfSmartLinkGroupPrimaryPortState_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,4,1,7),_HpicfSmartLinkGroupPrimaryPortState_Type())
hpicfSmartLinkGroupPrimaryPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSmartLinkGroupPrimaryPortState.setStatus(_B)
class _HpicfSmartLinkGroupSecondaryPortState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4)))
_HpicfSmartLinkGroupSecondaryPortState_Type.__name__=_E
_HpicfSmartLinkGroupSecondaryPortState_Object=MibTableColumn
hpicfSmartLinkGroupSecondaryPortState=_HpicfSmartLinkGroupSecondaryPortState_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,4,1,8),_HpicfSmartLinkGroupSecondaryPortState_Type())
hpicfSmartLinkGroupSecondaryPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSmartLinkGroupSecondaryPortState.setStatus(_B)
_HpicfSmartLinkPrimaryFlushPktTx_Type=Counter64
_HpicfSmartLinkPrimaryFlushPktTx_Object=MibTableColumn
hpicfSmartLinkPrimaryFlushPktTx=_HpicfSmartLinkPrimaryFlushPktTx_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,4,1,9),_HpicfSmartLinkPrimaryFlushPktTx_Type())
hpicfSmartLinkPrimaryFlushPktTx.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSmartLinkPrimaryFlushPktTx.setStatus(_B)
_HpicfSmartLinkPrimaryFlushPktLastUpdate_Type=DateAndTime
_HpicfSmartLinkPrimaryFlushPktLastUpdate_Object=MibTableColumn
hpicfSmartLinkPrimaryFlushPktLastUpdate=_HpicfSmartLinkPrimaryFlushPktLastUpdate_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,4,1,10),_HpicfSmartLinkPrimaryFlushPktLastUpdate_Type())
hpicfSmartLinkPrimaryFlushPktLastUpdate.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSmartLinkPrimaryFlushPktLastUpdate.setStatus(_B)
_HpicfSmartLinkSecondaryFlushPktTx_Type=Counter64
_HpicfSmartLinkSecondaryFlushPktTx_Object=MibTableColumn
hpicfSmartLinkSecondaryFlushPktTx=_HpicfSmartLinkSecondaryFlushPktTx_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,4,1,11),_HpicfSmartLinkSecondaryFlushPktTx_Type())
hpicfSmartLinkSecondaryFlushPktTx.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSmartLinkSecondaryFlushPktTx.setStatus(_B)
_HpicfSmartLinkSecondaryFlushPktLastUpdate_Type=DateAndTime
_HpicfSmartLinkSecondaryFlushPktLastUpdate_Object=MibTableColumn
hpicfSmartLinkSecondaryFlushPktLastUpdate=_HpicfSmartLinkSecondaryFlushPktLastUpdate_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,4,1,12),_HpicfSmartLinkSecondaryFlushPktLastUpdate_Type())
hpicfSmartLinkSecondaryFlushPktLastUpdate.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSmartLinkSecondaryFlushPktLastUpdate.setStatus(_B)
_HpicfSmartLinkPortTable_Object=MibTable
hpicfSmartLinkPortTable=_HpicfSmartLinkPortTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,5))
if mibBuilder.loadTexts:hpicfSmartLinkPortTable.setStatus(_B)
_HpicfSmartLinkPortEntry_Object=MibTableRow
hpicfSmartLinkPortEntry=_HpicfSmartLinkPortEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,5,1))
hpicfSmartLinkPortEntry.setIndexNames((0,_A,_n))
if mibBuilder.loadTexts:hpicfSmartLinkPortEntry.setStatus(_B)
class _HpicfSmartLinkPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpicfSmartLinkPortIndex_Type.__name__=_E
_HpicfSmartLinkPortIndex_Object=MibTableColumn
hpicfSmartLinkPortIndex=_HpicfSmartLinkPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,5,1,1),_HpicfSmartLinkPortIndex_Type())
hpicfSmartLinkPortIndex.setMaxAccess(_m)
if mibBuilder.loadTexts:hpicfSmartLinkPortIndex.setStatus(_B)
class _HpicfSmartLinkRecvControlVlans1k_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HpicfSmartLinkRecvControlVlans1k_Type.__name__=_F
_HpicfSmartLinkRecvControlVlans1k_Object=MibTableColumn
hpicfSmartLinkRecvControlVlans1k=_HpicfSmartLinkRecvControlVlans1k_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,5,1,2),_HpicfSmartLinkRecvControlVlans1k_Type())
hpicfSmartLinkRecvControlVlans1k.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSmartLinkRecvControlVlans1k.setStatus(_B)
class _HpicfSmartLinkRecvControlVlans2k_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HpicfSmartLinkRecvControlVlans2k_Type.__name__=_F
_HpicfSmartLinkRecvControlVlans2k_Object=MibTableColumn
hpicfSmartLinkRecvControlVlans2k=_HpicfSmartLinkRecvControlVlans2k_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,5,1,3),_HpicfSmartLinkRecvControlVlans2k_Type())
hpicfSmartLinkRecvControlVlans2k.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSmartLinkRecvControlVlans2k.setStatus(_B)
class _HpicfSmartLinkRecvControlVlans3k_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HpicfSmartLinkRecvControlVlans3k_Type.__name__=_F
_HpicfSmartLinkRecvControlVlans3k_Object=MibTableColumn
hpicfSmartLinkRecvControlVlans3k=_HpicfSmartLinkRecvControlVlans3k_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,5,1,4),_HpicfSmartLinkRecvControlVlans3k_Type())
hpicfSmartLinkRecvControlVlans3k.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSmartLinkRecvControlVlans3k.setStatus(_B)
class _HpicfSmartLinkRecvControlVlans4k_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HpicfSmartLinkRecvControlVlans4k_Type.__name__=_F
_HpicfSmartLinkRecvControlVlans4k_Object=MibTableColumn
hpicfSmartLinkRecvControlVlans4k=_HpicfSmartLinkRecvControlVlans4k_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,5,1,5),_HpicfSmartLinkRecvControlVlans4k_Type())
hpicfSmartLinkRecvControlVlans4k.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSmartLinkRecvControlVlans4k.setStatus(_B)
_HpicfSmartLinkPortRowStatus_Type=RowStatus
_HpicfSmartLinkPortRowStatus_Object=MibTableColumn
hpicfSmartLinkPortRowStatus=_HpicfSmartLinkPortRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,96,1,5,1,6),_HpicfSmartLinkPortRowStatus_Type())
hpicfSmartLinkPortRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSmartLinkPortRowStatus.setStatus(_B)
_HpicfSmartLinkConformance_ObjectIdentity=ObjectIdentity
hpicfSmartLinkConformance=_HpicfSmartLinkConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,96,2))
_HpicfSmartLinkConformanceGroups_ObjectIdentity=ObjectIdentity
hpicfSmartLinkConformanceGroups=_HpicfSmartLinkConformanceGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,96,2,1))
_HpicfSmartLinkCompliances_ObjectIdentity=ObjectIdentity
hpicfSmartLinkCompliances=_HpicfSmartLinkCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,96,2,2))
hpicfSmartLinkGroupEntry.registerAugmentions((_A,_o))
hpicfSmartLinkExtendedGroupEntry.setIndexNames(*hpicfSmartLinkGroupEntry.getIndexNames())
hpicfSmartLinkGlobalGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,96,2,1,1))
hpicfSmartLinkGlobalGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:hpicfSmartLinkGlobalGroup.setStatus(_B)
hpicfSmartLinkGroupsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,96,2,1,2))
hpicfSmartLinkGroupsGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_G),(_A,_H),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:hpicfSmartLinkGroupsGroup.setStatus(_N)
hpicfSmartLinkPortGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,96,2,1,3))
hpicfSmartLinkPortGroup.setObjects(*((_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:hpicfSmartLinkPortGroup.setStatus(_B)
hpicfSmartLinkNotificationObjectsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,96,2,1,4))
hpicfSmartLinkNotificationObjectsGroup.setObjects((_A,_O))
if mibBuilder.loadTexts:hpicfSmartLinkNotificationObjectsGroup.setStatus(_B)
hpicfSmartLinkGroupsGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,96,2,1,6))
hpicfSmartLinkGroupsGroup1.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_G),(_A,_H),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_A0),(_A,_g),(_A,_h),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:hpicfSmartLinkGroupsGroup1.setStatus(_B)
hpicfSmartLinkPortStateChangeNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,96,0,2))
hpicfSmartLinkPortStateChangeNotification.setObjects(*((_A,_O),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:hpicfSmartLinkPortStateChangeNotification.setStatus(_N)
hpicfSmartLinkPortStateChangeNotification1=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,96,0,3))
hpicfSmartLinkPortStateChangeNotification1.setObjects(*((_A,_O),(_A,_G),(_A,_H),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:hpicfSmartLinkPortStateChangeNotification1.setStatus(_B)
hpicfSmartLinkNotificationGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,5,1,96,2,1,5))
hpicfSmartLinkNotificationGroup.setObjects((_A,_A6))
if mibBuilder.loadTexts:hpicfSmartLinkNotificationGroup.setStatus(_N)
hpicfSmartLinkNotificationGroup1=NotificationGroup((1,3,6,1,4,1,11,2,14,11,5,1,96,2,1,7))
hpicfSmartLinkNotificationGroup1.setObjects((_A,_A7))
if mibBuilder.loadTexts:hpicfSmartLinkNotificationGroup1.setStatus(_B)
hpicfSmartLinkCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,96,2,2,1))
hpicfSmartLinkCompliance1.setObjects(*((_A,_i),(_A,_A8),(_A,_j),(_A,_A9),(_A,_k)))
if mibBuilder.loadTexts:hpicfSmartLinkCompliance1.setStatus(_N)
hpicfSmartLinkCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,96,2,2,2))
hpicfSmartLinkCompliance2.setObjects(*((_A,_i),(_A,_AA),(_A,_j),(_A,_AB),(_A,_k)))
if mibBuilder.loadTexts:hpicfSmartLinkCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfSmartLinkMIB':hpicfSmartLinkMIB,'hpicfSmartLinkNotifications':hpicfSmartLinkNotifications,_O:hpicfSmartLinkNotifyGroupIndex,_A6:hpicfSmartLinkPortStateChangeNotification,_A7:hpicfSmartLinkPortStateChangeNotification1,'hpicfSmartLinkObjects':hpicfSmartLinkObjects,'hpicfSmartLinkFlushStatistics':hpicfSmartLinkFlushStatistics,_r:hpicfSmartLinkLastFlushTime,_p:hpicfSmartLinkTotalFlushPktsRx,_q:hpicfSmartLinkLastFlushPort,_s:hpicfSmartLinkLastFlushDeviceId,_t:hpicfSmartLinkLastFlushVlan,_u:hpicfSmartLinkResetFlushStatistics,'hpicfSmartLinkGroupTable':hpicfSmartLinkGroupTable,'hpicfSmartLinkGroupEntry':hpicfSmartLinkGroupEntry,_l:hpicfSmartLinkGroupIndex,_Q:hpicfSmartLinkGroupMasterPort,_R:hpicfSmartLinkGroupSlavePort,_S:hpicfSmartLinkGroupSendControlVlan,_T:hpicfSmartLinkGroupPreemptionMode,_U:hpicfSmartLinkGroupPreemptionDelay,_V:hpicfSmartLinkGroupProtectedVlan1k,_W:hpicfSmartLinkGroupProtectedVlan2k,_X:hpicfSmartLinkGroupProtectedVlan3k,_Y:hpicfSmartLinkGroupProtectedVlan4k,_Z:hpicfSmartLinkGroupTrapControl,_a:hpicfSmartLinkGroupClearStats,_f:hpicfSmartLinkGroupRowStatus,_A0:hpicfSmartLinkGroupPrimaryPort,_A3:hpicfSmartLinkGroupSecondaryPort,'hpicfSmartLinkExtendedGroupTable':hpicfSmartLinkExtendedGroupTable,_o:hpicfSmartLinkExtendedGroupEntry,_G:hpicfSmartLinkGroupMasterPortState,_H:hpicfSmartLinkGroupSlavePortState,_b:hpicfSmartLinkMasterFlushPktTx,_c:hpicfSmartLinkMasterFlushPktLastUpdate,_d:hpicfSmartLinkSlaveFlushPktTx,_e:hpicfSmartLinkSlaveFlushPktLastUpdate,_g:hpicfSmartLinkGroupPrimaryPortState,_h:hpicfSmartLinkGroupSecondaryPortState,_A1:hpicfSmartLinkPrimaryFlushPktTx,_A2:hpicfSmartLinkPrimaryFlushPktLastUpdate,_A4:hpicfSmartLinkSecondaryFlushPktTx,_A5:hpicfSmartLinkSecondaryFlushPktLastUpdate,'hpicfSmartLinkPortTable':hpicfSmartLinkPortTable,'hpicfSmartLinkPortEntry':hpicfSmartLinkPortEntry,_n:hpicfSmartLinkPortIndex,_v:hpicfSmartLinkRecvControlVlans1k,_w:hpicfSmartLinkRecvControlVlans2k,_x:hpicfSmartLinkRecvControlVlans3k,_y:hpicfSmartLinkRecvControlVlans4k,_z:hpicfSmartLinkPortRowStatus,'hpicfSmartLinkConformance':hpicfSmartLinkConformance,'hpicfSmartLinkConformanceGroups':hpicfSmartLinkConformanceGroups,_i:hpicfSmartLinkGlobalGroup,_A8:hpicfSmartLinkGroupsGroup,_j:hpicfSmartLinkPortGroup,_k:hpicfSmartLinkNotificationObjectsGroup,_A9:hpicfSmartLinkNotificationGroup,_AA:hpicfSmartLinkGroupsGroup1,_AB:hpicfSmartLinkNotificationGroup1,'hpicfSmartLinkCompliances':hpicfSmartLinkCompliances,'hpicfSmartLinkCompliance1':hpicfSmartLinkCompliance1,'hpicfSmartLinkCompliance2':hpicfSmartLinkCompliance2})