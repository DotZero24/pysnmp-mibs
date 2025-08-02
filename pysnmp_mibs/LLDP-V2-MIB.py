_B6='lldpV2NotificationsGroup'
_B5='lldpV2RemSysGroup'
_B4='lldpV2StatsRxGroup'
_B3='lldpV2ConfigRxGroup'
_B2='lldpV2LocSysGroup'
_B1='lldpV2StatsTxGroup'
_B0='lldpV2ConfigTxGroup'
_A_='lldpV2ConfigGroup'
_Az='lldpV2RemTablesChange'
_Ay='lldpV2RemOrgDefInfo'
_Ax='lldpV2RemUnknownTLVInfo'
_Aw='lldpV2RemManAddrOID'
_Av='lldpV2RemManAddrIfId'
_Au='lldpV2RemManAddrIfSubtype'
_At='lldpV2RemTooManyNeighbors'
_As='lldpV2RemRemoteChanges'
_Ar='lldpV2RemSysCapEnabled'
_Aq='lldpV2RemSysCapSupported'
_Ap='lldpV2RemSysDesc'
_Ao='lldpV2RemSysName'
_An='lldpV2RemPortDesc'
_Am='lldpV2RemPortId'
_Al='lldpV2RemPortIdSubtype'
_Ak='lldpV2RemChassisId'
_Aj='lldpV2RemChassisIdSubtype'
_Ai='lldpV2LocManAddrOID'
_Ah='lldpV2LocManAddrIfId'
_Ag='lldpV2LocManAddrIfSubtype'
_Af='lldpV2LocManAddrLen'
_Ae='lldpV2LocSysCapEnabled'
_Ad='lldpV2LocSysCapSupported'
_Ac='lldpV2LocSysName'
_Ab='lldpV2LocSysDesc'
_Aa='lldpV2LocPortDesc'
_AZ='lldpV2LocPortId'
_AY='lldpV2LocPortIdSubtype'
_AX='lldpV2LocChassisId'
_AW='lldpV2LocChassisIdSubtype'
_AV='lldpV2StatsTxLLDPDULengthErrors'
_AU='lldpV2StatsTxPortFramesTotal'
_AT='lldpV2StatsRxPortAgeoutsTotal'
_AS='lldpV2StatsRxPortTLVsUnrecognizedTotal'
_AR='lldpV2StatsRxPortTLVsDiscardedTotal'
_AQ='lldpV2StatsRxPortFramesTotal'
_AP='lldpV2StatsRxPortFramesErrors'
_AO='lldpV2StatsRxPortFramesDiscardedTotal'
_AN='lldpV2StatsRemTablesLastChangeTime'
_AM='lldpV2PortTxFastInit'
_AL='lldpV2PortMessageFastTx'
_AK='lldpV2PortTxCreditMax'
_AJ='lldpV2PortNotificationInterval'
_AI='lldpV2PortReinitDelay'
_AH='lldpV2PortMessageTxHoldMultiplier'
_AG='lldpV2PortMessageTxInterval'
_AF='lldpV2DestMacAddress'
_AE='lldpV2TxFastInit'
_AD='lldpV2MessageFastTx'
_AC='lldpV2TxCreditMax'
_AB='lldpV2ManAddrConfigRowStatus'
_AA='lldpV2ManAddrConfigTxEnable'
_A9='lldpV2PortConfigTLVsTxEnableV2'
_A8='lldpV2ReinitDelay'
_A7='lldpV2MessageTxHoldMultiplier'
_A6='lldpV2MessageTxInterval'
_A5='lldpV2PortConfigNotificationEnableV2'
_A4='lldpV2NotificationInterval'
_A3='lldpV2PortConfigAdminStatusV2'
_A2='lldpV2RemOrgDefInfoIndex'
_A1='lldpV2RemOrgDefInfoSubtype'
_A0='lldpV2RemOrgDefInfoOUI'
_z='lldpV2RemUnknownTLVType'
_y='lldpV2RemManAddr'
_x='lldpV2RemManAddrSubtype'
_w='lldpV2LocManAddr'
_v='lldpV2LocManAddrSubtype'
_u='lldpV2LocPortIfIndex'
_t='lldpV2StatsRxDestMACAddress'
_s='lldpV2StatsRxDestIfIndex'
_r='lldpV2StatsTxDestMACAddress'
_q='lldpV2StatsTxIfIndex'
_p='lldpV2PortConfigDestAddressIndexV2'
_o='lldpV2PortConfigIfIndexV2'
_n='read-create'
_m='lldpV2ManAddrConfigLocManAddr'
_l='lldpV2ManAddrConfigLocManAddrSubtype'
_k='lldpV2ManAddrConfigDestAddressIndex'
_j='lldpV2ManAddrConfigIfIndex'
_i='lldpV2AddressTableIndex'
_h='sysCap'
_g='sysDesc'
_f='sysName'
_e='portDesc'
_d='disabled'
_c='txAndRx'
_b='rxOnly'
_a='txOnly'
_Z='lldpV2PortConfigDestAddressIndex'
_Y='lldpV2PortConfigIfIndex'
_X='ifGeneralInformationGroup'
_W='lldpV2StatsRemTablesAgeouts'
_V='lldpV2StatsRemTablesDrops'
_U='lldpV2StatsRemTablesDeletes'
_T='lldpV2StatsRemTablesInserts'
_S='Integer32'
_R='Bits'
_Q='table entries'
_P='TruthValue'
_O='OctetString'
_N='lldpV2RemIndex'
_M='lldpV2RemLocalDestMACAddress'
_L='lldpV2RemLocalIfIndex'
_K='lldpV2RemTimeMark'
_J='LLDP frames'
_I='deprecated'
_H='SnmpAdminString'
_G='seconds'
_F='Unsigned32'
_E='read-write'
_D='not-accessible'
_C='read-only'
_B='LLDP-V2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AddressFamilyNumbers,=mibBuilder.importSymbols('IANA-ADDRESS-FAMILY-NUMBERS-MIB','AddressFamilyNumbers')
InterfaceIndex,ifGeneralInformationGroup=mibBuilder.importSymbols('IF-MIB','InterfaceIndex',_X)
LldpV2ChassisId,LldpV2ChassisIdSubtype,LldpV2DestAddressTableIndex,LldpV2ManAddrIfSubtype,LldpV2ManAddress,LldpV2PortId,LldpV2PortIdSubtype,LldpV2SystemCapabilitiesMap,ieee802dot1mibs=mibBuilder.importSymbols('LLDP-V2-TC-MIB','LldpV2ChassisId','LldpV2ChassisIdSubtype','LldpV2DestAddressTableIndex','LldpV2ManAddrIfSubtype','LldpV2ManAddress','LldpV2PortId','LldpV2PortIdSubtype','LldpV2SystemCapabilitiesMap','ieee802dot1mibs')
TimeFilter,ZeroBasedCounter32=mibBuilder.importSymbols('RMON2-MIB','TimeFilter','ZeroBasedCounter32')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_R,'Counter32','Counter64','Gauge32',_S,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp',_P)
lldpV2MIB=ModuleIdentity((1,3,111,2,802,1,1,13))
if mibBuilder.loadTexts:lldpV2MIB.setRevisions(('2016-03-11 00:00','2015-02-16 00:00','2009-06-08 00:00'))
_LldpV2Notifications_ObjectIdentity=ObjectIdentity
lldpV2Notifications=_LldpV2Notifications_ObjectIdentity((1,3,111,2,802,1,1,13,0))
_LldpV2NotificationPrefix_ObjectIdentity=ObjectIdentity
lldpV2NotificationPrefix=_LldpV2NotificationPrefix_ObjectIdentity((1,3,111,2,802,1,1,13,0,0))
_LldpV2Objects_ObjectIdentity=ObjectIdentity
lldpV2Objects=_LldpV2Objects_ObjectIdentity((1,3,111,2,802,1,1,13,1))
_LldpV2Configuration_ObjectIdentity=ObjectIdentity
lldpV2Configuration=_LldpV2Configuration_ObjectIdentity((1,3,111,2,802,1,1,13,1,1))
class _LldpV2MessageTxInterval_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,32768))
_LldpV2MessageTxInterval_Type.__name__=_F
_LldpV2MessageTxInterval_Object=MibScalar
lldpV2MessageTxInterval=_LldpV2MessageTxInterval_Object((1,3,111,2,802,1,1,13,1,1,1),_LldpV2MessageTxInterval_Type())
lldpV2MessageTxInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpV2MessageTxInterval.setStatus(_A)
if mibBuilder.loadTexts:lldpV2MessageTxInterval.setUnits(_G)
class _LldpV2MessageTxHoldMultiplier_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_LldpV2MessageTxHoldMultiplier_Type.__name__=_F
_LldpV2MessageTxHoldMultiplier_Object=MibScalar
lldpV2MessageTxHoldMultiplier=_LldpV2MessageTxHoldMultiplier_Object((1,3,111,2,802,1,1,13,1,1,2),_LldpV2MessageTxHoldMultiplier_Type())
lldpV2MessageTxHoldMultiplier.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpV2MessageTxHoldMultiplier.setStatus(_A)
class _LldpV2ReinitDelay_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_LldpV2ReinitDelay_Type.__name__=_F
_LldpV2ReinitDelay_Object=MibScalar
lldpV2ReinitDelay=_LldpV2ReinitDelay_Object((1,3,111,2,802,1,1,13,1,1,3),_LldpV2ReinitDelay_Type())
lldpV2ReinitDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpV2ReinitDelay.setStatus(_A)
if mibBuilder.loadTexts:lldpV2ReinitDelay.setUnits(_G)
class _LldpV2NotificationInterval_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,3600))
_LldpV2NotificationInterval_Type.__name__=_F
_LldpV2NotificationInterval_Object=MibScalar
lldpV2NotificationInterval=_LldpV2NotificationInterval_Object((1,3,111,2,802,1,1,13,1,1,4),_LldpV2NotificationInterval_Type())
lldpV2NotificationInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpV2NotificationInterval.setStatus(_A)
if mibBuilder.loadTexts:lldpV2NotificationInterval.setUnits(_G)
class _LldpV2TxCreditMax_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_LldpV2TxCreditMax_Type.__name__=_F
_LldpV2TxCreditMax_Object=MibScalar
lldpV2TxCreditMax=_LldpV2TxCreditMax_Object((1,3,111,2,802,1,1,13,1,1,5),_LldpV2TxCreditMax_Type())
lldpV2TxCreditMax.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpV2TxCreditMax.setStatus(_A)
if mibBuilder.loadTexts:lldpV2TxCreditMax.setUnits('PDUs')
class _LldpV2MessageFastTx_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_LldpV2MessageFastTx_Type.__name__=_F
_LldpV2MessageFastTx_Object=MibScalar
lldpV2MessageFastTx=_LldpV2MessageFastTx_Object((1,3,111,2,802,1,1,13,1,1,6),_LldpV2MessageFastTx_Type())
lldpV2MessageFastTx.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpV2MessageFastTx.setStatus(_A)
if mibBuilder.loadTexts:lldpV2MessageFastTx.setUnits(_G)
class _LldpV2TxFastInit_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_LldpV2TxFastInit_Type.__name__=_F
_LldpV2TxFastInit_Object=MibScalar
lldpV2TxFastInit=_LldpV2TxFastInit_Object((1,3,111,2,802,1,1,13,1,1,7),_LldpV2TxFastInit_Type())
lldpV2TxFastInit.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpV2TxFastInit.setStatus(_A)
_LldpV2PortConfigTable_Object=MibTable
lldpV2PortConfigTable=_LldpV2PortConfigTable_Object((1,3,111,2,802,1,1,13,1,1,8))
if mibBuilder.loadTexts:lldpV2PortConfigTable.setStatus(_I)
_LldpV2PortConfigEntry_Object=MibTableRow
lldpV2PortConfigEntry=_LldpV2PortConfigEntry_Object((1,3,111,2,802,1,1,13,1,1,8,1))
lldpV2PortConfigEntry.setIndexNames((0,_B,_Y),(0,_B,_Z))
if mibBuilder.loadTexts:lldpV2PortConfigEntry.setStatus(_I)
_LldpV2PortConfigIfIndex_Type=InterfaceIndex
_LldpV2PortConfigIfIndex_Object=MibTableColumn
lldpV2PortConfigIfIndex=_LldpV2PortConfigIfIndex_Object((1,3,111,2,802,1,1,13,1,1,8,1,1),_LldpV2PortConfigIfIndex_Type())
lldpV2PortConfigIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2PortConfigIfIndex.setStatus(_I)
_LldpV2PortConfigDestAddressIndex_Type=LldpV2DestAddressTableIndex
_LldpV2PortConfigDestAddressIndex_Object=MibTableColumn
lldpV2PortConfigDestAddressIndex=_LldpV2PortConfigDestAddressIndex_Object((1,3,111,2,802,1,1,13,1,1,8,1,2),_LldpV2PortConfigDestAddressIndex_Type())
lldpV2PortConfigDestAddressIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2PortConfigDestAddressIndex.setStatus(_I)
class _LldpV2PortConfigAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_a,1),(_b,2),(_c,3),(_d,4)))
_LldpV2PortConfigAdminStatus_Type.__name__=_S
_LldpV2PortConfigAdminStatus_Object=MibTableColumn
lldpV2PortConfigAdminStatus=_LldpV2PortConfigAdminStatus_Object((1,3,111,2,802,1,1,13,1,1,8,1,3),_LldpV2PortConfigAdminStatus_Type())
lldpV2PortConfigAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpV2PortConfigAdminStatus.setStatus(_I)
class _LldpV2PortConfigNotificationEnable_Type(TruthValue):defaultValue=2
_LldpV2PortConfigNotificationEnable_Type.__name__=_P
_LldpV2PortConfigNotificationEnable_Object=MibTableColumn
lldpV2PortConfigNotificationEnable=_LldpV2PortConfigNotificationEnable_Object((1,3,111,2,802,1,1,13,1,1,8,1,4),_LldpV2PortConfigNotificationEnable_Type())
lldpV2PortConfigNotificationEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpV2PortConfigNotificationEnable.setStatus(_I)
class _LldpV2PortConfigTLVsTxEnable_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*((_e,0),(_f,1),(_g,2),(_h,3)))
_LldpV2PortConfigTLVsTxEnable_Type.__name__=_R
_LldpV2PortConfigTLVsTxEnable_Object=MibTableColumn
lldpV2PortConfigTLVsTxEnable=_LldpV2PortConfigTLVsTxEnable_Object((1,3,111,2,802,1,1,13,1,1,8,1,5),_LldpV2PortConfigTLVsTxEnable_Type())
lldpV2PortConfigTLVsTxEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpV2PortConfigTLVsTxEnable.setStatus(_I)
_LldpV2DestAddressTable_Object=MibTable
lldpV2DestAddressTable=_LldpV2DestAddressTable_Object((1,3,111,2,802,1,1,13,1,1,9))
if mibBuilder.loadTexts:lldpV2DestAddressTable.setStatus(_A)
_LldpV2DestAddressTableEntry_Object=MibTableRow
lldpV2DestAddressTableEntry=_LldpV2DestAddressTableEntry_Object((1,3,111,2,802,1,1,13,1,1,9,1))
lldpV2DestAddressTableEntry.setIndexNames((0,_B,_i))
if mibBuilder.loadTexts:lldpV2DestAddressTableEntry.setStatus(_A)
_LldpV2AddressTableIndex_Type=LldpV2DestAddressTableIndex
_LldpV2AddressTableIndex_Object=MibTableColumn
lldpV2AddressTableIndex=_LldpV2AddressTableIndex_Object((1,3,111,2,802,1,1,13,1,1,9,1,1),_LldpV2AddressTableIndex_Type())
lldpV2AddressTableIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2AddressTableIndex.setStatus(_A)
_LldpV2DestMacAddress_Type=MacAddress
_LldpV2DestMacAddress_Object=MibTableColumn
lldpV2DestMacAddress=_LldpV2DestMacAddress_Object((1,3,111,2,802,1,1,13,1,1,9,1,2),_LldpV2DestMacAddress_Type())
lldpV2DestMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2DestMacAddress.setStatus(_A)
_LldpV2ManAddrConfigTxPortsTable_Object=MibTable
lldpV2ManAddrConfigTxPortsTable=_LldpV2ManAddrConfigTxPortsTable_Object((1,3,111,2,802,1,1,13,1,1,10))
if mibBuilder.loadTexts:lldpV2ManAddrConfigTxPortsTable.setStatus(_A)
_LldpV2ManAddrConfigTxPortsEntry_Object=MibTableRow
lldpV2ManAddrConfigTxPortsEntry=_LldpV2ManAddrConfigTxPortsEntry_Object((1,3,111,2,802,1,1,13,1,1,10,1))
lldpV2ManAddrConfigTxPortsEntry.setIndexNames((0,_B,_j),(0,_B,_k),(0,_B,_l),(0,_B,_m))
if mibBuilder.loadTexts:lldpV2ManAddrConfigTxPortsEntry.setStatus(_A)
_LldpV2ManAddrConfigIfIndex_Type=InterfaceIndex
_LldpV2ManAddrConfigIfIndex_Object=MibTableColumn
lldpV2ManAddrConfigIfIndex=_LldpV2ManAddrConfigIfIndex_Object((1,3,111,2,802,1,1,13,1,1,10,1,1),_LldpV2ManAddrConfigIfIndex_Type())
lldpV2ManAddrConfigIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2ManAddrConfigIfIndex.setStatus(_A)
_LldpV2ManAddrConfigDestAddressIndex_Type=LldpV2DestAddressTableIndex
_LldpV2ManAddrConfigDestAddressIndex_Object=MibTableColumn
lldpV2ManAddrConfigDestAddressIndex=_LldpV2ManAddrConfigDestAddressIndex_Object((1,3,111,2,802,1,1,13,1,1,10,1,2),_LldpV2ManAddrConfigDestAddressIndex_Type())
lldpV2ManAddrConfigDestAddressIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2ManAddrConfigDestAddressIndex.setStatus(_A)
_LldpV2ManAddrConfigLocManAddrSubtype_Type=AddressFamilyNumbers
_LldpV2ManAddrConfigLocManAddrSubtype_Object=MibTableColumn
lldpV2ManAddrConfigLocManAddrSubtype=_LldpV2ManAddrConfigLocManAddrSubtype_Object((1,3,111,2,802,1,1,13,1,1,10,1,3),_LldpV2ManAddrConfigLocManAddrSubtype_Type())
lldpV2ManAddrConfigLocManAddrSubtype.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2ManAddrConfigLocManAddrSubtype.setStatus(_A)
_LldpV2ManAddrConfigLocManAddr_Type=LldpV2ManAddress
_LldpV2ManAddrConfigLocManAddr_Object=MibTableColumn
lldpV2ManAddrConfigLocManAddr=_LldpV2ManAddrConfigLocManAddr_Object((1,3,111,2,802,1,1,13,1,1,10,1,4),_LldpV2ManAddrConfigLocManAddr_Type())
lldpV2ManAddrConfigLocManAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2ManAddrConfigLocManAddr.setStatus(_A)
class _LldpV2ManAddrConfigTxEnable_Type(TruthValue):defaultValue=2
_LldpV2ManAddrConfigTxEnable_Type.__name__=_P
_LldpV2ManAddrConfigTxEnable_Object=MibTableColumn
lldpV2ManAddrConfigTxEnable=_LldpV2ManAddrConfigTxEnable_Object((1,3,111,2,802,1,1,13,1,1,10,1,5),_LldpV2ManAddrConfigTxEnable_Type())
lldpV2ManAddrConfigTxEnable.setMaxAccess(_n)
if mibBuilder.loadTexts:lldpV2ManAddrConfigTxEnable.setStatus(_A)
_LldpV2ManAddrConfigRowStatus_Type=RowStatus
_LldpV2ManAddrConfigRowStatus_Object=MibTableColumn
lldpV2ManAddrConfigRowStatus=_LldpV2ManAddrConfigRowStatus_Object((1,3,111,2,802,1,1,13,1,1,10,1,6),_LldpV2ManAddrConfigRowStatus_Type())
lldpV2ManAddrConfigRowStatus.setMaxAccess(_n)
if mibBuilder.loadTexts:lldpV2ManAddrConfigRowStatus.setStatus(_A)
_LldpV2PortConfigTableV2_Object=MibTable
lldpV2PortConfigTableV2=_LldpV2PortConfigTableV2_Object((1,3,111,2,802,1,1,13,1,1,11))
if mibBuilder.loadTexts:lldpV2PortConfigTableV2.setStatus(_A)
_LldpV2PortConfigEntryV2_Object=MibTableRow
lldpV2PortConfigEntryV2=_LldpV2PortConfigEntryV2_Object((1,3,111,2,802,1,1,13,1,1,11,1))
lldpV2PortConfigEntryV2.setIndexNames((0,_B,_o),(0,_B,_p))
if mibBuilder.loadTexts:lldpV2PortConfigEntryV2.setStatus(_A)
_LldpV2PortConfigIfIndexV2_Type=InterfaceIndex
_LldpV2PortConfigIfIndexV2_Object=MibTableColumn
lldpV2PortConfigIfIndexV2=_LldpV2PortConfigIfIndexV2_Object((1,3,111,2,802,1,1,13,1,1,11,1,1),_LldpV2PortConfigIfIndexV2_Type())
lldpV2PortConfigIfIndexV2.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2PortConfigIfIndexV2.setStatus(_A)
_LldpV2PortConfigDestAddressIndexV2_Type=LldpV2DestAddressTableIndex
_LldpV2PortConfigDestAddressIndexV2_Object=MibTableColumn
lldpV2PortConfigDestAddressIndexV2=_LldpV2PortConfigDestAddressIndexV2_Object((1,3,111,2,802,1,1,13,1,1,11,1,2),_LldpV2PortConfigDestAddressIndexV2_Type())
lldpV2PortConfigDestAddressIndexV2.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2PortConfigDestAddressIndexV2.setStatus(_A)
class _LldpV2PortConfigAdminStatusV2_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_a,1),(_b,2),(_c,3),(_d,4)))
_LldpV2PortConfigAdminStatusV2_Type.__name__=_S
_LldpV2PortConfigAdminStatusV2_Object=MibTableColumn
lldpV2PortConfigAdminStatusV2=_LldpV2PortConfigAdminStatusV2_Object((1,3,111,2,802,1,1,13,1,1,11,1,3),_LldpV2PortConfigAdminStatusV2_Type())
lldpV2PortConfigAdminStatusV2.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpV2PortConfigAdminStatusV2.setStatus(_A)
class _LldpV2PortMessageTxInterval_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,32768))
_LldpV2PortMessageTxInterval_Type.__name__=_F
_LldpV2PortMessageTxInterval_Object=MibTableColumn
lldpV2PortMessageTxInterval=_LldpV2PortMessageTxInterval_Object((1,3,111,2,802,1,1,13,1,1,11,1,4),_LldpV2PortMessageTxInterval_Type())
lldpV2PortMessageTxInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpV2PortMessageTxInterval.setStatus(_A)
if mibBuilder.loadTexts:lldpV2PortMessageTxInterval.setUnits(_G)
class _LldpV2PortMessageTxHoldMultiplier_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_LldpV2PortMessageTxHoldMultiplier_Type.__name__=_F
_LldpV2PortMessageTxHoldMultiplier_Object=MibTableColumn
lldpV2PortMessageTxHoldMultiplier=_LldpV2PortMessageTxHoldMultiplier_Object((1,3,111,2,802,1,1,13,1,1,11,1,5),_LldpV2PortMessageTxHoldMultiplier_Type())
lldpV2PortMessageTxHoldMultiplier.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpV2PortMessageTxHoldMultiplier.setStatus(_A)
class _LldpV2PortReinitDelay_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_LldpV2PortReinitDelay_Type.__name__=_F
_LldpV2PortReinitDelay_Object=MibTableColumn
lldpV2PortReinitDelay=_LldpV2PortReinitDelay_Object((1,3,111,2,802,1,1,13,1,1,11,1,6),_LldpV2PortReinitDelay_Type())
lldpV2PortReinitDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpV2PortReinitDelay.setStatus(_A)
if mibBuilder.loadTexts:lldpV2PortReinitDelay.setUnits(_G)
class _LldpV2PortNotificationInterval_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,3600))
_LldpV2PortNotificationInterval_Type.__name__=_F
_LldpV2PortNotificationInterval_Object=MibTableColumn
lldpV2PortNotificationInterval=_LldpV2PortNotificationInterval_Object((1,3,111,2,802,1,1,13,1,1,11,1,7),_LldpV2PortNotificationInterval_Type())
lldpV2PortNotificationInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpV2PortNotificationInterval.setStatus(_A)
if mibBuilder.loadTexts:lldpV2PortNotificationInterval.setUnits(_G)
class _LldpV2PortTxCreditMax_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_LldpV2PortTxCreditMax_Type.__name__=_F
_LldpV2PortTxCreditMax_Object=MibTableColumn
lldpV2PortTxCreditMax=_LldpV2PortTxCreditMax_Object((1,3,111,2,802,1,1,13,1,1,11,1,8),_LldpV2PortTxCreditMax_Type())
lldpV2PortTxCreditMax.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpV2PortTxCreditMax.setStatus(_A)
if mibBuilder.loadTexts:lldpV2PortTxCreditMax.setUnits('PDUs')
class _LldpV2PortMessageFastTx_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_LldpV2PortMessageFastTx_Type.__name__=_F
_LldpV2PortMessageFastTx_Object=MibTableColumn
lldpV2PortMessageFastTx=_LldpV2PortMessageFastTx_Object((1,3,111,2,802,1,1,13,1,1,11,1,9),_LldpV2PortMessageFastTx_Type())
lldpV2PortMessageFastTx.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpV2PortMessageFastTx.setStatus(_A)
if mibBuilder.loadTexts:lldpV2PortMessageFastTx.setUnits(_G)
class _LldpV2PortTxFastInit_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_LldpV2PortTxFastInit_Type.__name__=_F
_LldpV2PortTxFastInit_Object=MibTableColumn
lldpV2PortTxFastInit=_LldpV2PortTxFastInit_Object((1,3,111,2,802,1,1,13,1,1,11,1,10),_LldpV2PortTxFastInit_Type())
lldpV2PortTxFastInit.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpV2PortTxFastInit.setStatus(_A)
class _LldpV2PortConfigNotificationEnableV2_Type(TruthValue):defaultValue=2
_LldpV2PortConfigNotificationEnableV2_Type.__name__=_P
_LldpV2PortConfigNotificationEnableV2_Object=MibTableColumn
lldpV2PortConfigNotificationEnableV2=_LldpV2PortConfigNotificationEnableV2_Object((1,3,111,2,802,1,1,13,1,1,11,1,11),_LldpV2PortConfigNotificationEnableV2_Type())
lldpV2PortConfigNotificationEnableV2.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpV2PortConfigNotificationEnableV2.setStatus(_A)
class _LldpV2PortConfigTLVsTxEnableV2_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*((_e,0),(_f,1),(_g,2),(_h,3)))
_LldpV2PortConfigTLVsTxEnableV2_Type.__name__=_R
_LldpV2PortConfigTLVsTxEnableV2_Object=MibTableColumn
lldpV2PortConfigTLVsTxEnableV2=_LldpV2PortConfigTLVsTxEnableV2_Object((1,3,111,2,802,1,1,13,1,1,11,1,12),_LldpV2PortConfigTLVsTxEnableV2_Type())
lldpV2PortConfigTLVsTxEnableV2.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpV2PortConfigTLVsTxEnableV2.setStatus(_A)
_LldpV2Statistics_ObjectIdentity=ObjectIdentity
lldpV2Statistics=_LldpV2Statistics_ObjectIdentity((1,3,111,2,802,1,1,13,1,2))
_LldpV2StatsRemTablesLastChangeTime_Type=TimeStamp
_LldpV2StatsRemTablesLastChangeTime_Object=MibScalar
lldpV2StatsRemTablesLastChangeTime=_LldpV2StatsRemTablesLastChangeTime_Object((1,3,111,2,802,1,1,13,1,2,1),_LldpV2StatsRemTablesLastChangeTime_Type())
lldpV2StatsRemTablesLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2StatsRemTablesLastChangeTime.setStatus(_A)
_LldpV2StatsRemTablesInserts_Type=ZeroBasedCounter32
_LldpV2StatsRemTablesInserts_Object=MibScalar
lldpV2StatsRemTablesInserts=_LldpV2StatsRemTablesInserts_Object((1,3,111,2,802,1,1,13,1,2,2),_LldpV2StatsRemTablesInserts_Type())
lldpV2StatsRemTablesInserts.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2StatsRemTablesInserts.setStatus(_A)
if mibBuilder.loadTexts:lldpV2StatsRemTablesInserts.setUnits(_Q)
_LldpV2StatsRemTablesDeletes_Type=ZeroBasedCounter32
_LldpV2StatsRemTablesDeletes_Object=MibScalar
lldpV2StatsRemTablesDeletes=_LldpV2StatsRemTablesDeletes_Object((1,3,111,2,802,1,1,13,1,2,3),_LldpV2StatsRemTablesDeletes_Type())
lldpV2StatsRemTablesDeletes.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2StatsRemTablesDeletes.setStatus(_A)
if mibBuilder.loadTexts:lldpV2StatsRemTablesDeletes.setUnits(_Q)
_LldpV2StatsRemTablesDrops_Type=ZeroBasedCounter32
_LldpV2StatsRemTablesDrops_Object=MibScalar
lldpV2StatsRemTablesDrops=_LldpV2StatsRemTablesDrops_Object((1,3,111,2,802,1,1,13,1,2,4),_LldpV2StatsRemTablesDrops_Type())
lldpV2StatsRemTablesDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2StatsRemTablesDrops.setStatus(_A)
if mibBuilder.loadTexts:lldpV2StatsRemTablesDrops.setUnits(_Q)
_LldpV2StatsRemTablesAgeouts_Type=ZeroBasedCounter32
_LldpV2StatsRemTablesAgeouts_Object=MibScalar
lldpV2StatsRemTablesAgeouts=_LldpV2StatsRemTablesAgeouts_Object((1,3,111,2,802,1,1,13,1,2,5),_LldpV2StatsRemTablesAgeouts_Type())
lldpV2StatsRemTablesAgeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2StatsRemTablesAgeouts.setStatus(_A)
if mibBuilder.loadTexts:lldpV2StatsRemTablesAgeouts.setUnits(_Q)
_LldpV2StatsTxPortTable_Object=MibTable
lldpV2StatsTxPortTable=_LldpV2StatsTxPortTable_Object((1,3,111,2,802,1,1,13,1,2,6))
if mibBuilder.loadTexts:lldpV2StatsTxPortTable.setStatus(_A)
_LldpV2StatsTxPortEntry_Object=MibTableRow
lldpV2StatsTxPortEntry=_LldpV2StatsTxPortEntry_Object((1,3,111,2,802,1,1,13,1,2,6,1))
lldpV2StatsTxPortEntry.setIndexNames((0,_B,_q),(0,_B,_r))
if mibBuilder.loadTexts:lldpV2StatsTxPortEntry.setStatus(_A)
_LldpV2StatsTxIfIndex_Type=InterfaceIndex
_LldpV2StatsTxIfIndex_Object=MibTableColumn
lldpV2StatsTxIfIndex=_LldpV2StatsTxIfIndex_Object((1,3,111,2,802,1,1,13,1,2,6,1,1),_LldpV2StatsTxIfIndex_Type())
lldpV2StatsTxIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2StatsTxIfIndex.setStatus(_A)
_LldpV2StatsTxDestMACAddress_Type=LldpV2DestAddressTableIndex
_LldpV2StatsTxDestMACAddress_Object=MibTableColumn
lldpV2StatsTxDestMACAddress=_LldpV2StatsTxDestMACAddress_Object((1,3,111,2,802,1,1,13,1,2,6,1,2),_LldpV2StatsTxDestMACAddress_Type())
lldpV2StatsTxDestMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2StatsTxDestMACAddress.setStatus(_A)
_LldpV2StatsTxPortFramesTotal_Type=Counter32
_LldpV2StatsTxPortFramesTotal_Object=MibTableColumn
lldpV2StatsTxPortFramesTotal=_LldpV2StatsTxPortFramesTotal_Object((1,3,111,2,802,1,1,13,1,2,6,1,3),_LldpV2StatsTxPortFramesTotal_Type())
lldpV2StatsTxPortFramesTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2StatsTxPortFramesTotal.setStatus(_A)
if mibBuilder.loadTexts:lldpV2StatsTxPortFramesTotal.setUnits(_J)
_LldpV2StatsTxLLDPDULengthErrors_Type=Counter32
_LldpV2StatsTxLLDPDULengthErrors_Object=MibTableColumn
lldpV2StatsTxLLDPDULengthErrors=_LldpV2StatsTxLLDPDULengthErrors_Object((1,3,111,2,802,1,1,13,1,2,6,1,4),_LldpV2StatsTxLLDPDULengthErrors_Type())
lldpV2StatsTxLLDPDULengthErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2StatsTxLLDPDULengthErrors.setStatus(_A)
if mibBuilder.loadTexts:lldpV2StatsTxLLDPDULengthErrors.setUnits(_J)
_LldpV2StatsRxPortTable_Object=MibTable
lldpV2StatsRxPortTable=_LldpV2StatsRxPortTable_Object((1,3,111,2,802,1,1,13,1,2,7))
if mibBuilder.loadTexts:lldpV2StatsRxPortTable.setStatus(_A)
_LldpV2StatsRxPortEntry_Object=MibTableRow
lldpV2StatsRxPortEntry=_LldpV2StatsRxPortEntry_Object((1,3,111,2,802,1,1,13,1,2,7,1))
lldpV2StatsRxPortEntry.setIndexNames((0,_B,_s),(0,_B,_t))
if mibBuilder.loadTexts:lldpV2StatsRxPortEntry.setStatus(_A)
_LldpV2StatsRxDestIfIndex_Type=InterfaceIndex
_LldpV2StatsRxDestIfIndex_Object=MibTableColumn
lldpV2StatsRxDestIfIndex=_LldpV2StatsRxDestIfIndex_Object((1,3,111,2,802,1,1,13,1,2,7,1,1),_LldpV2StatsRxDestIfIndex_Type())
lldpV2StatsRxDestIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2StatsRxDestIfIndex.setStatus(_A)
_LldpV2StatsRxDestMACAddress_Type=LldpV2DestAddressTableIndex
_LldpV2StatsRxDestMACAddress_Object=MibTableColumn
lldpV2StatsRxDestMACAddress=_LldpV2StatsRxDestMACAddress_Object((1,3,111,2,802,1,1,13,1,2,7,1,2),_LldpV2StatsRxDestMACAddress_Type())
lldpV2StatsRxDestMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2StatsRxDestMACAddress.setStatus(_A)
_LldpV2StatsRxPortFramesDiscardedTotal_Type=Counter32
_LldpV2StatsRxPortFramesDiscardedTotal_Object=MibTableColumn
lldpV2StatsRxPortFramesDiscardedTotal=_LldpV2StatsRxPortFramesDiscardedTotal_Object((1,3,111,2,802,1,1,13,1,2,7,1,3),_LldpV2StatsRxPortFramesDiscardedTotal_Type())
lldpV2StatsRxPortFramesDiscardedTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2StatsRxPortFramesDiscardedTotal.setStatus(_A)
if mibBuilder.loadTexts:lldpV2StatsRxPortFramesDiscardedTotal.setUnits(_J)
_LldpV2StatsRxPortFramesErrors_Type=Counter32
_LldpV2StatsRxPortFramesErrors_Object=MibTableColumn
lldpV2StatsRxPortFramesErrors=_LldpV2StatsRxPortFramesErrors_Object((1,3,111,2,802,1,1,13,1,2,7,1,4),_LldpV2StatsRxPortFramesErrors_Type())
lldpV2StatsRxPortFramesErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2StatsRxPortFramesErrors.setStatus(_A)
if mibBuilder.loadTexts:lldpV2StatsRxPortFramesErrors.setUnits(_J)
_LldpV2StatsRxPortFramesTotal_Type=Counter32
_LldpV2StatsRxPortFramesTotal_Object=MibTableColumn
lldpV2StatsRxPortFramesTotal=_LldpV2StatsRxPortFramesTotal_Object((1,3,111,2,802,1,1,13,1,2,7,1,5),_LldpV2StatsRxPortFramesTotal_Type())
lldpV2StatsRxPortFramesTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2StatsRxPortFramesTotal.setStatus(_A)
if mibBuilder.loadTexts:lldpV2StatsRxPortFramesTotal.setUnits(_J)
_LldpV2StatsRxPortTLVsDiscardedTotal_Type=Counter32
_LldpV2StatsRxPortTLVsDiscardedTotal_Object=MibTableColumn
lldpV2StatsRxPortTLVsDiscardedTotal=_LldpV2StatsRxPortTLVsDiscardedTotal_Object((1,3,111,2,802,1,1,13,1,2,7,1,6),_LldpV2StatsRxPortTLVsDiscardedTotal_Type())
lldpV2StatsRxPortTLVsDiscardedTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2StatsRxPortTLVsDiscardedTotal.setStatus(_A)
if mibBuilder.loadTexts:lldpV2StatsRxPortTLVsDiscardedTotal.setUnits('TLVs')
_LldpV2StatsRxPortTLVsUnrecognizedTotal_Type=Counter32
_LldpV2StatsRxPortTLVsUnrecognizedTotal_Object=MibTableColumn
lldpV2StatsRxPortTLVsUnrecognizedTotal=_LldpV2StatsRxPortTLVsUnrecognizedTotal_Object((1,3,111,2,802,1,1,13,1,2,7,1,7),_LldpV2StatsRxPortTLVsUnrecognizedTotal_Type())
lldpV2StatsRxPortTLVsUnrecognizedTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2StatsRxPortTLVsUnrecognizedTotal.setStatus(_A)
if mibBuilder.loadTexts:lldpV2StatsRxPortTLVsUnrecognizedTotal.setUnits('TLVs')
_LldpV2StatsRxPortAgeoutsTotal_Type=ZeroBasedCounter32
_LldpV2StatsRxPortAgeoutsTotal_Object=MibTableColumn
lldpV2StatsRxPortAgeoutsTotal=_LldpV2StatsRxPortAgeoutsTotal_Object((1,3,111,2,802,1,1,13,1,2,7,1,8),_LldpV2StatsRxPortAgeoutsTotal_Type())
lldpV2StatsRxPortAgeoutsTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2StatsRxPortAgeoutsTotal.setStatus(_A)
_LldpV2LocalSystemData_ObjectIdentity=ObjectIdentity
lldpV2LocalSystemData=_LldpV2LocalSystemData_ObjectIdentity((1,3,111,2,802,1,1,13,1,3))
_LldpV2LocChassisIdSubtype_Type=LldpV2ChassisIdSubtype
_LldpV2LocChassisIdSubtype_Object=MibScalar
lldpV2LocChassisIdSubtype=_LldpV2LocChassisIdSubtype_Object((1,3,111,2,802,1,1,13,1,3,1),_LldpV2LocChassisIdSubtype_Type())
lldpV2LocChassisIdSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2LocChassisIdSubtype.setStatus(_A)
_LldpV2LocChassisId_Type=LldpV2ChassisId
_LldpV2LocChassisId_Object=MibScalar
lldpV2LocChassisId=_LldpV2LocChassisId_Object((1,3,111,2,802,1,1,13,1,3,2),_LldpV2LocChassisId_Type())
lldpV2LocChassisId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2LocChassisId.setStatus(_A)
class _LldpV2LocSysName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpV2LocSysName_Type.__name__=_H
_LldpV2LocSysName_Object=MibScalar
lldpV2LocSysName=_LldpV2LocSysName_Object((1,3,111,2,802,1,1,13,1,3,3),_LldpV2LocSysName_Type())
lldpV2LocSysName.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2LocSysName.setStatus(_A)
class _LldpV2LocSysDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpV2LocSysDesc_Type.__name__=_H
_LldpV2LocSysDesc_Object=MibScalar
lldpV2LocSysDesc=_LldpV2LocSysDesc_Object((1,3,111,2,802,1,1,13,1,3,4),_LldpV2LocSysDesc_Type())
lldpV2LocSysDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2LocSysDesc.setStatus(_A)
_LldpV2LocSysCapSupported_Type=LldpV2SystemCapabilitiesMap
_LldpV2LocSysCapSupported_Object=MibScalar
lldpV2LocSysCapSupported=_LldpV2LocSysCapSupported_Object((1,3,111,2,802,1,1,13,1,3,5),_LldpV2LocSysCapSupported_Type())
lldpV2LocSysCapSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2LocSysCapSupported.setStatus(_A)
_LldpV2LocSysCapEnabled_Type=LldpV2SystemCapabilitiesMap
_LldpV2LocSysCapEnabled_Object=MibScalar
lldpV2LocSysCapEnabled=_LldpV2LocSysCapEnabled_Object((1,3,111,2,802,1,1,13,1,3,6),_LldpV2LocSysCapEnabled_Type())
lldpV2LocSysCapEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2LocSysCapEnabled.setStatus(_A)
_LldpV2LocPortTable_Object=MibTable
lldpV2LocPortTable=_LldpV2LocPortTable_Object((1,3,111,2,802,1,1,13,1,3,7))
if mibBuilder.loadTexts:lldpV2LocPortTable.setStatus(_A)
_LldpV2LocPortEntry_Object=MibTableRow
lldpV2LocPortEntry=_LldpV2LocPortEntry_Object((1,3,111,2,802,1,1,13,1,3,7,1))
lldpV2LocPortEntry.setIndexNames((0,_B,_u))
if mibBuilder.loadTexts:lldpV2LocPortEntry.setStatus(_A)
_LldpV2LocPortIfIndex_Type=InterfaceIndex
_LldpV2LocPortIfIndex_Object=MibTableColumn
lldpV2LocPortIfIndex=_LldpV2LocPortIfIndex_Object((1,3,111,2,802,1,1,13,1,3,7,1,1),_LldpV2LocPortIfIndex_Type())
lldpV2LocPortIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2LocPortIfIndex.setStatus(_A)
_LldpV2LocPortIdSubtype_Type=LldpV2PortIdSubtype
_LldpV2LocPortIdSubtype_Object=MibTableColumn
lldpV2LocPortIdSubtype=_LldpV2LocPortIdSubtype_Object((1,3,111,2,802,1,1,13,1,3,7,1,2),_LldpV2LocPortIdSubtype_Type())
lldpV2LocPortIdSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2LocPortIdSubtype.setStatus(_A)
_LldpV2LocPortId_Type=LldpV2PortId
_LldpV2LocPortId_Object=MibTableColumn
lldpV2LocPortId=_LldpV2LocPortId_Object((1,3,111,2,802,1,1,13,1,3,7,1,3),_LldpV2LocPortId_Type())
lldpV2LocPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2LocPortId.setStatus(_A)
class _LldpV2LocPortDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpV2LocPortDesc_Type.__name__=_H
_LldpV2LocPortDesc_Object=MibTableColumn
lldpV2LocPortDesc=_LldpV2LocPortDesc_Object((1,3,111,2,802,1,1,13,1,3,7,1,4),_LldpV2LocPortDesc_Type())
lldpV2LocPortDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2LocPortDesc.setStatus(_A)
_LldpV2LocManAddrTable_Object=MibTable
lldpV2LocManAddrTable=_LldpV2LocManAddrTable_Object((1,3,111,2,802,1,1,13,1,3,8))
if mibBuilder.loadTexts:lldpV2LocManAddrTable.setStatus(_A)
_LldpV2LocManAddrEntry_Object=MibTableRow
lldpV2LocManAddrEntry=_LldpV2LocManAddrEntry_Object((1,3,111,2,802,1,1,13,1,3,8,1))
lldpV2LocManAddrEntry.setIndexNames((0,_B,_v),(0,_B,_w))
if mibBuilder.loadTexts:lldpV2LocManAddrEntry.setStatus(_A)
_LldpV2LocManAddrSubtype_Type=AddressFamilyNumbers
_LldpV2LocManAddrSubtype_Object=MibTableColumn
lldpV2LocManAddrSubtype=_LldpV2LocManAddrSubtype_Object((1,3,111,2,802,1,1,13,1,3,8,1,1),_LldpV2LocManAddrSubtype_Type())
lldpV2LocManAddrSubtype.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2LocManAddrSubtype.setStatus(_A)
_LldpV2LocManAddr_Type=LldpV2ManAddress
_LldpV2LocManAddr_Object=MibTableColumn
lldpV2LocManAddr=_LldpV2LocManAddr_Object((1,3,111,2,802,1,1,13,1,3,8,1,2),_LldpV2LocManAddr_Type())
lldpV2LocManAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2LocManAddr.setStatus(_A)
_LldpV2LocManAddrLen_Type=Unsigned32
_LldpV2LocManAddrLen_Object=MibTableColumn
lldpV2LocManAddrLen=_LldpV2LocManAddrLen_Object((1,3,111,2,802,1,1,13,1,3,8,1,3),_LldpV2LocManAddrLen_Type())
lldpV2LocManAddrLen.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2LocManAddrLen.setStatus(_A)
_LldpV2LocManAddrIfSubtype_Type=LldpV2ManAddrIfSubtype
_LldpV2LocManAddrIfSubtype_Object=MibTableColumn
lldpV2LocManAddrIfSubtype=_LldpV2LocManAddrIfSubtype_Object((1,3,111,2,802,1,1,13,1,3,8,1,4),_LldpV2LocManAddrIfSubtype_Type())
lldpV2LocManAddrIfSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2LocManAddrIfSubtype.setStatus(_A)
_LldpV2LocManAddrIfId_Type=Unsigned32
_LldpV2LocManAddrIfId_Object=MibTableColumn
lldpV2LocManAddrIfId=_LldpV2LocManAddrIfId_Object((1,3,111,2,802,1,1,13,1,3,8,1,5),_LldpV2LocManAddrIfId_Type())
lldpV2LocManAddrIfId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2LocManAddrIfId.setStatus(_A)
_LldpV2LocManAddrOID_Type=ObjectIdentifier
_LldpV2LocManAddrOID_Object=MibTableColumn
lldpV2LocManAddrOID=_LldpV2LocManAddrOID_Object((1,3,111,2,802,1,1,13,1,3,8,1,6),_LldpV2LocManAddrOID_Type())
lldpV2LocManAddrOID.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2LocManAddrOID.setStatus(_A)
_LldpV2RemoteSystemsData_ObjectIdentity=ObjectIdentity
lldpV2RemoteSystemsData=_LldpV2RemoteSystemsData_ObjectIdentity((1,3,111,2,802,1,1,13,1,4))
_LldpV2RemTable_Object=MibTable
lldpV2RemTable=_LldpV2RemTable_Object((1,3,111,2,802,1,1,13,1,4,1))
if mibBuilder.loadTexts:lldpV2RemTable.setStatus(_A)
_LldpV2RemEntry_Object=MibTableRow
lldpV2RemEntry=_LldpV2RemEntry_Object((1,3,111,2,802,1,1,13,1,4,1,1))
lldpV2RemEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:lldpV2RemEntry.setStatus(_A)
_LldpV2RemTimeMark_Type=TimeFilter
_LldpV2RemTimeMark_Object=MibTableColumn
lldpV2RemTimeMark=_LldpV2RemTimeMark_Object((1,3,111,2,802,1,1,13,1,4,1,1,1),_LldpV2RemTimeMark_Type())
lldpV2RemTimeMark.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2RemTimeMark.setStatus(_A)
_LldpV2RemLocalIfIndex_Type=InterfaceIndex
_LldpV2RemLocalIfIndex_Object=MibTableColumn
lldpV2RemLocalIfIndex=_LldpV2RemLocalIfIndex_Object((1,3,111,2,802,1,1,13,1,4,1,1,2),_LldpV2RemLocalIfIndex_Type())
lldpV2RemLocalIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2RemLocalIfIndex.setStatus(_A)
_LldpV2RemLocalDestMACAddress_Type=LldpV2DestAddressTableIndex
_LldpV2RemLocalDestMACAddress_Object=MibTableColumn
lldpV2RemLocalDestMACAddress=_LldpV2RemLocalDestMACAddress_Object((1,3,111,2,802,1,1,13,1,4,1,1,3),_LldpV2RemLocalDestMACAddress_Type())
lldpV2RemLocalDestMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2RemLocalDestMACAddress.setStatus(_A)
class _LldpV2RemIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LldpV2RemIndex_Type.__name__=_F
_LldpV2RemIndex_Object=MibTableColumn
lldpV2RemIndex=_LldpV2RemIndex_Object((1,3,111,2,802,1,1,13,1,4,1,1,4),_LldpV2RemIndex_Type())
lldpV2RemIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2RemIndex.setStatus(_A)
_LldpV2RemChassisIdSubtype_Type=LldpV2ChassisIdSubtype
_LldpV2RemChassisIdSubtype_Object=MibTableColumn
lldpV2RemChassisIdSubtype=_LldpV2RemChassisIdSubtype_Object((1,3,111,2,802,1,1,13,1,4,1,1,5),_LldpV2RemChassisIdSubtype_Type())
lldpV2RemChassisIdSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemChassisIdSubtype.setStatus(_A)
_LldpV2RemChassisId_Type=LldpV2ChassisId
_LldpV2RemChassisId_Object=MibTableColumn
lldpV2RemChassisId=_LldpV2RemChassisId_Object((1,3,111,2,802,1,1,13,1,4,1,1,6),_LldpV2RemChassisId_Type())
lldpV2RemChassisId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemChassisId.setStatus(_A)
_LldpV2RemPortIdSubtype_Type=LldpV2PortIdSubtype
_LldpV2RemPortIdSubtype_Object=MibTableColumn
lldpV2RemPortIdSubtype=_LldpV2RemPortIdSubtype_Object((1,3,111,2,802,1,1,13,1,4,1,1,7),_LldpV2RemPortIdSubtype_Type())
lldpV2RemPortIdSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemPortIdSubtype.setStatus(_A)
_LldpV2RemPortId_Type=LldpV2PortId
_LldpV2RemPortId_Object=MibTableColumn
lldpV2RemPortId=_LldpV2RemPortId_Object((1,3,111,2,802,1,1,13,1,4,1,1,8),_LldpV2RemPortId_Type())
lldpV2RemPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemPortId.setStatus(_A)
class _LldpV2RemPortDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpV2RemPortDesc_Type.__name__=_H
_LldpV2RemPortDesc_Object=MibTableColumn
lldpV2RemPortDesc=_LldpV2RemPortDesc_Object((1,3,111,2,802,1,1,13,1,4,1,1,9),_LldpV2RemPortDesc_Type())
lldpV2RemPortDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemPortDesc.setStatus(_A)
class _LldpV2RemSysName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpV2RemSysName_Type.__name__=_H
_LldpV2RemSysName_Object=MibTableColumn
lldpV2RemSysName=_LldpV2RemSysName_Object((1,3,111,2,802,1,1,13,1,4,1,1,10),_LldpV2RemSysName_Type())
lldpV2RemSysName.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemSysName.setStatus(_A)
class _LldpV2RemSysDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpV2RemSysDesc_Type.__name__=_H
_LldpV2RemSysDesc_Object=MibTableColumn
lldpV2RemSysDesc=_LldpV2RemSysDesc_Object((1,3,111,2,802,1,1,13,1,4,1,1,11),_LldpV2RemSysDesc_Type())
lldpV2RemSysDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemSysDesc.setStatus(_A)
_LldpV2RemSysCapSupported_Type=LldpV2SystemCapabilitiesMap
_LldpV2RemSysCapSupported_Object=MibTableColumn
lldpV2RemSysCapSupported=_LldpV2RemSysCapSupported_Object((1,3,111,2,802,1,1,13,1,4,1,1,12),_LldpV2RemSysCapSupported_Type())
lldpV2RemSysCapSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemSysCapSupported.setStatus(_A)
_LldpV2RemSysCapEnabled_Type=LldpV2SystemCapabilitiesMap
_LldpV2RemSysCapEnabled_Object=MibTableColumn
lldpV2RemSysCapEnabled=_LldpV2RemSysCapEnabled_Object((1,3,111,2,802,1,1,13,1,4,1,1,13),_LldpV2RemSysCapEnabled_Type())
lldpV2RemSysCapEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemSysCapEnabled.setStatus(_A)
_LldpV2RemRemoteChanges_Type=TruthValue
_LldpV2RemRemoteChanges_Object=MibTableColumn
lldpV2RemRemoteChanges=_LldpV2RemRemoteChanges_Object((1,3,111,2,802,1,1,13,1,4,1,1,14),_LldpV2RemRemoteChanges_Type())
lldpV2RemRemoteChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemRemoteChanges.setStatus(_A)
_LldpV2RemTooManyNeighbors_Type=TruthValue
_LldpV2RemTooManyNeighbors_Object=MibTableColumn
lldpV2RemTooManyNeighbors=_LldpV2RemTooManyNeighbors_Object((1,3,111,2,802,1,1,13,1,4,1,1,15),_LldpV2RemTooManyNeighbors_Type())
lldpV2RemTooManyNeighbors.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemTooManyNeighbors.setStatus(_A)
_LldpV2RemManAddrTable_Object=MibTable
lldpV2RemManAddrTable=_LldpV2RemManAddrTable_Object((1,3,111,2,802,1,1,13,1,4,2))
if mibBuilder.loadTexts:lldpV2RemManAddrTable.setStatus(_A)
_LldpV2RemManAddrEntry_Object=MibTableRow
lldpV2RemManAddrEntry=_LldpV2RemManAddrEntry_Object((1,3,111,2,802,1,1,13,1,4,2,1))
lldpV2RemManAddrEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N),(0,_B,_x),(0,_B,_y))
if mibBuilder.loadTexts:lldpV2RemManAddrEntry.setStatus(_A)
_LldpV2RemManAddrSubtype_Type=AddressFamilyNumbers
_LldpV2RemManAddrSubtype_Object=MibTableColumn
lldpV2RemManAddrSubtype=_LldpV2RemManAddrSubtype_Object((1,3,111,2,802,1,1,13,1,4,2,1,1),_LldpV2RemManAddrSubtype_Type())
lldpV2RemManAddrSubtype.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2RemManAddrSubtype.setStatus(_A)
_LldpV2RemManAddr_Type=LldpV2ManAddress
_LldpV2RemManAddr_Object=MibTableColumn
lldpV2RemManAddr=_LldpV2RemManAddr_Object((1,3,111,2,802,1,1,13,1,4,2,1,2),_LldpV2RemManAddr_Type())
lldpV2RemManAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2RemManAddr.setStatus(_A)
_LldpV2RemManAddrIfSubtype_Type=LldpV2ManAddrIfSubtype
_LldpV2RemManAddrIfSubtype_Object=MibTableColumn
lldpV2RemManAddrIfSubtype=_LldpV2RemManAddrIfSubtype_Object((1,3,111,2,802,1,1,13,1,4,2,1,3),_LldpV2RemManAddrIfSubtype_Type())
lldpV2RemManAddrIfSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemManAddrIfSubtype.setStatus(_A)
_LldpV2RemManAddrIfId_Type=Unsigned32
_LldpV2RemManAddrIfId_Object=MibTableColumn
lldpV2RemManAddrIfId=_LldpV2RemManAddrIfId_Object((1,3,111,2,802,1,1,13,1,4,2,1,4),_LldpV2RemManAddrIfId_Type())
lldpV2RemManAddrIfId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemManAddrIfId.setStatus(_A)
_LldpV2RemManAddrOID_Type=ObjectIdentifier
_LldpV2RemManAddrOID_Object=MibTableColumn
lldpV2RemManAddrOID=_LldpV2RemManAddrOID_Object((1,3,111,2,802,1,1,13,1,4,2,1,5),_LldpV2RemManAddrOID_Type())
lldpV2RemManAddrOID.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemManAddrOID.setStatus(_A)
_LldpV2RemUnknownTLVTable_Object=MibTable
lldpV2RemUnknownTLVTable=_LldpV2RemUnknownTLVTable_Object((1,3,111,2,802,1,1,13,1,4,3))
if mibBuilder.loadTexts:lldpV2RemUnknownTLVTable.setStatus(_A)
_LldpV2RemUnknownTLVEntry_Object=MibTableRow
lldpV2RemUnknownTLVEntry=_LldpV2RemUnknownTLVEntry_Object((1,3,111,2,802,1,1,13,1,4,3,1))
lldpV2RemUnknownTLVEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N),(0,_B,_z))
if mibBuilder.loadTexts:lldpV2RemUnknownTLVEntry.setStatus(_A)
class _LldpV2RemUnknownTLVType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(9,126))
_LldpV2RemUnknownTLVType_Type.__name__=_F
_LldpV2RemUnknownTLVType_Object=MibTableColumn
lldpV2RemUnknownTLVType=_LldpV2RemUnknownTLVType_Object((1,3,111,2,802,1,1,13,1,4,3,1,1),_LldpV2RemUnknownTLVType_Type())
lldpV2RemUnknownTLVType.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2RemUnknownTLVType.setStatus(_A)
class _LldpV2RemUnknownTLVInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,511))
_LldpV2RemUnknownTLVInfo_Type.__name__=_O
_LldpV2RemUnknownTLVInfo_Object=MibTableColumn
lldpV2RemUnknownTLVInfo=_LldpV2RemUnknownTLVInfo_Object((1,3,111,2,802,1,1,13,1,4,3,1,2),_LldpV2RemUnknownTLVInfo_Type())
lldpV2RemUnknownTLVInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemUnknownTLVInfo.setStatus(_A)
_LldpV2RemOrgDefInfoTable_Object=MibTable
lldpV2RemOrgDefInfoTable=_LldpV2RemOrgDefInfoTable_Object((1,3,111,2,802,1,1,13,1,4,4))
if mibBuilder.loadTexts:lldpV2RemOrgDefInfoTable.setStatus(_A)
_LldpV2RemOrgDefInfoEntry_Object=MibTableRow
lldpV2RemOrgDefInfoEntry=_LldpV2RemOrgDefInfoEntry_Object((1,3,111,2,802,1,1,13,1,4,4,1))
lldpV2RemOrgDefInfoEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N),(0,_B,_A0),(0,_B,_A1),(0,_B,_A2))
if mibBuilder.loadTexts:lldpV2RemOrgDefInfoEntry.setStatus(_A)
class _LldpV2RemOrgDefInfoOUI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_LldpV2RemOrgDefInfoOUI_Type.__name__=_O
_LldpV2RemOrgDefInfoOUI_Object=MibTableColumn
lldpV2RemOrgDefInfoOUI=_LldpV2RemOrgDefInfoOUI_Object((1,3,111,2,802,1,1,13,1,4,4,1,1),_LldpV2RemOrgDefInfoOUI_Type())
lldpV2RemOrgDefInfoOUI.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2RemOrgDefInfoOUI.setStatus(_A)
class _LldpV2RemOrgDefInfoSubtype_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_LldpV2RemOrgDefInfoSubtype_Type.__name__=_F
_LldpV2RemOrgDefInfoSubtype_Object=MibTableColumn
lldpV2RemOrgDefInfoSubtype=_LldpV2RemOrgDefInfoSubtype_Object((1,3,111,2,802,1,1,13,1,4,4,1,2),_LldpV2RemOrgDefInfoSubtype_Type())
lldpV2RemOrgDefInfoSubtype.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2RemOrgDefInfoSubtype.setStatus(_A)
class _LldpV2RemOrgDefInfoIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LldpV2RemOrgDefInfoIndex_Type.__name__=_F
_LldpV2RemOrgDefInfoIndex_Object=MibTableColumn
lldpV2RemOrgDefInfoIndex=_LldpV2RemOrgDefInfoIndex_Object((1,3,111,2,802,1,1,13,1,4,4,1,3),_LldpV2RemOrgDefInfoIndex_Type())
lldpV2RemOrgDefInfoIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpV2RemOrgDefInfoIndex.setStatus(_A)
class _LldpV2RemOrgDefInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,507))
_LldpV2RemOrgDefInfo_Type.__name__=_O
_LldpV2RemOrgDefInfo_Object=MibTableColumn
lldpV2RemOrgDefInfo=_LldpV2RemOrgDefInfo_Object((1,3,111,2,802,1,1,13,1,4,4,1,4),_LldpV2RemOrgDefInfo_Type())
lldpV2RemOrgDefInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2RemOrgDefInfo.setStatus(_A)
_LldpV2Extensions_ObjectIdentity=ObjectIdentity
lldpV2Extensions=_LldpV2Extensions_ObjectIdentity((1,3,111,2,802,1,1,13,1,5))
_LldpV2Conformance_ObjectIdentity=ObjectIdentity
lldpV2Conformance=_LldpV2Conformance_ObjectIdentity((1,3,111,2,802,1,1,13,2))
_LldpV2Compliances_ObjectIdentity=ObjectIdentity
lldpV2Compliances=_LldpV2Compliances_ObjectIdentity((1,3,111,2,802,1,1,13,2,1))
_LldpV2Groups_ObjectIdentity=ObjectIdentity
lldpV2Groups=_LldpV2Groups_ObjectIdentity((1,3,111,2,802,1,1,13,2,2))
lldpV2ConfigGroup=ObjectGroup((1,3,111,2,802,1,1,13,2,2,1))
lldpV2ConfigGroup.setObjects((_B,_A3))
if mibBuilder.loadTexts:lldpV2ConfigGroup.setStatus(_A)
lldpV2ConfigRxGroup=ObjectGroup((1,3,111,2,802,1,1,13,2,2,2))
lldpV2ConfigRxGroup.setObjects(*((_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:lldpV2ConfigRxGroup.setStatus(_A)
lldpV2ConfigTxGroup=ObjectGroup((1,3,111,2,802,1,1,13,2,2,3))
lldpV2ConfigTxGroup.setObjects(*((_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM)))
if mibBuilder.loadTexts:lldpV2ConfigTxGroup.setStatus(_A)
lldpV2StatsRxGroup=ObjectGroup((1,3,111,2,802,1,1,13,2,2,4))
lldpV2StatsRxGroup.setObjects(*((_B,_AN),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT)))
if mibBuilder.loadTexts:lldpV2StatsRxGroup.setStatus(_A)
lldpV2StatsTxGroup=ObjectGroup((1,3,111,2,802,1,1,13,2,2,5))
lldpV2StatsTxGroup.setObjects(*((_B,_AU),(_B,_AV)))
if mibBuilder.loadTexts:lldpV2StatsTxGroup.setStatus(_A)
lldpV2LocSysGroup=ObjectGroup((1,3,111,2,802,1,1,13,2,2,6))
lldpV2LocSysGroup.setObjects(*((_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai)))
if mibBuilder.loadTexts:lldpV2LocSysGroup.setStatus(_A)
lldpV2RemSysGroup=ObjectGroup((1,3,111,2,802,1,1,13,2,2,7))
lldpV2RemSysGroup.setObjects(*((_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax),(_B,_Ay)))
if mibBuilder.loadTexts:lldpV2RemSysGroup.setStatus(_A)
lldpV2RemTablesChange=NotificationType((1,3,111,2,802,1,1,13,0,0,1))
lldpV2RemTablesChange.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:lldpV2RemTablesChange.setStatus(_A)
lldpV2NotificationsGroup=NotificationGroup((1,3,111,2,802,1,1,13,2,2,8))
lldpV2NotificationsGroup.setObjects((_B,_Az))
if mibBuilder.loadTexts:lldpV2NotificationsGroup.setStatus(_A)
lldpV2TxRxCompliance=ModuleCompliance((1,3,111,2,802,1,1,13,2,1,1))
lldpV2TxRxCompliance.setObjects(*((_B,_A_),(_B,_X)))
if mibBuilder.loadTexts:lldpV2TxRxCompliance.setStatus(_A)
lldpV2TxCompliance=ModuleCompliance((1,3,111,2,802,1,1,13,2,1,2))
lldpV2TxCompliance.setObjects(*((_B,_B0),(_B,_B1),(_B,_B2)))
if mibBuilder.loadTexts:lldpV2TxCompliance.setStatus(_A)
lldpV2RxCompliance=ModuleCompliance((1,3,111,2,802,1,1,13,2,1,3))
lldpV2RxCompliance.setObjects(*((_B,_B3),(_B,_B4),(_B,_B5),(_B,_B6)))
if mibBuilder.loadTexts:lldpV2RxCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lldpV2MIB':lldpV2MIB,'lldpV2Notifications':lldpV2Notifications,'lldpV2NotificationPrefix':lldpV2NotificationPrefix,_Az:lldpV2RemTablesChange,'lldpV2Objects':lldpV2Objects,'lldpV2Configuration':lldpV2Configuration,_A6:lldpV2MessageTxInterval,_A7:lldpV2MessageTxHoldMultiplier,_A8:lldpV2ReinitDelay,_A4:lldpV2NotificationInterval,_AC:lldpV2TxCreditMax,_AD:lldpV2MessageFastTx,_AE:lldpV2TxFastInit,'lldpV2PortConfigTable':lldpV2PortConfigTable,'lldpV2PortConfigEntry':lldpV2PortConfigEntry,_Y:lldpV2PortConfigIfIndex,_Z:lldpV2PortConfigDestAddressIndex,'lldpV2PortConfigAdminStatus':lldpV2PortConfigAdminStatus,'lldpV2PortConfigNotificationEnable':lldpV2PortConfigNotificationEnable,'lldpV2PortConfigTLVsTxEnable':lldpV2PortConfigTLVsTxEnable,'lldpV2DestAddressTable':lldpV2DestAddressTable,'lldpV2DestAddressTableEntry':lldpV2DestAddressTableEntry,_i:lldpV2AddressTableIndex,_AF:lldpV2DestMacAddress,'lldpV2ManAddrConfigTxPortsTable':lldpV2ManAddrConfigTxPortsTable,'lldpV2ManAddrConfigTxPortsEntry':lldpV2ManAddrConfigTxPortsEntry,_j:lldpV2ManAddrConfigIfIndex,_k:lldpV2ManAddrConfigDestAddressIndex,_l:lldpV2ManAddrConfigLocManAddrSubtype,_m:lldpV2ManAddrConfigLocManAddr,_AA:lldpV2ManAddrConfigTxEnable,_AB:lldpV2ManAddrConfigRowStatus,'lldpV2PortConfigTableV2':lldpV2PortConfigTableV2,'lldpV2PortConfigEntryV2':lldpV2PortConfigEntryV2,_o:lldpV2PortConfigIfIndexV2,_p:lldpV2PortConfigDestAddressIndexV2,_A3:lldpV2PortConfigAdminStatusV2,_AG:lldpV2PortMessageTxInterval,_AH:lldpV2PortMessageTxHoldMultiplier,_AI:lldpV2PortReinitDelay,_AJ:lldpV2PortNotificationInterval,_AK:lldpV2PortTxCreditMax,_AL:lldpV2PortMessageFastTx,_AM:lldpV2PortTxFastInit,_A5:lldpV2PortConfigNotificationEnableV2,_A9:lldpV2PortConfigTLVsTxEnableV2,'lldpV2Statistics':lldpV2Statistics,_AN:lldpV2StatsRemTablesLastChangeTime,_T:lldpV2StatsRemTablesInserts,_U:lldpV2StatsRemTablesDeletes,_V:lldpV2StatsRemTablesDrops,_W:lldpV2StatsRemTablesAgeouts,'lldpV2StatsTxPortTable':lldpV2StatsTxPortTable,'lldpV2StatsTxPortEntry':lldpV2StatsTxPortEntry,_q:lldpV2StatsTxIfIndex,_r:lldpV2StatsTxDestMACAddress,_AU:lldpV2StatsTxPortFramesTotal,_AV:lldpV2StatsTxLLDPDULengthErrors,'lldpV2StatsRxPortTable':lldpV2StatsRxPortTable,'lldpV2StatsRxPortEntry':lldpV2StatsRxPortEntry,_s:lldpV2StatsRxDestIfIndex,_t:lldpV2StatsRxDestMACAddress,_AO:lldpV2StatsRxPortFramesDiscardedTotal,_AP:lldpV2StatsRxPortFramesErrors,_AQ:lldpV2StatsRxPortFramesTotal,_AR:lldpV2StatsRxPortTLVsDiscardedTotal,_AS:lldpV2StatsRxPortTLVsUnrecognizedTotal,_AT:lldpV2StatsRxPortAgeoutsTotal,'lldpV2LocalSystemData':lldpV2LocalSystemData,_AW:lldpV2LocChassisIdSubtype,_AX:lldpV2LocChassisId,_Ac:lldpV2LocSysName,_Ab:lldpV2LocSysDesc,_Ad:lldpV2LocSysCapSupported,_Ae:lldpV2LocSysCapEnabled,'lldpV2LocPortTable':lldpV2LocPortTable,'lldpV2LocPortEntry':lldpV2LocPortEntry,_u:lldpV2LocPortIfIndex,_AY:lldpV2LocPortIdSubtype,_AZ:lldpV2LocPortId,_Aa:lldpV2LocPortDesc,'lldpV2LocManAddrTable':lldpV2LocManAddrTable,'lldpV2LocManAddrEntry':lldpV2LocManAddrEntry,_v:lldpV2LocManAddrSubtype,_w:lldpV2LocManAddr,_Af:lldpV2LocManAddrLen,_Ag:lldpV2LocManAddrIfSubtype,_Ah:lldpV2LocManAddrIfId,_Ai:lldpV2LocManAddrOID,'lldpV2RemoteSystemsData':lldpV2RemoteSystemsData,'lldpV2RemTable':lldpV2RemTable,'lldpV2RemEntry':lldpV2RemEntry,_K:lldpV2RemTimeMark,_L:lldpV2RemLocalIfIndex,_M:lldpV2RemLocalDestMACAddress,_N:lldpV2RemIndex,_Aj:lldpV2RemChassisIdSubtype,_Ak:lldpV2RemChassisId,_Al:lldpV2RemPortIdSubtype,_Am:lldpV2RemPortId,_An:lldpV2RemPortDesc,_Ao:lldpV2RemSysName,_Ap:lldpV2RemSysDesc,_Aq:lldpV2RemSysCapSupported,_Ar:lldpV2RemSysCapEnabled,_As:lldpV2RemRemoteChanges,_At:lldpV2RemTooManyNeighbors,'lldpV2RemManAddrTable':lldpV2RemManAddrTable,'lldpV2RemManAddrEntry':lldpV2RemManAddrEntry,_x:lldpV2RemManAddrSubtype,_y:lldpV2RemManAddr,_Au:lldpV2RemManAddrIfSubtype,_Av:lldpV2RemManAddrIfId,_Aw:lldpV2RemManAddrOID,'lldpV2RemUnknownTLVTable':lldpV2RemUnknownTLVTable,'lldpV2RemUnknownTLVEntry':lldpV2RemUnknownTLVEntry,_z:lldpV2RemUnknownTLVType,_Ax:lldpV2RemUnknownTLVInfo,'lldpV2RemOrgDefInfoTable':lldpV2RemOrgDefInfoTable,'lldpV2RemOrgDefInfoEntry':lldpV2RemOrgDefInfoEntry,_A0:lldpV2RemOrgDefInfoOUI,_A1:lldpV2RemOrgDefInfoSubtype,_A2:lldpV2RemOrgDefInfoIndex,_Ay:lldpV2RemOrgDefInfo,'lldpV2Extensions':lldpV2Extensions,'lldpV2Conformance':lldpV2Conformance,'lldpV2Compliances':lldpV2Compliances,'lldpV2TxRxCompliance':lldpV2TxRxCompliance,'lldpV2TxCompliance':lldpV2TxCompliance,'lldpV2RxCompliance':lldpV2RxCompliance,'lldpV2Groups':lldpV2Groups,_A_:lldpV2ConfigGroup,_B3:lldpV2ConfigRxGroup,_B0:lldpV2ConfigTxGroup,_B4:lldpV2StatsRxGroup,_B1:lldpV2StatsTxGroup,_B2:lldpV2LocSysGroup,_B5:lldpV2RemSysGroup,_B6:lldpV2NotificationsGroup})