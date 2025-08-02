_J='domainName'
_I='schannelServerStatsIndex'
_H='lsaDomainControllerStatsIndex'
_G='schannelStatsIndex'
_F='not-accessible'
_E='Integer32'
_D='BLUECOAT-SG-AUTHENTICATION-MIB'
_C='Bytes'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
blueCoatMgmt,=mibBuilder.importSymbols('BLUECOAT-MIB','blueCoatMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bluecoatSGAuthentication=ModuleIdentity((1,3,6,1,4,1,3417,2,15))
if mibBuilder.loadTexts:bluecoatSGAuthentication.setRevisions(('2014-08-06 03:00',))
class ToggleState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_SchannelStats_ObjectIdentity=ObjectIdentity
schannelStats=_SchannelStats_ObjectIdentity((1,3,6,1,4,1,3417,2,15,2))
_SchannelStatsTable_Object=MibTable
schannelStatsTable=_SchannelStatsTable_Object((1,3,6,1,4,1,3417,2,15,2,1))
if mibBuilder.loadTexts:schannelStatsTable.setStatus(_A)
_SchannelStatsEntry_Object=MibTableRow
schannelStatsEntry=_SchannelStatsEntry_Object((1,3,6,1,4,1,3417,2,15,2,1,1))
schannelStatsEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:schannelStatsEntry.setStatus(_A)
class _SchannelStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SchannelStatsIndex_Type.__name__=_E
_SchannelStatsIndex_Object=MibTableColumn
schannelStatsIndex=_SchannelStatsIndex_Object((1,3,6,1,4,1,3417,2,15,2,1,1,1),_SchannelStatsIndex_Type())
schannelStatsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:schannelStatsIndex.setStatus(_A)
_DomainName_Type=DisplayString
_DomainName_Object=MibTableColumn
domainName=_DomainName_Object((1,3,6,1,4,1,3417,2,15,2,1,1,2),_DomainName_Type())
domainName.setMaxAccess(_B)
if mibBuilder.loadTexts:domainName.setStatus(_A)
_DomainStatus_Type=DisplayString
_DomainStatus_Object=MibTableColumn
domainStatus=_DomainStatus_Object((1,3,6,1,4,1,3417,2,15,2,1,1,3),_DomainStatus_Type())
domainStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:domainStatus.setStatus(_A)
_Timeouts_Type=Counter32
_Timeouts_Object=MibTableColumn
timeouts=_Timeouts_Object((1,3,6,1,4,1,3417,2,15,2,1,1,4),_Timeouts_Type())
timeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:timeouts.setStatus(_A)
if mibBuilder.loadTexts:timeouts.setUnits(_C)
_Transactions_Type=Counter32
_Transactions_Object=MibTableColumn
transactions=_Transactions_Object((1,3,6,1,4,1,3417,2,15,2,1,1,5),_Transactions_Type())
transactions.setMaxAccess(_B)
if mibBuilder.loadTexts:transactions.setStatus(_A)
if mibBuilder.loadTexts:transactions.setUnits(_C)
_CurrentWaiters_Type=Counter32
_CurrentWaiters_Object=MibTableColumn
currentWaiters=_CurrentWaiters_Object((1,3,6,1,4,1,3417,2,15,2,1,1,6),_CurrentWaiters_Type())
currentWaiters.setMaxAccess(_B)
if mibBuilder.loadTexts:currentWaiters.setStatus(_A)
if mibBuilder.loadTexts:currentWaiters.setUnits(_C)
_MaxWaiters_Type=Counter32
_MaxWaiters_Object=MibTableColumn
maxWaiters=_MaxWaiters_Object((1,3,6,1,4,1,3417,2,15,2,1,1,7),_MaxWaiters_Type())
maxWaiters.setMaxAccess(_B)
if mibBuilder.loadTexts:maxWaiters.setStatus(_A)
if mibBuilder.loadTexts:maxWaiters.setUnits(_C)
_Resets_Type=Counter32
_Resets_Object=MibTableColumn
resets=_Resets_Object((1,3,6,1,4,1,3417,2,15,2,1,1,8),_Resets_Type())
resets.setMaxAccess(_B)
if mibBuilder.loadTexts:resets.setStatus(_A)
if mibBuilder.loadTexts:resets.setUnits(_C)
_LsaDomainControllerStats_ObjectIdentity=ObjectIdentity
lsaDomainControllerStats=_LsaDomainControllerStats_ObjectIdentity((1,3,6,1,4,1,3417,2,15,3))
_LsaDomainControllerStatsTable_Object=MibTable
lsaDomainControllerStatsTable=_LsaDomainControllerStatsTable_Object((1,3,6,1,4,1,3417,2,15,3,1))
if mibBuilder.loadTexts:lsaDomainControllerStatsTable.setStatus(_A)
_LsaDomainControllerStatsEntry_Object=MibTableRow
lsaDomainControllerStatsEntry=_LsaDomainControllerStatsEntry_Object((1,3,6,1,4,1,3417,2,15,3,1,1))
lsaDomainControllerStatsEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:lsaDomainControllerStatsEntry.setStatus(_A)
class _LsaDomainControllerStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LsaDomainControllerStatsIndex_Type.__name__=_E
_LsaDomainControllerStatsIndex_Object=MibTableColumn
lsaDomainControllerStatsIndex=_LsaDomainControllerStatsIndex_Object((1,3,6,1,4,1,3417,2,15,3,1,1,1),_LsaDomainControllerStatsIndex_Type())
lsaDomainControllerStatsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:lsaDomainControllerStatsIndex.setStatus(_A)
_DomainControllerName_Type=DisplayString
_DomainControllerName_Object=MibTableColumn
domainControllerName=_DomainControllerName_Object((1,3,6,1,4,1,3417,2,15,3,1,1,2),_DomainControllerName_Type())
domainControllerName.setMaxAccess(_B)
if mibBuilder.loadTexts:domainControllerName.setStatus(_A)
_Address_Type=DisplayString
_Address_Object=MibTableColumn
address=_Address_Object((1,3,6,1,4,1,3417,2,15,3,1,1,3),_Address_Type())
address.setMaxAccess(_B)
if mibBuilder.loadTexts:address.setStatus(_A)
_SiteName_Type=DisplayString
_SiteName_Object=MibScalar
siteName=_SiteName_Object((1,3,6,1,4,1,3417,2,15,3,1,1,4),_SiteName_Type())
siteName.setMaxAccess(_B)
if mibBuilder.loadTexts:siteName.setStatus(_A)
_AvgLDAPPingTime_Type=Counter32
_AvgLDAPPingTime_Object=MibTableColumn
avgLDAPPingTime=_AvgLDAPPingTime_Object((1,3,6,1,4,1,3417,2,15,3,1,1,5),_AvgLDAPPingTime_Type())
avgLDAPPingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:avgLDAPPingTime.setStatus(_A)
_LastLDAPPingTime_Type=Counter32
_LastLDAPPingTime_Object=MibScalar
lastLDAPPingTime=_LastLDAPPingTime_Object((1,3,6,1,4,1,3417,2,15,3,1,1,6),_LastLDAPPingTime_Type())
lastLDAPPingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:lastLDAPPingTime.setStatus(_A)
_Flags_Type=DisplayString
_Flags_Object=MibTableColumn
flags=_Flags_Object((1,3,6,1,4,1,3417,2,15,3,1,1,7),_Flags_Type())
flags.setMaxAccess(_B)
if mibBuilder.loadTexts:flags.setStatus(_A)
_SchannelServerStats_ObjectIdentity=ObjectIdentity
schannelServerStats=_SchannelServerStats_ObjectIdentity((1,3,6,1,4,1,3417,2,15,4))
_SchannelServerStatsTable_Object=MibTable
schannelServerStatsTable=_SchannelServerStatsTable_Object((1,3,6,1,4,1,3417,2,15,4,1))
if mibBuilder.loadTexts:schannelServerStatsTable.setStatus(_A)
_SchannelServerStatsEntry_Object=MibTableRow
schannelServerStatsEntry=_SchannelServerStatsEntry_Object((1,3,6,1,4,1,3417,2,15,4,1,1))
schannelServerStatsEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:schannelServerStatsEntry.setStatus(_A)
class _SchannelServerStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SchannelServerStatsIndex_Type.__name__=_E
_SchannelServerStatsIndex_Object=MibTableColumn
schannelServerStatsIndex=_SchannelServerStatsIndex_Object((1,3,6,1,4,1,3417,2,15,4,1,1,1),_SchannelServerStatsIndex_Type())
schannelServerStatsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:schannelServerStatsIndex.setStatus(_A)
_ServerName_Type=DisplayString
_ServerName_Object=MibTableColumn
serverName=_ServerName_Object((1,3,6,1,4,1,3417,2,15,4,1,1,2),_ServerName_Type())
serverName.setMaxAccess(_B)
if mibBuilder.loadTexts:serverName.setStatus(_A)
_ConnectionsInUse_Type=Counter32
_ConnectionsInUse_Object=MibTableColumn
connectionsInUse=_ConnectionsInUse_Object((1,3,6,1,4,1,3417,2,15,4,1,1,3),_ConnectionsInUse_Type())
connectionsInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:connectionsInUse.setStatus(_A)
_AvailableConnections_Type=Counter32
_AvailableConnections_Object=MibTableColumn
availableConnections=_AvailableConnections_Object((1,3,6,1,4,1,3417,2,15,4,1,1,4),_AvailableConnections_Type())
availableConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:availableConnections.setStatus(_A)
_AverageTransactions_Type=Counter32
_AverageTransactions_Object=MibTableColumn
averageTransactions=_AverageTransactions_Object((1,3,6,1,4,1,3417,2,15,4,1,1,5),_AverageTransactions_Type())
averageTransactions.setMaxAccess(_B)
if mibBuilder.loadTexts:averageTransactions.setStatus(_A)
_AuthsByDomainLast1Minute_Type=Counter32
_AuthsByDomainLast1Minute_Object=MibTableColumn
authsByDomainLast1Minute=_AuthsByDomainLast1Minute_Object((1,3,6,1,4,1,3417,2,15,4,1,1,6),_AuthsByDomainLast1Minute_Type())
authsByDomainLast1Minute.setMaxAccess(_B)
if mibBuilder.loadTexts:authsByDomainLast1Minute.setStatus(_A)
if mibBuilder.loadTexts:authsByDomainLast1Minute.setUnits(_C)
_AuthsByDomainLast3Minutes_Type=Counter32
_AuthsByDomainLast3Minutes_Object=MibTableColumn
authsByDomainLast3Minutes=_AuthsByDomainLast3Minutes_Object((1,3,6,1,4,1,3417,2,15,4,1,1,7),_AuthsByDomainLast3Minutes_Type())
authsByDomainLast3Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:authsByDomainLast3Minutes.setStatus(_A)
if mibBuilder.loadTexts:authsByDomainLast3Minutes.setUnits(_C)
_AuthsByDomainLast5Minutes_Type=Counter32
_AuthsByDomainLast5Minutes_Object=MibTableColumn
authsByDomainLast5Minutes=_AuthsByDomainLast5Minutes_Object((1,3,6,1,4,1,3417,2,15,4,1,1,8),_AuthsByDomainLast5Minutes_Type())
authsByDomainLast5Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:authsByDomainLast5Minutes.setStatus(_A)
if mibBuilder.loadTexts:authsByDomainLast5Minutes.setUnits(_C)
_AuthsByDomainLast15Minutes_Type=Counter32
_AuthsByDomainLast15Minutes_Object=MibTableColumn
authsByDomainLast15Minutes=_AuthsByDomainLast15Minutes_Object((1,3,6,1,4,1,3417,2,15,4,1,1,9),_AuthsByDomainLast15Minutes_Type())
authsByDomainLast15Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:authsByDomainLast15Minutes.setStatus(_A)
if mibBuilder.loadTexts:authsByDomainLast15Minutes.setUnits(_C)
_AuthsByDomainLast60Minutes_Type=Counter32
_AuthsByDomainLast60Minutes_Object=MibTableColumn
authsByDomainLast60Minutes=_AuthsByDomainLast60Minutes_Object((1,3,6,1,4,1,3417,2,15,4,1,1,10),_AuthsByDomainLast60Minutes_Type())
authsByDomainLast60Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:authsByDomainLast60Minutes.setStatus(_A)
if mibBuilder.loadTexts:authsByDomainLast60Minutes.setUnits(_C)
_FailedAuthsByDomainLast1Minute_Type=Counter32
_FailedAuthsByDomainLast1Minute_Object=MibTableColumn
failedAuthsByDomainLast1Minute=_FailedAuthsByDomainLast1Minute_Object((1,3,6,1,4,1,3417,2,15,4,1,1,11),_FailedAuthsByDomainLast1Minute_Type())
failedAuthsByDomainLast1Minute.setMaxAccess(_B)
if mibBuilder.loadTexts:failedAuthsByDomainLast1Minute.setStatus(_A)
if mibBuilder.loadTexts:failedAuthsByDomainLast1Minute.setUnits(_C)
_FailedAuthsByDomainLast3Minutes_Type=Counter32
_FailedAuthsByDomainLast3Minutes_Object=MibTableColumn
failedAuthsByDomainLast3Minutes=_FailedAuthsByDomainLast3Minutes_Object((1,3,6,1,4,1,3417,2,15,4,1,1,12),_FailedAuthsByDomainLast3Minutes_Type())
failedAuthsByDomainLast3Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:failedAuthsByDomainLast3Minutes.setStatus(_A)
if mibBuilder.loadTexts:failedAuthsByDomainLast3Minutes.setUnits(_C)
_FailedAuthsByDomainLast5Minutes_Type=Counter32
_FailedAuthsByDomainLast5Minutes_Object=MibTableColumn
failedAuthsByDomainLast5Minutes=_FailedAuthsByDomainLast5Minutes_Object((1,3,6,1,4,1,3417,2,15,4,1,1,13),_FailedAuthsByDomainLast5Minutes_Type())
failedAuthsByDomainLast5Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:failedAuthsByDomainLast5Minutes.setStatus(_A)
if mibBuilder.loadTexts:failedAuthsByDomainLast5Minutes.setUnits(_C)
_FailedAuthsByDomainLast15Minutes_Type=Counter32
_FailedAuthsByDomainLast15Minutes_Object=MibTableColumn
failedAuthsByDomainLast15Minutes=_FailedAuthsByDomainLast15Minutes_Object((1,3,6,1,4,1,3417,2,15,4,1,1,14),_FailedAuthsByDomainLast15Minutes_Type())
failedAuthsByDomainLast15Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:failedAuthsByDomainLast15Minutes.setStatus(_A)
if mibBuilder.loadTexts:failedAuthsByDomainLast15Minutes.setUnits(_C)
_FailedAuthsByDomainLast60Minutes_Type=Counter32
_FailedAuthsByDomainLast60Minutes_Object=MibTableColumn
failedAuthsByDomainLast60Minutes=_FailedAuthsByDomainLast60Minutes_Object((1,3,6,1,4,1,3417,2,15,4,1,1,15),_FailedAuthsByDomainLast60Minutes_Type())
failedAuthsByDomainLast60Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:failedAuthsByDomainLast60Minutes.setStatus(_A)
if mibBuilder.loadTexts:failedAuthsByDomainLast60Minutes.setUnits(_C)
_AvgLatencyPerDomainLast1Minute_Type=Counter32
_AvgLatencyPerDomainLast1Minute_Object=MibTableColumn
avgLatencyPerDomainLast1Minute=_AvgLatencyPerDomainLast1Minute_Object((1,3,6,1,4,1,3417,2,15,4,1,1,16),_AvgLatencyPerDomainLast1Minute_Type())
avgLatencyPerDomainLast1Minute.setMaxAccess(_B)
if mibBuilder.loadTexts:avgLatencyPerDomainLast1Minute.setStatus(_A)
if mibBuilder.loadTexts:avgLatencyPerDomainLast1Minute.setUnits(_C)
_AvgLatencyPerDomainLast3Minutes_Type=Counter32
_AvgLatencyPerDomainLast3Minutes_Object=MibTableColumn
avgLatencyPerDomainLast3Minutes=_AvgLatencyPerDomainLast3Minutes_Object((1,3,6,1,4,1,3417,2,15,4,1,1,17),_AvgLatencyPerDomainLast3Minutes_Type())
avgLatencyPerDomainLast3Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:avgLatencyPerDomainLast3Minutes.setStatus(_A)
if mibBuilder.loadTexts:avgLatencyPerDomainLast3Minutes.setUnits(_C)
_AvgLatencyPerDomainLast5Minutes_Type=Counter32
_AvgLatencyPerDomainLast5Minutes_Object=MibTableColumn
avgLatencyPerDomainLast5Minutes=_AvgLatencyPerDomainLast5Minutes_Object((1,3,6,1,4,1,3417,2,15,4,1,1,18),_AvgLatencyPerDomainLast5Minutes_Type())
avgLatencyPerDomainLast5Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:avgLatencyPerDomainLast5Minutes.setStatus(_A)
if mibBuilder.loadTexts:avgLatencyPerDomainLast5Minutes.setUnits(_C)
_AvgLatencyPerDomainLast15Minutes_Type=Counter32
_AvgLatencyPerDomainLast15Minutes_Object=MibTableColumn
avgLatencyPerDomainLast15Minutes=_AvgLatencyPerDomainLast15Minutes_Object((1,3,6,1,4,1,3417,2,15,4,1,1,19),_AvgLatencyPerDomainLast15Minutes_Type())
avgLatencyPerDomainLast15Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:avgLatencyPerDomainLast15Minutes.setStatus(_A)
if mibBuilder.loadTexts:avgLatencyPerDomainLast15Minutes.setUnits(_C)
_AvgLatencyPerDomainLast60Minutes_Type=Counter32
_AvgLatencyPerDomainLast60Minutes_Object=MibTableColumn
avgLatencyPerDomainLast60Minutes=_AvgLatencyPerDomainLast60Minutes_Object((1,3,6,1,4,1,3417,2,15,4,1,1,20),_AvgLatencyPerDomainLast60Minutes_Type())
avgLatencyPerDomainLast60Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:avgLatencyPerDomainLast60Minutes.setStatus(_A)
if mibBuilder.loadTexts:avgLatencyPerDomainLast60Minutes.setUnits(_C)
_MaxLatencyPerDomainLast1Minute_Type=Counter32
_MaxLatencyPerDomainLast1Minute_Object=MibTableColumn
maxLatencyPerDomainLast1Minute=_MaxLatencyPerDomainLast1Minute_Object((1,3,6,1,4,1,3417,2,15,4,1,1,21),_MaxLatencyPerDomainLast1Minute_Type())
maxLatencyPerDomainLast1Minute.setMaxAccess(_B)
if mibBuilder.loadTexts:maxLatencyPerDomainLast1Minute.setStatus(_A)
if mibBuilder.loadTexts:maxLatencyPerDomainLast1Minute.setUnits(_C)
_MaxLatencyPerDomainLast3Minutes_Type=Counter32
_MaxLatencyPerDomainLast3Minutes_Object=MibTableColumn
maxLatencyPerDomainLast3Minutes=_MaxLatencyPerDomainLast3Minutes_Object((1,3,6,1,4,1,3417,2,15,4,1,1,22),_MaxLatencyPerDomainLast3Minutes_Type())
maxLatencyPerDomainLast3Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:maxLatencyPerDomainLast3Minutes.setStatus(_A)
if mibBuilder.loadTexts:maxLatencyPerDomainLast3Minutes.setUnits(_C)
_MaxLatencyPerDomainLast5Minutes_Type=Counter32
_MaxLatencyPerDomainLast5Minutes_Object=MibTableColumn
maxLatencyPerDomainLast5Minutes=_MaxLatencyPerDomainLast5Minutes_Object((1,3,6,1,4,1,3417,2,15,4,1,1,23),_MaxLatencyPerDomainLast5Minutes_Type())
maxLatencyPerDomainLast5Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:maxLatencyPerDomainLast5Minutes.setStatus(_A)
if mibBuilder.loadTexts:maxLatencyPerDomainLast5Minutes.setUnits(_C)
_MaxLatencyPerDomainLast15Minutes_Type=Counter32
_MaxLatencyPerDomainLast15Minutes_Object=MibTableColumn
maxLatencyPerDomainLast15Minutes=_MaxLatencyPerDomainLast15Minutes_Object((1,3,6,1,4,1,3417,2,15,4,1,1,24),_MaxLatencyPerDomainLast15Minutes_Type())
maxLatencyPerDomainLast15Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:maxLatencyPerDomainLast15Minutes.setStatus(_A)
if mibBuilder.loadTexts:maxLatencyPerDomainLast15Minutes.setUnits(_C)
_MaxLatencyPerDomainLast60Minutes_Type=Counter32
_MaxLatencyPerDomainLast60Minutes_Object=MibTableColumn
maxLatencyPerDomainLast60Minutes=_MaxLatencyPerDomainLast60Minutes_Object((1,3,6,1,4,1,3417,2,15,4,1,1,25),_MaxLatencyPerDomainLast60Minutes_Type())
maxLatencyPerDomainLast60Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:maxLatencyPerDomainLast60Minutes.setStatus(_A)
if mibBuilder.loadTexts:maxLatencyPerDomainLast60Minutes.setUnits(_C)
_MinLatencyPerDomainLast1Minute_Type=Counter32
_MinLatencyPerDomainLast1Minute_Object=MibTableColumn
minLatencyPerDomainLast1Minute=_MinLatencyPerDomainLast1Minute_Object((1,3,6,1,4,1,3417,2,15,4,1,1,26),_MinLatencyPerDomainLast1Minute_Type())
minLatencyPerDomainLast1Minute.setMaxAccess(_B)
if mibBuilder.loadTexts:minLatencyPerDomainLast1Minute.setStatus(_A)
if mibBuilder.loadTexts:minLatencyPerDomainLast1Minute.setUnits(_C)
_MinLatencyPerDomainLast3Minutes_Type=Counter32
_MinLatencyPerDomainLast3Minutes_Object=MibTableColumn
minLatencyPerDomainLast3Minutes=_MinLatencyPerDomainLast3Minutes_Object((1,3,6,1,4,1,3417,2,15,4,1,1,27),_MinLatencyPerDomainLast3Minutes_Type())
minLatencyPerDomainLast3Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:minLatencyPerDomainLast3Minutes.setStatus(_A)
if mibBuilder.loadTexts:minLatencyPerDomainLast3Minutes.setUnits(_C)
_MinLatencyPerDomainLast5Minutes_Type=Counter32
_MinLatencyPerDomainLast5Minutes_Object=MibTableColumn
minLatencyPerDomainLast5Minutes=_MinLatencyPerDomainLast5Minutes_Object((1,3,6,1,4,1,3417,2,15,4,1,1,28),_MinLatencyPerDomainLast5Minutes_Type())
minLatencyPerDomainLast5Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:minLatencyPerDomainLast5Minutes.setStatus(_A)
if mibBuilder.loadTexts:minLatencyPerDomainLast5Minutes.setUnits(_C)
_MinLatencyPerDomainLast15Minutes_Type=Counter32
_MinLatencyPerDomainLast15Minutes_Object=MibTableColumn
minLatencyPerDomainLast15Minutes=_MinLatencyPerDomainLast15Minutes_Object((1,3,6,1,4,1,3417,2,15,4,1,1,29),_MinLatencyPerDomainLast15Minutes_Type())
minLatencyPerDomainLast15Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:minLatencyPerDomainLast15Minutes.setStatus(_A)
if mibBuilder.loadTexts:minLatencyPerDomainLast15Minutes.setUnits(_C)
_MinLatencyPerDomainLast60Minutes_Type=Counter32
_MinLatencyPerDomainLast60Minutes_Object=MibTableColumn
minLatencyPerDomainLast60Minutes=_MinLatencyPerDomainLast60Minutes_Object((1,3,6,1,4,1,3417,2,15,4,1,1,30),_MinLatencyPerDomainLast60Minutes_Type())
minLatencyPerDomainLast60Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:minLatencyPerDomainLast60Minutes.setStatus(_A)
if mibBuilder.loadTexts:minLatencyPerDomainLast60Minutes.setUnits(_C)
_AuthNotifications_ObjectIdentity=ObjectIdentity
authNotifications=_AuthNotifications_ObjectIdentity((1,3,6,1,4,1,3417,2,15,5))
_AuthNotificationsPrefix_ObjectIdentity=ObjectIdentity
authNotificationsPrefix=_AuthNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,3417,2,15,5,0))
schannelLatencyTrap=NotificationType((1,3,6,1,4,1,3417,2,15,5,0,1))
schannelLatencyTrap.setObjects(*((_D,_J),(_D,'latencyType'),(_D,'latencyValue')))
if mibBuilder.loadTexts:schannelLatencyTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ToggleState':ToggleState,'bluecoatSGAuthentication':bluecoatSGAuthentication,'schannelStats':schannelStats,'schannelStatsTable':schannelStatsTable,'schannelStatsEntry':schannelStatsEntry,_G:schannelStatsIndex,_J:domainName,'domainStatus':domainStatus,'timeouts':timeouts,'transactions':transactions,'currentWaiters':currentWaiters,'maxWaiters':maxWaiters,'resets':resets,'lsaDomainControllerStats':lsaDomainControllerStats,'lsaDomainControllerStatsTable':lsaDomainControllerStatsTable,'lsaDomainControllerStatsEntry':lsaDomainControllerStatsEntry,_H:lsaDomainControllerStatsIndex,'domainControllerName':domainControllerName,'address':address,'siteName':siteName,'avgLDAPPingTime':avgLDAPPingTime,'lastLDAPPingTime':lastLDAPPingTime,'flags':flags,'schannelServerStats':schannelServerStats,'schannelServerStatsTable':schannelServerStatsTable,'schannelServerStatsEntry':schannelServerStatsEntry,_I:schannelServerStatsIndex,'serverName':serverName,'connectionsInUse':connectionsInUse,'availableConnections':availableConnections,'averageTransactions':averageTransactions,'authsByDomainLast1Minute':authsByDomainLast1Minute,'authsByDomainLast3Minutes':authsByDomainLast3Minutes,'authsByDomainLast5Minutes':authsByDomainLast5Minutes,'authsByDomainLast15Minutes':authsByDomainLast15Minutes,'authsByDomainLast60Minutes':authsByDomainLast60Minutes,'failedAuthsByDomainLast1Minute':failedAuthsByDomainLast1Minute,'failedAuthsByDomainLast3Minutes':failedAuthsByDomainLast3Minutes,'failedAuthsByDomainLast5Minutes':failedAuthsByDomainLast5Minutes,'failedAuthsByDomainLast15Minutes':failedAuthsByDomainLast15Minutes,'failedAuthsByDomainLast60Minutes':failedAuthsByDomainLast60Minutes,'avgLatencyPerDomainLast1Minute':avgLatencyPerDomainLast1Minute,'avgLatencyPerDomainLast3Minutes':avgLatencyPerDomainLast3Minutes,'avgLatencyPerDomainLast5Minutes':avgLatencyPerDomainLast5Minutes,'avgLatencyPerDomainLast15Minutes':avgLatencyPerDomainLast15Minutes,'avgLatencyPerDomainLast60Minutes':avgLatencyPerDomainLast60Minutes,'maxLatencyPerDomainLast1Minute':maxLatencyPerDomainLast1Minute,'maxLatencyPerDomainLast3Minutes':maxLatencyPerDomainLast3Minutes,'maxLatencyPerDomainLast5Minutes':maxLatencyPerDomainLast5Minutes,'maxLatencyPerDomainLast15Minutes':maxLatencyPerDomainLast15Minutes,'maxLatencyPerDomainLast60Minutes':maxLatencyPerDomainLast60Minutes,'minLatencyPerDomainLast1Minute':minLatencyPerDomainLast1Minute,'minLatencyPerDomainLast3Minutes':minLatencyPerDomainLast3Minutes,'minLatencyPerDomainLast5Minutes':minLatencyPerDomainLast5Minutes,'minLatencyPerDomainLast15Minutes':minLatencyPerDomainLast15Minutes,'minLatencyPerDomainLast60Minutes':minLatencyPerDomainLast60Minutes,'authNotifications':authNotifications,'authNotificationsPrefix':authNotificationsPrefix,'schannelLatencyTrap':schannelLatencyTrap})