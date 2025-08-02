_AP='tmnxEthTunnelSAPMemberGroup'
_AO='tmnxEthTunnelLEGroup'
_AN='tmnxEthTunnelBaseAPSV8v0Group'
_AM='tmnxEthTunnelBaseConfigV8v0Group'
_AL='tmnxEthTunnelTimeStampV8v0Group'
_AK='tmnxEthTunnelApsSwitchoverAlarm'
_AJ='tmnxEthTunnelApsNoRspClearAlarm'
_AI='tmnxEthTunnelApsNoRspRaiseAlarm'
_AH='tmnxEthTunnelApsPrvsnClearAlarm'
_AG='tmnxEthTunnelApsPrvsnRaiseAlarm'
_AF='tmnxEthTunnelApsCfgClearAlarm'
_AE='tmnxEthTunnelApsCfgRaiseAlarm'
_AD='tmnxEthTunnelLEMbrThreshold'
_AC='tmnxEthTunnelLEPerFpIngQueueing'
_AB='tmnxEthTunnelLEAccessAdaptQos'
_AA='tmnxEthTunnelSAPMemberTagValue'
_A9='tmnxEthTunnelSAPMemberRowStatus'
_A8='tmnxEthTunnelApsCommandExsResult'
_A7='tmnxEthTunnelApsCommandSwitch'
_A6='tmnxEthTunnelApsMemberActTime'
_A5='tmnxEthTunnelApsMemberActCount'
_A4='tmnxEthTunnelApsSwitchoverTime'
_A3='tmnxEthTunnelMemberOperStatus'
_A2='tmnxEthTunnelMemberAdminStatus'
_A1='tmnxEthTunnelMemberDescription'
_A0='tmnxEthTunnelMemberIfCtlTag'
_z='tmnxEthTunnelMemberIfIndex'
_y='tmnxEthTunnelMemberRowStatus'
_x='tmnxEthTunnelRevertTimeCountDn'
_w='tmnxEthTunnelActiveMembers'
_v='tmnxEthTunnelMgmtMemberIfIndex'
_u='tmnxEthTunnelIfIndex'
_t='tmnxEthTunnelHoldUpTimeMember'
_s='tmnxEthTunnelRevertTime'
_r='tmnxEthTunnelProtectionType'
_q='tmnxEthTunnelHoldDownTimeMember'
_p='tmnxEthTunnelRowStatus'
_o='tmnxEthTunnelChassisIndex'
_n='tmnxEthTunnelLETableChanged'
_m='tmnxEthTunnelSAPMbrTblChanged'
_l='tmnxEthTunnelMemberTimeStamp'
_k='tmnxEthTunnelMbrTblLastChanged'
_j='tmnxEthTunnelTimeStamp'
_i='tmnxEthTunnelCfgTblLastChanged'
_h='tmnxEthTunnelApsCommandEntry'
_g='tmnxEthTunnelOperEntry'
_f='TmnxEthTunnelMemberIndex'
_e='TmnxEthTunnelMemberList'
_d='not-accessible'
_c='TmnxEthTunnelIndex'
_b='TmnxAdminState'
_a='TIMETRA-SERV-MIB'
_Z='sapPortId'
_Y='sapEncapValue'
_X='TruthValue'
_W='InterfaceIndexOrZero'
_V='tmnxEthTunnelAPSNotifyGroup'
_U='tmnxEthTunnelBaseAPSGroup'
_T='tmnxEthTunnelBaseMemberGroup'
_S='tmnxEthTunnelBaseOperGroup'
_R='tmnxEthTunnelBaseConfigGroup'
_Q='tmnxEthTunnelTimeStampGroup'
_P='tmnxEthTunnelMemberPrecedence'
_O='seconds'
_N='TmnxEncapVal'
_M='TIMETRA-SAP-MIB'
_L='tmnxEthTunnelApsTxPdu'
_K='tmnxEthTunnelApsRxPdu'
_J='read-write'
_I='tmnxEthTunnelMemberIndex'
_H='Integer32'
_G='tmnxEthTunnelIndex'
_F='Unsigned32'
_E='tmnxEthTunnelApsDefectStatus'
_D='read-create'
_C='read-only'
_B='current'
_A='TIMETRA-ETH-TUNNEL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_W)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_X)
TmnxChassisIndex,=mibBuilder.importSymbols('TIMETRA-CHASSIS-MIB','TmnxChassisIndex')
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
sapEncapValue,sapPortId=mibBuilder.importSymbols(_M,_Y,_Z)
svcId,=mibBuilder.importSymbols(_a,'svcId')
TItemDescription,TmnxAdminState,TmnxEncapVal,TmnxOperState=mibBuilder.importSymbols('TIMETRA-TC-MIB','TItemDescription',_b,_N,'TmnxOperState')
timetraEthTunnelMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,64))
if mibBuilder.loadTexts:timetraEthTunnelMIBModule.setRevisions(('2014-02-01 00:00','2009-02-28 00:00'))
class TmnxEthTunnelIndex(TextualConvention,Unsigned32):status=_B
class TmnxEthTunnelMemberIndex(TextualConvention,Unsigned32):status=_B
class TmnxEthTunnelMemberList(TextualConvention,Bits):status=_B;namedValues=NamedValues(*(('member1',0),('member2',1),('member3',2),('member4',3),('member5',4),('member6',5),('member7',6),('member8',7),('member9',8),('member10',9),('member11',10),('member12',11),('member13',12),('member14',13),('member15',14),('member16',15)))
class TmnxEthTunnelApsPduType(TextualConvention,Unsigned32):status=_B
_TmnxEthTunnelConformance_ObjectIdentity=ObjectIdentity
tmnxEthTunnelConformance=_TmnxEthTunnelConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,64))
_TmnxEthTunnelCompliances_ObjectIdentity=ObjectIdentity
tmnxEthTunnelCompliances=_TmnxEthTunnelCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,64,1))
_TmnxEthTunnelGroups_ObjectIdentity=ObjectIdentity
tmnxEthTunnelGroups=_TmnxEthTunnelGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,64,2))
_TmnxEthTunnelTSGroups_ObjectIdentity=ObjectIdentity
tmnxEthTunnelTSGroups=_TmnxEthTunnelTSGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,64,2,0))
_TmnxEthTunnelConfigGroups_ObjectIdentity=ObjectIdentity
tmnxEthTunnelConfigGroups=_TmnxEthTunnelConfigGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,64,2,1))
_TmnxEthTunnelOperGroups_ObjectIdentity=ObjectIdentity
tmnxEthTunnelOperGroups=_TmnxEthTunnelOperGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,64,2,2))
_TmnxEthTunnelMemberGroups_ObjectIdentity=ObjectIdentity
tmnxEthTunnelMemberGroups=_TmnxEthTunnelMemberGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,64,2,3))
_TmnxEthTunnelAPSGroups_ObjectIdentity=ObjectIdentity
tmnxEthTunnelAPSGroups=_TmnxEthTunnelAPSGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,64,2,4))
_TmnxEthTunnelNotifyGroups_ObjectIdentity=ObjectIdentity
tmnxEthTunnelNotifyGroups=_TmnxEthTunnelNotifyGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,64,2,5))
_TmnxEthTunnelSAPGroups_ObjectIdentity=ObjectIdentity
tmnxEthTunnelSAPGroups=_TmnxEthTunnelSAPGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,64,2,6))
_TmnxEthTunnelLEGroups_ObjectIdentity=ObjectIdentity
tmnxEthTunnelLEGroups=_TmnxEthTunnelLEGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,64,2,7))
_TmnxEthTunnelObjs_ObjectIdentity=ObjectIdentity
tmnxEthTunnelObjs=_TmnxEthTunnelObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,64))
_TmnxEthTunnelConfigTimeStamps_ObjectIdentity=ObjectIdentity
tmnxEthTunnelConfigTimeStamps=_TmnxEthTunnelConfigTimeStamps_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,64,0))
_TmnxEthTunnelCfgTblLastChanged_Type=TimeStamp
_TmnxEthTunnelCfgTblLastChanged_Object=MibScalar
tmnxEthTunnelCfgTblLastChanged=_TmnxEthTunnelCfgTblLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,64,0,1),_TmnxEthTunnelCfgTblLastChanged_Type())
tmnxEthTunnelCfgTblLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthTunnelCfgTblLastChanged.setStatus(_B)
_TmnxEthTunnelMbrTblLastChanged_Type=TimeStamp
_TmnxEthTunnelMbrTblLastChanged_Object=MibScalar
tmnxEthTunnelMbrTblLastChanged=_TmnxEthTunnelMbrTblLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,64,0,2),_TmnxEthTunnelMbrTblLastChanged_Type())
tmnxEthTunnelMbrTblLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthTunnelMbrTblLastChanged.setStatus(_B)
_TmnxEthTunnelLETableChanged_Type=TimeStamp
_TmnxEthTunnelLETableChanged_Object=MibScalar
tmnxEthTunnelLETableChanged=_TmnxEthTunnelLETableChanged_Object((1,3,6,1,4,1,6527,3,1,2,64,0,3),_TmnxEthTunnelLETableChanged_Type())
tmnxEthTunnelLETableChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthTunnelLETableChanged.setStatus(_B)
_TmnxEthTunnelSAPMbrTblChanged_Type=TimeStamp
_TmnxEthTunnelSAPMbrTblChanged_Object=MibScalar
tmnxEthTunnelSAPMbrTblChanged=_TmnxEthTunnelSAPMbrTblChanged_Object((1,3,6,1,4,1,6527,3,1,2,64,0,4),_TmnxEthTunnelSAPMbrTblChanged_Type())
tmnxEthTunnelSAPMbrTblChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthTunnelSAPMbrTblChanged.setStatus(_B)
_TmnxEthTunnelConfigurations_ObjectIdentity=ObjectIdentity
tmnxEthTunnelConfigurations=_TmnxEthTunnelConfigurations_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,64,1))
_TmnxEthTunnelConfigTable_Object=MibTable
tmnxEthTunnelConfigTable=_TmnxEthTunnelConfigTable_Object((1,3,6,1,4,1,6527,3,1,2,64,1,1))
if mibBuilder.loadTexts:tmnxEthTunnelConfigTable.setStatus(_B)
_TmnxEthTunnelConfigEntry_Object=MibTableRow
tmnxEthTunnelConfigEntry=_TmnxEthTunnelConfigEntry_Object((1,3,6,1,4,1,6527,3,1,2,64,1,1,1))
tmnxEthTunnelConfigEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:tmnxEthTunnelConfigEntry.setStatus(_B)
class _TmnxEthTunnelIndex_Type(TmnxEthTunnelIndex):subtypeSpec=TmnxEthTunnelIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TmnxEthTunnelIndex_Type.__name__=_c
_TmnxEthTunnelIndex_Object=MibTableColumn
tmnxEthTunnelIndex=_TmnxEthTunnelIndex_Object((1,3,6,1,4,1,6527,3,1,2,64,1,1,1,1),_TmnxEthTunnelIndex_Type())
tmnxEthTunnelIndex.setMaxAccess(_d)
if mibBuilder.loadTexts:tmnxEthTunnelIndex.setStatus(_B)
_TmnxEthTunnelRowStatus_Type=RowStatus
_TmnxEthTunnelRowStatus_Object=MibTableColumn
tmnxEthTunnelRowStatus=_TmnxEthTunnelRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,64,1,1,1,2),_TmnxEthTunnelRowStatus_Type())
tmnxEthTunnelRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthTunnelRowStatus.setStatus(_B)
_TmnxEthTunnelTimeStamp_Type=TimeStamp
_TmnxEthTunnelTimeStamp_Object=MibTableColumn
tmnxEthTunnelTimeStamp=_TmnxEthTunnelTimeStamp_Object((1,3,6,1,4,1,6527,3,1,2,64,1,1,1,3),_TmnxEthTunnelTimeStamp_Type())
tmnxEthTunnelTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthTunnelTimeStamp.setStatus(_B)
class _TmnxEthTunnelHoldDownTimeMember_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_TmnxEthTunnelHoldDownTimeMember_Type.__name__=_F
_TmnxEthTunnelHoldDownTimeMember_Object=MibTableColumn
tmnxEthTunnelHoldDownTimeMember=_TmnxEthTunnelHoldDownTimeMember_Object((1,3,6,1,4,1,6527,3,1,2,64,1,1,1,4),_TmnxEthTunnelHoldDownTimeMember_Type())
tmnxEthTunnelHoldDownTimeMember.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthTunnelHoldDownTimeMember.setStatus(_B)
if mibBuilder.loadTexts:tmnxEthTunnelHoldDownTimeMember.setUnits('centiseconds')
class _TmnxEthTunnelProtectionType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('g8031-1to1',1),('loadsharing',2)))
_TmnxEthTunnelProtectionType_Type.__name__=_H
_TmnxEthTunnelProtectionType_Object=MibTableColumn
tmnxEthTunnelProtectionType=_TmnxEthTunnelProtectionType_Object((1,3,6,1,4,1,6527,3,1,2,64,1,1,1,5),_TmnxEthTunnelProtectionType_Type())
tmnxEthTunnelProtectionType.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthTunnelProtectionType.setStatus(_B)
class _TmnxEthTunnelRevertTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,720))
_TmnxEthTunnelRevertTime_Type.__name__=_F
_TmnxEthTunnelRevertTime_Object=MibTableColumn
tmnxEthTunnelRevertTime=_TmnxEthTunnelRevertTime_Object((1,3,6,1,4,1,6527,3,1,2,64,1,1,1,6),_TmnxEthTunnelRevertTime_Type())
tmnxEthTunnelRevertTime.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthTunnelRevertTime.setStatus(_B)
if mibBuilder.loadTexts:tmnxEthTunnelRevertTime.setUnits(_O)
class _TmnxEthTunnelHoldUpTimeMember_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_TmnxEthTunnelHoldUpTimeMember_Type.__name__=_F
_TmnxEthTunnelHoldUpTimeMember_Object=MibTableColumn
tmnxEthTunnelHoldUpTimeMember=_TmnxEthTunnelHoldUpTimeMember_Object((1,3,6,1,4,1,6527,3,1,2,64,1,1,1,7),_TmnxEthTunnelHoldUpTimeMember_Type())
tmnxEthTunnelHoldUpTimeMember.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthTunnelHoldUpTimeMember.setStatus(_B)
if mibBuilder.loadTexts:tmnxEthTunnelHoldUpTimeMember.setUnits('deciseconds')
_TmnxEthTunnelOperTable_Object=MibTable
tmnxEthTunnelOperTable=_TmnxEthTunnelOperTable_Object((1,3,6,1,4,1,6527,3,1,2,64,1,2))
if mibBuilder.loadTexts:tmnxEthTunnelOperTable.setStatus(_B)
_TmnxEthTunnelOperEntry_Object=MibTableRow
tmnxEthTunnelOperEntry=_TmnxEthTunnelOperEntry_Object((1,3,6,1,4,1,6527,3,1,2,64,1,2,1))
if mibBuilder.loadTexts:tmnxEthTunnelOperEntry.setStatus(_B)
_TmnxEthTunnelChassisIndex_Type=TmnxChassisIndex
_TmnxEthTunnelChassisIndex_Object=MibTableColumn
tmnxEthTunnelChassisIndex=_TmnxEthTunnelChassisIndex_Object((1,3,6,1,4,1,6527,3,1,2,64,1,2,1,1),_TmnxEthTunnelChassisIndex_Type())
tmnxEthTunnelChassisIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthTunnelChassisIndex.setStatus(_B)
_TmnxEthTunnelIfIndex_Type=InterfaceIndexOrZero
_TmnxEthTunnelIfIndex_Object=MibTableColumn
tmnxEthTunnelIfIndex=_TmnxEthTunnelIfIndex_Object((1,3,6,1,4,1,6527,3,1,2,64,1,2,1,2),_TmnxEthTunnelIfIndex_Type())
tmnxEthTunnelIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthTunnelIfIndex.setStatus(_B)
_TmnxEthTunnelMgmtMemberIfIndex_Type=InterfaceIndexOrZero
_TmnxEthTunnelMgmtMemberIfIndex_Object=MibTableColumn
tmnxEthTunnelMgmtMemberIfIndex=_TmnxEthTunnelMgmtMemberIfIndex_Object((1,3,6,1,4,1,6527,3,1,2,64,1,2,1,3),_TmnxEthTunnelMgmtMemberIfIndex_Type())
tmnxEthTunnelMgmtMemberIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthTunnelMgmtMemberIfIndex.setStatus(_B)
class _TmnxEthTunnelActiveMembers_Type(TmnxEthTunnelMemberList):defaultBinValue='0'
_TmnxEthTunnelActiveMembers_Type.__name__=_e
_TmnxEthTunnelActiveMembers_Object=MibTableColumn
tmnxEthTunnelActiveMembers=_TmnxEthTunnelActiveMembers_Object((1,3,6,1,4,1,6527,3,1,2,64,1,2,1,4),_TmnxEthTunnelActiveMembers_Type())
tmnxEthTunnelActiveMembers.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthTunnelActiveMembers.setStatus(_B)
_TmnxEthTunnelRevertTimeCountDn_Type=Unsigned32
_TmnxEthTunnelRevertTimeCountDn_Object=MibTableColumn
tmnxEthTunnelRevertTimeCountDn=_TmnxEthTunnelRevertTimeCountDn_Object((1,3,6,1,4,1,6527,3,1,2,64,1,2,1,5),_TmnxEthTunnelRevertTimeCountDn_Type())
tmnxEthTunnelRevertTimeCountDn.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthTunnelRevertTimeCountDn.setStatus(_B)
if mibBuilder.loadTexts:tmnxEthTunnelRevertTimeCountDn.setUnits(_O)
_TmnxEthTunnelMemberTable_Object=MibTable
tmnxEthTunnelMemberTable=_TmnxEthTunnelMemberTable_Object((1,3,6,1,4,1,6527,3,1,2,64,1,3))
if mibBuilder.loadTexts:tmnxEthTunnelMemberTable.setStatus(_B)
_TmnxEthTunnelMemberEntry_Object=MibTableRow
tmnxEthTunnelMemberEntry=_TmnxEthTunnelMemberEntry_Object((1,3,6,1,4,1,6527,3,1,2,64,1,3,1))
tmnxEthTunnelMemberEntry.setIndexNames((0,_A,_G),(0,_A,_I))
if mibBuilder.loadTexts:tmnxEthTunnelMemberEntry.setStatus(_B)
class _TmnxEthTunnelMemberIndex_Type(TmnxEthTunnelMemberIndex):subtypeSpec=TmnxEthTunnelMemberIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TmnxEthTunnelMemberIndex_Type.__name__=_f
_TmnxEthTunnelMemberIndex_Object=MibTableColumn
tmnxEthTunnelMemberIndex=_TmnxEthTunnelMemberIndex_Object((1,3,6,1,4,1,6527,3,1,2,64,1,3,1,1),_TmnxEthTunnelMemberIndex_Type())
tmnxEthTunnelMemberIndex.setMaxAccess(_d)
if mibBuilder.loadTexts:tmnxEthTunnelMemberIndex.setStatus(_B)
_TmnxEthTunnelMemberRowStatus_Type=RowStatus
_TmnxEthTunnelMemberRowStatus_Object=MibTableColumn
tmnxEthTunnelMemberRowStatus=_TmnxEthTunnelMemberRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,64,1,3,1,2),_TmnxEthTunnelMemberRowStatus_Type())
tmnxEthTunnelMemberRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthTunnelMemberRowStatus.setStatus(_B)
_TmnxEthTunnelMemberTimeStamp_Type=TimeStamp
_TmnxEthTunnelMemberTimeStamp_Object=MibTableColumn
tmnxEthTunnelMemberTimeStamp=_TmnxEthTunnelMemberTimeStamp_Object((1,3,6,1,4,1,6527,3,1,2,64,1,3,1,3),_TmnxEthTunnelMemberTimeStamp_Type())
tmnxEthTunnelMemberTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthTunnelMemberTimeStamp.setStatus(_B)
class _TmnxEthTunnelMemberIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_TmnxEthTunnelMemberIfIndex_Type.__name__=_W
_TmnxEthTunnelMemberIfIndex_Object=MibTableColumn
tmnxEthTunnelMemberIfIndex=_TmnxEthTunnelMemberIfIndex_Object((1,3,6,1,4,1,6527,3,1,2,64,1,3,1,4),_TmnxEthTunnelMemberIfIndex_Type())
tmnxEthTunnelMemberIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthTunnelMemberIfIndex.setStatus(_B)
class _TmnxEthTunnelMemberIfCtlTag_Type(TmnxEncapVal):defaultValue=4294967295
_TmnxEthTunnelMemberIfCtlTag_Type.__name__=_N
_TmnxEthTunnelMemberIfCtlTag_Object=MibTableColumn
tmnxEthTunnelMemberIfCtlTag=_TmnxEthTunnelMemberIfCtlTag_Object((1,3,6,1,4,1,6527,3,1,2,64,1,3,1,5),_TmnxEthTunnelMemberIfCtlTag_Type())
tmnxEthTunnelMemberIfCtlTag.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthTunnelMemberIfCtlTag.setStatus(_B)
_TmnxEthTunnelMemberDescription_Type=TItemDescription
_TmnxEthTunnelMemberDescription_Object=MibTableColumn
tmnxEthTunnelMemberDescription=_TmnxEthTunnelMemberDescription_Object((1,3,6,1,4,1,6527,3,1,2,64,1,3,1,6),_TmnxEthTunnelMemberDescription_Type())
tmnxEthTunnelMemberDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthTunnelMemberDescription.setStatus(_B)
class _TmnxEthTunnelMemberAdminStatus_Type(TmnxAdminState):defaultValue=3
_TmnxEthTunnelMemberAdminStatus_Type.__name__=_b
_TmnxEthTunnelMemberAdminStatus_Object=MibTableColumn
tmnxEthTunnelMemberAdminStatus=_TmnxEthTunnelMemberAdminStatus_Object((1,3,6,1,4,1,6527,3,1,2,64,1,3,1,7),_TmnxEthTunnelMemberAdminStatus_Type())
tmnxEthTunnelMemberAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthTunnelMemberAdminStatus.setStatus(_B)
_TmnxEthTunnelMemberOperStatus_Type=TmnxOperState
_TmnxEthTunnelMemberOperStatus_Object=MibTableColumn
tmnxEthTunnelMemberOperStatus=_TmnxEthTunnelMemberOperStatus_Object((1,3,6,1,4,1,6527,3,1,2,64,1,3,1,8),_TmnxEthTunnelMemberOperStatus_Type())
tmnxEthTunnelMemberOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthTunnelMemberOperStatus.setStatus(_B)
class _TmnxEthTunnelMemberPrecedence_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_TmnxEthTunnelMemberPrecedence_Type.__name__=_F
_TmnxEthTunnelMemberPrecedence_Object=MibTableColumn
tmnxEthTunnelMemberPrecedence=_TmnxEthTunnelMemberPrecedence_Object((1,3,6,1,4,1,6527,3,1,2,64,1,3,1,9),_TmnxEthTunnelMemberPrecedence_Type())
tmnxEthTunnelMemberPrecedence.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthTunnelMemberPrecedence.setStatus(_B)
_TmnxEthTunnelAPSConfigs_ObjectIdentity=ObjectIdentity
tmnxEthTunnelAPSConfigs=_TmnxEthTunnelAPSConfigs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,64,1,4))
_TmnxEthTunnelApsTable_Object=MibTable
tmnxEthTunnelApsTable=_TmnxEthTunnelApsTable_Object((1,3,6,1,4,1,6527,3,1,2,64,1,4,1))
if mibBuilder.loadTexts:tmnxEthTunnelApsTable.setStatus(_B)
_TmnxEthTunnelApsEntry_Object=MibTableRow
tmnxEthTunnelApsEntry=_TmnxEthTunnelApsEntry_Object((1,3,6,1,4,1,6527,3,1,2,64,1,4,1,1))
tmnxEthTunnelApsEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:tmnxEthTunnelApsEntry.setStatus(_B)
_TmnxEthTunnelApsRxPdu_Type=TmnxEthTunnelApsPduType
_TmnxEthTunnelApsRxPdu_Object=MibTableColumn
tmnxEthTunnelApsRxPdu=_TmnxEthTunnelApsRxPdu_Object((1,3,6,1,4,1,6527,3,1,2,64,1,4,1,1,1),_TmnxEthTunnelApsRxPdu_Type())
tmnxEthTunnelApsRxPdu.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthTunnelApsRxPdu.setStatus(_B)
_TmnxEthTunnelApsTxPdu_Type=TmnxEthTunnelApsPduType
_TmnxEthTunnelApsTxPdu_Object=MibTableColumn
tmnxEthTunnelApsTxPdu=_TmnxEthTunnelApsTxPdu_Object((1,3,6,1,4,1,6527,3,1,2,64,1,4,1,1,2),_TmnxEthTunnelApsTxPdu_Type())
tmnxEthTunnelApsTxPdu.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthTunnelApsTxPdu.setStatus(_B)
class _TmnxEthTunnelApsDefectStatus_Type(Bits):namedValues=NamedValues(*(('dFopCM',0),('dFopPM',1),('dFopNR',2)))
_TmnxEthTunnelApsDefectStatus_Type.__name__='Bits'
_TmnxEthTunnelApsDefectStatus_Object=MibTableColumn
tmnxEthTunnelApsDefectStatus=_TmnxEthTunnelApsDefectStatus_Object((1,3,6,1,4,1,6527,3,1,2,64,1,4,1,1,3),_TmnxEthTunnelApsDefectStatus_Type())
tmnxEthTunnelApsDefectStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthTunnelApsDefectStatus.setStatus(_B)
_TmnxEthTunnelApsSwitchoverTime_Type=TimeStamp
_TmnxEthTunnelApsSwitchoverTime_Object=MibTableColumn
tmnxEthTunnelApsSwitchoverTime=_TmnxEthTunnelApsSwitchoverTime_Object((1,3,6,1,4,1,6527,3,1,2,64,1,4,1,1,4),_TmnxEthTunnelApsSwitchoverTime_Type())
tmnxEthTunnelApsSwitchoverTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthTunnelApsSwitchoverTime.setStatus(_B)
_TmnxEthTunnelApsMemberTable_Object=MibTable
tmnxEthTunnelApsMemberTable=_TmnxEthTunnelApsMemberTable_Object((1,3,6,1,4,1,6527,3,1,2,64,1,4,2))
if mibBuilder.loadTexts:tmnxEthTunnelApsMemberTable.setStatus(_B)
_TmnxEthTunnelApsMemberEntry_Object=MibTableRow
tmnxEthTunnelApsMemberEntry=_TmnxEthTunnelApsMemberEntry_Object((1,3,6,1,4,1,6527,3,1,2,64,1,4,2,1))
tmnxEthTunnelApsMemberEntry.setIndexNames((0,_A,_G),(0,_A,_I))
if mibBuilder.loadTexts:tmnxEthTunnelApsMemberEntry.setStatus(_B)
_TmnxEthTunnelApsMemberActCount_Type=Counter32
_TmnxEthTunnelApsMemberActCount_Object=MibTableColumn
tmnxEthTunnelApsMemberActCount=_TmnxEthTunnelApsMemberActCount_Object((1,3,6,1,4,1,6527,3,1,2,64,1,4,2,1,1),_TmnxEthTunnelApsMemberActCount_Type())
tmnxEthTunnelApsMemberActCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthTunnelApsMemberActCount.setStatus(_B)
_TmnxEthTunnelApsMemberActTime_Type=Counter32
_TmnxEthTunnelApsMemberActTime_Object=MibTableColumn
tmnxEthTunnelApsMemberActTime=_TmnxEthTunnelApsMemberActTime_Object((1,3,6,1,4,1,6527,3,1,2,64,1,4,2,1,2),_TmnxEthTunnelApsMemberActTime_Type())
tmnxEthTunnelApsMemberActTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthTunnelApsMemberActTime.setStatus(_B)
if mibBuilder.loadTexts:tmnxEthTunnelApsMemberActTime.setUnits(_O)
_TmnxEthTunnelApsCommandTable_Object=MibTable
tmnxEthTunnelApsCommandTable=_TmnxEthTunnelApsCommandTable_Object((1,3,6,1,4,1,6527,3,1,2,64,1,4,3))
if mibBuilder.loadTexts:tmnxEthTunnelApsCommandTable.setStatus(_B)
_TmnxEthTunnelApsCommandEntry_Object=MibTableRow
tmnxEthTunnelApsCommandEntry=_TmnxEthTunnelApsCommandEntry_Object((1,3,6,1,4,1,6527,3,1,2,64,1,4,3,1))
if mibBuilder.loadTexts:tmnxEthTunnelApsCommandEntry.setStatus(_B)
class _TmnxEthTunnelApsCommandSwitch_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('noCmd',0),('clear',1),('lockoutOfSecondary',2),('forceSwitchPrimaryToSecondary',3),('manualSwitchPrimaryToSecondary',4),('exercise',5)))
_TmnxEthTunnelApsCommandSwitch_Type.__name__=_H
_TmnxEthTunnelApsCommandSwitch_Object=MibTableColumn
tmnxEthTunnelApsCommandSwitch=_TmnxEthTunnelApsCommandSwitch_Object((1,3,6,1,4,1,6527,3,1,2,64,1,4,3,1,1),_TmnxEthTunnelApsCommandSwitch_Type())
tmnxEthTunnelApsCommandSwitch.setMaxAccess(_J)
if mibBuilder.loadTexts:tmnxEthTunnelApsCommandSwitch.setStatus(_B)
class _TmnxEthTunnelApsCommandExsResult_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('passed',1),('failed',2),('preempted',3),('unknown',4)))
_TmnxEthTunnelApsCommandExsResult_Type.__name__=_H
_TmnxEthTunnelApsCommandExsResult_Object=MibTableColumn
tmnxEthTunnelApsCommandExsResult=_TmnxEthTunnelApsCommandExsResult_Object((1,3,6,1,4,1,6527,3,1,2,64,1,4,3,1,2),_TmnxEthTunnelApsCommandExsResult_Type())
tmnxEthTunnelApsCommandExsResult.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxEthTunnelApsCommandExsResult.setStatus(_B)
_TmnxEthTunnelLEConfigs_ObjectIdentity=ObjectIdentity
tmnxEthTunnelLEConfigs=_TmnxEthTunnelLEConfigs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,64,1,5))
_TmnxEthTunnelLETable_Object=MibTable
tmnxEthTunnelLETable=_TmnxEthTunnelLETable_Object((1,3,6,1,4,1,6527,3,1,2,64,1,5,1))
if mibBuilder.loadTexts:tmnxEthTunnelLETable.setStatus(_B)
_TmnxEthTunnelLEEntry_Object=MibTableRow
tmnxEthTunnelLEEntry=_TmnxEthTunnelLEEntry_Object((1,3,6,1,4,1,6527,3,1,2,64,1,5,1,1))
tmnxEthTunnelLEEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:tmnxEthTunnelLEEntry.setStatus(_B)
class _TmnxEthTunnelLEAccessAdaptQos_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('link',1),('distribute',2),('portFair',3)))
_TmnxEthTunnelLEAccessAdaptQos_Type.__name__=_H
_TmnxEthTunnelLEAccessAdaptQos_Object=MibTableColumn
tmnxEthTunnelLEAccessAdaptQos=_TmnxEthTunnelLEAccessAdaptQos_Object((1,3,6,1,4,1,6527,3,1,2,64,1,5,1,1,1),_TmnxEthTunnelLEAccessAdaptQos_Type())
tmnxEthTunnelLEAccessAdaptQos.setMaxAccess(_J)
if mibBuilder.loadTexts:tmnxEthTunnelLEAccessAdaptQos.setStatus(_B)
class _TmnxEthTunnelLEPerFpIngQueueing_Type(TruthValue):defaultValue=2
_TmnxEthTunnelLEPerFpIngQueueing_Type.__name__=_X
_TmnxEthTunnelLEPerFpIngQueueing_Object=MibTableColumn
tmnxEthTunnelLEPerFpIngQueueing=_TmnxEthTunnelLEPerFpIngQueueing_Object((1,3,6,1,4,1,6527,3,1,2,64,1,5,1,1,2),_TmnxEthTunnelLEPerFpIngQueueing_Type())
tmnxEthTunnelLEPerFpIngQueueing.setMaxAccess(_J)
if mibBuilder.loadTexts:tmnxEthTunnelLEPerFpIngQueueing.setStatus(_B)
class _TmnxEthTunnelLEMbrThreshold_Type(Unsigned32):defaultValue=0
_TmnxEthTunnelLEMbrThreshold_Type.__name__=_F
_TmnxEthTunnelLEMbrThreshold_Object=MibTableColumn
tmnxEthTunnelLEMbrThreshold=_TmnxEthTunnelLEMbrThreshold_Object((1,3,6,1,4,1,6527,3,1,2,64,1,5,1,1,3),_TmnxEthTunnelLEMbrThreshold_Type())
tmnxEthTunnelLEMbrThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:tmnxEthTunnelLEMbrThreshold.setStatus(_B)
_TmnxEthTunnelSAPConfigs_ObjectIdentity=ObjectIdentity
tmnxEthTunnelSAPConfigs=_TmnxEthTunnelSAPConfigs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,64,1,6))
_TmnxEthTunnelSAPMemberTable_Object=MibTable
tmnxEthTunnelSAPMemberTable=_TmnxEthTunnelSAPMemberTable_Object((1,3,6,1,4,1,6527,3,1,2,64,1,6,1))
if mibBuilder.loadTexts:tmnxEthTunnelSAPMemberTable.setStatus(_B)
_TmnxEthTunnelSAPMemberEntry_Object=MibTableRow
tmnxEthTunnelSAPMemberEntry=_TmnxEthTunnelSAPMemberEntry_Object((1,3,6,1,4,1,6527,3,1,2,64,1,6,1,1))
tmnxEthTunnelSAPMemberEntry.setIndexNames((0,_a,'svcId'),(0,_M,_Z),(0,_M,_Y),(0,_A,_I))
if mibBuilder.loadTexts:tmnxEthTunnelSAPMemberEntry.setStatus(_B)
_TmnxEthTunnelSAPMemberRowStatus_Type=RowStatus
_TmnxEthTunnelSAPMemberRowStatus_Object=MibTableColumn
tmnxEthTunnelSAPMemberRowStatus=_TmnxEthTunnelSAPMemberRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,64,1,6,1,1,1),_TmnxEthTunnelSAPMemberRowStatus_Type())
tmnxEthTunnelSAPMemberRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthTunnelSAPMemberRowStatus.setStatus(_B)
class _TmnxEthTunnelSAPMemberTagValue_Type(TmnxEncapVal):defaultValue=4294967295
_TmnxEthTunnelSAPMemberTagValue_Type.__name__=_N
_TmnxEthTunnelSAPMemberTagValue_Object=MibTableColumn
tmnxEthTunnelSAPMemberTagValue=_TmnxEthTunnelSAPMemberTagValue_Object((1,3,6,1,4,1,6527,3,1,2,64,1,6,1,1,2),_TmnxEthTunnelSAPMemberTagValue_Type())
tmnxEthTunnelSAPMemberTagValue.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxEthTunnelSAPMemberTagValue.setStatus(_B)
_TmnxEthTunnelStatistics_ObjectIdentity=ObjectIdentity
tmnxEthTunnelStatistics=_TmnxEthTunnelStatistics_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,64,2))
_TmnxEthTunnelNotifyPrefix_ObjectIdentity=ObjectIdentity
tmnxEthTunnelNotifyPrefix=_TmnxEthTunnelNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,64))
_TmnxEthTunnelNotifications_ObjectIdentity=ObjectIdentity
tmnxEthTunnelNotifications=_TmnxEthTunnelNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,64,0))
_TmnxEthTunnelApsNotifications_ObjectIdentity=ObjectIdentity
tmnxEthTunnelApsNotifications=_TmnxEthTunnelApsNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,64,0,2))
tmnxEthTunnelConfigEntry.registerAugmentions((_A,_g))
tmnxEthTunnelOperEntry.setIndexNames(*tmnxEthTunnelConfigEntry.getIndexNames())
tmnxEthTunnelApsMemberEntry.registerAugmentions((_A,_h))
tmnxEthTunnelApsCommandEntry.setIndexNames(*tmnxEthTunnelApsMemberEntry.getIndexNames())
tmnxEthTunnelTimeStampGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,64,2,0,1))
tmnxEthTunnelTimeStampGroup.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:tmnxEthTunnelTimeStampGroup.setStatus(_B)
tmnxEthTunnelTimeStampV8v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,64,2,0,2))
tmnxEthTunnelTimeStampV8v0Group.setObjects(*((_A,_m),(_A,_n)))
if mibBuilder.loadTexts:tmnxEthTunnelTimeStampV8v0Group.setStatus(_B)
tmnxEthTunnelBaseConfigGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,64,2,1,1))
tmnxEthTunnelBaseConfigGroup.setObjects(*((_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:tmnxEthTunnelBaseConfigGroup.setStatus(_B)
tmnxEthTunnelBaseConfigV8v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,64,2,1,2))
tmnxEthTunnelBaseConfigV8v0Group.setObjects((_A,_t))
if mibBuilder.loadTexts:tmnxEthTunnelBaseConfigV8v0Group.setStatus(_B)
tmnxEthTunnelBaseOperGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,64,2,2,1))
tmnxEthTunnelBaseOperGroup.setObjects(*((_A,_u),(_A,_v),(_A,_w),(_A,_x)))
if mibBuilder.loadTexts:tmnxEthTunnelBaseOperGroup.setStatus(_B)
tmnxEthTunnelBaseMemberGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,64,2,3,1))
tmnxEthTunnelBaseMemberGroup.setObjects(*((_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_P)))
if mibBuilder.loadTexts:tmnxEthTunnelBaseMemberGroup.setStatus(_B)
tmnxEthTunnelBaseAPSGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,64,2,4,1))
tmnxEthTunnelBaseAPSGroup.setObjects(*((_A,_K),(_A,_L),(_A,_E),(_A,_A4),(_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:tmnxEthTunnelBaseAPSGroup.setStatus(_B)
tmnxEthTunnelBaseAPSV8v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,64,2,4,2))
tmnxEthTunnelBaseAPSV8v0Group.setObjects(*((_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:tmnxEthTunnelBaseAPSV8v0Group.setStatus(_B)
tmnxEthTunnelSAPMemberGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,64,2,6,1))
tmnxEthTunnelSAPMemberGroup.setObjects(*((_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:tmnxEthTunnelSAPMemberGroup.setStatus(_B)
tmnxEthTunnelLEGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,64,2,7,1))
tmnxEthTunnelLEGroup.setObjects(*((_A,_AB),(_A,_AC),(_A,_AD)))
if mibBuilder.loadTexts:tmnxEthTunnelLEGroup.setStatus(_B)
tmnxEthTunnelApsCfgRaiseAlarm=NotificationType((1,3,6,1,4,1,6527,3,1,3,64,0,2,1))
tmnxEthTunnelApsCfgRaiseAlarm.setObjects((_A,_E))
if mibBuilder.loadTexts:tmnxEthTunnelApsCfgRaiseAlarm.setStatus(_B)
tmnxEthTunnelApsCfgClearAlarm=NotificationType((1,3,6,1,4,1,6527,3,1,3,64,0,2,2))
tmnxEthTunnelApsCfgClearAlarm.setObjects((_A,_E))
if mibBuilder.loadTexts:tmnxEthTunnelApsCfgClearAlarm.setStatus(_B)
tmnxEthTunnelApsPrvsnRaiseAlarm=NotificationType((1,3,6,1,4,1,6527,3,1,3,64,0,2,3))
tmnxEthTunnelApsPrvsnRaiseAlarm.setObjects(*((_A,_E),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:tmnxEthTunnelApsPrvsnRaiseAlarm.setStatus(_B)
tmnxEthTunnelApsPrvsnClearAlarm=NotificationType((1,3,6,1,4,1,6527,3,1,3,64,0,2,4))
tmnxEthTunnelApsPrvsnClearAlarm.setObjects(*((_A,_E),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:tmnxEthTunnelApsPrvsnClearAlarm.setStatus(_B)
tmnxEthTunnelApsNoRspRaiseAlarm=NotificationType((1,3,6,1,4,1,6527,3,1,3,64,0,2,5))
tmnxEthTunnelApsNoRspRaiseAlarm.setObjects((_A,_E))
if mibBuilder.loadTexts:tmnxEthTunnelApsNoRspRaiseAlarm.setStatus(_B)
tmnxEthTunnelApsNoRspClearAlarm=NotificationType((1,3,6,1,4,1,6527,3,1,3,64,0,2,6))
tmnxEthTunnelApsNoRspClearAlarm.setObjects((_A,_E))
if mibBuilder.loadTexts:tmnxEthTunnelApsNoRspClearAlarm.setStatus(_B)
tmnxEthTunnelApsSwitchoverAlarm=NotificationType((1,3,6,1,4,1,6527,3,1,3,64,0,2,7))
tmnxEthTunnelApsSwitchoverAlarm.setObjects((_A,_P))
if mibBuilder.loadTexts:tmnxEthTunnelApsSwitchoverAlarm.setStatus(_B)
tmnxEthTunnelAPSNotifyGroup=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,64,2,5,1))
tmnxEthTunnelAPSNotifyGroup.setObjects(*((_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:tmnxEthTunnelAPSNotifyGroup.setStatus(_B)
tmnxEthTunnelCompliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,64,1,1))
tmnxEthTunnelCompliance.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:tmnxEthTunnelCompliance.setStatus('obsolete')
tmnxEthTunnelV8v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,64,1,2))
tmnxEthTunnelV8v0Compliance.setObjects(*((_A,_Q),(_A,_AL),(_A,_R),(_A,_AM),(_A,_S),(_A,_T),(_A,_U),(_A,_AN),(_A,_V),(_A,_AO),(_A,_AP)))
if mibBuilder.loadTexts:tmnxEthTunnelV8v0Compliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_c:TmnxEthTunnelIndex,_f:TmnxEthTunnelMemberIndex,_e:TmnxEthTunnelMemberList,'TmnxEthTunnelApsPduType':TmnxEthTunnelApsPduType,'timetraEthTunnelMIBModule':timetraEthTunnelMIBModule,'tmnxEthTunnelConformance':tmnxEthTunnelConformance,'tmnxEthTunnelCompliances':tmnxEthTunnelCompliances,'tmnxEthTunnelCompliance':tmnxEthTunnelCompliance,'tmnxEthTunnelV8v0Compliance':tmnxEthTunnelV8v0Compliance,'tmnxEthTunnelGroups':tmnxEthTunnelGroups,'tmnxEthTunnelTSGroups':tmnxEthTunnelTSGroups,_Q:tmnxEthTunnelTimeStampGroup,_AL:tmnxEthTunnelTimeStampV8v0Group,'tmnxEthTunnelConfigGroups':tmnxEthTunnelConfigGroups,_R:tmnxEthTunnelBaseConfigGroup,_AM:tmnxEthTunnelBaseConfigV8v0Group,'tmnxEthTunnelOperGroups':tmnxEthTunnelOperGroups,_S:tmnxEthTunnelBaseOperGroup,'tmnxEthTunnelMemberGroups':tmnxEthTunnelMemberGroups,_T:tmnxEthTunnelBaseMemberGroup,'tmnxEthTunnelAPSGroups':tmnxEthTunnelAPSGroups,_U:tmnxEthTunnelBaseAPSGroup,_AN:tmnxEthTunnelBaseAPSV8v0Group,'tmnxEthTunnelNotifyGroups':tmnxEthTunnelNotifyGroups,_V:tmnxEthTunnelAPSNotifyGroup,'tmnxEthTunnelSAPGroups':tmnxEthTunnelSAPGroups,_AP:tmnxEthTunnelSAPMemberGroup,'tmnxEthTunnelLEGroups':tmnxEthTunnelLEGroups,_AO:tmnxEthTunnelLEGroup,'tmnxEthTunnelObjs':tmnxEthTunnelObjs,'tmnxEthTunnelConfigTimeStamps':tmnxEthTunnelConfigTimeStamps,_i:tmnxEthTunnelCfgTblLastChanged,_k:tmnxEthTunnelMbrTblLastChanged,_n:tmnxEthTunnelLETableChanged,_m:tmnxEthTunnelSAPMbrTblChanged,'tmnxEthTunnelConfigurations':tmnxEthTunnelConfigurations,'tmnxEthTunnelConfigTable':tmnxEthTunnelConfigTable,'tmnxEthTunnelConfigEntry':tmnxEthTunnelConfigEntry,_G:tmnxEthTunnelIndex,_p:tmnxEthTunnelRowStatus,_j:tmnxEthTunnelTimeStamp,_q:tmnxEthTunnelHoldDownTimeMember,_r:tmnxEthTunnelProtectionType,_s:tmnxEthTunnelRevertTime,_t:tmnxEthTunnelHoldUpTimeMember,'tmnxEthTunnelOperTable':tmnxEthTunnelOperTable,_g:tmnxEthTunnelOperEntry,_o:tmnxEthTunnelChassisIndex,_u:tmnxEthTunnelIfIndex,_v:tmnxEthTunnelMgmtMemberIfIndex,_w:tmnxEthTunnelActiveMembers,_x:tmnxEthTunnelRevertTimeCountDn,'tmnxEthTunnelMemberTable':tmnxEthTunnelMemberTable,'tmnxEthTunnelMemberEntry':tmnxEthTunnelMemberEntry,_I:tmnxEthTunnelMemberIndex,_y:tmnxEthTunnelMemberRowStatus,_l:tmnxEthTunnelMemberTimeStamp,_z:tmnxEthTunnelMemberIfIndex,_A0:tmnxEthTunnelMemberIfCtlTag,_A1:tmnxEthTunnelMemberDescription,_A2:tmnxEthTunnelMemberAdminStatus,_A3:tmnxEthTunnelMemberOperStatus,_P:tmnxEthTunnelMemberPrecedence,'tmnxEthTunnelAPSConfigs':tmnxEthTunnelAPSConfigs,'tmnxEthTunnelApsTable':tmnxEthTunnelApsTable,'tmnxEthTunnelApsEntry':tmnxEthTunnelApsEntry,_K:tmnxEthTunnelApsRxPdu,_L:tmnxEthTunnelApsTxPdu,_E:tmnxEthTunnelApsDefectStatus,_A4:tmnxEthTunnelApsSwitchoverTime,'tmnxEthTunnelApsMemberTable':tmnxEthTunnelApsMemberTable,'tmnxEthTunnelApsMemberEntry':tmnxEthTunnelApsMemberEntry,_A5:tmnxEthTunnelApsMemberActCount,_A6:tmnxEthTunnelApsMemberActTime,'tmnxEthTunnelApsCommandTable':tmnxEthTunnelApsCommandTable,_h:tmnxEthTunnelApsCommandEntry,_A7:tmnxEthTunnelApsCommandSwitch,_A8:tmnxEthTunnelApsCommandExsResult,'tmnxEthTunnelLEConfigs':tmnxEthTunnelLEConfigs,'tmnxEthTunnelLETable':tmnxEthTunnelLETable,'tmnxEthTunnelLEEntry':tmnxEthTunnelLEEntry,_AB:tmnxEthTunnelLEAccessAdaptQos,_AC:tmnxEthTunnelLEPerFpIngQueueing,_AD:tmnxEthTunnelLEMbrThreshold,'tmnxEthTunnelSAPConfigs':tmnxEthTunnelSAPConfigs,'tmnxEthTunnelSAPMemberTable':tmnxEthTunnelSAPMemberTable,'tmnxEthTunnelSAPMemberEntry':tmnxEthTunnelSAPMemberEntry,_A9:tmnxEthTunnelSAPMemberRowStatus,_AA:tmnxEthTunnelSAPMemberTagValue,'tmnxEthTunnelStatistics':tmnxEthTunnelStatistics,'tmnxEthTunnelNotifyPrefix':tmnxEthTunnelNotifyPrefix,'tmnxEthTunnelNotifications':tmnxEthTunnelNotifications,'tmnxEthTunnelApsNotifications':tmnxEthTunnelApsNotifications,_AE:tmnxEthTunnelApsCfgRaiseAlarm,_AF:tmnxEthTunnelApsCfgClearAlarm,_AG:tmnxEthTunnelApsPrvsnRaiseAlarm,_AH:tmnxEthTunnelApsPrvsnClearAlarm,_AI:tmnxEthTunnelApsNoRspRaiseAlarm,_AJ:tmnxEthTunnelApsNoRspClearAlarm,_AK:tmnxEthTunnelApsSwitchoverAlarm})