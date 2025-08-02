_N='aristaCvNotificationsGroup'
_M='aristaCvObjectsGroup'
_L='aristaCvAlertResolvedNotification'
_K='aristaCvAlertFiringNotification'
_J='Integer32'
_I='aristaCvAlertSource'
_H='aristaCvAlertKey'
_G='aristaCvAlertTimestamp'
_F='aristaCvAlertSeverity'
_E='aristaCvAlertDescription'
_D='aristaCvAlertEventType'
_C='accessible-for-notify'
_B='current'
_A='ARISTA-CV-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
aristaCvMIB=ModuleIdentity((1,3,6,1,4,1,30065,3,33))
if mibBuilder.loadTexts:aristaCvMIB.setRevisions(('2022-07-27 00:00',))
class CvString(TextualConvention,OctetString):status=_B;displayHint='65535t'
_AristaCvNotifications_ObjectIdentity=ObjectIdentity
aristaCvNotifications=_AristaCvNotifications_ObjectIdentity((1,3,6,1,4,1,30065,3,33,0))
_AristaCvObjects_ObjectIdentity=ObjectIdentity
aristaCvObjects=_AristaCvObjects_ObjectIdentity((1,3,6,1,4,1,30065,3,33,1))
_AristaCvAlertEventType_Type=CvString
_AristaCvAlertEventType_Object=MibScalar
aristaCvAlertEventType=_AristaCvAlertEventType_Object((1,3,6,1,4,1,30065,3,33,1,1),_AristaCvAlertEventType_Type())
aristaCvAlertEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaCvAlertEventType.setStatus(_B)
_AristaCvAlertDescription_Type=CvString
_AristaCvAlertDescription_Object=MibScalar
aristaCvAlertDescription=_AristaCvAlertDescription_Object((1,3,6,1,4,1,30065,3,33,1,2),_AristaCvAlertDescription_Type())
aristaCvAlertDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaCvAlertDescription.setStatus(_B)
class _AristaCvAlertSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('info',1),('warning',2),('error',3),('critical',4)))
_AristaCvAlertSeverity_Type.__name__=_J
_AristaCvAlertSeverity_Object=MibScalar
aristaCvAlertSeverity=_AristaCvAlertSeverity_Object((1,3,6,1,4,1,30065,3,33,1,3),_AristaCvAlertSeverity_Type())
aristaCvAlertSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaCvAlertSeverity.setStatus(_B)
_AristaCvAlertTimestamp_Type=DateAndTime
_AristaCvAlertTimestamp_Object=MibScalar
aristaCvAlertTimestamp=_AristaCvAlertTimestamp_Object((1,3,6,1,4,1,30065,3,33,1,4),_AristaCvAlertTimestamp_Type())
aristaCvAlertTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaCvAlertTimestamp.setStatus(_B)
_AristaCvAlertKey_Type=CvString
_AristaCvAlertKey_Object=MibScalar
aristaCvAlertKey=_AristaCvAlertKey_Object((1,3,6,1,4,1,30065,3,33,1,5),_AristaCvAlertKey_Type())
aristaCvAlertKey.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaCvAlertKey.setStatus(_B)
_AristaCvAlertSource_Type=CvString
_AristaCvAlertSource_Object=MibScalar
aristaCvAlertSource=_AristaCvAlertSource_Object((1,3,6,1,4,1,30065,3,33,1,6),_AristaCvAlertSource_Type())
aristaCvAlertSource.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaCvAlertSource.setStatus(_B)
_AristaCvConformance_ObjectIdentity=ObjectIdentity
aristaCvConformance=_AristaCvConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,33,2))
_AristaCvCompliances_ObjectIdentity=ObjectIdentity
aristaCvCompliances=_AristaCvCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,33,2,1))
_AristaCvGroups_ObjectIdentity=ObjectIdentity
aristaCvGroups=_AristaCvGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,33,2,2))
aristaCvObjectsGroup=ObjectGroup((1,3,6,1,4,1,30065,3,33,2,2,1))
aristaCvObjectsGroup.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:aristaCvObjectsGroup.setStatus(_B)
aristaCvAlertFiringNotification=NotificationType((1,3,6,1,4,1,30065,3,33,0,1))
aristaCvAlertFiringNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:aristaCvAlertFiringNotification.setStatus(_B)
aristaCvAlertResolvedNotification=NotificationType((1,3,6,1,4,1,30065,3,33,0,2))
aristaCvAlertResolvedNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:aristaCvAlertResolvedNotification.setStatus(_B)
aristaCvNotificationsGroup=NotificationGroup((1,3,6,1,4,1,30065,3,33,2,2,2))
aristaCvNotificationsGroup.setObjects(*((_A,_K),(_A,_L)))
if mibBuilder.loadTexts:aristaCvNotificationsGroup.setStatus(_B)
aristaCvCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,33,2,1,1))
aristaCvCompliance.setObjects(*((_A,_M),(_A,_N)))
if mibBuilder.loadTexts:aristaCvCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CvString':CvString,'aristaCvMIB':aristaCvMIB,'aristaCvNotifications':aristaCvNotifications,_K:aristaCvAlertFiringNotification,_L:aristaCvAlertResolvedNotification,'aristaCvObjects':aristaCvObjects,_D:aristaCvAlertEventType,_E:aristaCvAlertDescription,_F:aristaCvAlertSeverity,_G:aristaCvAlertTimestamp,_H:aristaCvAlertKey,_I:aristaCvAlertSource,'aristaCvConformance':aristaCvConformance,'aristaCvCompliances':aristaCvCompliances,'aristaCvCompliance':aristaCvCompliance,'aristaCvGroups':aristaCvGroups,_M:aristaCvObjectsGroup,_N:aristaCvNotificationsGroup})