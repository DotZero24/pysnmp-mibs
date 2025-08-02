_V='oduiKtPmRealGroup'
_U='oduiKtPmGroup'
_T='oduiKtPmRealDefectSeconds'
_S='oduiKtPmRealBEICount'
_R='oduiKtPmRealErroredBlocks'
_Q='oduiKtPmRealCVT'
_P='oduiKtPmPayloadType'
_O='oduiKtPmCircuitId'
_N='oduiKtPmDefectSeconds'
_M='oduiKtPmBEICount'
_L='oduiKtPmErroredBlocks'
_K='oduiKtPmCVT'
_J='oduiKtPmValidity'
_I='not-accessible'
_H='Integer32'
_G='oduiKtPmTimestamp'
_F='oduiKtPmSampleDuration'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-ODUKTI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HCPerfIntervalCount,=mibBuilder.importSymbols('HC-PerfHist-TC-MIB','HCPerfIntervalCount')
ifIndex,=mibBuilder.importSymbols(_D,_E)
perfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','perfMon')
InfnSampleDuration,InfnServiceType=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnSampleDuration','InfnServiceType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
oduiKtPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,31))
if mibBuilder.loadTexts:oduiKtPmMIB.setRevisions(('2011-10-20 00:00',))
_OduiKtPmRealTable_Object=MibTable
oduiKtPmRealTable=_OduiKtPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,31,1))
if mibBuilder.loadTexts:oduiKtPmRealTable.setStatus(_A)
_OduiKtPmRealEntry_Object=MibTableRow
oduiKtPmRealEntry=_OduiKtPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,31,1,1))
oduiKtPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:oduiKtPmRealEntry.setStatus(_A)
_OduiKtPmRealCVT_Type=HCPerfIntervalCount
_OduiKtPmRealCVT_Object=MibTableColumn
oduiKtPmRealCVT=_OduiKtPmRealCVT_Object((1,3,6,1,4,1,21296,2,2,2,3,31,1,1,1),_OduiKtPmRealCVT_Type())
oduiKtPmRealCVT.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiKtPmRealCVT.setStatus(_A)
_OduiKtPmRealErroredBlocks_Type=HCPerfIntervalCount
_OduiKtPmRealErroredBlocks_Object=MibTableColumn
oduiKtPmRealErroredBlocks=_OduiKtPmRealErroredBlocks_Object((1,3,6,1,4,1,21296,2,2,2,3,31,1,1,2),_OduiKtPmRealErroredBlocks_Type())
oduiKtPmRealErroredBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiKtPmRealErroredBlocks.setStatus(_A)
_OduiKtPmRealBEICount_Type=HCPerfIntervalCount
_OduiKtPmRealBEICount_Object=MibTableColumn
oduiKtPmRealBEICount=_OduiKtPmRealBEICount_Object((1,3,6,1,4,1,21296,2,2,2,3,31,1,1,3),_OduiKtPmRealBEICount_Type())
oduiKtPmRealBEICount.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiKtPmRealBEICount.setStatus(_A)
_OduiKtPmRealDefectSeconds_Type=Integer32
_OduiKtPmRealDefectSeconds_Object=MibTableColumn
oduiKtPmRealDefectSeconds=_OduiKtPmRealDefectSeconds_Object((1,3,6,1,4,1,21296,2,2,2,3,31,1,1,4),_OduiKtPmRealDefectSeconds_Type())
oduiKtPmRealDefectSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiKtPmRealDefectSeconds.setStatus(_A)
_OduiKtPmTable_Object=MibTable
oduiKtPmTable=_OduiKtPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,31,2))
if mibBuilder.loadTexts:oduiKtPmTable.setStatus(_A)
_OduiKtPmEntry_Object=MibTableRow
oduiKtPmEntry=_OduiKtPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,31,2,1))
oduiKtPmEntry.setIndexNames((0,_D,_E),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:oduiKtPmEntry.setStatus(_A)
class _OduiKtPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OduiKtPmTimestamp_Type.__name__=_H
_OduiKtPmTimestamp_Object=MibTableColumn
oduiKtPmTimestamp=_OduiKtPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,31,2,1,1),_OduiKtPmTimestamp_Type())
oduiKtPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:oduiKtPmTimestamp.setStatus(_A)
_OduiKtPmSampleDuration_Type=InfnSampleDuration
_OduiKtPmSampleDuration_Object=MibTableColumn
oduiKtPmSampleDuration=_OduiKtPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,31,2,1,2),_OduiKtPmSampleDuration_Type())
oduiKtPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:oduiKtPmSampleDuration.setStatus(_A)
_OduiKtPmValidity_Type=TruthValue
_OduiKtPmValidity_Object=MibTableColumn
oduiKtPmValidity=_OduiKtPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,31,2,1,3),_OduiKtPmValidity_Type())
oduiKtPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiKtPmValidity.setStatus(_A)
_OduiKtPmCVT_Type=HCPerfIntervalCount
_OduiKtPmCVT_Object=MibTableColumn
oduiKtPmCVT=_OduiKtPmCVT_Object((1,3,6,1,4,1,21296,2,2,2,3,31,2,1,4),_OduiKtPmCVT_Type())
oduiKtPmCVT.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiKtPmCVT.setStatus(_A)
_OduiKtPmErroredBlocks_Type=HCPerfIntervalCount
_OduiKtPmErroredBlocks_Object=MibTableColumn
oduiKtPmErroredBlocks=_OduiKtPmErroredBlocks_Object((1,3,6,1,4,1,21296,2,2,2,3,31,2,1,5),_OduiKtPmErroredBlocks_Type())
oduiKtPmErroredBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiKtPmErroredBlocks.setStatus(_A)
_OduiKtPmBEICount_Type=HCPerfIntervalCount
_OduiKtPmBEICount_Object=MibTableColumn
oduiKtPmBEICount=_OduiKtPmBEICount_Object((1,3,6,1,4,1,21296,2,2,2,3,31,2,1,6),_OduiKtPmBEICount_Type())
oduiKtPmBEICount.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiKtPmBEICount.setStatus(_A)
_OduiKtPmDefectSeconds_Type=Integer32
_OduiKtPmDefectSeconds_Object=MibTableColumn
oduiKtPmDefectSeconds=_OduiKtPmDefectSeconds_Object((1,3,6,1,4,1,21296,2,2,2,3,31,2,1,7),_OduiKtPmDefectSeconds_Type())
oduiKtPmDefectSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiKtPmDefectSeconds.setStatus(_A)
_OduiKtPmCircuitId_Type=DisplayString
_OduiKtPmCircuitId_Object=MibTableColumn
oduiKtPmCircuitId=_OduiKtPmCircuitId_Object((1,3,6,1,4,1,21296,2,2,2,3,31,2,1,8),_OduiKtPmCircuitId_Type())
oduiKtPmCircuitId.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiKtPmCircuitId.setStatus(_A)
_OduiKtPmPayloadType_Type=InfnServiceType
_OduiKtPmPayloadType_Object=MibTableColumn
oduiKtPmPayloadType=_OduiKtPmPayloadType_Object((1,3,6,1,4,1,21296,2,2,2,3,31,2,1,9),_OduiKtPmPayloadType_Type())
oduiKtPmPayloadType.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiKtPmPayloadType.setStatus(_A)
_OduiKtPmConformance_ObjectIdentity=ObjectIdentity
oduiKtPmConformance=_OduiKtPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,31,3))
_OduiKtPmCompliances_ObjectIdentity=ObjectIdentity
oduiKtPmCompliances=_OduiKtPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,31,3,1))
_OduiKtPmGroups_ObjectIdentity=ObjectIdentity
oduiKtPmGroups=_OduiKtPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,31,3,2))
oduiKtPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,31,3,2,1))
oduiKtPmGroup.setObjects(*((_B,_G),(_B,_F),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:oduiKtPmGroup.setStatus(_A)
oduiKtPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,31,3,2,2))
oduiKtPmRealGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:oduiKtPmRealGroup.setStatus(_A)
oduiKtPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,31,3,1,1))
oduiKtPmCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:oduiKtPmCompliance.setStatus(_A)
oduiKtPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,31,3,1,2))
oduiKtPmRealCompliance.setObjects((_B,_V))
if mibBuilder.loadTexts:oduiKtPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'oduiKtPmMIB':oduiKtPmMIB,'oduiKtPmRealTable':oduiKtPmRealTable,'oduiKtPmRealEntry':oduiKtPmRealEntry,_Q:oduiKtPmRealCVT,_R:oduiKtPmRealErroredBlocks,_S:oduiKtPmRealBEICount,_T:oduiKtPmRealDefectSeconds,'oduiKtPmTable':oduiKtPmTable,'oduiKtPmEntry':oduiKtPmEntry,_G:oduiKtPmTimestamp,_F:oduiKtPmSampleDuration,_J:oduiKtPmValidity,_K:oduiKtPmCVT,_L:oduiKtPmErroredBlocks,_M:oduiKtPmBEICount,_N:oduiKtPmDefectSeconds,_O:oduiKtPmCircuitId,_P:oduiKtPmPayloadType,'oduiKtPmConformance':oduiKtPmConformance,'oduiKtPmCompliances':oduiKtPmCompliances,'oduiKtPmCompliance':oduiKtPmCompliance,'oduiKtPmRealCompliance':oduiKtPmRealCompliance,'oduiKtPmGroups':oduiKtPmGroups,_U:oduiKtPmGroup,_V:oduiKtPmRealGroup})