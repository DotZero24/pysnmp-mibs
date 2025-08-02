_K='disable'
_J='enable'
_I='wwpIgmpSnoopGroupAddress'
_H='wwpIgmpSnoopVlanId'
_G='TruthValue'
_F='seconds'
_E='WWP-IGMP-SNOOP-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_G)
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpIgmpSnoopMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,10))
if mibBuilder.loadTexts:wwpIgmpSnoopMIB.setRevisions(('2001-04-03 17:00',))
class PortList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class VlanId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_WwpIgmpSnoopMIBObjects_ObjectIdentity=ObjectIdentity
wwpIgmpSnoopMIBObjects=_WwpIgmpSnoopMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,10,1))
_WwpIgmpSnoop_ObjectIdentity=ObjectIdentity
wwpIgmpSnoop=_WwpIgmpSnoop_ObjectIdentity((1,3,6,1,4,1,6141,2,10,1,1))
class _WwpIgmpSnoopActivate_Type(TruthValue):defaultValue=2
_WwpIgmpSnoopActivate_Type.__name__=_G
_WwpIgmpSnoopActivate_Object=MibScalar
wwpIgmpSnoopActivate=_WwpIgmpSnoopActivate_Object((1,3,6,1,4,1,6141,2,10,1,1,1),_WwpIgmpSnoopActivate_Type())
wwpIgmpSnoopActivate.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpIgmpSnoopActivate.setStatus(_A)
_WwpIgmpSnoopTable_Object=MibTable
wwpIgmpSnoopTable=_WwpIgmpSnoopTable_Object((1,3,6,1,4,1,6141,2,10,1,1,2))
if mibBuilder.loadTexts:wwpIgmpSnoopTable.setStatus(_A)
_WwpIgmpSnoopEntry_Object=MibTableRow
wwpIgmpSnoopEntry=_WwpIgmpSnoopEntry_Object((1,3,6,1,4,1,6141,2,10,1,1,2,1))
wwpIgmpSnoopEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:wwpIgmpSnoopEntry.setStatus(_A)
_WwpIgmpSnoopVlanId_Type=VlanId
_WwpIgmpSnoopVlanId_Object=MibTableColumn
wwpIgmpSnoopVlanId=_WwpIgmpSnoopVlanId_Object((1,3,6,1,4,1,6141,2,10,1,1,2,1,1),_WwpIgmpSnoopVlanId_Type())
wwpIgmpSnoopVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpIgmpSnoopVlanId.setStatus(_A)
_WwpIgmpSnoopGroupAddress_Type=IpAddress
_WwpIgmpSnoopGroupAddress_Object=MibTableColumn
wwpIgmpSnoopGroupAddress=_WwpIgmpSnoopGroupAddress_Object((1,3,6,1,4,1,6141,2,10,1,1,2,1,2),_WwpIgmpSnoopGroupAddress_Type())
wwpIgmpSnoopGroupAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpIgmpSnoopGroupAddress.setStatus(_A)
_WwpIgmpSnoopActivePorts_Type=PortList
_WwpIgmpSnoopActivePorts_Object=MibTableColumn
wwpIgmpSnoopActivePorts=_WwpIgmpSnoopActivePorts_Object((1,3,6,1,4,1,6141,2,10,1,1,2,1,3),_WwpIgmpSnoopActivePorts_Type())
wwpIgmpSnoopActivePorts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpIgmpSnoopActivePorts.setStatus(_A)
class _WwpIgmpSnoopRouterPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpIgmpSnoopRouterPort_Type.__name__=_C
_WwpIgmpSnoopRouterPort_Object=MibTableColumn
wwpIgmpSnoopRouterPort=_WwpIgmpSnoopRouterPort_Object((1,3,6,1,4,1,6141,2,10,1,1,2,1,4),_WwpIgmpSnoopRouterPort_Type())
wwpIgmpSnoopRouterPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpIgmpSnoopRouterPort.setStatus(_A)
_WwpIgmpSnoopQueryTime_Type=TimeTicks
_WwpIgmpSnoopQueryTime_Object=MibTableColumn
wwpIgmpSnoopQueryTime=_WwpIgmpSnoopQueryTime_Object((1,3,6,1,4,1,6141,2,10,1,1,2,1,5),_WwpIgmpSnoopQueryTime_Type())
wwpIgmpSnoopQueryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpIgmpSnoopQueryTime.setStatus(_A)
class _WwpIgmpSnoopLingerTimeout_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WwpIgmpSnoopLingerTimeout_Type.__name__=_C
_WwpIgmpSnoopLingerTimeout_Object=MibScalar
wwpIgmpSnoopLingerTimeout=_WwpIgmpSnoopLingerTimeout_Object((1,3,6,1,4,1,6141,2,10,1,1,3),_WwpIgmpSnoopLingerTimeout_Type())
wwpIgmpSnoopLingerTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpIgmpSnoopLingerTimeout.setStatus(_A)
if mibBuilder.loadTexts:wwpIgmpSnoopLingerTimeout.setUnits(_F)
class _WwpIgmpSnoopExpiryTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpIgmpSnoopExpiryTimeout_Type.__name__=_C
_WwpIgmpSnoopExpiryTimeout_Object=MibScalar
wwpIgmpSnoopExpiryTimeout=_WwpIgmpSnoopExpiryTimeout_Object((1,3,6,1,4,1,6141,2,10,1,1,4),_WwpIgmpSnoopExpiryTimeout_Type())
wwpIgmpSnoopExpiryTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpIgmpSnoopExpiryTimeout.setStatus(_A)
if mibBuilder.loadTexts:wwpIgmpSnoopExpiryTimeout.setUnits(_F)
_WwpIgmpSnoopQueryMessages_Type=Counter32
_WwpIgmpSnoopQueryMessages_Object=MibScalar
wwpIgmpSnoopQueryMessages=_WwpIgmpSnoopQueryMessages_Object((1,3,6,1,4,1,6141,2,10,1,1,5),_WwpIgmpSnoopQueryMessages_Type())
wwpIgmpSnoopQueryMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpIgmpSnoopQueryMessages.setStatus(_A)
_WwpIgmpSnoopJoinMessages_Type=Counter32
_WwpIgmpSnoopJoinMessages_Object=MibScalar
wwpIgmpSnoopJoinMessages=_WwpIgmpSnoopJoinMessages_Object((1,3,6,1,4,1,6141,2,10,1,1,6),_WwpIgmpSnoopJoinMessages_Type())
wwpIgmpSnoopJoinMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpIgmpSnoopJoinMessages.setStatus(_A)
_WwpIgmpSnoopLeaveMessages_Type=Counter32
_WwpIgmpSnoopLeaveMessages_Object=MibScalar
wwpIgmpSnoopLeaveMessages=_WwpIgmpSnoopLeaveMessages_Object((1,3,6,1,4,1,6141,2,10,1,1,7),_WwpIgmpSnoopLeaveMessages_Type())
wwpIgmpSnoopLeaveMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpIgmpSnoopLeaveMessages.setStatus(_A)
_WwpIgmpSnoopRouterDiscards_Type=Counter32
_WwpIgmpSnoopRouterDiscards_Object=MibScalar
wwpIgmpSnoopRouterDiscards=_WwpIgmpSnoopRouterDiscards_Object((1,3,6,1,4,1,6141,2,10,1,1,8),_WwpIgmpSnoopRouterDiscards_Type())
wwpIgmpSnoopRouterDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpIgmpSnoopRouterDiscards.setStatus(_A)
class _WwpIgmpSnoopMinQueryTimeout_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpIgmpSnoopMinQueryTimeout_Type.__name__=_C
_WwpIgmpSnoopMinQueryTimeout_Object=MibScalar
wwpIgmpSnoopMinQueryTimeout=_WwpIgmpSnoopMinQueryTimeout_Object((1,3,6,1,4,1,6141,2,10,1,1,9),_WwpIgmpSnoopMinQueryTimeout_Type())
wwpIgmpSnoopMinQueryTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpIgmpSnoopMinQueryTimeout.setStatus(_A)
if mibBuilder.loadTexts:wwpIgmpSnoopMinQueryTimeout.setUnits(_F)
class _WwpIgmpSnoopLeaveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fast',1),('inquisitive',2)))
_WwpIgmpSnoopLeaveMode_Type.__name__=_C
_WwpIgmpSnoopLeaveMode_Object=MibScalar
wwpIgmpSnoopLeaveMode=_WwpIgmpSnoopLeaveMode_Object((1,3,6,1,4,1,6141,2,10,1,1,10),_WwpIgmpSnoopLeaveMode_Type())
wwpIgmpSnoopLeaveMode.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpIgmpSnoopLeaveMode.setStatus(_A)
class _WwpIgmpSnoopInqLeaveTimeout_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpIgmpSnoopInqLeaveTimeout_Type.__name__=_C
_WwpIgmpSnoopInqLeaveTimeout_Object=MibScalar
wwpIgmpSnoopInqLeaveTimeout=_WwpIgmpSnoopInqLeaveTimeout_Object((1,3,6,1,4,1,6141,2,10,1,1,11),_WwpIgmpSnoopInqLeaveTimeout_Type())
wwpIgmpSnoopInqLeaveTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpIgmpSnoopInqLeaveTimeout.setStatus(_A)
class _WwpIgmpSnoopUnresMcastFilterAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_WwpIgmpSnoopUnresMcastFilterAdminStatus_Type.__name__=_C
_WwpIgmpSnoopUnresMcastFilterAdminStatus_Object=MibScalar
wwpIgmpSnoopUnresMcastFilterAdminStatus=_WwpIgmpSnoopUnresMcastFilterAdminStatus_Object((1,3,6,1,4,1,6141,2,10,1,1,12),_WwpIgmpSnoopUnresMcastFilterAdminStatus_Type())
wwpIgmpSnoopUnresMcastFilterAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpIgmpSnoopUnresMcastFilterAdminStatus.setStatus(_A)
class _WwpIgmpSnoopUnresMcastFilterOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_WwpIgmpSnoopUnresMcastFilterOperStatus_Type.__name__=_C
_WwpIgmpSnoopUnresMcastFilterOperStatus_Object=MibScalar
wwpIgmpSnoopUnresMcastFilterOperStatus=_WwpIgmpSnoopUnresMcastFilterOperStatus_Object((1,3,6,1,4,1,6141,2,10,1,1,13),_WwpIgmpSnoopUnresMcastFilterOperStatus_Type())
wwpIgmpSnoopUnresMcastFilterOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpIgmpSnoopUnresMcastFilterOperStatus.setStatus(_A)
_WwpIgmpSnoopMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpIgmpSnoopMIBNotificationPrefix=_WwpIgmpSnoopMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,10,2))
_WwpIgmpSnoopMIBNotifications_ObjectIdentity=ObjectIdentity
wwpIgmpSnoopMIBNotifications=_WwpIgmpSnoopMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,10,2,0))
_WwpIgmpSnoopMIBConformance_ObjectIdentity=ObjectIdentity
wwpIgmpSnoopMIBConformance=_WwpIgmpSnoopMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,10,3))
_WwpIgmpSnoopMIBCompliances_ObjectIdentity=ObjectIdentity
wwpIgmpSnoopMIBCompliances=_WwpIgmpSnoopMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,10,3,1))
_WwpIgmpSnoopMIBGroups_ObjectIdentity=ObjectIdentity
wwpIgmpSnoopMIBGroups=_WwpIgmpSnoopMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,10,3,2))
mibBuilder.exportSymbols(_E,**{'PortList':PortList,'VlanId':VlanId,'wwpIgmpSnoopMIB':wwpIgmpSnoopMIB,'wwpIgmpSnoopMIBObjects':wwpIgmpSnoopMIBObjects,'wwpIgmpSnoop':wwpIgmpSnoop,'wwpIgmpSnoopActivate':wwpIgmpSnoopActivate,'wwpIgmpSnoopTable':wwpIgmpSnoopTable,'wwpIgmpSnoopEntry':wwpIgmpSnoopEntry,_H:wwpIgmpSnoopVlanId,_I:wwpIgmpSnoopGroupAddress,'wwpIgmpSnoopActivePorts':wwpIgmpSnoopActivePorts,'wwpIgmpSnoopRouterPort':wwpIgmpSnoopRouterPort,'wwpIgmpSnoopQueryTime':wwpIgmpSnoopQueryTime,'wwpIgmpSnoopLingerTimeout':wwpIgmpSnoopLingerTimeout,'wwpIgmpSnoopExpiryTimeout':wwpIgmpSnoopExpiryTimeout,'wwpIgmpSnoopQueryMessages':wwpIgmpSnoopQueryMessages,'wwpIgmpSnoopJoinMessages':wwpIgmpSnoopJoinMessages,'wwpIgmpSnoopLeaveMessages':wwpIgmpSnoopLeaveMessages,'wwpIgmpSnoopRouterDiscards':wwpIgmpSnoopRouterDiscards,'wwpIgmpSnoopMinQueryTimeout':wwpIgmpSnoopMinQueryTimeout,'wwpIgmpSnoopLeaveMode':wwpIgmpSnoopLeaveMode,'wwpIgmpSnoopInqLeaveTimeout':wwpIgmpSnoopInqLeaveTimeout,'wwpIgmpSnoopUnresMcastFilterAdminStatus':wwpIgmpSnoopUnresMcastFilterAdminStatus,'wwpIgmpSnoopUnresMcastFilterOperStatus':wwpIgmpSnoopUnresMcastFilterOperStatus,'wwpIgmpSnoopMIBNotificationPrefix':wwpIgmpSnoopMIBNotificationPrefix,'wwpIgmpSnoopMIBNotifications':wwpIgmpSnoopMIBNotifications,'wwpIgmpSnoopMIBConformance':wwpIgmpSnoopMIBConformance,'wwpIgmpSnoopMIBCompliances':wwpIgmpSnoopMIBCompliances,'wwpIgmpSnoopMIBGroups':wwpIgmpSnoopMIBGroups})