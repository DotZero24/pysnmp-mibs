_o='hpicfMvrpNotifyGroup'
_n='hpicfMvrpPortStateGroup'
_m='hpicfMvrpPortStatsGroup'
_l='hpicfMvrpPortConfigGroup'
_k='hpicfMvrpBaseGroup'
_j='hpicfMvrpVlanLimitReachedEvent'
_i='hpicfMvrpRegistrarState'
_h='hpicfMvrpApplicantState'
_g='hpicfMvrpPortStatsFramesDiscarded'
_f='hpicfMvrpPortStatsTotalPDUTransmitted'
_e='hpicfMvrpPortStatsTotalPDUReceived'
_d='hpicfMvrpPortStatsLeaveAllTransmitted'
_c='hpicfMvrpPortStatsEmptyTransmitted'
_b='hpicfMvrpPortStatsInTransmitted'
_a='hpicfMvrpPortStatsLeaveTransmitted'
_Z='hpicfMvrpPortStatsJoinEmptyTransmitted'
_Y='hpicfMvrpPortStatsJoinInTransmitted'
_X='hpicfMvrpPortStatsNewTransmitted'
_W='hpicfMvrpPortStatsLeaveAllReceived'
_V='hpicfMvrpPortStatsEmptyReceived'
_U='hpicfMvrpPortStatsInReceived'
_T='hpicfMvrpPortStatsLeaveReceived'
_S='hpicfMvrpPortStatsJoinEmptyReceived'
_R='hpicfMvrpPortStatsJoinInReceived'
_Q='hpicfMvrpPortStatsNewReceived'
_P='hpicfMvrpPortStatsClearStats'
_O='hpicfMvrpPortConfigPeriodicTransmissionStatus'
_N='hpicfMvrpPortConfigPeriodicTimer'
_M='hpicfMvrpPortConfigRegistrarMode'
_L='hpicfMvrpGlobalClearStats'
_K='hpicfMvrpVlanId'
_J='TimeInterval'
_I='EnabledStatus'
_H='hpicfMvrpMaxVlanLimit'
_G='Integer32'
_F='ifIndex'
_E='IF-MIB'
_D='read-write'
_C='read-only'
_B='HP-ICF-MVRP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ifIndex,=mibBuilder.importSymbols(_E,_F)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_I)
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_J,'TruthValue')
hpicfMvrpMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,117))
if mibBuilder.loadTexts:hpicfMvrpMIB.setRevisions(('2015-04-20 00:00','2015-03-24 00:00'))
_HpicfMvrpNotifications_ObjectIdentity=ObjectIdentity
hpicfMvrpNotifications=_HpicfMvrpNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,117,0))
_HpicfMvrpObjects_ObjectIdentity=ObjectIdentity
hpicfMvrpObjects=_HpicfMvrpObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,117,1))
_HpicfMvrpConfig_ObjectIdentity=ObjectIdentity
hpicfMvrpConfig=_HpicfMvrpConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,117,1,1))
_HpicfMvrpGlobalClearStats_Type=TruthValue
_HpicfMvrpGlobalClearStats_Object=MibScalar
hpicfMvrpGlobalClearStats=_HpicfMvrpGlobalClearStats_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,1,1),_HpicfMvrpGlobalClearStats_Type())
hpicfMvrpGlobalClearStats.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfMvrpGlobalClearStats.setStatus(_A)
_HpicfMvrpMaxVlanLimit_Type=Integer32
_HpicfMvrpMaxVlanLimit_Object=MibScalar
hpicfMvrpMaxVlanLimit=_HpicfMvrpMaxVlanLimit_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,1,2),_HpicfMvrpMaxVlanLimit_Type())
hpicfMvrpMaxVlanLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfMvrpMaxVlanLimit.setStatus(_A)
_HpicfMvrpPortConfigTable_Object=MibTable
hpicfMvrpPortConfigTable=_HpicfMvrpPortConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,1,3))
if mibBuilder.loadTexts:hpicfMvrpPortConfigTable.setStatus(_A)
_HpicfMvrpPortConfigEntry_Object=MibTableRow
hpicfMvrpPortConfigEntry=_HpicfMvrpPortConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,1,3,1))
hpicfMvrpPortConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hpicfMvrpPortConfigEntry.setStatus(_A)
class _HpicfMvrpPortConfigRegistrarMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('fixed',2)))
_HpicfMvrpPortConfigRegistrarMode_Type.__name__=_G
_HpicfMvrpPortConfigRegistrarMode_Object=MibTableColumn
hpicfMvrpPortConfigRegistrarMode=_HpicfMvrpPortConfigRegistrarMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,1,3,1,1),_HpicfMvrpPortConfigRegistrarMode_Type())
hpicfMvrpPortConfigRegistrarMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfMvrpPortConfigRegistrarMode.setStatus(_A)
class _HpicfMvrpPortConfigPeriodicTimer_Type(TimeInterval):defaultValue=100;subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000000))
_HpicfMvrpPortConfigPeriodicTimer_Type.__name__=_J
_HpicfMvrpPortConfigPeriodicTimer_Object=MibTableColumn
hpicfMvrpPortConfigPeriodicTimer=_HpicfMvrpPortConfigPeriodicTimer_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,1,3,1,2),_HpicfMvrpPortConfigPeriodicTimer_Type())
hpicfMvrpPortConfigPeriodicTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfMvrpPortConfigPeriodicTimer.setStatus(_A)
if mibBuilder.loadTexts:hpicfMvrpPortConfigPeriodicTimer.setUnits('centi-seconds')
class _HpicfMvrpPortConfigPeriodicTransmissionStatus_Type(EnabledStatus):defaultValue=1
_HpicfMvrpPortConfigPeriodicTransmissionStatus_Type.__name__=_I
_HpicfMvrpPortConfigPeriodicTransmissionStatus_Object=MibTableColumn
hpicfMvrpPortConfigPeriodicTransmissionStatus=_HpicfMvrpPortConfigPeriodicTransmissionStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,1,3,1,3),_HpicfMvrpPortConfigPeriodicTransmissionStatus_Type())
hpicfMvrpPortConfigPeriodicTransmissionStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfMvrpPortConfigPeriodicTransmissionStatus.setStatus(_A)
_HpicfMvrpPortStatsClearStats_Type=TruthValue
_HpicfMvrpPortStatsClearStats_Object=MibTableColumn
hpicfMvrpPortStatsClearStats=_HpicfMvrpPortStatsClearStats_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,1,3,1,4),_HpicfMvrpPortStatsClearStats_Type())
hpicfMvrpPortStatsClearStats.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfMvrpPortStatsClearStats.setStatus(_A)
_HpicfMvrpStats_ObjectIdentity=ObjectIdentity
hpicfMvrpStats=_HpicfMvrpStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2))
_HpicfMvrpPortStatsTable_Object=MibTable
hpicfMvrpPortStatsTable=_HpicfMvrpPortStatsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2,1))
if mibBuilder.loadTexts:hpicfMvrpPortStatsTable.setStatus(_A)
_HpicfMvrpPortStatsEntry_Object=MibTableRow
hpicfMvrpPortStatsEntry=_HpicfMvrpPortStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2,1,1))
hpicfMvrpPortStatsEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hpicfMvrpPortStatsEntry.setStatus(_A)
_HpicfMvrpPortStatsNewReceived_Type=Counter32
_HpicfMvrpPortStatsNewReceived_Object=MibTableColumn
hpicfMvrpPortStatsNewReceived=_HpicfMvrpPortStatsNewReceived_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2,1,1,1),_HpicfMvrpPortStatsNewReceived_Type())
hpicfMvrpPortStatsNewReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMvrpPortStatsNewReceived.setStatus(_A)
_HpicfMvrpPortStatsJoinInReceived_Type=Counter32
_HpicfMvrpPortStatsJoinInReceived_Object=MibTableColumn
hpicfMvrpPortStatsJoinInReceived=_HpicfMvrpPortStatsJoinInReceived_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2,1,1,2),_HpicfMvrpPortStatsJoinInReceived_Type())
hpicfMvrpPortStatsJoinInReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMvrpPortStatsJoinInReceived.setStatus(_A)
_HpicfMvrpPortStatsJoinEmptyReceived_Type=Counter32
_HpicfMvrpPortStatsJoinEmptyReceived_Object=MibTableColumn
hpicfMvrpPortStatsJoinEmptyReceived=_HpicfMvrpPortStatsJoinEmptyReceived_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2,1,1,3),_HpicfMvrpPortStatsJoinEmptyReceived_Type())
hpicfMvrpPortStatsJoinEmptyReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMvrpPortStatsJoinEmptyReceived.setStatus(_A)
_HpicfMvrpPortStatsLeaveReceived_Type=Counter32
_HpicfMvrpPortStatsLeaveReceived_Object=MibTableColumn
hpicfMvrpPortStatsLeaveReceived=_HpicfMvrpPortStatsLeaveReceived_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2,1,1,4),_HpicfMvrpPortStatsLeaveReceived_Type())
hpicfMvrpPortStatsLeaveReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMvrpPortStatsLeaveReceived.setStatus(_A)
_HpicfMvrpPortStatsInReceived_Type=Counter32
_HpicfMvrpPortStatsInReceived_Object=MibTableColumn
hpicfMvrpPortStatsInReceived=_HpicfMvrpPortStatsInReceived_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2,1,1,5),_HpicfMvrpPortStatsInReceived_Type())
hpicfMvrpPortStatsInReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMvrpPortStatsInReceived.setStatus(_A)
_HpicfMvrpPortStatsEmptyReceived_Type=Counter32
_HpicfMvrpPortStatsEmptyReceived_Object=MibTableColumn
hpicfMvrpPortStatsEmptyReceived=_HpicfMvrpPortStatsEmptyReceived_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2,1,1,6),_HpicfMvrpPortStatsEmptyReceived_Type())
hpicfMvrpPortStatsEmptyReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMvrpPortStatsEmptyReceived.setStatus(_A)
_HpicfMvrpPortStatsLeaveAllReceived_Type=Counter32
_HpicfMvrpPortStatsLeaveAllReceived_Object=MibTableColumn
hpicfMvrpPortStatsLeaveAllReceived=_HpicfMvrpPortStatsLeaveAllReceived_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2,1,1,7),_HpicfMvrpPortStatsLeaveAllReceived_Type())
hpicfMvrpPortStatsLeaveAllReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMvrpPortStatsLeaveAllReceived.setStatus(_A)
_HpicfMvrpPortStatsNewTransmitted_Type=Counter32
_HpicfMvrpPortStatsNewTransmitted_Object=MibTableColumn
hpicfMvrpPortStatsNewTransmitted=_HpicfMvrpPortStatsNewTransmitted_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2,1,1,8),_HpicfMvrpPortStatsNewTransmitted_Type())
hpicfMvrpPortStatsNewTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMvrpPortStatsNewTransmitted.setStatus(_A)
_HpicfMvrpPortStatsJoinInTransmitted_Type=Counter32
_HpicfMvrpPortStatsJoinInTransmitted_Object=MibTableColumn
hpicfMvrpPortStatsJoinInTransmitted=_HpicfMvrpPortStatsJoinInTransmitted_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2,1,1,9),_HpicfMvrpPortStatsJoinInTransmitted_Type())
hpicfMvrpPortStatsJoinInTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMvrpPortStatsJoinInTransmitted.setStatus(_A)
_HpicfMvrpPortStatsJoinEmptyTransmitted_Type=Counter32
_HpicfMvrpPortStatsJoinEmptyTransmitted_Object=MibTableColumn
hpicfMvrpPortStatsJoinEmptyTransmitted=_HpicfMvrpPortStatsJoinEmptyTransmitted_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2,1,1,10),_HpicfMvrpPortStatsJoinEmptyTransmitted_Type())
hpicfMvrpPortStatsJoinEmptyTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMvrpPortStatsJoinEmptyTransmitted.setStatus(_A)
_HpicfMvrpPortStatsLeaveTransmitted_Type=Counter32
_HpicfMvrpPortStatsLeaveTransmitted_Object=MibTableColumn
hpicfMvrpPortStatsLeaveTransmitted=_HpicfMvrpPortStatsLeaveTransmitted_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2,1,1,11),_HpicfMvrpPortStatsLeaveTransmitted_Type())
hpicfMvrpPortStatsLeaveTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMvrpPortStatsLeaveTransmitted.setStatus(_A)
_HpicfMvrpPortStatsInTransmitted_Type=Counter32
_HpicfMvrpPortStatsInTransmitted_Object=MibTableColumn
hpicfMvrpPortStatsInTransmitted=_HpicfMvrpPortStatsInTransmitted_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2,1,1,12),_HpicfMvrpPortStatsInTransmitted_Type())
hpicfMvrpPortStatsInTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMvrpPortStatsInTransmitted.setStatus(_A)
_HpicfMvrpPortStatsEmptyTransmitted_Type=Counter32
_HpicfMvrpPortStatsEmptyTransmitted_Object=MibTableColumn
hpicfMvrpPortStatsEmptyTransmitted=_HpicfMvrpPortStatsEmptyTransmitted_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2,1,1,13),_HpicfMvrpPortStatsEmptyTransmitted_Type())
hpicfMvrpPortStatsEmptyTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMvrpPortStatsEmptyTransmitted.setStatus(_A)
_HpicfMvrpPortStatsLeaveAllTransmitted_Type=Counter32
_HpicfMvrpPortStatsLeaveAllTransmitted_Object=MibTableColumn
hpicfMvrpPortStatsLeaveAllTransmitted=_HpicfMvrpPortStatsLeaveAllTransmitted_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2,1,1,14),_HpicfMvrpPortStatsLeaveAllTransmitted_Type())
hpicfMvrpPortStatsLeaveAllTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMvrpPortStatsLeaveAllTransmitted.setStatus(_A)
_HpicfMvrpPortStatsTotalPDUReceived_Type=Counter32
_HpicfMvrpPortStatsTotalPDUReceived_Object=MibTableColumn
hpicfMvrpPortStatsTotalPDUReceived=_HpicfMvrpPortStatsTotalPDUReceived_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2,1,1,15),_HpicfMvrpPortStatsTotalPDUReceived_Type())
hpicfMvrpPortStatsTotalPDUReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMvrpPortStatsTotalPDUReceived.setStatus(_A)
_HpicfMvrpPortStatsTotalPDUTransmitted_Type=Counter32
_HpicfMvrpPortStatsTotalPDUTransmitted_Object=MibTableColumn
hpicfMvrpPortStatsTotalPDUTransmitted=_HpicfMvrpPortStatsTotalPDUTransmitted_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2,1,1,16),_HpicfMvrpPortStatsTotalPDUTransmitted_Type())
hpicfMvrpPortStatsTotalPDUTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMvrpPortStatsTotalPDUTransmitted.setStatus(_A)
_HpicfMvrpPortStatsFramesDiscarded_Type=Counter32
_HpicfMvrpPortStatsFramesDiscarded_Object=MibTableColumn
hpicfMvrpPortStatsFramesDiscarded=_HpicfMvrpPortStatsFramesDiscarded_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2,1,1,17),_HpicfMvrpPortStatsFramesDiscarded_Type())
hpicfMvrpPortStatsFramesDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMvrpPortStatsFramesDiscarded.setStatus(_A)
_HpicfBridgeMvrpStateTable_Object=MibTable
hpicfBridgeMvrpStateTable=_HpicfBridgeMvrpStateTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2,2))
if mibBuilder.loadTexts:hpicfBridgeMvrpStateTable.setStatus(_A)
_HpicfBridgeMvrpStateEntry_Object=MibTableRow
hpicfBridgeMvrpStateEntry=_HpicfBridgeMvrpStateEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2,2,1))
hpicfBridgeMvrpStateEntry.setIndexNames((0,_B,_K),(0,_E,_F))
if mibBuilder.loadTexts:hpicfBridgeMvrpStateEntry.setStatus(_A)
_HpicfMvrpVlanId_Type=VlanId
_HpicfMvrpVlanId_Object=MibTableColumn
hpicfMvrpVlanId=_HpicfMvrpVlanId_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2,2,1,1),_HpicfMvrpVlanId_Type())
hpicfMvrpVlanId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpicfMvrpVlanId.setStatus(_A)
class _HpicfMvrpApplicantState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('aa',0),('qa',1),('la',2),('vp',3),('ap',4),('qp',5),('vo',6),('ao',7),('qo',8),('lo',9),('vn',10),('an',11)))
_HpicfMvrpApplicantState_Type.__name__=_G
_HpicfMvrpApplicantState_Object=MibTableColumn
hpicfMvrpApplicantState=_HpicfMvrpApplicantState_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2,2,1,2),_HpicfMvrpApplicantState_Type())
hpicfMvrpApplicantState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMvrpApplicantState.setStatus(_A)
class _HpicfMvrpRegistrarState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('in',1),('lv',2),('mt',3)))
_HpicfMvrpRegistrarState_Type.__name__=_G
_HpicfMvrpRegistrarState_Object=MibTableColumn
hpicfMvrpRegistrarState=_HpicfMvrpRegistrarState_Object((1,3,6,1,4,1,11,2,14,11,5,1,117,1,2,2,1,3),_HpicfMvrpRegistrarState_Type())
hpicfMvrpRegistrarState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMvrpRegistrarState.setStatus(_A)
_HpicfMvrpConformance_ObjectIdentity=ObjectIdentity
hpicfMvrpConformance=_HpicfMvrpConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,117,3))
_HpicfMvrpCompliances_ObjectIdentity=ObjectIdentity
hpicfMvrpCompliances=_HpicfMvrpCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,117,3,1))
_HpicfMvrpGroups_ObjectIdentity=ObjectIdentity
hpicfMvrpGroups=_HpicfMvrpGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,117,3,2))
hpicfMvrpBaseGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,117,3,2,1))
hpicfMvrpBaseGroup.setObjects(*((_B,_L),(_B,_H)))
if mibBuilder.loadTexts:hpicfMvrpBaseGroup.setStatus(_A)
hpicfMvrpPortConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,117,3,2,2))
hpicfMvrpPortConfigGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:hpicfMvrpPortConfigGroup.setStatus(_A)
hpicfMvrpPortStatsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,117,3,2,3))
hpicfMvrpPortStatsGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:hpicfMvrpPortStatsGroup.setStatus(_A)
hpicfMvrpPortStateGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,117,3,2,4))
hpicfMvrpPortStateGroup.setObjects(*((_B,_h),(_B,_i)))
if mibBuilder.loadTexts:hpicfMvrpPortStateGroup.setStatus(_A)
hpicfMvrpVlanLimitReachedEvent=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,117,0,1))
hpicfMvrpVlanLimitReachedEvent.setObjects((_B,_H))
if mibBuilder.loadTexts:hpicfMvrpVlanLimitReachedEvent.setStatus(_A)
hpicfMvrpNotifyGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,5,1,117,3,2,5))
hpicfMvrpNotifyGroup.setObjects((_B,_j))
if mibBuilder.loadTexts:hpicfMvrpNotifyGroup.setStatus(_A)
hpicfMvrpCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,117,3,1,1))
hpicfMvrpCompliance.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:hpicfMvrpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfMvrpMIB':hpicfMvrpMIB,'hpicfMvrpNotifications':hpicfMvrpNotifications,_j:hpicfMvrpVlanLimitReachedEvent,'hpicfMvrpObjects':hpicfMvrpObjects,'hpicfMvrpConfig':hpicfMvrpConfig,_L:hpicfMvrpGlobalClearStats,_H:hpicfMvrpMaxVlanLimit,'hpicfMvrpPortConfigTable':hpicfMvrpPortConfigTable,'hpicfMvrpPortConfigEntry':hpicfMvrpPortConfigEntry,_M:hpicfMvrpPortConfigRegistrarMode,_N:hpicfMvrpPortConfigPeriodicTimer,_O:hpicfMvrpPortConfigPeriodicTransmissionStatus,_P:hpicfMvrpPortStatsClearStats,'hpicfMvrpStats':hpicfMvrpStats,'hpicfMvrpPortStatsTable':hpicfMvrpPortStatsTable,'hpicfMvrpPortStatsEntry':hpicfMvrpPortStatsEntry,_Q:hpicfMvrpPortStatsNewReceived,_R:hpicfMvrpPortStatsJoinInReceived,_S:hpicfMvrpPortStatsJoinEmptyReceived,_T:hpicfMvrpPortStatsLeaveReceived,_U:hpicfMvrpPortStatsInReceived,_V:hpicfMvrpPortStatsEmptyReceived,_W:hpicfMvrpPortStatsLeaveAllReceived,_X:hpicfMvrpPortStatsNewTransmitted,_Y:hpicfMvrpPortStatsJoinInTransmitted,_Z:hpicfMvrpPortStatsJoinEmptyTransmitted,_a:hpicfMvrpPortStatsLeaveTransmitted,_b:hpicfMvrpPortStatsInTransmitted,_c:hpicfMvrpPortStatsEmptyTransmitted,_d:hpicfMvrpPortStatsLeaveAllTransmitted,_e:hpicfMvrpPortStatsTotalPDUReceived,_f:hpicfMvrpPortStatsTotalPDUTransmitted,_g:hpicfMvrpPortStatsFramesDiscarded,'hpicfBridgeMvrpStateTable':hpicfBridgeMvrpStateTable,'hpicfBridgeMvrpStateEntry':hpicfBridgeMvrpStateEntry,_K:hpicfMvrpVlanId,_h:hpicfMvrpApplicantState,_i:hpicfMvrpRegistrarState,'hpicfMvrpConformance':hpicfMvrpConformance,'hpicfMvrpCompliances':hpicfMvrpCompliances,'hpicfMvrpCompliance':hpicfMvrpCompliance,'hpicfMvrpGroups':hpicfMvrpGroups,_k:hpicfMvrpBaseGroup,_l:hpicfMvrpPortConfigGroup,_m:hpicfMvrpPortStatsGroup,_n:hpicfMvrpPortStateGroup,_o:hpicfMvrpNotifyGroup})