_A1='ciscoEnvMonStatChangeNotifGroup'
_A0='ciscoEnvMonEnableStatChangeGroup'
_z='ciscoEnvMonMIBNotifGroup'
_y='ciscoEnvMonMIBGroupRev'
_x='ciscoEnvMonMIBGroup'
_w='ciscoEnvMonRedundantSupplyNotification'
_v='ciscoEnvMonFanNotification'
_u='ciscoEnvMonTemperatureNotification'
_t='ciscoEnvMonVoltageNotification'
_s='ciscoEnvMonSuppStatusChangeNotif'
_r='ciscoEnvMonFanStatusChangeNotif'
_q='ciscoEnvMonTempStatusChangeNotif'
_p='ciscoEnvMonVoltStatusChangeNotif'
_o='ciscoEnvMonShutdownNotification'
_n='ciscoEnvMonEnableStatChangeNotif'
_m='ciscoEnvMonEnableRedundantSupplyNotification'
_l='ciscoEnvMonEnableFanNotification'
_k='ciscoEnvMonEnableTemperatureNotification'
_j='ciscoEnvMonEnableVoltageNotification'
_i='ciscoEnvMonSupplyStatusIndex'
_h='ciscoEnvMonFanStatusIndex'
_g='ciscoEnvMonTemperatureStatusIndex'
_f='ciscoEnvMonVoltageStatusIndex'
_e='ciscoEnvMonEnableShutdownNotification'
_d='ciscoEnvMonAlarmContacts'
_c='ciscoEnvMonSupplySource'
_b='ciscoEnvMonTemperatureLastShutdown'
_a='ciscoEnvMonTemperatureThreshold'
_Z='ciscoEnvMonVoltageLastShutdown'
_Y='ciscoEnvMonVoltageThresholdHigh'
_X='ciscoEnvMonVoltageThresholdLow'
_W='ciscoEnvMonPresent'
_V='degrees Celsius'
_U='millivolts'
_T='not-accessible'
_S='ciscoEnvMonSupplyState'
_R='ciscoEnvMonSupplyStatusDescr'
_Q='ciscoEnvMonFanState'
_P='ciscoEnvMonFanStatusDescr'
_O='ciscoEnvMonTemperatureStatusValueRev1'
_N='ciscoEnvMonTemperatureState'
_M='ciscoEnvMonTemperatureStatusValue'
_L='ciscoEnvMonTemperatureStatusDescr'
_K='ciscoEnvMonVoltageState'
_J='ciscoEnvMonVoltageStatusValue'
_I='ciscoEnvMonVoltageStatusDescr'
_H='DisplayString'
_G='read-write'
_F='TruthValue'
_E='Integer32'
_D='deprecated'
_C='read-only'
_B='current'
_A='CISCO-ENVMON-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention',_F)
ciscoEnvMonMIB=ModuleIdentity((1,3,6,1,4,1,9,9,13))
if mibBuilder.loadTexts:ciscoEnvMonMIB.setRevisions(('2018-03-21 00:00','2003-12-01 00:00','2003-11-25 00:00','2002-10-15 00:00','2002-07-17 00:00','2002-02-04 00:00','2001-08-30 00:00','2001-08-16 00:00','2001-05-07 00:00','2000-01-31 00:00','1998-10-22 00:00','1998-08-05 00:00','1996-11-12 00:00','1995-08-15 00:00','1995-03-13 00:00'))
class CiscoEnvMonState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('normal',1),('warning',2),('critical',3),('shutdown',4),('notPresent',5),('notFunctioning',6)))
class CiscoSignedGauge(TextualConvention,Integer32):status=_B
_CiscoEnvMonObjects_ObjectIdentity=ObjectIdentity
ciscoEnvMonObjects=_CiscoEnvMonObjects_ObjectIdentity((1,3,6,1,4,1,9,9,13,1))
class _CiscoEnvMonPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('oldAgs',1),('ags',2),('c7000',3),('ci',4),('cAccessMon',6),('cat6000',7),('ubr7200',8),('cat4000',9),('c10000',10),('osr7600',11),('c7600',12),('c37xx',13),('other',14),('c7301',15),('c7304',16)))
_CiscoEnvMonPresent_Type.__name__=_E
_CiscoEnvMonPresent_Object=MibScalar
ciscoEnvMonPresent=_CiscoEnvMonPresent_Object((1,3,6,1,4,1,9,9,13,1,1),_CiscoEnvMonPresent_Type())
ciscoEnvMonPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoEnvMonPresent.setStatus(_B)
_CiscoEnvMonVoltageStatusTable_Object=MibTable
ciscoEnvMonVoltageStatusTable=_CiscoEnvMonVoltageStatusTable_Object((1,3,6,1,4,1,9,9,13,1,2))
if mibBuilder.loadTexts:ciscoEnvMonVoltageStatusTable.setStatus(_B)
_CiscoEnvMonVoltageStatusEntry_Object=MibTableRow
ciscoEnvMonVoltageStatusEntry=_CiscoEnvMonVoltageStatusEntry_Object((1,3,6,1,4,1,9,9,13,1,2,1))
ciscoEnvMonVoltageStatusEntry.setIndexNames((0,_A,_f))
if mibBuilder.loadTexts:ciscoEnvMonVoltageStatusEntry.setStatus(_B)
class _CiscoEnvMonVoltageStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CiscoEnvMonVoltageStatusIndex_Type.__name__=_E
_CiscoEnvMonVoltageStatusIndex_Object=MibTableColumn
ciscoEnvMonVoltageStatusIndex=_CiscoEnvMonVoltageStatusIndex_Object((1,3,6,1,4,1,9,9,13,1,2,1,1),_CiscoEnvMonVoltageStatusIndex_Type())
ciscoEnvMonVoltageStatusIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:ciscoEnvMonVoltageStatusIndex.setStatus(_B)
class _CiscoEnvMonVoltageStatusDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CiscoEnvMonVoltageStatusDescr_Type.__name__=_H
_CiscoEnvMonVoltageStatusDescr_Object=MibTableColumn
ciscoEnvMonVoltageStatusDescr=_CiscoEnvMonVoltageStatusDescr_Object((1,3,6,1,4,1,9,9,13,1,2,1,2),_CiscoEnvMonVoltageStatusDescr_Type())
ciscoEnvMonVoltageStatusDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoEnvMonVoltageStatusDescr.setStatus(_B)
_CiscoEnvMonVoltageStatusValue_Type=CiscoSignedGauge
_CiscoEnvMonVoltageStatusValue_Object=MibTableColumn
ciscoEnvMonVoltageStatusValue=_CiscoEnvMonVoltageStatusValue_Object((1,3,6,1,4,1,9,9,13,1,2,1,3),_CiscoEnvMonVoltageStatusValue_Type())
ciscoEnvMonVoltageStatusValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoEnvMonVoltageStatusValue.setStatus(_B)
if mibBuilder.loadTexts:ciscoEnvMonVoltageStatusValue.setUnits(_U)
_CiscoEnvMonVoltageThresholdLow_Type=Integer32
_CiscoEnvMonVoltageThresholdLow_Object=MibTableColumn
ciscoEnvMonVoltageThresholdLow=_CiscoEnvMonVoltageThresholdLow_Object((1,3,6,1,4,1,9,9,13,1,2,1,4),_CiscoEnvMonVoltageThresholdLow_Type())
ciscoEnvMonVoltageThresholdLow.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoEnvMonVoltageThresholdLow.setStatus(_B)
if mibBuilder.loadTexts:ciscoEnvMonVoltageThresholdLow.setUnits(_U)
_CiscoEnvMonVoltageThresholdHigh_Type=Integer32
_CiscoEnvMonVoltageThresholdHigh_Object=MibTableColumn
ciscoEnvMonVoltageThresholdHigh=_CiscoEnvMonVoltageThresholdHigh_Object((1,3,6,1,4,1,9,9,13,1,2,1,5),_CiscoEnvMonVoltageThresholdHigh_Type())
ciscoEnvMonVoltageThresholdHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoEnvMonVoltageThresholdHigh.setStatus(_B)
if mibBuilder.loadTexts:ciscoEnvMonVoltageThresholdHigh.setUnits(_U)
_CiscoEnvMonVoltageLastShutdown_Type=Integer32
_CiscoEnvMonVoltageLastShutdown_Object=MibTableColumn
ciscoEnvMonVoltageLastShutdown=_CiscoEnvMonVoltageLastShutdown_Object((1,3,6,1,4,1,9,9,13,1,2,1,6),_CiscoEnvMonVoltageLastShutdown_Type())
ciscoEnvMonVoltageLastShutdown.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoEnvMonVoltageLastShutdown.setStatus(_B)
if mibBuilder.loadTexts:ciscoEnvMonVoltageLastShutdown.setUnits(_U)
_CiscoEnvMonVoltageState_Type=CiscoEnvMonState
_CiscoEnvMonVoltageState_Object=MibTableColumn
ciscoEnvMonVoltageState=_CiscoEnvMonVoltageState_Object((1,3,6,1,4,1,9,9,13,1,2,1,7),_CiscoEnvMonVoltageState_Type())
ciscoEnvMonVoltageState.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoEnvMonVoltageState.setStatus(_B)
_CiscoEnvMonTemperatureStatusTable_Object=MibTable
ciscoEnvMonTemperatureStatusTable=_CiscoEnvMonTemperatureStatusTable_Object((1,3,6,1,4,1,9,9,13,1,3))
if mibBuilder.loadTexts:ciscoEnvMonTemperatureStatusTable.setStatus(_B)
_CiscoEnvMonTemperatureStatusEntry_Object=MibTableRow
ciscoEnvMonTemperatureStatusEntry=_CiscoEnvMonTemperatureStatusEntry_Object((1,3,6,1,4,1,9,9,13,1,3,1))
ciscoEnvMonTemperatureStatusEntry.setIndexNames((0,_A,_g))
if mibBuilder.loadTexts:ciscoEnvMonTemperatureStatusEntry.setStatus(_B)
class _CiscoEnvMonTemperatureStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CiscoEnvMonTemperatureStatusIndex_Type.__name__=_E
_CiscoEnvMonTemperatureStatusIndex_Object=MibTableColumn
ciscoEnvMonTemperatureStatusIndex=_CiscoEnvMonTemperatureStatusIndex_Object((1,3,6,1,4,1,9,9,13,1,3,1,1),_CiscoEnvMonTemperatureStatusIndex_Type())
ciscoEnvMonTemperatureStatusIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:ciscoEnvMonTemperatureStatusIndex.setStatus(_B)
class _CiscoEnvMonTemperatureStatusDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CiscoEnvMonTemperatureStatusDescr_Type.__name__=_H
_CiscoEnvMonTemperatureStatusDescr_Object=MibTableColumn
ciscoEnvMonTemperatureStatusDescr=_CiscoEnvMonTemperatureStatusDescr_Object((1,3,6,1,4,1,9,9,13,1,3,1,2),_CiscoEnvMonTemperatureStatusDescr_Type())
ciscoEnvMonTemperatureStatusDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoEnvMonTemperatureStatusDescr.setStatus(_B)
_CiscoEnvMonTemperatureStatusValue_Type=Gauge32
_CiscoEnvMonTemperatureStatusValue_Object=MibTableColumn
ciscoEnvMonTemperatureStatusValue=_CiscoEnvMonTemperatureStatusValue_Object((1,3,6,1,4,1,9,9,13,1,3,1,3),_CiscoEnvMonTemperatureStatusValue_Type())
ciscoEnvMonTemperatureStatusValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoEnvMonTemperatureStatusValue.setStatus(_D)
if mibBuilder.loadTexts:ciscoEnvMonTemperatureStatusValue.setUnits(_V)
_CiscoEnvMonTemperatureThreshold_Type=Integer32
_CiscoEnvMonTemperatureThreshold_Object=MibTableColumn
ciscoEnvMonTemperatureThreshold=_CiscoEnvMonTemperatureThreshold_Object((1,3,6,1,4,1,9,9,13,1,3,1,4),_CiscoEnvMonTemperatureThreshold_Type())
ciscoEnvMonTemperatureThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoEnvMonTemperatureThreshold.setStatus(_B)
if mibBuilder.loadTexts:ciscoEnvMonTemperatureThreshold.setUnits(_V)
_CiscoEnvMonTemperatureLastShutdown_Type=Integer32
_CiscoEnvMonTemperatureLastShutdown_Object=MibTableColumn
ciscoEnvMonTemperatureLastShutdown=_CiscoEnvMonTemperatureLastShutdown_Object((1,3,6,1,4,1,9,9,13,1,3,1,5),_CiscoEnvMonTemperatureLastShutdown_Type())
ciscoEnvMonTemperatureLastShutdown.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoEnvMonTemperatureLastShutdown.setStatus(_B)
if mibBuilder.loadTexts:ciscoEnvMonTemperatureLastShutdown.setUnits(_V)
_CiscoEnvMonTemperatureState_Type=CiscoEnvMonState
_CiscoEnvMonTemperatureState_Object=MibTableColumn
ciscoEnvMonTemperatureState=_CiscoEnvMonTemperatureState_Object((1,3,6,1,4,1,9,9,13,1,3,1,6),_CiscoEnvMonTemperatureState_Type())
ciscoEnvMonTemperatureState.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoEnvMonTemperatureState.setStatus(_B)
_CiscoEnvMonTemperatureStatusValueRev1_Type=Integer32
_CiscoEnvMonTemperatureStatusValueRev1_Object=MibTableColumn
ciscoEnvMonTemperatureStatusValueRev1=_CiscoEnvMonTemperatureStatusValueRev1_Object((1,3,6,1,4,1,9,9,13,1,3,1,7),_CiscoEnvMonTemperatureStatusValueRev1_Type())
ciscoEnvMonTemperatureStatusValueRev1.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoEnvMonTemperatureStatusValueRev1.setStatus(_B)
if mibBuilder.loadTexts:ciscoEnvMonTemperatureStatusValueRev1.setUnits(_V)
_CiscoEnvMonFanStatusTable_Object=MibTable
ciscoEnvMonFanStatusTable=_CiscoEnvMonFanStatusTable_Object((1,3,6,1,4,1,9,9,13,1,4))
if mibBuilder.loadTexts:ciscoEnvMonFanStatusTable.setStatus(_B)
_CiscoEnvMonFanStatusEntry_Object=MibTableRow
ciscoEnvMonFanStatusEntry=_CiscoEnvMonFanStatusEntry_Object((1,3,6,1,4,1,9,9,13,1,4,1))
ciscoEnvMonFanStatusEntry.setIndexNames((0,_A,_h))
if mibBuilder.loadTexts:ciscoEnvMonFanStatusEntry.setStatus(_B)
class _CiscoEnvMonFanStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CiscoEnvMonFanStatusIndex_Type.__name__=_E
_CiscoEnvMonFanStatusIndex_Object=MibTableColumn
ciscoEnvMonFanStatusIndex=_CiscoEnvMonFanStatusIndex_Object((1,3,6,1,4,1,9,9,13,1,4,1,1),_CiscoEnvMonFanStatusIndex_Type())
ciscoEnvMonFanStatusIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:ciscoEnvMonFanStatusIndex.setStatus(_B)
class _CiscoEnvMonFanStatusDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CiscoEnvMonFanStatusDescr_Type.__name__=_H
_CiscoEnvMonFanStatusDescr_Object=MibTableColumn
ciscoEnvMonFanStatusDescr=_CiscoEnvMonFanStatusDescr_Object((1,3,6,1,4,1,9,9,13,1,4,1,2),_CiscoEnvMonFanStatusDescr_Type())
ciscoEnvMonFanStatusDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoEnvMonFanStatusDescr.setStatus(_B)
_CiscoEnvMonFanState_Type=CiscoEnvMonState
_CiscoEnvMonFanState_Object=MibTableColumn
ciscoEnvMonFanState=_CiscoEnvMonFanState_Object((1,3,6,1,4,1,9,9,13,1,4,1,3),_CiscoEnvMonFanState_Type())
ciscoEnvMonFanState.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoEnvMonFanState.setStatus(_B)
_CiscoEnvMonSupplyStatusTable_Object=MibTable
ciscoEnvMonSupplyStatusTable=_CiscoEnvMonSupplyStatusTable_Object((1,3,6,1,4,1,9,9,13,1,5))
if mibBuilder.loadTexts:ciscoEnvMonSupplyStatusTable.setStatus(_B)
_CiscoEnvMonSupplyStatusEntry_Object=MibTableRow
ciscoEnvMonSupplyStatusEntry=_CiscoEnvMonSupplyStatusEntry_Object((1,3,6,1,4,1,9,9,13,1,5,1))
ciscoEnvMonSupplyStatusEntry.setIndexNames((0,_A,_i))
if mibBuilder.loadTexts:ciscoEnvMonSupplyStatusEntry.setStatus(_B)
class _CiscoEnvMonSupplyStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CiscoEnvMonSupplyStatusIndex_Type.__name__=_E
_CiscoEnvMonSupplyStatusIndex_Object=MibTableColumn
ciscoEnvMonSupplyStatusIndex=_CiscoEnvMonSupplyStatusIndex_Object((1,3,6,1,4,1,9,9,13,1,5,1,1),_CiscoEnvMonSupplyStatusIndex_Type())
ciscoEnvMonSupplyStatusIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:ciscoEnvMonSupplyStatusIndex.setStatus(_B)
class _CiscoEnvMonSupplyStatusDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CiscoEnvMonSupplyStatusDescr_Type.__name__=_H
_CiscoEnvMonSupplyStatusDescr_Object=MibTableColumn
ciscoEnvMonSupplyStatusDescr=_CiscoEnvMonSupplyStatusDescr_Object((1,3,6,1,4,1,9,9,13,1,5,1,2),_CiscoEnvMonSupplyStatusDescr_Type())
ciscoEnvMonSupplyStatusDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoEnvMonSupplyStatusDescr.setStatus(_B)
_CiscoEnvMonSupplyState_Type=CiscoEnvMonState
_CiscoEnvMonSupplyState_Object=MibTableColumn
ciscoEnvMonSupplyState=_CiscoEnvMonSupplyState_Object((1,3,6,1,4,1,9,9,13,1,5,1,3),_CiscoEnvMonSupplyState_Type())
ciscoEnvMonSupplyState.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoEnvMonSupplyState.setStatus(_B)
class _CiscoEnvMonSupplySource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unknown',1),('ac',2),('dc',3),('externalPowerSupply',4),('internalRedundant',5)))
_CiscoEnvMonSupplySource_Type.__name__=_E
_CiscoEnvMonSupplySource_Object=MibTableColumn
ciscoEnvMonSupplySource=_CiscoEnvMonSupplySource_Object((1,3,6,1,4,1,9,9,13,1,5,1,4),_CiscoEnvMonSupplySource_Type())
ciscoEnvMonSupplySource.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoEnvMonSupplySource.setStatus(_B)
class _CiscoEnvMonAlarmContacts_Type(Bits):namedValues=NamedValues(*(('minorVisual',0),('majorVisual',1),('criticalVisual',2),('minorAudible',3),('majorAudible',4),('criticalAudible',5),('input',6)))
_CiscoEnvMonAlarmContacts_Type.__name__='Bits'
_CiscoEnvMonAlarmContacts_Object=MibScalar
ciscoEnvMonAlarmContacts=_CiscoEnvMonAlarmContacts_Object((1,3,6,1,4,1,9,9,13,1,6),_CiscoEnvMonAlarmContacts_Type())
ciscoEnvMonAlarmContacts.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoEnvMonAlarmContacts.setStatus(_B)
_CiscoEnvMonMIBNotificationEnables_ObjectIdentity=ObjectIdentity
ciscoEnvMonMIBNotificationEnables=_CiscoEnvMonMIBNotificationEnables_ObjectIdentity((1,3,6,1,4,1,9,9,13,2))
class _CiscoEnvMonEnableShutdownNotification_Type(TruthValue):defaultValue=2
_CiscoEnvMonEnableShutdownNotification_Type.__name__=_F
_CiscoEnvMonEnableShutdownNotification_Object=MibScalar
ciscoEnvMonEnableShutdownNotification=_CiscoEnvMonEnableShutdownNotification_Object((1,3,6,1,4,1,9,9,13,2,1),_CiscoEnvMonEnableShutdownNotification_Type())
ciscoEnvMonEnableShutdownNotification.setMaxAccess(_G)
if mibBuilder.loadTexts:ciscoEnvMonEnableShutdownNotification.setStatus(_B)
class _CiscoEnvMonEnableVoltageNotification_Type(TruthValue):defaultValue=2
_CiscoEnvMonEnableVoltageNotification_Type.__name__=_F
_CiscoEnvMonEnableVoltageNotification_Object=MibScalar
ciscoEnvMonEnableVoltageNotification=_CiscoEnvMonEnableVoltageNotification_Object((1,3,6,1,4,1,9,9,13,2,2),_CiscoEnvMonEnableVoltageNotification_Type())
ciscoEnvMonEnableVoltageNotification.setMaxAccess(_G)
if mibBuilder.loadTexts:ciscoEnvMonEnableVoltageNotification.setStatus(_D)
class _CiscoEnvMonEnableTemperatureNotification_Type(TruthValue):defaultValue=2
_CiscoEnvMonEnableTemperatureNotification_Type.__name__=_F
_CiscoEnvMonEnableTemperatureNotification_Object=MibScalar
ciscoEnvMonEnableTemperatureNotification=_CiscoEnvMonEnableTemperatureNotification_Object((1,3,6,1,4,1,9,9,13,2,3),_CiscoEnvMonEnableTemperatureNotification_Type())
ciscoEnvMonEnableTemperatureNotification.setMaxAccess(_G)
if mibBuilder.loadTexts:ciscoEnvMonEnableTemperatureNotification.setStatus(_D)
class _CiscoEnvMonEnableFanNotification_Type(TruthValue):defaultValue=2
_CiscoEnvMonEnableFanNotification_Type.__name__=_F
_CiscoEnvMonEnableFanNotification_Object=MibScalar
ciscoEnvMonEnableFanNotification=_CiscoEnvMonEnableFanNotification_Object((1,3,6,1,4,1,9,9,13,2,4),_CiscoEnvMonEnableFanNotification_Type())
ciscoEnvMonEnableFanNotification.setMaxAccess(_G)
if mibBuilder.loadTexts:ciscoEnvMonEnableFanNotification.setStatus(_D)
class _CiscoEnvMonEnableRedundantSupplyNotification_Type(TruthValue):defaultValue=2
_CiscoEnvMonEnableRedundantSupplyNotification_Type.__name__=_F
_CiscoEnvMonEnableRedundantSupplyNotification_Object=MibScalar
ciscoEnvMonEnableRedundantSupplyNotification=_CiscoEnvMonEnableRedundantSupplyNotification_Object((1,3,6,1,4,1,9,9,13,2,5),_CiscoEnvMonEnableRedundantSupplyNotification_Type())
ciscoEnvMonEnableRedundantSupplyNotification.setMaxAccess(_G)
if mibBuilder.loadTexts:ciscoEnvMonEnableRedundantSupplyNotification.setStatus(_D)
class _CiscoEnvMonEnableStatChangeNotif_Type(TruthValue):defaultValue=2
_CiscoEnvMonEnableStatChangeNotif_Type.__name__=_F
_CiscoEnvMonEnableStatChangeNotif_Object=MibScalar
ciscoEnvMonEnableStatChangeNotif=_CiscoEnvMonEnableStatChangeNotif_Object((1,3,6,1,4,1,9,9,13,2,6),_CiscoEnvMonEnableStatChangeNotif_Type())
ciscoEnvMonEnableStatChangeNotif.setMaxAccess(_G)
if mibBuilder.loadTexts:ciscoEnvMonEnableStatChangeNotif.setStatus(_B)
_CiscoEnvMonMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoEnvMonMIBNotificationPrefix=_CiscoEnvMonMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,13,3))
_CiscoEnvMonMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoEnvMonMIBNotifications=_CiscoEnvMonMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,13,3,0))
_CiscoEnvMonMIBConformance_ObjectIdentity=ObjectIdentity
ciscoEnvMonMIBConformance=_CiscoEnvMonMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,13,4))
_CiscoEnvMonMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoEnvMonMIBCompliances=_CiscoEnvMonMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,13,4,1))
_CiscoEnvMonMIBGroups_ObjectIdentity=ObjectIdentity
ciscoEnvMonMIBGroups=_CiscoEnvMonMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,13,4,2))
ciscoEnvMonMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,13,4,2,1))
ciscoEnvMonMIBGroup.setObjects(*((_A,_W),(_A,_I),(_A,_J),(_A,_X),(_A,_Y),(_A,_Z),(_A,_K),(_A,_L),(_A,_M),(_A,_a),(_A,_b),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_c),(_A,_d),(_A,_e),(_A,_j),(_A,_k),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:ciscoEnvMonMIBGroup.setStatus(_D)
ciscoEnvMonMIBGroupRev=ObjectGroup((1,3,6,1,4,1,9,9,13,4,2,2))
ciscoEnvMonMIBGroupRev.setObjects(*((_A,_W),(_A,_I),(_A,_J),(_A,_X),(_A,_Y),(_A,_Z),(_A,_K),(_A,_L),(_A,_M),(_A,_a),(_A,_b),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:ciscoEnvMonMIBGroupRev.setStatus(_B)
ciscoEnvMonEnableStatChangeGroup=ObjectGroup((1,3,6,1,4,1,9,9,13,4,2,3))
ciscoEnvMonEnableStatChangeGroup.setObjects((_A,_n))
if mibBuilder.loadTexts:ciscoEnvMonEnableStatChangeGroup.setStatus(_B)
ciscoEnvMonShutdownNotification=NotificationType((1,3,6,1,4,1,9,9,13,3,0,1))
if mibBuilder.loadTexts:ciscoEnvMonShutdownNotification.setStatus(_B)
ciscoEnvMonVoltageNotification=NotificationType((1,3,6,1,4,1,9,9,13,3,0,2))
ciscoEnvMonVoltageNotification.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ciscoEnvMonVoltageNotification.setStatus(_D)
ciscoEnvMonTemperatureNotification=NotificationType((1,3,6,1,4,1,9,9,13,3,0,3))
ciscoEnvMonTemperatureNotification.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ciscoEnvMonTemperatureNotification.setStatus(_D)
ciscoEnvMonFanNotification=NotificationType((1,3,6,1,4,1,9,9,13,3,0,4))
ciscoEnvMonFanNotification.setObjects(*((_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:ciscoEnvMonFanNotification.setStatus(_D)
ciscoEnvMonRedundantSupplyNotification=NotificationType((1,3,6,1,4,1,9,9,13,3,0,5))
ciscoEnvMonRedundantSupplyNotification.setObjects(*((_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ciscoEnvMonRedundantSupplyNotification.setStatus(_D)
ciscoEnvMonVoltStatusChangeNotif=NotificationType((1,3,6,1,4,1,9,9,13,3,0,6))
ciscoEnvMonVoltStatusChangeNotif.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ciscoEnvMonVoltStatusChangeNotif.setStatus(_B)
ciscoEnvMonTempStatusChangeNotif=NotificationType((1,3,6,1,4,1,9,9,13,3,0,7))
ciscoEnvMonTempStatusChangeNotif.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ciscoEnvMonTempStatusChangeNotif.setStatus(_B)
ciscoEnvMonFanStatusChangeNotif=NotificationType((1,3,6,1,4,1,9,9,13,3,0,8))
ciscoEnvMonFanStatusChangeNotif.setObjects(*((_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:ciscoEnvMonFanStatusChangeNotif.setStatus(_B)
ciscoEnvMonSuppStatusChangeNotif=NotificationType((1,3,6,1,4,1,9,9,13,3,0,9))
ciscoEnvMonSuppStatusChangeNotif.setObjects(*((_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ciscoEnvMonSuppStatusChangeNotif.setStatus(_B)
ciscoEnvMonMIBNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,13,4,2,4))
ciscoEnvMonMIBNotifGroup.setObjects((_A,_o))
if mibBuilder.loadTexts:ciscoEnvMonMIBNotifGroup.setStatus(_B)
ciscoEnvMonStatChangeNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,13,4,2,5))
ciscoEnvMonStatChangeNotifGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:ciscoEnvMonStatChangeNotifGroup.setStatus(_B)
ciscoEnvMonMIBMiscNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,13,4,2,6))
ciscoEnvMonMIBMiscNotifGroup.setObjects(*((_A,_t),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:ciscoEnvMonMIBMiscNotifGroup.setStatus(_D)
ciscoEnvMonMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,13,4,1,1))
ciscoEnvMonMIBCompliance.setObjects((_A,_x))
if mibBuilder.loadTexts:ciscoEnvMonMIBCompliance.setStatus(_D)
ciscoEnvMonMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,13,4,1,2))
ciscoEnvMonMIBComplianceRev1.setObjects(*((_A,_y),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:ciscoEnvMonMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CiscoEnvMonState':CiscoEnvMonState,'CiscoSignedGauge':CiscoSignedGauge,'ciscoEnvMonMIB':ciscoEnvMonMIB,'ciscoEnvMonObjects':ciscoEnvMonObjects,_W:ciscoEnvMonPresent,'ciscoEnvMonVoltageStatusTable':ciscoEnvMonVoltageStatusTable,'ciscoEnvMonVoltageStatusEntry':ciscoEnvMonVoltageStatusEntry,_f:ciscoEnvMonVoltageStatusIndex,_I:ciscoEnvMonVoltageStatusDescr,_J:ciscoEnvMonVoltageStatusValue,_X:ciscoEnvMonVoltageThresholdLow,_Y:ciscoEnvMonVoltageThresholdHigh,_Z:ciscoEnvMonVoltageLastShutdown,_K:ciscoEnvMonVoltageState,'ciscoEnvMonTemperatureStatusTable':ciscoEnvMonTemperatureStatusTable,'ciscoEnvMonTemperatureStatusEntry':ciscoEnvMonTemperatureStatusEntry,_g:ciscoEnvMonTemperatureStatusIndex,_L:ciscoEnvMonTemperatureStatusDescr,_M:ciscoEnvMonTemperatureStatusValue,_a:ciscoEnvMonTemperatureThreshold,_b:ciscoEnvMonTemperatureLastShutdown,_N:ciscoEnvMonTemperatureState,_O:ciscoEnvMonTemperatureStatusValueRev1,'ciscoEnvMonFanStatusTable':ciscoEnvMonFanStatusTable,'ciscoEnvMonFanStatusEntry':ciscoEnvMonFanStatusEntry,_h:ciscoEnvMonFanStatusIndex,_P:ciscoEnvMonFanStatusDescr,_Q:ciscoEnvMonFanState,'ciscoEnvMonSupplyStatusTable':ciscoEnvMonSupplyStatusTable,'ciscoEnvMonSupplyStatusEntry':ciscoEnvMonSupplyStatusEntry,_i:ciscoEnvMonSupplyStatusIndex,_R:ciscoEnvMonSupplyStatusDescr,_S:ciscoEnvMonSupplyState,_c:ciscoEnvMonSupplySource,_d:ciscoEnvMonAlarmContacts,'ciscoEnvMonMIBNotificationEnables':ciscoEnvMonMIBNotificationEnables,_e:ciscoEnvMonEnableShutdownNotification,_j:ciscoEnvMonEnableVoltageNotification,_k:ciscoEnvMonEnableTemperatureNotification,_l:ciscoEnvMonEnableFanNotification,_m:ciscoEnvMonEnableRedundantSupplyNotification,_n:ciscoEnvMonEnableStatChangeNotif,'ciscoEnvMonMIBNotificationPrefix':ciscoEnvMonMIBNotificationPrefix,'ciscoEnvMonMIBNotifications':ciscoEnvMonMIBNotifications,_o:ciscoEnvMonShutdownNotification,_t:ciscoEnvMonVoltageNotification,_u:ciscoEnvMonTemperatureNotification,_v:ciscoEnvMonFanNotification,_w:ciscoEnvMonRedundantSupplyNotification,_p:ciscoEnvMonVoltStatusChangeNotif,_q:ciscoEnvMonTempStatusChangeNotif,_r:ciscoEnvMonFanStatusChangeNotif,_s:ciscoEnvMonSuppStatusChangeNotif,'ciscoEnvMonMIBConformance':ciscoEnvMonMIBConformance,'ciscoEnvMonMIBCompliances':ciscoEnvMonMIBCompliances,'ciscoEnvMonMIBCompliance':ciscoEnvMonMIBCompliance,'ciscoEnvMonMIBComplianceRev1':ciscoEnvMonMIBComplianceRev1,'ciscoEnvMonMIBGroups':ciscoEnvMonMIBGroups,_x:ciscoEnvMonMIBGroup,_y:ciscoEnvMonMIBGroupRev,_A0:ciscoEnvMonEnableStatChangeGroup,_z:ciscoEnvMonMIBNotifGroup,_A1:ciscoEnvMonStatChangeNotifGroup,'ciscoEnvMonMIBMiscNotifGroup':ciscoEnvMonMIBMiscNotifGroup})