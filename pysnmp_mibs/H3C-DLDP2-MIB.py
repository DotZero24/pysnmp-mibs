_N='not-accessible'
_M='h3cDldp2NeighborPortIndex'
_L='h3cDldp2NeighborBridgeMac'
_K='second'
_J='OctetString'
_I='H3C-DLDP2-MIB'
_H='ifDescr'
_G='read-only'
_F='unknown'
_E='read-write'
_D='ifIndex'
_C='Integer32'
_B='IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifDescr,ifIndex=mibBuilder.importSymbols(_B,_H,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
h3cDldp2=ModuleIdentity((1,3,6,1,4,1,2011,10,2,117))
if mibBuilder.loadTexts:h3cDldp2.setRevisions(('2011-12-26 15:30',))
_H3cDldp2ScalarGroup_ObjectIdentity=ObjectIdentity
h3cDldp2ScalarGroup=_H3cDldp2ScalarGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,117,1))
_H3cDldp2GlobalEnable_Type=TruthValue
_H3cDldp2GlobalEnable_Object=MibScalar
h3cDldp2GlobalEnable=_H3cDldp2GlobalEnable_Object((1,3,6,1,4,1,2011,10,2,117,1,1),_H3cDldp2GlobalEnable_Type())
h3cDldp2GlobalEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDldp2GlobalEnable.setStatus(_A)
class _H3cDldp2Interval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_H3cDldp2Interval_Type.__name__=_C
_H3cDldp2Interval_Object=MibScalar
h3cDldp2Interval=_H3cDldp2Interval_Object((1,3,6,1,4,1,2011,10,2,117,1,2),_H3cDldp2Interval_Type())
h3cDldp2Interval.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDldp2Interval.setStatus(_A)
if mibBuilder.loadTexts:h3cDldp2Interval.setUnits(_K)
class _H3cDldp2AuthMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('none',2),('simple',3),('md5',4)))
_H3cDldp2AuthMode_Type.__name__=_C
_H3cDldp2AuthMode_Object=MibScalar
h3cDldp2AuthMode=_H3cDldp2AuthMode_Object((1,3,6,1,4,1,2011,10,2,117,1,3),_H3cDldp2AuthMode_Type())
h3cDldp2AuthMode.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDldp2AuthMode.setStatus(_A)
class _H3cDldp2AuthPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_H3cDldp2AuthPassword_Type.__name__=_J
_H3cDldp2AuthPassword_Object=MibScalar
h3cDldp2AuthPassword=_H3cDldp2AuthPassword_Object((1,3,6,1,4,1,2011,10,2,117,1,4),_H3cDldp2AuthPassword_Type())
h3cDldp2AuthPassword.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDldp2AuthPassword.setStatus(_A)
class _H3cDldp2UniShutdown_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('auto',2),('manual',3)))
_H3cDldp2UniShutdown_Type.__name__=_C
_H3cDldp2UniShutdown_Object=MibScalar
h3cDldp2UniShutdown=_H3cDldp2UniShutdown_Object((1,3,6,1,4,1,2011,10,2,117,1,5),_H3cDldp2UniShutdown_Type())
h3cDldp2UniShutdown.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDldp2UniShutdown.setStatus(_A)
_H3cDldp2TableGroup_ObjectIdentity=ObjectIdentity
h3cDldp2TableGroup=_H3cDldp2TableGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,117,2))
_H3cDldp2PortConfigTable_Object=MibTable
h3cDldp2PortConfigTable=_H3cDldp2PortConfigTable_Object((1,3,6,1,4,1,2011,10,2,117,2,1))
if mibBuilder.loadTexts:h3cDldp2PortConfigTable.setStatus(_A)
_H3cDldp2PortConfigEntry_Object=MibTableRow
h3cDldp2PortConfigEntry=_H3cDldp2PortConfigEntry_Object((1,3,6,1,4,1,2011,10,2,117,2,1,1))
h3cDldp2PortConfigEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:h3cDldp2PortConfigEntry.setStatus(_A)
_H3cDldp2PortEnable_Type=TruthValue
_H3cDldp2PortEnable_Object=MibTableColumn
h3cDldp2PortEnable=_H3cDldp2PortEnable_Object((1,3,6,1,4,1,2011,10,2,117,2,1,1,1),_H3cDldp2PortEnable_Type())
h3cDldp2PortEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDldp2PortEnable.setStatus(_A)
_H3cDldp2PortStatusTable_Object=MibTable
h3cDldp2PortStatusTable=_H3cDldp2PortStatusTable_Object((1,3,6,1,4,1,2011,10,2,117,2,2))
if mibBuilder.loadTexts:h3cDldp2PortStatusTable.setStatus(_A)
_H3cDldp2PortStatusEntry_Object=MibTableRow
h3cDldp2PortStatusEntry=_H3cDldp2PortStatusEntry_Object((1,3,6,1,4,1,2011,10,2,117,2,2,1))
h3cDldp2PortStatusEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:h3cDldp2PortStatusEntry.setStatus(_A)
class _H3cDldp2PortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('initial',2),('inactive',3),('unidirectional',4),('bidirectional',5)))
_H3cDldp2PortOperStatus_Type.__name__=_C
_H3cDldp2PortOperStatus_Object=MibTableColumn
h3cDldp2PortOperStatus=_H3cDldp2PortOperStatus_Object((1,3,6,1,4,1,2011,10,2,117,2,2,1,1),_H3cDldp2PortOperStatus_Type())
h3cDldp2PortOperStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDldp2PortOperStatus.setStatus(_A)
class _H3cDldp2PortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('down',2),('up',3)))
_H3cDldp2PortLinkStatus_Type.__name__=_C
_H3cDldp2PortLinkStatus_Object=MibTableColumn
h3cDldp2PortLinkStatus=_H3cDldp2PortLinkStatus_Object((1,3,6,1,4,1,2011,10,2,117,2,2,1,2),_H3cDldp2PortLinkStatus_Type())
h3cDldp2PortLinkStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDldp2PortLinkStatus.setStatus(_A)
_H3cDldp2NeighborTable_Object=MibTable
h3cDldp2NeighborTable=_H3cDldp2NeighborTable_Object((1,3,6,1,4,1,2011,10,2,117,2,3))
if mibBuilder.loadTexts:h3cDldp2NeighborTable.setStatus(_A)
_H3cDldp2NeighborEntry_Object=MibTableRow
h3cDldp2NeighborEntry=_H3cDldp2NeighborEntry_Object((1,3,6,1,4,1,2011,10,2,117,2,3,1))
h3cDldp2NeighborEntry.setIndexNames((0,_B,_D),(0,_I,_L),(0,_I,_M))
if mibBuilder.loadTexts:h3cDldp2NeighborEntry.setStatus(_A)
_H3cDldp2NeighborBridgeMac_Type=MacAddress
_H3cDldp2NeighborBridgeMac_Object=MibTableColumn
h3cDldp2NeighborBridgeMac=_H3cDldp2NeighborBridgeMac_Object((1,3,6,1,4,1,2011,10,2,117,2,3,1,1),_H3cDldp2NeighborBridgeMac_Type())
h3cDldp2NeighborBridgeMac.setMaxAccess(_N)
if mibBuilder.loadTexts:h3cDldp2NeighborBridgeMac.setStatus(_A)
class _H3cDldp2NeighborPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cDldp2NeighborPortIndex_Type.__name__=_C
_H3cDldp2NeighborPortIndex_Object=MibTableColumn
h3cDldp2NeighborPortIndex=_H3cDldp2NeighborPortIndex_Object((1,3,6,1,4,1,2011,10,2,117,2,3,1,2),_H3cDldp2NeighborPortIndex_Type())
h3cDldp2NeighborPortIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:h3cDldp2NeighborPortIndex.setStatus(_A)
class _H3cDldp2NeighborStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('unconfirmed',2),('confirmed',3)))
_H3cDldp2NeighborStatus_Type.__name__=_C
_H3cDldp2NeighborStatus_Object=MibTableColumn
h3cDldp2NeighborStatus=_H3cDldp2NeighborStatus_Object((1,3,6,1,4,1,2011,10,2,117,2,3,1,3),_H3cDldp2NeighborStatus_Type())
h3cDldp2NeighborStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDldp2NeighborStatus.setStatus(_A)
_H3cDldp2NeighborAgingTime_Type=Integer32
_H3cDldp2NeighborAgingTime_Object=MibTableColumn
h3cDldp2NeighborAgingTime=_H3cDldp2NeighborAgingTime_Object((1,3,6,1,4,1,2011,10,2,117,2,3,1,4),_H3cDldp2NeighborAgingTime_Type())
h3cDldp2NeighborAgingTime.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDldp2NeighborAgingTime.setStatus(_A)
if mibBuilder.loadTexts:h3cDldp2NeighborAgingTime.setUnits(_K)
_H3cDldp2TrapBindObjects_ObjectIdentity=ObjectIdentity
h3cDldp2TrapBindObjects=_H3cDldp2TrapBindObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,117,3))
_H3cDldp2Trap_ObjectIdentity=ObjectIdentity
h3cDldp2Trap=_H3cDldp2Trap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,117,4))
_H3cDldp2TrapPrefix_ObjectIdentity=ObjectIdentity
h3cDldp2TrapPrefix=_H3cDldp2TrapPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,117,4,0))
h3cDldp2TrapUniLink=NotificationType((1,3,6,1,4,1,2011,10,2,117,4,0,1))
h3cDldp2TrapUniLink.setObjects(*((_B,_D),(_B,_H)))
if mibBuilder.loadTexts:h3cDldp2TrapUniLink.setStatus(_A)
h3cDldp2TrapBidLink=NotificationType((1,3,6,1,4,1,2011,10,2,117,4,0,2))
h3cDldp2TrapBidLink.setObjects(*((_B,_D),(_B,_H)))
if mibBuilder.loadTexts:h3cDldp2TrapBidLink.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'h3cDldp2':h3cDldp2,'h3cDldp2ScalarGroup':h3cDldp2ScalarGroup,'h3cDldp2GlobalEnable':h3cDldp2GlobalEnable,'h3cDldp2Interval':h3cDldp2Interval,'h3cDldp2AuthMode':h3cDldp2AuthMode,'h3cDldp2AuthPassword':h3cDldp2AuthPassword,'h3cDldp2UniShutdown':h3cDldp2UniShutdown,'h3cDldp2TableGroup':h3cDldp2TableGroup,'h3cDldp2PortConfigTable':h3cDldp2PortConfigTable,'h3cDldp2PortConfigEntry':h3cDldp2PortConfigEntry,'h3cDldp2PortEnable':h3cDldp2PortEnable,'h3cDldp2PortStatusTable':h3cDldp2PortStatusTable,'h3cDldp2PortStatusEntry':h3cDldp2PortStatusEntry,'h3cDldp2PortOperStatus':h3cDldp2PortOperStatus,'h3cDldp2PortLinkStatus':h3cDldp2PortLinkStatus,'h3cDldp2NeighborTable':h3cDldp2NeighborTable,'h3cDldp2NeighborEntry':h3cDldp2NeighborEntry,_L:h3cDldp2NeighborBridgeMac,_M:h3cDldp2NeighborPortIndex,'h3cDldp2NeighborStatus':h3cDldp2NeighborStatus,'h3cDldp2NeighborAgingTime':h3cDldp2NeighborAgingTime,'h3cDldp2TrapBindObjects':h3cDldp2TrapBindObjects,'h3cDldp2Trap':h3cDldp2Trap,'h3cDldp2TrapPrefix':h3cDldp2TrapPrefix,'h3cDldp2TrapUniLink':h3cDldp2TrapUniLink,'h3cDldp2TrapBidLink':h3cDldp2TrapBidLink})