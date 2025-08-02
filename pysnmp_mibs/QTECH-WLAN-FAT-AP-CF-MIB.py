_r='apAuthFailReason'
_q='apAuthMode'
_p='apChanChangeMode'
_o='apChannelAfterChange'
_n='apChannelBeforeChange'
_m='apTimeStamp'
_l='apIpAddr'
_k='apCyperIndex'
_j='apSSIDKeyConflict'
_i='apSSIDKey'
_h='apAPMac'
_g='apCurrentIpAddr'
_f='apOriginalIpAddr'
_e='apSTAAddress'
_d='apStaAddress'
_c='apTrapEnabledIndex'
_b='apTrapDesAddrIndex'
_a='apBlackListIndex'
_Z='apWhiteListIndex'
_Y='apSyslogSvrIndex'
_X='apQoSTrafficClassIndex'
_W='apStaMAC'
_V='admindown'
_U='apPermitAssoUser'
_T='apInterruptReason'
_S='apInterfStaMac'
_R='apInterfAPChannel'
_Q='DisplayString'
_P='apAssoFailReason'
_O='apInterfAPBSSID'
_N='Integer32'
_M='apStaMacAddr'
_L='apWorkingAPSSID'
_K='apWorkingAPBSSID'
_J='apWorkingAPChannel'
_I='apWlanId'
_H='ifIndex'
_G='IF-MIB'
_F='apWorkingAPRadioIfInfo'
_E='read-create'
_D='QTECH-WLAN-FAT-AP-CF-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
ifIndex,=mibBuilder.importSymbols(_G,_H)
qtechApgWlanId,=mibBuilder.importSymbols('QTECH-AC-MGMT-MIB','qtechApgWlanId')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_N,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_Q,'MacAddress','PhysAddress','RowStatus','TAddress','TextualConvention','TruthValue')
apStandardmibmodule=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,80))
if mibBuilder.loadTexts:apStandardmibmodule.setRevisions(('2010-02-28 00:00',))
_ApStandardSysTraps_ObjectIdentity=ObjectIdentity
apStandardSysTraps=_ApStandardSysTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,0))
_ApStandardSysTrapsObjects_ObjectIdentity=ObjectIdentity
apStandardSysTrapsObjects=_ApStandardSysTrapsObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,1))
_ApOriginalIpAddr_Type=IpAddress
_ApOriginalIpAddr_Object=MibScalar
apOriginalIpAddr=_ApOriginalIpAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,80,1,1),_ApOriginalIpAddr_Type())
apOriginalIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:apOriginalIpAddr.setStatus(_A)
_ApCurrentIpAddr_Type=IpAddress
_ApCurrentIpAddr_Object=MibScalar
apCurrentIpAddr=_ApCurrentIpAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,80,1,2),_ApCurrentIpAddr_Type())
apCurrentIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:apCurrentIpAddr.setStatus(_A)
_ApIpAddr_Type=IpAddress
_ApIpAddr_Object=MibScalar
apIpAddr=_ApIpAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,80,1,3),_ApIpAddr_Type())
apIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:apIpAddr.setStatus(_A)
_ApTimeStamp_Type=TimeTicks
_ApTimeStamp_Object=MibScalar
apTimeStamp=_ApTimeStamp_Object((1,3,6,1,4,1,27514,1,1,10,2,80,1,4),_ApTimeStamp_Type())
apTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:apTimeStamp.setStatus(_A)
_ApAPMac_Type=MacAddress
_ApAPMac_Object=MibScalar
apAPMac=_ApAPMac_Object((1,3,6,1,4,1,27514,1,1,10,2,80,1,5),_ApAPMac_Type())
apAPMac.setMaxAccess(_B)
if mibBuilder.loadTexts:apAPMac.setStatus(_A)
_ApSSIDKey_Type=DisplayString
_ApSSIDKey_Object=MibScalar
apSSIDKey=_ApSSIDKey_Object((1,3,6,1,4,1,27514,1,1,10,2,80,1,6),_ApSSIDKey_Type())
apSSIDKey.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDKey.setStatus(_A)
_ApSSIDKeyConflict_Type=DisplayString
_ApSSIDKeyConflict_Object=MibScalar
apSSIDKeyConflict=_ApSSIDKeyConflict_Object((1,3,6,1,4,1,27514,1,1,10,2,80,1,7),_ApSSIDKeyConflict_Type())
apSSIDKeyConflict.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDKeyConflict.setStatus(_A)
_ApCyperIndex_Type=Integer32
_ApCyperIndex_Object=MibScalar
apCyperIndex=_ApCyperIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,80,1,8),_ApCyperIndex_Type())
apCyperIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:apCyperIndex.setStatus(_A)
_ApStandardRadioTraps_ObjectIdentity=ObjectIdentity
apStandardRadioTraps=_ApStandardRadioTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,2))
_ApStandardRadioTrapsObjects_ObjectIdentity=ObjectIdentity
apStandardRadioTrapsObjects=_ApStandardRadioTrapsObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,3))
_ApInterruptReason_Type=DisplayString
_ApInterruptReason_Object=MibScalar
apInterruptReason=_ApInterruptReason_Object((1,3,6,1,4,1,27514,1,1,10,2,80,3,1),_ApInterruptReason_Type())
apInterruptReason.setMaxAccess(_B)
if mibBuilder.loadTexts:apInterruptReason.setStatus(_A)
_ApWorkingAPRadioIfInfo_Type=MacAddress
_ApWorkingAPRadioIfInfo_Object=MibScalar
apWorkingAPRadioIfInfo=_ApWorkingAPRadioIfInfo_Object((1,3,6,1,4,1,27514,1,1,10,2,80,3,2),_ApWorkingAPRadioIfInfo_Type())
apWorkingAPRadioIfInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:apWorkingAPRadioIfInfo.setStatus(_A)
_ApWorkingAPChannel_Type=Integer32
_ApWorkingAPChannel_Object=MibScalar
apWorkingAPChannel=_ApWorkingAPChannel_Object((1,3,6,1,4,1,27514,1,1,10,2,80,3,3),_ApWorkingAPChannel_Type())
apWorkingAPChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:apWorkingAPChannel.setStatus(_A)
_ApInterfAPChannel_Type=Integer32
_ApInterfAPChannel_Object=MibScalar
apInterfAPChannel=_ApInterfAPChannel_Object((1,3,6,1,4,1,27514,1,1,10,2,80,3,4),_ApInterfAPChannel_Type())
apInterfAPChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:apInterfAPChannel.setStatus(_A)
_ApInterfAPBSSID_Type=MacAddress
_ApInterfAPBSSID_Object=MibScalar
apInterfAPBSSID=_ApInterfAPBSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,80,3,5),_ApInterfAPBSSID_Type())
apInterfAPBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:apInterfAPBSSID.setStatus(_A)
_ApInterfStaMac_Type=MacAddress
_ApInterfStaMac_Object=MibScalar
apInterfStaMac=_ApInterfStaMac_Object((1,3,6,1,4,1,27514,1,1,10,2,80,3,6),_ApInterfStaMac_Type())
apInterfStaMac.setMaxAccess(_B)
if mibBuilder.loadTexts:apInterfStaMac.setStatus(_A)
_ApPermitAssoUser_Type=Integer32
_ApPermitAssoUser_Object=MibScalar
apPermitAssoUser=_ApPermitAssoUser_Object((1,3,6,1,4,1,27514,1,1,10,2,80,3,7),_ApPermitAssoUser_Type())
apPermitAssoUser.setMaxAccess(_B)
if mibBuilder.loadTexts:apPermitAssoUser.setStatus(_A)
_ApAssoFailReason_Type=DisplayString
_ApAssoFailReason_Object=MibScalar
apAssoFailReason=_ApAssoFailReason_Object((1,3,6,1,4,1,27514,1,1,10,2,80,3,8),_ApAssoFailReason_Type())
apAssoFailReason.setMaxAccess(_B)
if mibBuilder.loadTexts:apAssoFailReason.setStatus(_A)
_ApChannelBeforeChange_Type=Integer32
_ApChannelBeforeChange_Object=MibScalar
apChannelBeforeChange=_ApChannelBeforeChange_Object((1,3,6,1,4,1,27514,1,1,10,2,80,3,9),_ApChannelBeforeChange_Type())
apChannelBeforeChange.setMaxAccess(_B)
if mibBuilder.loadTexts:apChannelBeforeChange.setStatus(_A)
_ApChannelAfterChange_Type=Integer32
_ApChannelAfterChange_Object=MibScalar
apChannelAfterChange=_ApChannelAfterChange_Object((1,3,6,1,4,1,27514,1,1,10,2,80,3,10),_ApChannelAfterChange_Type())
apChannelAfterChange.setMaxAccess(_B)
if mibBuilder.loadTexts:apChannelAfterChange.setStatus(_A)
_ApChanChangeMode_Type=Integer32
_ApChanChangeMode_Object=MibScalar
apChanChangeMode=_ApChanChangeMode_Object((1,3,6,1,4,1,27514,1,1,10,2,80,3,11),_ApChanChangeMode_Type())
apChanChangeMode.setMaxAccess(_B)
if mibBuilder.loadTexts:apChanChangeMode.setStatus(_A)
_ApStandardTerminalTraps_ObjectIdentity=ObjectIdentity
apStandardTerminalTraps=_ApStandardTerminalTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,4))
_ApStandardTerminalTrapsObjects_ObjectIdentity=ObjectIdentity
apStandardTerminalTrapsObjects=_ApStandardTerminalTrapsObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,5))
_ApWorkingAPBSSID_Type=MacAddress
_ApWorkingAPBSSID_Object=MibScalar
apWorkingAPBSSID=_ApWorkingAPBSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,80,5,1),_ApWorkingAPBSSID_Type())
apWorkingAPBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:apWorkingAPBSSID.setStatus(_A)
_ApWorkingAPSSID_Type=MacAddress
_ApWorkingAPSSID_Object=MibScalar
apWorkingAPSSID=_ApWorkingAPSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,80,5,2),_ApWorkingAPSSID_Type())
apWorkingAPSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:apWorkingAPSSID.setStatus(_A)
_ApStaMacAddr_Type=MacAddress
_ApStaMacAddr_Object=MibScalar
apStaMacAddr=_ApStaMacAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,80,5,3),_ApStaMacAddr_Type())
apStaMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaMacAddr.setStatus(_A)
_ApAuthMode_Type=Integer32
_ApAuthMode_Object=MibScalar
apAuthMode=_ApAuthMode_Object((1,3,6,1,4,1,27514,1,1,10,2,80,5,4),_ApAuthMode_Type())
apAuthMode.setMaxAccess(_B)
if mibBuilder.loadTexts:apAuthMode.setStatus(_A)
_ApAuthFailReason_Type=DisplayString
_ApAuthFailReason_Object=MibScalar
apAuthFailReason=_ApAuthFailReason_Object((1,3,6,1,4,1,27514,1,1,10,2,80,5,5),_ApAuthFailReason_Type())
apAuthFailReason.setMaxAccess(_B)
if mibBuilder.loadTexts:apAuthFailReason.setStatus(_A)
_ApStandardAuthSvrTraps_ObjectIdentity=ObjectIdentity
apStandardAuthSvrTraps=_ApStandardAuthSvrTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,6))
_ApStandardWapiScrTraps_ObjectIdentity=ObjectIdentity
apStandardWapiScrTraps=_ApStandardWapiScrTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,7))
_ApConfigInfoObjects_ObjectIdentity=ObjectIdentity
apConfigInfoObjects=_ApConfigInfoObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,8))
_ApSysInfoObjects_ObjectIdentity=ObjectIdentity
apSysInfoObjects=_ApSysInfoObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,8,1))
class _ApSysNetID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,255))
_ApSysNetID_Type.__name__=_Q
_ApSysNetID_Object=MibScalar
apSysNetID=_ApSysNetID_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,1),_ApSysNetID_Type())
apSysNetID.setMaxAccess(_C)
if mibBuilder.loadTexts:apSysNetID.setStatus(_A)
class _ApSysHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(40,255))
_ApSysHostName_Type.__name__=_Q
_ApSysHostName_Object=MibScalar
apSysHostName=_ApSysHostName_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,2),_ApSysHostName_Type())
apSysHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:apSysHostName.setStatus(_A)
_ApSysDescr_Type=DisplayString
_ApSysDescr_Object=MibScalar
apSysDescr=_ApSysDescr_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,3),_ApSysDescr_Type())
apSysDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:apSysDescr.setStatus(_A)
_ApManufacturer_Type=DisplayString
_ApManufacturer_Object=MibScalar
apManufacturer=_ApManufacturer_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,4),_ApManufacturer_Type())
apManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:apManufacturer.setStatus(_A)
_ApSerialNumber_Type=DisplayString
_ApSerialNumber_Object=MibScalar
apSerialNumber=_ApSerialNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,5),_ApSerialNumber_Type())
apSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:apSerialNumber.setStatus(_A)
_ApSysModel_Type=DisplayString
_ApSysModel_Object=MibScalar
apSysModel=_ApSysModel_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,6),_ApSysModel_Type())
apSysModel.setMaxAccess(_B)
if mibBuilder.loadTexts:apSysModel.setStatus(_A)
_ApSysTime_Type=DisplayString
_ApSysTime_Object=MibScalar
apSysTime=_ApSysTime_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,7),_ApSysTime_Type())
apSysTime.setMaxAccess(_C)
if mibBuilder.loadTexts:apSysTime.setStatus(_A)
_ApSysUpTime_Type=TimeTicks
_ApSysUpTime_Object=MibScalar
apSysUpTime=_ApSysUpTime_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,8),_ApSysUpTime_Type())
apSysUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:apSysUpTime.setStatus(_A)
_ApSysIPAddress_Type=IpAddress
_ApSysIPAddress_Object=MibScalar
apSysIPAddress=_ApSysIPAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,9),_ApSysIPAddress_Type())
apSysIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:apSysIPAddress.setStatus(_A)
_ApSysIPNetMask_Type=IpAddress
_ApSysIPNetMask_Object=MibScalar
apSysIPNetMask=_ApSysIPNetMask_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,10),_ApSysIPNetMask_Type())
apSysIPNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:apSysIPNetMask.setStatus(_A)
_ApSysGWAddr_Type=IpAddress
_ApSysGWAddr_Object=MibScalar
apSysGWAddr=_ApSysGWAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,11),_ApSysGWAddr_Type())
apSysGWAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:apSysGWAddr.setStatus(_A)
_ApPrimDNSServerIPAdd_Type=IpAddress
_ApPrimDNSServerIPAdd_Object=MibScalar
apPrimDNSServerIPAdd=_ApPrimDNSServerIPAdd_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,12),_ApPrimDNSServerIPAdd_Type())
apPrimDNSServerIPAdd.setMaxAccess(_C)
if mibBuilder.loadTexts:apPrimDNSServerIPAdd.setStatus(_A)
_ApSeconDNSServerIPAdd_Type=IpAddress
_ApSeconDNSServerIPAdd_Object=MibScalar
apSeconDNSServerIPAdd=_ApSeconDNSServerIPAdd_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,13),_ApSeconDNSServerIPAdd_Type())
apSeconDNSServerIPAdd.setMaxAccess(_C)
if mibBuilder.loadTexts:apSeconDNSServerIPAdd.setStatus(_A)
_ApSysMacAddress_Type=MacAddress
_ApSysMacAddress_Object=MibScalar
apSysMacAddress=_ApSysMacAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,14),_ApSysMacAddress_Type())
apSysMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:apSysMacAddress.setStatus(_A)
_ApReadCommunityName_Type=DisplayString
_ApReadCommunityName_Object=MibScalar
apReadCommunityName=_ApReadCommunityName_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,15),_ApReadCommunityName_Type())
apReadCommunityName.setMaxAccess(_C)
if mibBuilder.loadTexts:apReadCommunityName.setStatus(_A)
_ApWriteCommunityName_Type=DisplayString
_ApWriteCommunityName_Object=MibScalar
apWriteCommunityName=_ApWriteCommunityName_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,16),_ApWriteCommunityName_Type())
apWriteCommunityName.setMaxAccess(_C)
if mibBuilder.loadTexts:apWriteCommunityName.setStatus(_A)
_ApStatWindowTime_Type=TimeTicks
_ApStatWindowTime_Object=MibScalar
apStatWindowTime=_ApStatWindowTime_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,17),_ApStatWindowTime_Type())
apStatWindowTime.setMaxAccess(_C)
if mibBuilder.loadTexts:apStatWindowTime.setStatus(_A)
_ApSampleTime_Type=Integer32
_ApSampleTime_Object=MibScalar
apSampleTime=_ApSampleTime_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,18),_ApSampleTime_Type())
apSampleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:apSampleTime.setStatus(_A)
_ApSysRestart_Type=Integer32
_ApSysRestart_Object=MibScalar
apSysRestart=_ApSysRestart_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,19),_ApSysRestart_Type())
apSysRestart.setMaxAccess(_C)
if mibBuilder.loadTexts:apSysRestart.setStatus(_A)
_ApSysReset_Type=Integer32
_ApSysReset_Object=MibScalar
apSysReset=_ApSysReset_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,20),_ApSysReset_Type())
apSysReset.setMaxAccess(_C)
if mibBuilder.loadTexts:apSysReset.setStatus(_A)
_ApSoftwareName_Type=DisplayString
_ApSoftwareName_Object=MibScalar
apSoftwareName=_ApSoftwareName_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,21),_ApSoftwareName_Type())
apSoftwareName.setMaxAccess(_B)
if mibBuilder.loadTexts:apSoftwareName.setStatus(_A)
_ApSoftwareVersion_Type=DisplayString
_ApSoftwareVersion_Object=MibScalar
apSoftwareVersion=_ApSoftwareVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,22),_ApSoftwareVersion_Type())
apSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:apSoftwareVersion.setStatus(_A)
_ApSoftwareVendor_Type=DisplayString
_ApSoftwareVendor_Object=MibScalar
apSoftwareVendor=_ApSoftwareVendor_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,23),_ApSoftwareVendor_Type())
apSoftwareVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:apSoftwareVendor.setStatus(_A)
_ApCPUType_Type=DisplayString
_ApCPUType_Object=MibScalar
apCPUType=_ApCPUType_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,24),_ApCPUType_Type())
apCPUType.setMaxAccess(_B)
if mibBuilder.loadTexts:apCPUType.setStatus(_A)
_ApMemoryType_Type=DisplayString
_ApMemoryType_Object=MibScalar
apMemoryType=_ApMemoryType_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,25),_ApMemoryType_Type())
apMemoryType.setMaxAccess(_B)
if mibBuilder.loadTexts:apMemoryType.setStatus(_A)
_ApMemorySize_Type=Gauge32
_ApMemorySize_Object=MibScalar
apMemorySize=_ApMemorySize_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,26),_ApMemorySize_Type())
apMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:apMemorySize.setStatus(_A)
_ApFlashSize_Type=Gauge32
_ApFlashSize_Object=MibScalar
apFlashSize=_ApFlashSize_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,1,27),_ApFlashSize_Type())
apFlashSize.setMaxAccess(_B)
if mibBuilder.loadTexts:apFlashSize.setStatus(_A)
_ApPhyInterfaceConfig_ObjectIdentity=ObjectIdentity
apPhyInterfaceConfig=_ApPhyInterfaceConfig_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,8,2))
_ApIfNumber_Type=Integer32
_ApIfNumber_Object=MibScalar
apIfNumber=_ApIfNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,2,1),_ApIfNumber_Type())
apIfNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfNumber.setStatus(_A)
_ApWiredInterfaceCfgTable_Object=MibTable
apWiredInterfaceCfgTable=_ApWiredInterfaceCfgTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,2,2))
if mibBuilder.loadTexts:apWiredInterfaceCfgTable.setStatus(_A)
_ApWiredInterfaceCfgEntry_Object=MibTableRow
apWiredInterfaceCfgEntry=_ApWiredInterfaceCfgEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,2,2,1))
apWiredInterfaceCfgEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:apWiredInterfaceCfgEntry.setStatus(_A)
_ApIfDescr_Type=DisplayString
_ApIfDescr_Object=MibTableColumn
apIfDescr=_ApIfDescr_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,2,2,1,1),_ApIfDescr_Type())
apIfDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfDescr.setStatus(_A)
_ApIfType_Type=IANAifType
_ApIfType_Object=MibTableColumn
apIfType=_ApIfType_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,2,2,1,2),_ApIfType_Type())
apIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfType.setStatus(_A)
_ApIfMTU_Type=Integer32
_ApIfMTU_Object=MibTableColumn
apIfMTU=_ApIfMTU_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,2,2,1,3),_ApIfMTU_Type())
apIfMTU.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfMTU.setStatus(_A)
_ApIfSpeed_Type=Integer32
_ApIfSpeed_Object=MibTableColumn
apIfSpeed=_ApIfSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,2,2,1,4),_ApIfSpeed_Type())
apIfSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfSpeed.setStatus(_A)
_ApIfPhysAddress_Type=MacAddress
_ApIfPhysAddress_Object=MibTableColumn
apIfPhysAddress=_ApIfPhysAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,2,2,1,5),_ApIfPhysAddress_Type())
apIfPhysAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfPhysAddress.setStatus(_A)
_ApIfAdminStatus_Type=Integer32
_ApIfAdminStatus_Object=MibTableColumn
apIfAdminStatus=_ApIfAdminStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,2,2,1,6),_ApIfAdminStatus_Type())
apIfAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:apIfAdminStatus.setStatus(_A)
_ApIfOperStatus_Type=Integer32
_ApIfOperStatus_Object=MibTableColumn
apIfOperStatus=_ApIfOperStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,2,2,1,7),_ApIfOperStatus_Type())
apIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfOperStatus.setStatus(_A)
_ApIfLastChange_Type=TimeTicks
_ApIfLastChange_Object=MibTableColumn
apIfLastChange=_ApIfLastChange_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,2,2,1,8),_ApIfLastChange_Type())
apIfLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfLastChange.setStatus(_A)
_ApRadioInterfaceCfg_ObjectIdentity=ObjectIdentity
apRadioInterfaceCfg=_ApRadioInterfaceCfg_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,8,3))
_ApRadioInterfaceInfoTable_Object=MibTable
apRadioInterfaceInfoTable=_ApRadioInterfaceInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1))
if mibBuilder.loadTexts:apRadioInterfaceInfoTable.setStatus(_A)
_ApRadioInterfaceInfoEntry_Object=MibTableRow
apRadioInterfaceInfoEntry=_ApRadioInterfaceInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1))
apRadioInterfaceInfoEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:apRadioInterfaceInfoEntry.setStatus(_A)
_ApRadioIfDescr_Type=DisplayString
_ApRadioIfDescr_Object=MibTableColumn
apRadioIfDescr=_ApRadioIfDescr_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,1),_ApRadioIfDescr_Type())
apRadioIfDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:apRadioIfDescr.setStatus(_A)
_ApRadioIfType_Type=IANAifType
_ApRadioIfType_Object=MibTableColumn
apRadioIfType=_ApRadioIfType_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,2),_ApRadioIfType_Type())
apRadioIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:apRadioIfType.setStatus(_A)
_ApRadioIfMTU_Type=Integer32
_ApRadioIfMTU_Object=MibTableColumn
apRadioIfMTU=_ApRadioIfMTU_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,3),_ApRadioIfMTU_Type())
apRadioIfMTU.setMaxAccess(_B)
if mibBuilder.loadTexts:apRadioIfMTU.setStatus(_A)
_ApRadioIfSpeed_Type=Integer32
_ApRadioIfSpeed_Object=MibTableColumn
apRadioIfSpeed=_ApRadioIfSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,4),_ApRadioIfSpeed_Type())
apRadioIfSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:apRadioIfSpeed.setStatus(_A)
_ApRadioIfMacAddress_Type=MacAddress
_ApRadioIfMacAddress_Object=MibTableColumn
apRadioIfMacAddress=_ApRadioIfMacAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,5),_ApRadioIfMacAddress_Type())
apRadioIfMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:apRadioIfMacAddress.setStatus(_A)
class _ApRadioIfDiversity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_ApRadioIfDiversity_Type.__name__=_N
_ApRadioIfDiversity_Object=MibTableColumn
apRadioIfDiversity=_ApRadioIfDiversity_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,6),_ApRadioIfDiversity_Type())
apRadioIfDiversity.setMaxAccess(_B)
if mibBuilder.loadTexts:apRadioIfDiversity.setStatus(_A)
class _ApRadioIfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_V,3)))
_ApRadioIfAdminStatus_Type.__name__=_N
_ApRadioIfAdminStatus_Object=MibTableColumn
apRadioIfAdminStatus=_ApRadioIfAdminStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,7),_ApRadioIfAdminStatus_Type())
apRadioIfAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadioIfAdminStatus.setStatus(_A)
class _ApRadioIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_V,3)))
_ApRadioIfOperStatus_Type.__name__=_N
_ApRadioIfOperStatus_Object=MibTableColumn
apRadioIfOperStatus=_ApRadioIfOperStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,8),_ApRadioIfOperStatus_Type())
apRadioIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:apRadioIfOperStatus.setStatus(_A)
_ApRadioIfLastChange_Type=TimeTicks
_ApRadioIfLastChange_Object=MibTableColumn
apRadioIfLastChange=_ApRadioIfLastChange_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,9),_ApRadioIfLastChange_Type())
apRadioIfLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:apRadioIfLastChange.setStatus(_A)
_ApRadioChannelAutoSelectEnable_Type=Integer32
_ApRadioChannelAutoSelectEnable_Object=MibTableColumn
apRadioChannelAutoSelectEnable=_ApRadioChannelAutoSelectEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,10),_ApRadioChannelAutoSelectEnable_Type())
apRadioChannelAutoSelectEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadioChannelAutoSelectEnable.setStatus(_A)
_ApRadioChannelConfig_Type=Integer32
_ApRadioChannelConfig_Object=MibTableColumn
apRadioChannelConfig=_ApRadioChannelConfig_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,11),_ApRadioChannelConfig_Type())
apRadioChannelConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadioChannelConfig.setStatus(_A)
_ApRadioChannelUsing_Type=Integer32
_ApRadioChannelUsing_Object=MibTableColumn
apRadioChannelUsing=_ApRadioChannelUsing_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,12),_ApRadioChannelUsing_Type())
apRadioChannelUsing.setMaxAccess(_B)
if mibBuilder.loadTexts:apRadioChannelUsing.setStatus(_A)
_ApCurrRadioModeSupport_Type=Integer32
_ApCurrRadioModeSupport_Object=MibTableColumn
apCurrRadioModeSupport=_ApCurrRadioModeSupport_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,13),_ApCurrRadioModeSupport_Type())
apCurrRadioModeSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:apCurrRadioModeSupport.setStatus(_A)
_ApRadioModeConfig_Type=Integer32
_ApRadioModeConfig_Object=MibTableColumn
apRadioModeConfig=_ApRadioModeConfig_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,14),_ApRadioModeConfig_Type())
apRadioModeConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadioModeConfig.setStatus(_A)
_ApTransmitSpeedConfig_Type=DisplayString
_ApTransmitSpeedConfig_Object=MibTableColumn
apTransmitSpeedConfig=_ApTransmitSpeedConfig_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,15),_ApTransmitSpeedConfig_Type())
apTransmitSpeedConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:apTransmitSpeedConfig.setStatus(_A)
_ApMaxTxPwrLvl_Type=DisplayString
_ApMaxTxPwrLvl_Object=MibTableColumn
apMaxTxPwrLvl=_ApMaxTxPwrLvl_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,16),_ApMaxTxPwrLvl_Type())
apMaxTxPwrLvl.setMaxAccess(_B)
if mibBuilder.loadTexts:apMaxTxPwrLvl.setStatus(_A)
_ApTxPwr_Type=Integer32
_ApTxPwr_Object=MibTableColumn
apTxPwr=_ApTxPwr_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,17),_ApTxPwr_Type())
apTxPwr.setMaxAccess(_C)
if mibBuilder.loadTexts:apTxPwr.setStatus(_A)
_ApPwrAttRange_Type=Integer32
_ApPwrAttRange_Object=MibTableColumn
apPwrAttRange=_ApPwrAttRange_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,18),_ApPwrAttRange_Type())
apPwrAttRange.setMaxAccess(_B)
if mibBuilder.loadTexts:apPwrAttRange.setStatus(_A)
_ApPwrAttValue_Type=Integer32
_ApPwrAttValue_Object=MibTableColumn
apPwrAttValue=_ApPwrAttValue_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,19),_ApPwrAttValue_Type())
apPwrAttValue.setMaxAccess(_C)
if mibBuilder.loadTexts:apPwrAttValue.setStatus(_A)
_ApAntennaGain_Type=Integer32
_ApAntennaGain_Object=MibTableColumn
apAntennaGain=_ApAntennaGain_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,20),_ApAntennaGain_Type())
apAntennaGain.setMaxAccess(_B)
if mibBuilder.loadTexts:apAntennaGain.setStatus(_A)
_ApPowerMgmtEnable_Type=TruthValue
_ApPowerMgmtEnable_Object=MibTableColumn
apPowerMgmtEnable=_ApPowerMgmtEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,21),_ApPowerMgmtEnable_Type())
apPowerMgmtEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:apPowerMgmtEnable.setStatus(_A)
_ApMaxStationNumPermitted_Type=Integer32
_ApMaxStationNumPermitted_Object=MibTableColumn
apMaxStationNumPermitted=_ApMaxStationNumPermitted_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,22),_ApMaxStationNumPermitted_Type())
apMaxStationNumPermitted.setMaxAccess(_C)
if mibBuilder.loadTexts:apMaxStationNumPermitted.setStatus(_A)
_ApAMPDUEnabled_Type=Integer32
_ApAMPDUEnabled_Object=MibTableColumn
apAMPDUEnabled=_ApAMPDUEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,23),_ApAMPDUEnabled_Type())
apAMPDUEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:apAMPDUEnabled.setStatus(_A)
_ApBWMode_Type=Integer32
_ApBWMode_Object=MibTableColumn
apBWMode=_ApBWMode_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,24),_ApBWMode_Type())
apBWMode.setMaxAccess(_C)
if mibBuilder.loadTexts:apBWMode.setStatus(_A)
_ApShortGIEnabled_Type=Integer32
_ApShortGIEnabled_Object=MibTableColumn
apShortGIEnabled=_ApShortGIEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,25),_ApShortGIEnabled_Type())
apShortGIEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:apShortGIEnabled.setStatus(_A)
_ApIs11nOnly_Type=TruthValue
_ApIs11nOnly_Object=MibTableColumn
apIs11nOnly=_ApIs11nOnly_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,1,1,26),_ApIs11nOnly_Type())
apIs11nOnly.setMaxAccess(_C)
if mibBuilder.loadTexts:apIs11nOnly.setStatus(_A)
_ApRadioInterfacePhyParaTable_Object=MibTable
apRadioInterfacePhyParaTable=_ApRadioInterfacePhyParaTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,2))
if mibBuilder.loadTexts:apRadioInterfacePhyParaTable.setStatus(_A)
_ApRadioInterfacePhyParaEntry_Object=MibTableRow
apRadioInterfacePhyParaEntry=_ApRadioInterfacePhyParaEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,2,1))
apRadioInterfacePhyParaEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:apRadioInterfacePhyParaEntry.setStatus(_A)
_ApBeaconIntvl_Type=Integer32
_ApBeaconIntvl_Object=MibTableColumn
apBeaconIntvl=_ApBeaconIntvl_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,2,1,1),_ApBeaconIntvl_Type())
apBeaconIntvl.setMaxAccess(_C)
if mibBuilder.loadTexts:apBeaconIntvl.setStatus(_A)
_ApDtimIntvl_Type=Integer32
_ApDtimIntvl_Object=MibTableColumn
apDtimIntvl=_ApDtimIntvl_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,2,1,2),_ApDtimIntvl_Type())
apDtimIntvl.setMaxAccess(_C)
if mibBuilder.loadTexts:apDtimIntvl.setStatus(_A)
_ApRtsThreshold_Type=Integer32
_ApRtsThreshold_Object=MibTableColumn
apRtsThreshold=_ApRtsThreshold_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,2,1,3),_ApRtsThreshold_Type())
apRtsThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:apRtsThreshold.setStatus(_A)
_ApFragThreshlod_Type=Integer32
_ApFragThreshlod_Object=MibTableColumn
apFragThreshlod=_ApFragThreshlod_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,2,1,4),_ApFragThreshlod_Type())
apFragThreshlod.setMaxAccess(_C)
if mibBuilder.loadTexts:apFragThreshlod.setStatus(_A)
_ApPreambleLen_Type=Integer32
_ApPreambleLen_Object=MibTableColumn
apPreambleLen=_ApPreambleLen_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,3,2,1,5),_ApPreambleLen_Type())
apPreambleLen.setMaxAccess(_C)
if mibBuilder.loadTexts:apPreambleLen.setStatus(_A)
_ApSSIDCfg_ObjectIdentity=ObjectIdentity
apSSIDCfg=_ApSSIDCfg_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,8,4))
_ApConfigBSSIDNum_Type=Integer32
_ApConfigBSSIDNum_Object=MibScalar
apConfigBSSIDNum=_ApConfigBSSIDNum_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,4,1),_ApConfigBSSIDNum_Type())
apConfigBSSIDNum.setMaxAccess(_B)
if mibBuilder.loadTexts:apConfigBSSIDNum.setStatus(_A)
_ApRadioIfSSIDCfgTable_Object=MibTable
apRadioIfSSIDCfgTable=_ApRadioIfSSIDCfgTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,4,2))
if mibBuilder.loadTexts:apRadioIfSSIDCfgTable.setStatus(_A)
_ApRadioIfSSIDCfgEntry_Object=MibTableRow
apRadioIfSSIDCfgEntry=_ApRadioIfSSIDCfgEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,4,2,1))
apRadioIfSSIDCfgEntry.setIndexNames((0,_G,_H),(0,_D,_I))
if mibBuilder.loadTexts:apRadioIfSSIDCfgEntry.setStatus(_A)
_ApBSSID_Type=MacAddress
_ApBSSID_Object=MibTableColumn
apBSSID=_ApBSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,4,2,1,1),_ApBSSID_Type())
apBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:apBSSID.setStatus(_A)
_ApSSIDCfgTable_Object=MibTable
apSSIDCfgTable=_ApSSIDCfgTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,4,3))
if mibBuilder.loadTexts:apSSIDCfgTable.setStatus(_A)
_ApSSIDCfgEntry_Object=MibTableRow
apSSIDCfgEntry=_ApSSIDCfgEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,4,3,1))
apSSIDCfgEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:apSSIDCfgEntry.setStatus(_A)
_ApWlanId_Type=Integer32
_ApWlanId_Object=MibTableColumn
apWlanId=_ApWlanId_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,4,3,1,1),_ApWlanId_Type())
apWlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:apWlanId.setStatus(_A)
_ApSSIDName_Type=DisplayString
_ApSSIDName_Object=MibTableColumn
apSSIDName=_ApSSIDName_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,4,3,1,2),_ApSSIDName_Type())
apSSIDName.setMaxAccess(_E)
if mibBuilder.loadTexts:apSSIDName.setStatus(_A)
_ApSSIDEnabled_Type=TruthValue
_ApSSIDEnabled_Object=MibTableColumn
apSSIDEnabled=_ApSSIDEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,4,3,1,3),_ApSSIDEnabled_Type())
apSSIDEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:apSSIDEnabled.setStatus(_A)
_ApSSIDHidden_Type=TruthValue
_ApSSIDHidden_Object=MibTableColumn
apSSIDHidden=_ApSSIDHidden_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,4,3,1,4),_ApSSIDHidden_Type())
apSSIDHidden.setMaxAccess(_E)
if mibBuilder.loadTexts:apSSIDHidden.setStatus(_A)
_ApStaIsolate_Type=TruthValue
_ApStaIsolate_Object=MibTableColumn
apStaIsolate=_ApStaIsolate_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,4,3,1,5),_ApStaIsolate_Type())
apStaIsolate.setMaxAccess(_E)
if mibBuilder.loadTexts:apStaIsolate.setStatus(_A)
_ApDot11Auth_Type=Integer32
_ApDot11Auth_Object=MibTableColumn
apDot11Auth=_ApDot11Auth_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,4,3,1,6),_ApDot11Auth_Type())
apDot11Auth.setMaxAccess(_E)
if mibBuilder.loadTexts:apDot11Auth.setStatus(_A)
_ApSecurity_Type=Integer32
_ApSecurity_Object=MibTableColumn
apSecurity=_ApSecurity_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,4,3,1,7),_ApSecurity_Type())
apSecurity.setMaxAccess(_E)
if mibBuilder.loadTexts:apSecurity.setStatus(_A)
_ApAuthenMode_Type=Integer32
_ApAuthenMode_Object=MibTableColumn
apAuthenMode=_ApAuthenMode_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,4,3,1,8),_ApAuthenMode_Type())
apAuthenMode.setMaxAccess(_E)
if mibBuilder.loadTexts:apAuthenMode.setStatus(_A)
class _ApSecurityCiphers_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('none',0),('wep40',1),('wep104',2),('tkip',3),('aesccmp',4),('wapisms4',5)))
_ApSecurityCiphers_Type.__name__=_N
_ApSecurityCiphers_Object=MibTableColumn
apSecurityCiphers=_ApSecurityCiphers_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,4,3,1,9),_ApSecurityCiphers_Type())
apSecurityCiphers.setMaxAccess(_E)
if mibBuilder.loadTexts:apSecurityCiphers.setStatus(_A)
_ApVlanId_Type=Integer32
_ApVlanId_Object=MibTableColumn
apVlanId=_ApVlanId_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,4,3,1,10),_ApVlanId_Type())
apVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:apVlanId.setStatus(_A)
_ApMaxSimultUsers_Type=Integer32
_ApMaxSimultUsers_Object=MibTableColumn
apMaxSimultUsers=_ApMaxSimultUsers_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,4,3,1,11),_ApMaxSimultUsers_Type())
apMaxSimultUsers.setMaxAccess(_E)
if mibBuilder.loadTexts:apMaxSimultUsers.setStatus(_A)
_ApStaUplinkMaxRate_Type=Integer32
_ApStaUplinkMaxRate_Object=MibTableColumn
apStaUplinkMaxRate=_ApStaUplinkMaxRate_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,4,3,1,12),_ApStaUplinkMaxRate_Type())
apStaUplinkMaxRate.setMaxAccess(_E)
if mibBuilder.loadTexts:apStaUplinkMaxRate.setStatus(_A)
_ApStaDwlinkMaxRate_Type=Integer32
_ApStaDwlinkMaxRate_Object=MibTableColumn
apStaDwlinkMaxRate=_ApStaDwlinkMaxRate_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,4,3,1,13),_ApStaDwlinkMaxRate_Type())
apStaDwlinkMaxRate.setMaxAccess(_E)
if mibBuilder.loadTexts:apStaDwlinkMaxRate.setStatus(_A)
_ApSSIDCfgStatus_Type=RowStatus
_ApSSIDCfgStatus_Object=MibTableColumn
apSSIDCfgStatus=_ApSSIDCfgStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,4,3,1,14),_ApSSIDCfgStatus_Type())
apSSIDCfgStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:apSSIDCfgStatus.setStatus(_A)
_ApSecurityCfg_ObjectIdentity=ObjectIdentity
apSecurityCfg=_ApSecurityCfg_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,8,5))
_ApSecurityCfgTable_Object=MibTable
apSecurityCfgTable=_ApSecurityCfgTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,5,1))
if mibBuilder.loadTexts:apSecurityCfgTable.setStatus(_A)
_ApSecurityCfgEntry_Object=MibTableRow
apSecurityCfgEntry=_ApSecurityCfgEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,5,1,1))
apSecurityCfgEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:apSecurityCfgEntry.setStatus(_A)
_ApWEPCipherKeyIndex_Type=Integer32
_ApWEPCipherKeyIndex_Object=MibTableColumn
apWEPCipherKeyIndex=_ApWEPCipherKeyIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,5,1,1,1),_ApWEPCipherKeyIndex_Type())
apWEPCipherKeyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:apWEPCipherKeyIndex.setStatus(_A)
_ApWEPCipherKeyValue_Type=DisplayString
_ApWEPCipherKeyValue_Object=MibTableColumn
apWEPCipherKeyValue=_ApWEPCipherKeyValue_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,5,1,1,2),_ApWEPCipherKeyValue_Type())
apWEPCipherKeyValue.setMaxAccess(_C)
if mibBuilder.loadTexts:apWEPCipherKeyValue.setStatus(_A)
_ApWEPCipherKeyCharType_Type=Integer32
_ApWEPCipherKeyCharType_Object=MibTableColumn
apWEPCipherKeyCharType=_ApWEPCipherKeyCharType_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,5,1,1,3),_ApWEPCipherKeyCharType_Type())
apWEPCipherKeyCharType.setMaxAccess(_C)
if mibBuilder.loadTexts:apWEPCipherKeyCharType.setStatus(_A)
_ApPSKCipherKeyValue_Type=DisplayString
_ApPSKCipherKeyValue_Object=MibTableColumn
apPSKCipherKeyValue=_ApPSKCipherKeyValue_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,5,1,1,4),_ApPSKCipherKeyValue_Type())
apPSKCipherKeyValue.setMaxAccess(_C)
if mibBuilder.loadTexts:apPSKCipherKeyValue.setStatus(_A)
_ApPSKCipherKeyCharType_Type=Integer32
_ApPSKCipherKeyCharType_Object=MibTableColumn
apPSKCipherKeyCharType=_ApPSKCipherKeyCharType_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,5,1,1,5),_ApPSKCipherKeyCharType_Type())
apPSKCipherKeyCharType.setMaxAccess(_C)
if mibBuilder.loadTexts:apPSKCipherKeyCharType.setStatus(_A)
_ApWAPIASIPAddress_Type=IpAddress
_ApWAPIASIPAddress_Object=MibTableColumn
apWAPIASIPAddress=_ApWAPIASIPAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,5,1,1,6),_ApWAPIASIPAddress_Type())
apWAPIASIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:apWAPIASIPAddress.setStatus(_A)
_ApWAPIIsInstalledCer_Type=TruthValue
_ApWAPIIsInstalledCer_Object=MibTableColumn
apWAPIIsInstalledCer=_ApWAPIIsInstalledCer_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,5,1,1,7),_ApWAPIIsInstalledCer_Type())
apWAPIIsInstalledCer.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAPIIsInstalledCer.setStatus(_A)
_ApTerminalCfg_ObjectIdentity=ObjectIdentity
apTerminalCfg=_ApTerminalCfg_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,8,6))
_ApTerminalInfoTable_Object=MibTable
apTerminalInfoTable=_ApTerminalInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,6,1))
if mibBuilder.loadTexts:apTerminalInfoTable.setStatus(_A)
_ApTerminalInfoEntry_Object=MibTableRow
apTerminalInfoEntry=_ApTerminalInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,6,1,1))
apTerminalInfoEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:apTerminalInfoEntry.setStatus(_A)
_ApStaMAC_Type=MacAddress
_ApStaMAC_Object=MibTableColumn
apStaMAC=_ApStaMAC_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,6,1,1,1),_ApStaMAC_Type())
apStaMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaMAC.setStatus(_A)
_ApStaWMMAttr_Type=Integer32
_ApStaWMMAttr_Object=MibTableColumn
apStaWMMAttr=_ApStaWMMAttr_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,6,1,1,2),_ApStaWMMAttr_Type())
apStaWMMAttr.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaWMMAttr.setStatus(_A)
_ApStaIPAddress_Type=IpAddress
_ApStaIPAddress_Object=MibTableColumn
apStaIPAddress=_ApStaIPAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,6,1,1,3),_ApStaIPAddress_Type())
apStaIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaIPAddress.setStatus(_A)
_ApStaRadioMode_Type=Integer32
_ApStaRadioMode_Object=MibTableColumn
apStaRadioMode=_ApStaRadioMode_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,6,1,1,4),_ApStaRadioMode_Type())
apStaRadioMode.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaRadioMode.setStatus(_A)
_ApStaRadioChannel_Type=Integer32
_ApStaRadioChannel_Object=MibTableColumn
apStaRadioChannel=_ApStaRadioChannel_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,6,1,1,5),_ApStaRadioChannel_Type())
apStaRadioChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaRadioChannel.setStatus(_A)
_ApStaTxRates_Type=Integer32
_ApStaTxRates_Object=MibTableColumn
apStaTxRates=_ApStaTxRates_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,6,1,1,6),_ApStaTxRates_Type())
apStaTxRates.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaTxRates.setStatus(_A)
_ApStaPowerSaveMode_Type=Integer32
_ApStaPowerSaveMode_Object=MibTableColumn
apStaPowerSaveMode=_ApStaPowerSaveMode_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,6,1,1,7),_ApStaPowerSaveMode_Type())
apStaPowerSaveMode.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaPowerSaveMode.setStatus(_A)
_ApStaVlanId_Type=Integer32
_ApStaVlanId_Object=MibTableColumn
apStaVlanId=_ApStaVlanId_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,6,1,1,8),_ApStaVlanId_Type())
apStaVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaVlanId.setStatus(_A)
_ApStaSSIDName_Type=DisplayString
_ApStaSSIDName_Object=MibTableColumn
apStaSSIDName=_ApStaSSIDName_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,6,1,1,9),_ApStaSSIDName_Type())
apStaSSIDName.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaSSIDName.setStatus(_A)
_ApStaDot11Auth_Type=Integer32
_ApStaDot11Auth_Object=MibTableColumn
apStaDot11Auth=_ApStaDot11Auth_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,6,1,1,10),_ApStaDot11Auth_Type())
apStaDot11Auth.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaDot11Auth.setStatus(_A)
_ApStaSecurity_Type=Integer32
_ApStaSecurity_Object=MibTableColumn
apStaSecurity=_ApStaSecurity_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,6,1,1,11),_ApStaSecurity_Type())
apStaSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaSecurity.setStatus(_A)
_ApStaAuthenMode_Type=Integer32
_ApStaAuthenMode_Object=MibTableColumn
apStaAuthenMode=_ApStaAuthenMode_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,6,1,1,12),_ApStaAuthenMode_Type())
apStaAuthenMode.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaAuthenMode.setStatus(_A)
_ApStaSecurityCiphers_Type=Integer32
_ApStaSecurityCiphers_Object=MibTableColumn
apStaSecurityCiphers=_ApStaSecurityCiphers_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,6,1,1,13),_ApStaSecurityCiphers_Type())
apStaSecurityCiphers.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaSecurityCiphers.setStatus(_A)
_ApQosCfg_ObjectIdentity=ObjectIdentity
apQosCfg=_ApQosCfg_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,8,7))
_ApQosRadioIfCfgTable_Object=MibTable
apQosRadioIfCfgTable=_ApQosRadioIfCfgTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,1))
if mibBuilder.loadTexts:apQosRadioIfCfgTable.setStatus(_A)
_ApQosRadioIfCfgEntry_Object=MibTableRow
apQosRadioIfCfgEntry=_ApQosRadioIfCfgEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,1,1))
apQosRadioIfCfgEntry.setIndexNames((0,_G,_H),(0,_D,_X))
if mibBuilder.loadTexts:apQosRadioIfCfgEntry.setStatus(_A)
class _ApQoSTrafficClassIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('bestEffort',0),('background',1),('video',2),('voice',3)))
_ApQoSTrafficClassIndex_Type.__name__=_N
_ApQoSTrafficClassIndex_Object=MibTableColumn
apQoSTrafficClassIndex=_ApQoSTrafficClassIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,1,1,1),_ApQoSTrafficClassIndex_Type())
apQoSTrafficClassIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:apQoSTrafficClassIndex.setStatus(_A)
_ApQosAIFS_Type=Integer32
_ApQosAIFS_Object=MibTableColumn
apQosAIFS=_ApQosAIFS_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,1,1,2),_ApQosAIFS_Type())
apQosAIFS.setMaxAccess(_C)
if mibBuilder.loadTexts:apQosAIFS.setStatus(_A)
_ApQoSCWmin_Type=Integer32
_ApQoSCWmin_Object=MibTableColumn
apQoSCWmin=_ApQoSCWmin_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,1,1,3),_ApQoSCWmin_Type())
apQoSCWmin.setMaxAccess(_C)
if mibBuilder.loadTexts:apQoSCWmin.setStatus(_A)
_ApQoSCWmax_Type=Integer32
_ApQoSCWmax_Object=MibTableColumn
apQoSCWmax=_ApQoSCWmax_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,1,1,4),_ApQoSCWmax_Type())
apQoSCWmax.setMaxAccess(_C)
if mibBuilder.loadTexts:apQoSCWmax.setStatus(_A)
_ApQoSTXOPLim_Type=Integer32
_ApQoSTXOPLim_Object=MibTableColumn
apQoSTXOPLim=_ApQoSTXOPLim_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,1,1,5),_ApQoSTXOPLim_Type())
apQoSTXOPLim.setMaxAccess(_C)
if mibBuilder.loadTexts:apQoSTXOPLim.setStatus(_A)
_ApQosBaseCfgTable_Object=MibTable
apQosBaseCfgTable=_ApQosBaseCfgTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2))
if mibBuilder.loadTexts:apQosBaseCfgTable.setStatus(_A)
_ApQosBaseCfgEntry_Object=MibTableRow
apQosBaseCfgEntry=_ApQosBaseCfgEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1))
apQosBaseCfgEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:apQosBaseCfgEntry.setStatus(_A)
_ApQoSBaseTrafficClass_Type=Integer32
_ApQoSBaseTrafficClass_Object=MibTableColumn
apQoSBaseTrafficClass=_ApQoSBaseTrafficClass_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,1),_ApQoSBaseTrafficClass_Type())
apQoSBaseTrafficClass.setMaxAccess(_C)
if mibBuilder.loadTexts:apQoSBaseTrafficClass.setStatus(_A)
_ApQoSEnabled_Type=TruthValue
_ApQoSEnabled_Object=MibTableColumn
apQoSEnabled=_ApQoSEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,2),_ApQoSEnabled_Type())
apQoSEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:apQoSEnabled.setStatus(_A)
_ApQoSBW_Type=Integer32
_ApQoSBW_Object=MibTableColumn
apQoSBW=_ApQoSBW_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,3),_ApQoSBW_Type())
apQoSBW.setMaxAccess(_C)
if mibBuilder.loadTexts:apQoSBW.setStatus(_A)
_ApQoSResPercent_Type=Integer32
_ApQoSResPercent_Object=MibTableColumn
apQoSResPercent=_ApQoSResPercent_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,4),_ApQoSResPercent_Type())
apQoSResPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:apQoSResPercent.setStatus(_A)
_ApQoSsharedBW_Type=Integer32
_ApQoSsharedBW_Object=MibTableColumn
apQoSsharedBW=_ApQoSsharedBW_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,5),_ApQoSsharedBW_Type())
apQoSsharedBW.setMaxAccess(_C)
if mibBuilder.loadTexts:apQoSsharedBW.setStatus(_A)
_ApQoSsharedBWPercent_Type=Integer32
_ApQoSsharedBWPercent_Object=MibTableColumn
apQoSsharedBWPercent=_ApQoSsharedBWPercent_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,6),_ApQoSsharedBWPercent_Type())
apQoSsharedBWPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:apQoSsharedBWPercent.setStatus(_A)
_ApSchedAlgName_Type=DisplayString
_ApSchedAlgName_Object=MibTableColumn
apSchedAlgName=_ApSchedAlgName_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,7),_ApSchedAlgName_Type())
apSchedAlgName.setMaxAccess(_C)
if mibBuilder.loadTexts:apSchedAlgName.setStatus(_A)
_ApResPolicyEnabled_Type=TruthValue
_ApResPolicyEnabled_Object=MibTableColumn
apResPolicyEnabled=_ApResPolicyEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,8),_ApResPolicyEnabled_Type())
apResPolicyEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:apResPolicyEnabled.setStatus(_A)
_ApResPolicyName_Type=DisplayString
_ApResPolicyName_Object=MibTableColumn
apResPolicyName=_ApResPolicyName_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,9),_ApResPolicyName_Type())
apResPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:apResPolicyName.setStatus(_A)
_ApBackgroundSvcAvgSpeed_Type=Integer32
_ApBackgroundSvcAvgSpeed_Object=MibTableColumn
apBackgroundSvcAvgSpeed=_ApBackgroundSvcAvgSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,10),_ApBackgroundSvcAvgSpeed_Type())
apBackgroundSvcAvgSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:apBackgroundSvcAvgSpeed.setStatus(_A)
_ApBackgroundSvcMaxBurst_Type=Integer32
_ApBackgroundSvcMaxBurst_Object=MibTableColumn
apBackgroundSvcMaxBurst=_ApBackgroundSvcMaxBurst_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,11),_ApBackgroundSvcMaxBurst_Type())
apBackgroundSvcMaxBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:apBackgroundSvcMaxBurst.setStatus(_A)
_ApBackgroundSvcPriority_Type=Integer32
_ApBackgroundSvcPriority_Object=MibTableColumn
apBackgroundSvcPriority=_ApBackgroundSvcPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,12),_ApBackgroundSvcPriority_Type())
apBackgroundSvcPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:apBackgroundSvcPriority.setStatus(_A)
_ApBackgroundSvcResPriority_Type=Integer32
_ApBackgroundSvcResPriority_Object=MibTableColumn
apBackgroundSvcResPriority=_ApBackgroundSvcResPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,13),_ApBackgroundSvcResPriority_Type())
apBackgroundSvcResPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:apBackgroundSvcResPriority.setStatus(_A)
_ApBestEffortSvcAvgSpeed_Type=Integer32
_ApBestEffortSvcAvgSpeed_Object=MibTableColumn
apBestEffortSvcAvgSpeed=_ApBestEffortSvcAvgSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,14),_ApBestEffortSvcAvgSpeed_Type())
apBestEffortSvcAvgSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:apBestEffortSvcAvgSpeed.setStatus(_A)
_ApBestEffortSvcMaxBurst_Type=Integer32
_ApBestEffortSvcMaxBurst_Object=MibTableColumn
apBestEffortSvcMaxBurst=_ApBestEffortSvcMaxBurst_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,15),_ApBestEffortSvcMaxBurst_Type())
apBestEffortSvcMaxBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:apBestEffortSvcMaxBurst.setStatus(_A)
_ApBestEffortSvcPriority_Type=Integer32
_ApBestEffortSvcPriority_Object=MibTableColumn
apBestEffortSvcPriority=_ApBestEffortSvcPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,16),_ApBestEffortSvcPriority_Type())
apBestEffortSvcPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:apBestEffortSvcPriority.setStatus(_A)
_ApBestEffortSvcResPriority_Type=Integer32
_ApBestEffortSvcResPriority_Object=MibTableColumn
apBestEffortSvcResPriority=_ApBestEffortSvcResPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,17),_ApBestEffortSvcResPriority_Type())
apBestEffortSvcResPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:apBestEffortSvcResPriority.setStatus(_A)
_ApVoiceSvcAvgSpeed_Type=Integer32
_ApVoiceSvcAvgSpeed_Object=MibTableColumn
apVoiceSvcAvgSpeed=_ApVoiceSvcAvgSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,18),_ApVoiceSvcAvgSpeed_Type())
apVoiceSvcAvgSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:apVoiceSvcAvgSpeed.setStatus(_A)
_ApVoiceSvcMaxBurst_Type=Integer32
_ApVoiceSvcMaxBurst_Object=MibTableColumn
apVoiceSvcMaxBurst=_ApVoiceSvcMaxBurst_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,19),_ApVoiceSvcMaxBurst_Type())
apVoiceSvcMaxBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:apVoiceSvcMaxBurst.setStatus(_A)
_ApVoiceSvcPriority_Type=Integer32
_ApVoiceSvcPriority_Object=MibTableColumn
apVoiceSvcPriority=_ApVoiceSvcPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,20),_ApVoiceSvcPriority_Type())
apVoiceSvcPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:apVoiceSvcPriority.setStatus(_A)
_ApVoiceSvcResPriority_Type=Integer32
_ApVoiceSvcResPriority_Object=MibTableColumn
apVoiceSvcResPriority=_ApVoiceSvcResPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,21),_ApVoiceSvcResPriority_Type())
apVoiceSvcResPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:apVoiceSvcResPriority.setStatus(_A)
_ApVideoSvcAvgSpeed_Type=Integer32
_ApVideoSvcAvgSpeed_Object=MibTableColumn
apVideoSvcAvgSpeed=_ApVideoSvcAvgSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,22),_ApVideoSvcAvgSpeed_Type())
apVideoSvcAvgSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:apVideoSvcAvgSpeed.setStatus(_A)
_ApVideoSvcMaxBurst_Type=Integer32
_ApVideoSvcMaxBurst_Object=MibTableColumn
apVideoSvcMaxBurst=_ApVideoSvcMaxBurst_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,23),_ApVideoSvcMaxBurst_Type())
apVideoSvcMaxBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:apVideoSvcMaxBurst.setStatus(_A)
_ApVideoSvcPriority_Type=Integer32
_ApVideoSvcPriority_Object=MibTableColumn
apVideoSvcPriority=_ApVideoSvcPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,24),_ApVideoSvcPriority_Type())
apVideoSvcPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:apVideoSvcPriority.setStatus(_A)
_ApVideoSvcResPriority_Type=Integer32
_ApVideoSvcResPriority_Object=MibTableColumn
apVideoSvcResPriority=_ApVideoSvcResPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,2,1,25),_ApVideoSvcResPriority_Type())
apVideoSvcResPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:apVideoSvcResPriority.setStatus(_A)
_ApQosBackgroundCfgTable_Object=MibTable
apQosBackgroundCfgTable=_ApQosBackgroundCfgTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,3))
if mibBuilder.loadTexts:apQosBackgroundCfgTable.setStatus(_A)
_ApQosBackgroundCfgEntry_Object=MibTableRow
apQosBackgroundCfgEntry=_ApQosBackgroundCfgEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,3,1))
apQosBackgroundCfgEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:apQosBackgroundCfgEntry.setStatus(_A)
_ApBgMaxSvcCnt_Type=Integer32
_ApBgMaxSvcCnt_Object=MibTableColumn
apBgMaxSvcCnt=_ApBgMaxSvcCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,3,1,1),_ApBgMaxSvcCnt_Type())
apBgMaxSvcCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:apBgMaxSvcCnt.setStatus(_A)
_ApBgSvcBW_Type=Integer32
_ApBgSvcBW_Object=MibTableColumn
apBgSvcBW=_ApBgSvcBW_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,3,1,2),_ApBgSvcBW_Type())
apBgSvcBW.setMaxAccess(_C)
if mibBuilder.loadTexts:apBgSvcBW.setStatus(_A)
_ApBgSvcBWPercent_Type=Integer32
_ApBgSvcBWPercent_Object=MibTableColumn
apBgSvcBWPercent=_ApBgSvcBWPercent_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,3,1,3),_ApBgSvcBWPercent_Type())
apBgSvcBWPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:apBgSvcBWPercent.setStatus(_A)
_ApBgIsUseWREDAlg_Type=TruthValue
_ApBgIsUseWREDAlg_Object=MibTableColumn
apBgIsUseWREDAlg=_ApBgIsUseWREDAlg_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,3,1,4),_ApBgIsUseWREDAlg_Type())
apBgIsUseWREDAlg.setMaxAccess(_C)
if mibBuilder.loadTexts:apBgIsUseWREDAlg.setStatus(_A)
_ApBgIsUseTrafficShaping_Type=TruthValue
_ApBgIsUseTrafficShaping_Object=MibTableColumn
apBgIsUseTrafficShaping=_ApBgIsUseTrafficShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,3,1,5),_ApBgIsUseTrafficShaping_Type())
apBgIsUseTrafficShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:apBgIsUseTrafficShaping.setStatus(_A)
_ApQosBestEffortCfgTable_Object=MibTable
apQosBestEffortCfgTable=_ApQosBestEffortCfgTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,4))
if mibBuilder.loadTexts:apQosBestEffortCfgTable.setStatus(_A)
_ApQosBestEffortCfgEntry_Object=MibTableRow
apQosBestEffortCfgEntry=_ApQosBestEffortCfgEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,4,1))
apQosBestEffortCfgEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:apQosBestEffortCfgEntry.setStatus(_A)
_ApBeMaxSvcCnt_Type=Integer32
_ApBeMaxSvcCnt_Object=MibTableColumn
apBeMaxSvcCnt=_ApBeMaxSvcCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,4,1,1),_ApBeMaxSvcCnt_Type())
apBeMaxSvcCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:apBeMaxSvcCnt.setStatus(_A)
_ApBeSvcBW_Type=Integer32
_ApBeSvcBW_Object=MibTableColumn
apBeSvcBW=_ApBeSvcBW_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,4,1,2),_ApBeSvcBW_Type())
apBeSvcBW.setMaxAccess(_C)
if mibBuilder.loadTexts:apBeSvcBW.setStatus(_A)
_ApBeSvcBWPercent_Type=Integer32
_ApBeSvcBWPercent_Object=MibTableColumn
apBeSvcBWPercent=_ApBeSvcBWPercent_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,4,1,3),_ApBeSvcBWPercent_Type())
apBeSvcBWPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:apBeSvcBWPercent.setStatus(_A)
_ApBeIsUseWREDAlg_Type=TruthValue
_ApBeIsUseWREDAlg_Object=MibTableColumn
apBeIsUseWREDAlg=_ApBeIsUseWREDAlg_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,4,1,4),_ApBeIsUseWREDAlg_Type())
apBeIsUseWREDAlg.setMaxAccess(_C)
if mibBuilder.loadTexts:apBeIsUseWREDAlg.setStatus(_A)
_ApBeIsUseTrafficShaping_Type=TruthValue
_ApBeIsUseTrafficShaping_Object=MibTableColumn
apBeIsUseTrafficShaping=_ApBeIsUseTrafficShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,4,1,5),_ApBeIsUseTrafficShaping_Type())
apBeIsUseTrafficShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:apBeIsUseTrafficShaping.setStatus(_A)
_ApQosVoiceCfgTable_Object=MibTable
apQosVoiceCfgTable=_ApQosVoiceCfgTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,5))
if mibBuilder.loadTexts:apQosVoiceCfgTable.setStatus(_A)
_ApQosVoiceCfgEntry_Object=MibTableRow
apQosVoiceCfgEntry=_ApQosVoiceCfgEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,5,1))
apQosVoiceCfgEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:apQosVoiceCfgEntry.setStatus(_A)
_ApVoiceMaxSvcCnt_Type=Integer32
_ApVoiceMaxSvcCnt_Object=MibTableColumn
apVoiceMaxSvcCnt=_ApVoiceMaxSvcCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,5,1,1),_ApVoiceMaxSvcCnt_Type())
apVoiceMaxSvcCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:apVoiceMaxSvcCnt.setStatus(_A)
_ApVoiceSvcBW_Type=Integer32
_ApVoiceSvcBW_Object=MibTableColumn
apVoiceSvcBW=_ApVoiceSvcBW_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,5,1,2),_ApVoiceSvcBW_Type())
apVoiceSvcBW.setMaxAccess(_C)
if mibBuilder.loadTexts:apVoiceSvcBW.setStatus(_A)
_ApVoiceSvcBWPercent_Type=Integer32
_ApVoiceSvcBWPercent_Object=MibTableColumn
apVoiceSvcBWPercent=_ApVoiceSvcBWPercent_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,5,1,3),_ApVoiceSvcBWPercent_Type())
apVoiceSvcBWPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:apVoiceSvcBWPercent.setStatus(_A)
_ApVoiceIsUseStreamBasedQueue_Type=TruthValue
_ApVoiceIsUseStreamBasedQueue_Object=MibTableColumn
apVoiceIsUseStreamBasedQueue=_ApVoiceIsUseStreamBasedQueue_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,5,1,4),_ApVoiceIsUseStreamBasedQueue_Type())
apVoiceIsUseStreamBasedQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:apVoiceIsUseStreamBasedQueue.setStatus(_A)
_ApVoiceStreamMaxQueueLen_Type=Integer32
_ApVoiceStreamMaxQueueLen_Object=MibTableColumn
apVoiceStreamMaxQueueLen=_ApVoiceStreamMaxQueueLen_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,5,1,5),_ApVoiceStreamMaxQueueLen_Type())
apVoiceStreamMaxQueueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:apVoiceStreamMaxQueueLen.setStatus(_A)
_ApVoiceStreamAvgSpeed_Type=Integer32
_ApVoiceStreamAvgSpeed_Object=MibTableColumn
apVoiceStreamAvgSpeed=_ApVoiceStreamAvgSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,5,1,6),_ApVoiceStreamAvgSpeed_Type())
apVoiceStreamAvgSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:apVoiceStreamAvgSpeed.setStatus(_A)
_ApVoiceStreamMaxBurst_Type=Integer32
_ApVoiceStreamMaxBurst_Object=MibTableColumn
apVoiceStreamMaxBurst=_ApVoiceStreamMaxBurst_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,5,1,7),_ApVoiceStreamMaxBurst_Type())
apVoiceStreamMaxBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:apVoiceStreamMaxBurst.setStatus(_A)
_ApVoiceIsUseWREDAlg_Type=TruthValue
_ApVoiceIsUseWREDAlg_Object=MibTableColumn
apVoiceIsUseWREDAlg=_ApVoiceIsUseWREDAlg_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,5,1,8),_ApVoiceIsUseWREDAlg_Type())
apVoiceIsUseWREDAlg.setMaxAccess(_C)
if mibBuilder.loadTexts:apVoiceIsUseWREDAlg.setStatus(_A)
_ApVoiceIsUseTrafficShaping_Type=TruthValue
_ApVoiceIsUseTrafficShaping_Object=MibTableColumn
apVoiceIsUseTrafficShaping=_ApVoiceIsUseTrafficShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,5,1,9),_ApVoiceIsUseTrafficShaping_Type())
apVoiceIsUseTrafficShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:apVoiceIsUseTrafficShaping.setStatus(_A)
_ApQosVedioCfgTable_Object=MibTable
apQosVedioCfgTable=_ApQosVedioCfgTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,6))
if mibBuilder.loadTexts:apQosVedioCfgTable.setStatus(_A)
_ApQosVedioCfgEntry_Object=MibTableRow
apQosVedioCfgEntry=_ApQosVedioCfgEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,6,1))
apQosVedioCfgEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:apQosVedioCfgEntry.setStatus(_A)
_ApVedioMaxSvcCnt_Type=Integer32
_ApVedioMaxSvcCnt_Object=MibTableColumn
apVedioMaxSvcCnt=_ApVedioMaxSvcCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,6,1,1),_ApVedioMaxSvcCnt_Type())
apVedioMaxSvcCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:apVedioMaxSvcCnt.setStatus(_A)
_ApVedioSvcBW_Type=Integer32
_ApVedioSvcBW_Object=MibTableColumn
apVedioSvcBW=_ApVedioSvcBW_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,6,1,2),_ApVedioSvcBW_Type())
apVedioSvcBW.setMaxAccess(_C)
if mibBuilder.loadTexts:apVedioSvcBW.setStatus(_A)
_ApVedioSvcBWPercent_Type=Integer32
_ApVedioSvcBWPercent_Object=MibTableColumn
apVedioSvcBWPercent=_ApVedioSvcBWPercent_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,6,1,3),_ApVedioSvcBWPercent_Type())
apVedioSvcBWPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:apVedioSvcBWPercent.setStatus(_A)
_ApVedioIsUseStreamBasedQueue_Type=TruthValue
_ApVedioIsUseStreamBasedQueue_Object=MibTableColumn
apVedioIsUseStreamBasedQueue=_ApVedioIsUseStreamBasedQueue_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,6,1,4),_ApVedioIsUseStreamBasedQueue_Type())
apVedioIsUseStreamBasedQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:apVedioIsUseStreamBasedQueue.setStatus(_A)
_ApVedioStreamMaxQueueLen_Type=Integer32
_ApVedioStreamMaxQueueLen_Object=MibTableColumn
apVedioStreamMaxQueueLen=_ApVedioStreamMaxQueueLen_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,6,1,5),_ApVedioStreamMaxQueueLen_Type())
apVedioStreamMaxQueueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:apVedioStreamMaxQueueLen.setStatus(_A)
_ApVedioStreamAvgSpeed_Type=Integer32
_ApVedioStreamAvgSpeed_Object=MibTableColumn
apVedioStreamAvgSpeed=_ApVedioStreamAvgSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,6,1,6),_ApVedioStreamAvgSpeed_Type())
apVedioStreamAvgSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:apVedioStreamAvgSpeed.setStatus(_A)
_ApVedioStreamMaxBurst_Type=Integer32
_ApVedioStreamMaxBurst_Object=MibTableColumn
apVedioStreamMaxBurst=_ApVedioStreamMaxBurst_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,6,1,7),_ApVedioStreamMaxBurst_Type())
apVedioStreamMaxBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:apVedioStreamMaxBurst.setStatus(_A)
_ApVedioIsUseWREDAlg_Type=TruthValue
_ApVedioIsUseWREDAlg_Object=MibTableColumn
apVedioIsUseWREDAlg=_ApVedioIsUseWREDAlg_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,6,1,8),_ApVedioIsUseWREDAlg_Type())
apVedioIsUseWREDAlg.setMaxAccess(_C)
if mibBuilder.loadTexts:apVedioIsUseWREDAlg.setStatus(_A)
_ApVedioIsUseTrafficShaping_Type=TruthValue
_ApVedioIsUseTrafficShaping_Object=MibTableColumn
apVedioIsUseTrafficShaping=_ApVedioIsUseTrafficShaping_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,7,6,1,9),_ApVedioIsUseTrafficShaping_Type())
apVedioIsUseTrafficShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:apVedioIsUseTrafficShaping.setStatus(_A)
_ApWapiCfg_ObjectIdentity=ObjectIdentity
apWapiCfg=_ApWapiCfg_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,8,8))
_ApWapiProtocolCfgTable_Object=MibTable
apWapiProtocolCfgTable=_ApWapiProtocolCfgTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1))
if mibBuilder.loadTexts:apWapiProtocolCfgTable.setStatus(_A)
_ApWapiProtocolCfgEntry_Object=MibTableRow
apWapiProtocolCfgEntry=_ApWapiProtocolCfgEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1))
apWapiProtocolCfgEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:apWapiProtocolCfgEntry.setStatus(_A)
_ApConfigVersion_Type=Integer32
_ApConfigVersion_Object=MibTableColumn
apConfigVersion=_ApConfigVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,1),_ApConfigVersion_Type())
apConfigVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:apConfigVersion.setStatus(_A)
_ApControlledAuthControl_Type=TruthValue
_ApControlledAuthControl_Object=MibTableColumn
apControlledAuthControl=_ApControlledAuthControl_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,2),_ApControlledAuthControl_Type())
apControlledAuthControl.setMaxAccess(_B)
if mibBuilder.loadTexts:apControlledAuthControl.setStatus(_A)
_ApControlledPortControl_Type=Integer32
_ApControlledPortControl_Object=MibTableColumn
apControlledPortControl=_ApControlledPortControl_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,3),_ApControlledPortControl_Type())
apControlledPortControl.setMaxAccess(_B)
if mibBuilder.loadTexts:apControlledPortControl.setStatus(_A)
_ApWapiOptionImplemented_Type=TruthValue
_ApWapiOptionImplemented_Object=MibTableColumn
apWapiOptionImplemented=_ApWapiOptionImplemented_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,4),_ApWapiOptionImplemented_Type())
apWapiOptionImplemented.setMaxAccess(_B)
if mibBuilder.loadTexts:apWapiOptionImplemented.setStatus(_A)
_ApWapiPreauthImplemented_Type=TruthValue
_ApWapiPreauthImplemented_Object=MibTableColumn
apWapiPreauthImplemented=_ApWapiPreauthImplemented_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,5),_ApWapiPreauthImplemented_Type())
apWapiPreauthImplemented.setMaxAccess(_B)
if mibBuilder.loadTexts:apWapiPreauthImplemented.setStatus(_A)
_ApWapiEnabled_Type=TruthValue
_ApWapiEnabled_Object=MibTableColumn
apWapiEnabled=_ApWapiEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,6),_ApWapiEnabled_Type())
apWapiEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:apWapiEnabled.setStatus(_A)
_ApWapiPreauthEnabled_Type=TruthValue
_ApWapiPreauthEnabled_Object=MibTableColumn
apWapiPreauthEnabled=_ApWapiPreauthEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,7),_ApWapiPreauthEnabled_Type())
apWapiPreauthEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:apWapiPreauthEnabled.setStatus(_A)
_ApUnicastKeysSupported_Type=Unsigned32
_ApUnicastKeysSupported_Object=MibTableColumn
apUnicastKeysSupported=_ApUnicastKeysSupported_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,8),_ApUnicastKeysSupported_Type())
apUnicastKeysSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:apUnicastKeysSupported.setStatus(_A)
_ApUnicastRekeyMethod_Type=Integer32
_ApUnicastRekeyMethod_Object=MibTableColumn
apUnicastRekeyMethod=_ApUnicastRekeyMethod_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,9),_ApUnicastRekeyMethod_Type())
apUnicastRekeyMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:apUnicastRekeyMethod.setStatus(_A)
_ApUnicastRekeyTime_Type=Unsigned32
_ApUnicastRekeyTime_Object=MibTableColumn
apUnicastRekeyTime=_ApUnicastRekeyTime_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,10),_ApUnicastRekeyTime_Type())
apUnicastRekeyTime.setMaxAccess(_C)
if mibBuilder.loadTexts:apUnicastRekeyTime.setStatus(_A)
_ApUnicastRekeyPackets_Type=Unsigned32
_ApUnicastRekeyPackets_Object=MibTableColumn
apUnicastRekeyPackets=_ApUnicastRekeyPackets_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,11),_ApUnicastRekeyPackets_Type())
apUnicastRekeyPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:apUnicastRekeyPackets.setStatus(_A)
_ApMulticastCipher_Type=OctetString
_ApMulticastCipher_Object=MibTableColumn
apMulticastCipher=_ApMulticastCipher_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,12),_ApMulticastCipher_Type())
apMulticastCipher.setMaxAccess(_C)
if mibBuilder.loadTexts:apMulticastCipher.setStatus(_A)
_ApMulticastRekeyMethod_Type=Integer32
_ApMulticastRekeyMethod_Object=MibTableColumn
apMulticastRekeyMethod=_ApMulticastRekeyMethod_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,13),_ApMulticastRekeyMethod_Type())
apMulticastRekeyMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:apMulticastRekeyMethod.setStatus(_A)
_ApMulticastRekeyTime_Type=Unsigned32
_ApMulticastRekeyTime_Object=MibTableColumn
apMulticastRekeyTime=_ApMulticastRekeyTime_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,14),_ApMulticastRekeyTime_Type())
apMulticastRekeyTime.setMaxAccess(_C)
if mibBuilder.loadTexts:apMulticastRekeyTime.setStatus(_A)
_ApMulticastRekeyPackets_Type=Unsigned32
_ApMulticastRekeyPackets_Object=MibTableColumn
apMulticastRekeyPackets=_ApMulticastRekeyPackets_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,15),_ApMulticastRekeyPackets_Type())
apMulticastRekeyPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:apMulticastRekeyPackets.setStatus(_A)
_ApMulticastRekeyStrict_Type=TruthValue
_ApMulticastRekeyStrict_Object=MibTableColumn
apMulticastRekeyStrict=_ApMulticastRekeyStrict_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,16),_ApMulticastRekeyStrict_Type())
apMulticastRekeyStrict.setMaxAccess(_C)
if mibBuilder.loadTexts:apMulticastRekeyStrict.setStatus(_A)
_ApPSKValue_Type=OctetString
_ApPSKValue_Object=MibTableColumn
apPSKValue=_ApPSKValue_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,17),_ApPSKValue_Type())
apPSKValue.setMaxAccess(_C)
if mibBuilder.loadTexts:apPSKValue.setStatus(_A)
_ApPSKPassPhrase_Type=DisplayString
_ApPSKPassPhrase_Object=MibTableColumn
apPSKPassPhrase=_ApPSKPassPhrase_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,18),_ApPSKPassPhrase_Type())
apPSKPassPhrase.setMaxAccess(_C)
if mibBuilder.loadTexts:apPSKPassPhrase.setStatus(_A)
_ApCertificateUpdateCount_Type=Unsigned32
_ApCertificateUpdateCount_Object=MibTableColumn
apCertificateUpdateCount=_ApCertificateUpdateCount_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,19),_ApCertificateUpdateCount_Type())
apCertificateUpdateCount.setMaxAccess(_C)
if mibBuilder.loadTexts:apCertificateUpdateCount.setStatus(_A)
_ApMulticastUpdateCount_Type=Unsigned32
_ApMulticastUpdateCount_Object=MibTableColumn
apMulticastUpdateCount=_ApMulticastUpdateCount_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,20),_ApMulticastUpdateCount_Type())
apMulticastUpdateCount.setMaxAccess(_C)
if mibBuilder.loadTexts:apMulticastUpdateCount.setStatus(_A)
_ApUnicastUpdateCount_Type=Unsigned32
_ApUnicastUpdateCount_Object=MibTableColumn
apUnicastUpdateCount=_ApUnicastUpdateCount_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,21),_ApUnicastUpdateCount_Type())
apUnicastUpdateCount.setMaxAccess(_C)
if mibBuilder.loadTexts:apUnicastUpdateCount.setStatus(_A)
_ApMulticastCipherSize_Type=Unsigned32
_ApMulticastCipherSize_Object=MibTableColumn
apMulticastCipherSize=_ApMulticastCipherSize_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,22),_ApMulticastCipherSize_Type())
apMulticastCipherSize.setMaxAccess(_B)
if mibBuilder.loadTexts:apMulticastCipherSize.setStatus(_A)
_ApBKLifetime_Type=Unsigned32
_ApBKLifetime_Object=MibTableColumn
apBKLifetime=_ApBKLifetime_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,23),_ApBKLifetime_Type())
apBKLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:apBKLifetime.setStatus(_A)
_ApBKReauthThreshold_Type=Unsigned32
_ApBKReauthThreshold_Object=MibTableColumn
apBKReauthThreshold=_ApBKReauthThreshold_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,24),_ApBKReauthThreshold_Type())
apBKReauthThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:apBKReauthThreshold.setStatus(_A)
_ApSATimeout_Type=Unsigned32
_ApSATimeout_Object=MibTableColumn
apSATimeout=_ApSATimeout_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,25),_ApSATimeout_Type())
apSATimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:apSATimeout.setStatus(_A)
_ApAuthSuiteSelected_Type=OctetString
_ApAuthSuiteSelected_Object=MibTableColumn
apAuthSuiteSelected=_ApAuthSuiteSelected_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,26),_ApAuthSuiteSelected_Type())
apAuthSuiteSelected.setMaxAccess(_B)
if mibBuilder.loadTexts:apAuthSuiteSelected.setStatus(_A)
_ApUnicastCipherSelected_Type=OctetString
_ApUnicastCipherSelected_Object=MibTableColumn
apUnicastCipherSelected=_ApUnicastCipherSelected_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,27),_ApUnicastCipherSelected_Type())
apUnicastCipherSelected.setMaxAccess(_B)
if mibBuilder.loadTexts:apUnicastCipherSelected.setStatus(_A)
_ApMulticastCipherSelected_Type=OctetString
_ApMulticastCipherSelected_Object=MibTableColumn
apMulticastCipherSelected=_ApMulticastCipherSelected_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,28),_ApMulticastCipherSelected_Type())
apMulticastCipherSelected.setMaxAccess(_B)
if mibBuilder.loadTexts:apMulticastCipherSelected.setStatus(_A)
_ApBKIDUsed_Type=OctetString
_ApBKIDUsed_Object=MibTableColumn
apBKIDUsed=_ApBKIDUsed_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,29),_ApBKIDUsed_Type())
apBKIDUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:apBKIDUsed.setStatus(_A)
_ApAuthSuiteRequested_Type=OctetString
_ApAuthSuiteRequested_Object=MibTableColumn
apAuthSuiteRequested=_ApAuthSuiteRequested_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,30),_ApAuthSuiteRequested_Type())
apAuthSuiteRequested.setMaxAccess(_B)
if mibBuilder.loadTexts:apAuthSuiteRequested.setStatus(_A)
_ApUnicastCipherRequested_Type=OctetString
_ApUnicastCipherRequested_Object=MibTableColumn
apUnicastCipherRequested=_ApUnicastCipherRequested_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,31),_ApUnicastCipherRequested_Type())
apUnicastCipherRequested.setMaxAccess(_B)
if mibBuilder.loadTexts:apUnicastCipherRequested.setStatus(_A)
_ApMulticastCipherRequested_Type=OctetString
_ApMulticastCipherRequested_Object=MibTableColumn
apMulticastCipherRequested=_ApMulticastCipherRequested_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,1,1,32),_ApMulticastCipherRequested_Type())
apMulticastCipherRequested.setMaxAccess(_B)
if mibBuilder.loadTexts:apMulticastCipherRequested.setStatus(_A)
_ApWapiUnicastCfgTable_Object=MibTable
apWapiUnicastCfgTable=_ApWapiUnicastCfgTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,2))
if mibBuilder.loadTexts:apWapiUnicastCfgTable.setStatus(_A)
_ApWapiUnicastCfgEntry_Object=MibTableRow
apWapiUnicastCfgEntry=_ApWapiUnicastCfgEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,2,1))
apWapiUnicastCfgEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:apWapiUnicastCfgEntry.setStatus(_A)
_ApUnicastCipher_Type=OctetString
_ApUnicastCipher_Object=MibTableColumn
apUnicastCipher=_ApUnicastCipher_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,2,1,1),_ApUnicastCipher_Type())
apUnicastCipher.setMaxAccess(_B)
if mibBuilder.loadTexts:apUnicastCipher.setStatus(_A)
_ApUnicastCipherEnabled_Type=TruthValue
_ApUnicastCipherEnabled_Object=MibTableColumn
apUnicastCipherEnabled=_ApUnicastCipherEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,2,1,2),_ApUnicastCipherEnabled_Type())
apUnicastCipherEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:apUnicastCipherEnabled.setStatus(_A)
_ApUnicastCipherSize_Type=Unsigned32
_ApUnicastCipherSize_Object=MibTableColumn
apUnicastCipherSize=_ApUnicastCipherSize_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,2,1,3),_ApUnicastCipherSize_Type())
apUnicastCipherSize.setMaxAccess(_B)
if mibBuilder.loadTexts:apUnicastCipherSize.setStatus(_A)
_ApWapiAKMCfgTable_Object=MibTable
apWapiAKMCfgTable=_ApWapiAKMCfgTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,3))
if mibBuilder.loadTexts:apWapiAKMCfgTable.setStatus(_A)
_ApWapiAKMCfgEntry_Object=MibTableRow
apWapiAKMCfgEntry=_ApWapiAKMCfgEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,3,1))
apWapiAKMCfgEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:apWapiAKMCfgEntry.setStatus(_A)
_ApAuthenticationSuite_Type=OctetString
_ApAuthenticationSuite_Object=MibTableColumn
apAuthenticationSuite=_ApAuthenticationSuite_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,3,1,1),_ApAuthenticationSuite_Type())
apAuthenticationSuite.setMaxAccess(_B)
if mibBuilder.loadTexts:apAuthenticationSuite.setStatus(_A)
_ApAuthenticationSuiteEnabled_Type=TruthValue
_ApAuthenticationSuiteEnabled_Object=MibTableColumn
apAuthenticationSuiteEnabled=_ApAuthenticationSuiteEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,8,3,1,2),_ApAuthenticationSuiteEnabled_Type())
apAuthenticationSuiteEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:apAuthenticationSuiteEnabled.setStatus(_A)
_ApSyslogCfg_ObjectIdentity=ObjectIdentity
apSyslogCfg=_ApSyslogCfg_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,8,9))
_ApSyslogSvcEnable_Type=TruthValue
_ApSyslogSvcEnable_Object=MibScalar
apSyslogSvcEnable=_ApSyslogSvcEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,9,1),_ApSyslogSvcEnable_Type())
apSyslogSvcEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:apSyslogSvcEnable.setStatus(_A)
_ApSyslogReportEventLevel_Type=Integer32
_ApSyslogReportEventLevel_Object=MibScalar
apSyslogReportEventLevel=_ApSyslogReportEventLevel_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,9,2),_ApSyslogReportEventLevel_Type())
apSyslogReportEventLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:apSyslogReportEventLevel.setStatus(_A)
_ApSyslogSvrCfgTable_Object=MibTable
apSyslogSvrCfgTable=_ApSyslogSvrCfgTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,9,3))
if mibBuilder.loadTexts:apSyslogSvrCfgTable.setStatus(_A)
_ApSyslogSvrCfgEntry_Object=MibTableRow
apSyslogSvrCfgEntry=_ApSyslogSvrCfgEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,9,3,1))
apSyslogSvrCfgEntry.setIndexNames((0,_D,_Y))
if mibBuilder.loadTexts:apSyslogSvrCfgEntry.setStatus(_A)
_ApSyslogSvrIndex_Type=Integer32
_ApSyslogSvrIndex_Object=MibTableColumn
apSyslogSvrIndex=_ApSyslogSvrIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,9,3,1,1),_ApSyslogSvrIndex_Type())
apSyslogSvrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:apSyslogSvrIndex.setStatus(_A)
_ApSyslogServerAddr_Type=TAddress
_ApSyslogServerAddr_Object=MibTableColumn
apSyslogServerAddr=_ApSyslogServerAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,9,3,1,2),_ApSyslogServerAddr_Type())
apSyslogServerAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:apSyslogServerAddr.setStatus(_A)
_ApSyslogStatus_Type=RowStatus
_ApSyslogStatus_Object=MibTableColumn
apSyslogStatus=_ApSyslogStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,9,3,1,3),_ApSyslogStatus_Type())
apSyslogStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:apSyslogStatus.setStatus(_A)
_ApSoftwareUpdate_ObjectIdentity=ObjectIdentity
apSoftwareUpdate=_ApSoftwareUpdate_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,8,10))
_ApLoadFlag_Type=Integer32
_ApLoadFlag_Object=MibScalar
apLoadFlag=_ApLoadFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,10,1),_ApLoadFlag_Type())
apLoadFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:apLoadFlag.setStatus(_A)
_ApFileName_Type=DisplayString
_ApFileName_Object=MibScalar
apFileName=_ApFileName_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,10,2),_ApFileName_Type())
apFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:apFileName.setStatus(_A)
_ApFileType_Type=Integer32
_ApFileType_Object=MibScalar
apFileType=_ApFileType_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,10,3),_ApFileType_Type())
apFileType.setMaxAccess(_C)
if mibBuilder.loadTexts:apFileType.setStatus(_A)
_ApTransProtocol_Type=Integer32
_ApTransProtocol_Object=MibScalar
apTransProtocol=_ApTransProtocol_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,10,4),_ApTransProtocol_Type())
apTransProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:apTransProtocol.setStatus(_A)
_ApServerAddr_Type=IpAddress
_ApServerAddr_Object=MibScalar
apServerAddr=_ApServerAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,10,5),_ApServerAddr_Type())
apServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:apServerAddr.setStatus(_A)
_ApServerPort_Type=Integer32
_ApServerPort_Object=MibScalar
apServerPort=_ApServerPort_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,10,6),_ApServerPort_Type())
apServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:apServerPort.setStatus(_A)
_ApServerUsername_Type=DisplayString
_ApServerUsername_Object=MibScalar
apServerUsername=_ApServerUsername_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,10,7),_ApServerUsername_Type())
apServerUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:apServerUsername.setStatus(_A)
_ApServerPasswd_Type=DisplayString
_ApServerPasswd_Object=MibScalar
apServerPasswd=_ApServerPasswd_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,10,8),_ApServerPasswd_Type())
apServerPasswd.setMaxAccess(_C)
if mibBuilder.loadTexts:apServerPasswd.setStatus(_A)
_ApTransStatus_Type=Integer32
_ApTransStatus_Object=MibScalar
apTransStatus=_ApTransStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,10,9),_ApTransStatus_Type())
apTransStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:apTransStatus.setStatus(_A)
_ApFailReason_Type=DisplayString
_ApFailReason_Object=MibScalar
apFailReason=_ApFailReason_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,10,10),_ApFailReason_Type())
apFailReason.setMaxAccess(_B)
if mibBuilder.loadTexts:apFailReason.setStatus(_A)
_ApCfgFileDistribute_ObjectIdentity=ObjectIdentity
apCfgFileDistribute=_ApCfgFileDistribute_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,8,11))
_ApCfgFileLoadFlag_Type=Integer32
_ApCfgFileLoadFlag_Object=MibScalar
apCfgFileLoadFlag=_ApCfgFileLoadFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,11,1),_ApCfgFileLoadFlag_Type())
apCfgFileLoadFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:apCfgFileLoadFlag.setStatus(_A)
_ApCfgFileFileName_Type=DisplayString
_ApCfgFileFileName_Object=MibScalar
apCfgFileFileName=_ApCfgFileFileName_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,11,2),_ApCfgFileFileName_Type())
apCfgFileFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:apCfgFileFileName.setStatus(_A)
_ApCfgFileFileType_Type=Integer32
_ApCfgFileFileType_Object=MibScalar
apCfgFileFileType=_ApCfgFileFileType_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,11,3),_ApCfgFileFileType_Type())
apCfgFileFileType.setMaxAccess(_C)
if mibBuilder.loadTexts:apCfgFileFileType.setStatus(_A)
_ApCfgFileTransProtocol_Type=Integer32
_ApCfgFileTransProtocol_Object=MibScalar
apCfgFileTransProtocol=_ApCfgFileTransProtocol_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,11,4),_ApCfgFileTransProtocol_Type())
apCfgFileTransProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:apCfgFileTransProtocol.setStatus(_A)
_ApCfgFileServerAddr_Type=IpAddress
_ApCfgFileServerAddr_Object=MibScalar
apCfgFileServerAddr=_ApCfgFileServerAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,11,5),_ApCfgFileServerAddr_Type())
apCfgFileServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:apCfgFileServerAddr.setStatus(_A)
_ApCfgFileServerPort_Type=Integer32
_ApCfgFileServerPort_Object=MibScalar
apCfgFileServerPort=_ApCfgFileServerPort_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,11,6),_ApCfgFileServerPort_Type())
apCfgFileServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:apCfgFileServerPort.setStatus(_A)
_ApCfgFileServerUsername_Type=DisplayString
_ApCfgFileServerUsername_Object=MibScalar
apCfgFileServerUsername=_ApCfgFileServerUsername_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,11,7),_ApCfgFileServerUsername_Type())
apCfgFileServerUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:apCfgFileServerUsername.setStatus(_A)
_ApCfgFileServerPasswd_Type=DisplayString
_ApCfgFileServerPasswd_Object=MibScalar
apCfgFileServerPasswd=_ApCfgFileServerPasswd_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,11,8),_ApCfgFileServerPasswd_Type())
apCfgFileServerPasswd.setMaxAccess(_C)
if mibBuilder.loadTexts:apCfgFileServerPasswd.setStatus(_A)
_ApCfgFileTransStatus_Type=Integer32
_ApCfgFileTransStatus_Object=MibScalar
apCfgFileTransStatus=_ApCfgFileTransStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,11,9),_ApCfgFileTransStatus_Type())
apCfgFileTransStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:apCfgFileTransStatus.setStatus(_A)
_ApCfgFileFailReason_Type=DisplayString
_ApCfgFileFailReason_Object=MibScalar
apCfgFileFailReason=_ApCfgFileFailReason_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,11,10),_ApCfgFileFailReason_Type())
apCfgFileFailReason.setMaxAccess(_C)
if mibBuilder.loadTexts:apCfgFileFailReason.setStatus(_A)
_ApAccessControl_ObjectIdentity=ObjectIdentity
apAccessControl=_ApAccessControl_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,8,12))
_ApTerminalPermitTable_Object=MibTable
apTerminalPermitTable=_ApTerminalPermitTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,12,1))
if mibBuilder.loadTexts:apTerminalPermitTable.setStatus(_A)
_ApTerminalPermitEntry_Object=MibTableRow
apTerminalPermitEntry=_ApTerminalPermitEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,12,1,1))
apTerminalPermitEntry.setIndexNames((0,_D,_Z))
if mibBuilder.loadTexts:apTerminalPermitEntry.setStatus(_A)
_ApWhiteListIndex_Type=Integer32
_ApWhiteListIndex_Object=MibTableColumn
apWhiteListIndex=_ApWhiteListIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,12,1,1,1),_ApWhiteListIndex_Type())
apWhiteListIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:apWhiteListIndex.setStatus(_A)
_ApPermitMAC_Type=MacAddress
_ApPermitMAC_Object=MibTableColumn
apPermitMAC=_ApPermitMAC_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,12,1,1,2),_ApPermitMAC_Type())
apPermitMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:apPermitMAC.setStatus(_A)
_ApWhiteListStatus_Type=RowStatus
_ApWhiteListStatus_Object=MibTableColumn
apWhiteListStatus=_ApWhiteListStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,12,1,1,3),_ApWhiteListStatus_Type())
apWhiteListStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:apWhiteListStatus.setStatus(_A)
_ApTerminalDeniedTable_Object=MibTable
apTerminalDeniedTable=_ApTerminalDeniedTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,12,2))
if mibBuilder.loadTexts:apTerminalDeniedTable.setStatus(_A)
_ApTerminalDeniedEntry_Object=MibTableRow
apTerminalDeniedEntry=_ApTerminalDeniedEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,12,2,1))
apTerminalDeniedEntry.setIndexNames((0,_D,_a))
if mibBuilder.loadTexts:apTerminalDeniedEntry.setStatus(_A)
_ApBlackListIndex_Type=Integer32
_ApBlackListIndex_Object=MibTableColumn
apBlackListIndex=_ApBlackListIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,12,2,1,1),_ApBlackListIndex_Type())
apBlackListIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:apBlackListIndex.setStatus(_A)
_ApAttackDeviceMAC_Type=MacAddress
_ApAttackDeviceMAC_Object=MibTableColumn
apAttackDeviceMAC=_ApAttackDeviceMAC_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,12,2,1,2),_ApAttackDeviceMAC_Type())
apAttackDeviceMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:apAttackDeviceMAC.setStatus(_A)
_ApBlackListStatus_Type=RowStatus
_ApBlackListStatus_Object=MibTableColumn
apBlackListStatus=_ApBlackListStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,12,2,1,3),_ApBlackListStatus_Type())
apBlackListStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:apBlackListStatus.setStatus(_A)
_ApTrapConfig_ObjectIdentity=ObjectIdentity
apTrapConfig=_ApTrapConfig_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,8,13))
_ApTrapResendWaitingTime_Type=Integer32
_ApTrapResendWaitingTime_Object=MibScalar
apTrapResendWaitingTime=_ApTrapResendWaitingTime_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,13,1),_ApTrapResendWaitingTime_Type())
apTrapResendWaitingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:apTrapResendWaitingTime.setStatus(_A)
_ApCPUusageThreshhd_Type=Integer32
_ApCPUusageThreshhd_Object=MibScalar
apCPUusageThreshhd=_ApCPUusageThreshhd_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,13,2),_ApCPUusageThreshhd_Type())
apCPUusageThreshhd.setMaxAccess(_C)
if mibBuilder.loadTexts:apCPUusageThreshhd.setStatus(_A)
_ApMemUsageThreshhd_Type=Integer32
_ApMemUsageThreshhd_Object=MibScalar
apMemUsageThreshhd=_ApMemUsageThreshhd_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,13,3),_ApMemUsageThreshhd_Type())
apMemUsageThreshhd.setMaxAccess(_C)
if mibBuilder.loadTexts:apMemUsageThreshhd.setStatus(_A)
_ApAPCoInterfThreshhd_Type=Integer32
_ApAPCoInterfThreshhd_Object=MibScalar
apAPCoInterfThreshhd=_ApAPCoInterfThreshhd_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,13,4),_ApAPCoInterfThreshhd_Type())
apAPCoInterfThreshhd.setMaxAccess(_C)
if mibBuilder.loadTexts:apAPCoInterfThreshhd.setStatus(_A)
_ApAPNeiborInterfThreshhd_Type=Integer32
_ApAPNeiborInterfThreshhd_Object=MibScalar
apAPNeiborInterfThreshhd=_ApAPNeiborInterfThreshhd_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,13,5),_ApAPNeiborInterfThreshhd_Type())
apAPNeiborInterfThreshhd.setMaxAccess(_C)
if mibBuilder.loadTexts:apAPNeiborInterfThreshhd.setStatus(_A)
_ApStaInterfNumThreshhd_Type=Integer32
_ApStaInterfNumThreshhd_Object=MibScalar
apStaInterfNumThreshhd=_ApStaInterfNumThreshhd_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,13,6),_ApStaInterfNumThreshhd_Type())
apStaInterfNumThreshhd.setMaxAccess(_C)
if mibBuilder.loadTexts:apStaInterfNumThreshhd.setStatus(_A)
_ApHeartbeatOnOff_Type=Integer32
_ApHeartbeatOnOff_Object=MibScalar
apHeartbeatOnOff=_ApHeartbeatOnOff_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,13,7),_ApHeartbeatOnOff_Type())
apHeartbeatOnOff.setMaxAccess(_C)
if mibBuilder.loadTexts:apHeartbeatOnOff.setStatus(_A)
_ApHeartbeatPeriod_Type=Integer32
_ApHeartbeatPeriod_Object=MibScalar
apHeartbeatPeriod=_ApHeartbeatPeriod_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,13,8),_ApHeartbeatPeriod_Type())
apHeartbeatPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:apHeartbeatPeriod.setStatus(_A)
_ApTrapAddrTable_Object=MibTable
apTrapAddrTable=_ApTrapAddrTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,13,9))
if mibBuilder.loadTexts:apTrapAddrTable.setStatus(_A)
_ApTrapAddrEntry_Object=MibTableRow
apTrapAddrEntry=_ApTrapAddrEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,13,9,1))
apTrapAddrEntry.setIndexNames((0,_D,_b))
if mibBuilder.loadTexts:apTrapAddrEntry.setStatus(_A)
_ApTrapDesAddrIndex_Type=Integer32
_ApTrapDesAddrIndex_Object=MibTableColumn
apTrapDesAddrIndex=_ApTrapDesAddrIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,13,9,1,1),_ApTrapDesAddrIndex_Type())
apTrapDesAddrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:apTrapDesAddrIndex.setStatus(_A)
_ApTrapDesIPAddress_Type=IpAddress
_ApTrapDesIPAddress_Object=MibTableColumn
apTrapDesIPAddress=_ApTrapDesIPAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,13,9,1,2),_ApTrapDesIPAddress_Type())
apTrapDesIPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:apTrapDesIPAddress.setStatus(_A)
_ApTrapAddrStatus_Type=RowStatus
_ApTrapAddrStatus_Object=MibTableColumn
apTrapAddrStatus=_ApTrapAddrStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,13,9,1,3),_ApTrapAddrStatus_Type())
apTrapAddrStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:apTrapAddrStatus.setStatus(_A)
_ApTrapEnabledTable_Object=MibTable
apTrapEnabledTable=_ApTrapEnabledTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,13,10))
if mibBuilder.loadTexts:apTrapEnabledTable.setStatus(_A)
_ApTrapEnabledEntry_Object=MibTableRow
apTrapEnabledEntry=_ApTrapEnabledEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,13,10,1))
apTrapEnabledEntry.setIndexNames((0,_D,_c))
if mibBuilder.loadTexts:apTrapEnabledEntry.setStatus(_A)
_ApTrapEnabledIndex_Type=Integer32
_ApTrapEnabledIndex_Object=MibTableColumn
apTrapEnabledIndex=_ApTrapEnabledIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,13,10,1,1),_ApTrapEnabledIndex_Type())
apTrapEnabledIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:apTrapEnabledIndex.setStatus(_A)
_ApTrapName_Type=DisplayString
_ApTrapName_Object=MibTableColumn
apTrapName=_ApTrapName_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,13,10,1,2),_ApTrapName_Type())
apTrapName.setMaxAccess(_B)
if mibBuilder.loadTexts:apTrapName.setStatus(_A)
_ApTrapDescr_Type=DisplayString
_ApTrapDescr_Object=MibTableColumn
apTrapDescr=_ApTrapDescr_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,13,10,1,3),_ApTrapDescr_Type())
apTrapDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:apTrapDescr.setStatus(_A)
_ApTrapOnOff_Type=Integer32
_ApTrapOnOff_Object=MibTableColumn
apTrapOnOff=_ApTrapOnOff_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,13,10,1,4),_ApTrapOnOff_Type())
apTrapOnOff.setMaxAccess(_C)
if mibBuilder.loadTexts:apTrapOnOff.setStatus(_A)
_ApVlanConfig_ObjectIdentity=ObjectIdentity
apVlanConfig=_ApVlanConfig_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,8,14))
_ApVlanConfigTable_Object=MibTable
apVlanConfigTable=_ApVlanConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,14,10))
if mibBuilder.loadTexts:apVlanConfigTable.setStatus(_A)
_ApVlanConfigEntry_Object=MibTableRow
apVlanConfigEntry=_ApVlanConfigEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,14,10,1))
apVlanConfigEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:apVlanConfigEntry.setStatus(_A)
_ApVlanCfgVlanId_Type=Integer32
_ApVlanCfgVlanId_Object=MibTableColumn
apVlanCfgVlanId=_ApVlanCfgVlanId_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,14,10,1,1),_ApVlanCfgVlanId_Type())
apVlanCfgVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:apVlanCfgVlanId.setStatus(_A)
_ApVlanCfgStatus_Type=RowStatus
_ApVlanCfgStatus_Object=MibTableColumn
apVlanCfgStatus=_ApVlanCfgStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,14,10,1,2),_ApVlanCfgStatus_Type())
apVlanCfgStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:apVlanCfgStatus.setStatus(_A)
_ApHeartbeatConfig_ObjectIdentity=ObjectIdentity
apHeartbeatConfig=_ApHeartbeatConfig_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,8,15))
_ApHeartbeatCycle_Type=Integer32
_ApHeartbeatCycle_Object=MibScalar
apHeartbeatCycle=_ApHeartbeatCycle_Object((1,3,6,1,4,1,27514,1,1,10,2,80,8,15,1),_ApHeartbeatCycle_Type())
apHeartbeatCycle.setMaxAccess(_C)
if mibBuilder.loadTexts:apHeartbeatCycle.setStatus(_A)
_ApPerformanceStatObjects_ObjectIdentity=ObjectIdentity
apPerformanceStatObjects=_ApPerformanceStatObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,9))
_ApSysPerformanceStat_ObjectIdentity=ObjectIdentity
apSysPerformanceStat=_ApSysPerformanceStat_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,9,1))
_ApCPURTUsage_Type=Integer32
_ApCPURTUsage_Object=MibScalar
apCPURTUsage=_ApCPURTUsage_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,1,1),_ApCPURTUsage_Type())
apCPURTUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:apCPURTUsage.setStatus(_A)
_ApCPUAvgUsage_Type=Integer32
_ApCPUAvgUsage_Object=MibScalar
apCPUAvgUsage=_ApCPUAvgUsage_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,1,2),_ApCPUAvgUsage_Type())
apCPUAvgUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:apCPUAvgUsage.setStatus(_A)
_ApMemRTUsage_Type=Integer32
_ApMemRTUsage_Object=MibScalar
apMemRTUsage=_ApMemRTUsage_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,1,3),_ApMemRTUsage_Type())
apMemRTUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:apMemRTUsage.setStatus(_A)
_ApMemAvgUsage_Type=Integer32
_ApMemAvgUsage_Object=MibScalar
apMemAvgUsage=_ApMemAvgUsage_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,1,4),_ApMemAvgUsage_Type())
apMemAvgUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:apMemAvgUsage.setStatus(_A)
_ApConInfoStat_ObjectIdentity=ObjectIdentity
apConInfoStat=_ApConInfoStat_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,9,2))
_ApApStationAssocSum_Type=Integer32
_ApApStationAssocSum_Object=MibScalar
apApStationAssocSum=_ApApStationAssocSum_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,2,1),_ApApStationAssocSum_Type())
apApStationAssocSum.setMaxAccess(_B)
if mibBuilder.loadTexts:apApStationAssocSum.setStatus(_A)
_ApApStationOnlineSum_Type=Integer32
_ApApStationOnlineSum_Object=MibScalar
apApStationOnlineSum=_ApApStationOnlineSum_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,2,2),_ApApStationOnlineSum_Type())
apApStationOnlineSum.setMaxAccess(_B)
if mibBuilder.loadTexts:apApStationOnlineSum.setStatus(_A)
_ApAssocTimes_Type=Counter32
_ApAssocTimes_Object=MibScalar
apAssocTimes=_ApAssocTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,2,3),_ApAssocTimes_Type())
apAssocTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:apAssocTimes.setStatus(_A)
_ApAssocFailTimes_Type=Counter32
_ApAssocFailTimes_Object=MibScalar
apAssocFailTimes=_ApAssocFailTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,2,4),_ApAssocFailTimes_Type())
apAssocFailTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:apAssocFailTimes.setStatus(_A)
_ApReassocTimes_Type=Counter32
_ApReassocTimes_Object=MibScalar
apReassocTimes=_ApReassocTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,2,5),_ApReassocTimes_Type())
apReassocTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:apReassocTimes.setStatus(_A)
_ApPreAssCannotShiftDeassocFailSum_Type=Counter32
_ApPreAssCannotShiftDeassocFailSum_Object=MibScalar
apPreAssCannotShiftDeassocFailSum=_ApPreAssCannotShiftDeassocFailSum_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,2,6),_ApPreAssCannotShiftDeassocFailSum_Type())
apPreAssCannotShiftDeassocFailSum.setMaxAccess(_B)
if mibBuilder.loadTexts:apPreAssCannotShiftDeassocFailSum.setStatus(_A)
_ApApStatsDisassociated_Type=Counter32
_ApApStatsDisassociated_Object=MibScalar
apApStatsDisassociated=_ApApStatsDisassociated_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,2,7),_ApApStatsDisassociated_Type())
apApStatsDisassociated.setMaxAccess(_B)
if mibBuilder.loadTexts:apApStatsDisassociated.setStatus(_A)
_ApAssocRejectSum_Type=Counter32
_ApAssocRejectSum_Object=MibScalar
apAssocRejectSum=_ApAssocRejectSum_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,2,8),_ApAssocRejectSum_Type())
apAssocRejectSum.setMaxAccess(_B)
if mibBuilder.loadTexts:apAssocRejectSum.setStatus(_A)
_ApBSSNotSupportAssocFailSum_Type=Counter32
_ApBSSNotSupportAssocFailSum_Object=MibScalar
apBSSNotSupportAssocFailSum=_ApBSSNotSupportAssocFailSum_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,2,9),_ApBSSNotSupportAssocFailSum_Type())
apBSSNotSupportAssocFailSum.setMaxAccess(_B)
if mibBuilder.loadTexts:apBSSNotSupportAssocFailSum.setStatus(_A)
_ApIfPeformanceStat_ObjectIdentity=ObjectIdentity
apIfPeformanceStat=_ApIfPeformanceStat_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,9,3))
_ApWiredIfPfmStatTable_Object=MibTable
apWiredIfPfmStatTable=_ApWiredIfPfmStatTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,1))
if mibBuilder.loadTexts:apWiredIfPfmStatTable.setStatus(_A)
_ApWiredIfPfmStatEntry_Object=MibTableRow
apWiredIfPfmStatEntry=_ApWiredIfPfmStatEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,1,1))
apWiredIfPfmStatEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:apWiredIfPfmStatEntry.setStatus(_A)
_ApIfInUcastPkts_Type=Counter32
_ApIfInUcastPkts_Object=MibTableColumn
apIfInUcastPkts=_ApIfInUcastPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,1,1,1),_ApIfInUcastPkts_Type())
apIfInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfInUcastPkts.setStatus(_A)
_ApIfInNUcastPkts_Type=Counter32
_ApIfInNUcastPkts_Object=MibTableColumn
apIfInNUcastPkts=_ApIfInNUcastPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,1,1,2),_ApIfInNUcastPkts_Type())
apIfInNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfInNUcastPkts.setStatus(_A)
_ApIfInOctets_Type=Counter32
_ApIfInOctets_Object=MibTableColumn
apIfInOctets=_ApIfInOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,1,1,3),_ApIfInOctets_Type())
apIfInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfInOctets.setStatus(_A)
_ApIfInDiscardPkts_Type=Counter32
_ApIfInDiscardPkts_Object=MibTableColumn
apIfInDiscardPkts=_ApIfInDiscardPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,1,1,4),_ApIfInDiscardPkts_Type())
apIfInDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfInDiscardPkts.setStatus(_A)
_ApIfInErrors_Type=Counter32
_ApIfInErrors_Object=MibTableColumn
apIfInErrors=_ApIfInErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,1,1,5),_ApIfInErrors_Type())
apIfInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfInErrors.setStatus(_A)
_ApIfOutUcastPkts_Type=Counter32
_ApIfOutUcastPkts_Object=MibTableColumn
apIfOutUcastPkts=_ApIfOutUcastPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,1,1,6),_ApIfOutUcastPkts_Type())
apIfOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfOutUcastPkts.setStatus(_A)
_ApIfOutNUcastPkts_Type=Counter32
_ApIfOutNUcastPkts_Object=MibTableColumn
apIfOutNUcastPkts=_ApIfOutNUcastPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,1,1,7),_ApIfOutNUcastPkts_Type())
apIfOutNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfOutNUcastPkts.setStatus(_A)
_ApIfOutOctets_Type=Counter32
_ApIfOutOctets_Object=MibTableColumn
apIfOutOctets=_ApIfOutOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,1,1,8),_ApIfOutOctets_Type())
apIfOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfOutOctets.setStatus(_A)
_ApIfOutDiscardPkts_Type=Counter32
_ApIfOutDiscardPkts_Object=MibTableColumn
apIfOutDiscardPkts=_ApIfOutDiscardPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,1,1,9),_ApIfOutDiscardPkts_Type())
apIfOutDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfOutDiscardPkts.setStatus(_A)
_ApIfOutErrors_Type=Counter32
_ApIfOutErrors_Object=MibTableColumn
apIfOutErrors=_ApIfOutErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,1,1,10),_ApIfOutErrors_Type())
apIfOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfOutErrors.setStatus(_A)
_ApIfUpDwnTimes_Type=Counter32
_ApIfUpDwnTimes_Object=MibTableColumn
apIfUpDwnTimes=_ApIfUpDwnTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,1,1,11),_ApIfUpDwnTimes_Type())
apIfUpDwnTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:apIfUpDwnTimes.setStatus(_A)
_ApRadioIfPfmStatTable_Object=MibTable
apRadioIfPfmStatTable=_ApRadioIfPfmStatTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2))
if mibBuilder.loadTexts:apRadioIfPfmStatTable.setStatus(_A)
_ApRadioIfPfmStatEntry_Object=MibTableRow
apRadioIfPfmStatEntry=_ApRadioIfPfmStatEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1))
apRadioIfPfmStatEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:apRadioIfPfmStatEntry.setStatus(_A)
_ApAvgRxSignalStrength_Type=Integer32
_ApAvgRxSignalStrength_Object=MibTableColumn
apAvgRxSignalStrength=_ApAvgRxSignalStrength_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,1),_ApAvgRxSignalStrength_Type())
apAvgRxSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:apAvgRxSignalStrength.setStatus(_A)
_ApHighestRxSignalStrength_Type=Integer32
_ApHighestRxSignalStrength_Object=MibTableColumn
apHighestRxSignalStrength=_ApHighestRxSignalStrength_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,2),_ApHighestRxSignalStrength_Type())
apHighestRxSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:apHighestRxSignalStrength.setStatus(_A)
_ApLowestRxSignalStrength_Type=Integer32
_ApLowestRxSignalStrength_Object=MibTableColumn
apLowestRxSignalStrength=_ApLowestRxSignalStrength_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,3),_ApLowestRxSignalStrength_Type())
apLowestRxSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:apLowestRxSignalStrength.setStatus(_A)
_ApUpdownTimes_Type=Counter32
_ApUpdownTimes_Object=MibTableColumn
apUpdownTimes=_ApUpdownTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,4),_ApUpdownTimes_Type())
apUpdownTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:apUpdownTimes.setStatus(_A)
_ApTxDataPkts_Type=Counter32
_ApTxDataPkts_Object=MibTableColumn
apTxDataPkts=_ApTxDataPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,5),_ApTxDataPkts_Type())
apTxDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apTxDataPkts.setStatus(_A)
_ApRxDataPkts_Type=Counter32
_ApRxDataPkts_Object=MibTableColumn
apRxDataPkts=_ApRxDataPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,6),_ApRxDataPkts_Type())
apRxDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apRxDataPkts.setStatus(_A)
_ApUplinkDataOctets_Type=Counter64
_ApUplinkDataOctets_Object=MibTableColumn
apUplinkDataOctets=_ApUplinkDataOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,7),_ApUplinkDataOctets_Type())
apUplinkDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:apUplinkDataOctets.setStatus(_A)
_ApDwlinkDataOctets_Type=Counter64
_ApDwlinkDataOctets_Object=MibTableColumn
apDwlinkDataOctets=_ApDwlinkDataOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,8),_ApDwlinkDataOctets_Type())
apDwlinkDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:apDwlinkDataOctets.setStatus(_A)
_ApChStatsDwlinkTotRetryPkts_Type=Counter32
_ApChStatsDwlinkTotRetryPkts_Object=MibTableColumn
apChStatsDwlinkTotRetryPkts=_ApChStatsDwlinkTotRetryPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,9),_ApChStatsDwlinkTotRetryPkts_Type())
apChStatsDwlinkTotRetryPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apChStatsDwlinkTotRetryPkts.setStatus(_A)
_ApChStatsPhyErrPkts_Type=Counter32
_ApChStatsPhyErrPkts_Object=MibTableColumn
apChStatsPhyErrPkts=_ApChStatsPhyErrPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,10),_ApChStatsPhyErrPkts_Type())
apChStatsPhyErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apChStatsPhyErrPkts.setStatus(_A)
_ApChStatsMacFcsErrPkts_Type=Counter32
_ApChStatsMacFcsErrPkts_Object=MibTableColumn
apChStatsMacFcsErrPkts=_ApChStatsMacFcsErrPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,11),_ApChStatsMacFcsErrPkts_Type())
apChStatsMacFcsErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apChStatsMacFcsErrPkts.setStatus(_A)
_ApChStatsMacMicErrPkts_Type=Counter32
_ApChStatsMacMicErrPkts_Object=MibTableColumn
apChStatsMacMicErrPkts=_ApChStatsMacMicErrPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,12),_ApChStatsMacMicErrPkts_Type())
apChStatsMacMicErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apChStatsMacMicErrPkts.setStatus(_A)
_ApChStatsMacDecryptErrPkts_Type=Counter32
_ApChStatsMacDecryptErrPkts_Object=MibTableColumn
apChStatsMacDecryptErrPkts=_ApChStatsMacDecryptErrPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,13),_ApChStatsMacDecryptErrPkts_Type())
apChStatsMacDecryptErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apChStatsMacDecryptErrPkts.setStatus(_A)
_ApChStatsTotalErrPkts_Type=Counter32
_ApChStatsTotalErrPkts_Object=MibTableColumn
apChStatsTotalErrPkts=_ApChStatsTotalErrPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,14),_ApChStatsTotalErrPkts_Type())
apChStatsTotalErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apChStatsTotalErrPkts.setStatus(_A)
_ApRxMgmtFrameCnt_Type=Counter32
_ApRxMgmtFrameCnt_Object=MibTableColumn
apRxMgmtFrameCnt=_ApRxMgmtFrameCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,15),_ApRxMgmtFrameCnt_Type())
apRxMgmtFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:apRxMgmtFrameCnt.setStatus(_A)
_ApRxCtrlFrameCnt_Type=Counter32
_ApRxCtrlFrameCnt_Object=MibTableColumn
apRxCtrlFrameCnt=_ApRxCtrlFrameCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,16),_ApRxCtrlFrameCnt_Type())
apRxCtrlFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:apRxCtrlFrameCnt.setStatus(_A)
_ApRxDataFrameCnt_Type=Counter32
_ApRxDataFrameCnt_Object=MibTableColumn
apRxDataFrameCnt=_ApRxDataFrameCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,17),_ApRxDataFrameCnt_Type())
apRxDataFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:apRxDataFrameCnt.setStatus(_A)
_ApTxMgmtFrameCnt_Type=Counter32
_ApTxMgmtFrameCnt_Object=MibTableColumn
apTxMgmtFrameCnt=_ApTxMgmtFrameCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,18),_ApTxMgmtFrameCnt_Type())
apTxMgmtFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:apTxMgmtFrameCnt.setStatus(_A)
_ApTxCtrlFrameCnt_Type=Counter32
_ApTxCtrlFrameCnt_Object=MibTableColumn
apTxCtrlFrameCnt=_ApTxCtrlFrameCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,19),_ApTxCtrlFrameCnt_Type())
apTxCtrlFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:apTxCtrlFrameCnt.setStatus(_A)
_ApTxDataFrameCnt_Type=Counter32
_ApTxDataFrameCnt_Object=MibTableColumn
apTxDataFrameCnt=_ApTxDataFrameCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,20),_ApTxDataFrameCnt_Type())
apTxDataFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:apTxDataFrameCnt.setStatus(_A)
_ApChStatsFrameErrorCnt_Type=Counter32
_ApChStatsFrameErrorCnt_Object=MibTableColumn
apChStatsFrameErrorCnt=_ApChStatsFrameErrorCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,21),_ApChStatsFrameErrorCnt_Type())
apChStatsFrameErrorCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:apChStatsFrameErrorCnt.setStatus(_A)
_ApRetryCnt_Type=Counter32
_ApRetryCnt_Object=MibTableColumn
apRetryCnt=_ApRetryCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,22),_ApRetryCnt_Type())
apRetryCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:apRetryCnt.setStatus(_A)
_ApCurTxPwr_Type=Integer32
_ApCurTxPwr_Object=MibTableColumn
apCurTxPwr=_ApCurTxPwr_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,23),_ApCurTxPwr_Type())
apCurTxPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:apCurTxPwr.setStatus(_A)
_ApAPNeighborSSIDList_Type=DisplayString
_ApAPNeighborSSIDList_Object=MibTableColumn
apAPNeighborSSIDList=_ApAPNeighborSSIDList_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,24),_ApAPNeighborSSIDList_Type())
apAPNeighborSSIDList.setMaxAccess(_B)
if mibBuilder.loadTexts:apAPNeighborSSIDList.setStatus(_A)
_ApChanStaNum_Type=Counter32
_ApChanStaNum_Object=MibTableColumn
apChanStaNum=_ApChanStaNum_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,25),_ApChanStaNum_Type())
apChanStaNum.setMaxAccess(_B)
if mibBuilder.loadTexts:apChanStaNum.setStatus(_A)
_ApChDownUnicastFrame_Type=Counter32
_ApChDownUnicastFrame_Object=MibTableColumn
apChDownUnicastFrame=_ApChDownUnicastFrame_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,26),_ApChDownUnicastFrame_Type())
apChDownUnicastFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:apChDownUnicastFrame.setStatus(_A)
_ApChDownNonUnicastFrame_Type=Counter32
_ApChDownNonUnicastFrame_Object=MibTableColumn
apChDownNonUnicastFrame=_ApChDownNonUnicastFrame_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,27),_ApChDownNonUnicastFrame_Type())
apChDownNonUnicastFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:apChDownNonUnicastFrame.setStatus(_A)
_ApChRxAuthFrame_Type=Counter32
_ApChRxAuthFrame_Object=MibTableColumn
apChRxAuthFrame=_ApChRxAuthFrame_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,28),_ApChRxAuthFrame_Type())
apChRxAuthFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:apChRxAuthFrame.setStatus(_A)
_ApChRxAssoFrame_Type=Counter32
_ApChRxAssoFrame_Object=MibTableColumn
apChRxAssoFrame=_ApChRxAssoFrame_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,29),_ApChRxAssoFrame_Type())
apChRxAssoFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:apChRxAssoFrame.setStatus(_A)
_ApChTxAuthFrame_Type=Counter32
_ApChTxAuthFrame_Object=MibTableColumn
apChTxAuthFrame=_ApChTxAuthFrame_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,30),_ApChTxAuthFrame_Type())
apChTxAuthFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:apChTxAuthFrame.setStatus(_A)
_ApChTxAssoFrame_Type=Counter32
_ApChTxAssoFrame_Object=MibTableColumn
apChTxAssoFrame=_ApChTxAssoFrame_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,3,2,1,31),_ApChTxAssoFrame_Type())
apChTxAssoFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:apChTxAssoFrame.setStatus(_A)
_ApSSIDPeformanceStat_ObjectIdentity=ObjectIdentity
apSSIDPeformanceStat=_ApSSIDPeformanceStat_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,9,4))
_ApSSIDPfmStatTable_Object=MibTable
apSSIDPfmStatTable=_ApSSIDPfmStatTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,4,1))
if mibBuilder.loadTexts:apSSIDPfmStatTable.setStatus(_A)
_ApSSIDPfmStatEntry_Object=MibTableRow
apSSIDPfmStatEntry=_ApSSIDPfmStatEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,4,1,1))
apSSIDPfmStatEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:apSSIDPfmStatEntry.setStatus(_A)
_ApSSIDTxDataPkts_Type=Counter32
_ApSSIDTxDataPkts_Object=MibTableColumn
apSSIDTxDataPkts=_ApSSIDTxDataPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,4,1,1,1),_ApSSIDTxDataPkts_Type())
apSSIDTxDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDTxDataPkts.setStatus(_A)
_ApSSIDRxDataPkts_Type=Counter32
_ApSSIDRxDataPkts_Object=MibTableColumn
apSSIDRxDataPkts=_ApSSIDRxDataPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,4,1,1,2),_ApSSIDRxDataPkts_Type())
apSSIDRxDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDRxDataPkts.setStatus(_A)
_ApSSIDUplinkDataOctets_Type=Counter64
_ApSSIDUplinkDataOctets_Object=MibTableColumn
apSSIDUplinkDataOctets=_ApSSIDUplinkDataOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,4,1,1,3),_ApSSIDUplinkDataOctets_Type())
apSSIDUplinkDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDUplinkDataOctets.setStatus(_A)
_ApSSIDDwlinkDataOctets_Type=Counter64
_ApSSIDDwlinkDataOctets_Object=MibTableColumn
apSSIDDwlinkDataOctets=_ApSSIDDwlinkDataOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,4,1,1,4),_ApSSIDDwlinkDataOctets_Type())
apSSIDDwlinkDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDDwlinkDataOctets.setStatus(_A)
_ApSSIDChStatsDwlinkTotRetryPkts_Type=Counter32
_ApSSIDChStatsDwlinkTotRetryPkts_Object=MibTableColumn
apSSIDChStatsDwlinkTotRetryPkts=_ApSSIDChStatsDwlinkTotRetryPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,4,1,1,5),_ApSSIDChStatsDwlinkTotRetryPkts_Type())
apSSIDChStatsDwlinkTotRetryPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDChStatsDwlinkTotRetryPkts.setStatus(_A)
_ApSSIDApChStatsNumStations_Type=Integer32
_ApSSIDApChStatsNumStations_Object=MibTableColumn
apSSIDApChStatsNumStations=_ApSSIDApChStatsNumStations_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,4,1,1,6),_ApSSIDApChStatsNumStations_Type())
apSSIDApChStatsNumStations.setMaxAccess(_B)
if mibBuilder.loadTexts:apSSIDApChStatsNumStations.setStatus(_A)
_ApTermPeformanceStat_ObjectIdentity=ObjectIdentity
apTermPeformanceStat=_ApTermPeformanceStat_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,9,5))
_ApTermPfmStatTable_Object=MibTable
apTermPfmStatTable=_ApTermPfmStatTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,5,1))
if mibBuilder.loadTexts:apTermPfmStatTable.setStatus(_A)
_ApTermPfmStatEntry_Object=MibTableRow
apTermPfmStatEntry=_ApTermPfmStatEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,5,1,1))
apTermPfmStatEntry.setIndexNames((0,_D,_d))
if mibBuilder.loadTexts:apTermPfmStatEntry.setStatus(_A)
_ApStaAddress_Type=MacAddress
_ApStaAddress_Object=MibTableColumn
apStaAddress=_ApStaAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,5,1,1,1),_ApStaAddress_Type())
apStaAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaAddress.setStatus(_A)
_ApStaUpTime_Type=TimeTicks
_ApStaUpTime_Object=MibTableColumn
apStaUpTime=_ApStaUpTime_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,5,1,1,2),_ApStaUpTime_Type())
apStaUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaUpTime.setStatus(_A)
_ApAPReceivedStaSignalStrength_Type=Counter32
_ApAPReceivedStaSignalStrength_Object=MibTableColumn
apAPReceivedStaSignalStrength=_ApAPReceivedStaSignalStrength_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,5,1,1,3),_ApAPReceivedStaSignalStrength_Type())
apAPReceivedStaSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:apAPReceivedStaSignalStrength.setStatus(_A)
_ApAPReceiveStaSNR_Type=Counter32
_ApAPReceiveStaSNR_Object=MibTableColumn
apAPReceiveStaSNR=_ApAPReceiveStaSNR_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,5,1,1,4),_ApAPReceiveStaSNR_Type())
apAPReceiveStaSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:apAPReceiveStaSNR.setStatus(_A)
_ApStaTxPkts_Type=Counter32
_ApStaTxPkts_Object=MibTableColumn
apStaTxPkts=_ApStaTxPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,5,1,1,5),_ApStaTxPkts_Type())
apStaTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaTxPkts.setStatus(_A)
_ApStaTxBytes_Type=Counter32
_ApStaTxBytes_Object=MibTableColumn
apStaTxBytes=_ApStaTxBytes_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,5,1,1,6),_ApStaTxBytes_Type())
apStaTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaTxBytes.setStatus(_A)
_ApStaRxPkts_Type=Counter32
_ApStaRxPkts_Object=MibTableColumn
apStaRxPkts=_ApStaRxPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,5,1,1,7),_ApStaRxPkts_Type())
apStaRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaRxPkts.setStatus(_A)
_ApStaRxBytes_Type=Counter32
_ApStaRxBytes_Object=MibTableColumn
apStaRxBytes=_ApStaRxBytes_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,5,1,1,8),_ApStaRxBytes_Type())
apStaRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:apStaRxBytes.setStatus(_A)
_ApWAPIPeformanceStat_ObjectIdentity=ObjectIdentity
apWAPIPeformanceStat=_ApWAPIPeformanceStat_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,9,6))
_ApWAPIPfmStatTable_Object=MibTable
apWAPIPfmStatTable=_ApWAPIPfmStatTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,6,1))
if mibBuilder.loadTexts:apWAPIPfmStatTable.setStatus(_A)
_ApWAPIPfmStatEntry_Object=MibTableRow
apWAPIPfmStatEntry=_ApWAPIPfmStatEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,6,1,1))
apWAPIPfmStatEntry.setIndexNames((0,_D,_e))
if mibBuilder.loadTexts:apWAPIPfmStatEntry.setStatus(_A)
_ApSTAAddress_Type=MacAddress
_ApSTAAddress_Object=MibTableColumn
apSTAAddress=_ApSTAAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,6,1,1,1),_ApSTAAddress_Type())
apSTAAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:apSTAAddress.setStatus(_A)
_ApVersion_Type=Unsigned32
_ApVersion_Object=MibTableColumn
apVersion=_ApVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,6,1,1,2),_ApVersion_Type())
apVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:apVersion.setStatus(_A)
_ApControlledPortStatus_Type=TruthValue
_ApControlledPortStatus_Object=MibTableColumn
apControlledPortStatus=_ApControlledPortStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,6,1,1,3),_ApControlledPortStatus_Type())
apControlledPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:apControlledPortStatus.setStatus(_A)
_ApSelectedUnicastCipher_Type=OctetString
_ApSelectedUnicastCipher_Object=MibTableColumn
apSelectedUnicastCipher=_ApSelectedUnicastCipher_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,6,1,1,4),_ApSelectedUnicastCipher_Type())
apSelectedUnicastCipher.setMaxAccess(_B)
if mibBuilder.loadTexts:apSelectedUnicastCipher.setStatus(_A)
_ApWPIReplayCounters_Type=Counter32
_ApWPIReplayCounters_Object=MibTableColumn
apWPIReplayCounters=_ApWPIReplayCounters_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,6,1,1,5),_ApWPIReplayCounters_Type())
apWPIReplayCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:apWPIReplayCounters.setStatus(_A)
_ApWPIDecryptableErrors_Type=Counter32
_ApWPIDecryptableErrors_Object=MibTableColumn
apWPIDecryptableErrors=_ApWPIDecryptableErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,6,1,1,6),_ApWPIDecryptableErrors_Type())
apWPIDecryptableErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:apWPIDecryptableErrors.setStatus(_A)
_ApWPIMICErrors_Type=Counter32
_ApWPIMICErrors_Object=MibTableColumn
apWPIMICErrors=_ApWPIMICErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,6,1,1,7),_ApWPIMICErrors_Type())
apWPIMICErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:apWPIMICErrors.setStatus(_A)
_ApWAISignatureErrors_Type=Counter32
_ApWAISignatureErrors_Object=MibTableColumn
apWAISignatureErrors=_ApWAISignatureErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,6,1,1,8),_ApWAISignatureErrors_Type())
apWAISignatureErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAISignatureErrors.setStatus(_A)
_ApWAIHMACErrors_Type=Counter32
_ApWAIHMACErrors_Object=MibTableColumn
apWAIHMACErrors=_ApWAIHMACErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,6,1,1,9),_ApWAIHMACErrors_Type())
apWAIHMACErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAIHMACErrors.setStatus(_A)
_ApWAIAuthResultFailures_Type=Counter32
_ApWAIAuthResultFailures_Object=MibTableColumn
apWAIAuthResultFailures=_ApWAIAuthResultFailures_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,6,1,1,10),_ApWAIAuthResultFailures_Type())
apWAIAuthResultFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAIAuthResultFailures.setStatus(_A)
_ApWAIDiscardCounters_Type=Counter32
_ApWAIDiscardCounters_Object=MibTableColumn
apWAIDiscardCounters=_ApWAIDiscardCounters_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,6,1,1,11),_ApWAIDiscardCounters_Type())
apWAIDiscardCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAIDiscardCounters.setStatus(_A)
_ApWAITimeoutCounters_Type=Counter32
_ApWAITimeoutCounters_Object=MibTableColumn
apWAITimeoutCounters=_ApWAITimeoutCounters_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,6,1,1,12),_ApWAITimeoutCounters_Type())
apWAITimeoutCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAITimeoutCounters.setStatus(_A)
_ApWAIFormatErrors_Type=Counter32
_ApWAIFormatErrors_Object=MibTableColumn
apWAIFormatErrors=_ApWAIFormatErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,6,1,1,13),_ApWAIFormatErrors_Type())
apWAIFormatErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAIFormatErrors.setStatus(_A)
_ApWAICertificateHandshakeFailures_Type=Counter32
_ApWAICertificateHandshakeFailures_Object=MibTableColumn
apWAICertificateHandshakeFailures=_ApWAICertificateHandshakeFailures_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,6,1,1,14),_ApWAICertificateHandshakeFailures_Type())
apWAICertificateHandshakeFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAICertificateHandshakeFailures.setStatus(_A)
_ApWAIUnicastHandshakeFailures_Type=Counter32
_ApWAIUnicastHandshakeFailures_Object=MibTableColumn
apWAIUnicastHandshakeFailures=_ApWAIUnicastHandshakeFailures_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,6,1,1,15),_ApWAIUnicastHandshakeFailures_Type())
apWAIUnicastHandshakeFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAIUnicastHandshakeFailures.setStatus(_A)
_ApWAIMulticastHandshakeFailures_Type=Counter32
_ApWAIMulticastHandshakeFailures_Object=MibTableColumn
apWAIMulticastHandshakeFailures=_ApWAIMulticastHandshakeFailures_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,6,1,1,16),_ApWAIMulticastHandshakeFailures_Type())
apWAIMulticastHandshakeFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:apWAIMulticastHandshakeFailures.setStatus(_A)
_ApQOSPeformanceStat_ObjectIdentity=ObjectIdentity
apQOSPeformanceStat=_ApQOSPeformanceStat_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,80,9,7))
_ApQosBasePfmStatTable_Object=MibTable
apQosBasePfmStatTable=_ApQosBasePfmStatTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,1))
if mibBuilder.loadTexts:apQosBasePfmStatTable.setStatus(_A)
_ApQosBasePfmStatEntry_Object=MibTableRow
apQosBasePfmStatEntry=_ApQosBasePfmStatEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,1,1))
apQosBasePfmStatEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:apQosBasePfmStatEntry.setStatus(_A)
_ApQoSSvcQueAvgLen_Type=Integer32
_ApQoSSvcQueAvgLen_Object=MibTableColumn
apQoSSvcQueAvgLen=_ApQoSSvcQueAvgLen_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,1,1,1),_ApQoSSvcQueAvgLen_Type())
apQoSSvcQueAvgLen.setMaxAccess(_B)
if mibBuilder.loadTexts:apQoSSvcQueAvgLen.setStatus(_A)
_ApQoSSvcPktLossRatio_Type=Integer32
_ApQoSSvcPktLossRatio_Object=MibTableColumn
apQoSSvcPktLossRatio=_ApQoSSvcPktLossRatio_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,1,1,2),_ApQoSSvcPktLossRatio_Type())
apQoSSvcPktLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:apQoSSvcPktLossRatio.setStatus(_A)
_ApAvgTransSpeed_Type=Integer32
_ApAvgTransSpeed_Object=MibTableColumn
apAvgTransSpeed=_ApAvgTransSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,1,1,3),_ApAvgTransSpeed_Type())
apAvgTransSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:apAvgTransSpeed.setStatus(_A)
_ApBackgroundQosPfmStatTable_Object=MibTable
apBackgroundQosPfmStatTable=_ApBackgroundQosPfmStatTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,2))
if mibBuilder.loadTexts:apBackgroundQosPfmStatTable.setStatus(_A)
_ApBackgroundQosPfmStatEntry_Object=MibTableRow
apBackgroundQosPfmStatEntry=_ApBackgroundQosPfmStatEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,2,1))
apBackgroundQosPfmStatEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:apBackgroundQosPfmStatEntry.setStatus(_A)
_ApBgQueAvgLen_Type=Integer32
_ApBgQueAvgLen_Object=MibTableColumn
apBgQueAvgLen=_ApBgQueAvgLen_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,2,1,1),_ApBgQueAvgLen_Type())
apBgQueAvgLen.setMaxAccess(_B)
if mibBuilder.loadTexts:apBgQueAvgLen.setStatus(_A)
_ApBgAvgBurst_Type=Integer32
_ApBgAvgBurst_Object=MibTableColumn
apBgAvgBurst=_ApBgAvgBurst_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,2,1,2),_ApBgAvgBurst_Type())
apBgAvgBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:apBgAvgBurst.setStatus(_A)
_ApBgPktLossRatio_Type=Integer32
_ApBgPktLossRatio_Object=MibTableColumn
apBgPktLossRatio=_ApBgPktLossRatio_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,2,1,3),_ApBgPktLossRatio_Type())
apBgPktLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:apBgPktLossRatio.setStatus(_A)
_ApBgAvgTransSpeed_Type=Integer32
_ApBgAvgTransSpeed_Object=MibTableColumn
apBgAvgTransSpeed=_ApBgAvgTransSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,2,1,4),_ApBgAvgTransSpeed_Type())
apBgAvgTransSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:apBgAvgTransSpeed.setStatus(_A)
_ApBgSvcLoss_Type=Integer32
_ApBgSvcLoss_Object=MibTableColumn
apBgSvcLoss=_ApBgSvcLoss_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,2,1,5),_ApBgSvcLoss_Type())
apBgSvcLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:apBgSvcLoss.setStatus(_A)
_ApBestEffortQosPfmStatTable_Object=MibTable
apBestEffortQosPfmStatTable=_ApBestEffortQosPfmStatTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,3))
if mibBuilder.loadTexts:apBestEffortQosPfmStatTable.setStatus(_A)
_ApBestEffortQosPfmStatEntry_Object=MibTableRow
apBestEffortQosPfmStatEntry=_ApBestEffortQosPfmStatEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,3,1))
apBestEffortQosPfmStatEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:apBestEffortQosPfmStatEntry.setStatus(_A)
_ApBeQueAvgLen_Type=Integer32
_ApBeQueAvgLen_Object=MibTableColumn
apBeQueAvgLen=_ApBeQueAvgLen_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,3,1,1),_ApBeQueAvgLen_Type())
apBeQueAvgLen.setMaxAccess(_B)
if mibBuilder.loadTexts:apBeQueAvgLen.setStatus(_A)
_ApBeAvgBurst_Type=Integer32
_ApBeAvgBurst_Object=MibTableColumn
apBeAvgBurst=_ApBeAvgBurst_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,3,1,2),_ApBeAvgBurst_Type())
apBeAvgBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:apBeAvgBurst.setStatus(_A)
_ApBePktLossRatio_Type=Integer32
_ApBePktLossRatio_Object=MibTableColumn
apBePktLossRatio=_ApBePktLossRatio_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,3,1,3),_ApBePktLossRatio_Type())
apBePktLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:apBePktLossRatio.setStatus(_A)
_ApBeAvgTransSpeed_Type=Integer32
_ApBeAvgTransSpeed_Object=MibTableColumn
apBeAvgTransSpeed=_ApBeAvgTransSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,3,1,4),_ApBeAvgTransSpeed_Type())
apBeAvgTransSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:apBeAvgTransSpeed.setStatus(_A)
_ApBeSvcLoss_Type=Integer32
_ApBeSvcLoss_Object=MibTableColumn
apBeSvcLoss=_ApBeSvcLoss_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,3,1,5),_ApBeSvcLoss_Type())
apBeSvcLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:apBeSvcLoss.setStatus(_A)
_ApVoiceQosPfmStatTable_Object=MibTable
apVoiceQosPfmStatTable=_ApVoiceQosPfmStatTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,4))
if mibBuilder.loadTexts:apVoiceQosPfmStatTable.setStatus(_A)
_ApVoiceQosPfmStatEntry_Object=MibTableRow
apVoiceQosPfmStatEntry=_ApVoiceQosPfmStatEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,4,1))
apVoiceQosPfmStatEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:apVoiceQosPfmStatEntry.setStatus(_A)
_ApVoiceQueAvgLen_Type=Integer32
_ApVoiceQueAvgLen_Object=MibTableColumn
apVoiceQueAvgLen=_ApVoiceQueAvgLen_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,4,1,1),_ApVoiceQueAvgLen_Type())
apVoiceQueAvgLen.setMaxAccess(_B)
if mibBuilder.loadTexts:apVoiceQueAvgLen.setStatus(_A)
_ApVoiceAvgBurst_Type=Integer32
_ApVoiceAvgBurst_Object=MibTableColumn
apVoiceAvgBurst=_ApVoiceAvgBurst_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,4,1,2),_ApVoiceAvgBurst_Type())
apVoiceAvgBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:apVoiceAvgBurst.setStatus(_A)
_ApVoicePktLossRatio_Type=Integer32
_ApVoicePktLossRatio_Object=MibTableColumn
apVoicePktLossRatio=_ApVoicePktLossRatio_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,4,1,3),_ApVoicePktLossRatio_Type())
apVoicePktLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:apVoicePktLossRatio.setStatus(_A)
_ApVoiceAvgTransSpeed_Type=Integer32
_ApVoiceAvgTransSpeed_Object=MibTableColumn
apVoiceAvgTransSpeed=_ApVoiceAvgTransSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,4,1,4),_ApVoiceAvgTransSpeed_Type())
apVoiceAvgTransSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:apVoiceAvgTransSpeed.setStatus(_A)
_ApVoicePutThroughRatio_Type=Integer32
_ApVoicePutThroughRatio_Object=MibTableColumn
apVoicePutThroughRatio=_ApVoicePutThroughRatio_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,4,1,5),_ApVoicePutThroughRatio_Type())
apVoicePutThroughRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:apVoicePutThroughRatio.setStatus(_A)
_ApVoiceDropRatio_Type=Integer32
_ApVoiceDropRatio_Object=MibTableColumn
apVoiceDropRatio=_ApVoiceDropRatio_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,4,1,6),_ApVoiceDropRatio_Type())
apVoiceDropRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:apVoiceDropRatio.setStatus(_A)
_ApVoiceSvcLoss_Type=Integer32
_ApVoiceSvcLoss_Object=MibTableColumn
apVoiceSvcLoss=_ApVoiceSvcLoss_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,4,1,7),_ApVoiceSvcLoss_Type())
apVoiceSvcLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:apVoiceSvcLoss.setStatus(_A)
_ApVoiceExceedMaxUsersRequest_Type=Integer32
_ApVoiceExceedMaxUsersRequest_Object=MibTableColumn
apVoiceExceedMaxUsersRequest=_ApVoiceExceedMaxUsersRequest_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,4,1,8),_ApVoiceExceedMaxUsersRequest_Type())
apVoiceExceedMaxUsersRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:apVoiceExceedMaxUsersRequest.setStatus(_A)
_ApVedioQosPfmStatTable_Object=MibTable
apVedioQosPfmStatTable=_ApVedioQosPfmStatTable_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,5))
if mibBuilder.loadTexts:apVedioQosPfmStatTable.setStatus(_A)
_ApVedioQosPfmStatEntry_Object=MibTableRow
apVedioQosPfmStatEntry=_ApVedioQosPfmStatEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,5,1))
apVedioQosPfmStatEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:apVedioQosPfmStatEntry.setStatus(_A)
_ApVedioQueAvgLen_Type=Integer32
_ApVedioQueAvgLen_Object=MibTableColumn
apVedioQueAvgLen=_ApVedioQueAvgLen_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,5,1,1),_ApVedioQueAvgLen_Type())
apVedioQueAvgLen.setMaxAccess(_B)
if mibBuilder.loadTexts:apVedioQueAvgLen.setStatus(_A)
_ApVedioAvgBurst_Type=Integer32
_ApVedioAvgBurst_Object=MibTableColumn
apVedioAvgBurst=_ApVedioAvgBurst_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,5,1,2),_ApVedioAvgBurst_Type())
apVedioAvgBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:apVedioAvgBurst.setStatus(_A)
_ApVedioPktLossRatio_Type=Integer32
_ApVedioPktLossRatio_Object=MibTableColumn
apVedioPktLossRatio=_ApVedioPktLossRatio_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,5,1,3),_ApVedioPktLossRatio_Type())
apVedioPktLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:apVedioPktLossRatio.setStatus(_A)
_ApVedioAvgTransSpeed_Type=Integer32
_ApVedioAvgTransSpeed_Object=MibTableColumn
apVedioAvgTransSpeed=_ApVedioAvgTransSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,5,1,4),_ApVedioAvgTransSpeed_Type())
apVedioAvgTransSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:apVedioAvgTransSpeed.setStatus(_A)
_ApVedioPutThroughRatio_Type=Integer32
_ApVedioPutThroughRatio_Object=MibTableColumn
apVedioPutThroughRatio=_ApVedioPutThroughRatio_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,5,1,5),_ApVedioPutThroughRatio_Type())
apVedioPutThroughRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:apVedioPutThroughRatio.setStatus(_A)
_ApVedioDropRatio_Type=Integer32
_ApVedioDropRatio_Object=MibTableColumn
apVedioDropRatio=_ApVedioDropRatio_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,5,1,6),_ApVedioDropRatio_Type())
apVedioDropRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:apVedioDropRatio.setStatus(_A)
_ApVedioSvcLoss_Type=Integer32
_ApVedioSvcLoss_Object=MibTableColumn
apVedioSvcLoss=_ApVedioSvcLoss_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,5,1,7),_ApVedioSvcLoss_Type())
apVedioSvcLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:apVedioSvcLoss.setStatus(_A)
_ApVedioExceedMaxUsersRequest_Type=Integer32
_ApVedioExceedMaxUsersRequest_Object=MibTableColumn
apVedioExceedMaxUsersRequest=_ApVedioExceedMaxUsersRequest_Object((1,3,6,1,4,1,27514,1,1,10,2,80,9,7,5,1,8),_ApVedioExceedMaxUsersRequest_Type())
apVedioExceedMaxUsersRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:apVedioExceedMaxUsersRequest.setStatus(_A)
apConfigurationErrorTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,0,1))
if mibBuilder.loadTexts:apConfigurationErrorTrap.setStatus(_A)
apCPUusageTooHighTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,0,2))
if mibBuilder.loadTexts:apCPUusageTooHighTrap.setStatus(_A)
apCPUusageTooHighRecovTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,0,3))
if mibBuilder.loadTexts:apCPUusageTooHighRecovTrap.setStatus(_A)
apMemUsageTooHighTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,0,4))
if mibBuilder.loadTexts:apMemUsageTooHighTrap.setStatus(_A)
apMemUsageTooHighRecovTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,0,5))
if mibBuilder.loadTexts:apMemUsageTooHighRecovTrap.setStatus(_A)
apSystmColdStartTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,0,6))
if mibBuilder.loadTexts:apSystmColdStartTrap.setStatus(_A)
apIPAddrChangeTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,0,7))
apIPAddrChangeTrap.setObjects(*((_D,_f),(_D,_g)))
if mibBuilder.loadTexts:apIPAddrChangeTrap.setStatus(_A)
apAPMtWorkModeChgTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,0,8))
if mibBuilder.loadTexts:apAPMtWorkModeChgTrap.setStatus(_A)
apAPSWUpdateFailTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,0,9))
if mibBuilder.loadTexts:apAPSWUpdateFailTrap.setStatus(_A)
apSSIDkeyConflictTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,0,10))
apSSIDkeyConflictTrap.setObjects(*((_D,_h),(_D,_F),(_D,_i),(_D,_j),(_D,_k)))
if mibBuilder.loadTexts:apSSIDkeyConflictTrap.setStatus(_A)
apFatAPHeartbeatTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,0,11))
apFatAPHeartbeatTrap.setObjects(*((_D,_l),(_D,_m)))
if mibBuilder.loadTexts:apFatAPHeartbeatTrap.setStatus(_A)
apAPCoInterfDetectedTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,2,1))
apAPCoInterfDetectedTrap.setObjects(*((_D,_F),(_D,_J),(_D,_O)))
if mibBuilder.loadTexts:apAPCoInterfDetectedTrap.setStatus(_A)
apAPCoInterfClearTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,2,2))
apAPCoInterfClearTrap.setObjects(*((_D,_F),(_D,_J),(_D,_O)))
if mibBuilder.loadTexts:apAPCoInterfClearTrap.setStatus(_A)
apAPNerborInterfDetectedTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,2,3))
apAPNerborInterfDetectedTrap.setObjects(*((_D,_F),(_D,_J),(_D,_O),(_D,_R)))
if mibBuilder.loadTexts:apAPNerborInterfDetectedTrap.setStatus(_A)
apAPNeiborInterfClearTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,2,4))
apAPNeiborInterfClearTrap.setObjects(*((_D,_F),(_D,_J),(_D,_O),(_D,_R)))
if mibBuilder.loadTexts:apAPNeiborInterfClearTrap.setStatus(_A)
apStaInterfDetectedTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,2,5))
apStaInterfDetectedTrap.setObjects(*((_D,_F),(_D,_J),(_D,_S)))
if mibBuilder.loadTexts:apStaInterfDetectedTrap.setStatus(_A)
apStaInterfClearTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,2,6))
apStaInterfClearTrap.setObjects(*((_D,_F),(_D,_J),(_D,_S)))
if mibBuilder.loadTexts:apStaInterfClearTrap.setStatus(_A)
apOtherDeviceInterfDetectedTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,2,7))
apOtherDeviceInterfDetectedTrap.setObjects(*((_D,_F),(_D,_J)))
if mibBuilder.loadTexts:apOtherDeviceInterfDetectedTrap.setStatus(_A)
apOtherDevInterfClearTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,2,8))
apOtherDevInterfClearTrap.setObjects(*((_D,_F),(_D,_J)))
if mibBuilder.loadTexts:apOtherDevInterfClearTrap.setStatus(_A)
apRadioDownTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,2,9))
apRadioDownTrap.setObjects(*((_D,_F),(_D,_T)))
if mibBuilder.loadTexts:apRadioDownTrap.setStatus(_A)
apRadioDownRecovTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,2,10))
apRadioDownRecovTrap.setObjects(*((_D,_F),(_D,_T)))
if mibBuilder.loadTexts:apRadioDownRecovTrap.setStatus(_A)
apAPStaFullTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,2,11))
apAPStaFullTrap.setObjects(*((_D,_U),(_D,_P)))
if mibBuilder.loadTexts:apAPStaFullTrap.setStatus(_A)
apAPStaFullRecoverTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,2,12))
apAPStaFullRecoverTrap.setObjects(*((_D,_U),(_D,_P)))
if mibBuilder.loadTexts:apAPStaFullRecoverTrap.setStatus(_A)
apAPMtRdoChanlChgTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,2,13))
apAPMtRdoChanlChgTrap.setObjects(*((_D,_F),(_D,_n),(_D,_o),(_D,_p)))
if mibBuilder.loadTexts:apAPMtRdoChanlChgTrap.setStatus(_A)
apStaAuthErrorTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,4,1))
apStaAuthErrorTrap.setObjects(*((_D,_F),(_D,_K),(_D,_L),(_D,_M),(_D,_q),(_D,_r)))
if mibBuilder.loadTexts:apStaAuthErrorTrap.setStatus(_A)
apStAssociationFailTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,4,2))
apStAssociationFailTrap.setObjects(*((_D,_F),(_D,_K),(_D,_L),(_D,_M),(_D,_P)))
if mibBuilder.loadTexts:apStAssociationFailTrap.setStatus(_A)
apRadiusAuthServerUnavailableTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,6,1))
if mibBuilder.loadTexts:apRadiusAuthServerUnavailableTrap.setStatus(_A)
apRadiusAuthServerAvailableTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,6,2))
if mibBuilder.loadTexts:apRadiusAuthServerAvailableTrap.setStatus(_A)
apRadioAccServerUnavailableTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,6,3))
if mibBuilder.loadTexts:apRadioAccServerUnavailableTrap.setStatus(_A)
apRadiusAccServerAvailableTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,6,4))
if mibBuilder.loadTexts:apRadiusAccServerAvailableTrap.setStatus(_A)
apUserWithInvalidCerficationInbreakNetworkTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,7,1))
apUserWithInvalidCerficationInbreakNetworkTrap.setObjects(*((_D,_F),(_D,_K),(_D,_L),(_D,_M)))
if mibBuilder.loadTexts:apUserWithInvalidCerficationInbreakNetworkTrap.setStatus(_A)
apStationRepititiveAttackTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,7,2))
apStationRepititiveAttackTrap.setObjects(*((_D,_F),(_D,_K),(_D,_L),(_D,_M)))
if mibBuilder.loadTexts:apStationRepititiveAttackTrap.setStatus(_A)
apTamperAttackTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,7,3))
apTamperAttackTrap.setObjects(*((_D,_F),(_D,_K),(_D,_L),(_D,_M)))
if mibBuilder.loadTexts:apTamperAttackTrap.setStatus(_A)
apLowSafeLevelAttackTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,7,4))
apLowSafeLevelAttackTrap.setObjects(*((_D,_F),(_D,_K),(_D,_L),(_D,_M)))
if mibBuilder.loadTexts:apLowSafeLevelAttackTrap.setStatus(_A)
apAddressRedirectionAttackTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,80,7,5))
apAddressRedirectionAttackTrap.setObjects(*((_D,_F),(_D,_K),(_D,_L),(_D,_M)))
if mibBuilder.loadTexts:apAddressRedirectionAttackTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'apStandardmibmodule':apStandardmibmodule,'apStandardSysTraps':apStandardSysTraps,'apConfigurationErrorTrap':apConfigurationErrorTrap,'apCPUusageTooHighTrap':apCPUusageTooHighTrap,'apCPUusageTooHighRecovTrap':apCPUusageTooHighRecovTrap,'apMemUsageTooHighTrap':apMemUsageTooHighTrap,'apMemUsageTooHighRecovTrap':apMemUsageTooHighRecovTrap,'apSystmColdStartTrap':apSystmColdStartTrap,'apIPAddrChangeTrap':apIPAddrChangeTrap,'apAPMtWorkModeChgTrap':apAPMtWorkModeChgTrap,'apAPSWUpdateFailTrap':apAPSWUpdateFailTrap,'apSSIDkeyConflictTrap':apSSIDkeyConflictTrap,'apFatAPHeartbeatTrap':apFatAPHeartbeatTrap,'apStandardSysTrapsObjects':apStandardSysTrapsObjects,_f:apOriginalIpAddr,_g:apCurrentIpAddr,_l:apIpAddr,_m:apTimeStamp,_h:apAPMac,_i:apSSIDKey,_j:apSSIDKeyConflict,_k:apCyperIndex,'apStandardRadioTraps':apStandardRadioTraps,'apAPCoInterfDetectedTrap':apAPCoInterfDetectedTrap,'apAPCoInterfClearTrap':apAPCoInterfClearTrap,'apAPNerborInterfDetectedTrap':apAPNerborInterfDetectedTrap,'apAPNeiborInterfClearTrap':apAPNeiborInterfClearTrap,'apStaInterfDetectedTrap':apStaInterfDetectedTrap,'apStaInterfClearTrap':apStaInterfClearTrap,'apOtherDeviceInterfDetectedTrap':apOtherDeviceInterfDetectedTrap,'apOtherDevInterfClearTrap':apOtherDevInterfClearTrap,'apRadioDownTrap':apRadioDownTrap,'apRadioDownRecovTrap':apRadioDownRecovTrap,'apAPStaFullTrap':apAPStaFullTrap,'apAPStaFullRecoverTrap':apAPStaFullRecoverTrap,'apAPMtRdoChanlChgTrap':apAPMtRdoChanlChgTrap,'apStandardRadioTrapsObjects':apStandardRadioTrapsObjects,_T:apInterruptReason,_F:apWorkingAPRadioIfInfo,_J:apWorkingAPChannel,_R:apInterfAPChannel,_O:apInterfAPBSSID,_S:apInterfStaMac,_U:apPermitAssoUser,_P:apAssoFailReason,_n:apChannelBeforeChange,_o:apChannelAfterChange,_p:apChanChangeMode,'apStandardTerminalTraps':apStandardTerminalTraps,'apStaAuthErrorTrap':apStaAuthErrorTrap,'apStAssociationFailTrap':apStAssociationFailTrap,'apStandardTerminalTrapsObjects':apStandardTerminalTrapsObjects,_K:apWorkingAPBSSID,_L:apWorkingAPSSID,_M:apStaMacAddr,_q:apAuthMode,_r:apAuthFailReason,'apStandardAuthSvrTraps':apStandardAuthSvrTraps,'apRadiusAuthServerUnavailableTrap':apRadiusAuthServerUnavailableTrap,'apRadiusAuthServerAvailableTrap':apRadiusAuthServerAvailableTrap,'apRadioAccServerUnavailableTrap':apRadioAccServerUnavailableTrap,'apRadiusAccServerAvailableTrap':apRadiusAccServerAvailableTrap,'apStandardWapiScrTraps':apStandardWapiScrTraps,'apUserWithInvalidCerficationInbreakNetworkTrap':apUserWithInvalidCerficationInbreakNetworkTrap,'apStationRepititiveAttackTrap':apStationRepititiveAttackTrap,'apTamperAttackTrap':apTamperAttackTrap,'apLowSafeLevelAttackTrap':apLowSafeLevelAttackTrap,'apAddressRedirectionAttackTrap':apAddressRedirectionAttackTrap,'apConfigInfoObjects':apConfigInfoObjects,'apSysInfoObjects':apSysInfoObjects,'apSysNetID':apSysNetID,'apSysHostName':apSysHostName,'apSysDescr':apSysDescr,'apManufacturer':apManufacturer,'apSerialNumber':apSerialNumber,'apSysModel':apSysModel,'apSysTime':apSysTime,'apSysUpTime':apSysUpTime,'apSysIPAddress':apSysIPAddress,'apSysIPNetMask':apSysIPNetMask,'apSysGWAddr':apSysGWAddr,'apPrimDNSServerIPAdd':apPrimDNSServerIPAdd,'apSeconDNSServerIPAdd':apSeconDNSServerIPAdd,'apSysMacAddress':apSysMacAddress,'apReadCommunityName':apReadCommunityName,'apWriteCommunityName':apWriteCommunityName,'apStatWindowTime':apStatWindowTime,'apSampleTime':apSampleTime,'apSysRestart':apSysRestart,'apSysReset':apSysReset,'apSoftwareName':apSoftwareName,'apSoftwareVersion':apSoftwareVersion,'apSoftwareVendor':apSoftwareVendor,'apCPUType':apCPUType,'apMemoryType':apMemoryType,'apMemorySize':apMemorySize,'apFlashSize':apFlashSize,'apPhyInterfaceConfig':apPhyInterfaceConfig,'apIfNumber':apIfNumber,'apWiredInterfaceCfgTable':apWiredInterfaceCfgTable,'apWiredInterfaceCfgEntry':apWiredInterfaceCfgEntry,'apIfDescr':apIfDescr,'apIfType':apIfType,'apIfMTU':apIfMTU,'apIfSpeed':apIfSpeed,'apIfPhysAddress':apIfPhysAddress,'apIfAdminStatus':apIfAdminStatus,'apIfOperStatus':apIfOperStatus,'apIfLastChange':apIfLastChange,'apRadioInterfaceCfg':apRadioInterfaceCfg,'apRadioInterfaceInfoTable':apRadioInterfaceInfoTable,'apRadioInterfaceInfoEntry':apRadioInterfaceInfoEntry,'apRadioIfDescr':apRadioIfDescr,'apRadioIfType':apRadioIfType,'apRadioIfMTU':apRadioIfMTU,'apRadioIfSpeed':apRadioIfSpeed,'apRadioIfMacAddress':apRadioIfMacAddress,'apRadioIfDiversity':apRadioIfDiversity,'apRadioIfAdminStatus':apRadioIfAdminStatus,'apRadioIfOperStatus':apRadioIfOperStatus,'apRadioIfLastChange':apRadioIfLastChange,'apRadioChannelAutoSelectEnable':apRadioChannelAutoSelectEnable,'apRadioChannelConfig':apRadioChannelConfig,'apRadioChannelUsing':apRadioChannelUsing,'apCurrRadioModeSupport':apCurrRadioModeSupport,'apRadioModeConfig':apRadioModeConfig,'apTransmitSpeedConfig':apTransmitSpeedConfig,'apMaxTxPwrLvl':apMaxTxPwrLvl,'apTxPwr':apTxPwr,'apPwrAttRange':apPwrAttRange,'apPwrAttValue':apPwrAttValue,'apAntennaGain':apAntennaGain,'apPowerMgmtEnable':apPowerMgmtEnable,'apMaxStationNumPermitted':apMaxStationNumPermitted,'apAMPDUEnabled':apAMPDUEnabled,'apBWMode':apBWMode,'apShortGIEnabled':apShortGIEnabled,'apIs11nOnly':apIs11nOnly,'apRadioInterfacePhyParaTable':apRadioInterfacePhyParaTable,'apRadioInterfacePhyParaEntry':apRadioInterfacePhyParaEntry,'apBeaconIntvl':apBeaconIntvl,'apDtimIntvl':apDtimIntvl,'apRtsThreshold':apRtsThreshold,'apFragThreshlod':apFragThreshlod,'apPreambleLen':apPreambleLen,'apSSIDCfg':apSSIDCfg,'apConfigBSSIDNum':apConfigBSSIDNum,'apRadioIfSSIDCfgTable':apRadioIfSSIDCfgTable,'apRadioIfSSIDCfgEntry':apRadioIfSSIDCfgEntry,'apBSSID':apBSSID,'apSSIDCfgTable':apSSIDCfgTable,'apSSIDCfgEntry':apSSIDCfgEntry,_I:apWlanId,'apSSIDName':apSSIDName,'apSSIDEnabled':apSSIDEnabled,'apSSIDHidden':apSSIDHidden,'apStaIsolate':apStaIsolate,'apDot11Auth':apDot11Auth,'apSecurity':apSecurity,'apAuthenMode':apAuthenMode,'apSecurityCiphers':apSecurityCiphers,'apVlanId':apVlanId,'apMaxSimultUsers':apMaxSimultUsers,'apStaUplinkMaxRate':apStaUplinkMaxRate,'apStaDwlinkMaxRate':apStaDwlinkMaxRate,'apSSIDCfgStatus':apSSIDCfgStatus,'apSecurityCfg':apSecurityCfg,'apSecurityCfgTable':apSecurityCfgTable,'apSecurityCfgEntry':apSecurityCfgEntry,'apWEPCipherKeyIndex':apWEPCipherKeyIndex,'apWEPCipherKeyValue':apWEPCipherKeyValue,'apWEPCipherKeyCharType':apWEPCipherKeyCharType,'apPSKCipherKeyValue':apPSKCipherKeyValue,'apPSKCipherKeyCharType':apPSKCipherKeyCharType,'apWAPIASIPAddress':apWAPIASIPAddress,'apWAPIIsInstalledCer':apWAPIIsInstalledCer,'apTerminalCfg':apTerminalCfg,'apTerminalInfoTable':apTerminalInfoTable,'apTerminalInfoEntry':apTerminalInfoEntry,_W:apStaMAC,'apStaWMMAttr':apStaWMMAttr,'apStaIPAddress':apStaIPAddress,'apStaRadioMode':apStaRadioMode,'apStaRadioChannel':apStaRadioChannel,'apStaTxRates':apStaTxRates,'apStaPowerSaveMode':apStaPowerSaveMode,'apStaVlanId':apStaVlanId,'apStaSSIDName':apStaSSIDName,'apStaDot11Auth':apStaDot11Auth,'apStaSecurity':apStaSecurity,'apStaAuthenMode':apStaAuthenMode,'apStaSecurityCiphers':apStaSecurityCiphers,'apQosCfg':apQosCfg,'apQosRadioIfCfgTable':apQosRadioIfCfgTable,'apQosRadioIfCfgEntry':apQosRadioIfCfgEntry,_X:apQoSTrafficClassIndex,'apQosAIFS':apQosAIFS,'apQoSCWmin':apQoSCWmin,'apQoSCWmax':apQoSCWmax,'apQoSTXOPLim':apQoSTXOPLim,'apQosBaseCfgTable':apQosBaseCfgTable,'apQosBaseCfgEntry':apQosBaseCfgEntry,'apQoSBaseTrafficClass':apQoSBaseTrafficClass,'apQoSEnabled':apQoSEnabled,'apQoSBW':apQoSBW,'apQoSResPercent':apQoSResPercent,'apQoSsharedBW':apQoSsharedBW,'apQoSsharedBWPercent':apQoSsharedBWPercent,'apSchedAlgName':apSchedAlgName,'apResPolicyEnabled':apResPolicyEnabled,'apResPolicyName':apResPolicyName,'apBackgroundSvcAvgSpeed':apBackgroundSvcAvgSpeed,'apBackgroundSvcMaxBurst':apBackgroundSvcMaxBurst,'apBackgroundSvcPriority':apBackgroundSvcPriority,'apBackgroundSvcResPriority':apBackgroundSvcResPriority,'apBestEffortSvcAvgSpeed':apBestEffortSvcAvgSpeed,'apBestEffortSvcMaxBurst':apBestEffortSvcMaxBurst,'apBestEffortSvcPriority':apBestEffortSvcPriority,'apBestEffortSvcResPriority':apBestEffortSvcResPriority,'apVoiceSvcAvgSpeed':apVoiceSvcAvgSpeed,'apVoiceSvcMaxBurst':apVoiceSvcMaxBurst,'apVoiceSvcPriority':apVoiceSvcPriority,'apVoiceSvcResPriority':apVoiceSvcResPriority,'apVideoSvcAvgSpeed':apVideoSvcAvgSpeed,'apVideoSvcMaxBurst':apVideoSvcMaxBurst,'apVideoSvcPriority':apVideoSvcPriority,'apVideoSvcResPriority':apVideoSvcResPriority,'apQosBackgroundCfgTable':apQosBackgroundCfgTable,'apQosBackgroundCfgEntry':apQosBackgroundCfgEntry,'apBgMaxSvcCnt':apBgMaxSvcCnt,'apBgSvcBW':apBgSvcBW,'apBgSvcBWPercent':apBgSvcBWPercent,'apBgIsUseWREDAlg':apBgIsUseWREDAlg,'apBgIsUseTrafficShaping':apBgIsUseTrafficShaping,'apQosBestEffortCfgTable':apQosBestEffortCfgTable,'apQosBestEffortCfgEntry':apQosBestEffortCfgEntry,'apBeMaxSvcCnt':apBeMaxSvcCnt,'apBeSvcBW':apBeSvcBW,'apBeSvcBWPercent':apBeSvcBWPercent,'apBeIsUseWREDAlg':apBeIsUseWREDAlg,'apBeIsUseTrafficShaping':apBeIsUseTrafficShaping,'apQosVoiceCfgTable':apQosVoiceCfgTable,'apQosVoiceCfgEntry':apQosVoiceCfgEntry,'apVoiceMaxSvcCnt':apVoiceMaxSvcCnt,'apVoiceSvcBW':apVoiceSvcBW,'apVoiceSvcBWPercent':apVoiceSvcBWPercent,'apVoiceIsUseStreamBasedQueue':apVoiceIsUseStreamBasedQueue,'apVoiceStreamMaxQueueLen':apVoiceStreamMaxQueueLen,'apVoiceStreamAvgSpeed':apVoiceStreamAvgSpeed,'apVoiceStreamMaxBurst':apVoiceStreamMaxBurst,'apVoiceIsUseWREDAlg':apVoiceIsUseWREDAlg,'apVoiceIsUseTrafficShaping':apVoiceIsUseTrafficShaping,'apQosVedioCfgTable':apQosVedioCfgTable,'apQosVedioCfgEntry':apQosVedioCfgEntry,'apVedioMaxSvcCnt':apVedioMaxSvcCnt,'apVedioSvcBW':apVedioSvcBW,'apVedioSvcBWPercent':apVedioSvcBWPercent,'apVedioIsUseStreamBasedQueue':apVedioIsUseStreamBasedQueue,'apVedioStreamMaxQueueLen':apVedioStreamMaxQueueLen,'apVedioStreamAvgSpeed':apVedioStreamAvgSpeed,'apVedioStreamMaxBurst':apVedioStreamMaxBurst,'apVedioIsUseWREDAlg':apVedioIsUseWREDAlg,'apVedioIsUseTrafficShaping':apVedioIsUseTrafficShaping,'apWapiCfg':apWapiCfg,'apWapiProtocolCfgTable':apWapiProtocolCfgTable,'apWapiProtocolCfgEntry':apWapiProtocolCfgEntry,'apConfigVersion':apConfigVersion,'apControlledAuthControl':apControlledAuthControl,'apControlledPortControl':apControlledPortControl,'apWapiOptionImplemented':apWapiOptionImplemented,'apWapiPreauthImplemented':apWapiPreauthImplemented,'apWapiEnabled':apWapiEnabled,'apWapiPreauthEnabled':apWapiPreauthEnabled,'apUnicastKeysSupported':apUnicastKeysSupported,'apUnicastRekeyMethod':apUnicastRekeyMethod,'apUnicastRekeyTime':apUnicastRekeyTime,'apUnicastRekeyPackets':apUnicastRekeyPackets,'apMulticastCipher':apMulticastCipher,'apMulticastRekeyMethod':apMulticastRekeyMethod,'apMulticastRekeyTime':apMulticastRekeyTime,'apMulticastRekeyPackets':apMulticastRekeyPackets,'apMulticastRekeyStrict':apMulticastRekeyStrict,'apPSKValue':apPSKValue,'apPSKPassPhrase':apPSKPassPhrase,'apCertificateUpdateCount':apCertificateUpdateCount,'apMulticastUpdateCount':apMulticastUpdateCount,'apUnicastUpdateCount':apUnicastUpdateCount,'apMulticastCipherSize':apMulticastCipherSize,'apBKLifetime':apBKLifetime,'apBKReauthThreshold':apBKReauthThreshold,'apSATimeout':apSATimeout,'apAuthSuiteSelected':apAuthSuiteSelected,'apUnicastCipherSelected':apUnicastCipherSelected,'apMulticastCipherSelected':apMulticastCipherSelected,'apBKIDUsed':apBKIDUsed,'apAuthSuiteRequested':apAuthSuiteRequested,'apUnicastCipherRequested':apUnicastCipherRequested,'apMulticastCipherRequested':apMulticastCipherRequested,'apWapiUnicastCfgTable':apWapiUnicastCfgTable,'apWapiUnicastCfgEntry':apWapiUnicastCfgEntry,'apUnicastCipher':apUnicastCipher,'apUnicastCipherEnabled':apUnicastCipherEnabled,'apUnicastCipherSize':apUnicastCipherSize,'apWapiAKMCfgTable':apWapiAKMCfgTable,'apWapiAKMCfgEntry':apWapiAKMCfgEntry,'apAuthenticationSuite':apAuthenticationSuite,'apAuthenticationSuiteEnabled':apAuthenticationSuiteEnabled,'apSyslogCfg':apSyslogCfg,'apSyslogSvcEnable':apSyslogSvcEnable,'apSyslogReportEventLevel':apSyslogReportEventLevel,'apSyslogSvrCfgTable':apSyslogSvrCfgTable,'apSyslogSvrCfgEntry':apSyslogSvrCfgEntry,_Y:apSyslogSvrIndex,'apSyslogServerAddr':apSyslogServerAddr,'apSyslogStatus':apSyslogStatus,'apSoftwareUpdate':apSoftwareUpdate,'apLoadFlag':apLoadFlag,'apFileName':apFileName,'apFileType':apFileType,'apTransProtocol':apTransProtocol,'apServerAddr':apServerAddr,'apServerPort':apServerPort,'apServerUsername':apServerUsername,'apServerPasswd':apServerPasswd,'apTransStatus':apTransStatus,'apFailReason':apFailReason,'apCfgFileDistribute':apCfgFileDistribute,'apCfgFileLoadFlag':apCfgFileLoadFlag,'apCfgFileFileName':apCfgFileFileName,'apCfgFileFileType':apCfgFileFileType,'apCfgFileTransProtocol':apCfgFileTransProtocol,'apCfgFileServerAddr':apCfgFileServerAddr,'apCfgFileServerPort':apCfgFileServerPort,'apCfgFileServerUsername':apCfgFileServerUsername,'apCfgFileServerPasswd':apCfgFileServerPasswd,'apCfgFileTransStatus':apCfgFileTransStatus,'apCfgFileFailReason':apCfgFileFailReason,'apAccessControl':apAccessControl,'apTerminalPermitTable':apTerminalPermitTable,'apTerminalPermitEntry':apTerminalPermitEntry,_Z:apWhiteListIndex,'apPermitMAC':apPermitMAC,'apWhiteListStatus':apWhiteListStatus,'apTerminalDeniedTable':apTerminalDeniedTable,'apTerminalDeniedEntry':apTerminalDeniedEntry,_a:apBlackListIndex,'apAttackDeviceMAC':apAttackDeviceMAC,'apBlackListStatus':apBlackListStatus,'apTrapConfig':apTrapConfig,'apTrapResendWaitingTime':apTrapResendWaitingTime,'apCPUusageThreshhd':apCPUusageThreshhd,'apMemUsageThreshhd':apMemUsageThreshhd,'apAPCoInterfThreshhd':apAPCoInterfThreshhd,'apAPNeiborInterfThreshhd':apAPNeiborInterfThreshhd,'apStaInterfNumThreshhd':apStaInterfNumThreshhd,'apHeartbeatOnOff':apHeartbeatOnOff,'apHeartbeatPeriod':apHeartbeatPeriod,'apTrapAddrTable':apTrapAddrTable,'apTrapAddrEntry':apTrapAddrEntry,_b:apTrapDesAddrIndex,'apTrapDesIPAddress':apTrapDesIPAddress,'apTrapAddrStatus':apTrapAddrStatus,'apTrapEnabledTable':apTrapEnabledTable,'apTrapEnabledEntry':apTrapEnabledEntry,_c:apTrapEnabledIndex,'apTrapName':apTrapName,'apTrapDescr':apTrapDescr,'apTrapOnOff':apTrapOnOff,'apVlanConfig':apVlanConfig,'apVlanConfigTable':apVlanConfigTable,'apVlanConfigEntry':apVlanConfigEntry,'apVlanCfgVlanId':apVlanCfgVlanId,'apVlanCfgStatus':apVlanCfgStatus,'apHeartbeatConfig':apHeartbeatConfig,'apHeartbeatCycle':apHeartbeatCycle,'apPerformanceStatObjects':apPerformanceStatObjects,'apSysPerformanceStat':apSysPerformanceStat,'apCPURTUsage':apCPURTUsage,'apCPUAvgUsage':apCPUAvgUsage,'apMemRTUsage':apMemRTUsage,'apMemAvgUsage':apMemAvgUsage,'apConInfoStat':apConInfoStat,'apApStationAssocSum':apApStationAssocSum,'apApStationOnlineSum':apApStationOnlineSum,'apAssocTimes':apAssocTimes,'apAssocFailTimes':apAssocFailTimes,'apReassocTimes':apReassocTimes,'apPreAssCannotShiftDeassocFailSum':apPreAssCannotShiftDeassocFailSum,'apApStatsDisassociated':apApStatsDisassociated,'apAssocRejectSum':apAssocRejectSum,'apBSSNotSupportAssocFailSum':apBSSNotSupportAssocFailSum,'apIfPeformanceStat':apIfPeformanceStat,'apWiredIfPfmStatTable':apWiredIfPfmStatTable,'apWiredIfPfmStatEntry':apWiredIfPfmStatEntry,'apIfInUcastPkts':apIfInUcastPkts,'apIfInNUcastPkts':apIfInNUcastPkts,'apIfInOctets':apIfInOctets,'apIfInDiscardPkts':apIfInDiscardPkts,'apIfInErrors':apIfInErrors,'apIfOutUcastPkts':apIfOutUcastPkts,'apIfOutNUcastPkts':apIfOutNUcastPkts,'apIfOutOctets':apIfOutOctets,'apIfOutDiscardPkts':apIfOutDiscardPkts,'apIfOutErrors':apIfOutErrors,'apIfUpDwnTimes':apIfUpDwnTimes,'apRadioIfPfmStatTable':apRadioIfPfmStatTable,'apRadioIfPfmStatEntry':apRadioIfPfmStatEntry,'apAvgRxSignalStrength':apAvgRxSignalStrength,'apHighestRxSignalStrength':apHighestRxSignalStrength,'apLowestRxSignalStrength':apLowestRxSignalStrength,'apUpdownTimes':apUpdownTimes,'apTxDataPkts':apTxDataPkts,'apRxDataPkts':apRxDataPkts,'apUplinkDataOctets':apUplinkDataOctets,'apDwlinkDataOctets':apDwlinkDataOctets,'apChStatsDwlinkTotRetryPkts':apChStatsDwlinkTotRetryPkts,'apChStatsPhyErrPkts':apChStatsPhyErrPkts,'apChStatsMacFcsErrPkts':apChStatsMacFcsErrPkts,'apChStatsMacMicErrPkts':apChStatsMacMicErrPkts,'apChStatsMacDecryptErrPkts':apChStatsMacDecryptErrPkts,'apChStatsTotalErrPkts':apChStatsTotalErrPkts,'apRxMgmtFrameCnt':apRxMgmtFrameCnt,'apRxCtrlFrameCnt':apRxCtrlFrameCnt,'apRxDataFrameCnt':apRxDataFrameCnt,'apTxMgmtFrameCnt':apTxMgmtFrameCnt,'apTxCtrlFrameCnt':apTxCtrlFrameCnt,'apTxDataFrameCnt':apTxDataFrameCnt,'apChStatsFrameErrorCnt':apChStatsFrameErrorCnt,'apRetryCnt':apRetryCnt,'apCurTxPwr':apCurTxPwr,'apAPNeighborSSIDList':apAPNeighborSSIDList,'apChanStaNum':apChanStaNum,'apChDownUnicastFrame':apChDownUnicastFrame,'apChDownNonUnicastFrame':apChDownNonUnicastFrame,'apChRxAuthFrame':apChRxAuthFrame,'apChRxAssoFrame':apChRxAssoFrame,'apChTxAuthFrame':apChTxAuthFrame,'apChTxAssoFrame':apChTxAssoFrame,'apSSIDPeformanceStat':apSSIDPeformanceStat,'apSSIDPfmStatTable':apSSIDPfmStatTable,'apSSIDPfmStatEntry':apSSIDPfmStatEntry,'apSSIDTxDataPkts':apSSIDTxDataPkts,'apSSIDRxDataPkts':apSSIDRxDataPkts,'apSSIDUplinkDataOctets':apSSIDUplinkDataOctets,'apSSIDDwlinkDataOctets':apSSIDDwlinkDataOctets,'apSSIDChStatsDwlinkTotRetryPkts':apSSIDChStatsDwlinkTotRetryPkts,'apSSIDApChStatsNumStations':apSSIDApChStatsNumStations,'apTermPeformanceStat':apTermPeformanceStat,'apTermPfmStatTable':apTermPfmStatTable,'apTermPfmStatEntry':apTermPfmStatEntry,_d:apStaAddress,'apStaUpTime':apStaUpTime,'apAPReceivedStaSignalStrength':apAPReceivedStaSignalStrength,'apAPReceiveStaSNR':apAPReceiveStaSNR,'apStaTxPkts':apStaTxPkts,'apStaTxBytes':apStaTxBytes,'apStaRxPkts':apStaRxPkts,'apStaRxBytes':apStaRxBytes,'apWAPIPeformanceStat':apWAPIPeformanceStat,'apWAPIPfmStatTable':apWAPIPfmStatTable,'apWAPIPfmStatEntry':apWAPIPfmStatEntry,_e:apSTAAddress,'apVersion':apVersion,'apControlledPortStatus':apControlledPortStatus,'apSelectedUnicastCipher':apSelectedUnicastCipher,'apWPIReplayCounters':apWPIReplayCounters,'apWPIDecryptableErrors':apWPIDecryptableErrors,'apWPIMICErrors':apWPIMICErrors,'apWAISignatureErrors':apWAISignatureErrors,'apWAIHMACErrors':apWAIHMACErrors,'apWAIAuthResultFailures':apWAIAuthResultFailures,'apWAIDiscardCounters':apWAIDiscardCounters,'apWAITimeoutCounters':apWAITimeoutCounters,'apWAIFormatErrors':apWAIFormatErrors,'apWAICertificateHandshakeFailures':apWAICertificateHandshakeFailures,'apWAIUnicastHandshakeFailures':apWAIUnicastHandshakeFailures,'apWAIMulticastHandshakeFailures':apWAIMulticastHandshakeFailures,'apQOSPeformanceStat':apQOSPeformanceStat,'apQosBasePfmStatTable':apQosBasePfmStatTable,'apQosBasePfmStatEntry':apQosBasePfmStatEntry,'apQoSSvcQueAvgLen':apQoSSvcQueAvgLen,'apQoSSvcPktLossRatio':apQoSSvcPktLossRatio,'apAvgTransSpeed':apAvgTransSpeed,'apBackgroundQosPfmStatTable':apBackgroundQosPfmStatTable,'apBackgroundQosPfmStatEntry':apBackgroundQosPfmStatEntry,'apBgQueAvgLen':apBgQueAvgLen,'apBgAvgBurst':apBgAvgBurst,'apBgPktLossRatio':apBgPktLossRatio,'apBgAvgTransSpeed':apBgAvgTransSpeed,'apBgSvcLoss':apBgSvcLoss,'apBestEffortQosPfmStatTable':apBestEffortQosPfmStatTable,'apBestEffortQosPfmStatEntry':apBestEffortQosPfmStatEntry,'apBeQueAvgLen':apBeQueAvgLen,'apBeAvgBurst':apBeAvgBurst,'apBePktLossRatio':apBePktLossRatio,'apBeAvgTransSpeed':apBeAvgTransSpeed,'apBeSvcLoss':apBeSvcLoss,'apVoiceQosPfmStatTable':apVoiceQosPfmStatTable,'apVoiceQosPfmStatEntry':apVoiceQosPfmStatEntry,'apVoiceQueAvgLen':apVoiceQueAvgLen,'apVoiceAvgBurst':apVoiceAvgBurst,'apVoicePktLossRatio':apVoicePktLossRatio,'apVoiceAvgTransSpeed':apVoiceAvgTransSpeed,'apVoicePutThroughRatio':apVoicePutThroughRatio,'apVoiceDropRatio':apVoiceDropRatio,'apVoiceSvcLoss':apVoiceSvcLoss,'apVoiceExceedMaxUsersRequest':apVoiceExceedMaxUsersRequest,'apVedioQosPfmStatTable':apVedioQosPfmStatTable,'apVedioQosPfmStatEntry':apVedioQosPfmStatEntry,'apVedioQueAvgLen':apVedioQueAvgLen,'apVedioAvgBurst':apVedioAvgBurst,'apVedioPktLossRatio':apVedioPktLossRatio,'apVedioAvgTransSpeed':apVedioAvgTransSpeed,'apVedioPutThroughRatio':apVedioPutThroughRatio,'apVedioDropRatio':apVedioDropRatio,'apVedioSvcLoss':apVedioSvcLoss,'apVedioExceedMaxUsersRequest':apVedioExceedMaxUsersRequest})