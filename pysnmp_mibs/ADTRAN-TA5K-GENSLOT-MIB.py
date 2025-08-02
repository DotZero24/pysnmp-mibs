_L='adGenTa5kSlotDeviceIndex'
_K='not-accessible'
_J='adGenTa5kSlotMacAddressIndex'
_I='read-write'
_H='DisplayString'
_G='OctetString'
_F='ADTRAN-TA5K-GENSLOT-MIB'
_E='Integer32'
_D='adGenSlotInfoIndex'
_C='ADTRAN-GENSLOT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenericShelves,=mibBuilder.importSymbols('ADTRAN-GENCHASSIS-MIB','adGenericShelves')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_C,_D)
adGenTa5kSlot,adGenTa5kSlotID=mibBuilder.importSymbols('ADTRAN-GENTA5K-MIB','adGenTa5kSlot','adGenTa5kSlotID')
AdPresence,AdProductIdentifier=mibBuilder.importSymbols('ADTRAN-TC','AdPresence','AdProductIdentifier')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
adGenTa5kSlotModuleIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,67,1,8,1))
if mibBuilder.loadTexts:adGenTa5kSlotModuleIdentity.setRevisions(('2014-10-09 00:00','2013-10-03 00:00'))
_AdGenTa5kSlotTable_Object=MibTable
adGenTa5kSlotTable=_AdGenTa5kSlotTable_Object((1,3,6,1,4,1,664,5,67,1,8,1))
if mibBuilder.loadTexts:adGenTa5kSlotTable.setStatus(_A)
_AdGenTa5kSlotEntry_Object=MibTableRow
adGenTa5kSlotEntry=_AdGenTa5kSlotEntry_Object((1,3,6,1,4,1,664,5,67,1,8,1,1))
adGenTa5kSlotEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adGenTa5kSlotEntry.setStatus(_A)
_AdGenTa5kSlotRestoreFactoryDefaults_Type=Integer32
_AdGenTa5kSlotRestoreFactoryDefaults_Object=MibTableColumn
adGenTa5kSlotRestoreFactoryDefaults=_AdGenTa5kSlotRestoreFactoryDefaults_Object((1,3,6,1,4,1,664,5,67,1,8,1,1,1),_AdGenTa5kSlotRestoreFactoryDefaults_Type())
adGenTa5kSlotRestoreFactoryDefaults.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenTa5kSlotRestoreFactoryDefaults.setStatus(_A)
_AdGenTa5kSlotReboot_Type=Integer32
_AdGenTa5kSlotReboot_Object=MibTableColumn
adGenTa5kSlotReboot=_AdGenTa5kSlotReboot_Object((1,3,6,1,4,1,664,5,67,1,8,1,1,2),_AdGenTa5kSlotReboot_Type())
adGenTa5kSlotReboot.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenTa5kSlotReboot.setStatus(_A)
_AdGenTa5kSlotMaxMacs_Type=Integer32
_AdGenTa5kSlotMaxMacs_Object=MibTableColumn
adGenTa5kSlotMaxMacs=_AdGenTa5kSlotMaxMacs_Object((1,3,6,1,4,1,664,5,67,1,8,1,1,3),_AdGenTa5kSlotMaxMacs_Type())
adGenTa5kSlotMaxMacs.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTa5kSlotMaxMacs.setStatus(_A)
class _AdGenTa5kSlotFlashStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('busy',1),('idle',2)))
_AdGenTa5kSlotFlashStatus_Type.__name__=_E
_AdGenTa5kSlotFlashStatus_Object=MibTableColumn
adGenTa5kSlotFlashStatus=_AdGenTa5kSlotFlashStatus_Object((1,3,6,1,4,1,664,5,67,1,8,1,1,4),_AdGenTa5kSlotFlashStatus_Type())
adGenTa5kSlotFlashStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTa5kSlotFlashStatus.setStatus(_A)
_AdGenTa5kSlotSystemSwVersion_Type=DisplayString
_AdGenTa5kSlotSystemSwVersion_Object=MibTableColumn
adGenTa5kSlotSystemSwVersion=_AdGenTa5kSlotSystemSwVersion_Object((1,3,6,1,4,1,664,5,67,1,8,1,1,5),_AdGenTa5kSlotSystemSwVersion_Type())
adGenTa5kSlotSystemSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTa5kSlotSystemSwVersion.setStatus(_A)
_AdGenTa5kSlotBootSwVersion_Type=DisplayString
_AdGenTa5kSlotBootSwVersion_Object=MibTableColumn
adGenTa5kSlotBootSwVersion=_AdGenTa5kSlotBootSwVersion_Object((1,3,6,1,4,1,664,5,67,1,8,1,1,6),_AdGenTa5kSlotBootSwVersion_Type())
adGenTa5kSlotBootSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTa5kSlotBootSwVersion.setStatus(_A)
_AdGenTa5kSlotBootSystemSwVersion_Type=DisplayString
_AdGenTa5kSlotBootSystemSwVersion_Object=MibTableColumn
adGenTa5kSlotBootSystemSwVersion=_AdGenTa5kSlotBootSystemSwVersion_Object((1,3,6,1,4,1,664,5,67,1,8,1,1,7),_AdGenTa5kSlotBootSystemSwVersion_Type())
adGenTa5kSlotBootSystemSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTa5kSlotBootSystemSwVersion.setStatus(_A)
_AdGenTa5kSlotDateOfManufacture_Type=DisplayString
_AdGenTa5kSlotDateOfManufacture_Object=MibTableColumn
adGenTa5kSlotDateOfManufacture=_AdGenTa5kSlotDateOfManufacture_Object((1,3,6,1,4,1,664,5,67,1,8,1,1,8),_AdGenTa5kSlotDateOfManufacture_Type())
adGenTa5kSlotDateOfManufacture.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTa5kSlotDateOfManufacture.setStatus(_A)
_AdGenTa5kSlotSwVerInstallTime_Type=DisplayString
_AdGenTa5kSlotSwVerInstallTime_Object=MibTableColumn
adGenTa5kSlotSwVerInstallTime=_AdGenTa5kSlotSwVerInstallTime_Object((1,3,6,1,4,1,664,5,67,1,8,1,1,9),_AdGenTa5kSlotSwVerInstallTime_Type())
adGenTa5kSlotSwVerInstallTime.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTa5kSlotSwVerInstallTime.setStatus(_A)
class _AdGenTa5kSlotIOModuleID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_AdGenTa5kSlotIOModuleID_Type.__name__=_H
_AdGenTa5kSlotIOModuleID_Object=MibTableColumn
adGenTa5kSlotIOModuleID=_AdGenTa5kSlotIOModuleID_Object((1,3,6,1,4,1,664,5,67,1,8,1,1,10),_AdGenTa5kSlotIOModuleID_Type())
adGenTa5kSlotIOModuleID.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTa5kSlotIOModuleID.setStatus(_A)
_AdGenTa5kSlotMacAddressTable_Object=MibTable
adGenTa5kSlotMacAddressTable=_AdGenTa5kSlotMacAddressTable_Object((1,3,6,1,4,1,664,5,67,1,8,2))
if mibBuilder.loadTexts:adGenTa5kSlotMacAddressTable.setStatus(_A)
_AdGenTa5kSlotMacAddressEntry_Object=MibTableRow
adGenTa5kSlotMacAddressEntry=_AdGenTa5kSlotMacAddressEntry_Object((1,3,6,1,4,1,664,5,67,1,8,2,1))
adGenTa5kSlotMacAddressEntry.setIndexNames((0,_C,_D),(0,_F,_J))
if mibBuilder.loadTexts:adGenTa5kSlotMacAddressEntry.setStatus(_A)
class _AdGenTa5kSlotMacAddressIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdGenTa5kSlotMacAddressIndex_Type.__name__=_E
_AdGenTa5kSlotMacAddressIndex_Object=MibTableColumn
adGenTa5kSlotMacAddressIndex=_AdGenTa5kSlotMacAddressIndex_Object((1,3,6,1,4,1,664,5,67,1,8,2,1,1),_AdGenTa5kSlotMacAddressIndex_Type())
adGenTa5kSlotMacAddressIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:adGenTa5kSlotMacAddressIndex.setStatus(_A)
class _AdGenTa5kSlotMacAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_AdGenTa5kSlotMacAddress_Type.__name__=_G
_AdGenTa5kSlotMacAddress_Object=MibTableColumn
adGenTa5kSlotMacAddress=_AdGenTa5kSlotMacAddress_Object((1,3,6,1,4,1,664,5,67,1,8,2,1,2),_AdGenTa5kSlotMacAddress_Type())
adGenTa5kSlotMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTa5kSlotMacAddress.setStatus(_A)
_AdGenTa5kSlotDeviceTable_Object=MibTable
adGenTa5kSlotDeviceTable=_AdGenTa5kSlotDeviceTable_Object((1,3,6,1,4,1,664,5,67,1,8,3))
if mibBuilder.loadTexts:adGenTa5kSlotDeviceTable.setStatus(_A)
_AdGenTa5kSlotDeviceEntry_Object=MibTableRow
adGenTa5kSlotDeviceEntry=_AdGenTa5kSlotDeviceEntry_Object((1,3,6,1,4,1,664,5,67,1,8,3,1))
adGenTa5kSlotDeviceEntry.setIndexNames((0,_C,_D),(0,_F,_L))
if mibBuilder.loadTexts:adGenTa5kSlotDeviceEntry.setStatus(_A)
class _AdGenTa5kSlotDeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdGenTa5kSlotDeviceIndex_Type.__name__=_E
_AdGenTa5kSlotDeviceIndex_Object=MibTableColumn
adGenTa5kSlotDeviceIndex=_AdGenTa5kSlotDeviceIndex_Object((1,3,6,1,4,1,664,5,67,1,8,3,1,1),_AdGenTa5kSlotDeviceIndex_Type())
adGenTa5kSlotDeviceIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:adGenTa5kSlotDeviceIndex.setStatus(_A)
_AdGenTa5kSlotDeviceDesc_Type=DisplayString
_AdGenTa5kSlotDeviceDesc_Object=MibTableColumn
adGenTa5kSlotDeviceDesc=_AdGenTa5kSlotDeviceDesc_Object((1,3,6,1,4,1,664,5,67,1,8,3,1,2),_AdGenTa5kSlotDeviceDesc_Type())
adGenTa5kSlotDeviceDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTa5kSlotDeviceDesc.setStatus(_A)
_AdGenTa5kSlotDeviceRevision_Type=DisplayString
_AdGenTa5kSlotDeviceRevision_Object=MibTableColumn
adGenTa5kSlotDeviceRevision=_AdGenTa5kSlotDeviceRevision_Object((1,3,6,1,4,1,664,5,67,1,8,3,1,3),_AdGenTa5kSlotDeviceRevision_Type())
adGenTa5kSlotDeviceRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTa5kSlotDeviceRevision.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'adGenTa5kSlotTable':adGenTa5kSlotTable,'adGenTa5kSlotEntry':adGenTa5kSlotEntry,'adGenTa5kSlotRestoreFactoryDefaults':adGenTa5kSlotRestoreFactoryDefaults,'adGenTa5kSlotReboot':adGenTa5kSlotReboot,'adGenTa5kSlotMaxMacs':adGenTa5kSlotMaxMacs,'adGenTa5kSlotFlashStatus':adGenTa5kSlotFlashStatus,'adGenTa5kSlotSystemSwVersion':adGenTa5kSlotSystemSwVersion,'adGenTa5kSlotBootSwVersion':adGenTa5kSlotBootSwVersion,'adGenTa5kSlotBootSystemSwVersion':adGenTa5kSlotBootSystemSwVersion,'adGenTa5kSlotDateOfManufacture':adGenTa5kSlotDateOfManufacture,'adGenTa5kSlotSwVerInstallTime':adGenTa5kSlotSwVerInstallTime,'adGenTa5kSlotIOModuleID':adGenTa5kSlotIOModuleID,'adGenTa5kSlotMacAddressTable':adGenTa5kSlotMacAddressTable,'adGenTa5kSlotMacAddressEntry':adGenTa5kSlotMacAddressEntry,_J:adGenTa5kSlotMacAddressIndex,'adGenTa5kSlotMacAddress':adGenTa5kSlotMacAddress,'adGenTa5kSlotDeviceTable':adGenTa5kSlotDeviceTable,'adGenTa5kSlotDeviceEntry':adGenTa5kSlotDeviceEntry,_L:adGenTa5kSlotDeviceIndex,'adGenTa5kSlotDeviceDesc':adGenTa5kSlotDeviceDesc,'adGenTa5kSlotDeviceRevision':adGenTa5kSlotDeviceRevision,'adGenTa5kSlotModuleIdentity':adGenTa5kSlotModuleIdentity})