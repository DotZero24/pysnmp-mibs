_W='jnxLdpSesDownIf'
_V='jnxLdpSesDownReason'
_U='jnxLdpSesUpIf'
_T='jnxLdpLspDownReason'
_S='jnxLdpFecLength'
_R='jnxLdpFec'
_Q='jnxLdpFecType'
_P='jnxLdpInstanceId'
_O='unknown'
_N='InetAddressPrefixLength'
_M='InetAddress'
_L='jnxLdpInstanceName'
_K='jnxLdpLspFecLen'
_J='jnxLdpRtrid'
_I='jnxLdpLspFec'
_H='jnxMplsLdpSesState'
_G='JUNIPER-MPLS-LDP-MIB'
_F='not-accessible'
_E='read-only'
_D='Integer32'
_C='accessible-for-notify'
_B='JUNIPER-LDP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_M,_N,'InetAddressType')
jnxMplsLdpSesState,=mibBuilder.importSymbols(_G,_H)
jnxLdpTraps,jnxMibs=mibBuilder.importSymbols('JUNIPER-SMI','jnxLdpTraps','jnxMibs')
MplsVpnName,=mibBuilder.importSymbols('MPLS-VPN-MIB','MplsVpnName')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
jnxLdp=ModuleIdentity((1,3,6,1,4,1,2636,3,14))
if mibBuilder.loadTexts:jnxLdp.setRevisions(('2004-08-10 00:00','2004-06-23 00:00','2004-06-22 00:00','2002-01-10 00:00'))
_JnxLdpTrapVars_ObjectIdentity=ObjectIdentity
jnxLdpTrapVars=_JnxLdpTrapVars_ObjectIdentity((1,3,6,1,4,1,2636,3,14,1))
_JnxLdpLspFec_Type=IpAddress
_JnxLdpLspFec_Object=MibScalar
jnxLdpLspFec=_JnxLdpLspFec_Object((1,3,6,1,4,1,2636,3,14,1,1),_JnxLdpLspFec_Type())
jnxLdpLspFec.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxLdpLspFec.setStatus(_A)
_JnxLdpRtrid_Type=IpAddress
_JnxLdpRtrid_Object=MibScalar
jnxLdpRtrid=_JnxLdpRtrid_Object((1,3,6,1,4,1,2636,3,14,1,2),_JnxLdpRtrid_Type())
jnxLdpRtrid.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxLdpRtrid.setStatus(_A)
class _JnxLdpLspDownReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('topologyChanged',1),('receivedWithdrawl',2),('neighborDown',3),('filterChanged',4),('bfdSessionDown',5),(_O,6),('lspingDown',7)))
_JnxLdpLspDownReason_Type.__name__=_D
_JnxLdpLspDownReason_Object=MibScalar
jnxLdpLspDownReason=_JnxLdpLspDownReason_Object((1,3,6,1,4,1,2636,3,14,1,3),_JnxLdpLspDownReason_Type())
jnxLdpLspDownReason.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxLdpLspDownReason.setStatus(_A)
class _JnxLdpSesDownReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_O,0),('holdExpired',1),('connectionExpired',2),('allAdjacenciesDown',3),('badTLV',4),('badPDU',5),('connectionError',6),('connectionReset',7),('peerSentNotification',8),('unexpectedEOF',9),('authenticationChanged',10),('initError',11),('gracefulRestartAbort',12),('cliCommand',13),('gracefulRestartChanged',14)))
_JnxLdpSesDownReason_Type.__name__=_D
_JnxLdpSesDownReason_Object=MibScalar
jnxLdpSesDownReason=_JnxLdpSesDownReason_Object((1,3,6,1,4,1,2636,3,14,1,4),_JnxLdpSesDownReason_Type())
jnxLdpSesDownReason.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxLdpSesDownReason.setStatus(_A)
_JnxLdpSesDownIf_Type=InterfaceIndexOrZero
_JnxLdpSesDownIf_Object=MibScalar
jnxLdpSesDownIf=_JnxLdpSesDownIf_Object((1,3,6,1,4,1,2636,3,14,1,5),_JnxLdpSesDownIf_Type())
jnxLdpSesDownIf.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxLdpSesDownIf.setStatus(_A)
class _JnxLdpLspFecLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_JnxLdpLspFecLen_Type.__name__=_D
_JnxLdpLspFecLen_Object=MibScalar
jnxLdpLspFecLen=_JnxLdpLspFecLen_Object((1,3,6,1,4,1,2636,3,14,1,6),_JnxLdpLspFecLen_Type())
jnxLdpLspFecLen.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxLdpLspFecLen.setStatus(_A)
_JnxLdpSesUpIf_Type=InterfaceIndexOrZero
_JnxLdpSesUpIf_Object=MibScalar
jnxLdpSesUpIf=_JnxLdpSesUpIf_Object((1,3,6,1,4,1,2636,3,14,1,7),_JnxLdpSesUpIf_Type())
jnxLdpSesUpIf.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxLdpSesUpIf.setStatus(_A)
_JnxLdpInstanceName_Type=MplsVpnName
_JnxLdpInstanceName_Object=MibScalar
jnxLdpInstanceName=_JnxLdpInstanceName_Object((1,3,6,1,4,1,2636,3,14,1,8),_JnxLdpInstanceName_Type())
jnxLdpInstanceName.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxLdpInstanceName.setStatus(_A)
_JnxLdpStatsTable_Object=MibTable
jnxLdpStatsTable=_JnxLdpStatsTable_Object((1,3,6,1,4,1,2636,3,14,2))
if mibBuilder.loadTexts:jnxLdpStatsTable.setStatus(_A)
_JnxLdpStatsEntry_Object=MibTableRow
jnxLdpStatsEntry=_JnxLdpStatsEntry_Object((1,3,6,1,4,1,2636,3,14,2,1))
jnxLdpStatsEntry.setIndexNames((0,_B,_P),(0,_B,_Q),(0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:jnxLdpStatsEntry.setStatus(_A)
_JnxLdpInstanceId_Type=Unsigned32
_JnxLdpInstanceId_Object=MibTableColumn
jnxLdpInstanceId=_JnxLdpInstanceId_Object((1,3,6,1,4,1,2636,3,14,2,1,1),_JnxLdpInstanceId_Type())
jnxLdpInstanceId.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxLdpInstanceId.setStatus(_A)
_JnxLdpFecType_Type=InetAddressType
_JnxLdpFecType_Object=MibTableColumn
jnxLdpFecType=_JnxLdpFecType_Object((1,3,6,1,4,1,2636,3,14,2,1,2),_JnxLdpFecType_Type())
jnxLdpFecType.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxLdpFecType.setStatus(_A)
class _JnxLdpFec_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_JnxLdpFec_Type.__name__=_M
_JnxLdpFec_Object=MibTableColumn
jnxLdpFec=_JnxLdpFec_Object((1,3,6,1,4,1,2636,3,14,2,1,3),_JnxLdpFec_Type())
jnxLdpFec.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxLdpFec.setStatus(_A)
class _JnxLdpFecLength_Type(InetAddressPrefixLength):subtypeSpec=InetAddressPrefixLength.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_JnxLdpFecLength_Type.__name__=_N
_JnxLdpFecLength_Object=MibTableColumn
jnxLdpFecLength=_JnxLdpFecLength_Object((1,3,6,1,4,1,2636,3,14,2,1,4),_JnxLdpFecLength_Type())
jnxLdpFecLength.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxLdpFecLength.setStatus(_A)
class _JnxLdpFecStatisticsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ok',1),('disabled',2),('unavailable',3)))
_JnxLdpFecStatisticsStatus_Type.__name__=_D
_JnxLdpFecStatisticsStatus_Object=MibTableColumn
jnxLdpFecStatisticsStatus=_JnxLdpFecStatisticsStatus_Object((1,3,6,1,4,1,2636,3,14,2,1,5),_JnxLdpFecStatisticsStatus_Type())
jnxLdpFecStatisticsStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:jnxLdpFecStatisticsStatus.setStatus(_A)
_JnxLdpIngressOctets_Type=Counter64
_JnxLdpIngressOctets_Object=MibTableColumn
jnxLdpIngressOctets=_JnxLdpIngressOctets_Object((1,3,6,1,4,1,2636,3,14,2,1,6),_JnxLdpIngressOctets_Type())
jnxLdpIngressOctets.setMaxAccess(_E)
if mibBuilder.loadTexts:jnxLdpIngressOctets.setStatus(_A)
_JnxLdpIngressPackets_Type=Counter64
_JnxLdpIngressPackets_Object=MibTableColumn
jnxLdpIngressPackets=_JnxLdpIngressPackets_Object((1,3,6,1,4,1,2636,3,14,2,1,7),_JnxLdpIngressPackets_Type())
jnxLdpIngressPackets.setMaxAccess(_E)
if mibBuilder.loadTexts:jnxLdpIngressPackets.setStatus(_A)
_JnxLdpTransitOctets_Type=Counter64
_JnxLdpTransitOctets_Object=MibTableColumn
jnxLdpTransitOctets=_JnxLdpTransitOctets_Object((1,3,6,1,4,1,2636,3,14,2,1,8),_JnxLdpTransitOctets_Type())
jnxLdpTransitOctets.setMaxAccess(_E)
if mibBuilder.loadTexts:jnxLdpTransitOctets.setStatus(_A)
_JnxLdpTransitPackets_Type=Counter64
_JnxLdpTransitPackets_Object=MibTableColumn
jnxLdpTransitPackets=_JnxLdpTransitPackets_Object((1,3,6,1,4,1,2636,3,14,2,1,9),_JnxLdpTransitPackets_Type())
jnxLdpTransitPackets.setMaxAccess(_E)
if mibBuilder.loadTexts:jnxLdpTransitPackets.setStatus(_A)
_JnxLdpTrapPrefix_ObjectIdentity=ObjectIdentity
jnxLdpTrapPrefix=_JnxLdpTrapPrefix_ObjectIdentity((1,3,6,1,4,1,2636,4,4,0))
jnxLdpLspUp=NotificationType((1,3,6,1,4,1,2636,4,4,0,1))
jnxLdpLspUp.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:jnxLdpLspUp.setStatus(_A)
jnxLdpLspDown=NotificationType((1,3,6,1,4,1,2636,4,4,0,2))
jnxLdpLspDown.setObjects(*((_B,_I),(_B,_J),(_B,_T),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:jnxLdpLspDown.setStatus(_A)
jnxLdpSesUp=NotificationType((1,3,6,1,4,1,2636,4,4,0,3))
jnxLdpSesUp.setObjects(*((_G,_H),(_B,_U)))
if mibBuilder.loadTexts:jnxLdpSesUp.setStatus(_A)
jnxLdpSesDown=NotificationType((1,3,6,1,4,1,2636,4,4,0,4))
jnxLdpSesDown.setObjects(*((_G,_H),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:jnxLdpSesDown.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'jnxLdp':jnxLdp,'jnxLdpTrapVars':jnxLdpTrapVars,_I:jnxLdpLspFec,_J:jnxLdpRtrid,_T:jnxLdpLspDownReason,_V:jnxLdpSesDownReason,_W:jnxLdpSesDownIf,_K:jnxLdpLspFecLen,_U:jnxLdpSesUpIf,_L:jnxLdpInstanceName,'jnxLdpStatsTable':jnxLdpStatsTable,'jnxLdpStatsEntry':jnxLdpStatsEntry,_P:jnxLdpInstanceId,_Q:jnxLdpFecType,_R:jnxLdpFec,_S:jnxLdpFecLength,'jnxLdpFecStatisticsStatus':jnxLdpFecStatisticsStatus,'jnxLdpIngressOctets':jnxLdpIngressOctets,'jnxLdpIngressPackets':jnxLdpIngressPackets,'jnxLdpTransitOctets':jnxLdpTransitOctets,'jnxLdpTransitPackets':jnxLdpTransitPackets,'jnxLdpTrapPrefix':jnxLdpTrapPrefix,'jnxLdpLspUp':jnxLdpLspUp,'jnxLdpLspDown':jnxLdpLspDown,'jnxLdpSesUp':jnxLdpSesUp,'jnxLdpSesDown':jnxLdpSesDown})