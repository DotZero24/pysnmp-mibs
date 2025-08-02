_X='oduKtPmRealGroup'
_W='oduKtPmGroup'
_V='oduKtPmRealDefectSecondsFEND'
_U='oduKtPmRealDefectSeconds'
_T='oduKtPmRealBEICount'
_S='oduKtPmRealErroredBlocks'
_R='oduKtPmRealCVT'
_Q='oduKtPmDefectSecondsFEND'
_P='oduKtPmPayloadType'
_O='oduKtPmCircuitId'
_N='oduKtPmDefectSeconds'
_M='oduKtPmBEICount'
_L='oduKtPmErroredBlocks'
_K='oduKtPmCVT'
_J='oduKtPmValidity'
_I='not-accessible'
_H='Integer32'
_G='oduKtPmTimestamp'
_F='oduKtPmSampleDuration'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-ODUKT-MIB'
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
oduKtPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,21))
if mibBuilder.loadTexts:oduKtPmMIB.setRevisions(('2009-07-20 00:00',))
_OduKtPmRealTable_Object=MibTable
oduKtPmRealTable=_OduKtPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,21,1))
if mibBuilder.loadTexts:oduKtPmRealTable.setStatus(_A)
_OduKtPmRealEntry_Object=MibTableRow
oduKtPmRealEntry=_OduKtPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,21,1,1))
oduKtPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:oduKtPmRealEntry.setStatus(_A)
_OduKtPmRealCVT_Type=HCPerfIntervalCount
_OduKtPmRealCVT_Object=MibTableColumn
oduKtPmRealCVT=_OduKtPmRealCVT_Object((1,3,6,1,4,1,21296,2,2,2,3,21,1,1,1),_OduKtPmRealCVT_Type())
oduKtPmRealCVT.setMaxAccess(_C)
if mibBuilder.loadTexts:oduKtPmRealCVT.setStatus(_A)
_OduKtPmRealErroredBlocks_Type=HCPerfIntervalCount
_OduKtPmRealErroredBlocks_Object=MibTableColumn
oduKtPmRealErroredBlocks=_OduKtPmRealErroredBlocks_Object((1,3,6,1,4,1,21296,2,2,2,3,21,1,1,2),_OduKtPmRealErroredBlocks_Type())
oduKtPmRealErroredBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:oduKtPmRealErroredBlocks.setStatus(_A)
_OduKtPmRealBEICount_Type=HCPerfIntervalCount
_OduKtPmRealBEICount_Object=MibTableColumn
oduKtPmRealBEICount=_OduKtPmRealBEICount_Object((1,3,6,1,4,1,21296,2,2,2,3,21,1,1,3),_OduKtPmRealBEICount_Type())
oduKtPmRealBEICount.setMaxAccess(_C)
if mibBuilder.loadTexts:oduKtPmRealBEICount.setStatus(_A)
_OduKtPmRealDefectSeconds_Type=Integer32
_OduKtPmRealDefectSeconds_Object=MibTableColumn
oduKtPmRealDefectSeconds=_OduKtPmRealDefectSeconds_Object((1,3,6,1,4,1,21296,2,2,2,3,21,1,1,4),_OduKtPmRealDefectSeconds_Type())
oduKtPmRealDefectSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:oduKtPmRealDefectSeconds.setStatus(_A)
_OduKtPmRealDefectSecondsFEND_Type=Integer32
_OduKtPmRealDefectSecondsFEND_Object=MibTableColumn
oduKtPmRealDefectSecondsFEND=_OduKtPmRealDefectSecondsFEND_Object((1,3,6,1,4,1,21296,2,2,2,3,21,1,1,5),_OduKtPmRealDefectSecondsFEND_Type())
oduKtPmRealDefectSecondsFEND.setMaxAccess(_C)
if mibBuilder.loadTexts:oduKtPmRealDefectSecondsFEND.setStatus(_A)
_OduKtPmTable_Object=MibTable
oduKtPmTable=_OduKtPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,21,2))
if mibBuilder.loadTexts:oduKtPmTable.setStatus(_A)
_OduKtPmEntry_Object=MibTableRow
oduKtPmEntry=_OduKtPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,21,2,1))
oduKtPmEntry.setIndexNames((0,_D,_E),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:oduKtPmEntry.setStatus(_A)
class _OduKtPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OduKtPmTimestamp_Type.__name__=_H
_OduKtPmTimestamp_Object=MibTableColumn
oduKtPmTimestamp=_OduKtPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,21,2,1,1),_OduKtPmTimestamp_Type())
oduKtPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:oduKtPmTimestamp.setStatus(_A)
_OduKtPmSampleDuration_Type=InfnSampleDuration
_OduKtPmSampleDuration_Object=MibTableColumn
oduKtPmSampleDuration=_OduKtPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,21,2,1,2),_OduKtPmSampleDuration_Type())
oduKtPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:oduKtPmSampleDuration.setStatus(_A)
_OduKtPmValidity_Type=TruthValue
_OduKtPmValidity_Object=MibTableColumn
oduKtPmValidity=_OduKtPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,21,2,1,3),_OduKtPmValidity_Type())
oduKtPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:oduKtPmValidity.setStatus(_A)
_OduKtPmCVT_Type=HCPerfIntervalCount
_OduKtPmCVT_Object=MibTableColumn
oduKtPmCVT=_OduKtPmCVT_Object((1,3,6,1,4,1,21296,2,2,2,3,21,2,1,4),_OduKtPmCVT_Type())
oduKtPmCVT.setMaxAccess(_C)
if mibBuilder.loadTexts:oduKtPmCVT.setStatus(_A)
_OduKtPmErroredBlocks_Type=HCPerfIntervalCount
_OduKtPmErroredBlocks_Object=MibTableColumn
oduKtPmErroredBlocks=_OduKtPmErroredBlocks_Object((1,3,6,1,4,1,21296,2,2,2,3,21,2,1,5),_OduKtPmErroredBlocks_Type())
oduKtPmErroredBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:oduKtPmErroredBlocks.setStatus(_A)
_OduKtPmBEICount_Type=HCPerfIntervalCount
_OduKtPmBEICount_Object=MibTableColumn
oduKtPmBEICount=_OduKtPmBEICount_Object((1,3,6,1,4,1,21296,2,2,2,3,21,2,1,6),_OduKtPmBEICount_Type())
oduKtPmBEICount.setMaxAccess(_C)
if mibBuilder.loadTexts:oduKtPmBEICount.setStatus(_A)
_OduKtPmDefectSeconds_Type=Integer32
_OduKtPmDefectSeconds_Object=MibTableColumn
oduKtPmDefectSeconds=_OduKtPmDefectSeconds_Object((1,3,6,1,4,1,21296,2,2,2,3,21,2,1,7),_OduKtPmDefectSeconds_Type())
oduKtPmDefectSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:oduKtPmDefectSeconds.setStatus(_A)
_OduKtPmCircuitId_Type=DisplayString
_OduKtPmCircuitId_Object=MibTableColumn
oduKtPmCircuitId=_OduKtPmCircuitId_Object((1,3,6,1,4,1,21296,2,2,2,3,21,2,1,8),_OduKtPmCircuitId_Type())
oduKtPmCircuitId.setMaxAccess(_C)
if mibBuilder.loadTexts:oduKtPmCircuitId.setStatus(_A)
_OduKtPmPayloadType_Type=InfnServiceType
_OduKtPmPayloadType_Object=MibTableColumn
oduKtPmPayloadType=_OduKtPmPayloadType_Object((1,3,6,1,4,1,21296,2,2,2,3,21,2,1,9),_OduKtPmPayloadType_Type())
oduKtPmPayloadType.setMaxAccess(_C)
if mibBuilder.loadTexts:oduKtPmPayloadType.setStatus(_A)
_OduKtPmDefectSecondsFEND_Type=Integer32
_OduKtPmDefectSecondsFEND_Object=MibTableColumn
oduKtPmDefectSecondsFEND=_OduKtPmDefectSecondsFEND_Object((1,3,6,1,4,1,21296,2,2,2,3,21,2,1,10),_OduKtPmDefectSecondsFEND_Type())
oduKtPmDefectSecondsFEND.setMaxAccess(_C)
if mibBuilder.loadTexts:oduKtPmDefectSecondsFEND.setStatus(_A)
_OduKtPmConformance_ObjectIdentity=ObjectIdentity
oduKtPmConformance=_OduKtPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,21,3))
_OduKtPmCompliances_ObjectIdentity=ObjectIdentity
oduKtPmCompliances=_OduKtPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,21,3,1))
_OduKtPmGroups_ObjectIdentity=ObjectIdentity
oduKtPmGroups=_OduKtPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,21,3,2))
oduKtPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,21,3,2,1))
oduKtPmGroup.setObjects(*((_B,_G),(_B,_F),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:oduKtPmGroup.setStatus(_A)
oduKtPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,21,3,2,2))
oduKtPmRealGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:oduKtPmRealGroup.setStatus(_A)
oduKtPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,21,3,1,1))
oduKtPmCompliance.setObjects((_B,_W))
if mibBuilder.loadTexts:oduKtPmCompliance.setStatus(_A)
oduKtPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,21,3,1,2))
oduKtPmRealCompliance.setObjects((_B,_X))
if mibBuilder.loadTexts:oduKtPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'oduKtPmMIB':oduKtPmMIB,'oduKtPmRealTable':oduKtPmRealTable,'oduKtPmRealEntry':oduKtPmRealEntry,_R:oduKtPmRealCVT,_S:oduKtPmRealErroredBlocks,_T:oduKtPmRealBEICount,_U:oduKtPmRealDefectSeconds,_V:oduKtPmRealDefectSecondsFEND,'oduKtPmTable':oduKtPmTable,'oduKtPmEntry':oduKtPmEntry,_G:oduKtPmTimestamp,_F:oduKtPmSampleDuration,_J:oduKtPmValidity,_K:oduKtPmCVT,_L:oduKtPmErroredBlocks,_M:oduKtPmBEICount,_N:oduKtPmDefectSeconds,_O:oduKtPmCircuitId,_P:oduKtPmPayloadType,_Q:oduKtPmDefectSecondsFEND,'oduKtPmConformance':oduKtPmConformance,'oduKtPmCompliances':oduKtPmCompliances,'oduKtPmCompliance':oduKtPmCompliance,'oduKtPmRealCompliance':oduKtPmRealCompliance,'oduKtPmGroups':oduKtPmGroups,_W:oduKtPmGroup,_X:oduKtPmRealGroup})