_W='qtechDhcpRelayCountersObjects'
_V='qtechDHCPRelayNakPktNum'
_U='qtechDHCPRelayAckPktNum'
_T='qtechDHCPRelayOfferPktNum'
_S='qtechDHCPRelayInformPktNum'
_R='qtechDHCPRelayReleasePktNum'
_Q='qtechDHCPRelayDeclinePktNum'
_P='qtechDHCPRelayRequestPktNum'
_O='qtechDHCPRelayDiscoverPktNum'
_N='qtechDHCPRTxClientBroPktNum'
_M='qtechDHCPRTxClientUniPktNum'
_L='qtechDHCPRRxClientBroPktNum'
_K='qtechDHCPRRxClientUniPktNum'
_J='qtechDHCPRTxClientPktNum'
_I='qtechDHCPRRxClientPktNum'
_H='qtechDHCPRTxServerPktNum'
_G='qtechDHCPRRxServerPktNum'
_F='qtechDHCPRRxBadPktNum'
_E='qtechDHCPRelayCycleStatus'
_D='Integer32'
_C='read-only'
_B='QTECH-DHCP-RELAY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
qtechDhcpMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,104))
if mibBuilder.loadTexts:qtechDhcpMIB.setRevisions(('2011-11-28 00:00',))
_QtechDhcpMIBObjects_ObjectIdentity=ObjectIdentity
qtechDhcpMIBObjects=_QtechDhcpMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,104,1))
if mibBuilder.loadTexts:qtechDhcpMIBObjects.setStatus(_A)
_QtechDhcpRelayMIBObjects_ObjectIdentity=ObjectIdentity
qtechDhcpRelayMIBObjects=_QtechDhcpRelayMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,104,1,1))
if mibBuilder.loadTexts:qtechDhcpRelayMIBObjects.setStatus(_A)
class _QtechDHCPRelayCycleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('on',0),('off',1)))
_QtechDHCPRelayCycleStatus_Type.__name__=_D
_QtechDHCPRelayCycleStatus_Object=MibScalar
qtechDHCPRelayCycleStatus=_QtechDHCPRelayCycleStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,104,1,1,1),_QtechDHCPRelayCycleStatus_Type())
qtechDHCPRelayCycleStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:qtechDHCPRelayCycleStatus.setStatus(_A)
_QtechDhcpRelayCounters_ObjectIdentity=ObjectIdentity
qtechDhcpRelayCounters=_QtechDhcpRelayCounters_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,104,1,1,2))
if mibBuilder.loadTexts:qtechDhcpRelayCounters.setStatus(_A)
_QtechDHCPRRxBadPktNum_Type=Integer32
_QtechDHCPRRxBadPktNum_Object=MibScalar
qtechDHCPRRxBadPktNum=_QtechDHCPRRxBadPktNum_Object((1,3,6,1,4,1,27514,1,1,10,2,104,1,1,2,1),_QtechDHCPRRxBadPktNum_Type())
qtechDHCPRRxBadPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDHCPRRxBadPktNum.setStatus(_A)
_QtechDHCPRRxServerPktNum_Type=Integer32
_QtechDHCPRRxServerPktNum_Object=MibScalar
qtechDHCPRRxServerPktNum=_QtechDHCPRRxServerPktNum_Object((1,3,6,1,4,1,27514,1,1,10,2,104,1,1,2,2),_QtechDHCPRRxServerPktNum_Type())
qtechDHCPRRxServerPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDHCPRRxServerPktNum.setStatus(_A)
_QtechDHCPRTxServerPktNum_Type=Integer32
_QtechDHCPRTxServerPktNum_Object=MibScalar
qtechDHCPRTxServerPktNum=_QtechDHCPRTxServerPktNum_Object((1,3,6,1,4,1,27514,1,1,10,2,104,1,1,2,3),_QtechDHCPRTxServerPktNum_Type())
qtechDHCPRTxServerPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDHCPRTxServerPktNum.setStatus(_A)
_QtechDHCPRRxClientPktNum_Type=Integer32
_QtechDHCPRRxClientPktNum_Object=MibScalar
qtechDHCPRRxClientPktNum=_QtechDHCPRRxClientPktNum_Object((1,3,6,1,4,1,27514,1,1,10,2,104,1,1,2,4),_QtechDHCPRRxClientPktNum_Type())
qtechDHCPRRxClientPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDHCPRRxClientPktNum.setStatus(_A)
_QtechDHCPRTxClientPktNum_Type=Integer32
_QtechDHCPRTxClientPktNum_Object=MibScalar
qtechDHCPRTxClientPktNum=_QtechDHCPRTxClientPktNum_Object((1,3,6,1,4,1,27514,1,1,10,2,104,1,1,2,5),_QtechDHCPRTxClientPktNum_Type())
qtechDHCPRTxClientPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDHCPRTxClientPktNum.setStatus(_A)
_QtechDHCPRRxClientUniPktNum_Type=Integer32
_QtechDHCPRRxClientUniPktNum_Object=MibScalar
qtechDHCPRRxClientUniPktNum=_QtechDHCPRRxClientUniPktNum_Object((1,3,6,1,4,1,27514,1,1,10,2,104,1,1,2,6),_QtechDHCPRRxClientUniPktNum_Type())
qtechDHCPRRxClientUniPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDHCPRRxClientUniPktNum.setStatus(_A)
_QtechDHCPRRxClientBroPktNum_Type=Integer32
_QtechDHCPRRxClientBroPktNum_Object=MibScalar
qtechDHCPRRxClientBroPktNum=_QtechDHCPRRxClientBroPktNum_Object((1,3,6,1,4,1,27514,1,1,10,2,104,1,1,2,7),_QtechDHCPRRxClientBroPktNum_Type())
qtechDHCPRRxClientBroPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDHCPRRxClientBroPktNum.setStatus(_A)
_QtechDHCPRTxClientUniPktNum_Type=Integer32
_QtechDHCPRTxClientUniPktNum_Object=MibScalar
qtechDHCPRTxClientUniPktNum=_QtechDHCPRTxClientUniPktNum_Object((1,3,6,1,4,1,27514,1,1,10,2,104,1,1,2,8),_QtechDHCPRTxClientUniPktNum_Type())
qtechDHCPRTxClientUniPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDHCPRTxClientUniPktNum.setStatus(_A)
_QtechDHCPRTxClientBroPktNum_Type=Integer32
_QtechDHCPRTxClientBroPktNum_Object=MibScalar
qtechDHCPRTxClientBroPktNum=_QtechDHCPRTxClientBroPktNum_Object((1,3,6,1,4,1,27514,1,1,10,2,104,1,1,2,9),_QtechDHCPRTxClientBroPktNum_Type())
qtechDHCPRTxClientBroPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDHCPRTxClientBroPktNum.setStatus(_A)
_QtechDHCPRelayDiscoverPktNum_Type=Integer32
_QtechDHCPRelayDiscoverPktNum_Object=MibScalar
qtechDHCPRelayDiscoverPktNum=_QtechDHCPRelayDiscoverPktNum_Object((1,3,6,1,4,1,27514,1,1,10,2,104,1,1,2,10),_QtechDHCPRelayDiscoverPktNum_Type())
qtechDHCPRelayDiscoverPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDHCPRelayDiscoverPktNum.setStatus(_A)
_QtechDHCPRelayRequestPktNum_Type=Integer32
_QtechDHCPRelayRequestPktNum_Object=MibScalar
qtechDHCPRelayRequestPktNum=_QtechDHCPRelayRequestPktNum_Object((1,3,6,1,4,1,27514,1,1,10,2,104,1,1,2,11),_QtechDHCPRelayRequestPktNum_Type())
qtechDHCPRelayRequestPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDHCPRelayRequestPktNum.setStatus(_A)
_QtechDHCPRelayDeclinePktNum_Type=Integer32
_QtechDHCPRelayDeclinePktNum_Object=MibScalar
qtechDHCPRelayDeclinePktNum=_QtechDHCPRelayDeclinePktNum_Object((1,3,6,1,4,1,27514,1,1,10,2,104,1,1,2,12),_QtechDHCPRelayDeclinePktNum_Type())
qtechDHCPRelayDeclinePktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDHCPRelayDeclinePktNum.setStatus(_A)
_QtechDHCPRelayReleasePktNum_Type=Integer32
_QtechDHCPRelayReleasePktNum_Object=MibScalar
qtechDHCPRelayReleasePktNum=_QtechDHCPRelayReleasePktNum_Object((1,3,6,1,4,1,27514,1,1,10,2,104,1,1,2,13),_QtechDHCPRelayReleasePktNum_Type())
qtechDHCPRelayReleasePktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDHCPRelayReleasePktNum.setStatus(_A)
_QtechDHCPRelayInformPktNum_Type=Integer32
_QtechDHCPRelayInformPktNum_Object=MibScalar
qtechDHCPRelayInformPktNum=_QtechDHCPRelayInformPktNum_Object((1,3,6,1,4,1,27514,1,1,10,2,104,1,1,2,14),_QtechDHCPRelayInformPktNum_Type())
qtechDHCPRelayInformPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDHCPRelayInformPktNum.setStatus(_A)
_QtechDHCPRelayOfferPktNum_Type=Integer32
_QtechDHCPRelayOfferPktNum_Object=MibScalar
qtechDHCPRelayOfferPktNum=_QtechDHCPRelayOfferPktNum_Object((1,3,6,1,4,1,27514,1,1,10,2,104,1,1,2,15),_QtechDHCPRelayOfferPktNum_Type())
qtechDHCPRelayOfferPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDHCPRelayOfferPktNum.setStatus(_A)
_QtechDHCPRelayAckPktNum_Type=Integer32
_QtechDHCPRelayAckPktNum_Object=MibScalar
qtechDHCPRelayAckPktNum=_QtechDHCPRelayAckPktNum_Object((1,3,6,1,4,1,27514,1,1,10,2,104,1,1,2,16),_QtechDHCPRelayAckPktNum_Type())
qtechDHCPRelayAckPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDHCPRelayAckPktNum.setStatus(_A)
_QtechDHCPRelayNakPktNum_Type=Integer32
_QtechDHCPRelayNakPktNum_Object=MibScalar
qtechDHCPRelayNakPktNum=_QtechDHCPRelayNakPktNum_Object((1,3,6,1,4,1,27514,1,1,10,2,104,1,1,2,17),_QtechDHCPRelayNakPktNum_Type())
qtechDHCPRelayNakPktNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDHCPRelayNakPktNum.setStatus(_A)
_QtechDhcpMIBConformance_ObjectIdentity=ObjectIdentity
qtechDhcpMIBConformance=_QtechDhcpMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,104,2))
if mibBuilder.loadTexts:qtechDhcpMIBConformance.setStatus(_A)
_QtechDhcpMIBCompliances_ObjectIdentity=ObjectIdentity
qtechDhcpMIBCompliances=_QtechDhcpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,104,2,1))
_QtechDhcpMIBGroups_ObjectIdentity=ObjectIdentity
qtechDhcpMIBGroups=_QtechDhcpMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,104,2,2))
qtechDhcpRelayCountersObjects=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,104,2,2,1))
qtechDhcpRelayCountersObjects.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:qtechDhcpRelayCountersObjects.setStatus(_A)
qtechDhcpRelayCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,104,2,1,1))
qtechDhcpRelayCompliance.setObjects((_B,_W))
if mibBuilder.loadTexts:qtechDhcpRelayCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechDhcpMIB':qtechDhcpMIB,'qtechDhcpMIBObjects':qtechDhcpMIBObjects,'qtechDhcpRelayMIBObjects':qtechDhcpRelayMIBObjects,_E:qtechDHCPRelayCycleStatus,'qtechDhcpRelayCounters':qtechDhcpRelayCounters,_F:qtechDHCPRRxBadPktNum,_G:qtechDHCPRRxServerPktNum,_H:qtechDHCPRTxServerPktNum,_I:qtechDHCPRRxClientPktNum,_J:qtechDHCPRTxClientPktNum,_K:qtechDHCPRRxClientUniPktNum,_L:qtechDHCPRRxClientBroPktNum,_M:qtechDHCPRTxClientUniPktNum,_N:qtechDHCPRTxClientBroPktNum,_O:qtechDHCPRelayDiscoverPktNum,_P:qtechDHCPRelayRequestPktNum,_Q:qtechDHCPRelayDeclinePktNum,_R:qtechDHCPRelayReleasePktNum,_S:qtechDHCPRelayInformPktNum,_T:qtechDHCPRelayOfferPktNum,_U:qtechDHCPRelayAckPktNum,_V:qtechDHCPRelayNakPktNum,'qtechDhcpMIBConformance':qtechDhcpMIBConformance,'qtechDhcpMIBCompliances':qtechDhcpMIBCompliances,'qtechDhcpRelayCompliance':qtechDhcpRelayCompliance,'qtechDhcpMIBGroups':qtechDhcpMIBGroups,_W:qtechDhcpRelayCountersObjects})