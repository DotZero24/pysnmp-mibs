_i='ipxStaticServType'
_h='ipxStaticServName'
_g='ipxStaticServCircIndex'
_f='ipxStaticServSysInstance'
_e='ipxDestServType'
_d='ipxDestServName'
_c='ipxDestServSocket'
_b='ipxDestServNode'
_a='ipxDestServNetNum'
_Z='ipxDestServSysInstance'
_Y='ipxServName'
_X='ipxServType'
_W='ipxServSysInstance'
_V='ipxStaticRouteNetNum'
_U='ipxStaticRouteCircIndex'
_T='ipxStaticRouteSysInstance'
_S='ipxDestNetNum'
_R='ipxDestSysInstance'
_Q='ipxAdvSysInstance'
_P='ipxBasicSysInstance'
_O='NotificationType'
_N='static'
_M='nlsp'
_L='local'
_K='other'
_J='ipxCircIndex'
_I='ipxCircSysInstance'
_H='on'
_G='off'
_F='Integer32'
_E='OctetString'
_D='NOVELL-IPX-MIB'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier',_O,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_O,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class NetNumber(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_NovellMib_ObjectIdentity=ObjectIdentity
novellMib=_NovellMib_ObjectIdentity((1,3,6,1,4,1,23))
_MibDoc_ObjectIdentity=ObjectIdentity
mibDoc=_MibDoc_ObjectIdentity((1,3,6,1,4,1,23,2))
_Ipx_ObjectIdentity=ObjectIdentity
ipx=_Ipx_ObjectIdentity((1,3,6,1,4,1,23,2,5))
_IpxSystem_ObjectIdentity=ObjectIdentity
ipxSystem=_IpxSystem_ObjectIdentity((1,3,6,1,4,1,23,2,5,1))
_IpxBasicSysTable_Object=MibTable
ipxBasicSysTable=_IpxBasicSysTable_Object((1,3,6,1,4,1,23,2,5,1,1))
if mibBuilder.loadTexts:ipxBasicSysTable.setStatus(_A)
_IpxBasicSysEntry_Object=MibTableRow
ipxBasicSysEntry=_IpxBasicSysEntry_Object((1,3,6,1,4,1,23,2,5,1,1,1))
ipxBasicSysEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:ipxBasicSysEntry.setStatus(_A)
_IpxBasicSysInstance_Type=Integer32
_IpxBasicSysInstance_Object=MibTableColumn
ipxBasicSysInstance=_IpxBasicSysInstance_Object((1,3,6,1,4,1,23,2,5,1,1,1,1),_IpxBasicSysInstance_Type())
ipxBasicSysInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxBasicSysInstance.setStatus(_A)
class _IpxBasicSysExistState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_IpxBasicSysExistState_Type.__name__=_F
_IpxBasicSysExistState_Object=MibTableColumn
ipxBasicSysExistState=_IpxBasicSysExistState_Object((1,3,6,1,4,1,23,2,5,1,1,1,2),_IpxBasicSysExistState_Type())
ipxBasicSysExistState.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxBasicSysExistState.setStatus(_A)
_IpxBasicSysNetNumber_Type=NetNumber
_IpxBasicSysNetNumber_Object=MibTableColumn
ipxBasicSysNetNumber=_IpxBasicSysNetNumber_Object((1,3,6,1,4,1,23,2,5,1,1,1,3),_IpxBasicSysNetNumber_Type())
ipxBasicSysNetNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxBasicSysNetNumber.setStatus(_A)
class _IpxBasicSysNode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_IpxBasicSysNode_Type.__name__=_E
_IpxBasicSysNode_Object=MibTableColumn
ipxBasicSysNode=_IpxBasicSysNode_Object((1,3,6,1,4,1,23,2,5,1,1,1,4),_IpxBasicSysNode_Type())
ipxBasicSysNode.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxBasicSysNode.setStatus(_A)
class _IpxBasicSysName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_IpxBasicSysName_Type.__name__=_E
_IpxBasicSysName_Object=MibTableColumn
ipxBasicSysName=_IpxBasicSysName_Object((1,3,6,1,4,1,23,2,5,1,1,1,5),_IpxBasicSysName_Type())
ipxBasicSysName.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxBasicSysName.setStatus(_A)
_IpxBasicSysInReceives_Type=Counter32
_IpxBasicSysInReceives_Object=MibTableColumn
ipxBasicSysInReceives=_IpxBasicSysInReceives_Object((1,3,6,1,4,1,23,2,5,1,1,1,6),_IpxBasicSysInReceives_Type())
ipxBasicSysInReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxBasicSysInReceives.setStatus(_A)
_IpxBasicSysInHdrErrors_Type=Counter32
_IpxBasicSysInHdrErrors_Object=MibTableColumn
ipxBasicSysInHdrErrors=_IpxBasicSysInHdrErrors_Object((1,3,6,1,4,1,23,2,5,1,1,1,7),_IpxBasicSysInHdrErrors_Type())
ipxBasicSysInHdrErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxBasicSysInHdrErrors.setStatus(_A)
_IpxBasicSysInUnknownSockets_Type=Counter32
_IpxBasicSysInUnknownSockets_Object=MibTableColumn
ipxBasicSysInUnknownSockets=_IpxBasicSysInUnknownSockets_Object((1,3,6,1,4,1,23,2,5,1,1,1,8),_IpxBasicSysInUnknownSockets_Type())
ipxBasicSysInUnknownSockets.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxBasicSysInUnknownSockets.setStatus(_A)
_IpxBasicSysInDiscards_Type=Counter32
_IpxBasicSysInDiscards_Object=MibTableColumn
ipxBasicSysInDiscards=_IpxBasicSysInDiscards_Object((1,3,6,1,4,1,23,2,5,1,1,1,9),_IpxBasicSysInDiscards_Type())
ipxBasicSysInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxBasicSysInDiscards.setStatus(_A)
_IpxBasicSysInBadChecksums_Type=Counter32
_IpxBasicSysInBadChecksums_Object=MibTableColumn
ipxBasicSysInBadChecksums=_IpxBasicSysInBadChecksums_Object((1,3,6,1,4,1,23,2,5,1,1,1,10),_IpxBasicSysInBadChecksums_Type())
ipxBasicSysInBadChecksums.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxBasicSysInBadChecksums.setStatus(_A)
_IpxBasicSysInDelivers_Type=Counter32
_IpxBasicSysInDelivers_Object=MibTableColumn
ipxBasicSysInDelivers=_IpxBasicSysInDelivers_Object((1,3,6,1,4,1,23,2,5,1,1,1,11),_IpxBasicSysInDelivers_Type())
ipxBasicSysInDelivers.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxBasicSysInDelivers.setStatus(_A)
_IpxBasicSysNoRoutes_Type=Counter32
_IpxBasicSysNoRoutes_Object=MibTableColumn
ipxBasicSysNoRoutes=_IpxBasicSysNoRoutes_Object((1,3,6,1,4,1,23,2,5,1,1,1,12),_IpxBasicSysNoRoutes_Type())
ipxBasicSysNoRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxBasicSysNoRoutes.setStatus(_A)
_IpxBasicSysOutRequests_Type=Counter32
_IpxBasicSysOutRequests_Object=MibTableColumn
ipxBasicSysOutRequests=_IpxBasicSysOutRequests_Object((1,3,6,1,4,1,23,2,5,1,1,1,13),_IpxBasicSysOutRequests_Type())
ipxBasicSysOutRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxBasicSysOutRequests.setStatus(_A)
_IpxBasicSysOutMalformedRequests_Type=Counter32
_IpxBasicSysOutMalformedRequests_Object=MibTableColumn
ipxBasicSysOutMalformedRequests=_IpxBasicSysOutMalformedRequests_Object((1,3,6,1,4,1,23,2,5,1,1,1,14),_IpxBasicSysOutMalformedRequests_Type())
ipxBasicSysOutMalformedRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxBasicSysOutMalformedRequests.setStatus(_A)
_IpxBasicSysOutDiscards_Type=Counter32
_IpxBasicSysOutDiscards_Object=MibTableColumn
ipxBasicSysOutDiscards=_IpxBasicSysOutDiscards_Object((1,3,6,1,4,1,23,2,5,1,1,1,15),_IpxBasicSysOutDiscards_Type())
ipxBasicSysOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxBasicSysOutDiscards.setStatus(_A)
_IpxBasicSysOutPackets_Type=Counter32
_IpxBasicSysOutPackets_Object=MibTableColumn
ipxBasicSysOutPackets=_IpxBasicSysOutPackets_Object((1,3,6,1,4,1,23,2,5,1,1,1,16),_IpxBasicSysOutPackets_Type())
ipxBasicSysOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxBasicSysOutPackets.setStatus(_A)
_IpxBasicSysConfigSockets_Type=Integer32
_IpxBasicSysConfigSockets_Object=MibTableColumn
ipxBasicSysConfigSockets=_IpxBasicSysConfigSockets_Object((1,3,6,1,4,1,23,2,5,1,1,1,17),_IpxBasicSysConfigSockets_Type())
ipxBasicSysConfigSockets.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxBasicSysConfigSockets.setStatus(_A)
_IpxBasicSysOpenSocketFails_Type=Counter32
_IpxBasicSysOpenSocketFails_Object=MibTableColumn
ipxBasicSysOpenSocketFails=_IpxBasicSysOpenSocketFails_Object((1,3,6,1,4,1,23,2,5,1,1,1,18),_IpxBasicSysOpenSocketFails_Type())
ipxBasicSysOpenSocketFails.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxBasicSysOpenSocketFails.setStatus(_A)
_IpxAdvSysTable_Object=MibTable
ipxAdvSysTable=_IpxAdvSysTable_Object((1,3,6,1,4,1,23,2,5,1,2))
if mibBuilder.loadTexts:ipxAdvSysTable.setStatus(_A)
_IpxAdvSysEntry_Object=MibTableRow
ipxAdvSysEntry=_IpxAdvSysEntry_Object((1,3,6,1,4,1,23,2,5,1,2,1))
ipxAdvSysEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:ipxAdvSysEntry.setStatus(_A)
_IpxAdvSysInstance_Type=Integer32
_IpxAdvSysInstance_Object=MibTableColumn
ipxAdvSysInstance=_IpxAdvSysInstance_Object((1,3,6,1,4,1,23,2,5,1,2,1,1),_IpxAdvSysInstance_Type())
ipxAdvSysInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxAdvSysInstance.setStatus(_A)
class _IpxAdvSysMaxPathSplits_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_IpxAdvSysMaxPathSplits_Type.__name__=_F
_IpxAdvSysMaxPathSplits_Object=MibTableColumn
ipxAdvSysMaxPathSplits=_IpxAdvSysMaxPathSplits_Object((1,3,6,1,4,1,23,2,5,1,2,1,2),_IpxAdvSysMaxPathSplits_Type())
ipxAdvSysMaxPathSplits.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxAdvSysMaxPathSplits.setStatus(_A)
class _IpxAdvSysMaxHops_Type(Integer32):defaultValue=64
_IpxAdvSysMaxHops_Type.__name__=_F
_IpxAdvSysMaxHops_Object=MibTableColumn
ipxAdvSysMaxHops=_IpxAdvSysMaxHops_Object((1,3,6,1,4,1,23,2,5,1,2,1,3),_IpxAdvSysMaxHops_Type())
ipxAdvSysMaxHops.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxAdvSysMaxHops.setStatus(_A)
_IpxAdvSysInTooManyHops_Type=Counter32
_IpxAdvSysInTooManyHops_Object=MibTableColumn
ipxAdvSysInTooManyHops=_IpxAdvSysInTooManyHops_Object((1,3,6,1,4,1,23,2,5,1,2,1,4),_IpxAdvSysInTooManyHops_Type())
ipxAdvSysInTooManyHops.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxAdvSysInTooManyHops.setStatus(_A)
_IpxAdvSysInFiltered_Type=Counter32
_IpxAdvSysInFiltered_Object=MibTableColumn
ipxAdvSysInFiltered=_IpxAdvSysInFiltered_Object((1,3,6,1,4,1,23,2,5,1,2,1,5),_IpxAdvSysInFiltered_Type())
ipxAdvSysInFiltered.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxAdvSysInFiltered.setStatus(_A)
_IpxAdvSysInCompressDiscards_Type=Counter32
_IpxAdvSysInCompressDiscards_Object=MibTableColumn
ipxAdvSysInCompressDiscards=_IpxAdvSysInCompressDiscards_Object((1,3,6,1,4,1,23,2,5,1,2,1,6),_IpxAdvSysInCompressDiscards_Type())
ipxAdvSysInCompressDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxAdvSysInCompressDiscards.setStatus(_A)
_IpxAdvSysNETBIOSPackets_Type=Counter32
_IpxAdvSysNETBIOSPackets_Object=MibTableColumn
ipxAdvSysNETBIOSPackets=_IpxAdvSysNETBIOSPackets_Object((1,3,6,1,4,1,23,2,5,1,2,1,7),_IpxAdvSysNETBIOSPackets_Type())
ipxAdvSysNETBIOSPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxAdvSysNETBIOSPackets.setStatus(_A)
_IpxAdvSysForwPackets_Type=Counter32
_IpxAdvSysForwPackets_Object=MibTableColumn
ipxAdvSysForwPackets=_IpxAdvSysForwPackets_Object((1,3,6,1,4,1,23,2,5,1,2,1,8),_IpxAdvSysForwPackets_Type())
ipxAdvSysForwPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxAdvSysForwPackets.setStatus(_A)
_IpxAdvSysOutFiltered_Type=Counter32
_IpxAdvSysOutFiltered_Object=MibTableColumn
ipxAdvSysOutFiltered=_IpxAdvSysOutFiltered_Object((1,3,6,1,4,1,23,2,5,1,2,1,9),_IpxAdvSysOutFiltered_Type())
ipxAdvSysOutFiltered.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxAdvSysOutFiltered.setStatus(_A)
_IpxAdvSysOutCompressDiscards_Type=Counter32
_IpxAdvSysOutCompressDiscards_Object=MibTableColumn
ipxAdvSysOutCompressDiscards=_IpxAdvSysOutCompressDiscards_Object((1,3,6,1,4,1,23,2,5,1,2,1,10),_IpxAdvSysOutCompressDiscards_Type())
ipxAdvSysOutCompressDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxAdvSysOutCompressDiscards.setStatus(_A)
_IpxAdvSysCircCount_Type=Integer32
_IpxAdvSysCircCount_Object=MibTableColumn
ipxAdvSysCircCount=_IpxAdvSysCircCount_Object((1,3,6,1,4,1,23,2,5,1,2,1,11),_IpxAdvSysCircCount_Type())
ipxAdvSysCircCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxAdvSysCircCount.setStatus(_A)
_IpxAdvSysDestCount_Type=Integer32
_IpxAdvSysDestCount_Object=MibTableColumn
ipxAdvSysDestCount=_IpxAdvSysDestCount_Object((1,3,6,1,4,1,23,2,5,1,2,1,12),_IpxAdvSysDestCount_Type())
ipxAdvSysDestCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxAdvSysDestCount.setStatus(_A)
_IpxAdvSysServCount_Type=Integer32
_IpxAdvSysServCount_Object=MibTableColumn
ipxAdvSysServCount=_IpxAdvSysServCount_Object((1,3,6,1,4,1,23,2,5,1,2,1,13),_IpxAdvSysServCount_Type())
ipxAdvSysServCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxAdvSysServCount.setStatus(_A)
_IpxCircuit_ObjectIdentity=ObjectIdentity
ipxCircuit=_IpxCircuit_ObjectIdentity((1,3,6,1,4,1,23,2,5,2))
_IpxCircTable_Object=MibTable
ipxCircTable=_IpxCircTable_Object((1,3,6,1,4,1,23,2,5,2,1))
if mibBuilder.loadTexts:ipxCircTable.setStatus(_A)
_IpxCircEntry_Object=MibTableRow
ipxCircEntry=_IpxCircEntry_Object((1,3,6,1,4,1,23,2,5,2,1,1))
ipxCircEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:ipxCircEntry.setStatus(_A)
_IpxCircSysInstance_Type=Integer32
_IpxCircSysInstance_Object=MibTableColumn
ipxCircSysInstance=_IpxCircSysInstance_Object((1,3,6,1,4,1,23,2,5,2,1,1,1),_IpxCircSysInstance_Type())
ipxCircSysInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxCircSysInstance.setStatus(_A)
_IpxCircIndex_Type=Integer32
_IpxCircIndex_Object=MibTableColumn
ipxCircIndex=_IpxCircIndex_Object((1,3,6,1,4,1,23,2,5,2,1,1,2),_IpxCircIndex_Type())
ipxCircIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxCircIndex.setStatus(_A)
class _IpxCircExistState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_IpxCircExistState_Type.__name__=_F
_IpxCircExistState_Object=MibTableColumn
ipxCircExistState=_IpxCircExistState_Object((1,3,6,1,4,1,23,2,5,2,1,1,3),_IpxCircExistState_Type())
ipxCircExistState.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxCircExistState.setStatus(_A)
class _IpxCircOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('down',1),('up',2),('sleeping',3)))
_IpxCircOperState_Type.__name__=_F
_IpxCircOperState_Object=MibTableColumn
ipxCircOperState=_IpxCircOperState_Object((1,3,6,1,4,1,23,2,5,2,1,1,4),_IpxCircOperState_Type())
ipxCircOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxCircOperState.setStatus(_A)
_IpxCircIfIndex_Type=Integer32
_IpxCircIfIndex_Object=MibTableColumn
ipxCircIfIndex=_IpxCircIfIndex_Object((1,3,6,1,4,1,23,2,5,2,1,1,5),_IpxCircIfIndex_Type())
ipxCircIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxCircIfIndex.setStatus(_A)
class _IpxCircName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_IpxCircName_Type.__name__=_E
_IpxCircName_Object=MibTableColumn
ipxCircName=_IpxCircName_Object((1,3,6,1,4,1,23,2,5,2,1,1,6),_IpxCircName_Type())
ipxCircName.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxCircName.setStatus(_A)
class _IpxCircType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_K,1),('broadcast',2),('ptToPt',3),('wanRIP',4),('unnumberedRIP',5),('dynamic',6),('wanWS',7)))
_IpxCircType_Type.__name__=_F
_IpxCircType_Object=MibTableColumn
ipxCircType=_IpxCircType_Object((1,3,6,1,4,1,23,2,5,2,1,1,7),_IpxCircType_Type())
ipxCircType.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxCircType.setStatus(_A)
class _IpxCircDialName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_IpxCircDialName_Type.__name__=_E
_IpxCircDialName_Object=MibTableColumn
ipxCircDialName=_IpxCircDialName_Object((1,3,6,1,4,1,23,2,5,2,1,1,8),_IpxCircDialName_Type())
ipxCircDialName.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxCircDialName.setStatus(_A)
_IpxCircLocalMaxPacketSize_Type=Integer32
_IpxCircLocalMaxPacketSize_Object=MibTableColumn
ipxCircLocalMaxPacketSize=_IpxCircLocalMaxPacketSize_Object((1,3,6,1,4,1,23,2,5,2,1,1,9),_IpxCircLocalMaxPacketSize_Type())
ipxCircLocalMaxPacketSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxCircLocalMaxPacketSize.setStatus(_A)
class _IpxCircCompressState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_IpxCircCompressState_Type.__name__=_F
_IpxCircCompressState_Object=MibTableColumn
ipxCircCompressState=_IpxCircCompressState_Object((1,3,6,1,4,1,23,2,5,2,1,1,10),_IpxCircCompressState_Type())
ipxCircCompressState.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxCircCompressState.setStatus(_A)
class _IpxCircCompressSlots_Type(Integer32):defaultValue=16
_IpxCircCompressSlots_Type.__name__=_F
_IpxCircCompressSlots_Object=MibTableColumn
ipxCircCompressSlots=_IpxCircCompressSlots_Object((1,3,6,1,4,1,23,2,5,2,1,1,11),_IpxCircCompressSlots_Type())
ipxCircCompressSlots.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxCircCompressSlots.setStatus(_A)
class _IpxCircStaticStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('unknown',1),('current',2),('changed',3),('read',4),('reading',5),('write',6),('writing',7)))
_IpxCircStaticStatus_Type.__name__=_F
_IpxCircStaticStatus_Object=MibTableColumn
ipxCircStaticStatus=_IpxCircStaticStatus_Object((1,3,6,1,4,1,23,2,5,2,1,1,12),_IpxCircStaticStatus_Type())
ipxCircStaticStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxCircStaticStatus.setStatus(_A)
_IpxCircCompressedSent_Type=Counter32
_IpxCircCompressedSent_Object=MibTableColumn
ipxCircCompressedSent=_IpxCircCompressedSent_Object((1,3,6,1,4,1,23,2,5,2,1,1,13),_IpxCircCompressedSent_Type())
ipxCircCompressedSent.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxCircCompressedSent.setStatus(_A)
_IpxCircCompressedInitSent_Type=Counter32
_IpxCircCompressedInitSent_Object=MibTableColumn
ipxCircCompressedInitSent=_IpxCircCompressedInitSent_Object((1,3,6,1,4,1,23,2,5,2,1,1,14),_IpxCircCompressedInitSent_Type())
ipxCircCompressedInitSent.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxCircCompressedInitSent.setStatus(_A)
_IpxCircCompressedRejectsSent_Type=Counter32
_IpxCircCompressedRejectsSent_Object=MibTableColumn
ipxCircCompressedRejectsSent=_IpxCircCompressedRejectsSent_Object((1,3,6,1,4,1,23,2,5,2,1,1,15),_IpxCircCompressedRejectsSent_Type())
ipxCircCompressedRejectsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxCircCompressedRejectsSent.setStatus(_A)
_IpxCircUncompressedSent_Type=Counter32
_IpxCircUncompressedSent_Object=MibTableColumn
ipxCircUncompressedSent=_IpxCircUncompressedSent_Object((1,3,6,1,4,1,23,2,5,2,1,1,16),_IpxCircUncompressedSent_Type())
ipxCircUncompressedSent.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxCircUncompressedSent.setStatus(_A)
_IpxCircCompressedReceived_Type=Counter32
_IpxCircCompressedReceived_Object=MibTableColumn
ipxCircCompressedReceived=_IpxCircCompressedReceived_Object((1,3,6,1,4,1,23,2,5,2,1,1,17),_IpxCircCompressedReceived_Type())
ipxCircCompressedReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxCircCompressedReceived.setStatus(_A)
_IpxCircCompressedInitReceived_Type=Counter32
_IpxCircCompressedInitReceived_Object=MibTableColumn
ipxCircCompressedInitReceived=_IpxCircCompressedInitReceived_Object((1,3,6,1,4,1,23,2,5,2,1,1,18),_IpxCircCompressedInitReceived_Type())
ipxCircCompressedInitReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxCircCompressedInitReceived.setStatus(_A)
_IpxCircCompressedRejectsReceived_Type=Counter32
_IpxCircCompressedRejectsReceived_Object=MibTableColumn
ipxCircCompressedRejectsReceived=_IpxCircCompressedRejectsReceived_Object((1,3,6,1,4,1,23,2,5,2,1,1,19),_IpxCircCompressedRejectsReceived_Type())
ipxCircCompressedRejectsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxCircCompressedRejectsReceived.setStatus(_A)
_IpxCircUncompressedReceived_Type=Counter32
_IpxCircUncompressedReceived_Object=MibTableColumn
ipxCircUncompressedReceived=_IpxCircUncompressedReceived_Object((1,3,6,1,4,1,23,2,5,2,1,1,20),_IpxCircUncompressedReceived_Type())
ipxCircUncompressedReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxCircUncompressedReceived.setStatus(_A)
class _IpxCircMediaType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_IpxCircMediaType_Type.__name__=_E
_IpxCircMediaType_Object=MibTableColumn
ipxCircMediaType=_IpxCircMediaType_Object((1,3,6,1,4,1,23,2,5,2,1,1,21),_IpxCircMediaType_Type())
ipxCircMediaType.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxCircMediaType.setStatus(_A)
_IpxCircNetNumber_Type=NetNumber
_IpxCircNetNumber_Object=MibTableColumn
ipxCircNetNumber=_IpxCircNetNumber_Object((1,3,6,1,4,1,23,2,5,2,1,1,22),_IpxCircNetNumber_Type())
ipxCircNetNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxCircNetNumber.setStatus(_A)
_IpxCircStateChanges_Type=Counter32
_IpxCircStateChanges_Object=MibTableColumn
ipxCircStateChanges=_IpxCircStateChanges_Object((1,3,6,1,4,1,23,2,5,2,1,1,23),_IpxCircStateChanges_Type())
ipxCircStateChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxCircStateChanges.setStatus(_A)
_IpxCircInitFails_Type=Counter32
_IpxCircInitFails_Object=MibTableColumn
ipxCircInitFails=_IpxCircInitFails_Object((1,3,6,1,4,1,23,2,5,2,1,1,24),_IpxCircInitFails_Type())
ipxCircInitFails.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxCircInitFails.setStatus(_A)
_IpxCircDelay_Type=Integer32
_IpxCircDelay_Object=MibTableColumn
ipxCircDelay=_IpxCircDelay_Object((1,3,6,1,4,1,23,2,5,2,1,1,25),_IpxCircDelay_Type())
ipxCircDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxCircDelay.setStatus(_A)
_IpxCircThroughput_Type=Integer32
_IpxCircThroughput_Object=MibTableColumn
ipxCircThroughput=_IpxCircThroughput_Object((1,3,6,1,4,1,23,2,5,2,1,1,26),_IpxCircThroughput_Type())
ipxCircThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxCircThroughput.setStatus(_A)
class _IpxCircNeighRouterName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_IpxCircNeighRouterName_Type.__name__=_E
_IpxCircNeighRouterName_Object=MibTableColumn
ipxCircNeighRouterName=_IpxCircNeighRouterName_Object((1,3,6,1,4,1,23,2,5,2,1,1,27),_IpxCircNeighRouterName_Type())
ipxCircNeighRouterName.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxCircNeighRouterName.setStatus(_A)
_IpxCircNeighInternalNetNum_Type=NetNumber
_IpxCircNeighInternalNetNum_Object=MibTableColumn
ipxCircNeighInternalNetNum=_IpxCircNeighInternalNetNum_Object((1,3,6,1,4,1,23,2,5,2,1,1,28),_IpxCircNeighInternalNetNum_Type())
ipxCircNeighInternalNetNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxCircNeighInternalNetNum.setStatus(_A)
_IpxForwarding_ObjectIdentity=ObjectIdentity
ipxForwarding=_IpxForwarding_ObjectIdentity((1,3,6,1,4,1,23,2,5,3))
_IpxDestTable_Object=MibTable
ipxDestTable=_IpxDestTable_Object((1,3,6,1,4,1,23,2,5,3,1))
if mibBuilder.loadTexts:ipxDestTable.setStatus(_A)
_IpxDestEntry_Object=MibTableRow
ipxDestEntry=_IpxDestEntry_Object((1,3,6,1,4,1,23,2,5,3,1,1))
ipxDestEntry.setIndexNames((0,_D,_R),(0,_D,_S))
if mibBuilder.loadTexts:ipxDestEntry.setStatus(_A)
_IpxDestSysInstance_Type=Integer32
_IpxDestSysInstance_Object=MibTableColumn
ipxDestSysInstance=_IpxDestSysInstance_Object((1,3,6,1,4,1,23,2,5,3,1,1,1),_IpxDestSysInstance_Type())
ipxDestSysInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxDestSysInstance.setStatus(_A)
_IpxDestNetNum_Type=NetNumber
_IpxDestNetNum_Object=MibTableColumn
ipxDestNetNum=_IpxDestNetNum_Object((1,3,6,1,4,1,23,2,5,3,1,1,2),_IpxDestNetNum_Type())
ipxDestNetNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxDestNetNum.setStatus(_A)
class _IpxDestProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_K,1),(_L,2),('rip',3),(_M,4),(_N,5)))
_IpxDestProtocol_Type.__name__=_F
_IpxDestProtocol_Object=MibTableColumn
ipxDestProtocol=_IpxDestProtocol_Object((1,3,6,1,4,1,23,2,5,3,1,1,3),_IpxDestProtocol_Type())
ipxDestProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxDestProtocol.setStatus(_A)
_IpxDestTicks_Type=Integer32
_IpxDestTicks_Object=MibTableColumn
ipxDestTicks=_IpxDestTicks_Object((1,3,6,1,4,1,23,2,5,3,1,1,4),_IpxDestTicks_Type())
ipxDestTicks.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxDestTicks.setStatus(_A)
_IpxDestHopCount_Type=Integer32
_IpxDestHopCount_Object=MibTableColumn
ipxDestHopCount=_IpxDestHopCount_Object((1,3,6,1,4,1,23,2,5,3,1,1,5),_IpxDestHopCount_Type())
ipxDestHopCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxDestHopCount.setStatus(_A)
_IpxDestNextHopCircIndex_Type=Integer32
_IpxDestNextHopCircIndex_Object=MibTableColumn
ipxDestNextHopCircIndex=_IpxDestNextHopCircIndex_Object((1,3,6,1,4,1,23,2,5,3,1,1,6),_IpxDestNextHopCircIndex_Type())
ipxDestNextHopCircIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxDestNextHopCircIndex.setStatus(_A)
_IpxDestNextHopNICAddress_Type=PhysAddress
_IpxDestNextHopNICAddress_Object=MibTableColumn
ipxDestNextHopNICAddress=_IpxDestNextHopNICAddress_Object((1,3,6,1,4,1,23,2,5,3,1,1,7),_IpxDestNextHopNICAddress_Type())
ipxDestNextHopNICAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxDestNextHopNICAddress.setStatus(_A)
_IpxDestNextHopNetNum_Type=NetNumber
_IpxDestNextHopNetNum_Object=MibTableColumn
ipxDestNextHopNetNum=_IpxDestNextHopNetNum_Object((1,3,6,1,4,1,23,2,5,3,1,1,8),_IpxDestNextHopNetNum_Type())
ipxDestNextHopNetNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxDestNextHopNetNum.setStatus(_A)
_IpxStaticRouteTable_Object=MibTable
ipxStaticRouteTable=_IpxStaticRouteTable_Object((1,3,6,1,4,1,23,2,5,3,2))
if mibBuilder.loadTexts:ipxStaticRouteTable.setStatus(_A)
_IpxStaticRouteEntry_Object=MibTableRow
ipxStaticRouteEntry=_IpxStaticRouteEntry_Object((1,3,6,1,4,1,23,2,5,3,2,1))
ipxStaticRouteEntry.setIndexNames((0,_D,_T),(0,_D,_U),(0,_D,_V))
if mibBuilder.loadTexts:ipxStaticRouteEntry.setStatus(_A)
_IpxStaticRouteSysInstance_Type=Integer32
_IpxStaticRouteSysInstance_Object=MibTableColumn
ipxStaticRouteSysInstance=_IpxStaticRouteSysInstance_Object((1,3,6,1,4,1,23,2,5,3,2,1,1),_IpxStaticRouteSysInstance_Type())
ipxStaticRouteSysInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxStaticRouteSysInstance.setStatus(_A)
_IpxStaticRouteCircIndex_Type=Integer32
_IpxStaticRouteCircIndex_Object=MibTableColumn
ipxStaticRouteCircIndex=_IpxStaticRouteCircIndex_Object((1,3,6,1,4,1,23,2,5,3,2,1,2),_IpxStaticRouteCircIndex_Type())
ipxStaticRouteCircIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxStaticRouteCircIndex.setStatus(_A)
_IpxStaticRouteNetNum_Type=NetNumber
_IpxStaticRouteNetNum_Object=MibTableColumn
ipxStaticRouteNetNum=_IpxStaticRouteNetNum_Object((1,3,6,1,4,1,23,2,5,3,2,1,3),_IpxStaticRouteNetNum_Type())
ipxStaticRouteNetNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxStaticRouteNetNum.setStatus(_A)
class _IpxStaticRouteExistState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_IpxStaticRouteExistState_Type.__name__=_F
_IpxStaticRouteExistState_Object=MibTableColumn
ipxStaticRouteExistState=_IpxStaticRouteExistState_Object((1,3,6,1,4,1,23,2,5,3,2,1,4),_IpxStaticRouteExistState_Type())
ipxStaticRouteExistState.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxStaticRouteExistState.setStatus(_A)
_IpxStaticRouteTicks_Type=Integer32
_IpxStaticRouteTicks_Object=MibTableColumn
ipxStaticRouteTicks=_IpxStaticRouteTicks_Object((1,3,6,1,4,1,23,2,5,3,2,1,5),_IpxStaticRouteTicks_Type())
ipxStaticRouteTicks.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxStaticRouteTicks.setStatus(_A)
_IpxStaticRouteHopCount_Type=Integer32
_IpxStaticRouteHopCount_Object=MibTableColumn
ipxStaticRouteHopCount=_IpxStaticRouteHopCount_Object((1,3,6,1,4,1,23,2,5,3,2,1,6),_IpxStaticRouteHopCount_Type())
ipxStaticRouteHopCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxStaticRouteHopCount.setStatus(_A)
_IpxServices_ObjectIdentity=ObjectIdentity
ipxServices=_IpxServices_ObjectIdentity((1,3,6,1,4,1,23,2,5,4))
_IpxServTable_Object=MibTable
ipxServTable=_IpxServTable_Object((1,3,6,1,4,1,23,2,5,4,1))
if mibBuilder.loadTexts:ipxServTable.setStatus(_A)
_IpxServEntry_Object=MibTableRow
ipxServEntry=_IpxServEntry_Object((1,3,6,1,4,1,23,2,5,4,1,1))
ipxServEntry.setIndexNames((0,_D,_W),(0,_D,_X),(0,_D,_Y))
if mibBuilder.loadTexts:ipxServEntry.setStatus(_A)
_IpxServSysInstance_Type=Integer32
_IpxServSysInstance_Object=MibTableColumn
ipxServSysInstance=_IpxServSysInstance_Object((1,3,6,1,4,1,23,2,5,4,1,1,1),_IpxServSysInstance_Type())
ipxServSysInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxServSysInstance.setStatus(_A)
class _IpxServType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_IpxServType_Type.__name__=_E
_IpxServType_Object=MibTableColumn
ipxServType=_IpxServType_Object((1,3,6,1,4,1,23,2,5,4,1,1,2),_IpxServType_Type())
ipxServType.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxServType.setStatus(_A)
class _IpxServName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,48))
_IpxServName_Type.__name__=_E
_IpxServName_Object=MibTableColumn
ipxServName=_IpxServName_Object((1,3,6,1,4,1,23,2,5,4,1,1,3),_IpxServName_Type())
ipxServName.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxServName.setStatus(_A)
class _IpxServProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,6)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,4),(_N,5),('sap',6)))
_IpxServProtocol_Type.__name__=_F
_IpxServProtocol_Object=MibTableColumn
ipxServProtocol=_IpxServProtocol_Object((1,3,6,1,4,1,23,2,5,4,1,1,4),_IpxServProtocol_Type())
ipxServProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxServProtocol.setStatus(_A)
_IpxServNetNum_Type=NetNumber
_IpxServNetNum_Object=MibTableColumn
ipxServNetNum=_IpxServNetNum_Object((1,3,6,1,4,1,23,2,5,4,1,1,5),_IpxServNetNum_Type())
ipxServNetNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxServNetNum.setStatus(_A)
class _IpxServNode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_IpxServNode_Type.__name__=_E
_IpxServNode_Object=MibTableColumn
ipxServNode=_IpxServNode_Object((1,3,6,1,4,1,23,2,5,4,1,1,6),_IpxServNode_Type())
ipxServNode.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxServNode.setStatus(_A)
class _IpxServSocket_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_IpxServSocket_Type.__name__=_E
_IpxServSocket_Object=MibTableColumn
ipxServSocket=_IpxServSocket_Object((1,3,6,1,4,1,23,2,5,4,1,1,7),_IpxServSocket_Type())
ipxServSocket.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxServSocket.setStatus(_A)
_IpxServHopCount_Type=Integer32
_IpxServHopCount_Object=MibTableColumn
ipxServHopCount=_IpxServHopCount_Object((1,3,6,1,4,1,23,2,5,4,1,1,8),_IpxServHopCount_Type())
ipxServHopCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxServHopCount.setStatus(_A)
_IpxDestServTable_Object=MibTable
ipxDestServTable=_IpxDestServTable_Object((1,3,6,1,4,1,23,2,5,4,2))
if mibBuilder.loadTexts:ipxDestServTable.setStatus(_A)
_IpxDestServEntry_Object=MibTableRow
ipxDestServEntry=_IpxDestServEntry_Object((1,3,6,1,4,1,23,2,5,4,2,1))
ipxDestServEntry.setIndexNames((0,_D,_Z),(0,_D,_a),(0,_D,_b),(0,_D,_c),(0,_D,_d),(0,_D,_e))
if mibBuilder.loadTexts:ipxDestServEntry.setStatus(_A)
_IpxDestServSysInstance_Type=Integer32
_IpxDestServSysInstance_Object=MibTableColumn
ipxDestServSysInstance=_IpxDestServSysInstance_Object((1,3,6,1,4,1,23,2,5,4,2,1,1),_IpxDestServSysInstance_Type())
ipxDestServSysInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxDestServSysInstance.setStatus(_A)
_IpxDestServNetNum_Type=NetNumber
_IpxDestServNetNum_Object=MibTableColumn
ipxDestServNetNum=_IpxDestServNetNum_Object((1,3,6,1,4,1,23,2,5,4,2,1,2),_IpxDestServNetNum_Type())
ipxDestServNetNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxDestServNetNum.setStatus(_A)
class _IpxDestServNode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_IpxDestServNode_Type.__name__=_E
_IpxDestServNode_Object=MibTableColumn
ipxDestServNode=_IpxDestServNode_Object((1,3,6,1,4,1,23,2,5,4,2,1,3),_IpxDestServNode_Type())
ipxDestServNode.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxDestServNode.setStatus(_A)
class _IpxDestServSocket_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_IpxDestServSocket_Type.__name__=_E
_IpxDestServSocket_Object=MibTableColumn
ipxDestServSocket=_IpxDestServSocket_Object((1,3,6,1,4,1,23,2,5,4,2,1,4),_IpxDestServSocket_Type())
ipxDestServSocket.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxDestServSocket.setStatus(_A)
class _IpxDestServName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,48))
_IpxDestServName_Type.__name__=_E
_IpxDestServName_Object=MibTableColumn
ipxDestServName=_IpxDestServName_Object((1,3,6,1,4,1,23,2,5,4,2,1,5),_IpxDestServName_Type())
ipxDestServName.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxDestServName.setStatus(_A)
class _IpxDestServType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_IpxDestServType_Type.__name__=_E
_IpxDestServType_Object=MibTableColumn
ipxDestServType=_IpxDestServType_Object((1,3,6,1,4,1,23,2,5,4,2,1,6),_IpxDestServType_Type())
ipxDestServType.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxDestServType.setStatus(_A)
class _IpxDestServProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,6)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,4),(_N,5),('sap',6)))
_IpxDestServProtocol_Type.__name__=_F
_IpxDestServProtocol_Object=MibTableColumn
ipxDestServProtocol=_IpxDestServProtocol_Object((1,3,6,1,4,1,23,2,5,4,2,1,7),_IpxDestServProtocol_Type())
ipxDestServProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxDestServProtocol.setStatus(_A)
_IpxDestServHopCount_Type=Integer32
_IpxDestServHopCount_Object=MibTableColumn
ipxDestServHopCount=_IpxDestServHopCount_Object((1,3,6,1,4,1,23,2,5,4,2,1,8),_IpxDestServHopCount_Type())
ipxDestServHopCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ipxDestServHopCount.setStatus(_A)
_IpxStaticServTable_Object=MibTable
ipxStaticServTable=_IpxStaticServTable_Object((1,3,6,1,4,1,23,2,5,4,3))
if mibBuilder.loadTexts:ipxStaticServTable.setStatus(_A)
_IpxStaticServEntry_Object=MibTableRow
ipxStaticServEntry=_IpxStaticServEntry_Object((1,3,6,1,4,1,23,2,5,4,3,1))
ipxStaticServEntry.setIndexNames((0,_D,_f),(0,_D,_g),(0,_D,_h),(0,_D,_i))
if mibBuilder.loadTexts:ipxStaticServEntry.setStatus(_A)
_IpxStaticServSysInstance_Type=Integer32
_IpxStaticServSysInstance_Object=MibTableColumn
ipxStaticServSysInstance=_IpxStaticServSysInstance_Object((1,3,6,1,4,1,23,2,5,4,3,1,1),_IpxStaticServSysInstance_Type())
ipxStaticServSysInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxStaticServSysInstance.setStatus(_A)
_IpxStaticServCircIndex_Type=Integer32
_IpxStaticServCircIndex_Object=MibTableColumn
ipxStaticServCircIndex=_IpxStaticServCircIndex_Object((1,3,6,1,4,1,23,2,5,4,3,1,2),_IpxStaticServCircIndex_Type())
ipxStaticServCircIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxStaticServCircIndex.setStatus(_A)
class _IpxStaticServName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,48))
_IpxStaticServName_Type.__name__=_E
_IpxStaticServName_Object=MibTableColumn
ipxStaticServName=_IpxStaticServName_Object((1,3,6,1,4,1,23,2,5,4,3,1,3),_IpxStaticServName_Type())
ipxStaticServName.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxStaticServName.setStatus(_A)
class _IpxStaticServType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_IpxStaticServType_Type.__name__=_E
_IpxStaticServType_Object=MibTableColumn
ipxStaticServType=_IpxStaticServType_Object((1,3,6,1,4,1,23,2,5,4,3,1,4),_IpxStaticServType_Type())
ipxStaticServType.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxStaticServType.setStatus(_A)
class _IpxStaticServExistState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_IpxStaticServExistState_Type.__name__=_F
_IpxStaticServExistState_Object=MibTableColumn
ipxStaticServExistState=_IpxStaticServExistState_Object((1,3,6,1,4,1,23,2,5,4,3,1,5),_IpxStaticServExistState_Type())
ipxStaticServExistState.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxStaticServExistState.setStatus(_A)
_IpxStaticServNetNum_Type=NetNumber
_IpxStaticServNetNum_Object=MibTableColumn
ipxStaticServNetNum=_IpxStaticServNetNum_Object((1,3,6,1,4,1,23,2,5,4,3,1,6),_IpxStaticServNetNum_Type())
ipxStaticServNetNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxStaticServNetNum.setStatus(_A)
class _IpxStaticServNode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_IpxStaticServNode_Type.__name__=_E
_IpxStaticServNode_Object=MibTableColumn
ipxStaticServNode=_IpxStaticServNode_Object((1,3,6,1,4,1,23,2,5,4,3,1,7),_IpxStaticServNode_Type())
ipxStaticServNode.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxStaticServNode.setStatus(_A)
class _IpxStaticServSocket_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_IpxStaticServSocket_Type.__name__=_E
_IpxStaticServSocket_Object=MibTableColumn
ipxStaticServSocket=_IpxStaticServSocket_Object((1,3,6,1,4,1,23,2,5,4,3,1,8),_IpxStaticServSocket_Type())
ipxStaticServSocket.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxStaticServSocket.setStatus(_A)
_IpxStaticServHopCount_Type=Integer32
_IpxStaticServHopCount_Object=MibTableColumn
ipxStaticServHopCount=_IpxStaticServHopCount_Object((1,3,6,1,4,1,23,2,5,4,3,1,9),_IpxStaticServHopCount_Type())
ipxStaticServHopCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxStaticServHopCount.setStatus(_A)
_IpxTraps_ObjectIdentity=ObjectIdentity
ipxTraps=_IpxTraps_ObjectIdentity((1,3,6,1,4,1,23,2,5,5))
ipxTrapCircuitDown=NotificationType((1,3,6,1,4,1,23,2,5,5,0,1))
ipxTrapCircuitDown.setObjects(*((_D,_I),(_D,_J)))
if mibBuilder.loadTexts:ipxTrapCircuitDown.setStatus('')
ipxTrapCircuitUp=NotificationType((1,3,6,1,4,1,23,2,5,5,0,2))
ipxTrapCircuitUp.setObjects(*((_D,_I),(_D,_J)))
if mibBuilder.loadTexts:ipxTrapCircuitUp.setStatus('')
mibBuilder.exportSymbols(_D,**{'NetNumber':NetNumber,'novellMib':novellMib,'mibDoc':mibDoc,'ipx':ipx,'ipxSystem':ipxSystem,'ipxBasicSysTable':ipxBasicSysTable,'ipxBasicSysEntry':ipxBasicSysEntry,_P:ipxBasicSysInstance,'ipxBasicSysExistState':ipxBasicSysExistState,'ipxBasicSysNetNumber':ipxBasicSysNetNumber,'ipxBasicSysNode':ipxBasicSysNode,'ipxBasicSysName':ipxBasicSysName,'ipxBasicSysInReceives':ipxBasicSysInReceives,'ipxBasicSysInHdrErrors':ipxBasicSysInHdrErrors,'ipxBasicSysInUnknownSockets':ipxBasicSysInUnknownSockets,'ipxBasicSysInDiscards':ipxBasicSysInDiscards,'ipxBasicSysInBadChecksums':ipxBasicSysInBadChecksums,'ipxBasicSysInDelivers':ipxBasicSysInDelivers,'ipxBasicSysNoRoutes':ipxBasicSysNoRoutes,'ipxBasicSysOutRequests':ipxBasicSysOutRequests,'ipxBasicSysOutMalformedRequests':ipxBasicSysOutMalformedRequests,'ipxBasicSysOutDiscards':ipxBasicSysOutDiscards,'ipxBasicSysOutPackets':ipxBasicSysOutPackets,'ipxBasicSysConfigSockets':ipxBasicSysConfigSockets,'ipxBasicSysOpenSocketFails':ipxBasicSysOpenSocketFails,'ipxAdvSysTable':ipxAdvSysTable,'ipxAdvSysEntry':ipxAdvSysEntry,_Q:ipxAdvSysInstance,'ipxAdvSysMaxPathSplits':ipxAdvSysMaxPathSplits,'ipxAdvSysMaxHops':ipxAdvSysMaxHops,'ipxAdvSysInTooManyHops':ipxAdvSysInTooManyHops,'ipxAdvSysInFiltered':ipxAdvSysInFiltered,'ipxAdvSysInCompressDiscards':ipxAdvSysInCompressDiscards,'ipxAdvSysNETBIOSPackets':ipxAdvSysNETBIOSPackets,'ipxAdvSysForwPackets':ipxAdvSysForwPackets,'ipxAdvSysOutFiltered':ipxAdvSysOutFiltered,'ipxAdvSysOutCompressDiscards':ipxAdvSysOutCompressDiscards,'ipxAdvSysCircCount':ipxAdvSysCircCount,'ipxAdvSysDestCount':ipxAdvSysDestCount,'ipxAdvSysServCount':ipxAdvSysServCount,'ipxCircuit':ipxCircuit,'ipxCircTable':ipxCircTable,'ipxCircEntry':ipxCircEntry,_I:ipxCircSysInstance,_J:ipxCircIndex,'ipxCircExistState':ipxCircExistState,'ipxCircOperState':ipxCircOperState,'ipxCircIfIndex':ipxCircIfIndex,'ipxCircName':ipxCircName,'ipxCircType':ipxCircType,'ipxCircDialName':ipxCircDialName,'ipxCircLocalMaxPacketSize':ipxCircLocalMaxPacketSize,'ipxCircCompressState':ipxCircCompressState,'ipxCircCompressSlots':ipxCircCompressSlots,'ipxCircStaticStatus':ipxCircStaticStatus,'ipxCircCompressedSent':ipxCircCompressedSent,'ipxCircCompressedInitSent':ipxCircCompressedInitSent,'ipxCircCompressedRejectsSent':ipxCircCompressedRejectsSent,'ipxCircUncompressedSent':ipxCircUncompressedSent,'ipxCircCompressedReceived':ipxCircCompressedReceived,'ipxCircCompressedInitReceived':ipxCircCompressedInitReceived,'ipxCircCompressedRejectsReceived':ipxCircCompressedRejectsReceived,'ipxCircUncompressedReceived':ipxCircUncompressedReceived,'ipxCircMediaType':ipxCircMediaType,'ipxCircNetNumber':ipxCircNetNumber,'ipxCircStateChanges':ipxCircStateChanges,'ipxCircInitFails':ipxCircInitFails,'ipxCircDelay':ipxCircDelay,'ipxCircThroughput':ipxCircThroughput,'ipxCircNeighRouterName':ipxCircNeighRouterName,'ipxCircNeighInternalNetNum':ipxCircNeighInternalNetNum,'ipxForwarding':ipxForwarding,'ipxDestTable':ipxDestTable,'ipxDestEntry':ipxDestEntry,_R:ipxDestSysInstance,_S:ipxDestNetNum,'ipxDestProtocol':ipxDestProtocol,'ipxDestTicks':ipxDestTicks,'ipxDestHopCount':ipxDestHopCount,'ipxDestNextHopCircIndex':ipxDestNextHopCircIndex,'ipxDestNextHopNICAddress':ipxDestNextHopNICAddress,'ipxDestNextHopNetNum':ipxDestNextHopNetNum,'ipxStaticRouteTable':ipxStaticRouteTable,'ipxStaticRouteEntry':ipxStaticRouteEntry,_T:ipxStaticRouteSysInstance,_U:ipxStaticRouteCircIndex,_V:ipxStaticRouteNetNum,'ipxStaticRouteExistState':ipxStaticRouteExistState,'ipxStaticRouteTicks':ipxStaticRouteTicks,'ipxStaticRouteHopCount':ipxStaticRouteHopCount,'ipxServices':ipxServices,'ipxServTable':ipxServTable,'ipxServEntry':ipxServEntry,_W:ipxServSysInstance,_X:ipxServType,_Y:ipxServName,'ipxServProtocol':ipxServProtocol,'ipxServNetNum':ipxServNetNum,'ipxServNode':ipxServNode,'ipxServSocket':ipxServSocket,'ipxServHopCount':ipxServHopCount,'ipxDestServTable':ipxDestServTable,'ipxDestServEntry':ipxDestServEntry,_Z:ipxDestServSysInstance,_a:ipxDestServNetNum,_b:ipxDestServNode,_c:ipxDestServSocket,_d:ipxDestServName,_e:ipxDestServType,'ipxDestServProtocol':ipxDestServProtocol,'ipxDestServHopCount':ipxDestServHopCount,'ipxStaticServTable':ipxStaticServTable,'ipxStaticServEntry':ipxStaticServEntry,_f:ipxStaticServSysInstance,_g:ipxStaticServCircIndex,_h:ipxStaticServName,_i:ipxStaticServType,'ipxStaticServExistState':ipxStaticServExistState,'ipxStaticServNetNum':ipxStaticServNetNum,'ipxStaticServNode':ipxStaticServNode,'ipxStaticServSocket':ipxStaticServSocket,'ipxStaticServHopCount':ipxStaticServHopCount,'ipxTraps':ipxTraps,'ipxTrapCircuitDown':ipxTrapCircuitDown,'ipxTrapCircuitUp':ipxTrapCircuitUp})