_P='dpPoeIfInfoGroup'
_O='dpPoeIfCfgGroup'
_N='dpPoeIfPower'
_M='dpPoeIfFaultyType'
_L='dpPoeIfDetectStatus'
_K='dpPoeIfTimeRange'
_J='dpPoeIfMaxPower'
_I='dpPoeIfState'
_H='DisplayString'
_G='read-only'
_F='read-write'
_E='pethPsePortIndex'
_D='POWER-ETHERNET-MIB'
_C='Integer32'
_B='DLINKPRIME-POE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
pethPsePortIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention','TruthValue')
dlinkPrimePoeExtMIB=ModuleIdentity((1,3,6,1,4,1,171,15,11))
if mibBuilder.loadTexts:dlinkPrimePoeExtMIB.setRevisions(('2014-04-26 00:00',))
_DpPoeMIBNotifications_ObjectIdentity=ObjectIdentity
dpPoeMIBNotifications=_DpPoeMIBNotifications_ObjectIdentity((1,3,6,1,4,1,171,15,11,0))
_DpPoeMIBObjects_ObjectIdentity=ObjectIdentity
dpPoeMIBObjects=_DpPoeMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,15,11,1))
_DpPoeIfObjects_ObjectIdentity=ObjectIdentity
dpPoeIfObjects=_DpPoeIfObjects_ObjectIdentity((1,3,6,1,4,1,171,15,11,1,1))
_DpPoeIfCfgTable_Object=MibTable
dpPoeIfCfgTable=_DpPoeIfCfgTable_Object((1,3,6,1,4,1,171,15,11,1,1,1))
if mibBuilder.loadTexts:dpPoeIfCfgTable.setStatus(_A)
_DpPoeIfCfgEntry_Object=MibTableRow
dpPoeIfCfgEntry=_DpPoeIfCfgEntry_Object((1,3,6,1,4,1,171,15,11,1,1,1,1))
dpPoeIfCfgEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:dpPoeIfCfgEntry.setStatus(_A)
class _DpPoeIfState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('auto',1),('never',2),('static',3),('class1',4),('class2',5),('class3',6),('class4',7)))
_DpPoeIfState_Type.__name__=_C
_DpPoeIfState_Object=MibTableColumn
dpPoeIfState=_DpPoeIfState_Object((1,3,6,1,4,1,171,15,11,1,1,1,1,1),_DpPoeIfState_Type())
dpPoeIfState.setMaxAccess(_F)
if mibBuilder.loadTexts:dpPoeIfState.setStatus(_A)
class _DpPoeIfMaxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1000,30000))
_DpPoeIfMaxPower_Type.__name__=_C
_DpPoeIfMaxPower_Object=MibTableColumn
dpPoeIfMaxPower=_DpPoeIfMaxPower_Object((1,3,6,1,4,1,171,15,11,1,1,1,1,2),_DpPoeIfMaxPower_Type())
dpPoeIfMaxPower.setMaxAccess(_F)
if mibBuilder.loadTexts:dpPoeIfMaxPower.setStatus(_A)
if mibBuilder.loadTexts:dpPoeIfMaxPower.setUnits('milliwatts')
class _DpPoeIfTimeRange_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_DpPoeIfTimeRange_Type.__name__=_H
_DpPoeIfTimeRange_Object=MibTableColumn
dpPoeIfTimeRange=_DpPoeIfTimeRange_Object((1,3,6,1,4,1,171,15,11,1,1,1,1,3),_DpPoeIfTimeRange_Type())
dpPoeIfTimeRange.setMaxAccess(_F)
if mibBuilder.loadTexts:dpPoeIfTimeRange.setStatus(_A)
_DpPoeIfInfoObjects_ObjectIdentity=ObjectIdentity
dpPoeIfInfoObjects=_DpPoeIfInfoObjects_ObjectIdentity((1,3,6,1,4,1,171,15,11,1,1,2))
_DpPoeIfStatusTable_Object=MibTable
dpPoeIfStatusTable=_DpPoeIfStatusTable_Object((1,3,6,1,4,1,171,15,11,1,1,2,1))
if mibBuilder.loadTexts:dpPoeIfStatusTable.setStatus(_A)
_DpPoeIfStatusEntry_Object=MibTableRow
dpPoeIfStatusEntry=_DpPoeIfStatusEntry_Object((1,3,6,1,4,1,171,15,11,1,1,2,1,1))
dpPoeIfStatusEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:dpPoeIfStatusEntry.setStatus(_A)
class _DpPoeIfDetectStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('disabled',1),('searching',2),('requesting',3),('delivering',4),('faulty',5)))
_DpPoeIfDetectStatus_Type.__name__=_C
_DpPoeIfDetectStatus_Object=MibTableColumn
dpPoeIfDetectStatus=_DpPoeIfDetectStatus_Object((1,3,6,1,4,1,171,15,11,1,1,2,1,1,1),_DpPoeIfDetectStatus_Type())
dpPoeIfDetectStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:dpPoeIfDetectStatus.setStatus(_A)
class _DpPoeIfFaultyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('notApplicable',0),('mpsAbsent',1),('pdShort',2),('overload',3),('powerDenied',4),('thermalShutdown',5),('startupFailure',6),('classificationFailure',7)))
_DpPoeIfFaultyType_Type.__name__=_C
_DpPoeIfFaultyType_Object=MibTableColumn
dpPoeIfFaultyType=_DpPoeIfFaultyType_Object((1,3,6,1,4,1,171,15,11,1,1,2,1,1,2),_DpPoeIfFaultyType_Type())
dpPoeIfFaultyType.setMaxAccess(_G)
if mibBuilder.loadTexts:dpPoeIfFaultyType.setStatus(_A)
_DpPoeIfMeasurementTable_Object=MibTable
dpPoeIfMeasurementTable=_DpPoeIfMeasurementTable_Object((1,3,6,1,4,1,171,15,11,1,1,2,2))
if mibBuilder.loadTexts:dpPoeIfMeasurementTable.setStatus(_A)
_DpPoeIfMeasurementEntry_Object=MibTableRow
dpPoeIfMeasurementEntry=_DpPoeIfMeasurementEntry_Object((1,3,6,1,4,1,171,15,11,1,1,2,2,1))
dpPoeIfMeasurementEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:dpPoeIfMeasurementEntry.setStatus(_A)
_DpPoeIfPower_Type=Integer32
_DpPoeIfPower_Object=MibTableColumn
dpPoeIfPower=_DpPoeIfPower_Object((1,3,6,1,4,1,171,15,11,1,1,2,2,1,1),_DpPoeIfPower_Type())
dpPoeIfPower.setMaxAccess(_G)
if mibBuilder.loadTexts:dpPoeIfPower.setStatus(_A)
_DpPoeMIBConformance_ObjectIdentity=ObjectIdentity
dpPoeMIBConformance=_DpPoeMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,15,11,2))
_DpPoeMIBCompliances_ObjectIdentity=ObjectIdentity
dpPoeMIBCompliances=_DpPoeMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,11,2,1))
_DpPoeMIBGroups_ObjectIdentity=ObjectIdentity
dpPoeMIBGroups=_DpPoeMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,15,11,2,2))
dpPoeIfCfgGroup=ObjectGroup((1,3,6,1,4,1,171,15,11,2,2,1))
dpPoeIfCfgGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:dpPoeIfCfgGroup.setStatus(_A)
dpPoeIfInfoGroup=ObjectGroup((1,3,6,1,4,1,171,15,11,2,2,2))
dpPoeIfInfoGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:dpPoeIfInfoGroup.setStatus(_A)
dpPoeMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,15,11,2,1,1))
dpPoeMIBCompliance.setObjects(*((_B,'dpPoeGroupCfgGroup'),(_B,_O),(_B,'dpPoeGroupInfoGroup'),(_B,_P),(_B,'dpPoeIfErrorStateNotificationGroup')))
if mibBuilder.loadTexts:dpPoeMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dlinkPrimePoeExtMIB':dlinkPrimePoeExtMIB,'dpPoeMIBNotifications':dpPoeMIBNotifications,'dpPoeMIBObjects':dpPoeMIBObjects,'dpPoeIfObjects':dpPoeIfObjects,'dpPoeIfCfgTable':dpPoeIfCfgTable,'dpPoeIfCfgEntry':dpPoeIfCfgEntry,_I:dpPoeIfState,_J:dpPoeIfMaxPower,_K:dpPoeIfTimeRange,'dpPoeIfInfoObjects':dpPoeIfInfoObjects,'dpPoeIfStatusTable':dpPoeIfStatusTable,'dpPoeIfStatusEntry':dpPoeIfStatusEntry,_L:dpPoeIfDetectStatus,_M:dpPoeIfFaultyType,'dpPoeIfMeasurementTable':dpPoeIfMeasurementTable,'dpPoeIfMeasurementEntry':dpPoeIfMeasurementEntry,_N:dpPoeIfPower,'dpPoeMIBConformance':dpPoeMIBConformance,'dpPoeMIBCompliances':dpPoeMIBCompliances,'dpPoeMIBCompliance':dpPoeMIBCompliance,'dpPoeMIBGroups':dpPoeMIBGroups,_O:dpPoeIfCfgGroup,_P:dpPoeIfInfoGroup})