_H='read-write'
_G='ctTxQPortGroup'
_F='CTRON-TX-QUEUE-ARBITRATION-MIB'
_E='Integer32'
_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctTxQArb,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctTxQArb')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtTxQArbConfig_ObjectIdentity=ObjectIdentity
ctTxQArbConfig=_CtTxQArbConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,5,12,1))
_CtTxQPortGroupMapTable_Object=MibTable
ctTxQPortGroupMapTable=_CtTxQPortGroupMapTable_Object((1,3,6,1,4,1,52,4,1,5,12,1,1))
if mibBuilder.loadTexts:ctTxQPortGroupMapTable.setStatus(_A)
_CtTxQPortGroupEntry_Object=MibTableRow
ctTxQPortGroupEntry=_CtTxQPortGroupEntry_Object((1,3,6,1,4,1,52,4,1,5,12,1,1,1))
ctTxQPortGroupEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:ctTxQPortGroupEntry.setStatus(_A)
_CtTxQPortGroup_Type=Integer32
_CtTxQPortGroup_Object=MibTableColumn
ctTxQPortGroup=_CtTxQPortGroup_Object((1,3,6,1,4,1,52,4,1,5,12,1,1,1,1),_CtTxQPortGroup_Type())
ctTxQPortGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTxQPortGroup.setStatus(_A)
_CtTxQArbTable_Object=MibTable
ctTxQArbTable=_CtTxQArbTable_Object((1,3,6,1,4,1,52,4,1,5,12,1,2))
if mibBuilder.loadTexts:ctTxQArbTable.setStatus(_A)
_CtTxQArbEntry_Object=MibTableRow
ctTxQArbEntry=_CtTxQArbEntry_Object((1,3,6,1,4,1,52,4,1,5,12,1,2,1))
ctTxQArbEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:ctTxQArbEntry.setStatus(_A)
_CtTxQArbNumQueues_Type=Integer32
_CtTxQArbNumQueues_Object=MibTableColumn
ctTxQArbNumQueues=_CtTxQArbNumQueues_Object((1,3,6,1,4,1,52,4,1,5,12,1,2,1,2),_CtTxQArbNumQueues_Type())
ctTxQArbNumQueues.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTxQArbNumQueues.setStatus(_A)
_CtTxQArbNumSlices_Type=Integer32
_CtTxQArbNumSlices_Object=MibTableColumn
ctTxQArbNumSlices=_CtTxQArbNumSlices_Object((1,3,6,1,4,1,52,4,1,5,12,1,2,1,3),_CtTxQArbNumSlices_Type())
ctTxQArbNumSlices.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTxQArbNumSlices.setStatus(_A)
_CtTxQArbSetting_Type=OctetString
_CtTxQArbSetting_Object=MibTableColumn
ctTxQArbSetting=_CtTxQArbSetting_Object((1,3,6,1,4,1,52,4,1,5,12,1,2,1,4),_CtTxQArbSetting_Type())
ctTxQArbSetting.setMaxAccess(_H)
if mibBuilder.loadTexts:ctTxQArbSetting.setStatus(_A)
_CtTxQBufferConfig_ObjectIdentity=ObjectIdentity
ctTxQBufferConfig=_CtTxQBufferConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,5,12,2))
class _CtTxQBufferOptimizeEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_CtTxQBufferOptimizeEnable_Type.__name__=_E
_CtTxQBufferOptimizeEnable_Object=MibScalar
ctTxQBufferOptimizeEnable=_CtTxQBufferOptimizeEnable_Object((1,3,6,1,4,1,52,4,1,5,12,2,1),_CtTxQBufferOptimizeEnable_Type())
ctTxQBufferOptimizeEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:ctTxQBufferOptimizeEnable.setStatus('optional')
mibBuilder.exportSymbols(_F,**{'ctTxQArbConfig':ctTxQArbConfig,'ctTxQPortGroupMapTable':ctTxQPortGroupMapTable,'ctTxQPortGroupEntry':ctTxQPortGroupEntry,_G:ctTxQPortGroup,'ctTxQArbTable':ctTxQArbTable,'ctTxQArbEntry':ctTxQArbEntry,'ctTxQArbNumQueues':ctTxQArbNumQueues,'ctTxQArbNumSlices':ctTxQArbNumSlices,'ctTxQArbSetting':ctTxQArbSetting,'ctTxQBufferConfig':ctTxQBufferConfig,'ctTxQBufferOptimizeEnable':ctTxQBufferOptimizeEnable})