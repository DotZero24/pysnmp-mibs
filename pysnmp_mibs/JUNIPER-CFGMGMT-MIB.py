_O='jnxCmRescueChgState'
_N='jnxCmRescueChgUser'
_M='jnxCmRescueChgSource'
_L='jnxCmRescueChgDate'
_K='jnxCmRescueChgTime'
_J='jnxCmCfgChgEventLog'
_I='jnxCmCfgChgEventUser'
_H='jnxCmCfgChgEventSource'
_G='jnxCmCfgChgEventDate'
_F='jnxCmCfgChgEventTime'
_E='jnxCmCfgChgEventIndex'
_D='Integer32'
_C='JUNIPER-CFGMGMT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
jnxCmNotifications,jnxMibs=mibBuilder.importSymbols('JUNIPER-SMI','jnxCmNotifications','jnxMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
jnxCfgMgmt=ModuleIdentity((1,3,6,1,4,1,2636,3,18))
if mibBuilder.loadTexts:jnxCfgMgmt.setRevisions(('2003-11-19 00:00','2003-10-24 00:00','2002-05-10 00:00'))
class JnxCmCfChgSource(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('other',1),('cli',2),('junoscript',3),('synchronize',4),('snmp',5),('button',6),('autoinstall',7),('unknown',8)))
class JnxCmRescueCfgState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonexistant',1),('updated',2)))
_JnxCmCfgChg_ObjectIdentity=ObjectIdentity
jnxCmCfgChg=_JnxCmCfgChg_ObjectIdentity((1,3,6,1,4,1,2636,3,18,1))
class _JnxCmCfgChgLatestIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_JnxCmCfgChgLatestIndex_Type.__name__=_D
_JnxCmCfgChgLatestIndex_Object=MibScalar
jnxCmCfgChgLatestIndex=_JnxCmCfgChgLatestIndex_Object((1,3,6,1,4,1,2636,3,18,1,1),_JnxCmCfgChgLatestIndex_Type())
jnxCmCfgChgLatestIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxCmCfgChgLatestIndex.setStatus(_A)
_JnxCmCfgChgLatestTime_Type=TimeTicks
_JnxCmCfgChgLatestTime_Object=MibScalar
jnxCmCfgChgLatestTime=_JnxCmCfgChgLatestTime_Object((1,3,6,1,4,1,2636,3,18,1,2),_JnxCmCfgChgLatestTime_Type())
jnxCmCfgChgLatestTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxCmCfgChgLatestTime.setStatus(_A)
_JnxCmCfgChgLatestDate_Type=DateAndTime
_JnxCmCfgChgLatestDate_Object=MibScalar
jnxCmCfgChgLatestDate=_JnxCmCfgChgLatestDate_Object((1,3,6,1,4,1,2636,3,18,1,3),_JnxCmCfgChgLatestDate_Type())
jnxCmCfgChgLatestDate.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxCmCfgChgLatestDate.setStatus(_A)
_JnxCmCfgChgLatestSource_Type=JnxCmCfChgSource
_JnxCmCfgChgLatestSource_Object=MibScalar
jnxCmCfgChgLatestSource=_JnxCmCfgChgLatestSource_Object((1,3,6,1,4,1,2636,3,18,1,4),_JnxCmCfgChgLatestSource_Type())
jnxCmCfgChgLatestSource.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxCmCfgChgLatestSource.setStatus(_A)
_JnxCmCfgChgLatestUser_Type=DisplayString
_JnxCmCfgChgLatestUser_Object=MibScalar
jnxCmCfgChgLatestUser=_JnxCmCfgChgLatestUser_Object((1,3,6,1,4,1,2636,3,18,1,5),_JnxCmCfgChgLatestUser_Type())
jnxCmCfgChgLatestUser.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxCmCfgChgLatestUser.setStatus(_A)
class _JnxCmCfgChgMaxEventEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JnxCmCfgChgMaxEventEntries_Type.__name__=_D
_JnxCmCfgChgMaxEventEntries_Object=MibScalar
jnxCmCfgChgMaxEventEntries=_JnxCmCfgChgMaxEventEntries_Object((1,3,6,1,4,1,2636,3,18,1,6),_JnxCmCfgChgMaxEventEntries_Type())
jnxCmCfgChgMaxEventEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxCmCfgChgMaxEventEntries.setStatus(_A)
_JnxCmCfgChgEventTable_Object=MibTable
jnxCmCfgChgEventTable=_JnxCmCfgChgEventTable_Object((1,3,6,1,4,1,2636,3,18,1,7))
if mibBuilder.loadTexts:jnxCmCfgChgEventTable.setStatus(_A)
_JnxCmCfgChgEventEntry_Object=MibTableRow
jnxCmCfgChgEventEntry=_JnxCmCfgChgEventEntry_Object((1,3,6,1,4,1,2636,3,18,1,7,1))
jnxCmCfgChgEventEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:jnxCmCfgChgEventEntry.setStatus(_A)
class _JnxCmCfgChgEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_JnxCmCfgChgEventIndex_Type.__name__=_D
_JnxCmCfgChgEventIndex_Object=MibTableColumn
jnxCmCfgChgEventIndex=_JnxCmCfgChgEventIndex_Object((1,3,6,1,4,1,2636,3,18,1,7,1,1),_JnxCmCfgChgEventIndex_Type())
jnxCmCfgChgEventIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:jnxCmCfgChgEventIndex.setStatus(_A)
_JnxCmCfgChgEventTime_Type=TimeTicks
_JnxCmCfgChgEventTime_Object=MibTableColumn
jnxCmCfgChgEventTime=_JnxCmCfgChgEventTime_Object((1,3,6,1,4,1,2636,3,18,1,7,1,2),_JnxCmCfgChgEventTime_Type())
jnxCmCfgChgEventTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxCmCfgChgEventTime.setStatus(_A)
_JnxCmCfgChgEventDate_Type=DateAndTime
_JnxCmCfgChgEventDate_Object=MibTableColumn
jnxCmCfgChgEventDate=_JnxCmCfgChgEventDate_Object((1,3,6,1,4,1,2636,3,18,1,7,1,3),_JnxCmCfgChgEventDate_Type())
jnxCmCfgChgEventDate.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxCmCfgChgEventDate.setStatus(_A)
_JnxCmCfgChgEventSource_Type=JnxCmCfChgSource
_JnxCmCfgChgEventSource_Object=MibTableColumn
jnxCmCfgChgEventSource=_JnxCmCfgChgEventSource_Object((1,3,6,1,4,1,2636,3,18,1,7,1,4),_JnxCmCfgChgEventSource_Type())
jnxCmCfgChgEventSource.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxCmCfgChgEventSource.setStatus(_A)
_JnxCmCfgChgEventUser_Type=DisplayString
_JnxCmCfgChgEventUser_Object=MibTableColumn
jnxCmCfgChgEventUser=_JnxCmCfgChgEventUser_Object((1,3,6,1,4,1,2636,3,18,1,7,1,5),_JnxCmCfgChgEventUser_Type())
jnxCmCfgChgEventUser.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxCmCfgChgEventUser.setStatus(_A)
_JnxCmCfgChgEventLog_Type=DisplayString
_JnxCmCfgChgEventLog_Object=MibTableColumn
jnxCmCfgChgEventLog=_JnxCmCfgChgEventLog_Object((1,3,6,1,4,1,2636,3,18,1,7,1,6),_JnxCmCfgChgEventLog_Type())
jnxCmCfgChgEventLog.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxCmCfgChgEventLog.setStatus(_A)
_JnxCmRescueChg_ObjectIdentity=ObjectIdentity
jnxCmRescueChg=_JnxCmRescueChg_ObjectIdentity((1,3,6,1,4,1,2636,3,18,2))
_JnxCmRescueChgTime_Type=TimeTicks
_JnxCmRescueChgTime_Object=MibScalar
jnxCmRescueChgTime=_JnxCmRescueChgTime_Object((1,3,6,1,4,1,2636,3,18,2,1),_JnxCmRescueChgTime_Type())
jnxCmRescueChgTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxCmRescueChgTime.setStatus(_A)
_JnxCmRescueChgDate_Type=DateAndTime
_JnxCmRescueChgDate_Object=MibScalar
jnxCmRescueChgDate=_JnxCmRescueChgDate_Object((1,3,6,1,4,1,2636,3,18,2,2),_JnxCmRescueChgDate_Type())
jnxCmRescueChgDate.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxCmRescueChgDate.setStatus(_A)
_JnxCmRescueChgSource_Type=JnxCmCfChgSource
_JnxCmRescueChgSource_Object=MibScalar
jnxCmRescueChgSource=_JnxCmRescueChgSource_Object((1,3,6,1,4,1,2636,3,18,2,3),_JnxCmRescueChgSource_Type())
jnxCmRescueChgSource.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxCmRescueChgSource.setStatus(_A)
_JnxCmRescueChgUser_Type=DisplayString
_JnxCmRescueChgUser_Object=MibScalar
jnxCmRescueChgUser=_JnxCmRescueChgUser_Object((1,3,6,1,4,1,2636,3,18,2,4),_JnxCmRescueChgUser_Type())
jnxCmRescueChgUser.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxCmRescueChgUser.setStatus(_A)
_JnxCmRescueChgState_Type=JnxCmRescueCfgState
_JnxCmRescueChgState_Object=MibScalar
jnxCmRescueChgState=_JnxCmRescueChgState_Object((1,3,6,1,4,1,2636,3,18,2,5),_JnxCmRescueChgState_Type())
jnxCmRescueChgState.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxCmRescueChgState.setStatus(_A)
_JnxCmNotificationsPrefix_ObjectIdentity=ObjectIdentity
jnxCmNotificationsPrefix=_JnxCmNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,2636,4,5,0))
jnxCmCfgChange=NotificationType((1,3,6,1,4,1,2636,4,5,0,1))
jnxCmCfgChange.setObjects(*((_C,_F),(_C,_G),(_C,_H),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:jnxCmCfgChange.setStatus(_A)
jnxCmRescueChange=NotificationType((1,3,6,1,4,1,2636,4,5,0,2))
jnxCmRescueChange.setObjects(*((_C,_K),(_C,_L),(_C,_M),(_C,_N),(_C,_O)))
if mibBuilder.loadTexts:jnxCmRescueChange.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'JnxCmCfChgSource':JnxCmCfChgSource,'JnxCmRescueCfgState':JnxCmRescueCfgState,'jnxCfgMgmt':jnxCfgMgmt,'jnxCmCfgChg':jnxCmCfgChg,'jnxCmCfgChgLatestIndex':jnxCmCfgChgLatestIndex,'jnxCmCfgChgLatestTime':jnxCmCfgChgLatestTime,'jnxCmCfgChgLatestDate':jnxCmCfgChgLatestDate,'jnxCmCfgChgLatestSource':jnxCmCfgChgLatestSource,'jnxCmCfgChgLatestUser':jnxCmCfgChgLatestUser,'jnxCmCfgChgMaxEventEntries':jnxCmCfgChgMaxEventEntries,'jnxCmCfgChgEventTable':jnxCmCfgChgEventTable,'jnxCmCfgChgEventEntry':jnxCmCfgChgEventEntry,_E:jnxCmCfgChgEventIndex,_F:jnxCmCfgChgEventTime,_G:jnxCmCfgChgEventDate,_H:jnxCmCfgChgEventSource,_I:jnxCmCfgChgEventUser,_J:jnxCmCfgChgEventLog,'jnxCmRescueChg':jnxCmRescueChg,_K:jnxCmRescueChgTime,_L:jnxCmRescueChgDate,_M:jnxCmRescueChgSource,_N:jnxCmRescueChgUser,_O:jnxCmRescueChgState,'jnxCmNotificationsPrefix':jnxCmNotificationsPrefix,'jnxCmCfgChange':jnxCmCfgChange,'jnxCmRescueChange':jnxCmRescueChange})