_M='eventName'
_L='eventId'
_K='componentId'
_J='componentName'
_I='deviceId'
_H='gridId'
_G='message'
_F='alertLevel'
_E='deviceName'
_D='Integer32'
_C='accessible-for-notify'
_B='SUNSTORAGEAGENT-NOTIFICATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alertTrap=ModuleIdentity((1,3,6,1,4,1,42,2,95,0))
if mibBuilder.loadTexts:alertTrap.setRevisions(('2002-10-16 00:00',))
_Sun_ObjectIdentity=ObjectIdentity
sun=_Sun_ObjectIdentity((1,3,6,1,4,1,42))
_Prod_ObjectIdentity=ObjectIdentity
prod=_Prod_ObjectIdentity((1,3,6,1,4,1,42,2))
_Storagent_ObjectIdentity=ObjectIdentity
storagent=_Storagent_ObjectIdentity((1,3,6,1,4,1,42,2,95))
_Alert_ObjectIdentity=ObjectIdentity
alert=_Alert_ObjectIdentity((1,3,6,1,4,1,42,2,95,1))
_AlertInfoGroup_ObjectIdentity=ObjectIdentity
alertInfoGroup=_AlertInfoGroup_ObjectIdentity((1,3,6,1,4,1,42,2,95,1,3))
_DeviceName_Type=OctetString
_DeviceName_Object=MibScalar
deviceName=_DeviceName_Object((1,3,6,1,4,1,42,2,95,1,3,1),_DeviceName_Type())
deviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceName.setStatus(_A)
class _AlertLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('clear',0),('minor',1),('major',2),('critical',3),('down',4)))
_AlertLevel_Type.__name__=_D
_AlertLevel_Object=MibScalar
alertLevel=_AlertLevel_Object((1,3,6,1,4,1,42,2,95,1,3,2),_AlertLevel_Type())
alertLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:alertLevel.setStatus(_A)
_Message_Type=OctetString
_Message_Object=MibScalar
message=_Message_Object((1,3,6,1,4,1,42,2,95,1,3,3),_Message_Type())
message.setMaxAccess(_C)
if mibBuilder.loadTexts:message.setStatus(_A)
_GridId_Type=OctetString
_GridId_Object=MibScalar
gridId=_GridId_Object((1,3,6,1,4,1,42,2,95,1,3,4),_GridId_Type())
gridId.setMaxAccess(_C)
if mibBuilder.loadTexts:gridId.setStatus(_A)
_DeviceId_Type=OctetString
_DeviceId_Object=MibScalar
deviceId=_DeviceId_Object((1,3,6,1,4,1,42,2,95,1,3,5),_DeviceId_Type())
deviceId.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceId.setStatus(_A)
_ComponentName_Type=OctetString
_ComponentName_Object=MibScalar
componentName=_ComponentName_Object((1,3,6,1,4,1,42,2,95,1,3,6),_ComponentName_Type())
componentName.setMaxAccess(_C)
if mibBuilder.loadTexts:componentName.setStatus(_A)
_ComponentId_Type=OctetString
_ComponentId_Object=MibScalar
componentId=_ComponentId_Object((1,3,6,1,4,1,42,2,95,1,3,7),_ComponentId_Type())
componentId.setMaxAccess(_C)
if mibBuilder.loadTexts:componentId.setStatus(_A)
_EventId_Type=OctetString
_EventId_Object=MibScalar
eventId=_EventId_Object((1,3,6,1,4,1,42,2,95,1,3,8),_EventId_Type())
eventId.setMaxAccess(_C)
if mibBuilder.loadTexts:eventId.setStatus(_A)
_EventName_Type=OctetString
_EventName_Object=MibScalar
eventName=_EventName_Object((1,3,6,1,4,1,42,2,95,1,3,9),_EventName_Type())
eventName.setMaxAccess(_C)
if mibBuilder.loadTexts:eventName.setStatus(_A)
alertMessage=NotificationType((1,3,6,1,4,1,42,2,95,0,6))
alertMessage.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:alertMessage.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'sun':sun,'prod':prod,'storagent':storagent,'alertTrap':alertTrap,'alertMessage':alertMessage,'alert':alert,'alertInfoGroup':alertInfoGroup,_E:deviceName,_F:alertLevel,_G:message,_H:gridId,_I:deviceId,_J:componentName,_K:componentId,_L:eventId,_M:eventName})