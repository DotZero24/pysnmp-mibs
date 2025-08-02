_G='read-only'
_F='h3cURPFIfIndex'
_E='H3C-UNICAST-MIB'
_D='TruthValue'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_D)
h3cUnicast=ModuleIdentity((1,3,6,1,4,1,2011,10,2,44))
if mibBuilder.loadTexts:h3cUnicast.setRevisions(('2005-03-24 14:54',))
_H3cURPFTable_Object=MibTable
h3cURPFTable=_H3cURPFTable_Object((1,3,6,1,4,1,2011,10,2,44,1))
if mibBuilder.loadTexts:h3cURPFTable.setStatus(_A)
_H3cURPFEntry_Object=MibTableRow
h3cURPFEntry=_H3cURPFEntry_Object((1,3,6,1,4,1,2011,10,2,44,1,1))
h3cURPFEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:h3cURPFEntry.setStatus(_A)
_H3cURPFIfIndex_Type=Integer32
_H3cURPFIfIndex_Object=MibTableColumn
h3cURPFIfIndex=_H3cURPFIfIndex_Object((1,3,6,1,4,1,2011,10,2,44,1,1,1),_H3cURPFIfIndex_Type())
h3cURPFIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cURPFIfIndex.setStatus(_A)
class _H3cURPFEnabled_Type(TruthValue):defaultValue=2
_H3cURPFEnabled_Type.__name__=_D
_H3cURPFEnabled_Object=MibTableColumn
h3cURPFEnabled=_H3cURPFEnabled_Object((1,3,6,1,4,1,2011,10,2,44,1,1,2),_H3cURPFEnabled_Type())
h3cURPFEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cURPFEnabled.setStatus(_A)
_H3cURPFSlotID_Type=Integer32
_H3cURPFSlotID_Object=MibTableColumn
h3cURPFSlotID=_H3cURPFSlotID_Object((1,3,6,1,4,1,2011,10,2,44,1,1,3),_H3cURPFSlotID_Type())
h3cURPFSlotID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cURPFSlotID.setStatus(_A)
_H3cURPFTotalReceivedPacket_Type=Counter64
_H3cURPFTotalReceivedPacket_Object=MibTableColumn
h3cURPFTotalReceivedPacket=_H3cURPFTotalReceivedPacket_Object((1,3,6,1,4,1,2011,10,2,44,1,1,4),_H3cURPFTotalReceivedPacket_Type())
h3cURPFTotalReceivedPacket.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cURPFTotalReceivedPacket.setStatus(_A)
_H3cURPFDroppedPacket_Type=Counter64
_H3cURPFDroppedPacket_Object=MibTableColumn
h3cURPFDroppedPacket=_H3cURPFDroppedPacket_Object((1,3,6,1,4,1,2011,10,2,44,1,1,5),_H3cURPFDroppedPacket_Type())
h3cURPFDroppedPacket.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cURPFDroppedPacket.setStatus(_A)
class _H3cURPFClearStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('reserved',0),('reset',1)))
_H3cURPFClearStat_Type.__name__=_C
_H3cURPFClearStat_Object=MibTableColumn
h3cURPFClearStat=_H3cURPFClearStat_Object((1,3,6,1,4,1,2011,10,2,44,1,1,6),_H3cURPFClearStat_Type())
h3cURPFClearStat.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cURPFClearStat.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'h3cUnicast':h3cUnicast,'h3cURPFTable':h3cURPFTable,'h3cURPFEntry':h3cURPFEntry,_F:h3cURPFIfIndex,'h3cURPFEnabled':h3cURPFEnabled,'h3cURPFSlotID':h3cURPFSlotID,'h3cURPFTotalReceivedPacket':h3cURPFTotalReceivedPacket,'h3cURPFDroppedPacket':h3cURPFDroppedPacket,'h3cURPFClearStat':h3cURPFClearStat})