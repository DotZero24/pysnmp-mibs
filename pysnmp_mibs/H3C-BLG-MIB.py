_E='h3cBlgIndex'
_D='H3C-BLG-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cBlg=ModuleIdentity((1,3,6,1,4,1,2011,10,2,108))
if mibBuilder.loadTexts:h3cBlg.setRevisions(('2009-09-15 11:11',))
class CounterClear(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cleared',1),('nouse',2)))
_H3cBlgObjects_ObjectIdentity=ObjectIdentity
h3cBlgObjects=_H3cBlgObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,108,1))
_H3cBlgStatsTable_Object=MibTable
h3cBlgStatsTable=_H3cBlgStatsTable_Object((1,3,6,1,4,1,2011,10,2,108,1,1))
if mibBuilder.loadTexts:h3cBlgStatsTable.setStatus(_A)
_H3cBlgStatsEntry_Object=MibTableRow
h3cBlgStatsEntry=_H3cBlgStatsEntry_Object((1,3,6,1,4,1,2011,10,2,108,1,1,1))
h3cBlgStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:h3cBlgStatsEntry.setStatus(_A)
class _H3cBlgIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cBlgIndex_Type.__name__=_C
_H3cBlgIndex_Object=MibTableColumn
h3cBlgIndex=_H3cBlgIndex_Object((1,3,6,1,4,1,2011,10,2,108,1,1,1,1),_H3cBlgIndex_Type())
h3cBlgIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cBlgIndex.setStatus(_A)
_H3cBlgGroupTxPacketCount_Type=Counter64
_H3cBlgGroupTxPacketCount_Object=MibTableColumn
h3cBlgGroupTxPacketCount=_H3cBlgGroupTxPacketCount_Object((1,3,6,1,4,1,2011,10,2,108,1,1,1,2),_H3cBlgGroupTxPacketCount_Type())
h3cBlgGroupTxPacketCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBlgGroupTxPacketCount.setStatus(_A)
_H3cBlgGroupRxPacketCount_Type=Counter64
_H3cBlgGroupRxPacketCount_Object=MibTableColumn
h3cBlgGroupRxPacketCount=_H3cBlgGroupRxPacketCount_Object((1,3,6,1,4,1,2011,10,2,108,1,1,1,3),_H3cBlgGroupRxPacketCount_Type())
h3cBlgGroupRxPacketCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBlgGroupRxPacketCount.setStatus(_A)
_H3cBlgGroupTxByteCount_Type=Counter64
_H3cBlgGroupTxByteCount_Object=MibTableColumn
h3cBlgGroupTxByteCount=_H3cBlgGroupTxByteCount_Object((1,3,6,1,4,1,2011,10,2,108,1,1,1,4),_H3cBlgGroupTxByteCount_Type())
h3cBlgGroupTxByteCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBlgGroupTxByteCount.setStatus(_A)
_H3cBlgGroupRxByteCount_Type=Counter64
_H3cBlgGroupRxByteCount_Object=MibTableColumn
h3cBlgGroupRxByteCount=_H3cBlgGroupRxByteCount_Object((1,3,6,1,4,1,2011,10,2,108,1,1,1,5),_H3cBlgGroupRxByteCount_Type())
h3cBlgGroupRxByteCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cBlgGroupRxByteCount.setStatus(_A)
_H3cBlgGroupCountClear_Type=CounterClear
_H3cBlgGroupCountClear_Object=MibTableColumn
h3cBlgGroupCountClear=_H3cBlgGroupCountClear_Object((1,3,6,1,4,1,2011,10,2,108,1,1,1,6),_H3cBlgGroupCountClear_Type())
h3cBlgGroupCountClear.setMaxAccess('read-write')
if mibBuilder.loadTexts:h3cBlgGroupCountClear.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'CounterClear':CounterClear,'h3cBlg':h3cBlg,'h3cBlgObjects':h3cBlgObjects,'h3cBlgStatsTable':h3cBlgStatsTable,'h3cBlgStatsEntry':h3cBlgStatsEntry,_E:h3cBlgIndex,'h3cBlgGroupTxPacketCount':h3cBlgGroupTxPacketCount,'h3cBlgGroupRxPacketCount':h3cBlgGroupRxPacketCount,'h3cBlgGroupTxByteCount':h3cBlgGroupTxByteCount,'h3cBlgGroupRxByteCount':h3cBlgGroupRxByteCount,'h3cBlgGroupCountClear':h3cBlgGroupCountClear})