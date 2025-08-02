_Q='h3cMplsExtVpnName'
_P='h3cMplsExtVpnStatsVrfIndex'
_O='unknown'
_N='h3cMplsExtBfdLocalDiscr'
_M='h3cMplsExtLdpIndex'
_L='h3cMplsExtIndex'
_K='read-write'
_J='DisplayString'
_I='TruthValue'
_H='read-create'
_G='not-accessible'
_F='Integer32'
_E='OctetString'
_D='H3C-MPLSEXT-MIB'
_C='Unsigned32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','RowStatus','TextualConvention',_I)
h3cMplsExt=ModuleIdentity((1,3,6,1,4,1,2011,10,2,142))
if mibBuilder.loadTexts:h3cMplsExt.setRevisions(('2017-02-17 18:00','2015-06-16 18:00','2014-12-17 12:00','2013-06-13 18:00'))
_H3cMplsExtObjects_ObjectIdentity=ObjectIdentity
h3cMplsExtObjects=_H3cMplsExtObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,142,1))
_H3cMplsExtScalarGroup_ObjectIdentity=ObjectIdentity
h3cMplsExtScalarGroup=_H3cMplsExtScalarGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,142,1,1))
class _H3cMplsExtLsrID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cMplsExtLsrID_Type.__name__=_E
_H3cMplsExtLsrID_Object=MibScalar
h3cMplsExtLsrID=_H3cMplsExtLsrID_Object((1,3,6,1,4,1,2011,10,2,142,1,1,1),_H3cMplsExtLsrID_Type())
h3cMplsExtLsrID.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cMplsExtLsrID.setStatus(_A)
_H3cMplsExtLdpStatus_Type=TruthValue
_H3cMplsExtLdpStatus_Object=MibScalar
h3cMplsExtLdpStatus=_H3cMplsExtLdpStatus_Object((1,3,6,1,4,1,2011,10,2,142,1,1,2),_H3cMplsExtLdpStatus_Type())
h3cMplsExtLdpStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cMplsExtLdpStatus.setStatus(_A)
_H3cMplsExtTable_Object=MibTable
h3cMplsExtTable=_H3cMplsExtTable_Object((1,3,6,1,4,1,2011,10,2,142,1,2))
if mibBuilder.loadTexts:h3cMplsExtTable.setStatus(_A)
_H3cMplsExtEntry_Object=MibTableRow
h3cMplsExtEntry=_H3cMplsExtEntry_Object((1,3,6,1,4,1,2011,10,2,142,1,2,1))
h3cMplsExtEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:h3cMplsExtEntry.setStatus(_A)
class _H3cMplsExtIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cMplsExtIndex_Type.__name__=_C
_H3cMplsExtIndex_Object=MibTableColumn
h3cMplsExtIndex=_H3cMplsExtIndex_Object((1,3,6,1,4,1,2011,10,2,142,1,2,1,1),_H3cMplsExtIndex_Type())
h3cMplsExtIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cMplsExtIndex.setStatus(_A)
class _H3cMplsExtCapability_Type(TruthValue):defaultValue=2
_H3cMplsExtCapability_Type.__name__=_I
_H3cMplsExtCapability_Object=MibTableColumn
h3cMplsExtCapability=_H3cMplsExtCapability_Object((1,3,6,1,4,1,2011,10,2,142,1,2,1,2),_H3cMplsExtCapability_Type())
h3cMplsExtCapability.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cMplsExtCapability.setStatus(_A)
class _H3cMplsExtMtu_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(46,65535))
_H3cMplsExtMtu_Type.__name__=_C
_H3cMplsExtMtu_Object=MibTableColumn
h3cMplsExtMtu=_H3cMplsExtMtu_Object((1,3,6,1,4,1,2011,10,2,142,1,2,1,3),_H3cMplsExtMtu_Type())
h3cMplsExtMtu.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cMplsExtMtu.setStatus(_A)
_H3cMplsExtRowStatus_Type=RowStatus
_H3cMplsExtRowStatus_Object=MibTableColumn
h3cMplsExtRowStatus=_H3cMplsExtRowStatus_Object((1,3,6,1,4,1,2011,10,2,142,1,2,1,4),_H3cMplsExtRowStatus_Type())
h3cMplsExtRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cMplsExtRowStatus.setStatus(_A)
_H3cMplsExtLdpTable_Object=MibTable
h3cMplsExtLdpTable=_H3cMplsExtLdpTable_Object((1,3,6,1,4,1,2011,10,2,142,1,3))
if mibBuilder.loadTexts:h3cMplsExtLdpTable.setStatus(_A)
_H3cMplsExtLdpEntry_Object=MibTableRow
h3cMplsExtLdpEntry=_H3cMplsExtLdpEntry_Object((1,3,6,1,4,1,2011,10,2,142,1,3,1))
h3cMplsExtLdpEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:h3cMplsExtLdpEntry.setStatus(_A)
class _H3cMplsExtLdpIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cMplsExtLdpIndex_Type.__name__=_C
_H3cMplsExtLdpIndex_Object=MibTableColumn
h3cMplsExtLdpIndex=_H3cMplsExtLdpIndex_Object((1,3,6,1,4,1,2011,10,2,142,1,3,1,1),_H3cMplsExtLdpIndex_Type())
h3cMplsExtLdpIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cMplsExtLdpIndex.setStatus(_A)
class _H3cMplsExtLdpCapability_Type(TruthValue):defaultValue=2
_H3cMplsExtLdpCapability_Type.__name__=_I
_H3cMplsExtLdpCapability_Object=MibTableColumn
h3cMplsExtLdpCapability=_H3cMplsExtLdpCapability_Object((1,3,6,1,4,1,2011,10,2,142,1,3,1,2),_H3cMplsExtLdpCapability_Type())
h3cMplsExtLdpCapability.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cMplsExtLdpCapability.setStatus(_A)
_H3cMplsExtLdpRowStatus_Type=RowStatus
_H3cMplsExtLdpRowStatus_Object=MibTableColumn
h3cMplsExtLdpRowStatus=_H3cMplsExtLdpRowStatus_Object((1,3,6,1,4,1,2011,10,2,142,1,3,1,3),_H3cMplsExtLdpRowStatus_Type())
h3cMplsExtLdpRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cMplsExtLdpRowStatus.setStatus(_A)
_H3cMplsExtBfdTable_Object=MibTable
h3cMplsExtBfdTable=_H3cMplsExtBfdTable_Object((1,3,6,1,4,1,2011,10,2,142,1,4))
if mibBuilder.loadTexts:h3cMplsExtBfdTable.setStatus(_A)
_H3cMplsExtBfdEntry_Object=MibTableRow
h3cMplsExtBfdEntry=_H3cMplsExtBfdEntry_Object((1,3,6,1,4,1,2011,10,2,142,1,4,1))
h3cMplsExtBfdEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:h3cMplsExtBfdEntry.setStatus(_A)
class _H3cMplsExtBfdLocalDiscr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cMplsExtBfdLocalDiscr_Type.__name__=_C
_H3cMplsExtBfdLocalDiscr_Object=MibTableColumn
h3cMplsExtBfdLocalDiscr=_H3cMplsExtBfdLocalDiscr_Object((1,3,6,1,4,1,2011,10,2,142,1,4,1,1),_H3cMplsExtBfdLocalDiscr_Type())
h3cMplsExtBfdLocalDiscr.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cMplsExtBfdLocalDiscr.setStatus(_A)
class _H3cMplsExtBfdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_O,1),('lsp',2),('vpwsPw',3),('vplsPw',4),('te',5)))
_H3cMplsExtBfdType_Type.__name__=_F
_H3cMplsExtBfdType_Object=MibTableColumn
h3cMplsExtBfdType=_H3cMplsExtBfdType_Object((1,3,6,1,4,1,2011,10,2,142,1,4,1,2),_H3cMplsExtBfdType_Type())
h3cMplsExtBfdType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsExtBfdType.setStatus(_A)
_H3cMplsExtBfdBindIfIndex_Type=InterfaceIndexOrZero
_H3cMplsExtBfdBindIfIndex_Object=MibTableColumn
h3cMplsExtBfdBindIfIndex=_H3cMplsExtBfdBindIfIndex_Object((1,3,6,1,4,1,2011,10,2,142,1,4,1,3),_H3cMplsExtBfdBindIfIndex_Type())
h3cMplsExtBfdBindIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsExtBfdBindIfIndex.setStatus(_A)
class _H3cMplsExtBfdBindIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cMplsExtBfdBindIfName_Type.__name__=_J
_H3cMplsExtBfdBindIfName_Object=MibTableColumn
h3cMplsExtBfdBindIfName=_H3cMplsExtBfdBindIfName_Object((1,3,6,1,4,1,2011,10,2,142,1,4,1,4),_H3cMplsExtBfdBindIfName_Type())
h3cMplsExtBfdBindIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsExtBfdBindIfName.setStatus(_A)
class _H3cMplsExtBfdXcIndex_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_H3cMplsExtBfdXcIndex_Type.__name__=_E
_H3cMplsExtBfdXcIndex_Object=MibTableColumn
h3cMplsExtBfdXcIndex=_H3cMplsExtBfdXcIndex_Object((1,3,6,1,4,1,2011,10,2,142,1,4,1,5),_H3cMplsExtBfdXcIndex_Type())
h3cMplsExtBfdXcIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsExtBfdXcIndex.setStatus(_A)
class _H3cMplsExtBfdPwBackupFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('primary',2),('backup',3)))
_H3cMplsExtBfdPwBackupFlag_Type.__name__=_F
_H3cMplsExtBfdPwBackupFlag_Object=MibTableColumn
h3cMplsExtBfdPwBackupFlag=_H3cMplsExtBfdPwBackupFlag_Object((1,3,6,1,4,1,2011,10,2,142,1,4,1,6),_H3cMplsExtBfdPwBackupFlag_Type())
h3cMplsExtBfdPwBackupFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsExtBfdPwBackupFlag.setStatus(_A)
class _H3cMplsExtBfdPwId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_H3cMplsExtBfdPwId_Type.__name__=_C
_H3cMplsExtBfdPwId_Object=MibTableColumn
h3cMplsExtBfdPwId=_H3cMplsExtBfdPwId_Object((1,3,6,1,4,1,2011,10,2,142,1,4,1,7),_H3cMplsExtBfdPwId_Type())
h3cMplsExtBfdPwId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsExtBfdPwId.setStatus(_A)
class _H3cMplsExtBfdVsiIndex_Type(Unsigned32):defaultValue=4294967295;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cMplsExtBfdVsiIndex_Type.__name__=_C
_H3cMplsExtBfdVsiIndex_Object=MibTableColumn
h3cMplsExtBfdVsiIndex=_H3cMplsExtBfdVsiIndex_Object((1,3,6,1,4,1,2011,10,2,142,1,4,1,8),_H3cMplsExtBfdVsiIndex_Type())
h3cMplsExtBfdVsiIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsExtBfdVsiIndex.setStatus(_A)
_H3cMplsExtBfdPwPeerIpType_Type=InetAddressType
_H3cMplsExtBfdPwPeerIpType_Object=MibTableColumn
h3cMplsExtBfdPwPeerIpType=_H3cMplsExtBfdPwPeerIpType_Object((1,3,6,1,4,1,2011,10,2,142,1,4,1,9),_H3cMplsExtBfdPwPeerIpType_Type())
h3cMplsExtBfdPwPeerIpType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsExtBfdPwPeerIpType.setStatus(_A)
_H3cMplsExtBfdPwPeerIp_Type=InetAddress
_H3cMplsExtBfdPwPeerIp_Object=MibTableColumn
h3cMplsExtBfdPwPeerIp=_H3cMplsExtBfdPwPeerIp_Object((1,3,6,1,4,1,2011,10,2,142,1,4,1,10),_H3cMplsExtBfdPwPeerIp_Type())
h3cMplsExtBfdPwPeerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsExtBfdPwPeerIp.setStatus(_A)
class _H3cMplsExtBfdPwSPE_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('upe',2),('spe',3)))
_H3cMplsExtBfdPwSPE_Type.__name__=_F
_H3cMplsExtBfdPwSPE_Object=MibTableColumn
h3cMplsExtBfdPwSPE=_H3cMplsExtBfdPwSPE_Object((1,3,6,1,4,1,2011,10,2,142,1,4,1,11),_H3cMplsExtBfdPwSPE_Type())
h3cMplsExtBfdPwSPE.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsExtBfdPwSPE.setStatus(_A)
class _H3cMplsExtBfdPwEncapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)));namedValues=NamedValues(*((_O,1),('frDlciMartini',2),('atmAal5Sdu',3),('atmTransCell',4),('vlan',5),('ethernet',6),('hdlc',7),('ppp',8),('cesom',9),('atmNto1Vcc',10),('atmNto1Vpc',11),('ipInterworking',12),('atm1to1Vcc',13),('atm1to1Vpc',14),('atmAal5Pdu',15),('frPort',16),('cep',17),('satopE1',18),('satopT1',19),('satopE3',20),('satopT3',21),('esopsnBasic',22),('tdmoipAal1Mode',23),('tdmCesopsnWithCas',24),('tdmoipAal2Mode',25),('frDlci',26)))
_H3cMplsExtBfdPwEncapType_Type.__name__=_F
_H3cMplsExtBfdPwEncapType_Object=MibTableColumn
h3cMplsExtBfdPwEncapType=_H3cMplsExtBfdPwEncapType_Object((1,3,6,1,4,1,2011,10,2,142,1,4,1,12),_H3cMplsExtBfdPwEncapType_Type())
h3cMplsExtBfdPwEncapType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsExtBfdPwEncapType.setStatus(_A)
_H3cMplsExtVpnStatsTable_Object=MibTable
h3cMplsExtVpnStatsTable=_H3cMplsExtVpnStatsTable_Object((1,3,6,1,4,1,2011,10,2,142,1,5))
if mibBuilder.loadTexts:h3cMplsExtVpnStatsTable.setStatus(_A)
_H3cMplsExtVpnStatsEntry_Object=MibTableRow
h3cMplsExtVpnStatsEntry=_H3cMplsExtVpnStatsEntry_Object((1,3,6,1,4,1,2011,10,2,142,1,5,1))
h3cMplsExtVpnStatsEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:h3cMplsExtVpnStatsEntry.setStatus(_A)
class _H3cMplsExtVpnStatsVrfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cMplsExtVpnStatsVrfIndex_Type.__name__=_C
_H3cMplsExtVpnStatsVrfIndex_Object=MibTableColumn
h3cMplsExtVpnStatsVrfIndex=_H3cMplsExtVpnStatsVrfIndex_Object((1,3,6,1,4,1,2011,10,2,142,1,5,1,1),_H3cMplsExtVpnStatsVrfIndex_Type())
h3cMplsExtVpnStatsVrfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cMplsExtVpnStatsVrfIndex.setStatus(_A)
class _H3cMplsExtVpnStatsVpnName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_H3cMplsExtVpnStatsVpnName_Type.__name__=_E
_H3cMplsExtVpnStatsVpnName_Object=MibTableColumn
h3cMplsExtVpnStatsVpnName=_H3cMplsExtVpnStatsVpnName_Object((1,3,6,1,4,1,2011,10,2,142,1,5,1,2),_H3cMplsExtVpnStatsVpnName_Type())
h3cMplsExtVpnStatsVpnName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsExtVpnStatsVpnName.setStatus(_A)
_H3cMplsExtVpnStatsInOctets_Type=Counter64
_H3cMplsExtVpnStatsInOctets_Object=MibTableColumn
h3cMplsExtVpnStatsInOctets=_H3cMplsExtVpnStatsInOctets_Object((1,3,6,1,4,1,2011,10,2,142,1,5,1,3),_H3cMplsExtVpnStatsInOctets_Type())
h3cMplsExtVpnStatsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsExtVpnStatsInOctets.setStatus(_A)
_H3cMplsExtVpnStatsInPackets_Type=Counter64
_H3cMplsExtVpnStatsInPackets_Object=MibTableColumn
h3cMplsExtVpnStatsInPackets=_H3cMplsExtVpnStatsInPackets_Object((1,3,6,1,4,1,2011,10,2,142,1,5,1,4),_H3cMplsExtVpnStatsInPackets_Type())
h3cMplsExtVpnStatsInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsExtVpnStatsInPackets.setStatus(_A)
_H3cMplsExtVpnStatsInErrors_Type=Counter64
_H3cMplsExtVpnStatsInErrors_Object=MibTableColumn
h3cMplsExtVpnStatsInErrors=_H3cMplsExtVpnStatsInErrors_Object((1,3,6,1,4,1,2011,10,2,142,1,5,1,5),_H3cMplsExtVpnStatsInErrors_Type())
h3cMplsExtVpnStatsInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsExtVpnStatsInErrors.setStatus(_A)
_H3cMplsExtVpnStatsInDiscards_Type=Counter64
_H3cMplsExtVpnStatsInDiscards_Object=MibTableColumn
h3cMplsExtVpnStatsInDiscards=_H3cMplsExtVpnStatsInDiscards_Object((1,3,6,1,4,1,2011,10,2,142,1,5,1,6),_H3cMplsExtVpnStatsInDiscards_Type())
h3cMplsExtVpnStatsInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsExtVpnStatsInDiscards.setStatus(_A)
_H3cMplsExtVpnStatsOutOctets_Type=Counter64
_H3cMplsExtVpnStatsOutOctets_Object=MibTableColumn
h3cMplsExtVpnStatsOutOctets=_H3cMplsExtVpnStatsOutOctets_Object((1,3,6,1,4,1,2011,10,2,142,1,5,1,7),_H3cMplsExtVpnStatsOutOctets_Type())
h3cMplsExtVpnStatsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsExtVpnStatsOutOctets.setStatus(_A)
_H3cMplsExtVpnStatsOutPackets_Type=Counter64
_H3cMplsExtVpnStatsOutPackets_Object=MibTableColumn
h3cMplsExtVpnStatsOutPackets=_H3cMplsExtVpnStatsOutPackets_Object((1,3,6,1,4,1,2011,10,2,142,1,5,1,8),_H3cMplsExtVpnStatsOutPackets_Type())
h3cMplsExtVpnStatsOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsExtVpnStatsOutPackets.setStatus(_A)
_H3cMplsExtVpnStatsOutErrors_Type=Counter64
_H3cMplsExtVpnStatsOutErrors_Object=MibTableColumn
h3cMplsExtVpnStatsOutErrors=_H3cMplsExtVpnStatsOutErrors_Object((1,3,6,1,4,1,2011,10,2,142,1,5,1,9),_H3cMplsExtVpnStatsOutErrors_Type())
h3cMplsExtVpnStatsOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsExtVpnStatsOutErrors.setStatus(_A)
_H3cMplsExtVpnStatsOutDiscards_Type=Counter64
_H3cMplsExtVpnStatsOutDiscards_Object=MibTableColumn
h3cMplsExtVpnStatsOutDiscards=_H3cMplsExtVpnStatsOutDiscards_Object((1,3,6,1,4,1,2011,10,2,142,1,5,1,10),_H3cMplsExtVpnStatsOutDiscards_Type())
h3cMplsExtVpnStatsOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsExtVpnStatsOutDiscards.setStatus(_A)
_H3cMplsExtVpnTable_Object=MibTable
h3cMplsExtVpnTable=_H3cMplsExtVpnTable_Object((1,3,6,1,4,1,2011,10,2,142,1,6))
if mibBuilder.loadTexts:h3cMplsExtVpnTable.setStatus(_A)
_H3cMplsExtVpnEntry_Object=MibTableRow
h3cMplsExtVpnEntry=_H3cMplsExtVpnEntry_Object((1,3,6,1,4,1,2011,10,2,142,1,6,1))
h3cMplsExtVpnEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:h3cMplsExtVpnEntry.setStatus(_A)
class _H3cMplsExtVpnName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_H3cMplsExtVpnName_Type.__name__=_E
_H3cMplsExtVpnName_Object=MibTableColumn
h3cMplsExtVpnName=_H3cMplsExtVpnName_Object((1,3,6,1,4,1,2011,10,2,142,1,6,1,1),_H3cMplsExtVpnName_Type())
h3cMplsExtVpnName.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cMplsExtVpnName.setStatus(_A)
class _H3cMplsExtVrfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_H3cMplsExtVrfIndex_Type.__name__=_C
_H3cMplsExtVrfIndex_Object=MibTableColumn
h3cMplsExtVrfIndex=_H3cMplsExtVrfIndex_Object((1,3,6,1,4,1,2011,10,2,142,1,6,1,2),_H3cMplsExtVrfIndex_Type())
h3cMplsExtVrfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMplsExtVrfIndex.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'h3cMplsExt':h3cMplsExt,'h3cMplsExtObjects':h3cMplsExtObjects,'h3cMplsExtScalarGroup':h3cMplsExtScalarGroup,'h3cMplsExtLsrID':h3cMplsExtLsrID,'h3cMplsExtLdpStatus':h3cMplsExtLdpStatus,'h3cMplsExtTable':h3cMplsExtTable,'h3cMplsExtEntry':h3cMplsExtEntry,_L:h3cMplsExtIndex,'h3cMplsExtCapability':h3cMplsExtCapability,'h3cMplsExtMtu':h3cMplsExtMtu,'h3cMplsExtRowStatus':h3cMplsExtRowStatus,'h3cMplsExtLdpTable':h3cMplsExtLdpTable,'h3cMplsExtLdpEntry':h3cMplsExtLdpEntry,_M:h3cMplsExtLdpIndex,'h3cMplsExtLdpCapability':h3cMplsExtLdpCapability,'h3cMplsExtLdpRowStatus':h3cMplsExtLdpRowStatus,'h3cMplsExtBfdTable':h3cMplsExtBfdTable,'h3cMplsExtBfdEntry':h3cMplsExtBfdEntry,_N:h3cMplsExtBfdLocalDiscr,'h3cMplsExtBfdType':h3cMplsExtBfdType,'h3cMplsExtBfdBindIfIndex':h3cMplsExtBfdBindIfIndex,'h3cMplsExtBfdBindIfName':h3cMplsExtBfdBindIfName,'h3cMplsExtBfdXcIndex':h3cMplsExtBfdXcIndex,'h3cMplsExtBfdPwBackupFlag':h3cMplsExtBfdPwBackupFlag,'h3cMplsExtBfdPwId':h3cMplsExtBfdPwId,'h3cMplsExtBfdVsiIndex':h3cMplsExtBfdVsiIndex,'h3cMplsExtBfdPwPeerIpType':h3cMplsExtBfdPwPeerIpType,'h3cMplsExtBfdPwPeerIp':h3cMplsExtBfdPwPeerIp,'h3cMplsExtBfdPwSPE':h3cMplsExtBfdPwSPE,'h3cMplsExtBfdPwEncapType':h3cMplsExtBfdPwEncapType,'h3cMplsExtVpnStatsTable':h3cMplsExtVpnStatsTable,'h3cMplsExtVpnStatsEntry':h3cMplsExtVpnStatsEntry,_P:h3cMplsExtVpnStatsVrfIndex,'h3cMplsExtVpnStatsVpnName':h3cMplsExtVpnStatsVpnName,'h3cMplsExtVpnStatsInOctets':h3cMplsExtVpnStatsInOctets,'h3cMplsExtVpnStatsInPackets':h3cMplsExtVpnStatsInPackets,'h3cMplsExtVpnStatsInErrors':h3cMplsExtVpnStatsInErrors,'h3cMplsExtVpnStatsInDiscards':h3cMplsExtVpnStatsInDiscards,'h3cMplsExtVpnStatsOutOctets':h3cMplsExtVpnStatsOutOctets,'h3cMplsExtVpnStatsOutPackets':h3cMplsExtVpnStatsOutPackets,'h3cMplsExtVpnStatsOutErrors':h3cMplsExtVpnStatsOutErrors,'h3cMplsExtVpnStatsOutDiscards':h3cMplsExtVpnStatsOutDiscards,'h3cMplsExtVpnTable':h3cMplsExtVpnTable,'h3cMplsExtVpnEntry':h3cMplsExtVpnEntry,_Q:h3cMplsExtVpnName,'h3cMplsExtVrfIndex':h3cMplsExtVrfIndex})