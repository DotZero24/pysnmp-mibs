_Q='altigaCertStatsGroup'
_P='alCertStatsServerCRLTimeouts'
_O='alCertStatsServerCRLPendingRequests'
_N='alCertStatsServerCRLRcvd'
_M='alCertStatsServerCRLRetransmissions'
_L='alCertStatsServerCRLRequests'
_K='alCertStatsServerCertTimeouts'
_J='alCertStatsServerCertPendingRequests'
_I='alCertStatsServerCertRcvd'
_H='alCertStatsServerCertRetransmissions'
_G='alCertStatsServerCertRequests'
_F='alCertStatsServerPortNumber'
_E='alCertStatsServerAddress'
_D='alCertStatsServerIndex'
_C='read-only'
_B='ALTIGA-CERT-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alCertMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alCertMibModule')
alCertGroup,alStatsCert=mibBuilder.importSymbols('ALTIGA-MIB','alCertGroup','alStatsCert')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
altigaCertStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,32,2))
if mibBuilder.loadTexts:altigaCertStatsMibModule.setRevisions(('2002-09-05 13:00','2002-07-10 00:00'))
_AltigaCertStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaCertStatsMibConformance=_AltigaCertStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,32,2,1))
_AltigaCertStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaCertStatsMibCompliances=_AltigaCertStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,32,2,1,1))
_AlStatsCertGlobal_ObjectIdentity=ObjectIdentity
alStatsCertGlobal=_AlStatsCertGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,27,1))
_AlCertStatsServerTable_Object=MibTable
alCertStatsServerTable=_AlCertStatsServerTable_Object((1,3,6,1,4,1,3076,2,1,2,27,2))
if mibBuilder.loadTexts:alCertStatsServerTable.setStatus(_A)
_AlCertStatsServerEntry_Object=MibTableRow
alCertStatsServerEntry=_AlCertStatsServerEntry_Object((1,3,6,1,4,1,3076,2,1,2,27,2,1))
alCertStatsServerEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:alCertStatsServerEntry.setStatus(_A)
_AlCertStatsServerIndex_Type=Integer32
_AlCertStatsServerIndex_Object=MibTableColumn
alCertStatsServerIndex=_AlCertStatsServerIndex_Object((1,3,6,1,4,1,3076,2,1,2,27,2,1,1),_AlCertStatsServerIndex_Type())
alCertStatsServerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alCertStatsServerIndex.setStatus(_A)
_AlCertStatsServerAddress_Type=IpAddress
_AlCertStatsServerAddress_Object=MibTableColumn
alCertStatsServerAddress=_AlCertStatsServerAddress_Object((1,3,6,1,4,1,3076,2,1,2,27,2,1,2),_AlCertStatsServerAddress_Type())
alCertStatsServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:alCertStatsServerAddress.setStatus(_A)
_AlCertStatsServerPortNumber_Type=Integer32
_AlCertStatsServerPortNumber_Object=MibTableColumn
alCertStatsServerPortNumber=_AlCertStatsServerPortNumber_Object((1,3,6,1,4,1,3076,2,1,2,27,2,1,3),_AlCertStatsServerPortNumber_Type())
alCertStatsServerPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alCertStatsServerPortNumber.setStatus(_A)
_AlCertStatsServerCertRequests_Type=Counter32
_AlCertStatsServerCertRequests_Object=MibTableColumn
alCertStatsServerCertRequests=_AlCertStatsServerCertRequests_Object((1,3,6,1,4,1,3076,2,1,2,27,2,1,4),_AlCertStatsServerCertRequests_Type())
alCertStatsServerCertRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:alCertStatsServerCertRequests.setStatus(_A)
_AlCertStatsServerCertRetransmissions_Type=Counter32
_AlCertStatsServerCertRetransmissions_Object=MibTableColumn
alCertStatsServerCertRetransmissions=_AlCertStatsServerCertRetransmissions_Object((1,3,6,1,4,1,3076,2,1,2,27,2,1,5),_AlCertStatsServerCertRetransmissions_Type())
alCertStatsServerCertRetransmissions.setMaxAccess(_C)
if mibBuilder.loadTexts:alCertStatsServerCertRetransmissions.setStatus(_A)
_AlCertStatsServerCertRcvd_Type=Counter32
_AlCertStatsServerCertRcvd_Object=MibTableColumn
alCertStatsServerCertRcvd=_AlCertStatsServerCertRcvd_Object((1,3,6,1,4,1,3076,2,1,2,27,2,1,6),_AlCertStatsServerCertRcvd_Type())
alCertStatsServerCertRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:alCertStatsServerCertRcvd.setStatus(_A)
_AlCertStatsServerCertPendingRequests_Type=Gauge32
_AlCertStatsServerCertPendingRequests_Object=MibTableColumn
alCertStatsServerCertPendingRequests=_AlCertStatsServerCertPendingRequests_Object((1,3,6,1,4,1,3076,2,1,2,27,2,1,7),_AlCertStatsServerCertPendingRequests_Type())
alCertStatsServerCertPendingRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:alCertStatsServerCertPendingRequests.setStatus(_A)
_AlCertStatsServerCertTimeouts_Type=Counter32
_AlCertStatsServerCertTimeouts_Object=MibTableColumn
alCertStatsServerCertTimeouts=_AlCertStatsServerCertTimeouts_Object((1,3,6,1,4,1,3076,2,1,2,27,2,1,8),_AlCertStatsServerCertTimeouts_Type())
alCertStatsServerCertTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:alCertStatsServerCertTimeouts.setStatus(_A)
_AlCertStatsServerCRLRequests_Type=Counter32
_AlCertStatsServerCRLRequests_Object=MibTableColumn
alCertStatsServerCRLRequests=_AlCertStatsServerCRLRequests_Object((1,3,6,1,4,1,3076,2,1,2,27,2,1,9),_AlCertStatsServerCRLRequests_Type())
alCertStatsServerCRLRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:alCertStatsServerCRLRequests.setStatus(_A)
_AlCertStatsServerCRLRetransmissions_Type=Counter32
_AlCertStatsServerCRLRetransmissions_Object=MibTableColumn
alCertStatsServerCRLRetransmissions=_AlCertStatsServerCRLRetransmissions_Object((1,3,6,1,4,1,3076,2,1,2,27,2,1,10),_AlCertStatsServerCRLRetransmissions_Type())
alCertStatsServerCRLRetransmissions.setMaxAccess(_C)
if mibBuilder.loadTexts:alCertStatsServerCRLRetransmissions.setStatus(_A)
_AlCertStatsServerCRLRcvd_Type=Counter32
_AlCertStatsServerCRLRcvd_Object=MibTableColumn
alCertStatsServerCRLRcvd=_AlCertStatsServerCRLRcvd_Object((1,3,6,1,4,1,3076,2,1,2,27,2,1,11),_AlCertStatsServerCRLRcvd_Type())
alCertStatsServerCRLRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:alCertStatsServerCRLRcvd.setStatus(_A)
_AlCertStatsServerCRLPendingRequests_Type=Gauge32
_AlCertStatsServerCRLPendingRequests_Object=MibTableColumn
alCertStatsServerCRLPendingRequests=_AlCertStatsServerCRLPendingRequests_Object((1,3,6,1,4,1,3076,2,1,2,27,2,1,12),_AlCertStatsServerCRLPendingRequests_Type())
alCertStatsServerCRLPendingRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:alCertStatsServerCRLPendingRequests.setStatus(_A)
_AlCertStatsServerCRLTimeouts_Type=Counter32
_AlCertStatsServerCRLTimeouts_Object=MibTableColumn
alCertStatsServerCRLTimeouts=_AlCertStatsServerCRLTimeouts_Object((1,3,6,1,4,1,3076,2,1,2,27,2,1,13),_AlCertStatsServerCRLTimeouts_Type())
alCertStatsServerCRLTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:alCertStatsServerCRLTimeouts.setStatus(_A)
altigaCertStatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,27,2))
altigaCertStatsGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:altigaCertStatsGroup.setStatus(_A)
altigaCertStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,32,2,1,1,1))
altigaCertStatsMibCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:altigaCertStatsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'altigaCertStatsMibModule':altigaCertStatsMibModule,'altigaCertStatsMibConformance':altigaCertStatsMibConformance,'altigaCertStatsMibCompliances':altigaCertStatsMibCompliances,'altigaCertStatsMibCompliance':altigaCertStatsMibCompliance,_Q:altigaCertStatsGroup,'alStatsCertGlobal':alStatsCertGlobal,'alCertStatsServerTable':alCertStatsServerTable,'alCertStatsServerEntry':alCertStatsServerEntry,_D:alCertStatsServerIndex,_E:alCertStatsServerAddress,_F:alCertStatsServerPortNumber,_G:alCertStatsServerCertRequests,_H:alCertStatsServerCertRetransmissions,_I:alCertStatsServerCertRcvd,_J:alCertStatsServerCertPendingRequests,_K:alCertStatsServerCertTimeouts,_L:alCertStatsServerCRLRequests,_M:alCertStatsServerCRLRetransmissions,_N:alCertStatsServerCRLRcvd,_O:alCertStatsServerCRLPendingRequests,_P:alCertStatsServerCRLTimeouts})