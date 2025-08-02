_a='hpnicfDHCPRelayStatisticsReset'
_Z='hpnicfDHCPRelayNakPktNum'
_Y='hpnicfDHCPRelayAckPktNum'
_X='hpnicfDHCPRelayOfferPktNum'
_W='hpnicfDHCPRelayInformPktNum'
_V='hpnicfDHCPRelayReleasePktNum'
_U='hpnicfDHCPRelayDeclinePktNum'
_T='hpnicfDHCPRelayRequestPktNum'
_S='hpnicfDHCPRelayDiscoverPktNum'
_R='hpnicfDHCPRTxClientBroPktNum'
_Q='hpnicfDHCPRTxClientUniPktNum'
_P='hpnicfDHCPRTxClientPktNum'
_O='hpnicfDHCPRRxClientPktNum'
_N='hpnicfDHCPRTxServerPktNum'
_M='hpnicfDHCPRRxServerPktNum'
_L='hpnicfDHCPRRxBadPktNum'
_K='hpnicfDHCPRelayCycleStatus'
_J='hpnicfDHCPRSelectAllocateMode'
_I='hpnicfDHCPRIPRowStatus'
_H='read-write'
_G='hpnicfDHCPRIPAddr'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-only'
_B='HPN-ICF-DHCPR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfRhw,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfRhw')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfDHCPRelayMib=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,1))
if mibBuilder.loadTexts:hpnicfDHCPRelayMib.setRevisions(('2003-02-12 00:00',))
_HpnicfDHCPRelayMibObject_ObjectIdentity=ObjectIdentity
hpnicfDHCPRelayMibObject=_HpnicfDHCPRelayMibObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,1,1))
_HpnicfDHCPRIPTable_Object=MibTable
hpnicfDHCPRIPTable=_HpnicfDHCPRIPTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,1,1,1))
if mibBuilder.loadTexts:hpnicfDHCPRIPTable.setStatus(_A)
_HpnicfDHCPRIPEntry_Object=MibTableRow
hpnicfDHCPRIPEntry=_HpnicfDHCPRIPEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,1,1,1,1))
hpnicfDHCPRIPEntry.setIndexNames((0,_E,_F),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfDHCPRIPEntry.setStatus(_A)
_HpnicfDHCPRIPAddr_Type=IpAddress
_HpnicfDHCPRIPAddr_Object=MibTableColumn
hpnicfDHCPRIPAddr=_HpnicfDHCPRIPAddr_Object((1,3,6,1,4,1,11,2,14,11,15,8,1,1,1,1,1),_HpnicfDHCPRIPAddr_Type())
hpnicfDHCPRIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDHCPRIPAddr.setStatus(_A)
_HpnicfDHCPRIPRowStatus_Type=RowStatus
_HpnicfDHCPRIPRowStatus_Object=MibTableColumn
hpnicfDHCPRIPRowStatus=_HpnicfDHCPRIPRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,1,1,1,1,2),_HpnicfDHCPRIPRowStatus_Type())
hpnicfDHCPRIPRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:hpnicfDHCPRIPRowStatus.setStatus(_A)
_HpnicfDHCPRSeletAllocateModeTable_Object=MibTable
hpnicfDHCPRSeletAllocateModeTable=_HpnicfDHCPRSeletAllocateModeTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,1,1,2))
if mibBuilder.loadTexts:hpnicfDHCPRSeletAllocateModeTable.setStatus(_A)
_HpnicfDHCPRSeletAllocateModeEntry_Object=MibTableRow
hpnicfDHCPRSeletAllocateModeEntry=_HpnicfDHCPRSeletAllocateModeEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,1,1,2,1))
hpnicfDHCPRSeletAllocateModeEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hpnicfDHCPRSeletAllocateModeEntry.setStatus(_A)
class _HpnicfDHCPRSelectAllocateMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('global',0),('interface',1),('relay',2)))
_HpnicfDHCPRSelectAllocateMode_Type.__name__=_D
_HpnicfDHCPRSelectAllocateMode_Object=MibTableColumn
hpnicfDHCPRSelectAllocateMode=_HpnicfDHCPRSelectAllocateMode_Object((1,3,6,1,4,1,11,2,14,11,15,8,1,1,2,1,1),_HpnicfDHCPRSelectAllocateMode_Type())
hpnicfDHCPRSelectAllocateMode.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDHCPRSelectAllocateMode.setStatus(_A)
class _HpnicfDHCPRelayCycleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('on',0),('off',1)))
_HpnicfDHCPRelayCycleStatus_Type.__name__=_D
_HpnicfDHCPRelayCycleStatus_Object=MibScalar
hpnicfDHCPRelayCycleStatus=_HpnicfDHCPRelayCycleStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,1,1,3),_HpnicfDHCPRelayCycleStatus_Type())
hpnicfDHCPRelayCycleStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDHCPRelayCycleStatus.setStatus(_A)
_HpnicfDHCPRRxBadPktNum_Type=Integer32
_HpnicfDHCPRRxBadPktNum_Object=MibScalar
hpnicfDHCPRRxBadPktNum=_HpnicfDHCPRRxBadPktNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,1,1,4),_HpnicfDHCPRRxBadPktNum_Type())
hpnicfDHCPRRxBadPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDHCPRRxBadPktNum.setStatus(_A)
_HpnicfDHCPRRxServerPktNum_Type=Integer32
_HpnicfDHCPRRxServerPktNum_Object=MibScalar
hpnicfDHCPRRxServerPktNum=_HpnicfDHCPRRxServerPktNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,1,1,5),_HpnicfDHCPRRxServerPktNum_Type())
hpnicfDHCPRRxServerPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDHCPRRxServerPktNum.setStatus(_A)
_HpnicfDHCPRTxServerPktNum_Type=Integer32
_HpnicfDHCPRTxServerPktNum_Object=MibScalar
hpnicfDHCPRTxServerPktNum=_HpnicfDHCPRTxServerPktNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,1,1,6),_HpnicfDHCPRTxServerPktNum_Type())
hpnicfDHCPRTxServerPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDHCPRTxServerPktNum.setStatus(_A)
_HpnicfDHCPRRxClientPktNum_Type=Integer32
_HpnicfDHCPRRxClientPktNum_Object=MibScalar
hpnicfDHCPRRxClientPktNum=_HpnicfDHCPRRxClientPktNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,1,1,7),_HpnicfDHCPRRxClientPktNum_Type())
hpnicfDHCPRRxClientPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDHCPRRxClientPktNum.setStatus(_A)
_HpnicfDHCPRTxClientPktNum_Type=Integer32
_HpnicfDHCPRTxClientPktNum_Object=MibScalar
hpnicfDHCPRTxClientPktNum=_HpnicfDHCPRTxClientPktNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,1,1,8),_HpnicfDHCPRTxClientPktNum_Type())
hpnicfDHCPRTxClientPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDHCPRTxClientPktNum.setStatus(_A)
_HpnicfDHCPRTxClientUniPktNum_Type=Integer32
_HpnicfDHCPRTxClientUniPktNum_Object=MibScalar
hpnicfDHCPRTxClientUniPktNum=_HpnicfDHCPRTxClientUniPktNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,1,1,9),_HpnicfDHCPRTxClientUniPktNum_Type())
hpnicfDHCPRTxClientUniPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDHCPRTxClientUniPktNum.setStatus(_A)
_HpnicfDHCPRTxClientBroPktNum_Type=Integer32
_HpnicfDHCPRTxClientBroPktNum_Object=MibScalar
hpnicfDHCPRTxClientBroPktNum=_HpnicfDHCPRTxClientBroPktNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,1,1,10),_HpnicfDHCPRTxClientBroPktNum_Type())
hpnicfDHCPRTxClientBroPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDHCPRTxClientBroPktNum.setStatus(_A)
_HpnicfDHCPRelayDiscoverPktNum_Type=Integer32
_HpnicfDHCPRelayDiscoverPktNum_Object=MibScalar
hpnicfDHCPRelayDiscoverPktNum=_HpnicfDHCPRelayDiscoverPktNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,1,1,11),_HpnicfDHCPRelayDiscoverPktNum_Type())
hpnicfDHCPRelayDiscoverPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDHCPRelayDiscoverPktNum.setStatus(_A)
_HpnicfDHCPRelayRequestPktNum_Type=Integer32
_HpnicfDHCPRelayRequestPktNum_Object=MibScalar
hpnicfDHCPRelayRequestPktNum=_HpnicfDHCPRelayRequestPktNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,1,1,12),_HpnicfDHCPRelayRequestPktNum_Type())
hpnicfDHCPRelayRequestPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDHCPRelayRequestPktNum.setStatus(_A)
_HpnicfDHCPRelayDeclinePktNum_Type=Integer32
_HpnicfDHCPRelayDeclinePktNum_Object=MibScalar
hpnicfDHCPRelayDeclinePktNum=_HpnicfDHCPRelayDeclinePktNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,1,1,13),_HpnicfDHCPRelayDeclinePktNum_Type())
hpnicfDHCPRelayDeclinePktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDHCPRelayDeclinePktNum.setStatus(_A)
_HpnicfDHCPRelayReleasePktNum_Type=Integer32
_HpnicfDHCPRelayReleasePktNum_Object=MibScalar
hpnicfDHCPRelayReleasePktNum=_HpnicfDHCPRelayReleasePktNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,1,1,14),_HpnicfDHCPRelayReleasePktNum_Type())
hpnicfDHCPRelayReleasePktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDHCPRelayReleasePktNum.setStatus(_A)
_HpnicfDHCPRelayInformPktNum_Type=Integer32
_HpnicfDHCPRelayInformPktNum_Object=MibScalar
hpnicfDHCPRelayInformPktNum=_HpnicfDHCPRelayInformPktNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,1,1,15),_HpnicfDHCPRelayInformPktNum_Type())
hpnicfDHCPRelayInformPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDHCPRelayInformPktNum.setStatus(_A)
_HpnicfDHCPRelayOfferPktNum_Type=Integer32
_HpnicfDHCPRelayOfferPktNum_Object=MibScalar
hpnicfDHCPRelayOfferPktNum=_HpnicfDHCPRelayOfferPktNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,1,1,16),_HpnicfDHCPRelayOfferPktNum_Type())
hpnicfDHCPRelayOfferPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDHCPRelayOfferPktNum.setStatus(_A)
_HpnicfDHCPRelayAckPktNum_Type=Integer32
_HpnicfDHCPRelayAckPktNum_Object=MibScalar
hpnicfDHCPRelayAckPktNum=_HpnicfDHCPRelayAckPktNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,1,1,17),_HpnicfDHCPRelayAckPktNum_Type())
hpnicfDHCPRelayAckPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDHCPRelayAckPktNum.setStatus(_A)
_HpnicfDHCPRelayNakPktNum_Type=Integer32
_HpnicfDHCPRelayNakPktNum_Object=MibScalar
hpnicfDHCPRelayNakPktNum=_HpnicfDHCPRelayNakPktNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,1,1,18),_HpnicfDHCPRelayNakPktNum_Type())
hpnicfDHCPRelayNakPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDHCPRelayNakPktNum.setStatus(_A)
class _HpnicfDHCPRelayStatisticsReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('invalid',0),('reset',1)))
_HpnicfDHCPRelayStatisticsReset_Type.__name__=_D
_HpnicfDHCPRelayStatisticsReset_Object=MibScalar
hpnicfDHCPRelayStatisticsReset=_HpnicfDHCPRelayStatisticsReset_Object((1,3,6,1,4,1,11,2,14,11,15,8,1,1,19),_HpnicfDHCPRelayStatisticsReset_Type())
hpnicfDHCPRelayStatisticsReset.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDHCPRelayStatisticsReset.setStatus(_A)
_HpnicfDHCPRelayMIBConformance_ObjectIdentity=ObjectIdentity
hpnicfDHCPRelayMIBConformance=_HpnicfDHCPRelayMIBConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,1,2))
_HpnicfDHCPRelayMIBCompliances_ObjectIdentity=ObjectIdentity
hpnicfDHCPRelayMIBCompliances=_HpnicfDHCPRelayMIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,1,2,1))
_HpnicfDHCPRelayMIBGroups_ObjectIdentity=ObjectIdentity
hpnicfDHCPRelayMIBGroups=_HpnicfDHCPRelayMIBGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,1,2,2))
hpnicfDHCPRelayMIBGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,8,1,2,2,1))
hpnicfDHCPRelayMIBGroup.setObjects(*((_B,_G),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:hpnicfDHCPRelayMIBGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfDHCPRelayMib':hpnicfDHCPRelayMib,'hpnicfDHCPRelayMibObject':hpnicfDHCPRelayMibObject,'hpnicfDHCPRIPTable':hpnicfDHCPRIPTable,'hpnicfDHCPRIPEntry':hpnicfDHCPRIPEntry,_G:hpnicfDHCPRIPAddr,_I:hpnicfDHCPRIPRowStatus,'hpnicfDHCPRSeletAllocateModeTable':hpnicfDHCPRSeletAllocateModeTable,'hpnicfDHCPRSeletAllocateModeEntry':hpnicfDHCPRSeletAllocateModeEntry,_J:hpnicfDHCPRSelectAllocateMode,_K:hpnicfDHCPRelayCycleStatus,_L:hpnicfDHCPRRxBadPktNum,_M:hpnicfDHCPRRxServerPktNum,_N:hpnicfDHCPRTxServerPktNum,_O:hpnicfDHCPRRxClientPktNum,_P:hpnicfDHCPRTxClientPktNum,_Q:hpnicfDHCPRTxClientUniPktNum,_R:hpnicfDHCPRTxClientBroPktNum,_S:hpnicfDHCPRelayDiscoverPktNum,_T:hpnicfDHCPRelayRequestPktNum,_U:hpnicfDHCPRelayDeclinePktNum,_V:hpnicfDHCPRelayReleasePktNum,_W:hpnicfDHCPRelayInformPktNum,_X:hpnicfDHCPRelayOfferPktNum,_Y:hpnicfDHCPRelayAckPktNum,_Z:hpnicfDHCPRelayNakPktNum,_a:hpnicfDHCPRelayStatisticsReset,'hpnicfDHCPRelayMIBConformance':hpnicfDHCPRelayMIBConformance,'hpnicfDHCPRelayMIBCompliances':hpnicfDHCPRelayMIBCompliances,'hpnicfDHCPRelayMIBGroups':hpnicfDHCPRelayMIBGroups,'hpnicfDHCPRelayMIBGroup':hpnicfDHCPRelayMIBGroup})