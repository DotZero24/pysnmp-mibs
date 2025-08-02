_G='rlComponentMapperIndex'
_F='rlComponentMapperType'
_E='rlComponentMapperUnitNum'
_D='not-accessible'
_C='CISCOSB-ComponentMapper-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rlComponentMapper=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,243))
if mibBuilder.loadTexts:rlComponentMapper.setRevisions(('2019-04-03 00:00',))
class ComponentType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('cpu',1),('packetProcessor',2),('phy',3),('flash',4),('sfp',5),('poe',6),('cpld',7),('image',8),('kernel',9),('bootloader',10),('fanController',11),('ssh',12),('ssl',13),('mcu',14)))
_RlComponentMapperTable_Object=MibTable
rlComponentMapperTable=_RlComponentMapperTable_Object((1,3,6,1,4,1,9,6,1,101,243,1))
if mibBuilder.loadTexts:rlComponentMapperTable.setStatus(_A)
_RlComponentMapperEntry_Object=MibTableRow
rlComponentMapperEntry=_RlComponentMapperEntry_Object((1,3,6,1,4,1,9,6,1,101,243,1,1))
rlComponentMapperEntry.setIndexNames((0,_C,_E),(0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:rlComponentMapperEntry.setStatus(_A)
_RlComponentMapperUnitNum_Type=Integer32
_RlComponentMapperUnitNum_Object=MibTableColumn
rlComponentMapperUnitNum=_RlComponentMapperUnitNum_Object((1,3,6,1,4,1,9,6,1,101,243,1,1,1),_RlComponentMapperUnitNum_Type())
rlComponentMapperUnitNum.setMaxAccess(_D)
if mibBuilder.loadTexts:rlComponentMapperUnitNum.setStatus(_A)
_RlComponentMapperType_Type=ComponentType
_RlComponentMapperType_Object=MibTableColumn
rlComponentMapperType=_RlComponentMapperType_Object((1,3,6,1,4,1,9,6,1,101,243,1,1,2),_RlComponentMapperType_Type())
rlComponentMapperType.setMaxAccess(_D)
if mibBuilder.loadTexts:rlComponentMapperType.setStatus(_A)
_RlComponentMapperIndex_Type=Integer32
_RlComponentMapperIndex_Object=MibTableColumn
rlComponentMapperIndex=_RlComponentMapperIndex_Object((1,3,6,1,4,1,9,6,1,101,243,1,1,3),_RlComponentMapperIndex_Type())
rlComponentMapperIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rlComponentMapperIndex.setStatus(_A)
_RlComponentMapperVendorID_Type=DisplayString
_RlComponentMapperVendorID_Object=MibTableColumn
rlComponentMapperVendorID=_RlComponentMapperVendorID_Object((1,3,6,1,4,1,9,6,1,101,243,1,1,4),_RlComponentMapperVendorID_Type())
rlComponentMapperVendorID.setMaxAccess(_B)
if mibBuilder.loadTexts:rlComponentMapperVendorID.setStatus(_A)
_RlComponentMapperDeviceID_Type=DisplayString
_RlComponentMapperDeviceID_Object=MibTableColumn
rlComponentMapperDeviceID=_RlComponentMapperDeviceID_Object((1,3,6,1,4,1,9,6,1,101,243,1,1,5),_RlComponentMapperDeviceID_Type())
rlComponentMapperDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:rlComponentMapperDeviceID.setStatus(_A)
_RlComponentMapperHardwareVersionID_Type=DisplayString
_RlComponentMapperHardwareVersionID_Object=MibTableColumn
rlComponentMapperHardwareVersionID=_RlComponentMapperHardwareVersionID_Object((1,3,6,1,4,1,9,6,1,101,243,1,1,6),_RlComponentMapperHardwareVersionID_Type())
rlComponentMapperHardwareVersionID.setMaxAccess(_B)
if mibBuilder.loadTexts:rlComponentMapperHardwareVersionID.setStatus(_A)
_RlComponentMapperSoftwareVersionID_Type=DisplayString
_RlComponentMapperSoftwareVersionID_Object=MibTableColumn
rlComponentMapperSoftwareVersionID=_RlComponentMapperSoftwareVersionID_Object((1,3,6,1,4,1,9,6,1,101,243,1,1,7),_RlComponentMapperSoftwareVersionID_Type())
rlComponentMapperSoftwareVersionID.setMaxAccess(_B)
if mibBuilder.loadTexts:rlComponentMapperSoftwareVersionID.setStatus(_A)
_RlComponentMapperAliasID_Type=DisplayString
_RlComponentMapperAliasID_Object=MibTableColumn
rlComponentMapperAliasID=_RlComponentMapperAliasID_Object((1,3,6,1,4,1,9,6,1,101,243,1,1,8),_RlComponentMapperAliasID_Type())
rlComponentMapperAliasID.setMaxAccess(_B)
if mibBuilder.loadTexts:rlComponentMapperAliasID.setStatus(_A)
_RlComponentMapperProductNumber_Type=DisplayString
_RlComponentMapperProductNumber_Object=MibTableColumn
rlComponentMapperProductNumber=_RlComponentMapperProductNumber_Object((1,3,6,1,4,1,9,6,1,101,243,1,1,9),_RlComponentMapperProductNumber_Type())
rlComponentMapperProductNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rlComponentMapperProductNumber.setStatus(_A)
_RlComponentMapperSerialNumber_Type=DisplayString
_RlComponentMapperSerialNumber_Object=MibTableColumn
rlComponentMapperSerialNumber=_RlComponentMapperSerialNumber_Object((1,3,6,1,4,1,9,6,1,101,243,1,1,10),_RlComponentMapperSerialNumber_Type())
rlComponentMapperSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rlComponentMapperSerialNumber.setStatus(_A)
_RlComponentMapperPartNumber_Type=DisplayString
_RlComponentMapperPartNumber_Object=MibTableColumn
rlComponentMapperPartNumber=_RlComponentMapperPartNumber_Object((1,3,6,1,4,1,9,6,1,101,243,1,1,11),_RlComponentMapperPartNumber_Type())
rlComponentMapperPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rlComponentMapperPartNumber.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ComponentType':ComponentType,'rlComponentMapper':rlComponentMapper,'rlComponentMapperTable':rlComponentMapperTable,'rlComponentMapperEntry':rlComponentMapperEntry,_E:rlComponentMapperUnitNum,_F:rlComponentMapperType,_G:rlComponentMapperIndex,'rlComponentMapperVendorID':rlComponentMapperVendorID,'rlComponentMapperDeviceID':rlComponentMapperDeviceID,'rlComponentMapperHardwareVersionID':rlComponentMapperHardwareVersionID,'rlComponentMapperSoftwareVersionID':rlComponentMapperSoftwareVersionID,'rlComponentMapperAliasID':rlComponentMapperAliasID,'rlComponentMapperProductNumber':rlComponentMapperProductNumber,'rlComponentMapperSerialNumber':rlComponentMapperSerialNumber,'rlComponentMapperPartNumber':rlComponentMapperPartNumber})