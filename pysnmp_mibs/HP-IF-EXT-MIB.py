_M='hpifStatsGroup'
_L='hpifStatsNumSessions'
_K='hpifStatsIntRoamsFrom'
_J='hpifStatsIntRoamsTo'
_I='hpifStatsExtRoamsFrom'
_H='hpifStatsExtRoamsTo'
_G='hpifStatsNumClients'
_F='hpifStatsPort'
_E='hpifStatsSlot'
_D='hpifStatsEntry'
_C='read-only'
_B='HP-IF-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpProcurveCommon,=mibBuilder.importSymbols('HP-BASE-MIB','hpProcurveCommon')
ifEntry,ifIndex=mibBuilder.importSymbols('IF-MIB','ifEntry','ifIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
hpIfExtMIB=ModuleIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,2))
if mibBuilder.loadTexts:hpIfExtMIB.setRevisions(('2005-02-01 14:55',))
_HpifMIBObjects_ObjectIdentity=ObjectIdentity
hpifMIBObjects=_HpifMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,2,1))
_HpifStats_ObjectIdentity=ObjectIdentity
hpifStats=_HpifStats_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,2,1,1))
_HpifStatsTable_Object=MibTable
hpifStatsTable=_HpifStatsTable_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,2,1,1,1))
if mibBuilder.loadTexts:hpifStatsTable.setStatus(_A)
_HpifStatsEntry_Object=MibTableRow
hpifStatsEntry=_HpifStatsEntry_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,2,1,1,1,1))
if mibBuilder.loadTexts:hpifStatsEntry.setStatus(_A)
_HpifStatsSlot_Type=Unsigned32
_HpifStatsSlot_Object=MibTableColumn
hpifStatsSlot=_HpifStatsSlot_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,2,1,1,1,1,1),_HpifStatsSlot_Type())
hpifStatsSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:hpifStatsSlot.setStatus(_A)
_HpifStatsPort_Type=Unsigned32
_HpifStatsPort_Object=MibTableColumn
hpifStatsPort=_HpifStatsPort_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,2,1,1,1,1,2),_HpifStatsPort_Type())
hpifStatsPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpifStatsPort.setStatus(_A)
_HpifStatsNumClients_Type=Gauge32
_HpifStatsNumClients_Object=MibTableColumn
hpifStatsNumClients=_HpifStatsNumClients_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,2,1,1,1,1,3),_HpifStatsNumClients_Type())
hpifStatsNumClients.setMaxAccess(_C)
if mibBuilder.loadTexts:hpifStatsNumClients.setStatus(_A)
_HpifStatsExtRoamsTo_Type=Counter32
_HpifStatsExtRoamsTo_Object=MibTableColumn
hpifStatsExtRoamsTo=_HpifStatsExtRoamsTo_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,2,1,1,1,1,4),_HpifStatsExtRoamsTo_Type())
hpifStatsExtRoamsTo.setMaxAccess(_C)
if mibBuilder.loadTexts:hpifStatsExtRoamsTo.setStatus(_A)
_HpifStatsExtRoamsFrom_Type=Counter32
_HpifStatsExtRoamsFrom_Object=MibTableColumn
hpifStatsExtRoamsFrom=_HpifStatsExtRoamsFrom_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,2,1,1,1,1,5),_HpifStatsExtRoamsFrom_Type())
hpifStatsExtRoamsFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:hpifStatsExtRoamsFrom.setStatus(_A)
_HpifStatsIntRoamsTo_Type=Counter32
_HpifStatsIntRoamsTo_Object=MibTableColumn
hpifStatsIntRoamsTo=_HpifStatsIntRoamsTo_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,2,1,1,1,1,6),_HpifStatsIntRoamsTo_Type())
hpifStatsIntRoamsTo.setMaxAccess(_C)
if mibBuilder.loadTexts:hpifStatsIntRoamsTo.setStatus(_A)
_HpifStatsIntRoamsFrom_Type=Counter32
_HpifStatsIntRoamsFrom_Object=MibTableColumn
hpifStatsIntRoamsFrom=_HpifStatsIntRoamsFrom_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,2,1,1,1,1,7),_HpifStatsIntRoamsFrom_Type())
hpifStatsIntRoamsFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:hpifStatsIntRoamsFrom.setStatus(_A)
_HpifStatsNumSessions_Type=Gauge32
_HpifStatsNumSessions_Object=MibTableColumn
hpifStatsNumSessions=_HpifStatsNumSessions_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,2,1,1,1,1,8),_HpifStatsNumSessions_Type())
hpifStatsNumSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:hpifStatsNumSessions.setStatus(_A)
_HpifNotificationConfig_ObjectIdentity=ObjectIdentity
hpifNotificationConfig=_HpifNotificationConfig_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,2,1,3))
_HpifExtMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
hpifExtMIBNotificationsPrefix=_HpifExtMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,2,2))
_HpifExtMIBNotifications_ObjectIdentity=ObjectIdentity
hpifExtMIBNotifications=_HpifExtMIBNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,2,2,0))
_HpIfExtMIBConformance_ObjectIdentity=ObjectIdentity
hpIfExtMIBConformance=_HpIfExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,2,3))
_HpifCompliances_ObjectIdentity=ObjectIdentity
hpifCompliances=_HpifCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,2,3,1))
_HpifGroups_ObjectIdentity=ObjectIdentity
hpifGroups=_HpifGroups_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,2,3,2))
ifEntry.registerAugmentions((_B,_D))
hpifStatsEntry.setIndexNames(*ifEntry.getIndexNames())
hpifStatsGroup=ObjectGroup((1,3,6,1,4,1,11,2,3,7,11,17,7,1,2,3,2,1))
hpifStatsGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:hpifStatsGroup.setStatus(_A)
hpifExtMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,3,7,11,17,7,1,2,3,1,1))
hpifExtMIBCompliance1.setObjects((_B,_M))
if mibBuilder.loadTexts:hpifExtMIBCompliance1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpIfExtMIB':hpIfExtMIB,'hpifMIBObjects':hpifMIBObjects,'hpifStats':hpifStats,'hpifStatsTable':hpifStatsTable,_D:hpifStatsEntry,_E:hpifStatsSlot,_F:hpifStatsPort,_G:hpifStatsNumClients,_H:hpifStatsExtRoamsTo,_I:hpifStatsExtRoamsFrom,_J:hpifStatsIntRoamsTo,_K:hpifStatsIntRoamsFrom,_L:hpifStatsNumSessions,'hpifNotificationConfig':hpifNotificationConfig,'hpifExtMIBNotificationsPrefix':hpifExtMIBNotificationsPrefix,'hpifExtMIBNotifications':hpifExtMIBNotifications,'hpIfExtMIBConformance':hpIfExtMIBConformance,'hpifCompliances':hpifCompliances,'hpifExtMIBCompliance1':hpifExtMIBCompliance1,'hpifGroups':hpifGroups,_M:hpifStatsGroup})