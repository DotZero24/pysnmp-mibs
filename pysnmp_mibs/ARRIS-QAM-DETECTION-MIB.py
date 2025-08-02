_H='read-only'
_G='arrisQamDetectionResultsIndex'
_F='not-accessible'
_E='arrisQamDetectionConfigFrequencyIndex'
_D='ARRIS-QAM-DETECTION-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
arrisProdIdCM,=mibBuilder.importSymbols('ARRIS-MIB','arrisProdIdCM')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
arrisQamDetectionMib=ModuleIdentity((1,3,6,1,4,1,4115,1,3,12))
if mibBuilder.loadTexts:arrisQamDetectionMib.setRevisions(('1911-08-03 00:00',))
_ArrisQamDetectionMibObjects_ObjectIdentity=ObjectIdentity
arrisQamDetectionMibObjects=_ArrisQamDetectionMibObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,3,12,1))
_ArrisQamDetectionConfig_ObjectIdentity=ObjectIdentity
arrisQamDetectionConfig=_ArrisQamDetectionConfig_ObjectIdentity((1,3,6,1,4,1,4115,1,3,12,1,1))
_ArrisQamDetectionConfigEnable_Type=TruthValue
_ArrisQamDetectionConfigEnable_Object=MibScalar
arrisQamDetectionConfigEnable=_ArrisQamDetectionConfigEnable_Object((1,3,6,1,4,1,4115,1,3,12,1,1,1),_ArrisQamDetectionConfigEnable_Type())
arrisQamDetectionConfigEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisQamDetectionConfigEnable.setStatus(_A)
_ArrisQamDetectionConfigFrequencyTable_Object=MibTable
arrisQamDetectionConfigFrequencyTable=_ArrisQamDetectionConfigFrequencyTable_Object((1,3,6,1,4,1,4115,1,3,12,1,1,2))
if mibBuilder.loadTexts:arrisQamDetectionConfigFrequencyTable.setStatus(_A)
_ArrisQamDetectionConfigFrequencyEntry_Object=MibTableRow
arrisQamDetectionConfigFrequencyEntry=_ArrisQamDetectionConfigFrequencyEntry_Object((1,3,6,1,4,1,4115,1,3,12,1,1,2,1))
arrisQamDetectionConfigFrequencyEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:arrisQamDetectionConfigFrequencyEntry.setStatus(_A)
class _ArrisQamDetectionConfigFrequencyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_ArrisQamDetectionConfigFrequencyIndex_Type.__name__=_B
_ArrisQamDetectionConfigFrequencyIndex_Object=MibTableColumn
arrisQamDetectionConfigFrequencyIndex=_ArrisQamDetectionConfigFrequencyIndex_Object((1,3,6,1,4,1,4115,1,3,12,1,1,2,1,1),_ArrisQamDetectionConfigFrequencyIndex_Type())
arrisQamDetectionConfigFrequencyIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:arrisQamDetectionConfigFrequencyIndex.setStatus(_A)
class _ArrisQamDetectionConfigFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(91000000,999000000))
_ArrisQamDetectionConfigFrequency_Type.__name__=_B
_ArrisQamDetectionConfigFrequency_Object=MibTableColumn
arrisQamDetectionConfigFrequency=_ArrisQamDetectionConfigFrequency_Object((1,3,6,1,4,1,4115,1,3,12,1,1,2,1,2),_ArrisQamDetectionConfigFrequency_Type())
arrisQamDetectionConfigFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisQamDetectionConfigFrequency.setStatus(_A)
if mibBuilder.loadTexts:arrisQamDetectionConfigFrequency.setUnits('hertz')
_ArrisQamDetectionConfigClearResults_Type=TruthValue
_ArrisQamDetectionConfigClearResults_Object=MibScalar
arrisQamDetectionConfigClearResults=_ArrisQamDetectionConfigClearResults_Object((1,3,6,1,4,1,4115,1,3,12,1,1,3),_ArrisQamDetectionConfigClearResults_Type())
arrisQamDetectionConfigClearResults.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisQamDetectionConfigClearResults.setStatus(_A)
_ArrisQamDetectionResultsTable_Object=MibTable
arrisQamDetectionResultsTable=_ArrisQamDetectionResultsTable_Object((1,3,6,1,4,1,4115,1,3,12,1,2))
if mibBuilder.loadTexts:arrisQamDetectionResultsTable.setStatus(_A)
_ArrisQamDetectionResultsEntry_Object=MibTableRow
arrisQamDetectionResultsEntry=_ArrisQamDetectionResultsEntry_Object((1,3,6,1,4,1,4115,1,3,12,1,2,1))
arrisQamDetectionResultsEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:arrisQamDetectionResultsEntry.setStatus(_A)
class _ArrisQamDetectionResultsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_ArrisQamDetectionResultsIndex_Type.__name__=_B
_ArrisQamDetectionResultsIndex_Object=MibTableColumn
arrisQamDetectionResultsIndex=_ArrisQamDetectionResultsIndex_Object((1,3,6,1,4,1,4115,1,3,12,1,2,1,1),_ArrisQamDetectionResultsIndex_Type())
arrisQamDetectionResultsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:arrisQamDetectionResultsIndex.setStatus(_A)
class _ArrisQamDetectionResultsFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(91000000,999000000))
_ArrisQamDetectionResultsFreq_Type.__name__=_B
_ArrisQamDetectionResultsFreq_Object=MibTableColumn
arrisQamDetectionResultsFreq=_ArrisQamDetectionResultsFreq_Object((1,3,6,1,4,1,4115,1,3,12,1,2,1,2),_ArrisQamDetectionResultsFreq_Type())
arrisQamDetectionResultsFreq.setMaxAccess(_H)
if mibBuilder.loadTexts:arrisQamDetectionResultsFreq.setStatus(_A)
if mibBuilder.loadTexts:arrisQamDetectionResultsFreq.setUnits('hertz')
_ArrisQamDetectionResultsTimestamp_Type=DisplayString
_ArrisQamDetectionResultsTimestamp_Object=MibTableColumn
arrisQamDetectionResultsTimestamp=_ArrisQamDetectionResultsTimestamp_Object((1,3,6,1,4,1,4115,1,3,12,1,2,1,3),_ArrisQamDetectionResultsTimestamp_Type())
arrisQamDetectionResultsTimestamp.setMaxAccess(_H)
if mibBuilder.loadTexts:arrisQamDetectionResultsTimestamp.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'arrisQamDetectionMib':arrisQamDetectionMib,'arrisQamDetectionMibObjects':arrisQamDetectionMibObjects,'arrisQamDetectionConfig':arrisQamDetectionConfig,'arrisQamDetectionConfigEnable':arrisQamDetectionConfigEnable,'arrisQamDetectionConfigFrequencyTable':arrisQamDetectionConfigFrequencyTable,'arrisQamDetectionConfigFrequencyEntry':arrisQamDetectionConfigFrequencyEntry,_E:arrisQamDetectionConfigFrequencyIndex,'arrisQamDetectionConfigFrequency':arrisQamDetectionConfigFrequency,'arrisQamDetectionConfigClearResults':arrisQamDetectionConfigClearResults,'arrisQamDetectionResultsTable':arrisQamDetectionResultsTable,'arrisQamDetectionResultsEntry':arrisQamDetectionResultsEntry,_G:arrisQamDetectionResultsIndex,'arrisQamDetectionResultsFreq':arrisQamDetectionResultsFreq,'arrisQamDetectionResultsTimestamp':arrisQamDetectionResultsTimestamp})