_O='ntcNotifConfGrpRepV1Standard'
_N='ntcNotifConfGrpFldV1Standard'
_M='ntcNotifAlReport'
_L='ntcNotifFldAlarmStatus'
_K='ntcNotifFldDescription'
_J='ntcNotifFldObjectId'
_I='ntcNotifFldObjectName'
_H='ntcNotifFldFunctionId'
_G='ntcNotifFldFunctionName'
_F='ntcNotifFldDevice'
_E='ntcNotifFldSeverity'
_D='ntcNotifFldSeqNbr'
_C='accessible-for-notify'
_B='current'
_A='NEWTEC-NOTIFICATION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcEvent,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcEvent')
NtcAlarmState,=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntcNotification=ModuleIdentity((1,3,6,1,4,1,5835,5,3,2))
if mibBuilder.loadTexts:ntcNotification.setRevisions(('2012-06-28 12:00','2012-05-16 12:35'))
_NtcNotifObjects_ObjectIdentity=ObjectIdentity
ntcNotifObjects=_NtcNotifObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,3,2,1))
if mibBuilder.loadTexts:ntcNotifObjects.setStatus(_B)
_NtcNotifReportList_ObjectIdentity=ObjectIdentity
ntcNotifReportList=_NtcNotifReportList_ObjectIdentity((1,3,6,1,4,1,5835,5,3,2,1,0))
if mibBuilder.loadTexts:ntcNotifReportList.setStatus(_B)
_NtcNotifField_ObjectIdentity=ObjectIdentity
ntcNotifField=_NtcNotifField_ObjectIdentity((1,3,6,1,4,1,5835,5,3,2,1,1))
if mibBuilder.loadTexts:ntcNotifField.setStatus(_B)
_NtcNotifFldSeqNbr_Type=Counter32
_NtcNotifFldSeqNbr_Object=MibScalar
ntcNotifFldSeqNbr=_NtcNotifFldSeqNbr_Object((1,3,6,1,4,1,5835,5,3,2,1,1,1),_NtcNotifFldSeqNbr_Type())
ntcNotifFldSeqNbr.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcNotifFldSeqNbr.setStatus(_B)
_NtcNotifFldSeverity_Type=DisplayString
_NtcNotifFldSeverity_Object=MibScalar
ntcNotifFldSeverity=_NtcNotifFldSeverity_Object((1,3,6,1,4,1,5835,5,3,2,1,1,2),_NtcNotifFldSeverity_Type())
ntcNotifFldSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcNotifFldSeverity.setStatus(_B)
_NtcNotifFldDevice_Type=DisplayString
_NtcNotifFldDevice_Object=MibScalar
ntcNotifFldDevice=_NtcNotifFldDevice_Object((1,3,6,1,4,1,5835,5,3,2,1,1,3),_NtcNotifFldDevice_Type())
ntcNotifFldDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcNotifFldDevice.setStatus(_B)
_NtcNotifFldFunctionName_Type=DisplayString
_NtcNotifFldFunctionName_Object=MibScalar
ntcNotifFldFunctionName=_NtcNotifFldFunctionName_Object((1,3,6,1,4,1,5835,5,3,2,1,1,4),_NtcNotifFldFunctionName_Type())
ntcNotifFldFunctionName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcNotifFldFunctionName.setStatus(_B)
_NtcNotifFldFunctionId_Type=ObjectIdentifier
_NtcNotifFldFunctionId_Object=MibScalar
ntcNotifFldFunctionId=_NtcNotifFldFunctionId_Object((1,3,6,1,4,1,5835,5,3,2,1,1,5),_NtcNotifFldFunctionId_Type())
ntcNotifFldFunctionId.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcNotifFldFunctionId.setStatus(_B)
_NtcNotifFldObjectName_Type=DisplayString
_NtcNotifFldObjectName_Object=MibScalar
ntcNotifFldObjectName=_NtcNotifFldObjectName_Object((1,3,6,1,4,1,5835,5,3,2,1,1,6),_NtcNotifFldObjectName_Type())
ntcNotifFldObjectName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcNotifFldObjectName.setStatus(_B)
_NtcNotifFldObjectId_Type=ObjectIdentifier
_NtcNotifFldObjectId_Object=MibScalar
ntcNotifFldObjectId=_NtcNotifFldObjectId_Object((1,3,6,1,4,1,5835,5,3,2,1,1,7),_NtcNotifFldObjectId_Type())
ntcNotifFldObjectId.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcNotifFldObjectId.setStatus(_B)
_NtcNotifFldDescription_Type=DisplayString
_NtcNotifFldDescription_Object=MibScalar
ntcNotifFldDescription=_NtcNotifFldDescription_Object((1,3,6,1,4,1,5835,5,3,2,1,1,8),_NtcNotifFldDescription_Type())
ntcNotifFldDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcNotifFldDescription.setStatus(_B)
_NtcNotifFldAlarmStatus_Type=NtcAlarmState
_NtcNotifFldAlarmStatus_Object=MibScalar
ntcNotifFldAlarmStatus=_NtcNotifFldAlarmStatus_Object((1,3,6,1,4,1,5835,5,3,2,1,1,9),_NtcNotifFldAlarmStatus_Type())
ntcNotifFldAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcNotifFldAlarmStatus.setStatus(_B)
_NtcNotifConformance_ObjectIdentity=ObjectIdentity
ntcNotifConformance=_NtcNotifConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,3,2,2))
if mibBuilder.loadTexts:ntcNotifConformance.setStatus(_B)
_NtcNotifConfGroup_ObjectIdentity=ObjectIdentity
ntcNotifConfGroup=_NtcNotifConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,3,2,2,1))
if mibBuilder.loadTexts:ntcNotifConfGroup.setStatus(_B)
_NtcNotifConfCompliance_ObjectIdentity=ObjectIdentity
ntcNotifConfCompliance=_NtcNotifConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,3,2,2,2))
if mibBuilder.loadTexts:ntcNotifConfCompliance.setStatus(_B)
ntcNotifConfGrpFldV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,3,2,2,1,1))
ntcNotifConfGrpFldV1Standard.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ntcNotifConfGrpFldV1Standard.setStatus(_B)
ntcNotifAlReport=NotificationType((1,3,6,1,4,1,5835,5,3,2,1,0,1))
ntcNotifAlReport.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ntcNotifAlReport.setStatus(_B)
ntcNotifConfGrpRepV1Standard=NotificationGroup((1,3,6,1,4,1,5835,5,3,2,2,1,2))
ntcNotifConfGrpRepV1Standard.setObjects((_A,_M))
if mibBuilder.loadTexts:ntcNotifConfGrpRepV1Standard.setStatus(_B)
ntcNotifConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,3,2,2,2,1))
ntcNotifConfCompV1Standard.setObjects(*((_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ntcNotifConfCompV1Standard.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ntcNotification':ntcNotification,'ntcNotifObjects':ntcNotifObjects,'ntcNotifReportList':ntcNotifReportList,_M:ntcNotifAlReport,'ntcNotifField':ntcNotifField,_D:ntcNotifFldSeqNbr,_E:ntcNotifFldSeverity,_F:ntcNotifFldDevice,_G:ntcNotifFldFunctionName,_H:ntcNotifFldFunctionId,_I:ntcNotifFldObjectName,_J:ntcNotifFldObjectId,_K:ntcNotifFldDescription,_L:ntcNotifFldAlarmStatus,'ntcNotifConformance':ntcNotifConformance,'ntcNotifConfGroup':ntcNotifConfGroup,_N:ntcNotifConfGrpFldV1Standard,_O:ntcNotifConfGrpRepV1Standard,'ntcNotifConfCompliance':ntcNotifConfCompliance,'ntcNotifConfCompV1Standard':ntcNotifConfCompV1Standard})