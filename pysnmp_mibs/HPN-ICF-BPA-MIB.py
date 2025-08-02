_K='hpnicfBpaTrafficIndex'
_J='hpnicfBpaTrafficType'
_I='read-create'
_H='hpnicfBpaDirection'
_G='not-accessible'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='HPN-ICF-BPA-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_E,_F)
InetAddressType,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfBpa=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,144))
if mibBuilder.loadTexts:hpnicfBpa.setRevisions(('2013-11-13 11:28',))
_HpnicfBpaObjects_ObjectIdentity=ObjectIdentity
hpnicfBpaObjects=_HpnicfBpaObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,144,1))
_HpnicfBpaCfgTable_Object=MibTable
hpnicfBpaCfgTable=_HpnicfBpaCfgTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,144,1,1))
if mibBuilder.loadTexts:hpnicfBpaCfgTable.setStatus(_A)
_HpnicfBpaCfgEntry_Object=MibTableRow
hpnicfBpaCfgEntry=_HpnicfBpaCfgEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,144,1,1,1))
hpnicfBpaCfgEntry.setIndexNames((0,_E,_F),(0,_C,_H))
if mibBuilder.loadTexts:hpnicfBpaCfgEntry.setStatus(_A)
class _HpnicfBpaDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('input',1),('output',2)))
_HpnicfBpaDirection_Type.__name__=_B
_HpnicfBpaDirection_Object=MibTableColumn
hpnicfBpaDirection=_HpnicfBpaDirection_Object((1,3,6,1,4,1,11,2,14,11,15,2,144,1,1,1,1),_HpnicfBpaDirection_Type())
hpnicfBpaDirection.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfBpaDirection.setStatus(_A)
class _HpnicfBpaSrcOrDest_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('source',1),('destination',2),('both',3)))
_HpnicfBpaSrcOrDest_Type.__name__=_B
_HpnicfBpaSrcOrDest_Object=MibTableColumn
hpnicfBpaSrcOrDest=_HpnicfBpaSrcOrDest_Object((1,3,6,1,4,1,11,2,14,11,15,2,144,1,1,1,2),_HpnicfBpaSrcOrDest_Type())
hpnicfBpaSrcOrDest.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfBpaSrcOrDest.setStatus(_A)
_HpnicfBpaRowStatus_Type=RowStatus
_HpnicfBpaRowStatus_Object=MibTableColumn
hpnicfBpaRowStatus=_HpnicfBpaRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,144,1,1,1,3),_HpnicfBpaRowStatus_Type())
hpnicfBpaRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfBpaRowStatus.setStatus(_A)
_HpnicfBpaStatTable_Object=MibTable
hpnicfBpaStatTable=_HpnicfBpaStatTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,144,1,2))
if mibBuilder.loadTexts:hpnicfBpaStatTable.setStatus(_A)
_HpnicfBpaStatEntry_Object=MibTableRow
hpnicfBpaStatEntry=_HpnicfBpaStatEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,144,1,2,1))
hpnicfBpaStatEntry.setIndexNames((0,_E,_F),(0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:hpnicfBpaStatEntry.setStatus(_A)
_HpnicfBpaTrafficType_Type=InetAddressType
_HpnicfBpaTrafficType_Object=MibTableColumn
hpnicfBpaTrafficType=_HpnicfBpaTrafficType_Object((1,3,6,1,4,1,11,2,14,11,15,2,144,1,2,1,1),_HpnicfBpaTrafficType_Type())
hpnicfBpaTrafficType.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfBpaTrafficType.setStatus(_A)
class _HpnicfBpaTrafficIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpnicfBpaTrafficIndex_Type.__name__=_B
_HpnicfBpaTrafficIndex_Object=MibTableColumn
hpnicfBpaTrafficIndex=_HpnicfBpaTrafficIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,144,1,2,1,2),_HpnicfBpaTrafficIndex_Type())
hpnicfBpaTrafficIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfBpaTrafficIndex.setStatus(_A)
_HpnicfBpaInPacketCount_Type=Counter64
_HpnicfBpaInPacketCount_Object=MibTableColumn
hpnicfBpaInPacketCount=_HpnicfBpaInPacketCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,144,1,2,1,3),_HpnicfBpaInPacketCount_Type())
hpnicfBpaInPacketCount.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfBpaInPacketCount.setStatus(_A)
_HpnicfBpaInOctetCount_Type=Counter64
_HpnicfBpaInOctetCount_Object=MibTableColumn
hpnicfBpaInOctetCount=_HpnicfBpaInOctetCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,144,1,2,1,4),_HpnicfBpaInOctetCount_Type())
hpnicfBpaInOctetCount.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfBpaInOctetCount.setStatus(_A)
_HpnicfBpaOutPacketCount_Type=Counter64
_HpnicfBpaOutPacketCount_Object=MibTableColumn
hpnicfBpaOutPacketCount=_HpnicfBpaOutPacketCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,144,1,2,1,5),_HpnicfBpaOutPacketCount_Type())
hpnicfBpaOutPacketCount.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfBpaOutPacketCount.setStatus(_A)
_HpnicfBpaOutOctetCount_Type=Counter64
_HpnicfBpaOutOctetCount_Object=MibTableColumn
hpnicfBpaOutOctetCount=_HpnicfBpaOutOctetCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,144,1,2,1,6),_HpnicfBpaOutOctetCount_Type())
hpnicfBpaOutOctetCount.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfBpaOutOctetCount.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'hpnicfBpa':hpnicfBpa,'hpnicfBpaObjects':hpnicfBpaObjects,'hpnicfBpaCfgTable':hpnicfBpaCfgTable,'hpnicfBpaCfgEntry':hpnicfBpaCfgEntry,_H:hpnicfBpaDirection,'hpnicfBpaSrcOrDest':hpnicfBpaSrcOrDest,'hpnicfBpaRowStatus':hpnicfBpaRowStatus,'hpnicfBpaStatTable':hpnicfBpaStatTable,'hpnicfBpaStatEntry':hpnicfBpaStatEntry,_J:hpnicfBpaTrafficType,_K:hpnicfBpaTrafficIndex,'hpnicfBpaInPacketCount':hpnicfBpaInPacketCount,'hpnicfBpaInOctetCount':hpnicfBpaInOctetCount,'hpnicfBpaOutPacketCount':hpnicfBpaOutPacketCount,'hpnicfBpaOutOctetCount':hpnicfBpaOutOctetCount})