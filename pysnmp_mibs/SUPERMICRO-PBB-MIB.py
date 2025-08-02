_y='fsPbbDynamicCbpGroup'
_x='fsPbbCBPServiceMappingGroup'
_w='fsPbbVipToPipMappingGroup'
_v='fsPbbPipGroup'
_u='fsPbbVipGroup'
_t='fsPbbBackboneEdgeBridgeGroup'
_s='fsPbbCbpRowStatus'
_r='fsPbbCBPServiceMappingRowStatus'
_q='fsPbbCBPServiceMappingLocalSid'
_p='fsPbbCBPServiceMappingType'
_o='fsPbbCBPServiceMappingDefaultBackboneDest'
_n='fsPbbCBPServiceMappingBVid'
_m='fsPbbVipToPipMappingRowStatus'
_l='fsPbbVipToPipMappingStorageType'
_k='fsPbbVipToPipMappingPipIfIndex'
_j='fsPbbPipRowStatus'
_i='fsPbbPipIComponentId'
_h='fsPbbPipName'
_g='fsPbbPipBMACAddress'
_f='fsPbbNextAvailablePipIfIndex'
_e='fsPbbISidToVipPort'
_d='fsPbbISidToVipComponentId'
_c='fsPbbVipRowStatus'
_b='fsPbbVipType'
_a='fsPbbVipDefaultDstBMAC'
_Z='fsPbbVipISid'
_Y='fsPbbVipPipIfIndex'
_X='fsPbbNumberOfBebPorts'
_W='fsPbbNumberOfBComponents'
_V='fsPbbNumberOfIComponents'
_U='fsPbbBackboneEdgeBridgeName'
_T='fsPbbBackboneEdgeBridgeAddress'
_S='fsPbbCBPServiceMappingBackboneSid'
_R='fsPbbISidToVipISid'
_Q='read-write'
_P='MacAddress'
_O='Unsigned32'
_N='Integer32'
_M='InterfaceIndexOrZero'
_L='IEEE8021PbbIngressEgress'
_K='fsPbbPipIfIndex'
_J='SnmpAdminString'
_I='IEEE8021PbbServiceIdentifierOrUnassigned'
_H='not-accessible'
_G='fsdot1ahContextId'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='read-create'
_B='SUPERMICRO-PBB-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IEEE8021PbbComponentIdentifier,IEEE8021PbbIngressEgress,IEEE8021PbbServiceIdentifier,IEEE8021PbbServiceIdentifierOrUnassigned=mibBuilder.importSymbols('IEEE8021-TC-MIB','IEEE8021PbbComponentIdentifier',_L,'IEEE8021PbbServiceIdentifier',_I)
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_E,'InterfaceIndex',_M,_F)
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_N,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_O,'enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_P,'PhysAddress','RowStatus','StorageType','TextualConvention','TruthValue')
fsPbbMib=ModuleIdentity((1,3,6,1,4,1,10876,101,2,14))
if mibBuilder.loadTexts:fsPbbMib.setRevisions(('2012-09-05 00:00',))
_FsPbbNotifications_ObjectIdentity=ObjectIdentity
fsPbbNotifications=_FsPbbNotifications_ObjectIdentity((1,3,6,1,4,1,10876,101,2,14,0))
_FsPbbObjects_ObjectIdentity=ObjectIdentity
fsPbbObjects=_FsPbbObjects_ObjectIdentity((1,3,6,1,4,1,10876,101,2,14,1))
_FsPbbProviderBackboneBridge_ObjectIdentity=ObjectIdentity
fsPbbProviderBackboneBridge=_FsPbbProviderBackboneBridge_ObjectIdentity((1,3,6,1,4,1,10876,101,2,14,1,1))
_FsPbbBackboneEdgeBridgeObjects_ObjectIdentity=ObjectIdentity
fsPbbBackboneEdgeBridgeObjects=_FsPbbBackboneEdgeBridgeObjects_ObjectIdentity((1,3,6,1,4,1,10876,101,2,14,1,1,1))
_FsPbbBackboneEdgeBridgeAddress_Type=MacAddress
_FsPbbBackboneEdgeBridgeAddress_Object=MibScalar
fsPbbBackboneEdgeBridgeAddress=_FsPbbBackboneEdgeBridgeAddress_Object((1,3,6,1,4,1,10876,101,2,14,1,1,1,1),_FsPbbBackboneEdgeBridgeAddress_Type())
fsPbbBackboneEdgeBridgeAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPbbBackboneEdgeBridgeAddress.setStatus(_A)
class _FsPbbBackboneEdgeBridgeName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsPbbBackboneEdgeBridgeName_Type.__name__=_J
_FsPbbBackboneEdgeBridgeName_Object=MibScalar
fsPbbBackboneEdgeBridgeName=_FsPbbBackboneEdgeBridgeName_Object((1,3,6,1,4,1,10876,101,2,14,1,1,1,2),_FsPbbBackboneEdgeBridgeName_Type())
fsPbbBackboneEdgeBridgeName.setMaxAccess(_Q)
if mibBuilder.loadTexts:fsPbbBackboneEdgeBridgeName.setStatus(_A)
_FsPbbNumberOfIComponents_Type=Unsigned32
_FsPbbNumberOfIComponents_Object=MibScalar
fsPbbNumberOfIComponents=_FsPbbNumberOfIComponents_Object((1,3,6,1,4,1,10876,101,2,14,1,1,1,3),_FsPbbNumberOfIComponents_Type())
fsPbbNumberOfIComponents.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPbbNumberOfIComponents.setStatus(_A)
class _FsPbbNumberOfBComponents_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsPbbNumberOfBComponents_Type.__name__=_O
_FsPbbNumberOfBComponents_Object=MibScalar
fsPbbNumberOfBComponents=_FsPbbNumberOfBComponents_Object((1,3,6,1,4,1,10876,101,2,14,1,1,1,4),_FsPbbNumberOfBComponents_Type())
fsPbbNumberOfBComponents.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPbbNumberOfBComponents.setStatus(_A)
_FsPbbNumberOfBebPorts_Type=Unsigned32
_FsPbbNumberOfBebPorts_Object=MibScalar
fsPbbNumberOfBebPorts=_FsPbbNumberOfBebPorts_Object((1,3,6,1,4,1,10876,101,2,14,1,1,1,5),_FsPbbNumberOfBebPorts_Type())
fsPbbNumberOfBebPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPbbNumberOfBebPorts.setStatus(_A)
_FsPbbNextAvailablePipIfIndex_Type=InterfaceIndex
_FsPbbNextAvailablePipIfIndex_Object=MibScalar
fsPbbNextAvailablePipIfIndex=_FsPbbNextAvailablePipIfIndex_Object((1,3,6,1,4,1,10876,101,2,14,1,1,1,6),_FsPbbNextAvailablePipIfIndex_Type())
fsPbbNextAvailablePipIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPbbNextAvailablePipIfIndex.setStatus(_A)
_FsPbbVipTable_Object=MibTable
fsPbbVipTable=_FsPbbVipTable_Object((1,3,6,1,4,1,10876,101,2,14,1,1,2))
if mibBuilder.loadTexts:fsPbbVipTable.setStatus(_A)
_FsPbbVipEntry_Object=MibTableRow
fsPbbVipEntry=_FsPbbVipEntry_Object((1,3,6,1,4,1,10876,101,2,14,1,1,2,1))
fsPbbVipEntry.setIndexNames((0,_B,_G),(0,_E,_F))
if mibBuilder.loadTexts:fsPbbVipEntry.setStatus(_A)
class _Fsdot1ahContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Fsdot1ahContextId_Type.__name__=_N
_Fsdot1ahContextId_Object=MibTableColumn
fsdot1ahContextId=_Fsdot1ahContextId_Object((1,3,6,1,4,1,10876,101,2,14,1,1,2,1,1),_Fsdot1ahContextId_Type())
fsdot1ahContextId.setMaxAccess(_H)
if mibBuilder.loadTexts:fsdot1ahContextId.setStatus(_A)
class _FsPbbVipPipIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_FsPbbVipPipIfIndex_Type.__name__=_M
_FsPbbVipPipIfIndex_Object=MibTableColumn
fsPbbVipPipIfIndex=_FsPbbVipPipIfIndex_Object((1,3,6,1,4,1,10876,101,2,14,1,1,2,1,2),_FsPbbVipPipIfIndex_Type())
fsPbbVipPipIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPbbVipPipIfIndex.setStatus(_A)
class _FsPbbVipISid_Type(IEEE8021PbbServiceIdentifierOrUnassigned):defaultValue=1
_FsPbbVipISid_Type.__name__=_I
_FsPbbVipISid_Object=MibTableColumn
fsPbbVipISid=_FsPbbVipISid_Object((1,3,6,1,4,1,10876,101,2,14,1,1,2,1,3),_FsPbbVipISid_Type())
fsPbbVipISid.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPbbVipISid.setStatus(_A)
class _FsPbbVipDefaultDstBMAC_Type(MacAddress):defaultHexValue='001e83000001'
_FsPbbVipDefaultDstBMAC_Type.__name__=_P
_FsPbbVipDefaultDstBMAC_Object=MibTableColumn
fsPbbVipDefaultDstBMAC=_FsPbbVipDefaultDstBMAC_Object((1,3,6,1,4,1,10876,101,2,14,1,1,2,1,4),_FsPbbVipDefaultDstBMAC_Type())
fsPbbVipDefaultDstBMAC.setMaxAccess(_Q)
if mibBuilder.loadTexts:fsPbbVipDefaultDstBMAC.setStatus(_A)
class _FsPbbVipType_Type(IEEE8021PbbIngressEgress):defaultHexValue='03'
_FsPbbVipType_Type.__name__=_L
_FsPbbVipType_Object=MibTableColumn
fsPbbVipType=_FsPbbVipType_Object((1,3,6,1,4,1,10876,101,2,14,1,1,2,1,5),_FsPbbVipType_Type())
fsPbbVipType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPbbVipType.setStatus(_A)
_FsPbbVipRowStatus_Type=RowStatus
_FsPbbVipRowStatus_Object=MibTableColumn
fsPbbVipRowStatus=_FsPbbVipRowStatus_Object((1,3,6,1,4,1,10876,101,2,14,1,1,2,1,6),_FsPbbVipRowStatus_Type())
fsPbbVipRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPbbVipRowStatus.setStatus(_A)
_FsPbbISidToVipTable_Object=MibTable
fsPbbISidToVipTable=_FsPbbISidToVipTable_Object((1,3,6,1,4,1,10876,101,2,14,1,1,3))
if mibBuilder.loadTexts:fsPbbISidToVipTable.setStatus(_A)
_FsPbbISidToVipEntry_Object=MibTableRow
fsPbbISidToVipEntry=_FsPbbISidToVipEntry_Object((1,3,6,1,4,1,10876,101,2,14,1,1,3,1))
fsPbbISidToVipEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:fsPbbISidToVipEntry.setStatus(_A)
_FsPbbISidToVipISid_Type=IEEE8021PbbServiceIdentifier
_FsPbbISidToVipISid_Object=MibTableColumn
fsPbbISidToVipISid=_FsPbbISidToVipISid_Object((1,3,6,1,4,1,10876,101,2,14,1,1,3,1,1),_FsPbbISidToVipISid_Type())
fsPbbISidToVipISid.setMaxAccess(_H)
if mibBuilder.loadTexts:fsPbbISidToVipISid.setStatus(_A)
_FsPbbISidToVipComponentId_Type=IEEE8021PbbComponentIdentifier
_FsPbbISidToVipComponentId_Object=MibTableColumn
fsPbbISidToVipComponentId=_FsPbbISidToVipComponentId_Object((1,3,6,1,4,1,10876,101,2,14,1,1,3,1,2),_FsPbbISidToVipComponentId_Type())
fsPbbISidToVipComponentId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPbbISidToVipComponentId.setStatus(_A)
_FsPbbISidToVipPort_Type=InterfaceIndex
_FsPbbISidToVipPort_Object=MibTableColumn
fsPbbISidToVipPort=_FsPbbISidToVipPort_Object((1,3,6,1,4,1,10876,101,2,14,1,1,3,1,3),_FsPbbISidToVipPort_Type())
fsPbbISidToVipPort.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPbbISidToVipPort.setStatus(_A)
_FsPbbPipTable_Object=MibTable
fsPbbPipTable=_FsPbbPipTable_Object((1,3,6,1,4,1,10876,101,2,14,1,1,4))
if mibBuilder.loadTexts:fsPbbPipTable.setStatus(_A)
_FsPbbPipEntry_Object=MibTableRow
fsPbbPipEntry=_FsPbbPipEntry_Object((1,3,6,1,4,1,10876,101,2,14,1,1,4,1))
fsPbbPipEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:fsPbbPipEntry.setStatus(_A)
_FsPbbPipIfIndex_Type=InterfaceIndex
_FsPbbPipIfIndex_Object=MibTableColumn
fsPbbPipIfIndex=_FsPbbPipIfIndex_Object((1,3,6,1,4,1,10876,101,2,14,1,1,4,1,1),_FsPbbPipIfIndex_Type())
fsPbbPipIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:fsPbbPipIfIndex.setStatus(_A)
_FsPbbPipBMACAddress_Type=MacAddress
_FsPbbPipBMACAddress_Object=MibTableColumn
fsPbbPipBMACAddress=_FsPbbPipBMACAddress_Object((1,3,6,1,4,1,10876,101,2,14,1,1,4,1,2),_FsPbbPipBMACAddress_Type())
fsPbbPipBMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPbbPipBMACAddress.setStatus(_A)
class _FsPbbPipName_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsPbbPipName_Type.__name__=_J
_FsPbbPipName_Object=MibTableColumn
fsPbbPipName=_FsPbbPipName_Object((1,3,6,1,4,1,10876,101,2,14,1,1,4,1,3),_FsPbbPipName_Type())
fsPbbPipName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPbbPipName.setStatus(_A)
_FsPbbPipIComponentId_Type=IEEE8021PbbComponentIdentifier
_FsPbbPipIComponentId_Object=MibTableColumn
fsPbbPipIComponentId=_FsPbbPipIComponentId_Object((1,3,6,1,4,1,10876,101,2,14,1,1,4,1,4),_FsPbbPipIComponentId_Type())
fsPbbPipIComponentId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPbbPipIComponentId.setStatus(_A)
_FsPbbPipRowStatus_Type=RowStatus
_FsPbbPipRowStatus_Object=MibTableColumn
fsPbbPipRowStatus=_FsPbbPipRowStatus_Object((1,3,6,1,4,1,10876,101,2,14,1,1,4,1,5),_FsPbbPipRowStatus_Type())
fsPbbPipRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPbbPipRowStatus.setStatus(_A)
_FsPbbVipToPipMappingTable_Object=MibTable
fsPbbVipToPipMappingTable=_FsPbbVipToPipMappingTable_Object((1,3,6,1,4,1,10876,101,2,14,1,1,5))
if mibBuilder.loadTexts:fsPbbVipToPipMappingTable.setStatus(_A)
_FsPbbVipToPipMappingEntry_Object=MibTableRow
fsPbbVipToPipMappingEntry=_FsPbbVipToPipMappingEntry_Object((1,3,6,1,4,1,10876,101,2,14,1,1,5,1))
fsPbbVipToPipMappingEntry.setIndexNames((0,_B,_G),(0,_E,_F))
if mibBuilder.loadTexts:fsPbbVipToPipMappingEntry.setStatus(_A)
_FsPbbVipToPipMappingPipIfIndex_Type=InterfaceIndex
_FsPbbVipToPipMappingPipIfIndex_Object=MibTableColumn
fsPbbVipToPipMappingPipIfIndex=_FsPbbVipToPipMappingPipIfIndex_Object((1,3,6,1,4,1,10876,101,2,14,1,1,5,1,1),_FsPbbVipToPipMappingPipIfIndex_Type())
fsPbbVipToPipMappingPipIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPbbVipToPipMappingPipIfIndex.setStatus(_A)
_FsPbbVipToPipMappingStorageType_Type=StorageType
_FsPbbVipToPipMappingStorageType_Object=MibTableColumn
fsPbbVipToPipMappingStorageType=_FsPbbVipToPipMappingStorageType_Object((1,3,6,1,4,1,10876,101,2,14,1,1,5,1,2),_FsPbbVipToPipMappingStorageType_Type())
fsPbbVipToPipMappingStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPbbVipToPipMappingStorageType.setStatus(_A)
_FsPbbVipToPipMappingRowStatus_Type=RowStatus
_FsPbbVipToPipMappingRowStatus_Object=MibTableColumn
fsPbbVipToPipMappingRowStatus=_FsPbbVipToPipMappingRowStatus_Object((1,3,6,1,4,1,10876,101,2,14,1,1,5,1,3),_FsPbbVipToPipMappingRowStatus_Type())
fsPbbVipToPipMappingRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPbbVipToPipMappingRowStatus.setStatus(_A)
_FsPbbCBPServiceMappingTable_Object=MibTable
fsPbbCBPServiceMappingTable=_FsPbbCBPServiceMappingTable_Object((1,3,6,1,4,1,10876,101,2,14,1,1,6))
if mibBuilder.loadTexts:fsPbbCBPServiceMappingTable.setStatus(_A)
_FsPbbCBPServiceMappingEntry_Object=MibTableRow
fsPbbCBPServiceMappingEntry=_FsPbbCBPServiceMappingEntry_Object((1,3,6,1,4,1,10876,101,2,14,1,1,6,1))
fsPbbCBPServiceMappingEntry.setIndexNames((0,_B,_G),(0,_E,_F),(0,_B,_S))
if mibBuilder.loadTexts:fsPbbCBPServiceMappingEntry.setStatus(_A)
_FsPbbCBPServiceMappingBackboneSid_Type=IEEE8021PbbServiceIdentifier
_FsPbbCBPServiceMappingBackboneSid_Object=MibTableColumn
fsPbbCBPServiceMappingBackboneSid=_FsPbbCBPServiceMappingBackboneSid_Object((1,3,6,1,4,1,10876,101,2,14,1,1,6,1,1),_FsPbbCBPServiceMappingBackboneSid_Type())
fsPbbCBPServiceMappingBackboneSid.setMaxAccess(_H)
if mibBuilder.loadTexts:fsPbbCBPServiceMappingBackboneSid.setStatus(_A)
_FsPbbCBPServiceMappingBVid_Type=VlanId
_FsPbbCBPServiceMappingBVid_Object=MibTableColumn
fsPbbCBPServiceMappingBVid=_FsPbbCBPServiceMappingBVid_Object((1,3,6,1,4,1,10876,101,2,14,1,1,6,1,2),_FsPbbCBPServiceMappingBVid_Type())
fsPbbCBPServiceMappingBVid.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPbbCBPServiceMappingBVid.setStatus(_A)
_FsPbbCBPServiceMappingDefaultBackboneDest_Type=MacAddress
_FsPbbCBPServiceMappingDefaultBackboneDest_Object=MibTableColumn
fsPbbCBPServiceMappingDefaultBackboneDest=_FsPbbCBPServiceMappingDefaultBackboneDest_Object((1,3,6,1,4,1,10876,101,2,14,1,1,6,1,3),_FsPbbCBPServiceMappingDefaultBackboneDest_Type())
fsPbbCBPServiceMappingDefaultBackboneDest.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPbbCBPServiceMappingDefaultBackboneDest.setStatus(_A)
_FsPbbCBPServiceMappingType_Type=IEEE8021PbbIngressEgress
_FsPbbCBPServiceMappingType_Object=MibTableColumn
fsPbbCBPServiceMappingType=_FsPbbCBPServiceMappingType_Object((1,3,6,1,4,1,10876,101,2,14,1,1,6,1,4),_FsPbbCBPServiceMappingType_Type())
fsPbbCBPServiceMappingType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPbbCBPServiceMappingType.setStatus(_A)
class _FsPbbCBPServiceMappingLocalSid_Type(IEEE8021PbbServiceIdentifierOrUnassigned):defaultValue=1
_FsPbbCBPServiceMappingLocalSid_Type.__name__=_I
_FsPbbCBPServiceMappingLocalSid_Object=MibTableColumn
fsPbbCBPServiceMappingLocalSid=_FsPbbCBPServiceMappingLocalSid_Object((1,3,6,1,4,1,10876,101,2,14,1,1,6,1,5),_FsPbbCBPServiceMappingLocalSid_Type())
fsPbbCBPServiceMappingLocalSid.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPbbCBPServiceMappingLocalSid.setStatus(_A)
_FsPbbCBPServiceMappingRowStatus_Type=RowStatus
_FsPbbCBPServiceMappingRowStatus_Object=MibTableColumn
fsPbbCBPServiceMappingRowStatus=_FsPbbCBPServiceMappingRowStatus_Object((1,3,6,1,4,1,10876,101,2,14,1,1,6,1,6),_FsPbbCBPServiceMappingRowStatus_Type())
fsPbbCBPServiceMappingRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPbbCBPServiceMappingRowStatus.setStatus(_A)
_FsPbbCbpTable_Object=MibTable
fsPbbCbpTable=_FsPbbCbpTable_Object((1,3,6,1,4,1,10876,101,2,14,1,1,7))
if mibBuilder.loadTexts:fsPbbCbpTable.setStatus(_A)
_FsPbbCbpEntry_Object=MibTableRow
fsPbbCbpEntry=_FsPbbCbpEntry_Object((1,3,6,1,4,1,10876,101,2,14,1,1,7,1))
fsPbbCbpEntry.setIndexNames((0,_B,_G),(0,_E,_F))
if mibBuilder.loadTexts:fsPbbCbpEntry.setStatus(_A)
_FsPbbCbpRowStatus_Type=RowStatus
_FsPbbCbpRowStatus_Object=MibTableColumn
fsPbbCbpRowStatus=_FsPbbCbpRowStatus_Object((1,3,6,1,4,1,10876,101,2,14,1,1,7,1,1),_FsPbbCbpRowStatus_Type())
fsPbbCbpRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPbbCbpRowStatus.setStatus(_A)
_FsPbbPipToVipMappingTable_Object=MibTable
fsPbbPipToVipMappingTable=_FsPbbPipToVipMappingTable_Object((1,3,6,1,4,1,10876,101,2,14,1,1,8))
if mibBuilder.loadTexts:fsPbbPipToVipMappingTable.setStatus(_A)
_FsPbbPipToVipMappingEntry_Object=MibTableRow
fsPbbPipToVipMappingEntry=_FsPbbPipToVipMappingEntry_Object((1,3,6,1,4,1,10876,101,2,14,1,1,8,1))
fsPbbPipToVipMappingEntry.setIndexNames((0,_B,_G),(0,_B,_K),(0,_E,_F))
if mibBuilder.loadTexts:fsPbbPipToVipMappingEntry.setStatus(_A)
_FsPbbPipToVipMappingStatus_Type=TruthValue
_FsPbbPipToVipMappingStatus_Object=MibTableColumn
fsPbbPipToVipMappingStatus=_FsPbbPipToVipMappingStatus_Object((1,3,6,1,4,1,10876,101,2,14,1,1,8,1,1),_FsPbbPipToVipMappingStatus_Type())
fsPbbPipToVipMappingStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPbbPipToVipMappingStatus.setStatus(_A)
_FsPbbConformance_ObjectIdentity=ObjectIdentity
fsPbbConformance=_FsPbbConformance_ObjectIdentity((1,3,6,1,4,1,10876,101,2,14,2))
_FsPbbGroups_ObjectIdentity=ObjectIdentity
fsPbbGroups=_FsPbbGroups_ObjectIdentity((1,3,6,1,4,1,10876,101,2,14,2,1))
_FsPbbCompliances_ObjectIdentity=ObjectIdentity
fsPbbCompliances=_FsPbbCompliances_ObjectIdentity((1,3,6,1,4,1,10876,101,2,14,2,2))
fsPbbBackboneEdgeBridgeGroup=ObjectGroup((1,3,6,1,4,1,10876,101,2,14,2,1,1))
fsPbbBackboneEdgeBridgeGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:fsPbbBackboneEdgeBridgeGroup.setStatus(_A)
fsPbbVipGroup=ObjectGroup((1,3,6,1,4,1,10876,101,2,14,2,1,2))
fsPbbVipGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:fsPbbVipGroup.setStatus(_A)
fsPbbPipGroup=ObjectGroup((1,3,6,1,4,1,10876,101,2,14,2,1,3))
fsPbbPipGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:fsPbbPipGroup.setStatus(_A)
fsPbbVipToPipMappingGroup=ObjectGroup((1,3,6,1,4,1,10876,101,2,14,2,1,4))
fsPbbVipToPipMappingGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:fsPbbVipToPipMappingGroup.setStatus(_A)
fsPbbCBPServiceMappingGroup=ObjectGroup((1,3,6,1,4,1,10876,101,2,14,2,1,5))
fsPbbCBPServiceMappingGroup.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:fsPbbCBPServiceMappingGroup.setStatus(_A)
fsPbbDynamicCbpGroup=ObjectGroup((1,3,6,1,4,1,10876,101,2,14,2,1,6))
fsPbbDynamicCbpGroup.setObjects((_B,_s))
if mibBuilder.loadTexts:fsPbbDynamicCbpGroup.setStatus(_A)
fsPbbCompliance=ModuleCompliance((1,3,6,1,4,1,10876,101,2,14,2,2,1))
fsPbbCompliance.setObjects(*((_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:fsPbbCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsPbbMib':fsPbbMib,'fsPbbNotifications':fsPbbNotifications,'fsPbbObjects':fsPbbObjects,'fsPbbProviderBackboneBridge':fsPbbProviderBackboneBridge,'fsPbbBackboneEdgeBridgeObjects':fsPbbBackboneEdgeBridgeObjects,_T:fsPbbBackboneEdgeBridgeAddress,_U:fsPbbBackboneEdgeBridgeName,_V:fsPbbNumberOfIComponents,_W:fsPbbNumberOfBComponents,_X:fsPbbNumberOfBebPorts,_f:fsPbbNextAvailablePipIfIndex,'fsPbbVipTable':fsPbbVipTable,'fsPbbVipEntry':fsPbbVipEntry,_G:fsdot1ahContextId,_Y:fsPbbVipPipIfIndex,_Z:fsPbbVipISid,_a:fsPbbVipDefaultDstBMAC,_b:fsPbbVipType,_c:fsPbbVipRowStatus,'fsPbbISidToVipTable':fsPbbISidToVipTable,'fsPbbISidToVipEntry':fsPbbISidToVipEntry,_R:fsPbbISidToVipISid,_d:fsPbbISidToVipComponentId,_e:fsPbbISidToVipPort,'fsPbbPipTable':fsPbbPipTable,'fsPbbPipEntry':fsPbbPipEntry,_K:fsPbbPipIfIndex,_g:fsPbbPipBMACAddress,_h:fsPbbPipName,_i:fsPbbPipIComponentId,_j:fsPbbPipRowStatus,'fsPbbVipToPipMappingTable':fsPbbVipToPipMappingTable,'fsPbbVipToPipMappingEntry':fsPbbVipToPipMappingEntry,_k:fsPbbVipToPipMappingPipIfIndex,_l:fsPbbVipToPipMappingStorageType,_m:fsPbbVipToPipMappingRowStatus,'fsPbbCBPServiceMappingTable':fsPbbCBPServiceMappingTable,'fsPbbCBPServiceMappingEntry':fsPbbCBPServiceMappingEntry,_S:fsPbbCBPServiceMappingBackboneSid,_n:fsPbbCBPServiceMappingBVid,_o:fsPbbCBPServiceMappingDefaultBackboneDest,_p:fsPbbCBPServiceMappingType,_q:fsPbbCBPServiceMappingLocalSid,_r:fsPbbCBPServiceMappingRowStatus,'fsPbbCbpTable':fsPbbCbpTable,'fsPbbCbpEntry':fsPbbCbpEntry,_s:fsPbbCbpRowStatus,'fsPbbPipToVipMappingTable':fsPbbPipToVipMappingTable,'fsPbbPipToVipMappingEntry':fsPbbPipToVipMappingEntry,'fsPbbPipToVipMappingStatus':fsPbbPipToVipMappingStatus,'fsPbbConformance':fsPbbConformance,'fsPbbGroups':fsPbbGroups,_t:fsPbbBackboneEdgeBridgeGroup,_u:fsPbbVipGroup,_v:fsPbbPipGroup,_w:fsPbbVipToPipMappingGroup,_x:fsPbbCBPServiceMappingGroup,_y:fsPbbDynamicCbpGroup,'fsPbbCompliances':fsPbbCompliances,'fsPbbCompliance':fsPbbCompliance})