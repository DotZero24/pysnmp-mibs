_B6='mplsXCIsNotPersistentGroup'
_B5='mplsXCIsPersistentGroup'
_B4='mplsTrafficParamGroup'
_B3='mplsHCOutSegmentPerfGroup'
_B2='mplsHCInSegmentPerfGroup'
_B1='mplsSegmentDiscontinuityGroup'
_B0='mplsPerfGroup'
_A_='mplsInterfaceGroup'
_Az='mplsXCGroup'
_Ay='mplsOutSegmentGroup'
_Ax='mplsInSegmentGroup'
_Aw='mplsXCDown'
_Av='mplsOutSegmentDown'
_Au='mplsOutSegmentUp'
_At='mplsInSegmentDown'
_As='mplsInSegmentUp'
_Ar='mplsOutSegmentPerfDiscontinuityTime'
_Aq='mplsInSegmentPerfDiscontinuityTime'
_Ap='mplsLabelStackIndexNext'
_Ao='mplsMaxLabelStackDepth'
_An='mplsLabelStackStorageType'
_Am='mplsLabelStackRowStatus'
_Al='mplsLabelStackLabel'
_Ak='mplsTrafficParamStorageType'
_Aj='mplsTrafficParamRowStatus'
_Ai='mplsTrafficParamMaxBurstSize'
_Ah='mplsTrafficParamMeanRate'
_Ag='mplsTrafficParamMaxRate'
_Af='mplsTrafficParamIndexNext'
_Ae='mplsOutSegmentHCOctets'
_Ad='mplsInSegmentHCOctets'
_Ac='mplsInterfaceOutLabelsUsed'
_Ab='mplsInterfaceOutFragments'
_Aa='mplsInterfaceOutDiscards'
_AZ='mplsInterfaceOutPackets'
_AY='mplsInterfaceFailedLabelLookup'
_AX='mplsInterfaceInDiscards'
_AW='mplsInterfaceInPackets'
_AV='mplsInterfaceInLabelsUsed'
_AU='mplsOutSegmentPackets'
_AT='mplsInSegmentErrors'
_AS='mplsInSegmentPackets'
_AR='mplsXCStorageType'
_AQ='mplsXCTrapEnable'
_AP='mplsXCRowStatus'
_AO='mplsXCOwner'
_AN='mplsXCLabelStackIndex'
_AM='mplsXCLspId'
_AL='mplsXCIndexNext'
_AK='mplsOutSegmentTrafficParamPtr'
_AJ='mplsOutSegmentStorageType'
_AI='mplsOutSegmentTrapEnable'
_AH='mplsOutSegmentRowStatus'
_AG='mplsOutSegmentOperStatus'
_AF='mplsOutSegmentAdminStatus'
_AE='mplsOutSegmentErrors'
_AD='mplsOutSegmentOwner'
_AC='mplsOutSegmentXCIndex'
_AB='mplsOutSegmentNextHopIpv6Addr'
_AA='mplsOutSegmentNextHopIpv4Addr'
_A9='mplsOutSegmentNextHopIpAddrType'
_A8='mplsOutSegmentTopLabel'
_A7='mplsOutSegmentPushTopLabel'
_A6='mplsOutSegmentIfIndex'
_A5='mplsOutSegmentIndexNext'
_A4='mplsInSegmentTrafficParamPtr'
_A3='mplsInSegmentStorageType'
_A2='mplsInSegmentTrapEnable'
_A1='mplsInSegmentRowStatus'
_A0='mplsInSegmentOwner'
_z='mplsInSegmentXCIndex'
_y='mplsInSegmentAddrFamily'
_x='mplsInSegmentNPop'
_w='mplsInterfaceConfStorageType'
_v='mplsInterfaceLabelParticipationType'
_u='mplsInterfaceAvailableBuffer'
_t='mplsInterfaceTotalBuffer'
_s='mplsInterfaceAvailableBandwidth'
_r='mplsInterfaceTotalBandwidth'
_q='mplsInterfaceLabelMaxOut'
_p='mplsInterfaceLabelMinOut'
_o='mplsInterfaceLabelMaxIn'
_n='mplsInterfaceLabelMinIn'
_m='mplsOutSegmentPerfEntry'
_l='mplsInSegmentPerfEntry'
_k='mplsInterfacePerfEntry'
_j='kilobits per second'
_i='mplsTrafficParamIndex'
_h='mplsLabelStackLabelIndex'
_g='mplsLabelStackIndex'
_f='mplsInterfaceConfIndex'
_e='InetAddressType'
_d='AddressFamilyNumbers'
_c='mplsXCIsPersistent'
_b='mplsOutSegmentDiscards'
_a='mplsOutSegmentOctets'
_Z='mplsInSegmentDiscards'
_Y='mplsInSegmentOctets'
_X='read-write'
_W='lowerLayerDown'
_V='notPresent'
_U='dormant'
_T='MplsObjectOwner'
_S='mplsXCOperStatus'
_R='mplsXCAdminStatus'
_Q='mplsXCIndex'
_P='unknown'
_O='TruthValue'
_N='mplsInSegmentOperStatus'
_M='mplsInSegmentAdminStatus'
_L='testing'
_K='down'
_J='up'
_I='mplsOutSegmentIndex'
_H='mplsInSegmentLabel'
_G='mplsInSegmentIfIndex'
_F='not-accessible'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='current'
_A='MPLS-LSR-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AddressFamilyNumbers,=mibBuilder.importSymbols('IANA-ADDRESS-FAMILY-NUMBERS-MIB',_d)
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddressIPv4,InetAddressIPv6,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6',_e)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','experimental','iso')
DisplayString,PhysAddress,RowPointer,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','RowStatus','StorageType','TextualConvention','TimeStamp',_O)
mplsLsrMIB=ModuleIdentity((1,3,6,1,3,96))
if mibBuilder.loadTexts:mplsLsrMIB.setRevisions(('1999-06-16 12:00','2000-02-16 12:00','2000-03-06 12:00','2000-04-21 12:00','2000-04-26 12:00'))
class MplsLSPID(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
class MplsLabel(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class MplsBitRate(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class MplsBurstSize(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class MplsBufferSize(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class MplsObjectOwner(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('snmp',2),('ldp',3),('rsvp',4),('policyAgent',5),(_P,6)))
_MplsLsrObjects_ObjectIdentity=ObjectIdentity
mplsLsrObjects=_MplsLsrObjects_ObjectIdentity((1,3,6,1,3,96,1))
_MplsInterfaceConfTable_Object=MibTable
mplsInterfaceConfTable=_MplsInterfaceConfTable_Object((1,3,6,1,3,96,1,1))
if mibBuilder.loadTexts:mplsInterfaceConfTable.setStatus(_B)
_MplsInterfaceConfEntry_Object=MibTableRow
mplsInterfaceConfEntry=_MplsInterfaceConfEntry_Object((1,3,6,1,3,96,1,1,1))
mplsInterfaceConfEntry.setIndexNames((0,_A,_f))
if mibBuilder.loadTexts:mplsInterfaceConfEntry.setStatus(_B)
_MplsInterfaceConfIndex_Type=InterfaceIndexOrZero
_MplsInterfaceConfIndex_Object=MibTableColumn
mplsInterfaceConfIndex=_MplsInterfaceConfIndex_Object((1,3,6,1,3,96,1,1,1,1),_MplsInterfaceConfIndex_Type())
mplsInterfaceConfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsInterfaceConfIndex.setStatus(_B)
_MplsInterfaceLabelMinIn_Type=MplsLabel
_MplsInterfaceLabelMinIn_Object=MibTableColumn
mplsInterfaceLabelMinIn=_MplsInterfaceLabelMinIn_Object((1,3,6,1,3,96,1,1,1,2),_MplsInterfaceLabelMinIn_Type())
mplsInterfaceLabelMinIn.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceLabelMinIn.setStatus(_B)
_MplsInterfaceLabelMaxIn_Type=MplsLabel
_MplsInterfaceLabelMaxIn_Object=MibTableColumn
mplsInterfaceLabelMaxIn=_MplsInterfaceLabelMaxIn_Object((1,3,6,1,3,96,1,1,1,3),_MplsInterfaceLabelMaxIn_Type())
mplsInterfaceLabelMaxIn.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceLabelMaxIn.setStatus(_B)
_MplsInterfaceLabelMinOut_Type=MplsLabel
_MplsInterfaceLabelMinOut_Object=MibTableColumn
mplsInterfaceLabelMinOut=_MplsInterfaceLabelMinOut_Object((1,3,6,1,3,96,1,1,1,4),_MplsInterfaceLabelMinOut_Type())
mplsInterfaceLabelMinOut.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceLabelMinOut.setStatus(_B)
_MplsInterfaceLabelMaxOut_Type=MplsLabel
_MplsInterfaceLabelMaxOut_Object=MibTableColumn
mplsInterfaceLabelMaxOut=_MplsInterfaceLabelMaxOut_Object((1,3,6,1,3,96,1,1,1,5),_MplsInterfaceLabelMaxOut_Type())
mplsInterfaceLabelMaxOut.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceLabelMaxOut.setStatus(_B)
_MplsInterfaceTotalBandwidth_Type=MplsBitRate
_MplsInterfaceTotalBandwidth_Object=MibTableColumn
mplsInterfaceTotalBandwidth=_MplsInterfaceTotalBandwidth_Object((1,3,6,1,3,96,1,1,1,6),_MplsInterfaceTotalBandwidth_Type())
mplsInterfaceTotalBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceTotalBandwidth.setStatus(_B)
_MplsInterfaceAvailableBandwidth_Type=MplsBitRate
_MplsInterfaceAvailableBandwidth_Object=MibTableColumn
mplsInterfaceAvailableBandwidth=_MplsInterfaceAvailableBandwidth_Object((1,3,6,1,3,96,1,1,1,7),_MplsInterfaceAvailableBandwidth_Type())
mplsInterfaceAvailableBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceAvailableBandwidth.setStatus(_B)
_MplsInterfaceTotalBuffer_Type=MplsBufferSize
_MplsInterfaceTotalBuffer_Object=MibTableColumn
mplsInterfaceTotalBuffer=_MplsInterfaceTotalBuffer_Object((1,3,6,1,3,96,1,1,1,8),_MplsInterfaceTotalBuffer_Type())
mplsInterfaceTotalBuffer.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceTotalBuffer.setStatus(_B)
_MplsInterfaceAvailableBuffer_Type=MplsBufferSize
_MplsInterfaceAvailableBuffer_Object=MibTableColumn
mplsInterfaceAvailableBuffer=_MplsInterfaceAvailableBuffer_Object((1,3,6,1,3,96,1,1,1,9),_MplsInterfaceAvailableBuffer_Type())
mplsInterfaceAvailableBuffer.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceAvailableBuffer.setStatus(_B)
class _MplsInterfaceLabelParticipationType_Type(Bits):namedValues=NamedValues(*(('perPlatform',0),('perInterface',1)))
_MplsInterfaceLabelParticipationType_Type.__name__='Bits'
_MplsInterfaceLabelParticipationType_Object=MibTableColumn
mplsInterfaceLabelParticipationType=_MplsInterfaceLabelParticipationType_Object((1,3,6,1,3,96,1,1,1,10),_MplsInterfaceLabelParticipationType_Type())
mplsInterfaceLabelParticipationType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceLabelParticipationType.setStatus(_B)
_MplsInterfaceConfStorageType_Type=StorageType
_MplsInterfaceConfStorageType_Object=MibTableColumn
mplsInterfaceConfStorageType=_MplsInterfaceConfStorageType_Object((1,3,6,1,3,96,1,1,1,11),_MplsInterfaceConfStorageType_Type())
mplsInterfaceConfStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInterfaceConfStorageType.setStatus(_B)
_MplsInterfacePerfTable_Object=MibTable
mplsInterfacePerfTable=_MplsInterfacePerfTable_Object((1,3,6,1,3,96,1,2))
if mibBuilder.loadTexts:mplsInterfacePerfTable.setStatus(_B)
_MplsInterfacePerfEntry_Object=MibTableRow
mplsInterfacePerfEntry=_MplsInterfacePerfEntry_Object((1,3,6,1,3,96,1,2,1))
if mibBuilder.loadTexts:mplsInterfacePerfEntry.setStatus(_B)
_MplsInterfaceInLabelsUsed_Type=Gauge32
_MplsInterfaceInLabelsUsed_Object=MibTableColumn
mplsInterfaceInLabelsUsed=_MplsInterfaceInLabelsUsed_Object((1,3,6,1,3,96,1,2,1,1),_MplsInterfaceInLabelsUsed_Type())
mplsInterfaceInLabelsUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceInLabelsUsed.setStatus(_B)
_MplsInterfaceInPackets_Type=Counter32
_MplsInterfaceInPackets_Object=MibTableColumn
mplsInterfaceInPackets=_MplsInterfaceInPackets_Object((1,3,6,1,3,96,1,2,1,2),_MplsInterfaceInPackets_Type())
mplsInterfaceInPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceInPackets.setStatus(_B)
_MplsInterfaceInDiscards_Type=Counter32
_MplsInterfaceInDiscards_Object=MibTableColumn
mplsInterfaceInDiscards=_MplsInterfaceInDiscards_Object((1,3,6,1,3,96,1,2,1,3),_MplsInterfaceInDiscards_Type())
mplsInterfaceInDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceInDiscards.setStatus(_B)
_MplsInterfaceFailedLabelLookup_Type=Counter32
_MplsInterfaceFailedLabelLookup_Object=MibTableColumn
mplsInterfaceFailedLabelLookup=_MplsInterfaceFailedLabelLookup_Object((1,3,6,1,3,96,1,2,1,4),_MplsInterfaceFailedLabelLookup_Type())
mplsInterfaceFailedLabelLookup.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceFailedLabelLookup.setStatus(_B)
_MplsInterfaceOutLabelsUsed_Type=Gauge32
_MplsInterfaceOutLabelsUsed_Object=MibTableColumn
mplsInterfaceOutLabelsUsed=_MplsInterfaceOutLabelsUsed_Object((1,3,6,1,3,96,1,2,1,5),_MplsInterfaceOutLabelsUsed_Type())
mplsInterfaceOutLabelsUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceOutLabelsUsed.setStatus(_B)
_MplsInterfaceOutPackets_Type=Counter32
_MplsInterfaceOutPackets_Object=MibTableColumn
mplsInterfaceOutPackets=_MplsInterfaceOutPackets_Object((1,3,6,1,3,96,1,2,1,6),_MplsInterfaceOutPackets_Type())
mplsInterfaceOutPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceOutPackets.setStatus(_B)
_MplsInterfaceOutDiscards_Type=Counter32
_MplsInterfaceOutDiscards_Object=MibTableColumn
mplsInterfaceOutDiscards=_MplsInterfaceOutDiscards_Object((1,3,6,1,3,96,1,2,1,7),_MplsInterfaceOutDiscards_Type())
mplsInterfaceOutDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceOutDiscards.setStatus(_B)
_MplsInterfaceOutFragments_Type=Counter32
_MplsInterfaceOutFragments_Object=MibTableColumn
mplsInterfaceOutFragments=_MplsInterfaceOutFragments_Object((1,3,6,1,3,96,1,2,1,8),_MplsInterfaceOutFragments_Type())
mplsInterfaceOutFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceOutFragments.setStatus(_B)
_MplsInSegmentTable_Object=MibTable
mplsInSegmentTable=_MplsInSegmentTable_Object((1,3,6,1,3,96,1,3))
if mibBuilder.loadTexts:mplsInSegmentTable.setStatus(_B)
_MplsInSegmentEntry_Object=MibTableRow
mplsInSegmentEntry=_MplsInSegmentEntry_Object((1,3,6,1,3,96,1,3,1))
mplsInSegmentEntry.setIndexNames((0,_A,_G),(0,_A,_H))
if mibBuilder.loadTexts:mplsInSegmentEntry.setStatus(_B)
_MplsInSegmentIfIndex_Type=InterfaceIndexOrZero
_MplsInSegmentIfIndex_Object=MibTableColumn
mplsInSegmentIfIndex=_MplsInSegmentIfIndex_Object((1,3,6,1,3,96,1,3,1,1),_MplsInSegmentIfIndex_Type())
mplsInSegmentIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsInSegmentIfIndex.setStatus(_B)
_MplsInSegmentLabel_Type=MplsLabel
_MplsInSegmentLabel_Object=MibTableColumn
mplsInSegmentLabel=_MplsInSegmentLabel_Object((1,3,6,1,3,96,1,3,1,2),_MplsInSegmentLabel_Type())
mplsInSegmentLabel.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsInSegmentLabel.setStatus(_B)
class _MplsInSegmentNPop_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsInSegmentNPop_Type.__name__=_E
_MplsInSegmentNPop_Object=MibTableColumn
mplsInSegmentNPop=_MplsInSegmentNPop_Object((1,3,6,1,3,96,1,3,1,3),_MplsInSegmentNPop_Type())
mplsInSegmentNPop.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentNPop.setStatus(_B)
class _MplsInSegmentAddrFamily_Type(AddressFamilyNumbers):defaultValue=0
_MplsInSegmentAddrFamily_Type.__name__=_d
_MplsInSegmentAddrFamily_Object=MibTableColumn
mplsInSegmentAddrFamily=_MplsInSegmentAddrFamily_Object((1,3,6,1,3,96,1,3,1,4),_MplsInSegmentAddrFamily_Type())
mplsInSegmentAddrFamily.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentAddrFamily.setStatus(_B)
class _MplsInSegmentXCIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsInSegmentXCIndex_Type.__name__=_E
_MplsInSegmentXCIndex_Object=MibTableColumn
mplsInSegmentXCIndex=_MplsInSegmentXCIndex_Object((1,3,6,1,3,96,1,3,1,5),_MplsInSegmentXCIndex_Type())
mplsInSegmentXCIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentXCIndex.setStatus(_B)
class _MplsInSegmentOwner_Type(MplsObjectOwner):defaultValue=6
_MplsInSegmentOwner_Type.__name__=_T
_MplsInSegmentOwner_Object=MibTableColumn
mplsInSegmentOwner=_MplsInSegmentOwner_Object((1,3,6,1,3,96,1,3,1,6),_MplsInSegmentOwner_Type())
mplsInSegmentOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentOwner.setStatus(_B)
_MplsInSegmentTrafficParamPtr_Type=RowPointer
_MplsInSegmentTrafficParamPtr_Object=MibTableColumn
mplsInSegmentTrafficParamPtr=_MplsInSegmentTrafficParamPtr_Object((1,3,6,1,3,96,1,3,1,7),_MplsInSegmentTrafficParamPtr_Type())
mplsInSegmentTrafficParamPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentTrafficParamPtr.setStatus(_B)
_MplsInSegmentRowStatus_Type=RowStatus
_MplsInSegmentRowStatus_Object=MibTableColumn
mplsInSegmentRowStatus=_MplsInSegmentRowStatus_Object((1,3,6,1,3,96,1,3,1,8),_MplsInSegmentRowStatus_Type())
mplsInSegmentRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentRowStatus.setStatus(_B)
_MplsInSegmentStorageType_Type=StorageType
_MplsInSegmentStorageType_Object=MibTableColumn
mplsInSegmentStorageType=_MplsInSegmentStorageType_Object((1,3,6,1,3,96,1,3,1,9),_MplsInSegmentStorageType_Type())
mplsInSegmentStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentStorageType.setStatus(_B)
class _MplsInSegmentAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3)))
_MplsInSegmentAdminStatus_Type.__name__=_E
_MplsInSegmentAdminStatus_Object=MibTableColumn
mplsInSegmentAdminStatus=_MplsInSegmentAdminStatus_Object((1,3,6,1,3,96,1,3,1,10),_MplsInSegmentAdminStatus_Type())
mplsInSegmentAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentAdminStatus.setStatus(_B)
class _MplsInSegmentOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_P,4),(_U,5),(_V,6),(_W,7)))
_MplsInSegmentOperStatus_Type.__name__=_E
_MplsInSegmentOperStatus_Object=MibTableColumn
mplsInSegmentOperStatus=_MplsInSegmentOperStatus_Object((1,3,6,1,3,96,1,3,1,11),_MplsInSegmentOperStatus_Type())
mplsInSegmentOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentOperStatus.setStatus(_B)
_MplsInSegmentPerfTable_Object=MibTable
mplsInSegmentPerfTable=_MplsInSegmentPerfTable_Object((1,3,6,1,3,96,1,4))
if mibBuilder.loadTexts:mplsInSegmentPerfTable.setStatus(_B)
_MplsInSegmentPerfEntry_Object=MibTableRow
mplsInSegmentPerfEntry=_MplsInSegmentPerfEntry_Object((1,3,6,1,3,96,1,4,1))
if mibBuilder.loadTexts:mplsInSegmentPerfEntry.setStatus(_B)
_MplsInSegmentOctets_Type=Counter32
_MplsInSegmentOctets_Object=MibTableColumn
mplsInSegmentOctets=_MplsInSegmentOctets_Object((1,3,6,1,3,96,1,4,1,1),_MplsInSegmentOctets_Type())
mplsInSegmentOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentOctets.setStatus(_B)
_MplsInSegmentPackets_Type=Counter32
_MplsInSegmentPackets_Object=MibTableColumn
mplsInSegmentPackets=_MplsInSegmentPackets_Object((1,3,6,1,3,96,1,4,1,2),_MplsInSegmentPackets_Type())
mplsInSegmentPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentPackets.setStatus(_B)
_MplsInSegmentErrors_Type=Counter32
_MplsInSegmentErrors_Object=MibTableColumn
mplsInSegmentErrors=_MplsInSegmentErrors_Object((1,3,6,1,3,96,1,4,1,3),_MplsInSegmentErrors_Type())
mplsInSegmentErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentErrors.setStatus(_B)
_MplsInSegmentDiscards_Type=Counter32
_MplsInSegmentDiscards_Object=MibTableColumn
mplsInSegmentDiscards=_MplsInSegmentDiscards_Object((1,3,6,1,3,96,1,4,1,4),_MplsInSegmentDiscards_Type())
mplsInSegmentDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentDiscards.setStatus(_B)
_MplsInSegmentHCOctets_Type=Counter64
_MplsInSegmentHCOctets_Object=MibTableColumn
mplsInSegmentHCOctets=_MplsInSegmentHCOctets_Object((1,3,6,1,3,96,1,4,1,5),_MplsInSegmentHCOctets_Type())
mplsInSegmentHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentHCOctets.setStatus(_B)
_MplsInSegmentPerfDiscontinuityTime_Type=TimeStamp
_MplsInSegmentPerfDiscontinuityTime_Object=MibTableColumn
mplsInSegmentPerfDiscontinuityTime=_MplsInSegmentPerfDiscontinuityTime_Object((1,3,6,1,3,96,1,4,1,6),_MplsInSegmentPerfDiscontinuityTime_Type())
mplsInSegmentPerfDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentPerfDiscontinuityTime.setStatus(_B)
class _MplsOutSegmentIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsOutSegmentIndexNext_Type.__name__=_E
_MplsOutSegmentIndexNext_Object=MibScalar
mplsOutSegmentIndexNext=_MplsOutSegmentIndexNext_Object((1,3,6,1,3,96,1,5),_MplsOutSegmentIndexNext_Type())
mplsOutSegmentIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentIndexNext.setStatus(_B)
_MplsOutSegmentTable_Object=MibTable
mplsOutSegmentTable=_MplsOutSegmentTable_Object((1,3,6,1,3,96,1,6))
if mibBuilder.loadTexts:mplsOutSegmentTable.setStatus(_B)
_MplsOutSegmentEntry_Object=MibTableRow
mplsOutSegmentEntry=_MplsOutSegmentEntry_Object((1,3,6,1,3,96,1,6,1))
mplsOutSegmentEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:mplsOutSegmentEntry.setStatus(_B)
class _MplsOutSegmentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsOutSegmentIndex_Type.__name__=_E
_MplsOutSegmentIndex_Object=MibTableColumn
mplsOutSegmentIndex=_MplsOutSegmentIndex_Object((1,3,6,1,3,96,1,6,1,1),_MplsOutSegmentIndex_Type())
mplsOutSegmentIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsOutSegmentIndex.setStatus(_B)
_MplsOutSegmentIfIndex_Type=InterfaceIndex
_MplsOutSegmentIfIndex_Object=MibTableColumn
mplsOutSegmentIfIndex=_MplsOutSegmentIfIndex_Object((1,3,6,1,3,96,1,6,1,2),_MplsOutSegmentIfIndex_Type())
mplsOutSegmentIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentIfIndex.setStatus(_B)
_MplsOutSegmentPushTopLabel_Type=TruthValue
_MplsOutSegmentPushTopLabel_Object=MibTableColumn
mplsOutSegmentPushTopLabel=_MplsOutSegmentPushTopLabel_Object((1,3,6,1,3,96,1,6,1,3),_MplsOutSegmentPushTopLabel_Type())
mplsOutSegmentPushTopLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentPushTopLabel.setStatus(_B)
_MplsOutSegmentTopLabel_Type=MplsLabel
_MplsOutSegmentTopLabel_Object=MibTableColumn
mplsOutSegmentTopLabel=_MplsOutSegmentTopLabel_Object((1,3,6,1,3,96,1,6,1,4),_MplsOutSegmentTopLabel_Type())
mplsOutSegmentTopLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentTopLabel.setStatus(_B)
class _MplsOutSegmentNextHopIpAddrType_Type(InetAddressType):defaultValue=0
_MplsOutSegmentNextHopIpAddrType_Type.__name__=_e
_MplsOutSegmentNextHopIpAddrType_Object=MibTableColumn
mplsOutSegmentNextHopIpAddrType=_MplsOutSegmentNextHopIpAddrType_Object((1,3,6,1,3,96,1,6,1,5),_MplsOutSegmentNextHopIpAddrType_Type())
mplsOutSegmentNextHopIpAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentNextHopIpAddrType.setStatus(_B)
_MplsOutSegmentNextHopIpv4Addr_Type=InetAddressIPv4
_MplsOutSegmentNextHopIpv4Addr_Object=MibTableColumn
mplsOutSegmentNextHopIpv4Addr=_MplsOutSegmentNextHopIpv4Addr_Object((1,3,6,1,3,96,1,6,1,6),_MplsOutSegmentNextHopIpv4Addr_Type())
mplsOutSegmentNextHopIpv4Addr.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentNextHopIpv4Addr.setStatus(_B)
_MplsOutSegmentNextHopIpv6Addr_Type=InetAddressIPv6
_MplsOutSegmentNextHopIpv6Addr_Object=MibTableColumn
mplsOutSegmentNextHopIpv6Addr=_MplsOutSegmentNextHopIpv6Addr_Object((1,3,6,1,3,96,1,6,1,7),_MplsOutSegmentNextHopIpv6Addr_Type())
mplsOutSegmentNextHopIpv6Addr.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentNextHopIpv6Addr.setStatus(_B)
class _MplsOutSegmentXCIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsOutSegmentXCIndex_Type.__name__=_E
_MplsOutSegmentXCIndex_Object=MibTableColumn
mplsOutSegmentXCIndex=_MplsOutSegmentXCIndex_Object((1,3,6,1,3,96,1,6,1,8),_MplsOutSegmentXCIndex_Type())
mplsOutSegmentXCIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentXCIndex.setStatus(_B)
class _MplsOutSegmentOwner_Type(MplsObjectOwner):defaultValue=6
_MplsOutSegmentOwner_Type.__name__=_T
_MplsOutSegmentOwner_Object=MibTableColumn
mplsOutSegmentOwner=_MplsOutSegmentOwner_Object((1,3,6,1,3,96,1,6,1,9),_MplsOutSegmentOwner_Type())
mplsOutSegmentOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentOwner.setStatus(_B)
_MplsOutSegmentTrafficParamPtr_Type=RowPointer
_MplsOutSegmentTrafficParamPtr_Object=MibTableColumn
mplsOutSegmentTrafficParamPtr=_MplsOutSegmentTrafficParamPtr_Object((1,3,6,1,3,96,1,6,1,10),_MplsOutSegmentTrafficParamPtr_Type())
mplsOutSegmentTrafficParamPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentTrafficParamPtr.setStatus(_B)
_MplsOutSegmentRowStatus_Type=RowStatus
_MplsOutSegmentRowStatus_Object=MibTableColumn
mplsOutSegmentRowStatus=_MplsOutSegmentRowStatus_Object((1,3,6,1,3,96,1,6,1,11),_MplsOutSegmentRowStatus_Type())
mplsOutSegmentRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentRowStatus.setStatus(_B)
_MplsOutSegmentStorageType_Type=StorageType
_MplsOutSegmentStorageType_Object=MibTableColumn
mplsOutSegmentStorageType=_MplsOutSegmentStorageType_Object((1,3,6,1,3,96,1,6,1,12),_MplsOutSegmentStorageType_Type())
mplsOutSegmentStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentStorageType.setStatus(_B)
class _MplsOutSegmentAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3)))
_MplsOutSegmentAdminStatus_Type.__name__=_E
_MplsOutSegmentAdminStatus_Object=MibTableColumn
mplsOutSegmentAdminStatus=_MplsOutSegmentAdminStatus_Object((1,3,6,1,3,96,1,6,1,13),_MplsOutSegmentAdminStatus_Type())
mplsOutSegmentAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentAdminStatus.setStatus(_B)
class _MplsOutSegmentOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_P,4),(_U,5),(_V,6),(_W,7)))
_MplsOutSegmentOperStatus_Type.__name__=_E
_MplsOutSegmentOperStatus_Object=MibTableColumn
mplsOutSegmentOperStatus=_MplsOutSegmentOperStatus_Object((1,3,6,1,3,96,1,6,1,14),_MplsOutSegmentOperStatus_Type())
mplsOutSegmentOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentOperStatus.setStatus(_B)
_MplsOutSegmentPerfTable_Object=MibTable
mplsOutSegmentPerfTable=_MplsOutSegmentPerfTable_Object((1,3,6,1,3,96,1,7))
if mibBuilder.loadTexts:mplsOutSegmentPerfTable.setStatus(_B)
_MplsOutSegmentPerfEntry_Object=MibTableRow
mplsOutSegmentPerfEntry=_MplsOutSegmentPerfEntry_Object((1,3,6,1,3,96,1,7,1))
if mibBuilder.loadTexts:mplsOutSegmentPerfEntry.setStatus(_B)
_MplsOutSegmentOctets_Type=Counter32
_MplsOutSegmentOctets_Object=MibTableColumn
mplsOutSegmentOctets=_MplsOutSegmentOctets_Object((1,3,6,1,3,96,1,7,1,1),_MplsOutSegmentOctets_Type())
mplsOutSegmentOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentOctets.setStatus(_B)
_MplsOutSegmentPackets_Type=Counter32
_MplsOutSegmentPackets_Object=MibTableColumn
mplsOutSegmentPackets=_MplsOutSegmentPackets_Object((1,3,6,1,3,96,1,7,1,2),_MplsOutSegmentPackets_Type())
mplsOutSegmentPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentPackets.setStatus(_B)
_MplsOutSegmentErrors_Type=Counter32
_MplsOutSegmentErrors_Object=MibTableColumn
mplsOutSegmentErrors=_MplsOutSegmentErrors_Object((1,3,6,1,3,96,1,7,1,3),_MplsOutSegmentErrors_Type())
mplsOutSegmentErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentErrors.setStatus(_B)
_MplsOutSegmentDiscards_Type=Counter32
_MplsOutSegmentDiscards_Object=MibTableColumn
mplsOutSegmentDiscards=_MplsOutSegmentDiscards_Object((1,3,6,1,3,96,1,7,1,4),_MplsOutSegmentDiscards_Type())
mplsOutSegmentDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentDiscards.setStatus(_B)
_MplsOutSegmentHCOctets_Type=Counter64
_MplsOutSegmentHCOctets_Object=MibTableColumn
mplsOutSegmentHCOctets=_MplsOutSegmentHCOctets_Object((1,3,6,1,3,96,1,7,1,5),_MplsOutSegmentHCOctets_Type())
mplsOutSegmentHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentHCOctets.setStatus(_B)
_MplsOutSegmentPerfDiscontinuityTime_Type=TimeStamp
_MplsOutSegmentPerfDiscontinuityTime_Object=MibTableColumn
mplsOutSegmentPerfDiscontinuityTime=_MplsOutSegmentPerfDiscontinuityTime_Object((1,3,6,1,3,96,1,7,1,6),_MplsOutSegmentPerfDiscontinuityTime_Type())
mplsOutSegmentPerfDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentPerfDiscontinuityTime.setStatus(_B)
class _MplsXCIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsXCIndexNext_Type.__name__=_E
_MplsXCIndexNext_Object=MibScalar
mplsXCIndexNext=_MplsXCIndexNext_Object((1,3,6,1,3,96,1,8),_MplsXCIndexNext_Type())
mplsXCIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsXCIndexNext.setStatus(_B)
_MplsXCTable_Object=MibTable
mplsXCTable=_MplsXCTable_Object((1,3,6,1,3,96,1,9))
if mibBuilder.loadTexts:mplsXCTable.setStatus(_B)
_MplsXCEntry_Object=MibTableRow
mplsXCEntry=_MplsXCEntry_Object((1,3,6,1,3,96,1,9,1))
mplsXCEntry.setIndexNames((0,_A,_Q),(0,_A,_G),(0,_A,_H),(0,_A,_I))
if mibBuilder.loadTexts:mplsXCEntry.setStatus(_B)
class _MplsXCIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsXCIndex_Type.__name__=_E
_MplsXCIndex_Object=MibTableColumn
mplsXCIndex=_MplsXCIndex_Object((1,3,6,1,3,96,1,9,1,1),_MplsXCIndex_Type())
mplsXCIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsXCIndex.setStatus(_B)
_MplsXCLspId_Type=MplsLSPID
_MplsXCLspId_Object=MibTableColumn
mplsXCLspId=_MplsXCLspId_Object((1,3,6,1,3,96,1,9,1,2),_MplsXCLspId_Type())
mplsXCLspId.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCLspId.setStatus(_B)
class _MplsXCLabelStackIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsXCLabelStackIndex_Type.__name__=_E
_MplsXCLabelStackIndex_Object=MibTableColumn
mplsXCLabelStackIndex=_MplsXCLabelStackIndex_Object((1,3,6,1,3,96,1,9,1,3),_MplsXCLabelStackIndex_Type())
mplsXCLabelStackIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCLabelStackIndex.setStatus(_B)
class _MplsXCIsPersistent_Type(TruthValue):defaultValue=2
_MplsXCIsPersistent_Type.__name__=_O
_MplsXCIsPersistent_Object=MibTableColumn
mplsXCIsPersistent=_MplsXCIsPersistent_Object((1,3,6,1,3,96,1,9,1,4),_MplsXCIsPersistent_Type())
mplsXCIsPersistent.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCIsPersistent.setStatus(_B)
_MplsXCOwner_Type=MplsObjectOwner
_MplsXCOwner_Object=MibTableColumn
mplsXCOwner=_MplsXCOwner_Object((1,3,6,1,3,96,1,9,1,5),_MplsXCOwner_Type())
mplsXCOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCOwner.setStatus(_B)
_MplsXCRowStatus_Type=RowStatus
_MplsXCRowStatus_Object=MibTableColumn
mplsXCRowStatus=_MplsXCRowStatus_Object((1,3,6,1,3,96,1,9,1,6),_MplsXCRowStatus_Type())
mplsXCRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCRowStatus.setStatus(_B)
_MplsXCStorageType_Type=StorageType
_MplsXCStorageType_Object=MibTableColumn
mplsXCStorageType=_MplsXCStorageType_Object((1,3,6,1,3,96,1,9,1,7),_MplsXCStorageType_Type())
mplsXCStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCStorageType.setStatus(_B)
class _MplsXCAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3)))
_MplsXCAdminStatus_Type.__name__=_E
_MplsXCAdminStatus_Object=MibTableColumn
mplsXCAdminStatus=_MplsXCAdminStatus_Object((1,3,6,1,3,96,1,9,1,8),_MplsXCAdminStatus_Type())
mplsXCAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCAdminStatus.setStatus(_B)
class _MplsXCOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_P,4),(_U,5),(_V,6),(_W,7)))
_MplsXCOperStatus_Type.__name__=_E
_MplsXCOperStatus_Object=MibTableColumn
mplsXCOperStatus=_MplsXCOperStatus_Object((1,3,6,1,3,96,1,9,1,9),_MplsXCOperStatus_Type())
mplsXCOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsXCOperStatus.setStatus(_B)
class _MplsMaxLabelStackDepth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsMaxLabelStackDepth_Type.__name__=_E
_MplsMaxLabelStackDepth_Object=MibScalar
mplsMaxLabelStackDepth=_MplsMaxLabelStackDepth_Object((1,3,6,1,3,96,1,10),_MplsMaxLabelStackDepth_Type())
mplsMaxLabelStackDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsMaxLabelStackDepth.setStatus(_B)
class _MplsLabelStackIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsLabelStackIndexNext_Type.__name__=_E
_MplsLabelStackIndexNext_Object=MibScalar
mplsLabelStackIndexNext=_MplsLabelStackIndexNext_Object((1,3,6,1,3,96,1,11),_MplsLabelStackIndexNext_Type())
mplsLabelStackIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLabelStackIndexNext.setStatus(_B)
_MplsLabelStackTable_Object=MibTable
mplsLabelStackTable=_MplsLabelStackTable_Object((1,3,6,1,3,96,1,12))
if mibBuilder.loadTexts:mplsLabelStackTable.setStatus(_B)
_MplsLabelStackEntry_Object=MibTableRow
mplsLabelStackEntry=_MplsLabelStackEntry_Object((1,3,6,1,3,96,1,12,1))
mplsLabelStackEntry.setIndexNames((0,_A,_g),(0,_A,_h))
if mibBuilder.loadTexts:mplsLabelStackEntry.setStatus(_B)
class _MplsLabelStackIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsLabelStackIndex_Type.__name__=_E
_MplsLabelStackIndex_Object=MibTableColumn
mplsLabelStackIndex=_MplsLabelStackIndex_Object((1,3,6,1,3,96,1,12,1,1),_MplsLabelStackIndex_Type())
mplsLabelStackIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsLabelStackIndex.setStatus(_B)
class _MplsLabelStackLabelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsLabelStackLabelIndex_Type.__name__=_E
_MplsLabelStackLabelIndex_Object=MibTableColumn
mplsLabelStackLabelIndex=_MplsLabelStackLabelIndex_Object((1,3,6,1,3,96,1,12,1,2),_MplsLabelStackLabelIndex_Type())
mplsLabelStackLabelIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsLabelStackLabelIndex.setStatus(_B)
_MplsLabelStackLabel_Type=MplsLabel
_MplsLabelStackLabel_Object=MibTableColumn
mplsLabelStackLabel=_MplsLabelStackLabel_Object((1,3,6,1,3,96,1,12,1,3),_MplsLabelStackLabel_Type())
mplsLabelStackLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLabelStackLabel.setStatus(_B)
_MplsLabelStackRowStatus_Type=RowStatus
_MplsLabelStackRowStatus_Object=MibTableColumn
mplsLabelStackRowStatus=_MplsLabelStackRowStatus_Object((1,3,6,1,3,96,1,12,1,4),_MplsLabelStackRowStatus_Type())
mplsLabelStackRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLabelStackRowStatus.setStatus(_B)
_MplsLabelStackStorageType_Type=StorageType
_MplsLabelStackStorageType_Object=MibTableColumn
mplsLabelStackStorageType=_MplsLabelStackStorageType_Object((1,3,6,1,3,96,1,12,1,5),_MplsLabelStackStorageType_Type())
mplsLabelStackStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLabelStackStorageType.setStatus(_B)
class _MplsTrafficParamIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsTrafficParamIndexNext_Type.__name__=_E
_MplsTrafficParamIndexNext_Object=MibScalar
mplsTrafficParamIndexNext=_MplsTrafficParamIndexNext_Object((1,3,6,1,3,96,1,13),_MplsTrafficParamIndexNext_Type())
mplsTrafficParamIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTrafficParamIndexNext.setStatus(_B)
_MplsTrafficParamTable_Object=MibTable
mplsTrafficParamTable=_MplsTrafficParamTable_Object((1,3,6,1,3,96,1,14))
if mibBuilder.loadTexts:mplsTrafficParamTable.setStatus(_B)
_MplsTrafficParamEntry_Object=MibTableRow
mplsTrafficParamEntry=_MplsTrafficParamEntry_Object((1,3,6,1,3,96,1,14,1))
mplsTrafficParamEntry.setIndexNames((0,_A,_i))
if mibBuilder.loadTexts:mplsTrafficParamEntry.setStatus(_B)
class _MplsTrafficParamIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsTrafficParamIndex_Type.__name__=_E
_MplsTrafficParamIndex_Object=MibTableColumn
mplsTrafficParamIndex=_MplsTrafficParamIndex_Object((1,3,6,1,3,96,1,14,1,1),_MplsTrafficParamIndex_Type())
mplsTrafficParamIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsTrafficParamIndex.setStatus(_B)
_MplsTrafficParamMaxRate_Type=MplsBitRate
_MplsTrafficParamMaxRate_Object=MibTableColumn
mplsTrafficParamMaxRate=_MplsTrafficParamMaxRate_Object((1,3,6,1,3,96,1,14,1,2),_MplsTrafficParamMaxRate_Type())
mplsTrafficParamMaxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTrafficParamMaxRate.setStatus(_B)
if mibBuilder.loadTexts:mplsTrafficParamMaxRate.setUnits(_j)
_MplsTrafficParamMeanRate_Type=MplsBitRate
_MplsTrafficParamMeanRate_Object=MibTableColumn
mplsTrafficParamMeanRate=_MplsTrafficParamMeanRate_Object((1,3,6,1,3,96,1,14,1,3),_MplsTrafficParamMeanRate_Type())
mplsTrafficParamMeanRate.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTrafficParamMeanRate.setStatus(_B)
if mibBuilder.loadTexts:mplsTrafficParamMeanRate.setUnits(_j)
_MplsTrafficParamMaxBurstSize_Type=MplsBurstSize
_MplsTrafficParamMaxBurstSize_Object=MibTableColumn
mplsTrafficParamMaxBurstSize=_MplsTrafficParamMaxBurstSize_Object((1,3,6,1,3,96,1,14,1,4),_MplsTrafficParamMaxBurstSize_Type())
mplsTrafficParamMaxBurstSize.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTrafficParamMaxBurstSize.setStatus(_B)
if mibBuilder.loadTexts:mplsTrafficParamMaxBurstSize.setUnits('bytes')
_MplsTrafficParamRowStatus_Type=RowStatus
_MplsTrafficParamRowStatus_Object=MibTableColumn
mplsTrafficParamRowStatus=_MplsTrafficParamRowStatus_Object((1,3,6,1,3,96,1,14,1,5),_MplsTrafficParamRowStatus_Type())
mplsTrafficParamRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTrafficParamRowStatus.setStatus(_B)
_MplsTrafficParamStorageType_Type=StorageType
_MplsTrafficParamStorageType_Object=MibTableColumn
mplsTrafficParamStorageType=_MplsTrafficParamStorageType_Object((1,3,6,1,3,96,1,14,1,6),_MplsTrafficParamStorageType_Type())
mplsTrafficParamStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTrafficParamStorageType.setStatus(_B)
class _MplsInSegmentTrapEnable_Type(TruthValue):defaultValue=2
_MplsInSegmentTrapEnable_Type.__name__=_O
_MplsInSegmentTrapEnable_Object=MibScalar
mplsInSegmentTrapEnable=_MplsInSegmentTrapEnable_Object((1,3,6,1,3,96,1,15),_MplsInSegmentTrapEnable_Type())
mplsInSegmentTrapEnable.setMaxAccess(_X)
if mibBuilder.loadTexts:mplsInSegmentTrapEnable.setStatus(_B)
class _MplsOutSegmentTrapEnable_Type(TruthValue):defaultValue=2
_MplsOutSegmentTrapEnable_Type.__name__=_O
_MplsOutSegmentTrapEnable_Object=MibScalar
mplsOutSegmentTrapEnable=_MplsOutSegmentTrapEnable_Object((1,3,6,1,3,96,1,16),_MplsOutSegmentTrapEnable_Type())
mplsOutSegmentTrapEnable.setMaxAccess(_X)
if mibBuilder.loadTexts:mplsOutSegmentTrapEnable.setStatus(_B)
class _MplsXCTrapEnable_Type(TruthValue):defaultValue=2
_MplsXCTrapEnable_Type.__name__=_O
_MplsXCTrapEnable_Object=MibScalar
mplsXCTrapEnable=_MplsXCTrapEnable_Object((1,3,6,1,3,96,1,17),_MplsXCTrapEnable_Type())
mplsXCTrapEnable.setMaxAccess(_X)
if mibBuilder.loadTexts:mplsXCTrapEnable.setStatus(_B)
_MplsLsrNotifications_ObjectIdentity=ObjectIdentity
mplsLsrNotifications=_MplsLsrNotifications_ObjectIdentity((1,3,6,1,3,96,2))
_MplsLsrConformance_ObjectIdentity=ObjectIdentity
mplsLsrConformance=_MplsLsrConformance_ObjectIdentity((1,3,6,1,3,96,3))
_MplsLsrGroups_ObjectIdentity=ObjectIdentity
mplsLsrGroups=_MplsLsrGroups_ObjectIdentity((1,3,6,1,3,96,3,1))
_MplsLsrCompliances_ObjectIdentity=ObjectIdentity
mplsLsrCompliances=_MplsLsrCompliances_ObjectIdentity((1,3,6,1,3,96,3,2))
mplsInterfaceConfEntry.registerAugmentions((_A,_k))
mplsInterfacePerfEntry.setIndexNames(*mplsInterfaceConfEntry.getIndexNames())
mplsInSegmentEntry.registerAugmentions((_A,_l))
mplsInSegmentPerfEntry.setIndexNames(*mplsInSegmentEntry.getIndexNames())
mplsOutSegmentEntry.registerAugmentions((_A,_m))
mplsOutSegmentPerfEntry.setIndexNames(*mplsOutSegmentEntry.getIndexNames())
mplsInterfaceGroup=ObjectGroup((1,3,6,1,3,96,3,1,1))
mplsInterfaceGroup.setObjects(*((_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:mplsInterfaceGroup.setStatus(_B)
mplsInSegmentGroup=ObjectGroup((1,3,6,1,3,96,3,1,2))
mplsInSegmentGroup.setObjects(*((_A,_x),(_A,_y),(_A,_z),(_A,_Y),(_A,_Z),(_A,_A0),(_A,_M),(_A,_N),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:mplsInSegmentGroup.setStatus(_B)
mplsOutSegmentGroup=ObjectGroup((1,3,6,1,3,96,3,1,3))
mplsOutSegmentGroup.setObjects(*((_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_a),(_A,_b),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:mplsOutSegmentGroup.setStatus(_B)
mplsXCGroup=ObjectGroup((1,3,6,1,3,96,3,1,4))
mplsXCGroup.setObjects(*((_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_R),(_A,_S),(_A,_AP),(_A,_AQ),(_A,_AR)))
if mibBuilder.loadTexts:mplsXCGroup.setStatus(_B)
mplsPerfGroup=ObjectGroup((1,3,6,1,3,96,3,1,5))
mplsPerfGroup.setObjects(*((_A,_Y),(_A,_AS),(_A,_AT),(_A,_Z),(_A,_a),(_A,_AU),(_A,_b),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac)))
if mibBuilder.loadTexts:mplsPerfGroup.setStatus(_B)
mplsHCInSegmentPerfGroup=ObjectGroup((1,3,6,1,3,96,3,1,6))
mplsHCInSegmentPerfGroup.setObjects((_A,_Ad))
if mibBuilder.loadTexts:mplsHCInSegmentPerfGroup.setStatus(_B)
mplsHCOutSegmentPerfGroup=ObjectGroup((1,3,6,1,3,96,3,1,7))
mplsHCOutSegmentPerfGroup.setObjects((_A,_Ae))
if mibBuilder.loadTexts:mplsHCOutSegmentPerfGroup.setStatus(_B)
mplsTrafficParamGroup=ObjectGroup((1,3,6,1,3,96,3,1,8))
mplsTrafficParamGroup.setObjects(*((_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak)))
if mibBuilder.loadTexts:mplsTrafficParamGroup.setStatus(_B)
mplsXCIsPersistentGroup=ObjectGroup((1,3,6,1,3,96,3,1,9))
mplsXCIsPersistentGroup.setObjects((_A,_c))
if mibBuilder.loadTexts:mplsXCIsPersistentGroup.setStatus(_B)
mplsXCIsNotPersistentGroup=ObjectGroup((1,3,6,1,3,96,3,1,10))
mplsXCIsNotPersistentGroup.setObjects((_A,_c))
if mibBuilder.loadTexts:mplsXCIsNotPersistentGroup.setStatus(_B)
mplsLabelStackGroup=ObjectGroup((1,3,6,1,3,96,3,1,11))
mplsLabelStackGroup.setObjects(*((_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap)))
if mibBuilder.loadTexts:mplsLabelStackGroup.setStatus(_B)
mplsSegmentDiscontinuityGroup=ObjectGroup((1,3,6,1,3,96,3,1,12))
mplsSegmentDiscontinuityGroup.setObjects(*((_A,_Aq),(_A,_Ar)))
if mibBuilder.loadTexts:mplsSegmentDiscontinuityGroup.setStatus(_B)
mplsInSegmentUp=NotificationType((1,3,6,1,3,96,2,1))
mplsInSegmentUp.setObjects(*((_A,_G),(_A,_H),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:mplsInSegmentUp.setStatus(_B)
mplsInSegmentDown=NotificationType((1,3,6,1,3,96,2,2))
mplsInSegmentDown.setObjects(*((_A,_G),(_A,_H),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:mplsInSegmentDown.setStatus(_B)
mplsOutSegmentUp=NotificationType((1,3,6,1,3,96,2,3))
mplsOutSegmentUp.setObjects(*((_A,_I),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:mplsOutSegmentUp.setStatus(_B)
mplsOutSegmentDown=NotificationType((1,3,6,1,3,96,2,4))
mplsOutSegmentDown.setObjects(*((_A,_I),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:mplsOutSegmentDown.setStatus(_B)
mplsXCUp=NotificationType((1,3,6,1,3,96,2,5))
mplsXCUp.setObjects(*((_A,_Q),(_A,_G),(_A,_H),(_A,_I),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:mplsXCUp.setStatus(_B)
mplsXCDown=NotificationType((1,3,6,1,3,96,2,6))
mplsXCDown.setObjects(*((_A,_Q),(_A,_G),(_A,_H),(_A,_I),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:mplsXCDown.setStatus(_B)
mplsLsrNotificationGroup=NotificationGroup((1,3,6,1,3,96,3,1,13))
mplsLsrNotificationGroup.setObjects(*((_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,'mplsXCUp'),(_A,_Aw)))
if mibBuilder.loadTexts:mplsLsrNotificationGroup.setStatus(_B)
mplsLsrModuleCompliance=ModuleCompliance((1,3,6,1,3,96,3,2,1))
mplsLsrModuleCompliance.setObjects(*((_A,_Ax),(_A,_Ay),(_A,_Az),(_A,_A_),(_A,_B0),(_A,_B1),(_A,_B2),(_A,_B3),(_A,_B4),(_A,_B5),(_A,_B6)))
if mibBuilder.loadTexts:mplsLsrModuleCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'MplsLSPID':MplsLSPID,'MplsLabel':MplsLabel,'MplsBitRate':MplsBitRate,'MplsBurstSize':MplsBurstSize,'MplsBufferSize':MplsBufferSize,_T:MplsObjectOwner,'mplsLsrMIB':mplsLsrMIB,'mplsLsrObjects':mplsLsrObjects,'mplsInterfaceConfTable':mplsInterfaceConfTable,'mplsInterfaceConfEntry':mplsInterfaceConfEntry,_f:mplsInterfaceConfIndex,_n:mplsInterfaceLabelMinIn,_o:mplsInterfaceLabelMaxIn,_p:mplsInterfaceLabelMinOut,_q:mplsInterfaceLabelMaxOut,_r:mplsInterfaceTotalBandwidth,_s:mplsInterfaceAvailableBandwidth,_t:mplsInterfaceTotalBuffer,_u:mplsInterfaceAvailableBuffer,_v:mplsInterfaceLabelParticipationType,_w:mplsInterfaceConfStorageType,'mplsInterfacePerfTable':mplsInterfacePerfTable,_k:mplsInterfacePerfEntry,_AV:mplsInterfaceInLabelsUsed,_AW:mplsInterfaceInPackets,_AX:mplsInterfaceInDiscards,_AY:mplsInterfaceFailedLabelLookup,_Ac:mplsInterfaceOutLabelsUsed,_AZ:mplsInterfaceOutPackets,_Aa:mplsInterfaceOutDiscards,_Ab:mplsInterfaceOutFragments,'mplsInSegmentTable':mplsInSegmentTable,'mplsInSegmentEntry':mplsInSegmentEntry,_G:mplsInSegmentIfIndex,_H:mplsInSegmentLabel,_x:mplsInSegmentNPop,_y:mplsInSegmentAddrFamily,_z:mplsInSegmentXCIndex,_A0:mplsInSegmentOwner,_A4:mplsInSegmentTrafficParamPtr,_A1:mplsInSegmentRowStatus,_A3:mplsInSegmentStorageType,_M:mplsInSegmentAdminStatus,_N:mplsInSegmentOperStatus,'mplsInSegmentPerfTable':mplsInSegmentPerfTable,_l:mplsInSegmentPerfEntry,_Y:mplsInSegmentOctets,_AS:mplsInSegmentPackets,_AT:mplsInSegmentErrors,_Z:mplsInSegmentDiscards,_Ad:mplsInSegmentHCOctets,_Aq:mplsInSegmentPerfDiscontinuityTime,_A5:mplsOutSegmentIndexNext,'mplsOutSegmentTable':mplsOutSegmentTable,'mplsOutSegmentEntry':mplsOutSegmentEntry,_I:mplsOutSegmentIndex,_A6:mplsOutSegmentIfIndex,_A7:mplsOutSegmentPushTopLabel,_A8:mplsOutSegmentTopLabel,_A9:mplsOutSegmentNextHopIpAddrType,_AA:mplsOutSegmentNextHopIpv4Addr,_AB:mplsOutSegmentNextHopIpv6Addr,_AC:mplsOutSegmentXCIndex,_AD:mplsOutSegmentOwner,_AK:mplsOutSegmentTrafficParamPtr,_AH:mplsOutSegmentRowStatus,_AJ:mplsOutSegmentStorageType,_AF:mplsOutSegmentAdminStatus,_AG:mplsOutSegmentOperStatus,'mplsOutSegmentPerfTable':mplsOutSegmentPerfTable,_m:mplsOutSegmentPerfEntry,_a:mplsOutSegmentOctets,_AU:mplsOutSegmentPackets,_AE:mplsOutSegmentErrors,_b:mplsOutSegmentDiscards,_Ae:mplsOutSegmentHCOctets,_Ar:mplsOutSegmentPerfDiscontinuityTime,_AL:mplsXCIndexNext,'mplsXCTable':mplsXCTable,'mplsXCEntry':mplsXCEntry,_Q:mplsXCIndex,_AM:mplsXCLspId,_AN:mplsXCLabelStackIndex,_c:mplsXCIsPersistent,_AO:mplsXCOwner,_AP:mplsXCRowStatus,_AR:mplsXCStorageType,_R:mplsXCAdminStatus,_S:mplsXCOperStatus,_Ao:mplsMaxLabelStackDepth,_Ap:mplsLabelStackIndexNext,'mplsLabelStackTable':mplsLabelStackTable,'mplsLabelStackEntry':mplsLabelStackEntry,_g:mplsLabelStackIndex,_h:mplsLabelStackLabelIndex,_Al:mplsLabelStackLabel,_Am:mplsLabelStackRowStatus,_An:mplsLabelStackStorageType,_Af:mplsTrafficParamIndexNext,'mplsTrafficParamTable':mplsTrafficParamTable,'mplsTrafficParamEntry':mplsTrafficParamEntry,_i:mplsTrafficParamIndex,_Ag:mplsTrafficParamMaxRate,_Ah:mplsTrafficParamMeanRate,_Ai:mplsTrafficParamMaxBurstSize,_Aj:mplsTrafficParamRowStatus,_Ak:mplsTrafficParamStorageType,_A2:mplsInSegmentTrapEnable,_AI:mplsOutSegmentTrapEnable,_AQ:mplsXCTrapEnable,'mplsLsrNotifications':mplsLsrNotifications,_As:mplsInSegmentUp,_At:mplsInSegmentDown,_Au:mplsOutSegmentUp,_Av:mplsOutSegmentDown,'mplsXCUp':mplsXCUp,_Aw:mplsXCDown,'mplsLsrConformance':mplsLsrConformance,'mplsLsrGroups':mplsLsrGroups,_A_:mplsInterfaceGroup,_Ax:mplsInSegmentGroup,_Ay:mplsOutSegmentGroup,_Az:mplsXCGroup,_B0:mplsPerfGroup,_B2:mplsHCInSegmentPerfGroup,_B3:mplsHCOutSegmentPerfGroup,_B4:mplsTrafficParamGroup,_B5:mplsXCIsPersistentGroup,_B6:mplsXCIsNotPersistentGroup,'mplsLabelStackGroup':mplsLabelStackGroup,_B1:mplsSegmentDiscontinuityGroup,'mplsLsrNotificationGroup':mplsLsrNotificationGroup,'mplsLsrCompliances':mplsLsrCompliances,'mplsLsrModuleCompliance':mplsLsrModuleCompliance})