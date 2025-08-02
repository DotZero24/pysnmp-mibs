_S='tmnxClearNotificationGroup'
_R='tmnxClearGroup'
_Q='tmnxClear'
_P='tmnxClearAction'
_O='read-write'
_N='tmnxClearIndex'
_M='TmnxActionType'
_L='tmnxEventAppIndex'
_K='TIMETRA-LOG-MIB'
_J='tmnxClearErrorText'
_I='tmnxClearResult'
_H='tmnxClearLastClearedTime'
_G='tmnxClearParams'
_F='tmnxClearName'
_E='Integer32'
_D='OctetString'
_C='read-only'
_B='current'
_A='TIMETRA-CLEAR-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
tmnxEventAppIndex,=mibBuilder.importSymbols(_K,_L)
TNamedItem,TmnxActionType=mibBuilder.importSymbols('TIMETRA-TC-MIB','TNamedItem',_M)
timetraClearMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,13))
if mibBuilder.loadTexts:timetraClearMIBModule.setRevisions(('2005-01-24 00:00','2004-06-02 00:00','2004-01-15 00:00','2003-08-15 00:00','2003-01-20 00:00','2002-02-27 00:00'))
_TmnxClearConformance_ObjectIdentity=ObjectIdentity
tmnxClearConformance=_TmnxClearConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,13))
_TmnxClearCompliances_ObjectIdentity=ObjectIdentity
tmnxClearCompliances=_TmnxClearCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,13,1))
_TmnxClearGroups_ObjectIdentity=ObjectIdentity
tmnxClearGroups=_TmnxClearGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,13,2))
_TmnxClearObjs_ObjectIdentity=ObjectIdentity
tmnxClearObjs=_TmnxClearObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,13))
_TmnxClearTable_Object=MibTable
tmnxClearTable=_TmnxClearTable_Object((1,3,6,1,4,1,6527,3,1,2,13,1))
if mibBuilder.loadTexts:tmnxClearTable.setStatus(_B)
_TmnxClearEntry_Object=MibTableRow
tmnxClearEntry=_TmnxClearEntry_Object((1,3,6,1,4,1,6527,3,1,2,13,1,1))
tmnxClearEntry.setIndexNames((0,_K,_L),(0,_A,_N))
if mibBuilder.loadTexts:tmnxClearEntry.setStatus(_B)
class _TmnxClearIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TmnxClearIndex_Type.__name__=_E
_TmnxClearIndex_Object=MibTableColumn
tmnxClearIndex=_TmnxClearIndex_Object((1,3,6,1,4,1,6527,3,1,2,13,1,1,1),_TmnxClearIndex_Type())
tmnxClearIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:tmnxClearIndex.setStatus(_B)
_TmnxClearName_Type=TNamedItem
_TmnxClearName_Object=MibTableColumn
tmnxClearName=_TmnxClearName_Object((1,3,6,1,4,1,6527,3,1,2,13,1,1,2),_TmnxClearName_Type())
tmnxClearName.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxClearName.setStatus(_B)
class _TmnxClearParams_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_TmnxClearParams_Type.__name__=_D
_TmnxClearParams_Object=MibTableColumn
tmnxClearParams=_TmnxClearParams_Object((1,3,6,1,4,1,6527,3,1,2,13,1,1,3),_TmnxClearParams_Type())
tmnxClearParams.setMaxAccess(_O)
if mibBuilder.loadTexts:tmnxClearParams.setStatus(_B)
class _TmnxClearAction_Type(TmnxActionType):defaultValue=2
_TmnxClearAction_Type.__name__=_M
_TmnxClearAction_Object=MibTableColumn
tmnxClearAction=_TmnxClearAction_Object((1,3,6,1,4,1,6527,3,1,2,13,1,1,4),_TmnxClearAction_Type())
tmnxClearAction.setMaxAccess(_O)
if mibBuilder.loadTexts:tmnxClearAction.setStatus(_B)
_TmnxClearLastClearedTime_Type=TimeStamp
_TmnxClearLastClearedTime_Object=MibTableColumn
tmnxClearLastClearedTime=_TmnxClearLastClearedTime_Object((1,3,6,1,4,1,6527,3,1,2,13,1,1,5),_TmnxClearLastClearedTime_Type())
tmnxClearLastClearedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxClearLastClearedTime.setStatus(_B)
class _TmnxClearResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('success',1),('failure',2)))
_TmnxClearResult_Type.__name__=_E
_TmnxClearResult_Object=MibTableColumn
tmnxClearResult=_TmnxClearResult_Object((1,3,6,1,4,1,6527,3,1,2,13,1,1,6),_TmnxClearResult_Type())
tmnxClearResult.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxClearResult.setStatus(_B)
class _TmnxClearErrorText_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TmnxClearErrorText_Type.__name__=_D
_TmnxClearErrorText_Object=MibTableColumn
tmnxClearErrorText=_TmnxClearErrorText_Object((1,3,6,1,4,1,6527,3,1,2,13,1,1,7),_TmnxClearErrorText_Type())
tmnxClearErrorText.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxClearErrorText.setStatus(_B)
_TmnxClearNotificationsPrefix_ObjectIdentity=ObjectIdentity
tmnxClearNotificationsPrefix=_TmnxClearNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,13))
_TmnxClearNotifications_ObjectIdentity=ObjectIdentity
tmnxClearNotifications=_TmnxClearNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,13,0))
tmnxClearGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,13,2,1))
tmnxClearGroup.setObjects(*((_A,_F),(_A,_G),(_A,_P),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:tmnxClearGroup.setStatus(_B)
tmnxClear=NotificationType((1,3,6,1,4,1,6527,3,1,3,13,0,1))
tmnxClear.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:tmnxClear.setStatus(_B)
tmnxClearNotificationGroup=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,13,2,2))
tmnxClearNotificationGroup.setObjects((_A,_Q))
if mibBuilder.loadTexts:tmnxClearNotificationGroup.setStatus(_B)
tmnxClearCompliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,13,1,1))
tmnxClearCompliance.setObjects(*((_A,_R),(_A,_S)))
if mibBuilder.loadTexts:tmnxClearCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'timetraClearMIBModule':timetraClearMIBModule,'tmnxClearConformance':tmnxClearConformance,'tmnxClearCompliances':tmnxClearCompliances,'tmnxClearCompliance':tmnxClearCompliance,'tmnxClearGroups':tmnxClearGroups,_R:tmnxClearGroup,_S:tmnxClearNotificationGroup,'tmnxClearObjs':tmnxClearObjs,'tmnxClearTable':tmnxClearTable,'tmnxClearEntry':tmnxClearEntry,_N:tmnxClearIndex,_F:tmnxClearName,_G:tmnxClearParams,_P:tmnxClearAction,_H:tmnxClearLastClearedTime,_I:tmnxClearResult,_J:tmnxClearErrorText,'tmnxClearNotificationsPrefix':tmnxClearNotificationsPrefix,'tmnxClearNotifications':tmnxClearNotifications,_Q:tmnxClear})