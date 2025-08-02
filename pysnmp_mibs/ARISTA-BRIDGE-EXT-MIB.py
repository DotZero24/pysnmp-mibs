_S='aristaBridgeExtNotificationGroup'
_R='aristaBridgeExtBaseGroup'
_Q='aristaMacAge'
_P='aristaMacLearn'
_O='aristaMacMove'
_N='aristaMacStatsEntries'
_M='aristaDot1qTpFdbLastMove'
_L='aristaMacStatsEntryType'
_K='not-accessible'
_J='aristaDot1qTpFdbTimeMark'
_I='Integer32'
_H='dot1qTpFdbAddress'
_G='aristaDot1qTpFdbNumMoves'
_F='read-only'
_E='dot1qFdbId'
_D='dot1qTpFdbPort'
_C='Q-BRIDGE-MIB'
_B='ARISTA-BRIDGE-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
dot1qFdbId,dot1qTpFdbAddress,dot1qTpFdbPort=mibBuilder.importSymbols(_C,_E,_H,_D)
TimeFilter,=mibBuilder.importSymbols('RMON2-MIB','TimeFilter')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
aristaBridgeExtMIB=ModuleIdentity((1,3,6,1,4,1,30065,3,2))
if mibBuilder.loadTexts:aristaBridgeExtMIB.setRevisions(('2020-09-29 00:00','2019-09-15 00:00','2014-08-15 00:00','2011-03-31 13:00','2010-05-03 00:00'))
_AristaBridgeExtNotifications_ObjectIdentity=ObjectIdentity
aristaBridgeExtNotifications=_AristaBridgeExtNotifications_ObjectIdentity((1,3,6,1,4,1,30065,3,2,0))
_AristaDot1qTpFdbTable_Object=MibTable
aristaDot1qTpFdbTable=_AristaDot1qTpFdbTable_Object((1,3,6,1,4,1,30065,3,2,1))
if mibBuilder.loadTexts:aristaDot1qTpFdbTable.setStatus(_A)
_AristaDot1qTpFdbEntry_Object=MibTableRow
aristaDot1qTpFdbEntry=_AristaDot1qTpFdbEntry_Object((1,3,6,1,4,1,30065,3,2,1,1))
aristaDot1qTpFdbEntry.setIndexNames((0,_B,_J),(0,_C,_E),(0,_C,_H))
if mibBuilder.loadTexts:aristaDot1qTpFdbEntry.setStatus(_A)
_AristaDot1qTpFdbTimeMark_Type=TimeFilter
_AristaDot1qTpFdbTimeMark_Object=MibTableColumn
aristaDot1qTpFdbTimeMark=_AristaDot1qTpFdbTimeMark_Object((1,3,6,1,4,1,30065,3,2,1,1,1),_AristaDot1qTpFdbTimeMark_Type())
aristaDot1qTpFdbTimeMark.setMaxAccess(_K)
if mibBuilder.loadTexts:aristaDot1qTpFdbTimeMark.setStatus(_A)
_AristaDot1qTpFdbNumMoves_Type=Counter32
_AristaDot1qTpFdbNumMoves_Object=MibTableColumn
aristaDot1qTpFdbNumMoves=_AristaDot1qTpFdbNumMoves_Object((1,3,6,1,4,1,30065,3,2,1,1,2),_AristaDot1qTpFdbNumMoves_Type())
aristaDot1qTpFdbNumMoves.setMaxAccess(_F)
if mibBuilder.loadTexts:aristaDot1qTpFdbNumMoves.setStatus(_A)
_AristaDot1qTpFdbLastMove_Type=TimeTicks
_AristaDot1qTpFdbLastMove_Object=MibTableColumn
aristaDot1qTpFdbLastMove=_AristaDot1qTpFdbLastMove_Object((1,3,6,1,4,1,30065,3,2,1,1,3),_AristaDot1qTpFdbLastMove_Type())
aristaDot1qTpFdbLastMove.setMaxAccess(_F)
if mibBuilder.loadTexts:aristaDot1qTpFdbLastMove.setStatus(_A)
_AristaBridgeExtConformance_ObjectIdentity=ObjectIdentity
aristaBridgeExtConformance=_AristaBridgeExtConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,2,2))
_AristaBridgeExtGroups_ObjectIdentity=ObjectIdentity
aristaBridgeExtGroups=_AristaBridgeExtGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,2,2,1))
_AristaBridgeExtCompliances_ObjectIdentity=ObjectIdentity
aristaBridgeExtCompliances=_AristaBridgeExtCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,2,2,2))
_AristaMacStatsTable_Object=MibTable
aristaMacStatsTable=_AristaMacStatsTable_Object((1,3,6,1,4,1,30065,3,2,3))
if mibBuilder.loadTexts:aristaMacStatsTable.setStatus(_A)
_AristaMacStatsEntry_Object=MibTableRow
aristaMacStatsEntry=_AristaMacStatsEntry_Object((1,3,6,1,4,1,30065,3,2,3,1))
aristaMacStatsEntry.setIndexNames((0,_C,_E),(0,_B,_L))
if mibBuilder.loadTexts:aristaMacStatsEntry.setStatus(_A)
class _AristaMacStatsEntryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
_AristaMacStatsEntryType_Type.__name__=_I
_AristaMacStatsEntryType_Object=MibTableColumn
aristaMacStatsEntryType=_AristaMacStatsEntryType_Object((1,3,6,1,4,1,30065,3,2,3,1,1),_AristaMacStatsEntryType_Type())
aristaMacStatsEntryType.setMaxAccess(_K)
if mibBuilder.loadTexts:aristaMacStatsEntryType.setStatus(_A)
_AristaMacStatsEntries_Type=Counter32
_AristaMacStatsEntries_Object=MibTableColumn
aristaMacStatsEntries=_AristaMacStatsEntries_Object((1,3,6,1,4,1,30065,3,2,3,1,2),_AristaMacStatsEntries_Type())
aristaMacStatsEntries.setMaxAccess(_F)
if mibBuilder.loadTexts:aristaMacStatsEntries.setStatus(_A)
aristaBridgeExtBaseGroup=ObjectGroup((1,3,6,1,4,1,30065,3,2,2,1,1))
aristaBridgeExtBaseGroup.setObjects(*((_B,_G),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:aristaBridgeExtBaseGroup.setStatus(_A)
aristaMacMove=NotificationType((1,3,6,1,4,1,30065,3,2,0,1))
aristaMacMove.setObjects(*((_B,_G),(_C,_D)))
if mibBuilder.loadTexts:aristaMacMove.setStatus(_A)
aristaMacLearn=NotificationType((1,3,6,1,4,1,30065,3,2,0,2))
aristaMacLearn.setObjects((_C,_D))
if mibBuilder.loadTexts:aristaMacLearn.setStatus(_A)
aristaMacAge=NotificationType((1,3,6,1,4,1,30065,3,2,0,3))
aristaMacAge.setObjects((_C,_D))
if mibBuilder.loadTexts:aristaMacAge.setStatus(_A)
aristaBridgeExtNotificationGroup=NotificationGroup((1,3,6,1,4,1,30065,3,2,2,1,2))
aristaBridgeExtNotificationGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:aristaBridgeExtNotificationGroup.setStatus(_A)
aristaBridgeExtCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,2,2,2,1))
aristaBridgeExtCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:aristaBridgeExtCompliance.setStatus(_A)
aristaBridgeExtNotificationCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,2,2,2,2))
aristaBridgeExtNotificationCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:aristaBridgeExtNotificationCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'aristaBridgeExtMIB':aristaBridgeExtMIB,'aristaBridgeExtNotifications':aristaBridgeExtNotifications,_O:aristaMacMove,_P:aristaMacLearn,_Q:aristaMacAge,'aristaDot1qTpFdbTable':aristaDot1qTpFdbTable,'aristaDot1qTpFdbEntry':aristaDot1qTpFdbEntry,_J:aristaDot1qTpFdbTimeMark,_G:aristaDot1qTpFdbNumMoves,_M:aristaDot1qTpFdbLastMove,'aristaBridgeExtConformance':aristaBridgeExtConformance,'aristaBridgeExtGroups':aristaBridgeExtGroups,_R:aristaBridgeExtBaseGroup,_S:aristaBridgeExtNotificationGroup,'aristaBridgeExtCompliances':aristaBridgeExtCompliances,'aristaBridgeExtCompliance':aristaBridgeExtCompliance,'aristaBridgeExtNotificationCompliance':aristaBridgeExtNotificationCompliance,'aristaMacStatsTable':aristaMacStatsTable,'aristaMacStatsEntry':aristaMacStatsEntry,_L:aristaMacStatsEntryType,_N:aristaMacStatsEntries})