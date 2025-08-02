_Q='bidirectional'
_P='unidirectional'
_O='sleMplsTpTunnelCfgInfoIndex'
_N='SLE-MPLS-TP-TUNNEL-MIB'
_M='swap'
_L='pop'
_K='push'
_J='none'
_I='OctetString'
_H='itut'
_G='ietf'
_F='MplsLabel'
_E='Unsigned32'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sleMgmt,=mibBuilder.importSymbols('DASAN-SMI','sleMgmt')
InterfaceIndexOrZero,ifCounterDiscontinuityGroup,ifGeneralInformationGroup=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero','ifCounterDiscontinuityGroup','ifGeneralInformationGroup')
MplsCcId,MplsIccId=mibBuilder.importSymbols('MPLS-TC-EXT-STD-MIB','MplsCcId','MplsIccId')
MplsLabel,mplsStdMIB=mibBuilder.importSymbols('MPLS-TC-STD-MIB',_F,'mplsStdMIB')
SleControlRequestResultType,SleControlStatusType=mibBuilder.importSymbols('SLE-TC-MIB','SleControlRequestResultType','SleControlStatusType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,zeroDotZero=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso','zeroDotZero')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
sleMplsTpTunnel=ModuleIdentity((1,3,6,1,4,1,6296,101,16,14))
if mibBuilder.loadTexts:sleMplsTpTunnel.setRevisions(('2004-06-03 00:00',))
_SleMpls_ObjectIdentity=ObjectIdentity
sleMpls=_SleMpls_ObjectIdentity((1,3,6,1,4,1,6296,101,16))
if mibBuilder.loadTexts:sleMpls.setStatus(_A)
_SleMplsTpTunnelCfg_ObjectIdentity=ObjectIdentity
sleMplsTpTunnelCfg=_SleMplsTpTunnelCfg_ObjectIdentity((1,3,6,1,4,1,6296,101,16,14,1))
_SleMplsTpTunnelCfgInfoTable_Object=MibTable
sleMplsTpTunnelCfgInfoTable=_SleMplsTpTunnelCfgInfoTable_Object((1,3,6,1,4,1,6296,101,16,14,1,1))
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoTable.setStatus(_A)
_SleMplsTpTunnelCfgInfoEntry_Object=MibTableRow
sleMplsTpTunnelCfgInfoEntry=_SleMplsTpTunnelCfgInfoEntry_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1))
sleMplsTpTunnelCfgInfoEntry.setIndexNames((0,_N,_O))
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoEntry.setStatus(_A)
class _SleMplsTpTunnelCfgInfoIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SleMplsTpTunnelCfgInfoIndex_Type.__name__=_E
_SleMplsTpTunnelCfgInfoIndex_Object=MibTableColumn
sleMplsTpTunnelCfgInfoIndex=_SleMplsTpTunnelCfgInfoIndex_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,1),_SleMplsTpTunnelCfgInfoIndex_Type())
sleMplsTpTunnelCfgInfoIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoIndex.setStatus(_A)
class _SleMplsTpTunnelCfgInfoName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SleMplsTpTunnelCfgInfoName_Type.__name__=_I
_SleMplsTpTunnelCfgInfoName_Object=MibTableColumn
sleMplsTpTunnelCfgInfoName=_SleMplsTpTunnelCfgInfoName_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,2),_SleMplsTpTunnelCfgInfoName_Type())
sleMplsTpTunnelCfgInfoName.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoName.setStatus(_A)
class _SleMplsTpTunnelCfgInfoId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SleMplsTpTunnelCfgInfoId_Type.__name__=_E
_SleMplsTpTunnelCfgInfoId_Object=MibTableColumn
sleMplsTpTunnelCfgInfoId=_SleMplsTpTunnelCfgInfoId_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,3),_SleMplsTpTunnelCfgInfoId_Type())
sleMplsTpTunnelCfgInfoId.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoId.setStatus(_A)
class _SleMplsTpTunnelCfgInfoSrcIdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SleMplsTpTunnelCfgInfoSrcIdType_Type.__name__=_D
_SleMplsTpTunnelCfgInfoSrcIdType_Object=MibTableColumn
sleMplsTpTunnelCfgInfoSrcIdType=_SleMplsTpTunnelCfgInfoSrcIdType_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,4),_SleMplsTpTunnelCfgInfoSrcIdType_Type())
sleMplsTpTunnelCfgInfoSrcIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoSrcIdType.setStatus(_A)
class _SleMplsTpTunnelCfgInfoSrcGId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_SleMplsTpTunnelCfgInfoSrcGId_Type.__name__=_E
_SleMplsTpTunnelCfgInfoSrcGId_Object=MibTableColumn
sleMplsTpTunnelCfgInfoSrcGId=_SleMplsTpTunnelCfgInfoSrcGId_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,5),_SleMplsTpTunnelCfgInfoSrcGId_Type())
sleMplsTpTunnelCfgInfoSrcGId.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoSrcGId.setStatus(_A)
_SleMplsTpTunnelCfgInfoSrcCc_Type=MplsCcId
_SleMplsTpTunnelCfgInfoSrcCc_Object=MibTableColumn
sleMplsTpTunnelCfgInfoSrcCc=_SleMplsTpTunnelCfgInfoSrcCc_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,6),_SleMplsTpTunnelCfgInfoSrcCc_Type())
sleMplsTpTunnelCfgInfoSrcCc.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoSrcCc.setStatus(_A)
_SleMplsTpTunnelCfgInfoSrcIcc_Type=MplsIccId
_SleMplsTpTunnelCfgInfoSrcIcc_Object=MibTableColumn
sleMplsTpTunnelCfgInfoSrcIcc=_SleMplsTpTunnelCfgInfoSrcIcc_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,7),_SleMplsTpTunnelCfgInfoSrcIcc_Type())
sleMplsTpTunnelCfgInfoSrcIcc.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoSrcIcc.setStatus(_A)
_SleMplsTpTunnelCfgInfoSrcNodeId_Type=IpAddress
_SleMplsTpTunnelCfgInfoSrcNodeId_Object=MibTableColumn
sleMplsTpTunnelCfgInfoSrcNodeId=_SleMplsTpTunnelCfgInfoSrcNodeId_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,8),_SleMplsTpTunnelCfgInfoSrcNodeId_Type())
sleMplsTpTunnelCfgInfoSrcNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoSrcNodeId.setStatus(_A)
class _SleMplsTpTunnelCfgInfoDestIdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SleMplsTpTunnelCfgInfoDestIdType_Type.__name__=_D
_SleMplsTpTunnelCfgInfoDestIdType_Object=MibTableColumn
sleMplsTpTunnelCfgInfoDestIdType=_SleMplsTpTunnelCfgInfoDestIdType_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,9),_SleMplsTpTunnelCfgInfoDestIdType_Type())
sleMplsTpTunnelCfgInfoDestIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoDestIdType.setStatus(_A)
class _SleMplsTpTunnelCfgInfoDestGId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_SleMplsTpTunnelCfgInfoDestGId_Type.__name__=_E
_SleMplsTpTunnelCfgInfoDestGId_Object=MibTableColumn
sleMplsTpTunnelCfgInfoDestGId=_SleMplsTpTunnelCfgInfoDestGId_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,10),_SleMplsTpTunnelCfgInfoDestGId_Type())
sleMplsTpTunnelCfgInfoDestGId.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoDestGId.setStatus(_A)
_SleMplsTpTunnelCfgInfoDestCc_Type=MplsCcId
_SleMplsTpTunnelCfgInfoDestCc_Object=MibTableColumn
sleMplsTpTunnelCfgInfoDestCc=_SleMplsTpTunnelCfgInfoDestCc_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,11),_SleMplsTpTunnelCfgInfoDestCc_Type())
sleMplsTpTunnelCfgInfoDestCc.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoDestCc.setStatus(_A)
_SleMplsTpTunnelCfgInfoDestIcc_Type=MplsIccId
_SleMplsTpTunnelCfgInfoDestIcc_Object=MibTableColumn
sleMplsTpTunnelCfgInfoDestIcc=_SleMplsTpTunnelCfgInfoDestIcc_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,12),_SleMplsTpTunnelCfgInfoDestIcc_Type())
sleMplsTpTunnelCfgInfoDestIcc.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoDestIcc.setStatus(_A)
_SleMplsTpTunnelCfgInfoDestNodeId_Type=IpAddress
_SleMplsTpTunnelCfgInfoDestNodeId_Object=MibTableColumn
sleMplsTpTunnelCfgInfoDestNodeId=_SleMplsTpTunnelCfgInfoDestNodeId_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,13),_SleMplsTpTunnelCfgInfoDestNodeId_Type())
sleMplsTpTunnelCfgInfoDestNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoDestNodeId.setStatus(_A)
class _SleMplsTpTunnelCfgInfoMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_J,0),(_P,1),(_Q,2),('corouted',3),('associate',4)))
_SleMplsTpTunnelCfgInfoMode_Type.__name__=_D
_SleMplsTpTunnelCfgInfoMode_Object=MibTableColumn
sleMplsTpTunnelCfgInfoMode=_SleMplsTpTunnelCfgInfoMode_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,14),_SleMplsTpTunnelCfgInfoMode_Type())
sleMplsTpTunnelCfgInfoMode.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoMode.setStatus(_A)
class _SleMplsTpTunnelCfgInfoFwdInLabel_Type(MplsLabel):defaultValue=1048576
_SleMplsTpTunnelCfgInfoFwdInLabel_Type.__name__=_F
_SleMplsTpTunnelCfgInfoFwdInLabel_Object=MibTableColumn
sleMplsTpTunnelCfgInfoFwdInLabel=_SleMplsTpTunnelCfgInfoFwdInLabel_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,15),_SleMplsTpTunnelCfgInfoFwdInLabel_Type())
sleMplsTpTunnelCfgInfoFwdInLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoFwdInLabel.setStatus(_A)
_SleMplsTpTunnelCfgInfoFwdInIfIndex_Type=InterfaceIndexOrZero
_SleMplsTpTunnelCfgInfoFwdInIfIndex_Object=MibTableColumn
sleMplsTpTunnelCfgInfoFwdInIfIndex=_SleMplsTpTunnelCfgInfoFwdInIfIndex_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,16),_SleMplsTpTunnelCfgInfoFwdInIfIndex_Type())
sleMplsTpTunnelCfgInfoFwdInIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoFwdInIfIndex.setStatus(_A)
class _SleMplsTpTunnelCfgInfoFwdOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2),(_M,3)))
_SleMplsTpTunnelCfgInfoFwdOperation_Type.__name__=_D
_SleMplsTpTunnelCfgInfoFwdOperation_Object=MibTableColumn
sleMplsTpTunnelCfgInfoFwdOperation=_SleMplsTpTunnelCfgInfoFwdOperation_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,17),_SleMplsTpTunnelCfgInfoFwdOperation_Type())
sleMplsTpTunnelCfgInfoFwdOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoFwdOperation.setStatus(_A)
class _SleMplsTpTunnelCfgInfoFwdOutLabel_Type(MplsLabel):defaultValue=1048576
_SleMplsTpTunnelCfgInfoFwdOutLabel_Type.__name__=_F
_SleMplsTpTunnelCfgInfoFwdOutLabel_Object=MibTableColumn
sleMplsTpTunnelCfgInfoFwdOutLabel=_SleMplsTpTunnelCfgInfoFwdOutLabel_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,18),_SleMplsTpTunnelCfgInfoFwdOutLabel_Type())
sleMplsTpTunnelCfgInfoFwdOutLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoFwdOutLabel.setStatus(_A)
_SleMplsTpTunnelCfgInfoFwdOutIfIndex_Type=InterfaceIndexOrZero
_SleMplsTpTunnelCfgInfoFwdOutIfIndex_Object=MibTableColumn
sleMplsTpTunnelCfgInfoFwdOutIfIndex=_SleMplsTpTunnelCfgInfoFwdOutIfIndex_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,19),_SleMplsTpTunnelCfgInfoFwdOutIfIndex_Type())
sleMplsTpTunnelCfgInfoFwdOutIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoFwdOutIfIndex.setStatus(_A)
_SleMplsTpTunnelCfgInfoFwdOutMac_Type=MacAddress
_SleMplsTpTunnelCfgInfoFwdOutMac_Object=MibTableColumn
sleMplsTpTunnelCfgInfoFwdOutMac=_SleMplsTpTunnelCfgInfoFwdOutMac_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,20),_SleMplsTpTunnelCfgInfoFwdOutMac_Type())
sleMplsTpTunnelCfgInfoFwdOutMac.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoFwdOutMac.setStatus(_A)
class _SleMplsTpTunnelCfgInfoRevInLabel_Type(MplsLabel):defaultValue=1048576
_SleMplsTpTunnelCfgInfoRevInLabel_Type.__name__=_F
_SleMplsTpTunnelCfgInfoRevInLabel_Object=MibTableColumn
sleMplsTpTunnelCfgInfoRevInLabel=_SleMplsTpTunnelCfgInfoRevInLabel_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,21),_SleMplsTpTunnelCfgInfoRevInLabel_Type())
sleMplsTpTunnelCfgInfoRevInLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoRevInLabel.setStatus(_A)
_SleMplsTpTunnelCfgInfoRevInIfIndex_Type=InterfaceIndexOrZero
_SleMplsTpTunnelCfgInfoRevInIfIndex_Object=MibTableColumn
sleMplsTpTunnelCfgInfoRevInIfIndex=_SleMplsTpTunnelCfgInfoRevInIfIndex_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,22),_SleMplsTpTunnelCfgInfoRevInIfIndex_Type())
sleMplsTpTunnelCfgInfoRevInIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoRevInIfIndex.setStatus(_A)
class _SleMplsTpTunnelCfgInfoRevOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2),(_M,3)))
_SleMplsTpTunnelCfgInfoRevOperation_Type.__name__=_D
_SleMplsTpTunnelCfgInfoRevOperation_Object=MibTableColumn
sleMplsTpTunnelCfgInfoRevOperation=_SleMplsTpTunnelCfgInfoRevOperation_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,23),_SleMplsTpTunnelCfgInfoRevOperation_Type())
sleMplsTpTunnelCfgInfoRevOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoRevOperation.setStatus(_A)
class _SleMplsTpTunnelCfgInfoRevOutLabel_Type(MplsLabel):defaultValue=1048576
_SleMplsTpTunnelCfgInfoRevOutLabel_Type.__name__=_F
_SleMplsTpTunnelCfgInfoRevOutLabel_Object=MibTableColumn
sleMplsTpTunnelCfgInfoRevOutLabel=_SleMplsTpTunnelCfgInfoRevOutLabel_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,24),_SleMplsTpTunnelCfgInfoRevOutLabel_Type())
sleMplsTpTunnelCfgInfoRevOutLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoRevOutLabel.setStatus(_A)
_SleMplsTpTunnelCfgInfoRevOutIfIndex_Type=InterfaceIndexOrZero
_SleMplsTpTunnelCfgInfoRevOutIfIndex_Object=MibTableColumn
sleMplsTpTunnelCfgInfoRevOutIfIndex=_SleMplsTpTunnelCfgInfoRevOutIfIndex_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,25),_SleMplsTpTunnelCfgInfoRevOutIfIndex_Type())
sleMplsTpTunnelCfgInfoRevOutIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoRevOutIfIndex.setStatus(_A)
_SleMplsTpTunnelCfgInfoRevOutMac_Type=MacAddress
_SleMplsTpTunnelCfgInfoRevOutMac_Object=MibTableColumn
sleMplsTpTunnelCfgInfoRevOutMac=_SleMplsTpTunnelCfgInfoRevOutMac_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,26),_SleMplsTpTunnelCfgInfoRevOutMac_Type())
sleMplsTpTunnelCfgInfoRevOutMac.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoRevOutMac.setStatus(_A)
class _SleMplsTpTunnelCfgInfoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_SleMplsTpTunnelCfgInfoState_Type.__name__=_D
_SleMplsTpTunnelCfgInfoState_Object=MibTableColumn
sleMplsTpTunnelCfgInfoState=_SleMplsTpTunnelCfgInfoState_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,27),_SleMplsTpTunnelCfgInfoState_Type())
sleMplsTpTunnelCfgInfoState.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoState.setStatus(_A)
class _SleMplsTpTunnelCfgInfoRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('source',0),('transist',1),('destination',2)))
_SleMplsTpTunnelCfgInfoRole_Type.__name__=_D
_SleMplsTpTunnelCfgInfoRole_Object=MibTableColumn
sleMplsTpTunnelCfgInfoRole=_SleMplsTpTunnelCfgInfoRole_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,28),_SleMplsTpTunnelCfgInfoRole_Type())
sleMplsTpTunnelCfgInfoRole.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoRole.setStatus(_A)
_SleMplsTpTunnelCfgInfoAssociateTnlName_Type=OctetString
_SleMplsTpTunnelCfgInfoAssociateTnlName_Object=MibTableColumn
sleMplsTpTunnelCfgInfoAssociateTnlName=_SleMplsTpTunnelCfgInfoAssociateTnlName_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,29),_SleMplsTpTunnelCfgInfoAssociateTnlName_Type())
sleMplsTpTunnelCfgInfoAssociateTnlName.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoAssociateTnlName.setStatus(_A)
_SleMplsTpTunnelCfgInfoDescription_Type=OctetString
_SleMplsTpTunnelCfgInfoDescription_Object=MibTableColumn
sleMplsTpTunnelCfgInfoDescription=_SleMplsTpTunnelCfgInfoDescription_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,30),_SleMplsTpTunnelCfgInfoDescription_Type())
sleMplsTpTunnelCfgInfoDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoDescription.setStatus(_A)
class _SleMplsTpTunnelCfgInfoHlspRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('server',1),('client',2)))
_SleMplsTpTunnelCfgInfoHlspRole_Type.__name__=_D
_SleMplsTpTunnelCfgInfoHlspRole_Object=MibTableColumn
sleMplsTpTunnelCfgInfoHlspRole=_SleMplsTpTunnelCfgInfoHlspRole_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,31),_SleMplsTpTunnelCfgInfoHlspRole_Type())
sleMplsTpTunnelCfgInfoHlspRole.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoHlspRole.setStatus(_A)
_SleMplsTpTunnelCfgInfoHlspServerTunnelName_Type=OctetString
_SleMplsTpTunnelCfgInfoHlspServerTunnelName_Object=MibTableColumn
sleMplsTpTunnelCfgInfoHlspServerTunnelName=_SleMplsTpTunnelCfgInfoHlspServerTunnelName_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,32),_SleMplsTpTunnelCfgInfoHlspServerTunnelName_Type())
sleMplsTpTunnelCfgInfoHlspServerTunnelName.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoHlspServerTunnelName.setStatus(_A)
_SleMplsTpTunnelCfgInfoQosPolicyName_Type=OctetString
_SleMplsTpTunnelCfgInfoQosPolicyName_Object=MibTableColumn
sleMplsTpTunnelCfgInfoQosPolicyName=_SleMplsTpTunnelCfgInfoQosPolicyName_Object((1,3,6,1,4,1,6296,101,16,14,1,1,1,33),_SleMplsTpTunnelCfgInfoQosPolicyName_Type())
sleMplsTpTunnelCfgInfoQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgInfoQosPolicyName.setStatus(_A)
_SleMplsTpTunnelCfgControl_ObjectIdentity=ObjectIdentity
sleMplsTpTunnelCfgControl=_SleMplsTpTunnelCfgControl_ObjectIdentity((1,3,6,1,4,1,6296,101,16,14,1,2))
class _SleMplsTpTunnelCfgControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*(('createMplsTpTunnelEntry',1),('deleteMplsTpTunnelEntry',2),('setMplsTpTunnelMode',3),('setNhlfe',4),('setIlmPop',5),('setIlmSwap',6),('setAssociateTunnel',7),('unsetNhlfe',8),('unsetIlmPop',9),('unsetIlmSwap',10),('unsetAssociateTunnel',11),('setDescription',12),('setHlspServerLsp',13),('setHlspClientLsp',14),('unsetHlspServerLsp',15),('unsetHlspClientLsp',16),('setTunnelQosPolicyName',17),('unsetTunnelQosPolicyName',18)))
_SleMplsTpTunnelCfgControlRequest_Type.__name__=_D
_SleMplsTpTunnelCfgControlRequest_Object=MibScalar
sleMplsTpTunnelCfgControlRequest=_SleMplsTpTunnelCfgControlRequest_Object((1,3,6,1,4,1,6296,101,16,14,1,2,1),_SleMplsTpTunnelCfgControlRequest_Type())
sleMplsTpTunnelCfgControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlRequest.setStatus(_A)
_SleMplsTpTunnelCfgControlStatus_Type=SleControlStatusType
_SleMplsTpTunnelCfgControlStatus_Object=MibScalar
sleMplsTpTunnelCfgControlStatus=_SleMplsTpTunnelCfgControlStatus_Object((1,3,6,1,4,1,6296,101,16,14,1,2,2),_SleMplsTpTunnelCfgControlStatus_Type())
sleMplsTpTunnelCfgControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlStatus.setStatus(_A)
_SleMplsTpTunnelCfgControlTimer_Type=Gauge32
_SleMplsTpTunnelCfgControlTimer_Object=MibScalar
sleMplsTpTunnelCfgControlTimer=_SleMplsTpTunnelCfgControlTimer_Object((1,3,6,1,4,1,6296,101,16,14,1,2,3),_SleMplsTpTunnelCfgControlTimer_Type())
sleMplsTpTunnelCfgControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlTimer.setStatus(_A)
_SleMplsTpTunnelCfgControlTimeStamp_Type=TimeTicks
_SleMplsTpTunnelCfgControlTimeStamp_Object=MibScalar
sleMplsTpTunnelCfgControlTimeStamp=_SleMplsTpTunnelCfgControlTimeStamp_Object((1,3,6,1,4,1,6296,101,16,14,1,2,4),_SleMplsTpTunnelCfgControlTimeStamp_Type())
sleMplsTpTunnelCfgControlTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlTimeStamp.setStatus(_A)
_SleMplsTpTunnelCfgControlReqResult_Type=SleControlRequestResultType
_SleMplsTpTunnelCfgControlReqResult_Object=MibScalar
sleMplsTpTunnelCfgControlReqResult=_SleMplsTpTunnelCfgControlReqResult_Object((1,3,6,1,4,1,6296,101,16,14,1,2,5),_SleMplsTpTunnelCfgControlReqResult_Type())
sleMplsTpTunnelCfgControlReqResult.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlReqResult.setStatus(_A)
class _SleMplsTpTunnelCfgControlName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SleMplsTpTunnelCfgControlName_Type.__name__=_I
_SleMplsTpTunnelCfgControlName_Object=MibScalar
sleMplsTpTunnelCfgControlName=_SleMplsTpTunnelCfgControlName_Object((1,3,6,1,4,1,6296,101,16,14,1,2,6),_SleMplsTpTunnelCfgControlName_Type())
sleMplsTpTunnelCfgControlName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlName.setStatus(_A)
class _SleMplsTpTunnelCfgControlId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SleMplsTpTunnelCfgControlId_Type.__name__=_E
_SleMplsTpTunnelCfgControlId_Object=MibScalar
sleMplsTpTunnelCfgControlId=_SleMplsTpTunnelCfgControlId_Object((1,3,6,1,4,1,6296,101,16,14,1,2,7),_SleMplsTpTunnelCfgControlId_Type())
sleMplsTpTunnelCfgControlId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlId.setStatus(_A)
class _SleMplsTpTunnelCfgControlSrcIdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SleMplsTpTunnelCfgControlSrcIdType_Type.__name__=_D
_SleMplsTpTunnelCfgControlSrcIdType_Object=MibScalar
sleMplsTpTunnelCfgControlSrcIdType=_SleMplsTpTunnelCfgControlSrcIdType_Object((1,3,6,1,4,1,6296,101,16,14,1,2,8),_SleMplsTpTunnelCfgControlSrcIdType_Type())
sleMplsTpTunnelCfgControlSrcIdType.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlSrcIdType.setStatus(_A)
class _SleMplsTpTunnelCfgControlSrcGId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_SleMplsTpTunnelCfgControlSrcGId_Type.__name__=_E
_SleMplsTpTunnelCfgControlSrcGId_Object=MibScalar
sleMplsTpTunnelCfgControlSrcGId=_SleMplsTpTunnelCfgControlSrcGId_Object((1,3,6,1,4,1,6296,101,16,14,1,2,9),_SleMplsTpTunnelCfgControlSrcGId_Type())
sleMplsTpTunnelCfgControlSrcGId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlSrcGId.setStatus(_A)
_SleMplsTpTunnelCfgControlSrcCc_Type=MplsCcId
_SleMplsTpTunnelCfgControlSrcCc_Object=MibScalar
sleMplsTpTunnelCfgControlSrcCc=_SleMplsTpTunnelCfgControlSrcCc_Object((1,3,6,1,4,1,6296,101,16,14,1,2,10),_SleMplsTpTunnelCfgControlSrcCc_Type())
sleMplsTpTunnelCfgControlSrcCc.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlSrcCc.setStatus(_A)
_SleMplsTpTunnelCfgControlSrcIcc_Type=MplsIccId
_SleMplsTpTunnelCfgControlSrcIcc_Object=MibScalar
sleMplsTpTunnelCfgControlSrcIcc=_SleMplsTpTunnelCfgControlSrcIcc_Object((1,3,6,1,4,1,6296,101,16,14,1,2,11),_SleMplsTpTunnelCfgControlSrcIcc_Type())
sleMplsTpTunnelCfgControlSrcIcc.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlSrcIcc.setStatus(_A)
_SleMplsTpTunnelCfgControlSrcNodeId_Type=IpAddress
_SleMplsTpTunnelCfgControlSrcNodeId_Object=MibScalar
sleMplsTpTunnelCfgControlSrcNodeId=_SleMplsTpTunnelCfgControlSrcNodeId_Object((1,3,6,1,4,1,6296,101,16,14,1,2,12),_SleMplsTpTunnelCfgControlSrcNodeId_Type())
sleMplsTpTunnelCfgControlSrcNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlSrcNodeId.setStatus(_A)
class _SleMplsTpTunnelCfgControlDestIdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SleMplsTpTunnelCfgControlDestIdType_Type.__name__=_D
_SleMplsTpTunnelCfgControlDestIdType_Object=MibScalar
sleMplsTpTunnelCfgControlDestIdType=_SleMplsTpTunnelCfgControlDestIdType_Object((1,3,6,1,4,1,6296,101,16,14,1,2,13),_SleMplsTpTunnelCfgControlDestIdType_Type())
sleMplsTpTunnelCfgControlDestIdType.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlDestIdType.setStatus(_A)
class _SleMplsTpTunnelCfgControlDestGId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_SleMplsTpTunnelCfgControlDestGId_Type.__name__=_E
_SleMplsTpTunnelCfgControlDestGId_Object=MibScalar
sleMplsTpTunnelCfgControlDestGId=_SleMplsTpTunnelCfgControlDestGId_Object((1,3,6,1,4,1,6296,101,16,14,1,2,14),_SleMplsTpTunnelCfgControlDestGId_Type())
sleMplsTpTunnelCfgControlDestGId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlDestGId.setStatus(_A)
_SleMplsTpTunnelCfgControlDestCc_Type=MplsCcId
_SleMplsTpTunnelCfgControlDestCc_Object=MibScalar
sleMplsTpTunnelCfgControlDestCc=_SleMplsTpTunnelCfgControlDestCc_Object((1,3,6,1,4,1,6296,101,16,14,1,2,15),_SleMplsTpTunnelCfgControlDestCc_Type())
sleMplsTpTunnelCfgControlDestCc.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlDestCc.setStatus(_A)
_SleMplsTpTunnelCfgControlDestIcc_Type=MplsIccId
_SleMplsTpTunnelCfgControlDestIcc_Object=MibScalar
sleMplsTpTunnelCfgControlDestIcc=_SleMplsTpTunnelCfgControlDestIcc_Object((1,3,6,1,4,1,6296,101,16,14,1,2,16),_SleMplsTpTunnelCfgControlDestIcc_Type())
sleMplsTpTunnelCfgControlDestIcc.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlDestIcc.setStatus(_A)
_SleMplsTpTunnelCfgControlDestNodeId_Type=IpAddress
_SleMplsTpTunnelCfgControlDestNodeId_Object=MibScalar
sleMplsTpTunnelCfgControlDestNodeId=_SleMplsTpTunnelCfgControlDestNodeId_Object((1,3,6,1,4,1,6296,101,16,14,1,2,17),_SleMplsTpTunnelCfgControlDestNodeId_Type())
sleMplsTpTunnelCfgControlDestNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlDestNodeId.setStatus(_A)
class _SleMplsTpTunnelCfgControlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_SleMplsTpTunnelCfgControlMode_Type.__name__=_D
_SleMplsTpTunnelCfgControlMode_Object=MibScalar
sleMplsTpTunnelCfgControlMode=_SleMplsTpTunnelCfgControlMode_Object((1,3,6,1,4,1,6296,101,16,14,1,2,18),_SleMplsTpTunnelCfgControlMode_Type())
sleMplsTpTunnelCfgControlMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlMode.setStatus(_A)
class _SleMplsTpTunnelCfgControlPath_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forwardPath',1),('reversePath',2)))
_SleMplsTpTunnelCfgControlPath_Type.__name__=_D
_SleMplsTpTunnelCfgControlPath_Object=MibScalar
sleMplsTpTunnelCfgControlPath=_SleMplsTpTunnelCfgControlPath_Object((1,3,6,1,4,1,6296,101,16,14,1,2,19),_SleMplsTpTunnelCfgControlPath_Type())
sleMplsTpTunnelCfgControlPath.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlPath.setStatus(_A)
_SleMplsTpTunnelCfgControlInLabel_Type=MplsLabel
_SleMplsTpTunnelCfgControlInLabel_Object=MibScalar
sleMplsTpTunnelCfgControlInLabel=_SleMplsTpTunnelCfgControlInLabel_Object((1,3,6,1,4,1,6296,101,16,14,1,2,20),_SleMplsTpTunnelCfgControlInLabel_Type())
sleMplsTpTunnelCfgControlInLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlInLabel.setStatus(_A)
_SleMplsTpTunnelCfgControlInInterface_Type=InterfaceIndexOrZero
_SleMplsTpTunnelCfgControlInInterface_Object=MibScalar
sleMplsTpTunnelCfgControlInInterface=_SleMplsTpTunnelCfgControlInInterface_Object((1,3,6,1,4,1,6296,101,16,14,1,2,21),_SleMplsTpTunnelCfgControlInInterface_Type())
sleMplsTpTunnelCfgControlInInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlInInterface.setStatus(_A)
class _SleMplsTpTunnelCfgControlOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3)))
_SleMplsTpTunnelCfgControlOperation_Type.__name__=_D
_SleMplsTpTunnelCfgControlOperation_Object=MibScalar
sleMplsTpTunnelCfgControlOperation=_SleMplsTpTunnelCfgControlOperation_Object((1,3,6,1,4,1,6296,101,16,14,1,2,22),_SleMplsTpTunnelCfgControlOperation_Type())
sleMplsTpTunnelCfgControlOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlOperation.setStatus(_A)
_SleMplsTpTunnelCfgControlOutLabel_Type=MplsLabel
_SleMplsTpTunnelCfgControlOutLabel_Object=MibScalar
sleMplsTpTunnelCfgControlOutLabel=_SleMplsTpTunnelCfgControlOutLabel_Object((1,3,6,1,4,1,6296,101,16,14,1,2,23),_SleMplsTpTunnelCfgControlOutLabel_Type())
sleMplsTpTunnelCfgControlOutLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlOutLabel.setStatus(_A)
_SleMplsTpTunnelCfgControlOutInterface_Type=InterfaceIndexOrZero
_SleMplsTpTunnelCfgControlOutInterface_Object=MibScalar
sleMplsTpTunnelCfgControlOutInterface=_SleMplsTpTunnelCfgControlOutInterface_Object((1,3,6,1,4,1,6296,101,16,14,1,2,24),_SleMplsTpTunnelCfgControlOutInterface_Type())
sleMplsTpTunnelCfgControlOutInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlOutInterface.setStatus(_A)
_SleMplsTpTunnelCfgControlOutMacAddress_Type=MacAddress
_SleMplsTpTunnelCfgControlOutMacAddress_Object=MibScalar
sleMplsTpTunnelCfgControlOutMacAddress=_SleMplsTpTunnelCfgControlOutMacAddress_Object((1,3,6,1,4,1,6296,101,16,14,1,2,25),_SleMplsTpTunnelCfgControlOutMacAddress_Type())
sleMplsTpTunnelCfgControlOutMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlOutMacAddress.setStatus(_A)
_SleMplsTpTunnelCfgControlAssociateTnlName_Type=OctetString
_SleMplsTpTunnelCfgControlAssociateTnlName_Object=MibScalar
sleMplsTpTunnelCfgControlAssociateTnlName=_SleMplsTpTunnelCfgControlAssociateTnlName_Object((1,3,6,1,4,1,6296,101,16,14,1,2,26),_SleMplsTpTunnelCfgControlAssociateTnlName_Type())
sleMplsTpTunnelCfgControlAssociateTnlName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlAssociateTnlName.setStatus(_A)
_SleMplsTpTunnelCfgControlDescription_Type=OctetString
_SleMplsTpTunnelCfgControlDescription_Object=MibScalar
sleMplsTpTunnelCfgControlDescription=_SleMplsTpTunnelCfgControlDescription_Object((1,3,6,1,4,1,6296,101,16,14,1,2,27),_SleMplsTpTunnelCfgControlDescription_Type())
sleMplsTpTunnelCfgControlDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlDescription.setStatus(_A)
_SleMplsTpTunnelCfgControlHlspSeverTunnelName_Type=OctetString
_SleMplsTpTunnelCfgControlHlspSeverTunnelName_Object=MibScalar
sleMplsTpTunnelCfgControlHlspSeverTunnelName=_SleMplsTpTunnelCfgControlHlspSeverTunnelName_Object((1,3,6,1,4,1,6296,101,16,14,1,2,28),_SleMplsTpTunnelCfgControlHlspSeverTunnelName_Type())
sleMplsTpTunnelCfgControlHlspSeverTunnelName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlHlspSeverTunnelName.setStatus(_A)
_SleMplsTpTunnelCfgControlQosPolicyName_Type=OctetString
_SleMplsTpTunnelCfgControlQosPolicyName_Object=MibScalar
sleMplsTpTunnelCfgControlQosPolicyName=_SleMplsTpTunnelCfgControlQosPolicyName_Object((1,3,6,1,4,1,6296,101,16,14,1,2,29),_SleMplsTpTunnelCfgControlQosPolicyName_Type())
sleMplsTpTunnelCfgControlQosPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpTunnelCfgControlQosPolicyName.setStatus(_A)
mibBuilder.exportSymbols(_N,**{'sleMpls':sleMpls,'sleMplsTpTunnel':sleMplsTpTunnel,'sleMplsTpTunnelCfg':sleMplsTpTunnelCfg,'sleMplsTpTunnelCfgInfoTable':sleMplsTpTunnelCfgInfoTable,'sleMplsTpTunnelCfgInfoEntry':sleMplsTpTunnelCfgInfoEntry,_O:sleMplsTpTunnelCfgInfoIndex,'sleMplsTpTunnelCfgInfoName':sleMplsTpTunnelCfgInfoName,'sleMplsTpTunnelCfgInfoId':sleMplsTpTunnelCfgInfoId,'sleMplsTpTunnelCfgInfoSrcIdType':sleMplsTpTunnelCfgInfoSrcIdType,'sleMplsTpTunnelCfgInfoSrcGId':sleMplsTpTunnelCfgInfoSrcGId,'sleMplsTpTunnelCfgInfoSrcCc':sleMplsTpTunnelCfgInfoSrcCc,'sleMplsTpTunnelCfgInfoSrcIcc':sleMplsTpTunnelCfgInfoSrcIcc,'sleMplsTpTunnelCfgInfoSrcNodeId':sleMplsTpTunnelCfgInfoSrcNodeId,'sleMplsTpTunnelCfgInfoDestIdType':sleMplsTpTunnelCfgInfoDestIdType,'sleMplsTpTunnelCfgInfoDestGId':sleMplsTpTunnelCfgInfoDestGId,'sleMplsTpTunnelCfgInfoDestCc':sleMplsTpTunnelCfgInfoDestCc,'sleMplsTpTunnelCfgInfoDestIcc':sleMplsTpTunnelCfgInfoDestIcc,'sleMplsTpTunnelCfgInfoDestNodeId':sleMplsTpTunnelCfgInfoDestNodeId,'sleMplsTpTunnelCfgInfoMode':sleMplsTpTunnelCfgInfoMode,'sleMplsTpTunnelCfgInfoFwdInLabel':sleMplsTpTunnelCfgInfoFwdInLabel,'sleMplsTpTunnelCfgInfoFwdInIfIndex':sleMplsTpTunnelCfgInfoFwdInIfIndex,'sleMplsTpTunnelCfgInfoFwdOperation':sleMplsTpTunnelCfgInfoFwdOperation,'sleMplsTpTunnelCfgInfoFwdOutLabel':sleMplsTpTunnelCfgInfoFwdOutLabel,'sleMplsTpTunnelCfgInfoFwdOutIfIndex':sleMplsTpTunnelCfgInfoFwdOutIfIndex,'sleMplsTpTunnelCfgInfoFwdOutMac':sleMplsTpTunnelCfgInfoFwdOutMac,'sleMplsTpTunnelCfgInfoRevInLabel':sleMplsTpTunnelCfgInfoRevInLabel,'sleMplsTpTunnelCfgInfoRevInIfIndex':sleMplsTpTunnelCfgInfoRevInIfIndex,'sleMplsTpTunnelCfgInfoRevOperation':sleMplsTpTunnelCfgInfoRevOperation,'sleMplsTpTunnelCfgInfoRevOutLabel':sleMplsTpTunnelCfgInfoRevOutLabel,'sleMplsTpTunnelCfgInfoRevOutIfIndex':sleMplsTpTunnelCfgInfoRevOutIfIndex,'sleMplsTpTunnelCfgInfoRevOutMac':sleMplsTpTunnelCfgInfoRevOutMac,'sleMplsTpTunnelCfgInfoState':sleMplsTpTunnelCfgInfoState,'sleMplsTpTunnelCfgInfoRole':sleMplsTpTunnelCfgInfoRole,'sleMplsTpTunnelCfgInfoAssociateTnlName':sleMplsTpTunnelCfgInfoAssociateTnlName,'sleMplsTpTunnelCfgInfoDescription':sleMplsTpTunnelCfgInfoDescription,'sleMplsTpTunnelCfgInfoHlspRole':sleMplsTpTunnelCfgInfoHlspRole,'sleMplsTpTunnelCfgInfoHlspServerTunnelName':sleMplsTpTunnelCfgInfoHlspServerTunnelName,'sleMplsTpTunnelCfgInfoQosPolicyName':sleMplsTpTunnelCfgInfoQosPolicyName,'sleMplsTpTunnelCfgControl':sleMplsTpTunnelCfgControl,'sleMplsTpTunnelCfgControlRequest':sleMplsTpTunnelCfgControlRequest,'sleMplsTpTunnelCfgControlStatus':sleMplsTpTunnelCfgControlStatus,'sleMplsTpTunnelCfgControlTimer':sleMplsTpTunnelCfgControlTimer,'sleMplsTpTunnelCfgControlTimeStamp':sleMplsTpTunnelCfgControlTimeStamp,'sleMplsTpTunnelCfgControlReqResult':sleMplsTpTunnelCfgControlReqResult,'sleMplsTpTunnelCfgControlName':sleMplsTpTunnelCfgControlName,'sleMplsTpTunnelCfgControlId':sleMplsTpTunnelCfgControlId,'sleMplsTpTunnelCfgControlSrcIdType':sleMplsTpTunnelCfgControlSrcIdType,'sleMplsTpTunnelCfgControlSrcGId':sleMplsTpTunnelCfgControlSrcGId,'sleMplsTpTunnelCfgControlSrcCc':sleMplsTpTunnelCfgControlSrcCc,'sleMplsTpTunnelCfgControlSrcIcc':sleMplsTpTunnelCfgControlSrcIcc,'sleMplsTpTunnelCfgControlSrcNodeId':sleMplsTpTunnelCfgControlSrcNodeId,'sleMplsTpTunnelCfgControlDestIdType':sleMplsTpTunnelCfgControlDestIdType,'sleMplsTpTunnelCfgControlDestGId':sleMplsTpTunnelCfgControlDestGId,'sleMplsTpTunnelCfgControlDestCc':sleMplsTpTunnelCfgControlDestCc,'sleMplsTpTunnelCfgControlDestIcc':sleMplsTpTunnelCfgControlDestIcc,'sleMplsTpTunnelCfgControlDestNodeId':sleMplsTpTunnelCfgControlDestNodeId,'sleMplsTpTunnelCfgControlMode':sleMplsTpTunnelCfgControlMode,'sleMplsTpTunnelCfgControlPath':sleMplsTpTunnelCfgControlPath,'sleMplsTpTunnelCfgControlInLabel':sleMplsTpTunnelCfgControlInLabel,'sleMplsTpTunnelCfgControlInInterface':sleMplsTpTunnelCfgControlInInterface,'sleMplsTpTunnelCfgControlOperation':sleMplsTpTunnelCfgControlOperation,'sleMplsTpTunnelCfgControlOutLabel':sleMplsTpTunnelCfgControlOutLabel,'sleMplsTpTunnelCfgControlOutInterface':sleMplsTpTunnelCfgControlOutInterface,'sleMplsTpTunnelCfgControlOutMacAddress':sleMplsTpTunnelCfgControlOutMacAddress,'sleMplsTpTunnelCfgControlAssociateTnlName':sleMplsTpTunnelCfgControlAssociateTnlName,'sleMplsTpTunnelCfgControlDescription':sleMplsTpTunnelCfgControlDescription,'sleMplsTpTunnelCfgControlHlspSeverTunnelName':sleMplsTpTunnelCfgControlHlspSeverTunnelName,'sleMplsTpTunnelCfgControlQosPolicyName':sleMplsTpTunnelCfgControlQosPolicyName})