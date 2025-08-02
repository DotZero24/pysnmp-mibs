_Y='nnenvPowerSupply2UpNotification'
_X='nnenvPowerSupply2DownNotification'
_W='nnenvPowerSupply1UpNotification'
_V='nnenvPowerSupply1DownNotification'
_U='nnenvFanNotification'
_T='nnenvTemperatureNotification'
_S='nnenvFanState'
_R='nnenvTempSensorState'
_Q='nnenvTempSensorValue'
_P='accessible-for-notify'
_O='normal'
_N='read-write'
_M='nnenvFanUnitIndex'
_L='Integer32'
_K='TruthValue'
_J='nnenvPwrsupDowntime'
_I='nnenvPwrsupUptime'
_H='nnenvPwrsupType'
_G='nnenvPwrsupStatus'
_F='nnenvPwrsupInstalled'
_E='nnenvPwrsupPowerFailCount'
_D='nnenvPwrsupIndex'
_C='read-only'
_B='current'
_A='ENVIRONMENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntEnterpriseDataTasmanMgmt,=mibBuilder.importSymbols('NT-ENTERPRISE-DATA-MIB','ntEnterpriseDataTasmanMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_K)
nnenvironmentMib=ModuleIdentity((1,3,6,1,4,1,562,73,1,1,1,3))
if mibBuilder.loadTexts:nnenvironmentMib.setRevisions(('1900-08-18 00:00',))
class EnvState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_O,1),('warning',2),('critical',3),('fail',4),('turned-off',5)))
class EnvInstalled(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('not-installed',1),('installed',2)))
class EnvStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('absent',1),('failed',2),(_O,3)))
class EnvType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('supply-AC-ONLY',1),('supply-AC-PoE',2),('supply-DC',3),('unknown',4)))
_NnenvObjects_ObjectIdentity=ObjectIdentity
nnenvObjects=_NnenvObjects_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,3,1))
_NnenvTempSensorGroup_ObjectIdentity=ObjectIdentity
nnenvTempSensorGroup=_NnenvTempSensorGroup_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,3,1,1))
_NnenvTempSensorValue_Type=Gauge32
_NnenvTempSensorValue_Object=MibScalar
nnenvTempSensorValue=_NnenvTempSensorValue_Object((1,3,6,1,4,1,562,73,1,1,1,3,1,1,1),_NnenvTempSensorValue_Type())
nnenvTempSensorValue.setMaxAccess(_C)
if mibBuilder.loadTexts:nnenvTempSensorValue.setStatus(_B)
_NnenvTempSensorState_Type=EnvState
_NnenvTempSensorState_Object=MibScalar
nnenvTempSensorState=_NnenvTempSensorState_Object((1,3,6,1,4,1,562,73,1,1,1,3,1,1,2),_NnenvTempSensorState_Type())
nnenvTempSensorState.setMaxAccess(_C)
if mibBuilder.loadTexts:nnenvTempSensorState.setStatus(_B)
_NnenvFanTable_Object=MibTable
nnenvFanTable=_NnenvFanTable_Object((1,3,6,1,4,1,562,73,1,1,1,3,1,2))
if mibBuilder.loadTexts:nnenvFanTable.setStatus(_B)
_NnenvFanEntry_Object=MibTableRow
nnenvFanEntry=_NnenvFanEntry_Object((1,3,6,1,4,1,562,73,1,1,1,3,1,2,1))
nnenvFanEntry.setIndexNames((0,_A,_M))
if mibBuilder.loadTexts:nnenvFanEntry.setStatus(_B)
class _NnenvFanUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_NnenvFanUnitIndex_Type.__name__=_L
_NnenvFanUnitIndex_Object=MibTableColumn
nnenvFanUnitIndex=_NnenvFanUnitIndex_Object((1,3,6,1,4,1,562,73,1,1,1,3,1,2,1,1),_NnenvFanUnitIndex_Type())
nnenvFanUnitIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:nnenvFanUnitIndex.setStatus(_B)
_NnenvFanState_Type=EnvState
_NnenvFanState_Object=MibTableColumn
nnenvFanState=_NnenvFanState_Object((1,3,6,1,4,1,562,73,1,1,1,3,1,2,1,2),_NnenvFanState_Type())
nnenvFanState.setMaxAccess(_C)
if mibBuilder.loadTexts:nnenvFanState.setStatus(_B)
_NnenvPwrsupPowerFailCount_Type=Integer32
_NnenvPwrsupPowerFailCount_Object=MibScalar
nnenvPwrsupPowerFailCount=_NnenvPwrsupPowerFailCount_Object((1,3,6,1,4,1,562,73,1,1,1,3,1,3),_NnenvPwrsupPowerFailCount_Type())
nnenvPwrsupPowerFailCount.setMaxAccess(_C)
if mibBuilder.loadTexts:nnenvPwrsupPowerFailCount.setStatus(_B)
_NnenvPwrsupTable_Object=MibTable
nnenvPwrsupTable=_NnenvPwrsupTable_Object((1,3,6,1,4,1,562,73,1,1,1,3,1,4))
if mibBuilder.loadTexts:nnenvPwrsupTable.setStatus(_B)
_NnenvPwrsupEntry_Object=MibTableRow
nnenvPwrsupEntry=_NnenvPwrsupEntry_Object((1,3,6,1,4,1,562,73,1,1,1,3,1,4,1))
nnenvPwrsupEntry.setIndexNames((0,_A,_D))
if mibBuilder.loadTexts:nnenvPwrsupEntry.setStatus(_B)
class _NnenvPwrsupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_NnenvPwrsupIndex_Type.__name__=_L
_NnenvPwrsupIndex_Object=MibTableColumn
nnenvPwrsupIndex=_NnenvPwrsupIndex_Object((1,3,6,1,4,1,562,73,1,1,1,3,1,4,1,1),_NnenvPwrsupIndex_Type())
nnenvPwrsupIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:nnenvPwrsupIndex.setStatus(_B)
_NnenvPwrsupInstalled_Type=EnvInstalled
_NnenvPwrsupInstalled_Object=MibTableColumn
nnenvPwrsupInstalled=_NnenvPwrsupInstalled_Object((1,3,6,1,4,1,562,73,1,1,1,3,1,4,1,2),_NnenvPwrsupInstalled_Type())
nnenvPwrsupInstalled.setMaxAccess(_C)
if mibBuilder.loadTexts:nnenvPwrsupInstalled.setStatus(_B)
_NnenvPwrsupStatus_Type=EnvStatus
_NnenvPwrsupStatus_Object=MibTableColumn
nnenvPwrsupStatus=_NnenvPwrsupStatus_Object((1,3,6,1,4,1,562,73,1,1,1,3,1,4,1,3),_NnenvPwrsupStatus_Type())
nnenvPwrsupStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nnenvPwrsupStatus.setStatus(_B)
_NnenvPwrsupType_Type=EnvType
_NnenvPwrsupType_Object=MibTableColumn
nnenvPwrsupType=_NnenvPwrsupType_Object((1,3,6,1,4,1,562,73,1,1,1,3,1,4,1,4),_NnenvPwrsupType_Type())
nnenvPwrsupType.setMaxAccess(_C)
if mibBuilder.loadTexts:nnenvPwrsupType.setStatus(_B)
_NnenvPwrsupUptime_Type=Integer32
_NnenvPwrsupUptime_Object=MibTableColumn
nnenvPwrsupUptime=_NnenvPwrsupUptime_Object((1,3,6,1,4,1,562,73,1,1,1,3,1,4,1,5),_NnenvPwrsupUptime_Type())
nnenvPwrsupUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:nnenvPwrsupUptime.setStatus(_B)
_NnenvPwrsupDowntime_Type=Integer32
_NnenvPwrsupDowntime_Object=MibTableColumn
nnenvPwrsupDowntime=_NnenvPwrsupDowntime_Object((1,3,6,1,4,1,562,73,1,1,1,3,1,4,1,6),_NnenvPwrsupDowntime_Type())
nnenvPwrsupDowntime.setMaxAccess(_C)
if mibBuilder.loadTexts:nnenvPwrsupDowntime.setStatus(_B)
_NnenvNotificationEnables_ObjectIdentity=ObjectIdentity
nnenvNotificationEnables=_NnenvNotificationEnables_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,3,2))
class _NnenvEnableTemperatureNotification_Type(TruthValue):defaultValue=1
_NnenvEnableTemperatureNotification_Type.__name__=_K
_NnenvEnableTemperatureNotification_Object=MibScalar
nnenvEnableTemperatureNotification=_NnenvEnableTemperatureNotification_Object((1,3,6,1,4,1,562,73,1,1,1,3,2,1),_NnenvEnableTemperatureNotification_Type())
nnenvEnableTemperatureNotification.setMaxAccess(_N)
if mibBuilder.loadTexts:nnenvEnableTemperatureNotification.setStatus(_B)
class _NnenvEnableFanNotification_Type(TruthValue):defaultValue=1
_NnenvEnableFanNotification_Type.__name__=_K
_NnenvEnableFanNotification_Object=MibScalar
nnenvEnableFanNotification=_NnenvEnableFanNotification_Object((1,3,6,1,4,1,562,73,1,1,1,3,2,2),_NnenvEnableFanNotification_Type())
nnenvEnableFanNotification.setMaxAccess(_N)
if mibBuilder.loadTexts:nnenvEnableFanNotification.setStatus(_B)
class _NnenvEnablePowerNotification_Type(TruthValue):defaultValue=1
_NnenvEnablePowerNotification_Type.__name__=_K
_NnenvEnablePowerNotification_Object=MibScalar
nnenvEnablePowerNotification=_NnenvEnablePowerNotification_Object((1,3,6,1,4,1,562,73,1,1,1,3,2,3),_NnenvEnablePowerNotification_Type())
nnenvEnablePowerNotification.setMaxAccess(_N)
if mibBuilder.loadTexts:nnenvEnablePowerNotification.setStatus(_B)
_NnenvNotifications_ObjectIdentity=ObjectIdentity
nnenvNotifications=_NnenvNotifications_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,3,3))
_NnenvTraps_ObjectIdentity=ObjectIdentity
nnenvTraps=_NnenvTraps_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,3,3,0))
nnenvTemperatureNotification=NotificationType((1,3,6,1,4,1,562,73,1,1,1,3,3,0,1))
nnenvTemperatureNotification.setObjects(*((_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:nnenvTemperatureNotification.setStatus(_B)
nnenvFanNotification=NotificationType((1,3,6,1,4,1,562,73,1,1,1,3,3,0,2))
nnenvFanNotification.setObjects(*((_A,_M),(_A,_S)))
if mibBuilder.loadTexts:nnenvFanNotification.setStatus(_B)
nnenvPowerSupply1DownNotification=NotificationType((1,3,6,1,4,1,562,73,1,1,1,3,3,0,3))
nnenvPowerSupply1DownNotification.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:nnenvPowerSupply1DownNotification.setStatus(_B)
nnenvPowerSupply1UpNotification=NotificationType((1,3,6,1,4,1,562,73,1,1,1,3,3,0,4))
nnenvPowerSupply1UpNotification.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:nnenvPowerSupply1UpNotification.setStatus(_B)
nnenvPowerSupply2DownNotification=NotificationType((1,3,6,1,4,1,562,73,1,1,1,3,3,0,5))
nnenvPowerSupply2DownNotification.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:nnenvPowerSupply2DownNotification.setStatus(_B)
nnenvPowerSupply2UpNotification=NotificationType((1,3,6,1,4,1,562,73,1,1,1,3,3,0,6))
nnenvPowerSupply2UpNotification.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:nnenvPowerSupply2UpNotification.setStatus(_B)
nnenvironementNotificationGroup=NotificationGroup((1,3,6,1,4,1,562,73,1,1,1,3,4))
nnenvironementNotificationGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:nnenvironementNotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'EnvState':EnvState,'EnvInstalled':EnvInstalled,'EnvStatus':EnvStatus,'EnvType':EnvType,'nnenvironmentMib':nnenvironmentMib,'nnenvObjects':nnenvObjects,'nnenvTempSensorGroup':nnenvTempSensorGroup,_Q:nnenvTempSensorValue,_R:nnenvTempSensorState,'nnenvFanTable':nnenvFanTable,'nnenvFanEntry':nnenvFanEntry,_M:nnenvFanUnitIndex,_S:nnenvFanState,_E:nnenvPwrsupPowerFailCount,'nnenvPwrsupTable':nnenvPwrsupTable,'nnenvPwrsupEntry':nnenvPwrsupEntry,_D:nnenvPwrsupIndex,_F:nnenvPwrsupInstalled,_G:nnenvPwrsupStatus,_H:nnenvPwrsupType,_I:nnenvPwrsupUptime,_J:nnenvPwrsupDowntime,'nnenvNotificationEnables':nnenvNotificationEnables,'nnenvEnableTemperatureNotification':nnenvEnableTemperatureNotification,'nnenvEnableFanNotification':nnenvEnableFanNotification,'nnenvEnablePowerNotification':nnenvEnablePowerNotification,'nnenvNotifications':nnenvNotifications,'nnenvTraps':nnenvTraps,_T:nnenvTemperatureNotification,_U:nnenvFanNotification,_V:nnenvPowerSupply1DownNotification,_W:nnenvPowerSupply1UpNotification,_X:nnenvPowerSupply2DownNotification,_Y:nnenvPowerSupply2UpNotification,'nnenvironementNotificationGroup':nnenvironementNotificationGroup})