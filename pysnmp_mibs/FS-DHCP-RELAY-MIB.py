_W='fsDhcpRelayCountersObjects'
_V='fsDHCPRelayNakPktNum'
_U='fsDHCPRelayAckPktNum'
_T='fsDHCPRelayOfferPktNum'
_S='fsDHCPRelayInformPktNum'
_R='fsDHCPRelayReleasePktNum'
_Q='fsDHCPRelayDeclinePktNum'
_P='fsDHCPRelayRequestPktNum'
_O='fsDHCPRelayDiscoverPktNum'
_N='fsDHCPRTxClientBroPktNum'
_M='fsDHCPRTxClientUniPktNum'
_L='fsDHCPRRxClientBroPktNum'
_K='fsDHCPRRxClientUniPktNum'
_J='fsDHCPRTxClientPktNum'
_I='fsDHCPRRxClientPktNum'
_H='fsDHCPRTxServerPktNum'
_G='fsDHCPRRxServerPktNum'
_F='fsDHCPRRxBadPktNum'
_E='fsDHCPRelayCycleStatus'
_D='Integer32'
_C='read-only'
_B='FS-DHCP-RELAY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
fsDhcpMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,104))
if mibBuilder.loadTexts:fsDhcpMIB.setRevisions(('2011-11-28 00:00',))
_FsDhcpMIBObjects_ObjectIdentity=ObjectIdentity
fsDhcpMIBObjects=_FsDhcpMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,104,1))
if mibBuilder.loadTexts:fsDhcpMIBObjects.setStatus(_A)
_FsDhcpRelayMIBObjects_ObjectIdentity=ObjectIdentity
fsDhcpRelayMIBObjects=_FsDhcpRelayMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,104,1,1))
if mibBuilder.loadTexts:fsDhcpRelayMIBObjects.setStatus(_A)
class _FsDHCPRelayCycleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('on',0),('off',1)))
_FsDHCPRelayCycleStatus_Type.__name__=_D
_FsDHCPRelayCycleStatus_Object=MibScalar
fsDHCPRelayCycleStatus=_FsDHCPRelayCycleStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,104,1,1,1),_FsDHCPRelayCycleStatus_Type())
fsDHCPRelayCycleStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:fsDHCPRelayCycleStatus.setStatus(_A)
_FsDhcpRelayCounters_ObjectIdentity=ObjectIdentity
fsDhcpRelayCounters=_FsDhcpRelayCounters_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,104,1,1,2))
if mibBuilder.loadTexts:fsDhcpRelayCounters.setStatus(_A)
_FsDHCPRRxBadPktNum_Type=Integer32
_FsDHCPRRxBadPktNum_Object=MibScalar
fsDHCPRRxBadPktNum=_FsDHCPRRxBadPktNum_Object((1,3,6,1,4,1,52642,1,1,10,2,104,1,1,2,1),_FsDHCPRRxBadPktNum_Type())
fsDHCPRRxBadPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDHCPRRxBadPktNum.setStatus(_A)
_FsDHCPRRxServerPktNum_Type=Integer32
_FsDHCPRRxServerPktNum_Object=MibScalar
fsDHCPRRxServerPktNum=_FsDHCPRRxServerPktNum_Object((1,3,6,1,4,1,52642,1,1,10,2,104,1,1,2,2),_FsDHCPRRxServerPktNum_Type())
fsDHCPRRxServerPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDHCPRRxServerPktNum.setStatus(_A)
_FsDHCPRTxServerPktNum_Type=Integer32
_FsDHCPRTxServerPktNum_Object=MibScalar
fsDHCPRTxServerPktNum=_FsDHCPRTxServerPktNum_Object((1,3,6,1,4,1,52642,1,1,10,2,104,1,1,2,3),_FsDHCPRTxServerPktNum_Type())
fsDHCPRTxServerPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDHCPRTxServerPktNum.setStatus(_A)
_FsDHCPRRxClientPktNum_Type=Integer32
_FsDHCPRRxClientPktNum_Object=MibScalar
fsDHCPRRxClientPktNum=_FsDHCPRRxClientPktNum_Object((1,3,6,1,4,1,52642,1,1,10,2,104,1,1,2,4),_FsDHCPRRxClientPktNum_Type())
fsDHCPRRxClientPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDHCPRRxClientPktNum.setStatus(_A)
_FsDHCPRTxClientPktNum_Type=Integer32
_FsDHCPRTxClientPktNum_Object=MibScalar
fsDHCPRTxClientPktNum=_FsDHCPRTxClientPktNum_Object((1,3,6,1,4,1,52642,1,1,10,2,104,1,1,2,5),_FsDHCPRTxClientPktNum_Type())
fsDHCPRTxClientPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDHCPRTxClientPktNum.setStatus(_A)
_FsDHCPRRxClientUniPktNum_Type=Integer32
_FsDHCPRRxClientUniPktNum_Object=MibScalar
fsDHCPRRxClientUniPktNum=_FsDHCPRRxClientUniPktNum_Object((1,3,6,1,4,1,52642,1,1,10,2,104,1,1,2,6),_FsDHCPRRxClientUniPktNum_Type())
fsDHCPRRxClientUniPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDHCPRRxClientUniPktNum.setStatus(_A)
_FsDHCPRRxClientBroPktNum_Type=Integer32
_FsDHCPRRxClientBroPktNum_Object=MibScalar
fsDHCPRRxClientBroPktNum=_FsDHCPRRxClientBroPktNum_Object((1,3,6,1,4,1,52642,1,1,10,2,104,1,1,2,7),_FsDHCPRRxClientBroPktNum_Type())
fsDHCPRRxClientBroPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDHCPRRxClientBroPktNum.setStatus(_A)
_FsDHCPRTxClientUniPktNum_Type=Integer32
_FsDHCPRTxClientUniPktNum_Object=MibScalar
fsDHCPRTxClientUniPktNum=_FsDHCPRTxClientUniPktNum_Object((1,3,6,1,4,1,52642,1,1,10,2,104,1,1,2,8),_FsDHCPRTxClientUniPktNum_Type())
fsDHCPRTxClientUniPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDHCPRTxClientUniPktNum.setStatus(_A)
_FsDHCPRTxClientBroPktNum_Type=Integer32
_FsDHCPRTxClientBroPktNum_Object=MibScalar
fsDHCPRTxClientBroPktNum=_FsDHCPRTxClientBroPktNum_Object((1,3,6,1,4,1,52642,1,1,10,2,104,1,1,2,9),_FsDHCPRTxClientBroPktNum_Type())
fsDHCPRTxClientBroPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDHCPRTxClientBroPktNum.setStatus(_A)
_FsDHCPRelayDiscoverPktNum_Type=Integer32
_FsDHCPRelayDiscoverPktNum_Object=MibScalar
fsDHCPRelayDiscoverPktNum=_FsDHCPRelayDiscoverPktNum_Object((1,3,6,1,4,1,52642,1,1,10,2,104,1,1,2,10),_FsDHCPRelayDiscoverPktNum_Type())
fsDHCPRelayDiscoverPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDHCPRelayDiscoverPktNum.setStatus(_A)
_FsDHCPRelayRequestPktNum_Type=Integer32
_FsDHCPRelayRequestPktNum_Object=MibScalar
fsDHCPRelayRequestPktNum=_FsDHCPRelayRequestPktNum_Object((1,3,6,1,4,1,52642,1,1,10,2,104,1,1,2,11),_FsDHCPRelayRequestPktNum_Type())
fsDHCPRelayRequestPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDHCPRelayRequestPktNum.setStatus(_A)
_FsDHCPRelayDeclinePktNum_Type=Integer32
_FsDHCPRelayDeclinePktNum_Object=MibScalar
fsDHCPRelayDeclinePktNum=_FsDHCPRelayDeclinePktNum_Object((1,3,6,1,4,1,52642,1,1,10,2,104,1,1,2,12),_FsDHCPRelayDeclinePktNum_Type())
fsDHCPRelayDeclinePktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDHCPRelayDeclinePktNum.setStatus(_A)
_FsDHCPRelayReleasePktNum_Type=Integer32
_FsDHCPRelayReleasePktNum_Object=MibScalar
fsDHCPRelayReleasePktNum=_FsDHCPRelayReleasePktNum_Object((1,3,6,1,4,1,52642,1,1,10,2,104,1,1,2,13),_FsDHCPRelayReleasePktNum_Type())
fsDHCPRelayReleasePktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDHCPRelayReleasePktNum.setStatus(_A)
_FsDHCPRelayInformPktNum_Type=Integer32
_FsDHCPRelayInformPktNum_Object=MibScalar
fsDHCPRelayInformPktNum=_FsDHCPRelayInformPktNum_Object((1,3,6,1,4,1,52642,1,1,10,2,104,1,1,2,14),_FsDHCPRelayInformPktNum_Type())
fsDHCPRelayInformPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDHCPRelayInformPktNum.setStatus(_A)
_FsDHCPRelayOfferPktNum_Type=Integer32
_FsDHCPRelayOfferPktNum_Object=MibScalar
fsDHCPRelayOfferPktNum=_FsDHCPRelayOfferPktNum_Object((1,3,6,1,4,1,52642,1,1,10,2,104,1,1,2,15),_FsDHCPRelayOfferPktNum_Type())
fsDHCPRelayOfferPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDHCPRelayOfferPktNum.setStatus(_A)
_FsDHCPRelayAckPktNum_Type=Integer32
_FsDHCPRelayAckPktNum_Object=MibScalar
fsDHCPRelayAckPktNum=_FsDHCPRelayAckPktNum_Object((1,3,6,1,4,1,52642,1,1,10,2,104,1,1,2,16),_FsDHCPRelayAckPktNum_Type())
fsDHCPRelayAckPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDHCPRelayAckPktNum.setStatus(_A)
_FsDHCPRelayNakPktNum_Type=Integer32
_FsDHCPRelayNakPktNum_Object=MibScalar
fsDHCPRelayNakPktNum=_FsDHCPRelayNakPktNum_Object((1,3,6,1,4,1,52642,1,1,10,2,104,1,1,2,17),_FsDHCPRelayNakPktNum_Type())
fsDHCPRelayNakPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDHCPRelayNakPktNum.setStatus(_A)
_FsDhcpMIBConformance_ObjectIdentity=ObjectIdentity
fsDhcpMIBConformance=_FsDhcpMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,104,2))
if mibBuilder.loadTexts:fsDhcpMIBConformance.setStatus(_A)
_FsDhcpMIBCompliances_ObjectIdentity=ObjectIdentity
fsDhcpMIBCompliances=_FsDhcpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,104,2,1))
_FsDhcpMIBGroups_ObjectIdentity=ObjectIdentity
fsDhcpMIBGroups=_FsDhcpMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,104,2,2))
fsDhcpRelayCountersObjects=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,104,2,2,1))
fsDhcpRelayCountersObjects.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:fsDhcpRelayCountersObjects.setStatus(_A)
fsDhcpRelayCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,104,2,1,1))
fsDhcpRelayCompliance.setObjects((_B,_W))
if mibBuilder.loadTexts:fsDhcpRelayCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsDhcpMIB':fsDhcpMIB,'fsDhcpMIBObjects':fsDhcpMIBObjects,'fsDhcpRelayMIBObjects':fsDhcpRelayMIBObjects,_E:fsDHCPRelayCycleStatus,'fsDhcpRelayCounters':fsDhcpRelayCounters,_F:fsDHCPRRxBadPktNum,_G:fsDHCPRRxServerPktNum,_H:fsDHCPRTxServerPktNum,_I:fsDHCPRRxClientPktNum,_J:fsDHCPRTxClientPktNum,_K:fsDHCPRRxClientUniPktNum,_L:fsDHCPRRxClientBroPktNum,_M:fsDHCPRTxClientUniPktNum,_N:fsDHCPRTxClientBroPktNum,_O:fsDHCPRelayDiscoverPktNum,_P:fsDHCPRelayRequestPktNum,_Q:fsDHCPRelayDeclinePktNum,_R:fsDHCPRelayReleasePktNum,_S:fsDHCPRelayInformPktNum,_T:fsDHCPRelayOfferPktNum,_U:fsDHCPRelayAckPktNum,_V:fsDHCPRelayNakPktNum,'fsDhcpMIBConformance':fsDhcpMIBConformance,'fsDhcpMIBCompliances':fsDhcpMIBCompliances,'fsDhcpRelayCompliance':fsDhcpRelayCompliance,'fsDhcpMIBGroups':fsDhcpMIBGroups,_W:fsDhcpRelayCountersObjects})