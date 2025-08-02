_BT='hmtsExtendedRevPortGroup'
_BS='hmtsExtendedFwdPortGroup'
_BR='hmtsExtendedTrapControlGroup'
_BQ='hmtsTrapControlGroup'
_BP='hmtsExtendedRegistrationGroup'
_BO='hmtsCommDeviceGroup'
_BN='hmtsIPDeviceGroup'
_BM='hmtsEventGroup'
_BL='hmtsReqDeviceGroup'
_BK='hmtsReqManagementGroup'
_BJ='hmtsSnmpProtocolInformationGroup'
_BI='hmtsMacProtocolInformationGroup'
_BH='hmtsInformationGroup'
_BG='hmtsRegistrationFailedEvent'
_BF='hmtsRevBackOffMaxExp'
_BE='hmtsRevBackOffMinExp'
_BD='hmtsRevMaxMACRetries'
_BC='hmtsRevACKTimeout'
_BB='hmtsRevBackOffPeriod'
_BA='hmtsRevCRCErrors'
_B9='hmtsRevFrameErrors'
_B8='hmtsRevMulticastAddr'
_B7='hmtsRevMuteLvl'
_B6='hmtsFwdPollTime'
_B5='hmtsFwdMaxPwrLvl'
_B4='hmtsFwdProvPwrLvl'
_B3='hmtsTControlMaxDuration'
_B2='hmtsTControlMulticastAddr'
_B1='hmtsTControlRowStatus'
_B0='hmtsTControlContinuity'
_A_='hmtsTControlChainId'
_Az='hmtsTControlMinDuration'
_Ay='hmtsTControlInterval'
_Ax='hmtsRegMaxDuration'
_Aw='hmtsRegMinDuration'
_Av='hmtsSnmpBroadcastDelay'
_Au='hmtsSnmpTimeout'
_At='hmtsDeviceAccessMode'
_As='hmtsTimePduInt'
_Ar='hmtsChnldescPduInt'
_Aq='hmtsAlarmDiscoveryMode'
_Ap='hmtsMacBroadcastDelay'
_Ao='hmtsTalkPduTimeout'
_An='hmtsMacPduTimeout'
_Am='hmtsTimeServerSyncInterval'
_Al='hmtsTimeServerAddress'
_Ak='hmtsSoftwareVersion'
_Aj='hmtsSerialNumber'
_Ai='hmtsModel'
_Ah='hmtsFreqSwitchMethod'
_Ag='hmtsProxyType'
_Af='hmtsOperState'
_Ae='hmtsAdminState'
_Ad='hmtsCommPhysAddr'
_Ac='hmtsCommManagementMethod'
_Ab='hmtsMulticastCommString'
_Aa='hmtsNetRowStatus'
_AZ='hmtsNetMask'
_AY='hmtsNetEndAddr'
_AX='hmtsIPPhysAddr'
_AW='hmtsIPManagementMethod'
_AV='hmtsMulticastIPAddr'
_AU='hmtsMulticastRowStatus'
_AT='hmtsComStat'
_AS='hmtsDevRowStatus'
_AR='hmtsDevRegTime'
_AQ='hmtsDevRegStatus'
_AP='hmtsDevContNRespCount'
_AO='hmtsDevRespTimeoutCount'
_AN='hmtsDevRqstCount'
_AM='hmtsDevLastRespTime'
_AL='hmtsDevLastStateChg'
_AK='hmtsDevReturnLvl'
_AJ='hmtsDevRevPortId'
_AI='hmtsDevFwdPortId'
_AH='hmtsDevCommString'
_AG='hmtsDevIPAddr'
_AF='hmtsDevInErr'
_AE='hmtsRevReturnLvl'
_AD='hmtsRevPortOperState'
_AC='hmtsRevFrequency'
_AB='hmtsRevPortType'
_AA='hmtsRevPortDescr'
_A9='hmtsRevFwdPortId'
_A8='hmtsRevPortAdminState'
_A7='hmtsFwdXpndrFrequency'
_A6='hmtsFwdHmtsFrequency'
_A5='hmtsFwdPortType'
_A4='hmtsFwdPortOperState'
_A3='hmtsFwdPortDescr'
_A2='hmtsFwdPortAdminState'
_A1='hmtsRegContinuity'
_A0='hmtsRegInterval'
_z='hmtsCommString'
_y='hmtsNetStartAddr'
_x='hmtsIPDevAddr'
_w='hmtsMulticastPhysAddr'
_v='hmtsComStatPhysAddr'
_u='hmtsDevPhysAddr'
_t='hmtsRevPortId'
_s='otherError'
_r='portComFailure'
_q='freqUnlocked'
_p='noFreqAssgn'
_o='enable'
_n='hmtsFwdPortId'
_m='hmtsTControlId'
_l='continuous'
_k='manual'
_j='registering'
_i='systemGroup'
_h='SNMPv2-MIB'
_g='snmpTargetBasicGroup'
_f='SNMP-TARGET-MIB'
_e='discreteAlarmsGroup'
_d='currentAlarmsGroup'
_c='analogAlarmsGroup'
_b='heCommonNotificationsGroup'
_a='heCommonLogGroup'
_Z='entityPhysicalGroup'
_Y='entityPhysical2Group'
_X='entityNotificationsGroup'
_W='entityGeneralGroup'
_V='hmtsDevComStat'
_U='hmtsDefaultCommString'
_T='1 Hz'
_S='queued'
_R='immediate'
_Q='automatic'
_P='other'
_O='noError'
_N='SCTE-HMS-PROPERTY-MIB'
_M='0.1 dBmV'
_L='ENTITY-MIB'
_K='SCTE-HMS-HE-COMMON-MIB'
_J='1 ms'
_I='1 s'
_H='not-accessible'
_G='DisplayString'
_F='read-create'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='SCTE-HMS-HMTS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entityGeneralGroup,entityNotificationsGroup,entityPhysical2Group,entityPhysicalGroup=mibBuilder.importSymbols(_L,_W,_X,_Y,_Z)
heCommonLogGroup,heCommonNotificationsGroup=mibBuilder.importSymbols(_K,_a,_b)
heHMTS,=mibBuilder.importSymbols('SCTE-HMS-HEADENDIDENT-MIB','heHMTS')
analogAlarmsGroup,currentAlarmsGroup,discreteAlarmsGroup=mibBuilder.importSymbols(_N,_c,_d,_e)
snmpTargetBasicGroup,=mibBuilder.importSymbols(_f,_g)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
systemGroup,=mibBuilder.importSymbols(_h,_i)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'MacAddress','PhysAddress','RowStatus','TextualConvention')
heHMTSMIB=ModuleIdentity((1,3,6,1,4,1,5591,1,11,3,2))
class HmtsComStatCodes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,20,21,30,31,32)));namedValues=NamedValues(*((_O,1),('noRevPortId',2),('notActive',3),('notRegis',4),('pendRegis',5),(_j,6),('transDisabled',7),('rcvrDisabled',8),('rtrnLvl',9),('notResp',10),('invMac',11),('fwdFreqMismatch',12),('invIP',20),('dupIP',21),('invComm',30),('dupComm',31),(_P,32)))
_HeHMTSObjects_ObjectIdentity=ObjectIdentity
heHMTSObjects=_HeHMTSObjects_ObjectIdentity((1,3,6,1,4,1,5591,1,11,3,2,1))
_HmtsNotifications_ObjectIdentity=ObjectIdentity
hmtsNotifications=_HmtsNotifications_ObjectIdentity((1,3,6,1,4,1,5591,1,11,3,2,1,0))
_HmtsInfoGroup_ObjectIdentity=ObjectIdentity
hmtsInfoGroup=_HmtsInfoGroup_ObjectIdentity((1,3,6,1,4,1,5591,1,11,3,2,1,1))
class _HmtsAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_HmtsAdminState_Type.__name__=_C
_HmtsAdminState_Object=MibScalar
hmtsAdminState=_HmtsAdminState_Object((1,3,6,1,4,1,5591,1,11,3,2,1,1,1),_HmtsAdminState_Type())
hmtsAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsAdminState.setStatus(_A)
class _HmtsOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('operational',1),('swFailure',2),('hwFailure',3)))
_HmtsOperState_Type.__name__=_C
_HmtsOperState_Object=MibScalar
hmtsOperState=_HmtsOperState_Object((1,3,6,1,4,1,5591,1,11,3,2,1,1,2),_HmtsOperState_Type())
hmtsOperState.setMaxAccess(_E)
if mibBuilder.loadTexts:hmtsOperState.setStatus(_A)
class _HmtsProxyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ipBased',1),('communityBased',2),('both',3)))
_HmtsProxyType_Type.__name__=_C
_HmtsProxyType_Object=MibScalar
hmtsProxyType=_HmtsProxyType_Object((1,3,6,1,4,1,5591,1,11,3,2,1,1,3),_HmtsProxyType_Type())
hmtsProxyType.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsProxyType.setStatus(_A)
class _HmtsFreqSwitchMethod_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_k,2)))
_HmtsFreqSwitchMethod_Type.__name__=_C
_HmtsFreqSwitchMethod_Object=MibScalar
hmtsFreqSwitchMethod=_HmtsFreqSwitchMethod_Object((1,3,6,1,4,1,5591,1,11,3,2,1,1,4),_HmtsFreqSwitchMethod_Type())
hmtsFreqSwitchMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsFreqSwitchMethod.setStatus(_A)
class _HmtsModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HmtsModel_Type.__name__=_G
_HmtsModel_Object=MibScalar
hmtsModel=_HmtsModel_Object((1,3,6,1,4,1,5591,1,11,3,2,1,1,5),_HmtsModel_Type())
hmtsModel.setMaxAccess(_E)
if mibBuilder.loadTexts:hmtsModel.setStatus(_A)
class _HmtsSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HmtsSerialNumber_Type.__name__=_G
_HmtsSerialNumber_Object=MibScalar
hmtsSerialNumber=_HmtsSerialNumber_Object((1,3,6,1,4,1,5591,1,11,3,2,1,1,6),_HmtsSerialNumber_Type())
hmtsSerialNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hmtsSerialNumber.setStatus(_A)
class _HmtsSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HmtsSoftwareVersion_Type.__name__=_G
_HmtsSoftwareVersion_Object=MibScalar
hmtsSoftwareVersion=_HmtsSoftwareVersion_Object((1,3,6,1,4,1,5591,1,11,3,2,1,1,7),_HmtsSoftwareVersion_Type())
hmtsSoftwareVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:hmtsSoftwareVersion.setStatus(_A)
_HmtsTimeServerAddress_Type=IpAddress
_HmtsTimeServerAddress_Object=MibScalar
hmtsTimeServerAddress=_HmtsTimeServerAddress_Object((1,3,6,1,4,1,5591,1,11,3,2,1,1,8),_HmtsTimeServerAddress_Type())
hmtsTimeServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsTimeServerAddress.setStatus(_A)
class _HmtsTimeServerSyncInterval_Type(Integer32):defaultValue=86400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3600,8640000))
_HmtsTimeServerSyncInterval_Type.__name__=_C
_HmtsTimeServerSyncInterval_Object=MibScalar
hmtsTimeServerSyncInterval=_HmtsTimeServerSyncInterval_Object((1,3,6,1,4,1,5591,1,11,3,2,1,1,9),_HmtsTimeServerSyncInterval_Type())
hmtsTimeServerSyncInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsTimeServerSyncInterval.setStatus(_A)
if mibBuilder.loadTexts:hmtsTimeServerSyncInterval.setUnits(_I)
_HmtsManagementGroup_ObjectIdentity=ObjectIdentity
hmtsManagementGroup=_HmtsManagementGroup_ObjectIdentity((1,3,6,1,4,1,5591,1,11,3,2,1,2))
_HmtsMacPduGroup_ObjectIdentity=ObjectIdentity
hmtsMacPduGroup=_HmtsMacPduGroup_ObjectIdentity((1,3,6,1,4,1,5591,1,11,3,2,1,2,1))
class _HmtsMacPduTimeout_Type(Integer32):defaultValue=15
_HmtsMacPduTimeout_Type.__name__=_C
_HmtsMacPduTimeout_Object=MibScalar
hmtsMacPduTimeout=_HmtsMacPduTimeout_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,1,1),_HmtsMacPduTimeout_Type())
hmtsMacPduTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsMacPduTimeout.setStatus(_A)
if mibBuilder.loadTexts:hmtsMacPduTimeout.setUnits(_J)
class _HmtsTalkPduTimeout_Type(Integer32):defaultValue=5000
_HmtsTalkPduTimeout_Type.__name__=_C
_HmtsTalkPduTimeout_Object=MibScalar
hmtsTalkPduTimeout=_HmtsTalkPduTimeout_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,1,2),_HmtsTalkPduTimeout_Type())
hmtsTalkPduTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsTalkPduTimeout.setStatus(_A)
if mibBuilder.loadTexts:hmtsTalkPduTimeout.setUnits(_J)
class _HmtsMacBroadcastDelay_Type(Integer32):defaultValue=250
_HmtsMacBroadcastDelay_Type.__name__=_C
_HmtsMacBroadcastDelay_Object=MibScalar
hmtsMacBroadcastDelay=_HmtsMacBroadcastDelay_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,1,3),_HmtsMacBroadcastDelay_Type())
hmtsMacBroadcastDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsMacBroadcastDelay.setStatus(_A)
if mibBuilder.loadTexts:hmtsMacBroadcastDelay.setUnits(_J)
class _HmtsAlarmDiscoveryMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('polling',1),('contention',2),('hybrid',3),('off',4)))
_HmtsAlarmDiscoveryMode_Type.__name__=_C
_HmtsAlarmDiscoveryMode_Object=MibScalar
hmtsAlarmDiscoveryMode=_HmtsAlarmDiscoveryMode_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,1,4),_HmtsAlarmDiscoveryMode_Type())
hmtsAlarmDiscoveryMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsAlarmDiscoveryMode.setStatus(_A)
class _HmtsChnldescPduInt_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_HmtsChnldescPduInt_Type.__name__=_C
_HmtsChnldescPduInt_Object=MibScalar
hmtsChnldescPduInt=_HmtsChnldescPduInt_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,1,5),_HmtsChnldescPduInt_Type())
hmtsChnldescPduInt.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsChnldescPduInt.setStatus(_A)
if mibBuilder.loadTexts:hmtsChnldescPduInt.setUnits(_I)
class _HmtsTimePduInt_Type(Integer32):defaultValue=3600
_HmtsTimePduInt_Type.__name__=_C
_HmtsTimePduInt_Object=MibScalar
hmtsTimePduInt=_HmtsTimePduInt_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,1,6),_HmtsTimePduInt_Type())
hmtsTimePduInt.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsTimePduInt.setStatus(_A)
if mibBuilder.loadTexts:hmtsTimePduInt.setUnits(_I)
class _HmtsDeviceAccessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_S,2),('interrupt',3)))
_HmtsDeviceAccessMode_Type.__name__=_C
_HmtsDeviceAccessMode_Object=MibScalar
hmtsDeviceAccessMode=_HmtsDeviceAccessMode_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,1,7),_HmtsDeviceAccessMode_Type())
hmtsDeviceAccessMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsDeviceAccessMode.setStatus(_A)
_HmtsRegistrationGroup_ObjectIdentity=ObjectIdentity
hmtsRegistrationGroup=_HmtsRegistrationGroup_ObjectIdentity((1,3,6,1,4,1,5591,1,11,3,2,1,2,2))
class _HmtsRegInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_HmtsRegInterval_Type.__name__=_C
_HmtsRegInterval_Object=MibScalar
hmtsRegInterval=_HmtsRegInterval_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,2,1),_HmtsRegInterval_Type())
hmtsRegInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsRegInterval.setStatus(_A)
if mibBuilder.loadTexts:hmtsRegInterval.setUnits(_I)
class _HmtsRegMinDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HmtsRegMinDuration_Type.__name__=_C
_HmtsRegMinDuration_Object=MibScalar
hmtsRegMinDuration=_HmtsRegMinDuration_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,2,2),_HmtsRegMinDuration_Type())
hmtsRegMinDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsRegMinDuration.setStatus(_A)
if mibBuilder.loadTexts:hmtsRegMinDuration.setUnits(_I)
class _HmtsRegMaxDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HmtsRegMaxDuration_Type.__name__=_C
_HmtsRegMaxDuration_Object=MibScalar
hmtsRegMaxDuration=_HmtsRegMaxDuration_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,2,3),_HmtsRegMaxDuration_Type())
hmtsRegMaxDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsRegMaxDuration.setStatus(_A)
if mibBuilder.loadTexts:hmtsRegMaxDuration.setUnits(_I)
class _HmtsRegContinuity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_S,2),(_l,3)))
_HmtsRegContinuity_Type.__name__=_C
_HmtsRegContinuity_Object=MibScalar
hmtsRegContinuity=_HmtsRegContinuity_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,2,4),_HmtsRegContinuity_Type())
hmtsRegContinuity.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsRegContinuity.setStatus(_A)
_HmtsSnmpTrapControlGroup_ObjectIdentity=ObjectIdentity
hmtsSnmpTrapControlGroup=_HmtsSnmpTrapControlGroup_ObjectIdentity((1,3,6,1,4,1,5591,1,11,3,2,1,2,3))
_HmtsTrapControlTable_Object=MibTable
hmtsTrapControlTable=_HmtsTrapControlTable_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,3,1))
if mibBuilder.loadTexts:hmtsTrapControlTable.setStatus(_A)
_HmtsTrapControlEntry_Object=MibTableRow
hmtsTrapControlEntry=_HmtsTrapControlEntry_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,3,1,1))
hmtsTrapControlEntry.setIndexNames((0,_B,_m))
if mibBuilder.loadTexts:hmtsTrapControlEntry.setStatus(_A)
class _HmtsTControlId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HmtsTControlId_Type.__name__=_C
_HmtsTControlId_Object=MibTableColumn
hmtsTControlId=_HmtsTControlId_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,3,1,1,1),_HmtsTControlId_Type())
hmtsTControlId.setMaxAccess(_H)
if mibBuilder.loadTexts:hmtsTControlId.setStatus(_A)
class _HmtsTControlInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_HmtsTControlInterval_Type.__name__=_C
_HmtsTControlInterval_Object=MibTableColumn
hmtsTControlInterval=_HmtsTControlInterval_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,3,1,1,2),_HmtsTControlInterval_Type())
hmtsTControlInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:hmtsTControlInterval.setStatus(_A)
if mibBuilder.loadTexts:hmtsTControlInterval.setUnits(_I)
class _HmtsTControlChainId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_HmtsTControlChainId_Type.__name__=_C
_HmtsTControlChainId_Object=MibTableColumn
hmtsTControlChainId=_HmtsTControlChainId_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,3,1,1,3),_HmtsTControlChainId_Type())
hmtsTControlChainId.setMaxAccess(_F)
if mibBuilder.loadTexts:hmtsTControlChainId.setStatus(_A)
class _HmtsTControlMinDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_HmtsTControlMinDuration_Type.__name__=_C
_HmtsTControlMinDuration_Object=MibTableColumn
hmtsTControlMinDuration=_HmtsTControlMinDuration_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,3,1,1,4),_HmtsTControlMinDuration_Type())
hmtsTControlMinDuration.setMaxAccess(_F)
if mibBuilder.loadTexts:hmtsTControlMinDuration.setStatus(_A)
if mibBuilder.loadTexts:hmtsTControlMinDuration.setUnits(_I)
class _HmtsTControlMaxDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_HmtsTControlMaxDuration_Type.__name__=_C
_HmtsTControlMaxDuration_Object=MibTableColumn
hmtsTControlMaxDuration=_HmtsTControlMaxDuration_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,3,1,1,5),_HmtsTControlMaxDuration_Type())
hmtsTControlMaxDuration.setMaxAccess(_F)
if mibBuilder.loadTexts:hmtsTControlMaxDuration.setStatus(_A)
if mibBuilder.loadTexts:hmtsTControlMaxDuration.setUnits(_I)
class _HmtsTControlContinuity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_S,2),(_l,3)))
_HmtsTControlContinuity_Type.__name__=_C
_HmtsTControlContinuity_Object=MibTableColumn
hmtsTControlContinuity=_HmtsTControlContinuity_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,3,1,1,6),_HmtsTControlContinuity_Type())
hmtsTControlContinuity.setMaxAccess(_F)
if mibBuilder.loadTexts:hmtsTControlContinuity.setStatus(_A)
_HmtsTControlMulticastAddr_Type=MacAddress
_HmtsTControlMulticastAddr_Object=MibTableColumn
hmtsTControlMulticastAddr=_HmtsTControlMulticastAddr_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,3,1,1,7),_HmtsTControlMulticastAddr_Type())
hmtsTControlMulticastAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:hmtsTControlMulticastAddr.setStatus(_A)
_HmtsTControlRowStatus_Type=RowStatus
_HmtsTControlRowStatus_Object=MibTableColumn
hmtsTControlRowStatus=_HmtsTControlRowStatus_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,3,1,1,8),_HmtsTControlRowStatus_Type())
hmtsTControlRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hmtsTControlRowStatus.setStatus(_A)
_HmtsSnmpProtocolGroup_ObjectIdentity=ObjectIdentity
hmtsSnmpProtocolGroup=_HmtsSnmpProtocolGroup_ObjectIdentity((1,3,6,1,4,1,5591,1,11,3,2,1,2,4))
class _HmtsSnmpTimeout_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_HmtsSnmpTimeout_Type.__name__=_C
_HmtsSnmpTimeout_Object=MibScalar
hmtsSnmpTimeout=_HmtsSnmpTimeout_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,4,1),_HmtsSnmpTimeout_Type())
hmtsSnmpTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsSnmpTimeout.setStatus(_A)
if mibBuilder.loadTexts:hmtsSnmpTimeout.setUnits(_J)
class _HmtsSnmpBroadcastDelay_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_HmtsSnmpBroadcastDelay_Type.__name__=_C
_HmtsSnmpBroadcastDelay_Object=MibScalar
hmtsSnmpBroadcastDelay=_HmtsSnmpBroadcastDelay_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,4,2),_HmtsSnmpBroadcastDelay_Type())
hmtsSnmpBroadcastDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsSnmpBroadcastDelay.setStatus(_A)
if mibBuilder.loadTexts:hmtsSnmpBroadcastDelay.setUnits(_J)
_HmtsFwdPortTable_Object=MibTable
hmtsFwdPortTable=_HmtsFwdPortTable_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,5))
if mibBuilder.loadTexts:hmtsFwdPortTable.setStatus(_A)
_HmtsFwdPortEntry_Object=MibTableRow
hmtsFwdPortEntry=_HmtsFwdPortEntry_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,5,1))
hmtsFwdPortEntry.setIndexNames((0,_B,_n))
if mibBuilder.loadTexts:hmtsFwdPortEntry.setStatus(_A)
class _HmtsFwdPortId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_HmtsFwdPortId_Type.__name__=_G
_HmtsFwdPortId_Object=MibTableColumn
hmtsFwdPortId=_HmtsFwdPortId_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,5,1,1),_HmtsFwdPortId_Type())
hmtsFwdPortId.setMaxAccess(_H)
if mibBuilder.loadTexts:hmtsFwdPortId.setStatus(_A)
_HmtsFwdPortDescr_Type=DisplayString
_HmtsFwdPortDescr_Object=MibTableColumn
hmtsFwdPortDescr=_HmtsFwdPortDescr_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,5,1,2),_HmtsFwdPortDescr_Type())
hmtsFwdPortDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:hmtsFwdPortDescr.setStatus(_A)
class _HmtsFwdPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('rf',1),('rs485',2),('rs232',3),(_P,4)))
_HmtsFwdPortType_Type.__name__=_C
_HmtsFwdPortType_Object=MibTableColumn
hmtsFwdPortType=_HmtsFwdPortType_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,5,1,3),_HmtsFwdPortType_Type())
hmtsFwdPortType.setMaxAccess(_E)
if mibBuilder.loadTexts:hmtsFwdPortType.setStatus(_A)
class _HmtsFwdPortAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_o,1),('disableCarrierOn',2),('disableCarrierOff',3)))
_HmtsFwdPortAdminState_Type.__name__=_C
_HmtsFwdPortAdminState_Object=MibTableColumn
hmtsFwdPortAdminState=_HmtsFwdPortAdminState_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,5,1,4),_HmtsFwdPortAdminState_Type())
hmtsFwdPortAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsFwdPortAdminState.setStatus(_A)
class _HmtsFwdPortOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_O,1),(_p,2),(_q,3),(_r,4),(_s,5)))
_HmtsFwdPortOperState_Type.__name__=_C
_HmtsFwdPortOperState_Object=MibTableColumn
hmtsFwdPortOperState=_HmtsFwdPortOperState_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,5,1,5),_HmtsFwdPortOperState_Type())
hmtsFwdPortOperState.setMaxAccess(_E)
if mibBuilder.loadTexts:hmtsFwdPortOperState.setStatus(_A)
_HmtsFwdHmtsFrequency_Type=Integer32
_HmtsFwdHmtsFrequency_Object=MibTableColumn
hmtsFwdHmtsFrequency=_HmtsFwdHmtsFrequency_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,5,1,6),_HmtsFwdHmtsFrequency_Type())
hmtsFwdHmtsFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsFwdHmtsFrequency.setStatus(_A)
if mibBuilder.loadTexts:hmtsFwdHmtsFrequency.setUnits(_T)
_HmtsFwdXpndrFrequency_Type=Integer32
_HmtsFwdXpndrFrequency_Object=MibTableColumn
hmtsFwdXpndrFrequency=_HmtsFwdXpndrFrequency_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,5,1,7),_HmtsFwdXpndrFrequency_Type())
hmtsFwdXpndrFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsFwdXpndrFrequency.setStatus(_A)
if mibBuilder.loadTexts:hmtsFwdXpndrFrequency.setUnits(_T)
_HmtsFwdProvPwrLvl_Type=Integer32
_HmtsFwdProvPwrLvl_Object=MibTableColumn
hmtsFwdProvPwrLvl=_HmtsFwdProvPwrLvl_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,5,1,8),_HmtsFwdProvPwrLvl_Type())
hmtsFwdProvPwrLvl.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsFwdProvPwrLvl.setStatus(_A)
if mibBuilder.loadTexts:hmtsFwdProvPwrLvl.setUnits(_M)
_HmtsFwdMaxPwrLvl_Type=Integer32
_HmtsFwdMaxPwrLvl_Object=MibTableColumn
hmtsFwdMaxPwrLvl=_HmtsFwdMaxPwrLvl_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,5,1,9),_HmtsFwdMaxPwrLvl_Type())
hmtsFwdMaxPwrLvl.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsFwdMaxPwrLvl.setStatus(_A)
if mibBuilder.loadTexts:hmtsFwdMaxPwrLvl.setUnits(_M)
class _HmtsFwdPollTime_Type(Integer32):defaultValue=360
_HmtsFwdPollTime_Type.__name__=_C
_HmtsFwdPollTime_Object=MibTableColumn
hmtsFwdPollTime=_HmtsFwdPollTime_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,5,1,10),_HmtsFwdPollTime_Type())
hmtsFwdPollTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsFwdPollTime.setStatus(_A)
if mibBuilder.loadTexts:hmtsFwdPollTime.setUnits(_I)
_HmtsRevPortTable_Object=MibTable
hmtsRevPortTable=_HmtsRevPortTable_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,6))
if mibBuilder.loadTexts:hmtsRevPortTable.setStatus(_A)
_HmtsRevPortEntry_Object=MibTableRow
hmtsRevPortEntry=_HmtsRevPortEntry_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,6,1))
hmtsRevPortEntry.setIndexNames((0,_B,_t))
if mibBuilder.loadTexts:hmtsRevPortEntry.setStatus(_A)
class _HmtsRevPortId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_HmtsRevPortId_Type.__name__=_G
_HmtsRevPortId_Object=MibTableColumn
hmtsRevPortId=_HmtsRevPortId_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,6,1,1),_HmtsRevPortId_Type())
hmtsRevPortId.setMaxAccess(_H)
if mibBuilder.loadTexts:hmtsRevPortId.setStatus(_A)
class _HmtsRevFwdPortId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_HmtsRevFwdPortId_Type.__name__=_G
_HmtsRevFwdPortId_Object=MibTableColumn
hmtsRevFwdPortId=_HmtsRevFwdPortId_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,6,1,2),_HmtsRevFwdPortId_Type())
hmtsRevFwdPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsRevFwdPortId.setStatus(_A)
_HmtsRevPortDescr_Type=DisplayString
_HmtsRevPortDescr_Object=MibTableColumn
hmtsRevPortDescr=_HmtsRevPortDescr_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,6,1,3),_HmtsRevPortDescr_Type())
hmtsRevPortDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:hmtsRevPortDescr.setStatus(_A)
class _HmtsRevPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('rf',1),('rs485',2),('rs232',3),(_P,4)))
_HmtsRevPortType_Type.__name__=_C
_HmtsRevPortType_Object=MibTableColumn
hmtsRevPortType=_HmtsRevPortType_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,6,1,4),_HmtsRevPortType_Type())
hmtsRevPortType.setMaxAccess(_E)
if mibBuilder.loadTexts:hmtsRevPortType.setStatus(_A)
class _HmtsRevPortAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_o,1),('disable',2)))
_HmtsRevPortAdminState_Type.__name__=_C
_HmtsRevPortAdminState_Object=MibTableColumn
hmtsRevPortAdminState=_HmtsRevPortAdminState_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,6,1,5),_HmtsRevPortAdminState_Type())
hmtsRevPortAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsRevPortAdminState.setStatus(_A)
class _HmtsRevPortOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_O,1),(_p,2),(_q,3),(_r,4),(_s,5)))
_HmtsRevPortOperState_Type.__name__=_C
_HmtsRevPortOperState_Object=MibTableColumn
hmtsRevPortOperState=_HmtsRevPortOperState_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,6,1,6),_HmtsRevPortOperState_Type())
hmtsRevPortOperState.setMaxAccess(_E)
if mibBuilder.loadTexts:hmtsRevPortOperState.setStatus(_A)
_HmtsRevFrequency_Type=Integer32
_HmtsRevFrequency_Object=MibTableColumn
hmtsRevFrequency=_HmtsRevFrequency_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,6,1,7),_HmtsRevFrequency_Type())
hmtsRevFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsRevFrequency.setStatus(_A)
if mibBuilder.loadTexts:hmtsRevFrequency.setUnits(_T)
_HmtsRevMuteLvl_Type=Integer32
_HmtsRevMuteLvl_Object=MibTableColumn
hmtsRevMuteLvl=_HmtsRevMuteLvl_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,6,1,8),_HmtsRevMuteLvl_Type())
hmtsRevMuteLvl.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsRevMuteLvl.setStatus(_A)
if mibBuilder.loadTexts:hmtsRevMuteLvl.setUnits(_M)
_HmtsRevMulticastAddr_Type=MacAddress
_HmtsRevMulticastAddr_Object=MibTableColumn
hmtsRevMulticastAddr=_HmtsRevMulticastAddr_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,6,1,9),_HmtsRevMulticastAddr_Type())
hmtsRevMulticastAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsRevMulticastAddr.setStatus(_A)
_HmtsRevReturnLvl_Type=Integer32
_HmtsRevReturnLvl_Object=MibTableColumn
hmtsRevReturnLvl=_HmtsRevReturnLvl_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,6,1,10),_HmtsRevReturnLvl_Type())
hmtsRevReturnLvl.setMaxAccess(_E)
if mibBuilder.loadTexts:hmtsRevReturnLvl.setStatus(_A)
if mibBuilder.loadTexts:hmtsRevReturnLvl.setUnits(_M)
_HmtsRevCRCErrors_Type=Integer32
_HmtsRevCRCErrors_Object=MibTableColumn
hmtsRevCRCErrors=_HmtsRevCRCErrors_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,6,1,11),_HmtsRevCRCErrors_Type())
hmtsRevCRCErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsRevCRCErrors.setStatus(_A)
_HmtsRevFrameErrors_Type=Integer32
_HmtsRevFrameErrors_Object=MibTableColumn
hmtsRevFrameErrors=_HmtsRevFrameErrors_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,6,1,12),_HmtsRevFrameErrors_Type())
hmtsRevFrameErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsRevFrameErrors.setStatus(_A)
class _HmtsRevBackOffPeriod_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16383))
_HmtsRevBackOffPeriod_Type.__name__=_C
_HmtsRevBackOffPeriod_Object=MibTableColumn
hmtsRevBackOffPeriod=_HmtsRevBackOffPeriod_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,6,1,13),_HmtsRevBackOffPeriod_Type())
hmtsRevBackOffPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsRevBackOffPeriod.setStatus(_A)
if mibBuilder.loadTexts:hmtsRevBackOffPeriod.setUnits(_J)
class _HmtsRevACKTimeout_Type(Integer32):defaultValue=19;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HmtsRevACKTimeout_Type.__name__=_C
_HmtsRevACKTimeout_Object=MibTableColumn
hmtsRevACKTimeout=_HmtsRevACKTimeout_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,6,1,14),_HmtsRevACKTimeout_Type())
hmtsRevACKTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsRevACKTimeout.setStatus(_A)
if mibBuilder.loadTexts:hmtsRevACKTimeout.setUnits(_J)
class _HmtsRevMaxMACRetries_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HmtsRevMaxMACRetries_Type.__name__=_C
_HmtsRevMaxMACRetries_Object=MibTableColumn
hmtsRevMaxMACRetries=_HmtsRevMaxMACRetries_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,6,1,15),_HmtsRevMaxMACRetries_Type())
hmtsRevMaxMACRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsRevMaxMACRetries.setStatus(_A)
class _HmtsRevBackOffMinExp_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_HmtsRevBackOffMinExp_Type.__name__=_C
_HmtsRevBackOffMinExp_Object=MibTableColumn
hmtsRevBackOffMinExp=_HmtsRevBackOffMinExp_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,6,1,16),_HmtsRevBackOffMinExp_Type())
hmtsRevBackOffMinExp.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsRevBackOffMinExp.setStatus(_A)
class _HmtsRevBackOffMaxExp_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_HmtsRevBackOffMaxExp_Type.__name__=_C
_HmtsRevBackOffMaxExp_Object=MibTableColumn
hmtsRevBackOffMaxExp=_HmtsRevBackOffMaxExp_Object((1,3,6,1,4,1,5591,1,11,3,2,1,2,6,1,17),_HmtsRevBackOffMaxExp_Type())
hmtsRevBackOffMaxExp.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsRevBackOffMaxExp.setStatus(_A)
_HmtsDeviceGroup_ObjectIdentity=ObjectIdentity
hmtsDeviceGroup=_HmtsDeviceGroup_ObjectIdentity((1,3,6,1,4,1,5591,1,11,3,2,1,3))
_HmtsDev_Type=Integer32
_HmtsDev_Object=MibScalar
hmtsDev=_HmtsDev_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,1),_HmtsDev_Type())
hmtsDev.setMaxAccess(_E)
if mibBuilder.loadTexts:hmtsDev.setStatus(_A)
_HmtsDevInErr_Type=Integer32
_HmtsDevInErr_Object=MibScalar
hmtsDevInErr=_HmtsDevInErr_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,2),_HmtsDevInErr_Type())
hmtsDevInErr.setMaxAccess(_E)
if mibBuilder.loadTexts:hmtsDevInErr.setStatus(_A)
class _HmtsDefaultCommString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HmtsDefaultCommString_Type.__name__=_G
_HmtsDefaultCommString_Object=MibScalar
hmtsDefaultCommString=_HmtsDefaultCommString_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,3),_HmtsDefaultCommString_Type())
hmtsDefaultCommString.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsDefaultCommString.setStatus(_A)
_HmtsComStatAlarm_Type=HmtsComStatCodes
_HmtsComStatAlarm_Object=MibScalar
hmtsComStatAlarm=_HmtsComStatAlarm_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,4),_HmtsComStatAlarm_Type())
hmtsComStatAlarm.setMaxAccess(_H)
if mibBuilder.loadTexts:hmtsComStatAlarm.setStatus(_A)
_HmtsContNRespCount_Type=Integer32
_HmtsContNRespCount_Object=MibScalar
hmtsContNRespCount=_HmtsContNRespCount_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,5),_HmtsContNRespCount_Type())
hmtsContNRespCount.setMaxAccess(_H)
if mibBuilder.loadTexts:hmtsContNRespCount.setStatus(_A)
_HmtsDevTable_Object=MibTable
hmtsDevTable=_HmtsDevTable_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,6))
if mibBuilder.loadTexts:hmtsDevTable.setStatus(_A)
_HmtsDevEntry_Object=MibTableRow
hmtsDevEntry=_HmtsDevEntry_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,6,1))
hmtsDevEntry.setIndexNames((0,_B,_u))
if mibBuilder.loadTexts:hmtsDevEntry.setStatus(_A)
_HmtsDevPhysAddr_Type=MacAddress
_HmtsDevPhysAddr_Object=MibTableColumn
hmtsDevPhysAddr=_HmtsDevPhysAddr_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,6,1,1),_HmtsDevPhysAddr_Type())
hmtsDevPhysAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:hmtsDevPhysAddr.setStatus(_A)
_HmtsDevIPAddr_Type=IpAddress
_HmtsDevIPAddr_Object=MibTableColumn
hmtsDevIPAddr=_HmtsDevIPAddr_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,6,1,2),_HmtsDevIPAddr_Type())
hmtsDevIPAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:hmtsDevIPAddr.setStatus(_A)
class _HmtsDevCommString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HmtsDevCommString_Type.__name__=_G
_HmtsDevCommString_Object=MibTableColumn
hmtsDevCommString=_HmtsDevCommString_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,6,1,3),_HmtsDevCommString_Type())
hmtsDevCommString.setMaxAccess(_F)
if mibBuilder.loadTexts:hmtsDevCommString.setStatus(_A)
class _HmtsDevFwdPortId_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HmtsDevFwdPortId_Type.__name__=_G
_HmtsDevFwdPortId_Object=MibTableColumn
hmtsDevFwdPortId=_HmtsDevFwdPortId_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,6,1,4),_HmtsDevFwdPortId_Type())
hmtsDevFwdPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:hmtsDevFwdPortId.setStatus(_A)
class _HmtsDevRevPortId_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HmtsDevRevPortId_Type.__name__=_G
_HmtsDevRevPortId_Object=MibTableColumn
hmtsDevRevPortId=_HmtsDevRevPortId_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,6,1,5),_HmtsDevRevPortId_Type())
hmtsDevRevPortId.setMaxAccess(_F)
if mibBuilder.loadTexts:hmtsDevRevPortId.setStatus(_A)
_HmtsDevComStat_Type=HmtsComStatCodes
_HmtsDevComStat_Object=MibTableColumn
hmtsDevComStat=_HmtsDevComStat_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,6,1,6),_HmtsDevComStat_Type())
hmtsDevComStat.setMaxAccess(_E)
if mibBuilder.loadTexts:hmtsDevComStat.setStatus(_A)
_HmtsDevReturnLvl_Type=Integer32
_HmtsDevReturnLvl_Object=MibTableColumn
hmtsDevReturnLvl=_HmtsDevReturnLvl_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,6,1,7),_HmtsDevReturnLvl_Type())
hmtsDevReturnLvl.setMaxAccess(_E)
if mibBuilder.loadTexts:hmtsDevReturnLvl.setStatus(_A)
if mibBuilder.loadTexts:hmtsDevReturnLvl.setUnits(_M)
_HmtsDevLastStateChg_Type=Unsigned32
_HmtsDevLastStateChg_Object=MibTableColumn
hmtsDevLastStateChg=_HmtsDevLastStateChg_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,6,1,8),_HmtsDevLastStateChg_Type())
hmtsDevLastStateChg.setMaxAccess(_E)
if mibBuilder.loadTexts:hmtsDevLastStateChg.setStatus(_A)
_HmtsDevLastRespTime_Type=Unsigned32
_HmtsDevLastRespTime_Object=MibTableColumn
hmtsDevLastRespTime=_HmtsDevLastRespTime_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,6,1,9),_HmtsDevLastRespTime_Type())
hmtsDevLastRespTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hmtsDevLastRespTime.setStatus(_A)
_HmtsDevRqstCount_Type=Integer32
_HmtsDevRqstCount_Object=MibTableColumn
hmtsDevRqstCount=_HmtsDevRqstCount_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,6,1,10),_HmtsDevRqstCount_Type())
hmtsDevRqstCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hmtsDevRqstCount.setStatus(_A)
_HmtsDevRespTimeoutCount_Type=Integer32
_HmtsDevRespTimeoutCount_Object=MibTableColumn
hmtsDevRespTimeoutCount=_HmtsDevRespTimeoutCount_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,6,1,11),_HmtsDevRespTimeoutCount_Type())
hmtsDevRespTimeoutCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hmtsDevRespTimeoutCount.setStatus(_A)
_HmtsDevContNRespCount_Type=Integer32
_HmtsDevContNRespCount_Object=MibTableColumn
hmtsDevContNRespCount=_HmtsDevContNRespCount_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,6,1,12),_HmtsDevContNRespCount_Type())
hmtsDevContNRespCount.setMaxAccess(_E)
if mibBuilder.loadTexts:hmtsDevContNRespCount.setStatus(_A)
class _HmtsDevRegStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('registered',1),(_j,2),('notRegistered',3)))
_HmtsDevRegStatus_Type.__name__=_C
_HmtsDevRegStatus_Object=MibTableColumn
hmtsDevRegStatus=_HmtsDevRegStatus_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,6,1,13),_HmtsDevRegStatus_Type())
hmtsDevRegStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hmtsDevRegStatus.setStatus(_A)
_HmtsDevRegTime_Type=Unsigned32
_HmtsDevRegTime_Object=MibTableColumn
hmtsDevRegTime=_HmtsDevRegTime_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,6,1,14),_HmtsDevRegTime_Type())
hmtsDevRegTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hmtsDevRegTime.setStatus(_A)
_HmtsDevRowStatus_Type=RowStatus
_HmtsDevRowStatus_Object=MibTableColumn
hmtsDevRowStatus=_HmtsDevRowStatus_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,6,1,15),_HmtsDevRowStatus_Type())
hmtsDevRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hmtsDevRowStatus.setStatus(_A)
_HmtsComFaultTable_Object=MibTable
hmtsComFaultTable=_HmtsComFaultTable_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,7))
if mibBuilder.loadTexts:hmtsComFaultTable.setStatus(_A)
_HmtsComFaultEntry_Object=MibTableRow
hmtsComFaultEntry=_HmtsComFaultEntry_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,7,1))
hmtsComFaultEntry.setIndexNames((0,_B,_v))
if mibBuilder.loadTexts:hmtsComFaultEntry.setStatus(_A)
_HmtsComStatPhysAddr_Type=MacAddress
_HmtsComStatPhysAddr_Object=MibTableColumn
hmtsComStatPhysAddr=_HmtsComStatPhysAddr_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,7,1,1),_HmtsComStatPhysAddr_Type())
hmtsComStatPhysAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:hmtsComStatPhysAddr.setStatus(_A)
_HmtsComStat_Type=HmtsComStatCodes
_HmtsComStat_Object=MibTableColumn
hmtsComStat=_HmtsComStat_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,7,1,2),_HmtsComStat_Type())
hmtsComStat.setMaxAccess(_E)
if mibBuilder.loadTexts:hmtsComStat.setStatus(_A)
_HmtsMulticastAddrTable_Object=MibTable
hmtsMulticastAddrTable=_HmtsMulticastAddrTable_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,8))
if mibBuilder.loadTexts:hmtsMulticastAddrTable.setStatus(_A)
_HmtsMulticastAddrEntry_Object=MibTableRow
hmtsMulticastAddrEntry=_HmtsMulticastAddrEntry_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,8,1))
hmtsMulticastAddrEntry.setIndexNames((0,_B,_w))
if mibBuilder.loadTexts:hmtsMulticastAddrEntry.setStatus(_A)
_HmtsMulticastPhysAddr_Type=MacAddress
_HmtsMulticastPhysAddr_Object=MibTableColumn
hmtsMulticastPhysAddr=_HmtsMulticastPhysAddr_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,8,1,1),_HmtsMulticastPhysAddr_Type())
hmtsMulticastPhysAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:hmtsMulticastPhysAddr.setStatus(_A)
_HmtsMulticastIPAddr_Type=IpAddress
_HmtsMulticastIPAddr_Object=MibTableColumn
hmtsMulticastIPAddr=_HmtsMulticastIPAddr_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,8,1,2),_HmtsMulticastIPAddr_Type())
hmtsMulticastIPAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:hmtsMulticastIPAddr.setStatus(_A)
class _HmtsMulticastCommString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HmtsMulticastCommString_Type.__name__=_G
_HmtsMulticastCommString_Object=MibTableColumn
hmtsMulticastCommString=_HmtsMulticastCommString_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,8,1,3),_HmtsMulticastCommString_Type())
hmtsMulticastCommString.setMaxAccess(_F)
if mibBuilder.loadTexts:hmtsMulticastCommString.setStatus(_A)
_HmtsMulticastRowStatus_Type=RowStatus
_HmtsMulticastRowStatus_Object=MibTableColumn
hmtsMulticastRowStatus=_HmtsMulticastRowStatus_Object((1,3,6,1,4,1,5591,1,11,3,2,1,3,8,1,4),_HmtsMulticastRowStatus_Type())
hmtsMulticastRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hmtsMulticastRowStatus.setStatus(_A)
_HmtsIPGroup_ObjectIdentity=ObjectIdentity
hmtsIPGroup=_HmtsIPGroup_ObjectIdentity((1,3,6,1,4,1,5591,1,11,3,2,1,4))
class _HmtsIPManagementMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('client',1),('manualXp',2),('manualHmts',3),(_Q,4)))
_HmtsIPManagementMethod_Type.__name__=_C
_HmtsIPManagementMethod_Object=MibScalar
hmtsIPManagementMethod=_HmtsIPManagementMethod_Object((1,3,6,1,4,1,5591,1,11,3,2,1,4,1),_HmtsIPManagementMethod_Type())
hmtsIPManagementMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsIPManagementMethod.setStatus(_A)
_HmtsIPDevTable_Object=MibTable
hmtsIPDevTable=_HmtsIPDevTable_Object((1,3,6,1,4,1,5591,1,11,3,2,1,4,2))
if mibBuilder.loadTexts:hmtsIPDevTable.setStatus(_A)
_HmtsIPDevEntry_Object=MibTableRow
hmtsIPDevEntry=_HmtsIPDevEntry_Object((1,3,6,1,4,1,5591,1,11,3,2,1,4,2,1))
hmtsIPDevEntry.setIndexNames((0,_B,_x))
if mibBuilder.loadTexts:hmtsIPDevEntry.setStatus(_A)
_HmtsIPDevAddr_Type=IpAddress
_HmtsIPDevAddr_Object=MibTableColumn
hmtsIPDevAddr=_HmtsIPDevAddr_Object((1,3,6,1,4,1,5591,1,11,3,2,1,4,2,1,1),_HmtsIPDevAddr_Type())
hmtsIPDevAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:hmtsIPDevAddr.setStatus(_A)
_HmtsIPPhysAddr_Type=MacAddress
_HmtsIPPhysAddr_Object=MibTableColumn
hmtsIPPhysAddr=_HmtsIPPhysAddr_Object((1,3,6,1,4,1,5591,1,11,3,2,1,4,2,1,2),_HmtsIPPhysAddr_Type())
hmtsIPPhysAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:hmtsIPPhysAddr.setStatus(_A)
_HmtsNetAddrTable_Object=MibTable
hmtsNetAddrTable=_HmtsNetAddrTable_Object((1,3,6,1,4,1,5591,1,11,3,2,1,4,3))
if mibBuilder.loadTexts:hmtsNetAddrTable.setStatus(_A)
_HmtsNetAddrEntry_Object=MibTableRow
hmtsNetAddrEntry=_HmtsNetAddrEntry_Object((1,3,6,1,4,1,5591,1,11,3,2,1,4,3,1))
hmtsNetAddrEntry.setIndexNames((0,_B,_y))
if mibBuilder.loadTexts:hmtsNetAddrEntry.setStatus(_A)
_HmtsNetStartAddr_Type=IpAddress
_HmtsNetStartAddr_Object=MibTableColumn
hmtsNetStartAddr=_HmtsNetStartAddr_Object((1,3,6,1,4,1,5591,1,11,3,2,1,4,3,1,1),_HmtsNetStartAddr_Type())
hmtsNetStartAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:hmtsNetStartAddr.setStatus(_A)
_HmtsNetEndAddr_Type=IpAddress
_HmtsNetEndAddr_Object=MibTableColumn
hmtsNetEndAddr=_HmtsNetEndAddr_Object((1,3,6,1,4,1,5591,1,11,3,2,1,4,3,1,2),_HmtsNetEndAddr_Type())
hmtsNetEndAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:hmtsNetEndAddr.setStatus(_A)
_HmtsNetMask_Type=IpAddress
_HmtsNetMask_Object=MibTableColumn
hmtsNetMask=_HmtsNetMask_Object((1,3,6,1,4,1,5591,1,11,3,2,1,4,3,1,3),_HmtsNetMask_Type())
hmtsNetMask.setMaxAccess(_F)
if mibBuilder.loadTexts:hmtsNetMask.setStatus(_A)
_HmtsNetRowStatus_Type=RowStatus
_HmtsNetRowStatus_Object=MibTableColumn
hmtsNetRowStatus=_HmtsNetRowStatus_Object((1,3,6,1,4,1,5591,1,11,3,2,1,4,3,1,4),_HmtsNetRowStatus_Type())
hmtsNetRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hmtsNetRowStatus.setStatus(_A)
_HmtsCommGroup_ObjectIdentity=ObjectIdentity
hmtsCommGroup=_HmtsCommGroup_ObjectIdentity((1,3,6,1,4,1,5591,1,11,3,2,1,5))
class _HmtsCommManagementMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_k,2)))
_HmtsCommManagementMethod_Type.__name__=_C
_HmtsCommManagementMethod_Object=MibScalar
hmtsCommManagementMethod=_HmtsCommManagementMethod_Object((1,3,6,1,4,1,5591,1,11,3,2,1,5,1),_HmtsCommManagementMethod_Type())
hmtsCommManagementMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:hmtsCommManagementMethod.setStatus(_A)
_HmtsCommDevTable_Object=MibTable
hmtsCommDevTable=_HmtsCommDevTable_Object((1,3,6,1,4,1,5591,1,11,3,2,1,5,2))
if mibBuilder.loadTexts:hmtsCommDevTable.setStatus(_A)
_HmtsCommDevEntry_Object=MibTableRow
hmtsCommDevEntry=_HmtsCommDevEntry_Object((1,3,6,1,4,1,5591,1,11,3,2,1,5,2,1))
hmtsCommDevEntry.setIndexNames((0,_B,_z))
if mibBuilder.loadTexts:hmtsCommDevEntry.setStatus(_A)
class _HmtsCommString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HmtsCommString_Type.__name__=_G
_HmtsCommString_Object=MibTableColumn
hmtsCommString=_HmtsCommString_Object((1,3,6,1,4,1,5591,1,11,3,2,1,5,2,1,1),_HmtsCommString_Type())
hmtsCommString.setMaxAccess(_H)
if mibBuilder.loadTexts:hmtsCommString.setStatus(_A)
_HmtsCommPhysAddr_Type=MacAddress
_HmtsCommPhysAddr_Object=MibTableColumn
hmtsCommPhysAddr=_HmtsCommPhysAddr_Object((1,3,6,1,4,1,5591,1,11,3,2,1,5,2,1,2),_HmtsCommPhysAddr_Type())
hmtsCommPhysAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:hmtsCommPhysAddr.setStatus(_A)
_HeHMTSConformance_ObjectIdentity=ObjectIdentity
heHMTSConformance=_HeHMTSConformance_ObjectIdentity((1,3,6,1,4,1,5591,1,11,3,2,2))
_HmtsCompliances_ObjectIdentity=ObjectIdentity
hmtsCompliances=_HmtsCompliances_ObjectIdentity((1,3,6,1,4,1,5591,1,11,3,2,2,1))
_HmtsGroups_ObjectIdentity=ObjectIdentity
hmtsGroups=_HmtsGroups_ObjectIdentity((1,3,6,1,4,1,5591,1,11,3,2,2,2))
hmtsReqManagementGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,3,2,2,2,1))
hmtsReqManagementGroup.setObjects(*((_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:hmtsReqManagementGroup.setStatus(_A)
hmtsReqDeviceGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,3,2,2,2,2))
hmtsReqDeviceGroup.setObjects(*((_B,'hmtsDev'),(_B,_AF),(_B,_U),(_B,_V),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU)))
if mibBuilder.loadTexts:hmtsReqDeviceGroup.setStatus(_A)
hmtsIPDeviceGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,3,2,2,2,3))
hmtsIPDeviceGroup.setObjects(*((_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa)))
if mibBuilder.loadTexts:hmtsIPDeviceGroup.setStatus(_A)
hmtsCommDeviceGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,3,2,2,2,4))
hmtsCommDeviceGroup.setObjects(*((_B,_U),(_B,_Ab),(_B,_Ac),(_B,_Ad)))
if mibBuilder.loadTexts:hmtsCommDeviceGroup.setStatus(_A)
hmtsInformationGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,3,2,2,2,5))
hmtsInformationGroup.setObjects(*((_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am)))
if mibBuilder.loadTexts:hmtsInformationGroup.setStatus(_A)
hmtsMacProtocolInformationGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,3,2,2,2,6))
hmtsMacProtocolInformationGroup.setObjects(*((_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At)))
if mibBuilder.loadTexts:hmtsMacProtocolInformationGroup.setStatus(_A)
hmtsSnmpProtocolInformationGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,3,2,2,2,7))
hmtsSnmpProtocolInformationGroup.setObjects(*((_B,_Au),(_B,_Av)))
if mibBuilder.loadTexts:hmtsSnmpProtocolInformationGroup.setStatus(_A)
hmtsExtendedRegistrationGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,3,2,2,2,8))
hmtsExtendedRegistrationGroup.setObjects(*((_B,_Aw),(_B,_Ax)))
if mibBuilder.loadTexts:hmtsExtendedRegistrationGroup.setStatus(_A)
hmtsTrapControlGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,3,2,2,2,9))
hmtsTrapControlGroup.setObjects(*((_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1),(_B,_B2)))
if mibBuilder.loadTexts:hmtsTrapControlGroup.setStatus(_A)
hmtsExtendedTrapControlGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,3,2,2,2,10))
hmtsExtendedTrapControlGroup.setObjects((_B,_B3))
if mibBuilder.loadTexts:hmtsExtendedTrapControlGroup.setStatus(_A)
hmtsExtendedFwdPortGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,3,2,2,2,11))
hmtsExtendedFwdPortGroup.setObjects(*((_B,_B4),(_B,_B5),(_B,_B6)))
if mibBuilder.loadTexts:hmtsExtendedFwdPortGroup.setStatus(_A)
hmtsExtendedRevPortGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,3,2,2,2,12))
hmtsExtendedRevPortGroup.setObjects(*((_B,_B7),(_B,_B8),(_B,_B9),(_B,_BA),(_B,_BB),(_B,_BC),(_B,_BD),(_B,_BE),(_B,_BF)))
if mibBuilder.loadTexts:hmtsExtendedRevPortGroup.setStatus(_A)
hmtsEventGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,3,2,2,2,13))
hmtsEventGroup.setObjects((_B,_BG))
if mibBuilder.loadTexts:hmtsEventGroup.setStatus(_A)
hmtsRegistrationFailedEvent=NotificationType((1,3,6,1,4,1,5591,1,11,3,2,1,0,1))
hmtsRegistrationFailedEvent.setObjects((_B,_V))
if mibBuilder.loadTexts:hmtsRegistrationFailedEvent.setStatus(_A)
heHMTSCompliance=ModuleCompliance((1,3,6,1,4,1,5591,1,11,3,2,2,1,1))
heHMTSCompliance.setObjects(*((_B,_BH),(_B,_BI),(_B,_BJ),(_B,_BK),(_B,_BL),(_B,_BM),(_B,_BN),(_B,_BO),(_B,_BP),(_B,_BQ),(_B,_BR),(_B,_BS),(_B,_BT),(_K,'heCommonTime'),(_K,'heCommonAlarmDetectionControl'),(_K,'heCommonParamsGroup'),(_K,_a),(_K,_b),(_L,_Z),(_L,_Y),(_L,_W),(_L,_X),(_f,_g),('SNMP-NOTIFICATION-MIB','snmpNotifyGroup'),(_h,_i),(_N,_c),(_N,_e),(_N,_d)))
if mibBuilder.loadTexts:heHMTSCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'HmtsComStatCodes':HmtsComStatCodes,'heHMTSMIB':heHMTSMIB,'heHMTSObjects':heHMTSObjects,'hmtsNotifications':hmtsNotifications,_BG:hmtsRegistrationFailedEvent,'hmtsInfoGroup':hmtsInfoGroup,_Ae:hmtsAdminState,_Af:hmtsOperState,_Ag:hmtsProxyType,_Ah:hmtsFreqSwitchMethod,_Ai:hmtsModel,_Aj:hmtsSerialNumber,_Ak:hmtsSoftwareVersion,_Al:hmtsTimeServerAddress,_Am:hmtsTimeServerSyncInterval,'hmtsManagementGroup':hmtsManagementGroup,'hmtsMacPduGroup':hmtsMacPduGroup,_An:hmtsMacPduTimeout,_Ao:hmtsTalkPduTimeout,_Ap:hmtsMacBroadcastDelay,_Aq:hmtsAlarmDiscoveryMode,_Ar:hmtsChnldescPduInt,_As:hmtsTimePduInt,_At:hmtsDeviceAccessMode,'hmtsRegistrationGroup':hmtsRegistrationGroup,_A0:hmtsRegInterval,_Aw:hmtsRegMinDuration,_Ax:hmtsRegMaxDuration,_A1:hmtsRegContinuity,'hmtsSnmpTrapControlGroup':hmtsSnmpTrapControlGroup,'hmtsTrapControlTable':hmtsTrapControlTable,'hmtsTrapControlEntry':hmtsTrapControlEntry,_m:hmtsTControlId,_Ay:hmtsTControlInterval,_A_:hmtsTControlChainId,_Az:hmtsTControlMinDuration,_B3:hmtsTControlMaxDuration,_B0:hmtsTControlContinuity,_B2:hmtsTControlMulticastAddr,_B1:hmtsTControlRowStatus,'hmtsSnmpProtocolGroup':hmtsSnmpProtocolGroup,_Au:hmtsSnmpTimeout,_Av:hmtsSnmpBroadcastDelay,'hmtsFwdPortTable':hmtsFwdPortTable,'hmtsFwdPortEntry':hmtsFwdPortEntry,_n:hmtsFwdPortId,_A3:hmtsFwdPortDescr,_A5:hmtsFwdPortType,_A2:hmtsFwdPortAdminState,_A4:hmtsFwdPortOperState,_A6:hmtsFwdHmtsFrequency,_A7:hmtsFwdXpndrFrequency,_B4:hmtsFwdProvPwrLvl,_B5:hmtsFwdMaxPwrLvl,_B6:hmtsFwdPollTime,'hmtsRevPortTable':hmtsRevPortTable,'hmtsRevPortEntry':hmtsRevPortEntry,_t:hmtsRevPortId,_A9:hmtsRevFwdPortId,_AA:hmtsRevPortDescr,_AB:hmtsRevPortType,_A8:hmtsRevPortAdminState,_AD:hmtsRevPortOperState,_AC:hmtsRevFrequency,_B7:hmtsRevMuteLvl,_B8:hmtsRevMulticastAddr,_AE:hmtsRevReturnLvl,_BA:hmtsRevCRCErrors,_B9:hmtsRevFrameErrors,_BB:hmtsRevBackOffPeriod,_BC:hmtsRevACKTimeout,_BD:hmtsRevMaxMACRetries,_BE:hmtsRevBackOffMinExp,_BF:hmtsRevBackOffMaxExp,'hmtsDeviceGroup':hmtsDeviceGroup,'hmtsDev':hmtsDev,_AF:hmtsDevInErr,_U:hmtsDefaultCommString,'hmtsComStatAlarm':hmtsComStatAlarm,'hmtsContNRespCount':hmtsContNRespCount,'hmtsDevTable':hmtsDevTable,'hmtsDevEntry':hmtsDevEntry,_u:hmtsDevPhysAddr,_AG:hmtsDevIPAddr,_AH:hmtsDevCommString,_AI:hmtsDevFwdPortId,_AJ:hmtsDevRevPortId,_V:hmtsDevComStat,_AK:hmtsDevReturnLvl,_AL:hmtsDevLastStateChg,_AM:hmtsDevLastRespTime,_AN:hmtsDevRqstCount,_AO:hmtsDevRespTimeoutCount,_AP:hmtsDevContNRespCount,_AQ:hmtsDevRegStatus,_AR:hmtsDevRegTime,_AS:hmtsDevRowStatus,'hmtsComFaultTable':hmtsComFaultTable,'hmtsComFaultEntry':hmtsComFaultEntry,_v:hmtsComStatPhysAddr,_AT:hmtsComStat,'hmtsMulticastAddrTable':hmtsMulticastAddrTable,'hmtsMulticastAddrEntry':hmtsMulticastAddrEntry,_w:hmtsMulticastPhysAddr,_AV:hmtsMulticastIPAddr,_Ab:hmtsMulticastCommString,_AU:hmtsMulticastRowStatus,'hmtsIPGroup':hmtsIPGroup,_AW:hmtsIPManagementMethod,'hmtsIPDevTable':hmtsIPDevTable,'hmtsIPDevEntry':hmtsIPDevEntry,_x:hmtsIPDevAddr,_AX:hmtsIPPhysAddr,'hmtsNetAddrTable':hmtsNetAddrTable,'hmtsNetAddrEntry':hmtsNetAddrEntry,_y:hmtsNetStartAddr,_AY:hmtsNetEndAddr,_AZ:hmtsNetMask,_Aa:hmtsNetRowStatus,'hmtsCommGroup':hmtsCommGroup,_Ac:hmtsCommManagementMethod,'hmtsCommDevTable':hmtsCommDevTable,'hmtsCommDevEntry':hmtsCommDevEntry,_z:hmtsCommString,_Ad:hmtsCommPhysAddr,'heHMTSConformance':heHMTSConformance,'hmtsCompliances':hmtsCompliances,'heHMTSCompliance':heHMTSCompliance,'hmtsGroups':hmtsGroups,_BK:hmtsReqManagementGroup,_BL:hmtsReqDeviceGroup,_BN:hmtsIPDeviceGroup,_BO:hmtsCommDeviceGroup,_BH:hmtsInformationGroup,_BI:hmtsMacProtocolInformationGroup,_BJ:hmtsSnmpProtocolInformationGroup,_BP:hmtsExtendedRegistrationGroup,_BQ:hmtsTrapControlGroup,_BR:hmtsExtendedTrapControlGroup,_BS:hmtsExtendedFwdPortGroup,_BT:hmtsExtendedRevPortGroup,_BM:hmtsEventGroup})