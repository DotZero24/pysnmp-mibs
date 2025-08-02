_U='me1200SyslogControlHistoryTableInfoGroup'
_T='me1200SyslogStatusHistoryTableInfoGroup'
_S='me1200SyslogConfigServerInfoGroup'
_R='me1200SyslogControlHistoryClear'
_Q='me1200SyslogStatusHistoryMsgText'
_P='me1200SyslogStatusHistoryMsgTimeStamp'
_O='me1200SyslogStatusHistoryMsgLevel'
_N='me1200SyslogConfigServerLevel'
_M='me1200SyslogConfigServerAddress'
_L='me1200SyslogConfigServerMode'
_K='me1200SyslogControlHistoryClearLevel'
_J='me1200SyslogControlHistorySwitchId'
_I='me1200SyslogStatusHistoryMsgId'
_H='me1200SyslogStatusHistorySwitchId'
_G='ME1200DisplayString'
_F='read-only'
_E='not-accessible'
_D='read-write'
_C='Integer32'
_B='ME1200-SYSLOG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
me1200SwitchMgmt,=mibBuilder.importSymbols('CISCOME1200-MIB','me1200SwitchMgmt')
ME1200DisplayString,ME1200InetAddress=mibBuilder.importSymbols('ME1200-TC',_G,'ME1200InetAddress')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
me1200SyslogMib=ModuleIdentity((1,3,6,1,4,1,9,9,815,1,37))
if mibBuilder.loadTexts:me1200SyslogMib.setRevisions(('2014-03-25 00:00',))
class ME1200SyslogLevelType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6,8)));namedValues=NamedValues(*(('error',3),('warning',4),('notice',5),('informational',6),('all',8)))
_Me1200SyslogMibObjects_ObjectIdentity=ObjectIdentity
me1200SyslogMibObjects=_Me1200SyslogMibObjects_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,37,1))
_Me1200SyslogConfig_ObjectIdentity=ObjectIdentity
me1200SyslogConfig=_Me1200SyslogConfig_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,37,1,2))
_Me1200SyslogConfigServer_ObjectIdentity=ObjectIdentity
me1200SyslogConfigServer=_Me1200SyslogConfigServer_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,37,1,2,1))
_Me1200SyslogConfigServerMode_Type=TruthValue
_Me1200SyslogConfigServerMode_Object=MibScalar
me1200SyslogConfigServerMode=_Me1200SyslogConfigServerMode_Object((1,3,6,1,4,1,9,9,815,1,37,1,2,1,1),_Me1200SyslogConfigServerMode_Type())
me1200SyslogConfigServerMode.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200SyslogConfigServerMode.setStatus(_A)
_Me1200SyslogConfigServerAddress_Type=ME1200InetAddress
_Me1200SyslogConfigServerAddress_Object=MibScalar
me1200SyslogConfigServerAddress=_Me1200SyslogConfigServerAddress_Object((1,3,6,1,4,1,9,9,815,1,37,1,2,1,2),_Me1200SyslogConfigServerAddress_Type())
me1200SyslogConfigServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200SyslogConfigServerAddress.setStatus(_A)
_Me1200SyslogConfigServerLevel_Type=ME1200SyslogLevelType
_Me1200SyslogConfigServerLevel_Object=MibScalar
me1200SyslogConfigServerLevel=_Me1200SyslogConfigServerLevel_Object((1,3,6,1,4,1,9,9,815,1,37,1,2,1,3),_Me1200SyslogConfigServerLevel_Type())
me1200SyslogConfigServerLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200SyslogConfigServerLevel.setStatus(_A)
_Me1200SyslogStatus_ObjectIdentity=ObjectIdentity
me1200SyslogStatus=_Me1200SyslogStatus_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,37,1,3))
_Me1200SyslogStatusHistoryTable_Object=MibTable
me1200SyslogStatusHistoryTable=_Me1200SyslogStatusHistoryTable_Object((1,3,6,1,4,1,9,9,815,1,37,1,3,1))
if mibBuilder.loadTexts:me1200SyslogStatusHistoryTable.setStatus(_A)
_Me1200SyslogStatusHistoryEntry_Object=MibTableRow
me1200SyslogStatusHistoryEntry=_Me1200SyslogStatusHistoryEntry_Object((1,3,6,1,4,1,9,9,815,1,37,1,3,1,1))
me1200SyslogStatusHistoryEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:me1200SyslogStatusHistoryEntry.setStatus(_A)
class _Me1200SyslogStatusHistorySwitchId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Me1200SyslogStatusHistorySwitchId_Type.__name__=_C
_Me1200SyslogStatusHistorySwitchId_Object=MibTableColumn
me1200SyslogStatusHistorySwitchId=_Me1200SyslogStatusHistorySwitchId_Object((1,3,6,1,4,1,9,9,815,1,37,1,3,1,1,1),_Me1200SyslogStatusHistorySwitchId_Type())
me1200SyslogStatusHistorySwitchId.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200SyslogStatusHistorySwitchId.setStatus(_A)
class _Me1200SyslogStatusHistoryMsgId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Me1200SyslogStatusHistoryMsgId_Type.__name__=_C
_Me1200SyslogStatusHistoryMsgId_Object=MibTableColumn
me1200SyslogStatusHistoryMsgId=_Me1200SyslogStatusHistoryMsgId_Object((1,3,6,1,4,1,9,9,815,1,37,1,3,1,1,2),_Me1200SyslogStatusHistoryMsgId_Type())
me1200SyslogStatusHistoryMsgId.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200SyslogStatusHistoryMsgId.setStatus(_A)
_Me1200SyslogStatusHistoryMsgLevel_Type=ME1200SyslogLevelType
_Me1200SyslogStatusHistoryMsgLevel_Object=MibTableColumn
me1200SyslogStatusHistoryMsgLevel=_Me1200SyslogStatusHistoryMsgLevel_Object((1,3,6,1,4,1,9,9,815,1,37,1,3,1,1,3),_Me1200SyslogStatusHistoryMsgLevel_Type())
me1200SyslogStatusHistoryMsgLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:me1200SyslogStatusHistoryMsgLevel.setStatus(_A)
_Me1200SyslogStatusHistoryMsgTimeStamp_Type=DateAndTime
_Me1200SyslogStatusHistoryMsgTimeStamp_Object=MibTableColumn
me1200SyslogStatusHistoryMsgTimeStamp=_Me1200SyslogStatusHistoryMsgTimeStamp_Object((1,3,6,1,4,1,9,9,815,1,37,1,3,1,1,4),_Me1200SyslogStatusHistoryMsgTimeStamp_Type())
me1200SyslogStatusHistoryMsgTimeStamp.setMaxAccess(_F)
if mibBuilder.loadTexts:me1200SyslogStatusHistoryMsgTimeStamp.setStatus(_A)
class _Me1200SyslogStatusHistoryMsgText_Type(ME1200DisplayString):subtypeSpec=ME1200DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Me1200SyslogStatusHistoryMsgText_Type.__name__=_G
_Me1200SyslogStatusHistoryMsgText_Object=MibTableColumn
me1200SyslogStatusHistoryMsgText=_Me1200SyslogStatusHistoryMsgText_Object((1,3,6,1,4,1,9,9,815,1,37,1,3,1,1,5),_Me1200SyslogStatusHistoryMsgText_Type())
me1200SyslogStatusHistoryMsgText.setMaxAccess(_F)
if mibBuilder.loadTexts:me1200SyslogStatusHistoryMsgText.setStatus(_A)
_Me1200SyslogControl_ObjectIdentity=ObjectIdentity
me1200SyslogControl=_Me1200SyslogControl_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,37,1,4))
_Me1200SyslogControlHistoryTable_Object=MibTable
me1200SyslogControlHistoryTable=_Me1200SyslogControlHistoryTable_Object((1,3,6,1,4,1,9,9,815,1,37,1,4,1))
if mibBuilder.loadTexts:me1200SyslogControlHistoryTable.setStatus(_A)
_Me1200SyslogControlHistoryEntry_Object=MibTableRow
me1200SyslogControlHistoryEntry=_Me1200SyslogControlHistoryEntry_Object((1,3,6,1,4,1,9,9,815,1,37,1,4,1,1))
me1200SyslogControlHistoryEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:me1200SyslogControlHistoryEntry.setStatus(_A)
class _Me1200SyslogControlHistorySwitchId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Me1200SyslogControlHistorySwitchId_Type.__name__=_C
_Me1200SyslogControlHistorySwitchId_Object=MibTableColumn
me1200SyslogControlHistorySwitchId=_Me1200SyslogControlHistorySwitchId_Object((1,3,6,1,4,1,9,9,815,1,37,1,4,1,1,1),_Me1200SyslogControlHistorySwitchId_Type())
me1200SyslogControlHistorySwitchId.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200SyslogControlHistorySwitchId.setStatus(_A)
_Me1200SyslogControlHistoryClearLevel_Type=ME1200SyslogLevelType
_Me1200SyslogControlHistoryClearLevel_Object=MibTableColumn
me1200SyslogControlHistoryClearLevel=_Me1200SyslogControlHistoryClearLevel_Object((1,3,6,1,4,1,9,9,815,1,37,1,4,1,1,2),_Me1200SyslogControlHistoryClearLevel_Type())
me1200SyslogControlHistoryClearLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200SyslogControlHistoryClearLevel.setStatus(_A)
_Me1200SyslogControlHistoryClear_Type=TruthValue
_Me1200SyslogControlHistoryClear_Object=MibTableColumn
me1200SyslogControlHistoryClear=_Me1200SyslogControlHistoryClear_Object((1,3,6,1,4,1,9,9,815,1,37,1,4,1,1,3),_Me1200SyslogControlHistoryClear_Type())
me1200SyslogControlHistoryClear.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200SyslogControlHistoryClear.setStatus(_A)
_Me1200SyslogMibConformance_ObjectIdentity=ObjectIdentity
me1200SyslogMibConformance=_Me1200SyslogMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,37,2))
_Me1200SyslogMibCompliances_ObjectIdentity=ObjectIdentity
me1200SyslogMibCompliances=_Me1200SyslogMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,37,2,1))
_Me1200SyslogMibGroups_ObjectIdentity=ObjectIdentity
me1200SyslogMibGroups=_Me1200SyslogMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,37,2,2))
me1200SyslogConfigServerInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,37,2,2,1))
me1200SyslogConfigServerInfoGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:me1200SyslogConfigServerInfoGroup.setStatus(_A)
me1200SyslogStatusHistoryTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,37,2,2,2))
me1200SyslogStatusHistoryTableInfoGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:me1200SyslogStatusHistoryTableInfoGroup.setStatus(_A)
me1200SyslogControlHistoryTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,37,2,2,3))
me1200SyslogControlHistoryTableInfoGroup.setObjects((_B,_R))
if mibBuilder.loadTexts:me1200SyslogControlHistoryTableInfoGroup.setStatus(_A)
me1200SyslogMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,815,1,37,2,1,1))
me1200SyslogMibCompliance.setObjects(*((_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:me1200SyslogMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ME1200SyslogLevelType':ME1200SyslogLevelType,'me1200SyslogMib':me1200SyslogMib,'me1200SyslogMibObjects':me1200SyslogMibObjects,'me1200SyslogConfig':me1200SyslogConfig,'me1200SyslogConfigServer':me1200SyslogConfigServer,_L:me1200SyslogConfigServerMode,_M:me1200SyslogConfigServerAddress,_N:me1200SyslogConfigServerLevel,'me1200SyslogStatus':me1200SyslogStatus,'me1200SyslogStatusHistoryTable':me1200SyslogStatusHistoryTable,'me1200SyslogStatusHistoryEntry':me1200SyslogStatusHistoryEntry,_H:me1200SyslogStatusHistorySwitchId,_I:me1200SyslogStatusHistoryMsgId,_O:me1200SyslogStatusHistoryMsgLevel,_P:me1200SyslogStatusHistoryMsgTimeStamp,_Q:me1200SyslogStatusHistoryMsgText,'me1200SyslogControl':me1200SyslogControl,'me1200SyslogControlHistoryTable':me1200SyslogControlHistoryTable,'me1200SyslogControlHistoryEntry':me1200SyslogControlHistoryEntry,_J:me1200SyslogControlHistorySwitchId,_K:me1200SyslogControlHistoryClearLevel,_R:me1200SyslogControlHistoryClear,'me1200SyslogMibConformance':me1200SyslogMibConformance,'me1200SyslogMibCompliances':me1200SyslogMibCompliances,'me1200SyslogMibCompliance':me1200SyslogMibCompliance,'me1200SyslogMibGroups':me1200SyslogMibGroups,_S:me1200SyslogConfigServerInfoGroup,_T:me1200SyslogStatusHistoryTableInfoGroup,_U:me1200SyslogControlHistoryTableInfoGroup})