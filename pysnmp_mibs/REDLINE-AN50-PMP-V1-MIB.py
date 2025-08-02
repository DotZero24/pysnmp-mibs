_G='OctetString'
_F='an50pmpLinkID'
_E='REDLINE-AN50-PMP-V1-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
_Redline_ObjectIdentity=ObjectIdentity
redline=_Redline_ObjectIdentity((1,3,6,1,4,1,10728))
_RedlineProducts_ObjectIdentity=ObjectIdentity
redlineProducts=_RedlineProducts_ObjectIdentity((1,3,6,1,4,1,10728,1))
_RedlineAN50_ObjectIdentity=ObjectIdentity
redlineAN50=_RedlineAN50_ObjectIdentity((1,3,6,1,4,1,10728,1,1))
_RedlineMgmt_ObjectIdentity=ObjectIdentity
redlineMgmt=_RedlineMgmt_ObjectIdentity((1,3,6,1,4,1,10728,2))
_RedlineAN50PMPV1_ObjectIdentity=ObjectIdentity
redlineAN50PMPV1=_RedlineAN50PMPV1_ObjectIdentity((1,3,6,1,4,1,10728,2,51))
_An50pmpLinkTable_Object=MibTable
an50pmpLinkTable=_An50pmpLinkTable_Object((1,3,6,1,4,1,10728,2,51,1))
if mibBuilder.loadTexts:an50pmpLinkTable.setStatus(_A)
_An50pmpLinkEntry_Object=MibTableRow
an50pmpLinkEntry=_An50pmpLinkEntry_Object((1,3,6,1,4,1,10728,2,51,1,1))
an50pmpLinkEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:an50pmpLinkEntry.setStatus(_A)
class _An50pmpLinkID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_An50pmpLinkID_Type.__name__=_C
_An50pmpLinkID_Object=MibTableColumn
an50pmpLinkID=_An50pmpLinkID_Object((1,3,6,1,4,1,10728,2,51,1,1,1),_An50pmpLinkID_Type())
an50pmpLinkID.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkID.setStatus(_A)
class _An50pmpLinkName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_An50pmpLinkName_Type.__name__=_G
_An50pmpLinkName_Object=MibTableColumn
an50pmpLinkName=_An50pmpLinkName_Object((1,3,6,1,4,1,10728,2,51,1,1,2),_An50pmpLinkName_Type())
an50pmpLinkName.setMaxAccess(_D)
if mibBuilder.loadTexts:an50pmpLinkName.setStatus(_A)
class _An50pmpLinkGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_An50pmpLinkGroupID_Type.__name__=_C
_An50pmpLinkGroupID_Object=MibTableColumn
an50pmpLinkGroupID=_An50pmpLinkGroupID_Object((1,3,6,1,4,1,10728,2,51,1,1,3),_An50pmpLinkGroupID_Type())
an50pmpLinkGroupID.setMaxAccess(_D)
if mibBuilder.loadTexts:an50pmpLinkGroupID.setStatus(_A)
_An50pmpLinkPeerMac_Type=OctetString
_An50pmpLinkPeerMac_Object=MibTableColumn
an50pmpLinkPeerMac=_An50pmpLinkPeerMac_Object((1,3,6,1,4,1,10728,2,51,1,1,4),_An50pmpLinkPeerMac_Type())
an50pmpLinkPeerMac.setMaxAccess(_D)
if mibBuilder.loadTexts:an50pmpLinkPeerMac.setStatus(_A)
class _An50pmpLinkMaxDLBurstRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_An50pmpLinkMaxDLBurstRate_Type.__name__=_C
_An50pmpLinkMaxDLBurstRate_Object=MibTableColumn
an50pmpLinkMaxDLBurstRate=_An50pmpLinkMaxDLBurstRate_Object((1,3,6,1,4,1,10728,2,51,1,1,5),_An50pmpLinkMaxDLBurstRate_Type())
an50pmpLinkMaxDLBurstRate.setMaxAccess(_D)
if mibBuilder.loadTexts:an50pmpLinkMaxDLBurstRate.setStatus(_A)
class _An50pmpLinkMaxULBurstRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_An50pmpLinkMaxULBurstRate_Type.__name__=_C
_An50pmpLinkMaxULBurstRate_Object=MibTableColumn
an50pmpLinkMaxULBurstRate=_An50pmpLinkMaxULBurstRate_Object((1,3,6,1,4,1,10728,2,51,1,1,6),_An50pmpLinkMaxULBurstRate_Type())
an50pmpLinkMaxULBurstRate.setMaxAccess(_D)
if mibBuilder.loadTexts:an50pmpLinkMaxULBurstRate.setStatus(_A)
_An50pmpLinkMaxHost_Type=Integer32
_An50pmpLinkMaxHost_Object=MibTableColumn
an50pmpLinkMaxHost=_An50pmpLinkMaxHost_Object((1,3,6,1,4,1,10728,2,51,1,1,7),_An50pmpLinkMaxHost_Type())
an50pmpLinkMaxHost.setMaxAccess(_D)
if mibBuilder.loadTexts:an50pmpLinkMaxHost.setStatus(_A)
class _An50pmpLinkCIDDLCIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_An50pmpLinkCIDDLCIR_Type.__name__=_C
_An50pmpLinkCIDDLCIR_Object=MibTableColumn
an50pmpLinkCIDDLCIR=_An50pmpLinkCIDDLCIR_Object((1,3,6,1,4,1,10728,2,51,1,1,8),_An50pmpLinkCIDDLCIR_Type())
an50pmpLinkCIDDLCIR.setMaxAccess(_D)
if mibBuilder.loadTexts:an50pmpLinkCIDDLCIR.setStatus(_A)
class _An50pmpLinkCIDDLPIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_An50pmpLinkCIDDLPIR_Type.__name__=_C
_An50pmpLinkCIDDLPIR_Object=MibTableColumn
an50pmpLinkCIDDLPIR=_An50pmpLinkCIDDLPIR_Object((1,3,6,1,4,1,10728,2,51,1,1,9),_An50pmpLinkCIDDLPIR_Type())
an50pmpLinkCIDDLPIR.setMaxAccess(_D)
if mibBuilder.loadTexts:an50pmpLinkCIDDLPIR.setStatus(_A)
class _An50pmpLinkCIDULCIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_An50pmpLinkCIDULCIR_Type.__name__=_C
_An50pmpLinkCIDULCIR_Object=MibTableColumn
an50pmpLinkCIDULCIR=_An50pmpLinkCIDULCIR_Object((1,3,6,1,4,1,10728,2,51,1,1,10),_An50pmpLinkCIDULCIR_Type())
an50pmpLinkCIDULCIR.setMaxAccess(_D)
if mibBuilder.loadTexts:an50pmpLinkCIDULCIR.setStatus(_A)
class _An50pmpLinkCIDULPIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_An50pmpLinkCIDULPIR_Type.__name__=_C
_An50pmpLinkCIDULPIR_Object=MibTableColumn
an50pmpLinkCIDULPIR=_An50pmpLinkCIDULPIR_Object((1,3,6,1,4,1,10728,2,51,1,1,11),_An50pmpLinkCIDULPIR_Type())
an50pmpLinkCIDULPIR.setMaxAccess(_D)
if mibBuilder.loadTexts:an50pmpLinkCIDULPIR.setStatus(_A)
class _An50pmpLinkDLQoS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,54))
_An50pmpLinkDLQoS_Type.__name__=_C
_An50pmpLinkDLQoS_Object=MibTableColumn
an50pmpLinkDLQoS=_An50pmpLinkDLQoS_Object((1,3,6,1,4,1,10728,2,51,1,1,12),_An50pmpLinkDLQoS_Type())
an50pmpLinkDLQoS.setMaxAccess(_D)
if mibBuilder.loadTexts:an50pmpLinkDLQoS.setStatus(_A)
class _An50pmpLinkULQoS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,54))
_An50pmpLinkULQoS_Type.__name__=_C
_An50pmpLinkULQoS_Object=MibTableColumn
an50pmpLinkULQoS=_An50pmpLinkULQoS_Object((1,3,6,1,4,1,10728,2,51,1,1,13),_An50pmpLinkULQoS_Type())
an50pmpLinkULQoS.setMaxAccess(_D)
if mibBuilder.loadTexts:an50pmpLinkULQoS.setStatus(_A)
_An50pmpLinkRowStatus_Type=RowStatus
_An50pmpLinkRowStatus_Object=MibTableColumn
an50pmpLinkRowStatus=_An50pmpLinkRowStatus_Object((1,3,6,1,4,1,10728,2,51,1,1,14),_An50pmpLinkRowStatus_Type())
an50pmpLinkRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:an50pmpLinkRowStatus.setStatus(_A)
_An50pmpLinkStatusTable_Object=MibTable
an50pmpLinkStatusTable=_An50pmpLinkStatusTable_Object((1,3,6,1,4,1,10728,2,51,2))
if mibBuilder.loadTexts:an50pmpLinkStatusTable.setStatus(_A)
_An50pmpLinkStatusEntry_Object=MibTableRow
an50pmpLinkStatusEntry=_An50pmpLinkStatusEntry_Object((1,3,6,1,4,1,10728,2,51,2,1))
an50pmpLinkStatusEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:an50pmpLinkStatusEntry.setStatus(_A)
class _An50pmpLinkStatusID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_An50pmpLinkStatusID_Type.__name__=_C
_An50pmpLinkStatusID_Object=MibTableColumn
an50pmpLinkStatusID=_An50pmpLinkStatusID_Object((1,3,6,1,4,1,10728,2,51,2,1,1),_An50pmpLinkStatusID_Type())
an50pmpLinkStatusID.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkStatusID.setStatus(_A)
class _An50pmpLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_An50pmpLinkStatus_Type.__name__=_C
_An50pmpLinkStatus_Object=MibTableColumn
an50pmpLinkStatus=_An50pmpLinkStatus_Object((1,3,6,1,4,1,10728,2,51,2,1,2),_An50pmpLinkStatus_Type())
an50pmpLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkStatus.setStatus(_A)
_An50pmpLinkStatusCode_Type=Integer32
_An50pmpLinkStatusCode_Object=MibTableColumn
an50pmpLinkStatusCode=_An50pmpLinkStatusCode_Object((1,3,6,1,4,1,10728,2,51,2,1,3),_An50pmpLinkStatusCode_Type())
an50pmpLinkStatusCode.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkStatusCode.setStatus(_A)
class _An50pmpLinkRegConn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_An50pmpLinkRegConn_Type.__name__=_C
_An50pmpLinkRegConn_Object=MibTableColumn
an50pmpLinkRegConn=_An50pmpLinkRegConn_Object((1,3,6,1,4,1,10728,2,51,2,1,4),_An50pmpLinkRegConn_Type())
an50pmpLinkRegConn.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkRegConn.setStatus(_A)
class _An50pmpLinkDLBurstRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_An50pmpLinkDLBurstRate_Type.__name__=_C
_An50pmpLinkDLBurstRate_Object=MibTableColumn
an50pmpLinkDLBurstRate=_An50pmpLinkDLBurstRate_Object((1,3,6,1,4,1,10728,2,51,2,1,5),_An50pmpLinkDLBurstRate_Type())
an50pmpLinkDLBurstRate.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkDLBurstRate.setStatus(_A)
_An50pmpLinkDLRSSI_Type=Integer32
_An50pmpLinkDLRSSI_Object=MibTableColumn
an50pmpLinkDLRSSI=_An50pmpLinkDLRSSI_Object((1,3,6,1,4,1,10728,2,51,2,1,6),_An50pmpLinkDLRSSI_Type())
an50pmpLinkDLRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkDLRSSI.setStatus(_A)
_An50pmpLinkDLSINADR_Type=Integer32
_An50pmpLinkDLSINADR_Object=MibTableColumn
an50pmpLinkDLSINADR=_An50pmpLinkDLSINADR_Object((1,3,6,1,4,1,10728,2,51,2,1,7),_An50pmpLinkDLSINADR_Type())
an50pmpLinkDLSINADR.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkDLSINADR.setStatus(_A)
_An50pmpLinkDLStatLostFrm_Type=Integer32
_An50pmpLinkDLStatLostFrm_Object=MibTableColumn
an50pmpLinkDLStatLostFrm=_An50pmpLinkDLStatLostFrm_Object((1,3,6,1,4,1,10728,2,51,2,1,8),_An50pmpLinkDLStatLostFrm_Type())
an50pmpLinkDLStatLostFrm.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkDLStatLostFrm.setStatus(_A)
_An50pmpLinkDLStatBlksTot_Type=Integer32
_An50pmpLinkDLStatBlksTot_Object=MibTableColumn
an50pmpLinkDLStatBlksTot=_An50pmpLinkDLStatBlksTot_Object((1,3,6,1,4,1,10728,2,51,2,1,9),_An50pmpLinkDLStatBlksTot_Type())
an50pmpLinkDLStatBlksTot.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkDLStatBlksTot.setStatus(_A)
_An50pmpLinkDLStatBlksRetr_Type=Integer32
_An50pmpLinkDLStatBlksRetr_Object=MibTableColumn
an50pmpLinkDLStatBlksRetr=_An50pmpLinkDLStatBlksRetr_Object((1,3,6,1,4,1,10728,2,51,2,1,10),_An50pmpLinkDLStatBlksRetr_Type())
an50pmpLinkDLStatBlksRetr.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkDLStatBlksRetr.setStatus(_A)
_An50pmpLinkDLStatBlksDisc_Type=Integer32
_An50pmpLinkDLStatBlksDisc_Object=MibTableColumn
an50pmpLinkDLStatBlksDisc=_An50pmpLinkDLStatBlksDisc_Object((1,3,6,1,4,1,10728,2,51,2,1,11),_An50pmpLinkDLStatBlksDisc_Type())
an50pmpLinkDLStatBlksDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkDLStatBlksDisc.setStatus(_A)
_An50pmpLinkDLCIDStatPktDisc_Type=Integer32
_An50pmpLinkDLCIDStatPktDisc_Object=MibTableColumn
an50pmpLinkDLCIDStatPktDisc=_An50pmpLinkDLCIDStatPktDisc_Object((1,3,6,1,4,1,10728,2,51,2,1,12),_An50pmpLinkDLCIDStatPktDisc_Type())
an50pmpLinkDLCIDStatPktDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkDLCIDStatPktDisc.setStatus(_A)
_An50pmpLinkDLCIDStatPktTran_Type=Integer32
_An50pmpLinkDLCIDStatPktTran_Object=MibTableColumn
an50pmpLinkDLCIDStatPktTran=_An50pmpLinkDLCIDStatPktTran_Object((1,3,6,1,4,1,10728,2,51,2,1,13),_An50pmpLinkDLCIDStatPktTran_Type())
an50pmpLinkDLCIDStatPktTran.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkDLCIDStatPktTran.setStatus(_A)
_An50pmpLinkDLCIDStatPktRecv_Type=Integer32
_An50pmpLinkDLCIDStatPktRecv_Object=MibTableColumn
an50pmpLinkDLCIDStatPktRecv=_An50pmpLinkDLCIDStatPktRecv_Object((1,3,6,1,4,1,10728,2,51,2,1,14),_An50pmpLinkDLCIDStatPktRecv_Type())
an50pmpLinkDLCIDStatPktRecv.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkDLCIDStatPktRecv.setStatus(_A)
class _An50pmpLinkULBurstRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_An50pmpLinkULBurstRate_Type.__name__=_C
_An50pmpLinkULBurstRate_Object=MibTableColumn
an50pmpLinkULBurstRate=_An50pmpLinkULBurstRate_Object((1,3,6,1,4,1,10728,2,51,2,1,15),_An50pmpLinkULBurstRate_Type())
an50pmpLinkULBurstRate.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkULBurstRate.setStatus(_A)
_An50pmpLinkULRSSI_Type=Integer32
_An50pmpLinkULRSSI_Object=MibTableColumn
an50pmpLinkULRSSI=_An50pmpLinkULRSSI_Object((1,3,6,1,4,1,10728,2,51,2,1,16),_An50pmpLinkULRSSI_Type())
an50pmpLinkULRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkULRSSI.setStatus(_A)
_An50pmpLinkULSINADR_Type=Integer32
_An50pmpLinkULSINADR_Object=MibTableColumn
an50pmpLinkULSINADR=_An50pmpLinkULSINADR_Object((1,3,6,1,4,1,10728,2,51,2,1,17),_An50pmpLinkULSINADR_Type())
an50pmpLinkULSINADR.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkULSINADR.setStatus(_A)
_An50pmpLinkULStatLostFrm_Type=Integer32
_An50pmpLinkULStatLostFrm_Object=MibTableColumn
an50pmpLinkULStatLostFrm=_An50pmpLinkULStatLostFrm_Object((1,3,6,1,4,1,10728,2,51,2,1,18),_An50pmpLinkULStatLostFrm_Type())
an50pmpLinkULStatLostFrm.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkULStatLostFrm.setStatus(_A)
_An50pmpLinkULStatBlksTot_Type=Integer32
_An50pmpLinkULStatBlksTot_Object=MibTableColumn
an50pmpLinkULStatBlksTot=_An50pmpLinkULStatBlksTot_Object((1,3,6,1,4,1,10728,2,51,2,1,19),_An50pmpLinkULStatBlksTot_Type())
an50pmpLinkULStatBlksTot.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkULStatBlksTot.setStatus(_A)
_An50pmpLinkULStatBlksRetr_Type=Integer32
_An50pmpLinkULStatBlksRetr_Object=MibTableColumn
an50pmpLinkULStatBlksRetr=_An50pmpLinkULStatBlksRetr_Object((1,3,6,1,4,1,10728,2,51,2,1,20),_An50pmpLinkULStatBlksRetr_Type())
an50pmpLinkULStatBlksRetr.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkULStatBlksRetr.setStatus(_A)
_An50pmpLinkULStatBlksDisc_Type=Integer32
_An50pmpLinkULStatBlksDisc_Object=MibTableColumn
an50pmpLinkULStatBlksDisc=_An50pmpLinkULStatBlksDisc_Object((1,3,6,1,4,1,10728,2,51,2,1,21),_An50pmpLinkULStatBlksDisc_Type())
an50pmpLinkULStatBlksDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkULStatBlksDisc.setStatus(_A)
_An50pmpLinkULCIDStatPktDisc_Type=Integer32
_An50pmpLinkULCIDStatPktDisc_Object=MibTableColumn
an50pmpLinkULCIDStatPktDisc=_An50pmpLinkULCIDStatPktDisc_Object((1,3,6,1,4,1,10728,2,51,2,1,22),_An50pmpLinkULCIDStatPktDisc_Type())
an50pmpLinkULCIDStatPktDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkULCIDStatPktDisc.setStatus(_A)
_An50pmpLinkULCIDStatPktTran_Type=Integer32
_An50pmpLinkULCIDStatPktTran_Object=MibTableColumn
an50pmpLinkULCIDStatPktTran=_An50pmpLinkULCIDStatPktTran_Object((1,3,6,1,4,1,10728,2,51,2,1,23),_An50pmpLinkULCIDStatPktTran_Type())
an50pmpLinkULCIDStatPktTran.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkULCIDStatPktTran.setStatus(_A)
_An50pmpLinkULCIDStatPktRecv_Type=Integer32
_An50pmpLinkULCIDStatPktRecv_Object=MibTableColumn
an50pmpLinkULCIDStatPktRecv=_An50pmpLinkULCIDStatPktRecv_Object((1,3,6,1,4,1,10728,2,51,2,1,24),_An50pmpLinkULCIDStatPktRecv_Type())
an50pmpLinkULCIDStatPktRecv.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkULCIDStatPktRecv.setStatus(_A)
_An50pmpLinkUpTime_Type=TimeTicks
_An50pmpLinkUpTime_Object=MibTableColumn
an50pmpLinkUpTime=_An50pmpLinkUpTime_Object((1,3,6,1,4,1,10728,2,51,2,1,25),_An50pmpLinkUpTime_Type())
an50pmpLinkUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkUpTime.setStatus(_A)
_An50pmpLinkLostCount_Type=Integer32
_An50pmpLinkLostCount_Object=MibTableColumn
an50pmpLinkLostCount=_An50pmpLinkLostCount_Object((1,3,6,1,4,1,10728,2,51,2,1,26),_An50pmpLinkLostCount_Type())
an50pmpLinkLostCount.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLinkLostCount.setStatus(_A)
class _An50pmpCIDSaveConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('donothing',1),('saveConfig',2)))
_An50pmpCIDSaveConfig_Type.__name__=_C
_An50pmpCIDSaveConfig_Object=MibScalar
an50pmpCIDSaveConfig=_An50pmpCIDSaveConfig_Object((1,3,6,1,4,1,10728,2,51,3),_An50pmpCIDSaveConfig_Type())
an50pmpCIDSaveConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:an50pmpCIDSaveConfig.setStatus(_A)
class _An50pmpLastModifiedCID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1023))
_An50pmpLastModifiedCID_Type.__name__=_C
_An50pmpLastModifiedCID_Object=MibScalar
an50pmpLastModifiedCID=_An50pmpLastModifiedCID_Object((1,3,6,1,4,1,10728,2,51,4),_An50pmpLastModifiedCID_Type())
an50pmpLastModifiedCID.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLastModifiedCID.setStatus(_A)
_An50pmpLastMissedSsMacAddress_Type=OctetString
_An50pmpLastMissedSsMacAddress_Object=MibScalar
an50pmpLastMissedSsMacAddress=_An50pmpLastMissedSsMacAddress_Object((1,3,6,1,4,1,10728,2,51,5),_An50pmpLastMissedSsMacAddress_Type())
an50pmpLastMissedSsMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLastMissedSsMacAddress.setStatus(_A)
_An50pmpLastRegisteredSsMacAddress_Type=OctetString
_An50pmpLastRegisteredSsMacAddress_Object=MibScalar
an50pmpLastRegisteredSsMacAddress=_An50pmpLastRegisteredSsMacAddress_Object((1,3,6,1,4,1,10728,2,51,6),_An50pmpLastRegisteredSsMacAddress_Type())
an50pmpLastRegisteredSsMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLastRegisteredSsMacAddress.setStatus(_A)
class _An50pmpLastSuccessfulID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1023))
_An50pmpLastSuccessfulID_Type.__name__=_C
_An50pmpLastSuccessfulID_Object=MibScalar
an50pmpLastSuccessfulID=_An50pmpLastSuccessfulID_Object((1,3,6,1,4,1,10728,2,51,7),_An50pmpLastSuccessfulID_Type())
an50pmpLastSuccessfulID.setMaxAccess(_B)
if mibBuilder.loadTexts:an50pmpLastSuccessfulID.setStatus(_A)
_An50pmpLastDeniedSsMacAddress_Type=OctetString
_An50pmpLastDeniedSsMacAddress_Object=MibScalar
an50pmpLastDeniedSsMacAddress=_An50pmpLastDeniedSsMacAddress_Object((1,3,6,1,4,1,10728,2,51,8),_An50pmpLastDeniedSsMacAddress_Type())
an50pmpLastDeniedSsMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:an50pmpLastDeniedSsMacAddress.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'redline':redline,'redlineProducts':redlineProducts,'redlineAN50':redlineAN50,'redlineMgmt':redlineMgmt,'redlineAN50PMPV1':redlineAN50PMPV1,'an50pmpLinkTable':an50pmpLinkTable,'an50pmpLinkEntry':an50pmpLinkEntry,_F:an50pmpLinkID,'an50pmpLinkName':an50pmpLinkName,'an50pmpLinkGroupID':an50pmpLinkGroupID,'an50pmpLinkPeerMac':an50pmpLinkPeerMac,'an50pmpLinkMaxDLBurstRate':an50pmpLinkMaxDLBurstRate,'an50pmpLinkMaxULBurstRate':an50pmpLinkMaxULBurstRate,'an50pmpLinkMaxHost':an50pmpLinkMaxHost,'an50pmpLinkCIDDLCIR':an50pmpLinkCIDDLCIR,'an50pmpLinkCIDDLPIR':an50pmpLinkCIDDLPIR,'an50pmpLinkCIDULCIR':an50pmpLinkCIDULCIR,'an50pmpLinkCIDULPIR':an50pmpLinkCIDULPIR,'an50pmpLinkDLQoS':an50pmpLinkDLQoS,'an50pmpLinkULQoS':an50pmpLinkULQoS,'an50pmpLinkRowStatus':an50pmpLinkRowStatus,'an50pmpLinkStatusTable':an50pmpLinkStatusTable,'an50pmpLinkStatusEntry':an50pmpLinkStatusEntry,'an50pmpLinkStatusID':an50pmpLinkStatusID,'an50pmpLinkStatus':an50pmpLinkStatus,'an50pmpLinkStatusCode':an50pmpLinkStatusCode,'an50pmpLinkRegConn':an50pmpLinkRegConn,'an50pmpLinkDLBurstRate':an50pmpLinkDLBurstRate,'an50pmpLinkDLRSSI':an50pmpLinkDLRSSI,'an50pmpLinkDLSINADR':an50pmpLinkDLSINADR,'an50pmpLinkDLStatLostFrm':an50pmpLinkDLStatLostFrm,'an50pmpLinkDLStatBlksTot':an50pmpLinkDLStatBlksTot,'an50pmpLinkDLStatBlksRetr':an50pmpLinkDLStatBlksRetr,'an50pmpLinkDLStatBlksDisc':an50pmpLinkDLStatBlksDisc,'an50pmpLinkDLCIDStatPktDisc':an50pmpLinkDLCIDStatPktDisc,'an50pmpLinkDLCIDStatPktTran':an50pmpLinkDLCIDStatPktTran,'an50pmpLinkDLCIDStatPktRecv':an50pmpLinkDLCIDStatPktRecv,'an50pmpLinkULBurstRate':an50pmpLinkULBurstRate,'an50pmpLinkULRSSI':an50pmpLinkULRSSI,'an50pmpLinkULSINADR':an50pmpLinkULSINADR,'an50pmpLinkULStatLostFrm':an50pmpLinkULStatLostFrm,'an50pmpLinkULStatBlksTot':an50pmpLinkULStatBlksTot,'an50pmpLinkULStatBlksRetr':an50pmpLinkULStatBlksRetr,'an50pmpLinkULStatBlksDisc':an50pmpLinkULStatBlksDisc,'an50pmpLinkULCIDStatPktDisc':an50pmpLinkULCIDStatPktDisc,'an50pmpLinkULCIDStatPktTran':an50pmpLinkULCIDStatPktTran,'an50pmpLinkULCIDStatPktRecv':an50pmpLinkULCIDStatPktRecv,'an50pmpLinkUpTime':an50pmpLinkUpTime,'an50pmpLinkLostCount':an50pmpLinkLostCount,'an50pmpCIDSaveConfig':an50pmpCIDSaveConfig,'an50pmpLastModifiedCID':an50pmpLastModifiedCID,'an50pmpLastMissedSsMacAddress':an50pmpLastMissedSsMacAddress,'an50pmpLastRegisteredSsMacAddress':an50pmpLastRegisteredSsMacAddress,'an50pmpLastSuccessfulID':an50pmpLastSuccessfulID,'an50pmpLastDeniedSsMacAddress':an50pmpLastDeniedSsMacAddress})