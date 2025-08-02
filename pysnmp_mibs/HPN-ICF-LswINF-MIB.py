_Y='hpnicfPortIsolateGroupIndex'
_X='hpnicfifVLANTrunkIndex'
_W='hpnicfifComboPortIndex'
_V='hpnicfifHybridPortIndex'
_U='hpnicfifAggregatePortIndex'
_T='copper'
_S='s100000M'
_R='s40000M'
_Q='s24000M'
_P='s10000M'
_O='s1000M'
_N='disable'
_M='DisplayString'
_L='DropDirection'
_K='disabled'
_J='enabled'
_I='read-create'
_H='ifIndex'
_G='IF-MIB'
_F='HPN-ICF-LswINF-MIB'
_E='OctetString'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicflswCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicflswCommon')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_G,'InterfaceIndex',_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_M,'PhysAddress','RowStatus','TextualConvention','TruthValue')
hpnicfLswL2InfMib=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,5))
if mibBuilder.loadTexts:hpnicfLswL2InfMib.setRevisions(('2001-06-29 00:00',))
class PortList(TextualConvention,OctetString):status=_A
class VlanIndex(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class DropDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),('enableInbound',2),('enableOutbound',3),('enableBoth',4)))
class SpeedModeFlag(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('s10M',0),('s100M',1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6)))
_HpnicfLswExtInterface_ObjectIdentity=ObjectIdentity
hpnicfLswExtInterface=_HpnicfLswExtInterface_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,1))
_HpnicfifXXTable_Object=MibTable
hpnicfifXXTable=_HpnicfifXXTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1))
if mibBuilder.loadTexts:hpnicfifXXTable.setStatus(_A)
_HpnicfifXXEntry_Object=MibTableRow
hpnicfifXXEntry=_HpnicfifXXEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1))
hpnicfifXXEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hpnicfifXXEntry.setStatus(_A)
_HpnicfifUnBoundPort_Type=TruthValue
_HpnicfifUnBoundPort_Object=MibTableColumn
hpnicfifUnBoundPort=_HpnicfifUnBoundPort_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,1),_HpnicfifUnBoundPort_Type())
hpnicfifUnBoundPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifUnBoundPort.setStatus(_A)
_HpnicfifISPhyPort_Type=TruthValue
_HpnicfifISPhyPort_Object=MibTableColumn
hpnicfifISPhyPort=_HpnicfifISPhyPort_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,2),_HpnicfifISPhyPort_Type())
hpnicfifISPhyPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifISPhyPort.setStatus(_A)
_HpnicfifAggregatePort_Type=TruthValue
_HpnicfifAggregatePort_Object=MibTableColumn
hpnicfifAggregatePort=_HpnicfifAggregatePort_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,3),_HpnicfifAggregatePort_Type())
hpnicfifAggregatePort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifAggregatePort.setStatus(_A)
_HpnicfifMirrorPort_Type=TruthValue
_HpnicfifMirrorPort_Object=MibTableColumn
hpnicfifMirrorPort=_HpnicfifMirrorPort_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,4),_HpnicfifMirrorPort_Type())
hpnicfifMirrorPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifMirrorPort.setStatus(_A)
class _HpnicfifVLANType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('vLANTrunk',1),('access',2),('hybrid',3),('fabric',4)))
_HpnicfifVLANType_Type.__name__=_D
_HpnicfifVLANType_Object=MibTableColumn
hpnicfifVLANType=_HpnicfifVLANType_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,5),_HpnicfifVLANType_Type())
hpnicfifVLANType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifVLANType.setStatus(_A)
class _HpnicfifMcastControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfifMcastControl_Type.__name__=_D
_HpnicfifMcastControl_Object=MibTableColumn
hpnicfifMcastControl=_HpnicfifMcastControl_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,6),_HpnicfifMcastControl_Type())
hpnicfifMcastControl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifMcastControl.setStatus(_A)
_HpnicfifFlowControl_Type=TruthValue
_HpnicfifFlowControl_Object=MibTableColumn
hpnicfifFlowControl=_HpnicfifFlowControl_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,7),_HpnicfifFlowControl_Type())
hpnicfifFlowControl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifFlowControl.setStatus(_A)
_HpnicfifSrcMacControl_Type=TruthValue
_HpnicfifSrcMacControl_Object=MibTableColumn
hpnicfifSrcMacControl=_HpnicfifSrcMacControl_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,8),_HpnicfifSrcMacControl_Type())
hpnicfifSrcMacControl.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifSrcMacControl.setStatus(_A)
class _HpnicfifClearStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_HpnicfifClearStat_Type.__name__=_D
_HpnicfifClearStat_Object=MibTableColumn
hpnicfifClearStat=_HpnicfifClearStat_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,9),_HpnicfifClearStat_Type())
hpnicfifClearStat.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifClearStat.setStatus(_A)
_HpnicfifXXBasePortIndex_Type=Integer32
_HpnicfifXXBasePortIndex_Object=MibTableColumn
hpnicfifXXBasePortIndex=_HpnicfifXXBasePortIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,10),_HpnicfifXXBasePortIndex_Type())
hpnicfifXXBasePortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifXXBasePortIndex.setStatus(_A)
_HpnicfifXXDevPortIndex_Type=Integer32
_HpnicfifXXDevPortIndex_Object=MibTableColumn
hpnicfifXXDevPortIndex=_HpnicfifXXDevPortIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,11),_HpnicfifXXDevPortIndex_Type())
hpnicfifXXDevPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifXXDevPortIndex.setStatus(_A)
_HpnicfifPpsMcastControl_Type=Integer32
_HpnicfifPpsMcastControl_Object=MibTableColumn
hpnicfifPpsMcastControl=_HpnicfifPpsMcastControl_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,12),_HpnicfifPpsMcastControl_Type())
hpnicfifPpsMcastControl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifPpsMcastControl.setStatus(_A)
class _HpnicfifPpsBcastDisValControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),(_N,2)))
_HpnicfifPpsBcastDisValControl_Type.__name__=_D
_HpnicfifPpsBcastDisValControl_Object=MibTableColumn
hpnicfifPpsBcastDisValControl=_HpnicfifPpsBcastDisValControl_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,13),_HpnicfifPpsBcastDisValControl_Type())
hpnicfifPpsBcastDisValControl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifPpsBcastDisValControl.setStatus(_A)
_HpnicfifUniSuppressionStep_Type=Integer32
_HpnicfifUniSuppressionStep_Object=MibTableColumn
hpnicfifUniSuppressionStep=_HpnicfifUniSuppressionStep_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,14),_HpnicfifUniSuppressionStep_Type())
hpnicfifUniSuppressionStep.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifUniSuppressionStep.setStatus(_A)
_HpnicfifPpsUniSuppressionMax_Type=Integer32
_HpnicfifPpsUniSuppressionMax_Object=MibTableColumn
hpnicfifPpsUniSuppressionMax=_HpnicfifPpsUniSuppressionMax_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,15),_HpnicfifPpsUniSuppressionMax_Type())
hpnicfifPpsUniSuppressionMax.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifPpsUniSuppressionMax.setStatus(_A)
_HpnicfifMulSuppressionStep_Type=Integer32
_HpnicfifMulSuppressionStep_Object=MibTableColumn
hpnicfifMulSuppressionStep=_HpnicfifMulSuppressionStep_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,16),_HpnicfifMulSuppressionStep_Type())
hpnicfifMulSuppressionStep.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifMulSuppressionStep.setStatus(_A)
_HpnicfifPpsMulSuppressionMax_Type=Integer32
_HpnicfifPpsMulSuppressionMax_Object=MibTableColumn
hpnicfifPpsMulSuppressionMax=_HpnicfifPpsMulSuppressionMax_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,17),_HpnicfifPpsMulSuppressionMax_Type())
hpnicfifPpsMulSuppressionMax.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifPpsMulSuppressionMax.setStatus(_A)
_HpnicfifUniSuppression_Type=Integer32
_HpnicfifUniSuppression_Object=MibTableColumn
hpnicfifUniSuppression=_HpnicfifUniSuppression_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,18),_HpnicfifUniSuppression_Type())
hpnicfifUniSuppression.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifUniSuppression.setStatus(_A)
_HpnicfifPpsUniSuppression_Type=Integer32
_HpnicfifPpsUniSuppression_Object=MibTableColumn
hpnicfifPpsUniSuppression=_HpnicfifPpsUniSuppression_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,19),_HpnicfifPpsUniSuppression_Type())
hpnicfifPpsUniSuppression.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifPpsUniSuppression.setStatus(_A)
_HpnicfifMulSuppression_Type=Integer32
_HpnicfifMulSuppression_Object=MibTableColumn
hpnicfifMulSuppression=_HpnicfifMulSuppression_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,20),_HpnicfifMulSuppression_Type())
hpnicfifMulSuppression.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifMulSuppression.setStatus(_A)
_HpnicfifPpsMulSuppression_Type=Integer32
_HpnicfifPpsMulSuppression_Object=MibTableColumn
hpnicfifPpsMulSuppression=_HpnicfifPpsMulSuppression_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,21),_HpnicfifPpsMulSuppression_Type())
hpnicfifPpsMulSuppression.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifPpsMulSuppression.setStatus(_A)
class _HpnicfifComboActivePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fiber',1),(_T,2),('na',3)))
_HpnicfifComboActivePort_Type.__name__=_D
_HpnicfifComboActivePort_Object=MibTableColumn
hpnicfifComboActivePort=_HpnicfifComboActivePort_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,22),_HpnicfifComboActivePort_Type())
hpnicfifComboActivePort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifComboActivePort.setStatus('obsolete')
_HpnicfifBMbpsMulSuppressionMax_Type=Integer32
_HpnicfifBMbpsMulSuppressionMax_Object=MibTableColumn
hpnicfifBMbpsMulSuppressionMax=_HpnicfifBMbpsMulSuppressionMax_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,23),_HpnicfifBMbpsMulSuppressionMax_Type())
hpnicfifBMbpsMulSuppressionMax.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifBMbpsMulSuppressionMax.setStatus(_A)
_HpnicfifBMbpsMulSuppression_Type=Integer32
_HpnicfifBMbpsMulSuppression_Object=MibTableColumn
hpnicfifBMbpsMulSuppression=_HpnicfifBMbpsMulSuppression_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,24),_HpnicfifBMbpsMulSuppression_Type())
hpnicfifBMbpsMulSuppression.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifBMbpsMulSuppression.setStatus(_A)
_HpnicfifBKbpsMulSuppressionMax_Type=Integer32
_HpnicfifBKbpsMulSuppressionMax_Object=MibTableColumn
hpnicfifBKbpsMulSuppressionMax=_HpnicfifBKbpsMulSuppressionMax_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,25),_HpnicfifBKbpsMulSuppressionMax_Type())
hpnicfifBKbpsMulSuppressionMax.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifBKbpsMulSuppressionMax.setStatus(_A)
_HpnicfifBKbpsMulSuppressionStep_Type=Integer32
_HpnicfifBKbpsMulSuppressionStep_Object=MibTableColumn
hpnicfifBKbpsMulSuppressionStep=_HpnicfifBKbpsMulSuppressionStep_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,26),_HpnicfifBKbpsMulSuppressionStep_Type())
hpnicfifBKbpsMulSuppressionStep.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifBKbpsMulSuppressionStep.setStatus(_A)
_HpnicfifBKbpsMulSuppression_Type=Integer32
_HpnicfifBKbpsMulSuppression_Object=MibTableColumn
hpnicfifBKbpsMulSuppression=_HpnicfifBKbpsMulSuppression_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,27),_HpnicfifBKbpsMulSuppression_Type())
hpnicfifBKbpsMulSuppression.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifBKbpsMulSuppression.setStatus(_A)
class _HpnicfifUnknownPacketDropMul_Type(DropDirection):defaultValue=1
_HpnicfifUnknownPacketDropMul_Type.__name__=_L
_HpnicfifUnknownPacketDropMul_Object=MibTableColumn
hpnicfifUnknownPacketDropMul=_HpnicfifUnknownPacketDropMul_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,28),_HpnicfifUnknownPacketDropMul_Type())
hpnicfifUnknownPacketDropMul.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifUnknownPacketDropMul.setStatus(_A)
class _HpnicfifUnknownPacketDropUni_Type(DropDirection):defaultValue=1
_HpnicfifUnknownPacketDropUni_Type.__name__=_L
_HpnicfifUnknownPacketDropUni_Object=MibTableColumn
hpnicfifUnknownPacketDropUni=_HpnicfifUnknownPacketDropUni_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,29),_HpnicfifUnknownPacketDropUni_Type())
hpnicfifUnknownPacketDropUni.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifUnknownPacketDropUni.setStatus(_A)
_HpnicfifBMbpsUniSuppressionMax_Type=Integer32
_HpnicfifBMbpsUniSuppressionMax_Object=MibTableColumn
hpnicfifBMbpsUniSuppressionMax=_HpnicfifBMbpsUniSuppressionMax_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,30),_HpnicfifBMbpsUniSuppressionMax_Type())
hpnicfifBMbpsUniSuppressionMax.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifBMbpsUniSuppressionMax.setStatus(_A)
_HpnicfifBMbpsUniSuppression_Type=Integer32
_HpnicfifBMbpsUniSuppression_Object=MibTableColumn
hpnicfifBMbpsUniSuppression=_HpnicfifBMbpsUniSuppression_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,31),_HpnicfifBMbpsUniSuppression_Type())
hpnicfifBMbpsUniSuppression.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifBMbpsUniSuppression.setStatus(_A)
_HpnicfifBKbpsUniSuppressionMax_Type=Integer32
_HpnicfifBKbpsUniSuppressionMax_Object=MibTableColumn
hpnicfifBKbpsUniSuppressionMax=_HpnicfifBKbpsUniSuppressionMax_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,32),_HpnicfifBKbpsUniSuppressionMax_Type())
hpnicfifBKbpsUniSuppressionMax.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifBKbpsUniSuppressionMax.setStatus(_A)
_HpnicfifBKbpsUniSuppressionStep_Type=Integer32
_HpnicfifBKbpsUniSuppressionStep_Object=MibTableColumn
hpnicfifBKbpsUniSuppressionStep=_HpnicfifBKbpsUniSuppressionStep_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,33),_HpnicfifBKbpsUniSuppressionStep_Type())
hpnicfifBKbpsUniSuppressionStep.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifBKbpsUniSuppressionStep.setStatus(_A)
_HpnicfifBKbpsUniSuppression_Type=Integer32
_HpnicfifBKbpsUniSuppression_Object=MibTableColumn
hpnicfifBKbpsUniSuppression=_HpnicfifBKbpsUniSuppression_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,34),_HpnicfifBKbpsUniSuppression_Type())
hpnicfifBKbpsUniSuppression.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifBKbpsUniSuppression.setStatus(_A)
_HpnicfifOutPayloadOctets_Type=Counter64
_HpnicfifOutPayloadOctets_Object=MibTableColumn
hpnicfifOutPayloadOctets=_HpnicfifOutPayloadOctets_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,35),_HpnicfifOutPayloadOctets_Type())
hpnicfifOutPayloadOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifOutPayloadOctets.setStatus(_A)
_HpnicfifInPayloadOctets_Type=Counter64
_HpnicfifInPayloadOctets_Object=MibTableColumn
hpnicfifInPayloadOctets=_HpnicfifInPayloadOctets_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,36),_HpnicfifInPayloadOctets_Type())
hpnicfifInPayloadOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifInPayloadOctets.setStatus(_A)
_HpnicfifInErrorPktsRate_Type=Integer32
_HpnicfifInErrorPktsRate_Object=MibTableColumn
hpnicfifInErrorPktsRate=_HpnicfifInErrorPktsRate_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,37),_HpnicfifInErrorPktsRate_Type())
hpnicfifInErrorPktsRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifInErrorPktsRate.setStatus(_A)
_HpnicfifInPkts_Type=Counter64
_HpnicfifInPkts_Object=MibTableColumn
hpnicfifInPkts=_HpnicfifInPkts_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,38),_HpnicfifInPkts_Type())
hpnicfifInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifInPkts.setStatus(_A)
_HpnicfifInNormalPkts_Type=Counter64
_HpnicfifInNormalPkts_Object=MibTableColumn
hpnicfifInNormalPkts=_HpnicfifInNormalPkts_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,39),_HpnicfifInNormalPkts_Type())
hpnicfifInNormalPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifInNormalPkts.setStatus(_A)
_HpnicfifOutPkts_Type=Counter64
_HpnicfifOutPkts_Object=MibTableColumn
hpnicfifOutPkts=_HpnicfifOutPkts_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,1,1,40),_HpnicfifOutPkts_Type())
hpnicfifOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifOutPkts.setStatus(_A)
_HpnicfifAggregateTable_Object=MibTable
hpnicfifAggregateTable=_HpnicfifAggregateTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,2))
if mibBuilder.loadTexts:hpnicfifAggregateTable.setStatus(_A)
_HpnicfifAggregateEntry_Object=MibTableRow
hpnicfifAggregateEntry=_HpnicfifAggregateEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,2,1))
hpnicfifAggregateEntry.setIndexNames((0,_F,_U))
if mibBuilder.loadTexts:hpnicfifAggregateEntry.setStatus(_A)
_HpnicfifAggregatePortIndex_Type=InterfaceIndex
_HpnicfifAggregatePortIndex_Object=MibTableColumn
hpnicfifAggregatePortIndex=_HpnicfifAggregatePortIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,2,1,1),_HpnicfifAggregatePortIndex_Type())
hpnicfifAggregatePortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifAggregatePortIndex.setStatus(_A)
class _HpnicfifAggregatePortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_HpnicfifAggregatePortName_Type.__name__=_E
_HpnicfifAggregatePortName_Object=MibTableColumn
hpnicfifAggregatePortName=_HpnicfifAggregatePortName_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,2,1,2),_HpnicfifAggregatePortName_Type())
hpnicfifAggregatePortName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifAggregatePortName.setStatus(_A)
_HpnicfifAggregatePortListPorts_Type=PortList
_HpnicfifAggregatePortListPorts_Object=MibTableColumn
hpnicfifAggregatePortListPorts=_HpnicfifAggregatePortListPorts_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,2,1,3),_HpnicfifAggregatePortListPorts_Type())
hpnicfifAggregatePortListPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifAggregatePortListPorts.setStatus(_A)
class _HpnicfifAggregateModel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ingress',1),('both',2),('round-robin',3)))
_HpnicfifAggregateModel_Type.__name__=_D
_HpnicfifAggregateModel_Object=MibTableColumn
hpnicfifAggregateModel=_HpnicfifAggregateModel_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,2,1,4),_HpnicfifAggregateModel_Type())
hpnicfifAggregateModel.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifAggregateModel.setStatus(_A)
_HpnicfifAggregateOperStatus_Type=RowStatus
_HpnicfifAggregateOperStatus_Object=MibTableColumn
hpnicfifAggregateOperStatus=_HpnicfifAggregateOperStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,2,1,5),_HpnicfifAggregateOperStatus_Type())
hpnicfifAggregateOperStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfifAggregateOperStatus.setStatus(_A)
_HpnicfifHybridPortTable_Object=MibTable
hpnicfifHybridPortTable=_HpnicfifHybridPortTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,3))
if mibBuilder.loadTexts:hpnicfifHybridPortTable.setStatus(_A)
_HpnicfifHybridPortEntry_Object=MibTableRow
hpnicfifHybridPortEntry=_HpnicfifHybridPortEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,3,1))
hpnicfifHybridPortEntry.setIndexNames((0,_F,_V))
if mibBuilder.loadTexts:hpnicfifHybridPortEntry.setStatus(_A)
_HpnicfifHybridPortIndex_Type=Integer32
_HpnicfifHybridPortIndex_Object=MibTableColumn
hpnicfifHybridPortIndex=_HpnicfifHybridPortIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,3,1,1),_HpnicfifHybridPortIndex_Type())
hpnicfifHybridPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifHybridPortIndex.setStatus(_A)
class _HpnicfifHybridTaggedVlanListLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnicfifHybridTaggedVlanListLow_Type.__name__=_E
_HpnicfifHybridTaggedVlanListLow_Object=MibTableColumn
hpnicfifHybridTaggedVlanListLow=_HpnicfifHybridTaggedVlanListLow_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,3,1,2),_HpnicfifHybridTaggedVlanListLow_Type())
hpnicfifHybridTaggedVlanListLow.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifHybridTaggedVlanListLow.setStatus(_A)
class _HpnicfifHybridTaggedVlanListHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnicfifHybridTaggedVlanListHigh_Type.__name__=_E
_HpnicfifHybridTaggedVlanListHigh_Object=MibTableColumn
hpnicfifHybridTaggedVlanListHigh=_HpnicfifHybridTaggedVlanListHigh_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,3,1,3),_HpnicfifHybridTaggedVlanListHigh_Type())
hpnicfifHybridTaggedVlanListHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifHybridTaggedVlanListHigh.setStatus(_A)
class _HpnicfifHybridUnTaggedVlanListLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnicfifHybridUnTaggedVlanListLow_Type.__name__=_E
_HpnicfifHybridUnTaggedVlanListLow_Object=MibTableColumn
hpnicfifHybridUnTaggedVlanListLow=_HpnicfifHybridUnTaggedVlanListLow_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,3,1,4),_HpnicfifHybridUnTaggedVlanListLow_Type())
hpnicfifHybridUnTaggedVlanListLow.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifHybridUnTaggedVlanListLow.setStatus(_A)
class _HpnicfifHybridUnTaggedVlanListHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnicfifHybridUnTaggedVlanListHigh_Type.__name__=_E
_HpnicfifHybridUnTaggedVlanListHigh_Object=MibTableColumn
hpnicfifHybridUnTaggedVlanListHigh=_HpnicfifHybridUnTaggedVlanListHigh_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,3,1,5),_HpnicfifHybridUnTaggedVlanListHigh_Type())
hpnicfifHybridUnTaggedVlanListHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifHybridUnTaggedVlanListHigh.setStatus(_A)
_HpnicfifComboPortTable_Object=MibTable
hpnicfifComboPortTable=_HpnicfifComboPortTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,4))
if mibBuilder.loadTexts:hpnicfifComboPortTable.setStatus(_A)
_HpnicfifComboPortEntry_Object=MibTableRow
hpnicfifComboPortEntry=_HpnicfifComboPortEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,4,1))
hpnicfifComboPortEntry.setIndexNames((0,_F,_W))
if mibBuilder.loadTexts:hpnicfifComboPortEntry.setStatus(_A)
_HpnicfifComboPortIndex_Type=InterfaceIndex
_HpnicfifComboPortIndex_Object=MibTableColumn
hpnicfifComboPortIndex=_HpnicfifComboPortIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,4,1,1),_HpnicfifComboPortIndex_Type())
hpnicfifComboPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifComboPortIndex.setStatus(_A)
class _HpnicfifComboPortCurActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fiber',1),(_T,2),('na',3)))
_HpnicfifComboPortCurActive_Type.__name__=_D
_HpnicfifComboPortCurActive_Object=MibTableColumn
hpnicfifComboPortCurActive=_HpnicfifComboPortCurActive_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,4,1,2),_HpnicfifComboPortCurActive_Type())
hpnicfifComboPortCurActive.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifComboPortCurActive.setStatus(_A)
_HpnicfifPktBufTable_Object=MibTable
hpnicfifPktBufTable=_HpnicfifPktBufTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,5))
if mibBuilder.loadTexts:hpnicfifPktBufTable.setStatus(_A)
_HpnicfifPktBufEntry_Object=MibTableRow
hpnicfifPktBufEntry=_HpnicfifPktBufEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,5,1))
hpnicfifPktBufEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hpnicfifPktBufEntry.setStatus(_A)
_HpnicfifPktBufFree_Type=Integer32
_HpnicfifPktBufFree_Object=MibTableColumn
hpnicfifPktBufFree=_HpnicfifPktBufFree_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,5,1,1),_HpnicfifPktBufFree_Type())
hpnicfifPktBufFree.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifPktBufFree.setStatus(_A)
_HpnicfifPktBufInit_Type=Integer32
_HpnicfifPktBufInit_Object=MibTableColumn
hpnicfifPktBufInit=_HpnicfifPktBufInit_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,5,1,2),_HpnicfifPktBufInit_Type())
hpnicfifPktBufInit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifPktBufInit.setStatus(_A)
_HpnicfifPktBufMin_Type=Integer32
_HpnicfifPktBufMin_Object=MibTableColumn
hpnicfifPktBufMin=_HpnicfifPktBufMin_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,5,1,3),_HpnicfifPktBufMin_Type())
hpnicfifPktBufMin.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifPktBufMin.setStatus(_A)
_HpnicfifPktBufMiss_Type=Counter64
_HpnicfifPktBufMiss_Object=MibTableColumn
hpnicfifPktBufMiss=_HpnicfifPktBufMiss_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,1,5,1,4),_HpnicfifPktBufMiss_Type())
hpnicfifPktBufMiss.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifPktBufMiss.setStatus(_A)
_HpnicfLswL2InfMibObject_ObjectIdentity=ObjectIdentity
hpnicfLswL2InfMibObject=_HpnicfLswL2InfMibObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1))
_HpnicfSlotPortMax_Type=Integer32
_HpnicfSlotPortMax_Object=MibScalar
hpnicfSlotPortMax=_HpnicfSlotPortMax_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,1),_HpnicfSlotPortMax_Type())
hpnicfSlotPortMax.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSlotPortMax.setStatus(_A)
_HpnicfSwitchPortMax_Type=Integer32
_HpnicfSwitchPortMax_Object=MibScalar
hpnicfSwitchPortMax=_HpnicfSwitchPortMax_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,2),_HpnicfSwitchPortMax_Type())
hpnicfSwitchPortMax.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSwitchPortMax.setStatus(_A)
_HpnicfifVLANTrunkStatusTable_Object=MibTable
hpnicfifVLANTrunkStatusTable=_HpnicfifVLANTrunkStatusTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,3))
if mibBuilder.loadTexts:hpnicfifVLANTrunkStatusTable.setStatus(_A)
_HpnicfifVLANTrunkStatusEntry_Object=MibTableRow
hpnicfifVLANTrunkStatusEntry=_HpnicfifVLANTrunkStatusEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,3,1))
hpnicfifVLANTrunkStatusEntry.setIndexNames((0,_F,_X))
if mibBuilder.loadTexts:hpnicfifVLANTrunkStatusEntry.setStatus(_A)
_HpnicfifVLANTrunkIndex_Type=InterfaceIndex
_HpnicfifVLANTrunkIndex_Object=MibTableColumn
hpnicfifVLANTrunkIndex=_HpnicfifVLANTrunkIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,3,1,1),_HpnicfifVLANTrunkIndex_Type())
hpnicfifVLANTrunkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifVLANTrunkIndex.setStatus(_A)
class _HpnicfifVLANTrunkGvrpRegistration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('fixed',2),('forbidden',3)))
_HpnicfifVLANTrunkGvrpRegistration_Type.__name__=_D
_HpnicfifVLANTrunkGvrpRegistration_Object=MibTableColumn
hpnicfifVLANTrunkGvrpRegistration=_HpnicfifVLANTrunkGvrpRegistration_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,3,1,2),_HpnicfifVLANTrunkGvrpRegistration_Type())
hpnicfifVLANTrunkGvrpRegistration.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifVLANTrunkGvrpRegistration.setStatus(_A)
_HpnicfifVLANTrunkPassListLow_Type=OctetString
_HpnicfifVLANTrunkPassListLow_Object=MibTableColumn
hpnicfifVLANTrunkPassListLow=_HpnicfifVLANTrunkPassListLow_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,3,1,4),_HpnicfifVLANTrunkPassListLow_Type())
hpnicfifVLANTrunkPassListLow.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifVLANTrunkPassListLow.setStatus(_A)
_HpnicfifVLANTrunkPassListHigh_Type=OctetString
_HpnicfifVLANTrunkPassListHigh_Object=MibTableColumn
hpnicfifVLANTrunkPassListHigh=_HpnicfifVLANTrunkPassListHigh_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,3,1,5),_HpnicfifVLANTrunkPassListHigh_Type())
hpnicfifVLANTrunkPassListHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifVLANTrunkPassListHigh.setStatus(_A)
_HpnicfifVLANTrunkAllowListLow_Type=OctetString
_HpnicfifVLANTrunkAllowListLow_Object=MibTableColumn
hpnicfifVLANTrunkAllowListLow=_HpnicfifVLANTrunkAllowListLow_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,3,1,6),_HpnicfifVLANTrunkAllowListLow_Type())
hpnicfifVLANTrunkAllowListLow.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifVLANTrunkAllowListLow.setStatus(_A)
_HpnicfifVLANTrunkAllowListHigh_Type=OctetString
_HpnicfifVLANTrunkAllowListHigh_Object=MibTableColumn
hpnicfifVLANTrunkAllowListHigh=_HpnicfifVLANTrunkAllowListHigh_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,3,1,7),_HpnicfifVLANTrunkAllowListHigh_Type())
hpnicfifVLANTrunkAllowListHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifVLANTrunkAllowListHigh.setStatus(_A)
_HpnicfethernetTable_Object=MibTable
hpnicfethernetTable=_HpnicfethernetTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,4))
if mibBuilder.loadTexts:hpnicfethernetTable.setStatus(_A)
_HpnicfethernetEntry_Object=MibTableRow
hpnicfethernetEntry=_HpnicfethernetEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,4,1))
hpnicfethernetEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hpnicfethernetEntry.setStatus(_A)
class _HpnicfifEthernetDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('full',1),('half',2),('auto',3)))
_HpnicfifEthernetDuplex_Type.__name__=_D
_HpnicfifEthernetDuplex_Object=MibTableColumn
hpnicfifEthernetDuplex=_HpnicfifEthernetDuplex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,4,1,3),_HpnicfifEthernetDuplex_Type())
hpnicfifEthernetDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifEthernetDuplex.setStatus(_A)
_HpnicfifEthernetMTU_Type=Integer32
_HpnicfifEthernetMTU_Object=MibTableColumn
hpnicfifEthernetMTU=_HpnicfifEthernetMTU_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,4,1,4),_HpnicfifEthernetMTU_Type())
hpnicfifEthernetMTU.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifEthernetMTU.setStatus(_A)
class _HpnicfifEthernetSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10,100,1000,10000,24000,40000,100000)));namedValues=NamedValues(*(('auto',0),('s10M',10),('s100M',100),(_O,1000),(_P,10000),(_Q,24000),(_R,40000),(_S,100000)))
_HpnicfifEthernetSpeed_Type.__name__=_D
_HpnicfifEthernetSpeed_Object=MibTableColumn
hpnicfifEthernetSpeed=_HpnicfifEthernetSpeed_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,4,1,5),_HpnicfifEthernetSpeed_Type())
hpnicfifEthernetSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifEthernetSpeed.setStatus(_A)
class _HpnicfifEthernetMdi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mdi-ii',1),('mdi-x',2),('mdi-auto',3)))
_HpnicfifEthernetMdi_Type.__name__=_D
_HpnicfifEthernetMdi_Object=MibTableColumn
hpnicfifEthernetMdi=_HpnicfifEthernetMdi_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,4,1,7),_HpnicfifEthernetMdi_Type())
hpnicfifEthernetMdi.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifEthernetMdi.setStatus(_A)
class _HpnicfMaxMacLearn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_HpnicfMaxMacLearn_Type.__name__=_D
_HpnicfMaxMacLearn_Object=MibTableColumn
hpnicfMaxMacLearn=_HpnicfMaxMacLearn_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,4,1,8),_HpnicfMaxMacLearn_Type())
hpnicfMaxMacLearn.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMaxMacLearn.setStatus(_A)
class _HpnicfifMacAddressLearn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_HpnicfifMacAddressLearn_Type.__name__=_D
_HpnicfifMacAddressLearn_Object=MibTableColumn
hpnicfifMacAddressLearn=_HpnicfifMacAddressLearn_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,4,1,9),_HpnicfifMacAddressLearn_Type())
hpnicfifMacAddressLearn.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifMacAddressLearn.setStatus(_A)
class _HpnicfifEthernetTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('test',1))
_HpnicfifEthernetTest_Type.__name__=_D
_HpnicfifEthernetTest_Object=MibTableColumn
hpnicfifEthernetTest=_HpnicfifEthernetTest_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,4,1,10),_HpnicfifEthernetTest_Type())
hpnicfifEthernetTest.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifEthernetTest.setStatus(_A)
class _HpnicfifMacAddrLearnMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('iVL',1),('sVL',2)))
_HpnicfifMacAddrLearnMode_Type.__name__=_D
_HpnicfifMacAddrLearnMode_Object=MibTableColumn
hpnicfifMacAddrLearnMode=_HpnicfifMacAddrLearnMode_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,4,1,11),_HpnicfifMacAddrLearnMode_Type())
hpnicfifMacAddrLearnMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifMacAddrLearnMode.setStatus(_A)
class _HpnicfifEthernetFlowInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,300))
_HpnicfifEthernetFlowInterval_Type.__name__=_D
_HpnicfifEthernetFlowInterval_Object=MibTableColumn
hpnicfifEthernetFlowInterval=_HpnicfifEthernetFlowInterval_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,4,1,12),_HpnicfifEthernetFlowInterval_Type())
hpnicfifEthernetFlowInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifEthernetFlowInterval.setStatus(_A)
_HpnicfifEthernetIsolate_Type=OctetString
_HpnicfifEthernetIsolate_Object=MibTableColumn
hpnicfifEthernetIsolate=_HpnicfifEthernetIsolate_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,4,1,13),_HpnicfifEthernetIsolate_Type())
hpnicfifEthernetIsolate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifEthernetIsolate.setStatus(_A)
class _HpnicfifVlanVPNStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_HpnicfifVlanVPNStatus_Type.__name__=_D
_HpnicfifVlanVPNStatus_Object=MibTableColumn
hpnicfifVlanVPNStatus=_HpnicfifVlanVPNStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,4,1,14),_HpnicfifVlanVPNStatus_Type())
hpnicfifVlanVPNStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifVlanVPNStatus.setStatus(_A)
class _HpnicfifVlanVPNUplinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_HpnicfifVlanVPNUplinkStatus_Type.__name__=_D
_HpnicfifVlanVPNUplinkStatus_Object=MibTableColumn
hpnicfifVlanVPNUplinkStatus=_HpnicfifVlanVPNUplinkStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,4,1,15),_HpnicfifVlanVPNUplinkStatus_Type())
hpnicfifVlanVPNUplinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifVlanVPNUplinkStatus.setStatus(_A)
class _HpnicfifVlanVPNTPID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfifVlanVPNTPID_Type.__name__=_D
_HpnicfifVlanVPNTPID_Object=MibTableColumn
hpnicfifVlanVPNTPID=_HpnicfifVlanVPNTPID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,4,1,16),_HpnicfifVlanVPNTPID_Type())
hpnicfifVlanVPNTPID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifVlanVPNTPID.setStatus(_A)
_HpnicfifIsolateGroupID_Type=Integer32
_HpnicfifIsolateGroupID_Object=MibTableColumn
hpnicfifIsolateGroupID=_HpnicfifIsolateGroupID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,4,1,17),_HpnicfifIsolateGroupID_Type())
hpnicfifIsolateGroupID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifIsolateGroupID.setStatus(_A)
class _HpnicfifisUplinkPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_HpnicfifisUplinkPort_Type.__name__=_D
_HpnicfifisUplinkPort_Object=MibTableColumn
hpnicfifisUplinkPort=_HpnicfifisUplinkPort_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,4,1,18),_HpnicfifisUplinkPort_Type())
hpnicfifisUplinkPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifisUplinkPort.setStatus(_A)
_HpnicfifEthernetAutoSpeedMask_Type=SpeedModeFlag
_HpnicfifEthernetAutoSpeedMask_Object=MibTableColumn
hpnicfifEthernetAutoSpeedMask=_HpnicfifEthernetAutoSpeedMask_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,4,1,19),_HpnicfifEthernetAutoSpeedMask_Type())
hpnicfifEthernetAutoSpeedMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifEthernetAutoSpeedMask.setStatus(_A)
_HpnicfifEthernetAutoSpeed_Type=SpeedModeFlag
_HpnicfifEthernetAutoSpeed_Object=MibTableColumn
hpnicfifEthernetAutoSpeed=_HpnicfifEthernetAutoSpeed_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,4,1,20),_HpnicfifEthernetAutoSpeed_Type())
hpnicfifEthernetAutoSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifEthernetAutoSpeed.setStatus(_A)
_HpnicfIsolateGroupMax_Type=Integer32
_HpnicfIsolateGroupMax_Object=MibScalar
hpnicfIsolateGroupMax=_HpnicfIsolateGroupMax_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,5),_HpnicfIsolateGroupMax_Type())
hpnicfIsolateGroupMax.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIsolateGroupMax.setStatus(_A)
class _HpnicfGlobalBroadcastMaxPps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14881000))
_HpnicfGlobalBroadcastMaxPps_Type.__name__=_D
_HpnicfGlobalBroadcastMaxPps_Object=MibScalar
hpnicfGlobalBroadcastMaxPps=_HpnicfGlobalBroadcastMaxPps_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,6),_HpnicfGlobalBroadcastMaxPps_Type())
hpnicfGlobalBroadcastMaxPps.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfGlobalBroadcastMaxPps.setStatus(_A)
class _HpnicfGlobalBroadcastMaxRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfGlobalBroadcastMaxRatio_Type.__name__=_D
_HpnicfGlobalBroadcastMaxRatio_Object=MibScalar
hpnicfGlobalBroadcastMaxRatio=_HpnicfGlobalBroadcastMaxRatio_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,7),_HpnicfGlobalBroadcastMaxRatio_Type())
hpnicfGlobalBroadcastMaxRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfGlobalBroadcastMaxRatio.setStatus(_A)
class _HpnicfBpduTunnelStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_HpnicfBpduTunnelStatus_Type.__name__=_D
_HpnicfBpduTunnelStatus_Object=MibScalar
hpnicfBpduTunnelStatus=_HpnicfBpduTunnelStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,8),_HpnicfBpduTunnelStatus_Type())
hpnicfBpduTunnelStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfBpduTunnelStatus.setStatus(_A)
class _HpnicfVlanVPNTPIDMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('port-based',1),('global',2)))
_HpnicfVlanVPNTPIDMode_Type.__name__=_D
_HpnicfVlanVPNTPIDMode_Object=MibScalar
hpnicfVlanVPNTPIDMode=_HpnicfVlanVPNTPIDMode_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,9),_HpnicfVlanVPNTPIDMode_Type())
hpnicfVlanVPNTPIDMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVlanVPNTPIDMode.setStatus(_A)
class _HpnicfVlanVPNTPID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfVlanVPNTPID_Type.__name__=_D
_HpnicfVlanVPNTPID_Object=MibScalar
hpnicfVlanVPNTPID=_HpnicfVlanVPNTPID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,10),_HpnicfVlanVPNTPID_Type())
hpnicfVlanVPNTPID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVlanVPNTPID.setStatus(_A)
_HpnicfPortIsolateGroupTable_Object=MibTable
hpnicfPortIsolateGroupTable=_HpnicfPortIsolateGroupTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,11))
if mibBuilder.loadTexts:hpnicfPortIsolateGroupTable.setStatus(_A)
_HpnicfPortIsolateGroupEntry_Object=MibTableRow
hpnicfPortIsolateGroupEntry=_HpnicfPortIsolateGroupEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,11,1))
hpnicfPortIsolateGroupEntry.setIndexNames((0,_F,_Y))
if mibBuilder.loadTexts:hpnicfPortIsolateGroupEntry.setStatus(_A)
_HpnicfPortIsolateGroupIndex_Type=Integer32
_HpnicfPortIsolateGroupIndex_Object=MibTableColumn
hpnicfPortIsolateGroupIndex=_HpnicfPortIsolateGroupIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,11,1,1),_HpnicfPortIsolateGroupIndex_Type())
hpnicfPortIsolateGroupIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicfPortIsolateGroupIndex.setStatus(_A)
_HpnicfPortIsolateUplinkIfIndex_Type=InterfaceIndex
_HpnicfPortIsolateUplinkIfIndex_Object=MibTableColumn
hpnicfPortIsolateUplinkIfIndex=_HpnicfPortIsolateUplinkIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,11,1,2),_HpnicfPortIsolateUplinkIfIndex_Type())
hpnicfPortIsolateUplinkIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfPortIsolateUplinkIfIndex.setStatus(_A)
_HpnicfPortIsolateGroupRowStatus_Type=RowStatus
_HpnicfPortIsolateGroupRowStatus_Object=MibTableColumn
hpnicfPortIsolateGroupRowStatus=_HpnicfPortIsolateGroupRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,11,1,3),_HpnicfPortIsolateGroupRowStatus_Type())
hpnicfPortIsolateGroupRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfPortIsolateGroupRowStatus.setStatus(_A)
class _HpnicfPortIsolateGroupDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_HpnicfPortIsolateGroupDescription_Type.__name__=_M
_HpnicfPortIsolateGroupDescription_Object=MibTableColumn
hpnicfPortIsolateGroupDescription=_HpnicfPortIsolateGroupDescription_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,11,1,4),_HpnicfPortIsolateGroupDescription_Type())
hpnicfPortIsolateGroupDescription.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfPortIsolateGroupDescription.setStatus(_A)
_HpnicfMaxMacLearnRange_Type=Integer32
_HpnicfMaxMacLearnRange_Object=MibScalar
hpnicfMaxMacLearnRange=_HpnicfMaxMacLearnRange_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,12),_HpnicfMaxMacLearnRange_Type())
hpnicfMaxMacLearnRange.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMaxMacLearnRange.setStatus(_A)
_HpnicfifPortProtocolStatTable_Object=MibTable
hpnicfifPortProtocolStatTable=_HpnicfifPortProtocolStatTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13))
if mibBuilder.loadTexts:hpnicfifPortProtocolStatTable.setStatus(_A)
_HpnicfifPortProtocolStatEntry_Object=MibTableRow
hpnicfifPortProtocolStatEntry=_HpnicfifPortProtocolStatEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1))
hpnicfifPortProtocolStatEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hpnicfifPortProtocolStatEntry.setStatus(_A)
_HpnicfifIPv4InOctets_Type=Counter64
_HpnicfifIPv4InOctets_Object=MibTableColumn
hpnicfifIPv4InOctets=_HpnicfifIPv4InOctets_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1,1),_HpnicfifIPv4InOctets_Type())
hpnicfifIPv4InOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIPv4InOctets.setStatus(_A)
_HpnicfifIPv4InUcastPkts_Type=Counter64
_HpnicfifIPv4InUcastPkts_Object=MibTableColumn
hpnicfifIPv4InUcastPkts=_HpnicfifIPv4InUcastPkts_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1,2),_HpnicfifIPv4InUcastPkts_Type())
hpnicfifIPv4InUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIPv4InUcastPkts.setStatus(_A)
_HpnicfifIPv4InMultiPkts_Type=Counter64
_HpnicfifIPv4InMultiPkts_Object=MibTableColumn
hpnicfifIPv4InMultiPkts=_HpnicfifIPv4InMultiPkts_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1,3),_HpnicfifIPv4InMultiPkts_Type())
hpnicfifIPv4InMultiPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIPv4InMultiPkts.setStatus(_A)
_HpnicfifIPv4InBroadcastPkts_Type=Counter64
_HpnicfifIPv4InBroadcastPkts_Object=MibTableColumn
hpnicfifIPv4InBroadcastPkts=_HpnicfifIPv4InBroadcastPkts_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1,4),_HpnicfifIPv4InBroadcastPkts_Type())
hpnicfifIPv4InBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIPv4InBroadcastPkts.setStatus(_A)
_HpnicfifIPv4InDiscards_Type=Counter64
_HpnicfifIPv4InDiscards_Object=MibTableColumn
hpnicfifIPv4InDiscards=_HpnicfifIPv4InDiscards_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1,5),_HpnicfifIPv4InDiscards_Type())
hpnicfifIPv4InDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIPv4InDiscards.setStatus(_A)
_HpnicfifIPv4InErrors_Type=Counter64
_HpnicfifIPv4InErrors_Object=MibTableColumn
hpnicfifIPv4InErrors=_HpnicfifIPv4InErrors_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1,6),_HpnicfifIPv4InErrors_Type())
hpnicfifIPv4InErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIPv4InErrors.setStatus(_A)
_HpnicfifIPv4OutOctets_Type=Counter64
_HpnicfifIPv4OutOctets_Object=MibTableColumn
hpnicfifIPv4OutOctets=_HpnicfifIPv4OutOctets_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1,7),_HpnicfifIPv4OutOctets_Type())
hpnicfifIPv4OutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIPv4OutOctets.setStatus(_A)
_HpnicfifIPv4OutUcastPkts_Type=Counter64
_HpnicfifIPv4OutUcastPkts_Object=MibTableColumn
hpnicfifIPv4OutUcastPkts=_HpnicfifIPv4OutUcastPkts_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1,8),_HpnicfifIPv4OutUcastPkts_Type())
hpnicfifIPv4OutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIPv4OutUcastPkts.setStatus(_A)
_HpnicfifIPv4OutMultiPkts_Type=Counter64
_HpnicfifIPv4OutMultiPkts_Object=MibTableColumn
hpnicfifIPv4OutMultiPkts=_HpnicfifIPv4OutMultiPkts_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1,9),_HpnicfifIPv4OutMultiPkts_Type())
hpnicfifIPv4OutMultiPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIPv4OutMultiPkts.setStatus(_A)
_HpnicfifIPv4OutBroadcastPkts_Type=Counter64
_HpnicfifIPv4OutBroadcastPkts_Object=MibTableColumn
hpnicfifIPv4OutBroadcastPkts=_HpnicfifIPv4OutBroadcastPkts_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1,10),_HpnicfifIPv4OutBroadcastPkts_Type())
hpnicfifIPv4OutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIPv4OutBroadcastPkts.setStatus(_A)
_HpnicfifIPv4OutDiscards_Type=Counter64
_HpnicfifIPv4OutDiscards_Object=MibTableColumn
hpnicfifIPv4OutDiscards=_HpnicfifIPv4OutDiscards_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1,11),_HpnicfifIPv4OutDiscards_Type())
hpnicfifIPv4OutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIPv4OutDiscards.setStatus(_A)
_HpnicfifIPv4OutErrors_Type=Counter64
_HpnicfifIPv4OutErrors_Object=MibTableColumn
hpnicfifIPv4OutErrors=_HpnicfifIPv4OutErrors_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1,12),_HpnicfifIPv4OutErrors_Type())
hpnicfifIPv4OutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIPv4OutErrors.setStatus(_A)
_HpnicfifIPv6InOctets_Type=Counter64
_HpnicfifIPv6InOctets_Object=MibTableColumn
hpnicfifIPv6InOctets=_HpnicfifIPv6InOctets_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1,13),_HpnicfifIPv6InOctets_Type())
hpnicfifIPv6InOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIPv6InOctets.setStatus(_A)
_HpnicfifIPv6InUcastPkts_Type=Counter64
_HpnicfifIPv6InUcastPkts_Object=MibTableColumn
hpnicfifIPv6InUcastPkts=_HpnicfifIPv6InUcastPkts_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1,14),_HpnicfifIPv6InUcastPkts_Type())
hpnicfifIPv6InUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIPv6InUcastPkts.setStatus(_A)
_HpnicfifIPv6InMultiPkts_Type=Counter64
_HpnicfifIPv6InMultiPkts_Object=MibTableColumn
hpnicfifIPv6InMultiPkts=_HpnicfifIPv6InMultiPkts_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1,15),_HpnicfifIPv6InMultiPkts_Type())
hpnicfifIPv6InMultiPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIPv6InMultiPkts.setStatus(_A)
_HpnicfifIPv6InAnycastPkts_Type=Counter64
_HpnicfifIPv6InAnycastPkts_Object=MibTableColumn
hpnicfifIPv6InAnycastPkts=_HpnicfifIPv6InAnycastPkts_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1,16),_HpnicfifIPv6InAnycastPkts_Type())
hpnicfifIPv6InAnycastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIPv6InAnycastPkts.setStatus(_A)
_HpnicfifIPv6InDiscards_Type=Counter64
_HpnicfifIPv6InDiscards_Object=MibTableColumn
hpnicfifIPv6InDiscards=_HpnicfifIPv6InDiscards_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1,17),_HpnicfifIPv6InDiscards_Type())
hpnicfifIPv6InDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIPv6InDiscards.setStatus(_A)
_HpnicfifIPv6InErrors_Type=Counter64
_HpnicfifIPv6InErrors_Object=MibTableColumn
hpnicfifIPv6InErrors=_HpnicfifIPv6InErrors_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1,18),_HpnicfifIPv6InErrors_Type())
hpnicfifIPv6InErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIPv6InErrors.setStatus(_A)
_HpnicfifIPv6OutOctets_Type=Counter64
_HpnicfifIPv6OutOctets_Object=MibTableColumn
hpnicfifIPv6OutOctets=_HpnicfifIPv6OutOctets_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1,19),_HpnicfifIPv6OutOctets_Type())
hpnicfifIPv6OutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIPv6OutOctets.setStatus(_A)
_HpnicfifIPv6OutUcastPkts_Type=Counter64
_HpnicfifIPv6OutUcastPkts_Object=MibTableColumn
hpnicfifIPv6OutUcastPkts=_HpnicfifIPv6OutUcastPkts_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1,20),_HpnicfifIPv6OutUcastPkts_Type())
hpnicfifIPv6OutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIPv6OutUcastPkts.setStatus(_A)
_HpnicfifIPv6OutMultiPkts_Type=Counter64
_HpnicfifIPv6OutMultiPkts_Object=MibTableColumn
hpnicfifIPv6OutMultiPkts=_HpnicfifIPv6OutMultiPkts_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1,21),_HpnicfifIPv6OutMultiPkts_Type())
hpnicfifIPv6OutMultiPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIPv6OutMultiPkts.setStatus(_A)
_HpnicfifIPv6OutAnycastPkts_Type=Counter64
_HpnicfifIPv6OutAnycastPkts_Object=MibTableColumn
hpnicfifIPv6OutAnycastPkts=_HpnicfifIPv6OutAnycastPkts_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1,22),_HpnicfifIPv6OutAnycastPkts_Type())
hpnicfifIPv6OutAnycastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIPv6OutAnycastPkts.setStatus(_A)
_HpnicfifIPv6OutDiscards_Type=Counter64
_HpnicfifIPv6OutDiscards_Object=MibTableColumn
hpnicfifIPv6OutDiscards=_HpnicfifIPv6OutDiscards_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1,23),_HpnicfifIPv6OutDiscards_Type())
hpnicfifIPv6OutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIPv6OutDiscards.setStatus(_A)
_HpnicfifIPv6OutErrors_Type=Counter64
_HpnicfifIPv6OutErrors_Object=MibTableColumn
hpnicfifIPv6OutErrors=_HpnicfifIPv6OutErrors_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,5,1,13,1,24),_HpnicfifIPv6OutErrors_Type())
hpnicfifIPv6OutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIPv6OutErrors.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'PortList':PortList,'VlanIndex':VlanIndex,_L:DropDirection,'SpeedModeFlag':SpeedModeFlag,'hpnicfLswExtInterface':hpnicfLswExtInterface,'hpnicfifXXTable':hpnicfifXXTable,'hpnicfifXXEntry':hpnicfifXXEntry,'hpnicfifUnBoundPort':hpnicfifUnBoundPort,'hpnicfifISPhyPort':hpnicfifISPhyPort,'hpnicfifAggregatePort':hpnicfifAggregatePort,'hpnicfifMirrorPort':hpnicfifMirrorPort,'hpnicfifVLANType':hpnicfifVLANType,'hpnicfifMcastControl':hpnicfifMcastControl,'hpnicfifFlowControl':hpnicfifFlowControl,'hpnicfifSrcMacControl':hpnicfifSrcMacControl,'hpnicfifClearStat':hpnicfifClearStat,'hpnicfifXXBasePortIndex':hpnicfifXXBasePortIndex,'hpnicfifXXDevPortIndex':hpnicfifXXDevPortIndex,'hpnicfifPpsMcastControl':hpnicfifPpsMcastControl,'hpnicfifPpsBcastDisValControl':hpnicfifPpsBcastDisValControl,'hpnicfifUniSuppressionStep':hpnicfifUniSuppressionStep,'hpnicfifPpsUniSuppressionMax':hpnicfifPpsUniSuppressionMax,'hpnicfifMulSuppressionStep':hpnicfifMulSuppressionStep,'hpnicfifPpsMulSuppressionMax':hpnicfifPpsMulSuppressionMax,'hpnicfifUniSuppression':hpnicfifUniSuppression,'hpnicfifPpsUniSuppression':hpnicfifPpsUniSuppression,'hpnicfifMulSuppression':hpnicfifMulSuppression,'hpnicfifPpsMulSuppression':hpnicfifPpsMulSuppression,'hpnicfifComboActivePort':hpnicfifComboActivePort,'hpnicfifBMbpsMulSuppressionMax':hpnicfifBMbpsMulSuppressionMax,'hpnicfifBMbpsMulSuppression':hpnicfifBMbpsMulSuppression,'hpnicfifBKbpsMulSuppressionMax':hpnicfifBKbpsMulSuppressionMax,'hpnicfifBKbpsMulSuppressionStep':hpnicfifBKbpsMulSuppressionStep,'hpnicfifBKbpsMulSuppression':hpnicfifBKbpsMulSuppression,'hpnicfifUnknownPacketDropMul':hpnicfifUnknownPacketDropMul,'hpnicfifUnknownPacketDropUni':hpnicfifUnknownPacketDropUni,'hpnicfifBMbpsUniSuppressionMax':hpnicfifBMbpsUniSuppressionMax,'hpnicfifBMbpsUniSuppression':hpnicfifBMbpsUniSuppression,'hpnicfifBKbpsUniSuppressionMax':hpnicfifBKbpsUniSuppressionMax,'hpnicfifBKbpsUniSuppressionStep':hpnicfifBKbpsUniSuppressionStep,'hpnicfifBKbpsUniSuppression':hpnicfifBKbpsUniSuppression,'hpnicfifOutPayloadOctets':hpnicfifOutPayloadOctets,'hpnicfifInPayloadOctets':hpnicfifInPayloadOctets,'hpnicfifInErrorPktsRate':hpnicfifInErrorPktsRate,'hpnicfifInPkts':hpnicfifInPkts,'hpnicfifInNormalPkts':hpnicfifInNormalPkts,'hpnicfifOutPkts':hpnicfifOutPkts,'hpnicfifAggregateTable':hpnicfifAggregateTable,'hpnicfifAggregateEntry':hpnicfifAggregateEntry,_U:hpnicfifAggregatePortIndex,'hpnicfifAggregatePortName':hpnicfifAggregatePortName,'hpnicfifAggregatePortListPorts':hpnicfifAggregatePortListPorts,'hpnicfifAggregateModel':hpnicfifAggregateModel,'hpnicfifAggregateOperStatus':hpnicfifAggregateOperStatus,'hpnicfifHybridPortTable':hpnicfifHybridPortTable,'hpnicfifHybridPortEntry':hpnicfifHybridPortEntry,_V:hpnicfifHybridPortIndex,'hpnicfifHybridTaggedVlanListLow':hpnicfifHybridTaggedVlanListLow,'hpnicfifHybridTaggedVlanListHigh':hpnicfifHybridTaggedVlanListHigh,'hpnicfifHybridUnTaggedVlanListLow':hpnicfifHybridUnTaggedVlanListLow,'hpnicfifHybridUnTaggedVlanListHigh':hpnicfifHybridUnTaggedVlanListHigh,'hpnicfifComboPortTable':hpnicfifComboPortTable,'hpnicfifComboPortEntry':hpnicfifComboPortEntry,_W:hpnicfifComboPortIndex,'hpnicfifComboPortCurActive':hpnicfifComboPortCurActive,'hpnicfifPktBufTable':hpnicfifPktBufTable,'hpnicfifPktBufEntry':hpnicfifPktBufEntry,'hpnicfifPktBufFree':hpnicfifPktBufFree,'hpnicfifPktBufInit':hpnicfifPktBufInit,'hpnicfifPktBufMin':hpnicfifPktBufMin,'hpnicfifPktBufMiss':hpnicfifPktBufMiss,'hpnicfLswL2InfMib':hpnicfLswL2InfMib,'hpnicfLswL2InfMibObject':hpnicfLswL2InfMibObject,'hpnicfSlotPortMax':hpnicfSlotPortMax,'hpnicfSwitchPortMax':hpnicfSwitchPortMax,'hpnicfifVLANTrunkStatusTable':hpnicfifVLANTrunkStatusTable,'hpnicfifVLANTrunkStatusEntry':hpnicfifVLANTrunkStatusEntry,_X:hpnicfifVLANTrunkIndex,'hpnicfifVLANTrunkGvrpRegistration':hpnicfifVLANTrunkGvrpRegistration,'hpnicfifVLANTrunkPassListLow':hpnicfifVLANTrunkPassListLow,'hpnicfifVLANTrunkPassListHigh':hpnicfifVLANTrunkPassListHigh,'hpnicfifVLANTrunkAllowListLow':hpnicfifVLANTrunkAllowListLow,'hpnicfifVLANTrunkAllowListHigh':hpnicfifVLANTrunkAllowListHigh,'hpnicfethernetTable':hpnicfethernetTable,'hpnicfethernetEntry':hpnicfethernetEntry,'hpnicfifEthernetDuplex':hpnicfifEthernetDuplex,'hpnicfifEthernetMTU':hpnicfifEthernetMTU,'hpnicfifEthernetSpeed':hpnicfifEthernetSpeed,'hpnicfifEthernetMdi':hpnicfifEthernetMdi,'hpnicfMaxMacLearn':hpnicfMaxMacLearn,'hpnicfifMacAddressLearn':hpnicfifMacAddressLearn,'hpnicfifEthernetTest':hpnicfifEthernetTest,'hpnicfifMacAddrLearnMode':hpnicfifMacAddrLearnMode,'hpnicfifEthernetFlowInterval':hpnicfifEthernetFlowInterval,'hpnicfifEthernetIsolate':hpnicfifEthernetIsolate,'hpnicfifVlanVPNStatus':hpnicfifVlanVPNStatus,'hpnicfifVlanVPNUplinkStatus':hpnicfifVlanVPNUplinkStatus,'hpnicfifVlanVPNTPID':hpnicfifVlanVPNTPID,'hpnicfifIsolateGroupID':hpnicfifIsolateGroupID,'hpnicfifisUplinkPort':hpnicfifisUplinkPort,'hpnicfifEthernetAutoSpeedMask':hpnicfifEthernetAutoSpeedMask,'hpnicfifEthernetAutoSpeed':hpnicfifEthernetAutoSpeed,'hpnicfIsolateGroupMax':hpnicfIsolateGroupMax,'hpnicfGlobalBroadcastMaxPps':hpnicfGlobalBroadcastMaxPps,'hpnicfGlobalBroadcastMaxRatio':hpnicfGlobalBroadcastMaxRatio,'hpnicfBpduTunnelStatus':hpnicfBpduTunnelStatus,'hpnicfVlanVPNTPIDMode':hpnicfVlanVPNTPIDMode,'hpnicfVlanVPNTPID':hpnicfVlanVPNTPID,'hpnicfPortIsolateGroupTable':hpnicfPortIsolateGroupTable,'hpnicfPortIsolateGroupEntry':hpnicfPortIsolateGroupEntry,_Y:hpnicfPortIsolateGroupIndex,'hpnicfPortIsolateUplinkIfIndex':hpnicfPortIsolateUplinkIfIndex,'hpnicfPortIsolateGroupRowStatus':hpnicfPortIsolateGroupRowStatus,'hpnicfPortIsolateGroupDescription':hpnicfPortIsolateGroupDescription,'hpnicfMaxMacLearnRange':hpnicfMaxMacLearnRange,'hpnicfifPortProtocolStatTable':hpnicfifPortProtocolStatTable,'hpnicfifPortProtocolStatEntry':hpnicfifPortProtocolStatEntry,'hpnicfifIPv4InOctets':hpnicfifIPv4InOctets,'hpnicfifIPv4InUcastPkts':hpnicfifIPv4InUcastPkts,'hpnicfifIPv4InMultiPkts':hpnicfifIPv4InMultiPkts,'hpnicfifIPv4InBroadcastPkts':hpnicfifIPv4InBroadcastPkts,'hpnicfifIPv4InDiscards':hpnicfifIPv4InDiscards,'hpnicfifIPv4InErrors':hpnicfifIPv4InErrors,'hpnicfifIPv4OutOctets':hpnicfifIPv4OutOctets,'hpnicfifIPv4OutUcastPkts':hpnicfifIPv4OutUcastPkts,'hpnicfifIPv4OutMultiPkts':hpnicfifIPv4OutMultiPkts,'hpnicfifIPv4OutBroadcastPkts':hpnicfifIPv4OutBroadcastPkts,'hpnicfifIPv4OutDiscards':hpnicfifIPv4OutDiscards,'hpnicfifIPv4OutErrors':hpnicfifIPv4OutErrors,'hpnicfifIPv6InOctets':hpnicfifIPv6InOctets,'hpnicfifIPv6InUcastPkts':hpnicfifIPv6InUcastPkts,'hpnicfifIPv6InMultiPkts':hpnicfifIPv6InMultiPkts,'hpnicfifIPv6InAnycastPkts':hpnicfifIPv6InAnycastPkts,'hpnicfifIPv6InDiscards':hpnicfifIPv6InDiscards,'hpnicfifIPv6InErrors':hpnicfifIPv6InErrors,'hpnicfifIPv6OutOctets':hpnicfifIPv6OutOctets,'hpnicfifIPv6OutUcastPkts':hpnicfifIPv6OutUcastPkts,'hpnicfifIPv6OutMultiPkts':hpnicfifIPv6OutMultiPkts,'hpnicfifIPv6OutAnycastPkts':hpnicfifIPv6OutAnycastPkts,'hpnicfifIPv6OutDiscards':hpnicfifIPv6OutDiscards,'hpnicfifIPv6OutErrors':hpnicfifIPv6OutErrors})