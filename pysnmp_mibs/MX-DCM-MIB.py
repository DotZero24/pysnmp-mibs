_H='activeFeatureID'
_G='hardwareExtInfoIndex'
_F='MxEnableState'
_E='read-write'
_D='MX-DCM-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap',_F,'MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort','MxIpHostNamePort','MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dcmMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2000))
_DcmMIBObjects_ObjectIdentity=ObjectIdentity
dcmMIBObjects=_DcmMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2000,1))
_UnitInfoGroup_ObjectIdentity=ObjectIdentity
unitInfoGroup=_UnitInfoGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,100))
_UnitInfoProductName_Type=OctetString
_UnitInfoProductName_Object=MibScalar
unitInfoProductName=_UnitInfoProductName_Object((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,100,100),_UnitInfoProductName_Type())
unitInfoProductName.setMaxAccess(_B)
if mibBuilder.loadTexts:unitInfoProductName.setStatus(_A)
_UnitInfoSerialNumber_Type=OctetString
_UnitInfoSerialNumber_Object=MibScalar
unitInfoSerialNumber=_UnitInfoSerialNumber_Object((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,100,200),_UnitInfoSerialNumber_Type())
unitInfoSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:unitInfoSerialNumber.setStatus(_A)
_UnitInfoMacAddress_Type=OctetString
_UnitInfoMacAddress_Object=MibScalar
unitInfoMacAddress=_UnitInfoMacAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,100,300),_UnitInfoMacAddress_Type())
unitInfoMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:unitInfoMacAddress.setStatus(_A)
_UnitInfoHardwareRevision_Type=OctetString
_UnitInfoHardwareRevision_Object=MibScalar
unitInfoHardwareRevision=_UnitInfoHardwareRevision_Object((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,100,400),_UnitInfoHardwareRevision_Type())
unitInfoHardwareRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:unitInfoHardwareRevision.setStatus(_A)
_TotalNumberOfDsp_Type=Unsigned32
_TotalNumberOfDsp_Object=MibScalar
totalNumberOfDsp=_TotalNumberOfDsp_Object((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,100,500),_TotalNumberOfDsp_Type())
totalNumberOfDsp.setMaxAccess(_B)
if mibBuilder.loadTexts:totalNumberOfDsp.setStatus(_A)
_HwExtInfoGroup_ObjectIdentity=ObjectIdentity
hwExtInfoGroup=_HwExtInfoGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,300))
_HardwareExtInfoTable_Object=MibTable
hardwareExtInfoTable=_HardwareExtInfoTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,300,100))
if mibBuilder.loadTexts:hardwareExtInfoTable.setStatus(_A)
_HardwareExtInfoEntry_Object=MibTableRow
hardwareExtInfoEntry=_HardwareExtInfoEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,300,100,1))
hardwareExtInfoEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:hardwareExtInfoEntry.setStatus(_A)
_HardwareExtInfoIndex_Type=Unsigned32
_HardwareExtInfoIndex_Object=MibTableColumn
hardwareExtInfoIndex=_HardwareExtInfoIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,300,100,1,100),_HardwareExtInfoIndex_Type())
hardwareExtInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hardwareExtInfoIndex.setStatus(_A)
_HardwareExtInfoProductName_Type=OctetString
_HardwareExtInfoProductName_Object=MibTableColumn
hardwareExtInfoProductName=_HardwareExtInfoProductName_Object((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,300,100,1,200),_HardwareExtInfoProductName_Type())
hardwareExtInfoProductName.setMaxAccess(_B)
if mibBuilder.loadTexts:hardwareExtInfoProductName.setStatus(_A)
_HardwareExtInfoSerialNumber_Type=OctetString
_HardwareExtInfoSerialNumber_Object=MibTableColumn
hardwareExtInfoSerialNumber=_HardwareExtInfoSerialNumber_Object((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,300,100,1,300),_HardwareExtInfoSerialNumber_Type())
hardwareExtInfoSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hardwareExtInfoSerialNumber.setStatus(_A)
_HardwareExtInfoLocation_Type=OctetString
_HardwareExtInfoLocation_Object=MibTableColumn
hardwareExtInfoLocation=_HardwareExtInfoLocation_Object((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,300,100,1,400),_HardwareExtInfoLocation_Type())
hardwareExtInfoLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:hardwareExtInfoLocation.setStatus(_A)
_LicenseGroup_ObjectIdentity=ObjectIdentity
licenseGroup=_LicenseGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,500))
_ActiveFeatureTable_Object=MibTable
activeFeatureTable=_ActiveFeatureTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,500,100))
if mibBuilder.loadTexts:activeFeatureTable.setStatus(_A)
_ActiveFeatureEntry_Object=MibTableRow
activeFeatureEntry=_ActiveFeatureEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,500,100,1))
activeFeatureEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:activeFeatureEntry.setStatus(_A)
_ActiveFeatureID_Type=Unsigned32
_ActiveFeatureID_Object=MibTableColumn
activeFeatureID=_ActiveFeatureID_Object((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,500,100,1,100),_ActiveFeatureID_Type())
activeFeatureID.setMaxAccess(_B)
if mibBuilder.loadTexts:activeFeatureID.setStatus(_A)
_ActiveFeatureDescription_Type=OctetString
_ActiveFeatureDescription_Object=MibTableColumn
activeFeatureDescription=_ActiveFeatureDescription_Object((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,500,100,1,200),_ActiveFeatureDescription_Type())
activeFeatureDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:activeFeatureDescription.setStatus(_A)
class _ActiveFeatureDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*(('noOp',0),('delete',10)))
_ActiveFeatureDelete_Type.__name__=_C
_ActiveFeatureDelete_Object=MibTableColumn
activeFeatureDelete=_ActiveFeatureDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,500,100,1,500),_ActiveFeatureDelete_Type())
activeFeatureDelete.setMaxAccess(_E)
if mibBuilder.loadTexts:activeFeatureDelete.setStatus(_A)
_StatisticsGroup_ObjectIdentity=ObjectIdentity
statisticsGroup=_StatisticsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,10000))
_MemoryGroup_ObjectIdentity=ObjectIdentity
memoryGroup=_MemoryGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,10000,100))
_PersistentMemoryTotal_Type=Unsigned32
_PersistentMemoryTotal_Object=MibScalar
persistentMemoryTotal=_PersistentMemoryTotal_Object((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,10000,100,100),_PersistentMemoryTotal_Type())
persistentMemoryTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:persistentMemoryTotal.setStatus(_A)
_PersistentMemoryInUse_Type=Unsigned32
_PersistentMemoryInUse_Object=MibScalar
persistentMemoryInUse=_PersistentMemoryInUse_Object((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,10000,100,200),_PersistentMemoryInUse_Type())
persistentMemoryInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:persistentMemoryInUse.setStatus(_A)
class _PersistentWearPercentage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1000))
_PersistentWearPercentage_Type.__name__=_C
_PersistentWearPercentage_Object=MibScalar
persistentWearPercentage=_PersistentWearPercentage_Object((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,10000,100,250),_PersistentWearPercentage_Type())
persistentWearPercentage.setMaxAccess(_B)
if mibBuilder.loadTexts:persistentWearPercentage.setStatus(_A)
_VolatileMemoryTotal_Type=MxUInt64
_VolatileMemoryTotal_Object=MibScalar
volatileMemoryTotal=_VolatileMemoryTotal_Object((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,10000,100,300),_VolatileMemoryTotal_Type())
volatileMemoryTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:volatileMemoryTotal.setStatus(_A)
_VolatileMemoryInUse_Type=MxUInt64
_VolatileMemoryInUse_Object=MibScalar
volatileMemoryInUse=_VolatileMemoryInUse_Object((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,10000,100,400),_VolatileMemoryInUse_Type())
volatileMemoryInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:volatileMemoryInUse.setStatus(_A)
_InteropGroup_ObjectIdentity=ObjectIdentity
interopGroup=_InteropGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,50000))
class _InteropEthernetControllerRevA0_Type(MxEnableState):defaultValue=1
_InteropEthernetControllerRevA0_Type.__name__=_F
_InteropEthernetControllerRevA0_Object=MibScalar
interopEthernetControllerRevA0=_InteropEthernetControllerRevA0_Object((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,50000,100),_InteropEthernetControllerRevA0_Type())
interopEthernetControllerRevA0.setMaxAccess(_E)
if mibBuilder.loadTexts:interopEthernetControllerRevA0.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_C
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_E)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_C
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,2000,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'dcmMIB':dcmMIB,'dcmMIBObjects':dcmMIBObjects,'unitInfoGroup':unitInfoGroup,'unitInfoProductName':unitInfoProductName,'unitInfoSerialNumber':unitInfoSerialNumber,'unitInfoMacAddress':unitInfoMacAddress,'unitInfoHardwareRevision':unitInfoHardwareRevision,'totalNumberOfDsp':totalNumberOfDsp,'hwExtInfoGroup':hwExtInfoGroup,'hardwareExtInfoTable':hardwareExtInfoTable,'hardwareExtInfoEntry':hardwareExtInfoEntry,_G:hardwareExtInfoIndex,'hardwareExtInfoProductName':hardwareExtInfoProductName,'hardwareExtInfoSerialNumber':hardwareExtInfoSerialNumber,'hardwareExtInfoLocation':hardwareExtInfoLocation,'licenseGroup':licenseGroup,'activeFeatureTable':activeFeatureTable,'activeFeatureEntry':activeFeatureEntry,_H:activeFeatureID,'activeFeatureDescription':activeFeatureDescription,'activeFeatureDelete':activeFeatureDelete,'statisticsGroup':statisticsGroup,'memoryGroup':memoryGroup,'persistentMemoryTotal':persistentMemoryTotal,'persistentMemoryInUse':persistentMemoryInUse,'persistentWearPercentage':persistentWearPercentage,'volatileMemoryTotal':volatileMemoryTotal,'volatileMemoryInUse':volatileMemoryInUse,'interopGroup':interopGroup,'interopEthernetControllerRevA0':interopEthernetControllerRevA0,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})