_L='environmentUnitIndex'
_K='userIndex'
_J='circuitGroupIndex'
_I='circuitIndex'
_H='not-accessible'
_G='DisplayString'
_F='read-only'
_E='trapInfo'
_D='read-write'
_C='Integer32'
_B='WTI-AFS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
afs=ModuleIdentity((1,3,6,1,4,1,2634,4))
if mibBuilder.loadTexts:afs.setRevisions(('2010-04-02 16:00',))
_WesternTelematic_ObjectIdentity=ObjectIdentity
westernTelematic=_WesternTelematic_ObjectIdentity((1,3,6,1,4,1,2634))
_SystemTables_ObjectIdentity=ObjectIdentity
systemTables=_SystemTables_ObjectIdentity((1,3,6,1,4,1,2634,4,100))
_CircuitTable_Object=MibTable
circuitTable=_CircuitTable_Object((1,3,6,1,4,1,2634,4,100,200))
if mibBuilder.loadTexts:circuitTable.setStatus(_A)
_CircuitEntry_Object=MibTableRow
circuitEntry=_CircuitEntry_Object((1,3,6,1,4,1,2634,4,100,200,1))
circuitEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:circuitEntry.setStatus(_A)
class _CircuitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_CircuitIndex_Type.__name__=_C
_CircuitIndex_Object=MibTableColumn
circuitIndex=_CircuitIndex_Object((1,3,6,1,4,1,2634,4,100,200,1,1),_CircuitIndex_Type())
circuitIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:circuitIndex.setStatus(_A)
class _CircuitID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(9,11))
_CircuitID_Type.__name__=_G
_CircuitID_Object=MibTableColumn
circuitID=_CircuitID_Object((1,3,6,1,4,1,2634,4,100,200,1,2),_CircuitID_Type())
circuitID.setMaxAccess(_F)
if mibBuilder.loadTexts:circuitID.setStatus(_A)
class _CircuitStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_CircuitStatus_Type.__name__=_C
_CircuitStatus_Object=MibTableColumn
circuitStatus=_CircuitStatus_Object((1,3,6,1,4,1,2634,4,100,200,1,3),_CircuitStatus_Type())
circuitStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:circuitStatus.setStatus(_A)
class _CircuitAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_CircuitAction_Type.__name__=_C
_CircuitAction_Object=MibTableColumn
circuitAction=_CircuitAction_Object((1,3,6,1,4,1,2634,4,100,200,1,4),_CircuitAction_Type())
circuitAction.setMaxAccess(_D)
if mibBuilder.loadTexts:circuitAction.setStatus(_A)
_CircuitName_Type=DisplayString
_CircuitName_Object=MibTableColumn
circuitName=_CircuitName_Object((1,3,6,1,4,1,2634,4,100,200,1,5),_CircuitName_Type())
circuitName.setMaxAccess(_F)
if mibBuilder.loadTexts:circuitName.setStatus(_A)
_CircuitReason_Type=Integer32
_CircuitReason_Object=MibTableColumn
circuitReason=_CircuitReason_Object((1,3,6,1,4,1,2634,4,100,200,1,6),_CircuitReason_Type())
circuitReason.setMaxAccess(_F)
if mibBuilder.loadTexts:circuitReason.setStatus(_A)
_CircuitGroupTable_Object=MibTable
circuitGroupTable=_CircuitGroupTable_Object((1,3,6,1,4,1,2634,4,100,300))
if mibBuilder.loadTexts:circuitGroupTable.setStatus(_A)
_CircuitGroupEntry_Object=MibTableRow
circuitGroupEntry=_CircuitGroupEntry_Object((1,3,6,1,4,1,2634,4,100,300,1))
circuitGroupEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:circuitGroupEntry.setStatus(_A)
class _CircuitGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,54))
_CircuitGroupIndex_Type.__name__=_C
_CircuitGroupIndex_Object=MibTableColumn
circuitGroupIndex=_CircuitGroupIndex_Object((1,3,6,1,4,1,2634,4,100,300,1,1),_CircuitGroupIndex_Type())
circuitGroupIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:circuitGroupIndex.setStatus(_A)
class _CircuitGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_CircuitGroupName_Type.__name__=_G
_CircuitGroupName_Object=MibTableColumn
circuitGroupName=_CircuitGroupName_Object((1,3,6,1,4,1,2634,4,100,300,1,2),_CircuitGroupName_Type())
circuitGroupName.setMaxAccess(_F)
if mibBuilder.loadTexts:circuitGroupName.setStatus(_A)
class _CircuitGroupAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_CircuitGroupAction_Type.__name__=_C
_CircuitGroupAction_Object=MibTableColumn
circuitGroupAction=_CircuitGroupAction_Object((1,3,6,1,4,1,2634,4,100,300,1,3),_CircuitGroupAction_Type())
circuitGroupAction.setMaxAccess(_D)
if mibBuilder.loadTexts:circuitGroupAction.setStatus(_A)
_UserTable_Object=MibTable
userTable=_UserTable_Object((1,3,6,1,4,1,2634,4,100,400))
if mibBuilder.loadTexts:userTable.setStatus(_A)
_UserEntry_Object=MibTableRow
userEntry=_UserEntry_Object((1,3,6,1,4,1,2634,4,100,400,1))
userEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:userEntry.setStatus(_A)
class _UserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_UserIndex_Type.__name__=_C
_UserIndex_Object=MibTableColumn
userIndex=_UserIndex_Object((1,3,6,1,4,1,2634,4,100,400,1,1),_UserIndex_Type())
userIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:userIndex.setStatus(_A)
class _UserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UserName_Type.__name__=_G
_UserName_Object=MibTableColumn
userName=_UserName_Object((1,3,6,1,4,1,2634,4,100,400,1,2),_UserName_Type())
userName.setMaxAccess(_D)
if mibBuilder.loadTexts:userName.setStatus(_A)
class _UserPasswd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_UserPasswd_Type.__name__=_G
_UserPasswd_Object=MibTableColumn
userPasswd=_UserPasswd_Object((1,3,6,1,4,1,2634,4,100,400,1,3),_UserPasswd_Type())
userPasswd.setMaxAccess(_D)
if mibBuilder.loadTexts:userPasswd.setStatus(_A)
class _UserAccessLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_UserAccessLevel_Type.__name__=_C
_UserAccessLevel_Object=MibTableColumn
userAccessLevel=_UserAccessLevel_Object((1,3,6,1,4,1,2634,4,100,400,1,4),_UserAccessLevel_Type())
userAccessLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:userAccessLevel.setStatus(_A)
class _UserCircuitAccess_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_UserCircuitAccess_Type.__name__=_G
_UserCircuitAccess_Object=MibTableColumn
userCircuitAccess=_UserCircuitAccess_Object((1,3,6,1,4,1,2634,4,100,400,1,6),_UserCircuitAccess_Type())
userCircuitAccess.setMaxAccess(_D)
if mibBuilder.loadTexts:userCircuitAccess.setStatus(_A)
class _UserGroupAccess_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,54))
_UserGroupAccess_Type.__name__=_G
_UserGroupAccess_Object=MibTableColumn
userGroupAccess=_UserGroupAccess_Object((1,3,6,1,4,1,2634,4,100,400,1,10),_UserGroupAccess_Type())
userGroupAccess.setMaxAccess(_D)
if mibBuilder.loadTexts:userGroupAccess.setStatus(_A)
class _UserSerialAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_UserSerialAccess_Type.__name__=_C
_UserSerialAccess_Object=MibTableColumn
userSerialAccess=_UserSerialAccess_Object((1,3,6,1,4,1,2634,4,100,400,1,11),_UserSerialAccess_Type())
userSerialAccess.setMaxAccess(_D)
if mibBuilder.loadTexts:userSerialAccess.setStatus(_A)
class _UserTelnetSshAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_UserTelnetSshAccess_Type.__name__=_C
_UserTelnetSshAccess_Object=MibTableColumn
userTelnetSshAccess=_UserTelnetSshAccess_Object((1,3,6,1,4,1,2634,4,100,400,1,12),_UserTelnetSshAccess_Type())
userTelnetSshAccess.setMaxAccess(_D)
if mibBuilder.loadTexts:userTelnetSshAccess.setStatus(_A)
class _UserWebAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_UserWebAccess_Type.__name__=_C
_UserWebAccess_Object=MibTableColumn
userWebAccess=_UserWebAccess_Object((1,3,6,1,4,1,2634,4,100,400,1,13),_UserWebAccess_Type())
userWebAccess.setMaxAccess(_D)
if mibBuilder.loadTexts:userWebAccess.setStatus(_A)
class _UserOutboundTelAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_UserOutboundTelAccess_Type.__name__=_C
_UserOutboundTelAccess_Object=MibTableColumn
userOutboundTelAccess=_UserOutboundTelAccess_Object((1,3,6,1,4,1,2634,4,100,400,1,14),_UserOutboundTelAccess_Type())
userOutboundTelAccess.setMaxAccess(_D)
if mibBuilder.loadTexts:userOutboundTelAccess.setStatus(_A)
class _UserCallbackNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UserCallbackNum_Type.__name__=_G
_UserCallbackNum_Object=MibTableColumn
userCallbackNum=_UserCallbackNum_Object((1,3,6,1,4,1,2634,4,100,400,1,16),_UserCallbackNum_Type())
userCallbackNum.setMaxAccess(_D)
if mibBuilder.loadTexts:userCallbackNum.setStatus(_A)
class _UserSubmit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_UserSubmit_Type.__name__=_C
_UserSubmit_Object=MibTableColumn
userSubmit=_UserSubmit_Object((1,3,6,1,4,1,2634,4,100,400,1,31),_UserSubmit_Type())
userSubmit.setMaxAccess(_D)
if mibBuilder.loadTexts:userSubmit.setStatus(_A)
_EnvironmentTables_ObjectIdentity=ObjectIdentity
environmentTables=_EnvironmentTables_ObjectIdentity((1,3,6,1,4,1,2634,4,200))
_EnvironmentUnitTable_Object=MibTable
environmentUnitTable=_EnvironmentUnitTable_Object((1,3,6,1,4,1,2634,4,200,10))
if mibBuilder.loadTexts:environmentUnitTable.setStatus(_A)
_EnvironmentUnitEntry_Object=MibTableRow
environmentUnitEntry=_EnvironmentUnitEntry_Object((1,3,6,1,4,1,2634,4,200,10,1))
environmentUnitEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:environmentUnitEntry.setStatus(_A)
class _EnvironmentUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_EnvironmentUnitIndex_Type.__name__=_C
_EnvironmentUnitIndex_Object=MibTableColumn
environmentUnitIndex=_EnvironmentUnitIndex_Object((1,3,6,1,4,1,2634,4,200,10,1,1),_EnvironmentUnitIndex_Type())
environmentUnitIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:environmentUnitIndex.setStatus(_A)
class _EnvironmentUnitName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_EnvironmentUnitName_Type.__name__=_G
_EnvironmentUnitName_Object=MibTableColumn
environmentUnitName=_EnvironmentUnitName_Object((1,3,6,1,4,1,2634,4,200,10,1,2),_EnvironmentUnitName_Type())
environmentUnitName.setMaxAccess(_F)
if mibBuilder.loadTexts:environmentUnitName.setStatus(_A)
_EnvironmentUnitTemperature_Type=Integer32
_EnvironmentUnitTemperature_Object=MibTableColumn
environmentUnitTemperature=_EnvironmentUnitTemperature_Object((1,3,6,1,4,1,2634,4,200,10,1,3),_EnvironmentUnitTemperature_Type())
environmentUnitTemperature.setMaxAccess(_F)
if mibBuilder.loadTexts:environmentUnitTemperature.setStatus(_A)
_EnvironmentUnitMonitorAlarm_Type=Integer32
_EnvironmentUnitMonitorAlarm_Object=MibTableColumn
environmentUnitMonitorAlarm=_EnvironmentUnitMonitorAlarm_Object((1,3,6,1,4,1,2634,4,200,10,1,17),_EnvironmentUnitMonitorAlarm_Type())
environmentUnitMonitorAlarm.setMaxAccess(_F)
if mibBuilder.loadTexts:environmentUnitMonitorAlarm.setStatus(_A)
_EnvironmentSysRAM_Type=Integer32
_EnvironmentSysRAM_Object=MibTableColumn
environmentSysRAM=_EnvironmentSysRAM_Object((1,3,6,1,4,1,2634,4,200,10,1,18),_EnvironmentSysRAM_Type())
environmentSysRAM.setMaxAccess(_F)
if mibBuilder.loadTexts:environmentSysRAM.setStatus(_A)
_EnvironmentSysFlash_Type=Integer32
_EnvironmentSysFlash_Object=MibTableColumn
environmentSysFlash=_EnvironmentSysFlash_Object((1,3,6,1,4,1,2634,4,200,10,1,19),_EnvironmentSysFlash_Type())
environmentSysFlash.setMaxAccess(_F)
if mibBuilder.loadTexts:environmentSysFlash.setStatus(_A)
_WtiTraps_ObjectIdentity=ObjectIdentity
wtiTraps=_WtiTraps_ObjectIdentity((1,3,6,1,4,1,2634,4,300))
_TrapInfo_Type=DisplayString
_TrapInfo_Object=MibScalar
trapInfo=_TrapInfo_Object((1,3,6,1,4,1,2634,4,300,1),_TrapInfo_Type())
trapInfo.setMaxAccess(_F)
if mibBuilder.loadTexts:trapInfo.setStatus(_A)
_TestTraps_ObjectIdentity=ObjectIdentity
testTraps=_TestTraps_ObjectIdentity((1,3,6,1,4,1,2634,4,300,2))
_OverTemperatureInitialTraps_ObjectIdentity=ObjectIdentity
overTemperatureInitialTraps=_OverTemperatureInitialTraps_ObjectIdentity((1,3,6,1,4,1,2634,4,300,6))
_OverTemperatureCriticalTraps_ObjectIdentity=ObjectIdentity
overTemperatureCriticalTraps=_OverTemperatureCriticalTraps_ObjectIdentity((1,3,6,1,4,1,2634,4,300,7))
_PingNoAnswerTraps_ObjectIdentity=ObjectIdentity
pingNoAnswerTraps=_PingNoAnswerTraps_ObjectIdentity((1,3,6,1,4,1,2634,4,300,11))
_LockoutTraps_ObjectIdentity=ObjectIdentity
lockoutTraps=_LockoutTraps_ObjectIdentity((1,3,6,1,4,1,2634,4,300,12))
_PowercycleTraps_ObjectIdentity=ObjectIdentity
powercycleTraps=_PowercycleTraps_ObjectIdentity((1,3,6,1,4,1,2634,4,300,13))
_MonitorAlarmTraps_ObjectIdentity=ObjectIdentity
monitorAlarmTraps=_MonitorAlarmTraps_ObjectIdentity((1,3,6,1,4,1,2634,4,300,14))
testTrap=NotificationType((1,3,6,1,4,1,2634,4,300,2,0,1))
testTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:testTrap.setStatus('')
overTemperatureInitialSetTrap=NotificationType((1,3,6,1,4,1,2634,4,300,6,0,1))
overTemperatureInitialSetTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:overTemperatureInitialSetTrap.setStatus('')
overTemperatureInitialClearTrap=NotificationType((1,3,6,1,4,1,2634,4,300,6,0,2))
overTemperatureInitialClearTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:overTemperatureInitialClearTrap.setStatus('')
overTemperatureCriticalSetTrap=NotificationType((1,3,6,1,4,1,2634,4,300,7,0,1))
overTemperatureCriticalSetTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:overTemperatureCriticalSetTrap.setStatus('')
overTemperatureCriticalClearTrap=NotificationType((1,3,6,1,4,1,2634,4,300,7,0,2))
overTemperatureCriticalClearTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:overTemperatureCriticalClearTrap.setStatus('')
pingNoAnswerSetTrap=NotificationType((1,3,6,1,4,1,2634,4,300,11,0,1))
pingNoAnswerSetTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:pingNoAnswerSetTrap.setStatus('')
pingNoAnswerClearTrap=NotificationType((1,3,6,1,4,1,2634,4,300,11,0,2))
pingNoAnswerClearTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:pingNoAnswerClearTrap.setStatus('')
lockoutSetTrap=NotificationType((1,3,6,1,4,1,2634,4,300,12,0,1))
lockoutSetTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:lockoutSetTrap.setStatus('')
lockoutClearTrap=NotificationType((1,3,6,1,4,1,2634,4,300,12,0,2))
lockoutClearTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:lockoutClearTrap.setStatus('')
powercycleSetTrap=NotificationType((1,3,6,1,4,1,2634,4,300,13,0,1))
powercycleSetTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:powercycleSetTrap.setStatus('')
monitorAlarmSetTrap=NotificationType((1,3,6,1,4,1,2634,4,300,14,0,1))
monitorAlarmSetTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:monitorAlarmSetTrap.setStatus('')
monitorAlarmClearTrap=NotificationType((1,3,6,1,4,1,2634,4,300,14,0,2))
monitorAlarmClearTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:monitorAlarmClearTrap.setStatus('')
mibBuilder.exportSymbols(_B,**{'westernTelematic':westernTelematic,'afs':afs,'systemTables':systemTables,'circuitTable':circuitTable,'circuitEntry':circuitEntry,_I:circuitIndex,'circuitID':circuitID,'circuitStatus':circuitStatus,'circuitAction':circuitAction,'circuitName':circuitName,'circuitReason':circuitReason,'circuitGroupTable':circuitGroupTable,'circuitGroupEntry':circuitGroupEntry,_J:circuitGroupIndex,'circuitGroupName':circuitGroupName,'circuitGroupAction':circuitGroupAction,'userTable':userTable,'userEntry':userEntry,_K:userIndex,'userName':userName,'userPasswd':userPasswd,'userAccessLevel':userAccessLevel,'userCircuitAccess':userCircuitAccess,'userGroupAccess':userGroupAccess,'userSerialAccess':userSerialAccess,'userTelnetSshAccess':userTelnetSshAccess,'userWebAccess':userWebAccess,'userOutboundTelAccess':userOutboundTelAccess,'userCallbackNum':userCallbackNum,'userSubmit':userSubmit,'environmentTables':environmentTables,'environmentUnitTable':environmentUnitTable,'environmentUnitEntry':environmentUnitEntry,_L:environmentUnitIndex,'environmentUnitName':environmentUnitName,'environmentUnitTemperature':environmentUnitTemperature,'environmentUnitMonitorAlarm':environmentUnitMonitorAlarm,'environmentSysRAM':environmentSysRAM,'environmentSysFlash':environmentSysFlash,'wtiTraps':wtiTraps,_E:trapInfo,'testTraps':testTraps,'testTrap':testTrap,'overTemperatureInitialTraps':overTemperatureInitialTraps,'overTemperatureInitialSetTrap':overTemperatureInitialSetTrap,'overTemperatureInitialClearTrap':overTemperatureInitialClearTrap,'overTemperatureCriticalTraps':overTemperatureCriticalTraps,'overTemperatureCriticalSetTrap':overTemperatureCriticalSetTrap,'overTemperatureCriticalClearTrap':overTemperatureCriticalClearTrap,'pingNoAnswerTraps':pingNoAnswerTraps,'pingNoAnswerSetTrap':pingNoAnswerSetTrap,'pingNoAnswerClearTrap':pingNoAnswerClearTrap,'lockoutTraps':lockoutTraps,'lockoutSetTrap':lockoutSetTrap,'lockoutClearTrap':lockoutClearTrap,'powercycleTraps':powercycleTraps,'powercycleSetTrap':powercycleSetTrap,'monitorAlarmTraps':monitorAlarmTraps,'monitorAlarmSetTrap':monitorAlarmSetTrap,'monitorAlarmClearTrap':monitorAlarmClearTrap})