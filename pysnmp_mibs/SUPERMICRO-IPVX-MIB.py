_K='fsIpv6IfIcmpEntry'
_J='fsIpvxAddrPrefixLen'
_I='fsIpvxAddrPrefix'
_H='fsIpvxAddrPrefixAddrType'
_G='fsIpvxAddrPrefixIfIndex'
_F='TruthValue'
_E='read-create'
_D='not-accessible'
_C='SUPERMICRO-IPVX-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType')
ipv6InterfaceEntry,=mibBuilder.importSymbols('IP-MIB','ipv6InterfaceEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_F)
fsipvxMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,2,16))
if mibBuilder.loadTexts:fsipvxMIB.setRevisions(('2012-09-05 00:00',))
_Fsipvx_ObjectIdentity=ObjectIdentity
fsipvx=_Fsipvx_ObjectIdentity((1,3,6,1,4,1,10876,101,2,16,1))
_FsIpvxAddrPrefixTable_Object=MibTable
fsIpvxAddrPrefixTable=_FsIpvxAddrPrefixTable_Object((1,3,6,1,4,1,10876,101,2,16,1,1))
if mibBuilder.loadTexts:fsIpvxAddrPrefixTable.setStatus(_A)
_FsIpvxAddrPrefixEntry_Object=MibTableRow
fsIpvxAddrPrefixEntry=_FsIpvxAddrPrefixEntry_Object((1,3,6,1,4,1,10876,101,2,16,1,1,1))
fsIpvxAddrPrefixEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:fsIpvxAddrPrefixEntry.setStatus(_A)
_FsIpvxAddrPrefixIfIndex_Type=InterfaceIndex
_FsIpvxAddrPrefixIfIndex_Object=MibTableColumn
fsIpvxAddrPrefixIfIndex=_FsIpvxAddrPrefixIfIndex_Object((1,3,6,1,4,1,10876,101,2,16,1,1,1,1),_FsIpvxAddrPrefixIfIndex_Type())
fsIpvxAddrPrefixIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIpvxAddrPrefixIfIndex.setStatus(_A)
_FsIpvxAddrPrefixAddrType_Type=InetAddressType
_FsIpvxAddrPrefixAddrType_Object=MibTableColumn
fsIpvxAddrPrefixAddrType=_FsIpvxAddrPrefixAddrType_Object((1,3,6,1,4,1,10876,101,2,16,1,1,1,2),_FsIpvxAddrPrefixAddrType_Type())
fsIpvxAddrPrefixAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIpvxAddrPrefixAddrType.setStatus(_A)
_FsIpvxAddrPrefix_Type=InetAddress
_FsIpvxAddrPrefix_Object=MibTableColumn
fsIpvxAddrPrefix=_FsIpvxAddrPrefix_Object((1,3,6,1,4,1,10876,101,2,16,1,1,1,3),_FsIpvxAddrPrefix_Type())
fsIpvxAddrPrefix.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIpvxAddrPrefix.setStatus(_A)
_FsIpvxAddrPrefixLen_Type=InetAddressPrefixLength
_FsIpvxAddrPrefixLen_Object=MibTableColumn
fsIpvxAddrPrefixLen=_FsIpvxAddrPrefixLen_Object((1,3,6,1,4,1,10876,101,2,16,1,1,1,4),_FsIpvxAddrPrefixLen_Type())
fsIpvxAddrPrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIpvxAddrPrefixLen.setStatus(_A)
_FsIpvxAddrPrefixProfileIndex_Type=Unsigned32
_FsIpvxAddrPrefixProfileIndex_Object=MibTableColumn
fsIpvxAddrPrefixProfileIndex=_FsIpvxAddrPrefixProfileIndex_Object((1,3,6,1,4,1,10876,101,2,16,1,1,1,5),_FsIpvxAddrPrefixProfileIndex_Type())
fsIpvxAddrPrefixProfileIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIpvxAddrPrefixProfileIndex.setStatus(_A)
class _FsIpvxAddrPrefixSecAddrFlag_Type(TruthValue):defaultValue=1
_FsIpvxAddrPrefixSecAddrFlag_Type.__name__=_F
_FsIpvxAddrPrefixSecAddrFlag_Object=MibTableColumn
fsIpvxAddrPrefixSecAddrFlag=_FsIpvxAddrPrefixSecAddrFlag_Object((1,3,6,1,4,1,10876,101,2,16,1,1,1,6),_FsIpvxAddrPrefixSecAddrFlag_Type())
fsIpvxAddrPrefixSecAddrFlag.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIpvxAddrPrefixSecAddrFlag.setStatus(_A)
_FsIpvxAddrPrefixRowStatus_Type=RowStatus
_FsIpvxAddrPrefixRowStatus_Object=MibTableColumn
fsIpvxAddrPrefixRowStatus=_FsIpvxAddrPrefixRowStatus_Object((1,3,6,1,4,1,10876,101,2,16,1,1,1,7),_FsIpvxAddrPrefixRowStatus_Type())
fsIpvxAddrPrefixRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIpvxAddrPrefixRowStatus.setStatus(_A)
_Fsipv6Icmpstats_ObjectIdentity=ObjectIdentity
fsipv6Icmpstats=_Fsipv6Icmpstats_ObjectIdentity((1,3,6,1,4,1,10876,101,2,16,2))
_FsIpv6IfIcmpTable_Object=MibTable
fsIpv6IfIcmpTable=_FsIpv6IfIcmpTable_Object((1,3,6,1,4,1,10876,101,2,16,2,1))
if mibBuilder.loadTexts:fsIpv6IfIcmpTable.setStatus(_A)
_FsIpv6IfIcmpEntry_Object=MibTableRow
fsIpv6IfIcmpEntry=_FsIpv6IfIcmpEntry_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1))
if mibBuilder.loadTexts:fsIpv6IfIcmpEntry.setStatus(_A)
_FsIpv6IfIcmpInMsgs_Type=Counter32
_FsIpv6IfIcmpInMsgs_Object=MibTableColumn
fsIpv6IfIcmpInMsgs=_FsIpv6IfIcmpInMsgs_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,1),_FsIpv6IfIcmpInMsgs_Type())
fsIpv6IfIcmpInMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpInMsgs.setStatus(_A)
_FsIpv6IfIcmpInErrors_Type=Counter32
_FsIpv6IfIcmpInErrors_Object=MibTableColumn
fsIpv6IfIcmpInErrors=_FsIpv6IfIcmpInErrors_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,2),_FsIpv6IfIcmpInErrors_Type())
fsIpv6IfIcmpInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpInErrors.setStatus(_A)
_FsIpv6IfIcmpInDestUnreachs_Type=Counter32
_FsIpv6IfIcmpInDestUnreachs_Object=MibTableColumn
fsIpv6IfIcmpInDestUnreachs=_FsIpv6IfIcmpInDestUnreachs_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,3),_FsIpv6IfIcmpInDestUnreachs_Type())
fsIpv6IfIcmpInDestUnreachs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpInDestUnreachs.setStatus(_A)
_FsIpv6IfIcmpInAdminProhibs_Type=Counter32
_FsIpv6IfIcmpInAdminProhibs_Object=MibTableColumn
fsIpv6IfIcmpInAdminProhibs=_FsIpv6IfIcmpInAdminProhibs_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,4),_FsIpv6IfIcmpInAdminProhibs_Type())
fsIpv6IfIcmpInAdminProhibs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpInAdminProhibs.setStatus(_A)
_FsIpv6IfIcmpInTimeExcds_Type=Counter32
_FsIpv6IfIcmpInTimeExcds_Object=MibTableColumn
fsIpv6IfIcmpInTimeExcds=_FsIpv6IfIcmpInTimeExcds_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,5),_FsIpv6IfIcmpInTimeExcds_Type())
fsIpv6IfIcmpInTimeExcds.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpInTimeExcds.setStatus(_A)
_FsIpv6IfIcmpInParmProblems_Type=Counter32
_FsIpv6IfIcmpInParmProblems_Object=MibTableColumn
fsIpv6IfIcmpInParmProblems=_FsIpv6IfIcmpInParmProblems_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,6),_FsIpv6IfIcmpInParmProblems_Type())
fsIpv6IfIcmpInParmProblems.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpInParmProblems.setStatus(_A)
_FsIpv6IfIcmpInPktTooBigs_Type=Counter32
_FsIpv6IfIcmpInPktTooBigs_Object=MibTableColumn
fsIpv6IfIcmpInPktTooBigs=_FsIpv6IfIcmpInPktTooBigs_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,7),_FsIpv6IfIcmpInPktTooBigs_Type())
fsIpv6IfIcmpInPktTooBigs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpInPktTooBigs.setStatus(_A)
_FsIpv6IfIcmpInEchos_Type=Counter32
_FsIpv6IfIcmpInEchos_Object=MibTableColumn
fsIpv6IfIcmpInEchos=_FsIpv6IfIcmpInEchos_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,8),_FsIpv6IfIcmpInEchos_Type())
fsIpv6IfIcmpInEchos.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpInEchos.setStatus(_A)
_FsIpv6IfIcmpInEchoReplies_Type=Counter32
_FsIpv6IfIcmpInEchoReplies_Object=MibTableColumn
fsIpv6IfIcmpInEchoReplies=_FsIpv6IfIcmpInEchoReplies_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,9),_FsIpv6IfIcmpInEchoReplies_Type())
fsIpv6IfIcmpInEchoReplies.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpInEchoReplies.setStatus(_A)
_FsIpv6IfIcmpInRouterSolicits_Type=Counter32
_FsIpv6IfIcmpInRouterSolicits_Object=MibTableColumn
fsIpv6IfIcmpInRouterSolicits=_FsIpv6IfIcmpInRouterSolicits_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,10),_FsIpv6IfIcmpInRouterSolicits_Type())
fsIpv6IfIcmpInRouterSolicits.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpInRouterSolicits.setStatus(_A)
_FsIpv6IfIcmpInRouterAdvertisements_Type=Counter32
_FsIpv6IfIcmpInRouterAdvertisements_Object=MibTableColumn
fsIpv6IfIcmpInRouterAdvertisements=_FsIpv6IfIcmpInRouterAdvertisements_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,11),_FsIpv6IfIcmpInRouterAdvertisements_Type())
fsIpv6IfIcmpInRouterAdvertisements.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpInRouterAdvertisements.setStatus(_A)
_FsIpv6IfIcmpInNeighborSolicits_Type=Counter32
_FsIpv6IfIcmpInNeighborSolicits_Object=MibTableColumn
fsIpv6IfIcmpInNeighborSolicits=_FsIpv6IfIcmpInNeighborSolicits_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,12),_FsIpv6IfIcmpInNeighborSolicits_Type())
fsIpv6IfIcmpInNeighborSolicits.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpInNeighborSolicits.setStatus(_A)
_FsIpv6IfIcmpInNeighborAdvertisements_Type=Counter32
_FsIpv6IfIcmpInNeighborAdvertisements_Object=MibTableColumn
fsIpv6IfIcmpInNeighborAdvertisements=_FsIpv6IfIcmpInNeighborAdvertisements_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,13),_FsIpv6IfIcmpInNeighborAdvertisements_Type())
fsIpv6IfIcmpInNeighborAdvertisements.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpInNeighborAdvertisements.setStatus(_A)
_FsIpv6IfIcmpInRedirects_Type=Counter32
_FsIpv6IfIcmpInRedirects_Object=MibTableColumn
fsIpv6IfIcmpInRedirects=_FsIpv6IfIcmpInRedirects_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,14),_FsIpv6IfIcmpInRedirects_Type())
fsIpv6IfIcmpInRedirects.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpInRedirects.setStatus(_A)
_FsIpv6IfIcmpInGroupMembQueries_Type=Counter32
_FsIpv6IfIcmpInGroupMembQueries_Object=MibTableColumn
fsIpv6IfIcmpInGroupMembQueries=_FsIpv6IfIcmpInGroupMembQueries_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,15),_FsIpv6IfIcmpInGroupMembQueries_Type())
fsIpv6IfIcmpInGroupMembQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpInGroupMembQueries.setStatus(_A)
_FsIpv6IfIcmpInGroupMembResponses_Type=Counter32
_FsIpv6IfIcmpInGroupMembResponses_Object=MibTableColumn
fsIpv6IfIcmpInGroupMembResponses=_FsIpv6IfIcmpInGroupMembResponses_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,16),_FsIpv6IfIcmpInGroupMembResponses_Type())
fsIpv6IfIcmpInGroupMembResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpInGroupMembResponses.setStatus(_A)
_FsIpv6IfIcmpInGroupMembReductions_Type=Counter32
_FsIpv6IfIcmpInGroupMembReductions_Object=MibTableColumn
fsIpv6IfIcmpInGroupMembReductions=_FsIpv6IfIcmpInGroupMembReductions_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,17),_FsIpv6IfIcmpInGroupMembReductions_Type())
fsIpv6IfIcmpInGroupMembReductions.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpInGroupMembReductions.setStatus(_A)
_FsIpv6IfIcmpOutMsgs_Type=Counter32
_FsIpv6IfIcmpOutMsgs_Object=MibTableColumn
fsIpv6IfIcmpOutMsgs=_FsIpv6IfIcmpOutMsgs_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,18),_FsIpv6IfIcmpOutMsgs_Type())
fsIpv6IfIcmpOutMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpOutMsgs.setStatus(_A)
_FsIpv6IfIcmpOutErrors_Type=Counter32
_FsIpv6IfIcmpOutErrors_Object=MibTableColumn
fsIpv6IfIcmpOutErrors=_FsIpv6IfIcmpOutErrors_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,19),_FsIpv6IfIcmpOutErrors_Type())
fsIpv6IfIcmpOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpOutErrors.setStatus(_A)
_FsIpv6IfIcmpOutDestUnreachs_Type=Counter32
_FsIpv6IfIcmpOutDestUnreachs_Object=MibTableColumn
fsIpv6IfIcmpOutDestUnreachs=_FsIpv6IfIcmpOutDestUnreachs_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,20),_FsIpv6IfIcmpOutDestUnreachs_Type())
fsIpv6IfIcmpOutDestUnreachs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpOutDestUnreachs.setStatus(_A)
_FsIpv6IfIcmpOutAdminProhibs_Type=Counter32
_FsIpv6IfIcmpOutAdminProhibs_Object=MibTableColumn
fsIpv6IfIcmpOutAdminProhibs=_FsIpv6IfIcmpOutAdminProhibs_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,21),_FsIpv6IfIcmpOutAdminProhibs_Type())
fsIpv6IfIcmpOutAdminProhibs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpOutAdminProhibs.setStatus(_A)
_FsIpv6IfIcmpOutTimeExcds_Type=Counter32
_FsIpv6IfIcmpOutTimeExcds_Object=MibTableColumn
fsIpv6IfIcmpOutTimeExcds=_FsIpv6IfIcmpOutTimeExcds_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,22),_FsIpv6IfIcmpOutTimeExcds_Type())
fsIpv6IfIcmpOutTimeExcds.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpOutTimeExcds.setStatus(_A)
_FsIpv6IfIcmpOutParmProblems_Type=Counter32
_FsIpv6IfIcmpOutParmProblems_Object=MibTableColumn
fsIpv6IfIcmpOutParmProblems=_FsIpv6IfIcmpOutParmProblems_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,23),_FsIpv6IfIcmpOutParmProblems_Type())
fsIpv6IfIcmpOutParmProblems.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpOutParmProblems.setStatus(_A)
_FsIpv6IfIcmpOutPktTooBigs_Type=Counter32
_FsIpv6IfIcmpOutPktTooBigs_Object=MibTableColumn
fsIpv6IfIcmpOutPktTooBigs=_FsIpv6IfIcmpOutPktTooBigs_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,24),_FsIpv6IfIcmpOutPktTooBigs_Type())
fsIpv6IfIcmpOutPktTooBigs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpOutPktTooBigs.setStatus(_A)
_FsIpv6IfIcmpOutEchos_Type=Counter32
_FsIpv6IfIcmpOutEchos_Object=MibTableColumn
fsIpv6IfIcmpOutEchos=_FsIpv6IfIcmpOutEchos_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,25),_FsIpv6IfIcmpOutEchos_Type())
fsIpv6IfIcmpOutEchos.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpOutEchos.setStatus(_A)
_FsIpv6IfIcmpOutEchoReplies_Type=Counter32
_FsIpv6IfIcmpOutEchoReplies_Object=MibTableColumn
fsIpv6IfIcmpOutEchoReplies=_FsIpv6IfIcmpOutEchoReplies_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,26),_FsIpv6IfIcmpOutEchoReplies_Type())
fsIpv6IfIcmpOutEchoReplies.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpOutEchoReplies.setStatus(_A)
_FsIpv6IfIcmpOutRouterSolicits_Type=Counter32
_FsIpv6IfIcmpOutRouterSolicits_Object=MibTableColumn
fsIpv6IfIcmpOutRouterSolicits=_FsIpv6IfIcmpOutRouterSolicits_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,27),_FsIpv6IfIcmpOutRouterSolicits_Type())
fsIpv6IfIcmpOutRouterSolicits.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpOutRouterSolicits.setStatus(_A)
_FsIpv6IfIcmpOutRouterAdvertisements_Type=Counter32
_FsIpv6IfIcmpOutRouterAdvertisements_Object=MibTableColumn
fsIpv6IfIcmpOutRouterAdvertisements=_FsIpv6IfIcmpOutRouterAdvertisements_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,28),_FsIpv6IfIcmpOutRouterAdvertisements_Type())
fsIpv6IfIcmpOutRouterAdvertisements.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpOutRouterAdvertisements.setStatus(_A)
_FsIpv6IfIcmpOutNeighborSolicits_Type=Counter32
_FsIpv6IfIcmpOutNeighborSolicits_Object=MibTableColumn
fsIpv6IfIcmpOutNeighborSolicits=_FsIpv6IfIcmpOutNeighborSolicits_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,29),_FsIpv6IfIcmpOutNeighborSolicits_Type())
fsIpv6IfIcmpOutNeighborSolicits.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpOutNeighborSolicits.setStatus(_A)
_FsIpv6IfIcmpOutNeighborAdvertisements_Type=Counter32
_FsIpv6IfIcmpOutNeighborAdvertisements_Object=MibTableColumn
fsIpv6IfIcmpOutNeighborAdvertisements=_FsIpv6IfIcmpOutNeighborAdvertisements_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,30),_FsIpv6IfIcmpOutNeighborAdvertisements_Type())
fsIpv6IfIcmpOutNeighborAdvertisements.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpOutNeighborAdvertisements.setStatus(_A)
_FsIpv6IfIcmpOutRedirects_Type=Counter32
_FsIpv6IfIcmpOutRedirects_Object=MibTableColumn
fsIpv6IfIcmpOutRedirects=_FsIpv6IfIcmpOutRedirects_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,31),_FsIpv6IfIcmpOutRedirects_Type())
fsIpv6IfIcmpOutRedirects.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpOutRedirects.setStatus(_A)
_FsIpv6IfIcmpOutGroupMembQueries_Type=Counter32
_FsIpv6IfIcmpOutGroupMembQueries_Object=MibTableColumn
fsIpv6IfIcmpOutGroupMembQueries=_FsIpv6IfIcmpOutGroupMembQueries_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,32),_FsIpv6IfIcmpOutGroupMembQueries_Type())
fsIpv6IfIcmpOutGroupMembQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpOutGroupMembQueries.setStatus(_A)
_FsIpv6IfIcmpOutGroupMembResponses_Type=Counter32
_FsIpv6IfIcmpOutGroupMembResponses_Object=MibTableColumn
fsIpv6IfIcmpOutGroupMembResponses=_FsIpv6IfIcmpOutGroupMembResponses_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,33),_FsIpv6IfIcmpOutGroupMembResponses_Type())
fsIpv6IfIcmpOutGroupMembResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpOutGroupMembResponses.setStatus(_A)
_FsIpv6IfIcmpOutGroupMembReductions_Type=Counter32
_FsIpv6IfIcmpOutGroupMembReductions_Object=MibTableColumn
fsIpv6IfIcmpOutGroupMembReductions=_FsIpv6IfIcmpOutGroupMembReductions_Object((1,3,6,1,4,1,10876,101,2,16,2,1,1,34),_FsIpv6IfIcmpOutGroupMembReductions_Type())
fsIpv6IfIcmpOutGroupMembReductions.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpv6IfIcmpOutGroupMembReductions.setStatus(_A)
ipv6InterfaceEntry.registerAugmentions((_C,_K))
fsIpv6IfIcmpEntry.setIndexNames(*ipv6InterfaceEntry.getIndexNames())
mibBuilder.exportSymbols(_C,**{'fsipvxMIB':fsipvxMIB,'fsipvx':fsipvx,'fsIpvxAddrPrefixTable':fsIpvxAddrPrefixTable,'fsIpvxAddrPrefixEntry':fsIpvxAddrPrefixEntry,_G:fsIpvxAddrPrefixIfIndex,_H:fsIpvxAddrPrefixAddrType,_I:fsIpvxAddrPrefix,_J:fsIpvxAddrPrefixLen,'fsIpvxAddrPrefixProfileIndex':fsIpvxAddrPrefixProfileIndex,'fsIpvxAddrPrefixSecAddrFlag':fsIpvxAddrPrefixSecAddrFlag,'fsIpvxAddrPrefixRowStatus':fsIpvxAddrPrefixRowStatus,'fsipv6Icmpstats':fsipv6Icmpstats,'fsIpv6IfIcmpTable':fsIpv6IfIcmpTable,_K:fsIpv6IfIcmpEntry,'fsIpv6IfIcmpInMsgs':fsIpv6IfIcmpInMsgs,'fsIpv6IfIcmpInErrors':fsIpv6IfIcmpInErrors,'fsIpv6IfIcmpInDestUnreachs':fsIpv6IfIcmpInDestUnreachs,'fsIpv6IfIcmpInAdminProhibs':fsIpv6IfIcmpInAdminProhibs,'fsIpv6IfIcmpInTimeExcds':fsIpv6IfIcmpInTimeExcds,'fsIpv6IfIcmpInParmProblems':fsIpv6IfIcmpInParmProblems,'fsIpv6IfIcmpInPktTooBigs':fsIpv6IfIcmpInPktTooBigs,'fsIpv6IfIcmpInEchos':fsIpv6IfIcmpInEchos,'fsIpv6IfIcmpInEchoReplies':fsIpv6IfIcmpInEchoReplies,'fsIpv6IfIcmpInRouterSolicits':fsIpv6IfIcmpInRouterSolicits,'fsIpv6IfIcmpInRouterAdvertisements':fsIpv6IfIcmpInRouterAdvertisements,'fsIpv6IfIcmpInNeighborSolicits':fsIpv6IfIcmpInNeighborSolicits,'fsIpv6IfIcmpInNeighborAdvertisements':fsIpv6IfIcmpInNeighborAdvertisements,'fsIpv6IfIcmpInRedirects':fsIpv6IfIcmpInRedirects,'fsIpv6IfIcmpInGroupMembQueries':fsIpv6IfIcmpInGroupMembQueries,'fsIpv6IfIcmpInGroupMembResponses':fsIpv6IfIcmpInGroupMembResponses,'fsIpv6IfIcmpInGroupMembReductions':fsIpv6IfIcmpInGroupMembReductions,'fsIpv6IfIcmpOutMsgs':fsIpv6IfIcmpOutMsgs,'fsIpv6IfIcmpOutErrors':fsIpv6IfIcmpOutErrors,'fsIpv6IfIcmpOutDestUnreachs':fsIpv6IfIcmpOutDestUnreachs,'fsIpv6IfIcmpOutAdminProhibs':fsIpv6IfIcmpOutAdminProhibs,'fsIpv6IfIcmpOutTimeExcds':fsIpv6IfIcmpOutTimeExcds,'fsIpv6IfIcmpOutParmProblems':fsIpv6IfIcmpOutParmProblems,'fsIpv6IfIcmpOutPktTooBigs':fsIpv6IfIcmpOutPktTooBigs,'fsIpv6IfIcmpOutEchos':fsIpv6IfIcmpOutEchos,'fsIpv6IfIcmpOutEchoReplies':fsIpv6IfIcmpOutEchoReplies,'fsIpv6IfIcmpOutRouterSolicits':fsIpv6IfIcmpOutRouterSolicits,'fsIpv6IfIcmpOutRouterAdvertisements':fsIpv6IfIcmpOutRouterAdvertisements,'fsIpv6IfIcmpOutNeighborSolicits':fsIpv6IfIcmpOutNeighborSolicits,'fsIpv6IfIcmpOutNeighborAdvertisements':fsIpv6IfIcmpOutNeighborAdvertisements,'fsIpv6IfIcmpOutRedirects':fsIpv6IfIcmpOutRedirects,'fsIpv6IfIcmpOutGroupMembQueries':fsIpv6IfIcmpOutGroupMembQueries,'fsIpv6IfIcmpOutGroupMembResponses':fsIpv6IfIcmpOutGroupMembResponses,'fsIpv6IfIcmpOutGroupMembReductions':fsIpv6IfIcmpOutGroupMembReductions})