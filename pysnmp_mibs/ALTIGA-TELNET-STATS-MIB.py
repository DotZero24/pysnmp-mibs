_t='altigaTelnetStatsGroup'
_s='alTelnetStatsSessionOutShDropOctets'
_r='alTelnetStatsSessionOutShDropPackets'
_q='alTelnetStatsSessionOutShOctets'
_p='alTelnetStatsSessionOutShPackets'
_o='alTelnetStatsSessionInShDropOctets'
_n='alTelnetStatsSessionInShDropPackets'
_m='alTelnetStatsSessionInShOctets'
_l='alTelnetStatsSessionInShPackets'
_k='alTelnetStatsSessionOutNetDropOctets'
_j='alTelnetStatsSessionOutNetDropPackets'
_i='alTelnetStatsSessionOutNetOctets'
_h='alTelnetStatsSessionOutNetPackets'
_g='alTelnetStatsSessionInNetDropOctets'
_f='alTelnetStatsSessionInNetDropPackets'
_e='alTelnetStatsSessionInNetCmdOctets'
_d='alTelnetStatsSessionInNetOctets'
_c='alTelnetStatsSessionInNetPackets'
_b='alTelnetStatsSessionName'
_a='alTelnetStatsSessionSrcPort'
_Z='alTelnetStatsSessionIpAddr'
_Y='alTelnetStatsSessionRowStatus'
_X='alTelnetStatsOutShDropOctets'
_W='alTelnetStatsOutShDropPackets'
_V='alTelnetStatsOutShOctets'
_U='alTelnetStatsOutShPackets'
_T='alTelnetStatsInShDropOctets'
_S='alTelnetStatsInShDropPackets'
_R='alTelnetStatsInShOctets'
_Q='alTelnetStatsInShPackets'
_P='alTelnetStatsOutNetDropOctets'
_O='alTelnetStatsOutNetDropPackets'
_N='alTelnetStatsOutNetOctets'
_M='alTelnetStatsOutNetPackets'
_L='alTelnetStatsInNetDropOctets'
_K='alTelnetStatsInNetDropPackets'
_J='alTelnetStatsInNetCmdOctets'
_I='alTelnetStatsInNetOctets'
_H='alTelnetStatsInNetPackets'
_G='alTelnetStatsSuccessfulSessions'
_F='alTelnetStatsAttemptedSessions'
_E='alTelnetStatsActiveSessions'
_D='alTelnetStatsSessionId'
_C='read-only'
_B='ALTIGA-TELNET-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alTelnetMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alTelnetMibModule')
alStatsTelnet,alTelnetGroup=mibBuilder.importSymbols('ALTIGA-MIB','alStatsTelnet','alTelnetGroup')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
altigaTelnetStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,16,2))
if mibBuilder.loadTexts:altigaTelnetStatsMibModule.setRevisions(('2002-09-05 13:00','2002-07-10 00:00'))
_AltigaTelnetStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaTelnetStatsMibConformance=_AltigaTelnetStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,16,2,1))
_AltigaTelnetStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaTelnetStatsMibCompliances=_AltigaTelnetStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,16,2,1,1))
_AlStatsTelnetGlobal_ObjectIdentity=ObjectIdentity
alStatsTelnetGlobal=_AlStatsTelnetGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,11,1))
_AlTelnetStatsActiveSessions_Type=Gauge32
_AlTelnetStatsActiveSessions_Object=MibScalar
alTelnetStatsActiveSessions=_AlTelnetStatsActiveSessions_Object((1,3,6,1,4,1,3076,2,1,2,11,1,1),_AlTelnetStatsActiveSessions_Type())
alTelnetStatsActiveSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsActiveSessions.setStatus(_A)
_AlTelnetStatsAttemptedSessions_Type=Counter32
_AlTelnetStatsAttemptedSessions_Object=MibScalar
alTelnetStatsAttemptedSessions=_AlTelnetStatsAttemptedSessions_Object((1,3,6,1,4,1,3076,2,1,2,11,1,2),_AlTelnetStatsAttemptedSessions_Type())
alTelnetStatsAttemptedSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsAttemptedSessions.setStatus(_A)
_AlTelnetStatsSuccessfulSessions_Type=Counter32
_AlTelnetStatsSuccessfulSessions_Object=MibScalar
alTelnetStatsSuccessfulSessions=_AlTelnetStatsSuccessfulSessions_Object((1,3,6,1,4,1,3076,2,1,2,11,1,3),_AlTelnetStatsSuccessfulSessions_Type())
alTelnetStatsSuccessfulSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsSuccessfulSessions.setStatus(_A)
_AlTelnetStatsInNetPackets_Type=Counter32
_AlTelnetStatsInNetPackets_Object=MibScalar
alTelnetStatsInNetPackets=_AlTelnetStatsInNetPackets_Object((1,3,6,1,4,1,3076,2,1,2,11,1,4),_AlTelnetStatsInNetPackets_Type())
alTelnetStatsInNetPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsInNetPackets.setStatus(_A)
_AlTelnetStatsInNetOctets_Type=Counter32
_AlTelnetStatsInNetOctets_Object=MibScalar
alTelnetStatsInNetOctets=_AlTelnetStatsInNetOctets_Object((1,3,6,1,4,1,3076,2,1,2,11,1,5),_AlTelnetStatsInNetOctets_Type())
alTelnetStatsInNetOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsInNetOctets.setStatus(_A)
_AlTelnetStatsInNetCmdOctets_Type=Counter32
_AlTelnetStatsInNetCmdOctets_Object=MibScalar
alTelnetStatsInNetCmdOctets=_AlTelnetStatsInNetCmdOctets_Object((1,3,6,1,4,1,3076,2,1,2,11,1,6),_AlTelnetStatsInNetCmdOctets_Type())
alTelnetStatsInNetCmdOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsInNetCmdOctets.setStatus(_A)
_AlTelnetStatsInNetDropPackets_Type=Counter32
_AlTelnetStatsInNetDropPackets_Object=MibScalar
alTelnetStatsInNetDropPackets=_AlTelnetStatsInNetDropPackets_Object((1,3,6,1,4,1,3076,2,1,2,11,1,7),_AlTelnetStatsInNetDropPackets_Type())
alTelnetStatsInNetDropPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsInNetDropPackets.setStatus(_A)
_AlTelnetStatsInNetDropOctets_Type=Counter32
_AlTelnetStatsInNetDropOctets_Object=MibScalar
alTelnetStatsInNetDropOctets=_AlTelnetStatsInNetDropOctets_Object((1,3,6,1,4,1,3076,2,1,2,11,1,8),_AlTelnetStatsInNetDropOctets_Type())
alTelnetStatsInNetDropOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsInNetDropOctets.setStatus(_A)
_AlTelnetStatsOutNetPackets_Type=Counter32
_AlTelnetStatsOutNetPackets_Object=MibScalar
alTelnetStatsOutNetPackets=_AlTelnetStatsOutNetPackets_Object((1,3,6,1,4,1,3076,2,1,2,11,1,9),_AlTelnetStatsOutNetPackets_Type())
alTelnetStatsOutNetPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsOutNetPackets.setStatus(_A)
_AlTelnetStatsOutNetOctets_Type=Counter32
_AlTelnetStatsOutNetOctets_Object=MibScalar
alTelnetStatsOutNetOctets=_AlTelnetStatsOutNetOctets_Object((1,3,6,1,4,1,3076,2,1,2,11,1,10),_AlTelnetStatsOutNetOctets_Type())
alTelnetStatsOutNetOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsOutNetOctets.setStatus(_A)
_AlTelnetStatsOutNetDropPackets_Type=Counter32
_AlTelnetStatsOutNetDropPackets_Object=MibScalar
alTelnetStatsOutNetDropPackets=_AlTelnetStatsOutNetDropPackets_Object((1,3,6,1,4,1,3076,2,1,2,11,1,11),_AlTelnetStatsOutNetDropPackets_Type())
alTelnetStatsOutNetDropPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsOutNetDropPackets.setStatus(_A)
_AlTelnetStatsOutNetDropOctets_Type=Counter32
_AlTelnetStatsOutNetDropOctets_Object=MibScalar
alTelnetStatsOutNetDropOctets=_AlTelnetStatsOutNetDropOctets_Object((1,3,6,1,4,1,3076,2,1,2,11,1,12),_AlTelnetStatsOutNetDropOctets_Type())
alTelnetStatsOutNetDropOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsOutNetDropOctets.setStatus(_A)
_AlTelnetStatsInShPackets_Type=Counter32
_AlTelnetStatsInShPackets_Object=MibScalar
alTelnetStatsInShPackets=_AlTelnetStatsInShPackets_Object((1,3,6,1,4,1,3076,2,1,2,11,1,13),_AlTelnetStatsInShPackets_Type())
alTelnetStatsInShPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsInShPackets.setStatus(_A)
_AlTelnetStatsInShOctets_Type=Counter32
_AlTelnetStatsInShOctets_Object=MibScalar
alTelnetStatsInShOctets=_AlTelnetStatsInShOctets_Object((1,3,6,1,4,1,3076,2,1,2,11,1,14),_AlTelnetStatsInShOctets_Type())
alTelnetStatsInShOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsInShOctets.setStatus(_A)
_AlTelnetStatsInShDropPackets_Type=Counter32
_AlTelnetStatsInShDropPackets_Object=MibScalar
alTelnetStatsInShDropPackets=_AlTelnetStatsInShDropPackets_Object((1,3,6,1,4,1,3076,2,1,2,11,1,15),_AlTelnetStatsInShDropPackets_Type())
alTelnetStatsInShDropPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsInShDropPackets.setStatus(_A)
_AlTelnetStatsInShDropOctets_Type=Counter32
_AlTelnetStatsInShDropOctets_Object=MibScalar
alTelnetStatsInShDropOctets=_AlTelnetStatsInShDropOctets_Object((1,3,6,1,4,1,3076,2,1,2,11,1,16),_AlTelnetStatsInShDropOctets_Type())
alTelnetStatsInShDropOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsInShDropOctets.setStatus(_A)
_AlTelnetStatsOutShPackets_Type=Counter32
_AlTelnetStatsOutShPackets_Object=MibScalar
alTelnetStatsOutShPackets=_AlTelnetStatsOutShPackets_Object((1,3,6,1,4,1,3076,2,1,2,11,1,17),_AlTelnetStatsOutShPackets_Type())
alTelnetStatsOutShPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsOutShPackets.setStatus(_A)
_AlTelnetStatsOutShOctets_Type=Counter32
_AlTelnetStatsOutShOctets_Object=MibScalar
alTelnetStatsOutShOctets=_AlTelnetStatsOutShOctets_Object((1,3,6,1,4,1,3076,2,1,2,11,1,18),_AlTelnetStatsOutShOctets_Type())
alTelnetStatsOutShOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsOutShOctets.setStatus(_A)
_AlTelnetStatsOutShDropPackets_Type=Counter32
_AlTelnetStatsOutShDropPackets_Object=MibScalar
alTelnetStatsOutShDropPackets=_AlTelnetStatsOutShDropPackets_Object((1,3,6,1,4,1,3076,2,1,2,11,1,19),_AlTelnetStatsOutShDropPackets_Type())
alTelnetStatsOutShDropPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsOutShDropPackets.setStatus(_A)
_AlTelnetStatsOutShDropOctets_Type=Counter32
_AlTelnetStatsOutShDropOctets_Object=MibScalar
alTelnetStatsOutShDropOctets=_AlTelnetStatsOutShDropOctets_Object((1,3,6,1,4,1,3076,2,1,2,11,1,20),_AlTelnetStatsOutShDropOctets_Type())
alTelnetStatsOutShDropOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsOutShDropOctets.setStatus(_A)
_AlTelnetStatsSessionTable_Object=MibTable
alTelnetStatsSessionTable=_AlTelnetStatsSessionTable_Object((1,3,6,1,4,1,3076,2,1,2,11,2))
if mibBuilder.loadTexts:alTelnetStatsSessionTable.setStatus(_A)
_AlTelnetStatsSessionEntry_Object=MibTableRow
alTelnetStatsSessionEntry=_AlTelnetStatsSessionEntry_Object((1,3,6,1,4,1,3076,2,1,2,11,2,1))
alTelnetStatsSessionEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:alTelnetStatsSessionEntry.setStatus(_A)
_AlTelnetStatsSessionRowStatus_Type=RowStatus
_AlTelnetStatsSessionRowStatus_Object=MibTableColumn
alTelnetStatsSessionRowStatus=_AlTelnetStatsSessionRowStatus_Object((1,3,6,1,4,1,3076,2,1,2,11,2,1,1),_AlTelnetStatsSessionRowStatus_Type())
alTelnetStatsSessionRowStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:alTelnetStatsSessionRowStatus.setStatus(_A)
_AlTelnetStatsSessionId_Type=Integer32
_AlTelnetStatsSessionId_Object=MibTableColumn
alTelnetStatsSessionId=_AlTelnetStatsSessionId_Object((1,3,6,1,4,1,3076,2,1,2,11,2,1,2),_AlTelnetStatsSessionId_Type())
alTelnetStatsSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsSessionId.setStatus(_A)
_AlTelnetStatsSessionIpAddr_Type=IpAddress
_AlTelnetStatsSessionIpAddr_Object=MibTableColumn
alTelnetStatsSessionIpAddr=_AlTelnetStatsSessionIpAddr_Object((1,3,6,1,4,1,3076,2,1,2,11,2,1,3),_AlTelnetStatsSessionIpAddr_Type())
alTelnetStatsSessionIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsSessionIpAddr.setStatus(_A)
_AlTelnetStatsSessionSrcPort_Type=Integer32
_AlTelnetStatsSessionSrcPort_Object=MibTableColumn
alTelnetStatsSessionSrcPort=_AlTelnetStatsSessionSrcPort_Object((1,3,6,1,4,1,3076,2,1,2,11,2,1,4),_AlTelnetStatsSessionSrcPort_Type())
alTelnetStatsSessionSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsSessionSrcPort.setStatus(_A)
_AlTelnetStatsSessionName_Type=DisplayString
_AlTelnetStatsSessionName_Object=MibTableColumn
alTelnetStatsSessionName=_AlTelnetStatsSessionName_Object((1,3,6,1,4,1,3076,2,1,2,11,2,1,5),_AlTelnetStatsSessionName_Type())
alTelnetStatsSessionName.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsSessionName.setStatus(_A)
_AlTelnetStatsSessionInNetPackets_Type=Counter32
_AlTelnetStatsSessionInNetPackets_Object=MibTableColumn
alTelnetStatsSessionInNetPackets=_AlTelnetStatsSessionInNetPackets_Object((1,3,6,1,4,1,3076,2,1,2,11,2,1,6),_AlTelnetStatsSessionInNetPackets_Type())
alTelnetStatsSessionInNetPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsSessionInNetPackets.setStatus(_A)
_AlTelnetStatsSessionInNetOctets_Type=Counter32
_AlTelnetStatsSessionInNetOctets_Object=MibTableColumn
alTelnetStatsSessionInNetOctets=_AlTelnetStatsSessionInNetOctets_Object((1,3,6,1,4,1,3076,2,1,2,11,2,1,7),_AlTelnetStatsSessionInNetOctets_Type())
alTelnetStatsSessionInNetOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsSessionInNetOctets.setStatus(_A)
_AlTelnetStatsSessionInNetCmdOctets_Type=Counter32
_AlTelnetStatsSessionInNetCmdOctets_Object=MibTableColumn
alTelnetStatsSessionInNetCmdOctets=_AlTelnetStatsSessionInNetCmdOctets_Object((1,3,6,1,4,1,3076,2,1,2,11,2,1,8),_AlTelnetStatsSessionInNetCmdOctets_Type())
alTelnetStatsSessionInNetCmdOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsSessionInNetCmdOctets.setStatus(_A)
_AlTelnetStatsSessionInNetDropPackets_Type=Counter32
_AlTelnetStatsSessionInNetDropPackets_Object=MibTableColumn
alTelnetStatsSessionInNetDropPackets=_AlTelnetStatsSessionInNetDropPackets_Object((1,3,6,1,4,1,3076,2,1,2,11,2,1,9),_AlTelnetStatsSessionInNetDropPackets_Type())
alTelnetStatsSessionInNetDropPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsSessionInNetDropPackets.setStatus(_A)
_AlTelnetStatsSessionInNetDropOctets_Type=Counter32
_AlTelnetStatsSessionInNetDropOctets_Object=MibTableColumn
alTelnetStatsSessionInNetDropOctets=_AlTelnetStatsSessionInNetDropOctets_Object((1,3,6,1,4,1,3076,2,1,2,11,2,1,10),_AlTelnetStatsSessionInNetDropOctets_Type())
alTelnetStatsSessionInNetDropOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsSessionInNetDropOctets.setStatus(_A)
_AlTelnetStatsSessionOutNetPackets_Type=Counter32
_AlTelnetStatsSessionOutNetPackets_Object=MibTableColumn
alTelnetStatsSessionOutNetPackets=_AlTelnetStatsSessionOutNetPackets_Object((1,3,6,1,4,1,3076,2,1,2,11,2,1,11),_AlTelnetStatsSessionOutNetPackets_Type())
alTelnetStatsSessionOutNetPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsSessionOutNetPackets.setStatus(_A)
_AlTelnetStatsSessionOutNetOctets_Type=Counter32
_AlTelnetStatsSessionOutNetOctets_Object=MibTableColumn
alTelnetStatsSessionOutNetOctets=_AlTelnetStatsSessionOutNetOctets_Object((1,3,6,1,4,1,3076,2,1,2,11,2,1,12),_AlTelnetStatsSessionOutNetOctets_Type())
alTelnetStatsSessionOutNetOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsSessionOutNetOctets.setStatus(_A)
_AlTelnetStatsSessionOutNetDropPackets_Type=Counter32
_AlTelnetStatsSessionOutNetDropPackets_Object=MibTableColumn
alTelnetStatsSessionOutNetDropPackets=_AlTelnetStatsSessionOutNetDropPackets_Object((1,3,6,1,4,1,3076,2,1,2,11,2,1,13),_AlTelnetStatsSessionOutNetDropPackets_Type())
alTelnetStatsSessionOutNetDropPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsSessionOutNetDropPackets.setStatus(_A)
_AlTelnetStatsSessionOutNetDropOctets_Type=Counter32
_AlTelnetStatsSessionOutNetDropOctets_Object=MibTableColumn
alTelnetStatsSessionOutNetDropOctets=_AlTelnetStatsSessionOutNetDropOctets_Object((1,3,6,1,4,1,3076,2,1,2,11,2,1,14),_AlTelnetStatsSessionOutNetDropOctets_Type())
alTelnetStatsSessionOutNetDropOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsSessionOutNetDropOctets.setStatus(_A)
_AlTelnetStatsSessionInShPackets_Type=Counter32
_AlTelnetStatsSessionInShPackets_Object=MibTableColumn
alTelnetStatsSessionInShPackets=_AlTelnetStatsSessionInShPackets_Object((1,3,6,1,4,1,3076,2,1,2,11,2,1,15),_AlTelnetStatsSessionInShPackets_Type())
alTelnetStatsSessionInShPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsSessionInShPackets.setStatus(_A)
_AlTelnetStatsSessionInShOctets_Type=Counter32
_AlTelnetStatsSessionInShOctets_Object=MibTableColumn
alTelnetStatsSessionInShOctets=_AlTelnetStatsSessionInShOctets_Object((1,3,6,1,4,1,3076,2,1,2,11,2,1,16),_AlTelnetStatsSessionInShOctets_Type())
alTelnetStatsSessionInShOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsSessionInShOctets.setStatus(_A)
_AlTelnetStatsSessionInShDropPackets_Type=Counter32
_AlTelnetStatsSessionInShDropPackets_Object=MibTableColumn
alTelnetStatsSessionInShDropPackets=_AlTelnetStatsSessionInShDropPackets_Object((1,3,6,1,4,1,3076,2,1,2,11,2,1,17),_AlTelnetStatsSessionInShDropPackets_Type())
alTelnetStatsSessionInShDropPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsSessionInShDropPackets.setStatus(_A)
_AlTelnetStatsSessionInShDropOctets_Type=Counter32
_AlTelnetStatsSessionInShDropOctets_Object=MibTableColumn
alTelnetStatsSessionInShDropOctets=_AlTelnetStatsSessionInShDropOctets_Object((1,3,6,1,4,1,3076,2,1,2,11,2,1,18),_AlTelnetStatsSessionInShDropOctets_Type())
alTelnetStatsSessionInShDropOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsSessionInShDropOctets.setStatus(_A)
_AlTelnetStatsSessionOutShPackets_Type=Counter32
_AlTelnetStatsSessionOutShPackets_Object=MibTableColumn
alTelnetStatsSessionOutShPackets=_AlTelnetStatsSessionOutShPackets_Object((1,3,6,1,4,1,3076,2,1,2,11,2,1,19),_AlTelnetStatsSessionOutShPackets_Type())
alTelnetStatsSessionOutShPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsSessionOutShPackets.setStatus(_A)
_AlTelnetStatsSessionOutShOctets_Type=Counter32
_AlTelnetStatsSessionOutShOctets_Object=MibTableColumn
alTelnetStatsSessionOutShOctets=_AlTelnetStatsSessionOutShOctets_Object((1,3,6,1,4,1,3076,2,1,2,11,2,1,20),_AlTelnetStatsSessionOutShOctets_Type())
alTelnetStatsSessionOutShOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsSessionOutShOctets.setStatus(_A)
_AlTelnetStatsSessionOutShDropPackets_Type=Counter32
_AlTelnetStatsSessionOutShDropPackets_Object=MibTableColumn
alTelnetStatsSessionOutShDropPackets=_AlTelnetStatsSessionOutShDropPackets_Object((1,3,6,1,4,1,3076,2,1,2,11,2,1,21),_AlTelnetStatsSessionOutShDropPackets_Type())
alTelnetStatsSessionOutShDropPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsSessionOutShDropPackets.setStatus(_A)
_AlTelnetStatsSessionOutShDropOctets_Type=Counter32
_AlTelnetStatsSessionOutShDropOctets_Object=MibTableColumn
alTelnetStatsSessionOutShDropOctets=_AlTelnetStatsSessionOutShDropOctets_Object((1,3,6,1,4,1,3076,2,1,2,11,2,1,22),_AlTelnetStatsSessionOutShDropOctets_Type())
alTelnetStatsSessionOutShDropOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alTelnetStatsSessionOutShDropOctets.setStatus(_A)
altigaTelnetStatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,11,2))
altigaTelnetStatsGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_D),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:altigaTelnetStatsGroup.setStatus(_A)
altigaTelnetStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,16,2,1,1,1))
altigaTelnetStatsMibCompliance.setObjects((_B,_t))
if mibBuilder.loadTexts:altigaTelnetStatsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'altigaTelnetStatsMibModule':altigaTelnetStatsMibModule,'altigaTelnetStatsMibConformance':altigaTelnetStatsMibConformance,'altigaTelnetStatsMibCompliances':altigaTelnetStatsMibCompliances,'altigaTelnetStatsMibCompliance':altigaTelnetStatsMibCompliance,_t:altigaTelnetStatsGroup,'alStatsTelnetGlobal':alStatsTelnetGlobal,_E:alTelnetStatsActiveSessions,_F:alTelnetStatsAttemptedSessions,_G:alTelnetStatsSuccessfulSessions,_H:alTelnetStatsInNetPackets,_I:alTelnetStatsInNetOctets,_J:alTelnetStatsInNetCmdOctets,_K:alTelnetStatsInNetDropPackets,_L:alTelnetStatsInNetDropOctets,_M:alTelnetStatsOutNetPackets,_N:alTelnetStatsOutNetOctets,_O:alTelnetStatsOutNetDropPackets,_P:alTelnetStatsOutNetDropOctets,_Q:alTelnetStatsInShPackets,_R:alTelnetStatsInShOctets,_S:alTelnetStatsInShDropPackets,_T:alTelnetStatsInShDropOctets,_U:alTelnetStatsOutShPackets,_V:alTelnetStatsOutShOctets,_W:alTelnetStatsOutShDropPackets,_X:alTelnetStatsOutShDropOctets,'alTelnetStatsSessionTable':alTelnetStatsSessionTable,'alTelnetStatsSessionEntry':alTelnetStatsSessionEntry,_Y:alTelnetStatsSessionRowStatus,_D:alTelnetStatsSessionId,_Z:alTelnetStatsSessionIpAddr,_a:alTelnetStatsSessionSrcPort,_b:alTelnetStatsSessionName,_c:alTelnetStatsSessionInNetPackets,_d:alTelnetStatsSessionInNetOctets,_e:alTelnetStatsSessionInNetCmdOctets,_f:alTelnetStatsSessionInNetDropPackets,_g:alTelnetStatsSessionInNetDropOctets,_h:alTelnetStatsSessionOutNetPackets,_i:alTelnetStatsSessionOutNetOctets,_j:alTelnetStatsSessionOutNetDropPackets,_k:alTelnetStatsSessionOutNetDropOctets,_l:alTelnetStatsSessionInShPackets,_m:alTelnetStatsSessionInShOctets,_n:alTelnetStatsSessionInShDropPackets,_o:alTelnetStatsSessionInShDropOctets,_p:alTelnetStatsSessionOutShPackets,_q:alTelnetStatsSessionOutShOctets,_r:alTelnetStatsSessionOutShDropPackets,_s:alTelnetStatsSessionOutShDropOctets})