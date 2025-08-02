_G='read-only'
_F='hpnicfURPFIfIndex'
_E='HPN-ICF-UNICAST-MIB'
_D='TruthValue'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_D)
hpnicfUnicast=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,44))
if mibBuilder.loadTexts:hpnicfUnicast.setRevisions(('2005-03-24 14:54',))
_HpnicfURPFTable_Object=MibTable
hpnicfURPFTable=_HpnicfURPFTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,44,1))
if mibBuilder.loadTexts:hpnicfURPFTable.setStatus(_A)
_HpnicfURPFEntry_Object=MibTableRow
hpnicfURPFEntry=_HpnicfURPFEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,44,1,1))
hpnicfURPFEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hpnicfURPFEntry.setStatus(_A)
_HpnicfURPFIfIndex_Type=Integer32
_HpnicfURPFIfIndex_Object=MibTableColumn
hpnicfURPFIfIndex=_HpnicfURPFIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,44,1,1,1),_HpnicfURPFIfIndex_Type())
hpnicfURPFIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicfURPFIfIndex.setStatus(_A)
class _HpnicfURPFEnabled_Type(TruthValue):defaultValue=2
_HpnicfURPFEnabled_Type.__name__=_D
_HpnicfURPFEnabled_Object=MibTableColumn
hpnicfURPFEnabled=_HpnicfURPFEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,44,1,1,2),_HpnicfURPFEnabled_Type())
hpnicfURPFEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfURPFEnabled.setStatus(_A)
_HpnicfURPFSlotID_Type=Integer32
_HpnicfURPFSlotID_Object=MibTableColumn
hpnicfURPFSlotID=_HpnicfURPFSlotID_Object((1,3,6,1,4,1,11,2,14,11,15,2,44,1,1,3),_HpnicfURPFSlotID_Type())
hpnicfURPFSlotID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfURPFSlotID.setStatus(_A)
_HpnicfURPFTotalReceivedPacket_Type=Counter64
_HpnicfURPFTotalReceivedPacket_Object=MibTableColumn
hpnicfURPFTotalReceivedPacket=_HpnicfURPFTotalReceivedPacket_Object((1,3,6,1,4,1,11,2,14,11,15,2,44,1,1,4),_HpnicfURPFTotalReceivedPacket_Type())
hpnicfURPFTotalReceivedPacket.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfURPFTotalReceivedPacket.setStatus(_A)
_HpnicfURPFDroppedPacket_Type=Counter64
_HpnicfURPFDroppedPacket_Object=MibTableColumn
hpnicfURPFDroppedPacket=_HpnicfURPFDroppedPacket_Object((1,3,6,1,4,1,11,2,14,11,15,2,44,1,1,5),_HpnicfURPFDroppedPacket_Type())
hpnicfURPFDroppedPacket.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfURPFDroppedPacket.setStatus(_A)
class _HpnicfURPFClearStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('reserved',0),('reset',1)))
_HpnicfURPFClearStat_Type.__name__=_C
_HpnicfURPFClearStat_Object=MibTableColumn
hpnicfURPFClearStat=_HpnicfURPFClearStat_Object((1,3,6,1,4,1,11,2,14,11,15,2,44,1,1,6),_HpnicfURPFClearStat_Type())
hpnicfURPFClearStat.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfURPFClearStat.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hpnicfUnicast':hpnicfUnicast,'hpnicfURPFTable':hpnicfURPFTable,'hpnicfURPFEntry':hpnicfURPFEntry,_F:hpnicfURPFIfIndex,'hpnicfURPFEnabled':hpnicfURPFEnabled,'hpnicfURPFSlotID':hpnicfURPFSlotID,'hpnicfURPFTotalReceivedPacket':hpnicfURPFTotalReceivedPacket,'hpnicfURPFDroppedPacket':hpnicfURPFDroppedPacket,'hpnicfURPFClearStat':hpnicfURPFClearStat})