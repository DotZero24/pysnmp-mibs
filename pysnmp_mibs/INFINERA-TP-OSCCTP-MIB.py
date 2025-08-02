_V='oscCtpGroup'
_U='oscCtpPmHistStatsEnable'
_T='oscCtpOspfRoutingEnabled'
_S='oscCtpOspfInstanceId'
_R='oscCtpOspfDeadInterval'
_Q='oscCtpOspfArea'
_P='oscCtpOspfHelloInterval'
_O='oscCtpTECost'
_N='oscCtpOspfCost'
_M='oscCtpOscNetmask'
_L='oscCtpOscIpAddress'
_K='oscCtpOscIpAddressType'
_J='read-only'
_I='seconds'
_H='TruthValue'
_G='ifIndex'
_F='IF-MIB'
_E='Integer32'
_D='obsolete'
_C='current'
_B='read-write'
_A='INFINERA-TP-OSCCTP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
InfnAdminState,=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnAdminState')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_H)
oscCtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,13))
if mibBuilder.loadTexts:oscCtpMIB.setRevisions(('2008-10-20 00:00',))
_OscCtpTable_Object=MibTable
oscCtpTable=_OscCtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,13,1))
if mibBuilder.loadTexts:oscCtpTable.setStatus(_C)
_OscCtpEntry_Object=MibTableRow
oscCtpEntry=_OscCtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,13,1,1))
oscCtpEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:oscCtpEntry.setStatus(_C)
_OscCtpOscIpAddressType_Type=InetAddressType
_OscCtpOscIpAddressType_Object=MibTableColumn
oscCtpOscIpAddressType=_OscCtpOscIpAddressType_Object((1,3,6,1,4,1,21296,2,2,2,2,13,1,1,1),_OscCtpOscIpAddressType_Type())
oscCtpOscIpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:oscCtpOscIpAddressType.setStatus(_C)
_OscCtpOscIpAddress_Type=InetAddress
_OscCtpOscIpAddress_Object=MibTableColumn
oscCtpOscIpAddress=_OscCtpOscIpAddress_Object((1,3,6,1,4,1,21296,2,2,2,2,13,1,1,2),_OscCtpOscIpAddress_Type())
oscCtpOscIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oscCtpOscIpAddress.setStatus(_C)
_OscCtpOscNetmask_Type=InetAddress
_OscCtpOscNetmask_Object=MibTableColumn
oscCtpOscNetmask=_OscCtpOscNetmask_Object((1,3,6,1,4,1,21296,2,2,2,2,13,1,1,3),_OscCtpOscNetmask_Type())
oscCtpOscNetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:oscCtpOscNetmask.setStatus(_C)
_OscCtpOscIpIfAdminState_Type=InfnAdminState
_OscCtpOscIpIfAdminState_Object=MibTableColumn
oscCtpOscIpIfAdminState=_OscCtpOscIpIfAdminState_Object((1,3,6,1,4,1,21296,2,2,2,2,13,1,1,4),_OscCtpOscIpIfAdminState_Type())
oscCtpOscIpIfAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:oscCtpOscIpIfAdminState.setStatus(_C)
class _OscCtpOspfCost_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OscCtpOspfCost_Type.__name__=_E
_OscCtpOspfCost_Object=MibTableColumn
oscCtpOspfCost=_OscCtpOspfCost_Object((1,3,6,1,4,1,21296,2,2,2,2,13,1,1,5),_OscCtpOspfCost_Type())
oscCtpOspfCost.setMaxAccess(_B)
if mibBuilder.loadTexts:oscCtpOspfCost.setStatus(_D)
class _OscCtpTECost_Type(Integer32):defaultValue=100
_OscCtpTECost_Type.__name__=_E
_OscCtpTECost_Object=MibTableColumn
oscCtpTECost=_OscCtpTECost_Object((1,3,6,1,4,1,21296,2,2,2,2,13,1,1,6),_OscCtpTECost_Type())
oscCtpTECost.setMaxAccess(_B)
if mibBuilder.loadTexts:oscCtpTECost.setStatus(_D)
class _OscCtpOspfHelloInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1200))
_OscCtpOspfHelloInterval_Type.__name__=_E
_OscCtpOspfHelloInterval_Object=MibTableColumn
oscCtpOspfHelloInterval=_OscCtpOspfHelloInterval_Object((1,3,6,1,4,1,21296,2,2,2,2,13,1,1,7),_OscCtpOspfHelloInterval_Type())
oscCtpOspfHelloInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:oscCtpOspfHelloInterval.setStatus(_D)
if mibBuilder.loadTexts:oscCtpOspfHelloInterval.setUnits(_I)
_OscCtpOspfArea_Type=InetAddress
_OscCtpOspfArea_Object=MibTableColumn
oscCtpOspfArea=_OscCtpOspfArea_Object((1,3,6,1,4,1,21296,2,2,2,2,13,1,1,8),_OscCtpOspfArea_Type())
oscCtpOspfArea.setMaxAccess(_J)
if mibBuilder.loadTexts:oscCtpOspfArea.setStatus(_D)
class _OscCtpOspfDeadInterval_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3600))
_OscCtpOspfDeadInterval_Type.__name__=_E
_OscCtpOspfDeadInterval_Object=MibTableColumn
oscCtpOspfDeadInterval=_OscCtpOspfDeadInterval_Object((1,3,6,1,4,1,21296,2,2,2,2,13,1,1,9),_OscCtpOspfDeadInterval_Type())
oscCtpOspfDeadInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:oscCtpOspfDeadInterval.setStatus(_D)
if mibBuilder.loadTexts:oscCtpOspfDeadInterval.setUnits(_I)
_OscCtpOspfInstanceId_Type=Integer32
_OscCtpOspfInstanceId_Object=MibTableColumn
oscCtpOspfInstanceId=_OscCtpOspfInstanceId_Object((1,3,6,1,4,1,21296,2,2,2,2,13,1,1,10),_OscCtpOspfInstanceId_Type())
oscCtpOspfInstanceId.setMaxAccess(_J)
if mibBuilder.loadTexts:oscCtpOspfInstanceId.setStatus(_D)
class _OscCtpOspfRoutingEnabled_Type(TruthValue):defaultValue=2
_OscCtpOspfRoutingEnabled_Type.__name__=_H
_OscCtpOspfRoutingEnabled_Object=MibTableColumn
oscCtpOspfRoutingEnabled=_OscCtpOspfRoutingEnabled_Object((1,3,6,1,4,1,21296,2,2,2,2,13,1,1,11),_OscCtpOspfRoutingEnabled_Type())
oscCtpOspfRoutingEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:oscCtpOspfRoutingEnabled.setStatus(_D)
class _OscCtpPmHistStatsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_OscCtpPmHistStatsEnable_Type.__name__=_E
_OscCtpPmHistStatsEnable_Object=MibTableColumn
oscCtpPmHistStatsEnable=_OscCtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,13,1,1,12),_OscCtpPmHistStatsEnable_Type())
oscCtpPmHistStatsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:oscCtpPmHistStatsEnable.setStatus(_C)
_OscCtpConformance_ObjectIdentity=ObjectIdentity
oscCtpConformance=_OscCtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,13,3))
_OscCtpCompliances_ObjectIdentity=ObjectIdentity
oscCtpCompliances=_OscCtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,13,3,1))
_OscCtpGroups_ObjectIdentity=ObjectIdentity
oscCtpGroups=_OscCtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,13,3,2))
oscCtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,13,3,2,1))
oscCtpGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:oscCtpGroup.setStatus(_C)
oscCtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,13,3,1,1))
oscCtpCompliance.setObjects((_A,_V))
if mibBuilder.loadTexts:oscCtpCompliance.setStatus(_C)
mibBuilder.exportSymbols(_A,**{'oscCtpMIB':oscCtpMIB,'oscCtpTable':oscCtpTable,'oscCtpEntry':oscCtpEntry,_K:oscCtpOscIpAddressType,_L:oscCtpOscIpAddress,_M:oscCtpOscNetmask,'oscCtpOscIpIfAdminState':oscCtpOscIpIfAdminState,_N:oscCtpOspfCost,_O:oscCtpTECost,_P:oscCtpOspfHelloInterval,_Q:oscCtpOspfArea,_R:oscCtpOspfDeadInterval,_S:oscCtpOspfInstanceId,_T:oscCtpOspfRoutingEnabled,_U:oscCtpPmHistStatsEnable,'oscCtpConformance':oscCtpConformance,'oscCtpCompliances':oscCtpCompliances,'oscCtpCompliance':oscCtpCompliance,'oscCtpGroups':oscCtpGroups,_V:oscCtpGroup})