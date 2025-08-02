_H='raisecomIpMcastStaticSAddressPrefix'
_G='raisecomIpMcastStaticSAddress'
_F='raisecomIpMcastStaticSAddressType'
_E='Integer32'
_D='not-accessible'
_C='RAISECOM-IPMCAST-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,InetAddressIPv6,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressIPv6','InetAddressType')
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
rcPortIndex,=mibBuilder.importSymbols('SWITCH-SYSTEM-MIB','rcPortIndex')
EnableVar,=mibBuilder.importSymbols('SWITCH-TC','EnableVar')
raisecomIpmcast=ModuleIdentity((1,3,6,1,4,1,8886,1,71))
if mibBuilder.loadTexts:raisecomIpmcast.setRevisions(('2012-01-05 00:00',))
_RaisecomIpmcastNotifications_ObjectIdentity=ObjectIdentity
raisecomIpmcastNotifications=_RaisecomIpmcastNotifications_ObjectIdentity((1,3,6,1,4,1,8886,1,71,1))
_RaisecomIpmcastObjects_ObjectIdentity=ObjectIdentity
raisecomIpmcastObjects=_RaisecomIpmcastObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,71,2))
_RaisecomIpMcastScalar_ObjectIdentity=ObjectIdentity
raisecomIpMcastScalar=_RaisecomIpMcastScalar_ObjectIdentity((1,3,6,1,4,1,8886,1,71,2,1))
_RaisecomIpMcastRouteLimit_Type=Integer32
_RaisecomIpMcastRouteLimit_Object=MibScalar
raisecomIpMcastRouteLimit=_RaisecomIpMcastRouteLimit_Object((1,3,6,1,4,1,8886,1,71,2,1,1),_RaisecomIpMcastRouteLimit_Type())
raisecomIpMcastRouteLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpMcastRouteLimit.setStatus(_A)
_RaisecomIpMcastOifLimitPerRoute_Type=Integer32
_RaisecomIpMcastOifLimitPerRoute_Object=MibScalar
raisecomIpMcastOifLimitPerRoute=_RaisecomIpMcastOifLimitPerRoute_Object((1,3,6,1,4,1,8886,1,71,2,1,2),_RaisecomIpMcastOifLimitPerRoute_Type())
raisecomIpMcastOifLimitPerRoute.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpMcastOifLimitPerRoute.setStatus(_A)
_RaisecomIpMcastStaticTable_Object=MibTable
raisecomIpMcastStaticTable=_RaisecomIpMcastStaticTable_Object((1,3,6,1,4,1,8886,1,71,2,2))
if mibBuilder.loadTexts:raisecomIpMcastStaticTable.setStatus(_A)
_RaisecomIpMcastStaticEntry_Object=MibTableRow
raisecomIpMcastStaticEntry=_RaisecomIpMcastStaticEntry_Object((1,3,6,1,4,1,8886,1,71,2,2,1))
raisecomIpMcastStaticEntry.setIndexNames((0,_C,_F),(0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:raisecomIpMcastStaticEntry.setStatus(_A)
_RaisecomIpMcastStaticSAddressType_Type=InetAddressType
_RaisecomIpMcastStaticSAddressType_Object=MibTableColumn
raisecomIpMcastStaticSAddressType=_RaisecomIpMcastStaticSAddressType_Object((1,3,6,1,4,1,8886,1,71,2,2,1,1),_RaisecomIpMcastStaticSAddressType_Type())
raisecomIpMcastStaticSAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomIpMcastStaticSAddressType.setStatus(_A)
_RaisecomIpMcastStaticSAddress_Type=InetAddress
_RaisecomIpMcastStaticSAddress_Object=MibTableColumn
raisecomIpMcastStaticSAddress=_RaisecomIpMcastStaticSAddress_Object((1,3,6,1,4,1,8886,1,71,2,2,1,2),_RaisecomIpMcastStaticSAddress_Type())
raisecomIpMcastStaticSAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomIpMcastStaticSAddress.setStatus(_A)
_RaisecomIpMcastStaticSAddressPrefix_Type=Integer32
_RaisecomIpMcastStaticSAddressPrefix_Object=MibTableColumn
raisecomIpMcastStaticSAddressPrefix=_RaisecomIpMcastStaticSAddressPrefix_Object((1,3,6,1,4,1,8886,1,71,2,2,1,3),_RaisecomIpMcastStaticSAddressPrefix_Type())
raisecomIpMcastStaticSAddressPrefix.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomIpMcastStaticSAddressPrefix.setStatus(_A)
_RaisecomIpMcastStaticNAddressType_Type=InetAddressType
_RaisecomIpMcastStaticNAddressType_Object=MibTableColumn
raisecomIpMcastStaticNAddressType=_RaisecomIpMcastStaticNAddressType_Object((1,3,6,1,4,1,8886,1,71,2,2,1,4),_RaisecomIpMcastStaticNAddressType_Type())
raisecomIpMcastStaticNAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpMcastStaticNAddressType.setStatus(_A)
_RaisecomIpMcastStaticNAddress_Type=InetAddress
_RaisecomIpMcastStaticNAddress_Object=MibTableColumn
raisecomIpMcastStaticNAddress=_RaisecomIpMcastStaticNAddress_Object((1,3,6,1,4,1,8886,1,71,2,2,1,5),_RaisecomIpMcastStaticNAddress_Type())
raisecomIpMcastStaticNAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpMcastStaticNAddress.setStatus(_A)
_RaisecomIpMcastStaticIfIndex_Type=InterfaceIndexOrZero
_RaisecomIpMcastStaticIfIndex_Object=MibTableColumn
raisecomIpMcastStaticIfIndex=_RaisecomIpMcastStaticIfIndex_Object((1,3,6,1,4,1,8886,1,71,2,2,1,6),_RaisecomIpMcastStaticIfIndex_Type())
raisecomIpMcastStaticIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpMcastStaticIfIndex.setStatus(_A)
class _RaisecomIpMcastStaticPreference_Type(Integer32):defaultValue=0
_RaisecomIpMcastStaticPreference_Type.__name__=_E
_RaisecomIpMcastStaticPreference_Object=MibTableColumn
raisecomIpMcastStaticPreference=_RaisecomIpMcastStaticPreference_Object((1,3,6,1,4,1,8886,1,71,2,2,1,7),_RaisecomIpMcastStaticPreference_Type())
raisecomIpMcastStaticPreference.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpMcastStaticPreference.setStatus(_A)
_RaisecomIpMcastStaticRowStatus_Type=RowStatus
_RaisecomIpMcastStaticRowStatus_Object=MibTableColumn
raisecomIpMcastStaticRowStatus=_RaisecomIpMcastStaticRowStatus_Object((1,3,6,1,4,1,8886,1,71,2,2,1,8),_RaisecomIpMcastStaticRowStatus_Type())
raisecomIpMcastStaticRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:raisecomIpMcastStaticRowStatus.setStatus(_A)
_RaisecomIpmcastConformance_ObjectIdentity=ObjectIdentity
raisecomIpmcastConformance=_RaisecomIpmcastConformance_ObjectIdentity((1,3,6,1,4,1,8886,1,71,3))
mibBuilder.exportSymbols(_C,**{'raisecomIpmcast':raisecomIpmcast,'raisecomIpmcastNotifications':raisecomIpmcastNotifications,'raisecomIpmcastObjects':raisecomIpmcastObjects,'raisecomIpMcastScalar':raisecomIpMcastScalar,'raisecomIpMcastRouteLimit':raisecomIpMcastRouteLimit,'raisecomIpMcastOifLimitPerRoute':raisecomIpMcastOifLimitPerRoute,'raisecomIpMcastStaticTable':raisecomIpMcastStaticTable,'raisecomIpMcastStaticEntry':raisecomIpMcastStaticEntry,_F:raisecomIpMcastStaticSAddressType,_G:raisecomIpMcastStaticSAddress,_H:raisecomIpMcastStaticSAddressPrefix,'raisecomIpMcastStaticNAddressType':raisecomIpMcastStaticNAddressType,'raisecomIpMcastStaticNAddress':raisecomIpMcastStaticNAddress,'raisecomIpMcastStaticIfIndex':raisecomIpMcastStaticIfIndex,'raisecomIpMcastStaticPreference':raisecomIpMcastStaticPreference,'raisecomIpMcastStaticRowStatus':raisecomIpMcastStaticRowStatus,'raisecomIpmcastConformance':raisecomIpmcastConformance})