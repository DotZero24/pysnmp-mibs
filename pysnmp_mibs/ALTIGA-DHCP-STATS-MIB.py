_e='altigaDhcpStatsGroup'
_d='alDhcpStatsSessSrvrIpAddr'
_c='alDhcpStatsSessClientId'
_b='alDhcpStatsSessState'
_a='alDhcpStatsSessLeaseExpire'
_Z='alDhcpStatsSessLeaseDuration'
_Y='alDhcpStatsSessUpTime'
_X='alDhcpStatsSessKey'
_W='alDhcpStatsSessId'
_V='alDhcpStatsSessRowStatus'
_U='alDhcpStatsLeaseTimeouts'
_T='alDhcpStatsApiRequests'
_S='alDhcpStatsT2Timeouts'
_R='alDhcpStatsT1Timeouts'
_Q='alDhcpStatsT2NaksRcvd'
_P='alDhcpStatsT2AcksRcvd'
_O='alDhcpStatsT1NaksRcvd'
_N='alDhcpStatsT1AcksRcvd'
_M='alDhcpStatsInitNaksRcvd'
_L='alDhcpStatsInitAcksRcvd'
_K='alDhcpStatsT2RequestsSent'
_J='alDhcpStatsT1RequestsSent'
_I='alDhcpStatsInitRequestsSent'
_H='alDhcpStatsOffersRcvd'
_G='alDhcpStatsDiscoversSent'
_F='alDhcpStatsMaximumLeases'
_E='alDhcpStatsActiveLeases'
_D='alDhcpStatsSessIpAddr'
_C='read-only'
_B='ALTIGA-DHCP-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alDhcpMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alDhcpMibModule')
alDhcpGroup,alStatsDhcp=mibBuilder.importSymbols('ALTIGA-MIB','alDhcpGroup','alStatsDhcp')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
altigaDhcpStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,25,2))
if mibBuilder.loadTexts:altigaDhcpStatsMibModule.setRevisions(('2002-09-05 13:00','2002-07-10 00:00'))
_AltigaDhcpStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaDhcpStatsMibConformance=_AltigaDhcpStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,25,2,1))
_AltigaDhcpStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaDhcpStatsMibCompliances=_AltigaDhcpStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,25,2,1,1))
_AlStatsDhcpGlobal_ObjectIdentity=ObjectIdentity
alStatsDhcpGlobal=_AlStatsDhcpGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,20,1))
_AlDhcpStatsActiveLeases_Type=Gauge32
_AlDhcpStatsActiveLeases_Object=MibScalar
alDhcpStatsActiveLeases=_AlDhcpStatsActiveLeases_Object((1,3,6,1,4,1,3076,2,1,2,20,1,1),_AlDhcpStatsActiveLeases_Type())
alDhcpStatsActiveLeases.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsActiveLeases.setStatus(_A)
_AlDhcpStatsMaximumLeases_Type=Gauge32
_AlDhcpStatsMaximumLeases_Object=MibScalar
alDhcpStatsMaximumLeases=_AlDhcpStatsMaximumLeases_Object((1,3,6,1,4,1,3076,2,1,2,20,1,2),_AlDhcpStatsMaximumLeases_Type())
alDhcpStatsMaximumLeases.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsMaximumLeases.setStatus(_A)
_AlDhcpStatsDiscoversSent_Type=Gauge32
_AlDhcpStatsDiscoversSent_Object=MibScalar
alDhcpStatsDiscoversSent=_AlDhcpStatsDiscoversSent_Object((1,3,6,1,4,1,3076,2,1,2,20,1,3),_AlDhcpStatsDiscoversSent_Type())
alDhcpStatsDiscoversSent.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsDiscoversSent.setStatus(_A)
_AlDhcpStatsOffersRcvd_Type=Gauge32
_AlDhcpStatsOffersRcvd_Object=MibScalar
alDhcpStatsOffersRcvd=_AlDhcpStatsOffersRcvd_Object((1,3,6,1,4,1,3076,2,1,2,20,1,4),_AlDhcpStatsOffersRcvd_Type())
alDhcpStatsOffersRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsOffersRcvd.setStatus(_A)
_AlDhcpStatsInitRequestsSent_Type=Gauge32
_AlDhcpStatsInitRequestsSent_Object=MibScalar
alDhcpStatsInitRequestsSent=_AlDhcpStatsInitRequestsSent_Object((1,3,6,1,4,1,3076,2,1,2,20,1,5),_AlDhcpStatsInitRequestsSent_Type())
alDhcpStatsInitRequestsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsInitRequestsSent.setStatus(_A)
_AlDhcpStatsT1RequestsSent_Type=Gauge32
_AlDhcpStatsT1RequestsSent_Object=MibScalar
alDhcpStatsT1RequestsSent=_AlDhcpStatsT1RequestsSent_Object((1,3,6,1,4,1,3076,2,1,2,20,1,6),_AlDhcpStatsT1RequestsSent_Type())
alDhcpStatsT1RequestsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsT1RequestsSent.setStatus(_A)
_AlDhcpStatsT2RequestsSent_Type=Gauge32
_AlDhcpStatsT2RequestsSent_Object=MibScalar
alDhcpStatsT2RequestsSent=_AlDhcpStatsT2RequestsSent_Object((1,3,6,1,4,1,3076,2,1,2,20,1,7),_AlDhcpStatsT2RequestsSent_Type())
alDhcpStatsT2RequestsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsT2RequestsSent.setStatus(_A)
_AlDhcpStatsInitAcksRcvd_Type=Gauge32
_AlDhcpStatsInitAcksRcvd_Object=MibScalar
alDhcpStatsInitAcksRcvd=_AlDhcpStatsInitAcksRcvd_Object((1,3,6,1,4,1,3076,2,1,2,20,1,8),_AlDhcpStatsInitAcksRcvd_Type())
alDhcpStatsInitAcksRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsInitAcksRcvd.setStatus(_A)
_AlDhcpStatsInitNaksRcvd_Type=Gauge32
_AlDhcpStatsInitNaksRcvd_Object=MibScalar
alDhcpStatsInitNaksRcvd=_AlDhcpStatsInitNaksRcvd_Object((1,3,6,1,4,1,3076,2,1,2,20,1,9),_AlDhcpStatsInitNaksRcvd_Type())
alDhcpStatsInitNaksRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsInitNaksRcvd.setStatus(_A)
_AlDhcpStatsT1AcksRcvd_Type=Gauge32
_AlDhcpStatsT1AcksRcvd_Object=MibScalar
alDhcpStatsT1AcksRcvd=_AlDhcpStatsT1AcksRcvd_Object((1,3,6,1,4,1,3076,2,1,2,20,1,10),_AlDhcpStatsT1AcksRcvd_Type())
alDhcpStatsT1AcksRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsT1AcksRcvd.setStatus(_A)
_AlDhcpStatsT1NaksRcvd_Type=Gauge32
_AlDhcpStatsT1NaksRcvd_Object=MibScalar
alDhcpStatsT1NaksRcvd=_AlDhcpStatsT1NaksRcvd_Object((1,3,6,1,4,1,3076,2,1,2,20,1,11),_AlDhcpStatsT1NaksRcvd_Type())
alDhcpStatsT1NaksRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsT1NaksRcvd.setStatus(_A)
_AlDhcpStatsT2AcksRcvd_Type=Gauge32
_AlDhcpStatsT2AcksRcvd_Object=MibScalar
alDhcpStatsT2AcksRcvd=_AlDhcpStatsT2AcksRcvd_Object((1,3,6,1,4,1,3076,2,1,2,20,1,12),_AlDhcpStatsT2AcksRcvd_Type())
alDhcpStatsT2AcksRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsT2AcksRcvd.setStatus(_A)
_AlDhcpStatsT2NaksRcvd_Type=Gauge32
_AlDhcpStatsT2NaksRcvd_Object=MibScalar
alDhcpStatsT2NaksRcvd=_AlDhcpStatsT2NaksRcvd_Object((1,3,6,1,4,1,3076,2,1,2,20,1,13),_AlDhcpStatsT2NaksRcvd_Type())
alDhcpStatsT2NaksRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsT2NaksRcvd.setStatus(_A)
_AlDhcpStatsT1Timeouts_Type=Gauge32
_AlDhcpStatsT1Timeouts_Object=MibScalar
alDhcpStatsT1Timeouts=_AlDhcpStatsT1Timeouts_Object((1,3,6,1,4,1,3076,2,1,2,20,1,14),_AlDhcpStatsT1Timeouts_Type())
alDhcpStatsT1Timeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsT1Timeouts.setStatus(_A)
_AlDhcpStatsT2Timeouts_Type=Gauge32
_AlDhcpStatsT2Timeouts_Object=MibScalar
alDhcpStatsT2Timeouts=_AlDhcpStatsT2Timeouts_Object((1,3,6,1,4,1,3076,2,1,2,20,1,15),_AlDhcpStatsT2Timeouts_Type())
alDhcpStatsT2Timeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsT2Timeouts.setStatus(_A)
_AlDhcpStatsApiRequests_Type=Gauge32
_AlDhcpStatsApiRequests_Object=MibScalar
alDhcpStatsApiRequests=_AlDhcpStatsApiRequests_Object((1,3,6,1,4,1,3076,2,1,2,20,1,16),_AlDhcpStatsApiRequests_Type())
alDhcpStatsApiRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsApiRequests.setStatus(_A)
_AlDhcpStatsLeaseTimeouts_Type=Gauge32
_AlDhcpStatsLeaseTimeouts_Object=MibScalar
alDhcpStatsLeaseTimeouts=_AlDhcpStatsLeaseTimeouts_Object((1,3,6,1,4,1,3076,2,1,2,20,1,17),_AlDhcpStatsLeaseTimeouts_Type())
alDhcpStatsLeaseTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsLeaseTimeouts.setStatus(_A)
_AlDhcpStatsSessTable_Object=MibTable
alDhcpStatsSessTable=_AlDhcpStatsSessTable_Object((1,3,6,1,4,1,3076,2,1,2,20,2))
if mibBuilder.loadTexts:alDhcpStatsSessTable.setStatus(_A)
_AlDhcpStatsSessEntry_Object=MibTableRow
alDhcpStatsSessEntry=_AlDhcpStatsSessEntry_Object((1,3,6,1,4,1,3076,2,1,2,20,2,1))
alDhcpStatsSessEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:alDhcpStatsSessEntry.setStatus(_A)
_AlDhcpStatsSessRowStatus_Type=RowStatus
_AlDhcpStatsSessRowStatus_Object=MibTableColumn
alDhcpStatsSessRowStatus=_AlDhcpStatsSessRowStatus_Object((1,3,6,1,4,1,3076,2,1,2,20,2,1,1),_AlDhcpStatsSessRowStatus_Type())
alDhcpStatsSessRowStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:alDhcpStatsSessRowStatus.setStatus(_A)
_AlDhcpStatsSessId_Type=Integer32
_AlDhcpStatsSessId_Object=MibTableColumn
alDhcpStatsSessId=_AlDhcpStatsSessId_Object((1,3,6,1,4,1,3076,2,1,2,20,2,1,2),_AlDhcpStatsSessId_Type())
alDhcpStatsSessId.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsSessId.setStatus(_A)
_AlDhcpStatsSessKey_Type=Integer32
_AlDhcpStatsSessKey_Object=MibTableColumn
alDhcpStatsSessKey=_AlDhcpStatsSessKey_Object((1,3,6,1,4,1,3076,2,1,2,20,2,1,3),_AlDhcpStatsSessKey_Type())
alDhcpStatsSessKey.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsSessKey.setStatus(_A)
_AlDhcpStatsSessIpAddr_Type=IpAddress
_AlDhcpStatsSessIpAddr_Object=MibTableColumn
alDhcpStatsSessIpAddr=_AlDhcpStatsSessIpAddr_Object((1,3,6,1,4,1,3076,2,1,2,20,2,1,4),_AlDhcpStatsSessIpAddr_Type())
alDhcpStatsSessIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsSessIpAddr.setStatus(_A)
_AlDhcpStatsSessUpTime_Type=Integer32
_AlDhcpStatsSessUpTime_Object=MibTableColumn
alDhcpStatsSessUpTime=_AlDhcpStatsSessUpTime_Object((1,3,6,1,4,1,3076,2,1,2,20,2,1,5),_AlDhcpStatsSessUpTime_Type())
alDhcpStatsSessUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsSessUpTime.setStatus(_A)
_AlDhcpStatsSessLeaseDuration_Type=Integer32
_AlDhcpStatsSessLeaseDuration_Object=MibTableColumn
alDhcpStatsSessLeaseDuration=_AlDhcpStatsSessLeaseDuration_Object((1,3,6,1,4,1,3076,2,1,2,20,2,1,6),_AlDhcpStatsSessLeaseDuration_Type())
alDhcpStatsSessLeaseDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsSessLeaseDuration.setStatus(_A)
_AlDhcpStatsSessLeaseExpire_Type=Integer32
_AlDhcpStatsSessLeaseExpire_Object=MibTableColumn
alDhcpStatsSessLeaseExpire=_AlDhcpStatsSessLeaseExpire_Object((1,3,6,1,4,1,3076,2,1,2,20,2,1,7),_AlDhcpStatsSessLeaseExpire_Type())
alDhcpStatsSessLeaseExpire.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsSessLeaseExpire.setStatus(_A)
_AlDhcpStatsSessState_Type=DisplayString
_AlDhcpStatsSessState_Object=MibTableColumn
alDhcpStatsSessState=_AlDhcpStatsSessState_Object((1,3,6,1,4,1,3076,2,1,2,20,2,1,8),_AlDhcpStatsSessState_Type())
alDhcpStatsSessState.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsSessState.setStatus(_A)
_AlDhcpStatsSessClientId_Type=DisplayString
_AlDhcpStatsSessClientId_Object=MibTableColumn
alDhcpStatsSessClientId=_AlDhcpStatsSessClientId_Object((1,3,6,1,4,1,3076,2,1,2,20,2,1,9),_AlDhcpStatsSessClientId_Type())
alDhcpStatsSessClientId.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsSessClientId.setStatus(_A)
_AlDhcpStatsSessSrvrIpAddr_Type=IpAddress
_AlDhcpStatsSessSrvrIpAddr_Object=MibTableColumn
alDhcpStatsSessSrvrIpAddr=_AlDhcpStatsSessSrvrIpAddr_Object((1,3,6,1,4,1,3076,2,1,2,20,2,1,10),_AlDhcpStatsSessSrvrIpAddr_Type())
alDhcpStatsSessSrvrIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:alDhcpStatsSessSrvrIpAddr.setStatus(_A)
altigaDhcpStatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,20,2))
altigaDhcpStatsGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_D),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:altigaDhcpStatsGroup.setStatus(_A)
altigaDhcpStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,25,2,1,1,1))
altigaDhcpStatsMibCompliance.setObjects((_B,_e))
if mibBuilder.loadTexts:altigaDhcpStatsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'altigaDhcpStatsMibModule':altigaDhcpStatsMibModule,'altigaDhcpStatsMibConformance':altigaDhcpStatsMibConformance,'altigaDhcpStatsMibCompliances':altigaDhcpStatsMibCompliances,'altigaDhcpStatsMibCompliance':altigaDhcpStatsMibCompliance,_e:altigaDhcpStatsGroup,'alStatsDhcpGlobal':alStatsDhcpGlobal,_E:alDhcpStatsActiveLeases,_F:alDhcpStatsMaximumLeases,_G:alDhcpStatsDiscoversSent,_H:alDhcpStatsOffersRcvd,_I:alDhcpStatsInitRequestsSent,_J:alDhcpStatsT1RequestsSent,_K:alDhcpStatsT2RequestsSent,_L:alDhcpStatsInitAcksRcvd,_M:alDhcpStatsInitNaksRcvd,_N:alDhcpStatsT1AcksRcvd,_O:alDhcpStatsT1NaksRcvd,_P:alDhcpStatsT2AcksRcvd,_Q:alDhcpStatsT2NaksRcvd,_R:alDhcpStatsT1Timeouts,_S:alDhcpStatsT2Timeouts,_T:alDhcpStatsApiRequests,_U:alDhcpStatsLeaseTimeouts,'alDhcpStatsSessTable':alDhcpStatsSessTable,'alDhcpStatsSessEntry':alDhcpStatsSessEntry,_V:alDhcpStatsSessRowStatus,_W:alDhcpStatsSessId,_X:alDhcpStatsSessKey,_D:alDhcpStatsSessIpAddr,_Y:alDhcpStatsSessUpTime,_Z:alDhcpStatsSessLeaseDuration,_a:alDhcpStatsSessLeaseExpire,_b:alDhcpStatsSessState,_c:alDhcpStatsSessClientId,_d:alDhcpStatsSessSrvrIpAddr})