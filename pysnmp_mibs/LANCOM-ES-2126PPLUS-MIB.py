_r='es2126PoEplusPoEConfPortNum'
_q='es2126PoEplusPoEStatusPortNum'
_p='es2126PoEplusAggregatorViewIndex'
_o='es2126PoEplusTrunkPortIndex'
_n='es2126PoEplusDot1XPortSecurityPortIndex'
_m='es2126PoEplusPortBasedVlanIndex'
_l='es2126PoEplusVlanPvidPort'
_k='es2126PoEplusTagBasedVlanVid'
_j='es2126PoEplusQoSDSCPPriorityIndex'
_i='es2126PoEplusQoSMTypeTOSPriorityIndex'
_h='es2126PoEplusQoSRTypeTOSPriorityIndex'
_g='es2126PoEplusQoSTTypeTOSPriorityIndex'
_f='es2126PoEplusQoSDTypeTOSPriorityIndex'
_e='es2126PoEplusQoS1pPriorityIndex'
_d='es2126PoEplusManagementSecurityIndex'
_c='es2126PoEplusGvrpGroupId'
_b='es2126PoEplusGvrpCounterIndex'
_a='es2126PoEplusGvrpConfIndex'
_Z='es2126PoEplusMacTableMacAliasIndex'
_Y='es2126PoEplusMacTableStaticMacIndex'
_X='es2126PoEplusMacTableLearnPortLimitIndex'
_W='es2126PoEplusLoopDetectedfIndex'
_V='es2126PoEplusPortSFPInfoIndex'
_U='es2126PoEplusPortBandwidthIndex'
_T='es2126PoEplusPortConfIndex'
_S='es2126PoEplusPortStatusIndex'
_R='es2126PoEplusLogIndex'
_Q='es2126PoEplusEmailUserIndex'
_P='es2126PoEplusEventIndex'
_O='es2126PoEplusMonitorTableIp'
_N='es2126PoEplusTrapHostIndex'
_M='es2126PoEplusAccountIndex'
_L='username'
_K='partnerkey'
_J='actorkey'
_I='groupId'
_H='ifIndex'
_G='IF-MIB'
_F='not-accessible'
_E='LANCOM-ES-2126PPLUS-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
MacAddress,=mibBuilder.importSymbols('BRIDGE-MIB','MacAddress')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
lancomSystems=ModuleIdentity((1,3,6,1,4,1,2356))
_SwitchingSystems_ObjectIdentity=ObjectIdentity
switchingSystems=_SwitchingSystems_ObjectIdentity((1,3,6,1,4,1,2356,800))
_FastEthernetSwitches_ObjectIdentity=ObjectIdentity
fastEthernetSwitches=_FastEthernetSwitches_ObjectIdentity((1,3,6,1,4,1,2356,800,2))
_LancomES2126P_ObjectIdentity=ObjectIdentity
lancomES2126P=_LancomES2126P_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129))
_Es2126PoEplusProduces_ObjectIdentity=ObjectIdentity
es2126PoEplusProduces=_Es2126PoEplusProduces_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1))
_Es2126PoEplusSystem_ObjectIdentity=ObjectIdentity
es2126PoEplusSystem=_Es2126PoEplusSystem_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,1))
_Es2126PoEplusCommonSys_ObjectIdentity=ObjectIdentity
es2126PoEplusCommonSys=_Es2126PoEplusCommonSys_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,1,1))
class _Es2126PoEplusReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_Es2126PoEplusReboot_Type.__name__=_B
_Es2126PoEplusReboot_Object=MibScalar
es2126PoEplusReboot=_Es2126PoEplusReboot_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,1,1),_Es2126PoEplusReboot_Type())
es2126PoEplusReboot.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusReboot.setStatus(_A)
_Es2126PoEplusBiosVsersion_Type=DisplayString
_Es2126PoEplusBiosVsersion_Object=MibScalar
es2126PoEplusBiosVsersion=_Es2126PoEplusBiosVsersion_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,1,2),_Es2126PoEplusBiosVsersion_Type())
es2126PoEplusBiosVsersion.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusBiosVsersion.setStatus(_A)
_Es2126PoEplusFirmwareVersion_Type=DisplayString
_Es2126PoEplusFirmwareVersion_Object=MibScalar
es2126PoEplusFirmwareVersion=_Es2126PoEplusFirmwareVersion_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,1,3),_Es2126PoEplusFirmwareVersion_Type())
es2126PoEplusFirmwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusFirmwareVersion.setStatus(_A)
_Es2126PoEplusHardwareVersion_Type=DisplayString
_Es2126PoEplusHardwareVersion_Object=MibScalar
es2126PoEplusHardwareVersion=_Es2126PoEplusHardwareVersion_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,1,4),_Es2126PoEplusHardwareVersion_Type())
es2126PoEplusHardwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusHardwareVersion.setStatus(_A)
_Es2126PoEplusMechanicalVersion_Type=DisplayString
_Es2126PoEplusMechanicalVersion_Object=MibScalar
es2126PoEplusMechanicalVersion=_Es2126PoEplusMechanicalVersion_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,1,5),_Es2126PoEplusMechanicalVersion_Type())
es2126PoEplusMechanicalVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusMechanicalVersion.setStatus(_A)
_Es2126PoEplusSerialNumber_Type=DisplayString
_Es2126PoEplusSerialNumber_Object=MibScalar
es2126PoEplusSerialNumber=_Es2126PoEplusSerialNumber_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,1,6),_Es2126PoEplusSerialNumber_Type())
es2126PoEplusSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusSerialNumber.setStatus(_A)
_Es2126PoEplusHostMacAddress_Type=DisplayString
_Es2126PoEplusHostMacAddress_Object=MibScalar
es2126PoEplusHostMacAddress=_Es2126PoEplusHostMacAddress_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,1,7),_Es2126PoEplusHostMacAddress_Type())
es2126PoEplusHostMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusHostMacAddress.setStatus(_A)
_Es2126PoEplusDevicePort_Type=DisplayString
_Es2126PoEplusDevicePort_Object=MibScalar
es2126PoEplusDevicePort=_Es2126PoEplusDevicePort_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,1,8),_Es2126PoEplusDevicePort_Type())
es2126PoEplusDevicePort.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusDevicePort.setStatus(_A)
_Es2126PoEplusRamSize_Type=DisplayString
_Es2126PoEplusRamSize_Object=MibScalar
es2126PoEplusRamSize=_Es2126PoEplusRamSize_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,1,9),_Es2126PoEplusRamSize_Type())
es2126PoEplusRamSize.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusRamSize.setStatus(_A)
_Es2126PoEplusFlashSize_Type=DisplayString
_Es2126PoEplusFlashSize_Object=MibScalar
es2126PoEplusFlashSize=_Es2126PoEplusFlashSize_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,1,10),_Es2126PoEplusFlashSize_Type())
es2126PoEplusFlashSize.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusFlashSize.setStatus(_A)
_Es2126PoEplusSystemDescription_Type=DisplayString
_Es2126PoEplusSystemDescription_Object=MibScalar
es2126PoEplusSystemDescription=_Es2126PoEplusSystemDescription_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,1,11),_Es2126PoEplusSystemDescription_Type())
es2126PoEplusSystemDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusSystemDescription.setStatus(_A)
_Es2126PoEplusDeviceName_Type=DisplayString
_Es2126PoEplusDeviceName_Object=MibScalar
es2126PoEplusDeviceName=_Es2126PoEplusDeviceName_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,1,12),_Es2126PoEplusDeviceName_Type())
es2126PoEplusDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDeviceName.setStatus(_A)
_Es2126PoEplusIP_ObjectIdentity=ObjectIdentity
es2126PoEplusIP=_Es2126PoEplusIP_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,1,2))
class _Es2126PoEplusDhcpSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusDhcpSetting_Type.__name__=_B
_Es2126PoEplusDhcpSetting_Object=MibScalar
es2126PoEplusDhcpSetting=_Es2126PoEplusDhcpSetting_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,2,1),_Es2126PoEplusDhcpSetting_Type())
es2126PoEplusDhcpSetting.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDhcpSetting.setStatus(_A)
_Es2126PoEplusIPAddress_Type=IpAddress
_Es2126PoEplusIPAddress_Object=MibScalar
es2126PoEplusIPAddress=_Es2126PoEplusIPAddress_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,2,2),_Es2126PoEplusIPAddress_Type())
es2126PoEplusIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusIPAddress.setStatus(_A)
_Es2126PoEplusNetMask_Type=IpAddress
_Es2126PoEplusNetMask_Object=MibScalar
es2126PoEplusNetMask=_Es2126PoEplusNetMask_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,2,3),_Es2126PoEplusNetMask_Type())
es2126PoEplusNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusNetMask.setStatus(_A)
_Es2126PoEplusDefaultGateway_Type=IpAddress
_Es2126PoEplusDefaultGateway_Object=MibScalar
es2126PoEplusDefaultGateway=_Es2126PoEplusDefaultGateway_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,2,4),_Es2126PoEplusDefaultGateway_Type())
es2126PoEplusDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDefaultGateway.setStatus(_A)
class _Es2126PoEplusDnsSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusDnsSetting_Type.__name__=_B
_Es2126PoEplusDnsSetting_Object=MibScalar
es2126PoEplusDnsSetting=_Es2126PoEplusDnsSetting_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,2,5),_Es2126PoEplusDnsSetting_Type())
es2126PoEplusDnsSetting.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDnsSetting.setStatus(_A)
_Es2126PoEplusDnsServer_Type=IpAddress
_Es2126PoEplusDnsServer_Object=MibScalar
es2126PoEplusDnsServer=_Es2126PoEplusDnsServer_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,2,6),_Es2126PoEplusDnsServer_Type())
es2126PoEplusDnsServer.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDnsServer.setStatus(_A)
_Es2126PoEplusTime_ObjectIdentity=ObjectIdentity
es2126PoEplusTime=_Es2126PoEplusTime_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,1,3))
_Es2126PoEplusSystemCurrentTime_Type=DisplayString
_Es2126PoEplusSystemCurrentTime_Object=MibScalar
es2126PoEplusSystemCurrentTime=_Es2126PoEplusSystemCurrentTime_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,3,1),_Es2126PoEplusSystemCurrentTime_Type())
es2126PoEplusSystemCurrentTime.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusSystemCurrentTime.setStatus(_A)
_Es2126PoEplusManualTimeSetting_Type=DisplayString
_Es2126PoEplusManualTimeSetting_Object=MibScalar
es2126PoEplusManualTimeSetting=_Es2126PoEplusManualTimeSetting_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,3,2),_Es2126PoEplusManualTimeSetting_Type())
es2126PoEplusManualTimeSetting.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusManualTimeSetting.setStatus(_A)
_Es2126PoEplusNTPServer_Type=DisplayString
_Es2126PoEplusNTPServer_Object=MibScalar
es2126PoEplusNTPServer=_Es2126PoEplusNTPServer_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,3,3),_Es2126PoEplusNTPServer_Type())
es2126PoEplusNTPServer.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusNTPServer.setStatus(_A)
class _Es2126PoEplusNTPTimeZone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-12,13))
_Es2126PoEplusNTPTimeZone_Type.__name__=_B
_Es2126PoEplusNTPTimeZone_Object=MibScalar
es2126PoEplusNTPTimeZone=_Es2126PoEplusNTPTimeZone_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,3,4),_Es2126PoEplusNTPTimeZone_Type())
es2126PoEplusNTPTimeZone.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusNTPTimeZone.setStatus(_A)
class _Es2126PoEplusNTPTimeSync_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusNTPTimeSync_Type.__name__=_B
_Es2126PoEplusNTPTimeSync_Object=MibScalar
es2126PoEplusNTPTimeSync=_Es2126PoEplusNTPTimeSync_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,3,5),_Es2126PoEplusNTPTimeSync_Type())
es2126PoEplusNTPTimeSync.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusNTPTimeSync.setStatus(_A)
class _Es2126PoEplusDaylightSavingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5,5))
_Es2126PoEplusDaylightSavingTime_Type.__name__=_B
_Es2126PoEplusDaylightSavingTime_Object=MibScalar
es2126PoEplusDaylightSavingTime=_Es2126PoEplusDaylightSavingTime_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,3,6),_Es2126PoEplusDaylightSavingTime_Type())
es2126PoEplusDaylightSavingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDaylightSavingTime.setStatus(_A)
_Es2126PoEplusDaylightStartTime_Type=DisplayString
_Es2126PoEplusDaylightStartTime_Object=MibScalar
es2126PoEplusDaylightStartTime=_Es2126PoEplusDaylightStartTime_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,3,7),_Es2126PoEplusDaylightStartTime_Type())
es2126PoEplusDaylightStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDaylightStartTime.setStatus(_A)
_Es2126PoEplusDaylightEndTime_Type=DisplayString
_Es2126PoEplusDaylightEndTime_Object=MibScalar
es2126PoEplusDaylightEndTime=_Es2126PoEplusDaylightEndTime_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,3,8),_Es2126PoEplusDaylightEndTime_Type())
es2126PoEplusDaylightEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDaylightEndTime.setStatus(_A)
_Es2126PoEplusAccount_ObjectIdentity=ObjectIdentity
es2126PoEplusAccount=_Es2126PoEplusAccount_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,1,4))
class _Es2126PoEplusAccountNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Es2126PoEplusAccountNumber_Type.__name__=_B
_Es2126PoEplusAccountNumber_Object=MibScalar
es2126PoEplusAccountNumber=_Es2126PoEplusAccountNumber_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,4,1),_Es2126PoEplusAccountNumber_Type())
es2126PoEplusAccountNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusAccountNumber.setStatus(_A)
_Es2126PoEplusAccountTable_Object=MibTable
es2126PoEplusAccountTable=_Es2126PoEplusAccountTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,4,2))
if mibBuilder.loadTexts:es2126PoEplusAccountTable.setStatus(_A)
_Es2126PoEplusAccountEntry_Object=MibTableRow
es2126PoEplusAccountEntry=_Es2126PoEplusAccountEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,4,2,1))
es2126PoEplusAccountEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:es2126PoEplusAccountEntry.setStatus(_A)
class _Es2126PoEplusAccountIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Es2126PoEplusAccountIndex_Type.__name__=_B
_Es2126PoEplusAccountIndex_Object=MibTableColumn
es2126PoEplusAccountIndex=_Es2126PoEplusAccountIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,4,2,1,1),_Es2126PoEplusAccountIndex_Type())
es2126PoEplusAccountIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusAccountIndex.setStatus(_A)
_Es2126PoEplusAccountAuthorization_Type=DisplayString
_Es2126PoEplusAccountAuthorization_Object=MibTableColumn
es2126PoEplusAccountAuthorization=_Es2126PoEplusAccountAuthorization_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,4,2,1,2),_Es2126PoEplusAccountAuthorization_Type())
es2126PoEplusAccountAuthorization.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusAccountAuthorization.setStatus(_A)
_Es2126PoEplusAccountName_Type=DisplayString
_Es2126PoEplusAccountName_Object=MibTableColumn
es2126PoEplusAccountName=_Es2126PoEplusAccountName_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,4,2,1,3),_Es2126PoEplusAccountName_Type())
es2126PoEplusAccountName.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusAccountName.setStatus(_A)
_Es2126PoEplusAccountPassword_Type=DisplayString
_Es2126PoEplusAccountPassword_Object=MibTableColumn
es2126PoEplusAccountPassword=_Es2126PoEplusAccountPassword_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,4,2,1,4),_Es2126PoEplusAccountPassword_Type())
es2126PoEplusAccountPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusAccountPassword.setStatus(_A)
_Es2126PoEplusAccountAddName_Type=DisplayString
_Es2126PoEplusAccountAddName_Object=MibScalar
es2126PoEplusAccountAddName=_Es2126PoEplusAccountAddName_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,4,3),_Es2126PoEplusAccountAddName_Type())
es2126PoEplusAccountAddName.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusAccountAddName.setStatus(_A)
_Es2126PoEplusAccountAddPassword_Type=DisplayString
_Es2126PoEplusAccountAddPassword_Object=MibScalar
es2126PoEplusAccountAddPassword=_Es2126PoEplusAccountAddPassword_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,4,4),_Es2126PoEplusAccountAddPassword_Type())
es2126PoEplusAccountAddPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusAccountAddPassword.setStatus(_A)
class _Es2126PoEplusDoAccountAdd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusDoAccountAdd_Type.__name__=_B
_Es2126PoEplusDoAccountAdd_Object=MibScalar
es2126PoEplusDoAccountAdd=_Es2126PoEplusDoAccountAdd_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,4,5),_Es2126PoEplusDoAccountAdd_Type())
es2126PoEplusDoAccountAdd.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDoAccountAdd.setStatus(_A)
class _Es2126PoEplusAccountDel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,5))
_Es2126PoEplusAccountDel_Type.__name__=_B
_Es2126PoEplusAccountDel_Object=MibScalar
es2126PoEplusAccountDel=_Es2126PoEplusAccountDel_Object((1,3,6,1,4,1,2356,800,2,2129,1,1,4,6),_Es2126PoEplusAccountDel_Type())
es2126PoEplusAccountDel.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusAccountDel.setStatus(_A)
_Es2126PoEplusSnmp_ObjectIdentity=ObjectIdentity
es2126PoEplusSnmp=_Es2126PoEplusSnmp_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,2))
_Es2126PoEplusGetCommunity_Type=DisplayString
_Es2126PoEplusGetCommunity_Object=MibScalar
es2126PoEplusGetCommunity=_Es2126PoEplusGetCommunity_Object((1,3,6,1,4,1,2356,800,2,2129,1,2,1),_Es2126PoEplusGetCommunity_Type())
es2126PoEplusGetCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusGetCommunity.setStatus(_A)
_Es2126PoEplusSetCommunity_Type=DisplayString
_Es2126PoEplusSetCommunity_Object=MibScalar
es2126PoEplusSetCommunity=_Es2126PoEplusSetCommunity_Object((1,3,6,1,4,1,2356,800,2,2129,1,2,2),_Es2126PoEplusSetCommunity_Type())
es2126PoEplusSetCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusSetCommunity.setStatus(_A)
class _Es2126PoEplusTrapHostNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_Es2126PoEplusTrapHostNumber_Type.__name__=_B
_Es2126PoEplusTrapHostNumber_Object=MibScalar
es2126PoEplusTrapHostNumber=_Es2126PoEplusTrapHostNumber_Object((1,3,6,1,4,1,2356,800,2,2129,1,2,3),_Es2126PoEplusTrapHostNumber_Type())
es2126PoEplusTrapHostNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusTrapHostNumber.setStatus(_A)
_Es2126PoEplusTrapHostTable_Object=MibTable
es2126PoEplusTrapHostTable=_Es2126PoEplusTrapHostTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,2,4))
if mibBuilder.loadTexts:es2126PoEplusTrapHostTable.setStatus(_A)
_Es2126PoEplusTrapHostEntry_Object=MibTableRow
es2126PoEplusTrapHostEntry=_Es2126PoEplusTrapHostEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,2,4,1))
es2126PoEplusTrapHostEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:es2126PoEplusTrapHostEntry.setStatus(_A)
class _Es2126PoEplusTrapHostIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_Es2126PoEplusTrapHostIndex_Type.__name__=_B
_Es2126PoEplusTrapHostIndex_Object=MibTableColumn
es2126PoEplusTrapHostIndex=_Es2126PoEplusTrapHostIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,2,4,1,1),_Es2126PoEplusTrapHostIndex_Type())
es2126PoEplusTrapHostIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusTrapHostIndex.setStatus(_A)
_Es2126PoEplusTrapHostIP_Type=IpAddress
_Es2126PoEplusTrapHostIP_Object=MibTableColumn
es2126PoEplusTrapHostIP=_Es2126PoEplusTrapHostIP_Object((1,3,6,1,4,1,2356,800,2,2129,1,2,4,1,2),_Es2126PoEplusTrapHostIP_Type())
es2126PoEplusTrapHostIP.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusTrapHostIP.setStatus(_A)
class _Es2126PoEplusTrapHostPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Es2126PoEplusTrapHostPort_Type.__name__=_B
_Es2126PoEplusTrapHostPort_Object=MibTableColumn
es2126PoEplusTrapHostPort=_Es2126PoEplusTrapHostPort_Object((1,3,6,1,4,1,2356,800,2,2129,1,2,4,1,3),_Es2126PoEplusTrapHostPort_Type())
es2126PoEplusTrapHostPort.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusTrapHostPort.setStatus(_A)
_Es2126PoEplusTrapHostCommunity_Type=DisplayString
_Es2126PoEplusTrapHostCommunity_Object=MibTableColumn
es2126PoEplusTrapHostCommunity=_Es2126PoEplusTrapHostCommunity_Object((1,3,6,1,4,1,2356,800,2,2129,1,2,4,1,4),_Es2126PoEplusTrapHostCommunity_Type())
es2126PoEplusTrapHostCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusTrapHostCommunity.setStatus(_A)
_Es2126PoEplusRegisterMonitor_Type=DisplayString
_Es2126PoEplusRegisterMonitor_Object=MibScalar
es2126PoEplusRegisterMonitor=_Es2126PoEplusRegisterMonitor_Object((1,3,6,1,4,1,2356,800,2,2129,1,2,5),_Es2126PoEplusRegisterMonitor_Type())
es2126PoEplusRegisterMonitor.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusRegisterMonitor.setStatus(_A)
_Es2126PoEplusDeleteMonitor_Type=DisplayString
_Es2126PoEplusDeleteMonitor_Object=MibScalar
es2126PoEplusDeleteMonitor=_Es2126PoEplusDeleteMonitor_Object((1,3,6,1,4,1,2356,800,2,2129,1,2,6),_Es2126PoEplusDeleteMonitor_Type())
es2126PoEplusDeleteMonitor.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDeleteMonitor.setStatus(_A)
_Es2126PoEplusMonitorTable_Object=MibTable
es2126PoEplusMonitorTable=_Es2126PoEplusMonitorTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,2,7))
if mibBuilder.loadTexts:es2126PoEplusMonitorTable.setStatus(_A)
_Es2126PoEplusMonitorEntry_Object=MibTableRow
es2126PoEplusMonitorEntry=_Es2126PoEplusMonitorEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,2,7,1))
es2126PoEplusMonitorEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:es2126PoEplusMonitorEntry.setStatus(_A)
_Es2126PoEplusMonitorTableIp_Type=IpAddress
_Es2126PoEplusMonitorTableIp_Object=MibTableColumn
es2126PoEplusMonitorTableIp=_Es2126PoEplusMonitorTableIp_Object((1,3,6,1,4,1,2356,800,2,2129,1,2,7,1,1),_Es2126PoEplusMonitorTableIp_Type())
es2126PoEplusMonitorTableIp.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusMonitorTableIp.setStatus(_A)
_Es2126PoEplusMonitorTableMac_Type=DisplayString
_Es2126PoEplusMonitorTableMac_Object=MibTableColumn
es2126PoEplusMonitorTableMac=_Es2126PoEplusMonitorTableMac_Object((1,3,6,1,4,1,2356,800,2,2129,1,2,7,1,2),_Es2126PoEplusMonitorTableMac_Type())
es2126PoEplusMonitorTableMac.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusMonitorTableMac.setStatus(_A)
class _Es2126PoEplusTrapBootDelayTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_Es2126PoEplusTrapBootDelayTime_Type.__name__=_B
_Es2126PoEplusTrapBootDelayTime_Object=MibScalar
es2126PoEplusTrapBootDelayTime=_Es2126PoEplusTrapBootDelayTime_Object((1,3,6,1,4,1,2356,800,2,2129,1,2,8),_Es2126PoEplusTrapBootDelayTime_Type())
es2126PoEplusTrapBootDelayTime.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusTrapBootDelayTime.setStatus(_A)
_Es2126PoEplusAlarm_ObjectIdentity=ObjectIdentity
es2126PoEplusAlarm=_Es2126PoEplusAlarm_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,3))
_Es2126PoEplusEvent_ObjectIdentity=ObjectIdentity
es2126PoEplusEvent=_Es2126PoEplusEvent_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,3,1))
class _Es2126PoEplusEventNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Es2126PoEplusEventNumber_Type.__name__=_B
_Es2126PoEplusEventNumber_Object=MibScalar
es2126PoEplusEventNumber=_Es2126PoEplusEventNumber_Object((1,3,6,1,4,1,2356,800,2,2129,1,3,1,1),_Es2126PoEplusEventNumber_Type())
es2126PoEplusEventNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusEventNumber.setStatus(_A)
_Es2126PoEplusEventTable_Object=MibTable
es2126PoEplusEventTable=_Es2126PoEplusEventTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,3,1,2))
if mibBuilder.loadTexts:es2126PoEplusEventTable.setStatus(_A)
_Es2126PoEplusEventEntry_Object=MibTableRow
es2126PoEplusEventEntry=_Es2126PoEplusEventEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,3,1,2,1))
es2126PoEplusEventEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:es2126PoEplusEventEntry.setStatus(_A)
class _Es2126PoEplusEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Es2126PoEplusEventIndex_Type.__name__=_B
_Es2126PoEplusEventIndex_Object=MibTableColumn
es2126PoEplusEventIndex=_Es2126PoEplusEventIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,3,1,2,1,1),_Es2126PoEplusEventIndex_Type())
es2126PoEplusEventIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusEventIndex.setStatus(_A)
_Es2126PoEplusEventName_Type=DisplayString
_Es2126PoEplusEventName_Object=MibTableColumn
es2126PoEplusEventName=_Es2126PoEplusEventName_Object((1,3,6,1,4,1,2356,800,2,2129,1,3,1,2,1,2),_Es2126PoEplusEventName_Type())
es2126PoEplusEventName.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusEventName.setStatus(_A)
class _Es2126PoEplusEventSendEmail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusEventSendEmail_Type.__name__=_B
_Es2126PoEplusEventSendEmail_Object=MibTableColumn
es2126PoEplusEventSendEmail=_Es2126PoEplusEventSendEmail_Object((1,3,6,1,4,1,2356,800,2,2129,1,3,1,2,1,3),_Es2126PoEplusEventSendEmail_Type())
es2126PoEplusEventSendEmail.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusEventSendEmail.setStatus(_A)
class _Es2126PoEplusEventSendTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusEventSendTrap_Type.__name__=_B
_Es2126PoEplusEventSendTrap_Object=MibTableColumn
es2126PoEplusEventSendTrap=_Es2126PoEplusEventSendTrap_Object((1,3,6,1,4,1,2356,800,2,2129,1,3,1,2,1,4),_Es2126PoEplusEventSendTrap_Type())
es2126PoEplusEventSendTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusEventSendTrap.setStatus(_A)
_Es2126PoEplusEmail_ObjectIdentity=ObjectIdentity
es2126PoEplusEmail=_Es2126PoEplusEmail_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,3,2))
_Es2126PoEplusEmailServer_Type=DisplayString
_Es2126PoEplusEmailServer_Object=MibScalar
es2126PoEplusEmailServer=_Es2126PoEplusEmailServer_Object((1,3,6,1,4,1,2356,800,2,2129,1,3,2,1),_Es2126PoEplusEmailServer_Type())
es2126PoEplusEmailServer.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusEmailServer.setStatus(_A)
_Es2126PoEplusEmailUsername_Type=DisplayString
_Es2126PoEplusEmailUsername_Object=MibScalar
es2126PoEplusEmailUsername=_Es2126PoEplusEmailUsername_Object((1,3,6,1,4,1,2356,800,2,2129,1,3,2,2),_Es2126PoEplusEmailUsername_Type())
es2126PoEplusEmailUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusEmailUsername.setStatus(_A)
_Es2126PoEplusEmailPassword_Type=DisplayString
_Es2126PoEplusEmailPassword_Object=MibScalar
es2126PoEplusEmailPassword=_Es2126PoEplusEmailPassword_Object((1,3,6,1,4,1,2356,800,2,2129,1,3,2,3),_Es2126PoEplusEmailPassword_Type())
es2126PoEplusEmailPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusEmailPassword.setStatus(_A)
_Es2126PoEplusEmailSender_Type=DisplayString
_Es2126PoEplusEmailSender_Object=MibScalar
es2126PoEplusEmailSender=_Es2126PoEplusEmailSender_Object((1,3,6,1,4,1,2356,800,2,2129,1,3,2,4),_Es2126PoEplusEmailSender_Type())
es2126PoEplusEmailSender.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusEmailSender.setStatus(_A)
_Es2126PoEplusEmailReturnPath_Type=DisplayString
_Es2126PoEplusEmailReturnPath_Object=MibScalar
es2126PoEplusEmailReturnPath=_Es2126PoEplusEmailReturnPath_Object((1,3,6,1,4,1,2356,800,2,2129,1,3,2,5),_Es2126PoEplusEmailReturnPath_Type())
es2126PoEplusEmailReturnPath.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusEmailReturnPath.setStatus(_A)
class _Es2126PoEplusEmailUserNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_Es2126PoEplusEmailUserNumber_Type.__name__=_B
_Es2126PoEplusEmailUserNumber_Object=MibScalar
es2126PoEplusEmailUserNumber=_Es2126PoEplusEmailUserNumber_Object((1,3,6,1,4,1,2356,800,2,2129,1,3,2,6),_Es2126PoEplusEmailUserNumber_Type())
es2126PoEplusEmailUserNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusEmailUserNumber.setStatus(_A)
_Es2126PoEplusEmailUserTable_Object=MibTable
es2126PoEplusEmailUserTable=_Es2126PoEplusEmailUserTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,3,2,7))
if mibBuilder.loadTexts:es2126PoEplusEmailUserTable.setStatus(_A)
_Es2126PoEplusEmailUserEntry_Object=MibTableRow
es2126PoEplusEmailUserEntry=_Es2126PoEplusEmailUserEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,3,2,7,1))
es2126PoEplusEmailUserEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:es2126PoEplusEmailUserEntry.setStatus(_A)
class _Es2126PoEplusEmailUserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_Es2126PoEplusEmailUserIndex_Type.__name__=_B
_Es2126PoEplusEmailUserIndex_Object=MibTableColumn
es2126PoEplusEmailUserIndex=_Es2126PoEplusEmailUserIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,3,2,7,1,1),_Es2126PoEplusEmailUserIndex_Type())
es2126PoEplusEmailUserIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusEmailUserIndex.setStatus(_A)
_Es2126PoEplusEmailUserAddress_Type=DisplayString
_Es2126PoEplusEmailUserAddress_Object=MibTableColumn
es2126PoEplusEmailUserAddress=_Es2126PoEplusEmailUserAddress_Object((1,3,6,1,4,1,2356,800,2,2129,1,3,2,7,1,2),_Es2126PoEplusEmailUserAddress_Type())
es2126PoEplusEmailUserAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusEmailUserAddress.setStatus(_A)
_Es2126PoEplusTftp_ObjectIdentity=ObjectIdentity
es2126PoEplusTftp=_Es2126PoEplusTftp_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,4))
_Es2126PoEplusRemoteTftpServer_Type=IpAddress
_Es2126PoEplusRemoteTftpServer_Object=MibScalar
es2126PoEplusRemoteTftpServer=_Es2126PoEplusRemoteTftpServer_Object((1,3,6,1,4,1,2356,800,2,2129,1,4,1),_Es2126PoEplusRemoteTftpServer_Type())
es2126PoEplusRemoteTftpServer.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusRemoteTftpServer.setStatus(_A)
class _Es2126PoEplusInternalTftpServerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusInternalTftpServerState_Type.__name__=_B
_Es2126PoEplusInternalTftpServerState_Object=MibScalar
es2126PoEplusInternalTftpServerState=_Es2126PoEplusInternalTftpServerState_Object((1,3,6,1,4,1,2356,800,2,2129,1,4,2),_Es2126PoEplusInternalTftpServerState_Type())
es2126PoEplusInternalTftpServerState.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusInternalTftpServerState.setStatus(_A)
_Es2126PoEplusConfiguration_ObjectIdentity=ObjectIdentity
es2126PoEplusConfiguration=_Es2126PoEplusConfiguration_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,5))
_Es2126PoEplusSaveRestore_ObjectIdentity=ObjectIdentity
es2126PoEplusSaveRestore=_Es2126PoEplusSaveRestore_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,5,1))
class _Es2126PoEplusSaveStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusSaveStart_Type.__name__=_B
_Es2126PoEplusSaveStart_Object=MibScalar
es2126PoEplusSaveStart=_Es2126PoEplusSaveStart_Object((1,3,6,1,4,1,2356,800,2,2129,1,5,1,1),_Es2126PoEplusSaveStart_Type())
es2126PoEplusSaveStart.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusSaveStart.setStatus(_A)
class _Es2126PoEplusSaveUser_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusSaveUser_Type.__name__=_B
_Es2126PoEplusSaveUser_Object=MibScalar
es2126PoEplusSaveUser=_Es2126PoEplusSaveUser_Object((1,3,6,1,4,1,2356,800,2,2129,1,5,1,2),_Es2126PoEplusSaveUser_Type())
es2126PoEplusSaveUser.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusSaveUser.setStatus(_A)
class _Es2126PoEplusRestoreDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_Es2126PoEplusRestoreDefault_Type.__name__=_B
_Es2126PoEplusRestoreDefault_Object=MibScalar
es2126PoEplusRestoreDefault=_Es2126PoEplusRestoreDefault_Object((1,3,6,1,4,1,2356,800,2,2129,1,5,1,3),_Es2126PoEplusRestoreDefault_Type())
es2126PoEplusRestoreDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusRestoreDefault.setStatus(_A)
class _Es2126PoEplusRestoreUser_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusRestoreUser_Type.__name__=_B
_Es2126PoEplusRestoreUser_Object=MibScalar
es2126PoEplusRestoreUser=_Es2126PoEplusRestoreUser_Object((1,3,6,1,4,1,2356,800,2,2129,1,5,1,4),_Es2126PoEplusRestoreUser_Type())
es2126PoEplusRestoreUser.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusRestoreUser.setStatus(_A)
_Es2126PoEplusConfigFile_ObjectIdentity=ObjectIdentity
es2126PoEplusConfigFile=_Es2126PoEplusConfigFile_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,5,2))
_Es2126PoEplusExportConfigName_Type=DisplayString
_Es2126PoEplusExportConfigName_Object=MibScalar
es2126PoEplusExportConfigName=_Es2126PoEplusExportConfigName_Object((1,3,6,1,4,1,2356,800,2,2129,1,5,2,1),_Es2126PoEplusExportConfigName_Type())
es2126PoEplusExportConfigName.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusExportConfigName.setStatus(_A)
class _Es2126PoEplusDoExportConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_Es2126PoEplusDoExportConfig_Type.__name__=_B
_Es2126PoEplusDoExportConfig_Object=MibScalar
es2126PoEplusDoExportConfig=_Es2126PoEplusDoExportConfig_Object((1,3,6,1,4,1,2356,800,2,2129,1,5,2,2),_Es2126PoEplusDoExportConfig_Type())
es2126PoEplusDoExportConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDoExportConfig.setStatus(_A)
_Es2126PoEplusImportConfigName_Type=DisplayString
_Es2126PoEplusImportConfigName_Object=MibScalar
es2126PoEplusImportConfigName=_Es2126PoEplusImportConfigName_Object((1,3,6,1,4,1,2356,800,2,2129,1,5,2,3),_Es2126PoEplusImportConfigName_Type())
es2126PoEplusImportConfigName.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusImportConfigName.setStatus(_A)
class _Es2126PoEplusDoImportConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Es2126PoEplusDoImportConfig_Type.__name__=_B
_Es2126PoEplusDoImportConfig_Object=MibScalar
es2126PoEplusDoImportConfig=_Es2126PoEplusDoImportConfig_Object((1,3,6,1,4,1,2356,800,2,2129,1,5,2,4),_Es2126PoEplusDoImportConfig_Type())
es2126PoEplusDoImportConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDoImportConfig.setStatus(_A)
_Es2126PoEplusDiagnostic_ObjectIdentity=ObjectIdentity
es2126PoEplusDiagnostic=_Es2126PoEplusDiagnostic_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,6))
_Es2126PoEplusEEPROMTest_Type=DisplayString
_Es2126PoEplusEEPROMTest_Object=MibScalar
es2126PoEplusEEPROMTest=_Es2126PoEplusEEPROMTest_Object((1,3,6,1,4,1,2356,800,2,2129,1,6,1),_Es2126PoEplusEEPROMTest_Type())
es2126PoEplusEEPROMTest.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusEEPROMTest.setStatus(_A)
_Es2126PoEplusUartTest_Type=DisplayString
_Es2126PoEplusUartTest_Object=MibScalar
es2126PoEplusUartTest=_Es2126PoEplusUartTest_Object((1,3,6,1,4,1,2356,800,2,2129,1,6,2),_Es2126PoEplusUartTest_Type())
es2126PoEplusUartTest.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusUartTest.setStatus(_A)
_Es2126PoEplusDramTest_Type=DisplayString
_Es2126PoEplusDramTest_Object=MibScalar
es2126PoEplusDramTest=_Es2126PoEplusDramTest_Object((1,3,6,1,4,1,2356,800,2,2129,1,6,3),_Es2126PoEplusDramTest_Type())
es2126PoEplusDramTest.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusDramTest.setStatus(_A)
_Es2126PoEplusFlashTest_Type=DisplayString
_Es2126PoEplusFlashTest_Object=MibScalar
es2126PoEplusFlashTest=_Es2126PoEplusFlashTest_Object((1,3,6,1,4,1,2356,800,2,2129,1,6,4),_Es2126PoEplusFlashTest_Type())
es2126PoEplusFlashTest.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusFlashTest.setStatus(_A)
_Es2126PoEplusInternalLoopbackTest_Type=DisplayString
_Es2126PoEplusInternalLoopbackTest_Object=MibScalar
es2126PoEplusInternalLoopbackTest=_Es2126PoEplusInternalLoopbackTest_Object((1,3,6,1,4,1,2356,800,2,2129,1,6,5),_Es2126PoEplusInternalLoopbackTest_Type())
es2126PoEplusInternalLoopbackTest.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusInternalLoopbackTest.setStatus(_A)
_Es2126PoEplusExternalLoopbackTest_Type=DisplayString
_Es2126PoEplusExternalLoopbackTest_Object=MibScalar
es2126PoEplusExternalLoopbackTest=_Es2126PoEplusExternalLoopbackTest_Object((1,3,6,1,4,1,2356,800,2,2129,1,6,6),_Es2126PoEplusExternalLoopbackTest_Type())
es2126PoEplusExternalLoopbackTest.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusExternalLoopbackTest.setStatus(_A)
_Es2126PoEplusPingTest_Type=DisplayString
_Es2126PoEplusPingTest_Object=MibScalar
es2126PoEplusPingTest=_Es2126PoEplusPingTest_Object((1,3,6,1,4,1,2356,800,2,2129,1,6,7),_Es2126PoEplusPingTest_Type())
es2126PoEplusPingTest.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusPingTest.setStatus(_A)
_Es2126PoEplusLog_ObjectIdentity=ObjectIdentity
es2126PoEplusLog=_Es2126PoEplusLog_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,7))
class _Es2126PoEplusClearLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusClearLog_Type.__name__=_B
_Es2126PoEplusClearLog_Object=MibScalar
es2126PoEplusClearLog=_Es2126PoEplusClearLog_Object((1,3,6,1,4,1,2356,800,2,2129,1,7,1),_Es2126PoEplusClearLog_Type())
es2126PoEplusClearLog.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusClearLog.setStatus(_A)
class _Es2126PoEplusUploadLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusUploadLog_Type.__name__=_B
_Es2126PoEplusUploadLog_Object=MibScalar
es2126PoEplusUploadLog=_Es2126PoEplusUploadLog_Object((1,3,6,1,4,1,2356,800,2,2129,1,7,2),_Es2126PoEplusUploadLog_Type())
es2126PoEplusUploadLog.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusUploadLog.setStatus(_A)
class _Es2126PoEplusAutoUploadLogState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusAutoUploadLogState_Type.__name__=_B
_Es2126PoEplusAutoUploadLogState_Object=MibScalar
es2126PoEplusAutoUploadLogState=_Es2126PoEplusAutoUploadLogState_Object((1,3,6,1,4,1,2356,800,2,2129,1,7,3),_Es2126PoEplusAutoUploadLogState_Type())
es2126PoEplusAutoUploadLogState.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusAutoUploadLogState.setStatus(_A)
class _Es2126PoEplusLogNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_Es2126PoEplusLogNumber_Type.__name__=_B
_Es2126PoEplusLogNumber_Object=MibScalar
es2126PoEplusLogNumber=_Es2126PoEplusLogNumber_Object((1,3,6,1,4,1,2356,800,2,2129,1,7,4),_Es2126PoEplusLogNumber_Type())
es2126PoEplusLogNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusLogNumber.setStatus(_A)
_Es2126PoEplusLogTable_Object=MibTable
es2126PoEplusLogTable=_Es2126PoEplusLogTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,7,5))
if mibBuilder.loadTexts:es2126PoEplusLogTable.setStatus(_A)
_Es2126PoEplusLogEntry_Object=MibTableRow
es2126PoEplusLogEntry=_Es2126PoEplusLogEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,7,5,1))
es2126PoEplusLogEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:es2126PoEplusLogEntry.setStatus(_A)
class _Es2126PoEplusLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_Es2126PoEplusLogIndex_Type.__name__=_B
_Es2126PoEplusLogIndex_Object=MibTableColumn
es2126PoEplusLogIndex=_Es2126PoEplusLogIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,7,5,1,1),_Es2126PoEplusLogIndex_Type())
es2126PoEplusLogIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusLogIndex.setStatus(_A)
_Es2126PoEplusLogEvent_Type=DisplayString
_Es2126PoEplusLogEvent_Object=MibTableColumn
es2126PoEplusLogEvent=_Es2126PoEplusLogEvent_Object((1,3,6,1,4,1,2356,800,2,2129,1,7,5,1,2),_Es2126PoEplusLogEvent_Type())
es2126PoEplusLogEvent.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusLogEvent.setStatus(_A)
_Es2126PoEplusFirmware_ObjectIdentity=ObjectIdentity
es2126PoEplusFirmware=_Es2126PoEplusFirmware_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,8))
_Es2126PoEplusFirmwareFileName_Type=DisplayString
_Es2126PoEplusFirmwareFileName_Object=MibScalar
es2126PoEplusFirmwareFileName=_Es2126PoEplusFirmwareFileName_Object((1,3,6,1,4,1,2356,800,2,2129,1,8,1),_Es2126PoEplusFirmwareFileName_Type())
es2126PoEplusFirmwareFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusFirmwareFileName.setStatus(_A)
class _Es2126PoEplusDoFirmwareUpgrade_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusDoFirmwareUpgrade_Type.__name__=_B
_Es2126PoEplusDoFirmwareUpgrade_Object=MibScalar
es2126PoEplusDoFirmwareUpgrade=_Es2126PoEplusDoFirmwareUpgrade_Object((1,3,6,1,4,1,2356,800,2,2129,1,8,2),_Es2126PoEplusDoFirmwareUpgrade_Type())
es2126PoEplusDoFirmwareUpgrade.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDoFirmwareUpgrade.setStatus(_A)
_Es2126PoEplusPort_ObjectIdentity=ObjectIdentity
es2126PoEplusPort=_Es2126PoEplusPort_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,9))
_Es2126PoEplusPortStatus_ObjectIdentity=ObjectIdentity
es2126PoEplusPortStatus=_Es2126PoEplusPortStatus_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,9,1))
class _Es2126PoEplusPortStatusNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Es2126PoEplusPortStatusNumber_Type.__name__=_B
_Es2126PoEplusPortStatusNumber_Object=MibScalar
es2126PoEplusPortStatusNumber=_Es2126PoEplusPortStatusNumber_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,1,1),_Es2126PoEplusPortStatusNumber_Type())
es2126PoEplusPortStatusNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortStatusNumber.setStatus(_A)
_Es2126PoEplusPortStatusTable_Object=MibTable
es2126PoEplusPortStatusTable=_Es2126PoEplusPortStatusTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,1,2))
if mibBuilder.loadTexts:es2126PoEplusPortStatusTable.setStatus(_A)
_Es2126PoEplusPortStatusEntry_Object=MibTableRow
es2126PoEplusPortStatusEntry=_Es2126PoEplusPortStatusEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,1,2,1))
es2126PoEplusPortStatusEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:es2126PoEplusPortStatusEntry.setStatus(_A)
class _Es2126PoEplusPortStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Es2126PoEplusPortStatusIndex_Type.__name__=_B
_Es2126PoEplusPortStatusIndex_Object=MibTableColumn
es2126PoEplusPortStatusIndex=_Es2126PoEplusPortStatusIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,1,2,1,1),_Es2126PoEplusPortStatusIndex_Type())
es2126PoEplusPortStatusIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortStatusIndex.setStatus(_A)
_Es2126PoEplusPortStatusMedia_Type=DisplayString
_Es2126PoEplusPortStatusMedia_Object=MibTableColumn
es2126PoEplusPortStatusMedia=_Es2126PoEplusPortStatusMedia_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,1,2,1,2),_Es2126PoEplusPortStatusMedia_Type())
es2126PoEplusPortStatusMedia.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortStatusMedia.setStatus(_A)
_Es2126PoEplusPortStatusLink_Type=DisplayString
_Es2126PoEplusPortStatusLink_Object=MibTableColumn
es2126PoEplusPortStatusLink=_Es2126PoEplusPortStatusLink_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,1,2,1,3),_Es2126PoEplusPortStatusLink_Type())
es2126PoEplusPortStatusLink.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortStatusLink.setStatus(_A)
_Es2126PoEplusPortStatusPortState_Type=DisplayString
_Es2126PoEplusPortStatusPortState_Object=MibTableColumn
es2126PoEplusPortStatusPortState=_Es2126PoEplusPortStatusPortState_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,1,2,1,4),_Es2126PoEplusPortStatusPortState_Type())
es2126PoEplusPortStatusPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortStatusPortState.setStatus(_A)
_Es2126PoEplusPortStatusAutoNego_Type=DisplayString
_Es2126PoEplusPortStatusAutoNego_Object=MibTableColumn
es2126PoEplusPortStatusAutoNego=_Es2126PoEplusPortStatusAutoNego_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,1,2,1,5),_Es2126PoEplusPortStatusAutoNego_Type())
es2126PoEplusPortStatusAutoNego.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortStatusAutoNego.setStatus(_A)
_Es2126PoEplusPortStatusSpdDpx_Type=DisplayString
_Es2126PoEplusPortStatusSpdDpx_Object=MibTableColumn
es2126PoEplusPortStatusSpdDpx=_Es2126PoEplusPortStatusSpdDpx_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,1,2,1,6),_Es2126PoEplusPortStatusSpdDpx_Type())
es2126PoEplusPortStatusSpdDpx.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortStatusSpdDpx.setStatus(_A)
_Es2126PoEplusPortStatusRxPause_Type=DisplayString
_Es2126PoEplusPortStatusRxPause_Object=MibTableColumn
es2126PoEplusPortStatusRxPause=_Es2126PoEplusPortStatusRxPause_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,1,2,1,7),_Es2126PoEplusPortStatusRxPause_Type())
es2126PoEplusPortStatusRxPause.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortStatusRxPause.setStatus(_A)
_Es2126PoEplusPortStatusTxPause_Type=DisplayString
_Es2126PoEplusPortStatusTxPause_Object=MibTableColumn
es2126PoEplusPortStatusTxPause=_Es2126PoEplusPortStatusTxPause_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,1,2,1,8),_Es2126PoEplusPortStatusTxPause_Type())
es2126PoEplusPortStatusTxPause.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortStatusTxPause.setStatus(_A)
_Es2126PoEplusPortStatusDescription_Type=DisplayString
_Es2126PoEplusPortStatusDescription_Object=MibTableColumn
es2126PoEplusPortStatusDescription=_Es2126PoEplusPortStatusDescription_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,1,2,1,9),_Es2126PoEplusPortStatusDescription_Type())
es2126PoEplusPortStatusDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortStatusDescription.setStatus(_A)
_Es2126PoEplusPortConf_ObjectIdentity=ObjectIdentity
es2126PoEplusPortConf=_Es2126PoEplusPortConf_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,9,2))
class _Es2126PoEplusPortConfNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Es2126PoEplusPortConfNumber_Type.__name__=_B
_Es2126PoEplusPortConfNumber_Object=MibScalar
es2126PoEplusPortConfNumber=_Es2126PoEplusPortConfNumber_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,2,1),_Es2126PoEplusPortConfNumber_Type())
es2126PoEplusPortConfNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortConfNumber.setStatus(_A)
_Es2126PoEplusPortConfTable_Object=MibTable
es2126PoEplusPortConfTable=_Es2126PoEplusPortConfTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,2,2))
if mibBuilder.loadTexts:es2126PoEplusPortConfTable.setStatus(_A)
_Es2126PoEplusPortConfEntry_Object=MibTableRow
es2126PoEplusPortConfEntry=_Es2126PoEplusPortConfEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,2,2,1))
es2126PoEplusPortConfEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:es2126PoEplusPortConfEntry.setStatus(_A)
class _Es2126PoEplusPortConfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Es2126PoEplusPortConfIndex_Type.__name__=_B
_Es2126PoEplusPortConfIndex_Object=MibTableColumn
es2126PoEplusPortConfIndex=_Es2126PoEplusPortConfIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,2,2,1,1),_Es2126PoEplusPortConfIndex_Type())
es2126PoEplusPortConfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortConfIndex.setStatus(_A)
class _Es2126PoEplusPortConfPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusPortConfPortState_Type.__name__=_B
_Es2126PoEplusPortConfPortState_Object=MibTableColumn
es2126PoEplusPortConfPortState=_Es2126PoEplusPortConfPortState_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,2,2,1,2),_Es2126PoEplusPortConfPortState_Type())
es2126PoEplusPortConfPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusPortConfPortState.setStatus(_A)
class _Es2126PoEplusPortConfSpdDpx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_Es2126PoEplusPortConfSpdDpx_Type.__name__=_B
_Es2126PoEplusPortConfSpdDpx_Object=MibTableColumn
es2126PoEplusPortConfSpdDpx=_Es2126PoEplusPortConfSpdDpx_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,2,2,1,3),_Es2126PoEplusPortConfSpdDpx_Type())
es2126PoEplusPortConfSpdDpx.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusPortConfSpdDpx.setStatus(_A)
class _Es2126PoEplusPortConfFlwCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusPortConfFlwCtrl_Type.__name__=_B
_Es2126PoEplusPortConfFlwCtrl_Object=MibTableColumn
es2126PoEplusPortConfFlwCtrl=_Es2126PoEplusPortConfFlwCtrl_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,2,2,1,4),_Es2126PoEplusPortConfFlwCtrl_Type())
es2126PoEplusPortConfFlwCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusPortConfFlwCtrl.setStatus(_A)
_Es2126PoEplusPortConfDescription_Type=DisplayString
_Es2126PoEplusPortConfDescription_Object=MibTableColumn
es2126PoEplusPortConfDescription=_Es2126PoEplusPortConfDescription_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,2,2,1,5),_Es2126PoEplusPortConfDescription_Type())
es2126PoEplusPortConfDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusPortConfDescription.setStatus(_A)
_Es2126PoEplusPortBandwidth_ObjectIdentity=ObjectIdentity
es2126PoEplusPortBandwidth=_Es2126PoEplusPortBandwidth_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,9,3))
_Es2126PoEplusPortBandwidthTable_Object=MibTable
es2126PoEplusPortBandwidthTable=_Es2126PoEplusPortBandwidthTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,3,1))
if mibBuilder.loadTexts:es2126PoEplusPortBandwidthTable.setStatus(_A)
_Es2126PoEplusPortBandwidthEntry_Object=MibTableRow
es2126PoEplusPortBandwidthEntry=_Es2126PoEplusPortBandwidthEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,3,1,1))
es2126PoEplusPortBandwidthEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:es2126PoEplusPortBandwidthEntry.setStatus(_A)
class _Es2126PoEplusPortBandwidthIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_Es2126PoEplusPortBandwidthIndex_Type.__name__=_B
_Es2126PoEplusPortBandwidthIndex_Object=MibTableColumn
es2126PoEplusPortBandwidthIndex=_Es2126PoEplusPortBandwidthIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,3,1,1,1),_Es2126PoEplusPortBandwidthIndex_Type())
es2126PoEplusPortBandwidthIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortBandwidthIndex.setStatus(_A)
class _Es2126PoEplusPortBandwidthIngressRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(66,1024000))
_Es2126PoEplusPortBandwidthIngressRate_Type.__name__=_B
_Es2126PoEplusPortBandwidthIngressRate_Object=MibTableColumn
es2126PoEplusPortBandwidthIngressRate=_Es2126PoEplusPortBandwidthIngressRate_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,3,1,1,2),_Es2126PoEplusPortBandwidthIngressRate_Type())
es2126PoEplusPortBandwidthIngressRate.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusPortBandwidthIngressRate.setStatus(_A)
class _Es2126PoEplusPortBandwidthEgressRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(66,1024000))
_Es2126PoEplusPortBandwidthEgressRate_Type.__name__=_B
_Es2126PoEplusPortBandwidthEgressRate_Object=MibTableColumn
es2126PoEplusPortBandwidthEgressRate=_Es2126PoEplusPortBandwidthEgressRate_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,3,1,1,3),_Es2126PoEplusPortBandwidthEgressRate_Type())
es2126PoEplusPortBandwidthEgressRate.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusPortBandwidthEgressRate.setStatus(_A)
class _Es2126PoEplusPortBandwidthStormType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_Es2126PoEplusPortBandwidthStormType_Type.__name__=_B
_Es2126PoEplusPortBandwidthStormType_Object=MibScalar
es2126PoEplusPortBandwidthStormType=_Es2126PoEplusPortBandwidthStormType_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,3,2),_Es2126PoEplusPortBandwidthStormType_Type())
es2126PoEplusPortBandwidthStormType.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusPortBandwidthStormType.setStatus(_A)
class _Es2126PoEplusPortBandwidthStormRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_Es2126PoEplusPortBandwidthStormRate_Type.__name__=_B
_Es2126PoEplusPortBandwidthStormRate_Object=MibScalar
es2126PoEplusPortBandwidthStormRate=_Es2126PoEplusPortBandwidthStormRate_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,3,3),_Es2126PoEplusPortBandwidthStormRate_Type())
es2126PoEplusPortBandwidthStormRate.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusPortBandwidthStormRate.setStatus(_A)
_Es2126PoEplusPortSFPInfo_ObjectIdentity=ObjectIdentity
es2126PoEplusPortSFPInfo=_Es2126PoEplusPortSFPInfo_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,9,4))
class _Es2126PoEplusPortSFPInfoNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Es2126PoEplusPortSFPInfoNumber_Type.__name__=_B
_Es2126PoEplusPortSFPInfoNumber_Object=MibScalar
es2126PoEplusPortSFPInfoNumber=_Es2126PoEplusPortSFPInfoNumber_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,4,1),_Es2126PoEplusPortSFPInfoNumber_Type())
es2126PoEplusPortSFPInfoNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortSFPInfoNumber.setStatus(_A)
_Es2126PoEplusPortSFPInfoTable_Object=MibTable
es2126PoEplusPortSFPInfoTable=_Es2126PoEplusPortSFPInfoTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,4,2))
if mibBuilder.loadTexts:es2126PoEplusPortSFPInfoTable.setStatus(_A)
_Es2126PoEplusPortSFPInfoEntry_Object=MibTableRow
es2126PoEplusPortSFPInfoEntry=_Es2126PoEplusPortSFPInfoEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,4,2,1))
es2126PoEplusPortSFPInfoEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:es2126PoEplusPortSFPInfoEntry.setStatus(_A)
class _Es2126PoEplusPortSFPInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Es2126PoEplusPortSFPInfoIndex_Type.__name__=_B
_Es2126PoEplusPortSFPInfoIndex_Object=MibTableColumn
es2126PoEplusPortSFPInfoIndex=_Es2126PoEplusPortSFPInfoIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,4,2,1,1),_Es2126PoEplusPortSFPInfoIndex_Type())
es2126PoEplusPortSFPInfoIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortSFPInfoIndex.setStatus(_A)
_Es2126PoEplusPortSFPConnectorType_Type=DisplayString
_Es2126PoEplusPortSFPConnectorType_Object=MibTableColumn
es2126PoEplusPortSFPConnectorType=_Es2126PoEplusPortSFPConnectorType_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,4,2,1,2),_Es2126PoEplusPortSFPConnectorType_Type())
es2126PoEplusPortSFPConnectorType.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortSFPConnectorType.setStatus(_A)
_Es2126PoEplusPortSFPFiberType_Type=DisplayString
_Es2126PoEplusPortSFPFiberType_Object=MibTableColumn
es2126PoEplusPortSFPFiberType=_Es2126PoEplusPortSFPFiberType_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,4,2,1,3),_Es2126PoEplusPortSFPFiberType_Type())
es2126PoEplusPortSFPFiberType.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortSFPFiberType.setStatus(_A)
_Es2126PoEplusPortSFPWavelength_Type=DisplayString
_Es2126PoEplusPortSFPWavelength_Object=MibTableColumn
es2126PoEplusPortSFPWavelength=_Es2126PoEplusPortSFPWavelength_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,4,2,1,4),_Es2126PoEplusPortSFPWavelength_Type())
es2126PoEplusPortSFPWavelength.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortSFPWavelength.setStatus(_A)
_Es2126PoEplusPortSFPBaudRate_Type=DisplayString
_Es2126PoEplusPortSFPBaudRate_Object=MibTableColumn
es2126PoEplusPortSFPBaudRate=_Es2126PoEplusPortSFPBaudRate_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,4,2,1,5),_Es2126PoEplusPortSFPBaudRate_Type())
es2126PoEplusPortSFPBaudRate.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortSFPBaudRate.setStatus(_A)
_Es2126PoEplusPortSFPVendorOUI_Type=DisplayString
_Es2126PoEplusPortSFPVendorOUI_Object=MibTableColumn
es2126PoEplusPortSFPVendorOUI=_Es2126PoEplusPortSFPVendorOUI_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,4,2,1,6),_Es2126PoEplusPortSFPVendorOUI_Type())
es2126PoEplusPortSFPVendorOUI.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortSFPVendorOUI.setStatus(_A)
_Es2126PoEplusPortSFPVendorName_Type=DisplayString
_Es2126PoEplusPortSFPVendorName_Object=MibTableColumn
es2126PoEplusPortSFPVendorName=_Es2126PoEplusPortSFPVendorName_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,4,2,1,7),_Es2126PoEplusPortSFPVendorName_Type())
es2126PoEplusPortSFPVendorName.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortSFPVendorName.setStatus(_A)
_Es2126PoEplusPortSFPVendorPN_Type=DisplayString
_Es2126PoEplusPortSFPVendorPN_Object=MibTableColumn
es2126PoEplusPortSFPVendorPN=_Es2126PoEplusPortSFPVendorPN_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,4,2,1,8),_Es2126PoEplusPortSFPVendorPN_Type())
es2126PoEplusPortSFPVendorPN.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortSFPVendorPN.setStatus(_A)
_Es2126PoEplusPortSFPVendorRev_Type=DisplayString
_Es2126PoEplusPortSFPVendorRev_Object=MibTableColumn
es2126PoEplusPortSFPVendorRev=_Es2126PoEplusPortSFPVendorRev_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,4,2,1,9),_Es2126PoEplusPortSFPVendorRev_Type())
es2126PoEplusPortSFPVendorRev.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortSFPVendorRev.setStatus(_A)
_Es2126PoEplusPortSFPVendorSN_Type=DisplayString
_Es2126PoEplusPortSFPVendorSN_Object=MibTableColumn
es2126PoEplusPortSFPVendorSN=_Es2126PoEplusPortSFPVendorSN_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,4,2,1,10),_Es2126PoEplusPortSFPVendorSN_Type())
es2126PoEplusPortSFPVendorSN.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortSFPVendorSN.setStatus(_A)
_Es2126PoEplusPortSFPDateCode_Type=DisplayString
_Es2126PoEplusPortSFPDateCode_Object=MibTableColumn
es2126PoEplusPortSFPDateCode=_Es2126PoEplusPortSFPDateCode_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,4,2,1,11),_Es2126PoEplusPortSFPDateCode_Type())
es2126PoEplusPortSFPDateCode.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortSFPDateCode.setStatus(_A)
_Es2126PoEplusPortSFPTemperature_Type=DisplayString
_Es2126PoEplusPortSFPTemperature_Object=MibTableColumn
es2126PoEplusPortSFPTemperature=_Es2126PoEplusPortSFPTemperature_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,4,2,1,12),_Es2126PoEplusPortSFPTemperature_Type())
es2126PoEplusPortSFPTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortSFPTemperature.setStatus(_A)
_Es2126PoEplusPortSFPVcc_Type=DisplayString
_Es2126PoEplusPortSFPVcc_Object=MibTableColumn
es2126PoEplusPortSFPVcc=_Es2126PoEplusPortSFPVcc_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,4,2,1,13),_Es2126PoEplusPortSFPVcc_Type())
es2126PoEplusPortSFPVcc.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortSFPVcc.setStatus(_A)
_Es2126PoEplusPortSFPTxBias_Type=DisplayString
_Es2126PoEplusPortSFPTxBias_Object=MibTableColumn
es2126PoEplusPortSFPTxBias=_Es2126PoEplusPortSFPTxBias_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,4,2,1,14),_Es2126PoEplusPortSFPTxBias_Type())
es2126PoEplusPortSFPTxBias.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortSFPTxBias.setStatus(_A)
_Es2126PoEplusPortSFPTxPWR_Type=DisplayString
_Es2126PoEplusPortSFPTxPWR_Object=MibTableColumn
es2126PoEplusPortSFPTxPWR=_Es2126PoEplusPortSFPTxPWR_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,4,2,1,15),_Es2126PoEplusPortSFPTxPWR_Type())
es2126PoEplusPortSFPTxPWR.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortSFPTxPWR.setStatus(_A)
_Es2126PoEplusPortSFPRxPWR_Type=DisplayString
_Es2126PoEplusPortSFPRxPWR_Object=MibTableColumn
es2126PoEplusPortSFPRxPWR=_Es2126PoEplusPortSFPRxPWR_Object((1,3,6,1,4,1,2356,800,2,2129,1,9,4,2,1,16),_Es2126PoEplusPortSFPRxPWR_Type())
es2126PoEplusPortSFPRxPWR.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortSFPRxPWR.setStatus(_A)
_Es2126PoEplusLoopDetectedConf_ObjectIdentity=ObjectIdentity
es2126PoEplusLoopDetectedConf=_Es2126PoEplusLoopDetectedConf_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,10))
class _Es2126PoEplusLoopDetectedNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Es2126PoEplusLoopDetectedNumber_Type.__name__=_B
_Es2126PoEplusLoopDetectedNumber_Object=MibScalar
es2126PoEplusLoopDetectedNumber=_Es2126PoEplusLoopDetectedNumber_Object((1,3,6,1,4,1,2356,800,2,2129,1,10,1),_Es2126PoEplusLoopDetectedNumber_Type())
es2126PoEplusLoopDetectedNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusLoopDetectedNumber.setStatus(_A)
_Es2126PoEplusLoopDetectedTable_Object=MibTable
es2126PoEplusLoopDetectedTable=_Es2126PoEplusLoopDetectedTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,10,2))
if mibBuilder.loadTexts:es2126PoEplusLoopDetectedTable.setStatus(_A)
_Es2126PoEplusLoopDetectedEntry_Object=MibTableRow
es2126PoEplusLoopDetectedEntry=_Es2126PoEplusLoopDetectedEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,10,2,1))
es2126PoEplusLoopDetectedEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:es2126PoEplusLoopDetectedEntry.setStatus(_A)
class _Es2126PoEplusLoopDetectedfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Es2126PoEplusLoopDetectedfIndex_Type.__name__=_B
_Es2126PoEplusLoopDetectedfIndex_Object=MibTableColumn
es2126PoEplusLoopDetectedfIndex=_Es2126PoEplusLoopDetectedfIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,10,2,1,1),_Es2126PoEplusLoopDetectedfIndex_Type())
es2126PoEplusLoopDetectedfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusLoopDetectedfIndex.setStatus(_A)
class _Es2126PoEplusLoopDetectedStateEbl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusLoopDetectedStateEbl_Type.__name__=_B
_Es2126PoEplusLoopDetectedStateEbl_Object=MibTableColumn
es2126PoEplusLoopDetectedStateEbl=_Es2126PoEplusLoopDetectedStateEbl_Object((1,3,6,1,4,1,2356,800,2,2129,1,10,2,1,2),_Es2126PoEplusLoopDetectedStateEbl_Type())
es2126PoEplusLoopDetectedStateEbl.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusLoopDetectedStateEbl.setStatus(_A)
class _Es2126PoEplusLoopDetectedCurrentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusLoopDetectedCurrentStatus_Type.__name__=_B
_Es2126PoEplusLoopDetectedCurrentStatus_Object=MibTableColumn
es2126PoEplusLoopDetectedCurrentStatus=_Es2126PoEplusLoopDetectedCurrentStatus_Object((1,3,6,1,4,1,2356,800,2,2129,1,10,2,1,3),_Es2126PoEplusLoopDetectedCurrentStatus_Type())
es2126PoEplusLoopDetectedCurrentStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusLoopDetectedCurrentStatus.setStatus(_A)
class _Es2126PoEplusLoopDetectedResumed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusLoopDetectedResumed_Type.__name__=_B
_Es2126PoEplusLoopDetectedResumed_Object=MibTableColumn
es2126PoEplusLoopDetectedResumed=_Es2126PoEplusLoopDetectedResumed_Object((1,3,6,1,4,1,2356,800,2,2129,1,10,2,1,4),_Es2126PoEplusLoopDetectedResumed_Type())
es2126PoEplusLoopDetectedResumed.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusLoopDetectedResumed.setStatus(_A)
class _Es2126PoEplusLoopDetectedAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusLoopDetectedAction_Type.__name__=_B
_Es2126PoEplusLoopDetectedAction_Object=MibScalar
es2126PoEplusLoopDetectedAction=_Es2126PoEplusLoopDetectedAction_Object((1,3,6,1,4,1,2356,800,2,2129,1,10,3),_Es2126PoEplusLoopDetectedAction_Type())
es2126PoEplusLoopDetectedAction.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusLoopDetectedAction.setStatus(_A)
_Es2126PoEplusMacTableInfo_ObjectIdentity=ObjectIdentity
es2126PoEplusMacTableInfo=_Es2126PoEplusMacTableInfo_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,11))
_Es2126PoEplusMacTableMaintenance_ObjectIdentity=ObjectIdentity
es2126PoEplusMacTableMaintenance=_Es2126PoEplusMacTableMaintenance_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,11,1))
class _Es2126PoEplusMacTableAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(10,1000000))
_Es2126PoEplusMacTableAgingTime_Type.__name__=_B
_Es2126PoEplusMacTableAgingTime_Object=MibScalar
es2126PoEplusMacTableAgingTime=_Es2126PoEplusMacTableAgingTime_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,1,1),_Es2126PoEplusMacTableAgingTime_Type())
es2126PoEplusMacTableAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusMacTableAgingTime.setStatus(_A)
class _Es2126PoEplusMacTableFlush_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusMacTableFlush_Type.__name__=_B
_Es2126PoEplusMacTableFlush_Object=MibScalar
es2126PoEplusMacTableFlush=_Es2126PoEplusMacTableFlush_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,1,2),_Es2126PoEplusMacTableFlush_Type())
es2126PoEplusMacTableFlush.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusMacTableFlush.setStatus(_A)
_Es2126PoEplusMacTableLearnPortLimitTable_Object=MibTable
es2126PoEplusMacTableLearnPortLimitTable=_Es2126PoEplusMacTableLearnPortLimitTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,1,3))
if mibBuilder.loadTexts:es2126PoEplusMacTableLearnPortLimitTable.setStatus(_A)
_Es2126PoEplusMacTableLearnPortLimitEntry_Object=MibTableRow
es2126PoEplusMacTableLearnPortLimitEntry=_Es2126PoEplusMacTableLearnPortLimitEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,1,3,1))
es2126PoEplusMacTableLearnPortLimitEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:es2126PoEplusMacTableLearnPortLimitEntry.setStatus(_A)
class _Es2126PoEplusMacTableLearnPortLimitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_Es2126PoEplusMacTableLearnPortLimitIndex_Type.__name__=_B
_Es2126PoEplusMacTableLearnPortLimitIndex_Object=MibTableColumn
es2126PoEplusMacTableLearnPortLimitIndex=_Es2126PoEplusMacTableLearnPortLimitIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,1,3,1,1),_Es2126PoEplusMacTableLearnPortLimitIndex_Type())
es2126PoEplusMacTableLearnPortLimitIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:es2126PoEplusMacTableLearnPortLimitIndex.setStatus(_A)
class _Es2126PoEplusMacTableLearnPortLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8191))
_Es2126PoEplusMacTableLearnPortLimit_Type.__name__=_B
_Es2126PoEplusMacTableLearnPortLimit_Object=MibTableColumn
es2126PoEplusMacTableLearnPortLimit=_Es2126PoEplusMacTableLearnPortLimit_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,1,3,1,2),_Es2126PoEplusMacTableLearnPortLimit_Type())
es2126PoEplusMacTableLearnPortLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusMacTableLearnPortLimit.setStatus(_A)
_Es2126PoEplusMacTableStaticMac_ObjectIdentity=ObjectIdentity
es2126PoEplusMacTableStaticMac=_Es2126PoEplusMacTableStaticMac_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,11,3))
class _Es2126PoEplusMacTableStaticMacNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_Es2126PoEplusMacTableStaticMacNumber_Type.__name__=_B
_Es2126PoEplusMacTableStaticMacNumber_Object=MibScalar
es2126PoEplusMacTableStaticMacNumber=_Es2126PoEplusMacTableStaticMacNumber_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,3,1),_Es2126PoEplusMacTableStaticMacNumber_Type())
es2126PoEplusMacTableStaticMacNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusMacTableStaticMacNumber.setStatus(_A)
class _Es2126PoEplusMacTableStaticMacEntryCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_Es2126PoEplusMacTableStaticMacEntryCreate_Type.__name__=_B
_Es2126PoEplusMacTableStaticMacEntryCreate_Object=MibScalar
es2126PoEplusMacTableStaticMacEntryCreate=_Es2126PoEplusMacTableStaticMacEntryCreate_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,3,2),_Es2126PoEplusMacTableStaticMacEntryCreate_Type())
es2126PoEplusMacTableStaticMacEntryCreate.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusMacTableStaticMacEntryCreate.setStatus(_A)
_Es2126PoEplusMacTableStaticMacTable_Object=MibTable
es2126PoEplusMacTableStaticMacTable=_Es2126PoEplusMacTableStaticMacTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,3,3))
if mibBuilder.loadTexts:es2126PoEplusMacTableStaticMacTable.setStatus(_A)
_Es2126PoEplusMacTableStaticMacEntry_Object=MibTableRow
es2126PoEplusMacTableStaticMacEntry=_Es2126PoEplusMacTableStaticMacEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,3,3,1))
es2126PoEplusMacTableStaticMacEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:es2126PoEplusMacTableStaticMacEntry.setStatus(_A)
class _Es2126PoEplusMacTableStaticMacIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_Es2126PoEplusMacTableStaticMacIndex_Type.__name__=_B
_Es2126PoEplusMacTableStaticMacIndex_Object=MibTableColumn
es2126PoEplusMacTableStaticMacIndex=_Es2126PoEplusMacTableStaticMacIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,3,3,1,1),_Es2126PoEplusMacTableStaticMacIndex_Type())
es2126PoEplusMacTableStaticMacIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:es2126PoEplusMacTableStaticMacIndex.setStatus(_A)
_Es2126PoEplusMacTableStaticMacAddress_Type=DisplayString
_Es2126PoEplusMacTableStaticMacAddress_Object=MibTableColumn
es2126PoEplusMacTableStaticMacAddress=_Es2126PoEplusMacTableStaticMacAddress_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,3,3,1,2),_Es2126PoEplusMacTableStaticMacAddress_Type())
es2126PoEplusMacTableStaticMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusMacTableStaticMacAddress.setStatus(_A)
class _Es2126PoEplusMacTableStaticMacVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Es2126PoEplusMacTableStaticMacVid_Type.__name__=_B
_Es2126PoEplusMacTableStaticMacVid_Object=MibTableColumn
es2126PoEplusMacTableStaticMacVid=_Es2126PoEplusMacTableStaticMacVid_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,3,3,1,3),_Es2126PoEplusMacTableStaticMacVid_Type())
es2126PoEplusMacTableStaticMacVid.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusMacTableStaticMacVid.setStatus(_A)
class _Es2126PoEplusMacTableStaticMacQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Es2126PoEplusMacTableStaticMacQueue_Type.__name__=_B
_Es2126PoEplusMacTableStaticMacQueue_Object=MibTableColumn
es2126PoEplusMacTableStaticMacQueue=_Es2126PoEplusMacTableStaticMacQueue_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,3,3,1,4),_Es2126PoEplusMacTableStaticMacQueue_Type())
es2126PoEplusMacTableStaticMacQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusMacTableStaticMacQueue.setStatus(_A)
class _Es2126PoEplusMacTableStaticMacFwRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Es2126PoEplusMacTableStaticMacFwRule_Type.__name__=_B
_Es2126PoEplusMacTableStaticMacFwRule_Object=MibTableColumn
es2126PoEplusMacTableStaticMacFwRule=_Es2126PoEplusMacTableStaticMacFwRule_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,3,3,1,5),_Es2126PoEplusMacTableStaticMacFwRule_Type())
es2126PoEplusMacTableStaticMacFwRule.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusMacTableStaticMacFwRule.setStatus(_A)
class _Es2126PoEplusMacTableStaticMacPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_Es2126PoEplusMacTableStaticMacPort_Type.__name__=_B
_Es2126PoEplusMacTableStaticMacPort_Object=MibTableColumn
es2126PoEplusMacTableStaticMacPort=_Es2126PoEplusMacTableStaticMacPort_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,3,3,1,6),_Es2126PoEplusMacTableStaticMacPort_Type())
es2126PoEplusMacTableStaticMacPort.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusMacTableStaticMacPort.setStatus(_A)
class _Es2126PoEplusMacTableStaticMacEntryAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Es2126PoEplusMacTableStaticMacEntryAction_Type.__name__=_B
_Es2126PoEplusMacTableStaticMacEntryAction_Object=MibTableColumn
es2126PoEplusMacTableStaticMacEntryAction=_Es2126PoEplusMacTableStaticMacEntryAction_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,3,3,1,7),_Es2126PoEplusMacTableStaticMacEntryAction_Type())
es2126PoEplusMacTableStaticMacEntryAction.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusMacTableStaticMacEntryAction.setStatus(_A)
_Es2126PoEplusMacTableMacAlias_ObjectIdentity=ObjectIdentity
es2126PoEplusMacTableMacAlias=_Es2126PoEplusMacTableMacAlias_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,11,4))
class _Es2126PoEplusMacTableMacAliasNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8192))
_Es2126PoEplusMacTableMacAliasNumber_Type.__name__=_B
_Es2126PoEplusMacTableMacAliasNumber_Object=MibScalar
es2126PoEplusMacTableMacAliasNumber=_Es2126PoEplusMacTableMacAliasNumber_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,4,1),_Es2126PoEplusMacTableMacAliasNumber_Type())
es2126PoEplusMacTableMacAliasNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusMacTableMacAliasNumber.setStatus(_A)
class _Es2126PoEplusMacTableMacAliasEntryCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8192))
_Es2126PoEplusMacTableMacAliasEntryCreate_Type.__name__=_B
_Es2126PoEplusMacTableMacAliasEntryCreate_Object=MibScalar
es2126PoEplusMacTableMacAliasEntryCreate=_Es2126PoEplusMacTableMacAliasEntryCreate_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,4,2),_Es2126PoEplusMacTableMacAliasEntryCreate_Type())
es2126PoEplusMacTableMacAliasEntryCreate.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusMacTableMacAliasEntryCreate.setStatus(_A)
_Es2126PoEplusMacTableMacAliasTable_Object=MibTable
es2126PoEplusMacTableMacAliasTable=_Es2126PoEplusMacTableMacAliasTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,4,3))
if mibBuilder.loadTexts:es2126PoEplusMacTableMacAliasTable.setStatus(_A)
_Es2126PoEplusMacTableMacAliasEntry_Object=MibTableRow
es2126PoEplusMacTableMacAliasEntry=_Es2126PoEplusMacTableMacAliasEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,4,3,1))
es2126PoEplusMacTableMacAliasEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:es2126PoEplusMacTableMacAliasEntry.setStatus(_A)
class _Es2126PoEplusMacTableMacAliasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_Es2126PoEplusMacTableMacAliasIndex_Type.__name__=_B
_Es2126PoEplusMacTableMacAliasIndex_Object=MibTableColumn
es2126PoEplusMacTableMacAliasIndex=_Es2126PoEplusMacTableMacAliasIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,4,3,1,1),_Es2126PoEplusMacTableMacAliasIndex_Type())
es2126PoEplusMacTableMacAliasIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:es2126PoEplusMacTableMacAliasIndex.setStatus(_A)
_Es2126PoEplusMacTableMacAliasAddress_Type=DisplayString
_Es2126PoEplusMacTableMacAliasAddress_Object=MibTableColumn
es2126PoEplusMacTableMacAliasAddress=_Es2126PoEplusMacTableMacAliasAddress_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,4,3,1,2),_Es2126PoEplusMacTableMacAliasAddress_Type())
es2126PoEplusMacTableMacAliasAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusMacTableMacAliasAddress.setStatus(_A)
_Es2126PoEplusMacTableMacAliasAlias_Type=DisplayString
_Es2126PoEplusMacTableMacAliasAlias_Object=MibTableColumn
es2126PoEplusMacTableMacAliasAlias=_Es2126PoEplusMacTableMacAliasAlias_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,4,3,1,3),_Es2126PoEplusMacTableMacAliasAlias_Type())
es2126PoEplusMacTableMacAliasAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusMacTableMacAliasAlias.setStatus(_A)
class _Es2126PoEplusMacTableMacAliasEntryAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Es2126PoEplusMacTableMacAliasEntryAction_Type.__name__=_B
_Es2126PoEplusMacTableMacAliasEntryAction_Object=MibTableColumn
es2126PoEplusMacTableMacAliasEntryAction=_Es2126PoEplusMacTableMacAliasEntryAction_Object((1,3,6,1,4,1,2356,800,2,2129,1,11,4,3,1,4),_Es2126PoEplusMacTableMacAliasEntryAction_Type())
es2126PoEplusMacTableMacAliasEntryAction.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusMacTableMacAliasEntryAction.setStatus(_A)
_Es2126PoEplusGVRPInfo_ObjectIdentity=ObjectIdentity
es2126PoEplusGVRPInfo=_Es2126PoEplusGVRPInfo_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,12))
_Es2126PoEplusGvrpConf_ObjectIdentity=ObjectIdentity
es2126PoEplusGvrpConf=_Es2126PoEplusGvrpConf_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,12,1))
class _Es2126PoEplusGvrpConfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusGvrpConfState_Type.__name__=_B
_Es2126PoEplusGvrpConfState_Object=MibScalar
es2126PoEplusGvrpConfState=_Es2126PoEplusGvrpConfState_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,1,1),_Es2126PoEplusGvrpConfState_Type())
es2126PoEplusGvrpConfState.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusGvrpConfState.setStatus(_A)
_Es2126PoEplusGvrpConfTable_Object=MibTable
es2126PoEplusGvrpConfTable=_Es2126PoEplusGvrpConfTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,1,2))
if mibBuilder.loadTexts:es2126PoEplusGvrpConfTable.setStatus(_A)
_Es2126PoEplusGvrpConfEntry_Object=MibTableRow
es2126PoEplusGvrpConfEntry=_Es2126PoEplusGvrpConfEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,1,2,1))
es2126PoEplusGvrpConfEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:es2126PoEplusGvrpConfEntry.setStatus(_A)
class _Es2126PoEplusGvrpConfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_Es2126PoEplusGvrpConfIndex_Type.__name__=_B
_Es2126PoEplusGvrpConfIndex_Object=MibTableColumn
es2126PoEplusGvrpConfIndex=_Es2126PoEplusGvrpConfIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,1,2,1,1),_Es2126PoEplusGvrpConfIndex_Type())
es2126PoEplusGvrpConfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:es2126PoEplusGvrpConfIndex.setStatus(_A)
class _Es2126PoEplusGvrpConfJoinTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,100))
_Es2126PoEplusGvrpConfJoinTime_Type.__name__=_B
_Es2126PoEplusGvrpConfJoinTime_Object=MibTableColumn
es2126PoEplusGvrpConfJoinTime=_Es2126PoEplusGvrpConfJoinTime_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,1,2,1,2),_Es2126PoEplusGvrpConfJoinTime_Type())
es2126PoEplusGvrpConfJoinTime.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusGvrpConfJoinTime.setStatus(_A)
class _Es2126PoEplusGvrpConfLeaveTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,300))
_Es2126PoEplusGvrpConfLeaveTime_Type.__name__=_B
_Es2126PoEplusGvrpConfLeaveTime_Object=MibTableColumn
es2126PoEplusGvrpConfLeaveTime=_Es2126PoEplusGvrpConfLeaveTime_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,1,2,1,3),_Es2126PoEplusGvrpConfLeaveTime_Type())
es2126PoEplusGvrpConfLeaveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusGvrpConfLeaveTime.setStatus(_A)
class _Es2126PoEplusGvrpConfLeaveAllTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,5000))
_Es2126PoEplusGvrpConfLeaveAllTime_Type.__name__=_B
_Es2126PoEplusGvrpConfLeaveAllTime_Object=MibTableColumn
es2126PoEplusGvrpConfLeaveAllTime=_Es2126PoEplusGvrpConfLeaveAllTime_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,1,2,1,4),_Es2126PoEplusGvrpConfLeaveAllTime_Type())
es2126PoEplusGvrpConfLeaveAllTime.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusGvrpConfLeaveAllTime.setStatus(_A)
class _Es2126PoEplusGvrpConfDefaultAppMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusGvrpConfDefaultAppMode_Type.__name__=_B
_Es2126PoEplusGvrpConfDefaultAppMode_Object=MibTableColumn
es2126PoEplusGvrpConfDefaultAppMode=_Es2126PoEplusGvrpConfDefaultAppMode_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,1,2,1,5),_Es2126PoEplusGvrpConfDefaultAppMode_Type())
es2126PoEplusGvrpConfDefaultAppMode.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusGvrpConfDefaultAppMode.setStatus(_A)
class _Es2126PoEplusGvrpConfDefaultRegMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_Es2126PoEplusGvrpConfDefaultRegMode_Type.__name__=_B
_Es2126PoEplusGvrpConfDefaultRegMode_Object=MibTableColumn
es2126PoEplusGvrpConfDefaultRegMode=_Es2126PoEplusGvrpConfDefaultRegMode_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,1,2,1,6),_Es2126PoEplusGvrpConfDefaultRegMode_Type())
es2126PoEplusGvrpConfDefaultRegMode.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusGvrpConfDefaultRegMode.setStatus(_A)
class _Es2126PoEplusGvrpConfRestrictedMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusGvrpConfRestrictedMode_Type.__name__=_B
_Es2126PoEplusGvrpConfRestrictedMode_Object=MibTableColumn
es2126PoEplusGvrpConfRestrictedMode=_Es2126PoEplusGvrpConfRestrictedMode_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,1,2,1,7),_Es2126PoEplusGvrpConfRestrictedMode_Type())
es2126PoEplusGvrpConfRestrictedMode.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusGvrpConfRestrictedMode.setStatus(_A)
_Es2126PoEplusGvrpCounter_ObjectIdentity=ObjectIdentity
es2126PoEplusGvrpCounter=_Es2126PoEplusGvrpCounter_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,12,2))
_Es2126PoEplusGvrpCounterTable_Object=MibTable
es2126PoEplusGvrpCounterTable=_Es2126PoEplusGvrpCounterTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,2,1))
if mibBuilder.loadTexts:es2126PoEplusGvrpCounterTable.setStatus(_A)
_Es2126PoEplusGvrpCounterEntry_Object=MibTableRow
es2126PoEplusGvrpCounterEntry=_Es2126PoEplusGvrpCounterEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,2,1,1))
es2126PoEplusGvrpCounterEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:es2126PoEplusGvrpCounterEntry.setStatus(_A)
class _Es2126PoEplusGvrpCounterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_Es2126PoEplusGvrpCounterIndex_Type.__name__=_B
_Es2126PoEplusGvrpCounterIndex_Object=MibTableColumn
es2126PoEplusGvrpCounterIndex=_Es2126PoEplusGvrpCounterIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,2,1,1,1),_Es2126PoEplusGvrpCounterIndex_Type())
es2126PoEplusGvrpCounterIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:es2126PoEplusGvrpCounterIndex.setStatus(_A)
_Es2126PoEplusGvrpCounterRxTotalGvrpPkts_Type=Counter32
_Es2126PoEplusGvrpCounterRxTotalGvrpPkts_Object=MibTableColumn
es2126PoEplusGvrpCounterRxTotalGvrpPkts=_Es2126PoEplusGvrpCounterRxTotalGvrpPkts_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,2,1,1,2),_Es2126PoEplusGvrpCounterRxTotalGvrpPkts_Type())
es2126PoEplusGvrpCounterRxTotalGvrpPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusGvrpCounterRxTotalGvrpPkts.setStatus(_A)
_Es2126PoEplusGvrpCounterRxInvalidGvrpPkts_Type=Counter32
_Es2126PoEplusGvrpCounterRxInvalidGvrpPkts_Object=MibTableColumn
es2126PoEplusGvrpCounterRxInvalidGvrpPkts=_Es2126PoEplusGvrpCounterRxInvalidGvrpPkts_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,2,1,1,3),_Es2126PoEplusGvrpCounterRxInvalidGvrpPkts_Type())
es2126PoEplusGvrpCounterRxInvalidGvrpPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusGvrpCounterRxInvalidGvrpPkts.setStatus(_A)
_Es2126PoEplusGvrpCounterRxLeaveAllMsg_Type=Counter32
_Es2126PoEplusGvrpCounterRxLeaveAllMsg_Object=MibTableColumn
es2126PoEplusGvrpCounterRxLeaveAllMsg=_Es2126PoEplusGvrpCounterRxLeaveAllMsg_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,2,1,1,4),_Es2126PoEplusGvrpCounterRxLeaveAllMsg_Type())
es2126PoEplusGvrpCounterRxLeaveAllMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusGvrpCounterRxLeaveAllMsg.setStatus(_A)
_Es2126PoEplusGvrpCounterRxJoinEmptyMsg_Type=Counter32
_Es2126PoEplusGvrpCounterRxJoinEmptyMsg_Object=MibTableColumn
es2126PoEplusGvrpCounterRxJoinEmptyMsg=_Es2126PoEplusGvrpCounterRxJoinEmptyMsg_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,2,1,1,5),_Es2126PoEplusGvrpCounterRxJoinEmptyMsg_Type())
es2126PoEplusGvrpCounterRxJoinEmptyMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusGvrpCounterRxJoinEmptyMsg.setStatus(_A)
_Es2126PoEplusGvrpCounterRxJoinInMsg_Type=Counter32
_Es2126PoEplusGvrpCounterRxJoinInMsg_Object=MibTableColumn
es2126PoEplusGvrpCounterRxJoinInMsg=_Es2126PoEplusGvrpCounterRxJoinInMsg_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,2,1,1,6),_Es2126PoEplusGvrpCounterRxJoinInMsg_Type())
es2126PoEplusGvrpCounterRxJoinInMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusGvrpCounterRxJoinInMsg.setStatus(_A)
_Es2126PoEplusGvrpCounterRxLeaveEmptyMsg_Type=Counter32
_Es2126PoEplusGvrpCounterRxLeaveEmptyMsg_Object=MibTableColumn
es2126PoEplusGvrpCounterRxLeaveEmptyMsg=_Es2126PoEplusGvrpCounterRxLeaveEmptyMsg_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,2,1,1,7),_Es2126PoEplusGvrpCounterRxLeaveEmptyMsg_Type())
es2126PoEplusGvrpCounterRxLeaveEmptyMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusGvrpCounterRxLeaveEmptyMsg.setStatus(_A)
_Es2126PoEplusGvrpCounterRxEmptyMsg_Type=Counter32
_Es2126PoEplusGvrpCounterRxEmptyMsg_Object=MibTableColumn
es2126PoEplusGvrpCounterRxEmptyMsg=_Es2126PoEplusGvrpCounterRxEmptyMsg_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,2,1,1,8),_Es2126PoEplusGvrpCounterRxEmptyMsg_Type())
es2126PoEplusGvrpCounterRxEmptyMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusGvrpCounterRxEmptyMsg.setStatus(_A)
_Es2126PoEplusGvrpCounterTxTotalGvrpPkts_Type=Counter32
_Es2126PoEplusGvrpCounterTxTotalGvrpPkts_Object=MibTableColumn
es2126PoEplusGvrpCounterTxTotalGvrpPkts=_Es2126PoEplusGvrpCounterTxTotalGvrpPkts_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,2,1,1,9),_Es2126PoEplusGvrpCounterTxTotalGvrpPkts_Type())
es2126PoEplusGvrpCounterTxTotalGvrpPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusGvrpCounterTxTotalGvrpPkts.setStatus(_A)
_Es2126PoEplusGvrpCounterTxLeaveAllMsg_Type=Counter32
_Es2126PoEplusGvrpCounterTxLeaveAllMsg_Object=MibTableColumn
es2126PoEplusGvrpCounterTxLeaveAllMsg=_Es2126PoEplusGvrpCounterTxLeaveAllMsg_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,2,1,1,10),_Es2126PoEplusGvrpCounterTxLeaveAllMsg_Type())
es2126PoEplusGvrpCounterTxLeaveAllMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusGvrpCounterTxLeaveAllMsg.setStatus(_A)
_Es2126PoEplusGvrpCounterTxJoinEmptyMsg_Type=Counter32
_Es2126PoEplusGvrpCounterTxJoinEmptyMsg_Object=MibTableColumn
es2126PoEplusGvrpCounterTxJoinEmptyMsg=_Es2126PoEplusGvrpCounterTxJoinEmptyMsg_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,2,1,1,11),_Es2126PoEplusGvrpCounterTxJoinEmptyMsg_Type())
es2126PoEplusGvrpCounterTxJoinEmptyMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusGvrpCounterTxJoinEmptyMsg.setStatus(_A)
_Es2126PoEplusGvrpCounterTxJoinInMsg_Type=Counter32
_Es2126PoEplusGvrpCounterTxJoinInMsg_Object=MibTableColumn
es2126PoEplusGvrpCounterTxJoinInMsg=_Es2126PoEplusGvrpCounterTxJoinInMsg_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,2,1,1,12),_Es2126PoEplusGvrpCounterTxJoinInMsg_Type())
es2126PoEplusGvrpCounterTxJoinInMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusGvrpCounterTxJoinInMsg.setStatus(_A)
_Es2126PoEplusGvrpCounterTxLeaveEmptyMsg_Type=Counter32
_Es2126PoEplusGvrpCounterTxLeaveEmptyMsg_Object=MibTableColumn
es2126PoEplusGvrpCounterTxLeaveEmptyMsg=_Es2126PoEplusGvrpCounterTxLeaveEmptyMsg_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,2,1,1,13),_Es2126PoEplusGvrpCounterTxLeaveEmptyMsg_Type())
es2126PoEplusGvrpCounterTxLeaveEmptyMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusGvrpCounterTxLeaveEmptyMsg.setStatus(_A)
_Es2126PoEplusGvrpCounterTxEmptyMsg_Type=Counter32
_Es2126PoEplusGvrpCounterTxEmptyMsg_Object=MibTableColumn
es2126PoEplusGvrpCounterTxEmptyMsg=_Es2126PoEplusGvrpCounterTxEmptyMsg_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,2,1,1,14),_Es2126PoEplusGvrpCounterTxEmptyMsg_Type())
es2126PoEplusGvrpCounterTxEmptyMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusGvrpCounterTxEmptyMsg.setStatus(_A)
_Es2126PoEplusGvrpGroup_ObjectIdentity=ObjectIdentity
es2126PoEplusGvrpGroup=_Es2126PoEplusGvrpGroup_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,12,3))
class _Es2126PoEplusGvrpGroupNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_Es2126PoEplusGvrpGroupNumber_Type.__name__=_B
_Es2126PoEplusGvrpGroupNumber_Object=MibScalar
es2126PoEplusGvrpGroupNumber=_Es2126PoEplusGvrpGroupNumber_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,3,1),_Es2126PoEplusGvrpGroupNumber_Type())
es2126PoEplusGvrpGroupNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusGvrpGroupNumber.setStatus(_A)
_Es2126PoEplusGvrpGroupTable_Object=MibTable
es2126PoEplusGvrpGroupTable=_Es2126PoEplusGvrpGroupTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,3,2))
if mibBuilder.loadTexts:es2126PoEplusGvrpGroupTable.setStatus(_A)
_Es2126PoEplusGvrpGroupEntry_Object=MibTableRow
es2126PoEplusGvrpGroupEntry=_Es2126PoEplusGvrpGroupEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,3,2,1))
es2126PoEplusGvrpGroupEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:es2126PoEplusGvrpGroupEntry.setStatus(_A)
class _Es2126PoEplusGvrpGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Es2126PoEplusGvrpGroupId_Type.__name__=_B
_Es2126PoEplusGvrpGroupId_Object=MibTableColumn
es2126PoEplusGvrpGroupId=_Es2126PoEplusGvrpGroupId_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,3,2,1,1),_Es2126PoEplusGvrpGroupId_Type())
es2126PoEplusGvrpGroupId.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusGvrpGroupId.setStatus(_A)
class _Es2126PoEplusGvrpGroupVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Es2126PoEplusGvrpGroupVid_Type.__name__=_B
_Es2126PoEplusGvrpGroupVid_Object=MibTableColumn
es2126PoEplusGvrpGroupVid=_Es2126PoEplusGvrpGroupVid_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,3,2,1,2),_Es2126PoEplusGvrpGroupVid_Type())
es2126PoEplusGvrpGroupVid.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusGvrpGroupVid.setStatus(_A)
_Es2126PoEplusGvrpGroupMemberPort_Type=DisplayString
_Es2126PoEplusGvrpGroupMemberPort_Object=MibTableColumn
es2126PoEplusGvrpGroupMemberPort=_Es2126PoEplusGvrpGroupMemberPort_Object((1,3,6,1,4,1,2356,800,2,2129,1,12,3,2,1,3),_Es2126PoEplusGvrpGroupMemberPort_Type())
es2126PoEplusGvrpGroupMemberPort.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusGvrpGroupMemberPort.setStatus(_A)
_Es2126PoEplusSecurity_ObjectIdentity=ObjectIdentity
es2126PoEplusSecurity=_Es2126PoEplusSecurity_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,13))
_Es2126PoEplusIsolatedPortGroup_Type=DisplayString
_Es2126PoEplusIsolatedPortGroup_Object=MibScalar
es2126PoEplusIsolatedPortGroup=_Es2126PoEplusIsolatedPortGroup_Object((1,3,6,1,4,1,2356,800,2,2129,1,13,1),_Es2126PoEplusIsolatedPortGroup_Type())
es2126PoEplusIsolatedPortGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusIsolatedPortGroup.setStatus(_A)
_Es2126PoEplusMirror_ObjectIdentity=ObjectIdentity
es2126PoEplusMirror=_Es2126PoEplusMirror_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,13,2))
class _Es2126PoEplusMirrorMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusMirrorMode_Type.__name__=_B
_Es2126PoEplusMirrorMode_Object=MibScalar
es2126PoEplusMirrorMode=_Es2126PoEplusMirrorMode_Object((1,3,6,1,4,1,2356,800,2,2129,1,13,2,1),_Es2126PoEplusMirrorMode_Type())
es2126PoEplusMirrorMode.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusMirrorMode.setStatus(_A)
class _Es2126PoEplusMonitoringPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_Es2126PoEplusMonitoringPort_Type.__name__=_B
_Es2126PoEplusMonitoringPort_Object=MibScalar
es2126PoEplusMonitoringPort=_Es2126PoEplusMonitoringPort_Object((1,3,6,1,4,1,2356,800,2,2129,1,13,2,2),_Es2126PoEplusMonitoringPort_Type())
es2126PoEplusMonitoringPort.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusMonitoringPort.setStatus(_A)
_Es2126PoEplusMonitoredIngressPort_Type=DisplayString
_Es2126PoEplusMonitoredIngressPort_Object=MibScalar
es2126PoEplusMonitoredIngressPort=_Es2126PoEplusMonitoredIngressPort_Object((1,3,6,1,4,1,2356,800,2,2129,1,13,2,3),_Es2126PoEplusMonitoredIngressPort_Type())
es2126PoEplusMonitoredIngressPort.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusMonitoredIngressPort.setStatus(_A)
_Es2126PoEplusMonitoredEgressPort_Type=DisplayString
_Es2126PoEplusMonitoredEgressPort_Object=MibScalar
es2126PoEplusMonitoredEgressPort=_Es2126PoEplusMonitoredEgressPort_Object((1,3,6,1,4,1,2356,800,2,2129,1,13,2,4),_Es2126PoEplusMonitoredEgressPort_Type())
es2126PoEplusMonitoredEgressPort.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusMonitoredEgressPort.setStatus(_A)
_Es2126PoEplusRestrictedGroup_ObjectIdentity=ObjectIdentity
es2126PoEplusRestrictedGroup=_Es2126PoEplusRestrictedGroup_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,13,3))
_Es2126PoEplusRestrictedGroupIngress_Type=DisplayString
_Es2126PoEplusRestrictedGroupIngress_Object=MibScalar
es2126PoEplusRestrictedGroupIngress=_Es2126PoEplusRestrictedGroupIngress_Object((1,3,6,1,4,1,2356,800,2,2129,1,13,3,1),_Es2126PoEplusRestrictedGroupIngress_Type())
es2126PoEplusRestrictedGroupIngress.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusRestrictedGroupIngress.setStatus(_A)
_Es2126PoEplusRestrictedGroupEgress_Type=DisplayString
_Es2126PoEplusRestrictedGroupEgress_Object=MibScalar
es2126PoEplusRestrictedGroupEgress=_Es2126PoEplusRestrictedGroupEgress_Object((1,3,6,1,4,1,2356,800,2,2129,1,13,3,2),_Es2126PoEplusRestrictedGroupEgress_Type())
es2126PoEplusRestrictedGroupEgress.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusRestrictedGroupEgress.setStatus(_A)
_Es2126PoEplusVirtualStack_ObjectIdentity=ObjectIdentity
es2126PoEplusVirtualStack=_Es2126PoEplusVirtualStack_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,14))
class _Es2126PoEplusVirtualStackState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusVirtualStackState_Type.__name__=_B
_Es2126PoEplusVirtualStackState_Object=MibScalar
es2126PoEplusVirtualStackState=_Es2126PoEplusVirtualStackState_Object((1,3,6,1,4,1,2356,800,2,2129,1,14,1),_Es2126PoEplusVirtualStackState_Type())
es2126PoEplusVirtualStackState.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusVirtualStackState.setStatus(_A)
class _Es2126PoEplusVirtualStackRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusVirtualStackRole_Type.__name__=_B
_Es2126PoEplusVirtualStackRole_Object=MibScalar
es2126PoEplusVirtualStackRole=_Es2126PoEplusVirtualStackRole_Object((1,3,6,1,4,1,2356,800,2,2129,1,14,2),_Es2126PoEplusVirtualStackRole_Type())
es2126PoEplusVirtualStackRole.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusVirtualStackRole.setStatus(_A)
_Es2126PoEplusVirtualStackGroupID_Type=DisplayString
_Es2126PoEplusVirtualStackGroupID_Object=MibScalar
es2126PoEplusVirtualStackGroupID=_Es2126PoEplusVirtualStackGroupID_Object((1,3,6,1,4,1,2356,800,2,2129,1,14,3),_Es2126PoEplusVirtualStackGroupID_Type())
es2126PoEplusVirtualStackGroupID.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusVirtualStackGroupID.setStatus(_A)
_Es2126PoEplusManagementSecurity_ObjectIdentity=ObjectIdentity
es2126PoEplusManagementSecurity=_Es2126PoEplusManagementSecurity_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,15))
class _Es2126PoEplusManagementSecurityNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_Es2126PoEplusManagementSecurityNumber_Type.__name__=_B
_Es2126PoEplusManagementSecurityNumber_Object=MibScalar
es2126PoEplusManagementSecurityNumber=_Es2126PoEplusManagementSecurityNumber_Object((1,3,6,1,4,1,2356,800,2,2129,1,15,1),_Es2126PoEplusManagementSecurityNumber_Type())
es2126PoEplusManagementSecurityNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusManagementSecurityNumber.setStatus(_A)
class _Es2126PoEplusManagementSecurityEntryCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_Es2126PoEplusManagementSecurityEntryCreate_Type.__name__=_B
_Es2126PoEplusManagementSecurityEntryCreate_Object=MibScalar
es2126PoEplusManagementSecurityEntryCreate=_Es2126PoEplusManagementSecurityEntryCreate_Object((1,3,6,1,4,1,2356,800,2,2129,1,15,2),_Es2126PoEplusManagementSecurityEntryCreate_Type())
es2126PoEplusManagementSecurityEntryCreate.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusManagementSecurityEntryCreate.setStatus(_A)
_Es2126PoEplusManagementSecurityTable_Object=MibTable
es2126PoEplusManagementSecurityTable=_Es2126PoEplusManagementSecurityTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,15,3))
if mibBuilder.loadTexts:es2126PoEplusManagementSecurityTable.setStatus(_A)
_Es2126PoEplusManagementSecurityEntry_Object=MibTableRow
es2126PoEplusManagementSecurityEntry=_Es2126PoEplusManagementSecurityEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,15,3,1))
es2126PoEplusManagementSecurityEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:es2126PoEplusManagementSecurityEntry.setStatus(_A)
class _Es2126PoEplusManagementSecurityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Es2126PoEplusManagementSecurityIndex_Type.__name__=_B
_Es2126PoEplusManagementSecurityIndex_Object=MibTableColumn
es2126PoEplusManagementSecurityIndex=_Es2126PoEplusManagementSecurityIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,15,3,1,1),_Es2126PoEplusManagementSecurityIndex_Type())
es2126PoEplusManagementSecurityIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:es2126PoEplusManagementSecurityIndex.setStatus(_A)
_Es2126PoEplusManagementSecurityName_Type=DisplayString
_Es2126PoEplusManagementSecurityName_Object=MibTableColumn
es2126PoEplusManagementSecurityName=_Es2126PoEplusManagementSecurityName_Object((1,3,6,1,4,1,2356,800,2,2129,1,15,3,1,2),_Es2126PoEplusManagementSecurityName_Type())
es2126PoEplusManagementSecurityName.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusManagementSecurityName.setStatus(_A)
class _Es2126PoEplusManagementSecurityVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_Es2126PoEplusManagementSecurityVid_Type.__name__=_B
_Es2126PoEplusManagementSecurityVid_Object=MibTableColumn
es2126PoEplusManagementSecurityVid=_Es2126PoEplusManagementSecurityVid_Object((1,3,6,1,4,1,2356,800,2,2129,1,15,3,1,3),_Es2126PoEplusManagementSecurityVid_Type())
es2126PoEplusManagementSecurityVid.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusManagementSecurityVid.setStatus(_A)
_Es2126PoEplusManagementSecurityIpRange_Type=DisplayString
_Es2126PoEplusManagementSecurityIpRange_Object=MibTableColumn
es2126PoEplusManagementSecurityIpRange=_Es2126PoEplusManagementSecurityIpRange_Object((1,3,6,1,4,1,2356,800,2,2129,1,15,3,1,4),_Es2126PoEplusManagementSecurityIpRange_Type())
es2126PoEplusManagementSecurityIpRange.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusManagementSecurityIpRange.setStatus(_A)
_Es2126PoEplusManagementSecurityIncomigPort_Type=DisplayString
_Es2126PoEplusManagementSecurityIncomigPort_Object=MibTableColumn
es2126PoEplusManagementSecurityIncomigPort=_Es2126PoEplusManagementSecurityIncomigPort_Object((1,3,6,1,4,1,2356,800,2,2129,1,15,3,1,5),_Es2126PoEplusManagementSecurityIncomigPort_Type())
es2126PoEplusManagementSecurityIncomigPort.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusManagementSecurityIncomigPort.setStatus(_A)
_Es2126PoEplusManagementSecurityAccessType_Type=DisplayString
_Es2126PoEplusManagementSecurityAccessType_Object=MibTableColumn
es2126PoEplusManagementSecurityAccessType=_Es2126PoEplusManagementSecurityAccessType_Object((1,3,6,1,4,1,2356,800,2,2129,1,15,3,1,6),_Es2126PoEplusManagementSecurityAccessType_Type())
es2126PoEplusManagementSecurityAccessType.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusManagementSecurityAccessType.setStatus(_A)
class _Es2126PoEplusManagementSecurityAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusManagementSecurityAction_Type.__name__=_B
_Es2126PoEplusManagementSecurityAction_Object=MibTableColumn
es2126PoEplusManagementSecurityAction=_Es2126PoEplusManagementSecurityAction_Object((1,3,6,1,4,1,2356,800,2,2129,1,15,3,1,7),_Es2126PoEplusManagementSecurityAction_Type())
es2126PoEplusManagementSecurityAction.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusManagementSecurityAction.setStatus(_A)
class _Es2126PoEplusManagementSecurityEntryAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Es2126PoEplusManagementSecurityEntryAction_Type.__name__=_B
_Es2126PoEplusManagementSecurityEntryAction_Object=MibTableColumn
es2126PoEplusManagementSecurityEntryAction=_Es2126PoEplusManagementSecurityEntryAction_Object((1,3,6,1,4,1,2356,800,2,2129,1,15,3,1,8),_Es2126PoEplusManagementSecurityEntryAction_Type())
es2126PoEplusManagementSecurityEntryAction.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusManagementSecurityEntryAction.setStatus(_A)
_Es2126PoEplusQoS_ObjectIdentity=ObjectIdentity
es2126PoEplusQoS=_Es2126PoEplusQoS_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,16))
_Es2126PoEplusQoSGlobalConfig_ObjectIdentity=ObjectIdentity
es2126PoEplusQoSGlobalConfig=_Es2126PoEplusQoSGlobalConfig_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,16,1))
class _Es2126PoEplusQoSMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusQoSMode_Type.__name__=_B
_Es2126PoEplusQoSMode_Object=MibScalar
es2126PoEplusQoSMode=_Es2126PoEplusQoSMode_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,1,1),_Es2126PoEplusQoSMode_Type())
es2126PoEplusQoSMode.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusQoSMode.setStatus(_A)
class _Es2126PoEplusQosPriorityControl1p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusQosPriorityControl1p_Type.__name__=_B
_Es2126PoEplusQosPriorityControl1p_Object=MibScalar
es2126PoEplusQosPriorityControl1p=_Es2126PoEplusQosPriorityControl1p_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,1,2),_Es2126PoEplusQosPriorityControl1p_Type())
es2126PoEplusQosPriorityControl1p.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusQosPriorityControl1p.setStatus(_A)
class _Es2126PoEplusQosPriorityControlTOS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusQosPriorityControlTOS_Type.__name__=_B
_Es2126PoEplusQosPriorityControlTOS_Object=MibScalar
es2126PoEplusQosPriorityControlTOS=_Es2126PoEplusQosPriorityControlTOS_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,1,3),_Es2126PoEplusQosPriorityControlTOS_Type())
es2126PoEplusQosPriorityControlTOS.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusQosPriorityControlTOS.setStatus(_A)
class _Es2126PoEplusQosPriorityControlDSCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusQosPriorityControlDSCP_Type.__name__=_B
_Es2126PoEplusQosPriorityControlDSCP_Object=MibScalar
es2126PoEplusQosPriorityControlDSCP=_Es2126PoEplusQosPriorityControlDSCP_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,1,4),_Es2126PoEplusQosPriorityControlDSCP_Type())
es2126PoEplusQosPriorityControlDSCP.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusQosPriorityControlDSCP.setStatus(_A)
class _Es2126PoEplusQoSSchedulingMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusQoSSchedulingMethod_Type.__name__=_B
_Es2126PoEplusQoSSchedulingMethod_Object=MibScalar
es2126PoEplusQoSSchedulingMethod=_Es2126PoEplusQoSSchedulingMethod_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,1,5),_Es2126PoEplusQoSSchedulingMethod_Type())
es2126PoEplusQoSSchedulingMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusQoSSchedulingMethod.setStatus(_A)
class _Es2126PoEplusQoSWeightQ0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,55))
_Es2126PoEplusQoSWeightQ0_Type.__name__=_B
_Es2126PoEplusQoSWeightQ0_Object=MibScalar
es2126PoEplusQoSWeightQ0=_Es2126PoEplusQoSWeightQ0_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,1,6),_Es2126PoEplusQoSWeightQ0_Type())
es2126PoEplusQoSWeightQ0.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusQoSWeightQ0.setStatus(_A)
class _Es2126PoEplusQoSWeightQ1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,55))
_Es2126PoEplusQoSWeightQ1_Type.__name__=_B
_Es2126PoEplusQoSWeightQ1_Object=MibScalar
es2126PoEplusQoSWeightQ1=_Es2126PoEplusQoSWeightQ1_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,1,7),_Es2126PoEplusQoSWeightQ1_Type())
es2126PoEplusQoSWeightQ1.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusQoSWeightQ1.setStatus(_A)
class _Es2126PoEplusQoSWeightQ2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,55))
_Es2126PoEplusQoSWeightQ2_Type.__name__=_B
_Es2126PoEplusQoSWeightQ2_Object=MibScalar
es2126PoEplusQoSWeightQ2=_Es2126PoEplusQoSWeightQ2_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,1,8),_Es2126PoEplusQoSWeightQ2_Type())
es2126PoEplusQoSWeightQ2.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusQoSWeightQ2.setStatus(_A)
class _Es2126PoEplusQoSWeightQ3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,55))
_Es2126PoEplusQoSWeightQ3_Type.__name__=_B
_Es2126PoEplusQoSWeightQ3_Object=MibScalar
es2126PoEplusQoSWeightQ3=_Es2126PoEplusQoSWeightQ3_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,1,9),_Es2126PoEplusQoSWeightQ3_Type())
es2126PoEplusQoSWeightQ3.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusQoSWeightQ3.setStatus(_A)
_Es2126PoEplusQoSVIPPort_Type=DisplayString
_Es2126PoEplusQoSVIPPort_Object=MibScalar
es2126PoEplusQoSVIPPort=_Es2126PoEplusQoSVIPPort_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,2),_Es2126PoEplusQoSVIPPort_Type())
es2126PoEplusQoSVIPPort.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusQoSVIPPort.setStatus(_A)
_Es2126PoEplusQoS1pPriority_ObjectIdentity=ObjectIdentity
es2126PoEplusQoS1pPriority=_Es2126PoEplusQoS1pPriority_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,16,3))
_Es2126PoEplusQoS1pPriorityTable_Object=MibTable
es2126PoEplusQoS1pPriorityTable=_Es2126PoEplusQoS1pPriorityTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,3,1))
if mibBuilder.loadTexts:es2126PoEplusQoS1pPriorityTable.setStatus(_A)
_Es2126PoEplusQoS1pPriorityEntry_Object=MibTableRow
es2126PoEplusQoS1pPriorityEntry=_Es2126PoEplusQoS1pPriorityEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,3,1,1))
es2126PoEplusQoS1pPriorityEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:es2126PoEplusQoS1pPriorityEntry.setStatus(_A)
class _Es2126PoEplusQoS1pPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Es2126PoEplusQoS1pPriorityIndex_Type.__name__=_B
_Es2126PoEplusQoS1pPriorityIndex_Object=MibTableColumn
es2126PoEplusQoS1pPriorityIndex=_Es2126PoEplusQoS1pPriorityIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,3,1,1,1),_Es2126PoEplusQoS1pPriorityIndex_Type())
es2126PoEplusQoS1pPriorityIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:es2126PoEplusQoS1pPriorityIndex.setStatus(_A)
class _Es2126PoEplusQoS1pPriorityValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Es2126PoEplusQoS1pPriorityValue_Type.__name__=_B
_Es2126PoEplusQoS1pPriorityValue_Object=MibTableColumn
es2126PoEplusQoS1pPriorityValue=_Es2126PoEplusQoS1pPriorityValue_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,3,1,1,2),_Es2126PoEplusQoS1pPriorityValue_Type())
es2126PoEplusQoS1pPriorityValue.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusQoS1pPriorityValue.setStatus(_A)
class _Es2126PoEplusQoS1pPriorityQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Es2126PoEplusQoS1pPriorityQueue_Type.__name__=_B
_Es2126PoEplusQoS1pPriorityQueue_Object=MibTableColumn
es2126PoEplusQoS1pPriorityQueue=_Es2126PoEplusQoS1pPriorityQueue_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,3,1,1,3),_Es2126PoEplusQoS1pPriorityQueue_Type())
es2126PoEplusQoS1pPriorityQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusQoS1pPriorityQueue.setStatus(_A)
_Es2126PoEplusQoSDTypeTOSPriority_ObjectIdentity=ObjectIdentity
es2126PoEplusQoSDTypeTOSPriority=_Es2126PoEplusQoSDTypeTOSPriority_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,16,4))
_Es2126PoEplusQoSDTypeTOSPriorityTable_Object=MibTable
es2126PoEplusQoSDTypeTOSPriorityTable=_Es2126PoEplusQoSDTypeTOSPriorityTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,4,1))
if mibBuilder.loadTexts:es2126PoEplusQoSDTypeTOSPriorityTable.setStatus(_A)
_Es2126PoEplusQoSDTypeTOSPriorityEntry_Object=MibTableRow
es2126PoEplusQoSDTypeTOSPriorityEntry=_Es2126PoEplusQoSDTypeTOSPriorityEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,4,1,1))
es2126PoEplusQoSDTypeTOSPriorityEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:es2126PoEplusQoSDTypeTOSPriorityEntry.setStatus(_A)
class _Es2126PoEplusQoSDTypeTOSPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Es2126PoEplusQoSDTypeTOSPriorityIndex_Type.__name__=_B
_Es2126PoEplusQoSDTypeTOSPriorityIndex_Object=MibTableColumn
es2126PoEplusQoSDTypeTOSPriorityIndex=_Es2126PoEplusQoSDTypeTOSPriorityIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,4,1,1,1),_Es2126PoEplusQoSDTypeTOSPriorityIndex_Type())
es2126PoEplusQoSDTypeTOSPriorityIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:es2126PoEplusQoSDTypeTOSPriorityIndex.setStatus(_A)
class _Es2126PoEplusQoSDTypeTOSPriorityValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Es2126PoEplusQoSDTypeTOSPriorityValue_Type.__name__=_B
_Es2126PoEplusQoSDTypeTOSPriorityValue_Object=MibTableColumn
es2126PoEplusQoSDTypeTOSPriorityValue=_Es2126PoEplusQoSDTypeTOSPriorityValue_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,4,1,1,2),_Es2126PoEplusQoSDTypeTOSPriorityValue_Type())
es2126PoEplusQoSDTypeTOSPriorityValue.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusQoSDTypeTOSPriorityValue.setStatus(_A)
class _Es2126PoEplusQoSDTypeTOSPriorityQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Es2126PoEplusQoSDTypeTOSPriorityQueue_Type.__name__=_B
_Es2126PoEplusQoSDTypeTOSPriorityQueue_Object=MibTableColumn
es2126PoEplusQoSDTypeTOSPriorityQueue=_Es2126PoEplusQoSDTypeTOSPriorityQueue_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,4,1,1,3),_Es2126PoEplusQoSDTypeTOSPriorityQueue_Type())
es2126PoEplusQoSDTypeTOSPriorityQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusQoSDTypeTOSPriorityQueue.setStatus(_A)
_Es2126PoEplusQoSTTypeTOSPriority_ObjectIdentity=ObjectIdentity
es2126PoEplusQoSTTypeTOSPriority=_Es2126PoEplusQoSTTypeTOSPriority_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,16,5))
_Es2126PoEplusQoSTTypeTOSPriorityTable_Object=MibTable
es2126PoEplusQoSTTypeTOSPriorityTable=_Es2126PoEplusQoSTTypeTOSPriorityTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,5,1))
if mibBuilder.loadTexts:es2126PoEplusQoSTTypeTOSPriorityTable.setStatus(_A)
_Es2126PoEplusQoSTTypeTOSPriorityEntry_Object=MibTableRow
es2126PoEplusQoSTTypeTOSPriorityEntry=_Es2126PoEplusQoSTTypeTOSPriorityEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,5,1,1))
es2126PoEplusQoSTTypeTOSPriorityEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:es2126PoEplusQoSTTypeTOSPriorityEntry.setStatus(_A)
class _Es2126PoEplusQoSTTypeTOSPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Es2126PoEplusQoSTTypeTOSPriorityIndex_Type.__name__=_B
_Es2126PoEplusQoSTTypeTOSPriorityIndex_Object=MibTableColumn
es2126PoEplusQoSTTypeTOSPriorityIndex=_Es2126PoEplusQoSTTypeTOSPriorityIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,5,1,1,1),_Es2126PoEplusQoSTTypeTOSPriorityIndex_Type())
es2126PoEplusQoSTTypeTOSPriorityIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:es2126PoEplusQoSTTypeTOSPriorityIndex.setStatus(_A)
class _Es2126PoEplusQoSTTypeTOSPriorityValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Es2126PoEplusQoSTTypeTOSPriorityValue_Type.__name__=_B
_Es2126PoEplusQoSTTypeTOSPriorityValue_Object=MibTableColumn
es2126PoEplusQoSTTypeTOSPriorityValue=_Es2126PoEplusQoSTTypeTOSPriorityValue_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,5,1,1,2),_Es2126PoEplusQoSTTypeTOSPriorityValue_Type())
es2126PoEplusQoSTTypeTOSPriorityValue.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusQoSTTypeTOSPriorityValue.setStatus(_A)
class _Es2126PoEplusQoSTTypeTOSPriorityQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Es2126PoEplusQoSTTypeTOSPriorityQueue_Type.__name__=_B
_Es2126PoEplusQoSTTypeTOSPriorityQueue_Object=MibTableColumn
es2126PoEplusQoSTTypeTOSPriorityQueue=_Es2126PoEplusQoSTTypeTOSPriorityQueue_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,5,1,1,3),_Es2126PoEplusQoSTTypeTOSPriorityQueue_Type())
es2126PoEplusQoSTTypeTOSPriorityQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusQoSTTypeTOSPriorityQueue.setStatus(_A)
_Es2126PoEplusQoSRTypeTOSPriority_ObjectIdentity=ObjectIdentity
es2126PoEplusQoSRTypeTOSPriority=_Es2126PoEplusQoSRTypeTOSPriority_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,16,6))
_Es2126PoEplusQoSRTypeTOSPriorityTable_Object=MibTable
es2126PoEplusQoSRTypeTOSPriorityTable=_Es2126PoEplusQoSRTypeTOSPriorityTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,6,1))
if mibBuilder.loadTexts:es2126PoEplusQoSRTypeTOSPriorityTable.setStatus(_A)
_Es2126PoEplusQoSRTypeTOSPriorityEntry_Object=MibTableRow
es2126PoEplusQoSRTypeTOSPriorityEntry=_Es2126PoEplusQoSRTypeTOSPriorityEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,6,1,1))
es2126PoEplusQoSRTypeTOSPriorityEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:es2126PoEplusQoSRTypeTOSPriorityEntry.setStatus(_A)
class _Es2126PoEplusQoSRTypeTOSPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Es2126PoEplusQoSRTypeTOSPriorityIndex_Type.__name__=_B
_Es2126PoEplusQoSRTypeTOSPriorityIndex_Object=MibTableColumn
es2126PoEplusQoSRTypeTOSPriorityIndex=_Es2126PoEplusQoSRTypeTOSPriorityIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,6,1,1,1),_Es2126PoEplusQoSRTypeTOSPriorityIndex_Type())
es2126PoEplusQoSRTypeTOSPriorityIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:es2126PoEplusQoSRTypeTOSPriorityIndex.setStatus(_A)
class _Es2126PoEplusQoSRTypeTOSPriorityValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Es2126PoEplusQoSRTypeTOSPriorityValue_Type.__name__=_B
_Es2126PoEplusQoSRTypeTOSPriorityValue_Object=MibTableColumn
es2126PoEplusQoSRTypeTOSPriorityValue=_Es2126PoEplusQoSRTypeTOSPriorityValue_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,6,1,1,2),_Es2126PoEplusQoSRTypeTOSPriorityValue_Type())
es2126PoEplusQoSRTypeTOSPriorityValue.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusQoSRTypeTOSPriorityValue.setStatus(_A)
class _Es2126PoEplusQoSRTypeTOSPriorityQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Es2126PoEplusQoSRTypeTOSPriorityQueue_Type.__name__=_B
_Es2126PoEplusQoSRTypeTOSPriorityQueue_Object=MibTableColumn
es2126PoEplusQoSRTypeTOSPriorityQueue=_Es2126PoEplusQoSRTypeTOSPriorityQueue_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,6,1,1,3),_Es2126PoEplusQoSRTypeTOSPriorityQueue_Type())
es2126PoEplusQoSRTypeTOSPriorityQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusQoSRTypeTOSPriorityQueue.setStatus(_A)
_Es2126PoEplusQoSMTypeTOSPriority_ObjectIdentity=ObjectIdentity
es2126PoEplusQoSMTypeTOSPriority=_Es2126PoEplusQoSMTypeTOSPriority_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,16,7))
_Es2126PoEplusQoSMTypeTOSPriorityTable_Object=MibTable
es2126PoEplusQoSMTypeTOSPriorityTable=_Es2126PoEplusQoSMTypeTOSPriorityTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,7,1))
if mibBuilder.loadTexts:es2126PoEplusQoSMTypeTOSPriorityTable.setStatus(_A)
_Es2126PoEplusQoSMTypeTOSPriorityEntry_Object=MibTableRow
es2126PoEplusQoSMTypeTOSPriorityEntry=_Es2126PoEplusQoSMTypeTOSPriorityEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,7,1,1))
es2126PoEplusQoSMTypeTOSPriorityEntry.setIndexNames((0,_E,_i))
if mibBuilder.loadTexts:es2126PoEplusQoSMTypeTOSPriorityEntry.setStatus(_A)
class _Es2126PoEplusQoSMTypeTOSPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Es2126PoEplusQoSMTypeTOSPriorityIndex_Type.__name__=_B
_Es2126PoEplusQoSMTypeTOSPriorityIndex_Object=MibTableColumn
es2126PoEplusQoSMTypeTOSPriorityIndex=_Es2126PoEplusQoSMTypeTOSPriorityIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,7,1,1,1),_Es2126PoEplusQoSMTypeTOSPriorityIndex_Type())
es2126PoEplusQoSMTypeTOSPriorityIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:es2126PoEplusQoSMTypeTOSPriorityIndex.setStatus(_A)
class _Es2126PoEplusQoSMTypeTOSPriorityValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Es2126PoEplusQoSMTypeTOSPriorityValue_Type.__name__=_B
_Es2126PoEplusQoSMTypeTOSPriorityValue_Object=MibTableColumn
es2126PoEplusQoSMTypeTOSPriorityValue=_Es2126PoEplusQoSMTypeTOSPriorityValue_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,7,1,1,2),_Es2126PoEplusQoSMTypeTOSPriorityValue_Type())
es2126PoEplusQoSMTypeTOSPriorityValue.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusQoSMTypeTOSPriorityValue.setStatus(_A)
class _Es2126PoEplusQoSMTypeTOSPriorityQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Es2126PoEplusQoSMTypeTOSPriorityQueue_Type.__name__=_B
_Es2126PoEplusQoSMTypeTOSPriorityQueue_Object=MibTableColumn
es2126PoEplusQoSMTypeTOSPriorityQueue=_Es2126PoEplusQoSMTypeTOSPriorityQueue_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,7,1,1,3),_Es2126PoEplusQoSMTypeTOSPriorityQueue_Type())
es2126PoEplusQoSMTypeTOSPriorityQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusQoSMTypeTOSPriorityQueue.setStatus(_A)
_Es2126PoEplusQoSDSCPPriority_ObjectIdentity=ObjectIdentity
es2126PoEplusQoSDSCPPriority=_Es2126PoEplusQoSDSCPPriority_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,16,8))
_Es2126PoEplusQoSDSCPPriorityTable_Object=MibTable
es2126PoEplusQoSDSCPPriorityTable=_Es2126PoEplusQoSDSCPPriorityTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,8,1))
if mibBuilder.loadTexts:es2126PoEplusQoSDSCPPriorityTable.setStatus(_A)
_Es2126PoEplusQoSDSCPPriorityEntry_Object=MibTableRow
es2126PoEplusQoSDSCPPriorityEntry=_Es2126PoEplusQoSDSCPPriorityEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,8,1,1))
es2126PoEplusQoSDSCPPriorityEntry.setIndexNames((0,_E,_j))
if mibBuilder.loadTexts:es2126PoEplusQoSDSCPPriorityEntry.setStatus(_A)
class _Es2126PoEplusQoSDSCPPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Es2126PoEplusQoSDSCPPriorityIndex_Type.__name__=_B
_Es2126PoEplusQoSDSCPPriorityIndex_Object=MibTableColumn
es2126PoEplusQoSDSCPPriorityIndex=_Es2126PoEplusQoSDSCPPriorityIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,8,1,1,1),_Es2126PoEplusQoSDSCPPriorityIndex_Type())
es2126PoEplusQoSDSCPPriorityIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:es2126PoEplusQoSDSCPPriorityIndex.setStatus(_A)
class _Es2126PoEplusQoSDSCPPriorityValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_Es2126PoEplusQoSDSCPPriorityValue_Type.__name__=_B
_Es2126PoEplusQoSDSCPPriorityValue_Object=MibTableColumn
es2126PoEplusQoSDSCPPriorityValue=_Es2126PoEplusQoSDSCPPriorityValue_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,8,1,1,2),_Es2126PoEplusQoSDSCPPriorityValue_Type())
es2126PoEplusQoSDSCPPriorityValue.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusQoSDSCPPriorityValue.setStatus(_A)
class _Es2126PoEplusQoSDSCPPriorityQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Es2126PoEplusQoSDSCPPriorityQueue_Type.__name__=_B
_Es2126PoEplusQoSDSCPPriorityQueue_Object=MibTableColumn
es2126PoEplusQoSDSCPPriorityQueue=_Es2126PoEplusQoSDSCPPriorityQueue_Object((1,3,6,1,4,1,2356,800,2,2129,1,16,8,1,1,3),_Es2126PoEplusQoSDSCPPriorityQueue_Type())
es2126PoEplusQoSDSCPPriorityQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusQoSDSCPPriorityQueue.setStatus(_A)
_Es2126PoEplusVlan_ObjectIdentity=ObjectIdentity
es2126PoEplusVlan=_Es2126PoEplusVlan_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,17))
_Es2126PoEplusVlanModeConfig_ObjectIdentity=ObjectIdentity
es2126PoEplusVlanModeConfig=_Es2126PoEplusVlanModeConfig_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,17,1))
class _Es2126PoEplusVlanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Es2126PoEplusVlanMode_Type.__name__=_B
_Es2126PoEplusVlanMode_Object=MibScalar
es2126PoEplusVlanMode=_Es2126PoEplusVlanMode_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,1,1),_Es2126PoEplusVlanMode_Type())
es2126PoEplusVlanMode.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusVlanMode.setStatus(_A)
class _Es2126PoEplusSymmetricVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusSymmetricVlan_Type.__name__=_B
_Es2126PoEplusSymmetricVlan_Object=MibScalar
es2126PoEplusSymmetricVlan=_Es2126PoEplusSymmetricVlan_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,1,2),_Es2126PoEplusSymmetricVlan_Type())
es2126PoEplusSymmetricVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusSymmetricVlan.setStatus(_A)
class _Es2126PoEplusVlanSVL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusVlanSVL_Type.__name__=_B
_Es2126PoEplusVlanSVL_Object=MibScalar
es2126PoEplusVlanSVL=_Es2126PoEplusVlanSVL_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,1,3),_Es2126PoEplusVlanSVL_Type())
es2126PoEplusVlanSVL.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusVlanSVL.setStatus(_A)
class _Es2126PoEplusDoubleTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusDoubleTag_Type.__name__=_B
_Es2126PoEplusDoubleTag_Object=MibScalar
es2126PoEplusDoubleTag=_Es2126PoEplusDoubleTag_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,1,4),_Es2126PoEplusDoubleTag_Type())
es2126PoEplusDoubleTag.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDoubleTag.setStatus(_A)
class _Es2126PoEplusUpLinkPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Es2126PoEplusUpLinkPort_Type.__name__=_B
_Es2126PoEplusUpLinkPort_Object=MibScalar
es2126PoEplusUpLinkPort=_Es2126PoEplusUpLinkPort_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,1,5),_Es2126PoEplusUpLinkPort_Type())
es2126PoEplusUpLinkPort.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusUpLinkPort.setStatus(_A)
_Es2126PoEplusTagBasedVlanGroup_ObjectIdentity=ObjectIdentity
es2126PoEplusTagBasedVlanGroup=_Es2126PoEplusTagBasedVlanGroup_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,17,2))
class _Es2126PoEplusTagBasedVlanNumbers_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Es2126PoEplusTagBasedVlanNumbers_Type.__name__=_B
_Es2126PoEplusTagBasedVlanNumbers_Object=MibScalar
es2126PoEplusTagBasedVlanNumbers=_Es2126PoEplusTagBasedVlanNumbers_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,2,1),_Es2126PoEplusTagBasedVlanNumbers_Type())
es2126PoEplusTagBasedVlanNumbers.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusTagBasedVlanNumbers.setStatus(_A)
class _Es2126PoEplusTagBasedCreateStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_Es2126PoEplusTagBasedCreateStatus_Type.__name__=_B
_Es2126PoEplusTagBasedCreateStatus_Object=MibScalar
es2126PoEplusTagBasedCreateStatus=_Es2126PoEplusTagBasedCreateStatus_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,2,2),_Es2126PoEplusTagBasedCreateStatus_Type())
es2126PoEplusTagBasedCreateStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusTagBasedCreateStatus.setStatus(_A)
_Es2126PoEplusTagBasedVlanTable_Object=MibTable
es2126PoEplusTagBasedVlanTable=_Es2126PoEplusTagBasedVlanTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,2,3))
if mibBuilder.loadTexts:es2126PoEplusTagBasedVlanTable.setStatus(_A)
_Es2126PoEplusTagBasedVlanEntry_Object=MibTableRow
es2126PoEplusTagBasedVlanEntry=_Es2126PoEplusTagBasedVlanEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,2,3,1))
es2126PoEplusTagBasedVlanEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:es2126PoEplusTagBasedVlanEntry.setStatus(_A)
class _Es2126PoEplusTagBasedVlanVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Es2126PoEplusTagBasedVlanVid_Type.__name__=_B
_Es2126PoEplusTagBasedVlanVid_Object=MibTableColumn
es2126PoEplusTagBasedVlanVid=_Es2126PoEplusTagBasedVlanVid_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,2,3,1,1),_Es2126PoEplusTagBasedVlanVid_Type())
es2126PoEplusTagBasedVlanVid.setMaxAccess(_F)
if mibBuilder.loadTexts:es2126PoEplusTagBasedVlanVid.setStatus(_A)
_Es2126PoEplusTagBasedVlanName_Type=DisplayString
_Es2126PoEplusTagBasedVlanName_Object=MibTableColumn
es2126PoEplusTagBasedVlanName=_Es2126PoEplusTagBasedVlanName_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,2,3,1,2),_Es2126PoEplusTagBasedVlanName_Type())
es2126PoEplusTagBasedVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusTagBasedVlanName.setStatus(_A)
_Es2126PoEplusTagBasedVlanMember_Type=DisplayString
_Es2126PoEplusTagBasedVlanMember_Object=MibTableColumn
es2126PoEplusTagBasedVlanMember=_Es2126PoEplusTagBasedVlanMember_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,2,3,1,3),_Es2126PoEplusTagBasedVlanMember_Type())
es2126PoEplusTagBasedVlanMember.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusTagBasedVlanMember.setStatus(_A)
_Es2126PoEplusTagBasedVlanUntag_Type=DisplayString
_Es2126PoEplusTagBasedVlanUntag_Object=MibTableColumn
es2126PoEplusTagBasedVlanUntag=_Es2126PoEplusTagBasedVlanUntag_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,2,3,1,4),_Es2126PoEplusTagBasedVlanUntag_Type())
es2126PoEplusTagBasedVlanUntag.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusTagBasedVlanUntag.setStatus(_A)
class _Es2126PoEplusTagBasedVlanRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Es2126PoEplusTagBasedVlanRowStatus_Type.__name__=_B
_Es2126PoEplusTagBasedVlanRowStatus_Object=MibTableColumn
es2126PoEplusTagBasedVlanRowStatus=_Es2126PoEplusTagBasedVlanRowStatus_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,2,3,1,5),_Es2126PoEplusTagBasedVlanRowStatus_Type())
es2126PoEplusTagBasedVlanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusTagBasedVlanRowStatus.setStatus(_A)
_Es2126PoEplusVlanPvid_ObjectIdentity=ObjectIdentity
es2126PoEplusVlanPvid=_Es2126PoEplusVlanPvid_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,17,3))
_Es2126PoEplusVlanPvidTable_Object=MibTable
es2126PoEplusVlanPvidTable=_Es2126PoEplusVlanPvidTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,3,1))
if mibBuilder.loadTexts:es2126PoEplusVlanPvidTable.setStatus(_A)
_Es2126PoEplusVlanPvidEntry_Object=MibTableRow
es2126PoEplusVlanPvidEntry=_Es2126PoEplusVlanPvidEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,3,1,1))
es2126PoEplusVlanPvidEntry.setIndexNames((0,_E,_l))
if mibBuilder.loadTexts:es2126PoEplusVlanPvidEntry.setStatus(_A)
class _Es2126PoEplusVlanPvidPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_Es2126PoEplusVlanPvidPort_Type.__name__=_B
_Es2126PoEplusVlanPvidPort_Object=MibTableColumn
es2126PoEplusVlanPvidPort=_Es2126PoEplusVlanPvidPort_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,3,1,1,1),_Es2126PoEplusVlanPvidPort_Type())
es2126PoEplusVlanPvidPort.setMaxAccess(_F)
if mibBuilder.loadTexts:es2126PoEplusVlanPvidPort.setStatus(_A)
class _Es2126PoEplusVlanPvidValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Es2126PoEplusVlanPvidValue_Type.__name__=_B
_Es2126PoEplusVlanPvidValue_Object=MibTableColumn
es2126PoEplusVlanPvidValue=_Es2126PoEplusVlanPvidValue_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,3,1,1,2),_Es2126PoEplusVlanPvidValue_Type())
es2126PoEplusVlanPvidValue.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusVlanPvidValue.setStatus(_A)
class _Es2126PoEplusVlanPvidDefaultPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Es2126PoEplusVlanPvidDefaultPriority_Type.__name__=_B
_Es2126PoEplusVlanPvidDefaultPriority_Object=MibTableColumn
es2126PoEplusVlanPvidDefaultPriority=_Es2126PoEplusVlanPvidDefaultPriority_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,3,1,1,3),_Es2126PoEplusVlanPvidDefaultPriority_Type())
es2126PoEplusVlanPvidDefaultPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusVlanPvidDefaultPriority.setStatus(_A)
class _Es2126PoEplusVlanPvidDropUntag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Es2126PoEplusVlanPvidDropUntag_Type.__name__=_B
_Es2126PoEplusVlanPvidDropUntag_Object=MibTableColumn
es2126PoEplusVlanPvidDropUntag=_Es2126PoEplusVlanPvidDropUntag_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,3,1,1,4),_Es2126PoEplusVlanPvidDropUntag_Type())
es2126PoEplusVlanPvidDropUntag.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusVlanPvidDropUntag.setStatus(_A)
_Es2126PoEplusPortBasedVlanGroup_ObjectIdentity=ObjectIdentity
es2126PoEplusPortBasedVlanGroup=_Es2126PoEplusPortBasedVlanGroup_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,17,4))
class _Es2126PoEplusPortBasedVlanNumbers_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_Es2126PoEplusPortBasedVlanNumbers_Type.__name__=_B
_Es2126PoEplusPortBasedVlanNumbers_Object=MibScalar
es2126PoEplusPortBasedVlanNumbers=_Es2126PoEplusPortBasedVlanNumbers_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,4,1),_Es2126PoEplusPortBasedVlanNumbers_Type())
es2126PoEplusPortBasedVlanNumbers.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPortBasedVlanNumbers.setStatus(_A)
class _Es2126PoEplusPortBasedCreateStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusPortBasedCreateStatus_Type.__name__=_B
_Es2126PoEplusPortBasedCreateStatus_Object=MibScalar
es2126PoEplusPortBasedCreateStatus=_Es2126PoEplusPortBasedCreateStatus_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,4,2),_Es2126PoEplusPortBasedCreateStatus_Type())
es2126PoEplusPortBasedCreateStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusPortBasedCreateStatus.setStatus(_A)
_Es2126PoEplusPortBasedVlanTable_Object=MibTable
es2126PoEplusPortBasedVlanTable=_Es2126PoEplusPortBasedVlanTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,4,3))
if mibBuilder.loadTexts:es2126PoEplusPortBasedVlanTable.setStatus(_A)
_Es2126PoEplusPortBasedVlanEntry_Object=MibTableRow
es2126PoEplusPortBasedVlanEntry=_Es2126PoEplusPortBasedVlanEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,4,3,1))
es2126PoEplusPortBasedVlanEntry.setIndexNames((0,_E,_m))
if mibBuilder.loadTexts:es2126PoEplusPortBasedVlanEntry.setStatus(_A)
class _Es2126PoEplusPortBasedVlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_Es2126PoEplusPortBasedVlanIndex_Type.__name__=_B
_Es2126PoEplusPortBasedVlanIndex_Object=MibTableColumn
es2126PoEplusPortBasedVlanIndex=_Es2126PoEplusPortBasedVlanIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,4,3,1,1),_Es2126PoEplusPortBasedVlanIndex_Type())
es2126PoEplusPortBasedVlanIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:es2126PoEplusPortBasedVlanIndex.setStatus(_A)
_Es2126PoEplusPortBasedVlanName_Type=DisplayString
_Es2126PoEplusPortBasedVlanName_Object=MibTableColumn
es2126PoEplusPortBasedVlanName=_Es2126PoEplusPortBasedVlanName_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,4,3,1,2),_Es2126PoEplusPortBasedVlanName_Type())
es2126PoEplusPortBasedVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusPortBasedVlanName.setStatus(_A)
_Es2126PoEplusPortBasedVlanMember_Type=DisplayString
_Es2126PoEplusPortBasedVlanMember_Object=MibTableColumn
es2126PoEplusPortBasedVlanMember=_Es2126PoEplusPortBasedVlanMember_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,4,3,1,3),_Es2126PoEplusPortBasedVlanMember_Type())
es2126PoEplusPortBasedVlanMember.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusPortBasedVlanMember.setStatus(_A)
class _Es2126PoEplusPortBasedVlanRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Es2126PoEplusPortBasedVlanRowStatus_Type.__name__=_B
_Es2126PoEplusPortBasedVlanRowStatus_Object=MibTableColumn
es2126PoEplusPortBasedVlanRowStatus=_Es2126PoEplusPortBasedVlanRowStatus_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,4,3,1,4),_Es2126PoEplusPortBasedVlanRowStatus_Type())
es2126PoEplusPortBasedVlanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusPortBasedVlanRowStatus.setStatus(_A)
_Es2126PoEplusManagementVlan_ObjectIdentity=ObjectIdentity
es2126PoEplusManagementVlan=_Es2126PoEplusManagementVlan_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,17,5))
class _Es2126PoEplusManagementVlanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusManagementVlanState_Type.__name__=_B
_Es2126PoEplusManagementVlanState_Object=MibScalar
es2126PoEplusManagementVlanState=_Es2126PoEplusManagementVlanState_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,5,1),_Es2126PoEplusManagementVlanState_Type())
es2126PoEplusManagementVlanState.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusManagementVlanState.setStatus(_A)
class _Es2126PoEplusManagementVlanVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Es2126PoEplusManagementVlanVid_Type.__name__=_B
_Es2126PoEplusManagementVlanVid_Object=MibScalar
es2126PoEplusManagementVlanVid=_Es2126PoEplusManagementVlanVid_Object((1,3,6,1,4,1,2356,800,2,2129,1,17,5,2),_Es2126PoEplusManagementVlanVid_Type())
es2126PoEplusManagementVlanVid.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusManagementVlanVid.setStatus(_A)
_Es2126PoEplusDot1X_ObjectIdentity=ObjectIdentity
es2126PoEplusDot1X=_Es2126PoEplusDot1X_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,18))
_Es2126PoEplusDot1XStateSetting_ObjectIdentity=ObjectIdentity
es2126PoEplusDot1XStateSetting=_Es2126PoEplusDot1XStateSetting_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,18,1))
_Es2126PoEplusRadiusServer_Type=IpAddress
_Es2126PoEplusRadiusServer_Object=MibScalar
es2126PoEplusRadiusServer=_Es2126PoEplusRadiusServer_Object((1,3,6,1,4,1,2356,800,2,2129,1,18,1,1),_Es2126PoEplusRadiusServer_Type())
es2126PoEplusRadiusServer.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusRadiusServer.setStatus(_A)
class _Es2126PoEplusDot1XPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Es2126PoEplusDot1XPort_Type.__name__=_B
_Es2126PoEplusDot1XPort_Object=MibScalar
es2126PoEplusDot1XPort=_Es2126PoEplusDot1XPort_Object((1,3,6,1,4,1,2356,800,2,2129,1,18,1,2),_Es2126PoEplusDot1XPort_Type())
es2126PoEplusDot1XPort.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDot1XPort.setStatus(_A)
_Es2126PoEplusSecretKey_Type=DisplayString
_Es2126PoEplusSecretKey_Object=MibScalar
es2126PoEplusSecretKey=_Es2126PoEplusSecretKey_Object((1,3,6,1,4,1,2356,800,2,2129,1,18,1,3),_Es2126PoEplusSecretKey_Type())
es2126PoEplusSecretKey.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusSecretKey.setStatus(_A)
class _Es2126PoEplusAccountingService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusAccountingService_Type.__name__=_B
_Es2126PoEplusAccountingService_Object=MibScalar
es2126PoEplusAccountingService=_Es2126PoEplusAccountingService_Object((1,3,6,1,4,1,2356,800,2,2129,1,18,1,4),_Es2126PoEplusAccountingService_Type())
es2126PoEplusAccountingService.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusAccountingService.setStatus(_A)
_Es2126PoEplusAccountingServer_Type=IpAddress
_Es2126PoEplusAccountingServer_Object=MibScalar
es2126PoEplusAccountingServer=_Es2126PoEplusAccountingServer_Object((1,3,6,1,4,1,2356,800,2,2129,1,18,1,5),_Es2126PoEplusAccountingServer_Type())
es2126PoEplusAccountingServer.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusAccountingServer.setStatus(_A)
class _Es2126PoEplusAccountingPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Es2126PoEplusAccountingPort_Type.__name__=_B
_Es2126PoEplusAccountingPort_Object=MibScalar
es2126PoEplusAccountingPort=_Es2126PoEplusAccountingPort_Object((1,3,6,1,4,1,2356,800,2,2129,1,18,1,6),_Es2126PoEplusAccountingPort_Type())
es2126PoEplusAccountingPort.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusAccountingPort.setStatus(_A)
_Es2126PoEplusDot1XPortSecurityManagement_ObjectIdentity=ObjectIdentity
es2126PoEplusDot1XPortSecurityManagement=_Es2126PoEplusDot1XPortSecurityManagement_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,18,2))
_Es2126PoEplusDot1XPortSecurityTable_Object=MibTable
es2126PoEplusDot1XPortSecurityTable=_Es2126PoEplusDot1XPortSecurityTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,18,2,1))
if mibBuilder.loadTexts:es2126PoEplusDot1XPortSecurityTable.setStatus(_A)
_Es2126PoEplusDot1XPortSecurityEntry_Object=MibTableRow
es2126PoEplusDot1XPortSecurityEntry=_Es2126PoEplusDot1XPortSecurityEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,18,2,1,1))
es2126PoEplusDot1XPortSecurityEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:es2126PoEplusDot1XPortSecurityEntry.setStatus(_A)
class _Es2126PoEplusDot1XPortSecurityPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_Es2126PoEplusDot1XPortSecurityPortIndex_Type.__name__=_B
_Es2126PoEplusDot1XPortSecurityPortIndex_Object=MibTableColumn
es2126PoEplusDot1XPortSecurityPortIndex=_Es2126PoEplusDot1XPortSecurityPortIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,18,2,1,1,1),_Es2126PoEplusDot1XPortSecurityPortIndex_Type())
es2126PoEplusDot1XPortSecurityPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:es2126PoEplusDot1XPortSecurityPortIndex.setStatus(_A)
class _Es2126PoEplusDot1XPortSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Es2126PoEplusDot1XPortSecurityMode_Type.__name__=_B
_Es2126PoEplusDot1XPortSecurityMode_Object=MibTableColumn
es2126PoEplusDot1XPortSecurityMode=_Es2126PoEplusDot1XPortSecurityMode_Object((1,3,6,1,4,1,2356,800,2,2129,1,18,2,1,1,2),_Es2126PoEplusDot1XPortSecurityMode_Type())
es2126PoEplusDot1XPortSecurityMode.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDot1XPortSecurityMode.setStatus(_A)
class _Es2126PoEplusDot1XPortSecurityPortControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Es2126PoEplusDot1XPortSecurityPortControl_Type.__name__=_B
_Es2126PoEplusDot1XPortSecurityPortControl_Object=MibTableColumn
es2126PoEplusDot1XPortSecurityPortControl=_Es2126PoEplusDot1XPortSecurityPortControl_Object((1,3,6,1,4,1,2356,800,2,2129,1,18,2,1,1,3),_Es2126PoEplusDot1XPortSecurityPortControl_Type())
es2126PoEplusDot1XPortSecurityPortControl.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDot1XPortSecurityPortControl.setStatus(_A)
class _Es2126PoEplusDot1XPortSecurityReAuthMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Es2126PoEplusDot1XPortSecurityReAuthMax_Type.__name__=_B
_Es2126PoEplusDot1XPortSecurityReAuthMax_Object=MibTableColumn
es2126PoEplusDot1XPortSecurityReAuthMax=_Es2126PoEplusDot1XPortSecurityReAuthMax_Object((1,3,6,1,4,1,2356,800,2,2129,1,18,2,1,1,4),_Es2126PoEplusDot1XPortSecurityReAuthMax_Type())
es2126PoEplusDot1XPortSecurityReAuthMax.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDot1XPortSecurityReAuthMax.setStatus(_A)
class _Es2126PoEplusDot1XPortSecurityTxPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Es2126PoEplusDot1XPortSecurityTxPeriod_Type.__name__=_B
_Es2126PoEplusDot1XPortSecurityTxPeriod_Object=MibTableColumn
es2126PoEplusDot1XPortSecurityTxPeriod=_Es2126PoEplusDot1XPortSecurityTxPeriod_Object((1,3,6,1,4,1,2356,800,2,2129,1,18,2,1,1,5),_Es2126PoEplusDot1XPortSecurityTxPeriod_Type())
es2126PoEplusDot1XPortSecurityTxPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDot1XPortSecurityTxPeriod.setStatus(_A)
class _Es2126PoEplusDot1XPortSecurityQuietPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Es2126PoEplusDot1XPortSecurityQuietPeriod_Type.__name__=_B
_Es2126PoEplusDot1XPortSecurityQuietPeriod_Object=MibTableColumn
es2126PoEplusDot1XPortSecurityQuietPeriod=_Es2126PoEplusDot1XPortSecurityQuietPeriod_Object((1,3,6,1,4,1,2356,800,2,2129,1,18,2,1,1,6),_Es2126PoEplusDot1XPortSecurityQuietPeriod_Type())
es2126PoEplusDot1XPortSecurityQuietPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDot1XPortSecurityQuietPeriod.setStatus(_A)
class _Es2126PoEplusDot1XPortSecurityReAuthEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusDot1XPortSecurityReAuthEnabled_Type.__name__=_B
_Es2126PoEplusDot1XPortSecurityReAuthEnabled_Object=MibTableColumn
es2126PoEplusDot1XPortSecurityReAuthEnabled=_Es2126PoEplusDot1XPortSecurityReAuthEnabled_Object((1,3,6,1,4,1,2356,800,2,2129,1,18,2,1,1,7),_Es2126PoEplusDot1XPortSecurityReAuthEnabled_Type())
es2126PoEplusDot1XPortSecurityReAuthEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDot1XPortSecurityReAuthEnabled.setStatus(_A)
class _Es2126PoEplusDot1XPortSecurityReAuthPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Es2126PoEplusDot1XPortSecurityReAuthPeriod_Type.__name__=_B
_Es2126PoEplusDot1XPortSecurityReAuthPeriod_Object=MibTableColumn
es2126PoEplusDot1XPortSecurityReAuthPeriod=_Es2126PoEplusDot1XPortSecurityReAuthPeriod_Object((1,3,6,1,4,1,2356,800,2,2129,1,18,2,1,1,8),_Es2126PoEplusDot1XPortSecurityReAuthPeriod_Type())
es2126PoEplusDot1XPortSecurityReAuthPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDot1XPortSecurityReAuthPeriod.setStatus(_A)
class _Es2126PoEplusDot1XPortSecurityMaxRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Es2126PoEplusDot1XPortSecurityMaxRequest_Type.__name__=_B
_Es2126PoEplusDot1XPortSecurityMaxRequest_Object=MibTableColumn
es2126PoEplusDot1XPortSecurityMaxRequest=_Es2126PoEplusDot1XPortSecurityMaxRequest_Object((1,3,6,1,4,1,2356,800,2,2129,1,18,2,1,1,9),_Es2126PoEplusDot1XPortSecurityMaxRequest_Type())
es2126PoEplusDot1XPortSecurityMaxRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDot1XPortSecurityMaxRequest.setStatus(_A)
class _Es2126PoEplusDot1XPortSecuritySuppTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Es2126PoEplusDot1XPortSecuritySuppTimeout_Type.__name__=_B
_Es2126PoEplusDot1XPortSecuritySuppTimeout_Object=MibTableColumn
es2126PoEplusDot1XPortSecuritySuppTimeout=_Es2126PoEplusDot1XPortSecuritySuppTimeout_Object((1,3,6,1,4,1,2356,800,2,2129,1,18,2,1,1,10),_Es2126PoEplusDot1XPortSecuritySuppTimeout_Type())
es2126PoEplusDot1XPortSecuritySuppTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDot1XPortSecuritySuppTimeout.setStatus(_A)
class _Es2126PoEplusDot1XPortSecurityServerTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Es2126PoEplusDot1XPortSecurityServerTimeout_Type.__name__=_B
_Es2126PoEplusDot1XPortSecurityServerTimeout_Object=MibTableColumn
es2126PoEplusDot1XPortSecurityServerTimeout=_Es2126PoEplusDot1XPortSecurityServerTimeout_Object((1,3,6,1,4,1,2356,800,2,2129,1,18,2,1,1,11),_Es2126PoEplusDot1XPortSecurityServerTimeout_Type())
es2126PoEplusDot1XPortSecurityServerTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusDot1XPortSecurityServerTimeout.setStatus(_A)
_Es2126PoEplusDot1XPortSecurityStatus_Type=DisplayString
_Es2126PoEplusDot1XPortSecurityStatus_Object=MibTableColumn
es2126PoEplusDot1XPortSecurityStatus=_Es2126PoEplusDot1XPortSecurityStatus_Object((1,3,6,1,4,1,2356,800,2,2129,1,18,2,1,1,12),_Es2126PoEplusDot1XPortSecurityStatus_Type())
es2126PoEplusDot1XPortSecurityStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusDot1XPortSecurityStatus.setStatus(_A)
_Es2126PoEplusTrunkInfo_ObjectIdentity=ObjectIdentity
es2126PoEplusTrunkInfo=_Es2126PoEplusTrunkInfo_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,19))
_Es2126PoEplusTrunkPort_ObjectIdentity=ObjectIdentity
es2126PoEplusTrunkPort=_Es2126PoEplusTrunkPort_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,19,1))
_Es2126PoEplusTrunkPortTable_Object=MibTable
es2126PoEplusTrunkPortTable=_Es2126PoEplusTrunkPortTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,19,1,1))
if mibBuilder.loadTexts:es2126PoEplusTrunkPortTable.setStatus(_A)
_Es2126PoEplusTrunkPortEntry_Object=MibTableRow
es2126PoEplusTrunkPortEntry=_Es2126PoEplusTrunkPortEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,19,1,1,1))
es2126PoEplusTrunkPortEntry.setIndexNames((0,_E,_o))
if mibBuilder.loadTexts:es2126PoEplusTrunkPortEntry.setStatus(_A)
class _Es2126PoEplusTrunkPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_Es2126PoEplusTrunkPortIndex_Type.__name__=_B
_Es2126PoEplusTrunkPortIndex_Object=MibTableColumn
es2126PoEplusTrunkPortIndex=_Es2126PoEplusTrunkPortIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,19,1,1,1,1),_Es2126PoEplusTrunkPortIndex_Type())
es2126PoEplusTrunkPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:es2126PoEplusTrunkPortIndex.setStatus(_A)
class _Es2126PoEplusTrunkPortMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Es2126PoEplusTrunkPortMethod_Type.__name__=_B
_Es2126PoEplusTrunkPortMethod_Object=MibTableColumn
es2126PoEplusTrunkPortMethod=_Es2126PoEplusTrunkPortMethod_Object((1,3,6,1,4,1,2356,800,2,2129,1,19,1,1,1,2),_Es2126PoEplusTrunkPortMethod_Type())
es2126PoEplusTrunkPortMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusTrunkPortMethod.setStatus(_A)
class _Es2126PoEplusTrunkPortGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Es2126PoEplusTrunkPortGroup_Type.__name__=_B
_Es2126PoEplusTrunkPortGroup_Object=MibTableColumn
es2126PoEplusTrunkPortGroup=_Es2126PoEplusTrunkPortGroup_Object((1,3,6,1,4,1,2356,800,2,2129,1,19,1,1,1,3),_Es2126PoEplusTrunkPortGroup_Type())
es2126PoEplusTrunkPortGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusTrunkPortGroup.setStatus(_A)
class _Es2126PoEplusTrunkPortActiveLacp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusTrunkPortActiveLacp_Type.__name__=_B
_Es2126PoEplusTrunkPortActiveLacp_Object=MibTableColumn
es2126PoEplusTrunkPortActiveLacp=_Es2126PoEplusTrunkPortActiveLacp_Object((1,3,6,1,4,1,2356,800,2,2129,1,19,1,1,1,4),_Es2126PoEplusTrunkPortActiveLacp_Type())
es2126PoEplusTrunkPortActiveLacp.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusTrunkPortActiveLacp.setStatus(_A)
class _Es2126PoEplusTrunkPortAggtr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_Es2126PoEplusTrunkPortAggtr_Type.__name__=_B
_Es2126PoEplusTrunkPortAggtr_Object=MibTableColumn
es2126PoEplusTrunkPortAggtr=_Es2126PoEplusTrunkPortAggtr_Object((1,3,6,1,4,1,2356,800,2,2129,1,19,1,1,1,5),_Es2126PoEplusTrunkPortAggtr_Type())
es2126PoEplusTrunkPortAggtr.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusTrunkPortAggtr.setStatus(_A)
class _Es2126PoEplusTrunkPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusTrunkPortStatus_Type.__name__=_B
_Es2126PoEplusTrunkPortStatus_Object=MibTableColumn
es2126PoEplusTrunkPortStatus=_Es2126PoEplusTrunkPortStatus_Object((1,3,6,1,4,1,2356,800,2,2129,1,19,1,1,1,6),_Es2126PoEplusTrunkPortStatus_Type())
es2126PoEplusTrunkPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusTrunkPortStatus.setStatus(_A)
class _Es2126PoEplusTrunkPortCurrentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Es2126PoEplusTrunkPortCurrentMode_Type.__name__=_B
_Es2126PoEplusTrunkPortCurrentMode_Object=MibTableColumn
es2126PoEplusTrunkPortCurrentMode=_Es2126PoEplusTrunkPortCurrentMode_Object((1,3,6,1,4,1,2356,800,2,2129,1,19,1,1,1,7),_Es2126PoEplusTrunkPortCurrentMode_Type())
es2126PoEplusTrunkPortCurrentMode.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusTrunkPortCurrentMode.setStatus(_A)
_Es2126PoEplusAggregatorView_ObjectIdentity=ObjectIdentity
es2126PoEplusAggregatorView=_Es2126PoEplusAggregatorView_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,19,2))
_Es2126PoEplusAggregatorViewTable_Object=MibTable
es2126PoEplusAggregatorViewTable=_Es2126PoEplusAggregatorViewTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,19,2,1))
if mibBuilder.loadTexts:es2126PoEplusAggregatorViewTable.setStatus(_A)
_Es2126PoEplusAggregatorViewEntry_Object=MibTableRow
es2126PoEplusAggregatorViewEntry=_Es2126PoEplusAggregatorViewEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,19,2,1,1))
es2126PoEplusAggregatorViewEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:es2126PoEplusAggregatorViewEntry.setStatus(_A)
class _Es2126PoEplusAggregatorViewIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_Es2126PoEplusAggregatorViewIndex_Type.__name__=_B
_Es2126PoEplusAggregatorViewIndex_Object=MibTableColumn
es2126PoEplusAggregatorViewIndex=_Es2126PoEplusAggregatorViewIndex_Object((1,3,6,1,4,1,2356,800,2,2129,1,19,2,1,1,1),_Es2126PoEplusAggregatorViewIndex_Type())
es2126PoEplusAggregatorViewIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:es2126PoEplusAggregatorViewIndex.setStatus(_A)
class _Es2126PoEplusAggregatorViewMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Es2126PoEplusAggregatorViewMethod_Type.__name__=_B
_Es2126PoEplusAggregatorViewMethod_Object=MibTableColumn
es2126PoEplusAggregatorViewMethod=_Es2126PoEplusAggregatorViewMethod_Object((1,3,6,1,4,1,2356,800,2,2129,1,19,2,1,1,2),_Es2126PoEplusAggregatorViewMethod_Type())
es2126PoEplusAggregatorViewMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusAggregatorViewMethod.setStatus(_A)
_Es2126PoEplusAggregatorViewMemberPorts_Type=DisplayString
_Es2126PoEplusAggregatorViewMemberPorts_Object=MibTableColumn
es2126PoEplusAggregatorViewMemberPorts=_Es2126PoEplusAggregatorViewMemberPorts_Object((1,3,6,1,4,1,2356,800,2,2129,1,19,2,1,1,3),_Es2126PoEplusAggregatorViewMemberPorts_Type())
es2126PoEplusAggregatorViewMemberPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusAggregatorViewMemberPorts.setStatus(_A)
_Es2126PoEplusAggregatorViewReadyPorts_Type=DisplayString
_Es2126PoEplusAggregatorViewReadyPorts_Object=MibTableColumn
es2126PoEplusAggregatorViewReadyPorts=_Es2126PoEplusAggregatorViewReadyPorts_Object((1,3,6,1,4,1,2356,800,2,2129,1,19,2,1,1,4),_Es2126PoEplusAggregatorViewReadyPorts_Type())
es2126PoEplusAggregatorViewReadyPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusAggregatorViewReadyPorts.setStatus(_A)
_Es2126PoEplusLacpSystemConfiguration_ObjectIdentity=ObjectIdentity
es2126PoEplusLacpSystemConfiguration=_Es2126PoEplusLacpSystemConfiguration_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,19,3))
class _Es2126PoEplusLacpSystemPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Es2126PoEplusLacpSystemPriority_Type.__name__=_B
_Es2126PoEplusLacpSystemPriority_Object=MibScalar
es2126PoEplusLacpSystemPriority=_Es2126PoEplusLacpSystemPriority_Object((1,3,6,1,4,1,2356,800,2,2129,1,19,3,1),_Es2126PoEplusLacpSystemPriority_Type())
es2126PoEplusLacpSystemPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusLacpSystemPriority.setStatus(_A)
class _Es2126PoEplusLacpSystemHashMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Es2126PoEplusLacpSystemHashMethod_Type.__name__=_B
_Es2126PoEplusLacpSystemHashMethod_Object=MibScalar
es2126PoEplusLacpSystemHashMethod=_Es2126PoEplusLacpSystemHashMethod_Object((1,3,6,1,4,1,2356,800,2,2129,1,19,3,2),_Es2126PoEplusLacpSystemHashMethod_Type())
es2126PoEplusLacpSystemHashMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusLacpSystemHashMethod.setStatus(_A)
_Es2126PoEplusTrapEntry_ObjectIdentity=ObjectIdentity
es2126PoEplusTrapEntry=_Es2126PoEplusTrapEntry_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,20))
_Es2126PoEplusTrapVariable_ObjectIdentity=ObjectIdentity
es2126PoEplusTrapVariable=_Es2126PoEplusTrapVariable_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,21))
_Username_Type=DisplayString
_Username_Object=MibScalar
username=_Username_Object((1,3,6,1,4,1,2356,800,2,2129,1,21,1),_Username_Type())
username.setMaxAccess(_D)
if mibBuilder.loadTexts:username.setStatus(_A)
class _GroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_GroupId_Type.__name__=_B
_GroupId_Object=MibScalar
groupId=_GroupId_Object((1,3,6,1,4,1,2356,800,2,2129,1,21,2),_GroupId_Type())
groupId.setMaxAccess(_D)
if mibBuilder.loadTexts:groupId.setStatus(_A)
class _Actorkey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Actorkey_Type.__name__=_B
_Actorkey_Object=MibScalar
actorkey=_Actorkey_Object((1,3,6,1,4,1,2356,800,2,2129,1,21,3),_Actorkey_Type())
actorkey.setMaxAccess(_D)
if mibBuilder.loadTexts:actorkey.setStatus(_A)
class _Partnerkey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Partnerkey_Type.__name__=_B
_Partnerkey_Object=MibScalar
partnerkey=_Partnerkey_Object((1,3,6,1,4,1,2356,800,2,2129,1,21,4),_Partnerkey_Type())
partnerkey.setMaxAccess(_D)
if mibBuilder.loadTexts:partnerkey.setStatus(_A)
_Uplink_Type=DisplayString
_Uplink_Object=MibScalar
uplink=_Uplink_Object((1,3,6,1,4,1,2356,800,2,2129,1,21,5),_Uplink_Type())
uplink.setMaxAccess(_D)
if mibBuilder.loadTexts:uplink.setStatus(_A)
_LoginProtectInfo_Type=DisplayString
_LoginProtectInfo_Object=MibScalar
loginProtectInfo=_LoginProtectInfo_Object((1,3,6,1,4,1,2356,800,2,2129,1,21,6),_LoginProtectInfo_Type())
loginProtectInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:loginProtectInfo.setStatus(_A)
_Es2126PoEplusPoE_ObjectIdentity=ObjectIdentity
es2126PoEplusPoE=_Es2126PoEplusPoE_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,22))
_Es2126PoEplusPoEStatus_ObjectIdentity=ObjectIdentity
es2126PoEplusPoEStatus=_Es2126PoEplusPoEStatus_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,22,1))
_Es2126PoEplusPoEStatusVmain_Type=DisplayString
_Es2126PoEplusPoEStatusVmain_Object=MibScalar
es2126PoEplusPoEStatusVmain=_Es2126PoEplusPoEStatusVmain_Object((1,3,6,1,4,1,2356,800,2,2129,1,22,1,1),_Es2126PoEplusPoEStatusVmain_Type())
es2126PoEplusPoEStatusVmain.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPoEStatusVmain.setStatus(_A)
_Es2126PoEplusPoEStatusImain_Type=DisplayString
_Es2126PoEplusPoEStatusImain_Object=MibScalar
es2126PoEplusPoEStatusImain=_Es2126PoEplusPoEStatusImain_Object((1,3,6,1,4,1,2356,800,2,2129,1,22,1,2),_Es2126PoEplusPoEStatusImain_Type())
es2126PoEplusPoEStatusImain.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPoEStatusImain.setStatus(_A)
_Es2126PoEplusPoEStatusPconsume_Type=DisplayString
_Es2126PoEplusPoEStatusPconsume_Object=MibScalar
es2126PoEplusPoEStatusPconsume=_Es2126PoEplusPoEStatusPconsume_Object((1,3,6,1,4,1,2356,800,2,2129,1,22,1,3),_Es2126PoEplusPoEStatusPconsume_Type())
es2126PoEplusPoEStatusPconsume.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPoEStatusPconsume.setStatus(_A)
_Es2126PoEplusPoEStatusPowerLimit_Type=DisplayString
_Es2126PoEplusPoEStatusPowerLimit_Object=MibScalar
es2126PoEplusPoEStatusPowerLimit=_Es2126PoEplusPoEStatusPowerLimit_Object((1,3,6,1,4,1,2356,800,2,2129,1,22,1,4),_Es2126PoEplusPoEStatusPowerLimit_Type())
es2126PoEplusPoEStatusPowerLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPoEStatusPowerLimit.setStatus(_A)
_Es2126PoEplusPoEStatusTemperature_Type=DisplayString
_Es2126PoEplusPoEStatusTemperature_Object=MibScalar
es2126PoEplusPoEStatusTemperature=_Es2126PoEplusPoEStatusTemperature_Object((1,3,6,1,4,1,2356,800,2,2129,1,22,1,5),_Es2126PoEplusPoEStatusTemperature_Type())
es2126PoEplusPoEStatusTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPoEStatusTemperature.setStatus(_A)
_Es2126PoEplusPoEStatusTable_Object=MibTable
es2126PoEplusPoEStatusTable=_Es2126PoEplusPoEStatusTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,22,1,6))
if mibBuilder.loadTexts:es2126PoEplusPoEStatusTable.setStatus(_A)
_Es2126PoEplusPoEStatusEntry_Object=MibTableRow
es2126PoEplusPoEStatusEntry=_Es2126PoEplusPoEStatusEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,22,1,6,1))
es2126PoEplusPoEStatusEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:es2126PoEplusPoEStatusEntry.setStatus(_A)
class _Es2126PoEplusPoEStatusPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Es2126PoEplusPoEStatusPortNum_Type.__name__=_B
_Es2126PoEplusPoEStatusPortNum_Object=MibTableColumn
es2126PoEplusPoEStatusPortNum=_Es2126PoEplusPoEStatusPortNum_Object((1,3,6,1,4,1,2356,800,2,2129,1,22,1,6,1,1),_Es2126PoEplusPoEStatusPortNum_Type())
es2126PoEplusPoEStatusPortNum.setMaxAccess(_F)
if mibBuilder.loadTexts:es2126PoEplusPoEStatusPortNum.setStatus(_A)
class _Es2126PoEplusPoEStatusPortOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusPoEStatusPortOn_Type.__name__=_B
_Es2126PoEplusPoEStatusPortOn_Object=MibTableColumn
es2126PoEplusPoEStatusPortOn=_Es2126PoEplusPoEStatusPortOn_Object((1,3,6,1,4,1,2356,800,2,2129,1,22,1,6,1,2),_Es2126PoEplusPoEStatusPortOn_Type())
es2126PoEplusPoEStatusPortOn.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPoEStatusPortOn.setStatus(_A)
class _Es2126PoEplusPoEStatusACPortOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(8,8))
_Es2126PoEplusPoEStatusACPortOff_Type.__name__=_B
_Es2126PoEplusPoEStatusACPortOff_Object=MibTableColumn
es2126PoEplusPoEStatusACPortOff=_Es2126PoEplusPoEStatusACPortOff_Object((1,3,6,1,4,1,2356,800,2,2129,1,22,1,6,1,3),_Es2126PoEplusPoEStatusACPortOff_Type())
es2126PoEplusPoEStatusACPortOff.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPoEStatusACPortOff.setStatus(_A)
class _Es2126PoEplusPoEStatusDCPortOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusPoEStatusDCPortOff_Type.__name__=_B
_Es2126PoEplusPoEStatusDCPortOff_Object=MibTableColumn
es2126PoEplusPoEStatusDCPortOff=_Es2126PoEplusPoEStatusDCPortOff_Object((1,3,6,1,4,1,2356,800,2,2129,1,22,1,6,1,4),_Es2126PoEplusPoEStatusDCPortOff_Type())
es2126PoEplusPoEStatusDCPortOff.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPoEStatusDCPortOff.setStatus(_A)
class _Es2126PoEplusPoEStatusOverloadPortOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(32,32))
_Es2126PoEplusPoEStatusOverloadPortOff_Type.__name__=_B
_Es2126PoEplusPoEStatusOverloadPortOff_Object=MibTableColumn
es2126PoEplusPoEStatusOverloadPortOff=_Es2126PoEplusPoEStatusOverloadPortOff_Object((1,3,6,1,4,1,2356,800,2,2129,1,22,1,6,1,5),_Es2126PoEplusPoEStatusOverloadPortOff_Type())
es2126PoEplusPoEStatusOverloadPortOff.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPoEStatusOverloadPortOff.setStatus(_A)
class _Es2126PoEplusPoEStatusShortCircuitPortOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusPoEStatusShortCircuitPortOff_Type.__name__=_B
_Es2126PoEplusPoEStatusShortCircuitPortOff_Object=MibTableColumn
es2126PoEplusPoEStatusShortCircuitPortOff=_Es2126PoEplusPoEStatusShortCircuitPortOff_Object((1,3,6,1,4,1,2356,800,2,2129,1,22,1,6,1,6),_Es2126PoEplusPoEStatusShortCircuitPortOff_Type())
es2126PoEplusPoEStatusShortCircuitPortOff.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPoEStatusShortCircuitPortOff.setStatus(_A)
class _Es2126PoEplusPoEStatusOverTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusPoEStatusOverTemperature_Type.__name__=_B
_Es2126PoEplusPoEStatusOverTemperature_Object=MibTableColumn
es2126PoEplusPoEStatusOverTemperature=_Es2126PoEplusPoEStatusOverTemperature_Object((1,3,6,1,4,1,2356,800,2,2129,1,22,1,6,1,7),_Es2126PoEplusPoEStatusOverTemperature_Type())
es2126PoEplusPoEStatusOverTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPoEStatusOverTemperature.setStatus(_A)
class _Es2126PoEplusPoEStatusPowerManagePortOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusPoEStatusPowerManagePortOff_Type.__name__=_B
_Es2126PoEplusPoEStatusPowerManagePortOff_Object=MibTableColumn
es2126PoEplusPoEStatusPowerManagePortOff=_Es2126PoEplusPoEStatusPowerManagePortOff_Object((1,3,6,1,4,1,2356,800,2,2129,1,22,1,6,1,8),_Es2126PoEplusPoEStatusPowerManagePortOff_Type())
es2126PoEplusPoEStatusPowerManagePortOff.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPoEStatusPowerManagePortOff.setStatus(_A)
_Es2126PoEplusPoEConfTable_Object=MibTable
es2126PoEplusPoEConfTable=_Es2126PoEplusPoEConfTable_Object((1,3,6,1,4,1,2356,800,2,2129,1,22,2))
if mibBuilder.loadTexts:es2126PoEplusPoEConfTable.setStatus(_A)
_Es2126PoEplusPoEConfEntry_Object=MibTableRow
es2126PoEplusPoEConfEntry=_Es2126PoEplusPoEConfEntry_Object((1,3,6,1,4,1,2356,800,2,2129,1,22,2,1))
es2126PoEplusPoEConfEntry.setIndexNames((0,_E,_r))
if mibBuilder.loadTexts:es2126PoEplusPoEConfEntry.setStatus(_A)
class _Es2126PoEplusPoEConfPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_Es2126PoEplusPoEConfPortNum_Type.__name__=_B
_Es2126PoEplusPoEConfPortNum_Object=MibTableColumn
es2126PoEplusPoEConfPortNum=_Es2126PoEplusPoEConfPortNum_Object((1,3,6,1,4,1,2356,800,2,2129,1,22,2,1,1),_Es2126PoEplusPoEConfPortNum_Type())
es2126PoEplusPoEConfPortNum.setMaxAccess(_F)
if mibBuilder.loadTexts:es2126PoEplusPoEConfPortNum.setStatus(_A)
class _Es2126PoEplusPoEConfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusPoEConfStatus_Type.__name__=_B
_Es2126PoEplusPoEConfStatus_Object=MibTableColumn
es2126PoEplusPoEConfStatus=_Es2126PoEplusPoEConfStatus_Object((1,3,6,1,4,1,2356,800,2,2129,1,22,2,1,2),_Es2126PoEplusPoEConfStatus_Type())
es2126PoEplusPoEConfStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPoEConfStatus.setStatus(_A)
class _Es2126PoEplusPoEConfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PoEplusPoEConfState_Type.__name__=_B
_Es2126PoEplusPoEConfState_Object=MibTableColumn
es2126PoEplusPoEConfState=_Es2126PoEplusPoEConfState_Object((1,3,6,1,4,1,2356,800,2,2129,1,22,2,1,3),_Es2126PoEplusPoEConfState_Type())
es2126PoEplusPoEConfState.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusPoEConfState.setStatus(_A)
class _Es2126PoEplusPoEConfPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Es2126PoEplusPoEConfPriority_Type.__name__=_B
_Es2126PoEplusPoEConfPriority_Object=MibTableColumn
es2126PoEplusPoEConfPriority=_Es2126PoEplusPoEConfPriority_Object((1,3,6,1,4,1,2356,800,2,2129,1,22,2,1,4),_Es2126PoEplusPoEConfPriority_Type())
es2126PoEplusPoEConfPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusPoEConfPriority.setStatus(_A)
_Es2126PoEplusPoEConfPower_Type=DisplayString
_Es2126PoEplusPoEConfPower_Object=MibTableColumn
es2126PoEplusPoEConfPower=_Es2126PoEplusPoEConfPower_Object((1,3,6,1,4,1,2356,800,2,2129,1,22,2,1,5),_Es2126PoEplusPoEConfPower_Type())
es2126PoEplusPoEConfPower.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPoEConfPower.setStatus(_A)
class _Es2126PoEplusPoEConfCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Es2126PoEplusPoEConfCurrent_Type.__name__=_B
_Es2126PoEplusPoEConfCurrent_Object=MibTableColumn
es2126PoEplusPoEConfCurrent=_Es2126PoEplusPoEConfCurrent_Object((1,3,6,1,4,1,2356,800,2,2129,1,22,2,1,6),_Es2126PoEplusPoEConfCurrent_Type())
es2126PoEplusPoEConfCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPoEConfCurrent.setStatus(_A)
class _Es2126PoEplusPoEConfClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Es2126PoEplusPoEConfClass_Type.__name__=_B
_Es2126PoEplusPoEConfClass_Object=MibTableColumn
es2126PoEplusPoEConfClass=_Es2126PoEplusPoEConfClass_Object((1,3,6,1,4,1,2356,800,2,2129,1,22,2,1,7),_Es2126PoEplusPoEConfClass_Type())
es2126PoEplusPoEConfClass.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PoEplusPoEConfClass.setStatus(_A)
_Es2126PoEplusLoginProtect_ObjectIdentity=ObjectIdentity
es2126PoEplusLoginProtect=_Es2126PoEplusLoginProtect_ObjectIdentity((1,3,6,1,4,1,2356,800,2,2129,1,23))
class _Es2126PoEplusLockMinutes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_Es2126PoEplusLockMinutes_Type.__name__=_B
_Es2126PoEplusLockMinutes_Object=MibScalar
es2126PoEplusLockMinutes=_Es2126PoEplusLockMinutes_Object((1,3,6,1,4,1,2356,800,2,2129,1,23,1),_Es2126PoEplusLockMinutes_Type())
es2126PoEplusLockMinutes.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusLockMinutes.setStatus(_A)
class _Es2126PoEplusLoginErrors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_Es2126PoEplusLoginErrors_Type.__name__=_B
_Es2126PoEplusLoginErrors_Object=MibScalar
es2126PoEplusLoginErrors=_Es2126PoEplusLoginErrors_Object((1,3,6,1,4,1,2356,800,2,2129,1,23,2),_Es2126PoEplusLoginErrors_Type())
es2126PoEplusLoginErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:es2126PoEplusLoginErrors.setStatus(_A)
es2126PoEplusModuleInserted=NotificationType((1,3,6,1,4,1,2356,800,2,2129,1,20,1))
es2126PoEplusModuleInserted.setObjects((_G,_H))
if mibBuilder.loadTexts:es2126PoEplusModuleInserted.setStatus(_A)
es2126PoEplusModuleRemoved=NotificationType((1,3,6,1,4,1,2356,800,2,2129,1,20,2))
es2126PoEplusModuleRemoved.setObjects((_G,_H))
if mibBuilder.loadTexts:es2126PoEplusModuleRemoved.setStatus(_A)
es2126PoEplusDualMediaSwapped=NotificationType((1,3,6,1,4,1,2356,800,2,2129,1,20,3))
es2126PoEplusDualMediaSwapped.setObjects((_G,_H))
if mibBuilder.loadTexts:es2126PoEplusDualMediaSwapped.setStatus(_A)
es2126PoEplusPoEFailure=NotificationType((1,3,6,1,4,1,2356,800,2,2129,1,20,4))
if mibBuilder.loadTexts:es2126PoEplusPoEFailure.setStatus(_A)
es2126PoEplusLoopDetected=NotificationType((1,3,6,1,4,1,2356,800,2,2129,1,20,5))
es2126PoEplusLoopDetected.setObjects((_G,_H))
if mibBuilder.loadTexts:es2126PoEplusLoopDetected.setStatus(_A)
es2126PoEplusLoginProtected=NotificationType((1,3,6,1,4,1,2356,800,2,2129,1,20,6))
es2126PoEplusLoginProtected.setObjects((_G,_H))
if mibBuilder.loadTexts:es2126PoEplusLoginProtected.setStatus(_A)
es2126PoEplusStpStateDisabled=NotificationType((1,3,6,1,4,1,2356,800,2,2129,1,20,100))
if mibBuilder.loadTexts:es2126PoEplusStpStateDisabled.setStatus(_A)
es2126PoEplusStpStateEnabled=NotificationType((1,3,6,1,4,1,2356,800,2,2129,1,20,101))
if mibBuilder.loadTexts:es2126PoEplusStpStateEnabled.setStatus(_A)
es2126PoEplusStpTopologyChanged=NotificationType((1,3,6,1,4,1,2356,800,2,2129,1,20,102))
es2126PoEplusStpTopologyChanged.setObjects((_G,_H))
if mibBuilder.loadTexts:es2126PoEplusStpTopologyChanged.setStatus(_A)
es2126PoEplusRmonRisingAlarm=NotificationType((1,3,6,1,4,1,2356,800,2,2129,1,20,110))
if mibBuilder.loadTexts:es2126PoEplusRmonRisingAlarm.setStatus(_A)
es2126PoEplusRmonFallingAlarm=NotificationType((1,3,6,1,4,1,2356,800,2,2129,1,20,111))
if mibBuilder.loadTexts:es2126PoEplusRmonFallingAlarm.setStatus(_A)
es2126PoEplusLacpStateDisabled=NotificationType((1,3,6,1,4,1,2356,800,2,2129,1,20,120))
es2126PoEplusLacpStateDisabled.setObjects(*((_G,_H),(_E,_I)))
if mibBuilder.loadTexts:es2126PoEplusLacpStateDisabled.setStatus(_A)
es2126PoEplusLacpStateEnabled=NotificationType((1,3,6,1,4,1,2356,800,2,2129,1,20,121))
es2126PoEplusLacpStateEnabled.setObjects(*((_G,_H),(_E,_I)))
if mibBuilder.loadTexts:es2126PoEplusLacpStateEnabled.setStatus(_A)
es2126PoEplusLacpPortAdded=NotificationType((1,3,6,1,4,1,2356,800,2,2129,1,20,123))
es2126PoEplusLacpPortAdded.setObjects(*((_G,_H),(_E,_J),(_E,_K)))
if mibBuilder.loadTexts:es2126PoEplusLacpPortAdded.setStatus(_A)
es2126PoEplusLacpPortTrunkFailure=NotificationType((1,3,6,1,4,1,2356,800,2,2129,1,20,124))
es2126PoEplusLacpPortTrunkFailure.setObjects(*((_G,_H),(_E,_J),(_E,_K)))
if mibBuilder.loadTexts:es2126PoEplusLacpPortTrunkFailure.setStatus(_A)
es2126PoEplusGvrpStateDisabled=NotificationType((1,3,6,1,4,1,2356,800,2,2129,1,20,140))
if mibBuilder.loadTexts:es2126PoEplusGvrpStateDisabled.setStatus(_A)
es2126PoEplusGvrpStateEnabled=NotificationType((1,3,6,1,4,1,2356,800,2,2129,1,20,141))
if mibBuilder.loadTexts:es2126PoEplusGvrpStateEnabled.setStatus(_A)
es2126PoEplusVlanPortBaseEnabled=NotificationType((1,3,6,1,4,1,2356,800,2,2129,1,20,151))
if mibBuilder.loadTexts:es2126PoEplusVlanPortBaseEnabled.setStatus(_A)
es2126PoEplusVlanTagBaseEnabled=NotificationType((1,3,6,1,4,1,2356,800,2,2129,1,20,152))
if mibBuilder.loadTexts:es2126PoEplusVlanTagBaseEnabled.setStatus(_A)
es2126PoEplusVlanMetroBaseEnabled=NotificationType((1,3,6,1,4,1,2356,800,2,2129,1,20,153))
if mibBuilder.loadTexts:es2126PoEplusVlanMetroBaseEnabled.setStatus(_A)
es2126PoEplusUserLogin=NotificationType((1,3,6,1,4,1,2356,800,2,2129,1,20,200))
es2126PoEplusUserLogin.setObjects((_E,_L))
if mibBuilder.loadTexts:es2126PoEplusUserLogin.setStatus(_A)
es2126PoEplusUserLogout=NotificationType((1,3,6,1,4,1,2356,800,2,2129,1,20,201))
es2126PoEplusUserLogout.setObjects((_E,_L))
if mibBuilder.loadTexts:es2126PoEplusUserLogout.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'lancomSystems':lancomSystems,'switchingSystems':switchingSystems,'fastEthernetSwitches':fastEthernetSwitches,'lancomES2126P':lancomES2126P,'es2126PoEplusProduces':es2126PoEplusProduces,'es2126PoEplusSystem':es2126PoEplusSystem,'es2126PoEplusCommonSys':es2126PoEplusCommonSys,'es2126PoEplusReboot':es2126PoEplusReboot,'es2126PoEplusBiosVsersion':es2126PoEplusBiosVsersion,'es2126PoEplusFirmwareVersion':es2126PoEplusFirmwareVersion,'es2126PoEplusHardwareVersion':es2126PoEplusHardwareVersion,'es2126PoEplusMechanicalVersion':es2126PoEplusMechanicalVersion,'es2126PoEplusSerialNumber':es2126PoEplusSerialNumber,'es2126PoEplusHostMacAddress':es2126PoEplusHostMacAddress,'es2126PoEplusDevicePort':es2126PoEplusDevicePort,'es2126PoEplusRamSize':es2126PoEplusRamSize,'es2126PoEplusFlashSize':es2126PoEplusFlashSize,'es2126PoEplusSystemDescription':es2126PoEplusSystemDescription,'es2126PoEplusDeviceName':es2126PoEplusDeviceName,'es2126PoEplusIP':es2126PoEplusIP,'es2126PoEplusDhcpSetting':es2126PoEplusDhcpSetting,'es2126PoEplusIPAddress':es2126PoEplusIPAddress,'es2126PoEplusNetMask':es2126PoEplusNetMask,'es2126PoEplusDefaultGateway':es2126PoEplusDefaultGateway,'es2126PoEplusDnsSetting':es2126PoEplusDnsSetting,'es2126PoEplusDnsServer':es2126PoEplusDnsServer,'es2126PoEplusTime':es2126PoEplusTime,'es2126PoEplusSystemCurrentTime':es2126PoEplusSystemCurrentTime,'es2126PoEplusManualTimeSetting':es2126PoEplusManualTimeSetting,'es2126PoEplusNTPServer':es2126PoEplusNTPServer,'es2126PoEplusNTPTimeZone':es2126PoEplusNTPTimeZone,'es2126PoEplusNTPTimeSync':es2126PoEplusNTPTimeSync,'es2126PoEplusDaylightSavingTime':es2126PoEplusDaylightSavingTime,'es2126PoEplusDaylightStartTime':es2126PoEplusDaylightStartTime,'es2126PoEplusDaylightEndTime':es2126PoEplusDaylightEndTime,'es2126PoEplusAccount':es2126PoEplusAccount,'es2126PoEplusAccountNumber':es2126PoEplusAccountNumber,'es2126PoEplusAccountTable':es2126PoEplusAccountTable,'es2126PoEplusAccountEntry':es2126PoEplusAccountEntry,_M:es2126PoEplusAccountIndex,'es2126PoEplusAccountAuthorization':es2126PoEplusAccountAuthorization,'es2126PoEplusAccountName':es2126PoEplusAccountName,'es2126PoEplusAccountPassword':es2126PoEplusAccountPassword,'es2126PoEplusAccountAddName':es2126PoEplusAccountAddName,'es2126PoEplusAccountAddPassword':es2126PoEplusAccountAddPassword,'es2126PoEplusDoAccountAdd':es2126PoEplusDoAccountAdd,'es2126PoEplusAccountDel':es2126PoEplusAccountDel,'es2126PoEplusSnmp':es2126PoEplusSnmp,'es2126PoEplusGetCommunity':es2126PoEplusGetCommunity,'es2126PoEplusSetCommunity':es2126PoEplusSetCommunity,'es2126PoEplusTrapHostNumber':es2126PoEplusTrapHostNumber,'es2126PoEplusTrapHostTable':es2126PoEplusTrapHostTable,'es2126PoEplusTrapHostEntry':es2126PoEplusTrapHostEntry,_N:es2126PoEplusTrapHostIndex,'es2126PoEplusTrapHostIP':es2126PoEplusTrapHostIP,'es2126PoEplusTrapHostPort':es2126PoEplusTrapHostPort,'es2126PoEplusTrapHostCommunity':es2126PoEplusTrapHostCommunity,'es2126PoEplusRegisterMonitor':es2126PoEplusRegisterMonitor,'es2126PoEplusDeleteMonitor':es2126PoEplusDeleteMonitor,'es2126PoEplusMonitorTable':es2126PoEplusMonitorTable,'es2126PoEplusMonitorEntry':es2126PoEplusMonitorEntry,_O:es2126PoEplusMonitorTableIp,'es2126PoEplusMonitorTableMac':es2126PoEplusMonitorTableMac,'es2126PoEplusTrapBootDelayTime':es2126PoEplusTrapBootDelayTime,'es2126PoEplusAlarm':es2126PoEplusAlarm,'es2126PoEplusEvent':es2126PoEplusEvent,'es2126PoEplusEventNumber':es2126PoEplusEventNumber,'es2126PoEplusEventTable':es2126PoEplusEventTable,'es2126PoEplusEventEntry':es2126PoEplusEventEntry,_P:es2126PoEplusEventIndex,'es2126PoEplusEventName':es2126PoEplusEventName,'es2126PoEplusEventSendEmail':es2126PoEplusEventSendEmail,'es2126PoEplusEventSendTrap':es2126PoEplusEventSendTrap,'es2126PoEplusEmail':es2126PoEplusEmail,'es2126PoEplusEmailServer':es2126PoEplusEmailServer,'es2126PoEplusEmailUsername':es2126PoEplusEmailUsername,'es2126PoEplusEmailPassword':es2126PoEplusEmailPassword,'es2126PoEplusEmailSender':es2126PoEplusEmailSender,'es2126PoEplusEmailReturnPath':es2126PoEplusEmailReturnPath,'es2126PoEplusEmailUserNumber':es2126PoEplusEmailUserNumber,'es2126PoEplusEmailUserTable':es2126PoEplusEmailUserTable,'es2126PoEplusEmailUserEntry':es2126PoEplusEmailUserEntry,_Q:es2126PoEplusEmailUserIndex,'es2126PoEplusEmailUserAddress':es2126PoEplusEmailUserAddress,'es2126PoEplusTftp':es2126PoEplusTftp,'es2126PoEplusRemoteTftpServer':es2126PoEplusRemoteTftpServer,'es2126PoEplusInternalTftpServerState':es2126PoEplusInternalTftpServerState,'es2126PoEplusConfiguration':es2126PoEplusConfiguration,'es2126PoEplusSaveRestore':es2126PoEplusSaveRestore,'es2126PoEplusSaveStart':es2126PoEplusSaveStart,'es2126PoEplusSaveUser':es2126PoEplusSaveUser,'es2126PoEplusRestoreDefault':es2126PoEplusRestoreDefault,'es2126PoEplusRestoreUser':es2126PoEplusRestoreUser,'es2126PoEplusConfigFile':es2126PoEplusConfigFile,'es2126PoEplusExportConfigName':es2126PoEplusExportConfigName,'es2126PoEplusDoExportConfig':es2126PoEplusDoExportConfig,'es2126PoEplusImportConfigName':es2126PoEplusImportConfigName,'es2126PoEplusDoImportConfig':es2126PoEplusDoImportConfig,'es2126PoEplusDiagnostic':es2126PoEplusDiagnostic,'es2126PoEplusEEPROMTest':es2126PoEplusEEPROMTest,'es2126PoEplusUartTest':es2126PoEplusUartTest,'es2126PoEplusDramTest':es2126PoEplusDramTest,'es2126PoEplusFlashTest':es2126PoEplusFlashTest,'es2126PoEplusInternalLoopbackTest':es2126PoEplusInternalLoopbackTest,'es2126PoEplusExternalLoopbackTest':es2126PoEplusExternalLoopbackTest,'es2126PoEplusPingTest':es2126PoEplusPingTest,'es2126PoEplusLog':es2126PoEplusLog,'es2126PoEplusClearLog':es2126PoEplusClearLog,'es2126PoEplusUploadLog':es2126PoEplusUploadLog,'es2126PoEplusAutoUploadLogState':es2126PoEplusAutoUploadLogState,'es2126PoEplusLogNumber':es2126PoEplusLogNumber,'es2126PoEplusLogTable':es2126PoEplusLogTable,'es2126PoEplusLogEntry':es2126PoEplusLogEntry,_R:es2126PoEplusLogIndex,'es2126PoEplusLogEvent':es2126PoEplusLogEvent,'es2126PoEplusFirmware':es2126PoEplusFirmware,'es2126PoEplusFirmwareFileName':es2126PoEplusFirmwareFileName,'es2126PoEplusDoFirmwareUpgrade':es2126PoEplusDoFirmwareUpgrade,'es2126PoEplusPort':es2126PoEplusPort,'es2126PoEplusPortStatus':es2126PoEplusPortStatus,'es2126PoEplusPortStatusNumber':es2126PoEplusPortStatusNumber,'es2126PoEplusPortStatusTable':es2126PoEplusPortStatusTable,'es2126PoEplusPortStatusEntry':es2126PoEplusPortStatusEntry,_S:es2126PoEplusPortStatusIndex,'es2126PoEplusPortStatusMedia':es2126PoEplusPortStatusMedia,'es2126PoEplusPortStatusLink':es2126PoEplusPortStatusLink,'es2126PoEplusPortStatusPortState':es2126PoEplusPortStatusPortState,'es2126PoEplusPortStatusAutoNego':es2126PoEplusPortStatusAutoNego,'es2126PoEplusPortStatusSpdDpx':es2126PoEplusPortStatusSpdDpx,'es2126PoEplusPortStatusRxPause':es2126PoEplusPortStatusRxPause,'es2126PoEplusPortStatusTxPause':es2126PoEplusPortStatusTxPause,'es2126PoEplusPortStatusDescription':es2126PoEplusPortStatusDescription,'es2126PoEplusPortConf':es2126PoEplusPortConf,'es2126PoEplusPortConfNumber':es2126PoEplusPortConfNumber,'es2126PoEplusPortConfTable':es2126PoEplusPortConfTable,'es2126PoEplusPortConfEntry':es2126PoEplusPortConfEntry,_T:es2126PoEplusPortConfIndex,'es2126PoEplusPortConfPortState':es2126PoEplusPortConfPortState,'es2126PoEplusPortConfSpdDpx':es2126PoEplusPortConfSpdDpx,'es2126PoEplusPortConfFlwCtrl':es2126PoEplusPortConfFlwCtrl,'es2126PoEplusPortConfDescription':es2126PoEplusPortConfDescription,'es2126PoEplusPortBandwidth':es2126PoEplusPortBandwidth,'es2126PoEplusPortBandwidthTable':es2126PoEplusPortBandwidthTable,'es2126PoEplusPortBandwidthEntry':es2126PoEplusPortBandwidthEntry,_U:es2126PoEplusPortBandwidthIndex,'es2126PoEplusPortBandwidthIngressRate':es2126PoEplusPortBandwidthIngressRate,'es2126PoEplusPortBandwidthEgressRate':es2126PoEplusPortBandwidthEgressRate,'es2126PoEplusPortBandwidthStormType':es2126PoEplusPortBandwidthStormType,'es2126PoEplusPortBandwidthStormRate':es2126PoEplusPortBandwidthStormRate,'es2126PoEplusPortSFPInfo':es2126PoEplusPortSFPInfo,'es2126PoEplusPortSFPInfoNumber':es2126PoEplusPortSFPInfoNumber,'es2126PoEplusPortSFPInfoTable':es2126PoEplusPortSFPInfoTable,'es2126PoEplusPortSFPInfoEntry':es2126PoEplusPortSFPInfoEntry,_V:es2126PoEplusPortSFPInfoIndex,'es2126PoEplusPortSFPConnectorType':es2126PoEplusPortSFPConnectorType,'es2126PoEplusPortSFPFiberType':es2126PoEplusPortSFPFiberType,'es2126PoEplusPortSFPWavelength':es2126PoEplusPortSFPWavelength,'es2126PoEplusPortSFPBaudRate':es2126PoEplusPortSFPBaudRate,'es2126PoEplusPortSFPVendorOUI':es2126PoEplusPortSFPVendorOUI,'es2126PoEplusPortSFPVendorName':es2126PoEplusPortSFPVendorName,'es2126PoEplusPortSFPVendorPN':es2126PoEplusPortSFPVendorPN,'es2126PoEplusPortSFPVendorRev':es2126PoEplusPortSFPVendorRev,'es2126PoEplusPortSFPVendorSN':es2126PoEplusPortSFPVendorSN,'es2126PoEplusPortSFPDateCode':es2126PoEplusPortSFPDateCode,'es2126PoEplusPortSFPTemperature':es2126PoEplusPortSFPTemperature,'es2126PoEplusPortSFPVcc':es2126PoEplusPortSFPVcc,'es2126PoEplusPortSFPTxBias':es2126PoEplusPortSFPTxBias,'es2126PoEplusPortSFPTxPWR':es2126PoEplusPortSFPTxPWR,'es2126PoEplusPortSFPRxPWR':es2126PoEplusPortSFPRxPWR,'es2126PoEplusLoopDetectedConf':es2126PoEplusLoopDetectedConf,'es2126PoEplusLoopDetectedNumber':es2126PoEplusLoopDetectedNumber,'es2126PoEplusLoopDetectedTable':es2126PoEplusLoopDetectedTable,'es2126PoEplusLoopDetectedEntry':es2126PoEplusLoopDetectedEntry,_W:es2126PoEplusLoopDetectedfIndex,'es2126PoEplusLoopDetectedStateEbl':es2126PoEplusLoopDetectedStateEbl,'es2126PoEplusLoopDetectedCurrentStatus':es2126PoEplusLoopDetectedCurrentStatus,'es2126PoEplusLoopDetectedResumed':es2126PoEplusLoopDetectedResumed,'es2126PoEplusLoopDetectedAction':es2126PoEplusLoopDetectedAction,'es2126PoEplusMacTableInfo':es2126PoEplusMacTableInfo,'es2126PoEplusMacTableMaintenance':es2126PoEplusMacTableMaintenance,'es2126PoEplusMacTableAgingTime':es2126PoEplusMacTableAgingTime,'es2126PoEplusMacTableFlush':es2126PoEplusMacTableFlush,'es2126PoEplusMacTableLearnPortLimitTable':es2126PoEplusMacTableLearnPortLimitTable,'es2126PoEplusMacTableLearnPortLimitEntry':es2126PoEplusMacTableLearnPortLimitEntry,_X:es2126PoEplusMacTableLearnPortLimitIndex,'es2126PoEplusMacTableLearnPortLimit':es2126PoEplusMacTableLearnPortLimit,'es2126PoEplusMacTableStaticMac':es2126PoEplusMacTableStaticMac,'es2126PoEplusMacTableStaticMacNumber':es2126PoEplusMacTableStaticMacNumber,'es2126PoEplusMacTableStaticMacEntryCreate':es2126PoEplusMacTableStaticMacEntryCreate,'es2126PoEplusMacTableStaticMacTable':es2126PoEplusMacTableStaticMacTable,'es2126PoEplusMacTableStaticMacEntry':es2126PoEplusMacTableStaticMacEntry,_Y:es2126PoEplusMacTableStaticMacIndex,'es2126PoEplusMacTableStaticMacAddress':es2126PoEplusMacTableStaticMacAddress,'es2126PoEplusMacTableStaticMacVid':es2126PoEplusMacTableStaticMacVid,'es2126PoEplusMacTableStaticMacQueue':es2126PoEplusMacTableStaticMacQueue,'es2126PoEplusMacTableStaticMacFwRule':es2126PoEplusMacTableStaticMacFwRule,'es2126PoEplusMacTableStaticMacPort':es2126PoEplusMacTableStaticMacPort,'es2126PoEplusMacTableStaticMacEntryAction':es2126PoEplusMacTableStaticMacEntryAction,'es2126PoEplusMacTableMacAlias':es2126PoEplusMacTableMacAlias,'es2126PoEplusMacTableMacAliasNumber':es2126PoEplusMacTableMacAliasNumber,'es2126PoEplusMacTableMacAliasEntryCreate':es2126PoEplusMacTableMacAliasEntryCreate,'es2126PoEplusMacTableMacAliasTable':es2126PoEplusMacTableMacAliasTable,'es2126PoEplusMacTableMacAliasEntry':es2126PoEplusMacTableMacAliasEntry,_Z:es2126PoEplusMacTableMacAliasIndex,'es2126PoEplusMacTableMacAliasAddress':es2126PoEplusMacTableMacAliasAddress,'es2126PoEplusMacTableMacAliasAlias':es2126PoEplusMacTableMacAliasAlias,'es2126PoEplusMacTableMacAliasEntryAction':es2126PoEplusMacTableMacAliasEntryAction,'es2126PoEplusGVRPInfo':es2126PoEplusGVRPInfo,'es2126PoEplusGvrpConf':es2126PoEplusGvrpConf,'es2126PoEplusGvrpConfState':es2126PoEplusGvrpConfState,'es2126PoEplusGvrpConfTable':es2126PoEplusGvrpConfTable,'es2126PoEplusGvrpConfEntry':es2126PoEplusGvrpConfEntry,_a:es2126PoEplusGvrpConfIndex,'es2126PoEplusGvrpConfJoinTime':es2126PoEplusGvrpConfJoinTime,'es2126PoEplusGvrpConfLeaveTime':es2126PoEplusGvrpConfLeaveTime,'es2126PoEplusGvrpConfLeaveAllTime':es2126PoEplusGvrpConfLeaveAllTime,'es2126PoEplusGvrpConfDefaultAppMode':es2126PoEplusGvrpConfDefaultAppMode,'es2126PoEplusGvrpConfDefaultRegMode':es2126PoEplusGvrpConfDefaultRegMode,'es2126PoEplusGvrpConfRestrictedMode':es2126PoEplusGvrpConfRestrictedMode,'es2126PoEplusGvrpCounter':es2126PoEplusGvrpCounter,'es2126PoEplusGvrpCounterTable':es2126PoEplusGvrpCounterTable,'es2126PoEplusGvrpCounterEntry':es2126PoEplusGvrpCounterEntry,_b:es2126PoEplusGvrpCounterIndex,'es2126PoEplusGvrpCounterRxTotalGvrpPkts':es2126PoEplusGvrpCounterRxTotalGvrpPkts,'es2126PoEplusGvrpCounterRxInvalidGvrpPkts':es2126PoEplusGvrpCounterRxInvalidGvrpPkts,'es2126PoEplusGvrpCounterRxLeaveAllMsg':es2126PoEplusGvrpCounterRxLeaveAllMsg,'es2126PoEplusGvrpCounterRxJoinEmptyMsg':es2126PoEplusGvrpCounterRxJoinEmptyMsg,'es2126PoEplusGvrpCounterRxJoinInMsg':es2126PoEplusGvrpCounterRxJoinInMsg,'es2126PoEplusGvrpCounterRxLeaveEmptyMsg':es2126PoEplusGvrpCounterRxLeaveEmptyMsg,'es2126PoEplusGvrpCounterRxEmptyMsg':es2126PoEplusGvrpCounterRxEmptyMsg,'es2126PoEplusGvrpCounterTxTotalGvrpPkts':es2126PoEplusGvrpCounterTxTotalGvrpPkts,'es2126PoEplusGvrpCounterTxLeaveAllMsg':es2126PoEplusGvrpCounterTxLeaveAllMsg,'es2126PoEplusGvrpCounterTxJoinEmptyMsg':es2126PoEplusGvrpCounterTxJoinEmptyMsg,'es2126PoEplusGvrpCounterTxJoinInMsg':es2126PoEplusGvrpCounterTxJoinInMsg,'es2126PoEplusGvrpCounterTxLeaveEmptyMsg':es2126PoEplusGvrpCounterTxLeaveEmptyMsg,'es2126PoEplusGvrpCounterTxEmptyMsg':es2126PoEplusGvrpCounterTxEmptyMsg,'es2126PoEplusGvrpGroup':es2126PoEplusGvrpGroup,'es2126PoEplusGvrpGroupNumber':es2126PoEplusGvrpGroupNumber,'es2126PoEplusGvrpGroupTable':es2126PoEplusGvrpGroupTable,'es2126PoEplusGvrpGroupEntry':es2126PoEplusGvrpGroupEntry,_c:es2126PoEplusGvrpGroupId,'es2126PoEplusGvrpGroupVid':es2126PoEplusGvrpGroupVid,'es2126PoEplusGvrpGroupMemberPort':es2126PoEplusGvrpGroupMemberPort,'es2126PoEplusSecurity':es2126PoEplusSecurity,'es2126PoEplusIsolatedPortGroup':es2126PoEplusIsolatedPortGroup,'es2126PoEplusMirror':es2126PoEplusMirror,'es2126PoEplusMirrorMode':es2126PoEplusMirrorMode,'es2126PoEplusMonitoringPort':es2126PoEplusMonitoringPort,'es2126PoEplusMonitoredIngressPort':es2126PoEplusMonitoredIngressPort,'es2126PoEplusMonitoredEgressPort':es2126PoEplusMonitoredEgressPort,'es2126PoEplusRestrictedGroup':es2126PoEplusRestrictedGroup,'es2126PoEplusRestrictedGroupIngress':es2126PoEplusRestrictedGroupIngress,'es2126PoEplusRestrictedGroupEgress':es2126PoEplusRestrictedGroupEgress,'es2126PoEplusVirtualStack':es2126PoEplusVirtualStack,'es2126PoEplusVirtualStackState':es2126PoEplusVirtualStackState,'es2126PoEplusVirtualStackRole':es2126PoEplusVirtualStackRole,'es2126PoEplusVirtualStackGroupID':es2126PoEplusVirtualStackGroupID,'es2126PoEplusManagementSecurity':es2126PoEplusManagementSecurity,'es2126PoEplusManagementSecurityNumber':es2126PoEplusManagementSecurityNumber,'es2126PoEplusManagementSecurityEntryCreate':es2126PoEplusManagementSecurityEntryCreate,'es2126PoEplusManagementSecurityTable':es2126PoEplusManagementSecurityTable,'es2126PoEplusManagementSecurityEntry':es2126PoEplusManagementSecurityEntry,_d:es2126PoEplusManagementSecurityIndex,'es2126PoEplusManagementSecurityName':es2126PoEplusManagementSecurityName,'es2126PoEplusManagementSecurityVid':es2126PoEplusManagementSecurityVid,'es2126PoEplusManagementSecurityIpRange':es2126PoEplusManagementSecurityIpRange,'es2126PoEplusManagementSecurityIncomigPort':es2126PoEplusManagementSecurityIncomigPort,'es2126PoEplusManagementSecurityAccessType':es2126PoEplusManagementSecurityAccessType,'es2126PoEplusManagementSecurityAction':es2126PoEplusManagementSecurityAction,'es2126PoEplusManagementSecurityEntryAction':es2126PoEplusManagementSecurityEntryAction,'es2126PoEplusQoS':es2126PoEplusQoS,'es2126PoEplusQoSGlobalConfig':es2126PoEplusQoSGlobalConfig,'es2126PoEplusQoSMode':es2126PoEplusQoSMode,'es2126PoEplusQosPriorityControl1p':es2126PoEplusQosPriorityControl1p,'es2126PoEplusQosPriorityControlTOS':es2126PoEplusQosPriorityControlTOS,'es2126PoEplusQosPriorityControlDSCP':es2126PoEplusQosPriorityControlDSCP,'es2126PoEplusQoSSchedulingMethod':es2126PoEplusQoSSchedulingMethod,'es2126PoEplusQoSWeightQ0':es2126PoEplusQoSWeightQ0,'es2126PoEplusQoSWeightQ1':es2126PoEplusQoSWeightQ1,'es2126PoEplusQoSWeightQ2':es2126PoEplusQoSWeightQ2,'es2126PoEplusQoSWeightQ3':es2126PoEplusQoSWeightQ3,'es2126PoEplusQoSVIPPort':es2126PoEplusQoSVIPPort,'es2126PoEplusQoS1pPriority':es2126PoEplusQoS1pPriority,'es2126PoEplusQoS1pPriorityTable':es2126PoEplusQoS1pPriorityTable,'es2126PoEplusQoS1pPriorityEntry':es2126PoEplusQoS1pPriorityEntry,_e:es2126PoEplusQoS1pPriorityIndex,'es2126PoEplusQoS1pPriorityValue':es2126PoEplusQoS1pPriorityValue,'es2126PoEplusQoS1pPriorityQueue':es2126PoEplusQoS1pPriorityQueue,'es2126PoEplusQoSDTypeTOSPriority':es2126PoEplusQoSDTypeTOSPriority,'es2126PoEplusQoSDTypeTOSPriorityTable':es2126PoEplusQoSDTypeTOSPriorityTable,'es2126PoEplusQoSDTypeTOSPriorityEntry':es2126PoEplusQoSDTypeTOSPriorityEntry,_f:es2126PoEplusQoSDTypeTOSPriorityIndex,'es2126PoEplusQoSDTypeTOSPriorityValue':es2126PoEplusQoSDTypeTOSPriorityValue,'es2126PoEplusQoSDTypeTOSPriorityQueue':es2126PoEplusQoSDTypeTOSPriorityQueue,'es2126PoEplusQoSTTypeTOSPriority':es2126PoEplusQoSTTypeTOSPriority,'es2126PoEplusQoSTTypeTOSPriorityTable':es2126PoEplusQoSTTypeTOSPriorityTable,'es2126PoEplusQoSTTypeTOSPriorityEntry':es2126PoEplusQoSTTypeTOSPriorityEntry,_g:es2126PoEplusQoSTTypeTOSPriorityIndex,'es2126PoEplusQoSTTypeTOSPriorityValue':es2126PoEplusQoSTTypeTOSPriorityValue,'es2126PoEplusQoSTTypeTOSPriorityQueue':es2126PoEplusQoSTTypeTOSPriorityQueue,'es2126PoEplusQoSRTypeTOSPriority':es2126PoEplusQoSRTypeTOSPriority,'es2126PoEplusQoSRTypeTOSPriorityTable':es2126PoEplusQoSRTypeTOSPriorityTable,'es2126PoEplusQoSRTypeTOSPriorityEntry':es2126PoEplusQoSRTypeTOSPriorityEntry,_h:es2126PoEplusQoSRTypeTOSPriorityIndex,'es2126PoEplusQoSRTypeTOSPriorityValue':es2126PoEplusQoSRTypeTOSPriorityValue,'es2126PoEplusQoSRTypeTOSPriorityQueue':es2126PoEplusQoSRTypeTOSPriorityQueue,'es2126PoEplusQoSMTypeTOSPriority':es2126PoEplusQoSMTypeTOSPriority,'es2126PoEplusQoSMTypeTOSPriorityTable':es2126PoEplusQoSMTypeTOSPriorityTable,'es2126PoEplusQoSMTypeTOSPriorityEntry':es2126PoEplusQoSMTypeTOSPriorityEntry,_i:es2126PoEplusQoSMTypeTOSPriorityIndex,'es2126PoEplusQoSMTypeTOSPriorityValue':es2126PoEplusQoSMTypeTOSPriorityValue,'es2126PoEplusQoSMTypeTOSPriorityQueue':es2126PoEplusQoSMTypeTOSPriorityQueue,'es2126PoEplusQoSDSCPPriority':es2126PoEplusQoSDSCPPriority,'es2126PoEplusQoSDSCPPriorityTable':es2126PoEplusQoSDSCPPriorityTable,'es2126PoEplusQoSDSCPPriorityEntry':es2126PoEplusQoSDSCPPriorityEntry,_j:es2126PoEplusQoSDSCPPriorityIndex,'es2126PoEplusQoSDSCPPriorityValue':es2126PoEplusQoSDSCPPriorityValue,'es2126PoEplusQoSDSCPPriorityQueue':es2126PoEplusQoSDSCPPriorityQueue,'es2126PoEplusVlan':es2126PoEplusVlan,'es2126PoEplusVlanModeConfig':es2126PoEplusVlanModeConfig,'es2126PoEplusVlanMode':es2126PoEplusVlanMode,'es2126PoEplusSymmetricVlan':es2126PoEplusSymmetricVlan,'es2126PoEplusVlanSVL':es2126PoEplusVlanSVL,'es2126PoEplusDoubleTag':es2126PoEplusDoubleTag,'es2126PoEplusUpLinkPort':es2126PoEplusUpLinkPort,'es2126PoEplusTagBasedVlanGroup':es2126PoEplusTagBasedVlanGroup,'es2126PoEplusTagBasedVlanNumbers':es2126PoEplusTagBasedVlanNumbers,'es2126PoEplusTagBasedCreateStatus':es2126PoEplusTagBasedCreateStatus,'es2126PoEplusTagBasedVlanTable':es2126PoEplusTagBasedVlanTable,'es2126PoEplusTagBasedVlanEntry':es2126PoEplusTagBasedVlanEntry,_k:es2126PoEplusTagBasedVlanVid,'es2126PoEplusTagBasedVlanName':es2126PoEplusTagBasedVlanName,'es2126PoEplusTagBasedVlanMember':es2126PoEplusTagBasedVlanMember,'es2126PoEplusTagBasedVlanUntag':es2126PoEplusTagBasedVlanUntag,'es2126PoEplusTagBasedVlanRowStatus':es2126PoEplusTagBasedVlanRowStatus,'es2126PoEplusVlanPvid':es2126PoEplusVlanPvid,'es2126PoEplusVlanPvidTable':es2126PoEplusVlanPvidTable,'es2126PoEplusVlanPvidEntry':es2126PoEplusVlanPvidEntry,_l:es2126PoEplusVlanPvidPort,'es2126PoEplusVlanPvidValue':es2126PoEplusVlanPvidValue,'es2126PoEplusVlanPvidDefaultPriority':es2126PoEplusVlanPvidDefaultPriority,'es2126PoEplusVlanPvidDropUntag':es2126PoEplusVlanPvidDropUntag,'es2126PoEplusPortBasedVlanGroup':es2126PoEplusPortBasedVlanGroup,'es2126PoEplusPortBasedVlanNumbers':es2126PoEplusPortBasedVlanNumbers,'es2126PoEplusPortBasedCreateStatus':es2126PoEplusPortBasedCreateStatus,'es2126PoEplusPortBasedVlanTable':es2126PoEplusPortBasedVlanTable,'es2126PoEplusPortBasedVlanEntry':es2126PoEplusPortBasedVlanEntry,_m:es2126PoEplusPortBasedVlanIndex,'es2126PoEplusPortBasedVlanName':es2126PoEplusPortBasedVlanName,'es2126PoEplusPortBasedVlanMember':es2126PoEplusPortBasedVlanMember,'es2126PoEplusPortBasedVlanRowStatus':es2126PoEplusPortBasedVlanRowStatus,'es2126PoEplusManagementVlan':es2126PoEplusManagementVlan,'es2126PoEplusManagementVlanState':es2126PoEplusManagementVlanState,'es2126PoEplusManagementVlanVid':es2126PoEplusManagementVlanVid,'es2126PoEplusDot1X':es2126PoEplusDot1X,'es2126PoEplusDot1XStateSetting':es2126PoEplusDot1XStateSetting,'es2126PoEplusRadiusServer':es2126PoEplusRadiusServer,'es2126PoEplusDot1XPort':es2126PoEplusDot1XPort,'es2126PoEplusSecretKey':es2126PoEplusSecretKey,'es2126PoEplusAccountingService':es2126PoEplusAccountingService,'es2126PoEplusAccountingServer':es2126PoEplusAccountingServer,'es2126PoEplusAccountingPort':es2126PoEplusAccountingPort,'es2126PoEplusDot1XPortSecurityManagement':es2126PoEplusDot1XPortSecurityManagement,'es2126PoEplusDot1XPortSecurityTable':es2126PoEplusDot1XPortSecurityTable,'es2126PoEplusDot1XPortSecurityEntry':es2126PoEplusDot1XPortSecurityEntry,_n:es2126PoEplusDot1XPortSecurityPortIndex,'es2126PoEplusDot1XPortSecurityMode':es2126PoEplusDot1XPortSecurityMode,'es2126PoEplusDot1XPortSecurityPortControl':es2126PoEplusDot1XPortSecurityPortControl,'es2126PoEplusDot1XPortSecurityReAuthMax':es2126PoEplusDot1XPortSecurityReAuthMax,'es2126PoEplusDot1XPortSecurityTxPeriod':es2126PoEplusDot1XPortSecurityTxPeriod,'es2126PoEplusDot1XPortSecurityQuietPeriod':es2126PoEplusDot1XPortSecurityQuietPeriod,'es2126PoEplusDot1XPortSecurityReAuthEnabled':es2126PoEplusDot1XPortSecurityReAuthEnabled,'es2126PoEplusDot1XPortSecurityReAuthPeriod':es2126PoEplusDot1XPortSecurityReAuthPeriod,'es2126PoEplusDot1XPortSecurityMaxRequest':es2126PoEplusDot1XPortSecurityMaxRequest,'es2126PoEplusDot1XPortSecuritySuppTimeout':es2126PoEplusDot1XPortSecuritySuppTimeout,'es2126PoEplusDot1XPortSecurityServerTimeout':es2126PoEplusDot1XPortSecurityServerTimeout,'es2126PoEplusDot1XPortSecurityStatus':es2126PoEplusDot1XPortSecurityStatus,'es2126PoEplusTrunkInfo':es2126PoEplusTrunkInfo,'es2126PoEplusTrunkPort':es2126PoEplusTrunkPort,'es2126PoEplusTrunkPortTable':es2126PoEplusTrunkPortTable,'es2126PoEplusTrunkPortEntry':es2126PoEplusTrunkPortEntry,_o:es2126PoEplusTrunkPortIndex,'es2126PoEplusTrunkPortMethod':es2126PoEplusTrunkPortMethod,'es2126PoEplusTrunkPortGroup':es2126PoEplusTrunkPortGroup,'es2126PoEplusTrunkPortActiveLacp':es2126PoEplusTrunkPortActiveLacp,'es2126PoEplusTrunkPortAggtr':es2126PoEplusTrunkPortAggtr,'es2126PoEplusTrunkPortStatus':es2126PoEplusTrunkPortStatus,'es2126PoEplusTrunkPortCurrentMode':es2126PoEplusTrunkPortCurrentMode,'es2126PoEplusAggregatorView':es2126PoEplusAggregatorView,'es2126PoEplusAggregatorViewTable':es2126PoEplusAggregatorViewTable,'es2126PoEplusAggregatorViewEntry':es2126PoEplusAggregatorViewEntry,_p:es2126PoEplusAggregatorViewIndex,'es2126PoEplusAggregatorViewMethod':es2126PoEplusAggregatorViewMethod,'es2126PoEplusAggregatorViewMemberPorts':es2126PoEplusAggregatorViewMemberPorts,'es2126PoEplusAggregatorViewReadyPorts':es2126PoEplusAggregatorViewReadyPorts,'es2126PoEplusLacpSystemConfiguration':es2126PoEplusLacpSystemConfiguration,'es2126PoEplusLacpSystemPriority':es2126PoEplusLacpSystemPriority,'es2126PoEplusLacpSystemHashMethod':es2126PoEplusLacpSystemHashMethod,'es2126PoEplusTrapEntry':es2126PoEplusTrapEntry,'es2126PoEplusModuleInserted':es2126PoEplusModuleInserted,'es2126PoEplusModuleRemoved':es2126PoEplusModuleRemoved,'es2126PoEplusDualMediaSwapped':es2126PoEplusDualMediaSwapped,'es2126PoEplusPoEFailure':es2126PoEplusPoEFailure,'es2126PoEplusLoopDetected':es2126PoEplusLoopDetected,'es2126PoEplusLoginProtected':es2126PoEplusLoginProtected,'es2126PoEplusStpStateDisabled':es2126PoEplusStpStateDisabled,'es2126PoEplusStpStateEnabled':es2126PoEplusStpStateEnabled,'es2126PoEplusStpTopologyChanged':es2126PoEplusStpTopologyChanged,'es2126PoEplusRmonRisingAlarm':es2126PoEplusRmonRisingAlarm,'es2126PoEplusRmonFallingAlarm':es2126PoEplusRmonFallingAlarm,'es2126PoEplusLacpStateDisabled':es2126PoEplusLacpStateDisabled,'es2126PoEplusLacpStateEnabled':es2126PoEplusLacpStateEnabled,'es2126PoEplusLacpPortAdded':es2126PoEplusLacpPortAdded,'es2126PoEplusLacpPortTrunkFailure':es2126PoEplusLacpPortTrunkFailure,'es2126PoEplusGvrpStateDisabled':es2126PoEplusGvrpStateDisabled,'es2126PoEplusGvrpStateEnabled':es2126PoEplusGvrpStateEnabled,'es2126PoEplusVlanPortBaseEnabled':es2126PoEplusVlanPortBaseEnabled,'es2126PoEplusVlanTagBaseEnabled':es2126PoEplusVlanTagBaseEnabled,'es2126PoEplusVlanMetroBaseEnabled':es2126PoEplusVlanMetroBaseEnabled,'es2126PoEplusUserLogin':es2126PoEplusUserLogin,'es2126PoEplusUserLogout':es2126PoEplusUserLogout,'es2126PoEplusTrapVariable':es2126PoEplusTrapVariable,_L:username,_I:groupId,_J:actorkey,_K:partnerkey,'uplink':uplink,'loginProtectInfo':loginProtectInfo,'es2126PoEplusPoE':es2126PoEplusPoE,'es2126PoEplusPoEStatus':es2126PoEplusPoEStatus,'es2126PoEplusPoEStatusVmain':es2126PoEplusPoEStatusVmain,'es2126PoEplusPoEStatusImain':es2126PoEplusPoEStatusImain,'es2126PoEplusPoEStatusPconsume':es2126PoEplusPoEStatusPconsume,'es2126PoEplusPoEStatusPowerLimit':es2126PoEplusPoEStatusPowerLimit,'es2126PoEplusPoEStatusTemperature':es2126PoEplusPoEStatusTemperature,'es2126PoEplusPoEStatusTable':es2126PoEplusPoEStatusTable,'es2126PoEplusPoEStatusEntry':es2126PoEplusPoEStatusEntry,_q:es2126PoEplusPoEStatusPortNum,'es2126PoEplusPoEStatusPortOn':es2126PoEplusPoEStatusPortOn,'es2126PoEplusPoEStatusACPortOff':es2126PoEplusPoEStatusACPortOff,'es2126PoEplusPoEStatusDCPortOff':es2126PoEplusPoEStatusDCPortOff,'es2126PoEplusPoEStatusOverloadPortOff':es2126PoEplusPoEStatusOverloadPortOff,'es2126PoEplusPoEStatusShortCircuitPortOff':es2126PoEplusPoEStatusShortCircuitPortOff,'es2126PoEplusPoEStatusOverTemperature':es2126PoEplusPoEStatusOverTemperature,'es2126PoEplusPoEStatusPowerManagePortOff':es2126PoEplusPoEStatusPowerManagePortOff,'es2126PoEplusPoEConfTable':es2126PoEplusPoEConfTable,'es2126PoEplusPoEConfEntry':es2126PoEplusPoEConfEntry,_r:es2126PoEplusPoEConfPortNum,'es2126PoEplusPoEConfStatus':es2126PoEplusPoEConfStatus,'es2126PoEplusPoEConfState':es2126PoEplusPoEConfState,'es2126PoEplusPoEConfPriority':es2126PoEplusPoEConfPriority,'es2126PoEplusPoEConfPower':es2126PoEplusPoEConfPower,'es2126PoEplusPoEConfCurrent':es2126PoEplusPoEConfCurrent,'es2126PoEplusPoEConfClass':es2126PoEplusPoEConfClass,'es2126PoEplusLoginProtect':es2126PoEplusLoginProtect,'es2126PoEplusLockMinutes':es2126PoEplusLockMinutes,'es2126PoEplusLoginErrors':es2126PoEplusLoginErrors})