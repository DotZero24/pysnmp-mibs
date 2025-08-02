_F='adGenSubSlotProdInfoIndex'
_E='ADTRAN-GENSLOT-SUB-MODULE-MIB'
_D='adGenSlotInfoIndex'
_C='ADTRAN-GENSLOT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlot,adGenSlotInfoIndex=mibBuilder.importSymbols(_C,'adGenSlot',_D)
AdProductIdentifier,=mibBuilder.importSymbols('ADTRAN-TC','AdProductIdentifier')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols('SNMPv2-MIB','sysName')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenSubSlotModule=ModuleIdentity((1,3,6,1,4,1,664,5,13,2,7))
_AdGenSubSlotProdTable_Object=MibTable
adGenSubSlotProdTable=_AdGenSubSlotProdTable_Object((1,3,6,1,4,1,664,5,13,2,8))
if mibBuilder.loadTexts:adGenSubSlotProdTable.setStatus(_A)
_AdGenSubSlotProdEntry_Object=MibTableRow
adGenSubSlotProdEntry=_AdGenSubSlotProdEntry_Object((1,3,6,1,4,1,664,5,13,2,8,1))
adGenSubSlotProdEntry.setIndexNames((0,_C,_D),(0,_E,_F))
if mibBuilder.loadTexts:adGenSubSlotProdEntry.setStatus(_A)
_AdGenSubSlotProdInfoIndex_Type=Integer32
_AdGenSubSlotProdInfoIndex_Object=MibTableColumn
adGenSubSlotProdInfoIndex=_AdGenSubSlotProdInfoIndex_Object((1,3,6,1,4,1,664,5,13,2,8,1,1),_AdGenSubSlotProdInfoIndex_Type())
adGenSubSlotProdInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubSlotProdInfoIndex.setStatus(_A)
_AdGenSubSlotProdName_Type=DisplayString
_AdGenSubSlotProdName_Object=MibTableColumn
adGenSubSlotProdName=_AdGenSubSlotProdName_Object((1,3,6,1,4,1,664,5,13,2,8,1,2),_AdGenSubSlotProdName_Type())
adGenSubSlotProdName.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubSlotProdName.setStatus(_A)
_AdGenSubSlotProdPartNumber_Type=DisplayString
_AdGenSubSlotProdPartNumber_Object=MibTableColumn
adGenSubSlotProdPartNumber=_AdGenSubSlotProdPartNumber_Object((1,3,6,1,4,1,664,5,13,2,8,1,3),_AdGenSubSlotProdPartNumber_Type())
adGenSubSlotProdPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubSlotProdPartNumber.setStatus(_A)
_AdGenSubSlotProdCLEIcode_Type=DisplayString
_AdGenSubSlotProdCLEIcode_Object=MibTableColumn
adGenSubSlotProdCLEIcode=_AdGenSubSlotProdCLEIcode_Object((1,3,6,1,4,1,664,5,13,2,8,1,4),_AdGenSubSlotProdCLEIcode_Type())
adGenSubSlotProdCLEIcode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubSlotProdCLEIcode.setStatus(_A)
_AdGenSubSlotProdSerialNumber_Type=DisplayString
_AdGenSubSlotProdSerialNumber_Object=MibTableColumn
adGenSubSlotProdSerialNumber=_AdGenSubSlotProdSerialNumber_Object((1,3,6,1,4,1,664,5,13,2,8,1,5),_AdGenSubSlotProdSerialNumber_Type())
adGenSubSlotProdSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubSlotProdSerialNumber.setStatus(_A)
_AdGenSubSlotProdRevision_Type=DisplayString
_AdGenSubSlotProdRevision_Object=MibTableColumn
adGenSubSlotProdRevision=_AdGenSubSlotProdRevision_Object((1,3,6,1,4,1,664,5,13,2,8,1,6),_AdGenSubSlotProdRevision_Type())
adGenSubSlotProdRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubSlotProdRevision.setStatus(_A)
_AdGenSubSlotProdSwVersion_Type=DisplayString
_AdGenSubSlotProdSwVersion_Object=MibTableColumn
adGenSubSlotProdSwVersion=_AdGenSubSlotProdSwVersion_Object((1,3,6,1,4,1,664,5,13,2,8,1,7),_AdGenSubSlotProdSwVersion_Type())
adGenSubSlotProdSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubSlotProdSwVersion.setStatus(_A)
_AdGenSubSlotProdDateOfManufacturing_Type=DisplayString
_AdGenSubSlotProdDateOfManufacturing_Object=MibTableColumn
adGenSubSlotProdDateOfManufacturing=_AdGenSubSlotProdDateOfManufacturing_Object((1,3,6,1,4,1,664,5,13,2,8,1,8),_AdGenSubSlotProdDateOfManufacturing_Type())
adGenSubSlotProdDateOfManufacturing.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSubSlotProdDateOfManufacturing.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'adGenSubSlotModule':adGenSubSlotModule,'adGenSubSlotProdTable':adGenSubSlotProdTable,'adGenSubSlotProdEntry':adGenSubSlotProdEntry,_F:adGenSubSlotProdInfoIndex,'adGenSubSlotProdName':adGenSubSlotProdName,'adGenSubSlotProdPartNumber':adGenSubSlotProdPartNumber,'adGenSubSlotProdCLEIcode':adGenSubSlotProdCLEIcode,'adGenSubSlotProdSerialNumber':adGenSubSlotProdSerialNumber,'adGenSubSlotProdRevision':adGenSubSlotProdRevision,'adGenSubSlotProdSwVersion':adGenSubSlotProdSwVersion,'adGenSubSlotProdDateOfManufacturing':adGenSubSlotProdDateOfManufacturing})