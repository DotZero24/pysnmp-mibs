_L='ciscoBbsmMIBNotificationGroup'
_K='ciscoBbsmMIBGroup'
_J='ciscoBbsmEvent'
_I='Integer32'
_H='cbbsmEventTime'
_G='cbbsmEventType'
_F='cbbsmEventID'
_E='cbbsmEventSource'
_D='cbbsmEventDescription'
_C='accessible-for-notify'
_B='current'
_A='CISCO-BBSM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
ciscoBbsmMIB=ModuleIdentity((1,3,6,1,4,1,9,9,358))
if mibBuilder.loadTexts:ciscoBbsmMIB.setRevisions(('2004-04-03 00:00',))
_CiscoBbsmNotifications_ObjectIdentity=ObjectIdentity
ciscoBbsmNotifications=_CiscoBbsmNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,358,0))
_CiscoBbsmMIBObjects_ObjectIdentity=ObjectIdentity
ciscoBbsmMIBObjects=_CiscoBbsmMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,358,1))
_CiscoBbsmEventInfo_ObjectIdentity=ObjectIdentity
ciscoBbsmEventInfo=_CiscoBbsmEventInfo_ObjectIdentity((1,3,6,1,4,1,9,9,358,1,1))
_CbbsmEventDescription_Type=OctetString
_CbbsmEventDescription_Object=MibScalar
cbbsmEventDescription=_CbbsmEventDescription_Object((1,3,6,1,4,1,9,9,358,1,1,1),_CbbsmEventDescription_Type())
cbbsmEventDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cbbsmEventDescription.setStatus(_B)
_CbbsmEventSource_Type=SnmpAdminString
_CbbsmEventSource_Object=MibScalar
cbbsmEventSource=_CbbsmEventSource_Object((1,3,6,1,4,1,9,9,358,1,1,2),_CbbsmEventSource_Type())
cbbsmEventSource.setMaxAccess(_C)
if mibBuilder.loadTexts:cbbsmEventSource.setStatus(_B)
_CbbsmEventID_Type=Unsigned32
_CbbsmEventID_Object=MibScalar
cbbsmEventID=_CbbsmEventID_Object((1,3,6,1,4,1,9,9,358,1,1,3),_CbbsmEventID_Type())
cbbsmEventID.setMaxAccess(_C)
if mibBuilder.loadTexts:cbbsmEventID.setStatus(_B)
class _CbbsmEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('error',1),('warning',2),('information',3)))
_CbbsmEventType_Type.__name__=_I
_CbbsmEventType_Object=MibScalar
cbbsmEventType=_CbbsmEventType_Object((1,3,6,1,4,1,9,9,358,1,1,4),_CbbsmEventType_Type())
cbbsmEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:cbbsmEventType.setStatus(_B)
_CbbsmEventTime_Type=DateAndTime
_CbbsmEventTime_Object=MibScalar
cbbsmEventTime=_CbbsmEventTime_Object((1,3,6,1,4,1,9,9,358,1,1,5),_CbbsmEventTime_Type())
cbbsmEventTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cbbsmEventTime.setStatus(_B)
_CiscoBbsmMIBConformance_ObjectIdentity=ObjectIdentity
ciscoBbsmMIBConformance=_CiscoBbsmMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,358,2))
_CiscoBbsmMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoBbsmMIBCompliances=_CiscoBbsmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,358,2,1))
_CiscoBbsmMIBGroups_ObjectIdentity=ObjectIdentity
ciscoBbsmMIBGroups=_CiscoBbsmMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,358,2,2))
ciscoBbsmMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,358,2,2,1))
ciscoBbsmMIBGroup.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:ciscoBbsmMIBGroup.setStatus(_B)
ciscoBbsmEvent=NotificationType((1,3,6,1,4,1,9,9,358,0,1))
ciscoBbsmEvent.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:ciscoBbsmEvent.setStatus(_B)
ciscoBbsmMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,358,2,2,2))
ciscoBbsmMIBNotificationGroup.setObjects((_A,_J))
if mibBuilder.loadTexts:ciscoBbsmMIBNotificationGroup.setStatus(_B)
ciscoBbsmMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,358,2,1,1))
ciscoBbsmMIBCompliance.setObjects(*((_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ciscoBbsmMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoBbsmMIB':ciscoBbsmMIB,'ciscoBbsmNotifications':ciscoBbsmNotifications,_J:ciscoBbsmEvent,'ciscoBbsmMIBObjects':ciscoBbsmMIBObjects,'ciscoBbsmEventInfo':ciscoBbsmEventInfo,_D:cbbsmEventDescription,_E:cbbsmEventSource,_F:cbbsmEventID,_G:cbbsmEventType,_H:cbbsmEventTime,'ciscoBbsmMIBConformance':ciscoBbsmMIBConformance,'ciscoBbsmMIBCompliances':ciscoBbsmMIBCompliances,'ciscoBbsmMIBCompliance':ciscoBbsmMIBCompliance,'ciscoBbsmMIBGroups':ciscoBbsmMIBGroups,_K:ciscoBbsmMIBGroup,_L:ciscoBbsmMIBNotificationGroup})