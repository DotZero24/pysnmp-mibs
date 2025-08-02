_J='nortelNMIinfoNotification'
_I='nortelNMInotifyLogTimeStamp'
_H='nortelNMInotifyLogText'
_G='nortelNMInotifyLogComponentId'
_F='DisplayString'
_E='nortelNMIcurrentTxNotificationSequenceNum'
_D='NORTEL-NMI-NOTIFICATIONS-MIB'
_C='accessible-for-notify'
_B='NORTEL-NMI-INFO-NOTI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nortelNMInotificationGroups,=mibBuilder.importSymbols('NORTEL-NMI-GROUPS-MIB','nortelNMInotificationGroups')
nortelNMIcurrentTxNotificationSequenceNum,nortelNMInotificationsMIB,nortelNMInotifyNeAdminState,nortelNMInotifyNeName,nortelNMInotifyNeOperState,nortelNMInotifyNeType,nortelNMInotifyNeUnknownStatus=mibBuilder.importSymbols(_D,_E,'nortelNMInotificationsMIB','nortelNMInotifyNeAdminState','nortelNMInotifyNeName','nortelNMInotifyNeOperState','nortelNMInotifyNeType','nortelNMInotifyNeUnknownStatus')
NortelNMItimeStampDef,=mibBuilder.importSymbols('NORTEL-NMI-TC-MIB','NortelNMItimeStampDef')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
nortelNMIinfoNotiMIB=ModuleIdentity((1,3,6,1,4,1,562,29,1,6,5))
_NortelNMIinfoNotiPrefix_ObjectIdentity=ObjectIdentity
nortelNMIinfoNotiPrefix=_NortelNMIinfoNotiPrefix_ObjectIdentity((1,3,6,1,4,1,562,29,1,6,5,0))
if mibBuilder.loadTexts:nortelNMIinfoNotiPrefix.setStatus(_A)
_NortelNMIinfoNotiVarbinds_ObjectIdentity=ObjectIdentity
nortelNMIinfoNotiVarbinds=_NortelNMIinfoNotiVarbinds_ObjectIdentity((1,3,6,1,4,1,562,29,1,6,5,1))
if mibBuilder.loadTexts:nortelNMIinfoNotiVarbinds.setStatus(_A)
_NortelNMInotifyLogComponentId_Type=DisplayString
_NortelNMInotifyLogComponentId_Object=MibScalar
nortelNMInotifyLogComponentId=_NortelNMInotifyLogComponentId_Object((1,3,6,1,4,1,562,29,1,6,5,1,1),_NortelNMInotifyLogComponentId_Type())
nortelNMInotifyLogComponentId.setMaxAccess(_C)
if mibBuilder.loadTexts:nortelNMInotifyLogComponentId.setStatus(_A)
class _NortelNMInotifyLogText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_NortelNMInotifyLogText_Type.__name__=_F
_NortelNMInotifyLogText_Object=MibScalar
nortelNMInotifyLogText=_NortelNMInotifyLogText_Object((1,3,6,1,4,1,562,29,1,6,5,1,2),_NortelNMInotifyLogText_Type())
nortelNMInotifyLogText.setMaxAccess(_C)
if mibBuilder.loadTexts:nortelNMInotifyLogText.setStatus(_A)
_NortelNMInotifyLogTimeStamp_Type=NortelNMItimeStampDef
_NortelNMInotifyLogTimeStamp_Object=MibScalar
nortelNMInotifyLogTimeStamp=_NortelNMInotifyLogTimeStamp_Object((1,3,6,1,4,1,562,29,1,6,5,1,3),_NortelNMInotifyLogTimeStamp_Type())
nortelNMInotifyLogTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:nortelNMInotifyLogTimeStamp.setStatus(_A)
nortelNMIinfoNotification=NotificationType((1,3,6,1,4,1,562,29,1,6,5,0,301))
nortelNMIinfoNotification.setObjects(*((_D,_E),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:nortelNMIinfoNotification.setStatus(_A)
nortelNMIneLogNotificationsGroup=NotificationGroup((1,3,6,1,4,1,562,29,1,2,1,2,5))
nortelNMIneLogNotificationsGroup.setObjects((_B,_J))
if mibBuilder.loadTexts:nortelNMIneLogNotificationsGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'nortelNMIneLogNotificationsGroup':nortelNMIneLogNotificationsGroup,'nortelNMIinfoNotiMIB':nortelNMIinfoNotiMIB,'nortelNMIinfoNotiPrefix':nortelNMIinfoNotiPrefix,_J:nortelNMIinfoNotification,'nortelNMIinfoNotiVarbinds':nortelNMIinfoNotiVarbinds,_G:nortelNMInotifyLogComponentId,_H:nortelNMInotifyLogText,_I:nortelNMInotifyLogTimeStamp})