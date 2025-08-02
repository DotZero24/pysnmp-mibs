_A6='alaMvrpNotifyGroup'
_A5='alaMvrpPortRestrictVlanConfigGroup'
_A4='alaMvrpPortStatsGroup'
_A3='alaMvrpPortConfigGroup'
_A2='alaMvrpBaseGroup'
_A1='alaMvrpVlanLimitReachedEvent'
_A0='alaMvrpE2eVlanConflict'
_z='alaMvrpPortVlanRestrictions'
_y='alaMvrpPortStatsClearStats'
_x='alaMvrpPortLastPduOrigin'
_w='alaMvrpPortFailedRegistrations'
_v='alaMvrpPortStatsInvalidMsgsReceived'
_u='alaMvrpPortStatsTotalMsgsTransmitted'
_t='alaMvrpPortStatsTotalMsgsReceived'
_s='alaMvrpPortStatsTotalPDUTransmitted'
_r='alaMvrpPortStatsTotalPDUReceived'
_q='alaMvrpPortStatsLeaveAllTransmitted'
_p='alaMvrpPortStatsEmptyTransmitted'
_o='alaMvrpPortStatsInTransmitted'
_n='alaMvrpPortStatsLeaveTransmitted'
_m='alaMvrpPortStatsJoinEmptyTransmitted'
_l='alaMvrpPortStatsJoinInTransmitted'
_k='alaMvrpPortStatsNewTransmitted'
_j='alaMvrpPortStatsLeaveAllReceived'
_i='alaMvrpPortStatsEmptyReceived'
_h='alaMvrpPortStatsInReceived'
_g='alaMvrpPortStatsLeaveReceived'
_f='alaMvrpPortStatsJoinEmptyReceived'
_e='alaMvrpPortStatsJoinInReceived'
_d='alaMvrpPortStatsNewReceived'
_c='alaMvrpPortConfigPeriodicTransmissionStatus'
_b='alaMvrpPortConfigPeriodicTimer'
_a='alaMvrpPortConfigLeaveAllTimer'
_Z='alaMvrpPortConfigLeaveTimer'
_Y='alaMvrpPortConfigJoinTimer'
_X='alaMvrpPortConfigApplicantMode'
_W='alaMvrpPortConfigRegistrarMode'
_V='alaMvrpPortStatus'
_U='alaVlanRegistrationProtocolType'
_T='alaMvrpTransparentSwitching'
_S='alaMvrpGlobalClearStats'
_R='alaMvrpGlobalStatus'
_Q='MvrpPortVlanRestrictBitmap'
_P='alaMvrpPortRestrictVlanID'
_O='alaMvrpPortRestrictVlanIfIndex'
_N='alaMvrpPortStatsIfIndex'
_M='alaMvrpPortConfigIfIndex'
_L='default'
_K='OctetString'
_J='alaMvrpVlanConflictInfo'
_I='alaMvrpMaxVlanLimit'
_H='milliseconds'
_G='not-accessible'
_F='EnabledStatus'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='ALCATEL-IND1-MVRP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1Mvrp,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1Mvrp')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_F)
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
alcatelIND1MVRPMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,57,1))
if mibBuilder.loadTexts:alcatelIND1MVRPMIB.setRevisions(('2009-08-07 00:00',))
class MvrpPortVlanRestrictBitmap(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('noRestriction',0),('restrictRegistration',1),('restrictAdvertisement',2),('restrictStaticVlanRegistration',3)))
_AlaMvrpEvents_ObjectIdentity=ObjectIdentity
alaMvrpEvents=_AlaMvrpEvents_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,57,1,0))
_AlcatelIND1MVRPMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1MVRPMIBObjects=_AlcatelIND1MVRPMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,57,1,1))
if mibBuilder.loadTexts:alcatelIND1MVRPMIBObjects.setStatus(_A)
class _AlaMvrpGlobalStatus_Type(EnabledStatus):defaultValue=2
_AlaMvrpGlobalStatus_Type.__name__=_F
_AlaMvrpGlobalStatus_Object=MibScalar
alaMvrpGlobalStatus=_AlaMvrpGlobalStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,1),_AlaMvrpGlobalStatus_Type())
alaMvrpGlobalStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMvrpGlobalStatus.setStatus(_A)
class _AlaMvrpGlobalClearStats_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),('reset',1)))
_AlaMvrpGlobalClearStats_Type.__name__=_E
_AlaMvrpGlobalClearStats_Object=MibScalar
alaMvrpGlobalClearStats=_AlaMvrpGlobalClearStats_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,2),_AlaMvrpGlobalClearStats_Type())
alaMvrpGlobalClearStats.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMvrpGlobalClearStats.setStatus(_A)
class _AlaMvrpTransparentSwitching_Type(EnabledStatus):defaultValue=2
_AlaMvrpTransparentSwitching_Type.__name__=_F
_AlaMvrpTransparentSwitching_Object=MibScalar
alaMvrpTransparentSwitching=_AlaMvrpTransparentSwitching_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,3),_AlaMvrpTransparentSwitching_Type())
alaMvrpTransparentSwitching.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMvrpTransparentSwitching.setStatus(_A)
class _AlaMvrpMaxVlanLimit_Type(Integer32):defaultValue=256;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,4094))
_AlaMvrpMaxVlanLimit_Type.__name__=_E
_AlaMvrpMaxVlanLimit_Object=MibScalar
alaMvrpMaxVlanLimit=_AlaMvrpMaxVlanLimit_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,4),_AlaMvrpMaxVlanLimit_Type())
alaMvrpMaxVlanLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMvrpMaxVlanLimit.setStatus(_A)
class _AlaMvrpVlanConflictInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_AlaMvrpVlanConflictInfo_Type.__name__=_K
_AlaMvrpVlanConflictInfo_Object=MibScalar
alaMvrpVlanConflictInfo=_AlaMvrpVlanConflictInfo_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,5),_AlaMvrpVlanConflictInfo_Type())
alaMvrpVlanConflictInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMvrpVlanConflictInfo.setStatus(_A)
class _AlaVlanRegistrationProtocolType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('gvrp',0),('mvrp',1)))
_AlaVlanRegistrationProtocolType_Type.__name__=_E
_AlaVlanRegistrationProtocolType_Object=MibScalar
alaVlanRegistrationProtocolType=_AlaVlanRegistrationProtocolType_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,6),_AlaVlanRegistrationProtocolType_Type())
alaVlanRegistrationProtocolType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaVlanRegistrationProtocolType.setStatus(_A)
_AlaMvrpPortConfig_ObjectIdentity=ObjectIdentity
alaMvrpPortConfig=_AlaMvrpPortConfig_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,7))
_AlaMvrpPortConfigTable_Object=MibTable
alaMvrpPortConfigTable=_AlaMvrpPortConfigTable_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,7,1))
if mibBuilder.loadTexts:alaMvrpPortConfigTable.setStatus(_A)
_AlaMvrpPortConfigEntry_Object=MibTableRow
alaMvrpPortConfigEntry=_AlaMvrpPortConfigEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,7,1,1))
alaMvrpPortConfigEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:alaMvrpPortConfigEntry.setStatus(_A)
_AlaMvrpPortConfigIfIndex_Type=InterfaceIndex
_AlaMvrpPortConfigIfIndex_Object=MibTableColumn
alaMvrpPortConfigIfIndex=_AlaMvrpPortConfigIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,7,1,1,1),_AlaMvrpPortConfigIfIndex_Type())
alaMvrpPortConfigIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:alaMvrpPortConfigIfIndex.setStatus(_A)
class _AlaMvrpPortStatus_Type(EnabledStatus):defaultValue=2
_AlaMvrpPortStatus_Type.__name__=_F
_AlaMvrpPortStatus_Object=MibTableColumn
alaMvrpPortStatus=_AlaMvrpPortStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,7,1,1,2),_AlaMvrpPortStatus_Type())
alaMvrpPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMvrpPortStatus.setStatus(_A)
class _AlaMvrpPortConfigRegistrarMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('fixed',2),('forbidden',3)))
_AlaMvrpPortConfigRegistrarMode_Type.__name__=_E
_AlaMvrpPortConfigRegistrarMode_Object=MibTableColumn
alaMvrpPortConfigRegistrarMode=_AlaMvrpPortConfigRegistrarMode_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,7,1,1,3),_AlaMvrpPortConfigRegistrarMode_Type())
alaMvrpPortConfigRegistrarMode.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMvrpPortConfigRegistrarMode.setStatus(_A)
class _AlaMvrpPortConfigApplicantMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('participant',1),('nonparticipant',2),('active',3)))
_AlaMvrpPortConfigApplicantMode_Type.__name__=_E
_AlaMvrpPortConfigApplicantMode_Object=MibTableColumn
alaMvrpPortConfigApplicantMode=_AlaMvrpPortConfigApplicantMode_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,7,1,1,4),_AlaMvrpPortConfigApplicantMode_Type())
alaMvrpPortConfigApplicantMode.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMvrpPortConfigApplicantMode.setStatus(_A)
class _AlaMvrpPortConfigJoinTimer_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(250,1073741773))
_AlaMvrpPortConfigJoinTimer_Type.__name__=_E
_AlaMvrpPortConfigJoinTimer_Object=MibTableColumn
alaMvrpPortConfigJoinTimer=_AlaMvrpPortConfigJoinTimer_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,7,1,1,5),_AlaMvrpPortConfigJoinTimer_Type())
alaMvrpPortConfigJoinTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMvrpPortConfigJoinTimer.setStatus(_A)
if mibBuilder.loadTexts:alaMvrpPortConfigJoinTimer.setUnits(_H)
class _AlaMvrpPortConfigLeaveTimer_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(750,2147483647))
_AlaMvrpPortConfigLeaveTimer_Type.__name__=_E
_AlaMvrpPortConfigLeaveTimer_Object=MibTableColumn
alaMvrpPortConfigLeaveTimer=_AlaMvrpPortConfigLeaveTimer_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,7,1,1,6),_AlaMvrpPortConfigLeaveTimer_Type())
alaMvrpPortConfigLeaveTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMvrpPortConfigLeaveTimer.setStatus(_A)
if mibBuilder.loadTexts:alaMvrpPortConfigLeaveTimer.setUnits(_H)
class _AlaMvrpPortConfigLeaveAllTimer_Type(Integer32):defaultValue=30000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(750,2147483647))
_AlaMvrpPortConfigLeaveAllTimer_Type.__name__=_E
_AlaMvrpPortConfigLeaveAllTimer_Object=MibTableColumn
alaMvrpPortConfigLeaveAllTimer=_AlaMvrpPortConfigLeaveAllTimer_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,7,1,1,7),_AlaMvrpPortConfigLeaveAllTimer_Type())
alaMvrpPortConfigLeaveAllTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMvrpPortConfigLeaveAllTimer.setStatus(_A)
if mibBuilder.loadTexts:alaMvrpPortConfigLeaveAllTimer.setUnits(_H)
class _AlaMvrpPortConfigPeriodicTimer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AlaMvrpPortConfigPeriodicTimer_Type.__name__=_E
_AlaMvrpPortConfigPeriodicTimer_Object=MibTableColumn
alaMvrpPortConfigPeriodicTimer=_AlaMvrpPortConfigPeriodicTimer_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,7,1,1,8),_AlaMvrpPortConfigPeriodicTimer_Type())
alaMvrpPortConfigPeriodicTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMvrpPortConfigPeriodicTimer.setStatus(_A)
if mibBuilder.loadTexts:alaMvrpPortConfigPeriodicTimer.setUnits('seconds')
class _AlaMvrpPortConfigPeriodicTransmissionStatus_Type(EnabledStatus):defaultValue=1
_AlaMvrpPortConfigPeriodicTransmissionStatus_Type.__name__=_F
_AlaMvrpPortConfigPeriodicTransmissionStatus_Object=MibTableColumn
alaMvrpPortConfigPeriodicTransmissionStatus=_AlaMvrpPortConfigPeriodicTransmissionStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,7,1,1,9),_AlaMvrpPortConfigPeriodicTransmissionStatus_Type())
alaMvrpPortConfigPeriodicTransmissionStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMvrpPortConfigPeriodicTransmissionStatus.setStatus(_A)
_AlaMvrpPortStats_ObjectIdentity=ObjectIdentity
alaMvrpPortStats=_AlaMvrpPortStats_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8))
_AlaMvrpPortStatsTable_Object=MibTable
alaMvrpPortStatsTable=_AlaMvrpPortStatsTable_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1))
if mibBuilder.loadTexts:alaMvrpPortStatsTable.setStatus(_A)
_AlaMvrpPortStatsEntry_Object=MibTableRow
alaMvrpPortStatsEntry=_AlaMvrpPortStatsEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1,1))
alaMvrpPortStatsEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:alaMvrpPortStatsEntry.setStatus(_A)
_AlaMvrpPortStatsIfIndex_Type=InterfaceIndex
_AlaMvrpPortStatsIfIndex_Object=MibTableColumn
alaMvrpPortStatsIfIndex=_AlaMvrpPortStatsIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1,1,1),_AlaMvrpPortStatsIfIndex_Type())
alaMvrpPortStatsIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:alaMvrpPortStatsIfIndex.setStatus(_A)
_AlaMvrpPortStatsNewReceived_Type=Counter32
_AlaMvrpPortStatsNewReceived_Object=MibTableColumn
alaMvrpPortStatsNewReceived=_AlaMvrpPortStatsNewReceived_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1,1,2),_AlaMvrpPortStatsNewReceived_Type())
alaMvrpPortStatsNewReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMvrpPortStatsNewReceived.setStatus(_A)
_AlaMvrpPortStatsJoinInReceived_Type=Counter32
_AlaMvrpPortStatsJoinInReceived_Object=MibTableColumn
alaMvrpPortStatsJoinInReceived=_AlaMvrpPortStatsJoinInReceived_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1,1,3),_AlaMvrpPortStatsJoinInReceived_Type())
alaMvrpPortStatsJoinInReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMvrpPortStatsJoinInReceived.setStatus(_A)
_AlaMvrpPortStatsJoinEmptyReceived_Type=Counter32
_AlaMvrpPortStatsJoinEmptyReceived_Object=MibTableColumn
alaMvrpPortStatsJoinEmptyReceived=_AlaMvrpPortStatsJoinEmptyReceived_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1,1,4),_AlaMvrpPortStatsJoinEmptyReceived_Type())
alaMvrpPortStatsJoinEmptyReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMvrpPortStatsJoinEmptyReceived.setStatus(_A)
_AlaMvrpPortStatsLeaveReceived_Type=Counter32
_AlaMvrpPortStatsLeaveReceived_Object=MibTableColumn
alaMvrpPortStatsLeaveReceived=_AlaMvrpPortStatsLeaveReceived_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1,1,5),_AlaMvrpPortStatsLeaveReceived_Type())
alaMvrpPortStatsLeaveReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMvrpPortStatsLeaveReceived.setStatus(_A)
_AlaMvrpPortStatsInReceived_Type=Counter32
_AlaMvrpPortStatsInReceived_Object=MibTableColumn
alaMvrpPortStatsInReceived=_AlaMvrpPortStatsInReceived_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1,1,6),_AlaMvrpPortStatsInReceived_Type())
alaMvrpPortStatsInReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMvrpPortStatsInReceived.setStatus(_A)
_AlaMvrpPortStatsEmptyReceived_Type=Counter32
_AlaMvrpPortStatsEmptyReceived_Object=MibTableColumn
alaMvrpPortStatsEmptyReceived=_AlaMvrpPortStatsEmptyReceived_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1,1,7),_AlaMvrpPortStatsEmptyReceived_Type())
alaMvrpPortStatsEmptyReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMvrpPortStatsEmptyReceived.setStatus(_A)
_AlaMvrpPortStatsLeaveAllReceived_Type=Counter32
_AlaMvrpPortStatsLeaveAllReceived_Object=MibTableColumn
alaMvrpPortStatsLeaveAllReceived=_AlaMvrpPortStatsLeaveAllReceived_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1,1,8),_AlaMvrpPortStatsLeaveAllReceived_Type())
alaMvrpPortStatsLeaveAllReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMvrpPortStatsLeaveAllReceived.setStatus(_A)
_AlaMvrpPortStatsNewTransmitted_Type=Counter32
_AlaMvrpPortStatsNewTransmitted_Object=MibTableColumn
alaMvrpPortStatsNewTransmitted=_AlaMvrpPortStatsNewTransmitted_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1,1,9),_AlaMvrpPortStatsNewTransmitted_Type())
alaMvrpPortStatsNewTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMvrpPortStatsNewTransmitted.setStatus(_A)
_AlaMvrpPortStatsJoinInTransmitted_Type=Counter32
_AlaMvrpPortStatsJoinInTransmitted_Object=MibTableColumn
alaMvrpPortStatsJoinInTransmitted=_AlaMvrpPortStatsJoinInTransmitted_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1,1,10),_AlaMvrpPortStatsJoinInTransmitted_Type())
alaMvrpPortStatsJoinInTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMvrpPortStatsJoinInTransmitted.setStatus(_A)
_AlaMvrpPortStatsJoinEmptyTransmitted_Type=Counter32
_AlaMvrpPortStatsJoinEmptyTransmitted_Object=MibTableColumn
alaMvrpPortStatsJoinEmptyTransmitted=_AlaMvrpPortStatsJoinEmptyTransmitted_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1,1,11),_AlaMvrpPortStatsJoinEmptyTransmitted_Type())
alaMvrpPortStatsJoinEmptyTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMvrpPortStatsJoinEmptyTransmitted.setStatus(_A)
_AlaMvrpPortStatsLeaveTransmitted_Type=Counter32
_AlaMvrpPortStatsLeaveTransmitted_Object=MibTableColumn
alaMvrpPortStatsLeaveTransmitted=_AlaMvrpPortStatsLeaveTransmitted_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1,1,12),_AlaMvrpPortStatsLeaveTransmitted_Type())
alaMvrpPortStatsLeaveTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMvrpPortStatsLeaveTransmitted.setStatus(_A)
_AlaMvrpPortStatsInTransmitted_Type=Counter32
_AlaMvrpPortStatsInTransmitted_Object=MibTableColumn
alaMvrpPortStatsInTransmitted=_AlaMvrpPortStatsInTransmitted_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1,1,13),_AlaMvrpPortStatsInTransmitted_Type())
alaMvrpPortStatsInTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMvrpPortStatsInTransmitted.setStatus(_A)
_AlaMvrpPortStatsEmptyTransmitted_Type=Counter32
_AlaMvrpPortStatsEmptyTransmitted_Object=MibTableColumn
alaMvrpPortStatsEmptyTransmitted=_AlaMvrpPortStatsEmptyTransmitted_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1,1,14),_AlaMvrpPortStatsEmptyTransmitted_Type())
alaMvrpPortStatsEmptyTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMvrpPortStatsEmptyTransmitted.setStatus(_A)
_AlaMvrpPortStatsLeaveAllTransmitted_Type=Counter32
_AlaMvrpPortStatsLeaveAllTransmitted_Object=MibTableColumn
alaMvrpPortStatsLeaveAllTransmitted=_AlaMvrpPortStatsLeaveAllTransmitted_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1,1,15),_AlaMvrpPortStatsLeaveAllTransmitted_Type())
alaMvrpPortStatsLeaveAllTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMvrpPortStatsLeaveAllTransmitted.setStatus(_A)
_AlaMvrpPortStatsTotalPDUReceived_Type=Counter32
_AlaMvrpPortStatsTotalPDUReceived_Object=MibTableColumn
alaMvrpPortStatsTotalPDUReceived=_AlaMvrpPortStatsTotalPDUReceived_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1,1,16),_AlaMvrpPortStatsTotalPDUReceived_Type())
alaMvrpPortStatsTotalPDUReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMvrpPortStatsTotalPDUReceived.setStatus(_A)
_AlaMvrpPortStatsTotalPDUTransmitted_Type=Counter32
_AlaMvrpPortStatsTotalPDUTransmitted_Object=MibTableColumn
alaMvrpPortStatsTotalPDUTransmitted=_AlaMvrpPortStatsTotalPDUTransmitted_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1,1,17),_AlaMvrpPortStatsTotalPDUTransmitted_Type())
alaMvrpPortStatsTotalPDUTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMvrpPortStatsTotalPDUTransmitted.setStatus(_A)
_AlaMvrpPortStatsTotalMsgsReceived_Type=Counter32
_AlaMvrpPortStatsTotalMsgsReceived_Object=MibTableColumn
alaMvrpPortStatsTotalMsgsReceived=_AlaMvrpPortStatsTotalMsgsReceived_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1,1,18),_AlaMvrpPortStatsTotalMsgsReceived_Type())
alaMvrpPortStatsTotalMsgsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMvrpPortStatsTotalMsgsReceived.setStatus(_A)
_AlaMvrpPortStatsTotalMsgsTransmitted_Type=Counter32
_AlaMvrpPortStatsTotalMsgsTransmitted_Object=MibTableColumn
alaMvrpPortStatsTotalMsgsTransmitted=_AlaMvrpPortStatsTotalMsgsTransmitted_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1,1,19),_AlaMvrpPortStatsTotalMsgsTransmitted_Type())
alaMvrpPortStatsTotalMsgsTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMvrpPortStatsTotalMsgsTransmitted.setStatus(_A)
_AlaMvrpPortStatsInvalidMsgsReceived_Type=Counter32
_AlaMvrpPortStatsInvalidMsgsReceived_Object=MibTableColumn
alaMvrpPortStatsInvalidMsgsReceived=_AlaMvrpPortStatsInvalidMsgsReceived_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1,1,20),_AlaMvrpPortStatsInvalidMsgsReceived_Type())
alaMvrpPortStatsInvalidMsgsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMvrpPortStatsInvalidMsgsReceived.setStatus(_A)
_AlaMvrpPortFailedRegistrations_Type=Counter32
_AlaMvrpPortFailedRegistrations_Object=MibTableColumn
alaMvrpPortFailedRegistrations=_AlaMvrpPortFailedRegistrations_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1,1,21),_AlaMvrpPortFailedRegistrations_Type())
alaMvrpPortFailedRegistrations.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMvrpPortFailedRegistrations.setStatus(_A)
_AlaMvrpPortLastPduOrigin_Type=MacAddress
_AlaMvrpPortLastPduOrigin_Object=MibTableColumn
alaMvrpPortLastPduOrigin=_AlaMvrpPortLastPduOrigin_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1,1,22),_AlaMvrpPortLastPduOrigin_Type())
alaMvrpPortLastPduOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:alaMvrpPortLastPduOrigin.setStatus(_A)
class _AlaMvrpPortStatsClearStats_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),('reset',1)))
_AlaMvrpPortStatsClearStats_Type.__name__=_E
_AlaMvrpPortStatsClearStats_Object=MibTableColumn
alaMvrpPortStatsClearStats=_AlaMvrpPortStatsClearStats_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,8,1,1,23),_AlaMvrpPortStatsClearStats_Type())
alaMvrpPortStatsClearStats.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMvrpPortStatsClearStats.setStatus(_A)
_AlaMvrpPortRestrictVlanConfig_ObjectIdentity=ObjectIdentity
alaMvrpPortRestrictVlanConfig=_AlaMvrpPortRestrictVlanConfig_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,9))
_AlaMvrpPortRestrictVlanConfigTable_Object=MibTable
alaMvrpPortRestrictVlanConfigTable=_AlaMvrpPortRestrictVlanConfigTable_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,9,1))
if mibBuilder.loadTexts:alaMvrpPortRestrictVlanConfigTable.setStatus(_A)
_AlaMvrpPortRestrictVlanConfigEntry_Object=MibTableRow
alaMvrpPortRestrictVlanConfigEntry=_AlaMvrpPortRestrictVlanConfigEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,9,1,1))
alaMvrpPortRestrictVlanConfigEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:alaMvrpPortRestrictVlanConfigEntry.setStatus(_A)
_AlaMvrpPortRestrictVlanIfIndex_Type=InterfaceIndex
_AlaMvrpPortRestrictVlanIfIndex_Object=MibTableColumn
alaMvrpPortRestrictVlanIfIndex=_AlaMvrpPortRestrictVlanIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,9,1,1,1),_AlaMvrpPortRestrictVlanIfIndex_Type())
alaMvrpPortRestrictVlanIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:alaMvrpPortRestrictVlanIfIndex.setStatus(_A)
_AlaMvrpPortRestrictVlanID_Type=VlanId
_AlaMvrpPortRestrictVlanID_Object=MibTableColumn
alaMvrpPortRestrictVlanID=_AlaMvrpPortRestrictVlanID_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,9,1,1,2),_AlaMvrpPortRestrictVlanID_Type())
alaMvrpPortRestrictVlanID.setMaxAccess(_G)
if mibBuilder.loadTexts:alaMvrpPortRestrictVlanID.setStatus(_A)
class _AlaMvrpPortVlanRestrictions_Type(MvrpPortVlanRestrictBitmap):defaultBinValue='1'
_AlaMvrpPortVlanRestrictions_Type.__name__=_Q
_AlaMvrpPortVlanRestrictions_Object=MibTableColumn
alaMvrpPortVlanRestrictions=_AlaMvrpPortVlanRestrictions_Object((1,3,6,1,4,1,6486,800,1,2,1,57,1,1,9,1,1,3),_AlaMvrpPortVlanRestrictions_Type())
alaMvrpPortVlanRestrictions.setMaxAccess(_D)
if mibBuilder.loadTexts:alaMvrpPortVlanRestrictions.setStatus(_A)
_AlcatelIND1MVRPMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1MVRPMIBConformance=_AlcatelIND1MVRPMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,57,1,2))
if mibBuilder.loadTexts:alcatelIND1MVRPMIBConformance.setStatus(_A)
_AlcatelIND1MVRPMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1MVRPMIBGroups=_AlcatelIND1MVRPMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,57,1,2,1))
if mibBuilder.loadTexts:alcatelIND1MVRPMIBGroups.setStatus(_A)
_AlcatelIND1MVRPMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1MVRPMIBCompliances=_AlcatelIND1MVRPMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,57,1,2,2))
if mibBuilder.loadTexts:alcatelIND1MVRPMIBCompliances.setStatus(_A)
alaMvrpBaseGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,57,1,2,1,1))
alaMvrpBaseGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_I),(_B,_J),(_B,_U)))
if mibBuilder.loadTexts:alaMvrpBaseGroup.setStatus(_A)
alaMvrpPortConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,57,1,2,1,2))
alaMvrpPortConfigGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:alaMvrpPortConfigGroup.setStatus(_A)
alaMvrpPortStatsGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,57,1,2,1,3))
alaMvrpPortStatsGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:alaMvrpPortStatsGroup.setStatus(_A)
alaMvrpPortRestrictVlanConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,57,1,2,1,4))
alaMvrpPortRestrictVlanConfigGroup.setObjects((_B,_z))
if mibBuilder.loadTexts:alaMvrpPortRestrictVlanConfigGroup.setStatus(_A)
alaMvrpVlanLimitReachedEvent=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,57,1,0,1))
alaMvrpVlanLimitReachedEvent.setObjects((_B,_I))
if mibBuilder.loadTexts:alaMvrpVlanLimitReachedEvent.setStatus(_A)
alaMvrpE2eVlanConflict=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,57,1,0,2))
alaMvrpE2eVlanConflict.setObjects((_B,_J))
if mibBuilder.loadTexts:alaMvrpE2eVlanConflict.setStatus(_A)
alaMvrpNotifyGroup=NotificationGroup((1,3,6,1,4,1,6486,800,1,2,1,57,1,2,1,5))
alaMvrpNotifyGroup.setObjects(*((_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:alaMvrpNotifyGroup.setStatus(_A)
alcatelIND1MVRPMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,57,1,2,2,1))
alcatelIND1MVRPMIBCompliance.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:alcatelIND1MVRPMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_Q:MvrpPortVlanRestrictBitmap,'alcatelIND1MVRPMIB':alcatelIND1MVRPMIB,'alaMvrpEvents':alaMvrpEvents,_A1:alaMvrpVlanLimitReachedEvent,_A0:alaMvrpE2eVlanConflict,'alcatelIND1MVRPMIBObjects':alcatelIND1MVRPMIBObjects,_R:alaMvrpGlobalStatus,_S:alaMvrpGlobalClearStats,_T:alaMvrpTransparentSwitching,_I:alaMvrpMaxVlanLimit,_J:alaMvrpVlanConflictInfo,_U:alaVlanRegistrationProtocolType,'alaMvrpPortConfig':alaMvrpPortConfig,'alaMvrpPortConfigTable':alaMvrpPortConfigTable,'alaMvrpPortConfigEntry':alaMvrpPortConfigEntry,_M:alaMvrpPortConfigIfIndex,_V:alaMvrpPortStatus,_W:alaMvrpPortConfigRegistrarMode,_X:alaMvrpPortConfigApplicantMode,_Y:alaMvrpPortConfigJoinTimer,_Z:alaMvrpPortConfigLeaveTimer,_a:alaMvrpPortConfigLeaveAllTimer,_b:alaMvrpPortConfigPeriodicTimer,_c:alaMvrpPortConfigPeriodicTransmissionStatus,'alaMvrpPortStats':alaMvrpPortStats,'alaMvrpPortStatsTable':alaMvrpPortStatsTable,'alaMvrpPortStatsEntry':alaMvrpPortStatsEntry,_N:alaMvrpPortStatsIfIndex,_d:alaMvrpPortStatsNewReceived,_e:alaMvrpPortStatsJoinInReceived,_f:alaMvrpPortStatsJoinEmptyReceived,_g:alaMvrpPortStatsLeaveReceived,_h:alaMvrpPortStatsInReceived,_i:alaMvrpPortStatsEmptyReceived,_j:alaMvrpPortStatsLeaveAllReceived,_k:alaMvrpPortStatsNewTransmitted,_l:alaMvrpPortStatsJoinInTransmitted,_m:alaMvrpPortStatsJoinEmptyTransmitted,_n:alaMvrpPortStatsLeaveTransmitted,_o:alaMvrpPortStatsInTransmitted,_p:alaMvrpPortStatsEmptyTransmitted,_q:alaMvrpPortStatsLeaveAllTransmitted,_r:alaMvrpPortStatsTotalPDUReceived,_s:alaMvrpPortStatsTotalPDUTransmitted,_t:alaMvrpPortStatsTotalMsgsReceived,_u:alaMvrpPortStatsTotalMsgsTransmitted,_v:alaMvrpPortStatsInvalidMsgsReceived,_w:alaMvrpPortFailedRegistrations,_x:alaMvrpPortLastPduOrigin,_y:alaMvrpPortStatsClearStats,'alaMvrpPortRestrictVlanConfig':alaMvrpPortRestrictVlanConfig,'alaMvrpPortRestrictVlanConfigTable':alaMvrpPortRestrictVlanConfigTable,'alaMvrpPortRestrictVlanConfigEntry':alaMvrpPortRestrictVlanConfigEntry,_O:alaMvrpPortRestrictVlanIfIndex,_P:alaMvrpPortRestrictVlanID,_z:alaMvrpPortVlanRestrictions,'alcatelIND1MVRPMIBConformance':alcatelIND1MVRPMIBConformance,'alcatelIND1MVRPMIBGroups':alcatelIND1MVRPMIBGroups,_A2:alaMvrpBaseGroup,_A3:alaMvrpPortConfigGroup,_A4:alaMvrpPortStatsGroup,_A5:alaMvrpPortRestrictVlanConfigGroup,_A6:alaMvrpNotifyGroup,'alcatelIND1MVRPMIBCompliances':alcatelIND1MVRPMIBCompliances,'alcatelIND1MVRPMIBCompliance':alcatelIND1MVRPMIBCompliance})