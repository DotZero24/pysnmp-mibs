_y='aristaSwFwdIpOctetGroup'
_x='aristaSwFwdIpStatsGroup'
_w='aristaSwFwdIpStatsHCOutMcastOctets'
_v='aristaSwFwdIpStatsOutMcastOctets'
_u='aristaSwFwdIpStatsHCInMcastOctets'
_t='aristaSwFwdIpStatsInMcastOctets'
_s='aristaSwFwdIpStatsHCOutOctets'
_r='aristaSwFwdIpStatsOutOctets'
_q='aristaSwFwdIpStatsHCInOctets'
_p='aristaSwFwdIpStatsInOctets'
_o='aristaSwFwdIpStatsRefreshRate'
_n='aristaSwFwdIpStatsDiscontinuityTime'
_m='aristaSwFwdIpStatsHCOutBcastPkts'
_l='aristaSwFwdIpStatsOutBcastPkts'
_k='aristaSwFwdIpStatsHCInBcastPkts'
_j='aristaSwFwdIpStatsInBcastPkts'
_i='aristaSwFwdIpStatsHCOutMcastPkts'
_h='aristaSwFwdIpStatsOutMcastPkts'
_g='aristaSwFwdIpStatsHCInMcastPkts'
_f='aristaSwFwdIpStatsInMcastPkts'
_e='aristaSwFwdIpStatsHCOutTransmits'
_d='aristaSwFwdIpStatsOutTransmits'
_c='aristaSwFwdIpStatsOutFragCreates'
_b='aristaSwFwdIpStatsOutFragFails'
_a='aristaSwFwdIpStatsOutFragOKs'
_Z='aristaSwFwdIpStatsOutFragReqds'
_Y='aristaSwFwdIpStatsOutDiscards'
_X='aristaSwFwdIpStatsHCOutForwDatagrams'
_W='aristaSwFwdIpStatsOutForwDatagrams'
_V='aristaSwFwdIpStatsOutNoRoutes'
_U='aristaSwFwdIpStatsHCOutRequests'
_T='aristaSwFwdIpStatsOutRequests'
_S='aristaSwFwdIpStatsHCInDelivers'
_R='aristaSwFwdIpStatsInDelivers'
_Q='aristaSwFwdIpStatsInDiscards'
_P='aristaSwFwdIpStatsReasmFails'
_O='aristaSwFwdIpStatsReasmOKs'
_N='aristaSwFwdIpStatsReasmReqds'
_M='aristaSwFwdIpStatsHCInForwDatagrams'
_L='aristaSwFwdIpStatsInForwDatagrams'
_K='aristaSwFwdIpStatsInTruncatedPkts'
_J='aristaSwFwdIpStatsInUnknownProtos'
_I='aristaSwFwdIpStatsInAddrErrors'
_H='aristaSwFwdIpStatsInNoRoutes'
_G='aristaSwFwdIpStatsInHdrErrors'
_F='aristaSwFwdIpStatsHCInReceives'
_E='aristaSwFwdIpStatsInReceives'
_D='aristaSwFwdIpStatsIPVersion'
_C='read-only'
_B='ARISTA-SW-IP-FORWARDING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
InetVersion,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetVersion')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
aristaSwIpForwardingMIB=ModuleIdentity((1,3,6,1,4,1,30065,3,1))
if mibBuilder.loadTexts:aristaSwIpForwardingMIB.setRevisions(('2014-08-15 00:00','2011-03-31 13:00','2010-01-31 00:00','2009-03-16 00:00'))
_AristaSwFwdIp_ObjectIdentity=ObjectIdentity
aristaSwFwdIp=_AristaSwFwdIp_ObjectIdentity((1,3,6,1,4,1,30065,3,1,1))
_AristaSwFwdIpStatsTable_Object=MibTable
aristaSwFwdIpStatsTable=_AristaSwFwdIpStatsTable_Object((1,3,6,1,4,1,30065,3,1,1,1))
if mibBuilder.loadTexts:aristaSwFwdIpStatsTable.setStatus(_A)
_AristaSwFwdIpStatsEntry_Object=MibTableRow
aristaSwFwdIpStatsEntry=_AristaSwFwdIpStatsEntry_Object((1,3,6,1,4,1,30065,3,1,1,1,1))
aristaSwFwdIpStatsEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:aristaSwFwdIpStatsEntry.setStatus(_A)
_AristaSwFwdIpStatsIPVersion_Type=InetVersion
_AristaSwFwdIpStatsIPVersion_Object=MibTableColumn
aristaSwFwdIpStatsIPVersion=_AristaSwFwdIpStatsIPVersion_Object((1,3,6,1,4,1,30065,3,1,1,1,1,1),_AristaSwFwdIpStatsIPVersion_Type())
aristaSwFwdIpStatsIPVersion.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:aristaSwFwdIpStatsIPVersion.setStatus(_A)
_AristaSwFwdIpStatsInReceives_Type=Counter32
_AristaSwFwdIpStatsInReceives_Object=MibTableColumn
aristaSwFwdIpStatsInReceives=_AristaSwFwdIpStatsInReceives_Object((1,3,6,1,4,1,30065,3,1,1,1,1,3),_AristaSwFwdIpStatsInReceives_Type())
aristaSwFwdIpStatsInReceives.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsInReceives.setStatus(_A)
_AristaSwFwdIpStatsHCInReceives_Type=Counter64
_AristaSwFwdIpStatsHCInReceives_Object=MibTableColumn
aristaSwFwdIpStatsHCInReceives=_AristaSwFwdIpStatsHCInReceives_Object((1,3,6,1,4,1,30065,3,1,1,1,1,4),_AristaSwFwdIpStatsHCInReceives_Type())
aristaSwFwdIpStatsHCInReceives.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsHCInReceives.setStatus(_A)
_AristaSwFwdIpStatsInOctets_Type=Counter32
_AristaSwFwdIpStatsInOctets_Object=MibTableColumn
aristaSwFwdIpStatsInOctets=_AristaSwFwdIpStatsInOctets_Object((1,3,6,1,4,1,30065,3,1,1,1,1,5),_AristaSwFwdIpStatsInOctets_Type())
aristaSwFwdIpStatsInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsInOctets.setStatus(_A)
_AristaSwFwdIpStatsHCInOctets_Type=Counter64
_AristaSwFwdIpStatsHCInOctets_Object=MibTableColumn
aristaSwFwdIpStatsHCInOctets=_AristaSwFwdIpStatsHCInOctets_Object((1,3,6,1,4,1,30065,3,1,1,1,1,6),_AristaSwFwdIpStatsHCInOctets_Type())
aristaSwFwdIpStatsHCInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsHCInOctets.setStatus(_A)
_AristaSwFwdIpStatsInHdrErrors_Type=Counter32
_AristaSwFwdIpStatsInHdrErrors_Object=MibTableColumn
aristaSwFwdIpStatsInHdrErrors=_AristaSwFwdIpStatsInHdrErrors_Object((1,3,6,1,4,1,30065,3,1,1,1,1,7),_AristaSwFwdIpStatsInHdrErrors_Type())
aristaSwFwdIpStatsInHdrErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsInHdrErrors.setStatus(_A)
_AristaSwFwdIpStatsInNoRoutes_Type=Counter32
_AristaSwFwdIpStatsInNoRoutes_Object=MibTableColumn
aristaSwFwdIpStatsInNoRoutes=_AristaSwFwdIpStatsInNoRoutes_Object((1,3,6,1,4,1,30065,3,1,1,1,1,8),_AristaSwFwdIpStatsInNoRoutes_Type())
aristaSwFwdIpStatsInNoRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsInNoRoutes.setStatus(_A)
_AristaSwFwdIpStatsInAddrErrors_Type=Counter32
_AristaSwFwdIpStatsInAddrErrors_Object=MibTableColumn
aristaSwFwdIpStatsInAddrErrors=_AristaSwFwdIpStatsInAddrErrors_Object((1,3,6,1,4,1,30065,3,1,1,1,1,9),_AristaSwFwdIpStatsInAddrErrors_Type())
aristaSwFwdIpStatsInAddrErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsInAddrErrors.setStatus(_A)
_AristaSwFwdIpStatsInUnknownProtos_Type=Counter32
_AristaSwFwdIpStatsInUnknownProtos_Object=MibTableColumn
aristaSwFwdIpStatsInUnknownProtos=_AristaSwFwdIpStatsInUnknownProtos_Object((1,3,6,1,4,1,30065,3,1,1,1,1,10),_AristaSwFwdIpStatsInUnknownProtos_Type())
aristaSwFwdIpStatsInUnknownProtos.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsInUnknownProtos.setStatus(_A)
_AristaSwFwdIpStatsInTruncatedPkts_Type=Counter32
_AristaSwFwdIpStatsInTruncatedPkts_Object=MibTableColumn
aristaSwFwdIpStatsInTruncatedPkts=_AristaSwFwdIpStatsInTruncatedPkts_Object((1,3,6,1,4,1,30065,3,1,1,1,1,11),_AristaSwFwdIpStatsInTruncatedPkts_Type())
aristaSwFwdIpStatsInTruncatedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsInTruncatedPkts.setStatus(_A)
_AristaSwFwdIpStatsInForwDatagrams_Type=Counter32
_AristaSwFwdIpStatsInForwDatagrams_Object=MibTableColumn
aristaSwFwdIpStatsInForwDatagrams=_AristaSwFwdIpStatsInForwDatagrams_Object((1,3,6,1,4,1,30065,3,1,1,1,1,12),_AristaSwFwdIpStatsInForwDatagrams_Type())
aristaSwFwdIpStatsInForwDatagrams.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsInForwDatagrams.setStatus(_A)
_AristaSwFwdIpStatsHCInForwDatagrams_Type=Counter64
_AristaSwFwdIpStatsHCInForwDatagrams_Object=MibTableColumn
aristaSwFwdIpStatsHCInForwDatagrams=_AristaSwFwdIpStatsHCInForwDatagrams_Object((1,3,6,1,4,1,30065,3,1,1,1,1,13),_AristaSwFwdIpStatsHCInForwDatagrams_Type())
aristaSwFwdIpStatsHCInForwDatagrams.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsHCInForwDatagrams.setStatus(_A)
_AristaSwFwdIpStatsReasmReqds_Type=Counter32
_AristaSwFwdIpStatsReasmReqds_Object=MibTableColumn
aristaSwFwdIpStatsReasmReqds=_AristaSwFwdIpStatsReasmReqds_Object((1,3,6,1,4,1,30065,3,1,1,1,1,14),_AristaSwFwdIpStatsReasmReqds_Type())
aristaSwFwdIpStatsReasmReqds.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsReasmReqds.setStatus(_A)
_AristaSwFwdIpStatsReasmOKs_Type=Counter32
_AristaSwFwdIpStatsReasmOKs_Object=MibTableColumn
aristaSwFwdIpStatsReasmOKs=_AristaSwFwdIpStatsReasmOKs_Object((1,3,6,1,4,1,30065,3,1,1,1,1,15),_AristaSwFwdIpStatsReasmOKs_Type())
aristaSwFwdIpStatsReasmOKs.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsReasmOKs.setStatus(_A)
_AristaSwFwdIpStatsReasmFails_Type=Counter32
_AristaSwFwdIpStatsReasmFails_Object=MibTableColumn
aristaSwFwdIpStatsReasmFails=_AristaSwFwdIpStatsReasmFails_Object((1,3,6,1,4,1,30065,3,1,1,1,1,16),_AristaSwFwdIpStatsReasmFails_Type())
aristaSwFwdIpStatsReasmFails.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsReasmFails.setStatus(_A)
_AristaSwFwdIpStatsInDiscards_Type=Counter32
_AristaSwFwdIpStatsInDiscards_Object=MibTableColumn
aristaSwFwdIpStatsInDiscards=_AristaSwFwdIpStatsInDiscards_Object((1,3,6,1,4,1,30065,3,1,1,1,1,17),_AristaSwFwdIpStatsInDiscards_Type())
aristaSwFwdIpStatsInDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsInDiscards.setStatus(_A)
_AristaSwFwdIpStatsInDelivers_Type=Counter32
_AristaSwFwdIpStatsInDelivers_Object=MibTableColumn
aristaSwFwdIpStatsInDelivers=_AristaSwFwdIpStatsInDelivers_Object((1,3,6,1,4,1,30065,3,1,1,1,1,18),_AristaSwFwdIpStatsInDelivers_Type())
aristaSwFwdIpStatsInDelivers.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsInDelivers.setStatus(_A)
_AristaSwFwdIpStatsHCInDelivers_Type=Counter64
_AristaSwFwdIpStatsHCInDelivers_Object=MibTableColumn
aristaSwFwdIpStatsHCInDelivers=_AristaSwFwdIpStatsHCInDelivers_Object((1,3,6,1,4,1,30065,3,1,1,1,1,19),_AristaSwFwdIpStatsHCInDelivers_Type())
aristaSwFwdIpStatsHCInDelivers.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsHCInDelivers.setStatus(_A)
_AristaSwFwdIpStatsOutRequests_Type=Counter32
_AristaSwFwdIpStatsOutRequests_Object=MibTableColumn
aristaSwFwdIpStatsOutRequests=_AristaSwFwdIpStatsOutRequests_Object((1,3,6,1,4,1,30065,3,1,1,1,1,20),_AristaSwFwdIpStatsOutRequests_Type())
aristaSwFwdIpStatsOutRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsOutRequests.setStatus(_A)
_AristaSwFwdIpStatsHCOutRequests_Type=Counter64
_AristaSwFwdIpStatsHCOutRequests_Object=MibTableColumn
aristaSwFwdIpStatsHCOutRequests=_AristaSwFwdIpStatsHCOutRequests_Object((1,3,6,1,4,1,30065,3,1,1,1,1,21),_AristaSwFwdIpStatsHCOutRequests_Type())
aristaSwFwdIpStatsHCOutRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsHCOutRequests.setStatus(_A)
_AristaSwFwdIpStatsOutNoRoutes_Type=Counter32
_AristaSwFwdIpStatsOutNoRoutes_Object=MibTableColumn
aristaSwFwdIpStatsOutNoRoutes=_AristaSwFwdIpStatsOutNoRoutes_Object((1,3,6,1,4,1,30065,3,1,1,1,1,22),_AristaSwFwdIpStatsOutNoRoutes_Type())
aristaSwFwdIpStatsOutNoRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsOutNoRoutes.setStatus(_A)
_AristaSwFwdIpStatsOutForwDatagrams_Type=Counter32
_AristaSwFwdIpStatsOutForwDatagrams_Object=MibTableColumn
aristaSwFwdIpStatsOutForwDatagrams=_AristaSwFwdIpStatsOutForwDatagrams_Object((1,3,6,1,4,1,30065,3,1,1,1,1,23),_AristaSwFwdIpStatsOutForwDatagrams_Type())
aristaSwFwdIpStatsOutForwDatagrams.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsOutForwDatagrams.setStatus(_A)
_AristaSwFwdIpStatsHCOutForwDatagrams_Type=Counter64
_AristaSwFwdIpStatsHCOutForwDatagrams_Object=MibTableColumn
aristaSwFwdIpStatsHCOutForwDatagrams=_AristaSwFwdIpStatsHCOutForwDatagrams_Object((1,3,6,1,4,1,30065,3,1,1,1,1,24),_AristaSwFwdIpStatsHCOutForwDatagrams_Type())
aristaSwFwdIpStatsHCOutForwDatagrams.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsHCOutForwDatagrams.setStatus(_A)
_AristaSwFwdIpStatsOutDiscards_Type=Counter32
_AristaSwFwdIpStatsOutDiscards_Object=MibTableColumn
aristaSwFwdIpStatsOutDiscards=_AristaSwFwdIpStatsOutDiscards_Object((1,3,6,1,4,1,30065,3,1,1,1,1,25),_AristaSwFwdIpStatsOutDiscards_Type())
aristaSwFwdIpStatsOutDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsOutDiscards.setStatus(_A)
_AristaSwFwdIpStatsOutFragReqds_Type=Counter32
_AristaSwFwdIpStatsOutFragReqds_Object=MibTableColumn
aristaSwFwdIpStatsOutFragReqds=_AristaSwFwdIpStatsOutFragReqds_Object((1,3,6,1,4,1,30065,3,1,1,1,1,26),_AristaSwFwdIpStatsOutFragReqds_Type())
aristaSwFwdIpStatsOutFragReqds.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsOutFragReqds.setStatus(_A)
_AristaSwFwdIpStatsOutFragOKs_Type=Counter32
_AristaSwFwdIpStatsOutFragOKs_Object=MibTableColumn
aristaSwFwdIpStatsOutFragOKs=_AristaSwFwdIpStatsOutFragOKs_Object((1,3,6,1,4,1,30065,3,1,1,1,1,27),_AristaSwFwdIpStatsOutFragOKs_Type())
aristaSwFwdIpStatsOutFragOKs.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsOutFragOKs.setStatus(_A)
_AristaSwFwdIpStatsOutFragFails_Type=Counter32
_AristaSwFwdIpStatsOutFragFails_Object=MibTableColumn
aristaSwFwdIpStatsOutFragFails=_AristaSwFwdIpStatsOutFragFails_Object((1,3,6,1,4,1,30065,3,1,1,1,1,28),_AristaSwFwdIpStatsOutFragFails_Type())
aristaSwFwdIpStatsOutFragFails.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsOutFragFails.setStatus(_A)
_AristaSwFwdIpStatsOutFragCreates_Type=Counter32
_AristaSwFwdIpStatsOutFragCreates_Object=MibTableColumn
aristaSwFwdIpStatsOutFragCreates=_AristaSwFwdIpStatsOutFragCreates_Object((1,3,6,1,4,1,30065,3,1,1,1,1,29),_AristaSwFwdIpStatsOutFragCreates_Type())
aristaSwFwdIpStatsOutFragCreates.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsOutFragCreates.setStatus(_A)
_AristaSwFwdIpStatsOutTransmits_Type=Counter32
_AristaSwFwdIpStatsOutTransmits_Object=MibTableColumn
aristaSwFwdIpStatsOutTransmits=_AristaSwFwdIpStatsOutTransmits_Object((1,3,6,1,4,1,30065,3,1,1,1,1,30),_AristaSwFwdIpStatsOutTransmits_Type())
aristaSwFwdIpStatsOutTransmits.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsOutTransmits.setStatus(_A)
_AristaSwFwdIpStatsHCOutTransmits_Type=Counter64
_AristaSwFwdIpStatsHCOutTransmits_Object=MibTableColumn
aristaSwFwdIpStatsHCOutTransmits=_AristaSwFwdIpStatsHCOutTransmits_Object((1,3,6,1,4,1,30065,3,1,1,1,1,31),_AristaSwFwdIpStatsHCOutTransmits_Type())
aristaSwFwdIpStatsHCOutTransmits.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsHCOutTransmits.setStatus(_A)
_AristaSwFwdIpStatsOutOctets_Type=Counter32
_AristaSwFwdIpStatsOutOctets_Object=MibTableColumn
aristaSwFwdIpStatsOutOctets=_AristaSwFwdIpStatsOutOctets_Object((1,3,6,1,4,1,30065,3,1,1,1,1,32),_AristaSwFwdIpStatsOutOctets_Type())
aristaSwFwdIpStatsOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsOutOctets.setStatus(_A)
_AristaSwFwdIpStatsHCOutOctets_Type=Counter64
_AristaSwFwdIpStatsHCOutOctets_Object=MibTableColumn
aristaSwFwdIpStatsHCOutOctets=_AristaSwFwdIpStatsHCOutOctets_Object((1,3,6,1,4,1,30065,3,1,1,1,1,33),_AristaSwFwdIpStatsHCOutOctets_Type())
aristaSwFwdIpStatsHCOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsHCOutOctets.setStatus(_A)
_AristaSwFwdIpStatsInMcastPkts_Type=Counter32
_AristaSwFwdIpStatsInMcastPkts_Object=MibTableColumn
aristaSwFwdIpStatsInMcastPkts=_AristaSwFwdIpStatsInMcastPkts_Object((1,3,6,1,4,1,30065,3,1,1,1,1,34),_AristaSwFwdIpStatsInMcastPkts_Type())
aristaSwFwdIpStatsInMcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsInMcastPkts.setStatus(_A)
_AristaSwFwdIpStatsHCInMcastPkts_Type=Counter64
_AristaSwFwdIpStatsHCInMcastPkts_Object=MibTableColumn
aristaSwFwdIpStatsHCInMcastPkts=_AristaSwFwdIpStatsHCInMcastPkts_Object((1,3,6,1,4,1,30065,3,1,1,1,1,35),_AristaSwFwdIpStatsHCInMcastPkts_Type())
aristaSwFwdIpStatsHCInMcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsHCInMcastPkts.setStatus(_A)
_AristaSwFwdIpStatsInMcastOctets_Type=Counter32
_AristaSwFwdIpStatsInMcastOctets_Object=MibTableColumn
aristaSwFwdIpStatsInMcastOctets=_AristaSwFwdIpStatsInMcastOctets_Object((1,3,6,1,4,1,30065,3,1,1,1,1,36),_AristaSwFwdIpStatsInMcastOctets_Type())
aristaSwFwdIpStatsInMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsInMcastOctets.setStatus(_A)
_AristaSwFwdIpStatsHCInMcastOctets_Type=Counter64
_AristaSwFwdIpStatsHCInMcastOctets_Object=MibTableColumn
aristaSwFwdIpStatsHCInMcastOctets=_AristaSwFwdIpStatsHCInMcastOctets_Object((1,3,6,1,4,1,30065,3,1,1,1,1,37),_AristaSwFwdIpStatsHCInMcastOctets_Type())
aristaSwFwdIpStatsHCInMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsHCInMcastOctets.setStatus(_A)
_AristaSwFwdIpStatsOutMcastPkts_Type=Counter32
_AristaSwFwdIpStatsOutMcastPkts_Object=MibTableColumn
aristaSwFwdIpStatsOutMcastPkts=_AristaSwFwdIpStatsOutMcastPkts_Object((1,3,6,1,4,1,30065,3,1,1,1,1,38),_AristaSwFwdIpStatsOutMcastPkts_Type())
aristaSwFwdIpStatsOutMcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsOutMcastPkts.setStatus(_A)
_AristaSwFwdIpStatsHCOutMcastPkts_Type=Counter64
_AristaSwFwdIpStatsHCOutMcastPkts_Object=MibTableColumn
aristaSwFwdIpStatsHCOutMcastPkts=_AristaSwFwdIpStatsHCOutMcastPkts_Object((1,3,6,1,4,1,30065,3,1,1,1,1,39),_AristaSwFwdIpStatsHCOutMcastPkts_Type())
aristaSwFwdIpStatsHCOutMcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsHCOutMcastPkts.setStatus(_A)
_AristaSwFwdIpStatsOutMcastOctets_Type=Counter32
_AristaSwFwdIpStatsOutMcastOctets_Object=MibTableColumn
aristaSwFwdIpStatsOutMcastOctets=_AristaSwFwdIpStatsOutMcastOctets_Object((1,3,6,1,4,1,30065,3,1,1,1,1,40),_AristaSwFwdIpStatsOutMcastOctets_Type())
aristaSwFwdIpStatsOutMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsOutMcastOctets.setStatus(_A)
_AristaSwFwdIpStatsHCOutMcastOctets_Type=Counter64
_AristaSwFwdIpStatsHCOutMcastOctets_Object=MibTableColumn
aristaSwFwdIpStatsHCOutMcastOctets=_AristaSwFwdIpStatsHCOutMcastOctets_Object((1,3,6,1,4,1,30065,3,1,1,1,1,41),_AristaSwFwdIpStatsHCOutMcastOctets_Type())
aristaSwFwdIpStatsHCOutMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsHCOutMcastOctets.setStatus(_A)
_AristaSwFwdIpStatsInBcastPkts_Type=Counter32
_AristaSwFwdIpStatsInBcastPkts_Object=MibTableColumn
aristaSwFwdIpStatsInBcastPkts=_AristaSwFwdIpStatsInBcastPkts_Object((1,3,6,1,4,1,30065,3,1,1,1,1,42),_AristaSwFwdIpStatsInBcastPkts_Type())
aristaSwFwdIpStatsInBcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsInBcastPkts.setStatus(_A)
_AristaSwFwdIpStatsHCInBcastPkts_Type=Counter64
_AristaSwFwdIpStatsHCInBcastPkts_Object=MibTableColumn
aristaSwFwdIpStatsHCInBcastPkts=_AristaSwFwdIpStatsHCInBcastPkts_Object((1,3,6,1,4,1,30065,3,1,1,1,1,43),_AristaSwFwdIpStatsHCInBcastPkts_Type())
aristaSwFwdIpStatsHCInBcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsHCInBcastPkts.setStatus(_A)
_AristaSwFwdIpStatsOutBcastPkts_Type=Counter32
_AristaSwFwdIpStatsOutBcastPkts_Object=MibTableColumn
aristaSwFwdIpStatsOutBcastPkts=_AristaSwFwdIpStatsOutBcastPkts_Object((1,3,6,1,4,1,30065,3,1,1,1,1,44),_AristaSwFwdIpStatsOutBcastPkts_Type())
aristaSwFwdIpStatsOutBcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsOutBcastPkts.setStatus(_A)
_AristaSwFwdIpStatsHCOutBcastPkts_Type=Counter64
_AristaSwFwdIpStatsHCOutBcastPkts_Object=MibTableColumn
aristaSwFwdIpStatsHCOutBcastPkts=_AristaSwFwdIpStatsHCOutBcastPkts_Object((1,3,6,1,4,1,30065,3,1,1,1,1,45),_AristaSwFwdIpStatsHCOutBcastPkts_Type())
aristaSwFwdIpStatsHCOutBcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsHCOutBcastPkts.setStatus(_A)
_AristaSwFwdIpStatsDiscontinuityTime_Type=TimeStamp
_AristaSwFwdIpStatsDiscontinuityTime_Object=MibTableColumn
aristaSwFwdIpStatsDiscontinuityTime=_AristaSwFwdIpStatsDiscontinuityTime_Object((1,3,6,1,4,1,30065,3,1,1,1,1,46),_AristaSwFwdIpStatsDiscontinuityTime_Type())
aristaSwFwdIpStatsDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsDiscontinuityTime.setStatus(_A)
_AristaSwFwdIpStatsRefreshRate_Type=Unsigned32
_AristaSwFwdIpStatsRefreshRate_Object=MibTableColumn
aristaSwFwdIpStatsRefreshRate=_AristaSwFwdIpStatsRefreshRate_Object((1,3,6,1,4,1,30065,3,1,1,1,1,47),_AristaSwFwdIpStatsRefreshRate_Type())
aristaSwFwdIpStatsRefreshRate.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaSwFwdIpStatsRefreshRate.setStatus(_A)
if mibBuilder.loadTexts:aristaSwFwdIpStatsRefreshRate.setUnits('milli-seconds')
_AristaSwIpFwdMIBConformance_ObjectIdentity=ObjectIdentity
aristaSwIpFwdMIBConformance=_AristaSwIpFwdMIBConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,1,2))
_AristaSwIpFwdMIBCompliances_ObjectIdentity=ObjectIdentity
aristaSwIpFwdMIBCompliances=_AristaSwIpFwdMIBCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,1,2,1))
_AristaSwIpFwdMIBGroups_ObjectIdentity=ObjectIdentity
aristaSwIpFwdMIBGroups=_AristaSwIpFwdMIBGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,1,2,2))
aristaSwFwdIpStatsGroup=ObjectGroup((1,3,6,1,4,1,30065,3,1,2,2,1))
aristaSwFwdIpStatsGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:aristaSwFwdIpStatsGroup.setStatus(_A)
aristaSwFwdIpOctetGroup=ObjectGroup((1,3,6,1,4,1,30065,3,1,2,2,2))
aristaSwFwdIpOctetGroup.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:aristaSwFwdIpOctetGroup.setStatus(_A)
aristaSwIpFwdMIBCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,1,2,1,2))
aristaSwIpFwdMIBCompliance.setObjects(*((_B,_x),(_B,_y)))
if mibBuilder.loadTexts:aristaSwIpFwdMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'aristaSwIpForwardingMIB':aristaSwIpForwardingMIB,'aristaSwFwdIp':aristaSwFwdIp,'aristaSwFwdIpStatsTable':aristaSwFwdIpStatsTable,'aristaSwFwdIpStatsEntry':aristaSwFwdIpStatsEntry,_D:aristaSwFwdIpStatsIPVersion,_E:aristaSwFwdIpStatsInReceives,_F:aristaSwFwdIpStatsHCInReceives,_p:aristaSwFwdIpStatsInOctets,_q:aristaSwFwdIpStatsHCInOctets,_G:aristaSwFwdIpStatsInHdrErrors,_H:aristaSwFwdIpStatsInNoRoutes,_I:aristaSwFwdIpStatsInAddrErrors,_J:aristaSwFwdIpStatsInUnknownProtos,_K:aristaSwFwdIpStatsInTruncatedPkts,_L:aristaSwFwdIpStatsInForwDatagrams,_M:aristaSwFwdIpStatsHCInForwDatagrams,_N:aristaSwFwdIpStatsReasmReqds,_O:aristaSwFwdIpStatsReasmOKs,_P:aristaSwFwdIpStatsReasmFails,_Q:aristaSwFwdIpStatsInDiscards,_R:aristaSwFwdIpStatsInDelivers,_S:aristaSwFwdIpStatsHCInDelivers,_T:aristaSwFwdIpStatsOutRequests,_U:aristaSwFwdIpStatsHCOutRequests,_V:aristaSwFwdIpStatsOutNoRoutes,_W:aristaSwFwdIpStatsOutForwDatagrams,_X:aristaSwFwdIpStatsHCOutForwDatagrams,_Y:aristaSwFwdIpStatsOutDiscards,_Z:aristaSwFwdIpStatsOutFragReqds,_a:aristaSwFwdIpStatsOutFragOKs,_b:aristaSwFwdIpStatsOutFragFails,_c:aristaSwFwdIpStatsOutFragCreates,_d:aristaSwFwdIpStatsOutTransmits,_e:aristaSwFwdIpStatsHCOutTransmits,_r:aristaSwFwdIpStatsOutOctets,_s:aristaSwFwdIpStatsHCOutOctets,_f:aristaSwFwdIpStatsInMcastPkts,_g:aristaSwFwdIpStatsHCInMcastPkts,_t:aristaSwFwdIpStatsInMcastOctets,_u:aristaSwFwdIpStatsHCInMcastOctets,_h:aristaSwFwdIpStatsOutMcastPkts,_i:aristaSwFwdIpStatsHCOutMcastPkts,_v:aristaSwFwdIpStatsOutMcastOctets,_w:aristaSwFwdIpStatsHCOutMcastOctets,_j:aristaSwFwdIpStatsInBcastPkts,_k:aristaSwFwdIpStatsHCInBcastPkts,_l:aristaSwFwdIpStatsOutBcastPkts,_m:aristaSwFwdIpStatsHCOutBcastPkts,_n:aristaSwFwdIpStatsDiscontinuityTime,_o:aristaSwFwdIpStatsRefreshRate,'aristaSwIpFwdMIBConformance':aristaSwIpFwdMIBConformance,'aristaSwIpFwdMIBCompliances':aristaSwIpFwdMIBCompliances,'aristaSwIpFwdMIBCompliance':aristaSwIpFwdMIBCompliance,'aristaSwIpFwdMIBGroups':aristaSwIpFwdMIBGroups,_x:aristaSwFwdIpStatsGroup,_y:aristaSwFwdIpOctetGroup})