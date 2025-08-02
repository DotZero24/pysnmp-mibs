_t='mpCbQosPoliceActionCfgIndex'
_s='cells/second'
_r='mplsExp'
_q='discardClass'
_p='mpCbQosAtmVCI'
_o='mpCbQosAtmVPI'
_n='mpCbQosFrDLCI'
_m='setL2CosInner'
_l='setIpPrecedenceTunnel'
_k='setIpDscpTunnel'
_j='setMplsExpTopMost'
_i='setDiscardClass'
_h='setL2Cos'
_g='setFrDe'
_f='setAtmClp'
_e='setMplsExp'
_d='drop'
_c='setQosGroup'
_b='setIpPrecedence'
_a='setIpDSCP'
_Z='transmit'
_Y='% of Interface Bandwidth'
_X='mpCbQosREDValue'
_W='percentage'
_V='ifIndex'
_U='bits/second'
_T='mpCbQosPolicyDirection'
_S='not-accessible'
_R='us'
_Q='ms'
_P='cells'
_O='bytes'
_N='packets'
_M='DisplayString'
_L='bits per second'
_K='milli-seconds'
_J='mpCbQosObjectsIndex'
_I='mpCbQosPolicyIndex'
_H='mpCbQosConfigIndex'
_G='Unsigned32'
_F='Octets'
_E='Packets'
_D='Integer32'
_C='MAIPU-CBQOS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_M,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
maipuCBQosMIB=ModuleIdentity((1,3,6,1,4,1,5651,6,2,3,4))
class Unsigned64(TextualConvention,Counter64):status=_A
_Maipu_ObjectIdentity=ObjectIdentity
maipu=_Maipu_ObjectIdentity((1,3,6,1,4,1,5651))
_MpMgmt2_ObjectIdentity=ObjectIdentity
mpMgmt2=_MpMgmt2_ObjectIdentity((1,3,6,1,4,1,5651,6))
_MpRouterTech_ObjectIdentity=ObjectIdentity
mpRouterTech=_MpRouterTech_ObjectIdentity((1,3,6,1,4,1,5651,6,2))
_MpRtQoSv2_ObjectIdentity=ObjectIdentity
mpRtQoSv2=_MpRtQoSv2_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3))
_MaipuCBQosMIBObjects_ObjectIdentity=ObjectIdentity
maipuCBQosMIBObjects=_MaipuCBQosMIBObjects_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,4,1))
_MpCbQosServicePolicy_ObjectIdentity=ObjectIdentity
mpCbQosServicePolicy=_MpCbQosServicePolicy_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,4,1,1))
_MpCbQosServicePolicyTable_Object=MibTable
mpCbQosServicePolicyTable=_MpCbQosServicePolicyTable_Object((1,3,6,1,4,1,5651,6,2,3,4,1,1,1))
if mibBuilder.loadTexts:mpCbQosServicePolicyTable.setStatus(_A)
_MpCbQosServicePolicyEntry_Object=MibTableRow
mpCbQosServicePolicyEntry=_MpCbQosServicePolicyEntry_Object((1,3,6,1,4,1,5651,6,2,3,4,1,1,1,1))
mpCbQosServicePolicyEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:mpCbQosServicePolicyEntry.setStatus(_A)
_MpCbQosPolicyIndex_Type=Unsigned32
_MpCbQosPolicyIndex_Object=MibTableColumn
mpCbQosPolicyIndex=_MpCbQosPolicyIndex_Object((1,3,6,1,4,1,5651,6,2,3,4,1,1,1,1,1),_MpCbQosPolicyIndex_Type())
mpCbQosPolicyIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:mpCbQosPolicyIndex.setStatus(_A)
class _MpCbQosIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('mainInterface',1),('subInterface',2),('frDLCI',3),('atmPVC',4),('controlPlane',5),('vlanPort',6)))
_MpCbQosIfType_Type.__name__=_D
_MpCbQosIfType_Object=MibTableColumn
mpCbQosIfType=_MpCbQosIfType_Object((1,3,6,1,4,1,5651,6,2,3,4,1,1,1,1,2),_MpCbQosIfType_Type())
mpCbQosIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosIfType.setStatus(_A)
class _MpCbQosPolicyDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('input',1),('output',2)))
_MpCbQosPolicyDirection_Type.__name__=_D
_MpCbQosPolicyDirection_Object=MibTableColumn
mpCbQosPolicyDirection=_MpCbQosPolicyDirection_Object((1,3,6,1,4,1,5651,6,2,3,4,1,1,1,1,3),_MpCbQosPolicyDirection_Type())
mpCbQosPolicyDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPolicyDirection.setStatus(_A)
_MpCbQosIfIndex_Type=Integer32
_MpCbQosIfIndex_Object=MibTableColumn
mpCbQosIfIndex=_MpCbQosIfIndex_Object((1,3,6,1,4,1,5651,6,2,3,4,1,1,1,1,4),_MpCbQosIfIndex_Type())
mpCbQosIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosIfIndex.setStatus(_A)
class _MpCbQosFrDLCI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1007))
_MpCbQosFrDLCI_Type.__name__=_G
_MpCbQosFrDLCI_Object=MibTableColumn
mpCbQosFrDLCI=_MpCbQosFrDLCI_Object((1,3,6,1,4,1,5651,6,2,3,4,1,1,1,1,5),_MpCbQosFrDLCI_Type())
mpCbQosFrDLCI.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosFrDLCI.setStatus(_A)
class _MpCbQosAtmVPI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_MpCbQosAtmVPI_Type.__name__=_G
_MpCbQosAtmVPI_Object=MibTableColumn
mpCbQosAtmVPI=_MpCbQosAtmVPI_Object((1,3,6,1,4,1,5651,6,2,3,4,1,1,1,1,6),_MpCbQosAtmVPI_Type())
mpCbQosAtmVPI.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosAtmVPI.setStatus(_A)
class _MpCbQosAtmVCI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MpCbQosAtmVCI_Type.__name__=_G
_MpCbQosAtmVCI_Object=MibTableColumn
mpCbQosAtmVCI=_MpCbQosAtmVCI_Object((1,3,6,1,4,1,5651,6,2,3,4,1,1,1,1,7),_MpCbQosAtmVCI_Type())
mpCbQosAtmVCI.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosAtmVCI.setStatus(_A)
_MpCbQosEntityIndex_Type=Integer32
_MpCbQosEntityIndex_Object=MibTableColumn
mpCbQosEntityIndex=_MpCbQosEntityIndex_Object((1,3,6,1,4,1,5651,6,2,3,4,1,1,1,1,8),_MpCbQosEntityIndex_Type())
mpCbQosEntityIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosEntityIndex.setStatus(_A)
class _MpCbQosVlanIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_MpCbQosVlanIndex_Type.__name__=_G
_MpCbQosVlanIndex_Object=MibTableColumn
mpCbQosVlanIndex=_MpCbQosVlanIndex_Object((1,3,6,1,4,1,5651,6,2,3,4,1,1,1,1,9),_MpCbQosVlanIndex_Type())
mpCbQosVlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosVlanIndex.setStatus(_A)
_MpCbQosInterfacePolicy_ObjectIdentity=ObjectIdentity
mpCbQosInterfacePolicy=_MpCbQosInterfacePolicy_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,4,1,2))
_MpCbQosInterfacePolicyTable_Object=MibTable
mpCbQosInterfacePolicyTable=_MpCbQosInterfacePolicyTable_Object((1,3,6,1,4,1,5651,6,2,3,4,1,2,1))
if mibBuilder.loadTexts:mpCbQosInterfacePolicyTable.setStatus(_A)
_MpCbQosInterfacePolicyEntry_Object=MibTableRow
mpCbQosInterfacePolicyEntry=_MpCbQosInterfacePolicyEntry_Object((1,3,6,1,4,1,5651,6,2,3,4,1,2,1,1))
mpCbQosInterfacePolicyEntry.setIndexNames((0,_C,_V),(0,_C,_T))
if mibBuilder.loadTexts:mpCbQosInterfacePolicyEntry.setStatus(_A)
_MpCbQosIFPolicyIndex_Type=Unsigned32
_MpCbQosIFPolicyIndex_Object=MibTableColumn
mpCbQosIFPolicyIndex=_MpCbQosIFPolicyIndex_Object((1,3,6,1,4,1,5651,6,2,3,4,1,2,1,1,1),_MpCbQosIFPolicyIndex_Type())
mpCbQosIFPolicyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosIFPolicyIndex.setStatus(_A)
_MpCbQosFrameRelayVCPolicy_ObjectIdentity=ObjectIdentity
mpCbQosFrameRelayVCPolicy=_MpCbQosFrameRelayVCPolicy_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,4,1,3))
_MpCbQosFrameRelayPolicyTable_Object=MibTable
mpCbQosFrameRelayPolicyTable=_MpCbQosFrameRelayPolicyTable_Object((1,3,6,1,4,1,5651,6,2,3,4,1,3,1))
if mibBuilder.loadTexts:mpCbQosFrameRelayPolicyTable.setStatus(_A)
_MpCbQosFrameRelayPolicyEntry_Object=MibTableRow
mpCbQosFrameRelayPolicyEntry=_MpCbQosFrameRelayPolicyEntry_Object((1,3,6,1,4,1,5651,6,2,3,4,1,3,1,1))
mpCbQosFrameRelayPolicyEntry.setIndexNames((0,_C,_V),(0,_C,_n),(0,_C,_T))
if mibBuilder.loadTexts:mpCbQosFrameRelayPolicyEntry.setStatus(_A)
_MpCbQosFRPolicyIndex_Type=Unsigned32
_MpCbQosFRPolicyIndex_Object=MibTableColumn
mpCbQosFRPolicyIndex=_MpCbQosFRPolicyIndex_Object((1,3,6,1,4,1,5651,6,2,3,4,1,3,1,1,1),_MpCbQosFRPolicyIndex_Type())
mpCbQosFRPolicyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosFRPolicyIndex.setStatus(_A)
_MpCbQosATMPVCPolicy_ObjectIdentity=ObjectIdentity
mpCbQosATMPVCPolicy=_MpCbQosATMPVCPolicy_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,4,1,4))
_MpCbQosATMPVCPolicyTable_Object=MibTable
mpCbQosATMPVCPolicyTable=_MpCbQosATMPVCPolicyTable_Object((1,3,6,1,4,1,5651,6,2,3,4,1,4,1))
if mibBuilder.loadTexts:mpCbQosATMPVCPolicyTable.setStatus(_A)
_MpCbQosATMPVCPolicyEntry_Object=MibTableRow
mpCbQosATMPVCPolicyEntry=_MpCbQosATMPVCPolicyEntry_Object((1,3,6,1,4,1,5651,6,2,3,4,1,4,1,1))
mpCbQosATMPVCPolicyEntry.setIndexNames((0,_C,_V),(0,_C,_o),(0,_C,_p),(0,_C,_T))
if mibBuilder.loadTexts:mpCbQosATMPVCPolicyEntry.setStatus(_A)
_MpCbQosATMPVCPolicyIndex_Type=Unsigned32
_MpCbQosATMPVCPolicyIndex_Object=MibTableColumn
mpCbQosATMPVCPolicyIndex=_MpCbQosATMPVCPolicyIndex_Object((1,3,6,1,4,1,5651,6,2,3,4,1,4,1,1,1),_MpCbQosATMPVCPolicyIndex_Type())
mpCbQosATMPVCPolicyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosATMPVCPolicyIndex.setStatus(_A)
_MpCbQosObjects_ObjectIdentity=ObjectIdentity
mpCbQosObjects=_MpCbQosObjects_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,4,1,5))
_MpCbQosObjectsTable_Object=MibTable
mpCbQosObjectsTable=_MpCbQosObjectsTable_Object((1,3,6,1,4,1,5651,6,2,3,4,1,5,1))
if mibBuilder.loadTexts:mpCbQosObjectsTable.setStatus(_A)
_MpCbQosObjectsEntry_Object=MibTableRow
mpCbQosObjectsEntry=_MpCbQosObjectsEntry_Object((1,3,6,1,4,1,5651,6,2,3,4,1,5,1,1))
mpCbQosObjectsEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:mpCbQosObjectsEntry.setStatus(_A)
_MpCbQosObjectsIndex_Type=Unsigned32
_MpCbQosObjectsIndex_Object=MibTableColumn
mpCbQosObjectsIndex=_MpCbQosObjectsIndex_Object((1,3,6,1,4,1,5651,6,2,3,4,1,5,1,1,1),_MpCbQosObjectsIndex_Type())
mpCbQosObjectsIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:mpCbQosObjectsIndex.setStatus(_A)
_MpCbQosConfigIndex_Type=Unsigned32
_MpCbQosConfigIndex_Object=MibTableColumn
mpCbQosConfigIndex=_MpCbQosConfigIndex_Object((1,3,6,1,4,1,5651,6,2,3,4,1,5,1,1,2),_MpCbQosConfigIndex_Type())
mpCbQosConfigIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosConfigIndex.setStatus(_A)
class _MpCbQosObjectsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('policymap',1),('classmap',2),('matchStatement',3),('queueing',4),('randomDetect',5),('trafficShaping',6),('police',7),('set',8)))
_MpCbQosObjectsType_Type.__name__=_D
_MpCbQosObjectsType_Object=MibTableColumn
mpCbQosObjectsType=_MpCbQosObjectsType_Object((1,3,6,1,4,1,5651,6,2,3,4,1,5,1,1,3),_MpCbQosObjectsType_Type())
mpCbQosObjectsType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosObjectsType.setStatus(_A)
_MpCbQosParentObjectsIndex_Type=Unsigned32
_MpCbQosParentObjectsIndex_Object=MibTableColumn
mpCbQosParentObjectsIndex=_MpCbQosParentObjectsIndex_Object((1,3,6,1,4,1,5651,6,2,3,4,1,5,1,1,4),_MpCbQosParentObjectsIndex_Type())
mpCbQosParentObjectsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosParentObjectsIndex.setStatus(_A)
_MpCbQosPolicyMapCfg_ObjectIdentity=ObjectIdentity
mpCbQosPolicyMapCfg=_MpCbQosPolicyMapCfg_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,4,1,6))
_MpCbQosPolicyMapCfgTable_Object=MibTable
mpCbQosPolicyMapCfgTable=_MpCbQosPolicyMapCfgTable_Object((1,3,6,1,4,1,5651,6,2,3,4,1,6,1))
if mibBuilder.loadTexts:mpCbQosPolicyMapCfgTable.setStatus(_A)
_MpCbQosPolicyMapCfgEntry_Object=MibTableRow
mpCbQosPolicyMapCfgEntry=_MpCbQosPolicyMapCfgEntry_Object((1,3,6,1,4,1,5651,6,2,3,4,1,6,1,1))
mpCbQosPolicyMapCfgEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:mpCbQosPolicyMapCfgEntry.setStatus(_A)
class _MpCbQosPolicyMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MpCbQosPolicyMapName_Type.__name__=_M
_MpCbQosPolicyMapName_Object=MibTableColumn
mpCbQosPolicyMapName=_MpCbQosPolicyMapName_Object((1,3,6,1,4,1,5651,6,2,3,4,1,6,1,1,1),_MpCbQosPolicyMapName_Type())
mpCbQosPolicyMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPolicyMapName.setStatus(_A)
class _MpCbQosPolicyMapDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MpCbQosPolicyMapDesc_Type.__name__=_M
_MpCbQosPolicyMapDesc_Object=MibTableColumn
mpCbQosPolicyMapDesc=_MpCbQosPolicyMapDesc_Object((1,3,6,1,4,1,5651,6,2,3,4,1,6,1,1,2),_MpCbQosPolicyMapDesc_Type())
mpCbQosPolicyMapDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPolicyMapDesc.setStatus(_A)
_MpCbQosClassMapCfg_ObjectIdentity=ObjectIdentity
mpCbQosClassMapCfg=_MpCbQosClassMapCfg_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,4,1,7))
_MpCbQosCMCfgTable_Object=MibTable
mpCbQosCMCfgTable=_MpCbQosCMCfgTable_Object((1,3,6,1,4,1,5651,6,2,3,4,1,7,1))
if mibBuilder.loadTexts:mpCbQosCMCfgTable.setStatus(_A)
_MpCbQosCMCfgEntry_Object=MibTableRow
mpCbQosCMCfgEntry=_MpCbQosCMCfgEntry_Object((1,3,6,1,4,1,5651,6,2,3,4,1,7,1,1))
mpCbQosCMCfgEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:mpCbQosCMCfgEntry.setStatus(_A)
class _MpCbQosCMName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MpCbQosCMName_Type.__name__=_M
_MpCbQosCMName_Object=MibTableColumn
mpCbQosCMName=_MpCbQosCMName_Object((1,3,6,1,4,1,5651,6,2,3,4,1,7,1,1,1),_MpCbQosCMName_Type())
mpCbQosCMName.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosCMName.setStatus(_A)
class _MpCbQosCMDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MpCbQosCMDesc_Type.__name__=_M
_MpCbQosCMDesc_Object=MibTableColumn
mpCbQosCMDesc=_MpCbQosCMDesc_Object((1,3,6,1,4,1,5651,6,2,3,4,1,7,1,1,2),_MpCbQosCMDesc_Type())
mpCbQosCMDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosCMDesc.setStatus(_A)
class _MpCbQosCMInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('matchAll',2),('matchAny',3)))
_MpCbQosCMInfo_Type.__name__=_D
_MpCbQosCMInfo_Object=MibTableColumn
mpCbQosCMInfo=_MpCbQosCMInfo_Object((1,3,6,1,4,1,5651,6,2,3,4,1,7,1,1,3),_MpCbQosCMInfo_Type())
mpCbQosCMInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosCMInfo.setStatus(_A)
_MpCbQosMatchStmtCfg_ObjectIdentity=ObjectIdentity
mpCbQosMatchStmtCfg=_MpCbQosMatchStmtCfg_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,4,1,8))
_MpCbQosMatchStmtCfgTable_Object=MibTable
mpCbQosMatchStmtCfgTable=_MpCbQosMatchStmtCfgTable_Object((1,3,6,1,4,1,5651,6,2,3,4,1,8,1))
if mibBuilder.loadTexts:mpCbQosMatchStmtCfgTable.setStatus(_A)
_MpCbQosMatchStmtCfgEntry_Object=MibTableRow
mpCbQosMatchStmtCfgEntry=_MpCbQosMatchStmtCfgEntry_Object((1,3,6,1,4,1,5651,6,2,3,4,1,8,1,1))
mpCbQosMatchStmtCfgEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:mpCbQosMatchStmtCfgEntry.setStatus(_A)
class _MpCbQosMatchStmtName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MpCbQosMatchStmtName_Type.__name__=_M
_MpCbQosMatchStmtName_Object=MibTableColumn
mpCbQosMatchStmtName=_MpCbQosMatchStmtName_Object((1,3,6,1,4,1,5651,6,2,3,4,1,8,1,1,1),_MpCbQosMatchStmtName_Type())
mpCbQosMatchStmtName.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosMatchStmtName.setStatus(_A)
class _MpCbQosMatchStmtInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('matchNot',2)))
_MpCbQosMatchStmtInfo_Type.__name__=_D
_MpCbQosMatchStmtInfo_Object=MibTableColumn
mpCbQosMatchStmtInfo=_MpCbQosMatchStmtInfo_Object((1,3,6,1,4,1,5651,6,2,3,4,1,8,1,1,2),_MpCbQosMatchStmtInfo_Type())
mpCbQosMatchStmtInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosMatchStmtInfo.setStatus(_A)
_MpCbQosQueueingCfg_ObjectIdentity=ObjectIdentity
mpCbQosQueueingCfg=_MpCbQosQueueingCfg_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,4,1,9))
_MpCbQosQueueingCfgTable_Object=MibTable
mpCbQosQueueingCfgTable=_MpCbQosQueueingCfgTable_Object((1,3,6,1,4,1,5651,6,2,3,4,1,9,1))
if mibBuilder.loadTexts:mpCbQosQueueingCfgTable.setStatus(_A)
_MpCbQosQueueingCfgEntry_Object=MibTableRow
mpCbQosQueueingCfgEntry=_MpCbQosQueueingCfgEntry_Object((1,3,6,1,4,1,5651,6,2,3,4,1,9,1,1))
mpCbQosQueueingCfgEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:mpCbQosQueueingCfgEntry.setStatus(_A)
_MpCbQosQueueingCfgBandwidth_Type=Unsigned32
_MpCbQosQueueingCfgBandwidth_Object=MibTableColumn
mpCbQosQueueingCfgBandwidth=_MpCbQosQueueingCfgBandwidth_Object((1,3,6,1,4,1,5651,6,2,3,4,1,9,1,1,1),_MpCbQosQueueingCfgBandwidth_Type())
mpCbQosQueueingCfgBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosQueueingCfgBandwidth.setStatus(_A)
class _MpCbQosQueueingCfgBandwidthUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('kbps',1),(_W,2),('percentageRemaining',3),('ratioRemaining',4)))
_MpCbQosQueueingCfgBandwidthUnits_Type.__name__=_D
_MpCbQosQueueingCfgBandwidthUnits_Object=MibTableColumn
mpCbQosQueueingCfgBandwidthUnits=_MpCbQosQueueingCfgBandwidthUnits_Object((1,3,6,1,4,1,5651,6,2,3,4,1,9,1,1,2),_MpCbQosQueueingCfgBandwidthUnits_Type())
mpCbQosQueueingCfgBandwidthUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosQueueingCfgBandwidthUnits.setStatus(_A)
_MpCbQosQueueingCfgFlowEnabled_Type=TruthValue
_MpCbQosQueueingCfgFlowEnabled_Object=MibTableColumn
mpCbQosQueueingCfgFlowEnabled=_MpCbQosQueueingCfgFlowEnabled_Object((1,3,6,1,4,1,5651,6,2,3,4,1,9,1,1,3),_MpCbQosQueueingCfgFlowEnabled_Type())
mpCbQosQueueingCfgFlowEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosQueueingCfgFlowEnabled.setStatus(_A)
_MpCbQosQueueingCfgPriorityEnabled_Type=TruthValue
_MpCbQosQueueingCfgPriorityEnabled_Object=MibTableColumn
mpCbQosQueueingCfgPriorityEnabled=_MpCbQosQueueingCfgPriorityEnabled_Object((1,3,6,1,4,1,5651,6,2,3,4,1,9,1,1,4),_MpCbQosQueueingCfgPriorityEnabled_Type())
mpCbQosQueueingCfgPriorityEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosQueueingCfgPriorityEnabled.setStatus(_A)
class _MpCbQosQueueingCfgDynamicQNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32768))
_MpCbQosQueueingCfgDynamicQNumber_Type.__name__=_D
_MpCbQosQueueingCfgDynamicQNumber_Object=MibTableColumn
mpCbQosQueueingCfgDynamicQNumber=_MpCbQosQueueingCfgDynamicQNumber_Object((1,3,6,1,4,1,5651,6,2,3,4,1,9,1,1,5),_MpCbQosQueueingCfgDynamicQNumber_Type())
mpCbQosQueueingCfgDynamicQNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosQueueingCfgDynamicQNumber.setStatus(_A)
_MpCbQosQueueingCfgPrioBurstSize_Type=Unsigned32
_MpCbQosQueueingCfgPrioBurstSize_Object=MibTableColumn
mpCbQosQueueingCfgPrioBurstSize=_MpCbQosQueueingCfgPrioBurstSize_Object((1,3,6,1,4,1,5651,6,2,3,4,1,9,1,1,6),_MpCbQosQueueingCfgPrioBurstSize_Type())
mpCbQosQueueingCfgPrioBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosQueueingCfgPrioBurstSize.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosQueueingCfgPrioBurstSize.setUnits('Bytes')
class _MpCbQosQueueingCfgQLimitUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5)))
_MpCbQosQueueingCfgQLimitUnits_Type.__name__=_D
_MpCbQosQueueingCfgQLimitUnits_Object=MibTableColumn
mpCbQosQueueingCfgQLimitUnits=_MpCbQosQueueingCfgQLimitUnits_Object((1,3,6,1,4,1,5651,6,2,3,4,1,9,1,1,7),_MpCbQosQueueingCfgQLimitUnits_Type())
mpCbQosQueueingCfgQLimitUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosQueueingCfgQLimitUnits.setStatus(_A)
_MpCbQosQueueingCfgAggregateQLimit_Type=Unsigned32
_MpCbQosQueueingCfgAggregateQLimit_Object=MibTableColumn
mpCbQosQueueingCfgAggregateQLimit=_MpCbQosQueueingCfgAggregateQLimit_Object((1,3,6,1,4,1,5651,6,2,3,4,1,9,1,1,8),_MpCbQosQueueingCfgAggregateQLimit_Type())
mpCbQosQueueingCfgAggregateQLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosQueueingCfgAggregateQLimit.setStatus(_A)
_MpCbQosQueueingCfgAggrQLimitTime_Type=Unsigned32
_MpCbQosQueueingCfgAggrQLimitTime_Object=MibTableColumn
mpCbQosQueueingCfgAggrQLimitTime=_MpCbQosQueueingCfgAggrQLimitTime_Object((1,3,6,1,4,1,5651,6,2,3,4,1,9,1,1,9),_MpCbQosQueueingCfgAggrQLimitTime_Type())
mpCbQosQueueingCfgAggrQLimitTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosQueueingCfgAggrQLimitTime.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosQueueingCfgAggrQLimitTime.setUnits(_K)
_MpCbQosQueueingCfgIndividualQLimit_Type=Unsigned32
_MpCbQosQueueingCfgIndividualQLimit_Object=MibTableColumn
mpCbQosQueueingCfgIndividualQLimit=_MpCbQosQueueingCfgIndividualQLimit_Object((1,3,6,1,4,1,5651,6,2,3,4,1,9,1,1,10),_MpCbQosQueueingCfgIndividualQLimit_Type())
mpCbQosQueueingCfgIndividualQLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosQueueingCfgIndividualQLimit.setStatus(_A)
_MpCbQosREDCfg_ObjectIdentity=ObjectIdentity
mpCbQosREDCfg=_MpCbQosREDCfg_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,4,1,10))
_MpCbQosREDCfgTable_Object=MibTable
mpCbQosREDCfgTable=_MpCbQosREDCfgTable_Object((1,3,6,1,4,1,5651,6,2,3,4,1,10,1))
if mibBuilder.loadTexts:mpCbQosREDCfgTable.setStatus(_A)
_MpCbQosREDCfgEntry_Object=MibTableRow
mpCbQosREDCfgEntry=_MpCbQosREDCfgEntry_Object((1,3,6,1,4,1,5651,6,2,3,4,1,10,1,1))
mpCbQosREDCfgEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:mpCbQosREDCfgEntry.setStatus(_A)
class _MpCbQosREDCfgExponWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_MpCbQosREDCfgExponWeight_Type.__name__=_D
_MpCbQosREDCfgExponWeight_Object=MibTableColumn
mpCbQosREDCfgExponWeight=_MpCbQosREDCfgExponWeight_Object((1,3,6,1,4,1,5651,6,2,3,4,1,10,1,1,1),_MpCbQosREDCfgExponWeight_Type())
mpCbQosREDCfgExponWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosREDCfgExponWeight.setStatus(_A)
class _MpCbQosREDCfgDscpPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('precedence',1),('dscp',2),(_q,3),('l2Cos',4),('atmClp',5),(_r,6),('redDefault',7),('redUserDefault',8)))
_MpCbQosREDCfgDscpPrec_Type.__name__=_D
_MpCbQosREDCfgDscpPrec_Object=MibTableColumn
mpCbQosREDCfgDscpPrec=_MpCbQosREDCfgDscpPrec_Object((1,3,6,1,4,1,5651,6,2,3,4,1,10,1,1,2),_MpCbQosREDCfgDscpPrec_Type())
mpCbQosREDCfgDscpPrec.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosREDCfgDscpPrec.setStatus(_A)
_MpCbQosREDCfgECNEnabled_Type=TruthValue
_MpCbQosREDCfgECNEnabled_Object=MibTableColumn
mpCbQosREDCfgECNEnabled=_MpCbQosREDCfgECNEnabled_Object((1,3,6,1,4,1,5651,6,2,3,4,1,10,1,1,3),_MpCbQosREDCfgECNEnabled_Type())
mpCbQosREDCfgECNEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosREDCfgECNEnabled.setStatus(_A)
_MpCbQosREDClassCfg_ObjectIdentity=ObjectIdentity
mpCbQosREDClassCfg=_MpCbQosREDClassCfg_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,4,1,11))
_MpCbQosREDClassCfgTable_Object=MibTable
mpCbQosREDClassCfgTable=_MpCbQosREDClassCfgTable_Object((1,3,6,1,4,1,5651,6,2,3,4,1,11,1))
if mibBuilder.loadTexts:mpCbQosREDClassCfgTable.setStatus(_A)
_MpCbQosREDClassCfgEntry_Object=MibTableRow
mpCbQosREDClassCfgEntry=_MpCbQosREDClassCfgEntry_Object((1,3,6,1,4,1,5651,6,2,3,4,1,11,1,1))
mpCbQosREDClassCfgEntry.setIndexNames((0,_C,_H),(0,_C,_X))
if mibBuilder.loadTexts:mpCbQosREDClassCfgEntry.setStatus(_A)
class _MpCbQosREDValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_MpCbQosREDValue_Type.__name__=_D
_MpCbQosREDValue_Object=MibTableColumn
mpCbQosREDValue=_MpCbQosREDValue_Object((1,3,6,1,4,1,5651,6,2,3,4,1,11,1,1,1),_MpCbQosREDValue_Type())
mpCbQosREDValue.setMaxAccess(_S)
if mibBuilder.loadTexts:mpCbQosREDValue.setStatus(_A)
class _MpCbQosREDCfgPktDropProb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_MpCbQosREDCfgPktDropProb_Type.__name__=_D
_MpCbQosREDCfgPktDropProb_Object=MibTableColumn
mpCbQosREDCfgPktDropProb=_MpCbQosREDCfgPktDropProb_Object((1,3,6,1,4,1,5651,6,2,3,4,1,11,1,1,2),_MpCbQosREDCfgPktDropProb_Type())
mpCbQosREDCfgPktDropProb.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosREDCfgPktDropProb.setStatus(_A)
class _MpCbQosREDClassCfgMinThresholdUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5)))
_MpCbQosREDClassCfgMinThresholdUnit_Type.__name__=_D
_MpCbQosREDClassCfgMinThresholdUnit_Object=MibTableColumn
mpCbQosREDClassCfgMinThresholdUnit=_MpCbQosREDClassCfgMinThresholdUnit_Object((1,3,6,1,4,1,5651,6,2,3,4,1,11,1,1,3),_MpCbQosREDClassCfgMinThresholdUnit_Type())
mpCbQosREDClassCfgMinThresholdUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosREDClassCfgMinThresholdUnit.setStatus(_A)
class _MpCbQosREDClassCfgMaxThresholdUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5)))
_MpCbQosREDClassCfgMaxThresholdUnit_Type.__name__=_D
_MpCbQosREDClassCfgMaxThresholdUnit_Object=MibTableColumn
mpCbQosREDClassCfgMaxThresholdUnit=_MpCbQosREDClassCfgMaxThresholdUnit_Object((1,3,6,1,4,1,5651,6,2,3,4,1,11,1,1,4),_MpCbQosREDClassCfgMaxThresholdUnit_Type())
mpCbQosREDClassCfgMaxThresholdUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosREDClassCfgMaxThresholdUnit.setStatus(_A)
_MpCbQosREDClassCfgMinThreshold_Type=Unsigned32
_MpCbQosREDClassCfgMinThreshold_Object=MibTableColumn
mpCbQosREDClassCfgMinThreshold=_MpCbQosREDClassCfgMinThreshold_Object((1,3,6,1,4,1,5651,6,2,3,4,1,11,1,1,5),_MpCbQosREDClassCfgMinThreshold_Type())
mpCbQosREDClassCfgMinThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosREDClassCfgMinThreshold.setStatus(_A)
_MpCbQosREDClassCfgMaxThreshold_Type=Unsigned32
_MpCbQosREDClassCfgMaxThreshold_Object=MibTableColumn
mpCbQosREDClassCfgMaxThreshold=_MpCbQosREDClassCfgMaxThreshold_Object((1,3,6,1,4,1,5651,6,2,3,4,1,11,1,1,6),_MpCbQosREDClassCfgMaxThreshold_Type())
mpCbQosREDClassCfgMaxThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosREDClassCfgMaxThreshold.setStatus(_A)
_MpCbQosREDClassCfgMinThresholdTime_Type=Unsigned32
_MpCbQosREDClassCfgMinThresholdTime_Object=MibTableColumn
mpCbQosREDClassCfgMinThresholdTime=_MpCbQosREDClassCfgMinThresholdTime_Object((1,3,6,1,4,1,5651,6,2,3,4,1,11,1,1,7),_MpCbQosREDClassCfgMinThresholdTime_Type())
mpCbQosREDClassCfgMinThresholdTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosREDClassCfgMinThresholdTime.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosREDClassCfgMinThresholdTime.setUnits(_K)
_MpCbQosREDClassCfgMaxThresholdTime_Type=Unsigned32
_MpCbQosREDClassCfgMaxThresholdTime_Object=MibTableColumn
mpCbQosREDClassCfgMaxThresholdTime=_MpCbQosREDClassCfgMaxThresholdTime_Object((1,3,6,1,4,1,5651,6,2,3,4,1,11,1,1,8),_MpCbQosREDClassCfgMaxThresholdTime_Type())
mpCbQosREDClassCfgMaxThresholdTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosREDClassCfgMaxThresholdTime.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosREDClassCfgMaxThresholdTime.setUnits(_K)
_MpCbQosPoliceCfg_ObjectIdentity=ObjectIdentity
mpCbQosPoliceCfg=_MpCbQosPoliceCfg_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,4,1,12))
_MpCbQosPoliceCfgTable_Object=MibTable
mpCbQosPoliceCfgTable=_MpCbQosPoliceCfgTable_Object((1,3,6,1,4,1,5651,6,2,3,4,1,12,1))
if mibBuilder.loadTexts:mpCbQosPoliceCfgTable.setStatus(_A)
_MpCbQosPoliceCfgEntry_Object=MibTableRow
mpCbQosPoliceCfgEntry=_MpCbQosPoliceCfgEntry_Object((1,3,6,1,4,1,5651,6,2,3,4,1,12,1,1))
mpCbQosPoliceCfgEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:mpCbQosPoliceCfgEntry.setStatus(_A)
_MpCbQosPoliceCfgRate64_Type=Unsigned64
_MpCbQosPoliceCfgRate64_Object=MibTableColumn
mpCbQosPoliceCfgRate64=_MpCbQosPoliceCfgRate64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,12,1,1,1),_MpCbQosPoliceCfgRate64_Type())
mpCbQosPoliceCfgRate64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceCfgRate64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosPoliceCfgRate64.setUnits(_U)
_MpCbQosPoliceCfgBurstSize_Type=Unsigned32
_MpCbQosPoliceCfgBurstSize_Object=MibTableColumn
mpCbQosPoliceCfgBurstSize=_MpCbQosPoliceCfgBurstSize_Object((1,3,6,1,4,1,5651,6,2,3,4,1,12,1,1,2),_MpCbQosPoliceCfgBurstSize_Type())
mpCbQosPoliceCfgBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceCfgBurstSize.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosPoliceCfgBurstSize.setUnits(_F)
_MpCbQosPoliceCfgExtBurstSize_Type=Unsigned32
_MpCbQosPoliceCfgExtBurstSize_Object=MibTableColumn
mpCbQosPoliceCfgExtBurstSize=_MpCbQosPoliceCfgExtBurstSize_Object((1,3,6,1,4,1,5651,6,2,3,4,1,12,1,1,3),_MpCbQosPoliceCfgExtBurstSize_Type())
mpCbQosPoliceCfgExtBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceCfgExtBurstSize.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosPoliceCfgExtBurstSize.setUnits(_F)
_MpCbQosPoliceCfgPir64_Type=Unsigned64
_MpCbQosPoliceCfgPir64_Object=MibTableColumn
mpCbQosPoliceCfgPir64=_MpCbQosPoliceCfgPir64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,12,1,1,4),_MpCbQosPoliceCfgPir64_Type())
mpCbQosPoliceCfgPir64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceCfgPir64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosPoliceCfgPir64.setUnits(_U)
class _MpCbQosPoliceCfgRateType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('bps',1),(_W,2),('cps',3)))
_MpCbQosPoliceCfgRateType_Type.__name__=_D
_MpCbQosPoliceCfgRateType_Object=MibTableColumn
mpCbQosPoliceCfgRateType=_MpCbQosPoliceCfgRateType_Object((1,3,6,1,4,1,5651,6,2,3,4,1,12,1,1,5),_MpCbQosPoliceCfgRateType_Type())
mpCbQosPoliceCfgRateType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceCfgRateType.setStatus(_A)
class _MpCbQosPoliceCfgPercentRateValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_MpCbQosPoliceCfgPercentRateValue_Type.__name__=_G
_MpCbQosPoliceCfgPercentRateValue_Object=MibTableColumn
mpCbQosPoliceCfgPercentRateValue=_MpCbQosPoliceCfgPercentRateValue_Object((1,3,6,1,4,1,5651,6,2,3,4,1,12,1,1,6),_MpCbQosPoliceCfgPercentRateValue_Type())
mpCbQosPoliceCfgPercentRateValue.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceCfgPercentRateValue.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosPoliceCfgPercentRateValue.setUnits(_Y)
class _MpCbQosPoliceCfgPercentPirValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_MpCbQosPoliceCfgPercentPirValue_Type.__name__=_G
_MpCbQosPoliceCfgPercentPirValue_Object=MibTableColumn
mpCbQosPoliceCfgPercentPirValue=_MpCbQosPoliceCfgPercentPirValue_Object((1,3,6,1,4,1,5651,6,2,3,4,1,12,1,1,7),_MpCbQosPoliceCfgPercentPirValue_Type())
mpCbQosPoliceCfgPercentPirValue.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceCfgPercentPirValue.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosPoliceCfgPercentPirValue.setUnits(_Y)
_MpCbQosPoliceCfgCellRate_Type=Unsigned32
_MpCbQosPoliceCfgCellRate_Object=MibTableColumn
mpCbQosPoliceCfgCellRate=_MpCbQosPoliceCfgCellRate_Object((1,3,6,1,4,1,5651,6,2,3,4,1,12,1,1,8),_MpCbQosPoliceCfgCellRate_Type())
mpCbQosPoliceCfgCellRate.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceCfgCellRate.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosPoliceCfgCellRate.setUnits(_s)
_MpCbQosPoliceCfgCellPir_Type=Unsigned32
_MpCbQosPoliceCfgCellPir_Object=MibTableColumn
mpCbQosPoliceCfgCellPir=_MpCbQosPoliceCfgCellPir_Object((1,3,6,1,4,1,5651,6,2,3,4,1,12,1,1,9),_MpCbQosPoliceCfgCellPir_Type())
mpCbQosPoliceCfgCellPir.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceCfgCellPir.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosPoliceCfgCellPir.setUnits(_s)
_MpCbQosPoliceCfgBurstCell_Type=Unsigned32
_MpCbQosPoliceCfgBurstCell_Object=MibTableColumn
mpCbQosPoliceCfgBurstCell=_MpCbQosPoliceCfgBurstCell_Object((1,3,6,1,4,1,5651,6,2,3,4,1,12,1,1,10),_MpCbQosPoliceCfgBurstCell_Type())
mpCbQosPoliceCfgBurstCell.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceCfgBurstCell.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosPoliceCfgBurstCell.setUnits('Cells')
_MpCbQosPoliceCfgExtBurstCell_Type=Unsigned32
_MpCbQosPoliceCfgExtBurstCell_Object=MibTableColumn
mpCbQosPoliceCfgExtBurstCell=_MpCbQosPoliceCfgExtBurstCell_Object((1,3,6,1,4,1,5651,6,2,3,4,1,12,1,1,11),_MpCbQosPoliceCfgExtBurstCell_Type())
mpCbQosPoliceCfgExtBurstCell.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceCfgExtBurstCell.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosPoliceCfgExtBurstCell.setUnits('Cells')
_MpCbQosPoliceCfgBurstTime_Type=Unsigned32
_MpCbQosPoliceCfgBurstTime_Object=MibTableColumn
mpCbQosPoliceCfgBurstTime=_MpCbQosPoliceCfgBurstTime_Object((1,3,6,1,4,1,5651,6,2,3,4,1,12,1,1,12),_MpCbQosPoliceCfgBurstTime_Type())
mpCbQosPoliceCfgBurstTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceCfgBurstTime.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosPoliceCfgBurstTime.setUnits(_K)
_MpCbQosPoliceCfgExtBurstTime_Type=Unsigned32
_MpCbQosPoliceCfgExtBurstTime_Object=MibTableColumn
mpCbQosPoliceCfgExtBurstTime=_MpCbQosPoliceCfgExtBurstTime_Object((1,3,6,1,4,1,5651,6,2,3,4,1,12,1,1,13),_MpCbQosPoliceCfgExtBurstTime_Type())
mpCbQosPoliceCfgExtBurstTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceCfgExtBurstTime.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosPoliceCfgExtBurstTime.setUnits(_K)
_MpCbQosPoliceActionCfg_ObjectIdentity=ObjectIdentity
mpCbQosPoliceActionCfg=_MpCbQosPoliceActionCfg_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,4,1,13))
_MpCbQosPoliceActionCfgTable_Object=MibTable
mpCbQosPoliceActionCfgTable=_MpCbQosPoliceActionCfgTable_Object((1,3,6,1,4,1,5651,6,2,3,4,1,13,1))
if mibBuilder.loadTexts:mpCbQosPoliceActionCfgTable.setStatus(_A)
_MpCbQosPoliceActionCfgEntry_Object=MibTableRow
mpCbQosPoliceActionCfgEntry=_MpCbQosPoliceActionCfgEntry_Object((1,3,6,1,4,1,5651,6,2,3,4,1,13,1,1))
mpCbQosPoliceActionCfgEntry.setIndexNames((0,_C,_H),(0,_C,_t))
if mibBuilder.loadTexts:mpCbQosPoliceActionCfgEntry.setStatus(_A)
_MpCbQosPoliceActionCfgIndex_Type=Unsigned32
_MpCbQosPoliceActionCfgIndex_Object=MibTableColumn
mpCbQosPoliceActionCfgIndex=_MpCbQosPoliceActionCfgIndex_Object((1,3,6,1,4,1,5651,6,2,3,4,1,13,1,1,1),_MpCbQosPoliceActionCfgIndex_Type())
mpCbQosPoliceActionCfgIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:mpCbQosPoliceActionCfgIndex.setStatus(_A)
class _MpCbQosPoliceActionCfgConform_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_Z,1),(_a,2),(_b,3),(_c,4),(_d,5),(_e,6),(_f,7),(_g,8),(_h,9),(_i,10),(_j,11),(_k,12),(_l,13),(_m,14)))
_MpCbQosPoliceActionCfgConform_Type.__name__=_D
_MpCbQosPoliceActionCfgConform_Object=MibTableColumn
mpCbQosPoliceActionCfgConform=_MpCbQosPoliceActionCfgConform_Object((1,3,6,1,4,1,5651,6,2,3,4,1,13,1,1,2),_MpCbQosPoliceActionCfgConform_Type())
mpCbQosPoliceActionCfgConform.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceActionCfgConform.setStatus(_A)
_MpCbQosPoliceActionCfgConformSetValue_Type=Unsigned32
_MpCbQosPoliceActionCfgConformSetValue_Object=MibTableColumn
mpCbQosPoliceActionCfgConformSetValue=_MpCbQosPoliceActionCfgConformSetValue_Object((1,3,6,1,4,1,5651,6,2,3,4,1,13,1,1,3),_MpCbQosPoliceActionCfgConformSetValue_Type())
mpCbQosPoliceActionCfgConformSetValue.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceActionCfgConformSetValue.setStatus(_A)
class _MpCbQosPoliceActionCfgExceed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_Z,1),(_a,2),(_b,3),(_c,4),(_d,5),(_e,6),(_f,7),(_g,8),(_h,9),(_i,10),(_j,11),(_k,12),(_l,13),(_m,14)))
_MpCbQosPoliceActionCfgExceed_Type.__name__=_D
_MpCbQosPoliceActionCfgExceed_Object=MibTableColumn
mpCbQosPoliceActionCfgExceed=_MpCbQosPoliceActionCfgExceed_Object((1,3,6,1,4,1,5651,6,2,3,4,1,13,1,1,4),_MpCbQosPoliceActionCfgExceed_Type())
mpCbQosPoliceActionCfgExceed.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceActionCfgExceed.setStatus(_A)
_MpCbQosPoliceActionCfgExceedSetValue_Type=Unsigned32
_MpCbQosPoliceActionCfgExceedSetValue_Object=MibTableColumn
mpCbQosPoliceActionCfgExceedSetValue=_MpCbQosPoliceActionCfgExceedSetValue_Object((1,3,6,1,4,1,5651,6,2,3,4,1,13,1,1,5),_MpCbQosPoliceActionCfgExceedSetValue_Type())
mpCbQosPoliceActionCfgExceedSetValue.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceActionCfgExceedSetValue.setStatus(_A)
class _MpCbQosPoliceActionCfgViolate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_Z,1),(_a,2),(_b,3),(_c,4),(_d,5),(_e,6),(_f,7),(_g,8),(_h,9),(_i,10),(_j,11),(_k,12),(_l,13),(_m,14)))
_MpCbQosPoliceActionCfgViolate_Type.__name__=_D
_MpCbQosPoliceActionCfgViolate_Object=MibTableColumn
mpCbQosPoliceActionCfgViolate=_MpCbQosPoliceActionCfgViolate_Object((1,3,6,1,4,1,5651,6,2,3,4,1,13,1,1,6),_MpCbQosPoliceActionCfgViolate_Type())
mpCbQosPoliceActionCfgViolate.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceActionCfgViolate.setStatus(_A)
_MpCbQosPoliceActionCfgViolateSetValue_Type=Unsigned32
_MpCbQosPoliceActionCfgViolateSetValue_Object=MibTableColumn
mpCbQosPoliceActionCfgViolateSetValue=_MpCbQosPoliceActionCfgViolateSetValue_Object((1,3,6,1,4,1,5651,6,2,3,4,1,13,1,1,7),_MpCbQosPoliceActionCfgViolateSetValue_Type())
mpCbQosPoliceActionCfgViolateSetValue.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceActionCfgViolateSetValue.setStatus(_A)
_MpCbQosTSCfg_ObjectIdentity=ObjectIdentity
mpCbQosTSCfg=_MpCbQosTSCfg_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,4,1,14))
_MpCbQosTSCfgTable_Object=MibTable
mpCbQosTSCfgTable=_MpCbQosTSCfgTable_Object((1,3,6,1,4,1,5651,6,2,3,4,1,14,1))
if mibBuilder.loadTexts:mpCbQosTSCfgTable.setStatus(_A)
_MpCbQosTSCfgEntry_Object=MibTableRow
mpCbQosTSCfgEntry=_MpCbQosTSCfgEntry_Object((1,3,6,1,4,1,5651,6,2,3,4,1,14,1,1))
mpCbQosTSCfgEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:mpCbQosTSCfgEntry.setStatus(_A)
_MpCbQosTSCfgRate64_Type=Unsigned64
_MpCbQosTSCfgRate64_Object=MibTableColumn
mpCbQosTSCfgRate64=_MpCbQosTSCfgRate64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,14,1,1,1),_MpCbQosTSCfgRate64_Type())
mpCbQosTSCfgRate64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosTSCfgRate64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosTSCfgRate64.setUnits(_U)
_MpCbQosTSCfgBurstSize_Type=Integer32
_MpCbQosTSCfgBurstSize_Object=MibTableColumn
mpCbQosTSCfgBurstSize=_MpCbQosTSCfgBurstSize_Object((1,3,6,1,4,1,5651,6,2,3,4,1,14,1,1,2),_MpCbQosTSCfgBurstSize_Type())
mpCbQosTSCfgBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosTSCfgBurstSize.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosTSCfgBurstSize.setUnits('bits')
_MpCbQosTSCfgExtBurstSize_Type=Integer32
_MpCbQosTSCfgExtBurstSize_Object=MibTableColumn
mpCbQosTSCfgExtBurstSize=_MpCbQosTSCfgExtBurstSize_Object((1,3,6,1,4,1,5651,6,2,3,4,1,14,1,1,3),_MpCbQosTSCfgExtBurstSize_Type())
mpCbQosTSCfgExtBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosTSCfgExtBurstSize.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosTSCfgExtBurstSize.setUnits('bits')
_MpCbQosTSCfgAdaptiveEnabled_Type=TruthValue
_MpCbQosTSCfgAdaptiveEnabled_Object=MibTableColumn
mpCbQosTSCfgAdaptiveEnabled=_MpCbQosTSCfgAdaptiveEnabled_Object((1,3,6,1,4,1,5651,6,2,3,4,1,14,1,1,4),_MpCbQosTSCfgAdaptiveEnabled_Type())
mpCbQosTSCfgAdaptiveEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosTSCfgAdaptiveEnabled.setStatus(_A)
_MpCbQosTSCfgAdaptiveRate64_Type=Unsigned64
_MpCbQosTSCfgAdaptiveRate64_Object=MibTableColumn
mpCbQosTSCfgAdaptiveRate64=_MpCbQosTSCfgAdaptiveRate64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,14,1,1,5),_MpCbQosTSCfgAdaptiveRate64_Type())
mpCbQosTSCfgAdaptiveRate64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosTSCfgAdaptiveRate64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosTSCfgAdaptiveRate64.setUnits(_U)
class _MpCbQosTSCfgLimitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('average',1),('peak',2)))
_MpCbQosTSCfgLimitType_Type.__name__=_D
_MpCbQosTSCfgLimitType_Object=MibTableColumn
mpCbQosTSCfgLimitType=_MpCbQosTSCfgLimitType_Object((1,3,6,1,4,1,5651,6,2,3,4,1,14,1,1,6),_MpCbQosTSCfgLimitType_Type())
mpCbQosTSCfgLimitType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosTSCfgLimitType.setStatus(_A)
class _MpCbQosTSCfgRateType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('bps',1),(_W,2),('cps',3)))
_MpCbQosTSCfgRateType_Type.__name__=_D
_MpCbQosTSCfgRateType_Object=MibTableColumn
mpCbQosTSCfgRateType=_MpCbQosTSCfgRateType_Object((1,3,6,1,4,1,5651,6,2,3,4,1,14,1,1,7),_MpCbQosTSCfgRateType_Type())
mpCbQosTSCfgRateType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosTSCfgRateType.setStatus(_A)
class _MpCbQosTSCfgPercentRateValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_MpCbQosTSCfgPercentRateValue_Type.__name__=_G
_MpCbQosTSCfgPercentRateValue_Object=MibTableColumn
mpCbQosTSCfgPercentRateValue=_MpCbQosTSCfgPercentRateValue_Object((1,3,6,1,4,1,5651,6,2,3,4,1,14,1,1,8),_MpCbQosTSCfgPercentRateValue_Type())
mpCbQosTSCfgPercentRateValue.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosTSCfgPercentRateValue.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosTSCfgPercentRateValue.setUnits(_Y)
_MpCbQosTSCfgBurstTime_Type=Unsigned32
_MpCbQosTSCfgBurstTime_Object=MibTableColumn
mpCbQosTSCfgBurstTime=_MpCbQosTSCfgBurstTime_Object((1,3,6,1,4,1,5651,6,2,3,4,1,14,1,1,9),_MpCbQosTSCfgBurstTime_Type())
mpCbQosTSCfgBurstTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosTSCfgBurstTime.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosTSCfgBurstTime.setUnits(_K)
_MpCbQosTSCfgExtBurstTime_Type=Unsigned32
_MpCbQosTSCfgExtBurstTime_Object=MibTableColumn
mpCbQosTSCfgExtBurstTime=_MpCbQosTSCfgExtBurstTime_Object((1,3,6,1,4,1,5651,6,2,3,4,1,14,1,1,10),_MpCbQosTSCfgExtBurstTime_Type())
mpCbQosTSCfgExtBurstTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosTSCfgExtBurstTime.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosTSCfgExtBurstTime.setUnits(_K)
_MpCbQosSetCfg_ObjectIdentity=ObjectIdentity
mpCbQosSetCfg=_MpCbQosSetCfg_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,4,1,15))
_MpCbQosSetCfgTable_Object=MibTable
mpCbQosSetCfgTable=_MpCbQosSetCfgTable_Object((1,3,6,1,4,1,5651,6,2,3,4,1,15,1))
if mibBuilder.loadTexts:mpCbQosSetCfgTable.setStatus(_A)
_MpCbQosSetCfgEntry_Object=MibTableRow
mpCbQosSetCfgEntry=_MpCbQosSetCfgEntry_Object((1,3,6,1,4,1,5651,6,2,3,4,1,15,1,1))
mpCbQosSetCfgEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:mpCbQosSetCfgEntry.setStatus(_A)
class _MpCbQosSetCfgFeature_Type(Bits):namedValues=NamedValues(*(('ipDscp',0),('ipPrecedence',1),('qosGroupNumber',2),('frDeBit',3),('atmClpBit',4),('l2Cos',5),(_r,6),(_q,7),('mplsExpTopMost',8),('frFecnBecn',9),('ipDscpTunnel',10),('ipPrecedenceTunnel',11),('l2CosInner',12),('ipTos',13)))
_MpCbQosSetCfgFeature_Type.__name__='Bits'
_MpCbQosSetCfgFeature_Object=MibTableColumn
mpCbQosSetCfgFeature=_MpCbQosSetCfgFeature_Object((1,3,6,1,4,1,5651,6,2,3,4,1,15,1,1,1),_MpCbQosSetCfgFeature_Type())
mpCbQosSetCfgFeature.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetCfgFeature.setStatus(_A)
class _MpCbQosSetCfgIpDSCPValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_MpCbQosSetCfgIpDSCPValue_Type.__name__=_D
_MpCbQosSetCfgIpDSCPValue_Object=MibTableColumn
mpCbQosSetCfgIpDSCPValue=_MpCbQosSetCfgIpDSCPValue_Object((1,3,6,1,4,1,5651,6,2,3,4,1,15,1,1,2),_MpCbQosSetCfgIpDSCPValue_Type())
mpCbQosSetCfgIpDSCPValue.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetCfgIpDSCPValue.setStatus(_A)
class _MpCbQosSetCfgIpPrecedenceValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_MpCbQosSetCfgIpPrecedenceValue_Type.__name__=_D
_MpCbQosSetCfgIpPrecedenceValue_Object=MibTableColumn
mpCbQosSetCfgIpPrecedenceValue=_MpCbQosSetCfgIpPrecedenceValue_Object((1,3,6,1,4,1,5651,6,2,3,4,1,15,1,1,3),_MpCbQosSetCfgIpPrecedenceValue_Type())
mpCbQosSetCfgIpPrecedenceValue.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetCfgIpPrecedenceValue.setStatus(_A)
_MpCbQosSetCfgQosGroupValue_Type=Integer32
_MpCbQosSetCfgQosGroupValue_Object=MibTableColumn
mpCbQosSetCfgQosGroupValue=_MpCbQosSetCfgQosGroupValue_Object((1,3,6,1,4,1,5651,6,2,3,4,1,15,1,1,4),_MpCbQosSetCfgQosGroupValue_Type())
mpCbQosSetCfgQosGroupValue.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetCfgQosGroupValue.setStatus(_A)
class _MpCbQosSetCfgL2CosValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_MpCbQosSetCfgL2CosValue_Type.__name__=_D
_MpCbQosSetCfgL2CosValue_Object=MibTableColumn
mpCbQosSetCfgL2CosValue=_MpCbQosSetCfgL2CosValue_Object((1,3,6,1,4,1,5651,6,2,3,4,1,15,1,1,5),_MpCbQosSetCfgL2CosValue_Type())
mpCbQosSetCfgL2CosValue.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetCfgL2CosValue.setStatus(_A)
class _MpCbQosSetCfgMplsExpValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_MpCbQosSetCfgMplsExpValue_Type.__name__=_G
_MpCbQosSetCfgMplsExpValue_Object=MibTableColumn
mpCbQosSetCfgMplsExpValue=_MpCbQosSetCfgMplsExpValue_Object((1,3,6,1,4,1,5651,6,2,3,4,1,15,1,1,6),_MpCbQosSetCfgMplsExpValue_Type())
mpCbQosSetCfgMplsExpValue.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetCfgMplsExpValue.setStatus(_A)
class _MpCbQosSetCfgDiscardClassValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_MpCbQosSetCfgDiscardClassValue_Type.__name__=_G
_MpCbQosSetCfgDiscardClassValue_Object=MibTableColumn
mpCbQosSetCfgDiscardClassValue=_MpCbQosSetCfgDiscardClassValue_Object((1,3,6,1,4,1,5651,6,2,3,4,1,15,1,1,7),_MpCbQosSetCfgDiscardClassValue_Type())
mpCbQosSetCfgDiscardClassValue.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetCfgDiscardClassValue.setStatus(_A)
class _MpCbQosSetCfgMplsExpTopMostValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_MpCbQosSetCfgMplsExpTopMostValue_Type.__name__=_G
_MpCbQosSetCfgMplsExpTopMostValue_Object=MibTableColumn
mpCbQosSetCfgMplsExpTopMostValue=_MpCbQosSetCfgMplsExpTopMostValue_Object((1,3,6,1,4,1,5651,6,2,3,4,1,15,1,1,8),_MpCbQosSetCfgMplsExpTopMostValue_Type())
mpCbQosSetCfgMplsExpTopMostValue.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetCfgMplsExpTopMostValue.setStatus(_A)
_MpCbQosSetCfgFrFecnBecn_Type=Unsigned32
_MpCbQosSetCfgFrFecnBecn_Object=MibTableColumn
mpCbQosSetCfgFrFecnBecn=_MpCbQosSetCfgFrFecnBecn_Object((1,3,6,1,4,1,5651,6,2,3,4,1,15,1,1,9),_MpCbQosSetCfgFrFecnBecn_Type())
mpCbQosSetCfgFrFecnBecn.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetCfgFrFecnBecn.setStatus(_A)
class _MpCbQosSetCfgIpDSCPTunnelValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_MpCbQosSetCfgIpDSCPTunnelValue_Type.__name__=_D
_MpCbQosSetCfgIpDSCPTunnelValue_Object=MibTableColumn
mpCbQosSetCfgIpDSCPTunnelValue=_MpCbQosSetCfgIpDSCPTunnelValue_Object((1,3,6,1,4,1,5651,6,2,3,4,1,15,1,1,10),_MpCbQosSetCfgIpDSCPTunnelValue_Type())
mpCbQosSetCfgIpDSCPTunnelValue.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetCfgIpDSCPTunnelValue.setStatus(_A)
class _MpCbQosSetCfgIpPrecedenceTunnelValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_MpCbQosSetCfgIpPrecedenceTunnelValue_Type.__name__=_D
_MpCbQosSetCfgIpPrecedenceTunnelValue_Object=MibTableColumn
mpCbQosSetCfgIpPrecedenceTunnelValue=_MpCbQosSetCfgIpPrecedenceTunnelValue_Object((1,3,6,1,4,1,5651,6,2,3,4,1,15,1,1,11),_MpCbQosSetCfgIpPrecedenceTunnelValue_Type())
mpCbQosSetCfgIpPrecedenceTunnelValue.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetCfgIpPrecedenceTunnelValue.setStatus(_A)
class _MpCbQosSetCfgL2CosInnerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_MpCbQosSetCfgL2CosInnerValue_Type.__name__=_D
_MpCbQosSetCfgL2CosInnerValue_Object=MibTableColumn
mpCbQosSetCfgL2CosInnerValue=_MpCbQosSetCfgL2CosInnerValue_Object((1,3,6,1,4,1,5651,6,2,3,4,1,15,1,1,12),_MpCbQosSetCfgL2CosInnerValue_Type())
mpCbQosSetCfgL2CosInnerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetCfgL2CosInnerValue.setStatus(_A)
class _MpCbQosSetCfgIpTosValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MpCbQosSetCfgIpTosValue_Type.__name__=_D
_MpCbQosSetCfgIpTosValue_Object=MibTableColumn
mpCbQosSetCfgIpTosValue=_MpCbQosSetCfgIpTosValue_Object((1,3,6,1,4,1,5651,6,2,3,4,1,15,1,1,13),_MpCbQosSetCfgIpTosValue_Type())
mpCbQosSetCfgIpTosValue.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetCfgIpTosValue.setStatus(_A)
_MpCbQosClassMapStats_ObjectIdentity=ObjectIdentity
mpCbQosClassMapStats=_MpCbQosClassMapStats_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,4,1,16))
_MpCbQosCMStatsTable_Object=MibTable
mpCbQosCMStatsTable=_MpCbQosCMStatsTable_Object((1,3,6,1,4,1,5651,6,2,3,4,1,16,1))
if mibBuilder.loadTexts:mpCbQosCMStatsTable.setStatus(_A)
_MpCbQosCMStatsEntry_Object=MibTableRow
mpCbQosCMStatsEntry=_MpCbQosCMStatsEntry_Object((1,3,6,1,4,1,5651,6,2,3,4,1,16,1,1))
mpCbQosCMStatsEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:mpCbQosCMStatsEntry.setStatus(_A)
_MpCbQosCMPrePolicyPkt64_Type=Counter64
_MpCbQosCMPrePolicyPkt64_Object=MibTableColumn
mpCbQosCMPrePolicyPkt64=_MpCbQosCMPrePolicyPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,16,1,1,1),_MpCbQosCMPrePolicyPkt64_Type())
mpCbQosCMPrePolicyPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosCMPrePolicyPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosCMPrePolicyPkt64.setUnits(_E)
_MpCbQosCMPrePolicyByte64_Type=Counter64
_MpCbQosCMPrePolicyByte64_Object=MibTableColumn
mpCbQosCMPrePolicyByte64=_MpCbQosCMPrePolicyByte64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,16,1,1,2),_MpCbQosCMPrePolicyByte64_Type())
mpCbQosCMPrePolicyByte64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosCMPrePolicyByte64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosCMPrePolicyByte64.setUnits(_F)
_MpCbQosCMPrePolicyBitRate64_Type=Unsigned64
_MpCbQosCMPrePolicyBitRate64_Object=MibTableColumn
mpCbQosCMPrePolicyBitRate64=_MpCbQosCMPrePolicyBitRate64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,16,1,1,3),_MpCbQosCMPrePolicyBitRate64_Type())
mpCbQosCMPrePolicyBitRate64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosCMPrePolicyBitRate64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosCMPrePolicyBitRate64.setUnits(_L)
_MpCbQosCMPostPolicyPkt64_Type=Counter64
_MpCbQosCMPostPolicyPkt64_Object=MibTableColumn
mpCbQosCMPostPolicyPkt64=_MpCbQosCMPostPolicyPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,16,1,1,4),_MpCbQosCMPostPolicyPkt64_Type())
mpCbQosCMPostPolicyPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosCMPostPolicyPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosCMPostPolicyPkt64.setUnits(_E)
_MpCbQosCMPostPolicyByte64_Type=Counter64
_MpCbQosCMPostPolicyByte64_Object=MibTableColumn
mpCbQosCMPostPolicyByte64=_MpCbQosCMPostPolicyByte64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,16,1,1,5),_MpCbQosCMPostPolicyByte64_Type())
mpCbQosCMPostPolicyByte64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosCMPostPolicyByte64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosCMPostPolicyByte64.setUnits(_F)
_MpCbQosCMPostPolicyBitRate64_Type=Unsigned64
_MpCbQosCMPostPolicyBitRate64_Object=MibTableColumn
mpCbQosCMPostPolicyBitRate64=_MpCbQosCMPostPolicyBitRate64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,16,1,1,6),_MpCbQosCMPostPolicyBitRate64_Type())
mpCbQosCMPostPolicyBitRate64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosCMPostPolicyBitRate64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosCMPostPolicyBitRate64.setUnits(_L)
_MpCbQosCMDropPkt64_Type=Counter64
_MpCbQosCMDropPkt64_Object=MibTableColumn
mpCbQosCMDropPkt64=_MpCbQosCMDropPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,16,1,1,7),_MpCbQosCMDropPkt64_Type())
mpCbQosCMDropPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosCMDropPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosCMDropPkt64.setUnits(_E)
_MpCbQosCMDropByte64_Type=Counter64
_MpCbQosCMDropByte64_Object=MibTableColumn
mpCbQosCMDropByte64=_MpCbQosCMDropByte64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,16,1,1,8),_MpCbQosCMDropByte64_Type())
mpCbQosCMDropByte64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosCMDropByte64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosCMDropByte64.setUnits(_F)
_MpCbQosCMDropBitRate64_Type=Unsigned64
_MpCbQosCMDropBitRate64_Object=MibTableColumn
mpCbQosCMDropBitRate64=_MpCbQosCMDropBitRate64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,16,1,1,9),_MpCbQosCMDropBitRate64_Type())
mpCbQosCMDropBitRate64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosCMDropBitRate64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosCMDropBitRate64.setUnits(_L)
_MpCbQosCMNoBufDropPkt64_Type=Counter64
_MpCbQosCMNoBufDropPkt64_Object=MibTableColumn
mpCbQosCMNoBufDropPkt64=_MpCbQosCMNoBufDropPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,16,1,1,10),_MpCbQosCMNoBufDropPkt64_Type())
mpCbQosCMNoBufDropPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosCMNoBufDropPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosCMNoBufDropPkt64.setUnits(_E)
_MpCbQosMatchStmtStats_ObjectIdentity=ObjectIdentity
mpCbQosMatchStmtStats=_MpCbQosMatchStmtStats_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,4,1,17))
_MpCbQosMatchStmtStatsTable_Object=MibTable
mpCbQosMatchStmtStatsTable=_MpCbQosMatchStmtStatsTable_Object((1,3,6,1,4,1,5651,6,2,3,4,1,17,1))
if mibBuilder.loadTexts:mpCbQosMatchStmtStatsTable.setStatus(_A)
_MpCbQosMatchStmtStatsEntry_Object=MibTableRow
mpCbQosMatchStmtStatsEntry=_MpCbQosMatchStmtStatsEntry_Object((1,3,6,1,4,1,5651,6,2,3,4,1,17,1,1))
mpCbQosMatchStmtStatsEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:mpCbQosMatchStmtStatsEntry.setStatus(_A)
_MpCbQosMatchPrePolicyPkt64_Type=Counter64
_MpCbQosMatchPrePolicyPkt64_Object=MibTableColumn
mpCbQosMatchPrePolicyPkt64=_MpCbQosMatchPrePolicyPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,17,1,1,1),_MpCbQosMatchPrePolicyPkt64_Type())
mpCbQosMatchPrePolicyPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosMatchPrePolicyPkt64.setStatus(_A)
_MpCbQosMatchPrePolicyByte64_Type=Counter64
_MpCbQosMatchPrePolicyByte64_Object=MibTableColumn
mpCbQosMatchPrePolicyByte64=_MpCbQosMatchPrePolicyByte64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,17,1,1,2),_MpCbQosMatchPrePolicyByte64_Type())
mpCbQosMatchPrePolicyByte64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosMatchPrePolicyByte64.setStatus(_A)
_MpCbQosMatchPrePolicyBitRate64_Type=Unsigned64
_MpCbQosMatchPrePolicyBitRate64_Object=MibTableColumn
mpCbQosMatchPrePolicyBitRate64=_MpCbQosMatchPrePolicyBitRate64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,17,1,1,3),_MpCbQosMatchPrePolicyBitRate64_Type())
mpCbQosMatchPrePolicyBitRate64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosMatchPrePolicyBitRate64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosMatchPrePolicyBitRate64.setUnits(_L)
_MpCbQosPoliceStats_ObjectIdentity=ObjectIdentity
mpCbQosPoliceStats=_MpCbQosPoliceStats_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,4,1,18))
_MpCbQosPoliceStatsTable_Object=MibTable
mpCbQosPoliceStatsTable=_MpCbQosPoliceStatsTable_Object((1,3,6,1,4,1,5651,6,2,3,4,1,18,1))
if mibBuilder.loadTexts:mpCbQosPoliceStatsTable.setStatus(_A)
_MpCbQosPoliceStatsEntry_Object=MibTableRow
mpCbQosPoliceStatsEntry=_MpCbQosPoliceStatsEntry_Object((1,3,6,1,4,1,5651,6,2,3,4,1,18,1,1))
mpCbQosPoliceStatsEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:mpCbQosPoliceStatsEntry.setStatus(_A)
_MpCbQosPoliceConformedPkt64_Type=Counter64
_MpCbQosPoliceConformedPkt64_Object=MibTableColumn
mpCbQosPoliceConformedPkt64=_MpCbQosPoliceConformedPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,18,1,1,1),_MpCbQosPoliceConformedPkt64_Type())
mpCbQosPoliceConformedPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceConformedPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosPoliceConformedPkt64.setUnits(_E)
_MpCbQosPoliceConformedByte64_Type=Counter64
_MpCbQosPoliceConformedByte64_Object=MibTableColumn
mpCbQosPoliceConformedByte64=_MpCbQosPoliceConformedByte64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,18,1,1,2),_MpCbQosPoliceConformedByte64_Type())
mpCbQosPoliceConformedByte64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceConformedByte64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosPoliceConformedByte64.setUnits(_F)
_MpCbQosPoliceConformedBitRate64_Type=Unsigned64
_MpCbQosPoliceConformedBitRate64_Object=MibTableColumn
mpCbQosPoliceConformedBitRate64=_MpCbQosPoliceConformedBitRate64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,18,1,1,3),_MpCbQosPoliceConformedBitRate64_Type())
mpCbQosPoliceConformedBitRate64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceConformedBitRate64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosPoliceConformedBitRate64.setUnits(_L)
_MpCbQosPoliceExceededPkt64_Type=Counter64
_MpCbQosPoliceExceededPkt64_Object=MibTableColumn
mpCbQosPoliceExceededPkt64=_MpCbQosPoliceExceededPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,18,1,1,4),_MpCbQosPoliceExceededPkt64_Type())
mpCbQosPoliceExceededPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceExceededPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosPoliceExceededPkt64.setUnits(_E)
_MpCbQosPoliceExceededByte64_Type=Counter64
_MpCbQosPoliceExceededByte64_Object=MibTableColumn
mpCbQosPoliceExceededByte64=_MpCbQosPoliceExceededByte64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,18,1,1,5),_MpCbQosPoliceExceededByte64_Type())
mpCbQosPoliceExceededByte64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceExceededByte64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosPoliceExceededByte64.setUnits(_F)
_MpCbQosPoliceExceededBitRate64_Type=Unsigned64
_MpCbQosPoliceExceededBitRate64_Object=MibTableColumn
mpCbQosPoliceExceededBitRate64=_MpCbQosPoliceExceededBitRate64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,18,1,1,6),_MpCbQosPoliceExceededBitRate64_Type())
mpCbQosPoliceExceededBitRate64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceExceededBitRate64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosPoliceExceededBitRate64.setUnits(_L)
_MpCbQosPoliceViolatedPkt64_Type=Counter64
_MpCbQosPoliceViolatedPkt64_Object=MibTableColumn
mpCbQosPoliceViolatedPkt64=_MpCbQosPoliceViolatedPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,18,1,1,7),_MpCbQosPoliceViolatedPkt64_Type())
mpCbQosPoliceViolatedPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceViolatedPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosPoliceViolatedPkt64.setUnits(_E)
_MpCbQosPoliceViolatedByte64_Type=Counter64
_MpCbQosPoliceViolatedByte64_Object=MibTableColumn
mpCbQosPoliceViolatedByte64=_MpCbQosPoliceViolatedByte64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,18,1,1,8),_MpCbQosPoliceViolatedByte64_Type())
mpCbQosPoliceViolatedByte64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceViolatedByte64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosPoliceViolatedByte64.setUnits(_F)
_MpCbQosPoliceViolatedBitRate64_Type=Unsigned64
_MpCbQosPoliceViolatedBitRate64_Object=MibTableColumn
mpCbQosPoliceViolatedBitRate64=_MpCbQosPoliceViolatedBitRate64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,18,1,1,9),_MpCbQosPoliceViolatedBitRate64_Type())
mpCbQosPoliceViolatedBitRate64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosPoliceViolatedBitRate64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosPoliceViolatedBitRate64.setUnits(_L)
_MpCbQosQueueingStats_ObjectIdentity=ObjectIdentity
mpCbQosQueueingStats=_MpCbQosQueueingStats_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,4,1,19))
_MpCbQosQueueingStatsTable_Object=MibTable
mpCbQosQueueingStatsTable=_MpCbQosQueueingStatsTable_Object((1,3,6,1,4,1,5651,6,2,3,4,1,19,1))
if mibBuilder.loadTexts:mpCbQosQueueingStatsTable.setStatus(_A)
_MpCbQosQueueingStatsEntry_Object=MibTableRow
mpCbQosQueueingStatsEntry=_MpCbQosQueueingStatsEntry_Object((1,3,6,1,4,1,5651,6,2,3,4,1,19,1,1))
mpCbQosQueueingStatsEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:mpCbQosQueueingStatsEntry.setStatus(_A)
class _MpCbQosQueueingQDepthUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5)))
_MpCbQosQueueingQDepthUnit_Type.__name__=_D
_MpCbQosQueueingQDepthUnit_Object=MibTableColumn
mpCbQosQueueingQDepthUnit=_MpCbQosQueueingQDepthUnit_Object((1,3,6,1,4,1,5651,6,2,3,4,1,19,1,1,1),_MpCbQosQueueingQDepthUnit_Type())
mpCbQosQueueingQDepthUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosQueueingQDepthUnit.setStatus(_A)
_MpCbQosQueueingCurrentQDepth_Type=Gauge32
_MpCbQosQueueingCurrentQDepth_Object=MibTableColumn
mpCbQosQueueingCurrentQDepth=_MpCbQosQueueingCurrentQDepth_Object((1,3,6,1,4,1,5651,6,2,3,4,1,19,1,1,2),_MpCbQosQueueingCurrentQDepth_Type())
mpCbQosQueueingCurrentQDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosQueueingCurrentQDepth.setStatus(_A)
_MpCbQosQueueingMaxQDepth_Type=Gauge32
_MpCbQosQueueingMaxQDepth_Object=MibTableColumn
mpCbQosQueueingMaxQDepth=_MpCbQosQueueingMaxQDepth_Object((1,3,6,1,4,1,5651,6,2,3,4,1,19,1,1,3),_MpCbQosQueueingMaxQDepth_Type())
mpCbQosQueueingMaxQDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosQueueingMaxQDepth.setStatus(_A)
_MpCbQosQueueingDiscardByte64_Type=Counter64
_MpCbQosQueueingDiscardByte64_Object=MibTableColumn
mpCbQosQueueingDiscardByte64=_MpCbQosQueueingDiscardByte64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,19,1,1,4),_MpCbQosQueueingDiscardByte64_Type())
mpCbQosQueueingDiscardByte64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosQueueingDiscardByte64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosQueueingDiscardByte64.setUnits(_F)
_MpCbQosQueueingDiscardPkt64_Type=Counter64
_MpCbQosQueueingDiscardPkt64_Object=MibTableColumn
mpCbQosQueueingDiscardPkt64=_MpCbQosQueueingDiscardPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,19,1,1,5),_MpCbQosQueueingDiscardPkt64_Type())
mpCbQosQueueingDiscardPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosQueueingDiscardPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosQueueingDiscardPkt64.setUnits(_E)
_MpCbQosTSStats_ObjectIdentity=ObjectIdentity
mpCbQosTSStats=_MpCbQosTSStats_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,4,1,20))
_MpCbQosTSStatsTable_Object=MibTable
mpCbQosTSStatsTable=_MpCbQosTSStatsTable_Object((1,3,6,1,4,1,5651,6,2,3,4,1,20,1))
if mibBuilder.loadTexts:mpCbQosTSStatsTable.setStatus(_A)
_MpCbQosTSStatsEntry_Object=MibTableRow
mpCbQosTSStatsEntry=_MpCbQosTSStatsEntry_Object((1,3,6,1,4,1,5651,6,2,3,4,1,20,1,1))
mpCbQosTSStatsEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:mpCbQosTSStatsEntry.setStatus(_A)
_MpCbQosTSStatsDelayedByte64_Type=Counter64
_MpCbQosTSStatsDelayedByte64_Object=MibTableColumn
mpCbQosTSStatsDelayedByte64=_MpCbQosTSStatsDelayedByte64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,20,1,1,1),_MpCbQosTSStatsDelayedByte64_Type())
mpCbQosTSStatsDelayedByte64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosTSStatsDelayedByte64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosTSStatsDelayedByte64.setUnits(_F)
_MpCbQosTSStatsDelayedPkt64_Type=Counter64
_MpCbQosTSStatsDelayedPkt64_Object=MibTableColumn
mpCbQosTSStatsDelayedPkt64=_MpCbQosTSStatsDelayedPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,20,1,1,2),_MpCbQosTSStatsDelayedPkt64_Type())
mpCbQosTSStatsDelayedPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosTSStatsDelayedPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosTSStatsDelayedPkt64.setUnits(_E)
_MpCbQosTSStatsDropByte64_Type=Counter64
_MpCbQosTSStatsDropByte64_Object=MibTableColumn
mpCbQosTSStatsDropByte64=_MpCbQosTSStatsDropByte64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,20,1,1,3),_MpCbQosTSStatsDropByte64_Type())
mpCbQosTSStatsDropByte64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosTSStatsDropByte64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosTSStatsDropByte64.setUnits(_F)
_MpCbQosTSStatsDropPkt64_Type=Counter64
_MpCbQosTSStatsDropPkt64_Object=MibTableColumn
mpCbQosTSStatsDropPkt64=_MpCbQosTSStatsDropPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,20,1,1,4),_MpCbQosTSStatsDropPkt64_Type())
mpCbQosTSStatsDropPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosTSStatsDropPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosTSStatsDropPkt64.setUnits(_E)
_MpCbQosTSStatsActive_Type=TruthValue
_MpCbQosTSStatsActive_Object=MibTableColumn
mpCbQosTSStatsActive=_MpCbQosTSStatsActive_Object((1,3,6,1,4,1,5651,6,2,3,4,1,20,1,1,5),_MpCbQosTSStatsActive_Type())
mpCbQosTSStatsActive.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosTSStatsActive.setStatus(_A)
_MpCbQosTSStatsCurrentQSize_Type=Gauge32
_MpCbQosTSStatsCurrentQSize_Object=MibTableColumn
mpCbQosTSStatsCurrentQSize=_MpCbQosTSStatsCurrentQSize_Object((1,3,6,1,4,1,5651,6,2,3,4,1,20,1,1,6),_MpCbQosTSStatsCurrentQSize_Type())
mpCbQosTSStatsCurrentQSize.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosTSStatsCurrentQSize.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosTSStatsCurrentQSize.setUnits(_E)
_MpCbQosREDClassStats_ObjectIdentity=ObjectIdentity
mpCbQosREDClassStats=_MpCbQosREDClassStats_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,4,1,21))
_MpCbQosREDClassStatsTable_Object=MibTable
mpCbQosREDClassStatsTable=_MpCbQosREDClassStatsTable_Object((1,3,6,1,4,1,5651,6,2,3,4,1,21,1))
if mibBuilder.loadTexts:mpCbQosREDClassStatsTable.setStatus(_A)
_MpCbQosREDClassStatsEntry_Object=MibTableRow
mpCbQosREDClassStatsEntry=_MpCbQosREDClassStatsEntry_Object((1,3,6,1,4,1,5651,6,2,3,4,1,21,1,1))
mpCbQosREDClassStatsEntry.setIndexNames((0,_C,_I),(0,_C,_J),(0,_C,_X))
if mibBuilder.loadTexts:mpCbQosREDClassStatsEntry.setStatus(_A)
_MpCbQosREDRandomDropPkt64_Type=Counter64
_MpCbQosREDRandomDropPkt64_Object=MibTableColumn
mpCbQosREDRandomDropPkt64=_MpCbQosREDRandomDropPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,21,1,1,1),_MpCbQosREDRandomDropPkt64_Type())
mpCbQosREDRandomDropPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosREDRandomDropPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosREDRandomDropPkt64.setUnits(_E)
_MpCbQosREDRandomDropByte64_Type=Counter64
_MpCbQosREDRandomDropByte64_Object=MibTableColumn
mpCbQosREDRandomDropByte64=_MpCbQosREDRandomDropByte64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,21,1,1,2),_MpCbQosREDRandomDropByte64_Type())
mpCbQosREDRandomDropByte64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosREDRandomDropByte64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosREDRandomDropByte64.setUnits(_F)
_MpCbQosREDTailDropPkt64_Type=Counter64
_MpCbQosREDTailDropPkt64_Object=MibTableColumn
mpCbQosREDTailDropPkt64=_MpCbQosREDTailDropPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,21,1,1,3),_MpCbQosREDTailDropPkt64_Type())
mpCbQosREDTailDropPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosREDTailDropPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosREDTailDropPkt64.setUnits(_E)
_MpCbQosREDTailDropByte64_Type=Counter64
_MpCbQosREDTailDropByte64_Object=MibTableColumn
mpCbQosREDTailDropByte64=_MpCbQosREDTailDropByte64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,21,1,1,4),_MpCbQosREDTailDropByte64_Type())
mpCbQosREDTailDropByte64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosREDTailDropByte64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosREDTailDropByte64.setUnits(_F)
_MpCbQosREDTransmitPkt64_Type=Counter64
_MpCbQosREDTransmitPkt64_Object=MibTableColumn
mpCbQosREDTransmitPkt64=_MpCbQosREDTransmitPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,21,1,1,5),_MpCbQosREDTransmitPkt64_Type())
mpCbQosREDTransmitPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosREDTransmitPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosREDTransmitPkt64.setUnits(_E)
_MpCbQosREDTransmitByte64_Type=Counter64
_MpCbQosREDTransmitByte64_Object=MibTableColumn
mpCbQosREDTransmitByte64=_MpCbQosREDTransmitByte64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,21,1,1,6),_MpCbQosREDTransmitByte64_Type())
mpCbQosREDTransmitByte64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosREDTransmitByte64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosREDTransmitByte64.setUnits(_F)
_MpCbQosREDECNMarkPkt64_Type=Counter64
_MpCbQosREDECNMarkPkt64_Object=MibTableColumn
mpCbQosREDECNMarkPkt64=_MpCbQosREDECNMarkPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,21,1,1,7),_MpCbQosREDECNMarkPkt64_Type())
mpCbQosREDECNMarkPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosREDECNMarkPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosREDECNMarkPkt64.setUnits(_E)
_MpCbQosREDECNMarkByte64_Type=Counter64
_MpCbQosREDECNMarkByte64_Object=MibTableColumn
mpCbQosREDECNMarkByte64=_MpCbQosREDECNMarkByte64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,21,1,1,8),_MpCbQosREDECNMarkByte64_Type())
mpCbQosREDECNMarkByte64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosREDECNMarkByte64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosREDECNMarkByte64.setUnits(_F)
class _MpCbQosREDMeanQSizeUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5)))
_MpCbQosREDMeanQSizeUnits_Type.__name__=_D
_MpCbQosREDMeanQSizeUnits_Object=MibTableColumn
mpCbQosREDMeanQSizeUnits=_MpCbQosREDMeanQSizeUnits_Object((1,3,6,1,4,1,5651,6,2,3,4,1,21,1,1,9),_MpCbQosREDMeanQSizeUnits_Type())
mpCbQosREDMeanQSizeUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosREDMeanQSizeUnits.setStatus(_A)
_MpCbQosREDMeanQSize_Type=Unsigned32
_MpCbQosREDMeanQSize_Object=MibTableColumn
mpCbQosREDMeanQSize=_MpCbQosREDMeanQSize_Object((1,3,6,1,4,1,5651,6,2,3,4,1,21,1,1,10),_MpCbQosREDMeanQSize_Type())
mpCbQosREDMeanQSize.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosREDMeanQSize.setStatus(_A)
_MpCbQosSetStats_ObjectIdentity=ObjectIdentity
mpCbQosSetStats=_MpCbQosSetStats_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,4,1,22))
_MpCbQosSetStatsTable_Object=MibTable
mpCbQosSetStatsTable=_MpCbQosSetStatsTable_Object((1,3,6,1,4,1,5651,6,2,3,4,1,22,1))
if mibBuilder.loadTexts:mpCbQosSetStatsTable.setStatus(_A)
_MpCbQosSetStatsEntry_Object=MibTableRow
mpCbQosSetStatsEntry=_MpCbQosSetStatsEntry_Object((1,3,6,1,4,1,5651,6,2,3,4,1,22,1,1))
mpCbQosSetStatsEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:mpCbQosSetStatsEntry.setStatus(_A)
_MpCbQosSetDscpPkt64_Type=Counter64
_MpCbQosSetDscpPkt64_Object=MibTableColumn
mpCbQosSetDscpPkt64=_MpCbQosSetDscpPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,22,1,1,1),_MpCbQosSetDscpPkt64_Type())
mpCbQosSetDscpPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetDscpPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosSetDscpPkt64.setUnits(_E)
_MpCbQosSetPrecedencePkt64_Type=Counter64
_MpCbQosSetPrecedencePkt64_Object=MibTableColumn
mpCbQosSetPrecedencePkt64=_MpCbQosSetPrecedencePkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,22,1,1,2),_MpCbQosSetPrecedencePkt64_Type())
mpCbQosSetPrecedencePkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetPrecedencePkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosSetPrecedencePkt64.setUnits(_E)
_MpCbQosSetQosGroupPkt64_Type=Counter64
_MpCbQosSetQosGroupPkt64_Object=MibTableColumn
mpCbQosSetQosGroupPkt64=_MpCbQosSetQosGroupPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,22,1,1,3),_MpCbQosSetQosGroupPkt64_Type())
mpCbQosSetQosGroupPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetQosGroupPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosSetQosGroupPkt64.setUnits(_E)
_MpCbQosSetFrDePkt64_Type=Counter64
_MpCbQosSetFrDePkt64_Object=MibTableColumn
mpCbQosSetFrDePkt64=_MpCbQosSetFrDePkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,22,1,1,4),_MpCbQosSetFrDePkt64_Type())
mpCbQosSetFrDePkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetFrDePkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosSetFrDePkt64.setUnits(_E)
_MpCbQosSetAtmClpPkt64_Type=Counter64
_MpCbQosSetAtmClpPkt64_Object=MibTableColumn
mpCbQosSetAtmClpPkt64=_MpCbQosSetAtmClpPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,22,1,1,5),_MpCbQosSetAtmClpPkt64_Type())
mpCbQosSetAtmClpPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetAtmClpPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosSetAtmClpPkt64.setUnits(_E)
_MpCbQosSetL2CosPkt64_Type=Counter64
_MpCbQosSetL2CosPkt64_Object=MibTableColumn
mpCbQosSetL2CosPkt64=_MpCbQosSetL2CosPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,22,1,1,6),_MpCbQosSetL2CosPkt64_Type())
mpCbQosSetL2CosPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetL2CosPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosSetL2CosPkt64.setUnits(_E)
_MpCbQosSetMplsExpImpositionPkt64_Type=Counter64
_MpCbQosSetMplsExpImpositionPkt64_Object=MibTableColumn
mpCbQosSetMplsExpImpositionPkt64=_MpCbQosSetMplsExpImpositionPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,22,1,1,7),_MpCbQosSetMplsExpImpositionPkt64_Type())
mpCbQosSetMplsExpImpositionPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetMplsExpImpositionPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosSetMplsExpImpositionPkt64.setUnits(_E)
_MpCbQosSetDiscardClassPkt64_Type=Counter64
_MpCbQosSetDiscardClassPkt64_Object=MibTableColumn
mpCbQosSetDiscardClassPkt64=_MpCbQosSetDiscardClassPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,22,1,1,8),_MpCbQosSetDiscardClassPkt64_Type())
mpCbQosSetDiscardClassPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetDiscardClassPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosSetDiscardClassPkt64.setUnits(_E)
_MpCbQosSetMplsExpTopMostPkt64_Type=Counter64
_MpCbQosSetMplsExpTopMostPkt64_Object=MibTableColumn
mpCbQosSetMplsExpTopMostPkt64=_MpCbQosSetMplsExpTopMostPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,22,1,1,9),_MpCbQosSetMplsExpTopMostPkt64_Type())
mpCbQosSetMplsExpTopMostPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetMplsExpTopMostPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosSetMplsExpTopMostPkt64.setUnits(_E)
_MpCbQosSetFrFecnBecnPkt64_Type=Counter64
_MpCbQosSetFrFecnBecnPkt64_Object=MibTableColumn
mpCbQosSetFrFecnBecnPkt64=_MpCbQosSetFrFecnBecnPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,22,1,1,10),_MpCbQosSetFrFecnBecnPkt64_Type())
mpCbQosSetFrFecnBecnPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetFrFecnBecnPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosSetFrFecnBecnPkt64.setUnits(_E)
_MpCbQosSetDscpTunnelPkt64_Type=Counter64
_MpCbQosSetDscpTunnelPkt64_Object=MibTableColumn
mpCbQosSetDscpTunnelPkt64=_MpCbQosSetDscpTunnelPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,22,1,1,11),_MpCbQosSetDscpTunnelPkt64_Type())
mpCbQosSetDscpTunnelPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetDscpTunnelPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosSetDscpTunnelPkt64.setUnits(_E)
_MpCbQosSetPrecedenceTunnelPkt64_Type=Counter64
_MpCbQosSetPrecedenceTunnelPkt64_Object=MibTableColumn
mpCbQosSetPrecedenceTunnelPkt64=_MpCbQosSetPrecedenceTunnelPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,22,1,1,12),_MpCbQosSetPrecedenceTunnelPkt64_Type())
mpCbQosSetPrecedenceTunnelPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetPrecedenceTunnelPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosSetPrecedenceTunnelPkt64.setUnits(_E)
_MpCbQosSetTosPkt64_Type=Counter64
_MpCbQosSetTosPkt64_Object=MibTableColumn
mpCbQosSetTosPkt64=_MpCbQosSetTosPkt64_Object((1,3,6,1,4,1,5651,6,2,3,4,1,22,1,1,13),_MpCbQosSetTosPkt64_Type())
mpCbQosSetTosPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCbQosSetTosPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpCbQosSetTosPkt64.setUnits(_E)
mibBuilder.exportSymbols(_C,**{'Unsigned64':Unsigned64,'maipu':maipu,'mpMgmt2':mpMgmt2,'mpRouterTech':mpRouterTech,'mpRtQoSv2':mpRtQoSv2,'maipuCBQosMIB':maipuCBQosMIB,'maipuCBQosMIBObjects':maipuCBQosMIBObjects,'mpCbQosServicePolicy':mpCbQosServicePolicy,'mpCbQosServicePolicyTable':mpCbQosServicePolicyTable,'mpCbQosServicePolicyEntry':mpCbQosServicePolicyEntry,_I:mpCbQosPolicyIndex,'mpCbQosIfType':mpCbQosIfType,_T:mpCbQosPolicyDirection,'mpCbQosIfIndex':mpCbQosIfIndex,_n:mpCbQosFrDLCI,_o:mpCbQosAtmVPI,_p:mpCbQosAtmVCI,'mpCbQosEntityIndex':mpCbQosEntityIndex,'mpCbQosVlanIndex':mpCbQosVlanIndex,'mpCbQosInterfacePolicy':mpCbQosInterfacePolicy,'mpCbQosInterfacePolicyTable':mpCbQosInterfacePolicyTable,'mpCbQosInterfacePolicyEntry':mpCbQosInterfacePolicyEntry,'mpCbQosIFPolicyIndex':mpCbQosIFPolicyIndex,'mpCbQosFrameRelayVCPolicy':mpCbQosFrameRelayVCPolicy,'mpCbQosFrameRelayPolicyTable':mpCbQosFrameRelayPolicyTable,'mpCbQosFrameRelayPolicyEntry':mpCbQosFrameRelayPolicyEntry,'mpCbQosFRPolicyIndex':mpCbQosFRPolicyIndex,'mpCbQosATMPVCPolicy':mpCbQosATMPVCPolicy,'mpCbQosATMPVCPolicyTable':mpCbQosATMPVCPolicyTable,'mpCbQosATMPVCPolicyEntry':mpCbQosATMPVCPolicyEntry,'mpCbQosATMPVCPolicyIndex':mpCbQosATMPVCPolicyIndex,'mpCbQosObjects':mpCbQosObjects,'mpCbQosObjectsTable':mpCbQosObjectsTable,'mpCbQosObjectsEntry':mpCbQosObjectsEntry,_J:mpCbQosObjectsIndex,_H:mpCbQosConfigIndex,'mpCbQosObjectsType':mpCbQosObjectsType,'mpCbQosParentObjectsIndex':mpCbQosParentObjectsIndex,'mpCbQosPolicyMapCfg':mpCbQosPolicyMapCfg,'mpCbQosPolicyMapCfgTable':mpCbQosPolicyMapCfgTable,'mpCbQosPolicyMapCfgEntry':mpCbQosPolicyMapCfgEntry,'mpCbQosPolicyMapName':mpCbQosPolicyMapName,'mpCbQosPolicyMapDesc':mpCbQosPolicyMapDesc,'mpCbQosClassMapCfg':mpCbQosClassMapCfg,'mpCbQosCMCfgTable':mpCbQosCMCfgTable,'mpCbQosCMCfgEntry':mpCbQosCMCfgEntry,'mpCbQosCMName':mpCbQosCMName,'mpCbQosCMDesc':mpCbQosCMDesc,'mpCbQosCMInfo':mpCbQosCMInfo,'mpCbQosMatchStmtCfg':mpCbQosMatchStmtCfg,'mpCbQosMatchStmtCfgTable':mpCbQosMatchStmtCfgTable,'mpCbQosMatchStmtCfgEntry':mpCbQosMatchStmtCfgEntry,'mpCbQosMatchStmtName':mpCbQosMatchStmtName,'mpCbQosMatchStmtInfo':mpCbQosMatchStmtInfo,'mpCbQosQueueingCfg':mpCbQosQueueingCfg,'mpCbQosQueueingCfgTable':mpCbQosQueueingCfgTable,'mpCbQosQueueingCfgEntry':mpCbQosQueueingCfgEntry,'mpCbQosQueueingCfgBandwidth':mpCbQosQueueingCfgBandwidth,'mpCbQosQueueingCfgBandwidthUnits':mpCbQosQueueingCfgBandwidthUnits,'mpCbQosQueueingCfgFlowEnabled':mpCbQosQueueingCfgFlowEnabled,'mpCbQosQueueingCfgPriorityEnabled':mpCbQosQueueingCfgPriorityEnabled,'mpCbQosQueueingCfgDynamicQNumber':mpCbQosQueueingCfgDynamicQNumber,'mpCbQosQueueingCfgPrioBurstSize':mpCbQosQueueingCfgPrioBurstSize,'mpCbQosQueueingCfgQLimitUnits':mpCbQosQueueingCfgQLimitUnits,'mpCbQosQueueingCfgAggregateQLimit':mpCbQosQueueingCfgAggregateQLimit,'mpCbQosQueueingCfgAggrQLimitTime':mpCbQosQueueingCfgAggrQLimitTime,'mpCbQosQueueingCfgIndividualQLimit':mpCbQosQueueingCfgIndividualQLimit,'mpCbQosREDCfg':mpCbQosREDCfg,'mpCbQosREDCfgTable':mpCbQosREDCfgTable,'mpCbQosREDCfgEntry':mpCbQosREDCfgEntry,'mpCbQosREDCfgExponWeight':mpCbQosREDCfgExponWeight,'mpCbQosREDCfgDscpPrec':mpCbQosREDCfgDscpPrec,'mpCbQosREDCfgECNEnabled':mpCbQosREDCfgECNEnabled,'mpCbQosREDClassCfg':mpCbQosREDClassCfg,'mpCbQosREDClassCfgTable':mpCbQosREDClassCfgTable,'mpCbQosREDClassCfgEntry':mpCbQosREDClassCfgEntry,_X:mpCbQosREDValue,'mpCbQosREDCfgPktDropProb':mpCbQosREDCfgPktDropProb,'mpCbQosREDClassCfgMinThresholdUnit':mpCbQosREDClassCfgMinThresholdUnit,'mpCbQosREDClassCfgMaxThresholdUnit':mpCbQosREDClassCfgMaxThresholdUnit,'mpCbQosREDClassCfgMinThreshold':mpCbQosREDClassCfgMinThreshold,'mpCbQosREDClassCfgMaxThreshold':mpCbQosREDClassCfgMaxThreshold,'mpCbQosREDClassCfgMinThresholdTime':mpCbQosREDClassCfgMinThresholdTime,'mpCbQosREDClassCfgMaxThresholdTime':mpCbQosREDClassCfgMaxThresholdTime,'mpCbQosPoliceCfg':mpCbQosPoliceCfg,'mpCbQosPoliceCfgTable':mpCbQosPoliceCfgTable,'mpCbQosPoliceCfgEntry':mpCbQosPoliceCfgEntry,'mpCbQosPoliceCfgRate64':mpCbQosPoliceCfgRate64,'mpCbQosPoliceCfgBurstSize':mpCbQosPoliceCfgBurstSize,'mpCbQosPoliceCfgExtBurstSize':mpCbQosPoliceCfgExtBurstSize,'mpCbQosPoliceCfgPir64':mpCbQosPoliceCfgPir64,'mpCbQosPoliceCfgRateType':mpCbQosPoliceCfgRateType,'mpCbQosPoliceCfgPercentRateValue':mpCbQosPoliceCfgPercentRateValue,'mpCbQosPoliceCfgPercentPirValue':mpCbQosPoliceCfgPercentPirValue,'mpCbQosPoliceCfgCellRate':mpCbQosPoliceCfgCellRate,'mpCbQosPoliceCfgCellPir':mpCbQosPoliceCfgCellPir,'mpCbQosPoliceCfgBurstCell':mpCbQosPoliceCfgBurstCell,'mpCbQosPoliceCfgExtBurstCell':mpCbQosPoliceCfgExtBurstCell,'mpCbQosPoliceCfgBurstTime':mpCbQosPoliceCfgBurstTime,'mpCbQosPoliceCfgExtBurstTime':mpCbQosPoliceCfgExtBurstTime,'mpCbQosPoliceActionCfg':mpCbQosPoliceActionCfg,'mpCbQosPoliceActionCfgTable':mpCbQosPoliceActionCfgTable,'mpCbQosPoliceActionCfgEntry':mpCbQosPoliceActionCfgEntry,_t:mpCbQosPoliceActionCfgIndex,'mpCbQosPoliceActionCfgConform':mpCbQosPoliceActionCfgConform,'mpCbQosPoliceActionCfgConformSetValue':mpCbQosPoliceActionCfgConformSetValue,'mpCbQosPoliceActionCfgExceed':mpCbQosPoliceActionCfgExceed,'mpCbQosPoliceActionCfgExceedSetValue':mpCbQosPoliceActionCfgExceedSetValue,'mpCbQosPoliceActionCfgViolate':mpCbQosPoliceActionCfgViolate,'mpCbQosPoliceActionCfgViolateSetValue':mpCbQosPoliceActionCfgViolateSetValue,'mpCbQosTSCfg':mpCbQosTSCfg,'mpCbQosTSCfgTable':mpCbQosTSCfgTable,'mpCbQosTSCfgEntry':mpCbQosTSCfgEntry,'mpCbQosTSCfgRate64':mpCbQosTSCfgRate64,'mpCbQosTSCfgBurstSize':mpCbQosTSCfgBurstSize,'mpCbQosTSCfgExtBurstSize':mpCbQosTSCfgExtBurstSize,'mpCbQosTSCfgAdaptiveEnabled':mpCbQosTSCfgAdaptiveEnabled,'mpCbQosTSCfgAdaptiveRate64':mpCbQosTSCfgAdaptiveRate64,'mpCbQosTSCfgLimitType':mpCbQosTSCfgLimitType,'mpCbQosTSCfgRateType':mpCbQosTSCfgRateType,'mpCbQosTSCfgPercentRateValue':mpCbQosTSCfgPercentRateValue,'mpCbQosTSCfgBurstTime':mpCbQosTSCfgBurstTime,'mpCbQosTSCfgExtBurstTime':mpCbQosTSCfgExtBurstTime,'mpCbQosSetCfg':mpCbQosSetCfg,'mpCbQosSetCfgTable':mpCbQosSetCfgTable,'mpCbQosSetCfgEntry':mpCbQosSetCfgEntry,'mpCbQosSetCfgFeature':mpCbQosSetCfgFeature,'mpCbQosSetCfgIpDSCPValue':mpCbQosSetCfgIpDSCPValue,'mpCbQosSetCfgIpPrecedenceValue':mpCbQosSetCfgIpPrecedenceValue,'mpCbQosSetCfgQosGroupValue':mpCbQosSetCfgQosGroupValue,'mpCbQosSetCfgL2CosValue':mpCbQosSetCfgL2CosValue,'mpCbQosSetCfgMplsExpValue':mpCbQosSetCfgMplsExpValue,'mpCbQosSetCfgDiscardClassValue':mpCbQosSetCfgDiscardClassValue,'mpCbQosSetCfgMplsExpTopMostValue':mpCbQosSetCfgMplsExpTopMostValue,'mpCbQosSetCfgFrFecnBecn':mpCbQosSetCfgFrFecnBecn,'mpCbQosSetCfgIpDSCPTunnelValue':mpCbQosSetCfgIpDSCPTunnelValue,'mpCbQosSetCfgIpPrecedenceTunnelValue':mpCbQosSetCfgIpPrecedenceTunnelValue,'mpCbQosSetCfgL2CosInnerValue':mpCbQosSetCfgL2CosInnerValue,'mpCbQosSetCfgIpTosValue':mpCbQosSetCfgIpTosValue,'mpCbQosClassMapStats':mpCbQosClassMapStats,'mpCbQosCMStatsTable':mpCbQosCMStatsTable,'mpCbQosCMStatsEntry':mpCbQosCMStatsEntry,'mpCbQosCMPrePolicyPkt64':mpCbQosCMPrePolicyPkt64,'mpCbQosCMPrePolicyByte64':mpCbQosCMPrePolicyByte64,'mpCbQosCMPrePolicyBitRate64':mpCbQosCMPrePolicyBitRate64,'mpCbQosCMPostPolicyPkt64':mpCbQosCMPostPolicyPkt64,'mpCbQosCMPostPolicyByte64':mpCbQosCMPostPolicyByte64,'mpCbQosCMPostPolicyBitRate64':mpCbQosCMPostPolicyBitRate64,'mpCbQosCMDropPkt64':mpCbQosCMDropPkt64,'mpCbQosCMDropByte64':mpCbQosCMDropByte64,'mpCbQosCMDropBitRate64':mpCbQosCMDropBitRate64,'mpCbQosCMNoBufDropPkt64':mpCbQosCMNoBufDropPkt64,'mpCbQosMatchStmtStats':mpCbQosMatchStmtStats,'mpCbQosMatchStmtStatsTable':mpCbQosMatchStmtStatsTable,'mpCbQosMatchStmtStatsEntry':mpCbQosMatchStmtStatsEntry,'mpCbQosMatchPrePolicyPkt64':mpCbQosMatchPrePolicyPkt64,'mpCbQosMatchPrePolicyByte64':mpCbQosMatchPrePolicyByte64,'mpCbQosMatchPrePolicyBitRate64':mpCbQosMatchPrePolicyBitRate64,'mpCbQosPoliceStats':mpCbQosPoliceStats,'mpCbQosPoliceStatsTable':mpCbQosPoliceStatsTable,'mpCbQosPoliceStatsEntry':mpCbQosPoliceStatsEntry,'mpCbQosPoliceConformedPkt64':mpCbQosPoliceConformedPkt64,'mpCbQosPoliceConformedByte64':mpCbQosPoliceConformedByte64,'mpCbQosPoliceConformedBitRate64':mpCbQosPoliceConformedBitRate64,'mpCbQosPoliceExceededPkt64':mpCbQosPoliceExceededPkt64,'mpCbQosPoliceExceededByte64':mpCbQosPoliceExceededByte64,'mpCbQosPoliceExceededBitRate64':mpCbQosPoliceExceededBitRate64,'mpCbQosPoliceViolatedPkt64':mpCbQosPoliceViolatedPkt64,'mpCbQosPoliceViolatedByte64':mpCbQosPoliceViolatedByte64,'mpCbQosPoliceViolatedBitRate64':mpCbQosPoliceViolatedBitRate64,'mpCbQosQueueingStats':mpCbQosQueueingStats,'mpCbQosQueueingStatsTable':mpCbQosQueueingStatsTable,'mpCbQosQueueingStatsEntry':mpCbQosQueueingStatsEntry,'mpCbQosQueueingQDepthUnit':mpCbQosQueueingQDepthUnit,'mpCbQosQueueingCurrentQDepth':mpCbQosQueueingCurrentQDepth,'mpCbQosQueueingMaxQDepth':mpCbQosQueueingMaxQDepth,'mpCbQosQueueingDiscardByte64':mpCbQosQueueingDiscardByte64,'mpCbQosQueueingDiscardPkt64':mpCbQosQueueingDiscardPkt64,'mpCbQosTSStats':mpCbQosTSStats,'mpCbQosTSStatsTable':mpCbQosTSStatsTable,'mpCbQosTSStatsEntry':mpCbQosTSStatsEntry,'mpCbQosTSStatsDelayedByte64':mpCbQosTSStatsDelayedByte64,'mpCbQosTSStatsDelayedPkt64':mpCbQosTSStatsDelayedPkt64,'mpCbQosTSStatsDropByte64':mpCbQosTSStatsDropByte64,'mpCbQosTSStatsDropPkt64':mpCbQosTSStatsDropPkt64,'mpCbQosTSStatsActive':mpCbQosTSStatsActive,'mpCbQosTSStatsCurrentQSize':mpCbQosTSStatsCurrentQSize,'mpCbQosREDClassStats':mpCbQosREDClassStats,'mpCbQosREDClassStatsTable':mpCbQosREDClassStatsTable,'mpCbQosREDClassStatsEntry':mpCbQosREDClassStatsEntry,'mpCbQosREDRandomDropPkt64':mpCbQosREDRandomDropPkt64,'mpCbQosREDRandomDropByte64':mpCbQosREDRandomDropByte64,'mpCbQosREDTailDropPkt64':mpCbQosREDTailDropPkt64,'mpCbQosREDTailDropByte64':mpCbQosREDTailDropByte64,'mpCbQosREDTransmitPkt64':mpCbQosREDTransmitPkt64,'mpCbQosREDTransmitByte64':mpCbQosREDTransmitByte64,'mpCbQosREDECNMarkPkt64':mpCbQosREDECNMarkPkt64,'mpCbQosREDECNMarkByte64':mpCbQosREDECNMarkByte64,'mpCbQosREDMeanQSizeUnits':mpCbQosREDMeanQSizeUnits,'mpCbQosREDMeanQSize':mpCbQosREDMeanQSize,'mpCbQosSetStats':mpCbQosSetStats,'mpCbQosSetStatsTable':mpCbQosSetStatsTable,'mpCbQosSetStatsEntry':mpCbQosSetStatsEntry,'mpCbQosSetDscpPkt64':mpCbQosSetDscpPkt64,'mpCbQosSetPrecedencePkt64':mpCbQosSetPrecedencePkt64,'mpCbQosSetQosGroupPkt64':mpCbQosSetQosGroupPkt64,'mpCbQosSetFrDePkt64':mpCbQosSetFrDePkt64,'mpCbQosSetAtmClpPkt64':mpCbQosSetAtmClpPkt64,'mpCbQosSetL2CosPkt64':mpCbQosSetL2CosPkt64,'mpCbQosSetMplsExpImpositionPkt64':mpCbQosSetMplsExpImpositionPkt64,'mpCbQosSetDiscardClassPkt64':mpCbQosSetDiscardClassPkt64,'mpCbQosSetMplsExpTopMostPkt64':mpCbQosSetMplsExpTopMostPkt64,'mpCbQosSetFrFecnBecnPkt64':mpCbQosSetFrFecnBecnPkt64,'mpCbQosSetDscpTunnelPkt64':mpCbQosSetDscpTunnelPkt64,'mpCbQosSetPrecedenceTunnelPkt64':mpCbQosSetPrecedenceTunnelPkt64,'mpCbQosSetTosPkt64':mpCbQosSetTosPkt64})