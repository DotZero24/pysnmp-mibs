_k='ctCdpGroupV10'
_j='ctCDPMemoryErrors'
_i='ctCDPTransmitErrors'
_h='ctCDPParseErrorPackets'
_g='ctCDPInvalidVersionPackets'
_f='ctCDPOutPackets'
_e='ctCDPInPackets'
_d='ctCDPVersion'
_c='ctCDPHoldTime'
_b='ctCDPTransmitFrequency'
_a='ctCDPNeighborCapability'
_Z='ctCDPNeighborPortName'
_Y='ctCDPNeighborDescription'
_X='ctCDPPortStatus'
_W='ctCDPAuthenticationCode'
_V='ctCDPGlobalStatus'
_U='ctCDPNeighborChassisIP'
_T='ctCDPNeighborChassisMAC'
_S='ctCDPNeighborType'
_R='ctCDPNeighborPort'
_Q='ctCDPNeighborIP'
_P='ctCDPNeighborLastDelete'
_O='ctCDPNeighborLastChange'
_N='autoEnable'
_M='dnsServer'
_L='dhcpServer'
_K='ifIndex'
_J='IF-MIB'
_I='ctCDPPort'
_H='ctCDPNeighborMAC'
_G='ctCDPNeighborTimeMark'
_F='OctetString'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='CTRON-CDP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctCDP,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctCDP')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_J,'InterfaceIndex',_K)
TimeFilter,=mibBuilder.importSymbols('RMON2-MIB','TimeFilter')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TimeStamp')
ctronCdpMIB=ModuleIdentity((1,3,6,1,4,1,52,4,1,2,19,3))
class CTCDPCapability(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('igmp',1),('rip',2),('bgp',3),('ospf',4),('dvmrp',5),('ieee8021q',6),('gvrp',7),('gmrp',8),('igmpSnoop',9),(_L,10),(_M,11),('activeDirectory',12)))
_CtCDPNeighbor_ObjectIdentity=ObjectIdentity
ctCDPNeighbor=_CtCDPNeighbor_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,19,1))
_CtCDPNeighborLastChange_Type=TimeStamp
_CtCDPNeighborLastChange_Object=MibScalar
ctCDPNeighborLastChange=_CtCDPNeighborLastChange_Object((1,3,6,1,4,1,52,4,1,2,19,1,1),_CtCDPNeighborLastChange_Type())
ctCDPNeighborLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:ctCDPNeighborLastChange.setStatus(_A)
_CtCDPNeighborLastDelete_Type=TimeStamp
_CtCDPNeighborLastDelete_Object=MibScalar
ctCDPNeighborLastDelete=_CtCDPNeighborLastDelete_Object((1,3,6,1,4,1,52,4,1,2,19,1,2),_CtCDPNeighborLastDelete_Type())
ctCDPNeighborLastDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:ctCDPNeighborLastDelete.setStatus(_A)
_CtCDPNeighborTable_Object=MibTable
ctCDPNeighborTable=_CtCDPNeighborTable_Object((1,3,6,1,4,1,52,4,1,2,19,1,3))
if mibBuilder.loadTexts:ctCDPNeighborTable.setStatus(_A)
_CtCDPNeighborEntry_Object=MibTableRow
ctCDPNeighborEntry=_CtCDPNeighborEntry_Object((1,3,6,1,4,1,52,4,1,2,19,1,3,1))
ctCDPNeighborEntry.setIndexNames((0,_B,_G),(0,_J,_K),(0,_B,_H))
if mibBuilder.loadTexts:ctCDPNeighborEntry.setStatus(_A)
_CtCDPNeighborTimeMark_Type=TimeFilter
_CtCDPNeighborTimeMark_Object=MibTableColumn
ctCDPNeighborTimeMark=_CtCDPNeighborTimeMark_Object((1,3,6,1,4,1,52,4,1,2,19,1,3,1,1),_CtCDPNeighborTimeMark_Type())
ctCDPNeighborTimeMark.setMaxAccess(_C)
if mibBuilder.loadTexts:ctCDPNeighborTimeMark.setStatus(_A)
_CtCDPNeighborMAC_Type=MacAddress
_CtCDPNeighborMAC_Object=MibTableColumn
ctCDPNeighborMAC=_CtCDPNeighborMAC_Object((1,3,6,1,4,1,52,4,1,2,19,1,3,1,2),_CtCDPNeighborMAC_Type())
ctCDPNeighborMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:ctCDPNeighborMAC.setStatus(_A)
_CtCDPNeighborIP_Type=IpAddress
_CtCDPNeighborIP_Object=MibTableColumn
ctCDPNeighborIP=_CtCDPNeighborIP_Object((1,3,6,1,4,1,52,4,1,2,19,1,3,1,3),_CtCDPNeighborIP_Type())
ctCDPNeighborIP.setMaxAccess(_C)
if mibBuilder.loadTexts:ctCDPNeighborIP.setStatus(_A)
_CtCDPNeighborPort_Type=InterfaceIndex
_CtCDPNeighborPort_Object=MibTableColumn
ctCDPNeighborPort=_CtCDPNeighborPort_Object((1,3,6,1,4,1,52,4,1,2,19,1,3,1,4),_CtCDPNeighborPort_Type())
ctCDPNeighborPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ctCDPNeighborPort.setStatus(_A)
class _CtCDPNeighborType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('secureFastSwitch',1),('dot1qSwitch',2),('router',3),('dot1dBridge',4),('vlanManager',5),(_M,6),(_L,7),('dnsDhcpServer',8)))
_CtCDPNeighborType_Type.__name__=_D
_CtCDPNeighborType_Object=MibTableColumn
ctCDPNeighborType=_CtCDPNeighborType_Object((1,3,6,1,4,1,52,4,1,2,19,1,3,1,5),_CtCDPNeighborType_Type())
ctCDPNeighborType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctCDPNeighborType.setStatus(_A)
_CtCDPNeighborChassisMAC_Type=MacAddress
_CtCDPNeighborChassisMAC_Object=MibTableColumn
ctCDPNeighborChassisMAC=_CtCDPNeighborChassisMAC_Object((1,3,6,1,4,1,52,4,1,2,19,1,3,1,6),_CtCDPNeighborChassisMAC_Type())
ctCDPNeighborChassisMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:ctCDPNeighborChassisMAC.setStatus(_A)
_CtCDPNeighborChassisIP_Type=IpAddress
_CtCDPNeighborChassisIP_Object=MibTableColumn
ctCDPNeighborChassisIP=_CtCDPNeighborChassisIP_Object((1,3,6,1,4,1,52,4,1,2,19,1,3,1,7),_CtCDPNeighborChassisIP_Type())
ctCDPNeighborChassisIP.setMaxAccess(_C)
if mibBuilder.loadTexts:ctCDPNeighborChassisIP.setStatus(_A)
_CtCDPNeighborDescription_Type=DisplayString
_CtCDPNeighborDescription_Object=MibTableColumn
ctCDPNeighborDescription=_CtCDPNeighborDescription_Object((1,3,6,1,4,1,52,4,1,2,19,1,3,1,8),_CtCDPNeighborDescription_Type())
ctCDPNeighborDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ctCDPNeighborDescription.setStatus(_A)
_CtCDPNeighborPortName_Type=DisplayString
_CtCDPNeighborPortName_Object=MibTableColumn
ctCDPNeighborPortName=_CtCDPNeighborPortName_Object((1,3,6,1,4,1,52,4,1,2,19,1,3,1,9),_CtCDPNeighborPortName_Type())
ctCDPNeighborPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctCDPNeighborPortName.setStatus(_A)
_CtCDPNeighborCapability_Type=CTCDPCapability
_CtCDPNeighborCapability_Object=MibTableColumn
ctCDPNeighborCapability=_CtCDPNeighborCapability_Object((1,3,6,1,4,1,52,4,1,2,19,1,3,1,10),_CtCDPNeighborCapability_Type())
ctCDPNeighborCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:ctCDPNeighborCapability.setStatus(_A)
_CtCDPStatus_ObjectIdentity=ObjectIdentity
ctCDPStatus=_CtCDPStatus_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,19,2))
class _CtCDPGlobalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enable',1),('disable',2),(_N,3)))
_CtCDPGlobalStatus_Type.__name__=_D
_CtCDPGlobalStatus_Object=MibScalar
ctCDPGlobalStatus=_CtCDPGlobalStatus_Object((1,3,6,1,4,1,52,4,1,2,19,2,1),_CtCDPGlobalStatus_Type())
ctCDPGlobalStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ctCDPGlobalStatus.setStatus(_A)
class _CtCDPAuthenticationCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CtCDPAuthenticationCode_Type.__name__=_F
_CtCDPAuthenticationCode_Object=MibScalar
ctCDPAuthenticationCode=_CtCDPAuthenticationCode_Object((1,3,6,1,4,1,52,4,1,2,19,2,2),_CtCDPAuthenticationCode_Type())
ctCDPAuthenticationCode.setMaxAccess(_E)
if mibBuilder.loadTexts:ctCDPAuthenticationCode.setStatus(_A)
_CtCDPPortTable_Object=MibTable
ctCDPPortTable=_CtCDPPortTable_Object((1,3,6,1,4,1,52,4,1,2,19,2,3))
if mibBuilder.loadTexts:ctCDPPortTable.setStatus(_A)
_CtCDPPortTableEntry_Object=MibTableRow
ctCDPPortTableEntry=_CtCDPPortTableEntry_Object((1,3,6,1,4,1,52,4,1,2,19,2,3,1))
ctCDPPortTableEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:ctCDPPortTableEntry.setStatus(_A)
_CtCDPPort_Type=InterfaceIndex
_CtCDPPort_Object=MibTableColumn
ctCDPPort=_CtCDPPort_Object((1,3,6,1,4,1,52,4,1,2,19,2,3,1,1),_CtCDPPort_Type())
ctCDPPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ctCDPPort.setStatus(_A)
class _CtCDPPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),('disabled',2),(_N,3)))
_CtCDPPortStatus_Type.__name__=_D
_CtCDPPortStatus_Object=MibTableColumn
ctCDPPortStatus=_CtCDPPortStatus_Object((1,3,6,1,4,1,52,4,1,2,19,2,3,1,2),_CtCDPPortStatus_Type())
ctCDPPortStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ctCDPPortStatus.setStatus(_A)
class _CtCDPTransmitFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,900))
_CtCDPTransmitFrequency_Type.__name__=_D
_CtCDPTransmitFrequency_Object=MibScalar
ctCDPTransmitFrequency=_CtCDPTransmitFrequency_Object((1,3,6,1,4,1,52,4,1,2,19,2,4),_CtCDPTransmitFrequency_Type())
ctCDPTransmitFrequency.setMaxAccess(_E)
if mibBuilder.loadTexts:ctCDPTransmitFrequency.setStatus(_A)
class _CtCDPHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,600))
_CtCDPHoldTime_Type.__name__=_D
_CtCDPHoldTime_Object=MibScalar
ctCDPHoldTime=_CtCDPHoldTime_Object((1,3,6,1,4,1,52,4,1,2,19,2,5),_CtCDPHoldTime_Type())
ctCDPHoldTime.setMaxAccess(_E)
if mibBuilder.loadTexts:ctCDPHoldTime.setStatus(_A)
class _CtCDPVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_CtCDPVersion_Type.__name__=_F
_CtCDPVersion_Object=MibScalar
ctCDPVersion=_CtCDPVersion_Object((1,3,6,1,4,1,52,4,1,2,19,2,6),_CtCDPVersion_Type())
ctCDPVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ctCDPVersion.setStatus(_A)
_CtCDPConformance_ObjectIdentity=ObjectIdentity
ctCDPConformance=_CtCDPConformance_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,19,3,11))
_CtCDPCompliances_ObjectIdentity=ObjectIdentity
ctCDPCompliances=_CtCDPCompliances_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,19,3,11,1))
_CtCDPGroups_ObjectIdentity=ObjectIdentity
ctCDPGroups=_CtCDPGroups_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,19,3,11,2))
_CtCDPStats_ObjectIdentity=ObjectIdentity
ctCDPStats=_CtCDPStats_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,19,4))
_CtCDPInPackets_Type=Counter32
_CtCDPInPackets_Object=MibScalar
ctCDPInPackets=_CtCDPInPackets_Object((1,3,6,1,4,1,52,4,1,2,19,4,1),_CtCDPInPackets_Type())
ctCDPInPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ctCDPInPackets.setStatus(_A)
_CtCDPOutPackets_Type=Counter32
_CtCDPOutPackets_Object=MibScalar
ctCDPOutPackets=_CtCDPOutPackets_Object((1,3,6,1,4,1,52,4,1,2,19,4,2),_CtCDPOutPackets_Type())
ctCDPOutPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ctCDPOutPackets.setStatus(_A)
_CtCDPInvalidVersionPackets_Type=Counter32
_CtCDPInvalidVersionPackets_Object=MibScalar
ctCDPInvalidVersionPackets=_CtCDPInvalidVersionPackets_Object((1,3,6,1,4,1,52,4,1,2,19,4,3),_CtCDPInvalidVersionPackets_Type())
ctCDPInvalidVersionPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ctCDPInvalidVersionPackets.setStatus(_A)
_CtCDPParseErrorPackets_Type=Counter32
_CtCDPParseErrorPackets_Object=MibScalar
ctCDPParseErrorPackets=_CtCDPParseErrorPackets_Object((1,3,6,1,4,1,52,4,1,2,19,4,4),_CtCDPParseErrorPackets_Type())
ctCDPParseErrorPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ctCDPParseErrorPackets.setStatus(_A)
_CtCDPTransmitErrors_Type=Counter32
_CtCDPTransmitErrors_Object=MibScalar
ctCDPTransmitErrors=_CtCDPTransmitErrors_Object((1,3,6,1,4,1,52,4,1,2,19,4,5),_CtCDPTransmitErrors_Type())
ctCDPTransmitErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ctCDPTransmitErrors.setStatus(_A)
_CtCDPMemoryErrors_Type=Counter32
_CtCDPMemoryErrors_Object=MibScalar
ctCDPMemoryErrors=_CtCDPMemoryErrors_Object((1,3,6,1,4,1,52,4,1,2,19,4,6),_CtCDPMemoryErrors_Type())
ctCDPMemoryErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ctCDPMemoryErrors.setStatus(_A)
ctCdpGroupV10=ObjectGroup((1,3,6,1,4,1,52,4,1,2,19,3,11,2,1))
ctCdpGroupV10.setObjects(*((_B,_O),(_B,_P),(_B,_G),(_B,_H),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_I),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:ctCdpGroupV10.setStatus(_A)
ctCDPComplianceV10=ModuleCompliance((1,3,6,1,4,1,52,4,1,2,19,3,11,1,1))
ctCDPComplianceV10.setObjects((_B,_k))
if mibBuilder.loadTexts:ctCDPComplianceV10.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CTCDPCapability':CTCDPCapability,'ctCDPNeighbor':ctCDPNeighbor,_O:ctCDPNeighborLastChange,_P:ctCDPNeighborLastDelete,'ctCDPNeighborTable':ctCDPNeighborTable,'ctCDPNeighborEntry':ctCDPNeighborEntry,_G:ctCDPNeighborTimeMark,_H:ctCDPNeighborMAC,_Q:ctCDPNeighborIP,_R:ctCDPNeighborPort,_S:ctCDPNeighborType,_T:ctCDPNeighborChassisMAC,_U:ctCDPNeighborChassisIP,_Y:ctCDPNeighborDescription,_Z:ctCDPNeighborPortName,_a:ctCDPNeighborCapability,'ctCDPStatus':ctCDPStatus,_V:ctCDPGlobalStatus,_W:ctCDPAuthenticationCode,'ctCDPPortTable':ctCDPPortTable,'ctCDPPortTableEntry':ctCDPPortTableEntry,_I:ctCDPPort,_X:ctCDPPortStatus,_b:ctCDPTransmitFrequency,_c:ctCDPHoldTime,_d:ctCDPVersion,'ctronCdpMIB':ctronCdpMIB,'ctCDPConformance':ctCDPConformance,'ctCDPCompliances':ctCDPCompliances,'ctCDPComplianceV10':ctCDPComplianceV10,'ctCDPGroups':ctCDPGroups,_k:ctCdpGroupV10,'ctCDPStats':ctCDPStats,_e:ctCDPInPackets,_f:ctCDPOutPackets,_g:ctCDPInvalidVersionPackets,_h:ctCDPParseErrorPackets,_i:ctCDPTransmitErrors,_j:ctCDPMemoryErrors})