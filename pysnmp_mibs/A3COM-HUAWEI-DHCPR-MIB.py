_a='hwDHCPRelayStatisticsReset'
_Z='hwDHCPRelayNakPktNum'
_Y='hwDHCPRelayAckPktNum'
_X='hwDHCPRelayOfferPktNum'
_W='hwDHCPRelayInformPktNum'
_V='hwDHCPRelayReleasePktNum'
_U='hwDHCPRelayDeclinePktNum'
_T='hwDHCPRelayRequestPktNum'
_S='hwDHCPRelayDiscoverPktNum'
_R='hwDHCPRTxClientBroPktNum'
_Q='hwDHCPRTxClientUniPktNum'
_P='hwDHCPRTxClientPktNum'
_O='hwDHCPRRxClientPktNum'
_N='hwDHCPRTxServerPktNum'
_M='hwDHCPRRxServerPktNum'
_L='hwDHCPRRxBadPktNum'
_K='hwDHCPRelayCycleStatus'
_J='hwDHCPRSelectAllocateMode'
_I='hwDHCPRIPRowStatus'
_H='read-write'
_G='hwDHCPRIPAddr'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-only'
_B='A3COM-HUAWEI-DHCPR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
huaweiMgmt,hwDhcp=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','huaweiMgmt','hwDhcp')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hwDHCPRelayMib=ModuleIdentity((1,3,6,1,4,1,43,45,1,5,7,1))
if mibBuilder.loadTexts:hwDHCPRelayMib.setRevisions(('2003-02-12 00:00',))
_HwDHCPRelayMibObject_ObjectIdentity=ObjectIdentity
hwDHCPRelayMibObject=_HwDHCPRelayMibObject_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,7,1,1))
_HwDHCPRIPTable_Object=MibTable
hwDHCPRIPTable=_HwDHCPRIPTable_Object((1,3,6,1,4,1,43,45,1,5,7,1,1,1))
if mibBuilder.loadTexts:hwDHCPRIPTable.setStatus(_A)
_HwDHCPRIPEntry_Object=MibTableRow
hwDHCPRIPEntry=_HwDHCPRIPEntry_Object((1,3,6,1,4,1,43,45,1,5,7,1,1,1,1))
hwDHCPRIPEntry.setIndexNames((0,_E,_F),(0,_B,_G))
if mibBuilder.loadTexts:hwDHCPRIPEntry.setStatus(_A)
_HwDHCPRIPAddr_Type=IpAddress
_HwDHCPRIPAddr_Object=MibTableColumn
hwDHCPRIPAddr=_HwDHCPRIPAddr_Object((1,3,6,1,4,1,43,45,1,5,7,1,1,1,1,1),_HwDHCPRIPAddr_Type())
hwDHCPRIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hwDHCPRIPAddr.setStatus(_A)
_HwDHCPRIPRowStatus_Type=RowStatus
_HwDHCPRIPRowStatus_Object=MibTableColumn
hwDHCPRIPRowStatus=_HwDHCPRIPRowStatus_Object((1,3,6,1,4,1,43,45,1,5,7,1,1,1,1,2),_HwDHCPRIPRowStatus_Type())
hwDHCPRIPRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:hwDHCPRIPRowStatus.setStatus(_A)
_HwDHCPRSeletAllocateModeTable_Object=MibTable
hwDHCPRSeletAllocateModeTable=_HwDHCPRSeletAllocateModeTable_Object((1,3,6,1,4,1,43,45,1,5,7,1,1,2))
if mibBuilder.loadTexts:hwDHCPRSeletAllocateModeTable.setStatus(_A)
_HwDHCPRSeletAllocateModeEntry_Object=MibTableRow
hwDHCPRSeletAllocateModeEntry=_HwDHCPRSeletAllocateModeEntry_Object((1,3,6,1,4,1,43,45,1,5,7,1,1,2,1))
hwDHCPRSeletAllocateModeEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hwDHCPRSeletAllocateModeEntry.setStatus(_A)
class _HwDHCPRSelectAllocateMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('global',0),('interface',1),('relay',2)))
_HwDHCPRSelectAllocateMode_Type.__name__=_D
_HwDHCPRSelectAllocateMode_Object=MibTableColumn
hwDHCPRSelectAllocateMode=_HwDHCPRSelectAllocateMode_Object((1,3,6,1,4,1,43,45,1,5,7,1,1,2,1,1),_HwDHCPRSelectAllocateMode_Type())
hwDHCPRSelectAllocateMode.setMaxAccess(_H)
if mibBuilder.loadTexts:hwDHCPRSelectAllocateMode.setStatus(_A)
class _HwDHCPRelayCycleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('on',0),('off',1)))
_HwDHCPRelayCycleStatus_Type.__name__=_D
_HwDHCPRelayCycleStatus_Object=MibScalar
hwDHCPRelayCycleStatus=_HwDHCPRelayCycleStatus_Object((1,3,6,1,4,1,43,45,1,5,7,1,1,3),_HwDHCPRelayCycleStatus_Type())
hwDHCPRelayCycleStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hwDHCPRelayCycleStatus.setStatus(_A)
_HwDHCPRRxBadPktNum_Type=Integer32
_HwDHCPRRxBadPktNum_Object=MibScalar
hwDHCPRRxBadPktNum=_HwDHCPRRxBadPktNum_Object((1,3,6,1,4,1,43,45,1,5,7,1,1,4),_HwDHCPRRxBadPktNum_Type())
hwDHCPRRxBadPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwDHCPRRxBadPktNum.setStatus(_A)
_HwDHCPRRxServerPktNum_Type=Integer32
_HwDHCPRRxServerPktNum_Object=MibScalar
hwDHCPRRxServerPktNum=_HwDHCPRRxServerPktNum_Object((1,3,6,1,4,1,43,45,1,5,7,1,1,5),_HwDHCPRRxServerPktNum_Type())
hwDHCPRRxServerPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwDHCPRRxServerPktNum.setStatus(_A)
_HwDHCPRTxServerPktNum_Type=Integer32
_HwDHCPRTxServerPktNum_Object=MibScalar
hwDHCPRTxServerPktNum=_HwDHCPRTxServerPktNum_Object((1,3,6,1,4,1,43,45,1,5,7,1,1,6),_HwDHCPRTxServerPktNum_Type())
hwDHCPRTxServerPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwDHCPRTxServerPktNum.setStatus(_A)
_HwDHCPRRxClientPktNum_Type=Integer32
_HwDHCPRRxClientPktNum_Object=MibScalar
hwDHCPRRxClientPktNum=_HwDHCPRRxClientPktNum_Object((1,3,6,1,4,1,43,45,1,5,7,1,1,7),_HwDHCPRRxClientPktNum_Type())
hwDHCPRRxClientPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwDHCPRRxClientPktNum.setStatus(_A)
_HwDHCPRTxClientPktNum_Type=Integer32
_HwDHCPRTxClientPktNum_Object=MibScalar
hwDHCPRTxClientPktNum=_HwDHCPRTxClientPktNum_Object((1,3,6,1,4,1,43,45,1,5,7,1,1,8),_HwDHCPRTxClientPktNum_Type())
hwDHCPRTxClientPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwDHCPRTxClientPktNum.setStatus(_A)
_HwDHCPRTxClientUniPktNum_Type=Integer32
_HwDHCPRTxClientUniPktNum_Object=MibScalar
hwDHCPRTxClientUniPktNum=_HwDHCPRTxClientUniPktNum_Object((1,3,6,1,4,1,43,45,1,5,7,1,1,9),_HwDHCPRTxClientUniPktNum_Type())
hwDHCPRTxClientUniPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwDHCPRTxClientUniPktNum.setStatus(_A)
_HwDHCPRTxClientBroPktNum_Type=Integer32
_HwDHCPRTxClientBroPktNum_Object=MibScalar
hwDHCPRTxClientBroPktNum=_HwDHCPRTxClientBroPktNum_Object((1,3,6,1,4,1,43,45,1,5,7,1,1,10),_HwDHCPRTxClientBroPktNum_Type())
hwDHCPRTxClientBroPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwDHCPRTxClientBroPktNum.setStatus(_A)
_HwDHCPRelayDiscoverPktNum_Type=Integer32
_HwDHCPRelayDiscoverPktNum_Object=MibScalar
hwDHCPRelayDiscoverPktNum=_HwDHCPRelayDiscoverPktNum_Object((1,3,6,1,4,1,43,45,1,5,7,1,1,11),_HwDHCPRelayDiscoverPktNum_Type())
hwDHCPRelayDiscoverPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwDHCPRelayDiscoverPktNum.setStatus(_A)
_HwDHCPRelayRequestPktNum_Type=Integer32
_HwDHCPRelayRequestPktNum_Object=MibScalar
hwDHCPRelayRequestPktNum=_HwDHCPRelayRequestPktNum_Object((1,3,6,1,4,1,43,45,1,5,7,1,1,12),_HwDHCPRelayRequestPktNum_Type())
hwDHCPRelayRequestPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwDHCPRelayRequestPktNum.setStatus(_A)
_HwDHCPRelayDeclinePktNum_Type=Integer32
_HwDHCPRelayDeclinePktNum_Object=MibScalar
hwDHCPRelayDeclinePktNum=_HwDHCPRelayDeclinePktNum_Object((1,3,6,1,4,1,43,45,1,5,7,1,1,13),_HwDHCPRelayDeclinePktNum_Type())
hwDHCPRelayDeclinePktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwDHCPRelayDeclinePktNum.setStatus(_A)
_HwDHCPRelayReleasePktNum_Type=Integer32
_HwDHCPRelayReleasePktNum_Object=MibScalar
hwDHCPRelayReleasePktNum=_HwDHCPRelayReleasePktNum_Object((1,3,6,1,4,1,43,45,1,5,7,1,1,14),_HwDHCPRelayReleasePktNum_Type())
hwDHCPRelayReleasePktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwDHCPRelayReleasePktNum.setStatus(_A)
_HwDHCPRelayInformPktNum_Type=Integer32
_HwDHCPRelayInformPktNum_Object=MibScalar
hwDHCPRelayInformPktNum=_HwDHCPRelayInformPktNum_Object((1,3,6,1,4,1,43,45,1,5,7,1,1,15),_HwDHCPRelayInformPktNum_Type())
hwDHCPRelayInformPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwDHCPRelayInformPktNum.setStatus(_A)
_HwDHCPRelayOfferPktNum_Type=Integer32
_HwDHCPRelayOfferPktNum_Object=MibScalar
hwDHCPRelayOfferPktNum=_HwDHCPRelayOfferPktNum_Object((1,3,6,1,4,1,43,45,1,5,7,1,1,16),_HwDHCPRelayOfferPktNum_Type())
hwDHCPRelayOfferPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwDHCPRelayOfferPktNum.setStatus(_A)
_HwDHCPRelayAckPktNum_Type=Integer32
_HwDHCPRelayAckPktNum_Object=MibScalar
hwDHCPRelayAckPktNum=_HwDHCPRelayAckPktNum_Object((1,3,6,1,4,1,43,45,1,5,7,1,1,17),_HwDHCPRelayAckPktNum_Type())
hwDHCPRelayAckPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwDHCPRelayAckPktNum.setStatus(_A)
_HwDHCPRelayNakPktNum_Type=Integer32
_HwDHCPRelayNakPktNum_Object=MibScalar
hwDHCPRelayNakPktNum=_HwDHCPRelayNakPktNum_Object((1,3,6,1,4,1,43,45,1,5,7,1,1,18),_HwDHCPRelayNakPktNum_Type())
hwDHCPRelayNakPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwDHCPRelayNakPktNum.setStatus(_A)
class _HwDHCPRelayStatisticsReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('invalid',0),('reset',1)))
_HwDHCPRelayStatisticsReset_Type.__name__=_D
_HwDHCPRelayStatisticsReset_Object=MibScalar
hwDHCPRelayStatisticsReset=_HwDHCPRelayStatisticsReset_Object((1,3,6,1,4,1,43,45,1,5,7,1,1,19),_HwDHCPRelayStatisticsReset_Type())
hwDHCPRelayStatisticsReset.setMaxAccess(_H)
if mibBuilder.loadTexts:hwDHCPRelayStatisticsReset.setStatus(_A)
_HwDHCPRelayMIBConformance_ObjectIdentity=ObjectIdentity
hwDHCPRelayMIBConformance=_HwDHCPRelayMIBConformance_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,7,1,2))
_HwDHCPRelayMIBCompliances_ObjectIdentity=ObjectIdentity
hwDHCPRelayMIBCompliances=_HwDHCPRelayMIBCompliances_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,7,1,2,1))
_HwDHCPRelayMIBGroups_ObjectIdentity=ObjectIdentity
hwDHCPRelayMIBGroups=_HwDHCPRelayMIBGroups_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,7,1,2,2))
hwDHCPRelayMIBGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,5,7,1,2,2,1))
hwDHCPRelayMIBGroup.setObjects(*((_B,_G),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:hwDHCPRelayMIBGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hwDHCPRelayMib':hwDHCPRelayMib,'hwDHCPRelayMibObject':hwDHCPRelayMibObject,'hwDHCPRIPTable':hwDHCPRIPTable,'hwDHCPRIPEntry':hwDHCPRIPEntry,_G:hwDHCPRIPAddr,_I:hwDHCPRIPRowStatus,'hwDHCPRSeletAllocateModeTable':hwDHCPRSeletAllocateModeTable,'hwDHCPRSeletAllocateModeEntry':hwDHCPRSeletAllocateModeEntry,_J:hwDHCPRSelectAllocateMode,_K:hwDHCPRelayCycleStatus,_L:hwDHCPRRxBadPktNum,_M:hwDHCPRRxServerPktNum,_N:hwDHCPRTxServerPktNum,_O:hwDHCPRRxClientPktNum,_P:hwDHCPRTxClientPktNum,_Q:hwDHCPRTxClientUniPktNum,_R:hwDHCPRTxClientBroPktNum,_S:hwDHCPRelayDiscoverPktNum,_T:hwDHCPRelayRequestPktNum,_U:hwDHCPRelayDeclinePktNum,_V:hwDHCPRelayReleasePktNum,_W:hwDHCPRelayInformPktNum,_X:hwDHCPRelayOfferPktNum,_Y:hwDHCPRelayAckPktNum,_Z:hwDHCPRelayNakPktNum,_a:hwDHCPRelayStatisticsReset,'hwDHCPRelayMIBConformance':hwDHCPRelayMIBConformance,'hwDHCPRelayMIBCompliances':hwDHCPRelayMIBCompliances,'hwDHCPRelayMIBGroups':hwDHCPRelayMIBGroups,'hwDHCPRelayMIBGroup':hwDHCPRelayMIBGroup})