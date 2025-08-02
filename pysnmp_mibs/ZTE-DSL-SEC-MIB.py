_J='zxDslIllegalLoginIP'
_I='zxDslIllegalLoginType'
_H='zxDslIllegalLoginUserName'
_G='zxDslSysLatestLogonCrftTerminalType'
_F='DisplayString'
_E='read-write'
_D='read-only'
_C='ZTE-DSL-SEC-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
zxDsl,=mibBuilder.importSymbols('ZTE-DSL-MIB','zxDsl')
zxDslSysSecMib=ModuleIdentity((1,3,6,1,4,1,3902,1004,36))
_ZxDslSysSecObjects_ObjectIdentity=ObjectIdentity
zxDslSysSecObjects=_ZxDslSysSecObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,36,1))
class _ZxDslCrftTerminalEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_ZxDslCrftTerminalEnable_Type.__name__=_B
_ZxDslCrftTerminalEnable_Object=MibScalar
zxDslCrftTerminalEnable=_ZxDslCrftTerminalEnable_Object((1,3,6,1,4,1,3902,1004,36,1,1),_ZxDslCrftTerminalEnable_Type())
zxDslCrftTerminalEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslCrftTerminalEnable.setStatus(_A)
class _ZxDslCliSecurityLevel_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('guest',1),('administrator',2)))
_ZxDslCliSecurityLevel_Type.__name__=_B
_ZxDslCliSecurityLevel_Object=MibScalar
zxDslCliSecurityLevel=_ZxDslCliSecurityLevel_Object((1,3,6,1,4,1,3902,1004,36,1,2),_ZxDslCliSecurityLevel_Type())
zxDslCliSecurityLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslCliSecurityLevel.setStatus(_A)
class _ZxDslCrftTerminalLogonStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('logon',1),('logout',2)))
_ZxDslCrftTerminalLogonStatus_Type.__name__=_B
_ZxDslCrftTerminalLogonStatus_Object=MibScalar
zxDslCrftTerminalLogonStatus=_ZxDslCrftTerminalLogonStatus_Object((1,3,6,1,4,1,3902,1004,36,1,3),_ZxDslCrftTerminalLogonStatus_Type())
zxDslCrftTerminalLogonStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslCrftTerminalLogonStatus.setStatus(_A)
class _ZxDslSysLatestLogonCrftTerminalType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rs232SerialInterface',1),('outbandMgmtInterface',2)))
_ZxDslSysLatestLogonCrftTerminalType_Type.__name__=_B
_ZxDslSysLatestLogonCrftTerminalType_Object=MibScalar
zxDslSysLatestLogonCrftTerminalType=_ZxDslSysLatestLogonCrftTerminalType_Object((1,3,6,1,4,1,3902,1004,36,1,4),_ZxDslSysLatestLogonCrftTerminalType_Type())
zxDslSysLatestLogonCrftTerminalType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslSysLatestLogonCrftTerminalType.setStatus(_A)
class _ZxDslCliLogonWelcomeMessage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,400))
_ZxDslCliLogonWelcomeMessage_Type.__name__=_F
_ZxDslCliLogonWelcomeMessage_Object=MibScalar
zxDslCliLogonWelcomeMessage=_ZxDslCliLogonWelcomeMessage_Object((1,3,6,1,4,1,3902,1004,36,1,5),_ZxDslCliLogonWelcomeMessage_Type())
zxDslCliLogonWelcomeMessage.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslCliLogonWelcomeMessage.setStatus(_A)
class _ZxDslCliLogonOvertimeMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_ZxDslCliLogonOvertimeMin_Type.__name__=_B
_ZxDslCliLogonOvertimeMin_Object=MibScalar
zxDslCliLogonOvertimeMin=_ZxDslCliLogonOvertimeMin_Object((1,3,6,1,4,1,3902,1004,36,1,6),_ZxDslCliLogonOvertimeMin_Type())
zxDslCliLogonOvertimeMin.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslCliLogonOvertimeMin.setStatus(_A)
class _ZxDslIllegalLoginUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ZxDslIllegalLoginUserName_Type.__name__=_F
_ZxDslIllegalLoginUserName_Object=MibScalar
zxDslIllegalLoginUserName=_ZxDslIllegalLoginUserName_Object((1,3,6,1,4,1,3902,1004,36,1,7),_ZxDslIllegalLoginUserName_Type())
zxDslIllegalLoginUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslIllegalLoginUserName.setStatus(_A)
class _ZxDslIllegalLoginType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('console',1),('telnet',2),('ssh',3)))
_ZxDslIllegalLoginType_Type.__name__=_B
_ZxDslIllegalLoginType_Object=MibScalar
zxDslIllegalLoginType=_ZxDslIllegalLoginType_Object((1,3,6,1,4,1,3902,1004,36,1,8),_ZxDslIllegalLoginType_Type())
zxDslIllegalLoginType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslIllegalLoginType.setStatus(_A)
_ZxDslIllegalLoginIP_Type=IpAddress
_ZxDslIllegalLoginIP_Object=MibScalar
zxDslIllegalLoginIP=_ZxDslIllegalLoginIP_Object((1,3,6,1,4,1,3902,1004,36,1,9),_ZxDslIllegalLoginIP_Type())
zxDslIllegalLoginIP.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslIllegalLoginIP.setStatus(_A)
_ZxDslSysSecTrapObjects_ObjectIdentity=ObjectIdentity
zxDslSysSecTrapObjects=_ZxDslSysSecTrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,36,2))
zxDslCrftTerminLogonTrap=NotificationType((1,3,6,1,4,1,3902,1004,36,2,1))
zxDslCrftTerminLogonTrap.setObjects((_C,_G))
if mibBuilder.loadTexts:zxDslCrftTerminLogonTrap.setStatus(_A)
zxDslCrftTerminLogoutTrap=NotificationType((1,3,6,1,4,1,3902,1004,36,2,2))
zxDslCrftTerminLogoutTrap.setObjects((_C,_G))
if mibBuilder.loadTexts:zxDslCrftTerminLogoutTrap.setStatus(_A)
zxDslIllegalLoginTrap=NotificationType((1,3,6,1,4,1,3902,1004,36,2,3))
zxDslIllegalLoginTrap.setObjects(*((_C,_H),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:zxDslIllegalLoginTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zxDslSysSecMib':zxDslSysSecMib,'zxDslSysSecObjects':zxDslSysSecObjects,'zxDslCrftTerminalEnable':zxDslCrftTerminalEnable,'zxDslCliSecurityLevel':zxDslCliSecurityLevel,'zxDslCrftTerminalLogonStatus':zxDslCrftTerminalLogonStatus,_G:zxDslSysLatestLogonCrftTerminalType,'zxDslCliLogonWelcomeMessage':zxDslCliLogonWelcomeMessage,'zxDslCliLogonOvertimeMin':zxDslCliLogonOvertimeMin,_H:zxDslIllegalLoginUserName,_I:zxDslIllegalLoginType,_J:zxDslIllegalLoginIP,'zxDslSysSecTrapObjects':zxDslSysSecTrapObjects,'zxDslCrftTerminLogonTrap':zxDslCrftTerminLogonTrap,'zxDslCrftTerminLogoutTrap':zxDslCrftTerminLogoutTrap,'zxDslIllegalLoginTrap':zxDslIllegalLoginTrap})