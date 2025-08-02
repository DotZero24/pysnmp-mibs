_L='cienaCesBfdSessionOperState'
_K='cienaCesBfdSessionAdminState'
_J='cienaCesBfdSessionName'
_I='cienaCesBfdProfileIndex'
_H='not-accessible'
_G='cienaGlobalSeverity'
_F='cienaGlobalMacAddress'
_E='CIENA-GLOBAL-MIB'
_D='cienaCesBfdSessionIndex'
_C='CIENA-CES-BFD-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaGlobalMacAddress,cienaGlobalSeverity=mibBuilder.importSymbols(_E,_F,_G)
cienaCesConfig,cienaCesNotifications,cienaCesStatistics=mibBuilder.importSymbols('CIENA-SMI','cienaCesConfig','cienaCesNotifications','cienaCesStatistics')
CienaGlobalState,CienaMacAddress,CienaStatsClear=mibBuilder.importSymbols('CIENA-TC','CienaGlobalState','CienaMacAddress','CienaStatsClear')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
cienaCesBfdMIB=ModuleIdentity((1,3,6,1,4,1,1271,2,1,22))
if mibBuilder.loadTexts:cienaCesBfdMIB.setRevisions(('2017-06-07 00:00','2014-04-04 00:00','2014-03-19 00:00','2011-07-26 00:00'))
class BfdRole(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('passive',1),('active',2)))
_CienaCesBfdMIBObjects_ObjectIdentity=ObjectIdentity
cienaCesBfdMIBObjects=_CienaCesBfdMIBObjects_ObjectIdentity((1,3,6,1,4,1,1271,2,1,22,1))
_CienaCesBfdSession_ObjectIdentity=ObjectIdentity
cienaCesBfdSession=_CienaCesBfdSession_ObjectIdentity((1,3,6,1,4,1,1271,2,1,22,1,2))
_CienaCesBfdSessionTable_Object=MibTable
cienaCesBfdSessionTable=_CienaCesBfdSessionTable_Object((1,3,6,1,4,1,1271,2,1,22,1,2,1))
if mibBuilder.loadTexts:cienaCesBfdSessionTable.setStatus(_A)
_CienaCesBfdSessionEntry_Object=MibTableRow
cienaCesBfdSessionEntry=_CienaCesBfdSessionEntry_Object((1,3,6,1,4,1,1271,2,1,22,1,2,1,1))
cienaCesBfdSessionEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cienaCesBfdSessionEntry.setStatus(_A)
_CienaCesBfdSessionIndex_Type=Unsigned32
_CienaCesBfdSessionIndex_Object=MibTableColumn
cienaCesBfdSessionIndex=_CienaCesBfdSessionIndex_Object((1,3,6,1,4,1,1271,2,1,22,1,2,1,1,1),_CienaCesBfdSessionIndex_Type())
cienaCesBfdSessionIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cienaCesBfdSessionIndex.setStatus(_A)
_CienaCesBfdSessionName_Type=DisplayString
_CienaCesBfdSessionName_Object=MibTableColumn
cienaCesBfdSessionName=_CienaCesBfdSessionName_Object((1,3,6,1,4,1,1271,2,1,22,1,2,1,1,2),_CienaCesBfdSessionName_Type())
cienaCesBfdSessionName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBfdSessionName.setStatus(_A)
_CienaCesBfdSessionAdminState_Type=CienaGlobalState
_CienaCesBfdSessionAdminState_Object=MibTableColumn
cienaCesBfdSessionAdminState=_CienaCesBfdSessionAdminState_Object((1,3,6,1,4,1,1271,2,1,22,1,2,1,1,3),_CienaCesBfdSessionAdminState_Type())
cienaCesBfdSessionAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBfdSessionAdminState.setStatus(_A)
_CienaCesBfdSessionOperState_Type=CienaGlobalState
_CienaCesBfdSessionOperState_Object=MibTableColumn
cienaCesBfdSessionOperState=_CienaCesBfdSessionOperState_Object((1,3,6,1,4,1,1271,2,1,22,1,2,1,1,4),_CienaCesBfdSessionOperState_Type())
cienaCesBfdSessionOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBfdSessionOperState.setStatus(_A)
_CienaCesBfdSessionProfileIndex_Type=Unsigned32
_CienaCesBfdSessionProfileIndex_Object=MibTableColumn
cienaCesBfdSessionProfileIndex=_CienaCesBfdSessionProfileIndex_Object((1,3,6,1,4,1,1271,2,1,22,1,2,1,1,5),_CienaCesBfdSessionProfileIndex_Type())
cienaCesBfdSessionProfileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBfdSessionProfileIndex.setStatus(_A)
_CienaCesBfdProfile_ObjectIdentity=ObjectIdentity
cienaCesBfdProfile=_CienaCesBfdProfile_ObjectIdentity((1,3,6,1,4,1,1271,2,1,22,1,3))
_CienaCesBfdProfileTable_Object=MibTable
cienaCesBfdProfileTable=_CienaCesBfdProfileTable_Object((1,3,6,1,4,1,1271,2,1,22,1,3,1))
if mibBuilder.loadTexts:cienaCesBfdProfileTable.setStatus(_A)
_CienaCesBfdProfileEntry_Object=MibTableRow
cienaCesBfdProfileEntry=_CienaCesBfdProfileEntry_Object((1,3,6,1,4,1,1271,2,1,22,1,3,1,1))
cienaCesBfdProfileEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cienaCesBfdProfileEntry.setStatus(_A)
_CienaCesBfdProfileIndex_Type=Unsigned32
_CienaCesBfdProfileIndex_Object=MibTableColumn
cienaCesBfdProfileIndex=_CienaCesBfdProfileIndex_Object((1,3,6,1,4,1,1271,2,1,22,1,3,1,1,1),_CienaCesBfdProfileIndex_Type())
cienaCesBfdProfileIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cienaCesBfdProfileIndex.setStatus(_A)
_CienaCesBfdProfileName_Type=DisplayString
_CienaCesBfdProfileName_Object=MibTableColumn
cienaCesBfdProfileName=_CienaCesBfdProfileName_Object((1,3,6,1,4,1,1271,2,1,22,1,3,1,1,2),_CienaCesBfdProfileName_Type())
cienaCesBfdProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBfdProfileName.setStatus(_A)
_CienaCesBfdTransmitInterval_Type=Unsigned32
_CienaCesBfdTransmitInterval_Object=MibTableColumn
cienaCesBfdTransmitInterval=_CienaCesBfdTransmitInterval_Object((1,3,6,1,4,1,1271,2,1,22,1,3,1,1,3),_CienaCesBfdTransmitInterval_Type())
cienaCesBfdTransmitInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBfdTransmitInterval.setStatus(_A)
_CienaCesBfdReceiveInterval_Type=Unsigned32
_CienaCesBfdReceiveInterval_Object=MibTableColumn
cienaCesBfdReceiveInterval=_CienaCesBfdReceiveInterval_Object((1,3,6,1,4,1,1271,2,1,22,1,3,1,1,4),_CienaCesBfdReceiveInterval_Type())
cienaCesBfdReceiveInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBfdReceiveInterval.setStatus(_A)
_CienaCesBfdRole_Type=BfdRole
_CienaCesBfdRole_Object=MibTableColumn
cienaCesBfdRole=_CienaCesBfdRole_Object((1,3,6,1,4,1,1271,2,1,22,1,3,1,1,5),_CienaCesBfdRole_Type())
cienaCesBfdRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBfdRole.setStatus(_A)
_CienaCesBfdLspGachType_Type=Unsigned32
_CienaCesBfdLspGachType_Object=MibTableColumn
cienaCesBfdLspGachType=_CienaCesBfdLspGachType_Object((1,3,6,1,4,1,1271,2,1,22,1,3,1,1,6),_CienaCesBfdLspGachType_Type())
cienaCesBfdLspGachType.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBfdLspGachType.setStatus(_A)
_CienaCesBfdDetectMultiplier_Type=Unsigned32
_CienaCesBfdDetectMultiplier_Object=MibTableColumn
cienaCesBfdDetectMultiplier=_CienaCesBfdDetectMultiplier_Object((1,3,6,1,4,1,1271,2,1,22,1,3,1,1,7),_CienaCesBfdDetectMultiplier_Type())
cienaCesBfdDetectMultiplier.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBfdDetectMultiplier.setStatus(_A)
_CienaCesBfdUseCount_Type=Unsigned32
_CienaCesBfdUseCount_Object=MibTableColumn
cienaCesBfdUseCount=_CienaCesBfdUseCount_Object((1,3,6,1,4,1,1271,2,1,22,1,3,1,1,8),_CienaCesBfdUseCount_Type())
cienaCesBfdUseCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBfdUseCount.setStatus(_A)
_CienaCesBfdSessionMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
cienaCesBfdSessionMIBNotificationPrefix=_CienaCesBfdSessionMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,1271,2,2,19))
_CienaCesBfdSessionMIBNotification_ObjectIdentity=ObjectIdentity
cienaCesBfdSessionMIBNotification=_CienaCesBfdSessionMIBNotification_ObjectIdentity((1,3,6,1,4,1,1271,2,2,19,0))
_CienaCesBfdSessionStats_ObjectIdentity=ObjectIdentity
cienaCesBfdSessionStats=_CienaCesBfdSessionStats_ObjectIdentity((1,3,6,1,4,1,1271,2,3,7))
_CienaCesBfdSessionStatsTable_Object=MibTable
cienaCesBfdSessionStatsTable=_CienaCesBfdSessionStatsTable_Object((1,3,6,1,4,1,1271,2,3,7,1))
if mibBuilder.loadTexts:cienaCesBfdSessionStatsTable.setStatus(_A)
_CienaCesBfdSessionStatsEntry_Object=MibTableRow
cienaCesBfdSessionStatsEntry=_CienaCesBfdSessionStatsEntry_Object((1,3,6,1,4,1,1271,2,3,7,1,1))
cienaCesBfdSessionStatsEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cienaCesBfdSessionStatsEntry.setStatus(_A)
_CienaCesBfdSessionStatsTotalTx_Type=Unsigned32
_CienaCesBfdSessionStatsTotalTx_Object=MibTableColumn
cienaCesBfdSessionStatsTotalTx=_CienaCesBfdSessionStatsTotalTx_Object((1,3,6,1,4,1,1271,2,3,7,1,1,1),_CienaCesBfdSessionStatsTotalTx_Type())
cienaCesBfdSessionStatsTotalTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBfdSessionStatsTotalTx.setStatus(_A)
_CienaCesBfdSessionStatsTotalRx_Type=Unsigned32
_CienaCesBfdSessionStatsTotalRx_Object=MibTableColumn
cienaCesBfdSessionStatsTotalRx=_CienaCesBfdSessionStatsTotalRx_Object((1,3,6,1,4,1,1271,2,3,7,1,1,2),_CienaCesBfdSessionStatsTotalRx_Type())
cienaCesBfdSessionStatsTotalRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBfdSessionStatsTotalRx.setStatus(_A)
_CienaCesBfdSessionUpTime_Type=Unsigned32
_CienaCesBfdSessionUpTime_Object=MibTableColumn
cienaCesBfdSessionUpTime=_CienaCesBfdSessionUpTime_Object((1,3,6,1,4,1,1271,2,3,7,1,1,3),_CienaCesBfdSessionUpTime_Type())
cienaCesBfdSessionUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBfdSessionUpTime.setStatus(_A)
_CienaCesBfdSessionDownTimeCount_Type=Unsigned32
_CienaCesBfdSessionDownTimeCount_Object=MibTableColumn
cienaCesBfdSessionDownTimeCount=_CienaCesBfdSessionDownTimeCount_Object((1,3,6,1,4,1,1271,2,3,7,1,1,4),_CienaCesBfdSessionDownTimeCount_Type())
cienaCesBfdSessionDownTimeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBfdSessionDownTimeCount.setStatus(_A)
cienaCesBfdSessionOperStateChangeTrap=NotificationType((1,3,6,1,4,1,1271,2,2,19,0,1))
cienaCesBfdSessionOperStateChangeTrap.setObjects(*((_E,_G),(_E,_F),(_C,_J),(_C,_D),(_C,_K),(_C,_L)))
if mibBuilder.loadTexts:cienaCesBfdSessionOperStateChangeTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'BfdRole':BfdRole,'cienaCesBfdMIB':cienaCesBfdMIB,'cienaCesBfdMIBObjects':cienaCesBfdMIBObjects,'cienaCesBfdSession':cienaCesBfdSession,'cienaCesBfdSessionTable':cienaCesBfdSessionTable,'cienaCesBfdSessionEntry':cienaCesBfdSessionEntry,_D:cienaCesBfdSessionIndex,_J:cienaCesBfdSessionName,_K:cienaCesBfdSessionAdminState,_L:cienaCesBfdSessionOperState,'cienaCesBfdSessionProfileIndex':cienaCesBfdSessionProfileIndex,'cienaCesBfdProfile':cienaCesBfdProfile,'cienaCesBfdProfileTable':cienaCesBfdProfileTable,'cienaCesBfdProfileEntry':cienaCesBfdProfileEntry,_I:cienaCesBfdProfileIndex,'cienaCesBfdProfileName':cienaCesBfdProfileName,'cienaCesBfdTransmitInterval':cienaCesBfdTransmitInterval,'cienaCesBfdReceiveInterval':cienaCesBfdReceiveInterval,'cienaCesBfdRole':cienaCesBfdRole,'cienaCesBfdLspGachType':cienaCesBfdLspGachType,'cienaCesBfdDetectMultiplier':cienaCesBfdDetectMultiplier,'cienaCesBfdUseCount':cienaCesBfdUseCount,'cienaCesBfdSessionMIBNotificationPrefix':cienaCesBfdSessionMIBNotificationPrefix,'cienaCesBfdSessionMIBNotification':cienaCesBfdSessionMIBNotification,'cienaCesBfdSessionOperStateChangeTrap':cienaCesBfdSessionOperStateChangeTrap,'cienaCesBfdSessionStats':cienaCesBfdSessionStats,'cienaCesBfdSessionStatsTable':cienaCesBfdSessionStatsTable,'cienaCesBfdSessionStatsEntry':cienaCesBfdSessionStatsEntry,'cienaCesBfdSessionStatsTotalTx':cienaCesBfdSessionStatsTotalTx,'cienaCesBfdSessionStatsTotalRx':cienaCesBfdSessionStatsTotalRx,'cienaCesBfdSessionUpTime':cienaCesBfdSessionUpTime,'cienaCesBfdSessionDownTimeCount':cienaCesBfdSessionDownTimeCount})