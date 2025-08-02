_AF='scPriorityQueuingModuleID'
_AE='scPowerEthPortPortId'
_AD='scPowerEthPortGroupId'
_AC='scPowerEthGroupId'
_AB='scEthGroupId'
_AA='noFlowControl'
_A9='scEthPortId'
_A8='scEthPortGroupId'
_A7='scGenPortIPAddressRspIpAddressIndex'
_A6='scGenPortIPAddressRspPortId'
_A5='scGenPortIPAddressRspGroupId'
_A4='scGenLinkAggregationId'
_A3='scGenSwitchId'
_A2='scGenPortDot1xPortPortId'
_A1='scGenPortDot1xPortGroupID'
_A0='initialize'
_z='scGenPortDot1xMAC'
_y='scGenPortDot1xMACPortId'
_x='scGenPortDot1xMACGroupID'
_w='scGenPortSecureMAC'
_v='scGenPortSecurePortId'
_u='scGenPortSecureGroupID'
_t='scGenPortRspId'
_s='scGenPortRspGroupId'
_r='disabled'
_q='enabled'
_p='scGenPortId'
_o='scGenPortGroupId'
_n='scGenGroupDot1xGroupId'
_m='scGenGroupRspGroupId'
_l='scGenGroupVlanId'
_k='scGenGroupVlanGroupId'
_j='scGenGroupSmonGroupId'
_i='oneFanFailed'
_h='allFansOK'
_g='unknown'
_f='token-ring'
_e='scGenGroupId'
_d='scHostTimeCreationOrder'
_c='scHostTimeIndex'
_b='scGenMonVLANId'
_a='scGenMonVLANSwitchId'
_Z='scGenMonPriorityId'
_Y='scGenMonPrioritySwitchId'
_X='scGenMonSwitchId'
_W='active'
_V='fail'
_U='regular'
_T='securityMode'
_S='nonSecurityMode'
_R='filterNotSupport'
_Q='filteringSupported'
_P='none'
_O='ethernet'
_N='not-accessible'
_M='ok'
_L='DisplayString'
_K='off'
_J='on'
_I='OctetString'
_H='enable'
_G='disable'
_F='XSWITCH-MIB'
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
PaeControlledPortStatus,=mibBuilder.importSymbols('IEEE8021-PAE-MIB','PaeControlledPortStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_L,'MacAddress','PhysAddress','TextualConvention','TruthValue')
class RowStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_W,1),('notInService',2),('notReady',3),('createAndGo',4),('createAndWait',5),('destroy',6)))
_SwitchChip_ObjectIdentity=ObjectIdentity
switchChip=_SwitchChip_ObjectIdentity((1,3,6,1,4,1,81,28))
_ScGen_ObjectIdentity=ObjectIdentity
scGen=_ScGen_ObjectIdentity((1,3,6,1,4,1,81,28,1))
_ScGenChassis_ObjectIdentity=ObjectIdentity
scGenChassis=_ScGenChassis_ObjectIdentity((1,3,6,1,4,1,81,28,1,1))
class _ScGenChMainAgPosition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_ScGenChMainAgPosition_Type.__name__=_C
_ScGenChMainAgPosition_Object=MibScalar
scGenChMainAgPosition=_ScGenChMainAgPosition_Object((1,3,6,1,4,1,81,28,1,1,1),_ScGenChMainAgPosition_Type())
scGenChMainAgPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenChMainAgPosition.setStatus(_A)
class _ScGenChRedunAgPosition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_ScGenChRedunAgPosition_Type.__name__=_C
_ScGenChRedunAgPosition_Object=MibScalar
scGenChRedunAgPosition=_ScGenChRedunAgPosition_Object((1,3,6,1,4,1,81,28,1,1,2),_ScGenChRedunAgPosition_Type())
scGenChRedunAgPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenChRedunAgPosition.setStatus(_A)
class _ScGenChRedunAgActivityStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('notPresent',1),('dormant',2),(_W,3),(_E,255)))
_ScGenChRedunAgActivityStatus_Type.__name__=_C
_ScGenChRedunAgActivityStatus_Object=MibScalar
scGenChRedunAgActivityStatus=_ScGenChRedunAgActivityStatus_Object((1,3,6,1,4,1,81,28,1,1,3),_ScGenChRedunAgActivityStatus_Type())
scGenChRedunAgActivityStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenChRedunAgActivityStatus.setStatus(_A)
class _ScGenChAgVLAN_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ScGenChAgVLAN_Type.__name__=_C
_ScGenChAgVLAN_Object=MibScalar
scGenChAgVLAN=_ScGenChAgVLAN_Object((1,3,6,1,4,1,81,28,1,1,4),_ScGenChAgVLAN_Type())
scGenChAgVLAN.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenChAgVLAN.setStatus(_A)
_ScGenMon_ObjectIdentity=ObjectIdentity
scGenMon=_ScGenMon_ObjectIdentity((1,3,6,1,4,1,81,28,1,2))
_ScGenMonTable_Object=MibTable
scGenMonTable=_ScGenMonTable_Object((1,3,6,1,4,1,81,28,1,2,1))
if mibBuilder.loadTexts:scGenMonTable.setStatus(_A)
_ScGenMonEntry_Object=MibTableRow
scGenMonEntry=_ScGenMonEntry_Object((1,3,6,1,4,1,81,28,1,2,1,1))
scGenMonEntry.setIndexNames((0,_F,_X))
if mibBuilder.loadTexts:scGenMonEntry.setStatus(_A)
class _ScGenMonSwitchId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ScGenMonSwitchId_Type.__name__=_C
_ScGenMonSwitchId_Object=MibTableColumn
scGenMonSwitchId=_ScGenMonSwitchId_Object((1,3,6,1,4,1,81,28,1,2,1,1,1),_ScGenMonSwitchId_Type())
scGenMonSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonSwitchId.setStatus(_A)
_ScGenMonDropEvents_Type=Counter32
_ScGenMonDropEvents_Object=MibTableColumn
scGenMonDropEvents=_ScGenMonDropEvents_Object((1,3,6,1,4,1,81,28,1,2,1,1,2),_ScGenMonDropEvents_Type())
scGenMonDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonDropEvents.setStatus(_A)
_ScGenMonOctets_Type=Counter32
_ScGenMonOctets_Object=MibTableColumn
scGenMonOctets=_ScGenMonOctets_Object((1,3,6,1,4,1,81,28,1,2,1,1,3),_ScGenMonOctets_Type())
scGenMonOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonOctets.setStatus(_A)
_ScGenMonPkts_Type=Counter32
_ScGenMonPkts_Object=MibTableColumn
scGenMonPkts=_ScGenMonPkts_Object((1,3,6,1,4,1,81,28,1,2,1,1,4),_ScGenMonPkts_Type())
scGenMonPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonPkts.setStatus(_A)
_ScGenMonGoodBroadcastPkts_Type=Counter32
_ScGenMonGoodBroadcastPkts_Object=MibTableColumn
scGenMonGoodBroadcastPkts=_ScGenMonGoodBroadcastPkts_Object((1,3,6,1,4,1,81,28,1,2,1,1,5),_ScGenMonGoodBroadcastPkts_Type())
scGenMonGoodBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonGoodBroadcastPkts.setStatus(_A)
_ScGenMonGoodMulticastPkts_Type=Counter32
_ScGenMonGoodMulticastPkts_Object=MibTableColumn
scGenMonGoodMulticastPkts=_ScGenMonGoodMulticastPkts_Object((1,3,6,1,4,1,81,28,1,2,1,1,6),_ScGenMonGoodMulticastPkts_Type())
scGenMonGoodMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonGoodMulticastPkts.setStatus(_A)
_ScGenMonGoodPkts_Type=Counter32
_ScGenMonGoodPkts_Object=MibTableColumn
scGenMonGoodPkts=_ScGenMonGoodPkts_Object((1,3,6,1,4,1,81,28,1,2,1,1,7),_ScGenMonGoodPkts_Type())
scGenMonGoodPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonGoodPkts.setStatus(_A)
_ScGenMonBadPkts_Type=Counter32
_ScGenMonBadPkts_Object=MibTableColumn
scGenMonBadPkts=_ScGenMonBadPkts_Object((1,3,6,1,4,1,81,28,1,2,1,1,8),_ScGenMonBadPkts_Type())
scGenMonBadPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonBadPkts.setStatus(_A)
_ScGenMonGoodOctets_Type=Counter32
_ScGenMonGoodOctets_Object=MibTableColumn
scGenMonGoodOctets=_ScGenMonGoodOctets_Object((1,3,6,1,4,1,81,28,1,2,1,1,9),_ScGenMonGoodOctets_Type())
scGenMonGoodOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonGoodOctets.setStatus(_A)
_ScGenMonBadOctets_Type=Counter32
_ScGenMonBadOctets_Object=MibTableColumn
scGenMonBadOctets=_ScGenMonBadOctets_Object((1,3,6,1,4,1,81,28,1,2,1,1,10),_ScGenMonBadOctets_Type())
scGenMonBadOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonBadOctets.setStatus(_A)
class _ScGenMonSmonCapability_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_ScGenMonSmonCapability_Type.__name__=_I
_ScGenMonSmonCapability_Object=MibTableColumn
scGenMonSmonCapability=_ScGenMonSmonCapability_Object((1,3,6,1,4,1,81,28,1,2,1,1,11),_ScGenMonSmonCapability_Type())
scGenMonSmonCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonSmonCapability.setStatus(_A)
class _ScGenMonMIBCtrMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_G,2),(_E,255)))
_ScGenMonMIBCtrMode_Type.__name__=_C
_ScGenMonMIBCtrMode_Object=MibTableColumn
scGenMonMIBCtrMode=_ScGenMonMIBCtrMode_Object((1,3,6,1,4,1,81,28,1,2,1,1,12),_ScGenMonMIBCtrMode_Type())
scGenMonMIBCtrMode.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenMonMIBCtrMode.setStatus(_A)
class _ScGenMonSwitchVLANList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_ScGenMonSwitchVLANList_Type.__name__=_I
_ScGenMonSwitchVLANList_Object=MibTableColumn
scGenMonSwitchVLANList=_ScGenMonSwitchVLANList_Object((1,3,6,1,4,1,81,28,1,2,1,1,13),_ScGenMonSwitchVLANList_Type())
scGenMonSwitchVLANList.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonSwitchVLANList.setStatus(_A)
class _ScGenMonMIBCtrList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_ScGenMonMIBCtrList_Type.__name__=_I
_ScGenMonMIBCtrList_Object=MibTableColumn
scGenMonMIBCtrList=_ScGenMonMIBCtrList_Object((1,3,6,1,4,1,81,28,1,2,1,1,14),_ScGenMonMIBCtrList_Type())
scGenMonMIBCtrList.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonMIBCtrList.setStatus(_A)
_ScGenMonTimeStamp_Type=TimeTicks
_ScGenMonTimeStamp_Object=MibTableColumn
scGenMonTimeStamp=_ScGenMonTimeStamp_Object((1,3,6,1,4,1,81,28,1,2,1,1,15),_ScGenMonTimeStamp_Type())
scGenMonTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonTimeStamp.setStatus(_A)
_ScGenMonVlanTimeStamp_Type=TimeTicks
_ScGenMonVlanTimeStamp_Object=MibTableColumn
scGenMonVlanTimeStamp=_ScGenMonVlanTimeStamp_Object((1,3,6,1,4,1,81,28,1,2,1,1,16),_ScGenMonVlanTimeStamp_Type())
scGenMonVlanTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonVlanTimeStamp.setStatus(_A)
_ScGenMonPriorityTable_Object=MibTable
scGenMonPriorityTable=_ScGenMonPriorityTable_Object((1,3,6,1,4,1,81,28,1,2,2))
if mibBuilder.loadTexts:scGenMonPriorityTable.setStatus(_A)
_ScGenMonPriorityEntry_Object=MibTableRow
scGenMonPriorityEntry=_ScGenMonPriorityEntry_Object((1,3,6,1,4,1,81,28,1,2,2,1))
scGenMonPriorityEntry.setIndexNames((0,_F,_Y),(0,_F,_Z))
if mibBuilder.loadTexts:scGenMonPriorityEntry.setStatus(_A)
class _ScGenMonPrioritySwitchId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ScGenMonPrioritySwitchId_Type.__name__=_C
_ScGenMonPrioritySwitchId_Object=MibTableColumn
scGenMonPrioritySwitchId=_ScGenMonPrioritySwitchId_Object((1,3,6,1,4,1,81,28,1,2,2,1,1),_ScGenMonPrioritySwitchId_Type())
scGenMonPrioritySwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonPrioritySwitchId.setStatus(_A)
class _ScGenMonPriorityId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_ScGenMonPriorityId_Type.__name__=_C
_ScGenMonPriorityId_Object=MibTableColumn
scGenMonPriorityId=_ScGenMonPriorityId_Object((1,3,6,1,4,1,81,28,1,2,2,1,2),_ScGenMonPriorityId_Type())
scGenMonPriorityId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonPriorityId.setStatus(_A)
_ScGenMonPriorityGoodPkts_Type=Counter32
_ScGenMonPriorityGoodPkts_Object=MibTableColumn
scGenMonPriorityGoodPkts=_ScGenMonPriorityGoodPkts_Object((1,3,6,1,4,1,81,28,1,2,2,1,3),_ScGenMonPriorityGoodPkts_Type())
scGenMonPriorityGoodPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonPriorityGoodPkts.setStatus(_A)
_ScGenMonPriorityGoodOctets_Type=Counter32
_ScGenMonPriorityGoodOctets_Object=MibTableColumn
scGenMonPriorityGoodOctets=_ScGenMonPriorityGoodOctets_Object((1,3,6,1,4,1,81,28,1,2,2,1,4),_ScGenMonPriorityGoodOctets_Type())
scGenMonPriorityGoodOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonPriorityGoodOctets.setStatus(_A)
class _ScGenMonVLANList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_ScGenMonVLANList_Type.__name__=_I
_ScGenMonVLANList_Object=MibScalar
scGenMonVLANList=_ScGenMonVLANList_Object((1,3,6,1,4,1,81,28,1,2,3),_ScGenMonVLANList_Type())
scGenMonVLANList.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonVLANList.setStatus(_A)
_ScGenMonVLANTable_Object=MibTable
scGenMonVLANTable=_ScGenMonVLANTable_Object((1,3,6,1,4,1,81,28,1,2,4))
if mibBuilder.loadTexts:scGenMonVLANTable.setStatus(_A)
_ScGenMonVLANEntry_Object=MibTableRow
scGenMonVLANEntry=_ScGenMonVLANEntry_Object((1,3,6,1,4,1,81,28,1,2,4,1))
scGenMonVLANEntry.setIndexNames((0,_F,_a),(0,_F,_b))
if mibBuilder.loadTexts:scGenMonVLANEntry.setStatus(_A)
class _ScGenMonVLANSwitchId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ScGenMonVLANSwitchId_Type.__name__=_C
_ScGenMonVLANSwitchId_Object=MibTableColumn
scGenMonVLANSwitchId=_ScGenMonVLANSwitchId_Object((1,3,6,1,4,1,81,28,1,2,4,1,1),_ScGenMonVLANSwitchId_Type())
scGenMonVLANSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonVLANSwitchId.setStatus(_A)
_ScGenMonVLANId_Type=Integer32
_ScGenMonVLANId_Object=MibTableColumn
scGenMonVLANId=_ScGenMonVLANId_Object((1,3,6,1,4,1,81,28,1,2,4,1,2),_ScGenMonVLANId_Type())
scGenMonVLANId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonVLANId.setStatus(_A)
_ScGenMonVLANGoodPkts_Type=Counter32
_ScGenMonVLANGoodPkts_Object=MibTableColumn
scGenMonVLANGoodPkts=_ScGenMonVLANGoodPkts_Object((1,3,6,1,4,1,81,28,1,2,4,1,3),_ScGenMonVLANGoodPkts_Type())
scGenMonVLANGoodPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonVLANGoodPkts.setStatus(_A)
_ScGenMonVLANGoodOctets_Type=Counter32
_ScGenMonVLANGoodOctets_Object=MibTableColumn
scGenMonVLANGoodOctets=_ScGenMonVLANGoodOctets_Object((1,3,6,1,4,1,81,28,1,2,4,1,4),_ScGenMonVLANGoodOctets_Type())
scGenMonVLANGoodOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonVLANGoodOctets.setStatus(_A)
_ScGenMonVLANStatsUcastPkts_Type=Counter32
_ScGenMonVLANStatsUcastPkts_Object=MibTableColumn
scGenMonVLANStatsUcastPkts=_ScGenMonVLANStatsUcastPkts_Object((1,3,6,1,4,1,81,28,1,2,4,1,5),_ScGenMonVLANStatsUcastPkts_Type())
scGenMonVLANStatsUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonVLANStatsUcastPkts.setStatus(_A)
_ScGenMonVLANStatsMcastPkts_Type=Counter32
_ScGenMonVLANStatsMcastPkts_Object=MibTableColumn
scGenMonVLANStatsMcastPkts=_ScGenMonVLANStatsMcastPkts_Object((1,3,6,1,4,1,81,28,1,2,4,1,6),_ScGenMonVLANStatsMcastPkts_Type())
scGenMonVLANStatsMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonVLANStatsMcastPkts.setStatus(_A)
_ScGenMonVLANStatsBcastPkts_Type=Counter32
_ScGenMonVLANStatsBcastPkts_Object=MibTableColumn
scGenMonVLANStatsBcastPkts=_ScGenMonVLANStatsBcastPkts_Object((1,3,6,1,4,1,81,28,1,2,4,1,7),_ScGenMonVLANStatsBcastPkts_Type())
scGenMonVLANStatsBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonVLANStatsBcastPkts.setStatus(_A)
class _ScGenMonSwitches_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_ScGenMonSwitches_Type.__name__=_I
_ScGenMonSwitches_Object=MibScalar
scGenMonSwitches=_ScGenMonSwitches_Object((1,3,6,1,4,1,81,28,1,2,5),_ScGenMonSwitches_Type())
scGenMonSwitches.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenMonSwitches.setStatus(_A)
_ScHostTimePortCorrTable_Object=MibTable
scHostTimePortCorrTable=_ScHostTimePortCorrTable_Object((1,3,6,1,4,1,81,28,1,2,6))
if mibBuilder.loadTexts:scHostTimePortCorrTable.setStatus(_A)
_ScHostTimePortCorrEntry_Object=MibTableRow
scHostTimePortCorrEntry=_ScHostTimePortCorrEntry_Object((1,3,6,1,4,1,81,28,1,2,6,1))
scHostTimePortCorrEntry.setIndexNames((0,_F,_c),(0,_F,_d))
if mibBuilder.loadTexts:scHostTimePortCorrEntry.setStatus(_A)
_ScHostTimeAddress_Type=OctetString
_ScHostTimeAddress_Object=MibTableColumn
scHostTimeAddress=_ScHostTimeAddress_Object((1,3,6,1,4,1,81,28,1,2,6,1,1),_ScHostTimeAddress_Type())
scHostTimeAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:scHostTimeAddress.setStatus(_A)
class _ScHostTimeCreationOrder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ScHostTimeCreationOrder_Type.__name__=_C
_ScHostTimeCreationOrder_Object=MibTableColumn
scHostTimeCreationOrder=_ScHostTimeCreationOrder_Object((1,3,6,1,4,1,81,28,1,2,6,1,2),_ScHostTimeCreationOrder_Type())
scHostTimeCreationOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:scHostTimeCreationOrder.setStatus(_A)
class _ScHostTimeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ScHostTimeIndex_Type.__name__=_C
_ScHostTimeIndex_Object=MibTableColumn
scHostTimeIndex=_ScHostTimeIndex_Object((1,3,6,1,4,1,81,28,1,2,6,1,3),_ScHostTimeIndex_Type())
scHostTimeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:scHostTimeIndex.setStatus(_A)
_ScHostTimePortConnection_Type=Integer32
_ScHostTimePortConnection_Object=MibTableColumn
scHostTimePortConnection=_ScHostTimePortConnection_Object((1,3,6,1,4,1,81,28,1,2,6,1,4),_ScHostTimePortConnection_Type())
scHostTimePortConnection.setMaxAccess(_B)
if mibBuilder.loadTexts:scHostTimePortConnection.setStatus(_A)
_ScGenGroup_ObjectIdentity=ObjectIdentity
scGenGroup=_ScGenGroup_ObjectIdentity((1,3,6,1,4,1,81,28,1,3))
_ScGenGroupTable_Object=MibTable
scGenGroupTable=_ScGenGroupTable_Object((1,3,6,1,4,1,81,28,1,3,1))
if mibBuilder.loadTexts:scGenGroupTable.setStatus(_A)
_ScGenGroupEntry_Object=MibTableRow
scGenGroupEntry=_ScGenGroupEntry_Object((1,3,6,1,4,1,81,28,1,3,1,1))
scGenGroupEntry.setIndexNames((0,_F,_e))
if mibBuilder.loadTexts:scGenGroupEntry.setStatus(_A)
_ScGenGroupId_Type=Integer32
_ScGenGroupId_Object=MibTableColumn
scGenGroupId=_ScGenGroupId_Object((1,3,6,1,4,1,81,28,1,3,1,1,1),_ScGenGroupId_Type())
scGenGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupId.setStatus(_A)
class _ScGenGroupUseSwitches_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_J,1),(_K,2),(_E,255)))
_ScGenGroupUseSwitches_Type.__name__=_C
_ScGenGroupUseSwitches_Object=MibTableColumn
scGenGroupUseSwitches=_ScGenGroupUseSwitches_Object((1,3,6,1,4,1,81,28,1,3,1,1,2),_ScGenGroupUseSwitches_Type())
scGenGroupUseSwitches.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupUseSwitches.setStatus(_A)
class _ScGenGroupCopyPortSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_J,1),(_K,2),(_E,255)))
_ScGenGroupCopyPortSupport_Type.__name__=_C
_ScGenGroupCopyPortSupport_Object=MibTableColumn
scGenGroupCopyPortSupport=_ScGenGroupCopyPortSupport_Object((1,3,6,1,4,1,81,28,1,3,1,1,3),_ScGenGroupCopyPortSupport_Type())
scGenGroupCopyPortSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupCopyPortSupport.setStatus(_A)
class _ScGenGroupXswitchConnection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ScGenGroupXswitchConnection_Type.__name__=_C
_ScGenGroupXswitchConnection_Object=MibTableColumn
scGenGroupXswitchConnection=_ScGenGroupXswitchConnection_Object((1,3,6,1,4,1,81,28,1,3,1,1,4),_ScGenGroupXswitchConnection_Type())
scGenGroupXswitchConnection.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupXswitchConnection.setStatus(_A)
class _ScGenGroupStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_M,1),('loadsBudgetProblem',2),(_E,255)))
_ScGenGroupStatus_Type.__name__=_C
_ScGenGroupStatus_Object=MibTableColumn
scGenGroupStatus=_ScGenGroupStatus_Object((1,3,6,1,4,1,81,28,1,3,1,1,5),_ScGenGroupStatus_Type())
scGenGroupStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupStatus.setStatus(_A)
class _ScGenGroupSwitchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_O,1),(_f,2),(_E,255)))
_ScGenGroupSwitchType_Type.__name__=_C
_ScGenGroupSwitchType_Object=MibTableColumn
scGenGroupSwitchType=_ScGenGroupSwitchType_Object((1,3,6,1,4,1,81,28,1,3,1,1,6),_ScGenGroupSwitchType_Type())
scGenGroupSwitchType.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupSwitchType.setStatus(_A)
class _ScGenGroupNumberOfLoads_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ScGenGroupNumberOfLoads_Type.__name__=_C
_ScGenGroupNumberOfLoads_Object=MibTableColumn
scGenGroupNumberOfLoads=_ScGenGroupNumberOfLoads_Object((1,3,6,1,4,1,81,28,1,3,1,1,7),_ScGenGroupNumberOfLoads_Type())
scGenGroupNumberOfLoads.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupNumberOfLoads.setStatus(_A)
class _ScGenGroupSetDefaults_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*((_J,1),(_K,2),('layer2Only',3),(_E,255)))
_ScGenGroupSetDefaults_Type.__name__=_C
_ScGenGroupSetDefaults_Object=MibTableColumn
scGenGroupSetDefaults=_ScGenGroupSetDefaults_Object((1,3,6,1,4,1,81,28,1,3,1,1,8),_ScGenGroupSetDefaults_Type())
scGenGroupSetDefaults.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupSetDefaults.setStatus(_A)
_ScGenGroupSupportCopyPortList_Type=OctetString
_ScGenGroupSupportCopyPortList_Object=MibTableColumn
scGenGroupSupportCopyPortList=_ScGenGroupSupportCopyPortList_Object((1,3,6,1,4,1,81,28,1,3,1,1,9),_ScGenGroupSupportCopyPortList_Type())
scGenGroupSupportCopyPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupSupportCopyPortList.setStatus(_A)
_ScGenGroupSupportPortCountersList_Type=OctetString
_ScGenGroupSupportPortCountersList_Object=MibTableColumn
scGenGroupSupportPortCountersList=_ScGenGroupSupportPortCountersList_Object((1,3,6,1,4,1,81,28,1,3,1,1,10),_ScGenGroupSupportPortCountersList_Type())
scGenGroupSupportPortCountersList.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupSupportPortCountersList.setStatus(_A)
_ScGenGroupSupportSegCountersList_Type=OctetString
_ScGenGroupSupportSegCountersList_Object=MibTableColumn
scGenGroupSupportSegCountersList=_ScGenGroupSupportSegCountersList_Object((1,3,6,1,4,1,81,28,1,3,1,1,11),_ScGenGroupSupportSegCountersList_Type())
scGenGroupSupportSegCountersList.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupSupportSegCountersList.setStatus(_A)
class _ScGenGroupUpLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('fiber',1),('copper',2),(_E,255)))
_ScGenGroupUpLinkType_Type.__name__=_C
_ScGenGroupUpLinkType_Object=MibTableColumn
scGenGroupUpLinkType=_ScGenGroupUpLinkType_Object((1,3,6,1,4,1,81,28,1,3,1,1,12),_ScGenGroupUpLinkType_Type())
scGenGroupUpLinkType.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupUpLinkType.setStatus(_A)
class _ScGenGroupPlugInType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,254,255)));namedValues=NamedValues(*(('cajunX120T8',1),('cajunX120F2',2),('cajunX120S1',3),('cajunX120S2',4),('cajunX120L1',5),('cajunX120L2',6),('cajunX120T16',7),('cajunX120F4',8),('cajunX120G2',9),('cajunX120GT2',10),('cajunX330T16',11),('cajunX330F4',12),('cajunX330F2',13),('cajunX330L2',14),('cajunX330S2',15),('cajunX330L1',16),('cajunX330S1',17),('cajunX330-OC12F1',18),('cajunX330-OC12F2',19),('cajunX330-OC3F1',20),('cajunX330-OC3F2',21),('cajunX330-OC12S1',22),('cajunX330-OC12S2',23),('cajunX330GT4',24),('cajunX330GT2',25),('cajunX330G2',26),('cajunX330W-4DS1',27),('cajunX330W-2DS1',28),('cajunX130F2',31),('cajunX130G2',32),('cajunX130GT2',33),('x330w-2ds1',34),('x330w-2usp',35),('x330w-2ds1-isdn',36),('x330w-2usp-isdn',37),('x330w-future1',38),('x330w-future2',39),('x330w-future3',40),('x330w-future4',41),('x330w-future5',42),('x330w-future6',43),('x330w-future7',44),('x330w-future8',45),('x330w-future9',46),(_g,254),(_P,255)))
_ScGenGroupPlugInType_Type.__name__=_C
_ScGenGroupPlugInType_Object=MibTableColumn
scGenGroupPlugInType=_ScGenGroupPlugInType_Object((1,3,6,1,4,1,81,28,1,3,1,1,13),_ScGenGroupPlugInType_Type())
scGenGroupPlugInType.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupPlugInType.setStatus(_A)
class _ScGenGroupPlugInDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ScGenGroupPlugInDescr_Type.__name__=_L
_ScGenGroupPlugInDescr_Object=MibTableColumn
scGenGroupPlugInDescr=_ScGenGroupPlugInDescr_Object((1,3,6,1,4,1,81,28,1,3,1,1,14),_ScGenGroupPlugInDescr_Type())
scGenGroupPlugInDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupPlugInDescr.setStatus(_A)
_ScGenGroupPlugInCS_Type=DisplayString
_ScGenGroupPlugInCS_Object=MibTableColumn
scGenGroupPlugInCS=_ScGenGroupPlugInCS_Object((1,3,6,1,4,1,81,28,1,3,1,1,15),_ScGenGroupPlugInCS_Type())
scGenGroupPlugInCS.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupPlugInCS.setStatus(_A)
class _ScGenGroupDefaultVLAN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('vlan0',1),('vlan1',2),(_E,255)))
_ScGenGroupDefaultVLAN_Type.__name__=_C
_ScGenGroupDefaultVLAN_Object=MibTableColumn
scGenGroupDefaultVLAN=_ScGenGroupDefaultVLAN_Object((1,3,6,1,4,1,81,28,1,3,1,1,16),_ScGenGroupDefaultVLAN_Type())
scGenGroupDefaultVLAN.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupDefaultVLAN.setStatus(_A)
class _ScGenGroupCascadingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,254,255)));namedValues=NamedValues(*(('cajunX330STK',1),('cajunX330MLSTK',2),('avayaX360STK',3),(_g,254),(_P,255)))
_ScGenGroupCascadingType_Type.__name__=_C
_ScGenGroupCascadingType_Object=MibTableColumn
scGenGroupCascadingType=_ScGenGroupCascadingType_Object((1,3,6,1,4,1,81,28,1,3,1,1,17),_ScGenGroupCascadingType_Type())
scGenGroupCascadingType.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupCascadingType.setStatus(_A)
class _ScGenGroupCascadingDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ScGenGroupCascadingDescr_Type.__name__=_L
_ScGenGroupCascadingDescr_Object=MibTableColumn
scGenGroupCascadingDescr=_ScGenGroupCascadingDescr_Object((1,3,6,1,4,1,81,28,1,3,1,1,18),_ScGenGroupCascadingDescr_Type())
scGenGroupCascadingDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupCascadingDescr.setStatus(_A)
_ScGenGroupCascadingCS_Type=DisplayString
_ScGenGroupCascadingCS_Object=MibTableColumn
scGenGroupCascadingCS=_ScGenGroupCascadingCS_Object((1,3,6,1,4,1,81,28,1,3,1,1,19),_ScGenGroupCascadingCS_Type())
scGenGroupCascadingCS.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupCascadingCS.setStatus(_A)
_ScGenGroupSupportDstCopyPortList_Type=OctetString
_ScGenGroupSupportDstCopyPortList_Object=MibTableColumn
scGenGroupSupportDstCopyPortList=_ScGenGroupSupportDstCopyPortList_Object((1,3,6,1,4,1,81,28,1,3,1,1,20),_ScGenGroupSupportDstCopyPortList_Type())
scGenGroupSupportDstCopyPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupSupportDstCopyPortList.setStatus(_A)
class _ScGenGroupBUPSType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('ac',1),('dc',2),(_P,255)))
_ScGenGroupBUPSType_Type.__name__=_C
_ScGenGroupBUPSType_Object=MibTableColumn
scGenGroupBUPSType=_ScGenGroupBUPSType_Object((1,3,6,1,4,1,81,28,1,3,1,1,21),_ScGenGroupBUPSType_Type())
scGenGroupBUPSType.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupBUPSType.setStatus(_A)
_ScGenGroupBUPSCS_Type=DisplayString
_ScGenGroupBUPSCS_Object=MibTableColumn
scGenGroupBUPSCS=_ScGenGroupBUPSCS_Object((1,3,6,1,4,1,81,28,1,3,1,1,22),_ScGenGroupBUPSCS_Type())
scGenGroupBUPSCS.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupBUPSCS.setStatus(_A)
class _ScGenGroupBUPSFansStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_h,1),(_i,2),(_E,255)))
_ScGenGroupBUPSFansStatus_Type.__name__=_C
_ScGenGroupBUPSFansStatus_Object=MibTableColumn
scGenGroupBUPSFansStatus=_ScGenGroupBUPSFansStatus_Object((1,3,6,1,4,1,81,28,1,3,1,1,23),_ScGenGroupBUPSFansStatus_Type())
scGenGroupBUPSFansStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupBUPSFansStatus.setStatus(_A)
class _ScGenGroupFansStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_h,1),(_i,2),(_E,255)))
_ScGenGroupFansStatus_Type.__name__=_C
_ScGenGroupFansStatus_Object=MibTableColumn
scGenGroupFansStatus=_ScGenGroupFansStatus_Object((1,3,6,1,4,1,81,28,1,3,1,1,24),_ScGenGroupFansStatus_Type())
scGenGroupFansStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupFansStatus.setStatus(_A)
class _ScGenGroupInternalBuffering_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('min',1),('max',2),('med',3),(_E,255)))
_ScGenGroupInternalBuffering_Type.__name__=_C
_ScGenGroupInternalBuffering_Object=MibTableColumn
scGenGroupInternalBuffering=_ScGenGroupInternalBuffering_Object((1,3,6,1,4,1,81,28,1,3,1,1,25),_ScGenGroupInternalBuffering_Type())
scGenGroupInternalBuffering.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupInternalBuffering.setStatus(_A)
class _ScGenGroupMcFilterBoxSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_Q,1),(_R,2),(_E,255)))
_ScGenGroupMcFilterBoxSupport_Type.__name__=_C
_ScGenGroupMcFilterBoxSupport_Object=MibTableColumn
scGenGroupMcFilterBoxSupport=_ScGenGroupMcFilterBoxSupport_Object((1,3,6,1,4,1,81,28,1,3,1,1,26),_ScGenGroupMcFilterBoxSupport_Type())
scGenGroupMcFilterBoxSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupMcFilterBoxSupport.setStatus(_A)
class _ScGenGroupMcFilterPersonalitySupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*((_Q,1),(_R,2),('personalityNotInstalled',3),(_E,255)))
_ScGenGroupMcFilterPersonalitySupport_Type.__name__=_C
_ScGenGroupMcFilterPersonalitySupport_Object=MibTableColumn
scGenGroupMcFilterPersonalitySupport=_ScGenGroupMcFilterPersonalitySupport_Object((1,3,6,1,4,1,81,28,1,3,1,1,27),_ScGenGroupMcFilterPersonalitySupport_Type())
scGenGroupMcFilterPersonalitySupport.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupMcFilterPersonalitySupport.setStatus(_A)
class _ScGenGroupMcFilterStackingSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*((_Q,1),(_R,2),('stackingNotInstalled',3),(_E,255)))
_ScGenGroupMcFilterStackingSupport_Type.__name__=_C
_ScGenGroupMcFilterStackingSupport_Object=MibTableColumn
scGenGroupMcFilterStackingSupport=_ScGenGroupMcFilterStackingSupport_Object((1,3,6,1,4,1,81,28,1,3,1,1,28),_ScGenGroupMcFilterStackingSupport_Type())
scGenGroupMcFilterStackingSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupMcFilterStackingSupport.setStatus(_A)
class _ScGenGroupLACPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_ScGenGroupLACPMode_Type.__name__=_C
_ScGenGroupLACPMode_Object=MibTableColumn
scGenGroupLACPMode=_ScGenGroupLACPMode_Object((1,3,6,1,4,1,81,28,1,3,1,1,29),_ScGenGroupLACPMode_Type())
scGenGroupLACPMode.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupLACPMode.setStatus(_A)
class _ScGenGroupSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_S,1),(_T,2),(_E,255)))
_ScGenGroupSecurityMode_Type.__name__=_C
_ScGenGroupSecurityMode_Object=MibTableColumn
scGenGroupSecurityMode=_ScGenGroupSecurityMode_Object((1,3,6,1,4,1,81,28,1,3,1,1,30),_ScGenGroupSecurityMode_Type())
scGenGroupSecurityMode.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupSecurityMode.setStatus(_A)
class _ScGenGroupBroadcastStormControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_J,1),(_K,2),(_E,255)))
_ScGenGroupBroadcastStormControl_Type.__name__=_C
_ScGenGroupBroadcastStormControl_Object=MibTableColumn
scGenGroupBroadcastStormControl=_ScGenGroupBroadcastStormControl_Object((1,3,6,1,4,1,81,28,1,3,1,1,31),_ScGenGroupBroadcastStormControl_Type())
scGenGroupBroadcastStormControl.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupBroadcastStormControl.setStatus(_A)
class _ScGenGroupBroadcastThreshold_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,144000))
_ScGenGroupBroadcastThreshold_Type.__name__=_C
_ScGenGroupBroadcastThreshold_Object=MibTableColumn
scGenGroupBroadcastThreshold=_ScGenGroupBroadcastThreshold_Object((1,3,6,1,4,1,81,28,1,3,1,1,32),_ScGenGroupBroadcastThreshold_Type())
scGenGroupBroadcastThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupBroadcastThreshold.setStatus(_A)
class _ScGenGroupPriorityQueuesScheduling_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('strict',1),('weighted',2),(_E,255)))
_ScGenGroupPriorityQueuesScheduling_Type.__name__=_C
_ScGenGroupPriorityQueuesScheduling_Object=MibTableColumn
scGenGroupPriorityQueuesScheduling=_ScGenGroupPriorityQueuesScheduling_Object((1,3,6,1,4,1,81,28,1,3,1,1,33),_ScGenGroupPriorityQueuesScheduling_Type())
scGenGroupPriorityQueuesScheduling.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupPriorityQueuesScheduling.setStatus(_A)
class _ScGenGroupBoundedDelay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_J,1),(_K,2),(_E,255)))
_ScGenGroupBoundedDelay_Type.__name__=_C
_ScGenGroupBoundedDelay_Object=MibTableColumn
scGenGroupBoundedDelay=_ScGenGroupBoundedDelay_Object((1,3,6,1,4,1,81,28,1,3,1,1,34),_ScGenGroupBoundedDelay_Type())
scGenGroupBoundedDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupBoundedDelay.setStatus(_A)
class _ScGenGroupSLDAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_G,2),(_E,255)))
_ScGenGroupSLDAdminStatus_Type.__name__=_C
_ScGenGroupSLDAdminStatus_Object=MibTableColumn
scGenGroupSLDAdminStatus=_ScGenGroupSLDAdminStatus_Object((1,3,6,1,4,1,81,28,1,3,1,1,35),_ScGenGroupSLDAdminStatus_Type())
scGenGroupSLDAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupSLDAdminStatus.setStatus(_A)
_ScGenGroupDynamicVlans_Type=Integer32
_ScGenGroupDynamicVlans_Object=MibTableColumn
scGenGroupDynamicVlans=_ScGenGroupDynamicVlans_Object((1,3,6,1,4,1,81,28,1,3,1,1,36),_ScGenGroupDynamicVlans_Type())
scGenGroupDynamicVlans.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupDynamicVlans.setStatus(_A)
class _ScGenGroupSecurityMacCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_ScGenGroupSecurityMacCount_Type.__name__=_C
_ScGenGroupSecurityMacCount_Object=MibTableColumn
scGenGroupSecurityMacCount=_ScGenGroupSecurityMacCount_Object((1,3,6,1,4,1,81,28,1,3,1,1,37),_ScGenGroupSecurityMacCount_Type())
scGenGroupSecurityMacCount.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupSecurityMacCount.setStatus(_A)
class _ScGenGroupBUPSAllocatedPower_Type(Integer32):defaultValue=800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,900))
_ScGenGroupBUPSAllocatedPower_Type.__name__=_C
_ScGenGroupBUPSAllocatedPower_Object=MibTableColumn
scGenGroupBUPSAllocatedPower=_ScGenGroupBUPSAllocatedPower_Object((1,3,6,1,4,1,81,28,1,3,1,1,38),_ScGenGroupBUPSAllocatedPower_Type())
scGenGroupBUPSAllocatedPower.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupBUPSAllocatedPower.setStatus(_A)
_ScGenGroupSmonTable_Object=MibTable
scGenGroupSmonTable=_ScGenGroupSmonTable_Object((1,3,6,1,4,1,81,28,1,3,2))
if mibBuilder.loadTexts:scGenGroupSmonTable.setStatus(_A)
_ScGenGroupSmonEntry_Object=MibTableRow
scGenGroupSmonEntry=_ScGenGroupSmonEntry_Object((1,3,6,1,4,1,81,28,1,3,2,1))
scGenGroupSmonEntry.setIndexNames((0,_F,_j))
if mibBuilder.loadTexts:scGenGroupSmonEntry.setStatus(_A)
_ScGenGroupSmonGroupId_Type=Integer32
_ScGenGroupSmonGroupId_Object=MibTableColumn
scGenGroupSmonGroupId=_ScGenGroupSmonGroupId_Object((1,3,6,1,4,1,81,28,1,3,2,1,1),_ScGenGroupSmonGroupId_Type())
scGenGroupSmonGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupSmonGroupId.setStatus(_A)
class _ScGenGroupSmonCapability_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_ScGenGroupSmonCapability_Type.__name__=_I
_ScGenGroupSmonCapability_Object=MibTableColumn
scGenGroupSmonCapability=_ScGenGroupSmonCapability_Object((1,3,6,1,4,1,81,28,1,3,2,1,2),_ScGenGroupSmonCapability_Type())
scGenGroupSmonCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupSmonCapability.setStatus(_A)
class _ScGenGroupSmonVlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_ScGenGroupSmonVlanList_Type.__name__=_I
_ScGenGroupSmonVlanList_Object=MibTableColumn
scGenGroupSmonVlanList=_ScGenGroupSmonVlanList_Object((1,3,6,1,4,1,81,28,1,3,2,1,3),_ScGenGroupSmonVlanList_Type())
scGenGroupSmonVlanList.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupSmonVlanList.setStatus(_A)
_ScGenGroupSmonDropEvents_Type=Counter32
_ScGenGroupSmonDropEvents_Object=MibTableColumn
scGenGroupSmonDropEvents=_ScGenGroupSmonDropEvents_Object((1,3,6,1,4,1,81,28,1,3,2,1,4),_ScGenGroupSmonDropEvents_Type())
scGenGroupSmonDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupSmonDropEvents.setStatus(_A)
_ScGenGroupSmonGoodBroadcastPkts_Type=Counter32
_ScGenGroupSmonGoodBroadcastPkts_Object=MibTableColumn
scGenGroupSmonGoodBroadcastPkts=_ScGenGroupSmonGoodBroadcastPkts_Object((1,3,6,1,4,1,81,28,1,3,2,1,5),_ScGenGroupSmonGoodBroadcastPkts_Type())
scGenGroupSmonGoodBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupSmonGoodBroadcastPkts.setStatus(_A)
_ScGenGroupSmonGoodMulticastPkts_Type=Counter32
_ScGenGroupSmonGoodMulticastPkts_Object=MibTableColumn
scGenGroupSmonGoodMulticastPkts=_ScGenGroupSmonGoodMulticastPkts_Object((1,3,6,1,4,1,81,28,1,3,2,1,6),_ScGenGroupSmonGoodMulticastPkts_Type())
scGenGroupSmonGoodMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupSmonGoodMulticastPkts.setStatus(_A)
_ScGenGroupSmonGoodPkts_Type=Counter32
_ScGenGroupSmonGoodPkts_Object=MibTableColumn
scGenGroupSmonGoodPkts=_ScGenGroupSmonGoodPkts_Object((1,3,6,1,4,1,81,28,1,3,2,1,7),_ScGenGroupSmonGoodPkts_Type())
scGenGroupSmonGoodPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupSmonGoodPkts.setStatus(_A)
_ScGenGroupSmonBadPkts_Type=Counter32
_ScGenGroupSmonBadPkts_Object=MibTableColumn
scGenGroupSmonBadPkts=_ScGenGroupSmonBadPkts_Object((1,3,6,1,4,1,81,28,1,3,2,1,8),_ScGenGroupSmonBadPkts_Type())
scGenGroupSmonBadPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupSmonBadPkts.setStatus(_A)
_ScGenGroupSmonGoodOctets_Type=Counter32
_ScGenGroupSmonGoodOctets_Object=MibTableColumn
scGenGroupSmonGoodOctets=_ScGenGroupSmonGoodOctets_Object((1,3,6,1,4,1,81,28,1,3,2,1,9),_ScGenGroupSmonGoodOctets_Type())
scGenGroupSmonGoodOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupSmonGoodOctets.setStatus(_A)
_ScGenGroupSmonBadOctets_Type=Counter32
_ScGenGroupSmonBadOctets_Object=MibTableColumn
scGenGroupSmonBadOctets=_ScGenGroupSmonBadOctets_Object((1,3,6,1,4,1,81,28,1,3,2,1,10),_ScGenGroupSmonBadOctets_Type())
scGenGroupSmonBadOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupSmonBadOctets.setStatus(_A)
_ScGenGroupSmonPkts_Type=Counter32
_ScGenGroupSmonPkts_Object=MibTableColumn
scGenGroupSmonPkts=_ScGenGroupSmonPkts_Object((1,3,6,1,4,1,81,28,1,3,2,1,11),_ScGenGroupSmonPkts_Type())
scGenGroupSmonPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupSmonPkts.setStatus(_A)
_ScGenGroupSmonOctets_Type=Counter32
_ScGenGroupSmonOctets_Object=MibTableColumn
scGenGroupSmonOctets=_ScGenGroupSmonOctets_Object((1,3,6,1,4,1,81,28,1,3,2,1,12),_ScGenGroupSmonOctets_Type())
scGenGroupSmonOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupSmonOctets.setStatus(_A)
class _ScGenGroupSmonMIBCtrMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_G,2),(_E,255)))
_ScGenGroupSmonMIBCtrMode_Type.__name__=_C
_ScGenGroupSmonMIBCtrMode_Object=MibTableColumn
scGenGroupSmonMIBCtrMode=_ScGenGroupSmonMIBCtrMode_Object((1,3,6,1,4,1,81,28,1,3,2,1,13),_ScGenGroupSmonMIBCtrMode_Type())
scGenGroupSmonMIBCtrMode.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupSmonMIBCtrMode.setStatus(_A)
_ScGenGroupVlanTable_Object=MibTable
scGenGroupVlanTable=_ScGenGroupVlanTable_Object((1,3,6,1,4,1,81,28,1,3,3))
if mibBuilder.loadTexts:scGenGroupVlanTable.setStatus(_A)
_ScGenGroupVlanEntry_Object=MibTableRow
scGenGroupVlanEntry=_ScGenGroupVlanEntry_Object((1,3,6,1,4,1,81,28,1,3,3,1))
scGenGroupVlanEntry.setIndexNames((0,_F,_k),(0,_F,_l))
if mibBuilder.loadTexts:scGenGroupVlanEntry.setStatus(_A)
_ScGenGroupVlanGroupId_Type=Integer32
_ScGenGroupVlanGroupId_Object=MibTableColumn
scGenGroupVlanGroupId=_ScGenGroupVlanGroupId_Object((1,3,6,1,4,1,81,28,1,3,3,1,1),_ScGenGroupVlanGroupId_Type())
scGenGroupVlanGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupVlanGroupId.setStatus(_A)
_ScGenGroupVlanId_Type=Integer32
_ScGenGroupVlanId_Object=MibTableColumn
scGenGroupVlanId=_ScGenGroupVlanId_Object((1,3,6,1,4,1,81,28,1,3,3,1,2),_ScGenGroupVlanId_Type())
scGenGroupVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupVlanId.setStatus(_A)
_ScGenGroupVlanUcastPkts_Type=Counter32
_ScGenGroupVlanUcastPkts_Object=MibTableColumn
scGenGroupVlanUcastPkts=_ScGenGroupVlanUcastPkts_Object((1,3,6,1,4,1,81,28,1,3,3,1,3),_ScGenGroupVlanUcastPkts_Type())
scGenGroupVlanUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupVlanUcastPkts.setStatus(_A)
_ScGenGroupVlanMcastPkts_Type=Counter32
_ScGenGroupVlanMcastPkts_Object=MibTableColumn
scGenGroupVlanMcastPkts=_ScGenGroupVlanMcastPkts_Object((1,3,6,1,4,1,81,28,1,3,3,1,4),_ScGenGroupVlanMcastPkts_Type())
scGenGroupVlanMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupVlanMcastPkts.setStatus(_A)
_ScGenGroupVlanBcastPkts_Type=Counter32
_ScGenGroupVlanBcastPkts_Object=MibTableColumn
scGenGroupVlanBcastPkts=_ScGenGroupVlanBcastPkts_Object((1,3,6,1,4,1,81,28,1,3,3,1,5),_ScGenGroupVlanBcastPkts_Type())
scGenGroupVlanBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupVlanBcastPkts.setStatus(_A)
_ScGenGroupVlanGoodPkts_Type=Counter32
_ScGenGroupVlanGoodPkts_Object=MibTableColumn
scGenGroupVlanGoodPkts=_ScGenGroupVlanGoodPkts_Object((1,3,6,1,4,1,81,28,1,3,3,1,6),_ScGenGroupVlanGoodPkts_Type())
scGenGroupVlanGoodPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupVlanGoodPkts.setStatus(_A)
_ScGenGroupVlanGoodOctets_Type=Counter32
_ScGenGroupVlanGoodOctets_Object=MibTableColumn
scGenGroupVlanGoodOctets=_ScGenGroupVlanGoodOctets_Object((1,3,6,1,4,1,81,28,1,3,3,1,7),_ScGenGroupVlanGoodOctets_Type())
scGenGroupVlanGoodOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupVlanGoodOctets.setStatus(_A)
_ScGenGroupVlanUcastOctets_Type=Counter32
_ScGenGroupVlanUcastOctets_Object=MibTableColumn
scGenGroupVlanUcastOctets=_ScGenGroupVlanUcastOctets_Object((1,3,6,1,4,1,81,28,1,3,3,1,8),_ScGenGroupVlanUcastOctets_Type())
scGenGroupVlanUcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupVlanUcastOctets.setStatus(_A)
_ScGenGroupVlanMcastOctets_Type=Counter32
_ScGenGroupVlanMcastOctets_Object=MibTableColumn
scGenGroupVlanMcastOctets=_ScGenGroupVlanMcastOctets_Object((1,3,6,1,4,1,81,28,1,3,3,1,9),_ScGenGroupVlanMcastOctets_Type())
scGenGroupVlanMcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupVlanMcastOctets.setStatus(_A)
_ScGenGroupVlanBcastOctets_Type=Counter32
_ScGenGroupVlanBcastOctets_Object=MibTableColumn
scGenGroupVlanBcastOctets=_ScGenGroupVlanBcastOctets_Object((1,3,6,1,4,1,81,28,1,3,3,1,10),_ScGenGroupVlanBcastOctets_Type())
scGenGroupVlanBcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupVlanBcastOctets.setStatus(_A)
_ScGenGroupVlanCurrentEgressPorts_Type=OctetString
_ScGenGroupVlanCurrentEgressPorts_Object=MibTableColumn
scGenGroupVlanCurrentEgressPorts=_ScGenGroupVlanCurrentEgressPorts_Object((1,3,6,1,4,1,81,28,1,3,3,1,11),_ScGenGroupVlanCurrentEgressPorts_Type())
scGenGroupVlanCurrentEgressPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupVlanCurrentEgressPorts.setStatus(_A)
_ScGenGroupVlanCurrentUntaggedPorts_Type=OctetString
_ScGenGroupVlanCurrentUntaggedPorts_Object=MibTableColumn
scGenGroupVlanCurrentUntaggedPorts=_ScGenGroupVlanCurrentUntaggedPorts_Object((1,3,6,1,4,1,81,28,1,3,3,1,12),_ScGenGroupVlanCurrentUntaggedPorts_Type())
scGenGroupVlanCurrentUntaggedPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupVlanCurrentUntaggedPorts.setStatus(_A)
_ScGenGroupVlanStaticEgressPorts_Type=OctetString
_ScGenGroupVlanStaticEgressPorts_Object=MibTableColumn
scGenGroupVlanStaticEgressPorts=_ScGenGroupVlanStaticEgressPorts_Object((1,3,6,1,4,1,81,28,1,3,3,1,13),_ScGenGroupVlanStaticEgressPorts_Type())
scGenGroupVlanStaticEgressPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupVlanStaticEgressPorts.setStatus(_A)
_ScGenGroupVlanStaticUntaggedPorts_Type=OctetString
_ScGenGroupVlanStaticUntaggedPorts_Object=MibTableColumn
scGenGroupVlanStaticUntaggedPorts=_ScGenGroupVlanStaticUntaggedPorts_Object((1,3,6,1,4,1,81,28,1,3,3,1,14),_ScGenGroupVlanStaticUntaggedPorts_Type())
scGenGroupVlanStaticUntaggedPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupVlanStaticUntaggedPorts.setStatus(_A)
_ScGenGroupRspTable_Object=MibTable
scGenGroupRspTable=_ScGenGroupRspTable_Object((1,3,6,1,4,1,81,28,1,3,4))
if mibBuilder.loadTexts:scGenGroupRspTable.setStatus(_A)
_ScGenGroupRspEntry_Object=MibTableRow
scGenGroupRspEntry=_ScGenGroupRspEntry_Object((1,3,6,1,4,1,81,28,1,3,4,1))
scGenGroupRspEntry.setIndexNames((0,_F,_m))
if mibBuilder.loadTexts:scGenGroupRspEntry.setStatus(_A)
_ScGenGroupRspGroupId_Type=Integer32
_ScGenGroupRspGroupId_Object=MibTableColumn
scGenGroupRspGroupId=_ScGenGroupRspGroupId_Object((1,3,6,1,4,1,81,28,1,3,4,1,1),_ScGenGroupRspGroupId_Type())
scGenGroupRspGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupRspGroupId.setStatus(_A)
class _ScGenGroupRspHelloInterval_Type(Integer32):defaultValue=1
_ScGenGroupRspHelloInterval_Type.__name__=_C
_ScGenGroupRspHelloInterval_Object=MibTableColumn
scGenGroupRspHelloInterval=_ScGenGroupRspHelloInterval_Object((1,3,6,1,4,1,81,28,1,3,4,1,2),_ScGenGroupRspHelloInterval_Type())
scGenGroupRspHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupRspHelloInterval.setStatus(_A)
class _ScGenGroupRspDevicePollingInterval_Type(Integer32):defaultValue=1
_ScGenGroupRspDevicePollingInterval_Type.__name__=_C
_ScGenGroupRspDevicePollingInterval_Object=MibTableColumn
scGenGroupRspDevicePollingInterval=_ScGenGroupRspDevicePollingInterval_Object((1,3,6,1,4,1,81,28,1,3,4,1,3),_ScGenGroupRspDevicePollingInterval_Type())
scGenGroupRspDevicePollingInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupRspDevicePollingInterval.setStatus(_A)
class _ScGenGroupRspDeviceNotRespondingTimeout_Type(Integer32):defaultValue=5
_ScGenGroupRspDeviceNotRespondingTimeout_Type.__name__=_C
_ScGenGroupRspDeviceNotRespondingTimeout_Object=MibTableColumn
scGenGroupRspDeviceNotRespondingTimeout=_ScGenGroupRspDeviceNotRespondingTimeout_Object((1,3,6,1,4,1,81,28,1,3,4,1,4),_ScGenGroupRspDeviceNotRespondingTimeout_Type())
scGenGroupRspDeviceNotRespondingTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupRspDeviceNotRespondingTimeout.setStatus(_A)
class _ScGenGroupRspSwitchNotRespondingTimeout_Type(Integer32):defaultValue=5
_ScGenGroupRspSwitchNotRespondingTimeout_Type.__name__=_C
_ScGenGroupRspSwitchNotRespondingTimeout_Object=MibTableColumn
scGenGroupRspSwitchNotRespondingTimeout=_ScGenGroupRspSwitchNotRespondingTimeout_Object((1,3,6,1,4,1,81,28,1,3,4,1,5),_ScGenGroupRspSwitchNotRespondingTimeout_Type())
scGenGroupRspSwitchNotRespondingTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupRspSwitchNotRespondingTimeout.setStatus(_A)
class _ScGenGroupRspMoveToForwardingInterval_Type(Integer32):defaultValue=5
_ScGenGroupRspMoveToForwardingInterval_Type.__name__=_C
_ScGenGroupRspMoveToForwardingInterval_Object=MibTableColumn
scGenGroupRspMoveToForwardingInterval=_ScGenGroupRspMoveToForwardingInterval_Object((1,3,6,1,4,1,81,28,1,3,4,1,6),_ScGenGroupRspMoveToForwardingInterval_Type())
scGenGroupRspMoveToForwardingInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupRspMoveToForwardingInterval.setStatus(_A)
class _ScGenGroupRspBroadcastArpShortInterval_Type(Integer32):defaultValue=5
_ScGenGroupRspBroadcastArpShortInterval_Type.__name__=_C
_ScGenGroupRspBroadcastArpShortInterval_Object=MibTableColumn
scGenGroupRspBroadcastArpShortInterval=_ScGenGroupRspBroadcastArpShortInterval_Object((1,3,6,1,4,1,81,28,1,3,4,1,7),_ScGenGroupRspBroadcastArpShortInterval_Type())
scGenGroupRspBroadcastArpShortInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupRspBroadcastArpShortInterval.setStatus(_A)
class _ScGenGroupRspBroadcastArpShortIntervalNumber_Type(Integer32):defaultValue=5
_ScGenGroupRspBroadcastArpShortIntervalNumber_Type.__name__=_C
_ScGenGroupRspBroadcastArpShortIntervalNumber_Object=MibTableColumn
scGenGroupRspBroadcastArpShortIntervalNumber=_ScGenGroupRspBroadcastArpShortIntervalNumber_Object((1,3,6,1,4,1,81,28,1,3,4,1,8),_ScGenGroupRspBroadcastArpShortIntervalNumber_Type())
scGenGroupRspBroadcastArpShortIntervalNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupRspBroadcastArpShortIntervalNumber.setStatus(_A)
class _ScGenGroupRspBroadcastArpLongInterval_Type(Integer32):defaultValue=150
_ScGenGroupRspBroadcastArpLongInterval_Type.__name__=_C
_ScGenGroupRspBroadcastArpLongInterval_Object=MibTableColumn
scGenGroupRspBroadcastArpLongInterval=_ScGenGroupRspBroadcastArpLongInterval_Object((1,3,6,1,4,1,81,28,1,3,4,1,9),_ScGenGroupRspBroadcastArpLongInterval_Type())
scGenGroupRspBroadcastArpLongInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupRspBroadcastArpLongInterval.setStatus(_A)
_ScGenGroupRspPeriodicPingsBoxIpAddress_Type=IpAddress
_ScGenGroupRspPeriodicPingsBoxIpAddress_Object=MibTableColumn
scGenGroupRspPeriodicPingsBoxIpAddress=_ScGenGroupRspPeriodicPingsBoxIpAddress_Object((1,3,6,1,4,1,81,28,1,3,4,1,10),_ScGenGroupRspPeriodicPingsBoxIpAddress_Type())
scGenGroupRspPeriodicPingsBoxIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupRspPeriodicPingsBoxIpAddress.setStatus(_A)
_ScGenGroupRspPeriodicPingsDestinationIpAddress_Type=IpAddress
_ScGenGroupRspPeriodicPingsDestinationIpAddress_Object=MibTableColumn
scGenGroupRspPeriodicPingsDestinationIpAddress=_ScGenGroupRspPeriodicPingsDestinationIpAddress_Object((1,3,6,1,4,1,81,28,1,3,4,1,11),_ScGenGroupRspPeriodicPingsDestinationIpAddress_Type())
scGenGroupRspPeriodicPingsDestinationIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupRspPeriodicPingsDestinationIpAddress.setStatus(_A)
class _ScGenGroupRspMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('rsp-module-mode-role-A',1),('rsp-modue-mode-role-B',2),(_E,255)))
_ScGenGroupRspMode_Type.__name__=_C
_ScGenGroupRspMode_Object=MibTableColumn
scGenGroupRspMode=_ScGenGroupRspMode_Object((1,3,6,1,4,1,81,28,1,3,4,1,12),_ScGenGroupRspMode_Type())
scGenGroupRspMode.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenGroupRspMode.setStatus(_A)
_ScGenGroupDot1xTable_Object=MibTable
scGenGroupDot1xTable=_ScGenGroupDot1xTable_Object((1,3,6,1,4,1,81,28,1,3,5))
if mibBuilder.loadTexts:scGenGroupDot1xTable.setStatus(_A)
_ScGenGroupDot1xEntry_Object=MibTableRow
scGenGroupDot1xEntry=_ScGenGroupDot1xEntry_Object((1,3,6,1,4,1,81,28,1,3,5,1))
scGenGroupDot1xEntry.setIndexNames((0,_F,_n))
if mibBuilder.loadTexts:scGenGroupDot1xEntry.setStatus(_A)
_ScGenGroupDot1xGroupId_Type=Integer32
_ScGenGroupDot1xGroupId_Object=MibTableColumn
scGenGroupDot1xGroupId=_ScGenGroupDot1xGroupId_Object((1,3,6,1,4,1,81,28,1,3,5,1,1),_ScGenGroupDot1xGroupId_Type())
scGenGroupDot1xGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupDot1xGroupId.setStatus(_A)
_ScGenGroupDot1xSystemMaxNumSupplicant_Type=Integer32
_ScGenGroupDot1xSystemMaxNumSupplicant_Object=MibTableColumn
scGenGroupDot1xSystemMaxNumSupplicant=_ScGenGroupDot1xSystemMaxNumSupplicant_Object((1,3,6,1,4,1,81,28,1,3,5,1,2),_ScGenGroupDot1xSystemMaxNumSupplicant_Type())
scGenGroupDot1xSystemMaxNumSupplicant.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupDot1xSystemMaxNumSupplicant.setStatus(_A)
_ScGenGroupDot1xCurrentNumSupplicant_Type=Integer32
_ScGenGroupDot1xCurrentNumSupplicant_Object=MibTableColumn
scGenGroupDot1xCurrentNumSupplicant=_ScGenGroupDot1xCurrentNumSupplicant_Object((1,3,6,1,4,1,81,28,1,3,5,1,3),_ScGenGroupDot1xCurrentNumSupplicant_Type())
scGenGroupDot1xCurrentNumSupplicant.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupDot1xCurrentNumSupplicant.setStatus(_A)
_ScGenGroupDot1xCurrentNumAuthenticatedSupplicant_Type=Integer32
_ScGenGroupDot1xCurrentNumAuthenticatedSupplicant_Object=MibTableColumn
scGenGroupDot1xCurrentNumAuthenticatedSupplicant=_ScGenGroupDot1xCurrentNumAuthenticatedSupplicant_Object((1,3,6,1,4,1,81,28,1,3,5,1,4),_ScGenGroupDot1xCurrentNumAuthenticatedSupplicant_Type())
scGenGroupDot1xCurrentNumAuthenticatedSupplicant.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupDot1xCurrentNumAuthenticatedSupplicant.setStatus(_A)
_ScGenGroupDot1xCurrentNumAuthenticatingSupplicant_Type=Integer32
_ScGenGroupDot1xCurrentNumAuthenticatingSupplicant_Object=MibTableColumn
scGenGroupDot1xCurrentNumAuthenticatingSupplicant=_ScGenGroupDot1xCurrentNumAuthenticatingSupplicant_Object((1,3,6,1,4,1,81,28,1,3,5,1,5),_ScGenGroupDot1xCurrentNumAuthenticatingSupplicant_Type())
scGenGroupDot1xCurrentNumAuthenticatingSupplicant.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenGroupDot1xCurrentNumAuthenticatingSupplicant.setStatus(_A)
_ScGenPort_ObjectIdentity=ObjectIdentity
scGenPort=_ScGenPort_ObjectIdentity((1,3,6,1,4,1,81,28,1,4))
_ScGenPortTable_Object=MibTable
scGenPortTable=_ScGenPortTable_Object((1,3,6,1,4,1,81,28,1,4,1))
if mibBuilder.loadTexts:scGenPortTable.setStatus(_A)
_ScGenPortEntry_Object=MibTableRow
scGenPortEntry=_ScGenPortEntry_Object((1,3,6,1,4,1,81,28,1,4,1,1))
scGenPortEntry.setIndexNames((0,_F,_o),(0,_F,_p))
if mibBuilder.loadTexts:scGenPortEntry.setStatus(_A)
_ScGenPortGroupId_Type=Integer32
_ScGenPortGroupId_Object=MibTableColumn
scGenPortGroupId=_ScGenPortGroupId_Object((1,3,6,1,4,1,81,28,1,4,1,1,1),_ScGenPortGroupId_Type())
scGenPortGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortGroupId.setStatus(_A)
_ScGenPortId_Type=Integer32
_ScGenPortId_Object=MibTableColumn
scGenPortId=_ScGenPortId_Object((1,3,6,1,4,1,81,28,1,4,1,1,2),_ScGenPortId_Type())
scGenPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortId.setStatus(_A)
class _ScGenPortVLAN_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_ScGenPortVLAN_Type.__name__=_C
_ScGenPortVLAN_Object=MibTableColumn
scGenPortVLAN=_ScGenPortVLAN_Object((1,3,6,1,4,1,81,28,1,4,1,1,3),_ScGenPortVLAN_Type())
scGenPortVLAN.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenPortVLAN.setStatus(_A)
class _ScGenPortPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,255)));namedValues=NamedValues(*((_U,1),('high',2),('userPriority1',3),('userPriority2',4),('userPriority3',5),('userPriority4',6),('userPriority5',7),('userPriority6',8),('userPriority7',9),('userPriority8',10),(_E,255)))
_ScGenPortPriority_Type.__name__=_C
_ScGenPortPriority_Object=MibTableColumn
scGenPortPriority=_ScGenPortPriority_Object((1,3,6,1,4,1,81,28,1,4,1,1,4),_ScGenPortPriority_Type())
scGenPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenPortPriority.setStatus(_A)
class _ScGenPortSetDefaults_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_J,1),(_K,2),(_E,255)))
_ScGenPortSetDefaults_Type.__name__=_C
_ScGenPortSetDefaults_Object=MibTableColumn
scGenPortSetDefaults=_ScGenPortSetDefaults_Object((1,3,6,1,4,1,81,28,1,4,1,1,5),_ScGenPortSetDefaults_Type())
scGenPortSetDefaults.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenPortSetDefaults.setStatus(_A)
class _ScGenPortBackbone_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_J,1),(_K,2),(_E,255)))
_ScGenPortBackbone_Type.__name__=_C
_ScGenPortBackbone_Object=MibTableColumn
scGenPortBackbone=_ScGenPortBackbone_Object((1,3,6,1,4,1,81,28,1,4,1,1,6),_ScGenPortBackbone_Type())
scGenPortBackbone.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortBackbone.setStatus(_A)
class _ScGenPortCopyMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_G,2),(_E,255)))
_ScGenPortCopyMode_Type.__name__=_C
_ScGenPortCopyMode_Object=MibTableColumn
scGenPortCopyMode=_ScGenPortCopyMode_Object((1,3,6,1,4,1,81,28,1,4,1,1,7),_ScGenPortCopyMode_Type())
scGenPortCopyMode.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenPortCopyMode.setStatus(_A)
class _ScGenPortCopyDestination_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8092))
_ScGenPortCopyDestination_Type.__name__=_C
_ScGenPortCopyDestination_Object=MibTableColumn
scGenPortCopyDestination=_ScGenPortCopyDestination_Object((1,3,6,1,4,1,81,28,1,4,1,1,8),_ScGenPortCopyDestination_Type())
scGenPortCopyDestination.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenPortCopyDestination.setStatus(_A)
class _ScGenPortLinkAggregationNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ScGenPortLinkAggregationNumber_Type.__name__=_C
_ScGenPortLinkAggregationNumber_Object=MibTableColumn
scGenPortLinkAggregationNumber=_ScGenPortLinkAggregationNumber_Object((1,3,6,1,4,1,81,28,1,4,1,1,9),_ScGenPortLinkAggregationNumber_Type())
scGenPortLinkAggregationNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenPortLinkAggregationNumber.setStatus(_A)
class _ScGenPortSendBridgedPackets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_J,1),(_K,2),(_E,255)))
_ScGenPortSendBridgedPackets_Type.__name__=_C
_ScGenPortSendBridgedPackets_Object=MibTableColumn
scGenPortSendBridgedPackets=_ScGenPortSendBridgedPackets_Object((1,3,6,1,4,1,81,28,1,4,1,1,10),_ScGenPortSendBridgedPackets_Type())
scGenPortSendBridgedPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenPortSendBridgedPackets.setStatus(_A)
class _ScGenPortVLANEgressStaticConfiguration_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_ScGenPortVLANEgressStaticConfiguration_Type.__name__=_I
_ScGenPortVLANEgressStaticConfiguration_Object=MibTableColumn
scGenPortVLANEgressStaticConfiguration=_ScGenPortVLANEgressStaticConfiguration_Object((1,3,6,1,4,1,81,28,1,4,1,1,11),_ScGenPortVLANEgressStaticConfiguration_Type())
scGenPortVLANEgressStaticConfiguration.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenPortVLANEgressStaticConfiguration.setStatus(_A)
class _ScGenPortStaticVLANBinding_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_G,2),(_E,255)))
_ScGenPortStaticVLANBinding_Type.__name__=_C
_ScGenPortStaticVLANBinding_Object=MibTableColumn
scGenPortStaticVLANBinding=_ScGenPortStaticVLANBinding_Object((1,3,6,1,4,1,81,28,1,4,1,1,12),_ScGenPortStaticVLANBinding_Type())
scGenPortStaticVLANBinding.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenPortStaticVLANBinding.setStatus(_A)
class _ScGenPortSecId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ScGenPortSecId_Type.__name__=_C
_ScGenPortSecId_Object=MibTableColumn
scGenPortSecId=_ScGenPortSecId_Object((1,3,6,1,4,1,81,28,1,4,1,1,13),_ScGenPortSecId_Type())
scGenPortSecId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortSecId.setStatus(_A)
class _ScGenPortMaxLagsOnSec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ScGenPortMaxLagsOnSec_Type.__name__=_C
_ScGenPortMaxLagsOnSec_Object=MibTableColumn
scGenPortMaxLagsOnSec=_ScGenPortMaxLagsOnSec_Object((1,3,6,1,4,1,81,28,1,4,1,1,14),_ScGenPortMaxLagsOnSec_Type())
scGenPortMaxLagsOnSec.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortMaxLagsOnSec.setStatus(_A)
class _ScGenPortGenericTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_ScGenPortGenericTrap_Type.__name__=_C
_ScGenPortGenericTrap_Object=MibTableColumn
scGenPortGenericTrap=_ScGenPortGenericTrap_Object((1,3,6,1,4,1,81,28,1,4,1,1,15),_ScGenPortGenericTrap_Type())
scGenPortGenericTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenPortGenericTrap.setStatus(_A)
class _ScGenPortLACPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_ScGenPortLACPMode_Type.__name__=_C
_ScGenPortLACPMode_Object=MibTableColumn
scGenPortLACPMode=_ScGenPortLACPMode_Object((1,3,6,1,4,1,81,28,1,4,1,1,16),_ScGenPortLACPMode_Type())
scGenPortLACPMode.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenPortLACPMode.setStatus(_A)
class _ScGenPortLastIntruderSourceAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1))
_ScGenPortLastIntruderSourceAddr_Type.__name__=_I
_ScGenPortLastIntruderSourceAddr_Object=MibTableColumn
scGenPortLastIntruderSourceAddr=_ScGenPortLastIntruderSourceAddr_Object((1,3,6,1,4,1,81,28,1,4,1,1,17),_ScGenPortLastIntruderSourceAddr_Type())
scGenPortLastIntruderSourceAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortLastIntruderSourceAddr.setStatus(_A)
class _ScGenPortSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_S,1),(_T,2),(_E,255)))
_ScGenPortSecurityMode_Type.__name__=_C
_ScGenPortSecurityMode_Object=MibTableColumn
scGenPortSecurityMode=_ScGenPortSecurityMode_Object((1,3,6,1,4,1,81,28,1,4,1,1,18),_ScGenPortSecurityMode_Type())
scGenPortSecurityMode.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenPortSecurityMode.setStatus(_A)
class _ScGenPortSTA_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_G,2),(_E,255)))
_ScGenPortSTA_Type.__name__=_C
_ScGenPortSTA_Object=MibTableColumn
scGenPortSTA=_ScGenPortSTA_Object((1,3,6,1,4,1,81,28,1,4,1,1,19),_ScGenPortSTA_Type())
scGenPortSTA.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenPortSTA.setStatus(_A)
_ScGenPortLagCapability_Type=OctetString
_ScGenPortLagCapability_Object=MibTableColumn
scGenPortLagCapability=_ScGenPortLagCapability_Object((1,3,6,1,4,1,81,28,1,4,1,1,20),_ScGenPortLagCapability_Type())
scGenPortLagCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortLagCapability.setStatus(_A)
_ScGenPortCapability_Type=OctetString
_ScGenPortCapability_Object=MibTableColumn
scGenPortCapability=_ScGenPortCapability_Object((1,3,6,1,4,1,81,28,1,4,1,1,21),_ScGenPortCapability_Type())
scGenPortCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortCapability.setStatus(_A)
class _ScGenPortSLDAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_q,1),(_r,2)))
_ScGenPortSLDAdminStatus_Type.__name__=_C
_ScGenPortSLDAdminStatus_Object=MibTableColumn
scGenPortSLDAdminStatus=_ScGenPortSLDAdminStatus_Object((1,3,6,1,4,1,81,28,1,4,1,1,22),_ScGenPortSLDAdminStatus_Type())
scGenPortSLDAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenPortSLDAdminStatus.setStatus(_A)
class _ScGenPortSLDStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('selfLoop',1),('noSelfLoop',2),(_E,255)))
_ScGenPortSLDStatus_Type.__name__=_C
_ScGenPortSLDStatus_Object=MibTableColumn
scGenPortSLDStatus=_ScGenPortSLDStatus_Object((1,3,6,1,4,1,81,28,1,4,1,1,23),_ScGenPortSLDStatus_Type())
scGenPortSLDStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortSLDStatus.setStatus(_A)
_ScGenPortCopyClassModuleLevel_Type=OctetString
_ScGenPortCopyClassModuleLevel_Object=MibTableColumn
scGenPortCopyClassModuleLevel=_ScGenPortCopyClassModuleLevel_Object((1,3,6,1,4,1,81,28,1,4,1,1,24),_ScGenPortCopyClassModuleLevel_Type())
scGenPortCopyClassModuleLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortCopyClassModuleLevel.setStatus(_A)
_ScGenPortCopyClassStackLevel_Type=OctetString
_ScGenPortCopyClassStackLevel_Object=MibTableColumn
scGenPortCopyClassStackLevel=_ScGenPortCopyClassStackLevel_Object((1,3,6,1,4,1,81,28,1,4,1,1,25),_ScGenPortCopyClassStackLevel_Type())
scGenPortCopyClassStackLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortCopyClassStackLevel.setStatus(_A)
_ScGenPortRspTable_Object=MibTable
scGenPortRspTable=_ScGenPortRspTable_Object((1,3,6,1,4,1,81,28,1,4,2))
if mibBuilder.loadTexts:scGenPortRspTable.setStatus(_A)
_ScGenPortRspEntry_Object=MibTableRow
scGenPortRspEntry=_ScGenPortRspEntry_Object((1,3,6,1,4,1,81,28,1,4,2,1))
scGenPortRspEntry.setIndexNames((0,_F,_s),(0,_F,_t))
if mibBuilder.loadTexts:scGenPortRspEntry.setStatus(_A)
_ScGenPortRspGroupId_Type=Integer32
_ScGenPortRspGroupId_Object=MibTableColumn
scGenPortRspGroupId=_ScGenPortRspGroupId_Object((1,3,6,1,4,1,81,28,1,4,2,1,1),_ScGenPortRspGroupId_Type())
scGenPortRspGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortRspGroupId.setStatus(_A)
_ScGenPortRspId_Type=Integer32
_ScGenPortRspId_Object=MibTableColumn
scGenPortRspId=_ScGenPortRspId_Object((1,3,6,1,4,1,81,28,1,4,2,1,2),_ScGenPortRspId_Type())
scGenPortRspId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortRspId.setStatus(_A)
class _ScGenPortRspMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*((_U,1),('rsp-mode-role-A',2),('rsp-mode-role-B',3),('device-mode',4),(_E,255)))
_ScGenPortRspMode_Type.__name__=_C
_ScGenPortRspMode_Object=MibTableColumn
scGenPortRspMode=_ScGenPortRspMode_Object((1,3,6,1,4,1,81,28,1,4,2,1,3),_ScGenPortRspMode_Type())
scGenPortRspMode.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenPortRspMode.setStatus(_A)
_ScGenPortSecureMACTable_Object=MibTable
scGenPortSecureMACTable=_ScGenPortSecureMACTable_Object((1,3,6,1,4,1,81,28,1,4,3))
if mibBuilder.loadTexts:scGenPortSecureMACTable.setStatus(_A)
_ScGenPortSecureMACEntry_Object=MibTableRow
scGenPortSecureMACEntry=_ScGenPortSecureMACEntry_Object((1,3,6,1,4,1,81,28,1,4,3,1))
scGenPortSecureMACEntry.setIndexNames((0,_F,_u),(0,_F,_v),(0,_F,_w))
if mibBuilder.loadTexts:scGenPortSecureMACEntry.setStatus(_A)
class _ScGenPortSecureGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_ScGenPortSecureGroupID_Type.__name__=_C
_ScGenPortSecureGroupID_Object=MibTableColumn
scGenPortSecureGroupID=_ScGenPortSecureGroupID_Object((1,3,6,1,4,1,81,28,1,4,3,1,1),_ScGenPortSecureGroupID_Type())
scGenPortSecureGroupID.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortSecureGroupID.setStatus(_A)
class _ScGenPortSecurePortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_ScGenPortSecurePortId_Type.__name__=_C
_ScGenPortSecurePortId_Object=MibTableColumn
scGenPortSecurePortId=_ScGenPortSecurePortId_Object((1,3,6,1,4,1,81,28,1,4,3,1,2),_ScGenPortSecurePortId_Type())
scGenPortSecurePortId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortSecurePortId.setStatus(_A)
_ScGenPortSecureMAC_Type=MacAddress
_ScGenPortSecureMAC_Object=MibTableColumn
scGenPortSecureMAC=_ScGenPortSecureMAC_Object((1,3,6,1,4,1,81,28,1,4,3,1,3),_ScGenPortSecureMAC_Type())
scGenPortSecureMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortSecureMAC.setStatus(_A)
_ScGenPortSecureMACStatus_Type=RowStatus
_ScGenPortSecureMACStatus_Object=MibTableColumn
scGenPortSecureMACStatus=_ScGenPortSecureMACStatus_Object((1,3,6,1,4,1,81,28,1,4,3,1,4),_ScGenPortSecureMACStatus_Type())
scGenPortSecureMACStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenPortSecureMACStatus.setStatus(_A)
_ScGenPortDot1xMACTable_Object=MibTable
scGenPortDot1xMACTable=_ScGenPortDot1xMACTable_Object((1,3,6,1,4,1,81,28,1,4,4))
if mibBuilder.loadTexts:scGenPortDot1xMACTable.setStatus(_A)
_ScGenPortDot1xMACEntry_Object=MibTableRow
scGenPortDot1xMACEntry=_ScGenPortDot1xMACEntry_Object((1,3,6,1,4,1,81,28,1,4,4,1))
scGenPortDot1xMACEntry.setIndexNames((0,_F,_x),(0,_F,_y),(0,_F,_z))
if mibBuilder.loadTexts:scGenPortDot1xMACEntry.setStatus(_A)
class _ScGenPortDot1xMACGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_ScGenPortDot1xMACGroupID_Type.__name__=_C
_ScGenPortDot1xMACGroupID_Object=MibTableColumn
scGenPortDot1xMACGroupID=_ScGenPortDot1xMACGroupID_Object((1,3,6,1,4,1,81,28,1,4,4,1,1),_ScGenPortDot1xMACGroupID_Type())
scGenPortDot1xMACGroupID.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortDot1xMACGroupID.setStatus(_A)
class _ScGenPortDot1xMACPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_ScGenPortDot1xMACPortId_Type.__name__=_C
_ScGenPortDot1xMACPortId_Object=MibTableColumn
scGenPortDot1xMACPortId=_ScGenPortDot1xMACPortId_Object((1,3,6,1,4,1,81,28,1,4,4,1,2),_ScGenPortDot1xMACPortId_Type())
scGenPortDot1xMACPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortDot1xMACPortId.setStatus(_A)
_ScGenPortDot1xMAC_Type=MacAddress
_ScGenPortDot1xMAC_Object=MibTableColumn
scGenPortDot1xMAC=_ScGenPortDot1xMAC_Object((1,3,6,1,4,1,81,28,1,4,4,1,3),_ScGenPortDot1xMAC_Type())
scGenPortDot1xMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortDot1xMAC.setStatus(_A)
class _ScGenPortDot1xMACAuthPaeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_A0,1),('disconnected',2),('connecting',3),('authenticating',4),('authenticated',5),('aborting',6),('held',7),('forceAuth',8),('forceUnauth',9)))
_ScGenPortDot1xMACAuthPaeState_Type.__name__=_C
_ScGenPortDot1xMACAuthPaeState_Object=MibTableColumn
scGenPortDot1xMACAuthPaeState=_ScGenPortDot1xMACAuthPaeState_Object((1,3,6,1,4,1,81,28,1,4,4,1,4),_ScGenPortDot1xMACAuthPaeState_Type())
scGenPortDot1xMACAuthPaeState.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortDot1xMACAuthPaeState.setStatus(_A)
class _ScGenPortDot1xMACAuthBackendAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('request',1),('response',2),('success',3),(_V,4),('timeout',5),('idle',6),(_A0,7)))
_ScGenPortDot1xMACAuthBackendAuthState_Type.__name__=_C
_ScGenPortDot1xMACAuthBackendAuthState_Object=MibTableColumn
scGenPortDot1xMACAuthBackendAuthState=_ScGenPortDot1xMACAuthBackendAuthState_Object((1,3,6,1,4,1,81,28,1,4,4,1,5),_ScGenPortDot1xMACAuthBackendAuthState_Type())
scGenPortDot1xMACAuthBackendAuthState.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortDot1xMACAuthBackendAuthState.setStatus(_A)
_ScGenPortDot1xAuthAuthControlledPortStatus_Type=PaeControlledPortStatus
_ScGenPortDot1xAuthAuthControlledPortStatus_Object=MibTableColumn
scGenPortDot1xAuthAuthControlledPortStatus=_ScGenPortDot1xAuthAuthControlledPortStatus_Object((1,3,6,1,4,1,81,28,1,4,4,1,6),_ScGenPortDot1xAuthAuthControlledPortStatus_Type())
scGenPortDot1xAuthAuthControlledPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortDot1xAuthAuthControlledPortStatus.setStatus(_A)
_ScGenPortDot1xPortTable_Object=MibTable
scGenPortDot1xPortTable=_ScGenPortDot1xPortTable_Object((1,3,6,1,4,1,81,28,1,4,5))
if mibBuilder.loadTexts:scGenPortDot1xPortTable.setStatus(_A)
_ScGenPortDot1xPortEntry_Object=MibTableRow
scGenPortDot1xPortEntry=_ScGenPortDot1xPortEntry_Object((1,3,6,1,4,1,81,28,1,4,5,1))
scGenPortDot1xPortEntry.setIndexNames((0,_F,_A1),(0,_F,_A2))
if mibBuilder.loadTexts:scGenPortDot1xPortEntry.setStatus(_A)
class _ScGenPortDot1xPortGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_ScGenPortDot1xPortGroupID_Type.__name__=_C
_ScGenPortDot1xPortGroupID_Object=MibTableColumn
scGenPortDot1xPortGroupID=_ScGenPortDot1xPortGroupID_Object((1,3,6,1,4,1,81,28,1,4,5,1,1),_ScGenPortDot1xPortGroupID_Type())
scGenPortDot1xPortGroupID.setMaxAccess(_N)
if mibBuilder.loadTexts:scGenPortDot1xPortGroupID.setStatus(_A)
class _ScGenPortDot1xPortPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_ScGenPortDot1xPortPortId_Type.__name__=_C
_ScGenPortDot1xPortPortId_Object=MibTableColumn
scGenPortDot1xPortPortId=_ScGenPortDot1xPortPortId_Object((1,3,6,1,4,1,81,28,1,4,5,1,2),_ScGenPortDot1xPortPortId_Type())
scGenPortDot1xPortPortId.setMaxAccess(_N)
if mibBuilder.loadTexts:scGenPortDot1xPortPortId.setStatus(_A)
class _ScGenPortDot1xPortMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('port',1),('mac',2)))
_ScGenPortDot1xPortMode_Type.__name__=_C
_ScGenPortDot1xPortMode_Object=MibTableColumn
scGenPortDot1xPortMode=_ScGenPortDot1xPortMode_Object((1,3,6,1,4,1,81,28,1,4,5,1,3),_ScGenPortDot1xPortMode_Type())
scGenPortDot1xPortMode.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenPortDot1xPortMode.setStatus(_A)
_ScGenPortDot1xPortNumSupplicants_Type=Integer32
_ScGenPortDot1xPortNumSupplicants_Object=MibTableColumn
scGenPortDot1xPortNumSupplicants=_ScGenPortDot1xPortNumSupplicants_Object((1,3,6,1,4,1,81,28,1,4,5,1,4),_ScGenPortDot1xPortNumSupplicants_Type())
scGenPortDot1xPortNumSupplicants.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortDot1xPortNumSupplicants.setStatus(_A)
_ScGenPortDot1xPortNumAuthenticatedSupplicants_Type=Integer32
_ScGenPortDot1xPortNumAuthenticatedSupplicants_Object=MibTableColumn
scGenPortDot1xPortNumAuthenticatedSupplicants=_ScGenPortDot1xPortNumAuthenticatedSupplicants_Object((1,3,6,1,4,1,81,28,1,4,5,1,5),_ScGenPortDot1xPortNumAuthenticatedSupplicants_Type())
scGenPortDot1xPortNumAuthenticatedSupplicants.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortDot1xPortNumAuthenticatedSupplicants.setStatus(_A)
_ScGenPortDot1xPortNumAuthenticatingSupplicants_Type=Integer32
_ScGenPortDot1xPortNumAuthenticatingSupplicants_Object=MibTableColumn
scGenPortDot1xPortNumAuthenticatingSupplicants=_ScGenPortDot1xPortNumAuthenticatingSupplicants_Object((1,3,6,1,4,1,81,28,1,4,5,1,6),_ScGenPortDot1xPortNumAuthenticatingSupplicants_Type())
scGenPortDot1xPortNumAuthenticatingSupplicants.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortDot1xPortNumAuthenticatingSupplicants.setStatus(_A)
_ScGenSwitch_ObjectIdentity=ObjectIdentity
scGenSwitch=_ScGenSwitch_ObjectIdentity((1,3,6,1,4,1,81,28,1,5))
_ScGenSwitchTable_Object=MibTable
scGenSwitchTable=_ScGenSwitchTable_Object((1,3,6,1,4,1,81,28,1,5,1))
if mibBuilder.loadTexts:scGenSwitchTable.setStatus(_A)
_ScGenSwitchEntry_Object=MibTableRow
scGenSwitchEntry=_ScGenSwitchEntry_Object((1,3,6,1,4,1,81,28,1,5,1,1))
scGenSwitchEntry.setIndexNames((0,_F,_A3))
if mibBuilder.loadTexts:scGenSwitchEntry.setStatus(_A)
class _ScGenSwitchId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ScGenSwitchId_Type.__name__=_C
_ScGenSwitchId_Object=MibTableColumn
scGenSwitchId=_ScGenSwitchId_Object((1,3,6,1,4,1,81,28,1,5,1,1,1),_ScGenSwitchId_Type())
scGenSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenSwitchId.setStatus(_A)
class _ScGenSwitchCopyMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_G,2),(_E,255)))
_ScGenSwitchCopyMode_Type.__name__=_C
_ScGenSwitchCopyMode_Object=MibTableColumn
scGenSwitchCopyMode=_ScGenSwitchCopyMode_Object((1,3,6,1,4,1,81,28,1,5,1,1,2),_ScGenSwitchCopyMode_Type())
scGenSwitchCopyMode.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchCopyMode.setStatus(_A)
_ScGenSwitchCopySource_Type=Integer32
_ScGenSwitchCopySource_Object=MibTableColumn
scGenSwitchCopySource=_ScGenSwitchCopySource_Object((1,3,6,1,4,1,81,28,1,5,1,1,3),_ScGenSwitchCopySource_Type())
scGenSwitchCopySource.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchCopySource.setStatus(_A)
_ScGenSwitchCopyDestination_Type=Integer32
_ScGenSwitchCopyDestination_Object=MibTableColumn
scGenSwitchCopyDestination=_ScGenSwitchCopyDestination_Object((1,3,6,1,4,1,81,28,1,5,1,1,4),_ScGenSwitchCopyDestination_Type())
scGenSwitchCopyDestination.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchCopyDestination.setStatus(_A)
class _ScGenSwitchSetDefaults_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_J,1),(_K,2),(_E,255)))
_ScGenSwitchSetDefaults_Type.__name__=_C
_ScGenSwitchSetDefaults_Object=MibTableColumn
scGenSwitchSetDefaults=_ScGenSwitchSetDefaults_Object((1,3,6,1,4,1,81,28,1,5,1,1,5),_ScGenSwitchSetDefaults_Type())
scGenSwitchSetDefaults.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchSetDefaults.setStatus(_A)
class _ScGenSwitchVIDP_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_G,2),(_E,255)))
_ScGenSwitchVIDP_Type.__name__=_C
_ScGenSwitchVIDP_Object=MibTableColumn
scGenSwitchVIDP=_ScGenSwitchVIDP_Object((1,3,6,1,4,1,81,28,1,5,1,1,6),_ScGenSwitchVIDP_Type())
scGenSwitchVIDP.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchVIDP.setStatus(_A)
class _ScGenSwitchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_O,1),(_f,2),(_E,255)))
_ScGenSwitchType_Type.__name__=_C
_ScGenSwitchType_Object=MibTableColumn
scGenSwitchType=_ScGenSwitchType_Object((1,3,6,1,4,1,81,28,1,5,1,1,7),_ScGenSwitchType_Type())
scGenSwitchType.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenSwitchType.setStatus(_A)
class _ScGenSwitchMasterId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ScGenSwitchMasterId_Type.__name__=_C
_ScGenSwitchMasterId_Object=MibTableColumn
scGenSwitchMasterId=_ScGenSwitchMasterId_Object((1,3,6,1,4,1,81,28,1,5,1,1,8),_ScGenSwitchMasterId_Type())
scGenSwitchMasterId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenSwitchMasterId.setStatus(_A)
class _ScGenSwitchReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_J,1),(_K,2),(_E,255)))
_ScGenSwitchReset_Type.__name__=_C
_ScGenSwitchReset_Object=MibTableColumn
scGenSwitchReset=_ScGenSwitchReset_Object((1,3,6,1,4,1,81,28,1,5,1,1,9),_ScGenSwitchReset_Type())
scGenSwitchReset.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchReset.setStatus(_A)
class _ScGenSwitchNumberOfLoads_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ScGenSwitchNumberOfLoads_Type.__name__=_C
_ScGenSwitchNumberOfLoads_Object=MibTableColumn
scGenSwitchNumberOfLoads=_ScGenSwitchNumberOfLoads_Object((1,3,6,1,4,1,81,28,1,5,1,1,10),_ScGenSwitchNumberOfLoads_Type())
scGenSwitchNumberOfLoads.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenSwitchNumberOfLoads.setStatus(_A)
class _ScGenSwitchAgVLAN_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_ScGenSwitchAgVLAN_Type.__name__=_C
_ScGenSwitchAgVLAN_Object=MibTableColumn
scGenSwitchAgVLAN=_ScGenSwitchAgVLAN_Object((1,3,6,1,4,1,81,28,1,5,1,1,11),_ScGenSwitchAgVLAN_Type())
scGenSwitchAgVLAN.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchAgVLAN.setStatus(_A)
class _ScGenSwitchVLANList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_ScGenSwitchVLANList_Type.__name__=_I
_ScGenSwitchVLANList_Object=MibTableColumn
scGenSwitchVLANList=_ScGenSwitchVLANList_Object((1,3,6,1,4,1,81,28,1,5,1,1,12),_ScGenSwitchVLANList_Type())
scGenSwitchVLANList.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenSwitchVLANList.setStatus(_A)
class _ScGenSwitchSTA_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_G,2),(_E,255)))
_ScGenSwitchSTA_Type.__name__=_C
_ScGenSwitchSTA_Object=MibTableColumn
scGenSwitchSTA=_ScGenSwitchSTA_Object((1,3,6,1,4,1,81,28,1,5,1,1,13),_ScGenSwitchSTA_Type())
scGenSwitchSTA.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchSTA.setStatus(_A)
class _ScGenSwitchSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_S,1),(_T,2),(_E,255)))
_ScGenSwitchSecurityMode_Type.__name__=_C
_ScGenSwitchSecurityMode_Object=MibTableColumn
scGenSwitchSecurityMode=_ScGenSwitchSecurityMode_Object((1,3,6,1,4,1,81,28,1,5,1,1,14),_ScGenSwitchSecurityMode_Type())
scGenSwitchSecurityMode.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchSecurityMode.setStatus(_A)
_ScGenSwitchFindQuery_Type=OctetString
_ScGenSwitchFindQuery_Object=MibTableColumn
scGenSwitchFindQuery=_ScGenSwitchFindQuery_Object((1,3,6,1,4,1,81,28,1,5,1,1,15),_ScGenSwitchFindQuery_Type())
scGenSwitchFindQuery.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchFindQuery.setStatus(_A)
_ScGenSwitchFindResult_Type=OctetString
_ScGenSwitchFindResult_Object=MibTableColumn
scGenSwitchFindResult=_ScGenSwitchFindResult_Object((1,3,6,1,4,1,81,28,1,5,1,1,16),_ScGenSwitchFindResult_Type())
scGenSwitchFindResult.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenSwitchFindResult.setStatus(_A)
_ScGenSwitchSWRdChange_Type=OctetString
_ScGenSwitchSWRdChange_Object=MibTableColumn
scGenSwitchSWRdChange=_ScGenSwitchSWRdChange_Object((1,3,6,1,4,1,81,28,1,5,1,1,17),_ScGenSwitchSWRdChange_Type())
scGenSwitchSWRdChange.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchSWRdChange.setStatus(_A)
class _ScGenSwitchDefaultVLAN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('vlan0',1),('vlan1',2),(_E,255)))
_ScGenSwitchDefaultVLAN_Type.__name__=_C
_ScGenSwitchDefaultVLAN_Object=MibTableColumn
scGenSwitchDefaultVLAN=_ScGenSwitchDefaultVLAN_Object((1,3,6,1,4,1,81,28,1,5,1,1,18),_ScGenSwitchDefaultVLAN_Type())
scGenSwitchDefaultVLAN.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenSwitchDefaultVLAN.setStatus(_A)
class _ScGenSwitchVLANBridging_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_G,2),(_E,255)))
_ScGenSwitchVLANBridging_Type.__name__=_C
_ScGenSwitchVLANBridging_Object=MibTableColumn
scGenSwitchVLANBridging=_ScGenSwitchVLANBridging_Object((1,3,6,1,4,1,81,28,1,5,1,1,19),_ScGenSwitchVLANBridging_Type())
scGenSwitchVLANBridging.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchVLANBridging.setStatus(_A)
class _ScGenSwitchOldVersionModules_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ScGenSwitchOldVersionModules_Type.__name__=_L
_ScGenSwitchOldVersionModules_Object=MibTableColumn
scGenSwitchOldVersionModules=_ScGenSwitchOldVersionModules_Object((1,3,6,1,4,1,81,28,1,5,1,1,20),_ScGenSwitchOldVersionModules_Type())
scGenSwitchOldVersionModules.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenSwitchOldVersionModules.setStatus(_A)
class _ScGenSwitchVIDPNonSupportedModules_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ScGenSwitchVIDPNonSupportedModules_Type.__name__=_L
_ScGenSwitchVIDPNonSupportedModules_Object=MibTableColumn
scGenSwitchVIDPNonSupportedModules=_ScGenSwitchVIDPNonSupportedModules_Object((1,3,6,1,4,1,81,28,1,5,1,1,21),_ScGenSwitchVIDPNonSupportedModules_Type())
scGenSwitchVIDPNonSupportedModules.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenSwitchVIDPNonSupportedModules.setStatus(_A)
class _ScGenSwitchSTANonSupportedModules_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ScGenSwitchSTANonSupportedModules_Type.__name__=_L
_ScGenSwitchSTANonSupportedModules_Object=MibTableColumn
scGenSwitchSTANonSupportedModules=_ScGenSwitchSTANonSupportedModules_Object((1,3,6,1,4,1,81,28,1,5,1,1,22),_ScGenSwitchSTANonSupportedModules_Type())
scGenSwitchSTANonSupportedModules.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenSwitchSTANonSupportedModules.setStatus(_A)
class _ScGenSwitchIDSNonSupportedModules_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ScGenSwitchIDSNonSupportedModules_Type.__name__=_L
_ScGenSwitchIDSNonSupportedModules_Object=MibTableColumn
scGenSwitchIDSNonSupportedModules=_ScGenSwitchIDSNonSupportedModules_Object((1,3,6,1,4,1,81,28,1,5,1,1,23),_ScGenSwitchIDSNonSupportedModules_Type())
scGenSwitchIDSNonSupportedModules.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenSwitchIDSNonSupportedModules.setStatus(_A)
class _ScGenSwitchMcFilter_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_G,2),(_E,255)))
_ScGenSwitchMcFilter_Type.__name__=_C
_ScGenSwitchMcFilter_Object=MibTableColumn
scGenSwitchMcFilter=_ScGenSwitchMcFilter_Object((1,3,6,1,4,1,81,28,1,5,1,1,24),_ScGenSwitchMcFilter_Type())
scGenSwitchMcFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchMcFilter.setStatus(_A)
class _ScGenSwitchMcFilterHostAgingTime_Type(Integer32):defaultValue=600
_ScGenSwitchMcFilterHostAgingTime_Type.__name__=_C
_ScGenSwitchMcFilterHostAgingTime_Object=MibTableColumn
scGenSwitchMcFilterHostAgingTime=_ScGenSwitchMcFilterHostAgingTime_Object((1,3,6,1,4,1,81,28,1,5,1,1,25),_ScGenSwitchMcFilterHostAgingTime_Type())
scGenSwitchMcFilterHostAgingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchMcFilterHostAgingTime.setStatus(_A)
class _ScGenSwitchMcFilterRouterAgingTime_Type(Integer32):defaultValue=1800
_ScGenSwitchMcFilterRouterAgingTime_Type.__name__=_C
_ScGenSwitchMcFilterRouterAgingTime_Object=MibTableColumn
scGenSwitchMcFilterRouterAgingTime=_ScGenSwitchMcFilterRouterAgingTime_Object((1,3,6,1,4,1,81,28,1,5,1,1,26),_ScGenSwitchMcFilterRouterAgingTime_Type())
scGenSwitchMcFilterRouterAgingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchMcFilterRouterAgingTime.setStatus(_A)
class _ScGenSwitchMcFilterDelayTime_Type(Integer32):defaultValue=10
_ScGenSwitchMcFilterDelayTime_Type.__name__=_C
_ScGenSwitchMcFilterDelayTime_Object=MibTableColumn
scGenSwitchMcFilterDelayTime=_ScGenSwitchMcFilterDelayTime_Object((1,3,6,1,4,1,81,28,1,5,1,1,27),_ScGenSwitchMcFilterDelayTime_Type())
scGenSwitchMcFilterDelayTime.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchMcFilterDelayTime.setStatus(_A)
class _ScGenSwitchLACPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_ScGenSwitchLACPMode_Type.__name__=_C
_ScGenSwitchLACPMode_Object=MibTableColumn
scGenSwitchLACPMode=_ScGenSwitchLACPMode_Object((1,3,6,1,4,1,81,28,1,5,1,1,28),_ScGenSwitchLACPMode_Type())
scGenSwitchLACPMode.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchLACPMode.setStatus(_A)
_ScGenSwitchSecurityModePermit_Type=Integer32
_ScGenSwitchSecurityModePermit_Object=MibTableColumn
scGenSwitchSecurityModePermit=_ScGenSwitchSecurityModePermit_Object((1,3,6,1,4,1,81,28,1,5,1,1,29),_ScGenSwitchSecurityModePermit_Type())
scGenSwitchSecurityModePermit.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchSecurityModePermit.setStatus(_A)
class _ScGenSwitchFastAgingOnRemoteTopChg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_q,1),(_r,2),(_E,255)))
_ScGenSwitchFastAgingOnRemoteTopChg_Type.__name__=_C
_ScGenSwitchFastAgingOnRemoteTopChg_Object=MibTableColumn
scGenSwitchFastAgingOnRemoteTopChg=_ScGenSwitchFastAgingOnRemoteTopChg_Object((1,3,6,1,4,1,81,28,1,5,1,1,30),_ScGenSwitchFastAgingOnRemoteTopChg_Type())
scGenSwitchFastAgingOnRemoteTopChg.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchFastAgingOnRemoteTopChg.setStatus(_A)
class _ScGenSwitchGigaMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),('link-load-sharing',2),('primary-bottom',3),('primary-top',4)))
_ScGenSwitchGigaMode_Type.__name__=_C
_ScGenSwitchGigaMode_Object=MibTableColumn
scGenSwitchGigaMode=_ScGenSwitchGigaMode_Object((1,3,6,1,4,1,81,28,1,5,1,1,31),_ScGenSwitchGigaMode_Type())
scGenSwitchGigaMode.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchGigaMode.setStatus(_A)
class _ScGenSwitchCAMClear_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_J,1),(_K,2),(_E,255)))
_ScGenSwitchCAMClear_Type.__name__=_C
_ScGenSwitchCAMClear_Object=MibTableColumn
scGenSwitchCAMClear=_ScGenSwitchCAMClear_Object((1,3,6,1,4,1,81,28,1,5,1,1,32),_ScGenSwitchCAMClear_Type())
scGenSwitchCAMClear.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchCAMClear.setStatus(_A)
class _ScGenSwitchWelcomeMessage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ScGenSwitchWelcomeMessage_Type.__name__=_L
_ScGenSwitchWelcomeMessage_Object=MibTableColumn
scGenSwitchWelcomeMessage=_ScGenSwitchWelcomeMessage_Object((1,3,6,1,4,1,81,28,1,5,1,1,33),_ScGenSwitchWelcomeMessage_Type())
scGenSwitchWelcomeMessage.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchWelcomeMessage.setStatus(_A)
class _ScGenSwitchPromptMessage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ScGenSwitchPromptMessage_Type.__name__=_L
_ScGenSwitchPromptMessage_Object=MibTableColumn
scGenSwitchPromptMessage=_ScGenSwitchPromptMessage_Object((1,3,6,1,4,1,81,28,1,5,1,1,34),_ScGenSwitchPromptMessage_Type())
scGenSwitchPromptMessage.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchPromptMessage.setStatus(_A)
class _ScGenSwitchMacAging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_ScGenSwitchMacAging_Type.__name__=_C
_ScGenSwitchMacAging_Object=MibTableColumn
scGenSwitchMacAging=_ScGenSwitchMacAging_Object((1,3,6,1,4,1,81,28,1,5,1,1,35),_ScGenSwitchMacAging_Type())
scGenSwitchMacAging.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchMacAging.setStatus(_A)
class _ScGenSwitchSecurityAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('drop',1),('dropAndNotify',2),('shutdownAndNotify',3)))
_ScGenSwitchSecurityAction_Type.__name__=_C
_ScGenSwitchSecurityAction_Object=MibTableColumn
scGenSwitchSecurityAction=_ScGenSwitchSecurityAction_Object((1,3,6,1,4,1,81,28,1,5,1,1,36),_ScGenSwitchSecurityAction_Type())
scGenSwitchSecurityAction.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchSecurityAction.setStatus(_A)
class _ScGenSwitchDot1xPortMaxSuppNum_Type(Integer32):defaultValue=2
_ScGenSwitchDot1xPortMaxSuppNum_Type.__name__=_C
_ScGenSwitchDot1xPortMaxSuppNum_Object=MibTableColumn
scGenSwitchDot1xPortMaxSuppNum=_ScGenSwitchDot1xPortMaxSuppNum_Object((1,3,6,1,4,1,81,28,1,5,1,1,37),_ScGenSwitchDot1xPortMaxSuppNum_Type())
scGenSwitchDot1xPortMaxSuppNum.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchDot1xPortMaxSuppNum.setStatus(_A)
class _ScGenSwitchDot1xLldpTxVlanName_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_ScGenSwitchDot1xLldpTxVlanName_Type.__name__=_C
_ScGenSwitchDot1xLldpTxVlanName_Object=MibTableColumn
scGenSwitchDot1xLldpTxVlanName=_ScGenSwitchDot1xLldpTxVlanName_Object((1,3,6,1,4,1,81,28,1,5,1,1,38),_ScGenSwitchDot1xLldpTxVlanName_Type())
scGenSwitchDot1xLldpTxVlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenSwitchDot1xLldpTxVlanName.setStatus(_A)
_ScGenLinkAggregation_ObjectIdentity=ObjectIdentity
scGenLinkAggregation=_ScGenLinkAggregation_ObjectIdentity((1,3,6,1,4,1,81,28,1,6))
_ScGenLinkAggregationTable_Object=MibTable
scGenLinkAggregationTable=_ScGenLinkAggregationTable_Object((1,3,6,1,4,1,81,28,1,6,1))
if mibBuilder.loadTexts:scGenLinkAggregationTable.setStatus(_A)
_ScGenLinkAggregationEntry_Object=MibTableRow
scGenLinkAggregationEntry=_ScGenLinkAggregationEntry_Object((1,3,6,1,4,1,81,28,1,6,1,1))
scGenLinkAggregationEntry.setIndexNames((0,_F,_A4))
if mibBuilder.loadTexts:scGenLinkAggregationEntry.setStatus(_A)
class _ScGenLinkAggregationId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_ScGenLinkAggregationId_Type.__name__=_C
_ScGenLinkAggregationId_Object=MibTableColumn
scGenLinkAggregationId=_ScGenLinkAggregationId_Object((1,3,6,1,4,1,81,28,1,6,1,1,1),_ScGenLinkAggregationId_Type())
scGenLinkAggregationId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenLinkAggregationId.setStatus(_A)
class _ScGenLinkAggregationName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ScGenLinkAggregationName_Type.__name__=_L
_ScGenLinkAggregationName_Object=MibTableColumn
scGenLinkAggregationName=_ScGenLinkAggregationName_Object((1,3,6,1,4,1,81,28,1,6,1,1,2),_ScGenLinkAggregationName_Type())
scGenLinkAggregationName.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenLinkAggregationName.setStatus(_A)
_ScGenLinkAggregationBasePortGroupId_Type=Integer32
_ScGenLinkAggregationBasePortGroupId_Object=MibTableColumn
scGenLinkAggregationBasePortGroupId=_ScGenLinkAggregationBasePortGroupId_Object((1,3,6,1,4,1,81,28,1,6,1,1,3),_ScGenLinkAggregationBasePortGroupId_Type())
scGenLinkAggregationBasePortGroupId.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenLinkAggregationBasePortGroupId.setStatus(_A)
_ScGenLinkAggregationBasePortId_Type=Integer32
_ScGenLinkAggregationBasePortId_Object=MibTableColumn
scGenLinkAggregationBasePortId=_ScGenLinkAggregationBasePortId_Object((1,3,6,1,4,1,81,28,1,6,1,1,4),_ScGenLinkAggregationBasePortId_Type())
scGenLinkAggregationBasePortId.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenLinkAggregationBasePortId.setStatus(_A)
_ScGenLinkAggregationNumberOfPorts_Type=Integer32
_ScGenLinkAggregationNumberOfPorts_Object=MibTableColumn
scGenLinkAggregationNumberOfPorts=_ScGenLinkAggregationNumberOfPorts_Object((1,3,6,1,4,1,81,28,1,6,1,1,5),_ScGenLinkAggregationNumberOfPorts_Type())
scGenLinkAggregationNumberOfPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenLinkAggregationNumberOfPorts.setStatus(_A)
_ScGenLinkAggregationLogicalPortGroupId_Type=Integer32
_ScGenLinkAggregationLogicalPortGroupId_Object=MibTableColumn
scGenLinkAggregationLogicalPortGroupId=_ScGenLinkAggregationLogicalPortGroupId_Object((1,3,6,1,4,1,81,28,1,6,1,1,6),_ScGenLinkAggregationLogicalPortGroupId_Type())
scGenLinkAggregationLogicalPortGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenLinkAggregationLogicalPortGroupId.setStatus(_A)
_ScGenLinkAggregationLogicalPortId_Type=Integer32
_ScGenLinkAggregationLogicalPortId_Object=MibTableColumn
scGenLinkAggregationLogicalPortId=_ScGenLinkAggregationLogicalPortId_Object((1,3,6,1,4,1,81,28,1,6,1,1,7),_ScGenLinkAggregationLogicalPortId_Type())
scGenLinkAggregationLogicalPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenLinkAggregationLogicalPortId.setStatus(_A)
class _ScGenLinkAggregationFunctionalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*((_M,1),(_V,2),('partialFail',3),(_E,255)))
_ScGenLinkAggregationFunctionalStatus_Type.__name__=_C
_ScGenLinkAggregationFunctionalStatus_Object=MibTableColumn
scGenLinkAggregationFunctionalStatus=_ScGenLinkAggregationFunctionalStatus_Object((1,3,6,1,4,1,81,28,1,6,1,1,8),_ScGenLinkAggregationFunctionalStatus_Type())
scGenLinkAggregationFunctionalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenLinkAggregationFunctionalStatus.setStatus(_A)
class _ScGenLinkAggregationAutoNegResults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_M,1),('autoNegInconsistantResults',2),(_E,255)))
_ScGenLinkAggregationAutoNegResults_Type.__name__=_C
_ScGenLinkAggregationAutoNegResults_Object=MibTableColumn
scGenLinkAggregationAutoNegResults=_ScGenLinkAggregationAutoNegResults_Object((1,3,6,1,4,1,81,28,1,6,1,1,9),_ScGenLinkAggregationAutoNegResults_Type())
scGenLinkAggregationAutoNegResults.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenLinkAggregationAutoNegResults.setStatus(_A)
_ScGenLinkAggregationFaultMask_Type=OctetString
_ScGenLinkAggregationFaultMask_Object=MibTableColumn
scGenLinkAggregationFaultMask=_ScGenLinkAggregationFaultMask_Object((1,3,6,1,4,1,81,28,1,6,1,1,10),_ScGenLinkAggregationFaultMask_Type())
scGenLinkAggregationFaultMask.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenLinkAggregationFaultMask.setStatus(_A)
_ScGenLinkAggregationStatus_Type=RowStatus
_ScGenLinkAggregationStatus_Object=MibTableColumn
scGenLinkAggregationStatus=_ScGenLinkAggregationStatus_Object((1,3,6,1,4,1,81,28,1,6,1,1,11),_ScGenLinkAggregationStatus_Type())
scGenLinkAggregationStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenLinkAggregationStatus.setStatus(_A)
_ScGenPortIPAddressRsp_ObjectIdentity=ObjectIdentity
scGenPortIPAddressRsp=_ScGenPortIPAddressRsp_ObjectIdentity((1,3,6,1,4,1,81,28,1,7))
_ScGenPortIPAddressRspTable_Object=MibTable
scGenPortIPAddressRspTable=_ScGenPortIPAddressRspTable_Object((1,3,6,1,4,1,81,28,1,7,1))
if mibBuilder.loadTexts:scGenPortIPAddressRspTable.setStatus(_A)
_ScGenPortIPAddressRspEntry_Object=MibTableRow
scGenPortIPAddressRspEntry=_ScGenPortIPAddressRspEntry_Object((1,3,6,1,4,1,81,28,1,7,1,1))
scGenPortIPAddressRspEntry.setIndexNames((0,_F,_A5),(0,_F,_A6),(0,_F,_A7))
if mibBuilder.loadTexts:scGenPortIPAddressRspEntry.setStatus(_A)
_ScGenPortIPAddressRspGroupId_Type=Integer32
_ScGenPortIPAddressRspGroupId_Object=MibTableColumn
scGenPortIPAddressRspGroupId=_ScGenPortIPAddressRspGroupId_Object((1,3,6,1,4,1,81,28,1,7,1,1,1),_ScGenPortIPAddressRspGroupId_Type())
scGenPortIPAddressRspGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortIPAddressRspGroupId.setStatus(_A)
_ScGenPortIPAddressRspPortId_Type=Integer32
_ScGenPortIPAddressRspPortId_Object=MibTableColumn
scGenPortIPAddressRspPortId=_ScGenPortIPAddressRspPortId_Object((1,3,6,1,4,1,81,28,1,7,1,1,2),_ScGenPortIPAddressRspPortId_Type())
scGenPortIPAddressRspPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortIPAddressRspPortId.setStatus(_A)
_ScGenPortIPAddressRspIpAddressIndex_Type=Integer32
_ScGenPortIPAddressRspIpAddressIndex_Object=MibTableColumn
scGenPortIPAddressRspIpAddressIndex=_ScGenPortIPAddressRspIpAddressIndex_Object((1,3,6,1,4,1,81,28,1,7,1,1,3),_ScGenPortIPAddressRspIpAddressIndex_Type())
scGenPortIPAddressRspIpAddressIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:scGenPortIPAddressRspIpAddressIndex.setStatus(_A)
_ScGenPortIPAddressRspIpAddress_Type=IpAddress
_ScGenPortIPAddressRspIpAddress_Object=MibTableColumn
scGenPortIPAddressRspIpAddress=_ScGenPortIPAddressRspIpAddress_Object((1,3,6,1,4,1,81,28,1,7,1,1,4),_ScGenPortIPAddressRspIpAddress_Type())
scGenPortIPAddressRspIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:scGenPortIPAddressRspIpAddress.setStatus(_A)
_ScEth_ObjectIdentity=ObjectIdentity
scEth=_ScEth_ObjectIdentity((1,3,6,1,4,1,81,28,2))
_ScEthPort_ObjectIdentity=ObjectIdentity
scEthPort=_ScEthPort_ObjectIdentity((1,3,6,1,4,1,81,28,2,1))
_ScEthPortTable_Object=MibTable
scEthPortTable=_ScEthPortTable_Object((1,3,6,1,4,1,81,28,2,1,1))
if mibBuilder.loadTexts:scEthPortTable.setStatus(_A)
_ScEthPortEntry_Object=MibTableRow
scEthPortEntry=_ScEthPortEntry_Object((1,3,6,1,4,1,81,28,2,1,1,1))
scEthPortEntry.setIndexNames((0,_F,_A8),(0,_F,_A9))
if mibBuilder.loadTexts:scEthPortEntry.setStatus(_A)
_ScEthPortGroupId_Type=Integer32
_ScEthPortGroupId_Object=MibTableColumn
scEthPortGroupId=_ScEthPortGroupId_Object((1,3,6,1,4,1,81,28,2,1,1,1,1),_ScEthPortGroupId_Type())
scEthPortGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortGroupId.setStatus(_A)
_ScEthPortId_Type=Integer32
_ScEthPortId_Object=MibTableColumn
scEthPortId=_ScEthPortId_Object((1,3,6,1,4,1,81,28,2,1,1,1,2),_ScEthPortId_Type())
scEthPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortId.setStatus(_A)
_ScEthPortOctetsRec_Type=Counter32
_ScEthPortOctetsRec_Object=MibTableColumn
scEthPortOctetsRec=_ScEthPortOctetsRec_Object((1,3,6,1,4,1,81,28,2,1,1,1,3),_ScEthPortOctetsRec_Type())
scEthPortOctetsRec.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortOctetsRec.setStatus(_A)
_ScEthPortPktsRec_Type=Counter32
_ScEthPortPktsRec_Object=MibTableColumn
scEthPortPktsRec=_ScEthPortPktsRec_Object((1,3,6,1,4,1,81,28,2,1,1,1,4),_ScEthPortPktsRec_Type())
scEthPortPktsRec.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortPktsRec.setStatus(_A)
_ScEthPortGoodBroadcastPktsRec_Type=Counter32
_ScEthPortGoodBroadcastPktsRec_Object=MibTableColumn
scEthPortGoodBroadcastPktsRec=_ScEthPortGoodBroadcastPktsRec_Object((1,3,6,1,4,1,81,28,2,1,1,1,5),_ScEthPortGoodBroadcastPktsRec_Type())
scEthPortGoodBroadcastPktsRec.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortGoodBroadcastPktsRec.setStatus(_A)
_ScEthPortGoodMulticastPktsRec_Type=Counter32
_ScEthPortGoodMulticastPktsRec_Object=MibTableColumn
scEthPortGoodMulticastPktsRec=_ScEthPortGoodMulticastPktsRec_Object((1,3,6,1,4,1,81,28,2,1,1,1,6),_ScEthPortGoodMulticastPktsRec_Type())
scEthPortGoodMulticastPktsRec.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortGoodMulticastPktsRec.setStatus(_A)
_ScEthPortCRCAlignErrors_Type=Counter32
_ScEthPortCRCAlignErrors_Object=MibTableColumn
scEthPortCRCAlignErrors=_ScEthPortCRCAlignErrors_Object((1,3,6,1,4,1,81,28,2,1,1,1,7),_ScEthPortCRCAlignErrors_Type())
scEthPortCRCAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortCRCAlignErrors.setStatus(_A)
_ScEthPortOversizePkts_Type=Counter32
_ScEthPortOversizePkts_Object=MibTableColumn
scEthPortOversizePkts=_ScEthPortOversizePkts_Object((1,3,6,1,4,1,81,28,2,1,1,1,8),_ScEthPortOversizePkts_Type())
scEthPortOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortOversizePkts.setStatus(_A)
_ScEthPortFragments_Type=Counter32
_ScEthPortFragments_Object=MibTableColumn
scEthPortFragments=_ScEthPortFragments_Object((1,3,6,1,4,1,81,28,2,1,1,1,9),_ScEthPortFragments_Type())
scEthPortFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortFragments.setStatus(_A)
_ScEthPortJabber_Type=Counter32
_ScEthPortJabber_Object=MibTableColumn
scEthPortJabber=_ScEthPortJabber_Object((1,3,6,1,4,1,81,28,2,1,1,1,10),_ScEthPortJabber_Type())
scEthPortJabber.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortJabber.setStatus(_A)
_ScEthPortCollisions_Type=Counter32
_ScEthPortCollisions_Object=MibTableColumn
scEthPortCollisions=_ScEthPortCollisions_Object((1,3,6,1,4,1,81,28,2,1,1,1,11),_ScEthPortCollisions_Type())
scEthPortCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortCollisions.setStatus(_A)
_ScEthPortPkts64Octets_Type=Counter32
_ScEthPortPkts64Octets_Object=MibTableColumn
scEthPortPkts64Octets=_ScEthPortPkts64Octets_Object((1,3,6,1,4,1,81,28,2,1,1,1,12),_ScEthPortPkts64Octets_Type())
scEthPortPkts64Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortPkts64Octets.setStatus(_A)
_ScEthPortPkts65to127Octets_Type=Counter32
_ScEthPortPkts65to127Octets_Object=MibTableColumn
scEthPortPkts65to127Octets=_ScEthPortPkts65to127Octets_Object((1,3,6,1,4,1,81,28,2,1,1,1,13),_ScEthPortPkts65to127Octets_Type())
scEthPortPkts65to127Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortPkts65to127Octets.setStatus(_A)
_ScEthPortPkts128to255Octets_Type=Counter32
_ScEthPortPkts128to255Octets_Object=MibTableColumn
scEthPortPkts128to255Octets=_ScEthPortPkts128to255Octets_Object((1,3,6,1,4,1,81,28,2,1,1,1,14),_ScEthPortPkts128to255Octets_Type())
scEthPortPkts128to255Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortPkts128to255Octets.setStatus(_A)
_ScEthPortPkts256to511Octets_Type=Counter32
_ScEthPortPkts256to511Octets_Object=MibTableColumn
scEthPortPkts256to511Octets=_ScEthPortPkts256to511Octets_Object((1,3,6,1,4,1,81,28,2,1,1,1,15),_ScEthPortPkts256to511Octets_Type())
scEthPortPkts256to511Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortPkts256to511Octets.setStatus(_A)
_ScEthPortPkts512to1023Octets_Type=Counter32
_ScEthPortPkts512to1023Octets_Object=MibTableColumn
scEthPortPkts512to1023Octets=_ScEthPortPkts512to1023Octets_Object((1,3,6,1,4,1,81,28,2,1,1,1,16),_ScEthPortPkts512to1023Octets_Type())
scEthPortPkts512to1023Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortPkts512to1023Octets.setStatus(_A)
_ScEthPortPkts1024to1518Octets_Type=Counter32
_ScEthPortPkts1024to1518Octets_Object=MibTableColumn
scEthPortPkts1024to1518Octets=_ScEthPortPkts1024to1518Octets_Object((1,3,6,1,4,1,81,28,2,1,1,1,17),_ScEthPortPkts1024to1518Octets_Type())
scEthPortPkts1024to1518Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortPkts1024to1518Octets.setStatus(_A)
_ScEthPortGoodPktsRec_Type=Counter32
_ScEthPortGoodPktsRec_Object=MibTableColumn
scEthPortGoodPktsRec=_ScEthPortGoodPktsRec_Object((1,3,6,1,4,1,81,28,2,1,1,1,18),_ScEthPortGoodPktsRec_Type())
scEthPortGoodPktsRec.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortGoodPktsRec.setStatus(_A)
_ScEthPortBadPkts_Type=Counter32
_ScEthPortBadPkts_Object=MibTableColumn
scEthPortBadPkts=_ScEthPortBadPkts_Object((1,3,6,1,4,1,81,28,2,1,1,1,19),_ScEthPortBadPkts_Type())
scEthPortBadPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortBadPkts.setStatus(_A)
_ScEthPortGoodOctetsRec_Type=Counter32
_ScEthPortGoodOctetsRec_Object=MibTableColumn
scEthPortGoodOctetsRec=_ScEthPortGoodOctetsRec_Object((1,3,6,1,4,1,81,28,2,1,1,1,20),_ScEthPortGoodOctetsRec_Type())
scEthPortGoodOctetsRec.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortGoodOctetsRec.setStatus(_A)
_ScEthPortBadOctets_Type=Counter32
_ScEthPortBadOctets_Object=MibTableColumn
scEthPortBadOctets=_ScEthPortBadOctets_Object((1,3,6,1,4,1,81,28,2,1,1,1,21),_ScEthPortBadOctets_Type())
scEthPortBadOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortBadOctets.setStatus(_A)
_ScEthPortGoodBroadcastOctetsRec_Type=Counter32
_ScEthPortGoodBroadcastOctetsRec_Object=MibTableColumn
scEthPortGoodBroadcastOctetsRec=_ScEthPortGoodBroadcastOctetsRec_Object((1,3,6,1,4,1,81,28,2,1,1,1,22),_ScEthPortGoodBroadcastOctetsRec_Type())
scEthPortGoodBroadcastOctetsRec.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortGoodBroadcastOctetsRec.setStatus(_A)
_ScEthPortGoodMulticastOctetsRec_Type=Counter32
_ScEthPortGoodMulticastOctetsRec_Object=MibTableColumn
scEthPortGoodMulticastOctetsRec=_ScEthPortGoodMulticastOctetsRec_Object((1,3,6,1,4,1,81,28,2,1,1,1,23),_ScEthPortGoodMulticastOctetsRec_Type())
scEthPortGoodMulticastOctetsRec.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortGoodMulticastOctetsRec.setStatus(_A)
_ScEthPortGoodOctetsSent_Type=Counter32
_ScEthPortGoodOctetsSent_Object=MibTableColumn
scEthPortGoodOctetsSent=_ScEthPortGoodOctetsSent_Object((1,3,6,1,4,1,81,28,2,1,1,1,24),_ScEthPortGoodOctetsSent_Type())
scEthPortGoodOctetsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortGoodOctetsSent.setStatus(_A)
_ScEthPortGoodPktsSent_Type=Counter32
_ScEthPortGoodPktsSent_Object=MibTableColumn
scEthPortGoodPktsSent=_ScEthPortGoodPktsSent_Object((1,3,6,1,4,1,81,28,2,1,1,1,25),_ScEthPortGoodPktsSent_Type())
scEthPortGoodPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortGoodPktsSent.setStatus(_A)
_ScEthPortLateCollisions_Type=Counter32
_ScEthPortLateCollisions_Object=MibTableColumn
scEthPortLateCollisions=_ScEthPortLateCollisions_Object((1,3,6,1,4,1,81,28,2,1,1,1,26),_ScEthPortLateCollisions_Type())
scEthPortLateCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortLateCollisions.setStatus(_A)
class _ScEthPortFunctionalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,8,10,11,255)));namedValues=NamedValues(*((_M,1),('rld',2),('rxJabber',3),('partition',8),('remoteFault',10),('rspError',11),(_E,255)))
_ScEthPortFunctionalStatus_Type.__name__=_C
_ScEthPortFunctionalStatus_Object=MibTableColumn
scEthPortFunctionalStatus=_ScEthPortFunctionalStatus_Object((1,3,6,1,4,1,81,28,2,1,1,1,27),_ScEthPortFunctionalStatus_Type())
scEthPortFunctionalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortFunctionalStatus.setStatus(_A)
class _ScEthPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,255)));namedValues=NamedValues(*(('halfDuplex',1),('fullDuplexNoPause',2),('fullDuplexProprietaryFC',3),('fullDuplexISL',4),('fullDuplexFlowControlISL',5),('fullDuplexAsymTxPause',6),('fullDuplexSymPause',7),('fullDuplexAsymRxPause',8),(_E,255)))
_ScEthPortMode_Type.__name__=_C
_ScEthPortMode_Object=MibTableColumn
scEthPortMode=_ScEthPortMode_Object((1,3,6,1,4,1,81,28,2,1,1,1,28),_ScEthPortMode_Type())
scEthPortMode.setMaxAccess(_D)
if mibBuilder.loadTexts:scEthPortMode.setStatus(_A)
class _ScEthPortSpeed_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,255)));namedValues=NamedValues(*((_O,1),('fastEthernet',2),('gigabitEthernet',3),('a155Mbps',4),('a622Mbps',5),(_E,255)))
_ScEthPortSpeed_Type.__name__=_C
_ScEthPortSpeed_Object=MibTableColumn
scEthPortSpeed=_ScEthPortSpeed_Object((1,3,6,1,4,1,81,28,2,1,1,1,29),_ScEthPortSpeed_Type())
scEthPortSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:scEthPortSpeed.setStatus(_A)
class _ScEthPortAutoNegotiation_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_G,2),(_E,255)))
_ScEthPortAutoNegotiation_Type.__name__=_C
_ScEthPortAutoNegotiation_Object=MibTableColumn
scEthPortAutoNegotiation=_ScEthPortAutoNegotiation_Object((1,3,6,1,4,1,81,28,2,1,1,1,30),_ScEthPortAutoNegotiation_Type())
scEthPortAutoNegotiation.setMaxAccess(_D)
if mibBuilder.loadTexts:scEthPortAutoNegotiation.setStatus(_A)
class _ScEthPortAutoNegotiationStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*(('pass',1),(_V,2),(_G,3),('inProgress',4),(_E,255)))
_ScEthPortAutoNegotiationStatus_Type.__name__=_C
_ScEthPortAutoNegotiationStatus_Object=MibTableColumn
scEthPortAutoNegotiationStatus=_ScEthPortAutoNegotiationStatus_Object((1,3,6,1,4,1,81,28,2,1,1,1,31),_ScEthPortAutoNegotiationStatus_Type())
scEthPortAutoNegotiationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortAutoNegotiationStatus.setStatus(_A)
_ScEthPortTotalOctets_Type=Counter32
_ScEthPortTotalOctets_Object=MibTableColumn
scEthPortTotalOctets=_ScEthPortTotalOctets_Object((1,3,6,1,4,1,81,28,2,1,1,1,32),_ScEthPortTotalOctets_Type())
scEthPortTotalOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortTotalOctets.setStatus(_A)
_ScEthPortTotalPkts_Type=Counter32
_ScEthPortTotalPkts_Object=MibTableColumn
scEthPortTotalPkts=_ScEthPortTotalPkts_Object((1,3,6,1,4,1,81,28,2,1,1,1,33),_ScEthPortTotalPkts_Type())
scEthPortTotalPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortTotalPkts.setStatus(_A)
_ScEthPortDropEvents_Type=Counter32
_ScEthPortDropEvents_Object=MibTableColumn
scEthPortDropEvents=_ScEthPortDropEvents_Object((1,3,6,1,4,1,81,28,2,1,1,1,34),_ScEthPortDropEvents_Type())
scEthPortDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortDropEvents.setStatus(_A)
class _ScEthPortGigaPauseStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('noPause',1),('symmetricPause',2),('asymmetricPauseRx',3),(_E,255)))
_ScEthPortGigaPauseStatus_Type.__name__=_C
_ScEthPortGigaPauseStatus_Object=MibTableColumn
scEthPortGigaPauseStatus=_ScEthPortGigaPauseStatus_Object((1,3,6,1,4,1,81,28,2,1,1,1,35),_ScEthPortGigaPauseStatus_Type())
scEthPortGigaPauseStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortGigaPauseStatus.setStatus(_A)
_ScEthPortLower32OctetsRec_Type=Counter32
_ScEthPortLower32OctetsRec_Object=MibTableColumn
scEthPortLower32OctetsRec=_ScEthPortLower32OctetsRec_Object((1,3,6,1,4,1,81,28,2,1,1,1,36),_ScEthPortLower32OctetsRec_Type())
scEthPortLower32OctetsRec.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortLower32OctetsRec.setStatus(_A)
_ScEthPortUpper32OctetsRec_Type=Counter32
_ScEthPortUpper32OctetsRec_Object=MibTableColumn
scEthPortUpper32OctetsRec=_ScEthPortUpper32OctetsRec_Object((1,3,6,1,4,1,81,28,2,1,1,1,37),_ScEthPortUpper32OctetsRec_Type())
scEthPortUpper32OctetsRec.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortUpper32OctetsRec.setStatus(_A)
_ScEthPortLower32OctetsSent_Type=Counter32
_ScEthPortLower32OctetsSent_Object=MibTableColumn
scEthPortLower32OctetsSent=_ScEthPortLower32OctetsSent_Object((1,3,6,1,4,1,81,28,2,1,1,1,38),_ScEthPortLower32OctetsSent_Type())
scEthPortLower32OctetsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortLower32OctetsSent.setStatus(_A)
_ScEthPortUpper32OctetsSent_Type=Counter32
_ScEthPortUpper32OctetsSent_Object=MibTableColumn
scEthPortUpper32OctetsSent=_ScEthPortUpper32OctetsSent_Object((1,3,6,1,4,1,81,28,2,1,1,1,39),_ScEthPortUpper32OctetsSent_Type())
scEthPortUpper32OctetsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortUpper32OctetsSent.setStatus(_A)
_ScEthPortGoodUnicastPktsRec_Type=Counter32
_ScEthPortGoodUnicastPktsRec_Object=MibTableColumn
scEthPortGoodUnicastPktsRec=_ScEthPortGoodUnicastPktsRec_Object((1,3,6,1,4,1,81,28,2,1,1,1,40),_ScEthPortGoodUnicastPktsRec_Type())
scEthPortGoodUnicastPktsRec.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortGoodUnicastPktsRec.setStatus(_A)
_ScEthPortDiscardPktsRec_Type=Counter32
_ScEthPortDiscardPktsRec_Object=MibTableColumn
scEthPortDiscardPktsRec=_ScEthPortDiscardPktsRec_Object((1,3,6,1,4,1,81,28,2,1,1,1,41),_ScEthPortDiscardPktsRec_Type())
scEthPortDiscardPktsRec.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortDiscardPktsRec.setStatus(_A)
_ScEthPortUnicastPktsSent_Type=Counter32
_ScEthPortUnicastPktsSent_Object=MibTableColumn
scEthPortUnicastPktsSent=_ScEthPortUnicastPktsSent_Object((1,3,6,1,4,1,81,28,2,1,1,1,42),_ScEthPortUnicastPktsSent_Type())
scEthPortUnicastPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortUnicastPktsSent.setStatus(_A)
_ScEthPortDiscardPktsSent_Type=Counter32
_ScEthPortDiscardPktsSent_Object=MibTableColumn
scEthPortDiscardPktsSent=_ScEthPortDiscardPktsSent_Object((1,3,6,1,4,1,81,28,2,1,1,1,43),_ScEthPortDiscardPktsSent_Type())
scEthPortDiscardPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortDiscardPktsSent.setStatus(_A)
class _ScEthPortPauseCapabilities_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*((_AA,1),('asymTxFlowControlOnly',2),('symFlowControlOnly',3),('symAndAsymRxFlowControl',4),(_E,255)))
_ScEthPortPauseCapabilities_Type.__name__=_C
_ScEthPortPauseCapabilities_Object=MibTableColumn
scEthPortPauseCapabilities=_ScEthPortPauseCapabilities_Object((1,3,6,1,4,1,81,28,2,1,1,1,44),_ScEthPortPauseCapabilities_Type())
scEthPortPauseCapabilities.setMaxAccess(_D)
if mibBuilder.loadTexts:scEthPortPauseCapabilities.setStatus(_A)
_ScEthPortMulticastPktsSent_Type=Counter32
_ScEthPortMulticastPktsSent_Object=MibTableColumn
scEthPortMulticastPktsSent=_ScEthPortMulticastPktsSent_Object((1,3,6,1,4,1,81,28,2,1,1,1,45),_ScEthPortMulticastPktsSent_Type())
scEthPortMulticastPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortMulticastPktsSent.setStatus(_A)
_ScEthPortUndersizePktsRec_Type=Counter32
_ScEthPortUndersizePktsRec_Object=MibTableColumn
scEthPortUndersizePktsRec=_ScEthPortUndersizePktsRec_Object((1,3,6,1,4,1,81,28,2,1,1,1,46),_ScEthPortUndersizePktsRec_Type())
scEthPortUndersizePktsRec.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthPortUndersizePktsRec.setStatus(_A)
class _ScEthPortFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,255)));namedValues=NamedValues(*((_AA,1),('asymTxFlowControl',2),('symFlowControl',3),('asymRxFlowControl',4),('proprietaryFlowControl',5),(_E,255)))
_ScEthPortFlowControl_Type.__name__=_C
_ScEthPortFlowControl_Object=MibTableColumn
scEthPortFlowControl=_ScEthPortFlowControl_Object((1,3,6,1,4,1,81,28,2,1,1,1,47),_ScEthPortFlowControl_Type())
scEthPortFlowControl.setMaxAccess(_D)
if mibBuilder.loadTexts:scEthPortFlowControl.setStatus(_A)
_ScEthGroup_ObjectIdentity=ObjectIdentity
scEthGroup=_ScEthGroup_ObjectIdentity((1,3,6,1,4,1,81,28,2,2))
_ScEthGroupTable_Object=MibTable
scEthGroupTable=_ScEthGroupTable_Object((1,3,6,1,4,1,81,28,2,2,1))
if mibBuilder.loadTexts:scEthGroupTable.setStatus(_A)
_ScEthGroupEntry_Object=MibTableRow
scEthGroupEntry=_ScEthGroupEntry_Object((1,3,6,1,4,1,81,28,2,2,1,1))
scEthGroupEntry.setIndexNames((0,_F,_AB))
if mibBuilder.loadTexts:scEthGroupEntry.setStatus(_A)
_ScEthGroupId_Type=Integer32
_ScEthGroupId_Object=MibTableColumn
scEthGroupId=_ScEthGroupId_Object((1,3,6,1,4,1,81,28,2,2,1,1,1),_ScEthGroupId_Type())
scEthGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:scEthGroupId.setStatus(_A)
class _ScEthGroupAutoPartitionEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_G,2),(_E,255)))
_ScEthGroupAutoPartitionEnable_Type.__name__=_C
_ScEthGroupAutoPartitionEnable_Object=MibTableColumn
scEthGroupAutoPartitionEnable=_ScEthGroupAutoPartitionEnable_Object((1,3,6,1,4,1,81,28,2,2,1,1,2),_ScEthGroupAutoPartitionEnable_Type())
scEthGroupAutoPartitionEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:scEthGroupAutoPartitionEnable.setStatus(_A)
class _ScEthGroupFefiEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_H,1),(_G,2),(_E,255)))
_ScEthGroupFefiEnable_Type.__name__=_C
_ScEthGroupFefiEnable_Object=MibTableColumn
scEthGroupFefiEnable=_ScEthGroupFefiEnable_Object((1,3,6,1,4,1,81,28,2,2,1,1,3),_ScEthGroupFefiEnable_Type())
scEthGroupFefiEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:scEthGroupFefiEnable.setStatus(_A)
class _ScPowerEthGroupInlineSWversion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_ScPowerEthGroupInlineSWversion_Type.__name__=_I
_ScPowerEthGroupInlineSWversion_Object=MibTableColumn
scPowerEthGroupInlineSWversion=_ScPowerEthGroupInlineSWversion_Object((1,3,6,1,4,1,81,28,2,2,1,1,4),_ScPowerEthGroupInlineSWversion_Type())
scPowerEthGroupInlineSWversion.setMaxAccess(_B)
if mibBuilder.loadTexts:scPowerEthGroupInlineSWversion.setStatus(_A)
_ScPowerEth_ObjectIdentity=ObjectIdentity
scPowerEth=_ScPowerEth_ObjectIdentity((1,3,6,1,4,1,81,28,3))
_ScPowerEthGroupTable_Object=MibTable
scPowerEthGroupTable=_ScPowerEthGroupTable_Object((1,3,6,1,4,1,81,28,3,1))
if mibBuilder.loadTexts:scPowerEthGroupTable.setStatus(_A)
_ScPowerEthGroupEntry_Object=MibTableRow
scPowerEthGroupEntry=_ScPowerEthGroupEntry_Object((1,3,6,1,4,1,81,28,3,1,1))
scPowerEthGroupEntry.setIndexNames((0,_F,_AC))
if mibBuilder.loadTexts:scPowerEthGroupEntry.setStatus(_A)
_ScPowerEthGroupId_Type=Integer32
_ScPowerEthGroupId_Object=MibTableColumn
scPowerEthGroupId=_ScPowerEthGroupId_Object((1,3,6,1,4,1,81,28,3,1,1,1),_ScPowerEthGroupId_Type())
scPowerEthGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:scPowerEthGroupId.setStatus(_A)
_ScPowerEthGroupPsePSPowerFaultErrMsg_Type=DisplayString
_ScPowerEthGroupPsePSPowerFaultErrMsg_Object=MibTableColumn
scPowerEthGroupPsePSPowerFaultErrMsg=_ScPowerEthGroupPsePSPowerFaultErrMsg_Object((1,3,6,1,4,1,81,28,3,1,1,2),_ScPowerEthGroupPsePSPowerFaultErrMsg_Type())
scPowerEthGroupPsePSPowerFaultErrMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:scPowerEthGroupPsePSPowerFaultErrMsg.setStatus(_A)
class _ScPowerEthGroupPseDetectionProcess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('resistive',1),('capacitive',2),('both',3)))
_ScPowerEthGroupPseDetectionProcess_Type.__name__=_C
_ScPowerEthGroupPseDetectionProcess_Object=MibTableColumn
scPowerEthGroupPseDetectionProcess=_ScPowerEthGroupPseDetectionProcess_Object((1,3,6,1,4,1,81,28,3,1,1,3),_ScPowerEthGroupPseDetectionProcess_Type())
scPowerEthGroupPseDetectionProcess.setMaxAccess(_D)
if mibBuilder.loadTexts:scPowerEthGroupPseDetectionProcess.setStatus(_A)
_ScPowerEthPortTable_Object=MibTable
scPowerEthPortTable=_ScPowerEthPortTable_Object((1,3,6,1,4,1,81,28,3,2))
if mibBuilder.loadTexts:scPowerEthPortTable.setStatus(_A)
_ScPowerEthPortEntry_Object=MibTableRow
scPowerEthPortEntry=_ScPowerEthPortEntry_Object((1,3,6,1,4,1,81,28,3,2,1))
scPowerEthPortEntry.setIndexNames((0,_F,_AD),(0,_F,_AE))
if mibBuilder.loadTexts:scPowerEthPortEntry.setStatus(_A)
_ScPowerEthPortGroupId_Type=Integer32
_ScPowerEthPortGroupId_Object=MibTableColumn
scPowerEthPortGroupId=_ScPowerEthPortGroupId_Object((1,3,6,1,4,1,81,28,3,2,1,1),_ScPowerEthPortGroupId_Type())
scPowerEthPortGroupId.setMaxAccess(_N)
if mibBuilder.loadTexts:scPowerEthPortGroupId.setStatus(_A)
_ScPowerEthPortPortId_Type=Integer32
_ScPowerEthPortPortId_Object=MibTableColumn
scPowerEthPortPortId=_ScPowerEthPortPortId_Object((1,3,6,1,4,1,81,28,3,2,1,2),_ScPowerEthPortPortId_Type())
scPowerEthPortPortId.setMaxAccess(_N)
if mibBuilder.loadTexts:scPowerEthPortPortId.setStatus(_A)
_ScPowerEthPortConsumptionPower_Type=Integer32
_ScPowerEthPortConsumptionPower_Object=MibTableColumn
scPowerEthPortConsumptionPower=_ScPowerEthPortConsumptionPower_Object((1,3,6,1,4,1,81,28,3,2,1,3),_ScPowerEthPortConsumptionPower_Type())
scPowerEthPortConsumptionPower.setMaxAccess(_B)
if mibBuilder.loadTexts:scPowerEthPortConsumptionPower.setStatus(_A)
_ScPriorityQueuing_ObjectIdentity=ObjectIdentity
scPriorityQueuing=_ScPriorityQueuing_ObjectIdentity((1,3,6,1,4,1,81,28,4))
_ScPriorityQueuingTable_Object=MibTable
scPriorityQueuingTable=_ScPriorityQueuingTable_Object((1,3,6,1,4,1,81,28,4,1))
if mibBuilder.loadTexts:scPriorityQueuingTable.setStatus(_A)
_ScPriorityQueuingEntry_Object=MibTableRow
scPriorityQueuingEntry=_ScPriorityQueuingEntry_Object((1,3,6,1,4,1,81,28,4,1,1))
scPriorityQueuingEntry.setIndexNames((0,_F,_AF))
if mibBuilder.loadTexts:scPriorityQueuingEntry.setStatus(_A)
class _ScPriorityQueuingModuleID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,21))
_ScPriorityQueuingModuleID_Type.__name__=_C
_ScPriorityQueuingModuleID_Object=MibTableColumn
scPriorityQueuingModuleID=_ScPriorityQueuingModuleID_Object((1,3,6,1,4,1,81,28,4,1,1,1),_ScPriorityQueuingModuleID_Type())
scPriorityQueuingModuleID.setMaxAccess(_B)
if mibBuilder.loadTexts:scPriorityQueuingModuleID.setStatus(_A)
class _ScPriorityQueuingNumberOfQueues_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ScPriorityQueuingNumberOfQueues_Type.__name__=_C
_ScPriorityQueuingNumberOfQueues_Object=MibTableColumn
scPriorityQueuingNumberOfQueues=_ScPriorityQueuingNumberOfQueues_Object((1,3,6,1,4,1,81,28,4,1,1,2),_ScPriorityQueuingNumberOfQueues_Type())
scPriorityQueuingNumberOfQueues.setMaxAccess(_B)
if mibBuilder.loadTexts:scPriorityQueuingNumberOfQueues.setStatus(_A)
class _ScPriorityQueuingExpediteWRRFlg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),('yes',2)))
_ScPriorityQueuingExpediteWRRFlg_Type.__name__=_C
_ScPriorityQueuingExpediteWRRFlg_Object=MibTableColumn
scPriorityQueuingExpediteWRRFlg=_ScPriorityQueuingExpediteWRRFlg_Object((1,3,6,1,4,1,81,28,4,1,1,3),_ScPriorityQueuingExpediteWRRFlg_Type())
scPriorityQueuingExpediteWRRFlg.setMaxAccess(_B)
if mibBuilder.loadTexts:scPriorityQueuingExpediteWRRFlg.setStatus(_A)
class _ScPriorityQueuingModeControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('strictMode',1),('wrrMode',2),('expediteMode',3)))
_ScPriorityQueuingModeControl_Type.__name__=_C
_ScPriorityQueuingModeControl_Object=MibTableColumn
scPriorityQueuingModeControl=_ScPriorityQueuingModeControl_Object((1,3,6,1,4,1,81,28,4,1,1,4),_ScPriorityQueuingModeControl_Type())
scPriorityQueuingModeControl.setMaxAccess(_D)
if mibBuilder.loadTexts:scPriorityQueuingModeControl.setStatus(_A)
class _ScPriorityQueuingDefaultControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ScPriorityQueuingDefaultControl_Type.__name__=_C
_ScPriorityQueuingDefaultControl_Object=MibTableColumn
scPriorityQueuingDefaultControl=_ScPriorityQueuingDefaultControl_Object((1,3,6,1,4,1,81,28,4,1,1,5),_ScPriorityQueuingDefaultControl_Type())
scPriorityQueuingDefaultControl.setMaxAccess(_D)
if mibBuilder.loadTexts:scPriorityQueuingDefaultControl.setStatus(_A)
class _ScPriorityQueuingWRRWeights_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_ScPriorityQueuingWRRWeights_Type.__name__=_I
_ScPriorityQueuingWRRWeights_Object=MibTableColumn
scPriorityQueuingWRRWeights=_ScPriorityQueuingWRRWeights_Object((1,3,6,1,4,1,81,28,4,1,1,6),_ScPriorityQueuingWRRWeights_Type())
scPriorityQueuingWRRWeights.setMaxAccess(_D)
if mibBuilder.loadTexts:scPriorityQueuingWRRWeights.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'RowStatus':RowStatus,'switchChip':switchChip,'scGen':scGen,'scGenChassis':scGenChassis,'scGenChMainAgPosition':scGenChMainAgPosition,'scGenChRedunAgPosition':scGenChRedunAgPosition,'scGenChRedunAgActivityStatus':scGenChRedunAgActivityStatus,'scGenChAgVLAN':scGenChAgVLAN,'scGenMon':scGenMon,'scGenMonTable':scGenMonTable,'scGenMonEntry':scGenMonEntry,_X:scGenMonSwitchId,'scGenMonDropEvents':scGenMonDropEvents,'scGenMonOctets':scGenMonOctets,'scGenMonPkts':scGenMonPkts,'scGenMonGoodBroadcastPkts':scGenMonGoodBroadcastPkts,'scGenMonGoodMulticastPkts':scGenMonGoodMulticastPkts,'scGenMonGoodPkts':scGenMonGoodPkts,'scGenMonBadPkts':scGenMonBadPkts,'scGenMonGoodOctets':scGenMonGoodOctets,'scGenMonBadOctets':scGenMonBadOctets,'scGenMonSmonCapability':scGenMonSmonCapability,'scGenMonMIBCtrMode':scGenMonMIBCtrMode,'scGenMonSwitchVLANList':scGenMonSwitchVLANList,'scGenMonMIBCtrList':scGenMonMIBCtrList,'scGenMonTimeStamp':scGenMonTimeStamp,'scGenMonVlanTimeStamp':scGenMonVlanTimeStamp,'scGenMonPriorityTable':scGenMonPriorityTable,'scGenMonPriorityEntry':scGenMonPriorityEntry,_Y:scGenMonPrioritySwitchId,_Z:scGenMonPriorityId,'scGenMonPriorityGoodPkts':scGenMonPriorityGoodPkts,'scGenMonPriorityGoodOctets':scGenMonPriorityGoodOctets,'scGenMonVLANList':scGenMonVLANList,'scGenMonVLANTable':scGenMonVLANTable,'scGenMonVLANEntry':scGenMonVLANEntry,_a:scGenMonVLANSwitchId,_b:scGenMonVLANId,'scGenMonVLANGoodPkts':scGenMonVLANGoodPkts,'scGenMonVLANGoodOctets':scGenMonVLANGoodOctets,'scGenMonVLANStatsUcastPkts':scGenMonVLANStatsUcastPkts,'scGenMonVLANStatsMcastPkts':scGenMonVLANStatsMcastPkts,'scGenMonVLANStatsBcastPkts':scGenMonVLANStatsBcastPkts,'scGenMonSwitches':scGenMonSwitches,'scHostTimePortCorrTable':scHostTimePortCorrTable,'scHostTimePortCorrEntry':scHostTimePortCorrEntry,'scHostTimeAddress':scHostTimeAddress,_d:scHostTimeCreationOrder,_c:scHostTimeIndex,'scHostTimePortConnection':scHostTimePortConnection,'scGenGroup':scGenGroup,'scGenGroupTable':scGenGroupTable,'scGenGroupEntry':scGenGroupEntry,_e:scGenGroupId,'scGenGroupUseSwitches':scGenGroupUseSwitches,'scGenGroupCopyPortSupport':scGenGroupCopyPortSupport,'scGenGroupXswitchConnection':scGenGroupXswitchConnection,'scGenGroupStatus':scGenGroupStatus,'scGenGroupSwitchType':scGenGroupSwitchType,'scGenGroupNumberOfLoads':scGenGroupNumberOfLoads,'scGenGroupSetDefaults':scGenGroupSetDefaults,'scGenGroupSupportCopyPortList':scGenGroupSupportCopyPortList,'scGenGroupSupportPortCountersList':scGenGroupSupportPortCountersList,'scGenGroupSupportSegCountersList':scGenGroupSupportSegCountersList,'scGenGroupUpLinkType':scGenGroupUpLinkType,'scGenGroupPlugInType':scGenGroupPlugInType,'scGenGroupPlugInDescr':scGenGroupPlugInDescr,'scGenGroupPlugInCS':scGenGroupPlugInCS,'scGenGroupDefaultVLAN':scGenGroupDefaultVLAN,'scGenGroupCascadingType':scGenGroupCascadingType,'scGenGroupCascadingDescr':scGenGroupCascadingDescr,'scGenGroupCascadingCS':scGenGroupCascadingCS,'scGenGroupSupportDstCopyPortList':scGenGroupSupportDstCopyPortList,'scGenGroupBUPSType':scGenGroupBUPSType,'scGenGroupBUPSCS':scGenGroupBUPSCS,'scGenGroupBUPSFansStatus':scGenGroupBUPSFansStatus,'scGenGroupFansStatus':scGenGroupFansStatus,'scGenGroupInternalBuffering':scGenGroupInternalBuffering,'scGenGroupMcFilterBoxSupport':scGenGroupMcFilterBoxSupport,'scGenGroupMcFilterPersonalitySupport':scGenGroupMcFilterPersonalitySupport,'scGenGroupMcFilterStackingSupport':scGenGroupMcFilterStackingSupport,'scGenGroupLACPMode':scGenGroupLACPMode,'scGenGroupSecurityMode':scGenGroupSecurityMode,'scGenGroupBroadcastStormControl':scGenGroupBroadcastStormControl,'scGenGroupBroadcastThreshold':scGenGroupBroadcastThreshold,'scGenGroupPriorityQueuesScheduling':scGenGroupPriorityQueuesScheduling,'scGenGroupBoundedDelay':scGenGroupBoundedDelay,'scGenGroupSLDAdminStatus':scGenGroupSLDAdminStatus,'scGenGroupDynamicVlans':scGenGroupDynamicVlans,'scGenGroupSecurityMacCount':scGenGroupSecurityMacCount,'scGenGroupBUPSAllocatedPower':scGenGroupBUPSAllocatedPower,'scGenGroupSmonTable':scGenGroupSmonTable,'scGenGroupSmonEntry':scGenGroupSmonEntry,_j:scGenGroupSmonGroupId,'scGenGroupSmonCapability':scGenGroupSmonCapability,'scGenGroupSmonVlanList':scGenGroupSmonVlanList,'scGenGroupSmonDropEvents':scGenGroupSmonDropEvents,'scGenGroupSmonGoodBroadcastPkts':scGenGroupSmonGoodBroadcastPkts,'scGenGroupSmonGoodMulticastPkts':scGenGroupSmonGoodMulticastPkts,'scGenGroupSmonGoodPkts':scGenGroupSmonGoodPkts,'scGenGroupSmonBadPkts':scGenGroupSmonBadPkts,'scGenGroupSmonGoodOctets':scGenGroupSmonGoodOctets,'scGenGroupSmonBadOctets':scGenGroupSmonBadOctets,'scGenGroupSmonPkts':scGenGroupSmonPkts,'scGenGroupSmonOctets':scGenGroupSmonOctets,'scGenGroupSmonMIBCtrMode':scGenGroupSmonMIBCtrMode,'scGenGroupVlanTable':scGenGroupVlanTable,'scGenGroupVlanEntry':scGenGroupVlanEntry,_k:scGenGroupVlanGroupId,_l:scGenGroupVlanId,'scGenGroupVlanUcastPkts':scGenGroupVlanUcastPkts,'scGenGroupVlanMcastPkts':scGenGroupVlanMcastPkts,'scGenGroupVlanBcastPkts':scGenGroupVlanBcastPkts,'scGenGroupVlanGoodPkts':scGenGroupVlanGoodPkts,'scGenGroupVlanGoodOctets':scGenGroupVlanGoodOctets,'scGenGroupVlanUcastOctets':scGenGroupVlanUcastOctets,'scGenGroupVlanMcastOctets':scGenGroupVlanMcastOctets,'scGenGroupVlanBcastOctets':scGenGroupVlanBcastOctets,'scGenGroupVlanCurrentEgressPorts':scGenGroupVlanCurrentEgressPorts,'scGenGroupVlanCurrentUntaggedPorts':scGenGroupVlanCurrentUntaggedPorts,'scGenGroupVlanStaticEgressPorts':scGenGroupVlanStaticEgressPorts,'scGenGroupVlanStaticUntaggedPorts':scGenGroupVlanStaticUntaggedPorts,'scGenGroupRspTable':scGenGroupRspTable,'scGenGroupRspEntry':scGenGroupRspEntry,_m:scGenGroupRspGroupId,'scGenGroupRspHelloInterval':scGenGroupRspHelloInterval,'scGenGroupRspDevicePollingInterval':scGenGroupRspDevicePollingInterval,'scGenGroupRspDeviceNotRespondingTimeout':scGenGroupRspDeviceNotRespondingTimeout,'scGenGroupRspSwitchNotRespondingTimeout':scGenGroupRspSwitchNotRespondingTimeout,'scGenGroupRspMoveToForwardingInterval':scGenGroupRspMoveToForwardingInterval,'scGenGroupRspBroadcastArpShortInterval':scGenGroupRspBroadcastArpShortInterval,'scGenGroupRspBroadcastArpShortIntervalNumber':scGenGroupRspBroadcastArpShortIntervalNumber,'scGenGroupRspBroadcastArpLongInterval':scGenGroupRspBroadcastArpLongInterval,'scGenGroupRspPeriodicPingsBoxIpAddress':scGenGroupRspPeriodicPingsBoxIpAddress,'scGenGroupRspPeriodicPingsDestinationIpAddress':scGenGroupRspPeriodicPingsDestinationIpAddress,'scGenGroupRspMode':scGenGroupRspMode,'scGenGroupDot1xTable':scGenGroupDot1xTable,'scGenGroupDot1xEntry':scGenGroupDot1xEntry,_n:scGenGroupDot1xGroupId,'scGenGroupDot1xSystemMaxNumSupplicant':scGenGroupDot1xSystemMaxNumSupplicant,'scGenGroupDot1xCurrentNumSupplicant':scGenGroupDot1xCurrentNumSupplicant,'scGenGroupDot1xCurrentNumAuthenticatedSupplicant':scGenGroupDot1xCurrentNumAuthenticatedSupplicant,'scGenGroupDot1xCurrentNumAuthenticatingSupplicant':scGenGroupDot1xCurrentNumAuthenticatingSupplicant,'scGenPort':scGenPort,'scGenPortTable':scGenPortTable,'scGenPortEntry':scGenPortEntry,_o:scGenPortGroupId,_p:scGenPortId,'scGenPortVLAN':scGenPortVLAN,'scGenPortPriority':scGenPortPriority,'scGenPortSetDefaults':scGenPortSetDefaults,'scGenPortBackbone':scGenPortBackbone,'scGenPortCopyMode':scGenPortCopyMode,'scGenPortCopyDestination':scGenPortCopyDestination,'scGenPortLinkAggregationNumber':scGenPortLinkAggregationNumber,'scGenPortSendBridgedPackets':scGenPortSendBridgedPackets,'scGenPortVLANEgressStaticConfiguration':scGenPortVLANEgressStaticConfiguration,'scGenPortStaticVLANBinding':scGenPortStaticVLANBinding,'scGenPortSecId':scGenPortSecId,'scGenPortMaxLagsOnSec':scGenPortMaxLagsOnSec,'scGenPortGenericTrap':scGenPortGenericTrap,'scGenPortLACPMode':scGenPortLACPMode,'scGenPortLastIntruderSourceAddr':scGenPortLastIntruderSourceAddr,'scGenPortSecurityMode':scGenPortSecurityMode,'scGenPortSTA':scGenPortSTA,'scGenPortLagCapability':scGenPortLagCapability,'scGenPortCapability':scGenPortCapability,'scGenPortSLDAdminStatus':scGenPortSLDAdminStatus,'scGenPortSLDStatus':scGenPortSLDStatus,'scGenPortCopyClassModuleLevel':scGenPortCopyClassModuleLevel,'scGenPortCopyClassStackLevel':scGenPortCopyClassStackLevel,'scGenPortRspTable':scGenPortRspTable,'scGenPortRspEntry':scGenPortRspEntry,_s:scGenPortRspGroupId,_t:scGenPortRspId,'scGenPortRspMode':scGenPortRspMode,'scGenPortSecureMACTable':scGenPortSecureMACTable,'scGenPortSecureMACEntry':scGenPortSecureMACEntry,_u:scGenPortSecureGroupID,_v:scGenPortSecurePortId,_w:scGenPortSecureMAC,'scGenPortSecureMACStatus':scGenPortSecureMACStatus,'scGenPortDot1xMACTable':scGenPortDot1xMACTable,'scGenPortDot1xMACEntry':scGenPortDot1xMACEntry,_x:scGenPortDot1xMACGroupID,_y:scGenPortDot1xMACPortId,_z:scGenPortDot1xMAC,'scGenPortDot1xMACAuthPaeState':scGenPortDot1xMACAuthPaeState,'scGenPortDot1xMACAuthBackendAuthState':scGenPortDot1xMACAuthBackendAuthState,'scGenPortDot1xAuthAuthControlledPortStatus':scGenPortDot1xAuthAuthControlledPortStatus,'scGenPortDot1xPortTable':scGenPortDot1xPortTable,'scGenPortDot1xPortEntry':scGenPortDot1xPortEntry,_A1:scGenPortDot1xPortGroupID,_A2:scGenPortDot1xPortPortId,'scGenPortDot1xPortMode':scGenPortDot1xPortMode,'scGenPortDot1xPortNumSupplicants':scGenPortDot1xPortNumSupplicants,'scGenPortDot1xPortNumAuthenticatedSupplicants':scGenPortDot1xPortNumAuthenticatedSupplicants,'scGenPortDot1xPortNumAuthenticatingSupplicants':scGenPortDot1xPortNumAuthenticatingSupplicants,'scGenSwitch':scGenSwitch,'scGenSwitchTable':scGenSwitchTable,'scGenSwitchEntry':scGenSwitchEntry,_A3:scGenSwitchId,'scGenSwitchCopyMode':scGenSwitchCopyMode,'scGenSwitchCopySource':scGenSwitchCopySource,'scGenSwitchCopyDestination':scGenSwitchCopyDestination,'scGenSwitchSetDefaults':scGenSwitchSetDefaults,'scGenSwitchVIDP':scGenSwitchVIDP,'scGenSwitchType':scGenSwitchType,'scGenSwitchMasterId':scGenSwitchMasterId,'scGenSwitchReset':scGenSwitchReset,'scGenSwitchNumberOfLoads':scGenSwitchNumberOfLoads,'scGenSwitchAgVLAN':scGenSwitchAgVLAN,'scGenSwitchVLANList':scGenSwitchVLANList,'scGenSwitchSTA':scGenSwitchSTA,'scGenSwitchSecurityMode':scGenSwitchSecurityMode,'scGenSwitchFindQuery':scGenSwitchFindQuery,'scGenSwitchFindResult':scGenSwitchFindResult,'scGenSwitchSWRdChange':scGenSwitchSWRdChange,'scGenSwitchDefaultVLAN':scGenSwitchDefaultVLAN,'scGenSwitchVLANBridging':scGenSwitchVLANBridging,'scGenSwitchOldVersionModules':scGenSwitchOldVersionModules,'scGenSwitchVIDPNonSupportedModules':scGenSwitchVIDPNonSupportedModules,'scGenSwitchSTANonSupportedModules':scGenSwitchSTANonSupportedModules,'scGenSwitchIDSNonSupportedModules':scGenSwitchIDSNonSupportedModules,'scGenSwitchMcFilter':scGenSwitchMcFilter,'scGenSwitchMcFilterHostAgingTime':scGenSwitchMcFilterHostAgingTime,'scGenSwitchMcFilterRouterAgingTime':scGenSwitchMcFilterRouterAgingTime,'scGenSwitchMcFilterDelayTime':scGenSwitchMcFilterDelayTime,'scGenSwitchLACPMode':scGenSwitchLACPMode,'scGenSwitchSecurityModePermit':scGenSwitchSecurityModePermit,'scGenSwitchFastAgingOnRemoteTopChg':scGenSwitchFastAgingOnRemoteTopChg,'scGenSwitchGigaMode':scGenSwitchGigaMode,'scGenSwitchCAMClear':scGenSwitchCAMClear,'scGenSwitchWelcomeMessage':scGenSwitchWelcomeMessage,'scGenSwitchPromptMessage':scGenSwitchPromptMessage,'scGenSwitchMacAging':scGenSwitchMacAging,'scGenSwitchSecurityAction':scGenSwitchSecurityAction,'scGenSwitchDot1xPortMaxSuppNum':scGenSwitchDot1xPortMaxSuppNum,'scGenSwitchDot1xLldpTxVlanName':scGenSwitchDot1xLldpTxVlanName,'scGenLinkAggregation':scGenLinkAggregation,'scGenLinkAggregationTable':scGenLinkAggregationTable,'scGenLinkAggregationEntry':scGenLinkAggregationEntry,_A4:scGenLinkAggregationId,'scGenLinkAggregationName':scGenLinkAggregationName,'scGenLinkAggregationBasePortGroupId':scGenLinkAggregationBasePortGroupId,'scGenLinkAggregationBasePortId':scGenLinkAggregationBasePortId,'scGenLinkAggregationNumberOfPorts':scGenLinkAggregationNumberOfPorts,'scGenLinkAggregationLogicalPortGroupId':scGenLinkAggregationLogicalPortGroupId,'scGenLinkAggregationLogicalPortId':scGenLinkAggregationLogicalPortId,'scGenLinkAggregationFunctionalStatus':scGenLinkAggregationFunctionalStatus,'scGenLinkAggregationAutoNegResults':scGenLinkAggregationAutoNegResults,'scGenLinkAggregationFaultMask':scGenLinkAggregationFaultMask,'scGenLinkAggregationStatus':scGenLinkAggregationStatus,'scGenPortIPAddressRsp':scGenPortIPAddressRsp,'scGenPortIPAddressRspTable':scGenPortIPAddressRspTable,'scGenPortIPAddressRspEntry':scGenPortIPAddressRspEntry,_A5:scGenPortIPAddressRspGroupId,_A6:scGenPortIPAddressRspPortId,_A7:scGenPortIPAddressRspIpAddressIndex,'scGenPortIPAddressRspIpAddress':scGenPortIPAddressRspIpAddress,'scEth':scEth,'scEthPort':scEthPort,'scEthPortTable':scEthPortTable,'scEthPortEntry':scEthPortEntry,_A8:scEthPortGroupId,_A9:scEthPortId,'scEthPortOctetsRec':scEthPortOctetsRec,'scEthPortPktsRec':scEthPortPktsRec,'scEthPortGoodBroadcastPktsRec':scEthPortGoodBroadcastPktsRec,'scEthPortGoodMulticastPktsRec':scEthPortGoodMulticastPktsRec,'scEthPortCRCAlignErrors':scEthPortCRCAlignErrors,'scEthPortOversizePkts':scEthPortOversizePkts,'scEthPortFragments':scEthPortFragments,'scEthPortJabber':scEthPortJabber,'scEthPortCollisions':scEthPortCollisions,'scEthPortPkts64Octets':scEthPortPkts64Octets,'scEthPortPkts65to127Octets':scEthPortPkts65to127Octets,'scEthPortPkts128to255Octets':scEthPortPkts128to255Octets,'scEthPortPkts256to511Octets':scEthPortPkts256to511Octets,'scEthPortPkts512to1023Octets':scEthPortPkts512to1023Octets,'scEthPortPkts1024to1518Octets':scEthPortPkts1024to1518Octets,'scEthPortGoodPktsRec':scEthPortGoodPktsRec,'scEthPortBadPkts':scEthPortBadPkts,'scEthPortGoodOctetsRec':scEthPortGoodOctetsRec,'scEthPortBadOctets':scEthPortBadOctets,'scEthPortGoodBroadcastOctetsRec':scEthPortGoodBroadcastOctetsRec,'scEthPortGoodMulticastOctetsRec':scEthPortGoodMulticastOctetsRec,'scEthPortGoodOctetsSent':scEthPortGoodOctetsSent,'scEthPortGoodPktsSent':scEthPortGoodPktsSent,'scEthPortLateCollisions':scEthPortLateCollisions,'scEthPortFunctionalStatus':scEthPortFunctionalStatus,'scEthPortMode':scEthPortMode,'scEthPortSpeed':scEthPortSpeed,'scEthPortAutoNegotiation':scEthPortAutoNegotiation,'scEthPortAutoNegotiationStatus':scEthPortAutoNegotiationStatus,'scEthPortTotalOctets':scEthPortTotalOctets,'scEthPortTotalPkts':scEthPortTotalPkts,'scEthPortDropEvents':scEthPortDropEvents,'scEthPortGigaPauseStatus':scEthPortGigaPauseStatus,'scEthPortLower32OctetsRec':scEthPortLower32OctetsRec,'scEthPortUpper32OctetsRec':scEthPortUpper32OctetsRec,'scEthPortLower32OctetsSent':scEthPortLower32OctetsSent,'scEthPortUpper32OctetsSent':scEthPortUpper32OctetsSent,'scEthPortGoodUnicastPktsRec':scEthPortGoodUnicastPktsRec,'scEthPortDiscardPktsRec':scEthPortDiscardPktsRec,'scEthPortUnicastPktsSent':scEthPortUnicastPktsSent,'scEthPortDiscardPktsSent':scEthPortDiscardPktsSent,'scEthPortPauseCapabilities':scEthPortPauseCapabilities,'scEthPortMulticastPktsSent':scEthPortMulticastPktsSent,'scEthPortUndersizePktsRec':scEthPortUndersizePktsRec,'scEthPortFlowControl':scEthPortFlowControl,'scEthGroup':scEthGroup,'scEthGroupTable':scEthGroupTable,'scEthGroupEntry':scEthGroupEntry,_AB:scEthGroupId,'scEthGroupAutoPartitionEnable':scEthGroupAutoPartitionEnable,'scEthGroupFefiEnable':scEthGroupFefiEnable,'scPowerEthGroupInlineSWversion':scPowerEthGroupInlineSWversion,'scPowerEth':scPowerEth,'scPowerEthGroupTable':scPowerEthGroupTable,'scPowerEthGroupEntry':scPowerEthGroupEntry,_AC:scPowerEthGroupId,'scPowerEthGroupPsePSPowerFaultErrMsg':scPowerEthGroupPsePSPowerFaultErrMsg,'scPowerEthGroupPseDetectionProcess':scPowerEthGroupPseDetectionProcess,'scPowerEthPortTable':scPowerEthPortTable,'scPowerEthPortEntry':scPowerEthPortEntry,_AD:scPowerEthPortGroupId,_AE:scPowerEthPortPortId,'scPowerEthPortConsumptionPower':scPowerEthPortConsumptionPower,'scPriorityQueuing':scPriorityQueuing,'scPriorityQueuingTable':scPriorityQueuingTable,'scPriorityQueuingEntry':scPriorityQueuingEntry,_AF:scPriorityQueuingModuleID,'scPriorityQueuingNumberOfQueues':scPriorityQueuingNumberOfQueues,'scPriorityQueuingExpediteWRRFlg':scPriorityQueuingExpediteWRRFlg,'scPriorityQueuingModeControl':scPriorityQueuingModeControl,'scPriorityQueuingDefaultControl':scPriorityQueuingDefaultControl,'scPriorityQueuingWRRWeights':scPriorityQueuingWRRWeights})