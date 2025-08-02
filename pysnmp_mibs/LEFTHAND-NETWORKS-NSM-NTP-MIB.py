_L='lefthandNetworksNsmNtpGroup'
_K='ntpRowStatus'
_J='ntpServer'
_I='ntpPreferred'
_H='timeTimeZone'
_G='timeGMTTime'
_F='ntpCount'
_E='obsolete'
_D='ntpIndex'
_C='read-only'
_B='LEFTHAND-NETWORKS-NSM-NTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lhnModules,lhnNsm=mibBuilder.importSymbols('LEFTHAND-NETWORKS-GLOBAL-REG-MIB','lhnModules','lhnNsm')
lhnNsmNTP,=mibBuilder.importSymbols('LEFTHAND-NETWORKS-NSM-MIB','lhnNsmNTP')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
lhnNsmNTPModule=ModuleIdentity((1,3,6,1,4,1,9804,2,1,6))
if mibBuilder.loadTexts:lhnNsmNTPModule.setRevisions(('2013-11-19 00:00','2013-06-25 00:00','2012-09-04 00:00','2011-06-21 00:00','2010-09-07 00:00','2010-07-19 00:00','2009-11-20 00:00','2009-03-10 00:00','2008-01-24 00:00'))
_LhnNsmNTPModuleConformance_ObjectIdentity=ObjectIdentity
lhnNsmNTPModuleConformance=_LhnNsmNTPModuleConformance_ObjectIdentity((1,3,6,1,4,1,9804,2,1,6,1))
_LhnNsmNTPModuleCompliances_ObjectIdentity=ObjectIdentity
lhnNsmNTPModuleCompliances=_LhnNsmNTPModuleCompliances_ObjectIdentity((1,3,6,1,4,1,9804,2,1,6,1,1))
_LhnNsmNTPModuleGroups_ObjectIdentity=ObjectIdentity
lhnNsmNTPModuleGroups=_LhnNsmNTPModuleGroups_ObjectIdentity((1,3,6,1,4,1,9804,2,1,6,1,2))
_NtpCount_Type=Integer32
_NtpCount_Object=MibScalar
ntpCount=_NtpCount_Object((1,3,6,1,4,1,9804,3,1,1,2,5,1),_NtpCount_Type())
ntpCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpCount.setStatus(_A)
_NtpTable_Object=MibTable
ntpTable=_NtpTable_Object((1,3,6,1,4,1,9804,3,1,1,2,5,2))
if mibBuilder.loadTexts:ntpTable.setStatus(_A)
_NtpEntry_Object=MibTableRow
ntpEntry=_NtpEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,5,2,1))
ntpEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:ntpEntry.setStatus(_A)
_NtpIndex_Type=Unsigned32
_NtpIndex_Object=MibTableColumn
ntpIndex=_NtpIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,5,2,1,1),_NtpIndex_Type())
ntpIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ntpIndex.setStatus(_A)
_NtpPreferred_Type=TruthValue
_NtpPreferred_Object=MibTableColumn
ntpPreferred=_NtpPreferred_Object((1,3,6,1,4,1,9804,3,1,1,2,5,2,1,2),_NtpPreferred_Type())
ntpPreferred.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpPreferred.setStatus(_A)
_NtpServer_Type=DisplayString
_NtpServer_Object=MibTableColumn
ntpServer=_NtpServer_Object((1,3,6,1,4,1,9804,3,1,1,2,5,2,1,3),_NtpServer_Type())
ntpServer.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpServer.setStatus(_A)
_NtpRowStatus_Type=RowStatus
_NtpRowStatus_Object=MibTableColumn
ntpRowStatus=_NtpRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,5,2,1,4),_NtpRowStatus_Type())
ntpRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpRowStatus.setStatus(_E)
_TimeGMTTime_Type=DisplayString
_TimeGMTTime_Object=MibScalar
timeGMTTime=_TimeGMTTime_Object((1,3,6,1,4,1,9804,3,1,1,2,5,7),_TimeGMTTime_Type())
timeGMTTime.setMaxAccess(_C)
if mibBuilder.loadTexts:timeGMTTime.setStatus(_A)
_TimeTimeZone_Type=DisplayString
_TimeTimeZone_Object=MibScalar
timeTimeZone=_TimeTimeZone_Object((1,3,6,1,4,1,9804,3,1,1,2,5,8),_TimeTimeZone_Type())
timeTimeZone.setMaxAccess(_C)
if mibBuilder.loadTexts:timeTimeZone.setStatus(_A)
lefthandNetworksNsmNtpGroup=ObjectGroup((1,3,6,1,4,1,9804,2,1,6,1,2,1))
lefthandNetworksNsmNtpGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:lefthandNetworksNsmNtpGroup.setStatus(_A)
lefthandNetworksNsmNtpGroupObsolete=ObjectGroup((1,3,6,1,4,1,9804,2,1,6,1,2,2))
lefthandNetworksNsmNtpGroupObsolete.setObjects((_B,_K))
if mibBuilder.loadTexts:lefthandNetworksNsmNtpGroupObsolete.setStatus(_E)
lefthandNetworksNsmNTPMibCompliance=ModuleCompliance((1,3,6,1,4,1,9804,2,1,6,1,1,1))
lefthandNetworksNsmNTPMibCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:lefthandNetworksNsmNTPMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lhnNsmNTPModule':lhnNsmNTPModule,'lhnNsmNTPModuleConformance':lhnNsmNTPModuleConformance,'lhnNsmNTPModuleCompliances':lhnNsmNTPModuleCompliances,'lefthandNetworksNsmNTPMibCompliance':lefthandNetworksNsmNTPMibCompliance,'lhnNsmNTPModuleGroups':lhnNsmNTPModuleGroups,_L:lefthandNetworksNsmNtpGroup,'lefthandNetworksNsmNtpGroupObsolete':lefthandNetworksNsmNtpGroupObsolete,_F:ntpCount,'ntpTable':ntpTable,'ntpEntry':ntpEntry,_D:ntpIndex,_I:ntpPreferred,_J:ntpServer,_K:ntpRowStatus,_G:timeGMTTime,_H:timeTimeZone})