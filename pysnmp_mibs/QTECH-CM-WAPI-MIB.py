_A6='cmStandardBase'
_A5='apDownlinkUpdownTimes'
_A4='apUplinkUpdownTimes'
_A3='apIfPhysAddress'
_A2='apIfSpeed'
_A1='apIfDescr'
_A0='apIfNumber'
_z='acSoftwareVendor'
_y='acSoftwareVersion'
_x='acSoftwareName'
_w='apSoftwareVendor'
_v='apSoftwareVersion'
_u='apSoftwareName'
_t='gb15629dot11wapiConfigAuthenticationSuiteEnabled'
_s='gb15629dot11wapiConfigAuthenticationSuite'
_r='gb15629dot11wapiConfigUnicastCipherSize'
_q='gb15629dot11wapiConfigUnicastCipherEnabled'
_p='gb15629dot11wapiConfigUnicastCipher'
_o='gb15629dot11wapiGroupCipherRequested'
_n='mutiModeAccesssimultStatus'
_m='peruserWAPIMaxBindwithAllocated'
_l='apWAPIMaxUserNum'
_k='support80211g'
_j='flashmemCapacity'
_i='memoryCapacity'
_h='cpuHandleAbility'
_g='acWAPICertInstalled'
_f='acWAPIASIPAddress'
_e='acWAPIAuthMode'
_d='apWAPIAuthMode'
_c='apBGmode'
_b='apWorkingMode'
_a='apIpAdEntNetMask'
_Z='apIPAddress'
_Y='apUpTime'
_X='apMaxSimultTraffic'
_W='apMaxSimultUsers'
_V='apCurrentBSSID'
_U='apMacAddressConnectedWithAC'
_T='apSysVersion'
_S='apManufacturer'
_R='apSysLocation'
_Q='apSysHostName'
_P='apSysNEId'
_O='ifIndex'
_N='IF-MIB'
_M='qtechWAPIClientOtherInfo'
_L='qtechWAPIClientIP'
_K='apCurrentIP'
_J='apOriginalIP'
_I='read-only'
_H='DisplayString'
_G='qtechWAPIIllegalClientOtherInfo'
_F='qtechWAPIIllegalClientIP'
_E='qtechApgWlanId'
_D='QTECH-AC-MGMT-MIB'
_C='read-write'
_B='QTECH-CM-WAPI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_N,_O)
qtechApgWlanId,=mibBuilder.importSymbols(_D,_E)
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
cmStandardmibmodule=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,70))
if mibBuilder.loadTexts:cmStandardmibmodule.setRevisions(('2010-02-28 00:00',))
_CmStandardWAPITraps_ObjectIdentity=ObjectIdentity
cmStandardWAPITraps=_CmStandardWAPITraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,70,0))
_CmStandardMIBObjects_ObjectIdentity=ObjectIdentity
cmStandardMIBObjects=_CmStandardMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,70,1))
_ApAttributeInfoTable_Object=MibTable
apAttributeInfoTable=_ApAttributeInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,1))
if mibBuilder.loadTexts:apAttributeInfoTable.setStatus(_A)
_ApAttributeInfoEntry_Object=MibTableRow
apAttributeInfoEntry=_ApAttributeInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,1,1))
apAttributeInfoEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:apAttributeInfoEntry.setStatus(_A)
class _ApSysNEId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,255))
_ApSysNEId_Type.__name__=_H
_ApSysNEId_Object=MibTableColumn
apSysNEId=_ApSysNEId_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,1,1,1),_ApSysNEId_Type())
apSysNEId.setMaxAccess(_C)
if mibBuilder.loadTexts:apSysNEId.setStatus(_A)
class _ApSysHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(40,255))
_ApSysHostName_Type.__name__=_H
_ApSysHostName_Object=MibTableColumn
apSysHostName=_ApSysHostName_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,1,1,2),_ApSysHostName_Type())
apSysHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:apSysHostName.setStatus(_A)
_ApSysLocation_Type=DisplayString
_ApSysLocation_Object=MibTableColumn
apSysLocation=_ApSysLocation_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,1,1,3),_ApSysLocation_Type())
apSysLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:apSysLocation.setStatus(_A)
_ApManufacturer_Type=DisplayString
_ApManufacturer_Object=MibTableColumn
apManufacturer=_ApManufacturer_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,1,1,4),_ApManufacturer_Type())
apManufacturer.setMaxAccess(_C)
if mibBuilder.loadTexts:apManufacturer.setStatus(_A)
_ApSysVersion_Type=DisplayString
_ApSysVersion_Object=MibTableColumn
apSysVersion=_ApSysVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,1,1,5),_ApSysVersion_Type())
apSysVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:apSysVersion.setStatus(_A)
_ApMacAddressConnectedWithAC_Type=DisplayString
_ApMacAddressConnectedWithAC_Object=MibTableColumn
apMacAddressConnectedWithAC=_ApMacAddressConnectedWithAC_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,1,1,6),_ApMacAddressConnectedWithAC_Type())
apMacAddressConnectedWithAC.setMaxAccess(_C)
if mibBuilder.loadTexts:apMacAddressConnectedWithAC.setStatus(_A)
_ApCurrentBSSID_Type=DisplayString
_ApCurrentBSSID_Object=MibTableColumn
apCurrentBSSID=_ApCurrentBSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,1,1,7),_ApCurrentBSSID_Type())
apCurrentBSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:apCurrentBSSID.setStatus(_A)
_ApMaxSimultUsers_Type=Integer32
_ApMaxSimultUsers_Object=MibTableColumn
apMaxSimultUsers=_ApMaxSimultUsers_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,1,1,8),_ApMaxSimultUsers_Type())
apMaxSimultUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:apMaxSimultUsers.setStatus(_A)
_ApMaxSimultTraffic_Type=Integer32
_ApMaxSimultTraffic_Object=MibTableColumn
apMaxSimultTraffic=_ApMaxSimultTraffic_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,1,1,9),_ApMaxSimultTraffic_Type())
apMaxSimultTraffic.setMaxAccess(_C)
if mibBuilder.loadTexts:apMaxSimultTraffic.setStatus(_A)
_ApUpTime_Type=Integer32
_ApUpTime_Object=MibTableColumn
apUpTime=_ApUpTime_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,1,1,10),_ApUpTime_Type())
apUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:apUpTime.setStatus(_A)
_ApconfigurationInfoTable_Object=MibTable
apconfigurationInfoTable=_ApconfigurationInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,2))
if mibBuilder.loadTexts:apconfigurationInfoTable.setStatus(_A)
_ApconfigurationInfoEntry_Object=MibTableRow
apconfigurationInfoEntry=_ApconfigurationInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,2,1))
apconfigurationInfoEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:apconfigurationInfoEntry.setStatus(_A)
_ApIPAddress_Type=IpAddress
_ApIPAddress_Object=MibTableColumn
apIPAddress=_ApIPAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,2,1,1),_ApIPAddress_Type())
apIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:apIPAddress.setStatus(_A)
_ApIpAdEntNetMask_Type=IpAddress
_ApIpAdEntNetMask_Object=MibTableColumn
apIpAdEntNetMask=_ApIpAdEntNetMask_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,2,1,2),_ApIpAdEntNetMask_Type())
apIpAdEntNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:apIpAdEntNetMask.setStatus(_A)
_ApWorkingMode_Type=Integer32
_ApWorkingMode_Object=MibTableColumn
apWorkingMode=_ApWorkingMode_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,2,1,3),_ApWorkingMode_Type())
apWorkingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:apWorkingMode.setStatus(_A)
_ApBGmode_Type=Integer32
_ApBGmode_Object=MibTableColumn
apBGmode=_ApBGmode_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,2,1,4),_ApBGmode_Type())
apBGmode.setMaxAccess(_C)
if mibBuilder.loadTexts:apBGmode.setStatus(_A)
_ApacWAPIconfigurationInfoTable_Object=MibTable
apacWAPIconfigurationInfoTable=_ApacWAPIconfigurationInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,3))
if mibBuilder.loadTexts:apacWAPIconfigurationInfoTable.setStatus(_A)
_ApacWAPIconfigurationInfoEntry_Object=MibTableRow
apacWAPIconfigurationInfoEntry=_ApacWAPIconfigurationInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,3,1))
apacWAPIconfigurationInfoEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:apacWAPIconfigurationInfoEntry.setStatus(_A)
_ApWAPIAuthMode_Type=TruthValue
_ApWAPIAuthMode_Object=MibTableColumn
apWAPIAuthMode=_ApWAPIAuthMode_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,3,1,1),_ApWAPIAuthMode_Type())
apWAPIAuthMode.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIAuthMode.setStatus(_A)
_AcWAPIAuthMode_Type=TruthValue
_AcWAPIAuthMode_Object=MibTableColumn
acWAPIAuthMode=_AcWAPIAuthMode_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,3,1,2),_AcWAPIAuthMode_Type())
acWAPIAuthMode.setMaxAccess(_C)
if mibBuilder.loadTexts:acWAPIAuthMode.setStatus(_A)
_AcWAPIASIPAddress_Type=IpAddress
_AcWAPIASIPAddress_Object=MibTableColumn
acWAPIASIPAddress=_AcWAPIASIPAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,3,1,3),_AcWAPIASIPAddress_Type())
acWAPIASIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:acWAPIASIPAddress.setStatus(_A)
_AcWAPICertInstalled_Type=TruthValue
_AcWAPICertInstalled_Object=MibTableColumn
acWAPICertInstalled=_AcWAPICertInstalled_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,3,1,4),_AcWAPICertInstalled_Type())
acWAPICertInstalled.setMaxAccess(_C)
if mibBuilder.loadTexts:acWAPICertInstalled.setStatus(_A)
_CpuHandleAbility_Type=OctetString
_CpuHandleAbility_Object=MibTableColumn
cpuHandleAbility=_CpuHandleAbility_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,3,1,5),_CpuHandleAbility_Type())
cpuHandleAbility.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuHandleAbility.setStatus(_A)
_MemoryCapacity_Type=OctetString
_MemoryCapacity_Object=MibTableColumn
memoryCapacity=_MemoryCapacity_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,3,1,6),_MemoryCapacity_Type())
memoryCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:memoryCapacity.setStatus(_A)
_FlashmemCapacity_Type=OctetString
_FlashmemCapacity_Object=MibTableColumn
flashmemCapacity=_FlashmemCapacity_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,3,1,7),_FlashmemCapacity_Type())
flashmemCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:flashmemCapacity.setStatus(_A)
_Support80211g_Type=OctetString
_Support80211g_Object=MibTableColumn
support80211g=_Support80211g_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,3,1,8),_Support80211g_Type())
support80211g.setMaxAccess(_C)
if mibBuilder.loadTexts:support80211g.setStatus(_A)
_ApWAPIMaxUserNum_Type=Integer32
_ApWAPIMaxUserNum_Object=MibTableColumn
apWAPIMaxUserNum=_ApWAPIMaxUserNum_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,3,1,9),_ApWAPIMaxUserNum_Type())
apWAPIMaxUserNum.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIMaxUserNum.setStatus(_A)
_PeruserWAPIMaxBindwithAllocated_Type=Integer32
_PeruserWAPIMaxBindwithAllocated_Object=MibTableColumn
peruserWAPIMaxBindwithAllocated=_PeruserWAPIMaxBindwithAllocated_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,3,1,10),_PeruserWAPIMaxBindwithAllocated_Type())
peruserWAPIMaxBindwithAllocated.setMaxAccess(_C)
if mibBuilder.loadTexts:peruserWAPIMaxBindwithAllocated.setStatus(_A)
_MutiModeAccesssimultStatus_Type=TruthValue
_MutiModeAccesssimultStatus_Object=MibTableColumn
mutiModeAccesssimultStatus=_MutiModeAccesssimultStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,3,1,11),_MutiModeAccesssimultStatus_Type())
mutiModeAccesssimultStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mutiModeAccesssimultStatus.setStatus(_A)
_Gb15629dot11wapiConfigExtraTable_Object=MibTable
gb15629dot11wapiConfigExtraTable=_Gb15629dot11wapiConfigExtraTable_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,4))
if mibBuilder.loadTexts:gb15629dot11wapiConfigExtraTable.setStatus(_A)
_Gb15629dot11wapiConfigExtraEntry_Object=MibTableRow
gb15629dot11wapiConfigExtraEntry=_Gb15629dot11wapiConfigExtraEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,4,1))
gb15629dot11wapiConfigExtraEntry.setIndexNames((0,_N,_O))
if mibBuilder.loadTexts:gb15629dot11wapiConfigExtraEntry.setStatus(_A)
_Gb15629dot11wapiGroupCipherRequested_Type=DisplayString
_Gb15629dot11wapiGroupCipherRequested_Object=MibTableColumn
gb15629dot11wapiGroupCipherRequested=_Gb15629dot11wapiGroupCipherRequested_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,4,1,1),_Gb15629dot11wapiGroupCipherRequested_Type())
gb15629dot11wapiGroupCipherRequested.setMaxAccess(_I)
if mibBuilder.loadTexts:gb15629dot11wapiGroupCipherRequested.setStatus(_A)
_Gb15629dot11wapiConfigUnicastCipher_Type=DisplayString
_Gb15629dot11wapiConfigUnicastCipher_Object=MibTableColumn
gb15629dot11wapiConfigUnicastCipher=_Gb15629dot11wapiConfigUnicastCipher_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,4,1,2),_Gb15629dot11wapiConfigUnicastCipher_Type())
gb15629dot11wapiConfigUnicastCipher.setMaxAccess(_I)
if mibBuilder.loadTexts:gb15629dot11wapiConfigUnicastCipher.setStatus(_A)
_Gb15629dot11wapiConfigUnicastCipherEnabled_Type=TruthValue
_Gb15629dot11wapiConfigUnicastCipherEnabled_Object=MibTableColumn
gb15629dot11wapiConfigUnicastCipherEnabled=_Gb15629dot11wapiConfigUnicastCipherEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,4,1,3),_Gb15629dot11wapiConfigUnicastCipherEnabled_Type())
gb15629dot11wapiConfigUnicastCipherEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:gb15629dot11wapiConfigUnicastCipherEnabled.setStatus(_A)
_Gb15629dot11wapiConfigUnicastCipherSize_Type=Unsigned32
_Gb15629dot11wapiConfigUnicastCipherSize_Object=MibTableColumn
gb15629dot11wapiConfigUnicastCipherSize=_Gb15629dot11wapiConfigUnicastCipherSize_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,4,1,4),_Gb15629dot11wapiConfigUnicastCipherSize_Type())
gb15629dot11wapiConfigUnicastCipherSize.setMaxAccess(_C)
if mibBuilder.loadTexts:gb15629dot11wapiConfigUnicastCipherSize.setStatus(_A)
_Gb15629dot11wapiConfigAuthenticationSuite_Type=DisplayString
_Gb15629dot11wapiConfigAuthenticationSuite_Object=MibTableColumn
gb15629dot11wapiConfigAuthenticationSuite=_Gb15629dot11wapiConfigAuthenticationSuite_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,4,1,5),_Gb15629dot11wapiConfigAuthenticationSuite_Type())
gb15629dot11wapiConfigAuthenticationSuite.setMaxAccess(_I)
if mibBuilder.loadTexts:gb15629dot11wapiConfigAuthenticationSuite.setStatus(_A)
_Gb15629dot11wapiConfigAuthenticationSuiteEnabled_Type=TruthValue
_Gb15629dot11wapiConfigAuthenticationSuiteEnabled_Object=MibTableColumn
gb15629dot11wapiConfigAuthenticationSuiteEnabled=_Gb15629dot11wapiConfigAuthenticationSuiteEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,4,1,6),_Gb15629dot11wapiConfigAuthenticationSuiteEnabled_Type())
gb15629dot11wapiConfigAuthenticationSuiteEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:gb15629dot11wapiConfigAuthenticationSuiteEnabled.setStatus(_A)
_ApacsoftorHardwareconfigInfoTable_Object=MibTable
apacsoftorHardwareconfigInfoTable=_ApacsoftorHardwareconfigInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,5))
if mibBuilder.loadTexts:apacsoftorHardwareconfigInfoTable.setStatus(_A)
_ApacsoftorHardwareconfigInfoEntry_Object=MibTableRow
apacsoftorHardwareconfigInfoEntry=_ApacsoftorHardwareconfigInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,5,1))
apacsoftorHardwareconfigInfoEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:apacsoftorHardwareconfigInfoEntry.setStatus(_A)
_ApSoftwareName_Type=OctetString
_ApSoftwareName_Object=MibTableColumn
apSoftwareName=_ApSoftwareName_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,5,1,1),_ApSoftwareName_Type())
apSoftwareName.setMaxAccess(_C)
if mibBuilder.loadTexts:apSoftwareName.setStatus(_A)
_ApSoftwareVersion_Type=DisplayString
_ApSoftwareVersion_Object=MibTableColumn
apSoftwareVersion=_ApSoftwareVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,5,1,2),_ApSoftwareVersion_Type())
apSoftwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:apSoftwareVersion.setStatus(_A)
_ApSoftwareVendor_Type=DisplayString
_ApSoftwareVendor_Object=MibTableColumn
apSoftwareVendor=_ApSoftwareVendor_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,5,1,3),_ApSoftwareVendor_Type())
apSoftwareVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:apSoftwareVendor.setStatus(_A)
_AcSoftwareName_Type=OctetString
_AcSoftwareName_Object=MibTableColumn
acSoftwareName=_AcSoftwareName_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,5,1,4),_AcSoftwareName_Type())
acSoftwareName.setMaxAccess(_C)
if mibBuilder.loadTexts:acSoftwareName.setStatus(_A)
_AcSoftwareVersion_Type=DisplayString
_AcSoftwareVersion_Object=MibTableColumn
acSoftwareVersion=_AcSoftwareVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,5,1,5),_AcSoftwareVersion_Type())
acSoftwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:acSoftwareVersion.setStatus(_A)
_AcSoftwareVendor_Type=DisplayString
_AcSoftwareVendor_Object=MibTableColumn
acSoftwareVendor=_AcSoftwareVendor_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,5,1,6),_AcSoftwareVendor_Type())
acSoftwareVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:acSoftwareVendor.setStatus(_A)
_ApPhyInterfaceConfigurationParametersTable_Object=MibTable
apPhyInterfaceConfigurationParametersTable=_ApPhyInterfaceConfigurationParametersTable_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,6))
if mibBuilder.loadTexts:apPhyInterfaceConfigurationParametersTable.setStatus(_A)
_ApPhyInterfaceConfigurationParametersEntry_Object=MibTableRow
apPhyInterfaceConfigurationParametersEntry=_ApPhyInterfaceConfigurationParametersEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,6,1))
apPhyInterfaceConfigurationParametersEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:apPhyInterfaceConfigurationParametersEntry.setStatus(_A)
_ApIfNumber_Type=Integer32
_ApIfNumber_Object=MibTableColumn
apIfNumber=_ApIfNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,6,1,1),_ApIfNumber_Type())
apIfNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfNumber.setStatus(_A)
class _ApIfDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ApIfDescr_Type.__name__=_H
_ApIfDescr_Object=MibTableColumn
apIfDescr=_ApIfDescr_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,6,1,2),_ApIfDescr_Type())
apIfDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfDescr.setStatus(_A)
_ApIfType_Type=Integer32
_ApIfType_Object=MibTableColumn
apIfType=_ApIfType_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,6,1,3),_ApIfType_Type())
apIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfType.setStatus(_A)
_ApIfMtu_Type=Integer32
_ApIfMtu_Object=MibTableColumn
apIfMtu=_ApIfMtu_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,6,1,4),_ApIfMtu_Type())
apIfMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfMtu.setStatus(_A)
_ApIfSpeed_Type=Gauge32
_ApIfSpeed_Object=MibTableColumn
apIfSpeed=_ApIfSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,6,1,5),_ApIfSpeed_Type())
apIfSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfSpeed.setStatus(_A)
_ApIfPhysAddress_Type=OctetString
_ApIfPhysAddress_Object=MibTableColumn
apIfPhysAddress=_ApIfPhysAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,6,1,6),_ApIfPhysAddress_Type())
apIfPhysAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfPhysAddress.setStatus(_A)
_RadioInterfacePerformanceParameterTable_Object=MibTable
radioInterfacePerformanceParameterTable=_RadioInterfacePerformanceParameterTable_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,7))
if mibBuilder.loadTexts:radioInterfacePerformanceParameterTable.setStatus(_A)
_RadioInterfacePerformanceParameterEntry_Object=MibTableRow
radioInterfacePerformanceParameterEntry=_RadioInterfacePerformanceParameterEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,7,1))
radioInterfacePerformanceParameterEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:radioInterfacePerformanceParameterEntry.setStatus(_A)
_ApUplinkUpdownTimes_Type=Counter32
_ApUplinkUpdownTimes_Object=MibTableColumn
apUplinkUpdownTimes=_ApUplinkUpdownTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,7,1,1),_ApUplinkUpdownTimes_Type())
apUplinkUpdownTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:apUplinkUpdownTimes.setStatus(_A)
_ApDownlinkUpdownTimes_Type=Counter32
_ApDownlinkUpdownTimes_Object=MibTableColumn
apDownlinkUpdownTimes=_ApDownlinkUpdownTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,70,1,7,1,2),_ApDownlinkUpdownTimes_Type())
apDownlinkUpdownTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:apDownlinkUpdownTimes.setStatus(_A)
_CmStandardCompliances_ObjectIdentity=ObjectIdentity
cmStandardCompliances=_CmStandardCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,70,2))
_CmStandardGroup_ObjectIdentity=ObjectIdentity
cmStandardGroup=_CmStandardGroup_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,70,3))
_CmStandardWAPITrapsObjects_ObjectIdentity=ObjectIdentity
cmStandardWAPITrapsObjects=_CmStandardWAPITrapsObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,70,4))
_ApOriginalIP_Type=IpAddress
_ApOriginalIP_Object=MibScalar
apOriginalIP=_ApOriginalIP_Object((1,3,6,1,4,1,27514,1,1,10,2,70,4,1),_ApOriginalIP_Type())
apOriginalIP.setMaxAccess(_C)
if mibBuilder.loadTexts:apOriginalIP.setStatus(_A)
_ApCurrentIP_Type=IpAddress
_ApCurrentIP_Object=MibScalar
apCurrentIP=_ApCurrentIP_Object((1,3,6,1,4,1,27514,1,1,10,2,70,4,2),_ApCurrentIP_Type())
apCurrentIP.setMaxAccess(_C)
if mibBuilder.loadTexts:apCurrentIP.setStatus(_A)
_QtechWAPIClientIP_Type=IpAddress
_QtechWAPIClientIP_Object=MibScalar
qtechWAPIClientIP=_QtechWAPIClientIP_Object((1,3,6,1,4,1,27514,1,1,10,2,70,4,3),_QtechWAPIClientIP_Type())
qtechWAPIClientIP.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWAPIClientIP.setStatus(_A)
_QtechWAPIClientOtherInfo_Type=DisplayString
_QtechWAPIClientOtherInfo_Object=MibScalar
qtechWAPIClientOtherInfo=_QtechWAPIClientOtherInfo_Object((1,3,6,1,4,1,27514,1,1,10,2,70,4,4),_QtechWAPIClientOtherInfo_Type())
qtechWAPIClientOtherInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWAPIClientOtherInfo.setStatus(_A)
_QtechWAPIIllegalClientIP_Type=IpAddress
_QtechWAPIIllegalClientIP_Object=MibScalar
qtechWAPIIllegalClientIP=_QtechWAPIIllegalClientIP_Object((1,3,6,1,4,1,27514,1,1,10,2,70,4,5),_QtechWAPIIllegalClientIP_Type())
qtechWAPIIllegalClientIP.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWAPIIllegalClientIP.setStatus(_A)
_QtechWAPIIllegalClientOtherInfo_Type=DisplayString
_QtechWAPIIllegalClientOtherInfo_Object=MibScalar
qtechWAPIIllegalClientOtherInfo=_QtechWAPIIllegalClientOtherInfo_Object((1,3,6,1,4,1,27514,1,1,10,2,70,4,6),_QtechWAPIIllegalClientOtherInfo_Type())
qtechWAPIIllegalClientOtherInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWAPIIllegalClientOtherInfo.setStatus(_A)
cmStandardBase=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,70,3,1))
cmStandardBase.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,'apIfType'),(_B,'apIfMtu'),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:cmStandardBase.setStatus(_A)
apDown=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,70,0,1))
if mibBuilder.loadTexts:apDown.setStatus(_A)
apSysStart=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,70,0,2))
if mibBuilder.loadTexts:apSysStart.setStatus(_A)
apIPChangeAlarm=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,70,0,3))
apIPChangeAlarm.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:apIPChangeAlarm.setStatus(_A)
flashWriteFail=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,70,0,4))
if mibBuilder.loadTexts:flashWriteFail.setStatus(_A)
userwithInvalidCerficationInbreakNetwork=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,70,0,5))
userwithInvalidCerficationInbreakNetwork.setObjects(*((_B,_L),(_B,_M)))
if mibBuilder.loadTexts:userwithInvalidCerficationInbreakNetwork.setStatus(_A)
stationRepititiveAttack=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,70,0,6))
stationRepititiveAttack.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:stationRepititiveAttack.setStatus(_A)
tamperAttack=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,70,0,7))
tamperAttack.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:tamperAttack.setStatus(_A)
lowSafeLevelAttack=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,70,0,8))
lowSafeLevelAttack.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:lowSafeLevelAttack.setStatus(_A)
addressRedirectionAttack=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,70,0,9))
addressRedirectionAttack.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:addressRedirectionAttack.setStatus(_A)
cmStandardCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,70,2,2))
cmStandardCompliance.setObjects((_B,_A6))
if mibBuilder.loadTexts:cmStandardCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cmStandardmibmodule':cmStandardmibmodule,'cmStandardWAPITraps':cmStandardWAPITraps,'apDown':apDown,'apSysStart':apSysStart,'apIPChangeAlarm':apIPChangeAlarm,'flashWriteFail':flashWriteFail,'userwithInvalidCerficationInbreakNetwork':userwithInvalidCerficationInbreakNetwork,'stationRepititiveAttack':stationRepititiveAttack,'tamperAttack':tamperAttack,'lowSafeLevelAttack':lowSafeLevelAttack,'addressRedirectionAttack':addressRedirectionAttack,'cmStandardMIBObjects':cmStandardMIBObjects,'apAttributeInfoTable':apAttributeInfoTable,'apAttributeInfoEntry':apAttributeInfoEntry,_P:apSysNEId,_Q:apSysHostName,_R:apSysLocation,_S:apManufacturer,_T:apSysVersion,_U:apMacAddressConnectedWithAC,_V:apCurrentBSSID,_W:apMaxSimultUsers,_X:apMaxSimultTraffic,_Y:apUpTime,'apconfigurationInfoTable':apconfigurationInfoTable,'apconfigurationInfoEntry':apconfigurationInfoEntry,_Z:apIPAddress,_a:apIpAdEntNetMask,_b:apWorkingMode,_c:apBGmode,'apacWAPIconfigurationInfoTable':apacWAPIconfigurationInfoTable,'apacWAPIconfigurationInfoEntry':apacWAPIconfigurationInfoEntry,_d:apWAPIAuthMode,_e:acWAPIAuthMode,_f:acWAPIASIPAddress,_g:acWAPICertInstalled,_h:cpuHandleAbility,_i:memoryCapacity,_j:flashmemCapacity,_k:support80211g,_l:apWAPIMaxUserNum,_m:peruserWAPIMaxBindwithAllocated,_n:mutiModeAccesssimultStatus,'gb15629dot11wapiConfigExtraTable':gb15629dot11wapiConfigExtraTable,'gb15629dot11wapiConfigExtraEntry':gb15629dot11wapiConfigExtraEntry,_o:gb15629dot11wapiGroupCipherRequested,_p:gb15629dot11wapiConfigUnicastCipher,_q:gb15629dot11wapiConfigUnicastCipherEnabled,_r:gb15629dot11wapiConfigUnicastCipherSize,_s:gb15629dot11wapiConfigAuthenticationSuite,_t:gb15629dot11wapiConfigAuthenticationSuiteEnabled,'apacsoftorHardwareconfigInfoTable':apacsoftorHardwareconfigInfoTable,'apacsoftorHardwareconfigInfoEntry':apacsoftorHardwareconfigInfoEntry,_u:apSoftwareName,_v:apSoftwareVersion,_w:apSoftwareVendor,_x:acSoftwareName,_y:acSoftwareVersion,_z:acSoftwareVendor,'apPhyInterfaceConfigurationParametersTable':apPhyInterfaceConfigurationParametersTable,'apPhyInterfaceConfigurationParametersEntry':apPhyInterfaceConfigurationParametersEntry,_A0:apIfNumber,_A1:apIfDescr,'apIfType':apIfType,'apIfMtu':apIfMtu,_A2:apIfSpeed,_A3:apIfPhysAddress,'radioInterfacePerformanceParameterTable':radioInterfacePerformanceParameterTable,'radioInterfacePerformanceParameterEntry':radioInterfacePerformanceParameterEntry,_A4:apUplinkUpdownTimes,_A5:apDownlinkUpdownTimes,'cmStandardCompliances':cmStandardCompliances,'cmStandardCompliance':cmStandardCompliance,'cmStandardGroup':cmStandardGroup,_A6:cmStandardBase,'cmStandardWAPITrapsObjects':cmStandardWAPITrapsObjects,_J:apOriginalIP,_K:apCurrentIP,_L:qtechWAPIClientIP,_M:qtechWAPIClientOtherInfo,_F:qtechWAPIIllegalClientIP,_G:qtechWAPIIllegalClientOtherInfo})