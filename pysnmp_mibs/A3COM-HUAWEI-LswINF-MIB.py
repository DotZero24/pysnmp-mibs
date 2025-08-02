_Y='hwethernetEntry'
_X='hwifXXEntry'
_W='hwPortIsolateGroupIndex'
_V='hwifVLANTrunkIndex'
_U='hwifComboPortIndex'
_T='hwifHybridPortIndex'
_S='hwifAggregatePortIndex'
_R='copper'
_Q='s100000M'
_P='s40000M'
_O='s24000M'
_N='s10000M'
_M='s1000M'
_L='disable'
_K='DisplayString'
_J='DropDirection'
_I='disabled'
_H='enabled'
_G='read-create'
_F='OctetString'
_E='A3COM-HUAWEI-LswINF-MIB'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lswCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','lswCommon')
ifEntry,ifIndex=mibBuilder.importSymbols('IF-MIB','ifEntry','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','RowStatus','TextualConvention','TruthValue')
hwLswL2InfMib=ModuleIdentity((1,3,6,1,4,1,43,45,1,2,23,1,5))
if mibBuilder.loadTexts:hwLswL2InfMib.setRevisions(('2001-06-29 00:00',))
class PortList(TextualConvention,OctetString):status=_A
class VlanIndex(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class InterfaceIndex(TextualConvention,Integer32):status=_A;displayHint='d'
class DropDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),('enableInbound',2),('enableOutbound',3),('enableBoth',4)))
class SpeedModeFlag(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('s10M',0),('s100M',1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6)))
_HwLswExtInterface_ObjectIdentity=ObjectIdentity
hwLswExtInterface=_HwLswExtInterface_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,23,1,1))
_HwifXXTable_Object=MibTable
hwifXXTable=_HwifXXTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1))
if mibBuilder.loadTexts:hwifXXTable.setStatus(_A)
_HwifXXEntry_Object=MibTableRow
hwifXXEntry=_HwifXXEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1))
if mibBuilder.loadTexts:hwifXXEntry.setStatus(_A)
_HwifUnBoundPort_Type=TruthValue
_HwifUnBoundPort_Object=MibTableColumn
hwifUnBoundPort=_HwifUnBoundPort_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,1),_HwifUnBoundPort_Type())
hwifUnBoundPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifUnBoundPort.setStatus(_A)
_HwifISPhyPort_Type=TruthValue
_HwifISPhyPort_Object=MibTableColumn
hwifISPhyPort=_HwifISPhyPort_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,2),_HwifISPhyPort_Type())
hwifISPhyPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifISPhyPort.setStatus(_A)
_HwifAggregatePort_Type=TruthValue
_HwifAggregatePort_Object=MibTableColumn
hwifAggregatePort=_HwifAggregatePort_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,3),_HwifAggregatePort_Type())
hwifAggregatePort.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifAggregatePort.setStatus(_A)
_HwifMirrorPort_Type=TruthValue
_HwifMirrorPort_Object=MibTableColumn
hwifMirrorPort=_HwifMirrorPort_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,4),_HwifMirrorPort_Type())
hwifMirrorPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifMirrorPort.setStatus(_A)
class _HwifVLANType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('vLANTrunk',1),('access',2),('hybrid',3),('fabric',4)))
_HwifVLANType_Type.__name__=_D
_HwifVLANType_Object=MibTableColumn
hwifVLANType=_HwifVLANType_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,5),_HwifVLANType_Type())
hwifVLANType.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifVLANType.setStatus(_A)
class _HwifMcastControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HwifMcastControl_Type.__name__=_D
_HwifMcastControl_Object=MibTableColumn
hwifMcastControl=_HwifMcastControl_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,6),_HwifMcastControl_Type())
hwifMcastControl.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifMcastControl.setStatus(_A)
_HwifFlowControl_Type=TruthValue
_HwifFlowControl_Object=MibTableColumn
hwifFlowControl=_HwifFlowControl_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,7),_HwifFlowControl_Type())
hwifFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifFlowControl.setStatus(_A)
_HwifSrcMacControl_Type=TruthValue
_HwifSrcMacControl_Object=MibTableColumn
hwifSrcMacControl=_HwifSrcMacControl_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,8),_HwifSrcMacControl_Type())
hwifSrcMacControl.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifSrcMacControl.setStatus(_A)
class _HwifClearStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_HwifClearStat_Type.__name__=_D
_HwifClearStat_Object=MibTableColumn
hwifClearStat=_HwifClearStat_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,9),_HwifClearStat_Type())
hwifClearStat.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifClearStat.setStatus(_A)
_HwifXXBasePortIndex_Type=Integer32
_HwifXXBasePortIndex_Object=MibTableColumn
hwifXXBasePortIndex=_HwifXXBasePortIndex_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,10),_HwifXXBasePortIndex_Type())
hwifXXBasePortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifXXBasePortIndex.setStatus(_A)
_HwifXXDevPortIndex_Type=Integer32
_HwifXXDevPortIndex_Object=MibTableColumn
hwifXXDevPortIndex=_HwifXXDevPortIndex_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,11),_HwifXXDevPortIndex_Type())
hwifXXDevPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifXXDevPortIndex.setStatus(_A)
_HwifPpsMcastControl_Type=Integer32
_HwifPpsMcastControl_Object=MibTableColumn
hwifPpsMcastControl=_HwifPpsMcastControl_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,12),_HwifPpsMcastControl_Type())
hwifPpsMcastControl.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifPpsMcastControl.setStatus(_A)
class _HwifPpsBcastDisValControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),(_L,2)))
_HwifPpsBcastDisValControl_Type.__name__=_D
_HwifPpsBcastDisValControl_Object=MibTableColumn
hwifPpsBcastDisValControl=_HwifPpsBcastDisValControl_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,13),_HwifPpsBcastDisValControl_Type())
hwifPpsBcastDisValControl.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifPpsBcastDisValControl.setStatus(_A)
_HwifUniSuppressionStep_Type=Integer32
_HwifUniSuppressionStep_Object=MibTableColumn
hwifUniSuppressionStep=_HwifUniSuppressionStep_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,14),_HwifUniSuppressionStep_Type())
hwifUniSuppressionStep.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifUniSuppressionStep.setStatus(_A)
_HwifPpsUniSuppressionMax_Type=Integer32
_HwifPpsUniSuppressionMax_Object=MibTableColumn
hwifPpsUniSuppressionMax=_HwifPpsUniSuppressionMax_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,15),_HwifPpsUniSuppressionMax_Type())
hwifPpsUniSuppressionMax.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifPpsUniSuppressionMax.setStatus(_A)
_HwifMulSuppressionStep_Type=Integer32
_HwifMulSuppressionStep_Object=MibTableColumn
hwifMulSuppressionStep=_HwifMulSuppressionStep_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,16),_HwifMulSuppressionStep_Type())
hwifMulSuppressionStep.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifMulSuppressionStep.setStatus(_A)
_HwifPpsMulSuppressionMax_Type=Integer32
_HwifPpsMulSuppressionMax_Object=MibTableColumn
hwifPpsMulSuppressionMax=_HwifPpsMulSuppressionMax_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,17),_HwifPpsMulSuppressionMax_Type())
hwifPpsMulSuppressionMax.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifPpsMulSuppressionMax.setStatus(_A)
_HwifUniSuppression_Type=Integer32
_HwifUniSuppression_Object=MibTableColumn
hwifUniSuppression=_HwifUniSuppression_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,18),_HwifUniSuppression_Type())
hwifUniSuppression.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifUniSuppression.setStatus(_A)
_HwifPpsUniSuppression_Type=Integer32
_HwifPpsUniSuppression_Object=MibTableColumn
hwifPpsUniSuppression=_HwifPpsUniSuppression_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,19),_HwifPpsUniSuppression_Type())
hwifPpsUniSuppression.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifPpsUniSuppression.setStatus(_A)
_HwifMulSuppression_Type=Integer32
_HwifMulSuppression_Object=MibTableColumn
hwifMulSuppression=_HwifMulSuppression_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,20),_HwifMulSuppression_Type())
hwifMulSuppression.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifMulSuppression.setStatus(_A)
_HwifPpsMulSuppression_Type=Integer32
_HwifPpsMulSuppression_Object=MibTableColumn
hwifPpsMulSuppression=_HwifPpsMulSuppression_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,21),_HwifPpsMulSuppression_Type())
hwifPpsMulSuppression.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifPpsMulSuppression.setStatus(_A)
class _HwifComboActivePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fiber',1),(_R,2),('na',3)))
_HwifComboActivePort_Type.__name__=_D
_HwifComboActivePort_Object=MibTableColumn
hwifComboActivePort=_HwifComboActivePort_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,22),_HwifComboActivePort_Type())
hwifComboActivePort.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifComboActivePort.setStatus('obsolete')
_HwifBMbpsMulSuppressionMax_Type=Integer32
_HwifBMbpsMulSuppressionMax_Object=MibTableColumn
hwifBMbpsMulSuppressionMax=_HwifBMbpsMulSuppressionMax_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,23),_HwifBMbpsMulSuppressionMax_Type())
hwifBMbpsMulSuppressionMax.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifBMbpsMulSuppressionMax.setStatus(_A)
_HwifBMbpsMulSuppression_Type=Integer32
_HwifBMbpsMulSuppression_Object=MibTableColumn
hwifBMbpsMulSuppression=_HwifBMbpsMulSuppression_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,24),_HwifBMbpsMulSuppression_Type())
hwifBMbpsMulSuppression.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifBMbpsMulSuppression.setStatus(_A)
_HwifBKbpsMulSuppressionMax_Type=Integer32
_HwifBKbpsMulSuppressionMax_Object=MibTableColumn
hwifBKbpsMulSuppressionMax=_HwifBKbpsMulSuppressionMax_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,25),_HwifBKbpsMulSuppressionMax_Type())
hwifBKbpsMulSuppressionMax.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifBKbpsMulSuppressionMax.setStatus(_A)
_HwifBKbpsMulSuppressionStep_Type=Integer32
_HwifBKbpsMulSuppressionStep_Object=MibTableColumn
hwifBKbpsMulSuppressionStep=_HwifBKbpsMulSuppressionStep_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,26),_HwifBKbpsMulSuppressionStep_Type())
hwifBKbpsMulSuppressionStep.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifBKbpsMulSuppressionStep.setStatus(_A)
_HwifBKbpsMulSuppression_Type=Integer32
_HwifBKbpsMulSuppression_Object=MibTableColumn
hwifBKbpsMulSuppression=_HwifBKbpsMulSuppression_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,27),_HwifBKbpsMulSuppression_Type())
hwifBKbpsMulSuppression.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifBKbpsMulSuppression.setStatus(_A)
class _HwifUnknownPacketDropMul_Type(DropDirection):defaultValue=1
_HwifUnknownPacketDropMul_Type.__name__=_J
_HwifUnknownPacketDropMul_Object=MibTableColumn
hwifUnknownPacketDropMul=_HwifUnknownPacketDropMul_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,28),_HwifUnknownPacketDropMul_Type())
hwifUnknownPacketDropMul.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifUnknownPacketDropMul.setStatus(_A)
class _HwifUnknownPacketDropUni_Type(DropDirection):defaultValue=1
_HwifUnknownPacketDropUni_Type.__name__=_J
_HwifUnknownPacketDropUni_Object=MibTableColumn
hwifUnknownPacketDropUni=_HwifUnknownPacketDropUni_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,29),_HwifUnknownPacketDropUni_Type())
hwifUnknownPacketDropUni.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifUnknownPacketDropUni.setStatus(_A)
_HwifBMbpsUniSuppressionMax_Type=Integer32
_HwifBMbpsUniSuppressionMax_Object=MibTableColumn
hwifBMbpsUniSuppressionMax=_HwifBMbpsUniSuppressionMax_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,30),_HwifBMbpsUniSuppressionMax_Type())
hwifBMbpsUniSuppressionMax.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifBMbpsUniSuppressionMax.setStatus(_A)
_HwifBMbpsUniSuppression_Type=Integer32
_HwifBMbpsUniSuppression_Object=MibTableColumn
hwifBMbpsUniSuppression=_HwifBMbpsUniSuppression_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,31),_HwifBMbpsUniSuppression_Type())
hwifBMbpsUniSuppression.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifBMbpsUniSuppression.setStatus(_A)
_HwifBKbpsUniSuppressionMax_Type=Integer32
_HwifBKbpsUniSuppressionMax_Object=MibTableColumn
hwifBKbpsUniSuppressionMax=_HwifBKbpsUniSuppressionMax_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,32),_HwifBKbpsUniSuppressionMax_Type())
hwifBKbpsUniSuppressionMax.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifBKbpsUniSuppressionMax.setStatus(_A)
_HwifBKbpsUniSuppressionStep_Type=Integer32
_HwifBKbpsUniSuppressionStep_Object=MibTableColumn
hwifBKbpsUniSuppressionStep=_HwifBKbpsUniSuppressionStep_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,33),_HwifBKbpsUniSuppressionStep_Type())
hwifBKbpsUniSuppressionStep.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifBKbpsUniSuppressionStep.setStatus(_A)
_HwifBKbpsUniSuppression_Type=Integer32
_HwifBKbpsUniSuppression_Object=MibTableColumn
hwifBKbpsUniSuppression=_HwifBKbpsUniSuppression_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,34),_HwifBKbpsUniSuppression_Type())
hwifBKbpsUniSuppression.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifBKbpsUniSuppression.setStatus(_A)
_HwifOutPayloadOctets_Type=Counter64
_HwifOutPayloadOctets_Object=MibTableColumn
hwifOutPayloadOctets=_HwifOutPayloadOctets_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,35),_HwifOutPayloadOctets_Type())
hwifOutPayloadOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifOutPayloadOctets.setStatus(_A)
_HwifInPayloadOctets_Type=Counter64
_HwifInPayloadOctets_Object=MibTableColumn
hwifInPayloadOctets=_HwifInPayloadOctets_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,36),_HwifInPayloadOctets_Type())
hwifInPayloadOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifInPayloadOctets.setStatus(_A)
_HwifInErrorPktsRate_Type=Integer32
_HwifInErrorPktsRate_Object=MibTableColumn
hwifInErrorPktsRate=_HwifInErrorPktsRate_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,37),_HwifInErrorPktsRate_Type())
hwifInErrorPktsRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifInErrorPktsRate.setStatus(_A)
_HwifInPkts_Type=Counter64
_HwifInPkts_Object=MibTableColumn
hwifInPkts=_HwifInPkts_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,38),_HwifInPkts_Type())
hwifInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifInPkts.setStatus(_A)
_HwifInNormalPkts_Type=Counter64
_HwifInNormalPkts_Object=MibTableColumn
hwifInNormalPkts=_HwifInNormalPkts_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,39),_HwifInNormalPkts_Type())
hwifInNormalPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifInNormalPkts.setStatus(_A)
_HwifOutPkts_Type=Counter64
_HwifOutPkts_Object=MibTableColumn
hwifOutPkts=_HwifOutPkts_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,1,1,40),_HwifOutPkts_Type())
hwifOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifOutPkts.setStatus(_A)
_HwifAggregateTable_Object=MibTable
hwifAggregateTable=_HwifAggregateTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,2))
if mibBuilder.loadTexts:hwifAggregateTable.setStatus(_A)
_HwifAggregateEntry_Object=MibTableRow
hwifAggregateEntry=_HwifAggregateEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,2,1))
hwifAggregateEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:hwifAggregateEntry.setStatus(_A)
_HwifAggregatePortIndex_Type=InterfaceIndex
_HwifAggregatePortIndex_Object=MibTableColumn
hwifAggregatePortIndex=_HwifAggregatePortIndex_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,2,1,1),_HwifAggregatePortIndex_Type())
hwifAggregatePortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifAggregatePortIndex.setStatus(_A)
class _HwifAggregatePortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_HwifAggregatePortName_Type.__name__=_F
_HwifAggregatePortName_Object=MibTableColumn
hwifAggregatePortName=_HwifAggregatePortName_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,2,1,2),_HwifAggregatePortName_Type())
hwifAggregatePortName.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifAggregatePortName.setStatus(_A)
_HwifAggregatePortListPorts_Type=PortList
_HwifAggregatePortListPorts_Object=MibTableColumn
hwifAggregatePortListPorts=_HwifAggregatePortListPorts_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,2,1,3),_HwifAggregatePortListPorts_Type())
hwifAggregatePortListPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifAggregatePortListPorts.setStatus(_A)
class _HwifAggregateModel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ingress',1),('both',2),('round-robin',3)))
_HwifAggregateModel_Type.__name__=_D
_HwifAggregateModel_Object=MibTableColumn
hwifAggregateModel=_HwifAggregateModel_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,2,1,4),_HwifAggregateModel_Type())
hwifAggregateModel.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifAggregateModel.setStatus(_A)
_HwifAggregateOperStatus_Type=RowStatus
_HwifAggregateOperStatus_Object=MibTableColumn
hwifAggregateOperStatus=_HwifAggregateOperStatus_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,2,1,5),_HwifAggregateOperStatus_Type())
hwifAggregateOperStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hwifAggregateOperStatus.setStatus(_A)
_HwifHybridPortTable_Object=MibTable
hwifHybridPortTable=_HwifHybridPortTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,3))
if mibBuilder.loadTexts:hwifHybridPortTable.setStatus(_A)
_HwifHybridPortEntry_Object=MibTableRow
hwifHybridPortEntry=_HwifHybridPortEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,3,1))
hwifHybridPortEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:hwifHybridPortEntry.setStatus(_A)
_HwifHybridPortIndex_Type=Integer32
_HwifHybridPortIndex_Object=MibTableColumn
hwifHybridPortIndex=_HwifHybridPortIndex_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,3,1,1),_HwifHybridPortIndex_Type())
hwifHybridPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifHybridPortIndex.setStatus(_A)
class _HwifHybridTaggedVlanListLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HwifHybridTaggedVlanListLow_Type.__name__=_F
_HwifHybridTaggedVlanListLow_Object=MibTableColumn
hwifHybridTaggedVlanListLow=_HwifHybridTaggedVlanListLow_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,3,1,2),_HwifHybridTaggedVlanListLow_Type())
hwifHybridTaggedVlanListLow.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifHybridTaggedVlanListLow.setStatus(_A)
class _HwifHybridTaggedVlanListHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HwifHybridTaggedVlanListHigh_Type.__name__=_F
_HwifHybridTaggedVlanListHigh_Object=MibTableColumn
hwifHybridTaggedVlanListHigh=_HwifHybridTaggedVlanListHigh_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,3,1,3),_HwifHybridTaggedVlanListHigh_Type())
hwifHybridTaggedVlanListHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifHybridTaggedVlanListHigh.setStatus(_A)
class _HwifHybridUnTaggedVlanListLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HwifHybridUnTaggedVlanListLow_Type.__name__=_F
_HwifHybridUnTaggedVlanListLow_Object=MibTableColumn
hwifHybridUnTaggedVlanListLow=_HwifHybridUnTaggedVlanListLow_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,3,1,4),_HwifHybridUnTaggedVlanListLow_Type())
hwifHybridUnTaggedVlanListLow.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifHybridUnTaggedVlanListLow.setStatus(_A)
class _HwifHybridUnTaggedVlanListHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HwifHybridUnTaggedVlanListHigh_Type.__name__=_F
_HwifHybridUnTaggedVlanListHigh_Object=MibTableColumn
hwifHybridUnTaggedVlanListHigh=_HwifHybridUnTaggedVlanListHigh_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,3,1,5),_HwifHybridUnTaggedVlanListHigh_Type())
hwifHybridUnTaggedVlanListHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifHybridUnTaggedVlanListHigh.setStatus(_A)
_HwifComboPortTable_Object=MibTable
hwifComboPortTable=_HwifComboPortTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,4))
if mibBuilder.loadTexts:hwifComboPortTable.setStatus(_A)
_HwifComboPortEntry_Object=MibTableRow
hwifComboPortEntry=_HwifComboPortEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,4,1))
hwifComboPortEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:hwifComboPortEntry.setStatus(_A)
_HwifComboPortIndex_Type=InterfaceIndex
_HwifComboPortIndex_Object=MibTableColumn
hwifComboPortIndex=_HwifComboPortIndex_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,4,1,1),_HwifComboPortIndex_Type())
hwifComboPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifComboPortIndex.setStatus(_A)
class _HwifComboPortCurActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fiber',1),(_R,2),('na',3)))
_HwifComboPortCurActive_Type.__name__=_D
_HwifComboPortCurActive_Object=MibTableColumn
hwifComboPortCurActive=_HwifComboPortCurActive_Object((1,3,6,1,4,1,43,45,1,2,23,1,1,4,1,2),_HwifComboPortCurActive_Type())
hwifComboPortCurActive.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifComboPortCurActive.setStatus(_A)
_HwLswL2InfMibObject_ObjectIdentity=ObjectIdentity
hwLswL2InfMibObject=_HwLswL2InfMibObject_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,23,1,5,1))
_HwSlotPortMax_Type=Integer32
_HwSlotPortMax_Object=MibScalar
hwSlotPortMax=_HwSlotPortMax_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,1),_HwSlotPortMax_Type())
hwSlotPortMax.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSlotPortMax.setStatus(_A)
_HwSwitchPortMax_Type=Integer32
_HwSwitchPortMax_Object=MibScalar
hwSwitchPortMax=_HwSwitchPortMax_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,2),_HwSwitchPortMax_Type())
hwSwitchPortMax.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSwitchPortMax.setStatus(_A)
_HwifVLANTrunkStatusTable_Object=MibTable
hwifVLANTrunkStatusTable=_HwifVLANTrunkStatusTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,3))
if mibBuilder.loadTexts:hwifVLANTrunkStatusTable.setStatus(_A)
_HwifVLANTrunkStatusEntry_Object=MibTableRow
hwifVLANTrunkStatusEntry=_HwifVLANTrunkStatusEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,3,1))
hwifVLANTrunkStatusEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:hwifVLANTrunkStatusEntry.setStatus(_A)
_HwifVLANTrunkIndex_Type=InterfaceIndex
_HwifVLANTrunkIndex_Object=MibTableColumn
hwifVLANTrunkIndex=_HwifVLANTrunkIndex_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,3,1,1),_HwifVLANTrunkIndex_Type())
hwifVLANTrunkIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifVLANTrunkIndex.setStatus(_A)
class _HwifVLANTrunkGvrpRegistration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('fixed',2),('forbidden',3)))
_HwifVLANTrunkGvrpRegistration_Type.__name__=_D
_HwifVLANTrunkGvrpRegistration_Object=MibTableColumn
hwifVLANTrunkGvrpRegistration=_HwifVLANTrunkGvrpRegistration_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,3,1,2),_HwifVLANTrunkGvrpRegistration_Type())
hwifVLANTrunkGvrpRegistration.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifVLANTrunkGvrpRegistration.setStatus(_A)
_HwifVLANTrunkPassListLow_Type=OctetString
_HwifVLANTrunkPassListLow_Object=MibTableColumn
hwifVLANTrunkPassListLow=_HwifVLANTrunkPassListLow_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,3,1,4),_HwifVLANTrunkPassListLow_Type())
hwifVLANTrunkPassListLow.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifVLANTrunkPassListLow.setStatus(_A)
_HwifVLANTrunkPassListHigh_Type=OctetString
_HwifVLANTrunkPassListHigh_Object=MibTableColumn
hwifVLANTrunkPassListHigh=_HwifVLANTrunkPassListHigh_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,3,1,5),_HwifVLANTrunkPassListHigh_Type())
hwifVLANTrunkPassListHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifVLANTrunkPassListHigh.setStatus(_A)
_HwifVLANTrunkAllowListLow_Type=OctetString
_HwifVLANTrunkAllowListLow_Object=MibTableColumn
hwifVLANTrunkAllowListLow=_HwifVLANTrunkAllowListLow_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,3,1,6),_HwifVLANTrunkAllowListLow_Type())
hwifVLANTrunkAllowListLow.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifVLANTrunkAllowListLow.setStatus(_A)
_HwifVLANTrunkAllowListHigh_Type=OctetString
_HwifVLANTrunkAllowListHigh_Object=MibTableColumn
hwifVLANTrunkAllowListHigh=_HwifVLANTrunkAllowListHigh_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,3,1,7),_HwifVLANTrunkAllowListHigh_Type())
hwifVLANTrunkAllowListHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifVLANTrunkAllowListHigh.setStatus(_A)
_HwethernetTable_Object=MibTable
hwethernetTable=_HwethernetTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,4))
if mibBuilder.loadTexts:hwethernetTable.setStatus(_A)
_HwethernetEntry_Object=MibTableRow
hwethernetEntry=_HwethernetEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,4,1))
if mibBuilder.loadTexts:hwethernetEntry.setStatus(_A)
class _HwifEthernetDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('full',1),('half',2),('auto',3)))
_HwifEthernetDuplex_Type.__name__=_D
_HwifEthernetDuplex_Object=MibTableColumn
hwifEthernetDuplex=_HwifEthernetDuplex_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,4,1,3),_HwifEthernetDuplex_Type())
hwifEthernetDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifEthernetDuplex.setStatus(_A)
_HwifEthernetMTU_Type=Integer32
_HwifEthernetMTU_Object=MibTableColumn
hwifEthernetMTU=_HwifEthernetMTU_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,4,1,4),_HwifEthernetMTU_Type())
hwifEthernetMTU.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifEthernetMTU.setStatus(_A)
class _HwifEthernetSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10,100,1000,10000,24000,40000,100000)));namedValues=NamedValues(*(('auto',0),('s10M',10),('s100M',100),(_M,1000),(_N,10000),(_O,24000),(_P,40000),(_Q,100000)))
_HwifEthernetSpeed_Type.__name__=_D
_HwifEthernetSpeed_Object=MibTableColumn
hwifEthernetSpeed=_HwifEthernetSpeed_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,4,1,5),_HwifEthernetSpeed_Type())
hwifEthernetSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifEthernetSpeed.setStatus(_A)
class _HwifEthernetMdi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mdi-ii',1),('mdi-x',2),('mdi-auto',3)))
_HwifEthernetMdi_Type.__name__=_D
_HwifEthernetMdi_Object=MibTableColumn
hwifEthernetMdi=_HwifEthernetMdi_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,4,1,7),_HwifEthernetMdi_Type())
hwifEthernetMdi.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifEthernetMdi.setStatus(_A)
class _HwMaxMacLearn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_HwMaxMacLearn_Type.__name__=_D
_HwMaxMacLearn_Object=MibTableColumn
hwMaxMacLearn=_HwMaxMacLearn_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,4,1,8),_HwMaxMacLearn_Type())
hwMaxMacLearn.setMaxAccess(_B)
if mibBuilder.loadTexts:hwMaxMacLearn.setStatus(_A)
class _HwifMacAddressLearn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HwifMacAddressLearn_Type.__name__=_D
_HwifMacAddressLearn_Object=MibTableColumn
hwifMacAddressLearn=_HwifMacAddressLearn_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,4,1,9),_HwifMacAddressLearn_Type())
hwifMacAddressLearn.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifMacAddressLearn.setStatus(_A)
class _HwifEthernetTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('test',1))
_HwifEthernetTest_Type.__name__=_D
_HwifEthernetTest_Object=MibTableColumn
hwifEthernetTest=_HwifEthernetTest_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,4,1,10),_HwifEthernetTest_Type())
hwifEthernetTest.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifEthernetTest.setStatus(_A)
class _HwifMacAddrLearnMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('iVL',1),('sVL',2)))
_HwifMacAddrLearnMode_Type.__name__=_D
_HwifMacAddrLearnMode_Object=MibTableColumn
hwifMacAddrLearnMode=_HwifMacAddrLearnMode_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,4,1,11),_HwifMacAddrLearnMode_Type())
hwifMacAddrLearnMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifMacAddrLearnMode.setStatus(_A)
class _HwifEthernetFlowInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,300))
_HwifEthernetFlowInterval_Type.__name__=_D
_HwifEthernetFlowInterval_Object=MibTableColumn
hwifEthernetFlowInterval=_HwifEthernetFlowInterval_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,4,1,12),_HwifEthernetFlowInterval_Type())
hwifEthernetFlowInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifEthernetFlowInterval.setStatus(_A)
_HwifEthernetIsolate_Type=OctetString
_HwifEthernetIsolate_Object=MibTableColumn
hwifEthernetIsolate=_HwifEthernetIsolate_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,4,1,13),_HwifEthernetIsolate_Type())
hwifEthernetIsolate.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifEthernetIsolate.setStatus(_A)
class _HwifVlanVPNStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HwifVlanVPNStatus_Type.__name__=_D
_HwifVlanVPNStatus_Object=MibTableColumn
hwifVlanVPNStatus=_HwifVlanVPNStatus_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,4,1,14),_HwifVlanVPNStatus_Type())
hwifVlanVPNStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifVlanVPNStatus.setStatus(_A)
class _HwifVlanVPNUplinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HwifVlanVPNUplinkStatus_Type.__name__=_D
_HwifVlanVPNUplinkStatus_Object=MibTableColumn
hwifVlanVPNUplinkStatus=_HwifVlanVPNUplinkStatus_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,4,1,15),_HwifVlanVPNUplinkStatus_Type())
hwifVlanVPNUplinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifVlanVPNUplinkStatus.setStatus(_A)
class _HwifVlanVPNTPID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HwifVlanVPNTPID_Type.__name__=_D
_HwifVlanVPNTPID_Object=MibTableColumn
hwifVlanVPNTPID=_HwifVlanVPNTPID_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,4,1,16),_HwifVlanVPNTPID_Type())
hwifVlanVPNTPID.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifVlanVPNTPID.setStatus(_A)
_HwifIsolateGroupID_Type=Integer32
_HwifIsolateGroupID_Object=MibTableColumn
hwifIsolateGroupID=_HwifIsolateGroupID_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,4,1,17),_HwifIsolateGroupID_Type())
hwifIsolateGroupID.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifIsolateGroupID.setStatus(_A)
class _HwifisUplinkPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_HwifisUplinkPort_Type.__name__=_D
_HwifisUplinkPort_Object=MibTableColumn
hwifisUplinkPort=_HwifisUplinkPort_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,4,1,18),_HwifisUplinkPort_Type())
hwifisUplinkPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifisUplinkPort.setStatus(_A)
_HwifEthernetAutoSpeedMask_Type=SpeedModeFlag
_HwifEthernetAutoSpeedMask_Object=MibTableColumn
hwifEthernetAutoSpeedMask=_HwifEthernetAutoSpeedMask_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,4,1,19),_HwifEthernetAutoSpeedMask_Type())
hwifEthernetAutoSpeedMask.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifEthernetAutoSpeedMask.setStatus(_A)
_HwifEthernetAutoSpeed_Type=SpeedModeFlag
_HwifEthernetAutoSpeed_Object=MibTableColumn
hwifEthernetAutoSpeed=_HwifEthernetAutoSpeed_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,4,1,20),_HwifEthernetAutoSpeed_Type())
hwifEthernetAutoSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifEthernetAutoSpeed.setStatus(_A)
_HwIsolateGroupMax_Type=Integer32
_HwIsolateGroupMax_Object=MibScalar
hwIsolateGroupMax=_HwIsolateGroupMax_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,5),_HwIsolateGroupMax_Type())
hwIsolateGroupMax.setMaxAccess(_C)
if mibBuilder.loadTexts:hwIsolateGroupMax.setStatus(_A)
class _HwGlobalBroadcastMaxPps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14881000))
_HwGlobalBroadcastMaxPps_Type.__name__=_D
_HwGlobalBroadcastMaxPps_Object=MibScalar
hwGlobalBroadcastMaxPps=_HwGlobalBroadcastMaxPps_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,6),_HwGlobalBroadcastMaxPps_Type())
hwGlobalBroadcastMaxPps.setMaxAccess(_B)
if mibBuilder.loadTexts:hwGlobalBroadcastMaxPps.setStatus(_A)
class _HwGlobalBroadcastMaxRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HwGlobalBroadcastMaxRatio_Type.__name__=_D
_HwGlobalBroadcastMaxRatio_Object=MibScalar
hwGlobalBroadcastMaxRatio=_HwGlobalBroadcastMaxRatio_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,7),_HwGlobalBroadcastMaxRatio_Type())
hwGlobalBroadcastMaxRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:hwGlobalBroadcastMaxRatio.setStatus(_A)
class _HwBpduTunnelStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HwBpduTunnelStatus_Type.__name__=_D
_HwBpduTunnelStatus_Object=MibScalar
hwBpduTunnelStatus=_HwBpduTunnelStatus_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,8),_HwBpduTunnelStatus_Type())
hwBpduTunnelStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwBpduTunnelStatus.setStatus(_A)
class _HwVlanVPNTPIDMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('port-based',1),('global',2)))
_HwVlanVPNTPIDMode_Type.__name__=_D
_HwVlanVPNTPIDMode_Object=MibScalar
hwVlanVPNTPIDMode=_HwVlanVPNTPIDMode_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,9),_HwVlanVPNTPIDMode_Type())
hwVlanVPNTPIDMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVlanVPNTPIDMode.setStatus(_A)
class _HwVlanVPNTPID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HwVlanVPNTPID_Type.__name__=_D
_HwVlanVPNTPID_Object=MibScalar
hwVlanVPNTPID=_HwVlanVPNTPID_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,10),_HwVlanVPNTPID_Type())
hwVlanVPNTPID.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVlanVPNTPID.setStatus(_A)
_HwPortIsolateGroupTable_Object=MibTable
hwPortIsolateGroupTable=_HwPortIsolateGroupTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,11))
if mibBuilder.loadTexts:hwPortIsolateGroupTable.setStatus(_A)
_HwPortIsolateGroupEntry_Object=MibTableRow
hwPortIsolateGroupEntry=_HwPortIsolateGroupEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,11,1))
hwPortIsolateGroupEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:hwPortIsolateGroupEntry.setStatus(_A)
_HwPortIsolateGroupIndex_Type=Integer32
_HwPortIsolateGroupIndex_Object=MibTableColumn
hwPortIsolateGroupIndex=_HwPortIsolateGroupIndex_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,11,1,1),_HwPortIsolateGroupIndex_Type())
hwPortIsolateGroupIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hwPortIsolateGroupIndex.setStatus(_A)
_HwPortIsolateUplinkIfIndex_Type=InterfaceIndex
_HwPortIsolateUplinkIfIndex_Object=MibTableColumn
hwPortIsolateUplinkIfIndex=_HwPortIsolateUplinkIfIndex_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,11,1,2),_HwPortIsolateUplinkIfIndex_Type())
hwPortIsolateUplinkIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hwPortIsolateUplinkIfIndex.setStatus(_A)
_HwPortIsolateGroupRowStatus_Type=RowStatus
_HwPortIsolateGroupRowStatus_Object=MibTableColumn
hwPortIsolateGroupRowStatus=_HwPortIsolateGroupRowStatus_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,11,1,3),_HwPortIsolateGroupRowStatus_Type())
hwPortIsolateGroupRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hwPortIsolateGroupRowStatus.setStatus(_A)
class _HwPortIsolateGroupDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_HwPortIsolateGroupDescription_Type.__name__=_K
_HwPortIsolateGroupDescription_Object=MibTableColumn
hwPortIsolateGroupDescription=_HwPortIsolateGroupDescription_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,11,1,4),_HwPortIsolateGroupDescription_Type())
hwPortIsolateGroupDescription.setMaxAccess(_G)
if mibBuilder.loadTexts:hwPortIsolateGroupDescription.setStatus(_A)
_HwMaxMacLearnRange_Type=Integer32
_HwMaxMacLearnRange_Object=MibScalar
hwMaxMacLearnRange=_HwMaxMacLearnRange_Object((1,3,6,1,4,1,43,45,1,2,23,1,5,1,12),_HwMaxMacLearnRange_Type())
hwMaxMacLearnRange.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMaxMacLearnRange.setStatus(_A)
ifEntry.registerAugmentions((_E,_X))
hwifXXEntry.setIndexNames(*ifEntry.getIndexNames())
ifEntry.registerAugmentions((_E,_Y))
hwethernetEntry.setIndexNames(*ifEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{'PortList':PortList,'VlanIndex':VlanIndex,'InterfaceIndex':InterfaceIndex,_J:DropDirection,'SpeedModeFlag':SpeedModeFlag,'hwLswExtInterface':hwLswExtInterface,'hwifXXTable':hwifXXTable,_X:hwifXXEntry,'hwifUnBoundPort':hwifUnBoundPort,'hwifISPhyPort':hwifISPhyPort,'hwifAggregatePort':hwifAggregatePort,'hwifMirrorPort':hwifMirrorPort,'hwifVLANType':hwifVLANType,'hwifMcastControl':hwifMcastControl,'hwifFlowControl':hwifFlowControl,'hwifSrcMacControl':hwifSrcMacControl,'hwifClearStat':hwifClearStat,'hwifXXBasePortIndex':hwifXXBasePortIndex,'hwifXXDevPortIndex':hwifXXDevPortIndex,'hwifPpsMcastControl':hwifPpsMcastControl,'hwifPpsBcastDisValControl':hwifPpsBcastDisValControl,'hwifUniSuppressionStep':hwifUniSuppressionStep,'hwifPpsUniSuppressionMax':hwifPpsUniSuppressionMax,'hwifMulSuppressionStep':hwifMulSuppressionStep,'hwifPpsMulSuppressionMax':hwifPpsMulSuppressionMax,'hwifUniSuppression':hwifUniSuppression,'hwifPpsUniSuppression':hwifPpsUniSuppression,'hwifMulSuppression':hwifMulSuppression,'hwifPpsMulSuppression':hwifPpsMulSuppression,'hwifComboActivePort':hwifComboActivePort,'hwifBMbpsMulSuppressionMax':hwifBMbpsMulSuppressionMax,'hwifBMbpsMulSuppression':hwifBMbpsMulSuppression,'hwifBKbpsMulSuppressionMax':hwifBKbpsMulSuppressionMax,'hwifBKbpsMulSuppressionStep':hwifBKbpsMulSuppressionStep,'hwifBKbpsMulSuppression':hwifBKbpsMulSuppression,'hwifUnknownPacketDropMul':hwifUnknownPacketDropMul,'hwifUnknownPacketDropUni':hwifUnknownPacketDropUni,'hwifBMbpsUniSuppressionMax':hwifBMbpsUniSuppressionMax,'hwifBMbpsUniSuppression':hwifBMbpsUniSuppression,'hwifBKbpsUniSuppressionMax':hwifBKbpsUniSuppressionMax,'hwifBKbpsUniSuppressionStep':hwifBKbpsUniSuppressionStep,'hwifBKbpsUniSuppression':hwifBKbpsUniSuppression,'hwifOutPayloadOctets':hwifOutPayloadOctets,'hwifInPayloadOctets':hwifInPayloadOctets,'hwifInErrorPktsRate':hwifInErrorPktsRate,'hwifInPkts':hwifInPkts,'hwifInNormalPkts':hwifInNormalPkts,'hwifOutPkts':hwifOutPkts,'hwifAggregateTable':hwifAggregateTable,'hwifAggregateEntry':hwifAggregateEntry,_S:hwifAggregatePortIndex,'hwifAggregatePortName':hwifAggregatePortName,'hwifAggregatePortListPorts':hwifAggregatePortListPorts,'hwifAggregateModel':hwifAggregateModel,'hwifAggregateOperStatus':hwifAggregateOperStatus,'hwifHybridPortTable':hwifHybridPortTable,'hwifHybridPortEntry':hwifHybridPortEntry,_T:hwifHybridPortIndex,'hwifHybridTaggedVlanListLow':hwifHybridTaggedVlanListLow,'hwifHybridTaggedVlanListHigh':hwifHybridTaggedVlanListHigh,'hwifHybridUnTaggedVlanListLow':hwifHybridUnTaggedVlanListLow,'hwifHybridUnTaggedVlanListHigh':hwifHybridUnTaggedVlanListHigh,'hwifComboPortTable':hwifComboPortTable,'hwifComboPortEntry':hwifComboPortEntry,_U:hwifComboPortIndex,'hwifComboPortCurActive':hwifComboPortCurActive,'hwLswL2InfMib':hwLswL2InfMib,'hwLswL2InfMibObject':hwLswL2InfMibObject,'hwSlotPortMax':hwSlotPortMax,'hwSwitchPortMax':hwSwitchPortMax,'hwifVLANTrunkStatusTable':hwifVLANTrunkStatusTable,'hwifVLANTrunkStatusEntry':hwifVLANTrunkStatusEntry,_V:hwifVLANTrunkIndex,'hwifVLANTrunkGvrpRegistration':hwifVLANTrunkGvrpRegistration,'hwifVLANTrunkPassListLow':hwifVLANTrunkPassListLow,'hwifVLANTrunkPassListHigh':hwifVLANTrunkPassListHigh,'hwifVLANTrunkAllowListLow':hwifVLANTrunkAllowListLow,'hwifVLANTrunkAllowListHigh':hwifVLANTrunkAllowListHigh,'hwethernetTable':hwethernetTable,_Y:hwethernetEntry,'hwifEthernetDuplex':hwifEthernetDuplex,'hwifEthernetMTU':hwifEthernetMTU,'hwifEthernetSpeed':hwifEthernetSpeed,'hwifEthernetMdi':hwifEthernetMdi,'hwMaxMacLearn':hwMaxMacLearn,'hwifMacAddressLearn':hwifMacAddressLearn,'hwifEthernetTest':hwifEthernetTest,'hwifMacAddrLearnMode':hwifMacAddrLearnMode,'hwifEthernetFlowInterval':hwifEthernetFlowInterval,'hwifEthernetIsolate':hwifEthernetIsolate,'hwifVlanVPNStatus':hwifVlanVPNStatus,'hwifVlanVPNUplinkStatus':hwifVlanVPNUplinkStatus,'hwifVlanVPNTPID':hwifVlanVPNTPID,'hwifIsolateGroupID':hwifIsolateGroupID,'hwifisUplinkPort':hwifisUplinkPort,'hwifEthernetAutoSpeedMask':hwifEthernetAutoSpeedMask,'hwifEthernetAutoSpeed':hwifEthernetAutoSpeed,'hwIsolateGroupMax':hwIsolateGroupMax,'hwGlobalBroadcastMaxPps':hwGlobalBroadcastMaxPps,'hwGlobalBroadcastMaxRatio':hwGlobalBroadcastMaxRatio,'hwBpduTunnelStatus':hwBpduTunnelStatus,'hwVlanVPNTPIDMode':hwVlanVPNTPIDMode,'hwVlanVPNTPID':hwVlanVPNTPID,'hwPortIsolateGroupTable':hwPortIsolateGroupTable,'hwPortIsolateGroupEntry':hwPortIsolateGroupEntry,_W:hwPortIsolateGroupIndex,'hwPortIsolateUplinkIfIndex':hwPortIsolateUplinkIfIndex,'hwPortIsolateGroupRowStatus':hwPortIsolateGroupRowStatus,'hwPortIsolateGroupDescription':hwPortIsolateGroupDescription,'hwMaxMacLearnRange':hwMaxMacLearnRange})