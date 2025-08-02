_I='nsIdsAttkMonIfIdx'
_H='nsIdsProtectThreshZoneIdx'
_G='nsIdsProtectZoneIdx'
_F='NETSCREEN-IDS-MIB'
_E='enabled'
_D='disable'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenIDS,=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenIDS')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nsIdsProtect=ModuleIdentity((1,3,6,1,4,1,3224,3,1))
if mibBuilder.loadTexts:nsIdsProtect.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2002-04-26 00:00','2001-09-28 00:00','2001-01-08 00:00'))
_NsIdsProtectSetTable_Object=MibTable
nsIdsProtectSetTable=_NsIdsProtectSetTable_Object((1,3,6,1,4,1,3224,3,1,1))
if mibBuilder.loadTexts:nsIdsProtectSetTable.setStatus(_A)
_NsIdsProtectSetEntry_Object=MibTableRow
nsIdsProtectSetEntry=_NsIdsProtectSetEntry_Object((1,3,6,1,4,1,3224,3,1,1,1))
nsIdsProtectSetEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:nsIdsProtectSetEntry.setStatus(_A)
class _NsIdsProtectZoneIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsIdsProtectZoneIdx_Type.__name__=_C
_NsIdsProtectZoneIdx_Object=MibTableColumn
nsIdsProtectZoneIdx=_NsIdsProtectZoneIdx_Object((1,3,6,1,4,1,3224,3,1,1,1,1),_NsIdsProtectZoneIdx_Type())
nsIdsProtectZoneIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsProtectZoneIdx.setStatus(_A)
class _NsIdsDetectPingOfDeath_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectPingOfDeath_Type.__name__=_C
_NsIdsDetectPingOfDeath_Object=MibTableColumn
nsIdsDetectPingOfDeath=_NsIdsDetectPingOfDeath_Object((1,3,6,1,4,1,3224,3,1,1,1,2),_NsIdsDetectPingOfDeath_Type())
nsIdsDetectPingOfDeath.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectPingOfDeath.setStatus(_A)
class _NsIdsDetectTearDrop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectTearDrop_Type.__name__=_C
_NsIdsDetectTearDrop_Object=MibTableColumn
nsIdsDetectTearDrop=_NsIdsDetectTearDrop_Object((1,3,6,1,4,1,3224,3,1,1,1,3),_NsIdsDetectTearDrop_Type())
nsIdsDetectTearDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectTearDrop.setStatus(_A)
class _NsIdsDetectWinNuke_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectWinNuke_Type.__name__=_C
_NsIdsDetectWinNuke_Object=MibTableColumn
nsIdsDetectWinNuke=_NsIdsDetectWinNuke_Object((1,3,6,1,4,1,3224,3,1,1,1,4),_NsIdsDetectWinNuke_Type())
nsIdsDetectWinNuke.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectWinNuke.setStatus(_A)
class _NsIdsFilterIpSrcRoute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsFilterIpSrcRoute_Type.__name__=_C
_NsIdsFilterIpSrcRoute_Object=MibTableColumn
nsIdsFilterIpSrcRoute=_NsIdsFilterIpSrcRoute_Object((1,3,6,1,4,1,3224,3,1,1,1,5),_NsIdsFilterIpSrcRoute_Type())
nsIdsFilterIpSrcRoute.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsFilterIpSrcRoute.setStatus(_A)
class _NsIdsDetectPortScan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectPortScan_Type.__name__=_C
_NsIdsDetectPortScan_Object=MibTableColumn
nsIdsDetectPortScan=_NsIdsDetectPortScan_Object((1,3,6,1,4,1,3224,3,1,1,1,6),_NsIdsDetectPortScan_Type())
nsIdsDetectPortScan.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectPortScan.setStatus(_A)
class _NsIdsDetectAddrSweep_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectAddrSweep_Type.__name__=_C
_NsIdsDetectAddrSweep_Object=MibTableColumn
nsIdsDetectAddrSweep=_NsIdsDetectAddrSweep_Object((1,3,6,1,4,1,3224,3,1,1,1,7),_NsIdsDetectAddrSweep_Type())
nsIdsDetectAddrSweep.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectAddrSweep.setStatus(_A)
class _NsIdsDetectLand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectLand_Type.__name__=_C
_NsIdsDetectLand_Object=MibTableColumn
nsIdsDetectLand=_NsIdsDetectLand_Object((1,3,6,1,4,1,3224,3,1,1,1,8),_NsIdsDetectLand_Type())
nsIdsDetectLand.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectLand.setStatus(_A)
class _NsIdsBlockComponent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsBlockComponent_Type.__name__=_C
_NsIdsBlockComponent_Object=MibTableColumn
nsIdsBlockComponent=_NsIdsBlockComponent_Object((1,3,6,1,4,1,3224,3,1,1,1,9),_NsIdsBlockComponent_Type())
nsIdsBlockComponent.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsBlockComponent.setStatus(_A)
class _NsIdsDetectIpSpoof_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectIpSpoof_Type.__name__=_C
_NsIdsDetectIpSpoof_Object=MibTableColumn
nsIdsDetectIpSpoof=_NsIdsDetectIpSpoof_Object((1,3,6,1,4,1,3224,3,1,1,1,10),_NsIdsDetectIpSpoof_Type())
nsIdsDetectIpSpoof.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectIpSpoof.setStatus(_A)
class _NsIdsDetectSyn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectSyn_Type.__name__=_C
_NsIdsDetectSyn_Object=MibTableColumn
nsIdsDetectSyn=_NsIdsDetectSyn_Object((1,3,6,1,4,1,3224,3,1,1,1,11),_NsIdsDetectSyn_Type())
nsIdsDetectSyn.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectSyn.setStatus(_A)
class _NsIdsDetectIcmpFlood_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectIcmpFlood_Type.__name__=_C
_NsIdsDetectIcmpFlood_Object=MibTableColumn
nsIdsDetectIcmpFlood=_NsIdsDetectIcmpFlood_Object((1,3,6,1,4,1,3224,3,1,1,1,12),_NsIdsDetectIcmpFlood_Type())
nsIdsDetectIcmpFlood.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectIcmpFlood.setStatus(_A)
class _NsIdsDetectUdpFlood_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectUdpFlood_Type.__name__=_C
_NsIdsDetectUdpFlood_Object=MibTableColumn
nsIdsDetectUdpFlood=_NsIdsDetectUdpFlood_Object((1,3,6,1,4,1,3224,3,1,1,1,13),_NsIdsDetectUdpFlood_Type())
nsIdsDetectUdpFlood.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectUdpFlood.setStatus(_A)
class _NsIdsDetectSynFrag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectSynFrag_Type.__name__=_C
_NsIdsDetectSynFrag_Object=MibTableColumn
nsIdsDetectSynFrag=_NsIdsDetectSynFrag_Object((1,3,6,1,4,1,3224,3,1,1,1,14),_NsIdsDetectSynFrag_Type())
nsIdsDetectSynFrag.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectSynFrag.setStatus(_A)
class _NsIdsDetectTcpNoFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectTcpNoFlag_Type.__name__=_C
_NsIdsDetectTcpNoFlag_Object=MibTableColumn
nsIdsDetectTcpNoFlag=_NsIdsDetectTcpNoFlag_Object((1,3,6,1,4,1,3224,3,1,1,1,15),_NsIdsDetectTcpNoFlag_Type())
nsIdsDetectTcpNoFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectTcpNoFlag.setStatus(_A)
class _NsIdsDetectIpUnknownProt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectIpUnknownProt_Type.__name__=_C
_NsIdsDetectIpUnknownProt_Object=MibTableColumn
nsIdsDetectIpUnknownProt=_NsIdsDetectIpUnknownProt_Object((1,3,6,1,4,1,3224,3,1,1,1,16),_NsIdsDetectIpUnknownProt_Type())
nsIdsDetectIpUnknownProt.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectIpUnknownProt.setStatus(_A)
class _NsIdsDetectIpOptBad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectIpOptBad_Type.__name__=_C
_NsIdsDetectIpOptBad_Object=MibTableColumn
nsIdsDetectIpOptBad=_NsIdsDetectIpOptBad_Object((1,3,6,1,4,1,3224,3,1,1,1,17),_NsIdsDetectIpOptBad_Type())
nsIdsDetectIpOptBad.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectIpOptBad.setStatus(_A)
class _NsIdsDetectIpOptRecord_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectIpOptRecord_Type.__name__=_C
_NsIdsDetectIpOptRecord_Object=MibTableColumn
nsIdsDetectIpOptRecord=_NsIdsDetectIpOptRecord_Object((1,3,6,1,4,1,3224,3,1,1,1,18),_NsIdsDetectIpOptRecord_Type())
nsIdsDetectIpOptRecord.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectIpOptRecord.setStatus(_A)
class _NsIdsDetectIpOptTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectIpOptTimestamp_Type.__name__=_C
_NsIdsDetectIpOptTimestamp_Object=MibTableColumn
nsIdsDetectIpOptTimestamp=_NsIdsDetectIpOptTimestamp_Object((1,3,6,1,4,1,3224,3,1,1,1,19),_NsIdsDetectIpOptTimestamp_Type())
nsIdsDetectIpOptTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectIpOptTimestamp.setStatus(_A)
class _NsIdsDetectIpOptSCHT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectIpOptSCHT_Type.__name__=_C
_NsIdsDetectIpOptSCHT_Object=MibTableColumn
nsIdsDetectIpOptSCHT=_NsIdsDetectIpOptSCHT_Object((1,3,6,1,4,1,3224,3,1,1,1,20),_NsIdsDetectIpOptSCHT_Type())
nsIdsDetectIpOptSCHT.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectIpOptSCHT.setStatus(_A)
class _NsIdsDetectIpOptLSR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectIpOptLSR_Type.__name__=_C
_NsIdsDetectIpOptLSR_Object=MibTableColumn
nsIdsDetectIpOptLSR=_NsIdsDetectIpOptLSR_Object((1,3,6,1,4,1,3224,3,1,1,1,21),_NsIdsDetectIpOptLSR_Type())
nsIdsDetectIpOptLSR.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectIpOptLSR.setStatus(_A)
class _NsIdsDetectIpOptSSR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectIpOptSSR_Type.__name__=_C
_NsIdsDetectIpOptSSR_Object=MibTableColumn
nsIdsDetectIpOptSSR=_NsIdsDetectIpOptSSR_Object((1,3,6,1,4,1,3224,3,1,1,1,22),_NsIdsDetectIpOptSSR_Type())
nsIdsDetectIpOptSSR.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectIpOptSSR.setStatus(_A)
class _NsIdsDetectIpOptStream_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectIpOptStream_Type.__name__=_C
_NsIdsDetectIpOptStream_Object=MibTableColumn
nsIdsDetectIpOptStream=_NsIdsDetectIpOptStream_Object((1,3,6,1,4,1,3224,3,1,1,1,23),_NsIdsDetectIpOptStream_Type())
nsIdsDetectIpOptStream.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectIpOptStream.setStatus(_A)
class _NsIdsDetectIcmpFrag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectIcmpFrag_Type.__name__=_C
_NsIdsDetectIcmpFrag_Object=MibTableColumn
nsIdsDetectIcmpFrag=_NsIdsDetectIcmpFrag_Object((1,3,6,1,4,1,3224,3,1,1,1,24),_NsIdsDetectIcmpFrag_Type())
nsIdsDetectIcmpFrag.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectIcmpFrag.setStatus(_A)
class _NsIdsDetectIcmpLarge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectIcmpLarge_Type.__name__=_C
_NsIdsDetectIcmpLarge_Object=MibTableColumn
nsIdsDetectIcmpLarge=_NsIdsDetectIcmpLarge_Object((1,3,6,1,4,1,3224,3,1,1,1,25),_NsIdsDetectIcmpLarge_Type())
nsIdsDetectIcmpLarge.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectIcmpLarge.setStatus(_A)
class _NsIdsDetectTcpSynFin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectTcpSynFin_Type.__name__=_C
_NsIdsDetectTcpSynFin_Object=MibTableColumn
nsIdsDetectTcpSynFin=_NsIdsDetectTcpSynFin_Object((1,3,6,1,4,1,3224,3,1,1,1,26),_NsIdsDetectTcpSynFin_Type())
nsIdsDetectTcpSynFin.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectTcpSynFin.setStatus(_A)
class _NsIdsDetectTcpFinNoAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectTcpFinNoAck_Type.__name__=_C
_NsIdsDetectTcpFinNoAck_Object=MibTableColumn
nsIdsDetectTcpFinNoAck=_NsIdsDetectTcpFinNoAck_Object((1,3,6,1,4,1,3224,3,1,1,1,27),_NsIdsDetectTcpFinNoAck_Type())
nsIdsDetectTcpFinNoAck.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectTcpFinNoAck.setStatus(_A)
class _NsIdsHttpMalUrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsHttpMalUrl_Type.__name__=_C
_NsIdsHttpMalUrl_Object=MibTableColumn
nsIdsHttpMalUrl=_NsIdsHttpMalUrl_Object((1,3,6,1,4,1,3224,3,1,1,1,28),_NsIdsHttpMalUrl_Type())
nsIdsHttpMalUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsHttpMalUrl.setStatus(_A)
class _NsIdsSessMalNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsSessMalNum_Type.__name__=_C
_NsIdsSessMalNum_Object=MibTableColumn
nsIdsSessMalNum=_NsIdsSessMalNum_Object((1,3,6,1,4,1,3224,3,1,1,1,29),_NsIdsSessMalNum_Type())
nsIdsSessMalNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsSessMalNum.setStatus(_A)
class _NsIdsDetectSynAckAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectSynAckAck_Type.__name__=_C
_NsIdsDetectSynAckAck_Object=MibTableColumn
nsIdsDetectSynAckAck=_NsIdsDetectSynAckAck_Object((1,3,6,1,4,1,3224,3,1,1,1,30),_NsIdsDetectSynAckAck_Type())
nsIdsDetectSynAckAck.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectSynAckAck.setStatus(_A)
class _NsIdsDetectIpFrag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIdsDetectIpFrag_Type.__name__=_C
_NsIdsDetectIpFrag_Object=MibTableColumn
nsIdsDetectIpFrag=_NsIdsDetectIpFrag_Object((1,3,6,1,4,1,3224,3,1,1,1,31),_NsIdsDetectIpFrag_Type())
nsIdsDetectIpFrag.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsDetectIpFrag.setStatus(_A)
_NsIdsProtectThreshTable_Object=MibTable
nsIdsProtectThreshTable=_NsIdsProtectThreshTable_Object((1,3,6,1,4,1,3224,3,1,2))
if mibBuilder.loadTexts:nsIdsProtectThreshTable.setStatus(_A)
_NsIdsProtectThreshEntry_Object=MibTableRow
nsIdsProtectThreshEntry=_NsIdsProtectThreshEntry_Object((1,3,6,1,4,1,3224,3,1,2,1))
nsIdsProtectThreshEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:nsIdsProtectThreshEntry.setStatus(_A)
class _NsIdsProtectThreshZoneIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsIdsProtectThreshZoneIdx_Type.__name__=_C
_NsIdsProtectThreshZoneIdx_Object=MibTableColumn
nsIdsProtectThreshZoneIdx=_NsIdsProtectThreshZoneIdx_Object((1,3,6,1,4,1,3224,3,1,2,1,1),_NsIdsProtectThreshZoneIdx_Type())
nsIdsProtectThreshZoneIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsProtectThreshZoneIdx.setStatus(_A)
_NsIdsSynAttackThresh_Type=Integer32
_NsIdsSynAttackThresh_Object=MibTableColumn
nsIdsSynAttackThresh=_NsIdsSynAttackThresh_Object((1,3,6,1,4,1,3224,3,1,2,1,2),_NsIdsSynAttackThresh_Type())
nsIdsSynAttackThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsSynAttackThresh.setStatus(_A)
_NsIdsSynAttackTimeout_Type=Integer32
_NsIdsSynAttackTimeout_Object=MibTableColumn
nsIdsSynAttackTimeout=_NsIdsSynAttackTimeout_Object((1,3,6,1,4,1,3224,3,1,2,1,3),_NsIdsSynAttackTimeout_Type())
nsIdsSynAttackTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsSynAttackTimeout.setStatus(_A)
_NsIdsSynAttackAlmTh_Type=Integer32
_NsIdsSynAttackAlmTh_Object=MibTableColumn
nsIdsSynAttackAlmTh=_NsIdsSynAttackAlmTh_Object((1,3,6,1,4,1,3224,3,1,2,1,4),_NsIdsSynAttackAlmTh_Type())
nsIdsSynAttackAlmTh.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsSynAttackAlmTh.setStatus(_A)
_NsIdsSynAttackQueSize_Type=Integer32
_NsIdsSynAttackQueSize_Object=MibTableColumn
nsIdsSynAttackQueSize=_NsIdsSynAttackQueSize_Object((1,3,6,1,4,1,3224,3,1,2,1,5),_NsIdsSynAttackQueSize_Type())
nsIdsSynAttackQueSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsSynAttackQueSize.setStatus(_A)
_NsIdsSynAttackAgeTime_Type=Integer32
_NsIdsSynAttackAgeTime_Object=MibTableColumn
nsIdsSynAttackAgeTime=_NsIdsSynAttackAgeTime_Object((1,3,6,1,4,1,3224,3,1,2,1,6),_NsIdsSynAttackAgeTime_Type())
nsIdsSynAttackAgeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsSynAttackAgeTime.setStatus(_A)
_NsIdsIcmpFloodThresh_Type=Integer32
_NsIdsIcmpFloodThresh_Object=MibTableColumn
nsIdsIcmpFloodThresh=_NsIdsIcmpFloodThresh_Object((1,3,6,1,4,1,3224,3,1,2,1,7),_NsIdsIcmpFloodThresh_Type())
nsIdsIcmpFloodThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsIcmpFloodThresh.setStatus(_A)
_NsIdsUdpFloodThresh_Type=Integer32
_NsIdsUdpFloodThresh_Object=MibTableColumn
nsIdsUdpFloodThresh=_NsIdsUdpFloodThresh_Object((1,3,6,1,4,1,3224,3,1,2,1,8),_NsIdsUdpFloodThresh_Type())
nsIdsUdpFloodThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsUdpFloodThresh.setStatus(_A)
_NsIdsPortScanThresh_Type=Integer32
_NsIdsPortScanThresh_Object=MibTableColumn
nsIdsPortScanThresh=_NsIdsPortScanThresh_Object((1,3,6,1,4,1,3224,3,1,2,1,9),_NsIdsPortScanThresh_Type())
nsIdsPortScanThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsPortScanThresh.setStatus(_A)
_NsIdsIpSweepThresh_Type=Integer32
_NsIdsIpSweepThresh_Object=MibTableColumn
nsIdsIpSweepThresh=_NsIdsIpSweepThresh_Object((1,3,6,1,4,1,3224,3,1,2,1,10),_NsIdsIpSweepThresh_Type())
nsIdsIpSweepThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsIpSweepThresh.setStatus(_A)
_NsIdsSynAckAckThres_Type=Integer32
_NsIdsSynAckAckThres_Object=MibTableColumn
nsIdsSynAckAckThres=_NsIdsSynAckAckThres_Object((1,3,6,1,4,1,3224,3,1,2,1,11),_NsIdsSynAckAckThres_Type())
nsIdsSynAckAckThres.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsSynAckAckThres.setStatus(_A)
_NsIdsAttkMonTable_Object=MibTable
nsIdsAttkMonTable=_NsIdsAttkMonTable_Object((1,3,6,1,4,1,3224,3,2))
if mibBuilder.loadTexts:nsIdsAttkMonTable.setStatus(_A)
_NsIdsAttkMonEntry_Object=MibTableRow
nsIdsAttkMonEntry=_NsIdsAttkMonEntry_Object((1,3,6,1,4,1,3224,3,2,1))
nsIdsAttkMonEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:nsIdsAttkMonEntry.setStatus(_A)
class _NsIdsAttkMonIfIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsIdsAttkMonIfIdx_Type.__name__=_C
_NsIdsAttkMonIfIdx_Object=MibTableColumn
nsIdsAttkMonIfIdx=_NsIdsAttkMonIfIdx_Object((1,3,6,1,4,1,3224,3,2,1,1),_NsIdsAttkMonIfIdx_Type())
nsIdsAttkMonIfIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsAttkMonIfIdx.setStatus(_A)
_NsIdsAttkMonVsys_Type=Integer32
_NsIdsAttkMonVsys_Object=MibTableColumn
nsIdsAttkMonVsys=_NsIdsAttkMonVsys_Object((1,3,6,1,4,1,3224,3,2,1,2),_NsIdsAttkMonVsys_Type())
nsIdsAttkMonVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsAttkMonVsys.setStatus(_A)
_NsIdsAttkMonSynAttk_Type=Counter32
_NsIdsAttkMonSynAttk_Object=MibTableColumn
nsIdsAttkMonSynAttk=_NsIdsAttkMonSynAttk_Object((1,3,6,1,4,1,3224,3,2,1,3),_NsIdsAttkMonSynAttk_Type())
nsIdsAttkMonSynAttk.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsAttkMonSynAttk.setStatus(_A)
_NsIdsAttkMonTearDrop_Type=Counter32
_NsIdsAttkMonTearDrop_Object=MibTableColumn
nsIdsAttkMonTearDrop=_NsIdsAttkMonTearDrop_Object((1,3,6,1,4,1,3224,3,2,1,4),_NsIdsAttkMonTearDrop_Type())
nsIdsAttkMonTearDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsAttkMonTearDrop.setStatus(_A)
_NsIdsAttkMonSrcRoute_Type=Counter32
_NsIdsAttkMonSrcRoute_Object=MibTableColumn
nsIdsAttkMonSrcRoute=_NsIdsAttkMonSrcRoute_Object((1,3,6,1,4,1,3224,3,2,1,5),_NsIdsAttkMonSrcRoute_Type())
nsIdsAttkMonSrcRoute.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsAttkMonSrcRoute.setStatus(_A)
_NsIdsAttkMonPingDeath_Type=Counter32
_NsIdsAttkMonPingDeath_Object=MibTableColumn
nsIdsAttkMonPingDeath=_NsIdsAttkMonPingDeath_Object((1,3,6,1,4,1,3224,3,2,1,6),_NsIdsAttkMonPingDeath_Type())
nsIdsAttkMonPingDeath.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsAttkMonPingDeath.setStatus(_A)
_NsIdsAttkMonAddrSpoof_Type=Counter32
_NsIdsAttkMonAddrSpoof_Object=MibTableColumn
nsIdsAttkMonAddrSpoof=_NsIdsAttkMonAddrSpoof_Object((1,3,6,1,4,1,3224,3,2,1,7),_NsIdsAttkMonAddrSpoof_Type())
nsIdsAttkMonAddrSpoof.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsAttkMonAddrSpoof.setStatus(_A)
_NsIdsAttkMonLand_Type=Counter32
_NsIdsAttkMonLand_Object=MibTableColumn
nsIdsAttkMonLand=_NsIdsAttkMonLand_Object((1,3,6,1,4,1,3224,3,2,1,8),_NsIdsAttkMonLand_Type())
nsIdsAttkMonLand.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsAttkMonLand.setStatus(_A)
_NsIdsAttkMonIcmpFlood_Type=Counter32
_NsIdsAttkMonIcmpFlood_Object=MibTableColumn
nsIdsAttkMonIcmpFlood=_NsIdsAttkMonIcmpFlood_Object((1,3,6,1,4,1,3224,3,2,1,9),_NsIdsAttkMonIcmpFlood_Type())
nsIdsAttkMonIcmpFlood.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsAttkMonIcmpFlood.setStatus(_A)
_NsIdsAttkMonUdpFlood_Type=Counter32
_NsIdsAttkMonUdpFlood_Object=MibTableColumn
nsIdsAttkMonUdpFlood=_NsIdsAttkMonUdpFlood_Object((1,3,6,1,4,1,3224,3,2,1,10),_NsIdsAttkMonUdpFlood_Type())
nsIdsAttkMonUdpFlood.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsAttkMonUdpFlood.setStatus(_A)
_NsIdsAttkMonWinnuke_Type=Counter32
_NsIdsAttkMonWinnuke_Object=MibTableColumn
nsIdsAttkMonWinnuke=_NsIdsAttkMonWinnuke_Object((1,3,6,1,4,1,3224,3,2,1,11),_NsIdsAttkMonWinnuke_Type())
nsIdsAttkMonWinnuke.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsAttkMonWinnuke.setStatus(_A)
_NsIdsAttkMonPortScan_Type=Counter32
_NsIdsAttkMonPortScan_Object=MibTableColumn
nsIdsAttkMonPortScan=_NsIdsAttkMonPortScan_Object((1,3,6,1,4,1,3224,3,2,1,12),_NsIdsAttkMonPortScan_Type())
nsIdsAttkMonPortScan.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsAttkMonPortScan.setStatus(_A)
_NsIdsAttkMonIpSweep_Type=Counter32
_NsIdsAttkMonIpSweep_Object=MibTableColumn
nsIdsAttkMonIpSweep=_NsIdsAttkMonIpSweep_Object((1,3,6,1,4,1,3224,3,2,1,13),_NsIdsAttkMonIpSweep_Type())
nsIdsAttkMonIpSweep.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsAttkMonIpSweep.setStatus(_A)
_NsAttkMonSynFrag_Type=Counter32
_NsAttkMonSynFrag_Object=MibTableColumn
nsAttkMonSynFrag=_NsAttkMonSynFrag_Object((1,3,6,1,4,1,3224,3,2,1,14),_NsAttkMonSynFrag_Type())
nsAttkMonSynFrag.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAttkMonSynFrag.setStatus(_A)
_NsAttkMonTcpNoFlag_Type=Counter32
_NsAttkMonTcpNoFlag_Object=MibTableColumn
nsAttkMonTcpNoFlag=_NsAttkMonTcpNoFlag_Object((1,3,6,1,4,1,3224,3,2,1,15),_NsAttkMonTcpNoFlag_Type())
nsAttkMonTcpNoFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAttkMonTcpNoFlag.setStatus(_A)
_NsAttkMonIpUnknownProt_Type=Counter32
_NsAttkMonIpUnknownProt_Object=MibTableColumn
nsAttkMonIpUnknownProt=_NsAttkMonIpUnknownProt_Object((1,3,6,1,4,1,3224,3,2,1,16),_NsAttkMonIpUnknownProt_Type())
nsAttkMonIpUnknownProt.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAttkMonIpUnknownProt.setStatus(_A)
_NsAttkMonIpOptBad_Type=Counter32
_NsAttkMonIpOptBad_Object=MibTableColumn
nsAttkMonIpOptBad=_NsAttkMonIpOptBad_Object((1,3,6,1,4,1,3224,3,2,1,17),_NsAttkMonIpOptBad_Type())
nsAttkMonIpOptBad.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAttkMonIpOptBad.setStatus(_A)
_NsAttkMonIpOptRecord_Type=Counter32
_NsAttkMonIpOptRecord_Object=MibTableColumn
nsAttkMonIpOptRecord=_NsAttkMonIpOptRecord_Object((1,3,6,1,4,1,3224,3,2,1,18),_NsAttkMonIpOptRecord_Type())
nsAttkMonIpOptRecord.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAttkMonIpOptRecord.setStatus(_A)
_NsAttkMonIpOptTimestamp_Type=Counter32
_NsAttkMonIpOptTimestamp_Object=MibTableColumn
nsAttkMonIpOptTimestamp=_NsAttkMonIpOptTimestamp_Object((1,3,6,1,4,1,3224,3,2,1,19),_NsAttkMonIpOptTimestamp_Type())
nsAttkMonIpOptTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAttkMonIpOptTimestamp.setStatus(_A)
_NsAttkMonIpOptSCHT_Type=Counter32
_NsAttkMonIpOptSCHT_Object=MibTableColumn
nsAttkMonIpOptSCHT=_NsAttkMonIpOptSCHT_Object((1,3,6,1,4,1,3224,3,2,1,20),_NsAttkMonIpOptSCHT_Type())
nsAttkMonIpOptSCHT.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAttkMonIpOptSCHT.setStatus(_A)
_NsAttkMonIpOptLSR_Type=Counter32
_NsAttkMonIpOptLSR_Object=MibTableColumn
nsAttkMonIpOptLSR=_NsAttkMonIpOptLSR_Object((1,3,6,1,4,1,3224,3,2,1,21),_NsAttkMonIpOptLSR_Type())
nsAttkMonIpOptLSR.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAttkMonIpOptLSR.setStatus(_A)
_NsAttkMonIpOptSSR_Type=Counter32
_NsAttkMonIpOptSSR_Object=MibTableColumn
nsAttkMonIpOptSSR=_NsAttkMonIpOptSSR_Object((1,3,6,1,4,1,3224,3,2,1,22),_NsAttkMonIpOptSSR_Type())
nsAttkMonIpOptSSR.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAttkMonIpOptSSR.setStatus(_A)
_NsAttkMonIpOptStream_Type=Counter32
_NsAttkMonIpOptStream_Object=MibTableColumn
nsAttkMonIpOptStream=_NsAttkMonIpOptStream_Object((1,3,6,1,4,1,3224,3,2,1,23),_NsAttkMonIpOptStream_Type())
nsAttkMonIpOptStream.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAttkMonIpOptStream.setStatus(_A)
_NsAttkMonIcmpFrag_Type=Counter32
_NsAttkMonIcmpFrag_Object=MibTableColumn
nsAttkMonIcmpFrag=_NsAttkMonIcmpFrag_Object((1,3,6,1,4,1,3224,3,2,1,24),_NsAttkMonIcmpFrag_Type())
nsAttkMonIcmpFrag.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAttkMonIcmpFrag.setStatus(_A)
_NsAttkMonIcmpLarge_Type=Counter32
_NsAttkMonIcmpLarge_Object=MibTableColumn
nsAttkMonIcmpLarge=_NsAttkMonIcmpLarge_Object((1,3,6,1,4,1,3224,3,2,1,25),_NsAttkMonIcmpLarge_Type())
nsAttkMonIcmpLarge.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAttkMonIcmpLarge.setStatus(_A)
_NsAttkMonTcpSynFin_Type=Counter32
_NsAttkMonTcpSynFin_Object=MibTableColumn
nsAttkMonTcpSynFin=_NsAttkMonTcpSynFin_Object((1,3,6,1,4,1,3224,3,2,1,26),_NsAttkMonTcpSynFin_Type())
nsAttkMonTcpSynFin.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAttkMonTcpSynFin.setStatus(_A)
_NsAttkMonTcpFinNoAck_Type=Counter32
_NsAttkMonTcpFinNoAck_Object=MibTableColumn
nsAttkMonTcpFinNoAck=_NsAttkMonTcpFinNoAck_Object((1,3,6,1,4,1,3224,3,2,1,27),_NsAttkMonTcpFinNoAck_Type())
nsAttkMonTcpFinNoAck.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAttkMonTcpFinNoAck.setStatus(_A)
_NsAttkMonHttpMalUrl_Type=Counter32
_NsAttkMonHttpMalUrl_Object=MibTableColumn
nsAttkMonHttpMalUrl=_NsAttkMonHttpMalUrl_Object((1,3,6,1,4,1,3224,3,2,1,28),_NsAttkMonHttpMalUrl_Type())
nsAttkMonHttpMalUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAttkMonHttpMalUrl.setStatus(_A)
_NsAttkMonSessMalNum_Type=Counter32
_NsAttkMonSessMalNum_Object=MibTableColumn
nsAttkMonSessMalNum=_NsAttkMonSessMalNum_Object((1,3,6,1,4,1,3224,3,2,1,29),_NsAttkMonSessMalNum_Type())
nsAttkMonSessMalNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAttkMonSessMalNum.setStatus(_A)
_NsAttkMonSynAckAck_Type=Counter32
_NsAttkMonSynAckAck_Object=MibTableColumn
nsAttkMonSynAckAck=_NsAttkMonSynAckAck_Object((1,3,6,1,4,1,3224,3,2,1,30),_NsAttkMonSynAckAck_Type())
nsAttkMonSynAckAck.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAttkMonSynAckAck.setStatus(_A)
_NsAttkMonIpFrag_Type=Counter32
_NsAttkMonIpFrag_Object=MibTableColumn
nsAttkMonIpFrag=_NsAttkMonIpFrag_Object((1,3,6,1,4,1,3224,3,2,1,31),_NsAttkMonIpFrag_Type())
nsAttkMonIpFrag.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAttkMonIpFrag.setStatus(_A)
class _NsIdsAttkMonIfInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsIdsAttkMonIfInfo_Type.__name__=_C
_NsIdsAttkMonIfInfo_Object=MibTableColumn
nsIdsAttkMonIfInfo=_NsIdsAttkMonIfInfo_Object((1,3,6,1,4,1,3224,3,2,1,32),_NsIdsAttkMonIfInfo_Type())
nsIdsAttkMonIfInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIdsAttkMonIfInfo.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'nsIdsProtect':nsIdsProtect,'nsIdsProtectSetTable':nsIdsProtectSetTable,'nsIdsProtectSetEntry':nsIdsProtectSetEntry,_G:nsIdsProtectZoneIdx,'nsIdsDetectPingOfDeath':nsIdsDetectPingOfDeath,'nsIdsDetectTearDrop':nsIdsDetectTearDrop,'nsIdsDetectWinNuke':nsIdsDetectWinNuke,'nsIdsFilterIpSrcRoute':nsIdsFilterIpSrcRoute,'nsIdsDetectPortScan':nsIdsDetectPortScan,'nsIdsDetectAddrSweep':nsIdsDetectAddrSweep,'nsIdsDetectLand':nsIdsDetectLand,'nsIdsBlockComponent':nsIdsBlockComponent,'nsIdsDetectIpSpoof':nsIdsDetectIpSpoof,'nsIdsDetectSyn':nsIdsDetectSyn,'nsIdsDetectIcmpFlood':nsIdsDetectIcmpFlood,'nsIdsDetectUdpFlood':nsIdsDetectUdpFlood,'nsIdsDetectSynFrag':nsIdsDetectSynFrag,'nsIdsDetectTcpNoFlag':nsIdsDetectTcpNoFlag,'nsIdsDetectIpUnknownProt':nsIdsDetectIpUnknownProt,'nsIdsDetectIpOptBad':nsIdsDetectIpOptBad,'nsIdsDetectIpOptRecord':nsIdsDetectIpOptRecord,'nsIdsDetectIpOptTimestamp':nsIdsDetectIpOptTimestamp,'nsIdsDetectIpOptSCHT':nsIdsDetectIpOptSCHT,'nsIdsDetectIpOptLSR':nsIdsDetectIpOptLSR,'nsIdsDetectIpOptSSR':nsIdsDetectIpOptSSR,'nsIdsDetectIpOptStream':nsIdsDetectIpOptStream,'nsIdsDetectIcmpFrag':nsIdsDetectIcmpFrag,'nsIdsDetectIcmpLarge':nsIdsDetectIcmpLarge,'nsIdsDetectTcpSynFin':nsIdsDetectTcpSynFin,'nsIdsDetectTcpFinNoAck':nsIdsDetectTcpFinNoAck,'nsIdsHttpMalUrl':nsIdsHttpMalUrl,'nsIdsSessMalNum':nsIdsSessMalNum,'nsIdsDetectSynAckAck':nsIdsDetectSynAckAck,'nsIdsDetectIpFrag':nsIdsDetectIpFrag,'nsIdsProtectThreshTable':nsIdsProtectThreshTable,'nsIdsProtectThreshEntry':nsIdsProtectThreshEntry,_H:nsIdsProtectThreshZoneIdx,'nsIdsSynAttackThresh':nsIdsSynAttackThresh,'nsIdsSynAttackTimeout':nsIdsSynAttackTimeout,'nsIdsSynAttackAlmTh':nsIdsSynAttackAlmTh,'nsIdsSynAttackQueSize':nsIdsSynAttackQueSize,'nsIdsSynAttackAgeTime':nsIdsSynAttackAgeTime,'nsIdsIcmpFloodThresh':nsIdsIcmpFloodThresh,'nsIdsUdpFloodThresh':nsIdsUdpFloodThresh,'nsIdsPortScanThresh':nsIdsPortScanThresh,'nsIdsIpSweepThresh':nsIdsIpSweepThresh,'nsIdsSynAckAckThres':nsIdsSynAckAckThres,'nsIdsAttkMonTable':nsIdsAttkMonTable,'nsIdsAttkMonEntry':nsIdsAttkMonEntry,_I:nsIdsAttkMonIfIdx,'nsIdsAttkMonVsys':nsIdsAttkMonVsys,'nsIdsAttkMonSynAttk':nsIdsAttkMonSynAttk,'nsIdsAttkMonTearDrop':nsIdsAttkMonTearDrop,'nsIdsAttkMonSrcRoute':nsIdsAttkMonSrcRoute,'nsIdsAttkMonPingDeath':nsIdsAttkMonPingDeath,'nsIdsAttkMonAddrSpoof':nsIdsAttkMonAddrSpoof,'nsIdsAttkMonLand':nsIdsAttkMonLand,'nsIdsAttkMonIcmpFlood':nsIdsAttkMonIcmpFlood,'nsIdsAttkMonUdpFlood':nsIdsAttkMonUdpFlood,'nsIdsAttkMonWinnuke':nsIdsAttkMonWinnuke,'nsIdsAttkMonPortScan':nsIdsAttkMonPortScan,'nsIdsAttkMonIpSweep':nsIdsAttkMonIpSweep,'nsAttkMonSynFrag':nsAttkMonSynFrag,'nsAttkMonTcpNoFlag':nsAttkMonTcpNoFlag,'nsAttkMonIpUnknownProt':nsAttkMonIpUnknownProt,'nsAttkMonIpOptBad':nsAttkMonIpOptBad,'nsAttkMonIpOptRecord':nsAttkMonIpOptRecord,'nsAttkMonIpOptTimestamp':nsAttkMonIpOptTimestamp,'nsAttkMonIpOptSCHT':nsAttkMonIpOptSCHT,'nsAttkMonIpOptLSR':nsAttkMonIpOptLSR,'nsAttkMonIpOptSSR':nsAttkMonIpOptSSR,'nsAttkMonIpOptStream':nsAttkMonIpOptStream,'nsAttkMonIcmpFrag':nsAttkMonIcmpFrag,'nsAttkMonIcmpLarge':nsAttkMonIcmpLarge,'nsAttkMonTcpSynFin':nsAttkMonTcpSynFin,'nsAttkMonTcpFinNoAck':nsAttkMonTcpFinNoAck,'nsAttkMonHttpMalUrl':nsAttkMonHttpMalUrl,'nsAttkMonSessMalNum':nsAttkMonSessMalNum,'nsAttkMonSynAckAck':nsAttkMonSynAckAck,'nsAttkMonIpFrag':nsAttkMonIpFrag,'nsIdsAttkMonIfInfo':nsIdsAttkMonIfInfo})