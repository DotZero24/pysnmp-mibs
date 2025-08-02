_T='oduiPmRealGroup'
_S='oduiPmGroup'
_R='oduiPmRealRxDefectSecondsFEND'
_Q='oduiPmRealRxDefectSeconds'
_P='oduiPmRxDefectSecondsFEND'
_O='oduiPmPayloadType'
_N='oduiPmCircuitId'
_M='oduiPmRxDefectSeconds'
_L='oduiPmValidity'
_K='not-accessible'
_J='Integer32'
_I='oduiPmRealRxBEICount'
_H='oduiPmRealRxCVP'
_G='oduiPmTimestamp'
_F='oduiPmSampleDuration'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-ODUI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HCPerfIntervalCount,=mibBuilder.importSymbols('HC-PerfHist-TC-MIB','HCPerfIntervalCount')
ifIndex,=mibBuilder.importSymbols(_D,_E)
perfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','perfMon')
InfnSampleDuration,InfnServiceType,InfnValidityBitmap=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnSampleDuration','InfnServiceType','InfnValidityBitmap')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
oduiPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,29))
if mibBuilder.loadTexts:oduiPmMIB.setRevisions(('2009-07-20 00:00',))
_OduiPmRealTable_Object=MibTable
oduiPmRealTable=_OduiPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,29,1))
if mibBuilder.loadTexts:oduiPmRealTable.setStatus(_A)
_OduiPmRealEntry_Object=MibTableRow
oduiPmRealEntry=_OduiPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,29,1,1))
oduiPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:oduiPmRealEntry.setStatus(_A)
_OduiPmRealRxDefectSeconds_Type=Integer32
_OduiPmRealRxDefectSeconds_Object=MibTableColumn
oduiPmRealRxDefectSeconds=_OduiPmRealRxDefectSeconds_Object((1,3,6,1,4,1,21296,2,2,2,3,29,1,1,1),_OduiPmRealRxDefectSeconds_Type())
oduiPmRealRxDefectSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiPmRealRxDefectSeconds.setStatus(_A)
_OduiPmRealRxDefectSecondsFEND_Type=Integer32
_OduiPmRealRxDefectSecondsFEND_Object=MibTableColumn
oduiPmRealRxDefectSecondsFEND=_OduiPmRealRxDefectSecondsFEND_Object((1,3,6,1,4,1,21296,2,2,2,3,29,1,1,2),_OduiPmRealRxDefectSecondsFEND_Type())
oduiPmRealRxDefectSecondsFEND.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiPmRealRxDefectSecondsFEND.setStatus(_A)
_OduiPmRealRxCVP_Type=HCPerfIntervalCount
_OduiPmRealRxCVP_Object=MibTableColumn
oduiPmRealRxCVP=_OduiPmRealRxCVP_Object((1,3,6,1,4,1,21296,2,2,2,3,29,1,1,3),_OduiPmRealRxCVP_Type())
oduiPmRealRxCVP.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiPmRealRxCVP.setStatus(_A)
_OduiPmRealRxBEICount_Type=HCPerfIntervalCount
_OduiPmRealRxBEICount_Object=MibTableColumn
oduiPmRealRxBEICount=_OduiPmRealRxBEICount_Object((1,3,6,1,4,1,21296,2,2,2,3,29,1,1,4),_OduiPmRealRxBEICount_Type())
oduiPmRealRxBEICount.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiPmRealRxBEICount.setStatus(_A)
_OduiPmTable_Object=MibTable
oduiPmTable=_OduiPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,29,2))
if mibBuilder.loadTexts:oduiPmTable.setStatus(_A)
_OduiPmEntry_Object=MibTableRow
oduiPmEntry=_OduiPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,29,2,1))
oduiPmEntry.setIndexNames((0,_D,_E),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:oduiPmEntry.setStatus(_A)
class _OduiPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OduiPmTimestamp_Type.__name__=_J
_OduiPmTimestamp_Object=MibTableColumn
oduiPmTimestamp=_OduiPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,29,2,1,1),_OduiPmTimestamp_Type())
oduiPmTimestamp.setMaxAccess(_K)
if mibBuilder.loadTexts:oduiPmTimestamp.setStatus(_A)
_OduiPmSampleDuration_Type=InfnSampleDuration
_OduiPmSampleDuration_Object=MibTableColumn
oduiPmSampleDuration=_OduiPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,29,2,1,2),_OduiPmSampleDuration_Type())
oduiPmSampleDuration.setMaxAccess(_K)
if mibBuilder.loadTexts:oduiPmSampleDuration.setStatus(_A)
_OduiPmValidity_Type=InfnValidityBitmap
_OduiPmValidity_Object=MibTableColumn
oduiPmValidity=_OduiPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,29,2,1,3),_OduiPmValidity_Type())
oduiPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiPmValidity.setStatus(_A)
_OduiPmRxDefectSeconds_Type=Integer32
_OduiPmRxDefectSeconds_Object=MibTableColumn
oduiPmRxDefectSeconds=_OduiPmRxDefectSeconds_Object((1,3,6,1,4,1,21296,2,2,2,3,29,2,1,4),_OduiPmRxDefectSeconds_Type())
oduiPmRxDefectSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiPmRxDefectSeconds.setStatus(_A)
_OduiPmCircuitId_Type=DisplayString
_OduiPmCircuitId_Object=MibTableColumn
oduiPmCircuitId=_OduiPmCircuitId_Object((1,3,6,1,4,1,21296,2,2,2,3,29,2,1,5),_OduiPmCircuitId_Type())
oduiPmCircuitId.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiPmCircuitId.setStatus(_A)
_OduiPmPayloadType_Type=InfnServiceType
_OduiPmPayloadType_Object=MibTableColumn
oduiPmPayloadType=_OduiPmPayloadType_Object((1,3,6,1,4,1,21296,2,2,2,3,29,2,1,6),_OduiPmPayloadType_Type())
oduiPmPayloadType.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiPmPayloadType.setStatus(_A)
_OduiPmRxDefectSecondsFEND_Type=Integer32
_OduiPmRxDefectSecondsFEND_Object=MibTableColumn
oduiPmRxDefectSecondsFEND=_OduiPmRxDefectSecondsFEND_Object((1,3,6,1,4,1,21296,2,2,2,3,29,2,1,7),_OduiPmRxDefectSecondsFEND_Type())
oduiPmRxDefectSecondsFEND.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiPmRxDefectSecondsFEND.setStatus(_A)
_OduiPmRxCVP_Type=HCPerfIntervalCount
_OduiPmRxCVP_Object=MibTableColumn
oduiPmRxCVP=_OduiPmRxCVP_Object((1,3,6,1,4,1,21296,2,2,2,3,29,2,1,8),_OduiPmRxCVP_Type())
oduiPmRxCVP.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiPmRxCVP.setStatus(_A)
_OduiPmRxBEICount_Type=HCPerfIntervalCount
_OduiPmRxBEICount_Object=MibTableColumn
oduiPmRxBEICount=_OduiPmRxBEICount_Object((1,3,6,1,4,1,21296,2,2,2,3,29,2,1,9),_OduiPmRxBEICount_Type())
oduiPmRxBEICount.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiPmRxBEICount.setStatus(_A)
_OduiPmConformance_ObjectIdentity=ObjectIdentity
oduiPmConformance=_OduiPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,29,3))
_OduiPmCompliances_ObjectIdentity=ObjectIdentity
oduiPmCompliances=_OduiPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,29,3,1))
_OduiPmGroups_ObjectIdentity=ObjectIdentity
oduiPmGroups=_OduiPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,29,3,2))
oduiPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,29,3,2,1))
oduiPmGroup.setObjects(*((_B,_G),(_B,_F),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:oduiPmGroup.setStatus(_A)
oduiPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,29,3,2,2))
oduiPmRealGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:oduiPmRealGroup.setStatus(_A)
oduiPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,29,3,1,1))
oduiPmCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:oduiPmCompliance.setStatus(_A)
oduiPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,29,3,1,2))
oduiPmRealCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:oduiPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'oduiPmMIB':oduiPmMIB,'oduiPmRealTable':oduiPmRealTable,'oduiPmRealEntry':oduiPmRealEntry,_Q:oduiPmRealRxDefectSeconds,_R:oduiPmRealRxDefectSecondsFEND,_H:oduiPmRealRxCVP,_I:oduiPmRealRxBEICount,'oduiPmTable':oduiPmTable,'oduiPmEntry':oduiPmEntry,_G:oduiPmTimestamp,_F:oduiPmSampleDuration,_L:oduiPmValidity,_M:oduiPmRxDefectSeconds,_N:oduiPmCircuitId,_O:oduiPmPayloadType,_P:oduiPmRxDefectSecondsFEND,'oduiPmRxCVP':oduiPmRxCVP,'oduiPmRxBEICount':oduiPmRxBEICount,'oduiPmConformance':oduiPmConformance,'oduiPmCompliances':oduiPmCompliances,'oduiPmCompliance':oduiPmCompliance,'oduiPmRealCompliance':oduiPmRealCompliance,'oduiPmGroups':oduiPmGroups,_S:oduiPmGroup,_T:oduiPmRealGroup})