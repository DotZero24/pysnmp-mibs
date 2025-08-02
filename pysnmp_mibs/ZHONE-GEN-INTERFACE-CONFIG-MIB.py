_D='ifIndex'
_C='IF-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
zhoneInterfaceConfig,zhoneModules=mibBuilder.importSymbols('Zhone','zhoneInterfaceConfig','zhoneModules')
ZhoneAlarmSeverity,ZhoneRowStatus=mibBuilder.importSymbols('Zhone-TC','ZhoneAlarmSeverity','ZhoneRowStatus')
alarmConfigMib=ModuleIdentity((1,3,6,1,4,1,5504,3,13,1))
if mibBuilder.loadTexts:alarmConfigMib.setRevisions(('2010-12-07 02:37','2008-02-26 06:25'))
_AlarmConfigTable_Object=MibTable
alarmConfigTable=_AlarmConfigTable_Object((1,3,6,1,4,1,5504,3,13,1,1))
if mibBuilder.loadTexts:alarmConfigTable.setStatus(_A)
_AlarmConfigEntry_Object=MibTableRow
alarmConfigEntry=_AlarmConfigEntry_Object((1,3,6,1,4,1,5504,3,13,1,1,1))
alarmConfigEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:alarmConfigEntry.setStatus(_A)
_AlarmConfigBitRateThreshold_Type=TruthValue
_AlarmConfigBitRateThreshold_Object=MibTableColumn
alarmConfigBitRateThreshold=_AlarmConfigBitRateThreshold_Object((1,3,6,1,4,1,5504,3,13,1,1,1,1),_AlarmConfigBitRateThreshold_Type())
alarmConfigBitRateThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmConfigBitRateThreshold.setStatus(_A)
_AlarmConfigBitRateThresholdValue_Type=Integer32
_AlarmConfigBitRateThresholdValue_Object=MibTableColumn
alarmConfigBitRateThresholdValue=_AlarmConfigBitRateThresholdValue_Object((1,3,6,1,4,1,5504,3,13,1,1,1,2),_AlarmConfigBitRateThresholdValue_Type())
alarmConfigBitRateThresholdValue.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmConfigBitRateThresholdValue.setStatus(_A)
_AlarmConfigBitRateThresholdHoldtime_Type=Integer32
_AlarmConfigBitRateThresholdHoldtime_Object=MibTableColumn
alarmConfigBitRateThresholdHoldtime=_AlarmConfigBitRateThresholdHoldtime_Object((1,3,6,1,4,1,5504,3,13,1,1,1,3),_AlarmConfigBitRateThresholdHoldtime_Type())
alarmConfigBitRateThresholdHoldtime.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmConfigBitRateThresholdHoldtime.setStatus(_A)
_AlarmConfigStatusTrap_Type=TruthValue
_AlarmConfigStatusTrap_Object=MibTableColumn
alarmConfigStatusTrap=_AlarmConfigStatusTrap_Object((1,3,6,1,4,1,5504,3,13,1,1,1,4),_AlarmConfigStatusTrap_Type())
alarmConfigStatusTrap.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmConfigStatusTrap.setStatus(_A)
_AlarmConfigAdminUp_Type=TruthValue
_AlarmConfigAdminUp_Object=MibTableColumn
alarmConfigAdminUp=_AlarmConfigAdminUp_Object((1,3,6,1,4,1,5504,3,13,1,1,1,5),_AlarmConfigAdminUp_Type())
alarmConfigAdminUp.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmConfigAdminUp.setStatus(_A)
_AlarmConfigAlarmSeverity_Type=ZhoneAlarmSeverity
_AlarmConfigAlarmSeverity_Object=MibTableColumn
alarmConfigAlarmSeverity=_AlarmConfigAlarmSeverity_Object((1,3,6,1,4,1,5504,3,13,1,1,1,6),_AlarmConfigAlarmSeverity_Type())
alarmConfigAlarmSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmConfigAlarmSeverity.setStatus(_A)
_AlarmConfigRowStatus_Type=ZhoneRowStatus
_AlarmConfigRowStatus_Object=MibTableColumn
alarmConfigRowStatus=_AlarmConfigRowStatus_Object((1,3,6,1,4,1,5504,3,13,1,1,1,7),_AlarmConfigRowStatus_Type())
alarmConfigRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmConfigRowStatus.setStatus(_A)
_AlarmConfigTraps_ObjectIdentity=ObjectIdentity
alarmConfigTraps=_AlarmConfigTraps_ObjectIdentity((1,3,6,1,4,1,5504,3,13,1,2))
_AlarmConfigTrapPrefix_ObjectIdentity=ObjectIdentity
alarmConfigTrapPrefix=_AlarmConfigTrapPrefix_ObjectIdentity((1,3,6,1,4,1,5504,3,13,1,2,0))
if mibBuilder.loadTexts:alarmConfigTrapPrefix.setStatus(_A)
zhoneAlarmConfigThresholdTrap=NotificationType((1,3,6,1,4,1,5504,3,13,1,2,0,1))
if mibBuilder.loadTexts:zhoneAlarmConfigThresholdTrap.setStatus(_A)
zhoneAlarmConfigThresholdClearTrap=NotificationType((1,3,6,1,4,1,5504,3,13,1,2,0,2))
if mibBuilder.loadTexts:zhoneAlarmConfigThresholdClearTrap.setStatus(_A)
mibBuilder.exportSymbols('ZHONE-GEN-INTERFACE-CONFIG-MIB',**{'alarmConfigMib':alarmConfigMib,'alarmConfigTable':alarmConfigTable,'alarmConfigEntry':alarmConfigEntry,'alarmConfigBitRateThreshold':alarmConfigBitRateThreshold,'alarmConfigBitRateThresholdValue':alarmConfigBitRateThresholdValue,'alarmConfigBitRateThresholdHoldtime':alarmConfigBitRateThresholdHoldtime,'alarmConfigStatusTrap':alarmConfigStatusTrap,'alarmConfigAdminUp':alarmConfigAdminUp,'alarmConfigAlarmSeverity':alarmConfigAlarmSeverity,'alarmConfigRowStatus':alarmConfigRowStatus,'alarmConfigTraps':alarmConfigTraps,'alarmConfigTrapPrefix':alarmConfigTrapPrefix,'zhoneAlarmConfigThresholdTrap':zhoneAlarmConfigThresholdTrap,'zhoneAlarmConfigThresholdClearTrap':zhoneAlarmConfigThresholdClearTrap})