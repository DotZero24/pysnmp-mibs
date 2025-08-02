_AN='alaNetSecMonitoringGroup'
_AM='alaNetSecPortTrapsComplianceGroup'
_AL='alaNetSecGroupComplianceGroup'
_AK='alaNetSecGroupOpComplianceGroup'
_AJ='alaNetSecPortOpComplianceGroup'
_AI='alaNetSecPortAnomalySummaryComplianceGroup'
_AH='alaNetSecPortAnomalyStatsComplianceGroup'
_AG='alaNetSecPortStatsComplianceGroup'
_AF='alaNetSecMonitoringGroupComplianceGroup'
_AE='alaNetSecPortRangeComplianceGroup'
_AD='alaNetSecPortTrapQuarantine'
_AC='alaNetSecPortTrapAnomaly'
_AB='alaNetSecPortRangeGroupName'
_AA='alaNetSecMonitoringGroupAnomalyTrap'
_A9='alaNetSecMonitoringGroupAnomalyState'
_A8='alaNetSecMonitoringGroupAnomalySensitivity'
_A7='alaNetSecMonitoringGroupAnomalyQuarantine'
_A6='alaNetSecMonitoringGroupAnomalyPeriod'
_A5='alaNetSecMonitoringGroupAnomalyLog'
_A4='alaNetSecMonitoringGroupAnomalyCount'
_A3='alaNetSecGroupAnomalyCfg'
_A2='alaNetSecGroupMemberPorts'
_A1='alaNetSecGroupOpPeriod'
_A0='alaNetSecGroupOpSensitivity'
_z='alaNetSecGroupOpCount'
_y='alaNetSecGroupOpQuarantine'
_x='alaNetSecGroupOpTrap'
_w='alaNetSecGroupOpLog'
_v='alaNetSecGroupOpState'
_u='alaNetSecPortOpPeriod'
_t='alaNetSecPortOpSensitivity'
_s='alaNetSecPortOpCount'
_r='alaNetSecPortOpQuarantine'
_q='alaNetSecPortOpTrap'
_p='alaNetSecPortOpLog'
_o='alaNetSecPortOpState'
_n='alaNetSecPortAnomalySummaryDetected'
_m='alaNetSecPortAnomalySummaryObserved'
_l='alaNetSecPortAnomalyStatsLastEgress'
_k='alaNetSecPortAnomalyStatsLastIngress'
_j='alaNetSecPortAnomalyStatsCurrentEgress'
_i='alaNetSecPortAnomalyStatsCurrentIngress'
_h='alaNetSecPortStatsTotalEgress'
_g='alaNetSecPortStatsTotalIngress'
_f='alaNetSecPortStatsLastEgress'
_e='alaNetSecPortStatsLastIngress'
_d='alaNetSecMonitoringGroupRowStatus'
_c='alaNetSecPortRangeGroupRowStatus'
_b='alaNetSecGroupName'
_a='alaNetSecGroupOpAnomaly'
_Z='alaNetSecGroupOpName'
_Y='alaNetSecPortOpAnomaly'
_X='alaNetSecPortOpIfId'
_W='alaNetSecPortAnomalySummaryAnomaly'
_V='alaNetSecPortAnomalySummaryIfId'
_U='alaNetSecPortAnomalyStatsPacket'
_T='alaNetSecPortAnomalyStatsAnomaly'
_S='alaNetSecPortAnomalyStatsIfId'
_R='alaNetSecPortStatsPacket'
_Q='alaNetSecPortStatsIfId'
_P='alaNetSecMonitoringGroupAnomaly'
_O='alaNetSecMonitoringGroupName'
_N='alaNetSecPortRangeGroupEndIfId'
_M='alaNetSecPortRangeGroupStartIfId'
_L='alaNetSecPortTrapInfoType'
_K='alaNetSecPortTrapInfoAnomaly'
_J='accessible-for-notify'
_I='alaNetSecPortTrapInfoIfId'
_H='AlaNetsecStatus'
_G='DisplayString'
_F='read-create'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='ALCATEL-IND1-NETSEC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alaNetSecTraps,softentIND1NetSec=mibBuilder.importSymbols('ALCATEL-IND1-BASE','alaNetSecTraps','softentIND1NetSec')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention','TruthValue')
alcatelIND1NETSECMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,48,1))
class AlaAnomalyType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('all',0),('arpaddressscan',1),('arpflood',2),('reserved',3),('arpfailure',4),('icmpaddressscan',5),('icmpflood',6),('icmpunreachable',7),('tcpportscan',8),('tcpaddressscan',9),('synflood',10),('synfailure',11),('synackscan',12),('finscan',13),('finackdiff',14),('rstcount',15)))
class AlaPacketType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('arpreply',1),('arprequest',2),('icmpechoreply',3),('icmpechorequest',4),('icmpdnr',5),('tcpsynonly',6),('tcpsynack',7),('tcpsynnack',8),('tcpfinack',9),('tcpfinnack',10),('tcprst',11)))
class AlaNetsecStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('default',0),('enable',1),('disable',2)))
_AlcatelIND1NETSECMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1NETSECMIBObjects=_AlcatelIND1NETSECMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,48,1,1))
_AlaNetSecPortRangeConfig_ObjectIdentity=ObjectIdentity
alaNetSecPortRangeConfig=_AlaNetSecPortRangeConfig_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,1))
_AlaNetSecPortRangeGroupTable_Object=MibTable
alaNetSecPortRangeGroupTable=_AlaNetSecPortRangeGroupTable_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,1,1))
if mibBuilder.loadTexts:alaNetSecPortRangeGroupTable.setStatus(_A)
_AlaNetSecPortRangeGroupEntry_Object=MibTableRow
alaNetSecPortRangeGroupEntry=_AlaNetSecPortRangeGroupEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,1,1,1))
alaNetSecPortRangeGroupEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:alaNetSecPortRangeGroupEntry.setStatus(_A)
_AlaNetSecPortRangeGroupStartIfId_Type=InterfaceIndex
_AlaNetSecPortRangeGroupStartIfId_Object=MibTableColumn
alaNetSecPortRangeGroupStartIfId=_AlaNetSecPortRangeGroupStartIfId_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,1,1,1,1),_AlaNetSecPortRangeGroupStartIfId_Type())
alaNetSecPortRangeGroupStartIfId.setMaxAccess(_D)
if mibBuilder.loadTexts:alaNetSecPortRangeGroupStartIfId.setStatus(_A)
_AlaNetSecPortRangeGroupEndIfId_Type=InterfaceIndex
_AlaNetSecPortRangeGroupEndIfId_Object=MibTableColumn
alaNetSecPortRangeGroupEndIfId=_AlaNetSecPortRangeGroupEndIfId_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,1,1,1,2),_AlaNetSecPortRangeGroupEndIfId_Type())
alaNetSecPortRangeGroupEndIfId.setMaxAccess(_D)
if mibBuilder.loadTexts:alaNetSecPortRangeGroupEndIfId.setStatus(_A)
class _AlaNetSecPortRangeGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AlaNetSecPortRangeGroupName_Type.__name__=_G
_AlaNetSecPortRangeGroupName_Object=MibTableColumn
alaNetSecPortRangeGroupName=_AlaNetSecPortRangeGroupName_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,1,1,1,3),_AlaNetSecPortRangeGroupName_Type())
alaNetSecPortRangeGroupName.setMaxAccess(_F)
if mibBuilder.loadTexts:alaNetSecPortRangeGroupName.setStatus(_A)
_AlaNetSecPortRangeGroupRowStatus_Type=RowStatus
_AlaNetSecPortRangeGroupRowStatus_Object=MibTableColumn
alaNetSecPortRangeGroupRowStatus=_AlaNetSecPortRangeGroupRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,1,1,1,4),_AlaNetSecPortRangeGroupRowStatus_Type())
alaNetSecPortRangeGroupRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alaNetSecPortRangeGroupRowStatus.setStatus(_A)
_AlaNetSecMonitoringGroupConfig_ObjectIdentity=ObjectIdentity
alaNetSecMonitoringGroupConfig=_AlaNetSecMonitoringGroupConfig_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,2))
_AlaNetSecMonitoringGroupTable_Object=MibTable
alaNetSecMonitoringGroupTable=_AlaNetSecMonitoringGroupTable_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,2,1))
if mibBuilder.loadTexts:alaNetSecMonitoringGroupTable.setStatus(_A)
_AlaNetSecMonitoringGroupEntry_Object=MibTableRow
alaNetSecMonitoringGroupEntry=_AlaNetSecMonitoringGroupEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,2,1,1))
alaNetSecMonitoringGroupEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:alaNetSecMonitoringGroupEntry.setStatus(_A)
class _AlaNetSecMonitoringGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AlaNetSecMonitoringGroupName_Type.__name__=_G
_AlaNetSecMonitoringGroupName_Object=MibTableColumn
alaNetSecMonitoringGroupName=_AlaNetSecMonitoringGroupName_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,2,1,1,1),_AlaNetSecMonitoringGroupName_Type())
alaNetSecMonitoringGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:alaNetSecMonitoringGroupName.setStatus(_A)
_AlaNetSecMonitoringGroupAnomaly_Type=AlaAnomalyType
_AlaNetSecMonitoringGroupAnomaly_Object=MibTableColumn
alaNetSecMonitoringGroupAnomaly=_AlaNetSecMonitoringGroupAnomaly_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,2,1,1,2),_AlaNetSecMonitoringGroupAnomaly_Type())
alaNetSecMonitoringGroupAnomaly.setMaxAccess(_D)
if mibBuilder.loadTexts:alaNetSecMonitoringGroupAnomaly.setStatus(_A)
class _AlaNetSecMonitoringGroupAnomalyState_Type(AlaNetsecStatus):defaultValue=2
_AlaNetSecMonitoringGroupAnomalyState_Type.__name__=_H
_AlaNetSecMonitoringGroupAnomalyState_Object=MibTableColumn
alaNetSecMonitoringGroupAnomalyState=_AlaNetSecMonitoringGroupAnomalyState_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,2,1,1,3),_AlaNetSecMonitoringGroupAnomalyState_Type())
alaNetSecMonitoringGroupAnomalyState.setMaxAccess(_F)
if mibBuilder.loadTexts:alaNetSecMonitoringGroupAnomalyState.setStatus(_A)
class _AlaNetSecMonitoringGroupAnomalyLog_Type(AlaNetsecStatus):defaultValue=2
_AlaNetSecMonitoringGroupAnomalyLog_Type.__name__=_H
_AlaNetSecMonitoringGroupAnomalyLog_Object=MibTableColumn
alaNetSecMonitoringGroupAnomalyLog=_AlaNetSecMonitoringGroupAnomalyLog_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,2,1,1,4),_AlaNetSecMonitoringGroupAnomalyLog_Type())
alaNetSecMonitoringGroupAnomalyLog.setMaxAccess(_F)
if mibBuilder.loadTexts:alaNetSecMonitoringGroupAnomalyLog.setStatus(_A)
class _AlaNetSecMonitoringGroupAnomalyTrap_Type(AlaNetsecStatus):defaultValue=2
_AlaNetSecMonitoringGroupAnomalyTrap_Type.__name__=_H
_AlaNetSecMonitoringGroupAnomalyTrap_Object=MibTableColumn
alaNetSecMonitoringGroupAnomalyTrap=_AlaNetSecMonitoringGroupAnomalyTrap_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,2,1,1,5),_AlaNetSecMonitoringGroupAnomalyTrap_Type())
alaNetSecMonitoringGroupAnomalyTrap.setMaxAccess(_F)
if mibBuilder.loadTexts:alaNetSecMonitoringGroupAnomalyTrap.setStatus(_A)
class _AlaNetSecMonitoringGroupAnomalyQuarantine_Type(AlaNetsecStatus):defaultValue=2
_AlaNetSecMonitoringGroupAnomalyQuarantine_Type.__name__=_H
_AlaNetSecMonitoringGroupAnomalyQuarantine_Object=MibTableColumn
alaNetSecMonitoringGroupAnomalyQuarantine=_AlaNetSecMonitoringGroupAnomalyQuarantine_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,2,1,1,6),_AlaNetSecMonitoringGroupAnomalyQuarantine_Type())
alaNetSecMonitoringGroupAnomalyQuarantine.setMaxAccess(_F)
if mibBuilder.loadTexts:alaNetSecMonitoringGroupAnomalyQuarantine.setStatus(_A)
class _AlaNetSecMonitoringGroupAnomalyCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100000))
_AlaNetSecMonitoringGroupAnomalyCount_Type.__name__=_E
_AlaNetSecMonitoringGroupAnomalyCount_Object=MibTableColumn
alaNetSecMonitoringGroupAnomalyCount=_AlaNetSecMonitoringGroupAnomalyCount_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,2,1,1,7),_AlaNetSecMonitoringGroupAnomalyCount_Type())
alaNetSecMonitoringGroupAnomalyCount.setMaxAccess(_F)
if mibBuilder.loadTexts:alaNetSecMonitoringGroupAnomalyCount.setStatus(_A)
class _AlaNetSecMonitoringGroupAnomalySensitivity_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_AlaNetSecMonitoringGroupAnomalySensitivity_Type.__name__=_E
_AlaNetSecMonitoringGroupAnomalySensitivity_Object=MibTableColumn
alaNetSecMonitoringGroupAnomalySensitivity=_AlaNetSecMonitoringGroupAnomalySensitivity_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,2,1,1,8),_AlaNetSecMonitoringGroupAnomalySensitivity_Type())
alaNetSecMonitoringGroupAnomalySensitivity.setMaxAccess(_F)
if mibBuilder.loadTexts:alaNetSecMonitoringGroupAnomalySensitivity.setStatus(_A)
class _AlaNetSecMonitoringGroupAnomalyPeriod_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,3600))
_AlaNetSecMonitoringGroupAnomalyPeriod_Type.__name__=_E
_AlaNetSecMonitoringGroupAnomalyPeriod_Object=MibTableColumn
alaNetSecMonitoringGroupAnomalyPeriod=_AlaNetSecMonitoringGroupAnomalyPeriod_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,2,1,1,9),_AlaNetSecMonitoringGroupAnomalyPeriod_Type())
alaNetSecMonitoringGroupAnomalyPeriod.setMaxAccess(_F)
if mibBuilder.loadTexts:alaNetSecMonitoringGroupAnomalyPeriod.setStatus(_A)
_AlaNetSecMonitoringGroupRowStatus_Type=RowStatus
_AlaNetSecMonitoringGroupRowStatus_Object=MibTableColumn
alaNetSecMonitoringGroupRowStatus=_AlaNetSecMonitoringGroupRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,2,1,1,10),_AlaNetSecMonitoringGroupRowStatus_Type())
alaNetSecMonitoringGroupRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alaNetSecMonitoringGroupRowStatus.setStatus(_A)
_AlaNetSecPortStats_ObjectIdentity=ObjectIdentity
alaNetSecPortStats=_AlaNetSecPortStats_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,3))
_AlaNetSecPortStatsTable_Object=MibTable
alaNetSecPortStatsTable=_AlaNetSecPortStatsTable_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,3,1))
if mibBuilder.loadTexts:alaNetSecPortStatsTable.setStatus(_A)
_AlaNetSecPortStatsEntry_Object=MibTableRow
alaNetSecPortStatsEntry=_AlaNetSecPortStatsEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,3,1,1))
alaNetSecPortStatsEntry.setIndexNames((0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:alaNetSecPortStatsEntry.setStatus(_A)
_AlaNetSecPortStatsIfId_Type=InterfaceIndex
_AlaNetSecPortStatsIfId_Object=MibTableColumn
alaNetSecPortStatsIfId=_AlaNetSecPortStatsIfId_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,3,1,1,1),_AlaNetSecPortStatsIfId_Type())
alaNetSecPortStatsIfId.setMaxAccess(_D)
if mibBuilder.loadTexts:alaNetSecPortStatsIfId.setStatus(_A)
_AlaNetSecPortStatsPacket_Type=AlaPacketType
_AlaNetSecPortStatsPacket_Object=MibTableColumn
alaNetSecPortStatsPacket=_AlaNetSecPortStatsPacket_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,3,1,1,2),_AlaNetSecPortStatsPacket_Type())
alaNetSecPortStatsPacket.setMaxAccess(_D)
if mibBuilder.loadTexts:alaNetSecPortStatsPacket.setStatus(_A)
_AlaNetSecPortStatsLastIngress_Type=Counter32
_AlaNetSecPortStatsLastIngress_Object=MibTableColumn
alaNetSecPortStatsLastIngress=_AlaNetSecPortStatsLastIngress_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,3,1,1,3),_AlaNetSecPortStatsLastIngress_Type())
alaNetSecPortStatsLastIngress.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecPortStatsLastIngress.setStatus(_A)
_AlaNetSecPortStatsLastEgress_Type=Counter32
_AlaNetSecPortStatsLastEgress_Object=MibTableColumn
alaNetSecPortStatsLastEgress=_AlaNetSecPortStatsLastEgress_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,3,1,1,4),_AlaNetSecPortStatsLastEgress_Type())
alaNetSecPortStatsLastEgress.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecPortStatsLastEgress.setStatus(_A)
_AlaNetSecPortStatsTotalIngress_Type=Counter32
_AlaNetSecPortStatsTotalIngress_Object=MibTableColumn
alaNetSecPortStatsTotalIngress=_AlaNetSecPortStatsTotalIngress_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,3,1,1,5),_AlaNetSecPortStatsTotalIngress_Type())
alaNetSecPortStatsTotalIngress.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecPortStatsTotalIngress.setStatus(_A)
_AlaNetSecPortStatsTotalEgress_Type=Counter32
_AlaNetSecPortStatsTotalEgress_Object=MibTableColumn
alaNetSecPortStatsTotalEgress=_AlaNetSecPortStatsTotalEgress_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,3,1,1,6),_AlaNetSecPortStatsTotalEgress_Type())
alaNetSecPortStatsTotalEgress.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecPortStatsTotalEgress.setStatus(_A)
_AlaNetSecPortAnomalyStats_ObjectIdentity=ObjectIdentity
alaNetSecPortAnomalyStats=_AlaNetSecPortAnomalyStats_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,4))
_AlaNetSecPortAnomalyStatsTable_Object=MibTable
alaNetSecPortAnomalyStatsTable=_AlaNetSecPortAnomalyStatsTable_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,4,1))
if mibBuilder.loadTexts:alaNetSecPortAnomalyStatsTable.setStatus(_A)
_AlaNetSecPortAnomalyStatsEntry_Object=MibTableRow
alaNetSecPortAnomalyStatsEntry=_AlaNetSecPortAnomalyStatsEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,4,1,1))
alaNetSecPortAnomalyStatsEntry.setIndexNames((0,_B,_S),(0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:alaNetSecPortAnomalyStatsEntry.setStatus(_A)
_AlaNetSecPortAnomalyStatsIfId_Type=InterfaceIndex
_AlaNetSecPortAnomalyStatsIfId_Object=MibTableColumn
alaNetSecPortAnomalyStatsIfId=_AlaNetSecPortAnomalyStatsIfId_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,4,1,1,1),_AlaNetSecPortAnomalyStatsIfId_Type())
alaNetSecPortAnomalyStatsIfId.setMaxAccess(_D)
if mibBuilder.loadTexts:alaNetSecPortAnomalyStatsIfId.setStatus(_A)
_AlaNetSecPortAnomalyStatsAnomaly_Type=AlaAnomalyType
_AlaNetSecPortAnomalyStatsAnomaly_Object=MibTableColumn
alaNetSecPortAnomalyStatsAnomaly=_AlaNetSecPortAnomalyStatsAnomaly_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,4,1,1,2),_AlaNetSecPortAnomalyStatsAnomaly_Type())
alaNetSecPortAnomalyStatsAnomaly.setMaxAccess(_D)
if mibBuilder.loadTexts:alaNetSecPortAnomalyStatsAnomaly.setStatus(_A)
_AlaNetSecPortAnomalyStatsPacket_Type=AlaPacketType
_AlaNetSecPortAnomalyStatsPacket_Object=MibTableColumn
alaNetSecPortAnomalyStatsPacket=_AlaNetSecPortAnomalyStatsPacket_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,4,1,1,3),_AlaNetSecPortAnomalyStatsPacket_Type())
alaNetSecPortAnomalyStatsPacket.setMaxAccess(_D)
if mibBuilder.loadTexts:alaNetSecPortAnomalyStatsPacket.setStatus(_A)
_AlaNetSecPortAnomalyStatsCurrentIngress_Type=Counter32
_AlaNetSecPortAnomalyStatsCurrentIngress_Object=MibTableColumn
alaNetSecPortAnomalyStatsCurrentIngress=_AlaNetSecPortAnomalyStatsCurrentIngress_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,4,1,1,4),_AlaNetSecPortAnomalyStatsCurrentIngress_Type())
alaNetSecPortAnomalyStatsCurrentIngress.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecPortAnomalyStatsCurrentIngress.setStatus(_A)
_AlaNetSecPortAnomalyStatsCurrentEgress_Type=Counter32
_AlaNetSecPortAnomalyStatsCurrentEgress_Object=MibTableColumn
alaNetSecPortAnomalyStatsCurrentEgress=_AlaNetSecPortAnomalyStatsCurrentEgress_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,4,1,1,5),_AlaNetSecPortAnomalyStatsCurrentEgress_Type())
alaNetSecPortAnomalyStatsCurrentEgress.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecPortAnomalyStatsCurrentEgress.setStatus(_A)
_AlaNetSecPortAnomalyStatsLastIngress_Type=Counter32
_AlaNetSecPortAnomalyStatsLastIngress_Object=MibTableColumn
alaNetSecPortAnomalyStatsLastIngress=_AlaNetSecPortAnomalyStatsLastIngress_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,4,1,1,6),_AlaNetSecPortAnomalyStatsLastIngress_Type())
alaNetSecPortAnomalyStatsLastIngress.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecPortAnomalyStatsLastIngress.setStatus(_A)
_AlaNetSecPortAnomalyStatsLastEgress_Type=Counter32
_AlaNetSecPortAnomalyStatsLastEgress_Object=MibTableColumn
alaNetSecPortAnomalyStatsLastEgress=_AlaNetSecPortAnomalyStatsLastEgress_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,4,1,1,7),_AlaNetSecPortAnomalyStatsLastEgress_Type())
alaNetSecPortAnomalyStatsLastEgress.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecPortAnomalyStatsLastEgress.setStatus(_A)
_AlaNetSecPortAnomalySummary_ObjectIdentity=ObjectIdentity
alaNetSecPortAnomalySummary=_AlaNetSecPortAnomalySummary_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,5))
_AlaNetSecPortAnomalySummaryTable_Object=MibTable
alaNetSecPortAnomalySummaryTable=_AlaNetSecPortAnomalySummaryTable_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,5,1))
if mibBuilder.loadTexts:alaNetSecPortAnomalySummaryTable.setStatus(_A)
_AlaNetSecPortAnomalySummaryEntry_Object=MibTableRow
alaNetSecPortAnomalySummaryEntry=_AlaNetSecPortAnomalySummaryEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,5,1,1))
alaNetSecPortAnomalySummaryEntry.setIndexNames((0,_B,_V),(0,_B,_W))
if mibBuilder.loadTexts:alaNetSecPortAnomalySummaryEntry.setStatus(_A)
_AlaNetSecPortAnomalySummaryIfId_Type=InterfaceIndex
_AlaNetSecPortAnomalySummaryIfId_Object=MibTableColumn
alaNetSecPortAnomalySummaryIfId=_AlaNetSecPortAnomalySummaryIfId_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,5,1,1,1),_AlaNetSecPortAnomalySummaryIfId_Type())
alaNetSecPortAnomalySummaryIfId.setMaxAccess(_D)
if mibBuilder.loadTexts:alaNetSecPortAnomalySummaryIfId.setStatus(_A)
_AlaNetSecPortAnomalySummaryAnomaly_Type=AlaAnomalyType
_AlaNetSecPortAnomalySummaryAnomaly_Object=MibTableColumn
alaNetSecPortAnomalySummaryAnomaly=_AlaNetSecPortAnomalySummaryAnomaly_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,5,1,1,2),_AlaNetSecPortAnomalySummaryAnomaly_Type())
alaNetSecPortAnomalySummaryAnomaly.setMaxAccess(_D)
if mibBuilder.loadTexts:alaNetSecPortAnomalySummaryAnomaly.setStatus(_A)
_AlaNetSecPortAnomalySummaryObserved_Type=Counter32
_AlaNetSecPortAnomalySummaryObserved_Object=MibTableColumn
alaNetSecPortAnomalySummaryObserved=_AlaNetSecPortAnomalySummaryObserved_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,5,1,1,3),_AlaNetSecPortAnomalySummaryObserved_Type())
alaNetSecPortAnomalySummaryObserved.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecPortAnomalySummaryObserved.setStatus(_A)
_AlaNetSecPortAnomalySummaryDetected_Type=Counter32
_AlaNetSecPortAnomalySummaryDetected_Object=MibTableColumn
alaNetSecPortAnomalySummaryDetected=_AlaNetSecPortAnomalySummaryDetected_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,5,1,1,4),_AlaNetSecPortAnomalySummaryDetected_Type())
alaNetSecPortAnomalySummaryDetected.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecPortAnomalySummaryDetected.setStatus(_A)
_AlaNetSecPortOp_ObjectIdentity=ObjectIdentity
alaNetSecPortOp=_AlaNetSecPortOp_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,6))
_AlaNetSecPortOpTable_Object=MibTable
alaNetSecPortOpTable=_AlaNetSecPortOpTable_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,6,1))
if mibBuilder.loadTexts:alaNetSecPortOpTable.setStatus(_A)
_AlaNetSecPortOpEntry_Object=MibTableRow
alaNetSecPortOpEntry=_AlaNetSecPortOpEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,6,1,1))
alaNetSecPortOpEntry.setIndexNames((0,_B,_X),(0,_B,_Y))
if mibBuilder.loadTexts:alaNetSecPortOpEntry.setStatus(_A)
_AlaNetSecPortOpIfId_Type=InterfaceIndex
_AlaNetSecPortOpIfId_Object=MibTableColumn
alaNetSecPortOpIfId=_AlaNetSecPortOpIfId_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,6,1,1,1),_AlaNetSecPortOpIfId_Type())
alaNetSecPortOpIfId.setMaxAccess(_D)
if mibBuilder.loadTexts:alaNetSecPortOpIfId.setStatus(_A)
_AlaNetSecPortOpAnomaly_Type=AlaAnomalyType
_AlaNetSecPortOpAnomaly_Object=MibTableColumn
alaNetSecPortOpAnomaly=_AlaNetSecPortOpAnomaly_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,6,1,1,2),_AlaNetSecPortOpAnomaly_Type())
alaNetSecPortOpAnomaly.setMaxAccess(_D)
if mibBuilder.loadTexts:alaNetSecPortOpAnomaly.setStatus(_A)
_AlaNetSecPortOpState_Type=AlaNetsecStatus
_AlaNetSecPortOpState_Object=MibTableColumn
alaNetSecPortOpState=_AlaNetSecPortOpState_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,6,1,1,3),_AlaNetSecPortOpState_Type())
alaNetSecPortOpState.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecPortOpState.setStatus(_A)
_AlaNetSecPortOpLog_Type=AlaNetsecStatus
_AlaNetSecPortOpLog_Object=MibTableColumn
alaNetSecPortOpLog=_AlaNetSecPortOpLog_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,6,1,1,4),_AlaNetSecPortOpLog_Type())
alaNetSecPortOpLog.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecPortOpLog.setStatus(_A)
_AlaNetSecPortOpTrap_Type=AlaNetsecStatus
_AlaNetSecPortOpTrap_Object=MibTableColumn
alaNetSecPortOpTrap=_AlaNetSecPortOpTrap_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,6,1,1,5),_AlaNetSecPortOpTrap_Type())
alaNetSecPortOpTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecPortOpTrap.setStatus(_A)
_AlaNetSecPortOpQuarantine_Type=AlaNetsecStatus
_AlaNetSecPortOpQuarantine_Object=MibTableColumn
alaNetSecPortOpQuarantine=_AlaNetSecPortOpQuarantine_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,6,1,1,6),_AlaNetSecPortOpQuarantine_Type())
alaNetSecPortOpQuarantine.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecPortOpQuarantine.setStatus(_A)
class _AlaNetSecPortOpCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100000))
_AlaNetSecPortOpCount_Type.__name__=_E
_AlaNetSecPortOpCount_Object=MibTableColumn
alaNetSecPortOpCount=_AlaNetSecPortOpCount_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,6,1,1,7),_AlaNetSecPortOpCount_Type())
alaNetSecPortOpCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecPortOpCount.setStatus(_A)
class _AlaNetSecPortOpSensitivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_AlaNetSecPortOpSensitivity_Type.__name__=_E
_AlaNetSecPortOpSensitivity_Object=MibTableColumn
alaNetSecPortOpSensitivity=_AlaNetSecPortOpSensitivity_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,6,1,1,8),_AlaNetSecPortOpSensitivity_Type())
alaNetSecPortOpSensitivity.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecPortOpSensitivity.setStatus(_A)
class _AlaNetSecPortOpPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,3600))
_AlaNetSecPortOpPeriod_Type.__name__=_E
_AlaNetSecPortOpPeriod_Object=MibTableColumn
alaNetSecPortOpPeriod=_AlaNetSecPortOpPeriod_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,6,1,1,9),_AlaNetSecPortOpPeriod_Type())
alaNetSecPortOpPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecPortOpPeriod.setStatus(_A)
_AlaNetSecGroupOp_ObjectIdentity=ObjectIdentity
alaNetSecGroupOp=_AlaNetSecGroupOp_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,7))
_AlaNetSecGroupOpTable_Object=MibTable
alaNetSecGroupOpTable=_AlaNetSecGroupOpTable_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,7,1))
if mibBuilder.loadTexts:alaNetSecGroupOpTable.setStatus(_A)
_AlaNetSecGroupOpEntry_Object=MibTableRow
alaNetSecGroupOpEntry=_AlaNetSecGroupOpEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,7,1,1))
alaNetSecGroupOpEntry.setIndexNames((0,_B,_Z),(0,_B,_a))
if mibBuilder.loadTexts:alaNetSecGroupOpEntry.setStatus(_A)
class _AlaNetSecGroupOpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AlaNetSecGroupOpName_Type.__name__=_G
_AlaNetSecGroupOpName_Object=MibTableColumn
alaNetSecGroupOpName=_AlaNetSecGroupOpName_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,7,1,1,1),_AlaNetSecGroupOpName_Type())
alaNetSecGroupOpName.setMaxAccess(_D)
if mibBuilder.loadTexts:alaNetSecGroupOpName.setStatus(_A)
_AlaNetSecGroupOpAnomaly_Type=AlaAnomalyType
_AlaNetSecGroupOpAnomaly_Object=MibTableColumn
alaNetSecGroupOpAnomaly=_AlaNetSecGroupOpAnomaly_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,7,1,1,2),_AlaNetSecGroupOpAnomaly_Type())
alaNetSecGroupOpAnomaly.setMaxAccess(_D)
if mibBuilder.loadTexts:alaNetSecGroupOpAnomaly.setStatus(_A)
_AlaNetSecGroupOpState_Type=AlaNetsecStatus
_AlaNetSecGroupOpState_Object=MibTableColumn
alaNetSecGroupOpState=_AlaNetSecGroupOpState_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,7,1,1,3),_AlaNetSecGroupOpState_Type())
alaNetSecGroupOpState.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecGroupOpState.setStatus(_A)
_AlaNetSecGroupOpLog_Type=AlaNetsecStatus
_AlaNetSecGroupOpLog_Object=MibTableColumn
alaNetSecGroupOpLog=_AlaNetSecGroupOpLog_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,7,1,1,4),_AlaNetSecGroupOpLog_Type())
alaNetSecGroupOpLog.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecGroupOpLog.setStatus(_A)
_AlaNetSecGroupOpTrap_Type=AlaNetsecStatus
_AlaNetSecGroupOpTrap_Object=MibTableColumn
alaNetSecGroupOpTrap=_AlaNetSecGroupOpTrap_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,7,1,1,5),_AlaNetSecGroupOpTrap_Type())
alaNetSecGroupOpTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecGroupOpTrap.setStatus(_A)
_AlaNetSecGroupOpQuarantine_Type=AlaNetsecStatus
_AlaNetSecGroupOpQuarantine_Object=MibTableColumn
alaNetSecGroupOpQuarantine=_AlaNetSecGroupOpQuarantine_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,7,1,1,6),_AlaNetSecGroupOpQuarantine_Type())
alaNetSecGroupOpQuarantine.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecGroupOpQuarantine.setStatus(_A)
class _AlaNetSecGroupOpCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100000))
_AlaNetSecGroupOpCount_Type.__name__=_E
_AlaNetSecGroupOpCount_Object=MibTableColumn
alaNetSecGroupOpCount=_AlaNetSecGroupOpCount_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,7,1,1,7),_AlaNetSecGroupOpCount_Type())
alaNetSecGroupOpCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecGroupOpCount.setStatus(_A)
class _AlaNetSecGroupOpSensitivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_AlaNetSecGroupOpSensitivity_Type.__name__=_E
_AlaNetSecGroupOpSensitivity_Object=MibTableColumn
alaNetSecGroupOpSensitivity=_AlaNetSecGroupOpSensitivity_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,7,1,1,8),_AlaNetSecGroupOpSensitivity_Type())
alaNetSecGroupOpSensitivity.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecGroupOpSensitivity.setStatus(_A)
class _AlaNetSecGroupOpPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,3600))
_AlaNetSecGroupOpPeriod_Type.__name__=_E
_AlaNetSecGroupOpPeriod_Object=MibTableColumn
alaNetSecGroupOpPeriod=_AlaNetSecGroupOpPeriod_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,7,1,1,9),_AlaNetSecGroupOpPeriod_Type())
alaNetSecGroupOpPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecGroupOpPeriod.setStatus(_A)
_AlaNetSecGroup_ObjectIdentity=ObjectIdentity
alaNetSecGroup=_AlaNetSecGroup_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,8))
_AlaNetSecGroupTable_Object=MibTable
alaNetSecGroupTable=_AlaNetSecGroupTable_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,8,1))
if mibBuilder.loadTexts:alaNetSecGroupTable.setStatus(_A)
_AlaNetSecGroupEntry_Object=MibTableRow
alaNetSecGroupEntry=_AlaNetSecGroupEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,8,1,1))
alaNetSecGroupEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:alaNetSecGroupEntry.setStatus(_A)
class _AlaNetSecGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AlaNetSecGroupName_Type.__name__=_G
_AlaNetSecGroupName_Object=MibTableColumn
alaNetSecGroupName=_AlaNetSecGroupName_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,8,1,1,1),_AlaNetSecGroupName_Type())
alaNetSecGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:alaNetSecGroupName.setStatus(_A)
_AlaNetSecGroupMemberPorts_Type=TruthValue
_AlaNetSecGroupMemberPorts_Object=MibTableColumn
alaNetSecGroupMemberPorts=_AlaNetSecGroupMemberPorts_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,8,1,1,2),_AlaNetSecGroupMemberPorts_Type())
alaNetSecGroupMemberPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecGroupMemberPorts.setStatus(_A)
_AlaNetSecGroupAnomalyCfg_Type=TruthValue
_AlaNetSecGroupAnomalyCfg_Object=MibTableColumn
alaNetSecGroupAnomalyCfg=_AlaNetSecGroupAnomalyCfg_Object((1,3,6,1,4,1,6486,800,1,2,1,48,1,1,8,1,1,3),_AlaNetSecGroupAnomalyCfg_Type())
alaNetSecGroupAnomalyCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:alaNetSecGroupAnomalyCfg.setStatus(_A)
_AlcatelIND1NETSECMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1NETSECMIBConformance=_AlcatelIND1NETSECMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,48,1,2))
if mibBuilder.loadTexts:alcatelIND1NETSECMIBConformance.setStatus(_A)
_AlcatelIND1NETSECMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1NETSECMIBGroups=_AlcatelIND1NETSECMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,48,1,2,1))
if mibBuilder.loadTexts:alcatelIND1NETSECMIBGroups.setStatus(_A)
_AlcatelIND1NETSECMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1NETSECMIBCompliances=_AlcatelIND1NETSECMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,48,1,2,2))
if mibBuilder.loadTexts:alcatelIND1NETSECMIBCompliances.setStatus(_A)
_AlaNetSecPortTrapsDesc_ObjectIdentity=ObjectIdentity
alaNetSecPortTrapsDesc=_AlaNetSecPortTrapsDesc_ObjectIdentity((1,3,6,1,4,1,6486,800,1,3,2,20,1))
_AlaNetSecPortTrapsObj_ObjectIdentity=ObjectIdentity
alaNetSecPortTrapsObj=_AlaNetSecPortTrapsObj_ObjectIdentity((1,3,6,1,4,1,6486,800,1,3,2,20,2))
_AlaNetSecPortTrapInfoIfId_Type=InterfaceIndex
_AlaNetSecPortTrapInfoIfId_Object=MibScalar
alaNetSecPortTrapInfoIfId=_AlaNetSecPortTrapInfoIfId_Object((1,3,6,1,4,1,6486,800,1,3,2,20,2,1),_AlaNetSecPortTrapInfoIfId_Type())
alaNetSecPortTrapInfoIfId.setMaxAccess(_J)
if mibBuilder.loadTexts:alaNetSecPortTrapInfoIfId.setStatus(_A)
_AlaNetSecPortTrapInfoAnomaly_Type=AlaAnomalyType
_AlaNetSecPortTrapInfoAnomaly_Object=MibScalar
alaNetSecPortTrapInfoAnomaly=_AlaNetSecPortTrapInfoAnomaly_Object((1,3,6,1,4,1,6486,800,1,3,2,20,2,2),_AlaNetSecPortTrapInfoAnomaly_Type())
alaNetSecPortTrapInfoAnomaly.setMaxAccess(_J)
if mibBuilder.loadTexts:alaNetSecPortTrapInfoAnomaly.setStatus(_A)
class _AlaNetSecPortTrapInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('source',2),('target',3)))
_AlaNetSecPortTrapInfoType_Type.__name__=_E
_AlaNetSecPortTrapInfoType_Object=MibScalar
alaNetSecPortTrapInfoType=_AlaNetSecPortTrapInfoType_Object((1,3,6,1,4,1,6486,800,1,3,2,20,2,3),_AlaNetSecPortTrapInfoType_Type())
alaNetSecPortTrapInfoType.setMaxAccess(_J)
if mibBuilder.loadTexts:alaNetSecPortTrapInfoType.setStatus(_A)
alaNetSecPortRangeComplianceGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,48,1,2,1,1))
alaNetSecPortRangeComplianceGroup.setObjects((_B,_c))
if mibBuilder.loadTexts:alaNetSecPortRangeComplianceGroup.setStatus(_A)
alaNetSecMonitoringGroupComplianceGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,48,1,2,1,2))
alaNetSecMonitoringGroupComplianceGroup.setObjects((_B,_d))
if mibBuilder.loadTexts:alaNetSecMonitoringGroupComplianceGroup.setStatus(_A)
alaNetSecPortStatsComplianceGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,48,1,2,1,4))
alaNetSecPortStatsComplianceGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:alaNetSecPortStatsComplianceGroup.setStatus(_A)
alaNetSecPortAnomalyStatsComplianceGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,48,1,2,1,5))
alaNetSecPortAnomalyStatsComplianceGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:alaNetSecPortAnomalyStatsComplianceGroup.setStatus(_A)
alaNetSecPortAnomalySummaryComplianceGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,48,1,2,1,6))
alaNetSecPortAnomalySummaryComplianceGroup.setObjects(*((_B,_m),(_B,_n)))
if mibBuilder.loadTexts:alaNetSecPortAnomalySummaryComplianceGroup.setStatus(_A)
alaNetSecPortOpComplianceGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,48,1,2,1,7))
alaNetSecPortOpComplianceGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:alaNetSecPortOpComplianceGroup.setStatus(_A)
alaNetSecGroupOpComplianceGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,48,1,2,1,8))
alaNetSecGroupOpComplianceGroup.setObjects(*((_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:alaNetSecGroupOpComplianceGroup.setStatus(_A)
alaNetSecGroupComplianceGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,48,1,2,1,9))
alaNetSecGroupComplianceGroup.setObjects(*((_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:alaNetSecGroupComplianceGroup.setStatus(_A)
alaNetSecMonitoringGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,48,1,2,1,10))
alaNetSecMonitoringGroup.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:alaNetSecMonitoringGroup.setStatus(_A)
alaNetSecPortTrapInfoGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,48,1,2,1,11))
alaNetSecPortTrapInfoGroup.setObjects(*((_B,_I),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:alaNetSecPortTrapInfoGroup.setStatus(_A)
alaNetSecPortTrapAnomaly=NotificationType((1,3,6,1,4,1,6486,800,1,3,2,20,1,0,1))
alaNetSecPortTrapAnomaly.setObjects(*((_B,_I),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:alaNetSecPortTrapAnomaly.setStatus(_A)
alaNetSecPortTrapQuarantine=NotificationType((1,3,6,1,4,1,6486,800,1,3,2,20,1,0,2))
alaNetSecPortTrapQuarantine.setObjects((_B,_I))
if mibBuilder.loadTexts:alaNetSecPortTrapQuarantine.setStatus(_A)
alaNetSecPortTrapsComplianceGroup=NotificationGroup((1,3,6,1,4,1,6486,800,1,2,1,48,1,2,1,3))
alaNetSecPortTrapsComplianceGroup.setObjects(*((_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:alaNetSecPortTrapsComplianceGroup.setStatus(_A)
alcatelIND1NETSECMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,48,1,2,2,1))
alcatelIND1NETSECMIBCompliance.setObjects(*((_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN)))
if mibBuilder.loadTexts:alcatelIND1NETSECMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AlaAnomalyType':AlaAnomalyType,'AlaPacketType':AlaPacketType,_H:AlaNetsecStatus,'alcatelIND1NETSECMIB':alcatelIND1NETSECMIB,'alcatelIND1NETSECMIBObjects':alcatelIND1NETSECMIBObjects,'alaNetSecPortRangeConfig':alaNetSecPortRangeConfig,'alaNetSecPortRangeGroupTable':alaNetSecPortRangeGroupTable,'alaNetSecPortRangeGroupEntry':alaNetSecPortRangeGroupEntry,_M:alaNetSecPortRangeGroupStartIfId,_N:alaNetSecPortRangeGroupEndIfId,_AB:alaNetSecPortRangeGroupName,_c:alaNetSecPortRangeGroupRowStatus,'alaNetSecMonitoringGroupConfig':alaNetSecMonitoringGroupConfig,'alaNetSecMonitoringGroupTable':alaNetSecMonitoringGroupTable,'alaNetSecMonitoringGroupEntry':alaNetSecMonitoringGroupEntry,_O:alaNetSecMonitoringGroupName,_P:alaNetSecMonitoringGroupAnomaly,_A9:alaNetSecMonitoringGroupAnomalyState,_A5:alaNetSecMonitoringGroupAnomalyLog,_AA:alaNetSecMonitoringGroupAnomalyTrap,_A7:alaNetSecMonitoringGroupAnomalyQuarantine,_A4:alaNetSecMonitoringGroupAnomalyCount,_A8:alaNetSecMonitoringGroupAnomalySensitivity,_A6:alaNetSecMonitoringGroupAnomalyPeriod,_d:alaNetSecMonitoringGroupRowStatus,'alaNetSecPortStats':alaNetSecPortStats,'alaNetSecPortStatsTable':alaNetSecPortStatsTable,'alaNetSecPortStatsEntry':alaNetSecPortStatsEntry,_Q:alaNetSecPortStatsIfId,_R:alaNetSecPortStatsPacket,_e:alaNetSecPortStatsLastIngress,_f:alaNetSecPortStatsLastEgress,_g:alaNetSecPortStatsTotalIngress,_h:alaNetSecPortStatsTotalEgress,'alaNetSecPortAnomalyStats':alaNetSecPortAnomalyStats,'alaNetSecPortAnomalyStatsTable':alaNetSecPortAnomalyStatsTable,'alaNetSecPortAnomalyStatsEntry':alaNetSecPortAnomalyStatsEntry,_S:alaNetSecPortAnomalyStatsIfId,_T:alaNetSecPortAnomalyStatsAnomaly,_U:alaNetSecPortAnomalyStatsPacket,_i:alaNetSecPortAnomalyStatsCurrentIngress,_j:alaNetSecPortAnomalyStatsCurrentEgress,_k:alaNetSecPortAnomalyStatsLastIngress,_l:alaNetSecPortAnomalyStatsLastEgress,'alaNetSecPortAnomalySummary':alaNetSecPortAnomalySummary,'alaNetSecPortAnomalySummaryTable':alaNetSecPortAnomalySummaryTable,'alaNetSecPortAnomalySummaryEntry':alaNetSecPortAnomalySummaryEntry,_V:alaNetSecPortAnomalySummaryIfId,_W:alaNetSecPortAnomalySummaryAnomaly,_m:alaNetSecPortAnomalySummaryObserved,_n:alaNetSecPortAnomalySummaryDetected,'alaNetSecPortOp':alaNetSecPortOp,'alaNetSecPortOpTable':alaNetSecPortOpTable,'alaNetSecPortOpEntry':alaNetSecPortOpEntry,_X:alaNetSecPortOpIfId,_Y:alaNetSecPortOpAnomaly,_o:alaNetSecPortOpState,_p:alaNetSecPortOpLog,_q:alaNetSecPortOpTrap,_r:alaNetSecPortOpQuarantine,_s:alaNetSecPortOpCount,_t:alaNetSecPortOpSensitivity,_u:alaNetSecPortOpPeriod,'alaNetSecGroupOp':alaNetSecGroupOp,'alaNetSecGroupOpTable':alaNetSecGroupOpTable,'alaNetSecGroupOpEntry':alaNetSecGroupOpEntry,_Z:alaNetSecGroupOpName,_a:alaNetSecGroupOpAnomaly,_v:alaNetSecGroupOpState,_w:alaNetSecGroupOpLog,_x:alaNetSecGroupOpTrap,_y:alaNetSecGroupOpQuarantine,_z:alaNetSecGroupOpCount,_A0:alaNetSecGroupOpSensitivity,_A1:alaNetSecGroupOpPeriod,'alaNetSecGroup':alaNetSecGroup,'alaNetSecGroupTable':alaNetSecGroupTable,'alaNetSecGroupEntry':alaNetSecGroupEntry,_b:alaNetSecGroupName,_A2:alaNetSecGroupMemberPorts,_A3:alaNetSecGroupAnomalyCfg,'alcatelIND1NETSECMIBConformance':alcatelIND1NETSECMIBConformance,'alcatelIND1NETSECMIBGroups':alcatelIND1NETSECMIBGroups,_AE:alaNetSecPortRangeComplianceGroup,_AF:alaNetSecMonitoringGroupComplianceGroup,_AM:alaNetSecPortTrapsComplianceGroup,_AG:alaNetSecPortStatsComplianceGroup,_AH:alaNetSecPortAnomalyStatsComplianceGroup,_AI:alaNetSecPortAnomalySummaryComplianceGroup,_AJ:alaNetSecPortOpComplianceGroup,_AK:alaNetSecGroupOpComplianceGroup,_AL:alaNetSecGroupComplianceGroup,_AN:alaNetSecMonitoringGroup,'alaNetSecPortTrapInfoGroup':alaNetSecPortTrapInfoGroup,'alcatelIND1NETSECMIBCompliances':alcatelIND1NETSECMIBCompliances,'alcatelIND1NETSECMIBCompliance':alcatelIND1NETSECMIBCompliance,'alaNetSecPortTrapsDesc':alaNetSecPortTrapsDesc,_AC:alaNetSecPortTrapAnomaly,_AD:alaNetSecPortTrapQuarantine,'alaNetSecPortTrapsObj':alaNetSecPortTrapsObj,_I:alaNetSecPortTrapInfoIfId,_K:alaNetSecPortTrapInfoAnomaly,_L:alaNetSecPortTrapInfoType})