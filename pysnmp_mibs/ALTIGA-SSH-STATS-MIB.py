_V='altigaSshStatsGroup'
_U='alSshStatsSessionPacketsRcvd'
_T='alSshStatsSessionPacketsSent'
_S='alSshStatsSessionOctetsRcvd'
_R='alSshStatsSessionOctetsSent'
_Q='alSshStatsSessionEncr'
_P='alSshStatsSessionLoginTime'
_O='alSshStatsSessionStartTime'
_N='alSshStatsSessionPort'
_M='alSshStatsSessionIpAddr'
_L='alSshStatsSessionName'
_K='alSshStatsMaxSessions'
_J='alSshStatsActiveSessions'
_I='alSshStatsTotalSessions'
_H='alSshStatsPacketsRcvd'
_G='alSshStatsPacketsSent'
_F='alSshStatsOctetsRcvd'
_E='alSshStatsOctetsSent'
_D='alSshStatsSessionIndex'
_C='read-only'
_B='ALTIGA-SSH-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alSshMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alSshMibModule')
alSshGroup,alStatsSsh=mibBuilder.importSymbols('ALTIGA-MIB','alSshGroup','alStatsSsh')
EncryptionAlgorithm,=mibBuilder.importSymbols('ALTIGA-SESSION-STATS-MIB','EncryptionAlgorithm')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
altigaSshStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,40,2))
if mibBuilder.loadTexts:altigaSshStatsMibModule.setRevisions(('2002-09-05 13:00','2002-07-10 00:00'))
_AltigaSshStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaSshStatsMibConformance=_AltigaSshStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,40,2,1))
_AltigaSshStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaSshStatsMibCompliances=_AltigaSshStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,40,2,1,1))
_AlStatsSshGlobal_ObjectIdentity=ObjectIdentity
alStatsSshGlobal=_AlStatsSshGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,35,1))
_AlSshStatsOctetsSent_Type=Counter32
_AlSshStatsOctetsSent_Object=MibScalar
alSshStatsOctetsSent=_AlSshStatsOctetsSent_Object((1,3,6,1,4,1,3076,2,1,2,35,1,1),_AlSshStatsOctetsSent_Type())
alSshStatsOctetsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:alSshStatsOctetsSent.setStatus(_A)
_AlSshStatsOctetsRcvd_Type=Counter32
_AlSshStatsOctetsRcvd_Object=MibScalar
alSshStatsOctetsRcvd=_AlSshStatsOctetsRcvd_Object((1,3,6,1,4,1,3076,2,1,2,35,1,2),_AlSshStatsOctetsRcvd_Type())
alSshStatsOctetsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:alSshStatsOctetsRcvd.setStatus(_A)
_AlSshStatsPacketsSent_Type=Counter32
_AlSshStatsPacketsSent_Object=MibScalar
alSshStatsPacketsSent=_AlSshStatsPacketsSent_Object((1,3,6,1,4,1,3076,2,1,2,35,1,3),_AlSshStatsPacketsSent_Type())
alSshStatsPacketsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:alSshStatsPacketsSent.setStatus(_A)
_AlSshStatsPacketsRcvd_Type=Counter32
_AlSshStatsPacketsRcvd_Object=MibScalar
alSshStatsPacketsRcvd=_AlSshStatsPacketsRcvd_Object((1,3,6,1,4,1,3076,2,1,2,35,1,4),_AlSshStatsPacketsRcvd_Type())
alSshStatsPacketsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:alSshStatsPacketsRcvd.setStatus(_A)
_AlSshStatsTotalSessions_Type=Counter32
_AlSshStatsTotalSessions_Object=MibScalar
alSshStatsTotalSessions=_AlSshStatsTotalSessions_Object((1,3,6,1,4,1,3076,2,1,2,35,1,5),_AlSshStatsTotalSessions_Type())
alSshStatsTotalSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:alSshStatsTotalSessions.setStatus(_A)
_AlSshStatsActiveSessions_Type=Gauge32
_AlSshStatsActiveSessions_Object=MibScalar
alSshStatsActiveSessions=_AlSshStatsActiveSessions_Object((1,3,6,1,4,1,3076,2,1,2,35,1,6),_AlSshStatsActiveSessions_Type())
alSshStatsActiveSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:alSshStatsActiveSessions.setStatus(_A)
_AlSshStatsMaxSessions_Type=Counter32
_AlSshStatsMaxSessions_Object=MibScalar
alSshStatsMaxSessions=_AlSshStatsMaxSessions_Object((1,3,6,1,4,1,3076,2,1,2,35,1,7),_AlSshStatsMaxSessions_Type())
alSshStatsMaxSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:alSshStatsMaxSessions.setStatus(_A)
_AlSshStatsSessionTable_Object=MibTable
alSshStatsSessionTable=_AlSshStatsSessionTable_Object((1,3,6,1,4,1,3076,2,1,2,35,2))
if mibBuilder.loadTexts:alSshStatsSessionTable.setStatus(_A)
_AlSshStatsSessionEntry_Object=MibTableRow
alSshStatsSessionEntry=_AlSshStatsSessionEntry_Object((1,3,6,1,4,1,3076,2,1,2,35,2,1))
alSshStatsSessionEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:alSshStatsSessionEntry.setStatus(_A)
_AlSshStatsSessionIndex_Type=Integer32
_AlSshStatsSessionIndex_Object=MibTableColumn
alSshStatsSessionIndex=_AlSshStatsSessionIndex_Object((1,3,6,1,4,1,3076,2,1,2,35,2,1,1),_AlSshStatsSessionIndex_Type())
alSshStatsSessionIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alSshStatsSessionIndex.setStatus(_A)
_AlSshStatsSessionName_Type=DisplayString
_AlSshStatsSessionName_Object=MibTableColumn
alSshStatsSessionName=_AlSshStatsSessionName_Object((1,3,6,1,4,1,3076,2,1,2,35,2,1,2),_AlSshStatsSessionName_Type())
alSshStatsSessionName.setMaxAccess(_C)
if mibBuilder.loadTexts:alSshStatsSessionName.setStatus(_A)
_AlSshStatsSessionIpAddr_Type=IpAddress
_AlSshStatsSessionIpAddr_Object=MibTableColumn
alSshStatsSessionIpAddr=_AlSshStatsSessionIpAddr_Object((1,3,6,1,4,1,3076,2,1,2,35,2,1,3),_AlSshStatsSessionIpAddr_Type())
alSshStatsSessionIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:alSshStatsSessionIpAddr.setStatus(_A)
_AlSshStatsSessionPort_Type=Unsigned32
_AlSshStatsSessionPort_Object=MibTableColumn
alSshStatsSessionPort=_AlSshStatsSessionPort_Object((1,3,6,1,4,1,3076,2,1,2,35,2,1,4),_AlSshStatsSessionPort_Type())
alSshStatsSessionPort.setMaxAccess(_C)
if mibBuilder.loadTexts:alSshStatsSessionPort.setStatus(_A)
_AlSshStatsSessionStartTime_Type=TimeTicks
_AlSshStatsSessionStartTime_Object=MibTableColumn
alSshStatsSessionStartTime=_AlSshStatsSessionStartTime_Object((1,3,6,1,4,1,3076,2,1,2,35,2,1,5),_AlSshStatsSessionStartTime_Type())
alSshStatsSessionStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alSshStatsSessionStartTime.setStatus(_A)
_AlSshStatsSessionLoginTime_Type=Unsigned32
_AlSshStatsSessionLoginTime_Object=MibTableColumn
alSshStatsSessionLoginTime=_AlSshStatsSessionLoginTime_Object((1,3,6,1,4,1,3076,2,1,2,35,2,1,6),_AlSshStatsSessionLoginTime_Type())
alSshStatsSessionLoginTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alSshStatsSessionLoginTime.setStatus(_A)
_AlSshStatsSessionEncr_Type=EncryptionAlgorithm
_AlSshStatsSessionEncr_Object=MibTableColumn
alSshStatsSessionEncr=_AlSshStatsSessionEncr_Object((1,3,6,1,4,1,3076,2,1,2,35,2,1,7),_AlSshStatsSessionEncr_Type())
alSshStatsSessionEncr.setMaxAccess(_C)
if mibBuilder.loadTexts:alSshStatsSessionEncr.setStatus(_A)
_AlSshStatsSessionOctetsSent_Type=Counter32
_AlSshStatsSessionOctetsSent_Object=MibTableColumn
alSshStatsSessionOctetsSent=_AlSshStatsSessionOctetsSent_Object((1,3,6,1,4,1,3076,2,1,2,35,2,1,8),_AlSshStatsSessionOctetsSent_Type())
alSshStatsSessionOctetsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:alSshStatsSessionOctetsSent.setStatus(_A)
_AlSshStatsSessionOctetsRcvd_Type=Counter32
_AlSshStatsSessionOctetsRcvd_Object=MibTableColumn
alSshStatsSessionOctetsRcvd=_AlSshStatsSessionOctetsRcvd_Object((1,3,6,1,4,1,3076,2,1,2,35,2,1,9),_AlSshStatsSessionOctetsRcvd_Type())
alSshStatsSessionOctetsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:alSshStatsSessionOctetsRcvd.setStatus(_A)
_AlSshStatsSessionPacketsSent_Type=Counter32
_AlSshStatsSessionPacketsSent_Object=MibTableColumn
alSshStatsSessionPacketsSent=_AlSshStatsSessionPacketsSent_Object((1,3,6,1,4,1,3076,2,1,2,35,2,1,10),_AlSshStatsSessionPacketsSent_Type())
alSshStatsSessionPacketsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:alSshStatsSessionPacketsSent.setStatus(_A)
_AlSshStatsSessionPacketsRcvd_Type=Counter32
_AlSshStatsSessionPacketsRcvd_Object=MibTableColumn
alSshStatsSessionPacketsRcvd=_AlSshStatsSessionPacketsRcvd_Object((1,3,6,1,4,1,3076,2,1,2,35,2,1,11),_AlSshStatsSessionPacketsRcvd_Type())
alSshStatsSessionPacketsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:alSshStatsSessionPacketsRcvd.setStatus(_A)
altigaSshStatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,35,2))
altigaSshStatsGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_D),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:altigaSshStatsGroup.setStatus(_A)
altigaSshStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,40,2,1,1,1))
altigaSshStatsMibCompliance.setObjects((_B,_V))
if mibBuilder.loadTexts:altigaSshStatsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'altigaSshStatsMibModule':altigaSshStatsMibModule,'altigaSshStatsMibConformance':altigaSshStatsMibConformance,'altigaSshStatsMibCompliances':altigaSshStatsMibCompliances,'altigaSshStatsMibCompliance':altigaSshStatsMibCompliance,_V:altigaSshStatsGroup,'alStatsSshGlobal':alStatsSshGlobal,_E:alSshStatsOctetsSent,_F:alSshStatsOctetsRcvd,_G:alSshStatsPacketsSent,_H:alSshStatsPacketsRcvd,_I:alSshStatsTotalSessions,_J:alSshStatsActiveSessions,_K:alSshStatsMaxSessions,'alSshStatsSessionTable':alSshStatsSessionTable,'alSshStatsSessionEntry':alSshStatsSessionEntry,_D:alSshStatsSessionIndex,_L:alSshStatsSessionName,_M:alSshStatsSessionIpAddr,_N:alSshStatsSessionPort,_O:alSshStatsSessionStartTime,_P:alSshStatsSessionLoginTime,_Q:alSshStatsSessionEncr,_R:alSshStatsSessionOctetsSent,_S:alSshStatsSessionOctetsRcvd,_T:alSshStatsSessionPacketsSent,_U:alSshStatsSessionPacketsRcvd})