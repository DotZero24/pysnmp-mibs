_R='frPvcStatDlci'
_Q='frPvcStatIfIndex'
_P='active'
_O='frPvcConfDlci'
_N='frPvcConfIfIndex'
_M='frLmiStatIfIndex'
_L='frLmiConfIfIndex'
_K='frConfIfIndex'
_J='static'
_I='frInarpConfIfIndex'
_H='DisplayString'
_G='disable'
_F='enable'
_E='MAIPU-FR-MIB'
_D='Integer32'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention')
mpFrMib=ModuleIdentity((1,3,6,1,4,1,5651,3,6))
_FrIfMib_ObjectIdentity=ObjectIdentity
frIfMib=_FrIfMib_ObjectIdentity((1,3,6,1,4,1,5651,3,6,1))
if mibBuilder.loadTexts:frIfMib.setStatus(_A)
_FrConfTable_Object=MibTable
frConfTable=_FrConfTable_Object((1,3,6,1,4,1,5651,3,6,1,1))
if mibBuilder.loadTexts:frConfTable.setStatus(_A)
_FrConfEntry_Object=MibTableRow
frConfEntry=_FrConfEntry_Object((1,3,6,1,4,1,5651,3,6,1,1,1))
frConfEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:frConfEntry.setStatus(_A)
_FrConfIfIndex_Type=Integer32
_FrConfIfIndex_Object=MibTableColumn
frConfIfIndex=_FrConfIfIndex_Object((1,3,6,1,4,1,5651,3,6,1,1,1,1),_FrConfIfIndex_Type())
frConfIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:frConfIfIndex.setStatus(_A)
class _FrConfIfType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dte',1),('dce',2),('nni',3)))
_FrConfIfType_Type.__name__=_D
_FrConfIfType_Object=MibTableColumn
frConfIfType=_FrConfIfType_Object((1,3,6,1,4,1,5651,3,6,1,1,1,2),_FrConfIfType_Type())
frConfIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:frConfIfType.setStatus(_A)
_FrConfIfStatus_Type=RowStatus
_FrConfIfStatus_Object=MibTableColumn
frConfIfStatus=_FrConfIfStatus_Object((1,3,6,1,4,1,5651,3,6,1,1,1,3),_FrConfIfStatus_Type())
frConfIfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:frConfIfStatus.setStatus(_A)
_FrLmiConfTable_Object=MibTable
frLmiConfTable=_FrLmiConfTable_Object((1,3,6,1,4,1,5651,3,6,1,2))
if mibBuilder.loadTexts:frLmiConfTable.setStatus(_A)
_FrLmiConfEntry_Object=MibTableRow
frLmiConfEntry=_FrLmiConfEntry_Object((1,3,6,1,4,1,5651,3,6,1,2,1))
frLmiConfEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:frLmiConfEntry.setStatus(_A)
_FrLmiConfIfIndex_Type=Integer32
_FrLmiConfIfIndex_Object=MibTableColumn
frLmiConfIfIndex=_FrLmiConfIfIndex_Object((1,3,6,1,4,1,5651,3,6,1,2,1,1),_FrLmiConfIfIndex_Type())
frLmiConfIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:frLmiConfIfIndex.setStatus(_A)
class _FrLmiType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ansi',1),('q933a',2),('lmi',3)))
_FrLmiType_Type.__name__=_D
_FrLmiType_Object=MibTableColumn
frLmiType=_FrLmiType_Object((1,3,6,1,4,1,5651,3,6,1,2,1,2),_FrLmiType_Type())
frLmiType.setMaxAccess(_C)
if mibBuilder.loadTexts:frLmiType.setStatus(_A)
class _FrLmiN391Dte_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FrLmiN391Dte_Type.__name__=_D
_FrLmiN391Dte_Object=MibTableColumn
frLmiN391Dte=_FrLmiN391Dte_Object((1,3,6,1,4,1,5651,3,6,1,2,1,3),_FrLmiN391Dte_Type())
frLmiN391Dte.setMaxAccess(_C)
if mibBuilder.loadTexts:frLmiN391Dte.setStatus(_A)
class _FrLmiN392Dte_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrLmiN392Dte_Type.__name__=_D
_FrLmiN392Dte_Object=MibTableColumn
frLmiN392Dte=_FrLmiN392Dte_Object((1,3,6,1,4,1,5651,3,6,1,2,1,4),_FrLmiN392Dte_Type())
frLmiN392Dte.setMaxAccess(_C)
if mibBuilder.loadTexts:frLmiN392Dte.setStatus(_A)
class _FrLmiN393Dte_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrLmiN393Dte_Type.__name__=_D
_FrLmiN393Dte_Object=MibTableColumn
frLmiN393Dte=_FrLmiN393Dte_Object((1,3,6,1,4,1,5651,3,6,1,2,1,5),_FrLmiN393Dte_Type())
frLmiN393Dte.setMaxAccess(_C)
if mibBuilder.loadTexts:frLmiN393Dte.setStatus(_A)
class _FrLmiN392Dce_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrLmiN392Dce_Type.__name__=_D
_FrLmiN392Dce_Object=MibTableColumn
frLmiN392Dce=_FrLmiN392Dce_Object((1,3,6,1,4,1,5651,3,6,1,2,1,6),_FrLmiN392Dce_Type())
frLmiN392Dce.setMaxAccess(_C)
if mibBuilder.loadTexts:frLmiN392Dce.setStatus(_A)
class _FrLmiN393Dce_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrLmiN393Dce_Type.__name__=_D
_FrLmiN393Dce_Object=MibTableColumn
frLmiN393Dce=_FrLmiN393Dce_Object((1,3,6,1,4,1,5651,3,6,1,2,1,7),_FrLmiN393Dce_Type())
frLmiN393Dce.setMaxAccess(_C)
if mibBuilder.loadTexts:frLmiN393Dce.setStatus(_A)
class _FrLmiT392Dce_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_FrLmiT392Dce_Type.__name__=_D
_FrLmiT392Dce_Object=MibTableColumn
frLmiT392Dce=_FrLmiT392Dce_Object((1,3,6,1,4,1,5651,3,6,1,2,1,8),_FrLmiT392Dce_Type())
frLmiT392Dce.setMaxAccess(_C)
if mibBuilder.loadTexts:frLmiT392Dce.setStatus(_A)
class _FrLmiKeepalive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_FrLmiKeepalive_Type.__name__=_D
_FrLmiKeepalive_Object=MibTableColumn
frLmiKeepalive=_FrLmiKeepalive_Object((1,3,6,1,4,1,5651,3,6,1,2,1,9),_FrLmiKeepalive_Type())
frLmiKeepalive.setMaxAccess(_C)
if mibBuilder.loadTexts:frLmiKeepalive.setStatus(_A)
_FrLmiConfStatus_Type=RowStatus
_FrLmiConfStatus_Object=MibTableColumn
frLmiConfStatus=_FrLmiConfStatus_Object((1,3,6,1,4,1,5651,3,6,1,2,1,10),_FrLmiConfStatus_Type())
frLmiConfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:frLmiConfStatus.setStatus(_A)
_FrLmiStatTable_Object=MibTable
frLmiStatTable=_FrLmiStatTable_Object((1,3,6,1,4,1,5651,3,6,1,3))
if mibBuilder.loadTexts:frLmiStatTable.setStatus(_A)
_FrLmiStatEntry_Object=MibTableRow
frLmiStatEntry=_FrLmiStatEntry_Object((1,3,6,1,4,1,5651,3,6,1,3,1))
frLmiStatEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:frLmiStatEntry.setStatus(_A)
_FrLmiStatIfIndex_Type=Integer32
_FrLmiStatIfIndex_Object=MibTableColumn
frLmiStatIfIndex=_FrLmiStatIfIndex_Object((1,3,6,1,4,1,5651,3,6,1,3,1,1),_FrLmiStatIfIndex_Type())
frLmiStatIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:frLmiStatIfIndex.setStatus(_A)
_FrLmiStEnqSent_Type=Counter32
_FrLmiStEnqSent_Object=MibTableColumn
frLmiStEnqSent=_FrLmiStEnqSent_Object((1,3,6,1,4,1,5651,3,6,1,3,1,2),_FrLmiStEnqSent_Type())
frLmiStEnqSent.setMaxAccess(_B)
if mibBuilder.loadTexts:frLmiStEnqSent.setStatus(_A)
_FrLmiStMsgRecv_Type=Counter32
_FrLmiStMsgRecv_Object=MibTableColumn
frLmiStMsgRecv=_FrLmiStMsgRecv_Object((1,3,6,1,4,1,5651,3,6,1,3,1,3),_FrLmiStMsgRecv_Type())
frLmiStMsgRecv.setMaxAccess(_B)
if mibBuilder.loadTexts:frLmiStMsgRecv.setStatus(_A)
_FrLmiStTimeout_Type=Counter32
_FrLmiStTimeout_Object=MibTableColumn
frLmiStTimeout=_FrLmiStTimeout_Object((1,3,6,1,4,1,5651,3,6,1,3,1,4),_FrLmiStTimeout_Type())
frLmiStTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:frLmiStTimeout.setStatus(_A)
_FrLmiStEnqRecv_Type=Counter32
_FrLmiStEnqRecv_Object=MibTableColumn
frLmiStEnqRecv=_FrLmiStEnqRecv_Object((1,3,6,1,4,1,5651,3,6,1,3,1,5),_FrLmiStEnqRecv_Type())
frLmiStEnqRecv.setMaxAccess(_B)
if mibBuilder.loadTexts:frLmiStEnqRecv.setStatus(_A)
_FrLmiStMsgSent_Type=Counter32
_FrLmiStMsgSent_Object=MibTableColumn
frLmiStMsgSent=_FrLmiStMsgSent_Object((1,3,6,1,4,1,5651,3,6,1,3,1,6),_FrLmiStMsgSent_Type())
frLmiStMsgSent.setMaxAccess(_B)
if mibBuilder.loadTexts:frLmiStMsgSent.setStatus(_A)
_FrLmiStEnqTimeout_Type=Counter32
_FrLmiStEnqTimeout_Object=MibTableColumn
frLmiStEnqTimeout=_FrLmiStEnqTimeout_Object((1,3,6,1,4,1,5651,3,6,1,3,1,7),_FrLmiStEnqTimeout_Type())
frLmiStEnqTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:frLmiStEnqTimeout.setStatus(_A)
_FrInarpConfTable_Object=MibTable
frInarpConfTable=_FrInarpConfTable_Object((1,3,6,1,4,1,5651,3,6,1,4))
if mibBuilder.loadTexts:frInarpConfTable.setStatus(_A)
_FrInarpConfEntry_Object=MibTableRow
frInarpConfEntry=_FrInarpConfEntry_Object((1,3,6,1,4,1,5651,3,6,1,4,1))
frInarpConfEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:frInarpConfEntry.setStatus(_A)
_FrInarpConfIfIndex_Type=Integer32
_FrInarpConfIfIndex_Object=MibTableColumn
frInarpConfIfIndex=_FrInarpConfIfIndex_Object((1,3,6,1,4,1,5651,3,6,1,4,1,1),_FrInarpConfIfIndex_Type())
frInarpConfIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:frInarpConfIfIndex.setStatus(_A)
class _FrInarpEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FrInarpEnable_Type.__name__=_D
_FrInarpEnable_Object=MibTableColumn
frInarpEnable=_FrInarpEnable_Object((1,3,6,1,4,1,5651,3,6,1,4,1,2),_FrInarpEnable_Type())
frInarpEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:frInarpEnable.setStatus(_A)
class _FrInarpInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,300))
_FrInarpInterval_Type.__name__=_D
_FrInarpInterval_Object=MibTableColumn
frInarpInterval=_FrInarpInterval_Object((1,3,6,1,4,1,5651,3,6,1,4,1,3),_FrInarpInterval_Type())
frInarpInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:frInarpInterval.setStatus(_A)
class _FrInarpUpdate_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_FrInarpUpdate_Type.__name__=_D
_FrInarpUpdate_Object=MibTableColumn
frInarpUpdate=_FrInarpUpdate_Object((1,3,6,1,4,1,5651,3,6,1,4,1,4),_FrInarpUpdate_Type())
frInarpUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:frInarpUpdate.setStatus(_A)
_FrInarpStatus_Type=RowStatus
_FrInarpStatus_Object=MibTableColumn
frInarpStatus=_FrInarpStatus_Object((1,3,6,1,4,1,5651,3,6,1,4,1,5),_FrInarpStatus_Type())
frInarpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:frInarpStatus.setStatus(_A)
_FrInarpStatTable_Object=MibTable
frInarpStatTable=_FrInarpStatTable_Object((1,3,6,1,4,1,5651,3,6,1,5))
if mibBuilder.loadTexts:frInarpStatTable.setStatus(_A)
_FrInarpStatEntry_Object=MibTableRow
frInarpStatEntry=_FrInarpStatEntry_Object((1,3,6,1,4,1,5651,3,6,1,5,1))
frInarpStatEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:frInarpStatEntry.setStatus(_A)
_FrInarpStatIfIndex_Type=Integer32
_FrInarpStatIfIndex_Object=MibTableColumn
frInarpStatIfIndex=_FrInarpStatIfIndex_Object((1,3,6,1,4,1,5651,3,6,1,5,1,1),_FrInarpStatIfIndex_Type())
frInarpStatIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:frInarpStatIfIndex.setStatus(_A)
_FrInarpReqSent_Type=Counter32
_FrInarpReqSent_Object=MibTableColumn
frInarpReqSent=_FrInarpReqSent_Object((1,3,6,1,4,1,5651,3,6,1,5,1,2),_FrInarpReqSent_Type())
frInarpReqSent.setMaxAccess(_B)
if mibBuilder.loadTexts:frInarpReqSent.setStatus(_A)
_FrInarpReqRecv_Type=Counter32
_FrInarpReqRecv_Object=MibTableColumn
frInarpReqRecv=_FrInarpReqRecv_Object((1,3,6,1,4,1,5651,3,6,1,5,1,3),_FrInarpReqRecv_Type())
frInarpReqRecv.setMaxAccess(_B)
if mibBuilder.loadTexts:frInarpReqRecv.setStatus(_A)
_FrInarpReplySent_Type=Counter32
_FrInarpReplySent_Object=MibTableColumn
frInarpReplySent=_FrInarpReplySent_Object((1,3,6,1,4,1,5651,3,6,1,5,1,4),_FrInarpReplySent_Type())
frInarpReplySent.setMaxAccess(_B)
if mibBuilder.loadTexts:frInarpReplySent.setStatus(_A)
_FrInarpReplyRecv_Type=Counter32
_FrInarpReplyRecv_Object=MibTableColumn
frInarpReplyRecv=_FrInarpReplyRecv_Object((1,3,6,1,4,1,5651,3,6,1,5,1,5),_FrInarpReplyRecv_Type())
frInarpReplyRecv.setMaxAccess(_B)
if mibBuilder.loadTexts:frInarpReplyRecv.setStatus(_A)
_FrPvcMib_ObjectIdentity=ObjectIdentity
frPvcMib=_FrPvcMib_ObjectIdentity((1,3,6,1,4,1,5651,3,6,2))
if mibBuilder.loadTexts:frPvcMib.setStatus(_A)
_FrPvcConfTable_Object=MibTable
frPvcConfTable=_FrPvcConfTable_Object((1,3,6,1,4,1,5651,3,6,2,1))
if mibBuilder.loadTexts:frPvcConfTable.setStatus(_A)
_FrPvcConfEntry_Object=MibTableRow
frPvcConfEntry=_FrPvcConfEntry_Object((1,3,6,1,4,1,5651,3,6,2,1,1))
frPvcConfEntry.setIndexNames((0,_E,_N),(0,_E,_O))
if mibBuilder.loadTexts:frPvcConfEntry.setStatus(_A)
_FrPvcConfIfIndex_Type=Integer32
_FrPvcConfIfIndex_Object=MibTableColumn
frPvcConfIfIndex=_FrPvcConfIfIndex_Object((1,3,6,1,4,1,5651,3,6,2,1,1,1),_FrPvcConfIfIndex_Type())
frPvcConfIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:frPvcConfIfIndex.setStatus(_A)
class _FrPvcConfDlci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1007))
_FrPvcConfDlci_Type.__name__=_D
_FrPvcConfDlci_Object=MibTableColumn
frPvcConfDlci=_FrPvcConfDlci_Object((1,3,6,1,4,1,5651,3,6,2,1,1,2),_FrPvcConfDlci_Type())
frPvcConfDlci.setMaxAccess(_C)
if mibBuilder.loadTexts:frPvcConfDlci.setStatus(_A)
class _FrPvcIntf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_FrPvcIntf_Type.__name__=_H
_FrPvcIntf_Object=MibTableColumn
frPvcIntf=_FrPvcIntf_Object((1,3,6,1,4,1,5651,3,6,2,1,1,3),_FrPvcIntf_Type())
frPvcIntf.setMaxAccess(_C)
if mibBuilder.loadTexts:frPvcIntf.setStatus(_A)
class _FrPvcUsage_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('switched',2)))
_FrPvcUsage_Type.__name__=_D
_FrPvcUsage_Object=MibTableColumn
frPvcUsage=_FrPvcUsage_Object((1,3,6,1,4,1,5651,3,6,2,1,1,4),_FrPvcUsage_Type())
frPvcUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:frPvcUsage.setStatus(_A)
class _FrPvcStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('inActive',1),(_P,2),(_J,3),('deleted',4),('defined',5)))
_FrPvcStatus_Type.__name__=_D
_FrPvcStatus_Object=MibTableColumn
frPvcStatus=_FrPvcStatus_Object((1,3,6,1,4,1,5651,3,6,2,1,1,5),_FrPvcStatus_Type())
frPvcStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:frPvcStatus.setStatus(_A)
class _FrPvcEncType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ietf',1),('cisco',2)))
_FrPvcEncType_Type.__name__=_D
_FrPvcEncType_Object=MibTableColumn
frPvcEncType=_FrPvcEncType_Object((1,3,6,1,4,1,5651,3,6,2,1,1,6),_FrPvcEncType_Type())
frPvcEncType.setMaxAccess(_C)
if mibBuilder.loadTexts:frPvcEncType.setStatus(_A)
_FrPvcMapIp_Type=IpAddress
_FrPvcMapIp_Object=MibTableColumn
frPvcMapIp=_FrPvcMapIp_Object((1,3,6,1,4,1,5651,3,6,2,1,1,7),_FrPvcMapIp_Type())
frPvcMapIp.setMaxAccess(_C)
if mibBuilder.loadTexts:frPvcMapIp.setStatus(_A)
class _FrPvcMapType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('dynamic',2)))
_FrPvcMapType_Type.__name__=_D
_FrPvcMapType_Object=MibTableColumn
frPvcMapType=_FrPvcMapType_Object((1,3,6,1,4,1,5651,3,6,2,1,1,8),_FrPvcMapType_Type())
frPvcMapType.setMaxAccess(_C)
if mibBuilder.loadTexts:frPvcMapType.setStatus(_A)
class _FrPvcRouteOutIntf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_FrPvcRouteOutIntf_Type.__name__=_H
_FrPvcRouteOutIntf_Object=MibTableColumn
frPvcRouteOutIntf=_FrPvcRouteOutIntf_Object((1,3,6,1,4,1,5651,3,6,2,1,1,9),_FrPvcRouteOutIntf_Type())
frPvcRouteOutIntf.setMaxAccess(_C)
if mibBuilder.loadTexts:frPvcRouteOutIntf.setStatus(_A)
_FrPvcRouteOutDlci_Type=Integer32
_FrPvcRouteOutDlci_Object=MibTableColumn
frPvcRouteOutDlci=_FrPvcRouteOutDlci_Object((1,3,6,1,4,1,5651,3,6,2,1,1,10),_FrPvcRouteOutDlci_Type())
frPvcRouteOutDlci.setMaxAccess(_C)
if mibBuilder.loadTexts:frPvcRouteOutDlci.setStatus(_A)
class _FrPvcRouteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inactive',1),(_P,2),(_J,3)))
_FrPvcRouteStatus_Type.__name__=_D
_FrPvcRouteStatus_Object=MibTableColumn
frPvcRouteStatus=_FrPvcRouteStatus_Object((1,3,6,1,4,1,5651,3,6,2,1,1,11),_FrPvcRouteStatus_Type())
frPvcRouteStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:frPvcRouteStatus.setStatus(_A)
class _FrPvcBroadcast_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_FrPvcBroadcast_Type.__name__=_D
_FrPvcBroadcast_Object=MibTableColumn
frPvcBroadcast=_FrPvcBroadcast_Object((1,3,6,1,4,1,5651,3,6,2,1,1,12),_FrPvcBroadcast_Type())
frPvcBroadcast.setMaxAccess(_C)
if mibBuilder.loadTexts:frPvcBroadcast.setStatus(_A)
class _FrPvcNoInarpIp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_FrPvcNoInarpIp_Type.__name__=_D
_FrPvcNoInarpIp_Object=MibTableColumn
frPvcNoInarpIp=_FrPvcNoInarpIp_Object((1,3,6,1,4,1,5651,3,6,2,1,1,13),_FrPvcNoInarpIp_Type())
frPvcNoInarpIp.setMaxAccess(_C)
if mibBuilder.loadTexts:frPvcNoInarpIp.setStatus(_A)
class _FrPvcGetFromDce_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('false',1),('true',2)))
_FrPvcGetFromDce_Type.__name__=_D
_FrPvcGetFromDce_Object=MibTableColumn
frPvcGetFromDce=_FrPvcGetFromDce_Object((1,3,6,1,4,1,5651,3,6,2,1,1,14),_FrPvcGetFromDce_Type())
frPvcGetFromDce.setMaxAccess(_C)
if mibBuilder.loadTexts:frPvcGetFromDce.setStatus(_A)
_FrPvcConfTableStatus_Type=RowStatus
_FrPvcConfTableStatus_Object=MibTableColumn
frPvcConfTableStatus=_FrPvcConfTableStatus_Object((1,3,6,1,4,1,5651,3,6,2,1,1,15),_FrPvcConfTableStatus_Type())
frPvcConfTableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:frPvcConfTableStatus.setStatus(_A)
_FrPvcStaticTable_Object=MibTable
frPvcStaticTable=_FrPvcStaticTable_Object((1,3,6,1,4,1,5651,3,6,2,2))
if mibBuilder.loadTexts:frPvcStaticTable.setStatus(_A)
_FrPvcStaticEntry_Object=MibTableRow
frPvcStaticEntry=_FrPvcStaticEntry_Object((1,3,6,1,4,1,5651,3,6,2,2,1))
frPvcStaticEntry.setIndexNames((0,_E,_Q),(0,_E,_R))
if mibBuilder.loadTexts:frPvcStaticEntry.setStatus(_A)
_FrPvcStatIfIndex_Type=Integer32
_FrPvcStatIfIndex_Object=MibTableColumn
frPvcStatIfIndex=_FrPvcStatIfIndex_Object((1,3,6,1,4,1,5651,3,6,2,2,1,1),_FrPvcStatIfIndex_Type())
frPvcStatIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:frPvcStatIfIndex.setStatus(_A)
class _FrPvcStatDlci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1007))
_FrPvcStatDlci_Type.__name__=_D
_FrPvcStatDlci_Object=MibTableColumn
frPvcStatDlci=_FrPvcStatDlci_Object((1,3,6,1,4,1,5651,3,6,2,2,1,2),_FrPvcStatDlci_Type())
frPvcStatDlci.setMaxAccess(_B)
if mibBuilder.loadTexts:frPvcStatDlci.setStatus(_A)
_FrPvcStatInPkts_Type=Counter32
_FrPvcStatInPkts_Object=MibTableColumn
frPvcStatInPkts=_FrPvcStatInPkts_Object((1,3,6,1,4,1,5651,3,6,2,2,1,3),_FrPvcStatInPkts_Type())
frPvcStatInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:frPvcStatInPkts.setStatus(_A)
_FrPvcStatOutPkts_Type=Counter32
_FrPvcStatOutPkts_Object=MibTableColumn
frPvcStatOutPkts=_FrPvcStatOutPkts_Object((1,3,6,1,4,1,5651,3,6,2,2,1,4),_FrPvcStatOutPkts_Type())
frPvcStatOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:frPvcStatOutPkts.setStatus(_A)
_FrPvcStatInBytes_Type=Counter32
_FrPvcStatInBytes_Object=MibTableColumn
frPvcStatInBytes=_FrPvcStatInBytes_Object((1,3,6,1,4,1,5651,3,6,2,2,1,5),_FrPvcStatInBytes_Type())
frPvcStatInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:frPvcStatInBytes.setStatus(_A)
_FrPvcStatOutBytes_Type=Counter32
_FrPvcStatOutBytes_Object=MibTableColumn
frPvcStatOutBytes=_FrPvcStatOutBytes_Object((1,3,6,1,4,1,5651,3,6,2,2,1,6),_FrPvcStatOutBytes_Type())
frPvcStatOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:frPvcStatOutBytes.setStatus(_A)
_FrPvcStatDroppedPkts_Type=Counter32
_FrPvcStatDroppedPkts_Object=MibTableColumn
frPvcStatDroppedPkts=_FrPvcStatDroppedPkts_Object((1,3,6,1,4,1,5651,3,6,2,2,1,7),_FrPvcStatDroppedPkts_Type())
frPvcStatDroppedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:frPvcStatDroppedPkts.setStatus(_A)
_FrPvcStatInFecnPkts_Type=Counter32
_FrPvcStatInFecnPkts_Object=MibTableColumn
frPvcStatInFecnPkts=_FrPvcStatInFecnPkts_Object((1,3,6,1,4,1,5651,3,6,2,2,1,8),_FrPvcStatInFecnPkts_Type())
frPvcStatInFecnPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:frPvcStatInFecnPkts.setStatus(_A)
_FrPvcStatOutFecnPkts_Type=Counter32
_FrPvcStatOutFecnPkts_Object=MibTableColumn
frPvcStatOutFecnPkts=_FrPvcStatOutFecnPkts_Object((1,3,6,1,4,1,5651,3,6,2,2,1,9),_FrPvcStatOutFecnPkts_Type())
frPvcStatOutFecnPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:frPvcStatOutFecnPkts.setStatus(_A)
_FrPvcStatInBecnPkts_Type=Counter32
_FrPvcStatInBecnPkts_Object=MibTableColumn
frPvcStatInBecnPkts=_FrPvcStatInBecnPkts_Object((1,3,6,1,4,1,5651,3,6,2,2,1,10),_FrPvcStatInBecnPkts_Type())
frPvcStatInBecnPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:frPvcStatInBecnPkts.setStatus(_A)
_FrPvcStatOutBecnPkts_Type=Counter32
_FrPvcStatOutBecnPkts_Object=MibTableColumn
frPvcStatOutBecnPkts=_FrPvcStatOutBecnPkts_Object((1,3,6,1,4,1,5651,3,6,2,2,1,11),_FrPvcStatOutBecnPkts_Type())
frPvcStatOutBecnPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:frPvcStatOutBecnPkts.setStatus(_A)
_FrPvcStatInDePkts_Type=Counter32
_FrPvcStatInDePkts_Object=MibTableColumn
frPvcStatInDePkts=_FrPvcStatInDePkts_Object((1,3,6,1,4,1,5651,3,6,2,2,1,12),_FrPvcStatInDePkts_Type())
frPvcStatInDePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:frPvcStatInDePkts.setStatus(_A)
_FrPvcStatOutDePkts_Type=Counter32
_FrPvcStatOutDePkts_Object=MibTableColumn
frPvcStatOutDePkts=_FrPvcStatOutDePkts_Object((1,3,6,1,4,1,5651,3,6,2,2,1,13),_FrPvcStatOutDePkts_Type())
frPvcStatOutDePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:frPvcStatOutDePkts.setStatus(_A)
_FrPvcSwitchPkts_Type=Counter32
_FrPvcSwitchPkts_Object=MibTableColumn
frPvcSwitchPkts=_FrPvcSwitchPkts_Object((1,3,6,1,4,1,5651,3,6,2,2,1,14),_FrPvcSwitchPkts_Type())
frPvcSwitchPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:frPvcSwitchPkts.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'mpFrMib':mpFrMib,'frIfMib':frIfMib,'frConfTable':frConfTable,'frConfEntry':frConfEntry,_K:frConfIfIndex,'frConfIfType':frConfIfType,'frConfIfStatus':frConfIfStatus,'frLmiConfTable':frLmiConfTable,'frLmiConfEntry':frLmiConfEntry,_L:frLmiConfIfIndex,'frLmiType':frLmiType,'frLmiN391Dte':frLmiN391Dte,'frLmiN392Dte':frLmiN392Dte,'frLmiN393Dte':frLmiN393Dte,'frLmiN392Dce':frLmiN392Dce,'frLmiN393Dce':frLmiN393Dce,'frLmiT392Dce':frLmiT392Dce,'frLmiKeepalive':frLmiKeepalive,'frLmiConfStatus':frLmiConfStatus,'frLmiStatTable':frLmiStatTable,'frLmiStatEntry':frLmiStatEntry,_M:frLmiStatIfIndex,'frLmiStEnqSent':frLmiStEnqSent,'frLmiStMsgRecv':frLmiStMsgRecv,'frLmiStTimeout':frLmiStTimeout,'frLmiStEnqRecv':frLmiStEnqRecv,'frLmiStMsgSent':frLmiStMsgSent,'frLmiStEnqTimeout':frLmiStEnqTimeout,'frInarpConfTable':frInarpConfTable,'frInarpConfEntry':frInarpConfEntry,_I:frInarpConfIfIndex,'frInarpEnable':frInarpEnable,'frInarpInterval':frInarpInterval,'frInarpUpdate':frInarpUpdate,'frInarpStatus':frInarpStatus,'frInarpStatTable':frInarpStatTable,'frInarpStatEntry':frInarpStatEntry,'frInarpStatIfIndex':frInarpStatIfIndex,'frInarpReqSent':frInarpReqSent,'frInarpReqRecv':frInarpReqRecv,'frInarpReplySent':frInarpReplySent,'frInarpReplyRecv':frInarpReplyRecv,'frPvcMib':frPvcMib,'frPvcConfTable':frPvcConfTable,'frPvcConfEntry':frPvcConfEntry,_N:frPvcConfIfIndex,_O:frPvcConfDlci,'frPvcIntf':frPvcIntf,'frPvcUsage':frPvcUsage,'frPvcStatus':frPvcStatus,'frPvcEncType':frPvcEncType,'frPvcMapIp':frPvcMapIp,'frPvcMapType':frPvcMapType,'frPvcRouteOutIntf':frPvcRouteOutIntf,'frPvcRouteOutDlci':frPvcRouteOutDlci,'frPvcRouteStatus':frPvcRouteStatus,'frPvcBroadcast':frPvcBroadcast,'frPvcNoInarpIp':frPvcNoInarpIp,'frPvcGetFromDce':frPvcGetFromDce,'frPvcConfTableStatus':frPvcConfTableStatus,'frPvcStaticTable':frPvcStaticTable,'frPvcStaticEntry':frPvcStaticEntry,_Q:frPvcStatIfIndex,_R:frPvcStatDlci,'frPvcStatInPkts':frPvcStatInPkts,'frPvcStatOutPkts':frPvcStatOutPkts,'frPvcStatInBytes':frPvcStatInBytes,'frPvcStatOutBytes':frPvcStatOutBytes,'frPvcStatDroppedPkts':frPvcStatDroppedPkts,'frPvcStatInFecnPkts':frPvcStatInFecnPkts,'frPvcStatOutFecnPkts':frPvcStatOutFecnPkts,'frPvcStatInBecnPkts':frPvcStatInBecnPkts,'frPvcStatOutBecnPkts':frPvcStatOutBecnPkts,'frPvcStatInDePkts':frPvcStatInDePkts,'frPvcStatOutDePkts':frPvcStatOutDePkts,'frPvcSwitchPkts':frPvcSwitchPkts})