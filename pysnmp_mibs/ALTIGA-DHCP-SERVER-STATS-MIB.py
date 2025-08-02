_Q='altigaDhcpServerStatsGroup'
_P='alDhcpServerStatsSessHostName'
_O='alDhcpServerStatsSessMacAddr'
_N='alDhcpServerStatsSessLeaseExpire'
_M='alDhcpServerStatsSessIpAddr'
_L='alDhcpServerStatsSessRowStatus'
_K='alDhcpServerStatsReqTimeouts'
_J='alDhcpServerStatsNaksSent'
_I='alDhcpServerStatsAcksSent'
_H='alDhcpServerStatsOffersSent'
_G='alDhcpServerStatsDiscoversRcvd'
_F='alDhcpServerStatsMaximumLeases'
_E='alDhcpServerStatsActiveLeases'
_D='alDhcpServerStatsSessId'
_C='read-only'
_B='ALTIGA-DHCP-SERVER-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alDhcpServerMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alDhcpServerMibModule')
alDhcpServerGroup,alStatsDhcpServer=mibBuilder.importSymbols('ALTIGA-MIB','alDhcpServerGroup','alStatsDhcpServer')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
altigaDhcpServerStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,42,2))
if mibBuilder.loadTexts:altigaDhcpServerStatsMibModule.setRevisions(('2002-09-05 13:00','2002-07-10 00:00'))
_AltigaDhcpServerStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaDhcpServerStatsMibConformance=_AltigaDhcpServerStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,42,2,1))
_AltigaDhcpServerStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaDhcpServerStatsMibCompliances=_AltigaDhcpServerStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,42,2,1,1))
_AlStatsDhcpServerGlobal_ObjectIdentity=ObjectIdentity
alStatsDhcpServerGlobal=_AlStatsDhcpServerGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,37,1))
_AlDhcpServerStatsActiveLeases_Type=Gauge32
_AlDhcpServerStatsActiveLeases_Object=MibScalar
alDhcpServerStatsActiveLeases=_AlDhcpServerStatsActiveLeases_Object((1,3,6,1,4,1,3076,2,1,2,37,1,1),_AlDhcpServerStatsActiveLeases_Type())
alDhcpServerStatsActiveLeases.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpServerStatsActiveLeases.setStatus(_A)
_AlDhcpServerStatsMaximumLeases_Type=Counter32
_AlDhcpServerStatsMaximumLeases_Object=MibScalar
alDhcpServerStatsMaximumLeases=_AlDhcpServerStatsMaximumLeases_Object((1,3,6,1,4,1,3076,2,1,2,37,1,2),_AlDhcpServerStatsMaximumLeases_Type())
alDhcpServerStatsMaximumLeases.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpServerStatsMaximumLeases.setStatus(_A)
_AlDhcpServerStatsDiscoversRcvd_Type=Counter32
_AlDhcpServerStatsDiscoversRcvd_Object=MibScalar
alDhcpServerStatsDiscoversRcvd=_AlDhcpServerStatsDiscoversRcvd_Object((1,3,6,1,4,1,3076,2,1,2,37,1,3),_AlDhcpServerStatsDiscoversRcvd_Type())
alDhcpServerStatsDiscoversRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpServerStatsDiscoversRcvd.setStatus(_A)
_AlDhcpServerStatsOffersSent_Type=Counter32
_AlDhcpServerStatsOffersSent_Object=MibScalar
alDhcpServerStatsOffersSent=_AlDhcpServerStatsOffersSent_Object((1,3,6,1,4,1,3076,2,1,2,37,1,4),_AlDhcpServerStatsOffersSent_Type())
alDhcpServerStatsOffersSent.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpServerStatsOffersSent.setStatus(_A)
_AlDhcpServerStatsAcksSent_Type=Counter32
_AlDhcpServerStatsAcksSent_Object=MibScalar
alDhcpServerStatsAcksSent=_AlDhcpServerStatsAcksSent_Object((1,3,6,1,4,1,3076,2,1,2,37,1,5),_AlDhcpServerStatsAcksSent_Type())
alDhcpServerStatsAcksSent.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpServerStatsAcksSent.setStatus(_A)
_AlDhcpServerStatsNaksSent_Type=Counter32
_AlDhcpServerStatsNaksSent_Object=MibScalar
alDhcpServerStatsNaksSent=_AlDhcpServerStatsNaksSent_Object((1,3,6,1,4,1,3076,2,1,2,37,1,6),_AlDhcpServerStatsNaksSent_Type())
alDhcpServerStatsNaksSent.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpServerStatsNaksSent.setStatus(_A)
_AlDhcpServerStatsReqTimeouts_Type=Counter32
_AlDhcpServerStatsReqTimeouts_Object=MibScalar
alDhcpServerStatsReqTimeouts=_AlDhcpServerStatsReqTimeouts_Object((1,3,6,1,4,1,3076,2,1,2,37,1,7),_AlDhcpServerStatsReqTimeouts_Type())
alDhcpServerStatsReqTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpServerStatsReqTimeouts.setStatus(_A)
_AlDhcpServerStatsSessTable_Object=MibTable
alDhcpServerStatsSessTable=_AlDhcpServerStatsSessTable_Object((1,3,6,1,4,1,3076,2,1,2,37,2))
if mibBuilder.loadTexts:alDhcpServerStatsSessTable.setStatus(_A)
_AlDhcpServerStatsSessEntry_Object=MibTableRow
alDhcpServerStatsSessEntry=_AlDhcpServerStatsSessEntry_Object((1,3,6,1,4,1,3076,2,1,2,37,2,1))
alDhcpServerStatsSessEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:alDhcpServerStatsSessEntry.setStatus(_A)
_AlDhcpServerStatsSessRowStatus_Type=RowStatus
_AlDhcpServerStatsSessRowStatus_Object=MibTableColumn
alDhcpServerStatsSessRowStatus=_AlDhcpServerStatsSessRowStatus_Object((1,3,6,1,4,1,3076,2,1,2,37,2,1,1),_AlDhcpServerStatsSessRowStatus_Type())
alDhcpServerStatsSessRowStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:alDhcpServerStatsSessRowStatus.setStatus(_A)
_AlDhcpServerStatsSessId_Type=Integer32
_AlDhcpServerStatsSessId_Object=MibTableColumn
alDhcpServerStatsSessId=_AlDhcpServerStatsSessId_Object((1,3,6,1,4,1,3076,2,1,2,37,2,1,2),_AlDhcpServerStatsSessId_Type())
alDhcpServerStatsSessId.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpServerStatsSessId.setStatus(_A)
_AlDhcpServerStatsSessIpAddr_Type=IpAddress
_AlDhcpServerStatsSessIpAddr_Object=MibTableColumn
alDhcpServerStatsSessIpAddr=_AlDhcpServerStatsSessIpAddr_Object((1,3,6,1,4,1,3076,2,1,2,37,2,1,3),_AlDhcpServerStatsSessIpAddr_Type())
alDhcpServerStatsSessIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpServerStatsSessIpAddr.setStatus(_A)
_AlDhcpServerStatsSessLeaseExpire_Type=Gauge32
_AlDhcpServerStatsSessLeaseExpire_Object=MibTableColumn
alDhcpServerStatsSessLeaseExpire=_AlDhcpServerStatsSessLeaseExpire_Object((1,3,6,1,4,1,3076,2,1,2,37,2,1,4),_AlDhcpServerStatsSessLeaseExpire_Type())
alDhcpServerStatsSessLeaseExpire.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpServerStatsSessLeaseExpire.setStatus(_A)
_AlDhcpServerStatsSessMacAddr_Type=MacAddress
_AlDhcpServerStatsSessMacAddr_Object=MibTableColumn
alDhcpServerStatsSessMacAddr=_AlDhcpServerStatsSessMacAddr_Object((1,3,6,1,4,1,3076,2,1,2,37,2,1,5),_AlDhcpServerStatsSessMacAddr_Type())
alDhcpServerStatsSessMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpServerStatsSessMacAddr.setStatus(_A)
_AlDhcpServerStatsSessHostName_Type=DisplayString
_AlDhcpServerStatsSessHostName_Object=MibTableColumn
alDhcpServerStatsSessHostName=_AlDhcpServerStatsSessHostName_Object((1,3,6,1,4,1,3076,2,1,2,37,2,1,6),_AlDhcpServerStatsSessHostName_Type())
alDhcpServerStatsSessHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpServerStatsSessHostName.setStatus(_A)
altigaDhcpServerStatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,37,2))
altigaDhcpServerStatsGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_D),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:altigaDhcpServerStatsGroup.setStatus(_A)
altigaDhcpServerStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,42,2,1,1,1))
altigaDhcpServerStatsMibCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:altigaDhcpServerStatsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'altigaDhcpServerStatsMibModule':altigaDhcpServerStatsMibModule,'altigaDhcpServerStatsMibConformance':altigaDhcpServerStatsMibConformance,'altigaDhcpServerStatsMibCompliances':altigaDhcpServerStatsMibCompliances,'altigaDhcpServerStatsMibCompliance':altigaDhcpServerStatsMibCompliance,_Q:altigaDhcpServerStatsGroup,'alStatsDhcpServerGlobal':alStatsDhcpServerGlobal,_E:alDhcpServerStatsActiveLeases,_F:alDhcpServerStatsMaximumLeases,_G:alDhcpServerStatsDiscoversRcvd,_H:alDhcpServerStatsOffersSent,_I:alDhcpServerStatsAcksSent,_J:alDhcpServerStatsNaksSent,_K:alDhcpServerStatsReqTimeouts,'alDhcpServerStatsSessTable':alDhcpServerStatsSessTable,'alDhcpServerStatsSessEntry':alDhcpServerStatsSessEntry,_L:alDhcpServerStatsSessRowStatus,_D:alDhcpServerStatsSessId,_M:alDhcpServerStatsSessIpAddr,_N:alDhcpServerStatsSessLeaseExpire,_O:alDhcpServerStatsSessMacAddr,_P:alDhcpServerStatsSessHostName})