_m='qtechGvrpStatsMIBGroup'
_l='qtechGvrpMIBGroup'
_k='qtechGvrpStatisticsPortClear'
_j='qtechGvrpLeavePropagated'
_i='qtechGvrpJoinPropagated'
_h='qtechGvrpLeaveIndicated'
_g='qtechGvrpJoinIndicated'
_f='qtechGvrpSentLeaveAll'
_e='qtechGvrpSentLeaveIn'
_d='qtechGvrpSentLeaveEmpty'
_c='qtechGvrpSentEmpty'
_b='qtechGvrpSentJoinIn'
_a='qtechGvrpSentJoin'
_Z='qtechGvrpSentGvrpPdu'
_Y='qtechGvrpRecLeaveAll'
_X='qtechGvrpRecLeaveIn'
_W='qtechGvrpRecLeaveEmpty'
_V='qtechGvrpRecEmpty'
_U='qtechGvrpRecJoinIn'
_T='qtechGvrpRecJoin'
_S='qtechGvrpRecInvalidGvrpPdu'
_R='qtechGvrpRecValidGvrpPdu'
_Q='qtechGvrpApplicantState'
_P='qtechGvrpRegistrationMode'
_O='qtechGvrpLeaveAllTimer'
_N='qtechGvrpLeaveTimer'
_M='qtechGvrpJoinTimer'
_L='qtechGvrpDynamicVlanCreateStauts'
_K='qtechGvrpStatus'
_J='qtechGvrpStatsIfIndex'
_I='not-accessible'
_H='qtechGvrpIfIndex'
_G='VlanId'
_F='Integer32'
_E='EnabledStatus'
_D='read-write'
_C='read-only'
_B='QTECH-GVRP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_E)
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_G)
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
IfIndex,=mibBuilder.importSymbols('QTECH-TC','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qtechGvrpMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,25))
if mibBuilder.loadTexts:qtechGvrpMIB.setRevisions(('2002-03-20 00:00',))
_QtechGvrpMIBObjects_ObjectIdentity=ObjectIdentity
qtechGvrpMIBObjects=_QtechGvrpMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,25,1))
class _QtechGvrpStatus_Type(EnabledStatus):defaultValue=2
_QtechGvrpStatus_Type.__name__=_E
_QtechGvrpStatus_Object=MibScalar
qtechGvrpStatus=_QtechGvrpStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,1),_QtechGvrpStatus_Type())
qtechGvrpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechGvrpStatus.setStatus(_A)
class _QtechGvrpDynamicVlanCreateStauts_Type(EnabledStatus):defaultValue=2
_QtechGvrpDynamicVlanCreateStauts_Type.__name__=_E
_QtechGvrpDynamicVlanCreateStauts_Object=MibScalar
qtechGvrpDynamicVlanCreateStauts=_QtechGvrpDynamicVlanCreateStauts_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,2),_QtechGvrpDynamicVlanCreateStauts_Type())
qtechGvrpDynamicVlanCreateStauts.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechGvrpDynamicVlanCreateStauts.setStatus(_A)
class _QtechGvrpJoinTimer_Type(Integer32):defaultValue=200
_QtechGvrpJoinTimer_Type.__name__=_F
_QtechGvrpJoinTimer_Object=MibScalar
qtechGvrpJoinTimer=_QtechGvrpJoinTimer_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,3),_QtechGvrpJoinTimer_Type())
qtechGvrpJoinTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechGvrpJoinTimer.setStatus(_A)
class _QtechGvrpLeaveTimer_Type(Integer32):defaultValue=600
_QtechGvrpLeaveTimer_Type.__name__=_F
_QtechGvrpLeaveTimer_Object=MibScalar
qtechGvrpLeaveTimer=_QtechGvrpLeaveTimer_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,4),_QtechGvrpLeaveTimer_Type())
qtechGvrpLeaveTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechGvrpLeaveTimer.setStatus(_A)
class _QtechGvrpLeaveAllTimer_Type(Integer32):defaultValue=10000
_QtechGvrpLeaveAllTimer_Type.__name__=_F
_QtechGvrpLeaveAllTimer_Object=MibScalar
qtechGvrpLeaveAllTimer=_QtechGvrpLeaveAllTimer_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,5),_QtechGvrpLeaveAllTimer_Type())
qtechGvrpLeaveAllTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechGvrpLeaveAllTimer.setStatus(_A)
_QtechGvrpTable_Object=MibTable
qtechGvrpTable=_QtechGvrpTable_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,6))
if mibBuilder.loadTexts:qtechGvrpTable.setStatus(_A)
_QtechGvrpEntry_Object=MibTableRow
qtechGvrpEntry=_QtechGvrpEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,6,1))
qtechGvrpEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:qtechGvrpEntry.setStatus(_A)
_QtechGvrpIfIndex_Type=IfIndex
_QtechGvrpIfIndex_Object=MibTableColumn
qtechGvrpIfIndex=_QtechGvrpIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,6,1,1),_QtechGvrpIfIndex_Type())
qtechGvrpIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechGvrpIfIndex.setStatus(_A)
class _QtechGvrpRegistrationMode_Type(EnabledStatus):defaultValue=1
_QtechGvrpRegistrationMode_Type.__name__=_E
_QtechGvrpRegistrationMode_Object=MibTableColumn
qtechGvrpRegistrationMode=_QtechGvrpRegistrationMode_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,6,1,2),_QtechGvrpRegistrationMode_Type())
qtechGvrpRegistrationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechGvrpRegistrationMode.setStatus(_A)
class _QtechGvrpApplicantState_Type(EnabledStatus):defaultValue=1
_QtechGvrpApplicantState_Type.__name__=_E
_QtechGvrpApplicantState_Object=MibTableColumn
qtechGvrpApplicantState=_QtechGvrpApplicantState_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,6,1,3),_QtechGvrpApplicantState_Type())
qtechGvrpApplicantState.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechGvrpApplicantState.setStatus(_A)
_QtechGvrpStatsTable_Object=MibTable
qtechGvrpStatsTable=_QtechGvrpStatsTable_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,7))
if mibBuilder.loadTexts:qtechGvrpStatsTable.setStatus(_A)
_QtechGvrpStatsEntry_Object=MibTableRow
qtechGvrpStatsEntry=_QtechGvrpStatsEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,7,1))
qtechGvrpStatsEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:qtechGvrpStatsEntry.setStatus(_A)
_QtechGvrpStatsIfIndex_Type=IfIndex
_QtechGvrpStatsIfIndex_Object=MibTableColumn
qtechGvrpStatsIfIndex=_QtechGvrpStatsIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,7,1,1),_QtechGvrpStatsIfIndex_Type())
qtechGvrpStatsIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechGvrpStatsIfIndex.setStatus(_A)
_QtechGvrpRecValidGvrpPdu_Type=Counter32
_QtechGvrpRecValidGvrpPdu_Object=MibTableColumn
qtechGvrpRecValidGvrpPdu=_QtechGvrpRecValidGvrpPdu_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,7,1,2),_QtechGvrpRecValidGvrpPdu_Type())
qtechGvrpRecValidGvrpPdu.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechGvrpRecValidGvrpPdu.setStatus(_A)
_QtechGvrpRecInvalidGvrpPdu_Type=Counter32
_QtechGvrpRecInvalidGvrpPdu_Object=MibTableColumn
qtechGvrpRecInvalidGvrpPdu=_QtechGvrpRecInvalidGvrpPdu_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,7,1,3),_QtechGvrpRecInvalidGvrpPdu_Type())
qtechGvrpRecInvalidGvrpPdu.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechGvrpRecInvalidGvrpPdu.setStatus(_A)
_QtechGvrpRecJoin_Type=Counter32
_QtechGvrpRecJoin_Object=MibTableColumn
qtechGvrpRecJoin=_QtechGvrpRecJoin_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,7,1,4),_QtechGvrpRecJoin_Type())
qtechGvrpRecJoin.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechGvrpRecJoin.setStatus(_A)
_QtechGvrpRecJoinIn_Type=Counter32
_QtechGvrpRecJoinIn_Object=MibTableColumn
qtechGvrpRecJoinIn=_QtechGvrpRecJoinIn_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,7,1,5),_QtechGvrpRecJoinIn_Type())
qtechGvrpRecJoinIn.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechGvrpRecJoinIn.setStatus(_A)
_QtechGvrpRecEmpty_Type=Counter32
_QtechGvrpRecEmpty_Object=MibTableColumn
qtechGvrpRecEmpty=_QtechGvrpRecEmpty_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,7,1,6),_QtechGvrpRecEmpty_Type())
qtechGvrpRecEmpty.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechGvrpRecEmpty.setStatus(_A)
_QtechGvrpRecLeaveEmpty_Type=Counter32
_QtechGvrpRecLeaveEmpty_Object=MibTableColumn
qtechGvrpRecLeaveEmpty=_QtechGvrpRecLeaveEmpty_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,7,1,7),_QtechGvrpRecLeaveEmpty_Type())
qtechGvrpRecLeaveEmpty.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechGvrpRecLeaveEmpty.setStatus(_A)
_QtechGvrpRecLeaveIn_Type=Counter32
_QtechGvrpRecLeaveIn_Object=MibTableColumn
qtechGvrpRecLeaveIn=_QtechGvrpRecLeaveIn_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,7,1,8),_QtechGvrpRecLeaveIn_Type())
qtechGvrpRecLeaveIn.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechGvrpRecLeaveIn.setStatus(_A)
_QtechGvrpRecLeaveAll_Type=Counter32
_QtechGvrpRecLeaveAll_Object=MibTableColumn
qtechGvrpRecLeaveAll=_QtechGvrpRecLeaveAll_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,7,1,9),_QtechGvrpRecLeaveAll_Type())
qtechGvrpRecLeaveAll.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechGvrpRecLeaveAll.setStatus(_A)
_QtechGvrpSentGvrpPdu_Type=Counter32
_QtechGvrpSentGvrpPdu_Object=MibTableColumn
qtechGvrpSentGvrpPdu=_QtechGvrpSentGvrpPdu_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,7,1,10),_QtechGvrpSentGvrpPdu_Type())
qtechGvrpSentGvrpPdu.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechGvrpSentGvrpPdu.setStatus(_A)
_QtechGvrpSentJoin_Type=Counter32
_QtechGvrpSentJoin_Object=MibTableColumn
qtechGvrpSentJoin=_QtechGvrpSentJoin_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,7,1,11),_QtechGvrpSentJoin_Type())
qtechGvrpSentJoin.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechGvrpSentJoin.setStatus(_A)
_QtechGvrpSentJoinIn_Type=Counter32
_QtechGvrpSentJoinIn_Object=MibTableColumn
qtechGvrpSentJoinIn=_QtechGvrpSentJoinIn_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,7,1,12),_QtechGvrpSentJoinIn_Type())
qtechGvrpSentJoinIn.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechGvrpSentJoinIn.setStatus(_A)
_QtechGvrpSentEmpty_Type=Counter32
_QtechGvrpSentEmpty_Object=MibTableColumn
qtechGvrpSentEmpty=_QtechGvrpSentEmpty_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,7,1,13),_QtechGvrpSentEmpty_Type())
qtechGvrpSentEmpty.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechGvrpSentEmpty.setStatus(_A)
_QtechGvrpSentLeaveEmpty_Type=Counter32
_QtechGvrpSentLeaveEmpty_Object=MibTableColumn
qtechGvrpSentLeaveEmpty=_QtechGvrpSentLeaveEmpty_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,7,1,14),_QtechGvrpSentLeaveEmpty_Type())
qtechGvrpSentLeaveEmpty.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechGvrpSentLeaveEmpty.setStatus(_A)
_QtechGvrpSentLeaveIn_Type=Counter32
_QtechGvrpSentLeaveIn_Object=MibTableColumn
qtechGvrpSentLeaveIn=_QtechGvrpSentLeaveIn_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,7,1,15),_QtechGvrpSentLeaveIn_Type())
qtechGvrpSentLeaveIn.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechGvrpSentLeaveIn.setStatus(_A)
_QtechGvrpSentLeaveAll_Type=Counter32
_QtechGvrpSentLeaveAll_Object=MibTableColumn
qtechGvrpSentLeaveAll=_QtechGvrpSentLeaveAll_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,7,1,16),_QtechGvrpSentLeaveAll_Type())
qtechGvrpSentLeaveAll.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechGvrpSentLeaveAll.setStatus(_A)
_QtechGvrpJoinIndicated_Type=Counter32
_QtechGvrpJoinIndicated_Object=MibTableColumn
qtechGvrpJoinIndicated=_QtechGvrpJoinIndicated_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,7,1,17),_QtechGvrpJoinIndicated_Type())
qtechGvrpJoinIndicated.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechGvrpJoinIndicated.setStatus(_A)
_QtechGvrpLeaveIndicated_Type=Counter32
_QtechGvrpLeaveIndicated_Object=MibTableColumn
qtechGvrpLeaveIndicated=_QtechGvrpLeaveIndicated_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,7,1,18),_QtechGvrpLeaveIndicated_Type())
qtechGvrpLeaveIndicated.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechGvrpLeaveIndicated.setStatus(_A)
_QtechGvrpJoinPropagated_Type=Counter32
_QtechGvrpJoinPropagated_Object=MibTableColumn
qtechGvrpJoinPropagated=_QtechGvrpJoinPropagated_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,7,1,19),_QtechGvrpJoinPropagated_Type())
qtechGvrpJoinPropagated.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechGvrpJoinPropagated.setStatus(_A)
_QtechGvrpLeavePropagated_Type=Counter32
_QtechGvrpLeavePropagated_Object=MibTableColumn
qtechGvrpLeavePropagated=_QtechGvrpLeavePropagated_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,7,1,20),_QtechGvrpLeavePropagated_Type())
qtechGvrpLeavePropagated.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechGvrpLeavePropagated.setStatus(_A)
_QtechGvrpStatisticsPortClear_Type=Integer32
_QtechGvrpStatisticsPortClear_Object=MibTableColumn
qtechGvrpStatisticsPortClear=_QtechGvrpStatisticsPortClear_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,7,1,21),_QtechGvrpStatisticsPortClear_Type())
qtechGvrpStatisticsPortClear.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechGvrpStatisticsPortClear.setStatus(_A)
class _QtechGvrpOperVid_Type(VlanId):defaultValue=1
_QtechGvrpOperVid_Type.__name__=_G
_QtechGvrpOperVid_Object=MibScalar
qtechGvrpOperVid=_QtechGvrpOperVid_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,8),_QtechGvrpOperVid_Type())
qtechGvrpOperVid.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechGvrpOperVid.setStatus(_A)
_QtechGvrpStatisticsClear_Type=Integer32
_QtechGvrpStatisticsClear_Object=MibScalar
qtechGvrpStatisticsClear=_QtechGvrpStatisticsClear_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,9),_QtechGvrpStatisticsClear_Type())
qtechGvrpStatisticsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechGvrpStatisticsClear.setStatus(_A)
_QtechGvrpResetTimer_Type=VlanId
_QtechGvrpResetTimer_Object=MibScalar
qtechGvrpResetTimer=_QtechGvrpResetTimer_Object((1,3,6,1,4,1,27514,1,1,10,2,25,1,10),_QtechGvrpResetTimer_Type())
qtechGvrpResetTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechGvrpResetTimer.setStatus(_A)
_QtechGvrpMIBConformance_ObjectIdentity=ObjectIdentity
qtechGvrpMIBConformance=_QtechGvrpMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,25,2))
_QtechGvrpMIBCompliances_ObjectIdentity=ObjectIdentity
qtechGvrpMIBCompliances=_QtechGvrpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,25,2,1))
_QtechGvrpMIBGroups_ObjectIdentity=ObjectIdentity
qtechGvrpMIBGroups=_QtechGvrpMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,25,2,2))
qtechGvrpMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,25,2,2,1))
qtechGvrpMIBGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:qtechGvrpMIBGroup.setStatus(_A)
qtechGvrpStatsMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,25,2,2,2))
qtechGvrpStatsMIBGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:qtechGvrpStatsMIBGroup.setStatus(_A)
qtechGvrpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,25,2,1,1))
qtechGvrpMIBCompliance.setObjects(*((_B,_l),(_B,_m)))
if mibBuilder.loadTexts:qtechGvrpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechGvrpMIB':qtechGvrpMIB,'qtechGvrpMIBObjects':qtechGvrpMIBObjects,_K:qtechGvrpStatus,_L:qtechGvrpDynamicVlanCreateStauts,_M:qtechGvrpJoinTimer,_N:qtechGvrpLeaveTimer,_O:qtechGvrpLeaveAllTimer,'qtechGvrpTable':qtechGvrpTable,'qtechGvrpEntry':qtechGvrpEntry,_H:qtechGvrpIfIndex,_P:qtechGvrpRegistrationMode,_Q:qtechGvrpApplicantState,'qtechGvrpStatsTable':qtechGvrpStatsTable,'qtechGvrpStatsEntry':qtechGvrpStatsEntry,_J:qtechGvrpStatsIfIndex,_R:qtechGvrpRecValidGvrpPdu,_S:qtechGvrpRecInvalidGvrpPdu,_T:qtechGvrpRecJoin,_U:qtechGvrpRecJoinIn,_V:qtechGvrpRecEmpty,_W:qtechGvrpRecLeaveEmpty,_X:qtechGvrpRecLeaveIn,_Y:qtechGvrpRecLeaveAll,_Z:qtechGvrpSentGvrpPdu,_a:qtechGvrpSentJoin,_b:qtechGvrpSentJoinIn,_c:qtechGvrpSentEmpty,_d:qtechGvrpSentLeaveEmpty,_e:qtechGvrpSentLeaveIn,_f:qtechGvrpSentLeaveAll,_g:qtechGvrpJoinIndicated,_h:qtechGvrpLeaveIndicated,_i:qtechGvrpJoinPropagated,_j:qtechGvrpLeavePropagated,_k:qtechGvrpStatisticsPortClear,'qtechGvrpOperVid':qtechGvrpOperVid,'qtechGvrpStatisticsClear':qtechGvrpStatisticsClear,'qtechGvrpResetTimer':qtechGvrpResetTimer,'qtechGvrpMIBConformance':qtechGvrpMIBConformance,'qtechGvrpMIBCompliances':qtechGvrpMIBCompliances,'qtechGvrpMIBCompliance':qtechGvrpMIBCompliance,'qtechGvrpMIBGroups':qtechGvrpMIBGroups,_l:qtechGvrpMIBGroup,_m:qtechGvrpStatsMIBGroup})