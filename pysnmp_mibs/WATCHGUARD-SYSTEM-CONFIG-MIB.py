_K='wgAlarmMsg'
_J='wgAlarmHostname'
_I='wgAlarmLevel'
_H='wgAlarmTime'
_G='wgAlarmLabel'
_F='wgAlarmId'
_E='Integer32'
_D='OctetString'
_C='WATCHGUARD-SYSTEM-CONFIG-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
watchguard,=mibBuilder.importSymbols('WATCHGUARD-SMI','watchguard')
wgSystemConfigMIB=ModuleIdentity((1,3,6,1,4,1,3097,2))
if mibBuilder.loadTexts:wgSystemConfigMIB.setRevisions(('2007-01-25 12:00','2008-11-10 00:00'))
_WgSysTraps_ObjectIdentity=ObjectIdentity
wgSysTraps=_WgSysTraps_ObjectIdentity((1,3,6,1,4,1,3097,2,3))
if mibBuilder.loadTexts:wgSysTraps.setStatus(_A)
_WgSysTrapsPrefix_ObjectIdentity=ObjectIdentity
wgSysTrapsPrefix=_WgSysTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,3097,2,3,0))
if mibBuilder.loadTexts:wgSysTrapsPrefix.setStatus(_A)
_WgSysTrapObjects_ObjectIdentity=ObjectIdentity
wgSysTrapObjects=_WgSysTrapObjects_ObjectIdentity((1,3,6,1,4,1,3097,2,4))
if mibBuilder.loadTexts:wgSysTrapObjects.setStatus(_A)
_WgAlarmId_Type=Integer32
_WgAlarmId_Object=MibScalar
wgAlarmId=_WgAlarmId_Object((1,3,6,1,4,1,3097,2,4,1),_WgAlarmId_Type())
wgAlarmId.setMaxAccess(_B)
if mibBuilder.loadTexts:wgAlarmId.setStatus(_A)
class _WgAlarmLabel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WgAlarmLabel_Type.__name__=_D
_WgAlarmLabel_Object=MibScalar
wgAlarmLabel=_WgAlarmLabel_Object((1,3,6,1,4,1,3097,2,4,2),_WgAlarmLabel_Type())
wgAlarmLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:wgAlarmLabel.setStatus(_A)
_WgAlarmTime_Type=OctetString
_WgAlarmTime_Object=MibScalar
wgAlarmTime=_WgAlarmTime_Object((1,3,6,1,4,1,3097,2,4,3),_WgAlarmTime_Type())
wgAlarmTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wgAlarmTime.setStatus(_A)
class _WgAlarmLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('critical',1),('error',2),('warning',3),('normal',4)))
_WgAlarmLevel_Type.__name__=_E
_WgAlarmLevel_Object=MibScalar
wgAlarmLevel=_WgAlarmLevel_Object((1,3,6,1,4,1,3097,2,4,4),_WgAlarmLevel_Type())
wgAlarmLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:wgAlarmLevel.setStatus(_A)
class _WgAlarmHostname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WgAlarmHostname_Type.__name__=_D
_WgAlarmHostname_Object=MibScalar
wgAlarmHostname=_WgAlarmHostname_Object((1,3,6,1,4,1,3097,2,4,5),_WgAlarmHostname_Type())
wgAlarmHostname.setMaxAccess(_B)
if mibBuilder.loadTexts:wgAlarmHostname.setStatus(_A)
_WgAlarmMsg_Type=OctetString
_WgAlarmMsg_Object=MibScalar
wgAlarmMsg=_WgAlarmMsg_Object((1,3,6,1,4,1,3097,2,4,6),_WgAlarmMsg_Type())
wgAlarmMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:wgAlarmMsg.setStatus(_A)
_WgSysTrapControl_ObjectIdentity=ObjectIdentity
wgSysTrapControl=_WgSysTrapControl_ObjectIdentity((1,3,6,1,4,1,3097,2,5))
if mibBuilder.loadTexts:wgSysTrapControl.setStatus(_A)
class _WgAlarmTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_WgAlarmTrapEnable_Type.__name__=_E
_WgAlarmTrapEnable_Object=MibScalar
wgAlarmTrapEnable=_WgAlarmTrapEnable_Object((1,3,6,1,4,1,3097,2,5,1),_WgAlarmTrapEnable_Type())
wgAlarmTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wgAlarmTrapEnable.setStatus(_A)
wgAlarmTrap=NotificationType((1,3,6,1,4,1,3097,2,3,0,1))
wgAlarmTrap.setObjects(*((_C,_F),(_C,_G),(_C,_H),(_C,_I),(_C,_J),(_C,_K)))
if mibBuilder.loadTexts:wgAlarmTrap.setStatus(_A)
wgSnmpShutdown=NotificationType((1,3,6,1,4,1,3097,2,3,0,2))
if mibBuilder.loadTexts:wgSnmpShutdown.setStatus(_A)
wgSnmpStart=NotificationType((1,3,6,1,4,1,3097,2,3,0,3))
if mibBuilder.loadTexts:wgSnmpStart.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'wgSystemConfigMIB':wgSystemConfigMIB,'wgSysTraps':wgSysTraps,'wgSysTrapsPrefix':wgSysTrapsPrefix,'wgAlarmTrap':wgAlarmTrap,'wgSnmpShutdown':wgSnmpShutdown,'wgSnmpStart':wgSnmpStart,'wgSysTrapObjects':wgSysTrapObjects,_F:wgAlarmId,_G:wgAlarmLabel,_H:wgAlarmTime,_I:wgAlarmLevel,_J:wgAlarmHostname,_K:wgAlarmMsg,'wgSysTrapControl':wgSysTrapControl,'wgAlarmTrapEnable':wgAlarmTrapEnable})