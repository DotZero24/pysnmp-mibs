_G='qtechNFPPNotificationsGroup'
_F='qtechNFPPNotifObjectsGroup'
_E='qtechNFPPMessageGenerated'
_D='OctetString'
_C='qtechNFPPMessageContent'
_B='current'
_A='QTECH-NFPP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qtechNFPPMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,43))
if mibBuilder.loadTexts:qtechNFPPMIB.setRevisions(('2009-07-09 00:00',))
_QtechNFPPMIBObjects_ObjectIdentity=ObjectIdentity
qtechNFPPMIBObjects=_QtechNFPPMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,43,1))
class _QtechNFPPMessageContent_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_QtechNFPPMessageContent_Type.__name__=_D
_QtechNFPPMessageContent_Object=MibScalar
qtechNFPPMessageContent=_QtechNFPPMessageContent_Object((1,3,6,1,4,1,27514,1,1,10,2,43,1,0),_QtechNFPPMessageContent_Type())
qtechNFPPMessageContent.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:qtechNFPPMessageContent.setStatus(_B)
_QtechNFPPMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
qtechNFPPMIBNotificationPrefix=_QtechNFPPMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,43,2))
_QtechNFPPMIBNotifications_ObjectIdentity=ObjectIdentity
qtechNFPPMIBNotifications=_QtechNFPPMIBNotifications_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,43,2,0))
_QtechNFPPMIBConformance_ObjectIdentity=ObjectIdentity
qtechNFPPMIBConformance=_QtechNFPPMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,43,3))
_QtechNFPPMIBCompliances_ObjectIdentity=ObjectIdentity
qtechNFPPMIBCompliances=_QtechNFPPMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,43,3,1))
_QtechNFPPMIBGroups_ObjectIdentity=ObjectIdentity
qtechNFPPMIBGroups=_QtechNFPPMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,43,3,2))
qtechNFPPNotifObjectsGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,43,3,2,1))
qtechNFPPNotifObjectsGroup.setObjects((_A,_C))
if mibBuilder.loadTexts:qtechNFPPNotifObjectsGroup.setStatus(_B)
qtechNFPPMessageGenerated=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,43,2,0,1))
qtechNFPPMessageGenerated.setObjects((_A,_C))
if mibBuilder.loadTexts:qtechNFPPMessageGenerated.setStatus(_B)
qtechNFPPNotificationsGroup=NotificationGroup((1,3,6,1,4,1,27514,1,1,10,2,43,3,2,2))
qtechNFPPNotificationsGroup.setObjects((_A,_E))
if mibBuilder.loadTexts:qtechNFPPNotificationsGroup.setStatus(_B)
qtechNFPPMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,43,3,1,1))
qtechNFPPMIBCompliance.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:qtechNFPPMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'qtechNFPPMIB':qtechNFPPMIB,'qtechNFPPMIBObjects':qtechNFPPMIBObjects,_C:qtechNFPPMessageContent,'qtechNFPPMIBNotificationPrefix':qtechNFPPMIBNotificationPrefix,'qtechNFPPMIBNotifications':qtechNFPPMIBNotifications,_E:qtechNFPPMessageGenerated,'qtechNFPPMIBConformance':qtechNFPPMIBConformance,'qtechNFPPMIBCompliances':qtechNFPPMIBCompliances,'qtechNFPPMIBCompliance':qtechNFPPMIBCompliance,'qtechNFPPMIBGroups':qtechNFPPMIBGroups,_F:qtechNFPPNotifObjectsGroup,_G:qtechNFPPNotificationsGroup})