_BV='cooOtsOchNotifEnableGroup'
_BU='cooOtsPowerGroup'
_BT='cooOtsEquipmentAlarmInfoGroup'
_BS='cooOtsOchNotifGroup'
_BR='cooOtsNotifGroup'
_BQ='cooOtsNotifEnableGroup'
_BP='cooOtsIntervalGroup'
_BO='cooOtsCurrentGroup'
_BN='cooOtsThresholdGroup'
_BM='cooOtsOchControllerGroup'
_BL='cooOtsControllerGroup'
_BK='cooOtsOchGroup'
_BJ='cooOtsGroup'
_BI='cooOtsOchStatusChange'
_BH='cooOtsStatusChange'
_BG='cooOtsOchNotifEnabled'
_BF='cooOtsNotifEnabled'
_BE='cooIntervalTimestamp'
_BD='cooCurrentTimestamp'
_BC='cooThreshLBCEnableMax'
_BB='cooThreshRXPowerEnableMax'
_BA='cooThreshTXPowerEnableMax'
_B9='cooThreshLBCEnableMin'
_B8='cooThreshRXPowerEnableMin'
_B7='cooThreshTXPowerEnableMin'
_B6='cooOtsOchControllerWidth'
_B5='cooOtsOchControllerTranspAdminState'
_B4='cooOtsOchControllerState'
_B3='cooOtsOchControllerChannelNumber'
_B2='cooOtsOchControllerFrequency'
_B1='cooOtsOchControllerWavelength'
_B0='cooOtsOchControllerTXPower'
_A_='cooOtsOchControllerRXPower'
_Az='cooOtsOchControllerLaserStatus'
_Ay='cooOtsControllerTXSpanLoss'
_Ax='cooOtsControllerRXSpanLoss'
_Aw='cooOtsControllerTranspAdminState'
_Av='cooOtsControllerState'
_Au='cooOtsControllerProtectionPortRole'
_At='cooOtsControllerLaserStatus'
_As='cooIntervalNum'
_Ar='cooIntervalType'
_Aq='cooCurrentIntervalType'
_Ap='cooThreshIntervalType'
_Ao='switchToProtect'
_An='misAutoAmp'
_Am='noEqAutoAmp'
_Al='degHighGain'
_Ak='degLowGain'
_Aj='lospRXPwr'
_Ai='highTXPwr'
_Ah='highRXPwr'
_Ag='CoiOpticalWavelength'
_Af='cooOtsEquipmentAlarm'
_Ae='cooOtsAlarmServiceAffecting'
_Ad='cooOtsAlarmStatus'
_Ac='cooOtsAlarmSeverity'
_Ab='cooOtsAlarmAdditionalInfo'
_Aa='cooOtsAlarmName'
_AZ='cooOtsAlarmTimeStamp'
_AY='cooOtsAlarmType'
_AX='cooOtsAlarmLocation'
_AW='cooOtsOchControllerAlarmState'
_AV='cooOtsOchControllerTXLowThreshold'
_AU='cooOtsOchControllerRXLowThreshold'
_AT='cooOtsOchControllerPortType'
_AS='cooIntervalAmpliGainTiltAvg'
_AR='cooIntervalAmpliGainTiltMax'
_AQ='cooIntervalAmpliGainTiltMin'
_AP='cooIntervalAmpliGainAvg'
_AO='cooIntervalAmpliGainMax'
_AN='cooIntervalAmpliGainMin'
_AM='cooCurrentAmpliGainTiltAvg'
_AL='cooCurrentAmpliGainTiltMax'
_AK='cooCurrentAmpliGainTiltMin'
_AJ='cooCurrentAmpliGainAvg'
_AI='cooCurrentAmpliGainMax'
_AH='cooCurrentAmpliGainMin'
_AG='cooThreshAmpliGainTiltEnableMin'
_AF='cooThreshAmpliGainTiltEnableMax'
_AE='cooThreshAmpliGainTiltMax'
_AD='cooThreshAmpliGainTiltMin'
_AC='cooThreshAmpliGainEnableMin'
_AB='cooThreshAmpliGainEnableMax'
_AA='cooThreshAmpliGainMax'
_A9='cooThreshAmpliGainMin'
_A8='cooOtsControllerTXEnabled'
_A7='cooOtsControllerRXEnabled'
_A6='cooOtsControllerAlarmState'
_A5='cooOtsControllerOsri'
_A4='cooOtsControllerAmpliSafetyCtrlMode'
_A3='cooOtsControllerAmpliGainRange'
_A2='cooOtsControllerAmpliControlMode'
_A1='cooOtsControllerChannelPwrMaxDelta'
_A0='cooOtsControllerAmpliChannelPwr'
_z='cooOtsControllerTXLowThreshold'
_y='cooOtsControllerRXLowThreshold'
_x='cooOtsControllerTXVoaAttenuation'
_w='cooOtsControllerRXVoaAttenuation'
_v='cooOtsControllerTotalTXPower'
_u='cooOtsControllerTotalRXPower'
_t='cooOtsControllerAmpliTilt'
_s='cooOtsControllerAmpliGain'
_r='cooOtsControllerTXPower'
_q='cooOtsControllerRXPower'
_p='cooOtsControllerPortType'
_o='Bits'
_n='CoiOpticalPower'
_m='cooIntervalLBCAvg'
_l='cooIntervalRXPowerAvg'
_k='cooIntervalTXPowerAvg'
_j='cooIntervalLBCMin'
_i='cooIntervalRXPowerMin'
_h='cooIntervalTXPowerMin'
_g='cooIntervalLBCMax'
_f='cooIntervalRXPowerMax'
_e='cooIntervalTXPowerMax'
_d='cooCurrentLBCAvg'
_c='cooCurrentRXPowerAvg'
_b='cooCurrentTXPowerAvg'
_a='cooCurrentLBCMin'
_Z='cooCurrentRXPowerMin'
_Y='cooCurrentTXPowerMin'
_X='cooCurrentLBCMax'
_W='cooCurrentRXPowerMax'
_V='cooCurrentTXPowerMax'
_U='cooThreshLBCMax'
_T='cooThreshRXPowerMax'
_S='cooThreshTXPowerMax'
_R='cooThreshLBCMin'
_Q='cooThreshRXPowerMin'
_P='cooThreshTXPowerMin'
_O='not-accessible'
_N='ifName'
_M='Integer32'
_L='accessible-for-notify'
_K='1/10 percent'
_J='ifIndex'
_I='IF-MIB'
_H='TruthValue'
_G='Unsigned32'
_F='1/100 dB'
_E='1/100 dBm'
_D='read-write'
_C='read-only'
_B='current'
_A='CISCO-OPTICAL-OTS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CoiIntervalType,CoiOptAlarmServiceAffecting,CoiOptAlarmSeverity,CoiOptAlarmStatus,CoiOptAlarmType,CoiOpticalPower,CoiOpticalWavelength=mibBuilder.importSymbols('CISCO-OPTICAL-MIB','CoiIntervalType','CoiOptAlarmServiceAffecting','CoiOptAlarmSeverity','CoiOptAlarmStatus','CoiOptAlarmType',_n,_Ag)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,ifName=mibBuilder.importSymbols(_I,_J,_N)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_o,'Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_H)
ciscoOpticalOtsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,834))
if mibBuilder.loadTexts:ciscoOpticalOtsMIB.setRevisions(('2020-04-08 00:00','2018-06-06 00:00','2016-12-16 00:00','2016-12-09 00:00'))
class CiscoOpticalOtsPortType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('line',1),('com',2),('osc',3),('comCheck',4),('working',5),('protected',6)))
class CiscoOpticalOtsGainInDb(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,4000))
class CiscoOpticalOtsTiltInDb(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-500,500))
class CiscoOpticalOtsVoaAttenInDb(TextualConvention,Unsigned32):status=_B
class CiscoOpticalOtsLaserStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('on',2),('off',3),('apr',4)))
class CiscoOpticalOtsAmpliControlMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual',1),('auto',2)))
class CiscoOpticalOtsAmpliGainRange(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('extended',2)))
class CiscoOpticalOtsAmpliSafetyCtrlMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('disabled',2)))
class CiscoOpticalOtsOsri(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
class CiscoOpticalOtsProtectionPortRole(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('standby',2)))
class CiscoOpticalOtsState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('adminDown',3)))
class CiscoOpticalOtsTranspAdminState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('inService',1),('outOfService',2),('maintenance',3),('ains',4)))
_CiscoOpticalOtsMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoOpticalOtsMIBNotifs=_CiscoOpticalOtsMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,834,0))
_CiscoOpticalOtsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoOpticalOtsMIBObjects=_CiscoOpticalOtsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,834,1))
_CooOtsController_ObjectIdentity=ObjectIdentity
cooOtsController=_CooOtsController_ObjectIdentity((1,3,6,1,4,1,9,9,834,1,1))
class _CooOtsNotifEnabled_Type(TruthValue):defaultValue=2
_CooOtsNotifEnabled_Type.__name__=_H
_CooOtsNotifEnabled_Object=MibScalar
cooOtsNotifEnabled=_CooOtsNotifEnabled_Object((1,3,6,1,4,1,9,9,834,1,1,1),_CooOtsNotifEnabled_Type())
cooOtsNotifEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cooOtsNotifEnabled.setStatus(_B)
_CooOtsControllerTable_Object=MibTable
cooOtsControllerTable=_CooOtsControllerTable_Object((1,3,6,1,4,1,9,9,834,1,1,2))
if mibBuilder.loadTexts:cooOtsControllerTable.setStatus(_B)
_CooOtsControllerEntry_Object=MibTableRow
cooOtsControllerEntry=_CooOtsControllerEntry_Object((1,3,6,1,4,1,9,9,834,1,1,2,1))
cooOtsControllerEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:cooOtsControllerEntry.setStatus(_B)
_CooOtsControllerPortType_Type=CiscoOpticalOtsPortType
_CooOtsControllerPortType_Object=MibTableColumn
cooOtsControllerPortType=_CooOtsControllerPortType_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,1),_CooOtsControllerPortType_Type())
cooOtsControllerPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:cooOtsControllerPortType.setStatus(_B)
_CooOtsControllerLaserStatus_Type=CiscoOpticalOtsLaserStatus
_CooOtsControllerLaserStatus_Object=MibTableColumn
cooOtsControllerLaserStatus=_CooOtsControllerLaserStatus_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,2),_CooOtsControllerLaserStatus_Type())
cooOtsControllerLaserStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cooOtsControllerLaserStatus.setStatus(_B)
_CooOtsControllerRXPower_Type=CoiOpticalPower
_CooOtsControllerRXPower_Object=MibTableColumn
cooOtsControllerRXPower=_CooOtsControllerRXPower_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,3),_CooOtsControllerRXPower_Type())
cooOtsControllerRXPower.setMaxAccess(_C)
if mibBuilder.loadTexts:cooOtsControllerRXPower.setStatus(_B)
if mibBuilder.loadTexts:cooOtsControllerRXPower.setUnits(_E)
_CooOtsControllerTXPower_Type=CoiOpticalPower
_CooOtsControllerTXPower_Object=MibTableColumn
cooOtsControllerTXPower=_CooOtsControllerTXPower_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,4),_CooOtsControllerTXPower_Type())
cooOtsControllerTXPower.setMaxAccess(_C)
if mibBuilder.loadTexts:cooOtsControllerTXPower.setStatus(_B)
if mibBuilder.loadTexts:cooOtsControllerTXPower.setUnits(_E)
_CooOtsControllerAmpliGain_Type=CiscoOpticalOtsGainInDb
_CooOtsControllerAmpliGain_Object=MibTableColumn
cooOtsControllerAmpliGain=_CooOtsControllerAmpliGain_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,5),_CooOtsControllerAmpliGain_Type())
cooOtsControllerAmpliGain.setMaxAccess(_D)
if mibBuilder.loadTexts:cooOtsControllerAmpliGain.setStatus(_B)
if mibBuilder.loadTexts:cooOtsControllerAmpliGain.setUnits(_F)
_CooOtsControllerAmpliTilt_Type=CiscoOpticalOtsTiltInDb
_CooOtsControllerAmpliTilt_Object=MibTableColumn
cooOtsControllerAmpliTilt=_CooOtsControllerAmpliTilt_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,6),_CooOtsControllerAmpliTilt_Type())
cooOtsControllerAmpliTilt.setMaxAccess(_D)
if mibBuilder.loadTexts:cooOtsControllerAmpliTilt.setStatus(_B)
if mibBuilder.loadTexts:cooOtsControllerAmpliTilt.setUnits(_F)
_CooOtsControllerTotalRXPower_Type=CoiOpticalPower
_CooOtsControllerTotalRXPower_Object=MibTableColumn
cooOtsControllerTotalRXPower=_CooOtsControllerTotalRXPower_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,7),_CooOtsControllerTotalRXPower_Type())
cooOtsControllerTotalRXPower.setMaxAccess(_C)
if mibBuilder.loadTexts:cooOtsControllerTotalRXPower.setStatus(_B)
if mibBuilder.loadTexts:cooOtsControllerTotalRXPower.setUnits(_E)
_CooOtsControllerTotalTXPower_Type=CoiOpticalPower
_CooOtsControllerTotalTXPower_Object=MibTableColumn
cooOtsControllerTotalTXPower=_CooOtsControllerTotalTXPower_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,8),_CooOtsControllerTotalTXPower_Type())
cooOtsControllerTotalTXPower.setMaxAccess(_C)
if mibBuilder.loadTexts:cooOtsControllerTotalTXPower.setStatus(_B)
if mibBuilder.loadTexts:cooOtsControllerTotalTXPower.setUnits(_E)
_CooOtsControllerRXVoaAttenuation_Type=CiscoOpticalOtsVoaAttenInDb
_CooOtsControllerRXVoaAttenuation_Object=MibTableColumn
cooOtsControllerRXVoaAttenuation=_CooOtsControllerRXVoaAttenuation_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,9),_CooOtsControllerRXVoaAttenuation_Type())
cooOtsControllerRXVoaAttenuation.setMaxAccess(_D)
if mibBuilder.loadTexts:cooOtsControllerRXVoaAttenuation.setStatus(_B)
if mibBuilder.loadTexts:cooOtsControllerRXVoaAttenuation.setUnits(_F)
_CooOtsControllerTXVoaAttenuation_Type=CiscoOpticalOtsVoaAttenInDb
_CooOtsControllerTXVoaAttenuation_Object=MibTableColumn
cooOtsControllerTXVoaAttenuation=_CooOtsControllerTXVoaAttenuation_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,10),_CooOtsControllerTXVoaAttenuation_Type())
cooOtsControllerTXVoaAttenuation.setMaxAccess(_D)
if mibBuilder.loadTexts:cooOtsControllerTXVoaAttenuation.setStatus(_B)
if mibBuilder.loadTexts:cooOtsControllerTXVoaAttenuation.setUnits(_F)
_CooOtsControllerRXLowThreshold_Type=CoiOpticalPower
_CooOtsControllerRXLowThreshold_Object=MibTableColumn
cooOtsControllerRXLowThreshold=_CooOtsControllerRXLowThreshold_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,11),_CooOtsControllerRXLowThreshold_Type())
cooOtsControllerRXLowThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cooOtsControllerRXLowThreshold.setStatus(_B)
if mibBuilder.loadTexts:cooOtsControllerRXLowThreshold.setUnits(_E)
_CooOtsControllerTXLowThreshold_Type=CoiOpticalPower
_CooOtsControllerTXLowThreshold_Object=MibTableColumn
cooOtsControllerTXLowThreshold=_CooOtsControllerTXLowThreshold_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,12),_CooOtsControllerTXLowThreshold_Type())
cooOtsControllerTXLowThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cooOtsControllerTXLowThreshold.setStatus(_B)
if mibBuilder.loadTexts:cooOtsControllerTXLowThreshold.setUnits(_E)
_CooOtsControllerAmpliChannelPwr_Type=CoiOpticalPower
_CooOtsControllerAmpliChannelPwr_Object=MibTableColumn
cooOtsControllerAmpliChannelPwr=_CooOtsControllerAmpliChannelPwr_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,13),_CooOtsControllerAmpliChannelPwr_Type())
cooOtsControllerAmpliChannelPwr.setMaxAccess(_D)
if mibBuilder.loadTexts:cooOtsControllerAmpliChannelPwr.setStatus(_B)
if mibBuilder.loadTexts:cooOtsControllerAmpliChannelPwr.setUnits(_E)
_CooOtsControllerChannelPwrMaxDelta_Type=CoiOpticalPower
_CooOtsControllerChannelPwrMaxDelta_Object=MibTableColumn
cooOtsControllerChannelPwrMaxDelta=_CooOtsControllerChannelPwrMaxDelta_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,14),_CooOtsControllerChannelPwrMaxDelta_Type())
cooOtsControllerChannelPwrMaxDelta.setMaxAccess(_D)
if mibBuilder.loadTexts:cooOtsControllerChannelPwrMaxDelta.setStatus(_B)
if mibBuilder.loadTexts:cooOtsControllerChannelPwrMaxDelta.setUnits(_E)
_CooOtsControllerAmpliControlMode_Type=CiscoOpticalOtsAmpliControlMode
_CooOtsControllerAmpliControlMode_Object=MibTableColumn
cooOtsControllerAmpliControlMode=_CooOtsControllerAmpliControlMode_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,15),_CooOtsControllerAmpliControlMode_Type())
cooOtsControllerAmpliControlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:cooOtsControllerAmpliControlMode.setStatus(_B)
_CooOtsControllerAmpliGainRange_Type=CiscoOpticalOtsAmpliGainRange
_CooOtsControllerAmpliGainRange_Object=MibTableColumn
cooOtsControllerAmpliGainRange=_CooOtsControllerAmpliGainRange_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,16),_CooOtsControllerAmpliGainRange_Type())
cooOtsControllerAmpliGainRange.setMaxAccess(_D)
if mibBuilder.loadTexts:cooOtsControllerAmpliGainRange.setStatus(_B)
_CooOtsControllerAmpliSafetyCtrlMode_Type=CiscoOpticalOtsAmpliSafetyCtrlMode
_CooOtsControllerAmpliSafetyCtrlMode_Object=MibTableColumn
cooOtsControllerAmpliSafetyCtrlMode=_CooOtsControllerAmpliSafetyCtrlMode_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,17),_CooOtsControllerAmpliSafetyCtrlMode_Type())
cooOtsControllerAmpliSafetyCtrlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:cooOtsControllerAmpliSafetyCtrlMode.setStatus(_B)
_CooOtsControllerOsri_Type=CiscoOpticalOtsOsri
_CooOtsControllerOsri_Object=MibTableColumn
cooOtsControllerOsri=_CooOtsControllerOsri_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,18),_CooOtsControllerOsri_Type())
cooOtsControllerOsri.setMaxAccess(_D)
if mibBuilder.loadTexts:cooOtsControllerOsri.setStatus(_B)
_CooOtsControllerProtectionPortRole_Type=CiscoOpticalOtsProtectionPortRole
_CooOtsControllerProtectionPortRole_Object=MibTableColumn
cooOtsControllerProtectionPortRole=_CooOtsControllerProtectionPortRole_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,19),_CooOtsControllerProtectionPortRole_Type())
cooOtsControllerProtectionPortRole.setMaxAccess(_C)
if mibBuilder.loadTexts:cooOtsControllerProtectionPortRole.setStatus(_B)
_CooOtsControllerState_Type=CiscoOpticalOtsState
_CooOtsControllerState_Object=MibTableColumn
cooOtsControllerState=_CooOtsControllerState_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,20),_CooOtsControllerState_Type())
cooOtsControllerState.setMaxAccess(_C)
if mibBuilder.loadTexts:cooOtsControllerState.setStatus(_B)
_CooOtsControllerTranspAdminState_Type=CiscoOpticalOtsTranspAdminState
_CooOtsControllerTranspAdminState_Object=MibTableColumn
cooOtsControllerTranspAdminState=_CooOtsControllerTranspAdminState_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,21),_CooOtsControllerTranspAdminState_Type())
cooOtsControllerTranspAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:cooOtsControllerTranspAdminState.setStatus(_B)
class _CooOtsControllerAlarmState_Type(Bits):namedValues=NamedValues(*(('noDefect',0),(_Ah,1),(_Ai,2),('lowRXPwr',3),('lowTXPwr',4),(_Aj,5),('locRXPwr',6),(_Ak,7),(_Al,8),('alsAmp',9),('aprAmp',10),(_Am,11),(_An,12),(_Ao,13),('autoAmpliCtrlRunning',14)))
_CooOtsControllerAlarmState_Type.__name__=_o
_CooOtsControllerAlarmState_Object=MibTableColumn
cooOtsControllerAlarmState=_CooOtsControllerAlarmState_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,22),_CooOtsControllerAlarmState_Type())
cooOtsControllerAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:cooOtsControllerAlarmState.setStatus(_B)
class _CooOtsControllerRXSpanLoss_Type(CoiOpticalPower):subtypeSpec=CoiOpticalPower.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-4000,3000))
_CooOtsControllerRXSpanLoss_Type.__name__=_n
_CooOtsControllerRXSpanLoss_Object=MibTableColumn
cooOtsControllerRXSpanLoss=_CooOtsControllerRXSpanLoss_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,23),_CooOtsControllerRXSpanLoss_Type())
cooOtsControllerRXSpanLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:cooOtsControllerRXSpanLoss.setStatus(_B)
if mibBuilder.loadTexts:cooOtsControllerRXSpanLoss.setUnits(_E)
class _CooOtsControllerTXSpanLoss_Type(CoiOpticalPower):subtypeSpec=CoiOpticalPower.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-4000,3000))
_CooOtsControllerTXSpanLoss_Type.__name__=_n
_CooOtsControllerTXSpanLoss_Object=MibTableColumn
cooOtsControllerTXSpanLoss=_CooOtsControllerTXSpanLoss_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,24),_CooOtsControllerTXSpanLoss_Type())
cooOtsControllerTXSpanLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:cooOtsControllerTXSpanLoss.setStatus(_B)
if mibBuilder.loadTexts:cooOtsControllerTXSpanLoss.setUnits(_E)
_CooOtsControllerRXEnabled_Type=TruthValue
_CooOtsControllerRXEnabled_Object=MibTableColumn
cooOtsControllerRXEnabled=_CooOtsControllerRXEnabled_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,25),_CooOtsControllerRXEnabled_Type())
cooOtsControllerRXEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cooOtsControllerRXEnabled.setStatus(_B)
_CooOtsControllerTXEnabled_Type=TruthValue
_CooOtsControllerTXEnabled_Object=MibTableColumn
cooOtsControllerTXEnabled=_CooOtsControllerTXEnabled_Object((1,3,6,1,4,1,9,9,834,1,1,2,1,26),_CooOtsControllerTXEnabled_Type())
cooOtsControllerTXEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cooOtsControllerTXEnabled.setStatus(_B)
_CooOtsOchControllerTable_Object=MibTable
cooOtsOchControllerTable=_CooOtsOchControllerTable_Object((1,3,6,1,4,1,9,9,834,1,1,3))
if mibBuilder.loadTexts:cooOtsOchControllerTable.setStatus(_B)
_CooOtsOchControllerEntry_Object=MibTableRow
cooOtsOchControllerEntry=_CooOtsOchControllerEntry_Object((1,3,6,1,4,1,9,9,834,1,1,3,1))
cooOtsOchControllerEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:cooOtsOchControllerEntry.setStatus(_B)
_CooOtsOchControllerPortType_Type=CiscoOpticalOtsPortType
_CooOtsOchControllerPortType_Object=MibTableColumn
cooOtsOchControllerPortType=_CooOtsOchControllerPortType_Object((1,3,6,1,4,1,9,9,834,1,1,3,1,1),_CooOtsOchControllerPortType_Type())
cooOtsOchControllerPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:cooOtsOchControllerPortType.setStatus(_B)
_CooOtsOchControllerLaserStatus_Type=CiscoOpticalOtsLaserStatus
_CooOtsOchControllerLaserStatus_Object=MibTableColumn
cooOtsOchControllerLaserStatus=_CooOtsOchControllerLaserStatus_Object((1,3,6,1,4,1,9,9,834,1,1,3,1,2),_CooOtsOchControllerLaserStatus_Type())
cooOtsOchControllerLaserStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cooOtsOchControllerLaserStatus.setStatus(_B)
_CooOtsOchControllerRXPower_Type=CoiOpticalPower
_CooOtsOchControllerRXPower_Object=MibTableColumn
cooOtsOchControllerRXPower=_CooOtsOchControllerRXPower_Object((1,3,6,1,4,1,9,9,834,1,1,3,1,3),_CooOtsOchControllerRXPower_Type())
cooOtsOchControllerRXPower.setMaxAccess(_C)
if mibBuilder.loadTexts:cooOtsOchControllerRXPower.setStatus(_B)
if mibBuilder.loadTexts:cooOtsOchControllerRXPower.setUnits(_E)
_CooOtsOchControllerTXPower_Type=CoiOpticalPower
_CooOtsOchControllerTXPower_Object=MibTableColumn
cooOtsOchControllerTXPower=_CooOtsOchControllerTXPower_Object((1,3,6,1,4,1,9,9,834,1,1,3,1,4),_CooOtsOchControllerTXPower_Type())
cooOtsOchControllerTXPower.setMaxAccess(_C)
if mibBuilder.loadTexts:cooOtsOchControllerTXPower.setStatus(_B)
if mibBuilder.loadTexts:cooOtsOchControllerTXPower.setUnits(_E)
_CooOtsOchControllerRXLowThreshold_Type=CoiOpticalPower
_CooOtsOchControllerRXLowThreshold_Object=MibTableColumn
cooOtsOchControllerRXLowThreshold=_CooOtsOchControllerRXLowThreshold_Object((1,3,6,1,4,1,9,9,834,1,1,3,1,5),_CooOtsOchControllerRXLowThreshold_Type())
cooOtsOchControllerRXLowThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cooOtsOchControllerRXLowThreshold.setStatus(_B)
if mibBuilder.loadTexts:cooOtsOchControllerRXLowThreshold.setUnits(_E)
_CooOtsOchControllerTXLowThreshold_Type=CoiOpticalPower
_CooOtsOchControllerTXLowThreshold_Object=MibTableColumn
cooOtsOchControllerTXLowThreshold=_CooOtsOchControllerTXLowThreshold_Object((1,3,6,1,4,1,9,9,834,1,1,3,1,6),_CooOtsOchControllerTXLowThreshold_Type())
cooOtsOchControllerTXLowThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cooOtsOchControllerTXLowThreshold.setStatus(_B)
if mibBuilder.loadTexts:cooOtsOchControllerTXLowThreshold.setUnits(_E)
class _CooOtsOchControllerWavelength_Type(CoiOpticalWavelength):defaultValue=0
_CooOtsOchControllerWavelength_Type.__name__=_Ag
_CooOtsOchControllerWavelength_Object=MibTableColumn
cooOtsOchControllerWavelength=_CooOtsOchControllerWavelength_Object((1,3,6,1,4,1,9,9,834,1,1,3,1,7),_CooOtsOchControllerWavelength_Type())
cooOtsOchControllerWavelength.setMaxAccess(_C)
if mibBuilder.loadTexts:cooOtsOchControllerWavelength.setStatus(_B)
if mibBuilder.loadTexts:cooOtsOchControllerWavelength.setUnits('1/100 nm')
class _CooOtsOchControllerFrequency_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1913500,1961000))
_CooOtsOchControllerFrequency_Type.__name__=_G
_CooOtsOchControllerFrequency_Object=MibTableColumn
cooOtsOchControllerFrequency=_CooOtsOchControllerFrequency_Object((1,3,6,1,4,1,9,9,834,1,1,3,1,8),_CooOtsOchControllerFrequency_Type())
cooOtsOchControllerFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:cooOtsOchControllerFrequency.setStatus(_B)
if mibBuilder.loadTexts:cooOtsOchControllerFrequency.setUnits('100 MHz')
class _CooOtsOchControllerChannelNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,384))
_CooOtsOchControllerChannelNumber_Type.__name__=_G
_CooOtsOchControllerChannelNumber_Object=MibTableColumn
cooOtsOchControllerChannelNumber=_CooOtsOchControllerChannelNumber_Object((1,3,6,1,4,1,9,9,834,1,1,3,1,9),_CooOtsOchControllerChannelNumber_Type())
cooOtsOchControllerChannelNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cooOtsOchControllerChannelNumber.setStatus(_B)
_CooOtsOchControllerState_Type=CiscoOpticalOtsState
_CooOtsOchControllerState_Object=MibTableColumn
cooOtsOchControllerState=_CooOtsOchControllerState_Object((1,3,6,1,4,1,9,9,834,1,1,3,1,10),_CooOtsOchControllerState_Type())
cooOtsOchControllerState.setMaxAccess(_C)
if mibBuilder.loadTexts:cooOtsOchControllerState.setStatus(_B)
_CooOtsOchControllerTranspAdminState_Type=CiscoOpticalOtsTranspAdminState
_CooOtsOchControllerTranspAdminState_Object=MibTableColumn
cooOtsOchControllerTranspAdminState=_CooOtsOchControllerTranspAdminState_Object((1,3,6,1,4,1,9,9,834,1,1,3,1,11),_CooOtsOchControllerTranspAdminState_Type())
cooOtsOchControllerTranspAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:cooOtsOchControllerTranspAdminState.setStatus(_B)
class _CooOtsOchControllerAlarmState_Type(Bits):namedValues=NamedValues(*(('noDefect',0),(_Ah,1),(_Ai,2),('lowRXPwr',3),('lowTXPwr',4),(_Aj,5),('locRXPwr',6),(_Ak,7),(_Al,8),('alsAmp',9),('aprAmp',10),(_Am,11),(_An,12),(_Ao,13)))
_CooOtsOchControllerAlarmState_Type.__name__=_o
_CooOtsOchControllerAlarmState_Object=MibTableColumn
cooOtsOchControllerAlarmState=_CooOtsOchControllerAlarmState_Object((1,3,6,1,4,1,9,9,834,1,1,3,1,12),_CooOtsOchControllerAlarmState_Type())
cooOtsOchControllerAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:cooOtsOchControllerAlarmState.setStatus(_B)
class _CooOtsOchControllerWidth_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,8000))
_CooOtsOchControllerWidth_Type.__name__=_G
_CooOtsOchControllerWidth_Object=MibTableColumn
cooOtsOchControllerWidth=_CooOtsOchControllerWidth_Object((1,3,6,1,4,1,9,9,834,1,1,3,1,13),_CooOtsOchControllerWidth_Type())
cooOtsOchControllerWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cooOtsOchControllerWidth.setStatus(_B)
if mibBuilder.loadTexts:cooOtsOchControllerWidth.setUnits('1/10 GHz')
class _CooOtsOchNotifEnabled_Type(TruthValue):defaultValue=2
_CooOtsOchNotifEnabled_Type.__name__=_H
_CooOtsOchNotifEnabled_Object=MibScalar
cooOtsOchNotifEnabled=_CooOtsOchNotifEnabled_Object((1,3,6,1,4,1,9,9,834,1,1,4),_CooOtsOchNotifEnabled_Type())
cooOtsOchNotifEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cooOtsOchNotifEnabled.setStatus(_B)
_CooOtsPerformanceMonitoring_ObjectIdentity=ObjectIdentity
cooOtsPerformanceMonitoring=_CooOtsPerformanceMonitoring_ObjectIdentity((1,3,6,1,4,1,9,9,834,1,2))
_CooOtsThresholdTable_Object=MibTable
cooOtsThresholdTable=_CooOtsThresholdTable_Object((1,3,6,1,4,1,9,9,834,1,2,1))
if mibBuilder.loadTexts:cooOtsThresholdTable.setStatus(_B)
_CooOtsThresholdEntry_Object=MibTableRow
cooOtsThresholdEntry=_CooOtsThresholdEntry_Object((1,3,6,1,4,1,9,9,834,1,2,1,1))
cooOtsThresholdEntry.setIndexNames((0,_I,_J),(0,_A,_Ap))
if mibBuilder.loadTexts:cooOtsThresholdEntry.setStatus(_B)
_CooThreshIntervalType_Type=CoiIntervalType
_CooThreshIntervalType_Object=MibTableColumn
cooThreshIntervalType=_CooThreshIntervalType_Object((1,3,6,1,4,1,9,9,834,1,2,1,1,1),_CooThreshIntervalType_Type())
cooThreshIntervalType.setMaxAccess(_O)
if mibBuilder.loadTexts:cooThreshIntervalType.setStatus(_B)
_CooThreshTXPowerMin_Type=CoiOpticalPower
_CooThreshTXPowerMin_Object=MibTableColumn
cooThreshTXPowerMin=_CooThreshTXPowerMin_Object((1,3,6,1,4,1,9,9,834,1,2,1,1,2),_CooThreshTXPowerMin_Type())
cooThreshTXPowerMin.setMaxAccess(_D)
if mibBuilder.loadTexts:cooThreshTXPowerMin.setStatus(_B)
if mibBuilder.loadTexts:cooThreshTXPowerMin.setUnits(_E)
_CooThreshRXPowerMin_Type=CoiOpticalPower
_CooThreshRXPowerMin_Object=MibTableColumn
cooThreshRXPowerMin=_CooThreshRXPowerMin_Object((1,3,6,1,4,1,9,9,834,1,2,1,1,3),_CooThreshRXPowerMin_Type())
cooThreshRXPowerMin.setMaxAccess(_D)
if mibBuilder.loadTexts:cooThreshRXPowerMin.setStatus(_B)
if mibBuilder.loadTexts:cooThreshRXPowerMin.setUnits(_E)
class _CooThreshLBCMin_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CooThreshLBCMin_Type.__name__=_G
_CooThreshLBCMin_Object=MibTableColumn
cooThreshLBCMin=_CooThreshLBCMin_Object((1,3,6,1,4,1,9,9,834,1,2,1,1,4),_CooThreshLBCMin_Type())
cooThreshLBCMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cooThreshLBCMin.setStatus(_B)
if mibBuilder.loadTexts:cooThreshLBCMin.setUnits(_K)
_CooThreshTXPowerMax_Type=CoiOpticalPower
_CooThreshTXPowerMax_Object=MibTableColumn
cooThreshTXPowerMax=_CooThreshTXPowerMax_Object((1,3,6,1,4,1,9,9,834,1,2,1,1,5),_CooThreshTXPowerMax_Type())
cooThreshTXPowerMax.setMaxAccess(_D)
if mibBuilder.loadTexts:cooThreshTXPowerMax.setStatus(_B)
if mibBuilder.loadTexts:cooThreshTXPowerMax.setUnits(_E)
_CooThreshRXPowerMax_Type=CoiOpticalPower
_CooThreshRXPowerMax_Object=MibTableColumn
cooThreshRXPowerMax=_CooThreshRXPowerMax_Object((1,3,6,1,4,1,9,9,834,1,2,1,1,6),_CooThreshRXPowerMax_Type())
cooThreshRXPowerMax.setMaxAccess(_D)
if mibBuilder.loadTexts:cooThreshRXPowerMax.setStatus(_B)
if mibBuilder.loadTexts:cooThreshRXPowerMax.setUnits(_E)
class _CooThreshLBCMax_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CooThreshLBCMax_Type.__name__=_G
_CooThreshLBCMax_Object=MibTableColumn
cooThreshLBCMax=_CooThreshLBCMax_Object((1,3,6,1,4,1,9,9,834,1,2,1,1,7),_CooThreshLBCMax_Type())
cooThreshLBCMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cooThreshLBCMax.setStatus(_B)
if mibBuilder.loadTexts:cooThreshLBCMax.setUnits(_K)
class _CooThreshTXPowerEnableMin_Type(TruthValue):defaultValue=2
_CooThreshTXPowerEnableMin_Type.__name__=_H
_CooThreshTXPowerEnableMin_Object=MibTableColumn
cooThreshTXPowerEnableMin=_CooThreshTXPowerEnableMin_Object((1,3,6,1,4,1,9,9,834,1,2,1,1,8),_CooThreshTXPowerEnableMin_Type())
cooThreshTXPowerEnableMin.setMaxAccess(_D)
if mibBuilder.loadTexts:cooThreshTXPowerEnableMin.setStatus(_B)
class _CooThreshRXPowerEnableMin_Type(TruthValue):defaultValue=2
_CooThreshRXPowerEnableMin_Type.__name__=_H
_CooThreshRXPowerEnableMin_Object=MibTableColumn
cooThreshRXPowerEnableMin=_CooThreshRXPowerEnableMin_Object((1,3,6,1,4,1,9,9,834,1,2,1,1,9),_CooThreshRXPowerEnableMin_Type())
cooThreshRXPowerEnableMin.setMaxAccess(_D)
if mibBuilder.loadTexts:cooThreshRXPowerEnableMin.setStatus(_B)
class _CooThreshLBCEnableMin_Type(TruthValue):defaultValue=2
_CooThreshLBCEnableMin_Type.__name__=_H
_CooThreshLBCEnableMin_Object=MibTableColumn
cooThreshLBCEnableMin=_CooThreshLBCEnableMin_Object((1,3,6,1,4,1,9,9,834,1,2,1,1,10),_CooThreshLBCEnableMin_Type())
cooThreshLBCEnableMin.setMaxAccess(_D)
if mibBuilder.loadTexts:cooThreshLBCEnableMin.setStatus(_B)
class _CooThreshTXPowerEnableMax_Type(TruthValue):defaultValue=2
_CooThreshTXPowerEnableMax_Type.__name__=_H
_CooThreshTXPowerEnableMax_Object=MibTableColumn
cooThreshTXPowerEnableMax=_CooThreshTXPowerEnableMax_Object((1,3,6,1,4,1,9,9,834,1,2,1,1,11),_CooThreshTXPowerEnableMax_Type())
cooThreshTXPowerEnableMax.setMaxAccess(_D)
if mibBuilder.loadTexts:cooThreshTXPowerEnableMax.setStatus(_B)
class _CooThreshRXPowerEnableMax_Type(TruthValue):defaultValue=2
_CooThreshRXPowerEnableMax_Type.__name__=_H
_CooThreshRXPowerEnableMax_Object=MibTableColumn
cooThreshRXPowerEnableMax=_CooThreshRXPowerEnableMax_Object((1,3,6,1,4,1,9,9,834,1,2,1,1,12),_CooThreshRXPowerEnableMax_Type())
cooThreshRXPowerEnableMax.setMaxAccess(_D)
if mibBuilder.loadTexts:cooThreshRXPowerEnableMax.setStatus(_B)
class _CooThreshLBCEnableMax_Type(TruthValue):defaultValue=2
_CooThreshLBCEnableMax_Type.__name__=_H
_CooThreshLBCEnableMax_Object=MibTableColumn
cooThreshLBCEnableMax=_CooThreshLBCEnableMax_Object((1,3,6,1,4,1,9,9,834,1,2,1,1,13),_CooThreshLBCEnableMax_Type())
cooThreshLBCEnableMax.setMaxAccess(_D)
if mibBuilder.loadTexts:cooThreshLBCEnableMax.setStatus(_B)
class _CooThreshAmpliGainMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_CooThreshAmpliGainMin_Type.__name__=_M
_CooThreshAmpliGainMin_Object=MibTableColumn
cooThreshAmpliGainMin=_CooThreshAmpliGainMin_Object((1,3,6,1,4,1,9,9,834,1,2,1,1,14),_CooThreshAmpliGainMin_Type())
cooThreshAmpliGainMin.setMaxAccess(_D)
if mibBuilder.loadTexts:cooThreshAmpliGainMin.setStatus(_B)
if mibBuilder.loadTexts:cooThreshAmpliGainMin.setUnits(_F)
class _CooThreshAmpliGainMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_CooThreshAmpliGainMax_Type.__name__=_M
_CooThreshAmpliGainMax_Object=MibTableColumn
cooThreshAmpliGainMax=_CooThreshAmpliGainMax_Object((1,3,6,1,4,1,9,9,834,1,2,1,1,15),_CooThreshAmpliGainMax_Type())
cooThreshAmpliGainMax.setMaxAccess(_D)
if mibBuilder.loadTexts:cooThreshAmpliGainMax.setStatus(_B)
if mibBuilder.loadTexts:cooThreshAmpliGainMax.setUnits(_F)
class _CooThreshAmpliGainEnableMax_Type(TruthValue):defaultValue=2
_CooThreshAmpliGainEnableMax_Type.__name__=_H
_CooThreshAmpliGainEnableMax_Object=MibTableColumn
cooThreshAmpliGainEnableMax=_CooThreshAmpliGainEnableMax_Object((1,3,6,1,4,1,9,9,834,1,2,1,1,16),_CooThreshAmpliGainEnableMax_Type())
cooThreshAmpliGainEnableMax.setMaxAccess(_D)
if mibBuilder.loadTexts:cooThreshAmpliGainEnableMax.setStatus(_B)
class _CooThreshAmpliGainEnableMin_Type(TruthValue):defaultValue=2
_CooThreshAmpliGainEnableMin_Type.__name__=_H
_CooThreshAmpliGainEnableMin_Object=MibTableColumn
cooThreshAmpliGainEnableMin=_CooThreshAmpliGainEnableMin_Object((1,3,6,1,4,1,9,9,834,1,2,1,1,17),_CooThreshAmpliGainEnableMin_Type())
cooThreshAmpliGainEnableMin.setMaxAccess(_D)
if mibBuilder.loadTexts:cooThreshAmpliGainEnableMin.setStatus(_B)
class _CooThreshAmpliGainTiltMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,50))
_CooThreshAmpliGainTiltMin_Type.__name__=_M
_CooThreshAmpliGainTiltMin_Object=MibTableColumn
cooThreshAmpliGainTiltMin=_CooThreshAmpliGainTiltMin_Object((1,3,6,1,4,1,9,9,834,1,2,1,1,18),_CooThreshAmpliGainTiltMin_Type())
cooThreshAmpliGainTiltMin.setMaxAccess(_D)
if mibBuilder.loadTexts:cooThreshAmpliGainTiltMin.setStatus(_B)
if mibBuilder.loadTexts:cooThreshAmpliGainTiltMin.setUnits(_F)
class _CooThreshAmpliGainTiltMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,50))
_CooThreshAmpliGainTiltMax_Type.__name__=_M
_CooThreshAmpliGainTiltMax_Object=MibTableColumn
cooThreshAmpliGainTiltMax=_CooThreshAmpliGainTiltMax_Object((1,3,6,1,4,1,9,9,834,1,2,1,1,19),_CooThreshAmpliGainTiltMax_Type())
cooThreshAmpliGainTiltMax.setMaxAccess(_D)
if mibBuilder.loadTexts:cooThreshAmpliGainTiltMax.setStatus(_B)
if mibBuilder.loadTexts:cooThreshAmpliGainTiltMax.setUnits('1/100 db')
class _CooThreshAmpliGainTiltEnableMax_Type(TruthValue):defaultValue=2
_CooThreshAmpliGainTiltEnableMax_Type.__name__=_H
_CooThreshAmpliGainTiltEnableMax_Object=MibTableColumn
cooThreshAmpliGainTiltEnableMax=_CooThreshAmpliGainTiltEnableMax_Object((1,3,6,1,4,1,9,9,834,1,2,1,1,20),_CooThreshAmpliGainTiltEnableMax_Type())
cooThreshAmpliGainTiltEnableMax.setMaxAccess(_D)
if mibBuilder.loadTexts:cooThreshAmpliGainTiltEnableMax.setStatus(_B)
class _CooThreshAmpliGainTiltEnableMin_Type(TruthValue):defaultValue=2
_CooThreshAmpliGainTiltEnableMin_Type.__name__=_H
_CooThreshAmpliGainTiltEnableMin_Object=MibTableColumn
cooThreshAmpliGainTiltEnableMin=_CooThreshAmpliGainTiltEnableMin_Object((1,3,6,1,4,1,9,9,834,1,2,1,1,21),_CooThreshAmpliGainTiltEnableMin_Type())
cooThreshAmpliGainTiltEnableMin.setMaxAccess(_D)
if mibBuilder.loadTexts:cooThreshAmpliGainTiltEnableMin.setStatus(_B)
_CooOtsCurrentTable_Object=MibTable
cooOtsCurrentTable=_CooOtsCurrentTable_Object((1,3,6,1,4,1,9,9,834,1,2,2))
if mibBuilder.loadTexts:cooOtsCurrentTable.setStatus(_B)
_CooOtsCurrentEntry_Object=MibTableRow
cooOtsCurrentEntry=_CooOtsCurrentEntry_Object((1,3,6,1,4,1,9,9,834,1,2,2,1))
cooOtsCurrentEntry.setIndexNames((0,_I,_J),(0,_A,_Aq))
if mibBuilder.loadTexts:cooOtsCurrentEntry.setStatus(_B)
_CooCurrentIntervalType_Type=CoiIntervalType
_CooCurrentIntervalType_Object=MibTableColumn
cooCurrentIntervalType=_CooCurrentIntervalType_Object((1,3,6,1,4,1,9,9,834,1,2,2,1,1),_CooCurrentIntervalType_Type())
cooCurrentIntervalType.setMaxAccess(_O)
if mibBuilder.loadTexts:cooCurrentIntervalType.setStatus(_B)
_CooCurrentTXPowerMax_Type=CoiOpticalPower
_CooCurrentTXPowerMax_Object=MibTableColumn
cooCurrentTXPowerMax=_CooCurrentTXPowerMax_Object((1,3,6,1,4,1,9,9,834,1,2,2,1,2),_CooCurrentTXPowerMax_Type())
cooCurrentTXPowerMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cooCurrentTXPowerMax.setStatus(_B)
if mibBuilder.loadTexts:cooCurrentTXPowerMax.setUnits(_E)
_CooCurrentRXPowerMax_Type=CoiOpticalPower
_CooCurrentRXPowerMax_Object=MibTableColumn
cooCurrentRXPowerMax=_CooCurrentRXPowerMax_Object((1,3,6,1,4,1,9,9,834,1,2,2,1,3),_CooCurrentRXPowerMax_Type())
cooCurrentRXPowerMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cooCurrentRXPowerMax.setStatus(_B)
if mibBuilder.loadTexts:cooCurrentRXPowerMax.setUnits(_E)
class _CooCurrentLBCMax_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CooCurrentLBCMax_Type.__name__=_G
_CooCurrentLBCMax_Object=MibTableColumn
cooCurrentLBCMax=_CooCurrentLBCMax_Object((1,3,6,1,4,1,9,9,834,1,2,2,1,4),_CooCurrentLBCMax_Type())
cooCurrentLBCMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cooCurrentLBCMax.setStatus(_B)
if mibBuilder.loadTexts:cooCurrentLBCMax.setUnits(_K)
_CooCurrentTXPowerMin_Type=CoiOpticalPower
_CooCurrentTXPowerMin_Object=MibTableColumn
cooCurrentTXPowerMin=_CooCurrentTXPowerMin_Object((1,3,6,1,4,1,9,9,834,1,2,2,1,5),_CooCurrentTXPowerMin_Type())
cooCurrentTXPowerMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cooCurrentTXPowerMin.setStatus(_B)
if mibBuilder.loadTexts:cooCurrentTXPowerMin.setUnits(_E)
_CooCurrentRXPowerMin_Type=CoiOpticalPower
_CooCurrentRXPowerMin_Object=MibTableColumn
cooCurrentRXPowerMin=_CooCurrentRXPowerMin_Object((1,3,6,1,4,1,9,9,834,1,2,2,1,6),_CooCurrentRXPowerMin_Type())
cooCurrentRXPowerMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cooCurrentRXPowerMin.setStatus(_B)
if mibBuilder.loadTexts:cooCurrentRXPowerMin.setUnits(_E)
class _CooCurrentLBCMin_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CooCurrentLBCMin_Type.__name__=_G
_CooCurrentLBCMin_Object=MibTableColumn
cooCurrentLBCMin=_CooCurrentLBCMin_Object((1,3,6,1,4,1,9,9,834,1,2,2,1,7),_CooCurrentLBCMin_Type())
cooCurrentLBCMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cooCurrentLBCMin.setStatus(_B)
if mibBuilder.loadTexts:cooCurrentLBCMin.setUnits(_K)
_CooCurrentTXPowerAvg_Type=CoiOpticalPower
_CooCurrentTXPowerAvg_Object=MibTableColumn
cooCurrentTXPowerAvg=_CooCurrentTXPowerAvg_Object((1,3,6,1,4,1,9,9,834,1,2,2,1,8),_CooCurrentTXPowerAvg_Type())
cooCurrentTXPowerAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:cooCurrentTXPowerAvg.setStatus(_B)
if mibBuilder.loadTexts:cooCurrentTXPowerAvg.setUnits(_E)
_CooCurrentRXPowerAvg_Type=CoiOpticalPower
_CooCurrentRXPowerAvg_Object=MibTableColumn
cooCurrentRXPowerAvg=_CooCurrentRXPowerAvg_Object((1,3,6,1,4,1,9,9,834,1,2,2,1,9),_CooCurrentRXPowerAvg_Type())
cooCurrentRXPowerAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:cooCurrentRXPowerAvg.setStatus(_B)
if mibBuilder.loadTexts:cooCurrentRXPowerAvg.setUnits(_E)
class _CooCurrentLBCAvg_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CooCurrentLBCAvg_Type.__name__=_G
_CooCurrentLBCAvg_Object=MibTableColumn
cooCurrentLBCAvg=_CooCurrentLBCAvg_Object((1,3,6,1,4,1,9,9,834,1,2,2,1,10),_CooCurrentLBCAvg_Type())
cooCurrentLBCAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:cooCurrentLBCAvg.setStatus(_B)
if mibBuilder.loadTexts:cooCurrentLBCAvg.setUnits(_K)
_CooCurrentTimestamp_Type=OctetString
_CooCurrentTimestamp_Object=MibTableColumn
cooCurrentTimestamp=_CooCurrentTimestamp_Object((1,3,6,1,4,1,9,9,834,1,2,2,1,11),_CooCurrentTimestamp_Type())
cooCurrentTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cooCurrentTimestamp.setStatus(_B)
_CooCurrentAmpliGainMin_Type=Integer32
_CooCurrentAmpliGainMin_Object=MibTableColumn
cooCurrentAmpliGainMin=_CooCurrentAmpliGainMin_Object((1,3,6,1,4,1,9,9,834,1,2,2,1,12),_CooCurrentAmpliGainMin_Type())
cooCurrentAmpliGainMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cooCurrentAmpliGainMin.setStatus(_B)
if mibBuilder.loadTexts:cooCurrentAmpliGainMin.setUnits(_F)
_CooCurrentAmpliGainMax_Type=Integer32
_CooCurrentAmpliGainMax_Object=MibTableColumn
cooCurrentAmpliGainMax=_CooCurrentAmpliGainMax_Object((1,3,6,1,4,1,9,9,834,1,2,2,1,13),_CooCurrentAmpliGainMax_Type())
cooCurrentAmpliGainMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cooCurrentAmpliGainMax.setStatus(_B)
if mibBuilder.loadTexts:cooCurrentAmpliGainMax.setUnits(_F)
_CooCurrentAmpliGainAvg_Type=Integer32
_CooCurrentAmpliGainAvg_Object=MibTableColumn
cooCurrentAmpliGainAvg=_CooCurrentAmpliGainAvg_Object((1,3,6,1,4,1,9,9,834,1,2,2,1,14),_CooCurrentAmpliGainAvg_Type())
cooCurrentAmpliGainAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:cooCurrentAmpliGainAvg.setStatus(_B)
if mibBuilder.loadTexts:cooCurrentAmpliGainAvg.setUnits(_F)
_CooCurrentAmpliGainTiltMin_Type=Integer32
_CooCurrentAmpliGainTiltMin_Object=MibTableColumn
cooCurrentAmpliGainTiltMin=_CooCurrentAmpliGainTiltMin_Object((1,3,6,1,4,1,9,9,834,1,2,2,1,15),_CooCurrentAmpliGainTiltMin_Type())
cooCurrentAmpliGainTiltMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cooCurrentAmpliGainTiltMin.setStatus(_B)
if mibBuilder.loadTexts:cooCurrentAmpliGainTiltMin.setUnits(_F)
_CooCurrentAmpliGainTiltMax_Type=Integer32
_CooCurrentAmpliGainTiltMax_Object=MibTableColumn
cooCurrentAmpliGainTiltMax=_CooCurrentAmpliGainTiltMax_Object((1,3,6,1,4,1,9,9,834,1,2,2,1,16),_CooCurrentAmpliGainTiltMax_Type())
cooCurrentAmpliGainTiltMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cooCurrentAmpliGainTiltMax.setStatus(_B)
if mibBuilder.loadTexts:cooCurrentAmpliGainTiltMax.setUnits(_F)
_CooCurrentAmpliGainTiltAvg_Type=Integer32
_CooCurrentAmpliGainTiltAvg_Object=MibTableColumn
cooCurrentAmpliGainTiltAvg=_CooCurrentAmpliGainTiltAvg_Object((1,3,6,1,4,1,9,9,834,1,2,2,1,17),_CooCurrentAmpliGainTiltAvg_Type())
cooCurrentAmpliGainTiltAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:cooCurrentAmpliGainTiltAvg.setStatus(_B)
if mibBuilder.loadTexts:cooCurrentAmpliGainTiltAvg.setUnits(_F)
_CooOtsIntervalTable_Object=MibTable
cooOtsIntervalTable=_CooOtsIntervalTable_Object((1,3,6,1,4,1,9,9,834,1,2,3))
if mibBuilder.loadTexts:cooOtsIntervalTable.setStatus(_B)
_CooOtsIntervalEntry_Object=MibTableRow
cooOtsIntervalEntry=_CooOtsIntervalEntry_Object((1,3,6,1,4,1,9,9,834,1,2,3,1))
cooOtsIntervalEntry.setIndexNames((0,_I,_J),(0,_A,_Ar),(0,_A,_As))
if mibBuilder.loadTexts:cooOtsIntervalEntry.setStatus(_B)
_CooIntervalType_Type=CoiIntervalType
_CooIntervalType_Object=MibTableColumn
cooIntervalType=_CooIntervalType_Object((1,3,6,1,4,1,9,9,834,1,2,3,1,1),_CooIntervalType_Type())
cooIntervalType.setMaxAccess(_O)
if mibBuilder.loadTexts:cooIntervalType.setStatus(_B)
class _CooIntervalNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_CooIntervalNum_Type.__name__=_G
_CooIntervalNum_Object=MibTableColumn
cooIntervalNum=_CooIntervalNum_Object((1,3,6,1,4,1,9,9,834,1,2,3,1,2),_CooIntervalNum_Type())
cooIntervalNum.setMaxAccess(_O)
if mibBuilder.loadTexts:cooIntervalNum.setStatus(_B)
_CooIntervalTXPowerMax_Type=CoiOpticalPower
_CooIntervalTXPowerMax_Object=MibTableColumn
cooIntervalTXPowerMax=_CooIntervalTXPowerMax_Object((1,3,6,1,4,1,9,9,834,1,2,3,1,3),_CooIntervalTXPowerMax_Type())
cooIntervalTXPowerMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cooIntervalTXPowerMax.setStatus(_B)
if mibBuilder.loadTexts:cooIntervalTXPowerMax.setUnits(_E)
_CooIntervalRXPowerMax_Type=CoiOpticalPower
_CooIntervalRXPowerMax_Object=MibTableColumn
cooIntervalRXPowerMax=_CooIntervalRXPowerMax_Object((1,3,6,1,4,1,9,9,834,1,2,3,1,4),_CooIntervalRXPowerMax_Type())
cooIntervalRXPowerMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cooIntervalRXPowerMax.setStatus(_B)
if mibBuilder.loadTexts:cooIntervalRXPowerMax.setUnits(_E)
class _CooIntervalLBCMax_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CooIntervalLBCMax_Type.__name__=_G
_CooIntervalLBCMax_Object=MibTableColumn
cooIntervalLBCMax=_CooIntervalLBCMax_Object((1,3,6,1,4,1,9,9,834,1,2,3,1,5),_CooIntervalLBCMax_Type())
cooIntervalLBCMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cooIntervalLBCMax.setStatus(_B)
if mibBuilder.loadTexts:cooIntervalLBCMax.setUnits(_K)
_CooIntervalTXPowerMin_Type=CoiOpticalPower
_CooIntervalTXPowerMin_Object=MibTableColumn
cooIntervalTXPowerMin=_CooIntervalTXPowerMin_Object((1,3,6,1,4,1,9,9,834,1,2,3,1,6),_CooIntervalTXPowerMin_Type())
cooIntervalTXPowerMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cooIntervalTXPowerMin.setStatus(_B)
if mibBuilder.loadTexts:cooIntervalTXPowerMin.setUnits(_E)
_CooIntervalRXPowerMin_Type=CoiOpticalPower
_CooIntervalRXPowerMin_Object=MibTableColumn
cooIntervalRXPowerMin=_CooIntervalRXPowerMin_Object((1,3,6,1,4,1,9,9,834,1,2,3,1,7),_CooIntervalRXPowerMin_Type())
cooIntervalRXPowerMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cooIntervalRXPowerMin.setStatus(_B)
if mibBuilder.loadTexts:cooIntervalRXPowerMin.setUnits(_E)
class _CooIntervalLBCMin_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CooIntervalLBCMin_Type.__name__=_G
_CooIntervalLBCMin_Object=MibTableColumn
cooIntervalLBCMin=_CooIntervalLBCMin_Object((1,3,6,1,4,1,9,9,834,1,2,3,1,8),_CooIntervalLBCMin_Type())
cooIntervalLBCMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cooIntervalLBCMin.setStatus(_B)
if mibBuilder.loadTexts:cooIntervalLBCMin.setUnits(_K)
_CooIntervalTXPowerAvg_Type=CoiOpticalPower
_CooIntervalTXPowerAvg_Object=MibTableColumn
cooIntervalTXPowerAvg=_CooIntervalTXPowerAvg_Object((1,3,6,1,4,1,9,9,834,1,2,3,1,9),_CooIntervalTXPowerAvg_Type())
cooIntervalTXPowerAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:cooIntervalTXPowerAvg.setStatus(_B)
if mibBuilder.loadTexts:cooIntervalTXPowerAvg.setUnits(_E)
_CooIntervalRXPowerAvg_Type=CoiOpticalPower
_CooIntervalRXPowerAvg_Object=MibTableColumn
cooIntervalRXPowerAvg=_CooIntervalRXPowerAvg_Object((1,3,6,1,4,1,9,9,834,1,2,3,1,10),_CooIntervalRXPowerAvg_Type())
cooIntervalRXPowerAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:cooIntervalRXPowerAvg.setStatus(_B)
if mibBuilder.loadTexts:cooIntervalRXPowerAvg.setUnits(_E)
class _CooIntervalLBCAvg_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CooIntervalLBCAvg_Type.__name__=_G
_CooIntervalLBCAvg_Object=MibTableColumn
cooIntervalLBCAvg=_CooIntervalLBCAvg_Object((1,3,6,1,4,1,9,9,834,1,2,3,1,11),_CooIntervalLBCAvg_Type())
cooIntervalLBCAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:cooIntervalLBCAvg.setStatus(_B)
if mibBuilder.loadTexts:cooIntervalLBCAvg.setUnits(_K)
_CooIntervalTimestamp_Type=OctetString
_CooIntervalTimestamp_Object=MibTableColumn
cooIntervalTimestamp=_CooIntervalTimestamp_Object((1,3,6,1,4,1,9,9,834,1,2,3,1,12),_CooIntervalTimestamp_Type())
cooIntervalTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cooIntervalTimestamp.setStatus(_B)
_CooIntervalAmpliGainMin_Type=Integer32
_CooIntervalAmpliGainMin_Object=MibTableColumn
cooIntervalAmpliGainMin=_CooIntervalAmpliGainMin_Object((1,3,6,1,4,1,9,9,834,1,2,3,1,13),_CooIntervalAmpliGainMin_Type())
cooIntervalAmpliGainMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cooIntervalAmpliGainMin.setStatus(_B)
if mibBuilder.loadTexts:cooIntervalAmpliGainMin.setUnits(_F)
_CooIntervalAmpliGainMax_Type=Integer32
_CooIntervalAmpliGainMax_Object=MibTableColumn
cooIntervalAmpliGainMax=_CooIntervalAmpliGainMax_Object((1,3,6,1,4,1,9,9,834,1,2,3,1,14),_CooIntervalAmpliGainMax_Type())
cooIntervalAmpliGainMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cooIntervalAmpliGainMax.setStatus(_B)
if mibBuilder.loadTexts:cooIntervalAmpliGainMax.setUnits(_F)
_CooIntervalAmpliGainAvg_Type=Integer32
_CooIntervalAmpliGainAvg_Object=MibTableColumn
cooIntervalAmpliGainAvg=_CooIntervalAmpliGainAvg_Object((1,3,6,1,4,1,9,9,834,1,2,3,1,15),_CooIntervalAmpliGainAvg_Type())
cooIntervalAmpliGainAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:cooIntervalAmpliGainAvg.setStatus(_B)
_CooIntervalAmpliGainTiltMin_Type=Integer32
_CooIntervalAmpliGainTiltMin_Object=MibTableColumn
cooIntervalAmpliGainTiltMin=_CooIntervalAmpliGainTiltMin_Object((1,3,6,1,4,1,9,9,834,1,2,3,1,16),_CooIntervalAmpliGainTiltMin_Type())
cooIntervalAmpliGainTiltMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cooIntervalAmpliGainTiltMin.setStatus(_B)
if mibBuilder.loadTexts:cooIntervalAmpliGainTiltMin.setUnits(_F)
_CooIntervalAmpliGainTiltMax_Type=Integer32
_CooIntervalAmpliGainTiltMax_Object=MibTableColumn
cooIntervalAmpliGainTiltMax=_CooIntervalAmpliGainTiltMax_Object((1,3,6,1,4,1,9,9,834,1,2,3,1,17),_CooIntervalAmpliGainTiltMax_Type())
cooIntervalAmpliGainTiltMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cooIntervalAmpliGainTiltMax.setStatus(_B)
if mibBuilder.loadTexts:cooIntervalAmpliGainTiltMax.setUnits(_F)
_CooIntervalAmpliGainTiltAvg_Type=Integer32
_CooIntervalAmpliGainTiltAvg_Object=MibTableColumn
cooIntervalAmpliGainTiltAvg=_CooIntervalAmpliGainTiltAvg_Object((1,3,6,1,4,1,9,9,834,1,2,3,1,18),_CooIntervalAmpliGainTiltAvg_Type())
cooIntervalAmpliGainTiltAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:cooIntervalAmpliGainTiltAvg.setStatus(_B)
if mibBuilder.loadTexts:cooIntervalAmpliGainTiltAvg.setUnits(_F)
_CooOtsEquipmentAlarmGroup_ObjectIdentity=ObjectIdentity
cooOtsEquipmentAlarmGroup=_CooOtsEquipmentAlarmGroup_ObjectIdentity((1,3,6,1,4,1,9,9,834,1,5))
_CooOtsAlarmLocation_Type=SnmpAdminString
_CooOtsAlarmLocation_Object=MibScalar
cooOtsAlarmLocation=_CooOtsAlarmLocation_Object((1,3,6,1,4,1,9,9,834,1,5,1),_CooOtsAlarmLocation_Type())
cooOtsAlarmLocation.setMaxAccess(_L)
if mibBuilder.loadTexts:cooOtsAlarmLocation.setStatus(_B)
_CooOtsAlarmType_Type=CoiOptAlarmType
_CooOtsAlarmType_Object=MibScalar
cooOtsAlarmType=_CooOtsAlarmType_Object((1,3,6,1,4,1,9,9,834,1,5,2),_CooOtsAlarmType_Type())
cooOtsAlarmType.setMaxAccess(_L)
if mibBuilder.loadTexts:cooOtsAlarmType.setStatus(_B)
_CooOtsAlarmTimeStamp_Type=TimeStamp
_CooOtsAlarmTimeStamp_Object=MibScalar
cooOtsAlarmTimeStamp=_CooOtsAlarmTimeStamp_Object((1,3,6,1,4,1,9,9,834,1,5,3),_CooOtsAlarmTimeStamp_Type())
cooOtsAlarmTimeStamp.setMaxAccess(_L)
if mibBuilder.loadTexts:cooOtsAlarmTimeStamp.setStatus(_B)
_CooOtsAlarmName_Type=SnmpAdminString
_CooOtsAlarmName_Object=MibScalar
cooOtsAlarmName=_CooOtsAlarmName_Object((1,3,6,1,4,1,9,9,834,1,5,4),_CooOtsAlarmName_Type())
cooOtsAlarmName.setMaxAccess(_L)
if mibBuilder.loadTexts:cooOtsAlarmName.setStatus(_B)
_CooOtsAlarmAdditionalInfo_Type=SnmpAdminString
_CooOtsAlarmAdditionalInfo_Object=MibScalar
cooOtsAlarmAdditionalInfo=_CooOtsAlarmAdditionalInfo_Object((1,3,6,1,4,1,9,9,834,1,5,5),_CooOtsAlarmAdditionalInfo_Type())
cooOtsAlarmAdditionalInfo.setMaxAccess(_L)
if mibBuilder.loadTexts:cooOtsAlarmAdditionalInfo.setStatus(_B)
_CooOtsAlarmSeverity_Type=CoiOptAlarmSeverity
_CooOtsAlarmSeverity_Object=MibScalar
cooOtsAlarmSeverity=_CooOtsAlarmSeverity_Object((1,3,6,1,4,1,9,9,834,1,5,6),_CooOtsAlarmSeverity_Type())
cooOtsAlarmSeverity.setMaxAccess(_L)
if mibBuilder.loadTexts:cooOtsAlarmSeverity.setStatus(_B)
_CooOtsAlarmStatus_Type=CoiOptAlarmStatus
_CooOtsAlarmStatus_Object=MibScalar
cooOtsAlarmStatus=_CooOtsAlarmStatus_Object((1,3,6,1,4,1,9,9,834,1,5,7),_CooOtsAlarmStatus_Type())
cooOtsAlarmStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:cooOtsAlarmStatus.setStatus(_B)
_CooOtsAlarmServiceAffecting_Type=CoiOptAlarmServiceAffecting
_CooOtsAlarmServiceAffecting_Object=MibScalar
cooOtsAlarmServiceAffecting=_CooOtsAlarmServiceAffecting_Object((1,3,6,1,4,1,9,9,834,1,5,8),_CooOtsAlarmServiceAffecting_Type())
cooOtsAlarmServiceAffecting.setMaxAccess(_L)
if mibBuilder.loadTexts:cooOtsAlarmServiceAffecting.setStatus(_B)
_CiscoOpticalOtsMIBConformance_ObjectIdentity=ObjectIdentity
ciscoOpticalOtsMIBConformance=_CiscoOpticalOtsMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,834,2))
_CiscoOpticalOtsMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoOpticalOtsMIBCompliances=_CiscoOpticalOtsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,834,2,1))
_CiscoOpticalOtsMIBGroups_ObjectIdentity=ObjectIdentity
ciscoOpticalOtsMIBGroups=_CiscoOpticalOtsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,834,2,2))
cooOtsGroup=ObjectGroup((1,3,6,1,4,1,9,9,834,2,2,1))
cooOtsGroup.setObjects(*((_A,_p),(_A,_At),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_A6),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_Ax),(_A,_Ay),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS)))
if mibBuilder.loadTexts:cooOtsGroup.setStatus(_B)
cooOtsOchGroup=ObjectGroup((1,3,6,1,4,1,9,9,834,2,2,2))
cooOtsOchGroup.setObjects(*((_A,_AT),(_A,_Az),(_A,_A_),(_A,_B0),(_A,_AU),(_A,_AV),(_A,_B1),(_A,_B2),(_A,_B3),(_A,_B4),(_A,_B5),(_A,_AW),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_B6)))
if mibBuilder.loadTexts:cooOtsOchGroup.setStatus(_B)
cooOtsControllerGroup=ObjectGroup((1,3,6,1,4,1,9,9,834,2,2,3))
cooOtsControllerGroup.setObjects(*((_A,_s),(_A,_t),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:cooOtsControllerGroup.setStatus(_B)
cooOtsOchControllerGroup=ObjectGroup((1,3,6,1,4,1,9,9,834,2,2,4))
cooOtsOchControllerGroup.setObjects(*((_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:cooOtsOchControllerGroup.setStatus(_B)
cooOtsThresholdGroup=ObjectGroup((1,3,6,1,4,1,9,9,834,2,2,5))
cooOtsThresholdGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_B7),(_A,_B8),(_A,_B9),(_A,_BA),(_A,_BB),(_A,_BC),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG)))
if mibBuilder.loadTexts:cooOtsThresholdGroup.setStatus(_B)
cooOtsCurrentGroup=ObjectGroup((1,3,6,1,4,1,9,9,834,2,2,6))
cooOtsCurrentGroup.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_BD),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM)))
if mibBuilder.loadTexts:cooOtsCurrentGroup.setStatus(_B)
cooOtsIntervalGroup=ObjectGroup((1,3,6,1,4,1,9,9,834,2,2,7))
cooOtsIntervalGroup.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_BE),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS)))
if mibBuilder.loadTexts:cooOtsIntervalGroup.setStatus(_B)
cooOtsNotifEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,834,2,2,8))
cooOtsNotifEnableGroup.setObjects((_A,_BF))
if mibBuilder.loadTexts:cooOtsNotifEnableGroup.setStatus(_B)
cooOtsEquipmentAlarmInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,834,2,2,11))
cooOtsEquipmentAlarmInfoGroup.setObjects(*((_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae)))
if mibBuilder.loadTexts:cooOtsEquipmentAlarmInfoGroup.setStatus(_B)
cooOtsPowerGroup=ObjectGroup((1,3,6,1,4,1,9,9,834,2,2,12))
cooOtsPowerGroup.setObjects(*((_A,_u),(_A,_v),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:cooOtsPowerGroup.setStatus(_B)
cooOtsOchNotifEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,834,2,2,13))
cooOtsOchNotifEnableGroup.setObjects((_A,_BG))
if mibBuilder.loadTexts:cooOtsOchNotifEnableGroup.setStatus(_B)
cooOtsStatusChange=NotificationType((1,3,6,1,4,1,9,9,834,0,1))
cooOtsStatusChange.setObjects(*((_I,_J),(_I,_N),(_A,_p),(_A,_A6)))
if mibBuilder.loadTexts:cooOtsStatusChange.setStatus(_B)
cooOtsOchStatusChange=NotificationType((1,3,6,1,4,1,9,9,834,0,2))
cooOtsOchStatusChange.setObjects(*((_I,_J),(_I,_N),(_A,_AT),(_A,_AW)))
if mibBuilder.loadTexts:cooOtsOchStatusChange.setStatus(_B)
cooOtsEquipmentAlarm=NotificationType((1,3,6,1,4,1,9,9,834,0,3))
cooOtsEquipmentAlarm.setObjects(*((_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_I,_N)))
if mibBuilder.loadTexts:cooOtsEquipmentAlarm.setStatus(_B)
cooOtsNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,834,2,2,9))
cooOtsNotifGroup.setObjects(*((_A,_BH),(_A,_Af)))
if mibBuilder.loadTexts:cooOtsNotifGroup.setStatus(_B)
cooOtsOchNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,834,2,2,10))
cooOtsOchNotifGroup.setObjects(*((_A,_BI),(_A,_Af)))
if mibBuilder.loadTexts:cooOtsOchNotifGroup.setStatus(_B)
ciscoOpticalOtsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,834,2,1,1))
ciscoOpticalOtsMIBCompliance.setObjects(*((_A,_BJ),(_A,_BK),(_A,_BL),(_A,_BM),(_A,_BN),(_A,_BO),(_A,_BP),(_A,_BQ),(_A,_BR),(_A,_BS),(_A,_BT),(_A,_BU),(_A,_BV)))
if mibBuilder.loadTexts:ciscoOpticalOtsMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CiscoOpticalOtsPortType':CiscoOpticalOtsPortType,'CiscoOpticalOtsGainInDb':CiscoOpticalOtsGainInDb,'CiscoOpticalOtsTiltInDb':CiscoOpticalOtsTiltInDb,'CiscoOpticalOtsVoaAttenInDb':CiscoOpticalOtsVoaAttenInDb,'CiscoOpticalOtsLaserStatus':CiscoOpticalOtsLaserStatus,'CiscoOpticalOtsAmpliControlMode':CiscoOpticalOtsAmpliControlMode,'CiscoOpticalOtsAmpliGainRange':CiscoOpticalOtsAmpliGainRange,'CiscoOpticalOtsAmpliSafetyCtrlMode':CiscoOpticalOtsAmpliSafetyCtrlMode,'CiscoOpticalOtsOsri':CiscoOpticalOtsOsri,'CiscoOpticalOtsProtectionPortRole':CiscoOpticalOtsProtectionPortRole,'CiscoOpticalOtsState':CiscoOpticalOtsState,'CiscoOpticalOtsTranspAdminState':CiscoOpticalOtsTranspAdminState,'ciscoOpticalOtsMIB':ciscoOpticalOtsMIB,'ciscoOpticalOtsMIBNotifs':ciscoOpticalOtsMIBNotifs,_BH:cooOtsStatusChange,_BI:cooOtsOchStatusChange,_Af:cooOtsEquipmentAlarm,'ciscoOpticalOtsMIBObjects':ciscoOpticalOtsMIBObjects,'cooOtsController':cooOtsController,_BF:cooOtsNotifEnabled,'cooOtsControllerTable':cooOtsControllerTable,'cooOtsControllerEntry':cooOtsControllerEntry,_p:cooOtsControllerPortType,_At:cooOtsControllerLaserStatus,_q:cooOtsControllerRXPower,_r:cooOtsControllerTXPower,_s:cooOtsControllerAmpliGain,_t:cooOtsControllerAmpliTilt,_u:cooOtsControllerTotalRXPower,_v:cooOtsControllerTotalTXPower,_w:cooOtsControllerRXVoaAttenuation,_x:cooOtsControllerTXVoaAttenuation,_y:cooOtsControllerRXLowThreshold,_z:cooOtsControllerTXLowThreshold,_A0:cooOtsControllerAmpliChannelPwr,_A1:cooOtsControllerChannelPwrMaxDelta,_A2:cooOtsControllerAmpliControlMode,_A3:cooOtsControllerAmpliGainRange,_A4:cooOtsControllerAmpliSafetyCtrlMode,_A5:cooOtsControllerOsri,_Au:cooOtsControllerProtectionPortRole,_Av:cooOtsControllerState,_Aw:cooOtsControllerTranspAdminState,_A6:cooOtsControllerAlarmState,_Ax:cooOtsControllerRXSpanLoss,_Ay:cooOtsControllerTXSpanLoss,_A7:cooOtsControllerRXEnabled,_A8:cooOtsControllerTXEnabled,'cooOtsOchControllerTable':cooOtsOchControllerTable,'cooOtsOchControllerEntry':cooOtsOchControllerEntry,_AT:cooOtsOchControllerPortType,_Az:cooOtsOchControllerLaserStatus,_A_:cooOtsOchControllerRXPower,_B0:cooOtsOchControllerTXPower,_AU:cooOtsOchControllerRXLowThreshold,_AV:cooOtsOchControllerTXLowThreshold,_B1:cooOtsOchControllerWavelength,_B2:cooOtsOchControllerFrequency,_B3:cooOtsOchControllerChannelNumber,_B4:cooOtsOchControllerState,_B5:cooOtsOchControllerTranspAdminState,_AW:cooOtsOchControllerAlarmState,_B6:cooOtsOchControllerWidth,_BG:cooOtsOchNotifEnabled,'cooOtsPerformanceMonitoring':cooOtsPerformanceMonitoring,'cooOtsThresholdTable':cooOtsThresholdTable,'cooOtsThresholdEntry':cooOtsThresholdEntry,_Ap:cooThreshIntervalType,_P:cooThreshTXPowerMin,_Q:cooThreshRXPowerMin,_R:cooThreshLBCMin,_S:cooThreshTXPowerMax,_T:cooThreshRXPowerMax,_U:cooThreshLBCMax,_B7:cooThreshTXPowerEnableMin,_B8:cooThreshRXPowerEnableMin,_B9:cooThreshLBCEnableMin,_BA:cooThreshTXPowerEnableMax,_BB:cooThreshRXPowerEnableMax,_BC:cooThreshLBCEnableMax,_A9:cooThreshAmpliGainMin,_AA:cooThreshAmpliGainMax,_AB:cooThreshAmpliGainEnableMax,_AC:cooThreshAmpliGainEnableMin,_AD:cooThreshAmpliGainTiltMin,_AE:cooThreshAmpliGainTiltMax,_AF:cooThreshAmpliGainTiltEnableMax,_AG:cooThreshAmpliGainTiltEnableMin,'cooOtsCurrentTable':cooOtsCurrentTable,'cooOtsCurrentEntry':cooOtsCurrentEntry,_Aq:cooCurrentIntervalType,_V:cooCurrentTXPowerMax,_W:cooCurrentRXPowerMax,_X:cooCurrentLBCMax,_Y:cooCurrentTXPowerMin,_Z:cooCurrentRXPowerMin,_a:cooCurrentLBCMin,_b:cooCurrentTXPowerAvg,_c:cooCurrentRXPowerAvg,_d:cooCurrentLBCAvg,_BD:cooCurrentTimestamp,_AH:cooCurrentAmpliGainMin,_AI:cooCurrentAmpliGainMax,_AJ:cooCurrentAmpliGainAvg,_AK:cooCurrentAmpliGainTiltMin,_AL:cooCurrentAmpliGainTiltMax,_AM:cooCurrentAmpliGainTiltAvg,'cooOtsIntervalTable':cooOtsIntervalTable,'cooOtsIntervalEntry':cooOtsIntervalEntry,_Ar:cooIntervalType,_As:cooIntervalNum,_e:cooIntervalTXPowerMax,_f:cooIntervalRXPowerMax,_g:cooIntervalLBCMax,_h:cooIntervalTXPowerMin,_i:cooIntervalRXPowerMin,_j:cooIntervalLBCMin,_k:cooIntervalTXPowerAvg,_l:cooIntervalRXPowerAvg,_m:cooIntervalLBCAvg,_BE:cooIntervalTimestamp,_AN:cooIntervalAmpliGainMin,_AO:cooIntervalAmpliGainMax,_AP:cooIntervalAmpliGainAvg,_AQ:cooIntervalAmpliGainTiltMin,_AR:cooIntervalAmpliGainTiltMax,_AS:cooIntervalAmpliGainTiltAvg,'cooOtsEquipmentAlarmGroup':cooOtsEquipmentAlarmGroup,_AX:cooOtsAlarmLocation,_AY:cooOtsAlarmType,_AZ:cooOtsAlarmTimeStamp,_Aa:cooOtsAlarmName,_Ab:cooOtsAlarmAdditionalInfo,_Ac:cooOtsAlarmSeverity,_Ad:cooOtsAlarmStatus,_Ae:cooOtsAlarmServiceAffecting,'ciscoOpticalOtsMIBConformance':ciscoOpticalOtsMIBConformance,'ciscoOpticalOtsMIBCompliances':ciscoOpticalOtsMIBCompliances,'ciscoOpticalOtsMIBCompliance':ciscoOpticalOtsMIBCompliance,'ciscoOpticalOtsMIBGroups':ciscoOpticalOtsMIBGroups,_BJ:cooOtsGroup,_BK:cooOtsOchGroup,_BL:cooOtsControllerGroup,_BM:cooOtsOchControllerGroup,_BN:cooOtsThresholdGroup,_BO:cooOtsCurrentGroup,_BP:cooOtsIntervalGroup,_BQ:cooOtsNotifEnableGroup,_BR:cooOtsNotifGroup,_BS:cooOtsOchNotifGroup,_BT:cooOtsEquipmentAlarmInfoGroup,_BU:cooOtsPowerGroup,_BV:cooOtsOchNotifEnableGroup})