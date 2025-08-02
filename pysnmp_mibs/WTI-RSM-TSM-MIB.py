_M='environmentUnitIndex'
_L='userIndex'
_K='plugGroupIndex'
_J='plugIndex'
_I='portIndex'
_H='not-accessible'
_G='DisplayString'
_F='read-write'
_E='Integer32'
_D='trapInfo'
_C='read-only'
_B='WTI-RSM-TSM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
rsm_tsm=ModuleIdentity((1,3,6,1,4,1,2634,1))
if mibBuilder.loadTexts:rsm_tsm.setRevisions(('2014-01-08 16:00',))
_WesternTelematic_ObjectIdentity=ObjectIdentity
westernTelematic=_WesternTelematic_ObjectIdentity((1,3,6,1,4,1,2634))
_SystemTables_ObjectIdentity=ObjectIdentity
systemTables=_SystemTables_ObjectIdentity((1,3,6,1,4,1,2634,1,100))
_PortTable_Object=MibTable
portTable=_PortTable_Object((1,3,6,1,4,1,2634,1,100,100))
if mibBuilder.loadTexts:portTable.setStatus(_A)
_PortEntry_Object=MibTableRow
portEntry=_PortEntry_Object((1,3,6,1,4,1,2634,1,100,100,1))
portEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:portEntry.setStatus(_A)
class _PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,41))
_PortIndex_Type.__name__=_E
_PortIndex_Object=MibTableColumn
portIndex=_PortIndex_Object((1,3,6,1,4,1,2634,1,100,100,1,1),_PortIndex_Type())
portIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:portIndex.setStatus(_A)
class _PortID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,7))
_PortID_Type.__name__=_G
_PortID_Object=MibTableColumn
portID=_PortID_Object((1,3,6,1,4,1,2634,1,100,100,1,2),_PortID_Type())
portID.setMaxAccess(_C)
if mibBuilder.loadTexts:portID.setStatus(_A)
_PortName_Type=DisplayString
_PortName_Object=MibTableColumn
portName=_PortName_Object((1,3,6,1,4,1,2634,1,100,100,1,3),_PortName_Type())
portName.setMaxAccess(_C)
if mibBuilder.loadTexts:portName.setStatus(_A)
class _PortBufferThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,262144))
_PortBufferThreshold_Type.__name__=_E
_PortBufferThreshold_Object=MibTableColumn
portBufferThreshold=_PortBufferThreshold_Object((1,3,6,1,4,1,2634,1,100,100,1,4),_PortBufferThreshold_Type())
portBufferThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:portBufferThreshold.setStatus(_A)
_PortUserName_Type=DisplayString
_PortUserName_Object=MibTableColumn
portUserName=_PortUserName_Object((1,3,6,1,4,1,2634,1,100,100,1,5),_PortUserName_Type())
portUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:portUserName.setStatus(_A)
_PortStatus_Type=DisplayString
_PortStatus_Object=MibTableColumn
portStatus=_PortStatus_Object((1,3,6,1,4,1,2634,1,100,100,1,6),_PortStatus_Type())
portStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:portStatus.setStatus(_A)
_PortBufferCt_Type=Integer32
_PortBufferCt_Object=MibTableColumn
portBufferCt=_PortBufferCt_Object((1,3,6,1,4,1,2634,1,100,100,1,7),_PortBufferCt_Type())
portBufferCt.setMaxAccess(_C)
if mibBuilder.loadTexts:portBufferCt.setStatus(_A)
_PlugTable_Object=MibTable
plugTable=_PlugTable_Object((1,3,6,1,4,1,2634,1,100,200))
if mibBuilder.loadTexts:plugTable.setStatus(_A)
_PlugEntry_Object=MibTableRow
plugEntry=_PlugEntry_Object((1,3,6,1,4,1,2634,1,100,200,1))
plugEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:plugEntry.setStatus(_A)
class _PlugIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,80))
_PlugIndex_Type.__name__=_E
_PlugIndex_Object=MibTableColumn
plugIndex=_PlugIndex_Object((1,3,6,1,4,1,2634,1,100,200,1,1),_PlugIndex_Type())
plugIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:plugIndex.setStatus(_A)
class _PlugID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(9,11))
_PlugID_Type.__name__=_G
_PlugID_Object=MibTableColumn
plugID=_PlugID_Object((1,3,6,1,4,1,2634,1,100,200,1,2),_PlugID_Type())
plugID.setMaxAccess(_C)
if mibBuilder.loadTexts:plugID.setStatus(_A)
class _PlugStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_PlugStatus_Type.__name__=_E
_PlugStatus_Object=MibTableColumn
plugStatus=_PlugStatus_Object((1,3,6,1,4,1,2634,1,100,200,1,3),_PlugStatus_Type())
plugStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:plugStatus.setStatus(_A)
class _PlugAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_PlugAction_Type.__name__=_E
_PlugAction_Object=MibTableColumn
plugAction=_PlugAction_Object((1,3,6,1,4,1,2634,1,100,200,1,4),_PlugAction_Type())
plugAction.setMaxAccess(_F)
if mibBuilder.loadTexts:plugAction.setStatus(_A)
_PlugName_Type=DisplayString
_PlugName_Object=MibTableColumn
plugName=_PlugName_Object((1,3,6,1,4,1,2634,1,100,200,1,5),_PlugName_Type())
plugName.setMaxAccess(_C)
if mibBuilder.loadTexts:plugName.setStatus(_A)
_PlugCurrent_Type=Integer32
_PlugCurrent_Object=MibTableColumn
plugCurrent=_PlugCurrent_Object((1,3,6,1,4,1,2634,1,100,200,1,7),_PlugCurrent_Type())
plugCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:plugCurrent.setStatus(_A)
_PlugPower_Type=Integer32
_PlugPower_Object=MibTableColumn
plugPower=_PlugPower_Object((1,3,6,1,4,1,2634,1,100,200,1,8),_PlugPower_Type())
plugPower.setMaxAccess(_C)
if mibBuilder.loadTexts:plugPower.setStatus(_A)
_PlugGroupTable_Object=MibTable
plugGroupTable=_PlugGroupTable_Object((1,3,6,1,4,1,2634,1,100,300))
if mibBuilder.loadTexts:plugGroupTable.setStatus(_A)
_PlugGroupEntry_Object=MibTableRow
plugGroupEntry=_PlugGroupEntry_Object((1,3,6,1,4,1,2634,1,100,300,1))
plugGroupEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:plugGroupEntry.setStatus(_A)
class _PlugGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,54))
_PlugGroupIndex_Type.__name__=_E
_PlugGroupIndex_Object=MibTableColumn
plugGroupIndex=_PlugGroupIndex_Object((1,3,6,1,4,1,2634,1,100,300,1,1),_PlugGroupIndex_Type())
plugGroupIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:plugGroupIndex.setStatus(_A)
class _PlugGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_PlugGroupName_Type.__name__=_G
_PlugGroupName_Object=MibTableColumn
plugGroupName=_PlugGroupName_Object((1,3,6,1,4,1,2634,1,100,300,1,2),_PlugGroupName_Type())
plugGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:plugGroupName.setStatus(_A)
class _PlugGroupAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_PlugGroupAction_Type.__name__=_E
_PlugGroupAction_Object=MibTableColumn
plugGroupAction=_PlugGroupAction_Object((1,3,6,1,4,1,2634,1,100,300,1,3),_PlugGroupAction_Type())
plugGroupAction.setMaxAccess(_F)
if mibBuilder.loadTexts:plugGroupAction.setStatus(_A)
_PlugGroupCurrent_Type=Integer32
_PlugGroupCurrent_Object=MibTableColumn
plugGroupCurrent=_PlugGroupCurrent_Object((1,3,6,1,4,1,2634,1,100,300,1,4),_PlugGroupCurrent_Type())
plugGroupCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:plugGroupCurrent.setStatus(_A)
_PlugGroupPower_Type=Integer32
_PlugGroupPower_Object=MibTableColumn
plugGroupPower=_PlugGroupPower_Object((1,3,6,1,4,1,2634,1,100,300,1,5),_PlugGroupPower_Type())
plugGroupPower.setMaxAccess(_C)
if mibBuilder.loadTexts:plugGroupPower.setStatus(_A)
_UserTable_Object=MibTable
userTable=_UserTable_Object((1,3,6,1,4,1,2634,1,100,400))
if mibBuilder.loadTexts:userTable.setStatus(_A)
_UserEntry_Object=MibTableRow
userEntry=_UserEntry_Object((1,3,6,1,4,1,2634,1,100,400,1))
userEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:userEntry.setStatus(_A)
class _UserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_UserIndex_Type.__name__=_E
_UserIndex_Object=MibTableColumn
userIndex=_UserIndex_Object((1,3,6,1,4,1,2634,1,100,400,1,1),_UserIndex_Type())
userIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:userIndex.setStatus(_A)
class _UserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UserName_Type.__name__=_G
_UserName_Object=MibTableColumn
userName=_UserName_Object((1,3,6,1,4,1,2634,1,100,400,1,2),_UserName_Type())
userName.setMaxAccess(_F)
if mibBuilder.loadTexts:userName.setStatus(_A)
class _UserPasswd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_UserPasswd_Type.__name__=_G
_UserPasswd_Object=MibTableColumn
userPasswd=_UserPasswd_Object((1,3,6,1,4,1,2634,1,100,400,1,3),_UserPasswd_Type())
userPasswd.setMaxAccess(_F)
if mibBuilder.loadTexts:userPasswd.setStatus(_A)
class _UserAccessLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_UserAccessLevel_Type.__name__=_E
_UserAccessLevel_Object=MibTableColumn
userAccessLevel=_UserAccessLevel_Object((1,3,6,1,4,1,2634,1,100,400,1,4),_UserAccessLevel_Type())
userAccessLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:userAccessLevel.setStatus(_A)
class _UserPortAccess_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,41))
_UserPortAccess_Type.__name__=_G
_UserPortAccess_Object=MibTableColumn
userPortAccess=_UserPortAccess_Object((1,3,6,1,4,1,2634,1,100,400,1,5),_UserPortAccess_Type())
userPortAccess.setMaxAccess(_F)
if mibBuilder.loadTexts:userPortAccess.setStatus(_A)
class _UserPlugAccess_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_UserPlugAccess_Type.__name__=_G
_UserPlugAccess_Object=MibTableColumn
userPlugAccess=_UserPlugAccess_Object((1,3,6,1,4,1,2634,1,100,400,1,6),_UserPlugAccess_Type())
userPlugAccess.setMaxAccess(_F)
if mibBuilder.loadTexts:userPlugAccess.setStatus(_A)
class _UserGroupAccess_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,54))
_UserGroupAccess_Type.__name__=_G
_UserGroupAccess_Object=MibTableColumn
userGroupAccess=_UserGroupAccess_Object((1,3,6,1,4,1,2634,1,100,400,1,10),_UserGroupAccess_Type())
userGroupAccess.setMaxAccess(_F)
if mibBuilder.loadTexts:userGroupAccess.setStatus(_A)
class _UserSerialAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_UserSerialAccess_Type.__name__=_E
_UserSerialAccess_Object=MibTableColumn
userSerialAccess=_UserSerialAccess_Object((1,3,6,1,4,1,2634,1,100,400,1,11),_UserSerialAccess_Type())
userSerialAccess.setMaxAccess(_F)
if mibBuilder.loadTexts:userSerialAccess.setStatus(_A)
class _UserTelnetSshAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_UserTelnetSshAccess_Type.__name__=_E
_UserTelnetSshAccess_Object=MibTableColumn
userTelnetSshAccess=_UserTelnetSshAccess_Object((1,3,6,1,4,1,2634,1,100,400,1,12),_UserTelnetSshAccess_Type())
userTelnetSshAccess.setMaxAccess(_F)
if mibBuilder.loadTexts:userTelnetSshAccess.setStatus(_A)
class _UserWebAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_UserWebAccess_Type.__name__=_E
_UserWebAccess_Object=MibTableColumn
userWebAccess=_UserWebAccess_Object((1,3,6,1,4,1,2634,1,100,400,1,13),_UserWebAccess_Type())
userWebAccess.setMaxAccess(_F)
if mibBuilder.loadTexts:userWebAccess.setStatus(_A)
class _UserOutboundTelAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_UserOutboundTelAccess_Type.__name__=_E
_UserOutboundTelAccess_Object=MibTableColumn
userOutboundTelAccess=_UserOutboundTelAccess_Object((1,3,6,1,4,1,2634,1,100,400,1,14),_UserOutboundTelAccess_Type())
userOutboundTelAccess.setMaxAccess(_F)
if mibBuilder.loadTexts:userOutboundTelAccess.setStatus(_A)
class _UserCallbackNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UserCallbackNum_Type.__name__=_G
_UserCallbackNum_Object=MibTableColumn
userCallbackNum=_UserCallbackNum_Object((1,3,6,1,4,1,2634,1,100,400,1,16),_UserCallbackNum_Type())
userCallbackNum.setMaxAccess(_F)
if mibBuilder.loadTexts:userCallbackNum.setStatus(_A)
class _UserSubmit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_UserSubmit_Type.__name__=_E
_UserSubmit_Object=MibTableColumn
userSubmit=_UserSubmit_Object((1,3,6,1,4,1,2634,1,100,400,1,31),_UserSubmit_Type())
userSubmit.setMaxAccess(_F)
if mibBuilder.loadTexts:userSubmit.setStatus(_A)
_EnvironmentTables_ObjectIdentity=ObjectIdentity
environmentTables=_EnvironmentTables_ObjectIdentity((1,3,6,1,4,1,2634,1,200))
_EnvironmentUnitTable_Object=MibTable
environmentUnitTable=_EnvironmentUnitTable_Object((1,3,6,1,4,1,2634,1,200,10))
if mibBuilder.loadTexts:environmentUnitTable.setStatus(_A)
_EnvironmentUnitEntry_Object=MibTableRow
environmentUnitEntry=_EnvironmentUnitEntry_Object((1,3,6,1,4,1,2634,1,200,10,1))
environmentUnitEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:environmentUnitEntry.setStatus(_A)
class _EnvironmentUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_EnvironmentUnitIndex_Type.__name__=_E
_EnvironmentUnitIndex_Object=MibTableColumn
environmentUnitIndex=_EnvironmentUnitIndex_Object((1,3,6,1,4,1,2634,1,200,10,1,1),_EnvironmentUnitIndex_Type())
environmentUnitIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:environmentUnitIndex.setStatus(_A)
_EnvironmentUnitName_Type=DisplayString
_EnvironmentUnitName_Object=MibTableColumn
environmentUnitName=_EnvironmentUnitName_Object((1,3,6,1,4,1,2634,1,200,10,1,2),_EnvironmentUnitName_Type())
environmentUnitName.setMaxAccess(_C)
if mibBuilder.loadTexts:environmentUnitName.setStatus(_A)
_EnvironmentUnitTemperature_Type=Integer32
_EnvironmentUnitTemperature_Object=MibTableColumn
environmentUnitTemperature=_EnvironmentUnitTemperature_Object((1,3,6,1,4,1,2634,1,200,10,1,3),_EnvironmentUnitTemperature_Type())
environmentUnitTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:environmentUnitTemperature.setStatus(_A)
_EnvironmentSysRAM_Type=Integer32
_EnvironmentSysRAM_Object=MibTableColumn
environmentSysRAM=_EnvironmentSysRAM_Object((1,3,6,1,4,1,2634,1,200,10,1,18),_EnvironmentSysRAM_Type())
environmentSysRAM.setMaxAccess(_C)
if mibBuilder.loadTexts:environmentSysRAM.setStatus(_A)
_EnvironmentSysFlash_Type=Integer32
_EnvironmentSysFlash_Object=MibTableColumn
environmentSysFlash=_EnvironmentSysFlash_Object((1,3,6,1,4,1,2634,1,200,10,1,19),_EnvironmentSysFlash_Type())
environmentSysFlash.setMaxAccess(_C)
if mibBuilder.loadTexts:environmentSysFlash.setStatus(_A)
_EnvironmentMacEth0_Type=DisplayString
_EnvironmentMacEth0_Object=MibTableColumn
environmentMacEth0=_EnvironmentMacEth0_Object((1,3,6,1,4,1,2634,1,200,10,1,20),_EnvironmentMacEth0_Type())
environmentMacEth0.setMaxAccess(_C)
if mibBuilder.loadTexts:environmentMacEth0.setStatus(_A)
_EnvironmentMacEth1_Type=DisplayString
_EnvironmentMacEth1_Object=MibTableColumn
environmentMacEth1=_EnvironmentMacEth1_Object((1,3,6,1,4,1,2634,1,200,10,1,21),_EnvironmentMacEth1_Type())
environmentMacEth1.setMaxAccess(_C)
if mibBuilder.loadTexts:environmentMacEth1.setStatus(_A)
_AlarmTables_ObjectIdentity=ObjectIdentity
alarmTables=_AlarmTables_ObjectIdentity((1,3,6,1,4,1,2634,1,280))
_AlarmOverCurrentInitial_Type=Integer32
_AlarmOverCurrentInitial_Object=MibScalar
alarmOverCurrentInitial=_AlarmOverCurrentInitial_Object((1,3,6,1,4,1,2634,1,280,1),_AlarmOverCurrentInitial_Type())
alarmOverCurrentInitial.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmOverCurrentInitial.setStatus(_A)
_AlarmOverCurrentCritical_Type=Integer32
_AlarmOverCurrentCritical_Object=MibScalar
alarmOverCurrentCritical=_AlarmOverCurrentCritical_Object((1,3,6,1,4,1,2634,1,280,2),_AlarmOverCurrentCritical_Type())
alarmOverCurrentCritical.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmOverCurrentCritical.setStatus(_A)
_AlarmOverTemperatureInitial_Type=Integer32
_AlarmOverTemperatureInitial_Object=MibScalar
alarmOverTemperatureInitial=_AlarmOverTemperatureInitial_Object((1,3,6,1,4,1,2634,1,280,3),_AlarmOverTemperatureInitial_Type())
alarmOverTemperatureInitial.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmOverTemperatureInitial.setStatus(_A)
_AlarmOverTemperatureCritical_Type=Integer32
_AlarmOverTemperatureCritical_Object=MibScalar
alarmOverTemperatureCritical=_AlarmOverTemperatureCritical_Object((1,3,6,1,4,1,2634,1,280,4),_AlarmOverTemperatureCritical_Type())
alarmOverTemperatureCritical.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmOverTemperatureCritical.setStatus(_A)
_AlarmCircuitBreakerOpen_Type=Integer32
_AlarmCircuitBreakerOpen_Object=MibScalar
alarmCircuitBreakerOpen=_AlarmCircuitBreakerOpen_Object((1,3,6,1,4,1,2634,1,280,5),_AlarmCircuitBreakerOpen_Type())
alarmCircuitBreakerOpen.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmCircuitBreakerOpen.setStatus(_A)
_AlarmCommLoss_Type=Integer32
_AlarmCommLoss_Object=MibScalar
alarmCommLoss=_AlarmCommLoss_Object((1,3,6,1,4,1,2634,1,280,6),_AlarmCommLoss_Type())
alarmCommLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmCommLoss.setStatus(_A)
_AlarmPingNoAnswer_Type=Integer32
_AlarmPingNoAnswer_Object=MibScalar
alarmPingNoAnswer=_AlarmPingNoAnswer_Object((1,3,6,1,4,1,2634,1,280,8),_AlarmPingNoAnswer_Type())
alarmPingNoAnswer.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmPingNoAnswer.setStatus(_A)
_AlarmInvalidAccessLockout_Type=Integer32
_AlarmInvalidAccessLockout_Object=MibScalar
alarmInvalidAccessLockout=_AlarmInvalidAccessLockout_Object((1,3,6,1,4,1,2634,1,280,9),_AlarmInvalidAccessLockout_Type())
alarmInvalidAccessLockout.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmInvalidAccessLockout.setStatus(_A)
_AlarmPowerCycle_Type=Integer32
_AlarmPowerCycle_Object=MibScalar
alarmPowerCycle=_AlarmPowerCycle_Object((1,3,6,1,4,1,2634,1,280,10),_AlarmPowerCycle_Type())
alarmPowerCycle.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmPowerCycle.setStatus(_A)
_AlarmBufferThreshold_Type=Integer32
_AlarmBufferThreshold_Object=MibScalar
alarmBufferThreshold=_AlarmBufferThreshold_Object((1,3,6,1,4,1,2634,1,280,11),_AlarmBufferThreshold_Type())
alarmBufferThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmBufferThreshold.setStatus(_A)
_AlarmPlugCurrent_Type=Integer32
_AlarmPlugCurrent_Object=MibScalar
alarmPlugCurrent=_AlarmPlugCurrent_Object((1,3,6,1,4,1,2634,1,280,13),_AlarmPlugCurrent_Type())
alarmPlugCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmPlugCurrent.setStatus(_A)
_AlarmLostOptoVoltage_Type=Integer32
_AlarmLostOptoVoltage_Object=MibScalar
alarmLostOptoVoltage=_AlarmLostOptoVoltage_Object((1,3,6,1,4,1,2634,1,280,14),_AlarmLostOptoVoltage_Type())
alarmLostOptoVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmLostOptoVoltage.setStatus(_A)
_AlarmEmergencyShutoff_Type=Integer32
_AlarmEmergencyShutoff_Object=MibScalar
alarmEmergencyShutoff=_AlarmEmergencyShutoff_Object((1,3,6,1,4,1,2634,1,280,15),_AlarmEmergencyShutoff_Type())
alarmEmergencyShutoff.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmEmergencyShutoff.setStatus(_A)
_AlarmNoDialtone_Type=Integer32
_AlarmNoDialtone_Object=MibScalar
alarmNoDialtone=_AlarmNoDialtone_Object((1,3,6,1,4,1,2634,1,280,16),_AlarmNoDialtone_Type())
alarmNoDialtone.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmNoDialtone.setStatus(_A)
_WtiTraps_ObjectIdentity=ObjectIdentity
wtiTraps=_WtiTraps_ObjectIdentity((1,3,6,1,4,1,2634,1,300))
_TrapInfo_Type=DisplayString
_TrapInfo_Object=MibScalar
trapInfo=_TrapInfo_Object((1,3,6,1,4,1,2634,1,300,1),_TrapInfo_Type())
trapInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:trapInfo.setStatus(_A)
_TestTraps_ObjectIdentity=ObjectIdentity
testTraps=_TestTraps_ObjectIdentity((1,3,6,1,4,1,2634,1,300,2))
_BufferThresholdTraps_ObjectIdentity=ObjectIdentity
bufferThresholdTraps=_BufferThresholdTraps_ObjectIdentity((1,3,6,1,4,1,2634,1,300,3))
_OverCurrentInitialTraps_ObjectIdentity=ObjectIdentity
overCurrentInitialTraps=_OverCurrentInitialTraps_ObjectIdentity((1,3,6,1,4,1,2634,1,300,4))
_OverCurrentCriticalTraps_ObjectIdentity=ObjectIdentity
overCurrentCriticalTraps=_OverCurrentCriticalTraps_ObjectIdentity((1,3,6,1,4,1,2634,1,300,5))
_OverTemperatureInitialTraps_ObjectIdentity=ObjectIdentity
overTemperatureInitialTraps=_OverTemperatureInitialTraps_ObjectIdentity((1,3,6,1,4,1,2634,1,300,6))
_OverTemperatureCriticalTraps_ObjectIdentity=ObjectIdentity
overTemperatureCriticalTraps=_OverTemperatureCriticalTraps_ObjectIdentity((1,3,6,1,4,1,2634,1,300,7))
_CircuitBreakerOpenTraps_ObjectIdentity=ObjectIdentity
circuitBreakerOpenTraps=_CircuitBreakerOpenTraps_ObjectIdentity((1,3,6,1,4,1,2634,1,300,8))
_LostCommTraps_ObjectIdentity=ObjectIdentity
lostCommTraps=_LostCommTraps_ObjectIdentity((1,3,6,1,4,1,2634,1,300,9))
_PingNoAnswerTraps_ObjectIdentity=ObjectIdentity
pingNoAnswerTraps=_PingNoAnswerTraps_ObjectIdentity((1,3,6,1,4,1,2634,1,300,11))
_LockoutTraps_ObjectIdentity=ObjectIdentity
lockoutTraps=_LockoutTraps_ObjectIdentity((1,3,6,1,4,1,2634,1,300,12))
_PowercycleTraps_ObjectIdentity=ObjectIdentity
powercycleTraps=_PowercycleTraps_ObjectIdentity((1,3,6,1,4,1,2634,1,300,13))
_PlugCurrentTraps_ObjectIdentity=ObjectIdentity
plugCurrentTraps=_PlugCurrentTraps_ObjectIdentity((1,3,6,1,4,1,2634,1,300,15))
_LostOptoVoltageTraps_ObjectIdentity=ObjectIdentity
lostOptoVoltageTraps=_LostOptoVoltageTraps_ObjectIdentity((1,3,6,1,4,1,2634,1,300,16))
_EmergencyShutoffTraps_ObjectIdentity=ObjectIdentity
emergencyShutoffTraps=_EmergencyShutoffTraps_ObjectIdentity((1,3,6,1,4,1,2634,1,300,17))
_NoDialtoneTraps_ObjectIdentity=ObjectIdentity
noDialtoneTraps=_NoDialtoneTraps_ObjectIdentity((1,3,6,1,4,1,2634,1,300,18))
testTrap=NotificationType((1,3,6,1,4,1,2634,1,300,2,0,1))
testTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:testTrap.setStatus('')
bufferThresholdCrossedSetTrap=NotificationType((1,3,6,1,4,1,2634,1,300,3,0,1))
bufferThresholdCrossedSetTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:bufferThresholdCrossedSetTrap.setStatus('')
bufferThresholdCrossedClearTrap=NotificationType((1,3,6,1,4,1,2634,1,300,3,0,2))
bufferThresholdCrossedClearTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:bufferThresholdCrossedClearTrap.setStatus('')
overCurrentInitialSetTrap=NotificationType((1,3,6,1,4,1,2634,1,300,4,0,1))
overCurrentInitialSetTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:overCurrentInitialSetTrap.setStatus('')
overCurrentInitialClearTrap=NotificationType((1,3,6,1,4,1,2634,1,300,4,0,2))
overCurrentInitialClearTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:overCurrentInitialClearTrap.setStatus('')
overCurrentCriticalSetTrap=NotificationType((1,3,6,1,4,1,2634,1,300,5,0,1))
overCurrentCriticalSetTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:overCurrentCriticalSetTrap.setStatus('')
overCurrentCriticalClearTrap=NotificationType((1,3,6,1,4,1,2634,1,300,5,0,2))
overCurrentCriticalClearTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:overCurrentCriticalClearTrap.setStatus('')
overTemperatureInitialSetTrap=NotificationType((1,3,6,1,4,1,2634,1,300,6,0,1))
overTemperatureInitialSetTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:overTemperatureInitialSetTrap.setStatus('')
overTemperatureInitialClearTrap=NotificationType((1,3,6,1,4,1,2634,1,300,6,0,2))
overTemperatureInitialClearTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:overTemperatureInitialClearTrap.setStatus('')
overTemperatureCriticalSetTrap=NotificationType((1,3,6,1,4,1,2634,1,300,7,0,1))
overTemperatureCriticalSetTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:overTemperatureCriticalSetTrap.setStatus('')
overTemperatureCriticalClearTrap=NotificationType((1,3,6,1,4,1,2634,1,300,7,0,2))
overTemperatureCriticalClearTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:overTemperatureCriticalClearTrap.setStatus('')
circuitBreakerOpenSetTrap=NotificationType((1,3,6,1,4,1,2634,1,300,8,0,1))
circuitBreakerOpenSetTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:circuitBreakerOpenSetTrap.setStatus('')
circuitBreakerOpenClearTrap=NotificationType((1,3,6,1,4,1,2634,1,300,8,0,2))
circuitBreakerOpenClearTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:circuitBreakerOpenClearTrap.setStatus('')
lostCommSetTrap=NotificationType((1,3,6,1,4,1,2634,1,300,9,0,1))
lostCommSetTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:lostCommSetTrap.setStatus('')
lostCommClearTrap=NotificationType((1,3,6,1,4,1,2634,1,300,9,0,2))
lostCommClearTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:lostCommClearTrap.setStatus('')
pingNoAnswerSetTrap=NotificationType((1,3,6,1,4,1,2634,1,300,11,0,1))
pingNoAnswerSetTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:pingNoAnswerSetTrap.setStatus('')
pingNoAnswerClearTrap=NotificationType((1,3,6,1,4,1,2634,1,300,11,0,2))
pingNoAnswerClearTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:pingNoAnswerClearTrap.setStatus('')
lockoutSetTrap=NotificationType((1,3,6,1,4,1,2634,1,300,12,0,1))
lockoutSetTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:lockoutSetTrap.setStatus('')
lockoutClearTrap=NotificationType((1,3,6,1,4,1,2634,1,300,12,0,2))
lockoutClearTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:lockoutClearTrap.setStatus('')
powercycleSetTrap=NotificationType((1,3,6,1,4,1,2634,1,300,13,0,1))
powercycleSetTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:powercycleSetTrap.setStatus('')
plugCurrentSetTrap=NotificationType((1,3,6,1,4,1,2634,1,300,15,0,1))
plugCurrentSetTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:plugCurrentSetTrap.setStatus('')
plugCurrentClearTrap=NotificationType((1,3,6,1,4,1,2634,1,300,15,0,2))
plugCurrentClearTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:plugCurrentClearTrap.setStatus('')
lostOptoVoltageSetTrap=NotificationType((1,3,6,1,4,1,2634,1,300,16,0,1))
lostOptoVoltageSetTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:lostOptoVoltageSetTrap.setStatus('')
lostOptoVoltageClearTrap=NotificationType((1,3,6,1,4,1,2634,1,300,16,0,2))
lostOptoVoltageClearTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:lostOptoVoltageClearTrap.setStatus('')
emergencyShutoffSetTrap=NotificationType((1,3,6,1,4,1,2634,1,300,17,0,1))
emergencyShutoffSetTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:emergencyShutoffSetTrap.setStatus('')
emergencyShutoffClearTrap=NotificationType((1,3,6,1,4,1,2634,1,300,17,0,2))
emergencyShutoffClearTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:emergencyShutoffClearTrap.setStatus('')
noDialtoneSetTrap=NotificationType((1,3,6,1,4,1,2634,1,300,18,0,1))
noDialtoneSetTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:noDialtoneSetTrap.setStatus('')
noDialtoneClearTrap=NotificationType((1,3,6,1,4,1,2634,1,300,18,0,2))
noDialtoneClearTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:noDialtoneClearTrap.setStatus('')
mibBuilder.exportSymbols(_B,**{'westernTelematic':westernTelematic,'rsm-tsm':rsm_tsm,'systemTables':systemTables,'portTable':portTable,'portEntry':portEntry,_I:portIndex,'portID':portID,'portName':portName,'portBufferThreshold':portBufferThreshold,'portUserName':portUserName,'portStatus':portStatus,'portBufferCt':portBufferCt,'plugTable':plugTable,'plugEntry':plugEntry,_J:plugIndex,'plugID':plugID,'plugStatus':plugStatus,'plugAction':plugAction,'plugName':plugName,'plugCurrent':plugCurrent,'plugPower':plugPower,'plugGroupTable':plugGroupTable,'plugGroupEntry':plugGroupEntry,_K:plugGroupIndex,'plugGroupName':plugGroupName,'plugGroupAction':plugGroupAction,'plugGroupCurrent':plugGroupCurrent,'plugGroupPower':plugGroupPower,'userTable':userTable,'userEntry':userEntry,_L:userIndex,'userName':userName,'userPasswd':userPasswd,'userAccessLevel':userAccessLevel,'userPortAccess':userPortAccess,'userPlugAccess':userPlugAccess,'userGroupAccess':userGroupAccess,'userSerialAccess':userSerialAccess,'userTelnetSshAccess':userTelnetSshAccess,'userWebAccess':userWebAccess,'userOutboundTelAccess':userOutboundTelAccess,'userCallbackNum':userCallbackNum,'userSubmit':userSubmit,'environmentTables':environmentTables,'environmentUnitTable':environmentUnitTable,'environmentUnitEntry':environmentUnitEntry,_M:environmentUnitIndex,'environmentUnitName':environmentUnitName,'environmentUnitTemperature':environmentUnitTemperature,'environmentSysRAM':environmentSysRAM,'environmentSysFlash':environmentSysFlash,'environmentMacEth0':environmentMacEth0,'environmentMacEth1':environmentMacEth1,'alarmTables':alarmTables,'alarmOverCurrentInitial':alarmOverCurrentInitial,'alarmOverCurrentCritical':alarmOverCurrentCritical,'alarmOverTemperatureInitial':alarmOverTemperatureInitial,'alarmOverTemperatureCritical':alarmOverTemperatureCritical,'alarmCircuitBreakerOpen':alarmCircuitBreakerOpen,'alarmCommLoss':alarmCommLoss,'alarmPingNoAnswer':alarmPingNoAnswer,'alarmInvalidAccessLockout':alarmInvalidAccessLockout,'alarmPowerCycle':alarmPowerCycle,'alarmBufferThreshold':alarmBufferThreshold,'alarmPlugCurrent':alarmPlugCurrent,'alarmLostOptoVoltage':alarmLostOptoVoltage,'alarmEmergencyShutoff':alarmEmergencyShutoff,'alarmNoDialtone':alarmNoDialtone,'wtiTraps':wtiTraps,_D:trapInfo,'testTraps':testTraps,'testTrap':testTrap,'bufferThresholdTraps':bufferThresholdTraps,'bufferThresholdCrossedSetTrap':bufferThresholdCrossedSetTrap,'bufferThresholdCrossedClearTrap':bufferThresholdCrossedClearTrap,'overCurrentInitialTraps':overCurrentInitialTraps,'overCurrentInitialSetTrap':overCurrentInitialSetTrap,'overCurrentInitialClearTrap':overCurrentInitialClearTrap,'overCurrentCriticalTraps':overCurrentCriticalTraps,'overCurrentCriticalSetTrap':overCurrentCriticalSetTrap,'overCurrentCriticalClearTrap':overCurrentCriticalClearTrap,'overTemperatureInitialTraps':overTemperatureInitialTraps,'overTemperatureInitialSetTrap':overTemperatureInitialSetTrap,'overTemperatureInitialClearTrap':overTemperatureInitialClearTrap,'overTemperatureCriticalTraps':overTemperatureCriticalTraps,'overTemperatureCriticalSetTrap':overTemperatureCriticalSetTrap,'overTemperatureCriticalClearTrap':overTemperatureCriticalClearTrap,'circuitBreakerOpenTraps':circuitBreakerOpenTraps,'circuitBreakerOpenSetTrap':circuitBreakerOpenSetTrap,'circuitBreakerOpenClearTrap':circuitBreakerOpenClearTrap,'lostCommTraps':lostCommTraps,'lostCommSetTrap':lostCommSetTrap,'lostCommClearTrap':lostCommClearTrap,'pingNoAnswerTraps':pingNoAnswerTraps,'pingNoAnswerSetTrap':pingNoAnswerSetTrap,'pingNoAnswerClearTrap':pingNoAnswerClearTrap,'lockoutTraps':lockoutTraps,'lockoutSetTrap':lockoutSetTrap,'lockoutClearTrap':lockoutClearTrap,'powercycleTraps':powercycleTraps,'powercycleSetTrap':powercycleSetTrap,'plugCurrentTraps':plugCurrentTraps,'plugCurrentSetTrap':plugCurrentSetTrap,'plugCurrentClearTrap':plugCurrentClearTrap,'lostOptoVoltageTraps':lostOptoVoltageTraps,'lostOptoVoltageSetTrap':lostOptoVoltageSetTrap,'lostOptoVoltageClearTrap':lostOptoVoltageClearTrap,'emergencyShutoffTraps':emergencyShutoffTraps,'emergencyShutoffSetTrap':emergencyShutoffSetTrap,'emergencyShutoffClearTrap':emergencyShutoffClearTrap,'noDialtoneTraps':noDialtoneTraps,'noDialtoneSetTrap':noDialtoneSetTrap,'noDialtoneClearTrap':noDialtoneClearTrap})