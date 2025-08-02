_AL='hm2DiagEgressIfaceUtilizationAlarmCondition'
_AK='hm2DiagEgressIfaceUtilization'
_AJ='hm2PortMonitorConditionField'
_AI='hm2DiagIfaceUtilizationAlarmCondition'
_AH='hm2DiagIfaceUtilization'
_AG='hm2DevSecTrapCauseIndex'
_AF='hm2DevSecTrapCause'
_AE='hm2DevSecOperState'
_AD='hm2DevMonTrapCauseIndex'
_AC='hm2DevMonTrapCause'
_AB='hm2DevMonOperState'
_AA='hm2SigConTrapCauseIndex'
_A9='hm2SigConTrapCause'
_A8='hm2SigConOperState'
_A7='hm2DiagCableTesterCablePair'
_A6='hm2LedGlobalLedType'
_A5='hm2DevSecStatusIndex'
_A4='hm2DevMonStatusIndex'
_A3='hm2DevMonFanModID'
_A2='hm2DevMonModID'
_A1='hm2SigConStatusIndex'
_A0='hm2SigConFanModID'
_z='hm2SigConModID'
_y='ethernet-loops'
_x='hm2IfacePhysIndex'
_w='HM2-DEVMGMT-MIB'
_v='iec61850-mms-enabled'
_u='open'
_t='pml-disabled'
_s='hm2DiagSelftestActionCause'
_r='Bits'
_q='hm2PSID'
_p='HM2-PWRMGMT-MIB'
_o='stp-port-blocked'
_n='humidity'
_m='profinet-io-enabled'
_l='ethernet-ip-enabled'
_k='modbus-tcp-enabled'
_j='https-certificate-warning'
_i='ext-nvm-config-load-unsecure'
_h='hidisc-enabled'
_g='no-link'
_f='ext-nvm-update-enabled'
_e='sysmon-enabled'
_d='snmp-unsecure'
_c='http-enabled'
_b='telnet-enabled'
_a='password-policy-inactive'
_Z='password-policy-not-configured'
_Y='password-min-length'
_X='password-change'
_W='ring-redundancy'
_V='ext-nvm-not-in-sync'
_U='ext-nvm-removal'
_T='module-removal'
_S='fan-failure'
_R='temperature'
_Q='link-failure'
_P='power-supply'
_O='not-accessible'
_N='Unsigned32'
_M='none'
_L='kBytes'
_K='hm2DevMonID'
_J='hm2SigConID'
_I='TruthValue'
_H='ifIndex'
_G='IF-MIB'
_F='HM2-DIAGNOSTIC-MIB'
_E='HmEnabledStatus'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hm2IfacePhysIndex,=mibBuilder.importSymbols(_w,_x)
hm2PSID,=mibBuilder.importSymbols(_p,_q)
HmEnabledStatus,HmTimeSeconds1970,hm2ConfigurationMibs=mibBuilder.importSymbols('HM2-TC-MIB',_E,'HmTimeSeconds1970','hm2ConfigurationMibs')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_r,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_I)
hm2DiagnosticMib=ModuleIdentity((1,3,6,1,4,1,248,11,22))
if mibBuilder.loadTexts:hm2DiagnosticMib.setRevisions(('2012-08-28 00:00','2011-03-16 00:00'))
class Hm2LedType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('power',1),('status',2),('rm',3),('envm',4),('i1',5),('i2',6)))
class Hm2LedStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('off',1),('greenSolid',2),('greenBlink1',3),('greenBlink3',4),('greenBlink4',5),('greenBlink5',6),('greenBlink5i',7),('yellowSolid',8),('yellowBlink1',9),('yellowBlink3',10),('yellowBlink4',11),('yellowBlink5',12),('redSolid',13),('redBlink1',14),('redBlink3',15),('redBlink4',16),('redBlink5',17)))
_Hm2DiagnosticMibNotifications_ObjectIdentity=ObjectIdentity
hm2DiagnosticMibNotifications=_Hm2DiagnosticMibNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,22,0))
_Hm2DiagnosticMibObjects_ObjectIdentity=ObjectIdentity
hm2DiagnosticMibObjects=_Hm2DiagnosticMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,22,1))
_Hm2DiagSelftestGroup_ObjectIdentity=ObjectIdentity
hm2DiagSelftestGroup=_Hm2DiagSelftestGroup_ObjectIdentity((1,3,6,1,4,1,248,11,22,1,1))
class _Hm2DiagSelftestRAM_Type(HmEnabledStatus):defaultValue=1
_Hm2DiagSelftestRAM_Type.__name__=_E
_Hm2DiagSelftestRAM_Object=MibScalar
hm2DiagSelftestRAM=_Hm2DiagSelftestRAM_Object((1,3,6,1,4,1,248,11,22,1,1,1),_Hm2DiagSelftestRAM_Type())
hm2DiagSelftestRAM.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DiagSelftestRAM.setStatus(_A)
_Hm2DiagSelftestBootTime_Type=Integer32
_Hm2DiagSelftestBootTime_Object=MibScalar
hm2DiagSelftestBootTime=_Hm2DiagSelftestBootTime_Object((1,3,6,1,4,1,248,11,22,1,1,2),_Hm2DiagSelftestBootTime_Type())
hm2DiagSelftestBootTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DiagSelftestBootTime.setStatus(_A)
_Hm2DiagSelftestActionTable_Object=MibTable
hm2DiagSelftestActionTable=_Hm2DiagSelftestActionTable_Object((1,3,6,1,4,1,248,11,22,1,1,10))
if mibBuilder.loadTexts:hm2DiagSelftestActionTable.setStatus(_A)
_Hm2DiagSelftestActionEntry_Object=MibTableRow
hm2DiagSelftestActionEntry=_Hm2DiagSelftestActionEntry_Object((1,3,6,1,4,1,248,11,22,1,1,10,1))
hm2DiagSelftestActionEntry.setIndexNames((0,_F,_s))
if mibBuilder.loadTexts:hm2DiagSelftestActionEntry.setStatus(_A)
class _Hm2DiagSelftestActionCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('task',1),('resource',2),('software',3),('hardware',4)))
_Hm2DiagSelftestActionCause_Type.__name__=_D
_Hm2DiagSelftestActionCause_Object=MibTableColumn
hm2DiagSelftestActionCause=_Hm2DiagSelftestActionCause_Object((1,3,6,1,4,1,248,11,22,1,1,10,1,1),_Hm2DiagSelftestActionCause_Type())
hm2DiagSelftestActionCause.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DiagSelftestActionCause.setStatus(_A)
class _Hm2DiagSelftestAction_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('logOnly',1),('sendTrap',2),('reboot',3)))
_Hm2DiagSelftestAction_Type.__name__=_D
_Hm2DiagSelftestAction_Object=MibTableColumn
hm2DiagSelftestAction=_Hm2DiagSelftestAction_Object((1,3,6,1,4,1,248,11,22,1,1,10,1,2),_Hm2DiagSelftestAction_Type())
hm2DiagSelftestAction.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DiagSelftestAction.setStatus(_A)
_Hm2DiagBootGroup_ObjectIdentity=ObjectIdentity
hm2DiagBootGroup=_Hm2DiagBootGroup_ObjectIdentity((1,3,6,1,4,1,248,11,22,1,2))
class _Hm2BootSystemMonitor_Type(HmEnabledStatus):defaultValue=1
_Hm2BootSystemMonitor_Type.__name__=_E
_Hm2BootSystemMonitor_Object=MibScalar
hm2BootSystemMonitor=_Hm2BootSystemMonitor_Object((1,3,6,1,4,1,248,11,22,1,2,1),_Hm2BootSystemMonitor_Type())
hm2BootSystemMonitor.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2BootSystemMonitor.setStatus(_A)
class _Hm2BootDefaultConfigOnError_Type(HmEnabledStatus):defaultValue=1
_Hm2BootDefaultConfigOnError_Type.__name__=_E
_Hm2BootDefaultConfigOnError_Object=MibScalar
hm2BootDefaultConfigOnError=_Hm2BootDefaultConfigOnError_Object((1,3,6,1,4,1,248,11,22,1,2,2),_Hm2BootDefaultConfigOnError_Type())
hm2BootDefaultConfigOnError.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2BootDefaultConfigOnError.setStatus(_A)
class _Hm2BootConfigPushButton_Type(HmEnabledStatus):defaultValue=1
_Hm2BootConfigPushButton_Type.__name__=_E
_Hm2BootConfigPushButton_Object=MibScalar
hm2BootConfigPushButton=_Hm2BootConfigPushButton_Object((1,3,6,1,4,1,248,11,22,1,2,3),_Hm2BootConfigPushButton_Type())
hm2BootConfigPushButton.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2BootConfigPushButton.setStatus(_A)
_Hm2DiagDeviceMonitorGroup_ObjectIdentity=ObjectIdentity
hm2DiagDeviceMonitorGroup=_Hm2DiagDeviceMonitorGroup_ObjectIdentity((1,3,6,1,4,1,248,11,22,1,3))
_Hm2SignalContactGroup_ObjectIdentity=ObjectIdentity
hm2SignalContactGroup=_Hm2SignalContactGroup_ObjectIdentity((1,3,6,1,4,1,248,11,22,1,3,1))
_Hm2SigConCommonTable_Object=MibTable
hm2SigConCommonTable=_Hm2SigConCommonTable_Object((1,3,6,1,4,1,248,11,22,1,3,1,1))
if mibBuilder.loadTexts:hm2SigConCommonTable.setStatus(_A)
_Hm2SigConCommonEntry_Object=MibTableRow
hm2SigConCommonEntry=_Hm2SigConCommonEntry_Object((1,3,6,1,4,1,248,11,22,1,3,1,1,1))
hm2SigConCommonEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:hm2SigConCommonEntry.setStatus(_A)
class _Hm2SigConID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Hm2SigConID_Type.__name__=_D
_Hm2SigConID_Object=MibTableColumn
hm2SigConID=_Hm2SigConID_Object((1,3,6,1,4,1,248,11,22,1,3,1,1,1,1),_Hm2SigConID_Type())
hm2SigConID.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2SigConID.setStatus(_A)
class _Hm2SigConTrapEnable_Type(HmEnabledStatus):defaultValue=2
_Hm2SigConTrapEnable_Type.__name__=_E
_Hm2SigConTrapEnable_Object=MibTableColumn
hm2SigConTrapEnable=_Hm2SigConTrapEnable_Object((1,3,6,1,4,1,248,11,22,1,3,1,1,1,2),_Hm2SigConTrapEnable_Type())
hm2SigConTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SigConTrapEnable.setStatus(_A)
class _Hm2SigConTrapCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30)));namedValues=NamedValues(*((_M,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8),(_W,9),(_X,10),(_Y,11),(_Z,12),(_a,13),(_b,14),(_c,15),(_d,16),(_e,17),(_f,18),(_g,19),(_h,20),(_i,21),(_j,23),(_k,24),(_l,25),(_m,26),(_y,27),(_n,28),(_t,29),(_o,30)))
_Hm2SigConTrapCause_Type.__name__=_D
_Hm2SigConTrapCause_Object=MibTableColumn
hm2SigConTrapCause=_Hm2SigConTrapCause_Object((1,3,6,1,4,1,248,11,22,1,3,1,1,1,3),_Hm2SigConTrapCause_Type())
hm2SigConTrapCause.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2SigConTrapCause.setStatus(_A)
_Hm2SigConTrapCauseIndex_Type=Integer32
_Hm2SigConTrapCauseIndex_Object=MibTableColumn
hm2SigConTrapCauseIndex=_Hm2SigConTrapCauseIndex_Object((1,3,6,1,4,1,248,11,22,1,3,1,1,1,4),_Hm2SigConTrapCauseIndex_Type())
hm2SigConTrapCauseIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2SigConTrapCauseIndex.setStatus(_A)
class _Hm2SigConMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('manual',1),('monitor',2),('deviceState',3),('deviceSecurity',4),('deviceStateAndSecurity',5)))
_Hm2SigConMode_Type.__name__=_D
_Hm2SigConMode_Object=MibTableColumn
hm2SigConMode=_Hm2SigConMode_Object((1,3,6,1,4,1,248,11,22,1,3,1,1,1,5),_Hm2SigConMode_Type())
hm2SigConMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SigConMode.setStatus(_A)
class _Hm2SigConOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_u,1),('close',2)))
_Hm2SigConOperState_Type.__name__=_D
_Hm2SigConOperState_Object=MibTableColumn
hm2SigConOperState=_Hm2SigConOperState_Object((1,3,6,1,4,1,248,11,22,1,3,1,1,1,6),_Hm2SigConOperState_Type())
hm2SigConOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2SigConOperState.setStatus(_A)
_Hm2SigConOperTimeStamp_Type=HmTimeSeconds1970
_Hm2SigConOperTimeStamp_Object=MibTableColumn
hm2SigConOperTimeStamp=_Hm2SigConOperTimeStamp_Object((1,3,6,1,4,1,248,11,22,1,3,1,1,1,7),_Hm2SigConOperTimeStamp_Type())
hm2SigConOperTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2SigConOperTimeStamp.setStatus(_A)
class _Hm2SigConManualActivate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_u,1),('close',2)))
_Hm2SigConManualActivate_Type.__name__=_D
_Hm2SigConManualActivate_Object=MibTableColumn
hm2SigConManualActivate=_Hm2SigConManualActivate_Object((1,3,6,1,4,1,248,11,22,1,3,1,1,1,8),_Hm2SigConManualActivate_Type())
hm2SigConManualActivate.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SigConManualActivate.setStatus(_A)
class _Hm2SigConSenseLinkFailure_Type(HmEnabledStatus):defaultValue=2
_Hm2SigConSenseLinkFailure_Type.__name__=_E
_Hm2SigConSenseLinkFailure_Object=MibTableColumn
hm2SigConSenseLinkFailure=_Hm2SigConSenseLinkFailure_Object((1,3,6,1,4,1,248,11,22,1,3,1,1,1,9),_Hm2SigConSenseLinkFailure_Type())
hm2SigConSenseLinkFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SigConSenseLinkFailure.setStatus(_A)
class _Hm2SigConSenseTemperature_Type(HmEnabledStatus):defaultValue=1
_Hm2SigConSenseTemperature_Type.__name__=_E
_Hm2SigConSenseTemperature_Object=MibTableColumn
hm2SigConSenseTemperature=_Hm2SigConSenseTemperature_Object((1,3,6,1,4,1,248,11,22,1,3,1,1,1,10),_Hm2SigConSenseTemperature_Type())
hm2SigConSenseTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SigConSenseTemperature.setStatus(_A)
class _Hm2SigConSenseFan_Type(HmEnabledStatus):defaultValue=1
_Hm2SigConSenseFan_Type.__name__=_E
_Hm2SigConSenseFan_Object=MibTableColumn
hm2SigConSenseFan=_Hm2SigConSenseFan_Object((1,3,6,1,4,1,248,11,22,1,3,1,1,1,11),_Hm2SigConSenseFan_Type())
hm2SigConSenseFan.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SigConSenseFan.setStatus(_A)
class _Hm2SigConSenseModuleRemoval_Type(HmEnabledStatus):defaultValue=2
_Hm2SigConSenseModuleRemoval_Type.__name__=_E
_Hm2SigConSenseModuleRemoval_Object=MibTableColumn
hm2SigConSenseModuleRemoval=_Hm2SigConSenseModuleRemoval_Object((1,3,6,1,4,1,248,11,22,1,3,1,1,1,12),_Hm2SigConSenseModuleRemoval_Type())
hm2SigConSenseModuleRemoval.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SigConSenseModuleRemoval.setStatus(_A)
class _Hm2SigConSenseExtNvmRemoval_Type(HmEnabledStatus):defaultValue=2
_Hm2SigConSenseExtNvmRemoval_Type.__name__=_E
_Hm2SigConSenseExtNvmRemoval_Object=MibTableColumn
hm2SigConSenseExtNvmRemoval=_Hm2SigConSenseExtNvmRemoval_Object((1,3,6,1,4,1,248,11,22,1,3,1,1,1,13),_Hm2SigConSenseExtNvmRemoval_Type())
hm2SigConSenseExtNvmRemoval.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SigConSenseExtNvmRemoval.setStatus(_A)
class _Hm2SigConSenseExtNvmNotInSync_Type(HmEnabledStatus):defaultValue=2
_Hm2SigConSenseExtNvmNotInSync_Type.__name__=_E
_Hm2SigConSenseExtNvmNotInSync_Object=MibTableColumn
hm2SigConSenseExtNvmNotInSync=_Hm2SigConSenseExtNvmNotInSync_Object((1,3,6,1,4,1,248,11,22,1,3,1,1,1,14),_Hm2SigConSenseExtNvmNotInSync_Type())
hm2SigConSenseExtNvmNotInSync.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SigConSenseExtNvmNotInSync.setStatus(_A)
class _Hm2SigConSenseRingRedundancy_Type(HmEnabledStatus):defaultValue=2
_Hm2SigConSenseRingRedundancy_Type.__name__=_E
_Hm2SigConSenseRingRedundancy_Object=MibTableColumn
hm2SigConSenseRingRedundancy=_Hm2SigConSenseRingRedundancy_Object((1,3,6,1,4,1,248,11,22,1,3,1,1,1,15),_Hm2SigConSenseRingRedundancy_Type())
hm2SigConSenseRingRedundancy.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SigConSenseRingRedundancy.setStatus(_A)
class _Hm2SigConSenseEthernetLoops_Type(HmEnabledStatus):defaultValue=2
_Hm2SigConSenseEthernetLoops_Type.__name__=_E
_Hm2SigConSenseEthernetLoops_Object=MibTableColumn
hm2SigConSenseEthernetLoops=_Hm2SigConSenseEthernetLoops_Object((1,3,6,1,4,1,248,11,22,1,3,1,1,1,16),_Hm2SigConSenseEthernetLoops_Type())
hm2SigConSenseEthernetLoops.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SigConSenseEthernetLoops.setStatus(_A)
class _Hm2SigConSenseHumidity_Type(HmEnabledStatus):defaultValue=1
_Hm2SigConSenseHumidity_Type.__name__=_E
_Hm2SigConSenseHumidity_Object=MibTableColumn
hm2SigConSenseHumidity=_Hm2SigConSenseHumidity_Object((1,3,6,1,4,1,248,11,22,1,3,1,1,1,17),_Hm2SigConSenseHumidity_Type())
hm2SigConSenseHumidity.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SigConSenseHumidity.setStatus(_A)
class _Hm2SigConSenseStpPortBlock_Type(HmEnabledStatus):defaultValue=1
_Hm2SigConSenseStpPortBlock_Type.__name__=_E
_Hm2SigConSenseStpPortBlock_Object=MibTableColumn
hm2SigConSenseStpPortBlock=_Hm2SigConSenseStpPortBlock_Object((1,3,6,1,4,1,248,11,22,1,3,1,1,1,18),_Hm2SigConSenseStpPortBlock_Type())
hm2SigConSenseStpPortBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SigConSenseStpPortBlock.setStatus(_A)
_Hm2SigConPSTable_Object=MibTable
hm2SigConPSTable=_Hm2SigConPSTable_Object((1,3,6,1,4,1,248,11,22,1,3,1,2))
if mibBuilder.loadTexts:hm2SigConPSTable.setStatus(_A)
_Hm2SigConPSEntry_Object=MibTableRow
hm2SigConPSEntry=_Hm2SigConPSEntry_Object((1,3,6,1,4,1,248,11,22,1,3,1,2,1))
hm2SigConPSEntry.setIndexNames((0,_F,_J),(0,_p,_q))
if mibBuilder.loadTexts:hm2SigConPSEntry.setStatus(_A)
class _Hm2SigConSensePSState_Type(HmEnabledStatus):defaultValue=1
_Hm2SigConSensePSState_Type.__name__=_E
_Hm2SigConSensePSState_Object=MibTableColumn
hm2SigConSensePSState=_Hm2SigConSensePSState_Object((1,3,6,1,4,1,248,11,22,1,3,1,2,1,1),_Hm2SigConSensePSState_Type())
hm2SigConSensePSState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SigConSensePSState.setStatus(_A)
_Hm2SigConInterfaceTable_Object=MibTable
hm2SigConInterfaceTable=_Hm2SigConInterfaceTable_Object((1,3,6,1,4,1,248,11,22,1,3,1,3))
if mibBuilder.loadTexts:hm2SigConInterfaceTable.setStatus(_A)
_Hm2SigConInterfaceEntry_Object=MibTableRow
hm2SigConInterfaceEntry=_Hm2SigConInterfaceEntry_Object((1,3,6,1,4,1,248,11,22,1,3,1,3,1))
hm2SigConInterfaceEntry.setIndexNames((0,_F,_J),(0,_G,_H))
if mibBuilder.loadTexts:hm2SigConInterfaceEntry.setStatus(_A)
class _Hm2SigConSenseIfLinkAlarm_Type(HmEnabledStatus):defaultValue=2
_Hm2SigConSenseIfLinkAlarm_Type.__name__=_E
_Hm2SigConSenseIfLinkAlarm_Object=MibTableColumn
hm2SigConSenseIfLinkAlarm=_Hm2SigConSenseIfLinkAlarm_Object((1,3,6,1,4,1,248,11,22,1,3,1,3,1,1),_Hm2SigConSenseIfLinkAlarm_Type())
hm2SigConSenseIfLinkAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SigConSenseIfLinkAlarm.setStatus(_A)
_Hm2SigConModuleTable_Object=MibTable
hm2SigConModuleTable=_Hm2SigConModuleTable_Object((1,3,6,1,4,1,248,11,22,1,3,1,4))
if mibBuilder.loadTexts:hm2SigConModuleTable.setStatus(_A)
_Hm2SigConModuleEntry_Object=MibTableRow
hm2SigConModuleEntry=_Hm2SigConModuleEntry_Object((1,3,6,1,4,1,248,11,22,1,3,1,4,1))
hm2SigConModuleEntry.setIndexNames((0,_F,_J),(0,_F,_z))
if mibBuilder.loadTexts:hm2SigConModuleEntry.setStatus(_A)
class _Hm2SigConModID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_Hm2SigConModID_Type.__name__=_D
_Hm2SigConModID_Object=MibTableColumn
hm2SigConModID=_Hm2SigConModID_Object((1,3,6,1,4,1,248,11,22,1,3,1,4,1,1),_Hm2SigConModID_Type())
hm2SigConModID.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2SigConModID.setStatus(_A)
class _Hm2SigConSenseModule_Type(HmEnabledStatus):defaultValue=2
_Hm2SigConSenseModule_Type.__name__=_E
_Hm2SigConSenseModule_Object=MibTableColumn
hm2SigConSenseModule=_Hm2SigConSenseModule_Object((1,3,6,1,4,1,248,11,22,1,3,1,4,1,2),_Hm2SigConSenseModule_Type())
hm2SigConSenseModule.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SigConSenseModule.setStatus(_A)
_Hm2SigConFanModuleTable_Object=MibTable
hm2SigConFanModuleTable=_Hm2SigConFanModuleTable_Object((1,3,6,1,4,1,248,11,22,1,3,1,5))
if mibBuilder.loadTexts:hm2SigConFanModuleTable.setStatus(_A)
_Hm2SigConFanModuleEntry_Object=MibTableRow
hm2SigConFanModuleEntry=_Hm2SigConFanModuleEntry_Object((1,3,6,1,4,1,248,11,22,1,3,1,5,1))
hm2SigConFanModuleEntry.setIndexNames((0,_F,_J),(0,_F,_A0))
if mibBuilder.loadTexts:hm2SigConFanModuleEntry.setStatus(_A)
class _Hm2SigConFanModID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_Hm2SigConFanModID_Type.__name__=_D
_Hm2SigConFanModID_Object=MibTableColumn
hm2SigConFanModID=_Hm2SigConFanModID_Object((1,3,6,1,4,1,248,11,22,1,3,1,5,1,1),_Hm2SigConFanModID_Type())
hm2SigConFanModID.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2SigConFanModID.setStatus(_A)
class _Hm2SigConSenseFanModule_Type(HmEnabledStatus):defaultValue=1
_Hm2SigConSenseFanModule_Type.__name__=_E
_Hm2SigConSenseFanModule_Object=MibTableColumn
hm2SigConSenseFanModule=_Hm2SigConSenseFanModule_Object((1,3,6,1,4,1,248,11,22,1,3,1,5,1,2),_Hm2SigConSenseFanModule_Type())
hm2SigConSenseFanModule.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SigConSenseFanModule.setStatus(_A)
_Hm2SigConStatusTable_Object=MibTable
hm2SigConStatusTable=_Hm2SigConStatusTable_Object((1,3,6,1,4,1,248,11,22,1,3,1,10))
if mibBuilder.loadTexts:hm2SigConStatusTable.setStatus(_A)
_Hm2SigConStatusEntry_Object=MibTableRow
hm2SigConStatusEntry=_Hm2SigConStatusEntry_Object((1,3,6,1,4,1,248,11,22,1,3,1,10,1))
hm2SigConStatusEntry.setIndexNames((0,_F,_J),(0,_F,_A1))
if mibBuilder.loadTexts:hm2SigConStatusEntry.setStatus(_A)
_Hm2SigConStatusIndex_Type=Integer32
_Hm2SigConStatusIndex_Object=MibTableColumn
hm2SigConStatusIndex=_Hm2SigConStatusIndex_Object((1,3,6,1,4,1,248,11,22,1,3,1,10,1,1),_Hm2SigConStatusIndex_Type())
hm2SigConStatusIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:hm2SigConStatusIndex.setStatus(_A)
_Hm2SigConStatusTimeStamp_Type=HmTimeSeconds1970
_Hm2SigConStatusTimeStamp_Object=MibTableColumn
hm2SigConStatusTimeStamp=_Hm2SigConStatusTimeStamp_Object((1,3,6,1,4,1,248,11,22,1,3,1,10,1,2),_Hm2SigConStatusTimeStamp_Type())
hm2SigConStatusTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2SigConStatusTimeStamp.setStatus(_A)
class _Hm2SigConStatusTrapCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30)));namedValues=NamedValues(*((_M,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8),(_W,9),(_X,10),(_Y,11),(_Z,12),(_a,13),(_b,14),(_c,15),(_d,16),(_e,17),(_f,18),(_g,19),(_h,20),(_i,21),(_v,22),(_j,23),(_k,24),(_l,25),(_m,26),(_y,27),(_n,28),(_o,30)))
_Hm2SigConStatusTrapCause_Type.__name__=_D
_Hm2SigConStatusTrapCause_Object=MibTableColumn
hm2SigConStatusTrapCause=_Hm2SigConStatusTrapCause_Object((1,3,6,1,4,1,248,11,22,1,3,1,10,1,3),_Hm2SigConStatusTrapCause_Type())
hm2SigConStatusTrapCause.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2SigConStatusTrapCause.setStatus(_A)
_Hm2SigConStatusTrapCauseIndex_Type=Integer32
_Hm2SigConStatusTrapCauseIndex_Object=MibTableColumn
hm2SigConStatusTrapCauseIndex=_Hm2SigConStatusTrapCauseIndex_Object((1,3,6,1,4,1,248,11,22,1,3,1,10,1,4),_Hm2SigConStatusTrapCauseIndex_Type())
hm2SigConStatusTrapCauseIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2SigConStatusTrapCauseIndex.setStatus(_A)
_Hm2DeviceMonitorGroup_ObjectIdentity=ObjectIdentity
hm2DeviceMonitorGroup=_Hm2DeviceMonitorGroup_ObjectIdentity((1,3,6,1,4,1,248,11,22,1,3,2))
_Hm2DevMonCommonTable_Object=MibTable
hm2DevMonCommonTable=_Hm2DevMonCommonTable_Object((1,3,6,1,4,1,248,11,22,1,3,2,1))
if mibBuilder.loadTexts:hm2DevMonCommonTable.setStatus(_A)
_Hm2DevMonCommonEntry_Object=MibTableRow
hm2DevMonCommonEntry=_Hm2DevMonCommonEntry_Object((1,3,6,1,4,1,248,11,22,1,3,2,1,1))
hm2DevMonCommonEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:hm2DevMonCommonEntry.setStatus(_A)
class _Hm2DevMonID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Hm2DevMonID_Type.__name__=_D
_Hm2DevMonID_Object=MibTableColumn
hm2DevMonID=_Hm2DevMonID_Object((1,3,6,1,4,1,248,11,22,1,3,2,1,1,1),_Hm2DevMonID_Type())
hm2DevMonID.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DevMonID.setStatus(_A)
class _Hm2DevMonTrapEnable_Type(HmEnabledStatus):defaultValue=1
_Hm2DevMonTrapEnable_Type.__name__=_E
_Hm2DevMonTrapEnable_Object=MibTableColumn
hm2DevMonTrapEnable=_Hm2DevMonTrapEnable_Object((1,3,6,1,4,1,248,11,22,1,3,2,1,1,2),_Hm2DevMonTrapEnable_Type())
hm2DevMonTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMonTrapEnable.setStatus(_A)
class _Hm2DevMonTrapCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,28,30)));namedValues=NamedValues(*((_M,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8),(_W,9),(_n,28),(_o,30)))
_Hm2DevMonTrapCause_Type.__name__=_D
_Hm2DevMonTrapCause_Object=MibTableColumn
hm2DevMonTrapCause=_Hm2DevMonTrapCause_Object((1,3,6,1,4,1,248,11,22,1,3,2,1,1,3),_Hm2DevMonTrapCause_Type())
hm2DevMonTrapCause.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DevMonTrapCause.setStatus(_A)
_Hm2DevMonTrapCauseIndex_Type=Integer32
_Hm2DevMonTrapCauseIndex_Object=MibTableColumn
hm2DevMonTrapCauseIndex=_Hm2DevMonTrapCauseIndex_Object((1,3,6,1,4,1,248,11,22,1,3,2,1,1,4),_Hm2DevMonTrapCauseIndex_Type())
hm2DevMonTrapCauseIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DevMonTrapCauseIndex.setStatus(_A)
class _Hm2DevMonOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noerror',1),('error',2)))
_Hm2DevMonOperState_Type.__name__=_D
_Hm2DevMonOperState_Object=MibTableColumn
hm2DevMonOperState=_Hm2DevMonOperState_Object((1,3,6,1,4,1,248,11,22,1,3,2,1,1,5),_Hm2DevMonOperState_Type())
hm2DevMonOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DevMonOperState.setStatus(_A)
_Hm2DevMonOperTimeStamp_Type=HmTimeSeconds1970
_Hm2DevMonOperTimeStamp_Object=MibTableColumn
hm2DevMonOperTimeStamp=_Hm2DevMonOperTimeStamp_Object((1,3,6,1,4,1,248,11,22,1,3,2,1,1,6),_Hm2DevMonOperTimeStamp_Type())
hm2DevMonOperTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DevMonOperTimeStamp.setStatus(_A)
class _Hm2DevMonSenseLinkFailure_Type(HmEnabledStatus):defaultValue=2
_Hm2DevMonSenseLinkFailure_Type.__name__=_E
_Hm2DevMonSenseLinkFailure_Object=MibTableColumn
hm2DevMonSenseLinkFailure=_Hm2DevMonSenseLinkFailure_Object((1,3,6,1,4,1,248,11,22,1,3,2,1,1,7),_Hm2DevMonSenseLinkFailure_Type())
hm2DevMonSenseLinkFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMonSenseLinkFailure.setStatus(_A)
class _Hm2DevMonSenseTemperature_Type(HmEnabledStatus):defaultValue=1
_Hm2DevMonSenseTemperature_Type.__name__=_E
_Hm2DevMonSenseTemperature_Object=MibTableColumn
hm2DevMonSenseTemperature=_Hm2DevMonSenseTemperature_Object((1,3,6,1,4,1,248,11,22,1,3,2,1,1,8),_Hm2DevMonSenseTemperature_Type())
hm2DevMonSenseTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMonSenseTemperature.setStatus(_A)
class _Hm2DevMonSenseFan_Type(HmEnabledStatus):defaultValue=1
_Hm2DevMonSenseFan_Type.__name__=_E
_Hm2DevMonSenseFan_Object=MibTableColumn
hm2DevMonSenseFan=_Hm2DevMonSenseFan_Object((1,3,6,1,4,1,248,11,22,1,3,2,1,1,9),_Hm2DevMonSenseFan_Type())
hm2DevMonSenseFan.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMonSenseFan.setStatus(_A)
class _Hm2DevMonSenseModuleRemoval_Type(HmEnabledStatus):defaultValue=2
_Hm2DevMonSenseModuleRemoval_Type.__name__=_E
_Hm2DevMonSenseModuleRemoval_Object=MibTableColumn
hm2DevMonSenseModuleRemoval=_Hm2DevMonSenseModuleRemoval_Object((1,3,6,1,4,1,248,11,22,1,3,2,1,1,10),_Hm2DevMonSenseModuleRemoval_Type())
hm2DevMonSenseModuleRemoval.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMonSenseModuleRemoval.setStatus(_A)
class _Hm2DevMonSenseExtNvmRemoval_Type(HmEnabledStatus):defaultValue=2
_Hm2DevMonSenseExtNvmRemoval_Type.__name__=_E
_Hm2DevMonSenseExtNvmRemoval_Object=MibTableColumn
hm2DevMonSenseExtNvmRemoval=_Hm2DevMonSenseExtNvmRemoval_Object((1,3,6,1,4,1,248,11,22,1,3,2,1,1,11),_Hm2DevMonSenseExtNvmRemoval_Type())
hm2DevMonSenseExtNvmRemoval.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMonSenseExtNvmRemoval.setStatus(_A)
class _Hm2DevMonSenseExtNvmNotInSync_Type(HmEnabledStatus):defaultValue=2
_Hm2DevMonSenseExtNvmNotInSync_Type.__name__=_E
_Hm2DevMonSenseExtNvmNotInSync_Object=MibTableColumn
hm2DevMonSenseExtNvmNotInSync=_Hm2DevMonSenseExtNvmNotInSync_Object((1,3,6,1,4,1,248,11,22,1,3,2,1,1,12),_Hm2DevMonSenseExtNvmNotInSync_Type())
hm2DevMonSenseExtNvmNotInSync.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMonSenseExtNvmNotInSync.setStatus(_A)
class _Hm2DevMonSenseRingRedundancy_Type(HmEnabledStatus):defaultValue=2
_Hm2DevMonSenseRingRedundancy_Type.__name__=_E
_Hm2DevMonSenseRingRedundancy_Object=MibTableColumn
hm2DevMonSenseRingRedundancy=_Hm2DevMonSenseRingRedundancy_Object((1,3,6,1,4,1,248,11,22,1,3,2,1,1,13),_Hm2DevMonSenseRingRedundancy_Type())
hm2DevMonSenseRingRedundancy.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMonSenseRingRedundancy.setStatus(_A)
class _Hm2DevMonSenseHumidity_Type(HmEnabledStatus):defaultValue=1
_Hm2DevMonSenseHumidity_Type.__name__=_E
_Hm2DevMonSenseHumidity_Object=MibTableColumn
hm2DevMonSenseHumidity=_Hm2DevMonSenseHumidity_Object((1,3,6,1,4,1,248,11,22,1,3,2,1,1,14),_Hm2DevMonSenseHumidity_Type())
hm2DevMonSenseHumidity.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMonSenseHumidity.setStatus(_A)
class _Hm2DevMonSenseStpPortBlock_Type(HmEnabledStatus):defaultValue=1
_Hm2DevMonSenseStpPortBlock_Type.__name__=_E
_Hm2DevMonSenseStpPortBlock_Object=MibTableColumn
hm2DevMonSenseStpPortBlock=_Hm2DevMonSenseStpPortBlock_Object((1,3,6,1,4,1,248,11,22,1,3,2,1,1,15),_Hm2DevMonSenseStpPortBlock_Type())
hm2DevMonSenseStpPortBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMonSenseStpPortBlock.setStatus(_A)
_Hm2DevMonPSTable_Object=MibTable
hm2DevMonPSTable=_Hm2DevMonPSTable_Object((1,3,6,1,4,1,248,11,22,1,3,2,2))
if mibBuilder.loadTexts:hm2DevMonPSTable.setStatus(_A)
_Hm2DevMonPSEntry_Object=MibTableRow
hm2DevMonPSEntry=_Hm2DevMonPSEntry_Object((1,3,6,1,4,1,248,11,22,1,3,2,2,1))
hm2DevMonPSEntry.setIndexNames((0,_F,_K),(0,_p,_q))
if mibBuilder.loadTexts:hm2DevMonPSEntry.setStatus(_A)
class _Hm2DevMonSensePSState_Type(HmEnabledStatus):defaultValue=1
_Hm2DevMonSensePSState_Type.__name__=_E
_Hm2DevMonSensePSState_Object=MibTableColumn
hm2DevMonSensePSState=_Hm2DevMonSensePSState_Object((1,3,6,1,4,1,248,11,22,1,3,2,2,1,1),_Hm2DevMonSensePSState_Type())
hm2DevMonSensePSState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMonSensePSState.setStatus(_A)
_Hm2DevMonInterfaceTable_Object=MibTable
hm2DevMonInterfaceTable=_Hm2DevMonInterfaceTable_Object((1,3,6,1,4,1,248,11,22,1,3,2,3))
if mibBuilder.loadTexts:hm2DevMonInterfaceTable.setStatus(_A)
_Hm2DevMonInterfaceEntry_Object=MibTableRow
hm2DevMonInterfaceEntry=_Hm2DevMonInterfaceEntry_Object((1,3,6,1,4,1,248,11,22,1,3,2,3,1))
hm2DevMonInterfaceEntry.setIndexNames((0,_F,_K),(0,_G,_H))
if mibBuilder.loadTexts:hm2DevMonInterfaceEntry.setStatus(_A)
class _Hm2DevMonSenseIfLinkAlarm_Type(HmEnabledStatus):defaultValue=2
_Hm2DevMonSenseIfLinkAlarm_Type.__name__=_E
_Hm2DevMonSenseIfLinkAlarm_Object=MibTableColumn
hm2DevMonSenseIfLinkAlarm=_Hm2DevMonSenseIfLinkAlarm_Object((1,3,6,1,4,1,248,11,22,1,3,2,3,1,1),_Hm2DevMonSenseIfLinkAlarm_Type())
hm2DevMonSenseIfLinkAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMonSenseIfLinkAlarm.setStatus(_A)
_Hm2DevMonModuleTable_Object=MibTable
hm2DevMonModuleTable=_Hm2DevMonModuleTable_Object((1,3,6,1,4,1,248,11,22,1,3,2,4))
if mibBuilder.loadTexts:hm2DevMonModuleTable.setStatus(_A)
_Hm2DevMonModuleEntry_Object=MibTableRow
hm2DevMonModuleEntry=_Hm2DevMonModuleEntry_Object((1,3,6,1,4,1,248,11,22,1,3,2,4,1))
hm2DevMonModuleEntry.setIndexNames((0,_F,_K),(0,_F,_A2))
if mibBuilder.loadTexts:hm2DevMonModuleEntry.setStatus(_A)
class _Hm2DevMonModID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_Hm2DevMonModID_Type.__name__=_D
_Hm2DevMonModID_Object=MibTableColumn
hm2DevMonModID=_Hm2DevMonModID_Object((1,3,6,1,4,1,248,11,22,1,3,2,4,1,1),_Hm2DevMonModID_Type())
hm2DevMonModID.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DevMonModID.setStatus(_A)
class _Hm2DevMonSenseModule_Type(HmEnabledStatus):defaultValue=2
_Hm2DevMonSenseModule_Type.__name__=_E
_Hm2DevMonSenseModule_Object=MibTableColumn
hm2DevMonSenseModule=_Hm2DevMonSenseModule_Object((1,3,6,1,4,1,248,11,22,1,3,2,4,1,2),_Hm2DevMonSenseModule_Type())
hm2DevMonSenseModule.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMonSenseModule.setStatus(_A)
_Hm2DevMonFanModuleTable_Object=MibTable
hm2DevMonFanModuleTable=_Hm2DevMonFanModuleTable_Object((1,3,6,1,4,1,248,11,22,1,3,2,5))
if mibBuilder.loadTexts:hm2DevMonFanModuleTable.setStatus(_A)
_Hm2DevMonFanModuleEntry_Object=MibTableRow
hm2DevMonFanModuleEntry=_Hm2DevMonFanModuleEntry_Object((1,3,6,1,4,1,248,11,22,1,3,2,5,1))
hm2DevMonFanModuleEntry.setIndexNames((0,_F,_K),(0,_F,_A3))
if mibBuilder.loadTexts:hm2DevMonFanModuleEntry.setStatus(_A)
class _Hm2DevMonFanModID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_Hm2DevMonFanModID_Type.__name__=_D
_Hm2DevMonFanModID_Object=MibTableColumn
hm2DevMonFanModID=_Hm2DevMonFanModID_Object((1,3,6,1,4,1,248,11,22,1,3,2,5,1,1),_Hm2DevMonFanModID_Type())
hm2DevMonFanModID.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DevMonFanModID.setStatus(_A)
class _Hm2DevMonSenseFanModule_Type(HmEnabledStatus):defaultValue=1
_Hm2DevMonSenseFanModule_Type.__name__=_E
_Hm2DevMonSenseFanModule_Object=MibTableColumn
hm2DevMonSenseFanModule=_Hm2DevMonSenseFanModule_Object((1,3,6,1,4,1,248,11,22,1,3,2,5,1,2),_Hm2DevMonSenseFanModule_Type())
hm2DevMonSenseFanModule.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevMonSenseFanModule.setStatus(_A)
_Hm2DevMonStatusTable_Object=MibTable
hm2DevMonStatusTable=_Hm2DevMonStatusTable_Object((1,3,6,1,4,1,248,11,22,1,3,2,10))
if mibBuilder.loadTexts:hm2DevMonStatusTable.setStatus(_A)
_Hm2DevMonStatusEntry_Object=MibTableRow
hm2DevMonStatusEntry=_Hm2DevMonStatusEntry_Object((1,3,6,1,4,1,248,11,22,1,3,2,10,1))
hm2DevMonStatusEntry.setIndexNames((0,_F,_K),(0,_F,_A4))
if mibBuilder.loadTexts:hm2DevMonStatusEntry.setStatus(_A)
_Hm2DevMonStatusIndex_Type=Integer32
_Hm2DevMonStatusIndex_Object=MibTableColumn
hm2DevMonStatusIndex=_Hm2DevMonStatusIndex_Object((1,3,6,1,4,1,248,11,22,1,3,2,10,1,1),_Hm2DevMonStatusIndex_Type())
hm2DevMonStatusIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:hm2DevMonStatusIndex.setStatus(_A)
_Hm2DevMonStatusTimeStamp_Type=HmTimeSeconds1970
_Hm2DevMonStatusTimeStamp_Object=MibTableColumn
hm2DevMonStatusTimeStamp=_Hm2DevMonStatusTimeStamp_Object((1,3,6,1,4,1,248,11,22,1,3,2,10,1,2),_Hm2DevMonStatusTimeStamp_Type())
hm2DevMonStatusTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DevMonStatusTimeStamp.setStatus(_A)
class _Hm2DevMonStatusTrapCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,28,30)));namedValues=NamedValues(*((_M,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8),(_W,9),(_n,28),(_o,30)))
_Hm2DevMonStatusTrapCause_Type.__name__=_D
_Hm2DevMonStatusTrapCause_Object=MibTableColumn
hm2DevMonStatusTrapCause=_Hm2DevMonStatusTrapCause_Object((1,3,6,1,4,1,248,11,22,1,3,2,10,1,3),_Hm2DevMonStatusTrapCause_Type())
hm2DevMonStatusTrapCause.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DevMonStatusTrapCause.setStatus(_A)
_Hm2DevMonStatusTrapCauseIndex_Type=Integer32
_Hm2DevMonStatusTrapCauseIndex_Object=MibTableColumn
hm2DevMonStatusTrapCauseIndex=_Hm2DevMonStatusTrapCauseIndex_Object((1,3,6,1,4,1,248,11,22,1,3,2,10,1,4),_Hm2DevMonStatusTrapCauseIndex_Type())
hm2DevMonStatusTrapCauseIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DevMonStatusTrapCauseIndex.setStatus(_A)
_Hm2DeviceSecurityGroup_ObjectIdentity=ObjectIdentity
hm2DeviceSecurityGroup=_Hm2DeviceSecurityGroup_ObjectIdentity((1,3,6,1,4,1,248,11,22,1,3,3))
_Hm2DevSecConfigGroup_ObjectIdentity=ObjectIdentity
hm2DevSecConfigGroup=_Hm2DevSecConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,11,22,1,3,3,1))
class _Hm2DevSecTrapEnable_Type(HmEnabledStatus):defaultValue=2
_Hm2DevSecTrapEnable_Type.__name__=_E
_Hm2DevSecTrapEnable_Object=MibScalar
hm2DevSecTrapEnable=_Hm2DevSecTrapEnable_Object((1,3,6,1,4,1,248,11,22,1,3,3,1,1),_Hm2DevSecTrapEnable_Type())
hm2DevSecTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevSecTrapEnable.setStatus(_A)
class _Hm2DevSecTrapCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,29)));namedValues=NamedValues(*((_M,1),(_X,10),(_Y,11),(_Z,12),(_a,13),(_b,14),(_c,15),(_d,16),(_e,17),(_f,18),(_g,19),(_h,20),(_i,21),(_v,22),(_j,23),(_k,24),(_l,25),(_m,26),(_t,29)))
_Hm2DevSecTrapCause_Type.__name__=_D
_Hm2DevSecTrapCause_Object=MibScalar
hm2DevSecTrapCause=_Hm2DevSecTrapCause_Object((1,3,6,1,4,1,248,11,22,1,3,3,1,2),_Hm2DevSecTrapCause_Type())
hm2DevSecTrapCause.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DevSecTrapCause.setStatus(_A)
_Hm2DevSecTrapCauseIndex_Type=Integer32
_Hm2DevSecTrapCauseIndex_Object=MibScalar
hm2DevSecTrapCauseIndex=_Hm2DevSecTrapCauseIndex_Object((1,3,6,1,4,1,248,11,22,1,3,3,1,3),_Hm2DevSecTrapCauseIndex_Type())
hm2DevSecTrapCauseIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DevSecTrapCauseIndex.setStatus(_A)
class _Hm2DevSecOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noerror',1),('error',2)))
_Hm2DevSecOperState_Type.__name__=_D
_Hm2DevSecOperState_Object=MibScalar
hm2DevSecOperState=_Hm2DevSecOperState_Object((1,3,6,1,4,1,248,11,22,1,3,3,1,4),_Hm2DevSecOperState_Type())
hm2DevSecOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DevSecOperState.setStatus(_A)
_Hm2DevSecOperTimeStamp_Type=HmTimeSeconds1970
_Hm2DevSecOperTimeStamp_Object=MibScalar
hm2DevSecOperTimeStamp=_Hm2DevSecOperTimeStamp_Object((1,3,6,1,4,1,248,11,22,1,3,3,1,5),_Hm2DevSecOperTimeStamp_Type())
hm2DevSecOperTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DevSecOperTimeStamp.setStatus(_A)
class _Hm2DevSecSensePasswordChange_Type(HmEnabledStatus):defaultValue=1
_Hm2DevSecSensePasswordChange_Type.__name__=_E
_Hm2DevSecSensePasswordChange_Object=MibScalar
hm2DevSecSensePasswordChange=_Hm2DevSecSensePasswordChange_Object((1,3,6,1,4,1,248,11,22,1,3,3,1,6),_Hm2DevSecSensePasswordChange_Type())
hm2DevSecSensePasswordChange.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevSecSensePasswordChange.setStatus(_A)
class _Hm2DevSecSensePasswordMinLength_Type(HmEnabledStatus):defaultValue=1
_Hm2DevSecSensePasswordMinLength_Type.__name__=_E
_Hm2DevSecSensePasswordMinLength_Object=MibScalar
hm2DevSecSensePasswordMinLength=_Hm2DevSecSensePasswordMinLength_Object((1,3,6,1,4,1,248,11,22,1,3,3,1,7),_Hm2DevSecSensePasswordMinLength_Type())
hm2DevSecSensePasswordMinLength.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevSecSensePasswordMinLength.setStatus(_A)
class _Hm2DevSecSensePasswordStrengthNotConfigured_Type(HmEnabledStatus):defaultValue=1
_Hm2DevSecSensePasswordStrengthNotConfigured_Type.__name__=_E
_Hm2DevSecSensePasswordStrengthNotConfigured_Object=MibScalar
hm2DevSecSensePasswordStrengthNotConfigured=_Hm2DevSecSensePasswordStrengthNotConfigured_Object((1,3,6,1,4,1,248,11,22,1,3,3,1,8),_Hm2DevSecSensePasswordStrengthNotConfigured_Type())
hm2DevSecSensePasswordStrengthNotConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevSecSensePasswordStrengthNotConfigured.setStatus(_A)
class _Hm2DevSecSenseBypassPasswordStrength_Type(HmEnabledStatus):defaultValue=2
_Hm2DevSecSenseBypassPasswordStrength_Type.__name__=_E
_Hm2DevSecSenseBypassPasswordStrength_Object=MibScalar
hm2DevSecSenseBypassPasswordStrength=_Hm2DevSecSenseBypassPasswordStrength_Object((1,3,6,1,4,1,248,11,22,1,3,3,1,9),_Hm2DevSecSenseBypassPasswordStrength_Type())
hm2DevSecSenseBypassPasswordStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevSecSenseBypassPasswordStrength.setStatus(_A)
class _Hm2DevSecSenseTelnetEnabled_Type(HmEnabledStatus):defaultValue=1
_Hm2DevSecSenseTelnetEnabled_Type.__name__=_E
_Hm2DevSecSenseTelnetEnabled_Object=MibScalar
hm2DevSecSenseTelnetEnabled=_Hm2DevSecSenseTelnetEnabled_Object((1,3,6,1,4,1,248,11,22,1,3,3,1,10),_Hm2DevSecSenseTelnetEnabled_Type())
hm2DevSecSenseTelnetEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevSecSenseTelnetEnabled.setStatus(_A)
class _Hm2DevSecSenseHttpEnabled_Type(HmEnabledStatus):defaultValue=1
_Hm2DevSecSenseHttpEnabled_Type.__name__=_E
_Hm2DevSecSenseHttpEnabled_Object=MibScalar
hm2DevSecSenseHttpEnabled=_Hm2DevSecSenseHttpEnabled_Object((1,3,6,1,4,1,248,11,22,1,3,3,1,11),_Hm2DevSecSenseHttpEnabled_Type())
hm2DevSecSenseHttpEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevSecSenseHttpEnabled.setStatus(_A)
class _Hm2DevSecSenseSnmpUnsecure_Type(HmEnabledStatus):defaultValue=1
_Hm2DevSecSenseSnmpUnsecure_Type.__name__=_E
_Hm2DevSecSenseSnmpUnsecure_Object=MibScalar
hm2DevSecSenseSnmpUnsecure=_Hm2DevSecSenseSnmpUnsecure_Object((1,3,6,1,4,1,248,11,22,1,3,3,1,12),_Hm2DevSecSenseSnmpUnsecure_Type())
hm2DevSecSenseSnmpUnsecure.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevSecSenseSnmpUnsecure.setStatus(_A)
class _Hm2DevSecSenseSysmonEnabled_Type(HmEnabledStatus):defaultValue=2
_Hm2DevSecSenseSysmonEnabled_Type.__name__=_E
_Hm2DevSecSenseSysmonEnabled_Object=MibScalar
hm2DevSecSenseSysmonEnabled=_Hm2DevSecSenseSysmonEnabled_Object((1,3,6,1,4,1,248,11,22,1,3,3,1,13),_Hm2DevSecSenseSysmonEnabled_Type())
hm2DevSecSenseSysmonEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevSecSenseSysmonEnabled.setStatus(_A)
class _Hm2DevSecSenseExtNvmUpdateEnabled_Type(HmEnabledStatus):defaultValue=2
_Hm2DevSecSenseExtNvmUpdateEnabled_Type.__name__=_E
_Hm2DevSecSenseExtNvmUpdateEnabled_Object=MibScalar
hm2DevSecSenseExtNvmUpdateEnabled=_Hm2DevSecSenseExtNvmUpdateEnabled_Object((1,3,6,1,4,1,248,11,22,1,3,3,1,14),_Hm2DevSecSenseExtNvmUpdateEnabled_Type())
hm2DevSecSenseExtNvmUpdateEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevSecSenseExtNvmUpdateEnabled.setStatus(_A)
class _Hm2DevSecSenseNoLinkEnabled_Type(HmEnabledStatus):defaultValue=2
_Hm2DevSecSenseNoLinkEnabled_Type.__name__=_E
_Hm2DevSecSenseNoLinkEnabled_Object=MibScalar
hm2DevSecSenseNoLinkEnabled=_Hm2DevSecSenseNoLinkEnabled_Object((1,3,6,1,4,1,248,11,22,1,3,3,1,15),_Hm2DevSecSenseNoLinkEnabled_Type())
hm2DevSecSenseNoLinkEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevSecSenseNoLinkEnabled.setStatus(_A)
class _Hm2DevSecSenseHiDiscoveryEnabled_Type(HmEnabledStatus):defaultValue=1
_Hm2DevSecSenseHiDiscoveryEnabled_Type.__name__=_E
_Hm2DevSecSenseHiDiscoveryEnabled_Object=MibScalar
hm2DevSecSenseHiDiscoveryEnabled=_Hm2DevSecSenseHiDiscoveryEnabled_Object((1,3,6,1,4,1,248,11,22,1,3,3,1,16),_Hm2DevSecSenseHiDiscoveryEnabled_Type())
hm2DevSecSenseHiDiscoveryEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevSecSenseHiDiscoveryEnabled.setStatus(_A)
class _Hm2DevSecSenseExtNvmConfigLoadUnsecure_Type(HmEnabledStatus):defaultValue=1
_Hm2DevSecSenseExtNvmConfigLoadUnsecure_Type.__name__=_E
_Hm2DevSecSenseExtNvmConfigLoadUnsecure_Object=MibScalar
hm2DevSecSenseExtNvmConfigLoadUnsecure=_Hm2DevSecSenseExtNvmConfigLoadUnsecure_Object((1,3,6,1,4,1,248,11,22,1,3,3,1,17),_Hm2DevSecSenseExtNvmConfigLoadUnsecure_Type())
hm2DevSecSenseExtNvmConfigLoadUnsecure.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevSecSenseExtNvmConfigLoadUnsecure.setStatus(_A)
class _Hm2DevSecSenseIec61850MmsEnabled_Type(HmEnabledStatus):defaultValue=1
_Hm2DevSecSenseIec61850MmsEnabled_Type.__name__=_E
_Hm2DevSecSenseIec61850MmsEnabled_Object=MibScalar
hm2DevSecSenseIec61850MmsEnabled=_Hm2DevSecSenseIec61850MmsEnabled_Object((1,3,6,1,4,1,248,11,22,1,3,3,1,18),_Hm2DevSecSenseIec61850MmsEnabled_Type())
hm2DevSecSenseIec61850MmsEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevSecSenseIec61850MmsEnabled.setStatus(_A)
class _Hm2DevSecSenseHttpsCertificateWarning_Type(HmEnabledStatus):defaultValue=1
_Hm2DevSecSenseHttpsCertificateWarning_Type.__name__=_E
_Hm2DevSecSenseHttpsCertificateWarning_Object=MibScalar
hm2DevSecSenseHttpsCertificateWarning=_Hm2DevSecSenseHttpsCertificateWarning_Object((1,3,6,1,4,1,248,11,22,1,3,3,1,19),_Hm2DevSecSenseHttpsCertificateWarning_Type())
hm2DevSecSenseHttpsCertificateWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevSecSenseHttpsCertificateWarning.setStatus(_A)
class _Hm2DevSecSenseModbusTcpEnabled_Type(HmEnabledStatus):defaultValue=1
_Hm2DevSecSenseModbusTcpEnabled_Type.__name__=_E
_Hm2DevSecSenseModbusTcpEnabled_Object=MibScalar
hm2DevSecSenseModbusTcpEnabled=_Hm2DevSecSenseModbusTcpEnabled_Object((1,3,6,1,4,1,248,11,22,1,3,3,1,20),_Hm2DevSecSenseModbusTcpEnabled_Type())
hm2DevSecSenseModbusTcpEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevSecSenseModbusTcpEnabled.setStatus(_A)
class _Hm2DevSecSenseEtherNetIpEnabled_Type(HmEnabledStatus):defaultValue=1
_Hm2DevSecSenseEtherNetIpEnabled_Type.__name__=_E
_Hm2DevSecSenseEtherNetIpEnabled_Object=MibScalar
hm2DevSecSenseEtherNetIpEnabled=_Hm2DevSecSenseEtherNetIpEnabled_Object((1,3,6,1,4,1,248,11,22,1,3,3,1,21),_Hm2DevSecSenseEtherNetIpEnabled_Type())
hm2DevSecSenseEtherNetIpEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevSecSenseEtherNetIpEnabled.setStatus(_A)
class _Hm2DevSecSenseProfinetIOEnabled_Type(HmEnabledStatus):defaultValue=1
_Hm2DevSecSenseProfinetIOEnabled_Type.__name__=_E
_Hm2DevSecSenseProfinetIOEnabled_Object=MibScalar
hm2DevSecSenseProfinetIOEnabled=_Hm2DevSecSenseProfinetIOEnabled_Object((1,3,6,1,4,1,248,11,22,1,3,3,1,22),_Hm2DevSecSenseProfinetIOEnabled_Type())
hm2DevSecSenseProfinetIOEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevSecSenseProfinetIOEnabled.setStatus(_A)
class _Hm2DevSecSensePMLDisabled_Type(HmEnabledStatus):defaultValue=1
_Hm2DevSecSensePMLDisabled_Type.__name__=_E
_Hm2DevSecSensePMLDisabled_Object=MibScalar
hm2DevSecSensePMLDisabled=_Hm2DevSecSensePMLDisabled_Object((1,3,6,1,4,1,248,11,22,1,3,3,1,23),_Hm2DevSecSensePMLDisabled_Type())
hm2DevSecSensePMLDisabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevSecSensePMLDisabled.setStatus(_A)
_Hm2DevSecInterfaceTable_Object=MibTable
hm2DevSecInterfaceTable=_Hm2DevSecInterfaceTable_Object((1,3,6,1,4,1,248,11,22,1,3,3,2))
if mibBuilder.loadTexts:hm2DevSecInterfaceTable.setStatus(_A)
_Hm2DevSecInterfaceEntry_Object=MibTableRow
hm2DevSecInterfaceEntry=_Hm2DevSecInterfaceEntry_Object((1,3,6,1,4,1,248,11,22,1,3,3,2,1))
hm2DevSecInterfaceEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hm2DevSecInterfaceEntry.setStatus(_A)
class _Hm2DevSecSenseIfNoLink_Type(HmEnabledStatus):defaultValue=2
_Hm2DevSecSenseIfNoLink_Type.__name__=_E
_Hm2DevSecSenseIfNoLink_Object=MibTableColumn
hm2DevSecSenseIfNoLink=_Hm2DevSecSenseIfNoLink_Object((1,3,6,1,4,1,248,11,22,1,3,3,2,1,1),_Hm2DevSecSenseIfNoLink_Type())
hm2DevSecSenseIfNoLink.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DevSecSenseIfNoLink.setStatus(_A)
_Hm2DevSecStatusTable_Object=MibTable
hm2DevSecStatusTable=_Hm2DevSecStatusTable_Object((1,3,6,1,4,1,248,11,22,1,3,3,10))
if mibBuilder.loadTexts:hm2DevSecStatusTable.setStatus(_A)
_Hm2DevSecStatusEntry_Object=MibTableRow
hm2DevSecStatusEntry=_Hm2DevSecStatusEntry_Object((1,3,6,1,4,1,248,11,22,1,3,3,10,1))
hm2DevSecStatusEntry.setIndexNames((0,_F,_A5))
if mibBuilder.loadTexts:hm2DevSecStatusEntry.setStatus(_A)
_Hm2DevSecStatusIndex_Type=Integer32
_Hm2DevSecStatusIndex_Object=MibTableColumn
hm2DevSecStatusIndex=_Hm2DevSecStatusIndex_Object((1,3,6,1,4,1,248,11,22,1,3,3,10,1,1),_Hm2DevSecStatusIndex_Type())
hm2DevSecStatusIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:hm2DevSecStatusIndex.setStatus(_A)
_Hm2DevSecStatusTimeStamp_Type=HmTimeSeconds1970
_Hm2DevSecStatusTimeStamp_Object=MibTableColumn
hm2DevSecStatusTimeStamp=_Hm2DevSecStatusTimeStamp_Object((1,3,6,1,4,1,248,11,22,1,3,3,10,1,2),_Hm2DevSecStatusTimeStamp_Type())
hm2DevSecStatusTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DevSecStatusTimeStamp.setStatus(_A)
class _Hm2DevSecStatusTrapCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,29)));namedValues=NamedValues(*((_M,1),(_X,10),(_Y,11),(_Z,12),(_a,13),(_b,14),(_c,15),(_d,16),(_e,17),(_f,18),(_g,19),(_h,20),(_i,21),(_v,22),(_j,23),(_k,24),(_l,25),(_m,26),(_t,29)))
_Hm2DevSecStatusTrapCause_Type.__name__=_D
_Hm2DevSecStatusTrapCause_Object=MibTableColumn
hm2DevSecStatusTrapCause=_Hm2DevSecStatusTrapCause_Object((1,3,6,1,4,1,248,11,22,1,3,3,10,1,3),_Hm2DevSecStatusTrapCause_Type())
hm2DevSecStatusTrapCause.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DevSecStatusTrapCause.setStatus(_A)
_Hm2DevSecStatusTrapCauseIndex_Type=Integer32
_Hm2DevSecStatusTrapCauseIndex_Object=MibTableColumn
hm2DevSecStatusTrapCauseIndex=_Hm2DevSecStatusTrapCauseIndex_Object((1,3,6,1,4,1,248,11,22,1,3,3,10,1,4),_Hm2DevSecStatusTrapCauseIndex_Type())
hm2DevSecStatusTrapCauseIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DevSecStatusTrapCauseIndex.setStatus(_A)
_Hm2DiagLedGroup_ObjectIdentity=ObjectIdentity
hm2DiagLedGroup=_Hm2DiagLedGroup_ObjectIdentity((1,3,6,1,4,1,248,11,22,1,4))
_Hm2LedGlobalTable_Object=MibTable
hm2LedGlobalTable=_Hm2LedGlobalTable_Object((1,3,6,1,4,1,248,11,22,1,4,1))
if mibBuilder.loadTexts:hm2LedGlobalTable.setStatus(_A)
_Hm2LedGlobalEntry_Object=MibTableRow
hm2LedGlobalEntry=_Hm2LedGlobalEntry_Object((1,3,6,1,4,1,248,11,22,1,4,1,1))
hm2LedGlobalEntry.setIndexNames((0,_F,_A6))
if mibBuilder.loadTexts:hm2LedGlobalEntry.setStatus(_A)
_Hm2LedGlobalLedType_Type=Hm2LedType
_Hm2LedGlobalLedType_Object=MibTableColumn
hm2LedGlobalLedType=_Hm2LedGlobalLedType_Object((1,3,6,1,4,1,248,11,22,1,4,1,1,1),_Hm2LedGlobalLedType_Type())
hm2LedGlobalLedType.setMaxAccess(_O)
if mibBuilder.loadTexts:hm2LedGlobalLedType.setStatus(_A)
_Hm2LedGlobalStatus_Type=Hm2LedStatus
_Hm2LedGlobalStatus_Object=MibTableColumn
hm2LedGlobalStatus=_Hm2LedGlobalStatus_Object((1,3,6,1,4,1,248,11,22,1,4,1,1,2),_Hm2LedGlobalStatus_Type())
hm2LedGlobalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LedGlobalStatus.setStatus(_A)
_Hm2LedPortTable_Object=MibTable
hm2LedPortTable=_Hm2LedPortTable_Object((1,3,6,1,4,1,248,11,22,1,4,2))
if mibBuilder.loadTexts:hm2LedPortTable.setStatus(_A)
_Hm2LedPortEntry_Object=MibTableRow
hm2LedPortEntry=_Hm2LedPortEntry_Object((1,3,6,1,4,1,248,11,22,1,4,2,1))
hm2LedPortEntry.setIndexNames((0,_w,_x))
if mibBuilder.loadTexts:hm2LedPortEntry.setStatus(_A)
_Hm2LedPortStatus_Type=Hm2LedStatus
_Hm2LedPortStatus_Object=MibTableColumn
hm2LedPortStatus=_Hm2LedPortStatus_Object((1,3,6,1,4,1,248,11,22,1,4,2,1,1),_Hm2LedPortStatus_Type())
hm2LedPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LedPortStatus.setStatus(_A)
_Hm2LedPortPoeStatus_Type=Hm2LedStatus
_Hm2LedPortPoeStatus_Object=MibTableColumn
hm2LedPortPoeStatus=_Hm2LedPortPoeStatus_Object((1,3,6,1,4,1,248,11,22,1,4,2,1,2),_Hm2LedPortPoeStatus_Type())
hm2LedPortPoeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LedPortPoeStatus.setStatus(_A)
class _Hm2LedPortSignaling_Type(HmEnabledStatus):defaultValue=2
_Hm2LedPortSignaling_Type.__name__=_E
_Hm2LedPortSignaling_Object=MibTableColumn
hm2LedPortSignaling=_Hm2LedPortSignaling_Object((1,3,6,1,4,1,248,11,22,1,4,2,1,3),_Hm2LedPortSignaling_Type())
hm2LedPortSignaling.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LedPortSignaling.setStatus(_A)
_Hm2LedControlGroup_ObjectIdentity=ObjectIdentity
hm2LedControlGroup=_Hm2LedControlGroup_ObjectIdentity((1,3,6,1,4,1,248,11,22,1,4,3))
class _Hm2LedPortMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('portpanel',0),('servicepanel',1)))
_Hm2LedPortMode_Type.__name__=_D
_Hm2LedPortMode_Object=MibScalar
hm2LedPortMode=_Hm2LedPortMode_Object((1,3,6,1,4,1,248,11,22,1,4,3,1),_Hm2LedPortMode_Type())
hm2LedPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LedPortMode.setStatus(_A)
_Hm2DiagIfaceUtilizationGroup_ObjectIdentity=ObjectIdentity
hm2DiagIfaceUtilizationGroup=_Hm2DiagIfaceUtilizationGroup_ObjectIdentity((1,3,6,1,4,1,248,11,22,1,5))
_Hm2DiagIfaceUtilizationTable_Object=MibTable
hm2DiagIfaceUtilizationTable=_Hm2DiagIfaceUtilizationTable_Object((1,3,6,1,4,1,248,11,22,1,5,1))
if mibBuilder.loadTexts:hm2DiagIfaceUtilizationTable.setStatus(_A)
_Hm2DiagIfaceUtilizationEntry_Object=MibTableRow
hm2DiagIfaceUtilizationEntry=_Hm2DiagIfaceUtilizationEntry_Object((1,3,6,1,4,1,248,11,22,1,5,1,1))
hm2DiagIfaceUtilizationEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hm2DiagIfaceUtilizationEntry.setStatus(_A)
class _Hm2DiagIfaceUtilization_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_Hm2DiagIfaceUtilization_Type.__name__=_D
_Hm2DiagIfaceUtilization_Object=MibTableColumn
hm2DiagIfaceUtilization=_Hm2DiagIfaceUtilization_Object((1,3,6,1,4,1,248,11,22,1,5,1,1,1),_Hm2DiagIfaceUtilization_Type())
hm2DiagIfaceUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DiagIfaceUtilization.setStatus(_A)
class _Hm2DiagIfaceUtilizationControlInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_Hm2DiagIfaceUtilizationControlInterval_Type.__name__=_D
_Hm2DiagIfaceUtilizationControlInterval_Object=MibTableColumn
hm2DiagIfaceUtilizationControlInterval=_Hm2DiagIfaceUtilizationControlInterval_Object((1,3,6,1,4,1,248,11,22,1,5,1,1,2),_Hm2DiagIfaceUtilizationControlInterval_Type())
hm2DiagIfaceUtilizationControlInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DiagIfaceUtilizationControlInterval.setStatus(_A)
class _Hm2DiagIfaceUtilizationAlarmLowerThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_Hm2DiagIfaceUtilizationAlarmLowerThreshold_Type.__name__=_D
_Hm2DiagIfaceUtilizationAlarmLowerThreshold_Object=MibTableColumn
hm2DiagIfaceUtilizationAlarmLowerThreshold=_Hm2DiagIfaceUtilizationAlarmLowerThreshold_Object((1,3,6,1,4,1,248,11,22,1,5,1,1,3),_Hm2DiagIfaceUtilizationAlarmLowerThreshold_Type())
hm2DiagIfaceUtilizationAlarmLowerThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DiagIfaceUtilizationAlarmLowerThreshold.setStatus(_A)
class _Hm2DiagIfaceUtilizationAlarmUpperThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_Hm2DiagIfaceUtilizationAlarmUpperThreshold_Type.__name__=_D
_Hm2DiagIfaceUtilizationAlarmUpperThreshold_Object=MibTableColumn
hm2DiagIfaceUtilizationAlarmUpperThreshold=_Hm2DiagIfaceUtilizationAlarmUpperThreshold_Object((1,3,6,1,4,1,248,11,22,1,5,1,1,4),_Hm2DiagIfaceUtilizationAlarmUpperThreshold_Type())
hm2DiagIfaceUtilizationAlarmUpperThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DiagIfaceUtilizationAlarmUpperThreshold.setStatus(_A)
_Hm2DiagIfaceUtilizationAlarmCondition_Type=TruthValue
_Hm2DiagIfaceUtilizationAlarmCondition_Object=MibTableColumn
hm2DiagIfaceUtilizationAlarmCondition=_Hm2DiagIfaceUtilizationAlarmCondition_Object((1,3,6,1,4,1,248,11,22,1,5,1,1,5),_Hm2DiagIfaceUtilizationAlarmCondition_Type())
hm2DiagIfaceUtilizationAlarmCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DiagIfaceUtilizationAlarmCondition.setStatus(_A)
_Hm2DiagEgressIfaceUtilizationTable_Object=MibTable
hm2DiagEgressIfaceUtilizationTable=_Hm2DiagEgressIfaceUtilizationTable_Object((1,3,6,1,4,1,248,11,22,1,5,2))
if mibBuilder.loadTexts:hm2DiagEgressIfaceUtilizationTable.setStatus(_A)
_Hm2DiagEgressIfaceUtilizationEntry_Object=MibTableRow
hm2DiagEgressIfaceUtilizationEntry=_Hm2DiagEgressIfaceUtilizationEntry_Object((1,3,6,1,4,1,248,11,22,1,5,2,1))
hm2DiagEgressIfaceUtilizationEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hm2DiagEgressIfaceUtilizationEntry.setStatus(_A)
class _Hm2DiagEgressIfaceUtilization_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_Hm2DiagEgressIfaceUtilization_Type.__name__=_D
_Hm2DiagEgressIfaceUtilization_Object=MibTableColumn
hm2DiagEgressIfaceUtilization=_Hm2DiagEgressIfaceUtilization_Object((1,3,6,1,4,1,248,11,22,1,5,2,1,1),_Hm2DiagEgressIfaceUtilization_Type())
hm2DiagEgressIfaceUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DiagEgressIfaceUtilization.setStatus(_A)
class _Hm2DiagEgressIfaceUtilizationControlInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_Hm2DiagEgressIfaceUtilizationControlInterval_Type.__name__=_D
_Hm2DiagEgressIfaceUtilizationControlInterval_Object=MibTableColumn
hm2DiagEgressIfaceUtilizationControlInterval=_Hm2DiagEgressIfaceUtilizationControlInterval_Object((1,3,6,1,4,1,248,11,22,1,5,2,1,2),_Hm2DiagEgressIfaceUtilizationControlInterval_Type())
hm2DiagEgressIfaceUtilizationControlInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DiagEgressIfaceUtilizationControlInterval.setStatus(_A)
class _Hm2DiagEgressIfaceUtilizationAlarmLowerThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_Hm2DiagEgressIfaceUtilizationAlarmLowerThreshold_Type.__name__=_D
_Hm2DiagEgressIfaceUtilizationAlarmLowerThreshold_Object=MibTableColumn
hm2DiagEgressIfaceUtilizationAlarmLowerThreshold=_Hm2DiagEgressIfaceUtilizationAlarmLowerThreshold_Object((1,3,6,1,4,1,248,11,22,1,5,2,1,3),_Hm2DiagEgressIfaceUtilizationAlarmLowerThreshold_Type())
hm2DiagEgressIfaceUtilizationAlarmLowerThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DiagEgressIfaceUtilizationAlarmLowerThreshold.setStatus(_A)
class _Hm2DiagEgressIfaceUtilizationAlarmUpperThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_Hm2DiagEgressIfaceUtilizationAlarmUpperThreshold_Type.__name__=_D
_Hm2DiagEgressIfaceUtilizationAlarmUpperThreshold_Object=MibTableColumn
hm2DiagEgressIfaceUtilizationAlarmUpperThreshold=_Hm2DiagEgressIfaceUtilizationAlarmUpperThreshold_Object((1,3,6,1,4,1,248,11,22,1,5,2,1,4),_Hm2DiagEgressIfaceUtilizationAlarmUpperThreshold_Type())
hm2DiagEgressIfaceUtilizationAlarmUpperThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DiagEgressIfaceUtilizationAlarmUpperThreshold.setStatus(_A)
_Hm2DiagEgressIfaceUtilizationAlarmCondition_Type=TruthValue
_Hm2DiagEgressIfaceUtilizationAlarmCondition_Object=MibTableColumn
hm2DiagEgressIfaceUtilizationAlarmCondition=_Hm2DiagEgressIfaceUtilizationAlarmCondition_Object((1,3,6,1,4,1,248,11,22,1,5,2,1,5),_Hm2DiagEgressIfaceUtilizationAlarmCondition_Type())
hm2DiagEgressIfaceUtilizationAlarmCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DiagEgressIfaceUtilizationAlarmCondition.setStatus(_A)
_Hm2DiagCableTesterGroup_ObjectIdentity=ObjectIdentity
hm2DiagCableTesterGroup=_Hm2DiagCableTesterGroup_ObjectIdentity((1,3,6,1,4,1,248,11,22,1,6))
class _Hm2DiagCableTesterStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('active',1),('success',2),('failure',3),('uninitialized',4)))
_Hm2DiagCableTesterStatus_Type.__name__=_D
_Hm2DiagCableTesterStatus_Object=MibScalar
hm2DiagCableTesterStatus=_Hm2DiagCableTesterStatus_Object((1,3,6,1,4,1,248,11,22,1,6,1),_Hm2DiagCableTesterStatus_Type())
hm2DiagCableTesterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DiagCableTesterStatus.setStatus(_A)
class _Hm2DiagCableTesterIfIndex_Type(Unsigned32):defaultValue=0
_Hm2DiagCableTesterIfIndex_Type.__name__=_N
_Hm2DiagCableTesterIfIndex_Object=MibScalar
hm2DiagCableTesterIfIndex=_Hm2DiagCableTesterIfIndex_Object((1,3,6,1,4,1,248,11,22,1,6,2),_Hm2DiagCableTesterIfIndex_Type())
hm2DiagCableTesterIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DiagCableTesterIfIndex.setStatus(_A)
_Hm2DiagCableTesterCableTable_Object=MibTable
hm2DiagCableTesterCableTable=_Hm2DiagCableTesterCableTable_Object((1,3,6,1,4,1,248,11,22,1,6,10))
if mibBuilder.loadTexts:hm2DiagCableTesterCableTable.setStatus(_A)
_Hm2DiagCableTesterCableEntry_Object=MibTableRow
hm2DiagCableTesterCableEntry=_Hm2DiagCableTesterCableEntry_Object((1,3,6,1,4,1,248,11,22,1,6,10,1))
hm2DiagCableTesterCableEntry.setIndexNames((0,_F,_A7))
if mibBuilder.loadTexts:hm2DiagCableTesterCableEntry.setStatus(_A)
class _Hm2DiagCableTesterCablePair_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Hm2DiagCableTesterCablePair_Type.__name__=_D
_Hm2DiagCableTesterCablePair_Object=MibTableColumn
hm2DiagCableTesterCablePair=_Hm2DiagCableTesterCablePair_Object((1,3,6,1,4,1,248,11,22,1,6,10,1,1),_Hm2DiagCableTesterCablePair_Type())
hm2DiagCableTesterCablePair.setMaxAccess(_O)
if mibBuilder.loadTexts:hm2DiagCableTesterCablePair.setStatus(_A)
class _Hm2DiagCableTesterCableStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normal',1),(_u,2),('short',3),('unknown',4)))
_Hm2DiagCableTesterCableStatus_Type.__name__=_D
_Hm2DiagCableTesterCableStatus_Object=MibTableColumn
hm2DiagCableTesterCableStatus=_Hm2DiagCableTesterCableStatus_Object((1,3,6,1,4,1,248,11,22,1,6,10,1,2),_Hm2DiagCableTesterCableStatus_Type())
hm2DiagCableTesterCableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DiagCableTesterCableStatus.setStatus(_A)
class _Hm2DiagCableTesterCableMinimumLength_Type(Unsigned32):defaultValue=0
_Hm2DiagCableTesterCableMinimumLength_Type.__name__=_N
_Hm2DiagCableTesterCableMinimumLength_Object=MibTableColumn
hm2DiagCableTesterCableMinimumLength=_Hm2DiagCableTesterCableMinimumLength_Object((1,3,6,1,4,1,248,11,22,1,6,10,1,3),_Hm2DiagCableTesterCableMinimumLength_Type())
hm2DiagCableTesterCableMinimumLength.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DiagCableTesterCableMinimumLength.setStatus(_A)
class _Hm2DiagCableTesterCableMaximumLength_Type(Unsigned32):defaultValue=0
_Hm2DiagCableTesterCableMaximumLength_Type.__name__=_N
_Hm2DiagCableTesterCableMaximumLength_Object=MibTableColumn
hm2DiagCableTesterCableMaximumLength=_Hm2DiagCableTesterCableMaximumLength_Object((1,3,6,1,4,1,248,11,22,1,6,10,1,4),_Hm2DiagCableTesterCableMaximumLength_Type())
hm2DiagCableTesterCableMaximumLength.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DiagCableTesterCableMaximumLength.setStatus(_A)
class _Hm2DiagCableTesterCableFailureLocation_Type(Unsigned32):defaultValue=0
_Hm2DiagCableTesterCableFailureLocation_Type.__name__=_N
_Hm2DiagCableTesterCableFailureLocation_Object=MibTableColumn
hm2DiagCableTesterCableFailureLocation=_Hm2DiagCableTesterCableFailureLocation_Object((1,3,6,1,4,1,248,11,22,1,6,10,1,5),_Hm2DiagCableTesterCableFailureLocation_Type())
hm2DiagCableTesterCableFailureLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DiagCableTesterCableFailureLocation.setStatus(_A)
_Hm2PortMonitorGroup_ObjectIdentity=ObjectIdentity
hm2PortMonitorGroup=_Hm2PortMonitorGroup_ObjectIdentity((1,3,6,1,4,1,248,11,22,1,7))
class _Hm2PortMonitorAdminMode_Type(TruthValue):defaultValue=2
_Hm2PortMonitorAdminMode_Type.__name__=_I
_Hm2PortMonitorAdminMode_Object=MibScalar
hm2PortMonitorAdminMode=_Hm2PortMonitorAdminMode_Object((1,3,6,1,4,1,248,11,22,1,7,1),_Hm2PortMonitorAdminMode_Type())
hm2PortMonitorAdminMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortMonitorAdminMode.setStatus(_A)
_Hm2PortMonitorIntfTable_Object=MibTable
hm2PortMonitorIntfTable=_Hm2PortMonitorIntfTable_Object((1,3,6,1,4,1,248,11,22,1,7,2))
if mibBuilder.loadTexts:hm2PortMonitorIntfTable.setStatus(_A)
_Hm2PortMonitorIntfEntry_Object=MibTableRow
hm2PortMonitorIntfEntry=_Hm2PortMonitorIntfEntry_Object((1,3,6,1,4,1,248,11,22,1,7,2,1))
hm2PortMonitorIntfEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hm2PortMonitorIntfEntry.setStatus(_A)
class _Hm2PortMonitorIntfReset_Type(TruthValue):defaultValue=2
_Hm2PortMonitorIntfReset_Type.__name__=_I
_Hm2PortMonitorIntfReset_Object=MibTableColumn
hm2PortMonitorIntfReset=_Hm2PortMonitorIntfReset_Object((1,3,6,1,4,1,248,11,22,1,7,2,1,2),_Hm2PortMonitorIntfReset_Type())
hm2PortMonitorIntfReset.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortMonitorIntfReset.setStatus(_A)
class _Hm2PortMonitorIntfAction_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('port-disable',1),('trap-only',2),('auto-disable',3)))
_Hm2PortMonitorIntfAction_Type.__name__=_D
_Hm2PortMonitorIntfAction_Object=MibTableColumn
hm2PortMonitorIntfAction=_Hm2PortMonitorIntfAction_Object((1,3,6,1,4,1,248,11,22,1,7,2,1,3),_Hm2PortMonitorIntfAction_Type())
hm2PortMonitorIntfAction.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortMonitorIntfAction.setStatus(_A)
_Hm2PortMonitorConditionGroup_ObjectIdentity=ObjectIdentity
hm2PortMonitorConditionGroup=_Hm2PortMonitorConditionGroup_ObjectIdentity((1,3,6,1,4,1,248,11,22,1,7,3))
_Hm2PortMonitorConditionIntfTable_Object=MibTable
hm2PortMonitorConditionIntfTable=_Hm2PortMonitorConditionIntfTable_Object((1,3,6,1,4,1,248,11,22,1,7,3,1))
if mibBuilder.loadTexts:hm2PortMonitorConditionIntfTable.setStatus(_A)
_Hm2PortMonitorConditionIntfEntry_Object=MibTableRow
hm2PortMonitorConditionIntfEntry=_Hm2PortMonitorConditionIntfEntry_Object((1,3,6,1,4,1,248,11,22,1,7,3,1,1))
hm2PortMonitorConditionIntfEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hm2PortMonitorConditionIntfEntry.setStatus(_A)
class _Hm2PortMonitorConditionField_Type(Bits):namedValues=NamedValues(*((_M,0),('link-flap',1),('crcFragments',2),('duplexMismatch',3),('overload-detection',4),('speed-duplex',5)))
_Hm2PortMonitorConditionField_Type.__name__=_r
_Hm2PortMonitorConditionField_Object=MibTableColumn
hm2PortMonitorConditionField=_Hm2PortMonitorConditionField_Object((1,3,6,1,4,1,248,11,22,1,7,3,1,1,1),_Hm2PortMonitorConditionField_Type())
hm2PortMonitorConditionField.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PortMonitorConditionField.setStatus(_A)
class _Hm2PortMonitorConditionLinkFlapMode_Type(TruthValue):defaultValue=2
_Hm2PortMonitorConditionLinkFlapMode_Type.__name__=_I
_Hm2PortMonitorConditionLinkFlapMode_Object=MibTableColumn
hm2PortMonitorConditionLinkFlapMode=_Hm2PortMonitorConditionLinkFlapMode_Object((1,3,6,1,4,1,248,11,22,1,7,3,1,1,2),_Hm2PortMonitorConditionLinkFlapMode_Type())
hm2PortMonitorConditionLinkFlapMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortMonitorConditionLinkFlapMode.setStatus(_A)
class _Hm2PortMonitorConditionCrcFragmentsMode_Type(TruthValue):defaultValue=2
_Hm2PortMonitorConditionCrcFragmentsMode_Type.__name__=_I
_Hm2PortMonitorConditionCrcFragmentsMode_Object=MibTableColumn
hm2PortMonitorConditionCrcFragmentsMode=_Hm2PortMonitorConditionCrcFragmentsMode_Object((1,3,6,1,4,1,248,11,22,1,7,3,1,1,3),_Hm2PortMonitorConditionCrcFragmentsMode_Type())
hm2PortMonitorConditionCrcFragmentsMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortMonitorConditionCrcFragmentsMode.setStatus(_A)
class _Hm2PortMonitorConditionDuplexMismatchDetectionMode_Type(TruthValue):defaultValue=2
_Hm2PortMonitorConditionDuplexMismatchDetectionMode_Type.__name__=_I
_Hm2PortMonitorConditionDuplexMismatchDetectionMode_Object=MibTableColumn
hm2PortMonitorConditionDuplexMismatchDetectionMode=_Hm2PortMonitorConditionDuplexMismatchDetectionMode_Object((1,3,6,1,4,1,248,11,22,1,7,3,1,1,4),_Hm2PortMonitorConditionDuplexMismatchDetectionMode_Type())
hm2PortMonitorConditionDuplexMismatchDetectionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortMonitorConditionDuplexMismatchDetectionMode.setStatus(_A)
class _Hm2PortMonitorConditionOverloadDetectionMode_Type(TruthValue):defaultValue=2
_Hm2PortMonitorConditionOverloadDetectionMode_Type.__name__=_I
_Hm2PortMonitorConditionOverloadDetectionMode_Object=MibTableColumn
hm2PortMonitorConditionOverloadDetectionMode=_Hm2PortMonitorConditionOverloadDetectionMode_Object((1,3,6,1,4,1,248,11,22,1,7,3,1,1,5),_Hm2PortMonitorConditionOverloadDetectionMode_Type())
hm2PortMonitorConditionOverloadDetectionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortMonitorConditionOverloadDetectionMode.setStatus(_A)
class _Hm2PortMonitorConditionSpeedDuplexMode_Type(TruthValue):defaultValue=2
_Hm2PortMonitorConditionSpeedDuplexMode_Type.__name__=_I
_Hm2PortMonitorConditionSpeedDuplexMode_Object=MibTableColumn
hm2PortMonitorConditionSpeedDuplexMode=_Hm2PortMonitorConditionSpeedDuplexMode_Object((1,3,6,1,4,1,248,11,22,1,7,3,1,1,6),_Hm2PortMonitorConditionSpeedDuplexMode_Type())
hm2PortMonitorConditionSpeedDuplexMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortMonitorConditionSpeedDuplexMode.setStatus(_A)
_Hm2PortMonitorConditionLinkFlapGroup_ObjectIdentity=ObjectIdentity
hm2PortMonitorConditionLinkFlapGroup=_Hm2PortMonitorConditionLinkFlapGroup_ObjectIdentity((1,3,6,1,4,1,248,11,22,1,7,3,2))
_Hm2PortMonitorConditionLinkFlapIntfTable_Object=MibTable
hm2PortMonitorConditionLinkFlapIntfTable=_Hm2PortMonitorConditionLinkFlapIntfTable_Object((1,3,6,1,4,1,248,11,22,1,7,3,2,1))
if mibBuilder.loadTexts:hm2PortMonitorConditionLinkFlapIntfTable.setStatus(_A)
_Hm2PortMonitorConditionLinkFlapIntfEntry_Object=MibTableRow
hm2PortMonitorConditionLinkFlapIntfEntry=_Hm2PortMonitorConditionLinkFlapIntfEntry_Object((1,3,6,1,4,1,248,11,22,1,7,3,2,1,1))
hm2PortMonitorConditionLinkFlapIntfEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hm2PortMonitorConditionLinkFlapIntfEntry.setStatus(_A)
class _Hm2PortMonitorConditionLinkFlapInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,180))
_Hm2PortMonitorConditionLinkFlapInterval_Type.__name__=_D
_Hm2PortMonitorConditionLinkFlapInterval_Object=MibTableColumn
hm2PortMonitorConditionLinkFlapInterval=_Hm2PortMonitorConditionLinkFlapInterval_Object((1,3,6,1,4,1,248,11,22,1,7,3,2,1,1,1),_Hm2PortMonitorConditionLinkFlapInterval_Type())
hm2PortMonitorConditionLinkFlapInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortMonitorConditionLinkFlapInterval.setStatus(_A)
class _Hm2PortMonitorConditionLinkFlapCount_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_Hm2PortMonitorConditionLinkFlapCount_Type.__name__=_D
_Hm2PortMonitorConditionLinkFlapCount_Object=MibTableColumn
hm2PortMonitorConditionLinkFlapCount=_Hm2PortMonitorConditionLinkFlapCount_Object((1,3,6,1,4,1,248,11,22,1,7,3,2,1,1,2),_Hm2PortMonitorConditionLinkFlapCount_Type())
hm2PortMonitorConditionLinkFlapCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortMonitorConditionLinkFlapCount.setStatus(_A)
_Hm2PortMonitorConditionLinkFlapCountInterval_Type=Integer32
_Hm2PortMonitorConditionLinkFlapCountInterval_Object=MibTableColumn
hm2PortMonitorConditionLinkFlapCountInterval=_Hm2PortMonitorConditionLinkFlapCountInterval_Object((1,3,6,1,4,1,248,11,22,1,7,3,2,1,1,3),_Hm2PortMonitorConditionLinkFlapCountInterval_Type())
hm2PortMonitorConditionLinkFlapCountInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PortMonitorConditionLinkFlapCountInterval.setStatus(_A)
_Hm2PortMonitorConditionLinkFlapCountTotal_Type=Integer32
_Hm2PortMonitorConditionLinkFlapCountTotal_Object=MibTableColumn
hm2PortMonitorConditionLinkFlapCountTotal=_Hm2PortMonitorConditionLinkFlapCountTotal_Object((1,3,6,1,4,1,248,11,22,1,7,3,2,1,1,4),_Hm2PortMonitorConditionLinkFlapCountTotal_Type())
hm2PortMonitorConditionLinkFlapCountTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PortMonitorConditionLinkFlapCountTotal.setStatus(_A)
_Hm2PortMonitorConditionCrcFragmentsGroup_ObjectIdentity=ObjectIdentity
hm2PortMonitorConditionCrcFragmentsGroup=_Hm2PortMonitorConditionCrcFragmentsGroup_ObjectIdentity((1,3,6,1,4,1,248,11,22,1,7,3,3))
_Hm2PortMonitorConditionCrcFragmentsIntfTable_Object=MibTable
hm2PortMonitorConditionCrcFragmentsIntfTable=_Hm2PortMonitorConditionCrcFragmentsIntfTable_Object((1,3,6,1,4,1,248,11,22,1,7,3,3,1))
if mibBuilder.loadTexts:hm2PortMonitorConditionCrcFragmentsIntfTable.setStatus(_A)
_Hm2PortMonitorConditionCrcFragmentsIntfEntry_Object=MibTableRow
hm2PortMonitorConditionCrcFragmentsIntfEntry=_Hm2PortMonitorConditionCrcFragmentsIntfEntry_Object((1,3,6,1,4,1,248,11,22,1,7,3,3,1,1))
hm2PortMonitorConditionCrcFragmentsIntfEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hm2PortMonitorConditionCrcFragmentsIntfEntry.setStatus(_A)
class _Hm2PortMonitorConditionCrcFragmentsInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,180))
_Hm2PortMonitorConditionCrcFragmentsInterval_Type.__name__=_D
_Hm2PortMonitorConditionCrcFragmentsInterval_Object=MibTableColumn
hm2PortMonitorConditionCrcFragmentsInterval=_Hm2PortMonitorConditionCrcFragmentsInterval_Object((1,3,6,1,4,1,248,11,22,1,7,3,3,1,1,1),_Hm2PortMonitorConditionCrcFragmentsInterval_Type())
hm2PortMonitorConditionCrcFragmentsInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortMonitorConditionCrcFragmentsInterval.setStatus(_A)
class _Hm2PortMonitorConditionCrcFragmentsCount_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000000))
_Hm2PortMonitorConditionCrcFragmentsCount_Type.__name__=_D
_Hm2PortMonitorConditionCrcFragmentsCount_Object=MibTableColumn
hm2PortMonitorConditionCrcFragmentsCount=_Hm2PortMonitorConditionCrcFragmentsCount_Object((1,3,6,1,4,1,248,11,22,1,7,3,3,1,1,2),_Hm2PortMonitorConditionCrcFragmentsCount_Type())
hm2PortMonitorConditionCrcFragmentsCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortMonitorConditionCrcFragmentsCount.setStatus(_A)
_Hm2PortMonitorConditionCrcFragmentsCountInterval_Type=Integer32
_Hm2PortMonitorConditionCrcFragmentsCountInterval_Object=MibTableColumn
hm2PortMonitorConditionCrcFragmentsCountInterval=_Hm2PortMonitorConditionCrcFragmentsCountInterval_Object((1,3,6,1,4,1,248,11,22,1,7,3,3,1,1,3),_Hm2PortMonitorConditionCrcFragmentsCountInterval_Type())
hm2PortMonitorConditionCrcFragmentsCountInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PortMonitorConditionCrcFragmentsCountInterval.setStatus(_A)
_Hm2PortMonitorConditionCrcFragmentsCountTotal_Type=Integer32
_Hm2PortMonitorConditionCrcFragmentsCountTotal_Object=MibTableColumn
hm2PortMonitorConditionCrcFragmentsCountTotal=_Hm2PortMonitorConditionCrcFragmentsCountTotal_Object((1,3,6,1,4,1,248,11,22,1,7,3,3,1,1,4),_Hm2PortMonitorConditionCrcFragmentsCountTotal_Type())
hm2PortMonitorConditionCrcFragmentsCountTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PortMonitorConditionCrcFragmentsCountTotal.setStatus(_A)
_Hm2PortMonitorConditionOverloadDetectionGroup_ObjectIdentity=ObjectIdentity
hm2PortMonitorConditionOverloadDetectionGroup=_Hm2PortMonitorConditionOverloadDetectionGroup_ObjectIdentity((1,3,6,1,4,1,248,11,22,1,7,3,4))
_Hm2PortMonitorConditionOvldDetIntfTable_Object=MibTable
hm2PortMonitorConditionOvldDetIntfTable=_Hm2PortMonitorConditionOvldDetIntfTable_Object((1,3,6,1,4,1,248,11,22,1,7,3,4,1))
if mibBuilder.loadTexts:hm2PortMonitorConditionOvldDetIntfTable.setStatus(_A)
_Hm2PortMonitorConditionOvldDetIntfEntry_Object=MibTableRow
hm2PortMonitorConditionOvldDetIntfEntry=_Hm2PortMonitorConditionOvldDetIntfEntry_Object((1,3,6,1,4,1,248,11,22,1,7,3,4,1,1))
hm2PortMonitorConditionOvldDetIntfEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hm2PortMonitorConditionOvldDetIntfEntry.setStatus(_A)
class _Hm2PortMonitorConditionOvldDetTrfcType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('all',1),('bc',2),('bc-mc',3)))
_Hm2PortMonitorConditionOvldDetTrfcType_Type.__name__=_D
_Hm2PortMonitorConditionOvldDetTrfcType_Object=MibTableColumn
hm2PortMonitorConditionOvldDetTrfcType=_Hm2PortMonitorConditionOvldDetTrfcType_Object((1,3,6,1,4,1,248,11,22,1,7,3,4,1,1,1),_Hm2PortMonitorConditionOvldDetTrfcType_Type())
hm2PortMonitorConditionOvldDetTrfcType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortMonitorConditionOvldDetTrfcType.setStatus(_A)
class _Hm2PortMonitorConditionOvldDetTholdType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pps',1),('kbps',2)))
_Hm2PortMonitorConditionOvldDetTholdType_Type.__name__=_D
_Hm2PortMonitorConditionOvldDetTholdType_Object=MibTableColumn
hm2PortMonitorConditionOvldDetTholdType=_Hm2PortMonitorConditionOvldDetTholdType_Object((1,3,6,1,4,1,248,11,22,1,7,3,4,1,1,2),_Hm2PortMonitorConditionOvldDetTholdType_Type())
hm2PortMonitorConditionOvldDetTholdType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortMonitorConditionOvldDetTholdType.setStatus(_A)
class _Hm2PortMonitorConditionOvldDetLwrTholdVal_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_Hm2PortMonitorConditionOvldDetLwrTholdVal_Type.__name__=_D
_Hm2PortMonitorConditionOvldDetLwrTholdVal_Object=MibTableColumn
hm2PortMonitorConditionOvldDetLwrTholdVal=_Hm2PortMonitorConditionOvldDetLwrTholdVal_Object((1,3,6,1,4,1,248,11,22,1,7,3,4,1,1,3),_Hm2PortMonitorConditionOvldDetLwrTholdVal_Type())
hm2PortMonitorConditionOvldDetLwrTholdVal.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortMonitorConditionOvldDetLwrTholdVal.setStatus(_A)
class _Hm2PortMonitorConditionOvldDetUprTholdVal_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_Hm2PortMonitorConditionOvldDetUprTholdVal_Type.__name__=_D
_Hm2PortMonitorConditionOvldDetUprTholdVal_Object=MibTableColumn
hm2PortMonitorConditionOvldDetUprTholdVal=_Hm2PortMonitorConditionOvldDetUprTholdVal_Object((1,3,6,1,4,1,248,11,22,1,7,3,4,1,1,4),_Hm2PortMonitorConditionOvldDetUprTholdVal_Type())
hm2PortMonitorConditionOvldDetUprTholdVal.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortMonitorConditionOvldDetUprTholdVal.setStatus(_A)
class _Hm2PortMonitorConditionOvldDetIntvl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_Hm2PortMonitorConditionOvldDetIntvl_Type.__name__=_D
_Hm2PortMonitorConditionOvldDetIntvl_Object=MibTableColumn
hm2PortMonitorConditionOvldDetIntvl=_Hm2PortMonitorConditionOvldDetIntvl_Object((1,3,6,1,4,1,248,11,22,1,7,3,4,1,1,5),_Hm2PortMonitorConditionOvldDetIntvl_Type())
hm2PortMonitorConditionOvldDetIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortMonitorConditionOvldDetIntvl.setStatus(_A)
class _Hm2PortMonitorConditionOvldDetPkgCntAll_Type(Integer32):defaultValue=0
_Hm2PortMonitorConditionOvldDetPkgCntAll_Type.__name__=_D
_Hm2PortMonitorConditionOvldDetPkgCntAll_Object=MibTableColumn
hm2PortMonitorConditionOvldDetPkgCntAll=_Hm2PortMonitorConditionOvldDetPkgCntAll_Object((1,3,6,1,4,1,248,11,22,1,7,3,4,1,1,6),_Hm2PortMonitorConditionOvldDetPkgCntAll_Type())
hm2PortMonitorConditionOvldDetPkgCntAll.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PortMonitorConditionOvldDetPkgCntAll.setStatus(_A)
class _Hm2PortMonitorConditionOvldDetPkgCntBC_Type(Integer32):defaultValue=0
_Hm2PortMonitorConditionOvldDetPkgCntBC_Type.__name__=_D
_Hm2PortMonitorConditionOvldDetPkgCntBC_Object=MibTableColumn
hm2PortMonitorConditionOvldDetPkgCntBC=_Hm2PortMonitorConditionOvldDetPkgCntBC_Object((1,3,6,1,4,1,248,11,22,1,7,3,4,1,1,7),_Hm2PortMonitorConditionOvldDetPkgCntBC_Type())
hm2PortMonitorConditionOvldDetPkgCntBC.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PortMonitorConditionOvldDetPkgCntBC.setStatus(_A)
class _Hm2PortMonitorConditionOvldDetPkgCntMC_Type(Integer32):defaultValue=0
_Hm2PortMonitorConditionOvldDetPkgCntMC_Type.__name__=_D
_Hm2PortMonitorConditionOvldDetPkgCntMC_Object=MibTableColumn
hm2PortMonitorConditionOvldDetPkgCntMC=_Hm2PortMonitorConditionOvldDetPkgCntMC_Object((1,3,6,1,4,1,248,11,22,1,7,3,4,1,1,8),_Hm2PortMonitorConditionOvldDetPkgCntMC_Type())
hm2PortMonitorConditionOvldDetPkgCntMC.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PortMonitorConditionOvldDetPkgCntMC.setStatus(_A)
class _Hm2PortMonitorConditionOvldDetPkgCntKbit_Type(Integer32):defaultValue=0
_Hm2PortMonitorConditionOvldDetPkgCntKbit_Type.__name__=_D
_Hm2PortMonitorConditionOvldDetPkgCntKbit_Object=MibTableColumn
hm2PortMonitorConditionOvldDetPkgCntKbit=_Hm2PortMonitorConditionOvldDetPkgCntKbit_Object((1,3,6,1,4,1,248,11,22,1,7,3,4,1,1,9),_Hm2PortMonitorConditionOvldDetPkgCntKbit_Type())
hm2PortMonitorConditionOvldDetPkgCntKbit.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PortMonitorConditionOvldDetPkgCntKbit.setStatus(_A)
_Hm2PortMonitorConditionSpeedDuplexGroup_ObjectIdentity=ObjectIdentity
hm2PortMonitorConditionSpeedDuplexGroup=_Hm2PortMonitorConditionSpeedDuplexGroup_ObjectIdentity((1,3,6,1,4,1,248,11,22,1,7,3,5))
_Hm2PortMonitorConditionSpeedDuplexTable_Object=MibTable
hm2PortMonitorConditionSpeedDuplexTable=_Hm2PortMonitorConditionSpeedDuplexTable_Object((1,3,6,1,4,1,248,11,22,1,7,3,5,1))
if mibBuilder.loadTexts:hm2PortMonitorConditionSpeedDuplexTable.setStatus(_A)
_Hm2PortMonitorConditionSpeedDuplexEntry_Object=MibTableRow
hm2PortMonitorConditionSpeedDuplexEntry=_Hm2PortMonitorConditionSpeedDuplexEntry_Object((1,3,6,1,4,1,248,11,22,1,7,3,5,1,1))
hm2PortMonitorConditionSpeedDuplexEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hm2PortMonitorConditionSpeedDuplexEntry.setStatus(_A)
class _Hm2PortMonitorConditionSpeedDuplexValue_Type(Bits):defaultBinValue='11111111';namedValues=NamedValues(*(('hdx-10',0),('fdx-10',1),('hdx-100',2),('fdx-100',3),('hdx-1000',4),('fdx-1000',5),('fdx-2500',6),('fdx-10000',7)))
_Hm2PortMonitorConditionSpeedDuplexValue_Type.__name__=_r
_Hm2PortMonitorConditionSpeedDuplexValue_Object=MibTableColumn
hm2PortMonitorConditionSpeedDuplexValue=_Hm2PortMonitorConditionSpeedDuplexValue_Object((1,3,6,1,4,1,248,11,22,1,7,3,5,1,1,1),_Hm2PortMonitorConditionSpeedDuplexValue_Type())
hm2PortMonitorConditionSpeedDuplexValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortMonitorConditionSpeedDuplexValue.setStatus(_A)
_Hm2KbpsUnitTrafficTypeInvalid_ObjectIdentity=ObjectIdentity
hm2KbpsUnitTrafficTypeInvalid=_Hm2KbpsUnitTrafficTypeInvalid_ObjectIdentity((1,3,6,1,4,1,248,11,22,1,7,4))
if mibBuilder.loadTexts:hm2KbpsUnitTrafficTypeInvalid.setStatus(_A)
_Hm2DiagResourcesGroup_ObjectIdentity=ObjectIdentity
hm2DiagResourcesGroup=_Hm2DiagResourcesGroup_ObjectIdentity((1,3,6,1,4,1,248,11,22,1,8))
class _Hm2DiagEnableMeasurement_Type(HmEnabledStatus):defaultValue=1
_Hm2DiagEnableMeasurement_Type.__name__=_E
_Hm2DiagEnableMeasurement_Object=MibScalar
hm2DiagEnableMeasurement=_Hm2DiagEnableMeasurement_Object((1,3,6,1,4,1,248,11,22,1,8,1),_Hm2DiagEnableMeasurement_Type())
hm2DiagEnableMeasurement.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DiagEnableMeasurement.setStatus(_A)
_Hm2DiagCpuResourcesGroup_ObjectIdentity=ObjectIdentity
hm2DiagCpuResourcesGroup=_Hm2DiagCpuResourcesGroup_ObjectIdentity((1,3,6,1,4,1,248,11,22,1,8,10))
class _Hm2DiagCpuUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Hm2DiagCpuUtilization_Type.__name__=_D
_Hm2DiagCpuUtilization_Object=MibScalar
hm2DiagCpuUtilization=_Hm2DiagCpuUtilization_Object((1,3,6,1,4,1,248,11,22,1,8,10,1),_Hm2DiagCpuUtilization_Type())
hm2DiagCpuUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DiagCpuUtilization.setStatus(_A)
if mibBuilder.loadTexts:hm2DiagCpuUtilization.setUnits('percent')
class _Hm2DiagCpuAverageUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Hm2DiagCpuAverageUtilization_Type.__name__=_D
_Hm2DiagCpuAverageUtilization_Object=MibScalar
hm2DiagCpuAverageUtilization=_Hm2DiagCpuAverageUtilization_Object((1,3,6,1,4,1,248,11,22,1,8,10,2),_Hm2DiagCpuAverageUtilization_Type())
hm2DiagCpuAverageUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DiagCpuAverageUtilization.setStatus(_A)
if mibBuilder.loadTexts:hm2DiagCpuAverageUtilization.setUnits('percent')
class _Hm2DiagCpuRunningProcesses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32768))
_Hm2DiagCpuRunningProcesses_Type.__name__=_D
_Hm2DiagCpuRunningProcesses_Object=MibScalar
hm2DiagCpuRunningProcesses=_Hm2DiagCpuRunningProcesses_Object((1,3,6,1,4,1,248,11,22,1,8,10,3),_Hm2DiagCpuRunningProcesses_Type())
hm2DiagCpuRunningProcesses.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DiagCpuRunningProcesses.setStatus(_A)
class _Hm2DiagCpuMaxRunningProcesses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32768))
_Hm2DiagCpuMaxRunningProcesses_Type.__name__=_D
_Hm2DiagCpuMaxRunningProcesses_Object=MibScalar
hm2DiagCpuMaxRunningProcesses=_Hm2DiagCpuMaxRunningProcesses_Object((1,3,6,1,4,1,248,11,22,1,8,10,4),_Hm2DiagCpuMaxRunningProcesses_Type())
hm2DiagCpuMaxRunningProcesses.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DiagCpuMaxRunningProcesses.setStatus(_A)
_Hm2DiagMemoryResourcesGroup_ObjectIdentity=ObjectIdentity
hm2DiagMemoryResourcesGroup=_Hm2DiagMemoryResourcesGroup_ObjectIdentity((1,3,6,1,4,1,248,11,22,1,8,11))
class _Hm2DiagMemoryRamAllocated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Hm2DiagMemoryRamAllocated_Type.__name__=_D
_Hm2DiagMemoryRamAllocated_Object=MibScalar
hm2DiagMemoryRamAllocated=_Hm2DiagMemoryRamAllocated_Object((1,3,6,1,4,1,248,11,22,1,8,11,1),_Hm2DiagMemoryRamAllocated_Type())
hm2DiagMemoryRamAllocated.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DiagMemoryRamAllocated.setStatus(_A)
if mibBuilder.loadTexts:hm2DiagMemoryRamAllocated.setUnits(_L)
class _Hm2DiagMemoryRamFree_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Hm2DiagMemoryRamFree_Type.__name__=_D
_Hm2DiagMemoryRamFree_Object=MibScalar
hm2DiagMemoryRamFree=_Hm2DiagMemoryRamFree_Object((1,3,6,1,4,1,248,11,22,1,8,11,2),_Hm2DiagMemoryRamFree_Type())
hm2DiagMemoryRamFree.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DiagMemoryRamFree.setStatus(_A)
if mibBuilder.loadTexts:hm2DiagMemoryRamFree.setUnits(_L)
class _Hm2DiagMemoryRamAllocatedAverage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Hm2DiagMemoryRamAllocatedAverage_Type.__name__=_D
_Hm2DiagMemoryRamAllocatedAverage_Object=MibScalar
hm2DiagMemoryRamAllocatedAverage=_Hm2DiagMemoryRamAllocatedAverage_Object((1,3,6,1,4,1,248,11,22,1,8,11,3),_Hm2DiagMemoryRamAllocatedAverage_Type())
hm2DiagMemoryRamAllocatedAverage.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DiagMemoryRamAllocatedAverage.setStatus(_A)
if mibBuilder.loadTexts:hm2DiagMemoryRamAllocatedAverage.setUnits(_L)
class _Hm2DiagMemoryRamFreeAverage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Hm2DiagMemoryRamFreeAverage_Type.__name__=_D
_Hm2DiagMemoryRamFreeAverage_Object=MibScalar
hm2DiagMemoryRamFreeAverage=_Hm2DiagMemoryRamFreeAverage_Object((1,3,6,1,4,1,248,11,22,1,8,11,4),_Hm2DiagMemoryRamFreeAverage_Type())
hm2DiagMemoryRamFreeAverage.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DiagMemoryRamFreeAverage.setStatus(_A)
if mibBuilder.loadTexts:hm2DiagMemoryRamFreeAverage.setUnits(_L)
class _Hm2DiagMemoryRawFlashMainAllocated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Hm2DiagMemoryRawFlashMainAllocated_Type.__name__=_D
_Hm2DiagMemoryRawFlashMainAllocated_Object=MibScalar
hm2DiagMemoryRawFlashMainAllocated=_Hm2DiagMemoryRawFlashMainAllocated_Object((1,3,6,1,4,1,248,11,22,1,8,11,10),_Hm2DiagMemoryRawFlashMainAllocated_Type())
hm2DiagMemoryRawFlashMainAllocated.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DiagMemoryRawFlashMainAllocated.setStatus(_A)
if mibBuilder.loadTexts:hm2DiagMemoryRawFlashMainAllocated.setUnits(_L)
class _Hm2DiagMemoryRawFlashMainFree_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Hm2DiagMemoryRawFlashMainFree_Type.__name__=_D
_Hm2DiagMemoryRawFlashMainFree_Object=MibScalar
hm2DiagMemoryRawFlashMainFree=_Hm2DiagMemoryRawFlashMainFree_Object((1,3,6,1,4,1,248,11,22,1,8,11,11),_Hm2DiagMemoryRawFlashMainFree_Type())
hm2DiagMemoryRawFlashMainFree.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DiagMemoryRawFlashMainFree.setStatus(_A)
if mibBuilder.loadTexts:hm2DiagMemoryRawFlashMainFree.setUnits(_L)
class _Hm2DiagMemoryFlashFileSystemAllocated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Hm2DiagMemoryFlashFileSystemAllocated_Type.__name__=_D
_Hm2DiagMemoryFlashFileSystemAllocated_Object=MibScalar
hm2DiagMemoryFlashFileSystemAllocated=_Hm2DiagMemoryFlashFileSystemAllocated_Object((1,3,6,1,4,1,248,11,22,1,8,11,12),_Hm2DiagMemoryFlashFileSystemAllocated_Type())
hm2DiagMemoryFlashFileSystemAllocated.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DiagMemoryFlashFileSystemAllocated.setStatus(_A)
if mibBuilder.loadTexts:hm2DiagMemoryFlashFileSystemAllocated.setUnits(_L)
class _Hm2DiagMemoryFlashFileSystemFree_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Hm2DiagMemoryFlashFileSystemFree_Type.__name__=_D
_Hm2DiagMemoryFlashFileSystemFree_Object=MibScalar
hm2DiagMemoryFlashFileSystemFree=_Hm2DiagMemoryFlashFileSystemFree_Object((1,3,6,1,4,1,248,11,22,1,8,11,13),_Hm2DiagMemoryFlashFileSystemFree_Type())
hm2DiagMemoryFlashFileSystemFree.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DiagMemoryFlashFileSystemFree.setStatus(_A)
if mibBuilder.loadTexts:hm2DiagMemoryFlashFileSystemFree.setUnits(_L)
_Hm2DiagNetworkResourcesGroup_ObjectIdentity=ObjectIdentity
hm2DiagNetworkResourcesGroup=_Hm2DiagNetworkResourcesGroup_ObjectIdentity((1,3,6,1,4,1,248,11,22,1,8,12))
class _Hm2DiagNetworkCpuIfUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Hm2DiagNetworkCpuIfUtilization_Type.__name__=_D
_Hm2DiagNetworkCpuIfUtilization_Object=MibScalar
hm2DiagNetworkCpuIfUtilization=_Hm2DiagNetworkCpuIfUtilization_Object((1,3,6,1,4,1,248,11,22,1,8,12,1),_Hm2DiagNetworkCpuIfUtilization_Type())
hm2DiagNetworkCpuIfUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DiagNetworkCpuIfUtilization.setStatus(_A)
if mibBuilder.loadTexts:hm2DiagNetworkCpuIfUtilization.setUnits('precent')
class _Hm2DiagNetworkCpuIfAverageUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Hm2DiagNetworkCpuIfAverageUtilization_Type.__name__=_D
_Hm2DiagNetworkCpuIfAverageUtilization_Object=MibScalar
hm2DiagNetworkCpuIfAverageUtilization=_Hm2DiagNetworkCpuIfAverageUtilization_Object((1,3,6,1,4,1,248,11,22,1,8,12,2),_Hm2DiagNetworkCpuIfAverageUtilization_Type())
hm2DiagNetworkCpuIfAverageUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DiagNetworkCpuIfAverageUtilization.setStatus(_A)
if mibBuilder.loadTexts:hm2DiagNetworkCpuIfAverageUtilization.setUnits('precent')
_Hm2DiagnosticSNMPExtensionGroup_ObjectIdentity=ObjectIdentity
hm2DiagnosticSNMPExtensionGroup=_Hm2DiagnosticSNMPExtensionGroup_ObjectIdentity((1,3,6,1,4,1,248,11,22,3))
_Hm2PortMonitorSpeedDuplexErrorReturn_ObjectIdentity=ObjectIdentity
hm2PortMonitorSpeedDuplexErrorReturn=_Hm2PortMonitorSpeedDuplexErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,11,22,3,1))
if mibBuilder.loadTexts:hm2PortMonitorSpeedDuplexErrorReturn.setStatus(_A)
_Hm2PortMonitorCndOvldDetInconsistenTholdVal_ObjectIdentity=ObjectIdentity
hm2PortMonitorCndOvldDetInconsistenTholdVal=_Hm2PortMonitorCndOvldDetInconsistenTholdVal_ObjectIdentity((1,3,6,1,4,1,248,11,22,3,2))
if mibBuilder.loadTexts:hm2PortMonitorCndOvldDetInconsistenTholdVal.setStatus(_A)
hm2SigConStateChangeTrap=NotificationType((1,3,6,1,4,1,248,11,22,0,1))
hm2SigConStateChangeTrap.setObjects(*((_F,_J),(_F,_A8),(_F,_A9),(_F,_AA)))
if mibBuilder.loadTexts:hm2SigConStateChangeTrap.setStatus(_A)
hm2DevMonStateChangeTrap=NotificationType((1,3,6,1,4,1,248,11,22,0,2))
hm2DevMonStateChangeTrap.setObjects(*((_F,_K),(_F,_AB),(_F,_AC),(_F,_AD)))
if mibBuilder.loadTexts:hm2DevMonStateChangeTrap.setStatus(_A)
hm2DevSecStateChangeTrap=NotificationType((1,3,6,1,4,1,248,11,22,0,3))
hm2DevSecStateChangeTrap.setObjects(*((_F,_AE),(_F,_AF),(_F,_AG)))
if mibBuilder.loadTexts:hm2DevSecStateChangeTrap.setStatus(_A)
hm2DiagSelftestActionTrap=NotificationType((1,3,6,1,4,1,248,11,22,0,4))
hm2DiagSelftestActionTrap.setObjects((_F,_s))
if mibBuilder.loadTexts:hm2DiagSelftestActionTrap.setStatus(_A)
hm2DiagIfaceUtilizationTrap=NotificationType((1,3,6,1,4,1,248,11,22,0,5))
hm2DiagIfaceUtilizationTrap.setObjects(*((_F,_AH),(_F,_AI)))
if mibBuilder.loadTexts:hm2DiagIfaceUtilizationTrap.setStatus(_A)
hm2PortMonitorPortTrap=NotificationType((1,3,6,1,4,1,248,11,22,0,6))
hm2PortMonitorPortTrap.setObjects(*((_G,_H),(_F,_AJ)))
if mibBuilder.loadTexts:hm2PortMonitorPortTrap.setStatus(_A)
hm2DiagEgressIfaceUtilizationTrap=NotificationType((1,3,6,1,4,1,248,11,22,0,7))
hm2DiagEgressIfaceUtilizationTrap.setObjects(*((_F,_AK),(_F,_AL)))
if mibBuilder.loadTexts:hm2DiagEgressIfaceUtilizationTrap.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'Hm2LedType':Hm2LedType,'Hm2LedStatus':Hm2LedStatus,'hm2DiagnosticMib':hm2DiagnosticMib,'hm2DiagnosticMibNotifications':hm2DiagnosticMibNotifications,'hm2SigConStateChangeTrap':hm2SigConStateChangeTrap,'hm2DevMonStateChangeTrap':hm2DevMonStateChangeTrap,'hm2DevSecStateChangeTrap':hm2DevSecStateChangeTrap,'hm2DiagSelftestActionTrap':hm2DiagSelftestActionTrap,'hm2DiagIfaceUtilizationTrap':hm2DiagIfaceUtilizationTrap,'hm2PortMonitorPortTrap':hm2PortMonitorPortTrap,'hm2DiagEgressIfaceUtilizationTrap':hm2DiagEgressIfaceUtilizationTrap,'hm2DiagnosticMibObjects':hm2DiagnosticMibObjects,'hm2DiagSelftestGroup':hm2DiagSelftestGroup,'hm2DiagSelftestRAM':hm2DiagSelftestRAM,'hm2DiagSelftestBootTime':hm2DiagSelftestBootTime,'hm2DiagSelftestActionTable':hm2DiagSelftestActionTable,'hm2DiagSelftestActionEntry':hm2DiagSelftestActionEntry,_s:hm2DiagSelftestActionCause,'hm2DiagSelftestAction':hm2DiagSelftestAction,'hm2DiagBootGroup':hm2DiagBootGroup,'hm2BootSystemMonitor':hm2BootSystemMonitor,'hm2BootDefaultConfigOnError':hm2BootDefaultConfigOnError,'hm2BootConfigPushButton':hm2BootConfigPushButton,'hm2DiagDeviceMonitorGroup':hm2DiagDeviceMonitorGroup,'hm2SignalContactGroup':hm2SignalContactGroup,'hm2SigConCommonTable':hm2SigConCommonTable,'hm2SigConCommonEntry':hm2SigConCommonEntry,_J:hm2SigConID,'hm2SigConTrapEnable':hm2SigConTrapEnable,_A9:hm2SigConTrapCause,_AA:hm2SigConTrapCauseIndex,'hm2SigConMode':hm2SigConMode,_A8:hm2SigConOperState,'hm2SigConOperTimeStamp':hm2SigConOperTimeStamp,'hm2SigConManualActivate':hm2SigConManualActivate,'hm2SigConSenseLinkFailure':hm2SigConSenseLinkFailure,'hm2SigConSenseTemperature':hm2SigConSenseTemperature,'hm2SigConSenseFan':hm2SigConSenseFan,'hm2SigConSenseModuleRemoval':hm2SigConSenseModuleRemoval,'hm2SigConSenseExtNvmRemoval':hm2SigConSenseExtNvmRemoval,'hm2SigConSenseExtNvmNotInSync':hm2SigConSenseExtNvmNotInSync,'hm2SigConSenseRingRedundancy':hm2SigConSenseRingRedundancy,'hm2SigConSenseEthernetLoops':hm2SigConSenseEthernetLoops,'hm2SigConSenseHumidity':hm2SigConSenseHumidity,'hm2SigConSenseStpPortBlock':hm2SigConSenseStpPortBlock,'hm2SigConPSTable':hm2SigConPSTable,'hm2SigConPSEntry':hm2SigConPSEntry,'hm2SigConSensePSState':hm2SigConSensePSState,'hm2SigConInterfaceTable':hm2SigConInterfaceTable,'hm2SigConInterfaceEntry':hm2SigConInterfaceEntry,'hm2SigConSenseIfLinkAlarm':hm2SigConSenseIfLinkAlarm,'hm2SigConModuleTable':hm2SigConModuleTable,'hm2SigConModuleEntry':hm2SigConModuleEntry,_z:hm2SigConModID,'hm2SigConSenseModule':hm2SigConSenseModule,'hm2SigConFanModuleTable':hm2SigConFanModuleTable,'hm2SigConFanModuleEntry':hm2SigConFanModuleEntry,_A0:hm2SigConFanModID,'hm2SigConSenseFanModule':hm2SigConSenseFanModule,'hm2SigConStatusTable':hm2SigConStatusTable,'hm2SigConStatusEntry':hm2SigConStatusEntry,_A1:hm2SigConStatusIndex,'hm2SigConStatusTimeStamp':hm2SigConStatusTimeStamp,'hm2SigConStatusTrapCause':hm2SigConStatusTrapCause,'hm2SigConStatusTrapCauseIndex':hm2SigConStatusTrapCauseIndex,'hm2DeviceMonitorGroup':hm2DeviceMonitorGroup,'hm2DevMonCommonTable':hm2DevMonCommonTable,'hm2DevMonCommonEntry':hm2DevMonCommonEntry,_K:hm2DevMonID,'hm2DevMonTrapEnable':hm2DevMonTrapEnable,_AC:hm2DevMonTrapCause,_AD:hm2DevMonTrapCauseIndex,_AB:hm2DevMonOperState,'hm2DevMonOperTimeStamp':hm2DevMonOperTimeStamp,'hm2DevMonSenseLinkFailure':hm2DevMonSenseLinkFailure,'hm2DevMonSenseTemperature':hm2DevMonSenseTemperature,'hm2DevMonSenseFan':hm2DevMonSenseFan,'hm2DevMonSenseModuleRemoval':hm2DevMonSenseModuleRemoval,'hm2DevMonSenseExtNvmRemoval':hm2DevMonSenseExtNvmRemoval,'hm2DevMonSenseExtNvmNotInSync':hm2DevMonSenseExtNvmNotInSync,'hm2DevMonSenseRingRedundancy':hm2DevMonSenseRingRedundancy,'hm2DevMonSenseHumidity':hm2DevMonSenseHumidity,'hm2DevMonSenseStpPortBlock':hm2DevMonSenseStpPortBlock,'hm2DevMonPSTable':hm2DevMonPSTable,'hm2DevMonPSEntry':hm2DevMonPSEntry,'hm2DevMonSensePSState':hm2DevMonSensePSState,'hm2DevMonInterfaceTable':hm2DevMonInterfaceTable,'hm2DevMonInterfaceEntry':hm2DevMonInterfaceEntry,'hm2DevMonSenseIfLinkAlarm':hm2DevMonSenseIfLinkAlarm,'hm2DevMonModuleTable':hm2DevMonModuleTable,'hm2DevMonModuleEntry':hm2DevMonModuleEntry,_A2:hm2DevMonModID,'hm2DevMonSenseModule':hm2DevMonSenseModule,'hm2DevMonFanModuleTable':hm2DevMonFanModuleTable,'hm2DevMonFanModuleEntry':hm2DevMonFanModuleEntry,_A3:hm2DevMonFanModID,'hm2DevMonSenseFanModule':hm2DevMonSenseFanModule,'hm2DevMonStatusTable':hm2DevMonStatusTable,'hm2DevMonStatusEntry':hm2DevMonStatusEntry,_A4:hm2DevMonStatusIndex,'hm2DevMonStatusTimeStamp':hm2DevMonStatusTimeStamp,'hm2DevMonStatusTrapCause':hm2DevMonStatusTrapCause,'hm2DevMonStatusTrapCauseIndex':hm2DevMonStatusTrapCauseIndex,'hm2DeviceSecurityGroup':hm2DeviceSecurityGroup,'hm2DevSecConfigGroup':hm2DevSecConfigGroup,'hm2DevSecTrapEnable':hm2DevSecTrapEnable,_AF:hm2DevSecTrapCause,_AG:hm2DevSecTrapCauseIndex,_AE:hm2DevSecOperState,'hm2DevSecOperTimeStamp':hm2DevSecOperTimeStamp,'hm2DevSecSensePasswordChange':hm2DevSecSensePasswordChange,'hm2DevSecSensePasswordMinLength':hm2DevSecSensePasswordMinLength,'hm2DevSecSensePasswordStrengthNotConfigured':hm2DevSecSensePasswordStrengthNotConfigured,'hm2DevSecSenseBypassPasswordStrength':hm2DevSecSenseBypassPasswordStrength,'hm2DevSecSenseTelnetEnabled':hm2DevSecSenseTelnetEnabled,'hm2DevSecSenseHttpEnabled':hm2DevSecSenseHttpEnabled,'hm2DevSecSenseSnmpUnsecure':hm2DevSecSenseSnmpUnsecure,'hm2DevSecSenseSysmonEnabled':hm2DevSecSenseSysmonEnabled,'hm2DevSecSenseExtNvmUpdateEnabled':hm2DevSecSenseExtNvmUpdateEnabled,'hm2DevSecSenseNoLinkEnabled':hm2DevSecSenseNoLinkEnabled,'hm2DevSecSenseHiDiscoveryEnabled':hm2DevSecSenseHiDiscoveryEnabled,'hm2DevSecSenseExtNvmConfigLoadUnsecure':hm2DevSecSenseExtNvmConfigLoadUnsecure,'hm2DevSecSenseIec61850MmsEnabled':hm2DevSecSenseIec61850MmsEnabled,'hm2DevSecSenseHttpsCertificateWarning':hm2DevSecSenseHttpsCertificateWarning,'hm2DevSecSenseModbusTcpEnabled':hm2DevSecSenseModbusTcpEnabled,'hm2DevSecSenseEtherNetIpEnabled':hm2DevSecSenseEtherNetIpEnabled,'hm2DevSecSenseProfinetIOEnabled':hm2DevSecSenseProfinetIOEnabled,'hm2DevSecSensePMLDisabled':hm2DevSecSensePMLDisabled,'hm2DevSecInterfaceTable':hm2DevSecInterfaceTable,'hm2DevSecInterfaceEntry':hm2DevSecInterfaceEntry,'hm2DevSecSenseIfNoLink':hm2DevSecSenseIfNoLink,'hm2DevSecStatusTable':hm2DevSecStatusTable,'hm2DevSecStatusEntry':hm2DevSecStatusEntry,_A5:hm2DevSecStatusIndex,'hm2DevSecStatusTimeStamp':hm2DevSecStatusTimeStamp,'hm2DevSecStatusTrapCause':hm2DevSecStatusTrapCause,'hm2DevSecStatusTrapCauseIndex':hm2DevSecStatusTrapCauseIndex,'hm2DiagLedGroup':hm2DiagLedGroup,'hm2LedGlobalTable':hm2LedGlobalTable,'hm2LedGlobalEntry':hm2LedGlobalEntry,_A6:hm2LedGlobalLedType,'hm2LedGlobalStatus':hm2LedGlobalStatus,'hm2LedPortTable':hm2LedPortTable,'hm2LedPortEntry':hm2LedPortEntry,'hm2LedPortStatus':hm2LedPortStatus,'hm2LedPortPoeStatus':hm2LedPortPoeStatus,'hm2LedPortSignaling':hm2LedPortSignaling,'hm2LedControlGroup':hm2LedControlGroup,'hm2LedPortMode':hm2LedPortMode,'hm2DiagIfaceUtilizationGroup':hm2DiagIfaceUtilizationGroup,'hm2DiagIfaceUtilizationTable':hm2DiagIfaceUtilizationTable,'hm2DiagIfaceUtilizationEntry':hm2DiagIfaceUtilizationEntry,_AH:hm2DiagIfaceUtilization,'hm2DiagIfaceUtilizationControlInterval':hm2DiagIfaceUtilizationControlInterval,'hm2DiagIfaceUtilizationAlarmLowerThreshold':hm2DiagIfaceUtilizationAlarmLowerThreshold,'hm2DiagIfaceUtilizationAlarmUpperThreshold':hm2DiagIfaceUtilizationAlarmUpperThreshold,_AI:hm2DiagIfaceUtilizationAlarmCondition,'hm2DiagEgressIfaceUtilizationTable':hm2DiagEgressIfaceUtilizationTable,'hm2DiagEgressIfaceUtilizationEntry':hm2DiagEgressIfaceUtilizationEntry,_AK:hm2DiagEgressIfaceUtilization,'hm2DiagEgressIfaceUtilizationControlInterval':hm2DiagEgressIfaceUtilizationControlInterval,'hm2DiagEgressIfaceUtilizationAlarmLowerThreshold':hm2DiagEgressIfaceUtilizationAlarmLowerThreshold,'hm2DiagEgressIfaceUtilizationAlarmUpperThreshold':hm2DiagEgressIfaceUtilizationAlarmUpperThreshold,_AL:hm2DiagEgressIfaceUtilizationAlarmCondition,'hm2DiagCableTesterGroup':hm2DiagCableTesterGroup,'hm2DiagCableTesterStatus':hm2DiagCableTesterStatus,'hm2DiagCableTesterIfIndex':hm2DiagCableTesterIfIndex,'hm2DiagCableTesterCableTable':hm2DiagCableTesterCableTable,'hm2DiagCableTesterCableEntry':hm2DiagCableTesterCableEntry,_A7:hm2DiagCableTesterCablePair,'hm2DiagCableTesterCableStatus':hm2DiagCableTesterCableStatus,'hm2DiagCableTesterCableMinimumLength':hm2DiagCableTesterCableMinimumLength,'hm2DiagCableTesterCableMaximumLength':hm2DiagCableTesterCableMaximumLength,'hm2DiagCableTesterCableFailureLocation':hm2DiagCableTesterCableFailureLocation,'hm2PortMonitorGroup':hm2PortMonitorGroup,'hm2PortMonitorAdminMode':hm2PortMonitorAdminMode,'hm2PortMonitorIntfTable':hm2PortMonitorIntfTable,'hm2PortMonitorIntfEntry':hm2PortMonitorIntfEntry,'hm2PortMonitorIntfReset':hm2PortMonitorIntfReset,'hm2PortMonitorIntfAction':hm2PortMonitorIntfAction,'hm2PortMonitorConditionGroup':hm2PortMonitorConditionGroup,'hm2PortMonitorConditionIntfTable':hm2PortMonitorConditionIntfTable,'hm2PortMonitorConditionIntfEntry':hm2PortMonitorConditionIntfEntry,_AJ:hm2PortMonitorConditionField,'hm2PortMonitorConditionLinkFlapMode':hm2PortMonitorConditionLinkFlapMode,'hm2PortMonitorConditionCrcFragmentsMode':hm2PortMonitorConditionCrcFragmentsMode,'hm2PortMonitorConditionDuplexMismatchDetectionMode':hm2PortMonitorConditionDuplexMismatchDetectionMode,'hm2PortMonitorConditionOverloadDetectionMode':hm2PortMonitorConditionOverloadDetectionMode,'hm2PortMonitorConditionSpeedDuplexMode':hm2PortMonitorConditionSpeedDuplexMode,'hm2PortMonitorConditionLinkFlapGroup':hm2PortMonitorConditionLinkFlapGroup,'hm2PortMonitorConditionLinkFlapIntfTable':hm2PortMonitorConditionLinkFlapIntfTable,'hm2PortMonitorConditionLinkFlapIntfEntry':hm2PortMonitorConditionLinkFlapIntfEntry,'hm2PortMonitorConditionLinkFlapInterval':hm2PortMonitorConditionLinkFlapInterval,'hm2PortMonitorConditionLinkFlapCount':hm2PortMonitorConditionLinkFlapCount,'hm2PortMonitorConditionLinkFlapCountInterval':hm2PortMonitorConditionLinkFlapCountInterval,'hm2PortMonitorConditionLinkFlapCountTotal':hm2PortMonitorConditionLinkFlapCountTotal,'hm2PortMonitorConditionCrcFragmentsGroup':hm2PortMonitorConditionCrcFragmentsGroup,'hm2PortMonitorConditionCrcFragmentsIntfTable':hm2PortMonitorConditionCrcFragmentsIntfTable,'hm2PortMonitorConditionCrcFragmentsIntfEntry':hm2PortMonitorConditionCrcFragmentsIntfEntry,'hm2PortMonitorConditionCrcFragmentsInterval':hm2PortMonitorConditionCrcFragmentsInterval,'hm2PortMonitorConditionCrcFragmentsCount':hm2PortMonitorConditionCrcFragmentsCount,'hm2PortMonitorConditionCrcFragmentsCountInterval':hm2PortMonitorConditionCrcFragmentsCountInterval,'hm2PortMonitorConditionCrcFragmentsCountTotal':hm2PortMonitorConditionCrcFragmentsCountTotal,'hm2PortMonitorConditionOverloadDetectionGroup':hm2PortMonitorConditionOverloadDetectionGroup,'hm2PortMonitorConditionOvldDetIntfTable':hm2PortMonitorConditionOvldDetIntfTable,'hm2PortMonitorConditionOvldDetIntfEntry':hm2PortMonitorConditionOvldDetIntfEntry,'hm2PortMonitorConditionOvldDetTrfcType':hm2PortMonitorConditionOvldDetTrfcType,'hm2PortMonitorConditionOvldDetTholdType':hm2PortMonitorConditionOvldDetTholdType,'hm2PortMonitorConditionOvldDetLwrTholdVal':hm2PortMonitorConditionOvldDetLwrTholdVal,'hm2PortMonitorConditionOvldDetUprTholdVal':hm2PortMonitorConditionOvldDetUprTholdVal,'hm2PortMonitorConditionOvldDetIntvl':hm2PortMonitorConditionOvldDetIntvl,'hm2PortMonitorConditionOvldDetPkgCntAll':hm2PortMonitorConditionOvldDetPkgCntAll,'hm2PortMonitorConditionOvldDetPkgCntBC':hm2PortMonitorConditionOvldDetPkgCntBC,'hm2PortMonitorConditionOvldDetPkgCntMC':hm2PortMonitorConditionOvldDetPkgCntMC,'hm2PortMonitorConditionOvldDetPkgCntKbit':hm2PortMonitorConditionOvldDetPkgCntKbit,'hm2PortMonitorConditionSpeedDuplexGroup':hm2PortMonitorConditionSpeedDuplexGroup,'hm2PortMonitorConditionSpeedDuplexTable':hm2PortMonitorConditionSpeedDuplexTable,'hm2PortMonitorConditionSpeedDuplexEntry':hm2PortMonitorConditionSpeedDuplexEntry,'hm2PortMonitorConditionSpeedDuplexValue':hm2PortMonitorConditionSpeedDuplexValue,'hm2KbpsUnitTrafficTypeInvalid':hm2KbpsUnitTrafficTypeInvalid,'hm2DiagResourcesGroup':hm2DiagResourcesGroup,'hm2DiagEnableMeasurement':hm2DiagEnableMeasurement,'hm2DiagCpuResourcesGroup':hm2DiagCpuResourcesGroup,'hm2DiagCpuUtilization':hm2DiagCpuUtilization,'hm2DiagCpuAverageUtilization':hm2DiagCpuAverageUtilization,'hm2DiagCpuRunningProcesses':hm2DiagCpuRunningProcesses,'hm2DiagCpuMaxRunningProcesses':hm2DiagCpuMaxRunningProcesses,'hm2DiagMemoryResourcesGroup':hm2DiagMemoryResourcesGroup,'hm2DiagMemoryRamAllocated':hm2DiagMemoryRamAllocated,'hm2DiagMemoryRamFree':hm2DiagMemoryRamFree,'hm2DiagMemoryRamAllocatedAverage':hm2DiagMemoryRamAllocatedAverage,'hm2DiagMemoryRamFreeAverage':hm2DiagMemoryRamFreeAverage,'hm2DiagMemoryRawFlashMainAllocated':hm2DiagMemoryRawFlashMainAllocated,'hm2DiagMemoryRawFlashMainFree':hm2DiagMemoryRawFlashMainFree,'hm2DiagMemoryFlashFileSystemAllocated':hm2DiagMemoryFlashFileSystemAllocated,'hm2DiagMemoryFlashFileSystemFree':hm2DiagMemoryFlashFileSystemFree,'hm2DiagNetworkResourcesGroup':hm2DiagNetworkResourcesGroup,'hm2DiagNetworkCpuIfUtilization':hm2DiagNetworkCpuIfUtilization,'hm2DiagNetworkCpuIfAverageUtilization':hm2DiagNetworkCpuIfAverageUtilization,'hm2DiagnosticSNMPExtensionGroup':hm2DiagnosticSNMPExtensionGroup,'hm2PortMonitorSpeedDuplexErrorReturn':hm2PortMonitorSpeedDuplexErrorReturn,'hm2PortMonitorCndOvldDetInconsistenTholdVal':hm2PortMonitorCndOvldDetInconsistenTholdVal})