_A2='cpwVcMplsInboundGroup'
_A1='cpwVcMplsMappingGroup'
_A0='cpwVcMplsOutboundGroup'
_z='cpwVcMplsGroup'
_y='cpwVcMplsInboundStorageType'
_x='cpwVcMplsInboundRowStatus'
_w='cpwVcMplsInboundIfIndex'
_v='cpwVcMplsInboundTunnelPeerLSR'
_u='cpwVcMplsInboundTunnelLclLSR'
_t='cpwVcMplsInboundTunnelInstance'
_s='cpwVcMplsInboundTunnelIndex'
_r='cpwVcMplsInboundLsrXcIndex'
_q='cpwVcMplsInboundIndexNext'
_p='cpwVcMplsOutboundStorageType'
_o='cpwVcMplsOutboundRowStatus'
_n='cpwVcMplsOutboundIfIndex'
_m='cpwVcMplsOutboundTunnelPeerLSR'
_l='cpwVcMplsOutboundTunnelLclLSR'
_k='cpwVcMplsOutboundTunnelInstance'
_j='cpwVcMplsOutboundTunnelIndex'
_i='cpwVcMplsOutboundLsrXcIndex'
_h='cpwVcMplsOutboundIndexNext'
_g='cpwVcMplsStorageType'
_f='cpwVcMplsPeerLdpID'
_e='cpwVcMplsLocalLdpEntityID'
_d='cpwVcMplsLocalLdpID'
_c='cpwVcMplsTtl'
_b='cpwVcMplsExpBits'
_a='cpwVcMplsExpBitsMode'
_Z='cpwVcMplsMplsType'
_Y='cpwVcMplsTeMappingTunnelLocalLsrID'
_X='cpwVcMplsTeMappingTunnelPeerLsrID'
_W='cpwVcMplsTeMappingTunnelInstance'
_V='cpwVcMplsTeMappingTunnelIndex'
_U='cpwVcMplsTeMappingTunnelDirection'
_T='inbound'
_S='outbound'
_R='cpwVcMplsNonTeMappingIfIndex'
_Q='cpwVcMplsNonTeMappingXcTunnelIndex'
_P='cpwVcMplsNonTeMappingTunnelDirection'
_O='cpwVcMplsInboundIndex'
_N='cpwVcMplsOutboundIndex'
_M='2001-07-11 12:00'
_L='cpwVcMplsTeMappingVcIndex'
_K='cpwVcMplsNonTeMappingVcIndex'
_J='Integer32'
_I='cpwVcIndex'
_H='CISCO-IETF-PW-MIB'
_G='read-only'
_F='read-write'
_E='Unsigned32'
_D='not-accessible'
_C='read-create'
_B='CISCO-IETF-PW-MPLS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cpwVcIndex,=mibBuilder.importSymbols(_H,_I)
CpwVcIndexType,=mibBuilder.importSymbols('CISCO-IETF-PW-TC-MIB','CpwVcIndexType')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
MplsLdpIdentifier,MplsLsrIdentifier,MplsTunnelIndex,MplsTunnelInstanceIndex=mibBuilder.importSymbols('MPLS-TC-STD-MIB','MplsLdpIdentifier','MplsLsrIdentifier','MplsTunnelIndex','MplsTunnelInstanceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention')
cpwVcMplsMIB=ModuleIdentity((1,3,6,1,4,1,9,10,107))
if mibBuilder.loadTexts:cpwVcMplsMIB.setRevisions(('2003-02-26 12:00','2002-06-02 12:00','2002-01-29 12:00',_M,_M))
_CpwVcMplsNotifications_ObjectIdentity=ObjectIdentity
cpwVcMplsNotifications=_CpwVcMplsNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,107,0))
_CpwVcMplsNotifyPrefix_ObjectIdentity=ObjectIdentity
cpwVcMplsNotifyPrefix=_CpwVcMplsNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,107,0,0))
_CpwVcMplsObjects_ObjectIdentity=ObjectIdentity
cpwVcMplsObjects=_CpwVcMplsObjects_ObjectIdentity((1,3,6,1,4,1,9,10,107,1))
_CpwVcMplsTable_Object=MibTable
cpwVcMplsTable=_CpwVcMplsTable_Object((1,3,6,1,4,1,9,10,107,1,1))
if mibBuilder.loadTexts:cpwVcMplsTable.setStatus(_A)
_CpwVcMplsEntry_Object=MibTableRow
cpwVcMplsEntry=_CpwVcMplsEntry_Object((1,3,6,1,4,1,9,10,107,1,1,1))
cpwVcMplsEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cpwVcMplsEntry.setStatus(_A)
class _CpwVcMplsMplsType_Type(Bits):namedValues=NamedValues(*(('mplsTe',0),('mplsNonTe',1),('vcOnly',2)))
_CpwVcMplsMplsType_Type.__name__='Bits'
_CpwVcMplsMplsType_Object=MibTableColumn
cpwVcMplsMplsType=_CpwVcMplsMplsType_Object((1,3,6,1,4,1,9,10,107,1,1,1,1),_CpwVcMplsMplsType_Type())
cpwVcMplsMplsType.setMaxAccess(_F)
if mibBuilder.loadTexts:cpwVcMplsMplsType.setStatus(_A)
class _CpwVcMplsExpBitsMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('outerTunnel',1),('specifiedValue',2),('serviceDependant',3)))
_CpwVcMplsExpBitsMode_Type.__name__=_J
_CpwVcMplsExpBitsMode_Object=MibTableColumn
cpwVcMplsExpBitsMode=_CpwVcMplsExpBitsMode_Object((1,3,6,1,4,1,9,10,107,1,1,1,2),_CpwVcMplsExpBitsMode_Type())
cpwVcMplsExpBitsMode.setMaxAccess(_F)
if mibBuilder.loadTexts:cpwVcMplsExpBitsMode.setStatus(_A)
class _CpwVcMplsExpBits_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CpwVcMplsExpBits_Type.__name__=_E
_CpwVcMplsExpBits_Object=MibTableColumn
cpwVcMplsExpBits=_CpwVcMplsExpBits_Object((1,3,6,1,4,1,9,10,107,1,1,1,3),_CpwVcMplsExpBits_Type())
cpwVcMplsExpBits.setMaxAccess(_F)
if mibBuilder.loadTexts:cpwVcMplsExpBits.setStatus(_A)
class _CpwVcMplsTtl_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpwVcMplsTtl_Type.__name__=_E
_CpwVcMplsTtl_Object=MibTableColumn
cpwVcMplsTtl=_CpwVcMplsTtl_Object((1,3,6,1,4,1,9,10,107,1,1,1,4),_CpwVcMplsTtl_Type())
cpwVcMplsTtl.setMaxAccess(_F)
if mibBuilder.loadTexts:cpwVcMplsTtl.setStatus(_A)
_CpwVcMplsLocalLdpID_Type=MplsLdpIdentifier
_CpwVcMplsLocalLdpID_Object=MibTableColumn
cpwVcMplsLocalLdpID=_CpwVcMplsLocalLdpID_Object((1,3,6,1,4,1,9,10,107,1,1,1,5),_CpwVcMplsLocalLdpID_Type())
cpwVcMplsLocalLdpID.setMaxAccess(_F)
if mibBuilder.loadTexts:cpwVcMplsLocalLdpID.setStatus(_A)
_CpwVcMplsLocalLdpEntityID_Type=Unsigned32
_CpwVcMplsLocalLdpEntityID_Object=MibTableColumn
cpwVcMplsLocalLdpEntityID=_CpwVcMplsLocalLdpEntityID_Object((1,3,6,1,4,1,9,10,107,1,1,1,6),_CpwVcMplsLocalLdpEntityID_Type())
cpwVcMplsLocalLdpEntityID.setMaxAccess(_F)
if mibBuilder.loadTexts:cpwVcMplsLocalLdpEntityID.setStatus(_A)
_CpwVcMplsPeerLdpID_Type=MplsLdpIdentifier
_CpwVcMplsPeerLdpID_Object=MibTableColumn
cpwVcMplsPeerLdpID=_CpwVcMplsPeerLdpID_Object((1,3,6,1,4,1,9,10,107,1,1,1,7),_CpwVcMplsPeerLdpID_Type())
cpwVcMplsPeerLdpID.setMaxAccess(_G)
if mibBuilder.loadTexts:cpwVcMplsPeerLdpID.setStatus(_A)
_CpwVcMplsStorageType_Type=StorageType
_CpwVcMplsStorageType_Object=MibTableColumn
cpwVcMplsStorageType=_CpwVcMplsStorageType_Object((1,3,6,1,4,1,9,10,107,1,1,1,8),_CpwVcMplsStorageType_Type())
cpwVcMplsStorageType.setMaxAccess(_F)
if mibBuilder.loadTexts:cpwVcMplsStorageType.setStatus(_A)
class _CpwVcMplsOutboundIndexNext_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CpwVcMplsOutboundIndexNext_Type.__name__=_E
_CpwVcMplsOutboundIndexNext_Object=MibScalar
cpwVcMplsOutboundIndexNext=_CpwVcMplsOutboundIndexNext_Object((1,3,6,1,4,1,9,10,107,1,2),_CpwVcMplsOutboundIndexNext_Type())
cpwVcMplsOutboundIndexNext.setMaxAccess(_G)
if mibBuilder.loadTexts:cpwVcMplsOutboundIndexNext.setStatus(_A)
_CpwVcMplsOutboundTable_Object=MibTable
cpwVcMplsOutboundTable=_CpwVcMplsOutboundTable_Object((1,3,6,1,4,1,9,10,107,1,3))
if mibBuilder.loadTexts:cpwVcMplsOutboundTable.setStatus(_A)
_CpwVcMplsOutboundEntry_Object=MibTableRow
cpwVcMplsOutboundEntry=_CpwVcMplsOutboundEntry_Object((1,3,6,1,4,1,9,10,107,1,3,1))
cpwVcMplsOutboundEntry.setIndexNames((0,_H,_I),(0,_B,_N))
if mibBuilder.loadTexts:cpwVcMplsOutboundEntry.setStatus(_A)
class _CpwVcMplsOutboundIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CpwVcMplsOutboundIndex_Type.__name__=_E
_CpwVcMplsOutboundIndex_Object=MibTableColumn
cpwVcMplsOutboundIndex=_CpwVcMplsOutboundIndex_Object((1,3,6,1,4,1,9,10,107,1,3,1,1),_CpwVcMplsOutboundIndex_Type())
cpwVcMplsOutboundIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcMplsOutboundIndex.setStatus(_A)
_CpwVcMplsOutboundLsrXcIndex_Type=Unsigned32
_CpwVcMplsOutboundLsrXcIndex_Object=MibTableColumn
cpwVcMplsOutboundLsrXcIndex=_CpwVcMplsOutboundLsrXcIndex_Object((1,3,6,1,4,1,9,10,107,1,3,1,2),_CpwVcMplsOutboundLsrXcIndex_Type())
cpwVcMplsOutboundLsrXcIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcMplsOutboundLsrXcIndex.setStatus(_A)
_CpwVcMplsOutboundTunnelIndex_Type=MplsTunnelIndex
_CpwVcMplsOutboundTunnelIndex_Object=MibTableColumn
cpwVcMplsOutboundTunnelIndex=_CpwVcMplsOutboundTunnelIndex_Object((1,3,6,1,4,1,9,10,107,1,3,1,3),_CpwVcMplsOutboundTunnelIndex_Type())
cpwVcMplsOutboundTunnelIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcMplsOutboundTunnelIndex.setStatus(_A)
_CpwVcMplsOutboundTunnelInstance_Type=MplsTunnelInstanceIndex
_CpwVcMplsOutboundTunnelInstance_Object=MibTableColumn
cpwVcMplsOutboundTunnelInstance=_CpwVcMplsOutboundTunnelInstance_Object((1,3,6,1,4,1,9,10,107,1,3,1,4),_CpwVcMplsOutboundTunnelInstance_Type())
cpwVcMplsOutboundTunnelInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcMplsOutboundTunnelInstance.setStatus(_A)
_CpwVcMplsOutboundTunnelLclLSR_Type=MplsLsrIdentifier
_CpwVcMplsOutboundTunnelLclLSR_Object=MibTableColumn
cpwVcMplsOutboundTunnelLclLSR=_CpwVcMplsOutboundTunnelLclLSR_Object((1,3,6,1,4,1,9,10,107,1,3,1,5),_CpwVcMplsOutboundTunnelLclLSR_Type())
cpwVcMplsOutboundTunnelLclLSR.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcMplsOutboundTunnelLclLSR.setStatus(_A)
_CpwVcMplsOutboundTunnelPeerLSR_Type=MplsLsrIdentifier
_CpwVcMplsOutboundTunnelPeerLSR_Object=MibTableColumn
cpwVcMplsOutboundTunnelPeerLSR=_CpwVcMplsOutboundTunnelPeerLSR_Object((1,3,6,1,4,1,9,10,107,1,3,1,6),_CpwVcMplsOutboundTunnelPeerLSR_Type())
cpwVcMplsOutboundTunnelPeerLSR.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcMplsOutboundTunnelPeerLSR.setStatus(_A)
_CpwVcMplsOutboundIfIndex_Type=InterfaceIndexOrZero
_CpwVcMplsOutboundIfIndex_Object=MibTableColumn
cpwVcMplsOutboundIfIndex=_CpwVcMplsOutboundIfIndex_Object((1,3,6,1,4,1,9,10,107,1,3,1,7),_CpwVcMplsOutboundIfIndex_Type())
cpwVcMplsOutboundIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcMplsOutboundIfIndex.setStatus(_A)
_CpwVcMplsOutboundRowStatus_Type=RowStatus
_CpwVcMplsOutboundRowStatus_Object=MibTableColumn
cpwVcMplsOutboundRowStatus=_CpwVcMplsOutboundRowStatus_Object((1,3,6,1,4,1,9,10,107,1,3,1,8),_CpwVcMplsOutboundRowStatus_Type())
cpwVcMplsOutboundRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcMplsOutboundRowStatus.setStatus(_A)
_CpwVcMplsOutboundStorageType_Type=StorageType
_CpwVcMplsOutboundStorageType_Object=MibTableColumn
cpwVcMplsOutboundStorageType=_CpwVcMplsOutboundStorageType_Object((1,3,6,1,4,1,9,10,107,1,3,1,9),_CpwVcMplsOutboundStorageType_Type())
cpwVcMplsOutboundStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcMplsOutboundStorageType.setStatus(_A)
class _CpwVcMplsInboundIndexNext_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CpwVcMplsInboundIndexNext_Type.__name__=_E
_CpwVcMplsInboundIndexNext_Object=MibScalar
cpwVcMplsInboundIndexNext=_CpwVcMplsInboundIndexNext_Object((1,3,6,1,4,1,9,10,107,1,4),_CpwVcMplsInboundIndexNext_Type())
cpwVcMplsInboundIndexNext.setMaxAccess(_G)
if mibBuilder.loadTexts:cpwVcMplsInboundIndexNext.setStatus(_A)
_CpwVcMplsInboundTable_Object=MibTable
cpwVcMplsInboundTable=_CpwVcMplsInboundTable_Object((1,3,6,1,4,1,9,10,107,1,5))
if mibBuilder.loadTexts:cpwVcMplsInboundTable.setStatus(_A)
_CpwVcMplsInboundEntry_Object=MibTableRow
cpwVcMplsInboundEntry=_CpwVcMplsInboundEntry_Object((1,3,6,1,4,1,9,10,107,1,5,1))
cpwVcMplsInboundEntry.setIndexNames((0,_H,_I),(0,_B,_O))
if mibBuilder.loadTexts:cpwVcMplsInboundEntry.setStatus(_A)
class _CpwVcMplsInboundIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CpwVcMplsInboundIndex_Type.__name__=_E
_CpwVcMplsInboundIndex_Object=MibTableColumn
cpwVcMplsInboundIndex=_CpwVcMplsInboundIndex_Object((1,3,6,1,4,1,9,10,107,1,5,1,1),_CpwVcMplsInboundIndex_Type())
cpwVcMplsInboundIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcMplsInboundIndex.setStatus(_A)
_CpwVcMplsInboundLsrXcIndex_Type=Unsigned32
_CpwVcMplsInboundLsrXcIndex_Object=MibTableColumn
cpwVcMplsInboundLsrXcIndex=_CpwVcMplsInboundLsrXcIndex_Object((1,3,6,1,4,1,9,10,107,1,5,1,2),_CpwVcMplsInboundLsrXcIndex_Type())
cpwVcMplsInboundLsrXcIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcMplsInboundLsrXcIndex.setStatus(_A)
_CpwVcMplsInboundTunnelIndex_Type=MplsTunnelIndex
_CpwVcMplsInboundTunnelIndex_Object=MibTableColumn
cpwVcMplsInboundTunnelIndex=_CpwVcMplsInboundTunnelIndex_Object((1,3,6,1,4,1,9,10,107,1,5,1,3),_CpwVcMplsInboundTunnelIndex_Type())
cpwVcMplsInboundTunnelIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcMplsInboundTunnelIndex.setStatus(_A)
_CpwVcMplsInboundTunnelInstance_Type=MplsTunnelInstanceIndex
_CpwVcMplsInboundTunnelInstance_Object=MibTableColumn
cpwVcMplsInboundTunnelInstance=_CpwVcMplsInboundTunnelInstance_Object((1,3,6,1,4,1,9,10,107,1,5,1,4),_CpwVcMplsInboundTunnelInstance_Type())
cpwVcMplsInboundTunnelInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcMplsInboundTunnelInstance.setStatus(_A)
_CpwVcMplsInboundTunnelLclLSR_Type=MplsLsrIdentifier
_CpwVcMplsInboundTunnelLclLSR_Object=MibTableColumn
cpwVcMplsInboundTunnelLclLSR=_CpwVcMplsInboundTunnelLclLSR_Object((1,3,6,1,4,1,9,10,107,1,5,1,5),_CpwVcMplsInboundTunnelLclLSR_Type())
cpwVcMplsInboundTunnelLclLSR.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcMplsInboundTunnelLclLSR.setStatus(_A)
_CpwVcMplsInboundTunnelPeerLSR_Type=MplsLsrIdentifier
_CpwVcMplsInboundTunnelPeerLSR_Object=MibTableColumn
cpwVcMplsInboundTunnelPeerLSR=_CpwVcMplsInboundTunnelPeerLSR_Object((1,3,6,1,4,1,9,10,107,1,5,1,6),_CpwVcMplsInboundTunnelPeerLSR_Type())
cpwVcMplsInboundTunnelPeerLSR.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcMplsInboundTunnelPeerLSR.setStatus(_A)
_CpwVcMplsInboundIfIndex_Type=InterfaceIndexOrZero
_CpwVcMplsInboundIfIndex_Object=MibTableColumn
cpwVcMplsInboundIfIndex=_CpwVcMplsInboundIfIndex_Object((1,3,6,1,4,1,9,10,107,1,5,1,7),_CpwVcMplsInboundIfIndex_Type())
cpwVcMplsInboundIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcMplsInboundIfIndex.setStatus(_A)
_CpwVcMplsInboundRowStatus_Type=RowStatus
_CpwVcMplsInboundRowStatus_Object=MibTableColumn
cpwVcMplsInboundRowStatus=_CpwVcMplsInboundRowStatus_Object((1,3,6,1,4,1,9,10,107,1,5,1,8),_CpwVcMplsInboundRowStatus_Type())
cpwVcMplsInboundRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcMplsInboundRowStatus.setStatus(_A)
_CpwVcMplsInboundStorageType_Type=StorageType
_CpwVcMplsInboundStorageType_Object=MibTableColumn
cpwVcMplsInboundStorageType=_CpwVcMplsInboundStorageType_Object((1,3,6,1,4,1,9,10,107,1,5,1,9),_CpwVcMplsInboundStorageType_Type())
cpwVcMplsInboundStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcMplsInboundStorageType.setStatus(_A)
_CpwVcMplsNonTeMappingTable_Object=MibTable
cpwVcMplsNonTeMappingTable=_CpwVcMplsNonTeMappingTable_Object((1,3,6,1,4,1,9,10,107,1,6))
if mibBuilder.loadTexts:cpwVcMplsNonTeMappingTable.setStatus(_A)
_CpwVcMplsNonTeMappingEntry_Object=MibTableRow
cpwVcMplsNonTeMappingEntry=_CpwVcMplsNonTeMappingEntry_Object((1,3,6,1,4,1,9,10,107,1,6,1))
cpwVcMplsNonTeMappingEntry.setIndexNames((0,_B,_P),(0,_B,_Q),(0,_B,_R),(0,_B,_K))
if mibBuilder.loadTexts:cpwVcMplsNonTeMappingEntry.setStatus(_A)
class _CpwVcMplsNonTeMappingTunnelDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_CpwVcMplsNonTeMappingTunnelDirection_Type.__name__=_J
_CpwVcMplsNonTeMappingTunnelDirection_Object=MibTableColumn
cpwVcMplsNonTeMappingTunnelDirection=_CpwVcMplsNonTeMappingTunnelDirection_Object((1,3,6,1,4,1,9,10,107,1,6,1,1),_CpwVcMplsNonTeMappingTunnelDirection_Type())
cpwVcMplsNonTeMappingTunnelDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcMplsNonTeMappingTunnelDirection.setStatus(_A)
class _CpwVcMplsNonTeMappingXcTunnelIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CpwVcMplsNonTeMappingXcTunnelIndex_Type.__name__=_E
_CpwVcMplsNonTeMappingXcTunnelIndex_Object=MibTableColumn
cpwVcMplsNonTeMappingXcTunnelIndex=_CpwVcMplsNonTeMappingXcTunnelIndex_Object((1,3,6,1,4,1,9,10,107,1,6,1,2),_CpwVcMplsNonTeMappingXcTunnelIndex_Type())
cpwVcMplsNonTeMappingXcTunnelIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcMplsNonTeMappingXcTunnelIndex.setStatus(_A)
_CpwVcMplsNonTeMappingIfIndex_Type=InterfaceIndexOrZero
_CpwVcMplsNonTeMappingIfIndex_Object=MibTableColumn
cpwVcMplsNonTeMappingIfIndex=_CpwVcMplsNonTeMappingIfIndex_Object((1,3,6,1,4,1,9,10,107,1,6,1,3),_CpwVcMplsNonTeMappingIfIndex_Type())
cpwVcMplsNonTeMappingIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcMplsNonTeMappingIfIndex.setStatus(_A)
_CpwVcMplsNonTeMappingVcIndex_Type=CpwVcIndexType
_CpwVcMplsNonTeMappingVcIndex_Object=MibTableColumn
cpwVcMplsNonTeMappingVcIndex=_CpwVcMplsNonTeMappingVcIndex_Object((1,3,6,1,4,1,9,10,107,1,6,1,4),_CpwVcMplsNonTeMappingVcIndex_Type())
cpwVcMplsNonTeMappingVcIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cpwVcMplsNonTeMappingVcIndex.setStatus(_A)
_CpwVcMplsTeMappingTable_Object=MibTable
cpwVcMplsTeMappingTable=_CpwVcMplsTeMappingTable_Object((1,3,6,1,4,1,9,10,107,1,7))
if mibBuilder.loadTexts:cpwVcMplsTeMappingTable.setStatus(_A)
_CpwVcMplsTeMappingEntry_Object=MibTableRow
cpwVcMplsTeMappingEntry=_CpwVcMplsTeMappingEntry_Object((1,3,6,1,4,1,9,10,107,1,7,1))
cpwVcMplsTeMappingEntry.setIndexNames((0,_B,_U),(0,_B,_V),(0,_B,_W),(0,_B,_X),(0,_B,_Y),(0,_B,_L))
if mibBuilder.loadTexts:cpwVcMplsTeMappingEntry.setStatus(_A)
class _CpwVcMplsTeMappingTunnelDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_CpwVcMplsTeMappingTunnelDirection_Type.__name__=_J
_CpwVcMplsTeMappingTunnelDirection_Object=MibTableColumn
cpwVcMplsTeMappingTunnelDirection=_CpwVcMplsTeMappingTunnelDirection_Object((1,3,6,1,4,1,9,10,107,1,7,1,1),_CpwVcMplsTeMappingTunnelDirection_Type())
cpwVcMplsTeMappingTunnelDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcMplsTeMappingTunnelDirection.setStatus(_A)
_CpwVcMplsTeMappingTunnelIndex_Type=MplsTunnelIndex
_CpwVcMplsTeMappingTunnelIndex_Object=MibTableColumn
cpwVcMplsTeMappingTunnelIndex=_CpwVcMplsTeMappingTunnelIndex_Object((1,3,6,1,4,1,9,10,107,1,7,1,2),_CpwVcMplsTeMappingTunnelIndex_Type())
cpwVcMplsTeMappingTunnelIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcMplsTeMappingTunnelIndex.setStatus(_A)
_CpwVcMplsTeMappingTunnelInstance_Type=MplsTunnelInstanceIndex
_CpwVcMplsTeMappingTunnelInstance_Object=MibTableColumn
cpwVcMplsTeMappingTunnelInstance=_CpwVcMplsTeMappingTunnelInstance_Object((1,3,6,1,4,1,9,10,107,1,7,1,3),_CpwVcMplsTeMappingTunnelInstance_Type())
cpwVcMplsTeMappingTunnelInstance.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcMplsTeMappingTunnelInstance.setStatus(_A)
_CpwVcMplsTeMappingTunnelPeerLsrID_Type=MplsLsrIdentifier
_CpwVcMplsTeMappingTunnelPeerLsrID_Object=MibTableColumn
cpwVcMplsTeMappingTunnelPeerLsrID=_CpwVcMplsTeMappingTunnelPeerLsrID_Object((1,3,6,1,4,1,9,10,107,1,7,1,4),_CpwVcMplsTeMappingTunnelPeerLsrID_Type())
cpwVcMplsTeMappingTunnelPeerLsrID.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcMplsTeMappingTunnelPeerLsrID.setStatus(_A)
_CpwVcMplsTeMappingTunnelLocalLsrID_Type=MplsLsrIdentifier
_CpwVcMplsTeMappingTunnelLocalLsrID_Object=MibTableColumn
cpwVcMplsTeMappingTunnelLocalLsrID=_CpwVcMplsTeMappingTunnelLocalLsrID_Object((1,3,6,1,4,1,9,10,107,1,7,1,5),_CpwVcMplsTeMappingTunnelLocalLsrID_Type())
cpwVcMplsTeMappingTunnelLocalLsrID.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcMplsTeMappingTunnelLocalLsrID.setStatus(_A)
_CpwVcMplsTeMappingVcIndex_Type=CpwVcIndexType
_CpwVcMplsTeMappingVcIndex_Object=MibTableColumn
cpwVcMplsTeMappingVcIndex=_CpwVcMplsTeMappingVcIndex_Object((1,3,6,1,4,1,9,10,107,1,7,1,6),_CpwVcMplsTeMappingVcIndex_Type())
cpwVcMplsTeMappingVcIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cpwVcMplsTeMappingVcIndex.setStatus(_A)
_CpwVcMplsConformance_ObjectIdentity=ObjectIdentity
cpwVcMplsConformance=_CpwVcMplsConformance_ObjectIdentity((1,3,6,1,4,1,9,10,107,2))
_CpwVcMplsGroups_ObjectIdentity=ObjectIdentity
cpwVcMplsGroups=_CpwVcMplsGroups_ObjectIdentity((1,3,6,1,4,1,9,10,107,2,1))
_CpwVcMplsCompliances_ObjectIdentity=ObjectIdentity
cpwVcMplsCompliances=_CpwVcMplsCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,107,2,2))
cpwVcMplsGroup=ObjectGroup((1,3,6,1,4,1,9,10,107,2,1,1))
cpwVcMplsGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:cpwVcMplsGroup.setStatus(_A)
cpwVcMplsOutboundGroup=ObjectGroup((1,3,6,1,4,1,9,10,107,2,1,2))
cpwVcMplsOutboundGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:cpwVcMplsOutboundGroup.setStatus(_A)
cpwVcMplsInboundGroup=ObjectGroup((1,3,6,1,4,1,9,10,107,2,1,3))
cpwVcMplsInboundGroup.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:cpwVcMplsInboundGroup.setStatus(_A)
cpwVcMplsMappingGroup=ObjectGroup((1,3,6,1,4,1,9,10,107,2,1,4))
cpwVcMplsMappingGroup.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:cpwVcMplsMappingGroup.setStatus(_A)
cpwMplsModuleCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,107,2,2,1))
cpwMplsModuleCompliance.setObjects(*((_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:cpwMplsModuleCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cpwVcMplsMIB':cpwVcMplsMIB,'cpwVcMplsNotifications':cpwVcMplsNotifications,'cpwVcMplsNotifyPrefix':cpwVcMplsNotifyPrefix,'cpwVcMplsObjects':cpwVcMplsObjects,'cpwVcMplsTable':cpwVcMplsTable,'cpwVcMplsEntry':cpwVcMplsEntry,_Z:cpwVcMplsMplsType,_a:cpwVcMplsExpBitsMode,_b:cpwVcMplsExpBits,_c:cpwVcMplsTtl,_d:cpwVcMplsLocalLdpID,_e:cpwVcMplsLocalLdpEntityID,_f:cpwVcMplsPeerLdpID,_g:cpwVcMplsStorageType,_h:cpwVcMplsOutboundIndexNext,'cpwVcMplsOutboundTable':cpwVcMplsOutboundTable,'cpwVcMplsOutboundEntry':cpwVcMplsOutboundEntry,_N:cpwVcMplsOutboundIndex,_i:cpwVcMplsOutboundLsrXcIndex,_j:cpwVcMplsOutboundTunnelIndex,_k:cpwVcMplsOutboundTunnelInstance,_l:cpwVcMplsOutboundTunnelLclLSR,_m:cpwVcMplsOutboundTunnelPeerLSR,_n:cpwVcMplsOutboundIfIndex,_o:cpwVcMplsOutboundRowStatus,_p:cpwVcMplsOutboundStorageType,_q:cpwVcMplsInboundIndexNext,'cpwVcMplsInboundTable':cpwVcMplsInboundTable,'cpwVcMplsInboundEntry':cpwVcMplsInboundEntry,_O:cpwVcMplsInboundIndex,_r:cpwVcMplsInboundLsrXcIndex,_s:cpwVcMplsInboundTunnelIndex,_t:cpwVcMplsInboundTunnelInstance,_u:cpwVcMplsInboundTunnelLclLSR,_v:cpwVcMplsInboundTunnelPeerLSR,_w:cpwVcMplsInboundIfIndex,_x:cpwVcMplsInboundRowStatus,_y:cpwVcMplsInboundStorageType,'cpwVcMplsNonTeMappingTable':cpwVcMplsNonTeMappingTable,'cpwVcMplsNonTeMappingEntry':cpwVcMplsNonTeMappingEntry,_P:cpwVcMplsNonTeMappingTunnelDirection,_Q:cpwVcMplsNonTeMappingXcTunnelIndex,_R:cpwVcMplsNonTeMappingIfIndex,_K:cpwVcMplsNonTeMappingVcIndex,'cpwVcMplsTeMappingTable':cpwVcMplsTeMappingTable,'cpwVcMplsTeMappingEntry':cpwVcMplsTeMappingEntry,_U:cpwVcMplsTeMappingTunnelDirection,_V:cpwVcMplsTeMappingTunnelIndex,_W:cpwVcMplsTeMappingTunnelInstance,_X:cpwVcMplsTeMappingTunnelPeerLsrID,_Y:cpwVcMplsTeMappingTunnelLocalLsrID,_L:cpwVcMplsTeMappingVcIndex,'cpwVcMplsConformance':cpwVcMplsConformance,'cpwVcMplsGroups':cpwVcMplsGroups,_z:cpwVcMplsGroup,_A0:cpwVcMplsOutboundGroup,_A2:cpwVcMplsInboundGroup,_A1:cpwVcMplsMappingGroup,'cpwVcMplsCompliances':cpwVcMplsCompliances,'cpwMplsModuleCompliance':cpwMplsModuleCompliance})