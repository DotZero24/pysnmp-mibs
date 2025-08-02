_V='ccpcPerfGrp'
_U='ccpcSystemGrp'
_T='ccpcPcfSentZlbs'
_S='ccpcPcfRcvdZlbs'
_R='ccpcPcfDroppedCdns'
_Q='ccpcPcfSentCdns'
_P='ccpcPcfRcvdCdns'
_O='ccpcPcfDroppedIccns'
_N='ccpcPcfAcptdIccns'
_M='ccpcPcfRcvdIccns'
_L='ccpcPcfSentIcrps'
_K='ccpcPcfDroppedIcrqs'
_J='ccpcPcfAcptdIcrqs'
_I='ccpcPcfRcvdIcrqs'
_H='ccpcSessionTotal'
_G='ccpcEnabled'
_F='not-accessible'
_E='ccpcPcfIpAddress'
_D='ccpcPcfIpAddressType'
_C='read-only'
_B='CISCO-CDMA-PDSN-CRP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoCdmaPdsnCrpMIB=ModuleIdentity((1,3,6,1,4,1,9,9,957))
if mibBuilder.loadTexts:ciscoCdmaPdsnCrpMIB.setRevisions(('2004-07-27 00:00',))
_CcpcMIBObjects_ObjectIdentity=ObjectIdentity
ccpcMIBObjects=_CcpcMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,957,1))
_CcpcSystemInfo_ObjectIdentity=ObjectIdentity
ccpcSystemInfo=_CcpcSystemInfo_ObjectIdentity((1,3,6,1,4,1,9,9,957,1,1))
_CcpcEnabled_Type=TruthValue
_CcpcEnabled_Object=MibScalar
ccpcEnabled=_CcpcEnabled_Object((1,3,6,1,4,1,9,9,957,1,1,1),_CcpcEnabled_Type())
ccpcEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:ccpcEnabled.setStatus(_A)
_CcpcSessionTotal_Type=Gauge32
_CcpcSessionTotal_Object=MibScalar
ccpcSessionTotal=_CcpcSessionTotal_Object((1,3,6,1,4,1,9,9,957,1,1,2),_CcpcSessionTotal_Type())
ccpcSessionTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:ccpcSessionTotal.setStatus(_A)
_CcpcPerfStats_ObjectIdentity=ObjectIdentity
ccpcPerfStats=_CcpcPerfStats_ObjectIdentity((1,3,6,1,4,1,9,9,957,1,2))
_CcpcPcfPerfStatsTable_Object=MibTable
ccpcPcfPerfStatsTable=_CcpcPcfPerfStatsTable_Object((1,3,6,1,4,1,9,9,957,1,2,1))
if mibBuilder.loadTexts:ccpcPcfPerfStatsTable.setStatus(_A)
_CcpcPcfPerfStatsEntry_Object=MibTableRow
ccpcPcfPerfStatsEntry=_CcpcPcfPerfStatsEntry_Object((1,3,6,1,4,1,9,9,957,1,2,1,1))
ccpcPcfPerfStatsEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:ccpcPcfPerfStatsEntry.setStatus(_A)
_CcpcPcfIpAddressType_Type=InetAddressType
_CcpcPcfIpAddressType_Object=MibTableColumn
ccpcPcfIpAddressType=_CcpcPcfIpAddressType_Object((1,3,6,1,4,1,9,9,957,1,2,1,1,1),_CcpcPcfIpAddressType_Type())
ccpcPcfIpAddressType.setMaxAccess(_F)
if mibBuilder.loadTexts:ccpcPcfIpAddressType.setStatus(_A)
_CcpcPcfIpAddress_Type=InetAddress
_CcpcPcfIpAddress_Object=MibTableColumn
ccpcPcfIpAddress=_CcpcPcfIpAddress_Object((1,3,6,1,4,1,9,9,957,1,2,1,1,2),_CcpcPcfIpAddress_Type())
ccpcPcfIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:ccpcPcfIpAddress.setStatus(_A)
_CcpcPcfRcvdIcrqs_Type=Counter32
_CcpcPcfRcvdIcrqs_Object=MibTableColumn
ccpcPcfRcvdIcrqs=_CcpcPcfRcvdIcrqs_Object((1,3,6,1,4,1,9,9,957,1,2,1,1,3),_CcpcPcfRcvdIcrqs_Type())
ccpcPcfRcvdIcrqs.setMaxAccess(_C)
if mibBuilder.loadTexts:ccpcPcfRcvdIcrqs.setStatus(_A)
_CcpcPcfAcptdIcrqs_Type=Counter32
_CcpcPcfAcptdIcrqs_Object=MibTableColumn
ccpcPcfAcptdIcrqs=_CcpcPcfAcptdIcrqs_Object((1,3,6,1,4,1,9,9,957,1,2,1,1,4),_CcpcPcfAcptdIcrqs_Type())
ccpcPcfAcptdIcrqs.setMaxAccess(_C)
if mibBuilder.loadTexts:ccpcPcfAcptdIcrqs.setStatus(_A)
_CcpcPcfDroppedIcrqs_Type=Counter32
_CcpcPcfDroppedIcrqs_Object=MibTableColumn
ccpcPcfDroppedIcrqs=_CcpcPcfDroppedIcrqs_Object((1,3,6,1,4,1,9,9,957,1,2,1,1,5),_CcpcPcfDroppedIcrqs_Type())
ccpcPcfDroppedIcrqs.setMaxAccess(_C)
if mibBuilder.loadTexts:ccpcPcfDroppedIcrqs.setStatus(_A)
_CcpcPcfSentIcrps_Type=Counter32
_CcpcPcfSentIcrps_Object=MibTableColumn
ccpcPcfSentIcrps=_CcpcPcfSentIcrps_Object((1,3,6,1,4,1,9,9,957,1,2,1,1,6),_CcpcPcfSentIcrps_Type())
ccpcPcfSentIcrps.setMaxAccess(_C)
if mibBuilder.loadTexts:ccpcPcfSentIcrps.setStatus(_A)
_CcpcPcfRcvdIccns_Type=Counter32
_CcpcPcfRcvdIccns_Object=MibTableColumn
ccpcPcfRcvdIccns=_CcpcPcfRcvdIccns_Object((1,3,6,1,4,1,9,9,957,1,2,1,1,7),_CcpcPcfRcvdIccns_Type())
ccpcPcfRcvdIccns.setMaxAccess(_C)
if mibBuilder.loadTexts:ccpcPcfRcvdIccns.setStatus(_A)
_CcpcPcfAcptdIccns_Type=Counter32
_CcpcPcfAcptdIccns_Object=MibTableColumn
ccpcPcfAcptdIccns=_CcpcPcfAcptdIccns_Object((1,3,6,1,4,1,9,9,957,1,2,1,1,8),_CcpcPcfAcptdIccns_Type())
ccpcPcfAcptdIccns.setMaxAccess(_C)
if mibBuilder.loadTexts:ccpcPcfAcptdIccns.setStatus(_A)
_CcpcPcfDroppedIccns_Type=Counter32
_CcpcPcfDroppedIccns_Object=MibTableColumn
ccpcPcfDroppedIccns=_CcpcPcfDroppedIccns_Object((1,3,6,1,4,1,9,9,957,1,2,1,1,9),_CcpcPcfDroppedIccns_Type())
ccpcPcfDroppedIccns.setMaxAccess(_C)
if mibBuilder.loadTexts:ccpcPcfDroppedIccns.setStatus(_A)
_CcpcPcfRcvdCdns_Type=Counter32
_CcpcPcfRcvdCdns_Object=MibTableColumn
ccpcPcfRcvdCdns=_CcpcPcfRcvdCdns_Object((1,3,6,1,4,1,9,9,957,1,2,1,1,10),_CcpcPcfRcvdCdns_Type())
ccpcPcfRcvdCdns.setMaxAccess(_C)
if mibBuilder.loadTexts:ccpcPcfRcvdCdns.setStatus(_A)
_CcpcPcfSentCdns_Type=Counter32
_CcpcPcfSentCdns_Object=MibTableColumn
ccpcPcfSentCdns=_CcpcPcfSentCdns_Object((1,3,6,1,4,1,9,9,957,1,2,1,1,11),_CcpcPcfSentCdns_Type())
ccpcPcfSentCdns.setMaxAccess(_C)
if mibBuilder.loadTexts:ccpcPcfSentCdns.setStatus(_A)
_CcpcPcfDroppedCdns_Type=Counter32
_CcpcPcfDroppedCdns_Object=MibTableColumn
ccpcPcfDroppedCdns=_CcpcPcfDroppedCdns_Object((1,3,6,1,4,1,9,9,957,1,2,1,1,12),_CcpcPcfDroppedCdns_Type())
ccpcPcfDroppedCdns.setMaxAccess(_C)
if mibBuilder.loadTexts:ccpcPcfDroppedCdns.setStatus(_A)
_CcpcPcfRcvdZlbs_Type=Counter32
_CcpcPcfRcvdZlbs_Object=MibTableColumn
ccpcPcfRcvdZlbs=_CcpcPcfRcvdZlbs_Object((1,3,6,1,4,1,9,9,957,1,2,1,1,13),_CcpcPcfRcvdZlbs_Type())
ccpcPcfRcvdZlbs.setMaxAccess(_C)
if mibBuilder.loadTexts:ccpcPcfRcvdZlbs.setStatus(_A)
_CcpcPcfSentZlbs_Type=Counter32
_CcpcPcfSentZlbs_Object=MibTableColumn
ccpcPcfSentZlbs=_CcpcPcfSentZlbs_Object((1,3,6,1,4,1,9,9,957,1,2,1,1,14),_CcpcPcfSentZlbs_Type())
ccpcPcfSentZlbs.setMaxAccess(_C)
if mibBuilder.loadTexts:ccpcPcfSentZlbs.setStatus(_A)
_CcpcMIBConformance_ObjectIdentity=ObjectIdentity
ccpcMIBConformance=_CcpcMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,957,2))
_CcpcMIBCompliances_ObjectIdentity=ObjectIdentity
ccpcMIBCompliances=_CcpcMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,957,2,1))
_CcpcMIBGroups_ObjectIdentity=ObjectIdentity
ccpcMIBGroups=_CcpcMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,957,2,2))
ccpcSystemGrp=ObjectGroup((1,3,6,1,4,1,9,9,957,2,2,1))
ccpcSystemGrp.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:ccpcSystemGrp.setStatus(_A)
ccpcPerfGrp=ObjectGroup((1,3,6,1,4,1,9,9,957,2,2,2))
ccpcPerfGrp.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ccpcPerfGrp.setStatus(_A)
ccpcMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,957,2,1,1))
ccpcMIBCompliance.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:ccpcMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoCdmaPdsnCrpMIB':ciscoCdmaPdsnCrpMIB,'ccpcMIBObjects':ccpcMIBObjects,'ccpcSystemInfo':ccpcSystemInfo,_G:ccpcEnabled,_H:ccpcSessionTotal,'ccpcPerfStats':ccpcPerfStats,'ccpcPcfPerfStatsTable':ccpcPcfPerfStatsTable,'ccpcPcfPerfStatsEntry':ccpcPcfPerfStatsEntry,_D:ccpcPcfIpAddressType,_E:ccpcPcfIpAddress,_I:ccpcPcfRcvdIcrqs,_J:ccpcPcfAcptdIcrqs,_K:ccpcPcfDroppedIcrqs,_L:ccpcPcfSentIcrps,_M:ccpcPcfRcvdIccns,_N:ccpcPcfAcptdIccns,_O:ccpcPcfDroppedIccns,_P:ccpcPcfRcvdCdns,_Q:ccpcPcfSentCdns,_R:ccpcPcfDroppedCdns,_S:ccpcPcfRcvdZlbs,_T:ccpcPcfSentZlbs,'ccpcMIBConformance':ccpcMIBConformance,'ccpcMIBCompliances':ccpcMIBCompliances,'ccpcMIBCompliance':ccpcMIBCompliance,'ccpcMIBGroups':ccpcMIBGroups,_U:ccpcSystemGrp,_V:ccpcPerfGrp})