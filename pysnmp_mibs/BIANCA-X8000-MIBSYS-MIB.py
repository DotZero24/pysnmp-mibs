_S='critical'
_R='normal'
_Q='running'
_P='missing'
_O='NotificationType'
_N='sysX8ConfigPowerSupply1TempAlarmThreshold'
_M='read-write'
_L='sysX8ConfigPowerSupply1TempAlarmTrap'
_K='sysX8ConfigPowerSupply2TempAlarmThreshold'
_J='sysX8ConfigPowerSupply2Temp'
_I='sysX8ConfigPowerSupply2State'
_H='sysX8ConfigPowerSupply1Temp'
_G='sysX8ConfigPowerSupply1State'
_F='Integer32'
_E='read-only'
_D='sysName'
_C='sysDescr'
_B='mandatory'
_A='BIANCA-X8000-MIBSYS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier',_O,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_O,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bibo_ObjectIdentity=ObjectIdentity
bibo=_Bibo_ObjectIdentity((1,3,6,1,4,1,272,4))
_Sys_ObjectIdentity=ObjectIdentity
sys=_Sys_ObjectIdentity((1,3,6,1,4,1,272,4,17))
_X8_ObjectIdentity=ObjectIdentity
x8=_X8_ObjectIdentity((1,3,6,1,4,1,272,4,17,3))
_SysX8Config_ObjectIdentity=ObjectIdentity
sysX8Config=_SysX8Config_ObjectIdentity((1,3,6,1,4,1,272,4,17,3,1))
class _SysX8ConfigPowerSupply1State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),('off',2),(_Q,3),('fail',4)))
_SysX8ConfigPowerSupply1State_Type.__name__=_F
_SysX8ConfigPowerSupply1State_Object=MibScalar
sysX8ConfigPowerSupply1State=_SysX8ConfigPowerSupply1State_Object((1,3,6,1,4,1,272,4,17,3,1,1),_SysX8ConfigPowerSupply1State_Type())
sysX8ConfigPowerSupply1State.setMaxAccess(_E)
if mibBuilder.loadTexts:sysX8ConfigPowerSupply1State.setStatus(_B)
class _SysX8ConfigPowerSupply1Temp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,250))
_SysX8ConfigPowerSupply1Temp_Type.__name__=_F
_SysX8ConfigPowerSupply1Temp_Object=MibScalar
sysX8ConfigPowerSupply1Temp=_SysX8ConfigPowerSupply1Temp_Object((1,3,6,1,4,1,272,4,17,3,1,2),_SysX8ConfigPowerSupply1Temp_Type())
sysX8ConfigPowerSupply1Temp.setMaxAccess(_E)
if mibBuilder.loadTexts:sysX8ConfigPowerSupply1Temp.setStatus(_B)
class _SysX8ConfigPowerSupply1TempAlarmThreshold_Type(Integer32):defaultValue=40;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,250))
_SysX8ConfigPowerSupply1TempAlarmThreshold_Type.__name__=_F
_SysX8ConfigPowerSupply1TempAlarmThreshold_Object=MibScalar
sysX8ConfigPowerSupply1TempAlarmThreshold=_SysX8ConfigPowerSupply1TempAlarmThreshold_Object((1,3,6,1,4,1,272,4,17,3,1,3),_SysX8ConfigPowerSupply1TempAlarmThreshold_Type())
sysX8ConfigPowerSupply1TempAlarmThreshold.setMaxAccess(_M)
if mibBuilder.loadTexts:sysX8ConfigPowerSupply1TempAlarmThreshold.setStatus(_B)
class _SysX8ConfigPowerSupply1TempAlarmTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_SysX8ConfigPowerSupply1TempAlarmTrap_Type.__name__=_F
_SysX8ConfigPowerSupply1TempAlarmTrap_Object=MibScalar
sysX8ConfigPowerSupply1TempAlarmTrap=_SysX8ConfigPowerSupply1TempAlarmTrap_Object((1,3,6,1,4,1,272,4,17,3,1,4),_SysX8ConfigPowerSupply1TempAlarmTrap_Type())
sysX8ConfigPowerSupply1TempAlarmTrap.setMaxAccess(_E)
if mibBuilder.loadTexts:sysX8ConfigPowerSupply1TempAlarmTrap.setStatus(_B)
class _SysX8ConfigPowerSupply2State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),('off',2),(_Q,3),('fail',4)))
_SysX8ConfigPowerSupply2State_Type.__name__=_F
_SysX8ConfigPowerSupply2State_Object=MibScalar
sysX8ConfigPowerSupply2State=_SysX8ConfigPowerSupply2State_Object((1,3,6,1,4,1,272,4,17,3,1,5),_SysX8ConfigPowerSupply2State_Type())
sysX8ConfigPowerSupply2State.setMaxAccess(_E)
if mibBuilder.loadTexts:sysX8ConfigPowerSupply2State.setStatus(_B)
class _SysX8ConfigPowerSupply2Temp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,250))
_SysX8ConfigPowerSupply2Temp_Type.__name__=_F
_SysX8ConfigPowerSupply2Temp_Object=MibScalar
sysX8ConfigPowerSupply2Temp=_SysX8ConfigPowerSupply2Temp_Object((1,3,6,1,4,1,272,4,17,3,1,6),_SysX8ConfigPowerSupply2Temp_Type())
sysX8ConfigPowerSupply2Temp.setMaxAccess(_E)
if mibBuilder.loadTexts:sysX8ConfigPowerSupply2Temp.setStatus(_B)
class _SysX8ConfigPowerSupply2TempAlarmThreshold_Type(Integer32):defaultValue=40;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,250))
_SysX8ConfigPowerSupply2TempAlarmThreshold_Type.__name__=_F
_SysX8ConfigPowerSupply2TempAlarmThreshold_Object=MibScalar
sysX8ConfigPowerSupply2TempAlarmThreshold=_SysX8ConfigPowerSupply2TempAlarmThreshold_Object((1,3,6,1,4,1,272,4,17,3,1,7),_SysX8ConfigPowerSupply2TempAlarmThreshold_Type())
sysX8ConfigPowerSupply2TempAlarmThreshold.setMaxAccess(_M)
if mibBuilder.loadTexts:sysX8ConfigPowerSupply2TempAlarmThreshold.setStatus(_B)
class _SysX8ConfigPowerSupply2TempAlarmTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_SysX8ConfigPowerSupply2TempAlarmTrap_Type.__name__=_F
_SysX8ConfigPowerSupply2TempAlarmTrap_Object=MibScalar
sysX8ConfigPowerSupply2TempAlarmTrap=_SysX8ConfigPowerSupply2TempAlarmTrap_Object((1,3,6,1,4,1,272,4,17,3,1,8),_SysX8ConfigPowerSupply2TempAlarmTrap_Type())
sysX8ConfigPowerSupply2TempAlarmTrap.setMaxAccess(_E)
if mibBuilder.loadTexts:sysX8ConfigPowerSupply2TempAlarmTrap.setStatus(_B)
class _SysX8ConfigFanControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('high',2)))
_SysX8ConfigFanControl_Type.__name__=_F
_SysX8ConfigFanControl_Object=MibScalar
sysX8ConfigFanControl=_SysX8ConfigFanControl_Object((1,3,6,1,4,1,272,4,17,3,1,9),_SysX8ConfigFanControl_Type())
sysX8ConfigFanControl.setMaxAccess(_M)
if mibBuilder.loadTexts:sysX8ConfigFanControl.setStatus(_B)
_SysX8ConfigFanVersion_Type=DisplayString
_SysX8ConfigFanVersion_Object=MibScalar
sysX8ConfigFanVersion=_SysX8ConfigFanVersion_Object((1,3,6,1,4,1,272,4,17,3,1,10),_SysX8ConfigFanVersion_Type())
sysX8ConfigFanVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:sysX8ConfigFanVersion.setStatus(_B)
_SysX8ConfigFan1_Type=Integer32
_SysX8ConfigFan1_Object=MibScalar
sysX8ConfigFan1=_SysX8ConfigFan1_Object((1,3,6,1,4,1,272,4,17,3,1,11),_SysX8ConfigFan1_Type())
sysX8ConfigFan1.setMaxAccess(_E)
if mibBuilder.loadTexts:sysX8ConfigFan1.setStatus(_B)
_SysX8ConfigFan2_Type=Integer32
_SysX8ConfigFan2_Object=MibScalar
sysX8ConfigFan2=_SysX8ConfigFan2_Object((1,3,6,1,4,1,272,4,17,3,1,12),_SysX8ConfigFan2_Type())
sysX8ConfigFan2.setMaxAccess(_E)
if mibBuilder.loadTexts:sysX8ConfigFan2.setStatus(_B)
_SysX8ConfigFan3_Type=Integer32
_SysX8ConfigFan3_Object=MibScalar
sysX8ConfigFan3=_SysX8ConfigFan3_Object((1,3,6,1,4,1,272,4,17,3,1,13),_SysX8ConfigFan3_Type())
sysX8ConfigFan3.setMaxAccess(_E)
if mibBuilder.loadTexts:sysX8ConfigFan3.setStatus(_B)
_SysX8ConfigFan4_Type=Integer32
_SysX8ConfigFan4_Object=MibScalar
sysX8ConfigFan4=_SysX8ConfigFan4_Object((1,3,6,1,4,1,272,4,17,3,1,14),_SysX8ConfigFan4_Type())
sysX8ConfigFan4.setMaxAccess(_E)
if mibBuilder.loadTexts:sysX8ConfigFan4.setStatus(_B)
_SysX8Traps_ObjectIdentity=ObjectIdentity
sysX8Traps=_SysX8Traps_ObjectIdentity((1,3,6,1,4,1,272,4,17,3,2))
sysX8TrapPowerSupply1Missing=NotificationType((1,3,6,1,4,1,272,4,17,3,2,0,1))
sysX8TrapPowerSupply1Missing.setObjects(*((_A,_C),(_A,_D),(_A,_G),(_A,_H),(_A,_L)))
if mibBuilder.loadTexts:sysX8TrapPowerSupply1Missing.setStatus('')
sysX8TrapPowerSupply1PowerOff=NotificationType((1,3,6,1,4,1,272,4,17,3,2,0,2))
sysX8TrapPowerSupply1PowerOff.setObjects(*((_A,_C),(_A,_D),(_A,_G),(_A,_H),(_A,_L)))
if mibBuilder.loadTexts:sysX8TrapPowerSupply1PowerOff.setStatus('')
sysX8TrapPowerSupply1PowerFail=NotificationType((1,3,6,1,4,1,272,4,17,3,2,0,3))
sysX8TrapPowerSupply1PowerFail.setObjects(*((_A,_C),(_A,_D),(_A,_G),(_A,_H),(_A,_L)))
if mibBuilder.loadTexts:sysX8TrapPowerSupply1PowerFail.setStatus('')
sysX8TrapPowerSupply1PowerGood=NotificationType((1,3,6,1,4,1,272,4,17,3,2,0,4))
sysX8TrapPowerSupply1PowerGood.setObjects(*((_A,_C),(_A,_D),(_A,_G),(_A,_H),(_A,_L)))
if mibBuilder.loadTexts:sysX8TrapPowerSupply1PowerGood.setStatus('')
sysX8TrapPowerSupply1TempCritical=NotificationType((1,3,6,1,4,1,272,4,17,3,2,0,5))
sysX8TrapPowerSupply1TempCritical.setObjects(*((_A,_C),(_A,_D),(_A,_G),(_A,_H),(_A,_N)))
if mibBuilder.loadTexts:sysX8TrapPowerSupply1TempCritical.setStatus('')
sysX8TrapPowerSupply1TempOk=NotificationType((1,3,6,1,4,1,272,4,17,3,2,0,6))
sysX8TrapPowerSupply1TempOk.setObjects(*((_A,_C),(_A,_D),(_A,_G),(_A,_H),(_A,_N)))
if mibBuilder.loadTexts:sysX8TrapPowerSupply1TempOk.setStatus('')
sysX8TrapPowerSupply2Missing=NotificationType((1,3,6,1,4,1,272,4,17,3,2,0,7))
sysX8TrapPowerSupply2Missing.setObjects(*((_A,_C),(_A,_D),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:sysX8TrapPowerSupply2Missing.setStatus('')
sysX8TrapPowerSupply2PowerOff=NotificationType((1,3,6,1,4,1,272,4,17,3,2,0,8))
sysX8TrapPowerSupply2PowerOff.setObjects(*((_A,_C),(_A,_D),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:sysX8TrapPowerSupply2PowerOff.setStatus('')
sysX8TrapPowerSupply2PowerFail=NotificationType((1,3,6,1,4,1,272,4,17,3,2,0,9))
sysX8TrapPowerSupply2PowerFail.setObjects(*((_A,_C),(_A,_D),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:sysX8TrapPowerSupply2PowerFail.setStatus('')
sysX8TrapPowerSupply2PowerGood=NotificationType((1,3,6,1,4,1,272,4,17,3,2,0,10))
sysX8TrapPowerSupply2PowerGood.setObjects(*((_A,_C),(_A,_D),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:sysX8TrapPowerSupply2PowerGood.setStatus('')
sysX8TrapPowerSupply2TempCritical=NotificationType((1,3,6,1,4,1,272,4,17,3,2,0,11))
sysX8TrapPowerSupply2TempCritical.setObjects(*((_A,_C),(_A,_D),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:sysX8TrapPowerSupply2TempCritical.setStatus('')
sysX8TrapPowerSupply2TempOk=NotificationType((1,3,6,1,4,1,272,4,17,3,2,0,12))
sysX8TrapPowerSupply2TempOk.setObjects(*((_A,_C),(_A,_D),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:sysX8TrapPowerSupply2TempOk.setStatus('')
mibBuilder.exportSymbols(_A,**{'bintec':bintec,'bibo':bibo,'sys':sys,'x8':x8,'sysX8Config':sysX8Config,_G:sysX8ConfigPowerSupply1State,_H:sysX8ConfigPowerSupply1Temp,_N:sysX8ConfigPowerSupply1TempAlarmThreshold,_L:sysX8ConfigPowerSupply1TempAlarmTrap,_I:sysX8ConfigPowerSupply2State,_J:sysX8ConfigPowerSupply2Temp,_K:sysX8ConfigPowerSupply2TempAlarmThreshold,'sysX8ConfigPowerSupply2TempAlarmTrap':sysX8ConfigPowerSupply2TempAlarmTrap,'sysX8ConfigFanControl':sysX8ConfigFanControl,'sysX8ConfigFanVersion':sysX8ConfigFanVersion,'sysX8ConfigFan1':sysX8ConfigFan1,'sysX8ConfigFan2':sysX8ConfigFan2,'sysX8ConfigFan3':sysX8ConfigFan3,'sysX8ConfigFan4':sysX8ConfigFan4,'sysX8Traps':sysX8Traps,'sysX8TrapPowerSupply1Missing':sysX8TrapPowerSupply1Missing,'sysX8TrapPowerSupply1PowerOff':sysX8TrapPowerSupply1PowerOff,'sysX8TrapPowerSupply1PowerFail':sysX8TrapPowerSupply1PowerFail,'sysX8TrapPowerSupply1PowerGood':sysX8TrapPowerSupply1PowerGood,'sysX8TrapPowerSupply1TempCritical':sysX8TrapPowerSupply1TempCritical,'sysX8TrapPowerSupply1TempOk':sysX8TrapPowerSupply1TempOk,'sysX8TrapPowerSupply2Missing':sysX8TrapPowerSupply2Missing,'sysX8TrapPowerSupply2PowerOff':sysX8TrapPowerSupply2PowerOff,'sysX8TrapPowerSupply2PowerFail':sysX8TrapPowerSupply2PowerFail,'sysX8TrapPowerSupply2PowerGood':sysX8TrapPowerSupply2PowerGood,'sysX8TrapPowerSupply2TempCritical':sysX8TrapPowerSupply2TempCritical,'sysX8TrapPowerSupply2TempOk':sysX8TrapPowerSupply2TempOk})