_R='sysExtNSwitchIPAddress'
_Q='sysExtNSwitchIPAddressType'
_P='sysExtLicenseIndex'
_O='sysExtSwitchIPAddress'
_N='sysExtPowerSupplyIndex'
_M='sysExtFanIndex'
_L='sysExtCardSlot'
_K='sysExtMemoryIndex'
_J='sysExtStorageIndex'
_I='sysExtProcessorID'
_H='read-write'
_G='Integer32'
_F='not-accessible'
_E='deprecated'
_D='WLSX-SYSTEMEXT-MIB'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wlsxEnterpriseMibModules,=mibBuilder.importSymbols('ARUBA-MIB','wlsxEnterpriseMibModules')
ArubaActiveState,ArubaCardType,ArubaSwitchRole=mibBuilder.importSymbols('ARUBA-TC','ArubaActiveState','ArubaCardType','ArubaSwitchRole')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,snmpModules=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','snmpModules')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TAddress,TDomain,TextualConvention,TestAndIncr,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_C,'MacAddress','PhysAddress','RowStatus','StorageType','TAddress','TDomain','TextualConvention','TestAndIncr','TimeInterval','TruthValue')
wlsxSystemExtMIB=ModuleIdentity((1,3,6,1,4,1,14823,2,2,1,2))
if mibBuilder.loadTexts:wlsxSystemExtMIB.setRevisions(('2020-08-14 17:45',))
_WlsxSystemExtGroup_ObjectIdentity=ObjectIdentity
wlsxSystemExtGroup=_WlsxSystemExtGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,2,1))
_WlsxSysExtSwitchIp_Type=IpAddress
_WlsxSysExtSwitchIp_Object=MibScalar
wlsxSysExtSwitchIp=_WlsxSysExtSwitchIp_Object((1,3,6,1,4,1,14823,2,2,1,2,1,1),_WlsxSysExtSwitchIp_Type())
wlsxSysExtSwitchIp.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtSwitchIp.setStatus(_A)
class _WlsxSysExtHostname_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_WlsxSysExtHostname_Type.__name__=_C
_WlsxSysExtHostname_Object=MibScalar
wlsxSysExtHostname=_WlsxSysExtHostname_Object((1,3,6,1,4,1,14823,2,2,1,2,1,2),_WlsxSysExtHostname_Type())
wlsxSysExtHostname.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtHostname.setStatus(_A)
class _WlsxSysExtModelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_WlsxSysExtModelName_Type.__name__=_C
_WlsxSysExtModelName_Object=MibScalar
wlsxSysExtModelName=_WlsxSysExtModelName_Object((1,3,6,1,4,1,14823,2,2,1,2,1,3),_WlsxSysExtModelName_Type())
wlsxSysExtModelName.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtModelName.setStatus(_A)
_WlsxSysExtSwitchRole_Type=ArubaSwitchRole
_WlsxSysExtSwitchRole_Object=MibScalar
wlsxSysExtSwitchRole=_WlsxSysExtSwitchRole_Object((1,3,6,1,4,1,14823,2,2,1,2,1,4),_WlsxSysExtSwitchRole_Type())
wlsxSysExtSwitchRole.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtSwitchRole.setStatus(_A)
_WlsxSysExtSwitchMasterIp_Type=IpAddress
_WlsxSysExtSwitchMasterIp_Object=MibScalar
wlsxSysExtSwitchMasterIp=_WlsxSysExtSwitchMasterIp_Object((1,3,6,1,4,1,14823,2,2,1,2,1,5),_WlsxSysExtSwitchMasterIp_Type())
wlsxSysExtSwitchMasterIp.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtSwitchMasterIp.setStatus('obsolete')
class _WlsxSysExtSwitchDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxSysExtSwitchDate_Type.__name__=_C
_WlsxSysExtSwitchDate_Object=MibScalar
wlsxSysExtSwitchDate=_WlsxSysExtSwitchDate_Object((1,3,6,1,4,1,14823,2,2,1,2,1,6),_WlsxSysExtSwitchDate_Type())
wlsxSysExtSwitchDate.setMaxAccess(_H)
if mibBuilder.loadTexts:wlsxSysExtSwitchDate.setStatus(_A)
_WlsxSysExtSwitchBaseMacaddress_Type=MacAddress
_WlsxSysExtSwitchBaseMacaddress_Object=MibScalar
wlsxSysExtSwitchBaseMacaddress=_WlsxSysExtSwitchBaseMacaddress_Object((1,3,6,1,4,1,14823,2,2,1,2,1,7),_WlsxSysExtSwitchBaseMacaddress_Type())
wlsxSysExtSwitchBaseMacaddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtSwitchBaseMacaddress.setStatus(_A)
class _WlsxSysExtFanTrayAssemblyNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxSysExtFanTrayAssemblyNumber_Type.__name__=_C
_WlsxSysExtFanTrayAssemblyNumber_Object=MibScalar
wlsxSysExtFanTrayAssemblyNumber=_WlsxSysExtFanTrayAssemblyNumber_Object((1,3,6,1,4,1,14823,2,2,1,2,1,8),_WlsxSysExtFanTrayAssemblyNumber_Type())
wlsxSysExtFanTrayAssemblyNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtFanTrayAssemblyNumber.setStatus(_A)
class _WlsxSysExtFanTraySerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxSysExtFanTraySerialNumber_Type.__name__=_C
_WlsxSysExtFanTraySerialNumber_Object=MibScalar
wlsxSysExtFanTraySerialNumber=_WlsxSysExtFanTraySerialNumber_Object((1,3,6,1,4,1,14823,2,2,1,2,1,9),_WlsxSysExtFanTraySerialNumber_Type())
wlsxSysExtFanTraySerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtFanTraySerialNumber.setStatus(_A)
class _WlsxSysExtInternalTemparature_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxSysExtInternalTemparature_Type.__name__=_C
_WlsxSysExtInternalTemparature_Object=MibScalar
wlsxSysExtInternalTemparature=_WlsxSysExtInternalTemparature_Object((1,3,6,1,4,1,14823,2,2,1,2,1,10),_WlsxSysExtInternalTemparature_Type())
wlsxSysExtInternalTemparature.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtInternalTemparature.setStatus(_A)
class _WlsxSysExtLicenseSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxSysExtLicenseSerialNumber_Type.__name__=_C
_WlsxSysExtLicenseSerialNumber_Object=MibScalar
wlsxSysExtLicenseSerialNumber=_WlsxSysExtLicenseSerialNumber_Object((1,3,6,1,4,1,14823,2,2,1,2,1,11),_WlsxSysExtLicenseSerialNumber_Type())
wlsxSysExtLicenseSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtLicenseSerialNumber.setStatus(_A)
_WlsxSysExtSwitchLicenseCount_Type=Integer32
_WlsxSysExtSwitchLicenseCount_Object=MibScalar
wlsxSysExtSwitchLicenseCount=_WlsxSysExtSwitchLicenseCount_Object((1,3,6,1,4,1,14823,2,2,1,2,1,12),_WlsxSysExtSwitchLicenseCount_Type())
wlsxSysExtSwitchLicenseCount.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtSwitchLicenseCount.setStatus(_A)
_WlsxSysExtProcessorTable_Object=MibTable
wlsxSysExtProcessorTable=_WlsxSysExtProcessorTable_Object((1,3,6,1,4,1,14823,2,2,1,2,1,13))
if mibBuilder.loadTexts:wlsxSysExtProcessorTable.setStatus(_A)
_WlsxSysExtProcessorEntry_Object=MibTableRow
wlsxSysExtProcessorEntry=_WlsxSysExtProcessorEntry_Object((1,3,6,1,4,1,14823,2,2,1,2,1,13,1))
wlsxSysExtProcessorEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:wlsxSysExtProcessorEntry.setStatus(_A)
_SysExtProcessorID_Type=Integer32
_SysExtProcessorID_Object=MibTableColumn
sysExtProcessorID=_SysExtProcessorID_Object((1,3,6,1,4,1,14823,2,2,1,2,1,13,1,1),_SysExtProcessorID_Type())
sysExtProcessorID.setMaxAccess(_F)
if mibBuilder.loadTexts:sysExtProcessorID.setStatus(_A)
class _SysExtProcessorDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SysExtProcessorDescr_Type.__name__=_C
_SysExtProcessorDescr_Object=MibTableColumn
sysExtProcessorDescr=_SysExtProcessorDescr_Object((1,3,6,1,4,1,14823,2,2,1,2,1,13,1,2),_SysExtProcessorDescr_Type())
sysExtProcessorDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtProcessorDescr.setStatus(_A)
class _SysExtProcessorLoad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SysExtProcessorLoad_Type.__name__=_G
_SysExtProcessorLoad_Object=MibTableColumn
sysExtProcessorLoad=_SysExtProcessorLoad_Object((1,3,6,1,4,1,14823,2,2,1,2,1,13,1,3),_SysExtProcessorLoad_Type())
sysExtProcessorLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtProcessorLoad.setStatus(_A)
_WlsxSysExtStorageTable_Object=MibTable
wlsxSysExtStorageTable=_WlsxSysExtStorageTable_Object((1,3,6,1,4,1,14823,2,2,1,2,1,14))
if mibBuilder.loadTexts:wlsxSysExtStorageTable.setStatus(_A)
_WlsxSysExtStorageEntry_Object=MibTableRow
wlsxSysExtStorageEntry=_WlsxSysExtStorageEntry_Object((1,3,6,1,4,1,14823,2,2,1,2,1,14,1))
wlsxSysExtStorageEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:wlsxSysExtStorageEntry.setStatus(_A)
_SysExtStorageIndex_Type=Integer32
_SysExtStorageIndex_Object=MibTableColumn
sysExtStorageIndex=_SysExtStorageIndex_Object((1,3,6,1,4,1,14823,2,2,1,2,1,14,1,1),_SysExtStorageIndex_Type())
sysExtStorageIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:sysExtStorageIndex.setStatus(_A)
class _SysExtStorageType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ram',1),('flashMemory',2)))
_SysExtStorageType_Type.__name__=_G
_SysExtStorageType_Object=MibTableColumn
sysExtStorageType=_SysExtStorageType_Object((1,3,6,1,4,1,14823,2,2,1,2,1,14,1,2),_SysExtStorageType_Type())
sysExtStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtStorageType.setStatus(_A)
_SysExtStorageSize_Type=Integer32
_SysExtStorageSize_Object=MibTableColumn
sysExtStorageSize=_SysExtStorageSize_Object((1,3,6,1,4,1,14823,2,2,1,2,1,14,1,3),_SysExtStorageSize_Type())
sysExtStorageSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtStorageSize.setStatus(_A)
_SysExtStorageUsed_Type=Integer32
_SysExtStorageUsed_Object=MibTableColumn
sysExtStorageUsed=_SysExtStorageUsed_Object((1,3,6,1,4,1,14823,2,2,1,2,1,14,1,4),_SysExtStorageUsed_Type())
sysExtStorageUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtStorageUsed.setStatus(_A)
class _SysExtStorageName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SysExtStorageName_Type.__name__=_C
_SysExtStorageName_Object=MibTableColumn
sysExtStorageName=_SysExtStorageName_Object((1,3,6,1,4,1,14823,2,2,1,2,1,14,1,5),_SysExtStorageName_Type())
sysExtStorageName.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtStorageName.setStatus(_A)
_WlsxSysExtMemoryTable_Object=MibTable
wlsxSysExtMemoryTable=_WlsxSysExtMemoryTable_Object((1,3,6,1,4,1,14823,2,2,1,2,1,15))
if mibBuilder.loadTexts:wlsxSysExtMemoryTable.setStatus(_A)
_WlsxSysExtMemoryEntry_Object=MibTableRow
wlsxSysExtMemoryEntry=_WlsxSysExtMemoryEntry_Object((1,3,6,1,4,1,14823,2,2,1,2,1,15,1))
wlsxSysExtMemoryEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:wlsxSysExtMemoryEntry.setStatus(_A)
_SysExtMemoryIndex_Type=Integer32
_SysExtMemoryIndex_Object=MibTableColumn
sysExtMemoryIndex=_SysExtMemoryIndex_Object((1,3,6,1,4,1,14823,2,2,1,2,1,15,1,1),_SysExtMemoryIndex_Type())
sysExtMemoryIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:sysExtMemoryIndex.setStatus(_A)
_SysExtMemorySize_Type=Integer32
_SysExtMemorySize_Object=MibTableColumn
sysExtMemorySize=_SysExtMemorySize_Object((1,3,6,1,4,1,14823,2,2,1,2,1,15,1,2),_SysExtMemorySize_Type())
sysExtMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtMemorySize.setStatus(_A)
_SysExtMemoryUsed_Type=Integer32
_SysExtMemoryUsed_Object=MibTableColumn
sysExtMemoryUsed=_SysExtMemoryUsed_Object((1,3,6,1,4,1,14823,2,2,1,2,1,15,1,3),_SysExtMemoryUsed_Type())
sysExtMemoryUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtMemoryUsed.setStatus(_A)
_SysExtMemoryFree_Type=Integer32
_SysExtMemoryFree_Object=MibTableColumn
sysExtMemoryFree=_SysExtMemoryFree_Object((1,3,6,1,4,1,14823,2,2,1,2,1,15,1,4),_SysExtMemoryFree_Type())
sysExtMemoryFree.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtMemoryFree.setStatus(_A)
_WlsxSysExtCardTable_Object=MibTable
wlsxSysExtCardTable=_WlsxSysExtCardTable_Object((1,3,6,1,4,1,14823,2,2,1,2,1,16))
if mibBuilder.loadTexts:wlsxSysExtCardTable.setStatus(_A)
_WlsxSysExtCardEntry_Object=MibTableRow
wlsxSysExtCardEntry=_WlsxSysExtCardEntry_Object((1,3,6,1,4,1,14823,2,2,1,2,1,16,1))
wlsxSysExtCardEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:wlsxSysExtCardEntry.setStatus(_A)
_SysExtCardSlot_Type=Integer32
_SysExtCardSlot_Object=MibTableColumn
sysExtCardSlot=_SysExtCardSlot_Object((1,3,6,1,4,1,14823,2,2,1,2,1,16,1,1),_SysExtCardSlot_Type())
sysExtCardSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:sysExtCardSlot.setStatus(_A)
_SysExtCardType_Type=ArubaCardType
_SysExtCardType_Object=MibTableColumn
sysExtCardType=_SysExtCardType_Object((1,3,6,1,4,1,14823,2,2,1,2,1,16,1,2),_SysExtCardType_Type())
sysExtCardType.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtCardType.setStatus(_A)
_SysExtCardNumOfPorts_Type=Integer32
_SysExtCardNumOfPorts_Object=MibTableColumn
sysExtCardNumOfPorts=_SysExtCardNumOfPorts_Object((1,3,6,1,4,1,14823,2,2,1,2,1,16,1,3),_SysExtCardNumOfPorts_Type())
sysExtCardNumOfPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtCardNumOfPorts.setStatus(_A)
_SysExtCardNumOfFastethernetPorts_Type=Integer32
_SysExtCardNumOfFastethernetPorts_Object=MibTableColumn
sysExtCardNumOfFastethernetPorts=_SysExtCardNumOfFastethernetPorts_Object((1,3,6,1,4,1,14823,2,2,1,2,1,16,1,4),_SysExtCardNumOfFastethernetPorts_Type())
sysExtCardNumOfFastethernetPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtCardNumOfFastethernetPorts.setStatus(_A)
_SysExtCardNumOfGigPorts_Type=Integer32
_SysExtCardNumOfGigPorts_Object=MibTableColumn
sysExtCardNumOfGigPorts=_SysExtCardNumOfGigPorts_Object((1,3,6,1,4,1,14823,2,2,1,2,1,16,1,5),_SysExtCardNumOfGigPorts_Type())
sysExtCardNumOfGigPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtCardNumOfGigPorts.setStatus(_A)
class _SysExtCardSerialNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SysExtCardSerialNo_Type.__name__=_C
_SysExtCardSerialNo_Object=MibTableColumn
sysExtCardSerialNo=_SysExtCardSerialNo_Object((1,3,6,1,4,1,14823,2,2,1,2,1,16,1,6),_SysExtCardSerialNo_Type())
sysExtCardSerialNo.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtCardSerialNo.setStatus(_A)
class _SysExtCardAssemblyNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SysExtCardAssemblyNo_Type.__name__=_C
_SysExtCardAssemblyNo_Object=MibTableColumn
sysExtCardAssemblyNo=_SysExtCardAssemblyNo_Object((1,3,6,1,4,1,14823,2,2,1,2,1,16,1,7),_SysExtCardAssemblyNo_Type())
sysExtCardAssemblyNo.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtCardAssemblyNo.setStatus(_A)
_SysExtCardManufacturingDate_Type=DisplayString
_SysExtCardManufacturingDate_Object=MibTableColumn
sysExtCardManufacturingDate=_SysExtCardManufacturingDate_Object((1,3,6,1,4,1,14823,2,2,1,2,1,16,1,8),_SysExtCardManufacturingDate_Type())
sysExtCardManufacturingDate.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtCardManufacturingDate.setStatus(_A)
class _SysExtCardHwRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SysExtCardHwRevision_Type.__name__=_C
_SysExtCardHwRevision_Object=MibTableColumn
sysExtCardHwRevision=_SysExtCardHwRevision_Object((1,3,6,1,4,1,14823,2,2,1,2,1,16,1,9),_SysExtCardHwRevision_Type())
sysExtCardHwRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtCardHwRevision.setStatus(_A)
class _SysExtCardFpgaRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SysExtCardFpgaRevision_Type.__name__=_C
_SysExtCardFpgaRevision_Object=MibTableColumn
sysExtCardFpgaRevision=_SysExtCardFpgaRevision_Object((1,3,6,1,4,1,14823,2,2,1,2,1,16,1,10),_SysExtCardFpgaRevision_Type())
sysExtCardFpgaRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtCardFpgaRevision.setStatus(_A)
class _SysExtCardSwitchChip_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SysExtCardSwitchChip_Type.__name__=_C
_SysExtCardSwitchChip_Object=MibTableColumn
sysExtCardSwitchChip=_SysExtCardSwitchChip_Object((1,3,6,1,4,1,14823,2,2,1,2,1,16,1,11),_SysExtCardSwitchChip_Type())
sysExtCardSwitchChip.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtCardSwitchChip.setStatus(_A)
_SysExtCardStatus_Type=ArubaActiveState
_SysExtCardStatus_Object=MibTableColumn
sysExtCardStatus=_SysExtCardStatus_Object((1,3,6,1,4,1,14823,2,2,1,2,1,16,1,12),_SysExtCardStatus_Type())
sysExtCardStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtCardStatus.setStatus(_A)
_SysExtCardUserSlot_Type=Integer32
_SysExtCardUserSlot_Object=MibTableColumn
sysExtCardUserSlot=_SysExtCardUserSlot_Object((1,3,6,1,4,1,14823,2,2,1,2,1,16,1,13),_SysExtCardUserSlot_Type())
sysExtCardUserSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtCardUserSlot.setStatus(_A)
class _SysExtCardServiceTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SysExtCardServiceTag_Type.__name__=_C
_SysExtCardServiceTag_Object=MibTableColumn
sysExtCardServiceTag=_SysExtCardServiceTag_Object((1,3,6,1,4,1,14823,2,2,1,2,1,16,1,14),_SysExtCardServiceTag_Type())
sysExtCardServiceTag.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtCardServiceTag.setStatus(_A)
class _SysExtCardPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SysExtCardPartNumber_Type.__name__=_C
_SysExtCardPartNumber_Object=MibTableColumn
sysExtCardPartNumber=_SysExtCardPartNumber_Object((1,3,6,1,4,1,14823,2,2,1,2,1,16,1,15),_SysExtCardPartNumber_Type())
sysExtCardPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtCardPartNumber.setStatus(_A)
_WlsxSysExtFanTable_Object=MibTable
wlsxSysExtFanTable=_WlsxSysExtFanTable_Object((1,3,6,1,4,1,14823,2,2,1,2,1,17))
if mibBuilder.loadTexts:wlsxSysExtFanTable.setStatus(_A)
_WlsxSysExtFanEntry_Object=MibTableRow
wlsxSysExtFanEntry=_WlsxSysExtFanEntry_Object((1,3,6,1,4,1,14823,2,2,1,2,1,17,1))
wlsxSysExtFanEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:wlsxSysExtFanEntry.setStatus(_A)
_SysExtFanIndex_Type=Integer32
_SysExtFanIndex_Object=MibTableColumn
sysExtFanIndex=_SysExtFanIndex_Object((1,3,6,1,4,1,14823,2,2,1,2,1,17,1,1),_SysExtFanIndex_Type())
sysExtFanIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:sysExtFanIndex.setStatus(_A)
_SysExtFanStatus_Type=ArubaActiveState
_SysExtFanStatus_Object=MibTableColumn
sysExtFanStatus=_SysExtFanStatus_Object((1,3,6,1,4,1,14823,2,2,1,2,1,17,1,2),_SysExtFanStatus_Type())
sysExtFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtFanStatus.setStatus(_A)
_WlsxSysExtPowerSupplyTable_Object=MibTable
wlsxSysExtPowerSupplyTable=_WlsxSysExtPowerSupplyTable_Object((1,3,6,1,4,1,14823,2,2,1,2,1,18))
if mibBuilder.loadTexts:wlsxSysExtPowerSupplyTable.setStatus(_A)
_WlsxSysExtPowerSupplyEntry_Object=MibTableRow
wlsxSysExtPowerSupplyEntry=_WlsxSysExtPowerSupplyEntry_Object((1,3,6,1,4,1,14823,2,2,1,2,1,18,1))
wlsxSysExtPowerSupplyEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:wlsxSysExtPowerSupplyEntry.setStatus(_A)
_SysExtPowerSupplyIndex_Type=Integer32
_SysExtPowerSupplyIndex_Object=MibTableColumn
sysExtPowerSupplyIndex=_SysExtPowerSupplyIndex_Object((1,3,6,1,4,1,14823,2,2,1,2,1,18,1,1),_SysExtPowerSupplyIndex_Type())
sysExtPowerSupplyIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:sysExtPowerSupplyIndex.setStatus(_A)
_SysExtPowerSupplyStatus_Type=ArubaActiveState
_SysExtPowerSupplyStatus_Object=MibTableColumn
sysExtPowerSupplyStatus=_SysExtPowerSupplyStatus_Object((1,3,6,1,4,1,14823,2,2,1,2,1,18,1,2),_SysExtPowerSupplyStatus_Type())
sysExtPowerSupplyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtPowerSupplyStatus.setStatus(_A)
_WlsxSysExtSwitchListTable_Object=MibTable
wlsxSysExtSwitchListTable=_WlsxSysExtSwitchListTable_Object((1,3,6,1,4,1,14823,2,2,1,2,1,19))
if mibBuilder.loadTexts:wlsxSysExtSwitchListTable.setStatus(_A)
_WlsxSysExtSwitchListEntry_Object=MibTableRow
wlsxSysExtSwitchListEntry=_WlsxSysExtSwitchListEntry_Object((1,3,6,1,4,1,14823,2,2,1,2,1,19,1))
wlsxSysExtSwitchListEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:wlsxSysExtSwitchListEntry.setStatus(_A)
_SysExtSwitchIPAddress_Type=IpAddress
_SysExtSwitchIPAddress_Object=MibTableColumn
sysExtSwitchIPAddress=_SysExtSwitchIPAddress_Object((1,3,6,1,4,1,14823,2,2,1,2,1,19,1,1),_SysExtSwitchIPAddress_Type())
sysExtSwitchIPAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:sysExtSwitchIPAddress.setStatus(_A)
_SysExtSwitchRole_Type=ArubaSwitchRole
_SysExtSwitchRole_Object=MibTableColumn
sysExtSwitchRole=_SysExtSwitchRole_Object((1,3,6,1,4,1,14823,2,2,1,2,1,19,1,2),_SysExtSwitchRole_Type())
sysExtSwitchRole.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtSwitchRole.setStatus(_A)
class _SysExtSwitchLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SysExtSwitchLocation_Type.__name__=_C
_SysExtSwitchLocation_Object=MibTableColumn
sysExtSwitchLocation=_SysExtSwitchLocation_Object((1,3,6,1,4,1,14823,2,2,1,2,1,19,1,3),_SysExtSwitchLocation_Type())
sysExtSwitchLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtSwitchLocation.setStatus(_A)
class _SysExtSwitchSWVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SysExtSwitchSWVersion_Type.__name__=_C
_SysExtSwitchSWVersion_Object=MibTableColumn
sysExtSwitchSWVersion=_SysExtSwitchSWVersion_Object((1,3,6,1,4,1,14823,2,2,1,2,1,19,1,4),_SysExtSwitchSWVersion_Type())
sysExtSwitchSWVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtSwitchSWVersion.setStatus(_A)
_SysExtSwitchStatus_Type=ArubaActiveState
_SysExtSwitchStatus_Object=MibTableColumn
sysExtSwitchStatus=_SysExtSwitchStatus_Object((1,3,6,1,4,1,14823,2,2,1,2,1,19,1,5),_SysExtSwitchStatus_Type())
sysExtSwitchStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtSwitchStatus.setStatus(_A)
class _SysExtSwitchName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SysExtSwitchName_Type.__name__=_C
_SysExtSwitchName_Object=MibTableColumn
sysExtSwitchName=_SysExtSwitchName_Object((1,3,6,1,4,1,14823,2,2,1,2,1,19,1,6),_SysExtSwitchName_Type())
sysExtSwitchName.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtSwitchName.setStatus(_A)
class _SysExtSwitchSerNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SysExtSwitchSerNo_Type.__name__=_C
_SysExtSwitchSerNo_Object=MibTableColumn
sysExtSwitchSerNo=_SysExtSwitchSerNo_Object((1,3,6,1,4,1,14823,2,2,1,2,1,19,1,7),_SysExtSwitchSerNo_Type())
sysExtSwitchSerNo.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtSwitchSerNo.setStatus(_A)
_WlsxSysExtSwitchLicenseTable_Object=MibTable
wlsxSysExtSwitchLicenseTable=_WlsxSysExtSwitchLicenseTable_Object((1,3,6,1,4,1,14823,2,2,1,2,1,20))
if mibBuilder.loadTexts:wlsxSysExtSwitchLicenseTable.setStatus(_A)
_WlsxSysExtLicenseEntry_Object=MibTableRow
wlsxSysExtLicenseEntry=_WlsxSysExtLicenseEntry_Object((1,3,6,1,4,1,14823,2,2,1,2,1,20,1))
wlsxSysExtLicenseEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:wlsxSysExtLicenseEntry.setStatus(_A)
_SysExtLicenseIndex_Type=Integer32
_SysExtLicenseIndex_Object=MibTableColumn
sysExtLicenseIndex=_SysExtLicenseIndex_Object((1,3,6,1,4,1,14823,2,2,1,2,1,20,1,1),_SysExtLicenseIndex_Type())
sysExtLicenseIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:sysExtLicenseIndex.setStatus(_A)
_SysExtLicenseKey_Type=DisplayString
_SysExtLicenseKey_Object=MibTableColumn
sysExtLicenseKey=_SysExtLicenseKey_Object((1,3,6,1,4,1,14823,2,2,1,2,1,20,1,2),_SysExtLicenseKey_Type())
sysExtLicenseKey.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtLicenseKey.setStatus(_A)
_SysExtLicenseInstalled_Type=DisplayString
_SysExtLicenseInstalled_Object=MibTableColumn
sysExtLicenseInstalled=_SysExtLicenseInstalled_Object((1,3,6,1,4,1,14823,2,2,1,2,1,20,1,3),_SysExtLicenseInstalled_Type())
sysExtLicenseInstalled.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtLicenseInstalled.setStatus(_A)
_SysExtLicenseExpires_Type=DisplayString
_SysExtLicenseExpires_Object=MibTableColumn
sysExtLicenseExpires=_SysExtLicenseExpires_Object((1,3,6,1,4,1,14823,2,2,1,2,1,20,1,4),_SysExtLicenseExpires_Type())
sysExtLicenseExpires.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtLicenseExpires.setStatus(_A)
_SysExtLicenseFlags_Type=DisplayString
_SysExtLicenseFlags_Object=MibTableColumn
sysExtLicenseFlags=_SysExtLicenseFlags_Object((1,3,6,1,4,1,14823,2,2,1,2,1,20,1,5),_SysExtLicenseFlags_Type())
sysExtLicenseFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtLicenseFlags.setStatus(_A)
_SysExtLicenseService_Type=DisplayString
_SysExtLicenseService_Object=MibTableColumn
sysExtLicenseService=_SysExtLicenseService_Object((1,3,6,1,4,1,14823,2,2,1,2,1,20,1,6),_SysExtLicenseService_Type())
sysExtLicenseService.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtLicenseService.setStatus(_A)
_WlsxSysExtMMSCompatLevel_Type=Integer32
_WlsxSysExtMMSCompatLevel_Object=MibScalar
wlsxSysExtMMSCompatLevel=_WlsxSysExtMMSCompatLevel_Object((1,3,6,1,4,1,14823,2,2,1,2,1,21),_WlsxSysExtMMSCompatLevel_Type())
wlsxSysExtMMSCompatLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtMMSCompatLevel.setStatus(_A)
_WlsxSysExtMMSConfigID_Type=Integer32
_WlsxSysExtMMSConfigID_Object=MibScalar
wlsxSysExtMMSConfigID=_WlsxSysExtMMSConfigID_Object((1,3,6,1,4,1,14823,2,2,1,2,1,22),_WlsxSysExtMMSConfigID_Type())
wlsxSysExtMMSConfigID.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtMMSConfigID.setStatus(_A)
_WlsxSysExtControllerConfigID_Type=Integer32
_WlsxSysExtControllerConfigID_Object=MibScalar
wlsxSysExtControllerConfigID=_WlsxSysExtControllerConfigID_Object((1,3,6,1,4,1,14823,2,2,1,2,1,23),_WlsxSysExtControllerConfigID_Type())
wlsxSysExtControllerConfigID.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtControllerConfigID.setStatus(_A)
_WlsxSysExtIsMMSConfigUpdateEnabled_Type=TruthValue
_WlsxSysExtIsMMSConfigUpdateEnabled_Object=MibScalar
wlsxSysExtIsMMSConfigUpdateEnabled=_WlsxSysExtIsMMSConfigUpdateEnabled_Object((1,3,6,1,4,1,14823,2,2,1,2,1,24),_WlsxSysExtIsMMSConfigUpdateEnabled_Type())
wlsxSysExtIsMMSConfigUpdateEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:wlsxSysExtIsMMSConfigUpdateEnabled.setStatus(_A)
class _WlsxSysExtSwitchLastReload_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_WlsxSysExtSwitchLastReload_Type.__name__=_C
_WlsxSysExtSwitchLastReload_Object=MibScalar
wlsxSysExtSwitchLastReload=_WlsxSysExtSwitchLastReload_Object((1,3,6,1,4,1,14823,2,2,1,2,1,25),_WlsxSysExtSwitchLastReload_Type())
wlsxSysExtSwitchLastReload.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtSwitchLastReload.setStatus(_A)
_WlsxSysExtLastStatsReset_Type=TimeTicks
_WlsxSysExtLastStatsReset_Object=MibScalar
wlsxSysExtLastStatsReset=_WlsxSysExtLastStatsReset_Object((1,3,6,1,4,1,14823,2,2,1,2,1,26),_WlsxSysExtLastStatsReset_Type())
wlsxSysExtLastStatsReset.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtLastStatsReset.setStatus(_A)
class _WlsxSysExtHwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_WlsxSysExtHwVersion_Type.__name__=_C
_WlsxSysExtHwVersion_Object=MibScalar
wlsxSysExtHwVersion=_WlsxSysExtHwVersion_Object((1,3,6,1,4,1,14823,2,2,1,2,1,27),_WlsxSysExtHwVersion_Type())
wlsxSysExtHwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtHwVersion.setStatus(_A)
class _WlsxSysExtSwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_WlsxSysExtSwVersion_Type.__name__=_C
_WlsxSysExtSwVersion_Object=MibScalar
wlsxSysExtSwVersion=_WlsxSysExtSwVersion_Object((1,3,6,1,4,1,14823,2,2,1,2,1,28),_WlsxSysExtSwVersion_Type())
wlsxSysExtSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtSwVersion.setStatus(_A)
class _WlsxSysExtSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_WlsxSysExtSerialNumber_Type.__name__=_C
_WlsxSysExtSerialNumber_Object=MibScalar
wlsxSysExtSerialNumber=_WlsxSysExtSerialNumber_Object((1,3,6,1,4,1,14823,2,2,1,2,1,29),_WlsxSysExtSerialNumber_Type())
wlsxSysExtSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtSerialNumber.setStatus(_A)
_WlsxSysExtCpuUsedPercent_Type=Gauge32
_WlsxSysExtCpuUsedPercent_Object=MibScalar
wlsxSysExtCpuUsedPercent=_WlsxSysExtCpuUsedPercent_Object((1,3,6,1,4,1,14823,2,2,1,2,1,30),_WlsxSysExtCpuUsedPercent_Type())
wlsxSysExtCpuUsedPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtCpuUsedPercent.setStatus(_A)
_WlsxSysExtMemoryUsedPercent_Type=Gauge32
_WlsxSysExtMemoryUsedPercent_Object=MibScalar
wlsxSysExtMemoryUsedPercent=_WlsxSysExtMemoryUsedPercent_Object((1,3,6,1,4,1,14823,2,2,1,2,1,31),_WlsxSysExtMemoryUsedPercent_Type())
wlsxSysExtMemoryUsedPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtMemoryUsedPercent.setStatus(_A)
_WlsxSysExtPacketLossPercent_Type=Integer32
_WlsxSysExtPacketLossPercent_Object=MibScalar
wlsxSysExtPacketLossPercent=_WlsxSysExtPacketLossPercent_Object((1,3,6,1,4,1,14823,2,2,1,2,1,32),_WlsxSysExtPacketLossPercent_Type())
wlsxSysExtPacketLossPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtPacketLossPercent.setStatus(_A)
_WlsxSysExtPoweredViaPoe_Type=Integer32
_WlsxSysExtPoweredViaPoe_Object=MibScalar
wlsxSysExtPoweredViaPoe=_WlsxSysExtPoweredViaPoe_Object((1,3,6,1,4,1,14823,2,2,1,2,1,33),_WlsxSysExtPoweredViaPoe_Type())
wlsxSysExtPoweredViaPoe.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtPoweredViaPoe.setStatus(_A)
class _WlsxSysVMHostType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_WlsxSysVMHostType_Type.__name__=_C
_WlsxSysVMHostType_Object=MibScalar
wlsxSysVMHostType=_WlsxSysVMHostType_Object((1,3,6,1,4,1,14823,2,2,1,2,1,34),_WlsxSysVMHostType_Type())
wlsxSysVMHostType.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysVMHostType.setStatus(_A)
class _WlsxSysExtProcessorModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_WlsxSysExtProcessorModel_Type.__name__=_C
_WlsxSysExtProcessorModel_Object=MibScalar
wlsxSysExtProcessorModel=_WlsxSysExtProcessorModel_Object((1,3,6,1,4,1,14823,2,2,1,2,1,35),_WlsxSysExtProcessorModel_Type())
wlsxSysExtProcessorModel.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtProcessorModel.setStatus(_A)
_WlsxSysExtTotalCpu_Type=Integer32
_WlsxSysExtTotalCpu_Object=MibScalar
wlsxSysExtTotalCpu=_WlsxSysExtTotalCpu_Object((1,3,6,1,4,1,14823,2,2,1,2,1,36),_WlsxSysExtTotalCpu_Type())
wlsxSysExtTotalCpu.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtTotalCpu.setStatus(_A)
_WlsxSysExtTotalSocket_Type=Integer32
_WlsxSysExtTotalSocket_Object=MibScalar
wlsxSysExtTotalSocket=_WlsxSysExtTotalSocket_Object((1,3,6,1,4,1,14823,2,2,1,2,1,37),_WlsxSysExtTotalSocket_Type())
wlsxSysExtTotalSocket.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtTotalSocket.setStatus(_A)
_WlsxAuthFailIp_Type=IpAddress
_WlsxAuthFailIp_Object=MibScalar
wlsxAuthFailIp=_WlsxAuthFailIp_Object((1,3,6,1,4,1,14823,2,2,1,2,1,38),_WlsxAuthFailIp_Type())
wlsxAuthFailIp.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxAuthFailIp.setStatus(_A)
_WlsxSysExtDiskSize_Type=Integer32
_WlsxSysExtDiskSize_Object=MibScalar
wlsxSysExtDiskSize=_WlsxSysExtDiskSize_Object((1,3,6,1,4,1,14823,2,2,1,2,1,39),_WlsxSysExtDiskSize_Type())
wlsxSysExtDiskSize.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtDiskSize.setStatus(_A)
_WlsxNSysExtSwitchListTable_Object=MibTable
wlsxNSysExtSwitchListTable=_WlsxNSysExtSwitchListTable_Object((1,3,6,1,4,1,14823,2,2,1,2,1,40))
if mibBuilder.loadTexts:wlsxNSysExtSwitchListTable.setStatus(_A)
_WlsxNSysExtSwitchListEntry_Object=MibTableRow
wlsxNSysExtSwitchListEntry=_WlsxNSysExtSwitchListEntry_Object((1,3,6,1,4,1,14823,2,2,1,2,1,40,1))
wlsxNSysExtSwitchListEntry.setIndexNames((0,_D,_Q),(0,_D,_R))
if mibBuilder.loadTexts:wlsxNSysExtSwitchListEntry.setStatus(_A)
_SysExtNSwitchIPAddressType_Type=Integer32
_SysExtNSwitchIPAddressType_Object=MibTableColumn
sysExtNSwitchIPAddressType=_SysExtNSwitchIPAddressType_Object((1,3,6,1,4,1,14823,2,2,1,2,1,40,1,1),_SysExtNSwitchIPAddressType_Type())
sysExtNSwitchIPAddressType.setMaxAccess(_F)
if mibBuilder.loadTexts:sysExtNSwitchIPAddressType.setStatus(_A)
class _SysExtNSwitchIPAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,45))
_SysExtNSwitchIPAddress_Type.__name__=_C
_SysExtNSwitchIPAddress_Object=MibTableColumn
sysExtNSwitchIPAddress=_SysExtNSwitchIPAddress_Object((1,3,6,1,4,1,14823,2,2,1,2,1,40,1,2),_SysExtNSwitchIPAddress_Type())
sysExtNSwitchIPAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:sysExtNSwitchIPAddress.setStatus(_A)
_SysExtNSwitchRole_Type=ArubaSwitchRole
_SysExtNSwitchRole_Object=MibTableColumn
sysExtNSwitchRole=_SysExtNSwitchRole_Object((1,3,6,1,4,1,14823,2,2,1,2,1,40,1,3),_SysExtNSwitchRole_Type())
sysExtNSwitchRole.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtNSwitchRole.setStatus(_A)
class _SysExtNSwitchLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SysExtNSwitchLocation_Type.__name__=_C
_SysExtNSwitchLocation_Object=MibTableColumn
sysExtNSwitchLocation=_SysExtNSwitchLocation_Object((1,3,6,1,4,1,14823,2,2,1,2,1,40,1,4),_SysExtNSwitchLocation_Type())
sysExtNSwitchLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtNSwitchLocation.setStatus(_A)
class _SysExtNSwitchSWVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SysExtNSwitchSWVersion_Type.__name__=_C
_SysExtNSwitchSWVersion_Object=MibTableColumn
sysExtNSwitchSWVersion=_SysExtNSwitchSWVersion_Object((1,3,6,1,4,1,14823,2,2,1,2,1,40,1,5),_SysExtNSwitchSWVersion_Type())
sysExtNSwitchSWVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtNSwitchSWVersion.setStatus(_A)
_SysExtNSwitchStatus_Type=ArubaActiveState
_SysExtNSwitchStatus_Object=MibTableColumn
sysExtNSwitchStatus=_SysExtNSwitchStatus_Object((1,3,6,1,4,1,14823,2,2,1,2,1,40,1,6),_SysExtNSwitchStatus_Type())
sysExtNSwitchStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtNSwitchStatus.setStatus(_A)
class _SysExtNSwitchName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SysExtNSwitchName_Type.__name__=_C
_SysExtNSwitchName_Object=MibTableColumn
sysExtNSwitchName=_SysExtNSwitchName_Object((1,3,6,1,4,1,14823,2,2,1,2,1,40,1,7),_SysExtNSwitchName_Type())
sysExtNSwitchName.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtNSwitchName.setStatus(_A)
class _SysExtNSwitchSerNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SysExtNSwitchSerNo_Type.__name__=_C
_SysExtNSwitchSerNo_Object=MibTableColumn
sysExtNSwitchSerNo=_SysExtNSwitchSerNo_Object((1,3,6,1,4,1,14823,2,2,1,2,1,40,1,8),_SysExtNSwitchSerNo_Type())
sysExtNSwitchSerNo.setMaxAccess(_B)
if mibBuilder.loadTexts:sysExtNSwitchSerNo.setStatus(_A)
_WlsxSysExtSwitchConductorIp_Type=IpAddress
_WlsxSysExtSwitchConductorIp_Object=MibScalar
wlsxSysExtSwitchConductorIp=_WlsxSysExtSwitchConductorIp_Object((1,3,6,1,4,1,14823,2,2,1,2,1,41),_WlsxSysExtSwitchConductorIp_Type())
wlsxSysExtSwitchConductorIp.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtSwitchConductorIp.setStatus(_A)
_WlsxSystemExtTableGenNumberGroup_ObjectIdentity=ObjectIdentity
wlsxSystemExtTableGenNumberGroup=_WlsxSystemExtTableGenNumberGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,2,2))
_WlsxSysExtUserTableGenNumber_Type=Integer32
_WlsxSysExtUserTableGenNumber_Object=MibScalar
wlsxSysExtUserTableGenNumber=_WlsxSysExtUserTableGenNumber_Object((1,3,6,1,4,1,14823,2,2,1,2,2,1),_WlsxSysExtUserTableGenNumber_Type())
wlsxSysExtUserTableGenNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtUserTableGenNumber.setStatus(_E)
_WlsxSysExtAPBssidTableGenNumber_Type=Integer32
_WlsxSysExtAPBssidTableGenNumber_Object=MibScalar
wlsxSysExtAPBssidTableGenNumber=_WlsxSysExtAPBssidTableGenNumber_Object((1,3,6,1,4,1,14823,2,2,1,2,2,2),_WlsxSysExtAPBssidTableGenNumber_Type())
wlsxSysExtAPBssidTableGenNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtAPBssidTableGenNumber.setStatus(_E)
_WlsxSysExtAPRadioTableGenNumber_Type=Integer32
_WlsxSysExtAPRadioTableGenNumber_Object=MibScalar
wlsxSysExtAPRadioTableGenNumber=_WlsxSysExtAPRadioTableGenNumber_Object((1,3,6,1,4,1,14823,2,2,1,2,2,3),_WlsxSysExtAPRadioTableGenNumber_Type())
wlsxSysExtAPRadioTableGenNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtAPRadioTableGenNumber.setStatus(_E)
_WlsxSysExtAPTableGenNumber_Type=Integer32
_WlsxSysExtAPTableGenNumber_Object=MibScalar
wlsxSysExtAPTableGenNumber=_WlsxSysExtAPTableGenNumber_Object((1,3,6,1,4,1,14823,2,2,1,2,2,4),_WlsxSysExtAPTableGenNumber_Type())
wlsxSysExtAPTableGenNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtAPTableGenNumber.setStatus(_E)
_WlsxSysExtSwitchListTableGenNumber_Type=Integer32
_WlsxSysExtSwitchListTableGenNumber_Object=MibScalar
wlsxSysExtSwitchListTableGenNumber=_WlsxSysExtSwitchListTableGenNumber_Object((1,3,6,1,4,1,14823,2,2,1,2,2,5),_WlsxSysExtSwitchListTableGenNumber_Type())
wlsxSysExtSwitchListTableGenNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtSwitchListTableGenNumber.setStatus(_E)
_WlsxSysExtPortTableGenNumber_Type=Integer32
_WlsxSysExtPortTableGenNumber_Object=MibScalar
wlsxSysExtPortTableGenNumber=_WlsxSysExtPortTableGenNumber_Object((1,3,6,1,4,1,14823,2,2,1,2,2,6),_WlsxSysExtPortTableGenNumber_Type())
wlsxSysExtPortTableGenNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtPortTableGenNumber.setStatus(_E)
_WlsxSysExtVlanTableGenNumber_Type=Integer32
_WlsxSysExtVlanTableGenNumber_Object=MibScalar
wlsxSysExtVlanTableGenNumber=_WlsxSysExtVlanTableGenNumber_Object((1,3,6,1,4,1,14823,2,2,1,2,2,7),_WlsxSysExtVlanTableGenNumber_Type())
wlsxSysExtVlanTableGenNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtVlanTableGenNumber.setStatus(_E)
_WlsxSysExtVlanInterfaceTableGenNumber_Type=Integer32
_WlsxSysExtVlanInterfaceTableGenNumber_Object=MibScalar
wlsxSysExtVlanInterfaceTableGenNumber=_WlsxSysExtVlanInterfaceTableGenNumber_Object((1,3,6,1,4,1,14823,2,2,1,2,2,8),_WlsxSysExtVlanInterfaceTableGenNumber_Type())
wlsxSysExtVlanInterfaceTableGenNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtVlanInterfaceTableGenNumber.setStatus(_E)
_WlsxSysExtLicenseTableGenNumber_Type=Integer32
_WlsxSysExtLicenseTableGenNumber_Object=MibScalar
wlsxSysExtLicenseTableGenNumber=_WlsxSysExtLicenseTableGenNumber_Object((1,3,6,1,4,1,14823,2,2,1,2,2,9),_WlsxSysExtLicenseTableGenNumber_Type())
wlsxSysExtLicenseTableGenNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtLicenseTableGenNumber.setStatus(_E)
_WlsxSysExtMonAPTableGenNumber_Type=Integer32
_WlsxSysExtMonAPTableGenNumber_Object=MibScalar
wlsxSysExtMonAPTableGenNumber=_WlsxSysExtMonAPTableGenNumber_Object((1,3,6,1,4,1,14823,2,2,1,2,2,10),_WlsxSysExtMonAPTableGenNumber_Type())
wlsxSysExtMonAPTableGenNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtMonAPTableGenNumber.setStatus(_E)
_WlsxSysExtMonStationTableGenNumber_Type=Integer32
_WlsxSysExtMonStationTableGenNumber_Object=MibScalar
wlsxSysExtMonStationTableGenNumber=_WlsxSysExtMonStationTableGenNumber_Object((1,3,6,1,4,1,14823,2,2,1,2,2,11),_WlsxSysExtMonStationTableGenNumber_Type())
wlsxSysExtMonStationTableGenNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxSysExtMonStationTableGenNumber.setStatus(_E)
mibBuilder.exportSymbols(_D,**{'wlsxSystemExtMIB':wlsxSystemExtMIB,'wlsxSystemExtGroup':wlsxSystemExtGroup,'wlsxSysExtSwitchIp':wlsxSysExtSwitchIp,'wlsxSysExtHostname':wlsxSysExtHostname,'wlsxSysExtModelName':wlsxSysExtModelName,'wlsxSysExtSwitchRole':wlsxSysExtSwitchRole,'wlsxSysExtSwitchMasterIp':wlsxSysExtSwitchMasterIp,'wlsxSysExtSwitchDate':wlsxSysExtSwitchDate,'wlsxSysExtSwitchBaseMacaddress':wlsxSysExtSwitchBaseMacaddress,'wlsxSysExtFanTrayAssemblyNumber':wlsxSysExtFanTrayAssemblyNumber,'wlsxSysExtFanTraySerialNumber':wlsxSysExtFanTraySerialNumber,'wlsxSysExtInternalTemparature':wlsxSysExtInternalTemparature,'wlsxSysExtLicenseSerialNumber':wlsxSysExtLicenseSerialNumber,'wlsxSysExtSwitchLicenseCount':wlsxSysExtSwitchLicenseCount,'wlsxSysExtProcessorTable':wlsxSysExtProcessorTable,'wlsxSysExtProcessorEntry':wlsxSysExtProcessorEntry,_I:sysExtProcessorID,'sysExtProcessorDescr':sysExtProcessorDescr,'sysExtProcessorLoad':sysExtProcessorLoad,'wlsxSysExtStorageTable':wlsxSysExtStorageTable,'wlsxSysExtStorageEntry':wlsxSysExtStorageEntry,_J:sysExtStorageIndex,'sysExtStorageType':sysExtStorageType,'sysExtStorageSize':sysExtStorageSize,'sysExtStorageUsed':sysExtStorageUsed,'sysExtStorageName':sysExtStorageName,'wlsxSysExtMemoryTable':wlsxSysExtMemoryTable,'wlsxSysExtMemoryEntry':wlsxSysExtMemoryEntry,_K:sysExtMemoryIndex,'sysExtMemorySize':sysExtMemorySize,'sysExtMemoryUsed':sysExtMemoryUsed,'sysExtMemoryFree':sysExtMemoryFree,'wlsxSysExtCardTable':wlsxSysExtCardTable,'wlsxSysExtCardEntry':wlsxSysExtCardEntry,_L:sysExtCardSlot,'sysExtCardType':sysExtCardType,'sysExtCardNumOfPorts':sysExtCardNumOfPorts,'sysExtCardNumOfFastethernetPorts':sysExtCardNumOfFastethernetPorts,'sysExtCardNumOfGigPorts':sysExtCardNumOfGigPorts,'sysExtCardSerialNo':sysExtCardSerialNo,'sysExtCardAssemblyNo':sysExtCardAssemblyNo,'sysExtCardManufacturingDate':sysExtCardManufacturingDate,'sysExtCardHwRevision':sysExtCardHwRevision,'sysExtCardFpgaRevision':sysExtCardFpgaRevision,'sysExtCardSwitchChip':sysExtCardSwitchChip,'sysExtCardStatus':sysExtCardStatus,'sysExtCardUserSlot':sysExtCardUserSlot,'sysExtCardServiceTag':sysExtCardServiceTag,'sysExtCardPartNumber':sysExtCardPartNumber,'wlsxSysExtFanTable':wlsxSysExtFanTable,'wlsxSysExtFanEntry':wlsxSysExtFanEntry,_M:sysExtFanIndex,'sysExtFanStatus':sysExtFanStatus,'wlsxSysExtPowerSupplyTable':wlsxSysExtPowerSupplyTable,'wlsxSysExtPowerSupplyEntry':wlsxSysExtPowerSupplyEntry,_N:sysExtPowerSupplyIndex,'sysExtPowerSupplyStatus':sysExtPowerSupplyStatus,'wlsxSysExtSwitchListTable':wlsxSysExtSwitchListTable,'wlsxSysExtSwitchListEntry':wlsxSysExtSwitchListEntry,_O:sysExtSwitchIPAddress,'sysExtSwitchRole':sysExtSwitchRole,'sysExtSwitchLocation':sysExtSwitchLocation,'sysExtSwitchSWVersion':sysExtSwitchSWVersion,'sysExtSwitchStatus':sysExtSwitchStatus,'sysExtSwitchName':sysExtSwitchName,'sysExtSwitchSerNo':sysExtSwitchSerNo,'wlsxSysExtSwitchLicenseTable':wlsxSysExtSwitchLicenseTable,'wlsxSysExtLicenseEntry':wlsxSysExtLicenseEntry,_P:sysExtLicenseIndex,'sysExtLicenseKey':sysExtLicenseKey,'sysExtLicenseInstalled':sysExtLicenseInstalled,'sysExtLicenseExpires':sysExtLicenseExpires,'sysExtLicenseFlags':sysExtLicenseFlags,'sysExtLicenseService':sysExtLicenseService,'wlsxSysExtMMSCompatLevel':wlsxSysExtMMSCompatLevel,'wlsxSysExtMMSConfigID':wlsxSysExtMMSConfigID,'wlsxSysExtControllerConfigID':wlsxSysExtControllerConfigID,'wlsxSysExtIsMMSConfigUpdateEnabled':wlsxSysExtIsMMSConfigUpdateEnabled,'wlsxSysExtSwitchLastReload':wlsxSysExtSwitchLastReload,'wlsxSysExtLastStatsReset':wlsxSysExtLastStatsReset,'wlsxSysExtHwVersion':wlsxSysExtHwVersion,'wlsxSysExtSwVersion':wlsxSysExtSwVersion,'wlsxSysExtSerialNumber':wlsxSysExtSerialNumber,'wlsxSysExtCpuUsedPercent':wlsxSysExtCpuUsedPercent,'wlsxSysExtMemoryUsedPercent':wlsxSysExtMemoryUsedPercent,'wlsxSysExtPacketLossPercent':wlsxSysExtPacketLossPercent,'wlsxSysExtPoweredViaPoe':wlsxSysExtPoweredViaPoe,'wlsxSysVMHostType':wlsxSysVMHostType,'wlsxSysExtProcessorModel':wlsxSysExtProcessorModel,'wlsxSysExtTotalCpu':wlsxSysExtTotalCpu,'wlsxSysExtTotalSocket':wlsxSysExtTotalSocket,'wlsxAuthFailIp':wlsxAuthFailIp,'wlsxSysExtDiskSize':wlsxSysExtDiskSize,'wlsxNSysExtSwitchListTable':wlsxNSysExtSwitchListTable,'wlsxNSysExtSwitchListEntry':wlsxNSysExtSwitchListEntry,_Q:sysExtNSwitchIPAddressType,_R:sysExtNSwitchIPAddress,'sysExtNSwitchRole':sysExtNSwitchRole,'sysExtNSwitchLocation':sysExtNSwitchLocation,'sysExtNSwitchSWVersion':sysExtNSwitchSWVersion,'sysExtNSwitchStatus':sysExtNSwitchStatus,'sysExtNSwitchName':sysExtNSwitchName,'sysExtNSwitchSerNo':sysExtNSwitchSerNo,'wlsxSysExtSwitchConductorIp':wlsxSysExtSwitchConductorIp,'wlsxSystemExtTableGenNumberGroup':wlsxSystemExtTableGenNumberGroup,'wlsxSysExtUserTableGenNumber':wlsxSysExtUserTableGenNumber,'wlsxSysExtAPBssidTableGenNumber':wlsxSysExtAPBssidTableGenNumber,'wlsxSysExtAPRadioTableGenNumber':wlsxSysExtAPRadioTableGenNumber,'wlsxSysExtAPTableGenNumber':wlsxSysExtAPTableGenNumber,'wlsxSysExtSwitchListTableGenNumber':wlsxSysExtSwitchListTableGenNumber,'wlsxSysExtPortTableGenNumber':wlsxSysExtPortTableGenNumber,'wlsxSysExtVlanTableGenNumber':wlsxSysExtVlanTableGenNumber,'wlsxSysExtVlanInterfaceTableGenNumber':wlsxSysExtVlanInterfaceTableGenNumber,'wlsxSysExtLicenseTableGenNumber':wlsxSysExtLicenseTableGenNumber,'wlsxSysExtMonAPTableGenNumber':wlsxSysExtMonAPTableGenNumber,'wlsxSysExtMonStationTableGenNumber':wlsxSysExtMonStationTableGenNumber})