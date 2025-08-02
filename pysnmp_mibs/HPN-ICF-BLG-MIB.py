_E='hpnicfBlgIndex'
_D='HPN-ICF-BLG-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfBlg=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,108))
if mibBuilder.loadTexts:hpnicfBlg.setRevisions(('2009-09-15 11:11',))
class CounterClear(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cleared',1),('nouse',2)))
_HpnicfBlgObjects_ObjectIdentity=ObjectIdentity
hpnicfBlgObjects=_HpnicfBlgObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,108,1))
_HpnicfBlgStatsTable_Object=MibTable
hpnicfBlgStatsTable=_HpnicfBlgStatsTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,108,1,1))
if mibBuilder.loadTexts:hpnicfBlgStatsTable.setStatus(_A)
_HpnicfBlgStatsEntry_Object=MibTableRow
hpnicfBlgStatsEntry=_HpnicfBlgStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,108,1,1,1))
hpnicfBlgStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfBlgStatsEntry.setStatus(_A)
class _HpnicfBlgIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfBlgIndex_Type.__name__=_C
_HpnicfBlgIndex_Object=MibTableColumn
hpnicfBlgIndex=_HpnicfBlgIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,108,1,1,1,1),_HpnicfBlgIndex_Type())
hpnicfBlgIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicfBlgIndex.setStatus(_A)
_HpnicfBlgGroupTxPacketCount_Type=Counter64
_HpnicfBlgGroupTxPacketCount_Object=MibTableColumn
hpnicfBlgGroupTxPacketCount=_HpnicfBlgGroupTxPacketCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,108,1,1,1,2),_HpnicfBlgGroupTxPacketCount_Type())
hpnicfBlgGroupTxPacketCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBlgGroupTxPacketCount.setStatus(_A)
_HpnicfBlgGroupRxPacketCount_Type=Counter64
_HpnicfBlgGroupRxPacketCount_Object=MibTableColumn
hpnicfBlgGroupRxPacketCount=_HpnicfBlgGroupRxPacketCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,108,1,1,1,3),_HpnicfBlgGroupRxPacketCount_Type())
hpnicfBlgGroupRxPacketCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBlgGroupRxPacketCount.setStatus(_A)
_HpnicfBlgGroupTxByteCount_Type=Counter64
_HpnicfBlgGroupTxByteCount_Object=MibTableColumn
hpnicfBlgGroupTxByteCount=_HpnicfBlgGroupTxByteCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,108,1,1,1,4),_HpnicfBlgGroupTxByteCount_Type())
hpnicfBlgGroupTxByteCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBlgGroupTxByteCount.setStatus(_A)
_HpnicfBlgGroupRxByteCount_Type=Counter64
_HpnicfBlgGroupRxByteCount_Object=MibTableColumn
hpnicfBlgGroupRxByteCount=_HpnicfBlgGroupRxByteCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,108,1,1,1,5),_HpnicfBlgGroupRxByteCount_Type())
hpnicfBlgGroupRxByteCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfBlgGroupRxByteCount.setStatus(_A)
_HpnicfBlgGroupCountClear_Type=CounterClear
_HpnicfBlgGroupCountClear_Object=MibTableColumn
hpnicfBlgGroupCountClear=_HpnicfBlgGroupCountClear_Object((1,3,6,1,4,1,11,2,14,11,15,2,108,1,1,1,6),_HpnicfBlgGroupCountClear_Type())
hpnicfBlgGroupCountClear.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfBlgGroupCountClear.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'CounterClear':CounterClear,'hpnicfBlg':hpnicfBlg,'hpnicfBlgObjects':hpnicfBlgObjects,'hpnicfBlgStatsTable':hpnicfBlgStatsTable,'hpnicfBlgStatsEntry':hpnicfBlgStatsEntry,_E:hpnicfBlgIndex,'hpnicfBlgGroupTxPacketCount':hpnicfBlgGroupTxPacketCount,'hpnicfBlgGroupRxPacketCount':hpnicfBlgGroupRxPacketCount,'hpnicfBlgGroupTxByteCount':hpnicfBlgGroupTxByteCount,'hpnicfBlgGroupRxByteCount':hpnicfBlgGroupRxByteCount,'hpnicfBlgGroupCountClear':hpnicfBlgGroupCountClear})