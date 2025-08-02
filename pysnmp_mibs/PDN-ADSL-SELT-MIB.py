_Z='pdnAdslSeltLnfGroup'
_Y='pdnAdslSeltLcGroup'
_X='pdnAdslSeltGroup'
_W='pdnAdslSeltLnfSignalPsd'
_V='pdnAdslSeltLnfTotalPsd'
_U='pdnAdslSeltLnfPeakPsd'
_T='pdnAdslSeltLcSegmentType'
_S='pdnAdslSeltLcSegmentGauge'
_R='pdnAdslSeltLcSegmentLength'
_Q='pdnAdslSeltTimeLeft'
_P='pdnAdslSeltDuration'
_O='pdnAdslSeltWireSize'
_N='pdnAdslSeltStatus'
_M='pdnAdslSeltCmd'
_L='pdnAdslSeltLnfSubCarrierIndex'
_K='pdnAdslSeltLcSegmentIndex'
_J='seconds'
_I='pdnAdslSeltType'
_H='not-accessible'
_G='read-write'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='Integer32'
_B='PDN-ADSL-SELT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
pdn_interfaces,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-interfaces')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pdnAdslSeltMIB=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,6,31))
if mibBuilder.loadTexts:pdnAdslSeltMIB.setRevisions(('2005-03-28 00:00','2005-03-10 00:00','2004-12-02 00:00'))
class PdnSeltTypes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('loopCharacterization',1),('loopNoiseFloor',2)))
_PdnAdslSeltNotifications_ObjectIdentity=ObjectIdentity
pdnAdslSeltNotifications=_PdnAdslSeltNotifications_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,31,0))
_PdnAdslSeltObjects_ObjectIdentity=ObjectIdentity
pdnAdslSeltObjects=_PdnAdslSeltObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,31,1))
class _PdnAdslSeltWireSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('awg',1),('metric',2),('metricJapan',3)))
_PdnAdslSeltWireSize_Type.__name__=_C
_PdnAdslSeltWireSize_Object=MibScalar
pdnAdslSeltWireSize=_PdnAdslSeltWireSize_Object((1,3,6,1,4,1,1795,2,24,2,6,31,1,1),_PdnAdslSeltWireSize_Type())
pdnAdslSeltWireSize.setMaxAccess(_G)
if mibBuilder.loadTexts:pdnAdslSeltWireSize.setStatus(_A)
_PdnAdslSeltTable_Object=MibTable
pdnAdslSeltTable=_PdnAdslSeltTable_Object((1,3,6,1,4,1,1795,2,24,2,6,31,1,2))
if mibBuilder.loadTexts:pdnAdslSeltTable.setStatus(_A)
_PdnAdslSeltEntry_Object=MibTableRow
pdnAdslSeltEntry=_PdnAdslSeltEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,31,1,2,1))
pdnAdslSeltEntry.setIndexNames((0,_E,_F),(0,_B,_I))
if mibBuilder.loadTexts:pdnAdslSeltEntry.setStatus(_A)
_PdnAdslSeltType_Type=PdnSeltTypes
_PdnAdslSeltType_Object=MibTableColumn
pdnAdslSeltType=_PdnAdslSeltType_Object((1,3,6,1,4,1,1795,2,24,2,6,31,1,2,1,1),_PdnAdslSeltType_Type())
pdnAdslSeltType.setMaxAccess(_H)
if mibBuilder.loadTexts:pdnAdslSeltType.setStatus(_A)
class _PdnAdslSeltCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noOp',1),('start',2),('stop',3),('clearResults',4)))
_PdnAdslSeltCmd_Type.__name__=_C
_PdnAdslSeltCmd_Object=MibTableColumn
pdnAdslSeltCmd=_PdnAdslSeltCmd_Object((1,3,6,1,4,1,1795,2,24,2,6,31,1,2,1,2),_PdnAdslSeltCmd_Type())
pdnAdslSeltCmd.setMaxAccess(_G)
if mibBuilder.loadTexts:pdnAdslSeltCmd.setStatus(_A)
class _PdnAdslSeltStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('inProgress',1),('stoppedInProgress',2),('complete',3),('notStarted',4),('resultsCleared',5)))
_PdnAdslSeltStatus_Type.__name__=_C
_PdnAdslSeltStatus_Object=MibTableColumn
pdnAdslSeltStatus=_PdnAdslSeltStatus_Object((1,3,6,1,4,1,1795,2,24,2,6,31,1,2,1,3),_PdnAdslSeltStatus_Type())
pdnAdslSeltStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnAdslSeltStatus.setStatus(_A)
_PdnAdslSeltDuration_Type=Unsigned32
_PdnAdslSeltDuration_Object=MibTableColumn
pdnAdslSeltDuration=_PdnAdslSeltDuration_Object((1,3,6,1,4,1,1795,2,24,2,6,31,1,2,1,4),_PdnAdslSeltDuration_Type())
pdnAdslSeltDuration.setMaxAccess(_G)
if mibBuilder.loadTexts:pdnAdslSeltDuration.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslSeltDuration.setUnits(_J)
_PdnAdslSeltTimeLeft_Type=Unsigned32
_PdnAdslSeltTimeLeft_Object=MibTableColumn
pdnAdslSeltTimeLeft=_PdnAdslSeltTimeLeft_Object((1,3,6,1,4,1,1795,2,24,2,6,31,1,2,1,5),_PdnAdslSeltTimeLeft_Type())
pdnAdslSeltTimeLeft.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnAdslSeltTimeLeft.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslSeltTimeLeft.setUnits(_J)
_PdnAdslSeltLcTable_Object=MibTable
pdnAdslSeltLcTable=_PdnAdslSeltLcTable_Object((1,3,6,1,4,1,1795,2,24,2,6,31,1,3))
if mibBuilder.loadTexts:pdnAdslSeltLcTable.setStatus(_A)
_PdnAdslSeltLcEntry_Object=MibTableRow
pdnAdslSeltLcEntry=_PdnAdslSeltLcEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,31,1,3,1))
pdnAdslSeltLcEntry.setIndexNames((0,_E,_F),(0,_B,_K))
if mibBuilder.loadTexts:pdnAdslSeltLcEntry.setStatus(_A)
class _PdnAdslSeltLcSegmentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_PdnAdslSeltLcSegmentIndex_Type.__name__=_C
_PdnAdslSeltLcSegmentIndex_Object=MibTableColumn
pdnAdslSeltLcSegmentIndex=_PdnAdslSeltLcSegmentIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,31,1,3,1,1),_PdnAdslSeltLcSegmentIndex_Type())
pdnAdslSeltLcSegmentIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:pdnAdslSeltLcSegmentIndex.setStatus(_A)
class _PdnAdslSeltLcSegmentLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_PdnAdslSeltLcSegmentLength_Type.__name__=_C
_PdnAdslSeltLcSegmentLength_Object=MibTableColumn
pdnAdslSeltLcSegmentLength=_PdnAdslSeltLcSegmentLength_Object((1,3,6,1,4,1,1795,2,24,2,6,31,1,3,1,2),_PdnAdslSeltLcSegmentLength_Type())
pdnAdslSeltLcSegmentLength.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnAdslSeltLcSegmentLength.setStatus(_A)
class _PdnAdslSeltLcSegmentGauge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,10,11,12,13,14,20,21,22,23,24)));namedValues=NamedValues(*(('unknown',1),('awg26',2),('awg24',3),('awg22',4),('awg19',5),('metric32',10),('metric40',11),('metric50',12),('metric63',13),('metric90',14),('metricJapan32',20),('metricJapan40',21),('metricJapan50',22),('metricJapan65',23),('metricJapan90',24)))
_PdnAdslSeltLcSegmentGauge_Type.__name__=_C
_PdnAdslSeltLcSegmentGauge_Object=MibTableColumn
pdnAdslSeltLcSegmentGauge=_PdnAdslSeltLcSegmentGauge_Object((1,3,6,1,4,1,1795,2,24,2,6,31,1,3,1,3),_PdnAdslSeltLcSegmentGauge_Type())
pdnAdslSeltLcSegmentGauge.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnAdslSeltLcSegmentGauge.setStatus(_A)
class _PdnAdslSeltLcSegmentType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notPresent',1),('inline',2),('bridgeTap',3)))
_PdnAdslSeltLcSegmentType_Type.__name__=_C
_PdnAdslSeltLcSegmentType_Object=MibTableColumn
pdnAdslSeltLcSegmentType=_PdnAdslSeltLcSegmentType_Object((1,3,6,1,4,1,1795,2,24,2,6,31,1,3,1,4),_PdnAdslSeltLcSegmentType_Type())
pdnAdslSeltLcSegmentType.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnAdslSeltLcSegmentType.setStatus(_A)
_PdnAdslSeltLnfTable_Object=MibTable
pdnAdslSeltLnfTable=_PdnAdslSeltLnfTable_Object((1,3,6,1,4,1,1795,2,24,2,6,31,1,4))
if mibBuilder.loadTexts:pdnAdslSeltLnfTable.setStatus(_A)
_PdnAdslSeltLnfEntry_Object=MibTableRow
pdnAdslSeltLnfEntry=_PdnAdslSeltLnfEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,31,1,4,1))
pdnAdslSeltLnfEntry.setIndexNames((0,_E,_F),(0,_B,_L))
if mibBuilder.loadTexts:pdnAdslSeltLnfEntry.setStatus(_A)
class _PdnAdslSeltLnfSubCarrierIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_PdnAdslSeltLnfSubCarrierIndex_Type.__name__=_C
_PdnAdslSeltLnfSubCarrierIndex_Object=MibTableColumn
pdnAdslSeltLnfSubCarrierIndex=_PdnAdslSeltLnfSubCarrierIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,31,1,4,1,1),_PdnAdslSeltLnfSubCarrierIndex_Type())
pdnAdslSeltLnfSubCarrierIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:pdnAdslSeltLnfSubCarrierIndex.setStatus(_A)
class _PdnAdslSeltLnfPeakPsd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_PdnAdslSeltLnfPeakPsd_Type.__name__=_C
_PdnAdslSeltLnfPeakPsd_Object=MibTableColumn
pdnAdslSeltLnfPeakPsd=_PdnAdslSeltLnfPeakPsd_Object((1,3,6,1,4,1,1795,2,24,2,6,31,1,4,1,2),_PdnAdslSeltLnfPeakPsd_Type())
pdnAdslSeltLnfPeakPsd.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnAdslSeltLnfPeakPsd.setStatus(_A)
class _PdnAdslSeltLnfTotalPsd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_PdnAdslSeltLnfTotalPsd_Type.__name__=_C
_PdnAdslSeltLnfTotalPsd_Object=MibTableColumn
pdnAdslSeltLnfTotalPsd=_PdnAdslSeltLnfTotalPsd_Object((1,3,6,1,4,1,1795,2,24,2,6,31,1,4,1,3),_PdnAdslSeltLnfTotalPsd_Type())
pdnAdslSeltLnfTotalPsd.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnAdslSeltLnfTotalPsd.setStatus(_A)
class _PdnAdslSeltLnfSignalPsd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_PdnAdslSeltLnfSignalPsd_Type.__name__=_C
_PdnAdslSeltLnfSignalPsd_Object=MibTableColumn
pdnAdslSeltLnfSignalPsd=_PdnAdslSeltLnfSignalPsd_Object((1,3,6,1,4,1,1795,2,24,2,6,31,1,4,1,4),_PdnAdslSeltLnfSignalPsd_Type())
pdnAdslSeltLnfSignalPsd.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnAdslSeltLnfSignalPsd.setStatus(_A)
_PdnAdslSeltAFNs_ObjectIdentity=ObjectIdentity
pdnAdslSeltAFNs=_PdnAdslSeltAFNs_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,31,2))
_PdnAdslSeltConformance_ObjectIdentity=ObjectIdentity
pdnAdslSeltConformance=_PdnAdslSeltConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,31,3))
_PdnAdslSeltCompliances_ObjectIdentity=ObjectIdentity
pdnAdslSeltCompliances=_PdnAdslSeltCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,31,3,1))
_PdnAdslSeltGroups_ObjectIdentity=ObjectIdentity
pdnAdslSeltGroups=_PdnAdslSeltGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,31,3,2))
_PdnAdslSeltObjGroups_ObjectIdentity=ObjectIdentity
pdnAdslSeltObjGroups=_PdnAdslSeltObjGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,31,3,2,1))
_PdnAdslSeltAfnGroups_ObjectIdentity=ObjectIdentity
pdnAdslSeltAfnGroups=_PdnAdslSeltAfnGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,31,3,2,2))
_PdnAdslSeltNtfyGroups_ObjectIdentity=ObjectIdentity
pdnAdslSeltNtfyGroups=_PdnAdslSeltNtfyGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,31,3,2,3))
pdnAdslSeltGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,31,3,2,1,1))
pdnAdslSeltGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:pdnAdslSeltGroup.setStatus(_A)
pdnAdslSeltLcGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,31,3,2,1,2))
pdnAdslSeltLcGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:pdnAdslSeltLcGroup.setStatus(_A)
pdnAdslSeltLnfGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,31,3,2,1,3))
pdnAdslSeltLnfGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:pdnAdslSeltLnfGroup.setStatus(_A)
pdnAdslSeltMIBCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,6,31,3,1,1))
pdnAdslSeltMIBCompliance.setObjects(*((_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:pdnAdslSeltMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PdnSeltTypes':PdnSeltTypes,'pdnAdslSeltMIB':pdnAdslSeltMIB,'pdnAdslSeltNotifications':pdnAdslSeltNotifications,'pdnAdslSeltObjects':pdnAdslSeltObjects,_O:pdnAdslSeltWireSize,'pdnAdslSeltTable':pdnAdslSeltTable,'pdnAdslSeltEntry':pdnAdslSeltEntry,_I:pdnAdslSeltType,_M:pdnAdslSeltCmd,_N:pdnAdslSeltStatus,_P:pdnAdslSeltDuration,_Q:pdnAdslSeltTimeLeft,'pdnAdslSeltLcTable':pdnAdslSeltLcTable,'pdnAdslSeltLcEntry':pdnAdslSeltLcEntry,_K:pdnAdslSeltLcSegmentIndex,_R:pdnAdslSeltLcSegmentLength,_S:pdnAdslSeltLcSegmentGauge,_T:pdnAdslSeltLcSegmentType,'pdnAdslSeltLnfTable':pdnAdslSeltLnfTable,'pdnAdslSeltLnfEntry':pdnAdslSeltLnfEntry,_L:pdnAdslSeltLnfSubCarrierIndex,_U:pdnAdslSeltLnfPeakPsd,_V:pdnAdslSeltLnfTotalPsd,_W:pdnAdslSeltLnfSignalPsd,'pdnAdslSeltAFNs':pdnAdslSeltAFNs,'pdnAdslSeltConformance':pdnAdslSeltConformance,'pdnAdslSeltCompliances':pdnAdslSeltCompliances,'pdnAdslSeltMIBCompliance':pdnAdslSeltMIBCompliance,'pdnAdslSeltGroups':pdnAdslSeltGroups,'pdnAdslSeltObjGroups':pdnAdslSeltObjGroups,_X:pdnAdslSeltGroup,_Y:pdnAdslSeltLcGroup,_Z:pdnAdslSeltLnfGroup,'pdnAdslSeltAfnGroups':pdnAdslSeltAfnGroups,'pdnAdslSeltNtfyGroups':pdnAdslSeltNtfyGroups})