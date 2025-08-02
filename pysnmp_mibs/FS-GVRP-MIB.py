_m='fsGvrpStatsMIBGroup'
_l='fsGvrpMIBGroup'
_k='fsGvrpStatisticsPortClear'
_j='fsGvrpLeavePropagated'
_i='fsGvrpJoinPropagated'
_h='fsGvrpLeaveIndicated'
_g='fsGvrpJoinIndicated'
_f='fsGvrpSentLeaveAll'
_e='fsGvrpSentLeaveIn'
_d='fsGvrpSentLeaveEmpty'
_c='fsGvrpSentEmpty'
_b='fsGvrpSentJoinIn'
_a='fsGvrpSentJoin'
_Z='fsGvrpSentGvrpPdu'
_Y='fsGvrpRecLeaveAll'
_X='fsGvrpRecLeaveIn'
_W='fsGvrpRecLeaveEmpty'
_V='fsGvrpRecEmpty'
_U='fsGvrpRecJoinIn'
_T='fsGvrpRecJoin'
_S='fsGvrpRecInvalidGvrpPdu'
_R='fsGvrpRecValidGvrpPdu'
_Q='fsGvrpApplicantState'
_P='fsGvrpRegistrationMode'
_O='fsGvrpLeaveAllTimer'
_N='fsGvrpLeaveTimer'
_M='fsGvrpJoinTimer'
_L='fsGvrpDynamicVlanCreateStauts'
_K='fsGvrpStatus'
_J='fsGvrpStatsIfIndex'
_I='not-accessible'
_H='fsGvrpIfIndex'
_G='VlanId'
_F='Integer32'
_E='EnabledStatus'
_D='read-write'
_C='read-only'
_B='FS-GVRP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
IfIndex,=mibBuilder.importSymbols('FS-TC','IfIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_E)
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsGvrpMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,25))
if mibBuilder.loadTexts:fsGvrpMIB.setRevisions(('2002-03-20 00:00',))
_FsGvrpMIBObjects_ObjectIdentity=ObjectIdentity
fsGvrpMIBObjects=_FsGvrpMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,25,1))
class _FsGvrpStatus_Type(EnabledStatus):defaultValue=2
_FsGvrpStatus_Type.__name__=_E
_FsGvrpStatus_Object=MibScalar
fsGvrpStatus=_FsGvrpStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,1),_FsGvrpStatus_Type())
fsGvrpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsGvrpStatus.setStatus(_A)
class _FsGvrpDynamicVlanCreateStauts_Type(EnabledStatus):defaultValue=2
_FsGvrpDynamicVlanCreateStauts_Type.__name__=_E
_FsGvrpDynamicVlanCreateStauts_Object=MibScalar
fsGvrpDynamicVlanCreateStauts=_FsGvrpDynamicVlanCreateStauts_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,2),_FsGvrpDynamicVlanCreateStauts_Type())
fsGvrpDynamicVlanCreateStauts.setMaxAccess(_D)
if mibBuilder.loadTexts:fsGvrpDynamicVlanCreateStauts.setStatus(_A)
class _FsGvrpJoinTimer_Type(Integer32):defaultValue=200
_FsGvrpJoinTimer_Type.__name__=_F
_FsGvrpJoinTimer_Object=MibScalar
fsGvrpJoinTimer=_FsGvrpJoinTimer_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,3),_FsGvrpJoinTimer_Type())
fsGvrpJoinTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:fsGvrpJoinTimer.setStatus(_A)
class _FsGvrpLeaveTimer_Type(Integer32):defaultValue=600
_FsGvrpLeaveTimer_Type.__name__=_F
_FsGvrpLeaveTimer_Object=MibScalar
fsGvrpLeaveTimer=_FsGvrpLeaveTimer_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,4),_FsGvrpLeaveTimer_Type())
fsGvrpLeaveTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:fsGvrpLeaveTimer.setStatus(_A)
class _FsGvrpLeaveAllTimer_Type(Integer32):defaultValue=10000
_FsGvrpLeaveAllTimer_Type.__name__=_F
_FsGvrpLeaveAllTimer_Object=MibScalar
fsGvrpLeaveAllTimer=_FsGvrpLeaveAllTimer_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,5),_FsGvrpLeaveAllTimer_Type())
fsGvrpLeaveAllTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:fsGvrpLeaveAllTimer.setStatus(_A)
_FsGvrpTable_Object=MibTable
fsGvrpTable=_FsGvrpTable_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,6))
if mibBuilder.loadTexts:fsGvrpTable.setStatus(_A)
_FsGvrpEntry_Object=MibTableRow
fsGvrpEntry=_FsGvrpEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,6,1))
fsGvrpEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:fsGvrpEntry.setStatus(_A)
_FsGvrpIfIndex_Type=IfIndex
_FsGvrpIfIndex_Object=MibTableColumn
fsGvrpIfIndex=_FsGvrpIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,6,1,1),_FsGvrpIfIndex_Type())
fsGvrpIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:fsGvrpIfIndex.setStatus(_A)
class _FsGvrpRegistrationMode_Type(EnabledStatus):defaultValue=1
_FsGvrpRegistrationMode_Type.__name__=_E
_FsGvrpRegistrationMode_Object=MibTableColumn
fsGvrpRegistrationMode=_FsGvrpRegistrationMode_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,6,1,2),_FsGvrpRegistrationMode_Type())
fsGvrpRegistrationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsGvrpRegistrationMode.setStatus(_A)
class _FsGvrpApplicantState_Type(EnabledStatus):defaultValue=1
_FsGvrpApplicantState_Type.__name__=_E
_FsGvrpApplicantState_Object=MibTableColumn
fsGvrpApplicantState=_FsGvrpApplicantState_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,6,1,3),_FsGvrpApplicantState_Type())
fsGvrpApplicantState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsGvrpApplicantState.setStatus(_A)
_FsGvrpStatsTable_Object=MibTable
fsGvrpStatsTable=_FsGvrpStatsTable_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,7))
if mibBuilder.loadTexts:fsGvrpStatsTable.setStatus(_A)
_FsGvrpStatsEntry_Object=MibTableRow
fsGvrpStatsEntry=_FsGvrpStatsEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,7,1))
fsGvrpStatsEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:fsGvrpStatsEntry.setStatus(_A)
_FsGvrpStatsIfIndex_Type=IfIndex
_FsGvrpStatsIfIndex_Object=MibTableColumn
fsGvrpStatsIfIndex=_FsGvrpStatsIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,7,1,1),_FsGvrpStatsIfIndex_Type())
fsGvrpStatsIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:fsGvrpStatsIfIndex.setStatus(_A)
_FsGvrpRecValidGvrpPdu_Type=Counter32
_FsGvrpRecValidGvrpPdu_Object=MibTableColumn
fsGvrpRecValidGvrpPdu=_FsGvrpRecValidGvrpPdu_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,7,1,2),_FsGvrpRecValidGvrpPdu_Type())
fsGvrpRecValidGvrpPdu.setMaxAccess(_C)
if mibBuilder.loadTexts:fsGvrpRecValidGvrpPdu.setStatus(_A)
_FsGvrpRecInvalidGvrpPdu_Type=Counter32
_FsGvrpRecInvalidGvrpPdu_Object=MibTableColumn
fsGvrpRecInvalidGvrpPdu=_FsGvrpRecInvalidGvrpPdu_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,7,1,3),_FsGvrpRecInvalidGvrpPdu_Type())
fsGvrpRecInvalidGvrpPdu.setMaxAccess(_C)
if mibBuilder.loadTexts:fsGvrpRecInvalidGvrpPdu.setStatus(_A)
_FsGvrpRecJoin_Type=Counter32
_FsGvrpRecJoin_Object=MibTableColumn
fsGvrpRecJoin=_FsGvrpRecJoin_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,7,1,4),_FsGvrpRecJoin_Type())
fsGvrpRecJoin.setMaxAccess(_C)
if mibBuilder.loadTexts:fsGvrpRecJoin.setStatus(_A)
_FsGvrpRecJoinIn_Type=Counter32
_FsGvrpRecJoinIn_Object=MibTableColumn
fsGvrpRecJoinIn=_FsGvrpRecJoinIn_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,7,1,5),_FsGvrpRecJoinIn_Type())
fsGvrpRecJoinIn.setMaxAccess(_C)
if mibBuilder.loadTexts:fsGvrpRecJoinIn.setStatus(_A)
_FsGvrpRecEmpty_Type=Counter32
_FsGvrpRecEmpty_Object=MibTableColumn
fsGvrpRecEmpty=_FsGvrpRecEmpty_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,7,1,6),_FsGvrpRecEmpty_Type())
fsGvrpRecEmpty.setMaxAccess(_C)
if mibBuilder.loadTexts:fsGvrpRecEmpty.setStatus(_A)
_FsGvrpRecLeaveEmpty_Type=Counter32
_FsGvrpRecLeaveEmpty_Object=MibTableColumn
fsGvrpRecLeaveEmpty=_FsGvrpRecLeaveEmpty_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,7,1,7),_FsGvrpRecLeaveEmpty_Type())
fsGvrpRecLeaveEmpty.setMaxAccess(_C)
if mibBuilder.loadTexts:fsGvrpRecLeaveEmpty.setStatus(_A)
_FsGvrpRecLeaveIn_Type=Counter32
_FsGvrpRecLeaveIn_Object=MibTableColumn
fsGvrpRecLeaveIn=_FsGvrpRecLeaveIn_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,7,1,8),_FsGvrpRecLeaveIn_Type())
fsGvrpRecLeaveIn.setMaxAccess(_C)
if mibBuilder.loadTexts:fsGvrpRecLeaveIn.setStatus(_A)
_FsGvrpRecLeaveAll_Type=Counter32
_FsGvrpRecLeaveAll_Object=MibTableColumn
fsGvrpRecLeaveAll=_FsGvrpRecLeaveAll_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,7,1,9),_FsGvrpRecLeaveAll_Type())
fsGvrpRecLeaveAll.setMaxAccess(_C)
if mibBuilder.loadTexts:fsGvrpRecLeaveAll.setStatus(_A)
_FsGvrpSentGvrpPdu_Type=Counter32
_FsGvrpSentGvrpPdu_Object=MibTableColumn
fsGvrpSentGvrpPdu=_FsGvrpSentGvrpPdu_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,7,1,10),_FsGvrpSentGvrpPdu_Type())
fsGvrpSentGvrpPdu.setMaxAccess(_C)
if mibBuilder.loadTexts:fsGvrpSentGvrpPdu.setStatus(_A)
_FsGvrpSentJoin_Type=Counter32
_FsGvrpSentJoin_Object=MibTableColumn
fsGvrpSentJoin=_FsGvrpSentJoin_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,7,1,11),_FsGvrpSentJoin_Type())
fsGvrpSentJoin.setMaxAccess(_C)
if mibBuilder.loadTexts:fsGvrpSentJoin.setStatus(_A)
_FsGvrpSentJoinIn_Type=Counter32
_FsGvrpSentJoinIn_Object=MibTableColumn
fsGvrpSentJoinIn=_FsGvrpSentJoinIn_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,7,1,12),_FsGvrpSentJoinIn_Type())
fsGvrpSentJoinIn.setMaxAccess(_C)
if mibBuilder.loadTexts:fsGvrpSentJoinIn.setStatus(_A)
_FsGvrpSentEmpty_Type=Counter32
_FsGvrpSentEmpty_Object=MibTableColumn
fsGvrpSentEmpty=_FsGvrpSentEmpty_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,7,1,13),_FsGvrpSentEmpty_Type())
fsGvrpSentEmpty.setMaxAccess(_C)
if mibBuilder.loadTexts:fsGvrpSentEmpty.setStatus(_A)
_FsGvrpSentLeaveEmpty_Type=Counter32
_FsGvrpSentLeaveEmpty_Object=MibTableColumn
fsGvrpSentLeaveEmpty=_FsGvrpSentLeaveEmpty_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,7,1,14),_FsGvrpSentLeaveEmpty_Type())
fsGvrpSentLeaveEmpty.setMaxAccess(_C)
if mibBuilder.loadTexts:fsGvrpSentLeaveEmpty.setStatus(_A)
_FsGvrpSentLeaveIn_Type=Counter32
_FsGvrpSentLeaveIn_Object=MibTableColumn
fsGvrpSentLeaveIn=_FsGvrpSentLeaveIn_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,7,1,15),_FsGvrpSentLeaveIn_Type())
fsGvrpSentLeaveIn.setMaxAccess(_C)
if mibBuilder.loadTexts:fsGvrpSentLeaveIn.setStatus(_A)
_FsGvrpSentLeaveAll_Type=Counter32
_FsGvrpSentLeaveAll_Object=MibTableColumn
fsGvrpSentLeaveAll=_FsGvrpSentLeaveAll_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,7,1,16),_FsGvrpSentLeaveAll_Type())
fsGvrpSentLeaveAll.setMaxAccess(_C)
if mibBuilder.loadTexts:fsGvrpSentLeaveAll.setStatus(_A)
_FsGvrpJoinIndicated_Type=Counter32
_FsGvrpJoinIndicated_Object=MibTableColumn
fsGvrpJoinIndicated=_FsGvrpJoinIndicated_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,7,1,17),_FsGvrpJoinIndicated_Type())
fsGvrpJoinIndicated.setMaxAccess(_C)
if mibBuilder.loadTexts:fsGvrpJoinIndicated.setStatus(_A)
_FsGvrpLeaveIndicated_Type=Counter32
_FsGvrpLeaveIndicated_Object=MibTableColumn
fsGvrpLeaveIndicated=_FsGvrpLeaveIndicated_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,7,1,18),_FsGvrpLeaveIndicated_Type())
fsGvrpLeaveIndicated.setMaxAccess(_C)
if mibBuilder.loadTexts:fsGvrpLeaveIndicated.setStatus(_A)
_FsGvrpJoinPropagated_Type=Counter32
_FsGvrpJoinPropagated_Object=MibTableColumn
fsGvrpJoinPropagated=_FsGvrpJoinPropagated_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,7,1,19),_FsGvrpJoinPropagated_Type())
fsGvrpJoinPropagated.setMaxAccess(_C)
if mibBuilder.loadTexts:fsGvrpJoinPropagated.setStatus(_A)
_FsGvrpLeavePropagated_Type=Counter32
_FsGvrpLeavePropagated_Object=MibTableColumn
fsGvrpLeavePropagated=_FsGvrpLeavePropagated_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,7,1,20),_FsGvrpLeavePropagated_Type())
fsGvrpLeavePropagated.setMaxAccess(_C)
if mibBuilder.loadTexts:fsGvrpLeavePropagated.setStatus(_A)
_FsGvrpStatisticsPortClear_Type=Integer32
_FsGvrpStatisticsPortClear_Object=MibTableColumn
fsGvrpStatisticsPortClear=_FsGvrpStatisticsPortClear_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,7,1,21),_FsGvrpStatisticsPortClear_Type())
fsGvrpStatisticsPortClear.setMaxAccess(_D)
if mibBuilder.loadTexts:fsGvrpStatisticsPortClear.setStatus(_A)
class _FsGvrpOperVid_Type(VlanId):defaultValue=1
_FsGvrpOperVid_Type.__name__=_G
_FsGvrpOperVid_Object=MibScalar
fsGvrpOperVid=_FsGvrpOperVid_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,8),_FsGvrpOperVid_Type())
fsGvrpOperVid.setMaxAccess(_D)
if mibBuilder.loadTexts:fsGvrpOperVid.setStatus(_A)
_FsGvrpStatisticsClear_Type=Integer32
_FsGvrpStatisticsClear_Object=MibScalar
fsGvrpStatisticsClear=_FsGvrpStatisticsClear_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,9),_FsGvrpStatisticsClear_Type())
fsGvrpStatisticsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:fsGvrpStatisticsClear.setStatus(_A)
_FsGvrpResetTimer_Type=VlanId
_FsGvrpResetTimer_Object=MibScalar
fsGvrpResetTimer=_FsGvrpResetTimer_Object((1,3,6,1,4,1,52642,1,1,10,2,25,1,10),_FsGvrpResetTimer_Type())
fsGvrpResetTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:fsGvrpResetTimer.setStatus(_A)
_FsGvrpMIBConformance_ObjectIdentity=ObjectIdentity
fsGvrpMIBConformance=_FsGvrpMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,25,2))
_FsGvrpMIBCompliances_ObjectIdentity=ObjectIdentity
fsGvrpMIBCompliances=_FsGvrpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,25,2,1))
_FsGvrpMIBGroups_ObjectIdentity=ObjectIdentity
fsGvrpMIBGroups=_FsGvrpMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,25,2,2))
fsGvrpMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,25,2,2,1))
fsGvrpMIBGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:fsGvrpMIBGroup.setStatus(_A)
fsGvrpStatsMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,25,2,2,2))
fsGvrpStatsMIBGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:fsGvrpStatsMIBGroup.setStatus(_A)
fsGvrpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,25,2,1,1))
fsGvrpMIBCompliance.setObjects(*((_B,_l),(_B,_m)))
if mibBuilder.loadTexts:fsGvrpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsGvrpMIB':fsGvrpMIB,'fsGvrpMIBObjects':fsGvrpMIBObjects,_K:fsGvrpStatus,_L:fsGvrpDynamicVlanCreateStauts,_M:fsGvrpJoinTimer,_N:fsGvrpLeaveTimer,_O:fsGvrpLeaveAllTimer,'fsGvrpTable':fsGvrpTable,'fsGvrpEntry':fsGvrpEntry,_H:fsGvrpIfIndex,_P:fsGvrpRegistrationMode,_Q:fsGvrpApplicantState,'fsGvrpStatsTable':fsGvrpStatsTable,'fsGvrpStatsEntry':fsGvrpStatsEntry,_J:fsGvrpStatsIfIndex,_R:fsGvrpRecValidGvrpPdu,_S:fsGvrpRecInvalidGvrpPdu,_T:fsGvrpRecJoin,_U:fsGvrpRecJoinIn,_V:fsGvrpRecEmpty,_W:fsGvrpRecLeaveEmpty,_X:fsGvrpRecLeaveIn,_Y:fsGvrpRecLeaveAll,_Z:fsGvrpSentGvrpPdu,_a:fsGvrpSentJoin,_b:fsGvrpSentJoinIn,_c:fsGvrpSentEmpty,_d:fsGvrpSentLeaveEmpty,_e:fsGvrpSentLeaveIn,_f:fsGvrpSentLeaveAll,_g:fsGvrpJoinIndicated,_h:fsGvrpLeaveIndicated,_i:fsGvrpJoinPropagated,_j:fsGvrpLeavePropagated,_k:fsGvrpStatisticsPortClear,'fsGvrpOperVid':fsGvrpOperVid,'fsGvrpStatisticsClear':fsGvrpStatisticsClear,'fsGvrpResetTimer':fsGvrpResetTimer,'fsGvrpMIBConformance':fsGvrpMIBConformance,'fsGvrpMIBCompliances':fsGvrpMIBCompliances,'fsGvrpMIBCompliance':fsGvrpMIBCompliance,'fsGvrpMIBGroups':fsGvrpMIBGroups,_l:fsGvrpMIBGroup,_m:fsGvrpStatsMIBGroup})