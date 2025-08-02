_An='hpnicfmplsXCIsNotPersistentGroup'
_Am='hpnicfmplsXCIsPersistentGroup'
_Al='hpnicfmplsTrafficParamGroup'
_Ak='hpnicfmplsHCOutSegmentPerfGroup'
_Aj='hpnicfmplsHCInSegmentPerfGroup'
_Ai='hpnicfmplsSegmentDiscontinuityGroup'
_Ah='hpnicfmplsPerfGroup'
_Ag='hpnicfmplsInterfaceGroup'
_Af='hpnicfmplsXCGroup'
_Ae='hpnicfmplsOutSegmentGroup'
_Ad='hpnicfmplsInSegmentGroup'
_Ac='hpnicfmplsXCDown'
_Ab='hpnicfmplsXCUp'
_Aa='hpnicfmplsOutSegmentPerfDiscontinuityTime'
_AZ='hpnicfmplsInSegmentPerfDiscontinuityTime'
_AY='hpnicfmplsLabelStackIndexNext'
_AX='hpnicfmplsMaxLabelStackDepth'
_AW='hpnicfmplsLabelStackStorageType'
_AV='hpnicfmplsLabelStackRowStatus'
_AU='hpnicfmplsLabelStackLabel'
_AT='hpnicfmplsTrafficParamStorageType'
_AS='hpnicfmplsTrafficParamRowStatus'
_AR='hpnicfmplsTrafficParamMaxBurstSize'
_AQ='hpnicfmplsTrafficParamMeanRate'
_AP='hpnicfmplsTrafficParamMaxRate'
_AO='hpnicfmplsTrafficParamIndexNext'
_AN='hpnicfmplsOutSegmentHCOctets'
_AM='hpnicfmplsInSegmentHCOctets'
_AL='hpnicfmplsInterfaceOutLabelsUsed'
_AK='hpnicfmplsInterfaceOutFragments'
_AJ='hpnicfmplsInterfaceFailedLabelLookup'
_AI='hpnicfmplsInterfaceInLabelsUsed'
_AH='hpnicfmplsOutSegmentPackets'
_AG='hpnicfmplsInSegmentErrors'
_AF='hpnicfmplsInSegmentPackets'
_AE='hpnicfmplsXCLspId'
_AD='hpnicfmplsXCStorageType'
_AC='hpnicfmplsXCTrapEnable'
_AB='hpnicfmplsXCRowStatus'
_AA='hpnicfmplsXCOwner'
_A9='hpnicfmplsXCLabelStackIndex'
_A8='hpnicfmplsXCIndexNext'
_A7='hpnicfmplsOutSegmentTrafficParamPtr'
_A6='hpnicfmplsOutSegmentStorageType'
_A5='hpnicfmplsOutSegmentRowStatus'
_A4='hpnicfmplsOutSegmentErrors'
_A3='hpnicfmplsOutSegmentOwner'
_A2='hpnicfmplsOutSegmentXCIndex'
_A1='hpnicfmplsOutSegmentNextHopIpv6Addr'
_A0='hpnicfmplsOutSegmentNextHopIpv4Addr'
_z='hpnicfmplsOutSegmentNextHopIpAddrType'
_y='hpnicfmplsOutSegmentTopLabel'
_x='hpnicfmplsOutSegmentPushTopLabel'
_w='hpnicfmplsOutSegmentIfIndex'
_v='hpnicfmplsOutSegmentIndexNext'
_u='hpnicfmplsInSegmentTrafficParamPtr'
_t='hpnicfmplsInSegmentStorageType'
_s='hpnicfmplsInSegmentRowStatus'
_r='hpnicfmplsInSegmentOwner'
_q='hpnicfmplsInSegmentXCIndex'
_p='hpnicfmplsInSegmentAddrFamily'
_o='hpnicfmplsInSegmentNPop'
_n='hpnicfmplsInterfaceConfStorageType'
_m='hpnicfmplsInterfaceLabelParticipationType'
_l='hpnicfmplsInterfaceAvailableBandwidth'
_k='hpnicfmplsInterfaceTotalBandwidth'
_j='hpnicfmplsInterfaceLabelMaxOut'
_i='hpnicfmplsInterfaceLabelMinOut'
_h='hpnicfmplsInterfaceLabelMaxIn'
_g='hpnicfmplsInterfaceLabelMinIn'
_f='hpnicfmplsOutSegmentPerfEntry'
_e='hpnicfmplsInSegmentPerfEntry'
_d='hpnicfmplsInterfacePerfEntry'
_c='kilobits per second'
_b='hpnicfmplsTrafficParamIndex'
_a='hpnicfmplsLabelStackLabelIndex'
_Z='hpnicfmplsLabelStackIndex'
_Y='testing'
_X='hpnicfmplsInterfaceConfIndex'
_W='unknown'
_V='InetAddressType'
_U='AddressFamilyNumbers'
_T='hpnicfmplsXCIsPersistent'
_S='hpnicfmplsOutSegmentDiscards'
_R='hpnicfmplsOutSegmentOctets'
_Q='hpnicfmplsInSegmentDiscards'
_P='hpnicfmplsInSegmentOctets'
_O='HpnicfMplsObjectOwner'
_N='TruthValue'
_M='hpnicfmplsXCOperStatus'
_L='hpnicfmplsXCAdminStatus'
_K='hpnicfmplsXCIndex'
_J='accessible-for-notify'
_I='not-accessible'
_H='hpnicfmplsOutSegmentIndex'
_G='hpnicfmplsInSegmentLabel'
_F='hpnicfmplsInSegmentIfIndex'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='HPN-ICF-MPLS-LSR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfMpls,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfMpls')
AddressFamilyNumbers,=mibBuilder.importSymbols('IANA-ADDRESS-FAMILY-NUMBERS-MIB',_U)
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddressIPv4,InetAddressIPv6,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6',_V)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowPointer,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','RowStatus','StorageType','TextualConvention','TimeStamp',_N)
hpnicfMplsLsr=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,12,1))
if mibBuilder.loadTexts:hpnicfMplsLsr.setRevisions(('2000-07-12 12:00','2000-07-07 12:00','2000-04-26 12:00','2000-04-21 12:00','2000-03-06 12:00','2000-02-16 12:00','1999-06-16 12:00'))
class HpnicfMplsLSPID(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
class HpnicfMplsLabel(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class HpnicfMplsBitRate(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class HpnicfMplsBurstSize(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class HpnicfMplsObjectOwner(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('other',1),('snmp',2),('ldp',3),('rsvp',4),('crldp',5),('policyAgent',6),(_W,7)))
_HpnicfmplsLsrObjects_ObjectIdentity=ObjectIdentity
hpnicfmplsLsrObjects=_HpnicfmplsLsrObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1))
_HpnicfmplsInterfaceConfTable_Object=MibTable
hpnicfmplsInterfaceConfTable=_HpnicfmplsInterfaceConfTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,1))
if mibBuilder.loadTexts:hpnicfmplsInterfaceConfTable.setStatus(_A)
_HpnicfmplsInterfaceConfEntry_Object=MibTableRow
hpnicfmplsInterfaceConfEntry=_HpnicfmplsInterfaceConfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,1,1))
hpnicfmplsInterfaceConfEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:hpnicfmplsInterfaceConfEntry.setStatus(_A)
_HpnicfmplsInterfaceConfIndex_Type=InterfaceIndexOrZero
_HpnicfmplsInterfaceConfIndex_Object=MibTableColumn
hpnicfmplsInterfaceConfIndex=_HpnicfmplsInterfaceConfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,1,1,1),_HpnicfmplsInterfaceConfIndex_Type())
hpnicfmplsInterfaceConfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfmplsInterfaceConfIndex.setStatus(_A)
_HpnicfmplsInterfaceLabelMinIn_Type=HpnicfMplsLabel
_HpnicfmplsInterfaceLabelMinIn_Object=MibTableColumn
hpnicfmplsInterfaceLabelMinIn=_HpnicfmplsInterfaceLabelMinIn_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,1,1,2),_HpnicfmplsInterfaceLabelMinIn_Type())
hpnicfmplsInterfaceLabelMinIn.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsInterfaceLabelMinIn.setStatus(_A)
_HpnicfmplsInterfaceLabelMaxIn_Type=HpnicfMplsLabel
_HpnicfmplsInterfaceLabelMaxIn_Object=MibTableColumn
hpnicfmplsInterfaceLabelMaxIn=_HpnicfmplsInterfaceLabelMaxIn_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,1,1,3),_HpnicfmplsInterfaceLabelMaxIn_Type())
hpnicfmplsInterfaceLabelMaxIn.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsInterfaceLabelMaxIn.setStatus(_A)
_HpnicfmplsInterfaceLabelMinOut_Type=HpnicfMplsLabel
_HpnicfmplsInterfaceLabelMinOut_Object=MibTableColumn
hpnicfmplsInterfaceLabelMinOut=_HpnicfmplsInterfaceLabelMinOut_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,1,1,4),_HpnicfmplsInterfaceLabelMinOut_Type())
hpnicfmplsInterfaceLabelMinOut.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsInterfaceLabelMinOut.setStatus(_A)
_HpnicfmplsInterfaceLabelMaxOut_Type=HpnicfMplsLabel
_HpnicfmplsInterfaceLabelMaxOut_Object=MibTableColumn
hpnicfmplsInterfaceLabelMaxOut=_HpnicfmplsInterfaceLabelMaxOut_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,1,1,5),_HpnicfmplsInterfaceLabelMaxOut_Type())
hpnicfmplsInterfaceLabelMaxOut.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsInterfaceLabelMaxOut.setStatus(_A)
_HpnicfmplsInterfaceTotalBandwidth_Type=HpnicfMplsBitRate
_HpnicfmplsInterfaceTotalBandwidth_Object=MibTableColumn
hpnicfmplsInterfaceTotalBandwidth=_HpnicfmplsInterfaceTotalBandwidth_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,1,1,6),_HpnicfmplsInterfaceTotalBandwidth_Type())
hpnicfmplsInterfaceTotalBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsInterfaceTotalBandwidth.setStatus(_A)
_HpnicfmplsInterfaceAvailableBandwidth_Type=HpnicfMplsBitRate
_HpnicfmplsInterfaceAvailableBandwidth_Object=MibTableColumn
hpnicfmplsInterfaceAvailableBandwidth=_HpnicfmplsInterfaceAvailableBandwidth_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,1,1,7),_HpnicfmplsInterfaceAvailableBandwidth_Type())
hpnicfmplsInterfaceAvailableBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsInterfaceAvailableBandwidth.setStatus(_A)
class _HpnicfmplsInterfaceLabelParticipationType_Type(Bits):namedValues=NamedValues(*(('perPlatform',0),('perInterface',1)))
_HpnicfmplsInterfaceLabelParticipationType_Type.__name__='Bits'
_HpnicfmplsInterfaceLabelParticipationType_Object=MibTableColumn
hpnicfmplsInterfaceLabelParticipationType=_HpnicfmplsInterfaceLabelParticipationType_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,1,1,8),_HpnicfmplsInterfaceLabelParticipationType_Type())
hpnicfmplsInterfaceLabelParticipationType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsInterfaceLabelParticipationType.setStatus(_A)
_HpnicfmplsInterfaceConfStorageType_Type=StorageType
_HpnicfmplsInterfaceConfStorageType_Object=MibTableColumn
hpnicfmplsInterfaceConfStorageType=_HpnicfmplsInterfaceConfStorageType_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,1,1,9),_HpnicfmplsInterfaceConfStorageType_Type())
hpnicfmplsInterfaceConfStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsInterfaceConfStorageType.setStatus(_A)
_HpnicfmplsInterfacePerfTable_Object=MibTable
hpnicfmplsInterfacePerfTable=_HpnicfmplsInterfacePerfTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,2))
if mibBuilder.loadTexts:hpnicfmplsInterfacePerfTable.setStatus(_A)
_HpnicfmplsInterfacePerfEntry_Object=MibTableRow
hpnicfmplsInterfacePerfEntry=_HpnicfmplsInterfacePerfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,2,1))
if mibBuilder.loadTexts:hpnicfmplsInterfacePerfEntry.setStatus(_A)
_HpnicfmplsInterfaceInLabelsUsed_Type=Gauge32
_HpnicfmplsInterfaceInLabelsUsed_Object=MibTableColumn
hpnicfmplsInterfaceInLabelsUsed=_HpnicfmplsInterfaceInLabelsUsed_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,2,1,1),_HpnicfmplsInterfaceInLabelsUsed_Type())
hpnicfmplsInterfaceInLabelsUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsInterfaceInLabelsUsed.setStatus(_A)
_HpnicfmplsInterfaceFailedLabelLookup_Type=Counter32
_HpnicfmplsInterfaceFailedLabelLookup_Object=MibTableColumn
hpnicfmplsInterfaceFailedLabelLookup=_HpnicfmplsInterfaceFailedLabelLookup_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,2,1,2),_HpnicfmplsInterfaceFailedLabelLookup_Type())
hpnicfmplsInterfaceFailedLabelLookup.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsInterfaceFailedLabelLookup.setStatus(_A)
_HpnicfmplsInterfaceOutLabelsUsed_Type=Gauge32
_HpnicfmplsInterfaceOutLabelsUsed_Object=MibTableColumn
hpnicfmplsInterfaceOutLabelsUsed=_HpnicfmplsInterfaceOutLabelsUsed_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,2,1,3),_HpnicfmplsInterfaceOutLabelsUsed_Type())
hpnicfmplsInterfaceOutLabelsUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsInterfaceOutLabelsUsed.setStatus(_A)
_HpnicfmplsInterfaceOutFragments_Type=Counter32
_HpnicfmplsInterfaceOutFragments_Object=MibTableColumn
hpnicfmplsInterfaceOutFragments=_HpnicfmplsInterfaceOutFragments_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,2,1,4),_HpnicfmplsInterfaceOutFragments_Type())
hpnicfmplsInterfaceOutFragments.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsInterfaceOutFragments.setStatus(_A)
_HpnicfmplsInSegmentTable_Object=MibTable
hpnicfmplsInSegmentTable=_HpnicfmplsInSegmentTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,3))
if mibBuilder.loadTexts:hpnicfmplsInSegmentTable.setStatus(_A)
_HpnicfmplsInSegmentEntry_Object=MibTableRow
hpnicfmplsInSegmentEntry=_HpnicfmplsInSegmentEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,3,1))
hpnicfmplsInSegmentEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfmplsInSegmentEntry.setStatus(_A)
_HpnicfmplsInSegmentIfIndex_Type=InterfaceIndexOrZero
_HpnicfmplsInSegmentIfIndex_Object=MibTableColumn
hpnicfmplsInSegmentIfIndex=_HpnicfmplsInSegmentIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,3,1,1),_HpnicfmplsInSegmentIfIndex_Type())
hpnicfmplsInSegmentIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfmplsInSegmentIfIndex.setStatus(_A)
_HpnicfmplsInSegmentLabel_Type=HpnicfMplsLabel
_HpnicfmplsInSegmentLabel_Object=MibTableColumn
hpnicfmplsInSegmentLabel=_HpnicfmplsInSegmentLabel_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,3,1,2),_HpnicfmplsInSegmentLabel_Type())
hpnicfmplsInSegmentLabel.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfmplsInSegmentLabel.setStatus(_A)
class _HpnicfmplsInSegmentNPop_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfmplsInSegmentNPop_Type.__name__=_E
_HpnicfmplsInSegmentNPop_Object=MibTableColumn
hpnicfmplsInSegmentNPop=_HpnicfmplsInSegmentNPop_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,3,1,3),_HpnicfmplsInSegmentNPop_Type())
hpnicfmplsInSegmentNPop.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsInSegmentNPop.setStatus(_A)
class _HpnicfmplsInSegmentAddrFamily_Type(AddressFamilyNumbers):defaultValue=0
_HpnicfmplsInSegmentAddrFamily_Type.__name__=_U
_HpnicfmplsInSegmentAddrFamily_Object=MibTableColumn
hpnicfmplsInSegmentAddrFamily=_HpnicfmplsInSegmentAddrFamily_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,3,1,4),_HpnicfmplsInSegmentAddrFamily_Type())
hpnicfmplsInSegmentAddrFamily.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsInSegmentAddrFamily.setStatus(_A)
class _HpnicfmplsInSegmentXCIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfmplsInSegmentXCIndex_Type.__name__=_E
_HpnicfmplsInSegmentXCIndex_Object=MibTableColumn
hpnicfmplsInSegmentXCIndex=_HpnicfmplsInSegmentXCIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,3,1,5),_HpnicfmplsInSegmentXCIndex_Type())
hpnicfmplsInSegmentXCIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsInSegmentXCIndex.setStatus(_A)
class _HpnicfmplsInSegmentOwner_Type(HpnicfMplsObjectOwner):defaultValue=7
_HpnicfmplsInSegmentOwner_Type.__name__=_O
_HpnicfmplsInSegmentOwner_Object=MibTableColumn
hpnicfmplsInSegmentOwner=_HpnicfmplsInSegmentOwner_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,3,1,6),_HpnicfmplsInSegmentOwner_Type())
hpnicfmplsInSegmentOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsInSegmentOwner.setStatus(_A)
_HpnicfmplsInSegmentTrafficParamPtr_Type=RowPointer
_HpnicfmplsInSegmentTrafficParamPtr_Object=MibTableColumn
hpnicfmplsInSegmentTrafficParamPtr=_HpnicfmplsInSegmentTrafficParamPtr_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,3,1,7),_HpnicfmplsInSegmentTrafficParamPtr_Type())
hpnicfmplsInSegmentTrafficParamPtr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsInSegmentTrafficParamPtr.setStatus(_A)
_HpnicfmplsInSegmentRowStatus_Type=RowStatus
_HpnicfmplsInSegmentRowStatus_Object=MibTableColumn
hpnicfmplsInSegmentRowStatus=_HpnicfmplsInSegmentRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,3,1,8),_HpnicfmplsInSegmentRowStatus_Type())
hpnicfmplsInSegmentRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsInSegmentRowStatus.setStatus(_A)
_HpnicfmplsInSegmentStorageType_Type=StorageType
_HpnicfmplsInSegmentStorageType_Object=MibTableColumn
hpnicfmplsInSegmentStorageType=_HpnicfmplsInSegmentStorageType_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,3,1,9),_HpnicfmplsInSegmentStorageType_Type())
hpnicfmplsInSegmentStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsInSegmentStorageType.setStatus(_A)
_HpnicfmplsInSegmentPerfTable_Object=MibTable
hpnicfmplsInSegmentPerfTable=_HpnicfmplsInSegmentPerfTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,4))
if mibBuilder.loadTexts:hpnicfmplsInSegmentPerfTable.setStatus(_A)
_HpnicfmplsInSegmentPerfEntry_Object=MibTableRow
hpnicfmplsInSegmentPerfEntry=_HpnicfmplsInSegmentPerfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,4,1))
if mibBuilder.loadTexts:hpnicfmplsInSegmentPerfEntry.setStatus(_A)
_HpnicfmplsInSegmentOctets_Type=Counter32
_HpnicfmplsInSegmentOctets_Object=MibTableColumn
hpnicfmplsInSegmentOctets=_HpnicfmplsInSegmentOctets_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,4,1,1),_HpnicfmplsInSegmentOctets_Type())
hpnicfmplsInSegmentOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsInSegmentOctets.setStatus(_A)
_HpnicfmplsInSegmentPackets_Type=Counter32
_HpnicfmplsInSegmentPackets_Object=MibTableColumn
hpnicfmplsInSegmentPackets=_HpnicfmplsInSegmentPackets_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,4,1,2),_HpnicfmplsInSegmentPackets_Type())
hpnicfmplsInSegmentPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsInSegmentPackets.setStatus(_A)
_HpnicfmplsInSegmentErrors_Type=Counter32
_HpnicfmplsInSegmentErrors_Object=MibTableColumn
hpnicfmplsInSegmentErrors=_HpnicfmplsInSegmentErrors_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,4,1,3),_HpnicfmplsInSegmentErrors_Type())
hpnicfmplsInSegmentErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsInSegmentErrors.setStatus(_A)
_HpnicfmplsInSegmentDiscards_Type=Counter32
_HpnicfmplsInSegmentDiscards_Object=MibTableColumn
hpnicfmplsInSegmentDiscards=_HpnicfmplsInSegmentDiscards_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,4,1,4),_HpnicfmplsInSegmentDiscards_Type())
hpnicfmplsInSegmentDiscards.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsInSegmentDiscards.setStatus(_A)
_HpnicfmplsInSegmentHCOctets_Type=Counter64
_HpnicfmplsInSegmentHCOctets_Object=MibTableColumn
hpnicfmplsInSegmentHCOctets=_HpnicfmplsInSegmentHCOctets_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,4,1,5),_HpnicfmplsInSegmentHCOctets_Type())
hpnicfmplsInSegmentHCOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsInSegmentHCOctets.setStatus(_A)
_HpnicfmplsInSegmentPerfDiscontinuityTime_Type=TimeStamp
_HpnicfmplsInSegmentPerfDiscontinuityTime_Object=MibTableColumn
hpnicfmplsInSegmentPerfDiscontinuityTime=_HpnicfmplsInSegmentPerfDiscontinuityTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,4,1,6),_HpnicfmplsInSegmentPerfDiscontinuityTime_Type())
hpnicfmplsInSegmentPerfDiscontinuityTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsInSegmentPerfDiscontinuityTime.setStatus(_A)
class _HpnicfmplsOutSegmentIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfmplsOutSegmentIndexNext_Type.__name__=_E
_HpnicfmplsOutSegmentIndexNext_Object=MibScalar
hpnicfmplsOutSegmentIndexNext=_HpnicfmplsOutSegmentIndexNext_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,5),_HpnicfmplsOutSegmentIndexNext_Type())
hpnicfmplsOutSegmentIndexNext.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsOutSegmentIndexNext.setStatus(_A)
_HpnicfmplsOutSegmentTable_Object=MibTable
hpnicfmplsOutSegmentTable=_HpnicfmplsOutSegmentTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,6))
if mibBuilder.loadTexts:hpnicfmplsOutSegmentTable.setStatus(_A)
_HpnicfmplsOutSegmentEntry_Object=MibTableRow
hpnicfmplsOutSegmentEntry=_HpnicfmplsOutSegmentEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,6,1))
hpnicfmplsOutSegmentEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpnicfmplsOutSegmentEntry.setStatus(_A)
class _HpnicfmplsOutSegmentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfmplsOutSegmentIndex_Type.__name__=_E
_HpnicfmplsOutSegmentIndex_Object=MibTableColumn
hpnicfmplsOutSegmentIndex=_HpnicfmplsOutSegmentIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,6,1,1),_HpnicfmplsOutSegmentIndex_Type())
hpnicfmplsOutSegmentIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfmplsOutSegmentIndex.setStatus(_A)
_HpnicfmplsOutSegmentIfIndex_Type=InterfaceIndex
_HpnicfmplsOutSegmentIfIndex_Object=MibTableColumn
hpnicfmplsOutSegmentIfIndex=_HpnicfmplsOutSegmentIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,6,1,2),_HpnicfmplsOutSegmentIfIndex_Type())
hpnicfmplsOutSegmentIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsOutSegmentIfIndex.setStatus(_A)
_HpnicfmplsOutSegmentPushTopLabel_Type=TruthValue
_HpnicfmplsOutSegmentPushTopLabel_Object=MibTableColumn
hpnicfmplsOutSegmentPushTopLabel=_HpnicfmplsOutSegmentPushTopLabel_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,6,1,3),_HpnicfmplsOutSegmentPushTopLabel_Type())
hpnicfmplsOutSegmentPushTopLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsOutSegmentPushTopLabel.setStatus(_A)
_HpnicfmplsOutSegmentTopLabel_Type=HpnicfMplsLabel
_HpnicfmplsOutSegmentTopLabel_Object=MibTableColumn
hpnicfmplsOutSegmentTopLabel=_HpnicfmplsOutSegmentTopLabel_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,6,1,4),_HpnicfmplsOutSegmentTopLabel_Type())
hpnicfmplsOutSegmentTopLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsOutSegmentTopLabel.setStatus(_A)
class _HpnicfmplsOutSegmentNextHopIpAddrType_Type(InetAddressType):defaultValue=0
_HpnicfmplsOutSegmentNextHopIpAddrType_Type.__name__=_V
_HpnicfmplsOutSegmentNextHopIpAddrType_Object=MibTableColumn
hpnicfmplsOutSegmentNextHopIpAddrType=_HpnicfmplsOutSegmentNextHopIpAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,6,1,5),_HpnicfmplsOutSegmentNextHopIpAddrType_Type())
hpnicfmplsOutSegmentNextHopIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsOutSegmentNextHopIpAddrType.setStatus(_A)
_HpnicfmplsOutSegmentNextHopIpv4Addr_Type=InetAddressIPv4
_HpnicfmplsOutSegmentNextHopIpv4Addr_Object=MibTableColumn
hpnicfmplsOutSegmentNextHopIpv4Addr=_HpnicfmplsOutSegmentNextHopIpv4Addr_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,6,1,6),_HpnicfmplsOutSegmentNextHopIpv4Addr_Type())
hpnicfmplsOutSegmentNextHopIpv4Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsOutSegmentNextHopIpv4Addr.setStatus(_A)
_HpnicfmplsOutSegmentNextHopIpv6Addr_Type=InetAddressIPv6
_HpnicfmplsOutSegmentNextHopIpv6Addr_Object=MibTableColumn
hpnicfmplsOutSegmentNextHopIpv6Addr=_HpnicfmplsOutSegmentNextHopIpv6Addr_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,6,1,7),_HpnicfmplsOutSegmentNextHopIpv6Addr_Type())
hpnicfmplsOutSegmentNextHopIpv6Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsOutSegmentNextHopIpv6Addr.setStatus(_A)
class _HpnicfmplsOutSegmentXCIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfmplsOutSegmentXCIndex_Type.__name__=_E
_HpnicfmplsOutSegmentXCIndex_Object=MibTableColumn
hpnicfmplsOutSegmentXCIndex=_HpnicfmplsOutSegmentXCIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,6,1,8),_HpnicfmplsOutSegmentXCIndex_Type())
hpnicfmplsOutSegmentXCIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsOutSegmentXCIndex.setStatus(_A)
class _HpnicfmplsOutSegmentOwner_Type(HpnicfMplsObjectOwner):defaultValue=7
_HpnicfmplsOutSegmentOwner_Type.__name__=_O
_HpnicfmplsOutSegmentOwner_Object=MibTableColumn
hpnicfmplsOutSegmentOwner=_HpnicfmplsOutSegmentOwner_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,6,1,9),_HpnicfmplsOutSegmentOwner_Type())
hpnicfmplsOutSegmentOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsOutSegmentOwner.setStatus(_A)
_HpnicfmplsOutSegmentTrafficParamPtr_Type=RowPointer
_HpnicfmplsOutSegmentTrafficParamPtr_Object=MibTableColumn
hpnicfmplsOutSegmentTrafficParamPtr=_HpnicfmplsOutSegmentTrafficParamPtr_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,6,1,10),_HpnicfmplsOutSegmentTrafficParamPtr_Type())
hpnicfmplsOutSegmentTrafficParamPtr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsOutSegmentTrafficParamPtr.setStatus(_A)
_HpnicfmplsOutSegmentRowStatus_Type=RowStatus
_HpnicfmplsOutSegmentRowStatus_Object=MibTableColumn
hpnicfmplsOutSegmentRowStatus=_HpnicfmplsOutSegmentRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,6,1,11),_HpnicfmplsOutSegmentRowStatus_Type())
hpnicfmplsOutSegmentRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsOutSegmentRowStatus.setStatus(_A)
_HpnicfmplsOutSegmentStorageType_Type=StorageType
_HpnicfmplsOutSegmentStorageType_Object=MibTableColumn
hpnicfmplsOutSegmentStorageType=_HpnicfmplsOutSegmentStorageType_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,6,1,12),_HpnicfmplsOutSegmentStorageType_Type())
hpnicfmplsOutSegmentStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsOutSegmentStorageType.setStatus(_A)
_HpnicfmplsOutSegmentPerfTable_Object=MibTable
hpnicfmplsOutSegmentPerfTable=_HpnicfmplsOutSegmentPerfTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,7))
if mibBuilder.loadTexts:hpnicfmplsOutSegmentPerfTable.setStatus(_A)
_HpnicfmplsOutSegmentPerfEntry_Object=MibTableRow
hpnicfmplsOutSegmentPerfEntry=_HpnicfmplsOutSegmentPerfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,7,1))
if mibBuilder.loadTexts:hpnicfmplsOutSegmentPerfEntry.setStatus(_A)
_HpnicfmplsOutSegmentOctets_Type=Counter32
_HpnicfmplsOutSegmentOctets_Object=MibTableColumn
hpnicfmplsOutSegmentOctets=_HpnicfmplsOutSegmentOctets_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,7,1,1),_HpnicfmplsOutSegmentOctets_Type())
hpnicfmplsOutSegmentOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsOutSegmentOctets.setStatus(_A)
_HpnicfmplsOutSegmentPackets_Type=Counter32
_HpnicfmplsOutSegmentPackets_Object=MibTableColumn
hpnicfmplsOutSegmentPackets=_HpnicfmplsOutSegmentPackets_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,7,1,2),_HpnicfmplsOutSegmentPackets_Type())
hpnicfmplsOutSegmentPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsOutSegmentPackets.setStatus(_A)
_HpnicfmplsOutSegmentErrors_Type=Counter32
_HpnicfmplsOutSegmentErrors_Object=MibTableColumn
hpnicfmplsOutSegmentErrors=_HpnicfmplsOutSegmentErrors_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,7,1,3),_HpnicfmplsOutSegmentErrors_Type())
hpnicfmplsOutSegmentErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsOutSegmentErrors.setStatus(_A)
_HpnicfmplsOutSegmentDiscards_Type=Counter32
_HpnicfmplsOutSegmentDiscards_Object=MibTableColumn
hpnicfmplsOutSegmentDiscards=_HpnicfmplsOutSegmentDiscards_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,7,1,4),_HpnicfmplsOutSegmentDiscards_Type())
hpnicfmplsOutSegmentDiscards.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsOutSegmentDiscards.setStatus(_A)
_HpnicfmplsOutSegmentHCOctets_Type=Counter64
_HpnicfmplsOutSegmentHCOctets_Object=MibTableColumn
hpnicfmplsOutSegmentHCOctets=_HpnicfmplsOutSegmentHCOctets_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,7,1,5),_HpnicfmplsOutSegmentHCOctets_Type())
hpnicfmplsOutSegmentHCOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsOutSegmentHCOctets.setStatus(_A)
_HpnicfmplsOutSegmentPerfDiscontinuityTime_Type=TimeStamp
_HpnicfmplsOutSegmentPerfDiscontinuityTime_Object=MibTableColumn
hpnicfmplsOutSegmentPerfDiscontinuityTime=_HpnicfmplsOutSegmentPerfDiscontinuityTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,7,1,6),_HpnicfmplsOutSegmentPerfDiscontinuityTime_Type())
hpnicfmplsOutSegmentPerfDiscontinuityTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsOutSegmentPerfDiscontinuityTime.setStatus(_A)
class _HpnicfmplsXCIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfmplsXCIndexNext_Type.__name__=_E
_HpnicfmplsXCIndexNext_Object=MibScalar
hpnicfmplsXCIndexNext=_HpnicfmplsXCIndexNext_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,8),_HpnicfmplsXCIndexNext_Type())
hpnicfmplsXCIndexNext.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsXCIndexNext.setStatus(_A)
_HpnicfmplsXCTable_Object=MibTable
hpnicfmplsXCTable=_HpnicfmplsXCTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,9))
if mibBuilder.loadTexts:hpnicfmplsXCTable.setStatus(_A)
_HpnicfmplsXCEntry_Object=MibTableRow
hpnicfmplsXCEntry=_HpnicfmplsXCEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,9,1))
hpnicfmplsXCEntry.setIndexNames((0,_B,_K),(0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:hpnicfmplsXCEntry.setStatus(_A)
class _HpnicfmplsXCIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfmplsXCIndex_Type.__name__=_E
_HpnicfmplsXCIndex_Object=MibTableColumn
hpnicfmplsXCIndex=_HpnicfmplsXCIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,9,1,1),_HpnicfmplsXCIndex_Type())
hpnicfmplsXCIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfmplsXCIndex.setStatus(_A)
_HpnicfmplsXCLspId_Type=HpnicfMplsLSPID
_HpnicfmplsXCLspId_Object=MibTableColumn
hpnicfmplsXCLspId=_HpnicfmplsXCLspId_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,9,1,2),_HpnicfmplsXCLspId_Type())
hpnicfmplsXCLspId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsXCLspId.setStatus(_A)
class _HpnicfmplsXCLabelStackIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfmplsXCLabelStackIndex_Type.__name__=_E
_HpnicfmplsXCLabelStackIndex_Object=MibTableColumn
hpnicfmplsXCLabelStackIndex=_HpnicfmplsXCLabelStackIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,9,1,3),_HpnicfmplsXCLabelStackIndex_Type())
hpnicfmplsXCLabelStackIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsXCLabelStackIndex.setStatus(_A)
class _HpnicfmplsXCIsPersistent_Type(TruthValue):defaultValue=2
_HpnicfmplsXCIsPersistent_Type.__name__=_N
_HpnicfmplsXCIsPersistent_Object=MibTableColumn
hpnicfmplsXCIsPersistent=_HpnicfmplsXCIsPersistent_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,9,1,4),_HpnicfmplsXCIsPersistent_Type())
hpnicfmplsXCIsPersistent.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsXCIsPersistent.setStatus(_A)
_HpnicfmplsXCOwner_Type=HpnicfMplsObjectOwner
_HpnicfmplsXCOwner_Object=MibTableColumn
hpnicfmplsXCOwner=_HpnicfmplsXCOwner_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,9,1,5),_HpnicfmplsXCOwner_Type())
hpnicfmplsXCOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsXCOwner.setStatus(_A)
_HpnicfmplsXCRowStatus_Type=RowStatus
_HpnicfmplsXCRowStatus_Object=MibTableColumn
hpnicfmplsXCRowStatus=_HpnicfmplsXCRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,9,1,6),_HpnicfmplsXCRowStatus_Type())
hpnicfmplsXCRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsXCRowStatus.setStatus(_A)
_HpnicfmplsXCStorageType_Type=StorageType
_HpnicfmplsXCStorageType_Object=MibTableColumn
hpnicfmplsXCStorageType=_HpnicfmplsXCStorageType_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,9,1,7),_HpnicfmplsXCStorageType_Type())
hpnicfmplsXCStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsXCStorageType.setStatus(_A)
class _HpnicfmplsXCAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_Y,3)))
_HpnicfmplsXCAdminStatus_Type.__name__=_E
_HpnicfmplsXCAdminStatus_Object=MibTableColumn
hpnicfmplsXCAdminStatus=_HpnicfmplsXCAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,9,1,8),_HpnicfmplsXCAdminStatus_Type())
hpnicfmplsXCAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsXCAdminStatus.setStatus(_A)
class _HpnicfmplsXCOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('up',1),('down',2),(_Y,3),(_W,4),('dormant',5),('notPresent',6),('lowerLayerDown',7)))
_HpnicfmplsXCOperStatus_Type.__name__=_E
_HpnicfmplsXCOperStatus_Object=MibTableColumn
hpnicfmplsXCOperStatus=_HpnicfmplsXCOperStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,9,1,9),_HpnicfmplsXCOperStatus_Type())
hpnicfmplsXCOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsXCOperStatus.setStatus(_A)
class _HpnicfmplsMaxLabelStackDepth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfmplsMaxLabelStackDepth_Type.__name__=_E
_HpnicfmplsMaxLabelStackDepth_Object=MibScalar
hpnicfmplsMaxLabelStackDepth=_HpnicfmplsMaxLabelStackDepth_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,10),_HpnicfmplsMaxLabelStackDepth_Type())
hpnicfmplsMaxLabelStackDepth.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsMaxLabelStackDepth.setStatus(_A)
class _HpnicfmplsLabelStackIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfmplsLabelStackIndexNext_Type.__name__=_E
_HpnicfmplsLabelStackIndexNext_Object=MibScalar
hpnicfmplsLabelStackIndexNext=_HpnicfmplsLabelStackIndexNext_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,11),_HpnicfmplsLabelStackIndexNext_Type())
hpnicfmplsLabelStackIndexNext.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsLabelStackIndexNext.setStatus(_A)
_HpnicfmplsLabelStackTable_Object=MibTable
hpnicfmplsLabelStackTable=_HpnicfmplsLabelStackTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,12))
if mibBuilder.loadTexts:hpnicfmplsLabelStackTable.setStatus(_A)
_HpnicfmplsLabelStackEntry_Object=MibTableRow
hpnicfmplsLabelStackEntry=_HpnicfmplsLabelStackEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,12,1))
hpnicfmplsLabelStackEntry.setIndexNames((0,_B,_Z),(0,_B,_a))
if mibBuilder.loadTexts:hpnicfmplsLabelStackEntry.setStatus(_A)
class _HpnicfmplsLabelStackIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfmplsLabelStackIndex_Type.__name__=_E
_HpnicfmplsLabelStackIndex_Object=MibTableColumn
hpnicfmplsLabelStackIndex=_HpnicfmplsLabelStackIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,12,1,1),_HpnicfmplsLabelStackIndex_Type())
hpnicfmplsLabelStackIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfmplsLabelStackIndex.setStatus(_A)
class _HpnicfmplsLabelStackLabelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfmplsLabelStackLabelIndex_Type.__name__=_E
_HpnicfmplsLabelStackLabelIndex_Object=MibTableColumn
hpnicfmplsLabelStackLabelIndex=_HpnicfmplsLabelStackLabelIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,12,1,2),_HpnicfmplsLabelStackLabelIndex_Type())
hpnicfmplsLabelStackLabelIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfmplsLabelStackLabelIndex.setStatus(_A)
_HpnicfmplsLabelStackLabel_Type=HpnicfMplsLabel
_HpnicfmplsLabelStackLabel_Object=MibTableColumn
hpnicfmplsLabelStackLabel=_HpnicfmplsLabelStackLabel_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,12,1,3),_HpnicfmplsLabelStackLabel_Type())
hpnicfmplsLabelStackLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsLabelStackLabel.setStatus(_A)
_HpnicfmplsLabelStackRowStatus_Type=RowStatus
_HpnicfmplsLabelStackRowStatus_Object=MibTableColumn
hpnicfmplsLabelStackRowStatus=_HpnicfmplsLabelStackRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,12,1,4),_HpnicfmplsLabelStackRowStatus_Type())
hpnicfmplsLabelStackRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsLabelStackRowStatus.setStatus(_A)
_HpnicfmplsLabelStackStorageType_Type=StorageType
_HpnicfmplsLabelStackStorageType_Object=MibTableColumn
hpnicfmplsLabelStackStorageType=_HpnicfmplsLabelStackStorageType_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,12,1,5),_HpnicfmplsLabelStackStorageType_Type())
hpnicfmplsLabelStackStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsLabelStackStorageType.setStatus(_A)
class _HpnicfmplsTrafficParamIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfmplsTrafficParamIndexNext_Type.__name__=_E
_HpnicfmplsTrafficParamIndexNext_Object=MibScalar
hpnicfmplsTrafficParamIndexNext=_HpnicfmplsTrafficParamIndexNext_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,13),_HpnicfmplsTrafficParamIndexNext_Type())
hpnicfmplsTrafficParamIndexNext.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfmplsTrafficParamIndexNext.setStatus(_A)
_HpnicfmplsTrafficParamTable_Object=MibTable
hpnicfmplsTrafficParamTable=_HpnicfmplsTrafficParamTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,14))
if mibBuilder.loadTexts:hpnicfmplsTrafficParamTable.setStatus(_A)
_HpnicfmplsTrafficParamEntry_Object=MibTableRow
hpnicfmplsTrafficParamEntry=_HpnicfmplsTrafficParamEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,14,1))
hpnicfmplsTrafficParamEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:hpnicfmplsTrafficParamEntry.setStatus(_A)
class _HpnicfmplsTrafficParamIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfmplsTrafficParamIndex_Type.__name__=_E
_HpnicfmplsTrafficParamIndex_Object=MibTableColumn
hpnicfmplsTrafficParamIndex=_HpnicfmplsTrafficParamIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,14,1,1),_HpnicfmplsTrafficParamIndex_Type())
hpnicfmplsTrafficParamIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfmplsTrafficParamIndex.setStatus(_A)
_HpnicfmplsTrafficParamMaxRate_Type=HpnicfMplsBitRate
_HpnicfmplsTrafficParamMaxRate_Object=MibTableColumn
hpnicfmplsTrafficParamMaxRate=_HpnicfmplsTrafficParamMaxRate_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,14,1,2),_HpnicfmplsTrafficParamMaxRate_Type())
hpnicfmplsTrafficParamMaxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsTrafficParamMaxRate.setStatus(_A)
if mibBuilder.loadTexts:hpnicfmplsTrafficParamMaxRate.setUnits(_c)
_HpnicfmplsTrafficParamMeanRate_Type=HpnicfMplsBitRate
_HpnicfmplsTrafficParamMeanRate_Object=MibTableColumn
hpnicfmplsTrafficParamMeanRate=_HpnicfmplsTrafficParamMeanRate_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,14,1,3),_HpnicfmplsTrafficParamMeanRate_Type())
hpnicfmplsTrafficParamMeanRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsTrafficParamMeanRate.setStatus(_A)
if mibBuilder.loadTexts:hpnicfmplsTrafficParamMeanRate.setUnits(_c)
_HpnicfmplsTrafficParamMaxBurstSize_Type=HpnicfMplsBurstSize
_HpnicfmplsTrafficParamMaxBurstSize_Object=MibTableColumn
hpnicfmplsTrafficParamMaxBurstSize=_HpnicfmplsTrafficParamMaxBurstSize_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,14,1,4),_HpnicfmplsTrafficParamMaxBurstSize_Type())
hpnicfmplsTrafficParamMaxBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsTrafficParamMaxBurstSize.setStatus(_A)
if mibBuilder.loadTexts:hpnicfmplsTrafficParamMaxBurstSize.setUnits('bytes')
_HpnicfmplsTrafficParamRowStatus_Type=RowStatus
_HpnicfmplsTrafficParamRowStatus_Object=MibTableColumn
hpnicfmplsTrafficParamRowStatus=_HpnicfmplsTrafficParamRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,14,1,5),_HpnicfmplsTrafficParamRowStatus_Type())
hpnicfmplsTrafficParamRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsTrafficParamRowStatus.setStatus(_A)
_HpnicfmplsTrafficParamStorageType_Type=StorageType
_HpnicfmplsTrafficParamStorageType_Object=MibTableColumn
hpnicfmplsTrafficParamStorageType=_HpnicfmplsTrafficParamStorageType_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,14,1,6),_HpnicfmplsTrafficParamStorageType_Type())
hpnicfmplsTrafficParamStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsTrafficParamStorageType.setStatus(_A)
class _HpnicfmplsXCTrapEnable_Type(TruthValue):defaultValue=2
_HpnicfmplsXCTrapEnable_Type.__name__=_N
_HpnicfmplsXCTrapEnable_Object=MibScalar
hpnicfmplsXCTrapEnable=_HpnicfmplsXCTrapEnable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,1,1,15),_HpnicfmplsXCTrapEnable_Type())
hpnicfmplsXCTrapEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfmplsXCTrapEnable.setStatus(_A)
_HpnicfmplsLsrNotifications_ObjectIdentity=ObjectIdentity
hpnicfmplsLsrNotifications=_HpnicfmplsLsrNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,12,1,2))
_HpnicfmplsLsrNotifyPrefix_ObjectIdentity=ObjectIdentity
hpnicfmplsLsrNotifyPrefix=_HpnicfmplsLsrNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,12,1,2,0))
_HpnicfmplsLsrConformance_ObjectIdentity=ObjectIdentity
hpnicfmplsLsrConformance=_HpnicfmplsLsrConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,12,1,3))
_HpnicfmplsLsrGroups_ObjectIdentity=ObjectIdentity
hpnicfmplsLsrGroups=_HpnicfmplsLsrGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,12,1,3,1))
_HpnicfmplsLsrCompliances_ObjectIdentity=ObjectIdentity
hpnicfmplsLsrCompliances=_HpnicfmplsLsrCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,12,1,3,2))
hpnicfmplsInterfaceConfEntry.registerAugmentions((_B,_d))
hpnicfmplsInterfacePerfEntry.setIndexNames(*hpnicfmplsInterfaceConfEntry.getIndexNames())
hpnicfmplsInSegmentEntry.registerAugmentions((_B,_e))
hpnicfmplsInSegmentPerfEntry.setIndexNames(*hpnicfmplsInSegmentEntry.getIndexNames())
hpnicfmplsOutSegmentEntry.registerAugmentions((_B,_f))
hpnicfmplsOutSegmentPerfEntry.setIndexNames(*hpnicfmplsOutSegmentEntry.getIndexNames())
hpnicfmplsInterfaceGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,8,12,1,3,1,1))
hpnicfmplsInterfaceGroup.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:hpnicfmplsInterfaceGroup.setStatus(_A)
hpnicfmplsInSegmentGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,8,12,1,3,1,2))
hpnicfmplsInSegmentGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_P),(_B,_Q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:hpnicfmplsInSegmentGroup.setStatus(_A)
hpnicfmplsOutSegmentGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,8,12,1,3,1,3))
hpnicfmplsOutSegmentGroup.setObjects(*((_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_R),(_B,_S),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:hpnicfmplsOutSegmentGroup.setStatus(_A)
hpnicfmplsXCGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,8,12,1,3,1,4))
hpnicfmplsXCGroup.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA),(_B,_L),(_B,_M),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:hpnicfmplsXCGroup.setStatus(_A)
hpnicfmplsXCOptionalGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,8,12,1,3,1,5))
hpnicfmplsXCOptionalGroup.setObjects((_B,_AE))
if mibBuilder.loadTexts:hpnicfmplsXCOptionalGroup.setStatus(_A)
hpnicfmplsPerfGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,8,12,1,3,1,6))
hpnicfmplsPerfGroup.setObjects(*((_B,_P),(_B,_AF),(_B,_AG),(_B,_Q),(_B,_R),(_B,_AH),(_B,_S),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:hpnicfmplsPerfGroup.setStatus(_A)
hpnicfmplsHCInSegmentPerfGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,8,12,1,3,1,7))
hpnicfmplsHCInSegmentPerfGroup.setObjects((_B,_AM))
if mibBuilder.loadTexts:hpnicfmplsHCInSegmentPerfGroup.setStatus(_A)
hpnicfmplsHCOutSegmentPerfGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,8,12,1,3,1,8))
hpnicfmplsHCOutSegmentPerfGroup.setObjects((_B,_AN))
if mibBuilder.loadTexts:hpnicfmplsHCOutSegmentPerfGroup.setStatus(_A)
hpnicfmplsTrafficParamGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,8,12,1,3,1,9))
hpnicfmplsTrafficParamGroup.setObjects(*((_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT)))
if mibBuilder.loadTexts:hpnicfmplsTrafficParamGroup.setStatus(_A)
hpnicfmplsXCIsPersistentGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,8,12,1,3,1,10))
hpnicfmplsXCIsPersistentGroup.setObjects((_B,_T))
if mibBuilder.loadTexts:hpnicfmplsXCIsPersistentGroup.setStatus(_A)
hpnicfmplsXCIsNotPersistentGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,8,12,1,3,1,11))
hpnicfmplsXCIsNotPersistentGroup.setObjects((_B,_T))
if mibBuilder.loadTexts:hpnicfmplsXCIsNotPersistentGroup.setStatus(_A)
hpnicfmplsLabelStackGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,8,12,1,3,1,12))
hpnicfmplsLabelStackGroup.setObjects(*((_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY)))
if mibBuilder.loadTexts:hpnicfmplsLabelStackGroup.setStatus(_A)
hpnicfmplsSegmentDiscontinuityGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,8,12,1,3,1,13))
hpnicfmplsSegmentDiscontinuityGroup.setObjects(*((_B,_AZ),(_B,_Aa)))
if mibBuilder.loadTexts:hpnicfmplsSegmentDiscontinuityGroup.setStatus(_A)
hpnicfmplsXCUp=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,12,1,2,0,1))
hpnicfmplsXCUp.setObjects(*((_B,_K),(_B,_F),(_B,_G),(_B,_H),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:hpnicfmplsXCUp.setStatus(_A)
hpnicfmplsXCDown=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,12,1,2,0,2))
hpnicfmplsXCDown.setObjects(*((_B,_K),(_B,_F),(_B,_G),(_B,_H),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:hpnicfmplsXCDown.setStatus(_A)
hpnicfmplsLsrNotificationGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,15,8,12,1,3,1,14))
hpnicfmplsLsrNotificationGroup.setObjects(*((_B,_Ab),(_B,_Ac)))
if mibBuilder.loadTexts:hpnicfmplsLsrNotificationGroup.setStatus(_A)
hpnicfmplsLsrModuleCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,8,12,1,3,2,1))
hpnicfmplsLsrModuleCompliance.setObjects(*((_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An)))
if mibBuilder.loadTexts:hpnicfmplsLsrModuleCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'HpnicfMplsLSPID':HpnicfMplsLSPID,'HpnicfMplsLabel':HpnicfMplsLabel,'HpnicfMplsBitRate':HpnicfMplsBitRate,'HpnicfMplsBurstSize':HpnicfMplsBurstSize,_O:HpnicfMplsObjectOwner,'hpnicfMplsLsr':hpnicfMplsLsr,'hpnicfmplsLsrObjects':hpnicfmplsLsrObjects,'hpnicfmplsInterfaceConfTable':hpnicfmplsInterfaceConfTable,'hpnicfmplsInterfaceConfEntry':hpnicfmplsInterfaceConfEntry,_X:hpnicfmplsInterfaceConfIndex,_g:hpnicfmplsInterfaceLabelMinIn,_h:hpnicfmplsInterfaceLabelMaxIn,_i:hpnicfmplsInterfaceLabelMinOut,_j:hpnicfmplsInterfaceLabelMaxOut,_k:hpnicfmplsInterfaceTotalBandwidth,_l:hpnicfmplsInterfaceAvailableBandwidth,_m:hpnicfmplsInterfaceLabelParticipationType,_n:hpnicfmplsInterfaceConfStorageType,'hpnicfmplsInterfacePerfTable':hpnicfmplsInterfacePerfTable,_d:hpnicfmplsInterfacePerfEntry,_AI:hpnicfmplsInterfaceInLabelsUsed,_AJ:hpnicfmplsInterfaceFailedLabelLookup,_AL:hpnicfmplsInterfaceOutLabelsUsed,_AK:hpnicfmplsInterfaceOutFragments,'hpnicfmplsInSegmentTable':hpnicfmplsInSegmentTable,'hpnicfmplsInSegmentEntry':hpnicfmplsInSegmentEntry,_F:hpnicfmplsInSegmentIfIndex,_G:hpnicfmplsInSegmentLabel,_o:hpnicfmplsInSegmentNPop,_p:hpnicfmplsInSegmentAddrFamily,_q:hpnicfmplsInSegmentXCIndex,_r:hpnicfmplsInSegmentOwner,_u:hpnicfmplsInSegmentTrafficParamPtr,_s:hpnicfmplsInSegmentRowStatus,_t:hpnicfmplsInSegmentStorageType,'hpnicfmplsInSegmentPerfTable':hpnicfmplsInSegmentPerfTable,_e:hpnicfmplsInSegmentPerfEntry,_P:hpnicfmplsInSegmentOctets,_AF:hpnicfmplsInSegmentPackets,_AG:hpnicfmplsInSegmentErrors,_Q:hpnicfmplsInSegmentDiscards,_AM:hpnicfmplsInSegmentHCOctets,_AZ:hpnicfmplsInSegmentPerfDiscontinuityTime,_v:hpnicfmplsOutSegmentIndexNext,'hpnicfmplsOutSegmentTable':hpnicfmplsOutSegmentTable,'hpnicfmplsOutSegmentEntry':hpnicfmplsOutSegmentEntry,_H:hpnicfmplsOutSegmentIndex,_w:hpnicfmplsOutSegmentIfIndex,_x:hpnicfmplsOutSegmentPushTopLabel,_y:hpnicfmplsOutSegmentTopLabel,_z:hpnicfmplsOutSegmentNextHopIpAddrType,_A0:hpnicfmplsOutSegmentNextHopIpv4Addr,_A1:hpnicfmplsOutSegmentNextHopIpv6Addr,_A2:hpnicfmplsOutSegmentXCIndex,_A3:hpnicfmplsOutSegmentOwner,_A7:hpnicfmplsOutSegmentTrafficParamPtr,_A5:hpnicfmplsOutSegmentRowStatus,_A6:hpnicfmplsOutSegmentStorageType,'hpnicfmplsOutSegmentPerfTable':hpnicfmplsOutSegmentPerfTable,_f:hpnicfmplsOutSegmentPerfEntry,_R:hpnicfmplsOutSegmentOctets,_AH:hpnicfmplsOutSegmentPackets,_A4:hpnicfmplsOutSegmentErrors,_S:hpnicfmplsOutSegmentDiscards,_AN:hpnicfmplsOutSegmentHCOctets,_Aa:hpnicfmplsOutSegmentPerfDiscontinuityTime,_A8:hpnicfmplsXCIndexNext,'hpnicfmplsXCTable':hpnicfmplsXCTable,'hpnicfmplsXCEntry':hpnicfmplsXCEntry,_K:hpnicfmplsXCIndex,_AE:hpnicfmplsXCLspId,_A9:hpnicfmplsXCLabelStackIndex,_T:hpnicfmplsXCIsPersistent,_AA:hpnicfmplsXCOwner,_AB:hpnicfmplsXCRowStatus,_AD:hpnicfmplsXCStorageType,_L:hpnicfmplsXCAdminStatus,_M:hpnicfmplsXCOperStatus,_AX:hpnicfmplsMaxLabelStackDepth,_AY:hpnicfmplsLabelStackIndexNext,'hpnicfmplsLabelStackTable':hpnicfmplsLabelStackTable,'hpnicfmplsLabelStackEntry':hpnicfmplsLabelStackEntry,_Z:hpnicfmplsLabelStackIndex,_a:hpnicfmplsLabelStackLabelIndex,_AU:hpnicfmplsLabelStackLabel,_AV:hpnicfmplsLabelStackRowStatus,_AW:hpnicfmplsLabelStackStorageType,_AO:hpnicfmplsTrafficParamIndexNext,'hpnicfmplsTrafficParamTable':hpnicfmplsTrafficParamTable,'hpnicfmplsTrafficParamEntry':hpnicfmplsTrafficParamEntry,_b:hpnicfmplsTrafficParamIndex,_AP:hpnicfmplsTrafficParamMaxRate,_AQ:hpnicfmplsTrafficParamMeanRate,_AR:hpnicfmplsTrafficParamMaxBurstSize,_AS:hpnicfmplsTrafficParamRowStatus,_AT:hpnicfmplsTrafficParamStorageType,_AC:hpnicfmplsXCTrapEnable,'hpnicfmplsLsrNotifications':hpnicfmplsLsrNotifications,'hpnicfmplsLsrNotifyPrefix':hpnicfmplsLsrNotifyPrefix,_Ab:hpnicfmplsXCUp,_Ac:hpnicfmplsXCDown,'hpnicfmplsLsrConformance':hpnicfmplsLsrConformance,'hpnicfmplsLsrGroups':hpnicfmplsLsrGroups,_Ag:hpnicfmplsInterfaceGroup,_Ad:hpnicfmplsInSegmentGroup,_Ae:hpnicfmplsOutSegmentGroup,_Af:hpnicfmplsXCGroup,'hpnicfmplsXCOptionalGroup':hpnicfmplsXCOptionalGroup,_Ah:hpnicfmplsPerfGroup,_Aj:hpnicfmplsHCInSegmentPerfGroup,_Ak:hpnicfmplsHCOutSegmentPerfGroup,_Al:hpnicfmplsTrafficParamGroup,_Am:hpnicfmplsXCIsPersistentGroup,_An:hpnicfmplsXCIsNotPersistentGroup,'hpnicfmplsLabelStackGroup':hpnicfmplsLabelStackGroup,_Ai:hpnicfmplsSegmentDiscontinuityGroup,'hpnicfmplsLsrNotificationGroup':hpnicfmplsLsrNotificationGroup,'hpnicfmplsLsrCompliances':hpnicfmplsLsrCompliances,'hpnicfmplsLsrModuleCompliance':hpnicfmplsLsrModuleCompliance})