_K='not-accessible'
_J='xfcipLinkIndex'
_I='xfcipEntityId'
_H='compression ratio'
_G='fcipExtendedLinkIfIndex'
_F='Unsigned32'
_E='OctetString'
_D='milliseconds'
_C='BRCD-FCIP-EXT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bcsi,=mibBuilder.importSymbols('Brocade-REG-MIB','bcsi')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
fcipExtMIB=ModuleIdentity((1,3,6,1,4,1,1588,4))
if mibBuilder.loadTexts:fcipExtMIB.setRevisions(('2009-06-19 15:05','2013-04-26 11:33'))
class BrcdCompressionRatio(TextualConvention,Unsigned32):status=_A;displayHint='d'
_FcipExtendedLinkTable_Object=MibTable
fcipExtendedLinkTable=_FcipExtendedLinkTable_Object((1,3,6,1,4,1,1588,4,1))
if mibBuilder.loadTexts:fcipExtendedLinkTable.setStatus(_A)
_FcipExtendedLinkEntry_Object=MibTableRow
fcipExtendedLinkEntry=_FcipExtendedLinkEntry_Object((1,3,6,1,4,1,1588,4,1,1))
fcipExtendedLinkEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:fcipExtendedLinkEntry.setStatus(_A)
_FcipExtendedLinkIfIndex_Type=InterfaceIndex
_FcipExtendedLinkIfIndex_Object=MibTableColumn
fcipExtendedLinkIfIndex=_FcipExtendedLinkIfIndex_Object((1,3,6,1,4,1,1588,4,1,1,1),_FcipExtendedLinkIfIndex_Type())
fcipExtendedLinkIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fcipExtendedLinkIfIndex.setStatus(_A)
_FcipExtendedLinkTcpRetransmits_Type=Counter64
_FcipExtendedLinkTcpRetransmits_Object=MibTableColumn
fcipExtendedLinkTcpRetransmits=_FcipExtendedLinkTcpRetransmits_Object((1,3,6,1,4,1,1588,4,1,1,2),_FcipExtendedLinkTcpRetransmits_Type())
fcipExtendedLinkTcpRetransmits.setMaxAccess(_B)
if mibBuilder.loadTexts:fcipExtendedLinkTcpRetransmits.setStatus(_A)
_FcipExtendedLinkTcpDroppedPackets_Type=Counter64
_FcipExtendedLinkTcpDroppedPackets_Object=MibTableColumn
fcipExtendedLinkTcpDroppedPackets=_FcipExtendedLinkTcpDroppedPackets_Object((1,3,6,1,4,1,1588,4,1,1,3),_FcipExtendedLinkTcpDroppedPackets_Type())
fcipExtendedLinkTcpDroppedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fcipExtendedLinkTcpDroppedPackets.setStatus(_A)
_FcipExtendedLinkCompressionRatio_Type=BrcdCompressionRatio
_FcipExtendedLinkCompressionRatio_Object=MibTableColumn
fcipExtendedLinkCompressionRatio=_FcipExtendedLinkCompressionRatio_Object((1,3,6,1,4,1,1588,4,1,1,4),_FcipExtendedLinkCompressionRatio_Type())
fcipExtendedLinkCompressionRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:fcipExtendedLinkCompressionRatio.setStatus(_A)
if mibBuilder.loadTexts:fcipExtendedLinkCompressionRatio.setUnits(_H)
_FcipExtendedLinkTcpSmoothedRTT_Type=Integer32
_FcipExtendedLinkTcpSmoothedRTT_Object=MibTableColumn
fcipExtendedLinkTcpSmoothedRTT=_FcipExtendedLinkTcpSmoothedRTT_Object((1,3,6,1,4,1,1588,4,1,1,5),_FcipExtendedLinkTcpSmoothedRTT_Type())
fcipExtendedLinkTcpSmoothedRTT.setMaxAccess(_B)
if mibBuilder.loadTexts:fcipExtendedLinkTcpSmoothedRTT.setStatus(_A)
if mibBuilder.loadTexts:fcipExtendedLinkTcpSmoothedRTT.setUnits(_D)
_FcipExtendedLinkRawBytes_Type=Counter64
_FcipExtendedLinkRawBytes_Object=MibTableColumn
fcipExtendedLinkRawBytes=_FcipExtendedLinkRawBytes_Object((1,3,6,1,4,1,1588,4,1,1,6),_FcipExtendedLinkRawBytes_Type())
fcipExtendedLinkRawBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fcipExtendedLinkRawBytes.setStatus(_A)
_FcipExtendedLinkCompressedBytes_Type=Counter64
_FcipExtendedLinkCompressedBytes_Object=MibTableColumn
fcipExtendedLinkCompressedBytes=_FcipExtendedLinkCompressedBytes_Object((1,3,6,1,4,1,1588,4,1,1,7),_FcipExtendedLinkCompressedBytes_Type())
fcipExtendedLinkCompressedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fcipExtendedLinkCompressedBytes.setStatus(_A)
_FcipExtendedLinkConnectedCount_Type=Counter64
_FcipExtendedLinkConnectedCount_Object=MibTableColumn
fcipExtendedLinkConnectedCount=_FcipExtendedLinkConnectedCount_Object((1,3,6,1,4,1,1588,4,1,1,8),_FcipExtendedLinkConnectedCount_Type())
fcipExtendedLinkConnectedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fcipExtendedLinkConnectedCount.setStatus(_A)
_FcipExtendedLinkRtxRtxTO_Type=Counter64
_FcipExtendedLinkRtxRtxTO_Object=MibTableColumn
fcipExtendedLinkRtxRtxTO=_FcipExtendedLinkRtxRtxTO_Object((1,3,6,1,4,1,1588,4,1,1,9),_FcipExtendedLinkRtxRtxTO_Type())
fcipExtendedLinkRtxRtxTO.setMaxAccess(_B)
if mibBuilder.loadTexts:fcipExtendedLinkRtxRtxTO.setStatus(_A)
_FcipExtendedLinkRtxDupAck_Type=Counter64
_FcipExtendedLinkRtxDupAck_Object=MibTableColumn
fcipExtendedLinkRtxDupAck=_FcipExtendedLinkRtxDupAck_Object((1,3,6,1,4,1,1588,4,1,1,10),_FcipExtendedLinkRtxDupAck_Type())
fcipExtendedLinkRtxDupAck.setMaxAccess(_B)
if mibBuilder.loadTexts:fcipExtendedLinkRtxDupAck.setStatus(_A)
_FcipExtendedLinkDupAck_Type=Counter64
_FcipExtendedLinkDupAck_Object=MibTableColumn
fcipExtendedLinkDupAck=_FcipExtendedLinkDupAck_Object((1,3,6,1,4,1,1588,4,1,1,11),_FcipExtendedLinkDupAck_Type())
fcipExtendedLinkDupAck.setMaxAccess(_B)
if mibBuilder.loadTexts:fcipExtendedLinkDupAck.setStatus(_A)
_FcipExtendedLinkRtt_Type=Integer32
_FcipExtendedLinkRtt_Object=MibTableColumn
fcipExtendedLinkRtt=_FcipExtendedLinkRtt_Object((1,3,6,1,4,1,1588,4,1,1,12),_FcipExtendedLinkRtt_Type())
fcipExtendedLinkRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:fcipExtendedLinkRtt.setStatus(_A)
if mibBuilder.loadTexts:fcipExtendedLinkRtt.setUnits(_D)
_FcipExtendedLinkOoo_Type=Counter64
_FcipExtendedLinkOoo_Object=MibTableColumn
fcipExtendedLinkOoo=_FcipExtendedLinkOoo_Object((1,3,6,1,4,1,1588,4,1,1,13),_FcipExtendedLinkOoo_Type())
fcipExtendedLinkOoo.setMaxAccess(_B)
if mibBuilder.loadTexts:fcipExtendedLinkOoo.setStatus(_A)
_FcipExtendedLinkSlowStarts_Type=Counter64
_FcipExtendedLinkSlowStarts_Object=MibTableColumn
fcipExtendedLinkSlowStarts=_FcipExtendedLinkSlowStarts_Object((1,3,6,1,4,1,1588,4,1,1,14),_FcipExtendedLinkSlowStarts_Type())
fcipExtendedLinkSlowStarts.setMaxAccess(_B)
if mibBuilder.loadTexts:fcipExtendedLinkSlowStarts.setStatus(_A)
_FcipConnStatsTable_Object=MibTable
fcipConnStatsTable=_FcipConnStatsTable_Object((1,3,6,1,4,1,1588,4,2))
if mibBuilder.loadTexts:fcipConnStatsTable.setStatus(_A)
_FcipConnStatsEntry_Object=MibTableRow
fcipConnStatsEntry=_FcipConnStatsEntry_Object((1,3,6,1,4,1,1588,4,2,1))
fcipConnStatsEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:fcipConnStatsEntry.setStatus(_A)
class _XfcipEntityId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_XfcipEntityId_Type.__name__=_E
_XfcipEntityId_Object=MibTableColumn
xfcipEntityId=_XfcipEntityId_Object((1,3,6,1,4,1,1588,4,2,1,1),_XfcipEntityId_Type())
xfcipEntityId.setMaxAccess(_K)
if mibBuilder.loadTexts:xfcipEntityId.setStatus(_A)
_XfcipLinkIfIndex_Type=InterfaceIndex
_XfcipLinkIfIndex_Object=MibTableColumn
xfcipLinkIfIndex=_XfcipLinkIfIndex_Object((1,3,6,1,4,1,1588,4,2,1,2),_XfcipLinkIfIndex_Type())
xfcipLinkIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:xfcipLinkIfIndex.setStatus(_A)
class _XfcipLinkIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_XfcipLinkIndex_Type.__name__=_F
_XfcipLinkIndex_Object=MibTableColumn
xfcipLinkIndex=_XfcipLinkIndex_Object((1,3,6,1,4,1,1588,4,2,1,3),_XfcipLinkIndex_Type())
xfcipLinkIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:xfcipLinkIndex.setStatus(_A)
_XfcipExtendedLinkTcpRetransmits_Type=Counter64
_XfcipExtendedLinkTcpRetransmits_Object=MibTableColumn
xfcipExtendedLinkTcpRetransmits=_XfcipExtendedLinkTcpRetransmits_Object((1,3,6,1,4,1,1588,4,2,1,4),_XfcipExtendedLinkTcpRetransmits_Type())
xfcipExtendedLinkTcpRetransmits.setMaxAccess(_B)
if mibBuilder.loadTexts:xfcipExtendedLinkTcpRetransmits.setStatus(_A)
_XfcipExtendedLinkTcpDroppedPackets_Type=Counter64
_XfcipExtendedLinkTcpDroppedPackets_Object=MibTableColumn
xfcipExtendedLinkTcpDroppedPackets=_XfcipExtendedLinkTcpDroppedPackets_Object((1,3,6,1,4,1,1588,4,2,1,5),_XfcipExtendedLinkTcpDroppedPackets_Type())
xfcipExtendedLinkTcpDroppedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:xfcipExtendedLinkTcpDroppedPackets.setStatus(_A)
_XfcipExtendedLinkCompressionRatio_Type=BrcdCompressionRatio
_XfcipExtendedLinkCompressionRatio_Object=MibTableColumn
xfcipExtendedLinkCompressionRatio=_XfcipExtendedLinkCompressionRatio_Object((1,3,6,1,4,1,1588,4,2,1,6),_XfcipExtendedLinkCompressionRatio_Type())
xfcipExtendedLinkCompressionRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:xfcipExtendedLinkCompressionRatio.setStatus(_A)
if mibBuilder.loadTexts:xfcipExtendedLinkCompressionRatio.setUnits(_H)
_XfcipExtendedLinkTcpSmoothedRTT_Type=Integer32
_XfcipExtendedLinkTcpSmoothedRTT_Object=MibTableColumn
xfcipExtendedLinkTcpSmoothedRTT=_XfcipExtendedLinkTcpSmoothedRTT_Object((1,3,6,1,4,1,1588,4,2,1,7),_XfcipExtendedLinkTcpSmoothedRTT_Type())
xfcipExtendedLinkTcpSmoothedRTT.setMaxAccess(_B)
if mibBuilder.loadTexts:xfcipExtendedLinkTcpSmoothedRTT.setStatus(_A)
if mibBuilder.loadTexts:xfcipExtendedLinkTcpSmoothedRTT.setUnits(_D)
_XfcipExtendedLinkRawBytes_Type=Counter64
_XfcipExtendedLinkRawBytes_Object=MibTableColumn
xfcipExtendedLinkRawBytes=_XfcipExtendedLinkRawBytes_Object((1,3,6,1,4,1,1588,4,2,1,8),_XfcipExtendedLinkRawBytes_Type())
xfcipExtendedLinkRawBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:xfcipExtendedLinkRawBytes.setStatus(_A)
_XfcipExtendedLinkCompressedBytes_Type=Counter64
_XfcipExtendedLinkCompressedBytes_Object=MibTableColumn
xfcipExtendedLinkCompressedBytes=_XfcipExtendedLinkCompressedBytes_Object((1,3,6,1,4,1,1588,4,2,1,9),_XfcipExtendedLinkCompressedBytes_Type())
xfcipExtendedLinkCompressedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:xfcipExtendedLinkCompressedBytes.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'BrcdCompressionRatio':BrcdCompressionRatio,'fcipExtMIB':fcipExtMIB,'fcipExtendedLinkTable':fcipExtendedLinkTable,'fcipExtendedLinkEntry':fcipExtendedLinkEntry,_G:fcipExtendedLinkIfIndex,'fcipExtendedLinkTcpRetransmits':fcipExtendedLinkTcpRetransmits,'fcipExtendedLinkTcpDroppedPackets':fcipExtendedLinkTcpDroppedPackets,'fcipExtendedLinkCompressionRatio':fcipExtendedLinkCompressionRatio,'fcipExtendedLinkTcpSmoothedRTT':fcipExtendedLinkTcpSmoothedRTT,'fcipExtendedLinkRawBytes':fcipExtendedLinkRawBytes,'fcipExtendedLinkCompressedBytes':fcipExtendedLinkCompressedBytes,'fcipExtendedLinkConnectedCount':fcipExtendedLinkConnectedCount,'fcipExtendedLinkRtxRtxTO':fcipExtendedLinkRtxRtxTO,'fcipExtendedLinkRtxDupAck':fcipExtendedLinkRtxDupAck,'fcipExtendedLinkDupAck':fcipExtendedLinkDupAck,'fcipExtendedLinkRtt':fcipExtendedLinkRtt,'fcipExtendedLinkOoo':fcipExtendedLinkOoo,'fcipExtendedLinkSlowStarts':fcipExtendedLinkSlowStarts,'fcipConnStatsTable':fcipConnStatsTable,'fcipConnStatsEntry':fcipConnStatsEntry,_I:xfcipEntityId,'xfcipLinkIfIndex':xfcipLinkIfIndex,_J:xfcipLinkIndex,'xfcipExtendedLinkTcpRetransmits':xfcipExtendedLinkTcpRetransmits,'xfcipExtendedLinkTcpDroppedPackets':xfcipExtendedLinkTcpDroppedPackets,'xfcipExtendedLinkCompressionRatio':xfcipExtendedLinkCompressionRatio,'xfcipExtendedLinkTcpSmoothedRTT':xfcipExtendedLinkTcpSmoothedRTT,'xfcipExtendedLinkRawBytes':xfcipExtendedLinkRawBytes,'xfcipExtendedLinkCompressedBytes':xfcipExtendedLinkCompressedBytes})