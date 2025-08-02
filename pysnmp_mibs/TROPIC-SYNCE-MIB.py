_B2='tnSyncEPacketswitchControlGroup'
_B1='tnWanGroup'
_B0='tnSyncEBITSPortGroup'
_A_='tnSyncEStationClockGroup'
_Az='tnSyncEPortGroup'
_Ay='tnSyncEControlGroup'
_Ax='tnSyncELineRefGroup'
_Aw='tnSyncEGroup'
_Av='tnSyncEPacketswitchControlEECEnable'
_Au='tnWanDescription'
_At='tnWanOperationalCapability'
_As='tnWanStateQualifier'
_Ar='tnWanOperStatus'
_Aq='tnWanAdminStatus'
_Ap='tnWanSyncEOutgoingForceSsmTrans'
_Ao='tnWanSyncEOprMode'
_An='tnWanAlmProfName'
_Am='tnSyncEBITSPortAlmProfName'
_Al='tnSyncEBITSPortLbo'
_Ak='tnSyncEBITSPortLineCode'
_Aj='tnSyncEBITSPortLineImpedance'
_Ai='tnSyncEBITSPortOutputAISMode'
_Ah='tnSyncEBITSPortOutputSSMTrans'
_Ag='tnSyncEBITSPortSaBit'
_Af='tnSyncEBITSPortSignalType'
_Ae='tnSyncEBITSPortDirection'
_Ad='tnSyncEStationClockAlmProfName'
_Ac='tnSyncEStationClockOutSel'
_Ab='tnSyncEStationClockQLThreshold'
_Aa='tnSyncEStationClockSystemQL'
_AZ='tnSyncEStationClockSwCmdLineRef'
_AY='tnSyncEStationClockWTR'
_AX='tnSyncEStationClockActiveRef'
_AW='tnSyncEStationClockSyncMsg'
_AV='tnSyncEOutgoingForceSsmTrans'
_AU='tnSyncEOprMode'
_AT='tnSyncEControlEECEnable'
_AS='tnSyncELineRefIncSSMStatusOfStationClock'
_AR='tnSyncELineRefIncSSMMsgOfStationClock'
_AQ='tnSyncELineRefProvQLOfStationClock'
_AP='tnSyncELineRefIncExtdQLTLVNumEEC'
_AO='tnSyncELineRefIncExtdQLTLVNumeEEC'
_AN='tnSyncELineRefIncExtdQLTLVPartialChain'
_AM='tnSyncELineRefIncExtdQLTLVMixedClockType'
_AL='tnSyncELineRefIncExtdQLTLVClockID'
_AK='tnSyncELineRefAlmProfName'
_AJ='tnSyncELineRefCurrentFreqOff'
_AI='tnSyncELineRefSwStateOfStationClock'
_AH='tnSyncELineRefLockOutOfStationClock'
_AG='tnSyncELineRefPriorityOfStationClock'
_AF='tnSyncELineRefAssociatedPort'
_AE='tnSyncELineRefProvQL'
_AD='tnSyncELineRefIncSSMSupp'
_AC='tnSyncELineRefIncSSMStatus'
_AB='tnSyncELineRefIncSSMMsg'
_AA='tnSyncELineRefSwState'
_A9='tnSyncELineRefState'
_A8='tnSyncELineLockOut'
_A7='tnSyncELineRefOperState'
_A6='tnSyncELineRefAdminState'
_A5='tnSyncELineRefPriority'
_A4='tnSyncELineRefAssignedPort'
_A3='tnSyncEAlmProfName'
_A2='tnSyncECurrentActiveLineRefFreqOff'
_A1='tnSyncEQLDegradeThreshold'
_A0='tnSyncESystemQL'
_z='tnSyncEClkModState'
_y='tnSyncESwCmdLineRef'
_x='tnSyncEWTR'
_w='tnSyncEActiveRef'
_v='tnSyncESyncMsg'
_u='non-sync'
_t='lockout'
_s='forced'
_r='tnSyncELineRefIndex'
_q='lineRef5'
_p='lineRef4'
_o='lineRef3'
_n='lineRef2'
_m='lineRef1'
_l='lineRef0'
_k='tnSysSwitchId'
_j='TROPIC-SYSTEM-MIB'
_i='SnmpAdminString'
_h='InterfaceIndexOrZero'
_g='dus'
_f='st3'
_e='sts3e'
_d='st2'
_c='prs'
_b='stu'
_a='dnu'
_Z='sec'
_Y='ssub'
_X='ssua'
_W='prc'
_V='act'
_U='disable'
_T='enable'
_S='wtr'
_R='NokiaSyncStatusMsgType'
_Q='down'
_P='up'
_O='ifIndex'
_N='IF-MIB'
_M='notApplicable'
_L='tnSlotIndex'
_K='TROPIC-SLOT-MIB'
_J='tnShelfIndex'
_I='TROPIC-SHELF-MIB'
_H='Unsigned32'
_G='OctetString'
_F='none'
_E='read-only'
_D='Integer32'
_C='read-create'
_B='TROPIC-SYNCE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_N,_h,_O)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_i)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
tnPortModules,tnSyncEMIB=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnPortModules','tnSyncEMIB')
AluWdmPtpClockIdentifier,=mibBuilder.importSymbols('TROPIC-PTP-MIB','AluWdmPtpClockIdentifier')
tnShelfIndex,=mibBuilder.importSymbols(_I,_J)
tnSlotIndex,=mibBuilder.importSymbols(_K,_L)
tnSysSwitchId,=mibBuilder.importSymbols(_j,_k)
NokiaSyncStatusMsgType,TropicOperationalCapabilityType,TropicStateQualifierType=mibBuilder.importSymbols('TROPIC-TC',_R,'TropicOperationalCapabilityType','TropicStateQualifierType')
tnSyncEMibModule=ModuleIdentity((1,3,6,1,4,1,7483,1,1,2,2,4,6))
if mibBuilder.loadTexts:tnSyncEMibModule.setRevisions(('2020-11-20 12:00','2020-11-13 12:00','2020-11-06 12:00','2020-01-10 12:00','2019-09-06 12:00','2018-09-07 12:00','2018-04-06 12:00','2018-02-23 12:00','2018-02-16 12:00','2018-02-09 12:00','2017-09-29 12:00','2017-07-07 12:00','2017-06-30 12:00','2017-05-26 12:00','2017-04-21 12:00','2016-11-29 12:00','2016-11-16 12:00','2016-10-19 12:00','2016-08-24 12:00','2013-08-26 12:00','2013-07-12 12:00','2013-06-01 12:00','2012-12-20 12:00','2012-09-01 12:00','2012-05-08 12:00','2011-12-21 12:00','2011-08-19 12:00','2011-07-22 12:00','2010-11-30 12:00','2010-11-22 12:00'))
_TnSyncEConf_ObjectIdentity=ObjectIdentity
tnSyncEConf=_TnSyncEConf_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,8,1))
_TnSyncEGroups_ObjectIdentity=ObjectIdentity
tnSyncEGroups=_TnSyncEGroups_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,8,1,1))
_TnSyncECompliances_ObjectIdentity=ObjectIdentity
tnSyncECompliances=_TnSyncECompliances_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,8,1,2))
_TnSyncEObjs_ObjectIdentity=ObjectIdentity
tnSyncEObjs=_TnSyncEObjs_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,8,2))
_TnSyncEBasics_ObjectIdentity=ObjectIdentity
tnSyncEBasics=_TnSyncEBasics_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,8,2,1))
_TnSyncETable_Object=MibTable
tnSyncETable=_TnSyncETable_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,1))
if mibBuilder.loadTexts:tnSyncETable.setStatus(_A)
_TnSyncEEntry_Object=MibTableRow
tnSyncEEntry=_TnSyncEEntry_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,1,1))
tnSyncEEntry.setIndexNames((0,_I,_J),(0,_K,_L))
if mibBuilder.loadTexts:tnSyncEEntry.setStatus(_A)
class _TnSyncESyncMsg_Type(NokiaSyncStatusMsgType):defaultValue=2
_TnSyncESyncMsg_Type.__name__=_R
_TnSyncESyncMsg_Object=MibTableColumn
tnSyncESyncMsg=_TnSyncESyncMsg_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,1,1,1),_TnSyncESyncMsg_Type())
tnSyncESyncMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncESyncMsg.setStatus(_A)
class _TnSyncEActiveRef_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),(_l,2),(_m,3),(_n,4),(_o,5),(_p,6),(_q,7)))
_TnSyncEActiveRef_Type.__name__=_D
_TnSyncEActiveRef_Object=MibTableColumn
tnSyncEActiveRef=_TnSyncEActiveRef_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,1,1,2),_TnSyncEActiveRef_Type())
tnSyncEActiveRef.setMaxAccess(_E)
if mibBuilder.loadTexts:tnSyncEActiveRef.setStatus(_A)
class _TnSyncEWTR_Type(Unsigned32):defaultValue=5
_TnSyncEWTR_Type.__name__=_H
_TnSyncEWTR_Object=MibTableColumn
tnSyncEWTR=_TnSyncEWTR_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,1,1,3),_TnSyncEWTR_Type())
tnSyncEWTR.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncEWTR.setStatus(_A)
_TnSyncESwCmdLineRef_Type=Unsigned32
_TnSyncESwCmdLineRef_Object=MibTableColumn
tnSyncESwCmdLineRef=_TnSyncESwCmdLineRef_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,1,1,4),_TnSyncESwCmdLineRef_Type())
tnSyncESwCmdLineRef.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncESwCmdLineRef.setStatus(_A)
class _TnSyncEClkModState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unknown',1),('locked',2),('autonomousHoldOver',3),('autonomousFreeRunning',4),('forcedFreeRunning',5)))
_TnSyncEClkModState_Type.__name__=_D
_TnSyncEClkModState_Object=MibTableColumn
tnSyncEClkModState=_TnSyncEClkModState_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,1,1,5),_TnSyncEClkModState_Type())
tnSyncEClkModState.setMaxAccess(_E)
if mibBuilder.loadTexts:tnSyncEClkModState.setStatus(_A)
_TnSyncESystemQL_Type=Integer32
_TnSyncESystemQL_Object=MibTableColumn
tnSyncESystemQL=_TnSyncESystemQL_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,1,1,6),_TnSyncESystemQL_Type())
tnSyncESystemQL.setMaxAccess(_E)
if mibBuilder.loadTexts:tnSyncESystemQL.setStatus(_A)
_TnSyncEQLDegradeThreshold_Type=Integer32
_TnSyncEQLDegradeThreshold_Object=MibTableColumn
tnSyncEQLDegradeThreshold=_TnSyncEQLDegradeThreshold_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,1,1,7),_TnSyncEQLDegradeThreshold_Type())
tnSyncEQLDegradeThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncEQLDegradeThreshold.setStatus(_A)
_TnSyncECurrentActiveLineRefFreqOff_Type=Integer32
_TnSyncECurrentActiveLineRefFreqOff_Object=MibTableColumn
tnSyncECurrentActiveLineRefFreqOff=_TnSyncECurrentActiveLineRefFreqOff_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,1,1,8),_TnSyncECurrentActiveLineRefFreqOff_Type())
tnSyncECurrentActiveLineRefFreqOff.setMaxAccess(_E)
if mibBuilder.loadTexts:tnSyncECurrentActiveLineRefFreqOff.setStatus(_A)
if mibBuilder.loadTexts:tnSyncECurrentActiveLineRefFreqOff.setUnits('ppb')
class _TnSyncEAlmProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_TnSyncEAlmProfName_Type.__name__=_G
_TnSyncEAlmProfName_Object=MibTableColumn
tnSyncEAlmProfName=_TnSyncEAlmProfName_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,1,1,9),_TnSyncEAlmProfName_Type())
tnSyncEAlmProfName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncEAlmProfName.setStatus(_A)
_TnSyncELineRefTable_Object=MibTable
tnSyncELineRefTable=_TnSyncELineRefTable_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2))
if mibBuilder.loadTexts:tnSyncELineRefTable.setStatus(_A)
_TnSyncELineRefEntry_Object=MibTableRow
tnSyncELineRefEntry=_TnSyncELineRefEntry_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1))
tnSyncELineRefEntry.setIndexNames((0,_I,_J),(0,_K,_L),(0,_B,_r))
if mibBuilder.loadTexts:tnSyncELineRefEntry.setStatus(_A)
_TnSyncELineRefIndex_Type=Unsigned32
_TnSyncELineRefIndex_Object=MibTableColumn
tnSyncELineRefIndex=_TnSyncELineRefIndex_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,1),_TnSyncELineRefIndex_Type())
tnSyncELineRefIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:tnSyncELineRefIndex.setStatus(_A)
class _TnSyncELineRefAssignedPort_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43)));namedValues=NamedValues(*((_F,1),('l1',2),('l2',3),('c1',4),('c2',5),('c3',6),('c4',7),('c5',8),('c6',9),('c7',10),('c8',11),('c9',12),('c10',13),('c11',14),('c12',15),('c13',16),('c14',17),('c15',18),('c16',19),('c17',20),('c18',21),('c19',22),('c20',23),('c21',24),('c22',25),('c23',26),('c24',27),('x1',28),('x2',29),('x3',30),('x4',31),('x5',32),('x6',33),('m1',34),('m2',35),('m3',36),('m4',37),('x7',38),('x8',39),('x9',40),('x10',41),('x11',42),('x12',43)))
_TnSyncELineRefAssignedPort_Type.__name__=_D
_TnSyncELineRefAssignedPort_Object=MibTableColumn
tnSyncELineRefAssignedPort=_TnSyncELineRefAssignedPort_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,2),_TnSyncELineRefAssignedPort_Type())
tnSyncELineRefAssignedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncELineRefAssignedPort.setStatus(_A)
class _TnSyncELineRefPriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_TnSyncELineRefPriority_Type.__name__=_H
_TnSyncELineRefPriority_Object=MibTableColumn
tnSyncELineRefPriority=_TnSyncELineRefPriority_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,3),_TnSyncELineRefPriority_Type())
tnSyncELineRefPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncELineRefPriority.setStatus(_A)
class _TnSyncELineRefAdminState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_TnSyncELineRefAdminState_Type.__name__=_D
_TnSyncELineRefAdminState_Object=MibTableColumn
tnSyncELineRefAdminState=_TnSyncELineRefAdminState_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,4),_TnSyncELineRefAdminState_Type())
tnSyncELineRefAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncELineRefAdminState.setStatus(_A)
class _TnSyncELineRefOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_TnSyncELineRefOperState_Type.__name__=_D
_TnSyncELineRefOperState_Object=MibTableColumn
tnSyncELineRefOperState=_TnSyncELineRefOperState_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,5),_TnSyncELineRefOperState_Type())
tnSyncELineRefOperState.setMaxAccess(_E)
if mibBuilder.loadTexts:tnSyncELineRefOperState.setStatus(_A)
_TnSyncELineLockOut_Type=TruthValue
_TnSyncELineLockOut_Object=MibTableColumn
tnSyncELineLockOut=_TnSyncELineLockOut_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,6),_TnSyncELineLockOut_Type())
tnSyncELineLockOut.setMaxAccess(_E)
if mibBuilder.loadTexts:tnSyncELineLockOut.setStatus(_A)
class _TnSyncELineRefState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notAssigned',1),('normal',2),('signalFailure',3),(_S,4)))
_TnSyncELineRefState_Type.__name__=_D
_TnSyncELineRefState_Object=MibTableColumn
tnSyncELineRefState=_TnSyncELineRefState_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,7),_TnSyncELineRefState_Type())
tnSyncELineRefState.setMaxAccess(_E)
if mibBuilder.loadTexts:tnSyncELineRefState.setStatus(_A)
class _TnSyncELineRefSwState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('nocmd',1),(_s,2),('mansw',3),(_t,4),(_S,5)))
_TnSyncELineRefSwState_Type.__name__=_D
_TnSyncELineRefSwState_Object=MibTableColumn
tnSyncELineRefSwState=_TnSyncELineRefSwState_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,8),_TnSyncELineRefSwState_Type())
tnSyncELineRefSwState.setMaxAccess(_E)
if mibBuilder.loadTexts:tnSyncELineRefSwState.setStatus(_A)
_TnSyncELineRefIncSSMMsg_Type=Integer32
_TnSyncELineRefIncSSMMsg_Object=MibTableColumn
tnSyncELineRefIncSSMMsg=_TnSyncELineRefIncSSMMsg_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,9),_TnSyncELineRefIncSSMMsg_Type())
tnSyncELineRefIncSSMMsg.setMaxAccess(_E)
if mibBuilder.loadTexts:tnSyncELineRefIncSSMMsg.setStatus(_A)
_TnSyncELineRefIncSSMStatus_Type=Integer32
_TnSyncELineRefIncSSMStatus_Object=MibTableColumn
tnSyncELineRefIncSSMStatus=_TnSyncELineRefIncSSMStatus_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,10),_TnSyncELineRefIncSSMStatus_Type())
tnSyncELineRefIncSSMStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tnSyncELineRefIncSSMStatus.setStatus(_A)
class _TnSyncELineRefIncSSMSupp_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_TnSyncELineRefIncSSMSupp_Type.__name__=_D
_TnSyncELineRefIncSSMSupp_Object=MibTableColumn
tnSyncELineRefIncSSMSupp=_TnSyncELineRefIncSSMSupp_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,11),_TnSyncELineRefIncSSMSupp_Type())
tnSyncELineRefIncSSMSupp.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncELineRefIncSSMSupp.setStatus(_A)
class _TnSyncELineRefProvQL_Type(Integer32):defaultValue=0
_TnSyncELineRefProvQL_Type.__name__=_D
_TnSyncELineRefProvQL_Object=MibTableColumn
tnSyncELineRefProvQL=_TnSyncELineRefProvQL_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,12),_TnSyncELineRefProvQL_Type())
tnSyncELineRefProvQL.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncELineRefProvQL.setStatus(_A)
class _TnSyncELineRefAssociatedPort_Type(InterfaceIndexOrZero):defaultValue=0
_TnSyncELineRefAssociatedPort_Type.__name__=_h
_TnSyncELineRefAssociatedPort_Object=MibTableColumn
tnSyncELineRefAssociatedPort=_TnSyncELineRefAssociatedPort_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,13),_TnSyncELineRefAssociatedPort_Type())
tnSyncELineRefAssociatedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncELineRefAssociatedPort.setStatus(_A)
class _TnSyncELineRefPriorityOfStationClock_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_TnSyncELineRefPriorityOfStationClock_Type.__name__=_H
_TnSyncELineRefPriorityOfStationClock_Object=MibTableColumn
tnSyncELineRefPriorityOfStationClock=_TnSyncELineRefPriorityOfStationClock_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,14),_TnSyncELineRefPriorityOfStationClock_Type())
tnSyncELineRefPriorityOfStationClock.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncELineRefPriorityOfStationClock.setStatus(_A)
_TnSyncELineRefLockOutOfStationClock_Type=TruthValue
_TnSyncELineRefLockOutOfStationClock_Object=MibTableColumn
tnSyncELineRefLockOutOfStationClock=_TnSyncELineRefLockOutOfStationClock_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,15),_TnSyncELineRefLockOutOfStationClock_Type())
tnSyncELineRefLockOutOfStationClock.setMaxAccess(_E)
if mibBuilder.loadTexts:tnSyncELineRefLockOutOfStationClock.setStatus(_A)
class _TnSyncELineRefSwStateOfStationClock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('nocmd',1),(_s,2),('mansw',3),(_t,4),(_S,5)))
_TnSyncELineRefSwStateOfStationClock_Type.__name__=_D
_TnSyncELineRefSwStateOfStationClock_Object=MibTableColumn
tnSyncELineRefSwStateOfStationClock=_TnSyncELineRefSwStateOfStationClock_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,16),_TnSyncELineRefSwStateOfStationClock_Type())
tnSyncELineRefSwStateOfStationClock.setMaxAccess(_E)
if mibBuilder.loadTexts:tnSyncELineRefSwStateOfStationClock.setStatus(_A)
_TnSyncELineRefCurrentFreqOff_Type=Integer32
_TnSyncELineRefCurrentFreqOff_Object=MibTableColumn
tnSyncELineRefCurrentFreqOff=_TnSyncELineRefCurrentFreqOff_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,17),_TnSyncELineRefCurrentFreqOff_Type())
tnSyncELineRefCurrentFreqOff.setMaxAccess(_E)
if mibBuilder.loadTexts:tnSyncELineRefCurrentFreqOff.setStatus(_A)
if mibBuilder.loadTexts:tnSyncELineRefCurrentFreqOff.setUnits('ppb')
class _TnSyncELineRefAlmProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_TnSyncELineRefAlmProfName_Type.__name__=_G
_TnSyncELineRefAlmProfName_Object=MibTableColumn
tnSyncELineRefAlmProfName=_TnSyncELineRefAlmProfName_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,18),_TnSyncELineRefAlmProfName_Type())
tnSyncELineRefAlmProfName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncELineRefAlmProfName.setStatus(_A)
_TnSyncELineRefIncExtdQLTLVClockID_Type=AluWdmPtpClockIdentifier
_TnSyncELineRefIncExtdQLTLVClockID_Object=MibTableColumn
tnSyncELineRefIncExtdQLTLVClockID=_TnSyncELineRefIncExtdQLTLVClockID_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,19),_TnSyncELineRefIncExtdQLTLVClockID_Type())
tnSyncELineRefIncExtdQLTLVClockID.setMaxAccess(_E)
if mibBuilder.loadTexts:tnSyncELineRefIncExtdQLTLVClockID.setStatus(_A)
class _TnSyncELineRefIncExtdQLTLVMixedClockType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eEECFull',1),('eEECMixedEEC',2)))
_TnSyncELineRefIncExtdQLTLVMixedClockType_Type.__name__=_D
_TnSyncELineRefIncExtdQLTLVMixedClockType_Object=MibTableColumn
tnSyncELineRefIncExtdQLTLVMixedClockType=_TnSyncELineRefIncExtdQLTLVMixedClockType_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,20),_TnSyncELineRefIncExtdQLTLVMixedClockType_Type())
tnSyncELineRefIncExtdQLTLVMixedClockType.setMaxAccess(_E)
if mibBuilder.loadTexts:tnSyncELineRefIncExtdQLTLVMixedClockType.setStatus(_A)
class _TnSyncELineRefIncExtdQLTLVPartialChain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('completeChain',1),('partialChain',2)))
_TnSyncELineRefIncExtdQLTLVPartialChain_Type.__name__=_D
_TnSyncELineRefIncExtdQLTLVPartialChain_Object=MibTableColumn
tnSyncELineRefIncExtdQLTLVPartialChain=_TnSyncELineRefIncExtdQLTLVPartialChain_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,21),_TnSyncELineRefIncExtdQLTLVPartialChain_Type())
tnSyncELineRefIncExtdQLTLVPartialChain.setMaxAccess(_E)
if mibBuilder.loadTexts:tnSyncELineRefIncExtdQLTLVPartialChain.setStatus(_A)
_TnSyncELineRefIncExtdQLTLVNumeEEC_Type=Unsigned32
_TnSyncELineRefIncExtdQLTLVNumeEEC_Object=MibTableColumn
tnSyncELineRefIncExtdQLTLVNumeEEC=_TnSyncELineRefIncExtdQLTLVNumeEEC_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,22),_TnSyncELineRefIncExtdQLTLVNumeEEC_Type())
tnSyncELineRefIncExtdQLTLVNumeEEC.setMaxAccess(_E)
if mibBuilder.loadTexts:tnSyncELineRefIncExtdQLTLVNumeEEC.setStatus(_A)
_TnSyncELineRefIncExtdQLTLVNumEEC_Type=Unsigned32
_TnSyncELineRefIncExtdQLTLVNumEEC_Object=MibTableColumn
tnSyncELineRefIncExtdQLTLVNumEEC=_TnSyncELineRefIncExtdQLTLVNumEEC_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,23),_TnSyncELineRefIncExtdQLTLVNumEEC_Type())
tnSyncELineRefIncExtdQLTLVNumEEC.setMaxAccess(_E)
if mibBuilder.loadTexts:tnSyncELineRefIncExtdQLTLVNumEEC.setStatus(_A)
class _TnSyncELineRefProvQLOfStationClock_Type(Integer32):defaultValue=0
_TnSyncELineRefProvQLOfStationClock_Type.__name__=_D
_TnSyncELineRefProvQLOfStationClock_Object=MibTableColumn
tnSyncELineRefProvQLOfStationClock=_TnSyncELineRefProvQLOfStationClock_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,24),_TnSyncELineRefProvQLOfStationClock_Type())
tnSyncELineRefProvQLOfStationClock.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncELineRefProvQLOfStationClock.setStatus(_A)
_TnSyncELineRefIncSSMMsgOfStationClock_Type=Integer32
_TnSyncELineRefIncSSMMsgOfStationClock_Object=MibTableColumn
tnSyncELineRefIncSSMMsgOfStationClock=_TnSyncELineRefIncSSMMsgOfStationClock_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,25),_TnSyncELineRefIncSSMMsgOfStationClock_Type())
tnSyncELineRefIncSSMMsgOfStationClock.setMaxAccess(_E)
if mibBuilder.loadTexts:tnSyncELineRefIncSSMMsgOfStationClock.setStatus(_A)
_TnSyncELineRefIncSSMStatusOfStationClock_Type=Integer32
_TnSyncELineRefIncSSMStatusOfStationClock_Object=MibTableColumn
tnSyncELineRefIncSSMStatusOfStationClock=_TnSyncELineRefIncSSMStatusOfStationClock_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,2,1,26),_TnSyncELineRefIncSSMStatusOfStationClock_Type())
tnSyncELineRefIncSSMStatusOfStationClock.setMaxAccess(_E)
if mibBuilder.loadTexts:tnSyncELineRefIncSSMStatusOfStationClock.setStatus(_A)
_TnSyncEControlTable_Object=MibTable
tnSyncEControlTable=_TnSyncEControlTable_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,3))
if mibBuilder.loadTexts:tnSyncEControlTable.setStatus(_A)
_TnSyncEControlEntry_Object=MibTableRow
tnSyncEControlEntry=_TnSyncEControlEntry_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,3,1))
tnSyncEControlEntry.setIndexNames((0,_I,_J),(0,_K,_L))
if mibBuilder.loadTexts:tnSyncEControlEntry.setStatus(_A)
class _TnSyncEControlEECEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_TnSyncEControlEECEnable_Type.__name__=_D
_TnSyncEControlEECEnable_Object=MibTableColumn
tnSyncEControlEECEnable=_TnSyncEControlEECEnable_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,3,1,1),_TnSyncEControlEECEnable_Type())
tnSyncEControlEECEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncEControlEECEnable.setStatus(_A)
_TnSyncEPortTable_Object=MibTable
tnSyncEPortTable=_TnSyncEPortTable_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,4))
if mibBuilder.loadTexts:tnSyncEPortTable.setStatus(_A)
_TnSyncEPortEntry_Object=MibTableRow
tnSyncEPortEntry=_TnSyncEPortEntry_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,4,1))
tnSyncEPortEntry.setIndexNames((0,_N,_O))
if mibBuilder.loadTexts:tnSyncEPortEntry.setStatus(_A)
class _TnSyncEOprMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sync',1),(_u,2)))
_TnSyncEOprMode_Type.__name__=_D
_TnSyncEOprMode_Object=MibTableColumn
tnSyncEOprMode=_TnSyncEOprMode_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,4,1,1),_TnSyncEOprMode_Type())
tnSyncEOprMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncEOprMode.setStatus(_A)
class _TnSyncEOutgoingForceSsmTrans_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,23,24,25,26)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3),(_Y,4),(_Z,5),(_a,6),(_b,7),(_c,8),(_d,9),(_e,10),(_f,11),(_F,12),(_g,13),('ePRTC',23),('pRTC',24),('ePRC',25),('eSEC',26)))
_TnSyncEOutgoingForceSsmTrans_Type.__name__=_D
_TnSyncEOutgoingForceSsmTrans_Object=MibTableColumn
tnSyncEOutgoingForceSsmTrans=_TnSyncEOutgoingForceSsmTrans_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,4,1,2),_TnSyncEOutgoingForceSsmTrans_Type())
tnSyncEOutgoingForceSsmTrans.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncEOutgoingForceSsmTrans.setStatus(_A)
_TnSyncEStationClockTable_Object=MibTable
tnSyncEStationClockTable=_TnSyncEStationClockTable_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,5))
if mibBuilder.loadTexts:tnSyncEStationClockTable.setStatus(_A)
_TnSyncEStationClockEntry_Object=MibTableRow
tnSyncEStationClockEntry=_TnSyncEStationClockEntry_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,5,1))
tnSyncEStationClockEntry.setIndexNames((0,_I,_J),(0,_K,_L))
if mibBuilder.loadTexts:tnSyncEStationClockEntry.setStatus(_A)
class _TnSyncEStationClockSyncMsg_Type(NokiaSyncStatusMsgType):defaultValue=2
_TnSyncEStationClockSyncMsg_Type.__name__=_R
_TnSyncEStationClockSyncMsg_Object=MibTableColumn
tnSyncEStationClockSyncMsg=_TnSyncEStationClockSyncMsg_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,5,1,1),_TnSyncEStationClockSyncMsg_Type())
tnSyncEStationClockSyncMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncEStationClockSyncMsg.setStatus(_A)
class _TnSyncEStationClockActiveRef_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),(_l,2),(_m,3),(_n,4),(_o,5),(_p,6),(_q,7)))
_TnSyncEStationClockActiveRef_Type.__name__=_D
_TnSyncEStationClockActiveRef_Object=MibTableColumn
tnSyncEStationClockActiveRef=_TnSyncEStationClockActiveRef_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,5,1,2),_TnSyncEStationClockActiveRef_Type())
tnSyncEStationClockActiveRef.setMaxAccess(_E)
if mibBuilder.loadTexts:tnSyncEStationClockActiveRef.setStatus(_A)
class _TnSyncEStationClockWTR_Type(Unsigned32):defaultValue=5
_TnSyncEStationClockWTR_Type.__name__=_H
_TnSyncEStationClockWTR_Object=MibTableColumn
tnSyncEStationClockWTR=_TnSyncEStationClockWTR_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,5,1,3),_TnSyncEStationClockWTR_Type())
tnSyncEStationClockWTR.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncEStationClockWTR.setStatus(_A)
_TnSyncEStationClockSwCmdLineRef_Type=Unsigned32
_TnSyncEStationClockSwCmdLineRef_Object=MibTableColumn
tnSyncEStationClockSwCmdLineRef=_TnSyncEStationClockSwCmdLineRef_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,5,1,4),_TnSyncEStationClockSwCmdLineRef_Type())
tnSyncEStationClockSwCmdLineRef.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncEStationClockSwCmdLineRef.setStatus(_A)
_TnSyncEStationClockSystemQL_Type=Integer32
_TnSyncEStationClockSystemQL_Object=MibTableColumn
tnSyncEStationClockSystemQL=_TnSyncEStationClockSystemQL_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,5,1,5),_TnSyncEStationClockSystemQL_Type())
tnSyncEStationClockSystemQL.setMaxAccess(_E)
if mibBuilder.loadTexts:tnSyncEStationClockSystemQL.setStatus(_A)
class _TnSyncEStationClockQLThreshold_Type(Integer32):defaultValue=4
_TnSyncEStationClockQLThreshold_Type.__name__=_D
_TnSyncEStationClockQLThreshold_Object=MibTableColumn
tnSyncEStationClockQLThreshold=_TnSyncEStationClockQLThreshold_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,5,1,6),_TnSyncEStationClockQLThreshold_Type())
tnSyncEStationClockQLThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncEStationClockQLThreshold.setStatus(_A)
class _TnSyncEStationClockOutSel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('outtim',1),('setg',2)))
_TnSyncEStationClockOutSel_Type.__name__=_D
_TnSyncEStationClockOutSel_Object=MibTableColumn
tnSyncEStationClockOutSel=_TnSyncEStationClockOutSel_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,5,1,7),_TnSyncEStationClockOutSel_Type())
tnSyncEStationClockOutSel.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncEStationClockOutSel.setStatus(_A)
class _TnSyncEStationClockAlmProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_TnSyncEStationClockAlmProfName_Type.__name__=_G
_TnSyncEStationClockAlmProfName_Object=MibTableColumn
tnSyncEStationClockAlmProfName=_TnSyncEStationClockAlmProfName_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,5,1,8),_TnSyncEStationClockAlmProfName_Type())
tnSyncEStationClockAlmProfName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncEStationClockAlmProfName.setStatus(_A)
_TnSyncEBITSPortTable_Object=MibTable
tnSyncEBITSPortTable=_TnSyncEBITSPortTable_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,6))
if mibBuilder.loadTexts:tnSyncEBITSPortTable.setStatus(_A)
_TnSyncEBITSPortEntry_Object=MibTableRow
tnSyncEBITSPortEntry=_TnSyncEBITSPortEntry_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,6,1))
tnSyncEBITSPortEntry.setIndexNames((0,_N,_O))
if mibBuilder.loadTexts:tnSyncEBITSPortEntry.setStatus(_A)
class _TnSyncEBITSPortDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('input',1),('output',2)))
_TnSyncEBITSPortDirection_Type.__name__=_D
_TnSyncEBITSPortDirection_Object=MibTableColumn
tnSyncEBITSPortDirection=_TnSyncEBITSPortDirection_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,6,1,1),_TnSyncEBITSPortDirection_Type())
tnSyncEBITSPortDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncEBITSPortDirection.setStatus(_A)
class _TnSyncEBITSPortSignalType_Type(Integer32):defaultValue=0
_TnSyncEBITSPortSignalType_Type.__name__=_D
_TnSyncEBITSPortSignalType_Object=MibTableColumn
tnSyncEBITSPortSignalType=_TnSyncEBITSPortSignalType_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,6,1,2),_TnSyncEBITSPortSignalType_Type())
tnSyncEBITSPortSignalType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncEBITSPortSignalType.setStatus(_A)
class _TnSyncEBITSPortSaBit_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_M,0),('sa4',1),('sa5',2),('sa6',3),('sa7',4),('sa8',5)))
_TnSyncEBITSPortSaBit_Type.__name__=_D
_TnSyncEBITSPortSaBit_Object=MibTableColumn
tnSyncEBITSPortSaBit=_TnSyncEBITSPortSaBit_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,6,1,3),_TnSyncEBITSPortSaBit_Type())
tnSyncEBITSPortSaBit.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncEBITSPortSaBit.setStatus(_A)
class _TnSyncEBITSPortOutputSSMTrans_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_M,0),(_V,1),(_W,2),(_X,3),(_Y,4),(_Z,5),(_a,6),(_b,7),(_c,8),(_d,9),(_e,10),(_f,11),(_F,12),(_g,13)))
_TnSyncEBITSPortOutputSSMTrans_Type.__name__=_D
_TnSyncEBITSPortOutputSSMTrans_Object=MibTableColumn
tnSyncEBITSPortOutputSSMTrans=_TnSyncEBITSPortOutputSSMTrans_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,6,1,4),_TnSyncEBITSPortOutputSSMTrans_Type())
tnSyncEBITSPortOutputSSMTrans.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncEBITSPortOutputSSMTrans.setStatus(_A)
class _TnSyncEBITSPortOutputAISMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),('aismode',1),('qlmode',2)))
_TnSyncEBITSPortOutputAISMode_Type.__name__=_D
_TnSyncEBITSPortOutputAISMode_Object=MibTableColumn
tnSyncEBITSPortOutputAISMode=_TnSyncEBITSPortOutputAISMode_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,6,1,5),_TnSyncEBITSPortOutputAISMode_Type())
tnSyncEBITSPortOutputAISMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncEBITSPortOutputAISMode.setStatus(_A)
class _TnSyncEBITSPortLineImpedance_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('imp75ohms',1),('imp120ohms',2),('imp100ohms',3)))
_TnSyncEBITSPortLineImpedance_Type.__name__=_D
_TnSyncEBITSPortLineImpedance_Object=MibTableColumn
tnSyncEBITSPortLineImpedance=_TnSyncEBITSPortLineImpedance_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,6,1,6),_TnSyncEBITSPortLineImpedance_Type())
tnSyncEBITSPortLineImpedance.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncEBITSPortLineImpedance.setStatus(_A)
class _TnSyncEBITSPortLineCode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('b8zs',1),('ami',2),(_M,3)))
_TnSyncEBITSPortLineCode_Type.__name__=_D
_TnSyncEBITSPortLineCode_Object=MibTableColumn
tnSyncEBITSPortLineCode=_TnSyncEBITSPortLineCode_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,6,1,7),_TnSyncEBITSPortLineCode_Type())
tnSyncEBITSPortLineCode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncEBITSPortLineCode.setStatus(_A)
class _TnSyncEBITSPortLbo_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('lbo',1),('lbo1',2),('lbo2',3),('lbo3',4),('lbo4',5),('lbo5',6)))
_TnSyncEBITSPortLbo_Type.__name__=_D
_TnSyncEBITSPortLbo_Object=MibTableColumn
tnSyncEBITSPortLbo=_TnSyncEBITSPortLbo_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,6,1,8),_TnSyncEBITSPortLbo_Type())
tnSyncEBITSPortLbo.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncEBITSPortLbo.setStatus(_A)
class _TnSyncEBITSPortAlmProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_TnSyncEBITSPortAlmProfName_Type.__name__=_G
_TnSyncEBITSPortAlmProfName_Object=MibTableColumn
tnSyncEBITSPortAlmProfName=_TnSyncEBITSPortAlmProfName_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,6,1,9),_TnSyncEBITSPortAlmProfName_Type())
tnSyncEBITSPortAlmProfName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncEBITSPortAlmProfName.setStatus(_A)
_TnWanTable_Object=MibTable
tnWanTable=_TnWanTable_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,7))
if mibBuilder.loadTexts:tnWanTable.setStatus(_A)
_TnWanEntry_Object=MibTableRow
tnWanEntry=_TnWanEntry_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,7,1))
tnWanEntry.setIndexNames((0,_N,_O))
if mibBuilder.loadTexts:tnWanEntry.setStatus(_A)
_TnWanAlmProfName_Type=OctetString
_TnWanAlmProfName_Object=MibTableColumn
tnWanAlmProfName=_TnWanAlmProfName_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,7,1,1),_TnWanAlmProfName_Type())
tnWanAlmProfName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnWanAlmProfName.setStatus(_A)
class _TnWanSyncEOprMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sync',1),(_u,2)))
_TnWanSyncEOprMode_Type.__name__=_D
_TnWanSyncEOprMode_Object=MibTableColumn
tnWanSyncEOprMode=_TnWanSyncEOprMode_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,7,1,2),_TnWanSyncEOprMode_Type())
tnWanSyncEOprMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnWanSyncEOprMode.setStatus(_A)
class _TnWanSyncEOutgoingForceSsmTrans_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,23,24,25,26)));namedValues=NamedValues(*((_M,1),(_V,2),(_W,3),(_X,4),(_Y,5),(_Z,6),(_a,7),(_b,8),(_c,9),(_d,10),(_e,11),(_f,12),(_F,13),(_g,14),('ePRTC',23),('pRTC',24),('ePRC',25),('eSEC',26)))
_TnWanSyncEOutgoingForceSsmTrans_Type.__name__=_D
_TnWanSyncEOutgoingForceSsmTrans_Object=MibTableColumn
tnWanSyncEOutgoingForceSsmTrans=_TnWanSyncEOutgoingForceSsmTrans_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,7,1,3),_TnWanSyncEOutgoingForceSsmTrans_Type())
tnWanSyncEOutgoingForceSsmTrans.setMaxAccess(_C)
if mibBuilder.loadTexts:tnWanSyncEOutgoingForceSsmTrans.setStatus(_A)
class _TnWanAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_TnWanAdminStatus_Type.__name__=_D
_TnWanAdminStatus_Object=MibTableColumn
tnWanAdminStatus=_TnWanAdminStatus_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,7,1,4),_TnWanAdminStatus_Type())
tnWanAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnWanAdminStatus.setStatus(_A)
class _TnWanOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_TnWanOperStatus_Type.__name__=_D
_TnWanOperStatus_Object=MibTableColumn
tnWanOperStatus=_TnWanOperStatus_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,7,1,5),_TnWanOperStatus_Type())
tnWanOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tnWanOperStatus.setStatus(_A)
_TnWanStateQualifier_Type=TropicStateQualifierType
_TnWanStateQualifier_Object=MibTableColumn
tnWanStateQualifier=_TnWanStateQualifier_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,7,1,6),_TnWanStateQualifier_Type())
tnWanStateQualifier.setMaxAccess(_E)
if mibBuilder.loadTexts:tnWanStateQualifier.setStatus(_A)
_TnWanOperationalCapability_Type=TropicOperationalCapabilityType
_TnWanOperationalCapability_Object=MibTableColumn
tnWanOperationalCapability=_TnWanOperationalCapability_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,7,1,7),_TnWanOperationalCapability_Type())
tnWanOperationalCapability.setMaxAccess(_E)
if mibBuilder.loadTexts:tnWanOperationalCapability.setStatus(_A)
class _TnWanDescription_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TnWanDescription_Type.__name__=_i
_TnWanDescription_Object=MibTableColumn
tnWanDescription=_TnWanDescription_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,7,1,8),_TnWanDescription_Type())
tnWanDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tnWanDescription.setStatus(_A)
_TnSyncEPacketswitchControlTable_Object=MibTable
tnSyncEPacketswitchControlTable=_TnSyncEPacketswitchControlTable_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,8))
if mibBuilder.loadTexts:tnSyncEPacketswitchControlTable.setStatus(_A)
_TnSyncEPacketswitchControlEntry_Object=MibTableRow
tnSyncEPacketswitchControlEntry=_TnSyncEPacketswitchControlEntry_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,8,1))
tnSyncEPacketswitchControlEntry.setIndexNames((0,_j,_k))
if mibBuilder.loadTexts:tnSyncEPacketswitchControlEntry.setStatus(_A)
class _TnSyncEPacketswitchControlEECEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_TnSyncEPacketswitchControlEECEnable_Type.__name__=_D
_TnSyncEPacketswitchControlEECEnable_Object=MibTableColumn
tnSyncEPacketswitchControlEECEnable=_TnSyncEPacketswitchControlEECEnable_Object((1,3,6,1,4,1,7483,2,2,4,8,2,1,8,1,1),_TnSyncEPacketswitchControlEECEnable_Type())
tnSyncEPacketswitchControlEECEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSyncEPacketswitchControlEECEnable.setStatus(_A)
tnSyncEGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,8,1,1,1))
tnSyncEGroup.setObjects(*((_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:tnSyncEGroup.setStatus(_A)
tnSyncELineRefGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,8,1,1,2))
tnSyncELineRefGroup.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS)))
if mibBuilder.loadTexts:tnSyncELineRefGroup.setStatus(_A)
tnSyncEControlGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,8,1,1,3))
tnSyncEControlGroup.setObjects((_B,_AT))
if mibBuilder.loadTexts:tnSyncEControlGroup.setStatus(_A)
tnSyncEPortGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,8,1,1,4))
tnSyncEPortGroup.setObjects(*((_B,_AU),(_B,_AV)))
if mibBuilder.loadTexts:tnSyncEPortGroup.setStatus(_A)
tnSyncEStationClockGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,8,1,1,5))
tnSyncEStationClockGroup.setObjects(*((_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad)))
if mibBuilder.loadTexts:tnSyncEStationClockGroup.setStatus(_A)
tnSyncEBITSPortGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,8,1,1,6))
tnSyncEBITSPortGroup.setObjects(*((_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am)))
if mibBuilder.loadTexts:tnSyncEBITSPortGroup.setStatus(_A)
tnWanGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,8,1,1,7))
tnWanGroup.setObjects(*((_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au)))
if mibBuilder.loadTexts:tnWanGroup.setStatus(_A)
tnSyncEPacketswitchControlGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,8,1,1,8))
tnSyncEPacketswitchControlGroup.setObjects((_B,_Av))
if mibBuilder.loadTexts:tnSyncEPacketswitchControlGroup.setStatus(_A)
tnSyncECompliance=ModuleCompliance((1,3,6,1,4,1,7483,2,2,4,8,1,2,1))
tnSyncECompliance.setObjects(*((_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1),(_B,_B2)))
if mibBuilder.loadTexts:tnSyncECompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'tnSyncEMibModule':tnSyncEMibModule,'tnSyncEConf':tnSyncEConf,'tnSyncEGroups':tnSyncEGroups,_Aw:tnSyncEGroup,_Ax:tnSyncELineRefGroup,_Ay:tnSyncEControlGroup,_Az:tnSyncEPortGroup,_A_:tnSyncEStationClockGroup,_B0:tnSyncEBITSPortGroup,_B1:tnWanGroup,_B2:tnSyncEPacketswitchControlGroup,'tnSyncECompliances':tnSyncECompliances,'tnSyncECompliance':tnSyncECompliance,'tnSyncEObjs':tnSyncEObjs,'tnSyncEBasics':tnSyncEBasics,'tnSyncETable':tnSyncETable,'tnSyncEEntry':tnSyncEEntry,_v:tnSyncESyncMsg,_w:tnSyncEActiveRef,_x:tnSyncEWTR,_y:tnSyncESwCmdLineRef,_z:tnSyncEClkModState,_A0:tnSyncESystemQL,_A1:tnSyncEQLDegradeThreshold,_A2:tnSyncECurrentActiveLineRefFreqOff,_A3:tnSyncEAlmProfName,'tnSyncELineRefTable':tnSyncELineRefTable,'tnSyncELineRefEntry':tnSyncELineRefEntry,_r:tnSyncELineRefIndex,_A4:tnSyncELineRefAssignedPort,_A5:tnSyncELineRefPriority,_A6:tnSyncELineRefAdminState,_A7:tnSyncELineRefOperState,_A8:tnSyncELineLockOut,_A9:tnSyncELineRefState,_AA:tnSyncELineRefSwState,_AB:tnSyncELineRefIncSSMMsg,_AC:tnSyncELineRefIncSSMStatus,_AD:tnSyncELineRefIncSSMSupp,_AE:tnSyncELineRefProvQL,_AF:tnSyncELineRefAssociatedPort,_AG:tnSyncELineRefPriorityOfStationClock,_AH:tnSyncELineRefLockOutOfStationClock,_AI:tnSyncELineRefSwStateOfStationClock,_AJ:tnSyncELineRefCurrentFreqOff,_AK:tnSyncELineRefAlmProfName,_AL:tnSyncELineRefIncExtdQLTLVClockID,_AM:tnSyncELineRefIncExtdQLTLVMixedClockType,_AN:tnSyncELineRefIncExtdQLTLVPartialChain,_AO:tnSyncELineRefIncExtdQLTLVNumeEEC,_AP:tnSyncELineRefIncExtdQLTLVNumEEC,_AQ:tnSyncELineRefProvQLOfStationClock,_AR:tnSyncELineRefIncSSMMsgOfStationClock,_AS:tnSyncELineRefIncSSMStatusOfStationClock,'tnSyncEControlTable':tnSyncEControlTable,'tnSyncEControlEntry':tnSyncEControlEntry,_AT:tnSyncEControlEECEnable,'tnSyncEPortTable':tnSyncEPortTable,'tnSyncEPortEntry':tnSyncEPortEntry,_AU:tnSyncEOprMode,_AV:tnSyncEOutgoingForceSsmTrans,'tnSyncEStationClockTable':tnSyncEStationClockTable,'tnSyncEStationClockEntry':tnSyncEStationClockEntry,_AW:tnSyncEStationClockSyncMsg,_AX:tnSyncEStationClockActiveRef,_AY:tnSyncEStationClockWTR,_AZ:tnSyncEStationClockSwCmdLineRef,_Aa:tnSyncEStationClockSystemQL,_Ab:tnSyncEStationClockQLThreshold,_Ac:tnSyncEStationClockOutSel,_Ad:tnSyncEStationClockAlmProfName,'tnSyncEBITSPortTable':tnSyncEBITSPortTable,'tnSyncEBITSPortEntry':tnSyncEBITSPortEntry,_Ae:tnSyncEBITSPortDirection,_Af:tnSyncEBITSPortSignalType,_Ag:tnSyncEBITSPortSaBit,_Ah:tnSyncEBITSPortOutputSSMTrans,_Ai:tnSyncEBITSPortOutputAISMode,_Aj:tnSyncEBITSPortLineImpedance,_Ak:tnSyncEBITSPortLineCode,_Al:tnSyncEBITSPortLbo,_Am:tnSyncEBITSPortAlmProfName,'tnWanTable':tnWanTable,'tnWanEntry':tnWanEntry,_An:tnWanAlmProfName,_Ao:tnWanSyncEOprMode,_Ap:tnWanSyncEOutgoingForceSsmTrans,_Aq:tnWanAdminStatus,_Ar:tnWanOperStatus,_As:tnWanStateQualifier,_At:tnWanOperationalCapability,_Au:tnWanDescription,'tnSyncEPacketswitchControlTable':tnSyncEPacketswitchControlTable,'tnSyncEPacketswitchControlEntry':tnSyncEPacketswitchControlEntry,_Av:tnSyncEPacketswitchControlEECEnable})