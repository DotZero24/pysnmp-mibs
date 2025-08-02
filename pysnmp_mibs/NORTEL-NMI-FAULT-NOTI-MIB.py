_a='nortelNMIcriticalAlarmNotification'
_Z='nortelNMImajorAlarmNotification'
_Y='nortelNMIminorAlarmNotification'
_X='nortelNMIwarningAlarmNotification'
_W='nortelNMIalarmClearNotification'
_V='nortelNMIneOSIstateChangeNotification'
_U='nortelNMInotifyNeStateChangeTime'
_T='Unsigned32'
_S='nortelNMInotifyNeUnknownStatus'
_R='nortelNMInotifyNeType'
_Q='nortelNMInotifyNeOperState'
_P='nortelNMInotifyNeName'
_O='nortelNMInotifyNeAdminState'
_N='DisplayString'
_M='nortelNMInotifyAlarmSpecificProblem'
_L='nortelNMInotifyAlarmProbableCause'
_K='nortelNMInotifyAlarmNotificationID'
_J='nortelNMInotifyAlarmCategory'
_I='nortelNMInotifyAlarmCorrelationIdList'
_H='nortelNMInotifyAlarmTimeStamp'
_G='nortelNMInotifyAlarmDescription'
_F='nortelNMInotifyAlarmComponentId'
_E='nortelNMIcurrentTxNotificationSequenceNum'
_D='accessible-for-notify'
_C='NORTEL-NMI-NOTIFICATIONS-MIB'
_B='current'
_A='NORTEL-NMI-FAULT-NOTI-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nortelNMInotificationGroups,=mibBuilder.importSymbols('NORTEL-NMI-GROUPS-MIB','nortelNMInotificationGroups')
nortelNMIcurrentTxNotificationSequenceNum,nortelNMInotificationsMIB,nortelNMInotifyNeAdminState,nortelNMInotifyNeName,nortelNMInotifyNeOperState,nortelNMInotifyNeType,nortelNMInotifyNeUnknownStatus=mibBuilder.importSymbols(_C,_E,'nortelNMInotificationsMIB',_O,_P,_Q,_R,_S)
NortelNMIalarmProbableCause,NortelNMIalarmProblemCategory,NortelNMItimeStampDef=mibBuilder.importSymbols('NORTEL-NMI-TC-MIB','NortelNMIalarmProbableCause','NortelNMIalarmProblemCategory','NortelNMItimeStampDef')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_T,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_N,'PhysAddress','TextualConvention')
nortelNMIfaultNotiMIB=ModuleIdentity((1,3,6,1,4,1,562,29,1,6,4))
if mibBuilder.loadTexts:nortelNMIfaultNotiMIB.setRevisions(('1999-07-19 00:00','1999-06-24 00:00','1999-05-31 00:00','1999-04-12 00:00','1999-03-22 00:00'))
_NortelNMIfaultNotiPrefix_ObjectIdentity=ObjectIdentity
nortelNMIfaultNotiPrefix=_NortelNMIfaultNotiPrefix_ObjectIdentity((1,3,6,1,4,1,562,29,1,6,4,0))
if mibBuilder.loadTexts:nortelNMIfaultNotiPrefix.setStatus(_B)
_NortelNMIfaultNotiVarbinds_ObjectIdentity=ObjectIdentity
nortelNMIfaultNotiVarbinds=_NortelNMIfaultNotiVarbinds_ObjectIdentity((1,3,6,1,4,1,562,29,1,6,4,1))
if mibBuilder.loadTexts:nortelNMIfaultNotiVarbinds.setStatus(_B)
_NortelNMInotifyAlarmComponentId_Type=DisplayString
_NortelNMInotifyAlarmComponentId_Object=MibScalar
nortelNMInotifyAlarmComponentId=_NortelNMInotifyAlarmComponentId_Object((1,3,6,1,4,1,562,29,1,6,4,1,1),_NortelNMInotifyAlarmComponentId_Type())
nortelNMInotifyAlarmComponentId.setMaxAccess(_D)
if mibBuilder.loadTexts:nortelNMInotifyAlarmComponentId.setStatus(_B)
_NortelNMInotifyAlarmCategory_Type=NortelNMIalarmProblemCategory
_NortelNMInotifyAlarmCategory_Object=MibScalar
nortelNMInotifyAlarmCategory=_NortelNMInotifyAlarmCategory_Object((1,3,6,1,4,1,562,29,1,6,4,1,2),_NortelNMInotifyAlarmCategory_Type())
nortelNMInotifyAlarmCategory.setMaxAccess(_D)
if mibBuilder.loadTexts:nortelNMInotifyAlarmCategory.setStatus(_B)
class _NortelNMInotifyAlarmNotificationID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1073741824))
_NortelNMInotifyAlarmNotificationID_Type.__name__=_T
_NortelNMInotifyAlarmNotificationID_Object=MibScalar
nortelNMInotifyAlarmNotificationID=_NortelNMInotifyAlarmNotificationID_Object((1,3,6,1,4,1,562,29,1,6,4,1,3),_NortelNMInotifyAlarmNotificationID_Type())
nortelNMInotifyAlarmNotificationID.setMaxAccess(_D)
if mibBuilder.loadTexts:nortelNMInotifyAlarmNotificationID.setStatus(_B)
class _NortelNMInotifyAlarmDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_NortelNMInotifyAlarmDescription_Type.__name__=_N
_NortelNMInotifyAlarmDescription_Object=MibScalar
nortelNMInotifyAlarmDescription=_NortelNMInotifyAlarmDescription_Object((1,3,6,1,4,1,562,29,1,6,4,1,4),_NortelNMInotifyAlarmDescription_Type())
nortelNMInotifyAlarmDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:nortelNMInotifyAlarmDescription.setStatus(_B)
_NortelNMInotifyAlarmTimeStamp_Type=NortelNMItimeStampDef
_NortelNMInotifyAlarmTimeStamp_Object=MibScalar
nortelNMInotifyAlarmTimeStamp=_NortelNMInotifyAlarmTimeStamp_Object((1,3,6,1,4,1,562,29,1,6,4,1,5),_NortelNMInotifyAlarmTimeStamp_Type())
nortelNMInotifyAlarmTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:nortelNMInotifyAlarmTimeStamp.setStatus(_B)
_NortelNMInotifyAlarmProbableCause_Type=NortelNMIalarmProbableCause
_NortelNMInotifyAlarmProbableCause_Object=MibScalar
nortelNMInotifyAlarmProbableCause=_NortelNMInotifyAlarmProbableCause_Object((1,3,6,1,4,1,562,29,1,6,4,1,6),_NortelNMInotifyAlarmProbableCause_Type())
nortelNMInotifyAlarmProbableCause.setMaxAccess(_D)
if mibBuilder.loadTexts:nortelNMInotifyAlarmProbableCause.setStatus(_B)
class _NortelNMInotifyAlarmSpecificProblem_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_NortelNMInotifyAlarmSpecificProblem_Type.__name__=_N
_NortelNMInotifyAlarmSpecificProblem_Object=MibScalar
nortelNMInotifyAlarmSpecificProblem=_NortelNMInotifyAlarmSpecificProblem_Object((1,3,6,1,4,1,562,29,1,6,4,1,7),_NortelNMInotifyAlarmSpecificProblem_Type())
nortelNMInotifyAlarmSpecificProblem.setMaxAccess(_D)
if mibBuilder.loadTexts:nortelNMInotifyAlarmSpecificProblem.setStatus(_B)
_NortelNMInotifyAlarmCorrelationIdList_Type=DisplayString
_NortelNMInotifyAlarmCorrelationIdList_Object=MibScalar
nortelNMInotifyAlarmCorrelationIdList=_NortelNMInotifyAlarmCorrelationIdList_Object((1,3,6,1,4,1,562,29,1,6,4,1,8),_NortelNMInotifyAlarmCorrelationIdList_Type())
nortelNMInotifyAlarmCorrelationIdList.setMaxAccess(_D)
if mibBuilder.loadTexts:nortelNMInotifyAlarmCorrelationIdList.setStatus(_B)
_NortelNMInotifyNeStateChangeTime_Type=NortelNMItimeStampDef
_NortelNMInotifyNeStateChangeTime_Object=MibScalar
nortelNMInotifyNeStateChangeTime=_NortelNMInotifyNeStateChangeTime_Object((1,3,6,1,4,1,562,29,1,6,4,1,9),_NortelNMInotifyNeStateChangeTime_Type())
nortelNMInotifyNeStateChangeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:nortelNMInotifyNeStateChangeTime.setStatus(_B)
nortelNMIneOSIstateChangeNotification=NotificationType((1,3,6,1,4,1,562,29,1,6,4,0,101))
nortelNMIneOSIstateChangeNotification.setObjects(*((_C,_E),(_C,_R),(_C,_P),(_A,_U),(_C,_O),(_C,_Q),(_C,_S)))
if mibBuilder.loadTexts:nortelNMIneOSIstateChangeNotification.setStatus(_B)
nortelNMIalarmClearNotification=NotificationType((1,3,6,1,4,1,562,29,1,6,4,0,201))
nortelNMIalarmClearNotification.setObjects(*((_C,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:nortelNMIalarmClearNotification.setStatus(_B)
nortelNMIwarningAlarmNotification=NotificationType((1,3,6,1,4,1,562,29,1,6,4,0,202))
nortelNMIwarningAlarmNotification.setObjects(*((_C,_E),(_A,_F),(_A,_J),(_A,_K),(_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_I)))
if mibBuilder.loadTexts:nortelNMIwarningAlarmNotification.setStatus(_B)
nortelNMIminorAlarmNotification=NotificationType((1,3,6,1,4,1,562,29,1,6,4,0,203))
nortelNMIminorAlarmNotification.setObjects(*((_C,_E),(_A,_F),(_A,_J),(_A,_K),(_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_I)))
if mibBuilder.loadTexts:nortelNMIminorAlarmNotification.setStatus(_B)
nortelNMImajorAlarmNotification=NotificationType((1,3,6,1,4,1,562,29,1,6,4,0,204))
nortelNMImajorAlarmNotification.setObjects(*((_C,_E),(_A,_F),(_A,_J),(_A,_K),(_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_I)))
if mibBuilder.loadTexts:nortelNMImajorAlarmNotification.setStatus(_B)
nortelNMIcriticalAlarmNotification=NotificationType((1,3,6,1,4,1,562,29,1,6,4,0,205))
nortelNMIcriticalAlarmNotification.setObjects(*((_C,_E),(_A,_F),(_A,_J),(_A,_K),(_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_I)))
if mibBuilder.loadTexts:nortelNMIcriticalAlarmNotification.setStatus(_B)
nortelNMIneStateChangeNotificationGroup=NotificationGroup((1,3,6,1,4,1,562,29,1,2,1,2,3))
nortelNMIneStateChangeNotificationGroup.setObjects((_A,_V))
if mibBuilder.loadTexts:nortelNMIneStateChangeNotificationGroup.setStatus(_B)
nortelNMIneAlarmNotificationsGroup=NotificationGroup((1,3,6,1,4,1,562,29,1,2,1,2,4))
nortelNMIneAlarmNotificationsGroup.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:nortelNMIneAlarmNotificationsGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'nortelNMIneStateChangeNotificationGroup':nortelNMIneStateChangeNotificationGroup,'nortelNMIneAlarmNotificationsGroup':nortelNMIneAlarmNotificationsGroup,'nortelNMIfaultNotiMIB':nortelNMIfaultNotiMIB,'nortelNMIfaultNotiPrefix':nortelNMIfaultNotiPrefix,_V:nortelNMIneOSIstateChangeNotification,_W:nortelNMIalarmClearNotification,_X:nortelNMIwarningAlarmNotification,_Y:nortelNMIminorAlarmNotification,_Z:nortelNMImajorAlarmNotification,_a:nortelNMIcriticalAlarmNotification,'nortelNMIfaultNotiVarbinds':nortelNMIfaultNotiVarbinds,_F:nortelNMInotifyAlarmComponentId,_J:nortelNMInotifyAlarmCategory,_K:nortelNMInotifyAlarmNotificationID,_G:nortelNMInotifyAlarmDescription,_H:nortelNMInotifyAlarmTimeStamp,_L:nortelNMInotifyAlarmProbableCause,_M:nortelNMInotifyAlarmSpecificProblem,_I:nortelNMInotifyAlarmCorrelationIdList,_U:nortelNMInotifyNeStateChangeTime})