_b='altigaPPPoEStatsGroup'
_a='alPPPoEStatsIfRelaySessID'
_Z='alPPPoEStatsIfHostUnique'
_Y='alPPPoEStatsIfACCookie'
_X='alPPPoEStatsIfPeerName'
_W='alPPPoEStatsIfDuration'
_V='alPPPoEStatsIfConnectTime'
_U='alPPPoEStatsIfType'
_T='alPPPoEStatsIfVersion'
_S='alPPPoEStatsIfSessionState'
_R='alPPPoEStatsIfPeerAddr'
_Q='alPPPoEStatsIfSessionID'
_P='alPPPoEStatsIfMultPADORx'
_O='alPPPoEStatsIfPADRTimeouts'
_N='alPPPoEStatsIfPADITimeouts'
_M='alPPPoEStatsIfMalformedPacketsRx'
_L='alPPPoEStatsIfGenericErrorsRx'
_K='alPPPoEStatsIfPADTTx'
_J='alPPPoEStatsIfPADTRx'
_I='alPPPoEStatsMaxSessions'
_H='alPPPoEStatsTotalSessions'
_G='alPPPoEStatsActiveSessions'
_F='alPPPoEStatsIfIndex'
_E='Integer32'
_D='OctetString'
_C='read-only'
_B='ALTIGA-PPPOE-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alPPPoEMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alPPPoEMibModule')
alPPPoEGroup,alStatsPPPoE=mibBuilder.importSymbols('ALTIGA-MIB','alPPPoEGroup','alStatsPPPoE')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
altigaPPPoEStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,45,2))
if mibBuilder.loadTexts:altigaPPPoEStatsMibModule.setRevisions(('2007-07-11 00:00','2002-09-05 13:00','2002-07-10 00:00'))
_AltigaPPPoEStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaPPPoEStatsMibConformance=_AltigaPPPoEStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,45,2,1))
_AltigaPPPoEStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaPPPoEStatsMibCompliances=_AltigaPPPoEStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,45,2,1,1))
_AlStatsPPPoEGlobal_ObjectIdentity=ObjectIdentity
alStatsPPPoEGlobal=_AlStatsPPPoEGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,40,1))
_AlPPPoEStatsActiveSessions_Type=Gauge32
_AlPPPoEStatsActiveSessions_Object=MibScalar
alPPPoEStatsActiveSessions=_AlPPPoEStatsActiveSessions_Object((1,3,6,1,4,1,3076,2,1,2,40,1,1),_AlPPPoEStatsActiveSessions_Type())
alPPPoEStatsActiveSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:alPPPoEStatsActiveSessions.setStatus(_A)
_AlPPPoEStatsTotalSessions_Type=Counter32
_AlPPPoEStatsTotalSessions_Object=MibScalar
alPPPoEStatsTotalSessions=_AlPPPoEStatsTotalSessions_Object((1,3,6,1,4,1,3076,2,1,2,40,1,2),_AlPPPoEStatsTotalSessions_Type())
alPPPoEStatsTotalSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:alPPPoEStatsTotalSessions.setStatus(_A)
_AlPPPoEStatsMaxSessions_Type=Counter32
_AlPPPoEStatsMaxSessions_Object=MibScalar
alPPPoEStatsMaxSessions=_AlPPPoEStatsMaxSessions_Object((1,3,6,1,4,1,3076,2,1,2,40,1,3),_AlPPPoEStatsMaxSessions_Type())
alPPPoEStatsMaxSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:alPPPoEStatsMaxSessions.setStatus(_A)
_AlPPPoEStatsIfTable_Object=MibTable
alPPPoEStatsIfTable=_AlPPPoEStatsIfTable_Object((1,3,6,1,4,1,3076,2,1,2,40,2))
if mibBuilder.loadTexts:alPPPoEStatsIfTable.setStatus(_A)
_AlPPPoEStatsIfEntry_Object=MibTableRow
alPPPoEStatsIfEntry=_AlPPPoEStatsIfEntry_Object((1,3,6,1,4,1,3076,2,1,2,40,2,1))
alPPPoEStatsIfEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:alPPPoEStatsIfEntry.setStatus(_A)
class _AlPPPoEStatsIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AlPPPoEStatsIfIndex_Type.__name__=_E
_AlPPPoEStatsIfIndex_Object=MibTableColumn
alPPPoEStatsIfIndex=_AlPPPoEStatsIfIndex_Object((1,3,6,1,4,1,3076,2,1,2,40,2,1,1),_AlPPPoEStatsIfIndex_Type())
alPPPoEStatsIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alPPPoEStatsIfIndex.setStatus(_A)
_AlPPPoEStatsIfPADTRx_Type=Counter32
_AlPPPoEStatsIfPADTRx_Object=MibTableColumn
alPPPoEStatsIfPADTRx=_AlPPPoEStatsIfPADTRx_Object((1,3,6,1,4,1,3076,2,1,2,40,2,1,2),_AlPPPoEStatsIfPADTRx_Type())
alPPPoEStatsIfPADTRx.setMaxAccess(_C)
if mibBuilder.loadTexts:alPPPoEStatsIfPADTRx.setStatus(_A)
_AlPPPoEStatsIfPADTTx_Type=Counter32
_AlPPPoEStatsIfPADTTx_Object=MibTableColumn
alPPPoEStatsIfPADTTx=_AlPPPoEStatsIfPADTTx_Object((1,3,6,1,4,1,3076,2,1,2,40,2,1,3),_AlPPPoEStatsIfPADTTx_Type())
alPPPoEStatsIfPADTTx.setMaxAccess(_C)
if mibBuilder.loadTexts:alPPPoEStatsIfPADTTx.setStatus(_A)
_AlPPPoEStatsIfGenericErrorsRx_Type=Counter32
_AlPPPoEStatsIfGenericErrorsRx_Object=MibTableColumn
alPPPoEStatsIfGenericErrorsRx=_AlPPPoEStatsIfGenericErrorsRx_Object((1,3,6,1,4,1,3076,2,1,2,40,2,1,4),_AlPPPoEStatsIfGenericErrorsRx_Type())
alPPPoEStatsIfGenericErrorsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:alPPPoEStatsIfGenericErrorsRx.setStatus(_A)
_AlPPPoEStatsIfMalformedPacketsRx_Type=Counter32
_AlPPPoEStatsIfMalformedPacketsRx_Object=MibTableColumn
alPPPoEStatsIfMalformedPacketsRx=_AlPPPoEStatsIfMalformedPacketsRx_Object((1,3,6,1,4,1,3076,2,1,2,40,2,1,5),_AlPPPoEStatsIfMalformedPacketsRx_Type())
alPPPoEStatsIfMalformedPacketsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:alPPPoEStatsIfMalformedPacketsRx.setStatus(_A)
_AlPPPoEStatsIfPADITimeouts_Type=Counter32
_AlPPPoEStatsIfPADITimeouts_Object=MibTableColumn
alPPPoEStatsIfPADITimeouts=_AlPPPoEStatsIfPADITimeouts_Object((1,3,6,1,4,1,3076,2,1,2,40,2,1,6),_AlPPPoEStatsIfPADITimeouts_Type())
alPPPoEStatsIfPADITimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:alPPPoEStatsIfPADITimeouts.setStatus(_A)
_AlPPPoEStatsIfPADRTimeouts_Type=Counter32
_AlPPPoEStatsIfPADRTimeouts_Object=MibTableColumn
alPPPoEStatsIfPADRTimeouts=_AlPPPoEStatsIfPADRTimeouts_Object((1,3,6,1,4,1,3076,2,1,2,40,2,1,7),_AlPPPoEStatsIfPADRTimeouts_Type())
alPPPoEStatsIfPADRTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:alPPPoEStatsIfPADRTimeouts.setStatus(_A)
_AlPPPoEStatsIfMultPADORx_Type=Counter32
_AlPPPoEStatsIfMultPADORx_Object=MibTableColumn
alPPPoEStatsIfMultPADORx=_AlPPPoEStatsIfMultPADORx_Object((1,3,6,1,4,1,3076,2,1,2,40,2,1,8),_AlPPPoEStatsIfMultPADORx_Type())
alPPPoEStatsIfMultPADORx.setMaxAccess(_C)
if mibBuilder.loadTexts:alPPPoEStatsIfMultPADORx.setStatus(_A)
_AlPPPoEStatsIfSessionID_Type=Integer32
_AlPPPoEStatsIfSessionID_Object=MibTableColumn
alPPPoEStatsIfSessionID=_AlPPPoEStatsIfSessionID_Object((1,3,6,1,4,1,3076,2,1,2,40,2,1,9),_AlPPPoEStatsIfSessionID_Type())
alPPPoEStatsIfSessionID.setMaxAccess(_C)
if mibBuilder.loadTexts:alPPPoEStatsIfSessionID.setStatus(_A)
_AlPPPoEStatsIfPeerAddr_Type=MacAddress
_AlPPPoEStatsIfPeerAddr_Object=MibTableColumn
alPPPoEStatsIfPeerAddr=_AlPPPoEStatsIfPeerAddr_Object((1,3,6,1,4,1,3076,2,1,2,40,2,1,10),_AlPPPoEStatsIfPeerAddr_Type())
alPPPoEStatsIfPeerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:alPPPoEStatsIfPeerAddr.setStatus(_A)
class _AlPPPoEStatsIfSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('noState',1),('pADISent',2),('pADIRcvd',3),('pADOSent',4),('pADORcvd',5),('pADRSent',6),('pADRRcvd',7),('pADSSent',8),('pADSRcvd',9),('sessionStage',10)))
_AlPPPoEStatsIfSessionState_Type.__name__=_E
_AlPPPoEStatsIfSessionState_Object=MibTableColumn
alPPPoEStatsIfSessionState=_AlPPPoEStatsIfSessionState_Object((1,3,6,1,4,1,3076,2,1,2,40,2,1,11),_AlPPPoEStatsIfSessionState_Type())
alPPPoEStatsIfSessionState.setMaxAccess(_C)
if mibBuilder.loadTexts:alPPPoEStatsIfSessionState.setStatus(_A)
_AlPPPoEStatsIfVersion_Type=Integer32
_AlPPPoEStatsIfVersion_Object=MibTableColumn
alPPPoEStatsIfVersion=_AlPPPoEStatsIfVersion_Object((1,3,6,1,4,1,3076,2,1,2,40,2,1,12),_AlPPPoEStatsIfVersion_Type())
alPPPoEStatsIfVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:alPPPoEStatsIfVersion.setStatus(_A)
_AlPPPoEStatsIfType_Type=Integer32
_AlPPPoEStatsIfType_Object=MibTableColumn
alPPPoEStatsIfType=_AlPPPoEStatsIfType_Object((1,3,6,1,4,1,3076,2,1,2,40,2,1,13),_AlPPPoEStatsIfType_Type())
alPPPoEStatsIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:alPPPoEStatsIfType.setStatus(_A)
_AlPPPoEStatsIfConnectTime_Type=Unsigned32
_AlPPPoEStatsIfConnectTime_Object=MibTableColumn
alPPPoEStatsIfConnectTime=_AlPPPoEStatsIfConnectTime_Object((1,3,6,1,4,1,3076,2,1,2,40,2,1,14),_AlPPPoEStatsIfConnectTime_Type())
alPPPoEStatsIfConnectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alPPPoEStatsIfConnectTime.setStatus(_A)
_AlPPPoEStatsIfDuration_Type=Unsigned32
_AlPPPoEStatsIfDuration_Object=MibTableColumn
alPPPoEStatsIfDuration=_AlPPPoEStatsIfDuration_Object((1,3,6,1,4,1,3076,2,1,2,40,2,1,15),_AlPPPoEStatsIfDuration_Type())
alPPPoEStatsIfDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:alPPPoEStatsIfDuration.setStatus(_A)
_AlPPPoEStatsIfPeerName_Type=DisplayString
_AlPPPoEStatsIfPeerName_Object=MibTableColumn
alPPPoEStatsIfPeerName=_AlPPPoEStatsIfPeerName_Object((1,3,6,1,4,1,3076,2,1,2,40,2,1,16),_AlPPPoEStatsIfPeerName_Type())
alPPPoEStatsIfPeerName.setMaxAccess(_C)
if mibBuilder.loadTexts:alPPPoEStatsIfPeerName.setStatus(_A)
class _AlPPPoEStatsIfACCookie_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AlPPPoEStatsIfACCookie_Type.__name__=_D
_AlPPPoEStatsIfACCookie_Object=MibTableColumn
alPPPoEStatsIfACCookie=_AlPPPoEStatsIfACCookie_Object((1,3,6,1,4,1,3076,2,1,2,40,2,1,17),_AlPPPoEStatsIfACCookie_Type())
alPPPoEStatsIfACCookie.setMaxAccess(_C)
if mibBuilder.loadTexts:alPPPoEStatsIfACCookie.setStatus(_A)
class _AlPPPoEStatsIfHostUnique_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_AlPPPoEStatsIfHostUnique_Type.__name__=_D
_AlPPPoEStatsIfHostUnique_Object=MibTableColumn
alPPPoEStatsIfHostUnique=_AlPPPoEStatsIfHostUnique_Object((1,3,6,1,4,1,3076,2,1,2,40,2,1,18),_AlPPPoEStatsIfHostUnique_Type())
alPPPoEStatsIfHostUnique.setMaxAccess(_C)
if mibBuilder.loadTexts:alPPPoEStatsIfHostUnique.setStatus(_A)
class _AlPPPoEStatsIfRelaySessID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_AlPPPoEStatsIfRelaySessID_Type.__name__=_D
_AlPPPoEStatsIfRelaySessID_Object=MibTableColumn
alPPPoEStatsIfRelaySessID=_AlPPPoEStatsIfRelaySessID_Object((1,3,6,1,4,1,3076,2,1,2,40,2,1,19),_AlPPPoEStatsIfRelaySessID_Type())
alPPPoEStatsIfRelaySessID.setMaxAccess(_C)
if mibBuilder.loadTexts:alPPPoEStatsIfRelaySessID.setStatus(_A)
altigaPPPoEStatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,40,2))
altigaPPPoEStatsGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_F),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:altigaPPPoEStatsGroup.setStatus(_A)
altigaPPPoEStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,45,2,1,1,1))
altigaPPPoEStatsMibCompliance.setObjects((_B,_b))
if mibBuilder.loadTexts:altigaPPPoEStatsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'altigaPPPoEStatsMibModule':altigaPPPoEStatsMibModule,'altigaPPPoEStatsMibConformance':altigaPPPoEStatsMibConformance,'altigaPPPoEStatsMibCompliances':altigaPPPoEStatsMibCompliances,'altigaPPPoEStatsMibCompliance':altigaPPPoEStatsMibCompliance,_b:altigaPPPoEStatsGroup,'alStatsPPPoEGlobal':alStatsPPPoEGlobal,_G:alPPPoEStatsActiveSessions,_H:alPPPoEStatsTotalSessions,_I:alPPPoEStatsMaxSessions,'alPPPoEStatsIfTable':alPPPoEStatsIfTable,'alPPPoEStatsIfEntry':alPPPoEStatsIfEntry,_F:alPPPoEStatsIfIndex,_J:alPPPoEStatsIfPADTRx,_K:alPPPoEStatsIfPADTTx,_L:alPPPoEStatsIfGenericErrorsRx,_M:alPPPoEStatsIfMalformedPacketsRx,_N:alPPPoEStatsIfPADITimeouts,_O:alPPPoEStatsIfPADRTimeouts,_P:alPPPoEStatsIfMultPADORx,_Q:alPPPoEStatsIfSessionID,_R:alPPPoEStatsIfPeerAddr,_S:alPPPoEStatsIfSessionState,_T:alPPPoEStatsIfVersion,_U:alPPPoEStatsIfType,_V:alPPPoEStatsIfConnectTime,_W:alPPPoEStatsIfDuration,_X:alPPPoEStatsIfPeerName,_Y:alPPPoEStatsIfACCookie,_Z:alPPPoEStatsIfHostUnique,_a:alPPPoEStatsIfRelaySessID})