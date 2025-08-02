_G='not-accessible'
_F='cnUsbSlotIndex'
_E='CAMBIUM-NETWORKS-USB-MIB'
_D='Integer32'
_C='read-only'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
cnUsbMib=ModuleIdentity((1,3,6,1,4,1,17713,24,3))
if mibBuilder.loadTexts:cnUsbMib.setRevisions(('2019-03-14 00:00',))
_CnUsbMountDevice_ObjectIdentity=ObjectIdentity
cnUsbMountDevice=_CnUsbMountDevice_ObjectIdentity((1,3,6,1,4,1,17713,24,3,0))
class _CnUsbMount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mount',1),('unmount',2)))
_CnUsbMount_Type.__name__=_D
_CnUsbMount_Object=MibScalar
cnUsbMount=_CnUsbMount_Object((1,3,6,1,4,1,17713,24,3,0,1),_CnUsbMount_Type())
cnUsbMount.setMaxAccess('read-write')
if mibBuilder.loadTexts:cnUsbMount.setStatus(_A)
_CnUsbDeviceTable_ObjectIdentity=ObjectIdentity
cnUsbDeviceTable=_CnUsbDeviceTable_ObjectIdentity((1,3,6,1,4,1,17713,24,3,1))
_CnUsbTable_Object=MibTable
cnUsbTable=_CnUsbTable_Object((1,3,6,1,4,1,17713,24,3,1,1))
if mibBuilder.loadTexts:cnUsbTable.setStatus(_A)
_CnUsbEntry_Object=MibTableRow
cnUsbEntry=_CnUsbEntry_Object((1,3,6,1,4,1,17713,24,3,1,1,1))
cnUsbEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cnUsbEntry.setStatus(_A)
class _CnUsbSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_CnUsbSlotIndex_Type.__name__=_D
_CnUsbSlotIndex_Object=MibTableColumn
cnUsbSlotIndex=_CnUsbSlotIndex_Object((1,3,6,1,4,1,17713,24,3,1,1,1,1),_CnUsbSlotIndex_Type())
cnUsbSlotIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cnUsbSlotIndex.setStatus(_A)
class _CnUsbSlotDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CnUsbSlotDescription_Type.__name__=_B
_CnUsbSlotDescription_Object=MibTableColumn
cnUsbSlotDescription=_CnUsbSlotDescription_Object((1,3,6,1,4,1,17713,24,3,1,1,1,2),_CnUsbSlotDescription_Type())
cnUsbSlotDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cnUsbSlotDescription.setStatus(_A)
class _CnUsbVendorId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnUsbVendorId_Type.__name__=_B
_CnUsbVendorId_Object=MibTableColumn
cnUsbVendorId=_CnUsbVendorId_Object((1,3,6,1,4,1,17713,24,3,1,1,1,3),_CnUsbVendorId_Type())
cnUsbVendorId.setMaxAccess(_C)
if mibBuilder.loadTexts:cnUsbVendorId.setStatus(_A)
class _CnUsbManufacturer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnUsbManufacturer_Type.__name__=_B
_CnUsbManufacturer_Object=MibTableColumn
cnUsbManufacturer=_CnUsbManufacturer_Object((1,3,6,1,4,1,17713,24,3,1,1,1,4),_CnUsbManufacturer_Type())
cnUsbManufacturer.setMaxAccess(_C)
if mibBuilder.loadTexts:cnUsbManufacturer.setStatus(_A)
class _CnUsbProductId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnUsbProductId_Type.__name__=_B
_CnUsbProductId_Object=MibTableColumn
cnUsbProductId=_CnUsbProductId_Object((1,3,6,1,4,1,17713,24,3,1,1,1,5),_CnUsbProductId_Type())
cnUsbProductId.setMaxAccess(_C)
if mibBuilder.loadTexts:cnUsbProductId.setStatus(_A)
class _CnUsbProductName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnUsbProductName_Type.__name__=_B
_CnUsbProductName_Object=MibTableColumn
cnUsbProductName=_CnUsbProductName_Object((1,3,6,1,4,1,17713,24,3,1,1,1,6),_CnUsbProductName_Type())
cnUsbProductName.setMaxAccess(_C)
if mibBuilder.loadTexts:cnUsbProductName.setStatus(_A)
class _CnUsbSerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnUsbSerialNumber_Type.__name__=_B
_CnUsbSerialNumber_Object=MibTableColumn
cnUsbSerialNumber=_CnUsbSerialNumber_Object((1,3,6,1,4,1,17713,24,3,1,1,1,7),_CnUsbSerialNumber_Type())
cnUsbSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cnUsbSerialNumber.setStatus(_A)
class _CnUsbVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_CnUsbVersion_Type.__name__=_B
_CnUsbVersion_Object=MibTableColumn
cnUsbVersion=_CnUsbVersion_Object((1,3,6,1,4,1,17713,24,3,1,1,1,8),_CnUsbVersion_Type())
cnUsbVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cnUsbVersion.setStatus(_A)
_CnUsbMaxCurrent_Type=Integer32
_CnUsbMaxCurrent_Object=MibTableColumn
cnUsbMaxCurrent=_CnUsbMaxCurrent_Object((1,3,6,1,4,1,17713,24,3,1,1,1,9),_CnUsbMaxCurrent_Type())
cnUsbMaxCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:cnUsbMaxCurrent.setStatus(_A)
if mibBuilder.loadTexts:cnUsbMaxCurrent.setUnits('milliamps')
_CnUsbDeviceFiles_ObjectIdentity=ObjectIdentity
cnUsbDeviceFiles=_CnUsbDeviceFiles_ObjectIdentity((1,3,6,1,4,1,17713,24,3,2))
_CnUsbFile_Object=MibTable
cnUsbFile=_CnUsbFile_Object((1,3,6,1,4,1,17713,24,3,2,1))
if mibBuilder.loadTexts:cnUsbFile.setStatus(_A)
_CnUsbFileEntry_Object=MibTableRow
cnUsbFileEntry=_CnUsbFileEntry_Object((1,3,6,1,4,1,17713,24,3,2,1,1))
cnUsbFileEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cnUsbFileEntry.setStatus(_A)
class _CnUsbFileSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_CnUsbFileSlot_Type.__name__=_D
_CnUsbFileSlot_Object=MibTableColumn
cnUsbFileSlot=_CnUsbFileSlot_Object((1,3,6,1,4,1,17713,24,3,2,1,1,1),_CnUsbFileSlot_Type())
cnUsbFileSlot.setMaxAccess(_G)
if mibBuilder.loadTexts:cnUsbFileSlot.setStatus(_A)
class _CnUsbFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,114))
_CnUsbFileName_Type.__name__=_B
_CnUsbFileName_Object=MibTableColumn
cnUsbFileName=_CnUsbFileName_Object((1,3,6,1,4,1,17713,24,3,2,1,1,2),_CnUsbFileName_Type())
cnUsbFileName.setMaxAccess(_G)
if mibBuilder.loadTexts:cnUsbFileName.setStatus(_A)
class _CnUsbFileDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnUsbFileDate_Type.__name__=_B
_CnUsbFileDate_Object=MibTableColumn
cnUsbFileDate=_CnUsbFileDate_Object((1,3,6,1,4,1,17713,24,3,2,1,1,3),_CnUsbFileDate_Type())
cnUsbFileDate.setMaxAccess(_C)
if mibBuilder.loadTexts:cnUsbFileDate.setStatus(_A)
_CnUsbFileSize_Type=Unsigned32
_CnUsbFileSize_Object=MibTableColumn
cnUsbFileSize=_CnUsbFileSize_Object((1,3,6,1,4,1,17713,24,3,2,1,1,4),_CnUsbFileSize_Type())
cnUsbFileSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cnUsbFileSize.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'cnUsbMib':cnUsbMib,'cnUsbMountDevice':cnUsbMountDevice,'cnUsbMount':cnUsbMount,'cnUsbDeviceTable':cnUsbDeviceTable,'cnUsbTable':cnUsbTable,'cnUsbEntry':cnUsbEntry,_F:cnUsbSlotIndex,'cnUsbSlotDescription':cnUsbSlotDescription,'cnUsbVendorId':cnUsbVendorId,'cnUsbManufacturer':cnUsbManufacturer,'cnUsbProductId':cnUsbProductId,'cnUsbProductName':cnUsbProductName,'cnUsbSerialNumber':cnUsbSerialNumber,'cnUsbVersion':cnUsbVersion,'cnUsbMaxCurrent':cnUsbMaxCurrent,'cnUsbDeviceFiles':cnUsbDeviceFiles,'cnUsbFile':cnUsbFile,'cnUsbFileEntry':cnUsbFileEntry,'cnUsbFileSlot':cnUsbFileSlot,'cnUsbFileName':cnUsbFileName,'cnUsbFileDate':cnUsbFileDate,'cnUsbFileSize':cnUsbFileSize})