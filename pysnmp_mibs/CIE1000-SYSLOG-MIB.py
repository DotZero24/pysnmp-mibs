_U='cie1000SyslogControlHistoryTableInfoGroup'
_T='cie1000SyslogStatusHistoryTableInfoGroup'
_S='cie1000SyslogConfigServerInfoGroup'
_R='cie1000SyslogControlHistoryClear'
_Q='cie1000SyslogStatusHistoryMsgText'
_P='cie1000SyslogStatusHistoryMsgTimeStamp'
_O='cie1000SyslogStatusHistoryMsgLevel'
_N='cie1000SyslogConfigServerLevel'
_M='cie1000SyslogConfigServerAddress'
_L='cie1000SyslogConfigServerMode'
_K='CIE1000DisplayString'
_J='cie1000SyslogControlHistoryClearLevel'
_I='cie1000SyslogControlHistorySwitchId'
_H='read-only'
_G='cie1000SyslogStatusHistoryMsgId'
_F='cie1000SyslogStatusHistorySwitchId'
_E='accessible-for-notify'
_D='read-write'
_C='Integer32'
_B='CIE1000-SYSLOG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CIE1000DisplayString,CIE1000InetAddress=mibBuilder.importSymbols('CIE1000-TC',_K,'CIE1000InetAddress')
cie1000SwitchMgmt,=mibBuilder.importSymbols('CISCO-IE1000-MIB','cie1000SwitchMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
cie1000SyslogMib=ModuleIdentity((1,3,6,1,4,1,9,9,832,1,37))
if mibBuilder.loadTexts:cie1000SyslogMib.setRevisions(('2014-07-01 00:00',))
class CIE1000SyslogLevelType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,8)));namedValues=NamedValues(*(('critical',2),('error',3),('warning',4),('notice',5),('informational',6),('all',8)))
_Cie1000SyslogMibObjects_ObjectIdentity=ObjectIdentity
cie1000SyslogMibObjects=_Cie1000SyslogMibObjects_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,37,1))
_Cie1000SyslogConfig_ObjectIdentity=ObjectIdentity
cie1000SyslogConfig=_Cie1000SyslogConfig_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,37,1,2))
_Cie1000SyslogConfigServer_ObjectIdentity=ObjectIdentity
cie1000SyslogConfigServer=_Cie1000SyslogConfigServer_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,37,1,2,1))
_Cie1000SyslogConfigServerMode_Type=TruthValue
_Cie1000SyslogConfigServerMode_Object=MibScalar
cie1000SyslogConfigServerMode=_Cie1000SyslogConfigServerMode_Object((1,3,6,1,4,1,9,9,832,1,37,1,2,1,1),_Cie1000SyslogConfigServerMode_Type())
cie1000SyslogConfigServerMode.setMaxAccess(_D)
if mibBuilder.loadTexts:cie1000SyslogConfigServerMode.setStatus(_A)
_Cie1000SyslogConfigServerAddress_Type=CIE1000InetAddress
_Cie1000SyslogConfigServerAddress_Object=MibScalar
cie1000SyslogConfigServerAddress=_Cie1000SyslogConfigServerAddress_Object((1,3,6,1,4,1,9,9,832,1,37,1,2,1,2),_Cie1000SyslogConfigServerAddress_Type())
cie1000SyslogConfigServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cie1000SyslogConfigServerAddress.setStatus(_A)
_Cie1000SyslogConfigServerLevel_Type=CIE1000SyslogLevelType
_Cie1000SyslogConfigServerLevel_Object=MibScalar
cie1000SyslogConfigServerLevel=_Cie1000SyslogConfigServerLevel_Object((1,3,6,1,4,1,9,9,832,1,37,1,2,1,3),_Cie1000SyslogConfigServerLevel_Type())
cie1000SyslogConfigServerLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:cie1000SyslogConfigServerLevel.setStatus(_A)
_Cie1000SyslogStatus_ObjectIdentity=ObjectIdentity
cie1000SyslogStatus=_Cie1000SyslogStatus_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,37,1,3))
_Cie1000SyslogStatusHistoryTable_Object=MibTable
cie1000SyslogStatusHistoryTable=_Cie1000SyslogStatusHistoryTable_Object((1,3,6,1,4,1,9,9,832,1,37,1,3,1))
if mibBuilder.loadTexts:cie1000SyslogStatusHistoryTable.setStatus(_A)
_Cie1000SyslogStatusHistoryEntry_Object=MibTableRow
cie1000SyslogStatusHistoryEntry=_Cie1000SyslogStatusHistoryEntry_Object((1,3,6,1,4,1,9,9,832,1,37,1,3,1,1))
cie1000SyslogStatusHistoryEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:cie1000SyslogStatusHistoryEntry.setStatus(_A)
class _Cie1000SyslogStatusHistorySwitchId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cie1000SyslogStatusHistorySwitchId_Type.__name__=_C
_Cie1000SyslogStatusHistorySwitchId_Object=MibTableColumn
cie1000SyslogStatusHistorySwitchId=_Cie1000SyslogStatusHistorySwitchId_Object((1,3,6,1,4,1,9,9,832,1,37,1,3,1,1,1),_Cie1000SyslogStatusHistorySwitchId_Type())
cie1000SyslogStatusHistorySwitchId.setMaxAccess(_E)
if mibBuilder.loadTexts:cie1000SyslogStatusHistorySwitchId.setStatus(_A)
class _Cie1000SyslogStatusHistoryMsgId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cie1000SyslogStatusHistoryMsgId_Type.__name__=_C
_Cie1000SyslogStatusHistoryMsgId_Object=MibTableColumn
cie1000SyslogStatusHistoryMsgId=_Cie1000SyslogStatusHistoryMsgId_Object((1,3,6,1,4,1,9,9,832,1,37,1,3,1,1,2),_Cie1000SyslogStatusHistoryMsgId_Type())
cie1000SyslogStatusHistoryMsgId.setMaxAccess(_E)
if mibBuilder.loadTexts:cie1000SyslogStatusHistoryMsgId.setStatus(_A)
_Cie1000SyslogStatusHistoryMsgLevel_Type=CIE1000SyslogLevelType
_Cie1000SyslogStatusHistoryMsgLevel_Object=MibTableColumn
cie1000SyslogStatusHistoryMsgLevel=_Cie1000SyslogStatusHistoryMsgLevel_Object((1,3,6,1,4,1,9,9,832,1,37,1,3,1,1,3),_Cie1000SyslogStatusHistoryMsgLevel_Type())
cie1000SyslogStatusHistoryMsgLevel.setMaxAccess(_H)
if mibBuilder.loadTexts:cie1000SyslogStatusHistoryMsgLevel.setStatus(_A)
_Cie1000SyslogStatusHistoryMsgTimeStamp_Type=DateAndTime
_Cie1000SyslogStatusHistoryMsgTimeStamp_Object=MibTableColumn
cie1000SyslogStatusHistoryMsgTimeStamp=_Cie1000SyslogStatusHistoryMsgTimeStamp_Object((1,3,6,1,4,1,9,9,832,1,37,1,3,1,1,4),_Cie1000SyslogStatusHistoryMsgTimeStamp_Type())
cie1000SyslogStatusHistoryMsgTimeStamp.setMaxAccess(_H)
if mibBuilder.loadTexts:cie1000SyslogStatusHistoryMsgTimeStamp.setStatus(_A)
class _Cie1000SyslogStatusHistoryMsgText_Type(CIE1000DisplayString):subtypeSpec=CIE1000DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4000))
_Cie1000SyslogStatusHistoryMsgText_Type.__name__=_K
_Cie1000SyslogStatusHistoryMsgText_Object=MibTableColumn
cie1000SyslogStatusHistoryMsgText=_Cie1000SyslogStatusHistoryMsgText_Object((1,3,6,1,4,1,9,9,832,1,37,1,3,1,1,5),_Cie1000SyslogStatusHistoryMsgText_Type())
cie1000SyslogStatusHistoryMsgText.setMaxAccess(_H)
if mibBuilder.loadTexts:cie1000SyslogStatusHistoryMsgText.setStatus(_A)
_Cie1000SyslogControl_ObjectIdentity=ObjectIdentity
cie1000SyslogControl=_Cie1000SyslogControl_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,37,1,4))
_Cie1000SyslogControlHistoryTable_Object=MibTable
cie1000SyslogControlHistoryTable=_Cie1000SyslogControlHistoryTable_Object((1,3,6,1,4,1,9,9,832,1,37,1,4,1))
if mibBuilder.loadTexts:cie1000SyslogControlHistoryTable.setStatus(_A)
_Cie1000SyslogControlHistoryEntry_Object=MibTableRow
cie1000SyslogControlHistoryEntry=_Cie1000SyslogControlHistoryEntry_Object((1,3,6,1,4,1,9,9,832,1,37,1,4,1,1))
cie1000SyslogControlHistoryEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:cie1000SyslogControlHistoryEntry.setStatus(_A)
class _Cie1000SyslogControlHistorySwitchId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cie1000SyslogControlHistorySwitchId_Type.__name__=_C
_Cie1000SyslogControlHistorySwitchId_Object=MibTableColumn
cie1000SyslogControlHistorySwitchId=_Cie1000SyslogControlHistorySwitchId_Object((1,3,6,1,4,1,9,9,832,1,37,1,4,1,1,1),_Cie1000SyslogControlHistorySwitchId_Type())
cie1000SyslogControlHistorySwitchId.setMaxAccess(_E)
if mibBuilder.loadTexts:cie1000SyslogControlHistorySwitchId.setStatus(_A)
_Cie1000SyslogControlHistoryClearLevel_Type=CIE1000SyslogLevelType
_Cie1000SyslogControlHistoryClearLevel_Object=MibTableColumn
cie1000SyslogControlHistoryClearLevel=_Cie1000SyslogControlHistoryClearLevel_Object((1,3,6,1,4,1,9,9,832,1,37,1,4,1,1,2),_Cie1000SyslogControlHistoryClearLevel_Type())
cie1000SyslogControlHistoryClearLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:cie1000SyslogControlHistoryClearLevel.setStatus(_A)
_Cie1000SyslogControlHistoryClear_Type=TruthValue
_Cie1000SyslogControlHistoryClear_Object=MibTableColumn
cie1000SyslogControlHistoryClear=_Cie1000SyslogControlHistoryClear_Object((1,3,6,1,4,1,9,9,832,1,37,1,4,1,1,3),_Cie1000SyslogControlHistoryClear_Type())
cie1000SyslogControlHistoryClear.setMaxAccess(_D)
if mibBuilder.loadTexts:cie1000SyslogControlHistoryClear.setStatus(_A)
_Cie1000SyslogMibConformance_ObjectIdentity=ObjectIdentity
cie1000SyslogMibConformance=_Cie1000SyslogMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,37,2))
_Cie1000SyslogMibCompliances_ObjectIdentity=ObjectIdentity
cie1000SyslogMibCompliances=_Cie1000SyslogMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,37,2,1))
_Cie1000SyslogMibGroups_ObjectIdentity=ObjectIdentity
cie1000SyslogMibGroups=_Cie1000SyslogMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,37,2,2))
cie1000SyslogConfigServerInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,832,1,37,2,2,1))
cie1000SyslogConfigServerInfoGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:cie1000SyslogConfigServerInfoGroup.setStatus(_A)
cie1000SyslogStatusHistoryTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,832,1,37,2,2,2))
cie1000SyslogStatusHistoryTableInfoGroup.setObjects(*((_B,_F),(_B,_G),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:cie1000SyslogStatusHistoryTableInfoGroup.setStatus(_A)
cie1000SyslogControlHistoryTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,832,1,37,2,2,3))
cie1000SyslogControlHistoryTableInfoGroup.setObjects(*((_B,_I),(_B,_J),(_B,_R)))
if mibBuilder.loadTexts:cie1000SyslogControlHistoryTableInfoGroup.setStatus(_A)
cie1000SyslogMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,832,1,37,2,1,1))
cie1000SyslogMibCompliance.setObjects(*((_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:cie1000SyslogMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CIE1000SyslogLevelType':CIE1000SyslogLevelType,'cie1000SyslogMib':cie1000SyslogMib,'cie1000SyslogMibObjects':cie1000SyslogMibObjects,'cie1000SyslogConfig':cie1000SyslogConfig,'cie1000SyslogConfigServer':cie1000SyslogConfigServer,_L:cie1000SyslogConfigServerMode,_M:cie1000SyslogConfigServerAddress,_N:cie1000SyslogConfigServerLevel,'cie1000SyslogStatus':cie1000SyslogStatus,'cie1000SyslogStatusHistoryTable':cie1000SyslogStatusHistoryTable,'cie1000SyslogStatusHistoryEntry':cie1000SyslogStatusHistoryEntry,_F:cie1000SyslogStatusHistorySwitchId,_G:cie1000SyslogStatusHistoryMsgId,_O:cie1000SyslogStatusHistoryMsgLevel,_P:cie1000SyslogStatusHistoryMsgTimeStamp,_Q:cie1000SyslogStatusHistoryMsgText,'cie1000SyslogControl':cie1000SyslogControl,'cie1000SyslogControlHistoryTable':cie1000SyslogControlHistoryTable,'cie1000SyslogControlHistoryEntry':cie1000SyslogControlHistoryEntry,_I:cie1000SyslogControlHistorySwitchId,_J:cie1000SyslogControlHistoryClearLevel,_R:cie1000SyslogControlHistoryClear,'cie1000SyslogMibConformance':cie1000SyslogMibConformance,'cie1000SyslogMibCompliances':cie1000SyslogMibCompliances,'cie1000SyslogMibCompliance':cie1000SyslogMibCompliance,'cie1000SyslogMibGroups':cie1000SyslogMibGroups,_S:cie1000SyslogConfigServerInfoGroup,_T:cie1000SyslogStatusHistoryTableInfoGroup,_U:cie1000SyslogControlHistoryTableInfoGroup})