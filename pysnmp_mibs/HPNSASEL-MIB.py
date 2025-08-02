_F='hpSELAgtIndex'
_E='HPNSASEL-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_Hpnsa_ObjectIdentity=ObjectIdentity
hpnsa=_Hpnsa_ObjectIdentity((1,3,6,1,4,1,11,2,23))
_HpSELAgt_ObjectIdentity=ObjectIdentity
hpSELAgt=_HpSELAgt_ObjectIdentity((1,3,6,1,4,1,11,2,23,29))
class _HpSELAgtVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpSELAgtVersion_Type.__name__=_C
_HpSELAgtVersion_Object=MibScalar
hpSELAgtVersion=_HpSELAgtVersion_Object((1,3,6,1,4,1,11,2,23,29,1),_HpSELAgtVersion_Type())
hpSELAgtVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSELAgtVersion.setStatus(_A)
class _HpSELAgtRevision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpSELAgtRevision_Type.__name__=_C
_HpSELAgtRevision_Object=MibScalar
hpSELAgtRevision=_HpSELAgtRevision_Object((1,3,6,1,4,1,11,2,23,29,2),_HpSELAgtRevision_Type())
hpSELAgtRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSELAgtRevision.setStatus(_A)
class _HpSELAgtMibVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpSELAgtMibVersion_Type.__name__=_C
_HpSELAgtMibVersion_Object=MibScalar
hpSELAgtMibVersion=_HpSELAgtMibVersion_Object((1,3,6,1,4,1,11,2,23,29,3),_HpSELAgtMibVersion_Type())
hpSELAgtMibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSELAgtMibVersion.setStatus(_A)
class _HpSELAgtMibRevision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpSELAgtMibRevision_Type.__name__=_C
_HpSELAgtMibRevision_Object=MibScalar
hpSELAgtMibRevision=_HpSELAgtMibRevision_Object((1,3,6,1,4,1,11,2,23,29,4),_HpSELAgtMibRevision_Type())
hpSELAgtMibRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSELAgtMibRevision.setStatus(_A)
class _HpSELAgtNumEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpSELAgtNumEntries_Type.__name__=_C
_HpSELAgtNumEntries_Object=MibScalar
hpSELAgtNumEntries=_HpSELAgtNumEntries_Object((1,3,6,1,4,1,11,2,23,29,5),_HpSELAgtNumEntries_Type())
hpSELAgtNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSELAgtNumEntries.setStatus(_A)
_HpSELAgtLogTable_Object=MibTable
hpSELAgtLogTable=_HpSELAgtLogTable_Object((1,3,6,1,4,1,11,2,23,29,6))
if mibBuilder.loadTexts:hpSELAgtLogTable.setStatus(_A)
_HpSELAgtLogEntry_Object=MibTableRow
hpSELAgtLogEntry=_HpSELAgtLogEntry_Object((1,3,6,1,4,1,11,2,23,29,6,1))
hpSELAgtLogEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hpSELAgtLogEntry.setStatus(_A)
_HpSELAgtIndex_Type=Integer32
_HpSELAgtIndex_Object=MibTableColumn
hpSELAgtIndex=_HpSELAgtIndex_Object((1,3,6,1,4,1,11,2,23,29,6,1,1),_HpSELAgtIndex_Type())
hpSELAgtIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSELAgtIndex.setStatus(_A)
class _HpSELAgtRecordID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpSELAgtRecordID_Type.__name__=_C
_HpSELAgtRecordID_Object=MibTableColumn
hpSELAgtRecordID=_HpSELAgtRecordID_Object((1,3,6,1,4,1,11,2,23,29,6,1,2),_HpSELAgtRecordID_Type())
hpSELAgtRecordID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSELAgtRecordID.setStatus(_A)
class _HpSELAgtRecordType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpSELAgtRecordType_Type.__name__=_C
_HpSELAgtRecordType_Object=MibTableColumn
hpSELAgtRecordType=_HpSELAgtRecordType_Object((1,3,6,1,4,1,11,2,23,29,6,1,3),_HpSELAgtRecordType_Type())
hpSELAgtRecordType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSELAgtRecordType.setStatus(_A)
_HpSELAgtTimestamp_Type=Integer32
_HpSELAgtTimestamp_Object=MibTableColumn
hpSELAgtTimestamp=_HpSELAgtTimestamp_Object((1,3,6,1,4,1,11,2,23,29,6,1,4),_HpSELAgtTimestamp_Type())
hpSELAgtTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSELAgtTimestamp.setStatus(_A)
class _HpSELAgtGeneratorID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpSELAgtGeneratorID_Type.__name__=_C
_HpSELAgtGeneratorID_Object=MibTableColumn
hpSELAgtGeneratorID=_HpSELAgtGeneratorID_Object((1,3,6,1,4,1,11,2,23,29,6,1,5),_HpSELAgtGeneratorID_Type())
hpSELAgtGeneratorID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSELAgtGeneratorID.setStatus(_A)
class _HpSELAgtGeneratorLUN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpSELAgtGeneratorLUN_Type.__name__=_C
_HpSELAgtGeneratorLUN_Object=MibTableColumn
hpSELAgtGeneratorLUN=_HpSELAgtGeneratorLUN_Object((1,3,6,1,4,1,11,2,23,29,6,1,6),_HpSELAgtGeneratorLUN_Type())
hpSELAgtGeneratorLUN.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSELAgtGeneratorLUN.setStatus(_A)
class _HpSELAgtEventVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpSELAgtEventVersion_Type.__name__=_C
_HpSELAgtEventVersion_Object=MibTableColumn
hpSELAgtEventVersion=_HpSELAgtEventVersion_Object((1,3,6,1,4,1,11,2,23,29,6,1,7),_HpSELAgtEventVersion_Type())
hpSELAgtEventVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSELAgtEventVersion.setStatus(_A)
class _HpSELAgtSensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpSELAgtSensorType_Type.__name__=_C
_HpSELAgtSensorType_Object=MibTableColumn
hpSELAgtSensorType=_HpSELAgtSensorType_Object((1,3,6,1,4,1,11,2,23,29,6,1,8),_HpSELAgtSensorType_Type())
hpSELAgtSensorType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSELAgtSensorType.setStatus(_A)
class _HpSELAgtSensorNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpSELAgtSensorNumber_Type.__name__=_C
_HpSELAgtSensorNumber_Object=MibTableColumn
hpSELAgtSensorNumber=_HpSELAgtSensorNumber_Object((1,3,6,1,4,1,11,2,23,29,6,1,9),_HpSELAgtSensorNumber_Type())
hpSELAgtSensorNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSELAgtSensorNumber.setStatus(_A)
class _HpSELAgtEventTrigger_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpSELAgtEventTrigger_Type.__name__=_C
_HpSELAgtEventTrigger_Object=MibTableColumn
hpSELAgtEventTrigger=_HpSELAgtEventTrigger_Object((1,3,6,1,4,1,11,2,23,29,6,1,10),_HpSELAgtEventTrigger_Type())
hpSELAgtEventTrigger.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSELAgtEventTrigger.setStatus(_A)
class _HpSELAgtEventData1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpSELAgtEventData1_Type.__name__=_C
_HpSELAgtEventData1_Object=MibTableColumn
hpSELAgtEventData1=_HpSELAgtEventData1_Object((1,3,6,1,4,1,11,2,23,29,6,1,11),_HpSELAgtEventData1_Type())
hpSELAgtEventData1.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSELAgtEventData1.setStatus(_A)
class _HpSELAgtEventData2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpSELAgtEventData2_Type.__name__=_C
_HpSELAgtEventData2_Object=MibTableColumn
hpSELAgtEventData2=_HpSELAgtEventData2_Object((1,3,6,1,4,1,11,2,23,29,6,1,12),_HpSELAgtEventData2_Type())
hpSELAgtEventData2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSELAgtEventData2.setStatus(_A)
class _HpSELAgtEventData3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpSELAgtEventData3_Type.__name__=_C
_HpSELAgtEventData3_Object=MibTableColumn
hpSELAgtEventData3=_HpSELAgtEventData3_Object((1,3,6,1,4,1,11,2,23,29,6,1,13),_HpSELAgtEventData3_Type())
hpSELAgtEventData3.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSELAgtEventData3.setStatus(_A)
_HpSELAgtLineNum_Type=Integer32
_HpSELAgtLineNum_Object=MibTableColumn
hpSELAgtLineNum=_HpSELAgtLineNum_Object((1,3,6,1,4,1,11,2,23,29,6,1,14),_HpSELAgtLineNum_Type())
hpSELAgtLineNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSELAgtLineNum.setStatus(_A)
_HpSELAgtStrInfo_Type=DisplayString
_HpSELAgtStrInfo_Object=MibTableColumn
hpSELAgtStrInfo=_HpSELAgtStrInfo_Object((1,3,6,1,4,1,11,2,23,29,6,1,15),_HpSELAgtStrInfo_Type())
hpSELAgtStrInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSELAgtStrInfo.setStatus(_A)
_HpSELAgtSeverity_Type=DisplayString
_HpSELAgtSeverity_Object=MibTableColumn
hpSELAgtSeverity=_HpSELAgtSeverity_Object((1,3,6,1,4,1,11,2,23,29,6,1,16),_HpSELAgtSeverity_Type())
hpSELAgtSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSELAgtSeverity.setStatus(_A)
class _HpSELAgtFilterSensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpSELAgtFilterSensorType_Type.__name__=_C
_HpSELAgtFilterSensorType_Object=MibScalar
hpSELAgtFilterSensorType=_HpSELAgtFilterSensorType_Object((1,3,6,1,4,1,11,2,23,29,7),_HpSELAgtFilterSensorType_Type())
hpSELAgtFilterSensorType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSELAgtFilterSensorType.setStatus(_A)
class _HpSELAgtFilterEventTrigger_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpSELAgtFilterEventTrigger_Type.__name__=_C
_HpSELAgtFilterEventTrigger_Object=MibScalar
hpSELAgtFilterEventTrigger=_HpSELAgtFilterEventTrigger_Object((1,3,6,1,4,1,11,2,23,29,8),_HpSELAgtFilterEventTrigger_Type())
hpSELAgtFilterEventTrigger.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSELAgtFilterEventTrigger.setStatus(_A)
class _HpSELAgtFilterOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpSELAgtFilterOffset_Type.__name__=_C
_HpSELAgtFilterOffset_Object=MibScalar
hpSELAgtFilterOffset=_HpSELAgtFilterOffset_Object((1,3,6,1,4,1,11,2,23,29,9),_HpSELAgtFilterOffset_Type())
hpSELAgtFilterOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSELAgtFilterOffset.setStatus(_A)
_HpSELAgtLogFile_Type=DisplayString
_HpSELAgtLogFile_Object=MibScalar
hpSELAgtLogFile=_HpSELAgtLogFile_Object((1,3,6,1,4,1,11,2,23,29,10),_HpSELAgtLogFile_Type())
hpSELAgtLogFile.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSELAgtLogFile.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hp':hp,'nm':nm,'hpnsa':hpnsa,'hpSELAgt':hpSELAgt,'hpSELAgtVersion':hpSELAgtVersion,'hpSELAgtRevision':hpSELAgtRevision,'hpSELAgtMibVersion':hpSELAgtMibVersion,'hpSELAgtMibRevision':hpSELAgtMibRevision,'hpSELAgtNumEntries':hpSELAgtNumEntries,'hpSELAgtLogTable':hpSELAgtLogTable,'hpSELAgtLogEntry':hpSELAgtLogEntry,_F:hpSELAgtIndex,'hpSELAgtRecordID':hpSELAgtRecordID,'hpSELAgtRecordType':hpSELAgtRecordType,'hpSELAgtTimestamp':hpSELAgtTimestamp,'hpSELAgtGeneratorID':hpSELAgtGeneratorID,'hpSELAgtGeneratorLUN':hpSELAgtGeneratorLUN,'hpSELAgtEventVersion':hpSELAgtEventVersion,'hpSELAgtSensorType':hpSELAgtSensorType,'hpSELAgtSensorNumber':hpSELAgtSensorNumber,'hpSELAgtEventTrigger':hpSELAgtEventTrigger,'hpSELAgtEventData1':hpSELAgtEventData1,'hpSELAgtEventData2':hpSELAgtEventData2,'hpSELAgtEventData3':hpSELAgtEventData3,'hpSELAgtLineNum':hpSELAgtLineNum,'hpSELAgtStrInfo':hpSELAgtStrInfo,'hpSELAgtSeverity':hpSELAgtSeverity,'hpSELAgtFilterSensorType':hpSELAgtFilterSensorType,'hpSELAgtFilterEventTrigger':hpSELAgtFilterEventTrigger,'hpSELAgtFilterOffset':hpSELAgtFilterOffset,'hpSELAgtLogFile':hpSELAgtLogFile})