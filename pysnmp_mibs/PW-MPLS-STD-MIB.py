_r='pwMplsInboundXcIndex'
_q='pwMplsOutboundTunnelPeerLSR'
_p='pwMplsOutboundTunnelLclLSR'
_o='pwMplsOutboundTunnelInstance'
_n='pwMplsOutboundTunnelIndex'
_m='pwMplsOutboundTunnelTypeInUse'
_l='pwMplsOutboundIfIndex'
_k='pwMplsOutboundLsrXcIndex'
_j='pwMplsStorageType'
_i='pwMplsPeerLdpID'
_h='pwMplsLocalLdpEntityIndex'
_g='pwMplsLocalLdpID'
_f='pwMplsTtl'
_e='pwMplsExpBits'
_d='pwMplsExpBitsMode'
_c='pwMplsMplsType'
_b='pwMplsOutboundEntry'
_a='pwMplsTeMappingTunnelLocalLsrID'
_Z='pwMplsTeMappingTunnelPeerLsrID'
_Y='pwMplsTeMappingTunnelInstance'
_X='pwMplsTeMappingTunnelIndex'
_W='pwMplsNonTeMappingIfIndex'
_V='pwMplsNonTeMappingXcIndex'
_U='pwMplsNonTeMappingDirection'
_T='pwOnly'
_S='mplsNonTe'
_R='mplsTe'
_Q='StorageType'
_P='pwMplsOutboundTeGroup'
_O='pwMplsMappingGroup'
_N='pwMplsInboundGroup'
_M='pwMplsOutboundMainGroup'
_L='pwMplsGroup'
_K='pwMplsTeMappingPwIndex'
_J='pwMplsNonTeMappingPwIndex'
_I='pwIndex'
_H='PW-STD-MIB'
_G='Unsigned32'
_F='Integer32'
_E='read-only'
_D='not-accessible'
_C='read-write'
_B='PW-MPLS-STD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
MplsIndexType,=mibBuilder.importSymbols('MPLS-LSR-STD-MIB','MplsIndexType')
MplsLdpIdentifier,MplsLsrIdentifier,MplsTunnelIndex,MplsTunnelInstanceIndex=mibBuilder.importSymbols('MPLS-TC-STD-MIB','MplsLdpIdentifier','MplsLsrIdentifier','MplsTunnelIndex','MplsTunnelInstanceIndex')
pwIndex,=mibBuilder.importSymbols(_H,_I)
PwIndexType,=mibBuilder.importSymbols('PW-TC-STD-MIB','PwIndexType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso','mib-2')
DisplayString,PhysAddress,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress',_Q,'TextualConvention')
pwMplsStdMIB=ModuleIdentity((1,3,6,1,2,1,181))
if mibBuilder.loadTexts:pwMplsStdMIB.setRevisions(('2009-06-12 00:00',))
_PwMplsNotifications_ObjectIdentity=ObjectIdentity
pwMplsNotifications=_PwMplsNotifications_ObjectIdentity((1,3,6,1,2,1,181,0))
_PwMplsObjects_ObjectIdentity=ObjectIdentity
pwMplsObjects=_PwMplsObjects_ObjectIdentity((1,3,6,1,2,1,181,1))
_PwMplsTable_Object=MibTable
pwMplsTable=_PwMplsTable_Object((1,3,6,1,2,1,181,1,1))
if mibBuilder.loadTexts:pwMplsTable.setStatus(_A)
_PwMplsEntry_Object=MibTableRow
pwMplsEntry=_PwMplsEntry_Object((1,3,6,1,2,1,181,1,1,1))
pwMplsEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:pwMplsEntry.setStatus(_A)
class _PwMplsMplsType_Type(Bits):defaultBinValue='01';namedValues=NamedValues(*((_R,0),(_S,1),(_T,2)))
_PwMplsMplsType_Type.__name__='Bits'
_PwMplsMplsType_Object=MibTableColumn
pwMplsMplsType=_PwMplsMplsType_Object((1,3,6,1,2,1,181,1,1,1,1),_PwMplsMplsType_Type())
pwMplsMplsType.setMaxAccess(_C)
if mibBuilder.loadTexts:pwMplsMplsType.setStatus(_A)
class _PwMplsExpBitsMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('outerTunnel',1),('specifiedValue',2),('serviceDependant',3)))
_PwMplsExpBitsMode_Type.__name__=_F
_PwMplsExpBitsMode_Object=MibTableColumn
pwMplsExpBitsMode=_PwMplsExpBitsMode_Object((1,3,6,1,2,1,181,1,1,1,2),_PwMplsExpBitsMode_Type())
pwMplsExpBitsMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pwMplsExpBitsMode.setStatus(_A)
class _PwMplsExpBits_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PwMplsExpBits_Type.__name__=_G
_PwMplsExpBits_Object=MibTableColumn
pwMplsExpBits=_PwMplsExpBits_Object((1,3,6,1,2,1,181,1,1,1,3),_PwMplsExpBits_Type())
pwMplsExpBits.setMaxAccess(_C)
if mibBuilder.loadTexts:pwMplsExpBits.setStatus(_A)
class _PwMplsTtl_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PwMplsTtl_Type.__name__=_G
_PwMplsTtl_Object=MibTableColumn
pwMplsTtl=_PwMplsTtl_Object((1,3,6,1,2,1,181,1,1,1,4),_PwMplsTtl_Type())
pwMplsTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:pwMplsTtl.setStatus(_A)
_PwMplsLocalLdpID_Type=MplsLdpIdentifier
_PwMplsLocalLdpID_Object=MibTableColumn
pwMplsLocalLdpID=_PwMplsLocalLdpID_Object((1,3,6,1,2,1,181,1,1,1,5),_PwMplsLocalLdpID_Type())
pwMplsLocalLdpID.setMaxAccess(_C)
if mibBuilder.loadTexts:pwMplsLocalLdpID.setStatus(_A)
class _PwMplsLocalLdpEntityIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_PwMplsLocalLdpEntityIndex_Type.__name__=_G
_PwMplsLocalLdpEntityIndex_Object=MibTableColumn
pwMplsLocalLdpEntityIndex=_PwMplsLocalLdpEntityIndex_Object((1,3,6,1,2,1,181,1,1,1,6),_PwMplsLocalLdpEntityIndex_Type())
pwMplsLocalLdpEntityIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pwMplsLocalLdpEntityIndex.setStatus(_A)
_PwMplsPeerLdpID_Type=MplsLdpIdentifier
_PwMplsPeerLdpID_Object=MibTableColumn
pwMplsPeerLdpID=_PwMplsPeerLdpID_Object((1,3,6,1,2,1,181,1,1,1,7),_PwMplsPeerLdpID_Type())
pwMplsPeerLdpID.setMaxAccess(_E)
if mibBuilder.loadTexts:pwMplsPeerLdpID.setStatus(_A)
class _PwMplsStorageType_Type(StorageType):defaultValue=3
_PwMplsStorageType_Type.__name__=_Q
_PwMplsStorageType_Object=MibTableColumn
pwMplsStorageType=_PwMplsStorageType_Object((1,3,6,1,2,1,181,1,1,1,8),_PwMplsStorageType_Type())
pwMplsStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:pwMplsStorageType.setStatus(_A)
_PwMplsOutboundTable_Object=MibTable
pwMplsOutboundTable=_PwMplsOutboundTable_Object((1,3,6,1,2,1,181,1,2))
if mibBuilder.loadTexts:pwMplsOutboundTable.setStatus(_A)
_PwMplsOutboundEntry_Object=MibTableRow
pwMplsOutboundEntry=_PwMplsOutboundEntry_Object((1,3,6,1,2,1,181,1,2,1))
if mibBuilder.loadTexts:pwMplsOutboundEntry.setStatus(_A)
_PwMplsOutboundLsrXcIndex_Type=MplsIndexType
_PwMplsOutboundLsrXcIndex_Object=MibTableColumn
pwMplsOutboundLsrXcIndex=_PwMplsOutboundLsrXcIndex_Object((1,3,6,1,2,1,181,1,2,1,1),_PwMplsOutboundLsrXcIndex_Type())
pwMplsOutboundLsrXcIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pwMplsOutboundLsrXcIndex.setStatus(_A)
_PwMplsOutboundTunnelIndex_Type=MplsTunnelIndex
_PwMplsOutboundTunnelIndex_Object=MibTableColumn
pwMplsOutboundTunnelIndex=_PwMplsOutboundTunnelIndex_Object((1,3,6,1,2,1,181,1,2,1,2),_PwMplsOutboundTunnelIndex_Type())
pwMplsOutboundTunnelIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pwMplsOutboundTunnelIndex.setStatus(_A)
_PwMplsOutboundTunnelInstance_Type=MplsTunnelInstanceIndex
_PwMplsOutboundTunnelInstance_Object=MibTableColumn
pwMplsOutboundTunnelInstance=_PwMplsOutboundTunnelInstance_Object((1,3,6,1,2,1,181,1,2,1,3),_PwMplsOutboundTunnelInstance_Type())
pwMplsOutboundTunnelInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:pwMplsOutboundTunnelInstance.setStatus(_A)
_PwMplsOutboundTunnelLclLSR_Type=MplsLsrIdentifier
_PwMplsOutboundTunnelLclLSR_Object=MibTableColumn
pwMplsOutboundTunnelLclLSR=_PwMplsOutboundTunnelLclLSR_Object((1,3,6,1,2,1,181,1,2,1,4),_PwMplsOutboundTunnelLclLSR_Type())
pwMplsOutboundTunnelLclLSR.setMaxAccess(_C)
if mibBuilder.loadTexts:pwMplsOutboundTunnelLclLSR.setStatus(_A)
_PwMplsOutboundTunnelPeerLSR_Type=MplsLsrIdentifier
_PwMplsOutboundTunnelPeerLSR_Object=MibTableColumn
pwMplsOutboundTunnelPeerLSR=_PwMplsOutboundTunnelPeerLSR_Object((1,3,6,1,2,1,181,1,2,1,5),_PwMplsOutboundTunnelPeerLSR_Type())
pwMplsOutboundTunnelPeerLSR.setMaxAccess(_C)
if mibBuilder.loadTexts:pwMplsOutboundTunnelPeerLSR.setStatus(_A)
_PwMplsOutboundIfIndex_Type=InterfaceIndexOrZero
_PwMplsOutboundIfIndex_Object=MibTableColumn
pwMplsOutboundIfIndex=_PwMplsOutboundIfIndex_Object((1,3,6,1,2,1,181,1,2,1,6),_PwMplsOutboundIfIndex_Type())
pwMplsOutboundIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pwMplsOutboundIfIndex.setStatus(_A)
class _PwMplsOutboundTunnelTypeInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notYetKnown',1),(_R,2),(_S,3),(_T,4)))
_PwMplsOutboundTunnelTypeInUse_Type.__name__=_F
_PwMplsOutboundTunnelTypeInUse_Object=MibTableColumn
pwMplsOutboundTunnelTypeInUse=_PwMplsOutboundTunnelTypeInUse_Object((1,3,6,1,2,1,181,1,2,1,7),_PwMplsOutboundTunnelTypeInUse_Type())
pwMplsOutboundTunnelTypeInUse.setMaxAccess(_E)
if mibBuilder.loadTexts:pwMplsOutboundTunnelTypeInUse.setStatus(_A)
_PwMplsInboundTable_Object=MibTable
pwMplsInboundTable=_PwMplsInboundTable_Object((1,3,6,1,2,1,181,1,3))
if mibBuilder.loadTexts:pwMplsInboundTable.setStatus(_A)
_PwMplsInboundEntry_Object=MibTableRow
pwMplsInboundEntry=_PwMplsInboundEntry_Object((1,3,6,1,2,1,181,1,3,1))
pwMplsInboundEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:pwMplsInboundEntry.setStatus(_A)
_PwMplsInboundXcIndex_Type=MplsIndexType
_PwMplsInboundXcIndex_Object=MibTableColumn
pwMplsInboundXcIndex=_PwMplsInboundXcIndex_Object((1,3,6,1,2,1,181,1,3,1,1),_PwMplsInboundXcIndex_Type())
pwMplsInboundXcIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:pwMplsInboundXcIndex.setStatus(_A)
_PwMplsNonTeMappingTable_Object=MibTable
pwMplsNonTeMappingTable=_PwMplsNonTeMappingTable_Object((1,3,6,1,2,1,181,1,4))
if mibBuilder.loadTexts:pwMplsNonTeMappingTable.setStatus(_A)
_PwMplsNonTeMappingEntry_Object=MibTableRow
pwMplsNonTeMappingEntry=_PwMplsNonTeMappingEntry_Object((1,3,6,1,2,1,181,1,4,1))
pwMplsNonTeMappingEntry.setIndexNames((0,_B,_U),(0,_B,_V),(0,_B,_W),(0,_B,_J))
if mibBuilder.loadTexts:pwMplsNonTeMappingEntry.setStatus(_A)
class _PwMplsNonTeMappingDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('psnBound',1),('fromPsn',2)))
_PwMplsNonTeMappingDirection_Type.__name__=_F
_PwMplsNonTeMappingDirection_Object=MibTableColumn
pwMplsNonTeMappingDirection=_PwMplsNonTeMappingDirection_Object((1,3,6,1,2,1,181,1,4,1,1),_PwMplsNonTeMappingDirection_Type())
pwMplsNonTeMappingDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:pwMplsNonTeMappingDirection.setStatus(_A)
_PwMplsNonTeMappingXcIndex_Type=MplsIndexType
_PwMplsNonTeMappingXcIndex_Object=MibTableColumn
pwMplsNonTeMappingXcIndex=_PwMplsNonTeMappingXcIndex_Object((1,3,6,1,2,1,181,1,4,1,2),_PwMplsNonTeMappingXcIndex_Type())
pwMplsNonTeMappingXcIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:pwMplsNonTeMappingXcIndex.setStatus(_A)
_PwMplsNonTeMappingIfIndex_Type=InterfaceIndexOrZero
_PwMplsNonTeMappingIfIndex_Object=MibTableColumn
pwMplsNonTeMappingIfIndex=_PwMplsNonTeMappingIfIndex_Object((1,3,6,1,2,1,181,1,4,1,3),_PwMplsNonTeMappingIfIndex_Type())
pwMplsNonTeMappingIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:pwMplsNonTeMappingIfIndex.setStatus(_A)
_PwMplsNonTeMappingPwIndex_Type=PwIndexType
_PwMplsNonTeMappingPwIndex_Object=MibTableColumn
pwMplsNonTeMappingPwIndex=_PwMplsNonTeMappingPwIndex_Object((1,3,6,1,2,1,181,1,4,1,4),_PwMplsNonTeMappingPwIndex_Type())
pwMplsNonTeMappingPwIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:pwMplsNonTeMappingPwIndex.setStatus(_A)
_PwMplsTeMappingTable_Object=MibTable
pwMplsTeMappingTable=_PwMplsTeMappingTable_Object((1,3,6,1,2,1,181,1,5))
if mibBuilder.loadTexts:pwMplsTeMappingTable.setStatus(_A)
_PwMplsTeMappingEntry_Object=MibTableRow
pwMplsTeMappingEntry=_PwMplsTeMappingEntry_Object((1,3,6,1,2,1,181,1,5,1))
pwMplsTeMappingEntry.setIndexNames((0,_B,_X),(0,_B,_Y),(0,_B,_Z),(0,_B,_a),(0,_B,_K))
if mibBuilder.loadTexts:pwMplsTeMappingEntry.setStatus(_A)
_PwMplsTeMappingTunnelIndex_Type=MplsTunnelIndex
_PwMplsTeMappingTunnelIndex_Object=MibTableColumn
pwMplsTeMappingTunnelIndex=_PwMplsTeMappingTunnelIndex_Object((1,3,6,1,2,1,181,1,5,1,1),_PwMplsTeMappingTunnelIndex_Type())
pwMplsTeMappingTunnelIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:pwMplsTeMappingTunnelIndex.setStatus(_A)
_PwMplsTeMappingTunnelInstance_Type=MplsTunnelInstanceIndex
_PwMplsTeMappingTunnelInstance_Object=MibTableColumn
pwMplsTeMappingTunnelInstance=_PwMplsTeMappingTunnelInstance_Object((1,3,6,1,2,1,181,1,5,1,2),_PwMplsTeMappingTunnelInstance_Type())
pwMplsTeMappingTunnelInstance.setMaxAccess(_D)
if mibBuilder.loadTexts:pwMplsTeMappingTunnelInstance.setStatus(_A)
_PwMplsTeMappingTunnelPeerLsrID_Type=MplsLsrIdentifier
_PwMplsTeMappingTunnelPeerLsrID_Object=MibTableColumn
pwMplsTeMappingTunnelPeerLsrID=_PwMplsTeMappingTunnelPeerLsrID_Object((1,3,6,1,2,1,181,1,5,1,3),_PwMplsTeMappingTunnelPeerLsrID_Type())
pwMplsTeMappingTunnelPeerLsrID.setMaxAccess(_D)
if mibBuilder.loadTexts:pwMplsTeMappingTunnelPeerLsrID.setStatus(_A)
_PwMplsTeMappingTunnelLocalLsrID_Type=MplsLsrIdentifier
_PwMplsTeMappingTunnelLocalLsrID_Object=MibTableColumn
pwMplsTeMappingTunnelLocalLsrID=_PwMplsTeMappingTunnelLocalLsrID_Object((1,3,6,1,2,1,181,1,5,1,4),_PwMplsTeMappingTunnelLocalLsrID_Type())
pwMplsTeMappingTunnelLocalLsrID.setMaxAccess(_D)
if mibBuilder.loadTexts:pwMplsTeMappingTunnelLocalLsrID.setStatus(_A)
_PwMplsTeMappingPwIndex_Type=PwIndexType
_PwMplsTeMappingPwIndex_Object=MibTableColumn
pwMplsTeMappingPwIndex=_PwMplsTeMappingPwIndex_Object((1,3,6,1,2,1,181,1,5,1,5),_PwMplsTeMappingPwIndex_Type())
pwMplsTeMappingPwIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:pwMplsTeMappingPwIndex.setStatus(_A)
_PwMplsConformance_ObjectIdentity=ObjectIdentity
pwMplsConformance=_PwMplsConformance_ObjectIdentity((1,3,6,1,2,1,181,2))
_PwMplsGroups_ObjectIdentity=ObjectIdentity
pwMplsGroups=_PwMplsGroups_ObjectIdentity((1,3,6,1,2,1,181,2,1))
_PwMplsCompliances_ObjectIdentity=ObjectIdentity
pwMplsCompliances=_PwMplsCompliances_ObjectIdentity((1,3,6,1,2,1,181,2,2))
pwMplsEntry.registerAugmentions((_B,_b))
pwMplsOutboundEntry.setIndexNames(*pwMplsEntry.getIndexNames())
pwMplsGroup=ObjectGroup((1,3,6,1,2,1,181,2,1,1))
pwMplsGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:pwMplsGroup.setStatus(_A)
pwMplsOutboundMainGroup=ObjectGroup((1,3,6,1,2,1,181,2,1,2))
pwMplsOutboundMainGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:pwMplsOutboundMainGroup.setStatus(_A)
pwMplsOutboundTeGroup=ObjectGroup((1,3,6,1,2,1,181,2,1,3))
pwMplsOutboundTeGroup.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:pwMplsOutboundTeGroup.setStatus(_A)
pwMplsInboundGroup=ObjectGroup((1,3,6,1,2,1,181,2,1,4))
pwMplsInboundGroup.setObjects((_B,_r))
if mibBuilder.loadTexts:pwMplsInboundGroup.setStatus(_A)
pwMplsMappingGroup=ObjectGroup((1,3,6,1,2,1,181,2,1,5))
pwMplsMappingGroup.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:pwMplsMappingGroup.setStatus(_A)
pwMplsModuleFullCompliance=ModuleCompliance((1,3,6,1,2,1,181,2,2,1))
pwMplsModuleFullCompliance.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:pwMplsModuleFullCompliance.setStatus(_A)
pwMplsModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,181,2,2,2))
pwMplsModuleReadOnlyCompliance.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:pwMplsModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pwMplsStdMIB':pwMplsStdMIB,'pwMplsNotifications':pwMplsNotifications,'pwMplsObjects':pwMplsObjects,'pwMplsTable':pwMplsTable,'pwMplsEntry':pwMplsEntry,_c:pwMplsMplsType,_d:pwMplsExpBitsMode,_e:pwMplsExpBits,_f:pwMplsTtl,_g:pwMplsLocalLdpID,_h:pwMplsLocalLdpEntityIndex,_i:pwMplsPeerLdpID,_j:pwMplsStorageType,'pwMplsOutboundTable':pwMplsOutboundTable,_b:pwMplsOutboundEntry,_k:pwMplsOutboundLsrXcIndex,_n:pwMplsOutboundTunnelIndex,_o:pwMplsOutboundTunnelInstance,_p:pwMplsOutboundTunnelLclLSR,_q:pwMplsOutboundTunnelPeerLSR,_l:pwMplsOutboundIfIndex,_m:pwMplsOutboundTunnelTypeInUse,'pwMplsInboundTable':pwMplsInboundTable,'pwMplsInboundEntry':pwMplsInboundEntry,_r:pwMplsInboundXcIndex,'pwMplsNonTeMappingTable':pwMplsNonTeMappingTable,'pwMplsNonTeMappingEntry':pwMplsNonTeMappingEntry,_U:pwMplsNonTeMappingDirection,_V:pwMplsNonTeMappingXcIndex,_W:pwMplsNonTeMappingIfIndex,_J:pwMplsNonTeMappingPwIndex,'pwMplsTeMappingTable':pwMplsTeMappingTable,'pwMplsTeMappingEntry':pwMplsTeMappingEntry,_X:pwMplsTeMappingTunnelIndex,_Y:pwMplsTeMappingTunnelInstance,_Z:pwMplsTeMappingTunnelPeerLsrID,_a:pwMplsTeMappingTunnelLocalLsrID,_K:pwMplsTeMappingPwIndex,'pwMplsConformance':pwMplsConformance,'pwMplsGroups':pwMplsGroups,_L:pwMplsGroup,_M:pwMplsOutboundMainGroup,_P:pwMplsOutboundTeGroup,_N:pwMplsInboundGroup,_O:pwMplsMappingGroup,'pwMplsCompliances':pwMplsCompliances,'pwMplsModuleFullCompliance':pwMplsModuleFullCompliance,'pwMplsModuleReadOnlyCompliance':pwMplsModuleReadOnlyCompliance})