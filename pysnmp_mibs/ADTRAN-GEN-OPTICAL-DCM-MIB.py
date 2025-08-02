_G='adGenOpticalDCMPortInfoIndex'
_F='ADTRAN-GEN-OPTICAL-DCM-MIB'
_E='adGenSlotInfoIndex'
_D='ADTRAN-GENSLOT-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_D,_E)
adGenOpticalDCM,adGenOpticalDCMID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenOpticalDCM','adGenOpticalDCMID')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenOpticalDCMMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,42,1))
if mibBuilder.loadTexts:adGenOpticalDCMMIB.setRevisions(('2012-01-12 00:00','2011-05-23 00:00'))
_AdGenOpticalDCMProduct_ObjectIdentity=ObjectIdentity
adGenOpticalDCMProduct=_AdGenOpticalDCMProduct_ObjectIdentity((1,3,6,1,4,1,664,5,70,42,1))
_AdGenOpticalDCMTable_Object=MibTable
adGenOpticalDCMTable=_AdGenOpticalDCMTable_Object((1,3,6,1,4,1,664,5,70,42,1,1))
if mibBuilder.loadTexts:adGenOpticalDCMTable.setStatus(_A)
_AdGenOpticalDCMEntry_Object=MibTableRow
adGenOpticalDCMEntry=_AdGenOpticalDCMEntry_Object((1,3,6,1,4,1,664,5,70,42,1,1,1))
adGenOpticalDCMEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:adGenOpticalDCMEntry.setStatus(_A)
class _AdGenOpticalDCMType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('dcmFTwentyKM',1),('dcmFFortyKM',2),('dcmFSixtyKM',3),('dcmFEightyKM',4),('dcmBTwentyKM',5),('dcmBFortyKM',6),('dcmBSixtyKM',7),('dcmBEightyKM',8)))
_AdGenOpticalDCMType_Type.__name__=_C
_AdGenOpticalDCMType_Object=MibTableColumn
adGenOpticalDCMType=_AdGenOpticalDCMType_Object((1,3,6,1,4,1,664,5,70,42,1,1,1,1),_AdGenOpticalDCMType_Type())
adGenOpticalDCMType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenOpticalDCMType.setStatus(_A)
class _AdGenOpticalDCMGridSpacing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('allRange',1),('twentyFiveGHz',2),('fiftyGHz',3),('oneHundredGHz',4)))
_AdGenOpticalDCMGridSpacing_Type.__name__=_C
_AdGenOpticalDCMGridSpacing_Object=MibTableColumn
adGenOpticalDCMGridSpacing=_AdGenOpticalDCMGridSpacing_Object((1,3,6,1,4,1,664,5,70,42,1,1,1,2),_AdGenOpticalDCMGridSpacing_Type())
adGenOpticalDCMGridSpacing.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenOpticalDCMGridSpacing.setStatus(_A)
_AdGenOpticalDCMNumOfPorts_Type=Integer32
_AdGenOpticalDCMNumOfPorts_Object=MibTableColumn
adGenOpticalDCMNumOfPorts=_AdGenOpticalDCMNumOfPorts_Object((1,3,6,1,4,1,664,5,70,42,1,1,1,3),_AdGenOpticalDCMNumOfPorts_Type())
adGenOpticalDCMNumOfPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenOpticalDCMNumOfPorts.setStatus(_A)
_AdGenOpticalDCMPortTable_Object=MibTable
adGenOpticalDCMPortTable=_AdGenOpticalDCMPortTable_Object((1,3,6,1,4,1,664,5,70,42,1,2))
if mibBuilder.loadTexts:adGenOpticalDCMPortTable.setStatus(_A)
_AdGenOpticalDCMPortEntry_Object=MibTableRow
adGenOpticalDCMPortEntry=_AdGenOpticalDCMPortEntry_Object((1,3,6,1,4,1,664,5,70,42,1,2,1))
adGenOpticalDCMPortEntry.setIndexNames((0,_D,_E),(0,_F,_G))
if mibBuilder.loadTexts:adGenOpticalDCMPortEntry.setStatus(_A)
_AdGenOpticalDCMPortInfoIndex_Type=Integer32
_AdGenOpticalDCMPortInfoIndex_Object=MibTableColumn
adGenOpticalDCMPortInfoIndex=_AdGenOpticalDCMPortInfoIndex_Object((1,3,6,1,4,1,664,5,70,42,1,2,1,1),_AdGenOpticalDCMPortInfoIndex_Type())
adGenOpticalDCMPortInfoIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:adGenOpticalDCMPortInfoIndex.setStatus(_A)
class _AdGenOpticalDCMPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),('out',2)))
_AdGenOpticalDCMPortType_Type.__name__=_C
_AdGenOpticalDCMPortType_Object=MibTableColumn
adGenOpticalDCMPortType=_AdGenOpticalDCMPortType_Object((1,3,6,1,4,1,664,5,70,42,1,2,1,2),_AdGenOpticalDCMPortType_Type())
adGenOpticalDCMPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenOpticalDCMPortType.setStatus(_A)
class _AdGenOpticalDCMPortDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),('out',2)))
_AdGenOpticalDCMPortDirection_Type.__name__=_C
_AdGenOpticalDCMPortDirection_Object=MibTableColumn
adGenOpticalDCMPortDirection=_AdGenOpticalDCMPortDirection_Object((1,3,6,1,4,1,664,5,70,42,1,2,1,3),_AdGenOpticalDCMPortDirection_Type())
adGenOpticalDCMPortDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenOpticalDCMPortDirection.setStatus(_A)
_AdGenOpticalDCMPortMinWaveLengthPicoMeter_Type=Integer32
_AdGenOpticalDCMPortMinWaveLengthPicoMeter_Object=MibTableColumn
adGenOpticalDCMPortMinWaveLengthPicoMeter=_AdGenOpticalDCMPortMinWaveLengthPicoMeter_Object((1,3,6,1,4,1,664,5,70,42,1,2,1,4),_AdGenOpticalDCMPortMinWaveLengthPicoMeter_Type())
adGenOpticalDCMPortMinWaveLengthPicoMeter.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenOpticalDCMPortMinWaveLengthPicoMeter.setStatus(_A)
_AdGenOpticalDCMPortMaxWaveLengthPicoMeter_Type=Integer32
_AdGenOpticalDCMPortMaxWaveLengthPicoMeter_Object=MibTableColumn
adGenOpticalDCMPortMaxWaveLengthPicoMeter=_AdGenOpticalDCMPortMaxWaveLengthPicoMeter_Object((1,3,6,1,4,1,664,5,70,42,1,2,1,5),_AdGenOpticalDCMPortMaxWaveLengthPicoMeter_Type())
adGenOpticalDCMPortMaxWaveLengthPicoMeter.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenOpticalDCMPortMaxWaveLengthPicoMeter.setStatus(_A)
_AdGenOpticalDCMPortInsertionLossDB_Type=Integer32
_AdGenOpticalDCMPortInsertionLossDB_Object=MibTableColumn
adGenOpticalDCMPortInsertionLossDB=_AdGenOpticalDCMPortInsertionLossDB_Object((1,3,6,1,4,1,664,5,70,42,1,2,1,6),_AdGenOpticalDCMPortInsertionLossDB_Type())
adGenOpticalDCMPortInsertionLossDB.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenOpticalDCMPortInsertionLossDB.setStatus(_A)
_AdGenOpticalDCMPortIfIndexReference_Type=InterfaceIndex
_AdGenOpticalDCMPortIfIndexReference_Object=MibTableColumn
adGenOpticalDCMPortIfIndexReference=_AdGenOpticalDCMPortIfIndexReference_Object((1,3,6,1,4,1,664,5,70,42,1,2,1,7),_AdGenOpticalDCMPortIfIndexReference_Type())
adGenOpticalDCMPortIfIndexReference.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenOpticalDCMPortIfIndexReference.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'adGenOpticalDCMProduct':adGenOpticalDCMProduct,'adGenOpticalDCMTable':adGenOpticalDCMTable,'adGenOpticalDCMEntry':adGenOpticalDCMEntry,'adGenOpticalDCMType':adGenOpticalDCMType,'adGenOpticalDCMGridSpacing':adGenOpticalDCMGridSpacing,'adGenOpticalDCMNumOfPorts':adGenOpticalDCMNumOfPorts,'adGenOpticalDCMPortTable':adGenOpticalDCMPortTable,'adGenOpticalDCMPortEntry':adGenOpticalDCMPortEntry,_G:adGenOpticalDCMPortInfoIndex,'adGenOpticalDCMPortType':adGenOpticalDCMPortType,'adGenOpticalDCMPortDirection':adGenOpticalDCMPortDirection,'adGenOpticalDCMPortMinWaveLengthPicoMeter':adGenOpticalDCMPortMinWaveLengthPicoMeter,'adGenOpticalDCMPortMaxWaveLengthPicoMeter':adGenOpticalDCMPortMaxWaveLengthPicoMeter,'adGenOpticalDCMPortInsertionLossDB':adGenOpticalDCMPortInsertionLossDB,'adGenOpticalDCMPortIfIndexReference':adGenOpticalDCMPortIfIndexReference,'adGenOpticalDCMMIB':adGenOpticalDCMMIB})