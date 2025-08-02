_U='nortelNMIneAttributeChangeNotification'
_T='nortelNMIneDeEnrolNotification'
_S='nortelNMIneEnrolNotification'
_R='nortelNMInotifyNeDataChangeTime'
_Q='nortelNMInotifyNeDeEnrolTime'
_P='nortelNMInotifyNeEnrolTime'
_O='nortelNMInotifyNeUnknownStatus'
_N='nortelNMInotifyNeOperState'
_M='nortelNMInotifyNeAdminState'
_L='nortelNMInotifyNeLocationName'
_K='nortelNMInotifyNeVendorName'
_J='nortelNMInotifyNeVersionInfo'
_I='nortelNMInotifyNeIPaddress'
_H='DisplayString'
_G='nortelNMInotifyNeType'
_F='nortelNMInotifyNeName'
_E='nortelNMIcurrentTxNotificationSequenceNum'
_D='accessible-for-notify'
_C='NORTEL-NMI-NOTIFICATIONS-MIB'
_B='current'
_A='NORTEL-NMI-CONFIG-NOTI-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nortelNMInotificationGroups,=mibBuilder.importSymbols('NORTEL-NMI-GROUPS-MIB','nortelNMInotificationGroups')
nortelNMIcurrentTxNotificationSequenceNum,nortelNMInotificationsMIB,nortelNMInotifyNeAdminState,nortelNMInotifyNeName,nortelNMInotifyNeOperState,nortelNMInotifyNeType,nortelNMInotifyNeUnknownStatus=mibBuilder.importSymbols(_C,_E,'nortelNMInotificationsMIB',_M,_F,_N,_G,_O)
NortelNMItimeStampDef,=mibBuilder.importSymbols('NORTEL-NMI-TC-MIB','NortelNMItimeStampDef')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
nortelNMIconfigNotiMIB=ModuleIdentity((1,3,6,1,4,1,562,29,1,6,3))
if mibBuilder.loadTexts:nortelNMIconfigNotiMIB.setRevisions(('1999-06-24 00:00','1999-05-31 00:00','1999-04-12 00:00','1999-03-22 00:00'))
_NortelNMIconfigNotiPrefix_ObjectIdentity=ObjectIdentity
nortelNMIconfigNotiPrefix=_NortelNMIconfigNotiPrefix_ObjectIdentity((1,3,6,1,4,1,562,29,1,6,3,0))
if mibBuilder.loadTexts:nortelNMIconfigNotiPrefix.setStatus(_B)
_NortelNMIconfigNotiVarbinds_ObjectIdentity=ObjectIdentity
nortelNMIconfigNotiVarbinds=_NortelNMIconfigNotiVarbinds_ObjectIdentity((1,3,6,1,4,1,562,29,1,6,3,1))
if mibBuilder.loadTexts:nortelNMIconfigNotiVarbinds.setStatus(_B)
_NortelNMInotifyNeDeEnrolTime_Type=NortelNMItimeStampDef
_NortelNMInotifyNeDeEnrolTime_Object=MibScalar
nortelNMInotifyNeDeEnrolTime=_NortelNMInotifyNeDeEnrolTime_Object((1,3,6,1,4,1,562,29,1,6,3,1,1),_NortelNMInotifyNeDeEnrolTime_Type())
nortelNMInotifyNeDeEnrolTime.setMaxAccess(_D)
if mibBuilder.loadTexts:nortelNMInotifyNeDeEnrolTime.setStatus(_B)
_NortelNMInotifyNeEnrolTime_Type=NortelNMItimeStampDef
_NortelNMInotifyNeEnrolTime_Object=MibScalar
nortelNMInotifyNeEnrolTime=_NortelNMInotifyNeEnrolTime_Object((1,3,6,1,4,1,562,29,1,6,3,1,2),_NortelNMInotifyNeEnrolTime_Type())
nortelNMInotifyNeEnrolTime.setMaxAccess(_D)
if mibBuilder.loadTexts:nortelNMInotifyNeEnrolTime.setStatus(_B)
_NortelNMInotifyNeIPaddress_Type=IpAddress
_NortelNMInotifyNeIPaddress_Object=MibScalar
nortelNMInotifyNeIPaddress=_NortelNMInotifyNeIPaddress_Object((1,3,6,1,4,1,562,29,1,6,3,1,3),_NortelNMInotifyNeIPaddress_Type())
nortelNMInotifyNeIPaddress.setMaxAccess(_D)
if mibBuilder.loadTexts:nortelNMInotifyNeIPaddress.setStatus(_B)
class _NortelNMInotifyNeVersionInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_NortelNMInotifyNeVersionInfo_Type.__name__=_H
_NortelNMInotifyNeVersionInfo_Object=MibScalar
nortelNMInotifyNeVersionInfo=_NortelNMInotifyNeVersionInfo_Object((1,3,6,1,4,1,562,29,1,6,3,1,4),_NortelNMInotifyNeVersionInfo_Type())
nortelNMInotifyNeVersionInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:nortelNMInotifyNeVersionInfo.setStatus(_B)
class _NortelNMInotifyNeVendorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_NortelNMInotifyNeVendorName_Type.__name__=_H
_NortelNMInotifyNeVendorName_Object=MibScalar
nortelNMInotifyNeVendorName=_NortelNMInotifyNeVendorName_Object((1,3,6,1,4,1,562,29,1,6,3,1,5),_NortelNMInotifyNeVendorName_Type())
nortelNMInotifyNeVendorName.setMaxAccess(_D)
if mibBuilder.loadTexts:nortelNMInotifyNeVendorName.setStatus(_B)
class _NortelNMInotifyNeLocationName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_NortelNMInotifyNeLocationName_Type.__name__=_H
_NortelNMInotifyNeLocationName_Object=MibScalar
nortelNMInotifyNeLocationName=_NortelNMInotifyNeLocationName_Object((1,3,6,1,4,1,562,29,1,6,3,1,6),_NortelNMInotifyNeLocationName_Type())
nortelNMInotifyNeLocationName.setMaxAccess(_D)
if mibBuilder.loadTexts:nortelNMInotifyNeLocationName.setStatus(_B)
_NortelNMInotifyNeDataChangeTime_Type=NortelNMItimeStampDef
_NortelNMInotifyNeDataChangeTime_Object=MibScalar
nortelNMInotifyNeDataChangeTime=_NortelNMInotifyNeDataChangeTime_Object((1,3,6,1,4,1,562,29,1,6,3,1,7),_NortelNMInotifyNeDataChangeTime_Type())
nortelNMInotifyNeDataChangeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:nortelNMInotifyNeDataChangeTime.setStatus(_B)
nortelNMIneEnrolNotification=NotificationType((1,3,6,1,4,1,562,29,1,6,3,0,11))
nortelNMIneEnrolNotification.setObjects(*((_C,_E),(_C,_G),(_C,_F),(_A,_P),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_C,_M),(_C,_N),(_C,_O)))
if mibBuilder.loadTexts:nortelNMIneEnrolNotification.setStatus(_B)
nortelNMIneDeEnrolNotification=NotificationType((1,3,6,1,4,1,562,29,1,6,3,0,12))
nortelNMIneDeEnrolNotification.setObjects(*((_C,_E),(_C,_G),(_C,_F),(_A,_Q)))
if mibBuilder.loadTexts:nortelNMIneDeEnrolNotification.setStatus(_B)
nortelNMIneAttributeChangeNotification=NotificationType((1,3,6,1,4,1,562,29,1,6,3,0,13))
nortelNMIneAttributeChangeNotification.setObjects(*((_C,_E),(_C,_G),(_C,_F),(_A,_R),(_A,_J),(_A,_K),(_A,_L),(_A,_I)))
if mibBuilder.loadTexts:nortelNMIneAttributeChangeNotification.setStatus(_B)
nortelNMIneRegistrationNotificationGroup=NotificationGroup((1,3,6,1,4,1,562,29,1,2,1,2,1))
nortelNMIneRegistrationNotificationGroup.setObjects(*((_A,_S),(_A,_T)))
if mibBuilder.loadTexts:nortelNMIneRegistrationNotificationGroup.setStatus(_B)
nortelNMIneAttrChangeNotificationGroup=NotificationGroup((1,3,6,1,4,1,562,29,1,2,1,2,2))
nortelNMIneAttrChangeNotificationGroup.setObjects((_A,_U))
if mibBuilder.loadTexts:nortelNMIneAttrChangeNotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'nortelNMIneRegistrationNotificationGroup':nortelNMIneRegistrationNotificationGroup,'nortelNMIneAttrChangeNotificationGroup':nortelNMIneAttrChangeNotificationGroup,'nortelNMIconfigNotiMIB':nortelNMIconfigNotiMIB,'nortelNMIconfigNotiPrefix':nortelNMIconfigNotiPrefix,_S:nortelNMIneEnrolNotification,_T:nortelNMIneDeEnrolNotification,_U:nortelNMIneAttributeChangeNotification,'nortelNMIconfigNotiVarbinds':nortelNMIconfigNotiVarbinds,_Q:nortelNMInotifyNeDeEnrolTime,_P:nortelNMInotifyNeEnrolTime,_I:nortelNMInotifyNeIPaddress,_J:nortelNMInotifyNeVersionInfo,_K:nortelNMInotifyNeVendorName,_L:nortelNMInotifyNeLocationName,_R:nortelNMInotifyNeDataChangeTime})