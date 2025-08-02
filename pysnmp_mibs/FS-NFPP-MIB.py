_G='fsNFPPNotificationsGroup'
_F='fsNFPPNotifObjectsGroup'
_E='fsNFPPMessageGenerated'
_D='OctetString'
_C='fsNFPPMessageContent'
_B='current'
_A='FS-NFPP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsNFPPMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,43))
if mibBuilder.loadTexts:fsNFPPMIB.setRevisions(('2009-07-09 00:00',))
_FsNFPPMIBObjects_ObjectIdentity=ObjectIdentity
fsNFPPMIBObjects=_FsNFPPMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,43,1))
class _FsNFPPMessageContent_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_FsNFPPMessageContent_Type.__name__=_D
_FsNFPPMessageContent_Object=MibScalar
fsNFPPMessageContent=_FsNFPPMessageContent_Object((1,3,6,1,4,1,52642,1,1,10,2,43,1,0),_FsNFPPMessageContent_Type())
fsNFPPMessageContent.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:fsNFPPMessageContent.setStatus(_B)
_FsNFPPMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
fsNFPPMIBNotificationPrefix=_FsNFPPMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,43,2))
_FsNFPPMIBNotifications_ObjectIdentity=ObjectIdentity
fsNFPPMIBNotifications=_FsNFPPMIBNotifications_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,43,2,0))
_FsNFPPMIBConformance_ObjectIdentity=ObjectIdentity
fsNFPPMIBConformance=_FsNFPPMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,43,3))
_FsNFPPMIBCompliances_ObjectIdentity=ObjectIdentity
fsNFPPMIBCompliances=_FsNFPPMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,43,3,1))
_FsNFPPMIBGroups_ObjectIdentity=ObjectIdentity
fsNFPPMIBGroups=_FsNFPPMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,43,3,2))
fsNFPPNotifObjectsGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,43,3,2,1))
fsNFPPNotifObjectsGroup.setObjects((_A,_C))
if mibBuilder.loadTexts:fsNFPPNotifObjectsGroup.setStatus(_B)
fsNFPPMessageGenerated=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,43,2,0,1))
fsNFPPMessageGenerated.setObjects((_A,_C))
if mibBuilder.loadTexts:fsNFPPMessageGenerated.setStatus(_B)
fsNFPPNotificationsGroup=NotificationGroup((1,3,6,1,4,1,52642,1,1,10,2,43,3,2,2))
fsNFPPNotificationsGroup.setObjects((_A,_E))
if mibBuilder.loadTexts:fsNFPPNotificationsGroup.setStatus(_B)
fsNFPPMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,43,3,1,1))
fsNFPPMIBCompliance.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:fsNFPPMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'fsNFPPMIB':fsNFPPMIB,'fsNFPPMIBObjects':fsNFPPMIBObjects,_C:fsNFPPMessageContent,'fsNFPPMIBNotificationPrefix':fsNFPPMIBNotificationPrefix,'fsNFPPMIBNotifications':fsNFPPMIBNotifications,_E:fsNFPPMessageGenerated,'fsNFPPMIBConformance':fsNFPPMIBConformance,'fsNFPPMIBCompliances':fsNFPPMIBCompliances,'fsNFPPMIBCompliance':fsNFPPMIBCompliance,'fsNFPPMIBGroups':fsNFPPMIBGroups,_F:fsNFPPNotifObjectsGroup,_G:fsNFPPNotificationsGroup})