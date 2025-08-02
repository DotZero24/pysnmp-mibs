_Am='hpSwitchAclGroupingEnableGroup'
_Al='hpSwitchRESTInterfaceGroup'
_Ak='hpSwitchFPModuleGroup'
_Aj='hpSwitchBasicConfigGroup4'
_Ai='hpSwitchModuleConfigGroup'
_Ah='hpSwitchIgnoreUntagMacConfigGroup'
_Ag='hpSwitchCdpPreStdVoiceGroup'
_Af='hpSwitchCdpConfigGroup'
_Ae='hpSwitchBasicConfigGroup3'
_Ad='hpSwitchBasicConfigGroup2'
_Ac='hpSwitchStartupConfigChange'
_Ab='hpSwitchRunningConfigChange'
_Aa='hpSwitchAclGroupingEnable'
_AZ='hpSwitchRESTSessionIdleTimeout'
_AY='hpSwitchRESTInterfaceStatus'
_AX='hpSwitchFPModuleConfigName'
_AW='hpSwitchFPModuleConfigType'
_AV='hpSwitchAclIpv6DenyNonClassifiableL4Header'
_AU='hpSwitchAclIpv4DenyFragmentedTcpHeader'
_AT='hpSwitchControlPlaneProtectionAdminStatus'
_AS='hpSwitchModuleConfigModRemove'
_AR='hpSwitchIgnoreUntagMacPortList'
_AQ='hpSwitchCdpPreStdVoiceStatus'
_AP='hpSwitchCdpRunMode'
_AO='hpSwitchSecureModeLevel'
_AN='hpSwitchRunningCfgChgEntriesBumped'
_AM='hpSwitchRunningCfgChgCount'
_AL='hpSwitchRunningCfgChgLatestDateAndTime'
_AK='hpSwitchRunningCfgChgTransmitInterval'
_AJ='hpSwitchRunningCfgChgNotifyEnable'
_AI='hpSwitchImplicitConfigSave'
_AH='hpSwitchStartupConfigNotifyEnable'
_AG='hpSwitchModuleConfigModName'
_AF='hpSwitchModuleConfigModType'
_AE='hpSwitchModuleInfoModType'
_AD='hpSwitchChassisLocateWhen'
_AC='hpSwitchChassisLocateDuration'
_AB='hpSwitchChassisLocateState'
_AA='hpSwitchIgmpProxyMcastUpperIp'
_A9='hpSwitchIgmpProxyMcastLowerIp'
_A8='hpSwitchIgmpProxyDomainIp'
_A7='hpSwitchIgmpProxyDomainStatus'
_A6='hpSwitchIgmpProxyDomainName'
_A5='hpSwitchAclLogtimeoutConfig'
_A4='hpicfPortCopyName'
_A3='hpicfBridgeFilterEntryStatus'
_A2='hpicfBridgeFilterDropPortMask'
_A1='hpSwitchAliasConfigRowStatus'
_A0='hpSwitchAliasCommand'
_z='hpSwitchWebSupportUrl'
_y='hpSwitchDefaultLogon'
_x='hpSwitchSaveConfig'
_w='hpicfPortCopyNameEntry'
_v='hpSwitchCdpPreStdVoiceIfIndex'
_u='hpSwitchRunningCfgChgEventTableIndex'
_t='hpSwitchModuleInfoModId'
_s='seconds'
_r='hpSwitchAliasName'
_q='unknown'
_p='hpSwitchIgmpProxyDomainId'
_o='hpicfBridgeFilterName'
_n='OctetString'
_m='hpSwitchAclGroup'
_l='hpSwitchStartupConfigChangeGroup'
_k='hpSwitchRunningCfgChgGroup'
_j='hpSwitchBasicNotificationGroup'
_i='hpSwitchModuleGroup'
_h='hpSwitchChassisLocateGroup'
_g='hpSwitchIgmpProxyDomainConfigGroup'
_f='hpSwitchAclLogtimeoutGroup'
_e='hpicfPortCopyNameGroup'
_d='hpicfBridgeFilterConfigGroup'
_c='hpSwitchAliasGroup'
_b='hpSwitchBasicConfigGroup'
_a='hpSwitchRunningCfgChgEventDateAndTime'
_Z='hpSwitchRunningCfgChgEventUsername'
_Y='hpSwitchRunningCfgChgEventSourceIPAddr'
_X='hpSwitchRunningCfgChgEventSourceIPAddrType'
_W='hpSwitchRunningCfgChgEventMethod'
_V='hpSwitchRunningCfgChgEventId'
_U='hpSwitchStartupConfigThrottled'
_T='hpSwitchStartupConfigSourceUsername'
_S='hpSwitchStartupConfigSourceIPAddr'
_R='hpSwitchStartupConfigSourceIPAddrType'
_Q='hpSwitchStartupConfigSource'
_P='hpSwitchStartupConfigSeqNum'
_O='TruthValue'
_N='Unsigned32'
_M='entPhysicalIndex'
_L='ENTITY-MIB'
_K='accessible-for-notify'
_J='not-accessible'
_I='disable'
_H='enable'
_G='read-create'
_F='DisplayString'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='HP-SWITCH-BASIC-CONFIG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_n,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitchConfig,hpSwitchFilterConfig,hpSwitchIgmpConfig=mibBuilder.importSymbols('CONFIG-MIB','hpSwitchConfig','hpSwitchFilterConfig','hpSwitchIgmpConfig')
entPhysicalIndex,=mibBuilder.importSymbols(_L,_M)
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
portCopyEntry,=mibBuilder.importSymbols('SMON-MIB','portCopyEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'PhysAddress','RowStatus','TextualConvention',_O)
hpSwitchBasicConfigMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29))
if mibBuilder.loadTexts:hpSwitchBasicConfigMIB.setRevisions(('2015-10-11 00:00','2015-04-20 00:00','2014-12-11 00:00','2014-03-25 00:00','2013-07-22 00:00','2013-05-22 00:00','2013-02-16 00:00','2012-02-03 00:00','2011-09-08 00:00','2011-06-15 21:07','2010-08-05 00:00','2010-06-28 00:00','2010-04-14 00:00','2010-02-17 00:00','2009-09-10 00:00','2009-08-18 00:00','2009-07-30 00:00'))
_HpicfBridgeFilterConfigTable_Object=MibTable
hpicfBridgeFilterConfigTable=_HpicfBridgeFilterConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,8,2))
if mibBuilder.loadTexts:hpicfBridgeFilterConfigTable.setStatus(_A)
_HpicfBridgeFilterConfigEntry_Object=MibTableRow
hpicfBridgeFilterConfigEntry=_HpicfBridgeFilterConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,8,2,1))
hpicfBridgeFilterConfigEntry.setIndexNames((0,_B,_o))
if mibBuilder.loadTexts:hpicfBridgeFilterConfigEntry.setStatus(_A)
class _HpicfBridgeFilterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_HpicfBridgeFilterName_Type.__name__=_F
_HpicfBridgeFilterName_Object=MibTableColumn
hpicfBridgeFilterName=_HpicfBridgeFilterName_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,8,2,1,1),_HpicfBridgeFilterName_Type())
hpicfBridgeFilterName.setMaxAccess(_J)
if mibBuilder.loadTexts:hpicfBridgeFilterName.setStatus(_A)
_HpicfBridgeFilterDropPortMask_Type=PortList
_HpicfBridgeFilterDropPortMask_Object=MibTableColumn
hpicfBridgeFilterDropPortMask=_HpicfBridgeFilterDropPortMask_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,8,2,1,2),_HpicfBridgeFilterDropPortMask_Type())
hpicfBridgeFilterDropPortMask.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfBridgeFilterDropPortMask.setStatus(_A)
_HpicfBridgeFilterEntryStatus_Type=RowStatus
_HpicfBridgeFilterEntryStatus_Object=MibTableColumn
hpicfBridgeFilterEntryStatus=_HpicfBridgeFilterEntryStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,8,2,1,3),_HpicfBridgeFilterEntryStatus_Type())
hpicfBridgeFilterEntryStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfBridgeFilterEntryStatus.setStatus(_A)
_HpSwitchIgmpProxyDomainConfigTable_Object=MibTable
hpSwitchIgmpProxyDomainConfigTable=_HpSwitchIgmpProxyDomainConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,5))
if mibBuilder.loadTexts:hpSwitchIgmpProxyDomainConfigTable.setStatus(_A)
_HpSwitchIgmpProxyDomainConfigEntry_Object=MibTableRow
hpSwitchIgmpProxyDomainConfigEntry=_HpSwitchIgmpProxyDomainConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,5,1))
hpSwitchIgmpProxyDomainConfigEntry.setIndexNames((0,_B,_p))
if mibBuilder.loadTexts:hpSwitchIgmpProxyDomainConfigEntry.setStatus(_A)
class _HpSwitchIgmpProxyDomainId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchIgmpProxyDomainId_Type.__name__=_D
_HpSwitchIgmpProxyDomainId_Object=MibTableColumn
hpSwitchIgmpProxyDomainId=_HpSwitchIgmpProxyDomainId_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,5,1,1),_HpSwitchIgmpProxyDomainId_Type())
hpSwitchIgmpProxyDomainId.setMaxAccess(_J)
if mibBuilder.loadTexts:hpSwitchIgmpProxyDomainId.setStatus(_A)
_HpSwitchIgmpProxyDomainStatus_Type=RowStatus
_HpSwitchIgmpProxyDomainStatus_Object=MibTableColumn
hpSwitchIgmpProxyDomainStatus=_HpSwitchIgmpProxyDomainStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,5,1,2),_HpSwitchIgmpProxyDomainStatus_Type())
hpSwitchIgmpProxyDomainStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpSwitchIgmpProxyDomainStatus.setStatus(_A)
_HpSwitchIgmpProxyDomainName_Type=DisplayString
_HpSwitchIgmpProxyDomainName_Object=MibTableColumn
hpSwitchIgmpProxyDomainName=_HpSwitchIgmpProxyDomainName_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,5,1,3),_HpSwitchIgmpProxyDomainName_Type())
hpSwitchIgmpProxyDomainName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpSwitchIgmpProxyDomainName.setStatus(_A)
_HpSwitchIgmpProxyDomainIp_Type=IpAddress
_HpSwitchIgmpProxyDomainIp_Object=MibTableColumn
hpSwitchIgmpProxyDomainIp=_HpSwitchIgmpProxyDomainIp_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,5,1,4),_HpSwitchIgmpProxyDomainIp_Type())
hpSwitchIgmpProxyDomainIp.setMaxAccess(_G)
if mibBuilder.loadTexts:hpSwitchIgmpProxyDomainIp.setStatus(_A)
_HpSwitchIgmpProxyMcastLowerIp_Type=IpAddress
_HpSwitchIgmpProxyMcastLowerIp_Object=MibTableColumn
hpSwitchIgmpProxyMcastLowerIp=_HpSwitchIgmpProxyMcastLowerIp_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,5,1,5),_HpSwitchIgmpProxyMcastLowerIp_Type())
hpSwitchIgmpProxyMcastLowerIp.setMaxAccess(_G)
if mibBuilder.loadTexts:hpSwitchIgmpProxyMcastLowerIp.setStatus(_A)
_HpSwitchIgmpProxyMcastUpperIp_Type=IpAddress
_HpSwitchIgmpProxyMcastUpperIp_Object=MibTableColumn
hpSwitchIgmpProxyMcastUpperIp=_HpSwitchIgmpProxyMcastUpperIp_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,5,1,6),_HpSwitchIgmpProxyMcastUpperIp_Type())
hpSwitchIgmpProxyMcastUpperIp.setMaxAccess(_G)
if mibBuilder.loadTexts:hpSwitchIgmpProxyMcastUpperIp.setStatus(_A)
_HpSwitchBasicConfigObjects_ObjectIdentity=ObjectIdentity
hpSwitchBasicConfigObjects=_HpSwitchBasicConfigObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1))
_HpSwitchNotificationObjects_ObjectIdentity=ObjectIdentity
hpSwitchNotificationObjects=_HpSwitchNotificationObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,0))
class _HpSwitchStartupConfigSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_q,0),('viaCli',1),('viaSnmp',2),('viaWebUI',3)))
_HpSwitchStartupConfigSource_Type.__name__=_D
_HpSwitchStartupConfigSource_Object=MibScalar
hpSwitchStartupConfigSource=_HpSwitchStartupConfigSource_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,0,1),_HpSwitchStartupConfigSource_Type())
hpSwitchStartupConfigSource.setMaxAccess(_K)
if mibBuilder.loadTexts:hpSwitchStartupConfigSource.setStatus(_A)
_HpSwitchStartupConfigSourceIPAddrType_Type=InetAddressType
_HpSwitchStartupConfigSourceIPAddrType_Object=MibScalar
hpSwitchStartupConfigSourceIPAddrType=_HpSwitchStartupConfigSourceIPAddrType_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,0,2),_HpSwitchStartupConfigSourceIPAddrType_Type())
hpSwitchStartupConfigSourceIPAddrType.setMaxAccess(_K)
if mibBuilder.loadTexts:hpSwitchStartupConfigSourceIPAddrType.setStatus(_A)
_HpSwitchStartupConfigSourceIPAddr_Type=InetAddress
_HpSwitchStartupConfigSourceIPAddr_Object=MibScalar
hpSwitchStartupConfigSourceIPAddr=_HpSwitchStartupConfigSourceIPAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,0,3),_HpSwitchStartupConfigSourceIPAddr_Type())
hpSwitchStartupConfigSourceIPAddr.setMaxAccess(_K)
if mibBuilder.loadTexts:hpSwitchStartupConfigSourceIPAddr.setStatus(_A)
class _HpSwitchStartupConfigSourceUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpSwitchStartupConfigSourceUsername_Type.__name__=_F
_HpSwitchStartupConfigSourceUsername_Object=MibScalar
hpSwitchStartupConfigSourceUsername=_HpSwitchStartupConfigSourceUsername_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,0,4),_HpSwitchStartupConfigSourceUsername_Type())
hpSwitchStartupConfigSourceUsername.setMaxAccess(_K)
if mibBuilder.loadTexts:hpSwitchStartupConfigSourceUsername.setStatus(_A)
class _HpSwitchStartupConfigThrottled_Type(TruthValue):defaultValue=2
_HpSwitchStartupConfigThrottled_Type.__name__=_O
_HpSwitchStartupConfigThrottled_Object=MibScalar
hpSwitchStartupConfigThrottled=_HpSwitchStartupConfigThrottled_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,0,5),_HpSwitchStartupConfigThrottled_Type())
hpSwitchStartupConfigThrottled.setMaxAccess(_K)
if mibBuilder.loadTexts:hpSwitchStartupConfigThrottled.setStatus(_A)
class _HpSwitchSaveConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noConfigSave',1),('saveConfig',2)))
_HpSwitchSaveConfig_Type.__name__=_D
_HpSwitchSaveConfig_Object=MibScalar
hpSwitchSaveConfig=_HpSwitchSaveConfig_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,1),_HpSwitchSaveConfig_Type())
hpSwitchSaveConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSaveConfig.setStatus(_A)
_HpSwitchAliasTable_Object=MibTable
hpSwitchAliasTable=_HpSwitchAliasTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,2))
if mibBuilder.loadTexts:hpSwitchAliasTable.setStatus(_A)
_HpSwitchAliasEntry_Object=MibTableRow
hpSwitchAliasEntry=_HpSwitchAliasEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,2,1))
hpSwitchAliasEntry.setIndexNames((0,_B,_r))
if mibBuilder.loadTexts:hpSwitchAliasEntry.setStatus(_A)
class _HpSwitchAliasName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_HpSwitchAliasName_Type.__name__=_F
_HpSwitchAliasName_Object=MibTableColumn
hpSwitchAliasName=_HpSwitchAliasName_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,2,1,1),_HpSwitchAliasName_Type())
hpSwitchAliasName.setMaxAccess(_J)
if mibBuilder.loadTexts:hpSwitchAliasName.setStatus(_A)
class _HpSwitchAliasCommand_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_HpSwitchAliasCommand_Type.__name__=_n
_HpSwitchAliasCommand_Object=MibTableColumn
hpSwitchAliasCommand=_HpSwitchAliasCommand_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,2,1,2),_HpSwitchAliasCommand_Type())
hpSwitchAliasCommand.setMaxAccess(_G)
if mibBuilder.loadTexts:hpSwitchAliasCommand.setStatus(_A)
_HpSwitchAliasConfigRowStatus_Type=RowStatus
_HpSwitchAliasConfigRowStatus_Object=MibTableColumn
hpSwitchAliasConfigRowStatus=_HpSwitchAliasConfigRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,2,1,3),_HpSwitchAliasConfigRowStatus_Type())
hpSwitchAliasConfigRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpSwitchAliasConfigRowStatus.setStatus(_A)
_HpSwitchACLConfig_ObjectIdentity=ObjectIdentity
hpSwitchACLConfig=_HpSwitchACLConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,3))
class _HpSwitchAclLogtimeoutConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchAclLogtimeoutConfig_Type.__name__=_D
_HpSwitchAclLogtimeoutConfig_Object=MibScalar
hpSwitchAclLogtimeoutConfig=_HpSwitchAclLogtimeoutConfig_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,3,1),_HpSwitchAclLogtimeoutConfig_Type())
hpSwitchAclLogtimeoutConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAclLogtimeoutConfig.setStatus(_A)
class _HpSwitchAclIpv4DenyFragmentedTcpHeader_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HpSwitchAclIpv4DenyFragmentedTcpHeader_Type.__name__=_D
_HpSwitchAclIpv4DenyFragmentedTcpHeader_Object=MibScalar
hpSwitchAclIpv4DenyFragmentedTcpHeader=_HpSwitchAclIpv4DenyFragmentedTcpHeader_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,3,2),_HpSwitchAclIpv4DenyFragmentedTcpHeader_Type())
hpSwitchAclIpv4DenyFragmentedTcpHeader.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAclIpv4DenyFragmentedTcpHeader.setStatus(_A)
class _HpSwitchAclIpv6DenyNonClassifiableL4Header_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HpSwitchAclIpv6DenyNonClassifiableL4Header_Type.__name__=_D
_HpSwitchAclIpv6DenyNonClassifiableL4Header_Object=MibScalar
hpSwitchAclIpv6DenyNonClassifiableL4Header=_HpSwitchAclIpv6DenyNonClassifiableL4Header_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,3,3),_HpSwitchAclIpv6DenyNonClassifiableL4Header_Type())
hpSwitchAclIpv6DenyNonClassifiableL4Header.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAclIpv6DenyNonClassifiableL4Header.setStatus(_A)
class _HpSwitchAclGroupingEnable_Type(TruthValue):defaultValue=2
_HpSwitchAclGroupingEnable_Type.__name__=_O
_HpSwitchAclGroupingEnable_Object=MibScalar
hpSwitchAclGroupingEnable=_HpSwitchAclGroupingEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,3,4),_HpSwitchAclGroupingEnable_Type())
hpSwitchAclGroupingEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAclGroupingEnable.setStatus(_A)
_HpicfPortCopyNameTable_Object=MibTable
hpicfPortCopyNameTable=_HpicfPortCopyNameTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,4))
if mibBuilder.loadTexts:hpicfPortCopyNameTable.setStatus(_A)
_HpicfPortCopyNameEntry_Object=MibTableRow
hpicfPortCopyNameEntry=_HpicfPortCopyNameEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,4,1))
if mibBuilder.loadTexts:hpicfPortCopyNameEntry.setStatus(_A)
_HpicfPortCopyName_Type=DisplayString
_HpicfPortCopyName_Object=MibTableColumn
hpicfPortCopyName=_HpicfPortCopyName_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,4,1,1),_HpicfPortCopyName_Type())
hpicfPortCopyName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfPortCopyName.setStatus(_A)
class _HpSwitchDefaultLogon_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('cli',0),('menu',1)))
_HpSwitchDefaultLogon_Type.__name__=_D
_HpSwitchDefaultLogon_Object=MibScalar
hpSwitchDefaultLogon=_HpSwitchDefaultLogon_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,5),_HpSwitchDefaultLogon_Type())
hpSwitchDefaultLogon.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDefaultLogon.setStatus(_A)
_HpSwitchChassisLocateTable_Object=MibTable
hpSwitchChassisLocateTable=_HpSwitchChassisLocateTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,6))
if mibBuilder.loadTexts:hpSwitchChassisLocateTable.setStatus(_A)
_HpSwitchChassisLocateEntry_Object=MibTableRow
hpSwitchChassisLocateEntry=_HpSwitchChassisLocateEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,6,1))
hpSwitchChassisLocateEntry.setIndexNames((0,_L,_M))
if mibBuilder.loadTexts:hpSwitchChassisLocateEntry.setStatus(_A)
class _HpSwitchChassisLocateState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('off',1),('on',2),('blink',3)))
_HpSwitchChassisLocateState_Type.__name__=_D
_HpSwitchChassisLocateState_Object=MibTableColumn
hpSwitchChassisLocateState=_HpSwitchChassisLocateState_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,6,1,1),_HpSwitchChassisLocateState_Type())
hpSwitchChassisLocateState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchChassisLocateState.setStatus(_A)
class _HpSwitchChassisLocateDuration_Type(Integer32):defaultValue=1800
_HpSwitchChassisLocateDuration_Type.__name__=_D
_HpSwitchChassisLocateDuration_Object=MibTableColumn
hpSwitchChassisLocateDuration=_HpSwitchChassisLocateDuration_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,6,1,2),_HpSwitchChassisLocateDuration_Type())
hpSwitchChassisLocateDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchChassisLocateDuration.setStatus(_A)
if mibBuilder.loadTexts:hpSwitchChassisLocateDuration.setUnits(_s)
class _HpSwitchChassisLocateWhen_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('now',1),('startup',2)))
_HpSwitchChassisLocateWhen_Type.__name__=_D
_HpSwitchChassisLocateWhen_Object=MibTableColumn
hpSwitchChassisLocateWhen=_HpSwitchChassisLocateWhen_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,6,1,3),_HpSwitchChassisLocateWhen_Type())
hpSwitchChassisLocateWhen.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchChassisLocateWhen.setStatus(_A)
_HpSwitchModules_ObjectIdentity=ObjectIdentity
hpSwitchModules=_HpSwitchModules_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,7))
_HpSwitchModuleInfoTable_Object=MibTable
hpSwitchModuleInfoTable=_HpSwitchModuleInfoTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,7,1))
if mibBuilder.loadTexts:hpSwitchModuleInfoTable.setStatus(_A)
_HpSwitchModuleInfoEntry_Object=MibTableRow
hpSwitchModuleInfoEntry=_HpSwitchModuleInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,7,1,1))
hpSwitchModuleInfoEntry.setIndexNames((0,_B,_t))
if mibBuilder.loadTexts:hpSwitchModuleInfoEntry.setStatus(_A)
class _HpSwitchModuleInfoModId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchModuleInfoModId_Type.__name__=_D
_HpSwitchModuleInfoModId_Object=MibTableColumn
hpSwitchModuleInfoModId=_HpSwitchModuleInfoModId_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,7,1,1,1),_HpSwitchModuleInfoModId_Type())
hpSwitchModuleInfoModId.setMaxAccess(_J)
if mibBuilder.loadTexts:hpSwitchModuleInfoModId.setStatus(_A)
class _HpSwitchModuleInfoModType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_HpSwitchModuleInfoModType_Type.__name__=_F
_HpSwitchModuleInfoModType_Object=MibTableColumn
hpSwitchModuleInfoModType=_HpSwitchModuleInfoModType_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,7,1,1,2),_HpSwitchModuleInfoModType_Type())
hpSwitchModuleInfoModType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchModuleInfoModType.setStatus(_A)
_HpSwitchModuleConfigTable_Object=MibTable
hpSwitchModuleConfigTable=_HpSwitchModuleConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,7,2))
if mibBuilder.loadTexts:hpSwitchModuleConfigTable.setStatus(_A)
_HpSwitchModuleConfigEntry_Object=MibTableRow
hpSwitchModuleConfigEntry=_HpSwitchModuleConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,7,2,1))
hpSwitchModuleConfigEntry.setIndexNames((0,_L,_M))
if mibBuilder.loadTexts:hpSwitchModuleConfigEntry.setStatus(_A)
class _HpSwitchModuleConfigModType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpSwitchModuleConfigModType_Type.__name__=_F
_HpSwitchModuleConfigModType_Object=MibTableColumn
hpSwitchModuleConfigModType=_HpSwitchModuleConfigModType_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,7,2,1,1),_HpSwitchModuleConfigModType_Type())
hpSwitchModuleConfigModType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchModuleConfigModType.setStatus(_A)
class _HpSwitchModuleConfigModName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpSwitchModuleConfigModName_Type.__name__=_F
_HpSwitchModuleConfigModName_Object=MibTableColumn
hpSwitchModuleConfigModName=_HpSwitchModuleConfigModName_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,7,2,1,2),_HpSwitchModuleConfigModName_Type())
hpSwitchModuleConfigModName.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchModuleConfigModName.setStatus(_A)
_HpSwitchModuleConfigModRemove_Type=TruthValue
_HpSwitchModuleConfigModRemove_Object=MibTableColumn
hpSwitchModuleConfigModRemove=_HpSwitchModuleConfigModRemove_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,7,2,1,3),_HpSwitchModuleConfigModRemove_Type())
hpSwitchModuleConfigModRemove.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchModuleConfigModRemove.setStatus(_A)
class _HpSwitchWebSupportUrl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpSwitchWebSupportUrl_Type.__name__=_F
_HpSwitchWebSupportUrl_Object=MibScalar
hpSwitchWebSupportUrl=_HpSwitchWebSupportUrl_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,8),_HpSwitchWebSupportUrl_Type())
hpSwitchWebSupportUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchWebSupportUrl.setStatus(_A)
class _HpSwitchStartupConfigSeqNum_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpSwitchStartupConfigSeqNum_Type.__name__=_N
_HpSwitchStartupConfigSeqNum_Object=MibScalar
hpSwitchStartupConfigSeqNum=_HpSwitchStartupConfigSeqNum_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,9),_HpSwitchStartupConfigSeqNum_Type())
hpSwitchStartupConfigSeqNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchStartupConfigSeqNum.setStatus(_A)
class _HpSwitchStartupConfigNotifyEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HpSwitchStartupConfigNotifyEnable_Type.__name__=_D
_HpSwitchStartupConfigNotifyEnable_Object=MibScalar
hpSwitchStartupConfigNotifyEnable=_HpSwitchStartupConfigNotifyEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,10),_HpSwitchStartupConfigNotifyEnable_Type())
hpSwitchStartupConfigNotifyEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchStartupConfigNotifyEnable.setStatus(_A)
class _HpSwitchImplicitConfigSave_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HpSwitchImplicitConfigSave_Type.__name__=_D
_HpSwitchImplicitConfigSave_Object=MibScalar
hpSwitchImplicitConfigSave=_HpSwitchImplicitConfigSave_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,11),_HpSwitchImplicitConfigSave_Type())
hpSwitchImplicitConfigSave.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchImplicitConfigSave.setStatus(_A)
_HpSwitchRunningCfgChgObjects_ObjectIdentity=ObjectIdentity
hpSwitchRunningCfgChgObjects=_HpSwitchRunningCfgChgObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,12))
class _HpSwitchRunningCfgChgNotifyEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HpSwitchRunningCfgChgNotifyEnable_Type.__name__=_D
_HpSwitchRunningCfgChgNotifyEnable_Object=MibScalar
hpSwitchRunningCfgChgNotifyEnable=_HpSwitchRunningCfgChgNotifyEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,12,1),_HpSwitchRunningCfgChgNotifyEnable_Type())
hpSwitchRunningCfgChgNotifyEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchRunningCfgChgNotifyEnable.setStatus(_A)
class _HpSwitchRunningCfgChgTransmitInterval_Type(Unsigned32):defaultValue=0
_HpSwitchRunningCfgChgTransmitInterval_Type.__name__=_N
_HpSwitchRunningCfgChgTransmitInterval_Object=MibScalar
hpSwitchRunningCfgChgTransmitInterval=_HpSwitchRunningCfgChgTransmitInterval_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,12,2),_HpSwitchRunningCfgChgTransmitInterval_Type())
hpSwitchRunningCfgChgTransmitInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchRunningCfgChgTransmitInterval.setStatus(_A)
_HpSwitchRunningCfgChgLatestDateAndTime_Type=DateAndTime
_HpSwitchRunningCfgChgLatestDateAndTime_Object=MibScalar
hpSwitchRunningCfgChgLatestDateAndTime=_HpSwitchRunningCfgChgLatestDateAndTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,12,3),_HpSwitchRunningCfgChgLatestDateAndTime_Type())
hpSwitchRunningCfgChgLatestDateAndTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchRunningCfgChgLatestDateAndTime.setStatus(_A)
_HpSwitchRunningCfgChgCount_Type=Counter32
_HpSwitchRunningCfgChgCount_Object=MibScalar
hpSwitchRunningCfgChgCount=_HpSwitchRunningCfgChgCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,12,4),_HpSwitchRunningCfgChgCount_Type())
hpSwitchRunningCfgChgCount.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchRunningCfgChgCount.setStatus(_A)
_HpSwitchRunningCfgChgEntriesBumped_Type=Counter32
_HpSwitchRunningCfgChgEntriesBumped_Object=MibScalar
hpSwitchRunningCfgChgEntriesBumped=_HpSwitchRunningCfgChgEntriesBumped_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,12,5),_HpSwitchRunningCfgChgEntriesBumped_Type())
hpSwitchRunningCfgChgEntriesBumped.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchRunningCfgChgEntriesBumped.setStatus(_A)
_HpSwitchRunningCfgChgEventTable_Object=MibTable
hpSwitchRunningCfgChgEventTable=_HpSwitchRunningCfgChgEventTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,12,6))
if mibBuilder.loadTexts:hpSwitchRunningCfgChgEventTable.setStatus(_A)
_HpSwitchRunningCfgChgEventEntry_Object=MibTableRow
hpSwitchRunningCfgChgEventEntry=_HpSwitchRunningCfgChgEventEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,12,6,1))
hpSwitchRunningCfgChgEventEntry.setIndexNames((0,_B,_u))
if mibBuilder.loadTexts:hpSwitchRunningCfgChgEventEntry.setStatus(_A)
class _HpSwitchRunningCfgChgEventTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpSwitchRunningCfgChgEventTableIndex_Type.__name__=_D
_HpSwitchRunningCfgChgEventTableIndex_Object=MibTableColumn
hpSwitchRunningCfgChgEventTableIndex=_HpSwitchRunningCfgChgEventTableIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,12,6,1,1),_HpSwitchRunningCfgChgEventTableIndex_Type())
hpSwitchRunningCfgChgEventTableIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hpSwitchRunningCfgChgEventTableIndex.setStatus(_A)
class _HpSwitchRunningCfgChgEventId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpSwitchRunningCfgChgEventId_Type.__name__=_N
_HpSwitchRunningCfgChgEventId_Object=MibTableColumn
hpSwitchRunningCfgChgEventId=_HpSwitchRunningCfgChgEventId_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,12,6,1,2),_HpSwitchRunningCfgChgEventId_Type())
hpSwitchRunningCfgChgEventId.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchRunningCfgChgEventId.setStatus(_A)
class _HpSwitchRunningCfgChgEventMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_q,0),('cli',1),('menu',2),('snmp',3),('webUI',4),('internalEvent',5)))
_HpSwitchRunningCfgChgEventMethod_Type.__name__=_D
_HpSwitchRunningCfgChgEventMethod_Object=MibTableColumn
hpSwitchRunningCfgChgEventMethod=_HpSwitchRunningCfgChgEventMethod_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,12,6,1,3),_HpSwitchRunningCfgChgEventMethod_Type())
hpSwitchRunningCfgChgEventMethod.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchRunningCfgChgEventMethod.setStatus(_A)
_HpSwitchRunningCfgChgEventSourceIPAddrType_Type=InetAddressType
_HpSwitchRunningCfgChgEventSourceIPAddrType_Object=MibTableColumn
hpSwitchRunningCfgChgEventSourceIPAddrType=_HpSwitchRunningCfgChgEventSourceIPAddrType_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,12,6,1,4),_HpSwitchRunningCfgChgEventSourceIPAddrType_Type())
hpSwitchRunningCfgChgEventSourceIPAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchRunningCfgChgEventSourceIPAddrType.setStatus(_A)
_HpSwitchRunningCfgChgEventSourceIPAddr_Type=InetAddress
_HpSwitchRunningCfgChgEventSourceIPAddr_Object=MibTableColumn
hpSwitchRunningCfgChgEventSourceIPAddr=_HpSwitchRunningCfgChgEventSourceIPAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,12,6,1,5),_HpSwitchRunningCfgChgEventSourceIPAddr_Type())
hpSwitchRunningCfgChgEventSourceIPAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchRunningCfgChgEventSourceIPAddr.setStatus(_A)
class _HpSwitchRunningCfgChgEventUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpSwitchRunningCfgChgEventUsername_Type.__name__=_F
_HpSwitchRunningCfgChgEventUsername_Object=MibTableColumn
hpSwitchRunningCfgChgEventUsername=_HpSwitchRunningCfgChgEventUsername_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,12,6,1,6),_HpSwitchRunningCfgChgEventUsername_Type())
hpSwitchRunningCfgChgEventUsername.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchRunningCfgChgEventUsername.setStatus(_A)
_HpSwitchRunningCfgChgEventDateAndTime_Type=DateAndTime
_HpSwitchRunningCfgChgEventDateAndTime_Object=MibTableColumn
hpSwitchRunningCfgChgEventDateAndTime=_HpSwitchRunningCfgChgEventDateAndTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,12,6,1,7),_HpSwitchRunningCfgChgEventDateAndTime_Type())
hpSwitchRunningCfgChgEventDateAndTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchRunningCfgChgEventDateAndTime.setStatus(_A)
class _HpSwitchSecureModeLevel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,16)));namedValues=NamedValues(*(('error',0),('standard',1),('enhanced',16)))
_HpSwitchSecureModeLevel_Type.__name__=_D
_HpSwitchSecureModeLevel_Object=MibScalar
hpSwitchSecureModeLevel=_HpSwitchSecureModeLevel_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,13),_HpSwitchSecureModeLevel_Type())
hpSwitchSecureModeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSecureModeLevel.setStatus(_A)
class _HpSwitchCdpRunMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('rxonly',1),('passthru',2),('preStdVoice',3)))
_HpSwitchCdpRunMode_Type.__name__=_D
_HpSwitchCdpRunMode_Object=MibScalar
hpSwitchCdpRunMode=_HpSwitchCdpRunMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,14),_HpSwitchCdpRunMode_Type())
hpSwitchCdpRunMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCdpRunMode.setStatus(_A)
_HpSwitchCdpObjects_ObjectIdentity=ObjectIdentity
hpSwitchCdpObjects=_HpSwitchCdpObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,15))
_HpSwitchCdpPreStdVoiceTable_Object=MibTable
hpSwitchCdpPreStdVoiceTable=_HpSwitchCdpPreStdVoiceTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,15,1))
if mibBuilder.loadTexts:hpSwitchCdpPreStdVoiceTable.setStatus(_A)
_HpSwitchCdpPreStdVoiceEntry_Object=MibTableRow
hpSwitchCdpPreStdVoiceEntry=_HpSwitchCdpPreStdVoiceEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,15,1,1))
hpSwitchCdpPreStdVoiceEntry.setIndexNames((0,_B,_v))
if mibBuilder.loadTexts:hpSwitchCdpPreStdVoiceEntry.setStatus(_A)
_HpSwitchCdpPreStdVoiceIfIndex_Type=InterfaceIndex
_HpSwitchCdpPreStdVoiceIfIndex_Object=MibTableColumn
hpSwitchCdpPreStdVoiceIfIndex=_HpSwitchCdpPreStdVoiceIfIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,15,1,1,1),_HpSwitchCdpPreStdVoiceIfIndex_Type())
hpSwitchCdpPreStdVoiceIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hpSwitchCdpPreStdVoiceIfIndex.setStatus(_A)
class _HpSwitchCdpPreStdVoiceStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('txAndRx',1),('rxOnly',2)))
_HpSwitchCdpPreStdVoiceStatus_Type.__name__=_D
_HpSwitchCdpPreStdVoiceStatus_Object=MibTableColumn
hpSwitchCdpPreStdVoiceStatus=_HpSwitchCdpPreStdVoiceStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,15,1,1,2),_HpSwitchCdpPreStdVoiceStatus_Type())
hpSwitchCdpPreStdVoiceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCdpPreStdVoiceStatus.setStatus(_A)
_HpSwitchIgnoreUntagMacPortList_Type=PortList
_HpSwitchIgnoreUntagMacPortList_Object=MibScalar
hpSwitchIgnoreUntagMacPortList=_HpSwitchIgnoreUntagMacPortList_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,16),_HpSwitchIgnoreUntagMacPortList_Type())
hpSwitchIgnoreUntagMacPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchIgnoreUntagMacPortList.setStatus(_A)
class _HpSwitchControlPlaneProtectionAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HpSwitchControlPlaneProtectionAdminStatus_Type.__name__=_D
_HpSwitchControlPlaneProtectionAdminStatus_Object=MibScalar
hpSwitchControlPlaneProtectionAdminStatus=_HpSwitchControlPlaneProtectionAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,17),_HpSwitchControlPlaneProtectionAdminStatus_Type())
hpSwitchControlPlaneProtectionAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchControlPlaneProtectionAdminStatus.setStatus(_A)
_HpSwitchFPModules_ObjectIdentity=ObjectIdentity
hpSwitchFPModules=_HpSwitchFPModules_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,19))
_HpSwitchFPModuleConfigTable_Object=MibTable
hpSwitchFPModuleConfigTable=_HpSwitchFPModuleConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,19,1))
if mibBuilder.loadTexts:hpSwitchFPModuleConfigTable.setStatus(_A)
_HpSwitchFPModuleConfigEntry_Object=MibTableRow
hpSwitchFPModuleConfigEntry=_HpSwitchFPModuleConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,19,1,1))
hpSwitchFPModuleConfigEntry.setIndexNames((0,_L,_M))
if mibBuilder.loadTexts:hpSwitchFPModuleConfigEntry.setStatus(_A)
class _HpSwitchFPModuleConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('none',0),('jl078a',1),('jl079a',2),('jl081a',3),('jl083a',4)))
_HpSwitchFPModuleConfigType_Type.__name__=_D
_HpSwitchFPModuleConfigType_Object=MibTableColumn
hpSwitchFPModuleConfigType=_HpSwitchFPModuleConfigType_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,19,1,1,1),_HpSwitchFPModuleConfigType_Type())
hpSwitchFPModuleConfigType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFPModuleConfigType.setStatus(_A)
class _HpSwitchFPModuleConfigName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpSwitchFPModuleConfigName_Type.__name__=_F
_HpSwitchFPModuleConfigName_Object=MibTableColumn
hpSwitchFPModuleConfigName=_HpSwitchFPModuleConfigName_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,19,1,1,2),_HpSwitchFPModuleConfigName_Type())
hpSwitchFPModuleConfigName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFPModuleConfigName.setStatus(_A)
class _HpSwitchRESTInterfaceStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HpSwitchRESTInterfaceStatus_Type.__name__=_D
_HpSwitchRESTInterfaceStatus_Object=MibScalar
hpSwitchRESTInterfaceStatus=_HpSwitchRESTInterfaceStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,20),_HpSwitchRESTInterfaceStatus_Type())
hpSwitchRESTInterfaceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchRESTInterfaceStatus.setStatus(_A)
class _HpSwitchRESTSessionIdleTimeout_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15000))
_HpSwitchRESTSessionIdleTimeout_Type.__name__=_D
_HpSwitchRESTSessionIdleTimeout_Object=MibScalar
hpSwitchRESTSessionIdleTimeout=_HpSwitchRESTSessionIdleTimeout_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,21),_HpSwitchRESTSessionIdleTimeout_Type())
hpSwitchRESTSessionIdleTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchRESTSessionIdleTimeout.setStatus(_A)
if mibBuilder.loadTexts:hpSwitchRESTSessionIdleTimeout.setUnits(_s)
_HpSwitchBasicConfigConformance_ObjectIdentity=ObjectIdentity
hpSwitchBasicConfigConformance=_HpSwitchBasicConfigConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2))
_HpSwitchBasicConfigCompliances_ObjectIdentity=ObjectIdentity
hpSwitchBasicConfigCompliances=_HpSwitchBasicConfigCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,1))
_HpSwitchBasicConfigGroups_ObjectIdentity=ObjectIdentity
hpSwitchBasicConfigGroups=_HpSwitchBasicConfigGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,2))
_HpSwitchBasicNotificationGroups_ObjectIdentity=ObjectIdentity
hpSwitchBasicNotificationGroups=_HpSwitchBasicNotificationGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,3))
portCopyEntry.registerAugmentions((_B,_w))
hpicfPortCopyNameEntry.setIndexNames(*portCopyEntry.getIndexNames())
hpSwitchBasicConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,2,1))
hpSwitchBasicConfigGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:hpSwitchBasicConfigGroup.setStatus(_A)
hpSwitchAliasGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,2,2))
hpSwitchAliasGroup.setObjects(*((_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:hpSwitchAliasGroup.setStatus(_A)
hpicfBridgeFilterConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,2,3))
hpicfBridgeFilterConfigGroup.setObjects(*((_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:hpicfBridgeFilterConfigGroup.setStatus(_A)
hpicfPortCopyNameGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,2,4))
hpicfPortCopyNameGroup.setObjects((_B,_A4))
if mibBuilder.loadTexts:hpicfPortCopyNameGroup.setStatus(_A)
hpSwitchAclLogtimeoutGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,2,5))
hpSwitchAclLogtimeoutGroup.setObjects((_B,_A5))
if mibBuilder.loadTexts:hpSwitchAclLogtimeoutGroup.setStatus(_A)
hpSwitchIgmpProxyDomainConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,2,6))
hpSwitchIgmpProxyDomainConfigGroup.setObjects(*((_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:hpSwitchIgmpProxyDomainConfigGroup.setStatus(_A)
hpSwitchChassisLocateGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,2,7))
hpSwitchChassisLocateGroup.setObjects(*((_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:hpSwitchChassisLocateGroup.setStatus(_A)
hpSwitchModuleGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,2,8))
hpSwitchModuleGroup.setObjects(*((_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:hpSwitchModuleGroup.setStatus(_A)
hpSwitchStartupConfigChangeGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,2,9))
hpSwitchStartupConfigChangeGroup.setObjects(*((_B,_P),(_B,_AH),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:hpSwitchStartupConfigChangeGroup.setStatus(_A)
hpSwitchBasicConfigGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,2,10))
hpSwitchBasicConfigGroup2.setObjects((_B,_AI))
if mibBuilder.loadTexts:hpSwitchBasicConfigGroup2.setStatus(_A)
hpSwitchRunningCfgChgGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,2,11))
hpSwitchRunningCfgChgGroup.setObjects(*((_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:hpSwitchRunningCfgChgGroup.setStatus(_A)
hpSwitchBasicConfigGroup3=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,2,12))
hpSwitchBasicConfigGroup3.setObjects((_B,_AO))
if mibBuilder.loadTexts:hpSwitchBasicConfigGroup3.setStatus(_A)
hpSwitchCdpConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,2,13))
hpSwitchCdpConfigGroup.setObjects((_B,_AP))
if mibBuilder.loadTexts:hpSwitchCdpConfigGroup.setStatus(_A)
hpSwitchCdpPreStdVoiceGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,2,14))
hpSwitchCdpPreStdVoiceGroup.setObjects((_B,_AQ))
if mibBuilder.loadTexts:hpSwitchCdpPreStdVoiceGroup.setStatus(_A)
hpSwitchIgnoreUntagMacConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,2,15))
hpSwitchIgnoreUntagMacConfigGroup.setObjects((_B,_AR))
if mibBuilder.loadTexts:hpSwitchIgnoreUntagMacConfigGroup.setStatus(_A)
hpSwitchModuleConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,2,16))
hpSwitchModuleConfigGroup.setObjects((_B,_AS))
if mibBuilder.loadTexts:hpSwitchModuleConfigGroup.setStatus(_A)
hpSwitchBasicConfigGroup4=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,2,17))
hpSwitchBasicConfigGroup4.setObjects((_B,_AT))
if mibBuilder.loadTexts:hpSwitchBasicConfigGroup4.setStatus(_A)
hpSwitchAclGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,2,20))
hpSwitchAclGroup.setObjects(*((_B,_AU),(_B,_AV)))
if mibBuilder.loadTexts:hpSwitchAclGroup.setStatus(_A)
hpSwitchFPModuleGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,2,21))
hpSwitchFPModuleGroup.setObjects(*((_B,_AW),(_B,_AX)))
if mibBuilder.loadTexts:hpSwitchFPModuleGroup.setStatus(_A)
hpSwitchRESTInterfaceGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,2,22))
hpSwitchRESTInterfaceGroup.setObjects(*((_B,_AY),(_B,_AZ)))
if mibBuilder.loadTexts:hpSwitchRESTInterfaceGroup.setStatus(_A)
hpSwitchAclGroupingEnableGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,2,23))
hpSwitchAclGroupingEnableGroup.setObjects((_B,_Aa))
if mibBuilder.loadTexts:hpSwitchAclGroupingEnableGroup.setStatus(_A)
hpSwitchStartupConfigChange=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,0,6))
hpSwitchStartupConfigChange.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:hpSwitchStartupConfigChange.setStatus(_A)
hpSwitchRunningConfigChange=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,1,0,7))
hpSwitchRunningConfigChange.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:hpSwitchRunningConfigChange.setStatus(_A)
hpSwitchBasicNotificationGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,3,1))
hpSwitchBasicNotificationGroup.setObjects(*((_B,_Ab),(_B,_Ac)))
if mibBuilder.loadTexts:hpSwitchBasicNotificationGroup.setStatus(_A)
hpSwitchBasicConfigCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,1,1))
hpSwitchBasicConfigCompliance.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:hpSwitchBasicConfigCompliance.setStatus(_A)
hpSwitchBasicConfigCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,1,2))
hpSwitchBasicConfigCompliance2.setObjects((_B,_Ad))
if mibBuilder.loadTexts:hpSwitchBasicConfigCompliance2.setStatus(_A)
hpSwitchBasicConfigCompliance3=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,1,3))
hpSwitchBasicConfigCompliance3.setObjects((_B,_Ae))
if mibBuilder.loadTexts:hpSwitchBasicConfigCompliance3.setStatus(_A)
hpSwitchBasicConfigCompliance4=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,1,4))
hpSwitchBasicConfigCompliance4.setObjects((_B,_Af))
if mibBuilder.loadTexts:hpSwitchBasicConfigCompliance4.setStatus(_A)
hpSwitchBasicConfigCompliance5=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,1,5))
hpSwitchBasicConfigCompliance5.setObjects((_B,_Ag))
if mibBuilder.loadTexts:hpSwitchBasicConfigCompliance5.setStatus(_A)
hpSwitchBasicConfigCompliance6=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,1,6))
hpSwitchBasicConfigCompliance6.setObjects((_B,_Ah))
if mibBuilder.loadTexts:hpSwitchBasicConfigCompliance6.setStatus(_A)
hpSwitchBasicConfigCompliance7=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,1,7))
hpSwitchBasicConfigCompliance7.setObjects((_B,_Ai))
if mibBuilder.loadTexts:hpSwitchBasicConfigCompliance7.setStatus(_A)
hpSwitchBasicConfigCompliance8=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,1,8))
hpSwitchBasicConfigCompliance8.setObjects((_B,_Aj))
if mibBuilder.loadTexts:hpSwitchBasicConfigCompliance8.setStatus(_A)
hpSwitchBasicConfigCompliance10=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,1,10))
hpSwitchBasicConfigCompliance10.setObjects((_B,_Ak))
if mibBuilder.loadTexts:hpSwitchBasicConfigCompliance10.setStatus(_A)
hpSwitchBasicConfigCompliance11=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,1,11))
hpSwitchBasicConfigCompliance11.setObjects((_B,_Al))
if mibBuilder.loadTexts:hpSwitchBasicConfigCompliance11.setStatus(_A)
hpSwitchBasicConfigCompliance12=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,7,1,29,2,1,12))
hpSwitchBasicConfigCompliance12.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_Am)))
if mibBuilder.loadTexts:hpSwitchBasicConfigCompliance12.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfBridgeFilterConfigTable':hpicfBridgeFilterConfigTable,'hpicfBridgeFilterConfigEntry':hpicfBridgeFilterConfigEntry,_o:hpicfBridgeFilterName,_A2:hpicfBridgeFilterDropPortMask,_A3:hpicfBridgeFilterEntryStatus,'hpSwitchIgmpProxyDomainConfigTable':hpSwitchIgmpProxyDomainConfigTable,'hpSwitchIgmpProxyDomainConfigEntry':hpSwitchIgmpProxyDomainConfigEntry,_p:hpSwitchIgmpProxyDomainId,_A7:hpSwitchIgmpProxyDomainStatus,_A6:hpSwitchIgmpProxyDomainName,_A8:hpSwitchIgmpProxyDomainIp,_A9:hpSwitchIgmpProxyMcastLowerIp,_AA:hpSwitchIgmpProxyMcastUpperIp,'hpSwitchBasicConfigMIB':hpSwitchBasicConfigMIB,'hpSwitchBasicConfigObjects':hpSwitchBasicConfigObjects,'hpSwitchNotificationObjects':hpSwitchNotificationObjects,_Q:hpSwitchStartupConfigSource,_R:hpSwitchStartupConfigSourceIPAddrType,_S:hpSwitchStartupConfigSourceIPAddr,_T:hpSwitchStartupConfigSourceUsername,_U:hpSwitchStartupConfigThrottled,_Ac:hpSwitchStartupConfigChange,_Ab:hpSwitchRunningConfigChange,_x:hpSwitchSaveConfig,'hpSwitchAliasTable':hpSwitchAliasTable,'hpSwitchAliasEntry':hpSwitchAliasEntry,_r:hpSwitchAliasName,_A0:hpSwitchAliasCommand,_A1:hpSwitchAliasConfigRowStatus,'hpSwitchACLConfig':hpSwitchACLConfig,_A5:hpSwitchAclLogtimeoutConfig,_AU:hpSwitchAclIpv4DenyFragmentedTcpHeader,_AV:hpSwitchAclIpv6DenyNonClassifiableL4Header,_Aa:hpSwitchAclGroupingEnable,'hpicfPortCopyNameTable':hpicfPortCopyNameTable,_w:hpicfPortCopyNameEntry,_A4:hpicfPortCopyName,_y:hpSwitchDefaultLogon,'hpSwitchChassisLocateTable':hpSwitchChassisLocateTable,'hpSwitchChassisLocateEntry':hpSwitchChassisLocateEntry,_AB:hpSwitchChassisLocateState,_AC:hpSwitchChassisLocateDuration,_AD:hpSwitchChassisLocateWhen,'hpSwitchModules':hpSwitchModules,'hpSwitchModuleInfoTable':hpSwitchModuleInfoTable,'hpSwitchModuleInfoEntry':hpSwitchModuleInfoEntry,_t:hpSwitchModuleInfoModId,_AE:hpSwitchModuleInfoModType,'hpSwitchModuleConfigTable':hpSwitchModuleConfigTable,'hpSwitchModuleConfigEntry':hpSwitchModuleConfigEntry,_AF:hpSwitchModuleConfigModType,_AG:hpSwitchModuleConfigModName,_AS:hpSwitchModuleConfigModRemove,_z:hpSwitchWebSupportUrl,_P:hpSwitchStartupConfigSeqNum,_AH:hpSwitchStartupConfigNotifyEnable,_AI:hpSwitchImplicitConfigSave,'hpSwitchRunningCfgChgObjects':hpSwitchRunningCfgChgObjects,_AJ:hpSwitchRunningCfgChgNotifyEnable,_AK:hpSwitchRunningCfgChgTransmitInterval,_AL:hpSwitchRunningCfgChgLatestDateAndTime,_AM:hpSwitchRunningCfgChgCount,_AN:hpSwitchRunningCfgChgEntriesBumped,'hpSwitchRunningCfgChgEventTable':hpSwitchRunningCfgChgEventTable,'hpSwitchRunningCfgChgEventEntry':hpSwitchRunningCfgChgEventEntry,_u:hpSwitchRunningCfgChgEventTableIndex,_V:hpSwitchRunningCfgChgEventId,_W:hpSwitchRunningCfgChgEventMethod,_X:hpSwitchRunningCfgChgEventSourceIPAddrType,_Y:hpSwitchRunningCfgChgEventSourceIPAddr,_Z:hpSwitchRunningCfgChgEventUsername,_a:hpSwitchRunningCfgChgEventDateAndTime,_AO:hpSwitchSecureModeLevel,_AP:hpSwitchCdpRunMode,'hpSwitchCdpObjects':hpSwitchCdpObjects,'hpSwitchCdpPreStdVoiceTable':hpSwitchCdpPreStdVoiceTable,'hpSwitchCdpPreStdVoiceEntry':hpSwitchCdpPreStdVoiceEntry,_v:hpSwitchCdpPreStdVoiceIfIndex,_AQ:hpSwitchCdpPreStdVoiceStatus,_AR:hpSwitchIgnoreUntagMacPortList,_AT:hpSwitchControlPlaneProtectionAdminStatus,'hpSwitchFPModules':hpSwitchFPModules,'hpSwitchFPModuleConfigTable':hpSwitchFPModuleConfigTable,'hpSwitchFPModuleConfigEntry':hpSwitchFPModuleConfigEntry,_AW:hpSwitchFPModuleConfigType,_AX:hpSwitchFPModuleConfigName,_AY:hpSwitchRESTInterfaceStatus,_AZ:hpSwitchRESTSessionIdleTimeout,'hpSwitchBasicConfigConformance':hpSwitchBasicConfigConformance,'hpSwitchBasicConfigCompliances':hpSwitchBasicConfigCompliances,'hpSwitchBasicConfigCompliance':hpSwitchBasicConfigCompliance,'hpSwitchBasicConfigCompliance2':hpSwitchBasicConfigCompliance2,'hpSwitchBasicConfigCompliance3':hpSwitchBasicConfigCompliance3,'hpSwitchBasicConfigCompliance4':hpSwitchBasicConfigCompliance4,'hpSwitchBasicConfigCompliance5':hpSwitchBasicConfigCompliance5,'hpSwitchBasicConfigCompliance6':hpSwitchBasicConfigCompliance6,'hpSwitchBasicConfigCompliance7':hpSwitchBasicConfigCompliance7,'hpSwitchBasicConfigCompliance8':hpSwitchBasicConfigCompliance8,'hpSwitchBasicConfigCompliance10':hpSwitchBasicConfigCompliance10,'hpSwitchBasicConfigCompliance11':hpSwitchBasicConfigCompliance11,'hpSwitchBasicConfigCompliance12':hpSwitchBasicConfigCompliance12,'hpSwitchBasicConfigGroups':hpSwitchBasicConfigGroups,_b:hpSwitchBasicConfigGroup,_c:hpSwitchAliasGroup,_d:hpicfBridgeFilterConfigGroup,_e:hpicfPortCopyNameGroup,_f:hpSwitchAclLogtimeoutGroup,_g:hpSwitchIgmpProxyDomainConfigGroup,_h:hpSwitchChassisLocateGroup,_i:hpSwitchModuleGroup,_l:hpSwitchStartupConfigChangeGroup,_Ad:hpSwitchBasicConfigGroup2,_k:hpSwitchRunningCfgChgGroup,_Ae:hpSwitchBasicConfigGroup3,_Af:hpSwitchCdpConfigGroup,_Ag:hpSwitchCdpPreStdVoiceGroup,_Ah:hpSwitchIgnoreUntagMacConfigGroup,_Ai:hpSwitchModuleConfigGroup,_Aj:hpSwitchBasicConfigGroup4,_m:hpSwitchAclGroup,_Ak:hpSwitchFPModuleGroup,_Al:hpSwitchRESTInterfaceGroup,_Am:hpSwitchAclGroupingEnableGroup,'hpSwitchBasicNotificationGroups':hpSwitchBasicNotificationGroups,_j:hpSwitchBasicNotificationGroup})