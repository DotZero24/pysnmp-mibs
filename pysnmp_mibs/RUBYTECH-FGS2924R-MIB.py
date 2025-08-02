_A4='fgs2924rDhcpSnoopingClientIndex'
_A3='fgs2924rDhcpSnoopingIndex'
_A2='fgs2924rMVRGroupNo'
_A1='fgs2924rMVIDGroupAllowNo'
_A0='fgs2924rMVID'
_z='fgs2924rIgmpSnoopingGroupNo'
_y='fgs2924rIgmpProxyGroupNo'
_x='fgs2924rIGMPGroupAllowNo'
_w='fgs2924rAggregatorViewIndex'
_v='fgs2924rTrunkPortIndex'
_u='fgs2924rDot1XStatisticsIndex'
_t='fgs2924rDot1XStatusIndex'
_s='fgs2924rDot1XPort'
_r='fgs2924rIpMacBindSettingIndex'
_q='fgs2924rAclInfoViewNo'
_p='fgs2924rAclRateLimiterIndex'
_o='fgs2924rAclPortsConfIndex'
_n='fgs2924rQosQclQceListNo'
_m='fgs2924rQosQclNo'
_l='fgs2924rQosRateLimitersIndex'
_k='fgs2924rQosPortConfIndex'
_j='fgs2924rGvrpGroupAdministrativeCtrlPort'
_i='fgs2924rGvrpGroupAdministrativeCtrlVid'
_h='fgs2924rGvrpGroupId'
_g='fgs2924rGvrpCounterIndex'
_f='fgs2924rGvrpConfIndex'
_e='fgs2924rMacAliasIndex'
_d='fgs2924rMacTableStaticForwardIndex'
_c='fgs2924rMacTableStaticFilterIndex'
_b='fgs2924rMacTableLearningConfIndex'
_a='fgs2924rPortBaseVlanGroupIndex'
_Z='fgs2924rVlanPortConfIndex'
_Y='fgs2924rTagBaseVlanVid'
_X='fgs2924rManagementSecurityIndex'
_W='fgs2924rLoopDetectedfIndex'
_V='fgs2924rMaxPktLenConfIndex'
_U='fgs2924rMirroredPortIndex'
_T='fgs2924rSFPInfoIndex'
_S='fgs2924rPortConfIndex'
_R='fgs2924rPortStatusIndex'
_Q='fgs2924rLogIndex'
_P='fgs2924rEmailUserIndex'
_O='fgs2924rEventIndex'
_N='fgs2924rTrapHostIndex'
_M='fgs2924rAccountIndex'
_L='partnerkey'
_K='actorkey'
_J='groupId'
_I='username'
_H='ifIndex'
_G='IF-MIB'
_F='not-accessible'
_E='RUBYTECH-FGS2924R-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
MacAddress,=mibBuilder.importSymbols('BRIDGE-MIB','MacAddress')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rubytech=ModuleIdentity((1,3,6,1,4,1,5205))
_Switch_ObjectIdentity=ObjectIdentity
switch=_Switch_ObjectIdentity((1,3,6,1,4,1,5205,2))
_Fgs2924rProductID_ObjectIdentity=ObjectIdentity
fgs2924rProductID=_Fgs2924rProductID_ObjectIdentity((1,3,6,1,4,1,5205,2,34))
_Fgs2924rProduces_ObjectIdentity=ObjectIdentity
fgs2924rProduces=_Fgs2924rProduces_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1))
_Fgs2924rSystem_ObjectIdentity=ObjectIdentity
fgs2924rSystem=_Fgs2924rSystem_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,1))
_Fgs2924rCommonSys_ObjectIdentity=ObjectIdentity
fgs2924rCommonSys=_Fgs2924rCommonSys_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,1,1))
class _Fgs2924rReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rReboot_Type.__name__=_C
_Fgs2924rReboot_Object=MibScalar
fgs2924rReboot=_Fgs2924rReboot_Object((1,3,6,1,4,1,5205,2,34,1,1,1,1),_Fgs2924rReboot_Type())
fgs2924rReboot.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rReboot.setStatus(_A)
_Fgs2924rBiosVsersion_Type=DisplayString
_Fgs2924rBiosVsersion_Object=MibScalar
fgs2924rBiosVsersion=_Fgs2924rBiosVsersion_Object((1,3,6,1,4,1,5205,2,34,1,1,1,2),_Fgs2924rBiosVsersion_Type())
fgs2924rBiosVsersion.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rBiosVsersion.setStatus(_A)
_Fgs2924rFirmwareVersion_Type=DisplayString
_Fgs2924rFirmwareVersion_Object=MibScalar
fgs2924rFirmwareVersion=_Fgs2924rFirmwareVersion_Object((1,3,6,1,4,1,5205,2,34,1,1,1,3),_Fgs2924rFirmwareVersion_Type())
fgs2924rFirmwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rFirmwareVersion.setStatus(_A)
_Fgs2924rHardwareVersion_Type=DisplayString
_Fgs2924rHardwareVersion_Object=MibScalar
fgs2924rHardwareVersion=_Fgs2924rHardwareVersion_Object((1,3,6,1,4,1,5205,2,34,1,1,1,4),_Fgs2924rHardwareVersion_Type())
fgs2924rHardwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rHardwareVersion.setStatus(_A)
_Fgs2924rMechanicalVersion_Type=DisplayString
_Fgs2924rMechanicalVersion_Object=MibScalar
fgs2924rMechanicalVersion=_Fgs2924rMechanicalVersion_Object((1,3,6,1,4,1,5205,2,34,1,1,1,5),_Fgs2924rMechanicalVersion_Type())
fgs2924rMechanicalVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rMechanicalVersion.setStatus(_A)
_Fgs2924rSerialNumber_Type=DisplayString
_Fgs2924rSerialNumber_Object=MibScalar
fgs2924rSerialNumber=_Fgs2924rSerialNumber_Object((1,3,6,1,4,1,5205,2,34,1,1,1,6),_Fgs2924rSerialNumber_Type())
fgs2924rSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rSerialNumber.setStatus(_A)
_Fgs2924rHostMacAddress_Type=DisplayString
_Fgs2924rHostMacAddress_Object=MibScalar
fgs2924rHostMacAddress=_Fgs2924rHostMacAddress_Object((1,3,6,1,4,1,5205,2,34,1,1,1,7),_Fgs2924rHostMacAddress_Type())
fgs2924rHostMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rHostMacAddress.setStatus(_A)
_Fgs2924rDevicePort_Type=DisplayString
_Fgs2924rDevicePort_Object=MibScalar
fgs2924rDevicePort=_Fgs2924rDevicePort_Object((1,3,6,1,4,1,5205,2,34,1,1,1,8),_Fgs2924rDevicePort_Type())
fgs2924rDevicePort.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDevicePort.setStatus(_A)
_Fgs2924rRamSize_Type=DisplayString
_Fgs2924rRamSize_Object=MibScalar
fgs2924rRamSize=_Fgs2924rRamSize_Object((1,3,6,1,4,1,5205,2,34,1,1,1,9),_Fgs2924rRamSize_Type())
fgs2924rRamSize.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rRamSize.setStatus(_A)
_Fgs2924rFlashSize_Type=DisplayString
_Fgs2924rFlashSize_Object=MibScalar
fgs2924rFlashSize=_Fgs2924rFlashSize_Object((1,3,6,1,4,1,5205,2,34,1,1,1,10),_Fgs2924rFlashSize_Type())
fgs2924rFlashSize.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rFlashSize.setStatus(_A)
_Fgs2924rDeviceName_Type=DisplayString
_Fgs2924rDeviceName_Object=MibScalar
fgs2924rDeviceName=_Fgs2924rDeviceName_Object((1,3,6,1,4,1,5205,2,34,1,1,1,11),_Fgs2924rDeviceName_Type())
fgs2924rDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDeviceName.setStatus(_A)
_Fgs2924rSystemDescription_Type=DisplayString
_Fgs2924rSystemDescription_Object=MibScalar
fgs2924rSystemDescription=_Fgs2924rSystemDescription_Object((1,3,6,1,4,1,5205,2,34,1,1,1,12),_Fgs2924rSystemDescription_Type())
fgs2924rSystemDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rSystemDescription.setStatus(_A)
_Fgs2924rCpuLoad_Type=DisplayString
_Fgs2924rCpuLoad_Object=MibScalar
fgs2924rCpuLoad=_Fgs2924rCpuLoad_Object((1,3,6,1,4,1,5205,2,34,1,1,1,13),_Fgs2924rCpuLoad_Type())
fgs2924rCpuLoad.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rCpuLoad.setStatus(_A)
_Fgs2924rIP_ObjectIdentity=ObjectIdentity
fgs2924rIP=_Fgs2924rIP_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,1,2))
class _Fgs2924rDhcpSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rDhcpSetting_Type.__name__=_C
_Fgs2924rDhcpSetting_Object=MibScalar
fgs2924rDhcpSetting=_Fgs2924rDhcpSetting_Object((1,3,6,1,4,1,5205,2,34,1,1,2,1),_Fgs2924rDhcpSetting_Type())
fgs2924rDhcpSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDhcpSetting.setStatus(_A)
_Fgs2924rIPAddress_Type=IpAddress
_Fgs2924rIPAddress_Object=MibScalar
fgs2924rIPAddress=_Fgs2924rIPAddress_Object((1,3,6,1,4,1,5205,2,34,1,1,2,2),_Fgs2924rIPAddress_Type())
fgs2924rIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIPAddress.setStatus(_A)
_Fgs2924rNetMask_Type=IpAddress
_Fgs2924rNetMask_Object=MibScalar
fgs2924rNetMask=_Fgs2924rNetMask_Object((1,3,6,1,4,1,5205,2,34,1,1,2,3),_Fgs2924rNetMask_Type())
fgs2924rNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rNetMask.setStatus(_A)
_Fgs2924rDefaultGateway_Type=IpAddress
_Fgs2924rDefaultGateway_Object=MibScalar
fgs2924rDefaultGateway=_Fgs2924rDefaultGateway_Object((1,3,6,1,4,1,5205,2,34,1,1,2,4),_Fgs2924rDefaultGateway_Type())
fgs2924rDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDefaultGateway.setStatus(_A)
class _Fgs2924rDnsConf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rDnsConf_Type.__name__=_C
_Fgs2924rDnsConf_Object=MibScalar
fgs2924rDnsConf=_Fgs2924rDnsConf_Object((1,3,6,1,4,1,5205,2,34,1,1,2,5),_Fgs2924rDnsConf_Type())
fgs2924rDnsConf.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDnsConf.setStatus(_A)
class _Fgs2924rDnsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rDnsState_Type.__name__=_C
_Fgs2924rDnsState_Object=MibScalar
fgs2924rDnsState=_Fgs2924rDnsState_Object((1,3,6,1,4,1,5205,2,34,1,1,2,6),_Fgs2924rDnsState_Type())
fgs2924rDnsState.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDnsState.setStatus(_A)
_Fgs2924rDnsServer_Type=IpAddress
_Fgs2924rDnsServer_Object=MibScalar
fgs2924rDnsServer=_Fgs2924rDnsServer_Object((1,3,6,1,4,1,5205,2,34,1,1,2,7),_Fgs2924rDnsServer_Type())
fgs2924rDnsServer.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDnsServer.setStatus(_A)
_Fgs2924rTime_ObjectIdentity=ObjectIdentity
fgs2924rTime=_Fgs2924rTime_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,1,3))
_Fgs2924rSystemCurrentTime_Type=DisplayString
_Fgs2924rSystemCurrentTime_Object=MibScalar
fgs2924rSystemCurrentTime=_Fgs2924rSystemCurrentTime_Object((1,3,6,1,4,1,5205,2,34,1,1,3,1),_Fgs2924rSystemCurrentTime_Type())
fgs2924rSystemCurrentTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rSystemCurrentTime.setStatus(_A)
_Fgs2924rManualTimeSetting_Type=DisplayString
_Fgs2924rManualTimeSetting_Object=MibScalar
fgs2924rManualTimeSetting=_Fgs2924rManualTimeSetting_Object((1,3,6,1,4,1,5205,2,34,1,1,3,2),_Fgs2924rManualTimeSetting_Type())
fgs2924rManualTimeSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rManualTimeSetting.setStatus(_A)
_Fgs2924rNTPServer_Type=DisplayString
_Fgs2924rNTPServer_Object=MibScalar
fgs2924rNTPServer=_Fgs2924rNTPServer_Object((1,3,6,1,4,1,5205,2,34,1,1,3,3),_Fgs2924rNTPServer_Type())
fgs2924rNTPServer.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rNTPServer.setStatus(_A)
class _Fgs2924rNTPTimeZone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-12,13))
_Fgs2924rNTPTimeZone_Type.__name__=_C
_Fgs2924rNTPTimeZone_Object=MibScalar
fgs2924rNTPTimeZone=_Fgs2924rNTPTimeZone_Object((1,3,6,1,4,1,5205,2,34,1,1,3,4),_Fgs2924rNTPTimeZone_Type())
fgs2924rNTPTimeZone.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rNTPTimeZone.setStatus(_A)
class _Fgs2924rNTPTimeSync_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rNTPTimeSync_Type.__name__=_C
_Fgs2924rNTPTimeSync_Object=MibScalar
fgs2924rNTPTimeSync=_Fgs2924rNTPTimeSync_Object((1,3,6,1,4,1,5205,2,34,1,1,3,5),_Fgs2924rNTPTimeSync_Type())
fgs2924rNTPTimeSync.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rNTPTimeSync.setStatus(_A)
class _Fgs2924rDaylightSavingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5,5))
_Fgs2924rDaylightSavingTime_Type.__name__=_C
_Fgs2924rDaylightSavingTime_Object=MibScalar
fgs2924rDaylightSavingTime=_Fgs2924rDaylightSavingTime_Object((1,3,6,1,4,1,5205,2,34,1,1,3,6),_Fgs2924rDaylightSavingTime_Type())
fgs2924rDaylightSavingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDaylightSavingTime.setStatus(_A)
_Fgs2924rDaylightStartTime_Type=DisplayString
_Fgs2924rDaylightStartTime_Object=MibScalar
fgs2924rDaylightStartTime=_Fgs2924rDaylightStartTime_Object((1,3,6,1,4,1,5205,2,34,1,1,3,7),_Fgs2924rDaylightStartTime_Type())
fgs2924rDaylightStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDaylightStartTime.setStatus(_A)
_Fgs2924rDaylightEndTime_Type=DisplayString
_Fgs2924rDaylightEndTime_Object=MibScalar
fgs2924rDaylightEndTime=_Fgs2924rDaylightEndTime_Object((1,3,6,1,4,1,5205,2,34,1,1,3,8),_Fgs2924rDaylightEndTime_Type())
fgs2924rDaylightEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDaylightEndTime.setStatus(_A)
_Fgs2924rAccount_ObjectIdentity=ObjectIdentity
fgs2924rAccount=_Fgs2924rAccount_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,1,4))
class _Fgs2924rAccountNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Fgs2924rAccountNumber_Type.__name__=_C
_Fgs2924rAccountNumber_Object=MibScalar
fgs2924rAccountNumber=_Fgs2924rAccountNumber_Object((1,3,6,1,4,1,5205,2,34,1,1,4,1),_Fgs2924rAccountNumber_Type())
fgs2924rAccountNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rAccountNumber.setStatus(_A)
_Fgs2924rAccountTable_Object=MibTable
fgs2924rAccountTable=_Fgs2924rAccountTable_Object((1,3,6,1,4,1,5205,2,34,1,1,4,2))
if mibBuilder.loadTexts:fgs2924rAccountTable.setStatus(_A)
_Fgs2924rAccountEntry_Object=MibTableRow
fgs2924rAccountEntry=_Fgs2924rAccountEntry_Object((1,3,6,1,4,1,5205,2,34,1,1,4,2,1))
fgs2924rAccountEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:fgs2924rAccountEntry.setStatus(_A)
class _Fgs2924rAccountIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Fgs2924rAccountIndex_Type.__name__=_C
_Fgs2924rAccountIndex_Object=MibTableColumn
fgs2924rAccountIndex=_Fgs2924rAccountIndex_Object((1,3,6,1,4,1,5205,2,34,1,1,4,2,1,1),_Fgs2924rAccountIndex_Type())
fgs2924rAccountIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rAccountIndex.setStatus(_A)
_Fgs2924rAccountAuthorization_Type=DisplayString
_Fgs2924rAccountAuthorization_Object=MibTableColumn
fgs2924rAccountAuthorization=_Fgs2924rAccountAuthorization_Object((1,3,6,1,4,1,5205,2,34,1,1,4,2,1,2),_Fgs2924rAccountAuthorization_Type())
fgs2924rAccountAuthorization.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rAccountAuthorization.setStatus(_A)
_Fgs2924rAccountName_Type=DisplayString
_Fgs2924rAccountName_Object=MibTableColumn
fgs2924rAccountName=_Fgs2924rAccountName_Object((1,3,6,1,4,1,5205,2,34,1,1,4,2,1,3),_Fgs2924rAccountName_Type())
fgs2924rAccountName.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAccountName.setStatus(_A)
_Fgs2924rAccountPassword_Type=DisplayString
_Fgs2924rAccountPassword_Object=MibTableColumn
fgs2924rAccountPassword=_Fgs2924rAccountPassword_Object((1,3,6,1,4,1,5205,2,34,1,1,4,2,1,4),_Fgs2924rAccountPassword_Type())
fgs2924rAccountPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAccountPassword.setStatus(_A)
class _Fgs2924rAccountAddAuthorization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Fgs2924rAccountAddAuthorization_Type.__name__=_C
_Fgs2924rAccountAddAuthorization_Object=MibScalar
fgs2924rAccountAddAuthorization=_Fgs2924rAccountAddAuthorization_Object((1,3,6,1,4,1,5205,2,34,1,1,4,3),_Fgs2924rAccountAddAuthorization_Type())
fgs2924rAccountAddAuthorization.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAccountAddAuthorization.setStatus(_A)
_Fgs2924rAccountAddName_Type=DisplayString
_Fgs2924rAccountAddName_Object=MibScalar
fgs2924rAccountAddName=_Fgs2924rAccountAddName_Object((1,3,6,1,4,1,5205,2,34,1,1,4,4),_Fgs2924rAccountAddName_Type())
fgs2924rAccountAddName.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAccountAddName.setStatus(_A)
_Fgs2924rAccountAddPassword_Type=DisplayString
_Fgs2924rAccountAddPassword_Object=MibScalar
fgs2924rAccountAddPassword=_Fgs2924rAccountAddPassword_Object((1,3,6,1,4,1,5205,2,34,1,1,4,5),_Fgs2924rAccountAddPassword_Type())
fgs2924rAccountAddPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAccountAddPassword.setStatus(_A)
class _Fgs2924rDoAccountAdd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rDoAccountAdd_Type.__name__=_C
_Fgs2924rDoAccountAdd_Object=MibScalar
fgs2924rDoAccountAdd=_Fgs2924rDoAccountAdd_Object((1,3,6,1,4,1,5205,2,34,1,1,4,6),_Fgs2924rDoAccountAdd_Type())
fgs2924rDoAccountAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDoAccountAdd.setStatus(_A)
class _Fgs2924rAccountDel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,5))
_Fgs2924rAccountDel_Type.__name__=_C
_Fgs2924rAccountDel_Object=MibScalar
fgs2924rAccountDel=_Fgs2924rAccountDel_Object((1,3,6,1,4,1,5205,2,34,1,1,4,7),_Fgs2924rAccountDel_Type())
fgs2924rAccountDel.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAccountDel.setStatus(_A)
_Fgs2924rVsm_ObjectIdentity=ObjectIdentity
fgs2924rVsm=_Fgs2924rVsm_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,1,5))
class _Fgs2924rVsmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rVsmState_Type.__name__=_C
_Fgs2924rVsmState_Object=MibScalar
fgs2924rVsmState=_Fgs2924rVsmState_Object((1,3,6,1,4,1,5205,2,34,1,1,5,1),_Fgs2924rVsmState_Type())
fgs2924rVsmState.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rVsmState.setStatus(_A)
class _Fgs2924rVsmRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rVsmRole_Type.__name__=_C
_Fgs2924rVsmRole_Object=MibScalar
fgs2924rVsmRole=_Fgs2924rVsmRole_Object((1,3,6,1,4,1,5205,2,34,1,1,5,2),_Fgs2924rVsmRole_Type())
fgs2924rVsmRole.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rVsmRole.setStatus(_A)
_Fgs2924rVsmGroupid_Type=DisplayString
_Fgs2924rVsmGroupid_Object=MibScalar
fgs2924rVsmGroupid=_Fgs2924rVsmGroupid_Object((1,3,6,1,4,1,5205,2,34,1,1,5,3),_Fgs2924rVsmGroupid_Type())
fgs2924rVsmGroupid.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rVsmGroupid.setStatus(_A)
_Fgs2924rSnmp_ObjectIdentity=ObjectIdentity
fgs2924rSnmp=_Fgs2924rSnmp_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,2))
_Fgs2924rGetCommunity_Type=DisplayString
_Fgs2924rGetCommunity_Object=MibScalar
fgs2924rGetCommunity=_Fgs2924rGetCommunity_Object((1,3,6,1,4,1,5205,2,34,1,2,1),_Fgs2924rGetCommunity_Type())
fgs2924rGetCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rGetCommunity.setStatus(_A)
_Fgs2924rSetCommunity_Type=DisplayString
_Fgs2924rSetCommunity_Object=MibScalar
fgs2924rSetCommunity=_Fgs2924rSetCommunity_Object((1,3,6,1,4,1,5205,2,34,1,2,2),_Fgs2924rSetCommunity_Type())
fgs2924rSetCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rSetCommunity.setStatus(_A)
class _Fgs2924rTrapHostNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_Fgs2924rTrapHostNumber_Type.__name__=_C
_Fgs2924rTrapHostNumber_Object=MibScalar
fgs2924rTrapHostNumber=_Fgs2924rTrapHostNumber_Object((1,3,6,1,4,1,5205,2,34,1,2,3),_Fgs2924rTrapHostNumber_Type())
fgs2924rTrapHostNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rTrapHostNumber.setStatus(_A)
_Fgs2924rTrapHostTable_Object=MibTable
fgs2924rTrapHostTable=_Fgs2924rTrapHostTable_Object((1,3,6,1,4,1,5205,2,34,1,2,4))
if mibBuilder.loadTexts:fgs2924rTrapHostTable.setStatus(_A)
_Fgs2924rTrapHostEntry_Object=MibTableRow
fgs2924rTrapHostEntry=_Fgs2924rTrapHostEntry_Object((1,3,6,1,4,1,5205,2,34,1,2,4,1))
fgs2924rTrapHostEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:fgs2924rTrapHostEntry.setStatus(_A)
class _Fgs2924rTrapHostIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_Fgs2924rTrapHostIndex_Type.__name__=_C
_Fgs2924rTrapHostIndex_Object=MibTableColumn
fgs2924rTrapHostIndex=_Fgs2924rTrapHostIndex_Object((1,3,6,1,4,1,5205,2,34,1,2,4,1,1),_Fgs2924rTrapHostIndex_Type())
fgs2924rTrapHostIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rTrapHostIndex.setStatus(_A)
_Fgs2924rTrapHostIP_Type=IpAddress
_Fgs2924rTrapHostIP_Object=MibTableColumn
fgs2924rTrapHostIP=_Fgs2924rTrapHostIP_Object((1,3,6,1,4,1,5205,2,34,1,2,4,1,2),_Fgs2924rTrapHostIP_Type())
fgs2924rTrapHostIP.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rTrapHostIP.setStatus(_A)
class _Fgs2924rTrapHostPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Fgs2924rTrapHostPort_Type.__name__=_C
_Fgs2924rTrapHostPort_Object=MibTableColumn
fgs2924rTrapHostPort=_Fgs2924rTrapHostPort_Object((1,3,6,1,4,1,5205,2,34,1,2,4,1,3),_Fgs2924rTrapHostPort_Type())
fgs2924rTrapHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rTrapHostPort.setStatus(_A)
_Fgs2924rTrapHostCommunity_Type=DisplayString
_Fgs2924rTrapHostCommunity_Object=MibTableColumn
fgs2924rTrapHostCommunity=_Fgs2924rTrapHostCommunity_Object((1,3,6,1,4,1,5205,2,34,1,2,4,1,4),_Fgs2924rTrapHostCommunity_Type())
fgs2924rTrapHostCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rTrapHostCommunity.setStatus(_A)
_Fgs2924rAlarm_ObjectIdentity=ObjectIdentity
fgs2924rAlarm=_Fgs2924rAlarm_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,3))
_Fgs2924rEvent_ObjectIdentity=ObjectIdentity
fgs2924rEvent=_Fgs2924rEvent_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,3,1))
class _Fgs2924rEventNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Fgs2924rEventNumber_Type.__name__=_C
_Fgs2924rEventNumber_Object=MibScalar
fgs2924rEventNumber=_Fgs2924rEventNumber_Object((1,3,6,1,4,1,5205,2,34,1,3,1,1),_Fgs2924rEventNumber_Type())
fgs2924rEventNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rEventNumber.setStatus(_A)
_Fgs2924rEventTable_Object=MibTable
fgs2924rEventTable=_Fgs2924rEventTable_Object((1,3,6,1,4,1,5205,2,34,1,3,1,2))
if mibBuilder.loadTexts:fgs2924rEventTable.setStatus(_A)
_Fgs2924rEventEntry_Object=MibTableRow
fgs2924rEventEntry=_Fgs2924rEventEntry_Object((1,3,6,1,4,1,5205,2,34,1,3,1,2,1))
fgs2924rEventEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:fgs2924rEventEntry.setStatus(_A)
class _Fgs2924rEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Fgs2924rEventIndex_Type.__name__=_C
_Fgs2924rEventIndex_Object=MibTableColumn
fgs2924rEventIndex=_Fgs2924rEventIndex_Object((1,3,6,1,4,1,5205,2,34,1,3,1,2,1,1),_Fgs2924rEventIndex_Type())
fgs2924rEventIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rEventIndex.setStatus(_A)
_Fgs2924rEventName_Type=DisplayString
_Fgs2924rEventName_Object=MibTableColumn
fgs2924rEventName=_Fgs2924rEventName_Object((1,3,6,1,4,1,5205,2,34,1,3,1,2,1,2),_Fgs2924rEventName_Type())
fgs2924rEventName.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rEventName.setStatus(_A)
class _Fgs2924rEventSendEmail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rEventSendEmail_Type.__name__=_C
_Fgs2924rEventSendEmail_Object=MibTableColumn
fgs2924rEventSendEmail=_Fgs2924rEventSendEmail_Object((1,3,6,1,4,1,5205,2,34,1,3,1,2,1,3),_Fgs2924rEventSendEmail_Type())
fgs2924rEventSendEmail.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rEventSendEmail.setStatus(_A)
class _Fgs2924rEventSendTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rEventSendTrap_Type.__name__=_C
_Fgs2924rEventSendTrap_Object=MibTableColumn
fgs2924rEventSendTrap=_Fgs2924rEventSendTrap_Object((1,3,6,1,4,1,5205,2,34,1,3,1,2,1,4),_Fgs2924rEventSendTrap_Type())
fgs2924rEventSendTrap.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rEventSendTrap.setStatus(_A)
_Fgs2924rEmail_ObjectIdentity=ObjectIdentity
fgs2924rEmail=_Fgs2924rEmail_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,3,2))
_Fgs2924rEmailServer_Type=DisplayString
_Fgs2924rEmailServer_Object=MibScalar
fgs2924rEmailServer=_Fgs2924rEmailServer_Object((1,3,6,1,4,1,5205,2,34,1,3,2,1),_Fgs2924rEmailServer_Type())
fgs2924rEmailServer.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rEmailServer.setStatus(_A)
_Fgs2924rEmailUsername_Type=DisplayString
_Fgs2924rEmailUsername_Object=MibScalar
fgs2924rEmailUsername=_Fgs2924rEmailUsername_Object((1,3,6,1,4,1,5205,2,34,1,3,2,2),_Fgs2924rEmailUsername_Type())
fgs2924rEmailUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rEmailUsername.setStatus(_A)
_Fgs2924rEmailPassword_Type=DisplayString
_Fgs2924rEmailPassword_Object=MibScalar
fgs2924rEmailPassword=_Fgs2924rEmailPassword_Object((1,3,6,1,4,1,5205,2,34,1,3,2,3),_Fgs2924rEmailPassword_Type())
fgs2924rEmailPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rEmailPassword.setStatus(_A)
_Fgs2924rEmailSender_Type=DisplayString
_Fgs2924rEmailSender_Object=MibScalar
fgs2924rEmailSender=_Fgs2924rEmailSender_Object((1,3,6,1,4,1,5205,2,34,1,3,2,4),_Fgs2924rEmailSender_Type())
fgs2924rEmailSender.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rEmailSender.setStatus(_A)
_Fgs2924rEmailReturnPath_Type=DisplayString
_Fgs2924rEmailReturnPath_Object=MibScalar
fgs2924rEmailReturnPath=_Fgs2924rEmailReturnPath_Object((1,3,6,1,4,1,5205,2,34,1,3,2,5),_Fgs2924rEmailReturnPath_Type())
fgs2924rEmailReturnPath.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rEmailReturnPath.setStatus(_A)
class _Fgs2924rEmailUserNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_Fgs2924rEmailUserNumber_Type.__name__=_C
_Fgs2924rEmailUserNumber_Object=MibScalar
fgs2924rEmailUserNumber=_Fgs2924rEmailUserNumber_Object((1,3,6,1,4,1,5205,2,34,1,3,2,6),_Fgs2924rEmailUserNumber_Type())
fgs2924rEmailUserNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rEmailUserNumber.setStatus(_A)
_Fgs2924rEmailUserTable_Object=MibTable
fgs2924rEmailUserTable=_Fgs2924rEmailUserTable_Object((1,3,6,1,4,1,5205,2,34,1,3,2,7))
if mibBuilder.loadTexts:fgs2924rEmailUserTable.setStatus(_A)
_Fgs2924rEmailUserEntry_Object=MibTableRow
fgs2924rEmailUserEntry=_Fgs2924rEmailUserEntry_Object((1,3,6,1,4,1,5205,2,34,1,3,2,7,1))
fgs2924rEmailUserEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:fgs2924rEmailUserEntry.setStatus(_A)
class _Fgs2924rEmailUserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_Fgs2924rEmailUserIndex_Type.__name__=_C
_Fgs2924rEmailUserIndex_Object=MibTableColumn
fgs2924rEmailUserIndex=_Fgs2924rEmailUserIndex_Object((1,3,6,1,4,1,5205,2,34,1,3,2,7,1,1),_Fgs2924rEmailUserIndex_Type())
fgs2924rEmailUserIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rEmailUserIndex.setStatus(_A)
_Fgs2924rEmailUserAddress_Type=DisplayString
_Fgs2924rEmailUserAddress_Object=MibTableColumn
fgs2924rEmailUserAddress=_Fgs2924rEmailUserAddress_Object((1,3,6,1,4,1,5205,2,34,1,3,2,7,1,2),_Fgs2924rEmailUserAddress_Type())
fgs2924rEmailUserAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rEmailUserAddress.setStatus(_A)
_Fgs2924rConfiguration_ObjectIdentity=ObjectIdentity
fgs2924rConfiguration=_Fgs2924rConfiguration_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,5))
_Fgs2924rSaveRestore_ObjectIdentity=ObjectIdentity
fgs2924rSaveRestore=_Fgs2924rSaveRestore_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,5,1))
class _Fgs2924rSaveStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rSaveStart_Type.__name__=_C
_Fgs2924rSaveStart_Object=MibScalar
fgs2924rSaveStart=_Fgs2924rSaveStart_Object((1,3,6,1,4,1,5205,2,34,1,5,1,1),_Fgs2924rSaveStart_Type())
fgs2924rSaveStart.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rSaveStart.setStatus(_A)
class _Fgs2924rSaveUser_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rSaveUser_Type.__name__=_C
_Fgs2924rSaveUser_Object=MibScalar
fgs2924rSaveUser=_Fgs2924rSaveUser_Object((1,3,6,1,4,1,5205,2,34,1,5,1,2),_Fgs2924rSaveUser_Type())
fgs2924rSaveUser.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rSaveUser.setStatus(_A)
class _Fgs2924rRestoreDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_Fgs2924rRestoreDefault_Type.__name__=_C
_Fgs2924rRestoreDefault_Object=MibScalar
fgs2924rRestoreDefault=_Fgs2924rRestoreDefault_Object((1,3,6,1,4,1,5205,2,34,1,5,1,3),_Fgs2924rRestoreDefault_Type())
fgs2924rRestoreDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rRestoreDefault.setStatus(_A)
class _Fgs2924rRestoreUser_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rRestoreUser_Type.__name__=_C
_Fgs2924rRestoreUser_Object=MibScalar
fgs2924rRestoreUser=_Fgs2924rRestoreUser_Object((1,3,6,1,4,1,5205,2,34,1,5,1,4),_Fgs2924rRestoreUser_Type())
fgs2924rRestoreUser.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rRestoreUser.setStatus(_A)
_Fgs2924rConfigFile_ObjectIdentity=ObjectIdentity
fgs2924rConfigFile=_Fgs2924rConfigFile_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,5,2))
_Fgs2924rExportIpAddress_Type=IpAddress
_Fgs2924rExportIpAddress_Object=MibScalar
fgs2924rExportIpAddress=_Fgs2924rExportIpAddress_Object((1,3,6,1,4,1,5205,2,34,1,5,2,1),_Fgs2924rExportIpAddress_Type())
fgs2924rExportIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rExportIpAddress.setStatus(_A)
class _Fgs2924rDoExportConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_Fgs2924rDoExportConfig_Type.__name__=_C
_Fgs2924rDoExportConfig_Object=MibScalar
fgs2924rDoExportConfig=_Fgs2924rDoExportConfig_Object((1,3,6,1,4,1,5205,2,34,1,5,2,2),_Fgs2924rDoExportConfig_Type())
fgs2924rDoExportConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDoExportConfig.setStatus(_A)
_Fgs2924rImportIpAddress_Type=IpAddress
_Fgs2924rImportIpAddress_Object=MibScalar
fgs2924rImportIpAddress=_Fgs2924rImportIpAddress_Object((1,3,6,1,4,1,5205,2,34,1,5,2,3),_Fgs2924rImportIpAddress_Type())
fgs2924rImportIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rImportIpAddress.setStatus(_A)
_Fgs2924rImportConfigName_Type=DisplayString
_Fgs2924rImportConfigName_Object=MibScalar
fgs2924rImportConfigName=_Fgs2924rImportConfigName_Object((1,3,6,1,4,1,5205,2,34,1,5,2,4),_Fgs2924rImportConfigName_Type())
fgs2924rImportConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rImportConfigName.setStatus(_A)
class _Fgs2924rDoImportConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_Fgs2924rDoImportConfig_Type.__name__=_C
_Fgs2924rDoImportConfig_Object=MibScalar
fgs2924rDoImportConfig=_Fgs2924rDoImportConfig_Object((1,3,6,1,4,1,5205,2,34,1,5,2,5),_Fgs2924rDoImportConfig_Type())
fgs2924rDoImportConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDoImportConfig.setStatus(_A)
_Fgs2924rLog_ObjectIdentity=ObjectIdentity
fgs2924rLog=_Fgs2924rLog_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,7))
class _Fgs2924rClearLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rClearLog_Type.__name__=_C
_Fgs2924rClearLog_Object=MibScalar
fgs2924rClearLog=_Fgs2924rClearLog_Object((1,3,6,1,4,1,5205,2,34,1,7,1),_Fgs2924rClearLog_Type())
fgs2924rClearLog.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rClearLog.setStatus(_A)
class _Fgs2924rLogNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_Fgs2924rLogNumber_Type.__name__=_C
_Fgs2924rLogNumber_Object=MibScalar
fgs2924rLogNumber=_Fgs2924rLogNumber_Object((1,3,6,1,4,1,5205,2,34,1,7,4),_Fgs2924rLogNumber_Type())
fgs2924rLogNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rLogNumber.setStatus(_A)
_Fgs2924rLogTable_Object=MibTable
fgs2924rLogTable=_Fgs2924rLogTable_Object((1,3,6,1,4,1,5205,2,34,1,7,5))
if mibBuilder.loadTexts:fgs2924rLogTable.setStatus(_A)
_Fgs2924rLogEntry_Object=MibTableRow
fgs2924rLogEntry=_Fgs2924rLogEntry_Object((1,3,6,1,4,1,5205,2,34,1,7,5,1))
fgs2924rLogEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:fgs2924rLogEntry.setStatus(_A)
class _Fgs2924rLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_Fgs2924rLogIndex_Type.__name__=_C
_Fgs2924rLogIndex_Object=MibTableColumn
fgs2924rLogIndex=_Fgs2924rLogIndex_Object((1,3,6,1,4,1,5205,2,34,1,7,5,1,1),_Fgs2924rLogIndex_Type())
fgs2924rLogIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rLogIndex.setStatus(_A)
_Fgs2924rLogEvent_Type=DisplayString
_Fgs2924rLogEvent_Object=MibTableColumn
fgs2924rLogEvent=_Fgs2924rLogEvent_Object((1,3,6,1,4,1,5205,2,34,1,7,5,1,2),_Fgs2924rLogEvent_Type())
fgs2924rLogEvent.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rLogEvent.setStatus(_A)
_Fgs2924rFirmware_ObjectIdentity=ObjectIdentity
fgs2924rFirmware=_Fgs2924rFirmware_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,8))
_Fgs2924rFirmwareIpAddress_Type=IpAddress
_Fgs2924rFirmwareIpAddress_Object=MibScalar
fgs2924rFirmwareIpAddress=_Fgs2924rFirmwareIpAddress_Object((1,3,6,1,4,1,5205,2,34,1,8,1),_Fgs2924rFirmwareIpAddress_Type())
fgs2924rFirmwareIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rFirmwareIpAddress.setStatus(_A)
_Fgs2924rFirmwareFileName_Type=DisplayString
_Fgs2924rFirmwareFileName_Object=MibScalar
fgs2924rFirmwareFileName=_Fgs2924rFirmwareFileName_Object((1,3,6,1,4,1,5205,2,34,1,8,2),_Fgs2924rFirmwareFileName_Type())
fgs2924rFirmwareFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rFirmwareFileName.setStatus(_A)
class _Fgs2924rDoFirmwareUpgrade_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rDoFirmwareUpgrade_Type.__name__=_C
_Fgs2924rDoFirmwareUpgrade_Object=MibScalar
fgs2924rDoFirmwareUpgrade=_Fgs2924rDoFirmwareUpgrade_Object((1,3,6,1,4,1,5205,2,34,1,8,3),_Fgs2924rDoFirmwareUpgrade_Type())
fgs2924rDoFirmwareUpgrade.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDoFirmwareUpgrade.setStatus(_A)
_Fgs2924rPort_ObjectIdentity=ObjectIdentity
fgs2924rPort=_Fgs2924rPort_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,9))
_Fgs2924rPortStatus_ObjectIdentity=ObjectIdentity
fgs2924rPortStatus=_Fgs2924rPortStatus_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,9,1))
class _Fgs2924rPortStatusNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Fgs2924rPortStatusNumber_Type.__name__=_C
_Fgs2924rPortStatusNumber_Object=MibScalar
fgs2924rPortStatusNumber=_Fgs2924rPortStatusNumber_Object((1,3,6,1,4,1,5205,2,34,1,9,1,1),_Fgs2924rPortStatusNumber_Type())
fgs2924rPortStatusNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rPortStatusNumber.setStatus(_A)
_Fgs2924rPortStatusTable_Object=MibTable
fgs2924rPortStatusTable=_Fgs2924rPortStatusTable_Object((1,3,6,1,4,1,5205,2,34,1,9,1,2))
if mibBuilder.loadTexts:fgs2924rPortStatusTable.setStatus(_A)
_Fgs2924rPortStatusEntry_Object=MibTableRow
fgs2924rPortStatusEntry=_Fgs2924rPortStatusEntry_Object((1,3,6,1,4,1,5205,2,34,1,9,1,2,1))
fgs2924rPortStatusEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:fgs2924rPortStatusEntry.setStatus(_A)
class _Fgs2924rPortStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Fgs2924rPortStatusIndex_Type.__name__=_C
_Fgs2924rPortStatusIndex_Object=MibTableColumn
fgs2924rPortStatusIndex=_Fgs2924rPortStatusIndex_Object((1,3,6,1,4,1,5205,2,34,1,9,1,2,1,1),_Fgs2924rPortStatusIndex_Type())
fgs2924rPortStatusIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rPortStatusIndex.setStatus(_A)
_Fgs2924rPortStatusMedia_Type=DisplayString
_Fgs2924rPortStatusMedia_Object=MibTableColumn
fgs2924rPortStatusMedia=_Fgs2924rPortStatusMedia_Object((1,3,6,1,4,1,5205,2,34,1,9,1,2,1,2),_Fgs2924rPortStatusMedia_Type())
fgs2924rPortStatusMedia.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rPortStatusMedia.setStatus(_A)
_Fgs2924rPortStatusPortState_Type=DisplayString
_Fgs2924rPortStatusPortState_Object=MibTableColumn
fgs2924rPortStatusPortState=_Fgs2924rPortStatusPortState_Object((1,3,6,1,4,1,5205,2,34,1,9,1,2,1,3),_Fgs2924rPortStatusPortState_Type())
fgs2924rPortStatusPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rPortStatusPortState.setStatus(_A)
_Fgs2924rPortStatusLink_Type=DisplayString
_Fgs2924rPortStatusLink_Object=MibTableColumn
fgs2924rPortStatusLink=_Fgs2924rPortStatusLink_Object((1,3,6,1,4,1,5205,2,34,1,9,1,2,1,4),_Fgs2924rPortStatusLink_Type())
fgs2924rPortStatusLink.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rPortStatusLink.setStatus(_A)
_Fgs2924rPortStatusAutoNego_Type=DisplayString
_Fgs2924rPortStatusAutoNego_Object=MibTableColumn
fgs2924rPortStatusAutoNego=_Fgs2924rPortStatusAutoNego_Object((1,3,6,1,4,1,5205,2,34,1,9,1,2,1,5),_Fgs2924rPortStatusAutoNego_Type())
fgs2924rPortStatusAutoNego.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rPortStatusAutoNego.setStatus(_A)
_Fgs2924rPortStatusSpdDpx_Type=DisplayString
_Fgs2924rPortStatusSpdDpx_Object=MibTableColumn
fgs2924rPortStatusSpdDpx=_Fgs2924rPortStatusSpdDpx_Object((1,3,6,1,4,1,5205,2,34,1,9,1,2,1,6),_Fgs2924rPortStatusSpdDpx_Type())
fgs2924rPortStatusSpdDpx.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rPortStatusSpdDpx.setStatus(_A)
_Fgs2924rPortStatusFlwCtrlRx_Type=DisplayString
_Fgs2924rPortStatusFlwCtrlRx_Object=MibTableColumn
fgs2924rPortStatusFlwCtrlRx=_Fgs2924rPortStatusFlwCtrlRx_Object((1,3,6,1,4,1,5205,2,34,1,9,1,2,1,7),_Fgs2924rPortStatusFlwCtrlRx_Type())
fgs2924rPortStatusFlwCtrlRx.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rPortStatusFlwCtrlRx.setStatus(_A)
_Fgs2924rPortStatusFlwCtrlTx_Type=DisplayString
_Fgs2924rPortStatusFlwCtrlTx_Object=MibTableColumn
fgs2924rPortStatusFlwCtrlTx=_Fgs2924rPortStatusFlwCtrlTx_Object((1,3,6,1,4,1,5205,2,34,1,9,1,2,1,8),_Fgs2924rPortStatusFlwCtrlTx_Type())
fgs2924rPortStatusFlwCtrlTx.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rPortStatusFlwCtrlTx.setStatus(_A)
_Fgs2924rPortStatuDescription_Type=DisplayString
_Fgs2924rPortStatuDescription_Object=MibTableColumn
fgs2924rPortStatuDescription=_Fgs2924rPortStatuDescription_Object((1,3,6,1,4,1,5205,2,34,1,9,1,2,1,9),_Fgs2924rPortStatuDescription_Type())
fgs2924rPortStatuDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rPortStatuDescription.setStatus(_A)
_Fgs2924rPortConf_ObjectIdentity=ObjectIdentity
fgs2924rPortConf=_Fgs2924rPortConf_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,9,2))
class _Fgs2924rPortConfNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Fgs2924rPortConfNumber_Type.__name__=_C
_Fgs2924rPortConfNumber_Object=MibScalar
fgs2924rPortConfNumber=_Fgs2924rPortConfNumber_Object((1,3,6,1,4,1,5205,2,34,1,9,2,1),_Fgs2924rPortConfNumber_Type())
fgs2924rPortConfNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rPortConfNumber.setStatus(_A)
_Fgs2924rPortConfTable_Object=MibTable
fgs2924rPortConfTable=_Fgs2924rPortConfTable_Object((1,3,6,1,4,1,5205,2,34,1,9,2,2))
if mibBuilder.loadTexts:fgs2924rPortConfTable.setStatus(_A)
_Fgs2924rPortConfEntry_Object=MibTableRow
fgs2924rPortConfEntry=_Fgs2924rPortConfEntry_Object((1,3,6,1,4,1,5205,2,34,1,9,2,2,1))
fgs2924rPortConfEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:fgs2924rPortConfEntry.setStatus(_A)
class _Fgs2924rPortConfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Fgs2924rPortConfIndex_Type.__name__=_C
_Fgs2924rPortConfIndex_Object=MibTableColumn
fgs2924rPortConfIndex=_Fgs2924rPortConfIndex_Object((1,3,6,1,4,1,5205,2,34,1,9,2,2,1,1),_Fgs2924rPortConfIndex_Type())
fgs2924rPortConfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rPortConfIndex.setStatus(_A)
class _Fgs2924rPortConfPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rPortConfPortState_Type.__name__=_C
_Fgs2924rPortConfPortState_Object=MibTableColumn
fgs2924rPortConfPortState=_Fgs2924rPortConfPortState_Object((1,3,6,1,4,1,5205,2,34,1,9,2,2,1,2),_Fgs2924rPortConfPortState_Type())
fgs2924rPortConfPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rPortConfPortState.setStatus(_A)
class _Fgs2924rPortConfTPSpdDpx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_Fgs2924rPortConfTPSpdDpx_Type.__name__=_C
_Fgs2924rPortConfTPSpdDpx_Object=MibTableColumn
fgs2924rPortConfTPSpdDpx=_Fgs2924rPortConfTPSpdDpx_Object((1,3,6,1,4,1,5205,2,34,1,9,2,2,1,3),_Fgs2924rPortConfTPSpdDpx_Type())
fgs2924rPortConfTPSpdDpx.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rPortConfTPSpdDpx.setStatus(_A)
class _Fgs2924rPortConfSFPSpdDpx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,5))
_Fgs2924rPortConfSFPSpdDpx_Type.__name__=_C
_Fgs2924rPortConfSFPSpdDpx_Object=MibTableColumn
fgs2924rPortConfSFPSpdDpx=_Fgs2924rPortConfSFPSpdDpx_Object((1,3,6,1,4,1,5205,2,34,1,9,2,2,1,4),_Fgs2924rPortConfSFPSpdDpx_Type())
fgs2924rPortConfSFPSpdDpx.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rPortConfSFPSpdDpx.setStatus(_A)
class _Fgs2924rPortConfFlwCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rPortConfFlwCtrl_Type.__name__=_C
_Fgs2924rPortConfFlwCtrl_Object=MibTableColumn
fgs2924rPortConfFlwCtrl=_Fgs2924rPortConfFlwCtrl_Object((1,3,6,1,4,1,5205,2,34,1,9,2,2,1,5),_Fgs2924rPortConfFlwCtrl_Type())
fgs2924rPortConfFlwCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rPortConfFlwCtrl.setStatus(_A)
class _Fgs2924rPortConfExcessiveCollisionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rPortConfExcessiveCollisionMode_Type.__name__=_C
_Fgs2924rPortConfExcessiveCollisionMode_Object=MibTableColumn
fgs2924rPortConfExcessiveCollisionMode=_Fgs2924rPortConfExcessiveCollisionMode_Object((1,3,6,1,4,1,5205,2,34,1,9,2,2,1,6),_Fgs2924rPortConfExcessiveCollisionMode_Type())
fgs2924rPortConfExcessiveCollisionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rPortConfExcessiveCollisionMode.setStatus(_A)
_Fgs2924rPortConfDescription_Type=DisplayString
_Fgs2924rPortConfDescription_Object=MibTableColumn
fgs2924rPortConfDescription=_Fgs2924rPortConfDescription_Object((1,3,6,1,4,1,5205,2,34,1,9,2,2,1,7),_Fgs2924rPortConfDescription_Type())
fgs2924rPortConfDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rPortConfDescription.setStatus(_A)
class _Fgs2924rPortConfPowerSaving_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rPortConfPowerSaving_Type.__name__=_C
_Fgs2924rPortConfPowerSaving_Object=MibTableColumn
fgs2924rPortConfPowerSaving=_Fgs2924rPortConfPowerSaving_Object((1,3,6,1,4,1,5205,2,34,1,9,2,2,1,8),_Fgs2924rPortConfPowerSaving_Type())
fgs2924rPortConfPowerSaving.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rPortConfPowerSaving.setStatus(_A)
_Fgs2924rSFPInfo_ObjectIdentity=ObjectIdentity
fgs2924rSFPInfo=_Fgs2924rSFPInfo_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,9,3))
class _Fgs2924rSFPInfoNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Fgs2924rSFPInfoNumber_Type.__name__=_C
_Fgs2924rSFPInfoNumber_Object=MibScalar
fgs2924rSFPInfoNumber=_Fgs2924rSFPInfoNumber_Object((1,3,6,1,4,1,5205,2,34,1,9,3,1),_Fgs2924rSFPInfoNumber_Type())
fgs2924rSFPInfoNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rSFPInfoNumber.setStatus(_A)
_Fgs2924rSFPInfoTable_Object=MibTable
fgs2924rSFPInfoTable=_Fgs2924rSFPInfoTable_Object((1,3,6,1,4,1,5205,2,34,1,9,3,2))
if mibBuilder.loadTexts:fgs2924rSFPInfoTable.setStatus(_A)
_Fgs2924rSFPInfoEntry_Object=MibTableRow
fgs2924rSFPInfoEntry=_Fgs2924rSFPInfoEntry_Object((1,3,6,1,4,1,5205,2,34,1,9,3,2,1))
fgs2924rSFPInfoEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:fgs2924rSFPInfoEntry.setStatus(_A)
class _Fgs2924rSFPInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Fgs2924rSFPInfoIndex_Type.__name__=_C
_Fgs2924rSFPInfoIndex_Object=MibTableColumn
fgs2924rSFPInfoIndex=_Fgs2924rSFPInfoIndex_Object((1,3,6,1,4,1,5205,2,34,1,9,3,2,1,1),_Fgs2924rSFPInfoIndex_Type())
fgs2924rSFPInfoIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rSFPInfoIndex.setStatus(_A)
_Fgs2924rSFPConnectorType_Type=DisplayString
_Fgs2924rSFPConnectorType_Object=MibTableColumn
fgs2924rSFPConnectorType=_Fgs2924rSFPConnectorType_Object((1,3,6,1,4,1,5205,2,34,1,9,3,2,1,2),_Fgs2924rSFPConnectorType_Type())
fgs2924rSFPConnectorType.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rSFPConnectorType.setStatus(_A)
_Fgs2924rSFPFiberType_Type=DisplayString
_Fgs2924rSFPFiberType_Object=MibTableColumn
fgs2924rSFPFiberType=_Fgs2924rSFPFiberType_Object((1,3,6,1,4,1,5205,2,34,1,9,3,2,1,3),_Fgs2924rSFPFiberType_Type())
fgs2924rSFPFiberType.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rSFPFiberType.setStatus(_A)
_Fgs2924rSFPWavelength_Type=DisplayString
_Fgs2924rSFPWavelength_Object=MibTableColumn
fgs2924rSFPWavelength=_Fgs2924rSFPWavelength_Object((1,3,6,1,4,1,5205,2,34,1,9,3,2,1,4),_Fgs2924rSFPWavelength_Type())
fgs2924rSFPWavelength.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rSFPWavelength.setStatus(_A)
_Fgs2924rSFPBaudRate_Type=DisplayString
_Fgs2924rSFPBaudRate_Object=MibTableColumn
fgs2924rSFPBaudRate=_Fgs2924rSFPBaudRate_Object((1,3,6,1,4,1,5205,2,34,1,9,3,2,1,5),_Fgs2924rSFPBaudRate_Type())
fgs2924rSFPBaudRate.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rSFPBaudRate.setStatus(_A)
_Fgs2924rSFPVendorOUI_Type=DisplayString
_Fgs2924rSFPVendorOUI_Object=MibTableColumn
fgs2924rSFPVendorOUI=_Fgs2924rSFPVendorOUI_Object((1,3,6,1,4,1,5205,2,34,1,9,3,2,1,6),_Fgs2924rSFPVendorOUI_Type())
fgs2924rSFPVendorOUI.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rSFPVendorOUI.setStatus(_A)
_Fgs2924rSFPVendorName_Type=DisplayString
_Fgs2924rSFPVendorName_Object=MibTableColumn
fgs2924rSFPVendorName=_Fgs2924rSFPVendorName_Object((1,3,6,1,4,1,5205,2,34,1,9,3,2,1,7),_Fgs2924rSFPVendorName_Type())
fgs2924rSFPVendorName.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rSFPVendorName.setStatus(_A)
_Fgs2924rSFPVendorPN_Type=DisplayString
_Fgs2924rSFPVendorPN_Object=MibTableColumn
fgs2924rSFPVendorPN=_Fgs2924rSFPVendorPN_Object((1,3,6,1,4,1,5205,2,34,1,9,3,2,1,8),_Fgs2924rSFPVendorPN_Type())
fgs2924rSFPVendorPN.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rSFPVendorPN.setStatus(_A)
_Fgs2924rSFPVendorRev_Type=DisplayString
_Fgs2924rSFPVendorRev_Object=MibTableColumn
fgs2924rSFPVendorRev=_Fgs2924rSFPVendorRev_Object((1,3,6,1,4,1,5205,2,34,1,9,3,2,1,9),_Fgs2924rSFPVendorRev_Type())
fgs2924rSFPVendorRev.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rSFPVendorRev.setStatus(_A)
_Fgs2924rSFPVendorSN_Type=DisplayString
_Fgs2924rSFPVendorSN_Object=MibTableColumn
fgs2924rSFPVendorSN=_Fgs2924rSFPVendorSN_Object((1,3,6,1,4,1,5205,2,34,1,9,3,2,1,10),_Fgs2924rSFPVendorSN_Type())
fgs2924rSFPVendorSN.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rSFPVendorSN.setStatus(_A)
_Fgs2924rSFPDateCode_Type=DisplayString
_Fgs2924rSFPDateCode_Object=MibTableColumn
fgs2924rSFPDateCode=_Fgs2924rSFPDateCode_Object((1,3,6,1,4,1,5205,2,34,1,9,3,2,1,11),_Fgs2924rSFPDateCode_Type())
fgs2924rSFPDateCode.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rSFPDateCode.setStatus(_A)
_Fgs2924rSFPTemperature_Type=DisplayString
_Fgs2924rSFPTemperature_Object=MibTableColumn
fgs2924rSFPTemperature=_Fgs2924rSFPTemperature_Object((1,3,6,1,4,1,5205,2,34,1,9,3,2,1,12),_Fgs2924rSFPTemperature_Type())
fgs2924rSFPTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rSFPTemperature.setStatus(_A)
_Fgs2924rSFPVcc_Type=DisplayString
_Fgs2924rSFPVcc_Object=MibTableColumn
fgs2924rSFPVcc=_Fgs2924rSFPVcc_Object((1,3,6,1,4,1,5205,2,34,1,9,3,2,1,13),_Fgs2924rSFPVcc_Type())
fgs2924rSFPVcc.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rSFPVcc.setStatus(_A)
_Fgs2924rSFPTxBias_Type=DisplayString
_Fgs2924rSFPTxBias_Object=MibTableColumn
fgs2924rSFPTxBias=_Fgs2924rSFPTxBias_Object((1,3,6,1,4,1,5205,2,34,1,9,3,2,1,14),_Fgs2924rSFPTxBias_Type())
fgs2924rSFPTxBias.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rSFPTxBias.setStatus(_A)
_Fgs2924rSFPTxPWR_Type=DisplayString
_Fgs2924rSFPTxPWR_Object=MibTableColumn
fgs2924rSFPTxPWR=_Fgs2924rSFPTxPWR_Object((1,3,6,1,4,1,5205,2,34,1,9,3,2,1,15),_Fgs2924rSFPTxPWR_Type())
fgs2924rSFPTxPWR.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rSFPTxPWR.setStatus(_A)
_Fgs2924rSFPRxPWR_Type=DisplayString
_Fgs2924rSFPRxPWR_Object=MibTableColumn
fgs2924rSFPRxPWR=_Fgs2924rSFPRxPWR_Object((1,3,6,1,4,1,5205,2,34,1,9,3,2,1,16),_Fgs2924rSFPRxPWR_Type())
fgs2924rSFPRxPWR.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rSFPRxPWR.setStatus(_A)
_Fgs2924rMirror_ObjectIdentity=ObjectIdentity
fgs2924rMirror=_Fgs2924rMirror_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,10))
class _Fgs2924rMirroringPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Fgs2924rMirroringPort_Type.__name__=_C
_Fgs2924rMirroringPort_Object=MibScalar
fgs2924rMirroringPort=_Fgs2924rMirroringPort_Object((1,3,6,1,4,1,5205,2,34,1,10,1),_Fgs2924rMirroringPort_Type())
fgs2924rMirroringPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMirroringPort.setStatus(_A)
_Fgs2924rMirroredPortsTable_Object=MibTable
fgs2924rMirroredPortsTable=_Fgs2924rMirroredPortsTable_Object((1,3,6,1,4,1,5205,2,34,1,10,2))
if mibBuilder.loadTexts:fgs2924rMirroredPortsTable.setStatus(_A)
_Fgs2924rMirroredPortsEntry_Object=MibTableRow
fgs2924rMirroredPortsEntry=_Fgs2924rMirroredPortsEntry_Object((1,3,6,1,4,1,5205,2,34,1,10,2,1))
fgs2924rMirroredPortsEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:fgs2924rMirroredPortsEntry.setStatus(_A)
class _Fgs2924rMirroredPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rMirroredPortIndex_Type.__name__=_C
_Fgs2924rMirroredPortIndex_Object=MibTableColumn
fgs2924rMirroredPortIndex=_Fgs2924rMirroredPortIndex_Object((1,3,6,1,4,1,5205,2,34,1,10,2,1,1),_Fgs2924rMirroredPortIndex_Type())
fgs2924rMirroredPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rMirroredPortIndex.setStatus(_A)
class _Fgs2924rMirroredPortSrouceEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rMirroredPortSrouceEnable_Type.__name__=_C
_Fgs2924rMirroredPortSrouceEnable_Object=MibTableColumn
fgs2924rMirroredPortSrouceEnable=_Fgs2924rMirroredPortSrouceEnable_Object((1,3,6,1,4,1,5205,2,34,1,10,2,1,2),_Fgs2924rMirroredPortSrouceEnable_Type())
fgs2924rMirroredPortSrouceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMirroredPortSrouceEnable.setStatus(_A)
class _Fgs2924rMirroredPortDestinationEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rMirroredPortDestinationEnable_Type.__name__=_C
_Fgs2924rMirroredPortDestinationEnable_Object=MibTableColumn
fgs2924rMirroredPortDestinationEnable=_Fgs2924rMirroredPortDestinationEnable_Object((1,3,6,1,4,1,5205,2,34,1,10,2,1,3),_Fgs2924rMirroredPortDestinationEnable_Type())
fgs2924rMirroredPortDestinationEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMirroredPortDestinationEnable.setStatus(_A)
_Fgs2924rMaxPktLen_ObjectIdentity=ObjectIdentity
fgs2924rMaxPktLen=_Fgs2924rMaxPktLen_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,11))
class _Fgs2924rMaxPktLenPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rMaxPktLenPortNumber_Type.__name__=_C
_Fgs2924rMaxPktLenPortNumber_Object=MibScalar
fgs2924rMaxPktLenPortNumber=_Fgs2924rMaxPktLenPortNumber_Object((1,3,6,1,4,1,5205,2,34,1,11,1),_Fgs2924rMaxPktLenPortNumber_Type())
fgs2924rMaxPktLenPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rMaxPktLenPortNumber.setStatus(_A)
_Fgs2924rMaxPktLenConfTable_Object=MibTable
fgs2924rMaxPktLenConfTable=_Fgs2924rMaxPktLenConfTable_Object((1,3,6,1,4,1,5205,2,34,1,11,2))
if mibBuilder.loadTexts:fgs2924rMaxPktLenConfTable.setStatus(_A)
_Fgs2924rMaxPktLenConfEntry_Object=MibTableRow
fgs2924rMaxPktLenConfEntry=_Fgs2924rMaxPktLenConfEntry_Object((1,3,6,1,4,1,5205,2,34,1,11,2,1))
fgs2924rMaxPktLenConfEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:fgs2924rMaxPktLenConfEntry.setStatus(_A)
class _Fgs2924rMaxPktLenConfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rMaxPktLenConfIndex_Type.__name__=_C
_Fgs2924rMaxPktLenConfIndex_Object=MibTableColumn
fgs2924rMaxPktLenConfIndex=_Fgs2924rMaxPktLenConfIndex_Object((1,3,6,1,4,1,5205,2,34,1,11,2,1,1),_Fgs2924rMaxPktLenConfIndex_Type())
fgs2924rMaxPktLenConfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rMaxPktLenConfIndex.setStatus(_A)
class _Fgs2924rMaxPktLenConfSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1518,9600))
_Fgs2924rMaxPktLenConfSetting_Type.__name__=_C
_Fgs2924rMaxPktLenConfSetting_Object=MibTableColumn
fgs2924rMaxPktLenConfSetting=_Fgs2924rMaxPktLenConfSetting_Object((1,3,6,1,4,1,5205,2,34,1,11,2,1,2),_Fgs2924rMaxPktLenConfSetting_Type())
fgs2924rMaxPktLenConfSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMaxPktLenConfSetting.setStatus(_A)
_Fgs2924rLoopDetectedConf_ObjectIdentity=ObjectIdentity
fgs2924rLoopDetectedConf=_Fgs2924rLoopDetectedConf_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,12))
class _Fgs2924rLoopDetectedNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Fgs2924rLoopDetectedNumber_Type.__name__=_C
_Fgs2924rLoopDetectedNumber_Object=MibScalar
fgs2924rLoopDetectedNumber=_Fgs2924rLoopDetectedNumber_Object((1,3,6,1,4,1,5205,2,34,1,12,1),_Fgs2924rLoopDetectedNumber_Type())
fgs2924rLoopDetectedNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rLoopDetectedNumber.setStatus(_A)
_Fgs2924rLoopDetectedTable_Object=MibTable
fgs2924rLoopDetectedTable=_Fgs2924rLoopDetectedTable_Object((1,3,6,1,4,1,5205,2,34,1,12,2))
if mibBuilder.loadTexts:fgs2924rLoopDetectedTable.setStatus(_A)
_Fgs2924rLoopDetectedEntry_Object=MibTableRow
fgs2924rLoopDetectedEntry=_Fgs2924rLoopDetectedEntry_Object((1,3,6,1,4,1,5205,2,34,1,12,2,1))
fgs2924rLoopDetectedEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:fgs2924rLoopDetectedEntry.setStatus(_A)
class _Fgs2924rLoopDetectedfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Fgs2924rLoopDetectedfIndex_Type.__name__=_C
_Fgs2924rLoopDetectedfIndex_Object=MibTableColumn
fgs2924rLoopDetectedfIndex=_Fgs2924rLoopDetectedfIndex_Object((1,3,6,1,4,1,5205,2,34,1,12,2,1,1),_Fgs2924rLoopDetectedfIndex_Type())
fgs2924rLoopDetectedfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rLoopDetectedfIndex.setStatus(_A)
class _Fgs2924rLoopDetectedPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rLoopDetectedPort_Type.__name__=_C
_Fgs2924rLoopDetectedPort_Object=MibTableColumn
fgs2924rLoopDetectedPort=_Fgs2924rLoopDetectedPort_Object((1,3,6,1,4,1,5205,2,34,1,12,2,1,2),_Fgs2924rLoopDetectedPort_Type())
fgs2924rLoopDetectedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rLoopDetectedPort.setStatus(_A)
class _Fgs2924rLoopDetectedLockedPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rLoopDetectedLockedPort_Type.__name__=_C
_Fgs2924rLoopDetectedLockedPort_Object=MibTableColumn
fgs2924rLoopDetectedLockedPort=_Fgs2924rLoopDetectedLockedPort_Object((1,3,6,1,4,1,5205,2,34,1,12,2,1,3),_Fgs2924rLoopDetectedLockedPort_Type())
fgs2924rLoopDetectedLockedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rLoopDetectedLockedPort.setStatus(_A)
_Fgs2924rManagementPolicy_ObjectIdentity=ObjectIdentity
fgs2924rManagementPolicy=_Fgs2924rManagementPolicy_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,13))
class _Fgs2924rManagementSecurityNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_Fgs2924rManagementSecurityNumber_Type.__name__=_C
_Fgs2924rManagementSecurityNumber_Object=MibScalar
fgs2924rManagementSecurityNumber=_Fgs2924rManagementSecurityNumber_Object((1,3,6,1,4,1,5205,2,34,1,13,1),_Fgs2924rManagementSecurityNumber_Type())
fgs2924rManagementSecurityNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rManagementSecurityNumber.setStatus(_A)
class _Fgs2924rManagementSecurityEntryCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_Fgs2924rManagementSecurityEntryCreate_Type.__name__=_C
_Fgs2924rManagementSecurityEntryCreate_Object=MibScalar
fgs2924rManagementSecurityEntryCreate=_Fgs2924rManagementSecurityEntryCreate_Object((1,3,6,1,4,1,5205,2,34,1,13,2),_Fgs2924rManagementSecurityEntryCreate_Type())
fgs2924rManagementSecurityEntryCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rManagementSecurityEntryCreate.setStatus(_A)
_Fgs2924rManagementSecurityTable_Object=MibTable
fgs2924rManagementSecurityTable=_Fgs2924rManagementSecurityTable_Object((1,3,6,1,4,1,5205,2,34,1,13,3))
if mibBuilder.loadTexts:fgs2924rManagementSecurityTable.setStatus(_A)
_Fgs2924rManagementSecurityEntry_Object=MibTableRow
fgs2924rManagementSecurityEntry=_Fgs2924rManagementSecurityEntry_Object((1,3,6,1,4,1,5205,2,34,1,13,3,1))
fgs2924rManagementSecurityEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:fgs2924rManagementSecurityEntry.setStatus(_A)
class _Fgs2924rManagementSecurityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Fgs2924rManagementSecurityIndex_Type.__name__=_C
_Fgs2924rManagementSecurityIndex_Object=MibTableColumn
fgs2924rManagementSecurityIndex=_Fgs2924rManagementSecurityIndex_Object((1,3,6,1,4,1,5205,2,34,1,13,3,1,1),_Fgs2924rManagementSecurityIndex_Type())
fgs2924rManagementSecurityIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rManagementSecurityIndex.setStatus(_A)
_Fgs2924rManagementSecurityName_Type=DisplayString
_Fgs2924rManagementSecurityName_Object=MibTableColumn
fgs2924rManagementSecurityName=_Fgs2924rManagementSecurityName_Object((1,3,6,1,4,1,5205,2,34,1,13,3,1,2),_Fgs2924rManagementSecurityName_Type())
fgs2924rManagementSecurityName.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rManagementSecurityName.setStatus(_A)
_Fgs2924rManagementSecurityIpRange_Type=DisplayString
_Fgs2924rManagementSecurityIpRange_Object=MibTableColumn
fgs2924rManagementSecurityIpRange=_Fgs2924rManagementSecurityIpRange_Object((1,3,6,1,4,1,5205,2,34,1,13,3,1,3),_Fgs2924rManagementSecurityIpRange_Type())
fgs2924rManagementSecurityIpRange.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rManagementSecurityIpRange.setStatus(_A)
_Fgs2924rManagementSecurityIncomigPort_Type=DisplayString
_Fgs2924rManagementSecurityIncomigPort_Object=MibTableColumn
fgs2924rManagementSecurityIncomigPort=_Fgs2924rManagementSecurityIncomigPort_Object((1,3,6,1,4,1,5205,2,34,1,13,3,1,4),_Fgs2924rManagementSecurityIncomigPort_Type())
fgs2924rManagementSecurityIncomigPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rManagementSecurityIncomigPort.setStatus(_A)
_Fgs2924rManagementSecurityAccessType_Type=DisplayString
_Fgs2924rManagementSecurityAccessType_Object=MibTableColumn
fgs2924rManagementSecurityAccessType=_Fgs2924rManagementSecurityAccessType_Object((1,3,6,1,4,1,5205,2,34,1,13,3,1,5),_Fgs2924rManagementSecurityAccessType_Type())
fgs2924rManagementSecurityAccessType.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rManagementSecurityAccessType.setStatus(_A)
class _Fgs2924rManagementSecurityAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rManagementSecurityAction_Type.__name__=_C
_Fgs2924rManagementSecurityAction_Object=MibTableColumn
fgs2924rManagementSecurityAction=_Fgs2924rManagementSecurityAction_Object((1,3,6,1,4,1,5205,2,34,1,13,3,1,6),_Fgs2924rManagementSecurityAction_Type())
fgs2924rManagementSecurityAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rManagementSecurityAction.setStatus(_A)
class _Fgs2924rManagementSecurityEntryAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Fgs2924rManagementSecurityEntryAction_Type.__name__=_C
_Fgs2924rManagementSecurityEntryAction_Object=MibTableColumn
fgs2924rManagementSecurityEntryAction=_Fgs2924rManagementSecurityEntryAction_Object((1,3,6,1,4,1,5205,2,34,1,13,3,1,7),_Fgs2924rManagementSecurityEntryAction_Type())
fgs2924rManagementSecurityEntryAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rManagementSecurityEntryAction.setStatus(_A)
_Fgs2924rVLAN_ObjectIdentity=ObjectIdentity
fgs2924rVLAN=_Fgs2924rVLAN_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,14))
_Fgs2924rVlanConf_ObjectIdentity=ObjectIdentity
fgs2924rVlanConf=_Fgs2924rVlanConf_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,14,1))
class _Fgs2924rVlanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rVlanMode_Type.__name__=_C
_Fgs2924rVlanMode_Object=MibScalar
fgs2924rVlanMode=_Fgs2924rVlanMode_Object((1,3,6,1,4,1,5205,2,34,1,14,1,1),_Fgs2924rVlanMode_Type())
fgs2924rVlanMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rVlanMode.setStatus(_A)
class _Fgs2924rManagementVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Fgs2924rManagementVlan_Type.__name__=_C
_Fgs2924rManagementVlan_Object=MibScalar
fgs2924rManagementVlan=_Fgs2924rManagementVlan_Object((1,3,6,1,4,1,5205,2,34,1,14,1,2),_Fgs2924rManagementVlan_Type())
fgs2924rManagementVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rManagementVlan.setStatus(_A)
_Fgs2924rPortIsolation_Type=DisplayString
_Fgs2924rPortIsolation_Object=MibScalar
fgs2924rPortIsolation=_Fgs2924rPortIsolation_Object((1,3,6,1,4,1,5205,2,34,1,14,1,3),_Fgs2924rPortIsolation_Type())
fgs2924rPortIsolation.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rPortIsolation.setStatus(_A)
class _Fgs2924rTagIdentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rTagIdentifier_Type.__name__=_C
_Fgs2924rTagIdentifier_Object=MibScalar
fgs2924rTagIdentifier=_Fgs2924rTagIdentifier_Object((1,3,6,1,4,1,5205,2,34,1,14,1,4),_Fgs2924rTagIdentifier_Type())
fgs2924rTagIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rTagIdentifier.setStatus(_A)
_Fgs2924rTagBaseVlanGroup_ObjectIdentity=ObjectIdentity
fgs2924rTagBaseVlanGroup=_Fgs2924rTagBaseVlanGroup_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,14,2))
class _Fgs2924rTagBaseVlanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Fgs2924rTagBaseVlanNumber_Type.__name__=_C
_Fgs2924rTagBaseVlanNumber_Object=MibScalar
fgs2924rTagBaseVlanNumber=_Fgs2924rTagBaseVlanNumber_Object((1,3,6,1,4,1,5205,2,34,1,14,2,1),_Fgs2924rTagBaseVlanNumber_Type())
fgs2924rTagBaseVlanNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rTagBaseVlanNumber.setStatus(_A)
class _Fgs2924rTagBaseVlanGroupEntryCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_Fgs2924rTagBaseVlanGroupEntryCreate_Type.__name__=_C
_Fgs2924rTagBaseVlanGroupEntryCreate_Object=MibScalar
fgs2924rTagBaseVlanGroupEntryCreate=_Fgs2924rTagBaseVlanGroupEntryCreate_Object((1,3,6,1,4,1,5205,2,34,1,14,2,2),_Fgs2924rTagBaseVlanGroupEntryCreate_Type())
fgs2924rTagBaseVlanGroupEntryCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rTagBaseVlanGroupEntryCreate.setStatus(_A)
_Fgs2924rTagBaseVlanGroupTable_Object=MibTable
fgs2924rTagBaseVlanGroupTable=_Fgs2924rTagBaseVlanGroupTable_Object((1,3,6,1,4,1,5205,2,34,1,14,2,3))
if mibBuilder.loadTexts:fgs2924rTagBaseVlanGroupTable.setStatus(_A)
_Fgs2924rTagBaseVlanGroupEntry_Object=MibTableRow
fgs2924rTagBaseVlanGroupEntry=_Fgs2924rTagBaseVlanGroupEntry_Object((1,3,6,1,4,1,5205,2,34,1,14,2,3,1))
fgs2924rTagBaseVlanGroupEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:fgs2924rTagBaseVlanGroupEntry.setStatus(_A)
class _Fgs2924rTagBaseVlanVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Fgs2924rTagBaseVlanVid_Type.__name__=_C
_Fgs2924rTagBaseVlanVid_Object=MibTableColumn
fgs2924rTagBaseVlanVid=_Fgs2924rTagBaseVlanVid_Object((1,3,6,1,4,1,5205,2,34,1,14,2,3,1,1),_Fgs2924rTagBaseVlanVid_Type())
fgs2924rTagBaseVlanVid.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rTagBaseVlanVid.setStatus(_A)
_Fgs2924rTagBaseVlanName_Type=DisplayString
_Fgs2924rTagBaseVlanName_Object=MibTableColumn
fgs2924rTagBaseVlanName=_Fgs2924rTagBaseVlanName_Object((1,3,6,1,4,1,5205,2,34,1,14,2,3,1,2),_Fgs2924rTagBaseVlanName_Type())
fgs2924rTagBaseVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rTagBaseVlanName.setStatus(_A)
class _Fgs2924rTagBaseVlanIgmpProxy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rTagBaseVlanIgmpProxy_Type.__name__=_C
_Fgs2924rTagBaseVlanIgmpProxy_Object=MibTableColumn
fgs2924rTagBaseVlanIgmpProxy=_Fgs2924rTagBaseVlanIgmpProxy_Object((1,3,6,1,4,1,5205,2,34,1,14,2,3,1,3),_Fgs2924rTagBaseVlanIgmpProxy_Type())
fgs2924rTagBaseVlanIgmpProxy.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rTagBaseVlanIgmpProxy.setStatus(_A)
class _Fgs2924rTagBaseVlanPrivateVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rTagBaseVlanPrivateVlan_Type.__name__=_C
_Fgs2924rTagBaseVlanPrivateVlan_Object=MibTableColumn
fgs2924rTagBaseVlanPrivateVlan=_Fgs2924rTagBaseVlanPrivateVlan_Object((1,3,6,1,4,1,5205,2,34,1,14,2,3,1,4),_Fgs2924rTagBaseVlanPrivateVlan_Type())
fgs2924rTagBaseVlanPrivateVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rTagBaseVlanPrivateVlan.setStatus(_A)
class _Fgs2924rTagBaseVlanGvrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rTagBaseVlanGvrp_Type.__name__=_C
_Fgs2924rTagBaseVlanGvrp_Object=MibTableColumn
fgs2924rTagBaseVlanGvrp=_Fgs2924rTagBaseVlanGvrp_Object((1,3,6,1,4,1,5205,2,34,1,14,2,3,1,5),_Fgs2924rTagBaseVlanGvrp_Type())
fgs2924rTagBaseVlanGvrp.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rTagBaseVlanGvrp.setStatus(_A)
_Fgs2924rTagBaseVlanMemberPort_Type=DisplayString
_Fgs2924rTagBaseVlanMemberPort_Object=MibTableColumn
fgs2924rTagBaseVlanMemberPort=_Fgs2924rTagBaseVlanMemberPort_Object((1,3,6,1,4,1,5205,2,34,1,14,2,3,1,6),_Fgs2924rTagBaseVlanMemberPort_Type())
fgs2924rTagBaseVlanMemberPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rTagBaseVlanMemberPort.setStatus(_A)
class _Fgs2924rTagBaseVlanEntryAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Fgs2924rTagBaseVlanEntryAction_Type.__name__=_C
_Fgs2924rTagBaseVlanEntryAction_Object=MibTableColumn
fgs2924rTagBaseVlanEntryAction=_Fgs2924rTagBaseVlanEntryAction_Object((1,3,6,1,4,1,5205,2,34,1,14,2,3,1,7),_Fgs2924rTagBaseVlanEntryAction_Type())
fgs2924rTagBaseVlanEntryAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rTagBaseVlanEntryAction.setStatus(_A)
_Fgs2924rVlanPortConfTable_Object=MibTable
fgs2924rVlanPortConfTable=_Fgs2924rVlanPortConfTable_Object((1,3,6,1,4,1,5205,2,34,1,14,3))
if mibBuilder.loadTexts:fgs2924rVlanPortConfTable.setStatus(_A)
_Fgs2924rVlanPortConfEntry_Object=MibTableRow
fgs2924rVlanPortConfEntry=_Fgs2924rVlanPortConfEntry_Object((1,3,6,1,4,1,5205,2,34,1,14,3,1))
fgs2924rVlanPortConfEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:fgs2924rVlanPortConfEntry.setStatus(_A)
class _Fgs2924rVlanPortConfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rVlanPortConfIndex_Type.__name__=_C
_Fgs2924rVlanPortConfIndex_Object=MibTableColumn
fgs2924rVlanPortConfIndex=_Fgs2924rVlanPortConfIndex_Object((1,3,6,1,4,1,5205,2,34,1,14,3,1,1),_Fgs2924rVlanPortConfIndex_Type())
fgs2924rVlanPortConfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rVlanPortConfIndex.setStatus(_A)
class _Fgs2924rVlanPortConfVlanAware_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rVlanPortConfVlanAware_Type.__name__=_C
_Fgs2924rVlanPortConfVlanAware_Object=MibTableColumn
fgs2924rVlanPortConfVlanAware=_Fgs2924rVlanPortConfVlanAware_Object((1,3,6,1,4,1,5205,2,34,1,14,3,1,2),_Fgs2924rVlanPortConfVlanAware_Type())
fgs2924rVlanPortConfVlanAware.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rVlanPortConfVlanAware.setStatus(_A)
class _Fgs2924rVlanPortConfIngressFiltering_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rVlanPortConfIngressFiltering_Type.__name__=_C
_Fgs2924rVlanPortConfIngressFiltering_Object=MibTableColumn
fgs2924rVlanPortConfIngressFiltering=_Fgs2924rVlanPortConfIngressFiltering_Object((1,3,6,1,4,1,5205,2,34,1,14,3,1,3),_Fgs2924rVlanPortConfIngressFiltering_Type())
fgs2924rVlanPortConfIngressFiltering.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rVlanPortConfIngressFiltering.setStatus(_A)
class _Fgs2924rVlanPortConfFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rVlanPortConfFrameType_Type.__name__=_C
_Fgs2924rVlanPortConfFrameType_Object=MibTableColumn
fgs2924rVlanPortConfFrameType=_Fgs2924rVlanPortConfFrameType_Object((1,3,6,1,4,1,5205,2,34,1,14,3,1,4),_Fgs2924rVlanPortConfFrameType_Type())
fgs2924rVlanPortConfFrameType.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rVlanPortConfFrameType.setStatus(_A)
class _Fgs2924rVlanPortConfPvid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Fgs2924rVlanPortConfPvid_Type.__name__=_C
_Fgs2924rVlanPortConfPvid_Object=MibTableColumn
fgs2924rVlanPortConfPvid=_Fgs2924rVlanPortConfPvid_Object((1,3,6,1,4,1,5205,2,34,1,14,3,1,5),_Fgs2924rVlanPortConfPvid_Type())
fgs2924rVlanPortConfPvid.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rVlanPortConfPvid.setStatus(_A)
class _Fgs2924rVlanPortConfRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Fgs2924rVlanPortConfRole_Type.__name__=_C
_Fgs2924rVlanPortConfRole_Object=MibTableColumn
fgs2924rVlanPortConfRole=_Fgs2924rVlanPortConfRole_Object((1,3,6,1,4,1,5205,2,34,1,14,3,1,6),_Fgs2924rVlanPortConfRole_Type())
fgs2924rVlanPortConfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rVlanPortConfRole.setStatus(_A)
class _Fgs2924rVlanPortConfUntagVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Fgs2924rVlanPortConfUntagVid_Type.__name__=_C
_Fgs2924rVlanPortConfUntagVid_Object=MibTableColumn
fgs2924rVlanPortConfUntagVid=_Fgs2924rVlanPortConfUntagVid_Object((1,3,6,1,4,1,5205,2,34,1,14,3,1,7),_Fgs2924rVlanPortConfUntagVid_Type())
fgs2924rVlanPortConfUntagVid.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rVlanPortConfUntagVid.setStatus(_A)
class _Fgs2924rVlanPortConfDoubleTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Fgs2924rVlanPortConfDoubleTag_Type.__name__=_C
_Fgs2924rVlanPortConfDoubleTag_Object=MibTableColumn
fgs2924rVlanPortConfDoubleTag=_Fgs2924rVlanPortConfDoubleTag_Object((1,3,6,1,4,1,5205,2,34,1,14,3,1,8),_Fgs2924rVlanPortConfDoubleTag_Type())
fgs2924rVlanPortConfDoubleTag.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rVlanPortConfDoubleTag.setStatus(_A)
_Fgs2924rPortBaseVlanGroup_ObjectIdentity=ObjectIdentity
fgs2924rPortBaseVlanGroup=_Fgs2924rPortBaseVlanGroup_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,14,4))
class _Fgs2924rPortBaseVlanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rPortBaseVlanNumber_Type.__name__=_C
_Fgs2924rPortBaseVlanNumber_Object=MibScalar
fgs2924rPortBaseVlanNumber=_Fgs2924rPortBaseVlanNumber_Object((1,3,6,1,4,1,5205,2,34,1,14,4,1),_Fgs2924rPortBaseVlanNumber_Type())
fgs2924rPortBaseVlanNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rPortBaseVlanNumber.setStatus(_A)
class _Fgs2924rPortBaseVlanGroupEntryCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_Fgs2924rPortBaseVlanGroupEntryCreate_Type.__name__=_C
_Fgs2924rPortBaseVlanGroupEntryCreate_Object=MibScalar
fgs2924rPortBaseVlanGroupEntryCreate=_Fgs2924rPortBaseVlanGroupEntryCreate_Object((1,3,6,1,4,1,5205,2,34,1,14,4,2),_Fgs2924rPortBaseVlanGroupEntryCreate_Type())
fgs2924rPortBaseVlanGroupEntryCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rPortBaseVlanGroupEntryCreate.setStatus(_A)
_Fgs2924rPortBaseVlanGroupTable_Object=MibTable
fgs2924rPortBaseVlanGroupTable=_Fgs2924rPortBaseVlanGroupTable_Object((1,3,6,1,4,1,5205,2,34,1,14,4,3))
if mibBuilder.loadTexts:fgs2924rPortBaseVlanGroupTable.setStatus(_A)
_Fgs2924rPortBaseVlanGroupEntry_Object=MibTableRow
fgs2924rPortBaseVlanGroupEntry=_Fgs2924rPortBaseVlanGroupEntry_Object((1,3,6,1,4,1,5205,2,34,1,14,4,3,1))
fgs2924rPortBaseVlanGroupEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:fgs2924rPortBaseVlanGroupEntry.setStatus(_A)
class _Fgs2924rPortBaseVlanGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rPortBaseVlanGroupIndex_Type.__name__=_C
_Fgs2924rPortBaseVlanGroupIndex_Object=MibTableColumn
fgs2924rPortBaseVlanGroupIndex=_Fgs2924rPortBaseVlanGroupIndex_Object((1,3,6,1,4,1,5205,2,34,1,14,4,3,1,1),_Fgs2924rPortBaseVlanGroupIndex_Type())
fgs2924rPortBaseVlanGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rPortBaseVlanGroupIndex.setStatus(_A)
_Fgs2924rPortBaseVlanGroupName_Type=DisplayString
_Fgs2924rPortBaseVlanGroupName_Object=MibTableColumn
fgs2924rPortBaseVlanGroupName=_Fgs2924rPortBaseVlanGroupName_Object((1,3,6,1,4,1,5205,2,34,1,14,4,3,1,2),_Fgs2924rPortBaseVlanGroupName_Type())
fgs2924rPortBaseVlanGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rPortBaseVlanGroupName.setStatus(_A)
_Fgs2924rPortBaseVlanGroupMembers_Type=DisplayString
_Fgs2924rPortBaseVlanGroupMembers_Object=MibTableColumn
fgs2924rPortBaseVlanGroupMembers=_Fgs2924rPortBaseVlanGroupMembers_Object((1,3,6,1,4,1,5205,2,34,1,14,4,3,1,3),_Fgs2924rPortBaseVlanGroupMembers_Type())
fgs2924rPortBaseVlanGroupMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rPortBaseVlanGroupMembers.setStatus(_A)
class _Fgs2924rPortBaseVlanGroupEntryAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Fgs2924rPortBaseVlanGroupEntryAction_Type.__name__=_C
_Fgs2924rPortBaseVlanGroupEntryAction_Object=MibTableColumn
fgs2924rPortBaseVlanGroupEntryAction=_Fgs2924rPortBaseVlanGroupEntryAction_Object((1,3,6,1,4,1,5205,2,34,1,14,4,3,1,4),_Fgs2924rPortBaseVlanGroupEntryAction_Type())
fgs2924rPortBaseVlanGroupEntryAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rPortBaseVlanGroupEntryAction.setStatus(_A)
_Fgs2924rMacTableInfo_ObjectIdentity=ObjectIdentity
fgs2924rMacTableInfo=_Fgs2924rMacTableInfo_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,15))
_Fgs2924rMacTableConf_ObjectIdentity=ObjectIdentity
fgs2924rMacTableConf=_Fgs2924rMacTableConf_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,15,1))
class _Fgs2924rMacAgeTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000000))
_Fgs2924rMacAgeTime_Type.__name__=_C
_Fgs2924rMacAgeTime_Object=MibScalar
fgs2924rMacAgeTime=_Fgs2924rMacAgeTime_Object((1,3,6,1,4,1,5205,2,34,1,15,1,1),_Fgs2924rMacAgeTime_Type())
fgs2924rMacAgeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMacAgeTime.setStatus(_A)
_Fgs2924rMacTableLearningConfTable_Object=MibTable
fgs2924rMacTableLearningConfTable=_Fgs2924rMacTableLearningConfTable_Object((1,3,6,1,4,1,5205,2,34,1,15,1,2))
if mibBuilder.loadTexts:fgs2924rMacTableLearningConfTable.setStatus(_A)
_Fgs2924rMacTableLearningConfEntry_Object=MibTableRow
fgs2924rMacTableLearningConfEntry=_Fgs2924rMacTableLearningConfEntry_Object((1,3,6,1,4,1,5205,2,34,1,15,1,2,1))
fgs2924rMacTableLearningConfEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:fgs2924rMacTableLearningConfEntry.setStatus(_A)
class _Fgs2924rMacTableLearningConfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rMacTableLearningConfIndex_Type.__name__=_C
_Fgs2924rMacTableLearningConfIndex_Object=MibTableColumn
fgs2924rMacTableLearningConfIndex=_Fgs2924rMacTableLearningConfIndex_Object((1,3,6,1,4,1,5205,2,34,1,15,1,2,1,1),_Fgs2924rMacTableLearningConfIndex_Type())
fgs2924rMacTableLearningConfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rMacTableLearningConfIndex.setStatus(_A)
class _Fgs2924rMacTableLearningConfstate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_Fgs2924rMacTableLearningConfstate_Type.__name__=_C
_Fgs2924rMacTableLearningConfstate_Object=MibTableColumn
fgs2924rMacTableLearningConfstate=_Fgs2924rMacTableLearningConfstate_Object((1,3,6,1,4,1,5205,2,34,1,15,1,2,1,2),_Fgs2924rMacTableLearningConfstate_Type())
fgs2924rMacTableLearningConfstate.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMacTableLearningConfstate.setStatus(_A)
_Fgs2924rMacTableStaticFilter_ObjectIdentity=ObjectIdentity
fgs2924rMacTableStaticFilter=_Fgs2924rMacTableStaticFilter_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,15,2))
class _Fgs2924rMacTableStaticFilterNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512))
_Fgs2924rMacTableStaticFilterNumber_Type.__name__=_C
_Fgs2924rMacTableStaticFilterNumber_Object=MibScalar
fgs2924rMacTableStaticFilterNumber=_Fgs2924rMacTableStaticFilterNumber_Object((1,3,6,1,4,1,5205,2,34,1,15,2,1),_Fgs2924rMacTableStaticFilterNumber_Type())
fgs2924rMacTableStaticFilterNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rMacTableStaticFilterNumber.setStatus(_A)
class _Fgs2924rMacTableStaticFilterEntryCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512))
_Fgs2924rMacTableStaticFilterEntryCreate_Type.__name__=_C
_Fgs2924rMacTableStaticFilterEntryCreate_Object=MibScalar
fgs2924rMacTableStaticFilterEntryCreate=_Fgs2924rMacTableStaticFilterEntryCreate_Object((1,3,6,1,4,1,5205,2,34,1,15,2,2),_Fgs2924rMacTableStaticFilterEntryCreate_Type())
fgs2924rMacTableStaticFilterEntryCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMacTableStaticFilterEntryCreate.setStatus(_A)
_Fgs2924rMacTableStaticFilterTable_Object=MibTable
fgs2924rMacTableStaticFilterTable=_Fgs2924rMacTableStaticFilterTable_Object((1,3,6,1,4,1,5205,2,34,1,15,2,3))
if mibBuilder.loadTexts:fgs2924rMacTableStaticFilterTable.setStatus(_A)
_Fgs2924rMacTableStaticFilterEntry_Object=MibTableRow
fgs2924rMacTableStaticFilterEntry=_Fgs2924rMacTableStaticFilterEntry_Object((1,3,6,1,4,1,5205,2,34,1,15,2,3,1))
fgs2924rMacTableStaticFilterEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:fgs2924rMacTableStaticFilterEntry.setStatus(_A)
class _Fgs2924rMacTableStaticFilterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_Fgs2924rMacTableStaticFilterIndex_Type.__name__=_C
_Fgs2924rMacTableStaticFilterIndex_Object=MibTableColumn
fgs2924rMacTableStaticFilterIndex=_Fgs2924rMacTableStaticFilterIndex_Object((1,3,6,1,4,1,5205,2,34,1,15,2,3,1,1),_Fgs2924rMacTableStaticFilterIndex_Type())
fgs2924rMacTableStaticFilterIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rMacTableStaticFilterIndex.setStatus(_A)
_Fgs2924rMacTableStaticFilterMac_Type=DisplayString
_Fgs2924rMacTableStaticFilterMac_Object=MibTableColumn
fgs2924rMacTableStaticFilterMac=_Fgs2924rMacTableStaticFilterMac_Object((1,3,6,1,4,1,5205,2,34,1,15,2,3,1,2),_Fgs2924rMacTableStaticFilterMac_Type())
fgs2924rMacTableStaticFilterMac.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMacTableStaticFilterMac.setStatus(_A)
class _Fgs2924rMacTableStaticFilterVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Fgs2924rMacTableStaticFilterVid_Type.__name__=_C
_Fgs2924rMacTableStaticFilterVid_Object=MibTableColumn
fgs2924rMacTableStaticFilterVid=_Fgs2924rMacTableStaticFilterVid_Object((1,3,6,1,4,1,5205,2,34,1,15,2,3,1,3),_Fgs2924rMacTableStaticFilterVid_Type())
fgs2924rMacTableStaticFilterVid.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMacTableStaticFilterVid.setStatus(_A)
_Fgs2924rMacTableStaticFilterAlias_Type=DisplayString
_Fgs2924rMacTableStaticFilterAlias_Object=MibTableColumn
fgs2924rMacTableStaticFilterAlias=_Fgs2924rMacTableStaticFilterAlias_Object((1,3,6,1,4,1,5205,2,34,1,15,2,3,1,4),_Fgs2924rMacTableStaticFilterAlias_Type())
fgs2924rMacTableStaticFilterAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMacTableStaticFilterAlias.setStatus(_A)
class _Fgs2924rMacTableStaticFilterEntryAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Fgs2924rMacTableStaticFilterEntryAction_Type.__name__=_C
_Fgs2924rMacTableStaticFilterEntryAction_Object=MibTableColumn
fgs2924rMacTableStaticFilterEntryAction=_Fgs2924rMacTableStaticFilterEntryAction_Object((1,3,6,1,4,1,5205,2,34,1,15,2,3,1,5),_Fgs2924rMacTableStaticFilterEntryAction_Type())
fgs2924rMacTableStaticFilterEntryAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMacTableStaticFilterEntryAction.setStatus(_A)
_Fgs2924rMacTableStaticForward_ObjectIdentity=ObjectIdentity
fgs2924rMacTableStaticForward=_Fgs2924rMacTableStaticForward_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,15,3))
class _Fgs2924rMacTableStaticForwardNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512))
_Fgs2924rMacTableStaticForwardNumber_Type.__name__=_C
_Fgs2924rMacTableStaticForwardNumber_Object=MibScalar
fgs2924rMacTableStaticForwardNumber=_Fgs2924rMacTableStaticForwardNumber_Object((1,3,6,1,4,1,5205,2,34,1,15,3,1),_Fgs2924rMacTableStaticForwardNumber_Type())
fgs2924rMacTableStaticForwardNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rMacTableStaticForwardNumber.setStatus(_A)
class _Fgs2924rMacTableStaticForwardEntryCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512))
_Fgs2924rMacTableStaticForwardEntryCreate_Type.__name__=_C
_Fgs2924rMacTableStaticForwardEntryCreate_Object=MibScalar
fgs2924rMacTableStaticForwardEntryCreate=_Fgs2924rMacTableStaticForwardEntryCreate_Object((1,3,6,1,4,1,5205,2,34,1,15,3,2),_Fgs2924rMacTableStaticForwardEntryCreate_Type())
fgs2924rMacTableStaticForwardEntryCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMacTableStaticForwardEntryCreate.setStatus(_A)
_Fgs2924rMacTableStaticForwardTable_Object=MibTable
fgs2924rMacTableStaticForwardTable=_Fgs2924rMacTableStaticForwardTable_Object((1,3,6,1,4,1,5205,2,34,1,15,3,3))
if mibBuilder.loadTexts:fgs2924rMacTableStaticForwardTable.setStatus(_A)
_Fgs2924rMacTableStaticForwardEntry_Object=MibTableRow
fgs2924rMacTableStaticForwardEntry=_Fgs2924rMacTableStaticForwardEntry_Object((1,3,6,1,4,1,5205,2,34,1,15,3,3,1))
fgs2924rMacTableStaticForwardEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:fgs2924rMacTableStaticForwardEntry.setStatus(_A)
class _Fgs2924rMacTableStaticForwardIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_Fgs2924rMacTableStaticForwardIndex_Type.__name__=_C
_Fgs2924rMacTableStaticForwardIndex_Object=MibTableColumn
fgs2924rMacTableStaticForwardIndex=_Fgs2924rMacTableStaticForwardIndex_Object((1,3,6,1,4,1,5205,2,34,1,15,3,3,1,1),_Fgs2924rMacTableStaticForwardIndex_Type())
fgs2924rMacTableStaticForwardIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rMacTableStaticForwardIndex.setStatus(_A)
_Fgs2924rMacTableStaticForwardMac_Type=DisplayString
_Fgs2924rMacTableStaticForwardMac_Object=MibTableColumn
fgs2924rMacTableStaticForwardMac=_Fgs2924rMacTableStaticForwardMac_Object((1,3,6,1,4,1,5205,2,34,1,15,3,3,1,2),_Fgs2924rMacTableStaticForwardMac_Type())
fgs2924rMacTableStaticForwardMac.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMacTableStaticForwardMac.setStatus(_A)
class _Fgs2924rMacTableStaticForwardPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rMacTableStaticForwardPort_Type.__name__=_C
_Fgs2924rMacTableStaticForwardPort_Object=MibTableColumn
fgs2924rMacTableStaticForwardPort=_Fgs2924rMacTableStaticForwardPort_Object((1,3,6,1,4,1,5205,2,34,1,15,3,3,1,3),_Fgs2924rMacTableStaticForwardPort_Type())
fgs2924rMacTableStaticForwardPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMacTableStaticForwardPort.setStatus(_A)
class _Fgs2924rMacTableStaticForwardVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Fgs2924rMacTableStaticForwardVid_Type.__name__=_C
_Fgs2924rMacTableStaticForwardVid_Object=MibTableColumn
fgs2924rMacTableStaticForwardVid=_Fgs2924rMacTableStaticForwardVid_Object((1,3,6,1,4,1,5205,2,34,1,15,3,3,1,4),_Fgs2924rMacTableStaticForwardVid_Type())
fgs2924rMacTableStaticForwardVid.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMacTableStaticForwardVid.setStatus(_A)
_Fgs2924rMacTableStaticForwardAlias_Type=DisplayString
_Fgs2924rMacTableStaticForwardAlias_Object=MibTableColumn
fgs2924rMacTableStaticForwardAlias=_Fgs2924rMacTableStaticForwardAlias_Object((1,3,6,1,4,1,5205,2,34,1,15,3,3,1,5),_Fgs2924rMacTableStaticForwardAlias_Type())
fgs2924rMacTableStaticForwardAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMacTableStaticForwardAlias.setStatus(_A)
class _Fgs2924rMacTableStaticForwardEntryAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Fgs2924rMacTableStaticForwardEntryAction_Type.__name__=_C
_Fgs2924rMacTableStaticForwardEntryAction_Object=MibTableColumn
fgs2924rMacTableStaticForwardEntryAction=_Fgs2924rMacTableStaticForwardEntryAction_Object((1,3,6,1,4,1,5205,2,34,1,15,3,3,1,6),_Fgs2924rMacTableStaticForwardEntryAction_Type())
fgs2924rMacTableStaticForwardEntryAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMacTableStaticForwardEntryAction.setStatus(_A)
_Fgs2924rMacAlias_ObjectIdentity=ObjectIdentity
fgs2924rMacAlias=_Fgs2924rMacAlias_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,15,4))
class _Fgs2924rMacAliasNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_Fgs2924rMacAliasNumber_Type.__name__=_C
_Fgs2924rMacAliasNumber_Object=MibScalar
fgs2924rMacAliasNumber=_Fgs2924rMacAliasNumber_Object((1,3,6,1,4,1,5205,2,34,1,15,4,1),_Fgs2924rMacAliasNumber_Type())
fgs2924rMacAliasNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rMacAliasNumber.setStatus(_A)
class _Fgs2924rMacAliasEntryCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_Fgs2924rMacAliasEntryCreate_Type.__name__=_C
_Fgs2924rMacAliasEntryCreate_Object=MibScalar
fgs2924rMacAliasEntryCreate=_Fgs2924rMacAliasEntryCreate_Object((1,3,6,1,4,1,5205,2,34,1,15,4,2),_Fgs2924rMacAliasEntryCreate_Type())
fgs2924rMacAliasEntryCreate.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rMacAliasEntryCreate.setStatus(_A)
_Fgs2924rMacAliasTable_Object=MibTable
fgs2924rMacAliasTable=_Fgs2924rMacAliasTable_Object((1,3,6,1,4,1,5205,2,34,1,15,4,3))
if mibBuilder.loadTexts:fgs2924rMacAliasTable.setStatus(_A)
_Fgs2924rMacAliasEntry_Object=MibTableRow
fgs2924rMacAliasEntry=_Fgs2924rMacAliasEntry_Object((1,3,6,1,4,1,5205,2,34,1,15,4,3,1))
fgs2924rMacAliasEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:fgs2924rMacAliasEntry.setStatus(_A)
class _Fgs2924rMacAliasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_Fgs2924rMacAliasIndex_Type.__name__=_C
_Fgs2924rMacAliasIndex_Object=MibTableColumn
fgs2924rMacAliasIndex=_Fgs2924rMacAliasIndex_Object((1,3,6,1,4,1,5205,2,34,1,15,4,3,1,1),_Fgs2924rMacAliasIndex_Type())
fgs2924rMacAliasIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rMacAliasIndex.setStatus(_A)
_Fgs2924rAliasMac_Type=DisplayString
_Fgs2924rAliasMac_Object=MibTableColumn
fgs2924rAliasMac=_Fgs2924rAliasMac_Object((1,3,6,1,4,1,5205,2,34,1,15,4,3,1,2),_Fgs2924rAliasMac_Type())
fgs2924rAliasMac.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAliasMac.setStatus(_A)
_Fgs2924rAliasName_Type=DisplayString
_Fgs2924rAliasName_Object=MibTableColumn
fgs2924rAliasName=_Fgs2924rAliasName_Object((1,3,6,1,4,1,5205,2,34,1,15,4,3,1,3),_Fgs2924rAliasName_Type())
fgs2924rAliasName.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAliasName.setStatus(_A)
class _Fgs2924rMacAliasEntryAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Fgs2924rMacAliasEntryAction_Type.__name__=_C
_Fgs2924rMacAliasEntryAction_Object=MibTableColumn
fgs2924rMacAliasEntryAction=_Fgs2924rMacAliasEntryAction_Object((1,3,6,1,4,1,5205,2,34,1,15,4,3,1,4),_Fgs2924rMacAliasEntryAction_Type())
fgs2924rMacAliasEntryAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMacAliasEntryAction.setStatus(_A)
_Fgs2924rGVRPInfo_ObjectIdentity=ObjectIdentity
fgs2924rGVRPInfo=_Fgs2924rGVRPInfo_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,16))
_Fgs2924rGvrpConf_ObjectIdentity=ObjectIdentity
fgs2924rGvrpConf=_Fgs2924rGvrpConf_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,16,1))
class _Fgs2924rGvrpConfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rGvrpConfState_Type.__name__=_C
_Fgs2924rGvrpConfState_Object=MibScalar
fgs2924rGvrpConfState=_Fgs2924rGvrpConfState_Object((1,3,6,1,4,1,5205,2,34,1,16,1,1),_Fgs2924rGvrpConfState_Type())
fgs2924rGvrpConfState.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rGvrpConfState.setStatus(_A)
_Fgs2924rGvrpConfTable_Object=MibTable
fgs2924rGvrpConfTable=_Fgs2924rGvrpConfTable_Object((1,3,6,1,4,1,5205,2,34,1,16,1,2))
if mibBuilder.loadTexts:fgs2924rGvrpConfTable.setStatus(_A)
_Fgs2924rGvrpConfEntry_Object=MibTableRow
fgs2924rGvrpConfEntry=_Fgs2924rGvrpConfEntry_Object((1,3,6,1,4,1,5205,2,34,1,16,1,2,1))
fgs2924rGvrpConfEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:fgs2924rGvrpConfEntry.setStatus(_A)
class _Fgs2924rGvrpConfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rGvrpConfIndex_Type.__name__=_C
_Fgs2924rGvrpConfIndex_Object=MibTableColumn
fgs2924rGvrpConfIndex=_Fgs2924rGvrpConfIndex_Object((1,3,6,1,4,1,5205,2,34,1,16,1,2,1,1),_Fgs2924rGvrpConfIndex_Type())
fgs2924rGvrpConfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rGvrpConfIndex.setStatus(_A)
class _Fgs2924rGvrpConfJoinTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,100))
_Fgs2924rGvrpConfJoinTime_Type.__name__=_C
_Fgs2924rGvrpConfJoinTime_Object=MibTableColumn
fgs2924rGvrpConfJoinTime=_Fgs2924rGvrpConfJoinTime_Object((1,3,6,1,4,1,5205,2,34,1,16,1,2,1,2),_Fgs2924rGvrpConfJoinTime_Type())
fgs2924rGvrpConfJoinTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rGvrpConfJoinTime.setStatus(_A)
class _Fgs2924rGvrpConfLeaveTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,300))
_Fgs2924rGvrpConfLeaveTime_Type.__name__=_C
_Fgs2924rGvrpConfLeaveTime_Object=MibTableColumn
fgs2924rGvrpConfLeaveTime=_Fgs2924rGvrpConfLeaveTime_Object((1,3,6,1,4,1,5205,2,34,1,16,1,2,1,3),_Fgs2924rGvrpConfLeaveTime_Type())
fgs2924rGvrpConfLeaveTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rGvrpConfLeaveTime.setStatus(_A)
class _Fgs2924rGvrpConfLeaveAllTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,5000))
_Fgs2924rGvrpConfLeaveAllTime_Type.__name__=_C
_Fgs2924rGvrpConfLeaveAllTime_Object=MibTableColumn
fgs2924rGvrpConfLeaveAllTime=_Fgs2924rGvrpConfLeaveAllTime_Object((1,3,6,1,4,1,5205,2,34,1,16,1,2,1,4),_Fgs2924rGvrpConfLeaveAllTime_Type())
fgs2924rGvrpConfLeaveAllTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rGvrpConfLeaveAllTime.setStatus(_A)
class _Fgs2924rGvrpConfDefaultAppMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rGvrpConfDefaultAppMode_Type.__name__=_C
_Fgs2924rGvrpConfDefaultAppMode_Object=MibTableColumn
fgs2924rGvrpConfDefaultAppMode=_Fgs2924rGvrpConfDefaultAppMode_Object((1,3,6,1,4,1,5205,2,34,1,16,1,2,1,5),_Fgs2924rGvrpConfDefaultAppMode_Type())
fgs2924rGvrpConfDefaultAppMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rGvrpConfDefaultAppMode.setStatus(_A)
class _Fgs2924rGvrpConfDefaultRegMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_Fgs2924rGvrpConfDefaultRegMode_Type.__name__=_C
_Fgs2924rGvrpConfDefaultRegMode_Object=MibTableColumn
fgs2924rGvrpConfDefaultRegMode=_Fgs2924rGvrpConfDefaultRegMode_Object((1,3,6,1,4,1,5205,2,34,1,16,1,2,1,6),_Fgs2924rGvrpConfDefaultRegMode_Type())
fgs2924rGvrpConfDefaultRegMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rGvrpConfDefaultRegMode.setStatus(_A)
class _Fgs2924rGvrpConfRestrictedMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rGvrpConfRestrictedMode_Type.__name__=_C
_Fgs2924rGvrpConfRestrictedMode_Object=MibTableColumn
fgs2924rGvrpConfRestrictedMode=_Fgs2924rGvrpConfRestrictedMode_Object((1,3,6,1,4,1,5205,2,34,1,16,1,2,1,7),_Fgs2924rGvrpConfRestrictedMode_Type())
fgs2924rGvrpConfRestrictedMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rGvrpConfRestrictedMode.setStatus(_A)
_Fgs2924rGvrpCounter_ObjectIdentity=ObjectIdentity
fgs2924rGvrpCounter=_Fgs2924rGvrpCounter_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,16,2))
_Fgs2924rGvrpCounterTable_Object=MibTable
fgs2924rGvrpCounterTable=_Fgs2924rGvrpCounterTable_Object((1,3,6,1,4,1,5205,2,34,1,16,2,1))
if mibBuilder.loadTexts:fgs2924rGvrpCounterTable.setStatus(_A)
_Fgs2924rGvrpCounterEntry_Object=MibTableRow
fgs2924rGvrpCounterEntry=_Fgs2924rGvrpCounterEntry_Object((1,3,6,1,4,1,5205,2,34,1,16,2,1,1))
fgs2924rGvrpCounterEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:fgs2924rGvrpCounterEntry.setStatus(_A)
class _Fgs2924rGvrpCounterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rGvrpCounterIndex_Type.__name__=_C
_Fgs2924rGvrpCounterIndex_Object=MibTableColumn
fgs2924rGvrpCounterIndex=_Fgs2924rGvrpCounterIndex_Object((1,3,6,1,4,1,5205,2,34,1,16,2,1,1,1),_Fgs2924rGvrpCounterIndex_Type())
fgs2924rGvrpCounterIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rGvrpCounterIndex.setStatus(_A)
_Fgs2924rGvrpCounterRxTotalGvrpPkts_Type=Counter32
_Fgs2924rGvrpCounterRxTotalGvrpPkts_Object=MibTableColumn
fgs2924rGvrpCounterRxTotalGvrpPkts=_Fgs2924rGvrpCounterRxTotalGvrpPkts_Object((1,3,6,1,4,1,5205,2,34,1,16,2,1,1,2),_Fgs2924rGvrpCounterRxTotalGvrpPkts_Type())
fgs2924rGvrpCounterRxTotalGvrpPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rGvrpCounterRxTotalGvrpPkts.setStatus(_A)
_Fgs2924rGvrpCounterRxInvalidGvrpPkts_Type=Counter32
_Fgs2924rGvrpCounterRxInvalidGvrpPkts_Object=MibTableColumn
fgs2924rGvrpCounterRxInvalidGvrpPkts=_Fgs2924rGvrpCounterRxInvalidGvrpPkts_Object((1,3,6,1,4,1,5205,2,34,1,16,2,1,1,3),_Fgs2924rGvrpCounterRxInvalidGvrpPkts_Type())
fgs2924rGvrpCounterRxInvalidGvrpPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rGvrpCounterRxInvalidGvrpPkts.setStatus(_A)
_Fgs2924rGvrpCounterRxLeaveAllMsg_Type=Counter32
_Fgs2924rGvrpCounterRxLeaveAllMsg_Object=MibTableColumn
fgs2924rGvrpCounterRxLeaveAllMsg=_Fgs2924rGvrpCounterRxLeaveAllMsg_Object((1,3,6,1,4,1,5205,2,34,1,16,2,1,1,4),_Fgs2924rGvrpCounterRxLeaveAllMsg_Type())
fgs2924rGvrpCounterRxLeaveAllMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rGvrpCounterRxLeaveAllMsg.setStatus(_A)
_Fgs2924rGvrpCounterRxJoinEmptyMsg_Type=Counter32
_Fgs2924rGvrpCounterRxJoinEmptyMsg_Object=MibTableColumn
fgs2924rGvrpCounterRxJoinEmptyMsg=_Fgs2924rGvrpCounterRxJoinEmptyMsg_Object((1,3,6,1,4,1,5205,2,34,1,16,2,1,1,5),_Fgs2924rGvrpCounterRxJoinEmptyMsg_Type())
fgs2924rGvrpCounterRxJoinEmptyMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rGvrpCounterRxJoinEmptyMsg.setStatus(_A)
_Fgs2924rGvrpCounterRxJoinInMsg_Type=Counter32
_Fgs2924rGvrpCounterRxJoinInMsg_Object=MibTableColumn
fgs2924rGvrpCounterRxJoinInMsg=_Fgs2924rGvrpCounterRxJoinInMsg_Object((1,3,6,1,4,1,5205,2,34,1,16,2,1,1,6),_Fgs2924rGvrpCounterRxJoinInMsg_Type())
fgs2924rGvrpCounterRxJoinInMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rGvrpCounterRxJoinInMsg.setStatus(_A)
_Fgs2924rGvrpCounterRxLeaveEmptyMsg_Type=Counter32
_Fgs2924rGvrpCounterRxLeaveEmptyMsg_Object=MibTableColumn
fgs2924rGvrpCounterRxLeaveEmptyMsg=_Fgs2924rGvrpCounterRxLeaveEmptyMsg_Object((1,3,6,1,4,1,5205,2,34,1,16,2,1,1,7),_Fgs2924rGvrpCounterRxLeaveEmptyMsg_Type())
fgs2924rGvrpCounterRxLeaveEmptyMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rGvrpCounterRxLeaveEmptyMsg.setStatus(_A)
_Fgs2924rGvrpCounterRxEmptyMsg_Type=Counter32
_Fgs2924rGvrpCounterRxEmptyMsg_Object=MibTableColumn
fgs2924rGvrpCounterRxEmptyMsg=_Fgs2924rGvrpCounterRxEmptyMsg_Object((1,3,6,1,4,1,5205,2,34,1,16,2,1,1,8),_Fgs2924rGvrpCounterRxEmptyMsg_Type())
fgs2924rGvrpCounterRxEmptyMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rGvrpCounterRxEmptyMsg.setStatus(_A)
_Fgs2924rGvrpCounterTxTotalGvrpPkts_Type=Counter32
_Fgs2924rGvrpCounterTxTotalGvrpPkts_Object=MibTableColumn
fgs2924rGvrpCounterTxTotalGvrpPkts=_Fgs2924rGvrpCounterTxTotalGvrpPkts_Object((1,3,6,1,4,1,5205,2,34,1,16,2,1,1,9),_Fgs2924rGvrpCounterTxTotalGvrpPkts_Type())
fgs2924rGvrpCounterTxTotalGvrpPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rGvrpCounterTxTotalGvrpPkts.setStatus(_A)
_Fgs2924rGvrpCounterTxLeaveAllMsg_Type=Counter32
_Fgs2924rGvrpCounterTxLeaveAllMsg_Object=MibTableColumn
fgs2924rGvrpCounterTxLeaveAllMsg=_Fgs2924rGvrpCounterTxLeaveAllMsg_Object((1,3,6,1,4,1,5205,2,34,1,16,2,1,1,10),_Fgs2924rGvrpCounterTxLeaveAllMsg_Type())
fgs2924rGvrpCounterTxLeaveAllMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rGvrpCounterTxLeaveAllMsg.setStatus(_A)
_Fgs2924rGvrpCounterTxJoinEmptyMsg_Type=Counter32
_Fgs2924rGvrpCounterTxJoinEmptyMsg_Object=MibTableColumn
fgs2924rGvrpCounterTxJoinEmptyMsg=_Fgs2924rGvrpCounterTxJoinEmptyMsg_Object((1,3,6,1,4,1,5205,2,34,1,16,2,1,1,11),_Fgs2924rGvrpCounterTxJoinEmptyMsg_Type())
fgs2924rGvrpCounterTxJoinEmptyMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rGvrpCounterTxJoinEmptyMsg.setStatus(_A)
_Fgs2924rGvrpCounterTxJoinInMsg_Type=Counter32
_Fgs2924rGvrpCounterTxJoinInMsg_Object=MibTableColumn
fgs2924rGvrpCounterTxJoinInMsg=_Fgs2924rGvrpCounterTxJoinInMsg_Object((1,3,6,1,4,1,5205,2,34,1,16,2,1,1,12),_Fgs2924rGvrpCounterTxJoinInMsg_Type())
fgs2924rGvrpCounterTxJoinInMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rGvrpCounterTxJoinInMsg.setStatus(_A)
_Fgs2924rGvrpCounterTxLeaveEmptyMsg_Type=Counter32
_Fgs2924rGvrpCounterTxLeaveEmptyMsg_Object=MibTableColumn
fgs2924rGvrpCounterTxLeaveEmptyMsg=_Fgs2924rGvrpCounterTxLeaveEmptyMsg_Object((1,3,6,1,4,1,5205,2,34,1,16,2,1,1,13),_Fgs2924rGvrpCounterTxLeaveEmptyMsg_Type())
fgs2924rGvrpCounterTxLeaveEmptyMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rGvrpCounterTxLeaveEmptyMsg.setStatus(_A)
_Fgs2924rGvrpCounterTxEmptyMsg_Type=Counter32
_Fgs2924rGvrpCounterTxEmptyMsg_Object=MibTableColumn
fgs2924rGvrpCounterTxEmptyMsg=_Fgs2924rGvrpCounterTxEmptyMsg_Object((1,3,6,1,4,1,5205,2,34,1,16,2,1,1,14),_Fgs2924rGvrpCounterTxEmptyMsg_Type())
fgs2924rGvrpCounterTxEmptyMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rGvrpCounterTxEmptyMsg.setStatus(_A)
_Fgs2924rGvrpGroup_ObjectIdentity=ObjectIdentity
fgs2924rGvrpGroup=_Fgs2924rGvrpGroup_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,16,3))
class _Fgs2924rGvrpGroupNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_Fgs2924rGvrpGroupNumber_Type.__name__=_C
_Fgs2924rGvrpGroupNumber_Object=MibScalar
fgs2924rGvrpGroupNumber=_Fgs2924rGvrpGroupNumber_Object((1,3,6,1,4,1,5205,2,34,1,16,3,1),_Fgs2924rGvrpGroupNumber_Type())
fgs2924rGvrpGroupNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rGvrpGroupNumber.setStatus(_A)
_Fgs2924rGvrpGroupTable_Object=MibTable
fgs2924rGvrpGroupTable=_Fgs2924rGvrpGroupTable_Object((1,3,6,1,4,1,5205,2,34,1,16,3,2))
if mibBuilder.loadTexts:fgs2924rGvrpGroupTable.setStatus(_A)
_Fgs2924rGvrpGroupEntry_Object=MibTableRow
fgs2924rGvrpGroupEntry=_Fgs2924rGvrpGroupEntry_Object((1,3,6,1,4,1,5205,2,34,1,16,3,2,1))
fgs2924rGvrpGroupEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:fgs2924rGvrpGroupEntry.setStatus(_A)
class _Fgs2924rGvrpGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Fgs2924rGvrpGroupId_Type.__name__=_C
_Fgs2924rGvrpGroupId_Object=MibTableColumn
fgs2924rGvrpGroupId=_Fgs2924rGvrpGroupId_Object((1,3,6,1,4,1,5205,2,34,1,16,3,2,1,1),_Fgs2924rGvrpGroupId_Type())
fgs2924rGvrpGroupId.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rGvrpGroupId.setStatus(_A)
class _Fgs2924rGvrpGroupVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Fgs2924rGvrpGroupVid_Type.__name__=_C
_Fgs2924rGvrpGroupVid_Object=MibTableColumn
fgs2924rGvrpGroupVid=_Fgs2924rGvrpGroupVid_Object((1,3,6,1,4,1,5205,2,34,1,16,3,2,1,2),_Fgs2924rGvrpGroupVid_Type())
fgs2924rGvrpGroupVid.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rGvrpGroupVid.setStatus(_A)
_Fgs2924rGvrpGroupMemberPort_Type=DisplayString
_Fgs2924rGvrpGroupMemberPort_Object=MibTableColumn
fgs2924rGvrpGroupMemberPort=_Fgs2924rGvrpGroupMemberPort_Object((1,3,6,1,4,1,5205,2,34,1,16,3,2,1,3),_Fgs2924rGvrpGroupMemberPort_Type())
fgs2924rGvrpGroupMemberPort.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rGvrpGroupMemberPort.setStatus(_A)
_Fgs2924rGvrpGroupAdministrativeCtrlTable_Object=MibTable
fgs2924rGvrpGroupAdministrativeCtrlTable=_Fgs2924rGvrpGroupAdministrativeCtrlTable_Object((1,3,6,1,4,1,5205,2,34,1,16,3,3))
if mibBuilder.loadTexts:fgs2924rGvrpGroupAdministrativeCtrlTable.setStatus(_A)
_Fgs2924rGvrpGroupAdministrativeCtrlEntry_Object=MibTableRow
fgs2924rGvrpGroupAdministrativeCtrlEntry=_Fgs2924rGvrpGroupAdministrativeCtrlEntry_Object((1,3,6,1,4,1,5205,2,34,1,16,3,3,1))
fgs2924rGvrpGroupAdministrativeCtrlEntry.setIndexNames((0,_E,_i),(0,_E,_j))
if mibBuilder.loadTexts:fgs2924rGvrpGroupAdministrativeCtrlEntry.setStatus(_A)
class _Fgs2924rGvrpGroupAdministrativeCtrlVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Fgs2924rGvrpGroupAdministrativeCtrlVid_Type.__name__=_C
_Fgs2924rGvrpGroupAdministrativeCtrlVid_Object=MibTableColumn
fgs2924rGvrpGroupAdministrativeCtrlVid=_Fgs2924rGvrpGroupAdministrativeCtrlVid_Object((1,3,6,1,4,1,5205,2,34,1,16,3,3,1,1),_Fgs2924rGvrpGroupAdministrativeCtrlVid_Type())
fgs2924rGvrpGroupAdministrativeCtrlVid.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rGvrpGroupAdministrativeCtrlVid.setStatus(_A)
class _Fgs2924rGvrpGroupAdministrativeCtrlPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rGvrpGroupAdministrativeCtrlPort_Type.__name__=_C
_Fgs2924rGvrpGroupAdministrativeCtrlPort_Object=MibTableColumn
fgs2924rGvrpGroupAdministrativeCtrlPort=_Fgs2924rGvrpGroupAdministrativeCtrlPort_Object((1,3,6,1,4,1,5205,2,34,1,16,3,3,1,2),_Fgs2924rGvrpGroupAdministrativeCtrlPort_Type())
fgs2924rGvrpGroupAdministrativeCtrlPort.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rGvrpGroupAdministrativeCtrlPort.setStatus(_A)
class _Fgs2924rGvrpGroupAdministrativeCtrlApp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rGvrpGroupAdministrativeCtrlApp_Type.__name__=_C
_Fgs2924rGvrpGroupAdministrativeCtrlApp_Object=MibTableColumn
fgs2924rGvrpGroupAdministrativeCtrlApp=_Fgs2924rGvrpGroupAdministrativeCtrlApp_Object((1,3,6,1,4,1,5205,2,34,1,16,3,3,1,3),_Fgs2924rGvrpGroupAdministrativeCtrlApp_Type())
fgs2924rGvrpGroupAdministrativeCtrlApp.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rGvrpGroupAdministrativeCtrlApp.setStatus(_A)
class _Fgs2924rGvrpGroupAdministrativeCtrlReg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Fgs2924rGvrpGroupAdministrativeCtrlReg_Type.__name__=_C
_Fgs2924rGvrpGroupAdministrativeCtrlReg_Object=MibTableColumn
fgs2924rGvrpGroupAdministrativeCtrlReg=_Fgs2924rGvrpGroupAdministrativeCtrlReg_Object((1,3,6,1,4,1,5205,2,34,1,16,3,3,1,4),_Fgs2924rGvrpGroupAdministrativeCtrlReg_Type())
fgs2924rGvrpGroupAdministrativeCtrlReg.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rGvrpGroupAdministrativeCtrlReg.setStatus(_A)
_Fgs2924rQosInfo_ObjectIdentity=ObjectIdentity
fgs2924rQosInfo=_Fgs2924rQosInfo_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,17))
_Fgs2924rQosPortConf_ObjectIdentity=ObjectIdentity
fgs2924rQosPortConf=_Fgs2924rQosPortConf_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,17,1))
class _Fgs2924rQosNumOfClasses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2),ValueRangeConstraint(4,4))
_Fgs2924rQosNumOfClasses_Type.__name__=_C
_Fgs2924rQosNumOfClasses_Object=MibScalar
fgs2924rQosNumOfClasses=_Fgs2924rQosNumOfClasses_Object((1,3,6,1,4,1,5205,2,34,1,17,1,1),_Fgs2924rQosNumOfClasses_Type())
fgs2924rQosNumOfClasses.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosNumOfClasses.setStatus(_A)
_Fgs2924rQosPortConfTable_Object=MibTable
fgs2924rQosPortConfTable=_Fgs2924rQosPortConfTable_Object((1,3,6,1,4,1,5205,2,34,1,17,1,2))
if mibBuilder.loadTexts:fgs2924rQosPortConfTable.setStatus(_A)
_Fgs2924rQosPortConfEntry_Object=MibTableRow
fgs2924rQosPortConfEntry=_Fgs2924rQosPortConfEntry_Object((1,3,6,1,4,1,5205,2,34,1,17,1,2,1))
fgs2924rQosPortConfEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:fgs2924rQosPortConfEntry.setStatus(_A)
class _Fgs2924rQosPortConfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rQosPortConfIndex_Type.__name__=_C
_Fgs2924rQosPortConfIndex_Object=MibTableColumn
fgs2924rQosPortConfIndex=_Fgs2924rQosPortConfIndex_Object((1,3,6,1,4,1,5205,2,34,1,17,1,2,1,1),_Fgs2924rQosPortConfIndex_Type())
fgs2924rQosPortConfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rQosPortConfIndex.setStatus(_A)
class _Fgs2924rQosPortConfDefaultClasses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Fgs2924rQosPortConfDefaultClasses_Type.__name__=_C
_Fgs2924rQosPortConfDefaultClasses_Object=MibTableColumn
fgs2924rQosPortConfDefaultClasses=_Fgs2924rQosPortConfDefaultClasses_Object((1,3,6,1,4,1,5205,2,34,1,17,1,2,1,2),_Fgs2924rQosPortConfDefaultClasses_Type())
fgs2924rQosPortConfDefaultClasses.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosPortConfDefaultClasses.setStatus(_A)
class _Fgs2924rQosPortConfQCL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rQosPortConfQCL_Type.__name__=_C
_Fgs2924rQosPortConfQCL_Object=MibTableColumn
fgs2924rQosPortConfQCL=_Fgs2924rQosPortConfQCL_Object((1,3,6,1,4,1,5205,2,34,1,17,1,2,1,3),_Fgs2924rQosPortConfQCL_Type())
fgs2924rQosPortConfQCL.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosPortConfQCL.setStatus(_A)
class _Fgs2924rQosPortConfUserPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Fgs2924rQosPortConfUserPriority_Type.__name__=_C
_Fgs2924rQosPortConfUserPriority_Object=MibTableColumn
fgs2924rQosPortConfUserPriority=_Fgs2924rQosPortConfUserPriority_Object((1,3,6,1,4,1,5205,2,34,1,17,1,2,1,4),_Fgs2924rQosPortConfUserPriority_Type())
fgs2924rQosPortConfUserPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosPortConfUserPriority.setStatus(_A)
class _Fgs2924rQosPortConfQueuingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rQosPortConfQueuingMode_Type.__name__=_C
_Fgs2924rQosPortConfQueuingMode_Object=MibTableColumn
fgs2924rQosPortConfQueuingMode=_Fgs2924rQosPortConfQueuingMode_Object((1,3,6,1,4,1,5205,2,34,1,17,1,2,1,5),_Fgs2924rQosPortConfQueuingMode_Type())
fgs2924rQosPortConfQueuingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosPortConfQueuingMode.setStatus(_A)
class _Fgs2924rQosPortConfQueueWeightedLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2),ValueRangeConstraint(4,4),ValueRangeConstraint(8,8))
_Fgs2924rQosPortConfQueueWeightedLow_Type.__name__=_C
_Fgs2924rQosPortConfQueueWeightedLow_Object=MibTableColumn
fgs2924rQosPortConfQueueWeightedLow=_Fgs2924rQosPortConfQueueWeightedLow_Object((1,3,6,1,4,1,5205,2,34,1,17,1,2,1,6),_Fgs2924rQosPortConfQueueWeightedLow_Type())
fgs2924rQosPortConfQueueWeightedLow.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosPortConfQueueWeightedLow.setStatus(_A)
class _Fgs2924rQosPortConfQueueWeightedNormal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2),ValueRangeConstraint(4,4),ValueRangeConstraint(8,8))
_Fgs2924rQosPortConfQueueWeightedNormal_Type.__name__=_C
_Fgs2924rQosPortConfQueueWeightedNormal_Object=MibTableColumn
fgs2924rQosPortConfQueueWeightedNormal=_Fgs2924rQosPortConfQueueWeightedNormal_Object((1,3,6,1,4,1,5205,2,34,1,17,1,2,1,7),_Fgs2924rQosPortConfQueueWeightedNormal_Type())
fgs2924rQosPortConfQueueWeightedNormal.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosPortConfQueueWeightedNormal.setStatus(_A)
class _Fgs2924rQosPortConfQueueWeightedMedium_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2),ValueRangeConstraint(4,4),ValueRangeConstraint(8,8))
_Fgs2924rQosPortConfQueueWeightedMedium_Type.__name__=_C
_Fgs2924rQosPortConfQueueWeightedMedium_Object=MibTableColumn
fgs2924rQosPortConfQueueWeightedMedium=_Fgs2924rQosPortConfQueueWeightedMedium_Object((1,3,6,1,4,1,5205,2,34,1,17,1,2,1,8),_Fgs2924rQosPortConfQueueWeightedMedium_Type())
fgs2924rQosPortConfQueueWeightedMedium.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosPortConfQueueWeightedMedium.setStatus(_A)
class _Fgs2924rQosPortConfQueueWeightedHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2),ValueRangeConstraint(4,4),ValueRangeConstraint(8,8))
_Fgs2924rQosPortConfQueueWeightedHigh_Type.__name__=_C
_Fgs2924rQosPortConfQueueWeightedHigh_Object=MibTableColumn
fgs2924rQosPortConfQueueWeightedHigh=_Fgs2924rQosPortConfQueueWeightedHigh_Object((1,3,6,1,4,1,5205,2,34,1,17,1,2,1,9),_Fgs2924rQosPortConfQueueWeightedHigh_Type())
fgs2924rQosPortConfQueueWeightedHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosPortConfQueueWeightedHigh.setStatus(_A)
_Fgs2924rQosRateLimiters_ObjectIdentity=ObjectIdentity
fgs2924rQosRateLimiters=_Fgs2924rQosRateLimiters_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,17,3))
_Fgs2924rQosRateLimitersTable_Object=MibTable
fgs2924rQosRateLimitersTable=_Fgs2924rQosRateLimitersTable_Object((1,3,6,1,4,1,5205,2,34,1,17,3,1))
if mibBuilder.loadTexts:fgs2924rQosRateLimitersTable.setStatus(_A)
_Fgs2924rQosRateLimitersEntry_Object=MibTableRow
fgs2924rQosRateLimitersEntry=_Fgs2924rQosRateLimitersEntry_Object((1,3,6,1,4,1,5205,2,34,1,17,3,1,1))
fgs2924rQosRateLimitersEntry.setIndexNames((0,_E,_l))
if mibBuilder.loadTexts:fgs2924rQosRateLimitersEntry.setStatus(_A)
class _Fgs2924rQosRateLimitersIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rQosRateLimitersIndex_Type.__name__=_C
_Fgs2924rQosRateLimitersIndex_Object=MibTableColumn
fgs2924rQosRateLimitersIndex=_Fgs2924rQosRateLimitersIndex_Object((1,3,6,1,4,1,5205,2,34,1,17,3,1,1,1),_Fgs2924rQosRateLimitersIndex_Type())
fgs2924rQosRateLimitersIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rQosRateLimitersIndex.setStatus(_A)
class _Fgs2924rQosRateLimitersPolicer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rQosRateLimitersPolicer_Type.__name__=_C
_Fgs2924rQosRateLimitersPolicer_Object=MibTableColumn
fgs2924rQosRateLimitersPolicer=_Fgs2924rQosRateLimitersPolicer_Object((1,3,6,1,4,1,5205,2,34,1,17,3,1,1,2),_Fgs2924rQosRateLimitersPolicer_Type())
fgs2924rQosRateLimitersPolicer.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosRateLimitersPolicer.setStatus(_A)
class _Fgs2924rQosRateLimitersPolicerRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000000))
_Fgs2924rQosRateLimitersPolicerRate_Type.__name__=_C
_Fgs2924rQosRateLimitersPolicerRate_Object=MibTableColumn
fgs2924rQosRateLimitersPolicerRate=_Fgs2924rQosRateLimitersPolicerRate_Object((1,3,6,1,4,1,5205,2,34,1,17,3,1,1,3),_Fgs2924rQosRateLimitersPolicerRate_Type())
fgs2924rQosRateLimitersPolicerRate.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosRateLimitersPolicerRate.setStatus(_A)
class _Fgs2924rQosRateLimitersShaper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rQosRateLimitersShaper_Type.__name__=_C
_Fgs2924rQosRateLimitersShaper_Object=MibTableColumn
fgs2924rQosRateLimitersShaper=_Fgs2924rQosRateLimitersShaper_Object((1,3,6,1,4,1,5205,2,34,1,17,3,1,1,4),_Fgs2924rQosRateLimitersShaper_Type())
fgs2924rQosRateLimitersShaper.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosRateLimitersShaper.setStatus(_A)
class _Fgs2924rQosRateLimitersShaperRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000000))
_Fgs2924rQosRateLimitersShaperRate_Type.__name__=_C
_Fgs2924rQosRateLimitersShaperRate_Object=MibTableColumn
fgs2924rQosRateLimitersShaperRate=_Fgs2924rQosRateLimitersShaperRate_Object((1,3,6,1,4,1,5205,2,34,1,17,3,1,1,5),_Fgs2924rQosRateLimitersShaperRate_Type())
fgs2924rQosRateLimitersShaperRate.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosRateLimitersShaperRate.setStatus(_A)
_Fgs2924rQosStormCtrl_ObjectIdentity=ObjectIdentity
fgs2924rQosStormCtrl=_Fgs2924rQosStormCtrl_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,17,4))
class _Fgs2924rQosStromCtrlFloodedUnicastStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rQosStromCtrlFloodedUnicastStatus_Type.__name__=_C
_Fgs2924rQosStromCtrlFloodedUnicastStatus_Object=MibScalar
fgs2924rQosStromCtrlFloodedUnicastStatus=_Fgs2924rQosStromCtrlFloodedUnicastStatus_Object((1,3,6,1,4,1,5205,2,34,1,17,4,1),_Fgs2924rQosStromCtrlFloodedUnicastStatus_Type())
fgs2924rQosStromCtrlFloodedUnicastStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosStromCtrlFloodedUnicastStatus.setStatus(_A)
_Fgs2924rQosStromCtrlFloodedUnicastRate_Type=DisplayString
_Fgs2924rQosStromCtrlFloodedUnicastRate_Object=MibScalar
fgs2924rQosStromCtrlFloodedUnicastRate=_Fgs2924rQosStromCtrlFloodedUnicastRate_Object((1,3,6,1,4,1,5205,2,34,1,17,4,2),_Fgs2924rQosStromCtrlFloodedUnicastRate_Type())
fgs2924rQosStromCtrlFloodedUnicastRate.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosStromCtrlFloodedUnicastRate.setStatus(_A)
class _Fgs2924rQosStromCtrlMulticastStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rQosStromCtrlMulticastStatus_Type.__name__=_C
_Fgs2924rQosStromCtrlMulticastStatus_Object=MibScalar
fgs2924rQosStromCtrlMulticastStatus=_Fgs2924rQosStromCtrlMulticastStatus_Object((1,3,6,1,4,1,5205,2,34,1,17,4,3),_Fgs2924rQosStromCtrlMulticastStatus_Type())
fgs2924rQosStromCtrlMulticastStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosStromCtrlMulticastStatus.setStatus(_A)
_Fgs2924rQosStromCtrlMulticastRate_Type=DisplayString
_Fgs2924rQosStromCtrlMulticastRate_Object=MibScalar
fgs2924rQosStromCtrlMulticastRate=_Fgs2924rQosStromCtrlMulticastRate_Object((1,3,6,1,4,1,5205,2,34,1,17,4,4),_Fgs2924rQosStromCtrlMulticastRate_Type())
fgs2924rQosStromCtrlMulticastRate.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosStromCtrlMulticastRate.setStatus(_A)
class _Fgs2924rQosStromCtrlBroadcastStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rQosStromCtrlBroadcastStatus_Type.__name__=_C
_Fgs2924rQosStromCtrlBroadcastStatus_Object=MibScalar
fgs2924rQosStromCtrlBroadcastStatus=_Fgs2924rQosStromCtrlBroadcastStatus_Object((1,3,6,1,4,1,5205,2,34,1,17,4,5),_Fgs2924rQosStromCtrlBroadcastStatus_Type())
fgs2924rQosStromCtrlBroadcastStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosStromCtrlBroadcastStatus.setStatus(_A)
_Fgs2924rQosStromCtrlBroadcastRate_Type=DisplayString
_Fgs2924rQosStromCtrlBroadcastRate_Object=MibScalar
fgs2924rQosStromCtrlBroadcastRate=_Fgs2924rQosStromCtrlBroadcastRate_Object((1,3,6,1,4,1,5205,2,34,1,17,4,6),_Fgs2924rQosStromCtrlBroadcastRate_Type())
fgs2924rQosStromCtrlBroadcastRate.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosStromCtrlBroadcastRate.setStatus(_A)
_Fgs2924rQosQCL_ObjectIdentity=ObjectIdentity
fgs2924rQosQCL=_Fgs2924rQosQCL_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,17,5))
class _Fgs2924rQosQclCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rQosQclCreate_Type.__name__=_C
_Fgs2924rQosQclCreate_Object=MibScalar
fgs2924rQosQclCreate=_Fgs2924rQosQclCreate_Object((1,3,6,1,4,1,5205,2,34,1,17,5,1),_Fgs2924rQosQclCreate_Type())
fgs2924rQosQclCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosQclCreate.setStatus(_A)
_Fgs2924rQosQclTable_Object=MibTable
fgs2924rQosQclTable=_Fgs2924rQosQclTable_Object((1,3,6,1,4,1,5205,2,34,1,17,5,2))
if mibBuilder.loadTexts:fgs2924rQosQclTable.setStatus(_A)
_Fgs2924rQosQclEntry_Object=MibTableRow
fgs2924rQosQclEntry=_Fgs2924rQosQclEntry_Object((1,3,6,1,4,1,5205,2,34,1,17,5,2,1))
fgs2924rQosQclEntry.setIndexNames((0,_E,_m),(0,_E,_n))
if mibBuilder.loadTexts:fgs2924rQosQclEntry.setStatus(_A)
class _Fgs2924rQosQclNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rQosQclNo_Type.__name__=_C
_Fgs2924rQosQclNo_Object=MibTableColumn
fgs2924rQosQclNo=_Fgs2924rQosQclNo_Object((1,3,6,1,4,1,5205,2,34,1,17,5,2,1,1),_Fgs2924rQosQclNo_Type())
fgs2924rQosQclNo.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rQosQclNo.setStatus(_A)
class _Fgs2924rQosQclQceListNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rQosQclQceListNo_Type.__name__=_C
_Fgs2924rQosQclQceListNo_Object=MibTableColumn
fgs2924rQosQclQceListNo=_Fgs2924rQosQclQceListNo_Object((1,3,6,1,4,1,5205,2,34,1,17,5,2,1,2),_Fgs2924rQosQclQceListNo_Type())
fgs2924rQosQclQceListNo.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rQosQclQceListNo.setStatus(_A)
class _Fgs2924rQosQclQceMoveTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rQosQclQceMoveTo_Type.__name__=_C
_Fgs2924rQosQclQceMoveTo_Object=MibTableColumn
fgs2924rQosQclQceMoveTo=_Fgs2924rQosQclQceMoveTo_Object((1,3,6,1,4,1,5205,2,34,1,17,5,2,1,3),_Fgs2924rQosQclQceMoveTo_Type())
fgs2924rQosQclQceMoveTo.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rQosQclQceMoveTo.setStatus(_A)
class _Fgs2924rQosQclQceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_Fgs2924rQosQclQceType_Type.__name__=_C
_Fgs2924rQosQclQceType_Object=MibTableColumn
fgs2924rQosQclQceType=_Fgs2924rQosQclQceType_Object((1,3,6,1,4,1,5205,2,34,1,17,5,2,1,4),_Fgs2924rQosQclQceType_Type())
fgs2924rQosQclQceType.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosQclQceType.setStatus(_A)
_Fgs2924rQosQclQceValue_Type=DisplayString
_Fgs2924rQosQclQceValue_Object=MibTableColumn
fgs2924rQosQclQceValue=_Fgs2924rQosQclQceValue_Object((1,3,6,1,4,1,5205,2,34,1,17,5,2,1,5),_Fgs2924rQosQclQceValue_Type())
fgs2924rQosQclQceValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosQclQceValue.setStatus(_A)
_Fgs2924rQosQclQceTrafficClass_Type=DisplayString
_Fgs2924rQosQclQceTrafficClass_Object=MibTableColumn
fgs2924rQosQclQceTrafficClass=_Fgs2924rQosQclQceTrafficClass_Object((1,3,6,1,4,1,5205,2,34,1,17,5,2,1,6),_Fgs2924rQosQclQceTrafficClass_Type())
fgs2924rQosQclQceTrafficClass.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosQclQceTrafficClass.setStatus(_A)
_Fgs2924rQosQclQcePriority0Class_Type=DisplayString
_Fgs2924rQosQclQcePriority0Class_Object=MibTableColumn
fgs2924rQosQclQcePriority0Class=_Fgs2924rQosQclQcePriority0Class_Object((1,3,6,1,4,1,5205,2,34,1,17,5,2,1,7),_Fgs2924rQosQclQcePriority0Class_Type())
fgs2924rQosQclQcePriority0Class.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosQclQcePriority0Class.setStatus(_A)
_Fgs2924rQosQclQcePriority1Class_Type=DisplayString
_Fgs2924rQosQclQcePriority1Class_Object=MibTableColumn
fgs2924rQosQclQcePriority1Class=_Fgs2924rQosQclQcePriority1Class_Object((1,3,6,1,4,1,5205,2,34,1,17,5,2,1,8),_Fgs2924rQosQclQcePriority1Class_Type())
fgs2924rQosQclQcePriority1Class.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosQclQcePriority1Class.setStatus(_A)
_Fgs2924rQosQclQcePriority2Class_Type=DisplayString
_Fgs2924rQosQclQcePriority2Class_Object=MibTableColumn
fgs2924rQosQclQcePriority2Class=_Fgs2924rQosQclQcePriority2Class_Object((1,3,6,1,4,1,5205,2,34,1,17,5,2,1,9),_Fgs2924rQosQclQcePriority2Class_Type())
fgs2924rQosQclQcePriority2Class.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosQclQcePriority2Class.setStatus(_A)
_Fgs2924rQosQclQcePriority3Class_Type=DisplayString
_Fgs2924rQosQclQcePriority3Class_Object=MibTableColumn
fgs2924rQosQclQcePriority3Class=_Fgs2924rQosQclQcePriority3Class_Object((1,3,6,1,4,1,5205,2,34,1,17,5,2,1,10),_Fgs2924rQosQclQcePriority3Class_Type())
fgs2924rQosQclQcePriority3Class.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosQclQcePriority3Class.setStatus(_A)
_Fgs2924rQosQclQcePriority4Class_Type=DisplayString
_Fgs2924rQosQclQcePriority4Class_Object=MibTableColumn
fgs2924rQosQclQcePriority4Class=_Fgs2924rQosQclQcePriority4Class_Object((1,3,6,1,4,1,5205,2,34,1,17,5,2,1,11),_Fgs2924rQosQclQcePriority4Class_Type())
fgs2924rQosQclQcePriority4Class.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosQclQcePriority4Class.setStatus(_A)
_Fgs2924rQosQclQcePriority5Class_Type=DisplayString
_Fgs2924rQosQclQcePriority5Class_Object=MibTableColumn
fgs2924rQosQclQcePriority5Class=_Fgs2924rQosQclQcePriority5Class_Object((1,3,6,1,4,1,5205,2,34,1,17,5,2,1,12),_Fgs2924rQosQclQcePriority5Class_Type())
fgs2924rQosQclQcePriority5Class.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosQclQcePriority5Class.setStatus(_A)
_Fgs2924rQosQclQcePriority6Class_Type=DisplayString
_Fgs2924rQosQclQcePriority6Class_Object=MibTableColumn
fgs2924rQosQclQcePriority6Class=_Fgs2924rQosQclQcePriority6Class_Object((1,3,6,1,4,1,5205,2,34,1,17,5,2,1,13),_Fgs2924rQosQclQcePriority6Class_Type())
fgs2924rQosQclQcePriority6Class.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosQclQcePriority6Class.setStatus(_A)
_Fgs2924rQosQclQcePriority7Class_Type=DisplayString
_Fgs2924rQosQclQcePriority7Class_Object=MibTableColumn
fgs2924rQosQclQcePriority7Class=_Fgs2924rQosQclQcePriority7Class_Object((1,3,6,1,4,1,5205,2,34,1,17,5,2,1,14),_Fgs2924rQosQclQcePriority7Class_Type())
fgs2924rQosQclQcePriority7Class.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosQclQcePriority7Class.setStatus(_A)
class _Fgs2924rQosQclQceEntryAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Fgs2924rQosQclQceEntryAction_Type.__name__=_C
_Fgs2924rQosQclQceEntryAction_Object=MibTableColumn
fgs2924rQosQclQceEntryAction=_Fgs2924rQosQclQceEntryAction_Object((1,3,6,1,4,1,5205,2,34,1,17,5,2,1,15),_Fgs2924rQosQclQceEntryAction_Type())
fgs2924rQosQclQceEntryAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rQosQclQceEntryAction.setStatus(_A)
_Fgs2924rAclInfo_ObjectIdentity=ObjectIdentity
fgs2924rAclInfo=_Fgs2924rAclInfo_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,18))
_Fgs2924rAclPortsConfTable_Object=MibTable
fgs2924rAclPortsConfTable=_Fgs2924rAclPortsConfTable_Object((1,3,6,1,4,1,5205,2,34,1,18,1))
if mibBuilder.loadTexts:fgs2924rAclPortsConfTable.setStatus(_A)
_Fgs2924rAclPortsConfEntry_Object=MibTableRow
fgs2924rAclPortsConfEntry=_Fgs2924rAclPortsConfEntry_Object((1,3,6,1,4,1,5205,2,34,1,18,1,1))
fgs2924rAclPortsConfEntry.setIndexNames((0,_E,_o))
if mibBuilder.loadTexts:fgs2924rAclPortsConfEntry.setStatus(_A)
class _Fgs2924rAclPortsConfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rAclPortsConfIndex_Type.__name__=_C
_Fgs2924rAclPortsConfIndex_Object=MibTableColumn
fgs2924rAclPortsConfIndex=_Fgs2924rAclPortsConfIndex_Object((1,3,6,1,4,1,5205,2,34,1,18,1,1,1),_Fgs2924rAclPortsConfIndex_Type())
fgs2924rAclPortsConfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rAclPortsConfIndex.setStatus(_A)
class _Fgs2924rAclPortsConfPolicyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Fgs2924rAclPortsConfPolicyId_Type.__name__=_C
_Fgs2924rAclPortsConfPolicyId_Object=MibTableColumn
fgs2924rAclPortsConfPolicyId=_Fgs2924rAclPortsConfPolicyId_Object((1,3,6,1,4,1,5205,2,34,1,18,1,1,2),_Fgs2924rAclPortsConfPolicyId_Type())
fgs2924rAclPortsConfPolicyId.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAclPortsConfPolicyId.setStatus(_A)
class _Fgs2924rAclPortsConfAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rAclPortsConfAction_Type.__name__=_C
_Fgs2924rAclPortsConfAction_Object=MibTableColumn
fgs2924rAclPortsConfAction=_Fgs2924rAclPortsConfAction_Object((1,3,6,1,4,1,5205,2,34,1,18,1,1,3),_Fgs2924rAclPortsConfAction_Type())
fgs2924rAclPortsConfAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAclPortsConfAction.setStatus(_A)
class _Fgs2924rAclPortsConfRateLimiterId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_Fgs2924rAclPortsConfRateLimiterId_Type.__name__=_C
_Fgs2924rAclPortsConfRateLimiterId_Object=MibTableColumn
fgs2924rAclPortsConfRateLimiterId=_Fgs2924rAclPortsConfRateLimiterId_Object((1,3,6,1,4,1,5205,2,34,1,18,1,1,4),_Fgs2924rAclPortsConfRateLimiterId_Type())
fgs2924rAclPortsConfRateLimiterId.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAclPortsConfRateLimiterId.setStatus(_A)
class _Fgs2924rAclPortsConfPortCopy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_Fgs2924rAclPortsConfPortCopy_Type.__name__=_C
_Fgs2924rAclPortsConfPortCopy_Object=MibTableColumn
fgs2924rAclPortsConfPortCopy=_Fgs2924rAclPortsConfPortCopy_Object((1,3,6,1,4,1,5205,2,34,1,18,1,1,5),_Fgs2924rAclPortsConfPortCopy_Type())
fgs2924rAclPortsConfPortCopy.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAclPortsConfPortCopy.setStatus(_A)
_Fgs2924rAclPortsConfCounter_Type=Counter32
_Fgs2924rAclPortsConfCounter_Object=MibTableColumn
fgs2924rAclPortsConfCounter=_Fgs2924rAclPortsConfCounter_Object((1,3,6,1,4,1,5205,2,34,1,18,1,1,6),_Fgs2924rAclPortsConfCounter_Type())
fgs2924rAclPortsConfCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rAclPortsConfCounter.setStatus(_A)
_Fgs2924rAclRateLimiter_ObjectIdentity=ObjectIdentity
fgs2924rAclRateLimiter=_Fgs2924rAclRateLimiter_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,18,2))
_Fgs2924rAclRateLimiterTable_Object=MibTable
fgs2924rAclRateLimiterTable=_Fgs2924rAclRateLimiterTable_Object((1,3,6,1,4,1,5205,2,34,1,18,2,1))
if mibBuilder.loadTexts:fgs2924rAclRateLimiterTable.setStatus(_A)
_Fgs2924rAclRateLimiterEntry_Object=MibTableRow
fgs2924rAclRateLimiterEntry=_Fgs2924rAclRateLimiterEntry_Object((1,3,6,1,4,1,5205,2,34,1,18,2,1,1))
fgs2924rAclRateLimiterEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:fgs2924rAclRateLimiterEntry.setStatus(_A)
class _Fgs2924rAclRateLimiterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rAclRateLimiterIndex_Type.__name__=_C
_Fgs2924rAclRateLimiterIndex_Object=MibTableColumn
fgs2924rAclRateLimiterIndex=_Fgs2924rAclRateLimiterIndex_Object((1,3,6,1,4,1,5205,2,34,1,18,2,1,1,1),_Fgs2924rAclRateLimiterIndex_Type())
fgs2924rAclRateLimiterIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rAclRateLimiterIndex.setStatus(_A)
_Fgs2924rAclRateLimiterRate_Type=DisplayString
_Fgs2924rAclRateLimiterRate_Object=MibTableColumn
fgs2924rAclRateLimiterRate=_Fgs2924rAclRateLimiterRate_Object((1,3,6,1,4,1,5205,2,34,1,18,2,1,1,2),_Fgs2924rAclRateLimiterRate_Type())
fgs2924rAclRateLimiterRate.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAclRateLimiterRate.setStatus(_A)
_Fgs2924rAclInfoViewTable_Object=MibTable
fgs2924rAclInfoViewTable=_Fgs2924rAclInfoViewTable_Object((1,3,6,1,4,1,5205,2,34,1,18,3))
if mibBuilder.loadTexts:fgs2924rAclInfoViewTable.setStatus(_A)
_Fgs2924rAclInfoViewEntry_Object=MibTableRow
fgs2924rAclInfoViewEntry=_Fgs2924rAclInfoViewEntry_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1))
fgs2924rAclInfoViewEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:fgs2924rAclInfoViewEntry.setStatus(_A)
class _Fgs2924rAclInfoViewNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Fgs2924rAclInfoViewNo_Type.__name__=_C
_Fgs2924rAclInfoViewNo_Object=MibTableColumn
fgs2924rAclInfoViewNo=_Fgs2924rAclInfoViewNo_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,1),_Fgs2924rAclInfoViewNo_Type())
fgs2924rAclInfoViewNo.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rAclInfoViewNo.setStatus(_A)
_Fgs2924rAceIngressPort_Type=DisplayString
_Fgs2924rAceIngressPort_Object=MibTableColumn
fgs2924rAceIngressPort=_Fgs2924rAceIngressPort_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,2),_Fgs2924rAceIngressPort_Type())
fgs2924rAceIngressPort.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rAceIngressPort.setStatus(_A)
_Fgs2924rAceFrameType_Type=DisplayString
_Fgs2924rAceFrameType_Object=MibTableColumn
fgs2924rAceFrameType=_Fgs2924rAceFrameType_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,3),_Fgs2924rAceFrameType_Type())
fgs2924rAceFrameType.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rAceFrameType.setStatus(_A)
_Fgs2924rAceAction_Type=DisplayString
_Fgs2924rAceAction_Object=MibTableColumn
fgs2924rAceAction=_Fgs2924rAceAction_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,4),_Fgs2924rAceAction_Type())
fgs2924rAceAction.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rAceAction.setStatus(_A)
_Fgs2924rAceRateLimiter_Type=DisplayString
_Fgs2924rAceRateLimiter_Object=MibTableColumn
fgs2924rAceRateLimiter=_Fgs2924rAceRateLimiter_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,5),_Fgs2924rAceRateLimiter_Type())
fgs2924rAceRateLimiter.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rAceRateLimiter.setStatus(_A)
_Fgs2924rAcePortCopy_Type=DisplayString
_Fgs2924rAcePortCopy_Object=MibTableColumn
fgs2924rAcePortCopy=_Fgs2924rAcePortCopy_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,6),_Fgs2924rAcePortCopy_Type())
fgs2924rAcePortCopy.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rAcePortCopy.setStatus(_A)
_Fgs2924rAceCounter_Type=Counter32
_Fgs2924rAceCounter_Object=MibTableColumn
fgs2924rAceCounter=_Fgs2924rAceCounter_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,7),_Fgs2924rAceCounter_Type())
fgs2924rAceCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rAceCounter.setStatus(_A)
_Fgs2924rSmacFilter_Type=DisplayString
_Fgs2924rSmacFilter_Object=MibTableColumn
fgs2924rSmacFilter=_Fgs2924rSmacFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,8),_Fgs2924rSmacFilter_Type())
fgs2924rSmacFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rSmacFilter.setStatus(_A)
_Fgs2924rDmacFilter_Type=DisplayString
_Fgs2924rDmacFilter_Object=MibTableColumn
fgs2924rDmacFilter=_Fgs2924rDmacFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,9),_Fgs2924rDmacFilter_Type())
fgs2924rDmacFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDmacFilter.setStatus(_A)
_Fgs2924rVlanIdFilter_Type=DisplayString
_Fgs2924rVlanIdFilter_Object=MibTableColumn
fgs2924rVlanIdFilter=_Fgs2924rVlanIdFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,10),_Fgs2924rVlanIdFilter_Type())
fgs2924rVlanIdFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rVlanIdFilter.setStatus(_A)
_Fgs2924rVlanTagPriority_Type=DisplayString
_Fgs2924rVlanTagPriority_Object=MibTableColumn
fgs2924rVlanTagPriority=_Fgs2924rVlanTagPriority_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,11),_Fgs2924rVlanTagPriority_Type())
fgs2924rVlanTagPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rVlanTagPriority.setStatus(_A)
_Fgs2924rEtherTypeFilter_Type=DisplayString
_Fgs2924rEtherTypeFilter_Object=MibTableColumn
fgs2924rEtherTypeFilter=_Fgs2924rEtherTypeFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,12),_Fgs2924rEtherTypeFilter_Type())
fgs2924rEtherTypeFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rEtherTypeFilter.setStatus(_A)
_Fgs2924rArpRarp_Type=DisplayString
_Fgs2924rArpRarp_Object=MibTableColumn
fgs2924rArpRarp=_Fgs2924rArpRarp_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,13),_Fgs2924rArpRarp_Type())
fgs2924rArpRarp.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rArpRarp.setStatus(_A)
_Fgs2924rArpRequestReply_Type=DisplayString
_Fgs2924rArpRequestReply_Object=MibTableColumn
fgs2924rArpRequestReply=_Fgs2924rArpRequestReply_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,14),_Fgs2924rArpRequestReply_Type())
fgs2924rArpRequestReply.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rArpRequestReply.setStatus(_A)
_Fgs2924rArpSenderIpFilter_Type=DisplayString
_Fgs2924rArpSenderIpFilter_Object=MibTableColumn
fgs2924rArpSenderIpFilter=_Fgs2924rArpSenderIpFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,15),_Fgs2924rArpSenderIpFilter_Type())
fgs2924rArpSenderIpFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rArpSenderIpFilter.setStatus(_A)
_Fgs2924rArpSenderIpAddress_Type=DisplayString
_Fgs2924rArpSenderIpAddress_Object=MibTableColumn
fgs2924rArpSenderIpAddress=_Fgs2924rArpSenderIpAddress_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,16),_Fgs2924rArpSenderIpAddress_Type())
fgs2924rArpSenderIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rArpSenderIpAddress.setStatus(_A)
_Fgs2924rArpSenderIpMask_Type=DisplayString
_Fgs2924rArpSenderIpMask_Object=MibTableColumn
fgs2924rArpSenderIpMask=_Fgs2924rArpSenderIpMask_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,17),_Fgs2924rArpSenderIpMask_Type())
fgs2924rArpSenderIpMask.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rArpSenderIpMask.setStatus(_A)
_Fgs2924rArpTargetIpFilter_Type=DisplayString
_Fgs2924rArpTargetIpFilter_Object=MibTableColumn
fgs2924rArpTargetIpFilter=_Fgs2924rArpTargetIpFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,18),_Fgs2924rArpTargetIpFilter_Type())
fgs2924rArpTargetIpFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rArpTargetIpFilter.setStatus(_A)
_Fgs2924rArpTargetIpAddress_Type=DisplayString
_Fgs2924rArpTargetIpAddress_Object=MibTableColumn
fgs2924rArpTargetIpAddress=_Fgs2924rArpTargetIpAddress_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,19),_Fgs2924rArpTargetIpAddress_Type())
fgs2924rArpTargetIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rArpTargetIpAddress.setStatus(_A)
_Fgs2924rArpTargetIpMask_Type=DisplayString
_Fgs2924rArpTargetIpMask_Object=MibTableColumn
fgs2924rArpTargetIpMask=_Fgs2924rArpTargetIpMask_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,20),_Fgs2924rArpTargetIpMask_Type())
fgs2924rArpTargetIpMask.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rArpTargetIpMask.setStatus(_A)
_Fgs2924rArpSmacMatch_Type=DisplayString
_Fgs2924rArpSmacMatch_Object=MibTableColumn
fgs2924rArpSmacMatch=_Fgs2924rArpSmacMatch_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,21),_Fgs2924rArpSmacMatch_Type())
fgs2924rArpSmacMatch.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rArpSmacMatch.setStatus(_A)
_Fgs2924rArpRarpDmacMatch_Type=DisplayString
_Fgs2924rArpRarpDmacMatch_Object=MibTableColumn
fgs2924rArpRarpDmacMatch=_Fgs2924rArpRarpDmacMatch_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,22),_Fgs2924rArpRarpDmacMatch_Type())
fgs2924rArpRarpDmacMatch.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rArpRarpDmacMatch.setStatus(_A)
_Fgs2924rArpIpEthernetLength_Type=DisplayString
_Fgs2924rArpIpEthernetLength_Object=MibTableColumn
fgs2924rArpIpEthernetLength=_Fgs2924rArpIpEthernetLength_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,23),_Fgs2924rArpIpEthernetLength_Type())
fgs2924rArpIpEthernetLength.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rArpIpEthernetLength.setStatus(_A)
_Fgs2924rArpIp_Type=DisplayString
_Fgs2924rArpIp_Object=MibTableColumn
fgs2924rArpIp=_Fgs2924rArpIp_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,24),_Fgs2924rArpIp_Type())
fgs2924rArpIp.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rArpIp.setStatus(_A)
_Fgs2924rArpEthernet_Type=DisplayString
_Fgs2924rArpEthernet_Object=MibTableColumn
fgs2924rArpEthernet=_Fgs2924rArpEthernet_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,25),_Fgs2924rArpEthernet_Type())
fgs2924rArpEthernet.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rArpEthernet.setStatus(_A)
_Fgs2924rIpProtocolFilter_Type=DisplayString
_Fgs2924rIpProtocolFilter_Object=MibTableColumn
fgs2924rIpProtocolFilter=_Fgs2924rIpProtocolFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,26),_Fgs2924rIpProtocolFilter_Type())
fgs2924rIpProtocolFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rIpProtocolFilter.setStatus(_A)
_Fgs2924rIpProtocolValue_Type=DisplayString
_Fgs2924rIpProtocolValue_Object=MibTableColumn
fgs2924rIpProtocolValue=_Fgs2924rIpProtocolValue_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,27),_Fgs2924rIpProtocolValue_Type())
fgs2924rIpProtocolValue.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rIpProtocolValue.setStatus(_A)
_Fgs2924rIpTTL_Type=DisplayString
_Fgs2924rIpTTL_Object=MibTableColumn
fgs2924rIpTTL=_Fgs2924rIpTTL_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,28),_Fgs2924rIpTTL_Type())
fgs2924rIpTTL.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rIpTTL.setStatus(_A)
_Fgs2924rIpFragment_Type=DisplayString
_Fgs2924rIpFragment_Object=MibTableColumn
fgs2924rIpFragment=_Fgs2924rIpFragment_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,29),_Fgs2924rIpFragment_Type())
fgs2924rIpFragment.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rIpFragment.setStatus(_A)
_Fgs2924rIpOption_Type=DisplayString
_Fgs2924rIpOption_Object=MibTableColumn
fgs2924rIpOption=_Fgs2924rIpOption_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,30),_Fgs2924rIpOption_Type())
fgs2924rIpOption.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rIpOption.setStatus(_A)
_Fgs2924rSipFilter_Type=DisplayString
_Fgs2924rSipFilter_Object=MibTableColumn
fgs2924rSipFilter=_Fgs2924rSipFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,31),_Fgs2924rSipFilter_Type())
fgs2924rSipFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rSipFilter.setStatus(_A)
_Fgs2924rSipAddress_Type=DisplayString
_Fgs2924rSipAddress_Object=MibTableColumn
fgs2924rSipAddress=_Fgs2924rSipAddress_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,32),_Fgs2924rSipAddress_Type())
fgs2924rSipAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rSipAddress.setStatus(_A)
_Fgs2924rSipMask_Type=DisplayString
_Fgs2924rSipMask_Object=MibTableColumn
fgs2924rSipMask=_Fgs2924rSipMask_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,33),_Fgs2924rSipMask_Type())
fgs2924rSipMask.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rSipMask.setStatus(_A)
_Fgs2924rDipFilter_Type=DisplayString
_Fgs2924rDipFilter_Object=MibTableColumn
fgs2924rDipFilter=_Fgs2924rDipFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,34),_Fgs2924rDipFilter_Type())
fgs2924rDipFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDipFilter.setStatus(_A)
_Fgs2924rDipAddress_Type=DisplayString
_Fgs2924rDipAddress_Object=MibTableColumn
fgs2924rDipAddress=_Fgs2924rDipAddress_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,35),_Fgs2924rDipAddress_Type())
fgs2924rDipAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDipAddress.setStatus(_A)
_Fgs2924rDipMask_Type=DisplayString
_Fgs2924rDipMask_Object=MibTableColumn
fgs2924rDipMask=_Fgs2924rDipMask_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,36),_Fgs2924rDipMask_Type())
fgs2924rDipMask.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDipMask.setStatus(_A)
_Fgs2924rIcmpTypeFilter_Type=DisplayString
_Fgs2924rIcmpTypeFilter_Object=MibTableColumn
fgs2924rIcmpTypeFilter=_Fgs2924rIcmpTypeFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,37),_Fgs2924rIcmpTypeFilter_Type())
fgs2924rIcmpTypeFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rIcmpTypeFilter.setStatus(_A)
_Fgs2924rIcmpCodeFilter_Type=DisplayString
_Fgs2924rIcmpCodeFilter_Object=MibTableColumn
fgs2924rIcmpCodeFilter=_Fgs2924rIcmpCodeFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,38),_Fgs2924rIcmpCodeFilter_Type())
fgs2924rIcmpCodeFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rIcmpCodeFilter.setStatus(_A)
_Fgs2924rUdpSourcePortFilter_Type=DisplayString
_Fgs2924rUdpSourcePortFilter_Object=MibTableColumn
fgs2924rUdpSourcePortFilter=_Fgs2924rUdpSourcePortFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,39),_Fgs2924rUdpSourcePortFilter_Type())
fgs2924rUdpSourcePortFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rUdpSourcePortFilter.setStatus(_A)
_Fgs2924rUdpDestPortFilter_Type=DisplayString
_Fgs2924rUdpDestPortFilter_Object=MibTableColumn
fgs2924rUdpDestPortFilter=_Fgs2924rUdpDestPortFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,40),_Fgs2924rUdpDestPortFilter_Type())
fgs2924rUdpDestPortFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rUdpDestPortFilter.setStatus(_A)
_Fgs2924rTcpSourcePortFilter_Type=DisplayString
_Fgs2924rTcpSourcePortFilter_Object=MibTableColumn
fgs2924rTcpSourcePortFilter=_Fgs2924rTcpSourcePortFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,41),_Fgs2924rTcpSourcePortFilter_Type())
fgs2924rTcpSourcePortFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rTcpSourcePortFilter.setStatus(_A)
_Fgs2924rTcpDestPortFilter_Type=DisplayString
_Fgs2924rTcpDestPortFilter_Object=MibTableColumn
fgs2924rTcpDestPortFilter=_Fgs2924rTcpDestPortFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,42),_Fgs2924rTcpDestPortFilter_Type())
fgs2924rTcpDestPortFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rTcpDestPortFilter.setStatus(_A)
_Fgs2924rTcpFIN_Type=DisplayString
_Fgs2924rTcpFIN_Object=MibTableColumn
fgs2924rTcpFIN=_Fgs2924rTcpFIN_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,43),_Fgs2924rTcpFIN_Type())
fgs2924rTcpFIN.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rTcpFIN.setStatus(_A)
_Fgs2924rTcpSYN_Type=DisplayString
_Fgs2924rTcpSYN_Object=MibTableColumn
fgs2924rTcpSYN=_Fgs2924rTcpSYN_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,44),_Fgs2924rTcpSYN_Type())
fgs2924rTcpSYN.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rTcpSYN.setStatus(_A)
_Fgs2924rTcpRST_Type=DisplayString
_Fgs2924rTcpRST_Object=MibTableColumn
fgs2924rTcpRST=_Fgs2924rTcpRST_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,45),_Fgs2924rTcpRST_Type())
fgs2924rTcpRST.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rTcpRST.setStatus(_A)
_Fgs2924rTcpPSH_Type=DisplayString
_Fgs2924rTcpPSH_Object=MibTableColumn
fgs2924rTcpPSH=_Fgs2924rTcpPSH_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,46),_Fgs2924rTcpPSH_Type())
fgs2924rTcpPSH.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rTcpPSH.setStatus(_A)
_Fgs2924rTcpACK_Type=DisplayString
_Fgs2924rTcpACK_Object=MibTableColumn
fgs2924rTcpACK=_Fgs2924rTcpACK_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,47),_Fgs2924rTcpACK_Type())
fgs2924rTcpACK.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rTcpACK.setStatus(_A)
_Fgs2924rTcpURG_Type=DisplayString
_Fgs2924rTcpURG_Object=MibTableColumn
fgs2924rTcpURG=_Fgs2924rTcpURG_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,48),_Fgs2924rTcpURG_Type())
fgs2924rTcpURG.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rTcpURG.setStatus(_A)
class _Fgs2924rAclInfoEntryAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Fgs2924rAclInfoEntryAction_Type.__name__=_C
_Fgs2924rAclInfoEntryAction_Object=MibTableColumn
fgs2924rAclInfoEntryAction=_Fgs2924rAclInfoEntryAction_Object((1,3,6,1,4,1,5205,2,34,1,18,3,1,49),_Fgs2924rAclInfoEntryAction_Type())
fgs2924rAclInfoEntryAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAclInfoEntryAction.setStatus(_A)
_Fgs2924rAclInfoConf_ObjectIdentity=ObjectIdentity
fgs2924rAclInfoConf=_Fgs2924rAclInfoConf_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,18,4))
class _Fgs2924rAceNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Fgs2924rAceNo_Type.__name__=_C
_Fgs2924rAceNo_Object=MibScalar
fgs2924rAceNo=_Fgs2924rAceNo_Object((1,3,6,1,4,1,5205,2,34,1,18,4,1),_Fgs2924rAceNo_Type())
fgs2924rAceNo.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceNo.setStatus(_A)
class _Fgs2924rAceMoveTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Fgs2924rAceMoveTo_Type.__name__=_C
_Fgs2924rAceMoveTo_Object=MibScalar
fgs2924rAceMoveTo=_Fgs2924rAceMoveTo_Object((1,3,6,1,4,1,5205,2,34,1,18,4,2),_Fgs2924rAceMoveTo_Type())
fgs2924rAceMoveTo.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceMoveTo.setStatus(_A)
_Fgs2924rAceIngressPortConf_Type=DisplayString
_Fgs2924rAceIngressPortConf_Object=MibScalar
fgs2924rAceIngressPortConf=_Fgs2924rAceIngressPortConf_Object((1,3,6,1,4,1,5205,2,34,1,18,4,3),_Fgs2924rAceIngressPortConf_Type())
fgs2924rAceIngressPortConf.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceIngressPortConf.setStatus(_A)
class _Fgs2924rAceFrameTypeConf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Fgs2924rAceFrameTypeConf_Type.__name__=_C
_Fgs2924rAceFrameTypeConf_Object=MibScalar
fgs2924rAceFrameTypeConf=_Fgs2924rAceFrameTypeConf_Object((1,3,6,1,4,1,5205,2,34,1,18,4,4),_Fgs2924rAceFrameTypeConf_Type())
fgs2924rAceFrameTypeConf.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceFrameTypeConf.setStatus(_A)
_Fgs2924rAceFrameTypeParameters_ObjectIdentity=ObjectIdentity
fgs2924rAceFrameTypeParameters=_Fgs2924rAceFrameTypeParameters_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,18,4,5))
_Fgs2924rEthernetTypeFilter_Type=DisplayString
_Fgs2924rEthernetTypeFilter_Object=MibScalar
fgs2924rEthernetTypeFilter=_Fgs2924rEthernetTypeFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,1),_Fgs2924rEthernetTypeFilter_Type())
fgs2924rEthernetTypeFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rEthernetTypeFilter.setStatus(_A)
_Fgs2924rAclArpParameters_ObjectIdentity=ObjectIdentity
fgs2924rAclArpParameters=_Fgs2924rAclArpParameters_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,18,4,5,2))
class _Fgs2924rAceArpRarp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Fgs2924rAceArpRarp_Type.__name__=_C
_Fgs2924rAceArpRarp_Object=MibScalar
fgs2924rAceArpRarp=_Fgs2924rAceArpRarp_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,2,1),_Fgs2924rAceArpRarp_Type())
fgs2924rAceArpRarp.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceArpRarp.setStatus(_A)
class _Fgs2924rAceArpRequestReply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Fgs2924rAceArpRequestReply_Type.__name__=_C
_Fgs2924rAceArpRequestReply_Object=MibScalar
fgs2924rAceArpRequestReply=_Fgs2924rAceArpRequestReply_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,2,2),_Fgs2924rAceArpRequestReply_Type())
fgs2924rAceArpRequestReply.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceArpRequestReply.setStatus(_A)
class _Fgs2924rAceArpSenderIpFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Fgs2924rAceArpSenderIpFilter_Type.__name__=_C
_Fgs2924rAceArpSenderIpFilter_Object=MibScalar
fgs2924rAceArpSenderIpFilter=_Fgs2924rAceArpSenderIpFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,2,3),_Fgs2924rAceArpSenderIpFilter_Type())
fgs2924rAceArpSenderIpFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceArpSenderIpFilter.setStatus(_A)
_Fgs2924rAceArpSenderIpAddress_Type=DisplayString
_Fgs2924rAceArpSenderIpAddress_Object=MibScalar
fgs2924rAceArpSenderIpAddress=_Fgs2924rAceArpSenderIpAddress_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,2,4),_Fgs2924rAceArpSenderIpAddress_Type())
fgs2924rAceArpSenderIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceArpSenderIpAddress.setStatus(_A)
_Fgs2924rAceArpSenderIpMask_Type=DisplayString
_Fgs2924rAceArpSenderIpMask_Object=MibScalar
fgs2924rAceArpSenderIpMask=_Fgs2924rAceArpSenderIpMask_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,2,5),_Fgs2924rAceArpSenderIpMask_Type())
fgs2924rAceArpSenderIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceArpSenderIpMask.setStatus(_A)
class _Fgs2924rAceArpTargetIpFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Fgs2924rAceArpTargetIpFilter_Type.__name__=_C
_Fgs2924rAceArpTargetIpFilter_Object=MibScalar
fgs2924rAceArpTargetIpFilter=_Fgs2924rAceArpTargetIpFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,2,6),_Fgs2924rAceArpTargetIpFilter_Type())
fgs2924rAceArpTargetIpFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceArpTargetIpFilter.setStatus(_A)
_Fgs2924rAceArpTargetIpAddress_Type=DisplayString
_Fgs2924rAceArpTargetIpAddress_Object=MibScalar
fgs2924rAceArpTargetIpAddress=_Fgs2924rAceArpTargetIpAddress_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,2,7),_Fgs2924rAceArpTargetIpAddress_Type())
fgs2924rAceArpTargetIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceArpTargetIpAddress.setStatus(_A)
_Fgs2924rAceArpTargetIpMask_Type=DisplayString
_Fgs2924rAceArpTargetIpMask_Object=MibScalar
fgs2924rAceArpTargetIpMask=_Fgs2924rAceArpTargetIpMask_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,2,8),_Fgs2924rAceArpTargetIpMask_Type())
fgs2924rAceArpTargetIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceArpTargetIpMask.setStatus(_A)
_Fgs2924rAceArpSmacMatch_Type=DisplayString
_Fgs2924rAceArpSmacMatch_Object=MibScalar
fgs2924rAceArpSmacMatch=_Fgs2924rAceArpSmacMatch_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,2,9),_Fgs2924rAceArpSmacMatch_Type())
fgs2924rAceArpSmacMatch.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceArpSmacMatch.setStatus(_A)
_Fgs2924rAceArpRarpDmacMatch_Type=DisplayString
_Fgs2924rAceArpRarpDmacMatch_Object=MibScalar
fgs2924rAceArpRarpDmacMatch=_Fgs2924rAceArpRarpDmacMatch_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,2,10),_Fgs2924rAceArpRarpDmacMatch_Type())
fgs2924rAceArpRarpDmacMatch.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceArpRarpDmacMatch.setStatus(_A)
_Fgs2924rAceArpIpEthernetLength_Type=DisplayString
_Fgs2924rAceArpIpEthernetLength_Object=MibScalar
fgs2924rAceArpIpEthernetLength=_Fgs2924rAceArpIpEthernetLength_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,2,11),_Fgs2924rAceArpIpEthernetLength_Type())
fgs2924rAceArpIpEthernetLength.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceArpIpEthernetLength.setStatus(_A)
_Fgs2924rAceArpIp_Type=DisplayString
_Fgs2924rAceArpIp_Object=MibScalar
fgs2924rAceArpIp=_Fgs2924rAceArpIp_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,2,12),_Fgs2924rAceArpIp_Type())
fgs2924rAceArpIp.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceArpIp.setStatus(_A)
_Fgs2924rAceArpEthernet_Type=DisplayString
_Fgs2924rAceArpEthernet_Object=MibScalar
fgs2924rAceArpEthernet=_Fgs2924rAceArpEthernet_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,2,13),_Fgs2924rAceArpEthernet_Type())
fgs2924rAceArpEthernet.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceArpEthernet.setStatus(_A)
_Fgs2924rAclIpParameters_ObjectIdentity=ObjectIdentity
fgs2924rAclIpParameters=_Fgs2924rAclIpParameters_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,18,4,5,3))
class _Fgs2924rAceIpProtocolFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_Fgs2924rAceIpProtocolFilter_Type.__name__=_C
_Fgs2924rAceIpProtocolFilter_Object=MibScalar
fgs2924rAceIpProtocolFilter=_Fgs2924rAceIpProtocolFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,1),_Fgs2924rAceIpProtocolFilter_Type())
fgs2924rAceIpProtocolFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceIpProtocolFilter.setStatus(_A)
_Fgs2924rAceIpProtocolFilterParameters_ObjectIdentity=ObjectIdentity
fgs2924rAceIpProtocolFilterParameters=_Fgs2924rAceIpProtocolFilterParameters_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,2))
_Fgs2924rAceIcmpParameters_ObjectIdentity=ObjectIdentity
fgs2924rAceIcmpParameters=_Fgs2924rAceIcmpParameters_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,2,1))
_Fgs2924rAceIcmpTypeFilter_Type=DisplayString
_Fgs2924rAceIcmpTypeFilter_Object=MibScalar
fgs2924rAceIcmpTypeFilter=_Fgs2924rAceIcmpTypeFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,2,1,1),_Fgs2924rAceIcmpTypeFilter_Type())
fgs2924rAceIcmpTypeFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceIcmpTypeFilter.setStatus(_A)
_Fgs2924rAceIcmpCodeFilter_Type=DisplayString
_Fgs2924rAceIcmpCodeFilter_Object=MibScalar
fgs2924rAceIcmpCodeFilter=_Fgs2924rAceIcmpCodeFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,2,1,2),_Fgs2924rAceIcmpCodeFilter_Type())
fgs2924rAceIcmpCodeFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceIcmpCodeFilter.setStatus(_A)
_Fgs2924rAceUdpParameters_ObjectIdentity=ObjectIdentity
fgs2924rAceUdpParameters=_Fgs2924rAceUdpParameters_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,2,2))
_Fgs2924rUdpSourcePortFilterConf_Type=DisplayString
_Fgs2924rUdpSourcePortFilterConf_Object=MibScalar
fgs2924rUdpSourcePortFilterConf=_Fgs2924rUdpSourcePortFilterConf_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,2,2,1),_Fgs2924rUdpSourcePortFilterConf_Type())
fgs2924rUdpSourcePortFilterConf.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rUdpSourcePortFilterConf.setStatus(_A)
_Fgs2924rUdpDestPortFilterConf_Type=DisplayString
_Fgs2924rUdpDestPortFilterConf_Object=MibScalar
fgs2924rUdpDestPortFilterConf=_Fgs2924rUdpDestPortFilterConf_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,2,2,2),_Fgs2924rUdpDestPortFilterConf_Type())
fgs2924rUdpDestPortFilterConf.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rUdpDestPortFilterConf.setStatus(_A)
_Fgs2924rAceTcpParameters_ObjectIdentity=ObjectIdentity
fgs2924rAceTcpParameters=_Fgs2924rAceTcpParameters_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,2,3))
_Fgs2924rTcpSourcePortFilterConf_Type=DisplayString
_Fgs2924rTcpSourcePortFilterConf_Object=MibScalar
fgs2924rTcpSourcePortFilterConf=_Fgs2924rTcpSourcePortFilterConf_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,2,3,1),_Fgs2924rTcpSourcePortFilterConf_Type())
fgs2924rTcpSourcePortFilterConf.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rTcpSourcePortFilterConf.setStatus(_A)
_Fgs2924rTcpDestPortFilterConf_Type=DisplayString
_Fgs2924rTcpDestPortFilterConf_Object=MibScalar
fgs2924rTcpDestPortFilterConf=_Fgs2924rTcpDestPortFilterConf_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,2,3,2),_Fgs2924rTcpDestPortFilterConf_Type())
fgs2924rTcpDestPortFilterConf.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rTcpDestPortFilterConf.setStatus(_A)
_Fgs2924rTcpFINConf_Type=DisplayString
_Fgs2924rTcpFINConf_Object=MibScalar
fgs2924rTcpFINConf=_Fgs2924rTcpFINConf_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,2,3,3),_Fgs2924rTcpFINConf_Type())
fgs2924rTcpFINConf.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rTcpFINConf.setStatus(_A)
_Fgs2924rTcpSYNConf_Type=DisplayString
_Fgs2924rTcpSYNConf_Object=MibScalar
fgs2924rTcpSYNConf=_Fgs2924rTcpSYNConf_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,2,3,4),_Fgs2924rTcpSYNConf_Type())
fgs2924rTcpSYNConf.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rTcpSYNConf.setStatus(_A)
_Fgs2924rTcpRSTConf_Type=DisplayString
_Fgs2924rTcpRSTConf_Object=MibScalar
fgs2924rTcpRSTConf=_Fgs2924rTcpRSTConf_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,2,3,5),_Fgs2924rTcpRSTConf_Type())
fgs2924rTcpRSTConf.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rTcpRSTConf.setStatus(_A)
_Fgs2924rTcpPSHConf_Type=DisplayString
_Fgs2924rTcpPSHConf_Object=MibScalar
fgs2924rTcpPSHConf=_Fgs2924rTcpPSHConf_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,2,3,6),_Fgs2924rTcpPSHConf_Type())
fgs2924rTcpPSHConf.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rTcpPSHConf.setStatus(_A)
_Fgs2924rTcpACKConf_Type=DisplayString
_Fgs2924rTcpACKConf_Object=MibScalar
fgs2924rTcpACKConf=_Fgs2924rTcpACKConf_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,2,3,7),_Fgs2924rTcpACKConf_Type())
fgs2924rTcpACKConf.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rTcpACKConf.setStatus(_A)
_Fgs2924rTcpURGConf_Type=DisplayString
_Fgs2924rTcpURGConf_Object=MibScalar
fgs2924rTcpURGConf=_Fgs2924rTcpURGConf_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,2,3,8),_Fgs2924rTcpURGConf_Type())
fgs2924rTcpURGConf.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rTcpURGConf.setStatus(_A)
class _Fgs2924rAceIpProtocolValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_Fgs2924rAceIpProtocolValue_Type.__name__=_C
_Fgs2924rAceIpProtocolValue_Object=MibScalar
fgs2924rAceIpProtocolValue=_Fgs2924rAceIpProtocolValue_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,3),_Fgs2924rAceIpProtocolValue_Type())
fgs2924rAceIpProtocolValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceIpProtocolValue.setStatus(_A)
_Fgs2924rAceIpTTL_Type=DisplayString
_Fgs2924rAceIpTTL_Object=MibScalar
fgs2924rAceIpTTL=_Fgs2924rAceIpTTL_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,4),_Fgs2924rAceIpTTL_Type())
fgs2924rAceIpTTL.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceIpTTL.setStatus(_A)
_Fgs2924rAceIpFragment_Type=DisplayString
_Fgs2924rAceIpFragment_Object=MibScalar
fgs2924rAceIpFragment=_Fgs2924rAceIpFragment_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,5),_Fgs2924rAceIpFragment_Type())
fgs2924rAceIpFragment.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceIpFragment.setStatus(_A)
_Fgs2924rAceIpOption_Type=DisplayString
_Fgs2924rAceIpOption_Object=MibScalar
fgs2924rAceIpOption=_Fgs2924rAceIpOption_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,6),_Fgs2924rAceIpOption_Type())
fgs2924rAceIpOption.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceIpOption.setStatus(_A)
class _Fgs2924rAceSipFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Fgs2924rAceSipFilter_Type.__name__=_C
_Fgs2924rAceSipFilter_Object=MibScalar
fgs2924rAceSipFilter=_Fgs2924rAceSipFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,7),_Fgs2924rAceSipFilter_Type())
fgs2924rAceSipFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceSipFilter.setStatus(_A)
_Fgs2924rAceSipAddress_Type=DisplayString
_Fgs2924rAceSipAddress_Object=MibScalar
fgs2924rAceSipAddress=_Fgs2924rAceSipAddress_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,8),_Fgs2924rAceSipAddress_Type())
fgs2924rAceSipAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceSipAddress.setStatus(_A)
_Fgs2924rAceSipMask_Type=DisplayString
_Fgs2924rAceSipMask_Object=MibScalar
fgs2924rAceSipMask=_Fgs2924rAceSipMask_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,9),_Fgs2924rAceSipMask_Type())
fgs2924rAceSipMask.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceSipMask.setStatus(_A)
class _Fgs2924rAceDipFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Fgs2924rAceDipFilter_Type.__name__=_C
_Fgs2924rAceDipFilter_Object=MibScalar
fgs2924rAceDipFilter=_Fgs2924rAceDipFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,10),_Fgs2924rAceDipFilter_Type())
fgs2924rAceDipFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceDipFilter.setStatus(_A)
_Fgs2924rAceDipAddress_Type=DisplayString
_Fgs2924rAceDipAddress_Object=MibScalar
fgs2924rAceDipAddress=_Fgs2924rAceDipAddress_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,11),_Fgs2924rAceDipAddress_Type())
fgs2924rAceDipAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceDipAddress.setStatus(_A)
_Fgs2924rAceDipMask_Type=DisplayString
_Fgs2924rAceDipMask_Object=MibScalar
fgs2924rAceDipMask=_Fgs2924rAceDipMask_Object((1,3,6,1,4,1,5205,2,34,1,18,4,5,3,12),_Fgs2924rAceDipMask_Type())
fgs2924rAceDipMask.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceDipMask.setStatus(_A)
class _Fgs2924rAceActionConf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rAceActionConf_Type.__name__=_C
_Fgs2924rAceActionConf_Object=MibScalar
fgs2924rAceActionConf=_Fgs2924rAceActionConf_Object((1,3,6,1,4,1,5205,2,34,1,18,4,6),_Fgs2924rAceActionConf_Type())
fgs2924rAceActionConf.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceActionConf.setStatus(_A)
class _Fgs2924rAceRateLimiterConf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_Fgs2924rAceRateLimiterConf_Type.__name__=_C
_Fgs2924rAceRateLimiterConf_Object=MibScalar
fgs2924rAceRateLimiterConf=_Fgs2924rAceRateLimiterConf_Object((1,3,6,1,4,1,5205,2,34,1,18,4,7),_Fgs2924rAceRateLimiterConf_Type())
fgs2924rAceRateLimiterConf.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceRateLimiterConf.setStatus(_A)
class _Fgs2924rAcePortCopyConf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_Fgs2924rAcePortCopyConf_Type.__name__=_C
_Fgs2924rAcePortCopyConf_Object=MibScalar
fgs2924rAcePortCopyConf=_Fgs2924rAcePortCopyConf_Object((1,3,6,1,4,1,5205,2,34,1,18,4,8),_Fgs2924rAcePortCopyConf_Type())
fgs2924rAcePortCopyConf.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAcePortCopyConf.setStatus(_A)
_Fgs2924rAceMacParameters_ObjectIdentity=ObjectIdentity
fgs2924rAceMacParameters=_Fgs2924rAceMacParameters_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,18,4,9))
_Fgs2924rAceSmacFilter_Type=DisplayString
_Fgs2924rAceSmacFilter_Object=MibScalar
fgs2924rAceSmacFilter=_Fgs2924rAceSmacFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,4,9,1),_Fgs2924rAceSmacFilter_Type())
fgs2924rAceSmacFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceSmacFilter.setStatus(_A)
_Fgs2924rAceDmacFilter_Type=DisplayString
_Fgs2924rAceDmacFilter_Object=MibScalar
fgs2924rAceDmacFilter=_Fgs2924rAceDmacFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,4,9,2),_Fgs2924rAceDmacFilter_Type())
fgs2924rAceDmacFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceDmacFilter.setStatus(_A)
_Fgs2924rAceVlanParameters_ObjectIdentity=ObjectIdentity
fgs2924rAceVlanParameters=_Fgs2924rAceVlanParameters_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,18,4,10))
_Fgs2924rAceVlanIdFilter_Type=DisplayString
_Fgs2924rAceVlanIdFilter_Object=MibScalar
fgs2924rAceVlanIdFilter=_Fgs2924rAceVlanIdFilter_Object((1,3,6,1,4,1,5205,2,34,1,18,4,10,1),_Fgs2924rAceVlanIdFilter_Type())
fgs2924rAceVlanIdFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceVlanIdFilter.setStatus(_A)
_Fgs2924rAceTagPriority_Type=DisplayString
_Fgs2924rAceTagPriority_Object=MibScalar
fgs2924rAceTagPriority=_Fgs2924rAceTagPriority_Object((1,3,6,1,4,1,5205,2,34,1,18,4,10,2),_Fgs2924rAceTagPriority_Type())
fgs2924rAceTagPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceTagPriority.setStatus(_A)
class _Fgs2924rAceInfoEntryAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Fgs2924rAceInfoEntryAction_Type.__name__=_C
_Fgs2924rAceInfoEntryAction_Object=MibScalar
fgs2924rAceInfoEntryAction=_Fgs2924rAceInfoEntryAction_Object((1,3,6,1,4,1,5205,2,34,1,18,4,11),_Fgs2924rAceInfoEntryAction_Type())
fgs2924rAceInfoEntryAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rAceInfoEntryAction.setStatus(_A)
_Fgs2924rIpMacBind_ObjectIdentity=ObjectIdentity
fgs2924rIpMacBind=_Fgs2924rIpMacBind_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,19))
_Fgs2924rIpMacBindConf_ObjectIdentity=ObjectIdentity
fgs2924rIpMacBindConf=_Fgs2924rIpMacBindConf_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,19,1))
class _Fgs2924rIpMacBindstate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rIpMacBindstate_Type.__name__=_C
_Fgs2924rIpMacBindstate_Object=MibScalar
fgs2924rIpMacBindstate=_Fgs2924rIpMacBindstate_Object((1,3,6,1,4,1,5205,2,34,1,19,1,1),_Fgs2924rIpMacBindstate_Type())
fgs2924rIpMacBindstate.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIpMacBindstate.setStatus(_A)
_Fgs2924rIpMacBindTrustPort_Type=DisplayString
_Fgs2924rIpMacBindTrustPort_Object=MibScalar
fgs2924rIpMacBindTrustPort=_Fgs2924rIpMacBindTrustPort_Object((1,3,6,1,4,1,5205,2,34,1,19,1,2),_Fgs2924rIpMacBindTrustPort_Type())
fgs2924rIpMacBindTrustPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIpMacBindTrustPort.setStatus(_A)
_Fgs2924rIpMacBindSetting_ObjectIdentity=ObjectIdentity
fgs2924rIpMacBindSetting=_Fgs2924rIpMacBindSetting_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,19,2))
class _Fgs2924rIpMacBindSettingNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_Fgs2924rIpMacBindSettingNumber_Type.__name__=_C
_Fgs2924rIpMacBindSettingNumber_Object=MibScalar
fgs2924rIpMacBindSettingNumber=_Fgs2924rIpMacBindSettingNumber_Object((1,3,6,1,4,1,5205,2,34,1,19,2,1),_Fgs2924rIpMacBindSettingNumber_Type())
fgs2924rIpMacBindSettingNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIpMacBindSettingNumber.setStatus(_A)
class _Fgs2924rIpMacBindSettingEntryCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rIpMacBindSettingEntryCreate_Type.__name__=_C
_Fgs2924rIpMacBindSettingEntryCreate_Object=MibScalar
fgs2924rIpMacBindSettingEntryCreate=_Fgs2924rIpMacBindSettingEntryCreate_Object((1,3,6,1,4,1,5205,2,34,1,19,2,2),_Fgs2924rIpMacBindSettingEntryCreate_Type())
fgs2924rIpMacBindSettingEntryCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIpMacBindSettingEntryCreate.setStatus(_A)
_Fgs2924rIpMacBindSettingTable_Object=MibTable
fgs2924rIpMacBindSettingTable=_Fgs2924rIpMacBindSettingTable_Object((1,3,6,1,4,1,5205,2,34,1,19,2,3))
if mibBuilder.loadTexts:fgs2924rIpMacBindSettingTable.setStatus(_A)
_Fgs2924rIpMacBindSettingEntry_Object=MibTableRow
fgs2924rIpMacBindSettingEntry=_Fgs2924rIpMacBindSettingEntry_Object((1,3,6,1,4,1,5205,2,34,1,19,2,3,1))
fgs2924rIpMacBindSettingEntry.setIndexNames((0,_E,_r))
if mibBuilder.loadTexts:fgs2924rIpMacBindSettingEntry.setStatus(_A)
class _Fgs2924rIpMacBindSettingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_Fgs2924rIpMacBindSettingIndex_Type.__name__=_C
_Fgs2924rIpMacBindSettingIndex_Object=MibTableColumn
fgs2924rIpMacBindSettingIndex=_Fgs2924rIpMacBindSettingIndex_Object((1,3,6,1,4,1,5205,2,34,1,19,2,3,1,1),_Fgs2924rIpMacBindSettingIndex_Type())
fgs2924rIpMacBindSettingIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rIpMacBindSettingIndex.setStatus(_A)
_Fgs2924rIpMacBindSettingMAC_Type=DisplayString
_Fgs2924rIpMacBindSettingMAC_Object=MibTableColumn
fgs2924rIpMacBindSettingMAC=_Fgs2924rIpMacBindSettingMAC_Object((1,3,6,1,4,1,5205,2,34,1,19,2,3,1,2),_Fgs2924rIpMacBindSettingMAC_Type())
fgs2924rIpMacBindSettingMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIpMacBindSettingMAC.setStatus(_A)
_Fgs2924rIpMacBindSettingIP_Type=IpAddress
_Fgs2924rIpMacBindSettingIP_Object=MibTableColumn
fgs2924rIpMacBindSettingIP=_Fgs2924rIpMacBindSettingIP_Object((1,3,6,1,4,1,5205,2,34,1,19,2,3,1,3),_Fgs2924rIpMacBindSettingIP_Type())
fgs2924rIpMacBindSettingIP.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIpMacBindSettingIP.setStatus(_A)
class _Fgs2924rIpMacBindSettingPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rIpMacBindSettingPort_Type.__name__=_C
_Fgs2924rIpMacBindSettingPort_Object=MibTableColumn
fgs2924rIpMacBindSettingPort=_Fgs2924rIpMacBindSettingPort_Object((1,3,6,1,4,1,5205,2,34,1,19,2,3,1,4),_Fgs2924rIpMacBindSettingPort_Type())
fgs2924rIpMacBindSettingPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIpMacBindSettingPort.setStatus(_A)
class _Fgs2924rIpMacBindSettingVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Fgs2924rIpMacBindSettingVID_Type.__name__=_C
_Fgs2924rIpMacBindSettingVID_Object=MibTableColumn
fgs2924rIpMacBindSettingVID=_Fgs2924rIpMacBindSettingVID_Object((1,3,6,1,4,1,5205,2,34,1,19,2,3,1,5),_Fgs2924rIpMacBindSettingVID_Type())
fgs2924rIpMacBindSettingVID.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIpMacBindSettingVID.setStatus(_A)
class _Fgs2924rIpMacBindSettingEntryAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Fgs2924rIpMacBindSettingEntryAction_Type.__name__=_C
_Fgs2924rIpMacBindSettingEntryAction_Object=MibTableColumn
fgs2924rIpMacBindSettingEntryAction=_Fgs2924rIpMacBindSettingEntryAction_Object((1,3,6,1,4,1,5205,2,34,1,19,2,3,1,6),_Fgs2924rIpMacBindSettingEntryAction_Type())
fgs2924rIpMacBindSettingEntryAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIpMacBindSettingEntryAction.setStatus(_A)
_Fgs2924rTrapEntry_ObjectIdentity=ObjectIdentity
fgs2924rTrapEntry=_Fgs2924rTrapEntry_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,20))
_Fgs2924rTrapVariable_ObjectIdentity=ObjectIdentity
fgs2924rTrapVariable=_Fgs2924rTrapVariable_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,21))
_Username_Type=DisplayString
_Username_Object=MibScalar
username=_Username_Object((1,3,6,1,4,1,5205,2,34,1,21,1),_Username_Type())
username.setMaxAccess(_D)
if mibBuilder.loadTexts:username.setStatus(_A)
class _GroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_GroupId_Type.__name__=_C
_GroupId_Object=MibScalar
groupId=_GroupId_Object((1,3,6,1,4,1,5205,2,34,1,21,2),_GroupId_Type())
groupId.setMaxAccess(_D)
if mibBuilder.loadTexts:groupId.setStatus(_A)
class _Actorkey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Actorkey_Type.__name__=_C
_Actorkey_Object=MibScalar
actorkey=_Actorkey_Object((1,3,6,1,4,1,5205,2,34,1,21,3),_Actorkey_Type())
actorkey.setMaxAccess(_D)
if mibBuilder.loadTexts:actorkey.setStatus(_A)
class _Partnerkey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Partnerkey_Type.__name__=_C
_Partnerkey_Object=MibScalar
partnerkey=_Partnerkey_Object((1,3,6,1,4,1,5205,2,34,1,21,4),_Partnerkey_Type())
partnerkey.setMaxAccess(_D)
if mibBuilder.loadTexts:partnerkey.setStatus(_A)
_Swapto_Type=DisplayString
_Swapto_Object=MibScalar
swapto=_Swapto_Object((1,3,6,1,4,1,5205,2,34,1,21,6),_Swapto_Type())
swapto.setMaxAccess(_D)
if mibBuilder.loadTexts:swapto.setStatus(_A)
_IpmacIp_Type=DisplayString
_IpmacIp_Object=MibScalar
ipmacIp=_IpmacIp_Object((1,3,6,1,4,1,5205,2,34,1,21,7),_IpmacIp_Type())
ipmacIp.setMaxAccess(_D)
if mibBuilder.loadTexts:ipmacIp.setStatus(_A)
_IpmacMac_Type=DisplayString
_IpmacMac_Object=MibScalar
ipmacMac=_IpmacMac_Object((1,3,6,1,4,1,5205,2,34,1,21,8),_IpmacMac_Type())
ipmacMac.setMaxAccess(_D)
if mibBuilder.loadTexts:ipmacMac.setStatus(_A)
_Fgs2924rDot1X_ObjectIdentity=ObjectIdentity
fgs2924rDot1X=_Fgs2924rDot1X_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,23))
_Fgs2924rDot1XServerConf_ObjectIdentity=ObjectIdentity
fgs2924rDot1XServerConf=_Fgs2924rDot1XServerConf_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,23,1))
_Fgs2924rDot1XServerConfAuthenticationServerIp_Type=IpAddress
_Fgs2924rDot1XServerConfAuthenticationServerIp_Object=MibScalar
fgs2924rDot1XServerConfAuthenticationServerIp=_Fgs2924rDot1XServerConfAuthenticationServerIp_Object((1,3,6,1,4,1,5205,2,34,1,23,1,1),_Fgs2924rDot1XServerConfAuthenticationServerIp_Type())
fgs2924rDot1XServerConfAuthenticationServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XServerConfAuthenticationServerIp.setStatus(_A)
class _Fgs2924rDot1XServerConfAuthenticationUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Fgs2924rDot1XServerConfAuthenticationUdpPort_Type.__name__=_C
_Fgs2924rDot1XServerConfAuthenticationUdpPort_Object=MibScalar
fgs2924rDot1XServerConfAuthenticationUdpPort=_Fgs2924rDot1XServerConfAuthenticationUdpPort_Object((1,3,6,1,4,1,5205,2,34,1,23,1,2),_Fgs2924rDot1XServerConfAuthenticationUdpPort_Type())
fgs2924rDot1XServerConfAuthenticationUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XServerConfAuthenticationUdpPort.setStatus(_A)
_Fgs2924rDot1XServerConfAuthenticationServerIp2_Type=IpAddress
_Fgs2924rDot1XServerConfAuthenticationServerIp2_Object=MibScalar
fgs2924rDot1XServerConfAuthenticationServerIp2=_Fgs2924rDot1XServerConfAuthenticationServerIp2_Object((1,3,6,1,4,1,5205,2,34,1,23,1,3),_Fgs2924rDot1XServerConfAuthenticationServerIp2_Type())
fgs2924rDot1XServerConfAuthenticationServerIp2.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XServerConfAuthenticationServerIp2.setStatus(_A)
class _Fgs2924rDot1XServerConfAuthenticationUdpPort2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Fgs2924rDot1XServerConfAuthenticationUdpPort2_Type.__name__=_C
_Fgs2924rDot1XServerConfAuthenticationUdpPort2_Object=MibScalar
fgs2924rDot1XServerConfAuthenticationUdpPort2=_Fgs2924rDot1XServerConfAuthenticationUdpPort2_Object((1,3,6,1,4,1,5205,2,34,1,23,1,4),_Fgs2924rDot1XServerConfAuthenticationUdpPort2_Type())
fgs2924rDot1XServerConfAuthenticationUdpPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XServerConfAuthenticationUdpPort2.setStatus(_A)
_Fgs2924rDot1XServerConfAuthenticationSecretKey_Type=DisplayString
_Fgs2924rDot1XServerConfAuthenticationSecretKey_Object=MibScalar
fgs2924rDot1XServerConfAuthenticationSecretKey=_Fgs2924rDot1XServerConfAuthenticationSecretKey_Object((1,3,6,1,4,1,5205,2,34,1,23,1,5),_Fgs2924rDot1XServerConfAuthenticationSecretKey_Type())
fgs2924rDot1XServerConfAuthenticationSecretKey.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XServerConfAuthenticationSecretKey.setStatus(_A)
_Fgs2924rDot1XServerConfAccountingServerIp_Type=IpAddress
_Fgs2924rDot1XServerConfAccountingServerIp_Object=MibScalar
fgs2924rDot1XServerConfAccountingServerIp=_Fgs2924rDot1XServerConfAccountingServerIp_Object((1,3,6,1,4,1,5205,2,34,1,23,1,6),_Fgs2924rDot1XServerConfAccountingServerIp_Type())
fgs2924rDot1XServerConfAccountingServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XServerConfAccountingServerIp.setStatus(_A)
class _Fgs2924rDot1XServerConfAccountingUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Fgs2924rDot1XServerConfAccountingUdpPort_Type.__name__=_C
_Fgs2924rDot1XServerConfAccountingUdpPort_Object=MibScalar
fgs2924rDot1XServerConfAccountingUdpPort=_Fgs2924rDot1XServerConfAccountingUdpPort_Object((1,3,6,1,4,1,5205,2,34,1,23,1,7),_Fgs2924rDot1XServerConfAccountingUdpPort_Type())
fgs2924rDot1XServerConfAccountingUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XServerConfAccountingUdpPort.setStatus(_A)
_Fgs2924rDot1XServerConfAccountingServerIp2_Type=IpAddress
_Fgs2924rDot1XServerConfAccountingServerIp2_Object=MibScalar
fgs2924rDot1XServerConfAccountingServerIp2=_Fgs2924rDot1XServerConfAccountingServerIp2_Object((1,3,6,1,4,1,5205,2,34,1,23,1,8),_Fgs2924rDot1XServerConfAccountingServerIp2_Type())
fgs2924rDot1XServerConfAccountingServerIp2.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XServerConfAccountingServerIp2.setStatus(_A)
class _Fgs2924rDot1XServerConfAccountingUdpPort2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Fgs2924rDot1XServerConfAccountingUdpPort2_Type.__name__=_C
_Fgs2924rDot1XServerConfAccountingUdpPort2_Object=MibScalar
fgs2924rDot1XServerConfAccountingUdpPort2=_Fgs2924rDot1XServerConfAccountingUdpPort2_Object((1,3,6,1,4,1,5205,2,34,1,23,1,9),_Fgs2924rDot1XServerConfAccountingUdpPort2_Type())
fgs2924rDot1XServerConfAccountingUdpPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XServerConfAccountingUdpPort2.setStatus(_A)
_Fgs2924rDot1XServerConfAccountingSecretKey_Type=DisplayString
_Fgs2924rDot1XServerConfAccountingSecretKey_Object=MibScalar
fgs2924rDot1XServerConfAccountingSecretKey=_Fgs2924rDot1XServerConfAccountingSecretKey_Object((1,3,6,1,4,1,5205,2,34,1,23,1,10),_Fgs2924rDot1XServerConfAccountingSecretKey_Type())
fgs2924rDot1XServerConfAccountingSecretKey.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XServerConfAccountingSecretKey.setStatus(_A)
_Fgs2924rDot1XPortConfTable_Object=MibTable
fgs2924rDot1XPortConfTable=_Fgs2924rDot1XPortConfTable_Object((1,3,6,1,4,1,5205,2,34,1,23,2))
if mibBuilder.loadTexts:fgs2924rDot1XPortConfTable.setStatus(_A)
_Fgs2924rDot1XPortConfEntry_Object=MibTableRow
fgs2924rDot1XPortConfEntry=_Fgs2924rDot1XPortConfEntry_Object((1,3,6,1,4,1,5205,2,34,1,23,2,1))
fgs2924rDot1XPortConfEntry.setIndexNames((0,_E,_s))
if mibBuilder.loadTexts:fgs2924rDot1XPortConfEntry.setStatus(_A)
class _Fgs2924rDot1XPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rDot1XPort_Type.__name__=_C
_Fgs2924rDot1XPort_Object=MibTableColumn
fgs2924rDot1XPort=_Fgs2924rDot1XPort_Object((1,3,6,1,4,1,5205,2,34,1,23,2,1,1),_Fgs2924rDot1XPort_Type())
fgs2924rDot1XPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XPort.setStatus(_A)
class _Fgs2924rDot1XPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_Fgs2924rDot1XPortMode_Type.__name__=_C
_Fgs2924rDot1XPortMode_Object=MibTableColumn
fgs2924rDot1XPortMode=_Fgs2924rDot1XPortMode_Object((1,3,6,1,4,1,5205,2,34,1,23,2,1,2),_Fgs2924rDot1XPortMode_Type())
fgs2924rDot1XPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XPortMode.setStatus(_A)
class _Fgs2924rDot1XPortControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Fgs2924rDot1XPortControl_Type.__name__=_C
_Fgs2924rDot1XPortControl_Object=MibTableColumn
fgs2924rDot1XPortControl=_Fgs2924rDot1XPortControl_Object((1,3,6,1,4,1,5205,2,34,1,23,2,1,3),_Fgs2924rDot1XPortControl_Type())
fgs2924rDot1XPortControl.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XPortControl.setStatus(_A)
class _Fgs2924rDot1XPortreAuthMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Fgs2924rDot1XPortreAuthMax_Type.__name__=_C
_Fgs2924rDot1XPortreAuthMax_Object=MibTableColumn
fgs2924rDot1XPortreAuthMax=_Fgs2924rDot1XPortreAuthMax_Object((1,3,6,1,4,1,5205,2,34,1,23,2,1,4),_Fgs2924rDot1XPortreAuthMax_Type())
fgs2924rDot1XPortreAuthMax.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XPortreAuthMax.setStatus(_A)
class _Fgs2924rDot1XPorttxPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Fgs2924rDot1XPorttxPeriod_Type.__name__=_C
_Fgs2924rDot1XPorttxPeriod_Object=MibTableColumn
fgs2924rDot1XPorttxPeriod=_Fgs2924rDot1XPorttxPeriod_Object((1,3,6,1,4,1,5205,2,34,1,23,2,1,5),_Fgs2924rDot1XPorttxPeriod_Type())
fgs2924rDot1XPorttxPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XPorttxPeriod.setStatus(_A)
class _Fgs2924rDot1XPortquietPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Fgs2924rDot1XPortquietPeriod_Type.__name__=_C
_Fgs2924rDot1XPortquietPeriod_Object=MibTableColumn
fgs2924rDot1XPortquietPeriod=_Fgs2924rDot1XPortquietPeriod_Object((1,3,6,1,4,1,5205,2,34,1,23,2,1,6),_Fgs2924rDot1XPortquietPeriod_Type())
fgs2924rDot1XPortquietPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XPortquietPeriod.setStatus(_A)
class _Fgs2924rDot1XPortreAuthEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rDot1XPortreAuthEnabled_Type.__name__=_C
_Fgs2924rDot1XPortreAuthEnabled_Object=MibTableColumn
fgs2924rDot1XPortreAuthEnabled=_Fgs2924rDot1XPortreAuthEnabled_Object((1,3,6,1,4,1,5205,2,34,1,23,2,1,7),_Fgs2924rDot1XPortreAuthEnabled_Type())
fgs2924rDot1XPortreAuthEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XPortreAuthEnabled.setStatus(_A)
class _Fgs2924rDot1XPortreAuthPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Fgs2924rDot1XPortreAuthPeriod_Type.__name__=_C
_Fgs2924rDot1XPortreAuthPeriod_Object=MibTableColumn
fgs2924rDot1XPortreAuthPeriod=_Fgs2924rDot1XPortreAuthPeriod_Object((1,3,6,1,4,1,5205,2,34,1,23,2,1,8),_Fgs2924rDot1XPortreAuthPeriod_Type())
fgs2924rDot1XPortreAuthPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XPortreAuthPeriod.setStatus(_A)
class _Fgs2924rDot1XPortmaxReq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Fgs2924rDot1XPortmaxReq_Type.__name__=_C
_Fgs2924rDot1XPortmaxReq_Object=MibTableColumn
fgs2924rDot1XPortmaxReq=_Fgs2924rDot1XPortmaxReq_Object((1,3,6,1,4,1,5205,2,34,1,23,2,1,9),_Fgs2924rDot1XPortmaxReq_Type())
fgs2924rDot1XPortmaxReq.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XPortmaxReq.setStatus(_A)
class _Fgs2924rDot1XPortsuppTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Fgs2924rDot1XPortsuppTimeout_Type.__name__=_C
_Fgs2924rDot1XPortsuppTimeout_Object=MibTableColumn
fgs2924rDot1XPortsuppTimeout=_Fgs2924rDot1XPortsuppTimeout_Object((1,3,6,1,4,1,5205,2,34,1,23,2,1,10),_Fgs2924rDot1XPortsuppTimeout_Type())
fgs2924rDot1XPortsuppTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XPortsuppTimeout.setStatus(_A)
class _Fgs2924rDot1XPortserverTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Fgs2924rDot1XPortserverTimeout_Type.__name__=_C
_Fgs2924rDot1XPortserverTimeout_Object=MibTableColumn
fgs2924rDot1XPortserverTimeout=_Fgs2924rDot1XPortserverTimeout_Object((1,3,6,1,4,1,5205,2,34,1,23,2,1,11),_Fgs2924rDot1XPortserverTimeout_Type())
fgs2924rDot1XPortserverTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XPortserverTimeout.setStatus(_A)
class _Fgs2924rDot1XPortVlanAssignment_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fgs2924rDot1XPortVlanAssignment_Type.__name__=_C
_Fgs2924rDot1XPortVlanAssignment_Object=MibTableColumn
fgs2924rDot1XPortVlanAssignment=_Fgs2924rDot1XPortVlanAssignment_Object((1,3,6,1,4,1,5205,2,34,1,23,2,1,12),_Fgs2924rDot1XPortVlanAssignment_Type())
fgs2924rDot1XPortVlanAssignment.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XPortVlanAssignment.setStatus(_A)
class _Fgs2924rDot1XPortGuestVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_Fgs2924rDot1XPortGuestVlan_Type.__name__=_C
_Fgs2924rDot1XPortGuestVlan_Object=MibTableColumn
fgs2924rDot1XPortGuestVlan=_Fgs2924rDot1XPortGuestVlan_Object((1,3,6,1,4,1,5205,2,34,1,23,2,1,13),_Fgs2924rDot1XPortGuestVlan_Type())
fgs2924rDot1XPortGuestVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XPortGuestVlan.setStatus(_A)
class _Fgs2924rDot1XPortAuthFailedVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_Fgs2924rDot1XPortAuthFailedVlan_Type.__name__=_C
_Fgs2924rDot1XPortAuthFailedVlan_Object=MibTableColumn
fgs2924rDot1XPortAuthFailedVlan=_Fgs2924rDot1XPortAuthFailedVlan_Object((1,3,6,1,4,1,5205,2,34,1,23,2,1,14),_Fgs2924rDot1XPortAuthFailedVlan_Type())
fgs2924rDot1XPortAuthFailedVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XPortAuthFailedVlan.setStatus(_A)
_Fgs2924rDot1XStatusTable_Object=MibTable
fgs2924rDot1XStatusTable=_Fgs2924rDot1XStatusTable_Object((1,3,6,1,4,1,5205,2,34,1,23,3))
if mibBuilder.loadTexts:fgs2924rDot1XStatusTable.setStatus(_A)
_Fgs2924rDot1XStatusEntry_Object=MibTableRow
fgs2924rDot1XStatusEntry=_Fgs2924rDot1XStatusEntry_Object((1,3,6,1,4,1,5205,2,34,1,23,3,1))
fgs2924rDot1XStatusEntry.setIndexNames((0,_E,_t))
if mibBuilder.loadTexts:fgs2924rDot1XStatusEntry.setStatus(_A)
class _Fgs2924rDot1XStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rDot1XStatusIndex_Type.__name__=_C
_Fgs2924rDot1XStatusIndex_Object=MibTableColumn
fgs2924rDot1XStatusIndex=_Fgs2924rDot1XStatusIndex_Object((1,3,6,1,4,1,5205,2,34,1,23,3,1,1),_Fgs2924rDot1XStatusIndex_Type())
fgs2924rDot1XStatusIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rDot1XStatusIndex.setStatus(_A)
_Fgs2924rDot1XStatusMode_Type=DisplayString
_Fgs2924rDot1XStatusMode_Object=MibTableColumn
fgs2924rDot1XStatusMode=_Fgs2924rDot1XStatusMode_Object((1,3,6,1,4,1,5205,2,34,1,23,3,1,2),_Fgs2924rDot1XStatusMode_Type())
fgs2924rDot1XStatusMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XStatusMode.setStatus(_A)
_Fgs2924rDot1XStatusStatus_Type=DisplayString
_Fgs2924rDot1XStatusStatus_Object=MibTableColumn
fgs2924rDot1XStatusStatus=_Fgs2924rDot1XStatusStatus_Object((1,3,6,1,4,1,5205,2,34,1,23,3,1,3),_Fgs2924rDot1XStatusStatus_Type())
fgs2924rDot1XStatusStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XStatusStatus.setStatus(_A)
_Fgs2924rDot1XVlanPolicy_Type=DisplayString
_Fgs2924rDot1XVlanPolicy_Object=MibTableColumn
fgs2924rDot1XVlanPolicy=_Fgs2924rDot1XVlanPolicy_Object((1,3,6,1,4,1,5205,2,34,1,23,3,1,4),_Fgs2924rDot1XVlanPolicy_Type())
fgs2924rDot1XVlanPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XVlanPolicy.setStatus(_A)
_Fgs2924rDot1XStatisticsTable_Object=MibTable
fgs2924rDot1XStatisticsTable=_Fgs2924rDot1XStatisticsTable_Object((1,3,6,1,4,1,5205,2,34,1,23,4))
if mibBuilder.loadTexts:fgs2924rDot1XStatisticsTable.setStatus(_A)
_Fgs2924rDot1XStatisticsEntry_Object=MibTableRow
fgs2924rDot1XStatisticsEntry=_Fgs2924rDot1XStatisticsEntry_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1))
fgs2924rDot1XStatisticsEntry.setIndexNames((0,_E,_u))
if mibBuilder.loadTexts:fgs2924rDot1XStatisticsEntry.setStatus(_A)
class _Fgs2924rDot1XStatisticsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rDot1XStatisticsIndex_Type.__name__=_C
_Fgs2924rDot1XStatisticsIndex_Object=MibTableColumn
fgs2924rDot1XStatisticsIndex=_Fgs2924rDot1XStatisticsIndex_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,1),_Fgs2924rDot1XStatisticsIndex_Type())
fgs2924rDot1XStatisticsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rDot1XStatisticsIndex.setStatus(_A)
class _Fgs2924rDot1XClearCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rDot1XClearCounter_Type.__name__=_C
_Fgs2924rDot1XClearCounter_Object=MibTableColumn
fgs2924rDot1XClearCounter=_Fgs2924rDot1XClearCounter_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,2),_Fgs2924rDot1XClearCounter_Type())
fgs2924rDot1XClearCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDot1XClearCounter.setStatus(_A)
_Fgs2924rDot1XAuthEntersConnecting_Type=Counter32
_Fgs2924rDot1XAuthEntersConnecting_Object=MibTableColumn
fgs2924rDot1XAuthEntersConnecting=_Fgs2924rDot1XAuthEntersConnecting_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,3),_Fgs2924rDot1XAuthEntersConnecting_Type())
fgs2924rDot1XAuthEntersConnecting.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XAuthEntersConnecting.setStatus(_A)
_Fgs2924rDot1XauthEapLogoffsWhileConnecting_Type=Counter32
_Fgs2924rDot1XauthEapLogoffsWhileConnecting_Object=MibTableColumn
fgs2924rDot1XauthEapLogoffsWhileConnecting=_Fgs2924rDot1XauthEapLogoffsWhileConnecting_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,4),_Fgs2924rDot1XauthEapLogoffsWhileConnecting_Type())
fgs2924rDot1XauthEapLogoffsWhileConnecting.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XauthEapLogoffsWhileConnecting.setStatus(_A)
_Fgs2924rDot1XAuthEntersAuthenticating_Type=Counter32
_Fgs2924rDot1XAuthEntersAuthenticating_Object=MibTableColumn
fgs2924rDot1XAuthEntersAuthenticating=_Fgs2924rDot1XAuthEntersAuthenticating_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,5),_Fgs2924rDot1XAuthEntersAuthenticating_Type())
fgs2924rDot1XAuthEntersAuthenticating.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XAuthEntersAuthenticating.setStatus(_A)
_Fgs2924rDot1XAuthAuthSuccessesWhileAuthenticating_Type=Counter32
_Fgs2924rDot1XAuthAuthSuccessesWhileAuthenticating_Object=MibTableColumn
fgs2924rDot1XAuthAuthSuccessesWhileAuthenticating=_Fgs2924rDot1XAuthAuthSuccessesWhileAuthenticating_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,6),_Fgs2924rDot1XAuthAuthSuccessesWhileAuthenticating_Type())
fgs2924rDot1XAuthAuthSuccessesWhileAuthenticating.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XAuthAuthSuccessesWhileAuthenticating.setStatus(_A)
_Fgs2924rDot1XAuthAuthTimeoutsWhileAuthenticating_Type=Counter32
_Fgs2924rDot1XAuthAuthTimeoutsWhileAuthenticating_Object=MibTableColumn
fgs2924rDot1XAuthAuthTimeoutsWhileAuthenticating=_Fgs2924rDot1XAuthAuthTimeoutsWhileAuthenticating_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,7),_Fgs2924rDot1XAuthAuthTimeoutsWhileAuthenticating_Type())
fgs2924rDot1XAuthAuthTimeoutsWhileAuthenticating.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XAuthAuthTimeoutsWhileAuthenticating.setStatus(_A)
_Fgs2924rDot1XAuthAuthFailWhileAuthenticating_Type=Counter32
_Fgs2924rDot1XAuthAuthFailWhileAuthenticating_Object=MibTableColumn
fgs2924rDot1XAuthAuthFailWhileAuthenticating=_Fgs2924rDot1XAuthAuthFailWhileAuthenticating_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,8),_Fgs2924rDot1XAuthAuthFailWhileAuthenticating_Type())
fgs2924rDot1XAuthAuthFailWhileAuthenticating.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XAuthAuthFailWhileAuthenticating.setStatus(_A)
_Fgs2924rDot1XAuthAuthEapStartsWhileAuthenticating_Type=Counter32
_Fgs2924rDot1XAuthAuthEapStartsWhileAuthenticating_Object=MibTableColumn
fgs2924rDot1XAuthAuthEapStartsWhileAuthenticating=_Fgs2924rDot1XAuthAuthEapStartsWhileAuthenticating_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,9),_Fgs2924rDot1XAuthAuthEapStartsWhileAuthenticating_Type())
fgs2924rDot1XAuthAuthEapStartsWhileAuthenticating.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XAuthAuthEapStartsWhileAuthenticating.setStatus(_A)
_Fgs2924rDot1XAuthAuthEapLogoffWhileAuthenticating_Type=Counter32
_Fgs2924rDot1XAuthAuthEapLogoffWhileAuthenticating_Object=MibTableColumn
fgs2924rDot1XAuthAuthEapLogoffWhileAuthenticating=_Fgs2924rDot1XAuthAuthEapLogoffWhileAuthenticating_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,10),_Fgs2924rDot1XAuthAuthEapLogoffWhileAuthenticating_Type())
fgs2924rDot1XAuthAuthEapLogoffWhileAuthenticating.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XAuthAuthEapLogoffWhileAuthenticating.setStatus(_A)
_Fgs2924rDot1XAuthAuthReauthsWhileAuthenticated_Type=Counter32
_Fgs2924rDot1XAuthAuthReauthsWhileAuthenticated_Object=MibTableColumn
fgs2924rDot1XAuthAuthReauthsWhileAuthenticated=_Fgs2924rDot1XAuthAuthReauthsWhileAuthenticated_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,11),_Fgs2924rDot1XAuthAuthReauthsWhileAuthenticated_Type())
fgs2924rDot1XAuthAuthReauthsWhileAuthenticated.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XAuthAuthReauthsWhileAuthenticated.setStatus(_A)
_Fgs2924rDot1XAuthAuthEapStartsWhileAuthenticated_Type=Counter32
_Fgs2924rDot1XAuthAuthEapStartsWhileAuthenticated_Object=MibTableColumn
fgs2924rDot1XAuthAuthEapStartsWhileAuthenticated=_Fgs2924rDot1XAuthAuthEapStartsWhileAuthenticated_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,12),_Fgs2924rDot1XAuthAuthEapStartsWhileAuthenticated_Type())
fgs2924rDot1XAuthAuthEapStartsWhileAuthenticated.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XAuthAuthEapStartsWhileAuthenticated.setStatus(_A)
_Fgs2924rDot1XAuthAuthEapLogoffWhileAuthenticated_Type=Counter32
_Fgs2924rDot1XAuthAuthEapLogoffWhileAuthenticated_Object=MibTableColumn
fgs2924rDot1XAuthAuthEapLogoffWhileAuthenticated=_Fgs2924rDot1XAuthAuthEapLogoffWhileAuthenticated_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,13),_Fgs2924rDot1XAuthAuthEapLogoffWhileAuthenticated_Type())
fgs2924rDot1XAuthAuthEapLogoffWhileAuthenticated.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XAuthAuthEapLogoffWhileAuthenticated.setStatus(_A)
_Fgs2924rDot1XBackendResponses_Type=Counter32
_Fgs2924rDot1XBackendResponses_Object=MibTableColumn
fgs2924rDot1XBackendResponses=_Fgs2924rDot1XBackendResponses_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,14),_Fgs2924rDot1XBackendResponses_Type())
fgs2924rDot1XBackendResponses.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XBackendResponses.setStatus(_A)
_Fgs2924rDot1XBackendAccessChallenges_Type=Counter32
_Fgs2924rDot1XBackendAccessChallenges_Object=MibTableColumn
fgs2924rDot1XBackendAccessChallenges=_Fgs2924rDot1XBackendAccessChallenges_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,15),_Fgs2924rDot1XBackendAccessChallenges_Type())
fgs2924rDot1XBackendAccessChallenges.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XBackendAccessChallenges.setStatus(_A)
_Fgs2924rDot1XBackendOtherRequestsToSupplicant_Type=Counter32
_Fgs2924rDot1XBackendOtherRequestsToSupplicant_Object=MibTableColumn
fgs2924rDot1XBackendOtherRequestsToSupplicant=_Fgs2924rDot1XBackendOtherRequestsToSupplicant_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,16),_Fgs2924rDot1XBackendOtherRequestsToSupplicant_Type())
fgs2924rDot1XBackendOtherRequestsToSupplicant.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XBackendOtherRequestsToSupplicant.setStatus(_A)
_Fgs2924rDot1XBackendAuthSuccesses_Type=Counter32
_Fgs2924rDot1XBackendAuthSuccesses_Object=MibTableColumn
fgs2924rDot1XBackendAuthSuccesses=_Fgs2924rDot1XBackendAuthSuccesses_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,17),_Fgs2924rDot1XBackendAuthSuccesses_Type())
fgs2924rDot1XBackendAuthSuccesses.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XBackendAuthSuccesses.setStatus(_A)
_Fgs2924rDot1XBackendAuthFails_Type=Counter32
_Fgs2924rDot1XBackendAuthFails_Object=MibTableColumn
fgs2924rDot1XBackendAuthFails=_Fgs2924rDot1XBackendAuthFails_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,18),_Fgs2924rDot1XBackendAuthFails_Type())
fgs2924rDot1XBackendAuthFails.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XBackendAuthFails.setStatus(_A)
_Fgs2924rDot1XAuthEapolFramesRx_Type=Counter32
_Fgs2924rDot1XAuthEapolFramesRx_Object=MibTableColumn
fgs2924rDot1XAuthEapolFramesRx=_Fgs2924rDot1XAuthEapolFramesRx_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,19),_Fgs2924rDot1XAuthEapolFramesRx_Type())
fgs2924rDot1XAuthEapolFramesRx.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XAuthEapolFramesRx.setStatus(_A)
_Fgs2924rDot1XAuthEapolFramesTx_Type=Counter32
_Fgs2924rDot1XAuthEapolFramesTx_Object=MibTableColumn
fgs2924rDot1XAuthEapolFramesTx=_Fgs2924rDot1XAuthEapolFramesTx_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,20),_Fgs2924rDot1XAuthEapolFramesTx_Type())
fgs2924rDot1XAuthEapolFramesTx.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XAuthEapolFramesTx.setStatus(_A)
_Fgs2924rDot1XAuthEapolStartFramesRx_Type=Counter32
_Fgs2924rDot1XAuthEapolStartFramesRx_Object=MibTableColumn
fgs2924rDot1XAuthEapolStartFramesRx=_Fgs2924rDot1XAuthEapolStartFramesRx_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,21),_Fgs2924rDot1XAuthEapolStartFramesRx_Type())
fgs2924rDot1XAuthEapolStartFramesRx.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XAuthEapolStartFramesRx.setStatus(_A)
_Fgs2924rDot1XAuthEapolLogoffFramesRx_Type=Counter32
_Fgs2924rDot1XAuthEapolLogoffFramesRx_Object=MibTableColumn
fgs2924rDot1XAuthEapolLogoffFramesRx=_Fgs2924rDot1XAuthEapolLogoffFramesRx_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,22),_Fgs2924rDot1XAuthEapolLogoffFramesRx_Type())
fgs2924rDot1XAuthEapolLogoffFramesRx.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XAuthEapolLogoffFramesRx.setStatus(_A)
_Fgs2924rDot1XAuthEapolRespIdFramesRx_Type=Counter32
_Fgs2924rDot1XAuthEapolRespIdFramesRx_Object=MibTableColumn
fgs2924rDot1XAuthEapolRespIdFramesRx=_Fgs2924rDot1XAuthEapolRespIdFramesRx_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,23),_Fgs2924rDot1XAuthEapolRespIdFramesRx_Type())
fgs2924rDot1XAuthEapolRespIdFramesRx.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XAuthEapolRespIdFramesRx.setStatus(_A)
_Fgs2924rDot1XAuthEapolRespFramesRx_Type=Counter32
_Fgs2924rDot1XAuthEapolRespFramesRx_Object=MibTableColumn
fgs2924rDot1XAuthEapolRespFramesRx=_Fgs2924rDot1XAuthEapolRespFramesRx_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,24),_Fgs2924rDot1XAuthEapolRespFramesRx_Type())
fgs2924rDot1XAuthEapolRespFramesRx.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XAuthEapolRespFramesRx.setStatus(_A)
_Fgs2924rDot1XAuthEapolReqIdFramesTx_Type=Counter32
_Fgs2924rDot1XAuthEapolReqIdFramesTx_Object=MibTableColumn
fgs2924rDot1XAuthEapolReqIdFramesTx=_Fgs2924rDot1XAuthEapolReqIdFramesTx_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,25),_Fgs2924rDot1XAuthEapolReqIdFramesTx_Type())
fgs2924rDot1XAuthEapolReqIdFramesTx.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XAuthEapolReqIdFramesTx.setStatus(_A)
_Fgs2924rDot1XAuthEapolReqFramesTx_Type=Counter32
_Fgs2924rDot1XAuthEapolReqFramesTx_Object=MibTableColumn
fgs2924rDot1XAuthEapolReqFramesTx=_Fgs2924rDot1XAuthEapolReqFramesTx_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,26),_Fgs2924rDot1XAuthEapolReqFramesTx_Type())
fgs2924rDot1XAuthEapolReqFramesTx.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XAuthEapolReqFramesTx.setStatus(_A)
_Fgs2924rDot1XAuthInvalidEapolFramesRx_Type=Counter32
_Fgs2924rDot1XAuthInvalidEapolFramesRx_Object=MibTableColumn
fgs2924rDot1XAuthInvalidEapolFramesRx=_Fgs2924rDot1XAuthInvalidEapolFramesRx_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,27),_Fgs2924rDot1XAuthInvalidEapolFramesRx_Type())
fgs2924rDot1XAuthInvalidEapolFramesRx.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XAuthInvalidEapolFramesRx.setStatus(_A)
_Fgs2924rDot1XAuthEapLengthErrorFramesRx_Type=Counter32
_Fgs2924rDot1XAuthEapLengthErrorFramesRx_Object=MibTableColumn
fgs2924rDot1XAuthEapLengthErrorFramesRx=_Fgs2924rDot1XAuthEapLengthErrorFramesRx_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,28),_Fgs2924rDot1XAuthEapLengthErrorFramesRx_Type())
fgs2924rDot1XAuthEapLengthErrorFramesRx.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XAuthEapLengthErrorFramesRx.setStatus(_A)
_Fgs2924rDot1XAuthLastEapolFrameVersion_Type=Counter32
_Fgs2924rDot1XAuthLastEapolFrameVersion_Object=MibTableColumn
fgs2924rDot1XAuthLastEapolFrameVersion=_Fgs2924rDot1XAuthLastEapolFrameVersion_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,29),_Fgs2924rDot1XAuthLastEapolFrameVersion_Type())
fgs2924rDot1XAuthLastEapolFrameVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XAuthLastEapolFrameVersion.setStatus(_A)
_Fgs2924rDot1XAuthLastEapolFrameSource_Type=DisplayString
_Fgs2924rDot1XAuthLastEapolFrameSource_Object=MibTableColumn
fgs2924rDot1XAuthLastEapolFrameSource=_Fgs2924rDot1XAuthLastEapolFrameSource_Object((1,3,6,1,4,1,5205,2,34,1,23,4,1,30),_Fgs2924rDot1XAuthLastEapolFrameSource_Type())
fgs2924rDot1XAuthLastEapolFrameSource.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDot1XAuthLastEapolFrameSource.setStatus(_A)
_Fgs2924rTrunkInfo_ObjectIdentity=ObjectIdentity
fgs2924rTrunkInfo=_Fgs2924rTrunkInfo_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,24))
_Fgs2924rTrunkPort_ObjectIdentity=ObjectIdentity
fgs2924rTrunkPort=_Fgs2924rTrunkPort_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,24,1))
_Fgs2924rTrunkPortTable_Object=MibTable
fgs2924rTrunkPortTable=_Fgs2924rTrunkPortTable_Object((1,3,6,1,4,1,5205,2,34,1,24,1,1))
if mibBuilder.loadTexts:fgs2924rTrunkPortTable.setStatus(_A)
_Fgs2924rTrunkPortEntry_Object=MibTableRow
fgs2924rTrunkPortEntry=_Fgs2924rTrunkPortEntry_Object((1,3,6,1,4,1,5205,2,34,1,24,1,1,1))
fgs2924rTrunkPortEntry.setIndexNames((0,_E,_v))
if mibBuilder.loadTexts:fgs2924rTrunkPortEntry.setStatus(_A)
class _Fgs2924rTrunkPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rTrunkPortIndex_Type.__name__=_C
_Fgs2924rTrunkPortIndex_Object=MibTableColumn
fgs2924rTrunkPortIndex=_Fgs2924rTrunkPortIndex_Object((1,3,6,1,4,1,5205,2,34,1,24,1,1,1,1),_Fgs2924rTrunkPortIndex_Type())
fgs2924rTrunkPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rTrunkPortIndex.setStatus(_A)
class _Fgs2924rTrunkPortMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Fgs2924rTrunkPortMethod_Type.__name__=_C
_Fgs2924rTrunkPortMethod_Object=MibTableColumn
fgs2924rTrunkPortMethod=_Fgs2924rTrunkPortMethod_Object((1,3,6,1,4,1,5205,2,34,1,24,1,1,1,2),_Fgs2924rTrunkPortMethod_Type())
fgs2924rTrunkPortMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rTrunkPortMethod.setStatus(_A)
class _Fgs2924rTrunkPortGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_Fgs2924rTrunkPortGroup_Type.__name__=_C
_Fgs2924rTrunkPortGroup_Object=MibTableColumn
fgs2924rTrunkPortGroup=_Fgs2924rTrunkPortGroup_Object((1,3,6,1,4,1,5205,2,34,1,24,1,1,1,3),_Fgs2924rTrunkPortGroup_Type())
fgs2924rTrunkPortGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rTrunkPortGroup.setStatus(_A)
class _Fgs2924rTrunkPortActiveLacp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rTrunkPortActiveLacp_Type.__name__=_C
_Fgs2924rTrunkPortActiveLacp_Object=MibTableColumn
fgs2924rTrunkPortActiveLacp=_Fgs2924rTrunkPortActiveLacp_Object((1,3,6,1,4,1,5205,2,34,1,24,1,1,1,4),_Fgs2924rTrunkPortActiveLacp_Type())
fgs2924rTrunkPortActiveLacp.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rTrunkPortActiveLacp.setStatus(_A)
class _Fgs2924rTrunkPortAggtr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rTrunkPortAggtr_Type.__name__=_C
_Fgs2924rTrunkPortAggtr_Object=MibTableColumn
fgs2924rTrunkPortAggtr=_Fgs2924rTrunkPortAggtr_Object((1,3,6,1,4,1,5205,2,34,1,24,1,1,1,5),_Fgs2924rTrunkPortAggtr_Type())
fgs2924rTrunkPortAggtr.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rTrunkPortAggtr.setStatus(_A)
class _Fgs2924rTrunkPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rTrunkPortStatus_Type.__name__=_C
_Fgs2924rTrunkPortStatus_Object=MibTableColumn
fgs2924rTrunkPortStatus=_Fgs2924rTrunkPortStatus_Object((1,3,6,1,4,1,5205,2,34,1,24,1,1,1,6),_Fgs2924rTrunkPortStatus_Type())
fgs2924rTrunkPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rTrunkPortStatus.setStatus(_A)
class _Fgs2924rTrunkPortCurrentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Fgs2924rTrunkPortCurrentMode_Type.__name__=_C
_Fgs2924rTrunkPortCurrentMode_Object=MibTableColumn
fgs2924rTrunkPortCurrentMode=_Fgs2924rTrunkPortCurrentMode_Object((1,3,6,1,4,1,5205,2,34,1,24,1,1,1,7),_Fgs2924rTrunkPortCurrentMode_Type())
fgs2924rTrunkPortCurrentMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rTrunkPortCurrentMode.setStatus(_A)
_Fgs2924rAggregatorView_ObjectIdentity=ObjectIdentity
fgs2924rAggregatorView=_Fgs2924rAggregatorView_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,24,2))
_Fgs2924rAggregatorViewTable_Object=MibTable
fgs2924rAggregatorViewTable=_Fgs2924rAggregatorViewTable_Object((1,3,6,1,4,1,5205,2,34,1,24,2,1))
if mibBuilder.loadTexts:fgs2924rAggregatorViewTable.setStatus(_A)
_Fgs2924rAggregatorViewEntry_Object=MibTableRow
fgs2924rAggregatorViewEntry=_Fgs2924rAggregatorViewEntry_Object((1,3,6,1,4,1,5205,2,34,1,24,2,1,1))
fgs2924rAggregatorViewEntry.setIndexNames((0,_E,_w))
if mibBuilder.loadTexts:fgs2924rAggregatorViewEntry.setStatus(_A)
class _Fgs2924rAggregatorViewIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rAggregatorViewIndex_Type.__name__=_C
_Fgs2924rAggregatorViewIndex_Object=MibTableColumn
fgs2924rAggregatorViewIndex=_Fgs2924rAggregatorViewIndex_Object((1,3,6,1,4,1,5205,2,34,1,24,2,1,1,1),_Fgs2924rAggregatorViewIndex_Type())
fgs2924rAggregatorViewIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rAggregatorViewIndex.setStatus(_A)
class _Fgs2924rAggregatorViewMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Fgs2924rAggregatorViewMethod_Type.__name__=_C
_Fgs2924rAggregatorViewMethod_Object=MibTableColumn
fgs2924rAggregatorViewMethod=_Fgs2924rAggregatorViewMethod_Object((1,3,6,1,4,1,5205,2,34,1,24,2,1,1,2),_Fgs2924rAggregatorViewMethod_Type())
fgs2924rAggregatorViewMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rAggregatorViewMethod.setStatus(_A)
_Fgs2924rAggregatorViewMemberPorts_Type=DisplayString
_Fgs2924rAggregatorViewMemberPorts_Object=MibTableColumn
fgs2924rAggregatorViewMemberPorts=_Fgs2924rAggregatorViewMemberPorts_Object((1,3,6,1,4,1,5205,2,34,1,24,2,1,1,3),_Fgs2924rAggregatorViewMemberPorts_Type())
fgs2924rAggregatorViewMemberPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rAggregatorViewMemberPorts.setStatus(_A)
_Fgs2924rAggregatorViewReadyPorts_Type=DisplayString
_Fgs2924rAggregatorViewReadyPorts_Object=MibTableColumn
fgs2924rAggregatorViewReadyPorts=_Fgs2924rAggregatorViewReadyPorts_Object((1,3,6,1,4,1,5205,2,34,1,24,2,1,1,4),_Fgs2924rAggregatorViewReadyPorts_Type())
fgs2924rAggregatorViewReadyPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rAggregatorViewReadyPorts.setStatus(_A)
class _Fgs2924rLacpSystemPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Fgs2924rLacpSystemPriority_Type.__name__=_C
_Fgs2924rLacpSystemPriority_Object=MibScalar
fgs2924rLacpSystemPriority=_Fgs2924rLacpSystemPriority_Object((1,3,6,1,4,1,5205,2,34,1,24,3),_Fgs2924rLacpSystemPriority_Type())
fgs2924rLacpSystemPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rLacpSystemPriority.setStatus(_A)
_Fgs2924rAggregationHashMode_ObjectIdentity=ObjectIdentity
fgs2924rAggregationHashMode=_Fgs2924rAggregationHashMode_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,24,4))
class _Fgs2924rHashCodeSourceMacAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rHashCodeSourceMacAddress_Type.__name__=_C
_Fgs2924rHashCodeSourceMacAddress_Object=MibScalar
fgs2924rHashCodeSourceMacAddress=_Fgs2924rHashCodeSourceMacAddress_Object((1,3,6,1,4,1,5205,2,34,1,24,4,1),_Fgs2924rHashCodeSourceMacAddress_Type())
fgs2924rHashCodeSourceMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rHashCodeSourceMacAddress.setStatus(_A)
class _Fgs2924rHashCodeDestinationMacAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rHashCodeDestinationMacAddress_Type.__name__=_C
_Fgs2924rHashCodeDestinationMacAddress_Object=MibScalar
fgs2924rHashCodeDestinationMacAddress=_Fgs2924rHashCodeDestinationMacAddress_Object((1,3,6,1,4,1,5205,2,34,1,24,4,2),_Fgs2924rHashCodeDestinationMacAddress_Type())
fgs2924rHashCodeDestinationMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rHashCodeDestinationMacAddress.setStatus(_A)
class _Fgs2924rHashCodeIpAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rHashCodeIpAddress_Type.__name__=_C
_Fgs2924rHashCodeIpAddress_Object=MibScalar
fgs2924rHashCodeIpAddress=_Fgs2924rHashCodeIpAddress_Object((1,3,6,1,4,1,5205,2,34,1,24,4,3),_Fgs2924rHashCodeIpAddress_Type())
fgs2924rHashCodeIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rHashCodeIpAddress.setStatus(_A)
class _Fgs2924rHashCodeTcpUdpPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rHashCodeTcpUdpPortNumber_Type.__name__=_C
_Fgs2924rHashCodeTcpUdpPortNumber_Object=MibScalar
fgs2924rHashCodeTcpUdpPortNumber=_Fgs2924rHashCodeTcpUdpPortNumber_Object((1,3,6,1,4,1,5205,2,34,1,24,4,4),_Fgs2924rHashCodeTcpUdpPortNumber_Type())
fgs2924rHashCodeTcpUdpPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rHashCodeTcpUdpPortNumber.setStatus(_A)
_Fgs2924rMulticastInfo_ObjectIdentity=ObjectIdentity
fgs2924rMulticastInfo=_Fgs2924rMulticastInfo_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,25))
class _Fgs2924rIGMPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_Fgs2924rIGMPMode_Type.__name__=_C
_Fgs2924rIGMPMode_Object=MibScalar
fgs2924rIGMPMode=_Fgs2924rIGMPMode_Object((1,3,6,1,4,1,5205,2,34,1,25,1),_Fgs2924rIGMPMode_Type())
fgs2924rIGMPMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIGMPMode.setStatus(_A)
_Fgs2924rIGMPGroupAllowConf_ObjectIdentity=ObjectIdentity
fgs2924rIGMPGroupAllowConf=_Fgs2924rIGMPGroupAllowConf_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,25,2))
class _Fgs2924rIGMPGroupAllowNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Fgs2924rIGMPGroupAllowNumber_Type.__name__=_C
_Fgs2924rIGMPGroupAllowNumber_Object=MibScalar
fgs2924rIGMPGroupAllowNumber=_Fgs2924rIGMPGroupAllowNumber_Object((1,3,6,1,4,1,5205,2,34,1,25,2,1),_Fgs2924rIGMPGroupAllowNumber_Type())
fgs2924rIGMPGroupAllowNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rIGMPGroupAllowNumber.setStatus(_A)
class _Fgs2924rIGMPGroupAllowEntryCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_Fgs2924rIGMPGroupAllowEntryCreate_Type.__name__=_C
_Fgs2924rIGMPGroupAllowEntryCreate_Object=MibScalar
fgs2924rIGMPGroupAllowEntryCreate=_Fgs2924rIGMPGroupAllowEntryCreate_Object((1,3,6,1,4,1,5205,2,34,1,25,2,2),_Fgs2924rIGMPGroupAllowEntryCreate_Type())
fgs2924rIGMPGroupAllowEntryCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIGMPGroupAllowEntryCreate.setStatus(_A)
_Fgs2924rIGMPGroupAllowTable_Object=MibTable
fgs2924rIGMPGroupAllowTable=_Fgs2924rIGMPGroupAllowTable_Object((1,3,6,1,4,1,5205,2,34,1,25,2,3))
if mibBuilder.loadTexts:fgs2924rIGMPGroupAllowTable.setStatus(_A)
_Fgs2924rIGMPGroupAllowEntry_Object=MibTableRow
fgs2924rIGMPGroupAllowEntry=_Fgs2924rIGMPGroupAllowEntry_Object((1,3,6,1,4,1,5205,2,34,1,25,2,3,1))
fgs2924rIGMPGroupAllowEntry.setIndexNames((0,_E,_x))
if mibBuilder.loadTexts:fgs2924rIGMPGroupAllowEntry.setStatus(_A)
class _Fgs2924rIGMPGroupAllowNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Fgs2924rIGMPGroupAllowNo_Type.__name__=_C
_Fgs2924rIGMPGroupAllowNo_Object=MibTableColumn
fgs2924rIGMPGroupAllowNo=_Fgs2924rIGMPGroupAllowNo_Object((1,3,6,1,4,1,5205,2,34,1,25,2,3,1,1),_Fgs2924rIGMPGroupAllowNo_Type())
fgs2924rIGMPGroupAllowNo.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rIGMPGroupAllowNo.setStatus(_A)
class _Fgs2924rIGMPGroupAllowVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_Fgs2924rIGMPGroupAllowVid_Type.__name__=_C
_Fgs2924rIGMPGroupAllowVid_Object=MibTableColumn
fgs2924rIGMPGroupAllowVid=_Fgs2924rIGMPGroupAllowVid_Object((1,3,6,1,4,1,5205,2,34,1,25,2,3,1,2),_Fgs2924rIGMPGroupAllowVid_Type())
fgs2924rIGMPGroupAllowVid.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIGMPGroupAllowVid.setStatus(_A)
_Fgs2924rIGMPGroupAllowStartAddress_Type=DisplayString
_Fgs2924rIGMPGroupAllowStartAddress_Object=MibTableColumn
fgs2924rIGMPGroupAllowStartAddress=_Fgs2924rIGMPGroupAllowStartAddress_Object((1,3,6,1,4,1,5205,2,34,1,25,2,3,1,3),_Fgs2924rIGMPGroupAllowStartAddress_Type())
fgs2924rIGMPGroupAllowStartAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIGMPGroupAllowStartAddress.setStatus(_A)
_Fgs2924rIGMPGroupAllowEndAddress_Type=DisplayString
_Fgs2924rIGMPGroupAllowEndAddress_Object=MibTableColumn
fgs2924rIGMPGroupAllowEndAddress=_Fgs2924rIGMPGroupAllowEndAddress_Object((1,3,6,1,4,1,5205,2,34,1,25,2,3,1,4),_Fgs2924rIGMPGroupAllowEndAddress_Type())
fgs2924rIGMPGroupAllowEndAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIGMPGroupAllowEndAddress.setStatus(_A)
class _Fgs2924rIGMPGroupAllowEntryAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Fgs2924rIGMPGroupAllowEntryAction_Type.__name__=_C
_Fgs2924rIGMPGroupAllowEntryAction_Object=MibTableColumn
fgs2924rIGMPGroupAllowEntryAction=_Fgs2924rIGMPGroupAllowEntryAction_Object((1,3,6,1,4,1,5205,2,34,1,25,2,3,1,5),_Fgs2924rIGMPGroupAllowEntryAction_Type())
fgs2924rIGMPGroupAllowEntryAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIGMPGroupAllowEntryAction.setStatus(_A)
_Fgs2924rIGMPProxy_ObjectIdentity=ObjectIdentity
fgs2924rIGMPProxy=_Fgs2924rIGMPProxy_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,25,3))
class _Fgs2924rIgmpProxyConfGeneralQueryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_Fgs2924rIgmpProxyConfGeneralQueryInterval_Type.__name__=_C
_Fgs2924rIgmpProxyConfGeneralQueryInterval_Object=MibScalar
fgs2924rIgmpProxyConfGeneralQueryInterval=_Fgs2924rIgmpProxyConfGeneralQueryInterval_Object((1,3,6,1,4,1,5205,2,34,1,25,3,1),_Fgs2924rIgmpProxyConfGeneralQueryInterval_Type())
fgs2924rIgmpProxyConfGeneralQueryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIgmpProxyConfGeneralQueryInterval.setStatus(_A)
class _Fgs2924rIgmpProxyConfGeneralQueryRepTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_Fgs2924rIgmpProxyConfGeneralQueryRepTimeout_Type.__name__=_C
_Fgs2924rIgmpProxyConfGeneralQueryRepTimeout_Object=MibScalar
fgs2924rIgmpProxyConfGeneralQueryRepTimeout=_Fgs2924rIgmpProxyConfGeneralQueryRepTimeout_Object((1,3,6,1,4,1,5205,2,34,1,25,3,2),_Fgs2924rIgmpProxyConfGeneralQueryRepTimeout_Type())
fgs2924rIgmpProxyConfGeneralQueryRepTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIgmpProxyConfGeneralQueryRepTimeout.setStatus(_A)
class _Fgs2924rIgmpProxyConfGeneralQueryMaxRepTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_Fgs2924rIgmpProxyConfGeneralQueryMaxRepTime_Type.__name__=_C
_Fgs2924rIgmpProxyConfGeneralQueryMaxRepTime_Object=MibScalar
fgs2924rIgmpProxyConfGeneralQueryMaxRepTime=_Fgs2924rIgmpProxyConfGeneralQueryMaxRepTime_Object((1,3,6,1,4,1,5205,2,34,1,25,3,3),_Fgs2924rIgmpProxyConfGeneralQueryMaxRepTime_Type())
fgs2924rIgmpProxyConfGeneralQueryMaxRepTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIgmpProxyConfGeneralQueryMaxRepTime.setStatus(_A)
class _Fgs2924rIgmpProxyConfLastMemberQueryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Fgs2924rIgmpProxyConfLastMemberQueryCount_Type.__name__=_C
_Fgs2924rIgmpProxyConfLastMemberQueryCount_Object=MibScalar
fgs2924rIgmpProxyConfLastMemberQueryCount=_Fgs2924rIgmpProxyConfLastMemberQueryCount_Object((1,3,6,1,4,1,5205,2,34,1,25,3,4),_Fgs2924rIgmpProxyConfLastMemberQueryCount_Type())
fgs2924rIgmpProxyConfLastMemberQueryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIgmpProxyConfLastMemberQueryCount.setStatus(_A)
class _Fgs2924rIgmpProxyConfLastMemberQueryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_Fgs2924rIgmpProxyConfLastMemberQueryInterval_Type.__name__=_C
_Fgs2924rIgmpProxyConfLastMemberQueryInterval_Object=MibScalar
fgs2924rIgmpProxyConfLastMemberQueryInterval=_Fgs2924rIgmpProxyConfLastMemberQueryInterval_Object((1,3,6,1,4,1,5205,2,34,1,25,3,5),_Fgs2924rIgmpProxyConfLastMemberQueryInterval_Type())
fgs2924rIgmpProxyConfLastMemberQueryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIgmpProxyConfLastMemberQueryInterval.setStatus(_A)
class _Fgs2924rIgmpProxyConfLastMemberQueryMaxRepTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_Fgs2924rIgmpProxyConfLastMemberQueryMaxRepTime_Type.__name__=_C
_Fgs2924rIgmpProxyConfLastMemberQueryMaxRepTime_Object=MibScalar
fgs2924rIgmpProxyConfLastMemberQueryMaxRepTime=_Fgs2924rIgmpProxyConfLastMemberQueryMaxRepTime_Object((1,3,6,1,4,1,5205,2,34,1,25,3,6),_Fgs2924rIgmpProxyConfLastMemberQueryMaxRepTime_Type())
fgs2924rIgmpProxyConfLastMemberQueryMaxRepTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIgmpProxyConfLastMemberQueryMaxRepTime.setStatus(_A)
_Fgs2924rIgmpProxyConfRouterPorts_Type=DisplayString
_Fgs2924rIgmpProxyConfRouterPorts_Object=MibScalar
fgs2924rIgmpProxyConfRouterPorts=_Fgs2924rIgmpProxyConfRouterPorts_Object((1,3,6,1,4,1,5205,2,34,1,25,3,7),_Fgs2924rIgmpProxyConfRouterPorts_Type())
fgs2924rIgmpProxyConfRouterPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIgmpProxyConfRouterPorts.setStatus(_A)
class _Fgs2924rIgmpProxyGroupMembershipNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_Fgs2924rIgmpProxyGroupMembershipNumber_Type.__name__=_C
_Fgs2924rIgmpProxyGroupMembershipNumber_Object=MibScalar
fgs2924rIgmpProxyGroupMembershipNumber=_Fgs2924rIgmpProxyGroupMembershipNumber_Object((1,3,6,1,4,1,5205,2,34,1,25,3,8),_Fgs2924rIgmpProxyGroupMembershipNumber_Type())
fgs2924rIgmpProxyGroupMembershipNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIgmpProxyGroupMembershipNumber.setStatus(_A)
_Fgs2924rIgmpProxyGroupMembershipTable_Object=MibTable
fgs2924rIgmpProxyGroupMembershipTable=_Fgs2924rIgmpProxyGroupMembershipTable_Object((1,3,6,1,4,1,5205,2,34,1,25,3,9))
if mibBuilder.loadTexts:fgs2924rIgmpProxyGroupMembershipTable.setStatus(_A)
_Fgs2924rIgmpProxyGroupMembershipEntry_Object=MibTableRow
fgs2924rIgmpProxyGroupMembershipEntry=_Fgs2924rIgmpProxyGroupMembershipEntry_Object((1,3,6,1,4,1,5205,2,34,1,25,3,9,1))
fgs2924rIgmpProxyGroupMembershipEntry.setIndexNames((0,_E,_y))
if mibBuilder.loadTexts:fgs2924rIgmpProxyGroupMembershipEntry.setStatus(_A)
class _Fgs2924rIgmpProxyGroupNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_Fgs2924rIgmpProxyGroupNo_Type.__name__=_C
_Fgs2924rIgmpProxyGroupNo_Object=MibTableColumn
fgs2924rIgmpProxyGroupNo=_Fgs2924rIgmpProxyGroupNo_Object((1,3,6,1,4,1,5205,2,34,1,25,3,9,1,1),_Fgs2924rIgmpProxyGroupNo_Type())
fgs2924rIgmpProxyGroupNo.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rIgmpProxyGroupNo.setStatus(_A)
_Fgs2924rIgmpProxyGroupAddress_Type=DisplayString
_Fgs2924rIgmpProxyGroupAddress_Object=MibTableColumn
fgs2924rIgmpProxyGroupAddress=_Fgs2924rIgmpProxyGroupAddress_Object((1,3,6,1,4,1,5205,2,34,1,25,3,9,1,2),_Fgs2924rIgmpProxyGroupAddress_Type())
fgs2924rIgmpProxyGroupAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rIgmpProxyGroupAddress.setStatus(_A)
class _Fgs2924rIgmpProxyGroupVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Fgs2924rIgmpProxyGroupVLANId_Type.__name__=_C
_Fgs2924rIgmpProxyGroupVLANId_Object=MibTableColumn
fgs2924rIgmpProxyGroupVLANId=_Fgs2924rIgmpProxyGroupVLANId_Object((1,3,6,1,4,1,5205,2,34,1,25,3,9,1,3),_Fgs2924rIgmpProxyGroupVLANId_Type())
fgs2924rIgmpProxyGroupVLANId.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rIgmpProxyGroupVLANId.setStatus(_A)
_Fgs2924rIgmpProxyGroupPortMembers_Type=DisplayString
_Fgs2924rIgmpProxyGroupPortMembers_Object=MibTableColumn
fgs2924rIgmpProxyGroupPortMembers=_Fgs2924rIgmpProxyGroupPortMembers_Object((1,3,6,1,4,1,5205,2,34,1,25,3,9,1,4),_Fgs2924rIgmpProxyGroupPortMembers_Type())
fgs2924rIgmpProxyGroupPortMembers.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rIgmpProxyGroupPortMembers.setStatus(_A)
_Fgs2924rIGMPSnooping_ObjectIdentity=ObjectIdentity
fgs2924rIGMPSnooping=_Fgs2924rIGMPSnooping_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,25,4))
class _Fgs2924rIgmpSnoopingConfHostTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Fgs2924rIgmpSnoopingConfHostTimeout_Type.__name__=_C
_Fgs2924rIgmpSnoopingConfHostTimeout_Object=MibScalar
fgs2924rIgmpSnoopingConfHostTimeout=_Fgs2924rIgmpSnoopingConfHostTimeout_Object((1,3,6,1,4,1,5205,2,34,1,25,4,1),_Fgs2924rIgmpSnoopingConfHostTimeout_Type())
fgs2924rIgmpSnoopingConfHostTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIgmpSnoopingConfHostTimeout.setStatus(_A)
_Fgs2924rIgmpSnoopingConfFastLeave_Type=DisplayString
_Fgs2924rIgmpSnoopingConfFastLeave_Object=MibScalar
fgs2924rIgmpSnoopingConfFastLeave=_Fgs2924rIgmpSnoopingConfFastLeave_Object((1,3,6,1,4,1,5205,2,34,1,25,4,2),_Fgs2924rIgmpSnoopingConfFastLeave_Type())
fgs2924rIgmpSnoopingConfFastLeave.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIgmpSnoopingConfFastLeave.setStatus(_A)
_Fgs2924rIgmpSnoopingConfRouterPorts_Type=DisplayString
_Fgs2924rIgmpSnoopingConfRouterPorts_Object=MibScalar
fgs2924rIgmpSnoopingConfRouterPorts=_Fgs2924rIgmpSnoopingConfRouterPorts_Object((1,3,6,1,4,1,5205,2,34,1,25,4,3),_Fgs2924rIgmpSnoopingConfRouterPorts_Type())
fgs2924rIgmpSnoopingConfRouterPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIgmpSnoopingConfRouterPorts.setStatus(_A)
class _Fgs2924rIgmpSnoopingGroupMembershipNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_Fgs2924rIgmpSnoopingGroupMembershipNumber_Type.__name__=_C
_Fgs2924rIgmpSnoopingGroupMembershipNumber_Object=MibScalar
fgs2924rIgmpSnoopingGroupMembershipNumber=_Fgs2924rIgmpSnoopingGroupMembershipNumber_Object((1,3,6,1,4,1,5205,2,34,1,25,4,4),_Fgs2924rIgmpSnoopingGroupMembershipNumber_Type())
fgs2924rIgmpSnoopingGroupMembershipNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rIgmpSnoopingGroupMembershipNumber.setStatus(_A)
_Fgs2924rIgmpSnoopingGroupMembershipTable_Object=MibTable
fgs2924rIgmpSnoopingGroupMembershipTable=_Fgs2924rIgmpSnoopingGroupMembershipTable_Object((1,3,6,1,4,1,5205,2,34,1,25,4,5))
if mibBuilder.loadTexts:fgs2924rIgmpSnoopingGroupMembershipTable.setStatus(_A)
_Fgs2924rIgmpSnoopingGroupMembershipEntry_Object=MibTableRow
fgs2924rIgmpSnoopingGroupMembershipEntry=_Fgs2924rIgmpSnoopingGroupMembershipEntry_Object((1,3,6,1,4,1,5205,2,34,1,25,4,5,1))
fgs2924rIgmpSnoopingGroupMembershipEntry.setIndexNames((0,_E,_z))
if mibBuilder.loadTexts:fgs2924rIgmpSnoopingGroupMembershipEntry.setStatus(_A)
class _Fgs2924rIgmpSnoopingGroupNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_Fgs2924rIgmpSnoopingGroupNo_Type.__name__=_C
_Fgs2924rIgmpSnoopingGroupNo_Object=MibTableColumn
fgs2924rIgmpSnoopingGroupNo=_Fgs2924rIgmpSnoopingGroupNo_Object((1,3,6,1,4,1,5205,2,34,1,25,4,5,1,1),_Fgs2924rIgmpSnoopingGroupNo_Type())
fgs2924rIgmpSnoopingGroupNo.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rIgmpSnoopingGroupNo.setStatus(_A)
_Fgs2924rIgmpSnoopingGroupAddress_Type=DisplayString
_Fgs2924rIgmpSnoopingGroupAddress_Object=MibTableColumn
fgs2924rIgmpSnoopingGroupAddress=_Fgs2924rIgmpSnoopingGroupAddress_Object((1,3,6,1,4,1,5205,2,34,1,25,4,5,1,2),_Fgs2924rIgmpSnoopingGroupAddress_Type())
fgs2924rIgmpSnoopingGroupAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rIgmpSnoopingGroupAddress.setStatus(_A)
class _Fgs2924rIgmpSnoopingGroupVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Fgs2924rIgmpSnoopingGroupVLANId_Type.__name__=_C
_Fgs2924rIgmpSnoopingGroupVLANId_Object=MibTableColumn
fgs2924rIgmpSnoopingGroupVLANId=_Fgs2924rIgmpSnoopingGroupVLANId_Object((1,3,6,1,4,1,5205,2,34,1,25,4,5,1,3),_Fgs2924rIgmpSnoopingGroupVLANId_Type())
fgs2924rIgmpSnoopingGroupVLANId.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rIgmpSnoopingGroupVLANId.setStatus(_A)
_Fgs2924rIgmpSnoopingGroupPortMembers_Type=DisplayString
_Fgs2924rIgmpSnoopingGroupPortMembers_Object=MibTableColumn
fgs2924rIgmpSnoopingGroupPortMembers=_Fgs2924rIgmpSnoopingGroupPortMembers_Object((1,3,6,1,4,1,5205,2,34,1,25,4,5,1,4),_Fgs2924rIgmpSnoopingGroupPortMembers_Type())
fgs2924rIgmpSnoopingGroupPortMembers.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rIgmpSnoopingGroupPortMembers.setStatus(_A)
_Fgs2924rMVR_ObjectIdentity=ObjectIdentity
fgs2924rMVR=_Fgs2924rMVR_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,25,5))
class _Fgs2924rMVRMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rMVRMode_Type.__name__=_C
_Fgs2924rMVRMode_Object=MibScalar
fgs2924rMVRMode=_Fgs2924rMVRMode_Object((1,3,6,1,4,1,5205,2,34,1,25,5,1),_Fgs2924rMVRMode_Type())
fgs2924rMVRMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMVRMode.setStatus(_A)
class _Fgs2924rMVRConfHostTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Fgs2924rMVRConfHostTimeout_Type.__name__=_C
_Fgs2924rMVRConfHostTimeout_Object=MibScalar
fgs2924rMVRConfHostTimeout=_Fgs2924rMVRConfHostTimeout_Object((1,3,6,1,4,1,5205,2,34,1,25,5,2),_Fgs2924rMVRConfHostTimeout_Type())
fgs2924rMVRConfHostTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMVRConfHostTimeout.setStatus(_A)
_Fgs2924rMVRConfFastLeave_Type=DisplayString
_Fgs2924rMVRConfFastLeave_Object=MibScalar
fgs2924rMVRConfFastLeave=_Fgs2924rMVRConfFastLeave_Object((1,3,6,1,4,1,5205,2,34,1,25,5,3),_Fgs2924rMVRConfFastLeave_Type())
fgs2924rMVRConfFastLeave.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMVRConfFastLeave.setStatus(_A)
_Fgs2924rMVIDConf_ObjectIdentity=ObjectIdentity
fgs2924rMVIDConf=_Fgs2924rMVIDConf_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,25,5,4))
class _Fgs2924rMVIDNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Fgs2924rMVIDNumber_Type.__name__=_C
_Fgs2924rMVIDNumber_Object=MibScalar
fgs2924rMVIDNumber=_Fgs2924rMVIDNumber_Object((1,3,6,1,4,1,5205,2,34,1,25,5,4,1),_Fgs2924rMVIDNumber_Type())
fgs2924rMVIDNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rMVIDNumber.setStatus(_A)
class _Fgs2924rMVIDEntryCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_Fgs2924rMVIDEntryCreate_Type.__name__=_C
_Fgs2924rMVIDEntryCreate_Object=MibScalar
fgs2924rMVIDEntryCreate=_Fgs2924rMVIDEntryCreate_Object((1,3,6,1,4,1,5205,2,34,1,25,5,4,2),_Fgs2924rMVIDEntryCreate_Type())
fgs2924rMVIDEntryCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMVIDEntryCreate.setStatus(_A)
_Fgs2924rMVIDGroupTable_Object=MibTable
fgs2924rMVIDGroupTable=_Fgs2924rMVIDGroupTable_Object((1,3,6,1,4,1,5205,2,34,1,25,5,4,3))
if mibBuilder.loadTexts:fgs2924rMVIDGroupTable.setStatus(_A)
_Fgs2924rMVIDGroupEntry_Object=MibTableRow
fgs2924rMVIDGroupEntry=_Fgs2924rMVIDGroupEntry_Object((1,3,6,1,4,1,5205,2,34,1,25,5,4,3,1))
fgs2924rMVIDGroupEntry.setIndexNames((0,_E,_A0))
if mibBuilder.loadTexts:fgs2924rMVIDGroupEntry.setStatus(_A)
class _Fgs2924rMVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Fgs2924rMVID_Type.__name__=_C
_Fgs2924rMVID_Object=MibTableColumn
fgs2924rMVID=_Fgs2924rMVID_Object((1,3,6,1,4,1,5205,2,34,1,25,5,4,3,1,1),_Fgs2924rMVID_Type())
fgs2924rMVID.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rMVID.setStatus(_A)
_Fgs2924rMVIDMemberPort_Type=DisplayString
_Fgs2924rMVIDMemberPort_Object=MibTableColumn
fgs2924rMVIDMemberPort=_Fgs2924rMVIDMemberPort_Object((1,3,6,1,4,1,5205,2,34,1,25,5,4,3,1,2),_Fgs2924rMVIDMemberPort_Type())
fgs2924rMVIDMemberPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMVIDMemberPort.setStatus(_A)
_Fgs2924rMVIDRouterPorts_Type=DisplayString
_Fgs2924rMVIDRouterPorts_Object=MibTableColumn
fgs2924rMVIDRouterPorts=_Fgs2924rMVIDRouterPorts_Object((1,3,6,1,4,1,5205,2,34,1,25,5,4,3,1,3),_Fgs2924rMVIDRouterPorts_Type())
fgs2924rMVIDRouterPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMVIDRouterPorts.setStatus(_A)
class _Fgs2924rMVIDEntryAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Fgs2924rMVIDEntryAction_Type.__name__=_C
_Fgs2924rMVIDEntryAction_Object=MibTableColumn
fgs2924rMVIDEntryAction=_Fgs2924rMVIDEntryAction_Object((1,3,6,1,4,1,5205,2,34,1,25,5,4,3,1,4),_Fgs2924rMVIDEntryAction_Type())
fgs2924rMVIDEntryAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMVIDEntryAction.setStatus(_A)
_Fgs2924rMVIDGroupAllowConf_ObjectIdentity=ObjectIdentity
fgs2924rMVIDGroupAllowConf=_Fgs2924rMVIDGroupAllowConf_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,25,5,5))
class _Fgs2924rMVIDGroupAllowNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Fgs2924rMVIDGroupAllowNumber_Type.__name__=_C
_Fgs2924rMVIDGroupAllowNumber_Object=MibScalar
fgs2924rMVIDGroupAllowNumber=_Fgs2924rMVIDGroupAllowNumber_Object((1,3,6,1,4,1,5205,2,34,1,25,5,5,1),_Fgs2924rMVIDGroupAllowNumber_Type())
fgs2924rMVIDGroupAllowNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rMVIDGroupAllowNumber.setStatus(_A)
class _Fgs2924rMVIDGroupAllowEntryCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_Fgs2924rMVIDGroupAllowEntryCreate_Type.__name__=_C
_Fgs2924rMVIDGroupAllowEntryCreate_Object=MibScalar
fgs2924rMVIDGroupAllowEntryCreate=_Fgs2924rMVIDGroupAllowEntryCreate_Object((1,3,6,1,4,1,5205,2,34,1,25,5,5,2),_Fgs2924rMVIDGroupAllowEntryCreate_Type())
fgs2924rMVIDGroupAllowEntryCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMVIDGroupAllowEntryCreate.setStatus(_A)
_Fgs2924rMVIDGroupAllowTable_Object=MibTable
fgs2924rMVIDGroupAllowTable=_Fgs2924rMVIDGroupAllowTable_Object((1,3,6,1,4,1,5205,2,34,1,25,5,5,3))
if mibBuilder.loadTexts:fgs2924rMVIDGroupAllowTable.setStatus(_A)
_Fgs2924rMVIDGroupAllowEntry_Object=MibTableRow
fgs2924rMVIDGroupAllowEntry=_Fgs2924rMVIDGroupAllowEntry_Object((1,3,6,1,4,1,5205,2,34,1,25,5,5,3,1))
fgs2924rMVIDGroupAllowEntry.setIndexNames((0,_E,_A1))
if mibBuilder.loadTexts:fgs2924rMVIDGroupAllowEntry.setStatus(_A)
class _Fgs2924rMVIDGroupAllowNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Fgs2924rMVIDGroupAllowNo_Type.__name__=_C
_Fgs2924rMVIDGroupAllowNo_Object=MibTableColumn
fgs2924rMVIDGroupAllowNo=_Fgs2924rMVIDGroupAllowNo_Object((1,3,6,1,4,1,5205,2,34,1,25,5,5,3,1,1),_Fgs2924rMVIDGroupAllowNo_Type())
fgs2924rMVIDGroupAllowNo.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rMVIDGroupAllowNo.setStatus(_A)
class _Fgs2924rMVIDGroupAllowMvid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_Fgs2924rMVIDGroupAllowMvid_Type.__name__=_C
_Fgs2924rMVIDGroupAllowMvid_Object=MibTableColumn
fgs2924rMVIDGroupAllowMvid=_Fgs2924rMVIDGroupAllowMvid_Object((1,3,6,1,4,1,5205,2,34,1,25,5,5,3,1,2),_Fgs2924rMVIDGroupAllowMvid_Type())
fgs2924rMVIDGroupAllowMvid.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMVIDGroupAllowMvid.setStatus(_A)
_Fgs2924rMVIDGroupAllowStartAddress_Type=DisplayString
_Fgs2924rMVIDGroupAllowStartAddress_Object=MibTableColumn
fgs2924rMVIDGroupAllowStartAddress=_Fgs2924rMVIDGroupAllowStartAddress_Object((1,3,6,1,4,1,5205,2,34,1,25,5,5,3,1,3),_Fgs2924rMVIDGroupAllowStartAddress_Type())
fgs2924rMVIDGroupAllowStartAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMVIDGroupAllowStartAddress.setStatus(_A)
_Fgs2924rMVIDGroupAllowEndAddress_Type=DisplayString
_Fgs2924rMVIDGroupAllowEndAddress_Object=MibTableColumn
fgs2924rMVIDGroupAllowEndAddress=_Fgs2924rMVIDGroupAllowEndAddress_Object((1,3,6,1,4,1,5205,2,34,1,25,5,5,3,1,4),_Fgs2924rMVIDGroupAllowEndAddress_Type())
fgs2924rMVIDGroupAllowEndAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMVIDGroupAllowEndAddress.setStatus(_A)
class _Fgs2924rMVIDGroupAllowEntryAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Fgs2924rMVIDGroupAllowEntryAction_Type.__name__=_C
_Fgs2924rMVIDGroupAllowEntryAction_Object=MibTableColumn
fgs2924rMVIDGroupAllowEntryAction=_Fgs2924rMVIDGroupAllowEntryAction_Object((1,3,6,1,4,1,5205,2,34,1,25,5,5,3,1,5),_Fgs2924rMVIDGroupAllowEntryAction_Type())
fgs2924rMVIDGroupAllowEntryAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rMVIDGroupAllowEntryAction.setStatus(_A)
class _Fgs2924rMVRGroupMembershipNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_Fgs2924rMVRGroupMembershipNumber_Type.__name__=_C
_Fgs2924rMVRGroupMembershipNumber_Object=MibScalar
fgs2924rMVRGroupMembershipNumber=_Fgs2924rMVRGroupMembershipNumber_Object((1,3,6,1,4,1,5205,2,34,1,25,5,6),_Fgs2924rMVRGroupMembershipNumber_Type())
fgs2924rMVRGroupMembershipNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rMVRGroupMembershipNumber.setStatus(_A)
_Fgs2924rMVRGroupMembershipTable_Object=MibTable
fgs2924rMVRGroupMembershipTable=_Fgs2924rMVRGroupMembershipTable_Object((1,3,6,1,4,1,5205,2,34,1,25,5,7))
if mibBuilder.loadTexts:fgs2924rMVRGroupMembershipTable.setStatus(_A)
_Fgs2924rMVRGroupMembershipEntry_Object=MibTableRow
fgs2924rMVRGroupMembershipEntry=_Fgs2924rMVRGroupMembershipEntry_Object((1,3,6,1,4,1,5205,2,34,1,25,5,7,1))
fgs2924rMVRGroupMembershipEntry.setIndexNames((0,_E,_A2))
if mibBuilder.loadTexts:fgs2924rMVRGroupMembershipEntry.setStatus(_A)
class _Fgs2924rMVRGroupNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_Fgs2924rMVRGroupNo_Type.__name__=_C
_Fgs2924rMVRGroupNo_Object=MibTableColumn
fgs2924rMVRGroupNo=_Fgs2924rMVRGroupNo_Object((1,3,6,1,4,1,5205,2,34,1,25,5,7,1,1),_Fgs2924rMVRGroupNo_Type())
fgs2924rMVRGroupNo.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rMVRGroupNo.setStatus(_A)
_Fgs2924rMVRGroupAddress_Type=DisplayString
_Fgs2924rMVRGroupAddress_Object=MibTableColumn
fgs2924rMVRGroupAddress=_Fgs2924rMVRGroupAddress_Object((1,3,6,1,4,1,5205,2,34,1,25,5,7,1,2),_Fgs2924rMVRGroupAddress_Type())
fgs2924rMVRGroupAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rMVRGroupAddress.setStatus(_A)
class _Fgs2924rMVRGroupVLANId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Fgs2924rMVRGroupVLANId_Type.__name__=_C
_Fgs2924rMVRGroupVLANId_Object=MibTableColumn
fgs2924rMVRGroupVLANId=_Fgs2924rMVRGroupVLANId_Object((1,3,6,1,4,1,5205,2,34,1,25,5,7,1,3),_Fgs2924rMVRGroupVLANId_Type())
fgs2924rMVRGroupVLANId.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rMVRGroupVLANId.setStatus(_A)
_Fgs2924rMVRGroupPortMembers_Type=DisplayString
_Fgs2924rMVRGroupPortMembers_Object=MibTableColumn
fgs2924rMVRGroupPortMembers=_Fgs2924rMVRGroupPortMembers_Object((1,3,6,1,4,1,5205,2,34,1,25,5,7,1,4),_Fgs2924rMVRGroupPortMembers_Type())
fgs2924rMVRGroupPortMembers.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rMVRGroupPortMembers.setStatus(_A)
_Fgs2924rDhcpSnooping_ObjectIdentity=ObjectIdentity
fgs2924rDhcpSnooping=_Fgs2924rDhcpSnooping_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,26))
class _Fgs2924rDhcpSnoopingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rDhcpSnoopingState_Type.__name__=_C
_Fgs2924rDhcpSnoopingState_Object=MibScalar
fgs2924rDhcpSnoopingState=_Fgs2924rDhcpSnoopingState_Object((1,3,6,1,4,1,5205,2,34,1,26,1),_Fgs2924rDhcpSnoopingState_Type())
fgs2924rDhcpSnoopingState.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingState.setStatus(_A)
_Fgs2924rDhcpSnoopingInfo_ObjectIdentity=ObjectIdentity
fgs2924rDhcpSnoopingInfo=_Fgs2924rDhcpSnoopingInfo_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,26,2))
class _Fgs2924rDhcpSnoopingCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rDhcpSnoopingCreate_Type.__name__=_C
_Fgs2924rDhcpSnoopingCreate_Object=MibScalar
fgs2924rDhcpSnoopingCreate=_Fgs2924rDhcpSnoopingCreate_Object((1,3,6,1,4,1,5205,2,34,1,26,2,1),_Fgs2924rDhcpSnoopingCreate_Type())
fgs2924rDhcpSnoopingCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingCreate.setStatus(_A)
_Fgs2924rDhcpSnoopingTable_Object=MibTable
fgs2924rDhcpSnoopingTable=_Fgs2924rDhcpSnoopingTable_Object((1,3,6,1,4,1,5205,2,34,1,26,2,2))
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingTable.setStatus(_A)
_Fgs2924rDhcpSnoopingEntry_Object=MibTableRow
fgs2924rDhcpSnoopingEntry=_Fgs2924rDhcpSnoopingEntry_Object((1,3,6,1,4,1,5205,2,34,1,26,2,2,1))
fgs2924rDhcpSnoopingEntry.setIndexNames((0,_E,_A3))
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingEntry.setStatus(_A)
class _Fgs2924rDhcpSnoopingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Fgs2924rDhcpSnoopingIndex_Type.__name__=_C
_Fgs2924rDhcpSnoopingIndex_Object=MibTableColumn
fgs2924rDhcpSnoopingIndex=_Fgs2924rDhcpSnoopingIndex_Object((1,3,6,1,4,1,5205,2,34,1,26,2,2,1,1),_Fgs2924rDhcpSnoopingIndex_Type())
fgs2924rDhcpSnoopingIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingIndex.setStatus(_A)
class _Fgs2924rDhcpSnoopingVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Fgs2924rDhcpSnoopingVID_Type.__name__=_C
_Fgs2924rDhcpSnoopingVID_Object=MibTableColumn
fgs2924rDhcpSnoopingVID=_Fgs2924rDhcpSnoopingVID_Object((1,3,6,1,4,1,5205,2,34,1,26,2,2,1,2),_Fgs2924rDhcpSnoopingVID_Type())
fgs2924rDhcpSnoopingVID.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingVID.setStatus(_A)
class _Fgs2924rDhcpSnoopingTrustPort1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_Fgs2924rDhcpSnoopingTrustPort1_Type.__name__=_C
_Fgs2924rDhcpSnoopingTrustPort1_Object=MibTableColumn
fgs2924rDhcpSnoopingTrustPort1=_Fgs2924rDhcpSnoopingTrustPort1_Object((1,3,6,1,4,1,5205,2,34,1,26,2,2,1,3),_Fgs2924rDhcpSnoopingTrustPort1_Type())
fgs2924rDhcpSnoopingTrustPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingTrustPort1.setStatus(_A)
class _Fgs2924rDhcpSnoopingTrustPort2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_Fgs2924rDhcpSnoopingTrustPort2_Type.__name__=_C
_Fgs2924rDhcpSnoopingTrustPort2_Object=MibTableColumn
fgs2924rDhcpSnoopingTrustPort2=_Fgs2924rDhcpSnoopingTrustPort2_Object((1,3,6,1,4,1,5205,2,34,1,26,2,2,1,4),_Fgs2924rDhcpSnoopingTrustPort2_Type())
fgs2924rDhcpSnoopingTrustPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingTrustPort2.setStatus(_A)
_Fgs2924rDhcpSnoopingServerIP_Type=IpAddress
_Fgs2924rDhcpSnoopingServerIP_Object=MibTableColumn
fgs2924rDhcpSnoopingServerIP=_Fgs2924rDhcpSnoopingServerIP_Object((1,3,6,1,4,1,5205,2,34,1,26,2,2,1,5),_Fgs2924rDhcpSnoopingServerIP_Type())
fgs2924rDhcpSnoopingServerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingServerIP.setStatus(_A)
class _Fgs2924rDhcpSnoopingOption82_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rDhcpSnoopingOption82_Type.__name__=_C
_Fgs2924rDhcpSnoopingOption82_Object=MibTableColumn
fgs2924rDhcpSnoopingOption82=_Fgs2924rDhcpSnoopingOption82_Object((1,3,6,1,4,1,5205,2,34,1,26,2,2,1,6),_Fgs2924rDhcpSnoopingOption82_Type())
fgs2924rDhcpSnoopingOption82.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingOption82.setStatus(_A)
class _Fgs2924rDhcpSnoopingAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Fgs2924rDhcpSnoopingAction_Type.__name__=_C
_Fgs2924rDhcpSnoopingAction_Object=MibTableColumn
fgs2924rDhcpSnoopingAction=_Fgs2924rDhcpSnoopingAction_Object((1,3,6,1,4,1,5205,2,34,1,26,2,2,1,7),_Fgs2924rDhcpSnoopingAction_Type())
fgs2924rDhcpSnoopingAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingAction.setStatus(_A)
class _Fgs2924rDhcpSnoopingEntryAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Fgs2924rDhcpSnoopingEntryAction_Type.__name__=_C
_Fgs2924rDhcpSnoopingEntryAction_Object=MibTableColumn
fgs2924rDhcpSnoopingEntryAction=_Fgs2924rDhcpSnoopingEntryAction_Object((1,3,6,1,4,1,5205,2,34,1,26,2,2,1,8),_Fgs2924rDhcpSnoopingEntryAction_Type())
fgs2924rDhcpSnoopingEntryAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingEntryAction.setStatus(_A)
_Fgs2924rDhcpSnoopingDefaultData_ObjectIdentity=ObjectIdentity
fgs2924rDhcpSnoopingDefaultData=_Fgs2924rDhcpSnoopingDefaultData_ObjectIdentity((1,3,6,1,4,1,5205,2,34,1,26,2,3))
class _Fgs2924rDhcpSnoopingDefaultVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Fgs2924rDhcpSnoopingDefaultVID_Type.__name__=_C
_Fgs2924rDhcpSnoopingDefaultVID_Object=MibScalar
fgs2924rDhcpSnoopingDefaultVID=_Fgs2924rDhcpSnoopingDefaultVID_Object((1,3,6,1,4,1,5205,2,34,1,26,2,3,1),_Fgs2924rDhcpSnoopingDefaultVID_Type())
fgs2924rDhcpSnoopingDefaultVID.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingDefaultVID.setStatus(_A)
class _Fgs2924rDhcpSnoopingDefaultTrustPort1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_Fgs2924rDhcpSnoopingDefaultTrustPort1_Type.__name__=_C
_Fgs2924rDhcpSnoopingDefaultTrustPort1_Object=MibScalar
fgs2924rDhcpSnoopingDefaultTrustPort1=_Fgs2924rDhcpSnoopingDefaultTrustPort1_Object((1,3,6,1,4,1,5205,2,34,1,26,2,3,2),_Fgs2924rDhcpSnoopingDefaultTrustPort1_Type())
fgs2924rDhcpSnoopingDefaultTrustPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingDefaultTrustPort1.setStatus(_A)
class _Fgs2924rDhcpSnoopingDefaultTrustPort2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_Fgs2924rDhcpSnoopingDefaultTrustPort2_Type.__name__=_C
_Fgs2924rDhcpSnoopingDefaultTrustPort2_Object=MibScalar
fgs2924rDhcpSnoopingDefaultTrustPort2=_Fgs2924rDhcpSnoopingDefaultTrustPort2_Object((1,3,6,1,4,1,5205,2,34,1,26,2,3,3),_Fgs2924rDhcpSnoopingDefaultTrustPort2_Type())
fgs2924rDhcpSnoopingDefaultTrustPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingDefaultTrustPort2.setStatus(_A)
_Fgs2924rDhcpSnoopingDefaultServerIP_Type=IpAddress
_Fgs2924rDhcpSnoopingDefaultServerIP_Object=MibScalar
fgs2924rDhcpSnoopingDefaultServerIP=_Fgs2924rDhcpSnoopingDefaultServerIP_Object((1,3,6,1,4,1,5205,2,34,1,26,2,3,4),_Fgs2924rDhcpSnoopingDefaultServerIP_Type())
fgs2924rDhcpSnoopingDefaultServerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingDefaultServerIP.setStatus(_A)
class _Fgs2924rDhcpSnoopingDefaultOption82_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Fgs2924rDhcpSnoopingDefaultOption82_Type.__name__=_C
_Fgs2924rDhcpSnoopingDefaultOption82_Object=MibScalar
fgs2924rDhcpSnoopingDefaultOption82=_Fgs2924rDhcpSnoopingDefaultOption82_Object((1,3,6,1,4,1,5205,2,34,1,26,2,3,5),_Fgs2924rDhcpSnoopingDefaultOption82_Type())
fgs2924rDhcpSnoopingDefaultOption82.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingDefaultOption82.setStatus(_A)
class _Fgs2924rDhcpSnoopingDefaultAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Fgs2924rDhcpSnoopingDefaultAction_Type.__name__=_C
_Fgs2924rDhcpSnoopingDefaultAction_Object=MibScalar
fgs2924rDhcpSnoopingDefaultAction=_Fgs2924rDhcpSnoopingDefaultAction_Object((1,3,6,1,4,1,5205,2,34,1,26,2,3,6),_Fgs2924rDhcpSnoopingDefaultAction_Type())
fgs2924rDhcpSnoopingDefaultAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingDefaultAction.setStatus(_A)
class _Fgs2924rDhcpSnoopingDefaultEntryAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Fgs2924rDhcpSnoopingDefaultEntryAction_Type.__name__=_C
_Fgs2924rDhcpSnoopingDefaultEntryAction_Object=MibScalar
fgs2924rDhcpSnoopingDefaultEntryAction=_Fgs2924rDhcpSnoopingDefaultEntryAction_Object((1,3,6,1,4,1,5205,2,34,1,26,2,3,7),_Fgs2924rDhcpSnoopingDefaultEntryAction_Type())
fgs2924rDhcpSnoopingDefaultEntryAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingDefaultEntryAction.setStatus(_A)
_Fgs2924rDhcpSnoopingClientTable_Object=MibTable
fgs2924rDhcpSnoopingClientTable=_Fgs2924rDhcpSnoopingClientTable_Object((1,3,6,1,4,1,5205,2,34,1,26,3))
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingClientTable.setStatus(_A)
_Fgs2924rDhcpSnoopingClientEntry_Object=MibTableRow
fgs2924rDhcpSnoopingClientEntry=_Fgs2924rDhcpSnoopingClientEntry_Object((1,3,6,1,4,1,5205,2,34,1,26,3,1))
fgs2924rDhcpSnoopingClientEntry.setIndexNames((0,_E,_A4))
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingClientEntry.setStatus(_A)
class _Fgs2924rDhcpSnoopingClientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_Fgs2924rDhcpSnoopingClientIndex_Type.__name__=_C
_Fgs2924rDhcpSnoopingClientIndex_Object=MibTableColumn
fgs2924rDhcpSnoopingClientIndex=_Fgs2924rDhcpSnoopingClientIndex_Object((1,3,6,1,4,1,5205,2,34,1,26,3,1,1),_Fgs2924rDhcpSnoopingClientIndex_Type())
fgs2924rDhcpSnoopingClientIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingClientIndex.setStatus(_A)
_Fgs2924rDhcpSnoopingClientMac_Type=DisplayString
_Fgs2924rDhcpSnoopingClientMac_Object=MibTableColumn
fgs2924rDhcpSnoopingClientMac=_Fgs2924rDhcpSnoopingClientMac_Object((1,3,6,1,4,1,5205,2,34,1,26,3,1,2),_Fgs2924rDhcpSnoopingClientMac_Type())
fgs2924rDhcpSnoopingClientMac.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingClientMac.setStatus(_A)
class _Fgs2924rDhcpSnoopingClientVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Fgs2924rDhcpSnoopingClientVID_Type.__name__=_C
_Fgs2924rDhcpSnoopingClientVID_Object=MibTableColumn
fgs2924rDhcpSnoopingClientVID=_Fgs2924rDhcpSnoopingClientVID_Object((1,3,6,1,4,1,5205,2,34,1,26,3,1,3),_Fgs2924rDhcpSnoopingClientVID_Type())
fgs2924rDhcpSnoopingClientVID.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingClientVID.setStatus(_A)
class _Fgs2924rDhcpSnoopingClientPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Fgs2924rDhcpSnoopingClientPort_Type.__name__=_C
_Fgs2924rDhcpSnoopingClientPort_Object=MibTableColumn
fgs2924rDhcpSnoopingClientPort=_Fgs2924rDhcpSnoopingClientPort_Object((1,3,6,1,4,1,5205,2,34,1,26,3,1,4),_Fgs2924rDhcpSnoopingClientPort_Type())
fgs2924rDhcpSnoopingClientPort.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingClientPort.setStatus(_A)
_Fgs2924rDhcpSnoopingClientIP_Type=IpAddress
_Fgs2924rDhcpSnoopingClientIP_Object=MibTableColumn
fgs2924rDhcpSnoopingClientIP=_Fgs2924rDhcpSnoopingClientIP_Object((1,3,6,1,4,1,5205,2,34,1,26,3,1,5),_Fgs2924rDhcpSnoopingClientIP_Type())
fgs2924rDhcpSnoopingClientIP.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingClientIP.setStatus(_A)
_Fgs2924rDhcpSnoopingClientLease_Type=DisplayString
_Fgs2924rDhcpSnoopingClientLease_Object=MibTableColumn
fgs2924rDhcpSnoopingClientLease=_Fgs2924rDhcpSnoopingClientLease_Object((1,3,6,1,4,1,5205,2,34,1,26,3,1,6),_Fgs2924rDhcpSnoopingClientLease_Type())
fgs2924rDhcpSnoopingClientLease.setMaxAccess(_D)
if mibBuilder.loadTexts:fgs2924rDhcpSnoopingClientLease.setStatus(_A)
fgs2924rUserLogin=NotificationType((1,3,6,1,4,1,5205,2,34,1,20,1))
fgs2924rUserLogin.setObjects((_E,_I))
if mibBuilder.loadTexts:fgs2924rUserLogin.setStatus(_A)
fgs2924rUserLogout=NotificationType((1,3,6,1,4,1,5205,2,34,1,20,2))
fgs2924rUserLogout.setObjects((_E,_I))
if mibBuilder.loadTexts:fgs2924rUserLogout.setStatus(_A)
fgs2924rModuleInserted=NotificationType((1,3,6,1,4,1,5205,2,34,1,20,3))
fgs2924rModuleInserted.setObjects((_G,_H))
if mibBuilder.loadTexts:fgs2924rModuleInserted.setStatus(_A)
fgs2924rModuleRemoved=NotificationType((1,3,6,1,4,1,5205,2,34,1,20,4))
fgs2924rModuleRemoved.setObjects((_G,_H))
if mibBuilder.loadTexts:fgs2924rModuleRemoved.setStatus(_A)
fgs2924rDualMediaSwapped=NotificationType((1,3,6,1,4,1,5205,2,34,1,20,5))
fgs2924rDualMediaSwapped.setObjects(*((_G,_H),(_E,'swapto')))
if mibBuilder.loadTexts:fgs2924rDualMediaSwapped.setStatus(_A)
fgs2924rLoopDetected=NotificationType((1,3,6,1,4,1,5205,2,34,1,20,6))
fgs2924rLoopDetected.setObjects((_G,_H))
if mibBuilder.loadTexts:fgs2924rLoopDetected.setStatus(_A)
fgs2924rStpStateDisabled=NotificationType((1,3,6,1,4,1,5205,2,34,1,20,7))
if mibBuilder.loadTexts:fgs2924rStpStateDisabled.setStatus(_A)
fgs2924rStpStateEnabled=NotificationType((1,3,6,1,4,1,5205,2,34,1,20,8))
if mibBuilder.loadTexts:fgs2924rStpStateEnabled.setStatus(_A)
fgs2924rStpTopologyChanged=NotificationType((1,3,6,1,4,1,5205,2,34,1,20,9))
fgs2924rStpTopologyChanged.setObjects((_G,_H))
if mibBuilder.loadTexts:fgs2924rStpTopologyChanged.setStatus(_A)
fgs2924rLacpStateDisabled=NotificationType((1,3,6,1,4,1,5205,2,34,1,20,10))
fgs2924rLacpStateDisabled.setObjects(*((_G,_H),(_E,_J)))
if mibBuilder.loadTexts:fgs2924rLacpStateDisabled.setStatus(_A)
fgs2924rLacpStateEnabled=NotificationType((1,3,6,1,4,1,5205,2,34,1,20,11))
fgs2924rLacpStateEnabled.setObjects(*((_G,_H),(_E,_J)))
if mibBuilder.loadTexts:fgs2924rLacpStateEnabled.setStatus(_A)
fgs2924rLacpPortAdded=NotificationType((1,3,6,1,4,1,5205,2,34,1,20,12))
fgs2924rLacpPortAdded.setObjects(*((_G,_H),(_E,_K),(_E,_L)))
if mibBuilder.loadTexts:fgs2924rLacpPortAdded.setStatus(_A)
fgs2924rLacpPortTrunkFailure=NotificationType((1,3,6,1,4,1,5205,2,34,1,20,13))
fgs2924rLacpPortTrunkFailure.setObjects(*((_G,_H),(_E,_K),(_E,_L)))
if mibBuilder.loadTexts:fgs2924rLacpPortTrunkFailure.setStatus(_A)
fgs2924rGvrpStateDisabled=NotificationType((1,3,6,1,4,1,5205,2,34,1,20,14))
if mibBuilder.loadTexts:fgs2924rGvrpStateDisabled.setStatus(_A)
fgs2924rGvrpStateEnabled=NotificationType((1,3,6,1,4,1,5205,2,34,1,20,15))
if mibBuilder.loadTexts:fgs2924rGvrpStateEnabled.setStatus(_A)
fgs2924rVlanPortBaseEnabled=NotificationType((1,3,6,1,4,1,5205,2,34,1,20,17))
if mibBuilder.loadTexts:fgs2924rVlanPortBaseEnabled.setStatus(_A)
fgs2924rVlanTagBaseEnabled=NotificationType((1,3,6,1,4,1,5205,2,34,1,20,18))
if mibBuilder.loadTexts:fgs2924rVlanTagBaseEnabled.setStatus(_A)
fgs2924rIpmbStateEnabled=NotificationType((1,3,6,1,4,1,5205,2,34,1,20,19))
if mibBuilder.loadTexts:fgs2924rIpmbStateEnabled.setStatus(_A)
fgs2924rIpmbStateDisabled=NotificationType((1,3,6,1,4,1,5205,2,34,1,20,20))
if mibBuilder.loadTexts:fgs2924rIpmbStateDisabled.setStatus(_A)
fgs2924rIpmbEntryFailure=NotificationType((1,3,6,1,4,1,5205,2,34,1,20,21))
fgs2924rIpmbEntryFailure.setObjects(*((_E,'ipmacIp'),(_E,'ipmacMac'),(_G,_H)))
if mibBuilder.loadTexts:fgs2924rIpmbEntryFailure.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'rubytech':rubytech,'switch':switch,'fgs2924rProductID':fgs2924rProductID,'fgs2924rProduces':fgs2924rProduces,'fgs2924rSystem':fgs2924rSystem,'fgs2924rCommonSys':fgs2924rCommonSys,'fgs2924rReboot':fgs2924rReboot,'fgs2924rBiosVsersion':fgs2924rBiosVsersion,'fgs2924rFirmwareVersion':fgs2924rFirmwareVersion,'fgs2924rHardwareVersion':fgs2924rHardwareVersion,'fgs2924rMechanicalVersion':fgs2924rMechanicalVersion,'fgs2924rSerialNumber':fgs2924rSerialNumber,'fgs2924rHostMacAddress':fgs2924rHostMacAddress,'fgs2924rDevicePort':fgs2924rDevicePort,'fgs2924rRamSize':fgs2924rRamSize,'fgs2924rFlashSize':fgs2924rFlashSize,'fgs2924rDeviceName':fgs2924rDeviceName,'fgs2924rSystemDescription':fgs2924rSystemDescription,'fgs2924rCpuLoad':fgs2924rCpuLoad,'fgs2924rIP':fgs2924rIP,'fgs2924rDhcpSetting':fgs2924rDhcpSetting,'fgs2924rIPAddress':fgs2924rIPAddress,'fgs2924rNetMask':fgs2924rNetMask,'fgs2924rDefaultGateway':fgs2924rDefaultGateway,'fgs2924rDnsConf':fgs2924rDnsConf,'fgs2924rDnsState':fgs2924rDnsState,'fgs2924rDnsServer':fgs2924rDnsServer,'fgs2924rTime':fgs2924rTime,'fgs2924rSystemCurrentTime':fgs2924rSystemCurrentTime,'fgs2924rManualTimeSetting':fgs2924rManualTimeSetting,'fgs2924rNTPServer':fgs2924rNTPServer,'fgs2924rNTPTimeZone':fgs2924rNTPTimeZone,'fgs2924rNTPTimeSync':fgs2924rNTPTimeSync,'fgs2924rDaylightSavingTime':fgs2924rDaylightSavingTime,'fgs2924rDaylightStartTime':fgs2924rDaylightStartTime,'fgs2924rDaylightEndTime':fgs2924rDaylightEndTime,'fgs2924rAccount':fgs2924rAccount,'fgs2924rAccountNumber':fgs2924rAccountNumber,'fgs2924rAccountTable':fgs2924rAccountTable,'fgs2924rAccountEntry':fgs2924rAccountEntry,_M:fgs2924rAccountIndex,'fgs2924rAccountAuthorization':fgs2924rAccountAuthorization,'fgs2924rAccountName':fgs2924rAccountName,'fgs2924rAccountPassword':fgs2924rAccountPassword,'fgs2924rAccountAddAuthorization':fgs2924rAccountAddAuthorization,'fgs2924rAccountAddName':fgs2924rAccountAddName,'fgs2924rAccountAddPassword':fgs2924rAccountAddPassword,'fgs2924rDoAccountAdd':fgs2924rDoAccountAdd,'fgs2924rAccountDel':fgs2924rAccountDel,'fgs2924rVsm':fgs2924rVsm,'fgs2924rVsmState':fgs2924rVsmState,'fgs2924rVsmRole':fgs2924rVsmRole,'fgs2924rVsmGroupid':fgs2924rVsmGroupid,'fgs2924rSnmp':fgs2924rSnmp,'fgs2924rGetCommunity':fgs2924rGetCommunity,'fgs2924rSetCommunity':fgs2924rSetCommunity,'fgs2924rTrapHostNumber':fgs2924rTrapHostNumber,'fgs2924rTrapHostTable':fgs2924rTrapHostTable,'fgs2924rTrapHostEntry':fgs2924rTrapHostEntry,_N:fgs2924rTrapHostIndex,'fgs2924rTrapHostIP':fgs2924rTrapHostIP,'fgs2924rTrapHostPort':fgs2924rTrapHostPort,'fgs2924rTrapHostCommunity':fgs2924rTrapHostCommunity,'fgs2924rAlarm':fgs2924rAlarm,'fgs2924rEvent':fgs2924rEvent,'fgs2924rEventNumber':fgs2924rEventNumber,'fgs2924rEventTable':fgs2924rEventTable,'fgs2924rEventEntry':fgs2924rEventEntry,_O:fgs2924rEventIndex,'fgs2924rEventName':fgs2924rEventName,'fgs2924rEventSendEmail':fgs2924rEventSendEmail,'fgs2924rEventSendTrap':fgs2924rEventSendTrap,'fgs2924rEmail':fgs2924rEmail,'fgs2924rEmailServer':fgs2924rEmailServer,'fgs2924rEmailUsername':fgs2924rEmailUsername,'fgs2924rEmailPassword':fgs2924rEmailPassword,'fgs2924rEmailSender':fgs2924rEmailSender,'fgs2924rEmailReturnPath':fgs2924rEmailReturnPath,'fgs2924rEmailUserNumber':fgs2924rEmailUserNumber,'fgs2924rEmailUserTable':fgs2924rEmailUserTable,'fgs2924rEmailUserEntry':fgs2924rEmailUserEntry,_P:fgs2924rEmailUserIndex,'fgs2924rEmailUserAddress':fgs2924rEmailUserAddress,'fgs2924rConfiguration':fgs2924rConfiguration,'fgs2924rSaveRestore':fgs2924rSaveRestore,'fgs2924rSaveStart':fgs2924rSaveStart,'fgs2924rSaveUser':fgs2924rSaveUser,'fgs2924rRestoreDefault':fgs2924rRestoreDefault,'fgs2924rRestoreUser':fgs2924rRestoreUser,'fgs2924rConfigFile':fgs2924rConfigFile,'fgs2924rExportIpAddress':fgs2924rExportIpAddress,'fgs2924rDoExportConfig':fgs2924rDoExportConfig,'fgs2924rImportIpAddress':fgs2924rImportIpAddress,'fgs2924rImportConfigName':fgs2924rImportConfigName,'fgs2924rDoImportConfig':fgs2924rDoImportConfig,'fgs2924rLog':fgs2924rLog,'fgs2924rClearLog':fgs2924rClearLog,'fgs2924rLogNumber':fgs2924rLogNumber,'fgs2924rLogTable':fgs2924rLogTable,'fgs2924rLogEntry':fgs2924rLogEntry,_Q:fgs2924rLogIndex,'fgs2924rLogEvent':fgs2924rLogEvent,'fgs2924rFirmware':fgs2924rFirmware,'fgs2924rFirmwareIpAddress':fgs2924rFirmwareIpAddress,'fgs2924rFirmwareFileName':fgs2924rFirmwareFileName,'fgs2924rDoFirmwareUpgrade':fgs2924rDoFirmwareUpgrade,'fgs2924rPort':fgs2924rPort,'fgs2924rPortStatus':fgs2924rPortStatus,'fgs2924rPortStatusNumber':fgs2924rPortStatusNumber,'fgs2924rPortStatusTable':fgs2924rPortStatusTable,'fgs2924rPortStatusEntry':fgs2924rPortStatusEntry,_R:fgs2924rPortStatusIndex,'fgs2924rPortStatusMedia':fgs2924rPortStatusMedia,'fgs2924rPortStatusPortState':fgs2924rPortStatusPortState,'fgs2924rPortStatusLink':fgs2924rPortStatusLink,'fgs2924rPortStatusAutoNego':fgs2924rPortStatusAutoNego,'fgs2924rPortStatusSpdDpx':fgs2924rPortStatusSpdDpx,'fgs2924rPortStatusFlwCtrlRx':fgs2924rPortStatusFlwCtrlRx,'fgs2924rPortStatusFlwCtrlTx':fgs2924rPortStatusFlwCtrlTx,'fgs2924rPortStatuDescription':fgs2924rPortStatuDescription,'fgs2924rPortConf':fgs2924rPortConf,'fgs2924rPortConfNumber':fgs2924rPortConfNumber,'fgs2924rPortConfTable':fgs2924rPortConfTable,'fgs2924rPortConfEntry':fgs2924rPortConfEntry,_S:fgs2924rPortConfIndex,'fgs2924rPortConfPortState':fgs2924rPortConfPortState,'fgs2924rPortConfTPSpdDpx':fgs2924rPortConfTPSpdDpx,'fgs2924rPortConfSFPSpdDpx':fgs2924rPortConfSFPSpdDpx,'fgs2924rPortConfFlwCtrl':fgs2924rPortConfFlwCtrl,'fgs2924rPortConfExcessiveCollisionMode':fgs2924rPortConfExcessiveCollisionMode,'fgs2924rPortConfDescription':fgs2924rPortConfDescription,'fgs2924rPortConfPowerSaving':fgs2924rPortConfPowerSaving,'fgs2924rSFPInfo':fgs2924rSFPInfo,'fgs2924rSFPInfoNumber':fgs2924rSFPInfoNumber,'fgs2924rSFPInfoTable':fgs2924rSFPInfoTable,'fgs2924rSFPInfoEntry':fgs2924rSFPInfoEntry,_T:fgs2924rSFPInfoIndex,'fgs2924rSFPConnectorType':fgs2924rSFPConnectorType,'fgs2924rSFPFiberType':fgs2924rSFPFiberType,'fgs2924rSFPWavelength':fgs2924rSFPWavelength,'fgs2924rSFPBaudRate':fgs2924rSFPBaudRate,'fgs2924rSFPVendorOUI':fgs2924rSFPVendorOUI,'fgs2924rSFPVendorName':fgs2924rSFPVendorName,'fgs2924rSFPVendorPN':fgs2924rSFPVendorPN,'fgs2924rSFPVendorRev':fgs2924rSFPVendorRev,'fgs2924rSFPVendorSN':fgs2924rSFPVendorSN,'fgs2924rSFPDateCode':fgs2924rSFPDateCode,'fgs2924rSFPTemperature':fgs2924rSFPTemperature,'fgs2924rSFPVcc':fgs2924rSFPVcc,'fgs2924rSFPTxBias':fgs2924rSFPTxBias,'fgs2924rSFPTxPWR':fgs2924rSFPTxPWR,'fgs2924rSFPRxPWR':fgs2924rSFPRxPWR,'fgs2924rMirror':fgs2924rMirror,'fgs2924rMirroringPort':fgs2924rMirroringPort,'fgs2924rMirroredPortsTable':fgs2924rMirroredPortsTable,'fgs2924rMirroredPortsEntry':fgs2924rMirroredPortsEntry,_U:fgs2924rMirroredPortIndex,'fgs2924rMirroredPortSrouceEnable':fgs2924rMirroredPortSrouceEnable,'fgs2924rMirroredPortDestinationEnable':fgs2924rMirroredPortDestinationEnable,'fgs2924rMaxPktLen':fgs2924rMaxPktLen,'fgs2924rMaxPktLenPortNumber':fgs2924rMaxPktLenPortNumber,'fgs2924rMaxPktLenConfTable':fgs2924rMaxPktLenConfTable,'fgs2924rMaxPktLenConfEntry':fgs2924rMaxPktLenConfEntry,_V:fgs2924rMaxPktLenConfIndex,'fgs2924rMaxPktLenConfSetting':fgs2924rMaxPktLenConfSetting,'fgs2924rLoopDetectedConf':fgs2924rLoopDetectedConf,'fgs2924rLoopDetectedNumber':fgs2924rLoopDetectedNumber,'fgs2924rLoopDetectedTable':fgs2924rLoopDetectedTable,'fgs2924rLoopDetectedEntry':fgs2924rLoopDetectedEntry,_W:fgs2924rLoopDetectedfIndex,'fgs2924rLoopDetectedPort':fgs2924rLoopDetectedPort,'fgs2924rLoopDetectedLockedPort':fgs2924rLoopDetectedLockedPort,'fgs2924rManagementPolicy':fgs2924rManagementPolicy,'fgs2924rManagementSecurityNumber':fgs2924rManagementSecurityNumber,'fgs2924rManagementSecurityEntryCreate':fgs2924rManagementSecurityEntryCreate,'fgs2924rManagementSecurityTable':fgs2924rManagementSecurityTable,'fgs2924rManagementSecurityEntry':fgs2924rManagementSecurityEntry,_X:fgs2924rManagementSecurityIndex,'fgs2924rManagementSecurityName':fgs2924rManagementSecurityName,'fgs2924rManagementSecurityIpRange':fgs2924rManagementSecurityIpRange,'fgs2924rManagementSecurityIncomigPort':fgs2924rManagementSecurityIncomigPort,'fgs2924rManagementSecurityAccessType':fgs2924rManagementSecurityAccessType,'fgs2924rManagementSecurityAction':fgs2924rManagementSecurityAction,'fgs2924rManagementSecurityEntryAction':fgs2924rManagementSecurityEntryAction,'fgs2924rVLAN':fgs2924rVLAN,'fgs2924rVlanConf':fgs2924rVlanConf,'fgs2924rVlanMode':fgs2924rVlanMode,'fgs2924rManagementVlan':fgs2924rManagementVlan,'fgs2924rPortIsolation':fgs2924rPortIsolation,'fgs2924rTagIdentifier':fgs2924rTagIdentifier,'fgs2924rTagBaseVlanGroup':fgs2924rTagBaseVlanGroup,'fgs2924rTagBaseVlanNumber':fgs2924rTagBaseVlanNumber,'fgs2924rTagBaseVlanGroupEntryCreate':fgs2924rTagBaseVlanGroupEntryCreate,'fgs2924rTagBaseVlanGroupTable':fgs2924rTagBaseVlanGroupTable,'fgs2924rTagBaseVlanGroupEntry':fgs2924rTagBaseVlanGroupEntry,_Y:fgs2924rTagBaseVlanVid,'fgs2924rTagBaseVlanName':fgs2924rTagBaseVlanName,'fgs2924rTagBaseVlanIgmpProxy':fgs2924rTagBaseVlanIgmpProxy,'fgs2924rTagBaseVlanPrivateVlan':fgs2924rTagBaseVlanPrivateVlan,'fgs2924rTagBaseVlanGvrp':fgs2924rTagBaseVlanGvrp,'fgs2924rTagBaseVlanMemberPort':fgs2924rTagBaseVlanMemberPort,'fgs2924rTagBaseVlanEntryAction':fgs2924rTagBaseVlanEntryAction,'fgs2924rVlanPortConfTable':fgs2924rVlanPortConfTable,'fgs2924rVlanPortConfEntry':fgs2924rVlanPortConfEntry,_Z:fgs2924rVlanPortConfIndex,'fgs2924rVlanPortConfVlanAware':fgs2924rVlanPortConfVlanAware,'fgs2924rVlanPortConfIngressFiltering':fgs2924rVlanPortConfIngressFiltering,'fgs2924rVlanPortConfFrameType':fgs2924rVlanPortConfFrameType,'fgs2924rVlanPortConfPvid':fgs2924rVlanPortConfPvid,'fgs2924rVlanPortConfRole':fgs2924rVlanPortConfRole,'fgs2924rVlanPortConfUntagVid':fgs2924rVlanPortConfUntagVid,'fgs2924rVlanPortConfDoubleTag':fgs2924rVlanPortConfDoubleTag,'fgs2924rPortBaseVlanGroup':fgs2924rPortBaseVlanGroup,'fgs2924rPortBaseVlanNumber':fgs2924rPortBaseVlanNumber,'fgs2924rPortBaseVlanGroupEntryCreate':fgs2924rPortBaseVlanGroupEntryCreate,'fgs2924rPortBaseVlanGroupTable':fgs2924rPortBaseVlanGroupTable,'fgs2924rPortBaseVlanGroupEntry':fgs2924rPortBaseVlanGroupEntry,_a:fgs2924rPortBaseVlanGroupIndex,'fgs2924rPortBaseVlanGroupName':fgs2924rPortBaseVlanGroupName,'fgs2924rPortBaseVlanGroupMembers':fgs2924rPortBaseVlanGroupMembers,'fgs2924rPortBaseVlanGroupEntryAction':fgs2924rPortBaseVlanGroupEntryAction,'fgs2924rMacTableInfo':fgs2924rMacTableInfo,'fgs2924rMacTableConf':fgs2924rMacTableConf,'fgs2924rMacAgeTime':fgs2924rMacAgeTime,'fgs2924rMacTableLearningConfTable':fgs2924rMacTableLearningConfTable,'fgs2924rMacTableLearningConfEntry':fgs2924rMacTableLearningConfEntry,_b:fgs2924rMacTableLearningConfIndex,'fgs2924rMacTableLearningConfstate':fgs2924rMacTableLearningConfstate,'fgs2924rMacTableStaticFilter':fgs2924rMacTableStaticFilter,'fgs2924rMacTableStaticFilterNumber':fgs2924rMacTableStaticFilterNumber,'fgs2924rMacTableStaticFilterEntryCreate':fgs2924rMacTableStaticFilterEntryCreate,'fgs2924rMacTableStaticFilterTable':fgs2924rMacTableStaticFilterTable,'fgs2924rMacTableStaticFilterEntry':fgs2924rMacTableStaticFilterEntry,_c:fgs2924rMacTableStaticFilterIndex,'fgs2924rMacTableStaticFilterMac':fgs2924rMacTableStaticFilterMac,'fgs2924rMacTableStaticFilterVid':fgs2924rMacTableStaticFilterVid,'fgs2924rMacTableStaticFilterAlias':fgs2924rMacTableStaticFilterAlias,'fgs2924rMacTableStaticFilterEntryAction':fgs2924rMacTableStaticFilterEntryAction,'fgs2924rMacTableStaticForward':fgs2924rMacTableStaticForward,'fgs2924rMacTableStaticForwardNumber':fgs2924rMacTableStaticForwardNumber,'fgs2924rMacTableStaticForwardEntryCreate':fgs2924rMacTableStaticForwardEntryCreate,'fgs2924rMacTableStaticForwardTable':fgs2924rMacTableStaticForwardTable,'fgs2924rMacTableStaticForwardEntry':fgs2924rMacTableStaticForwardEntry,_d:fgs2924rMacTableStaticForwardIndex,'fgs2924rMacTableStaticForwardMac':fgs2924rMacTableStaticForwardMac,'fgs2924rMacTableStaticForwardPort':fgs2924rMacTableStaticForwardPort,'fgs2924rMacTableStaticForwardVid':fgs2924rMacTableStaticForwardVid,'fgs2924rMacTableStaticForwardAlias':fgs2924rMacTableStaticForwardAlias,'fgs2924rMacTableStaticForwardEntryAction':fgs2924rMacTableStaticForwardEntryAction,'fgs2924rMacAlias':fgs2924rMacAlias,'fgs2924rMacAliasNumber':fgs2924rMacAliasNumber,'fgs2924rMacAliasEntryCreate':fgs2924rMacAliasEntryCreate,'fgs2924rMacAliasTable':fgs2924rMacAliasTable,'fgs2924rMacAliasEntry':fgs2924rMacAliasEntry,_e:fgs2924rMacAliasIndex,'fgs2924rAliasMac':fgs2924rAliasMac,'fgs2924rAliasName':fgs2924rAliasName,'fgs2924rMacAliasEntryAction':fgs2924rMacAliasEntryAction,'fgs2924rGVRPInfo':fgs2924rGVRPInfo,'fgs2924rGvrpConf':fgs2924rGvrpConf,'fgs2924rGvrpConfState':fgs2924rGvrpConfState,'fgs2924rGvrpConfTable':fgs2924rGvrpConfTable,'fgs2924rGvrpConfEntry':fgs2924rGvrpConfEntry,_f:fgs2924rGvrpConfIndex,'fgs2924rGvrpConfJoinTime':fgs2924rGvrpConfJoinTime,'fgs2924rGvrpConfLeaveTime':fgs2924rGvrpConfLeaveTime,'fgs2924rGvrpConfLeaveAllTime':fgs2924rGvrpConfLeaveAllTime,'fgs2924rGvrpConfDefaultAppMode':fgs2924rGvrpConfDefaultAppMode,'fgs2924rGvrpConfDefaultRegMode':fgs2924rGvrpConfDefaultRegMode,'fgs2924rGvrpConfRestrictedMode':fgs2924rGvrpConfRestrictedMode,'fgs2924rGvrpCounter':fgs2924rGvrpCounter,'fgs2924rGvrpCounterTable':fgs2924rGvrpCounterTable,'fgs2924rGvrpCounterEntry':fgs2924rGvrpCounterEntry,_g:fgs2924rGvrpCounterIndex,'fgs2924rGvrpCounterRxTotalGvrpPkts':fgs2924rGvrpCounterRxTotalGvrpPkts,'fgs2924rGvrpCounterRxInvalidGvrpPkts':fgs2924rGvrpCounterRxInvalidGvrpPkts,'fgs2924rGvrpCounterRxLeaveAllMsg':fgs2924rGvrpCounterRxLeaveAllMsg,'fgs2924rGvrpCounterRxJoinEmptyMsg':fgs2924rGvrpCounterRxJoinEmptyMsg,'fgs2924rGvrpCounterRxJoinInMsg':fgs2924rGvrpCounterRxJoinInMsg,'fgs2924rGvrpCounterRxLeaveEmptyMsg':fgs2924rGvrpCounterRxLeaveEmptyMsg,'fgs2924rGvrpCounterRxEmptyMsg':fgs2924rGvrpCounterRxEmptyMsg,'fgs2924rGvrpCounterTxTotalGvrpPkts':fgs2924rGvrpCounterTxTotalGvrpPkts,'fgs2924rGvrpCounterTxLeaveAllMsg':fgs2924rGvrpCounterTxLeaveAllMsg,'fgs2924rGvrpCounterTxJoinEmptyMsg':fgs2924rGvrpCounterTxJoinEmptyMsg,'fgs2924rGvrpCounterTxJoinInMsg':fgs2924rGvrpCounterTxJoinInMsg,'fgs2924rGvrpCounterTxLeaveEmptyMsg':fgs2924rGvrpCounterTxLeaveEmptyMsg,'fgs2924rGvrpCounterTxEmptyMsg':fgs2924rGvrpCounterTxEmptyMsg,'fgs2924rGvrpGroup':fgs2924rGvrpGroup,'fgs2924rGvrpGroupNumber':fgs2924rGvrpGroupNumber,'fgs2924rGvrpGroupTable':fgs2924rGvrpGroupTable,'fgs2924rGvrpGroupEntry':fgs2924rGvrpGroupEntry,_h:fgs2924rGvrpGroupId,'fgs2924rGvrpGroupVid':fgs2924rGvrpGroupVid,'fgs2924rGvrpGroupMemberPort':fgs2924rGvrpGroupMemberPort,'fgs2924rGvrpGroupAdministrativeCtrlTable':fgs2924rGvrpGroupAdministrativeCtrlTable,'fgs2924rGvrpGroupAdministrativeCtrlEntry':fgs2924rGvrpGroupAdministrativeCtrlEntry,_i:fgs2924rGvrpGroupAdministrativeCtrlVid,_j:fgs2924rGvrpGroupAdministrativeCtrlPort,'fgs2924rGvrpGroupAdministrativeCtrlApp':fgs2924rGvrpGroupAdministrativeCtrlApp,'fgs2924rGvrpGroupAdministrativeCtrlReg':fgs2924rGvrpGroupAdministrativeCtrlReg,'fgs2924rQosInfo':fgs2924rQosInfo,'fgs2924rQosPortConf':fgs2924rQosPortConf,'fgs2924rQosNumOfClasses':fgs2924rQosNumOfClasses,'fgs2924rQosPortConfTable':fgs2924rQosPortConfTable,'fgs2924rQosPortConfEntry':fgs2924rQosPortConfEntry,_k:fgs2924rQosPortConfIndex,'fgs2924rQosPortConfDefaultClasses':fgs2924rQosPortConfDefaultClasses,'fgs2924rQosPortConfQCL':fgs2924rQosPortConfQCL,'fgs2924rQosPortConfUserPriority':fgs2924rQosPortConfUserPriority,'fgs2924rQosPortConfQueuingMode':fgs2924rQosPortConfQueuingMode,'fgs2924rQosPortConfQueueWeightedLow':fgs2924rQosPortConfQueueWeightedLow,'fgs2924rQosPortConfQueueWeightedNormal':fgs2924rQosPortConfQueueWeightedNormal,'fgs2924rQosPortConfQueueWeightedMedium':fgs2924rQosPortConfQueueWeightedMedium,'fgs2924rQosPortConfQueueWeightedHigh':fgs2924rQosPortConfQueueWeightedHigh,'fgs2924rQosRateLimiters':fgs2924rQosRateLimiters,'fgs2924rQosRateLimitersTable':fgs2924rQosRateLimitersTable,'fgs2924rQosRateLimitersEntry':fgs2924rQosRateLimitersEntry,_l:fgs2924rQosRateLimitersIndex,'fgs2924rQosRateLimitersPolicer':fgs2924rQosRateLimitersPolicer,'fgs2924rQosRateLimitersPolicerRate':fgs2924rQosRateLimitersPolicerRate,'fgs2924rQosRateLimitersShaper':fgs2924rQosRateLimitersShaper,'fgs2924rQosRateLimitersShaperRate':fgs2924rQosRateLimitersShaperRate,'fgs2924rQosStormCtrl':fgs2924rQosStormCtrl,'fgs2924rQosStromCtrlFloodedUnicastStatus':fgs2924rQosStromCtrlFloodedUnicastStatus,'fgs2924rQosStromCtrlFloodedUnicastRate':fgs2924rQosStromCtrlFloodedUnicastRate,'fgs2924rQosStromCtrlMulticastStatus':fgs2924rQosStromCtrlMulticastStatus,'fgs2924rQosStromCtrlMulticastRate':fgs2924rQosStromCtrlMulticastRate,'fgs2924rQosStromCtrlBroadcastStatus':fgs2924rQosStromCtrlBroadcastStatus,'fgs2924rQosStromCtrlBroadcastRate':fgs2924rQosStromCtrlBroadcastRate,'fgs2924rQosQCL':fgs2924rQosQCL,'fgs2924rQosQclCreate':fgs2924rQosQclCreate,'fgs2924rQosQclTable':fgs2924rQosQclTable,'fgs2924rQosQclEntry':fgs2924rQosQclEntry,_m:fgs2924rQosQclNo,_n:fgs2924rQosQclQceListNo,'fgs2924rQosQclQceMoveTo':fgs2924rQosQclQceMoveTo,'fgs2924rQosQclQceType':fgs2924rQosQclQceType,'fgs2924rQosQclQceValue':fgs2924rQosQclQceValue,'fgs2924rQosQclQceTrafficClass':fgs2924rQosQclQceTrafficClass,'fgs2924rQosQclQcePriority0Class':fgs2924rQosQclQcePriority0Class,'fgs2924rQosQclQcePriority1Class':fgs2924rQosQclQcePriority1Class,'fgs2924rQosQclQcePriority2Class':fgs2924rQosQclQcePriority2Class,'fgs2924rQosQclQcePriority3Class':fgs2924rQosQclQcePriority3Class,'fgs2924rQosQclQcePriority4Class':fgs2924rQosQclQcePriority4Class,'fgs2924rQosQclQcePriority5Class':fgs2924rQosQclQcePriority5Class,'fgs2924rQosQclQcePriority6Class':fgs2924rQosQclQcePriority6Class,'fgs2924rQosQclQcePriority7Class':fgs2924rQosQclQcePriority7Class,'fgs2924rQosQclQceEntryAction':fgs2924rQosQclQceEntryAction,'fgs2924rAclInfo':fgs2924rAclInfo,'fgs2924rAclPortsConfTable':fgs2924rAclPortsConfTable,'fgs2924rAclPortsConfEntry':fgs2924rAclPortsConfEntry,_o:fgs2924rAclPortsConfIndex,'fgs2924rAclPortsConfPolicyId':fgs2924rAclPortsConfPolicyId,'fgs2924rAclPortsConfAction':fgs2924rAclPortsConfAction,'fgs2924rAclPortsConfRateLimiterId':fgs2924rAclPortsConfRateLimiterId,'fgs2924rAclPortsConfPortCopy':fgs2924rAclPortsConfPortCopy,'fgs2924rAclPortsConfCounter':fgs2924rAclPortsConfCounter,'fgs2924rAclRateLimiter':fgs2924rAclRateLimiter,'fgs2924rAclRateLimiterTable':fgs2924rAclRateLimiterTable,'fgs2924rAclRateLimiterEntry':fgs2924rAclRateLimiterEntry,_p:fgs2924rAclRateLimiterIndex,'fgs2924rAclRateLimiterRate':fgs2924rAclRateLimiterRate,'fgs2924rAclInfoViewTable':fgs2924rAclInfoViewTable,'fgs2924rAclInfoViewEntry':fgs2924rAclInfoViewEntry,_q:fgs2924rAclInfoViewNo,'fgs2924rAceIngressPort':fgs2924rAceIngressPort,'fgs2924rAceFrameType':fgs2924rAceFrameType,'fgs2924rAceAction':fgs2924rAceAction,'fgs2924rAceRateLimiter':fgs2924rAceRateLimiter,'fgs2924rAcePortCopy':fgs2924rAcePortCopy,'fgs2924rAceCounter':fgs2924rAceCounter,'fgs2924rSmacFilter':fgs2924rSmacFilter,'fgs2924rDmacFilter':fgs2924rDmacFilter,'fgs2924rVlanIdFilter':fgs2924rVlanIdFilter,'fgs2924rVlanTagPriority':fgs2924rVlanTagPriority,'fgs2924rEtherTypeFilter':fgs2924rEtherTypeFilter,'fgs2924rArpRarp':fgs2924rArpRarp,'fgs2924rArpRequestReply':fgs2924rArpRequestReply,'fgs2924rArpSenderIpFilter':fgs2924rArpSenderIpFilter,'fgs2924rArpSenderIpAddress':fgs2924rArpSenderIpAddress,'fgs2924rArpSenderIpMask':fgs2924rArpSenderIpMask,'fgs2924rArpTargetIpFilter':fgs2924rArpTargetIpFilter,'fgs2924rArpTargetIpAddress':fgs2924rArpTargetIpAddress,'fgs2924rArpTargetIpMask':fgs2924rArpTargetIpMask,'fgs2924rArpSmacMatch':fgs2924rArpSmacMatch,'fgs2924rArpRarpDmacMatch':fgs2924rArpRarpDmacMatch,'fgs2924rArpIpEthernetLength':fgs2924rArpIpEthernetLength,'fgs2924rArpIp':fgs2924rArpIp,'fgs2924rArpEthernet':fgs2924rArpEthernet,'fgs2924rIpProtocolFilter':fgs2924rIpProtocolFilter,'fgs2924rIpProtocolValue':fgs2924rIpProtocolValue,'fgs2924rIpTTL':fgs2924rIpTTL,'fgs2924rIpFragment':fgs2924rIpFragment,'fgs2924rIpOption':fgs2924rIpOption,'fgs2924rSipFilter':fgs2924rSipFilter,'fgs2924rSipAddress':fgs2924rSipAddress,'fgs2924rSipMask':fgs2924rSipMask,'fgs2924rDipFilter':fgs2924rDipFilter,'fgs2924rDipAddress':fgs2924rDipAddress,'fgs2924rDipMask':fgs2924rDipMask,'fgs2924rIcmpTypeFilter':fgs2924rIcmpTypeFilter,'fgs2924rIcmpCodeFilter':fgs2924rIcmpCodeFilter,'fgs2924rUdpSourcePortFilter':fgs2924rUdpSourcePortFilter,'fgs2924rUdpDestPortFilter':fgs2924rUdpDestPortFilter,'fgs2924rTcpSourcePortFilter':fgs2924rTcpSourcePortFilter,'fgs2924rTcpDestPortFilter':fgs2924rTcpDestPortFilter,'fgs2924rTcpFIN':fgs2924rTcpFIN,'fgs2924rTcpSYN':fgs2924rTcpSYN,'fgs2924rTcpRST':fgs2924rTcpRST,'fgs2924rTcpPSH':fgs2924rTcpPSH,'fgs2924rTcpACK':fgs2924rTcpACK,'fgs2924rTcpURG':fgs2924rTcpURG,'fgs2924rAclInfoEntryAction':fgs2924rAclInfoEntryAction,'fgs2924rAclInfoConf':fgs2924rAclInfoConf,'fgs2924rAceNo':fgs2924rAceNo,'fgs2924rAceMoveTo':fgs2924rAceMoveTo,'fgs2924rAceIngressPortConf':fgs2924rAceIngressPortConf,'fgs2924rAceFrameTypeConf':fgs2924rAceFrameTypeConf,'fgs2924rAceFrameTypeParameters':fgs2924rAceFrameTypeParameters,'fgs2924rEthernetTypeFilter':fgs2924rEthernetTypeFilter,'fgs2924rAclArpParameters':fgs2924rAclArpParameters,'fgs2924rAceArpRarp':fgs2924rAceArpRarp,'fgs2924rAceArpRequestReply':fgs2924rAceArpRequestReply,'fgs2924rAceArpSenderIpFilter':fgs2924rAceArpSenderIpFilter,'fgs2924rAceArpSenderIpAddress':fgs2924rAceArpSenderIpAddress,'fgs2924rAceArpSenderIpMask':fgs2924rAceArpSenderIpMask,'fgs2924rAceArpTargetIpFilter':fgs2924rAceArpTargetIpFilter,'fgs2924rAceArpTargetIpAddress':fgs2924rAceArpTargetIpAddress,'fgs2924rAceArpTargetIpMask':fgs2924rAceArpTargetIpMask,'fgs2924rAceArpSmacMatch':fgs2924rAceArpSmacMatch,'fgs2924rAceArpRarpDmacMatch':fgs2924rAceArpRarpDmacMatch,'fgs2924rAceArpIpEthernetLength':fgs2924rAceArpIpEthernetLength,'fgs2924rAceArpIp':fgs2924rAceArpIp,'fgs2924rAceArpEthernet':fgs2924rAceArpEthernet,'fgs2924rAclIpParameters':fgs2924rAclIpParameters,'fgs2924rAceIpProtocolFilter':fgs2924rAceIpProtocolFilter,'fgs2924rAceIpProtocolFilterParameters':fgs2924rAceIpProtocolFilterParameters,'fgs2924rAceIcmpParameters':fgs2924rAceIcmpParameters,'fgs2924rAceIcmpTypeFilter':fgs2924rAceIcmpTypeFilter,'fgs2924rAceIcmpCodeFilter':fgs2924rAceIcmpCodeFilter,'fgs2924rAceUdpParameters':fgs2924rAceUdpParameters,'fgs2924rUdpSourcePortFilterConf':fgs2924rUdpSourcePortFilterConf,'fgs2924rUdpDestPortFilterConf':fgs2924rUdpDestPortFilterConf,'fgs2924rAceTcpParameters':fgs2924rAceTcpParameters,'fgs2924rTcpSourcePortFilterConf':fgs2924rTcpSourcePortFilterConf,'fgs2924rTcpDestPortFilterConf':fgs2924rTcpDestPortFilterConf,'fgs2924rTcpFINConf':fgs2924rTcpFINConf,'fgs2924rTcpSYNConf':fgs2924rTcpSYNConf,'fgs2924rTcpRSTConf':fgs2924rTcpRSTConf,'fgs2924rTcpPSHConf':fgs2924rTcpPSHConf,'fgs2924rTcpACKConf':fgs2924rTcpACKConf,'fgs2924rTcpURGConf':fgs2924rTcpURGConf,'fgs2924rAceIpProtocolValue':fgs2924rAceIpProtocolValue,'fgs2924rAceIpTTL':fgs2924rAceIpTTL,'fgs2924rAceIpFragment':fgs2924rAceIpFragment,'fgs2924rAceIpOption':fgs2924rAceIpOption,'fgs2924rAceSipFilter':fgs2924rAceSipFilter,'fgs2924rAceSipAddress':fgs2924rAceSipAddress,'fgs2924rAceSipMask':fgs2924rAceSipMask,'fgs2924rAceDipFilter':fgs2924rAceDipFilter,'fgs2924rAceDipAddress':fgs2924rAceDipAddress,'fgs2924rAceDipMask':fgs2924rAceDipMask,'fgs2924rAceActionConf':fgs2924rAceActionConf,'fgs2924rAceRateLimiterConf':fgs2924rAceRateLimiterConf,'fgs2924rAcePortCopyConf':fgs2924rAcePortCopyConf,'fgs2924rAceMacParameters':fgs2924rAceMacParameters,'fgs2924rAceSmacFilter':fgs2924rAceSmacFilter,'fgs2924rAceDmacFilter':fgs2924rAceDmacFilter,'fgs2924rAceVlanParameters':fgs2924rAceVlanParameters,'fgs2924rAceVlanIdFilter':fgs2924rAceVlanIdFilter,'fgs2924rAceTagPriority':fgs2924rAceTagPriority,'fgs2924rAceInfoEntryAction':fgs2924rAceInfoEntryAction,'fgs2924rIpMacBind':fgs2924rIpMacBind,'fgs2924rIpMacBindConf':fgs2924rIpMacBindConf,'fgs2924rIpMacBindstate':fgs2924rIpMacBindstate,'fgs2924rIpMacBindTrustPort':fgs2924rIpMacBindTrustPort,'fgs2924rIpMacBindSetting':fgs2924rIpMacBindSetting,'fgs2924rIpMacBindSettingNumber':fgs2924rIpMacBindSettingNumber,'fgs2924rIpMacBindSettingEntryCreate':fgs2924rIpMacBindSettingEntryCreate,'fgs2924rIpMacBindSettingTable':fgs2924rIpMacBindSettingTable,'fgs2924rIpMacBindSettingEntry':fgs2924rIpMacBindSettingEntry,_r:fgs2924rIpMacBindSettingIndex,'fgs2924rIpMacBindSettingMAC':fgs2924rIpMacBindSettingMAC,'fgs2924rIpMacBindSettingIP':fgs2924rIpMacBindSettingIP,'fgs2924rIpMacBindSettingPort':fgs2924rIpMacBindSettingPort,'fgs2924rIpMacBindSettingVID':fgs2924rIpMacBindSettingVID,'fgs2924rIpMacBindSettingEntryAction':fgs2924rIpMacBindSettingEntryAction,'fgs2924rTrapEntry':fgs2924rTrapEntry,'fgs2924rUserLogin':fgs2924rUserLogin,'fgs2924rUserLogout':fgs2924rUserLogout,'fgs2924rModuleInserted':fgs2924rModuleInserted,'fgs2924rModuleRemoved':fgs2924rModuleRemoved,'fgs2924rDualMediaSwapped':fgs2924rDualMediaSwapped,'fgs2924rLoopDetected':fgs2924rLoopDetected,'fgs2924rStpStateDisabled':fgs2924rStpStateDisabled,'fgs2924rStpStateEnabled':fgs2924rStpStateEnabled,'fgs2924rStpTopologyChanged':fgs2924rStpTopologyChanged,'fgs2924rLacpStateDisabled':fgs2924rLacpStateDisabled,'fgs2924rLacpStateEnabled':fgs2924rLacpStateEnabled,'fgs2924rLacpPortAdded':fgs2924rLacpPortAdded,'fgs2924rLacpPortTrunkFailure':fgs2924rLacpPortTrunkFailure,'fgs2924rGvrpStateDisabled':fgs2924rGvrpStateDisabled,'fgs2924rGvrpStateEnabled':fgs2924rGvrpStateEnabled,'fgs2924rVlanPortBaseEnabled':fgs2924rVlanPortBaseEnabled,'fgs2924rVlanTagBaseEnabled':fgs2924rVlanTagBaseEnabled,'fgs2924rIpmbStateEnabled':fgs2924rIpmbStateEnabled,'fgs2924rIpmbStateDisabled':fgs2924rIpmbStateDisabled,'fgs2924rIpmbEntryFailure':fgs2924rIpmbEntryFailure,'fgs2924rTrapVariable':fgs2924rTrapVariable,_I:username,_J:groupId,_K:actorkey,_L:partnerkey,'swapto':swapto,'ipmacIp':ipmacIp,'ipmacMac':ipmacMac,'fgs2924rDot1X':fgs2924rDot1X,'fgs2924rDot1XServerConf':fgs2924rDot1XServerConf,'fgs2924rDot1XServerConfAuthenticationServerIp':fgs2924rDot1XServerConfAuthenticationServerIp,'fgs2924rDot1XServerConfAuthenticationUdpPort':fgs2924rDot1XServerConfAuthenticationUdpPort,'fgs2924rDot1XServerConfAuthenticationServerIp2':fgs2924rDot1XServerConfAuthenticationServerIp2,'fgs2924rDot1XServerConfAuthenticationUdpPort2':fgs2924rDot1XServerConfAuthenticationUdpPort2,'fgs2924rDot1XServerConfAuthenticationSecretKey':fgs2924rDot1XServerConfAuthenticationSecretKey,'fgs2924rDot1XServerConfAccountingServerIp':fgs2924rDot1XServerConfAccountingServerIp,'fgs2924rDot1XServerConfAccountingUdpPort':fgs2924rDot1XServerConfAccountingUdpPort,'fgs2924rDot1XServerConfAccountingServerIp2':fgs2924rDot1XServerConfAccountingServerIp2,'fgs2924rDot1XServerConfAccountingUdpPort2':fgs2924rDot1XServerConfAccountingUdpPort2,'fgs2924rDot1XServerConfAccountingSecretKey':fgs2924rDot1XServerConfAccountingSecretKey,'fgs2924rDot1XPortConfTable':fgs2924rDot1XPortConfTable,'fgs2924rDot1XPortConfEntry':fgs2924rDot1XPortConfEntry,_s:fgs2924rDot1XPort,'fgs2924rDot1XPortMode':fgs2924rDot1XPortMode,'fgs2924rDot1XPortControl':fgs2924rDot1XPortControl,'fgs2924rDot1XPortreAuthMax':fgs2924rDot1XPortreAuthMax,'fgs2924rDot1XPorttxPeriod':fgs2924rDot1XPorttxPeriod,'fgs2924rDot1XPortquietPeriod':fgs2924rDot1XPortquietPeriod,'fgs2924rDot1XPortreAuthEnabled':fgs2924rDot1XPortreAuthEnabled,'fgs2924rDot1XPortreAuthPeriod':fgs2924rDot1XPortreAuthPeriod,'fgs2924rDot1XPortmaxReq':fgs2924rDot1XPortmaxReq,'fgs2924rDot1XPortsuppTimeout':fgs2924rDot1XPortsuppTimeout,'fgs2924rDot1XPortserverTimeout':fgs2924rDot1XPortserverTimeout,'fgs2924rDot1XPortVlanAssignment':fgs2924rDot1XPortVlanAssignment,'fgs2924rDot1XPortGuestVlan':fgs2924rDot1XPortGuestVlan,'fgs2924rDot1XPortAuthFailedVlan':fgs2924rDot1XPortAuthFailedVlan,'fgs2924rDot1XStatusTable':fgs2924rDot1XStatusTable,'fgs2924rDot1XStatusEntry':fgs2924rDot1XStatusEntry,_t:fgs2924rDot1XStatusIndex,'fgs2924rDot1XStatusMode':fgs2924rDot1XStatusMode,'fgs2924rDot1XStatusStatus':fgs2924rDot1XStatusStatus,'fgs2924rDot1XVlanPolicy':fgs2924rDot1XVlanPolicy,'fgs2924rDot1XStatisticsTable':fgs2924rDot1XStatisticsTable,'fgs2924rDot1XStatisticsEntry':fgs2924rDot1XStatisticsEntry,_u:fgs2924rDot1XStatisticsIndex,'fgs2924rDot1XClearCounter':fgs2924rDot1XClearCounter,'fgs2924rDot1XAuthEntersConnecting':fgs2924rDot1XAuthEntersConnecting,'fgs2924rDot1XauthEapLogoffsWhileConnecting':fgs2924rDot1XauthEapLogoffsWhileConnecting,'fgs2924rDot1XAuthEntersAuthenticating':fgs2924rDot1XAuthEntersAuthenticating,'fgs2924rDot1XAuthAuthSuccessesWhileAuthenticating':fgs2924rDot1XAuthAuthSuccessesWhileAuthenticating,'fgs2924rDot1XAuthAuthTimeoutsWhileAuthenticating':fgs2924rDot1XAuthAuthTimeoutsWhileAuthenticating,'fgs2924rDot1XAuthAuthFailWhileAuthenticating':fgs2924rDot1XAuthAuthFailWhileAuthenticating,'fgs2924rDot1XAuthAuthEapStartsWhileAuthenticating':fgs2924rDot1XAuthAuthEapStartsWhileAuthenticating,'fgs2924rDot1XAuthAuthEapLogoffWhileAuthenticating':fgs2924rDot1XAuthAuthEapLogoffWhileAuthenticating,'fgs2924rDot1XAuthAuthReauthsWhileAuthenticated':fgs2924rDot1XAuthAuthReauthsWhileAuthenticated,'fgs2924rDot1XAuthAuthEapStartsWhileAuthenticated':fgs2924rDot1XAuthAuthEapStartsWhileAuthenticated,'fgs2924rDot1XAuthAuthEapLogoffWhileAuthenticated':fgs2924rDot1XAuthAuthEapLogoffWhileAuthenticated,'fgs2924rDot1XBackendResponses':fgs2924rDot1XBackendResponses,'fgs2924rDot1XBackendAccessChallenges':fgs2924rDot1XBackendAccessChallenges,'fgs2924rDot1XBackendOtherRequestsToSupplicant':fgs2924rDot1XBackendOtherRequestsToSupplicant,'fgs2924rDot1XBackendAuthSuccesses':fgs2924rDot1XBackendAuthSuccesses,'fgs2924rDot1XBackendAuthFails':fgs2924rDot1XBackendAuthFails,'fgs2924rDot1XAuthEapolFramesRx':fgs2924rDot1XAuthEapolFramesRx,'fgs2924rDot1XAuthEapolFramesTx':fgs2924rDot1XAuthEapolFramesTx,'fgs2924rDot1XAuthEapolStartFramesRx':fgs2924rDot1XAuthEapolStartFramesRx,'fgs2924rDot1XAuthEapolLogoffFramesRx':fgs2924rDot1XAuthEapolLogoffFramesRx,'fgs2924rDot1XAuthEapolRespIdFramesRx':fgs2924rDot1XAuthEapolRespIdFramesRx,'fgs2924rDot1XAuthEapolRespFramesRx':fgs2924rDot1XAuthEapolRespFramesRx,'fgs2924rDot1XAuthEapolReqIdFramesTx':fgs2924rDot1XAuthEapolReqIdFramesTx,'fgs2924rDot1XAuthEapolReqFramesTx':fgs2924rDot1XAuthEapolReqFramesTx,'fgs2924rDot1XAuthInvalidEapolFramesRx':fgs2924rDot1XAuthInvalidEapolFramesRx,'fgs2924rDot1XAuthEapLengthErrorFramesRx':fgs2924rDot1XAuthEapLengthErrorFramesRx,'fgs2924rDot1XAuthLastEapolFrameVersion':fgs2924rDot1XAuthLastEapolFrameVersion,'fgs2924rDot1XAuthLastEapolFrameSource':fgs2924rDot1XAuthLastEapolFrameSource,'fgs2924rTrunkInfo':fgs2924rTrunkInfo,'fgs2924rTrunkPort':fgs2924rTrunkPort,'fgs2924rTrunkPortTable':fgs2924rTrunkPortTable,'fgs2924rTrunkPortEntry':fgs2924rTrunkPortEntry,_v:fgs2924rTrunkPortIndex,'fgs2924rTrunkPortMethod':fgs2924rTrunkPortMethod,'fgs2924rTrunkPortGroup':fgs2924rTrunkPortGroup,'fgs2924rTrunkPortActiveLacp':fgs2924rTrunkPortActiveLacp,'fgs2924rTrunkPortAggtr':fgs2924rTrunkPortAggtr,'fgs2924rTrunkPortStatus':fgs2924rTrunkPortStatus,'fgs2924rTrunkPortCurrentMode':fgs2924rTrunkPortCurrentMode,'fgs2924rAggregatorView':fgs2924rAggregatorView,'fgs2924rAggregatorViewTable':fgs2924rAggregatorViewTable,'fgs2924rAggregatorViewEntry':fgs2924rAggregatorViewEntry,_w:fgs2924rAggregatorViewIndex,'fgs2924rAggregatorViewMethod':fgs2924rAggregatorViewMethod,'fgs2924rAggregatorViewMemberPorts':fgs2924rAggregatorViewMemberPorts,'fgs2924rAggregatorViewReadyPorts':fgs2924rAggregatorViewReadyPorts,'fgs2924rLacpSystemPriority':fgs2924rLacpSystemPriority,'fgs2924rAggregationHashMode':fgs2924rAggregationHashMode,'fgs2924rHashCodeSourceMacAddress':fgs2924rHashCodeSourceMacAddress,'fgs2924rHashCodeDestinationMacAddress':fgs2924rHashCodeDestinationMacAddress,'fgs2924rHashCodeIpAddress':fgs2924rHashCodeIpAddress,'fgs2924rHashCodeTcpUdpPortNumber':fgs2924rHashCodeTcpUdpPortNumber,'fgs2924rMulticastInfo':fgs2924rMulticastInfo,'fgs2924rIGMPMode':fgs2924rIGMPMode,'fgs2924rIGMPGroupAllowConf':fgs2924rIGMPGroupAllowConf,'fgs2924rIGMPGroupAllowNumber':fgs2924rIGMPGroupAllowNumber,'fgs2924rIGMPGroupAllowEntryCreate':fgs2924rIGMPGroupAllowEntryCreate,'fgs2924rIGMPGroupAllowTable':fgs2924rIGMPGroupAllowTable,'fgs2924rIGMPGroupAllowEntry':fgs2924rIGMPGroupAllowEntry,_x:fgs2924rIGMPGroupAllowNo,'fgs2924rIGMPGroupAllowVid':fgs2924rIGMPGroupAllowVid,'fgs2924rIGMPGroupAllowStartAddress':fgs2924rIGMPGroupAllowStartAddress,'fgs2924rIGMPGroupAllowEndAddress':fgs2924rIGMPGroupAllowEndAddress,'fgs2924rIGMPGroupAllowEntryAction':fgs2924rIGMPGroupAllowEntryAction,'fgs2924rIGMPProxy':fgs2924rIGMPProxy,'fgs2924rIgmpProxyConfGeneralQueryInterval':fgs2924rIgmpProxyConfGeneralQueryInterval,'fgs2924rIgmpProxyConfGeneralQueryRepTimeout':fgs2924rIgmpProxyConfGeneralQueryRepTimeout,'fgs2924rIgmpProxyConfGeneralQueryMaxRepTime':fgs2924rIgmpProxyConfGeneralQueryMaxRepTime,'fgs2924rIgmpProxyConfLastMemberQueryCount':fgs2924rIgmpProxyConfLastMemberQueryCount,'fgs2924rIgmpProxyConfLastMemberQueryInterval':fgs2924rIgmpProxyConfLastMemberQueryInterval,'fgs2924rIgmpProxyConfLastMemberQueryMaxRepTime':fgs2924rIgmpProxyConfLastMemberQueryMaxRepTime,'fgs2924rIgmpProxyConfRouterPorts':fgs2924rIgmpProxyConfRouterPorts,'fgs2924rIgmpProxyGroupMembershipNumber':fgs2924rIgmpProxyGroupMembershipNumber,'fgs2924rIgmpProxyGroupMembershipTable':fgs2924rIgmpProxyGroupMembershipTable,'fgs2924rIgmpProxyGroupMembershipEntry':fgs2924rIgmpProxyGroupMembershipEntry,_y:fgs2924rIgmpProxyGroupNo,'fgs2924rIgmpProxyGroupAddress':fgs2924rIgmpProxyGroupAddress,'fgs2924rIgmpProxyGroupVLANId':fgs2924rIgmpProxyGroupVLANId,'fgs2924rIgmpProxyGroupPortMembers':fgs2924rIgmpProxyGroupPortMembers,'fgs2924rIGMPSnooping':fgs2924rIGMPSnooping,'fgs2924rIgmpSnoopingConfHostTimeout':fgs2924rIgmpSnoopingConfHostTimeout,'fgs2924rIgmpSnoopingConfFastLeave':fgs2924rIgmpSnoopingConfFastLeave,'fgs2924rIgmpSnoopingConfRouterPorts':fgs2924rIgmpSnoopingConfRouterPorts,'fgs2924rIgmpSnoopingGroupMembershipNumber':fgs2924rIgmpSnoopingGroupMembershipNumber,'fgs2924rIgmpSnoopingGroupMembershipTable':fgs2924rIgmpSnoopingGroupMembershipTable,'fgs2924rIgmpSnoopingGroupMembershipEntry':fgs2924rIgmpSnoopingGroupMembershipEntry,_z:fgs2924rIgmpSnoopingGroupNo,'fgs2924rIgmpSnoopingGroupAddress':fgs2924rIgmpSnoopingGroupAddress,'fgs2924rIgmpSnoopingGroupVLANId':fgs2924rIgmpSnoopingGroupVLANId,'fgs2924rIgmpSnoopingGroupPortMembers':fgs2924rIgmpSnoopingGroupPortMembers,'fgs2924rMVR':fgs2924rMVR,'fgs2924rMVRMode':fgs2924rMVRMode,'fgs2924rMVRConfHostTimeout':fgs2924rMVRConfHostTimeout,'fgs2924rMVRConfFastLeave':fgs2924rMVRConfFastLeave,'fgs2924rMVIDConf':fgs2924rMVIDConf,'fgs2924rMVIDNumber':fgs2924rMVIDNumber,'fgs2924rMVIDEntryCreate':fgs2924rMVIDEntryCreate,'fgs2924rMVIDGroupTable':fgs2924rMVIDGroupTable,'fgs2924rMVIDGroupEntry':fgs2924rMVIDGroupEntry,_A0:fgs2924rMVID,'fgs2924rMVIDMemberPort':fgs2924rMVIDMemberPort,'fgs2924rMVIDRouterPorts':fgs2924rMVIDRouterPorts,'fgs2924rMVIDEntryAction':fgs2924rMVIDEntryAction,'fgs2924rMVIDGroupAllowConf':fgs2924rMVIDGroupAllowConf,'fgs2924rMVIDGroupAllowNumber':fgs2924rMVIDGroupAllowNumber,'fgs2924rMVIDGroupAllowEntryCreate':fgs2924rMVIDGroupAllowEntryCreate,'fgs2924rMVIDGroupAllowTable':fgs2924rMVIDGroupAllowTable,'fgs2924rMVIDGroupAllowEntry':fgs2924rMVIDGroupAllowEntry,_A1:fgs2924rMVIDGroupAllowNo,'fgs2924rMVIDGroupAllowMvid':fgs2924rMVIDGroupAllowMvid,'fgs2924rMVIDGroupAllowStartAddress':fgs2924rMVIDGroupAllowStartAddress,'fgs2924rMVIDGroupAllowEndAddress':fgs2924rMVIDGroupAllowEndAddress,'fgs2924rMVIDGroupAllowEntryAction':fgs2924rMVIDGroupAllowEntryAction,'fgs2924rMVRGroupMembershipNumber':fgs2924rMVRGroupMembershipNumber,'fgs2924rMVRGroupMembershipTable':fgs2924rMVRGroupMembershipTable,'fgs2924rMVRGroupMembershipEntry':fgs2924rMVRGroupMembershipEntry,_A2:fgs2924rMVRGroupNo,'fgs2924rMVRGroupAddress':fgs2924rMVRGroupAddress,'fgs2924rMVRGroupVLANId':fgs2924rMVRGroupVLANId,'fgs2924rMVRGroupPortMembers':fgs2924rMVRGroupPortMembers,'fgs2924rDhcpSnooping':fgs2924rDhcpSnooping,'fgs2924rDhcpSnoopingState':fgs2924rDhcpSnoopingState,'fgs2924rDhcpSnoopingInfo':fgs2924rDhcpSnoopingInfo,'fgs2924rDhcpSnoopingCreate':fgs2924rDhcpSnoopingCreate,'fgs2924rDhcpSnoopingTable':fgs2924rDhcpSnoopingTable,'fgs2924rDhcpSnoopingEntry':fgs2924rDhcpSnoopingEntry,_A3:fgs2924rDhcpSnoopingIndex,'fgs2924rDhcpSnoopingVID':fgs2924rDhcpSnoopingVID,'fgs2924rDhcpSnoopingTrustPort1':fgs2924rDhcpSnoopingTrustPort1,'fgs2924rDhcpSnoopingTrustPort2':fgs2924rDhcpSnoopingTrustPort2,'fgs2924rDhcpSnoopingServerIP':fgs2924rDhcpSnoopingServerIP,'fgs2924rDhcpSnoopingOption82':fgs2924rDhcpSnoopingOption82,'fgs2924rDhcpSnoopingAction':fgs2924rDhcpSnoopingAction,'fgs2924rDhcpSnoopingEntryAction':fgs2924rDhcpSnoopingEntryAction,'fgs2924rDhcpSnoopingDefaultData':fgs2924rDhcpSnoopingDefaultData,'fgs2924rDhcpSnoopingDefaultVID':fgs2924rDhcpSnoopingDefaultVID,'fgs2924rDhcpSnoopingDefaultTrustPort1':fgs2924rDhcpSnoopingDefaultTrustPort1,'fgs2924rDhcpSnoopingDefaultTrustPort2':fgs2924rDhcpSnoopingDefaultTrustPort2,'fgs2924rDhcpSnoopingDefaultServerIP':fgs2924rDhcpSnoopingDefaultServerIP,'fgs2924rDhcpSnoopingDefaultOption82':fgs2924rDhcpSnoopingDefaultOption82,'fgs2924rDhcpSnoopingDefaultAction':fgs2924rDhcpSnoopingDefaultAction,'fgs2924rDhcpSnoopingDefaultEntryAction':fgs2924rDhcpSnoopingDefaultEntryAction,'fgs2924rDhcpSnoopingClientTable':fgs2924rDhcpSnoopingClientTable,'fgs2924rDhcpSnoopingClientEntry':fgs2924rDhcpSnoopingClientEntry,_A4:fgs2924rDhcpSnoopingClientIndex,'fgs2924rDhcpSnoopingClientMac':fgs2924rDhcpSnoopingClientMac,'fgs2924rDhcpSnoopingClientVID':fgs2924rDhcpSnoopingClientVID,'fgs2924rDhcpSnoopingClientPort':fgs2924rDhcpSnoopingClientPort,'fgs2924rDhcpSnoopingClientIP':fgs2924rDhcpSnoopingClientIP,'fgs2924rDhcpSnoopingClientLease':fgs2924rDhcpSnoopingClientLease})