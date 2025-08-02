_N='clabAniDevGroup'
_M='aniDevSysLoggingEventMessage'
_L='aniDevSysLoggingEventTimeStamp'
_K='aniDevSysLoggingGroupCtrl'
_J='aniDevSysLoggingLevelCtrl'
_I='aniDevSysLoggingSize'
_H='aniDevLoggingCtrlReset'
_G='aniDevResetNow'
_F='read-only'
_E='aniDevSysLoggingEventIndex'
_D='Integer32'
_C='read-write'
_B='CLAB-ANI-DEV-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
clabCommonMibs,=mibBuilder.importSymbols('CLAB-DEF-MIB','clabCommonMibs')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
clabAniDevMib=ModuleIdentity((1,3,6,1,4,1,4491,4,7))
if mibBuilder.loadTexts:clabAniDevMib.setRevisions(('2017-04-27 00:00','2017-02-21 00:00','2016-05-19 00:00','2016-03-17 00:00'))
_ClabAniDevObjects_ObjectIdentity=ObjectIdentity
clabAniDevObjects=_ClabAniDevObjects_ObjectIdentity((1,3,6,1,4,1,4491,4,7,1))
_AniDevResetNow_Type=TruthValue
_AniDevResetNow_Object=MibScalar
aniDevResetNow=_AniDevResetNow_Object((1,3,6,1,4,1,4491,4,7,1,1),_AniDevResetNow_Type())
aniDevResetNow.setMaxAccess(_C)
if mibBuilder.loadTexts:aniDevResetNow.setStatus(_A)
_ClabAniDevSysLoggingObjects_ObjectIdentity=ObjectIdentity
clabAniDevSysLoggingObjects=_ClabAniDevSysLoggingObjects_ObjectIdentity((1,3,6,1,4,1,4491,4,7,1,2))
class _AniDevLoggingCtrlReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('resetLog',1),('pauseLog',2),('startLog',3),('useDefaultReporting',4)))
_AniDevLoggingCtrlReset_Type.__name__=_D
_AniDevLoggingCtrlReset_Object=MibScalar
aniDevLoggingCtrlReset=_AniDevLoggingCtrlReset_Object((1,3,6,1,4,1,4491,4,7,1,2,1),_AniDevLoggingCtrlReset_Type())
aniDevLoggingCtrlReset.setMaxAccess(_C)
if mibBuilder.loadTexts:aniDevLoggingCtrlReset.setStatus(_A)
_AniDevSysLoggingSize_Type=Unsigned32
_AniDevSysLoggingSize_Object=MibScalar
aniDevSysLoggingSize=_AniDevSysLoggingSize_Object((1,3,6,1,4,1,4491,4,7,1,2,2),_AniDevSysLoggingSize_Type())
aniDevSysLoggingSize.setMaxAccess(_C)
if mibBuilder.loadTexts:aniDevSysLoggingSize.setStatus(_A)
if mibBuilder.loadTexts:aniDevSysLoggingSize.setUnits('bytes')
class _AniDevSysLoggingLevelCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('all',1),('trace',2),('debug',3),('info',4),('warn',5),('error',6),('fatal',7),('off',8)))
_AniDevSysLoggingLevelCtrl_Type.__name__=_D
_AniDevSysLoggingLevelCtrl_Object=MibScalar
aniDevSysLoggingLevelCtrl=_AniDevSysLoggingLevelCtrl_Object((1,3,6,1,4,1,4491,4,7,1,2,3),_AniDevSysLoggingLevelCtrl_Type())
aniDevSysLoggingLevelCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:aniDevSysLoggingLevelCtrl.setStatus(_A)
class _AniDevSysLoggingGroupCtrl_Type(Bits):defaultBinValue='1';namedValues=NamedValues(*(('none',0),('all',1),('group1',2),('group2',3),('group3',4),('group4',5),('group5',6)))
_AniDevSysLoggingGroupCtrl_Type.__name__='Bits'
_AniDevSysLoggingGroupCtrl_Object=MibScalar
aniDevSysLoggingGroupCtrl=_AniDevSysLoggingGroupCtrl_Object((1,3,6,1,4,1,4491,4,7,1,2,4),_AniDevSysLoggingGroupCtrl_Type())
aniDevSysLoggingGroupCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:aniDevSysLoggingGroupCtrl.setStatus(_A)
_AniDevSysLoggingEventTable_Object=MibTable
aniDevSysLoggingEventTable=_AniDevSysLoggingEventTable_Object((1,3,6,1,4,1,4491,4,7,1,2,5))
if mibBuilder.loadTexts:aniDevSysLoggingEventTable.setStatus(_A)
_AniDevSysLoggingEventEntry_Object=MibTableRow
aniDevSysLoggingEventEntry=_AniDevSysLoggingEventEntry_Object((1,3,6,1,4,1,4491,4,7,1,2,5,1))
aniDevSysLoggingEventEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:aniDevSysLoggingEventEntry.setStatus(_A)
_AniDevSysLoggingEventIndex_Type=Unsigned32
_AniDevSysLoggingEventIndex_Object=MibTableColumn
aniDevSysLoggingEventIndex=_AniDevSysLoggingEventIndex_Object((1,3,6,1,4,1,4491,4,7,1,2,5,1,1),_AniDevSysLoggingEventIndex_Type())
aniDevSysLoggingEventIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:aniDevSysLoggingEventIndex.setStatus(_A)
_AniDevSysLoggingEventTimeStamp_Type=DateAndTime
_AniDevSysLoggingEventTimeStamp_Object=MibTableColumn
aniDevSysLoggingEventTimeStamp=_AniDevSysLoggingEventTimeStamp_Object((1,3,6,1,4,1,4491,4,7,1,2,5,1,2),_AniDevSysLoggingEventTimeStamp_Type())
aniDevSysLoggingEventTimeStamp.setMaxAccess(_F)
if mibBuilder.loadTexts:aniDevSysLoggingEventTimeStamp.setStatus(_A)
_AniDevSysLoggingEventMessage_Type=SnmpAdminString
_AniDevSysLoggingEventMessage_Object=MibTableColumn
aniDevSysLoggingEventMessage=_AniDevSysLoggingEventMessage_Object((1,3,6,1,4,1,4491,4,7,1,2,5,1,3),_AniDevSysLoggingEventMessage_Type())
aniDevSysLoggingEventMessage.setMaxAccess(_F)
if mibBuilder.loadTexts:aniDevSysLoggingEventMessage.setStatus(_A)
_ClabAniDevConformance_ObjectIdentity=ObjectIdentity
clabAniDevConformance=_ClabAniDevConformance_ObjectIdentity((1,3,6,1,4,1,4491,4,7,2))
_ClabAniDevCompliances_ObjectIdentity=ObjectIdentity
clabAniDevCompliances=_ClabAniDevCompliances_ObjectIdentity((1,3,6,1,4,1,4491,4,7,2,1))
_ClabAniDevGroups_ObjectIdentity=ObjectIdentity
clabAniDevGroups=_ClabAniDevGroups_ObjectIdentity((1,3,6,1,4,1,4491,4,7,2,2))
clabAniDevGroup=ObjectGroup((1,3,6,1,4,1,4491,4,7,2,2,1))
clabAniDevGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:clabAniDevGroup.setStatus(_A)
clabAniDevCompliance=ModuleCompliance((1,3,6,1,4,1,4491,4,7,2,1,1))
clabAniDevCompliance.setObjects((_B,_N))
if mibBuilder.loadTexts:clabAniDevCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'clabAniDevMib':clabAniDevMib,'clabAniDevObjects':clabAniDevObjects,_G:aniDevResetNow,'clabAniDevSysLoggingObjects':clabAniDevSysLoggingObjects,_H:aniDevLoggingCtrlReset,_I:aniDevSysLoggingSize,_J:aniDevSysLoggingLevelCtrl,_K:aniDevSysLoggingGroupCtrl,'aniDevSysLoggingEventTable':aniDevSysLoggingEventTable,'aniDevSysLoggingEventEntry':aniDevSysLoggingEventEntry,_E:aniDevSysLoggingEventIndex,_L:aniDevSysLoggingEventTimeStamp,_M:aniDevSysLoggingEventMessage,'clabAniDevConformance':clabAniDevConformance,'clabAniDevCompliances':clabAniDevCompliances,'clabAniDevCompliance':clabAniDevCompliance,'clabAniDevGroups':clabAniDevGroups,_N:clabAniDevGroup})