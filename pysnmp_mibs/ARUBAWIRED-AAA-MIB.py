_T='arubaWiredAAATacacsStatusNotificationsGroup'
_S='arubaWiredTacacsServerGroup'
_R='arubaWiredAAARadiusStatusNotificationsGroup'
_Q='arubaWiredRadiusServerGroup'
_P='arubaWiredTacacsServerStatusChange'
_O='arubaWiredRadiusServerStatusChange'
_N='arubaWiredTacacsServerReachabilityStatus'
_M='arubaWiredRadiusServerReachabilityStatus'
_L='Unsigned32'
_K='arubaWiredTacacsServerPort'
_J='arubaWiredTacacsServerAddress'
_I='arubaWiredTacacsServerVrfName'
_H='arubaWiredRadiusServerPortType'
_G='arubaWiredRadiusServerPort'
_F='arubaWiredRadiusServerAddress'
_E='arubaWiredRadiusServerVrfName'
_D='DisplayString'
_C='read-only'
_B='current'
_A='ARUBAWIRED-AAA-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wndFeatures,=mibBuilder.importSymbols('ARUBAWIRED-NETWORKING-OID','wndFeatures')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
arubaWiredAAAMIB=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,16))
if mibBuilder.loadTexts:arubaWiredAAAMIB.setRevisions(('2021-07-14 00:00','2020-10-08 00:00'))
_ArubaWiredAAAStatusNotifications_ObjectIdentity=ObjectIdentity
arubaWiredAAAStatusNotifications=_ArubaWiredAAAStatusNotifications_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,16,0))
_ArubaWiredAAAObjects_ObjectIdentity=ObjectIdentity
arubaWiredAAAObjects=_ArubaWiredAAAObjects_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,16,1))
_ArubaWiredRadiusServer_ObjectIdentity=ObjectIdentity
arubaWiredRadiusServer=_ArubaWiredRadiusServer_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,16,1,1))
_ArubaWiredRadiusServerTable_Object=MibTable
arubaWiredRadiusServerTable=_ArubaWiredRadiusServerTable_Object((1,3,6,1,4,1,47196,4,1,1,3,16,1,1,1))
if mibBuilder.loadTexts:arubaWiredRadiusServerTable.setStatus(_B)
_ArubaWiredRadiusServerEntry_Object=MibTableRow
arubaWiredRadiusServerEntry=_ArubaWiredRadiusServerEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,16,1,1,1,1))
arubaWiredRadiusServerEntry.setIndexNames((0,_A,_E),(0,_A,_F),(0,_A,_G),(0,_A,_H))
if mibBuilder.loadTexts:arubaWiredRadiusServerEntry.setStatus(_B)
class _ArubaWiredRadiusServerVrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,33))
_ArubaWiredRadiusServerVrfName_Type.__name__=_D
_ArubaWiredRadiusServerVrfName_Object=MibTableColumn
arubaWiredRadiusServerVrfName=_ArubaWiredRadiusServerVrfName_Object((1,3,6,1,4,1,47196,4,1,1,3,16,1,1,1,1,1),_ArubaWiredRadiusServerVrfName_Type())
arubaWiredRadiusServerVrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRadiusServerVrfName.setStatus(_B)
class _ArubaWiredRadiusServerAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,257))
_ArubaWiredRadiusServerAddress_Type.__name__=_D
_ArubaWiredRadiusServerAddress_Object=MibTableColumn
arubaWiredRadiusServerAddress=_ArubaWiredRadiusServerAddress_Object((1,3,6,1,4,1,47196,4,1,1,3,16,1,1,1,1,2),_ArubaWiredRadiusServerAddress_Type())
arubaWiredRadiusServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRadiusServerAddress.setStatus(_B)
class _ArubaWiredRadiusServerPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ArubaWiredRadiusServerPort_Type.__name__=_L
_ArubaWiredRadiusServerPort_Object=MibTableColumn
arubaWiredRadiusServerPort=_ArubaWiredRadiusServerPort_Object((1,3,6,1,4,1,47196,4,1,1,3,16,1,1,1,1,3),_ArubaWiredRadiusServerPort_Type())
arubaWiredRadiusServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRadiusServerPort.setStatus(_B)
class _ArubaWiredRadiusServerPortType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_ArubaWiredRadiusServerPortType_Type.__name__=_D
_ArubaWiredRadiusServerPortType_Object=MibTableColumn
arubaWiredRadiusServerPortType=_ArubaWiredRadiusServerPortType_Object((1,3,6,1,4,1,47196,4,1,1,3,16,1,1,1,1,4),_ArubaWiredRadiusServerPortType_Type())
arubaWiredRadiusServerPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRadiusServerPortType.setStatus(_B)
class _ArubaWiredRadiusServerReachabilityStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArubaWiredRadiusServerReachabilityStatus_Type.__name__=_D
_ArubaWiredRadiusServerReachabilityStatus_Object=MibTableColumn
arubaWiredRadiusServerReachabilityStatus=_ArubaWiredRadiusServerReachabilityStatus_Object((1,3,6,1,4,1,47196,4,1,1,3,16,1,1,1,1,5),_ArubaWiredRadiusServerReachabilityStatus_Type())
arubaWiredRadiusServerReachabilityStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRadiusServerReachabilityStatus.setStatus(_B)
_ArubaWiredTacacsServer_ObjectIdentity=ObjectIdentity
arubaWiredTacacsServer=_ArubaWiredTacacsServer_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,16,1,2))
_ArubaWiredTacacsServerTable_Object=MibTable
arubaWiredTacacsServerTable=_ArubaWiredTacacsServerTable_Object((1,3,6,1,4,1,47196,4,1,1,3,16,1,2,1))
if mibBuilder.loadTexts:arubaWiredTacacsServerTable.setStatus(_B)
_ArubaWiredTacacsServerEntry_Object=MibTableRow
arubaWiredTacacsServerEntry=_ArubaWiredTacacsServerEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,16,1,2,1,1))
arubaWiredTacacsServerEntry.setIndexNames((0,_A,_I),(0,_A,_J),(0,_A,_K))
if mibBuilder.loadTexts:arubaWiredTacacsServerEntry.setStatus(_B)
class _ArubaWiredTacacsServerVrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,33))
_ArubaWiredTacacsServerVrfName_Type.__name__=_D
_ArubaWiredTacacsServerVrfName_Object=MibTableColumn
arubaWiredTacacsServerVrfName=_ArubaWiredTacacsServerVrfName_Object((1,3,6,1,4,1,47196,4,1,1,3,16,1,2,1,1,1),_ArubaWiredTacacsServerVrfName_Type())
arubaWiredTacacsServerVrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredTacacsServerVrfName.setStatus(_B)
class _ArubaWiredTacacsServerAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,257))
_ArubaWiredTacacsServerAddress_Type.__name__=_D
_ArubaWiredTacacsServerAddress_Object=MibTableColumn
arubaWiredTacacsServerAddress=_ArubaWiredTacacsServerAddress_Object((1,3,6,1,4,1,47196,4,1,1,3,16,1,2,1,1,2),_ArubaWiredTacacsServerAddress_Type())
arubaWiredTacacsServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredTacacsServerAddress.setStatus(_B)
class _ArubaWiredTacacsServerPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ArubaWiredTacacsServerPort_Type.__name__=_L
_ArubaWiredTacacsServerPort_Object=MibTableColumn
arubaWiredTacacsServerPort=_ArubaWiredTacacsServerPort_Object((1,3,6,1,4,1,47196,4,1,1,3,16,1,2,1,1,3),_ArubaWiredTacacsServerPort_Type())
arubaWiredTacacsServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredTacacsServerPort.setStatus(_B)
class _ArubaWiredTacacsServerReachabilityStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArubaWiredTacacsServerReachabilityStatus_Type.__name__=_D
_ArubaWiredTacacsServerReachabilityStatus_Object=MibTableColumn
arubaWiredTacacsServerReachabilityStatus=_ArubaWiredTacacsServerReachabilityStatus_Object((1,3,6,1,4,1,47196,4,1,1,3,16,1,2,1,1,4),_ArubaWiredTacacsServerReachabilityStatus_Type())
arubaWiredTacacsServerReachabilityStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredTacacsServerReachabilityStatus.setStatus(_B)
_ArubaWiredAAAServerConformance_ObjectIdentity=ObjectIdentity
arubaWiredAAAServerConformance=_ArubaWiredAAAServerConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,16,2))
_ArubaWiredRadiusServerGroups_ObjectIdentity=ObjectIdentity
arubaWiredRadiusServerGroups=_ArubaWiredRadiusServerGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,16,2,1))
_ArubaWiredRadiusServerCompliances_ObjectIdentity=ObjectIdentity
arubaWiredRadiusServerCompliances=_ArubaWiredRadiusServerCompliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,16,2,2))
_ArubaWiredTacacsServerGroups_ObjectIdentity=ObjectIdentity
arubaWiredTacacsServerGroups=_ArubaWiredTacacsServerGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,16,2,3))
_ArubaWiredTacacsServerCompliances_ObjectIdentity=ObjectIdentity
arubaWiredTacacsServerCompliances=_ArubaWiredTacacsServerCompliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,16,2,4))
arubaWiredRadiusServerGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,16,2,1,1))
arubaWiredRadiusServerGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_M)))
if mibBuilder.loadTexts:arubaWiredRadiusServerGroup.setStatus(_B)
arubaWiredTacacsServerGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,16,2,1,3))
arubaWiredTacacsServerGroup.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_N)))
if mibBuilder.loadTexts:arubaWiredTacacsServerGroup.setStatus(_B)
arubaWiredRadiusServerStatusChange=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,16,0,1))
arubaWiredRadiusServerStatusChange.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_M)))
if mibBuilder.loadTexts:arubaWiredRadiusServerStatusChange.setStatus(_B)
arubaWiredTacacsServerStatusChange=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,16,0,2))
arubaWiredTacacsServerStatusChange.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_N)))
if mibBuilder.loadTexts:arubaWiredTacacsServerStatusChange.setStatus(_B)
arubaWiredAAARadiusStatusNotificationsGroup=NotificationGroup((1,3,6,1,4,1,47196,4,1,1,3,16,2,1,2))
arubaWiredAAARadiusStatusNotificationsGroup.setObjects((_A,_O))
if mibBuilder.loadTexts:arubaWiredAAARadiusStatusNotificationsGroup.setStatus(_B)
arubaWiredAAATacacsStatusNotificationsGroup=NotificationGroup((1,3,6,1,4,1,47196,4,1,1,3,16,2,1,4))
arubaWiredAAATacacsStatusNotificationsGroup.setObjects((_A,_P))
if mibBuilder.loadTexts:arubaWiredAAATacacsStatusNotificationsGroup.setStatus(_B)
arubaWiredRadiusServerCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,16,2,2,1))
arubaWiredRadiusServerCompliance.setObjects(*((_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:arubaWiredRadiusServerCompliance.setStatus(_B)
arubaWiredTacacsServerCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,16,2,2,2))
arubaWiredTacacsServerCompliance.setObjects(*((_A,_S),(_A,_T)))
if mibBuilder.loadTexts:arubaWiredTacacsServerCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'arubaWiredAAAMIB':arubaWiredAAAMIB,'arubaWiredAAAStatusNotifications':arubaWiredAAAStatusNotifications,_O:arubaWiredRadiusServerStatusChange,_P:arubaWiredTacacsServerStatusChange,'arubaWiredAAAObjects':arubaWiredAAAObjects,'arubaWiredRadiusServer':arubaWiredRadiusServer,'arubaWiredRadiusServerTable':arubaWiredRadiusServerTable,'arubaWiredRadiusServerEntry':arubaWiredRadiusServerEntry,_E:arubaWiredRadiusServerVrfName,_F:arubaWiredRadiusServerAddress,_G:arubaWiredRadiusServerPort,_H:arubaWiredRadiusServerPortType,_M:arubaWiredRadiusServerReachabilityStatus,'arubaWiredTacacsServer':arubaWiredTacacsServer,'arubaWiredTacacsServerTable':arubaWiredTacacsServerTable,'arubaWiredTacacsServerEntry':arubaWiredTacacsServerEntry,_I:arubaWiredTacacsServerVrfName,_J:arubaWiredTacacsServerAddress,_K:arubaWiredTacacsServerPort,_N:arubaWiredTacacsServerReachabilityStatus,'arubaWiredAAAServerConformance':arubaWiredAAAServerConformance,'arubaWiredRadiusServerGroups':arubaWiredRadiusServerGroups,_Q:arubaWiredRadiusServerGroup,_R:arubaWiredAAARadiusStatusNotificationsGroup,_S:arubaWiredTacacsServerGroup,_T:arubaWiredAAATacacsStatusNotificationsGroup,'arubaWiredRadiusServerCompliances':arubaWiredRadiusServerCompliances,'arubaWiredRadiusServerCompliance':arubaWiredRadiusServerCompliance,'arubaWiredTacacsServerCompliance':arubaWiredTacacsServerCompliance,'arubaWiredTacacsServerGroups':arubaWiredTacacsServerGroups,'arubaWiredTacacsServerCompliances':arubaWiredTacacsServerCompliances})