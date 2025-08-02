_K='rsAlarmMsg'
_J='rsAlarmHostname'
_I='rsAlarmLevel'
_H='rsAlarmTime'
_G='rsAlarmLabel'
_F='rsAlarmId'
_E='Integer32'
_D='OctetString'
_C='RAPID-SYSTEM-CONFIG-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rapidstream,=mibBuilder.importSymbols('RAPID-MIB','rapidstream')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rsSystemConfigMIB=ModuleIdentity((1,3,6,1,4,1,4355,2))
if mibBuilder.loadTexts:rsSystemConfigMIB.setRevisions(('1999-06-26 12:00','2002-11-01 12:00','2004-06-01 12:00'))
_RsSysTraps_ObjectIdentity=ObjectIdentity
rsSysTraps=_RsSysTraps_ObjectIdentity((1,3,6,1,4,1,4355,2,3))
if mibBuilder.loadTexts:rsSysTraps.setStatus(_A)
_RsSysTrapsPrefix_ObjectIdentity=ObjectIdentity
rsSysTrapsPrefix=_RsSysTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,4355,2,3,0))
if mibBuilder.loadTexts:rsSysTrapsPrefix.setStatus(_A)
_RsSysTrapObjects_ObjectIdentity=ObjectIdentity
rsSysTrapObjects=_RsSysTrapObjects_ObjectIdentity((1,3,6,1,4,1,4355,2,4))
if mibBuilder.loadTexts:rsSysTrapObjects.setStatus(_A)
_RsAlarmId_Type=Integer32
_RsAlarmId_Object=MibScalar
rsAlarmId=_RsAlarmId_Object((1,3,6,1,4,1,4355,2,4,1),_RsAlarmId_Type())
rsAlarmId.setMaxAccess(_B)
if mibBuilder.loadTexts:rsAlarmId.setStatus(_A)
class _RsAlarmLabel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_RsAlarmLabel_Type.__name__=_D
_RsAlarmLabel_Object=MibScalar
rsAlarmLabel=_RsAlarmLabel_Object((1,3,6,1,4,1,4355,2,4,2),_RsAlarmLabel_Type())
rsAlarmLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:rsAlarmLabel.setStatus(_A)
_RsAlarmTime_Type=OctetString
_RsAlarmTime_Object=MibScalar
rsAlarmTime=_RsAlarmTime_Object((1,3,6,1,4,1,4355,2,4,3),_RsAlarmTime_Type())
rsAlarmTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rsAlarmTime.setStatus(_A)
class _RsAlarmLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('critical',1),('error',2),('warning',3),('normal',4)))
_RsAlarmLevel_Type.__name__=_E
_RsAlarmLevel_Object=MibScalar
rsAlarmLevel=_RsAlarmLevel_Object((1,3,6,1,4,1,4355,2,4,4),_RsAlarmLevel_Type())
rsAlarmLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:rsAlarmLevel.setStatus(_A)
class _RsAlarmHostname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_RsAlarmHostname_Type.__name__=_D
_RsAlarmHostname_Object=MibScalar
rsAlarmHostname=_RsAlarmHostname_Object((1,3,6,1,4,1,4355,2,4,5),_RsAlarmHostname_Type())
rsAlarmHostname.setMaxAccess(_B)
if mibBuilder.loadTexts:rsAlarmHostname.setStatus(_A)
_RsAlarmMsg_Type=OctetString
_RsAlarmMsg_Object=MibScalar
rsAlarmMsg=_RsAlarmMsg_Object((1,3,6,1,4,1,4355,2,4,6),_RsAlarmMsg_Type())
rsAlarmMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:rsAlarmMsg.setStatus(_A)
_RsSysTrapControl_ObjectIdentity=ObjectIdentity
rsSysTrapControl=_RsSysTrapControl_ObjectIdentity((1,3,6,1,4,1,4355,2,5))
if mibBuilder.loadTexts:rsSysTrapControl.setStatus(_A)
class _RsAlarmTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_RsAlarmTrapEnable_Type.__name__=_E
_RsAlarmTrapEnable_Object=MibScalar
rsAlarmTrapEnable=_RsAlarmTrapEnable_Object((1,3,6,1,4,1,4355,2,5,1),_RsAlarmTrapEnable_Type())
rsAlarmTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rsAlarmTrapEnable.setStatus(_A)
rsAlarmTrap=NotificationType((1,3,6,1,4,1,4355,2,3,0,1))
rsAlarmTrap.setObjects(*((_C,_F),(_C,_G),(_C,_H),(_C,_I),(_C,_J),(_C,_K)))
if mibBuilder.loadTexts:rsAlarmTrap.setStatus(_A)
rsSnmpStart=NotificationType((1,3,6,1,4,1,4355,2,3,0,2))
if mibBuilder.loadTexts:rsSnmpStart.setStatus(_A)
rsSnmpShutdown=NotificationType((1,3,6,1,4,1,4355,2,3,0,3))
if mibBuilder.loadTexts:rsSnmpShutdown.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'rsSystemConfigMIB':rsSystemConfigMIB,'rsSysTraps':rsSysTraps,'rsSysTrapsPrefix':rsSysTrapsPrefix,'rsAlarmTrap':rsAlarmTrap,'rsSnmpStart':rsSnmpStart,'rsSnmpShutdown':rsSnmpShutdown,'rsSysTrapObjects':rsSysTrapObjects,_F:rsAlarmId,_G:rsAlarmLabel,_H:rsAlarmTime,_I:rsAlarmLevel,_J:rsAlarmHostname,_K:rsAlarmMsg,'rsSysTrapControl':rsSysTrapControl,'rsAlarmTrapEnable':rsAlarmTrapEnable})