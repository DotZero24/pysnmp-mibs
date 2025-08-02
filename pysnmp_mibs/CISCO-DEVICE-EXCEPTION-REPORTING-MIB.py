_W='ciscoDERExceptionGroup'
_V='ciscoDERExceptionDataGroup'
_U='cderMonitoredExceptionEvent'
_T='cderNotificationsDropped'
_S='cderNotificationsSent'
_R='cderNotificationEnabled'
_Q='cderMaxExceptionRecords'
_P='cderExcepTableIndex'
_O='read-write'
_N='TruthValue'
_M='OctetString'
_L='cderExcepReportedBy'
_K='cderExcepData'
_J='cderExcepTime'
_I='cderExcepPriorityDescription'
_H='cderExcepHostAddress'
_G='cderExcepHostAddressType'
_F='cderExcepId'
_E='Unsigned32'
_D='SnmpAdminString'
_C='read-only'
_B='current'
_A='CISCO-DEVICE-EXCEPTION-REPORTING-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_N)
ciscoDevExcepReportMIB=ModuleIdentity((1,3,6,1,4,1,9,9,224))
_CiscoDevExcepReportMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDevExcepReportMIBObjects=_CiscoDevExcepReportMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,224,1))
_CderExceptionData_ObjectIdentity=ObjectIdentity
cderExceptionData=_CderExceptionData_ObjectIdentity((1,3,6,1,4,1,9,9,224,1,1))
class _CderMaxExceptionRecords_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_CderMaxExceptionRecords_Type.__name__=_E
_CderMaxExceptionRecords_Object=MibScalar
cderMaxExceptionRecords=_CderMaxExceptionRecords_Object((1,3,6,1,4,1,9,9,224,1,1,1),_CderMaxExceptionRecords_Type())
cderMaxExceptionRecords.setMaxAccess(_O)
if mibBuilder.loadTexts:cderMaxExceptionRecords.setStatus(_B)
class _CderNotificationEnabled_Type(TruthValue):defaultValue=2
_CderNotificationEnabled_Type.__name__=_N
_CderNotificationEnabled_Object=MibScalar
cderNotificationEnabled=_CderNotificationEnabled_Object((1,3,6,1,4,1,9,9,224,1,1,2),_CderNotificationEnabled_Type())
cderNotificationEnabled.setMaxAccess(_O)
if mibBuilder.loadTexts:cderNotificationEnabled.setStatus(_B)
_CderNotificationsSent_Type=Counter32
_CderNotificationsSent_Object=MibScalar
cderNotificationsSent=_CderNotificationsSent_Object((1,3,6,1,4,1,9,9,224,1,1,3),_CderNotificationsSent_Type())
cderNotificationsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cderNotificationsSent.setStatus(_B)
_CderNotificationsDropped_Type=Counter32
_CderNotificationsDropped_Object=MibScalar
cderNotificationsDropped=_CderNotificationsDropped_Object((1,3,6,1,4,1,9,9,224,1,1,4),_CderNotificationsDropped_Type())
cderNotificationsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:cderNotificationsDropped.setStatus(_B)
_CderExceptionTable_Object=MibTable
cderExceptionTable=_CderExceptionTable_Object((1,3,6,1,4,1,9,9,224,1,1,5))
if mibBuilder.loadTexts:cderExceptionTable.setStatus(_B)
_CderExceptionEntry_Object=MibTableRow
cderExceptionEntry=_CderExceptionEntry_Object((1,3,6,1,4,1,9,9,224,1,1,5,1))
cderExceptionEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:cderExceptionEntry.setStatus(_B)
class _CderExcepTableIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CderExcepTableIndex_Type.__name__=_E
_CderExcepTableIndex_Object=MibTableColumn
cderExcepTableIndex=_CderExcepTableIndex_Object((1,3,6,1,4,1,9,9,224,1,1,5,1,1),_CderExcepTableIndex_Type())
cderExcepTableIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cderExcepTableIndex.setStatus(_B)
class _CderExcepId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CderExcepId_Type.__name__=_D
_CderExcepId_Object=MibTableColumn
cderExcepId=_CderExcepId_Object((1,3,6,1,4,1,9,9,224,1,1,5,1,2),_CderExcepId_Type())
cderExcepId.setMaxAccess(_C)
if mibBuilder.loadTexts:cderExcepId.setStatus(_B)
_CderExcepHostAddressType_Type=InetAddressType
_CderExcepHostAddressType_Object=MibTableColumn
cderExcepHostAddressType=_CderExcepHostAddressType_Object((1,3,6,1,4,1,9,9,224,1,1,5,1,3),_CderExcepHostAddressType_Type())
cderExcepHostAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cderExcepHostAddressType.setStatus(_B)
_CderExcepHostAddress_Type=InetAddress
_CderExcepHostAddress_Object=MibTableColumn
cderExcepHostAddress=_CderExcepHostAddress_Object((1,3,6,1,4,1,9,9,224,1,1,5,1,4),_CderExcepHostAddress_Type())
cderExcepHostAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cderExcepHostAddress.setStatus(_B)
class _CderExcepPriorityDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CderExcepPriorityDescription_Type.__name__=_D
_CderExcepPriorityDescription_Object=MibTableColumn
cderExcepPriorityDescription=_CderExcepPriorityDescription_Object((1,3,6,1,4,1,9,9,224,1,1,5,1,5),_CderExcepPriorityDescription_Type())
cderExcepPriorityDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cderExcepPriorityDescription.setStatus(_B)
_CderExcepTime_Type=TimeStamp
_CderExcepTime_Object=MibTableColumn
cderExcepTime=_CderExcepTime_Object((1,3,6,1,4,1,9,9,224,1,1,5,1,6),_CderExcepTime_Type())
cderExcepTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cderExcepTime.setStatus(_B)
class _CderExcepData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CderExcepData_Type.__name__=_M
_CderExcepData_Object=MibTableColumn
cderExcepData=_CderExcepData_Object((1,3,6,1,4,1,9,9,224,1,1,5,1,7),_CderExcepData_Type())
cderExcepData.setMaxAccess(_C)
if mibBuilder.loadTexts:cderExcepData.setStatus(_B)
_CderExcepReportedBy_Type=SnmpAdminString
_CderExcepReportedBy_Object=MibTableColumn
cderExcepReportedBy=_CderExcepReportedBy_Object((1,3,6,1,4,1,9,9,224,1,1,5,1,8),_CderExcepReportedBy_Type())
cderExcepReportedBy.setMaxAccess(_C)
if mibBuilder.loadTexts:cderExcepReportedBy.setStatus(_B)
_CderMIBNotifPrefix_ObjectIdentity=ObjectIdentity
cderMIBNotifPrefix=_CderMIBNotifPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,224,2))
_CderMIBNotifications_ObjectIdentity=ObjectIdentity
cderMIBNotifications=_CderMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,224,2,0))
_CiscoDEReportMIBConformance_ObjectIdentity=ObjectIdentity
ciscoDEReportMIBConformance=_CiscoDEReportMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,224,3))
_CiscoDEReportMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDEReportMIBCompliances=_CiscoDEReportMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,224,3,1))
_CiscoDEReportMIBGroups_ObjectIdentity=ObjectIdentity
ciscoDEReportMIBGroups=_CiscoDEReportMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,224,3,2))
ciscoDERExceptionDataGroup=ObjectGroup((1,3,6,1,4,1,9,9,224,3,2,1))
ciscoDERExceptionDataGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ciscoDERExceptionDataGroup.setStatus(_B)
cderMonitoredExceptionEvent=NotificationType((1,3,6,1,4,1,9,9,224,2,0,1))
cderMonitoredExceptionEvent.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:cderMonitoredExceptionEvent.setStatus(_B)
ciscoDERExceptionGroup=NotificationGroup((1,3,6,1,4,1,9,9,224,3,2,2))
ciscoDERExceptionGroup.setObjects((_A,_U))
if mibBuilder.loadTexts:ciscoDERExceptionGroup.setStatus(_B)
ciscoDEReportMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,224,3,1,1))
ciscoDEReportMIBCompliance.setObjects(*((_A,_V),(_A,_W)))
if mibBuilder.loadTexts:ciscoDEReportMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoDevExcepReportMIB':ciscoDevExcepReportMIB,'ciscoDevExcepReportMIBObjects':ciscoDevExcepReportMIBObjects,'cderExceptionData':cderExceptionData,_Q:cderMaxExceptionRecords,_R:cderNotificationEnabled,_S:cderNotificationsSent,_T:cderNotificationsDropped,'cderExceptionTable':cderExceptionTable,'cderExceptionEntry':cderExceptionEntry,_P:cderExcepTableIndex,_F:cderExcepId,_G:cderExcepHostAddressType,_H:cderExcepHostAddress,_I:cderExcepPriorityDescription,_J:cderExcepTime,_K:cderExcepData,_L:cderExcepReportedBy,'cderMIBNotifPrefix':cderMIBNotifPrefix,'cderMIBNotifications':cderMIBNotifications,_U:cderMonitoredExceptionEvent,'ciscoDEReportMIBConformance':ciscoDEReportMIBConformance,'ciscoDEReportMIBCompliances':ciscoDEReportMIBCompliances,'ciscoDEReportMIBCompliance':ciscoDEReportMIBCompliance,'ciscoDEReportMIBGroups':ciscoDEReportMIBGroups,_V:ciscoDERExceptionDataGroup,_W:ciscoDERExceptionGroup})