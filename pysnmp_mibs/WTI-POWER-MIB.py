_L='environmentUnitIndex'
_K='userIndex'
_J='plugGroupIndex'
_I='plugIndex'
_H='not-accessible'
_G='DisplayString'
_F='Integer32'
_E='read-write'
_D='trapInfo'
_C='WTI-POWER-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
power=ModuleIdentity((1,3,6,1,4,1,2634,3))
if mibBuilder.loadTexts:power.setRevisions(('2019-01-29 16:00',))
_WesternTelematic_ObjectIdentity=ObjectIdentity
westernTelematic=_WesternTelematic_ObjectIdentity((1,3,6,1,4,1,2634))
_SystemTables_ObjectIdentity=ObjectIdentity
systemTables=_SystemTables_ObjectIdentity((1,3,6,1,4,1,2634,3,100))
_PlugTable_Object=MibTable
plugTable=_PlugTable_Object((1,3,6,1,4,1,2634,3,100,200))
if mibBuilder.loadTexts:plugTable.setStatus(_A)
_PlugEntry_Object=MibTableRow
plugEntry=_PlugEntry_Object((1,3,6,1,4,1,2634,3,100,200,1))
plugEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:plugEntry.setStatus(_A)
class _PlugIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,80))
_PlugIndex_Type.__name__=_F
_PlugIndex_Object=MibTableColumn
plugIndex=_PlugIndex_Object((1,3,6,1,4,1,2634,3,100,200,1,1),_PlugIndex_Type())
plugIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:plugIndex.setStatus(_A)
class _PlugID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(9,11))
_PlugID_Type.__name__=_G
_PlugID_Object=MibTableColumn
plugID=_PlugID_Object((1,3,6,1,4,1,2634,3,100,200,1,2),_PlugID_Type())
plugID.setMaxAccess(_B)
if mibBuilder.loadTexts:plugID.setStatus(_A)
class _PlugStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_PlugStatus_Type.__name__=_F
_PlugStatus_Object=MibTableColumn
plugStatus=_PlugStatus_Object((1,3,6,1,4,1,2634,3,100,200,1,3),_PlugStatus_Type())
plugStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:plugStatus.setStatus(_A)
class _PlugAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_PlugAction_Type.__name__=_F
_PlugAction_Object=MibTableColumn
plugAction=_PlugAction_Object((1,3,6,1,4,1,2634,3,100,200,1,4),_PlugAction_Type())
plugAction.setMaxAccess(_E)
if mibBuilder.loadTexts:plugAction.setStatus(_A)
_PlugName_Type=DisplayString
_PlugName_Object=MibTableColumn
plugName=_PlugName_Object((1,3,6,1,4,1,2634,3,100,200,1,5),_PlugName_Type())
plugName.setMaxAccess(_B)
if mibBuilder.loadTexts:plugName.setStatus(_A)
_PlugCurrent_Type=Integer32
_PlugCurrent_Object=MibTableColumn
plugCurrent=_PlugCurrent_Object((1,3,6,1,4,1,2634,3,100,200,1,7),_PlugCurrent_Type())
plugCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:plugCurrent.setStatus(_A)
_PlugPower_Type=Integer32
_PlugPower_Object=MibTableColumn
plugPower=_PlugPower_Object((1,3,6,1,4,1,2634,3,100,200,1,8),_PlugPower_Type())
plugPower.setMaxAccess(_B)
if mibBuilder.loadTexts:plugPower.setStatus(_A)
_PlugGroupTable_Object=MibTable
plugGroupTable=_PlugGroupTable_Object((1,3,6,1,4,1,2634,3,100,300))
if mibBuilder.loadTexts:plugGroupTable.setStatus(_A)
_PlugGroupEntry_Object=MibTableRow
plugGroupEntry=_PlugGroupEntry_Object((1,3,6,1,4,1,2634,3,100,300,1))
plugGroupEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:plugGroupEntry.setStatus(_A)
class _PlugGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,54))
_PlugGroupIndex_Type.__name__=_F
_PlugGroupIndex_Object=MibTableColumn
plugGroupIndex=_PlugGroupIndex_Object((1,3,6,1,4,1,2634,3,100,300,1,1),_PlugGroupIndex_Type())
plugGroupIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:plugGroupIndex.setStatus(_A)
class _PlugGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_PlugGroupName_Type.__name__=_G
_PlugGroupName_Object=MibTableColumn
plugGroupName=_PlugGroupName_Object((1,3,6,1,4,1,2634,3,100,300,1,2),_PlugGroupName_Type())
plugGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:plugGroupName.setStatus(_A)
class _PlugGroupAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_PlugGroupAction_Type.__name__=_F
_PlugGroupAction_Object=MibTableColumn
plugGroupAction=_PlugGroupAction_Object((1,3,6,1,4,1,2634,3,100,300,1,3),_PlugGroupAction_Type())
plugGroupAction.setMaxAccess(_E)
if mibBuilder.loadTexts:plugGroupAction.setStatus(_A)
_PlugGroupCurrent_Type=Integer32
_PlugGroupCurrent_Object=MibTableColumn
plugGroupCurrent=_PlugGroupCurrent_Object((1,3,6,1,4,1,2634,3,100,300,1,4),_PlugGroupCurrent_Type())
plugGroupCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:plugGroupCurrent.setStatus(_A)
_PlugGroupPower_Type=Integer32
_PlugGroupPower_Object=MibTableColumn
plugGroupPower=_PlugGroupPower_Object((1,3,6,1,4,1,2634,3,100,300,1,5),_PlugGroupPower_Type())
plugGroupPower.setMaxAccess(_B)
if mibBuilder.loadTexts:plugGroupPower.setStatus(_A)
_UserTable_Object=MibTable
userTable=_UserTable_Object((1,3,6,1,4,1,2634,3,100,400))
if mibBuilder.loadTexts:userTable.setStatus(_A)
_UserEntry_Object=MibTableRow
userEntry=_UserEntry_Object((1,3,6,1,4,1,2634,3,100,400,1))
userEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:userEntry.setStatus(_A)
class _UserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_UserIndex_Type.__name__=_F
_UserIndex_Object=MibTableColumn
userIndex=_UserIndex_Object((1,3,6,1,4,1,2634,3,100,400,1,1),_UserIndex_Type())
userIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:userIndex.setStatus(_A)
class _UserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UserName_Type.__name__=_G
_UserName_Object=MibTableColumn
userName=_UserName_Object((1,3,6,1,4,1,2634,3,100,400,1,2),_UserName_Type())
userName.setMaxAccess(_E)
if mibBuilder.loadTexts:userName.setStatus(_A)
class _UserPasswd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_UserPasswd_Type.__name__=_G
_UserPasswd_Object=MibTableColumn
userPasswd=_UserPasswd_Object((1,3,6,1,4,1,2634,3,100,400,1,3),_UserPasswd_Type())
userPasswd.setMaxAccess(_E)
if mibBuilder.loadTexts:userPasswd.setStatus(_A)
class _UserAccessLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_UserAccessLevel_Type.__name__=_F
_UserAccessLevel_Object=MibTableColumn
userAccessLevel=_UserAccessLevel_Object((1,3,6,1,4,1,2634,3,100,400,1,4),_UserAccessLevel_Type())
userAccessLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:userAccessLevel.setStatus(_A)
class _UserPortAccess_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,5))
_UserPortAccess_Type.__name__=_G
_UserPortAccess_Object=MibTableColumn
userPortAccess=_UserPortAccess_Object((1,3,6,1,4,1,2634,3,100,400,1,5),_UserPortAccess_Type())
userPortAccess.setMaxAccess(_E)
if mibBuilder.loadTexts:userPortAccess.setStatus(_A)
class _UserLocalAccess_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_UserLocalAccess_Type.__name__=_G
_UserLocalAccess_Object=MibTableColumn
userLocalAccess=_UserLocalAccess_Object((1,3,6,1,4,1,2634,3,100,400,1,6),_UserLocalAccess_Type())
userLocalAccess.setMaxAccess(_E)
if mibBuilder.loadTexts:userLocalAccess.setStatus(_A)
class _UserGroupAccess_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,54))
_UserGroupAccess_Type.__name__=_G
_UserGroupAccess_Object=MibTableColumn
userGroupAccess=_UserGroupAccess_Object((1,3,6,1,4,1,2634,3,100,400,1,10),_UserGroupAccess_Type())
userGroupAccess.setMaxAccess(_E)
if mibBuilder.loadTexts:userGroupAccess.setStatus(_A)
class _UserSerialAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_UserSerialAccess_Type.__name__=_F
_UserSerialAccess_Object=MibTableColumn
userSerialAccess=_UserSerialAccess_Object((1,3,6,1,4,1,2634,3,100,400,1,11),_UserSerialAccess_Type())
userSerialAccess.setMaxAccess(_E)
if mibBuilder.loadTexts:userSerialAccess.setStatus(_A)
class _UserTelnetSshAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_UserTelnetSshAccess_Type.__name__=_F
_UserTelnetSshAccess_Object=MibTableColumn
userTelnetSshAccess=_UserTelnetSshAccess_Object((1,3,6,1,4,1,2634,3,100,400,1,12),_UserTelnetSshAccess_Type())
userTelnetSshAccess.setMaxAccess(_E)
if mibBuilder.loadTexts:userTelnetSshAccess.setStatus(_A)
class _UserWebAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_UserWebAccess_Type.__name__=_F
_UserWebAccess_Object=MibTableColumn
userWebAccess=_UserWebAccess_Object((1,3,6,1,4,1,2634,3,100,400,1,13),_UserWebAccess_Type())
userWebAccess.setMaxAccess(_E)
if mibBuilder.loadTexts:userWebAccess.setStatus(_A)
class _UserCurrentPowerMetering_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_UserCurrentPowerMetering_Type.__name__=_F
_UserCurrentPowerMetering_Object=MibTableColumn
userCurrentPowerMetering=_UserCurrentPowerMetering_Object((1,3,6,1,4,1,2634,3,100,400,1,15),_UserCurrentPowerMetering_Type())
userCurrentPowerMetering.setMaxAccess(_E)
if mibBuilder.loadTexts:userCurrentPowerMetering.setStatus(_A)
class _UserCallbackNum1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UserCallbackNum1_Type.__name__=_G
_UserCallbackNum1_Object=MibTableColumn
userCallbackNum1=_UserCallbackNum1_Object((1,3,6,1,4,1,2634,3,100,400,1,16),_UserCallbackNum1_Type())
userCallbackNum1.setMaxAccess(_E)
if mibBuilder.loadTexts:userCallbackNum1.setStatus(_A)
class _UserCallbackNum2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UserCallbackNum2_Type.__name__=_G
_UserCallbackNum2_Object=MibTableColumn
userCallbackNum2=_UserCallbackNum2_Object((1,3,6,1,4,1,2634,3,100,400,1,17),_UserCallbackNum2_Type())
userCallbackNum2.setMaxAccess(_E)
if mibBuilder.loadTexts:userCallbackNum2.setStatus(_A)
class _UserCallbackNum3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UserCallbackNum3_Type.__name__=_G
_UserCallbackNum3_Object=MibTableColumn
userCallbackNum3=_UserCallbackNum3_Object((1,3,6,1,4,1,2634,3,100,400,1,18),_UserCallbackNum3_Type())
userCallbackNum3.setMaxAccess(_E)
if mibBuilder.loadTexts:userCallbackNum3.setStatus(_A)
class _UserCallbackNum4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UserCallbackNum4_Type.__name__=_G
_UserCallbackNum4_Object=MibTableColumn
userCallbackNum4=_UserCallbackNum4_Object((1,3,6,1,4,1,2634,3,100,400,1,19),_UserCallbackNum4_Type())
userCallbackNum4.setMaxAccess(_E)
if mibBuilder.loadTexts:userCallbackNum4.setStatus(_A)
class _UserCallbackNum5_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UserCallbackNum5_Type.__name__=_G
_UserCallbackNum5_Object=MibTableColumn
userCallbackNum5=_UserCallbackNum5_Object((1,3,6,1,4,1,2634,3,100,400,1,20),_UserCallbackNum5_Type())
userCallbackNum5.setMaxAccess(_E)
if mibBuilder.loadTexts:userCallbackNum5.setStatus(_A)
class _UserSubmit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_UserSubmit_Type.__name__=_F
_UserSubmit_Object=MibTableColumn
userSubmit=_UserSubmit_Object((1,3,6,1,4,1,2634,3,100,400,1,31),_UserSubmit_Type())
userSubmit.setMaxAccess(_E)
if mibBuilder.loadTexts:userSubmit.setStatus(_A)
_EnvironmentTables_ObjectIdentity=ObjectIdentity
environmentTables=_EnvironmentTables_ObjectIdentity((1,3,6,1,4,1,2634,3,200))
_EnvironmentUnitTable_Object=MibTable
environmentUnitTable=_EnvironmentUnitTable_Object((1,3,6,1,4,1,2634,3,200,10))
if mibBuilder.loadTexts:environmentUnitTable.setStatus(_A)
_EnvironmentUnitEntry_Object=MibTableRow
environmentUnitEntry=_EnvironmentUnitEntry_Object((1,3,6,1,4,1,2634,3,200,10,1))
environmentUnitEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:environmentUnitEntry.setStatus(_A)
class _EnvironmentUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_EnvironmentUnitIndex_Type.__name__=_F
_EnvironmentUnitIndex_Object=MibTableColumn
environmentUnitIndex=_EnvironmentUnitIndex_Object((1,3,6,1,4,1,2634,3,200,10,1,1),_EnvironmentUnitIndex_Type())
environmentUnitIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:environmentUnitIndex.setStatus(_A)
_EnvironmentUnitName_Type=DisplayString
_EnvironmentUnitName_Object=MibTableColumn
environmentUnitName=_EnvironmentUnitName_Object((1,3,6,1,4,1,2634,3,200,10,1,2),_EnvironmentUnitName_Type())
environmentUnitName.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentUnitName.setStatus(_A)
_EnvironmentUnitTemperature_Type=Integer32
_EnvironmentUnitTemperature_Object=MibTableColumn
environmentUnitTemperature=_EnvironmentUnitTemperature_Object((1,3,6,1,4,1,2634,3,200,10,1,3),_EnvironmentUnitTemperature_Type())
environmentUnitTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentUnitTemperature.setStatus(_A)
_EnvironmentUnitCurrentA_Type=Integer32
_EnvironmentUnitCurrentA_Object=MibTableColumn
environmentUnitCurrentA=_EnvironmentUnitCurrentA_Object((1,3,6,1,4,1,2634,3,200,10,1,4),_EnvironmentUnitCurrentA_Type())
environmentUnitCurrentA.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentUnitCurrentA.setStatus(_A)
_EnvironmentUnitVoltageA_Type=Integer32
_EnvironmentUnitVoltageA_Object=MibTableColumn
environmentUnitVoltageA=_EnvironmentUnitVoltageA_Object((1,3,6,1,4,1,2634,3,200,10,1,5),_EnvironmentUnitVoltageA_Type())
environmentUnitVoltageA.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentUnitVoltageA.setStatus(_A)
_EnvironmentUnitPowerA_Type=Integer32
_EnvironmentUnitPowerA_Object=MibTableColumn
environmentUnitPowerA=_EnvironmentUnitPowerA_Object((1,3,6,1,4,1,2634,3,200,10,1,6),_EnvironmentUnitPowerA_Type())
environmentUnitPowerA.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentUnitPowerA.setStatus(_A)
_EnvironmentUnitCurrentB_Type=Integer32
_EnvironmentUnitCurrentB_Object=MibTableColumn
environmentUnitCurrentB=_EnvironmentUnitCurrentB_Object((1,3,6,1,4,1,2634,3,200,10,1,7),_EnvironmentUnitCurrentB_Type())
environmentUnitCurrentB.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentUnitCurrentB.setStatus(_A)
_EnvironmentUnitVoltageB_Type=Integer32
_EnvironmentUnitVoltageB_Object=MibTableColumn
environmentUnitVoltageB=_EnvironmentUnitVoltageB_Object((1,3,6,1,4,1,2634,3,200,10,1,8),_EnvironmentUnitVoltageB_Type())
environmentUnitVoltageB.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentUnitVoltageB.setStatus(_A)
_EnvironmentUnitPowerB_Type=Integer32
_EnvironmentUnitPowerB_Object=MibTableColumn
environmentUnitPowerB=_EnvironmentUnitPowerB_Object((1,3,6,1,4,1,2634,3,200,10,1,9),_EnvironmentUnitPowerB_Type())
environmentUnitPowerB.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentUnitPowerB.setStatus(_A)
_EnvironmentUnitCurrentC_Type=Integer32
_EnvironmentUnitCurrentC_Object=MibTableColumn
environmentUnitCurrentC=_EnvironmentUnitCurrentC_Object((1,3,6,1,4,1,2634,3,200,10,1,10),_EnvironmentUnitCurrentC_Type())
environmentUnitCurrentC.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentUnitCurrentC.setStatus(_A)
_EnvironmentUnitVoltageC_Type=Integer32
_EnvironmentUnitVoltageC_Object=MibTableColumn
environmentUnitVoltageC=_EnvironmentUnitVoltageC_Object((1,3,6,1,4,1,2634,3,200,10,1,11),_EnvironmentUnitVoltageC_Type())
environmentUnitVoltageC.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentUnitVoltageC.setStatus(_A)
_EnvironmentUnitPowerC_Type=Integer32
_EnvironmentUnitPowerC_Object=MibTableColumn
environmentUnitPowerC=_EnvironmentUnitPowerC_Object((1,3,6,1,4,1,2634,3,200,10,1,12),_EnvironmentUnitPowerC_Type())
environmentUnitPowerC.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentUnitPowerC.setStatus(_A)
_EnvironmentUnitCurrentD_Type=Integer32
_EnvironmentUnitCurrentD_Object=MibTableColumn
environmentUnitCurrentD=_EnvironmentUnitCurrentD_Object((1,3,6,1,4,1,2634,3,200,10,1,13),_EnvironmentUnitCurrentD_Type())
environmentUnitCurrentD.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentUnitCurrentD.setStatus(_A)
_EnvironmentUnitVoltageD_Type=Integer32
_EnvironmentUnitVoltageD_Object=MibTableColumn
environmentUnitVoltageD=_EnvironmentUnitVoltageD_Object((1,3,6,1,4,1,2634,3,200,10,1,14),_EnvironmentUnitVoltageD_Type())
environmentUnitVoltageD.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentUnitVoltageD.setStatus(_A)
_EnvironmentUnitPowerD_Type=Integer32
_EnvironmentUnitPowerD_Object=MibTableColumn
environmentUnitPowerD=_EnvironmentUnitPowerD_Object((1,3,6,1,4,1,2634,3,200,10,1,15),_EnvironmentUnitPowerD_Type())
environmentUnitPowerD.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentUnitPowerD.setStatus(_A)
_EnvironmentSysRAM_Type=Integer32
_EnvironmentSysRAM_Object=MibTableColumn
environmentSysRAM=_EnvironmentSysRAM_Object((1,3,6,1,4,1,2634,3,200,10,1,18),_EnvironmentSysRAM_Type())
environmentSysRAM.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentSysRAM.setStatus(_A)
_EnvironmentSysFlash_Type=Integer32
_EnvironmentSysFlash_Object=MibTableColumn
environmentSysFlash=_EnvironmentSysFlash_Object((1,3,6,1,4,1,2634,3,200,10,1,19),_EnvironmentSysFlash_Type())
environmentSysFlash.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentSysFlash.setStatus(_A)
_EnvironmentMacEth0_Type=DisplayString
_EnvironmentMacEth0_Object=MibTableColumn
environmentMacEth0=_EnvironmentMacEth0_Object((1,3,6,1,4,1,2634,3,200,10,1,20),_EnvironmentMacEth0_Type())
environmentMacEth0.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentMacEth0.setStatus(_A)
_EnvironmentMacEth1_Type=DisplayString
_EnvironmentMacEth1_Object=MibTableColumn
environmentMacEth1=_EnvironmentMacEth1_Object((1,3,6,1,4,1,2634,3,200,10,1,21),_EnvironmentMacEth1_Type())
environmentMacEth1.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentMacEth1.setStatus(_A)
_EnvironmentInputPower1_Type=Integer32
_EnvironmentInputPower1_Object=MibTableColumn
environmentInputPower1=_EnvironmentInputPower1_Object((1,3,6,1,4,1,2634,3,200,10,1,22),_EnvironmentInputPower1_Type())
environmentInputPower1.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentInputPower1.setStatus(_A)
_EnvironmentInputPower2_Type=Integer32
_EnvironmentInputPower2_Object=MibTableColumn
environmentInputPower2=_EnvironmentInputPower2_Object((1,3,6,1,4,1,2634,3,200,10,1,23),_EnvironmentInputPower2_Type())
environmentInputPower2.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentInputPower2.setStatus(_A)
_EnvironmentInputPower3_Type=Integer32
_EnvironmentInputPower3_Object=MibTableColumn
environmentInputPower3=_EnvironmentInputPower3_Object((1,3,6,1,4,1,2634,3,200,10,1,24),_EnvironmentInputPower3_Type())
environmentInputPower3.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentInputPower3.setStatus(_A)
_EnvironmentInputPower4_Type=Integer32
_EnvironmentInputPower4_Object=MibTableColumn
environmentInputPower4=_EnvironmentInputPower4_Object((1,3,6,1,4,1,2634,3,200,10,1,25),_EnvironmentInputPower4_Type())
environmentInputPower4.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentInputPower4.setStatus(_A)
_EnvironmentModemPhoneNumber_Type=DisplayString
_EnvironmentModemPhoneNumber_Object=MibTableColumn
environmentModemPhoneNumber=_EnvironmentModemPhoneNumber_Object((1,3,6,1,4,1,2634,3,200,10,1,26),_EnvironmentModemPhoneNumber_Type())
environmentModemPhoneNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentModemPhoneNumber.setStatus(_A)
_EnvironmentSerialNumber_Type=DisplayString
_EnvironmentSerialNumber_Object=MibTableColumn
environmentSerialNumber=_EnvironmentSerialNumber_Object((1,3,6,1,4,1,2634,3,200,10,1,27),_EnvironmentSerialNumber_Type())
environmentSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentSerialNumber.setStatus(_A)
_EnvironmentSoftwareVersion_Type=DisplayString
_EnvironmentSoftwareVersion_Object=MibTableColumn
environmentSoftwareVersion=_EnvironmentSoftwareVersion_Object((1,3,6,1,4,1,2634,3,200,10,1,28),_EnvironmentSoftwareVersion_Type())
environmentSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentSoftwareVersion.setStatus(_A)
_EnvironmentSystemTotalCurrent_Type=Integer32
_EnvironmentSystemTotalCurrent_Object=MibScalar
environmentSystemTotalCurrent=_EnvironmentSystemTotalCurrent_Object((1,3,6,1,4,1,2634,3,200,60),_EnvironmentSystemTotalCurrent_Type())
environmentSystemTotalCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentSystemTotalCurrent.setStatus(_A)
_EnvironmentSystemTotalPower_Type=Integer32
_EnvironmentSystemTotalPower_Object=MibScalar
environmentSystemTotalPower=_EnvironmentSystemTotalPower_Object((1,3,6,1,4,1,2634,3,200,70),_EnvironmentSystemTotalPower_Type())
environmentSystemTotalPower.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentSystemTotalPower.setStatus(_A)
_EnvironmentMonthlyPowerLog_Type=DisplayString
_EnvironmentMonthlyPowerLog_Object=MibScalar
environmentMonthlyPowerLog=_EnvironmentMonthlyPowerLog_Object((1,3,6,1,4,1,2634,3,200,80),_EnvironmentMonthlyPowerLog_Type())
environmentMonthlyPowerLog.setMaxAccess(_B)
if mibBuilder.loadTexts:environmentMonthlyPowerLog.setStatus(_A)
_AlarmTables_ObjectIdentity=ObjectIdentity
alarmTables=_AlarmTables_ObjectIdentity((1,3,6,1,4,1,2634,3,280))
_AlarmOverCurrentInitial_Type=Integer32
_AlarmOverCurrentInitial_Object=MibScalar
alarmOverCurrentInitial=_AlarmOverCurrentInitial_Object((1,3,6,1,4,1,2634,3,280,1),_AlarmOverCurrentInitial_Type())
alarmOverCurrentInitial.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmOverCurrentInitial.setStatus(_A)
_AlarmOverCurrentCritical_Type=Integer32
_AlarmOverCurrentCritical_Object=MibScalar
alarmOverCurrentCritical=_AlarmOverCurrentCritical_Object((1,3,6,1,4,1,2634,3,280,2),_AlarmOverCurrentCritical_Type())
alarmOverCurrentCritical.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmOverCurrentCritical.setStatus(_A)
_AlarmOverTemperatureInitial_Type=Integer32
_AlarmOverTemperatureInitial_Object=MibScalar
alarmOverTemperatureInitial=_AlarmOverTemperatureInitial_Object((1,3,6,1,4,1,2634,3,280,3),_AlarmOverTemperatureInitial_Type())
alarmOverTemperatureInitial.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmOverTemperatureInitial.setStatus(_A)
_AlarmOverTemperatureCritical_Type=Integer32
_AlarmOverTemperatureCritical_Object=MibScalar
alarmOverTemperatureCritical=_AlarmOverTemperatureCritical_Object((1,3,6,1,4,1,2634,3,280,4),_AlarmOverTemperatureCritical_Type())
alarmOverTemperatureCritical.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmOverTemperatureCritical.setStatus(_A)
_AlarmCircuitBreakerOpen_Type=Integer32
_AlarmCircuitBreakerOpen_Object=MibScalar
alarmCircuitBreakerOpen=_AlarmCircuitBreakerOpen_Object((1,3,6,1,4,1,2634,3,280,5),_AlarmCircuitBreakerOpen_Type())
alarmCircuitBreakerOpen.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmCircuitBreakerOpen.setStatus(_A)
_AlarmCommLoss_Type=Integer32
_AlarmCommLoss_Object=MibScalar
alarmCommLoss=_AlarmCommLoss_Object((1,3,6,1,4,1,2634,3,280,6),_AlarmCommLoss_Type())
alarmCommLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmCommLoss.setStatus(_A)
_AlarmLostVoltage_Type=Integer32
_AlarmLostVoltage_Object=MibScalar
alarmLostVoltage=_AlarmLostVoltage_Object((1,3,6,1,4,1,2634,3,280,7),_AlarmLostVoltage_Type())
alarmLostVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmLostVoltage.setStatus(_A)
_AlarmPingNoAnswer_Type=Integer32
_AlarmPingNoAnswer_Object=MibScalar
alarmPingNoAnswer=_AlarmPingNoAnswer_Object((1,3,6,1,4,1,2634,3,280,8),_AlarmPingNoAnswer_Type())
alarmPingNoAnswer.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmPingNoAnswer.setStatus(_A)
_AlarmInvalidAccessLockout_Type=Integer32
_AlarmInvalidAccessLockout_Object=MibScalar
alarmInvalidAccessLockout=_AlarmInvalidAccessLockout_Object((1,3,6,1,4,1,2634,3,280,9),_AlarmInvalidAccessLockout_Type())
alarmInvalidAccessLockout.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmInvalidAccessLockout.setStatus(_A)
_AlarmPowerCycle_Type=Integer32
_AlarmPowerCycle_Object=MibScalar
alarmPowerCycle=_AlarmPowerCycle_Object((1,3,6,1,4,1,2634,3,280,10),_AlarmPowerCycle_Type())
alarmPowerCycle.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmPowerCycle.setStatus(_A)
_AlarmAlarmInput_Type=Integer32
_AlarmAlarmInput_Object=MibScalar
alarmAlarmInput=_AlarmAlarmInput_Object((1,3,6,1,4,1,2634,3,280,12),_AlarmAlarmInput_Type())
alarmAlarmInput.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmAlarmInput.setStatus(_A)
_AlarmPlugCurrent_Type=Integer32
_AlarmPlugCurrent_Object=MibScalar
alarmPlugCurrent=_AlarmPlugCurrent_Object((1,3,6,1,4,1,2634,3,280,13),_AlarmPlugCurrent_Type())
alarmPlugCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmPlugCurrent.setStatus(_A)
_AlarmLostOptoVoltage_Type=Integer32
_AlarmLostOptoVoltage_Object=MibScalar
alarmLostOptoVoltage=_AlarmLostOptoVoltage_Object((1,3,6,1,4,1,2634,3,280,14),_AlarmLostOptoVoltage_Type())
alarmLostOptoVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmLostOptoVoltage.setStatus(_A)
_AlarmEmergencyShutoff_Type=Integer32
_AlarmEmergencyShutoff_Object=MibScalar
alarmEmergencyShutoff=_AlarmEmergencyShutoff_Object((1,3,6,1,4,1,2634,3,280,15),_AlarmEmergencyShutoff_Type())
alarmEmergencyShutoff.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmEmergencyShutoff.setStatus(_A)
_AlarmNoDialtone_Type=Integer32
_AlarmNoDialtone_Object=MibScalar
alarmNoDialtone=_AlarmNoDialtone_Object((1,3,6,1,4,1,2634,3,280,16),_AlarmNoDialtone_Type())
alarmNoDialtone.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmNoDialtone.setStatus(_A)
_AlarmWakeupOnFailure_Type=Integer32
_AlarmWakeupOnFailure_Object=MibScalar
alarmWakeupOnFailure=_AlarmWakeupOnFailure_Object((1,3,6,1,4,1,2634,3,280,17),_AlarmWakeupOnFailure_Type())
alarmWakeupOnFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmWakeupOnFailure.setStatus(_A)
_AlarmIpPassthroughDataUsage_Type=Integer32
_AlarmIpPassthroughDataUsage_Object=MibScalar
alarmIpPassthroughDataUsage=_AlarmIpPassthroughDataUsage_Object((1,3,6,1,4,1,2634,3,280,18),_AlarmIpPassthroughDataUsage_Type())
alarmIpPassthroughDataUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmIpPassthroughDataUsage.setStatus(_A)
_AlarmBufferFiltering_Type=Integer32
_AlarmBufferFiltering_Object=MibScalar
alarmBufferFiltering=_AlarmBufferFiltering_Object((1,3,6,1,4,1,2634,3,280,19),_AlarmBufferFiltering_Type())
alarmBufferFiltering.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmBufferFiltering.setStatus(_A)
_WtiTraps_ObjectIdentity=ObjectIdentity
wtiTraps=_WtiTraps_ObjectIdentity((1,3,6,1,4,1,2634,3,300))
_TrapInfo_Type=DisplayString
_TrapInfo_Object=MibScalar
trapInfo=_TrapInfo_Object((1,3,6,1,4,1,2634,3,300,1),_TrapInfo_Type())
trapInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:trapInfo.setStatus(_A)
_TestTraps_ObjectIdentity=ObjectIdentity
testTraps=_TestTraps_ObjectIdentity((1,3,6,1,4,1,2634,3,300,2))
_OverCurrentInitialTraps_ObjectIdentity=ObjectIdentity
overCurrentInitialTraps=_OverCurrentInitialTraps_ObjectIdentity((1,3,6,1,4,1,2634,3,300,4))
_OverCurrentCriticalTraps_ObjectIdentity=ObjectIdentity
overCurrentCriticalTraps=_OverCurrentCriticalTraps_ObjectIdentity((1,3,6,1,4,1,2634,3,300,5))
_OverTemperatureInitialTraps_ObjectIdentity=ObjectIdentity
overTemperatureInitialTraps=_OverTemperatureInitialTraps_ObjectIdentity((1,3,6,1,4,1,2634,3,300,6))
_OverTemperatureCriticalTraps_ObjectIdentity=ObjectIdentity
overTemperatureCriticalTraps=_OverTemperatureCriticalTraps_ObjectIdentity((1,3,6,1,4,1,2634,3,300,7))
_CircuitBreakerOpenTraps_ObjectIdentity=ObjectIdentity
circuitBreakerOpenTraps=_CircuitBreakerOpenTraps_ObjectIdentity((1,3,6,1,4,1,2634,3,300,8))
_LostCommTraps_ObjectIdentity=ObjectIdentity
lostCommTraps=_LostCommTraps_ObjectIdentity((1,3,6,1,4,1,2634,3,300,9))
_LostVoltageTraps_ObjectIdentity=ObjectIdentity
lostVoltageTraps=_LostVoltageTraps_ObjectIdentity((1,3,6,1,4,1,2634,3,300,10))
_PingNoAnswerTraps_ObjectIdentity=ObjectIdentity
pingNoAnswerTraps=_PingNoAnswerTraps_ObjectIdentity((1,3,6,1,4,1,2634,3,300,11))
_LockoutTraps_ObjectIdentity=ObjectIdentity
lockoutTraps=_LockoutTraps_ObjectIdentity((1,3,6,1,4,1,2634,3,300,12))
_PowercycleTraps_ObjectIdentity=ObjectIdentity
powercycleTraps=_PowercycleTraps_ObjectIdentity((1,3,6,1,4,1,2634,3,300,13))
_AlarmInputTraps_ObjectIdentity=ObjectIdentity
alarmInputTraps=_AlarmInputTraps_ObjectIdentity((1,3,6,1,4,1,2634,3,300,14))
_PlugCurrentTraps_ObjectIdentity=ObjectIdentity
plugCurrentTraps=_PlugCurrentTraps_ObjectIdentity((1,3,6,1,4,1,2634,3,300,15))
_LostOptoVoltageTraps_ObjectIdentity=ObjectIdentity
lostOptoVoltageTraps=_LostOptoVoltageTraps_ObjectIdentity((1,3,6,1,4,1,2634,3,300,16))
_EmergencyShutoffTraps_ObjectIdentity=ObjectIdentity
emergencyShutoffTraps=_EmergencyShutoffTraps_ObjectIdentity((1,3,6,1,4,1,2634,3,300,17))
_NoDialtoneTraps_ObjectIdentity=ObjectIdentity
noDialtoneTraps=_NoDialtoneTraps_ObjectIdentity((1,3,6,1,4,1,2634,3,300,18))
_WakeupOnFailureTraps_ObjectIdentity=ObjectIdentity
wakeupOnFailureTraps=_WakeupOnFailureTraps_ObjectIdentity((1,3,6,1,4,1,2634,3,300,19))
_IpPassthroughDataUsageTraps_ObjectIdentity=ObjectIdentity
ipPassthroughDataUsageTraps=_IpPassthroughDataUsageTraps_ObjectIdentity((1,3,6,1,4,1,2634,3,300,20))
_BufferFilteringTraps_ObjectIdentity=ObjectIdentity
bufferFilteringTraps=_BufferFilteringTraps_ObjectIdentity((1,3,6,1,4,1,2634,3,300,21))
testTrap=NotificationType((1,3,6,1,4,1,2634,3,300,2,0,1))
testTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:testTrap.setStatus('')
overCurrentInitialSetTrap=NotificationType((1,3,6,1,4,1,2634,3,300,4,0,1))
overCurrentInitialSetTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:overCurrentInitialSetTrap.setStatus('')
overCurrentInitialClearTrap=NotificationType((1,3,6,1,4,1,2634,3,300,4,0,2))
overCurrentInitialClearTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:overCurrentInitialClearTrap.setStatus('')
overCurrentCriticalSetTrap=NotificationType((1,3,6,1,4,1,2634,3,300,5,0,1))
overCurrentCriticalSetTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:overCurrentCriticalSetTrap.setStatus('')
overCurrentCriticalClearTrap=NotificationType((1,3,6,1,4,1,2634,3,300,5,0,2))
overCurrentCriticalClearTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:overCurrentCriticalClearTrap.setStatus('')
overTemperatureInitialSetTrap=NotificationType((1,3,6,1,4,1,2634,3,300,6,0,1))
overTemperatureInitialSetTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:overTemperatureInitialSetTrap.setStatus('')
overTemperatureInitialClearTrap=NotificationType((1,3,6,1,4,1,2634,3,300,6,0,2))
overTemperatureInitialClearTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:overTemperatureInitialClearTrap.setStatus('')
overTemperatureCriticalSetTrap=NotificationType((1,3,6,1,4,1,2634,3,300,7,0,1))
overTemperatureCriticalSetTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:overTemperatureCriticalSetTrap.setStatus('')
overTemperatureCriticalClearTrap=NotificationType((1,3,6,1,4,1,2634,3,300,7,0,2))
overTemperatureCriticalClearTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:overTemperatureCriticalClearTrap.setStatus('')
circuitBreakerOpenSetTrap=NotificationType((1,3,6,1,4,1,2634,3,300,8,0,1))
circuitBreakerOpenSetTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:circuitBreakerOpenSetTrap.setStatus('')
circuitBreakerOpenClearTrap=NotificationType((1,3,6,1,4,1,2634,3,300,8,0,2))
circuitBreakerOpenClearTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:circuitBreakerOpenClearTrap.setStatus('')
lostCommSetTrap=NotificationType((1,3,6,1,4,1,2634,3,300,9,0,1))
lostCommSetTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:lostCommSetTrap.setStatus('')
lostCommClearTrap=NotificationType((1,3,6,1,4,1,2634,3,300,9,0,2))
lostCommClearTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:lostCommClearTrap.setStatus('')
lostVoltageSetTrap=NotificationType((1,3,6,1,4,1,2634,3,300,10,0,1))
lostVoltageSetTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:lostVoltageSetTrap.setStatus('')
lostVoltageClearTrap=NotificationType((1,3,6,1,4,1,2634,3,300,10,0,2))
lostVoltageClearTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:lostVoltageClearTrap.setStatus('')
pingNoAnswerSetTrap=NotificationType((1,3,6,1,4,1,2634,3,300,11,0,1))
pingNoAnswerSetTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:pingNoAnswerSetTrap.setStatus('')
pingNoAnswerClearTrap=NotificationType((1,3,6,1,4,1,2634,3,300,11,0,2))
pingNoAnswerClearTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:pingNoAnswerClearTrap.setStatus('')
lockoutSetTrap=NotificationType((1,3,6,1,4,1,2634,3,300,12,0,1))
lockoutSetTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:lockoutSetTrap.setStatus('')
lockoutClearTrap=NotificationType((1,3,6,1,4,1,2634,3,300,12,0,2))
lockoutClearTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:lockoutClearTrap.setStatus('')
powercycleSetTrap=NotificationType((1,3,6,1,4,1,2634,3,300,13,0,1))
powercycleSetTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:powercycleSetTrap.setStatus('')
alarmInputSetTrap=NotificationType((1,3,6,1,4,1,2634,3,300,14,0,1))
alarmInputSetTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:alarmInputSetTrap.setStatus('')
alarmInputClearTrap=NotificationType((1,3,6,1,4,1,2634,3,300,14,0,2))
alarmInputClearTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:alarmInputClearTrap.setStatus('')
plugCurrentSetTrap=NotificationType((1,3,6,1,4,1,2634,3,300,15,0,1))
plugCurrentSetTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:plugCurrentSetTrap.setStatus('')
plugCurrentClearTrap=NotificationType((1,3,6,1,4,1,2634,3,300,15,0,2))
plugCurrentClearTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:plugCurrentClearTrap.setStatus('')
lostOptoVoltageSetTrap=NotificationType((1,3,6,1,4,1,2634,3,300,16,0,1))
lostOptoVoltageSetTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:lostOptoVoltageSetTrap.setStatus('')
lostOptoVoltageClearTrap=NotificationType((1,3,6,1,4,1,2634,3,300,16,0,2))
lostOptoVoltageClearTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:lostOptoVoltageClearTrap.setStatus('')
emergencyShutoffSetTrap=NotificationType((1,3,6,1,4,1,2634,3,300,17,0,1))
emergencyShutoffSetTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:emergencyShutoffSetTrap.setStatus('')
emergencyShutoffClearTrap=NotificationType((1,3,6,1,4,1,2634,3,300,17,0,2))
emergencyShutoffClearTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:emergencyShutoffClearTrap.setStatus('')
noDialtoneSetTrap=NotificationType((1,3,6,1,4,1,2634,3,300,18,0,1))
noDialtoneSetTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:noDialtoneSetTrap.setStatus('')
noDialtoneClearTrap=NotificationType((1,3,6,1,4,1,2634,3,300,18,0,2))
noDialtoneClearTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:noDialtoneClearTrap.setStatus('')
wakeupOnFailureSetTrap=NotificationType((1,3,6,1,4,1,2634,3,300,19,0,1))
wakeupOnFailureSetTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:wakeupOnFailureSetTrap.setStatus('')
wakeupOnFailureClearTrap=NotificationType((1,3,6,1,4,1,2634,3,300,19,0,2))
wakeupOnFailureClearTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:wakeupOnFailureClearTrap.setStatus('')
ipPassthroughDataUsageSetTrap=NotificationType((1,3,6,1,4,1,2634,3,300,20,0,1))
ipPassthroughDataUsageSetTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:ipPassthroughDataUsageSetTrap.setStatus('')
ipPassthroughDataUsageClearTrap=NotificationType((1,3,6,1,4,1,2634,3,300,20,0,2))
ipPassthroughDataUsageClearTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:ipPassthroughDataUsageClearTrap.setStatus('')
bufferFilteringSetTrap=NotificationType((1,3,6,1,4,1,2634,3,300,21,0,1))
bufferFilteringSetTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:bufferFilteringSetTrap.setStatus('')
bufferFilteringClearTrap=NotificationType((1,3,6,1,4,1,2634,3,300,21,0,2))
bufferFilteringClearTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:bufferFilteringClearTrap.setStatus('')
mibBuilder.exportSymbols(_C,**{'westernTelematic':westernTelematic,'power':power,'systemTables':systemTables,'plugTable':plugTable,'plugEntry':plugEntry,_I:plugIndex,'plugID':plugID,'plugStatus':plugStatus,'plugAction':plugAction,'plugName':plugName,'plugCurrent':plugCurrent,'plugPower':plugPower,'plugGroupTable':plugGroupTable,'plugGroupEntry':plugGroupEntry,_J:plugGroupIndex,'plugGroupName':plugGroupName,'plugGroupAction':plugGroupAction,'plugGroupCurrent':plugGroupCurrent,'plugGroupPower':plugGroupPower,'userTable':userTable,'userEntry':userEntry,_K:userIndex,'userName':userName,'userPasswd':userPasswd,'userAccessLevel':userAccessLevel,'userPortAccess':userPortAccess,'userLocalAccess':userLocalAccess,'userGroupAccess':userGroupAccess,'userSerialAccess':userSerialAccess,'userTelnetSshAccess':userTelnetSshAccess,'userWebAccess':userWebAccess,'userCurrentPowerMetering':userCurrentPowerMetering,'userCallbackNum1':userCallbackNum1,'userCallbackNum2':userCallbackNum2,'userCallbackNum3':userCallbackNum3,'userCallbackNum4':userCallbackNum4,'userCallbackNum5':userCallbackNum5,'userSubmit':userSubmit,'environmentTables':environmentTables,'environmentUnitTable':environmentUnitTable,'environmentUnitEntry':environmentUnitEntry,_L:environmentUnitIndex,'environmentUnitName':environmentUnitName,'environmentUnitTemperature':environmentUnitTemperature,'environmentUnitCurrentA':environmentUnitCurrentA,'environmentUnitVoltageA':environmentUnitVoltageA,'environmentUnitPowerA':environmentUnitPowerA,'environmentUnitCurrentB':environmentUnitCurrentB,'environmentUnitVoltageB':environmentUnitVoltageB,'environmentUnitPowerB':environmentUnitPowerB,'environmentUnitCurrentC':environmentUnitCurrentC,'environmentUnitVoltageC':environmentUnitVoltageC,'environmentUnitPowerC':environmentUnitPowerC,'environmentUnitCurrentD':environmentUnitCurrentD,'environmentUnitVoltageD':environmentUnitVoltageD,'environmentUnitPowerD':environmentUnitPowerD,'environmentSysRAM':environmentSysRAM,'environmentSysFlash':environmentSysFlash,'environmentMacEth0':environmentMacEth0,'environmentMacEth1':environmentMacEth1,'environmentInputPower1':environmentInputPower1,'environmentInputPower2':environmentInputPower2,'environmentInputPower3':environmentInputPower3,'environmentInputPower4':environmentInputPower4,'environmentModemPhoneNumber':environmentModemPhoneNumber,'environmentSerialNumber':environmentSerialNumber,'environmentSoftwareVersion':environmentSoftwareVersion,'environmentSystemTotalCurrent':environmentSystemTotalCurrent,'environmentSystemTotalPower':environmentSystemTotalPower,'environmentMonthlyPowerLog':environmentMonthlyPowerLog,'alarmTables':alarmTables,'alarmOverCurrentInitial':alarmOverCurrentInitial,'alarmOverCurrentCritical':alarmOverCurrentCritical,'alarmOverTemperatureInitial':alarmOverTemperatureInitial,'alarmOverTemperatureCritical':alarmOverTemperatureCritical,'alarmCircuitBreakerOpen':alarmCircuitBreakerOpen,'alarmCommLoss':alarmCommLoss,'alarmLostVoltage':alarmLostVoltage,'alarmPingNoAnswer':alarmPingNoAnswer,'alarmInvalidAccessLockout':alarmInvalidAccessLockout,'alarmPowerCycle':alarmPowerCycle,'alarmAlarmInput':alarmAlarmInput,'alarmPlugCurrent':alarmPlugCurrent,'alarmLostOptoVoltage':alarmLostOptoVoltage,'alarmEmergencyShutoff':alarmEmergencyShutoff,'alarmNoDialtone':alarmNoDialtone,'alarmWakeupOnFailure':alarmWakeupOnFailure,'alarmIpPassthroughDataUsage':alarmIpPassthroughDataUsage,'alarmBufferFiltering':alarmBufferFiltering,'wtiTraps':wtiTraps,_D:trapInfo,'testTraps':testTraps,'testTrap':testTrap,'overCurrentInitialTraps':overCurrentInitialTraps,'overCurrentInitialSetTrap':overCurrentInitialSetTrap,'overCurrentInitialClearTrap':overCurrentInitialClearTrap,'overCurrentCriticalTraps':overCurrentCriticalTraps,'overCurrentCriticalSetTrap':overCurrentCriticalSetTrap,'overCurrentCriticalClearTrap':overCurrentCriticalClearTrap,'overTemperatureInitialTraps':overTemperatureInitialTraps,'overTemperatureInitialSetTrap':overTemperatureInitialSetTrap,'overTemperatureInitialClearTrap':overTemperatureInitialClearTrap,'overTemperatureCriticalTraps':overTemperatureCriticalTraps,'overTemperatureCriticalSetTrap':overTemperatureCriticalSetTrap,'overTemperatureCriticalClearTrap':overTemperatureCriticalClearTrap,'circuitBreakerOpenTraps':circuitBreakerOpenTraps,'circuitBreakerOpenSetTrap':circuitBreakerOpenSetTrap,'circuitBreakerOpenClearTrap':circuitBreakerOpenClearTrap,'lostCommTraps':lostCommTraps,'lostCommSetTrap':lostCommSetTrap,'lostCommClearTrap':lostCommClearTrap,'lostVoltageTraps':lostVoltageTraps,'lostVoltageSetTrap':lostVoltageSetTrap,'lostVoltageClearTrap':lostVoltageClearTrap,'pingNoAnswerTraps':pingNoAnswerTraps,'pingNoAnswerSetTrap':pingNoAnswerSetTrap,'pingNoAnswerClearTrap':pingNoAnswerClearTrap,'lockoutTraps':lockoutTraps,'lockoutSetTrap':lockoutSetTrap,'lockoutClearTrap':lockoutClearTrap,'powercycleTraps':powercycleTraps,'powercycleSetTrap':powercycleSetTrap,'alarmInputTraps':alarmInputTraps,'alarmInputSetTrap':alarmInputSetTrap,'alarmInputClearTrap':alarmInputClearTrap,'plugCurrentTraps':plugCurrentTraps,'plugCurrentSetTrap':plugCurrentSetTrap,'plugCurrentClearTrap':plugCurrentClearTrap,'lostOptoVoltageTraps':lostOptoVoltageTraps,'lostOptoVoltageSetTrap':lostOptoVoltageSetTrap,'lostOptoVoltageClearTrap':lostOptoVoltageClearTrap,'emergencyShutoffTraps':emergencyShutoffTraps,'emergencyShutoffSetTrap':emergencyShutoffSetTrap,'emergencyShutoffClearTrap':emergencyShutoffClearTrap,'noDialtoneTraps':noDialtoneTraps,'noDialtoneSetTrap':noDialtoneSetTrap,'noDialtoneClearTrap':noDialtoneClearTrap,'wakeupOnFailureTraps':wakeupOnFailureTraps,'wakeupOnFailureSetTrap':wakeupOnFailureSetTrap,'wakeupOnFailureClearTrap':wakeupOnFailureClearTrap,'ipPassthroughDataUsageTraps':ipPassthroughDataUsageTraps,'ipPassthroughDataUsageSetTrap':ipPassthroughDataUsageSetTrap,'ipPassthroughDataUsageClearTrap':ipPassthroughDataUsageClearTrap,'bufferFilteringTraps':bufferFilteringTraps,'bufferFilteringSetTrap':bufferFilteringSetTrap,'bufferFilteringClearTrap':bufferFilteringClearTrap})