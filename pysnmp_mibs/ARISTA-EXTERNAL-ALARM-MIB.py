_P='aristaExternalAlarmNotificationsGroup'
_O='aristaExternalAlarmObjectsGroup'
_N='aristaExternalAlarmDeassertedNotif'
_M='aristaExternalAlarmAssertedNotif'
_L='aristaExternalAlarmAction'
_K='aristaExternalAlarmPolarity'
_J='aristaExternalAlarmLastDeasserted'
_I='aristaExternalAlarmLastAsserted'
_H='aristaExternalAlarmCount'
_G='aristaExternalAlarmAsserted'
_F='aristaExternalAlarmId'
_E='Integer32'
_D='aristaExternalAlarmDescription'
_C='read-only'
_B='ARISTA-EXTERNAL-ALARM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
aristaExternalAlarmMIB=ModuleIdentity((1,3,6,1,4,1,30065,3,25))
if mibBuilder.loadTexts:aristaExternalAlarmMIB.setRevisions(('2018-02-26 00:00',))
_AristaExternalAlarmMibNotifications_ObjectIdentity=ObjectIdentity
aristaExternalAlarmMibNotifications=_AristaExternalAlarmMibNotifications_ObjectIdentity((1,3,6,1,4,1,30065,3,25,0))
_AristaExternalAlarmMibObjects_ObjectIdentity=ObjectIdentity
aristaExternalAlarmMibObjects=_AristaExternalAlarmMibObjects_ObjectIdentity((1,3,6,1,4,1,30065,3,25,1))
_AristaExternalAlarmTable_Object=MibTable
aristaExternalAlarmTable=_AristaExternalAlarmTable_Object((1,3,6,1,4,1,30065,3,25,1,1))
if mibBuilder.loadTexts:aristaExternalAlarmTable.setStatus(_A)
_AristaExternalAlarmTableEntry_Object=MibTableRow
aristaExternalAlarmTableEntry=_AristaExternalAlarmTableEntry_Object((1,3,6,1,4,1,30065,3,25,1,1,1))
aristaExternalAlarmTableEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:aristaExternalAlarmTableEntry.setStatus(_A)
_AristaExternalAlarmId_Type=Unsigned32
_AristaExternalAlarmId_Object=MibTableColumn
aristaExternalAlarmId=_AristaExternalAlarmId_Object((1,3,6,1,4,1,30065,3,25,1,1,1,1),_AristaExternalAlarmId_Type())
aristaExternalAlarmId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:aristaExternalAlarmId.setStatus(_A)
_AristaExternalAlarmAsserted_Type=TruthValue
_AristaExternalAlarmAsserted_Object=MibTableColumn
aristaExternalAlarmAsserted=_AristaExternalAlarmAsserted_Object((1,3,6,1,4,1,30065,3,25,1,1,1,2),_AristaExternalAlarmAsserted_Type())
aristaExternalAlarmAsserted.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaExternalAlarmAsserted.setStatus(_A)
_AristaExternalAlarmCount_Type=Unsigned32
_AristaExternalAlarmCount_Object=MibTableColumn
aristaExternalAlarmCount=_AristaExternalAlarmCount_Object((1,3,6,1,4,1,30065,3,25,1,1,1,3),_AristaExternalAlarmCount_Type())
aristaExternalAlarmCount.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaExternalAlarmCount.setStatus(_A)
_AristaExternalAlarmLastAsserted_Type=TimeStamp
_AristaExternalAlarmLastAsserted_Object=MibTableColumn
aristaExternalAlarmLastAsserted=_AristaExternalAlarmLastAsserted_Object((1,3,6,1,4,1,30065,3,25,1,1,1,4),_AristaExternalAlarmLastAsserted_Type())
aristaExternalAlarmLastAsserted.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaExternalAlarmLastAsserted.setStatus(_A)
_AristaExternalAlarmLastDeasserted_Type=TimeStamp
_AristaExternalAlarmLastDeasserted_Object=MibTableColumn
aristaExternalAlarmLastDeasserted=_AristaExternalAlarmLastDeasserted_Object((1,3,6,1,4,1,30065,3,25,1,1,1,5),_AristaExternalAlarmLastDeasserted_Type())
aristaExternalAlarmLastDeasserted.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaExternalAlarmLastDeasserted.setStatus(_A)
_AristaExternalAlarmDescription_Type=DisplayString
_AristaExternalAlarmDescription_Object=MibTableColumn
aristaExternalAlarmDescription=_AristaExternalAlarmDescription_Object((1,3,6,1,4,1,30065,3,25,1,1,1,6),_AristaExternalAlarmDescription_Type())
aristaExternalAlarmDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaExternalAlarmDescription.setStatus(_A)
class _AristaExternalAlarmPolarity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('open',1),('closed',2)))
_AristaExternalAlarmPolarity_Type.__name__=_E
_AristaExternalAlarmPolarity_Object=MibTableColumn
aristaExternalAlarmPolarity=_AristaExternalAlarmPolarity_Object((1,3,6,1,4,1,30065,3,25,1,1,1,7),_AristaExternalAlarmPolarity_Type())
aristaExternalAlarmPolarity.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaExternalAlarmPolarity.setStatus(_A)
class _AristaExternalAlarmAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ignore',1),('syslog',2),('snmpTrap',3)))
_AristaExternalAlarmAction_Type.__name__=_E
_AristaExternalAlarmAction_Object=MibTableColumn
aristaExternalAlarmAction=_AristaExternalAlarmAction_Object((1,3,6,1,4,1,30065,3,25,1,1,1,8),_AristaExternalAlarmAction_Type())
aristaExternalAlarmAction.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaExternalAlarmAction.setStatus(_A)
_AristaExternalAlarmMibConformance_ObjectIdentity=ObjectIdentity
aristaExternalAlarmMibConformance=_AristaExternalAlarmMibConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,25,2))
_AristaExternalAlarmMibCompliances_ObjectIdentity=ObjectIdentity
aristaExternalAlarmMibCompliances=_AristaExternalAlarmMibCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,25,2,1))
_AristaExternalAlarmMibGroups_ObjectIdentity=ObjectIdentity
aristaExternalAlarmMibGroups=_AristaExternalAlarmMibGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,25,2,2))
aristaExternalAlarmObjectsGroup=ObjectGroup((1,3,6,1,4,1,30065,3,25,2,2,1))
aristaExternalAlarmObjectsGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_D),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:aristaExternalAlarmObjectsGroup.setStatus(_A)
aristaExternalAlarmAssertedNotif=NotificationType((1,3,6,1,4,1,30065,3,25,0,1))
aristaExternalAlarmAssertedNotif.setObjects((_B,_D))
if mibBuilder.loadTexts:aristaExternalAlarmAssertedNotif.setStatus(_A)
aristaExternalAlarmDeassertedNotif=NotificationType((1,3,6,1,4,1,30065,3,25,0,2))
aristaExternalAlarmDeassertedNotif.setObjects((_B,_D))
if mibBuilder.loadTexts:aristaExternalAlarmDeassertedNotif.setStatus(_A)
aristaExternalAlarmNotificationsGroup=NotificationGroup((1,3,6,1,4,1,30065,3,25,2,2,2))
aristaExternalAlarmNotificationsGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:aristaExternalAlarmNotificationsGroup.setStatus(_A)
aristaExternalAlarmMibCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,25,2,1,1))
aristaExternalAlarmMibCompliance.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:aristaExternalAlarmMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'aristaExternalAlarmMIB':aristaExternalAlarmMIB,'aristaExternalAlarmMibNotifications':aristaExternalAlarmMibNotifications,_M:aristaExternalAlarmAssertedNotif,_N:aristaExternalAlarmDeassertedNotif,'aristaExternalAlarmMibObjects':aristaExternalAlarmMibObjects,'aristaExternalAlarmTable':aristaExternalAlarmTable,'aristaExternalAlarmTableEntry':aristaExternalAlarmTableEntry,_F:aristaExternalAlarmId,_G:aristaExternalAlarmAsserted,_H:aristaExternalAlarmCount,_I:aristaExternalAlarmLastAsserted,_J:aristaExternalAlarmLastDeasserted,_D:aristaExternalAlarmDescription,_K:aristaExternalAlarmPolarity,_L:aristaExternalAlarmAction,'aristaExternalAlarmMibConformance':aristaExternalAlarmMibConformance,'aristaExternalAlarmMibCompliances':aristaExternalAlarmMibCompliances,'aristaExternalAlarmMibCompliance':aristaExternalAlarmMibCompliance,'aristaExternalAlarmMibGroups':aristaExternalAlarmMibGroups,_O:aristaExternalAlarmObjectsGroup,_P:aristaExternalAlarmNotificationsGroup})