_K='h3cBpaTrafficIndex'
_J='h3cBpaTrafficType'
_I='read-create'
_H='h3cBpaDirection'
_G='not-accessible'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='H3C-BPA-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_E,_F)
InetAddressType,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cBpa=ModuleIdentity((1,3,6,1,4,1,2011,10,2,144))
if mibBuilder.loadTexts:h3cBpa.setRevisions(('2014-11-20 09:27','2013-11-13 11:28'))
_H3cBpaObjects_ObjectIdentity=ObjectIdentity
h3cBpaObjects=_H3cBpaObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,144,1))
_H3cBpaCfgTable_Object=MibTable
h3cBpaCfgTable=_H3cBpaCfgTable_Object((1,3,6,1,4,1,2011,10,2,144,1,1))
if mibBuilder.loadTexts:h3cBpaCfgTable.setStatus(_A)
_H3cBpaCfgEntry_Object=MibTableRow
h3cBpaCfgEntry=_H3cBpaCfgEntry_Object((1,3,6,1,4,1,2011,10,2,144,1,1,1))
h3cBpaCfgEntry.setIndexNames((0,_E,_F),(0,_C,_H))
if mibBuilder.loadTexts:h3cBpaCfgEntry.setStatus(_A)
class _H3cBpaDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('input',1),('output',2)))
_H3cBpaDirection_Type.__name__=_B
_H3cBpaDirection_Object=MibTableColumn
h3cBpaDirection=_H3cBpaDirection_Object((1,3,6,1,4,1,2011,10,2,144,1,1,1,1),_H3cBpaDirection_Type())
h3cBpaDirection.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cBpaDirection.setStatus(_A)
class _H3cBpaSrcOrDest_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('source',1),('destination',2),('both',3)))
_H3cBpaSrcOrDest_Type.__name__=_B
_H3cBpaSrcOrDest_Object=MibTableColumn
h3cBpaSrcOrDest=_H3cBpaSrcOrDest_Object((1,3,6,1,4,1,2011,10,2,144,1,1,1,2),_H3cBpaSrcOrDest_Type())
h3cBpaSrcOrDest.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cBpaSrcOrDest.setStatus(_A)
_H3cBpaRowStatus_Type=RowStatus
_H3cBpaRowStatus_Object=MibTableColumn
h3cBpaRowStatus=_H3cBpaRowStatus_Object((1,3,6,1,4,1,2011,10,2,144,1,1,1,3),_H3cBpaRowStatus_Type())
h3cBpaRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cBpaRowStatus.setStatus(_A)
_H3cBpaStatTable_Object=MibTable
h3cBpaStatTable=_H3cBpaStatTable_Object((1,3,6,1,4,1,2011,10,2,144,1,2))
if mibBuilder.loadTexts:h3cBpaStatTable.setStatus(_A)
_H3cBpaStatEntry_Object=MibTableRow
h3cBpaStatEntry=_H3cBpaStatEntry_Object((1,3,6,1,4,1,2011,10,2,144,1,2,1))
h3cBpaStatEntry.setIndexNames((0,_E,_F),(0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:h3cBpaStatEntry.setStatus(_A)
_H3cBpaTrafficType_Type=InetAddressType
_H3cBpaTrafficType_Object=MibTableColumn
h3cBpaTrafficType=_H3cBpaTrafficType_Object((1,3,6,1,4,1,2011,10,2,144,1,2,1,1),_H3cBpaTrafficType_Type())
h3cBpaTrafficType.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cBpaTrafficType.setStatus(_A)
class _H3cBpaTrafficIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_H3cBpaTrafficIndex_Type.__name__=_B
_H3cBpaTrafficIndex_Object=MibTableColumn
h3cBpaTrafficIndex=_H3cBpaTrafficIndex_Object((1,3,6,1,4,1,2011,10,2,144,1,2,1,2),_H3cBpaTrafficIndex_Type())
h3cBpaTrafficIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cBpaTrafficIndex.setStatus(_A)
_H3cBpaInPacketCount_Type=Counter64
_H3cBpaInPacketCount_Object=MibTableColumn
h3cBpaInPacketCount=_H3cBpaInPacketCount_Object((1,3,6,1,4,1,2011,10,2,144,1,2,1,3),_H3cBpaInPacketCount_Type())
h3cBpaInPacketCount.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cBpaInPacketCount.setStatus(_A)
_H3cBpaInOctetCount_Type=Counter64
_H3cBpaInOctetCount_Object=MibTableColumn
h3cBpaInOctetCount=_H3cBpaInOctetCount_Object((1,3,6,1,4,1,2011,10,2,144,1,2,1,4),_H3cBpaInOctetCount_Type())
h3cBpaInOctetCount.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cBpaInOctetCount.setStatus(_A)
_H3cBpaOutPacketCount_Type=Counter64
_H3cBpaOutPacketCount_Object=MibTableColumn
h3cBpaOutPacketCount=_H3cBpaOutPacketCount_Object((1,3,6,1,4,1,2011,10,2,144,1,2,1,5),_H3cBpaOutPacketCount_Type())
h3cBpaOutPacketCount.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cBpaOutPacketCount.setStatus(_A)
_H3cBpaOutOctetCount_Type=Counter64
_H3cBpaOutOctetCount_Object=MibTableColumn
h3cBpaOutOctetCount=_H3cBpaOutOctetCount_Object((1,3,6,1,4,1,2011,10,2,144,1,2,1,6),_H3cBpaOutOctetCount_Type())
h3cBpaOutOctetCount.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cBpaOutOctetCount.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'h3cBpa':h3cBpa,'h3cBpaObjects':h3cBpaObjects,'h3cBpaCfgTable':h3cBpaCfgTable,'h3cBpaCfgEntry':h3cBpaCfgEntry,_H:h3cBpaDirection,'h3cBpaSrcOrDest':h3cBpaSrcOrDest,'h3cBpaRowStatus':h3cBpaRowStatus,'h3cBpaStatTable':h3cBpaStatTable,'h3cBpaStatEntry':h3cBpaStatEntry,_J:h3cBpaTrafficType,_K:h3cBpaTrafficIndex,'h3cBpaInPacketCount':h3cBpaInPacketCount,'h3cBpaInOctetCount':h3cBpaInOctetCount,'h3cBpaOutPacketCount':h3cBpaOutPacketCount,'h3cBpaOutOctetCount':h3cBpaOutOctetCount})