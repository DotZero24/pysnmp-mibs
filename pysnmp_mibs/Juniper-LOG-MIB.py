_o='juniLogTrapGroup'
_n='juniLogGroup2'
_m='juniLogGroup'
_l='juniLogMsgThresholdTrap'
_k='juniLogSyslogFacility'
_j='juniLogSyslogSeverity'
_i='juniLogSyslogRowStatus'
_h='juniLogDestSyslogAddress'
_g='juniLogDestSyslogSeverity'
_f='juniLogMsgSequenceNumber'
_e='juniLogMsgSysUpTimeStamp'
_d='juniLogCatIndex'
_c='JuniLogSyslogFacility'
_b='juniLogSyslogIpAddress'
_a='JuniLogSeverity'
_Z='juniLogMsgDateAndTimeStamp'
_Y='juniLogMsgText'
_X='juniLogMsgSeverity'
_W='juniLogMsgCatIndex'
_V='juniLogMsgCatName'
_U='juniLogCatNameIndex'
_T='juniLogCatVerbosity'
_S='juniLogCatSeverity'
_R='juniLogCatDiscards'
_Q='juniLogCatEngineering'
_P='juniLogCatDescr'
_O='juniLogCatName'
_N='juniLogDestNvFileSeverity'
_M='juniLogDestConsoleSeverity'
_L='read-create'
_K='juniLogMsgThreshold'
_J='juniLogMsgLastSeqNumber'
_I='juniLogMsgCapacity'
_H='juniLogCatNameName'
_G='not-accessible'
_F='obsolete'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='current'
_A='Juniper-LOG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniLogSeverity,=mibBuilder.importSymbols('Juniper-TC',_a)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
juniLogMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,28))
if mibBuilder.loadTexts:juniLogMIB.setRevisions(('2002-09-16 21:44','2001-03-16 19:02','2000-03-27 05:00','1999-11-08 00:00'))
class JuniLogCatName(TextualConvention,OctetString):status=_B;displayHint='32a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
class JuniLogVerbosity(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('low',0),('medium',1),('high',2)))
class JuniLogSyslogFacility(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('local0',0),('local1',1),('local2',2),('local3',3),('local4',4),('local5',5),('local6',6),('local7',7)))
_JuniLogTrapPrefix_ObjectIdentity=ObjectIdentity
juniLogTrapPrefix=_JuniLogTrapPrefix_ObjectIdentity((1,3,6,1,4,1,4874,2,2,28,0))
_JuniLogObjects_ObjectIdentity=ObjectIdentity
juniLogObjects=_JuniLogObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,28,1))
_JuniLogDestinations_ObjectIdentity=ObjectIdentity
juniLogDestinations=_JuniLogDestinations_ObjectIdentity((1,3,6,1,4,1,4874,2,2,28,1,1))
_JuniLogDestSyslog_ObjectIdentity=ObjectIdentity
juniLogDestSyslog=_JuniLogDestSyslog_ObjectIdentity((1,3,6,1,4,1,4874,2,2,28,1,1,1))
_JuniLogDestSyslogSeverity_Type=JuniLogSeverity
_JuniLogDestSyslogSeverity_Object=MibScalar
juniLogDestSyslogSeverity=_JuniLogDestSyslogSeverity_Object((1,3,6,1,4,1,4874,2,2,28,1,1,1,1),_JuniLogDestSyslogSeverity_Type())
juniLogDestSyslogSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:juniLogDestSyslogSeverity.setStatus(_F)
_JuniLogDestSyslogAddress_Type=IpAddress
_JuniLogDestSyslogAddress_Object=MibScalar
juniLogDestSyslogAddress=_JuniLogDestSyslogAddress_Object((1,3,6,1,4,1,4874,2,2,28,1,1,1,2),_JuniLogDestSyslogAddress_Type())
juniLogDestSyslogAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:juniLogDestSyslogAddress.setStatus(_F)
_JuniLogSyslogTable_Object=MibTable
juniLogSyslogTable=_JuniLogSyslogTable_Object((1,3,6,1,4,1,4874,2,2,28,1,1,1,3))
if mibBuilder.loadTexts:juniLogSyslogTable.setStatus(_B)
_JuniLogSyslogEntry_Object=MibTableRow
juniLogSyslogEntry=_JuniLogSyslogEntry_Object((1,3,6,1,4,1,4874,2,2,28,1,1,1,3,1))
juniLogSyslogEntry.setIndexNames((0,_A,_b))
if mibBuilder.loadTexts:juniLogSyslogEntry.setStatus(_B)
_JuniLogSyslogIpAddress_Type=IpAddress
_JuniLogSyslogIpAddress_Object=MibTableColumn
juniLogSyslogIpAddress=_JuniLogSyslogIpAddress_Object((1,3,6,1,4,1,4874,2,2,28,1,1,1,3,1,1),_JuniLogSyslogIpAddress_Type())
juniLogSyslogIpAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:juniLogSyslogIpAddress.setStatus(_B)
_JuniLogSyslogRowStatus_Type=RowStatus
_JuniLogSyslogRowStatus_Object=MibTableColumn
juniLogSyslogRowStatus=_JuniLogSyslogRowStatus_Object((1,3,6,1,4,1,4874,2,2,28,1,1,1,3,1,2),_JuniLogSyslogRowStatus_Type())
juniLogSyslogRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:juniLogSyslogRowStatus.setStatus(_B)
class _JuniLogSyslogSeverity_Type(JuniLogSeverity):defaultValue=-1
_JuniLogSyslogSeverity_Type.__name__=_a
_JuniLogSyslogSeverity_Object=MibTableColumn
juniLogSyslogSeverity=_JuniLogSyslogSeverity_Object((1,3,6,1,4,1,4874,2,2,28,1,1,1,3,1,3),_JuniLogSyslogSeverity_Type())
juniLogSyslogSeverity.setMaxAccess(_L)
if mibBuilder.loadTexts:juniLogSyslogSeverity.setStatus(_B)
class _JuniLogSyslogFacility_Type(JuniLogSyslogFacility):defaultValue=7
_JuniLogSyslogFacility_Type.__name__=_c
_JuniLogSyslogFacility_Object=MibTableColumn
juniLogSyslogFacility=_JuniLogSyslogFacility_Object((1,3,6,1,4,1,4874,2,2,28,1,1,1,3,1,4),_JuniLogSyslogFacility_Type())
juniLogSyslogFacility.setMaxAccess(_L)
if mibBuilder.loadTexts:juniLogSyslogFacility.setStatus(_B)
_JuniLogDestConsole_ObjectIdentity=ObjectIdentity
juniLogDestConsole=_JuniLogDestConsole_ObjectIdentity((1,3,6,1,4,1,4874,2,2,28,1,1,2))
_JuniLogDestConsoleSeverity_Type=JuniLogSeverity
_JuniLogDestConsoleSeverity_Object=MibScalar
juniLogDestConsoleSeverity=_JuniLogDestConsoleSeverity_Object((1,3,6,1,4,1,4874,2,2,28,1,1,2,1),_JuniLogDestConsoleSeverity_Type())
juniLogDestConsoleSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:juniLogDestConsoleSeverity.setStatus(_B)
_JuniLogDestNvFile_ObjectIdentity=ObjectIdentity
juniLogDestNvFile=_JuniLogDestNvFile_ObjectIdentity((1,3,6,1,4,1,4874,2,2,28,1,1,3))
_JuniLogDestNvFileSeverity_Type=JuniLogSeverity
_JuniLogDestNvFileSeverity_Object=MibScalar
juniLogDestNvFileSeverity=_JuniLogDestNvFileSeverity_Object((1,3,6,1,4,1,4874,2,2,28,1,1,3,1),_JuniLogDestNvFileSeverity_Type())
juniLogDestNvFileSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:juniLogDestNvFileSeverity.setStatus(_B)
_JuniLogCategories_ObjectIdentity=ObjectIdentity
juniLogCategories=_JuniLogCategories_ObjectIdentity((1,3,6,1,4,1,4874,2,2,28,1,2))
_JuniLogCatScalars_ObjectIdentity=ObjectIdentity
juniLogCatScalars=_JuniLogCatScalars_ObjectIdentity((1,3,6,1,4,1,4874,2,2,28,1,2,1))
_JuniLogCatTable_Object=MibTable
juniLogCatTable=_JuniLogCatTable_Object((1,3,6,1,4,1,4874,2,2,28,1,2,2))
if mibBuilder.loadTexts:juniLogCatTable.setStatus(_B)
_JuniLogCatEntry_Object=MibTableRow
juniLogCatEntry=_JuniLogCatEntry_Object((1,3,6,1,4,1,4874,2,2,28,1,2,2,1))
juniLogCatEntry.setIndexNames((0,_A,_d))
if mibBuilder.loadTexts:juniLogCatEntry.setStatus(_B)
class _JuniLogCatIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_JuniLogCatIndex_Type.__name__=_E
_JuniLogCatIndex_Object=MibTableColumn
juniLogCatIndex=_JuniLogCatIndex_Object((1,3,6,1,4,1,4874,2,2,28,1,2,2,1,1),_JuniLogCatIndex_Type())
juniLogCatIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:juniLogCatIndex.setStatus(_B)
_JuniLogCatName_Type=JuniLogCatName
_JuniLogCatName_Object=MibTableColumn
juniLogCatName=_JuniLogCatName_Object((1,3,6,1,4,1,4874,2,2,28,1,2,2,1,2),_JuniLogCatName_Type())
juniLogCatName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniLogCatName.setStatus(_B)
_JuniLogCatDescr_Type=DisplayString
_JuniLogCatDescr_Object=MibTableColumn
juniLogCatDescr=_JuniLogCatDescr_Object((1,3,6,1,4,1,4874,2,2,28,1,2,2,1,3),_JuniLogCatDescr_Type())
juniLogCatDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:juniLogCatDescr.setStatus(_B)
_JuniLogCatEngineering_Type=TruthValue
_JuniLogCatEngineering_Object=MibTableColumn
juniLogCatEngineering=_JuniLogCatEngineering_Object((1,3,6,1,4,1,4874,2,2,28,1,2,2,1,4),_JuniLogCatEngineering_Type())
juniLogCatEngineering.setMaxAccess(_C)
if mibBuilder.loadTexts:juniLogCatEngineering.setStatus(_B)
_JuniLogCatDiscards_Type=Counter32
_JuniLogCatDiscards_Object=MibTableColumn
juniLogCatDiscards=_JuniLogCatDiscards_Object((1,3,6,1,4,1,4874,2,2,28,1,2,2,1,5),_JuniLogCatDiscards_Type())
juniLogCatDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:juniLogCatDiscards.setStatus(_B)
_JuniLogCatSeverity_Type=JuniLogSeverity
_JuniLogCatSeverity_Object=MibTableColumn
juniLogCatSeverity=_JuniLogCatSeverity_Object((1,3,6,1,4,1,4874,2,2,28,1,2,2,1,6),_JuniLogCatSeverity_Type())
juniLogCatSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:juniLogCatSeverity.setStatus(_B)
_JuniLogCatVerbosity_Type=JuniLogVerbosity
_JuniLogCatVerbosity_Object=MibTableColumn
juniLogCatVerbosity=_JuniLogCatVerbosity_Object((1,3,6,1,4,1,4874,2,2,28,1,2,2,1,7),_JuniLogCatVerbosity_Type())
juniLogCatVerbosity.setMaxAccess(_D)
if mibBuilder.loadTexts:juniLogCatVerbosity.setStatus(_B)
_JuniLogCatNameTable_Object=MibTable
juniLogCatNameTable=_JuniLogCatNameTable_Object((1,3,6,1,4,1,4874,2,2,28,1,2,3))
if mibBuilder.loadTexts:juniLogCatNameTable.setStatus(_B)
_JuniLogCatNameEntry_Object=MibTableRow
juniLogCatNameEntry=_JuniLogCatNameEntry_Object((1,3,6,1,4,1,4874,2,2,28,1,2,3,1))
juniLogCatNameEntry.setIndexNames((1,_A,_H))
if mibBuilder.loadTexts:juniLogCatNameEntry.setStatus(_B)
_JuniLogCatNameName_Type=JuniLogCatName
_JuniLogCatNameName_Object=MibTableColumn
juniLogCatNameName=_JuniLogCatNameName_Object((1,3,6,1,4,1,4874,2,2,28,1,2,3,1,1),_JuniLogCatNameName_Type())
juniLogCatNameName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniLogCatNameName.setStatus(_B)
class _JuniLogCatNameIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_JuniLogCatNameIndex_Type.__name__=_E
_JuniLogCatNameIndex_Object=MibTableColumn
juniLogCatNameIndex=_JuniLogCatNameIndex_Object((1,3,6,1,4,1,4874,2,2,28,1,2,3,1,2),_JuniLogCatNameIndex_Type())
juniLogCatNameIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniLogCatNameIndex.setStatus(_B)
_JuniLogMessages_ObjectIdentity=ObjectIdentity
juniLogMessages=_JuniLogMessages_ObjectIdentity((1,3,6,1,4,1,4874,2,2,28,1,3))
_JuniLogMsgScalars_ObjectIdentity=ObjectIdentity
juniLogMsgScalars=_JuniLogMsgScalars_ObjectIdentity((1,3,6,1,4,1,4874,2,2,28,1,3,1))
_JuniLogMsgCapacity_Type=Integer32
_JuniLogMsgCapacity_Object=MibScalar
juniLogMsgCapacity=_JuniLogMsgCapacity_Object((1,3,6,1,4,1,4874,2,2,28,1,3,1,1),_JuniLogMsgCapacity_Type())
juniLogMsgCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:juniLogMsgCapacity.setStatus(_B)
if mibBuilder.loadTexts:juniLogMsgCapacity.setUnits('messages')
_JuniLogMsgLastSeqNumber_Type=Counter32
_JuniLogMsgLastSeqNumber_Object=MibScalar
juniLogMsgLastSeqNumber=_JuniLogMsgLastSeqNumber_Object((1,3,6,1,4,1,4874,2,2,28,1,3,1,2),_JuniLogMsgLastSeqNumber_Type())
juniLogMsgLastSeqNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:juniLogMsgLastSeqNumber.setStatus(_B)
_JuniLogMsgTable_Object=MibTable
juniLogMsgTable=_JuniLogMsgTable_Object((1,3,6,1,4,1,4874,2,2,28,1,3,2))
if mibBuilder.loadTexts:juniLogMsgTable.setStatus(_B)
_JuniLogMsgEntry_Object=MibTableRow
juniLogMsgEntry=_JuniLogMsgEntry_Object((1,3,6,1,4,1,4874,2,2,28,1,3,2,1))
juniLogMsgEntry.setIndexNames((0,_A,_e),(0,_A,_f))
if mibBuilder.loadTexts:juniLogMsgEntry.setStatus(_B)
_JuniLogMsgSysUpTimeStamp_Type=TimeStamp
_JuniLogMsgSysUpTimeStamp_Object=MibTableColumn
juniLogMsgSysUpTimeStamp=_JuniLogMsgSysUpTimeStamp_Object((1,3,6,1,4,1,4874,2,2,28,1,3,2,1,1),_JuniLogMsgSysUpTimeStamp_Type())
juniLogMsgSysUpTimeStamp.setMaxAccess(_G)
if mibBuilder.loadTexts:juniLogMsgSysUpTimeStamp.setStatus(_B)
_JuniLogMsgSequenceNumber_Type=Unsigned32
_JuniLogMsgSequenceNumber_Object=MibTableColumn
juniLogMsgSequenceNumber=_JuniLogMsgSequenceNumber_Object((1,3,6,1,4,1,4874,2,2,28,1,3,2,1,2),_JuniLogMsgSequenceNumber_Type())
juniLogMsgSequenceNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:juniLogMsgSequenceNumber.setStatus(_B)
_JuniLogMsgCatName_Type=JuniLogCatName
_JuniLogMsgCatName_Object=MibTableColumn
juniLogMsgCatName=_JuniLogMsgCatName_Object((1,3,6,1,4,1,4874,2,2,28,1,3,2,1,3),_JuniLogMsgCatName_Type())
juniLogMsgCatName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniLogMsgCatName.setStatus(_B)
_JuniLogMsgCatIndex_Type=Integer32
_JuniLogMsgCatIndex_Object=MibTableColumn
juniLogMsgCatIndex=_JuniLogMsgCatIndex_Object((1,3,6,1,4,1,4874,2,2,28,1,3,2,1,4),_JuniLogMsgCatIndex_Type())
juniLogMsgCatIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniLogMsgCatIndex.setStatus(_B)
_JuniLogMsgSeverity_Type=JuniLogSeverity
_JuniLogMsgSeverity_Object=MibTableColumn
juniLogMsgSeverity=_JuniLogMsgSeverity_Object((1,3,6,1,4,1,4874,2,2,28,1,3,2,1,5),_JuniLogMsgSeverity_Type())
juniLogMsgSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:juniLogMsgSeverity.setStatus(_B)
_JuniLogMsgText_Type=DisplayString
_JuniLogMsgText_Object=MibTableColumn
juniLogMsgText=_JuniLogMsgText_Object((1,3,6,1,4,1,4874,2,2,28,1,3,2,1,6),_JuniLogMsgText_Type())
juniLogMsgText.setMaxAccess(_C)
if mibBuilder.loadTexts:juniLogMsgText.setStatus(_B)
_JuniLogMsgDateAndTimeStamp_Type=DateAndTime
_JuniLogMsgDateAndTimeStamp_Object=MibTableColumn
juniLogMsgDateAndTimeStamp=_JuniLogMsgDateAndTimeStamp_Object((1,3,6,1,4,1,4874,2,2,28,1,3,2,1,7),_JuniLogMsgDateAndTimeStamp_Type())
juniLogMsgDateAndTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:juniLogMsgDateAndTimeStamp.setStatus(_B)
_JuniLogTrapControl_ObjectIdentity=ObjectIdentity
juniLogTrapControl=_JuniLogTrapControl_ObjectIdentity((1,3,6,1,4,1,4874,2,2,28,2))
class _JuniLogMsgThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_JuniLogMsgThreshold_Type.__name__=_E
_JuniLogMsgThreshold_Object=MibScalar
juniLogMsgThreshold=_JuniLogMsgThreshold_Object((1,3,6,1,4,1,4874,2,2,28,2,1),_JuniLogMsgThreshold_Type())
juniLogMsgThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:juniLogMsgThreshold.setStatus(_B)
if mibBuilder.loadTexts:juniLogMsgThreshold.setUnits('percent')
_JuniLogMIBConformance_ObjectIdentity=ObjectIdentity
juniLogMIBConformance=_JuniLogMIBConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,28,4))
_JuniLogMIBCompliances_ObjectIdentity=ObjectIdentity
juniLogMIBCompliances=_JuniLogMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,28,4,1))
_JuniLogMIBGroups_ObjectIdentity=ObjectIdentity
juniLogMIBGroups=_JuniLogMIBGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,28,4,2))
juniLogGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,28,4,2,1))
juniLogGroup.setObjects(*((_A,_g),(_A,_h),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_H),(_A,_U),(_A,_I),(_A,_J),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_K)))
if mibBuilder.loadTexts:juniLogGroup.setStatus(_F)
juniLogGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,28,4,2,2))
juniLogGroup2.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_H),(_A,_U),(_A,_I),(_A,_J),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_K)))
if mibBuilder.loadTexts:juniLogGroup2.setStatus(_B)
juniLogMsgThresholdTrap=NotificationType((1,3,6,1,4,1,4874,2,2,28,0,1))
juniLogMsgThresholdTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:juniLogMsgThresholdTrap.setStatus(_B)
juniLogTrapGroup=NotificationGroup((1,3,6,1,4,1,4874,2,2,28,4,2,3))
juniLogTrapGroup.setObjects((_A,_l))
if mibBuilder.loadTexts:juniLogTrapGroup.setStatus(_B)
juniLogCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,28,4,1,1))
juniLogCompliance.setObjects((_A,_m))
if mibBuilder.loadTexts:juniLogCompliance.setStatus(_F)
juniLogCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,28,4,1,2))
juniLogCompliance2.setObjects(*((_A,_n),(_A,_o)))
if mibBuilder.loadTexts:juniLogCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'JuniLogCatName':JuniLogCatName,'JuniLogVerbosity':JuniLogVerbosity,_c:JuniLogSyslogFacility,'juniLogMIB':juniLogMIB,'juniLogTrapPrefix':juniLogTrapPrefix,_l:juniLogMsgThresholdTrap,'juniLogObjects':juniLogObjects,'juniLogDestinations':juniLogDestinations,'juniLogDestSyslog':juniLogDestSyslog,_g:juniLogDestSyslogSeverity,_h:juniLogDestSyslogAddress,'juniLogSyslogTable':juniLogSyslogTable,'juniLogSyslogEntry':juniLogSyslogEntry,_b:juniLogSyslogIpAddress,_i:juniLogSyslogRowStatus,_j:juniLogSyslogSeverity,_k:juniLogSyslogFacility,'juniLogDestConsole':juniLogDestConsole,_M:juniLogDestConsoleSeverity,'juniLogDestNvFile':juniLogDestNvFile,_N:juniLogDestNvFileSeverity,'juniLogCategories':juniLogCategories,'juniLogCatScalars':juniLogCatScalars,'juniLogCatTable':juniLogCatTable,'juniLogCatEntry':juniLogCatEntry,_d:juniLogCatIndex,_O:juniLogCatName,_P:juniLogCatDescr,_Q:juniLogCatEngineering,_R:juniLogCatDiscards,_S:juniLogCatSeverity,_T:juniLogCatVerbosity,'juniLogCatNameTable':juniLogCatNameTable,'juniLogCatNameEntry':juniLogCatNameEntry,_H:juniLogCatNameName,_U:juniLogCatNameIndex,'juniLogMessages':juniLogMessages,'juniLogMsgScalars':juniLogMsgScalars,_I:juniLogMsgCapacity,_J:juniLogMsgLastSeqNumber,'juniLogMsgTable':juniLogMsgTable,'juniLogMsgEntry':juniLogMsgEntry,_e:juniLogMsgSysUpTimeStamp,_f:juniLogMsgSequenceNumber,_V:juniLogMsgCatName,_W:juniLogMsgCatIndex,_X:juniLogMsgSeverity,_Y:juniLogMsgText,_Z:juniLogMsgDateAndTimeStamp,'juniLogTrapControl':juniLogTrapControl,_K:juniLogMsgThreshold,'juniLogMIBConformance':juniLogMIBConformance,'juniLogMIBCompliances':juniLogMIBCompliances,'juniLogCompliance':juniLogCompliance,'juniLogCompliance2':juniLogCompliance2,'juniLogMIBGroups':juniLogMIBGroups,_m:juniLogGroup,_n:juniLogGroup2,_o:juniLogTrapGroup})