_T='ceshCollectionIntervalGroup'
_S='ceshCollectionGroup'
_R='ceshCollectionIntervalSensorValue'
_Q='ceshCollectionIntervalTimeStamp'
_P='ceshCollectionMaxIntervals'
_O='ceshCollectionAlgorithm'
_N='ceshCollectionInvalidIntervals'
_M='ceshCollectionIntervals'
_L='ceshCollectionElapsedTime'
_K='ceshCollectionIntervalNumber'
_J='seconds'
_I='not-accessible'
_H='intervals'
_G='ceshCollectionIntervalTime'
_F='entPhysicalIndex'
_E='ENTITY-MIB'
_D='Unsigned32'
_C='read-only'
_B='CISCO-ENTITY-SENSOR-HISTORY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalIndex,=mibBuilder.importSymbols(_E,_F)
EntitySensorValue,=mibBuilder.importSymbols('ENTITY-SENSOR-MIB','EntitySensorValue')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
ciscoEntitySensorHistoryMIB=ModuleIdentity((1,3,6,1,4,1,9,9,768))
if mibBuilder.loadTexts:ciscoEntitySensorHistoryMIB.setRevisions(('2011-03-04 00:00',))
class SensorHistoryCollectionAlgorithm(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('unknown',2),('measured',3),('algoSMA',4)))
_CiscoEntitySensorHistoryMIBObjects_ObjectIdentity=ObjectIdentity
ciscoEntitySensorHistoryMIBObjects=_CiscoEntitySensorHistoryMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,768,0))
_CeshCollectionTable_Object=MibTable
ceshCollectionTable=_CeshCollectionTable_Object((1,3,6,1,4,1,9,9,768,0,1))
if mibBuilder.loadTexts:ceshCollectionTable.setStatus(_A)
_CeshCollectionEntry_Object=MibTableRow
ceshCollectionEntry=_CeshCollectionEntry_Object((1,3,6,1,4,1,9,9,768,0,1,1))
ceshCollectionEntry.setIndexNames((0,_E,_F),(0,_B,_G))
if mibBuilder.loadTexts:ceshCollectionEntry.setStatus(_A)
class _CeshCollectionIntervalTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CeshCollectionIntervalTime_Type.__name__=_D
_CeshCollectionIntervalTime_Object=MibTableColumn
ceshCollectionIntervalTime=_CeshCollectionIntervalTime_Object((1,3,6,1,4,1,9,9,768,0,1,1,1),_CeshCollectionIntervalTime_Type())
ceshCollectionIntervalTime.setMaxAccess(_I)
if mibBuilder.loadTexts:ceshCollectionIntervalTime.setStatus(_A)
if mibBuilder.loadTexts:ceshCollectionIntervalTime.setUnits(_J)
_CeshCollectionIntervals_Type=Gauge32
_CeshCollectionIntervals_Object=MibTableColumn
ceshCollectionIntervals=_CeshCollectionIntervals_Object((1,3,6,1,4,1,9,9,768,0,1,1,2),_CeshCollectionIntervals_Type())
ceshCollectionIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:ceshCollectionIntervals.setStatus(_A)
if mibBuilder.loadTexts:ceshCollectionIntervals.setUnits(_H)
_CeshCollectionInvalidIntervals_Type=Gauge32
_CeshCollectionInvalidIntervals_Object=MibTableColumn
ceshCollectionInvalidIntervals=_CeshCollectionInvalidIntervals_Object((1,3,6,1,4,1,9,9,768,0,1,1,3),_CeshCollectionInvalidIntervals_Type())
ceshCollectionInvalidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:ceshCollectionInvalidIntervals.setStatus(_A)
if mibBuilder.loadTexts:ceshCollectionInvalidIntervals.setUnits(_H)
class _CeshCollectionMaxIntervals_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CeshCollectionMaxIntervals_Type.__name__=_D
_CeshCollectionMaxIntervals_Object=MibTableColumn
ceshCollectionMaxIntervals=_CeshCollectionMaxIntervals_Object((1,3,6,1,4,1,9,9,768,0,1,1,4),_CeshCollectionMaxIntervals_Type())
ceshCollectionMaxIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:ceshCollectionMaxIntervals.setStatus(_A)
if mibBuilder.loadTexts:ceshCollectionMaxIntervals.setUnits(_H)
_CeshCollectionElapsedTime_Type=Gauge32
_CeshCollectionElapsedTime_Object=MibTableColumn
ceshCollectionElapsedTime=_CeshCollectionElapsedTime_Object((1,3,6,1,4,1,9,9,768,0,1,1,5),_CeshCollectionElapsedTime_Type())
ceshCollectionElapsedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ceshCollectionElapsedTime.setStatus(_A)
if mibBuilder.loadTexts:ceshCollectionElapsedTime.setUnits(_J)
_CeshCollectionAlgorithm_Type=SensorHistoryCollectionAlgorithm
_CeshCollectionAlgorithm_Object=MibTableColumn
ceshCollectionAlgorithm=_CeshCollectionAlgorithm_Object((1,3,6,1,4,1,9,9,768,0,1,1,6),_CeshCollectionAlgorithm_Type())
ceshCollectionAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:ceshCollectionAlgorithm.setStatus(_A)
_CeshCollectionIntervalTable_Object=MibTable
ceshCollectionIntervalTable=_CeshCollectionIntervalTable_Object((1,3,6,1,4,1,9,9,768,0,2))
if mibBuilder.loadTexts:ceshCollectionIntervalTable.setStatus(_A)
_CeshCollectionIntervalEntry_Object=MibTableRow
ceshCollectionIntervalEntry=_CeshCollectionIntervalEntry_Object((1,3,6,1,4,1,9,9,768,0,2,1))
ceshCollectionIntervalEntry.setIndexNames((0,_E,_F),(0,_B,_G),(0,_B,_K))
if mibBuilder.loadTexts:ceshCollectionIntervalEntry.setStatus(_A)
class _CeshCollectionIntervalNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CeshCollectionIntervalNumber_Type.__name__=_D
_CeshCollectionIntervalNumber_Object=MibTableColumn
ceshCollectionIntervalNumber=_CeshCollectionIntervalNumber_Object((1,3,6,1,4,1,9,9,768,0,2,1,1),_CeshCollectionIntervalNumber_Type())
ceshCollectionIntervalNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:ceshCollectionIntervalNumber.setStatus(_A)
_CeshCollectionIntervalSensorValue_Type=EntitySensorValue
_CeshCollectionIntervalSensorValue_Object=MibTableColumn
ceshCollectionIntervalSensorValue=_CeshCollectionIntervalSensorValue_Object((1,3,6,1,4,1,9,9,768,0,2,1,2),_CeshCollectionIntervalSensorValue_Type())
ceshCollectionIntervalSensorValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ceshCollectionIntervalSensorValue.setStatus(_A)
_CeshCollectionIntervalTimeStamp_Type=TimeStamp
_CeshCollectionIntervalTimeStamp_Object=MibTableColumn
ceshCollectionIntervalTimeStamp=_CeshCollectionIntervalTimeStamp_Object((1,3,6,1,4,1,9,9,768,0,2,1,3),_CeshCollectionIntervalTimeStamp_Type())
ceshCollectionIntervalTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:ceshCollectionIntervalTimeStamp.setStatus(_A)
_CiscoEntitySensorHistoryMIBConform_ObjectIdentity=ObjectIdentity
ciscoEntitySensorHistoryMIBConform=_CiscoEntitySensorHistoryMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,768,1))
_CiscoEntitySensorHistoryMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoEntitySensorHistoryMIBCompliances=_CiscoEntitySensorHistoryMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,768,1,1))
_CiscoEntitySensorHistoryMIBGroups_ObjectIdentity=ObjectIdentity
ciscoEntitySensorHistoryMIBGroups=_CiscoEntitySensorHistoryMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,768,1,2))
ceshCollectionGroup=ObjectGroup((1,3,6,1,4,1,9,9,768,1,2,1))
ceshCollectionGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:ceshCollectionGroup.setStatus(_A)
ceshCollectionIntervalGroup=ObjectGroup((1,3,6,1,4,1,9,9,768,1,2,2))
ceshCollectionIntervalGroup.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ceshCollectionIntervalGroup.setStatus(_A)
ciscoEntitySensorHistoryCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,768,1,1,1))
ciscoEntitySensorHistoryCompliance.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ciscoEntitySensorHistoryCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SensorHistoryCollectionAlgorithm':SensorHistoryCollectionAlgorithm,'ciscoEntitySensorHistoryMIB':ciscoEntitySensorHistoryMIB,'ciscoEntitySensorHistoryMIBObjects':ciscoEntitySensorHistoryMIBObjects,'ceshCollectionTable':ceshCollectionTable,'ceshCollectionEntry':ceshCollectionEntry,_G:ceshCollectionIntervalTime,_M:ceshCollectionIntervals,_N:ceshCollectionInvalidIntervals,_P:ceshCollectionMaxIntervals,_L:ceshCollectionElapsedTime,_O:ceshCollectionAlgorithm,'ceshCollectionIntervalTable':ceshCollectionIntervalTable,'ceshCollectionIntervalEntry':ceshCollectionIntervalEntry,_K:ceshCollectionIntervalNumber,_R:ceshCollectionIntervalSensorValue,_Q:ceshCollectionIntervalTimeStamp,'ciscoEntitySensorHistoryMIBConform':ciscoEntitySensorHistoryMIBConform,'ciscoEntitySensorHistoryMIBCompliances':ciscoEntitySensorHistoryMIBCompliances,'ciscoEntitySensorHistoryCompliance':ciscoEntitySensorHistoryCompliance,'ciscoEntitySensorHistoryMIBGroups':ciscoEntitySensorHistoryMIBGroups,_S:ceshCollectionGroup,_T:ceshCollectionIntervalGroup})