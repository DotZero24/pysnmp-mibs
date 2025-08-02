_a='altigaHttpStatsGroup'
_Z='alHttpStatsSessionTotalConnections'
_Y='alHttpStatsSessionMaxConnections'
_X='alHttpStatsSessionActiveConnections'
_W='alHttpStatsSessionPacketsRcvd'
_V='alHttpStatsSessionPacketsSent'
_U='alHttpStatsSessionOctetsRcvd'
_T='alHttpStatsSessionOctetsSent'
_S='alHttpStatsSessionEncr'
_R='alHttpStatsSessionLoginTime'
_Q='alHttpStatsSessionStartTime'
_P='alHttpStatsSessionIpAddr'
_O='alHttpStatsSessionName'
_N='alHttpStatsTotalSessions'
_M='alHttpStatsTotalConnections'
_L='alHttpStatsMaxSessions'
_K='alHttpStatsActiveSessions'
_J='alHttpStatsMaxConnections'
_I='alHttpStatsActiveConnections'
_H='alHttpStatsPacketsRcvd'
_G='alHttpStatsPacketsSent'
_F='alHttpStatsOctetsRcvd'
_E='alHttpStatsOctetsSent'
_D='alHttpStatsSessionIndex'
_C='read-only'
_B='ALTIGA-HTTP-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alHttpMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alHttpMibModule')
alHttpGroup,alStatsHttp=mibBuilder.importSymbols('ALTIGA-MIB','alHttpGroup','alStatsHttp')
EncryptionAlgorithm,=mibBuilder.importSymbols('ALTIGA-SESSION-STATS-MIB','EncryptionAlgorithm')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
altigaHttpStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,12,2))
if mibBuilder.loadTexts:altigaHttpStatsMibModule.setRevisions(('2002-09-05 13:00','2002-07-10 00:00'))
_AltigaHttpStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaHttpStatsMibConformance=_AltigaHttpStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,12,2,1))
_AltigaHttpStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaHttpStatsMibCompliances=_AltigaHttpStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,12,2,1,1))
_AlStatsHttpGlobal_ObjectIdentity=ObjectIdentity
alStatsHttpGlobal=_AlStatsHttpGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,7,1))
_AlHttpStatsOctetsSent_Type=Counter32
_AlHttpStatsOctetsSent_Object=MibScalar
alHttpStatsOctetsSent=_AlHttpStatsOctetsSent_Object((1,3,6,1,4,1,3076,2,1,2,7,1,1),_AlHttpStatsOctetsSent_Type())
alHttpStatsOctetsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:alHttpStatsOctetsSent.setStatus(_A)
_AlHttpStatsOctetsRcvd_Type=Counter32
_AlHttpStatsOctetsRcvd_Object=MibScalar
alHttpStatsOctetsRcvd=_AlHttpStatsOctetsRcvd_Object((1,3,6,1,4,1,3076,2,1,2,7,1,2),_AlHttpStatsOctetsRcvd_Type())
alHttpStatsOctetsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:alHttpStatsOctetsRcvd.setStatus(_A)
_AlHttpStatsPacketsSent_Type=Counter32
_AlHttpStatsPacketsSent_Object=MibScalar
alHttpStatsPacketsSent=_AlHttpStatsPacketsSent_Object((1,3,6,1,4,1,3076,2,1,2,7,1,3),_AlHttpStatsPacketsSent_Type())
alHttpStatsPacketsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:alHttpStatsPacketsSent.setStatus(_A)
_AlHttpStatsPacketsRcvd_Type=Counter32
_AlHttpStatsPacketsRcvd_Object=MibScalar
alHttpStatsPacketsRcvd=_AlHttpStatsPacketsRcvd_Object((1,3,6,1,4,1,3076,2,1,2,7,1,4),_AlHttpStatsPacketsRcvd_Type())
alHttpStatsPacketsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:alHttpStatsPacketsRcvd.setStatus(_A)
_AlHttpStatsActiveConnections_Type=Gauge32
_AlHttpStatsActiveConnections_Object=MibScalar
alHttpStatsActiveConnections=_AlHttpStatsActiveConnections_Object((1,3,6,1,4,1,3076,2,1,2,7,1,5),_AlHttpStatsActiveConnections_Type())
alHttpStatsActiveConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:alHttpStatsActiveConnections.setStatus(_A)
_AlHttpStatsMaxConnections_Type=Counter32
_AlHttpStatsMaxConnections_Object=MibScalar
alHttpStatsMaxConnections=_AlHttpStatsMaxConnections_Object((1,3,6,1,4,1,3076,2,1,2,7,1,6),_AlHttpStatsMaxConnections_Type())
alHttpStatsMaxConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:alHttpStatsMaxConnections.setStatus(_A)
_AlHttpStatsActiveSessions_Type=Gauge32
_AlHttpStatsActiveSessions_Object=MibScalar
alHttpStatsActiveSessions=_AlHttpStatsActiveSessions_Object((1,3,6,1,4,1,3076,2,1,2,7,1,7),_AlHttpStatsActiveSessions_Type())
alHttpStatsActiveSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:alHttpStatsActiveSessions.setStatus(_A)
_AlHttpStatsMaxSessions_Type=Counter32
_AlHttpStatsMaxSessions_Object=MibScalar
alHttpStatsMaxSessions=_AlHttpStatsMaxSessions_Object((1,3,6,1,4,1,3076,2,1,2,7,1,8),_AlHttpStatsMaxSessions_Type())
alHttpStatsMaxSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:alHttpStatsMaxSessions.setStatus(_A)
_AlHttpStatsTotalConnections_Type=Counter32
_AlHttpStatsTotalConnections_Object=MibScalar
alHttpStatsTotalConnections=_AlHttpStatsTotalConnections_Object((1,3,6,1,4,1,3076,2,1,2,7,1,9),_AlHttpStatsTotalConnections_Type())
alHttpStatsTotalConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:alHttpStatsTotalConnections.setStatus(_A)
_AlHttpStatsTotalSessions_Type=Counter32
_AlHttpStatsTotalSessions_Object=MibScalar
alHttpStatsTotalSessions=_AlHttpStatsTotalSessions_Object((1,3,6,1,4,1,3076,2,1,2,7,1,10),_AlHttpStatsTotalSessions_Type())
alHttpStatsTotalSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:alHttpStatsTotalSessions.setStatus(_A)
_AlHttpStatsSessionTable_Object=MibTable
alHttpStatsSessionTable=_AlHttpStatsSessionTable_Object((1,3,6,1,4,1,3076,2,1,2,7,2))
if mibBuilder.loadTexts:alHttpStatsSessionTable.setStatus(_A)
_AlHttpStatsSessionEntry_Object=MibTableRow
alHttpStatsSessionEntry=_AlHttpStatsSessionEntry_Object((1,3,6,1,4,1,3076,2,1,2,7,2,1))
alHttpStatsSessionEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:alHttpStatsSessionEntry.setStatus(_A)
_AlHttpStatsSessionIndex_Type=Integer32
_AlHttpStatsSessionIndex_Object=MibTableColumn
alHttpStatsSessionIndex=_AlHttpStatsSessionIndex_Object((1,3,6,1,4,1,3076,2,1,2,7,2,1,1),_AlHttpStatsSessionIndex_Type())
alHttpStatsSessionIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alHttpStatsSessionIndex.setStatus(_A)
_AlHttpStatsSessionName_Type=DisplayString
_AlHttpStatsSessionName_Object=MibTableColumn
alHttpStatsSessionName=_AlHttpStatsSessionName_Object((1,3,6,1,4,1,3076,2,1,2,7,2,1,2),_AlHttpStatsSessionName_Type())
alHttpStatsSessionName.setMaxAccess(_C)
if mibBuilder.loadTexts:alHttpStatsSessionName.setStatus(_A)
_AlHttpStatsSessionIpAddr_Type=IpAddress
_AlHttpStatsSessionIpAddr_Object=MibTableColumn
alHttpStatsSessionIpAddr=_AlHttpStatsSessionIpAddr_Object((1,3,6,1,4,1,3076,2,1,2,7,2,1,3),_AlHttpStatsSessionIpAddr_Type())
alHttpStatsSessionIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:alHttpStatsSessionIpAddr.setStatus(_A)
_AlHttpStatsSessionStartTime_Type=TimeTicks
_AlHttpStatsSessionStartTime_Object=MibTableColumn
alHttpStatsSessionStartTime=_AlHttpStatsSessionStartTime_Object((1,3,6,1,4,1,3076,2,1,2,7,2,1,4),_AlHttpStatsSessionStartTime_Type())
alHttpStatsSessionStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alHttpStatsSessionStartTime.setStatus(_A)
_AlHttpStatsSessionLoginTime_Type=Unsigned32
_AlHttpStatsSessionLoginTime_Object=MibTableColumn
alHttpStatsSessionLoginTime=_AlHttpStatsSessionLoginTime_Object((1,3,6,1,4,1,3076,2,1,2,7,2,1,5),_AlHttpStatsSessionLoginTime_Type())
alHttpStatsSessionLoginTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alHttpStatsSessionLoginTime.setStatus(_A)
_AlHttpStatsSessionEncr_Type=EncryptionAlgorithm
_AlHttpStatsSessionEncr_Object=MibTableColumn
alHttpStatsSessionEncr=_AlHttpStatsSessionEncr_Object((1,3,6,1,4,1,3076,2,1,2,7,2,1,6),_AlHttpStatsSessionEncr_Type())
alHttpStatsSessionEncr.setMaxAccess(_C)
if mibBuilder.loadTexts:alHttpStatsSessionEncr.setStatus(_A)
_AlHttpStatsSessionOctetsSent_Type=Counter32
_AlHttpStatsSessionOctetsSent_Object=MibTableColumn
alHttpStatsSessionOctetsSent=_AlHttpStatsSessionOctetsSent_Object((1,3,6,1,4,1,3076,2,1,2,7,2,1,7),_AlHttpStatsSessionOctetsSent_Type())
alHttpStatsSessionOctetsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:alHttpStatsSessionOctetsSent.setStatus(_A)
_AlHttpStatsSessionOctetsRcvd_Type=Counter32
_AlHttpStatsSessionOctetsRcvd_Object=MibTableColumn
alHttpStatsSessionOctetsRcvd=_AlHttpStatsSessionOctetsRcvd_Object((1,3,6,1,4,1,3076,2,1,2,7,2,1,8),_AlHttpStatsSessionOctetsRcvd_Type())
alHttpStatsSessionOctetsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:alHttpStatsSessionOctetsRcvd.setStatus(_A)
_AlHttpStatsSessionPacketsSent_Type=Counter32
_AlHttpStatsSessionPacketsSent_Object=MibTableColumn
alHttpStatsSessionPacketsSent=_AlHttpStatsSessionPacketsSent_Object((1,3,6,1,4,1,3076,2,1,2,7,2,1,9),_AlHttpStatsSessionPacketsSent_Type())
alHttpStatsSessionPacketsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:alHttpStatsSessionPacketsSent.setStatus(_A)
_AlHttpStatsSessionPacketsRcvd_Type=Counter32
_AlHttpStatsSessionPacketsRcvd_Object=MibTableColumn
alHttpStatsSessionPacketsRcvd=_AlHttpStatsSessionPacketsRcvd_Object((1,3,6,1,4,1,3076,2,1,2,7,2,1,10),_AlHttpStatsSessionPacketsRcvd_Type())
alHttpStatsSessionPacketsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:alHttpStatsSessionPacketsRcvd.setStatus(_A)
_AlHttpStatsSessionActiveConnections_Type=Gauge32
_AlHttpStatsSessionActiveConnections_Object=MibTableColumn
alHttpStatsSessionActiveConnections=_AlHttpStatsSessionActiveConnections_Object((1,3,6,1,4,1,3076,2,1,2,7,2,1,11),_AlHttpStatsSessionActiveConnections_Type())
alHttpStatsSessionActiveConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:alHttpStatsSessionActiveConnections.setStatus(_A)
_AlHttpStatsSessionMaxConnections_Type=Counter32
_AlHttpStatsSessionMaxConnections_Object=MibTableColumn
alHttpStatsSessionMaxConnections=_AlHttpStatsSessionMaxConnections_Object((1,3,6,1,4,1,3076,2,1,2,7,2,1,12),_AlHttpStatsSessionMaxConnections_Type())
alHttpStatsSessionMaxConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:alHttpStatsSessionMaxConnections.setStatus(_A)
_AlHttpStatsSessionTotalConnections_Type=Counter32
_AlHttpStatsSessionTotalConnections_Object=MibTableColumn
alHttpStatsSessionTotalConnections=_AlHttpStatsSessionTotalConnections_Object((1,3,6,1,4,1,3076,2,1,2,7,2,1,13),_AlHttpStatsSessionTotalConnections_Type())
alHttpStatsSessionTotalConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:alHttpStatsSessionTotalConnections.setStatus(_A)
altigaHttpStatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,7,2))
altigaHttpStatsGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_D),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:altigaHttpStatsGroup.setStatus(_A)
altigaHttpStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,12,2,1,1,1))
altigaHttpStatsMibCompliance.setObjects((_B,_a))
if mibBuilder.loadTexts:altigaHttpStatsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'altigaHttpStatsMibModule':altigaHttpStatsMibModule,'altigaHttpStatsMibConformance':altigaHttpStatsMibConformance,'altigaHttpStatsMibCompliances':altigaHttpStatsMibCompliances,'altigaHttpStatsMibCompliance':altigaHttpStatsMibCompliance,_a:altigaHttpStatsGroup,'alStatsHttpGlobal':alStatsHttpGlobal,_E:alHttpStatsOctetsSent,_F:alHttpStatsOctetsRcvd,_G:alHttpStatsPacketsSent,_H:alHttpStatsPacketsRcvd,_I:alHttpStatsActiveConnections,_J:alHttpStatsMaxConnections,_K:alHttpStatsActiveSessions,_L:alHttpStatsMaxSessions,_M:alHttpStatsTotalConnections,_N:alHttpStatsTotalSessions,'alHttpStatsSessionTable':alHttpStatsSessionTable,'alHttpStatsSessionEntry':alHttpStatsSessionEntry,_D:alHttpStatsSessionIndex,_O:alHttpStatsSessionName,_P:alHttpStatsSessionIpAddr,_Q:alHttpStatsSessionStartTime,_R:alHttpStatsSessionLoginTime,_S:alHttpStatsSessionEncr,_T:alHttpStatsSessionOctetsSent,_U:alHttpStatsSessionOctetsRcvd,_V:alHttpStatsSessionPacketsSent,_W:alHttpStatsSessionPacketsRcvd,_X:alHttpStatsSessionActiveConnections,_Y:alHttpStatsSessionMaxConnections,_Z:alHttpStatsSessionTotalConnections})