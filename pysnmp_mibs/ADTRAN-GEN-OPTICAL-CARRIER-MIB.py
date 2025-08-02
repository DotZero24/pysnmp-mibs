_J='adGenOpticalCarrierProdPortInfoIndex'
_I='ADTRAN-GEN-OPTICAL-CARRIER-MIB'
_H='adGenSubSlotProdInfoIndex'
_G='ADTRAN-GENSLOT-SUB-MODULE-MIB'
_F='adGenSlotInfoIndex'
_E='ADTRAN-GENSLOT-MIB'
_D='invalid'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_E,_F)
adGenSubSlotProdInfoIndex,=mibBuilder.importSymbols(_G,_H)
adGenOpticalCarrier,adGenOpticalCarrierID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenOpticalCarrier','adGenOpticalCarrierID')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenOpticalCarrierMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,40,1))
if mibBuilder.loadTexts:adGenOpticalCarrierMIB.setRevisions(('2012-01-12 00:00','2011-05-23 00:00'))
_AdGenOpticalCarrierProduct_ObjectIdentity=ObjectIdentity
adGenOpticalCarrierProduct=_AdGenOpticalCarrierProduct_ObjectIdentity((1,3,6,1,4,1,664,5,70,40,1))
_AdGenOpticalCarrierProductTable_Object=MibTable
adGenOpticalCarrierProductTable=_AdGenOpticalCarrierProductTable_Object((1,3,6,1,4,1,664,5,70,40,1,1))
if mibBuilder.loadTexts:adGenOpticalCarrierProductTable.setStatus(_A)
_AdGenOpticalCarrierProductEntry_Object=MibTableRow
adGenOpticalCarrierProductEntry=_AdGenOpticalCarrierProductEntry_Object((1,3,6,1,4,1,664,5,70,40,1,1,1))
adGenOpticalCarrierProductEntry.setIndexNames((0,_E,_F),(0,_G,_H))
if mibBuilder.loadTexts:adGenOpticalCarrierProductEntry.setStatus(_A)
class _AdGenOpticalCarrierProdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_D,1),('cwdmMUX',2),('dwdmMUX',3),('cwdmDEMUX',4),('dwdmDEMUX',5),('cwdmOADM',6),('dwdmOADM',7),('oscFILTER',8)))
_AdGenOpticalCarrierProdType_Type.__name__=_C
_AdGenOpticalCarrierProdType_Object=MibTableColumn
adGenOpticalCarrierProdType=_AdGenOpticalCarrierProdType_Object((1,3,6,1,4,1,664,5,70,40,1,1,1,1),_AdGenOpticalCarrierProdType_Type())
adGenOpticalCarrierProdType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenOpticalCarrierProdType.setStatus(_A)
class _AdGenOpticalCarrierProdGridSpacing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),('allRange',2),('twentyFiveGHz',3),('fiftyGHz',4),('oneHundredGHz',5)))
_AdGenOpticalCarrierProdGridSpacing_Type.__name__=_C
_AdGenOpticalCarrierProdGridSpacing_Object=MibTableColumn
adGenOpticalCarrierProdGridSpacing=_AdGenOpticalCarrierProdGridSpacing_Object((1,3,6,1,4,1,664,5,70,40,1,1,1,2),_AdGenOpticalCarrierProdGridSpacing_Type())
adGenOpticalCarrierProdGridSpacing.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenOpticalCarrierProdGridSpacing.setStatus(_A)
_AdGenOpticalCarrierProdNumOfPorts_Type=Integer32
_AdGenOpticalCarrierProdNumOfPorts_Object=MibTableColumn
adGenOpticalCarrierProdNumOfPorts=_AdGenOpticalCarrierProdNumOfPorts_Object((1,3,6,1,4,1,664,5,70,40,1,1,1,3),_AdGenOpticalCarrierProdNumOfPorts_Type())
adGenOpticalCarrierProdNumOfPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenOpticalCarrierProdNumOfPorts.setStatus(_A)
_AdGenOpticalCarrierProductPortTable_Object=MibTable
adGenOpticalCarrierProductPortTable=_AdGenOpticalCarrierProductPortTable_Object((1,3,6,1,4,1,664,5,70,40,1,2))
if mibBuilder.loadTexts:adGenOpticalCarrierProductPortTable.setStatus(_A)
_AdGenOpticalCarrierProductPortEntry_Object=MibTableRow
adGenOpticalCarrierProductPortEntry=_AdGenOpticalCarrierProductPortEntry_Object((1,3,6,1,4,1,664,5,70,40,1,2,1))
adGenOpticalCarrierProductPortEntry.setIndexNames((0,_E,_F),(0,_G,_H),(0,_I,_J))
if mibBuilder.loadTexts:adGenOpticalCarrierProductPortEntry.setStatus(_A)
_AdGenOpticalCarrierProdPortInfoIndex_Type=Integer32
_AdGenOpticalCarrierProdPortInfoIndex_Object=MibTableColumn
adGenOpticalCarrierProdPortInfoIndex=_AdGenOpticalCarrierProdPortInfoIndex_Object((1,3,6,1,4,1,664,5,70,40,1,2,1,1),_AdGenOpticalCarrierProdPortInfoIndex_Type())
adGenOpticalCarrierProdPortInfoIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:adGenOpticalCarrierProdPortInfoIndex.setStatus(_A)
class _AdGenOpticalCarrierProdPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_D,1),('add',2),('drop',3),('commonMUX',4),('commonDEMUX',5),('expressMUX',6),('expressDEMUX',7),('commonRX',8),('commonTX',9),('osc',10)))
_AdGenOpticalCarrierProdPortType_Type.__name__=_C
_AdGenOpticalCarrierProdPortType_Object=MibTableColumn
adGenOpticalCarrierProdPortType=_AdGenOpticalCarrierProdPortType_Object((1,3,6,1,4,1,664,5,70,40,1,2,1,2),_AdGenOpticalCarrierProdPortType_Type())
adGenOpticalCarrierProdPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenOpticalCarrierProdPortType.setStatus(_A)
class _AdGenOpticalCarrierProdPortDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('in',2),('out',3),('biDirection',4)))
_AdGenOpticalCarrierProdPortDirection_Type.__name__=_C
_AdGenOpticalCarrierProdPortDirection_Object=MibTableColumn
adGenOpticalCarrierProdPortDirection=_AdGenOpticalCarrierProdPortDirection_Object((1,3,6,1,4,1,664,5,70,40,1,2,1,3),_AdGenOpticalCarrierProdPortDirection_Type())
adGenOpticalCarrierProdPortDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenOpticalCarrierProdPortDirection.setStatus(_A)
_AdGenOpticalCarrierProdPortMinWaveLengthPicoMeter_Type=Integer32
_AdGenOpticalCarrierProdPortMinWaveLengthPicoMeter_Object=MibTableColumn
adGenOpticalCarrierProdPortMinWaveLengthPicoMeter=_AdGenOpticalCarrierProdPortMinWaveLengthPicoMeter_Object((1,3,6,1,4,1,664,5,70,40,1,2,1,4),_AdGenOpticalCarrierProdPortMinWaveLengthPicoMeter_Type())
adGenOpticalCarrierProdPortMinWaveLengthPicoMeter.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenOpticalCarrierProdPortMinWaveLengthPicoMeter.setStatus(_A)
_AdGenOpticalCarrierProdPortMaxWaveLengthPicoMeter_Type=Integer32
_AdGenOpticalCarrierProdPortMaxWaveLengthPicoMeter_Object=MibTableColumn
adGenOpticalCarrierProdPortMaxWaveLengthPicoMeter=_AdGenOpticalCarrierProdPortMaxWaveLengthPicoMeter_Object((1,3,6,1,4,1,664,5,70,40,1,2,1,5),_AdGenOpticalCarrierProdPortMaxWaveLengthPicoMeter_Type())
adGenOpticalCarrierProdPortMaxWaveLengthPicoMeter.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenOpticalCarrierProdPortMaxWaveLengthPicoMeter.setStatus(_A)
_AdGenOpticalCarrierProdPortInsertionLossDB_Type=Integer32
_AdGenOpticalCarrierProdPortInsertionLossDB_Object=MibTableColumn
adGenOpticalCarrierProdPortInsertionLossDB=_AdGenOpticalCarrierProdPortInsertionLossDB_Object((1,3,6,1,4,1,664,5,70,40,1,2,1,6),_AdGenOpticalCarrierProdPortInsertionLossDB_Type())
adGenOpticalCarrierProdPortInsertionLossDB.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenOpticalCarrierProdPortInsertionLossDB.setStatus(_A)
_AdGenOpticalCarrierProdPortIfIndexReference_Type=InterfaceIndex
_AdGenOpticalCarrierProdPortIfIndexReference_Object=MibTableColumn
adGenOpticalCarrierProdPortIfIndexReference=_AdGenOpticalCarrierProdPortIfIndexReference_Object((1,3,6,1,4,1,664,5,70,40,1,2,1,7),_AdGenOpticalCarrierProdPortIfIndexReference_Type())
adGenOpticalCarrierProdPortIfIndexReference.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenOpticalCarrierProdPortIfIndexReference.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'adGenOpticalCarrierProduct':adGenOpticalCarrierProduct,'adGenOpticalCarrierProductTable':adGenOpticalCarrierProductTable,'adGenOpticalCarrierProductEntry':adGenOpticalCarrierProductEntry,'adGenOpticalCarrierProdType':adGenOpticalCarrierProdType,'adGenOpticalCarrierProdGridSpacing':adGenOpticalCarrierProdGridSpacing,'adGenOpticalCarrierProdNumOfPorts':adGenOpticalCarrierProdNumOfPorts,'adGenOpticalCarrierProductPortTable':adGenOpticalCarrierProductPortTable,'adGenOpticalCarrierProductPortEntry':adGenOpticalCarrierProductPortEntry,_J:adGenOpticalCarrierProdPortInfoIndex,'adGenOpticalCarrierProdPortType':adGenOpticalCarrierProdPortType,'adGenOpticalCarrierProdPortDirection':adGenOpticalCarrierProdPortDirection,'adGenOpticalCarrierProdPortMinWaveLengthPicoMeter':adGenOpticalCarrierProdPortMinWaveLengthPicoMeter,'adGenOpticalCarrierProdPortMaxWaveLengthPicoMeter':adGenOpticalCarrierProdPortMaxWaveLengthPicoMeter,'adGenOpticalCarrierProdPortInsertionLossDB':adGenOpticalCarrierProdPortInsertionLossDB,'adGenOpticalCarrierProdPortIfIndexReference':adGenOpticalCarrierProdPortIfIndexReference,'adGenOpticalCarrierMIB':adGenOpticalCarrierMIB})