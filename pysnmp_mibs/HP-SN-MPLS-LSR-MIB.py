_Am='mplsXCIsNotPersistentGroup'
_Al='mplsXCIsPersistentGroup'
_Ak='mplsTrafficParamGroup'
_Aj='mplsHCOutSegmentPerfGroup'
_Ai='mplsHCInSegmentPerfGroup'
_Ah='mplsSegmentDiscontinuityGroup'
_Ag='mplsPerfGroup'
_Af='mplsInterfaceGroup'
_Ae='mplsXCGroup'
_Ad='mplsOutSegmentGroup'
_Ac='mplsInSegmentGroup'
_Ab='mplsXCDown'
_Aa='mplsOutSegmentPerfDiscontinuityTime'
_AZ='mplsInSegmentPerfDiscontinuityTime'
_AY='mplsLabelStackIndexNext'
_AX='mplsMaxLabelStackDepth'
_AW='mplsLabelStackStorageType'
_AV='mplsLabelStackRowStatus'
_AU='mplsLabelStackLabel'
_AT='mplsTrafficParamStorageType'
_AS='mplsTrafficParamRowStatus'
_AR='mplsTrafficParamMaxBurstSize'
_AQ='mplsTrafficParamMeanRate'
_AP='mplsTrafficParamMaxRate'
_AO='mplsTrafficParamIndexNext'
_AN='mplsOutSegmentHCOctets'
_AM='mplsInSegmentHCOctets'
_AL='mplsInterfaceOutLabelsUsed'
_AK='mplsInterfaceOutFragments'
_AJ='mplsInterfaceFailedLabelLookup'
_AI='mplsInterfaceInLabelsUsed'
_AH='mplsOutSegmentPackets'
_AG='mplsInSegmentErrors'
_AF='mplsInSegmentPackets'
_AE='mplsXCLspId'
_AD='mplsXCStorageType'
_AC='mplsXCTrapEnable'
_AB='mplsXCRowStatus'
_AA='mplsXCAdminStatus'
_A9='mplsXCOwner'
_A8='mplsXCLabelStackIndex'
_A7='mplsXCIndexNext'
_A6='mplsOutSegmentTrafficParamPtr'
_A5='mplsOutSegmentStorageType'
_A4='mplsOutSegmentRowStatus'
_A3='mplsOutSegmentErrors'
_A2='mplsOutSegmentOwner'
_A1='mplsOutSegmentXCIndex'
_A0='mplsOutSegmentNextHopIpv6Addr'
_z='mplsOutSegmentNextHopIpv4Addr'
_y='mplsOutSegmentNextHopIpAddrType'
_x='mplsOutSegmentTopLabel'
_w='mplsOutSegmentPushTopLabel'
_v='mplsOutSegmentIfIndex'
_u='mplsOutSegmentIndexNext'
_t='mplsInSegmentTrafficParamPtr'
_s='mplsInSegmentStorageType'
_r='mplsInSegmentRowStatus'
_q='mplsInSegmentOwner'
_p='mplsInSegmentXCIndex'
_o='mplsInSegmentAddrFamily'
_n='mplsInSegmentNPop'
_m='mplsInterfaceLabelParticipationType'
_l='mplsInterfaceAvailableBandwidth'
_k='mplsInterfaceTotalBandwidth'
_j='mplsInterfaceLabelMaxOut'
_i='mplsInterfaceLabelMinOut'
_h='mplsInterfaceLabelMaxIn'
_g='mplsInterfaceLabelMinIn'
_f='mplsOutSegmentPerfEntry'
_e='mplsInSegmentPerfEntry'
_d='mplsInterfacePerfEntry'
_c='kilobits per second'
_b='mplsTrafficParamIndex'
_a='mplsLabelStackLabelIndex'
_Z='mplsLabelStackIndex'
_Y='testing'
_X='mplsXCIndex'
_W='mplsInterfaceConfIndex'
_V='InetAddressType'
_U='InterfaceIndexOrZero'
_T='AddressFamilyNumbers'
_S='MplsLabel'
_R='mplsXCIsPersistent'
_Q='mplsOutSegmentDiscards'
_P='mplsOutSegmentOctets'
_O='mplsInSegmentDiscards'
_N='mplsInSegmentOctets'
_M='mplsOutSegmentIndex'
_L='mplsInSegmentLabel'
_K='mplsInSegmentIfIndex'
_J='TruthValue'
_I='MplsInitialCreationSource'
_H='Integer32'
_G='mplsXCOperStatus'
_F='not-accessible'
_E='Unsigned32'
_D='read-create'
_C='read-only'
_B='HP-SN-MPLS-LSR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
MplsBitRate,MplsBurstSize,MplsInitialCreationSource,MplsLSPID,MplsLabel,mplsMIB=mibBuilder.importSymbols('HP-SN-MPLS-TC-MIB','MplsBitRate','MplsBurstSize',_I,'MplsLSPID',_S,'mplsMIB')
snMpls,=mibBuilder.importSymbols('HP-SN-ROOT-MIB','snMpls')
AddressFamilyNumbers,=mibBuilder.importSymbols('IANA-ADDRESS-FAMILY-NUMBERS-MIB',_T)
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex',_U)
InetAddressIPv4,InetAddressIPv6,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6',_V)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowPointer,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','RowStatus','StorageType','TextualConvention','TimeStamp',_J)
mplsLsrMIB=ModuleIdentity((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2))
if mibBuilder.loadTexts:mplsLsrMIB.setRevisions(('2002-01-04 12:00',))
_MplsLsrObjects_ObjectIdentity=ObjectIdentity
mplsLsrObjects=_MplsLsrObjects_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1))
_MplsInterfaceConfTable_Object=MibTable
mplsInterfaceConfTable=_MplsInterfaceConfTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,1))
if mibBuilder.loadTexts:mplsInterfaceConfTable.setStatus(_A)
_MplsInterfaceConfEntry_Object=MibTableRow
mplsInterfaceConfEntry=_MplsInterfaceConfEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,1,1))
mplsInterfaceConfEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:mplsInterfaceConfEntry.setStatus(_A)
_MplsInterfaceConfIndex_Type=InterfaceIndexOrZero
_MplsInterfaceConfIndex_Object=MibTableColumn
mplsInterfaceConfIndex=_MplsInterfaceConfIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,1,1,1),_MplsInterfaceConfIndex_Type())
mplsInterfaceConfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsInterfaceConfIndex.setStatus(_A)
_MplsInterfaceLabelMinIn_Type=MplsLabel
_MplsInterfaceLabelMinIn_Object=MibTableColumn
mplsInterfaceLabelMinIn=_MplsInterfaceLabelMinIn_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,1,1,2),_MplsInterfaceLabelMinIn_Type())
mplsInterfaceLabelMinIn.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceLabelMinIn.setStatus(_A)
_MplsInterfaceLabelMaxIn_Type=MplsLabel
_MplsInterfaceLabelMaxIn_Object=MibTableColumn
mplsInterfaceLabelMaxIn=_MplsInterfaceLabelMaxIn_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,1,1,3),_MplsInterfaceLabelMaxIn_Type())
mplsInterfaceLabelMaxIn.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceLabelMaxIn.setStatus(_A)
_MplsInterfaceLabelMinOut_Type=MplsLabel
_MplsInterfaceLabelMinOut_Object=MibTableColumn
mplsInterfaceLabelMinOut=_MplsInterfaceLabelMinOut_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,1,1,4),_MplsInterfaceLabelMinOut_Type())
mplsInterfaceLabelMinOut.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceLabelMinOut.setStatus(_A)
_MplsInterfaceLabelMaxOut_Type=MplsLabel
_MplsInterfaceLabelMaxOut_Object=MibTableColumn
mplsInterfaceLabelMaxOut=_MplsInterfaceLabelMaxOut_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,1,1,5),_MplsInterfaceLabelMaxOut_Type())
mplsInterfaceLabelMaxOut.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceLabelMaxOut.setStatus(_A)
_MplsInterfaceTotalBandwidth_Type=MplsBitRate
_MplsInterfaceTotalBandwidth_Object=MibTableColumn
mplsInterfaceTotalBandwidth=_MplsInterfaceTotalBandwidth_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,1,1,6),_MplsInterfaceTotalBandwidth_Type())
mplsInterfaceTotalBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceTotalBandwidth.setStatus(_A)
_MplsInterfaceAvailableBandwidth_Type=MplsBitRate
_MplsInterfaceAvailableBandwidth_Object=MibTableColumn
mplsInterfaceAvailableBandwidth=_MplsInterfaceAvailableBandwidth_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,1,1,7),_MplsInterfaceAvailableBandwidth_Type())
mplsInterfaceAvailableBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceAvailableBandwidth.setStatus(_A)
class _MplsInterfaceLabelParticipationType_Type(Bits):namedValues=NamedValues(*(('perPlatform',0),('perInterface',1)))
_MplsInterfaceLabelParticipationType_Type.__name__='Bits'
_MplsInterfaceLabelParticipationType_Object=MibTableColumn
mplsInterfaceLabelParticipationType=_MplsInterfaceLabelParticipationType_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,1,1,8),_MplsInterfaceLabelParticipationType_Type())
mplsInterfaceLabelParticipationType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceLabelParticipationType.setStatus(_A)
_MplsInterfacePerfTable_Object=MibTable
mplsInterfacePerfTable=_MplsInterfacePerfTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,2))
if mibBuilder.loadTexts:mplsInterfacePerfTable.setStatus(_A)
_MplsInterfacePerfEntry_Object=MibTableRow
mplsInterfacePerfEntry=_MplsInterfacePerfEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,2,1))
if mibBuilder.loadTexts:mplsInterfacePerfEntry.setStatus(_A)
_MplsInterfaceInLabelsUsed_Type=Gauge32
_MplsInterfaceInLabelsUsed_Object=MibTableColumn
mplsInterfaceInLabelsUsed=_MplsInterfaceInLabelsUsed_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,2,1,1),_MplsInterfaceInLabelsUsed_Type())
mplsInterfaceInLabelsUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceInLabelsUsed.setStatus(_A)
_MplsInterfaceFailedLabelLookup_Type=Counter32
_MplsInterfaceFailedLabelLookup_Object=MibTableColumn
mplsInterfaceFailedLabelLookup=_MplsInterfaceFailedLabelLookup_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,2,1,2),_MplsInterfaceFailedLabelLookup_Type())
mplsInterfaceFailedLabelLookup.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceFailedLabelLookup.setStatus(_A)
_MplsInterfaceOutLabelsUsed_Type=Gauge32
_MplsInterfaceOutLabelsUsed_Object=MibTableColumn
mplsInterfaceOutLabelsUsed=_MplsInterfaceOutLabelsUsed_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,2,1,3),_MplsInterfaceOutLabelsUsed_Type())
mplsInterfaceOutLabelsUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceOutLabelsUsed.setStatus(_A)
_MplsInterfaceOutFragments_Type=Counter32
_MplsInterfaceOutFragments_Object=MibTableColumn
mplsInterfaceOutFragments=_MplsInterfaceOutFragments_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,2,1,4),_MplsInterfaceOutFragments_Type())
mplsInterfaceOutFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceOutFragments.setStatus(_A)
_MplsInSegmentTable_Object=MibTable
mplsInSegmentTable=_MplsInSegmentTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,3))
if mibBuilder.loadTexts:mplsInSegmentTable.setStatus(_A)
_MplsInSegmentEntry_Object=MibTableRow
mplsInSegmentEntry=_MplsInSegmentEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,3,1))
mplsInSegmentEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:mplsInSegmentEntry.setStatus(_A)
_MplsInSegmentIfIndex_Type=InterfaceIndexOrZero
_MplsInSegmentIfIndex_Object=MibTableColumn
mplsInSegmentIfIndex=_MplsInSegmentIfIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,3,1,1),_MplsInSegmentIfIndex_Type())
mplsInSegmentIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsInSegmentIfIndex.setStatus(_A)
_MplsInSegmentLabel_Type=MplsLabel
_MplsInSegmentLabel_Object=MibTableColumn
mplsInSegmentLabel=_MplsInSegmentLabel_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,3,1,2),_MplsInSegmentLabel_Type())
mplsInSegmentLabel.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsInSegmentLabel.setStatus(_A)
class _MplsInSegmentNPop_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsInSegmentNPop_Type.__name__=_H
_MplsInSegmentNPop_Object=MibTableColumn
mplsInSegmentNPop=_MplsInSegmentNPop_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,3,1,3),_MplsInSegmentNPop_Type())
mplsInSegmentNPop.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentNPop.setStatus(_A)
class _MplsInSegmentAddrFamily_Type(AddressFamilyNumbers):defaultValue=0
_MplsInSegmentAddrFamily_Type.__name__=_T
_MplsInSegmentAddrFamily_Object=MibTableColumn
mplsInSegmentAddrFamily=_MplsInSegmentAddrFamily_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,3,1,4),_MplsInSegmentAddrFamily_Type())
mplsInSegmentAddrFamily.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentAddrFamily.setStatus(_A)
class _MplsInSegmentXCIndex_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MplsInSegmentXCIndex_Type.__name__=_E
_MplsInSegmentXCIndex_Object=MibTableColumn
mplsInSegmentXCIndex=_MplsInSegmentXCIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,3,1,5),_MplsInSegmentXCIndex_Type())
mplsInSegmentXCIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentXCIndex.setStatus(_A)
class _MplsInSegmentOwner_Type(MplsInitialCreationSource):defaultValue=7
_MplsInSegmentOwner_Type.__name__=_I
_MplsInSegmentOwner_Object=MibTableColumn
mplsInSegmentOwner=_MplsInSegmentOwner_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,3,1,6),_MplsInSegmentOwner_Type())
mplsInSegmentOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentOwner.setStatus(_A)
_MplsInSegmentTrafficParamPtr_Type=RowPointer
_MplsInSegmentTrafficParamPtr_Object=MibTableColumn
mplsInSegmentTrafficParamPtr=_MplsInSegmentTrafficParamPtr_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,3,1,7),_MplsInSegmentTrafficParamPtr_Type())
mplsInSegmentTrafficParamPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentTrafficParamPtr.setStatus(_A)
_MplsInSegmentRowStatus_Type=RowStatus
_MplsInSegmentRowStatus_Object=MibTableColumn
mplsInSegmentRowStatus=_MplsInSegmentRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,3,1,8),_MplsInSegmentRowStatus_Type())
mplsInSegmentRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentRowStatus.setStatus(_A)
_MplsInSegmentStorageType_Type=StorageType
_MplsInSegmentStorageType_Object=MibTableColumn
mplsInSegmentStorageType=_MplsInSegmentStorageType_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,3,1,9),_MplsInSegmentStorageType_Type())
mplsInSegmentStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentStorageType.setStatus(_A)
_MplsInSegmentPerfTable_Object=MibTable
mplsInSegmentPerfTable=_MplsInSegmentPerfTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,4))
if mibBuilder.loadTexts:mplsInSegmentPerfTable.setStatus(_A)
_MplsInSegmentPerfEntry_Object=MibTableRow
mplsInSegmentPerfEntry=_MplsInSegmentPerfEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,4,1))
if mibBuilder.loadTexts:mplsInSegmentPerfEntry.setStatus(_A)
_MplsInSegmentOctets_Type=Counter32
_MplsInSegmentOctets_Object=MibTableColumn
mplsInSegmentOctets=_MplsInSegmentOctets_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,4,1,1),_MplsInSegmentOctets_Type())
mplsInSegmentOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentOctets.setStatus(_A)
_MplsInSegmentPackets_Type=Counter32
_MplsInSegmentPackets_Object=MibTableColumn
mplsInSegmentPackets=_MplsInSegmentPackets_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,4,1,2),_MplsInSegmentPackets_Type())
mplsInSegmentPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentPackets.setStatus(_A)
_MplsInSegmentErrors_Type=Counter32
_MplsInSegmentErrors_Object=MibTableColumn
mplsInSegmentErrors=_MplsInSegmentErrors_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,4,1,3),_MplsInSegmentErrors_Type())
mplsInSegmentErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentErrors.setStatus(_A)
_MplsInSegmentDiscards_Type=Counter32
_MplsInSegmentDiscards_Object=MibTableColumn
mplsInSegmentDiscards=_MplsInSegmentDiscards_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,4,1,4),_MplsInSegmentDiscards_Type())
mplsInSegmentDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentDiscards.setStatus(_A)
_MplsInSegmentHCOctets_Type=Counter64
_MplsInSegmentHCOctets_Object=MibTableColumn
mplsInSegmentHCOctets=_MplsInSegmentHCOctets_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,4,1,5),_MplsInSegmentHCOctets_Type())
mplsInSegmentHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentHCOctets.setStatus(_A)
_MplsInSegmentPerfDiscontinuityTime_Type=TimeStamp
_MplsInSegmentPerfDiscontinuityTime_Object=MibTableColumn
mplsInSegmentPerfDiscontinuityTime=_MplsInSegmentPerfDiscontinuityTime_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,4,1,6),_MplsInSegmentPerfDiscontinuityTime_Type())
mplsInSegmentPerfDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentPerfDiscontinuityTime.setStatus(_A)
class _MplsOutSegmentIndexNext_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MplsOutSegmentIndexNext_Type.__name__=_E
_MplsOutSegmentIndexNext_Object=MibScalar
mplsOutSegmentIndexNext=_MplsOutSegmentIndexNext_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,5),_MplsOutSegmentIndexNext_Type())
mplsOutSegmentIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentIndexNext.setStatus(_A)
_MplsOutSegmentTable_Object=MibTable
mplsOutSegmentTable=_MplsOutSegmentTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,6))
if mibBuilder.loadTexts:mplsOutSegmentTable.setStatus(_A)
_MplsOutSegmentEntry_Object=MibTableRow
mplsOutSegmentEntry=_MplsOutSegmentEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,6,1))
mplsOutSegmentEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:mplsOutSegmentEntry.setStatus(_A)
class _MplsOutSegmentIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsOutSegmentIndex_Type.__name__=_E
_MplsOutSegmentIndex_Object=MibTableColumn
mplsOutSegmentIndex=_MplsOutSegmentIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,6,1,1),_MplsOutSegmentIndex_Type())
mplsOutSegmentIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsOutSegmentIndex.setStatus(_A)
class _MplsOutSegmentIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_MplsOutSegmentIfIndex_Type.__name__=_U
_MplsOutSegmentIfIndex_Object=MibTableColumn
mplsOutSegmentIfIndex=_MplsOutSegmentIfIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,6,1,2),_MplsOutSegmentIfIndex_Type())
mplsOutSegmentIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentIfIndex.setStatus(_A)
_MplsOutSegmentPushTopLabel_Type=TruthValue
_MplsOutSegmentPushTopLabel_Object=MibTableColumn
mplsOutSegmentPushTopLabel=_MplsOutSegmentPushTopLabel_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,6,1,3),_MplsOutSegmentPushTopLabel_Type())
mplsOutSegmentPushTopLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentPushTopLabel.setStatus(_A)
class _MplsOutSegmentTopLabel_Type(MplsLabel):defaultValue=0
_MplsOutSegmentTopLabel_Type.__name__=_S
_MplsOutSegmentTopLabel_Object=MibTableColumn
mplsOutSegmentTopLabel=_MplsOutSegmentTopLabel_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,6,1,4),_MplsOutSegmentTopLabel_Type())
mplsOutSegmentTopLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentTopLabel.setStatus(_A)
class _MplsOutSegmentNextHopIpAddrType_Type(InetAddressType):defaultValue=0
_MplsOutSegmentNextHopIpAddrType_Type.__name__=_V
_MplsOutSegmentNextHopIpAddrType_Object=MibTableColumn
mplsOutSegmentNextHopIpAddrType=_MplsOutSegmentNextHopIpAddrType_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,6,1,5),_MplsOutSegmentNextHopIpAddrType_Type())
mplsOutSegmentNextHopIpAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentNextHopIpAddrType.setStatus(_A)
_MplsOutSegmentNextHopIpv4Addr_Type=InetAddressIPv4
_MplsOutSegmentNextHopIpv4Addr_Object=MibTableColumn
mplsOutSegmentNextHopIpv4Addr=_MplsOutSegmentNextHopIpv4Addr_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,6,1,6),_MplsOutSegmentNextHopIpv4Addr_Type())
mplsOutSegmentNextHopIpv4Addr.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentNextHopIpv4Addr.setStatus(_A)
_MplsOutSegmentNextHopIpv6Addr_Type=InetAddressIPv6
_MplsOutSegmentNextHopIpv6Addr_Object=MibTableColumn
mplsOutSegmentNextHopIpv6Addr=_MplsOutSegmentNextHopIpv6Addr_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,6,1,7),_MplsOutSegmentNextHopIpv6Addr_Type())
mplsOutSegmentNextHopIpv6Addr.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentNextHopIpv6Addr.setStatus(_A)
class _MplsOutSegmentXCIndex_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MplsOutSegmentXCIndex_Type.__name__=_E
_MplsOutSegmentXCIndex_Object=MibTableColumn
mplsOutSegmentXCIndex=_MplsOutSegmentXCIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,6,1,8),_MplsOutSegmentXCIndex_Type())
mplsOutSegmentXCIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentXCIndex.setStatus(_A)
class _MplsOutSegmentOwner_Type(MplsInitialCreationSource):defaultValue=7
_MplsOutSegmentOwner_Type.__name__=_I
_MplsOutSegmentOwner_Object=MibTableColumn
mplsOutSegmentOwner=_MplsOutSegmentOwner_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,6,1,9),_MplsOutSegmentOwner_Type())
mplsOutSegmentOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentOwner.setStatus(_A)
_MplsOutSegmentTrafficParamPtr_Type=RowPointer
_MplsOutSegmentTrafficParamPtr_Object=MibTableColumn
mplsOutSegmentTrafficParamPtr=_MplsOutSegmentTrafficParamPtr_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,6,1,10),_MplsOutSegmentTrafficParamPtr_Type())
mplsOutSegmentTrafficParamPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentTrafficParamPtr.setStatus(_A)
_MplsOutSegmentRowStatus_Type=RowStatus
_MplsOutSegmentRowStatus_Object=MibTableColumn
mplsOutSegmentRowStatus=_MplsOutSegmentRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,6,1,11),_MplsOutSegmentRowStatus_Type())
mplsOutSegmentRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentRowStatus.setStatus(_A)
_MplsOutSegmentStorageType_Type=StorageType
_MplsOutSegmentStorageType_Object=MibTableColumn
mplsOutSegmentStorageType=_MplsOutSegmentStorageType_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,6,1,12),_MplsOutSegmentStorageType_Type())
mplsOutSegmentStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentStorageType.setStatus(_A)
_MplsOutSegmentPerfTable_Object=MibTable
mplsOutSegmentPerfTable=_MplsOutSegmentPerfTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,7))
if mibBuilder.loadTexts:mplsOutSegmentPerfTable.setStatus(_A)
_MplsOutSegmentPerfEntry_Object=MibTableRow
mplsOutSegmentPerfEntry=_MplsOutSegmentPerfEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,7,1))
if mibBuilder.loadTexts:mplsOutSegmentPerfEntry.setStatus(_A)
_MplsOutSegmentOctets_Type=Counter32
_MplsOutSegmentOctets_Object=MibTableColumn
mplsOutSegmentOctets=_MplsOutSegmentOctets_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,7,1,1),_MplsOutSegmentOctets_Type())
mplsOutSegmentOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentOctets.setStatus(_A)
_MplsOutSegmentPackets_Type=Counter32
_MplsOutSegmentPackets_Object=MibTableColumn
mplsOutSegmentPackets=_MplsOutSegmentPackets_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,7,1,2),_MplsOutSegmentPackets_Type())
mplsOutSegmentPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentPackets.setStatus(_A)
_MplsOutSegmentErrors_Type=Counter32
_MplsOutSegmentErrors_Object=MibTableColumn
mplsOutSegmentErrors=_MplsOutSegmentErrors_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,7,1,3),_MplsOutSegmentErrors_Type())
mplsOutSegmentErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentErrors.setStatus(_A)
_MplsOutSegmentDiscards_Type=Counter32
_MplsOutSegmentDiscards_Object=MibTableColumn
mplsOutSegmentDiscards=_MplsOutSegmentDiscards_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,7,1,4),_MplsOutSegmentDiscards_Type())
mplsOutSegmentDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentDiscards.setStatus(_A)
_MplsOutSegmentHCOctets_Type=Counter64
_MplsOutSegmentHCOctets_Object=MibTableColumn
mplsOutSegmentHCOctets=_MplsOutSegmentHCOctets_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,7,1,5),_MplsOutSegmentHCOctets_Type())
mplsOutSegmentHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentHCOctets.setStatus(_A)
_MplsOutSegmentPerfDiscontinuityTime_Type=TimeStamp
_MplsOutSegmentPerfDiscontinuityTime_Object=MibTableColumn
mplsOutSegmentPerfDiscontinuityTime=_MplsOutSegmentPerfDiscontinuityTime_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,7,1,6),_MplsOutSegmentPerfDiscontinuityTime_Type())
mplsOutSegmentPerfDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentPerfDiscontinuityTime.setStatus(_A)
class _MplsXCIndexNext_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MplsXCIndexNext_Type.__name__=_E
_MplsXCIndexNext_Object=MibScalar
mplsXCIndexNext=_MplsXCIndexNext_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,8),_MplsXCIndexNext_Type())
mplsXCIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsXCIndexNext.setStatus(_A)
_MplsXCTable_Object=MibTable
mplsXCTable=_MplsXCTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,9))
if mibBuilder.loadTexts:mplsXCTable.setStatus(_A)
_MplsXCEntry_Object=MibTableRow
mplsXCEntry=_MplsXCEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,9,1))
mplsXCEntry.setIndexNames((0,_B,_X),(0,_B,_K),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:mplsXCEntry.setStatus(_A)
class _MplsXCIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsXCIndex_Type.__name__=_E
_MplsXCIndex_Object=MibTableColumn
mplsXCIndex=_MplsXCIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,9,1,1),_MplsXCIndex_Type())
mplsXCIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsXCIndex.setStatus(_A)
_MplsXCLspId_Type=MplsLSPID
_MplsXCLspId_Object=MibTableColumn
mplsXCLspId=_MplsXCLspId_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,9,1,2),_MplsXCLspId_Type())
mplsXCLspId.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCLspId.setStatus(_A)
class _MplsXCLabelStackIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MplsXCLabelStackIndex_Type.__name__=_E
_MplsXCLabelStackIndex_Object=MibTableColumn
mplsXCLabelStackIndex=_MplsXCLabelStackIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,9,1,3),_MplsXCLabelStackIndex_Type())
mplsXCLabelStackIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCLabelStackIndex.setStatus(_A)
class _MplsXCIsPersistent_Type(TruthValue):defaultValue=2
_MplsXCIsPersistent_Type.__name__=_J
_MplsXCIsPersistent_Object=MibTableColumn
mplsXCIsPersistent=_MplsXCIsPersistent_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,9,1,4),_MplsXCIsPersistent_Type())
mplsXCIsPersistent.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCIsPersistent.setStatus(_A)
_MplsXCOwner_Type=MplsInitialCreationSource
_MplsXCOwner_Object=MibTableColumn
mplsXCOwner=_MplsXCOwner_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,9,1,5),_MplsXCOwner_Type())
mplsXCOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCOwner.setStatus(_A)
_MplsXCRowStatus_Type=RowStatus
_MplsXCRowStatus_Object=MibTableColumn
mplsXCRowStatus=_MplsXCRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,9,1,6),_MplsXCRowStatus_Type())
mplsXCRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCRowStatus.setStatus(_A)
_MplsXCStorageType_Type=StorageType
_MplsXCStorageType_Object=MibTableColumn
mplsXCStorageType=_MplsXCStorageType_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,9,1,7),_MplsXCStorageType_Type())
mplsXCStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCStorageType.setStatus(_A)
class _MplsXCAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_Y,3)))
_MplsXCAdminStatus_Type.__name__=_H
_MplsXCAdminStatus_Object=MibTableColumn
mplsXCAdminStatus=_MplsXCAdminStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,9,1,8),_MplsXCAdminStatus_Type())
mplsXCAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCAdminStatus.setStatus(_A)
class _MplsXCOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('up',1),('down',2),(_Y,3),('unknown',4),('dormant',5),('notPresent',6),('lowerLayerDown',7)))
_MplsXCOperStatus_Type.__name__=_H
_MplsXCOperStatus_Object=MibTableColumn
mplsXCOperStatus=_MplsXCOperStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,9,1,9),_MplsXCOperStatus_Type())
mplsXCOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsXCOperStatus.setStatus(_A)
class _MplsMaxLabelStackDepth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsMaxLabelStackDepth_Type.__name__=_H
_MplsMaxLabelStackDepth_Object=MibScalar
mplsMaxLabelStackDepth=_MplsMaxLabelStackDepth_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,10),_MplsMaxLabelStackDepth_Type())
mplsMaxLabelStackDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsMaxLabelStackDepth.setStatus(_A)
class _MplsLabelStackIndexNext_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MplsLabelStackIndexNext_Type.__name__=_E
_MplsLabelStackIndexNext_Object=MibScalar
mplsLabelStackIndexNext=_MplsLabelStackIndexNext_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,11),_MplsLabelStackIndexNext_Type())
mplsLabelStackIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLabelStackIndexNext.setStatus(_A)
_MplsLabelStackTable_Object=MibTable
mplsLabelStackTable=_MplsLabelStackTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,12))
if mibBuilder.loadTexts:mplsLabelStackTable.setStatus(_A)
_MplsLabelStackEntry_Object=MibTableRow
mplsLabelStackEntry=_MplsLabelStackEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,12,1))
mplsLabelStackEntry.setIndexNames((0,_B,_Z),(0,_B,_a))
if mibBuilder.loadTexts:mplsLabelStackEntry.setStatus(_A)
class _MplsLabelStackIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsLabelStackIndex_Type.__name__=_E
_MplsLabelStackIndex_Object=MibTableColumn
mplsLabelStackIndex=_MplsLabelStackIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,12,1,1),_MplsLabelStackIndex_Type())
mplsLabelStackIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsLabelStackIndex.setStatus(_A)
class _MplsLabelStackLabelIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsLabelStackLabelIndex_Type.__name__=_E
_MplsLabelStackLabelIndex_Object=MibTableColumn
mplsLabelStackLabelIndex=_MplsLabelStackLabelIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,12,1,2),_MplsLabelStackLabelIndex_Type())
mplsLabelStackLabelIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsLabelStackLabelIndex.setStatus(_A)
_MplsLabelStackLabel_Type=MplsLabel
_MplsLabelStackLabel_Object=MibTableColumn
mplsLabelStackLabel=_MplsLabelStackLabel_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,12,1,3),_MplsLabelStackLabel_Type())
mplsLabelStackLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLabelStackLabel.setStatus(_A)
_MplsLabelStackRowStatus_Type=RowStatus
_MplsLabelStackRowStatus_Object=MibTableColumn
mplsLabelStackRowStatus=_MplsLabelStackRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,12,1,4),_MplsLabelStackRowStatus_Type())
mplsLabelStackRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLabelStackRowStatus.setStatus(_A)
_MplsLabelStackStorageType_Type=StorageType
_MplsLabelStackStorageType_Object=MibTableColumn
mplsLabelStackStorageType=_MplsLabelStackStorageType_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,12,1,5),_MplsLabelStackStorageType_Type())
mplsLabelStackStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLabelStackStorageType.setStatus(_A)
class _MplsTrafficParamIndexNext_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MplsTrafficParamIndexNext_Type.__name__=_E
_MplsTrafficParamIndexNext_Object=MibScalar
mplsTrafficParamIndexNext=_MplsTrafficParamIndexNext_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,13),_MplsTrafficParamIndexNext_Type())
mplsTrafficParamIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTrafficParamIndexNext.setStatus(_A)
_MplsTrafficParamTable_Object=MibTable
mplsTrafficParamTable=_MplsTrafficParamTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,14))
if mibBuilder.loadTexts:mplsTrafficParamTable.setStatus(_A)
_MplsTrafficParamEntry_Object=MibTableRow
mplsTrafficParamEntry=_MplsTrafficParamEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,14,1))
mplsTrafficParamEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:mplsTrafficParamEntry.setStatus(_A)
class _MplsTrafficParamIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsTrafficParamIndex_Type.__name__=_E
_MplsTrafficParamIndex_Object=MibTableColumn
mplsTrafficParamIndex=_MplsTrafficParamIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,14,1,1),_MplsTrafficParamIndex_Type())
mplsTrafficParamIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsTrafficParamIndex.setStatus(_A)
_MplsTrafficParamMaxRate_Type=MplsBitRate
_MplsTrafficParamMaxRate_Object=MibTableColumn
mplsTrafficParamMaxRate=_MplsTrafficParamMaxRate_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,14,1,2),_MplsTrafficParamMaxRate_Type())
mplsTrafficParamMaxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTrafficParamMaxRate.setStatus(_A)
if mibBuilder.loadTexts:mplsTrafficParamMaxRate.setUnits(_c)
_MplsTrafficParamMeanRate_Type=MplsBitRate
_MplsTrafficParamMeanRate_Object=MibTableColumn
mplsTrafficParamMeanRate=_MplsTrafficParamMeanRate_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,14,1,3),_MplsTrafficParamMeanRate_Type())
mplsTrafficParamMeanRate.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTrafficParamMeanRate.setStatus(_A)
if mibBuilder.loadTexts:mplsTrafficParamMeanRate.setUnits(_c)
_MplsTrafficParamMaxBurstSize_Type=MplsBurstSize
_MplsTrafficParamMaxBurstSize_Object=MibTableColumn
mplsTrafficParamMaxBurstSize=_MplsTrafficParamMaxBurstSize_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,14,1,4),_MplsTrafficParamMaxBurstSize_Type())
mplsTrafficParamMaxBurstSize.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTrafficParamMaxBurstSize.setStatus(_A)
if mibBuilder.loadTexts:mplsTrafficParamMaxBurstSize.setUnits('bytes')
_MplsTrafficParamRowStatus_Type=RowStatus
_MplsTrafficParamRowStatus_Object=MibTableColumn
mplsTrafficParamRowStatus=_MplsTrafficParamRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,14,1,5),_MplsTrafficParamRowStatus_Type())
mplsTrafficParamRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTrafficParamRowStatus.setStatus(_A)
_MplsTrafficParamStorageType_Type=StorageType
_MplsTrafficParamStorageType_Object=MibTableColumn
mplsTrafficParamStorageType=_MplsTrafficParamStorageType_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,14,1,6),_MplsTrafficParamStorageType_Type())
mplsTrafficParamStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTrafficParamStorageType.setStatus(_A)
class _MplsXCTrapEnable_Type(TruthValue):defaultValue=2
_MplsXCTrapEnable_Type.__name__=_J
_MplsXCTrapEnable_Object=MibScalar
mplsXCTrapEnable=_MplsXCTrapEnable_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,1,15),_MplsXCTrapEnable_Type())
mplsXCTrapEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:mplsXCTrapEnable.setStatus(_A)
_MplsLsrNotifications_ObjectIdentity=ObjectIdentity
mplsLsrNotifications=_MplsLsrNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,2))
_MplsLsrNotifyPrefix_ObjectIdentity=ObjectIdentity
mplsLsrNotifyPrefix=_MplsLsrNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,2,0))
_MplsLsrConformance_ObjectIdentity=ObjectIdentity
mplsLsrConformance=_MplsLsrConformance_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,3))
_MplsLsrGroups_ObjectIdentity=ObjectIdentity
mplsLsrGroups=_MplsLsrGroups_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,3,1))
_MplsLsrCompliances_ObjectIdentity=ObjectIdentity
mplsLsrCompliances=_MplsLsrCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,3,2))
mplsInterfaceConfEntry.registerAugmentions((_B,_d))
mplsInterfacePerfEntry.setIndexNames(*mplsInterfaceConfEntry.getIndexNames())
mplsInSegmentEntry.registerAugmentions((_B,_e))
mplsInSegmentPerfEntry.setIndexNames(*mplsInSegmentEntry.getIndexNames())
mplsOutSegmentEntry.registerAugmentions((_B,_f))
mplsOutSegmentPerfEntry.setIndexNames(*mplsOutSegmentEntry.getIndexNames())
mplsInterfaceGroup=ObjectGroup((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,3,1,1))
mplsInterfaceGroup.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:mplsInterfaceGroup.setStatus(_A)
mplsInSegmentGroup=ObjectGroup((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,3,1,2))
mplsInSegmentGroup.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_N),(_B,_O),(_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:mplsInSegmentGroup.setStatus(_A)
mplsOutSegmentGroup=ObjectGroup((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,3,1,3))
mplsOutSegmentGroup.setObjects(*((_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_P),(_B,_Q),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:mplsOutSegmentGroup.setStatus(_A)
mplsXCGroup=ObjectGroup((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,3,1,4))
mplsXCGroup.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_G),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:mplsXCGroup.setStatus(_A)
mplsXCOptionalGroup=ObjectGroup((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,3,1,5))
mplsXCOptionalGroup.setObjects((_B,_AE))
if mibBuilder.loadTexts:mplsXCOptionalGroup.setStatus(_A)
mplsPerfGroup=ObjectGroup((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,3,1,6))
mplsPerfGroup.setObjects(*((_B,_N),(_B,_AF),(_B,_AG),(_B,_O),(_B,_P),(_B,_AH),(_B,_Q),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:mplsPerfGroup.setStatus(_A)
mplsHCInSegmentPerfGroup=ObjectGroup((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,3,1,7))
mplsHCInSegmentPerfGroup.setObjects((_B,_AM))
if mibBuilder.loadTexts:mplsHCInSegmentPerfGroup.setStatus(_A)
mplsHCOutSegmentPerfGroup=ObjectGroup((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,3,1,8))
mplsHCOutSegmentPerfGroup.setObjects((_B,_AN))
if mibBuilder.loadTexts:mplsHCOutSegmentPerfGroup.setStatus(_A)
mplsTrafficParamGroup=ObjectGroup((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,3,1,9))
mplsTrafficParamGroup.setObjects(*((_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT)))
if mibBuilder.loadTexts:mplsTrafficParamGroup.setStatus(_A)
mplsXCIsPersistentGroup=ObjectGroup((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,3,1,10))
mplsXCIsPersistentGroup.setObjects((_B,_R))
if mibBuilder.loadTexts:mplsXCIsPersistentGroup.setStatus(_A)
mplsXCIsNotPersistentGroup=ObjectGroup((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,3,1,11))
mplsXCIsNotPersistentGroup.setObjects((_B,_R))
if mibBuilder.loadTexts:mplsXCIsNotPersistentGroup.setStatus(_A)
mplsLabelStackGroup=ObjectGroup((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,3,1,12))
mplsLabelStackGroup.setObjects(*((_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY)))
if mibBuilder.loadTexts:mplsLabelStackGroup.setStatus(_A)
mplsSegmentDiscontinuityGroup=ObjectGroup((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,3,1,13))
mplsSegmentDiscontinuityGroup.setObjects(*((_B,_AZ),(_B,_Aa)))
if mibBuilder.loadTexts:mplsSegmentDiscontinuityGroup.setStatus(_A)
mplsXCUp=NotificationType((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,2,0,1))
mplsXCUp.setObjects(*((_B,_G),(_B,_G)))
if mibBuilder.loadTexts:mplsXCUp.setStatus(_A)
mplsXCDown=NotificationType((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,2,0,2))
mplsXCDown.setObjects(*((_B,_G),(_B,_G)))
if mibBuilder.loadTexts:mplsXCDown.setStatus(_A)
mplsLsrNotificationGroup=NotificationGroup((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,3,1,14))
mplsLsrNotificationGroup.setObjects(*((_B,'mplsXCUp'),(_B,_Ab)))
if mibBuilder.loadTexts:mplsLsrNotificationGroup.setStatus(_A)
mplsLsrModuleCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,3,7,11,12,2,15,15,2,3,2,1))
mplsLsrModuleCompliance.setObjects(*((_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am)))
if mibBuilder.loadTexts:mplsLsrModuleCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mplsLsrMIB':mplsLsrMIB,'mplsLsrObjects':mplsLsrObjects,'mplsInterfaceConfTable':mplsInterfaceConfTable,'mplsInterfaceConfEntry':mplsInterfaceConfEntry,_W:mplsInterfaceConfIndex,_g:mplsInterfaceLabelMinIn,_h:mplsInterfaceLabelMaxIn,_i:mplsInterfaceLabelMinOut,_j:mplsInterfaceLabelMaxOut,_k:mplsInterfaceTotalBandwidth,_l:mplsInterfaceAvailableBandwidth,_m:mplsInterfaceLabelParticipationType,'mplsInterfacePerfTable':mplsInterfacePerfTable,_d:mplsInterfacePerfEntry,_AI:mplsInterfaceInLabelsUsed,_AJ:mplsInterfaceFailedLabelLookup,_AL:mplsInterfaceOutLabelsUsed,_AK:mplsInterfaceOutFragments,'mplsInSegmentTable':mplsInSegmentTable,'mplsInSegmentEntry':mplsInSegmentEntry,_K:mplsInSegmentIfIndex,_L:mplsInSegmentLabel,_n:mplsInSegmentNPop,_o:mplsInSegmentAddrFamily,_p:mplsInSegmentXCIndex,_q:mplsInSegmentOwner,_t:mplsInSegmentTrafficParamPtr,_r:mplsInSegmentRowStatus,_s:mplsInSegmentStorageType,'mplsInSegmentPerfTable':mplsInSegmentPerfTable,_e:mplsInSegmentPerfEntry,_N:mplsInSegmentOctets,_AF:mplsInSegmentPackets,_AG:mplsInSegmentErrors,_O:mplsInSegmentDiscards,_AM:mplsInSegmentHCOctets,_AZ:mplsInSegmentPerfDiscontinuityTime,_u:mplsOutSegmentIndexNext,'mplsOutSegmentTable':mplsOutSegmentTable,'mplsOutSegmentEntry':mplsOutSegmentEntry,_M:mplsOutSegmentIndex,_v:mplsOutSegmentIfIndex,_w:mplsOutSegmentPushTopLabel,_x:mplsOutSegmentTopLabel,_y:mplsOutSegmentNextHopIpAddrType,_z:mplsOutSegmentNextHopIpv4Addr,_A0:mplsOutSegmentNextHopIpv6Addr,_A1:mplsOutSegmentXCIndex,_A2:mplsOutSegmentOwner,_A6:mplsOutSegmentTrafficParamPtr,_A4:mplsOutSegmentRowStatus,_A5:mplsOutSegmentStorageType,'mplsOutSegmentPerfTable':mplsOutSegmentPerfTable,_f:mplsOutSegmentPerfEntry,_P:mplsOutSegmentOctets,_AH:mplsOutSegmentPackets,_A3:mplsOutSegmentErrors,_Q:mplsOutSegmentDiscards,_AN:mplsOutSegmentHCOctets,_Aa:mplsOutSegmentPerfDiscontinuityTime,_A7:mplsXCIndexNext,'mplsXCTable':mplsXCTable,'mplsXCEntry':mplsXCEntry,_X:mplsXCIndex,_AE:mplsXCLspId,_A8:mplsXCLabelStackIndex,_R:mplsXCIsPersistent,_A9:mplsXCOwner,_AB:mplsXCRowStatus,_AD:mplsXCStorageType,_AA:mplsXCAdminStatus,_G:mplsXCOperStatus,_AX:mplsMaxLabelStackDepth,_AY:mplsLabelStackIndexNext,'mplsLabelStackTable':mplsLabelStackTable,'mplsLabelStackEntry':mplsLabelStackEntry,_Z:mplsLabelStackIndex,_a:mplsLabelStackLabelIndex,_AU:mplsLabelStackLabel,_AV:mplsLabelStackRowStatus,_AW:mplsLabelStackStorageType,_AO:mplsTrafficParamIndexNext,'mplsTrafficParamTable':mplsTrafficParamTable,'mplsTrafficParamEntry':mplsTrafficParamEntry,_b:mplsTrafficParamIndex,_AP:mplsTrafficParamMaxRate,_AQ:mplsTrafficParamMeanRate,_AR:mplsTrafficParamMaxBurstSize,_AS:mplsTrafficParamRowStatus,_AT:mplsTrafficParamStorageType,_AC:mplsXCTrapEnable,'mplsLsrNotifications':mplsLsrNotifications,'mplsLsrNotifyPrefix':mplsLsrNotifyPrefix,'mplsXCUp':mplsXCUp,_Ab:mplsXCDown,'mplsLsrConformance':mplsLsrConformance,'mplsLsrGroups':mplsLsrGroups,_Af:mplsInterfaceGroup,_Ac:mplsInSegmentGroup,_Ad:mplsOutSegmentGroup,_Ae:mplsXCGroup,'mplsXCOptionalGroup':mplsXCOptionalGroup,_Ag:mplsPerfGroup,_Ai:mplsHCInSegmentPerfGroup,_Aj:mplsHCOutSegmentPerfGroup,_Ak:mplsTrafficParamGroup,_Al:mplsXCIsPersistentGroup,_Am:mplsXCIsNotPersistentGroup,'mplsLabelStackGroup':mplsLabelStackGroup,_Ah:mplsSegmentDiscontinuityGroup,'mplsLsrNotificationGroup':mplsLsrNotificationGroup,'mplsLsrCompliances':mplsLsrCompliances,'mplsLsrModuleCompliance':mplsLsrModuleCompliance})