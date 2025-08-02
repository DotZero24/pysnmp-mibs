_i='juniCopsProtocolGroup2'
_h='juniCopsProtocolGroup'
_g='juniCopsProtocolSessionTransportRouterName'
_f='juniCopsProtocolSessionLocalAddress'
_e='obsolete'
_d='juniCopsProtocolSessionClientType'
_c='Integer32'
_b='juniCopsProtocolSessionSSCSent'
_a='juniCopsProtocolSessionCCReceived'
_Z='juniCopsProtocolSessionCCSent'
_Y='juniCopsProtocolSessionCATReceived'
_X='juniCopsProtocolSessionOPNSent'
_W='juniCopsProtocolSessionSSQSent'
_V='juniCopsProtocolSessionDRQSent'
_U='juniCopsProtocolSessionRPTSent'
_T='juniCopsProtocolSessionDECReceived'
_S='juniCopsProtocolSessionREQSent'
_R='juniCopsProtocolSessionPacketsSent'
_Q='juniCopsProtocolSessionBytesSent'
_P='juniCopsProtocolSessionPacketsReceived'
_O='juniCopsProtocolSessionBytesReceived'
_N='juniCopsProtocolSessionRemotePort'
_M='juniCopsProtocolSessionRemoteAddress'
_L='juniCopsProtocolKeepAlivesSent'
_K='juniCopsProtocolKeepAlivesReceived'
_J='juniCopsProtocolPacketsSent'
_I='juniCopsProtocolBytesSent'
_H='juniCopsProtocolPacketsReceived'
_G='juniCopsProtocolBytesReceived'
_F='juniCopsProtocolCurrentSessions'
_E='juniCopsProtocolSessionsDeleted'
_D='juniCopsProtocolSessionsCreated'
_C='read-only'
_B='current'
_A='Juniper-COPS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniName,=mibBuilder.importSymbols('Juniper-TC','JuniName')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_c,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
juniCopsProtocolMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,37))
if mibBuilder.loadTexts:juniCopsProtocolMIB.setRevisions(('2002-09-16 21:44','2002-01-14 19:01','2000-02-22 00:00'))
_JuniCopsProtocolObjects_ObjectIdentity=ObjectIdentity
juniCopsProtocolObjects=_JuniCopsProtocolObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,37,1))
_JuniCopsProtocolCfg_ObjectIdentity=ObjectIdentity
juniCopsProtocolCfg=_JuniCopsProtocolCfg_ObjectIdentity((1,3,6,1,4,1,4874,2,2,37,1,1))
_JuniCopsProtocolStatus_ObjectIdentity=ObjectIdentity
juniCopsProtocolStatus=_JuniCopsProtocolStatus_ObjectIdentity((1,3,6,1,4,1,4874,2,2,37,1,2))
_JuniCopsProtocolStatistics_ObjectIdentity=ObjectIdentity
juniCopsProtocolStatistics=_JuniCopsProtocolStatistics_ObjectIdentity((1,3,6,1,4,1,4874,2,2,37,1,3))
_JuniCopsProtocolStatisticsScalars_ObjectIdentity=ObjectIdentity
juniCopsProtocolStatisticsScalars=_JuniCopsProtocolStatisticsScalars_ObjectIdentity((1,3,6,1,4,1,4874,2,2,37,1,3,1))
_JuniCopsProtocolSessionsCreated_Type=Counter32
_JuniCopsProtocolSessionsCreated_Object=MibScalar
juniCopsProtocolSessionsCreated=_JuniCopsProtocolSessionsCreated_Object((1,3,6,1,4,1,4874,2,2,37,1,3,1,1),_JuniCopsProtocolSessionsCreated_Type())
juniCopsProtocolSessionsCreated.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolSessionsCreated.setStatus(_B)
_JuniCopsProtocolSessionsDeleted_Type=Counter32
_JuniCopsProtocolSessionsDeleted_Object=MibScalar
juniCopsProtocolSessionsDeleted=_JuniCopsProtocolSessionsDeleted_Object((1,3,6,1,4,1,4874,2,2,37,1,3,1,2),_JuniCopsProtocolSessionsDeleted_Type())
juniCopsProtocolSessionsDeleted.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolSessionsDeleted.setStatus(_B)
_JuniCopsProtocolCurrentSessions_Type=Counter32
_JuniCopsProtocolCurrentSessions_Object=MibScalar
juniCopsProtocolCurrentSessions=_JuniCopsProtocolCurrentSessions_Object((1,3,6,1,4,1,4874,2,2,37,1,3,1,3),_JuniCopsProtocolCurrentSessions_Type())
juniCopsProtocolCurrentSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolCurrentSessions.setStatus(_B)
_JuniCopsProtocolBytesReceived_Type=Counter32
_JuniCopsProtocolBytesReceived_Object=MibScalar
juniCopsProtocolBytesReceived=_JuniCopsProtocolBytesReceived_Object((1,3,6,1,4,1,4874,2,2,37,1,3,1,4),_JuniCopsProtocolBytesReceived_Type())
juniCopsProtocolBytesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolBytesReceived.setStatus(_B)
_JuniCopsProtocolPacketsReceived_Type=Counter32
_JuniCopsProtocolPacketsReceived_Object=MibScalar
juniCopsProtocolPacketsReceived=_JuniCopsProtocolPacketsReceived_Object((1,3,6,1,4,1,4874,2,2,37,1,3,1,5),_JuniCopsProtocolPacketsReceived_Type())
juniCopsProtocolPacketsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolPacketsReceived.setStatus(_B)
_JuniCopsProtocolBytesSent_Type=Counter32
_JuniCopsProtocolBytesSent_Object=MibScalar
juniCopsProtocolBytesSent=_JuniCopsProtocolBytesSent_Object((1,3,6,1,4,1,4874,2,2,37,1,3,1,6),_JuniCopsProtocolBytesSent_Type())
juniCopsProtocolBytesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolBytesSent.setStatus(_B)
_JuniCopsProtocolPacketsSent_Type=Counter32
_JuniCopsProtocolPacketsSent_Object=MibScalar
juniCopsProtocolPacketsSent=_JuniCopsProtocolPacketsSent_Object((1,3,6,1,4,1,4874,2,2,37,1,3,1,7),_JuniCopsProtocolPacketsSent_Type())
juniCopsProtocolPacketsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolPacketsSent.setStatus(_B)
_JuniCopsProtocolKeepAlivesReceived_Type=Counter32
_JuniCopsProtocolKeepAlivesReceived_Object=MibScalar
juniCopsProtocolKeepAlivesReceived=_JuniCopsProtocolKeepAlivesReceived_Object((1,3,6,1,4,1,4874,2,2,37,1,3,1,8),_JuniCopsProtocolKeepAlivesReceived_Type())
juniCopsProtocolKeepAlivesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolKeepAlivesReceived.setStatus(_B)
_JuniCopsProtocolKeepAlivesSent_Type=Counter32
_JuniCopsProtocolKeepAlivesSent_Object=MibScalar
juniCopsProtocolKeepAlivesSent=_JuniCopsProtocolKeepAlivesSent_Object((1,3,6,1,4,1,4874,2,2,37,1,3,1,9),_JuniCopsProtocolKeepAlivesSent_Type())
juniCopsProtocolKeepAlivesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolKeepAlivesSent.setStatus(_B)
_JuniCopsProtocolSession_ObjectIdentity=ObjectIdentity
juniCopsProtocolSession=_JuniCopsProtocolSession_ObjectIdentity((1,3,6,1,4,1,4874,2,2,37,1,4))
_JuniCopsProtocolSessionTable_Object=MibTable
juniCopsProtocolSessionTable=_JuniCopsProtocolSessionTable_Object((1,3,6,1,4,1,4874,2,2,37,1,4,1))
if mibBuilder.loadTexts:juniCopsProtocolSessionTable.setStatus(_B)
_JuniCopsProtocolSessionEntry_Object=MibTableRow
juniCopsProtocolSessionEntry=_JuniCopsProtocolSessionEntry_Object((1,3,6,1,4,1,4874,2,2,37,1,4,1,1))
juniCopsProtocolSessionEntry.setIndexNames((0,_A,_d))
if mibBuilder.loadTexts:juniCopsProtocolSessionEntry.setStatus(_B)
class _JuniCopsProtocolSessionClientType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_JuniCopsProtocolSessionClientType_Type.__name__=_c
_JuniCopsProtocolSessionClientType_Object=MibTableColumn
juniCopsProtocolSessionClientType=_JuniCopsProtocolSessionClientType_Object((1,3,6,1,4,1,4874,2,2,37,1,4,1,1,1),_JuniCopsProtocolSessionClientType_Type())
juniCopsProtocolSessionClientType.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:juniCopsProtocolSessionClientType.setStatus(_B)
_JuniCopsProtocolSessionRemoteAddress_Type=IpAddress
_JuniCopsProtocolSessionRemoteAddress_Object=MibTableColumn
juniCopsProtocolSessionRemoteAddress=_JuniCopsProtocolSessionRemoteAddress_Object((1,3,6,1,4,1,4874,2,2,37,1,4,1,1,2),_JuniCopsProtocolSessionRemoteAddress_Type())
juniCopsProtocolSessionRemoteAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolSessionRemoteAddress.setStatus(_B)
_JuniCopsProtocolSessionRemotePort_Type=Integer32
_JuniCopsProtocolSessionRemotePort_Object=MibTableColumn
juniCopsProtocolSessionRemotePort=_JuniCopsProtocolSessionRemotePort_Object((1,3,6,1,4,1,4874,2,2,37,1,4,1,1,3),_JuniCopsProtocolSessionRemotePort_Type())
juniCopsProtocolSessionRemotePort.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolSessionRemotePort.setStatus(_B)
_JuniCopsProtocolSessionBytesReceived_Type=Counter32
_JuniCopsProtocolSessionBytesReceived_Object=MibTableColumn
juniCopsProtocolSessionBytesReceived=_JuniCopsProtocolSessionBytesReceived_Object((1,3,6,1,4,1,4874,2,2,37,1,4,1,1,4),_JuniCopsProtocolSessionBytesReceived_Type())
juniCopsProtocolSessionBytesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolSessionBytesReceived.setStatus(_B)
_JuniCopsProtocolSessionPacketsReceived_Type=Counter32
_JuniCopsProtocolSessionPacketsReceived_Object=MibTableColumn
juniCopsProtocolSessionPacketsReceived=_JuniCopsProtocolSessionPacketsReceived_Object((1,3,6,1,4,1,4874,2,2,37,1,4,1,1,5),_JuniCopsProtocolSessionPacketsReceived_Type())
juniCopsProtocolSessionPacketsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolSessionPacketsReceived.setStatus(_B)
_JuniCopsProtocolSessionBytesSent_Type=Counter32
_JuniCopsProtocolSessionBytesSent_Object=MibTableColumn
juniCopsProtocolSessionBytesSent=_JuniCopsProtocolSessionBytesSent_Object((1,3,6,1,4,1,4874,2,2,37,1,4,1,1,6),_JuniCopsProtocolSessionBytesSent_Type())
juniCopsProtocolSessionBytesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolSessionBytesSent.setStatus(_B)
_JuniCopsProtocolSessionPacketsSent_Type=Counter32
_JuniCopsProtocolSessionPacketsSent_Object=MibTableColumn
juniCopsProtocolSessionPacketsSent=_JuniCopsProtocolSessionPacketsSent_Object((1,3,6,1,4,1,4874,2,2,37,1,4,1,1,7),_JuniCopsProtocolSessionPacketsSent_Type())
juniCopsProtocolSessionPacketsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolSessionPacketsSent.setStatus(_B)
_JuniCopsProtocolSessionREQSent_Type=Counter32
_JuniCopsProtocolSessionREQSent_Object=MibTableColumn
juniCopsProtocolSessionREQSent=_JuniCopsProtocolSessionREQSent_Object((1,3,6,1,4,1,4874,2,2,37,1,4,1,1,8),_JuniCopsProtocolSessionREQSent_Type())
juniCopsProtocolSessionREQSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolSessionREQSent.setStatus(_B)
_JuniCopsProtocolSessionDECReceived_Type=Counter32
_JuniCopsProtocolSessionDECReceived_Object=MibTableColumn
juniCopsProtocolSessionDECReceived=_JuniCopsProtocolSessionDECReceived_Object((1,3,6,1,4,1,4874,2,2,37,1,4,1,1,9),_JuniCopsProtocolSessionDECReceived_Type())
juniCopsProtocolSessionDECReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolSessionDECReceived.setStatus(_B)
_JuniCopsProtocolSessionRPTSent_Type=Counter32
_JuniCopsProtocolSessionRPTSent_Object=MibTableColumn
juniCopsProtocolSessionRPTSent=_JuniCopsProtocolSessionRPTSent_Object((1,3,6,1,4,1,4874,2,2,37,1,4,1,1,10),_JuniCopsProtocolSessionRPTSent_Type())
juniCopsProtocolSessionRPTSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolSessionRPTSent.setStatus(_B)
_JuniCopsProtocolSessionDRQSent_Type=Counter32
_JuniCopsProtocolSessionDRQSent_Object=MibTableColumn
juniCopsProtocolSessionDRQSent=_JuniCopsProtocolSessionDRQSent_Object((1,3,6,1,4,1,4874,2,2,37,1,4,1,1,11),_JuniCopsProtocolSessionDRQSent_Type())
juniCopsProtocolSessionDRQSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolSessionDRQSent.setStatus(_B)
_JuniCopsProtocolSessionSSQSent_Type=Counter32
_JuniCopsProtocolSessionSSQSent_Object=MibTableColumn
juniCopsProtocolSessionSSQSent=_JuniCopsProtocolSessionSSQSent_Object((1,3,6,1,4,1,4874,2,2,37,1,4,1,1,12),_JuniCopsProtocolSessionSSQSent_Type())
juniCopsProtocolSessionSSQSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolSessionSSQSent.setStatus(_B)
_JuniCopsProtocolSessionOPNSent_Type=Counter32
_JuniCopsProtocolSessionOPNSent_Object=MibTableColumn
juniCopsProtocolSessionOPNSent=_JuniCopsProtocolSessionOPNSent_Object((1,3,6,1,4,1,4874,2,2,37,1,4,1,1,13),_JuniCopsProtocolSessionOPNSent_Type())
juniCopsProtocolSessionOPNSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolSessionOPNSent.setStatus(_B)
_JuniCopsProtocolSessionCATReceived_Type=Counter32
_JuniCopsProtocolSessionCATReceived_Object=MibTableColumn
juniCopsProtocolSessionCATReceived=_JuniCopsProtocolSessionCATReceived_Object((1,3,6,1,4,1,4874,2,2,37,1,4,1,1,14),_JuniCopsProtocolSessionCATReceived_Type())
juniCopsProtocolSessionCATReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolSessionCATReceived.setStatus(_B)
_JuniCopsProtocolSessionCCSent_Type=Counter32
_JuniCopsProtocolSessionCCSent_Object=MibTableColumn
juniCopsProtocolSessionCCSent=_JuniCopsProtocolSessionCCSent_Object((1,3,6,1,4,1,4874,2,2,37,1,4,1,1,15),_JuniCopsProtocolSessionCCSent_Type())
juniCopsProtocolSessionCCSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolSessionCCSent.setStatus(_B)
_JuniCopsProtocolSessionCCReceived_Type=Counter32
_JuniCopsProtocolSessionCCReceived_Object=MibTableColumn
juniCopsProtocolSessionCCReceived=_JuniCopsProtocolSessionCCReceived_Object((1,3,6,1,4,1,4874,2,2,37,1,4,1,1,16),_JuniCopsProtocolSessionCCReceived_Type())
juniCopsProtocolSessionCCReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolSessionCCReceived.setStatus(_B)
_JuniCopsProtocolSessionSSCSent_Type=Counter32
_JuniCopsProtocolSessionSSCSent_Object=MibTableColumn
juniCopsProtocolSessionSSCSent=_JuniCopsProtocolSessionSSCSent_Object((1,3,6,1,4,1,4874,2,2,37,1,4,1,1,17),_JuniCopsProtocolSessionSSCSent_Type())
juniCopsProtocolSessionSSCSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolSessionSSCSent.setStatus(_B)
_JuniCopsProtocolSessionLocalAddress_Type=IpAddress
_JuniCopsProtocolSessionLocalAddress_Object=MibTableColumn
juniCopsProtocolSessionLocalAddress=_JuniCopsProtocolSessionLocalAddress_Object((1,3,6,1,4,1,4874,2,2,37,1,4,1,1,18),_JuniCopsProtocolSessionLocalAddress_Type())
juniCopsProtocolSessionLocalAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolSessionLocalAddress.setStatus(_B)
_JuniCopsProtocolSessionTransportRouterName_Type=JuniName
_JuniCopsProtocolSessionTransportRouterName_Object=MibTableColumn
juniCopsProtocolSessionTransportRouterName=_JuniCopsProtocolSessionTransportRouterName_Object((1,3,6,1,4,1,4874,2,2,37,1,4,1,1,19),_JuniCopsProtocolSessionTransportRouterName_Type())
juniCopsProtocolSessionTransportRouterName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniCopsProtocolSessionTransportRouterName.setStatus(_B)
_JuniCopsProtocolMIBConformance_ObjectIdentity=ObjectIdentity
juniCopsProtocolMIBConformance=_JuniCopsProtocolMIBConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,37,4))
_JuniCopsProtocolMIBCompliances_ObjectIdentity=ObjectIdentity
juniCopsProtocolMIBCompliances=_JuniCopsProtocolMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,37,4,1))
_JuniCopsProtocolMIBGroups_ObjectIdentity=ObjectIdentity
juniCopsProtocolMIBGroups=_JuniCopsProtocolMIBGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,37,4,2))
juniCopsProtocolGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,37,4,2,1))
juniCopsProtocolGroup.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:juniCopsProtocolGroup.setStatus(_e)
juniCopsProtocolGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,37,4,2,2))
juniCopsProtocolGroup2.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:juniCopsProtocolGroup2.setStatus(_B)
juniCopsProtocolAuthCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,37,4,1,1))
juniCopsProtocolAuthCompliance.setObjects((_A,_h))
if mibBuilder.loadTexts:juniCopsProtocolAuthCompliance.setStatus(_e)
juniCopsProtocolAuthCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,37,4,1,2))
juniCopsProtocolAuthCompliance2.setObjects((_A,_i))
if mibBuilder.loadTexts:juniCopsProtocolAuthCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'juniCopsProtocolMIB':juniCopsProtocolMIB,'juniCopsProtocolObjects':juniCopsProtocolObjects,'juniCopsProtocolCfg':juniCopsProtocolCfg,'juniCopsProtocolStatus':juniCopsProtocolStatus,'juniCopsProtocolStatistics':juniCopsProtocolStatistics,'juniCopsProtocolStatisticsScalars':juniCopsProtocolStatisticsScalars,_D:juniCopsProtocolSessionsCreated,_E:juniCopsProtocolSessionsDeleted,_F:juniCopsProtocolCurrentSessions,_G:juniCopsProtocolBytesReceived,_H:juniCopsProtocolPacketsReceived,_I:juniCopsProtocolBytesSent,_J:juniCopsProtocolPacketsSent,_K:juniCopsProtocolKeepAlivesReceived,_L:juniCopsProtocolKeepAlivesSent,'juniCopsProtocolSession':juniCopsProtocolSession,'juniCopsProtocolSessionTable':juniCopsProtocolSessionTable,'juniCopsProtocolSessionEntry':juniCopsProtocolSessionEntry,_d:juniCopsProtocolSessionClientType,_M:juniCopsProtocolSessionRemoteAddress,_N:juniCopsProtocolSessionRemotePort,_O:juniCopsProtocolSessionBytesReceived,_P:juniCopsProtocolSessionPacketsReceived,_Q:juniCopsProtocolSessionBytesSent,_R:juniCopsProtocolSessionPacketsSent,_S:juniCopsProtocolSessionREQSent,_T:juniCopsProtocolSessionDECReceived,_U:juniCopsProtocolSessionRPTSent,_V:juniCopsProtocolSessionDRQSent,_W:juniCopsProtocolSessionSSQSent,_X:juniCopsProtocolSessionOPNSent,_Y:juniCopsProtocolSessionCATReceived,_Z:juniCopsProtocolSessionCCSent,_a:juniCopsProtocolSessionCCReceived,_b:juniCopsProtocolSessionSSCSent,_f:juniCopsProtocolSessionLocalAddress,_g:juniCopsProtocolSessionTransportRouterName,'juniCopsProtocolMIBConformance':juniCopsProtocolMIBConformance,'juniCopsProtocolMIBCompliances':juniCopsProtocolMIBCompliances,'juniCopsProtocolAuthCompliance':juniCopsProtocolAuthCompliance,'juniCopsProtocolAuthCompliance2':juniCopsProtocolAuthCompliance2,'juniCopsProtocolMIBGroups':juniCopsProtocolMIBGroups,_h:juniCopsProtocolGroup,_i:juniCopsProtocolGroup2})