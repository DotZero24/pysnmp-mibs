_J='hpnicfPwVcIndex'
_I='TruthValue'
_H='read-only'
_G='Integer32'
_F='read-create'
_E='hpnicfPwVcPeerAddr'
_D='hpnicfPwVcType'
_C='hpnicfPwVcID'
_B='current'
_A='HPN-ICF-L2VPN-PWE3-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_I)
hpnicfL2VpnPwe3=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,78))
class HpnicfL2VpnVcEncapsType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,64,255)));namedValues=NamedValues(*(('frameRelayDlciMartini',1),('atmAal5SduVccTransport',2),('atmTransparentCellTransport',3),('ethernetTagged',4),('ethernet',5),('hdlc',6),('ppp',7),('cem',8),('atmN2OneVccCellTransport',9),('atmN2OneVpcCellTransport',10),('ipLayer2Transport',11),('atmOne2OneVccCellMode',12),('atmOne2OneVpcCellMode',13),('atmAal5PduVccTransport',14),('frameRelayPortMode',15),('cep',16),('saE1oP',17),('saT1oP',18),('saE3oP',19),('saT3oP',20),('cESoPsnBasicMode',21),('tDMoIPbasicMode',22),('l2VpnCESoPSNTDMwithCAS',23),('l2VpnTDMoIPTDMwithCAS',24),('frameRelayDlci',25),('ipInterworking',64),('unknown',255)))
_HpnicfL2VpnPwe3ScalarGroup_ObjectIdentity=ObjectIdentity
hpnicfL2VpnPwe3ScalarGroup=_HpnicfL2VpnPwe3ScalarGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,78,1))
class _HpnicfPwVcTrapOpen_Type(TruthValue):defaultValue=2
_HpnicfPwVcTrapOpen_Type.__name__=_I
_HpnicfPwVcTrapOpen_Object=MibScalar
hpnicfPwVcTrapOpen=_HpnicfPwVcTrapOpen_Object((1,3,6,1,4,1,11,2,14,11,15,2,78,1,1),_HpnicfPwVcTrapOpen_Type())
hpnicfPwVcTrapOpen.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfPwVcTrapOpen.setStatus(_B)
_HpnicfL2VpnPwe3Table_ObjectIdentity=ObjectIdentity
hpnicfL2VpnPwe3Table=_HpnicfL2VpnPwe3Table_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,78,2))
_HpnicfPwVcTable_Object=MibTable
hpnicfPwVcTable=_HpnicfPwVcTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,78,2,1))
if mibBuilder.loadTexts:hpnicfPwVcTable.setStatus(_B)
_HpnicfPwVcEntry_Object=MibTableRow
hpnicfPwVcEntry=_HpnicfPwVcEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,78,2,1,1))
hpnicfPwVcEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:hpnicfPwVcEntry.setStatus(_B)
_HpnicfPwVcIndex_Type=Integer32
_HpnicfPwVcIndex_Object=MibTableColumn
hpnicfPwVcIndex=_HpnicfPwVcIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,78,2,1,1,1),_HpnicfPwVcIndex_Type())
hpnicfPwVcIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicfPwVcIndex.setStatus(_B)
_HpnicfPwVcID_Type=Unsigned32
_HpnicfPwVcID_Object=MibTableColumn
hpnicfPwVcID=_HpnicfPwVcID_Object((1,3,6,1,4,1,11,2,14,11,15,2,78,2,1,1,2),_HpnicfPwVcID_Type())
hpnicfPwVcID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPwVcID.setStatus(_B)
_HpnicfPwVcType_Type=HpnicfL2VpnVcEncapsType
_HpnicfPwVcType_Object=MibTableColumn
hpnicfPwVcType=_HpnicfPwVcType_Object((1,3,6,1,4,1,11,2,14,11,15,2,78,2,1,1,3),_HpnicfPwVcType_Type())
hpnicfPwVcType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPwVcType.setStatus(_B)
_HpnicfPwVcPeerAddr_Type=IpAddress
_HpnicfPwVcPeerAddr_Object=MibTableColumn
hpnicfPwVcPeerAddr=_HpnicfPwVcPeerAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,78,2,1,1,4),_HpnicfPwVcPeerAddr_Type())
hpnicfPwVcPeerAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPwVcPeerAddr.setStatus(_B)
_HpnicfPwVcMtu_Type=Unsigned32
_HpnicfPwVcMtu_Object=MibTableColumn
hpnicfPwVcMtu=_HpnicfPwVcMtu_Object((1,3,6,1,4,1,11,2,14,11,15,2,78,2,1,1,5),_HpnicfPwVcMtu_Type())
hpnicfPwVcMtu.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPwVcMtu.setStatus(_B)
class _HpnicfPwVcCfgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('backup',2),('multiPort',3)))
_HpnicfPwVcCfgType_Type.__name__=_G
_HpnicfPwVcCfgType_Object=MibTableColumn
hpnicfPwVcCfgType=_HpnicfPwVcCfgType_Object((1,3,6,1,4,1,11,2,14,11,15,2,78,2,1,1,6),_HpnicfPwVcCfgType_Type())
hpnicfPwVcCfgType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPwVcCfgType.setStatus(_B)
_HpnicfPwVcInboundLabel_Type=Unsigned32
_HpnicfPwVcInboundLabel_Object=MibTableColumn
hpnicfPwVcInboundLabel=_HpnicfPwVcInboundLabel_Object((1,3,6,1,4,1,11,2,14,11,15,2,78,2,1,1,7),_HpnicfPwVcInboundLabel_Type())
hpnicfPwVcInboundLabel.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfPwVcInboundLabel.setStatus(_B)
_HpnicfPwVcOutboundLabel_Type=Unsigned32
_HpnicfPwVcOutboundLabel_Object=MibTableColumn
hpnicfPwVcOutboundLabel=_HpnicfPwVcOutboundLabel_Object((1,3,6,1,4,1,11,2,14,11,15,2,78,2,1,1,8),_HpnicfPwVcOutboundLabel_Type())
hpnicfPwVcOutboundLabel.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfPwVcOutboundLabel.setStatus(_B)
_HpnicfPwVcIfIndex_Type=Unsigned32
_HpnicfPwVcIfIndex_Object=MibTableColumn
hpnicfPwVcIfIndex=_HpnicfPwVcIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,78,2,1,1,9),_HpnicfPwVcIfIndex_Type())
hpnicfPwVcIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPwVcIfIndex.setStatus(_B)
class _HpnicfPwVcAcStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
_HpnicfPwVcAcStatus_Type.__name__=_G
_HpnicfPwVcAcStatus_Object=MibTableColumn
hpnicfPwVcAcStatus=_HpnicfPwVcAcStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,78,2,1,1,10),_HpnicfPwVcAcStatus_Type())
hpnicfPwVcAcStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfPwVcAcStatus.setStatus(_B)
class _HpnicfPwVcStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
_HpnicfPwVcStatus_Type.__name__=_G
_HpnicfPwVcStatus_Object=MibTableColumn
hpnicfPwVcStatus=_HpnicfPwVcStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,78,2,1,1,11),_HpnicfPwVcStatus_Type())
hpnicfPwVcStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfPwVcStatus.setStatus(_B)
_HpnicfPwVcRowStatus_Type=RowStatus
_HpnicfPwVcRowStatus_Object=MibTableColumn
hpnicfPwVcRowStatus=_HpnicfPwVcRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,78,2,1,1,12),_HpnicfPwVcRowStatus_Type())
hpnicfPwVcRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPwVcRowStatus.setStatus(_B)
_HpnicfL2VpnPwe3Notifications_ObjectIdentity=ObjectIdentity
hpnicfL2VpnPwe3Notifications=_HpnicfL2VpnPwe3Notifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,78,3))
hpnicfPwVcSwitchWtoP=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,78,3,1))
hpnicfPwVcSwitchWtoP.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:hpnicfPwVcSwitchWtoP.setStatus(_B)
hpnicfPwVcSwitchPtoW=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,78,3,2))
hpnicfPwVcSwitchPtoW.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:hpnicfPwVcSwitchPtoW.setStatus(_B)
hpnicfPwVcDown=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,78,3,3))
hpnicfPwVcDown.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:hpnicfPwVcDown.setStatus(_B)
hpnicfPwVcUp=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,78,3,4))
hpnicfPwVcUp.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:hpnicfPwVcUp.setStatus(_B)
hpnicfPwVcDeleted=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,78,3,5))
hpnicfPwVcDeleted.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:hpnicfPwVcDeleted.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'HpnicfL2VpnVcEncapsType':HpnicfL2VpnVcEncapsType,'hpnicfL2VpnPwe3':hpnicfL2VpnPwe3,'hpnicfL2VpnPwe3ScalarGroup':hpnicfL2VpnPwe3ScalarGroup,'hpnicfPwVcTrapOpen':hpnicfPwVcTrapOpen,'hpnicfL2VpnPwe3Table':hpnicfL2VpnPwe3Table,'hpnicfPwVcTable':hpnicfPwVcTable,'hpnicfPwVcEntry':hpnicfPwVcEntry,_J:hpnicfPwVcIndex,_C:hpnicfPwVcID,_D:hpnicfPwVcType,_E:hpnicfPwVcPeerAddr,'hpnicfPwVcMtu':hpnicfPwVcMtu,'hpnicfPwVcCfgType':hpnicfPwVcCfgType,'hpnicfPwVcInboundLabel':hpnicfPwVcInboundLabel,'hpnicfPwVcOutboundLabel':hpnicfPwVcOutboundLabel,'hpnicfPwVcIfIndex':hpnicfPwVcIfIndex,'hpnicfPwVcAcStatus':hpnicfPwVcAcStatus,'hpnicfPwVcStatus':hpnicfPwVcStatus,'hpnicfPwVcRowStatus':hpnicfPwVcRowStatus,'hpnicfL2VpnPwe3Notifications':hpnicfL2VpnPwe3Notifications,'hpnicfPwVcSwitchWtoP':hpnicfPwVcSwitchWtoP,'hpnicfPwVcSwitchPtoW':hpnicfPwVcSwitchPtoW,'hpnicfPwVcDown':hpnicfPwVcDown,'hpnicfPwVcUp':hpnicfPwVcUp,'hpnicfPwVcDeleted':hpnicfPwVcDeleted})