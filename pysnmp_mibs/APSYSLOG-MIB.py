_W='apSyslogMessageGenerated'
_V='apSyslogHistMsgsFlushed'
_U='apSyslogHistTableMaxLength'
_T='apSyslogMsgDrops'
_S='apSyslogMsgIgnores'
_R='apSyslogMaxLevel'
_Q='apSyslogNotificationsEnabled'
_P='apSyslogNotificationsSent'
_O='SyslogLevel'
_N='TruthValue'
_M='apSyslogHistTimestamp'
_L='apSyslogHistContent'
_K='apSyslogHistType'
_J='apSyslogHistLevel'
_I='apSyslogHistFrom'
_H='apSyslogHistIndex'
_G='messages'
_F='read-write'
_E='Integer32'
_D='DisplayString'
_C='read-only'
_B='current'
_A='APSYSLOG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acmepacketMgmt,=mibBuilder.importSymbols('ACMEPACKET-SMI','acmepacketMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TimeStamp',_N)
apSyslogModule=ModuleIdentity((1,3,6,1,4,1,9148,3,1))
if mibBuilder.loadTexts:apSyslogModule.setRevisions(('2012-07-16 00:00',))
class SyslogLevel(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('emergency',1),('critical',2),('major',3),('minor',4),('warning',5),('notice',6),('info',7),('trace',8),('debug',9),('detail',10)))
_ApSyslogMIBObjects_ObjectIdentity=ObjectIdentity
apSyslogMIBObjects=_ApSyslogMIBObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,1,1))
_ApSyslogBasic_ObjectIdentity=ObjectIdentity
apSyslogBasic=_ApSyslogBasic_ObjectIdentity((1,3,6,1,4,1,9148,3,1,1,1))
_ApSyslogNotificationsSent_Type=Counter32
_ApSyslogNotificationsSent_Object=MibScalar
apSyslogNotificationsSent=_ApSyslogNotificationsSent_Object((1,3,6,1,4,1,9148,3,1,1,1,1),_ApSyslogNotificationsSent_Type())
apSyslogNotificationsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:apSyslogNotificationsSent.setStatus(_B)
if mibBuilder.loadTexts:apSyslogNotificationsSent.setUnits('notifications')
class _ApSyslogNotificationsEnabled_Type(TruthValue):defaultValue=2
_ApSyslogNotificationsEnabled_Type.__name__=_N
_ApSyslogNotificationsEnabled_Object=MibScalar
apSyslogNotificationsEnabled=_ApSyslogNotificationsEnabled_Object((1,3,6,1,4,1,9148,3,1,1,1,2),_ApSyslogNotificationsEnabled_Type())
apSyslogNotificationsEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:apSyslogNotificationsEnabled.setStatus(_B)
class _ApSyslogMaxLevel_Type(SyslogLevel):defaultValue=5
_ApSyslogMaxLevel_Type.__name__=_O
_ApSyslogMaxLevel_Object=MibScalar
apSyslogMaxLevel=_ApSyslogMaxLevel_Object((1,3,6,1,4,1,9148,3,1,1,1,3),_ApSyslogMaxLevel_Type())
apSyslogMaxLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:apSyslogMaxLevel.setStatus(_B)
_ApSyslogMsgIgnores_Type=Counter32
_ApSyslogMsgIgnores_Object=MibScalar
apSyslogMsgIgnores=_ApSyslogMsgIgnores_Object((1,3,6,1,4,1,9148,3,1,1,1,4),_ApSyslogMsgIgnores_Type())
apSyslogMsgIgnores.setMaxAccess(_C)
if mibBuilder.loadTexts:apSyslogMsgIgnores.setStatus(_B)
if mibBuilder.loadTexts:apSyslogMsgIgnores.setUnits(_G)
_ApSyslogMsgDrops_Type=Counter32
_ApSyslogMsgDrops_Object=MibScalar
apSyslogMsgDrops=_ApSyslogMsgDrops_Object((1,3,6,1,4,1,9148,3,1,1,1,5),_ApSyslogMsgDrops_Type())
apSyslogMsgDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:apSyslogMsgDrops.setStatus(_B)
if mibBuilder.loadTexts:apSyslogMsgDrops.setUnits(_G)
_ApSyslogHistory_ObjectIdentity=ObjectIdentity
apSyslogHistory=_ApSyslogHistory_ObjectIdentity((1,3,6,1,4,1,9148,3,1,1,2))
class _ApSyslogHistTableMaxLength_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_ApSyslogHistTableMaxLength_Type.__name__=_E
_ApSyslogHistTableMaxLength_Object=MibScalar
apSyslogHistTableMaxLength=_ApSyslogHistTableMaxLength_Object((1,3,6,1,4,1,9148,3,1,1,2,1),_ApSyslogHistTableMaxLength_Type())
apSyslogHistTableMaxLength.setMaxAccess(_F)
if mibBuilder.loadTexts:apSyslogHistTableMaxLength.setStatus(_B)
if mibBuilder.loadTexts:apSyslogHistTableMaxLength.setUnits('entries')
_ApSyslogHistMsgsFlushed_Type=Counter32
_ApSyslogHistMsgsFlushed_Object=MibScalar
apSyslogHistMsgsFlushed=_ApSyslogHistMsgsFlushed_Object((1,3,6,1,4,1,9148,3,1,1,2,2),_ApSyslogHistMsgsFlushed_Type())
apSyslogHistMsgsFlushed.setMaxAccess(_C)
if mibBuilder.loadTexts:apSyslogHistMsgsFlushed.setStatus(_B)
if mibBuilder.loadTexts:apSyslogHistMsgsFlushed.setUnits(_G)
_ApSyslogHistoryTable_Object=MibTable
apSyslogHistoryTable=_ApSyslogHistoryTable_Object((1,3,6,1,4,1,9148,3,1,1,2,3))
if mibBuilder.loadTexts:apSyslogHistoryTable.setStatus(_B)
_ApSyslogHistoryEntry_Object=MibTableRow
apSyslogHistoryEntry=_ApSyslogHistoryEntry_Object((1,3,6,1,4,1,9148,3,1,1,2,3,1))
apSyslogHistoryEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:apSyslogHistoryEntry.setStatus(_B)
class _ApSyslogHistIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApSyslogHistIndex_Type.__name__=_E
_ApSyslogHistIndex_Object=MibTableColumn
apSyslogHistIndex=_ApSyslogHistIndex_Object((1,3,6,1,4,1,9148,3,1,1,2,3,1,1),_ApSyslogHistIndex_Type())
apSyslogHistIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:apSyslogHistIndex.setStatus(_B)
class _ApSyslogHistFrom_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_ApSyslogHistFrom_Type.__name__=_D
_ApSyslogHistFrom_Object=MibTableColumn
apSyslogHistFrom=_ApSyslogHistFrom_Object((1,3,6,1,4,1,9148,3,1,1,2,3,1,2),_ApSyslogHistFrom_Type())
apSyslogHistFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:apSyslogHistFrom.setStatus(_B)
_ApSyslogHistLevel_Type=SyslogLevel
_ApSyslogHistLevel_Object=MibTableColumn
apSyslogHistLevel=_ApSyslogHistLevel_Object((1,3,6,1,4,1,9148,3,1,1,2,3,1,3),_ApSyslogHistLevel_Type())
apSyslogHistLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:apSyslogHistLevel.setStatus(_B)
class _ApSyslogHistType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_ApSyslogHistType_Type.__name__=_D
_ApSyslogHistType_Object=MibTableColumn
apSyslogHistType=_ApSyslogHistType_Object((1,3,6,1,4,1,9148,3,1,1,2,3,1,4),_ApSyslogHistType_Type())
apSyslogHistType.setMaxAccess(_C)
if mibBuilder.loadTexts:apSyslogHistType.setStatus(_B)
class _ApSyslogHistContent_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_ApSyslogHistContent_Type.__name__=_D
_ApSyslogHistContent_Object=MibTableColumn
apSyslogHistContent=_ApSyslogHistContent_Object((1,3,6,1,4,1,9148,3,1,1,2,3,1,5),_ApSyslogHistContent_Type())
apSyslogHistContent.setMaxAccess(_C)
if mibBuilder.loadTexts:apSyslogHistContent.setStatus(_B)
_ApSyslogHistTimestamp_Type=TimeStamp
_ApSyslogHistTimestamp_Object=MibTableColumn
apSyslogHistTimestamp=_ApSyslogHistTimestamp_Object((1,3,6,1,4,1,9148,3,1,1,2,3,1,6),_ApSyslogHistTimestamp_Type())
apSyslogHistTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:apSyslogHistTimestamp.setStatus(_B)
_ApSyslogMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
apSyslogMIBNotificationPrefix=_ApSyslogMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9148,3,1,2))
_ApSyslogMIBNotifications_ObjectIdentity=ObjectIdentity
apSyslogMIBNotifications=_ApSyslogMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9148,3,1,2,0))
_ApSyslogMIBConformance_ObjectIdentity=ObjectIdentity
apSyslogMIBConformance=_ApSyslogMIBConformance_ObjectIdentity((1,3,6,1,4,1,9148,3,1,3))
_ApSyslogMIBCompliances_ObjectIdentity=ObjectIdentity
apSyslogMIBCompliances=_ApSyslogMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9148,3,1,3,1))
_ApSyslogMIBGroups_ObjectIdentity=ObjectIdentity
apSyslogMIBGroups=_ApSyslogMIBGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,1,3,2))
apSyslogGroup=ObjectGroup((1,3,6,1,4,1,9148,3,1,3,2,1))
apSyslogGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:apSyslogGroup.setStatus(_B)
apSyslogMessageGenerated=NotificationType((1,3,6,1,4,1,9148,3,1,2,0,1))
apSyslogMessageGenerated.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:apSyslogMessageGenerated.setStatus(_B)
apSyslogNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9148,3,1,3,2,2))
apSyslogNotificationsGroup.setObjects((_A,_W))
if mibBuilder.loadTexts:apSyslogNotificationsGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_O:SyslogLevel,'apSyslogModule':apSyslogModule,'apSyslogMIBObjects':apSyslogMIBObjects,'apSyslogBasic':apSyslogBasic,_P:apSyslogNotificationsSent,_Q:apSyslogNotificationsEnabled,_R:apSyslogMaxLevel,_S:apSyslogMsgIgnores,_T:apSyslogMsgDrops,'apSyslogHistory':apSyslogHistory,_U:apSyslogHistTableMaxLength,_V:apSyslogHistMsgsFlushed,'apSyslogHistoryTable':apSyslogHistoryTable,'apSyslogHistoryEntry':apSyslogHistoryEntry,_H:apSyslogHistIndex,_I:apSyslogHistFrom,_J:apSyslogHistLevel,_K:apSyslogHistType,_L:apSyslogHistContent,_M:apSyslogHistTimestamp,'apSyslogMIBNotificationPrefix':apSyslogMIBNotificationPrefix,'apSyslogMIBNotifications':apSyslogMIBNotifications,_W:apSyslogMessageGenerated,'apSyslogMIBConformance':apSyslogMIBConformance,'apSyslogMIBCompliances':apSyslogMIBCompliances,'apSyslogMIBGroups':apSyslogMIBGroups,'apSyslogGroup':apSyslogGroup,'apSyslogNotificationsGroup':apSyslogNotificationsGroup})