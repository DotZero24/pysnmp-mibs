_L='wwpGenExtIgmpSnoopActEntry'
_K='wwpGenIgmpSnoopStatsVlanId'
_J='wwpGenIgmpSnoopGroupAddress'
_I='wwpGenIgmpSnoopVlanId'
_H='wwpGenIgmpSnoopActVlanId'
_G='seconds'
_F='WWP-GENERIC-IGMP-SNOOP-MIB'
_E='TruthValue'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_E)
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpGenIgmpSnoopMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,19))
if mibBuilder.loadTexts:wwpGenIgmpSnoopMIB.setRevisions(('2005-05-24 00:00','2003-05-02 00:00','2001-04-03 17:00'))
class PortList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class VlanId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_WwpGenIgmpSnoopMIBObjects_ObjectIdentity=ObjectIdentity
wwpGenIgmpSnoopMIBObjects=_WwpGenIgmpSnoopMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,19,1))
_WwpGenIgmpSnoop_ObjectIdentity=ObjectIdentity
wwpGenIgmpSnoop=_WwpGenIgmpSnoop_ObjectIdentity((1,3,6,1,4,1,6141,2,19,1,1))
class _WwpGenIgmpSnoopGlobalActivate_Type(TruthValue):defaultValue=1
_WwpGenIgmpSnoopGlobalActivate_Type.__name__=_E
_WwpGenIgmpSnoopGlobalActivate_Object=MibScalar
wwpGenIgmpSnoopGlobalActivate=_WwpGenIgmpSnoopGlobalActivate_Object((1,3,6,1,4,1,6141,2,19,1,1,1),_WwpGenIgmpSnoopGlobalActivate_Type())
wwpGenIgmpSnoopGlobalActivate.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpGenIgmpSnoopGlobalActivate.setStatus(_A)
_WwpGenIgmpSnoopActTable_Object=MibTable
wwpGenIgmpSnoopActTable=_WwpGenIgmpSnoopActTable_Object((1,3,6,1,4,1,6141,2,19,1,1,2))
if mibBuilder.loadTexts:wwpGenIgmpSnoopActTable.setStatus(_A)
_WwpGenIgmpSnoopActEntry_Object=MibTableRow
wwpGenIgmpSnoopActEntry=_WwpGenIgmpSnoopActEntry_Object((1,3,6,1,4,1,6141,2,19,1,1,2,1))
wwpGenIgmpSnoopActEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:wwpGenIgmpSnoopActEntry.setStatus(_A)
_WwpGenIgmpSnoopActVlanId_Type=VlanId
_WwpGenIgmpSnoopActVlanId_Object=MibTableColumn
wwpGenIgmpSnoopActVlanId=_WwpGenIgmpSnoopActVlanId_Object((1,3,6,1,4,1,6141,2,19,1,1,2,1,1),_WwpGenIgmpSnoopActVlanId_Type())
wwpGenIgmpSnoopActVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpGenIgmpSnoopActVlanId.setStatus(_A)
class _WwpGenIgmpSnoopRouterPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpGenIgmpSnoopRouterPort_Type.__name__=_D
_WwpGenIgmpSnoopRouterPort_Object=MibTableColumn
wwpGenIgmpSnoopRouterPort=_WwpGenIgmpSnoopRouterPort_Object((1,3,6,1,4,1,6141,2,19,1,1,2,1,2),_WwpGenIgmpSnoopRouterPort_Type())
wwpGenIgmpSnoopRouterPort.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpGenIgmpSnoopRouterPort.setStatus(_A)
class _WwpGenIgmpSnoopActivate_Type(TruthValue):defaultValue=1
_WwpGenIgmpSnoopActivate_Type.__name__=_E
_WwpGenIgmpSnoopActivate_Object=MibTableColumn
wwpGenIgmpSnoopActivate=_WwpGenIgmpSnoopActivate_Object((1,3,6,1,4,1,6141,2,19,1,1,2,1,3),_WwpGenIgmpSnoopActivate_Type())
wwpGenIgmpSnoopActivate.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpGenIgmpSnoopActivate.setStatus(_A)
_WwpGenIgmpSnoopTable_Object=MibTable
wwpGenIgmpSnoopTable=_WwpGenIgmpSnoopTable_Object((1,3,6,1,4,1,6141,2,19,1,1,3))
if mibBuilder.loadTexts:wwpGenIgmpSnoopTable.setStatus(_A)
_WwpGenIgmpSnoopEntry_Object=MibTableRow
wwpGenIgmpSnoopEntry=_WwpGenIgmpSnoopEntry_Object((1,3,6,1,4,1,6141,2,19,1,1,3,1))
wwpGenIgmpSnoopEntry.setIndexNames((0,_F,_I),(0,_F,_J))
if mibBuilder.loadTexts:wwpGenIgmpSnoopEntry.setStatus(_A)
_WwpGenIgmpSnoopVlanId_Type=VlanId
_WwpGenIgmpSnoopVlanId_Object=MibTableColumn
wwpGenIgmpSnoopVlanId=_WwpGenIgmpSnoopVlanId_Object((1,3,6,1,4,1,6141,2,19,1,1,3,1,1),_WwpGenIgmpSnoopVlanId_Type())
wwpGenIgmpSnoopVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpGenIgmpSnoopVlanId.setStatus(_A)
_WwpGenIgmpSnoopGroupAddress_Type=IpAddress
_WwpGenIgmpSnoopGroupAddress_Object=MibTableColumn
wwpGenIgmpSnoopGroupAddress=_WwpGenIgmpSnoopGroupAddress_Object((1,3,6,1,4,1,6141,2,19,1,1,3,1,2),_WwpGenIgmpSnoopGroupAddress_Type())
wwpGenIgmpSnoopGroupAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpGenIgmpSnoopGroupAddress.setStatus(_A)
_WwpGenIgmpSnoopActivePorts_Type=PortList
_WwpGenIgmpSnoopActivePorts_Object=MibTableColumn
wwpGenIgmpSnoopActivePorts=_WwpGenIgmpSnoopActivePorts_Object((1,3,6,1,4,1,6141,2,19,1,1,3,1,3),_WwpGenIgmpSnoopActivePorts_Type())
wwpGenIgmpSnoopActivePorts.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpGenIgmpSnoopActivePorts.setStatus(_A)
_WwpGenIgmpSnoopQueryTime_Type=TimeTicks
_WwpGenIgmpSnoopQueryTime_Object=MibTableColumn
wwpGenIgmpSnoopQueryTime=_WwpGenIgmpSnoopQueryTime_Object((1,3,6,1,4,1,6141,2,19,1,1,3,1,4),_WwpGenIgmpSnoopQueryTime_Type())
wwpGenIgmpSnoopQueryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpGenIgmpSnoopQueryTime.setStatus(_A)
class _WwpGenIgmpSnoopNoOfHosts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpGenIgmpSnoopNoOfHosts_Type.__name__=_D
_WwpGenIgmpSnoopNoOfHosts_Object=MibTableColumn
wwpGenIgmpSnoopNoOfHosts=_WwpGenIgmpSnoopNoOfHosts_Object((1,3,6,1,4,1,6141,2,19,1,1,3,1,5),_WwpGenIgmpSnoopNoOfHosts_Type())
wwpGenIgmpSnoopNoOfHosts.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpGenIgmpSnoopNoOfHosts.setStatus('deprecated')
_WwpGenIgmpSnoopStatsTable_Object=MibTable
wwpGenIgmpSnoopStatsTable=_WwpGenIgmpSnoopStatsTable_Object((1,3,6,1,4,1,6141,2,19,1,1,4))
if mibBuilder.loadTexts:wwpGenIgmpSnoopStatsTable.setStatus(_A)
_WwpGenIgmpSnoopStatsEntry_Object=MibTableRow
wwpGenIgmpSnoopStatsEntry=_WwpGenIgmpSnoopStatsEntry_Object((1,3,6,1,4,1,6141,2,19,1,1,4,1))
wwpGenIgmpSnoopStatsEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:wwpGenIgmpSnoopStatsEntry.setStatus(_A)
_WwpGenIgmpSnoopStatsVlanId_Type=VlanId
_WwpGenIgmpSnoopStatsVlanId_Object=MibTableColumn
wwpGenIgmpSnoopStatsVlanId=_WwpGenIgmpSnoopStatsVlanId_Object((1,3,6,1,4,1,6141,2,19,1,1,4,1,1),_WwpGenIgmpSnoopStatsVlanId_Type())
wwpGenIgmpSnoopStatsVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpGenIgmpSnoopStatsVlanId.setStatus(_A)
_WwpGenIgmpSnoopQueryMessages_Type=Counter32
_WwpGenIgmpSnoopQueryMessages_Object=MibTableColumn
wwpGenIgmpSnoopQueryMessages=_WwpGenIgmpSnoopQueryMessages_Object((1,3,6,1,4,1,6141,2,19,1,1,4,1,2),_WwpGenIgmpSnoopQueryMessages_Type())
wwpGenIgmpSnoopQueryMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpGenIgmpSnoopQueryMessages.setStatus(_A)
_WwpGenIgmpSnoopJoinMessages_Type=Counter32
_WwpGenIgmpSnoopJoinMessages_Object=MibTableColumn
wwpGenIgmpSnoopJoinMessages=_WwpGenIgmpSnoopJoinMessages_Object((1,3,6,1,4,1,6141,2,19,1,1,4,1,3),_WwpGenIgmpSnoopJoinMessages_Type())
wwpGenIgmpSnoopJoinMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpGenIgmpSnoopJoinMessages.setStatus(_A)
_WwpGenIgmpSnoopLeaveMessages_Type=Counter32
_WwpGenIgmpSnoopLeaveMessages_Object=MibTableColumn
wwpGenIgmpSnoopLeaveMessages=_WwpGenIgmpSnoopLeaveMessages_Object((1,3,6,1,4,1,6141,2,19,1,1,4,1,4),_WwpGenIgmpSnoopLeaveMessages_Type())
wwpGenIgmpSnoopLeaveMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpGenIgmpSnoopLeaveMessages.setStatus(_A)
_WwpGenIgmpSnoopRouterDiscards_Type=Counter32
_WwpGenIgmpSnoopRouterDiscards_Object=MibTableColumn
wwpGenIgmpSnoopRouterDiscards=_WwpGenIgmpSnoopRouterDiscards_Object((1,3,6,1,4,1,6141,2,19,1,1,4,1,5),_WwpGenIgmpSnoopRouterDiscards_Type())
wwpGenIgmpSnoopRouterDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpGenIgmpSnoopRouterDiscards.setStatus(_A)
class _WwpGenIgmpSnoopLingerTimeout_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WwpGenIgmpSnoopLingerTimeout_Type.__name__=_D
_WwpGenIgmpSnoopLingerTimeout_Object=MibScalar
wwpGenIgmpSnoopLingerTimeout=_WwpGenIgmpSnoopLingerTimeout_Object((1,3,6,1,4,1,6141,2,19,1,1,5),_WwpGenIgmpSnoopLingerTimeout_Type())
wwpGenIgmpSnoopLingerTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpGenIgmpSnoopLingerTimeout.setStatus(_A)
if mibBuilder.loadTexts:wwpGenIgmpSnoopLingerTimeout.setUnits(_G)
class _WwpGenIgmpSnoopExpiryTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpGenIgmpSnoopExpiryTimeout_Type.__name__=_D
_WwpGenIgmpSnoopExpiryTimeout_Object=MibScalar
wwpGenIgmpSnoopExpiryTimeout=_WwpGenIgmpSnoopExpiryTimeout_Object((1,3,6,1,4,1,6141,2,19,1,1,6),_WwpGenIgmpSnoopExpiryTimeout_Type())
wwpGenIgmpSnoopExpiryTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpGenIgmpSnoopExpiryTimeout.setStatus(_A)
if mibBuilder.loadTexts:wwpGenIgmpSnoopExpiryTimeout.setUnits(_G)
class _WwpGenIgmpSnoopQueryRespTimeout_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpGenIgmpSnoopQueryRespTimeout_Type.__name__=_D
_WwpGenIgmpSnoopQueryRespTimeout_Object=MibScalar
wwpGenIgmpSnoopQueryRespTimeout=_WwpGenIgmpSnoopQueryRespTimeout_Object((1,3,6,1,4,1,6141,2,19,1,1,7),_WwpGenIgmpSnoopQueryRespTimeout_Type())
wwpGenIgmpSnoopQueryRespTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpGenIgmpSnoopQueryRespTimeout.setStatus(_A)
if mibBuilder.loadTexts:wwpGenIgmpSnoopQueryRespTimeout.setUnits(_G)
class _WwpGenIgmpSnoopFilterActivate_Type(TruthValue):defaultValue=2
_WwpGenIgmpSnoopFilterActivate_Type.__name__=_E
_WwpGenIgmpSnoopFilterActivate_Object=MibScalar
wwpGenIgmpSnoopFilterActivate=_WwpGenIgmpSnoopFilterActivate_Object((1,3,6,1,4,1,6141,2,19,1,1,8),_WwpGenIgmpSnoopFilterActivate_Type())
wwpGenIgmpSnoopFilterActivate.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpGenIgmpSnoopFilterActivate.setStatus(_A)
_WwpGenExtIgmpSnoopActEntryTable_Object=MibTable
wwpGenExtIgmpSnoopActEntryTable=_WwpGenExtIgmpSnoopActEntryTable_Object((1,3,6,1,4,1,6141,2,19,1,1,9))
if mibBuilder.loadTexts:wwpGenExtIgmpSnoopActEntryTable.setStatus(_A)
_WwpGenExtIgmpSnoopActEntry_Object=MibTableRow
wwpGenExtIgmpSnoopActEntry=_WwpGenExtIgmpSnoopActEntry_Object((1,3,6,1,4,1,6141,2,19,1,1,9,1))
if mibBuilder.loadTexts:wwpGenExtIgmpSnoopActEntry.setStatus(_A)
class _WwpGenIgmpSnoopMinQueryTimeout_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpGenIgmpSnoopMinQueryTimeout_Type.__name__=_D
_WwpGenIgmpSnoopMinQueryTimeout_Object=MibTableColumn
wwpGenIgmpSnoopMinQueryTimeout=_WwpGenIgmpSnoopMinQueryTimeout_Object((1,3,6,1,4,1,6141,2,19,1,1,9,1,1),_WwpGenIgmpSnoopMinQueryTimeout_Type())
wwpGenIgmpSnoopMinQueryTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpGenIgmpSnoopMinQueryTimeout.setStatus(_A)
if mibBuilder.loadTexts:wwpGenIgmpSnoopMinQueryTimeout.setUnits(_G)
class _WwpGenIgmpSnoopUnresolvedMcastFilter_Type(TruthValue):defaultValue=2
_WwpGenIgmpSnoopUnresolvedMcastFilter_Type.__name__=_E
_WwpGenIgmpSnoopUnresolvedMcastFilter_Object=MibTableColumn
wwpGenIgmpSnoopUnresolvedMcastFilter=_WwpGenIgmpSnoopUnresolvedMcastFilter_Object((1,3,6,1,4,1,6141,2,19,1,1,9,1,2),_WwpGenIgmpSnoopUnresolvedMcastFilter_Type())
wwpGenIgmpSnoopUnresolvedMcastFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpGenIgmpSnoopUnresolvedMcastFilter.setStatus(_A)
class _WwpGenIgmpSnoopPktPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpGenIgmpSnoopPktPriority_Type.__name__=_D
_WwpGenIgmpSnoopPktPriority_Object=MibTableColumn
wwpGenIgmpSnoopPktPriority=_WwpGenIgmpSnoopPktPriority_Object((1,3,6,1,4,1,6141,2,19,1,1,9,1,3),_WwpGenIgmpSnoopPktPriority_Type())
wwpGenIgmpSnoopPktPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpGenIgmpSnoopPktPriority.setStatus(_A)
class _WwpGenIgmpSnoopLeaveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fast',1),('inquisitive',2)))
_WwpGenIgmpSnoopLeaveMode_Type.__name__=_D
_WwpGenIgmpSnoopLeaveMode_Object=MibTableColumn
wwpGenIgmpSnoopLeaveMode=_WwpGenIgmpSnoopLeaveMode_Object((1,3,6,1,4,1,6141,2,19,1,1,9,1,4),_WwpGenIgmpSnoopLeaveMode_Type())
wwpGenIgmpSnoopLeaveMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpGenIgmpSnoopLeaveMode.setStatus(_A)
class _WwpGenIgmpSnoopInqLeaveTimeout_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_WwpGenIgmpSnoopInqLeaveTimeout_Type.__name__=_D
_WwpGenIgmpSnoopInqLeaveTimeout_Object=MibScalar
wwpGenIgmpSnoopInqLeaveTimeout=_WwpGenIgmpSnoopInqLeaveTimeout_Object((1,3,6,1,4,1,6141,2,19,1,1,10),_WwpGenIgmpSnoopInqLeaveTimeout_Type())
wwpGenIgmpSnoopInqLeaveTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpGenIgmpSnoopInqLeaveTimeout.setStatus(_A)
class _WwpGenIgmpSnoopUMFFilterGlobal_Type(TruthValue):defaultValue=2
_WwpGenIgmpSnoopUMFFilterGlobal_Type.__name__=_E
_WwpGenIgmpSnoopUMFFilterGlobal_Object=MibScalar
wwpGenIgmpSnoopUMFFilterGlobal=_WwpGenIgmpSnoopUMFFilterGlobal_Object((1,3,6,1,4,1,6141,2,19,1,1,11),_WwpGenIgmpSnoopUMFFilterGlobal_Type())
wwpGenIgmpSnoopUMFFilterGlobal.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpGenIgmpSnoopUMFFilterGlobal.setStatus(_A)
_WwpGenIgmpSnoopMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpGenIgmpSnoopMIBNotificationPrefix=_WwpGenIgmpSnoopMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,19,2))
_WwpGenIgmpSnoopMIBNotifications_ObjectIdentity=ObjectIdentity
wwpGenIgmpSnoopMIBNotifications=_WwpGenIgmpSnoopMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,19,2,0))
_WwpGenIgmpSnoopMIBConformance_ObjectIdentity=ObjectIdentity
wwpGenIgmpSnoopMIBConformance=_WwpGenIgmpSnoopMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,19,3))
_WwpGenIgmpSnoopMIBCompliances_ObjectIdentity=ObjectIdentity
wwpGenIgmpSnoopMIBCompliances=_WwpGenIgmpSnoopMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,19,3,1))
_WwpGenIgmpSnoopMIBGroups_ObjectIdentity=ObjectIdentity
wwpGenIgmpSnoopMIBGroups=_WwpGenIgmpSnoopMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,19,3,2))
wwpGenIgmpSnoopActEntry.registerAugmentions((_F,_L))
wwpGenExtIgmpSnoopActEntry.setIndexNames(*wwpGenIgmpSnoopActEntry.getIndexNames())
mibBuilder.exportSymbols(_F,**{'PortList':PortList,'VlanId':VlanId,'wwpGenIgmpSnoopMIB':wwpGenIgmpSnoopMIB,'wwpGenIgmpSnoopMIBObjects':wwpGenIgmpSnoopMIBObjects,'wwpGenIgmpSnoop':wwpGenIgmpSnoop,'wwpGenIgmpSnoopGlobalActivate':wwpGenIgmpSnoopGlobalActivate,'wwpGenIgmpSnoopActTable':wwpGenIgmpSnoopActTable,'wwpGenIgmpSnoopActEntry':wwpGenIgmpSnoopActEntry,_H:wwpGenIgmpSnoopActVlanId,'wwpGenIgmpSnoopRouterPort':wwpGenIgmpSnoopRouterPort,'wwpGenIgmpSnoopActivate':wwpGenIgmpSnoopActivate,'wwpGenIgmpSnoopTable':wwpGenIgmpSnoopTable,'wwpGenIgmpSnoopEntry':wwpGenIgmpSnoopEntry,_I:wwpGenIgmpSnoopVlanId,_J:wwpGenIgmpSnoopGroupAddress,'wwpGenIgmpSnoopActivePorts':wwpGenIgmpSnoopActivePorts,'wwpGenIgmpSnoopQueryTime':wwpGenIgmpSnoopQueryTime,'wwpGenIgmpSnoopNoOfHosts':wwpGenIgmpSnoopNoOfHosts,'wwpGenIgmpSnoopStatsTable':wwpGenIgmpSnoopStatsTable,'wwpGenIgmpSnoopStatsEntry':wwpGenIgmpSnoopStatsEntry,_K:wwpGenIgmpSnoopStatsVlanId,'wwpGenIgmpSnoopQueryMessages':wwpGenIgmpSnoopQueryMessages,'wwpGenIgmpSnoopJoinMessages':wwpGenIgmpSnoopJoinMessages,'wwpGenIgmpSnoopLeaveMessages':wwpGenIgmpSnoopLeaveMessages,'wwpGenIgmpSnoopRouterDiscards':wwpGenIgmpSnoopRouterDiscards,'wwpGenIgmpSnoopLingerTimeout':wwpGenIgmpSnoopLingerTimeout,'wwpGenIgmpSnoopExpiryTimeout':wwpGenIgmpSnoopExpiryTimeout,'wwpGenIgmpSnoopQueryRespTimeout':wwpGenIgmpSnoopQueryRespTimeout,'wwpGenIgmpSnoopFilterActivate':wwpGenIgmpSnoopFilterActivate,'wwpGenExtIgmpSnoopActEntryTable':wwpGenExtIgmpSnoopActEntryTable,_L:wwpGenExtIgmpSnoopActEntry,'wwpGenIgmpSnoopMinQueryTimeout':wwpGenIgmpSnoopMinQueryTimeout,'wwpGenIgmpSnoopUnresolvedMcastFilter':wwpGenIgmpSnoopUnresolvedMcastFilter,'wwpGenIgmpSnoopPktPriority':wwpGenIgmpSnoopPktPriority,'wwpGenIgmpSnoopLeaveMode':wwpGenIgmpSnoopLeaveMode,'wwpGenIgmpSnoopInqLeaveTimeout':wwpGenIgmpSnoopInqLeaveTimeout,'wwpGenIgmpSnoopUMFFilterGlobal':wwpGenIgmpSnoopUMFFilterGlobal,'wwpGenIgmpSnoopMIBNotificationPrefix':wwpGenIgmpSnoopMIBNotificationPrefix,'wwpGenIgmpSnoopMIBNotifications':wwpGenIgmpSnoopMIBNotifications,'wwpGenIgmpSnoopMIBConformance':wwpGenIgmpSnoopMIBConformance,'wwpGenIgmpSnoopMIBCompliances':wwpGenIgmpSnoopMIBCompliances,'wwpGenIgmpSnoopMIBGroups':wwpGenIgmpSnoopMIBGroups})