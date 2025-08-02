_N='not-accessible'
_M='hpnicfDldp2NeighborPortIndex'
_L='hpnicfDldp2NeighborBridgeMac'
_K='second'
_J='OctetString'
_I='HPN-ICF-DLDP2-MIB'
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
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifDescr,ifIndex=mibBuilder.importSymbols(_B,_H,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
hpnicfDldp2=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,117))
if mibBuilder.loadTexts:hpnicfDldp2.setRevisions(('2011-12-26 15:30',))
_HpnicfDldp2ScalarGroup_ObjectIdentity=ObjectIdentity
hpnicfDldp2ScalarGroup=_HpnicfDldp2ScalarGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,117,1))
_HpnicfDldp2GlobalEnable_Type=TruthValue
_HpnicfDldp2GlobalEnable_Object=MibScalar
hpnicfDldp2GlobalEnable=_HpnicfDldp2GlobalEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,117,1,1),_HpnicfDldp2GlobalEnable_Type())
hpnicfDldp2GlobalEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDldp2GlobalEnable.setStatus(_A)
class _HpnicfDldp2Interval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpnicfDldp2Interval_Type.__name__=_C
_HpnicfDldp2Interval_Object=MibScalar
hpnicfDldp2Interval=_HpnicfDldp2Interval_Object((1,3,6,1,4,1,11,2,14,11,15,2,117,1,2),_HpnicfDldp2Interval_Type())
hpnicfDldp2Interval.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDldp2Interval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDldp2Interval.setUnits(_K)
class _HpnicfDldp2AuthMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('none',2),('simple',3),('md5',4)))
_HpnicfDldp2AuthMode_Type.__name__=_C
_HpnicfDldp2AuthMode_Object=MibScalar
hpnicfDldp2AuthMode=_HpnicfDldp2AuthMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,117,1,3),_HpnicfDldp2AuthMode_Type())
hpnicfDldp2AuthMode.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDldp2AuthMode.setStatus(_A)
class _HpnicfDldp2AuthPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_HpnicfDldp2AuthPassword_Type.__name__=_J
_HpnicfDldp2AuthPassword_Object=MibScalar
hpnicfDldp2AuthPassword=_HpnicfDldp2AuthPassword_Object((1,3,6,1,4,1,11,2,14,11,15,2,117,1,4),_HpnicfDldp2AuthPassword_Type())
hpnicfDldp2AuthPassword.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDldp2AuthPassword.setStatus(_A)
class _HpnicfDldp2UniShutdown_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('auto',2),('manual',3)))
_HpnicfDldp2UniShutdown_Type.__name__=_C
_HpnicfDldp2UniShutdown_Object=MibScalar
hpnicfDldp2UniShutdown=_HpnicfDldp2UniShutdown_Object((1,3,6,1,4,1,11,2,14,11,15,2,117,1,5),_HpnicfDldp2UniShutdown_Type())
hpnicfDldp2UniShutdown.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDldp2UniShutdown.setStatus(_A)
_HpnicfDldp2TableGroup_ObjectIdentity=ObjectIdentity
hpnicfDldp2TableGroup=_HpnicfDldp2TableGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,117,2))
_HpnicfDldp2PortConfigTable_Object=MibTable
hpnicfDldp2PortConfigTable=_HpnicfDldp2PortConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,117,2,1))
if mibBuilder.loadTexts:hpnicfDldp2PortConfigTable.setStatus(_A)
_HpnicfDldp2PortConfigEntry_Object=MibTableRow
hpnicfDldp2PortConfigEntry=_HpnicfDldp2PortConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,117,2,1,1))
hpnicfDldp2PortConfigEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:hpnicfDldp2PortConfigEntry.setStatus(_A)
_HpnicfDldp2PortEnable_Type=TruthValue
_HpnicfDldp2PortEnable_Object=MibTableColumn
hpnicfDldp2PortEnable=_HpnicfDldp2PortEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,117,2,1,1,1),_HpnicfDldp2PortEnable_Type())
hpnicfDldp2PortEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDldp2PortEnable.setStatus(_A)
_HpnicfDldp2PortStatusTable_Object=MibTable
hpnicfDldp2PortStatusTable=_HpnicfDldp2PortStatusTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,117,2,2))
if mibBuilder.loadTexts:hpnicfDldp2PortStatusTable.setStatus(_A)
_HpnicfDldp2PortStatusEntry_Object=MibTableRow
hpnicfDldp2PortStatusEntry=_HpnicfDldp2PortStatusEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,117,2,2,1))
hpnicfDldp2PortStatusEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:hpnicfDldp2PortStatusEntry.setStatus(_A)
class _HpnicfDldp2PortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('initial',2),('inactive',3),('unidirectional',4),('bidirectional',5)))
_HpnicfDldp2PortOperStatus_Type.__name__=_C
_HpnicfDldp2PortOperStatus_Object=MibTableColumn
hpnicfDldp2PortOperStatus=_HpnicfDldp2PortOperStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,117,2,2,1,1),_HpnicfDldp2PortOperStatus_Type())
hpnicfDldp2PortOperStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDldp2PortOperStatus.setStatus(_A)
class _HpnicfDldp2PortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('down',2),('up',3)))
_HpnicfDldp2PortLinkStatus_Type.__name__=_C
_HpnicfDldp2PortLinkStatus_Object=MibTableColumn
hpnicfDldp2PortLinkStatus=_HpnicfDldp2PortLinkStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,117,2,2,1,2),_HpnicfDldp2PortLinkStatus_Type())
hpnicfDldp2PortLinkStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDldp2PortLinkStatus.setStatus(_A)
_HpnicfDldp2NeighborTable_Object=MibTable
hpnicfDldp2NeighborTable=_HpnicfDldp2NeighborTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,117,2,3))
if mibBuilder.loadTexts:hpnicfDldp2NeighborTable.setStatus(_A)
_HpnicfDldp2NeighborEntry_Object=MibTableRow
hpnicfDldp2NeighborEntry=_HpnicfDldp2NeighborEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,117,2,3,1))
hpnicfDldp2NeighborEntry.setIndexNames((0,_B,_D),(0,_I,_L),(0,_I,_M))
if mibBuilder.loadTexts:hpnicfDldp2NeighborEntry.setStatus(_A)
_HpnicfDldp2NeighborBridgeMac_Type=MacAddress
_HpnicfDldp2NeighborBridgeMac_Object=MibTableColumn
hpnicfDldp2NeighborBridgeMac=_HpnicfDldp2NeighborBridgeMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,117,2,3,1,1),_HpnicfDldp2NeighborBridgeMac_Type())
hpnicfDldp2NeighborBridgeMac.setMaxAccess(_N)
if mibBuilder.loadTexts:hpnicfDldp2NeighborBridgeMac.setStatus(_A)
class _HpnicfDldp2NeighborPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfDldp2NeighborPortIndex_Type.__name__=_C
_HpnicfDldp2NeighborPortIndex_Object=MibTableColumn
hpnicfDldp2NeighborPortIndex=_HpnicfDldp2NeighborPortIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,117,2,3,1,2),_HpnicfDldp2NeighborPortIndex_Type())
hpnicfDldp2NeighborPortIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:hpnicfDldp2NeighborPortIndex.setStatus(_A)
class _HpnicfDldp2NeighborStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('unconfirmed',2),('confirmed',3)))
_HpnicfDldp2NeighborStatus_Type.__name__=_C
_HpnicfDldp2NeighborStatus_Object=MibTableColumn
hpnicfDldp2NeighborStatus=_HpnicfDldp2NeighborStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,117,2,3,1,3),_HpnicfDldp2NeighborStatus_Type())
hpnicfDldp2NeighborStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDldp2NeighborStatus.setStatus(_A)
_HpnicfDldp2NeighborAgingTime_Type=Integer32
_HpnicfDldp2NeighborAgingTime_Object=MibTableColumn
hpnicfDldp2NeighborAgingTime=_HpnicfDldp2NeighborAgingTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,117,2,3,1,4),_HpnicfDldp2NeighborAgingTime_Type())
hpnicfDldp2NeighborAgingTime.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDldp2NeighborAgingTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDldp2NeighborAgingTime.setUnits(_K)
_HpnicfDldp2TrapBindObjects_ObjectIdentity=ObjectIdentity
hpnicfDldp2TrapBindObjects=_HpnicfDldp2TrapBindObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,117,3))
_HpnicfDldp2Trap_ObjectIdentity=ObjectIdentity
hpnicfDldp2Trap=_HpnicfDldp2Trap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,117,4))
_HpnicfDldp2TrapPrefix_ObjectIdentity=ObjectIdentity
hpnicfDldp2TrapPrefix=_HpnicfDldp2TrapPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,117,4,0))
hpnicfDldp2TrapUniLink=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,117,4,0,1))
hpnicfDldp2TrapUniLink.setObjects(*((_B,_D),(_B,_H)))
if mibBuilder.loadTexts:hpnicfDldp2TrapUniLink.setStatus(_A)
hpnicfDldp2TrapBidLink=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,117,4,0,2))
hpnicfDldp2TrapBidLink.setObjects(*((_B,_D),(_B,_H)))
if mibBuilder.loadTexts:hpnicfDldp2TrapBidLink.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'hpnicfDldp2':hpnicfDldp2,'hpnicfDldp2ScalarGroup':hpnicfDldp2ScalarGroup,'hpnicfDldp2GlobalEnable':hpnicfDldp2GlobalEnable,'hpnicfDldp2Interval':hpnicfDldp2Interval,'hpnicfDldp2AuthMode':hpnicfDldp2AuthMode,'hpnicfDldp2AuthPassword':hpnicfDldp2AuthPassword,'hpnicfDldp2UniShutdown':hpnicfDldp2UniShutdown,'hpnicfDldp2TableGroup':hpnicfDldp2TableGroup,'hpnicfDldp2PortConfigTable':hpnicfDldp2PortConfigTable,'hpnicfDldp2PortConfigEntry':hpnicfDldp2PortConfigEntry,'hpnicfDldp2PortEnable':hpnicfDldp2PortEnable,'hpnicfDldp2PortStatusTable':hpnicfDldp2PortStatusTable,'hpnicfDldp2PortStatusEntry':hpnicfDldp2PortStatusEntry,'hpnicfDldp2PortOperStatus':hpnicfDldp2PortOperStatus,'hpnicfDldp2PortLinkStatus':hpnicfDldp2PortLinkStatus,'hpnicfDldp2NeighborTable':hpnicfDldp2NeighborTable,'hpnicfDldp2NeighborEntry':hpnicfDldp2NeighborEntry,_L:hpnicfDldp2NeighborBridgeMac,_M:hpnicfDldp2NeighborPortIndex,'hpnicfDldp2NeighborStatus':hpnicfDldp2NeighborStatus,'hpnicfDldp2NeighborAgingTime':hpnicfDldp2NeighborAgingTime,'hpnicfDldp2TrapBindObjects':hpnicfDldp2TrapBindObjects,'hpnicfDldp2Trap':hpnicfDldp2Trap,'hpnicfDldp2TrapPrefix':hpnicfDldp2TrapPrefix,'hpnicfDldp2TrapUniLink':hpnicfDldp2TrapUniLink,'hpnicfDldp2TrapBidLink':hpnicfDldp2TrapBidLink})