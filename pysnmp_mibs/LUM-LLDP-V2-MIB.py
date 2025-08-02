_Am='lldpV2StatsReset'
_Al='lldpV2StatsUpPortId'
_Ak='lldpV2StatsClientIdx'
_Aj='lldpV2StatsIfNo'
_Ai='lldpV2StatsIdx'
_Ah='lldpV2StatsRxPort'
_Ag='lldpV2StatsTxPort'
_Af='lldpV2StatsSlot'
_Ae='lldpV2StatsSubrack'
_Ad='lldpV2StatsTLVSUnrecognizedTotal'
_Ac='lldpV2StatsTLVSDiscardedTotal'
_Ab='lldpV2StatsAgeOutsTotal'
_Aa='lldpV2StatsRxPortFramesTotal'
_AZ='lldpV2StatsRxPortFramesErrors'
_AY='lldpV2StatsRxPortFramesDiscardedTotal'
_AX='lldpV2StatsTxPortFramesTotal'
_AW='lldpV2StatsAgentId'
_AV='lldpV2StatsName'
_AU='lldpV2RemAgentId'
_AT='lldpV2RemUpPortId'
_AS='lldpV2RemIfNo'
_AR='lldpV2RemIdx'
_AQ='lldpV2RemRxPort'
_AP='lldpV2RemTxPort'
_AO='lldpV2RemSlot'
_AN='lldpV2RemSubrack'
_AM='lldpV2RemTTL'
_AL='lldpV2RemTimeout'
_AK='lldpV2RemUpTime'
_AJ='lldpV2RemLagisAggregated'
_AI='lldpV2RemLagisAggCapable'
_AH='lldpV2RemLagId'
_AG='lldpV2RemMtuSize'
_AF='lldpV2RemTooManyNeighbors'
_AE='lldpV2RemManAddrOID'
_AD='lldpV2RemManAddrIfId'
_AC='lldpV2RemManAddrIfSubtype'
_AB='lldpV2RemManAddr'
_AA='lldpV2RemManAddrSubtype'
_A9='lldpV2RemSysCapSupported'
_A8='lldpV2RemSysCapEnabled'
_A7='lldpV2RemSysDesc'
_A6='lldpV2RemSysName'
_A5='lldpV2RemPortDesc'
_A4='lldpV2RemPortId'
_A3='lldpV2RemPortIdSubtype'
_A2='lldpV2RemChassisId'
_A1='lldpV2RemChassisIdSubtype'
_A0='lldpV2RemSourceMACAddress'
_z='lldpV2RemLocalIfIndex'
_y='lldpV2RemName'
_x='lldpV2AgentConfigIfNo'
_w='lldpV2AgentConfigAgentId'
_v='lldpV2AgentConfigUpPort'
_u='lldpV2AgentConfigTxPort'
_t='lldpV2AgentConfigRxPort'
_s='lldpV2AgentConfigMessageTxInterval'
_r='lldpV2AgentConfigNotificationEnable'
_q='lldpV2AgentConfigAdminStatus'
_p='lldpV2AgentConfigLocalMacAddress'
_o='lldpV2AgentConfigName'
_n='lldpV2SystemInfoMaxNeighbors'
_m='lldpV2SystemInfoManagementOID'
_l='lldpV2SystemInfoManagementIp'
_k='lldpV2SystemInfoSystemDescription'
_j='lldpV2SystemInfoSystemMacAddress'
_i='lldpV2SystemInfoSystemName'
_h='lldpV2SystemInfoName'
_g='lldpV2StaticsTableSize'
_f='lldpV2RemSystemDataTableSize'
_e='lldpV2AgentConfigTableSize'
_d='lldpV2GeneralStateLastChangeTime'
_c='lldpV2GeneralConfigLastChangeTime'
_b='interfaceName'
_a='networkAddress'
_Z='macAddress'
_Y='portComponent'
_X='interfaceAlias'
_W='notApplicable'
_V='TruthValue'
_U='lldpV2StatsGroupV1'
_T='lldpV2RemoteSystemsDataGroupV1'
_S='lldpV2AgentConfigGroupV1'
_R='lldpV2SystemInfoGroupV1'
_Q='lldpV2GeneralGroupV1'
_P='lldpV2StatsIndex'
_O='lldpV2RemIndex'
_N='lldpV2AgentConfigIndex'
_M='lldpV2SystemInfoIndex'
_L='1x:'
_K='PortNumber'
_J='read-write'
_I='notAvailable'
_H='SnmpAdminString'
_G='OctetString'
_F='Integer32'
_E='Unsigned32'
_D='read-only'
_C='read-create'
_B='LUM-LLDP-V2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumLldpV2MIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumLldpV2MIB','lumModules')
MgmtNameString,PortNumber,SlotNumber,SubrackNumber,TruthValueWithNA=mibBuilder.importSymbols('LUM-TC','MgmtNameString',_K,'SlotNumber','SubrackNumber','TruthValueWithNA')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention',_V)
lumLldpV2MIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,67))
if mibBuilder.loadTexts:lumLldpV2MIBModule.setRevisions(('2017-12-15 00:00','2017-06-15 00:00','2016-04-30 00:00'))
class LumAddressFamilyNumbers(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,65535,2147483646,2147483647)));namedValues=NamedValues(*(('other',0),('ipV4',1),('ipV6',2),('nsap',3),('hdlc',4),('bbn1822',5),('all802',6),('e163',7),('e164',8),('f69',9),('x121',10),('ipx',11),('appleTalk',12),('decnetIV',13),('banyanVines',14),('e164withNsap',15),('dns',16),('distinguishedName',17),('asNumber',18),('xtpOverIpv4',19),('xtpOverIpv6',20),('xtpNativeModeXTP',21),('fibreChannelWWPN',22),('fibreChannelWWNN',23),('gwid',24),('reserved',65535),(_I,2147483646),(_W,2147483647)))
class LldpV2ChassisIdSubtype(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,2147483646)));namedValues=NamedValues(*(('chassisComponent',1),(_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6),('local',7),(_I,2147483646)))
class LldpV2ChassisId(TextualConvention,OctetString):status=_A;displayHint=_L;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
class LldpV2PortIdSubtype(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,2147483646)));namedValues=NamedValues(*((_X,1),(_Y,2),(_Z,3),(_a,4),(_b,5),('agentCircuitId',6),('local',7),(_I,2147483646)))
class LldpV2PortId(TextualConvention,OctetString):status=_A;displayHint=_L;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class LldpV2ManAddrIfSubtype(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,2147483646,2147483647)));namedValues=NamedValues(*(('unknown',1),('ifIndex',2),('systemPortNumber',3),(_I,2147483646),(_W,2147483647)))
class LldpV2ManAddress(TextualConvention,OctetString):status=_A;displayHint=_L;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,127))
_LumLldpV2Confs_ObjectIdentity=ObjectIdentity
lumLldpV2Confs=_LumLldpV2Confs_ObjectIdentity((1,3,6,1,4,1,8708,2,67,1))
_LumLldpV2Groups_ObjectIdentity=ObjectIdentity
lumLldpV2Groups=_LumLldpV2Groups_ObjectIdentity((1,3,6,1,4,1,8708,2,67,1,1))
_LumLldpV2Compliances_ObjectIdentity=ObjectIdentity
lumLldpV2Compliances=_LumLldpV2Compliances_ObjectIdentity((1,3,6,1,4,1,8708,2,67,1,2))
_LumLldpV2MIBObjects_ObjectIdentity=ObjectIdentity
lumLldpV2MIBObjects=_LumLldpV2MIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,67,2))
_LldpGeneral_ObjectIdentity=ObjectIdentity
lldpGeneral=_LldpGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,67,2,1))
_LldpV2GeneralConfigLastChangeTime_Type=DateAndTime
_LldpV2GeneralConfigLastChangeTime_Object=MibScalar
lldpV2GeneralConfigLastChangeTime=_LldpV2GeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,67,2,1,1),_LldpV2GeneralConfigLastChangeTime_Type())
lldpV2GeneralConfigLastChangeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2GeneralConfigLastChangeTime.setStatus(_A)
_LldpV2GeneralStateLastChangeTime_Type=DateAndTime
_LldpV2GeneralStateLastChangeTime_Object=MibScalar
lldpV2GeneralStateLastChangeTime=_LldpV2GeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,67,2,1,2),_LldpV2GeneralStateLastChangeTime_Type())
lldpV2GeneralStateLastChangeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2GeneralStateLastChangeTime.setStatus(_A)
_LldpV2SystemInfoTableSize_Type=Unsigned32
_LldpV2SystemInfoTableSize_Object=MibScalar
lldpV2SystemInfoTableSize=_LldpV2SystemInfoTableSize_Object((1,3,6,1,4,1,8708,2,67,2,1,3),_LldpV2SystemInfoTableSize_Type())
lldpV2SystemInfoTableSize.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2SystemInfoTableSize.setStatus(_A)
_LldpV2AgentConfigTableSize_Type=Unsigned32
_LldpV2AgentConfigTableSize_Object=MibScalar
lldpV2AgentConfigTableSize=_LldpV2AgentConfigTableSize_Object((1,3,6,1,4,1,8708,2,67,2,1,4),_LldpV2AgentConfigTableSize_Type())
lldpV2AgentConfigTableSize.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2AgentConfigTableSize.setStatus(_A)
_LldpV2RemSystemDataTableSize_Type=Unsigned32
_LldpV2RemSystemDataTableSize_Object=MibScalar
lldpV2RemSystemDataTableSize=_LldpV2RemSystemDataTableSize_Object((1,3,6,1,4,1,8708,2,67,2,1,5),_LldpV2RemSystemDataTableSize_Type())
lldpV2RemSystemDataTableSize.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2RemSystemDataTableSize.setStatus(_A)
_LldpV2StaticsTableSize_Type=Unsigned32
_LldpV2StaticsTableSize_Object=MibScalar
lldpV2StaticsTableSize=_LldpV2StaticsTableSize_Object((1,3,6,1,4,1,8708,2,67,2,1,6),_LldpV2StaticsTableSize_Type())
lldpV2StaticsTableSize.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2StaticsTableSize.setStatus(_A)
_LldpV2SystemInfo_ObjectIdentity=ObjectIdentity
lldpV2SystemInfo=_LldpV2SystemInfo_ObjectIdentity((1,3,6,1,4,1,8708,2,67,2,2))
_LldpV2SystemInfoTable_Object=MibTable
lldpV2SystemInfoTable=_LldpV2SystemInfoTable_Object((1,3,6,1,4,1,8708,2,67,2,2,1))
if mibBuilder.loadTexts:lldpV2SystemInfoTable.setStatus(_A)
_LldpV2SystemInfoEntry_Object=MibTableRow
lldpV2SystemInfoEntry=_LldpV2SystemInfoEntry_Object((1,3,6,1,4,1,8708,2,67,2,2,1,1))
lldpV2SystemInfoEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:lldpV2SystemInfoEntry.setStatus(_A)
class _LldpV2SystemInfoIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LldpV2SystemInfoIndex_Type.__name__=_E
_LldpV2SystemInfoIndex_Object=MibTableColumn
lldpV2SystemInfoIndex=_LldpV2SystemInfoIndex_Object((1,3,6,1,4,1,8708,2,67,2,2,1,1,1),_LldpV2SystemInfoIndex_Type())
lldpV2SystemInfoIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2SystemInfoIndex.setStatus(_A)
_LldpV2SystemInfoName_Type=MgmtNameString
_LldpV2SystemInfoName_Object=MibTableColumn
lldpV2SystemInfoName=_LldpV2SystemInfoName_Object((1,3,6,1,4,1,8708,2,67,2,2,1,1,2),_LldpV2SystemInfoName_Type())
lldpV2SystemInfoName.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2SystemInfoName.setStatus(_A)
_LldpV2SystemInfoSystemName_Type=MgmtNameString
_LldpV2SystemInfoSystemName_Object=MibTableColumn
lldpV2SystemInfoSystemName=_LldpV2SystemInfoSystemName_Object((1,3,6,1,4,1,8708,2,67,2,2,1,1,3),_LldpV2SystemInfoSystemName_Type())
lldpV2SystemInfoSystemName.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2SystemInfoSystemName.setStatus(_A)
_LldpV2SystemInfoSystemDescription_Type=DisplayString
_LldpV2SystemInfoSystemDescription_Object=MibTableColumn
lldpV2SystemInfoSystemDescription=_LldpV2SystemInfoSystemDescription_Object((1,3,6,1,4,1,8708,2,67,2,2,1,1,4),_LldpV2SystemInfoSystemDescription_Type())
lldpV2SystemInfoSystemDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2SystemInfoSystemDescription.setStatus(_A)
class _LldpV2SystemInfoSystemMacAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_LldpV2SystemInfoSystemMacAddress_Type.__name__=_G
_LldpV2SystemInfoSystemMacAddress_Object=MibTableColumn
lldpV2SystemInfoSystemMacAddress=_LldpV2SystemInfoSystemMacAddress_Object((1,3,6,1,4,1,8708,2,67,2,2,1,1,5),_LldpV2SystemInfoSystemMacAddress_Type())
lldpV2SystemInfoSystemMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2SystemInfoSystemMacAddress.setStatus(_A)
_LldpV2SystemInfoManagementIp_Type=IpAddress
_LldpV2SystemInfoManagementIp_Object=MibTableColumn
lldpV2SystemInfoManagementIp=_LldpV2SystemInfoManagementIp_Object((1,3,6,1,4,1,8708,2,67,2,2,1,1,6),_LldpV2SystemInfoManagementIp_Type())
lldpV2SystemInfoManagementIp.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2SystemInfoManagementIp.setStatus(_A)
class _LldpV2SystemInfoManagementOID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,127))
_LldpV2SystemInfoManagementOID_Type.__name__=_G
_LldpV2SystemInfoManagementOID_Object=MibTableColumn
lldpV2SystemInfoManagementOID=_LldpV2SystemInfoManagementOID_Object((1,3,6,1,4,1,8708,2,67,2,2,1,1,7),_LldpV2SystemInfoManagementOID_Type())
lldpV2SystemInfoManagementOID.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2SystemInfoManagementOID.setStatus(_A)
class _LldpV2SystemInfoMaxNeighbors_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_LldpV2SystemInfoMaxNeighbors_Type.__name__=_E
_LldpV2SystemInfoMaxNeighbors_Object=MibTableColumn
lldpV2SystemInfoMaxNeighbors=_LldpV2SystemInfoMaxNeighbors_Object((1,3,6,1,4,1,8708,2,67,2,2,1,1,8),_LldpV2SystemInfoMaxNeighbors_Type())
lldpV2SystemInfoMaxNeighbors.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2SystemInfoMaxNeighbors.setStatus(_A)
_LldpV2AgentConfig_ObjectIdentity=ObjectIdentity
lldpV2AgentConfig=_LldpV2AgentConfig_ObjectIdentity((1,3,6,1,4,1,8708,2,67,2,3))
_LldpV2AgentConfigTable_Object=MibTable
lldpV2AgentConfigTable=_LldpV2AgentConfigTable_Object((1,3,6,1,4,1,8708,2,67,2,3,1))
if mibBuilder.loadTexts:lldpV2AgentConfigTable.setStatus(_A)
_LldpV2AgentConfigEntry_Object=MibTableRow
lldpV2AgentConfigEntry=_LldpV2AgentConfigEntry_Object((1,3,6,1,4,1,8708,2,67,2,3,1,1))
lldpV2AgentConfigEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:lldpV2AgentConfigEntry.setStatus(_A)
class _LldpV2AgentConfigIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LldpV2AgentConfigIndex_Type.__name__=_E
_LldpV2AgentConfigIndex_Object=MibTableColumn
lldpV2AgentConfigIndex=_LldpV2AgentConfigIndex_Object((1,3,6,1,4,1,8708,2,67,2,3,1,1,1),_LldpV2AgentConfigIndex_Type())
lldpV2AgentConfigIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2AgentConfigIndex.setStatus(_A)
_LldpV2AgentConfigName_Type=MgmtNameString
_LldpV2AgentConfigName_Object=MibTableColumn
lldpV2AgentConfigName=_LldpV2AgentConfigName_Object((1,3,6,1,4,1,8708,2,67,2,3,1,1,2),_LldpV2AgentConfigName_Type())
lldpV2AgentConfigName.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2AgentConfigName.setStatus(_A)
class _LldpV2AgentConfigLocalMacAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_LldpV2AgentConfigLocalMacAddress_Type.__name__=_G
_LldpV2AgentConfigLocalMacAddress_Object=MibTableColumn
lldpV2AgentConfigLocalMacAddress=_LldpV2AgentConfigLocalMacAddress_Object((1,3,6,1,4,1,8708,2,67,2,3,1,1,3),_LldpV2AgentConfigLocalMacAddress_Type())
lldpV2AgentConfigLocalMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2AgentConfigLocalMacAddress.setStatus(_A)
class _LldpV2AgentConfigDestMacAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_LldpV2AgentConfigDestMacAddress_Type.__name__=_G
_LldpV2AgentConfigDestMacAddress_Object=MibTableColumn
lldpV2AgentConfigDestMacAddress=_LldpV2AgentConfigDestMacAddress_Object((1,3,6,1,4,1,8708,2,67,2,3,1,1,4),_LldpV2AgentConfigDestMacAddress_Type())
lldpV2AgentConfigDestMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2AgentConfigDestMacAddress.setStatus(_A)
class _LldpV2AgentConfigAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('txAndRx',2)))
_LldpV2AgentConfigAdminStatus_Type.__name__=_F
_LldpV2AgentConfigAdminStatus_Object=MibTableColumn
lldpV2AgentConfigAdminStatus=_LldpV2AgentConfigAdminStatus_Object((1,3,6,1,4,1,8708,2,67,2,3,1,1,5),_LldpV2AgentConfigAdminStatus_Type())
lldpV2AgentConfigAdminStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:lldpV2AgentConfigAdminStatus.setStatus(_A)
class _LldpV2AgentConfigNotificationEnable_Type(TruthValue):defaultValue=2
_LldpV2AgentConfigNotificationEnable_Type.__name__=_V
_LldpV2AgentConfigNotificationEnable_Object=MibTableColumn
lldpV2AgentConfigNotificationEnable=_LldpV2AgentConfigNotificationEnable_Object((1,3,6,1,4,1,8708,2,67,2,3,1,1,6),_LldpV2AgentConfigNotificationEnable_Type())
lldpV2AgentConfigNotificationEnable.setMaxAccess(_J)
if mibBuilder.loadTexts:lldpV2AgentConfigNotificationEnable.setStatus(_A)
class _LldpV2AgentConfigMessageTxInterval_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_LldpV2AgentConfigMessageTxInterval_Type.__name__=_E
_LldpV2AgentConfigMessageTxInterval_Object=MibTableColumn
lldpV2AgentConfigMessageTxInterval=_LldpV2AgentConfigMessageTxInterval_Object((1,3,6,1,4,1,8708,2,67,2,3,1,1,7),_LldpV2AgentConfigMessageTxInterval_Type())
lldpV2AgentConfigMessageTxInterval.setMaxAccess(_J)
if mibBuilder.loadTexts:lldpV2AgentConfigMessageTxInterval.setStatus(_A)
_LldpV2AgentConfigRxPort_Type=PortNumber
_LldpV2AgentConfigRxPort_Object=MibTableColumn
lldpV2AgentConfigRxPort=_LldpV2AgentConfigRxPort_Object((1,3,6,1,4,1,8708,2,67,2,3,1,1,8),_LldpV2AgentConfigRxPort_Type())
lldpV2AgentConfigRxPort.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2AgentConfigRxPort.setStatus(_A)
_LldpV2AgentConfigTxPort_Type=PortNumber
_LldpV2AgentConfigTxPort_Object=MibTableColumn
lldpV2AgentConfigTxPort=_LldpV2AgentConfigTxPort_Object((1,3,6,1,4,1,8708,2,67,2,3,1,1,9),_LldpV2AgentConfigTxPort_Type())
lldpV2AgentConfigTxPort.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2AgentConfigTxPort.setStatus(_A)
class _LldpV2AgentConfigUpPort_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_LldpV2AgentConfigUpPort_Type.__name__=_F
_LldpV2AgentConfigUpPort_Object=MibTableColumn
lldpV2AgentConfigUpPort=_LldpV2AgentConfigUpPort_Object((1,3,6,1,4,1,8708,2,67,2,3,1,1,10),_LldpV2AgentConfigUpPort_Type())
lldpV2AgentConfigUpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2AgentConfigUpPort.setStatus(_A)
class _LldpV2AgentConfigAgentId_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_LldpV2AgentConfigAgentId_Type.__name__=_F
_LldpV2AgentConfigAgentId_Object=MibTableColumn
lldpV2AgentConfigAgentId=_LldpV2AgentConfigAgentId_Object((1,3,6,1,4,1,8708,2,67,2,3,1,1,11),_LldpV2AgentConfigAgentId_Type())
lldpV2AgentConfigAgentId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2AgentConfigAgentId.setStatus(_A)
_LldpV2AgentConfigIfNo_Type=PortNumber
_LldpV2AgentConfigIfNo_Object=MibTableColumn
lldpV2AgentConfigIfNo=_LldpV2AgentConfigIfNo_Object((1,3,6,1,4,1,8708,2,67,2,3,1,1,12),_LldpV2AgentConfigIfNo_Type())
lldpV2AgentConfigIfNo.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2AgentConfigIfNo.setStatus(_A)
class _LldpV2AgentConfigPortDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_LldpV2AgentConfigPortDesc_Type.__name__=_H
_LldpV2AgentConfigPortDesc_Object=MibTableColumn
lldpV2AgentConfigPortDesc=_LldpV2AgentConfigPortDesc_Object((1,3,6,1,4,1,8708,2,67,2,3,1,1,13),_LldpV2AgentConfigPortDesc_Type())
lldpV2AgentConfigPortDesc.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2AgentConfigPortDesc.setStatus(_A)
_LldpV2RemoteSystemData_ObjectIdentity=ObjectIdentity
lldpV2RemoteSystemData=_LldpV2RemoteSystemData_ObjectIdentity((1,3,6,1,4,1,8708,2,67,2,4))
_LldpV2RemTable_Object=MibTable
lldpV2RemTable=_LldpV2RemTable_Object((1,3,6,1,4,1,8708,2,67,2,4,1))
if mibBuilder.loadTexts:lldpV2RemTable.setStatus(_A)
_LldpV2RemEntry_Object=MibTableRow
lldpV2RemEntry=_LldpV2RemEntry_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1))
lldpV2RemEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:lldpV2RemEntry.setStatus(_A)
class _LldpV2RemIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LldpV2RemIndex_Type.__name__=_E
_LldpV2RemIndex_Object=MibTableColumn
lldpV2RemIndex=_LldpV2RemIndex_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,1),_LldpV2RemIndex_Type())
lldpV2RemIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2RemIndex.setStatus(_A)
_LldpV2RemName_Type=MgmtNameString
_LldpV2RemName_Object=MibTableColumn
lldpV2RemName=_LldpV2RemName_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,2),_LldpV2RemName_Type())
lldpV2RemName.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemName.setStatus(_A)
class _LldpV2RemLocalIfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LldpV2RemLocalIfIndex_Type.__name__=_E
_LldpV2RemLocalIfIndex_Object=MibTableColumn
lldpV2RemLocalIfIndex=_LldpV2RemLocalIfIndex_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,3),_LldpV2RemLocalIfIndex_Type())
lldpV2RemLocalIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemLocalIfIndex.setStatus(_A)
class _LldpV2RemSourceMACAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_LldpV2RemSourceMACAddress_Type.__name__=_G
_LldpV2RemSourceMACAddress_Object=MibTableColumn
lldpV2RemSourceMACAddress=_LldpV2RemSourceMACAddress_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,4),_LldpV2RemSourceMACAddress_Type())
lldpV2RemSourceMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemSourceMACAddress.setStatus(_A)
_LldpV2RemChassisIdSubtype_Type=LldpV2ChassisIdSubtype
_LldpV2RemChassisIdSubtype_Object=MibTableColumn
lldpV2RemChassisIdSubtype=_LldpV2RemChassisIdSubtype_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,5),_LldpV2RemChassisIdSubtype_Type())
lldpV2RemChassisIdSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemChassisIdSubtype.setStatus(_A)
_LldpV2RemChassisId_Type=LldpV2ChassisId
_LldpV2RemChassisId_Object=MibTableColumn
lldpV2RemChassisId=_LldpV2RemChassisId_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,6),_LldpV2RemChassisId_Type())
lldpV2RemChassisId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemChassisId.setStatus(_A)
_LldpV2RemPortIdSubtype_Type=LldpV2PortIdSubtype
_LldpV2RemPortIdSubtype_Object=MibTableColumn
lldpV2RemPortIdSubtype=_LldpV2RemPortIdSubtype_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,7),_LldpV2RemPortIdSubtype_Type())
lldpV2RemPortIdSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemPortIdSubtype.setStatus(_A)
_LldpV2RemPortId_Type=LldpV2PortId
_LldpV2RemPortId_Object=MibTableColumn
lldpV2RemPortId=_LldpV2RemPortId_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,8),_LldpV2RemPortId_Type())
lldpV2RemPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemPortId.setStatus(_A)
class _LldpV2RemPortDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_LldpV2RemPortDesc_Type.__name__=_H
_LldpV2RemPortDesc_Object=MibTableColumn
lldpV2RemPortDesc=_LldpV2RemPortDesc_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,9),_LldpV2RemPortDesc_Type())
lldpV2RemPortDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemPortDesc.setStatus(_A)
class _LldpV2RemSysName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpV2RemSysName_Type.__name__=_H
_LldpV2RemSysName_Object=MibTableColumn
lldpV2RemSysName=_LldpV2RemSysName_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,10),_LldpV2RemSysName_Type())
lldpV2RemSysName.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemSysName.setStatus(_A)
class _LldpV2RemSysDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpV2RemSysDesc_Type.__name__=_H
_LldpV2RemSysDesc_Object=MibTableColumn
lldpV2RemSysDesc=_LldpV2RemSysDesc_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,11),_LldpV2RemSysDesc_Type())
lldpV2RemSysDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemSysDesc.setStatus(_A)
class _LldpV2RemSysCapEnabled_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_LldpV2RemSysCapEnabled_Type.__name__=_G
_LldpV2RemSysCapEnabled_Object=MibTableColumn
lldpV2RemSysCapEnabled=_LldpV2RemSysCapEnabled_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,12),_LldpV2RemSysCapEnabled_Type())
lldpV2RemSysCapEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemSysCapEnabled.setStatus(_A)
class _LldpV2RemSysCapSupported_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_LldpV2RemSysCapSupported_Type.__name__=_G
_LldpV2RemSysCapSupported_Object=MibTableColumn
lldpV2RemSysCapSupported=_LldpV2RemSysCapSupported_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,13),_LldpV2RemSysCapSupported_Type())
lldpV2RemSysCapSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemSysCapSupported.setStatus(_A)
_LldpV2RemManAddrSubtype_Type=LumAddressFamilyNumbers
_LldpV2RemManAddrSubtype_Object=MibTableColumn
lldpV2RemManAddrSubtype=_LldpV2RemManAddrSubtype_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,14),_LldpV2RemManAddrSubtype_Type())
lldpV2RemManAddrSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemManAddrSubtype.setStatus(_A)
_LldpV2RemManAddr_Type=LldpV2ManAddress
_LldpV2RemManAddr_Object=MibTableColumn
lldpV2RemManAddr=_LldpV2RemManAddr_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,15),_LldpV2RemManAddr_Type())
lldpV2RemManAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemManAddr.setStatus(_A)
_LldpV2RemManAddrIfSubtype_Type=LldpV2ManAddrIfSubtype
_LldpV2RemManAddrIfSubtype_Object=MibTableColumn
lldpV2RemManAddrIfSubtype=_LldpV2RemManAddrIfSubtype_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,16),_LldpV2RemManAddrIfSubtype_Type())
lldpV2RemManAddrIfSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemManAddrIfSubtype.setStatus(_A)
class _LldpV2RemManAddrIfId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483644),ValueRangeConstraint(2147483646,2147483646),ValueRangeConstraint(2147483647,2147483647))
_LldpV2RemManAddrIfId_Type.__name__=_E
_LldpV2RemManAddrIfId_Object=MibTableColumn
lldpV2RemManAddrIfId=_LldpV2RemManAddrIfId_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,17),_LldpV2RemManAddrIfId_Type())
lldpV2RemManAddrIfId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemManAddrIfId.setStatus(_A)
class _LldpV2RemManAddrOID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_LldpV2RemManAddrOID_Type.__name__=_G
_LldpV2RemManAddrOID_Object=MibTableColumn
lldpV2RemManAddrOID=_LldpV2RemManAddrOID_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,18),_LldpV2RemManAddrOID_Type())
lldpV2RemManAddrOID.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemManAddrOID.setStatus(_A)
_LldpV2RemTooManyNeighbors_Type=TruthValue
_LldpV2RemTooManyNeighbors_Object=MibTableColumn
lldpV2RemTooManyNeighbors=_LldpV2RemTooManyNeighbors_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,19),_LldpV2RemTooManyNeighbors_Type())
lldpV2RemTooManyNeighbors.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemTooManyNeighbors.setStatus(_A)
class _LldpV2RemMtuSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_LldpV2RemMtuSize_Type.__name__=_E
_LldpV2RemMtuSize_Object=MibTableColumn
lldpV2RemMtuSize=_LldpV2RemMtuSize_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,20),_LldpV2RemMtuSize_Type())
lldpV2RemMtuSize.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemMtuSize.setStatus(_A)
class _LldpV2RemLagId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_LldpV2RemLagId_Type.__name__=_E
_LldpV2RemLagId_Object=MibTableColumn
lldpV2RemLagId=_LldpV2RemLagId_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,21),_LldpV2RemLagId_Type())
lldpV2RemLagId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemLagId.setStatus(_A)
_LldpV2RemLagisAggCapable_Type=TruthValueWithNA
_LldpV2RemLagisAggCapable_Object=MibTableColumn
lldpV2RemLagisAggCapable=_LldpV2RemLagisAggCapable_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,22),_LldpV2RemLagisAggCapable_Type())
lldpV2RemLagisAggCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemLagisAggCapable.setStatus(_A)
_LldpV2RemLagisAggregated_Type=TruthValueWithNA
_LldpV2RemLagisAggregated_Object=MibTableColumn
lldpV2RemLagisAggregated=_LldpV2RemLagisAggregated_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,23),_LldpV2RemLagisAggregated_Type())
lldpV2RemLagisAggregated.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemLagisAggregated.setStatus(_A)
class _LldpV2RemUpTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LldpV2RemUpTime_Type.__name__=_E
_LldpV2RemUpTime_Object=MibTableColumn
lldpV2RemUpTime=_LldpV2RemUpTime_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,24),_LldpV2RemUpTime_Type())
lldpV2RemUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemUpTime.setStatus(_A)
class _LldpV2RemTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LldpV2RemTimeout_Type.__name__=_E
_LldpV2RemTimeout_Object=MibTableColumn
lldpV2RemTimeout=_LldpV2RemTimeout_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,25),_LldpV2RemTimeout_Type())
lldpV2RemTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemTimeout.setStatus(_A)
class _LldpV2RemTTL_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LldpV2RemTTL_Type.__name__=_E
_LldpV2RemTTL_Object=MibTableColumn
lldpV2RemTTL=_LldpV2RemTTL_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,26),_LldpV2RemTTL_Type())
lldpV2RemTTL.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemTTL.setStatus(_A)
_LldpV2RemSubrack_Type=SubrackNumber
_LldpV2RemSubrack_Object=MibTableColumn
lldpV2RemSubrack=_LldpV2RemSubrack_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,27),_LldpV2RemSubrack_Type())
lldpV2RemSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemSubrack.setStatus(_A)
_LldpV2RemSlot_Type=SlotNumber
_LldpV2RemSlot_Object=MibTableColumn
lldpV2RemSlot=_LldpV2RemSlot_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,28),_LldpV2RemSlot_Type())
lldpV2RemSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemSlot.setStatus(_A)
_LldpV2RemTxPort_Type=PortNumber
_LldpV2RemTxPort_Object=MibTableColumn
lldpV2RemTxPort=_LldpV2RemTxPort_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,29),_LldpV2RemTxPort_Type())
lldpV2RemTxPort.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemTxPort.setStatus(_A)
_LldpV2RemRxPort_Type=PortNumber
_LldpV2RemRxPort_Object=MibTableColumn
lldpV2RemRxPort=_LldpV2RemRxPort_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,30),_LldpV2RemRxPort_Type())
lldpV2RemRxPort.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemRxPort.setStatus(_A)
class _LldpV2RemIdx_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_LldpV2RemIdx_Type.__name__=_F
_LldpV2RemIdx_Object=MibTableColumn
lldpV2RemIdx=_LldpV2RemIdx_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,31),_LldpV2RemIdx_Type())
lldpV2RemIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemIdx.setStatus(_A)
class _LldpV2RemIfNo_Type(PortNumber):defaultValue=1
_LldpV2RemIfNo_Type.__name__=_K
_LldpV2RemIfNo_Object=MibTableColumn
lldpV2RemIfNo=_LldpV2RemIfNo_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,32),_LldpV2RemIfNo_Type())
lldpV2RemIfNo.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemIfNo.setStatus(_A)
class _LldpV2RemUpPortId_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_LldpV2RemUpPortId_Type.__name__=_F
_LldpV2RemUpPortId_Object=MibTableColumn
lldpV2RemUpPortId=_LldpV2RemUpPortId_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,33),_LldpV2RemUpPortId_Type())
lldpV2RemUpPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemUpPortId.setStatus(_A)
class _LldpV2RemAgentId_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_LldpV2RemAgentId_Type.__name__=_F
_LldpV2RemAgentId_Object=MibTableColumn
lldpV2RemAgentId=_LldpV2RemAgentId_Object((1,3,6,1,4,1,8708,2,67,2,4,1,1,34),_LldpV2RemAgentId_Type())
lldpV2RemAgentId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemAgentId.setStatus(_A)
_LldpV2Statistics_ObjectIdentity=ObjectIdentity
lldpV2Statistics=_LldpV2Statistics_ObjectIdentity((1,3,6,1,4,1,8708,2,67,2,5))
_LldpV2StatsTable_Object=MibTable
lldpV2StatsTable=_LldpV2StatsTable_Object((1,3,6,1,4,1,8708,2,67,2,5,1))
if mibBuilder.loadTexts:lldpV2StatsTable.setStatus(_A)
_LldpV2StatsEntry_Object=MibTableRow
lldpV2StatsEntry=_LldpV2StatsEntry_Object((1,3,6,1,4,1,8708,2,67,2,5,1,1))
lldpV2StatsEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:lldpV2StatsEntry.setStatus(_A)
class _LldpV2StatsIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LldpV2StatsIndex_Type.__name__=_E
_LldpV2StatsIndex_Object=MibTableColumn
lldpV2StatsIndex=_LldpV2StatsIndex_Object((1,3,6,1,4,1,8708,2,67,2,5,1,1,1),_LldpV2StatsIndex_Type())
lldpV2StatsIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2StatsIndex.setStatus(_A)
class _LldpV2StatsAgentId_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_LldpV2StatsAgentId_Type.__name__=_F
_LldpV2StatsAgentId_Object=MibTableColumn
lldpV2StatsAgentId=_LldpV2StatsAgentId_Object((1,3,6,1,4,1,8708,2,67,2,5,1,1,2),_LldpV2StatsAgentId_Type())
lldpV2StatsAgentId.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2StatsAgentId.setStatus(_A)
_LldpV2StatsName_Type=MgmtNameString
_LldpV2StatsName_Object=MibTableColumn
lldpV2StatsName=_LldpV2StatsName_Object((1,3,6,1,4,1,8708,2,67,2,5,1,1,3),_LldpV2StatsName_Type())
lldpV2StatsName.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2StatsName.setStatus(_A)
_LldpV2StatsTxPortFramesTotal_Type=Counter32
_LldpV2StatsTxPortFramesTotal_Object=MibTableColumn
lldpV2StatsTxPortFramesTotal=_LldpV2StatsTxPortFramesTotal_Object((1,3,6,1,4,1,8708,2,67,2,5,1,1,4),_LldpV2StatsTxPortFramesTotal_Type())
lldpV2StatsTxPortFramesTotal.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2StatsTxPortFramesTotal.setStatus(_A)
_LldpV2StatsRxPortFramesDiscardedTotal_Type=Counter32
_LldpV2StatsRxPortFramesDiscardedTotal_Object=MibTableColumn
lldpV2StatsRxPortFramesDiscardedTotal=_LldpV2StatsRxPortFramesDiscardedTotal_Object((1,3,6,1,4,1,8708,2,67,2,5,1,1,5),_LldpV2StatsRxPortFramesDiscardedTotal_Type())
lldpV2StatsRxPortFramesDiscardedTotal.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2StatsRxPortFramesDiscardedTotal.setStatus(_A)
_LldpV2StatsRxPortFramesErrors_Type=Counter32
_LldpV2StatsRxPortFramesErrors_Object=MibTableColumn
lldpV2StatsRxPortFramesErrors=_LldpV2StatsRxPortFramesErrors_Object((1,3,6,1,4,1,8708,2,67,2,5,1,1,6),_LldpV2StatsRxPortFramesErrors_Type())
lldpV2StatsRxPortFramesErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2StatsRxPortFramesErrors.setStatus(_A)
_LldpV2StatsRxPortFramesTotal_Type=Counter32
_LldpV2StatsRxPortFramesTotal_Object=MibTableColumn
lldpV2StatsRxPortFramesTotal=_LldpV2StatsRxPortFramesTotal_Object((1,3,6,1,4,1,8708,2,67,2,5,1,1,7),_LldpV2StatsRxPortFramesTotal_Type())
lldpV2StatsRxPortFramesTotal.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2StatsRxPortFramesTotal.setStatus(_A)
_LldpV2StatsAgeOutsTotal_Type=Counter32
_LldpV2StatsAgeOutsTotal_Object=MibTableColumn
lldpV2StatsAgeOutsTotal=_LldpV2StatsAgeOutsTotal_Object((1,3,6,1,4,1,8708,2,67,2,5,1,1,8),_LldpV2StatsAgeOutsTotal_Type())
lldpV2StatsAgeOutsTotal.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2StatsAgeOutsTotal.setStatus(_A)
_LldpV2StatsTLVSDiscardedTotal_Type=Counter32
_LldpV2StatsTLVSDiscardedTotal_Object=MibTableColumn
lldpV2StatsTLVSDiscardedTotal=_LldpV2StatsTLVSDiscardedTotal_Object((1,3,6,1,4,1,8708,2,67,2,5,1,1,9),_LldpV2StatsTLVSDiscardedTotal_Type())
lldpV2StatsTLVSDiscardedTotal.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2StatsTLVSDiscardedTotal.setStatus(_A)
_LldpV2StatsTLVSUnrecognizedTotal_Type=Counter32
_LldpV2StatsTLVSUnrecognizedTotal_Object=MibTableColumn
lldpV2StatsTLVSUnrecognizedTotal=_LldpV2StatsTLVSUnrecognizedTotal_Object((1,3,6,1,4,1,8708,2,67,2,5,1,1,10),_LldpV2StatsTLVSUnrecognizedTotal_Type())
lldpV2StatsTLVSUnrecognizedTotal.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2StatsTLVSUnrecognizedTotal.setStatus(_A)
_LldpV2StatsSubrack_Type=SubrackNumber
_LldpV2StatsSubrack_Object=MibTableColumn
lldpV2StatsSubrack=_LldpV2StatsSubrack_Object((1,3,6,1,4,1,8708,2,67,2,5,1,1,11),_LldpV2StatsSubrack_Type())
lldpV2StatsSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2StatsSubrack.setStatus(_A)
_LldpV2StatsSlot_Type=SlotNumber
_LldpV2StatsSlot_Object=MibTableColumn
lldpV2StatsSlot=_LldpV2StatsSlot_Object((1,3,6,1,4,1,8708,2,67,2,5,1,1,12),_LldpV2StatsSlot_Type())
lldpV2StatsSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2StatsSlot.setStatus(_A)
_LldpV2StatsTxPort_Type=PortNumber
_LldpV2StatsTxPort_Object=MibTableColumn
lldpV2StatsTxPort=_LldpV2StatsTxPort_Object((1,3,6,1,4,1,8708,2,67,2,5,1,1,13),_LldpV2StatsTxPort_Type())
lldpV2StatsTxPort.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2StatsTxPort.setStatus(_A)
_LldpV2StatsRxPort_Type=PortNumber
_LldpV2StatsRxPort_Object=MibTableColumn
lldpV2StatsRxPort=_LldpV2StatsRxPort_Object((1,3,6,1,4,1,8708,2,67,2,5,1,1,14),_LldpV2StatsRxPort_Type())
lldpV2StatsRxPort.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2StatsRxPort.setStatus(_A)
class _LldpV2StatsIdx_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_LldpV2StatsIdx_Type.__name__=_F
_LldpV2StatsIdx_Object=MibTableColumn
lldpV2StatsIdx=_LldpV2StatsIdx_Object((1,3,6,1,4,1,8708,2,67,2,5,1,1,15),_LldpV2StatsIdx_Type())
lldpV2StatsIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2StatsIdx.setStatus(_A)
class _LldpV2StatsIfNo_Type(PortNumber):defaultValue=1
_LldpV2StatsIfNo_Type.__name__=_K
_LldpV2StatsIfNo_Object=MibTableColumn
lldpV2StatsIfNo=_LldpV2StatsIfNo_Object((1,3,6,1,4,1,8708,2,67,2,5,1,1,16),_LldpV2StatsIfNo_Type())
lldpV2StatsIfNo.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2StatsIfNo.setStatus(_A)
class _LldpV2StatsClientIdx_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_LldpV2StatsClientIdx_Type.__name__=_F
_LldpV2StatsClientIdx_Object=MibTableColumn
lldpV2StatsClientIdx=_LldpV2StatsClientIdx_Object((1,3,6,1,4,1,8708,2,67,2,5,1,1,17),_LldpV2StatsClientIdx_Type())
lldpV2StatsClientIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2StatsClientIdx.setStatus(_A)
class _LldpV2StatsUpPortId_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_LldpV2StatsUpPortId_Type.__name__=_F
_LldpV2StatsUpPortId_Object=MibTableColumn
lldpV2StatsUpPortId=_LldpV2StatsUpPortId_Object((1,3,6,1,4,1,8708,2,67,2,5,1,1,18),_LldpV2StatsUpPortId_Type())
lldpV2StatsUpPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2StatsUpPortId.setStatus(_A)
class _LldpV2StatsReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('reset',2)))
_LldpV2StatsReset_Type.__name__=_F
_LldpV2StatsReset_Object=MibTableColumn
lldpV2StatsReset=_LldpV2StatsReset_Object((1,3,6,1,4,1,8708,2,67,2,5,1,1,19),_LldpV2StatsReset_Type())
lldpV2StatsReset.setMaxAccess(_J)
if mibBuilder.loadTexts:lldpV2StatsReset.setStatus(_A)
lldpV2GeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,67,1,1,1))
lldpV2GeneralGroupV1.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:lldpV2GeneralGroupV1.setStatus(_A)
lldpV2SystemInfoGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,67,1,1,2))
lldpV2SystemInfoGroupV1.setObjects(*((_B,_M),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:lldpV2SystemInfoGroupV1.setStatus(_A)
lldpV2AgentConfigGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,67,1,1,3))
lldpV2AgentConfigGroupV1.setObjects(*((_B,_N),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:lldpV2AgentConfigGroupV1.setStatus(_A)
lldpV2RemoteSystemsDataGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,67,1,1,4))
lldpV2RemoteSystemsDataGroupV1.setObjects(*((_B,_O),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU)))
if mibBuilder.loadTexts:lldpV2RemoteSystemsDataGroupV1.setStatus(_A)
lldpV2StatsGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,67,1,1,5))
lldpV2StatsGroupV1.setObjects(*((_B,_P),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am)))
if mibBuilder.loadTexts:lldpV2StatsGroupV1.setStatus(_A)
lldpV2BasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,67,1,2,1))
lldpV2BasicComplV1.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:lldpV2BasicComplV1.setStatus('deprecated')
lldpV2BasicComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,67,1,2,2))
lldpV2BasicComplV2.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:lldpV2BasicComplV2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'LumAddressFamilyNumbers':LumAddressFamilyNumbers,'LldpV2ChassisIdSubtype':LldpV2ChassisIdSubtype,'LldpV2ChassisId':LldpV2ChassisId,'LldpV2PortIdSubtype':LldpV2PortIdSubtype,'LldpV2PortId':LldpV2PortId,'LldpV2ManAddrIfSubtype':LldpV2ManAddrIfSubtype,'LldpV2ManAddress':LldpV2ManAddress,'lumLldpV2MIBModule':lumLldpV2MIBModule,'lumLldpV2Confs':lumLldpV2Confs,'lumLldpV2Groups':lumLldpV2Groups,_Q:lldpV2GeneralGroupV1,_R:lldpV2SystemInfoGroupV1,_S:lldpV2AgentConfigGroupV1,_T:lldpV2RemoteSystemsDataGroupV1,_U:lldpV2StatsGroupV1,'lumLldpV2Compliances':lumLldpV2Compliances,'lldpV2BasicComplV1':lldpV2BasicComplV1,'lldpV2BasicComplV2':lldpV2BasicComplV2,'lumLldpV2MIBObjects':lumLldpV2MIBObjects,'lldpGeneral':lldpGeneral,_c:lldpV2GeneralConfigLastChangeTime,_d:lldpV2GeneralStateLastChangeTime,'lldpV2SystemInfoTableSize':lldpV2SystemInfoTableSize,_e:lldpV2AgentConfigTableSize,_f:lldpV2RemSystemDataTableSize,_g:lldpV2StaticsTableSize,'lldpV2SystemInfo':lldpV2SystemInfo,'lldpV2SystemInfoTable':lldpV2SystemInfoTable,'lldpV2SystemInfoEntry':lldpV2SystemInfoEntry,_M:lldpV2SystemInfoIndex,_h:lldpV2SystemInfoName,_i:lldpV2SystemInfoSystemName,_k:lldpV2SystemInfoSystemDescription,_j:lldpV2SystemInfoSystemMacAddress,_l:lldpV2SystemInfoManagementIp,_m:lldpV2SystemInfoManagementOID,_n:lldpV2SystemInfoMaxNeighbors,'lldpV2AgentConfig':lldpV2AgentConfig,'lldpV2AgentConfigTable':lldpV2AgentConfigTable,'lldpV2AgentConfigEntry':lldpV2AgentConfigEntry,_N:lldpV2AgentConfigIndex,_o:lldpV2AgentConfigName,_p:lldpV2AgentConfigLocalMacAddress,'lldpV2AgentConfigDestMacAddress':lldpV2AgentConfigDestMacAddress,_q:lldpV2AgentConfigAdminStatus,_r:lldpV2AgentConfigNotificationEnable,_s:lldpV2AgentConfigMessageTxInterval,_t:lldpV2AgentConfigRxPort,_u:lldpV2AgentConfigTxPort,_v:lldpV2AgentConfigUpPort,_w:lldpV2AgentConfigAgentId,_x:lldpV2AgentConfigIfNo,'lldpV2AgentConfigPortDesc':lldpV2AgentConfigPortDesc,'lldpV2RemoteSystemData':lldpV2RemoteSystemData,'lldpV2RemTable':lldpV2RemTable,'lldpV2RemEntry':lldpV2RemEntry,_O:lldpV2RemIndex,_y:lldpV2RemName,_z:lldpV2RemLocalIfIndex,_A0:lldpV2RemSourceMACAddress,_A1:lldpV2RemChassisIdSubtype,_A2:lldpV2RemChassisId,_A3:lldpV2RemPortIdSubtype,_A4:lldpV2RemPortId,_A5:lldpV2RemPortDesc,_A6:lldpV2RemSysName,_A7:lldpV2RemSysDesc,_A8:lldpV2RemSysCapEnabled,_A9:lldpV2RemSysCapSupported,_AA:lldpV2RemManAddrSubtype,_AB:lldpV2RemManAddr,_AC:lldpV2RemManAddrIfSubtype,_AD:lldpV2RemManAddrIfId,_AE:lldpV2RemManAddrOID,_AF:lldpV2RemTooManyNeighbors,_AG:lldpV2RemMtuSize,_AH:lldpV2RemLagId,_AI:lldpV2RemLagisAggCapable,_AJ:lldpV2RemLagisAggregated,_AK:lldpV2RemUpTime,_AL:lldpV2RemTimeout,_AM:lldpV2RemTTL,_AN:lldpV2RemSubrack,_AO:lldpV2RemSlot,_AP:lldpV2RemTxPort,_AQ:lldpV2RemRxPort,_AR:lldpV2RemIdx,_AS:lldpV2RemIfNo,_AT:lldpV2RemUpPortId,_AU:lldpV2RemAgentId,'lldpV2Statistics':lldpV2Statistics,'lldpV2StatsTable':lldpV2StatsTable,'lldpV2StatsEntry':lldpV2StatsEntry,_P:lldpV2StatsIndex,_AW:lldpV2StatsAgentId,_AV:lldpV2StatsName,_AX:lldpV2StatsTxPortFramesTotal,_AY:lldpV2StatsRxPortFramesDiscardedTotal,_AZ:lldpV2StatsRxPortFramesErrors,_Aa:lldpV2StatsRxPortFramesTotal,_Ab:lldpV2StatsAgeOutsTotal,_Ac:lldpV2StatsTLVSDiscardedTotal,_Ad:lldpV2StatsTLVSUnrecognizedTotal,_Ae:lldpV2StatsSubrack,_Af:lldpV2StatsSlot,_Ag:lldpV2StatsTxPort,_Ah:lldpV2StatsRxPort,_Ai:lldpV2StatsIdx,_Aj:lldpV2StatsIfNo,_Ak:lldpV2StatsClientIdx,_Al:lldpV2StatsUpPortId,_Am:lldpV2StatsReset})