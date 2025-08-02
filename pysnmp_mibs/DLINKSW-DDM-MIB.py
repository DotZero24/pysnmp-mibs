_AD='dDdmNotifyGroup'
_AC='dDdmCfgGroup'
_AB='dDdmInfoGroup'
_AA='dDdmWarningTrap'
_A9='dDdmAlarmTrap'
_A8='dDdmThresholdCfgRowStatus'
_A7='dDdmThresholdCfgValue'
_A6='dDdmShutdownLevel'
_A5='dDdmIfCfgEnabled'
_A4='dDdmNotifyEnable'
_A3='dDdmIfInfoLowAlarmRxPower'
_A2='dDdmIfInfoLowWarnRxPower'
_A1='dDdmIfInfoHighWarnRxPower'
_A0='dDdmIfInfoHighAlarmRxPower'
_z='dDdmIfInfoRxPowerState'
_y='dDdmIfInfoCurrentRxPower'
_x='dDdmIfInfoLowAlarmTxPower'
_w='dDdmIfInfoLowWarnTxPower'
_v='dDdmIfInfoHighWarnTxPower'
_u='dDdmIfInfoHighAlarmTxPower'
_t='dDdmIfInfoTxPowerState'
_s='dDdmIfInfoCurrentTxPower'
_r='dDdmIfInfoLowAlarmBiasCurrent'
_q='dDdmIfInfoLowWarnBiasCurrent'
_p='dDdmIfInfoHighWarnBiasCurrent'
_o='dDdmIfInfoHighAlarmBiasCurrent'
_n='dDdmIfInfoBiasCurrentState'
_m='dDdmIfInfoCurrentBiasCurrent'
_l='dDdmIfInfoLowAlarmVoltage'
_k='dDdmIfInfoLowWarnVoltage'
_j='dDdmIfInfoHighWarnVoltage'
_i='dDdmIfInfoHighAlarmVoltage'
_h='dDdmIfInfoVoltageState'
_g='dDdmIfInfoCurrentVoltage'
_f='dDdmIfInfoLowAlarmTemperature'
_e='dDdmIfInfoLowWarnTemperature'
_d='dDdmIfInfoHighWarnTemperature'
_c='dDdmIfInfoHighAlarmTemperature'
_b='dDdmIfInfoTemperatureState'
_a='dDdmIfInfoCurrentTemperature'
_Z='read-create'
_Y='not-accessible'
_X='rxPowerMw'
_W='txPowerMw'
_V='biasCurrent'
_U='voltage'
_T='temperature'
_S='dDmThresholdAbnormalLevel'
_R='dDdmThresholdComponent'
_Q='warning'
_P='read-write'
_O='dDdmNotifyInfoThresholdExceedOrRecover'
_N='dDdmNotifyInfoAbnormalLevel'
_M='dDdmNotifyInfoComponent'
_L='dDdmNotifyInfoIfIndex'
_K='accessible-for-notify'
_J='ifIndex'
_I='IF-MIB'
_H='milli-amperes'
_G='centi-Volt'
_F='milli-degrees Celsius'
_E='Integer32'
_D='tenths of a microwatt'
_C='read-only'
_B='current'
_A='DLINKSW-DDM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkIndustrialCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkIndustrialCommon')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_I,'InterfaceIndex',_J)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
dlinkSwDdmMIB=ModuleIdentity((1,3,6,1,4,1,171,14,72))
if mibBuilder.loadTexts:dlinkSwDdmMIB.setRevisions(('2013-02-04 00:00','2013-09-05 00:00'))
class DlinkThresholdState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('normal',0),('higherAlarm',1),('higherWarning',2),('lowerWarning',3),('lowerAlarm',4)))
_DDdmMIBNotifications_ObjectIdentity=ObjectIdentity
dDdmMIBNotifications=_DDdmMIBNotifications_ObjectIdentity((1,3,6,1,4,1,171,14,72,0))
_DDdmMIBObjects_ObjectIdentity=ObjectIdentity
dDdmMIBObjects=_DDdmMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,14,72,1))
_DDdmCtrl_ObjectIdentity=ObjectIdentity
dDdmCtrl=_DDdmCtrl_ObjectIdentity((1,3,6,1,4,1,171,14,72,1,1))
class _DDdmNotifyEnable_Type(Bits):namedValues=NamedValues(*(('alarm',0),(_Q,1)))
_DDdmNotifyEnable_Type.__name__='Bits'
_DDdmNotifyEnable_Object=MibScalar
dDdmNotifyEnable=_DDdmNotifyEnable_Object((1,3,6,1,4,1,171,14,72,1,1,1),_DDdmNotifyEnable_Type())
dDdmNotifyEnable.setMaxAccess(_P)
if mibBuilder.loadTexts:dDdmNotifyEnable.setStatus(_B)
_DDdmIfCtrl_ObjectIdentity=ObjectIdentity
dDdmIfCtrl=_DDdmIfCtrl_ObjectIdentity((1,3,6,1,4,1,171,14,72,1,2))
_DDdmIfCfgTable_Object=MibTable
dDdmIfCfgTable=_DDdmIfCfgTable_Object((1,3,6,1,4,1,171,14,72,1,2,1))
if mibBuilder.loadTexts:dDdmIfCfgTable.setStatus(_B)
_DDdmIfCfgEntry_Object=MibTableRow
dDdmIfCfgEntry=_DDdmIfCfgEntry_Object((1,3,6,1,4,1,171,14,72,1,2,1,1))
dDdmIfCfgEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:dDdmIfCfgEntry.setStatus(_B)
_DDdmIfCfgEnabled_Type=TruthValue
_DDdmIfCfgEnabled_Object=MibTableColumn
dDdmIfCfgEnabled=_DDdmIfCfgEnabled_Object((1,3,6,1,4,1,171,14,72,1,2,1,1,1),_DDdmIfCfgEnabled_Type())
dDdmIfCfgEnabled.setMaxAccess(_P)
if mibBuilder.loadTexts:dDdmIfCfgEnabled.setStatus(_B)
class _DDdmShutdownLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('alarm',2),(_Q,3)))
_DDdmShutdownLevel_Type.__name__=_E
_DDdmShutdownLevel_Object=MibTableColumn
dDdmShutdownLevel=_DDdmShutdownLevel_Object((1,3,6,1,4,1,171,14,72,1,2,1,1,2),_DDdmShutdownLevel_Type())
dDdmShutdownLevel.setMaxAccess(_P)
if mibBuilder.loadTexts:dDdmShutdownLevel.setStatus(_B)
_DDdmThresholdMgmt_ObjectIdentity=ObjectIdentity
dDdmThresholdMgmt=_DDdmThresholdMgmt_ObjectIdentity((1,3,6,1,4,1,171,14,72,1,3))
_DDdmThresholdCfgTable_Object=MibTable
dDdmThresholdCfgTable=_DDdmThresholdCfgTable_Object((1,3,6,1,4,1,171,14,72,1,3,1))
if mibBuilder.loadTexts:dDdmThresholdCfgTable.setStatus(_B)
_DDdmThresholdCfgEntry_Object=MibTableRow
dDdmThresholdCfgEntry=_DDdmThresholdCfgEntry_Object((1,3,6,1,4,1,171,14,72,1,3,1,1))
dDdmThresholdCfgEntry.setIndexNames((0,_I,_J),(0,_A,_R),(0,_A,_S))
if mibBuilder.loadTexts:dDdmThresholdCfgEntry.setStatus(_B)
class _DDdmThresholdComponent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_T,1),(_U,2),(_V,3),(_W,4),('txPowerDbm',5),(_X,6),('rxPowerDbm',7)))
_DDdmThresholdComponent_Type.__name__=_E
_DDdmThresholdComponent_Object=MibTableColumn
dDdmThresholdComponent=_DDdmThresholdComponent_Object((1,3,6,1,4,1,171,14,72,1,3,1,1,1),_DDdmThresholdComponent_Type())
dDdmThresholdComponent.setMaxAccess(_Y)
if mibBuilder.loadTexts:dDdmThresholdComponent.setStatus(_B)
class _DDmThresholdAbnormalLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('highAlarm',1),('highWarning',2),('lowWarning',3),('lowAlarm',4)))
_DDmThresholdAbnormalLevel_Type.__name__=_E
_DDmThresholdAbnormalLevel_Object=MibTableColumn
dDmThresholdAbnormalLevel=_DDmThresholdAbnormalLevel_Object((1,3,6,1,4,1,171,14,72,1,3,1,1,2),_DDmThresholdAbnormalLevel_Type())
dDmThresholdAbnormalLevel.setMaxAccess(_Y)
if mibBuilder.loadTexts:dDmThresholdAbnormalLevel.setStatus(_B)
_DDdmThresholdCfgValue_Type=Integer32
_DDdmThresholdCfgValue_Object=MibTableColumn
dDdmThresholdCfgValue=_DDdmThresholdCfgValue_Object((1,3,6,1,4,1,171,14,72,1,3,1,1,3),_DDdmThresholdCfgValue_Type())
dDdmThresholdCfgValue.setMaxAccess(_Z)
if mibBuilder.loadTexts:dDdmThresholdCfgValue.setStatus(_B)
_DDdmThresholdCfgRowStatus_Type=RowStatus
_DDdmThresholdCfgRowStatus_Object=MibTableColumn
dDdmThresholdCfgRowStatus=_DDdmThresholdCfgRowStatus_Object((1,3,6,1,4,1,171,14,72,1,3,1,1,4),_DDdmThresholdCfgRowStatus_Type())
dDdmThresholdCfgRowStatus.setMaxAccess(_Z)
if mibBuilder.loadTexts:dDdmThresholdCfgRowStatus.setStatus(_B)
_DDdmInfo_ObjectIdentity=ObjectIdentity
dDdmInfo=_DDdmInfo_ObjectIdentity((1,3,6,1,4,1,171,14,72,1,4))
_DDdmIfInfoTable_Object=MibTable
dDdmIfInfoTable=_DDdmIfInfoTable_Object((1,3,6,1,4,1,171,14,72,1,4,1))
if mibBuilder.loadTexts:dDdmIfInfoTable.setStatus(_B)
_DDdmIfInfoEntry_Object=MibTableRow
dDdmIfInfoEntry=_DDdmIfInfoEntry_Object((1,3,6,1,4,1,171,14,72,1,4,1,1))
dDdmIfInfoEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:dDdmIfInfoEntry.setStatus(_B)
_DDdmIfInfoCurrentTemperature_Type=Integer32
_DDdmIfInfoCurrentTemperature_Object=MibTableColumn
dDdmIfInfoCurrentTemperature=_DDdmIfInfoCurrentTemperature_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,1),_DDdmIfInfoCurrentTemperature_Type())
dDdmIfInfoCurrentTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoCurrentTemperature.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoCurrentTemperature.setUnits(_F)
_DDdmIfInfoTemperatureState_Type=DlinkThresholdState
_DDdmIfInfoTemperatureState_Object=MibTableColumn
dDdmIfInfoTemperatureState=_DDdmIfInfoTemperatureState_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,2),_DDdmIfInfoTemperatureState_Type())
dDdmIfInfoTemperatureState.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoTemperatureState.setStatus(_B)
_DDdmIfInfoHighAlarmTemperature_Type=Integer32
_DDdmIfInfoHighAlarmTemperature_Object=MibTableColumn
dDdmIfInfoHighAlarmTemperature=_DDdmIfInfoHighAlarmTemperature_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,3),_DDdmIfInfoHighAlarmTemperature_Type())
dDdmIfInfoHighAlarmTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoHighAlarmTemperature.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoHighAlarmTemperature.setUnits(_F)
_DDdmIfInfoHighWarnTemperature_Type=Integer32
_DDdmIfInfoHighWarnTemperature_Object=MibTableColumn
dDdmIfInfoHighWarnTemperature=_DDdmIfInfoHighWarnTemperature_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,4),_DDdmIfInfoHighWarnTemperature_Type())
dDdmIfInfoHighWarnTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoHighWarnTemperature.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoHighWarnTemperature.setUnits(_F)
_DDdmIfInfoLowWarnTemperature_Type=Integer32
_DDdmIfInfoLowWarnTemperature_Object=MibTableColumn
dDdmIfInfoLowWarnTemperature=_DDdmIfInfoLowWarnTemperature_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,5),_DDdmIfInfoLowWarnTemperature_Type())
dDdmIfInfoLowWarnTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoLowWarnTemperature.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoLowWarnTemperature.setUnits(_F)
_DDdmIfInfoLowAlarmTemperature_Type=Integer32
_DDdmIfInfoLowAlarmTemperature_Object=MibTableColumn
dDdmIfInfoLowAlarmTemperature=_DDdmIfInfoLowAlarmTemperature_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,6),_DDdmIfInfoLowAlarmTemperature_Type())
dDdmIfInfoLowAlarmTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoLowAlarmTemperature.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoLowAlarmTemperature.setUnits(_F)
_DDdmIfInfoCurrentVoltage_Type=Integer32
_DDdmIfInfoCurrentVoltage_Object=MibTableColumn
dDdmIfInfoCurrentVoltage=_DDdmIfInfoCurrentVoltage_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,7),_DDdmIfInfoCurrentVoltage_Type())
dDdmIfInfoCurrentVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoCurrentVoltage.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoCurrentVoltage.setUnits(_G)
_DDdmIfInfoVoltageState_Type=DlinkThresholdState
_DDdmIfInfoVoltageState_Object=MibTableColumn
dDdmIfInfoVoltageState=_DDdmIfInfoVoltageState_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,8),_DDdmIfInfoVoltageState_Type())
dDdmIfInfoVoltageState.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoVoltageState.setStatus(_B)
_DDdmIfInfoHighAlarmVoltage_Type=Integer32
_DDdmIfInfoHighAlarmVoltage_Object=MibTableColumn
dDdmIfInfoHighAlarmVoltage=_DDdmIfInfoHighAlarmVoltage_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,9),_DDdmIfInfoHighAlarmVoltage_Type())
dDdmIfInfoHighAlarmVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoHighAlarmVoltage.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoHighAlarmVoltage.setUnits(_G)
_DDdmIfInfoHighWarnVoltage_Type=Integer32
_DDdmIfInfoHighWarnVoltage_Object=MibTableColumn
dDdmIfInfoHighWarnVoltage=_DDdmIfInfoHighWarnVoltage_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,10),_DDdmIfInfoHighWarnVoltage_Type())
dDdmIfInfoHighWarnVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoHighWarnVoltage.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoHighWarnVoltage.setUnits(_G)
_DDdmIfInfoLowWarnVoltage_Type=Integer32
_DDdmIfInfoLowWarnVoltage_Object=MibTableColumn
dDdmIfInfoLowWarnVoltage=_DDdmIfInfoLowWarnVoltage_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,11),_DDdmIfInfoLowWarnVoltage_Type())
dDdmIfInfoLowWarnVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoLowWarnVoltage.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoLowWarnVoltage.setUnits(_G)
_DDdmIfInfoLowAlarmVoltage_Type=Integer32
_DDdmIfInfoLowAlarmVoltage_Object=MibTableColumn
dDdmIfInfoLowAlarmVoltage=_DDdmIfInfoLowAlarmVoltage_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,12),_DDdmIfInfoLowAlarmVoltage_Type())
dDdmIfInfoLowAlarmVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoLowAlarmVoltage.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoLowAlarmVoltage.setUnits(_G)
_DDdmIfInfoCurrentBiasCurrent_Type=Integer32
_DDdmIfInfoCurrentBiasCurrent_Object=MibTableColumn
dDdmIfInfoCurrentBiasCurrent=_DDdmIfInfoCurrentBiasCurrent_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,13),_DDdmIfInfoCurrentBiasCurrent_Type())
dDdmIfInfoCurrentBiasCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoCurrentBiasCurrent.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoCurrentBiasCurrent.setUnits(_H)
_DDdmIfInfoBiasCurrentState_Type=DlinkThresholdState
_DDdmIfInfoBiasCurrentState_Object=MibTableColumn
dDdmIfInfoBiasCurrentState=_DDdmIfInfoBiasCurrentState_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,14),_DDdmIfInfoBiasCurrentState_Type())
dDdmIfInfoBiasCurrentState.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoBiasCurrentState.setStatus(_B)
_DDdmIfInfoHighAlarmBiasCurrent_Type=Integer32
_DDdmIfInfoHighAlarmBiasCurrent_Object=MibTableColumn
dDdmIfInfoHighAlarmBiasCurrent=_DDdmIfInfoHighAlarmBiasCurrent_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,15),_DDdmIfInfoHighAlarmBiasCurrent_Type())
dDdmIfInfoHighAlarmBiasCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoHighAlarmBiasCurrent.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoHighAlarmBiasCurrent.setUnits(_H)
_DDdmIfInfoHighWarnBiasCurrent_Type=Integer32
_DDdmIfInfoHighWarnBiasCurrent_Object=MibTableColumn
dDdmIfInfoHighWarnBiasCurrent=_DDdmIfInfoHighWarnBiasCurrent_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,16),_DDdmIfInfoHighWarnBiasCurrent_Type())
dDdmIfInfoHighWarnBiasCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoHighWarnBiasCurrent.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoHighWarnBiasCurrent.setUnits(_H)
_DDdmIfInfoLowWarnBiasCurrent_Type=Integer32
_DDdmIfInfoLowWarnBiasCurrent_Object=MibTableColumn
dDdmIfInfoLowWarnBiasCurrent=_DDdmIfInfoLowWarnBiasCurrent_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,17),_DDdmIfInfoLowWarnBiasCurrent_Type())
dDdmIfInfoLowWarnBiasCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoLowWarnBiasCurrent.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoLowWarnBiasCurrent.setUnits(_H)
_DDdmIfInfoLowAlarmBiasCurrent_Type=Integer32
_DDdmIfInfoLowAlarmBiasCurrent_Object=MibTableColumn
dDdmIfInfoLowAlarmBiasCurrent=_DDdmIfInfoLowAlarmBiasCurrent_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,18),_DDdmIfInfoLowAlarmBiasCurrent_Type())
dDdmIfInfoLowAlarmBiasCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoLowAlarmBiasCurrent.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoLowAlarmBiasCurrent.setUnits(_H)
_DDdmIfInfoCurrentTxPower_Type=Integer32
_DDdmIfInfoCurrentTxPower_Object=MibTableColumn
dDdmIfInfoCurrentTxPower=_DDdmIfInfoCurrentTxPower_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,19),_DDdmIfInfoCurrentTxPower_Type())
dDdmIfInfoCurrentTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoCurrentTxPower.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoCurrentTxPower.setUnits(_D)
_DDdmIfInfoTxPowerState_Type=DlinkThresholdState
_DDdmIfInfoTxPowerState_Object=MibTableColumn
dDdmIfInfoTxPowerState=_DDdmIfInfoTxPowerState_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,20),_DDdmIfInfoTxPowerState_Type())
dDdmIfInfoTxPowerState.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoTxPowerState.setStatus(_B)
_DDdmIfInfoHighAlarmTxPower_Type=Integer32
_DDdmIfInfoHighAlarmTxPower_Object=MibTableColumn
dDdmIfInfoHighAlarmTxPower=_DDdmIfInfoHighAlarmTxPower_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,21),_DDdmIfInfoHighAlarmTxPower_Type())
dDdmIfInfoHighAlarmTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoHighAlarmTxPower.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoHighAlarmTxPower.setUnits(_D)
_DDdmIfInfoHighWarnTxPower_Type=Integer32
_DDdmIfInfoHighWarnTxPower_Object=MibTableColumn
dDdmIfInfoHighWarnTxPower=_DDdmIfInfoHighWarnTxPower_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,22),_DDdmIfInfoHighWarnTxPower_Type())
dDdmIfInfoHighWarnTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoHighWarnTxPower.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoHighWarnTxPower.setUnits(_D)
_DDdmIfInfoLowWarnTxPower_Type=Integer32
_DDdmIfInfoLowWarnTxPower_Object=MibTableColumn
dDdmIfInfoLowWarnTxPower=_DDdmIfInfoLowWarnTxPower_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,23),_DDdmIfInfoLowWarnTxPower_Type())
dDdmIfInfoLowWarnTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoLowWarnTxPower.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoLowWarnTxPower.setUnits(_D)
_DDdmIfInfoLowAlarmTxPower_Type=Integer32
_DDdmIfInfoLowAlarmTxPower_Object=MibTableColumn
dDdmIfInfoLowAlarmTxPower=_DDdmIfInfoLowAlarmTxPower_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,24),_DDdmIfInfoLowAlarmTxPower_Type())
dDdmIfInfoLowAlarmTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoLowAlarmTxPower.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoLowAlarmTxPower.setUnits(_D)
_DDdmIfInfoCurrentRxPower_Type=Integer32
_DDdmIfInfoCurrentRxPower_Object=MibTableColumn
dDdmIfInfoCurrentRxPower=_DDdmIfInfoCurrentRxPower_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,25),_DDdmIfInfoCurrentRxPower_Type())
dDdmIfInfoCurrentRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoCurrentRxPower.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoCurrentRxPower.setUnits(_D)
_DDdmIfInfoRxPowerState_Type=DlinkThresholdState
_DDdmIfInfoRxPowerState_Object=MibTableColumn
dDdmIfInfoRxPowerState=_DDdmIfInfoRxPowerState_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,26),_DDdmIfInfoRxPowerState_Type())
dDdmIfInfoRxPowerState.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoRxPowerState.setStatus(_B)
_DDdmIfInfoHighAlarmRxPower_Type=Integer32
_DDdmIfInfoHighAlarmRxPower_Object=MibTableColumn
dDdmIfInfoHighAlarmRxPower=_DDdmIfInfoHighAlarmRxPower_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,27),_DDdmIfInfoHighAlarmRxPower_Type())
dDdmIfInfoHighAlarmRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoHighAlarmRxPower.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoHighAlarmRxPower.setUnits(_D)
_DDdmIfInfoHighWarnRxPower_Type=Integer32
_DDdmIfInfoHighWarnRxPower_Object=MibTableColumn
dDdmIfInfoHighWarnRxPower=_DDdmIfInfoHighWarnRxPower_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,28),_DDdmIfInfoHighWarnRxPower_Type())
dDdmIfInfoHighWarnRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoHighWarnRxPower.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoHighWarnRxPower.setUnits(_D)
_DDdmIfInfoLowWarnRxPower_Type=Integer32
_DDdmIfInfoLowWarnRxPower_Object=MibTableColumn
dDdmIfInfoLowWarnRxPower=_DDdmIfInfoLowWarnRxPower_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,29),_DDdmIfInfoLowWarnRxPower_Type())
dDdmIfInfoLowWarnRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoLowWarnRxPower.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoLowWarnRxPower.setUnits(_D)
_DDdmIfInfoLowAlarmRxPower_Type=Integer32
_DDdmIfInfoLowAlarmRxPower_Object=MibTableColumn
dDdmIfInfoLowAlarmRxPower=_DDdmIfInfoLowAlarmRxPower_Object((1,3,6,1,4,1,171,14,72,1,4,1,1,30),_DDdmIfInfoLowAlarmRxPower_Type())
dDdmIfInfoLowAlarmRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dDdmIfInfoLowAlarmRxPower.setStatus(_B)
if mibBuilder.loadTexts:dDdmIfInfoLowAlarmRxPower.setUnits(_D)
_DDdmNotifyInfo_ObjectIdentity=ObjectIdentity
dDdmNotifyInfo=_DDdmNotifyInfo_ObjectIdentity((1,3,6,1,4,1,171,14,72,1,5))
_DDdmNotifyInfoIfIndex_Type=InterfaceIndex
_DDdmNotifyInfoIfIndex_Object=MibScalar
dDdmNotifyInfoIfIndex=_DDdmNotifyInfoIfIndex_Object((1,3,6,1,4,1,171,14,72,1,5,1),_DDdmNotifyInfoIfIndex_Type())
dDdmNotifyInfoIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:dDdmNotifyInfoIfIndex.setStatus(_B)
class _DDdmNotifyInfoComponent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_T,1),(_U,2),(_V,3),(_W,4),(_X,5)))
_DDdmNotifyInfoComponent_Type.__name__=_E
_DDdmNotifyInfoComponent_Object=MibScalar
dDdmNotifyInfoComponent=_DDdmNotifyInfoComponent_Object((1,3,6,1,4,1,171,14,72,1,5,2),_DDdmNotifyInfoComponent_Type())
dDdmNotifyInfoComponent.setMaxAccess(_K)
if mibBuilder.loadTexts:dDdmNotifyInfoComponent.setStatus(_B)
class _DDdmNotifyInfoAbnormalLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('high',1),('low',2)))
_DDdmNotifyInfoAbnormalLevel_Type.__name__=_E
_DDdmNotifyInfoAbnormalLevel_Object=MibScalar
dDdmNotifyInfoAbnormalLevel=_DDdmNotifyInfoAbnormalLevel_Object((1,3,6,1,4,1,171,14,72,1,5,3),_DDdmNotifyInfoAbnormalLevel_Type())
dDdmNotifyInfoAbnormalLevel.setMaxAccess(_K)
if mibBuilder.loadTexts:dDdmNotifyInfoAbnormalLevel.setStatus(_B)
class _DDdmNotifyInfoThresholdExceedOrRecover_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('exceed',1),('recover',2)))
_DDdmNotifyInfoThresholdExceedOrRecover_Type.__name__=_E
_DDdmNotifyInfoThresholdExceedOrRecover_Object=MibScalar
dDdmNotifyInfoThresholdExceedOrRecover=_DDdmNotifyInfoThresholdExceedOrRecover_Object((1,3,6,1,4,1,171,14,72,1,5,4),_DDdmNotifyInfoThresholdExceedOrRecover_Type())
dDdmNotifyInfoThresholdExceedOrRecover.setMaxAccess(_K)
if mibBuilder.loadTexts:dDdmNotifyInfoThresholdExceedOrRecover.setStatus(_B)
_DDdmMIBConformance_ObjectIdentity=ObjectIdentity
dDdmMIBConformance=_DDdmMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,14,72,2))
_DDdmCompliances_ObjectIdentity=ObjectIdentity
dDdmCompliances=_DDdmCompliances_ObjectIdentity((1,3,6,1,4,1,171,14,72,2,1))
_DDdmGroups_ObjectIdentity=ObjectIdentity
dDdmGroups=_DDdmGroups_ObjectIdentity((1,3,6,1,4,1,171,14,72,2,2))
dDdmInfoGroup=ObjectGroup((1,3,6,1,4,1,171,14,72,2,2,1))
dDdmInfoGroup.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:dDdmInfoGroup.setStatus(_B)
dDdmCfgGroup=ObjectGroup((1,3,6,1,4,1,171,14,72,2,2,2))
dDdmCfgGroup.setObjects(*((_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:dDdmCfgGroup.setStatus(_B)
dDdmAlarmTrap=NotificationType((1,3,6,1,4,1,171,14,72,0,1))
dDdmAlarmTrap.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:dDdmAlarmTrap.setStatus(_B)
dDdmWarningTrap=NotificationType((1,3,6,1,4,1,171,14,72,0,2))
dDdmWarningTrap.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:dDdmWarningTrap.setStatus(_B)
dDdmNotifyGroup=NotificationGroup((1,3,6,1,4,1,171,14,72,2,2,3))
dDdmNotifyGroup.setObjects(*((_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:dDdmNotifyGroup.setStatus(_B)
dDdmCompliance=ModuleCompliance((1,3,6,1,4,1,171,14,72,2,1,1))
dDdmCompliance.setObjects(*((_A,_AB),(_A,_AC),(_A,_AD)))
if mibBuilder.loadTexts:dDdmCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'DlinkThresholdState':DlinkThresholdState,'dlinkSwDdmMIB':dlinkSwDdmMIB,'dDdmMIBNotifications':dDdmMIBNotifications,_A9:dDdmAlarmTrap,_AA:dDdmWarningTrap,'dDdmMIBObjects':dDdmMIBObjects,'dDdmCtrl':dDdmCtrl,_A4:dDdmNotifyEnable,'dDdmIfCtrl':dDdmIfCtrl,'dDdmIfCfgTable':dDdmIfCfgTable,'dDdmIfCfgEntry':dDdmIfCfgEntry,_A5:dDdmIfCfgEnabled,_A6:dDdmShutdownLevel,'dDdmThresholdMgmt':dDdmThresholdMgmt,'dDdmThresholdCfgTable':dDdmThresholdCfgTable,'dDdmThresholdCfgEntry':dDdmThresholdCfgEntry,_R:dDdmThresholdComponent,_S:dDmThresholdAbnormalLevel,_A7:dDdmThresholdCfgValue,_A8:dDdmThresholdCfgRowStatus,'dDdmInfo':dDdmInfo,'dDdmIfInfoTable':dDdmIfInfoTable,'dDdmIfInfoEntry':dDdmIfInfoEntry,_a:dDdmIfInfoCurrentTemperature,_b:dDdmIfInfoTemperatureState,_c:dDdmIfInfoHighAlarmTemperature,_d:dDdmIfInfoHighWarnTemperature,_e:dDdmIfInfoLowWarnTemperature,_f:dDdmIfInfoLowAlarmTemperature,_g:dDdmIfInfoCurrentVoltage,_h:dDdmIfInfoVoltageState,_i:dDdmIfInfoHighAlarmVoltage,_j:dDdmIfInfoHighWarnVoltage,_k:dDdmIfInfoLowWarnVoltage,_l:dDdmIfInfoLowAlarmVoltage,_m:dDdmIfInfoCurrentBiasCurrent,_n:dDdmIfInfoBiasCurrentState,_o:dDdmIfInfoHighAlarmBiasCurrent,_p:dDdmIfInfoHighWarnBiasCurrent,_q:dDdmIfInfoLowWarnBiasCurrent,_r:dDdmIfInfoLowAlarmBiasCurrent,_s:dDdmIfInfoCurrentTxPower,_t:dDdmIfInfoTxPowerState,_u:dDdmIfInfoHighAlarmTxPower,_v:dDdmIfInfoHighWarnTxPower,_w:dDdmIfInfoLowWarnTxPower,_x:dDdmIfInfoLowAlarmTxPower,_y:dDdmIfInfoCurrentRxPower,_z:dDdmIfInfoRxPowerState,_A0:dDdmIfInfoHighAlarmRxPower,_A1:dDdmIfInfoHighWarnRxPower,_A2:dDdmIfInfoLowWarnRxPower,_A3:dDdmIfInfoLowAlarmRxPower,'dDdmNotifyInfo':dDdmNotifyInfo,_L:dDdmNotifyInfoIfIndex,_M:dDdmNotifyInfoComponent,_N:dDdmNotifyInfoAbnormalLevel,_O:dDdmNotifyInfoThresholdExceedOrRecover,'dDdmMIBConformance':dDdmMIBConformance,'dDdmCompliances':dDdmCompliances,'dDdmCompliance':dDdmCompliance,'dDdmGroups':dDdmGroups,_AB:dDdmInfoGroup,_AC:dDdmCfgGroup,_AD:dDdmNotifyGroup})