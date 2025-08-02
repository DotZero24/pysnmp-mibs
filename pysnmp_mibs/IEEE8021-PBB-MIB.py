_AN='ieee8021PbbVipPbbTeGroup'
_AM='ieee8021PbbVipEnableConnectionId'
_AL='ieee8021PbbCbpRowStatus'
_AK='ieee8021PbbCBPServiceMappingRowStatus'
_AJ='ieee8021PbbCBPServiceMappingLocalSid'
_AI='ieee8021PbbCBPServiceMappingType'
_AH='ieee8021PbbCBPServiceMappingDefaultBackboneDest'
_AG='ieee8021PbbCBPServiceMappingBVid'
_AF='ieee8021PbbVipToPipMappingRowStatus'
_AE='ieee8021PbbVipToPipMappingStorageType'
_AD='ieee8021PbbVipToPipMappingPipIfIndex'
_AC='ieee8021PbbPipEncodingPriority'
_AB='ieee8021PbbPipDecodingDropEligible'
_AA='ieee8021PbbPipDecodingPriority'
_A9='ieee8021PbbPipRequireDropEncoding'
_A8='ieee8021PbbPipUseDEI'
_A7='ieee8021PbbPipPriorityCodePointSelection'
_A6='ieee8021PbbPipRowStatus'
_A5='ieee8021PbbPipVipMap4'
_A4='ieee8021PbbPipVipMap3'
_A3='ieee8021PbbPipVipMap2'
_A2='ieee8021PbbPipVipMap1'
_A1='ieee8021PbbPipVipMap'
_A0='ieee8021PbbPipIComponentId'
_z='ieee8021PbbPipName'
_y='ieee8021PbbPipBMACAddress'
_x='ieee8021PbbNextAvailablePipIfIndex'
_w='ieee8021PbbISidToVipPort'
_v='ieee8021PbbISidToVipComponentId'
_u='ieee8021PbbVipRowStatus'
_t='ieee8021PbbVipType'
_s='ieee8021PbbVipDefaultDstBMAC'
_r='ieee8021PbbVipISid'
_q='ieee8021PbbVipPipIfIndex'
_p='ieee8021PbbNumberOfBebPorts'
_o='ieee8021PbbNumberOfBComponents'
_n='ieee8021PbbNumberOfIComponents'
_m='ieee8021PbbBackboneEdgeBridgeName'
_l='ieee8021PbbBackboneEdgeBridgeAddress'
_k='ieee8021PbbPipPriorityEntry'
_j='ieee8021PbbCBPServiceMappingBackboneSid'
_i='ieee8021PbbPipEncodingDropEligible'
_h='ieee8021PbbPipEncodingPriorityCodePoint'
_g='ieee8021PbbPipEncodingPriorityCodePointRow'
_f='ieee8021PbbPipDecodingPriorityCodePoint'
_e='ieee8021PbbPipDecodingPriorityCodePointRow'
_d='ieee8021PbbISidToVipISid'
_c='deprecated'
_b='MacAddress'
_a='Unsigned32'
_Z='InterfaceIndexOrZero'
_Y='IEEE8021PbbIngressEgress'
_X='ieee8021PbbPipEncodingGroup'
_W='ieee8021PbbPipDecodingGroup'
_V='ieee8021PbbDefaultPriorityGroup'
_U='ieee8021PbbDynamicCbpGroup'
_T='ieee8021PbbCBPServiceMappingGroup'
_S='ieee8021PbbVipToPipMappingGroup'
_R='ieee8021PbbPipGroup'
_Q='ieee8021PbbVipGroup'
_P='ieee8021PbbBackboneEdgeBridgeGroup'
_O='TruthValue'
_N='Integer32'
_M='SnmpAdminString'
_L='IEEE8021PbbServiceIdentifierOrUnassigned'
_K='ieee8021PbbPipIfIndex'
_J='ieee8021BridgeBasePortComponentId'
_I='ieee8021BridgeBasePort'
_H='OctetString'
_G='not-accessible'
_F='read-write'
_E='IEEE8021-BRIDGE-MIB'
_D='read-only'
_C='read-create'
_B='IEEE8021-PBB-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ieee8021BridgeBasePort,ieee8021BridgeBasePortComponentId=mibBuilder.importSymbols(_E,_I,_J)
IEEE8021BridgePortNumber,IEEE8021PbbComponentIdentifier,IEEE8021PbbIngressEgress,IEEE8021PbbServiceIdentifier,IEEE8021PbbServiceIdentifierOrUnassigned,IEEE8021PriorityCodePoint,IEEE8021PriorityValue,ieee802dot1mibs=mibBuilder.importSymbols('IEEE8021-TC-MIB','IEEE8021BridgePortNumber','IEEE8021PbbComponentIdentifier',_Y,'IEEE8021PbbServiceIdentifier',_L,'IEEE8021PriorityCodePoint','IEEE8021PriorityValue','ieee802dot1mibs')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex',_Z)
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_N,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_a,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_b,'PhysAddress','RowStatus','StorageType','TextualConvention',_O)
ieee8021PbbMib=ModuleIdentity((1,3,111,2,802,1,1,9))
if mibBuilder.loadTexts:ieee8021PbbMib.setRevisions(('2018-06-28 00:00','2014-12-15 00:00','2011-02-27 00:00','2008-11-18 00:00','2008-10-15 00:00'))
_Ieee8021PbbNotifications_ObjectIdentity=ObjectIdentity
ieee8021PbbNotifications=_Ieee8021PbbNotifications_ObjectIdentity((1,3,111,2,802,1,1,9,0))
_Ieee8021PbbObjects_ObjectIdentity=ObjectIdentity
ieee8021PbbObjects=_Ieee8021PbbObjects_ObjectIdentity((1,3,111,2,802,1,1,9,1))
_Ieee8021PbbProviderBackboneBridge_ObjectIdentity=ObjectIdentity
ieee8021PbbProviderBackboneBridge=_Ieee8021PbbProviderBackboneBridge_ObjectIdentity((1,3,111,2,802,1,1,9,1,1))
_Ieee8021PbbBackboneEdgeBridgeObjects_ObjectIdentity=ObjectIdentity
ieee8021PbbBackboneEdgeBridgeObjects=_Ieee8021PbbBackboneEdgeBridgeObjects_ObjectIdentity((1,3,111,2,802,1,1,9,1,1,1))
_Ieee8021PbbBackboneEdgeBridgeAddress_Type=MacAddress
_Ieee8021PbbBackboneEdgeBridgeAddress_Object=MibScalar
ieee8021PbbBackboneEdgeBridgeAddress=_Ieee8021PbbBackboneEdgeBridgeAddress_Object((1,3,111,2,802,1,1,9,1,1,1,1),_Ieee8021PbbBackboneEdgeBridgeAddress_Type())
ieee8021PbbBackboneEdgeBridgeAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021PbbBackboneEdgeBridgeAddress.setStatus(_A)
class _Ieee8021PbbBackboneEdgeBridgeName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Ieee8021PbbBackboneEdgeBridgeName_Type.__name__=_M
_Ieee8021PbbBackboneEdgeBridgeName_Object=MibScalar
ieee8021PbbBackboneEdgeBridgeName=_Ieee8021PbbBackboneEdgeBridgeName_Object((1,3,111,2,802,1,1,9,1,1,1,2),_Ieee8021PbbBackboneEdgeBridgeName_Type())
ieee8021PbbBackboneEdgeBridgeName.setMaxAccess(_F)
if mibBuilder.loadTexts:ieee8021PbbBackboneEdgeBridgeName.setStatus(_A)
_Ieee8021PbbNumberOfIComponents_Type=Unsigned32
_Ieee8021PbbNumberOfIComponents_Object=MibScalar
ieee8021PbbNumberOfIComponents=_Ieee8021PbbNumberOfIComponents_Object((1,3,111,2,802,1,1,9,1,1,1,3),_Ieee8021PbbNumberOfIComponents_Type())
ieee8021PbbNumberOfIComponents.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021PbbNumberOfIComponents.setStatus(_A)
class _Ieee8021PbbNumberOfBComponents_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Ieee8021PbbNumberOfBComponents_Type.__name__=_a
_Ieee8021PbbNumberOfBComponents_Object=MibScalar
ieee8021PbbNumberOfBComponents=_Ieee8021PbbNumberOfBComponents_Object((1,3,111,2,802,1,1,9,1,1,1,4),_Ieee8021PbbNumberOfBComponents_Type())
ieee8021PbbNumberOfBComponents.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021PbbNumberOfBComponents.setStatus(_A)
_Ieee8021PbbNumberOfBebPorts_Type=Unsigned32
_Ieee8021PbbNumberOfBebPorts_Object=MibScalar
ieee8021PbbNumberOfBebPorts=_Ieee8021PbbNumberOfBebPorts_Object((1,3,111,2,802,1,1,9,1,1,1,5),_Ieee8021PbbNumberOfBebPorts_Type())
ieee8021PbbNumberOfBebPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021PbbNumberOfBebPorts.setStatus(_A)
_Ieee8021PbbNextAvailablePipIfIndex_Type=InterfaceIndex
_Ieee8021PbbNextAvailablePipIfIndex_Object=MibScalar
ieee8021PbbNextAvailablePipIfIndex=_Ieee8021PbbNextAvailablePipIfIndex_Object((1,3,111,2,802,1,1,9,1,1,1,6),_Ieee8021PbbNextAvailablePipIfIndex_Type())
ieee8021PbbNextAvailablePipIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021PbbNextAvailablePipIfIndex.setStatus(_A)
_Ieee8021PbbVipTable_Object=MibTable
ieee8021PbbVipTable=_Ieee8021PbbVipTable_Object((1,3,111,2,802,1,1,9,1,1,2))
if mibBuilder.loadTexts:ieee8021PbbVipTable.setStatus(_A)
_Ieee8021PbbVipEntry_Object=MibTableRow
ieee8021PbbVipEntry=_Ieee8021PbbVipEntry_Object((1,3,111,2,802,1,1,9,1,1,2,1))
ieee8021PbbVipEntry.setIndexNames((0,_E,_J),(0,_E,_I))
if mibBuilder.loadTexts:ieee8021PbbVipEntry.setStatus(_A)
class _Ieee8021PbbVipPipIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_Ieee8021PbbVipPipIfIndex_Type.__name__=_Z
_Ieee8021PbbVipPipIfIndex_Object=MibTableColumn
ieee8021PbbVipPipIfIndex=_Ieee8021PbbVipPipIfIndex_Object((1,3,111,2,802,1,1,9,1,1,2,1,1),_Ieee8021PbbVipPipIfIndex_Type())
ieee8021PbbVipPipIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021PbbVipPipIfIndex.setStatus(_A)
class _Ieee8021PbbVipISid_Type(IEEE8021PbbServiceIdentifierOrUnassigned):defaultValue=1
_Ieee8021PbbVipISid_Type.__name__=_L
_Ieee8021PbbVipISid_Object=MibTableColumn
ieee8021PbbVipISid=_Ieee8021PbbVipISid_Object((1,3,111,2,802,1,1,9,1,1,2,1,2),_Ieee8021PbbVipISid_Type())
ieee8021PbbVipISid.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021PbbVipISid.setStatus(_A)
class _Ieee8021PbbVipDefaultDstBMAC_Type(MacAddress):defaultHexValue='001e83000001'
_Ieee8021PbbVipDefaultDstBMAC_Type.__name__=_b
_Ieee8021PbbVipDefaultDstBMAC_Object=MibTableColumn
ieee8021PbbVipDefaultDstBMAC=_Ieee8021PbbVipDefaultDstBMAC_Object((1,3,111,2,802,1,1,9,1,1,2,1,3),_Ieee8021PbbVipDefaultDstBMAC_Type())
ieee8021PbbVipDefaultDstBMAC.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021PbbVipDefaultDstBMAC.setStatus(_A)
class _Ieee8021PbbVipType_Type(IEEE8021PbbIngressEgress):defaultBinValue='11'
_Ieee8021PbbVipType_Type.__name__=_Y
_Ieee8021PbbVipType_Object=MibTableColumn
ieee8021PbbVipType=_Ieee8021PbbVipType_Object((1,3,111,2,802,1,1,9,1,1,2,1,4),_Ieee8021PbbVipType_Type())
ieee8021PbbVipType.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021PbbVipType.setStatus(_c)
_Ieee8021PbbVipRowStatus_Type=RowStatus
_Ieee8021PbbVipRowStatus_Object=MibTableColumn
ieee8021PbbVipRowStatus=_Ieee8021PbbVipRowStatus_Object((1,3,111,2,802,1,1,9,1,1,2,1,5),_Ieee8021PbbVipRowStatus_Type())
ieee8021PbbVipRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021PbbVipRowStatus.setStatus(_A)
class _Ieee8021PbbVipEnableConnectionId_Type(TruthValue):defaultValue=1
_Ieee8021PbbVipEnableConnectionId_Type.__name__=_O
_Ieee8021PbbVipEnableConnectionId_Object=MibTableColumn
ieee8021PbbVipEnableConnectionId=_Ieee8021PbbVipEnableConnectionId_Object((1,3,111,2,802,1,1,9,1,1,2,1,6),_Ieee8021PbbVipEnableConnectionId_Type())
ieee8021PbbVipEnableConnectionId.setMaxAccess(_F)
if mibBuilder.loadTexts:ieee8021PbbVipEnableConnectionId.setStatus(_A)
_Ieee8021PbbISidToVipTable_Object=MibTable
ieee8021PbbISidToVipTable=_Ieee8021PbbISidToVipTable_Object((1,3,111,2,802,1,1,9,1,1,3))
if mibBuilder.loadTexts:ieee8021PbbISidToVipTable.setStatus(_A)
_Ieee8021PbbISidToVipEntry_Object=MibTableRow
ieee8021PbbISidToVipEntry=_Ieee8021PbbISidToVipEntry_Object((1,3,111,2,802,1,1,9,1,1,3,1))
ieee8021PbbISidToVipEntry.setIndexNames((0,_B,_d))
if mibBuilder.loadTexts:ieee8021PbbISidToVipEntry.setStatus(_A)
_Ieee8021PbbISidToVipISid_Type=IEEE8021PbbServiceIdentifier
_Ieee8021PbbISidToVipISid_Object=MibTableColumn
ieee8021PbbISidToVipISid=_Ieee8021PbbISidToVipISid_Object((1,3,111,2,802,1,1,9,1,1,3,1,1),_Ieee8021PbbISidToVipISid_Type())
ieee8021PbbISidToVipISid.setMaxAccess(_G)
if mibBuilder.loadTexts:ieee8021PbbISidToVipISid.setStatus(_A)
_Ieee8021PbbISidToVipComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021PbbISidToVipComponentId_Object=MibTableColumn
ieee8021PbbISidToVipComponentId=_Ieee8021PbbISidToVipComponentId_Object((1,3,111,2,802,1,1,9,1,1,3,1,2),_Ieee8021PbbISidToVipComponentId_Type())
ieee8021PbbISidToVipComponentId.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021PbbISidToVipComponentId.setStatus(_A)
_Ieee8021PbbISidToVipPort_Type=IEEE8021BridgePortNumber
_Ieee8021PbbISidToVipPort_Object=MibTableColumn
ieee8021PbbISidToVipPort=_Ieee8021PbbISidToVipPort_Object((1,3,111,2,802,1,1,9,1,1,3,1,3),_Ieee8021PbbISidToVipPort_Type())
ieee8021PbbISidToVipPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021PbbISidToVipPort.setStatus(_A)
_Ieee8021PbbPipTable_Object=MibTable
ieee8021PbbPipTable=_Ieee8021PbbPipTable_Object((1,3,111,2,802,1,1,9,1,1,4))
if mibBuilder.loadTexts:ieee8021PbbPipTable.setStatus(_A)
_Ieee8021PbbPipEntry_Object=MibTableRow
ieee8021PbbPipEntry=_Ieee8021PbbPipEntry_Object((1,3,111,2,802,1,1,9,1,1,4,1))
ieee8021PbbPipEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:ieee8021PbbPipEntry.setStatus(_A)
_Ieee8021PbbPipIfIndex_Type=InterfaceIndex
_Ieee8021PbbPipIfIndex_Object=MibTableColumn
ieee8021PbbPipIfIndex=_Ieee8021PbbPipIfIndex_Object((1,3,111,2,802,1,1,9,1,1,4,1,1),_Ieee8021PbbPipIfIndex_Type())
ieee8021PbbPipIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ieee8021PbbPipIfIndex.setStatus(_A)
_Ieee8021PbbPipBMACAddress_Type=MacAddress
_Ieee8021PbbPipBMACAddress_Object=MibTableColumn
ieee8021PbbPipBMACAddress=_Ieee8021PbbPipBMACAddress_Object((1,3,111,2,802,1,1,9,1,1,4,1,2),_Ieee8021PbbPipBMACAddress_Type())
ieee8021PbbPipBMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021PbbPipBMACAddress.setStatus(_A)
class _Ieee8021PbbPipName_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Ieee8021PbbPipName_Type.__name__=_M
_Ieee8021PbbPipName_Object=MibTableColumn
ieee8021PbbPipName=_Ieee8021PbbPipName_Object((1,3,111,2,802,1,1,9,1,1,4,1,3),_Ieee8021PbbPipName_Type())
ieee8021PbbPipName.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021PbbPipName.setStatus(_A)
_Ieee8021PbbPipIComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021PbbPipIComponentId_Object=MibTableColumn
ieee8021PbbPipIComponentId=_Ieee8021PbbPipIComponentId_Object((1,3,111,2,802,1,1,9,1,1,4,1,4),_Ieee8021PbbPipIComponentId_Type())
ieee8021PbbPipIComponentId.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021PbbPipIComponentId.setStatus(_A)
class _Ieee8021PbbPipVipMap_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_Ieee8021PbbPipVipMap_Type.__name__=_H
_Ieee8021PbbPipVipMap_Object=MibTableColumn
ieee8021PbbPipVipMap=_Ieee8021PbbPipVipMap_Object((1,3,111,2,802,1,1,9,1,1,4,1,5),_Ieee8021PbbPipVipMap_Type())
ieee8021PbbPipVipMap.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021PbbPipVipMap.setStatus(_A)
class _Ieee8021PbbPipVipMap1_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2048))
_Ieee8021PbbPipVipMap1_Type.__name__=_H
_Ieee8021PbbPipVipMap1_Object=MibTableColumn
ieee8021PbbPipVipMap1=_Ieee8021PbbPipVipMap1_Object((1,3,111,2,802,1,1,9,1,1,4,1,6),_Ieee8021PbbPipVipMap1_Type())
ieee8021PbbPipVipMap1.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021PbbPipVipMap1.setStatus(_A)
class _Ieee8021PbbPipVipMap2_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2048))
_Ieee8021PbbPipVipMap2_Type.__name__=_H
_Ieee8021PbbPipVipMap2_Object=MibTableColumn
ieee8021PbbPipVipMap2=_Ieee8021PbbPipVipMap2_Object((1,3,111,2,802,1,1,9,1,1,4,1,7),_Ieee8021PbbPipVipMap2_Type())
ieee8021PbbPipVipMap2.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021PbbPipVipMap2.setStatus(_A)
class _Ieee8021PbbPipVipMap3_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2048))
_Ieee8021PbbPipVipMap3_Type.__name__=_H
_Ieee8021PbbPipVipMap3_Object=MibTableColumn
ieee8021PbbPipVipMap3=_Ieee8021PbbPipVipMap3_Object((1,3,111,2,802,1,1,9,1,1,4,1,8),_Ieee8021PbbPipVipMap3_Type())
ieee8021PbbPipVipMap3.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021PbbPipVipMap3.setStatus(_A)
class _Ieee8021PbbPipVipMap4_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1537))
_Ieee8021PbbPipVipMap4_Type.__name__=_H
_Ieee8021PbbPipVipMap4_Object=MibTableColumn
ieee8021PbbPipVipMap4=_Ieee8021PbbPipVipMap4_Object((1,3,111,2,802,1,1,9,1,1,4,1,9),_Ieee8021PbbPipVipMap4_Type())
ieee8021PbbPipVipMap4.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021PbbPipVipMap4.setStatus(_A)
_Ieee8021PbbPipRowStatus_Type=RowStatus
_Ieee8021PbbPipRowStatus_Object=MibTableColumn
ieee8021PbbPipRowStatus=_Ieee8021PbbPipRowStatus_Object((1,3,111,2,802,1,1,9,1,1,4,1,10),_Ieee8021PbbPipRowStatus_Type())
ieee8021PbbPipRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021PbbPipRowStatus.setStatus(_A)
_Ieee8021PbbPipPriorityTable_Object=MibTable
ieee8021PbbPipPriorityTable=_Ieee8021PbbPipPriorityTable_Object((1,3,111,2,802,1,1,9,1,1,5))
if mibBuilder.loadTexts:ieee8021PbbPipPriorityTable.setStatus(_A)
_Ieee8021PbbPipPriorityEntry_Object=MibTableRow
ieee8021PbbPipPriorityEntry=_Ieee8021PbbPipPriorityEntry_Object((1,3,111,2,802,1,1,9,1,1,5,1))
if mibBuilder.loadTexts:ieee8021PbbPipPriorityEntry.setStatus(_A)
_Ieee8021PbbPipPriorityCodePointSelection_Type=IEEE8021PriorityCodePoint
_Ieee8021PbbPipPriorityCodePointSelection_Object=MibTableColumn
ieee8021PbbPipPriorityCodePointSelection=_Ieee8021PbbPipPriorityCodePointSelection_Object((1,3,111,2,802,1,1,9,1,1,5,1,1),_Ieee8021PbbPipPriorityCodePointSelection_Type())
ieee8021PbbPipPriorityCodePointSelection.setMaxAccess(_F)
if mibBuilder.loadTexts:ieee8021PbbPipPriorityCodePointSelection.setStatus(_A)
_Ieee8021PbbPipUseDEI_Type=TruthValue
_Ieee8021PbbPipUseDEI_Object=MibTableColumn
ieee8021PbbPipUseDEI=_Ieee8021PbbPipUseDEI_Object((1,3,111,2,802,1,1,9,1,1,5,1,2),_Ieee8021PbbPipUseDEI_Type())
ieee8021PbbPipUseDEI.setMaxAccess(_F)
if mibBuilder.loadTexts:ieee8021PbbPipUseDEI.setStatus(_A)
class _Ieee8021PbbPipRequireDropEncoding_Type(TruthValue):defaultValue=2
_Ieee8021PbbPipRequireDropEncoding_Type.__name__=_O
_Ieee8021PbbPipRequireDropEncoding_Object=MibTableColumn
ieee8021PbbPipRequireDropEncoding=_Ieee8021PbbPipRequireDropEncoding_Object((1,3,111,2,802,1,1,9,1,1,5,1,3),_Ieee8021PbbPipRequireDropEncoding_Type())
ieee8021PbbPipRequireDropEncoding.setMaxAccess(_F)
if mibBuilder.loadTexts:ieee8021PbbPipRequireDropEncoding.setStatus(_A)
_Ieee8021PbbPipDecodingTable_Object=MibTable
ieee8021PbbPipDecodingTable=_Ieee8021PbbPipDecodingTable_Object((1,3,111,2,802,1,1,9,1,1,6))
if mibBuilder.loadTexts:ieee8021PbbPipDecodingTable.setStatus(_A)
_Ieee8021PbbPipDecodingEntry_Object=MibTableRow
ieee8021PbbPipDecodingEntry=_Ieee8021PbbPipDecodingEntry_Object((1,3,111,2,802,1,1,9,1,1,6,1))
ieee8021PbbPipDecodingEntry.setIndexNames((0,_B,_K),(0,_B,_e),(0,_B,_f))
if mibBuilder.loadTexts:ieee8021PbbPipDecodingEntry.setStatus(_A)
_Ieee8021PbbPipDecodingPriorityCodePointRow_Type=IEEE8021PriorityCodePoint
_Ieee8021PbbPipDecodingPriorityCodePointRow_Object=MibTableColumn
ieee8021PbbPipDecodingPriorityCodePointRow=_Ieee8021PbbPipDecodingPriorityCodePointRow_Object((1,3,111,2,802,1,1,9,1,1,6,1,1),_Ieee8021PbbPipDecodingPriorityCodePointRow_Type())
ieee8021PbbPipDecodingPriorityCodePointRow.setMaxAccess(_G)
if mibBuilder.loadTexts:ieee8021PbbPipDecodingPriorityCodePointRow.setStatus(_A)
class _Ieee8021PbbPipDecodingPriorityCodePoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Ieee8021PbbPipDecodingPriorityCodePoint_Type.__name__=_N
_Ieee8021PbbPipDecodingPriorityCodePoint_Object=MibTableColumn
ieee8021PbbPipDecodingPriorityCodePoint=_Ieee8021PbbPipDecodingPriorityCodePoint_Object((1,3,111,2,802,1,1,9,1,1,6,1,2),_Ieee8021PbbPipDecodingPriorityCodePoint_Type())
ieee8021PbbPipDecodingPriorityCodePoint.setMaxAccess(_G)
if mibBuilder.loadTexts:ieee8021PbbPipDecodingPriorityCodePoint.setStatus(_A)
_Ieee8021PbbPipDecodingPriority_Type=IEEE8021PriorityValue
_Ieee8021PbbPipDecodingPriority_Object=MibTableColumn
ieee8021PbbPipDecodingPriority=_Ieee8021PbbPipDecodingPriority_Object((1,3,111,2,802,1,1,9,1,1,6,1,3),_Ieee8021PbbPipDecodingPriority_Type())
ieee8021PbbPipDecodingPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:ieee8021PbbPipDecodingPriority.setStatus(_A)
_Ieee8021PbbPipDecodingDropEligible_Type=TruthValue
_Ieee8021PbbPipDecodingDropEligible_Object=MibTableColumn
ieee8021PbbPipDecodingDropEligible=_Ieee8021PbbPipDecodingDropEligible_Object((1,3,111,2,802,1,1,9,1,1,6,1,4),_Ieee8021PbbPipDecodingDropEligible_Type())
ieee8021PbbPipDecodingDropEligible.setMaxAccess(_F)
if mibBuilder.loadTexts:ieee8021PbbPipDecodingDropEligible.setStatus(_A)
_Ieee8021PbbPipEncodingTable_Object=MibTable
ieee8021PbbPipEncodingTable=_Ieee8021PbbPipEncodingTable_Object((1,3,111,2,802,1,1,9,1,1,7))
if mibBuilder.loadTexts:ieee8021PbbPipEncodingTable.setStatus(_A)
_Ieee8021PbbPipEncodingEntry_Object=MibTableRow
ieee8021PbbPipEncodingEntry=_Ieee8021PbbPipEncodingEntry_Object((1,3,111,2,802,1,1,9,1,1,7,1))
ieee8021PbbPipEncodingEntry.setIndexNames((0,_B,_K),(0,_B,_g),(0,_B,_h),(0,_B,_i))
if mibBuilder.loadTexts:ieee8021PbbPipEncodingEntry.setStatus(_A)
_Ieee8021PbbPipEncodingPriorityCodePointRow_Type=IEEE8021PriorityCodePoint
_Ieee8021PbbPipEncodingPriorityCodePointRow_Object=MibTableColumn
ieee8021PbbPipEncodingPriorityCodePointRow=_Ieee8021PbbPipEncodingPriorityCodePointRow_Object((1,3,111,2,802,1,1,9,1,1,7,1,1),_Ieee8021PbbPipEncodingPriorityCodePointRow_Type())
ieee8021PbbPipEncodingPriorityCodePointRow.setMaxAccess(_G)
if mibBuilder.loadTexts:ieee8021PbbPipEncodingPriorityCodePointRow.setStatus(_A)
class _Ieee8021PbbPipEncodingPriorityCodePoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Ieee8021PbbPipEncodingPriorityCodePoint_Type.__name__=_N
_Ieee8021PbbPipEncodingPriorityCodePoint_Object=MibTableColumn
ieee8021PbbPipEncodingPriorityCodePoint=_Ieee8021PbbPipEncodingPriorityCodePoint_Object((1,3,111,2,802,1,1,9,1,1,7,1,2),_Ieee8021PbbPipEncodingPriorityCodePoint_Type())
ieee8021PbbPipEncodingPriorityCodePoint.setMaxAccess(_G)
if mibBuilder.loadTexts:ieee8021PbbPipEncodingPriorityCodePoint.setStatus(_A)
_Ieee8021PbbPipEncodingDropEligible_Type=TruthValue
_Ieee8021PbbPipEncodingDropEligible_Object=MibTableColumn
ieee8021PbbPipEncodingDropEligible=_Ieee8021PbbPipEncodingDropEligible_Object((1,3,111,2,802,1,1,9,1,1,7,1,3),_Ieee8021PbbPipEncodingDropEligible_Type())
ieee8021PbbPipEncodingDropEligible.setMaxAccess(_G)
if mibBuilder.loadTexts:ieee8021PbbPipEncodingDropEligible.setStatus(_A)
_Ieee8021PbbPipEncodingPriority_Type=IEEE8021PriorityValue
_Ieee8021PbbPipEncodingPriority_Object=MibTableColumn
ieee8021PbbPipEncodingPriority=_Ieee8021PbbPipEncodingPriority_Object((1,3,111,2,802,1,1,9,1,1,7,1,4),_Ieee8021PbbPipEncodingPriority_Type())
ieee8021PbbPipEncodingPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:ieee8021PbbPipEncodingPriority.setStatus(_A)
_Ieee8021PbbVipToPipMappingTable_Object=MibTable
ieee8021PbbVipToPipMappingTable=_Ieee8021PbbVipToPipMappingTable_Object((1,3,111,2,802,1,1,9,1,1,8))
if mibBuilder.loadTexts:ieee8021PbbVipToPipMappingTable.setStatus(_A)
_Ieee8021PbbVipToPipMappingEntry_Object=MibTableRow
ieee8021PbbVipToPipMappingEntry=_Ieee8021PbbVipToPipMappingEntry_Object((1,3,111,2,802,1,1,9,1,1,8,1))
ieee8021PbbVipToPipMappingEntry.setIndexNames((0,_E,_J),(0,_E,_I))
if mibBuilder.loadTexts:ieee8021PbbVipToPipMappingEntry.setStatus(_A)
_Ieee8021PbbVipToPipMappingPipIfIndex_Type=InterfaceIndex
_Ieee8021PbbVipToPipMappingPipIfIndex_Object=MibTableColumn
ieee8021PbbVipToPipMappingPipIfIndex=_Ieee8021PbbVipToPipMappingPipIfIndex_Object((1,3,111,2,802,1,1,9,1,1,8,1,1),_Ieee8021PbbVipToPipMappingPipIfIndex_Type())
ieee8021PbbVipToPipMappingPipIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021PbbVipToPipMappingPipIfIndex.setStatus(_A)
_Ieee8021PbbVipToPipMappingStorageType_Type=StorageType
_Ieee8021PbbVipToPipMappingStorageType_Object=MibTableColumn
ieee8021PbbVipToPipMappingStorageType=_Ieee8021PbbVipToPipMappingStorageType_Object((1,3,111,2,802,1,1,9,1,1,8,1,2),_Ieee8021PbbVipToPipMappingStorageType_Type())
ieee8021PbbVipToPipMappingStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021PbbVipToPipMappingStorageType.setStatus(_A)
_Ieee8021PbbVipToPipMappingRowStatus_Type=RowStatus
_Ieee8021PbbVipToPipMappingRowStatus_Object=MibTableColumn
ieee8021PbbVipToPipMappingRowStatus=_Ieee8021PbbVipToPipMappingRowStatus_Object((1,3,111,2,802,1,1,9,1,1,8,1,3),_Ieee8021PbbVipToPipMappingRowStatus_Type())
ieee8021PbbVipToPipMappingRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021PbbVipToPipMappingRowStatus.setStatus(_A)
_Ieee8021PbbCBPServiceMappingTable_Object=MibTable
ieee8021PbbCBPServiceMappingTable=_Ieee8021PbbCBPServiceMappingTable_Object((1,3,111,2,802,1,1,9,1,1,9))
if mibBuilder.loadTexts:ieee8021PbbCBPServiceMappingTable.setStatus(_A)
_Ieee8021PbbCBPServiceMappingEntry_Object=MibTableRow
ieee8021PbbCBPServiceMappingEntry=_Ieee8021PbbCBPServiceMappingEntry_Object((1,3,111,2,802,1,1,9,1,1,9,1))
ieee8021PbbCBPServiceMappingEntry.setIndexNames((0,_E,_J),(0,_E,_I),(0,_B,_j))
if mibBuilder.loadTexts:ieee8021PbbCBPServiceMappingEntry.setStatus(_A)
_Ieee8021PbbCBPServiceMappingBackboneSid_Type=IEEE8021PbbServiceIdentifier
_Ieee8021PbbCBPServiceMappingBackboneSid_Object=MibTableColumn
ieee8021PbbCBPServiceMappingBackboneSid=_Ieee8021PbbCBPServiceMappingBackboneSid_Object((1,3,111,2,802,1,1,9,1,1,9,1,1),_Ieee8021PbbCBPServiceMappingBackboneSid_Type())
ieee8021PbbCBPServiceMappingBackboneSid.setMaxAccess(_G)
if mibBuilder.loadTexts:ieee8021PbbCBPServiceMappingBackboneSid.setStatus(_A)
_Ieee8021PbbCBPServiceMappingBVid_Type=VlanId
_Ieee8021PbbCBPServiceMappingBVid_Object=MibTableColumn
ieee8021PbbCBPServiceMappingBVid=_Ieee8021PbbCBPServiceMappingBVid_Object((1,3,111,2,802,1,1,9,1,1,9,1,2),_Ieee8021PbbCBPServiceMappingBVid_Type())
ieee8021PbbCBPServiceMappingBVid.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021PbbCBPServiceMappingBVid.setStatus(_A)
_Ieee8021PbbCBPServiceMappingDefaultBackboneDest_Type=MacAddress
_Ieee8021PbbCBPServiceMappingDefaultBackboneDest_Object=MibTableColumn
ieee8021PbbCBPServiceMappingDefaultBackboneDest=_Ieee8021PbbCBPServiceMappingDefaultBackboneDest_Object((1,3,111,2,802,1,1,9,1,1,9,1,3),_Ieee8021PbbCBPServiceMappingDefaultBackboneDest_Type())
ieee8021PbbCBPServiceMappingDefaultBackboneDest.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021PbbCBPServiceMappingDefaultBackboneDest.setStatus(_A)
_Ieee8021PbbCBPServiceMappingType_Type=IEEE8021PbbIngressEgress
_Ieee8021PbbCBPServiceMappingType_Object=MibTableColumn
ieee8021PbbCBPServiceMappingType=_Ieee8021PbbCBPServiceMappingType_Object((1,3,111,2,802,1,1,9,1,1,9,1,4),_Ieee8021PbbCBPServiceMappingType_Type())
ieee8021PbbCBPServiceMappingType.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021PbbCBPServiceMappingType.setStatus(_c)
class _Ieee8021PbbCBPServiceMappingLocalSid_Type(IEEE8021PbbServiceIdentifierOrUnassigned):defaultValue=1
_Ieee8021PbbCBPServiceMappingLocalSid_Type.__name__=_L
_Ieee8021PbbCBPServiceMappingLocalSid_Object=MibTableColumn
ieee8021PbbCBPServiceMappingLocalSid=_Ieee8021PbbCBPServiceMappingLocalSid_Object((1,3,111,2,802,1,1,9,1,1,9,1,5),_Ieee8021PbbCBPServiceMappingLocalSid_Type())
ieee8021PbbCBPServiceMappingLocalSid.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021PbbCBPServiceMappingLocalSid.setStatus(_A)
_Ieee8021PbbCBPServiceMappingRowStatus_Type=RowStatus
_Ieee8021PbbCBPServiceMappingRowStatus_Object=MibTableColumn
ieee8021PbbCBPServiceMappingRowStatus=_Ieee8021PbbCBPServiceMappingRowStatus_Object((1,3,111,2,802,1,1,9,1,1,9,1,6),_Ieee8021PbbCBPServiceMappingRowStatus_Type())
ieee8021PbbCBPServiceMappingRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021PbbCBPServiceMappingRowStatus.setStatus(_A)
_Ieee8021PbbCbpTable_Object=MibTable
ieee8021PbbCbpTable=_Ieee8021PbbCbpTable_Object((1,3,111,2,802,1,1,9,1,1,10))
if mibBuilder.loadTexts:ieee8021PbbCbpTable.setStatus(_A)
_Ieee8021PbbCbpEntry_Object=MibTableRow
ieee8021PbbCbpEntry=_Ieee8021PbbCbpEntry_Object((1,3,111,2,802,1,1,9,1,1,10,1))
ieee8021PbbCbpEntry.setIndexNames((0,_E,_J),(0,_E,_I))
if mibBuilder.loadTexts:ieee8021PbbCbpEntry.setStatus(_A)
_Ieee8021PbbCbpRowStatus_Type=RowStatus
_Ieee8021PbbCbpRowStatus_Object=MibTableColumn
ieee8021PbbCbpRowStatus=_Ieee8021PbbCbpRowStatus_Object((1,3,111,2,802,1,1,9,1,1,10,1,1),_Ieee8021PbbCbpRowStatus_Type())
ieee8021PbbCbpRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021PbbCbpRowStatus.setStatus(_A)
_Ieee8021PbbConformance_ObjectIdentity=ObjectIdentity
ieee8021PbbConformance=_Ieee8021PbbConformance_ObjectIdentity((1,3,111,2,802,1,1,9,2))
_Ieee8021PbbGroups_ObjectIdentity=ObjectIdentity
ieee8021PbbGroups=_Ieee8021PbbGroups_ObjectIdentity((1,3,111,2,802,1,1,9,2,1))
_Ieee8021PbbCompliances_ObjectIdentity=ObjectIdentity
ieee8021PbbCompliances=_Ieee8021PbbCompliances_ObjectIdentity((1,3,111,2,802,1,1,9,2,2))
ieee8021PbbPipEntry.registerAugmentions((_B,_k))
ieee8021PbbPipPriorityEntry.setIndexNames(*ieee8021PbbPipEntry.getIndexNames())
ieee8021PbbBackboneEdgeBridgeGroup=ObjectGroup((1,3,111,2,802,1,1,9,2,1,1))
ieee8021PbbBackboneEdgeBridgeGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:ieee8021PbbBackboneEdgeBridgeGroup.setStatus(_A)
ieee8021PbbVipGroup=ObjectGroup((1,3,111,2,802,1,1,9,2,1,2))
ieee8021PbbVipGroup.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:ieee8021PbbVipGroup.setStatus(_A)
ieee8021PbbPipGroup=ObjectGroup((1,3,111,2,802,1,1,9,2,1,3))
ieee8021PbbPipGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:ieee8021PbbPipGroup.setStatus(_A)
ieee8021PbbDefaultPriorityGroup=ObjectGroup((1,3,111,2,802,1,1,9,2,1,4))
ieee8021PbbDefaultPriorityGroup.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:ieee8021PbbDefaultPriorityGroup.setStatus(_A)
ieee8021PbbPipDecodingGroup=ObjectGroup((1,3,111,2,802,1,1,9,2,1,5))
ieee8021PbbPipDecodingGroup.setObjects(*((_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:ieee8021PbbPipDecodingGroup.setStatus(_A)
ieee8021PbbPipEncodingGroup=ObjectGroup((1,3,111,2,802,1,1,9,2,1,6))
ieee8021PbbPipEncodingGroup.setObjects((_B,_AC))
if mibBuilder.loadTexts:ieee8021PbbPipEncodingGroup.setStatus(_A)
ieee8021PbbVipToPipMappingGroup=ObjectGroup((1,3,111,2,802,1,1,9,2,1,7))
ieee8021PbbVipToPipMappingGroup.setObjects(*((_B,_AD),(_B,_AE),(_B,_AF)))
if mibBuilder.loadTexts:ieee8021PbbVipToPipMappingGroup.setStatus(_A)
ieee8021PbbCBPServiceMappingGroup=ObjectGroup((1,3,111,2,802,1,1,9,2,1,8))
ieee8021PbbCBPServiceMappingGroup.setObjects(*((_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK)))
if mibBuilder.loadTexts:ieee8021PbbCBPServiceMappingGroup.setStatus(_A)
ieee8021PbbDynamicCbpGroup=ObjectGroup((1,3,111,2,802,1,1,9,2,1,9))
ieee8021PbbDynamicCbpGroup.setObjects((_B,_AL))
if mibBuilder.loadTexts:ieee8021PbbDynamicCbpGroup.setStatus(_A)
ieee8021PbbVipPbbTeGroup=ObjectGroup((1,3,111,2,802,1,1,9,2,1,10))
ieee8021PbbVipPbbTeGroup.setObjects((_B,_AM))
if mibBuilder.loadTexts:ieee8021PbbVipPbbTeGroup.setStatus(_A)
ieee8021PbbCompliance=ModuleCompliance((1,3,111,2,802,1,1,9,2,2,1))
ieee8021PbbCompliance.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ieee8021PbbCompliance.setStatus(_A)
ieee8021PbbWithPbbTeCompliance=ModuleCompliance((1,3,111,2,802,1,1,9,2,2,2))
ieee8021PbbWithPbbTeCompliance.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_AN),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ieee8021PbbWithPbbTeCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ieee8021PbbMib':ieee8021PbbMib,'ieee8021PbbNotifications':ieee8021PbbNotifications,'ieee8021PbbObjects':ieee8021PbbObjects,'ieee8021PbbProviderBackboneBridge':ieee8021PbbProviderBackboneBridge,'ieee8021PbbBackboneEdgeBridgeObjects':ieee8021PbbBackboneEdgeBridgeObjects,_l:ieee8021PbbBackboneEdgeBridgeAddress,_m:ieee8021PbbBackboneEdgeBridgeName,_n:ieee8021PbbNumberOfIComponents,_o:ieee8021PbbNumberOfBComponents,_p:ieee8021PbbNumberOfBebPorts,_x:ieee8021PbbNextAvailablePipIfIndex,'ieee8021PbbVipTable':ieee8021PbbVipTable,'ieee8021PbbVipEntry':ieee8021PbbVipEntry,_q:ieee8021PbbVipPipIfIndex,_r:ieee8021PbbVipISid,_s:ieee8021PbbVipDefaultDstBMAC,_t:ieee8021PbbVipType,_u:ieee8021PbbVipRowStatus,_AM:ieee8021PbbVipEnableConnectionId,'ieee8021PbbISidToVipTable':ieee8021PbbISidToVipTable,'ieee8021PbbISidToVipEntry':ieee8021PbbISidToVipEntry,_d:ieee8021PbbISidToVipISid,_v:ieee8021PbbISidToVipComponentId,_w:ieee8021PbbISidToVipPort,'ieee8021PbbPipTable':ieee8021PbbPipTable,'ieee8021PbbPipEntry':ieee8021PbbPipEntry,_K:ieee8021PbbPipIfIndex,_y:ieee8021PbbPipBMACAddress,_z:ieee8021PbbPipName,_A0:ieee8021PbbPipIComponentId,_A1:ieee8021PbbPipVipMap,_A2:ieee8021PbbPipVipMap1,_A3:ieee8021PbbPipVipMap2,_A4:ieee8021PbbPipVipMap3,_A5:ieee8021PbbPipVipMap4,_A6:ieee8021PbbPipRowStatus,'ieee8021PbbPipPriorityTable':ieee8021PbbPipPriorityTable,_k:ieee8021PbbPipPriorityEntry,_A7:ieee8021PbbPipPriorityCodePointSelection,_A8:ieee8021PbbPipUseDEI,_A9:ieee8021PbbPipRequireDropEncoding,'ieee8021PbbPipDecodingTable':ieee8021PbbPipDecodingTable,'ieee8021PbbPipDecodingEntry':ieee8021PbbPipDecodingEntry,_e:ieee8021PbbPipDecodingPriorityCodePointRow,_f:ieee8021PbbPipDecodingPriorityCodePoint,_AA:ieee8021PbbPipDecodingPriority,_AB:ieee8021PbbPipDecodingDropEligible,'ieee8021PbbPipEncodingTable':ieee8021PbbPipEncodingTable,'ieee8021PbbPipEncodingEntry':ieee8021PbbPipEncodingEntry,_g:ieee8021PbbPipEncodingPriorityCodePointRow,_h:ieee8021PbbPipEncodingPriorityCodePoint,_i:ieee8021PbbPipEncodingDropEligible,_AC:ieee8021PbbPipEncodingPriority,'ieee8021PbbVipToPipMappingTable':ieee8021PbbVipToPipMappingTable,'ieee8021PbbVipToPipMappingEntry':ieee8021PbbVipToPipMappingEntry,_AD:ieee8021PbbVipToPipMappingPipIfIndex,_AE:ieee8021PbbVipToPipMappingStorageType,_AF:ieee8021PbbVipToPipMappingRowStatus,'ieee8021PbbCBPServiceMappingTable':ieee8021PbbCBPServiceMappingTable,'ieee8021PbbCBPServiceMappingEntry':ieee8021PbbCBPServiceMappingEntry,_j:ieee8021PbbCBPServiceMappingBackboneSid,_AG:ieee8021PbbCBPServiceMappingBVid,_AH:ieee8021PbbCBPServiceMappingDefaultBackboneDest,_AI:ieee8021PbbCBPServiceMappingType,_AJ:ieee8021PbbCBPServiceMappingLocalSid,_AK:ieee8021PbbCBPServiceMappingRowStatus,'ieee8021PbbCbpTable':ieee8021PbbCbpTable,'ieee8021PbbCbpEntry':ieee8021PbbCbpEntry,_AL:ieee8021PbbCbpRowStatus,'ieee8021PbbConformance':ieee8021PbbConformance,'ieee8021PbbGroups':ieee8021PbbGroups,_P:ieee8021PbbBackboneEdgeBridgeGroup,_Q:ieee8021PbbVipGroup,_R:ieee8021PbbPipGroup,_V:ieee8021PbbDefaultPriorityGroup,_W:ieee8021PbbPipDecodingGroup,_X:ieee8021PbbPipEncodingGroup,_S:ieee8021PbbVipToPipMappingGroup,_T:ieee8021PbbCBPServiceMappingGroup,_U:ieee8021PbbDynamicCbpGroup,_AN:ieee8021PbbVipPbbTeGroup,'ieee8021PbbCompliances':ieee8021PbbCompliances,'ieee8021PbbCompliance':ieee8021PbbCompliance,'ieee8021PbbWithPbbTeCompliance':ieee8021PbbWithPbbTeCompliance})