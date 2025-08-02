_AI='ibmappnCosTgRowIndex'
_AH='ibmappnCosTgRowName'
_AG='ibmappnCosNodeRowIndex'
_AF='ibmappnCosNodeRowName'
_AE='ibmappnCosName'
_AD='ibmappnCosModeName'
_AC='ibmappnDirLuName'
_AB='ibmappnLocalEnTgNum'
_AA='ibmappnLocalEnTgDest'
_A9='ibmappnLocalEnTgOrigin'
_A8='ibmappnLocalEnName'
_A7='ibmappnLocalTgNum'
_A6='ibmappnLocalTgDest'
_A5='ibmappnNnTgFRNum'
_A4='ibmappnNnTgFRDest'
_A3='ibmappnNnTgFROwner'
_A2='ibmappnNnTgFRFrsn'
_A1='ibmappnNnNodeFRName'
_A0='ibmappnNnNodeFRFrsn'
_z='ibmappnNnTgNum'
_y='ibmappnNnTgDest'
_x='ibmappnNnTgOwner'
_w='virtualnode'
_v='ibmappnNnNodeName'
_u='ibmappnNnAdjNodeAdjName'
_t='ibmappnNnTopoRouteCos'
_s='ibmappnNodeLsStatusIndex'
_r='ibmappnNodeLsTrName'
_q='ibmappnNodeLsDlsName'
_p='ibmappnNodeLsIpName'
_o='ibmappnNodeLsName'
_n='ibmappnNodePortDlcTracIndex'
_m='ibmappnNodePortDlcTracPortName'
_l='ibmappnNodePortTrName'
_k='ibmappnNodePortDlsName'
_j='ibmappnNodePortIpName'
_i='read-write'
_h='ibmappnNodePortName'
_g='networknode'
_f='tokenRing'
_e='len'
_d='ethernet'
_c='socket'
_b='dls'
_a='sdlc'
_Z='pendinact'
_Y='pendactive'
_X='maximum'
_W='long'
_V='packet'
_U='terrestrial'
_T='negligible'
_S='minimum'
_R='guardedRadiation'
_Q='encrypted'
_P='guardedConduit'
_O='secureConduit'
_N='undergroundCable'
_M='publicSwitchedNetwork'
_L='nonsecure'
_K='other'
_J='active'
_I='inactive'
_H='OctetString'
_G='IBM-6611-APPN-MIB'
_F='DisplayString'
_E='no'
_D='yes'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
_Ibm_ObjectIdentity=ObjectIdentity
ibm=_Ibm_ObjectIdentity((1,3,6,1,4,1,2))
_IbmProd_ObjectIdentity=ObjectIdentity
ibmProd=_IbmProd_ObjectIdentity((1,3,6,1,4,1,2,6))
_Ibm6611_ObjectIdentity=ObjectIdentity
ibm6611=_Ibm6611_ObjectIdentity((1,3,6,1,4,1,2,6,2))
_Ibmappn_ObjectIdentity=ObjectIdentity
ibmappn=_Ibmappn_ObjectIdentity((1,3,6,1,4,1,2,6,2,13))
_IbmappnNode_ObjectIdentity=ObjectIdentity
ibmappnNode=_IbmappnNode_ObjectIdentity((1,3,6,1,4,1,2,6,2,13,1))
_IbmappnGeneralInfoAndCaps_ObjectIdentity=ObjectIdentity
ibmappnGeneralInfoAndCaps=_IbmappnGeneralInfoAndCaps_ObjectIdentity((1,3,6,1,4,1,2,6,2,13,1,1))
class _IbmappnNodeCpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_IbmappnNodeCpName_Type.__name__=_F
_IbmappnNodeCpName_Object=MibScalar
ibmappnNodeCpName=_IbmappnNodeCpName_Object((1,3,6,1,4,1,2,6,2,13,1,1,1),_IbmappnNodeCpName_Type())
ibmappnNodeCpName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeCpName.setStatus(_A)
class _IbmappnNodeNetid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_IbmappnNodeNetid_Type.__name__=_F
_IbmappnNodeNetid_Object=MibScalar
ibmappnNodeNetid=_IbmappnNodeNetid_Object((1,3,6,1,4,1,2,6,2,13,1,1,2),_IbmappnNodeNetid_Type())
ibmappnNodeNetid.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeNetid.setStatus(_A)
class _IbmappnNodeBlockNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_IbmappnNodeBlockNum_Type.__name__=_F
_IbmappnNodeBlockNum_Object=MibScalar
ibmappnNodeBlockNum=_IbmappnNodeBlockNum_Object((1,3,6,1,4,1,2,6,2,13,1,1,3),_IbmappnNodeBlockNum_Type())
ibmappnNodeBlockNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeBlockNum.setStatus(_A)
class _IbmappnNodeIdNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_IbmappnNodeIdNum_Type.__name__=_F
_IbmappnNodeIdNum_Object=MibScalar
ibmappnNodeIdNum=_IbmappnNodeIdNum_Object((1,3,6,1,4,1,2,6,2,13,1,1,4),_IbmappnNodeIdNum_Type())
ibmappnNodeIdNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeIdNum.setStatus(_A)
class _IbmappnNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('networkNode',1),('endNode',2),(_e,4)))
_IbmappnNodeType_Type.__name__=_C
_IbmappnNodeType_Object=MibScalar
ibmappnNodeType=_IbmappnNodeType_Object((1,3,6,1,4,1,2,6,2,13,1,1,5),_IbmappnNodeType_Type())
ibmappnNodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeType.setStatus(_A)
_IbmappnNodeUpTime_Type=TimeTicks
_IbmappnNodeUpTime_Object=MibScalar
ibmappnNodeUpTime=_IbmappnNodeUpTime_Object((1,3,6,1,4,1,2,6,2,13,1,1,6),_IbmappnNodeUpTime_Type())
ibmappnNodeUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeUpTime.setStatus(_A)
class _IbmappnNodeNegotLs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNodeNegotLs_Type.__name__=_C
_IbmappnNodeNegotLs_Object=MibScalar
ibmappnNodeNegotLs=_IbmappnNodeNegotLs_Object((1,3,6,1,4,1,2,6,2,13,1,1,7),_IbmappnNodeNegotLs_Type())
ibmappnNodeNegotLs.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeNegotLs.setStatus(_A)
class _IbmappnNodeSegReasm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNodeSegReasm_Type.__name__=_C
_IbmappnNodeSegReasm_Object=MibScalar
ibmappnNodeSegReasm=_IbmappnNodeSegReasm_Object((1,3,6,1,4,1,2,6,2,13,1,1,8),_IbmappnNodeSegReasm_Type())
ibmappnNodeSegReasm.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeSegReasm.setStatus(_A)
class _IbmappnNodeBindReasm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNodeBindReasm_Type.__name__=_C
_IbmappnNodeBindReasm_Object=MibScalar
ibmappnNodeBindReasm=_IbmappnNodeBindReasm_Object((1,3,6,1,4,1,2,6,2,13,1,1,9),_IbmappnNodeBindReasm_Type())
ibmappnNodeBindReasm.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeBindReasm.setStatus(_A)
class _IbmappnNodeParallelTg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNodeParallelTg_Type.__name__=_C
_IbmappnNodeParallelTg_Object=MibScalar
ibmappnNodeParallelTg=_IbmappnNodeParallelTg_Object((1,3,6,1,4,1,2,6,2,13,1,1,10),_IbmappnNodeParallelTg_Type())
ibmappnNodeParallelTg.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeParallelTg.setStatus(_A)
class _IbmappnNodeService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNodeService_Type.__name__=_C
_IbmappnNodeService_Object=MibScalar
ibmappnNodeService=_IbmappnNodeService_Object((1,3,6,1,4,1,2,6,2,13,1,1,11),_IbmappnNodeService_Type())
ibmappnNodeService.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeService.setStatus(_A)
class _IbmappnNodeAdaptiveBindPacing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNodeAdaptiveBindPacing_Type.__name__=_C
_IbmappnNodeAdaptiveBindPacing_Object=MibScalar
ibmappnNodeAdaptiveBindPacing=_IbmappnNodeAdaptiveBindPacing_Object((1,3,6,1,4,1,2,6,2,13,1,1,12),_IbmappnNodeAdaptiveBindPacing_Type())
ibmappnNodeAdaptiveBindPacing.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeAdaptiveBindPacing.setStatus(_A)
_IbmappnNnUniqueInfoAndCaps_ObjectIdentity=ObjectIdentity
ibmappnNnUniqueInfoAndCaps=_IbmappnNnUniqueInfoAndCaps_ObjectIdentity((1,3,6,1,4,1,2,6,2,13,1,2))
class _IbmappnNodeNnRcvRegChar_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNodeNnRcvRegChar_Type.__name__=_C
_IbmappnNodeNnRcvRegChar_Object=MibScalar
ibmappnNodeNnRcvRegChar=_IbmappnNodeNnRcvRegChar_Object((1,3,6,1,4,1,2,6,2,13,1,2,1),_IbmappnNodeNnRcvRegChar_Type())
ibmappnNodeNnRcvRegChar.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeNnRcvRegChar.setStatus(_A)
class _IbmappnNodeNnGateway_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNodeNnGateway_Type.__name__=_C
_IbmappnNodeNnGateway_Object=MibScalar
ibmappnNodeNnGateway=_IbmappnNodeNnGateway_Object((1,3,6,1,4,1,2,6,2,13,1,2,2),_IbmappnNodeNnGateway_Type())
ibmappnNodeNnGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeNnGateway.setStatus(_A)
class _IbmappnNodeNnCentralDirectory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNodeNnCentralDirectory_Type.__name__=_C
_IbmappnNodeNnCentralDirectory_Object=MibScalar
ibmappnNodeNnCentralDirectory=_IbmappnNodeNnCentralDirectory_Object((1,3,6,1,4,1,2,6,2,13,1,2,3),_IbmappnNodeNnCentralDirectory_Type())
ibmappnNodeNnCentralDirectory.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeNnCentralDirectory.setStatus(_A)
class _IbmappnNodeNnTreeCache_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNodeNnTreeCache_Type.__name__=_C
_IbmappnNodeNnTreeCache_Object=MibScalar
ibmappnNodeNnTreeCache=_IbmappnNodeNnTreeCache_Object((1,3,6,1,4,1,2,6,2,13,1,2,4),_IbmappnNodeNnTreeCache_Type())
ibmappnNodeNnTreeCache.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeNnTreeCache.setStatus(_A)
class _IbmappnNodeNnTreeUpdate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNodeNnTreeUpdate_Type.__name__=_C
_IbmappnNodeNnTreeUpdate_Object=MibScalar
ibmappnNodeNnTreeUpdate=_IbmappnNodeNnTreeUpdate_Object((1,3,6,1,4,1,2,6,2,13,1,2,5),_IbmappnNodeNnTreeUpdate_Type())
ibmappnNodeNnTreeUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeNnTreeUpdate.setStatus(_A)
_IbmappnNodeNnRouteAddResist_Type=Integer32
_IbmappnNodeNnRouteAddResist_Object=MibScalar
ibmappnNodeNnRouteAddResist=_IbmappnNodeNnRouteAddResist_Object((1,3,6,1,4,1,2,6,2,13,1,2,6),_IbmappnNodeNnRouteAddResist_Type())
ibmappnNodeNnRouteAddResist.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeNnRouteAddResist.setStatus(_A)
class _IbmappnNodeNnIsr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNodeNnIsr_Type.__name__=_C
_IbmappnNodeNnIsr_Object=MibScalar
ibmappnNodeNnIsr=_IbmappnNodeNnIsr_Object((1,3,6,1,4,1,2,6,2,13,1,2,7),_IbmappnNodeNnIsr_Type())
ibmappnNodeNnIsr.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeNnIsr.setStatus(_A)
class _IbmappnNodeNnFrsn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IbmappnNodeNnFrsn_Type.__name__=_C
_IbmappnNodeNnFrsn_Object=MibScalar
ibmappnNodeNnFrsn=_IbmappnNodeNnFrsn_Object((1,3,6,1,4,1,2,6,2,13,1,2,8),_IbmappnNodeNnFrsn_Type())
ibmappnNodeNnFrsn.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeNnFrsn.setStatus(_A)
_IbmappnEnUniqueCaps_ObjectIdentity=ObjectIdentity
ibmappnEnUniqueCaps=_IbmappnEnUniqueCaps_ObjectIdentity((1,3,6,1,4,1,2,6,2,13,1,3))
class _IbmappnNodeEnSegGen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNodeEnSegGen_Type.__name__=_C
_IbmappnNodeEnSegGen_Object=MibScalar
ibmappnNodeEnSegGen=_IbmappnNodeEnSegGen_Object((1,3,6,1,4,1,2,6,2,13,1,3,1),_IbmappnNodeEnSegGen_Type())
ibmappnNodeEnSegGen.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeEnSegGen.setStatus(_A)
class _IbmappnNodeEnModeCosMap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNodeEnModeCosMap_Type.__name__=_C
_IbmappnNodeEnModeCosMap_Object=MibScalar
ibmappnNodeEnModeCosMap=_IbmappnNodeEnModeCosMap_Object((1,3,6,1,4,1,2,6,2,13,1,3,2),_IbmappnNodeEnModeCosMap_Type())
ibmappnNodeEnModeCosMap.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeEnModeCosMap.setStatus(_A)
class _IbmappnNodeEnLocateCdinit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNodeEnLocateCdinit_Type.__name__=_C
_IbmappnNodeEnLocateCdinit_Object=MibScalar
ibmappnNodeEnLocateCdinit=_IbmappnNodeEnLocateCdinit_Object((1,3,6,1,4,1,2,6,2,13,1,3,3),_IbmappnNodeEnLocateCdinit_Type())
ibmappnNodeEnLocateCdinit.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeEnLocateCdinit.setStatus(_A)
class _IbmappnNodeEnSendRegNames_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNodeEnSendRegNames_Type.__name__=_C
_IbmappnNodeEnSendRegNames_Object=MibScalar
ibmappnNodeEnSendRegNames=_IbmappnNodeEnSendRegNames_Object((1,3,6,1,4,1,2,6,2,13,1,3,4),_IbmappnNodeEnSendRegNames_Type())
ibmappnNodeEnSendRegNames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeEnSendRegNames.setStatus(_A)
class _IbmappnNodeEnSendRegChar_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNodeEnSendRegChar_Type.__name__=_C
_IbmappnNodeEnSendRegChar_Object=MibScalar
ibmappnNodeEnSendRegChar=_IbmappnNodeEnSendRegChar_Object((1,3,6,1,4,1,2,6,2,13,1,3,5),_IbmappnNodeEnSendRegChar_Type())
ibmappnNodeEnSendRegChar.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeEnSendRegChar.setStatus(_A)
_IbmappnPortInformation_ObjectIdentity=ObjectIdentity
ibmappnPortInformation=_IbmappnPortInformation_ObjectIdentity((1,3,6,1,4,1,2,6,2,13,1,4))
_IbmappnNodePortTable_Object=MibTable
ibmappnNodePortTable=_IbmappnNodePortTable_Object((1,3,6,1,4,1,2,6,2,13,1,4,1))
if mibBuilder.loadTexts:ibmappnNodePortTable.setStatus(_A)
_IbmappnNodePortEntry_Object=MibTableRow
ibmappnNodePortEntry=_IbmappnNodePortEntry_Object((1,3,6,1,4,1,2,6,2,13,1,4,1,1))
ibmappnNodePortEntry.setIndexNames((0,_G,_h))
if mibBuilder.loadTexts:ibmappnNodePortEntry.setStatus(_A)
class _IbmappnNodePortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_IbmappnNodePortName_Type.__name__=_F
_IbmappnNodePortName_Object=MibTableColumn
ibmappnNodePortName=_IbmappnNodePortName_Object((1,3,6,1,4,1,2,6,2,13,1,4,1,1,1),_IbmappnNodePortName_Type())
ibmappnNodePortName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortName.setStatus(_A)
class _IbmappnNodePortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_Y,2),(_J,3),(_Z,4)))
_IbmappnNodePortState_Type.__name__=_C
_IbmappnNodePortState_Object=MibTableColumn
ibmappnNodePortState=_IbmappnNodePortState_Object((1,3,6,1,4,1,2,6,2,13,1,4,1,1,2),_IbmappnNodePortState_Type())
ibmappnNodePortState.setMaxAccess(_i)
if mibBuilder.loadTexts:ibmappnNodePortState.setStatus(_A)
class _IbmappnNodePortDlcType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_K,1),(_a,2),(_b,3),(_c,4),(_d,5),(_f,6)))
_IbmappnNodePortDlcType_Type.__name__=_C
_IbmappnNodePortDlcType_Object=MibTableColumn
ibmappnNodePortDlcType=_IbmappnNodePortDlcType_Object((1,3,6,1,4,1,2,6,2,13,1,4,1,1,3),_IbmappnNodePortDlcType_Type())
ibmappnNodePortDlcType.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortDlcType.setStatus(_A)
class _IbmappnNodePortPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('leased',1),('switched',2),('sharedAccessFacilities',3)))
_IbmappnNodePortPortType_Type.__name__=_C
_IbmappnNodePortPortType_Object=MibTableColumn
ibmappnNodePortPortType=_IbmappnNodePortPortType_Object((1,3,6,1,4,1,2,6,2,13,1,4,1,1,4),_IbmappnNodePortPortType_Type())
ibmappnNodePortPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortPortType.setStatus(_A)
class _IbmappnNodePortSIMRIM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNodePortSIMRIM_Type.__name__=_C
_IbmappnNodePortSIMRIM_Object=MibTableColumn
ibmappnNodePortSIMRIM=_IbmappnNodePortSIMRIM_Object((1,3,6,1,4,1,2,6,2,13,1,4,1,1,5),_IbmappnNodePortSIMRIM_Type())
ibmappnNodePortSIMRIM.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortSIMRIM.setStatus(_A)
class _IbmappnNodePortLsRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('primary',1),('secondary',2),('negotiable',3),('abm',4)))
_IbmappnNodePortLsRole_Type.__name__=_C
_IbmappnNodePortLsRole_Object=MibTableColumn
ibmappnNodePortLsRole=_IbmappnNodePortLsRole_Object((1,3,6,1,4,1,2,6,2,13,1,4,1,1,6),_IbmappnNodePortLsRole_Type())
ibmappnNodePortLsRole.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortLsRole.setStatus(_A)
_IbmappnNodePortMaxRcvBtuSize_Type=Integer32
_IbmappnNodePortMaxRcvBtuSize_Object=MibTableColumn
ibmappnNodePortMaxRcvBtuSize=_IbmappnNodePortMaxRcvBtuSize_Object((1,3,6,1,4,1,2,6,2,13,1,4,1,1,7),_IbmappnNodePortMaxRcvBtuSize_Type())
ibmappnNodePortMaxRcvBtuSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortMaxRcvBtuSize.setStatus(_A)
_IbmappnNodePortMaxIframeWindow_Type=Integer32
_IbmappnNodePortMaxIframeWindow_Object=MibTableColumn
ibmappnNodePortMaxIframeWindow=_IbmappnNodePortMaxIframeWindow_Object((1,3,6,1,4,1,2,6,2,13,1,4,1,1,8),_IbmappnNodePortMaxIframeWindow_Type())
ibmappnNodePortMaxIframeWindow.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortMaxIframeWindow.setStatus(_A)
_IbmappnNodePortDefLsGoodXids_Type=Counter32
_IbmappnNodePortDefLsGoodXids_Object=MibTableColumn
ibmappnNodePortDefLsGoodXids=_IbmappnNodePortDefLsGoodXids_Object((1,3,6,1,4,1,2,6,2,13,1,4,1,1,9),_IbmappnNodePortDefLsGoodXids_Type())
ibmappnNodePortDefLsGoodXids.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortDefLsGoodXids.setStatus(_A)
_IbmappnNodePortDefLsBadXids_Type=Counter32
_IbmappnNodePortDefLsBadXids_Object=MibTableColumn
ibmappnNodePortDefLsBadXids=_IbmappnNodePortDefLsBadXids_Object((1,3,6,1,4,1,2,6,2,13,1,4,1,1,10),_IbmappnNodePortDefLsBadXids_Type())
ibmappnNodePortDefLsBadXids.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortDefLsBadXids.setStatus(_A)
_IbmappnNodePortDynLsGoodXids_Type=Counter32
_IbmappnNodePortDynLsGoodXids_Object=MibTableColumn
ibmappnNodePortDynLsGoodXids=_IbmappnNodePortDynLsGoodXids_Object((1,3,6,1,4,1,2,6,2,13,1,4,1,1,11),_IbmappnNodePortDynLsGoodXids_Type())
ibmappnNodePortDynLsGoodXids.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortDynLsGoodXids.setStatus(_A)
_IbmappnNodePortDynLsBadXids_Type=Counter32
_IbmappnNodePortDynLsBadXids_Object=MibTableColumn
ibmappnNodePortDynLsBadXids=_IbmappnNodePortDynLsBadXids_Object((1,3,6,1,4,1,2,6,2,13,1,4,1,1,12),_IbmappnNodePortDynLsBadXids_Type())
ibmappnNodePortDynLsBadXids.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortDynLsBadXids.setStatus(_A)
_IbmappnNodePortSpecific_Type=ObjectIdentifier
_IbmappnNodePortSpecific_Object=MibTableColumn
ibmappnNodePortSpecific=_IbmappnNodePortSpecific_Object((1,3,6,1,4,1,2,6,2,13,1,4,1,1,13),_IbmappnNodePortSpecific_Type())
ibmappnNodePortSpecific.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortSpecific.setStatus(_A)
_IbmappnNodePortIpTable_Object=MibTable
ibmappnNodePortIpTable=_IbmappnNodePortIpTable_Object((1,3,6,1,4,1,2,6,2,13,1,4,2))
if mibBuilder.loadTexts:ibmappnNodePortIpTable.setStatus(_A)
_IbmappnNodePortIpEntry_Object=MibTableRow
ibmappnNodePortIpEntry=_IbmappnNodePortIpEntry_Object((1,3,6,1,4,1,2,6,2,13,1,4,2,1))
ibmappnNodePortIpEntry.setIndexNames((0,_G,_j))
if mibBuilder.loadTexts:ibmappnNodePortIpEntry.setStatus(_A)
class _IbmappnNodePortIpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_IbmappnNodePortIpName_Type.__name__=_F
_IbmappnNodePortIpName_Object=MibTableColumn
ibmappnNodePortIpName=_IbmappnNodePortIpName_Object((1,3,6,1,4,1,2,6,2,13,1,4,2,1,1),_IbmappnNodePortIpName_Type())
ibmappnNodePortIpName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortIpName.setStatus(_A)
_IbmappnNodePortIpPortNum_Type=Integer32
_IbmappnNodePortIpPortNum_Object=MibTableColumn
ibmappnNodePortIpPortNum=_IbmappnNodePortIpPortNum_Object((1,3,6,1,4,1,2,6,2,13,1,4,2,1,2),_IbmappnNodePortIpPortNum_Type())
ibmappnNodePortIpPortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortIpPortNum.setStatus(_A)
_IbmappnNodePortDlsTable_Object=MibTable
ibmappnNodePortDlsTable=_IbmappnNodePortDlsTable_Object((1,3,6,1,4,1,2,6,2,13,1,4,3))
if mibBuilder.loadTexts:ibmappnNodePortDlsTable.setStatus(_A)
_IbmappnNodePortDlsEntry_Object=MibTableRow
ibmappnNodePortDlsEntry=_IbmappnNodePortDlsEntry_Object((1,3,6,1,4,1,2,6,2,13,1,4,3,1))
ibmappnNodePortDlsEntry.setIndexNames((0,_G,_k))
if mibBuilder.loadTexts:ibmappnNodePortDlsEntry.setStatus(_A)
class _IbmappnNodePortDlsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_IbmappnNodePortDlsName_Type.__name__=_F
_IbmappnNodePortDlsName_Object=MibTableColumn
ibmappnNodePortDlsName=_IbmappnNodePortDlsName_Object((1,3,6,1,4,1,2,6,2,13,1,4,3,1,1),_IbmappnNodePortDlsName_Type())
ibmappnNodePortDlsName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortDlsName.setStatus(_A)
class _IbmappnNodePortDlsMac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_IbmappnNodePortDlsMac_Type.__name__=_H
_IbmappnNodePortDlsMac_Object=MibTableColumn
ibmappnNodePortDlsMac=_IbmappnNodePortDlsMac_Object((1,3,6,1,4,1,2,6,2,13,1,4,3,1,2),_IbmappnNodePortDlsMac_Type())
ibmappnNodePortDlsMac.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortDlsMac.setStatus(_A)
class _IbmappnNodePortDlsSap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_IbmappnNodePortDlsSap_Type.__name__=_H
_IbmappnNodePortDlsSap_Object=MibTableColumn
ibmappnNodePortDlsSap=_IbmappnNodePortDlsSap_Object((1,3,6,1,4,1,2,6,2,13,1,4,3,1,3),_IbmappnNodePortDlsSap_Type())
ibmappnNodePortDlsSap.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortDlsSap.setStatus(_A)
_IbmappnNodePortTrTable_Object=MibTable
ibmappnNodePortTrTable=_IbmappnNodePortTrTable_Object((1,3,6,1,4,1,2,6,2,13,1,4,4))
if mibBuilder.loadTexts:ibmappnNodePortTrTable.setStatus(_A)
_IbmappnNodePortTrEntry_Object=MibTableRow
ibmappnNodePortTrEntry=_IbmappnNodePortTrEntry_Object((1,3,6,1,4,1,2,6,2,13,1,4,4,1))
ibmappnNodePortTrEntry.setIndexNames((0,_G,_l))
if mibBuilder.loadTexts:ibmappnNodePortTrEntry.setStatus(_A)
class _IbmappnNodePortTrName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_IbmappnNodePortTrName_Type.__name__=_F
_IbmappnNodePortTrName_Object=MibTableColumn
ibmappnNodePortTrName=_IbmappnNodePortTrName_Object((1,3,6,1,4,1,2,6,2,13,1,4,4,1,1),_IbmappnNodePortTrName_Type())
ibmappnNodePortTrName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortTrName.setStatus(_A)
class _IbmappnNodePortTrMac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_IbmappnNodePortTrMac_Type.__name__=_H
_IbmappnNodePortTrMac_Object=MibTableColumn
ibmappnNodePortTrMac=_IbmappnNodePortTrMac_Object((1,3,6,1,4,1,2,6,2,13,1,4,4,1,2),_IbmappnNodePortTrMac_Type())
ibmappnNodePortTrMac.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortTrMac.setStatus(_A)
class _IbmappnNodePortTrSap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_IbmappnNodePortTrSap_Type.__name__=_H
_IbmappnNodePortTrSap_Object=MibTableColumn
ibmappnNodePortTrSap=_IbmappnNodePortTrSap_Object((1,3,6,1,4,1,2,6,2,13,1,4,4,1,3),_IbmappnNodePortTrSap_Type())
ibmappnNodePortTrSap.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortTrSap.setStatus(_A)
_IbmappnNodePortDlcTraceTable_Object=MibTable
ibmappnNodePortDlcTraceTable=_IbmappnNodePortDlcTraceTable_Object((1,3,6,1,4,1,2,6,2,13,1,4,5))
if mibBuilder.loadTexts:ibmappnNodePortDlcTraceTable.setStatus(_A)
_IbmappnNodePortDlcTraceEntry_Object=MibTableRow
ibmappnNodePortDlcTraceEntry=_IbmappnNodePortDlcTraceEntry_Object((1,3,6,1,4,1,2,6,2,13,1,4,5,1))
ibmappnNodePortDlcTraceEntry.setIndexNames((0,_G,_m),(0,_G,_n))
if mibBuilder.loadTexts:ibmappnNodePortDlcTraceEntry.setStatus(_A)
_IbmappnNodePortDlcTracPortName_Type=DisplayString
_IbmappnNodePortDlcTracPortName_Object=MibTableColumn
ibmappnNodePortDlcTracPortName=_IbmappnNodePortDlcTracPortName_Object((1,3,6,1,4,1,2,6,2,13,1,4,5,1,1),_IbmappnNodePortDlcTracPortName_Type())
ibmappnNodePortDlcTracPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortDlcTracPortName.setStatus(_A)
_IbmappnNodePortDlcTracIndex_Type=Integer32
_IbmappnNodePortDlcTracIndex_Object=MibTableColumn
ibmappnNodePortDlcTracIndex=_IbmappnNodePortDlcTracIndex_Object((1,3,6,1,4,1,2,6,2,13,1,4,5,1,2),_IbmappnNodePortDlcTracIndex_Type())
ibmappnNodePortDlcTracIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortDlcTracIndex.setStatus(_A)
class _IbmappnNodePortDlcTracDlcType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_K,1),(_a,2),(_b,3),(_c,4),(_d,5),(_f,6)))
_IbmappnNodePortDlcTracDlcType_Type.__name__=_C
_IbmappnNodePortDlcTracDlcType_Object=MibTableColumn
ibmappnNodePortDlcTracDlcType=_IbmappnNodePortDlcTracDlcType_Object((1,3,6,1,4,1,2,6,2,13,1,4,5,1,3),_IbmappnNodePortDlcTracDlcType_Type())
ibmappnNodePortDlcTracDlcType.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortDlcTracDlcType.setStatus(_A)
_IbmappnNodePortDlcTracLocalAddr_Type=DisplayString
_IbmappnNodePortDlcTracLocalAddr_Object=MibTableColumn
ibmappnNodePortDlcTracLocalAddr=_IbmappnNodePortDlcTracLocalAddr_Object((1,3,6,1,4,1,2,6,2,13,1,4,5,1,4),_IbmappnNodePortDlcTracLocalAddr_Type())
ibmappnNodePortDlcTracLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortDlcTracLocalAddr.setStatus(_A)
_IbmappnNodePortDlcTracRemoteAddr_Type=DisplayString
_IbmappnNodePortDlcTracRemoteAddr_Object=MibTableColumn
ibmappnNodePortDlcTracRemoteAddr=_IbmappnNodePortDlcTracRemoteAddr_Object((1,3,6,1,4,1,2,6,2,13,1,4,5,1,5),_IbmappnNodePortDlcTracRemoteAddr_Type())
ibmappnNodePortDlcTracRemoteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortDlcTracRemoteAddr.setStatus(_A)
class _IbmappnNodePortDlcTracMsgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_K,1),('unknown',2),('request',3),('confirm',4),('indication',5),('response',6)))
_IbmappnNodePortDlcTracMsgType_Type.__name__=_C
_IbmappnNodePortDlcTracMsgType_Object=MibTableColumn
ibmappnNodePortDlcTracMsgType=_IbmappnNodePortDlcTracMsgType_Object((1,3,6,1,4,1,2,6,2,13,1,4,5,1,6),_IbmappnNodePortDlcTracMsgType_Type())
ibmappnNodePortDlcTracMsgType.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortDlcTracMsgType.setStatus(_A)
class _IbmappnNodePortDlcTracCmdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,4124,6001,6002,6003,6004,6005,6006,6007,6008,6009,6010,6012,6013,6014,6015,6016,6017,6018,6019,6020,6021,6022,6023,6024,6025,6026)));namedValues=NamedValues(*(('testFrame',1),('respFrame',2),('curFrame',3),('icrFrame',4),('respAck',5),('dgrmFrame',6),('xidFrame',7),('contFrame',8),('contedFrame',9),('iFrame',10),('enterBusy',12),('exitBusy',13),('haltFrame',14),('lsHalted',15),('restartLs',16),('lsRestarted',17),('netBioSnq',18),('netBioSnr',19),('gnetFrame',20),('netdFrame',21),('oobFrame',22),('alterSap',23),('testRsp',24),('haltLsNow',25),('testReq',26),('ipTestFrame',2001),('ipRespFrame',2002),('ipCurFrame',2003),('ipIcrFrame',2004),('ipRespAck',2005),('ipDgrmFrame',2006),('ipXidFrame',2007),('ipContFrame',2008),('ipContedFrame',2009),('ipIFrame',2010),('ipEnterBusy',2012),('ipExitBusy',2013),('ipHaltFrame',2014),('ipLsHalted',2015),('ipRestartLs',2016),('ipLsRestarted',2017),('ipNetBioSnq',2018),('ipNetBioSnr',2019),('ipGnetFrame',2020),('ipNetdFrame',2021),('ipOobFrame',2022),('ipAlterSap',2023),('ipTestRsp',2024),('ipHaltLsNow',2025),('ipTestReq',2026),('dlsIpm',4124),('trTestFrame',6001),('trRespFrame',6002),('trCurFrame',6003),('trIcrFrame',6004),('trRespAck',6005),('trDgrmFrame',6006),('trXidFrame',6007),('trContFrame',6008),('trContedFrame',6009),('trIFrame',6010),('trEnterBusy',6012),('trExitBusy',6013),('trHaltFrame',6014),('trLsHalted',6015),('trRestartLs',6016),('trLsRestarted',6017),('trNetBioSnq',6018),('trNetBioSnr',6019),('trGnetFrame',6020),('trNetdFrame',6021),('trOobFrame',6022),('trAlterSap',6023),('trTestRsp',6024),('trHaltLsNow',6025),('trTestReq',6026)))
_IbmappnNodePortDlcTracCmdType_Type.__name__=_C
_IbmappnNodePortDlcTracCmdType_Object=MibTableColumn
ibmappnNodePortDlcTracCmdType=_IbmappnNodePortDlcTracCmdType_Object((1,3,6,1,4,1,2,6,2,13,1,4,5,1,7),_IbmappnNodePortDlcTracCmdType_Type())
ibmappnNodePortDlcTracCmdType.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortDlcTracCmdType.setStatus(_A)
class _IbmappnNodePortDlcTracUseWan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_K,1),('notApplicable',2),('useUnknown',3),('useWan',4),('useLan',5)))
_IbmappnNodePortDlcTracUseWan_Type.__name__=_C
_IbmappnNodePortDlcTracUseWan_Object=MibTableColumn
ibmappnNodePortDlcTracUseWan=_IbmappnNodePortDlcTracUseWan_Object((1,3,6,1,4,1,2,6,2,13,1,4,5,1,8),_IbmappnNodePortDlcTracUseWan_Type())
ibmappnNodePortDlcTracUseWan.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodePortDlcTracUseWan.setStatus(_A)
_IbmappnLinkStationInformation_ObjectIdentity=ObjectIdentity
ibmappnLinkStationInformation=_IbmappnLinkStationInformation_ObjectIdentity((1,3,6,1,4,1,2,6,2,13,1,5))
_IbmappnNodeLsTable_Object=MibTable
ibmappnNodeLsTable=_IbmappnNodeLsTable_Object((1,3,6,1,4,1,2,6,2,13,1,5,1))
if mibBuilder.loadTexts:ibmappnNodeLsTable.setStatus(_A)
_IbmappnNodeLsEntry_Object=MibTableRow
ibmappnNodeLsEntry=_IbmappnNodeLsEntry_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1))
ibmappnNodeLsEntry.setIndexNames((0,_G,_o))
if mibBuilder.loadTexts:ibmappnNodeLsEntry.setStatus(_A)
class _IbmappnNodeLsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_IbmappnNodeLsName_Type.__name__=_F
_IbmappnNodeLsName_Object=MibTableColumn
ibmappnNodeLsName=_IbmappnNodeLsName_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,1),_IbmappnNodeLsName_Type())
ibmappnNodeLsName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsName.setStatus(_A)
class _IbmappnNodeLsPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_IbmappnNodeLsPortName_Type.__name__=_F
_IbmappnNodeLsPortName_Object=MibTableColumn
ibmappnNodeLsPortName=_IbmappnNodeLsPortName_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,2),_IbmappnNodeLsPortName_Type())
ibmappnNodeLsPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsPortName.setStatus(_A)
class _IbmappnNodeLsDlcType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_K,1),(_a,2),(_b,3),(_c,4),(_d,5),(_f,6)))
_IbmappnNodeLsDlcType_Type.__name__=_C
_IbmappnNodeLsDlcType_Object=MibTableColumn
ibmappnNodeLsDlcType=_IbmappnNodeLsDlcType_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,3),_IbmappnNodeLsDlcType_Type())
ibmappnNodeLsDlcType.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsDlcType.setStatus(_A)
class _IbmappnNodeLsDynamic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNodeLsDynamic_Type.__name__=_C
_IbmappnNodeLsDynamic_Object=MibTableColumn
ibmappnNodeLsDynamic=_IbmappnNodeLsDynamic_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,4),_IbmappnNodeLsDynamic_Type())
ibmappnNodeLsDynamic.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsDynamic.setStatus(_A)
class _IbmappnNodeLsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_Y,2),(_J,3),(_Z,4)))
_IbmappnNodeLsState_Type.__name__=_C
_IbmappnNodeLsState_Object=MibTableColumn
ibmappnNodeLsState=_IbmappnNodeLsState_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,5),_IbmappnNodeLsState_Type())
ibmappnNodeLsState.setMaxAccess(_i)
if mibBuilder.loadTexts:ibmappnNodeLsState.setStatus(_A)
class _IbmappnNodeLsCpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_IbmappnNodeLsCpName_Type.__name__=_F
_IbmappnNodeLsCpName_Object=MibTableColumn
ibmappnNodeLsCpName=_IbmappnNodeLsCpName_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,6),_IbmappnNodeLsCpName_Type())
ibmappnNodeLsCpName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsCpName.setStatus(_A)
_IbmappnNodeLsTgNum_Type=Integer32
_IbmappnNodeLsTgNum_Object=MibTableColumn
ibmappnNodeLsTgNum=_IbmappnNodeLsTgNum_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,7),_IbmappnNodeLsTgNum_Type())
ibmappnNodeLsTgNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsTgNum.setStatus(_A)
class _IbmappnNodeLsLimResource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNodeLsLimResource_Type.__name__=_C
_IbmappnNodeLsLimResource_Object=MibTableColumn
ibmappnNodeLsLimResource=_IbmappnNodeLsLimResource_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,8),_IbmappnNodeLsLimResource_Type())
ibmappnNodeLsLimResource.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsLimResource.setStatus(_A)
class _IbmappnNodeLsMigration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNodeLsMigration_Type.__name__=_C
_IbmappnNodeLsMigration_Object=MibTableColumn
ibmappnNodeLsMigration=_IbmappnNodeLsMigration_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,9),_IbmappnNodeLsMigration_Type())
ibmappnNodeLsMigration.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsMigration.setStatus(_A)
class _IbmappnNodeLsBlockNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_IbmappnNodeLsBlockNum_Type.__name__=_F
_IbmappnNodeLsBlockNum_Object=MibTableColumn
ibmappnNodeLsBlockNum=_IbmappnNodeLsBlockNum_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,10),_IbmappnNodeLsBlockNum_Type())
ibmappnNodeLsBlockNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsBlockNum.setStatus(_A)
class _IbmappnNodeLsIdNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_IbmappnNodeLsIdNum_Type.__name__=_F
_IbmappnNodeLsIdNum_Object=MibTableColumn
ibmappnNodeLsIdNum=_IbmappnNodeLsIdNum_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,11),_IbmappnNodeLsIdNum_Type())
ibmappnNodeLsIdNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsIdNum.setStatus(_A)
class _IbmappnNodeLsCpCpSession_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNodeLsCpCpSession_Type.__name__=_C
_IbmappnNodeLsCpCpSession_Object=MibTableColumn
ibmappnNodeLsCpCpSession=_IbmappnNodeLsCpCpSession_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,12),_IbmappnNodeLsCpCpSession_Type())
ibmappnNodeLsCpCpSession.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsCpCpSession.setStatus(_A)
_IbmappnNodeLsTargetPacingCount_Type=Integer32
_IbmappnNodeLsTargetPacingCount_Object=MibTableColumn
ibmappnNodeLsTargetPacingCount=_IbmappnNodeLsTargetPacingCount_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,13),_IbmappnNodeLsTargetPacingCount_Type())
ibmappnNodeLsTargetPacingCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsTargetPacingCount.setStatus(_A)
_IbmappnNodeLsMaxSendBtuSize_Type=Integer32
_IbmappnNodeLsMaxSendBtuSize_Object=MibTableColumn
ibmappnNodeLsMaxSendBtuSize=_IbmappnNodeLsMaxSendBtuSize_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,14),_IbmappnNodeLsMaxSendBtuSize_Type())
ibmappnNodeLsMaxSendBtuSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsMaxSendBtuSize.setStatus(_A)
_IbmappnNodeLsEffCap_Type=Integer32
_IbmappnNodeLsEffCap_Object=MibTableColumn
ibmappnNodeLsEffCap=_IbmappnNodeLsEffCap_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,15),_IbmappnNodeLsEffCap_Type())
ibmappnNodeLsEffCap.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsEffCap.setStatus(_A)
class _IbmappnNodeLsConnCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnNodeLsConnCost_Type.__name__=_C
_IbmappnNodeLsConnCost_Object=MibTableColumn
ibmappnNodeLsConnCost=_IbmappnNodeLsConnCost_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,16),_IbmappnNodeLsConnCost_Type())
ibmappnNodeLsConnCost.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsConnCost.setStatus(_A)
class _IbmappnNodeLsByteCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnNodeLsByteCost_Type.__name__=_C
_IbmappnNodeLsByteCost_Object=MibTableColumn
ibmappnNodeLsByteCost=_IbmappnNodeLsByteCost_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,17),_IbmappnNodeLsByteCost_Type())
ibmappnNodeLsByteCost.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsByteCost.setStatus(_A)
class _IbmappnNodeLsSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,32,64,96,128,160,192)));namedValues=NamedValues(*((_L,1),(_M,32),(_N,64),(_O,96),(_P,128),(_Q,160),(_R,192)))
_IbmappnNodeLsSecurity_Type.__name__=_C
_IbmappnNodeLsSecurity_Object=MibTableColumn
ibmappnNodeLsSecurity=_IbmappnNodeLsSecurity_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,18),_IbmappnNodeLsSecurity_Type())
ibmappnNodeLsSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsSecurity.setStatus(_A)
class _IbmappnNodeLsDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,384,9216,147456,294912,2013265920)));namedValues=NamedValues(*((_S,0),(_T,384),(_U,9216),(_V,147456),(_W,294912),(_X,2013265920)))
_IbmappnNodeLsDelay_Type.__name__=_C
_IbmappnNodeLsDelay_Object=MibTableColumn
ibmappnNodeLsDelay=_IbmappnNodeLsDelay_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,19),_IbmappnNodeLsDelay_Type())
ibmappnNodeLsDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsDelay.setStatus(_A)
class _IbmappnNodeLsUsr1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnNodeLsUsr1_Type.__name__=_C
_IbmappnNodeLsUsr1_Object=MibTableColumn
ibmappnNodeLsUsr1=_IbmappnNodeLsUsr1_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,20),_IbmappnNodeLsUsr1_Type())
ibmappnNodeLsUsr1.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsUsr1.setStatus(_A)
class _IbmappnNodeLsUsr2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnNodeLsUsr2_Type.__name__=_C
_IbmappnNodeLsUsr2_Object=MibTableColumn
ibmappnNodeLsUsr2=_IbmappnNodeLsUsr2_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,21),_IbmappnNodeLsUsr2_Type())
ibmappnNodeLsUsr2.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsUsr2.setStatus(_A)
class _IbmappnNodeLsUsr3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnNodeLsUsr3_Type.__name__=_C
_IbmappnNodeLsUsr3_Object=MibTableColumn
ibmappnNodeLsUsr3=_IbmappnNodeLsUsr3_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,22),_IbmappnNodeLsUsr3_Type())
ibmappnNodeLsUsr3.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsUsr3.setStatus(_A)
_IbmappnNodeLsInXidBytes_Type=Counter32
_IbmappnNodeLsInXidBytes_Object=MibTableColumn
ibmappnNodeLsInXidBytes=_IbmappnNodeLsInXidBytes_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,23),_IbmappnNodeLsInXidBytes_Type())
ibmappnNodeLsInXidBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsInXidBytes.setStatus(_A)
_IbmappnNodeLsInMsgBytes_Type=Counter32
_IbmappnNodeLsInMsgBytes_Object=MibTableColumn
ibmappnNodeLsInMsgBytes=_IbmappnNodeLsInMsgBytes_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,24),_IbmappnNodeLsInMsgBytes_Type())
ibmappnNodeLsInMsgBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsInMsgBytes.setStatus(_A)
_IbmappnNodeLsInXidFrames_Type=Counter32
_IbmappnNodeLsInXidFrames_Object=MibTableColumn
ibmappnNodeLsInXidFrames=_IbmappnNodeLsInXidFrames_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,25),_IbmappnNodeLsInXidFrames_Type())
ibmappnNodeLsInXidFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsInXidFrames.setStatus(_A)
_IbmappnNodeLsInMsgFrames_Type=Counter32
_IbmappnNodeLsInMsgFrames_Object=MibTableColumn
ibmappnNodeLsInMsgFrames=_IbmappnNodeLsInMsgFrames_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,26),_IbmappnNodeLsInMsgFrames_Type())
ibmappnNodeLsInMsgFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsInMsgFrames.setStatus(_A)
_IbmappnNodeLsOutXidBytes_Type=Counter32
_IbmappnNodeLsOutXidBytes_Object=MibTableColumn
ibmappnNodeLsOutXidBytes=_IbmappnNodeLsOutXidBytes_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,27),_IbmappnNodeLsOutXidBytes_Type())
ibmappnNodeLsOutXidBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsOutXidBytes.setStatus(_A)
_IbmappnNodeLsOutMsgBytes_Type=Counter32
_IbmappnNodeLsOutMsgBytes_Object=MibTableColumn
ibmappnNodeLsOutMsgBytes=_IbmappnNodeLsOutMsgBytes_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,28),_IbmappnNodeLsOutMsgBytes_Type())
ibmappnNodeLsOutMsgBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsOutMsgBytes.setStatus(_A)
_IbmappnNodeLsOutXidFrames_Type=Counter32
_IbmappnNodeLsOutXidFrames_Object=MibTableColumn
ibmappnNodeLsOutXidFrames=_IbmappnNodeLsOutXidFrames_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,29),_IbmappnNodeLsOutXidFrames_Type())
ibmappnNodeLsOutXidFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsOutXidFrames.setStatus(_A)
_IbmappnNodeLsOutMsgFrames_Type=Counter32
_IbmappnNodeLsOutMsgFrames_Object=MibTableColumn
ibmappnNodeLsOutMsgFrames=_IbmappnNodeLsOutMsgFrames_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,30),_IbmappnNodeLsOutMsgFrames_Type())
ibmappnNodeLsOutMsgFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsOutMsgFrames.setStatus(_A)
_IbmappnNodeLsEchoRsps_Type=Counter32
_IbmappnNodeLsEchoRsps_Object=MibTableColumn
ibmappnNodeLsEchoRsps=_IbmappnNodeLsEchoRsps_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,31),_IbmappnNodeLsEchoRsps_Type())
ibmappnNodeLsEchoRsps.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsEchoRsps.setStatus(_A)
_IbmappnNodeLsCurrentDelay_Type=Integer32
_IbmappnNodeLsCurrentDelay_Object=MibTableColumn
ibmappnNodeLsCurrentDelay=_IbmappnNodeLsCurrentDelay_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,32),_IbmappnNodeLsCurrentDelay_Type())
ibmappnNodeLsCurrentDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsCurrentDelay.setStatus(_A)
_IbmappnNodeLsMaxDelay_Type=Integer32
_IbmappnNodeLsMaxDelay_Object=MibTableColumn
ibmappnNodeLsMaxDelay=_IbmappnNodeLsMaxDelay_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,33),_IbmappnNodeLsMaxDelay_Type())
ibmappnNodeLsMaxDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsMaxDelay.setStatus(_A)
_IbmappnNodeLsMinDelay_Type=Integer32
_IbmappnNodeLsMinDelay_Object=MibTableColumn
ibmappnNodeLsMinDelay=_IbmappnNodeLsMinDelay_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,34),_IbmappnNodeLsMinDelay_Type())
ibmappnNodeLsMinDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsMinDelay.setStatus(_A)
_IbmappnNodeLsMaxDelayTime_Type=TimeTicks
_IbmappnNodeLsMaxDelayTime_Object=MibTableColumn
ibmappnNodeLsMaxDelayTime=_IbmappnNodeLsMaxDelayTime_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,35),_IbmappnNodeLsMaxDelayTime_Type())
ibmappnNodeLsMaxDelayTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsMaxDelayTime.setStatus(_A)
_IbmappnNodeLsGoodXids_Type=Counter32
_IbmappnNodeLsGoodXids_Object=MibTableColumn
ibmappnNodeLsGoodXids=_IbmappnNodeLsGoodXids_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,36),_IbmappnNodeLsGoodXids_Type())
ibmappnNodeLsGoodXids.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsGoodXids.setStatus(_A)
_IbmappnNodeLsBadXids_Type=Counter32
_IbmappnNodeLsBadXids_Object=MibTableColumn
ibmappnNodeLsBadXids=_IbmappnNodeLsBadXids_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,37),_IbmappnNodeLsBadXids_Type())
ibmappnNodeLsBadXids.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsBadXids.setStatus(_A)
_IbmappnNodeLsSpecific_Type=ObjectIdentifier
_IbmappnNodeLsSpecific_Object=MibTableColumn
ibmappnNodeLsSpecific=_IbmappnNodeLsSpecific_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,38),_IbmappnNodeLsSpecific_Type())
ibmappnNodeLsSpecific.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsSpecific.setStatus(_A)
class _IbmappnNodeLsSubState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_I,1),('sentReqOpnstn',2),('pendXidExch',3),('sentActAs',4),('sentSetMode',5),(_J,6),('sentDeactAsOrd',7),('sentDiscOrd',8),('sentDestroyTg',9),('sentCreateTg',10),('sentConnReq',11),('pendRcvConnInd',12),('pendSendConnRsp',13),('sentConnRsp',14),('pendDeact',15)))
_IbmappnNodeLsSubState_Type.__name__=_C
_IbmappnNodeLsSubState_Object=MibTableColumn
ibmappnNodeLsSubState=_IbmappnNodeLsSubState_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,39),_IbmappnNodeLsSubState_Type())
ibmappnNodeLsSubState.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsSubState.setStatus(_A)
_IbmappnNodeLsStartTime_Type=TimeTicks
_IbmappnNodeLsStartTime_Object=MibTableColumn
ibmappnNodeLsStartTime=_IbmappnNodeLsStartTime_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,40),_IbmappnNodeLsStartTime_Type())
ibmappnNodeLsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsStartTime.setStatus(_A)
_IbmappnNodeLsActiveTime_Type=TimeTicks
_IbmappnNodeLsActiveTime_Object=MibTableColumn
ibmappnNodeLsActiveTime=_IbmappnNodeLsActiveTime_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,41),_IbmappnNodeLsActiveTime_Type())
ibmappnNodeLsActiveTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsActiveTime.setStatus(_A)
_IbmappnNodeLsCurrentStateTime_Type=TimeTicks
_IbmappnNodeLsCurrentStateTime_Object=MibTableColumn
ibmappnNodeLsCurrentStateTime=_IbmappnNodeLsCurrentStateTime_Object((1,3,6,1,4,1,2,6,2,13,1,5,1,1,42),_IbmappnNodeLsCurrentStateTime_Type())
ibmappnNodeLsCurrentStateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsCurrentStateTime.setStatus(_A)
_IbmappnNodeLsIpTable_Object=MibTable
ibmappnNodeLsIpTable=_IbmappnNodeLsIpTable_Object((1,3,6,1,4,1,2,6,2,13,1,5,2))
if mibBuilder.loadTexts:ibmappnNodeLsIpTable.setStatus(_A)
_IbmappnNodeLsIpEntry_Object=MibTableRow
ibmappnNodeLsIpEntry=_IbmappnNodeLsIpEntry_Object((1,3,6,1,4,1,2,6,2,13,1,5,2,1))
ibmappnNodeLsIpEntry.setIndexNames((0,_G,_p))
if mibBuilder.loadTexts:ibmappnNodeLsIpEntry.setStatus(_A)
class _IbmappnNodeLsIpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_IbmappnNodeLsIpName_Type.__name__=_F
_IbmappnNodeLsIpName_Object=MibTableColumn
ibmappnNodeLsIpName=_IbmappnNodeLsIpName_Object((1,3,6,1,4,1,2,6,2,13,1,5,2,1,1),_IbmappnNodeLsIpName_Type())
ibmappnNodeLsIpName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsIpName.setStatus(_A)
class _IbmappnNodeLsIpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_Y,2),(_J,3),(_Z,4)))
_IbmappnNodeLsIpState_Type.__name__=_C
_IbmappnNodeLsIpState_Object=MibTableColumn
ibmappnNodeLsIpState=_IbmappnNodeLsIpState_Object((1,3,6,1,4,1,2,6,2,13,1,5,2,1,2),_IbmappnNodeLsIpState_Type())
ibmappnNodeLsIpState.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsIpState.setStatus(_A)
_IbmappnNodeLsLocalIpAddr_Type=IpAddress
_IbmappnNodeLsLocalIpAddr_Object=MibTableColumn
ibmappnNodeLsLocalIpAddr=_IbmappnNodeLsLocalIpAddr_Object((1,3,6,1,4,1,2,6,2,13,1,5,2,1,3),_IbmappnNodeLsLocalIpAddr_Type())
ibmappnNodeLsLocalIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsLocalIpAddr.setStatus(_A)
_IbmappnNodeLsLocalIpPortNum_Type=Integer32
_IbmappnNodeLsLocalIpPortNum_Object=MibTableColumn
ibmappnNodeLsLocalIpPortNum=_IbmappnNodeLsLocalIpPortNum_Object((1,3,6,1,4,1,2,6,2,13,1,5,2,1,4),_IbmappnNodeLsLocalIpPortNum_Type())
ibmappnNodeLsLocalIpPortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsLocalIpPortNum.setStatus(_A)
_IbmappnNodeLsRemoteIpAddr_Type=IpAddress
_IbmappnNodeLsRemoteIpAddr_Object=MibTableColumn
ibmappnNodeLsRemoteIpAddr=_IbmappnNodeLsRemoteIpAddr_Object((1,3,6,1,4,1,2,6,2,13,1,5,2,1,5),_IbmappnNodeLsRemoteIpAddr_Type())
ibmappnNodeLsRemoteIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsRemoteIpAddr.setStatus(_A)
_IbmappnNodeLsRemoteIpPortNum_Type=Integer32
_IbmappnNodeLsRemoteIpPortNum_Object=MibTableColumn
ibmappnNodeLsRemoteIpPortNum=_IbmappnNodeLsRemoteIpPortNum_Object((1,3,6,1,4,1,2,6,2,13,1,5,2,1,6),_IbmappnNodeLsRemoteIpPortNum_Type())
ibmappnNodeLsRemoteIpPortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsRemoteIpPortNum.setStatus(_A)
_IbmappnNodeLsDlsTable_Object=MibTable
ibmappnNodeLsDlsTable=_IbmappnNodeLsDlsTable_Object((1,3,6,1,4,1,2,6,2,13,1,5,3))
if mibBuilder.loadTexts:ibmappnNodeLsDlsTable.setStatus(_A)
_IbmappnNodeLsDlsEntry_Object=MibTableRow
ibmappnNodeLsDlsEntry=_IbmappnNodeLsDlsEntry_Object((1,3,6,1,4,1,2,6,2,13,1,5,3,1))
ibmappnNodeLsDlsEntry.setIndexNames((0,_G,_q))
if mibBuilder.loadTexts:ibmappnNodeLsDlsEntry.setStatus(_A)
class _IbmappnNodeLsDlsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_IbmappnNodeLsDlsName_Type.__name__=_F
_IbmappnNodeLsDlsName_Object=MibTableColumn
ibmappnNodeLsDlsName=_IbmappnNodeLsDlsName_Object((1,3,6,1,4,1,2,6,2,13,1,5,3,1,1),_IbmappnNodeLsDlsName_Type())
ibmappnNodeLsDlsName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsDlsName.setStatus(_A)
class _IbmappnNodeLsDlsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_Y,2),(_J,3),(_Z,4)))
_IbmappnNodeLsDlsState_Type.__name__=_C
_IbmappnNodeLsDlsState_Object=MibTableColumn
ibmappnNodeLsDlsState=_IbmappnNodeLsDlsState_Object((1,3,6,1,4,1,2,6,2,13,1,5,3,1,2),_IbmappnNodeLsDlsState_Type())
ibmappnNodeLsDlsState.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsDlsState.setStatus(_A)
class _IbmappnNodeLsLocalDlsMac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_IbmappnNodeLsLocalDlsMac_Type.__name__=_H
_IbmappnNodeLsLocalDlsMac_Object=MibTableColumn
ibmappnNodeLsLocalDlsMac=_IbmappnNodeLsLocalDlsMac_Object((1,3,6,1,4,1,2,6,2,13,1,5,3,1,3),_IbmappnNodeLsLocalDlsMac_Type())
ibmappnNodeLsLocalDlsMac.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsLocalDlsMac.setStatus(_A)
class _IbmappnNodeLsLocalDlsSap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_IbmappnNodeLsLocalDlsSap_Type.__name__=_H
_IbmappnNodeLsLocalDlsSap_Object=MibTableColumn
ibmappnNodeLsLocalDlsSap=_IbmappnNodeLsLocalDlsSap_Object((1,3,6,1,4,1,2,6,2,13,1,5,3,1,4),_IbmappnNodeLsLocalDlsSap_Type())
ibmappnNodeLsLocalDlsSap.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsLocalDlsSap.setStatus(_A)
class _IbmappnNodeLsRemoteDlsMac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_IbmappnNodeLsRemoteDlsMac_Type.__name__=_H
_IbmappnNodeLsRemoteDlsMac_Object=MibTableColumn
ibmappnNodeLsRemoteDlsMac=_IbmappnNodeLsRemoteDlsMac_Object((1,3,6,1,4,1,2,6,2,13,1,5,3,1,5),_IbmappnNodeLsRemoteDlsMac_Type())
ibmappnNodeLsRemoteDlsMac.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsRemoteDlsMac.setStatus(_A)
class _IbmappnNodeLsRemoteDlsSap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_IbmappnNodeLsRemoteDlsSap_Type.__name__=_H
_IbmappnNodeLsRemoteDlsSap_Object=MibTableColumn
ibmappnNodeLsRemoteDlsSap=_IbmappnNodeLsRemoteDlsSap_Object((1,3,6,1,4,1,2,6,2,13,1,5,3,1,6),_IbmappnNodeLsRemoteDlsSap_Type())
ibmappnNodeLsRemoteDlsSap.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsRemoteDlsSap.setStatus(_A)
_IbmappnNodeLsTrTable_Object=MibTable
ibmappnNodeLsTrTable=_IbmappnNodeLsTrTable_Object((1,3,6,1,4,1,2,6,2,13,1,5,4))
if mibBuilder.loadTexts:ibmappnNodeLsTrTable.setStatus(_A)
_IbmappnNodeLsTrEntry_Object=MibTableRow
ibmappnNodeLsTrEntry=_IbmappnNodeLsTrEntry_Object((1,3,6,1,4,1,2,6,2,13,1,5,4,1))
ibmappnNodeLsTrEntry.setIndexNames((0,_G,_r))
if mibBuilder.loadTexts:ibmappnNodeLsTrEntry.setStatus(_A)
class _IbmappnNodeLsTrName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_IbmappnNodeLsTrName_Type.__name__=_F
_IbmappnNodeLsTrName_Object=MibTableColumn
ibmappnNodeLsTrName=_IbmappnNodeLsTrName_Object((1,3,6,1,4,1,2,6,2,13,1,5,4,1,1),_IbmappnNodeLsTrName_Type())
ibmappnNodeLsTrName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsTrName.setStatus(_A)
class _IbmappnNodeLsTrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_Y,2),(_J,3),(_Z,4)))
_IbmappnNodeLsTrState_Type.__name__=_C
_IbmappnNodeLsTrState_Object=MibTableColumn
ibmappnNodeLsTrState=_IbmappnNodeLsTrState_Object((1,3,6,1,4,1,2,6,2,13,1,5,4,1,2),_IbmappnNodeLsTrState_Type())
ibmappnNodeLsTrState.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsTrState.setStatus(_A)
class _IbmappnNodeLsLocalTrMac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_IbmappnNodeLsLocalTrMac_Type.__name__=_H
_IbmappnNodeLsLocalTrMac_Object=MibTableColumn
ibmappnNodeLsLocalTrMac=_IbmappnNodeLsLocalTrMac_Object((1,3,6,1,4,1,2,6,2,13,1,5,4,1,3),_IbmappnNodeLsLocalTrMac_Type())
ibmappnNodeLsLocalTrMac.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsLocalTrMac.setStatus(_A)
class _IbmappnNodeLsLocalTrSap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_IbmappnNodeLsLocalTrSap_Type.__name__=_H
_IbmappnNodeLsLocalTrSap_Object=MibTableColumn
ibmappnNodeLsLocalTrSap=_IbmappnNodeLsLocalTrSap_Object((1,3,6,1,4,1,2,6,2,13,1,5,4,1,4),_IbmappnNodeLsLocalTrSap_Type())
ibmappnNodeLsLocalTrSap.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsLocalTrSap.setStatus(_A)
class _IbmappnNodeLsRemoteTrMac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_IbmappnNodeLsRemoteTrMac_Type.__name__=_H
_IbmappnNodeLsRemoteTrMac_Object=MibTableColumn
ibmappnNodeLsRemoteTrMac=_IbmappnNodeLsRemoteTrMac_Object((1,3,6,1,4,1,2,6,2,13,1,5,4,1,5),_IbmappnNodeLsRemoteTrMac_Type())
ibmappnNodeLsRemoteTrMac.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsRemoteTrMac.setStatus(_A)
class _IbmappnNodeLsRemoteTrSap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_IbmappnNodeLsRemoteTrSap_Type.__name__=_H
_IbmappnNodeLsRemoteTrSap_Object=MibTableColumn
ibmappnNodeLsRemoteTrSap=_IbmappnNodeLsRemoteTrSap_Object((1,3,6,1,4,1,2,6,2,13,1,5,4,1,6),_IbmappnNodeLsRemoteTrSap_Type())
ibmappnNodeLsRemoteTrSap.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsRemoteTrSap.setStatus(_A)
_IbmappnNodeLsStatusTable_Object=MibTable
ibmappnNodeLsStatusTable=_IbmappnNodeLsStatusTable_Object((1,3,6,1,4,1,2,6,2,13,1,5,5))
if mibBuilder.loadTexts:ibmappnNodeLsStatusTable.setStatus(_A)
_IbmappnNodeLsStatusEntry_Object=MibTableRow
ibmappnNodeLsStatusEntry=_IbmappnNodeLsStatusEntry_Object((1,3,6,1,4,1,2,6,2,13,1,5,5,1))
ibmappnNodeLsStatusEntry.setIndexNames((0,_G,_s))
if mibBuilder.loadTexts:ibmappnNodeLsStatusEntry.setStatus(_A)
_IbmappnNodeLsStatusIndex_Type=Integer32
_IbmappnNodeLsStatusIndex_Object=MibTableColumn
ibmappnNodeLsStatusIndex=_IbmappnNodeLsStatusIndex_Object((1,3,6,1,4,1,2,6,2,13,1,5,5,1,1),_IbmappnNodeLsStatusIndex_Type())
ibmappnNodeLsStatusIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsStatusIndex.setStatus(_A)
_IbmappnNodeLsStatusTime_Type=TimeTicks
_IbmappnNodeLsStatusTime_Object=MibTableColumn
ibmappnNodeLsStatusTime=_IbmappnNodeLsStatusTime_Object((1,3,6,1,4,1,2,6,2,13,1,5,5,1,2),_IbmappnNodeLsStatusTime_Type())
ibmappnNodeLsStatusTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsStatusTime.setStatus(_A)
class _IbmappnNodeLsStatusLsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_IbmappnNodeLsStatusLsName_Type.__name__=_F
_IbmappnNodeLsStatusLsName_Object=MibTableColumn
ibmappnNodeLsStatusLsName=_IbmappnNodeLsStatusLsName_Object((1,3,6,1,4,1,2,6,2,13,1,5,5,1,3),_IbmappnNodeLsStatusLsName_Type())
ibmappnNodeLsStatusLsName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsStatusLsName.setStatus(_A)
class _IbmappnNodeLsStatusCpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_IbmappnNodeLsStatusCpName_Type.__name__=_F
_IbmappnNodeLsStatusCpName_Object=MibTableColumn
ibmappnNodeLsStatusCpName=_IbmappnNodeLsStatusCpName_Object((1,3,6,1,4,1,2,6,2,13,1,5,5,1,4),_IbmappnNodeLsStatusCpName_Type())
ibmappnNodeLsStatusCpName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsStatusCpName.setStatus(_A)
_IbmappnNodeLsStatusNodeId_Type=OctetString
_IbmappnNodeLsStatusNodeId_Object=MibTableColumn
ibmappnNodeLsStatusNodeId=_IbmappnNodeLsStatusNodeId_Object((1,3,6,1,4,1,2,6,2,13,1,5,5,1,5),_IbmappnNodeLsStatusNodeId_Type())
ibmappnNodeLsStatusNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsStatusNodeId.setStatus(_A)
class _IbmappnNodeLsStatusTgNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_IbmappnNodeLsStatusTgNum_Type.__name__=_C
_IbmappnNodeLsStatusTgNum_Object=MibTableColumn
ibmappnNodeLsStatusTgNum=_IbmappnNodeLsStatusTgNum_Object((1,3,6,1,4,1,2,6,2,13,1,5,5,1,6),_IbmappnNodeLsStatusTgNum_Type())
ibmappnNodeLsStatusTgNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsStatusTgNum.setStatus(_A)
_IbmappnNodeLsStatusGeneralSense_Type=OctetString
_IbmappnNodeLsStatusGeneralSense_Object=MibTableColumn
ibmappnNodeLsStatusGeneralSense=_IbmappnNodeLsStatusGeneralSense_Object((1,3,6,1,4,1,2,6,2,13,1,5,5,1,7),_IbmappnNodeLsStatusGeneralSense_Type())
ibmappnNodeLsStatusGeneralSense.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsStatusGeneralSense.setStatus(_A)
class _IbmappnNodeLsStatusNofRetry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('retry',1),('noretry',2)))
_IbmappnNodeLsStatusNofRetry_Type.__name__=_C
_IbmappnNodeLsStatusNofRetry_Object=MibTableColumn
ibmappnNodeLsStatusNofRetry=_IbmappnNodeLsStatusNofRetry_Object((1,3,6,1,4,1,2,6,2,13,1,5,5,1,8),_IbmappnNodeLsStatusNofRetry_Type())
ibmappnNodeLsStatusNofRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsStatusNofRetry.setStatus(_A)
_IbmappnNodeLsStatusEndSense_Type=OctetString
_IbmappnNodeLsStatusEndSense_Object=MibTableColumn
ibmappnNodeLsStatusEndSense=_IbmappnNodeLsStatusEndSense_Object((1,3,6,1,4,1,2,6,2,13,1,5,5,1,9),_IbmappnNodeLsStatusEndSense_Type())
ibmappnNodeLsStatusEndSense.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsStatusEndSense.setStatus(_A)
_IbmappnNodeLsStatusXidLocalSense_Type=OctetString
_IbmappnNodeLsStatusXidLocalSense_Object=MibTableColumn
ibmappnNodeLsStatusXidLocalSense=_IbmappnNodeLsStatusXidLocalSense_Object((1,3,6,1,4,1,2,6,2,13,1,5,5,1,10),_IbmappnNodeLsStatusXidLocalSense_Type())
ibmappnNodeLsStatusXidLocalSense.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsStatusXidLocalSense.setStatus(_A)
_IbmappnNodeLsStatusXidRemoteSense_Type=OctetString
_IbmappnNodeLsStatusXidRemoteSense_Object=MibTableColumn
ibmappnNodeLsStatusXidRemoteSense=_IbmappnNodeLsStatusXidRemoteSense_Object((1,3,6,1,4,1,2,6,2,13,1,5,5,1,11),_IbmappnNodeLsStatusXidRemoteSense_Type())
ibmappnNodeLsStatusXidRemoteSense.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsStatusXidRemoteSense.setStatus(_A)
class _IbmappnNodeLsStatusXidByteInError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1000));namedValues=NamedValues(('na',1000))
_IbmappnNodeLsStatusXidByteInError_Type.__name__=_C
_IbmappnNodeLsStatusXidByteInError_Object=MibTableColumn
ibmappnNodeLsStatusXidByteInError=_IbmappnNodeLsStatusXidByteInError_Object((1,3,6,1,4,1,2,6,2,13,1,5,5,1,12),_IbmappnNodeLsStatusXidByteInError_Type())
ibmappnNodeLsStatusXidByteInError.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsStatusXidByteInError.setStatus(_A)
class _IbmappnNodeLsStatusXidBitInError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(8));namedValues=NamedValues(('na',8))
_IbmappnNodeLsStatusXidBitInError_Type.__name__=_C
_IbmappnNodeLsStatusXidBitInError_Object=MibTableColumn
ibmappnNodeLsStatusXidBitInError=_IbmappnNodeLsStatusXidBitInError_Object((1,3,6,1,4,1,2,6,2,13,1,5,5,1,13),_IbmappnNodeLsStatusXidBitInError_Type())
ibmappnNodeLsStatusXidBitInError.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsStatusXidBitInError.setStatus(_A)
class _IbmappnNodeLsStatusDlcType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_K,1),(_a,2),(_b,3),(_c,4),(_d,5),('tr',6)))
_IbmappnNodeLsStatusDlcType_Type.__name__=_C
_IbmappnNodeLsStatusDlcType_Object=MibTableColumn
ibmappnNodeLsStatusDlcType=_IbmappnNodeLsStatusDlcType_Object((1,3,6,1,4,1,2,6,2,13,1,5,5,1,14),_IbmappnNodeLsStatusDlcType_Type())
ibmappnNodeLsStatusDlcType.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsStatusDlcType.setStatus(_A)
_IbmappnNodeLsStatusLocalAddr_Type=DisplayString
_IbmappnNodeLsStatusLocalAddr_Object=MibTableColumn
ibmappnNodeLsStatusLocalAddr=_IbmappnNodeLsStatusLocalAddr_Object((1,3,6,1,4,1,2,6,2,13,1,5,5,1,15),_IbmappnNodeLsStatusLocalAddr_Type())
ibmappnNodeLsStatusLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsStatusLocalAddr.setStatus(_A)
_IbmappnNodeLsStatusRemoteAddr_Type=DisplayString
_IbmappnNodeLsStatusRemoteAddr_Object=MibTableColumn
ibmappnNodeLsStatusRemoteAddr=_IbmappnNodeLsStatusRemoteAddr_Object((1,3,6,1,4,1,2,6,2,13,1,5,5,1,16),_IbmappnNodeLsStatusRemoteAddr_Type())
ibmappnNodeLsStatusRemoteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeLsStatusRemoteAddr.setStatus(_A)
_IbmappnSnmpInformation_ObjectIdentity=ObjectIdentity
ibmappnSnmpInformation=_IbmappnSnmpInformation_ObjectIdentity((1,3,6,1,4,1,2,6,2,13,1,6))
_IbmappnSnmpInPkts_Type=Counter32
_IbmappnSnmpInPkts_Object=MibScalar
ibmappnSnmpInPkts=_IbmappnSnmpInPkts_Object((1,3,6,1,4,1,2,6,2,13,1,6,1),_IbmappnSnmpInPkts_Type())
ibmappnSnmpInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnSnmpInPkts.setStatus(_A)
_IbmappnSnmpInGetRequests_Type=Counter32
_IbmappnSnmpInGetRequests_Object=MibScalar
ibmappnSnmpInGetRequests=_IbmappnSnmpInGetRequests_Object((1,3,6,1,4,1,2,6,2,13,1,6,2),_IbmappnSnmpInGetRequests_Type())
ibmappnSnmpInGetRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnSnmpInGetRequests.setStatus(_A)
_IbmappnSnmpInGetNexts_Type=Counter32
_IbmappnSnmpInGetNexts_Object=MibScalar
ibmappnSnmpInGetNexts=_IbmappnSnmpInGetNexts_Object((1,3,6,1,4,1,2,6,2,13,1,6,3),_IbmappnSnmpInGetNexts_Type())
ibmappnSnmpInGetNexts.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnSnmpInGetNexts.setStatus(_A)
_IbmappnSnmpInSetRequests_Type=Counter32
_IbmappnSnmpInSetRequests_Object=MibScalar
ibmappnSnmpInSetRequests=_IbmappnSnmpInSetRequests_Object((1,3,6,1,4,1,2,6,2,13,1,6,4),_IbmappnSnmpInSetRequests_Type())
ibmappnSnmpInSetRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnSnmpInSetRequests.setStatus(_A)
_IbmappnSnmpInTotalVars_Type=Counter32
_IbmappnSnmpInTotalVars_Object=MibScalar
ibmappnSnmpInTotalVars=_IbmappnSnmpInTotalVars_Object((1,3,6,1,4,1,2,6,2,13,1,6,5),_IbmappnSnmpInTotalVars_Type())
ibmappnSnmpInTotalVars.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnSnmpInTotalVars.setStatus(_A)
_IbmappnSnmpInGetVars_Type=Counter32
_IbmappnSnmpInGetVars_Object=MibScalar
ibmappnSnmpInGetVars=_IbmappnSnmpInGetVars_Object((1,3,6,1,4,1,2,6,2,13,1,6,6),_IbmappnSnmpInGetVars_Type())
ibmappnSnmpInGetVars.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnSnmpInGetVars.setStatus(_A)
_IbmappnSnmpInGetNextVars_Type=Counter32
_IbmappnSnmpInGetNextVars_Object=MibScalar
ibmappnSnmpInGetNextVars=_IbmappnSnmpInGetNextVars_Object((1,3,6,1,4,1,2,6,2,13,1,6,7),_IbmappnSnmpInGetNextVars_Type())
ibmappnSnmpInGetNextVars.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnSnmpInGetNextVars.setStatus(_A)
_IbmappnSnmpInSetVars_Type=Counter32
_IbmappnSnmpInSetVars_Object=MibScalar
ibmappnSnmpInSetVars=_IbmappnSnmpInSetVars_Object((1,3,6,1,4,1,2,6,2,13,1,6,8),_IbmappnSnmpInSetVars_Type())
ibmappnSnmpInSetVars.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnSnmpInSetVars.setStatus(_A)
_IbmappnSnmpOutNoSuchNames_Type=Counter32
_IbmappnSnmpOutNoSuchNames_Object=MibScalar
ibmappnSnmpOutNoSuchNames=_IbmappnSnmpOutNoSuchNames_Object((1,3,6,1,4,1,2,6,2,13,1,6,9),_IbmappnSnmpOutNoSuchNames_Type())
ibmappnSnmpOutNoSuchNames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnSnmpOutNoSuchNames.setStatus(_A)
_IbmappnSnmpOutGenErrs_Type=Counter32
_IbmappnSnmpOutGenErrs_Object=MibScalar
ibmappnSnmpOutGenErrs=_IbmappnSnmpOutGenErrs_Object((1,3,6,1,4,1,2,6,2,13,1,6,10),_IbmappnSnmpOutGenErrs_Type())
ibmappnSnmpOutGenErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnSnmpOutGenErrs.setStatus(_A)
_IbmappnMemoryUse_ObjectIdentity=ObjectIdentity
ibmappnMemoryUse=_IbmappnMemoryUse_ObjectIdentity((1,3,6,1,4,1,2,6,2,13,1,7))
_IbmappnMemorySize_Type=Integer32
_IbmappnMemorySize_Object=MibScalar
ibmappnMemorySize=_IbmappnMemorySize_Object((1,3,6,1,4,1,2,6,2,13,1,7,1),_IbmappnMemorySize_Type())
ibmappnMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnMemorySize.setStatus(_A)
_IbmappnMemoryUsed_Type=Integer32
_IbmappnMemoryUsed_Object=MibScalar
ibmappnMemoryUsed=_IbmappnMemoryUsed_Object((1,3,6,1,4,1,2,6,2,13,1,7,2),_IbmappnMemoryUsed_Type())
ibmappnMemoryUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnMemoryUsed.setStatus(_A)
_IbmappnMemoryWarnThresh_Type=Integer32
_IbmappnMemoryWarnThresh_Object=MibScalar
ibmappnMemoryWarnThresh=_IbmappnMemoryWarnThresh_Object((1,3,6,1,4,1,2,6,2,13,1,7,3),_IbmappnMemoryWarnThresh_Type())
ibmappnMemoryWarnThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnMemoryWarnThresh.setStatus(_A)
_IbmappnMemoryCritThresh_Type=Integer32
_IbmappnMemoryCritThresh_Object=MibScalar
ibmappnMemoryCritThresh=_IbmappnMemoryCritThresh_Object((1,3,6,1,4,1,2,6,2,13,1,7,4),_IbmappnMemoryCritThresh_Type())
ibmappnMemoryCritThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnMemoryCritThresh.setStatus(_A)
_IbmappnXidInformation_ObjectIdentity=ObjectIdentity
ibmappnXidInformation=_IbmappnXidInformation_ObjectIdentity((1,3,6,1,4,1,2,6,2,13,1,8))
_IbmappnNodeDefLsGoodXids_Type=Counter32
_IbmappnNodeDefLsGoodXids_Object=MibScalar
ibmappnNodeDefLsGoodXids=_IbmappnNodeDefLsGoodXids_Object((1,3,6,1,4,1,2,6,2,13,1,8,1),_IbmappnNodeDefLsGoodXids_Type())
ibmappnNodeDefLsGoodXids.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeDefLsGoodXids.setStatus(_A)
_IbmappnNodeDefLsBadXids_Type=Counter32
_IbmappnNodeDefLsBadXids_Object=MibScalar
ibmappnNodeDefLsBadXids=_IbmappnNodeDefLsBadXids_Object((1,3,6,1,4,1,2,6,2,13,1,8,2),_IbmappnNodeDefLsBadXids_Type())
ibmappnNodeDefLsBadXids.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeDefLsBadXids.setStatus(_A)
_IbmappnNodeDynLsGoodXids_Type=Counter32
_IbmappnNodeDynLsGoodXids_Object=MibScalar
ibmappnNodeDynLsGoodXids=_IbmappnNodeDynLsGoodXids_Object((1,3,6,1,4,1,2,6,2,13,1,8,3),_IbmappnNodeDynLsGoodXids_Type())
ibmappnNodeDynLsGoodXids.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeDynLsGoodXids.setStatus(_A)
_IbmappnNodeDynLsBadXids_Type=Counter32
_IbmappnNodeDynLsBadXids_Object=MibScalar
ibmappnNodeDynLsBadXids=_IbmappnNodeDynLsBadXids_Object((1,3,6,1,4,1,2,6,2,13,1,8,4),_IbmappnNodeDynLsBadXids_Type())
ibmappnNodeDynLsBadXids.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNodeDynLsBadXids.setStatus(_A)
_IbmappnNn_ObjectIdentity=ObjectIdentity
ibmappnNn=_IbmappnNn_ObjectIdentity((1,3,6,1,4,1,2,6,2,13,2))
_IbmappnNnTopo_ObjectIdentity=ObjectIdentity
ibmappnNnTopo=_IbmappnNnTopo_ObjectIdentity((1,3,6,1,4,1,2,6,2,13,2,1))
_IbmappnNnTopoMaxNodes_Type=Integer32
_IbmappnNnTopoMaxNodes_Object=MibScalar
ibmappnNnTopoMaxNodes=_IbmappnNnTopoMaxNodes_Object((1,3,6,1,4,1,2,6,2,13,2,1,1),_IbmappnNnTopoMaxNodes_Type())
ibmappnNnTopoMaxNodes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoMaxNodes.setStatus(_A)
_IbmappnNnTopoCurNumNodes_Type=Gauge32
_IbmappnNnTopoCurNumNodes_Object=MibScalar
ibmappnNnTopoCurNumNodes=_IbmappnNnTopoCurNumNodes_Object((1,3,6,1,4,1,2,6,2,13,2,1,2),_IbmappnNnTopoCurNumNodes_Type())
ibmappnNnTopoCurNumNodes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoCurNumNodes.setStatus(_A)
_IbmappnNnTopoInTdus_Type=Counter32
_IbmappnNnTopoInTdus_Object=MibScalar
ibmappnNnTopoInTdus=_IbmappnNnTopoInTdus_Object((1,3,6,1,4,1,2,6,2,13,2,1,3),_IbmappnNnTopoInTdus_Type())
ibmappnNnTopoInTdus.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoInTdus.setStatus(_A)
_IbmappnNnTopoOutTdus_Type=Counter32
_IbmappnNnTopoOutTdus_Object=MibScalar
ibmappnNnTopoOutTdus=_IbmappnNnTopoOutTdus_Object((1,3,6,1,4,1,2,6,2,13,2,1,4),_IbmappnNnTopoOutTdus_Type())
ibmappnNnTopoOutTdus.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoOutTdus.setStatus(_A)
_IbmappnNnTopoNodeLowRsns_Type=Counter32
_IbmappnNnTopoNodeLowRsns_Object=MibScalar
ibmappnNnTopoNodeLowRsns=_IbmappnNnTopoNodeLowRsns_Object((1,3,6,1,4,1,2,6,2,13,2,1,5),_IbmappnNnTopoNodeLowRsns_Type())
ibmappnNnTopoNodeLowRsns.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoNodeLowRsns.setStatus(_A)
_IbmappnNnTopoNodeEqualRsns_Type=Counter32
_IbmappnNnTopoNodeEqualRsns_Object=MibScalar
ibmappnNnTopoNodeEqualRsns=_IbmappnNnTopoNodeEqualRsns_Object((1,3,6,1,4,1,2,6,2,13,2,1,6),_IbmappnNnTopoNodeEqualRsns_Type())
ibmappnNnTopoNodeEqualRsns.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoNodeEqualRsns.setStatus(_A)
_IbmappnNnTopoNodeGoodHighRsns_Type=Counter32
_IbmappnNnTopoNodeGoodHighRsns_Object=MibScalar
ibmappnNnTopoNodeGoodHighRsns=_IbmappnNnTopoNodeGoodHighRsns_Object((1,3,6,1,4,1,2,6,2,13,2,1,7),_IbmappnNnTopoNodeGoodHighRsns_Type())
ibmappnNnTopoNodeGoodHighRsns.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoNodeGoodHighRsns.setStatus(_A)
_IbmappnNnTopoNodeBadHighRsns_Type=Counter32
_IbmappnNnTopoNodeBadHighRsns_Object=MibScalar
ibmappnNnTopoNodeBadHighRsns=_IbmappnNnTopoNodeBadHighRsns_Object((1,3,6,1,4,1,2,6,2,13,2,1,8),_IbmappnNnTopoNodeBadHighRsns_Type())
ibmappnNnTopoNodeBadHighRsns.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoNodeBadHighRsns.setStatus(_A)
_IbmappnNnTopoNodeStateUpdates_Type=Counter32
_IbmappnNnTopoNodeStateUpdates_Object=MibScalar
ibmappnNnTopoNodeStateUpdates=_IbmappnNnTopoNodeStateUpdates_Object((1,3,6,1,4,1,2,6,2,13,2,1,9),_IbmappnNnTopoNodeStateUpdates_Type())
ibmappnNnTopoNodeStateUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoNodeStateUpdates.setStatus(_A)
_IbmappnNnTopoNodeErrors_Type=Counter32
_IbmappnNnTopoNodeErrors_Object=MibScalar
ibmappnNnTopoNodeErrors=_IbmappnNnTopoNodeErrors_Object((1,3,6,1,4,1,2,6,2,13,2,1,10),_IbmappnNnTopoNodeErrors_Type())
ibmappnNnTopoNodeErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoNodeErrors.setStatus(_A)
_IbmappnNnTopoNodeTimerUpdates_Type=Counter32
_IbmappnNnTopoNodeTimerUpdates_Object=MibScalar
ibmappnNnTopoNodeTimerUpdates=_IbmappnNnTopoNodeTimerUpdates_Object((1,3,6,1,4,1,2,6,2,13,2,1,11),_IbmappnNnTopoNodeTimerUpdates_Type())
ibmappnNnTopoNodeTimerUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoNodeTimerUpdates.setStatus(_A)
_IbmappnNnTopoNodePurges_Type=Counter32
_IbmappnNnTopoNodePurges_Object=MibScalar
ibmappnNnTopoNodePurges=_IbmappnNnTopoNodePurges_Object((1,3,6,1,4,1,2,6,2,13,2,1,12),_IbmappnNnTopoNodePurges_Type())
ibmappnNnTopoNodePurges.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoNodePurges.setStatus(_A)
_IbmappnNnTopoTgLowRsns_Type=Counter32
_IbmappnNnTopoTgLowRsns_Object=MibScalar
ibmappnNnTopoTgLowRsns=_IbmappnNnTopoTgLowRsns_Object((1,3,6,1,4,1,2,6,2,13,2,1,13),_IbmappnNnTopoTgLowRsns_Type())
ibmappnNnTopoTgLowRsns.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoTgLowRsns.setStatus(_A)
_IbmappnNnTopoTgEqualRsns_Type=Counter32
_IbmappnNnTopoTgEqualRsns_Object=MibScalar
ibmappnNnTopoTgEqualRsns=_IbmappnNnTopoTgEqualRsns_Object((1,3,6,1,4,1,2,6,2,13,2,1,14),_IbmappnNnTopoTgEqualRsns_Type())
ibmappnNnTopoTgEqualRsns.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoTgEqualRsns.setStatus(_A)
_IbmappnNnTopoTgGoodHighRsns_Type=Counter32
_IbmappnNnTopoTgGoodHighRsns_Object=MibScalar
ibmappnNnTopoTgGoodHighRsns=_IbmappnNnTopoTgGoodHighRsns_Object((1,3,6,1,4,1,2,6,2,13,2,1,15),_IbmappnNnTopoTgGoodHighRsns_Type())
ibmappnNnTopoTgGoodHighRsns.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoTgGoodHighRsns.setStatus(_A)
_IbmappnNnTopoTgBadHighRsns_Type=Counter32
_IbmappnNnTopoTgBadHighRsns_Object=MibScalar
ibmappnNnTopoTgBadHighRsns=_IbmappnNnTopoTgBadHighRsns_Object((1,3,6,1,4,1,2,6,2,13,2,1,16),_IbmappnNnTopoTgBadHighRsns_Type())
ibmappnNnTopoTgBadHighRsns.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoTgBadHighRsns.setStatus(_A)
_IbmappnNnTopoTgStateUpdates_Type=Counter32
_IbmappnNnTopoTgStateUpdates_Object=MibScalar
ibmappnNnTopoTgStateUpdates=_IbmappnNnTopoTgStateUpdates_Object((1,3,6,1,4,1,2,6,2,13,2,1,17),_IbmappnNnTopoTgStateUpdates_Type())
ibmappnNnTopoTgStateUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoTgStateUpdates.setStatus(_A)
_IbmappnNnTopoTgErrors_Type=Counter32
_IbmappnNnTopoTgErrors_Object=MibScalar
ibmappnNnTopoTgErrors=_IbmappnNnTopoTgErrors_Object((1,3,6,1,4,1,2,6,2,13,2,1,18),_IbmappnNnTopoTgErrors_Type())
ibmappnNnTopoTgErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoTgErrors.setStatus(_A)
_IbmappnNnTopoTgTimerUpdates_Type=Counter32
_IbmappnNnTopoTgTimerUpdates_Object=MibScalar
ibmappnNnTopoTgTimerUpdates=_IbmappnNnTopoTgTimerUpdates_Object((1,3,6,1,4,1,2,6,2,13,2,1,19),_IbmappnNnTopoTgTimerUpdates_Type())
ibmappnNnTopoTgTimerUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoTgTimerUpdates.setStatus(_A)
_IbmappnNnTopoTgPurges_Type=Counter32
_IbmappnNnTopoTgPurges_Object=MibScalar
ibmappnNnTopoTgPurges=_IbmappnNnTopoTgPurges_Object((1,3,6,1,4,1,2,6,2,13,2,1,20),_IbmappnNnTopoTgPurges_Type())
ibmappnNnTopoTgPurges.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoTgPurges.setStatus(_A)
_IbmappnNnTopoTotalRouteCalcs_Type=Counter32
_IbmappnNnTopoTotalRouteCalcs_Object=MibScalar
ibmappnNnTopoTotalRouteCalcs=_IbmappnNnTopoTotalRouteCalcs_Object((1,3,6,1,4,1,2,6,2,13,2,1,21),_IbmappnNnTopoTotalRouteCalcs_Type())
ibmappnNnTopoTotalRouteCalcs.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoTotalRouteCalcs.setStatus(_A)
_IbmappnNnTopoTotalRouteRejs_Type=Counter32
_IbmappnNnTopoTotalRouteRejs_Object=MibScalar
ibmappnNnTopoTotalRouteRejs=_IbmappnNnTopoTotalRouteRejs_Object((1,3,6,1,4,1,2,6,2,13,2,1,22),_IbmappnNnTopoTotalRouteRejs_Type())
ibmappnNnTopoTotalRouteRejs.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoTotalRouteRejs.setStatus(_A)
_IbmappnNnTopoRouteTable_Object=MibTable
ibmappnNnTopoRouteTable=_IbmappnNnTopoRouteTable_Object((1,3,6,1,4,1,2,6,2,13,2,1,23))
if mibBuilder.loadTexts:ibmappnNnTopoRouteTable.setStatus(_A)
_IbmappnNnTopoRouteEntry_Object=MibTableRow
ibmappnNnTopoRouteEntry=_IbmappnNnTopoRouteEntry_Object((1,3,6,1,4,1,2,6,2,13,2,1,23,1))
ibmappnNnTopoRouteEntry.setIndexNames((0,_G,_t))
if mibBuilder.loadTexts:ibmappnNnTopoRouteEntry.setStatus(_A)
_IbmappnNnTopoRouteCos_Type=DisplayString
_IbmappnNnTopoRouteCos_Object=MibTableColumn
ibmappnNnTopoRouteCos=_IbmappnNnTopoRouteCos_Object((1,3,6,1,4,1,2,6,2,13,2,1,23,1,1),_IbmappnNnTopoRouteCos_Type())
ibmappnNnTopoRouteCos.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoRouteCos.setStatus(_A)
_IbmappnNnTopoRouteTrees_Type=Counter32
_IbmappnNnTopoRouteTrees_Object=MibTableColumn
ibmappnNnTopoRouteTrees=_IbmappnNnTopoRouteTrees_Object((1,3,6,1,4,1,2,6,2,13,2,1,23,1,2),_IbmappnNnTopoRouteTrees_Type())
ibmappnNnTopoRouteTrees.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoRouteTrees.setStatus(_A)
_IbmappnNnTopoRouteCalcs_Type=Counter32
_IbmappnNnTopoRouteCalcs_Object=MibTableColumn
ibmappnNnTopoRouteCalcs=_IbmappnNnTopoRouteCalcs_Object((1,3,6,1,4,1,2,6,2,13,2,1,23,1,3),_IbmappnNnTopoRouteCalcs_Type())
ibmappnNnTopoRouteCalcs.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoRouteCalcs.setStatus(_A)
_IbmappnNnTopoRouteRejs_Type=Counter32
_IbmappnNnTopoRouteRejs_Object=MibTableColumn
ibmappnNnTopoRouteRejs=_IbmappnNnTopoRouteRejs_Object((1,3,6,1,4,1,2,6,2,13,2,1,23,1,4),_IbmappnNnTopoRouteRejs_Type())
ibmappnNnTopoRouteRejs.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTopoRouteRejs.setStatus(_A)
_IbmappnNnAdjNodeTable_Object=MibTable
ibmappnNnAdjNodeTable=_IbmappnNnAdjNodeTable_Object((1,3,6,1,4,1,2,6,2,13,2,2))
if mibBuilder.loadTexts:ibmappnNnAdjNodeTable.setStatus(_A)
_IbmappnNnAdjNodeEntry_Object=MibTableRow
ibmappnNnAdjNodeEntry=_IbmappnNnAdjNodeEntry_Object((1,3,6,1,4,1,2,6,2,13,2,2,1))
ibmappnNnAdjNodeEntry.setIndexNames((0,_G,_u))
if mibBuilder.loadTexts:ibmappnNnAdjNodeEntry.setStatus(_A)
class _IbmappnNnAdjNodeAdjName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_IbmappnNnAdjNodeAdjName_Type.__name__=_F
_IbmappnNnAdjNodeAdjName_Object=MibTableColumn
ibmappnNnAdjNodeAdjName=_IbmappnNnAdjNodeAdjName_Object((1,3,6,1,4,1,2,6,2,13,2,2,1,1),_IbmappnNnAdjNodeAdjName_Type())
ibmappnNnAdjNodeAdjName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnAdjNodeAdjName.setStatus(_A)
class _IbmappnNnAdjNodeCpCpSessStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),('conLoserActive',2),('conWinnerActive',3),(_I,4)))
_IbmappnNnAdjNodeCpCpSessStatus_Type.__name__=_C
_IbmappnNnAdjNodeCpCpSessStatus_Object=MibTableColumn
ibmappnNnAdjNodeCpCpSessStatus=_IbmappnNnAdjNodeCpCpSessStatus_Object((1,3,6,1,4,1,2,6,2,13,2,2,1,2),_IbmappnNnAdjNodeCpCpSessStatus_Type())
ibmappnNnAdjNodeCpCpSessStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnAdjNodeCpCpSessStatus.setStatus(_A)
_IbmappnNnAdjNodeOutOfSeqTdus_Type=Gauge32
_IbmappnNnAdjNodeOutOfSeqTdus_Object=MibTableColumn
ibmappnNnAdjNodeOutOfSeqTdus=_IbmappnNnAdjNodeOutOfSeqTdus_Object((1,3,6,1,4,1,2,6,2,13,2,2,1,3),_IbmappnNnAdjNodeOutOfSeqTdus_Type())
ibmappnNnAdjNodeOutOfSeqTdus.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnAdjNodeOutOfSeqTdus.setStatus(_A)
class _IbmappnNnAdjNodeLastFrsnSent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IbmappnNnAdjNodeLastFrsnSent_Type.__name__=_C
_IbmappnNnAdjNodeLastFrsnSent_Object=MibTableColumn
ibmappnNnAdjNodeLastFrsnSent=_IbmappnNnAdjNodeLastFrsnSent_Object((1,3,6,1,4,1,2,6,2,13,2,2,1,4),_IbmappnNnAdjNodeLastFrsnSent_Type())
ibmappnNnAdjNodeLastFrsnSent.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnAdjNodeLastFrsnSent.setStatus(_A)
class _IbmappnNnAdjNodeLastFrsnRcvd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IbmappnNnAdjNodeLastFrsnRcvd_Type.__name__=_C
_IbmappnNnAdjNodeLastFrsnRcvd_Object=MibTableColumn
ibmappnNnAdjNodeLastFrsnRcvd=_IbmappnNnAdjNodeLastFrsnRcvd_Object((1,3,6,1,4,1,2,6,2,13,2,2,1,5),_IbmappnNnAdjNodeLastFrsnRcvd_Type())
ibmappnNnAdjNodeLastFrsnRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnAdjNodeLastFrsnRcvd.setStatus(_A)
_IbmappnNnTopology_ObjectIdentity=ObjectIdentity
ibmappnNnTopology=_IbmappnNnTopology_ObjectIdentity((1,3,6,1,4,1,2,6,2,13,2,3))
_IbmappnNnTopologyTable_Object=MibTable
ibmappnNnTopologyTable=_IbmappnNnTopologyTable_Object((1,3,6,1,4,1,2,6,2,13,2,3,1))
if mibBuilder.loadTexts:ibmappnNnTopologyTable.setStatus(_A)
_IbmappnNnTopologyEntry_Object=MibTableRow
ibmappnNnTopologyEntry=_IbmappnNnTopologyEntry_Object((1,3,6,1,4,1,2,6,2,13,2,3,1,1))
ibmappnNnTopologyEntry.setIndexNames((0,_G,_v))
if mibBuilder.loadTexts:ibmappnNnTopologyEntry.setStatus(_A)
class _IbmappnNnNodeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_IbmappnNnNodeName_Type.__name__=_F
_IbmappnNnNodeName_Object=MibTableColumn
ibmappnNnNodeName=_IbmappnNnNodeName_Object((1,3,6,1,4,1,2,6,2,13,2,3,1,1,1),_IbmappnNnNodeName_Type())
ibmappnNnNodeName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeName.setStatus(_A)
class _IbmappnNnNodeFrsn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IbmappnNnNodeFrsn_Type.__name__=_C
_IbmappnNnNodeFrsn_Object=MibTableColumn
ibmappnNnNodeFrsn=_IbmappnNnNodeFrsn_Object((1,3,6,1,4,1,2,6,2,13,2,3,1,1,2),_IbmappnNnNodeFrsn_Type())
ibmappnNnNodeFrsn.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeFrsn.setStatus(_A)
class _IbmappnNnNodeEntryTimeLeft_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_IbmappnNnNodeEntryTimeLeft_Type.__name__=_C
_IbmappnNnNodeEntryTimeLeft_Object=MibTableColumn
ibmappnNnNodeEntryTimeLeft=_IbmappnNnNodeEntryTimeLeft_Object((1,3,6,1,4,1,2,6,2,13,2,3,1,1,3),_IbmappnNnNodeEntryTimeLeft_Type())
ibmappnNnNodeEntryTimeLeft.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeEntryTimeLeft.setStatus(_A)
class _IbmappnNnNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_g,1),(_w,3)))
_IbmappnNnNodeType_Type.__name__=_C
_IbmappnNnNodeType_Object=MibTableColumn
ibmappnNnNodeType=_IbmappnNnNodeType_Object((1,3,6,1,4,1,2,6,2,13,2,3,1,1,4),_IbmappnNnNodeType_Type())
ibmappnNnNodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeType.setStatus(_A)
_IbmappnNnNodeRsn_Type=Integer32
_IbmappnNnNodeRsn_Object=MibTableColumn
ibmappnNnNodeRsn=_IbmappnNnNodeRsn_Object((1,3,6,1,4,1,2,6,2,13,2,3,1,1,5),_IbmappnNnNodeRsn_Type())
ibmappnNnNodeRsn.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeRsn.setStatus(_A)
_IbmappnNnNodeRouteAddResist_Type=Integer32
_IbmappnNnNodeRouteAddResist_Object=MibTableColumn
ibmappnNnNodeRouteAddResist=_IbmappnNnNodeRouteAddResist_Object((1,3,6,1,4,1,2,6,2,13,2,3,1,1,6),_IbmappnNnNodeRouteAddResist_Type())
ibmappnNnNodeRouteAddResist.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeRouteAddResist.setStatus(_A)
class _IbmappnNnNodeCongested_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNnNodeCongested_Type.__name__=_C
_IbmappnNnNodeCongested_Object=MibTableColumn
ibmappnNnNodeCongested=_IbmappnNnNodeCongested_Object((1,3,6,1,4,1,2,6,2,13,2,3,1,1,7),_IbmappnNnNodeCongested_Type())
ibmappnNnNodeCongested.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeCongested.setStatus(_A)
class _IbmappnNnNodeIsrDepleted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNnNodeIsrDepleted_Type.__name__=_C
_IbmappnNnNodeIsrDepleted_Object=MibTableColumn
ibmappnNnNodeIsrDepleted=_IbmappnNnNodeIsrDepleted_Object((1,3,6,1,4,1,2,6,2,13,2,3,1,1,8),_IbmappnNnNodeIsrDepleted_Type())
ibmappnNnNodeIsrDepleted.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeIsrDepleted.setStatus(_A)
class _IbmappnNnNodeEndptDepleted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNnNodeEndptDepleted_Type.__name__=_C
_IbmappnNnNodeEndptDepleted_Object=MibTableColumn
ibmappnNnNodeEndptDepleted=_IbmappnNnNodeEndptDepleted_Object((1,3,6,1,4,1,2,6,2,13,2,3,1,1,9),_IbmappnNnNodeEndptDepleted_Type())
ibmappnNnNodeEndptDepleted.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeEndptDepleted.setStatus(_A)
class _IbmappnNnNodeQuiescing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNnNodeQuiescing_Type.__name__=_C
_IbmappnNnNodeQuiescing_Object=MibTableColumn
ibmappnNnNodeQuiescing=_IbmappnNnNodeQuiescing_Object((1,3,6,1,4,1,2,6,2,13,2,3,1,1,10),_IbmappnNnNodeQuiescing_Type())
ibmappnNnNodeQuiescing.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeQuiescing.setStatus(_A)
class _IbmappnNnNodeGateway_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNnNodeGateway_Type.__name__=_C
_IbmappnNnNodeGateway_Object=MibTableColumn
ibmappnNnNodeGateway=_IbmappnNnNodeGateway_Object((1,3,6,1,4,1,2,6,2,13,2,3,1,1,11),_IbmappnNnNodeGateway_Type())
ibmappnNnNodeGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeGateway.setStatus(_A)
class _IbmappnNnNodeCentralDirectory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNnNodeCentralDirectory_Type.__name__=_C
_IbmappnNnNodeCentralDirectory_Object=MibTableColumn
ibmappnNnNodeCentralDirectory=_IbmappnNnNodeCentralDirectory_Object((1,3,6,1,4,1,2,6,2,13,2,3,1,1,12),_IbmappnNnNodeCentralDirectory_Type())
ibmappnNnNodeCentralDirectory.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeCentralDirectory.setStatus(_A)
class _IbmappnNnNodeIsr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNnNodeIsr_Type.__name__=_C
_IbmappnNnNodeIsr_Object=MibTableColumn
ibmappnNnNodeIsr=_IbmappnNnNodeIsr_Object((1,3,6,1,4,1,2,6,2,13,2,3,1,1,13),_IbmappnNnNodeIsr_Type())
ibmappnNnNodeIsr.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeIsr.setStatus(_A)
class _IbmappnNnNodeChainSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNnNodeChainSupport_Type.__name__=_C
_IbmappnNnNodeChainSupport_Object=MibTableColumn
ibmappnNnNodeChainSupport=_IbmappnNnNodeChainSupport_Object((1,3,6,1,4,1,2,6,2,13,2,3,1,1,14),_IbmappnNnNodeChainSupport_Type())
ibmappnNnNodeChainSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeChainSupport.setStatus(_A)
_IbmappnNnTgTopologyTable_Object=MibTable
ibmappnNnTgTopologyTable=_IbmappnNnTgTopologyTable_Object((1,3,6,1,4,1,2,6,2,13,2,3,2))
if mibBuilder.loadTexts:ibmappnNnTgTopologyTable.setStatus(_A)
_IbmappnNnTgTopologyEntry_Object=MibTableRow
ibmappnNnTgTopologyEntry=_IbmappnNnTgTopologyEntry_Object((1,3,6,1,4,1,2,6,2,13,2,3,2,1))
ibmappnNnTgTopologyEntry.setIndexNames((0,_G,_x),(0,_G,_y),(0,_G,_z))
if mibBuilder.loadTexts:ibmappnNnTgTopologyEntry.setStatus(_A)
class _IbmappnNnTgOwner_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_IbmappnNnTgOwner_Type.__name__=_F
_IbmappnNnTgOwner_Object=MibTableColumn
ibmappnNnTgOwner=_IbmappnNnTgOwner_Object((1,3,6,1,4,1,2,6,2,13,2,3,2,1,1),_IbmappnNnTgOwner_Type())
ibmappnNnTgOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgOwner.setStatus(_A)
class _IbmappnNnTgDest_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_IbmappnNnTgDest_Type.__name__=_F
_IbmappnNnTgDest_Object=MibTableColumn
ibmappnNnTgDest=_IbmappnNnTgDest_Object((1,3,6,1,4,1,2,6,2,13,2,3,2,1,2),_IbmappnNnTgDest_Type())
ibmappnNnTgDest.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgDest.setStatus(_A)
class _IbmappnNnTgNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnNnTgNum_Type.__name__=_C
_IbmappnNnTgNum_Object=MibTableColumn
ibmappnNnTgNum=_IbmappnNnTgNum_Object((1,3,6,1,4,1,2,6,2,13,2,3,2,1,3),_IbmappnNnTgNum_Type())
ibmappnNnTgNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgNum.setStatus(_A)
class _IbmappnNnTgFrsn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IbmappnNnTgFrsn_Type.__name__=_C
_IbmappnNnTgFrsn_Object=MibTableColumn
ibmappnNnTgFrsn=_IbmappnNnTgFrsn_Object((1,3,6,1,4,1,2,6,2,13,2,3,2,1,4),_IbmappnNnTgFrsn_Type())
ibmappnNnTgFrsn.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgFrsn.setStatus(_A)
class _IbmappnNnTgEntryTimeLeft_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_IbmappnNnTgEntryTimeLeft_Type.__name__=_C
_IbmappnNnTgEntryTimeLeft_Object=MibTableColumn
ibmappnNnTgEntryTimeLeft=_IbmappnNnTgEntryTimeLeft_Object((1,3,6,1,4,1,2,6,2,13,2,3,2,1,5),_IbmappnNnTgEntryTimeLeft_Type())
ibmappnNnTgEntryTimeLeft.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgEntryTimeLeft.setStatus(_A)
class _IbmappnNnTgDestVirtual_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNnTgDestVirtual_Type.__name__=_C
_IbmappnNnTgDestVirtual_Object=MibTableColumn
ibmappnNnTgDestVirtual=_IbmappnNnTgDestVirtual_Object((1,3,6,1,4,1,2,6,2,13,2,3,2,1,6),_IbmappnNnTgDestVirtual_Type())
ibmappnNnTgDestVirtual.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgDestVirtual.setStatus(_A)
class _IbmappnNnTgDlcData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_IbmappnNnTgDlcData_Type.__name__=_H
_IbmappnNnTgDlcData_Object=MibTableColumn
ibmappnNnTgDlcData=_IbmappnNnTgDlcData_Object((1,3,6,1,4,1,2,6,2,13,2,3,2,1,7),_IbmappnNnTgDlcData_Type())
ibmappnNnTgDlcData.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgDlcData.setStatus(_A)
_IbmappnNnTgRsn_Type=Integer32
_IbmappnNnTgRsn_Object=MibTableColumn
ibmappnNnTgRsn=_IbmappnNnTgRsn_Object((1,3,6,1,4,1,2,6,2,13,2,3,2,1,8),_IbmappnNnTgRsn_Type())
ibmappnNnTgRsn.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgRsn.setStatus(_A)
class _IbmappnNnTgOperational_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNnTgOperational_Type.__name__=_C
_IbmappnNnTgOperational_Object=MibTableColumn
ibmappnNnTgOperational=_IbmappnNnTgOperational_Object((1,3,6,1,4,1,2,6,2,13,2,3,2,1,9),_IbmappnNnTgOperational_Type())
ibmappnNnTgOperational.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgOperational.setStatus(_A)
class _IbmappnNnTgQuiescing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNnTgQuiescing_Type.__name__=_C
_IbmappnNnTgQuiescing_Object=MibTableColumn
ibmappnNnTgQuiescing=_IbmappnNnTgQuiescing_Object((1,3,6,1,4,1,2,6,2,13,2,3,2,1,10),_IbmappnNnTgQuiescing_Type())
ibmappnNnTgQuiescing.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgQuiescing.setStatus(_A)
class _IbmappnNnTgCpCpSession_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNnTgCpCpSession_Type.__name__=_C
_IbmappnNnTgCpCpSession_Object=MibTableColumn
ibmappnNnTgCpCpSession=_IbmappnNnTgCpCpSession_Object((1,3,6,1,4,1,2,6,2,13,2,3,2,1,11),_IbmappnNnTgCpCpSession_Type())
ibmappnNnTgCpCpSession.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgCpCpSession.setStatus(_A)
_IbmappnNnTgEffCap_Type=Integer32
_IbmappnNnTgEffCap_Object=MibTableColumn
ibmappnNnTgEffCap=_IbmappnNnTgEffCap_Object((1,3,6,1,4,1,2,6,2,13,2,3,2,1,12),_IbmappnNnTgEffCap_Type())
ibmappnNnTgEffCap.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgEffCap.setStatus(_A)
class _IbmappnNnTgConnCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnNnTgConnCost_Type.__name__=_C
_IbmappnNnTgConnCost_Object=MibTableColumn
ibmappnNnTgConnCost=_IbmappnNnTgConnCost_Object((1,3,6,1,4,1,2,6,2,13,2,3,2,1,13),_IbmappnNnTgConnCost_Type())
ibmappnNnTgConnCost.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgConnCost.setStatus(_A)
class _IbmappnNnTgByteCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnNnTgByteCost_Type.__name__=_C
_IbmappnNnTgByteCost_Object=MibTableColumn
ibmappnNnTgByteCost=_IbmappnNnTgByteCost_Object((1,3,6,1,4,1,2,6,2,13,2,3,2,1,14),_IbmappnNnTgByteCost_Type())
ibmappnNnTgByteCost.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgByteCost.setStatus(_A)
class _IbmappnNnTgSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,32,64,96,128,160,192)));namedValues=NamedValues(*((_L,1),(_M,32),(_N,64),(_O,96),(_P,128),(_Q,160),(_R,192)))
_IbmappnNnTgSecurity_Type.__name__=_C
_IbmappnNnTgSecurity_Object=MibTableColumn
ibmappnNnTgSecurity=_IbmappnNnTgSecurity_Object((1,3,6,1,4,1,2,6,2,13,2,3,2,1,15),_IbmappnNnTgSecurity_Type())
ibmappnNnTgSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgSecurity.setStatus(_A)
class _IbmappnNnTgDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,384,9216,147456,294912,2013265920)));namedValues=NamedValues(*((_S,0),(_T,384),(_U,9216),(_V,147456),(_W,294912),(_X,2013265920)))
_IbmappnNnTgDelay_Type.__name__=_C
_IbmappnNnTgDelay_Object=MibTableColumn
ibmappnNnTgDelay=_IbmappnNnTgDelay_Object((1,3,6,1,4,1,2,6,2,13,2,3,2,1,16),_IbmappnNnTgDelay_Type())
ibmappnNnTgDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgDelay.setStatus(_A)
class _IbmappnNnTgModemClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IbmappnNnTgModemClass_Type.__name__=_C
_IbmappnNnTgModemClass_Object=MibTableColumn
ibmappnNnTgModemClass=_IbmappnNnTgModemClass_Object((1,3,6,1,4,1,2,6,2,13,2,3,2,1,17),_IbmappnNnTgModemClass_Type())
ibmappnNnTgModemClass.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgModemClass.setStatus(_A)
class _IbmappnNnTgUsr1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnNnTgUsr1_Type.__name__=_C
_IbmappnNnTgUsr1_Object=MibTableColumn
ibmappnNnTgUsr1=_IbmappnNnTgUsr1_Object((1,3,6,1,4,1,2,6,2,13,2,3,2,1,18),_IbmappnNnTgUsr1_Type())
ibmappnNnTgUsr1.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgUsr1.setStatus(_A)
class _IbmappnNnTgUsr2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnNnTgUsr2_Type.__name__=_C
_IbmappnNnTgUsr2_Object=MibTableColumn
ibmappnNnTgUsr2=_IbmappnNnTgUsr2_Object((1,3,6,1,4,1,2,6,2,13,2,3,2,1,19),_IbmappnNnTgUsr2_Type())
ibmappnNnTgUsr2.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgUsr2.setStatus(_A)
class _IbmappnNnTgUsr3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnNnTgUsr3_Type.__name__=_C
_IbmappnNnTgUsr3_Object=MibTableColumn
ibmappnNnTgUsr3=_IbmappnNnTgUsr3_Object((1,3,6,1,4,1,2,6,2,13,2,3,2,1,20),_IbmappnNnTgUsr3_Type())
ibmappnNnTgUsr3.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgUsr3.setStatus(_A)
_IbmappnNnTopologyFRTable_Object=MibTable
ibmappnNnTopologyFRTable=_IbmappnNnTopologyFRTable_Object((1,3,6,1,4,1,2,6,2,13,2,3,3))
if mibBuilder.loadTexts:ibmappnNnTopologyFRTable.setStatus(_A)
_IbmappnNnTopologyFREntry_Object=MibTableRow
ibmappnNnTopologyFREntry=_IbmappnNnTopologyFREntry_Object((1,3,6,1,4,1,2,6,2,13,2,3,3,1))
ibmappnNnTopologyFREntry.setIndexNames((0,_G,_A0),(0,_G,_A1))
if mibBuilder.loadTexts:ibmappnNnTopologyFREntry.setStatus(_A)
class _IbmappnNnNodeFRName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_IbmappnNnNodeFRName_Type.__name__=_F
_IbmappnNnNodeFRName_Object=MibTableColumn
ibmappnNnNodeFRName=_IbmappnNnNodeFRName_Object((1,3,6,1,4,1,2,6,2,13,2,3,3,1,1),_IbmappnNnNodeFRName_Type())
ibmappnNnNodeFRName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeFRName.setStatus(_A)
class _IbmappnNnNodeFRFrsn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IbmappnNnNodeFRFrsn_Type.__name__=_C
_IbmappnNnNodeFRFrsn_Object=MibTableColumn
ibmappnNnNodeFRFrsn=_IbmappnNnNodeFRFrsn_Object((1,3,6,1,4,1,2,6,2,13,2,3,3,1,2),_IbmappnNnNodeFRFrsn_Type())
ibmappnNnNodeFRFrsn.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeFRFrsn.setStatus(_A)
class _IbmappnNnNodeFREntryTimeLeft_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_IbmappnNnNodeFREntryTimeLeft_Type.__name__=_C
_IbmappnNnNodeFREntryTimeLeft_Object=MibTableColumn
ibmappnNnNodeFREntryTimeLeft=_IbmappnNnNodeFREntryTimeLeft_Object((1,3,6,1,4,1,2,6,2,13,2,3,3,1,3),_IbmappnNnNodeFREntryTimeLeft_Type())
ibmappnNnNodeFREntryTimeLeft.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeFREntryTimeLeft.setStatus(_A)
class _IbmappnNnNodeFRType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_g,1),(_w,3)))
_IbmappnNnNodeFRType_Type.__name__=_C
_IbmappnNnNodeFRType_Object=MibTableColumn
ibmappnNnNodeFRType=_IbmappnNnNodeFRType_Object((1,3,6,1,4,1,2,6,2,13,2,3,3,1,4),_IbmappnNnNodeFRType_Type())
ibmappnNnNodeFRType.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeFRType.setStatus(_A)
_IbmappnNnNodeFRRsn_Type=Integer32
_IbmappnNnNodeFRRsn_Object=MibTableColumn
ibmappnNnNodeFRRsn=_IbmappnNnNodeFRRsn_Object((1,3,6,1,4,1,2,6,2,13,2,3,3,1,5),_IbmappnNnNodeFRRsn_Type())
ibmappnNnNodeFRRsn.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeFRRsn.setStatus(_A)
_IbmappnNnNodeFRRouteAddResist_Type=Integer32
_IbmappnNnNodeFRRouteAddResist_Object=MibTableColumn
ibmappnNnNodeFRRouteAddResist=_IbmappnNnNodeFRRouteAddResist_Object((1,3,6,1,4,1,2,6,2,13,2,3,3,1,6),_IbmappnNnNodeFRRouteAddResist_Type())
ibmappnNnNodeFRRouteAddResist.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeFRRouteAddResist.setStatus(_A)
class _IbmappnNnNodeFRCongested_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNnNodeFRCongested_Type.__name__=_C
_IbmappnNnNodeFRCongested_Object=MibTableColumn
ibmappnNnNodeFRCongested=_IbmappnNnNodeFRCongested_Object((1,3,6,1,4,1,2,6,2,13,2,3,3,1,7),_IbmappnNnNodeFRCongested_Type())
ibmappnNnNodeFRCongested.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeFRCongested.setStatus(_A)
class _IbmappnNnNodeFRIsrDepleted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNnNodeFRIsrDepleted_Type.__name__=_C
_IbmappnNnNodeFRIsrDepleted_Object=MibTableColumn
ibmappnNnNodeFRIsrDepleted=_IbmappnNnNodeFRIsrDepleted_Object((1,3,6,1,4,1,2,6,2,13,2,3,3,1,8),_IbmappnNnNodeFRIsrDepleted_Type())
ibmappnNnNodeFRIsrDepleted.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeFRIsrDepleted.setStatus(_A)
class _IbmappnNnNodeFREndptDepleted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNnNodeFREndptDepleted_Type.__name__=_C
_IbmappnNnNodeFREndptDepleted_Object=MibTableColumn
ibmappnNnNodeFREndptDepleted=_IbmappnNnNodeFREndptDepleted_Object((1,3,6,1,4,1,2,6,2,13,2,3,3,1,9),_IbmappnNnNodeFREndptDepleted_Type())
ibmappnNnNodeFREndptDepleted.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeFREndptDepleted.setStatus(_A)
class _IbmappnNnNodeFRQuiescing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNnNodeFRQuiescing_Type.__name__=_C
_IbmappnNnNodeFRQuiescing_Object=MibTableColumn
ibmappnNnNodeFRQuiescing=_IbmappnNnNodeFRQuiescing_Object((1,3,6,1,4,1,2,6,2,13,2,3,3,1,10),_IbmappnNnNodeFRQuiescing_Type())
ibmappnNnNodeFRQuiescing.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeFRQuiescing.setStatus(_A)
class _IbmappnNnNodeFRGateway_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNnNodeFRGateway_Type.__name__=_C
_IbmappnNnNodeFRGateway_Object=MibTableColumn
ibmappnNnNodeFRGateway=_IbmappnNnNodeFRGateway_Object((1,3,6,1,4,1,2,6,2,13,2,3,3,1,11),_IbmappnNnNodeFRGateway_Type())
ibmappnNnNodeFRGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeFRGateway.setStatus(_A)
class _IbmappnNnNodeFRCentralDirectory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNnNodeFRCentralDirectory_Type.__name__=_C
_IbmappnNnNodeFRCentralDirectory_Object=MibTableColumn
ibmappnNnNodeFRCentralDirectory=_IbmappnNnNodeFRCentralDirectory_Object((1,3,6,1,4,1,2,6,2,13,2,3,3,1,12),_IbmappnNnNodeFRCentralDirectory_Type())
ibmappnNnNodeFRCentralDirectory.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeFRCentralDirectory.setStatus(_A)
class _IbmappnNnNodeFRIsr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNnNodeFRIsr_Type.__name__=_C
_IbmappnNnNodeFRIsr_Object=MibTableColumn
ibmappnNnNodeFRIsr=_IbmappnNnNodeFRIsr_Object((1,3,6,1,4,1,2,6,2,13,2,3,3,1,13),_IbmappnNnNodeFRIsr_Type())
ibmappnNnNodeFRIsr.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeFRIsr.setStatus(_A)
class _IbmappnNnNodeFRChainSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNnNodeFRChainSupport_Type.__name__=_C
_IbmappnNnNodeFRChainSupport_Object=MibTableColumn
ibmappnNnNodeFRChainSupport=_IbmappnNnNodeFRChainSupport_Object((1,3,6,1,4,1,2,6,2,13,2,3,3,1,14),_IbmappnNnNodeFRChainSupport_Type())
ibmappnNnNodeFRChainSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnNodeFRChainSupport.setStatus(_A)
_IbmappnNnTgTopologyFRTable_Object=MibTable
ibmappnNnTgTopologyFRTable=_IbmappnNnTgTopologyFRTable_Object((1,3,6,1,4,1,2,6,2,13,2,3,4))
if mibBuilder.loadTexts:ibmappnNnTgTopologyFRTable.setStatus(_A)
_IbmappnNnTgTopologyFREntry_Object=MibTableRow
ibmappnNnTgTopologyFREntry=_IbmappnNnTgTopologyFREntry_Object((1,3,6,1,4,1,2,6,2,13,2,3,4,1))
ibmappnNnTgTopologyFREntry.setIndexNames((0,_G,_A2),(0,_G,_A3),(0,_G,_A4),(0,_G,_A5))
if mibBuilder.loadTexts:ibmappnNnTgTopologyFREntry.setStatus(_A)
class _IbmappnNnTgFROwner_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_IbmappnNnTgFROwner_Type.__name__=_F
_IbmappnNnTgFROwner_Object=MibTableColumn
ibmappnNnTgFROwner=_IbmappnNnTgFROwner_Object((1,3,6,1,4,1,2,6,2,13,2,3,4,1,1),_IbmappnNnTgFROwner_Type())
ibmappnNnTgFROwner.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgFROwner.setStatus(_A)
class _IbmappnNnTgFRDest_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_IbmappnNnTgFRDest_Type.__name__=_F
_IbmappnNnTgFRDest_Object=MibTableColumn
ibmappnNnTgFRDest=_IbmappnNnTgFRDest_Object((1,3,6,1,4,1,2,6,2,13,2,3,4,1,2),_IbmappnNnTgFRDest_Type())
ibmappnNnTgFRDest.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgFRDest.setStatus(_A)
class _IbmappnNnTgFRNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnNnTgFRNum_Type.__name__=_C
_IbmappnNnTgFRNum_Object=MibTableColumn
ibmappnNnTgFRNum=_IbmappnNnTgFRNum_Object((1,3,6,1,4,1,2,6,2,13,2,3,4,1,3),_IbmappnNnTgFRNum_Type())
ibmappnNnTgFRNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgFRNum.setStatus(_A)
class _IbmappnNnTgFRFrsn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IbmappnNnTgFRFrsn_Type.__name__=_C
_IbmappnNnTgFRFrsn_Object=MibTableColumn
ibmappnNnTgFRFrsn=_IbmappnNnTgFRFrsn_Object((1,3,6,1,4,1,2,6,2,13,2,3,4,1,4),_IbmappnNnTgFRFrsn_Type())
ibmappnNnTgFRFrsn.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgFRFrsn.setStatus(_A)
class _IbmappnNnTgFREntryTimeLeft_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_IbmappnNnTgFREntryTimeLeft_Type.__name__=_C
_IbmappnNnTgFREntryTimeLeft_Object=MibTableColumn
ibmappnNnTgFREntryTimeLeft=_IbmappnNnTgFREntryTimeLeft_Object((1,3,6,1,4,1,2,6,2,13,2,3,4,1,5),_IbmappnNnTgFREntryTimeLeft_Type())
ibmappnNnTgFREntryTimeLeft.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgFREntryTimeLeft.setStatus(_A)
class _IbmappnNnTgFRDestVirtual_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNnTgFRDestVirtual_Type.__name__=_C
_IbmappnNnTgFRDestVirtual_Object=MibTableColumn
ibmappnNnTgFRDestVirtual=_IbmappnNnTgFRDestVirtual_Object((1,3,6,1,4,1,2,6,2,13,2,3,4,1,6),_IbmappnNnTgFRDestVirtual_Type())
ibmappnNnTgFRDestVirtual.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgFRDestVirtual.setStatus(_A)
class _IbmappnNnTgFRDlcData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_IbmappnNnTgFRDlcData_Type.__name__=_H
_IbmappnNnTgFRDlcData_Object=MibTableColumn
ibmappnNnTgFRDlcData=_IbmappnNnTgFRDlcData_Object((1,3,6,1,4,1,2,6,2,13,2,3,4,1,7),_IbmappnNnTgFRDlcData_Type())
ibmappnNnTgFRDlcData.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgFRDlcData.setStatus(_A)
_IbmappnNnTgFRRsn_Type=Integer32
_IbmappnNnTgFRRsn_Object=MibTableColumn
ibmappnNnTgFRRsn=_IbmappnNnTgFRRsn_Object((1,3,6,1,4,1,2,6,2,13,2,3,4,1,8),_IbmappnNnTgFRRsn_Type())
ibmappnNnTgFRRsn.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgFRRsn.setStatus(_A)
class _IbmappnNnTgFROperational_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNnTgFROperational_Type.__name__=_C
_IbmappnNnTgFROperational_Object=MibTableColumn
ibmappnNnTgFROperational=_IbmappnNnTgFROperational_Object((1,3,6,1,4,1,2,6,2,13,2,3,4,1,9),_IbmappnNnTgFROperational_Type())
ibmappnNnTgFROperational.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgFROperational.setStatus(_A)
class _IbmappnNnTgFRQuiescing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNnTgFRQuiescing_Type.__name__=_C
_IbmappnNnTgFRQuiescing_Object=MibTableColumn
ibmappnNnTgFRQuiescing=_IbmappnNnTgFRQuiescing_Object((1,3,6,1,4,1,2,6,2,13,2,3,4,1,10),_IbmappnNnTgFRQuiescing_Type())
ibmappnNnTgFRQuiescing.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgFRQuiescing.setStatus(_A)
class _IbmappnNnTgFRCpCpSession_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnNnTgFRCpCpSession_Type.__name__=_C
_IbmappnNnTgFRCpCpSession_Object=MibTableColumn
ibmappnNnTgFRCpCpSession=_IbmappnNnTgFRCpCpSession_Object((1,3,6,1,4,1,2,6,2,13,2,3,4,1,11),_IbmappnNnTgFRCpCpSession_Type())
ibmappnNnTgFRCpCpSession.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgFRCpCpSession.setStatus(_A)
_IbmappnNnTgFREffCap_Type=Integer32
_IbmappnNnTgFREffCap_Object=MibTableColumn
ibmappnNnTgFREffCap=_IbmappnNnTgFREffCap_Object((1,3,6,1,4,1,2,6,2,13,2,3,4,1,12),_IbmappnNnTgFREffCap_Type())
ibmappnNnTgFREffCap.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgFREffCap.setStatus(_A)
class _IbmappnNnTgFRConnCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnNnTgFRConnCost_Type.__name__=_C
_IbmappnNnTgFRConnCost_Object=MibTableColumn
ibmappnNnTgFRConnCost=_IbmappnNnTgFRConnCost_Object((1,3,6,1,4,1,2,6,2,13,2,3,4,1,13),_IbmappnNnTgFRConnCost_Type())
ibmappnNnTgFRConnCost.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgFRConnCost.setStatus(_A)
class _IbmappnNnTgFRByteCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnNnTgFRByteCost_Type.__name__=_C
_IbmappnNnTgFRByteCost_Object=MibTableColumn
ibmappnNnTgFRByteCost=_IbmappnNnTgFRByteCost_Object((1,3,6,1,4,1,2,6,2,13,2,3,4,1,14),_IbmappnNnTgFRByteCost_Type())
ibmappnNnTgFRByteCost.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgFRByteCost.setStatus(_A)
class _IbmappnNnTgFRSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,32,64,96,128,160,192)));namedValues=NamedValues(*((_L,1),(_M,32),(_N,64),(_O,96),(_P,128),(_Q,160),(_R,192)))
_IbmappnNnTgFRSecurity_Type.__name__=_C
_IbmappnNnTgFRSecurity_Object=MibTableColumn
ibmappnNnTgFRSecurity=_IbmappnNnTgFRSecurity_Object((1,3,6,1,4,1,2,6,2,13,2,3,4,1,15),_IbmappnNnTgFRSecurity_Type())
ibmappnNnTgFRSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgFRSecurity.setStatus(_A)
class _IbmappnNnTgFRDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,384,9216,147456,294912,2013265920)));namedValues=NamedValues(*((_S,0),(_T,384),(_U,9216),(_V,147456),(_W,294912),(_X,2013265920)))
_IbmappnNnTgFRDelay_Type.__name__=_C
_IbmappnNnTgFRDelay_Object=MibTableColumn
ibmappnNnTgFRDelay=_IbmappnNnTgFRDelay_Object((1,3,6,1,4,1,2,6,2,13,2,3,4,1,16),_IbmappnNnTgFRDelay_Type())
ibmappnNnTgFRDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgFRDelay.setStatus(_A)
class _IbmappnNnTgFRModemClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IbmappnNnTgFRModemClass_Type.__name__=_C
_IbmappnNnTgFRModemClass_Object=MibTableColumn
ibmappnNnTgFRModemClass=_IbmappnNnTgFRModemClass_Object((1,3,6,1,4,1,2,6,2,13,2,3,4,1,17),_IbmappnNnTgFRModemClass_Type())
ibmappnNnTgFRModemClass.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgFRModemClass.setStatus(_A)
class _IbmappnNnTgFRUsr1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnNnTgFRUsr1_Type.__name__=_C
_IbmappnNnTgFRUsr1_Object=MibTableColumn
ibmappnNnTgFRUsr1=_IbmappnNnTgFRUsr1_Object((1,3,6,1,4,1,2,6,2,13,2,3,4,1,18),_IbmappnNnTgFRUsr1_Type())
ibmappnNnTgFRUsr1.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgFRUsr1.setStatus(_A)
class _IbmappnNnTgFRUsr2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnNnTgFRUsr2_Type.__name__=_C
_IbmappnNnTgFRUsr2_Object=MibTableColumn
ibmappnNnTgFRUsr2=_IbmappnNnTgFRUsr2_Object((1,3,6,1,4,1,2,6,2,13,2,3,4,1,19),_IbmappnNnTgFRUsr2_Type())
ibmappnNnTgFRUsr2.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgFRUsr2.setStatus(_A)
class _IbmappnNnTgFRUsr3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnNnTgFRUsr3_Type.__name__=_C
_IbmappnNnTgFRUsr3_Object=MibTableColumn
ibmappnNnTgFRUsr3=_IbmappnNnTgFRUsr3_Object((1,3,6,1,4,1,2,6,2,13,2,3,4,1,20),_IbmappnNnTgFRUsr3_Type())
ibmappnNnTgFRUsr3.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnNnTgFRUsr3.setStatus(_A)
_IbmappnLocalTopology_ObjectIdentity=ObjectIdentity
ibmappnLocalTopology=_IbmappnLocalTopology_ObjectIdentity((1,3,6,1,4,1,2,6,2,13,3))
_IbmappnLocalThisNode_ObjectIdentity=ObjectIdentity
ibmappnLocalThisNode=_IbmappnLocalThisNode_ObjectIdentity((1,3,6,1,4,1,2,6,2,13,3,1))
_IbmappnLocalGeneral_ObjectIdentity=ObjectIdentity
ibmappnLocalGeneral=_IbmappnLocalGeneral_ObjectIdentity((1,3,6,1,4,1,2,6,2,13,3,1,1))
class _IbmappnLocalNodeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_IbmappnLocalNodeName_Type.__name__=_F
_IbmappnLocalNodeName_Object=MibScalar
ibmappnLocalNodeName=_IbmappnLocalNodeName_Object((1,3,6,1,4,1,2,6,2,13,3,1,1,1),_IbmappnLocalNodeName_Type())
ibmappnLocalNodeName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalNodeName.setStatus(_A)
class _IbmappnLocalNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*((_g,1),('endnode',2),(_e,4)))
_IbmappnLocalNodeType_Type.__name__=_C
_IbmappnLocalNodeType_Object=MibScalar
ibmappnLocalNodeType=_IbmappnLocalNodeType_Object((1,3,6,1,4,1,2,6,2,13,3,1,1,2),_IbmappnLocalNodeType_Type())
ibmappnLocalNodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalNodeType.setStatus(_A)
_IbmappnLocalNnSpecific_ObjectIdentity=ObjectIdentity
ibmappnLocalNnSpecific=_IbmappnLocalNnSpecific_ObjectIdentity((1,3,6,1,4,1,2,6,2,13,3,1,2))
_IbmappnLocalNnRsn_Type=Integer32
_IbmappnLocalNnRsn_Object=MibScalar
ibmappnLocalNnRsn=_IbmappnLocalNnRsn_Object((1,3,6,1,4,1,2,6,2,13,3,1,2,1),_IbmappnLocalNnRsn_Type())
ibmappnLocalNnRsn.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalNnRsn.setStatus(_A)
_IbmappnLocalNnRouteAddResist_Type=Integer32
_IbmappnLocalNnRouteAddResist_Object=MibScalar
ibmappnLocalNnRouteAddResist=_IbmappnLocalNnRouteAddResist_Object((1,3,6,1,4,1,2,6,2,13,3,1,2,2),_IbmappnLocalNnRouteAddResist_Type())
ibmappnLocalNnRouteAddResist.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalNnRouteAddResist.setStatus(_A)
class _IbmappnLocalNnCongested_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnLocalNnCongested_Type.__name__=_C
_IbmappnLocalNnCongested_Object=MibScalar
ibmappnLocalNnCongested=_IbmappnLocalNnCongested_Object((1,3,6,1,4,1,2,6,2,13,3,1,2,3),_IbmappnLocalNnCongested_Type())
ibmappnLocalNnCongested.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalNnCongested.setStatus(_A)
class _IbmappnLocalNnIsrDepleted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnLocalNnIsrDepleted_Type.__name__=_C
_IbmappnLocalNnIsrDepleted_Object=MibScalar
ibmappnLocalNnIsrDepleted=_IbmappnLocalNnIsrDepleted_Object((1,3,6,1,4,1,2,6,2,13,3,1,2,4),_IbmappnLocalNnIsrDepleted_Type())
ibmappnLocalNnIsrDepleted.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalNnIsrDepleted.setStatus(_A)
class _IbmappnLocalNnEndptDepleted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnLocalNnEndptDepleted_Type.__name__=_C
_IbmappnLocalNnEndptDepleted_Object=MibScalar
ibmappnLocalNnEndptDepleted=_IbmappnLocalNnEndptDepleted_Object((1,3,6,1,4,1,2,6,2,13,3,1,2,5),_IbmappnLocalNnEndptDepleted_Type())
ibmappnLocalNnEndptDepleted.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalNnEndptDepleted.setStatus(_A)
class _IbmappnLocalNnQuiescing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnLocalNnQuiescing_Type.__name__=_C
_IbmappnLocalNnQuiescing_Object=MibScalar
ibmappnLocalNnQuiescing=_IbmappnLocalNnQuiescing_Object((1,3,6,1,4,1,2,6,2,13,3,1,2,6),_IbmappnLocalNnQuiescing_Type())
ibmappnLocalNnQuiescing.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalNnQuiescing.setStatus(_A)
class _IbmappnLocalNnGateway_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnLocalNnGateway_Type.__name__=_C
_IbmappnLocalNnGateway_Object=MibScalar
ibmappnLocalNnGateway=_IbmappnLocalNnGateway_Object((1,3,6,1,4,1,2,6,2,13,3,1,2,7),_IbmappnLocalNnGateway_Type())
ibmappnLocalNnGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalNnGateway.setStatus(_A)
class _IbmappnLocalNnCentralDirectory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnLocalNnCentralDirectory_Type.__name__=_C
_IbmappnLocalNnCentralDirectory_Object=MibScalar
ibmappnLocalNnCentralDirectory=_IbmappnLocalNnCentralDirectory_Object((1,3,6,1,4,1,2,6,2,13,3,1,2,8),_IbmappnLocalNnCentralDirectory_Type())
ibmappnLocalNnCentralDirectory.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalNnCentralDirectory.setStatus(_A)
class _IbmappnLocalNnIsr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnLocalNnIsr_Type.__name__=_C
_IbmappnLocalNnIsr_Object=MibScalar
ibmappnLocalNnIsr=_IbmappnLocalNnIsr_Object((1,3,6,1,4,1,2,6,2,13,3,1,2,9),_IbmappnLocalNnIsr_Type())
ibmappnLocalNnIsr.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalNnIsr.setStatus(_A)
class _IbmappnLocalNnChainSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnLocalNnChainSupport_Type.__name__=_C
_IbmappnLocalNnChainSupport_Object=MibScalar
ibmappnLocalNnChainSupport=_IbmappnLocalNnChainSupport_Object((1,3,6,1,4,1,2,6,2,13,3,1,2,10),_IbmappnLocalNnChainSupport_Type())
ibmappnLocalNnChainSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalNnChainSupport.setStatus(_A)
_IbmappnLocalNnFrsn_Type=Integer32
_IbmappnLocalNnFrsn_Object=MibScalar
ibmappnLocalNnFrsn=_IbmappnLocalNnFrsn_Object((1,3,6,1,4,1,2,6,2,13,3,1,2,11),_IbmappnLocalNnFrsn_Type())
ibmappnLocalNnFrsn.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalNnFrsn.setStatus(_A)
_IbmappnLocalTg_ObjectIdentity=ObjectIdentity
ibmappnLocalTg=_IbmappnLocalTg_ObjectIdentity((1,3,6,1,4,1,2,6,2,13,3,1,3))
_IbmappnLocalTgTable_Object=MibTable
ibmappnLocalTgTable=_IbmappnLocalTgTable_Object((1,3,6,1,4,1,2,6,2,13,3,1,3,1))
if mibBuilder.loadTexts:ibmappnLocalTgTable.setStatus(_A)
_IbmappnLocalTgEntry_Object=MibTableRow
ibmappnLocalTgEntry=_IbmappnLocalTgEntry_Object((1,3,6,1,4,1,2,6,2,13,3,1,3,1,1))
ibmappnLocalTgEntry.setIndexNames((0,_G,_A6),(0,_G,_A7))
if mibBuilder.loadTexts:ibmappnLocalTgEntry.setStatus(_A)
class _IbmappnLocalTgDest_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_IbmappnLocalTgDest_Type.__name__=_F
_IbmappnLocalTgDest_Object=MibTableColumn
ibmappnLocalTgDest=_IbmappnLocalTgDest_Object((1,3,6,1,4,1,2,6,2,13,3,1,3,1,1,1),_IbmappnLocalTgDest_Type())
ibmappnLocalTgDest.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalTgDest.setStatus(_A)
_IbmappnLocalTgNum_Type=Integer32
_IbmappnLocalTgNum_Object=MibTableColumn
ibmappnLocalTgNum=_IbmappnLocalTgNum_Object((1,3,6,1,4,1,2,6,2,13,3,1,3,1,1,2),_IbmappnLocalTgNum_Type())
ibmappnLocalTgNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalTgNum.setStatus(_A)
class _IbmappnLocalTgDestVirtual_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnLocalTgDestVirtual_Type.__name__=_C
_IbmappnLocalTgDestVirtual_Object=MibTableColumn
ibmappnLocalTgDestVirtual=_IbmappnLocalTgDestVirtual_Object((1,3,6,1,4,1,2,6,2,13,3,1,3,1,1,3),_IbmappnLocalTgDestVirtual_Type())
ibmappnLocalTgDestVirtual.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalTgDestVirtual.setStatus(_A)
class _IbmappnLocalTgDlcData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_IbmappnLocalTgDlcData_Type.__name__=_H
_IbmappnLocalTgDlcData_Object=MibTableColumn
ibmappnLocalTgDlcData=_IbmappnLocalTgDlcData_Object((1,3,6,1,4,1,2,6,2,13,3,1,3,1,1,4),_IbmappnLocalTgDlcData_Type())
ibmappnLocalTgDlcData.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalTgDlcData.setStatus(_A)
_IbmappnLocalTgRsn_Type=Integer32
_IbmappnLocalTgRsn_Object=MibTableColumn
ibmappnLocalTgRsn=_IbmappnLocalTgRsn_Object((1,3,6,1,4,1,2,6,2,13,3,1,3,1,1,5),_IbmappnLocalTgRsn_Type())
ibmappnLocalTgRsn.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalTgRsn.setStatus(_A)
class _IbmappnLocalTgQuiescing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnLocalTgQuiescing_Type.__name__=_C
_IbmappnLocalTgQuiescing_Object=MibTableColumn
ibmappnLocalTgQuiescing=_IbmappnLocalTgQuiescing_Object((1,3,6,1,4,1,2,6,2,13,3,1,3,1,1,6),_IbmappnLocalTgQuiescing_Type())
ibmappnLocalTgQuiescing.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalTgQuiescing.setStatus(_A)
class _IbmappnLocalTgOperational_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnLocalTgOperational_Type.__name__=_C
_IbmappnLocalTgOperational_Object=MibTableColumn
ibmappnLocalTgOperational=_IbmappnLocalTgOperational_Object((1,3,6,1,4,1,2,6,2,13,3,1,3,1,1,7),_IbmappnLocalTgOperational_Type())
ibmappnLocalTgOperational.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalTgOperational.setStatus(_A)
class _IbmappnLocalTgCpCpSession_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnLocalTgCpCpSession_Type.__name__=_C
_IbmappnLocalTgCpCpSession_Object=MibTableColumn
ibmappnLocalTgCpCpSession=_IbmappnLocalTgCpCpSession_Object((1,3,6,1,4,1,2,6,2,13,3,1,3,1,1,8),_IbmappnLocalTgCpCpSession_Type())
ibmappnLocalTgCpCpSession.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalTgCpCpSession.setStatus(_A)
_IbmappnLocalTgEffCap_Type=Integer32
_IbmappnLocalTgEffCap_Object=MibTableColumn
ibmappnLocalTgEffCap=_IbmappnLocalTgEffCap_Object((1,3,6,1,4,1,2,6,2,13,3,1,3,1,1,9),_IbmappnLocalTgEffCap_Type())
ibmappnLocalTgEffCap.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalTgEffCap.setStatus(_A)
class _IbmappnLocalTgConnCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnLocalTgConnCost_Type.__name__=_C
_IbmappnLocalTgConnCost_Object=MibTableColumn
ibmappnLocalTgConnCost=_IbmappnLocalTgConnCost_Object((1,3,6,1,4,1,2,6,2,13,3,1,3,1,1,10),_IbmappnLocalTgConnCost_Type())
ibmappnLocalTgConnCost.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalTgConnCost.setStatus(_A)
class _IbmappnLocalTgByteCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnLocalTgByteCost_Type.__name__=_C
_IbmappnLocalTgByteCost_Object=MibTableColumn
ibmappnLocalTgByteCost=_IbmappnLocalTgByteCost_Object((1,3,6,1,4,1,2,6,2,13,3,1,3,1,1,11),_IbmappnLocalTgByteCost_Type())
ibmappnLocalTgByteCost.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalTgByteCost.setStatus(_A)
class _IbmappnLocalTgSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,32,64,96,128,160,192)));namedValues=NamedValues(*((_L,1),(_M,32),(_N,64),(_O,96),(_P,128),(_Q,160),(_R,192)))
_IbmappnLocalTgSecurity_Type.__name__=_C
_IbmappnLocalTgSecurity_Object=MibTableColumn
ibmappnLocalTgSecurity=_IbmappnLocalTgSecurity_Object((1,3,6,1,4,1,2,6,2,13,3,1,3,1,1,12),_IbmappnLocalTgSecurity_Type())
ibmappnLocalTgSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalTgSecurity.setStatus(_A)
class _IbmappnLocalTgDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,384,9216,147456,294912,2013265920)));namedValues=NamedValues(*((_S,0),(_T,384),(_U,9216),(_V,147456),(_W,294912),(_X,2013265920)))
_IbmappnLocalTgDelay_Type.__name__=_C
_IbmappnLocalTgDelay_Object=MibTableColumn
ibmappnLocalTgDelay=_IbmappnLocalTgDelay_Object((1,3,6,1,4,1,2,6,2,13,3,1,3,1,1,13),_IbmappnLocalTgDelay_Type())
ibmappnLocalTgDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalTgDelay.setStatus(_A)
_IbmappnLocalTgModemClass_Type=Integer32
_IbmappnLocalTgModemClass_Object=MibTableColumn
ibmappnLocalTgModemClass=_IbmappnLocalTgModemClass_Object((1,3,6,1,4,1,2,6,2,13,3,1,3,1,1,14),_IbmappnLocalTgModemClass_Type())
ibmappnLocalTgModemClass.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalTgModemClass.setStatus(_A)
class _IbmappnLocalTgUsr1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnLocalTgUsr1_Type.__name__=_C
_IbmappnLocalTgUsr1_Object=MibTableColumn
ibmappnLocalTgUsr1=_IbmappnLocalTgUsr1_Object((1,3,6,1,4,1,2,6,2,13,3,1,3,1,1,15),_IbmappnLocalTgUsr1_Type())
ibmappnLocalTgUsr1.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalTgUsr1.setStatus(_A)
class _IbmappnLocalTgUsr2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnLocalTgUsr2_Type.__name__=_C
_IbmappnLocalTgUsr2_Object=MibTableColumn
ibmappnLocalTgUsr2=_IbmappnLocalTgUsr2_Object((1,3,6,1,4,1,2,6,2,13,3,1,3,1,1,16),_IbmappnLocalTgUsr2_Type())
ibmappnLocalTgUsr2.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalTgUsr2.setStatus(_A)
class _IbmappnLocalTgUsr3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnLocalTgUsr3_Type.__name__=_C
_IbmappnLocalTgUsr3_Object=MibTableColumn
ibmappnLocalTgUsr3=_IbmappnLocalTgUsr3_Object((1,3,6,1,4,1,2,6,2,13,3,1,3,1,1,17),_IbmappnLocalTgUsr3_Type())
ibmappnLocalTgUsr3.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalTgUsr3.setStatus(_A)
_IbmappnLocalEnTopology_ObjectIdentity=ObjectIdentity
ibmappnLocalEnTopology=_IbmappnLocalEnTopology_ObjectIdentity((1,3,6,1,4,1,2,6,2,13,3,2))
_IbmappnLocalEnTable_Object=MibTable
ibmappnLocalEnTable=_IbmappnLocalEnTable_Object((1,3,6,1,4,1,2,6,2,13,3,2,1))
if mibBuilder.loadTexts:ibmappnLocalEnTable.setStatus(_A)
_IbmappnLocalEnEntry_Object=MibTableRow
ibmappnLocalEnEntry=_IbmappnLocalEnEntry_Object((1,3,6,1,4,1,2,6,2,13,3,2,1,1))
ibmappnLocalEnEntry.setIndexNames((0,_G,_A8))
if mibBuilder.loadTexts:ibmappnLocalEnEntry.setStatus(_A)
class _IbmappnLocalEnName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_IbmappnLocalEnName_Type.__name__=_F
_IbmappnLocalEnName_Object=MibTableColumn
ibmappnLocalEnName=_IbmappnLocalEnName_Object((1,3,6,1,4,1,2,6,2,13,3,2,1,1,1),_IbmappnLocalEnName_Type())
ibmappnLocalEnName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalEnName.setStatus(_A)
class _IbmappnLocalEnEntryTimeLeft_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_IbmappnLocalEnEntryTimeLeft_Type.__name__=_C
_IbmappnLocalEnEntryTimeLeft_Object=MibTableColumn
ibmappnLocalEnEntryTimeLeft=_IbmappnLocalEnEntryTimeLeft_Object((1,3,6,1,4,1,2,6,2,13,3,2,1,1,2),_IbmappnLocalEnEntryTimeLeft_Type())
ibmappnLocalEnEntryTimeLeft.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalEnEntryTimeLeft.setStatus(_A)
class _IbmappnLocalEnType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4)));namedValues=NamedValues(*(('endnode',2),(_e,4)))
_IbmappnLocalEnType_Type.__name__=_C
_IbmappnLocalEnType_Object=MibTableColumn
ibmappnLocalEnType=_IbmappnLocalEnType_Object((1,3,6,1,4,1,2,6,2,13,3,2,1,1,3),_IbmappnLocalEnType_Type())
ibmappnLocalEnType.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalEnType.setStatus(_A)
_IbmappnLocalEnTgTable_Object=MibTable
ibmappnLocalEnTgTable=_IbmappnLocalEnTgTable_Object((1,3,6,1,4,1,2,6,2,13,3,2,2))
if mibBuilder.loadTexts:ibmappnLocalEnTgTable.setStatus(_A)
_IbmappnLocalEnTgEntry_Object=MibTableRow
ibmappnLocalEnTgEntry=_IbmappnLocalEnTgEntry_Object((1,3,6,1,4,1,2,6,2,13,3,2,2,1))
ibmappnLocalEnTgEntry.setIndexNames((0,_G,_A9),(0,_G,_AA),(0,_G,_AB))
if mibBuilder.loadTexts:ibmappnLocalEnTgEntry.setStatus(_A)
class _IbmappnLocalEnTgOrigin_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_IbmappnLocalEnTgOrigin_Type.__name__=_F
_IbmappnLocalEnTgOrigin_Object=MibTableColumn
ibmappnLocalEnTgOrigin=_IbmappnLocalEnTgOrigin_Object((1,3,6,1,4,1,2,6,2,13,3,2,2,1,1),_IbmappnLocalEnTgOrigin_Type())
ibmappnLocalEnTgOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalEnTgOrigin.setStatus(_A)
class _IbmappnLocalEnTgDest_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_IbmappnLocalEnTgDest_Type.__name__=_F
_IbmappnLocalEnTgDest_Object=MibTableColumn
ibmappnLocalEnTgDest=_IbmappnLocalEnTgDest_Object((1,3,6,1,4,1,2,6,2,13,3,2,2,1,2),_IbmappnLocalEnTgDest_Type())
ibmappnLocalEnTgDest.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalEnTgDest.setStatus(_A)
_IbmappnLocalEnTgNum_Type=Integer32
_IbmappnLocalEnTgNum_Object=MibTableColumn
ibmappnLocalEnTgNum=_IbmappnLocalEnTgNum_Object((1,3,6,1,4,1,2,6,2,13,3,2,2,1,3),_IbmappnLocalEnTgNum_Type())
ibmappnLocalEnTgNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalEnTgNum.setStatus(_A)
class _IbmappnLocalEnTgEntryTimeLeft_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_IbmappnLocalEnTgEntryTimeLeft_Type.__name__=_C
_IbmappnLocalEnTgEntryTimeLeft_Object=MibTableColumn
ibmappnLocalEnTgEntryTimeLeft=_IbmappnLocalEnTgEntryTimeLeft_Object((1,3,6,1,4,1,2,6,2,13,3,2,2,1,4),_IbmappnLocalEnTgEntryTimeLeft_Type())
ibmappnLocalEnTgEntryTimeLeft.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalEnTgEntryTimeLeft.setStatus(_A)
class _IbmappnLocalEnTgDestVirtual_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnLocalEnTgDestVirtual_Type.__name__=_C
_IbmappnLocalEnTgDestVirtual_Object=MibTableColumn
ibmappnLocalEnTgDestVirtual=_IbmappnLocalEnTgDestVirtual_Object((1,3,6,1,4,1,2,6,2,13,3,2,2,1,5),_IbmappnLocalEnTgDestVirtual_Type())
ibmappnLocalEnTgDestVirtual.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalEnTgDestVirtual.setStatus(_A)
_IbmappnLocalEnTgDlcData_Type=OctetString
_IbmappnLocalEnTgDlcData_Object=MibTableColumn
ibmappnLocalEnTgDlcData=_IbmappnLocalEnTgDlcData_Object((1,3,6,1,4,1,2,6,2,13,3,2,2,1,6),_IbmappnLocalEnTgDlcData_Type())
ibmappnLocalEnTgDlcData.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalEnTgDlcData.setStatus(_A)
class _IbmappnLocalEnTgOperational_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnLocalEnTgOperational_Type.__name__=_C
_IbmappnLocalEnTgOperational_Object=MibTableColumn
ibmappnLocalEnTgOperational=_IbmappnLocalEnTgOperational_Object((1,3,6,1,4,1,2,6,2,13,3,2,2,1,7),_IbmappnLocalEnTgOperational_Type())
ibmappnLocalEnTgOperational.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalEnTgOperational.setStatus(_A)
class _IbmappnLocalEnTgCpCpSession_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnLocalEnTgCpCpSession_Type.__name__=_C
_IbmappnLocalEnTgCpCpSession_Object=MibTableColumn
ibmappnLocalEnTgCpCpSession=_IbmappnLocalEnTgCpCpSession_Object((1,3,6,1,4,1,2,6,2,13,3,2,2,1,8),_IbmappnLocalEnTgCpCpSession_Type())
ibmappnLocalEnTgCpCpSession.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalEnTgCpCpSession.setStatus(_A)
_IbmappnLocalEnTgEffCap_Type=Integer32
_IbmappnLocalEnTgEffCap_Object=MibTableColumn
ibmappnLocalEnTgEffCap=_IbmappnLocalEnTgEffCap_Object((1,3,6,1,4,1,2,6,2,13,3,2,2,1,9),_IbmappnLocalEnTgEffCap_Type())
ibmappnLocalEnTgEffCap.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalEnTgEffCap.setStatus(_A)
class _IbmappnLocalEnTgConnCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnLocalEnTgConnCost_Type.__name__=_C
_IbmappnLocalEnTgConnCost_Object=MibTableColumn
ibmappnLocalEnTgConnCost=_IbmappnLocalEnTgConnCost_Object((1,3,6,1,4,1,2,6,2,13,3,2,2,1,10),_IbmappnLocalEnTgConnCost_Type())
ibmappnLocalEnTgConnCost.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalEnTgConnCost.setStatus(_A)
class _IbmappnLocalEnTgByteCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnLocalEnTgByteCost_Type.__name__=_C
_IbmappnLocalEnTgByteCost_Object=MibTableColumn
ibmappnLocalEnTgByteCost=_IbmappnLocalEnTgByteCost_Object((1,3,6,1,4,1,2,6,2,13,3,2,2,1,11),_IbmappnLocalEnTgByteCost_Type())
ibmappnLocalEnTgByteCost.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalEnTgByteCost.setStatus(_A)
class _IbmappnLocalEnTgSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,32,64,96,128,160,192)));namedValues=NamedValues(*((_L,1),(_M,32),(_N,64),(_O,96),(_P,128),(_Q,160),(_R,192)))
_IbmappnLocalEnTgSecurity_Type.__name__=_C
_IbmappnLocalEnTgSecurity_Object=MibTableColumn
ibmappnLocalEnTgSecurity=_IbmappnLocalEnTgSecurity_Object((1,3,6,1,4,1,2,6,2,13,3,2,2,1,12),_IbmappnLocalEnTgSecurity_Type())
ibmappnLocalEnTgSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalEnTgSecurity.setStatus(_A)
class _IbmappnLocalEnTgDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,384,9216,147456,294912,2013265920)));namedValues=NamedValues(*((_S,0),(_T,384),(_U,9216),(_V,147456),(_W,294912),(_X,2013265920)))
_IbmappnLocalEnTgDelay_Type.__name__=_C
_IbmappnLocalEnTgDelay_Object=MibTableColumn
ibmappnLocalEnTgDelay=_IbmappnLocalEnTgDelay_Object((1,3,6,1,4,1,2,6,2,13,3,2,2,1,13),_IbmappnLocalEnTgDelay_Type())
ibmappnLocalEnTgDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalEnTgDelay.setStatus(_A)
class _IbmappnLocalEnTgModemClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IbmappnLocalEnTgModemClass_Type.__name__=_C
_IbmappnLocalEnTgModemClass_Object=MibTableColumn
ibmappnLocalEnTgModemClass=_IbmappnLocalEnTgModemClass_Object((1,3,6,1,4,1,2,6,2,13,3,2,2,1,14),_IbmappnLocalEnTgModemClass_Type())
ibmappnLocalEnTgModemClass.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalEnTgModemClass.setStatus(_A)
class _IbmappnLocalEnTgUsr1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnLocalEnTgUsr1_Type.__name__=_C
_IbmappnLocalEnTgUsr1_Object=MibTableColumn
ibmappnLocalEnTgUsr1=_IbmappnLocalEnTgUsr1_Object((1,3,6,1,4,1,2,6,2,13,3,2,2,1,15),_IbmappnLocalEnTgUsr1_Type())
ibmappnLocalEnTgUsr1.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalEnTgUsr1.setStatus(_A)
class _IbmappnLocalEnTgUsr2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnLocalEnTgUsr2_Type.__name__=_C
_IbmappnLocalEnTgUsr2_Object=MibTableColumn
ibmappnLocalEnTgUsr2=_IbmappnLocalEnTgUsr2_Object((1,3,6,1,4,1,2,6,2,13,3,2,2,1,16),_IbmappnLocalEnTgUsr2_Type())
ibmappnLocalEnTgUsr2.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalEnTgUsr2.setStatus(_A)
class _IbmappnLocalEnTgUsr3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnLocalEnTgUsr3_Type.__name__=_C
_IbmappnLocalEnTgUsr3_Object=MibTableColumn
ibmappnLocalEnTgUsr3=_IbmappnLocalEnTgUsr3_Object((1,3,6,1,4,1,2,6,2,13,3,2,2,1,17),_IbmappnLocalEnTgUsr3_Type())
ibmappnLocalEnTgUsr3.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnLocalEnTgUsr3.setStatus(_A)
_IbmappnDir_ObjectIdentity=ObjectIdentity
ibmappnDir=_IbmappnDir_ObjectIdentity((1,3,6,1,4,1,2,6,2,13,5))
_IbmappnDirPerf_ObjectIdentity=ObjectIdentity
ibmappnDirPerf=_IbmappnDirPerf_ObjectIdentity((1,3,6,1,4,1,2,6,2,13,5,1))
_IbmappnDirMaxCaches_Type=Integer32
_IbmappnDirMaxCaches_Object=MibScalar
ibmappnDirMaxCaches=_IbmappnDirMaxCaches_Object((1,3,6,1,4,1,2,6,2,13,5,1,1),_IbmappnDirMaxCaches_Type())
ibmappnDirMaxCaches.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnDirMaxCaches.setStatus(_A)
_IbmappnDirCurCaches_Type=Gauge32
_IbmappnDirCurCaches_Object=MibScalar
ibmappnDirCurCaches=_IbmappnDirCurCaches_Object((1,3,6,1,4,1,2,6,2,13,5,1,2),_IbmappnDirCurCaches_Type())
ibmappnDirCurCaches.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnDirCurCaches.setStatus(_A)
_IbmappnDirCurHomeEntries_Type=Gauge32
_IbmappnDirCurHomeEntries_Object=MibScalar
ibmappnDirCurHomeEntries=_IbmappnDirCurHomeEntries_Object((1,3,6,1,4,1,2,6,2,13,5,1,3),_IbmappnDirCurHomeEntries_Type())
ibmappnDirCurHomeEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnDirCurHomeEntries.setStatus(_A)
_IbmappnDirRegEntries_Type=Gauge32
_IbmappnDirRegEntries_Object=MibScalar
ibmappnDirRegEntries=_IbmappnDirRegEntries_Object((1,3,6,1,4,1,2,6,2,13,5,1,4),_IbmappnDirRegEntries_Type())
ibmappnDirRegEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnDirRegEntries.setStatus(_A)
_IbmappnDirInLocates_Type=Counter32
_IbmappnDirInLocates_Object=MibScalar
ibmappnDirInLocates=_IbmappnDirInLocates_Object((1,3,6,1,4,1,2,6,2,13,5,1,5),_IbmappnDirInLocates_Type())
ibmappnDirInLocates.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnDirInLocates.setStatus(_A)
_IbmappnDirInBcastLocates_Type=Counter32
_IbmappnDirInBcastLocates_Object=MibScalar
ibmappnDirInBcastLocates=_IbmappnDirInBcastLocates_Object((1,3,6,1,4,1,2,6,2,13,5,1,6),_IbmappnDirInBcastLocates_Type())
ibmappnDirInBcastLocates.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnDirInBcastLocates.setStatus(_A)
_IbmappnDirOutLocates_Type=Counter32
_IbmappnDirOutLocates_Object=MibScalar
ibmappnDirOutLocates=_IbmappnDirOutLocates_Object((1,3,6,1,4,1,2,6,2,13,5,1,7),_IbmappnDirOutLocates_Type())
ibmappnDirOutLocates.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnDirOutLocates.setStatus(_A)
_IbmappnDirOutBcastLocates_Type=Counter32
_IbmappnDirOutBcastLocates_Object=MibScalar
ibmappnDirOutBcastLocates=_IbmappnDirOutBcastLocates_Object((1,3,6,1,4,1,2,6,2,13,5,1,8),_IbmappnDirOutBcastLocates_Type())
ibmappnDirOutBcastLocates.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnDirOutBcastLocates.setStatus(_A)
_IbmappnDirNotFoundLocates_Type=Counter32
_IbmappnDirNotFoundLocates_Object=MibScalar
ibmappnDirNotFoundLocates=_IbmappnDirNotFoundLocates_Object((1,3,6,1,4,1,2,6,2,13,5,1,9),_IbmappnDirNotFoundLocates_Type())
ibmappnDirNotFoundLocates.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnDirNotFoundLocates.setStatus(_A)
_IbmappnDirNotFoundBcastLocates_Type=Counter32
_IbmappnDirNotFoundBcastLocates_Object=MibScalar
ibmappnDirNotFoundBcastLocates=_IbmappnDirNotFoundBcastLocates_Object((1,3,6,1,4,1,2,6,2,13,5,1,10),_IbmappnDirNotFoundBcastLocates_Type())
ibmappnDirNotFoundBcastLocates.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnDirNotFoundBcastLocates.setStatus(_A)
_IbmappnDirLocateOutstands_Type=Gauge32
_IbmappnDirLocateOutstands_Object=MibScalar
ibmappnDirLocateOutstands=_IbmappnDirLocateOutstands_Object((1,3,6,1,4,1,2,6,2,13,5,1,11),_IbmappnDirLocateOutstands_Type())
ibmappnDirLocateOutstands.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnDirLocateOutstands.setStatus(_A)
_IbmappnDirTable_Object=MibTable
ibmappnDirTable=_IbmappnDirTable_Object((1,3,6,1,4,1,2,6,2,13,5,2))
if mibBuilder.loadTexts:ibmappnDirTable.setStatus(_A)
_IbmappnDirEntry_Object=MibTableRow
ibmappnDirEntry=_IbmappnDirEntry_Object((1,3,6,1,4,1,2,6,2,13,5,2,1))
ibmappnDirEntry.setIndexNames((0,_G,_AC))
if mibBuilder.loadTexts:ibmappnDirEntry.setStatus(_A)
class _IbmappnDirLuName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_IbmappnDirLuName_Type.__name__=_F
_IbmappnDirLuName_Object=MibTableColumn
ibmappnDirLuName=_IbmappnDirLuName_Object((1,3,6,1,4,1,2,6,2,13,5,2,1,1),_IbmappnDirLuName_Type())
ibmappnDirLuName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnDirLuName.setStatus(_A)
class _IbmappnDirServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_IbmappnDirServerName_Type.__name__=_F
_IbmappnDirServerName_Object=MibTableColumn
ibmappnDirServerName=_IbmappnDirServerName_Object((1,3,6,1,4,1,2,6,2,13,5,2,1,2),_IbmappnDirServerName_Type())
ibmappnDirServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnDirServerName.setStatus(_A)
class _IbmappnDirLuOwnerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_IbmappnDirLuOwnerName_Type.__name__=_F
_IbmappnDirLuOwnerName_Object=MibTableColumn
ibmappnDirLuOwnerName=_IbmappnDirLuOwnerName_Object((1,3,6,1,4,1,2,6,2,13,5,2,1,3),_IbmappnDirLuOwnerName_Type())
ibmappnDirLuOwnerName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnDirLuOwnerName.setStatus(_A)
class _IbmappnDirLuLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('local',1),('domain',2),('xdomain',3)))
_IbmappnDirLuLocation_Type.__name__=_C
_IbmappnDirLuLocation_Object=MibTableColumn
ibmappnDirLuLocation=_IbmappnDirLuLocation_Object((1,3,6,1,4,1,2,6,2,13,5,2,1,4),_IbmappnDirLuLocation_Type())
ibmappnDirLuLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnDirLuLocation.setStatus(_A)
class _IbmappnDirType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('home',1),('cache',2),('registered',3)))
_IbmappnDirType_Type.__name__=_C
_IbmappnDirType_Object=MibTableColumn
ibmappnDirType=_IbmappnDirType_Object((1,3,6,1,4,1,2,6,2,13,5,2,1,5),_IbmappnDirType_Type())
ibmappnDirType.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnDirType.setStatus(_A)
class _IbmappnDirWildCard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('explicit-entry',2),('partial-wildcard',3),('full-wildcard',4)))
_IbmappnDirWildCard_Type.__name__=_C
_IbmappnDirWildCard_Object=MibTableColumn
ibmappnDirWildCard=_IbmappnDirWildCard_Object((1,3,6,1,4,1,2,6,2,13,5,2,1,6),_IbmappnDirWildCard_Type())
ibmappnDirWildCard.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnDirWildCard.setStatus(_A)
_IbmappnCos_ObjectIdentity=ObjectIdentity
ibmappnCos=_IbmappnCos_ObjectIdentity((1,3,6,1,4,1,2,6,2,13,6))
_IbmappnCosModeTable_Object=MibTable
ibmappnCosModeTable=_IbmappnCosModeTable_Object((1,3,6,1,4,1,2,6,2,13,6,1))
if mibBuilder.loadTexts:ibmappnCosModeTable.setStatus(_A)
_IbmappnCosModeEntry_Object=MibTableRow
ibmappnCosModeEntry=_IbmappnCosModeEntry_Object((1,3,6,1,4,1,2,6,2,13,6,1,1))
ibmappnCosModeEntry.setIndexNames((0,_G,_AD))
if mibBuilder.loadTexts:ibmappnCosModeEntry.setStatus(_A)
class _IbmappnCosModeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_IbmappnCosModeName_Type.__name__=_F
_IbmappnCosModeName_Object=MibTableColumn
ibmappnCosModeName=_IbmappnCosModeName_Object((1,3,6,1,4,1,2,6,2,13,6,1,1,1),_IbmappnCosModeName_Type())
ibmappnCosModeName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosModeName.setStatus(_A)
class _IbmappnCosModeCosName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_IbmappnCosModeCosName_Type.__name__=_F
_IbmappnCosModeCosName_Object=MibTableColumn
ibmappnCosModeCosName=_IbmappnCosModeCosName_Object((1,3,6,1,4,1,2,6,2,13,6,1,1,2),_IbmappnCosModeCosName_Type())
ibmappnCosModeCosName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosModeCosName.setStatus(_A)
_IbmappnCosNameTable_Object=MibTable
ibmappnCosNameTable=_IbmappnCosNameTable_Object((1,3,6,1,4,1,2,6,2,13,6,2))
if mibBuilder.loadTexts:ibmappnCosNameTable.setStatus(_A)
_IbmappnCosNameEntry_Object=MibTableRow
ibmappnCosNameEntry=_IbmappnCosNameEntry_Object((1,3,6,1,4,1,2,6,2,13,6,2,1))
ibmappnCosNameEntry.setIndexNames((0,_G,_AE))
if mibBuilder.loadTexts:ibmappnCosNameEntry.setStatus(_A)
class _IbmappnCosName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_IbmappnCosName_Type.__name__=_F
_IbmappnCosName_Object=MibTableColumn
ibmappnCosName=_IbmappnCosName_Object((1,3,6,1,4,1,2,6,2,13,6,2,1,1),_IbmappnCosName_Type())
ibmappnCosName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosName.setStatus(_A)
class _IbmappnCosTransPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('low',1),('medium',2),('high',3),('network',4)))
_IbmappnCosTransPriority_Type.__name__=_C
_IbmappnCosTransPriority_Object=MibTableColumn
ibmappnCosTransPriority=_IbmappnCosTransPriority_Object((1,3,6,1,4,1,2,6,2,13,6,2,1,2),_IbmappnCosTransPriority_Type())
ibmappnCosTransPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosTransPriority.setStatus(_A)
_IbmappnCosNodeRowTable_Object=MibTable
ibmappnCosNodeRowTable=_IbmappnCosNodeRowTable_Object((1,3,6,1,4,1,2,6,2,13,6,3))
if mibBuilder.loadTexts:ibmappnCosNodeRowTable.setStatus(_A)
_IbmappnCosNodeRowEntry_Object=MibTableRow
ibmappnCosNodeRowEntry=_IbmappnCosNodeRowEntry_Object((1,3,6,1,4,1,2,6,2,13,6,3,1))
ibmappnCosNodeRowEntry.setIndexNames((0,_G,_AF),(0,_G,_AG))
if mibBuilder.loadTexts:ibmappnCosNodeRowEntry.setStatus(_A)
class _IbmappnCosNodeRowName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_IbmappnCosNodeRowName_Type.__name__=_F
_IbmappnCosNodeRowName_Object=MibTableColumn
ibmappnCosNodeRowName=_IbmappnCosNodeRowName_Object((1,3,6,1,4,1,2,6,2,13,6,3,1,1),_IbmappnCosNodeRowName_Type())
ibmappnCosNodeRowName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosNodeRowName.setStatus(_A)
class _IbmappnCosNodeRowIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnCosNodeRowIndex_Type.__name__=_C
_IbmappnCosNodeRowIndex_Object=MibTableColumn
ibmappnCosNodeRowIndex=_IbmappnCosNodeRowIndex_Object((1,3,6,1,4,1,2,6,2,13,6,3,1,2),_IbmappnCosNodeRowIndex_Type())
ibmappnCosNodeRowIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosNodeRowIndex.setStatus(_A)
_IbmappnCosNodeRowWgt_Type=DisplayString
_IbmappnCosNodeRowWgt_Object=MibTableColumn
ibmappnCosNodeRowWgt=_IbmappnCosNodeRowWgt_Object((1,3,6,1,4,1,2,6,2,13,6,3,1,3),_IbmappnCosNodeRowWgt_Type())
ibmappnCosNodeRowWgt.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosNodeRowWgt.setStatus(_A)
class _IbmappnCosNodeRowResistMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnCosNodeRowResistMin_Type.__name__=_C
_IbmappnCosNodeRowResistMin_Object=MibTableColumn
ibmappnCosNodeRowResistMin=_IbmappnCosNodeRowResistMin_Object((1,3,6,1,4,1,2,6,2,13,6,3,1,4),_IbmappnCosNodeRowResistMin_Type())
ibmappnCosNodeRowResistMin.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosNodeRowResistMin.setStatus(_A)
class _IbmappnCosNodeRowResistMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnCosNodeRowResistMax_Type.__name__=_C
_IbmappnCosNodeRowResistMax_Object=MibTableColumn
ibmappnCosNodeRowResistMax=_IbmappnCosNodeRowResistMax_Object((1,3,6,1,4,1,2,6,2,13,6,3,1,5),_IbmappnCosNodeRowResistMax_Type())
ibmappnCosNodeRowResistMax.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosNodeRowResistMax.setStatus(_A)
class _IbmappnCosNodeRowMinCongestAllow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnCosNodeRowMinCongestAllow_Type.__name__=_C
_IbmappnCosNodeRowMinCongestAllow_Object=MibTableColumn
ibmappnCosNodeRowMinCongestAllow=_IbmappnCosNodeRowMinCongestAllow_Object((1,3,6,1,4,1,2,6,2,13,6,3,1,6),_IbmappnCosNodeRowMinCongestAllow_Type())
ibmappnCosNodeRowMinCongestAllow.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosNodeRowMinCongestAllow.setStatus(_A)
class _IbmappnCosNodeRowMaxCongestAllow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_IbmappnCosNodeRowMaxCongestAllow_Type.__name__=_C
_IbmappnCosNodeRowMaxCongestAllow_Object=MibTableColumn
ibmappnCosNodeRowMaxCongestAllow=_IbmappnCosNodeRowMaxCongestAllow_Object((1,3,6,1,4,1,2,6,2,13,6,3,1,7),_IbmappnCosNodeRowMaxCongestAllow_Type())
ibmappnCosNodeRowMaxCongestAllow.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosNodeRowMaxCongestAllow.setStatus(_A)
_IbmappnCosTgRowTable_Object=MibTable
ibmappnCosTgRowTable=_IbmappnCosTgRowTable_Object((1,3,6,1,4,1,2,6,2,13,6,4))
if mibBuilder.loadTexts:ibmappnCosTgRowTable.setStatus(_A)
_IbmappnCosTgRowEntry_Object=MibTableRow
ibmappnCosTgRowEntry=_IbmappnCosTgRowEntry_Object((1,3,6,1,4,1,2,6,2,13,6,4,1))
ibmappnCosTgRowEntry.setIndexNames((0,_G,_AH),(0,_G,_AI))
if mibBuilder.loadTexts:ibmappnCosTgRowEntry.setStatus(_A)
class _IbmappnCosTgRowName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_IbmappnCosTgRowName_Type.__name__=_F
_IbmappnCosTgRowName_Object=MibTableColumn
ibmappnCosTgRowName=_IbmappnCosTgRowName_Object((1,3,6,1,4,1,2,6,2,13,6,4,1,1),_IbmappnCosTgRowName_Type())
ibmappnCosTgRowName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosTgRowName.setStatus(_A)
class _IbmappnCosTgRowIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnCosTgRowIndex_Type.__name__=_C
_IbmappnCosTgRowIndex_Object=MibTableColumn
ibmappnCosTgRowIndex=_IbmappnCosTgRowIndex_Object((1,3,6,1,4,1,2,6,2,13,6,4,1,2),_IbmappnCosTgRowIndex_Type())
ibmappnCosTgRowIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosTgRowIndex.setStatus(_A)
_IbmappnCosTgRowWgt_Type=DisplayString
_IbmappnCosTgRowWgt_Object=MibTableColumn
ibmappnCosTgRowWgt=_IbmappnCosTgRowWgt_Object((1,3,6,1,4,1,2,6,2,13,6,4,1,3),_IbmappnCosTgRowWgt_Type())
ibmappnCosTgRowWgt.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosTgRowWgt.setStatus(_A)
_IbmappnCosTgRowEffCapMin_Type=Integer32
_IbmappnCosTgRowEffCapMin_Object=MibTableColumn
ibmappnCosTgRowEffCapMin=_IbmappnCosTgRowEffCapMin_Object((1,3,6,1,4,1,2,6,2,13,6,4,1,4),_IbmappnCosTgRowEffCapMin_Type())
ibmappnCosTgRowEffCapMin.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosTgRowEffCapMin.setStatus(_A)
_IbmappnCosTgRowEffCapMax_Type=Integer32
_IbmappnCosTgRowEffCapMax_Object=MibTableColumn
ibmappnCosTgRowEffCapMax=_IbmappnCosTgRowEffCapMax_Object((1,3,6,1,4,1,2,6,2,13,6,4,1,5),_IbmappnCosTgRowEffCapMax_Type())
ibmappnCosTgRowEffCapMax.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosTgRowEffCapMax.setStatus(_A)
class _IbmappnCosTgRowConnCostMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnCosTgRowConnCostMin_Type.__name__=_C
_IbmappnCosTgRowConnCostMin_Object=MibTableColumn
ibmappnCosTgRowConnCostMin=_IbmappnCosTgRowConnCostMin_Object((1,3,6,1,4,1,2,6,2,13,6,4,1,6),_IbmappnCosTgRowConnCostMin_Type())
ibmappnCosTgRowConnCostMin.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosTgRowConnCostMin.setStatus(_A)
class _IbmappnCosTgRowConnCostMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnCosTgRowConnCostMax_Type.__name__=_C
_IbmappnCosTgRowConnCostMax_Object=MibTableColumn
ibmappnCosTgRowConnCostMax=_IbmappnCosTgRowConnCostMax_Object((1,3,6,1,4,1,2,6,2,13,6,4,1,7),_IbmappnCosTgRowConnCostMax_Type())
ibmappnCosTgRowConnCostMax.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosTgRowConnCostMax.setStatus(_A)
class _IbmappnCosTgRowByteCostMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnCosTgRowByteCostMin_Type.__name__=_C
_IbmappnCosTgRowByteCostMin_Object=MibTableColumn
ibmappnCosTgRowByteCostMin=_IbmappnCosTgRowByteCostMin_Object((1,3,6,1,4,1,2,6,2,13,6,4,1,8),_IbmappnCosTgRowByteCostMin_Type())
ibmappnCosTgRowByteCostMin.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosTgRowByteCostMin.setStatus(_A)
class _IbmappnCosTgRowByteCostMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnCosTgRowByteCostMax_Type.__name__=_C
_IbmappnCosTgRowByteCostMax_Object=MibTableColumn
ibmappnCosTgRowByteCostMax=_IbmappnCosTgRowByteCostMax_Object((1,3,6,1,4,1,2,6,2,13,6,4,1,9),_IbmappnCosTgRowByteCostMax_Type())
ibmappnCosTgRowByteCostMax.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosTgRowByteCostMax.setStatus(_A)
class _IbmappnCosTgRowSecurityMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,32,64,96,128,160,192)));namedValues=NamedValues(*((_L,1),(_M,32),(_N,64),(_O,96),(_P,128),(_Q,160),(_R,192)))
_IbmappnCosTgRowSecurityMin_Type.__name__=_C
_IbmappnCosTgRowSecurityMin_Object=MibTableColumn
ibmappnCosTgRowSecurityMin=_IbmappnCosTgRowSecurityMin_Object((1,3,6,1,4,1,2,6,2,13,6,4,1,10),_IbmappnCosTgRowSecurityMin_Type())
ibmappnCosTgRowSecurityMin.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosTgRowSecurityMin.setStatus(_A)
class _IbmappnCosTgRowSecurityMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,32,64,96,128,160,192)));namedValues=NamedValues(*((_L,1),(_M,32),(_N,64),(_O,96),(_P,128),(_Q,160),(_R,192)))
_IbmappnCosTgRowSecurityMax_Type.__name__=_C
_IbmappnCosTgRowSecurityMax_Object=MibTableColumn
ibmappnCosTgRowSecurityMax=_IbmappnCosTgRowSecurityMax_Object((1,3,6,1,4,1,2,6,2,13,6,4,1,11),_IbmappnCosTgRowSecurityMax_Type())
ibmappnCosTgRowSecurityMax.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosTgRowSecurityMax.setStatus(_A)
class _IbmappnCosTgRowDelayMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,384,9216,147456,294912,2013265920)));namedValues=NamedValues(*((_S,0),(_T,384),(_U,9216),(_V,147456),(_W,294912),(_X,2013265920)))
_IbmappnCosTgRowDelayMin_Type.__name__=_C
_IbmappnCosTgRowDelayMin_Object=MibTableColumn
ibmappnCosTgRowDelayMin=_IbmappnCosTgRowDelayMin_Object((1,3,6,1,4,1,2,6,2,13,6,4,1,12),_IbmappnCosTgRowDelayMin_Type())
ibmappnCosTgRowDelayMin.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosTgRowDelayMin.setStatus(_A)
class _IbmappnCosTgRowDelayMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,384,9216,147456,294912,2013265920)));namedValues=NamedValues(*((_S,0),(_T,384),(_U,9216),(_V,147456),(_W,294912),(_X,2013265920)))
_IbmappnCosTgRowDelayMax_Type.__name__=_C
_IbmappnCosTgRowDelayMax_Object=MibTableColumn
ibmappnCosTgRowDelayMax=_IbmappnCosTgRowDelayMax_Object((1,3,6,1,4,1,2,6,2,13,6,4,1,13),_IbmappnCosTgRowDelayMax_Type())
ibmappnCosTgRowDelayMax.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosTgRowDelayMax.setStatus(_A)
class _IbmappnCosTgRowUsr1Min_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnCosTgRowUsr1Min_Type.__name__=_C
_IbmappnCosTgRowUsr1Min_Object=MibTableColumn
ibmappnCosTgRowUsr1Min=_IbmappnCosTgRowUsr1Min_Object((1,3,6,1,4,1,2,6,2,13,6,4,1,14),_IbmappnCosTgRowUsr1Min_Type())
ibmappnCosTgRowUsr1Min.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosTgRowUsr1Min.setStatus(_A)
class _IbmappnCosTgRowUsr1Max_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnCosTgRowUsr1Max_Type.__name__=_C
_IbmappnCosTgRowUsr1Max_Object=MibTableColumn
ibmappnCosTgRowUsr1Max=_IbmappnCosTgRowUsr1Max_Object((1,3,6,1,4,1,2,6,2,13,6,4,1,15),_IbmappnCosTgRowUsr1Max_Type())
ibmappnCosTgRowUsr1Max.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosTgRowUsr1Max.setStatus(_A)
class _IbmappnCosTgRowUsr2Min_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnCosTgRowUsr2Min_Type.__name__=_C
_IbmappnCosTgRowUsr2Min_Object=MibTableColumn
ibmappnCosTgRowUsr2Min=_IbmappnCosTgRowUsr2Min_Object((1,3,6,1,4,1,2,6,2,13,6,4,1,16),_IbmappnCosTgRowUsr2Min_Type())
ibmappnCosTgRowUsr2Min.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosTgRowUsr2Min.setStatus(_A)
class _IbmappnCosTgRowUsr2Max_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnCosTgRowUsr2Max_Type.__name__=_C
_IbmappnCosTgRowUsr2Max_Object=MibTableColumn
ibmappnCosTgRowUsr2Max=_IbmappnCosTgRowUsr2Max_Object((1,3,6,1,4,1,2,6,2,13,6,4,1,17),_IbmappnCosTgRowUsr2Max_Type())
ibmappnCosTgRowUsr2Max.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosTgRowUsr2Max.setStatus(_A)
class _IbmappnCosTgRowUsr3Min_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnCosTgRowUsr3Min_Type.__name__=_C
_IbmappnCosTgRowUsr3Min_Object=MibTableColumn
ibmappnCosTgRowUsr3Min=_IbmappnCosTgRowUsr3Min_Object((1,3,6,1,4,1,2,6,2,13,6,4,1,18),_IbmappnCosTgRowUsr3Min_Type())
ibmappnCosTgRowUsr3Min.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosTgRowUsr3Min.setStatus(_A)
class _IbmappnCosTgRowUsr3Max_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmappnCosTgRowUsr3Max_Type.__name__=_C
_IbmappnCosTgRowUsr3Max_Object=MibTableColumn
ibmappnCosTgRowUsr3Max=_IbmappnCosTgRowUsr3Max_Object((1,3,6,1,4,1,2,6,2,13,6,4,1,19),_IbmappnCosTgRowUsr3Max_Type())
ibmappnCosTgRowUsr3Max.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmappnCosTgRowUsr3Max.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'ibm':ibm,'ibmProd':ibmProd,'ibm6611':ibm6611,'ibmappn':ibmappn,'ibmappnNode':ibmappnNode,'ibmappnGeneralInfoAndCaps':ibmappnGeneralInfoAndCaps,'ibmappnNodeCpName':ibmappnNodeCpName,'ibmappnNodeNetid':ibmappnNodeNetid,'ibmappnNodeBlockNum':ibmappnNodeBlockNum,'ibmappnNodeIdNum':ibmappnNodeIdNum,'ibmappnNodeType':ibmappnNodeType,'ibmappnNodeUpTime':ibmappnNodeUpTime,'ibmappnNodeNegotLs':ibmappnNodeNegotLs,'ibmappnNodeSegReasm':ibmappnNodeSegReasm,'ibmappnNodeBindReasm':ibmappnNodeBindReasm,'ibmappnNodeParallelTg':ibmappnNodeParallelTg,'ibmappnNodeService':ibmappnNodeService,'ibmappnNodeAdaptiveBindPacing':ibmappnNodeAdaptiveBindPacing,'ibmappnNnUniqueInfoAndCaps':ibmappnNnUniqueInfoAndCaps,'ibmappnNodeNnRcvRegChar':ibmappnNodeNnRcvRegChar,'ibmappnNodeNnGateway':ibmappnNodeNnGateway,'ibmappnNodeNnCentralDirectory':ibmappnNodeNnCentralDirectory,'ibmappnNodeNnTreeCache':ibmappnNodeNnTreeCache,'ibmappnNodeNnTreeUpdate':ibmappnNodeNnTreeUpdate,'ibmappnNodeNnRouteAddResist':ibmappnNodeNnRouteAddResist,'ibmappnNodeNnIsr':ibmappnNodeNnIsr,'ibmappnNodeNnFrsn':ibmappnNodeNnFrsn,'ibmappnEnUniqueCaps':ibmappnEnUniqueCaps,'ibmappnNodeEnSegGen':ibmappnNodeEnSegGen,'ibmappnNodeEnModeCosMap':ibmappnNodeEnModeCosMap,'ibmappnNodeEnLocateCdinit':ibmappnNodeEnLocateCdinit,'ibmappnNodeEnSendRegNames':ibmappnNodeEnSendRegNames,'ibmappnNodeEnSendRegChar':ibmappnNodeEnSendRegChar,'ibmappnPortInformation':ibmappnPortInformation,'ibmappnNodePortTable':ibmappnNodePortTable,'ibmappnNodePortEntry':ibmappnNodePortEntry,_h:ibmappnNodePortName,'ibmappnNodePortState':ibmappnNodePortState,'ibmappnNodePortDlcType':ibmappnNodePortDlcType,'ibmappnNodePortPortType':ibmappnNodePortPortType,'ibmappnNodePortSIMRIM':ibmappnNodePortSIMRIM,'ibmappnNodePortLsRole':ibmappnNodePortLsRole,'ibmappnNodePortMaxRcvBtuSize':ibmappnNodePortMaxRcvBtuSize,'ibmappnNodePortMaxIframeWindow':ibmappnNodePortMaxIframeWindow,'ibmappnNodePortDefLsGoodXids':ibmappnNodePortDefLsGoodXids,'ibmappnNodePortDefLsBadXids':ibmappnNodePortDefLsBadXids,'ibmappnNodePortDynLsGoodXids':ibmappnNodePortDynLsGoodXids,'ibmappnNodePortDynLsBadXids':ibmappnNodePortDynLsBadXids,'ibmappnNodePortSpecific':ibmappnNodePortSpecific,'ibmappnNodePortIpTable':ibmappnNodePortIpTable,'ibmappnNodePortIpEntry':ibmappnNodePortIpEntry,_j:ibmappnNodePortIpName,'ibmappnNodePortIpPortNum':ibmappnNodePortIpPortNum,'ibmappnNodePortDlsTable':ibmappnNodePortDlsTable,'ibmappnNodePortDlsEntry':ibmappnNodePortDlsEntry,_k:ibmappnNodePortDlsName,'ibmappnNodePortDlsMac':ibmappnNodePortDlsMac,'ibmappnNodePortDlsSap':ibmappnNodePortDlsSap,'ibmappnNodePortTrTable':ibmappnNodePortTrTable,'ibmappnNodePortTrEntry':ibmappnNodePortTrEntry,_l:ibmappnNodePortTrName,'ibmappnNodePortTrMac':ibmappnNodePortTrMac,'ibmappnNodePortTrSap':ibmappnNodePortTrSap,'ibmappnNodePortDlcTraceTable':ibmappnNodePortDlcTraceTable,'ibmappnNodePortDlcTraceEntry':ibmappnNodePortDlcTraceEntry,_m:ibmappnNodePortDlcTracPortName,_n:ibmappnNodePortDlcTracIndex,'ibmappnNodePortDlcTracDlcType':ibmappnNodePortDlcTracDlcType,'ibmappnNodePortDlcTracLocalAddr':ibmappnNodePortDlcTracLocalAddr,'ibmappnNodePortDlcTracRemoteAddr':ibmappnNodePortDlcTracRemoteAddr,'ibmappnNodePortDlcTracMsgType':ibmappnNodePortDlcTracMsgType,'ibmappnNodePortDlcTracCmdType':ibmappnNodePortDlcTracCmdType,'ibmappnNodePortDlcTracUseWan':ibmappnNodePortDlcTracUseWan,'ibmappnLinkStationInformation':ibmappnLinkStationInformation,'ibmappnNodeLsTable':ibmappnNodeLsTable,'ibmappnNodeLsEntry':ibmappnNodeLsEntry,_o:ibmappnNodeLsName,'ibmappnNodeLsPortName':ibmappnNodeLsPortName,'ibmappnNodeLsDlcType':ibmappnNodeLsDlcType,'ibmappnNodeLsDynamic':ibmappnNodeLsDynamic,'ibmappnNodeLsState':ibmappnNodeLsState,'ibmappnNodeLsCpName':ibmappnNodeLsCpName,'ibmappnNodeLsTgNum':ibmappnNodeLsTgNum,'ibmappnNodeLsLimResource':ibmappnNodeLsLimResource,'ibmappnNodeLsMigration':ibmappnNodeLsMigration,'ibmappnNodeLsBlockNum':ibmappnNodeLsBlockNum,'ibmappnNodeLsIdNum':ibmappnNodeLsIdNum,'ibmappnNodeLsCpCpSession':ibmappnNodeLsCpCpSession,'ibmappnNodeLsTargetPacingCount':ibmappnNodeLsTargetPacingCount,'ibmappnNodeLsMaxSendBtuSize':ibmappnNodeLsMaxSendBtuSize,'ibmappnNodeLsEffCap':ibmappnNodeLsEffCap,'ibmappnNodeLsConnCost':ibmappnNodeLsConnCost,'ibmappnNodeLsByteCost':ibmappnNodeLsByteCost,'ibmappnNodeLsSecurity':ibmappnNodeLsSecurity,'ibmappnNodeLsDelay':ibmappnNodeLsDelay,'ibmappnNodeLsUsr1':ibmappnNodeLsUsr1,'ibmappnNodeLsUsr2':ibmappnNodeLsUsr2,'ibmappnNodeLsUsr3':ibmappnNodeLsUsr3,'ibmappnNodeLsInXidBytes':ibmappnNodeLsInXidBytes,'ibmappnNodeLsInMsgBytes':ibmappnNodeLsInMsgBytes,'ibmappnNodeLsInXidFrames':ibmappnNodeLsInXidFrames,'ibmappnNodeLsInMsgFrames':ibmappnNodeLsInMsgFrames,'ibmappnNodeLsOutXidBytes':ibmappnNodeLsOutXidBytes,'ibmappnNodeLsOutMsgBytes':ibmappnNodeLsOutMsgBytes,'ibmappnNodeLsOutXidFrames':ibmappnNodeLsOutXidFrames,'ibmappnNodeLsOutMsgFrames':ibmappnNodeLsOutMsgFrames,'ibmappnNodeLsEchoRsps':ibmappnNodeLsEchoRsps,'ibmappnNodeLsCurrentDelay':ibmappnNodeLsCurrentDelay,'ibmappnNodeLsMaxDelay':ibmappnNodeLsMaxDelay,'ibmappnNodeLsMinDelay':ibmappnNodeLsMinDelay,'ibmappnNodeLsMaxDelayTime':ibmappnNodeLsMaxDelayTime,'ibmappnNodeLsGoodXids':ibmappnNodeLsGoodXids,'ibmappnNodeLsBadXids':ibmappnNodeLsBadXids,'ibmappnNodeLsSpecific':ibmappnNodeLsSpecific,'ibmappnNodeLsSubState':ibmappnNodeLsSubState,'ibmappnNodeLsStartTime':ibmappnNodeLsStartTime,'ibmappnNodeLsActiveTime':ibmappnNodeLsActiveTime,'ibmappnNodeLsCurrentStateTime':ibmappnNodeLsCurrentStateTime,'ibmappnNodeLsIpTable':ibmappnNodeLsIpTable,'ibmappnNodeLsIpEntry':ibmappnNodeLsIpEntry,_p:ibmappnNodeLsIpName,'ibmappnNodeLsIpState':ibmappnNodeLsIpState,'ibmappnNodeLsLocalIpAddr':ibmappnNodeLsLocalIpAddr,'ibmappnNodeLsLocalIpPortNum':ibmappnNodeLsLocalIpPortNum,'ibmappnNodeLsRemoteIpAddr':ibmappnNodeLsRemoteIpAddr,'ibmappnNodeLsRemoteIpPortNum':ibmappnNodeLsRemoteIpPortNum,'ibmappnNodeLsDlsTable':ibmappnNodeLsDlsTable,'ibmappnNodeLsDlsEntry':ibmappnNodeLsDlsEntry,_q:ibmappnNodeLsDlsName,'ibmappnNodeLsDlsState':ibmappnNodeLsDlsState,'ibmappnNodeLsLocalDlsMac':ibmappnNodeLsLocalDlsMac,'ibmappnNodeLsLocalDlsSap':ibmappnNodeLsLocalDlsSap,'ibmappnNodeLsRemoteDlsMac':ibmappnNodeLsRemoteDlsMac,'ibmappnNodeLsRemoteDlsSap':ibmappnNodeLsRemoteDlsSap,'ibmappnNodeLsTrTable':ibmappnNodeLsTrTable,'ibmappnNodeLsTrEntry':ibmappnNodeLsTrEntry,_r:ibmappnNodeLsTrName,'ibmappnNodeLsTrState':ibmappnNodeLsTrState,'ibmappnNodeLsLocalTrMac':ibmappnNodeLsLocalTrMac,'ibmappnNodeLsLocalTrSap':ibmappnNodeLsLocalTrSap,'ibmappnNodeLsRemoteTrMac':ibmappnNodeLsRemoteTrMac,'ibmappnNodeLsRemoteTrSap':ibmappnNodeLsRemoteTrSap,'ibmappnNodeLsStatusTable':ibmappnNodeLsStatusTable,'ibmappnNodeLsStatusEntry':ibmappnNodeLsStatusEntry,_s:ibmappnNodeLsStatusIndex,'ibmappnNodeLsStatusTime':ibmappnNodeLsStatusTime,'ibmappnNodeLsStatusLsName':ibmappnNodeLsStatusLsName,'ibmappnNodeLsStatusCpName':ibmappnNodeLsStatusCpName,'ibmappnNodeLsStatusNodeId':ibmappnNodeLsStatusNodeId,'ibmappnNodeLsStatusTgNum':ibmappnNodeLsStatusTgNum,'ibmappnNodeLsStatusGeneralSense':ibmappnNodeLsStatusGeneralSense,'ibmappnNodeLsStatusNofRetry':ibmappnNodeLsStatusNofRetry,'ibmappnNodeLsStatusEndSense':ibmappnNodeLsStatusEndSense,'ibmappnNodeLsStatusXidLocalSense':ibmappnNodeLsStatusXidLocalSense,'ibmappnNodeLsStatusXidRemoteSense':ibmappnNodeLsStatusXidRemoteSense,'ibmappnNodeLsStatusXidByteInError':ibmappnNodeLsStatusXidByteInError,'ibmappnNodeLsStatusXidBitInError':ibmappnNodeLsStatusXidBitInError,'ibmappnNodeLsStatusDlcType':ibmappnNodeLsStatusDlcType,'ibmappnNodeLsStatusLocalAddr':ibmappnNodeLsStatusLocalAddr,'ibmappnNodeLsStatusRemoteAddr':ibmappnNodeLsStatusRemoteAddr,'ibmappnSnmpInformation':ibmappnSnmpInformation,'ibmappnSnmpInPkts':ibmappnSnmpInPkts,'ibmappnSnmpInGetRequests':ibmappnSnmpInGetRequests,'ibmappnSnmpInGetNexts':ibmappnSnmpInGetNexts,'ibmappnSnmpInSetRequests':ibmappnSnmpInSetRequests,'ibmappnSnmpInTotalVars':ibmappnSnmpInTotalVars,'ibmappnSnmpInGetVars':ibmappnSnmpInGetVars,'ibmappnSnmpInGetNextVars':ibmappnSnmpInGetNextVars,'ibmappnSnmpInSetVars':ibmappnSnmpInSetVars,'ibmappnSnmpOutNoSuchNames':ibmappnSnmpOutNoSuchNames,'ibmappnSnmpOutGenErrs':ibmappnSnmpOutGenErrs,'ibmappnMemoryUse':ibmappnMemoryUse,'ibmappnMemorySize':ibmappnMemorySize,'ibmappnMemoryUsed':ibmappnMemoryUsed,'ibmappnMemoryWarnThresh':ibmappnMemoryWarnThresh,'ibmappnMemoryCritThresh':ibmappnMemoryCritThresh,'ibmappnXidInformation':ibmappnXidInformation,'ibmappnNodeDefLsGoodXids':ibmappnNodeDefLsGoodXids,'ibmappnNodeDefLsBadXids':ibmappnNodeDefLsBadXids,'ibmappnNodeDynLsGoodXids':ibmappnNodeDynLsGoodXids,'ibmappnNodeDynLsBadXids':ibmappnNodeDynLsBadXids,'ibmappnNn':ibmappnNn,'ibmappnNnTopo':ibmappnNnTopo,'ibmappnNnTopoMaxNodes':ibmappnNnTopoMaxNodes,'ibmappnNnTopoCurNumNodes':ibmappnNnTopoCurNumNodes,'ibmappnNnTopoInTdus':ibmappnNnTopoInTdus,'ibmappnNnTopoOutTdus':ibmappnNnTopoOutTdus,'ibmappnNnTopoNodeLowRsns':ibmappnNnTopoNodeLowRsns,'ibmappnNnTopoNodeEqualRsns':ibmappnNnTopoNodeEqualRsns,'ibmappnNnTopoNodeGoodHighRsns':ibmappnNnTopoNodeGoodHighRsns,'ibmappnNnTopoNodeBadHighRsns':ibmappnNnTopoNodeBadHighRsns,'ibmappnNnTopoNodeStateUpdates':ibmappnNnTopoNodeStateUpdates,'ibmappnNnTopoNodeErrors':ibmappnNnTopoNodeErrors,'ibmappnNnTopoNodeTimerUpdates':ibmappnNnTopoNodeTimerUpdates,'ibmappnNnTopoNodePurges':ibmappnNnTopoNodePurges,'ibmappnNnTopoTgLowRsns':ibmappnNnTopoTgLowRsns,'ibmappnNnTopoTgEqualRsns':ibmappnNnTopoTgEqualRsns,'ibmappnNnTopoTgGoodHighRsns':ibmappnNnTopoTgGoodHighRsns,'ibmappnNnTopoTgBadHighRsns':ibmappnNnTopoTgBadHighRsns,'ibmappnNnTopoTgStateUpdates':ibmappnNnTopoTgStateUpdates,'ibmappnNnTopoTgErrors':ibmappnNnTopoTgErrors,'ibmappnNnTopoTgTimerUpdates':ibmappnNnTopoTgTimerUpdates,'ibmappnNnTopoTgPurges':ibmappnNnTopoTgPurges,'ibmappnNnTopoTotalRouteCalcs':ibmappnNnTopoTotalRouteCalcs,'ibmappnNnTopoTotalRouteRejs':ibmappnNnTopoTotalRouteRejs,'ibmappnNnTopoRouteTable':ibmappnNnTopoRouteTable,'ibmappnNnTopoRouteEntry':ibmappnNnTopoRouteEntry,_t:ibmappnNnTopoRouteCos,'ibmappnNnTopoRouteTrees':ibmappnNnTopoRouteTrees,'ibmappnNnTopoRouteCalcs':ibmappnNnTopoRouteCalcs,'ibmappnNnTopoRouteRejs':ibmappnNnTopoRouteRejs,'ibmappnNnAdjNodeTable':ibmappnNnAdjNodeTable,'ibmappnNnAdjNodeEntry':ibmappnNnAdjNodeEntry,_u:ibmappnNnAdjNodeAdjName,'ibmappnNnAdjNodeCpCpSessStatus':ibmappnNnAdjNodeCpCpSessStatus,'ibmappnNnAdjNodeOutOfSeqTdus':ibmappnNnAdjNodeOutOfSeqTdus,'ibmappnNnAdjNodeLastFrsnSent':ibmappnNnAdjNodeLastFrsnSent,'ibmappnNnAdjNodeLastFrsnRcvd':ibmappnNnAdjNodeLastFrsnRcvd,'ibmappnNnTopology':ibmappnNnTopology,'ibmappnNnTopologyTable':ibmappnNnTopologyTable,'ibmappnNnTopologyEntry':ibmappnNnTopologyEntry,_v:ibmappnNnNodeName,'ibmappnNnNodeFrsn':ibmappnNnNodeFrsn,'ibmappnNnNodeEntryTimeLeft':ibmappnNnNodeEntryTimeLeft,'ibmappnNnNodeType':ibmappnNnNodeType,'ibmappnNnNodeRsn':ibmappnNnNodeRsn,'ibmappnNnNodeRouteAddResist':ibmappnNnNodeRouteAddResist,'ibmappnNnNodeCongested':ibmappnNnNodeCongested,'ibmappnNnNodeIsrDepleted':ibmappnNnNodeIsrDepleted,'ibmappnNnNodeEndptDepleted':ibmappnNnNodeEndptDepleted,'ibmappnNnNodeQuiescing':ibmappnNnNodeQuiescing,'ibmappnNnNodeGateway':ibmappnNnNodeGateway,'ibmappnNnNodeCentralDirectory':ibmappnNnNodeCentralDirectory,'ibmappnNnNodeIsr':ibmappnNnNodeIsr,'ibmappnNnNodeChainSupport':ibmappnNnNodeChainSupport,'ibmappnNnTgTopologyTable':ibmappnNnTgTopologyTable,'ibmappnNnTgTopologyEntry':ibmappnNnTgTopologyEntry,_x:ibmappnNnTgOwner,_y:ibmappnNnTgDest,_z:ibmappnNnTgNum,'ibmappnNnTgFrsn':ibmappnNnTgFrsn,'ibmappnNnTgEntryTimeLeft':ibmappnNnTgEntryTimeLeft,'ibmappnNnTgDestVirtual':ibmappnNnTgDestVirtual,'ibmappnNnTgDlcData':ibmappnNnTgDlcData,'ibmappnNnTgRsn':ibmappnNnTgRsn,'ibmappnNnTgOperational':ibmappnNnTgOperational,'ibmappnNnTgQuiescing':ibmappnNnTgQuiescing,'ibmappnNnTgCpCpSession':ibmappnNnTgCpCpSession,'ibmappnNnTgEffCap':ibmappnNnTgEffCap,'ibmappnNnTgConnCost':ibmappnNnTgConnCost,'ibmappnNnTgByteCost':ibmappnNnTgByteCost,'ibmappnNnTgSecurity':ibmappnNnTgSecurity,'ibmappnNnTgDelay':ibmappnNnTgDelay,'ibmappnNnTgModemClass':ibmappnNnTgModemClass,'ibmappnNnTgUsr1':ibmappnNnTgUsr1,'ibmappnNnTgUsr2':ibmappnNnTgUsr2,'ibmappnNnTgUsr3':ibmappnNnTgUsr3,'ibmappnNnTopologyFRTable':ibmappnNnTopologyFRTable,'ibmappnNnTopologyFREntry':ibmappnNnTopologyFREntry,_A1:ibmappnNnNodeFRName,_A0:ibmappnNnNodeFRFrsn,'ibmappnNnNodeFREntryTimeLeft':ibmappnNnNodeFREntryTimeLeft,'ibmappnNnNodeFRType':ibmappnNnNodeFRType,'ibmappnNnNodeFRRsn':ibmappnNnNodeFRRsn,'ibmappnNnNodeFRRouteAddResist':ibmappnNnNodeFRRouteAddResist,'ibmappnNnNodeFRCongested':ibmappnNnNodeFRCongested,'ibmappnNnNodeFRIsrDepleted':ibmappnNnNodeFRIsrDepleted,'ibmappnNnNodeFREndptDepleted':ibmappnNnNodeFREndptDepleted,'ibmappnNnNodeFRQuiescing':ibmappnNnNodeFRQuiescing,'ibmappnNnNodeFRGateway':ibmappnNnNodeFRGateway,'ibmappnNnNodeFRCentralDirectory':ibmappnNnNodeFRCentralDirectory,'ibmappnNnNodeFRIsr':ibmappnNnNodeFRIsr,'ibmappnNnNodeFRChainSupport':ibmappnNnNodeFRChainSupport,'ibmappnNnTgTopologyFRTable':ibmappnNnTgTopologyFRTable,'ibmappnNnTgTopologyFREntry':ibmappnNnTgTopologyFREntry,_A3:ibmappnNnTgFROwner,_A4:ibmappnNnTgFRDest,_A5:ibmappnNnTgFRNum,_A2:ibmappnNnTgFRFrsn,'ibmappnNnTgFREntryTimeLeft':ibmappnNnTgFREntryTimeLeft,'ibmappnNnTgFRDestVirtual':ibmappnNnTgFRDestVirtual,'ibmappnNnTgFRDlcData':ibmappnNnTgFRDlcData,'ibmappnNnTgFRRsn':ibmappnNnTgFRRsn,'ibmappnNnTgFROperational':ibmappnNnTgFROperational,'ibmappnNnTgFRQuiescing':ibmappnNnTgFRQuiescing,'ibmappnNnTgFRCpCpSession':ibmappnNnTgFRCpCpSession,'ibmappnNnTgFREffCap':ibmappnNnTgFREffCap,'ibmappnNnTgFRConnCost':ibmappnNnTgFRConnCost,'ibmappnNnTgFRByteCost':ibmappnNnTgFRByteCost,'ibmappnNnTgFRSecurity':ibmappnNnTgFRSecurity,'ibmappnNnTgFRDelay':ibmappnNnTgFRDelay,'ibmappnNnTgFRModemClass':ibmappnNnTgFRModemClass,'ibmappnNnTgFRUsr1':ibmappnNnTgFRUsr1,'ibmappnNnTgFRUsr2':ibmappnNnTgFRUsr2,'ibmappnNnTgFRUsr3':ibmappnNnTgFRUsr3,'ibmappnLocalTopology':ibmappnLocalTopology,'ibmappnLocalThisNode':ibmappnLocalThisNode,'ibmappnLocalGeneral':ibmappnLocalGeneral,'ibmappnLocalNodeName':ibmappnLocalNodeName,'ibmappnLocalNodeType':ibmappnLocalNodeType,'ibmappnLocalNnSpecific':ibmappnLocalNnSpecific,'ibmappnLocalNnRsn':ibmappnLocalNnRsn,'ibmappnLocalNnRouteAddResist':ibmappnLocalNnRouteAddResist,'ibmappnLocalNnCongested':ibmappnLocalNnCongested,'ibmappnLocalNnIsrDepleted':ibmappnLocalNnIsrDepleted,'ibmappnLocalNnEndptDepleted':ibmappnLocalNnEndptDepleted,'ibmappnLocalNnQuiescing':ibmappnLocalNnQuiescing,'ibmappnLocalNnGateway':ibmappnLocalNnGateway,'ibmappnLocalNnCentralDirectory':ibmappnLocalNnCentralDirectory,'ibmappnLocalNnIsr':ibmappnLocalNnIsr,'ibmappnLocalNnChainSupport':ibmappnLocalNnChainSupport,'ibmappnLocalNnFrsn':ibmappnLocalNnFrsn,'ibmappnLocalTg':ibmappnLocalTg,'ibmappnLocalTgTable':ibmappnLocalTgTable,'ibmappnLocalTgEntry':ibmappnLocalTgEntry,_A6:ibmappnLocalTgDest,_A7:ibmappnLocalTgNum,'ibmappnLocalTgDestVirtual':ibmappnLocalTgDestVirtual,'ibmappnLocalTgDlcData':ibmappnLocalTgDlcData,'ibmappnLocalTgRsn':ibmappnLocalTgRsn,'ibmappnLocalTgQuiescing':ibmappnLocalTgQuiescing,'ibmappnLocalTgOperational':ibmappnLocalTgOperational,'ibmappnLocalTgCpCpSession':ibmappnLocalTgCpCpSession,'ibmappnLocalTgEffCap':ibmappnLocalTgEffCap,'ibmappnLocalTgConnCost':ibmappnLocalTgConnCost,'ibmappnLocalTgByteCost':ibmappnLocalTgByteCost,'ibmappnLocalTgSecurity':ibmappnLocalTgSecurity,'ibmappnLocalTgDelay':ibmappnLocalTgDelay,'ibmappnLocalTgModemClass':ibmappnLocalTgModemClass,'ibmappnLocalTgUsr1':ibmappnLocalTgUsr1,'ibmappnLocalTgUsr2':ibmappnLocalTgUsr2,'ibmappnLocalTgUsr3':ibmappnLocalTgUsr3,'ibmappnLocalEnTopology':ibmappnLocalEnTopology,'ibmappnLocalEnTable':ibmappnLocalEnTable,'ibmappnLocalEnEntry':ibmappnLocalEnEntry,_A8:ibmappnLocalEnName,'ibmappnLocalEnEntryTimeLeft':ibmappnLocalEnEntryTimeLeft,'ibmappnLocalEnType':ibmappnLocalEnType,'ibmappnLocalEnTgTable':ibmappnLocalEnTgTable,'ibmappnLocalEnTgEntry':ibmappnLocalEnTgEntry,_A9:ibmappnLocalEnTgOrigin,_AA:ibmappnLocalEnTgDest,_AB:ibmappnLocalEnTgNum,'ibmappnLocalEnTgEntryTimeLeft':ibmappnLocalEnTgEntryTimeLeft,'ibmappnLocalEnTgDestVirtual':ibmappnLocalEnTgDestVirtual,'ibmappnLocalEnTgDlcData':ibmappnLocalEnTgDlcData,'ibmappnLocalEnTgOperational':ibmappnLocalEnTgOperational,'ibmappnLocalEnTgCpCpSession':ibmappnLocalEnTgCpCpSession,'ibmappnLocalEnTgEffCap':ibmappnLocalEnTgEffCap,'ibmappnLocalEnTgConnCost':ibmappnLocalEnTgConnCost,'ibmappnLocalEnTgByteCost':ibmappnLocalEnTgByteCost,'ibmappnLocalEnTgSecurity':ibmappnLocalEnTgSecurity,'ibmappnLocalEnTgDelay':ibmappnLocalEnTgDelay,'ibmappnLocalEnTgModemClass':ibmappnLocalEnTgModemClass,'ibmappnLocalEnTgUsr1':ibmappnLocalEnTgUsr1,'ibmappnLocalEnTgUsr2':ibmappnLocalEnTgUsr2,'ibmappnLocalEnTgUsr3':ibmappnLocalEnTgUsr3,'ibmappnDir':ibmappnDir,'ibmappnDirPerf':ibmappnDirPerf,'ibmappnDirMaxCaches':ibmappnDirMaxCaches,'ibmappnDirCurCaches':ibmappnDirCurCaches,'ibmappnDirCurHomeEntries':ibmappnDirCurHomeEntries,'ibmappnDirRegEntries':ibmappnDirRegEntries,'ibmappnDirInLocates':ibmappnDirInLocates,'ibmappnDirInBcastLocates':ibmappnDirInBcastLocates,'ibmappnDirOutLocates':ibmappnDirOutLocates,'ibmappnDirOutBcastLocates':ibmappnDirOutBcastLocates,'ibmappnDirNotFoundLocates':ibmappnDirNotFoundLocates,'ibmappnDirNotFoundBcastLocates':ibmappnDirNotFoundBcastLocates,'ibmappnDirLocateOutstands':ibmappnDirLocateOutstands,'ibmappnDirTable':ibmappnDirTable,'ibmappnDirEntry':ibmappnDirEntry,_AC:ibmappnDirLuName,'ibmappnDirServerName':ibmappnDirServerName,'ibmappnDirLuOwnerName':ibmappnDirLuOwnerName,'ibmappnDirLuLocation':ibmappnDirLuLocation,'ibmappnDirType':ibmappnDirType,'ibmappnDirWildCard':ibmappnDirWildCard,'ibmappnCos':ibmappnCos,'ibmappnCosModeTable':ibmappnCosModeTable,'ibmappnCosModeEntry':ibmappnCosModeEntry,_AD:ibmappnCosModeName,'ibmappnCosModeCosName':ibmappnCosModeCosName,'ibmappnCosNameTable':ibmappnCosNameTable,'ibmappnCosNameEntry':ibmappnCosNameEntry,_AE:ibmappnCosName,'ibmappnCosTransPriority':ibmappnCosTransPriority,'ibmappnCosNodeRowTable':ibmappnCosNodeRowTable,'ibmappnCosNodeRowEntry':ibmappnCosNodeRowEntry,_AF:ibmappnCosNodeRowName,_AG:ibmappnCosNodeRowIndex,'ibmappnCosNodeRowWgt':ibmappnCosNodeRowWgt,'ibmappnCosNodeRowResistMin':ibmappnCosNodeRowResistMin,'ibmappnCosNodeRowResistMax':ibmappnCosNodeRowResistMax,'ibmappnCosNodeRowMinCongestAllow':ibmappnCosNodeRowMinCongestAllow,'ibmappnCosNodeRowMaxCongestAllow':ibmappnCosNodeRowMaxCongestAllow,'ibmappnCosTgRowTable':ibmappnCosTgRowTable,'ibmappnCosTgRowEntry':ibmappnCosTgRowEntry,_AH:ibmappnCosTgRowName,_AI:ibmappnCosTgRowIndex,'ibmappnCosTgRowWgt':ibmappnCosTgRowWgt,'ibmappnCosTgRowEffCapMin':ibmappnCosTgRowEffCapMin,'ibmappnCosTgRowEffCapMax':ibmappnCosTgRowEffCapMax,'ibmappnCosTgRowConnCostMin':ibmappnCosTgRowConnCostMin,'ibmappnCosTgRowConnCostMax':ibmappnCosTgRowConnCostMax,'ibmappnCosTgRowByteCostMin':ibmappnCosTgRowByteCostMin,'ibmappnCosTgRowByteCostMax':ibmappnCosTgRowByteCostMax,'ibmappnCosTgRowSecurityMin':ibmappnCosTgRowSecurityMin,'ibmappnCosTgRowSecurityMax':ibmappnCosTgRowSecurityMax,'ibmappnCosTgRowDelayMin':ibmappnCosTgRowDelayMin,'ibmappnCosTgRowDelayMax':ibmappnCosTgRowDelayMax,'ibmappnCosTgRowUsr1Min':ibmappnCosTgRowUsr1Min,'ibmappnCosTgRowUsr1Max':ibmappnCosTgRowUsr1Max,'ibmappnCosTgRowUsr2Min':ibmappnCosTgRowUsr2Min,'ibmappnCosTgRowUsr2Max':ibmappnCosTgRowUsr2Max,'ibmappnCosTgRowUsr3Min':ibmappnCosTgRowUsr3Min,'ibmappnCosTgRowUsr3Max':ibmappnCosTgRowUsr3Max})