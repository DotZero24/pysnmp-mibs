_A0='alvarionDeviceNotificationGroup'
_z='alvarionDeviceStatusMIBGroup'
_y='alvarionDeviceInformationMIBGroup'
_x='alvarionDeviceDiscoveryMIBGroup'
_w='alvarionDeviceConfigMIBGroup'
_v='coDeviceConfigurationFailureNotification'
_u='coDeviceFirmwareFailureNotification'
_t='coDeviceSecurityFailureNotification'
_s='coDeviceAuthorizationFailureNotification'
_r='coDeviceStateChangeNotification'
_q='coDevStStorageUseTemporary'
_p='coDevStStorageUsePermanent'
_o='coDevStRamCached'
_n='coDevStRamBuffer'
_m='coDevStRamFree'
_l='coDevStRamTotal'
_k='coDevStCpuUse20Sec'
_j='coDevStCpuUse10Sec'
_i='coDevStCpuUse5Sec'
_h='coDevStCpuUseNow'
_g='coDevStLoadAverage15Min'
_f='coDevStLoadAverage5Min'
_e='coDevStLoadAverage1Min'
_d='coDevStUpTime'
_c='coDevInfoHardwareRevision'
_b='coDevInfoBootRevision'
_a='coDevInfoFirmwareRevision'
_Z='coDevInfoProductName'
_Y='coDevInfoProductType'
_X='coDevDisConnectionTime'
_W='coDevDisGroupName'
_V='coDevDisContact'
_U='coDevDisLocation'
_T='coDevDisMacAddress'
_S='coDeviceConfigurationFailureNotificationEnabled'
_R='coDeviceFirmwareFailureNotificationEnabled'
_Q='coDeviceSecurityFailureNotificationEnabled'
_P='coDeviceAuthorizationFailureNotificationEnabled'
_O='coDeviceStateChangeNotificationEnabled'
_N='coDeviceStatusEntry'
_M='coDeviceInfoEntry'
_L='coDevDisIndex'
_K='Integer32'
_J='Kb'
_I='read-write'
_H='AlvarionNotificationEnable'
_G='coDevDisSystemName'
_F='coDevDisState'
_E='coDevDisIpAddress'
_D='coDevDisSerialNumber'
_C='read-only'
_B='current'
_A='ALVARION-DEVICE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alvarionMgmtV2,=mibBuilder.importSymbols('ALVARION-SMI','alvarionMgmtV2')
AlvarionNotificationEnable,=mibBuilder.importSymbols('ALVARION-TC',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
alvarionDeviceMIB=ModuleIdentity((1,3,6,1,4,1,12394,1,10,5,23))
_AlvarionDeviceMIBObjects_ObjectIdentity=ObjectIdentity
alvarionDeviceMIBObjects=_AlvarionDeviceMIBObjects_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,23,1))
_CoDeviceConfigGroup_ObjectIdentity=ObjectIdentity
coDeviceConfigGroup=_CoDeviceConfigGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,23,1,1))
class _CoDeviceStateChangeNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=2
_CoDeviceStateChangeNotificationEnabled_Type.__name__=_H
_CoDeviceStateChangeNotificationEnabled_Object=MibScalar
coDeviceStateChangeNotificationEnabled=_CoDeviceStateChangeNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,23,1,1,1),_CoDeviceStateChangeNotificationEnabled_Type())
coDeviceStateChangeNotificationEnabled.setMaxAccess(_I)
if mibBuilder.loadTexts:coDeviceStateChangeNotificationEnabled.setStatus(_B)
class _CoDeviceAuthorizationFailureNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=1
_CoDeviceAuthorizationFailureNotificationEnabled_Type.__name__=_H
_CoDeviceAuthorizationFailureNotificationEnabled_Object=MibScalar
coDeviceAuthorizationFailureNotificationEnabled=_CoDeviceAuthorizationFailureNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,23,1,1,2),_CoDeviceAuthorizationFailureNotificationEnabled_Type())
coDeviceAuthorizationFailureNotificationEnabled.setMaxAccess(_I)
if mibBuilder.loadTexts:coDeviceAuthorizationFailureNotificationEnabled.setStatus(_B)
class _CoDeviceSecurityFailureNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=1
_CoDeviceSecurityFailureNotificationEnabled_Type.__name__=_H
_CoDeviceSecurityFailureNotificationEnabled_Object=MibScalar
coDeviceSecurityFailureNotificationEnabled=_CoDeviceSecurityFailureNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,23,1,1,3),_CoDeviceSecurityFailureNotificationEnabled_Type())
coDeviceSecurityFailureNotificationEnabled.setMaxAccess(_I)
if mibBuilder.loadTexts:coDeviceSecurityFailureNotificationEnabled.setStatus(_B)
class _CoDeviceFirmwareFailureNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=1
_CoDeviceFirmwareFailureNotificationEnabled_Type.__name__=_H
_CoDeviceFirmwareFailureNotificationEnabled_Object=MibScalar
coDeviceFirmwareFailureNotificationEnabled=_CoDeviceFirmwareFailureNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,23,1,1,4),_CoDeviceFirmwareFailureNotificationEnabled_Type())
coDeviceFirmwareFailureNotificationEnabled.setMaxAccess(_I)
if mibBuilder.loadTexts:coDeviceFirmwareFailureNotificationEnabled.setStatus(_B)
class _CoDeviceConfigurationFailureNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=1
_CoDeviceConfigurationFailureNotificationEnabled_Type.__name__=_H
_CoDeviceConfigurationFailureNotificationEnabled_Object=MibScalar
coDeviceConfigurationFailureNotificationEnabled=_CoDeviceConfigurationFailureNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,23,1,1,5),_CoDeviceConfigurationFailureNotificationEnabled_Type())
coDeviceConfigurationFailureNotificationEnabled.setMaxAccess(_I)
if mibBuilder.loadTexts:coDeviceConfigurationFailureNotificationEnabled.setStatus(_B)
_CoDeviceDiscoveryGroup_ObjectIdentity=ObjectIdentity
coDeviceDiscoveryGroup=_CoDeviceDiscoveryGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,23,1,2))
_CoDeviceDiscoveryTable_Object=MibTable
coDeviceDiscoveryTable=_CoDeviceDiscoveryTable_Object((1,3,6,1,4,1,12394,1,10,5,23,1,2,1))
if mibBuilder.loadTexts:coDeviceDiscoveryTable.setStatus(_B)
_CoDeviceDiscoveryEntry_Object=MibTableRow
coDeviceDiscoveryEntry=_CoDeviceDiscoveryEntry_Object((1,3,6,1,4,1,12394,1,10,5,23,1,2,1,1))
coDeviceDiscoveryEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:coDeviceDiscoveryEntry.setStatus(_B)
class _CoDevDisIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CoDevDisIndex_Type.__name__=_K
_CoDevDisIndex_Object=MibTableColumn
coDevDisIndex=_CoDevDisIndex_Object((1,3,6,1,4,1,12394,1,10,5,23,1,2,1,1,1),_CoDevDisIndex_Type())
coDevDisIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:coDevDisIndex.setStatus(_B)
_CoDevDisSerialNumber_Type=DisplayString
_CoDevDisSerialNumber_Object=MibTableColumn
coDevDisSerialNumber=_CoDevDisSerialNumber_Object((1,3,6,1,4,1,12394,1,10,5,23,1,2,1,1,2),_CoDevDisSerialNumber_Type())
coDevDisSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevDisSerialNumber.setStatus(_B)
_CoDevDisMacAddress_Type=MacAddress
_CoDevDisMacAddress_Object=MibTableColumn
coDevDisMacAddress=_CoDevDisMacAddress_Object((1,3,6,1,4,1,12394,1,10,5,23,1,2,1,1,3),_CoDevDisMacAddress_Type())
coDevDisMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevDisMacAddress.setStatus(_B)
_CoDevDisIpAddress_Type=IpAddress
_CoDevDisIpAddress_Object=MibTableColumn
coDevDisIpAddress=_CoDevDisIpAddress_Object((1,3,6,1,4,1,12394,1,10,5,23,1,2,1,1,4),_CoDevDisIpAddress_Type())
coDevDisIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevDisIpAddress.setStatus(_B)
class _CoDevDisState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('disconnected',1),('authorized',2),('join',3),('firmware',4),('security',5),('configuration',6),('running',7)))
_CoDevDisState_Type.__name__=_K
_CoDevDisState_Object=MibTableColumn
coDevDisState=_CoDevDisState_Object((1,3,6,1,4,1,12394,1,10,5,23,1,2,1,1,5),_CoDevDisState_Type())
coDevDisState.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevDisState.setStatus(_B)
_CoDevDisSystemName_Type=DisplayString
_CoDevDisSystemName_Object=MibTableColumn
coDevDisSystemName=_CoDevDisSystemName_Object((1,3,6,1,4,1,12394,1,10,5,23,1,2,1,1,6),_CoDevDisSystemName_Type())
coDevDisSystemName.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevDisSystemName.setStatus(_B)
_CoDevDisLocation_Type=DisplayString
_CoDevDisLocation_Object=MibTableColumn
coDevDisLocation=_CoDevDisLocation_Object((1,3,6,1,4,1,12394,1,10,5,23,1,2,1,1,7),_CoDevDisLocation_Type())
coDevDisLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevDisLocation.setStatus(_B)
_CoDevDisContact_Type=DisplayString
_CoDevDisContact_Object=MibTableColumn
coDevDisContact=_CoDevDisContact_Object((1,3,6,1,4,1,12394,1,10,5,23,1,2,1,1,8),_CoDevDisContact_Type())
coDevDisContact.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevDisContact.setStatus(_B)
_CoDevDisGroupName_Type=DisplayString
_CoDevDisGroupName_Object=MibTableColumn
coDevDisGroupName=_CoDevDisGroupName_Object((1,3,6,1,4,1,12394,1,10,5,23,1,2,1,1,9),_CoDevDisGroupName_Type())
coDevDisGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevDisGroupName.setStatus(_B)
_CoDevDisConnectionTime_Type=Counter32
_CoDevDisConnectionTime_Object=MibTableColumn
coDevDisConnectionTime=_CoDevDisConnectionTime_Object((1,3,6,1,4,1,12394,1,10,5,23,1,2,1,1,10),_CoDevDisConnectionTime_Type())
coDevDisConnectionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevDisConnectionTime.setStatus(_B)
if mibBuilder.loadTexts:coDevDisConnectionTime.setUnits('minutes')
_CoDeviceInformationGroup_ObjectIdentity=ObjectIdentity
coDeviceInformationGroup=_CoDeviceInformationGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,23,1,3))
_CoDeviceInfoTable_Object=MibTable
coDeviceInfoTable=_CoDeviceInfoTable_Object((1,3,6,1,4,1,12394,1,10,5,23,1,3,1))
if mibBuilder.loadTexts:coDeviceInfoTable.setStatus(_B)
_CoDeviceInfoEntry_Object=MibTableRow
coDeviceInfoEntry=_CoDeviceInfoEntry_Object((1,3,6,1,4,1,12394,1,10,5,23,1,3,1,1))
if mibBuilder.loadTexts:coDeviceInfoEntry.setStatus(_B)
_CoDevInfoProductType_Type=ObjectIdentifier
_CoDevInfoProductType_Object=MibTableColumn
coDevInfoProductType=_CoDevInfoProductType_Object((1,3,6,1,4,1,12394,1,10,5,23,1,3,1,1,1),_CoDevInfoProductType_Type())
coDevInfoProductType.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevInfoProductType.setStatus(_B)
_CoDevInfoProductName_Type=DisplayString
_CoDevInfoProductName_Object=MibTableColumn
coDevInfoProductName=_CoDevInfoProductName_Object((1,3,6,1,4,1,12394,1,10,5,23,1,3,1,1,2),_CoDevInfoProductName_Type())
coDevInfoProductName.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevInfoProductName.setStatus(_B)
_CoDevInfoFirmwareRevision_Type=DisplayString
_CoDevInfoFirmwareRevision_Object=MibTableColumn
coDevInfoFirmwareRevision=_CoDevInfoFirmwareRevision_Object((1,3,6,1,4,1,12394,1,10,5,23,1,3,1,1,3),_CoDevInfoFirmwareRevision_Type())
coDevInfoFirmwareRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevInfoFirmwareRevision.setStatus(_B)
_CoDevInfoBootRevision_Type=DisplayString
_CoDevInfoBootRevision_Object=MibTableColumn
coDevInfoBootRevision=_CoDevInfoBootRevision_Object((1,3,6,1,4,1,12394,1,10,5,23,1,3,1,1,4),_CoDevInfoBootRevision_Type())
coDevInfoBootRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevInfoBootRevision.setStatus(_B)
_CoDevInfoHardwareRevision_Type=DisplayString
_CoDevInfoHardwareRevision_Object=MibTableColumn
coDevInfoHardwareRevision=_CoDevInfoHardwareRevision_Object((1,3,6,1,4,1,12394,1,10,5,23,1,3,1,1,5),_CoDevInfoHardwareRevision_Type())
coDevInfoHardwareRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevInfoHardwareRevision.setStatus(_B)
_CoDeviceStatusGroup_ObjectIdentity=ObjectIdentity
coDeviceStatusGroup=_CoDeviceStatusGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,23,1,4))
_CoDeviceStatusTable_Object=MibTable
coDeviceStatusTable=_CoDeviceStatusTable_Object((1,3,6,1,4,1,12394,1,10,5,23,1,4,1))
if mibBuilder.loadTexts:coDeviceStatusTable.setStatus(_B)
_CoDeviceStatusEntry_Object=MibTableRow
coDeviceStatusEntry=_CoDeviceStatusEntry_Object((1,3,6,1,4,1,12394,1,10,5,23,1,4,1,1))
if mibBuilder.loadTexts:coDeviceStatusEntry.setStatus(_B)
_CoDevStUpTime_Type=TimeTicks
_CoDevStUpTime_Object=MibTableColumn
coDevStUpTime=_CoDevStUpTime_Object((1,3,6,1,4,1,12394,1,10,5,23,1,4,1,1,1),_CoDevStUpTime_Type())
coDevStUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevStUpTime.setStatus(_B)
_CoDevStLoadAverage1Min_Type=Unsigned32
_CoDevStLoadAverage1Min_Object=MibTableColumn
coDevStLoadAverage1Min=_CoDevStLoadAverage1Min_Object((1,3,6,1,4,1,12394,1,10,5,23,1,4,1,1,2),_CoDevStLoadAverage1Min_Type())
coDevStLoadAverage1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevStLoadAverage1Min.setStatus(_B)
_CoDevStLoadAverage5Min_Type=Unsigned32
_CoDevStLoadAverage5Min_Object=MibTableColumn
coDevStLoadAverage5Min=_CoDevStLoadAverage5Min_Object((1,3,6,1,4,1,12394,1,10,5,23,1,4,1,1,3),_CoDevStLoadAverage5Min_Type())
coDevStLoadAverage5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevStLoadAverage5Min.setStatus(_B)
_CoDevStLoadAverage15Min_Type=Unsigned32
_CoDevStLoadAverage15Min_Object=MibTableColumn
coDevStLoadAverage15Min=_CoDevStLoadAverage15Min_Object((1,3,6,1,4,1,12394,1,10,5,23,1,4,1,1,4),_CoDevStLoadAverage15Min_Type())
coDevStLoadAverage15Min.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevStLoadAverage15Min.setStatus(_B)
_CoDevStCpuUseNow_Type=Unsigned32
_CoDevStCpuUseNow_Object=MibTableColumn
coDevStCpuUseNow=_CoDevStCpuUseNow_Object((1,3,6,1,4,1,12394,1,10,5,23,1,4,1,1,5),_CoDevStCpuUseNow_Type())
coDevStCpuUseNow.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevStCpuUseNow.setStatus(_B)
if mibBuilder.loadTexts:coDevStCpuUseNow.setUnits('%')
_CoDevStCpuUse5Sec_Type=Unsigned32
_CoDevStCpuUse5Sec_Object=MibTableColumn
coDevStCpuUse5Sec=_CoDevStCpuUse5Sec_Object((1,3,6,1,4,1,12394,1,10,5,23,1,4,1,1,6),_CoDevStCpuUse5Sec_Type())
coDevStCpuUse5Sec.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevStCpuUse5Sec.setStatus(_B)
if mibBuilder.loadTexts:coDevStCpuUse5Sec.setUnits('%')
_CoDevStCpuUse10Sec_Type=Unsigned32
_CoDevStCpuUse10Sec_Object=MibTableColumn
coDevStCpuUse10Sec=_CoDevStCpuUse10Sec_Object((1,3,6,1,4,1,12394,1,10,5,23,1,4,1,1,7),_CoDevStCpuUse10Sec_Type())
coDevStCpuUse10Sec.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevStCpuUse10Sec.setStatus(_B)
if mibBuilder.loadTexts:coDevStCpuUse10Sec.setUnits('%')
_CoDevStCpuUse20Sec_Type=Unsigned32
_CoDevStCpuUse20Sec_Object=MibTableColumn
coDevStCpuUse20Sec=_CoDevStCpuUse20Sec_Object((1,3,6,1,4,1,12394,1,10,5,23,1,4,1,1,8),_CoDevStCpuUse20Sec_Type())
coDevStCpuUse20Sec.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevStCpuUse20Sec.setStatus(_B)
if mibBuilder.loadTexts:coDevStCpuUse20Sec.setUnits('%')
_CoDevStRamTotal_Type=Unsigned32
_CoDevStRamTotal_Object=MibTableColumn
coDevStRamTotal=_CoDevStRamTotal_Object((1,3,6,1,4,1,12394,1,10,5,23,1,4,1,1,9),_CoDevStRamTotal_Type())
coDevStRamTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevStRamTotal.setStatus(_B)
if mibBuilder.loadTexts:coDevStRamTotal.setUnits(_J)
_CoDevStRamFree_Type=Unsigned32
_CoDevStRamFree_Object=MibTableColumn
coDevStRamFree=_CoDevStRamFree_Object((1,3,6,1,4,1,12394,1,10,5,23,1,4,1,1,10),_CoDevStRamFree_Type())
coDevStRamFree.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevStRamFree.setStatus(_B)
if mibBuilder.loadTexts:coDevStRamFree.setUnits(_J)
_CoDevStRamBuffer_Type=Unsigned32
_CoDevStRamBuffer_Object=MibTableColumn
coDevStRamBuffer=_CoDevStRamBuffer_Object((1,3,6,1,4,1,12394,1,10,5,23,1,4,1,1,11),_CoDevStRamBuffer_Type())
coDevStRamBuffer.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevStRamBuffer.setStatus(_B)
if mibBuilder.loadTexts:coDevStRamBuffer.setUnits(_J)
_CoDevStRamCached_Type=Unsigned32
_CoDevStRamCached_Object=MibTableColumn
coDevStRamCached=_CoDevStRamCached_Object((1,3,6,1,4,1,12394,1,10,5,23,1,4,1,1,12),_CoDevStRamCached_Type())
coDevStRamCached.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevStRamCached.setStatus(_B)
if mibBuilder.loadTexts:coDevStRamCached.setUnits(_J)
_CoDevStStorageUsePermanent_Type=Unsigned32
_CoDevStStorageUsePermanent_Object=MibTableColumn
coDevStStorageUsePermanent=_CoDevStStorageUsePermanent_Object((1,3,6,1,4,1,12394,1,10,5,23,1,4,1,1,13),_CoDevStStorageUsePermanent_Type())
coDevStStorageUsePermanent.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevStStorageUsePermanent.setStatus(_B)
if mibBuilder.loadTexts:coDevStStorageUsePermanent.setUnits('%')
_CoDevStStorageUseTemporary_Type=Unsigned32
_CoDevStStorageUseTemporary_Object=MibTableColumn
coDevStStorageUseTemporary=_CoDevStStorageUseTemporary_Object((1,3,6,1,4,1,12394,1,10,5,23,1,4,1,1,14),_CoDevStStorageUseTemporary_Type())
coDevStStorageUseTemporary.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevStStorageUseTemporary.setStatus(_B)
if mibBuilder.loadTexts:coDevStStorageUseTemporary.setUnits('%')
_AlvarionDeviceMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
alvarionDeviceMIBNotificationPrefix=_AlvarionDeviceMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,23,2))
_AlvarionDeviceMIBNotifications_ObjectIdentity=ObjectIdentity
alvarionDeviceMIBNotifications=_AlvarionDeviceMIBNotifications_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,23,2,0))
_AlvarionDeviceMIBConformance_ObjectIdentity=ObjectIdentity
alvarionDeviceMIBConformance=_AlvarionDeviceMIBConformance_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,23,3))
_AlvarionDeviceMIBCompliances_ObjectIdentity=ObjectIdentity
alvarionDeviceMIBCompliances=_AlvarionDeviceMIBCompliances_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,23,3,1))
_AlvarionDeviceMIBGroups_ObjectIdentity=ObjectIdentity
alvarionDeviceMIBGroups=_AlvarionDeviceMIBGroups_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,23,3,2))
coDeviceDiscoveryEntry.registerAugmentions((_A,_M))
coDeviceInfoEntry.setIndexNames(*coDeviceDiscoveryEntry.getIndexNames())
coDeviceDiscoveryEntry.registerAugmentions((_A,_N))
coDeviceStatusEntry.setIndexNames(*coDeviceDiscoveryEntry.getIndexNames())
alvarionDeviceConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,23,3,2,1))
alvarionDeviceConfigMIBGroup.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:alvarionDeviceConfigMIBGroup.setStatus(_B)
alvarionDeviceDiscoveryMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,23,3,2,2))
alvarionDeviceDiscoveryMIBGroup.setObjects(*((_A,_D),(_A,_T),(_A,_E),(_A,_F),(_A,_G),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:alvarionDeviceDiscoveryMIBGroup.setStatus(_B)
alvarionDeviceInformationMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,23,3,2,3))
alvarionDeviceInformationMIBGroup.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:alvarionDeviceInformationMIBGroup.setStatus(_B)
alvarionDeviceStatusMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,23,3,2,4))
alvarionDeviceStatusMIBGroup.setObjects(*((_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:alvarionDeviceStatusMIBGroup.setStatus(_B)
coDeviceStateChangeNotification=NotificationType((1,3,6,1,4,1,12394,1,10,5,23,2,0,1))
coDeviceStateChangeNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:coDeviceStateChangeNotification.setStatus(_B)
coDeviceAuthorizationFailureNotification=NotificationType((1,3,6,1,4,1,12394,1,10,5,23,2,0,2))
coDeviceAuthorizationFailureNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:coDeviceAuthorizationFailureNotification.setStatus(_B)
coDeviceSecurityFailureNotification=NotificationType((1,3,6,1,4,1,12394,1,10,5,23,2,0,3))
coDeviceSecurityFailureNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:coDeviceSecurityFailureNotification.setStatus(_B)
coDeviceFirmwareFailureNotification=NotificationType((1,3,6,1,4,1,12394,1,10,5,23,2,0,4))
coDeviceFirmwareFailureNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:coDeviceFirmwareFailureNotification.setStatus(_B)
coDeviceConfigurationFailureNotification=NotificationType((1,3,6,1,4,1,12394,1,10,5,23,2,0,5))
coDeviceConfigurationFailureNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:coDeviceConfigurationFailureNotification.setStatus(_B)
alvarionDeviceNotificationGroup=NotificationGroup((1,3,6,1,4,1,12394,1,10,5,23,3,2,5))
alvarionDeviceNotificationGroup.setObjects(*((_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:alvarionDeviceNotificationGroup.setStatus(_B)
alvarionDeviceMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12394,1,10,5,23,3,1,1))
alvarionDeviceMIBCompliance.setObjects(*((_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:alvarionDeviceMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'alvarionDeviceMIB':alvarionDeviceMIB,'alvarionDeviceMIBObjects':alvarionDeviceMIBObjects,'coDeviceConfigGroup':coDeviceConfigGroup,_O:coDeviceStateChangeNotificationEnabled,_P:coDeviceAuthorizationFailureNotificationEnabled,_Q:coDeviceSecurityFailureNotificationEnabled,_R:coDeviceFirmwareFailureNotificationEnabled,_S:coDeviceConfigurationFailureNotificationEnabled,'coDeviceDiscoveryGroup':coDeviceDiscoveryGroup,'coDeviceDiscoveryTable':coDeviceDiscoveryTable,'coDeviceDiscoveryEntry':coDeviceDiscoveryEntry,_L:coDevDisIndex,_D:coDevDisSerialNumber,_T:coDevDisMacAddress,_E:coDevDisIpAddress,_F:coDevDisState,_G:coDevDisSystemName,_U:coDevDisLocation,_V:coDevDisContact,_W:coDevDisGroupName,_X:coDevDisConnectionTime,'coDeviceInformationGroup':coDeviceInformationGroup,'coDeviceInfoTable':coDeviceInfoTable,_M:coDeviceInfoEntry,_Y:coDevInfoProductType,_Z:coDevInfoProductName,_a:coDevInfoFirmwareRevision,_b:coDevInfoBootRevision,_c:coDevInfoHardwareRevision,'coDeviceStatusGroup':coDeviceStatusGroup,'coDeviceStatusTable':coDeviceStatusTable,_N:coDeviceStatusEntry,_d:coDevStUpTime,_e:coDevStLoadAverage1Min,_f:coDevStLoadAverage5Min,_g:coDevStLoadAverage15Min,_h:coDevStCpuUseNow,_i:coDevStCpuUse5Sec,_j:coDevStCpuUse10Sec,_k:coDevStCpuUse20Sec,_l:coDevStRamTotal,_m:coDevStRamFree,_n:coDevStRamBuffer,_o:coDevStRamCached,_p:coDevStStorageUsePermanent,_q:coDevStStorageUseTemporary,'alvarionDeviceMIBNotificationPrefix':alvarionDeviceMIBNotificationPrefix,'alvarionDeviceMIBNotifications':alvarionDeviceMIBNotifications,_r:coDeviceStateChangeNotification,_s:coDeviceAuthorizationFailureNotification,_t:coDeviceSecurityFailureNotification,_u:coDeviceFirmwareFailureNotification,_v:coDeviceConfigurationFailureNotification,'alvarionDeviceMIBConformance':alvarionDeviceMIBConformance,'alvarionDeviceMIBCompliances':alvarionDeviceMIBCompliances,'alvarionDeviceMIBCompliance':alvarionDeviceMIBCompliance,'alvarionDeviceMIBGroups':alvarionDeviceMIBGroups,_w:alvarionDeviceConfigMIBGroup,_x:alvarionDeviceDiscoveryMIBGroup,_y:alvarionDeviceInformationMIBGroup,_z:alvarionDeviceStatusMIBGroup,_A0:alvarionDeviceNotificationGroup})