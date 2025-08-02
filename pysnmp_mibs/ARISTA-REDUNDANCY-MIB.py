_N='aristaRedundancyNotificationsGroup'
_M='aristaRedundancyStatusGroup'
_L='aristaRedundancySwitchOverNotif'
_K='aristaRedundancyUnitState'
_J='aristaRedundancyProtocolOper'
_I='aristaRedundancyProtocolConfig'
_H='aristaRedundancyUnitId'
_G='unknown'
_F='OctetString'
_E='aristaRedundancyLastSwOverReason'
_D='aristaRedundancyUnitStateEntryTime'
_C='read-only'
_B='ARISTA-REDUNDANCY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
aristaRedundancyMIB=ModuleIdentity((1,3,6,1,4,1,30065,3,8))
if mibBuilder.loadTexts:aristaRedundancyMIB.setRevisions(('2014-08-15 00:00','2012-11-10 22:37'))
class AristaRedundancyState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),('standby',1),('active',2),('disabled',3)))
class AristaRedundancyProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),('simplex',1),('rpr',2),('sso',3)))
_AristaRedundancyObjects_ObjectIdentity=ObjectIdentity
aristaRedundancyObjects=_AristaRedundancyObjects_ObjectIdentity((1,3,6,1,4,1,30065,3,8,0))
_AristaRedundancyStatus_ObjectIdentity=ObjectIdentity
aristaRedundancyStatus=_AristaRedundancyStatus_ObjectIdentity((1,3,6,1,4,1,30065,3,8,0,0))
_AristaRedundancyProtocolConfig_Type=AristaRedundancyProtocol
_AristaRedundancyProtocolConfig_Object=MibScalar
aristaRedundancyProtocolConfig=_AristaRedundancyProtocolConfig_Object((1,3,6,1,4,1,30065,3,8,0,0,1),_AristaRedundancyProtocolConfig_Type())
aristaRedundancyProtocolConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaRedundancyProtocolConfig.setStatus(_A)
_AristaRedundancyProtocolOper_Type=AristaRedundancyProtocol
_AristaRedundancyProtocolOper_Object=MibScalar
aristaRedundancyProtocolOper=_AristaRedundancyProtocolOper_Object((1,3,6,1,4,1,30065,3,8,0,0,2),_AristaRedundancyProtocolOper_Type())
aristaRedundancyProtocolOper.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaRedundancyProtocolOper.setStatus(_A)
_AristaRedundancyUnitStateTable_Object=MibTable
aristaRedundancyUnitStateTable=_AristaRedundancyUnitStateTable_Object((1,3,6,1,4,1,30065,3,8,0,0,3))
if mibBuilder.loadTexts:aristaRedundancyUnitStateTable.setStatus(_A)
_AristaRedundancyUnitStateEntry_Object=MibTableRow
aristaRedundancyUnitStateEntry=_AristaRedundancyUnitStateEntry_Object((1,3,6,1,4,1,30065,3,8,0,0,3,1))
aristaRedundancyUnitStateEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:aristaRedundancyUnitStateEntry.setStatus(_A)
_AristaRedundancyUnitId_Type=Unsigned32
_AristaRedundancyUnitId_Object=MibTableColumn
aristaRedundancyUnitId=_AristaRedundancyUnitId_Object((1,3,6,1,4,1,30065,3,8,0,0,3,1,1),_AristaRedundancyUnitId_Type())
aristaRedundancyUnitId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:aristaRedundancyUnitId.setStatus(_A)
_AristaRedundancyUnitState_Type=AristaRedundancyState
_AristaRedundancyUnitState_Object=MibTableColumn
aristaRedundancyUnitState=_AristaRedundancyUnitState_Object((1,3,6,1,4,1,30065,3,8,0,0,3,1,2),_AristaRedundancyUnitState_Type())
aristaRedundancyUnitState.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaRedundancyUnitState.setStatus(_A)
_AristaRedundancyUnitStateEntryTime_Type=TimeStamp
_AristaRedundancyUnitStateEntryTime_Object=MibTableColumn
aristaRedundancyUnitStateEntryTime=_AristaRedundancyUnitStateEntryTime_Object((1,3,6,1,4,1,30065,3,8,0,0,3,1,3),_AristaRedundancyUnitStateEntryTime_Type())
aristaRedundancyUnitStateEntryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaRedundancyUnitStateEntryTime.setStatus(_A)
class _AristaRedundancyLastSwOverReason_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AristaRedundancyLastSwOverReason_Type.__name__=_F
_AristaRedundancyLastSwOverReason_Object=MibScalar
aristaRedundancyLastSwOverReason=_AristaRedundancyLastSwOverReason_Object((1,3,6,1,4,1,30065,3,8,0,0,4),_AristaRedundancyLastSwOverReason_Type())
aristaRedundancyLastSwOverReason.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaRedundancyLastSwOverReason.setStatus(_A)
_AristaRedundancyHistory_ObjectIdentity=ObjectIdentity
aristaRedundancyHistory=_AristaRedundancyHistory_ObjectIdentity((1,3,6,1,4,1,30065,3,8,0,1))
_AristaRedundancyNotifications_ObjectIdentity=ObjectIdentity
aristaRedundancyNotifications=_AristaRedundancyNotifications_ObjectIdentity((1,3,6,1,4,1,30065,3,8,1))
_AristaRedundancyNotificationPrefix_ObjectIdentity=ObjectIdentity
aristaRedundancyNotificationPrefix=_AristaRedundancyNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,30065,3,8,1,0))
_AristaRedundancyConformance_ObjectIdentity=ObjectIdentity
aristaRedundancyConformance=_AristaRedundancyConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,8,2))
_AristaRedundancyCompliances_ObjectIdentity=ObjectIdentity
aristaRedundancyCompliances=_AristaRedundancyCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,8,2,1))
_AristaRedundancyGroups_ObjectIdentity=ObjectIdentity
aristaRedundancyGroups=_AristaRedundancyGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,8,2,2))
aristaRedundancyStatusGroup=ObjectGroup((1,3,6,1,4,1,30065,3,8,2,2,1))
aristaRedundancyStatusGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_D),(_B,_E)))
if mibBuilder.loadTexts:aristaRedundancyStatusGroup.setStatus(_A)
aristaRedundancySwitchOverNotif=NotificationType((1,3,6,1,4,1,30065,3,8,1,0,1))
aristaRedundancySwitchOverNotif.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:aristaRedundancySwitchOverNotif.setStatus(_A)
aristaRedundancyNotificationsGroup=NotificationGroup((1,3,6,1,4,1,30065,3,8,2,2,2))
aristaRedundancyNotificationsGroup.setObjects((_B,_L))
if mibBuilder.loadTexts:aristaRedundancyNotificationsGroup.setStatus(_A)
aristaRedundancyCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,8,2,1,1))
aristaRedundancyCompliance.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:aristaRedundancyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AristaRedundancyState':AristaRedundancyState,'AristaRedundancyProtocol':AristaRedundancyProtocol,'aristaRedundancyMIB':aristaRedundancyMIB,'aristaRedundancyObjects':aristaRedundancyObjects,'aristaRedundancyStatus':aristaRedundancyStatus,_I:aristaRedundancyProtocolConfig,_J:aristaRedundancyProtocolOper,'aristaRedundancyUnitStateTable':aristaRedundancyUnitStateTable,'aristaRedundancyUnitStateEntry':aristaRedundancyUnitStateEntry,_H:aristaRedundancyUnitId,_K:aristaRedundancyUnitState,_D:aristaRedundancyUnitStateEntryTime,_E:aristaRedundancyLastSwOverReason,'aristaRedundancyHistory':aristaRedundancyHistory,'aristaRedundancyNotifications':aristaRedundancyNotifications,'aristaRedundancyNotificationPrefix':aristaRedundancyNotificationPrefix,_L:aristaRedundancySwitchOverNotif,'aristaRedundancyConformance':aristaRedundancyConformance,'aristaRedundancyCompliances':aristaRedundancyCompliances,'aristaRedundancyCompliance':aristaRedundancyCompliance,'aristaRedundancyGroups':aristaRedundancyGroups,_M:aristaRedundancyStatusGroup,_N:aristaRedundancyNotificationsGroup})