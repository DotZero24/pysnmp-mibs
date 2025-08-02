_I='recoverTrapSequenceNum'
_H='trapManagerIPaddress'
_G='managerIPaddress'
_F='OctetString'
_E='RTM-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
stratacom,=mibBuilder.importSymbols('CISCOWAN-SMI','stratacom')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Rtm_ObjectIdentity=ObjectIdentity
rtm=_Rtm_ObjectIdentity((1,3,6,1,4,1,351,120))
_TrapsConfig_ObjectIdentity=ObjectIdentity
trapsConfig=_TrapsConfig_ObjectIdentity((1,3,6,1,4,1,351,120,1))
_TrapConfigTable_Object=MibTable
trapConfigTable=_TrapConfigTable_Object((1,3,6,1,4,1,351,120,1,1))
if mibBuilder.loadTexts:trapConfigTable.setStatus(_A)
_TrapConfigEntry_Object=MibTableRow
trapConfigEntry=_TrapConfigEntry_Object((1,3,6,1,4,1,351,120,1,1,1))
trapConfigEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:trapConfigEntry.setStatus(_A)
_ManagerIPaddress_Type=IpAddress
_ManagerIPaddress_Object=MibTableColumn
managerIPaddress=_ManagerIPaddress_Object((1,3,6,1,4,1,351,120,1,1,1,1),_ManagerIPaddress_Type())
managerIPaddress.setMaxAccess(_D)
if mibBuilder.loadTexts:managerIPaddress.setStatus(_A)
_ManagerPortNumber_Type=Integer32
_ManagerPortNumber_Object=MibTableColumn
managerPortNumber=_ManagerPortNumber_Object((1,3,6,1,4,1,351,120,1,1,1,2),_ManagerPortNumber_Type())
managerPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:managerPortNumber.setStatus(_A)
class _ManagerRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('addRow',1),('delRow',2)))
_ManagerRowStatus_Type.__name__=_C
_ManagerRowStatus_Object=MibTableColumn
managerRowStatus=_ManagerRowStatus_Object((1,3,6,1,4,1,351,120,1,1,1,3),_ManagerRowStatus_Type())
managerRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:managerRowStatus.setStatus(_A)
class _ReadingTrapsFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('false',1),('true',2)))
_ReadingTrapsFlag_Type.__name__=_C
_ReadingTrapsFlag_Object=MibTableColumn
readingTrapsFlag=_ReadingTrapsFlag_Object((1,3,6,1,4,1,351,120,1,1,1,4),_ReadingTrapsFlag_Type())
readingTrapsFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:readingTrapsFlag.setStatus(_A)
_NextTrapSeqNum_Type=Integer32
_NextTrapSeqNum_Object=MibTableColumn
nextTrapSeqNum=_NextTrapSeqNum_Object((1,3,6,1,4,1,351,120,1,1,1,5),_NextTrapSeqNum_Type())
nextTrapSeqNum.setMaxAccess(_D)
if mibBuilder.loadTexts:nextTrapSeqNum.setStatus(_A)
class _ManagerNumOfValidEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_ManagerNumOfValidEntries_Type.__name__=_C
_ManagerNumOfValidEntries_Object=MibScalar
managerNumOfValidEntries=_ManagerNumOfValidEntries_Object((1,3,6,1,4,1,351,120,1,2),_ManagerNumOfValidEntries_Type())
managerNumOfValidEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:managerNumOfValidEntries.setStatus(_A)
_LastSequenceNumber_Type=Integer32
_LastSequenceNumber_Object=MibScalar
lastSequenceNumber=_LastSequenceNumber_Object((1,3,6,1,4,1,351,120,1,3),_LastSequenceNumber_Type())
lastSequenceNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:lastSequenceNumber.setStatus(_A)
_TrapUploadTable_Object=MibTable
trapUploadTable=_TrapUploadTable_Object((1,3,6,1,4,1,351,120,1,4))
if mibBuilder.loadTexts:trapUploadTable.setStatus(_A)
_TrapUploadEntry_Object=MibTableRow
trapUploadEntry=_TrapUploadEntry_Object((1,3,6,1,4,1,351,120,1,4,1))
trapUploadEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:trapUploadEntry.setStatus(_A)
_TrapManagerIPaddress_Type=IpAddress
_TrapManagerIPaddress_Object=MibTableColumn
trapManagerIPaddress=_TrapManagerIPaddress_Object((1,3,6,1,4,1,351,120,1,4,1,1),_TrapManagerIPaddress_Type())
trapManagerIPaddress.setMaxAccess(_D)
if mibBuilder.loadTexts:trapManagerIPaddress.setStatus(_A)
_TrapSequenceNum_Type=Integer32
_TrapSequenceNum_Object=MibTableColumn
trapSequenceNum=_TrapSequenceNum_Object((1,3,6,1,4,1,351,120,1,4,1,2),_TrapSequenceNum_Type())
trapSequenceNum.setMaxAccess(_B)
if mibBuilder.loadTexts:trapSequenceNum.setStatus(_A)
_TrapPduString_Type=DisplayString
_TrapPduString_Object=MibTableColumn
trapPduString=_TrapPduString_Object((1,3,6,1,4,1,351,120,1,4,1,3),_TrapPduString_Type())
trapPduString.setMaxAccess(_B)
if mibBuilder.loadTexts:trapPduString.setStatus(_A)
class _EndOfQueueFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('false',1),('true',2)))
_EndOfQueueFlag_Type.__name__=_C
_EndOfQueueFlag_Object=MibTableColumn
endOfQueueFlag=_EndOfQueueFlag_Object((1,3,6,1,4,1,351,120,1,4,1,4),_EndOfQueueFlag_Type())
endOfQueueFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfQueueFlag.setStatus(_A)
_RecoverTrapTable_Object=MibTable
recoverTrapTable=_RecoverTrapTable_Object((1,3,6,1,4,1,351,120,1,5))
if mibBuilder.loadTexts:recoverTrapTable.setStatus(_A)
_RecoverTrapEntry_Object=MibTableRow
recoverTrapEntry=_RecoverTrapEntry_Object((1,3,6,1,4,1,351,120,1,5,1))
recoverTrapEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:recoverTrapEntry.setStatus(_A)
class _RecoverTrapSequenceNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RecoverTrapSequenceNum_Type.__name__=_C
_RecoverTrapSequenceNum_Object=MibTableColumn
recoverTrapSequenceNum=_RecoverTrapSequenceNum_Object((1,3,6,1,4,1,351,120,1,5,1,1),_RecoverTrapSequenceNum_Type())
recoverTrapSequenceNum.setMaxAccess(_B)
if mibBuilder.loadTexts:recoverTrapSequenceNum.setStatus(_A)
class _RecoverTrapPduString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_RecoverTrapPduString_Type.__name__=_F
_RecoverTrapPduString_Object=MibTableColumn
recoverTrapPduString=_RecoverTrapPduString_Object((1,3,6,1,4,1,351,120,1,5,1,2),_RecoverTrapPduString_Type())
recoverTrapPduString.setMaxAccess(_B)
if mibBuilder.loadTexts:recoverTrapPduString.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'rtm':rtm,'trapsConfig':trapsConfig,'trapConfigTable':trapConfigTable,'trapConfigEntry':trapConfigEntry,_G:managerIPaddress,'managerPortNumber':managerPortNumber,'managerRowStatus':managerRowStatus,'readingTrapsFlag':readingTrapsFlag,'nextTrapSeqNum':nextTrapSeqNum,'managerNumOfValidEntries':managerNumOfValidEntries,'lastSequenceNumber':lastSequenceNumber,'trapUploadTable':trapUploadTable,'trapUploadEntry':trapUploadEntry,_H:trapManagerIPaddress,'trapSequenceNum':trapSequenceNum,'trapPduString':trapPduString,'endOfQueueFlag':endOfQueueFlag,'recoverTrapTable':recoverTrapTable,'recoverTrapEntry':recoverTrapEntry,_I:recoverTrapSequenceNum,'recoverTrapPduString':recoverTrapPduString})