_J='h3cPwVcIndex'
_I='TruthValue'
_H='read-only'
_G='Integer32'
_F='read-create'
_E='h3cPwVcPeerAddr'
_D='h3cPwVcType'
_C='h3cPwVcID'
_B='current'
_A='A3COM-HUAWEI-L2VPN-PWE3-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_I)
h3cL2VpnPwe3=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,78))
class H3cL2VpnVcEncapsType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,64,255)));namedValues=NamedValues(*(('frameRelayDlciMartini',1),('atmAal5SduVccTransport',2),('atmTransparentCellTransport',3),('ethernetTagged',4),('ethernet',5),('hdlc',6),('ppp',7),('cem',8),('atmN2OneVccCellTransport',9),('atmN2OneVpcCellTransport',10),('ipLayer2Transport',11),('atmOne2OneVccCellMode',12),('atmOne2OneVpcCellMode',13),('atmAal5PduVccTransport',14),('frameRelayPortMode',15),('cep',16),('saE1oP',17),('saT1oP',18),('saE3oP',19),('saT3oP',20),('cESoPsnBasicMode',21),('tDMoIPbasicMode',22),('l2VpnCESoPSNTDMwithCAS',23),('l2VpnTDMoIPTDMwithCAS',24),('frameRelayDlci',25),('ipInterworking',64),('unknown',255)))
_H3cL2VpnPwe3ScalarGroup_ObjectIdentity=ObjectIdentity
h3cL2VpnPwe3ScalarGroup=_H3cL2VpnPwe3ScalarGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,78,1))
class _H3cPwVcTrapOpen_Type(TruthValue):defaultValue=2
_H3cPwVcTrapOpen_Type.__name__=_I
_H3cPwVcTrapOpen_Object=MibScalar
h3cPwVcTrapOpen=_H3cPwVcTrapOpen_Object((1,3,6,1,4,1,43,45,1,10,2,78,1,1),_H3cPwVcTrapOpen_Type())
h3cPwVcTrapOpen.setMaxAccess('read-write')
if mibBuilder.loadTexts:h3cPwVcTrapOpen.setStatus(_B)
_H3cL2VpnPwe3Table_ObjectIdentity=ObjectIdentity
h3cL2VpnPwe3Table=_H3cL2VpnPwe3Table_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,78,2))
_H3cPwVcTable_Object=MibTable
h3cPwVcTable=_H3cPwVcTable_Object((1,3,6,1,4,1,43,45,1,10,2,78,2,1))
if mibBuilder.loadTexts:h3cPwVcTable.setStatus(_B)
_H3cPwVcEntry_Object=MibTableRow
h3cPwVcEntry=_H3cPwVcEntry_Object((1,3,6,1,4,1,43,45,1,10,2,78,2,1,1))
h3cPwVcEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:h3cPwVcEntry.setStatus(_B)
_H3cPwVcIndex_Type=Integer32
_H3cPwVcIndex_Object=MibTableColumn
h3cPwVcIndex=_H3cPwVcIndex_Object((1,3,6,1,4,1,43,45,1,10,2,78,2,1,1,1),_H3cPwVcIndex_Type())
h3cPwVcIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cPwVcIndex.setStatus(_B)
_H3cPwVcID_Type=Unsigned32
_H3cPwVcID_Object=MibTableColumn
h3cPwVcID=_H3cPwVcID_Object((1,3,6,1,4,1,43,45,1,10,2,78,2,1,1,2),_H3cPwVcID_Type())
h3cPwVcID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cPwVcID.setStatus(_B)
_H3cPwVcType_Type=H3cL2VpnVcEncapsType
_H3cPwVcType_Object=MibTableColumn
h3cPwVcType=_H3cPwVcType_Object((1,3,6,1,4,1,43,45,1,10,2,78,2,1,1,3),_H3cPwVcType_Type())
h3cPwVcType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cPwVcType.setStatus(_B)
_H3cPwVcPeerAddr_Type=IpAddress
_H3cPwVcPeerAddr_Object=MibTableColumn
h3cPwVcPeerAddr=_H3cPwVcPeerAddr_Object((1,3,6,1,4,1,43,45,1,10,2,78,2,1,1,4),_H3cPwVcPeerAddr_Type())
h3cPwVcPeerAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cPwVcPeerAddr.setStatus(_B)
_H3cPwVcMtu_Type=Unsigned32
_H3cPwVcMtu_Object=MibTableColumn
h3cPwVcMtu=_H3cPwVcMtu_Object((1,3,6,1,4,1,43,45,1,10,2,78,2,1,1,5),_H3cPwVcMtu_Type())
h3cPwVcMtu.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cPwVcMtu.setStatus(_B)
class _HwPwVcCfgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('backup',2),('multiPort',3)))
_HwPwVcCfgType_Type.__name__=_G
_HwPwVcCfgType_Object=MibTableColumn
hwPwVcCfgType=_HwPwVcCfgType_Object((1,3,6,1,4,1,43,45,1,10,2,78,2,1,1,6),_HwPwVcCfgType_Type())
hwPwVcCfgType.setMaxAccess(_F)
if mibBuilder.loadTexts:hwPwVcCfgType.setStatus(_B)
_H3cPwVcInboundLabel_Type=Unsigned32
_H3cPwVcInboundLabel_Object=MibTableColumn
h3cPwVcInboundLabel=_H3cPwVcInboundLabel_Object((1,3,6,1,4,1,43,45,1,10,2,78,2,1,1,7),_H3cPwVcInboundLabel_Type())
h3cPwVcInboundLabel.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cPwVcInboundLabel.setStatus(_B)
_H3cPwVcOutboundLabel_Type=Unsigned32
_H3cPwVcOutboundLabel_Object=MibTableColumn
h3cPwVcOutboundLabel=_H3cPwVcOutboundLabel_Object((1,3,6,1,4,1,43,45,1,10,2,78,2,1,1,8),_H3cPwVcOutboundLabel_Type())
h3cPwVcOutboundLabel.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cPwVcOutboundLabel.setStatus(_B)
_H3cPwVcIfIndex_Type=Unsigned32
_H3cPwVcIfIndex_Object=MibTableColumn
h3cPwVcIfIndex=_H3cPwVcIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,78,2,1,1,9),_H3cPwVcIfIndex_Type())
h3cPwVcIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cPwVcIfIndex.setStatus(_B)
class _H3cPwVcAcStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
_H3cPwVcAcStatus_Type.__name__=_G
_H3cPwVcAcStatus_Object=MibTableColumn
h3cPwVcAcStatus=_H3cPwVcAcStatus_Object((1,3,6,1,4,1,43,45,1,10,2,78,2,1,1,10),_H3cPwVcAcStatus_Type())
h3cPwVcAcStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cPwVcAcStatus.setStatus(_B)
class _H3cPwVcStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
_H3cPwVcStatus_Type.__name__=_G
_H3cPwVcStatus_Object=MibTableColumn
h3cPwVcStatus=_H3cPwVcStatus_Object((1,3,6,1,4,1,43,45,1,10,2,78,2,1,1,11),_H3cPwVcStatus_Type())
h3cPwVcStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cPwVcStatus.setStatus(_B)
_H3cPwVcRowStatus_Type=RowStatus
_H3cPwVcRowStatus_Object=MibTableColumn
h3cPwVcRowStatus=_H3cPwVcRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,78,2,1,1,12),_H3cPwVcRowStatus_Type())
h3cPwVcRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cPwVcRowStatus.setStatus(_B)
_H3cL2VpnPwe3Notifications_ObjectIdentity=ObjectIdentity
h3cL2VpnPwe3Notifications=_H3cL2VpnPwe3Notifications_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,78,3))
h3cPwVcSwitchWtoP=NotificationType((1,3,6,1,4,1,43,45,1,10,2,78,3,1))
h3cPwVcSwitchWtoP.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:h3cPwVcSwitchWtoP.setStatus(_B)
h3cPwVcSwitchPtoW=NotificationType((1,3,6,1,4,1,43,45,1,10,2,78,3,2))
h3cPwVcSwitchPtoW.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:h3cPwVcSwitchPtoW.setStatus(_B)
h3cPwVcDown=NotificationType((1,3,6,1,4,1,43,45,1,10,2,78,3,3))
h3cPwVcDown.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:h3cPwVcDown.setStatus(_B)
h3cPwVcUp=NotificationType((1,3,6,1,4,1,43,45,1,10,2,78,3,4))
h3cPwVcUp.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:h3cPwVcUp.setStatus(_B)
h3cPwVcDeleted=NotificationType((1,3,6,1,4,1,43,45,1,10,2,78,3,5))
h3cPwVcDeleted.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:h3cPwVcDeleted.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'H3cL2VpnVcEncapsType':H3cL2VpnVcEncapsType,'h3cL2VpnPwe3':h3cL2VpnPwe3,'h3cL2VpnPwe3ScalarGroup':h3cL2VpnPwe3ScalarGroup,'h3cPwVcTrapOpen':h3cPwVcTrapOpen,'h3cL2VpnPwe3Table':h3cL2VpnPwe3Table,'h3cPwVcTable':h3cPwVcTable,'h3cPwVcEntry':h3cPwVcEntry,_J:h3cPwVcIndex,_C:h3cPwVcID,_D:h3cPwVcType,_E:h3cPwVcPeerAddr,'h3cPwVcMtu':h3cPwVcMtu,'hwPwVcCfgType':hwPwVcCfgType,'h3cPwVcInboundLabel':h3cPwVcInboundLabel,'h3cPwVcOutboundLabel':h3cPwVcOutboundLabel,'h3cPwVcIfIndex':h3cPwVcIfIndex,'h3cPwVcAcStatus':h3cPwVcAcStatus,'h3cPwVcStatus':h3cPwVcStatus,'h3cPwVcRowStatus':h3cPwVcRowStatus,'h3cL2VpnPwe3Notifications':h3cL2VpnPwe3Notifications,'h3cPwVcSwitchWtoP':h3cPwVcSwitchWtoP,'h3cPwVcSwitchPtoW':h3cPwVcSwitchPtoW,'h3cPwVcDown':h3cPwVcDown,'h3cPwVcUp':h3cPwVcUp,'h3cPwVcDeleted':h3cPwVcDeleted})