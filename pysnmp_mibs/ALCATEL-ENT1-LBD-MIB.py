_A8='alaLbdVlanViolationStatisticsGroup'
_A7='alaLbdVlanConfigGroup'
_A6='alaLbdTrapsGroup'
_A5='alaLbdStateTrapForAutoRecoveryGroup'
_A4='alaLbdStateTrapForClearViolationAllGroup'
_A3='alaLbdStateTrapToShutdownGroup'
_A2='alaLbdPortStatusGroup'
_A1='alaLbdIntfConfigGroup'
_A0='alaLbdGlobalConfigGroup'
_z='alaLbdStateChangeToShutdown'
_y='alaLbdStateChangeForClearViolationAll'
_x='alaLbdStateChangeForAutoRecovery'
_w='alaLbdViolatedVlanId'
_v='alaLbdVlanStatus'
_u='alaLbdPortLinkAgg'
_t='alaLbdPortStatsClear'
_s='alaLbdPortLbdSent'
_r='alaLbdPortNumLbdInvalidRcvd'
_q='alaLbdPortRemoteConfigAdminStatus'
_p='alaLbdPortAFDConfig'
_o='alaLbdPortConfigServiceAccessType'
_n='alaLbdPortConfigLbdOperStatus'
_m='alaLbdPortConfigLbdAdminStatus'
_l='alaLbdGlobalRemoteConfigStatus'
_k='alaLbdVlanConfigAllVlan'
_j='alaLbdVlanConfigLbdAdminStatus'
_i='alaLbdVlanGlobalConfigTransmissionTimer'
_h='alaLbdGlobalStatusAFDConfig'
_g='alaLbdGlobalConfigAutorecoveryTimer'
_f='alaLbdGlobalClearPortStat'
_e='alaLbdGlobalConfigTransmissionTimer'
_d='alaLbdGlobalConfigStatus'
_c='alaLbdVlanIfindex'
_b='alaLbdVlanId'
_a='alaLbdPortStatsIfIndex'
_Z='alaLbdPortConfigIfIndex'
_Y='default'
_X='remoteShutdown'
_W='inactive'
_V='alaLbdCurrentStateAutoRecovery'
_U='alaLbdPreviousStateAutoRecovery'
_T='alaLbdCurrentStateClearViolationAll'
_S='alaLbdPreviousStateClearViolationAll'
_R='alaLbdCurrentState'
_Q='alaLbdPreviousState'
_P='alaLbdPortRemoteBridgeID'
_O='alaLbdPortRemoteSrcMacAddr'
_N='seconds'
_M='normal'
_L='not-accessible'
_K='shutdown'
_J='alaLbdPortIfIndex'
_I='disable'
_H='enable'
_G='Unsigned32'
_F='accessible-for-notify'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='ALCATEL-ENT1-LBD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1Lbd,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1Lbd')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
alcatelIND1LBDMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,82,1))
if mibBuilder.loadTexts:alcatelIND1LBDMIB.setRevisions(('2008-12-10 00:00',))
class AlaLbdPortConfigLbdOperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_W,0),(_M,1),(_K,2),(_X,3)))
class AlaLbdCurrentStateCVAorAR(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),(_M,1)))
_AlaLbdTraps_ObjectIdentity=ObjectIdentity
alaLbdTraps=_AlaLbdTraps_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,82,1,0))
if mibBuilder.loadTexts:alaLbdTraps.setStatus(_A)
_AlcatelIND1LBDMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1LBDMIBObjects=_AlcatelIND1LBDMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,82,1,1))
if mibBuilder.loadTexts:alcatelIND1LBDMIBObjects.setStatus(_A)
class _AlaLbdGlobalConfigStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AlaLbdGlobalConfigStatus_Type.__name__=_C
_AlaLbdGlobalConfigStatus_Object=MibScalar
alaLbdGlobalConfigStatus=_AlaLbdGlobalConfigStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,1),_AlaLbdGlobalConfigStatus_Type())
alaLbdGlobalConfigStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaLbdGlobalConfigStatus.setStatus(_A)
class _AlaLbdGlobalConfigTransmissionTimer_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,600))
_AlaLbdGlobalConfigTransmissionTimer_Type.__name__=_G
_AlaLbdGlobalConfigTransmissionTimer_Object=MibScalar
alaLbdGlobalConfigTransmissionTimer=_AlaLbdGlobalConfigTransmissionTimer_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,2),_AlaLbdGlobalConfigTransmissionTimer_Type())
alaLbdGlobalConfigTransmissionTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:alaLbdGlobalConfigTransmissionTimer.setStatus(_A)
if mibBuilder.loadTexts:alaLbdGlobalConfigTransmissionTimer.setUnits(_N)
class _AlaLbdGlobalClearPortStat_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Y,0),('reset',1)))
_AlaLbdGlobalClearPortStat_Type.__name__=_C
_AlaLbdGlobalClearPortStat_Object=MibScalar
alaLbdGlobalClearPortStat=_AlaLbdGlobalClearPortStat_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,3),_AlaLbdGlobalClearPortStat_Type())
alaLbdGlobalClearPortStat.setMaxAccess(_D)
if mibBuilder.loadTexts:alaLbdGlobalClearPortStat.setStatus(_A)
class _AlaLbdGlobalConfigAutorecoveryTimer_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_AlaLbdGlobalConfigAutorecoveryTimer_Type.__name__=_G
_AlaLbdGlobalConfigAutorecoveryTimer_Object=MibScalar
alaLbdGlobalConfigAutorecoveryTimer=_AlaLbdGlobalConfigAutorecoveryTimer_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,4),_AlaLbdGlobalConfigAutorecoveryTimer_Type())
alaLbdGlobalConfigAutorecoveryTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:alaLbdGlobalConfigAutorecoveryTimer.setStatus(_A)
if mibBuilder.loadTexts:alaLbdGlobalConfigAutorecoveryTimer.setUnits(_N)
_AlaLbdPortConfig_ObjectIdentity=ObjectIdentity
alaLbdPortConfig=_AlaLbdPortConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,5))
_AlaLbdPortConfigTable_Object=MibTable
alaLbdPortConfigTable=_AlaLbdPortConfigTable_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,5,1))
if mibBuilder.loadTexts:alaLbdPortConfigTable.setStatus(_A)
_AlaLbdPortConfigEntry_Object=MibTableRow
alaLbdPortConfigEntry=_AlaLbdPortConfigEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,5,1,1))
alaLbdPortConfigEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:alaLbdPortConfigEntry.setStatus(_A)
_AlaLbdPortConfigIfIndex_Type=InterfaceIndex
_AlaLbdPortConfigIfIndex_Object=MibTableColumn
alaLbdPortConfigIfIndex=_AlaLbdPortConfigIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,5,1,1,1),_AlaLbdPortConfigIfIndex_Type())
alaLbdPortConfigIfIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:alaLbdPortConfigIfIndex.setStatus(_A)
class _AlaLbdPortConfigLbdAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AlaLbdPortConfigLbdAdminStatus_Type.__name__=_C
_AlaLbdPortConfigLbdAdminStatus_Object=MibTableColumn
alaLbdPortConfigLbdAdminStatus=_AlaLbdPortConfigLbdAdminStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,5,1,1,2),_AlaLbdPortConfigLbdAdminStatus_Type())
alaLbdPortConfigLbdAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaLbdPortConfigLbdAdminStatus.setStatus(_A)
_AlaLbdPortConfigLbdOperStatus_Type=AlaLbdPortConfigLbdOperStatus
_AlaLbdPortConfigLbdOperStatus_Object=MibTableColumn
alaLbdPortConfigLbdOperStatus=_AlaLbdPortConfigLbdOperStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,5,1,1,3),_AlaLbdPortConfigLbdOperStatus_Type())
alaLbdPortConfigLbdOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaLbdPortConfigLbdOperStatus.setStatus(_A)
class _AlaLbdPortConfigServiceAccessType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normalEdge',1),('serviceEdge',2),('noValue',3)))
_AlaLbdPortConfigServiceAccessType_Type.__name__=_C
_AlaLbdPortConfigServiceAccessType_Object=MibTableColumn
alaLbdPortConfigServiceAccessType=_AlaLbdPortConfigServiceAccessType_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,5,1,1,4),_AlaLbdPortConfigServiceAccessType_Type())
alaLbdPortConfigServiceAccessType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaLbdPortConfigServiceAccessType.setStatus(_A)
class _AlaLbdPortAFDConfig_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('admin',1),('autoFarbic',2)))
_AlaLbdPortAFDConfig_Type.__name__=_C
_AlaLbdPortAFDConfig_Object=MibTableColumn
alaLbdPortAFDConfig=_AlaLbdPortAFDConfig_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,5,1,1,5),_AlaLbdPortAFDConfig_Type())
alaLbdPortAFDConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:alaLbdPortAFDConfig.setStatus(_A)
class _AlaLbdPortRemoteConfigAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AlaLbdPortRemoteConfigAdminStatus_Type.__name__=_C
_AlaLbdPortRemoteConfigAdminStatus_Object=MibTableColumn
alaLbdPortRemoteConfigAdminStatus=_AlaLbdPortRemoteConfigAdminStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,5,1,1,6),_AlaLbdPortRemoteConfigAdminStatus_Type())
alaLbdPortRemoteConfigAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaLbdPortRemoteConfigAdminStatus.setStatus(_A)
_AlaLbdPortRemoteSrcMacAddr_Type=MacAddress
_AlaLbdPortRemoteSrcMacAddr_Object=MibTableColumn
alaLbdPortRemoteSrcMacAddr=_AlaLbdPortRemoteSrcMacAddr_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,5,1,1,7),_AlaLbdPortRemoteSrcMacAddr_Type())
alaLbdPortRemoteSrcMacAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:alaLbdPortRemoteSrcMacAddr.setStatus(_A)
_AlaLbdPortRemoteBridgeID_Type=MacAddress
_AlaLbdPortRemoteBridgeID_Object=MibTableColumn
alaLbdPortRemoteBridgeID=_AlaLbdPortRemoteBridgeID_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,5,1,1,8),_AlaLbdPortRemoteBridgeID_Type())
alaLbdPortRemoteBridgeID.setMaxAccess(_E)
if mibBuilder.loadTexts:alaLbdPortRemoteBridgeID.setStatus(_A)
_AlaLbdPortStat_ObjectIdentity=ObjectIdentity
alaLbdPortStat=_AlaLbdPortStat_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,6))
_AlaLbdPortStatsTable_Object=MibTable
alaLbdPortStatsTable=_AlaLbdPortStatsTable_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,6,1))
if mibBuilder.loadTexts:alaLbdPortStatsTable.setStatus(_A)
_AlaLbdPortStatsEntry_Object=MibTableRow
alaLbdPortStatsEntry=_AlaLbdPortStatsEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,6,1,1))
alaLbdPortStatsEntry.setIndexNames((0,_B,_a))
if mibBuilder.loadTexts:alaLbdPortStatsEntry.setStatus(_A)
_AlaLbdPortStatsIfIndex_Type=InterfaceIndex
_AlaLbdPortStatsIfIndex_Object=MibTableColumn
alaLbdPortStatsIfIndex=_AlaLbdPortStatsIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,6,1,1,1),_AlaLbdPortStatsIfIndex_Type())
alaLbdPortStatsIfIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:alaLbdPortStatsIfIndex.setStatus(_A)
_AlaLbdPortNumLbdInvalidRcvd_Type=Counter32
_AlaLbdPortNumLbdInvalidRcvd_Object=MibTableColumn
alaLbdPortNumLbdInvalidRcvd=_AlaLbdPortNumLbdInvalidRcvd_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,6,1,1,2),_AlaLbdPortNumLbdInvalidRcvd_Type())
alaLbdPortNumLbdInvalidRcvd.setMaxAccess(_E)
if mibBuilder.loadTexts:alaLbdPortNumLbdInvalidRcvd.setStatus(_A)
_AlaLbdPortLbdSent_Type=Counter32
_AlaLbdPortLbdSent_Object=MibTableColumn
alaLbdPortLbdSent=_AlaLbdPortLbdSent_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,6,1,1,3),_AlaLbdPortLbdSent_Type())
alaLbdPortLbdSent.setMaxAccess(_E)
if mibBuilder.loadTexts:alaLbdPortLbdSent.setStatus(_A)
class _AlaLbdPortStatsClear_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Y,0),('reset',1)))
_AlaLbdPortStatsClear_Type.__name__=_C
_AlaLbdPortStatsClear_Object=MibTableColumn
alaLbdPortStatsClear=_AlaLbdPortStatsClear_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,6,1,1,4),_AlaLbdPortStatsClear_Type())
alaLbdPortStatsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:alaLbdPortStatsClear.setStatus(_A)
class _AlaLbdPortLinkAgg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_AlaLbdPortLinkAgg_Type.__name__=_C
_AlaLbdPortLinkAgg_Object=MibTableColumn
alaLbdPortLinkAgg=_AlaLbdPortLinkAgg_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,6,1,1,5),_AlaLbdPortLinkAgg_Type())
alaLbdPortLinkAgg.setMaxAccess(_E)
if mibBuilder.loadTexts:alaLbdPortLinkAgg.setStatus(_A)
_AlaLbdTrapsObj_ObjectIdentity=ObjectIdentity
alaLbdTrapsObj=_AlaLbdTrapsObj_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,7))
_AlaLbdPortIfIndex_Type=InterfaceIndex
_AlaLbdPortIfIndex_Object=MibScalar
alaLbdPortIfIndex=_AlaLbdPortIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,7,1),_AlaLbdPortIfIndex_Type())
alaLbdPortIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:alaLbdPortIfIndex.setStatus(_A)
class _AlaLbdPreviousState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_M,1))
_AlaLbdPreviousState_Type.__name__=_C
_AlaLbdPreviousState_Object=MibScalar
alaLbdPreviousState=_AlaLbdPreviousState_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,7,2),_AlaLbdPreviousState_Type())
alaLbdPreviousState.setMaxAccess(_F)
if mibBuilder.loadTexts:alaLbdPreviousState.setStatus(_A)
class _AlaLbdCurrentState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_X,2)))
_AlaLbdCurrentState_Type.__name__=_C
_AlaLbdCurrentState_Object=MibScalar
alaLbdCurrentState=_AlaLbdCurrentState_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,7,3),_AlaLbdCurrentState_Type())
alaLbdCurrentState.setMaxAccess(_F)
if mibBuilder.loadTexts:alaLbdCurrentState.setStatus(_A)
class _AlaLbdPreviousStateClearViolationAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_K,1))
_AlaLbdPreviousStateClearViolationAll_Type.__name__=_C
_AlaLbdPreviousStateClearViolationAll_Object=MibScalar
alaLbdPreviousStateClearViolationAll=_AlaLbdPreviousStateClearViolationAll_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,7,4),_AlaLbdPreviousStateClearViolationAll_Type())
alaLbdPreviousStateClearViolationAll.setMaxAccess(_F)
if mibBuilder.loadTexts:alaLbdPreviousStateClearViolationAll.setStatus(_A)
_AlaLbdCurrentStateClearViolationAll_Type=AlaLbdCurrentStateCVAorAR
_AlaLbdCurrentStateClearViolationAll_Object=MibScalar
alaLbdCurrentStateClearViolationAll=_AlaLbdCurrentStateClearViolationAll_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,7,5),_AlaLbdCurrentStateClearViolationAll_Type())
alaLbdCurrentStateClearViolationAll.setMaxAccess(_F)
if mibBuilder.loadTexts:alaLbdCurrentStateClearViolationAll.setStatus(_A)
class _AlaLbdPreviousStateAutoRecovery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_K,1))
_AlaLbdPreviousStateAutoRecovery_Type.__name__=_C
_AlaLbdPreviousStateAutoRecovery_Object=MibScalar
alaLbdPreviousStateAutoRecovery=_AlaLbdPreviousStateAutoRecovery_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,7,6),_AlaLbdPreviousStateAutoRecovery_Type())
alaLbdPreviousStateAutoRecovery.setMaxAccess(_F)
if mibBuilder.loadTexts:alaLbdPreviousStateAutoRecovery.setStatus(_A)
_AlaLbdCurrentStateAutoRecovery_Type=AlaLbdCurrentStateCVAorAR
_AlaLbdCurrentStateAutoRecovery_Object=MibScalar
alaLbdCurrentStateAutoRecovery=_AlaLbdCurrentStateAutoRecovery_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,7,7),_AlaLbdCurrentStateAutoRecovery_Type())
alaLbdCurrentStateAutoRecovery.setMaxAccess(_F)
if mibBuilder.loadTexts:alaLbdCurrentStateAutoRecovery.setStatus(_A)
class _AlaLbdGlobalStatusAFDConfig_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('admin',1),('autoFabric',2)))
_AlaLbdGlobalStatusAFDConfig_Type.__name__=_C
_AlaLbdGlobalStatusAFDConfig_Object=MibScalar
alaLbdGlobalStatusAFDConfig=_AlaLbdGlobalStatusAFDConfig_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,8),_AlaLbdGlobalStatusAFDConfig_Type())
alaLbdGlobalStatusAFDConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:alaLbdGlobalStatusAFDConfig.setStatus(_A)
class _AlaLbdVlanGlobalConfigTransmissionTimer_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_AlaLbdVlanGlobalConfigTransmissionTimer_Type.__name__=_G
_AlaLbdVlanGlobalConfigTransmissionTimer_Object=MibScalar
alaLbdVlanGlobalConfigTransmissionTimer=_AlaLbdVlanGlobalConfigTransmissionTimer_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,9),_AlaLbdVlanGlobalConfigTransmissionTimer_Type())
alaLbdVlanGlobalConfigTransmissionTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:alaLbdVlanGlobalConfigTransmissionTimer.setStatus(_A)
if mibBuilder.loadTexts:alaLbdVlanGlobalConfigTransmissionTimer.setUnits(_N)
class _AlaLbdVlanConfigLbdAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AlaLbdVlanConfigLbdAdminStatus_Type.__name__=_C
_AlaLbdVlanConfigLbdAdminStatus_Object=MibScalar
alaLbdVlanConfigLbdAdminStatus=_AlaLbdVlanConfigLbdAdminStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,10),_AlaLbdVlanConfigLbdAdminStatus_Type())
alaLbdVlanConfigLbdAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaLbdVlanConfigLbdAdminStatus.setStatus(_A)
class _AlaLbdVlanConfigAllVlan_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AlaLbdVlanConfigAllVlan_Type.__name__=_C
_AlaLbdVlanConfigAllVlan_Object=MibScalar
alaLbdVlanConfigAllVlan=_AlaLbdVlanConfigAllVlan_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,11),_AlaLbdVlanConfigAllVlan_Type())
alaLbdVlanConfigAllVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:alaLbdVlanConfigAllVlan.setStatus(_A)
_AlaLbdVlanConfig_ObjectIdentity=ObjectIdentity
alaLbdVlanConfig=_AlaLbdVlanConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,12))
_AlaLbdVlanTable_Object=MibTable
alaLbdVlanTable=_AlaLbdVlanTable_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,12,1))
if mibBuilder.loadTexts:alaLbdVlanTable.setStatus(_A)
_AlaLbdVlanEntry_Object=MibTableRow
alaLbdVlanEntry=_AlaLbdVlanEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,12,1,1))
alaLbdVlanEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:alaLbdVlanEntry.setStatus(_A)
class _AlaLbdVlanId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_AlaLbdVlanId_Type.__name__=_G
_AlaLbdVlanId_Object=MibTableColumn
alaLbdVlanId=_AlaLbdVlanId_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,12,1,1,1),_AlaLbdVlanId_Type())
alaLbdVlanId.setMaxAccess(_L)
if mibBuilder.loadTexts:alaLbdVlanId.setStatus(_A)
_AlaLbdVlanStatus_Type=RowStatus
_AlaLbdVlanStatus_Object=MibTableColumn
alaLbdVlanStatus=_AlaLbdVlanStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,12,1,1,2),_AlaLbdVlanStatus_Type())
alaLbdVlanStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:alaLbdVlanStatus.setStatus(_A)
_AlaLbdVlanViolationStatistics_ObjectIdentity=ObjectIdentity
alaLbdVlanViolationStatistics=_AlaLbdVlanViolationStatistics_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,13))
_AlaLbdVlanViolationStatisticsTable_Object=MibTable
alaLbdVlanViolationStatisticsTable=_AlaLbdVlanViolationStatisticsTable_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,13,1))
if mibBuilder.loadTexts:alaLbdVlanViolationStatisticsTable.setStatus(_A)
_AlaLbdVlanViolationStatisticsEntry_Object=MibTableRow
alaLbdVlanViolationStatisticsEntry=_AlaLbdVlanViolationStatisticsEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,13,1,1))
alaLbdVlanViolationStatisticsEntry.setIndexNames((0,_B,_c))
if mibBuilder.loadTexts:alaLbdVlanViolationStatisticsEntry.setStatus(_A)
class _AlaLbdVlanIfindex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1001,4294967295))
_AlaLbdVlanIfindex_Type.__name__=_G
_AlaLbdVlanIfindex_Object=MibTableColumn
alaLbdVlanIfindex=_AlaLbdVlanIfindex_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,13,1,1,1),_AlaLbdVlanIfindex_Type())
alaLbdVlanIfindex.setMaxAccess(_L)
if mibBuilder.loadTexts:alaLbdVlanIfindex.setStatus(_A)
class _AlaLbdViolatedVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_AlaLbdViolatedVlanId_Type.__name__=_C
_AlaLbdViolatedVlanId_Object=MibTableColumn
alaLbdViolatedVlanId=_AlaLbdViolatedVlanId_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,13,1,1,2),_AlaLbdViolatedVlanId_Type())
alaLbdViolatedVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:alaLbdViolatedVlanId.setStatus(_A)
class _AlaLbdGlobalRemoteConfigStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AlaLbdGlobalRemoteConfigStatus_Type.__name__=_C
_AlaLbdGlobalRemoteConfigStatus_Object=MibScalar
alaLbdGlobalRemoteConfigStatus=_AlaLbdGlobalRemoteConfigStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,82,1,1,14),_AlaLbdGlobalRemoteConfigStatus_Type())
alaLbdGlobalRemoteConfigStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaLbdGlobalRemoteConfigStatus.setStatus(_A)
_AlcatelIND1LBDMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1LBDMIBConformance=_AlcatelIND1LBDMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,82,1,2))
if mibBuilder.loadTexts:alcatelIND1LBDMIBConformance.setStatus(_A)
_AlcatelIND1LBDMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1LBDMIBGroups=_AlcatelIND1LBDMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,82,1,2,1))
if mibBuilder.loadTexts:alcatelIND1LBDMIBGroups.setStatus(_A)
_AlcatelIND1LBDMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1LBDMIBCompliances=_AlcatelIND1LBDMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,82,1,2,2))
if mibBuilder.loadTexts:alcatelIND1LBDMIBCompliances.setStatus(_A)
alaLbdGlobalConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,82,1,2,1,1))
alaLbdGlobalConfigGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:alaLbdGlobalConfigGroup.setStatus(_A)
alaLbdIntfConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,82,1,2,1,2))
alaLbdIntfConfigGroup.setObjects(*((_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:alaLbdIntfConfigGroup.setStatus(_A)
alaLbdPortStatusGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,82,1,2,1,3))
alaLbdPortStatusGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:alaLbdPortStatusGroup.setStatus(_A)
alaLbdStateTrapToShutdownGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,82,1,2,1,4))
alaLbdStateTrapToShutdownGroup.setObjects(*((_B,_J),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:alaLbdStateTrapToShutdownGroup.setStatus(_A)
alaLbdStateTrapForClearViolationAllGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,82,1,2,1,5))
alaLbdStateTrapForClearViolationAllGroup.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:alaLbdStateTrapForClearViolationAllGroup.setStatus(_A)
alaLbdStateTrapForAutoRecoveryGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,82,1,2,1,6))
alaLbdStateTrapForAutoRecoveryGroup.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:alaLbdStateTrapForAutoRecoveryGroup.setStatus(_A)
alaLbdVlanConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,82,1,2,1,8))
alaLbdVlanConfigGroup.setObjects((_B,_v))
if mibBuilder.loadTexts:alaLbdVlanConfigGroup.setStatus(_A)
alaLbdVlanViolationStatisticsGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,82,1,2,1,9))
alaLbdVlanViolationStatisticsGroup.setObjects((_B,_w))
if mibBuilder.loadTexts:alaLbdVlanViolationStatisticsGroup.setStatus(_A)
alaLbdStateChangeToShutdown=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,82,1,0,1))
alaLbdStateChangeToShutdown.setObjects(*((_B,_J),(_B,_Q),(_B,_R),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:alaLbdStateChangeToShutdown.setStatus(_A)
alaLbdStateChangeForClearViolationAll=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,82,1,0,2))
alaLbdStateChangeForClearViolationAll.setObjects(*((_B,_J),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:alaLbdStateChangeForClearViolationAll.setStatus(_A)
alaLbdStateChangeForAutoRecovery=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,82,1,0,3))
alaLbdStateChangeForAutoRecovery.setObjects(*((_B,_J),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:alaLbdStateChangeForAutoRecovery.setStatus(_A)
alaLbdTrapsGroup=NotificationGroup((1,3,6,1,4,1,6486,801,1,2,1,82,1,2,1,7))
alaLbdTrapsGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:alaLbdTrapsGroup.setStatus(_A)
alcatelIND1LBDMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,82,1,2,2,1))
alcatelIND1LBDMIBCompliance.setObjects(*((_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:alcatelIND1LBDMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AlaLbdPortConfigLbdOperStatus':AlaLbdPortConfigLbdOperStatus,'AlaLbdCurrentStateCVAorAR':AlaLbdCurrentStateCVAorAR,'alcatelIND1LBDMIB':alcatelIND1LBDMIB,'alaLbdTraps':alaLbdTraps,_z:alaLbdStateChangeToShutdown,_y:alaLbdStateChangeForClearViolationAll,_x:alaLbdStateChangeForAutoRecovery,'alcatelIND1LBDMIBObjects':alcatelIND1LBDMIBObjects,_d:alaLbdGlobalConfigStatus,_e:alaLbdGlobalConfigTransmissionTimer,_f:alaLbdGlobalClearPortStat,_g:alaLbdGlobalConfigAutorecoveryTimer,'alaLbdPortConfig':alaLbdPortConfig,'alaLbdPortConfigTable':alaLbdPortConfigTable,'alaLbdPortConfigEntry':alaLbdPortConfigEntry,_Z:alaLbdPortConfigIfIndex,_m:alaLbdPortConfigLbdAdminStatus,_n:alaLbdPortConfigLbdOperStatus,_o:alaLbdPortConfigServiceAccessType,_p:alaLbdPortAFDConfig,_q:alaLbdPortRemoteConfigAdminStatus,_O:alaLbdPortRemoteSrcMacAddr,_P:alaLbdPortRemoteBridgeID,'alaLbdPortStat':alaLbdPortStat,'alaLbdPortStatsTable':alaLbdPortStatsTable,'alaLbdPortStatsEntry':alaLbdPortStatsEntry,_a:alaLbdPortStatsIfIndex,_r:alaLbdPortNumLbdInvalidRcvd,_s:alaLbdPortLbdSent,_t:alaLbdPortStatsClear,_u:alaLbdPortLinkAgg,'alaLbdTrapsObj':alaLbdTrapsObj,_J:alaLbdPortIfIndex,_Q:alaLbdPreviousState,_R:alaLbdCurrentState,_S:alaLbdPreviousStateClearViolationAll,_T:alaLbdCurrentStateClearViolationAll,_U:alaLbdPreviousStateAutoRecovery,_V:alaLbdCurrentStateAutoRecovery,_h:alaLbdGlobalStatusAFDConfig,_i:alaLbdVlanGlobalConfigTransmissionTimer,_j:alaLbdVlanConfigLbdAdminStatus,_k:alaLbdVlanConfigAllVlan,'alaLbdVlanConfig':alaLbdVlanConfig,'alaLbdVlanTable':alaLbdVlanTable,'alaLbdVlanEntry':alaLbdVlanEntry,_b:alaLbdVlanId,_v:alaLbdVlanStatus,'alaLbdVlanViolationStatistics':alaLbdVlanViolationStatistics,'alaLbdVlanViolationStatisticsTable':alaLbdVlanViolationStatisticsTable,'alaLbdVlanViolationStatisticsEntry':alaLbdVlanViolationStatisticsEntry,_c:alaLbdVlanIfindex,_w:alaLbdViolatedVlanId,_l:alaLbdGlobalRemoteConfigStatus,'alcatelIND1LBDMIBConformance':alcatelIND1LBDMIBConformance,'alcatelIND1LBDMIBGroups':alcatelIND1LBDMIBGroups,_A0:alaLbdGlobalConfigGroup,_A1:alaLbdIntfConfigGroup,_A2:alaLbdPortStatusGroup,_A3:alaLbdStateTrapToShutdownGroup,_A4:alaLbdStateTrapForClearViolationAllGroup,_A5:alaLbdStateTrapForAutoRecoveryGroup,_A6:alaLbdTrapsGroup,_A7:alaLbdVlanConfigGroup,_A8:alaLbdVlanViolationStatisticsGroup,'alcatelIND1LBDMIBCompliances':alcatelIND1LBDMIBCompliances,'alcatelIND1LBDMIBCompliance':alcatelIND1LBDMIBCompliance})