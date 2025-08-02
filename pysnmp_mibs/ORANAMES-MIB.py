_F='applIndex'
_E='NETWORK-SERVICES-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
applIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class DateAndTime(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,11))
class TruthValue(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_Oracle_ObjectIdentity=ObjectIdentity
oracle=_Oracle_ObjectIdentity((1,3,6,1,4,1,111))
_OraNamesMIB_ObjectIdentity=ObjectIdentity
oraNamesMIB=_OraNamesMIB_ObjectIdentity((1,3,6,1,4,1,111,6))
_OraNamesObjects_ObjectIdentity=ObjectIdentity
oraNamesObjects=_OraNamesObjects_ObjectIdentity((1,3,6,1,4,1,111,6,1))
_OraNamesTNSTable_Object=MibTable
oraNamesTNSTable=_OraNamesTNSTable_Object((1,3,6,1,4,1,111,6,1,1))
if mibBuilder.loadTexts:oraNamesTNSTable.setStatus(_A)
_OraNamesTNSEntry_Object=MibTableRow
oraNamesTNSEntry=_OraNamesTNSEntry_Object((1,3,6,1,4,1,111,6,1,1,1))
oraNamesTNSEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:oraNamesTNSEntry.setStatus(_A)
_OraNamesTNSstartDate_Type=DateAndTime
_OraNamesTNSstartDate_Object=MibTableColumn
oraNamesTNSstartDate=_OraNamesTNSstartDate_Object((1,3,6,1,4,1,111,6,1,1,1,1),_OraNamesTNSstartDate_Type())
oraNamesTNSstartDate.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesTNSstartDate.setStatus(_A)
class _OraNamesTNStraceLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_OraNamesTNStraceLevel_Type.__name__=_D
_OraNamesTNStraceLevel_Object=MibTableColumn
oraNamesTNStraceLevel=_OraNamesTNStraceLevel_Object((1,3,6,1,4,1,111,6,1,1,1,2),_OraNamesTNStraceLevel_Type())
oraNamesTNStraceLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesTNStraceLevel.setStatus(_A)
class _OraNamesTNSsecurityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_OraNamesTNSsecurityLevel_Type.__name__=_D
_OraNamesTNSsecurityLevel_Object=MibTableColumn
oraNamesTNSsecurityLevel=_OraNamesTNSsecurityLevel_Object((1,3,6,1,4,1,111,6,1,1,1,3),_OraNamesTNSsecurityLevel_Type())
oraNamesTNSsecurityLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesTNSsecurityLevel.setStatus(_A)
_OraNamesTNSparameterFile_Type=DisplayString
_OraNamesTNSparameterFile_Object=MibTableColumn
oraNamesTNSparameterFile=_OraNamesTNSparameterFile_Object((1,3,6,1,4,1,111,6,1,1,1,4),_OraNamesTNSparameterFile_Type())
oraNamesTNSparameterFile.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesTNSparameterFile.setStatus(_A)
_OraNamesTNSlogFile_Type=DisplayString
_OraNamesTNSlogFile_Object=MibTableColumn
oraNamesTNSlogFile=_OraNamesTNSlogFile_Object((1,3,6,1,4,1,111,6,1,1,1,5),_OraNamesTNSlogFile_Type())
oraNamesTNSlogFile.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesTNSlogFile.setStatus(_A)
_OraNamesTNStraceFile_Type=DisplayString
_OraNamesTNStraceFile_Object=MibTableColumn
oraNamesTNStraceFile=_OraNamesTNStraceFile_Object((1,3,6,1,4,1,111,6,1,1,1,6),_OraNamesTNStraceFile_Type())
oraNamesTNStraceFile.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesTNStraceFile.setStatus(_A)
class _OraNamesTNSstate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_OraNamesTNSstate_Type.__name__=_D
_OraNamesTNSstate_Object=MibTableColumn
oraNamesTNSstate=_OraNamesTNSstate_Object((1,3,6,1,4,1,111,6,1,1,1,7),_OraNamesTNSstate_Type())
oraNamesTNSstate.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesTNSstate.setStatus(_A)
_OraNamesTNScontact_Type=DisplayString
_OraNamesTNScontact_Object=MibTableColumn
oraNamesTNScontact=_OraNamesTNScontact_Object((1,3,6,1,4,1,111,6,1,1,1,8),_OraNamesTNScontact_Type())
oraNamesTNScontact.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesTNScontact.setStatus(_A)
_OraNamesTNSlistenAddresses_Type=DisplayString
_OraNamesTNSlistenAddresses_Object=MibTableColumn
oraNamesTNSlistenAddresses=_OraNamesTNSlistenAddresses_Object((1,3,6,1,4,1,111,6,1,1,1,9),_OraNamesTNSlistenAddresses_Type())
oraNamesTNSlistenAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesTNSlistenAddresses.setStatus(_A)
_OraNamesTNSfailedListenAddresses_Type=DisplayString
_OraNamesTNSfailedListenAddresses_Object=MibTableColumn
oraNamesTNSfailedListenAddresses=_OraNamesTNSfailedListenAddresses_Object((1,3,6,1,4,1,111,6,1,1,1,10),_OraNamesTNSfailedListenAddresses_Type())
oraNamesTNSfailedListenAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesTNSfailedListenAddresses.setStatus(_A)
_OraNamesTNSreload_Type=TimeTicks
_OraNamesTNSreload_Object=MibTableColumn
oraNamesTNSreload=_OraNamesTNSreload_Object((1,3,6,1,4,1,111,6,1,1,1,11),_OraNamesTNSreload_Type())
oraNamesTNSreload.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesTNSreload.setStatus(_A)
class _OraNamesTNSrunningTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_OraNamesTNSrunningTime_Type.__name__=_D
_OraNamesTNSrunningTime_Object=MibTableColumn
oraNamesTNSrunningTime=_OraNamesTNSrunningTime_Object((1,3,6,1,4,1,111,6,1,1,1,12),_OraNamesTNSrunningTime_Type())
oraNamesTNSrunningTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesTNSrunningTime.setStatus(_A)
_OraNamesConfigTable_Object=MibTable
oraNamesConfigTable=_OraNamesConfigTable_Object((1,3,6,1,4,1,111,6,1,2))
if mibBuilder.loadTexts:oraNamesConfigTable.setStatus(_A)
_OraNamesConfigEntry_Object=MibTableRow
oraNamesConfigEntry=_OraNamesConfigEntry_Object((1,3,6,1,4,1,111,6,1,2,1))
oraNamesConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:oraNamesConfigEntry.setStatus(_A)
_OraNamesConfigAdminRegion_Type=DisplayString
_OraNamesConfigAdminRegion_Object=MibTableColumn
oraNamesConfigAdminRegion=_OraNamesConfigAdminRegion_Object((1,3,6,1,4,1,111,6,1,2,1,1),_OraNamesConfigAdminRegion_Type())
oraNamesConfigAdminRegion.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigAdminRegion.setStatus(_A)
_OraNamesConfigAuthorityRequired_Type=TruthValue
_OraNamesConfigAuthorityRequired_Object=MibTableColumn
oraNamesConfigAuthorityRequired=_OraNamesConfigAuthorityRequired_Object((1,3,6,1,4,1,111,6,1,2,1,2),_OraNamesConfigAuthorityRequired_Type())
oraNamesConfigAuthorityRequired.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigAuthorityRequired.setStatus(_A)
_OraNamesConfigAutoRefreshExpire_Type=TimeTicks
_OraNamesConfigAutoRefreshExpire_Object=MibTableColumn
oraNamesConfigAutoRefreshExpire=_OraNamesConfigAutoRefreshExpire_Object((1,3,6,1,4,1,111,6,1,2,1,3),_OraNamesConfigAutoRefreshExpire_Type())
oraNamesConfigAutoRefreshExpire.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigAutoRefreshExpire.setStatus(_A)
_OraNamesConfigAutoRefreshRetry_Type=TimeTicks
_OraNamesConfigAutoRefreshRetry_Object=MibTableColumn
oraNamesConfigAutoRefreshRetry=_OraNamesConfigAutoRefreshRetry_Object((1,3,6,1,4,1,111,6,1,2,1,4),_OraNamesConfigAutoRefreshRetry_Type())
oraNamesConfigAutoRefreshRetry.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigAutoRefreshRetry.setStatus(_A)
_OraNamesConfigCacheCheckpointFile_Type=DisplayString
_OraNamesConfigCacheCheckpointFile_Object=MibTableColumn
oraNamesConfigCacheCheckpointFile=_OraNamesConfigCacheCheckpointFile_Object((1,3,6,1,4,1,111,6,1,2,1,5),_OraNamesConfigCacheCheckpointFile_Type())
oraNamesConfigCacheCheckpointFile.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigCacheCheckpointFile.setStatus(_A)
_OraNamesConfigCacheCheckpointInterval_Type=TimeTicks
_OraNamesConfigCacheCheckpointInterval_Object=MibTableColumn
oraNamesConfigCacheCheckpointInterval=_OraNamesConfigCacheCheckpointInterval_Object((1,3,6,1,4,1,111,6,1,2,1,6),_OraNamesConfigCacheCheckpointInterval_Type())
oraNamesConfigCacheCheckpointInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigCacheCheckpointInterval.setStatus(_A)
_OraNamesConfigConfigCheckpointFile_Type=DisplayString
_OraNamesConfigConfigCheckpointFile_Object=MibTableColumn
oraNamesConfigConfigCheckpointFile=_OraNamesConfigConfigCheckpointFile_Object((1,3,6,1,4,1,111,6,1,2,1,7),_OraNamesConfigConfigCheckpointFile_Type())
oraNamesConfigConfigCheckpointFile.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigConfigCheckpointFile.setStatus(_A)
_OraNamesConfigDefaultForwarders_Type=DisplayString
_OraNamesConfigDefaultForwarders_Object=MibTableColumn
oraNamesConfigDefaultForwarders=_OraNamesConfigDefaultForwarders_Object((1,3,6,1,4,1,111,6,1,2,1,8),_OraNamesConfigDefaultForwarders_Type())
oraNamesConfigDefaultForwarders.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigDefaultForwarders.setStatus(_A)
_OraNamesConfigDefaultForwardersOnly_Type=TruthValue
_OraNamesConfigDefaultForwardersOnly_Object=MibTableColumn
oraNamesConfigDefaultForwardersOnly=_OraNamesConfigDefaultForwardersOnly_Object((1,3,6,1,4,1,111,6,1,2,1,9),_OraNamesConfigDefaultForwardersOnly_Type())
oraNamesConfigDefaultForwardersOnly.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigDefaultForwardersOnly.setStatus(_A)
_OraNamesConfigDomainCheckpointFile_Type=DisplayString
_OraNamesConfigDomainCheckpointFile_Object=MibTableColumn
oraNamesConfigDomainCheckpointFile=_OraNamesConfigDomainCheckpointFile_Object((1,3,6,1,4,1,111,6,1,2,1,10),_OraNamesConfigDomainCheckpointFile_Type())
oraNamesConfigDomainCheckpointFile.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigDomainCheckpointFile.setStatus(_A)
_OraNamesConfigDomainHints_Type=DisplayString
_OraNamesConfigDomainHints_Object=MibTableColumn
oraNamesConfigDomainHints=_OraNamesConfigDomainHints_Object((1,3,6,1,4,1,111,6,1,2,1,11),_OraNamesConfigDomainHints_Type())
oraNamesConfigDomainHints.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigDomainHints.setStatus(_A)
_OraNamesConfigDomains_Type=DisplayString
_OraNamesConfigDomains_Object=MibTableColumn
oraNamesConfigDomains=_OraNamesConfigDomains_Object((1,3,6,1,4,1,111,6,1,2,1,12),_OraNamesConfigDomains_Type())
oraNamesConfigDomains.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigDomains.setStatus(_A)
_OraNamesConfigForwardingAvailable_Type=TruthValue
_OraNamesConfigForwardingAvailable_Object=MibTableColumn
oraNamesConfigForwardingAvailable=_OraNamesConfigForwardingAvailable_Object((1,3,6,1,4,1,111,6,1,2,1,13),_OraNamesConfigForwardingAvailable_Type())
oraNamesConfigForwardingAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigForwardingAvailable.setStatus(_A)
_OraNamesConfigForwardingDesired_Type=TruthValue
_OraNamesConfigForwardingDesired_Object=MibTableColumn
oraNamesConfigForwardingDesired=_OraNamesConfigForwardingDesired_Object((1,3,6,1,4,1,111,6,1,2,1,14),_OraNamesConfigForwardingDesired_Type())
oraNamesConfigForwardingDesired.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigForwardingDesired.setStatus(_A)
_OraNamesConfigLogDirectory_Type=DisplayString
_OraNamesConfigLogDirectory_Object=MibTableColumn
oraNamesConfigLogDirectory=_OraNamesConfigLogDirectory_Object((1,3,6,1,4,1,111,6,1,2,1,15),_OraNamesConfigLogDirectory_Type())
oraNamesConfigLogDirectory.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigLogDirectory.setStatus(_A)
_OraNamesConfigLogStatsInterval_Type=TimeTicks
_OraNamesConfigLogStatsInterval_Object=MibTableColumn
oraNamesConfigLogStatsInterval=_OraNamesConfigLogStatsInterval_Object((1,3,6,1,4,1,111,6,1,2,1,16),_OraNamesConfigLogStatsInterval_Type())
oraNamesConfigLogStatsInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigLogStatsInterval.setStatus(_A)
_OraNamesConfigLogUnique_Type=TruthValue
_OraNamesConfigLogUnique_Object=MibTableColumn
oraNamesConfigLogUnique=_OraNamesConfigLogUnique_Object((1,3,6,1,4,1,111,6,1,2,1,17),_OraNamesConfigLogUnique_Type())
oraNamesConfigLogUnique.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigLogUnique.setStatus(_A)
class _OraNamesConfigMaxOpenConnections_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_OraNamesConfigMaxOpenConnections_Type.__name__=_D
_OraNamesConfigMaxOpenConnections_Object=MibTableColumn
oraNamesConfigMaxOpenConnections=_OraNamesConfigMaxOpenConnections_Object((1,3,6,1,4,1,111,6,1,2,1,18),_OraNamesConfigMaxOpenConnections_Type())
oraNamesConfigMaxOpenConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigMaxOpenConnections.setStatus(_A)
class _OraNamesConfigMaxReforwards_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_OraNamesConfigMaxReforwards_Type.__name__=_D
_OraNamesConfigMaxReforwards_Object=MibTableColumn
oraNamesConfigMaxReforwards=_OraNamesConfigMaxReforwards_Object((1,3,6,1,4,1,111,6,1,2,1,19),_OraNamesConfigMaxReforwards_Type())
oraNamesConfigMaxReforwards.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigMaxReforwards.setStatus(_A)
class _OraNamesConfigMessagePoolStartSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_OraNamesConfigMessagePoolStartSize_Type.__name__=_D
_OraNamesConfigMessagePoolStartSize_Object=MibTableColumn
oraNamesConfigMessagePoolStartSize=_OraNamesConfigMessagePoolStartSize_Object((1,3,6,1,4,1,111,6,1,2,1,20),_OraNamesConfigMessagePoolStartSize_Type())
oraNamesConfigMessagePoolStartSize.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigMessagePoolStartSize.setStatus(_A)
_OraNamesConfigNoModifyRequests_Type=TruthValue
_OraNamesConfigNoModifyRequests_Object=MibTableColumn
oraNamesConfigNoModifyRequests=_OraNamesConfigNoModifyRequests_Object((1,3,6,1,4,1,111,6,1,2,1,21),_OraNamesConfigNoModifyRequests_Type())
oraNamesConfigNoModifyRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigNoModifyRequests.setStatus(_A)
_OraNamesConfigNoRegionDatabase_Type=TruthValue
_OraNamesConfigNoRegionDatabase_Object=MibTableColumn
oraNamesConfigNoRegionDatabase=_OraNamesConfigNoRegionDatabase_Object((1,3,6,1,4,1,111,6,1,2,1,22),_OraNamesConfigNoRegionDatabase_Type())
oraNamesConfigNoRegionDatabase.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigNoRegionDatabase.setStatus(_A)
_OraNamesConfigResetStatsInterval_Type=TimeTicks
_OraNamesConfigResetStatsInterval_Object=MibTableColumn
oraNamesConfigResetStatsInterval=_OraNamesConfigResetStatsInterval_Object((1,3,6,1,4,1,111,6,1,2,1,23),_OraNamesConfigResetStatsInterval_Type())
oraNamesConfigResetStatsInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigResetStatsInterval.setStatus(_A)
_OraNamesConfigServerName_Type=DisplayString
_OraNamesConfigServerName_Object=MibTableColumn
oraNamesConfigServerName=_OraNamesConfigServerName_Object((1,3,6,1,4,1,111,6,1,2,1,24),_OraNamesConfigServerName_Type())
oraNamesConfigServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigServerName.setStatus(_A)
_OraNamesConfigTopologyCheckpointFile_Type=DisplayString
_OraNamesConfigTopologyCheckpointFile_Object=MibTableColumn
oraNamesConfigTopologyCheckpointFile=_OraNamesConfigTopologyCheckpointFile_Object((1,3,6,1,4,1,111,6,1,2,1,25),_OraNamesConfigTopologyCheckpointFile_Type())
oraNamesConfigTopologyCheckpointFile.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigTopologyCheckpointFile.setStatus(_A)
_OraNamesConfigTraceDirectory_Type=DisplayString
_OraNamesConfigTraceDirectory_Object=MibTableColumn
oraNamesConfigTraceDirectory=_OraNamesConfigTraceDirectory_Object((1,3,6,1,4,1,111,6,1,2,1,26),_OraNamesConfigTraceDirectory_Type())
oraNamesConfigTraceDirectory.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigTraceDirectory.setStatus(_A)
_OraNamesConfigTraceFunc_Type=DisplayString
_OraNamesConfigTraceFunc_Object=MibTableColumn
oraNamesConfigTraceFunc=_OraNamesConfigTraceFunc_Object((1,3,6,1,4,1,111,6,1,2,1,27),_OraNamesConfigTraceFunc_Type())
oraNamesConfigTraceFunc.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigTraceFunc.setStatus(_A)
class _OraNamesConfigTraceMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_OraNamesConfigTraceMask_Type.__name__=_D
_OraNamesConfigTraceMask_Object=MibTableColumn
oraNamesConfigTraceMask=_OraNamesConfigTraceMask_Object((1,3,6,1,4,1,111,6,1,2,1,28),_OraNamesConfigTraceMask_Type())
oraNamesConfigTraceMask.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigTraceMask.setStatus(_A)
_OraNamesConfigTraceUnique_Type=TruthValue
_OraNamesConfigTraceUnique_Object=MibTableColumn
oraNamesConfigTraceUnique=_OraNamesConfigTraceUnique_Object((1,3,6,1,4,1,111,6,1,2,1,29),_OraNamesConfigTraceUnique_Type())
oraNamesConfigTraceUnique.setMaxAccess(_C)
if mibBuilder.loadTexts:oraNamesConfigTraceUnique.setStatus(_A)
_OraNamesServerTable_Object=MibTable
oraNamesServerTable=_OraNamesServerTable_Object((1,3,6,1,4,1,111,6,1,3))
if mibBuilder.loadTexts:oraNamesServerTable.setStatus(_A)
_OraNamesServerEntry_Object=MibTableRow
oraNamesServerEntry=_OraNamesServerEntry_Object((1,3,6,1,4,1,111,6,1,3,1))
oraNamesServerEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:oraNamesServerEntry.setStatus(_A)
_OraNamesServerQueriesReceived_Type=Counter32
_OraNamesServerQueriesReceived_Object=MibTableColumn
oraNamesServerQueriesReceived=_OraNamesServerQueriesReceived_Object((1,3,6,1,4,1,111,6,1,3,1,1),_OraNamesServerQueriesReceived_Type())
oraNamesServerQueriesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerQueriesReceived.setStatus(_A)
_OraNamesServerLastNnamesNotFound_Type=DisplayString
_OraNamesServerLastNnamesNotFound_Object=MibTableColumn
oraNamesServerLastNnamesNotFound=_OraNamesServerLastNnamesNotFound_Object((1,3,6,1,4,1,111,6,1,3,1,2),_OraNamesServerLastNnamesNotFound_Type())
oraNamesServerLastNnamesNotFound.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerLastNnamesNotFound.setStatus(_A)
_OraNamesServerQueriesTotalTime_Type=TimeTicks
_OraNamesServerQueriesTotalTime_Object=MibTableColumn
oraNamesServerQueriesTotalTime=_OraNamesServerQueriesTotalTime_Object((1,3,6,1,4,1,111,6,1,3,1,3),_OraNamesServerQueriesTotalTime_Type())
oraNamesServerQueriesTotalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerQueriesTotalTime.setStatus(_A)
_OraNamesServerDeletesReceived_Type=Counter32
_OraNamesServerDeletesReceived_Object=MibTableColumn
oraNamesServerDeletesReceived=_OraNamesServerDeletesReceived_Object((1,3,6,1,4,1,111,6,1,3,1,4),_OraNamesServerDeletesReceived_Type())
oraNamesServerDeletesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerDeletesReceived.setStatus(_A)
_OraNamesServerDeletesRefused_Type=Counter32
_OraNamesServerDeletesRefused_Object=MibTableColumn
oraNamesServerDeletesRefused=_OraNamesServerDeletesRefused_Object((1,3,6,1,4,1,111,6,1,3,1,5),_OraNamesServerDeletesRefused_Type())
oraNamesServerDeletesRefused.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerDeletesRefused.setStatus(_A)
_OraNamesServerDeletesTotalTime_Type=TimeTicks
_OraNamesServerDeletesTotalTime_Object=MibTableColumn
oraNamesServerDeletesTotalTime=_OraNamesServerDeletesTotalTime_Object((1,3,6,1,4,1,111,6,1,3,1,6),_OraNamesServerDeletesTotalTime_Type())
oraNamesServerDeletesTotalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerDeletesTotalTime.setStatus(_A)
_OraNamesServerRenamesReceived_Type=Counter32
_OraNamesServerRenamesReceived_Object=MibTableColumn
oraNamesServerRenamesReceived=_OraNamesServerRenamesReceived_Object((1,3,6,1,4,1,111,6,1,3,1,7),_OraNamesServerRenamesReceived_Type())
oraNamesServerRenamesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerRenamesReceived.setStatus(_A)
_OraNamesServerRenamesRefused_Type=Counter32
_OraNamesServerRenamesRefused_Object=MibTableColumn
oraNamesServerRenamesRefused=_OraNamesServerRenamesRefused_Object((1,3,6,1,4,1,111,6,1,3,1,8),_OraNamesServerRenamesRefused_Type())
oraNamesServerRenamesRefused.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerRenamesRefused.setStatus(_A)
_OraNamesServerRenamesTotalTime_Type=TimeTicks
_OraNamesServerRenamesTotalTime_Object=MibTableColumn
oraNamesServerRenamesTotalTime=_OraNamesServerRenamesTotalTime_Object((1,3,6,1,4,1,111,6,1,3,1,9),_OraNamesServerRenamesTotalTime_Type())
oraNamesServerRenamesTotalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerRenamesTotalTime.setStatus(_A)
_OraNamesServerUpdatesReceived_Type=Counter32
_OraNamesServerUpdatesReceived_Object=MibTableColumn
oraNamesServerUpdatesReceived=_OraNamesServerUpdatesReceived_Object((1,3,6,1,4,1,111,6,1,3,1,10),_OraNamesServerUpdatesReceived_Type())
oraNamesServerUpdatesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerUpdatesReceived.setStatus(_A)
_OraNamesServerUpdatesRefused_Type=Counter32
_OraNamesServerUpdatesRefused_Object=MibTableColumn
oraNamesServerUpdatesRefused=_OraNamesServerUpdatesRefused_Object((1,3,6,1,4,1,111,6,1,3,1,11),_OraNamesServerUpdatesRefused_Type())
oraNamesServerUpdatesRefused.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerUpdatesRefused.setStatus(_A)
_OraNamesServerUpdatesTotalTime_Type=TimeTicks
_OraNamesServerUpdatesTotalTime_Object=MibTableColumn
oraNamesServerUpdatesTotalTime=_OraNamesServerUpdatesTotalTime_Object((1,3,6,1,4,1,111,6,1,3,1,12),_OraNamesServerUpdatesTotalTime_Type())
oraNamesServerUpdatesTotalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerUpdatesTotalTime.setStatus(_A)
_OraNamesServerCorruptMessagesReceived_Type=Counter32
_OraNamesServerCorruptMessagesReceived_Object=MibTableColumn
oraNamesServerCorruptMessagesReceived=_OraNamesServerCorruptMessagesReceived_Object((1,3,6,1,4,1,111,6,1,3,1,13),_OraNamesServerCorruptMessagesReceived_Type())
oraNamesServerCorruptMessagesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerCorruptMessagesReceived.setStatus(_A)
_OraNamesServerResponsesSent_Type=Counter32
_OraNamesServerResponsesSent_Object=MibTableColumn
oraNamesServerResponsesSent=_OraNamesServerResponsesSent_Object((1,3,6,1,4,1,111,6,1,3,1,14),_OraNamesServerResponsesSent_Type())
oraNamesServerResponsesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerResponsesSent.setStatus(_A)
_OraNamesServerErrorResponsesSent_Type=Counter32
_OraNamesServerErrorResponsesSent_Object=MibTableColumn
oraNamesServerErrorResponsesSent=_OraNamesServerErrorResponsesSent_Object((1,3,6,1,4,1,111,6,1,3,1,15),_OraNamesServerErrorResponsesSent_Type())
oraNamesServerErrorResponsesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerErrorResponsesSent.setStatus(_A)
_OraNamesServerAliasLoopsDetected_Type=Counter32
_OraNamesServerAliasLoopsDetected_Object=MibTableColumn
oraNamesServerAliasLoopsDetected=_OraNamesServerAliasLoopsDetected_Object((1,3,6,1,4,1,111,6,1,3,1,16),_OraNamesServerAliasLoopsDetected_Type())
oraNamesServerAliasLoopsDetected.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerAliasLoopsDetected.setStatus(_A)
_OraNamesServerLookupsAttempted_Type=Counter32
_OraNamesServerLookupsAttempted_Object=MibTableColumn
oraNamesServerLookupsAttempted=_OraNamesServerLookupsAttempted_Object((1,3,6,1,4,1,111,6,1,3,1,17),_OraNamesServerLookupsAttempted_Type())
oraNamesServerLookupsAttempted.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerLookupsAttempted.setStatus(_A)
_OraNamesServerCreatedOnLookup_Type=Counter32
_OraNamesServerCreatedOnLookup_Object=MibTableColumn
oraNamesServerCreatedOnLookup=_OraNamesServerCreatedOnLookup_Object((1,3,6,1,4,1,111,6,1,3,1,18),_OraNamesServerCreatedOnLookup_Type())
oraNamesServerCreatedOnLookup.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerCreatedOnLookup.setStatus(_A)
_OraNamesServerLookupFailures_Type=Counter32
_OraNamesServerLookupFailures_Object=MibTableColumn
oraNamesServerLookupFailures=_OraNamesServerLookupFailures_Object((1,3,6,1,4,1,111,6,1,3,1,19),_OraNamesServerLookupFailures_Type())
oraNamesServerLookupFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerLookupFailures.setStatus(_A)
_OraNamesServerExactMatches_Type=Counter32
_OraNamesServerExactMatches_Object=MibTableColumn
oraNamesServerExactMatches=_OraNamesServerExactMatches_Object((1,3,6,1,4,1,111,6,1,3,1,20),_OraNamesServerExactMatches_Type())
oraNamesServerExactMatches.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerExactMatches.setStatus(_A)
_OraNamesServerForwardFailures_Type=Counter32
_OraNamesServerForwardFailures_Object=MibTableColumn
oraNamesServerForwardFailures=_OraNamesServerForwardFailures_Object((1,3,6,1,4,1,111,6,1,3,1,21),_OraNamesServerForwardFailures_Type())
oraNamesServerForwardFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerForwardFailures.setStatus(_A)
_OraNamesServerForwardTimeouts_Type=Counter32
_OraNamesServerForwardTimeouts_Object=MibTableColumn
oraNamesServerForwardTimeouts=_OraNamesServerForwardTimeouts_Object((1,3,6,1,4,1,111,6,1,3,1,22),_OraNamesServerForwardTimeouts_Type())
oraNamesServerForwardTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerForwardTimeouts.setStatus(_A)
_OraNamesServerResponsesReceived_Type=Counter32
_OraNamesServerResponsesReceived_Object=MibTableColumn
oraNamesServerResponsesReceived=_OraNamesServerResponsesReceived_Object((1,3,6,1,4,1,111,6,1,3,1,23),_OraNamesServerResponsesReceived_Type())
oraNamesServerResponsesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerResponsesReceived.setStatus(_A)
_OraNamesServerErrorResponsesReceived_Type=Counter32
_OraNamesServerErrorResponsesReceived_Object=MibTableColumn
oraNamesServerErrorResponsesReceived=_OraNamesServerErrorResponsesReceived_Object((1,3,6,1,4,1,111,6,1,3,1,24),_OraNamesServerErrorResponsesReceived_Type())
oraNamesServerErrorResponsesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerErrorResponsesReceived.setStatus(_A)
_OraNamesServerRequestsForwarded_Type=Counter32
_OraNamesServerRequestsForwarded_Object=MibTableColumn
oraNamesServerRequestsForwarded=_OraNamesServerRequestsForwarded_Object((1,3,6,1,4,1,111,6,1,3,1,25),_OraNamesServerRequestsForwarded_Type())
oraNamesServerRequestsForwarded.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerRequestsForwarded.setStatus(_A)
_OraNamesServerLastReload_Type=DateAndTime
_OraNamesServerLastReload_Object=MibTableColumn
oraNamesServerLastReload=_OraNamesServerLastReload_Object((1,3,6,1,4,1,111,6,1,3,1,26),_OraNamesServerLastReload_Type())
oraNamesServerLastReload.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerLastReload.setStatus(_A)
_OraNamesServerReloadCheckFailures_Type=Counter32
_OraNamesServerReloadCheckFailures_Object=MibTableColumn
oraNamesServerReloadCheckFailures=_OraNamesServerReloadCheckFailures_Object((1,3,6,1,4,1,111,6,1,3,1,27),_OraNamesServerReloadCheckFailures_Type())
oraNamesServerReloadCheckFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerReloadCheckFailures.setStatus(_A)
_OraNamesServerLastCheckpoint_Type=DateAndTime
_OraNamesServerLastCheckpoint_Object=MibTableColumn
oraNamesServerLastCheckpoint=_OraNamesServerLastCheckpoint_Object((1,3,6,1,4,1,111,6,1,3,1,28),_OraNamesServerLastCheckpoint_Type())
oraNamesServerLastCheckpoint.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerLastCheckpoint.setStatus(_A)
_OraNamesServerName_Type=DisplayString
_OraNamesServerName_Object=MibTableColumn
oraNamesServerName=_OraNamesServerName_Object((1,3,6,1,4,1,111,6,1,3,1,29),_OraNamesServerName_Type())
oraNamesServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerName.setStatus(_A)
_OraNamesServerAdminRegion_Type=DisplayString
_OraNamesServerAdminRegion_Object=MibTableColumn
oraNamesServerAdminRegion=_OraNamesServerAdminRegion_Object((1,3,6,1,4,1,111,6,1,3,1,30),_OraNamesServerAdminRegion_Type())
oraNamesServerAdminRegion.setMaxAccess(_B)
if mibBuilder.loadTexts:oraNamesServerAdminRegion.setStatus(_A)
mibBuilder.exportSymbols('ORANAMES-MIB',**{'DateAndTime':DateAndTime,'TruthValue':TruthValue,'oracle':oracle,'oraNamesMIB':oraNamesMIB,'oraNamesObjects':oraNamesObjects,'oraNamesTNSTable':oraNamesTNSTable,'oraNamesTNSEntry':oraNamesTNSEntry,'oraNamesTNSstartDate':oraNamesTNSstartDate,'oraNamesTNStraceLevel':oraNamesTNStraceLevel,'oraNamesTNSsecurityLevel':oraNamesTNSsecurityLevel,'oraNamesTNSparameterFile':oraNamesTNSparameterFile,'oraNamesTNSlogFile':oraNamesTNSlogFile,'oraNamesTNStraceFile':oraNamesTNStraceFile,'oraNamesTNSstate':oraNamesTNSstate,'oraNamesTNScontact':oraNamesTNScontact,'oraNamesTNSlistenAddresses':oraNamesTNSlistenAddresses,'oraNamesTNSfailedListenAddresses':oraNamesTNSfailedListenAddresses,'oraNamesTNSreload':oraNamesTNSreload,'oraNamesTNSrunningTime':oraNamesTNSrunningTime,'oraNamesConfigTable':oraNamesConfigTable,'oraNamesConfigEntry':oraNamesConfigEntry,'oraNamesConfigAdminRegion':oraNamesConfigAdminRegion,'oraNamesConfigAuthorityRequired':oraNamesConfigAuthorityRequired,'oraNamesConfigAutoRefreshExpire':oraNamesConfigAutoRefreshExpire,'oraNamesConfigAutoRefreshRetry':oraNamesConfigAutoRefreshRetry,'oraNamesConfigCacheCheckpointFile':oraNamesConfigCacheCheckpointFile,'oraNamesConfigCacheCheckpointInterval':oraNamesConfigCacheCheckpointInterval,'oraNamesConfigConfigCheckpointFile':oraNamesConfigConfigCheckpointFile,'oraNamesConfigDefaultForwarders':oraNamesConfigDefaultForwarders,'oraNamesConfigDefaultForwardersOnly':oraNamesConfigDefaultForwardersOnly,'oraNamesConfigDomainCheckpointFile':oraNamesConfigDomainCheckpointFile,'oraNamesConfigDomainHints':oraNamesConfigDomainHints,'oraNamesConfigDomains':oraNamesConfigDomains,'oraNamesConfigForwardingAvailable':oraNamesConfigForwardingAvailable,'oraNamesConfigForwardingDesired':oraNamesConfigForwardingDesired,'oraNamesConfigLogDirectory':oraNamesConfigLogDirectory,'oraNamesConfigLogStatsInterval':oraNamesConfigLogStatsInterval,'oraNamesConfigLogUnique':oraNamesConfigLogUnique,'oraNamesConfigMaxOpenConnections':oraNamesConfigMaxOpenConnections,'oraNamesConfigMaxReforwards':oraNamesConfigMaxReforwards,'oraNamesConfigMessagePoolStartSize':oraNamesConfigMessagePoolStartSize,'oraNamesConfigNoModifyRequests':oraNamesConfigNoModifyRequests,'oraNamesConfigNoRegionDatabase':oraNamesConfigNoRegionDatabase,'oraNamesConfigResetStatsInterval':oraNamesConfigResetStatsInterval,'oraNamesConfigServerName':oraNamesConfigServerName,'oraNamesConfigTopologyCheckpointFile':oraNamesConfigTopologyCheckpointFile,'oraNamesConfigTraceDirectory':oraNamesConfigTraceDirectory,'oraNamesConfigTraceFunc':oraNamesConfigTraceFunc,'oraNamesConfigTraceMask':oraNamesConfigTraceMask,'oraNamesConfigTraceUnique':oraNamesConfigTraceUnique,'oraNamesServerTable':oraNamesServerTable,'oraNamesServerEntry':oraNamesServerEntry,'oraNamesServerQueriesReceived':oraNamesServerQueriesReceived,'oraNamesServerLastNnamesNotFound':oraNamesServerLastNnamesNotFound,'oraNamesServerQueriesTotalTime':oraNamesServerQueriesTotalTime,'oraNamesServerDeletesReceived':oraNamesServerDeletesReceived,'oraNamesServerDeletesRefused':oraNamesServerDeletesRefused,'oraNamesServerDeletesTotalTime':oraNamesServerDeletesTotalTime,'oraNamesServerRenamesReceived':oraNamesServerRenamesReceived,'oraNamesServerRenamesRefused':oraNamesServerRenamesRefused,'oraNamesServerRenamesTotalTime':oraNamesServerRenamesTotalTime,'oraNamesServerUpdatesReceived':oraNamesServerUpdatesReceived,'oraNamesServerUpdatesRefused':oraNamesServerUpdatesRefused,'oraNamesServerUpdatesTotalTime':oraNamesServerUpdatesTotalTime,'oraNamesServerCorruptMessagesReceived':oraNamesServerCorruptMessagesReceived,'oraNamesServerResponsesSent':oraNamesServerResponsesSent,'oraNamesServerErrorResponsesSent':oraNamesServerErrorResponsesSent,'oraNamesServerAliasLoopsDetected':oraNamesServerAliasLoopsDetected,'oraNamesServerLookupsAttempted':oraNamesServerLookupsAttempted,'oraNamesServerCreatedOnLookup':oraNamesServerCreatedOnLookup,'oraNamesServerLookupFailures':oraNamesServerLookupFailures,'oraNamesServerExactMatches':oraNamesServerExactMatches,'oraNamesServerForwardFailures':oraNamesServerForwardFailures,'oraNamesServerForwardTimeouts':oraNamesServerForwardTimeouts,'oraNamesServerResponsesReceived':oraNamesServerResponsesReceived,'oraNamesServerErrorResponsesReceived':oraNamesServerErrorResponsesReceived,'oraNamesServerRequestsForwarded':oraNamesServerRequestsForwarded,'oraNamesServerLastReload':oraNamesServerLastReload,'oraNamesServerReloadCheckFailures':oraNamesServerReloadCheckFailures,'oraNamesServerLastCheckpoint':oraNamesServerLastCheckpoint,'oraNamesServerName':oraNamesServerName,'oraNamesServerAdminRegion':oraNamesServerAdminRegion})