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
_AA='mplsXCOwner'
_A9='mplsXCLabelStackIndex'
_A8='mplsXCIndexNext'
_A7='mplsOutSegmentTrafficParamPtr'
_A6='mplsOutSegmentStorageType'
_A5='mplsOutSegmentRowStatus'
_A4='mplsOutSegmentErrors'
_A3='mplsOutSegmentOwner'
_A2='mplsOutSegmentXCIndex'
_A1='mplsOutSegmentNextHopIpv6Addr'
_A0='mplsOutSegmentNextHopIpv4Addr'
_z='mplsOutSegmentNextHopIpAddrType'
_y='mplsOutSegmentTopLabel'
_x='mplsOutSegmentPushTopLabel'
_w='mplsOutSegmentIfIndex'
_v='mplsOutSegmentIndexNext'
_u='mplsInSegmentTrafficParamPtr'
_t='mplsInSegmentStorageType'
_s='mplsInSegmentRowStatus'
_r='mplsInSegmentOwner'
_q='mplsInSegmentXCIndex'
_p='mplsInSegmentAddrFamily'
_o='mplsInSegmentNPop'
_n='mplsInterfaceConfStorageType'
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
_X='mplsInterfaceConfIndex'
_W='unknown'
_V='InetAddressType'
_U='AddressFamilyNumbers'
_T='mplsXCIsPersistent'
_S='mplsOutSegmentDiscards'
_R='mplsOutSegmentOctets'
_Q='mplsInSegmentDiscards'
_P='mplsInSegmentOctets'
_O='MplsObjectOwner'
_N='TruthValue'
_M='mplsXCOperStatus'
_L='mplsXCAdminStatus'
_K='mplsXCIndex'
_J='accessible-for-notify'
_I='not-accessible'
_H='mplsOutSegmentIndex'
_G='mplsInSegmentLabel'
_F='mplsInSegmentIfIndex'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='HUAWEI-MPLS-LSR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
huaweiMgmt,hwMpls=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','huaweiMgmt','hwMpls')
AddressFamilyNumbers,=mibBuilder.importSymbols('IANA-ADDRESS-FAMILY-NUMBERS-MIB',_U)
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddressIPv4,InetAddressIPv6,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6',_V)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowPointer,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','RowStatus','StorageType','TextualConvention','TimeStamp',_N)
hwMplsLsr=ModuleIdentity((1,3,6,1,4,1,2011,5,12,1))
if mibBuilder.loadTexts:hwMplsLsr.setRevisions(('2000-07-12 12:00','2000-07-07 12:00','2000-04-26 12:00','2000-04-21 12:00','2000-03-06 12:00','2000-02-16 12:00','1999-06-16 12:00'))
class MplsLSPID(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
class MplsLabel(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class MplsBitRate(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class MplsBurstSize(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class MplsObjectOwner(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('other',1),('snmp',2),('ldp',3),('rsvp',4),('crldp',5),('policyAgent',6),(_W,7)))
_MplsLsrObjects_ObjectIdentity=ObjectIdentity
mplsLsrObjects=_MplsLsrObjects_ObjectIdentity((1,3,6,1,4,1,2011,5,12,1,1))
_MplsInterfaceConfTable_Object=MibTable
mplsInterfaceConfTable=_MplsInterfaceConfTable_Object((1,3,6,1,4,1,2011,5,12,1,1,1))
if mibBuilder.loadTexts:mplsInterfaceConfTable.setStatus(_A)
_MplsInterfaceConfEntry_Object=MibTableRow
mplsInterfaceConfEntry=_MplsInterfaceConfEntry_Object((1,3,6,1,4,1,2011,5,12,1,1,1,1))
mplsInterfaceConfEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:mplsInterfaceConfEntry.setStatus(_A)
_MplsInterfaceConfIndex_Type=InterfaceIndexOrZero
_MplsInterfaceConfIndex_Object=MibTableColumn
mplsInterfaceConfIndex=_MplsInterfaceConfIndex_Object((1,3,6,1,4,1,2011,5,12,1,1,1,1,1),_MplsInterfaceConfIndex_Type())
mplsInterfaceConfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:mplsInterfaceConfIndex.setStatus(_A)
_MplsInterfaceLabelMinIn_Type=MplsLabel
_MplsInterfaceLabelMinIn_Object=MibTableColumn
mplsInterfaceLabelMinIn=_MplsInterfaceLabelMinIn_Object((1,3,6,1,4,1,2011,5,12,1,1,1,1,2),_MplsInterfaceLabelMinIn_Type())
mplsInterfaceLabelMinIn.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInterfaceLabelMinIn.setStatus(_A)
_MplsInterfaceLabelMaxIn_Type=MplsLabel
_MplsInterfaceLabelMaxIn_Object=MibTableColumn
mplsInterfaceLabelMaxIn=_MplsInterfaceLabelMaxIn_Object((1,3,6,1,4,1,2011,5,12,1,1,1,1,3),_MplsInterfaceLabelMaxIn_Type())
mplsInterfaceLabelMaxIn.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInterfaceLabelMaxIn.setStatus(_A)
_MplsInterfaceLabelMinOut_Type=MplsLabel
_MplsInterfaceLabelMinOut_Object=MibTableColumn
mplsInterfaceLabelMinOut=_MplsInterfaceLabelMinOut_Object((1,3,6,1,4,1,2011,5,12,1,1,1,1,4),_MplsInterfaceLabelMinOut_Type())
mplsInterfaceLabelMinOut.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInterfaceLabelMinOut.setStatus(_A)
_MplsInterfaceLabelMaxOut_Type=MplsLabel
_MplsInterfaceLabelMaxOut_Object=MibTableColumn
mplsInterfaceLabelMaxOut=_MplsInterfaceLabelMaxOut_Object((1,3,6,1,4,1,2011,5,12,1,1,1,1,5),_MplsInterfaceLabelMaxOut_Type())
mplsInterfaceLabelMaxOut.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInterfaceLabelMaxOut.setStatus(_A)
_MplsInterfaceTotalBandwidth_Type=MplsBitRate
_MplsInterfaceTotalBandwidth_Object=MibTableColumn
mplsInterfaceTotalBandwidth=_MplsInterfaceTotalBandwidth_Object((1,3,6,1,4,1,2011,5,12,1,1,1,1,6),_MplsInterfaceTotalBandwidth_Type())
mplsInterfaceTotalBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInterfaceTotalBandwidth.setStatus(_A)
_MplsInterfaceAvailableBandwidth_Type=MplsBitRate
_MplsInterfaceAvailableBandwidth_Object=MibTableColumn
mplsInterfaceAvailableBandwidth=_MplsInterfaceAvailableBandwidth_Object((1,3,6,1,4,1,2011,5,12,1,1,1,1,7),_MplsInterfaceAvailableBandwidth_Type())
mplsInterfaceAvailableBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInterfaceAvailableBandwidth.setStatus(_A)
class _MplsInterfaceLabelParticipationType_Type(Bits):namedValues=NamedValues(*(('perPlatform',0),('perInterface',1)))
_MplsInterfaceLabelParticipationType_Type.__name__='Bits'
_MplsInterfaceLabelParticipationType_Object=MibTableColumn
mplsInterfaceLabelParticipationType=_MplsInterfaceLabelParticipationType_Object((1,3,6,1,4,1,2011,5,12,1,1,1,1,8),_MplsInterfaceLabelParticipationType_Type())
mplsInterfaceLabelParticipationType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInterfaceLabelParticipationType.setStatus(_A)
_MplsInterfaceConfStorageType_Type=StorageType
_MplsInterfaceConfStorageType_Object=MibTableColumn
mplsInterfaceConfStorageType=_MplsInterfaceConfStorageType_Object((1,3,6,1,4,1,2011,5,12,1,1,1,1,9),_MplsInterfaceConfStorageType_Type())
mplsInterfaceConfStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceConfStorageType.setStatus(_A)
_MplsInterfacePerfTable_Object=MibTable
mplsInterfacePerfTable=_MplsInterfacePerfTable_Object((1,3,6,1,4,1,2011,5,12,1,1,2))
if mibBuilder.loadTexts:mplsInterfacePerfTable.setStatus(_A)
_MplsInterfacePerfEntry_Object=MibTableRow
mplsInterfacePerfEntry=_MplsInterfacePerfEntry_Object((1,3,6,1,4,1,2011,5,12,1,1,2,1))
if mibBuilder.loadTexts:mplsInterfacePerfEntry.setStatus(_A)
_MplsInterfaceInLabelsUsed_Type=Gauge32
_MplsInterfaceInLabelsUsed_Object=MibTableColumn
mplsInterfaceInLabelsUsed=_MplsInterfaceInLabelsUsed_Object((1,3,6,1,4,1,2011,5,12,1,1,2,1,1),_MplsInterfaceInLabelsUsed_Type())
mplsInterfaceInLabelsUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInterfaceInLabelsUsed.setStatus(_A)
_MplsInterfaceFailedLabelLookup_Type=Counter32
_MplsInterfaceFailedLabelLookup_Object=MibTableColumn
mplsInterfaceFailedLabelLookup=_MplsInterfaceFailedLabelLookup_Object((1,3,6,1,4,1,2011,5,12,1,1,2,1,2),_MplsInterfaceFailedLabelLookup_Type())
mplsInterfaceFailedLabelLookup.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInterfaceFailedLabelLookup.setStatus(_A)
_MplsInterfaceOutLabelsUsed_Type=Gauge32
_MplsInterfaceOutLabelsUsed_Object=MibTableColumn
mplsInterfaceOutLabelsUsed=_MplsInterfaceOutLabelsUsed_Object((1,3,6,1,4,1,2011,5,12,1,1,2,1,3),_MplsInterfaceOutLabelsUsed_Type())
mplsInterfaceOutLabelsUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInterfaceOutLabelsUsed.setStatus(_A)
_MplsInterfaceOutFragments_Type=Counter32
_MplsInterfaceOutFragments_Object=MibTableColumn
mplsInterfaceOutFragments=_MplsInterfaceOutFragments_Object((1,3,6,1,4,1,2011,5,12,1,1,2,1,4),_MplsInterfaceOutFragments_Type())
mplsInterfaceOutFragments.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInterfaceOutFragments.setStatus(_A)
_MplsInSegmentTable_Object=MibTable
mplsInSegmentTable=_MplsInSegmentTable_Object((1,3,6,1,4,1,2011,5,12,1,1,3))
if mibBuilder.loadTexts:mplsInSegmentTable.setStatus(_A)
_MplsInSegmentEntry_Object=MibTableRow
mplsInSegmentEntry=_MplsInSegmentEntry_Object((1,3,6,1,4,1,2011,5,12,1,1,3,1))
mplsInSegmentEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:mplsInSegmentEntry.setStatus(_A)
_MplsInSegmentIfIndex_Type=InterfaceIndexOrZero
_MplsInSegmentIfIndex_Object=MibTableColumn
mplsInSegmentIfIndex=_MplsInSegmentIfIndex_Object((1,3,6,1,4,1,2011,5,12,1,1,3,1,1),_MplsInSegmentIfIndex_Type())
mplsInSegmentIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:mplsInSegmentIfIndex.setStatus(_A)
_MplsInSegmentLabel_Type=MplsLabel
_MplsInSegmentLabel_Object=MibTableColumn
mplsInSegmentLabel=_MplsInSegmentLabel_Object((1,3,6,1,4,1,2011,5,12,1,1,3,1,2),_MplsInSegmentLabel_Type())
mplsInSegmentLabel.setMaxAccess(_J)
if mibBuilder.loadTexts:mplsInSegmentLabel.setStatus(_A)
class _MplsInSegmentNPop_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsInSegmentNPop_Type.__name__=_E
_MplsInSegmentNPop_Object=MibTableColumn
mplsInSegmentNPop=_MplsInSegmentNPop_Object((1,3,6,1,4,1,2011,5,12,1,1,3,1,3),_MplsInSegmentNPop_Type())
mplsInSegmentNPop.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentNPop.setStatus(_A)
class _MplsInSegmentAddrFamily_Type(AddressFamilyNumbers):defaultValue=0
_MplsInSegmentAddrFamily_Type.__name__=_U
_MplsInSegmentAddrFamily_Object=MibTableColumn
mplsInSegmentAddrFamily=_MplsInSegmentAddrFamily_Object((1,3,6,1,4,1,2011,5,12,1,1,3,1,4),_MplsInSegmentAddrFamily_Type())
mplsInSegmentAddrFamily.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentAddrFamily.setStatus(_A)
class _MplsInSegmentXCIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsInSegmentXCIndex_Type.__name__=_E
_MplsInSegmentXCIndex_Object=MibTableColumn
mplsInSegmentXCIndex=_MplsInSegmentXCIndex_Object((1,3,6,1,4,1,2011,5,12,1,1,3,1,5),_MplsInSegmentXCIndex_Type())
mplsInSegmentXCIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentXCIndex.setStatus(_A)
class _MplsInSegmentOwner_Type(MplsObjectOwner):defaultValue=7
_MplsInSegmentOwner_Type.__name__=_O
_MplsInSegmentOwner_Object=MibTableColumn
mplsInSegmentOwner=_MplsInSegmentOwner_Object((1,3,6,1,4,1,2011,5,12,1,1,3,1,6),_MplsInSegmentOwner_Type())
mplsInSegmentOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentOwner.setStatus(_A)
_MplsInSegmentTrafficParamPtr_Type=RowPointer
_MplsInSegmentTrafficParamPtr_Object=MibTableColumn
mplsInSegmentTrafficParamPtr=_MplsInSegmentTrafficParamPtr_Object((1,3,6,1,4,1,2011,5,12,1,1,3,1,7),_MplsInSegmentTrafficParamPtr_Type())
mplsInSegmentTrafficParamPtr.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentTrafficParamPtr.setStatus(_A)
_MplsInSegmentRowStatus_Type=RowStatus
_MplsInSegmentRowStatus_Object=MibTableColumn
mplsInSegmentRowStatus=_MplsInSegmentRowStatus_Object((1,3,6,1,4,1,2011,5,12,1,1,3,1,8),_MplsInSegmentRowStatus_Type())
mplsInSegmentRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentRowStatus.setStatus(_A)
_MplsInSegmentStorageType_Type=StorageType
_MplsInSegmentStorageType_Object=MibTableColumn
mplsInSegmentStorageType=_MplsInSegmentStorageType_Object((1,3,6,1,4,1,2011,5,12,1,1,3,1,9),_MplsInSegmentStorageType_Type())
mplsInSegmentStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentStorageType.setStatus(_A)
_MplsInSegmentPerfTable_Object=MibTable
mplsInSegmentPerfTable=_MplsInSegmentPerfTable_Object((1,3,6,1,4,1,2011,5,12,1,1,4))
if mibBuilder.loadTexts:mplsInSegmentPerfTable.setStatus(_A)
_MplsInSegmentPerfEntry_Object=MibTableRow
mplsInSegmentPerfEntry=_MplsInSegmentPerfEntry_Object((1,3,6,1,4,1,2011,5,12,1,1,4,1))
if mibBuilder.loadTexts:mplsInSegmentPerfEntry.setStatus(_A)
_MplsInSegmentOctets_Type=Counter32
_MplsInSegmentOctets_Object=MibTableColumn
mplsInSegmentOctets=_MplsInSegmentOctets_Object((1,3,6,1,4,1,2011,5,12,1,1,4,1,1),_MplsInSegmentOctets_Type())
mplsInSegmentOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentOctets.setStatus(_A)
_MplsInSegmentPackets_Type=Counter32
_MplsInSegmentPackets_Object=MibTableColumn
mplsInSegmentPackets=_MplsInSegmentPackets_Object((1,3,6,1,4,1,2011,5,12,1,1,4,1,2),_MplsInSegmentPackets_Type())
mplsInSegmentPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentPackets.setStatus(_A)
_MplsInSegmentErrors_Type=Counter32
_MplsInSegmentErrors_Object=MibTableColumn
mplsInSegmentErrors=_MplsInSegmentErrors_Object((1,3,6,1,4,1,2011,5,12,1,1,4,1,3),_MplsInSegmentErrors_Type())
mplsInSegmentErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentErrors.setStatus(_A)
_MplsInSegmentDiscards_Type=Counter32
_MplsInSegmentDiscards_Object=MibTableColumn
mplsInSegmentDiscards=_MplsInSegmentDiscards_Object((1,3,6,1,4,1,2011,5,12,1,1,4,1,4),_MplsInSegmentDiscards_Type())
mplsInSegmentDiscards.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentDiscards.setStatus(_A)
_MplsInSegmentHCOctets_Type=Counter64
_MplsInSegmentHCOctets_Object=MibTableColumn
mplsInSegmentHCOctets=_MplsInSegmentHCOctets_Object((1,3,6,1,4,1,2011,5,12,1,1,4,1,5),_MplsInSegmentHCOctets_Type())
mplsInSegmentHCOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentHCOctets.setStatus(_A)
_MplsInSegmentPerfDiscontinuityTime_Type=TimeStamp
_MplsInSegmentPerfDiscontinuityTime_Object=MibTableColumn
mplsInSegmentPerfDiscontinuityTime=_MplsInSegmentPerfDiscontinuityTime_Object((1,3,6,1,4,1,2011,5,12,1,1,4,1,6),_MplsInSegmentPerfDiscontinuityTime_Type())
mplsInSegmentPerfDiscontinuityTime.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentPerfDiscontinuityTime.setStatus(_A)
class _MplsOutSegmentIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsOutSegmentIndexNext_Type.__name__=_E
_MplsOutSegmentIndexNext_Object=MibScalar
mplsOutSegmentIndexNext=_MplsOutSegmentIndexNext_Object((1,3,6,1,4,1,2011,5,12,1,1,5),_MplsOutSegmentIndexNext_Type())
mplsOutSegmentIndexNext.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentIndexNext.setStatus(_A)
_MplsOutSegmentTable_Object=MibTable
mplsOutSegmentTable=_MplsOutSegmentTable_Object((1,3,6,1,4,1,2011,5,12,1,1,6))
if mibBuilder.loadTexts:mplsOutSegmentTable.setStatus(_A)
_MplsOutSegmentEntry_Object=MibTableRow
mplsOutSegmentEntry=_MplsOutSegmentEntry_Object((1,3,6,1,4,1,2011,5,12,1,1,6,1))
mplsOutSegmentEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:mplsOutSegmentEntry.setStatus(_A)
class _MplsOutSegmentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsOutSegmentIndex_Type.__name__=_E
_MplsOutSegmentIndex_Object=MibTableColumn
mplsOutSegmentIndex=_MplsOutSegmentIndex_Object((1,3,6,1,4,1,2011,5,12,1,1,6,1,1),_MplsOutSegmentIndex_Type())
mplsOutSegmentIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:mplsOutSegmentIndex.setStatus(_A)
_MplsOutSegmentIfIndex_Type=InterfaceIndex
_MplsOutSegmentIfIndex_Object=MibTableColumn
mplsOutSegmentIfIndex=_MplsOutSegmentIfIndex_Object((1,3,6,1,4,1,2011,5,12,1,1,6,1,2),_MplsOutSegmentIfIndex_Type())
mplsOutSegmentIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentIfIndex.setStatus(_A)
_MplsOutSegmentPushTopLabel_Type=TruthValue
_MplsOutSegmentPushTopLabel_Object=MibTableColumn
mplsOutSegmentPushTopLabel=_MplsOutSegmentPushTopLabel_Object((1,3,6,1,4,1,2011,5,12,1,1,6,1,3),_MplsOutSegmentPushTopLabel_Type())
mplsOutSegmentPushTopLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentPushTopLabel.setStatus(_A)
_MplsOutSegmentTopLabel_Type=MplsLabel
_MplsOutSegmentTopLabel_Object=MibTableColumn
mplsOutSegmentTopLabel=_MplsOutSegmentTopLabel_Object((1,3,6,1,4,1,2011,5,12,1,1,6,1,4),_MplsOutSegmentTopLabel_Type())
mplsOutSegmentTopLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentTopLabel.setStatus(_A)
class _MplsOutSegmentNextHopIpAddrType_Type(InetAddressType):defaultValue=0
_MplsOutSegmentNextHopIpAddrType_Type.__name__=_V
_MplsOutSegmentNextHopIpAddrType_Object=MibTableColumn
mplsOutSegmentNextHopIpAddrType=_MplsOutSegmentNextHopIpAddrType_Object((1,3,6,1,4,1,2011,5,12,1,1,6,1,5),_MplsOutSegmentNextHopIpAddrType_Type())
mplsOutSegmentNextHopIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentNextHopIpAddrType.setStatus(_A)
_MplsOutSegmentNextHopIpv4Addr_Type=InetAddressIPv4
_MplsOutSegmentNextHopIpv4Addr_Object=MibTableColumn
mplsOutSegmentNextHopIpv4Addr=_MplsOutSegmentNextHopIpv4Addr_Object((1,3,6,1,4,1,2011,5,12,1,1,6,1,6),_MplsOutSegmentNextHopIpv4Addr_Type())
mplsOutSegmentNextHopIpv4Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentNextHopIpv4Addr.setStatus(_A)
_MplsOutSegmentNextHopIpv6Addr_Type=InetAddressIPv6
_MplsOutSegmentNextHopIpv6Addr_Object=MibTableColumn
mplsOutSegmentNextHopIpv6Addr=_MplsOutSegmentNextHopIpv6Addr_Object((1,3,6,1,4,1,2011,5,12,1,1,6,1,7),_MplsOutSegmentNextHopIpv6Addr_Type())
mplsOutSegmentNextHopIpv6Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentNextHopIpv6Addr.setStatus(_A)
class _MplsOutSegmentXCIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsOutSegmentXCIndex_Type.__name__=_E
_MplsOutSegmentXCIndex_Object=MibTableColumn
mplsOutSegmentXCIndex=_MplsOutSegmentXCIndex_Object((1,3,6,1,4,1,2011,5,12,1,1,6,1,8),_MplsOutSegmentXCIndex_Type())
mplsOutSegmentXCIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentXCIndex.setStatus(_A)
class _MplsOutSegmentOwner_Type(MplsObjectOwner):defaultValue=7
_MplsOutSegmentOwner_Type.__name__=_O
_MplsOutSegmentOwner_Object=MibTableColumn
mplsOutSegmentOwner=_MplsOutSegmentOwner_Object((1,3,6,1,4,1,2011,5,12,1,1,6,1,9),_MplsOutSegmentOwner_Type())
mplsOutSegmentOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentOwner.setStatus(_A)
_MplsOutSegmentTrafficParamPtr_Type=RowPointer
_MplsOutSegmentTrafficParamPtr_Object=MibTableColumn
mplsOutSegmentTrafficParamPtr=_MplsOutSegmentTrafficParamPtr_Object((1,3,6,1,4,1,2011,5,12,1,1,6,1,10),_MplsOutSegmentTrafficParamPtr_Type())
mplsOutSegmentTrafficParamPtr.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentTrafficParamPtr.setStatus(_A)
_MplsOutSegmentRowStatus_Type=RowStatus
_MplsOutSegmentRowStatus_Object=MibTableColumn
mplsOutSegmentRowStatus=_MplsOutSegmentRowStatus_Object((1,3,6,1,4,1,2011,5,12,1,1,6,1,11),_MplsOutSegmentRowStatus_Type())
mplsOutSegmentRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentRowStatus.setStatus(_A)
_MplsOutSegmentStorageType_Type=StorageType
_MplsOutSegmentStorageType_Object=MibTableColumn
mplsOutSegmentStorageType=_MplsOutSegmentStorageType_Object((1,3,6,1,4,1,2011,5,12,1,1,6,1,12),_MplsOutSegmentStorageType_Type())
mplsOutSegmentStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentStorageType.setStatus(_A)
_MplsOutSegmentPerfTable_Object=MibTable
mplsOutSegmentPerfTable=_MplsOutSegmentPerfTable_Object((1,3,6,1,4,1,2011,5,12,1,1,7))
if mibBuilder.loadTexts:mplsOutSegmentPerfTable.setStatus(_A)
_MplsOutSegmentPerfEntry_Object=MibTableRow
mplsOutSegmentPerfEntry=_MplsOutSegmentPerfEntry_Object((1,3,6,1,4,1,2011,5,12,1,1,7,1))
if mibBuilder.loadTexts:mplsOutSegmentPerfEntry.setStatus(_A)
_MplsOutSegmentOctets_Type=Counter32
_MplsOutSegmentOctets_Object=MibTableColumn
mplsOutSegmentOctets=_MplsOutSegmentOctets_Object((1,3,6,1,4,1,2011,5,12,1,1,7,1,1),_MplsOutSegmentOctets_Type())
mplsOutSegmentOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentOctets.setStatus(_A)
_MplsOutSegmentPackets_Type=Counter32
_MplsOutSegmentPackets_Object=MibTableColumn
mplsOutSegmentPackets=_MplsOutSegmentPackets_Object((1,3,6,1,4,1,2011,5,12,1,1,7,1,2),_MplsOutSegmentPackets_Type())
mplsOutSegmentPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentPackets.setStatus(_A)
_MplsOutSegmentErrors_Type=Counter32
_MplsOutSegmentErrors_Object=MibTableColumn
mplsOutSegmentErrors=_MplsOutSegmentErrors_Object((1,3,6,1,4,1,2011,5,12,1,1,7,1,3),_MplsOutSegmentErrors_Type())
mplsOutSegmentErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentErrors.setStatus(_A)
_MplsOutSegmentDiscards_Type=Counter32
_MplsOutSegmentDiscards_Object=MibTableColumn
mplsOutSegmentDiscards=_MplsOutSegmentDiscards_Object((1,3,6,1,4,1,2011,5,12,1,1,7,1,4),_MplsOutSegmentDiscards_Type())
mplsOutSegmentDiscards.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentDiscards.setStatus(_A)
_MplsOutSegmentHCOctets_Type=Counter64
_MplsOutSegmentHCOctets_Object=MibTableColumn
mplsOutSegmentHCOctets=_MplsOutSegmentHCOctets_Object((1,3,6,1,4,1,2011,5,12,1,1,7,1,5),_MplsOutSegmentHCOctets_Type())
mplsOutSegmentHCOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentHCOctets.setStatus(_A)
_MplsOutSegmentPerfDiscontinuityTime_Type=TimeStamp
_MplsOutSegmentPerfDiscontinuityTime_Object=MibTableColumn
mplsOutSegmentPerfDiscontinuityTime=_MplsOutSegmentPerfDiscontinuityTime_Object((1,3,6,1,4,1,2011,5,12,1,1,7,1,6),_MplsOutSegmentPerfDiscontinuityTime_Type())
mplsOutSegmentPerfDiscontinuityTime.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentPerfDiscontinuityTime.setStatus(_A)
class _MplsXCIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsXCIndexNext_Type.__name__=_E
_MplsXCIndexNext_Object=MibScalar
mplsXCIndexNext=_MplsXCIndexNext_Object((1,3,6,1,4,1,2011,5,12,1,1,8),_MplsXCIndexNext_Type())
mplsXCIndexNext.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCIndexNext.setStatus(_A)
_MplsXCTable_Object=MibTable
mplsXCTable=_MplsXCTable_Object((1,3,6,1,4,1,2011,5,12,1,1,9))
if mibBuilder.loadTexts:mplsXCTable.setStatus(_A)
_MplsXCEntry_Object=MibTableRow
mplsXCEntry=_MplsXCEntry_Object((1,3,6,1,4,1,2011,5,12,1,1,9,1))
mplsXCEntry.setIndexNames((0,_B,_K),(0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:mplsXCEntry.setStatus(_A)
class _MplsXCIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsXCIndex_Type.__name__=_E
_MplsXCIndex_Object=MibTableColumn
mplsXCIndex=_MplsXCIndex_Object((1,3,6,1,4,1,2011,5,12,1,1,9,1,1),_MplsXCIndex_Type())
mplsXCIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:mplsXCIndex.setStatus(_A)
_MplsXCLspId_Type=MplsLSPID
_MplsXCLspId_Object=MibTableColumn
mplsXCLspId=_MplsXCLspId_Object((1,3,6,1,4,1,2011,5,12,1,1,9,1,2),_MplsXCLspId_Type())
mplsXCLspId.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsXCLspId.setStatus(_A)
class _MplsXCLabelStackIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsXCLabelStackIndex_Type.__name__=_E
_MplsXCLabelStackIndex_Object=MibTableColumn
mplsXCLabelStackIndex=_MplsXCLabelStackIndex_Object((1,3,6,1,4,1,2011,5,12,1,1,9,1,3),_MplsXCLabelStackIndex_Type())
mplsXCLabelStackIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsXCLabelStackIndex.setStatus(_A)
class _MplsXCIsPersistent_Type(TruthValue):defaultValue=2
_MplsXCIsPersistent_Type.__name__=_N
_MplsXCIsPersistent_Object=MibTableColumn
mplsXCIsPersistent=_MplsXCIsPersistent_Object((1,3,6,1,4,1,2011,5,12,1,1,9,1,4),_MplsXCIsPersistent_Type())
mplsXCIsPersistent.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsXCIsPersistent.setStatus(_A)
_MplsXCOwner_Type=MplsObjectOwner
_MplsXCOwner_Object=MibTableColumn
mplsXCOwner=_MplsXCOwner_Object((1,3,6,1,4,1,2011,5,12,1,1,9,1,5),_MplsXCOwner_Type())
mplsXCOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsXCOwner.setStatus(_A)
_MplsXCRowStatus_Type=RowStatus
_MplsXCRowStatus_Object=MibTableColumn
mplsXCRowStatus=_MplsXCRowStatus_Object((1,3,6,1,4,1,2011,5,12,1,1,9,1,6),_MplsXCRowStatus_Type())
mplsXCRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsXCRowStatus.setStatus(_A)
_MplsXCStorageType_Type=StorageType
_MplsXCStorageType_Object=MibTableColumn
mplsXCStorageType=_MplsXCStorageType_Object((1,3,6,1,4,1,2011,5,12,1,1,9,1,7),_MplsXCStorageType_Type())
mplsXCStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsXCStorageType.setStatus(_A)
class _MplsXCAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_Y,3)))
_MplsXCAdminStatus_Type.__name__=_E
_MplsXCAdminStatus_Object=MibTableColumn
mplsXCAdminStatus=_MplsXCAdminStatus_Object((1,3,6,1,4,1,2011,5,12,1,1,9,1,8),_MplsXCAdminStatus_Type())
mplsXCAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsXCAdminStatus.setStatus(_A)
class _MplsXCOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('up',1),('down',2),(_Y,3),(_W,4),('dormant',5),('notPresent',6),('lowerLayerDown',7)))
_MplsXCOperStatus_Type.__name__=_E
_MplsXCOperStatus_Object=MibTableColumn
mplsXCOperStatus=_MplsXCOperStatus_Object((1,3,6,1,4,1,2011,5,12,1,1,9,1,9),_MplsXCOperStatus_Type())
mplsXCOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCOperStatus.setStatus(_A)
class _MplsMaxLabelStackDepth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsMaxLabelStackDepth_Type.__name__=_E
_MplsMaxLabelStackDepth_Object=MibScalar
mplsMaxLabelStackDepth=_MplsMaxLabelStackDepth_Object((1,3,6,1,4,1,2011,5,12,1,1,10),_MplsMaxLabelStackDepth_Type())
mplsMaxLabelStackDepth.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsMaxLabelStackDepth.setStatus(_A)
class _MplsLabelStackIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsLabelStackIndexNext_Type.__name__=_E
_MplsLabelStackIndexNext_Object=MibScalar
mplsLabelStackIndexNext=_MplsLabelStackIndexNext_Object((1,3,6,1,4,1,2011,5,12,1,1,11),_MplsLabelStackIndexNext_Type())
mplsLabelStackIndexNext.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLabelStackIndexNext.setStatus(_A)
_MplsLabelStackTable_Object=MibTable
mplsLabelStackTable=_MplsLabelStackTable_Object((1,3,6,1,4,1,2011,5,12,1,1,12))
if mibBuilder.loadTexts:mplsLabelStackTable.setStatus(_A)
_MplsLabelStackEntry_Object=MibTableRow
mplsLabelStackEntry=_MplsLabelStackEntry_Object((1,3,6,1,4,1,2011,5,12,1,1,12,1))
mplsLabelStackEntry.setIndexNames((0,_B,_Z),(0,_B,_a))
if mibBuilder.loadTexts:mplsLabelStackEntry.setStatus(_A)
class _MplsLabelStackIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsLabelStackIndex_Type.__name__=_E
_MplsLabelStackIndex_Object=MibTableColumn
mplsLabelStackIndex=_MplsLabelStackIndex_Object((1,3,6,1,4,1,2011,5,12,1,1,12,1,1),_MplsLabelStackIndex_Type())
mplsLabelStackIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:mplsLabelStackIndex.setStatus(_A)
class _MplsLabelStackLabelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsLabelStackLabelIndex_Type.__name__=_E
_MplsLabelStackLabelIndex_Object=MibTableColumn
mplsLabelStackLabelIndex=_MplsLabelStackLabelIndex_Object((1,3,6,1,4,1,2011,5,12,1,1,12,1,2),_MplsLabelStackLabelIndex_Type())
mplsLabelStackLabelIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:mplsLabelStackLabelIndex.setStatus(_A)
_MplsLabelStackLabel_Type=MplsLabel
_MplsLabelStackLabel_Object=MibTableColumn
mplsLabelStackLabel=_MplsLabelStackLabel_Object((1,3,6,1,4,1,2011,5,12,1,1,12,1,3),_MplsLabelStackLabel_Type())
mplsLabelStackLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLabelStackLabel.setStatus(_A)
_MplsLabelStackRowStatus_Type=RowStatus
_MplsLabelStackRowStatus_Object=MibTableColumn
mplsLabelStackRowStatus=_MplsLabelStackRowStatus_Object((1,3,6,1,4,1,2011,5,12,1,1,12,1,4),_MplsLabelStackRowStatus_Type())
mplsLabelStackRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLabelStackRowStatus.setStatus(_A)
_MplsLabelStackStorageType_Type=StorageType
_MplsLabelStackStorageType_Object=MibTableColumn
mplsLabelStackStorageType=_MplsLabelStackStorageType_Object((1,3,6,1,4,1,2011,5,12,1,1,12,1,5),_MplsLabelStackStorageType_Type())
mplsLabelStackStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLabelStackStorageType.setStatus(_A)
class _MplsTrafficParamIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsTrafficParamIndexNext_Type.__name__=_E
_MplsTrafficParamIndexNext_Object=MibScalar
mplsTrafficParamIndexNext=_MplsTrafficParamIndexNext_Object((1,3,6,1,4,1,2011,5,12,1,1,13),_MplsTrafficParamIndexNext_Type())
mplsTrafficParamIndexNext.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTrafficParamIndexNext.setStatus(_A)
_MplsTrafficParamTable_Object=MibTable
mplsTrafficParamTable=_MplsTrafficParamTable_Object((1,3,6,1,4,1,2011,5,12,1,1,14))
if mibBuilder.loadTexts:mplsTrafficParamTable.setStatus(_A)
_MplsTrafficParamEntry_Object=MibTableRow
mplsTrafficParamEntry=_MplsTrafficParamEntry_Object((1,3,6,1,4,1,2011,5,12,1,1,14,1))
mplsTrafficParamEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:mplsTrafficParamEntry.setStatus(_A)
class _MplsTrafficParamIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsTrafficParamIndex_Type.__name__=_E
_MplsTrafficParamIndex_Object=MibTableColumn
mplsTrafficParamIndex=_MplsTrafficParamIndex_Object((1,3,6,1,4,1,2011,5,12,1,1,14,1,1),_MplsTrafficParamIndex_Type())
mplsTrafficParamIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:mplsTrafficParamIndex.setStatus(_A)
_MplsTrafficParamMaxRate_Type=MplsBitRate
_MplsTrafficParamMaxRate_Object=MibTableColumn
mplsTrafficParamMaxRate=_MplsTrafficParamMaxRate_Object((1,3,6,1,4,1,2011,5,12,1,1,14,1,2),_MplsTrafficParamMaxRate_Type())
mplsTrafficParamMaxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTrafficParamMaxRate.setStatus(_A)
if mibBuilder.loadTexts:mplsTrafficParamMaxRate.setUnits(_c)
_MplsTrafficParamMeanRate_Type=MplsBitRate
_MplsTrafficParamMeanRate_Object=MibTableColumn
mplsTrafficParamMeanRate=_MplsTrafficParamMeanRate_Object((1,3,6,1,4,1,2011,5,12,1,1,14,1,3),_MplsTrafficParamMeanRate_Type())
mplsTrafficParamMeanRate.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTrafficParamMeanRate.setStatus(_A)
if mibBuilder.loadTexts:mplsTrafficParamMeanRate.setUnits(_c)
_MplsTrafficParamMaxBurstSize_Type=MplsBurstSize
_MplsTrafficParamMaxBurstSize_Object=MibTableColumn
mplsTrafficParamMaxBurstSize=_MplsTrafficParamMaxBurstSize_Object((1,3,6,1,4,1,2011,5,12,1,1,14,1,4),_MplsTrafficParamMaxBurstSize_Type())
mplsTrafficParamMaxBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTrafficParamMaxBurstSize.setStatus(_A)
if mibBuilder.loadTexts:mplsTrafficParamMaxBurstSize.setUnits('bytes')
_MplsTrafficParamRowStatus_Type=RowStatus
_MplsTrafficParamRowStatus_Object=MibTableColumn
mplsTrafficParamRowStatus=_MplsTrafficParamRowStatus_Object((1,3,6,1,4,1,2011,5,12,1,1,14,1,5),_MplsTrafficParamRowStatus_Type())
mplsTrafficParamRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTrafficParamRowStatus.setStatus(_A)
_MplsTrafficParamStorageType_Type=StorageType
_MplsTrafficParamStorageType_Object=MibTableColumn
mplsTrafficParamStorageType=_MplsTrafficParamStorageType_Object((1,3,6,1,4,1,2011,5,12,1,1,14,1,6),_MplsTrafficParamStorageType_Type())
mplsTrafficParamStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTrafficParamStorageType.setStatus(_A)
class _MplsXCTrapEnable_Type(TruthValue):defaultValue=2
_MplsXCTrapEnable_Type.__name__=_N
_MplsXCTrapEnable_Object=MibScalar
mplsXCTrapEnable=_MplsXCTrapEnable_Object((1,3,6,1,4,1,2011,5,12,1,1,15),_MplsXCTrapEnable_Type())
mplsXCTrapEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:mplsXCTrapEnable.setStatus(_A)
_MplsLsrNotifications_ObjectIdentity=ObjectIdentity
mplsLsrNotifications=_MplsLsrNotifications_ObjectIdentity((1,3,6,1,4,1,2011,5,12,1,2))
_MplsLsrNotifyPrefix_ObjectIdentity=ObjectIdentity
mplsLsrNotifyPrefix=_MplsLsrNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,2011,5,12,1,2,0))
_MplsLsrConformance_ObjectIdentity=ObjectIdentity
mplsLsrConformance=_MplsLsrConformance_ObjectIdentity((1,3,6,1,4,1,2011,5,12,1,3))
_MplsLsrGroups_ObjectIdentity=ObjectIdentity
mplsLsrGroups=_MplsLsrGroups_ObjectIdentity((1,3,6,1,4,1,2011,5,12,1,3,1))
_MplsLsrCompliances_ObjectIdentity=ObjectIdentity
mplsLsrCompliances=_MplsLsrCompliances_ObjectIdentity((1,3,6,1,4,1,2011,5,12,1,3,2))
mplsInterfaceConfEntry.registerAugmentions((_B,_d))
mplsInterfacePerfEntry.setIndexNames(*mplsInterfaceConfEntry.getIndexNames())
mplsInSegmentEntry.registerAugmentions((_B,_e))
mplsInSegmentPerfEntry.setIndexNames(*mplsInSegmentEntry.getIndexNames())
mplsOutSegmentEntry.registerAugmentions((_B,_f))
mplsOutSegmentPerfEntry.setIndexNames(*mplsOutSegmentEntry.getIndexNames())
mplsInterfaceGroup=ObjectGroup((1,3,6,1,4,1,2011,5,12,1,3,1,1))
mplsInterfaceGroup.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:mplsInterfaceGroup.setStatus(_A)
mplsInSegmentGroup=ObjectGroup((1,3,6,1,4,1,2011,5,12,1,3,1,2))
mplsInSegmentGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_P),(_B,_Q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:mplsInSegmentGroup.setStatus(_A)
mplsOutSegmentGroup=ObjectGroup((1,3,6,1,4,1,2011,5,12,1,3,1,3))
mplsOutSegmentGroup.setObjects(*((_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_R),(_B,_S),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:mplsOutSegmentGroup.setStatus(_A)
mplsXCGroup=ObjectGroup((1,3,6,1,4,1,2011,5,12,1,3,1,4))
mplsXCGroup.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA),(_B,_L),(_B,_M),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:mplsXCGroup.setStatus(_A)
mplsXCOptionalGroup=ObjectGroup((1,3,6,1,4,1,2011,5,12,1,3,1,5))
mplsXCOptionalGroup.setObjects((_B,_AE))
if mibBuilder.loadTexts:mplsXCOptionalGroup.setStatus(_A)
mplsPerfGroup=ObjectGroup((1,3,6,1,4,1,2011,5,12,1,3,1,6))
mplsPerfGroup.setObjects(*((_B,_P),(_B,_AF),(_B,_AG),(_B,_Q),(_B,_R),(_B,_AH),(_B,_S),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:mplsPerfGroup.setStatus(_A)
mplsHCInSegmentPerfGroup=ObjectGroup((1,3,6,1,4,1,2011,5,12,1,3,1,7))
mplsHCInSegmentPerfGroup.setObjects((_B,_AM))
if mibBuilder.loadTexts:mplsHCInSegmentPerfGroup.setStatus(_A)
mplsHCOutSegmentPerfGroup=ObjectGroup((1,3,6,1,4,1,2011,5,12,1,3,1,8))
mplsHCOutSegmentPerfGroup.setObjects((_B,_AN))
if mibBuilder.loadTexts:mplsHCOutSegmentPerfGroup.setStatus(_A)
mplsTrafficParamGroup=ObjectGroup((1,3,6,1,4,1,2011,5,12,1,3,1,9))
mplsTrafficParamGroup.setObjects(*((_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT)))
if mibBuilder.loadTexts:mplsTrafficParamGroup.setStatus(_A)
mplsXCIsPersistentGroup=ObjectGroup((1,3,6,1,4,1,2011,5,12,1,3,1,10))
mplsXCIsPersistentGroup.setObjects((_B,_T))
if mibBuilder.loadTexts:mplsXCIsPersistentGroup.setStatus(_A)
mplsXCIsNotPersistentGroup=ObjectGroup((1,3,6,1,4,1,2011,5,12,1,3,1,11))
mplsXCIsNotPersistentGroup.setObjects((_B,_T))
if mibBuilder.loadTexts:mplsXCIsNotPersistentGroup.setStatus(_A)
mplsLabelStackGroup=ObjectGroup((1,3,6,1,4,1,2011,5,12,1,3,1,12))
mplsLabelStackGroup.setObjects(*((_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY)))
if mibBuilder.loadTexts:mplsLabelStackGroup.setStatus(_A)
mplsSegmentDiscontinuityGroup=ObjectGroup((1,3,6,1,4,1,2011,5,12,1,3,1,13))
mplsSegmentDiscontinuityGroup.setObjects(*((_B,_AZ),(_B,_Aa)))
if mibBuilder.loadTexts:mplsSegmentDiscontinuityGroup.setStatus(_A)
mplsXCUp=NotificationType((1,3,6,1,4,1,2011,5,12,1,2,0,1))
mplsXCUp.setObjects(*((_B,_K),(_B,_F),(_B,_G),(_B,_H),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:mplsXCUp.setStatus(_A)
mplsXCDown=NotificationType((1,3,6,1,4,1,2011,5,12,1,2,0,2))
mplsXCDown.setObjects(*((_B,_K),(_B,_F),(_B,_G),(_B,_H),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:mplsXCDown.setStatus(_A)
mplsLsrNotificationGroup=NotificationGroup((1,3,6,1,4,1,2011,5,12,1,3,1,14))
mplsLsrNotificationGroup.setObjects(*((_B,'mplsXCUp'),(_B,_Ab)))
if mibBuilder.loadTexts:mplsLsrNotificationGroup.setStatus(_A)
mplsLsrModuleCompliance=ModuleCompliance((1,3,6,1,4,1,2011,5,12,1,3,2,1))
mplsLsrModuleCompliance.setObjects(*((_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am)))
if mibBuilder.loadTexts:mplsLsrModuleCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'MplsLSPID':MplsLSPID,'MplsLabel':MplsLabel,'MplsBitRate':MplsBitRate,'MplsBurstSize':MplsBurstSize,_O:MplsObjectOwner,'hwMplsLsr':hwMplsLsr,'mplsLsrObjects':mplsLsrObjects,'mplsInterfaceConfTable':mplsInterfaceConfTable,'mplsInterfaceConfEntry':mplsInterfaceConfEntry,_X:mplsInterfaceConfIndex,_g:mplsInterfaceLabelMinIn,_h:mplsInterfaceLabelMaxIn,_i:mplsInterfaceLabelMinOut,_j:mplsInterfaceLabelMaxOut,_k:mplsInterfaceTotalBandwidth,_l:mplsInterfaceAvailableBandwidth,_m:mplsInterfaceLabelParticipationType,_n:mplsInterfaceConfStorageType,'mplsInterfacePerfTable':mplsInterfacePerfTable,_d:mplsInterfacePerfEntry,_AI:mplsInterfaceInLabelsUsed,_AJ:mplsInterfaceFailedLabelLookup,_AL:mplsInterfaceOutLabelsUsed,_AK:mplsInterfaceOutFragments,'mplsInSegmentTable':mplsInSegmentTable,'mplsInSegmentEntry':mplsInSegmentEntry,_F:mplsInSegmentIfIndex,_G:mplsInSegmentLabel,_o:mplsInSegmentNPop,_p:mplsInSegmentAddrFamily,_q:mplsInSegmentXCIndex,_r:mplsInSegmentOwner,_u:mplsInSegmentTrafficParamPtr,_s:mplsInSegmentRowStatus,_t:mplsInSegmentStorageType,'mplsInSegmentPerfTable':mplsInSegmentPerfTable,_e:mplsInSegmentPerfEntry,_P:mplsInSegmentOctets,_AF:mplsInSegmentPackets,_AG:mplsInSegmentErrors,_Q:mplsInSegmentDiscards,_AM:mplsInSegmentHCOctets,_AZ:mplsInSegmentPerfDiscontinuityTime,_v:mplsOutSegmentIndexNext,'mplsOutSegmentTable':mplsOutSegmentTable,'mplsOutSegmentEntry':mplsOutSegmentEntry,_H:mplsOutSegmentIndex,_w:mplsOutSegmentIfIndex,_x:mplsOutSegmentPushTopLabel,_y:mplsOutSegmentTopLabel,_z:mplsOutSegmentNextHopIpAddrType,_A0:mplsOutSegmentNextHopIpv4Addr,_A1:mplsOutSegmentNextHopIpv6Addr,_A2:mplsOutSegmentXCIndex,_A3:mplsOutSegmentOwner,_A7:mplsOutSegmentTrafficParamPtr,_A5:mplsOutSegmentRowStatus,_A6:mplsOutSegmentStorageType,'mplsOutSegmentPerfTable':mplsOutSegmentPerfTable,_f:mplsOutSegmentPerfEntry,_R:mplsOutSegmentOctets,_AH:mplsOutSegmentPackets,_A4:mplsOutSegmentErrors,_S:mplsOutSegmentDiscards,_AN:mplsOutSegmentHCOctets,_Aa:mplsOutSegmentPerfDiscontinuityTime,_A8:mplsXCIndexNext,'mplsXCTable':mplsXCTable,'mplsXCEntry':mplsXCEntry,_K:mplsXCIndex,_AE:mplsXCLspId,_A9:mplsXCLabelStackIndex,_T:mplsXCIsPersistent,_AA:mplsXCOwner,_AB:mplsXCRowStatus,_AD:mplsXCStorageType,_L:mplsXCAdminStatus,_M:mplsXCOperStatus,_AX:mplsMaxLabelStackDepth,_AY:mplsLabelStackIndexNext,'mplsLabelStackTable':mplsLabelStackTable,'mplsLabelStackEntry':mplsLabelStackEntry,_Z:mplsLabelStackIndex,_a:mplsLabelStackLabelIndex,_AU:mplsLabelStackLabel,_AV:mplsLabelStackRowStatus,_AW:mplsLabelStackStorageType,_AO:mplsTrafficParamIndexNext,'mplsTrafficParamTable':mplsTrafficParamTable,'mplsTrafficParamEntry':mplsTrafficParamEntry,_b:mplsTrafficParamIndex,_AP:mplsTrafficParamMaxRate,_AQ:mplsTrafficParamMeanRate,_AR:mplsTrafficParamMaxBurstSize,_AS:mplsTrafficParamRowStatus,_AT:mplsTrafficParamStorageType,_AC:mplsXCTrapEnable,'mplsLsrNotifications':mplsLsrNotifications,'mplsLsrNotifyPrefix':mplsLsrNotifyPrefix,'mplsXCUp':mplsXCUp,_Ab:mplsXCDown,'mplsLsrConformance':mplsLsrConformance,'mplsLsrGroups':mplsLsrGroups,_Af:mplsInterfaceGroup,_Ac:mplsInSegmentGroup,_Ad:mplsOutSegmentGroup,_Ae:mplsXCGroup,'mplsXCOptionalGroup':mplsXCOptionalGroup,_Ag:mplsPerfGroup,_Ai:mplsHCInSegmentPerfGroup,_Aj:mplsHCOutSegmentPerfGroup,_Ak:mplsTrafficParamGroup,_Al:mplsXCIsPersistentGroup,_Am:mplsXCIsNotPersistentGroup,'mplsLabelStackGroup':mplsLabelStackGroup,_Ah:mplsSegmentDiscontinuityGroup,'mplsLsrNotificationGroup':mplsLsrNotificationGroup,'mplsLsrCompliances':mplsLsrCompliances,'mplsLsrModuleCompliance':mplsLsrModuleCompliance})