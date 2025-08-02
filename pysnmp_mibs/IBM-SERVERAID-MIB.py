_U='ibmServeRaidLogicalKeyIndex'
_T='online'
_S='ibmServeRaidPhysDeviceKeyIndex'
_R='ibmServeRaidKeyIndex'
_Q='NotificationType'
_P='ibmServeRaidTrapFru'
_O='unknown'
_N='ibmServeRaidTrapPowerSupply'
_M='ibmServeRaidTrapFan'
_L='ibmServeRaidTrapScsiId'
_K='ibmServeRaidTrapArray'
_J='Integer32'
_I='ibmServeRaidTrapErrorCode'
_H='ibmServeRaidTrapChannel'
_G='not-accessible'
_F='ibmServeRaidTrapLogicalDrive'
_E='read-only'
_D='mandatory'
_C='ibmServeRaidTrapController'
_B='ibmServeRaidTrapServerName'
_A='IBM-SERVERAID-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier',_Q,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_Q,'TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
_Ibm_ObjectIdentity=ObjectIdentity
ibm=_Ibm_ObjectIdentity((1,3,6,1,4,1,2))
_IbmProd_ObjectIdentity=ObjectIdentity
ibmProd=_IbmProd_ObjectIdentity((1,3,6,1,4,1,2,6))
_IbmServeRaid_ObjectIdentity=ObjectIdentity
ibmServeRaid=_IbmServeRaid_ObjectIdentity((1,3,6,1,4,1,2,6,167))
_IbmServeRaidMIB_ObjectIdentity=ObjectIdentity
ibmServeRaidMIB=_IbmServeRaidMIB_ObjectIdentity((1,3,6,1,4,1,2,6,167,2))
_IbmServeRaidNotifications_ObjectIdentity=ObjectIdentity
ibmServeRaidNotifications=_IbmServeRaidNotifications_ObjectIdentity((1,3,6,1,4,1,2,6,167,2,0))
_IbmServeRaidMibObjects_ObjectIdentity=ObjectIdentity
ibmServeRaidMibObjects=_IbmServeRaidMibObjects_ObjectIdentity((1,3,6,1,4,1,2,6,167,2,1))
_IbmServeRaidAgentInfo_ObjectIdentity=ObjectIdentity
ibmServeRaidAgentInfo=_IbmServeRaidAgentInfo_ObjectIdentity((1,3,6,1,4,1,2,6,167,2,1,1))
_IbmServeRaidAgentKeyIndex_Type=SnmpAdminString
_IbmServeRaidAgentKeyIndex_Object=MibScalar
ibmServeRaidAgentKeyIndex=_IbmServeRaidAgentKeyIndex_Object((1,3,6,1,4,1,2,6,167,2,1,1,1),_IbmServeRaidAgentKeyIndex_Type())
ibmServeRaidAgentKeyIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidAgentKeyIndex.setStatus(_D)
_IbmServeRaidAgentId_Type=SnmpAdminString
_IbmServeRaidAgentId_Object=MibScalar
ibmServeRaidAgentId=_IbmServeRaidAgentId_Object((1,3,6,1,4,1,2,6,167,2,1,1,2),_IbmServeRaidAgentId_Type())
ibmServeRaidAgentId.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidAgentId.setStatus(_D)
_IbmServeRaidAgentCompany_Type=SnmpAdminString
_IbmServeRaidAgentCompany_Object=MibScalar
ibmServeRaidAgentCompany=_IbmServeRaidAgentCompany_Object((1,3,6,1,4,1,2,6,167,2,1,1,3),_IbmServeRaidAgentCompany_Type())
ibmServeRaidAgentCompany.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidAgentCompany.setStatus(_D)
_IbmServeRaidAgentVersion_Type=SnmpAdminString
_IbmServeRaidAgentVersion_Object=MibScalar
ibmServeRaidAgentVersion=_IbmServeRaidAgentVersion_Object((1,3,6,1,4,1,2,6,167,2,1,1,4),_IbmServeRaidAgentVersion_Type())
ibmServeRaidAgentVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidAgentVersion.setStatus(_D)
_IbmServeRaidAgentBuildDate_Type=DateAndTime
_IbmServeRaidAgentBuildDate_Object=MibScalar
ibmServeRaidAgentBuildDate=_IbmServeRaidAgentBuildDate_Object((1,3,6,1,4,1,2,6,167,2,1,1,5),_IbmServeRaidAgentBuildDate_Type())
ibmServeRaidAgentBuildDate.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidAgentBuildDate.setStatus(_D)
_IbmServeRaidAgentVersionMajor_Type=Integer32
_IbmServeRaidAgentVersionMajor_Object=MibScalar
ibmServeRaidAgentVersionMajor=_IbmServeRaidAgentVersionMajor_Object((1,3,6,1,4,1,2,6,167,2,1,1,6),_IbmServeRaidAgentVersionMajor_Type())
ibmServeRaidAgentVersionMajor.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidAgentVersionMajor.setStatus(_D)
_IbmServeRaidAgentVersionMinor_Type=Integer32
_IbmServeRaidAgentVersionMinor_Object=MibScalar
ibmServeRaidAgentVersionMinor=_IbmServeRaidAgentVersionMinor_Object((1,3,6,1,4,1,2,6,167,2,1,1,7),_IbmServeRaidAgentVersionMinor_Type())
ibmServeRaidAgentVersionMinor.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidAgentVersionMinor.setStatus(_D)
_IbmServeRaidInfo_ObjectIdentity=ObjectIdentity
ibmServeRaidInfo=_IbmServeRaidInfo_ObjectIdentity((1,3,6,1,4,1,2,6,167,2,1,2))
_IbmServeRaidControllerTable_Object=MibTable
ibmServeRaidControllerTable=_IbmServeRaidControllerTable_Object((1,3,6,1,4,1,2,6,167,2,1,2,1))
if mibBuilder.loadTexts:ibmServeRaidControllerTable.setStatus(_D)
_IbmServeRaidControllerEntry_Object=MibTableRow
ibmServeRaidControllerEntry=_IbmServeRaidControllerEntry_Object((1,3,6,1,4,1,2,6,167,2,1,2,1,1))
ibmServeRaidControllerEntry.setIndexNames((0,_A,_R))
if mibBuilder.loadTexts:ibmServeRaidControllerEntry.setStatus(_D)
_IbmServeRaidKeyIndex_Type=SnmpAdminString
_IbmServeRaidKeyIndex_Object=MibTableColumn
ibmServeRaidKeyIndex=_IbmServeRaidKeyIndex_Object((1,3,6,1,4,1,2,6,167,2,1,2,1,1,1),_IbmServeRaidKeyIndex_Type())
ibmServeRaidKeyIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ibmServeRaidKeyIndex.setStatus(_D)
class _IbmServeRaidControllerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IbmServeRaidControllerId_Type.__name__=_J
_IbmServeRaidControllerId_Object=MibTableColumn
ibmServeRaidControllerId=_IbmServeRaidControllerId_Object((1,3,6,1,4,1,2,6,167,2,1,2,1,1,2),_IbmServeRaidControllerId_Type())
ibmServeRaidControllerId.setMaxAccess(_G)
if mibBuilder.loadTexts:ibmServeRaidControllerId.setStatus(_D)
_IbmServeRaidModel_Type=SnmpAdminString
_IbmServeRaidModel_Object=MibTableColumn
ibmServeRaidModel=_IbmServeRaidModel_Object((1,3,6,1,4,1,2,6,167,2,1,2,1,1,3),_IbmServeRaidModel_Type())
ibmServeRaidModel.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidModel.setStatus(_D)
_IbmServeRaidFirmwareVersion_Type=SnmpAdminString
_IbmServeRaidFirmwareVersion_Object=MibTableColumn
ibmServeRaidFirmwareVersion=_IbmServeRaidFirmwareVersion_Object((1,3,6,1,4,1,2,6,167,2,1,2,1,1,4),_IbmServeRaidFirmwareVersion_Type())
ibmServeRaidFirmwareVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidFirmwareVersion.setStatus(_D)
_IbmServeRaidBiosVersion_Type=SnmpAdminString
_IbmServeRaidBiosVersion_Object=MibTableColumn
ibmServeRaidBiosVersion=_IbmServeRaidBiosVersion_Object((1,3,6,1,4,1,2,6,167,2,1,2,1,1,5),_IbmServeRaidBiosVersion_Type())
ibmServeRaidBiosVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidBiosVersion.setStatus(_D)
_IbmServeRaidDefaultRebuildRate_Type=SnmpAdminString
_IbmServeRaidDefaultRebuildRate_Object=MibTableColumn
ibmServeRaidDefaultRebuildRate=_IbmServeRaidDefaultRebuildRate_Object((1,3,6,1,4,1,2,6,167,2,1,2,1,1,6),_IbmServeRaidDefaultRebuildRate_Type())
ibmServeRaidDefaultRebuildRate.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidDefaultRebuildRate.setStatus(_D)
_IbmServeRaidNumChannels_Type=Gauge32
_IbmServeRaidNumChannels_Object=MibTableColumn
ibmServeRaidNumChannels=_IbmServeRaidNumChannels_Object((1,3,6,1,4,1,2,6,167,2,1,2,1,1,7),_IbmServeRaidNumChannels_Type())
ibmServeRaidNumChannels.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidNumChannels.setStatus(_D)
_IbmServeRaidMaxChannels_Type=Integer32
_IbmServeRaidMaxChannels_Object=MibTableColumn
ibmServeRaidMaxChannels=_IbmServeRaidMaxChannels_Object((1,3,6,1,4,1,2,6,167,2,1,2,1,1,8),_IbmServeRaidMaxChannels_Type())
ibmServeRaidMaxChannels.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidMaxChannels.setStatus(_D)
_IbmServeRaidNumLogicalDrives_Type=Gauge32
_IbmServeRaidNumLogicalDrives_Object=MibTableColumn
ibmServeRaidNumLogicalDrives=_IbmServeRaidNumLogicalDrives_Object((1,3,6,1,4,1,2,6,167,2,1,2,1,1,9),_IbmServeRaidNumLogicalDrives_Type())
ibmServeRaidNumLogicalDrives.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidNumLogicalDrives.setStatus(_D)
_IbmServeRaidMaxLogicalDrives_Type=Integer32
_IbmServeRaidMaxLogicalDrives_Object=MibTableColumn
ibmServeRaidMaxLogicalDrives=_IbmServeRaidMaxLogicalDrives_Object((1,3,6,1,4,1,2,6,167,2,1,2,1,1,10),_IbmServeRaidMaxLogicalDrives_Type())
ibmServeRaidMaxLogicalDrives.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidMaxLogicalDrives.setStatus(_D)
_IbmServeRaidNumPhysicalDevices_Type=Gauge32
_IbmServeRaidNumPhysicalDevices_Object=MibTableColumn
ibmServeRaidNumPhysicalDevices=_IbmServeRaidNumPhysicalDevices_Object((1,3,6,1,4,1,2,6,167,2,1,2,1,1,11),_IbmServeRaidNumPhysicalDevices_Type())
ibmServeRaidNumPhysicalDevices.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidNumPhysicalDevices.setStatus(_D)
_IbmServeRaidMaxPhysicalDevices_Type=Integer32
_IbmServeRaidMaxPhysicalDevices_Object=MibTableColumn
ibmServeRaidMaxPhysicalDevices=_IbmServeRaidMaxPhysicalDevices_Object((1,3,6,1,4,1,2,6,167,2,1,2,1,1,12),_IbmServeRaidMaxPhysicalDevices_Type())
ibmServeRaidMaxPhysicalDevices.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidMaxPhysicalDevices.setStatus(_D)
_IbmServeRaidStripeSize_Type=Integer32
_IbmServeRaidStripeSize_Object=MibTableColumn
ibmServeRaidStripeSize=_IbmServeRaidStripeSize_Object((1,3,6,1,4,1,2,6,167,2,1,2,1,1,13),_IbmServeRaidStripeSize_Type())
ibmServeRaidStripeSize.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidStripeSize.setStatus(_D)
_IbmServeRaidSlotNumber_Type=Integer32
_IbmServeRaidSlotNumber_Object=MibTableColumn
ibmServeRaidSlotNumber=_IbmServeRaidSlotNumber_Object((1,3,6,1,4,1,2,6,167,2,1,2,1,1,14),_IbmServeRaidSlotNumber_Type())
ibmServeRaidSlotNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidSlotNumber.setStatus(_D)
_IbmServeRaidVendorName_Type=SnmpAdminString
_IbmServeRaidVendorName_Object=MibTableColumn
ibmServeRaidVendorName=_IbmServeRaidVendorName_Object((1,3,6,1,4,1,2,6,167,2,1,2,1,1,15),_IbmServeRaidVendorName_Type())
ibmServeRaidVendorName.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidVendorName.setStatus(_D)
class _IbmServeRaidGeneralStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('fail',2)))
_IbmServeRaidGeneralStatus_Type.__name__=_J
_IbmServeRaidGeneralStatus_Object=MibTableColumn
ibmServeRaidGeneralStatus=_IbmServeRaidGeneralStatus_Object((1,3,6,1,4,1,2,6,167,2,1,2,1,1,16),_IbmServeRaidGeneralStatus_Type())
ibmServeRaidGeneralStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidGeneralStatus.setStatus(_D)
_IbmServeRaidPhysDeviceTable_Object=MibTable
ibmServeRaidPhysDeviceTable=_IbmServeRaidPhysDeviceTable_Object((1,3,6,1,4,1,2,6,167,2,1,2,2))
if mibBuilder.loadTexts:ibmServeRaidPhysDeviceTable.setStatus(_D)
_IbmServeRaidPhysDeviceEntry_Object=MibTableRow
ibmServeRaidPhysDeviceEntry=_IbmServeRaidPhysDeviceEntry_Object((1,3,6,1,4,1,2,6,167,2,1,2,2,1))
ibmServeRaidPhysDeviceEntry.setIndexNames((0,_A,_S))
if mibBuilder.loadTexts:ibmServeRaidPhysDeviceEntry.setStatus(_D)
_IbmServeRaidPhysDeviceKeyIndex_Type=SnmpAdminString
_IbmServeRaidPhysDeviceKeyIndex_Object=MibTableColumn
ibmServeRaidPhysDeviceKeyIndex=_IbmServeRaidPhysDeviceKeyIndex_Object((1,3,6,1,4,1,2,6,167,2,1,2,2,1,1),_IbmServeRaidPhysDeviceKeyIndex_Type())
ibmServeRaidPhysDeviceKeyIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ibmServeRaidPhysDeviceKeyIndex.setStatus(_D)
class _IbmServeRaidPhysDeviceControllerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IbmServeRaidPhysDeviceControllerId_Type.__name__=_J
_IbmServeRaidPhysDeviceControllerId_Object=MibTableColumn
ibmServeRaidPhysDeviceControllerId=_IbmServeRaidPhysDeviceControllerId_Object((1,3,6,1,4,1,2,6,167,2,1,2,2,1,2),_IbmServeRaidPhysDeviceControllerId_Type())
ibmServeRaidPhysDeviceControllerId.setMaxAccess(_G)
if mibBuilder.loadTexts:ibmServeRaidPhysDeviceControllerId.setStatus(_D)
class _IbmServeRaidPhysDeviceChannelNr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IbmServeRaidPhysDeviceChannelNr_Type.__name__=_J
_IbmServeRaidPhysDeviceChannelNr_Object=MibTableColumn
ibmServeRaidPhysDeviceChannelNr=_IbmServeRaidPhysDeviceChannelNr_Object((1,3,6,1,4,1,2,6,167,2,1,2,2,1,3),_IbmServeRaidPhysDeviceChannelNr_Type())
ibmServeRaidPhysDeviceChannelNr.setMaxAccess(_G)
if mibBuilder.loadTexts:ibmServeRaidPhysDeviceChannelNr.setStatus(_D)
class _IbmServeRaidPhysDeviceDevNr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IbmServeRaidPhysDeviceDevNr_Type.__name__=_J
_IbmServeRaidPhysDeviceDevNr_Object=MibTableColumn
ibmServeRaidPhysDeviceDevNr=_IbmServeRaidPhysDeviceDevNr_Object((1,3,6,1,4,1,2,6,167,2,1,2,2,1,4),_IbmServeRaidPhysDeviceDevNr_Type())
ibmServeRaidPhysDeviceDevNr.setMaxAccess(_G)
if mibBuilder.loadTexts:ibmServeRaidPhysDeviceDevNr.setStatus(_D)
_IbmServeRaidPhysDeviceModel_Type=SnmpAdminString
_IbmServeRaidPhysDeviceModel_Object=MibTableColumn
ibmServeRaidPhysDeviceModel=_IbmServeRaidPhysDeviceModel_Object((1,3,6,1,4,1,2,6,167,2,1,2,2,1,5),_IbmServeRaidPhysDeviceModel_Type())
ibmServeRaidPhysDeviceModel.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidPhysDeviceModel.setStatus(_D)
_IbmServeRaidPhysDeviceCapacity_Type=Integer32
_IbmServeRaidPhysDeviceCapacity_Object=MibTableColumn
ibmServeRaidPhysDeviceCapacity=_IbmServeRaidPhysDeviceCapacity_Object((1,3,6,1,4,1,2,6,167,2,1,2,2,1,6),_IbmServeRaidPhysDeviceCapacity_Type())
ibmServeRaidPhysDeviceCapacity.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidPhysDeviceCapacity.setStatus(_D)
class _IbmServeRaidPhysDeviceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,9)));namedValues=NamedValues(*(('dead',1),(_T,2),('standby',3),('rebuild',4),('spare',5),('ready',6),('empty',7),(_O,9)))
_IbmServeRaidPhysDeviceStatus_Type.__name__=_J
_IbmServeRaidPhysDeviceStatus_Object=MibTableColumn
ibmServeRaidPhysDeviceStatus=_IbmServeRaidPhysDeviceStatus_Object((1,3,6,1,4,1,2,6,167,2,1,2,2,1,7),_IbmServeRaidPhysDeviceStatus_Type())
ibmServeRaidPhysDeviceStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidPhysDeviceStatus.setStatus(_D)
_IbmServeRaidPhysDeviceDiskConfigured_Type=TruthValue
_IbmServeRaidPhysDeviceDiskConfigured_Object=MibTableColumn
ibmServeRaidPhysDeviceDiskConfigured=_IbmServeRaidPhysDeviceDiskConfigured_Object((1,3,6,1,4,1,2,6,167,2,1,2,2,1,8),_IbmServeRaidPhysDeviceDiskConfigured_Type())
ibmServeRaidPhysDeviceDiskConfigured.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidPhysDeviceDiskConfigured.setStatus(_D)
class _IbmServeRaidPhysDeviceScsiType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,97,98,99)));namedValues=NamedValues(*(('disk',1),('tape',2),('printer',3),('processor',4),('writeOnce',5),('cdRom',6),('scanner',7),('optical',8),('jukebox',9),('commDev',10),('enclosure',97),('host',98),(_O,99)))
_IbmServeRaidPhysDeviceScsiType_Type.__name__=_J
_IbmServeRaidPhysDeviceScsiType_Object=MibTableColumn
ibmServeRaidPhysDeviceScsiType=_IbmServeRaidPhysDeviceScsiType_Object((1,3,6,1,4,1,2,6,167,2,1,2,2,1,9),_IbmServeRaidPhysDeviceScsiType_Type())
ibmServeRaidPhysDeviceScsiType.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidPhysDeviceScsiType.setStatus(_D)
class _IbmServeRaidPhysDevicePfaStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('failurePredicted',2)))
_IbmServeRaidPhysDevicePfaStatus_Type.__name__=_J
_IbmServeRaidPhysDevicePfaStatus_Object=MibTableColumn
ibmServeRaidPhysDevicePfaStatus=_IbmServeRaidPhysDevicePfaStatus_Object((1,3,6,1,4,1,2,6,167,2,1,2,2,1,10),_IbmServeRaidPhysDevicePfaStatus_Type())
ibmServeRaidPhysDevicePfaStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidPhysDevicePfaStatus.setStatus(_D)
_IbmServeRaidLogicalTable_Object=MibTable
ibmServeRaidLogicalTable=_IbmServeRaidLogicalTable_Object((1,3,6,1,4,1,2,6,167,2,1,2,3))
if mibBuilder.loadTexts:ibmServeRaidLogicalTable.setStatus(_D)
_IbmServeRaidLogicalEntry_Object=MibTableRow
ibmServeRaidLogicalEntry=_IbmServeRaidLogicalEntry_Object((1,3,6,1,4,1,2,6,167,2,1,2,3,1))
ibmServeRaidLogicalEntry.setIndexNames((0,_A,_U))
if mibBuilder.loadTexts:ibmServeRaidLogicalEntry.setStatus(_D)
_IbmServeRaidLogicalKeyIndex_Type=SnmpAdminString
_IbmServeRaidLogicalKeyIndex_Object=MibTableColumn
ibmServeRaidLogicalKeyIndex=_IbmServeRaidLogicalKeyIndex_Object((1,3,6,1,4,1,2,6,167,2,1,2,3,1,1),_IbmServeRaidLogicalKeyIndex_Type())
ibmServeRaidLogicalKeyIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ibmServeRaidLogicalKeyIndex.setStatus(_D)
class _IbmServeRaidLogicalControllerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IbmServeRaidLogicalControllerId_Type.__name__=_J
_IbmServeRaidLogicalControllerId_Object=MibTableColumn
ibmServeRaidLogicalControllerId=_IbmServeRaidLogicalControllerId_Object((1,3,6,1,4,1,2,6,167,2,1,2,3,1,2),_IbmServeRaidLogicalControllerId_Type())
ibmServeRaidLogicalControllerId.setMaxAccess(_G)
if mibBuilder.loadTexts:ibmServeRaidLogicalControllerId.setStatus(_D)
class _IbmServeRaidLogicalDriveNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IbmServeRaidLogicalDriveNum_Type.__name__=_J
_IbmServeRaidLogicalDriveNum_Object=MibTableColumn
ibmServeRaidLogicalDriveNum=_IbmServeRaidLogicalDriveNum_Object((1,3,6,1,4,1,2,6,167,2,1,2,3,1,3),_IbmServeRaidLogicalDriveNum_Type())
ibmServeRaidLogicalDriveNum.setMaxAccess(_G)
if mibBuilder.loadTexts:ibmServeRaidLogicalDriveNum.setStatus(_D)
class _IbmServeRaidLogicalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,9)));namedValues=NamedValues(*((_T,1),('critical',2),('offline',3),('migrating',4),('free',5),(_O,9)))
_IbmServeRaidLogicalStatus_Type.__name__=_J
_IbmServeRaidLogicalStatus_Object=MibTableColumn
ibmServeRaidLogicalStatus=_IbmServeRaidLogicalStatus_Object((1,3,6,1,4,1,2,6,167,2,1,2,3,1,4),_IbmServeRaidLogicalStatus_Type())
ibmServeRaidLogicalStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidLogicalStatus.setStatus(_D)
_IbmServeRaidLogicalSize_Type=Integer32
_IbmServeRaidLogicalSize_Object=MibTableColumn
ibmServeRaidLogicalSize=_IbmServeRaidLogicalSize_Object((1,3,6,1,4,1,2,6,167,2,1,2,3,1,5),_IbmServeRaidLogicalSize_Type())
ibmServeRaidLogicalSize.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidLogicalSize.setStatus(_D)
_IbmServeRaidLogicalRaidLevel_Type=SnmpAdminString
_IbmServeRaidLogicalRaidLevel_Object=MibTableColumn
ibmServeRaidLogicalRaidLevel=_IbmServeRaidLogicalRaidLevel_Object((1,3,6,1,4,1,2,6,167,2,1,2,3,1,6),_IbmServeRaidLogicalRaidLevel_Type())
ibmServeRaidLogicalRaidLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidLogicalRaidLevel.setStatus(_D)
class _IbmServeRaidLogicalWriteCacheMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('writeBack',1),('writeThrough',2)))
_IbmServeRaidLogicalWriteCacheMode_Type.__name__=_J
_IbmServeRaidLogicalWriteCacheMode_Object=MibTableColumn
ibmServeRaidLogicalWriteCacheMode=_IbmServeRaidLogicalWriteCacheMode_Object((1,3,6,1,4,1,2,6,167,2,1,2,3,1,7),_IbmServeRaidLogicalWriteCacheMode_Type())
ibmServeRaidLogicalWriteCacheMode.setMaxAccess(_E)
if mibBuilder.loadTexts:ibmServeRaidLogicalWriteCacheMode.setStatus(_D)
_IbmServeRaidTrapInfo_ObjectIdentity=ObjectIdentity
ibmServeRaidTrapInfo=_IbmServeRaidTrapInfo_ObjectIdentity((1,3,6,1,4,1,2,6,167,2,1,3))
_IbmServeRaidTrapController_Type=Integer32
_IbmServeRaidTrapController_Object=MibScalar
ibmServeRaidTrapController=_IbmServeRaidTrapController_Object((1,3,6,1,4,1,2,6,167,2,1,3,1),_IbmServeRaidTrapController_Type())
ibmServeRaidTrapController.setMaxAccess(_G)
if mibBuilder.loadTexts:ibmServeRaidTrapController.setStatus(_D)
_IbmServeRaidTrapLogicalDrive_Type=Integer32
_IbmServeRaidTrapLogicalDrive_Object=MibScalar
ibmServeRaidTrapLogicalDrive=_IbmServeRaidTrapLogicalDrive_Object((1,3,6,1,4,1,2,6,167,2,1,3,2),_IbmServeRaidTrapLogicalDrive_Type())
ibmServeRaidTrapLogicalDrive.setMaxAccess(_G)
if mibBuilder.loadTexts:ibmServeRaidTrapLogicalDrive.setStatus(_D)
_IbmServeRaidTrapChannel_Type=Integer32
_IbmServeRaidTrapChannel_Object=MibScalar
ibmServeRaidTrapChannel=_IbmServeRaidTrapChannel_Object((1,3,6,1,4,1,2,6,167,2,1,3,3),_IbmServeRaidTrapChannel_Type())
ibmServeRaidTrapChannel.setMaxAccess(_G)
if mibBuilder.loadTexts:ibmServeRaidTrapChannel.setStatus(_D)
_IbmServeRaidTrapScsiId_Type=Integer32
_IbmServeRaidTrapScsiId_Object=MibScalar
ibmServeRaidTrapScsiId=_IbmServeRaidTrapScsiId_Object((1,3,6,1,4,1,2,6,167,2,1,3,4),_IbmServeRaidTrapScsiId_Type())
ibmServeRaidTrapScsiId.setMaxAccess(_G)
if mibBuilder.loadTexts:ibmServeRaidTrapScsiId.setStatus(_D)
_IbmServeRaidTrapFan_Type=Integer32
_IbmServeRaidTrapFan_Object=MibScalar
ibmServeRaidTrapFan=_IbmServeRaidTrapFan_Object((1,3,6,1,4,1,2,6,167,2,1,3,5),_IbmServeRaidTrapFan_Type())
ibmServeRaidTrapFan.setMaxAccess(_G)
if mibBuilder.loadTexts:ibmServeRaidTrapFan.setStatus(_D)
_IbmServeRaidTrapPowerSupply_Type=Integer32
_IbmServeRaidTrapPowerSupply_Object=MibScalar
ibmServeRaidTrapPowerSupply=_IbmServeRaidTrapPowerSupply_Object((1,3,6,1,4,1,2,6,167,2,1,3,6),_IbmServeRaidTrapPowerSupply_Type())
ibmServeRaidTrapPowerSupply.setMaxAccess(_G)
if mibBuilder.loadTexts:ibmServeRaidTrapPowerSupply.setStatus(_D)
_IbmServeRaidTrapErrorCode_Type=Integer32
_IbmServeRaidTrapErrorCode_Object=MibScalar
ibmServeRaidTrapErrorCode=_IbmServeRaidTrapErrorCode_Object((1,3,6,1,4,1,2,6,167,2,1,3,7),_IbmServeRaidTrapErrorCode_Type())
ibmServeRaidTrapErrorCode.setMaxAccess(_G)
if mibBuilder.loadTexts:ibmServeRaidTrapErrorCode.setStatus(_D)
_IbmServeRaidTrapServerName_Type=SnmpAdminString
_IbmServeRaidTrapServerName_Object=MibScalar
ibmServeRaidTrapServerName=_IbmServeRaidTrapServerName_Object((1,3,6,1,4,1,2,6,167,2,1,3,8),_IbmServeRaidTrapServerName_Type())
ibmServeRaidTrapServerName.setMaxAccess(_G)
if mibBuilder.loadTexts:ibmServeRaidTrapServerName.setStatus(_D)
_IbmServeRaidTrapArray_Type=SnmpAdminString
_IbmServeRaidTrapArray_Object=MibScalar
ibmServeRaidTrapArray=_IbmServeRaidTrapArray_Object((1,3,6,1,4,1,2,6,167,2,1,3,9),_IbmServeRaidTrapArray_Type())
ibmServeRaidTrapArray.setMaxAccess(_G)
if mibBuilder.loadTexts:ibmServeRaidTrapArray.setStatus(_D)
_IbmServeRaidTrapFru_Type=SnmpAdminString
_IbmServeRaidTrapFru_Object=MibScalar
ibmServeRaidTrapFru=_IbmServeRaidTrapFru_Object((1,3,6,1,4,1,2,6,167,2,1,3,10),_IbmServeRaidTrapFru_Type())
ibmServeRaidTrapFru.setMaxAccess(_G)
if mibBuilder.loadTexts:ibmServeRaidTrapFru.setStatus(_D)
_IbmServeRaidConformance_ObjectIdentity=ObjectIdentity
ibmServeRaidConformance=_IbmServeRaidConformance_ObjectIdentity((1,3,6,1,4,1,2,6,167,2,2))
_IbmServeRaidCompliances_ObjectIdentity=ObjectIdentity
ibmServeRaidCompliances=_IbmServeRaidCompliances_ObjectIdentity((1,3,6,1,4,1,2,6,167,2,2,1))
_IbmServeRaidCompliance_ObjectIdentity=ObjectIdentity
ibmServeRaidCompliance=_IbmServeRaidCompliance_ObjectIdentity((1,3,6,1,4,1,2,6,167,2,2,1,1))
_IbmServeRaidGroups_ObjectIdentity=ObjectIdentity
ibmServeRaidGroups=_IbmServeRaidGroups_ObjectIdentity((1,3,6,1,4,1,2,6,167,2,2,2))
_IbmServeRaidAgentGroup_ObjectIdentity=ObjectIdentity
ibmServeRaidAgentGroup=_IbmServeRaidAgentGroup_ObjectIdentity((1,3,6,1,4,1,2,6,167,2,2,2,1))
_IbmServeRaidControllerGroup_ObjectIdentity=ObjectIdentity
ibmServeRaidControllerGroup=_IbmServeRaidControllerGroup_ObjectIdentity((1,3,6,1,4,1,2,6,167,2,2,2,2))
_IbmServeRaidPhysicalGroup_ObjectIdentity=ObjectIdentity
ibmServeRaidPhysicalGroup=_IbmServeRaidPhysicalGroup_ObjectIdentity((1,3,6,1,4,1,2,6,167,2,2,2,3))
_IbmServeRaidLogicalGroup_ObjectIdentity=ObjectIdentity
ibmServeRaidLogicalGroup=_IbmServeRaidLogicalGroup_ObjectIdentity((1,3,6,1,4,1,2,6,167,2,2,2,4))
_IbmServeRaidTrapInfoGroup_ObjectIdentity=ObjectIdentity
ibmServeRaidTrapInfoGroup=_IbmServeRaidTrapInfoGroup_ObjectIdentity((1,3,6,1,4,1,2,6,167,2,2,2,5))
_IbmServeRaidNotificationsGroup_ObjectIdentity=ObjectIdentity
ibmServeRaidNotificationsGroup=_IbmServeRaidNotificationsGroup_ObjectIdentity((1,3,6,1,4,1,2,6,167,2,2,2,6))
ibmServeRaidNoControllers=NotificationType((1,3,6,1,4,1,2,6,167,2,0,201))
ibmServeRaidNoControllers.setObjects((_A,_B))
if mibBuilder.loadTexts:ibmServeRaidNoControllers.setStatus('')
ibmServeRaidControllerFail=NotificationType((1,3,6,1,4,1,2,6,167,2,0,202))
ibmServeRaidControllerFail.setObjects(*((_A,_B),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidControllerFail.setStatus('')
ibmServeRaidDeadBattery=NotificationType((1,3,6,1,4,1,2,6,167,2,0,203))
ibmServeRaidDeadBattery.setObjects(*((_A,_B),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidDeadBattery.setStatus('')
ibmServeRaidDeadBatteryCache=NotificationType((1,3,6,1,4,1,2,6,167,2,0,204))
ibmServeRaidDeadBatteryCache.setObjects(*((_A,_B),(_A,_C),(_A,_I)))
if mibBuilder.loadTexts:ibmServeRaidDeadBatteryCache.setStatus('')
ibmServeRaidPollingFail=NotificationType((1,3,6,1,4,1,2,6,167,2,0,205))
ibmServeRaidPollingFail.setObjects(*((_A,_B),(_A,_C),(_A,_I)))
if mibBuilder.loadTexts:ibmServeRaidPollingFail.setStatus('')
ibmServeRaidConfigFail=NotificationType((1,3,6,1,4,1,2,6,167,2,0,206))
ibmServeRaidConfigFail.setObjects((_A,_B))
if mibBuilder.loadTexts:ibmServeRaidConfigFail.setStatus('')
ibmServeRaidControllerAdded=NotificationType((1,3,6,1,4,1,2,6,167,2,0,207))
ibmServeRaidControllerAdded.setObjects(*((_A,_B),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidControllerAdded.setStatus('')
ibmServeRaidControllerReplaced=NotificationType((1,3,6,1,4,1,2,6,167,2,0,208))
ibmServeRaidControllerReplaced.setObjects(*((_A,_B),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidControllerReplaced.setStatus('')
ibmServeRaidControllerFailover=NotificationType((1,3,6,1,4,1,2,6,167,2,0,209))
ibmServeRaidControllerFailover.setObjects(*((_A,_B),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidControllerFailover.setStatus('')
ibmServeRaidControllerVersionMismatch=NotificationType((1,3,6,1,4,1,2,6,167,2,0,210))
ibmServeRaidControllerVersionMismatch.setObjects(*((_A,_B),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidControllerVersionMismatch.setStatus('')
ibmServeRaidControllerBatteryOvertemp=NotificationType((1,3,6,1,4,1,2,6,167,2,0,211))
ibmServeRaidControllerBatteryOvertemp.setObjects(*((_A,_B),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidControllerBatteryOvertemp.setStatus('')
ibmServeRaidLogicalDriveCritical=NotificationType((1,3,6,1,4,1,2,6,167,2,0,301))
ibmServeRaidLogicalDriveCritical.setObjects(*((_A,_B),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidLogicalDriveCritical.setStatus('')
ibmServeRaidLogicalDriveBlocked=NotificationType((1,3,6,1,4,1,2,6,167,2,0,302))
ibmServeRaidLogicalDriveBlocked.setObjects(*((_A,_B),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidLogicalDriveBlocked.setStatus('')
ibmServeRaidLogicalDriveOffLine=NotificationType((1,3,6,1,4,1,2,6,167,2,0,303))
ibmServeRaidLogicalDriveOffLine.setObjects(*((_A,_B),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidLogicalDriveOffLine.setStatus('')
ibmServeRaidRebuildDetected=NotificationType((1,3,6,1,4,1,2,6,167,2,0,304))
ibmServeRaidRebuildDetected.setObjects(*((_A,_B),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidRebuildDetected.setStatus('')
ibmServeRaidRebuildComplete=NotificationType((1,3,6,1,4,1,2,6,167,2,0,305))
ibmServeRaidRebuildComplete.setObjects(*((_A,_B),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidRebuildComplete.setStatus('')
ibmServeRaidRebuildFail=NotificationType((1,3,6,1,4,1,2,6,167,2,0,306))
ibmServeRaidRebuildFail.setObjects(*((_A,_B),(_A,_F),(_A,_C),(_A,_I)))
if mibBuilder.loadTexts:ibmServeRaidRebuildFail.setStatus('')
ibmServeRaidSyncDetected=NotificationType((1,3,6,1,4,1,2,6,167,2,0,307))
ibmServeRaidSyncDetected.setObjects(*((_A,_B),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidSyncDetected.setStatus('')
ibmServeRaidSyncComplete=NotificationType((1,3,6,1,4,1,2,6,167,2,0,308))
ibmServeRaidSyncComplete.setObjects(*((_A,_B),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidSyncComplete.setStatus('')
ibmServeRaidSyncFail=NotificationType((1,3,6,1,4,1,2,6,167,2,0,309))
ibmServeRaidSyncFail.setObjects(*((_A,_B),(_A,_F),(_A,_C),(_A,_I)))
if mibBuilder.loadTexts:ibmServeRaidSyncFail.setStatus('')
ibmServeRaidMigrationDetected=NotificationType((1,3,6,1,4,1,2,6,167,2,0,310))
ibmServeRaidMigrationDetected.setObjects(*((_A,_B),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidMigrationDetected.setStatus('')
ibmServeRaidMigrationComplete=NotificationType((1,3,6,1,4,1,2,6,167,2,0,311))
ibmServeRaidMigrationComplete.setObjects(*((_A,_B),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidMigrationComplete.setStatus('')
ibmServeRaidMigrationFail=NotificationType((1,3,6,1,4,1,2,6,167,2,0,312))
ibmServeRaidMigrationFail.setObjects(*((_A,_B),(_A,_F),(_A,_C),(_A,_I)))
if mibBuilder.loadTexts:ibmServeRaidMigrationFail.setStatus('')
ibmServeRaidCompressionDetected=NotificationType((1,3,6,1,4,1,2,6,167,2,0,313))
ibmServeRaidCompressionDetected.setObjects(*((_A,_B),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidCompressionDetected.setStatus('')
ibmServeRaidCompressionComplete=NotificationType((1,3,6,1,4,1,2,6,167,2,0,314))
ibmServeRaidCompressionComplete.setObjects(*((_A,_B),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidCompressionComplete.setStatus('')
ibmServeRaidcompressionFail=NotificationType((1,3,6,1,4,1,2,6,167,2,0,315))
ibmServeRaidcompressionFail.setObjects(*((_A,_B),(_A,_F),(_A,_C),(_A,_I)))
if mibBuilder.loadTexts:ibmServeRaidcompressionFail.setStatus('')
ibmServeRaidDecompressionDetected=NotificationType((1,3,6,1,4,1,2,6,167,2,0,316))
ibmServeRaidDecompressionDetected.setObjects(*((_A,_B),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidDecompressionDetected.setStatus('')
ibmServeRaidDecompressionComplete=NotificationType((1,3,6,1,4,1,2,6,167,2,0,317))
ibmServeRaidDecompressionComplete.setObjects(*((_A,_B),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidDecompressionComplete.setStatus('')
ibmServeRaidDecompressionFail=NotificationType((1,3,6,1,4,1,2,6,167,2,0,318))
ibmServeRaidDecompressionFail.setObjects(*((_A,_B),(_A,_F),(_A,_C),(_A,_I)))
if mibBuilder.loadTexts:ibmServeRaidDecompressionFail.setStatus('')
ibmServeRaidFlashCopyDetected=NotificationType((1,3,6,1,4,1,2,6,167,2,0,319))
ibmServeRaidFlashCopyDetected.setObjects(*((_A,_B),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidFlashCopyDetected.setStatus('')
ibmServeRaidFlashCopyComplete=NotificationType((1,3,6,1,4,1,2,6,167,2,0,320))
ibmServeRaidFlashCopyComplete.setObjects(*((_A,_B),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidFlashCopyComplete.setStatus('')
ibmServeRaidFlashCopyFail=NotificationType((1,3,6,1,4,1,2,6,167,2,0,321))
ibmServeRaidFlashCopyFail.setObjects(*((_A,_B),(_A,_F),(_A,_C),(_A,_I)))
if mibBuilder.loadTexts:ibmServeRaidFlashCopyFail.setStatus('')
ibmServeRaidArrayRebuildDetected=NotificationType((1,3,6,1,4,1,2,6,167,2,0,322))
ibmServeRaidArrayRebuildDetected.setObjects(*((_A,_B),(_A,_K),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidArrayRebuildDetected.setStatus('')
ibmServeRaidArrayRebuildComplete=NotificationType((1,3,6,1,4,1,2,6,167,2,0,323))
ibmServeRaidArrayRebuildComplete.setObjects(*((_A,_B),(_A,_K),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidArrayRebuildComplete.setStatus('')
ibmServeRaidArrayRebuildFail=NotificationType((1,3,6,1,4,1,2,6,167,2,0,324))
ibmServeRaidArrayRebuildFail.setObjects(*((_A,_B),(_A,_K),(_A,_C),(_A,_I)))
if mibBuilder.loadTexts:ibmServeRaidArrayRebuildFail.setStatus('')
ibmServeRaidArraySyncDetected=NotificationType((1,3,6,1,4,1,2,6,167,2,0,325))
ibmServeRaidArraySyncDetected.setObjects(*((_A,_B),(_A,_K),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidArraySyncDetected.setStatus('')
ibmServeRaidArraySyncComplete=NotificationType((1,3,6,1,4,1,2,6,167,2,0,326))
ibmServeRaidArraySyncComplete.setObjects(*((_A,_B),(_A,_K),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidArraySyncComplete.setStatus('')
ibmServeRaidArraySyncFail=NotificationType((1,3,6,1,4,1,2,6,167,2,0,327))
ibmServeRaidArraySyncFail.setObjects(*((_A,_B),(_A,_K),(_A,_C),(_A,_I)))
if mibBuilder.loadTexts:ibmServeRaidArraySyncFail.setStatus('')
ibmServeRaidArrayFlashCopyDetected=NotificationType((1,3,6,1,4,1,2,6,167,2,0,328))
ibmServeRaidArrayFlashCopyDetected.setObjects(*((_A,_B),(_A,_K),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidArrayFlashCopyDetected.setStatus('')
ibmServeRaidArrayFlashCopyComplete=NotificationType((1,3,6,1,4,1,2,6,167,2,0,329))
ibmServeRaidArrayFlashCopyComplete.setObjects(*((_A,_B),(_A,_K),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidArrayFlashCopyComplete.setStatus('')
ibmServeRaidArrayFlashCopyFail=NotificationType((1,3,6,1,4,1,2,6,167,2,0,330))
ibmServeRaidArrayFlashCopyFail.setObjects(*((_A,_B),(_A,_K),(_A,_C),(_A,_I)))
if mibBuilder.loadTexts:ibmServeRaidArrayFlashCopyFail.setStatus('')
ibmServeRaidLogicalDriveUnblocked=NotificationType((1,3,6,1,4,1,2,6,167,2,0,331))
ibmServeRaidLogicalDriveUnblocked.setObjects(*((_A,_B),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidLogicalDriveUnblocked.setStatus('')
ibmServeRaidCompactionDetected=NotificationType((1,3,6,1,4,1,2,6,167,2,0,332))
ibmServeRaidCompactionDetected.setObjects(*((_A,_B),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidCompactionDetected.setStatus('')
ibmServeRaidCompactionComplete=NotificationType((1,3,6,1,4,1,2,6,167,2,0,333))
ibmServeRaidCompactionComplete.setObjects(*((_A,_B),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidCompactionComplete.setStatus('')
ibmServeRaidCompactionFail=NotificationType((1,3,6,1,4,1,2,6,167,2,0,334))
ibmServeRaidCompactionFail.setObjects(*((_A,_B),(_A,_F),(_A,_C),(_A,_I)))
if mibBuilder.loadTexts:ibmServeRaidCompactionFail.setStatus('')
ibmServeRaidExpansionDetected=NotificationType((1,3,6,1,4,1,2,6,167,2,0,335))
ibmServeRaidExpansionDetected.setObjects(*((_A,_B),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidExpansionDetected.setStatus('')
ibmServeRaidExpansionComplete=NotificationType((1,3,6,1,4,1,2,6,167,2,0,336))
ibmServeRaidExpansionComplete.setObjects(*((_A,_B),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidExpansionComplete.setStatus('')
ibmServeRaidExpansionFail=NotificationType((1,3,6,1,4,1,2,6,167,2,0,337))
ibmServeRaidExpansionFail.setObjects(*((_A,_B),(_A,_F),(_A,_C),(_A,_I)))
if mibBuilder.loadTexts:ibmServeRaidExpansionFail.setStatus('')
ibmServeRaidLogicalDriveCriticalPeriodic=NotificationType((1,3,6,1,4,1,2,6,167,2,0,338))
ibmServeRaidLogicalDriveCriticalPeriodic.setObjects(*((_A,_B),(_A,_C)))
if mibBuilder.loadTexts:ibmServeRaidLogicalDriveCriticalPeriodic.setStatus('')
ibmServeRaidDefunctDrive=NotificationType((1,3,6,1,4,1,2,6,167,2,0,401))
ibmServeRaidDefunctDrive.setObjects(*((_A,_B),(_A,_C),(_A,_H),(_A,_L)))
if mibBuilder.loadTexts:ibmServeRaidDefunctDrive.setStatus('')
ibmServeRaidPfaDrive=NotificationType((1,3,6,1,4,1,2,6,167,2,0,402))
ibmServeRaidPfaDrive.setObjects(*((_A,_B),(_A,_C),(_A,_H),(_A,_L)))
if mibBuilder.loadTexts:ibmServeRaidPfaDrive.setStatus('')
ibmServeRaidDefunctReplaced=NotificationType((1,3,6,1,4,1,2,6,167,2,0,403))
ibmServeRaidDefunctReplaced.setObjects(*((_A,_B),(_A,_C),(_A,_H),(_A,_L)))
if mibBuilder.loadTexts:ibmServeRaidDefunctReplaced.setStatus('')
ibmServeRaidDefunctDriveFru=NotificationType((1,3,6,1,4,1,2,6,167,2,0,404))
ibmServeRaidDefunctDriveFru.setObjects(*((_A,_B),(_A,_P),(_A,_C),(_A,_H),(_A,_L)))
if mibBuilder.loadTexts:ibmServeRaidDefunctDriveFru.setStatus('')
ibmServeRaidPfaDriveFru=NotificationType((1,3,6,1,4,1,2,6,167,2,0,405))
ibmServeRaidPfaDriveFru.setObjects(*((_A,_B),(_A,_P),(_A,_C),(_A,_H),(_A,_L)))
if mibBuilder.loadTexts:ibmServeRaidPfaDriveFru.setStatus('')
ibmServeRaidUnsupportedDrive=NotificationType((1,3,6,1,4,1,2,6,167,2,0,406))
ibmServeRaidUnsupportedDrive.setObjects(*((_A,_B),(_A,_C),(_A,_H),(_A,_L)))
if mibBuilder.loadTexts:ibmServeRaidUnsupportedDrive.setStatus('')
ibmServeRaidEnclosureOK=NotificationType((1,3,6,1,4,1,2,6,167,2,0,501))
ibmServeRaidEnclosureOK.setObjects(*((_A,_B),(_A,_C),(_A,_H)))
if mibBuilder.loadTexts:ibmServeRaidEnclosureOK.setStatus('')
ibmServeRaidEnclosureFail=NotificationType((1,3,6,1,4,1,2,6,167,2,0,502))
ibmServeRaidEnclosureFail.setObjects(*((_A,_B),(_A,_C),(_A,_H)))
if mibBuilder.loadTexts:ibmServeRaidEnclosureFail.setStatus('')
ibmServeRaidFanOk=NotificationType((1,3,6,1,4,1,2,6,167,2,0,503))
ibmServeRaidFanOk.setObjects(*((_A,_B),(_A,_M),(_A,_C),(_A,_H)))
if mibBuilder.loadTexts:ibmServeRaidFanOk.setStatus('')
ibmServeRaidFanFail=NotificationType((1,3,6,1,4,1,2,6,167,2,0,504))
ibmServeRaidFanFail.setObjects(*((_A,_B),(_A,_M),(_A,_C),(_A,_H)))
if mibBuilder.loadTexts:ibmServeRaidFanFail.setStatus('')
ibmServeRaidFanInstalled=NotificationType((1,3,6,1,4,1,2,6,167,2,0,505))
ibmServeRaidFanInstalled.setObjects(*((_A,_B),(_A,_M),(_A,_C),(_A,_H)))
if mibBuilder.loadTexts:ibmServeRaidFanInstalled.setStatus('')
ibmServeRaidFanRemoved=NotificationType((1,3,6,1,4,1,2,6,167,2,0,506))
ibmServeRaidFanRemoved.setObjects(*((_A,_B),(_A,_M),(_A,_C),(_A,_H)))
if mibBuilder.loadTexts:ibmServeRaidFanRemoved.setStatus('')
ibmServeRaidTempOk=NotificationType((1,3,6,1,4,1,2,6,167,2,0,507))
ibmServeRaidTempOk.setObjects(*((_A,_B),(_A,_C),(_A,_H)))
if mibBuilder.loadTexts:ibmServeRaidTempOk.setStatus('')
ibmServeRaidTempFail=NotificationType((1,3,6,1,4,1,2,6,167,2,0,508))
ibmServeRaidTempFail.setObjects(*((_A,_B),(_A,_C),(_A,_H)))
if mibBuilder.loadTexts:ibmServeRaidTempFail.setStatus('')
ibmServeRaidPowerSupplyOk=NotificationType((1,3,6,1,4,1,2,6,167,2,0,509))
ibmServeRaidPowerSupplyOk.setObjects(*((_A,_B),(_A,_N),(_A,_C),(_A,_H)))
if mibBuilder.loadTexts:ibmServeRaidPowerSupplyOk.setStatus('')
ibmServeRaidPowerSupplyFail=NotificationType((1,3,6,1,4,1,2,6,167,2,0,510))
ibmServeRaidPowerSupplyFail.setObjects(*((_A,_B),(_A,_N),(_A,_C),(_A,_H)))
if mibBuilder.loadTexts:ibmServeRaidPowerSupplyFail.setStatus('')
ibmServeRaidPowerSupplyInstalled=NotificationType((1,3,6,1,4,1,2,6,167,2,0,511))
ibmServeRaidPowerSupplyInstalled.setObjects(*((_A,_B),(_A,_N),(_A,_C),(_A,_H)))
if mibBuilder.loadTexts:ibmServeRaidPowerSupplyInstalled.setStatus('')
ibmServeRaidPowerSupplyRemoved=NotificationType((1,3,6,1,4,1,2,6,167,2,0,512))
ibmServeRaidPowerSupplyRemoved.setObjects(*((_A,_B),(_A,_N),(_A,_C),(_A,_H)))
if mibBuilder.loadTexts:ibmServeRaidPowerSupplyRemoved.setStatus('')
ibmServeRaidTestTrap=NotificationType((1,3,6,1,4,1,2,6,167,2,0,601))
ibmServeRaidTestTrap.setObjects((_A,_B))
if mibBuilder.loadTexts:ibmServeRaidTestTrap.setStatus('')
mibBuilder.exportSymbols(_A,**{'ibm':ibm,'ibmProd':ibmProd,'ibmServeRaid':ibmServeRaid,'ibmServeRaidMIB':ibmServeRaidMIB,'ibmServeRaidNotifications':ibmServeRaidNotifications,'ibmServeRaidNoControllers':ibmServeRaidNoControllers,'ibmServeRaidControllerFail':ibmServeRaidControllerFail,'ibmServeRaidDeadBattery':ibmServeRaidDeadBattery,'ibmServeRaidDeadBatteryCache':ibmServeRaidDeadBatteryCache,'ibmServeRaidPollingFail':ibmServeRaidPollingFail,'ibmServeRaidConfigFail':ibmServeRaidConfigFail,'ibmServeRaidControllerAdded':ibmServeRaidControllerAdded,'ibmServeRaidControllerReplaced':ibmServeRaidControllerReplaced,'ibmServeRaidControllerFailover':ibmServeRaidControllerFailover,'ibmServeRaidControllerVersionMismatch':ibmServeRaidControllerVersionMismatch,'ibmServeRaidControllerBatteryOvertemp':ibmServeRaidControllerBatteryOvertemp,'ibmServeRaidLogicalDriveCritical':ibmServeRaidLogicalDriveCritical,'ibmServeRaidLogicalDriveBlocked':ibmServeRaidLogicalDriveBlocked,'ibmServeRaidLogicalDriveOffLine':ibmServeRaidLogicalDriveOffLine,'ibmServeRaidRebuildDetected':ibmServeRaidRebuildDetected,'ibmServeRaidRebuildComplete':ibmServeRaidRebuildComplete,'ibmServeRaidRebuildFail':ibmServeRaidRebuildFail,'ibmServeRaidSyncDetected':ibmServeRaidSyncDetected,'ibmServeRaidSyncComplete':ibmServeRaidSyncComplete,'ibmServeRaidSyncFail':ibmServeRaidSyncFail,'ibmServeRaidMigrationDetected':ibmServeRaidMigrationDetected,'ibmServeRaidMigrationComplete':ibmServeRaidMigrationComplete,'ibmServeRaidMigrationFail':ibmServeRaidMigrationFail,'ibmServeRaidCompressionDetected':ibmServeRaidCompressionDetected,'ibmServeRaidCompressionComplete':ibmServeRaidCompressionComplete,'ibmServeRaidcompressionFail':ibmServeRaidcompressionFail,'ibmServeRaidDecompressionDetected':ibmServeRaidDecompressionDetected,'ibmServeRaidDecompressionComplete':ibmServeRaidDecompressionComplete,'ibmServeRaidDecompressionFail':ibmServeRaidDecompressionFail,'ibmServeRaidFlashCopyDetected':ibmServeRaidFlashCopyDetected,'ibmServeRaidFlashCopyComplete':ibmServeRaidFlashCopyComplete,'ibmServeRaidFlashCopyFail':ibmServeRaidFlashCopyFail,'ibmServeRaidArrayRebuildDetected':ibmServeRaidArrayRebuildDetected,'ibmServeRaidArrayRebuildComplete':ibmServeRaidArrayRebuildComplete,'ibmServeRaidArrayRebuildFail':ibmServeRaidArrayRebuildFail,'ibmServeRaidArraySyncDetected':ibmServeRaidArraySyncDetected,'ibmServeRaidArraySyncComplete':ibmServeRaidArraySyncComplete,'ibmServeRaidArraySyncFail':ibmServeRaidArraySyncFail,'ibmServeRaidArrayFlashCopyDetected':ibmServeRaidArrayFlashCopyDetected,'ibmServeRaidArrayFlashCopyComplete':ibmServeRaidArrayFlashCopyComplete,'ibmServeRaidArrayFlashCopyFail':ibmServeRaidArrayFlashCopyFail,'ibmServeRaidLogicalDriveUnblocked':ibmServeRaidLogicalDriveUnblocked,'ibmServeRaidCompactionDetected':ibmServeRaidCompactionDetected,'ibmServeRaidCompactionComplete':ibmServeRaidCompactionComplete,'ibmServeRaidCompactionFail':ibmServeRaidCompactionFail,'ibmServeRaidExpansionDetected':ibmServeRaidExpansionDetected,'ibmServeRaidExpansionComplete':ibmServeRaidExpansionComplete,'ibmServeRaidExpansionFail':ibmServeRaidExpansionFail,'ibmServeRaidLogicalDriveCriticalPeriodic':ibmServeRaidLogicalDriveCriticalPeriodic,'ibmServeRaidDefunctDrive':ibmServeRaidDefunctDrive,'ibmServeRaidPfaDrive':ibmServeRaidPfaDrive,'ibmServeRaidDefunctReplaced':ibmServeRaidDefunctReplaced,'ibmServeRaidDefunctDriveFru':ibmServeRaidDefunctDriveFru,'ibmServeRaidPfaDriveFru':ibmServeRaidPfaDriveFru,'ibmServeRaidUnsupportedDrive':ibmServeRaidUnsupportedDrive,'ibmServeRaidEnclosureOK':ibmServeRaidEnclosureOK,'ibmServeRaidEnclosureFail':ibmServeRaidEnclosureFail,'ibmServeRaidFanOk':ibmServeRaidFanOk,'ibmServeRaidFanFail':ibmServeRaidFanFail,'ibmServeRaidFanInstalled':ibmServeRaidFanInstalled,'ibmServeRaidFanRemoved':ibmServeRaidFanRemoved,'ibmServeRaidTempOk':ibmServeRaidTempOk,'ibmServeRaidTempFail':ibmServeRaidTempFail,'ibmServeRaidPowerSupplyOk':ibmServeRaidPowerSupplyOk,'ibmServeRaidPowerSupplyFail':ibmServeRaidPowerSupplyFail,'ibmServeRaidPowerSupplyInstalled':ibmServeRaidPowerSupplyInstalled,'ibmServeRaidPowerSupplyRemoved':ibmServeRaidPowerSupplyRemoved,'ibmServeRaidTestTrap':ibmServeRaidTestTrap,'ibmServeRaidMibObjects':ibmServeRaidMibObjects,'ibmServeRaidAgentInfo':ibmServeRaidAgentInfo,'ibmServeRaidAgentKeyIndex':ibmServeRaidAgentKeyIndex,'ibmServeRaidAgentId':ibmServeRaidAgentId,'ibmServeRaidAgentCompany':ibmServeRaidAgentCompany,'ibmServeRaidAgentVersion':ibmServeRaidAgentVersion,'ibmServeRaidAgentBuildDate':ibmServeRaidAgentBuildDate,'ibmServeRaidAgentVersionMajor':ibmServeRaidAgentVersionMajor,'ibmServeRaidAgentVersionMinor':ibmServeRaidAgentVersionMinor,'ibmServeRaidInfo':ibmServeRaidInfo,'ibmServeRaidControllerTable':ibmServeRaidControllerTable,'ibmServeRaidControllerEntry':ibmServeRaidControllerEntry,_R:ibmServeRaidKeyIndex,'ibmServeRaidControllerId':ibmServeRaidControllerId,'ibmServeRaidModel':ibmServeRaidModel,'ibmServeRaidFirmwareVersion':ibmServeRaidFirmwareVersion,'ibmServeRaidBiosVersion':ibmServeRaidBiosVersion,'ibmServeRaidDefaultRebuildRate':ibmServeRaidDefaultRebuildRate,'ibmServeRaidNumChannels':ibmServeRaidNumChannels,'ibmServeRaidMaxChannels':ibmServeRaidMaxChannels,'ibmServeRaidNumLogicalDrives':ibmServeRaidNumLogicalDrives,'ibmServeRaidMaxLogicalDrives':ibmServeRaidMaxLogicalDrives,'ibmServeRaidNumPhysicalDevices':ibmServeRaidNumPhysicalDevices,'ibmServeRaidMaxPhysicalDevices':ibmServeRaidMaxPhysicalDevices,'ibmServeRaidStripeSize':ibmServeRaidStripeSize,'ibmServeRaidSlotNumber':ibmServeRaidSlotNumber,'ibmServeRaidVendorName':ibmServeRaidVendorName,'ibmServeRaidGeneralStatus':ibmServeRaidGeneralStatus,'ibmServeRaidPhysDeviceTable':ibmServeRaidPhysDeviceTable,'ibmServeRaidPhysDeviceEntry':ibmServeRaidPhysDeviceEntry,_S:ibmServeRaidPhysDeviceKeyIndex,'ibmServeRaidPhysDeviceControllerId':ibmServeRaidPhysDeviceControllerId,'ibmServeRaidPhysDeviceChannelNr':ibmServeRaidPhysDeviceChannelNr,'ibmServeRaidPhysDeviceDevNr':ibmServeRaidPhysDeviceDevNr,'ibmServeRaidPhysDeviceModel':ibmServeRaidPhysDeviceModel,'ibmServeRaidPhysDeviceCapacity':ibmServeRaidPhysDeviceCapacity,'ibmServeRaidPhysDeviceStatus':ibmServeRaidPhysDeviceStatus,'ibmServeRaidPhysDeviceDiskConfigured':ibmServeRaidPhysDeviceDiskConfigured,'ibmServeRaidPhysDeviceScsiType':ibmServeRaidPhysDeviceScsiType,'ibmServeRaidPhysDevicePfaStatus':ibmServeRaidPhysDevicePfaStatus,'ibmServeRaidLogicalTable':ibmServeRaidLogicalTable,'ibmServeRaidLogicalEntry':ibmServeRaidLogicalEntry,_U:ibmServeRaidLogicalKeyIndex,'ibmServeRaidLogicalControllerId':ibmServeRaidLogicalControllerId,'ibmServeRaidLogicalDriveNum':ibmServeRaidLogicalDriveNum,'ibmServeRaidLogicalStatus':ibmServeRaidLogicalStatus,'ibmServeRaidLogicalSize':ibmServeRaidLogicalSize,'ibmServeRaidLogicalRaidLevel':ibmServeRaidLogicalRaidLevel,'ibmServeRaidLogicalWriteCacheMode':ibmServeRaidLogicalWriteCacheMode,'ibmServeRaidTrapInfo':ibmServeRaidTrapInfo,_C:ibmServeRaidTrapController,_F:ibmServeRaidTrapLogicalDrive,_H:ibmServeRaidTrapChannel,_L:ibmServeRaidTrapScsiId,_M:ibmServeRaidTrapFan,_N:ibmServeRaidTrapPowerSupply,_I:ibmServeRaidTrapErrorCode,_B:ibmServeRaidTrapServerName,_K:ibmServeRaidTrapArray,_P:ibmServeRaidTrapFru,'ibmServeRaidConformance':ibmServeRaidConformance,'ibmServeRaidCompliances':ibmServeRaidCompliances,'ibmServeRaidCompliance':ibmServeRaidCompliance,'ibmServeRaidGroups':ibmServeRaidGroups,'ibmServeRaidAgentGroup':ibmServeRaidAgentGroup,'ibmServeRaidControllerGroup':ibmServeRaidControllerGroup,'ibmServeRaidPhysicalGroup':ibmServeRaidPhysicalGroup,'ibmServeRaidLogicalGroup':ibmServeRaidLogicalGroup,'ibmServeRaidTrapInfoGroup':ibmServeRaidTrapInfoGroup,'ibmServeRaidNotificationsGroup':ibmServeRaidNotificationsGroup})