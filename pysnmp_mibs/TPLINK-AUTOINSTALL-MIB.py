_F='OctetString'
_E='enable'
_D='disable'
_C='read-write'
_B='current'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkAutoInstallMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,97))
if mibBuilder.loadTexts:tplinkAutoInstallMIB.setRevisions(('2012-12-17 10:14',))
_TplinkAutoInstallMIBObjects_ObjectIdentity=ObjectIdentity
tplinkAutoInstallMIBObjects=_TplinkAutoInstallMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,97,1))
_AutoInstallConfig_ObjectIdentity=ObjectIdentity
autoInstallConfig=_AutoInstallConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,97,1,1))
class _AutoInstallStartStop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('stop',0),('start',1)))
_AutoInstallStartStop_Type.__name__=_A
_AutoInstallStartStop_Object=MibScalar
autoInstallStartStop=_AutoInstallStartStop_Object((1,3,6,1,4,1,11863,6,97,1,1,1),_AutoInstallStartStop_Type())
autoInstallStartStop.setMaxAccess(_C)
if mibBuilder.loadTexts:autoInstallStartStop.setStatus(_B)
class _AutoInstallPersistentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_AutoInstallPersistentMode_Type.__name__=_A
_AutoInstallPersistentMode_Object=MibScalar
autoInstallPersistentMode=_AutoInstallPersistentMode_Object((1,3,6,1,4,1,11863,6,97,1,1,2),_AutoInstallPersistentMode_Type())
autoInstallPersistentMode.setMaxAccess(_C)
if mibBuilder.loadTexts:autoInstallPersistentMode.setStatus(_B)
class _AutoInstallAutoSave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_AutoInstallAutoSave_Type.__name__=_A
_AutoInstallAutoSave_Object=MibScalar
autoInstallAutoSave=_AutoInstallAutoSave_Object((1,3,6,1,4,1,11863,6,97,1,1,3),_AutoInstallAutoSave_Type())
autoInstallAutoSave.setMaxAccess(_C)
if mibBuilder.loadTexts:autoInstallAutoSave.setStatus(_B)
class _AutoInstallAutoReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_AutoInstallAutoReboot_Type.__name__=_A
_AutoInstallAutoReboot_Object=MibScalar
autoInstallAutoReboot=_AutoInstallAutoReboot_Object((1,3,6,1,4,1,11863,6,97,1,1,4),_AutoInstallAutoReboot_Type())
autoInstallAutoReboot.setMaxAccess(_C)
if mibBuilder.loadTexts:autoInstallAutoReboot.setStatus(_B)
class _AutoInstallRetryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_AutoInstallRetryCount_Type.__name__=_A
_AutoInstallRetryCount_Object=MibScalar
autoInstallRetryCount=_AutoInstallRetryCount_Object((1,3,6,1,4,1,11863,6,97,1,1,5),_AutoInstallRetryCount_Type())
autoInstallRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:autoInstallRetryCount.setStatus(_B)
class _AutoInstallState_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_AutoInstallState_Type.__name__=_F
_AutoInstallState_Object=MibScalar
autoInstallState=_AutoInstallState_Object((1,3,6,1,4,1,11863,6,97,1,1,6),_AutoInstallState_Type())
autoInstallState.setMaxAccess('read-only')
if mibBuilder.loadTexts:autoInstallState.setStatus(_B)
_TplinkAutoInstallNotifications_ObjectIdentity=ObjectIdentity
tplinkAutoInstallNotifications=_TplinkAutoInstallNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,97,2))
mibBuilder.exportSymbols('TPLINK-AUTOINSTALL-MIB',**{'tplinkAutoInstallMIB':tplinkAutoInstallMIB,'tplinkAutoInstallMIBObjects':tplinkAutoInstallMIBObjects,'autoInstallConfig':autoInstallConfig,'autoInstallStartStop':autoInstallStartStop,'autoInstallPersistentMode':autoInstallPersistentMode,'autoInstallAutoSave':autoInstallAutoSave,'autoInstallAutoReboot':autoInstallAutoReboot,'autoInstallRetryCount':autoInstallRetryCount,'autoInstallState':autoInstallState,'tplinkAutoInstallNotifications':tplinkAutoInstallNotifications})