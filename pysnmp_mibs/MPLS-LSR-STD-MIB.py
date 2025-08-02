_An='mplsXCDown'
_Am='mplsLabelStackIndexNext'
_Al='mplsMaxLabelStackDepth'
_Ak='mplsLabelStackStorageType'
_Aj='mplsLabelStackRowStatus'
_Ai='mplsLabelStackLabelPtr'
_Ah='mplsLabelStackLabel'
_Ag='mplsOutSegmentPerfHCOctets'
_Af='mplsInSegmentPerfHCOctets'
_Ae='mplsInterfacePerfOutLabelsInUse'
_Ad='mplsInterfacePerfOutFragmentedPkts'
_Ac='mplsInterfacePerfInLabelLookupFailures'
_Ab='mplsInterfacePerfInLabelsInUse'
_Aa='mplsOutSegmentPerfDiscontinuityTime'
_AZ='mplsOutSegmentPerfPackets'
_AY='mplsInSegmentPerfDiscontinuityTime'
_AX='mplsInSegmentPerfDiscards'
_AW='mplsInSegmentPerfErrors'
_AV='mplsInSegmentPerfPackets'
_AU='mplsInSegmentPerfOctets'
_AT='mplsXCNotificationsEnable'
_AS='mplsXCRowStatus'
_AR='mplsXCAdminStatus'
_AQ='mplsXCStorageType'
_AP='mplsXCOwner'
_AO='mplsXCLabelStackIndex'
_AN='mplsXCLspId'
_AM='mplsXCIndexNext'
_AL='mplsOutSegmentTrafficParamPtr'
_AK='mplsOutSegmentStorageType'
_AJ='mplsOutSegmentRowStatus'
_AI='mplsOutSegmentPerfErrors'
_AH='mplsOutSegmentOwner'
_AG='mplsOutSegmentXCIndex'
_AF='mplsOutSegmentNextHopAddr'
_AE='mplsOutSegmentNextHopAddrType'
_AD='mplsOutSegmentTopLabelPtr'
_AC='mplsOutSegmentTopLabel'
_AB='mplsOutSegmentPushTopLabel'
_AA='mplsOutSegmentInterface'
_A9='mplsOutSegmentIndexNext'
_A8='mplsInSegmentMapIndex'
_A7='mplsInSegmentTrafficParamPtr'
_A6='mplsInSegmentStorageType'
_A5='mplsInSegmentRowStatus'
_A4='mplsInSegmentOwner'
_A3='mplsInSegmentXCIndex'
_A2='mplsInSegmentAddrFamily'
_A1='mplsInSegmentNPop'
_A0='mplsInSegmentLabelPtr'
_z='mplsInSegmentLabel'
_y='mplsInSegmentInterface'
_x='mplsInSegmentIndexNext'
_w='mplsInterfaceLabelParticipationType'
_v='mplsInterfaceAvailableBandwidth'
_u='mplsInterfaceTotalBandwidth'
_t='mplsInterfaceLabelMaxOut'
_s='mplsInterfaceLabelMinOut'
_r='mplsInterfaceLabelMaxIn'
_q='mplsInterfaceLabelMinIn'
_p='mplsOutSegmentPerfEntry'
_o='mplsInSegmentPerfEntry'
_n='mplsInterfacePerfEntry'
_m='mplsInSegmentMapLabelPtrIndex'
_l='mplsInSegmentMapLabel'
_k='mplsInSegmentMapInterface'
_j='mplsLabelStackLabelIndex'
_i='mplsLabelStackIndex'
_h='testing'
_g='mplsXCOutSegmentIndex'
_f='mplsXCInSegmentIndex'
_e='mplsXCIndex'
_d='mplsOutSegmentIndex'
_c='mplsInSegmentIndex'
_b='mplsInterfaceIndex'
_a='MplsLabel'
_Z='AddressFamilyNumbers'
_Y='mplsLsrNotificationGroup'
_X='mplsHCOutSegmentPerfGroup'
_W='mplsHCInSegmentPerfGroup'
_V='mplsLabelStackGroup'
_U='mplsPerfGroup'
_T='mplsXCGroup'
_S='mplsOutSegmentGroup'
_R='mplsInSegmentGroup'
_Q='mplsInterfaceGroup'
_P='mplsOutSegmentPerfDiscards'
_O='mplsOutSegmentPerfOctets'
_N='TruthValue'
_M='Unsigned32'
_L='ifGeneralInformationGroup'
_K='ifCounterDiscontinuityGroup'
_J='Integer32'
_I='StorageType'
_H='IF-MIB'
_G='mplsXCOperStatus'
_F='RowPointer'
_E='not-accessible'
_D='read-create'
_C='read-only'
_B='MPLS-LSR-STD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AddressFamilyNumbers,=mibBuilder.importSymbols('IANA-ADDRESS-FAMILY-NUMBERS-MIB',_Z)
InterfaceIndexOrZero,ifCounterDiscontinuityGroup,ifGeneralInformationGroup=mibBuilder.importSymbols(_H,'InterfaceIndexOrZero',_K,_L)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
MplsBitRate,MplsLSPID,MplsLabel,MplsOwner,mplsStdMIB=mibBuilder.importSymbols('MPLS-TC-STD-MIB','MplsBitRate','MplsLSPID',_a,'MplsOwner','mplsStdMIB')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,zeroDotZero=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso','zeroDotZero')
DisplayString,PhysAddress,RowPointer,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress',_F,'RowStatus',_I,'TextualConvention','TimeStamp',_N)
mplsLsrStdMIB=ModuleIdentity((1,3,6,1,2,1,10,166,2))
if mibBuilder.loadTexts:mplsLsrStdMIB.setRevisions(('2004-06-03 00:00',))
class MplsIndexType(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
class MplsIndexNextType(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_MplsLsrNotifications_ObjectIdentity=ObjectIdentity
mplsLsrNotifications=_MplsLsrNotifications_ObjectIdentity((1,3,6,1,2,1,10,166,2,0))
_MplsLsrObjects_ObjectIdentity=ObjectIdentity
mplsLsrObjects=_MplsLsrObjects_ObjectIdentity((1,3,6,1,2,1,10,166,2,1))
_MplsInterfaceTable_Object=MibTable
mplsInterfaceTable=_MplsInterfaceTable_Object((1,3,6,1,2,1,10,166,2,1,1))
if mibBuilder.loadTexts:mplsInterfaceTable.setStatus(_A)
_MplsInterfaceEntry_Object=MibTableRow
mplsInterfaceEntry=_MplsInterfaceEntry_Object((1,3,6,1,2,1,10,166,2,1,1,1))
mplsInterfaceEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:mplsInterfaceEntry.setStatus(_A)
_MplsInterfaceIndex_Type=InterfaceIndexOrZero
_MplsInterfaceIndex_Object=MibTableColumn
mplsInterfaceIndex=_MplsInterfaceIndex_Object((1,3,6,1,2,1,10,166,2,1,1,1,1),_MplsInterfaceIndex_Type())
mplsInterfaceIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsInterfaceIndex.setStatus(_A)
_MplsInterfaceLabelMinIn_Type=MplsLabel
_MplsInterfaceLabelMinIn_Object=MibTableColumn
mplsInterfaceLabelMinIn=_MplsInterfaceLabelMinIn_Object((1,3,6,1,2,1,10,166,2,1,1,1,2),_MplsInterfaceLabelMinIn_Type())
mplsInterfaceLabelMinIn.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceLabelMinIn.setStatus(_A)
_MplsInterfaceLabelMaxIn_Type=MplsLabel
_MplsInterfaceLabelMaxIn_Object=MibTableColumn
mplsInterfaceLabelMaxIn=_MplsInterfaceLabelMaxIn_Object((1,3,6,1,2,1,10,166,2,1,1,1,3),_MplsInterfaceLabelMaxIn_Type())
mplsInterfaceLabelMaxIn.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceLabelMaxIn.setStatus(_A)
_MplsInterfaceLabelMinOut_Type=MplsLabel
_MplsInterfaceLabelMinOut_Object=MibTableColumn
mplsInterfaceLabelMinOut=_MplsInterfaceLabelMinOut_Object((1,3,6,1,2,1,10,166,2,1,1,1,4),_MplsInterfaceLabelMinOut_Type())
mplsInterfaceLabelMinOut.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceLabelMinOut.setStatus(_A)
_MplsInterfaceLabelMaxOut_Type=MplsLabel
_MplsInterfaceLabelMaxOut_Object=MibTableColumn
mplsInterfaceLabelMaxOut=_MplsInterfaceLabelMaxOut_Object((1,3,6,1,2,1,10,166,2,1,1,1,5),_MplsInterfaceLabelMaxOut_Type())
mplsInterfaceLabelMaxOut.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceLabelMaxOut.setStatus(_A)
_MplsInterfaceTotalBandwidth_Type=MplsBitRate
_MplsInterfaceTotalBandwidth_Object=MibTableColumn
mplsInterfaceTotalBandwidth=_MplsInterfaceTotalBandwidth_Object((1,3,6,1,2,1,10,166,2,1,1,1,6),_MplsInterfaceTotalBandwidth_Type())
mplsInterfaceTotalBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceTotalBandwidth.setStatus(_A)
if mibBuilder.loadTexts:mplsInterfaceTotalBandwidth.setUnits('kilobits per second')
_MplsInterfaceAvailableBandwidth_Type=MplsBitRate
_MplsInterfaceAvailableBandwidth_Object=MibTableColumn
mplsInterfaceAvailableBandwidth=_MplsInterfaceAvailableBandwidth_Object((1,3,6,1,2,1,10,166,2,1,1,1,7),_MplsInterfaceAvailableBandwidth_Type())
mplsInterfaceAvailableBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceAvailableBandwidth.setStatus(_A)
class _MplsInterfaceLabelParticipationType_Type(Bits):namedValues=NamedValues(*(('perPlatform',0),('perInterface',1)))
_MplsInterfaceLabelParticipationType_Type.__name__='Bits'
_MplsInterfaceLabelParticipationType_Object=MibTableColumn
mplsInterfaceLabelParticipationType=_MplsInterfaceLabelParticipationType_Object((1,3,6,1,2,1,10,166,2,1,1,1,8),_MplsInterfaceLabelParticipationType_Type())
mplsInterfaceLabelParticipationType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfaceLabelParticipationType.setStatus(_A)
_MplsInterfacePerfTable_Object=MibTable
mplsInterfacePerfTable=_MplsInterfacePerfTable_Object((1,3,6,1,2,1,10,166,2,1,2))
if mibBuilder.loadTexts:mplsInterfacePerfTable.setStatus(_A)
_MplsInterfacePerfEntry_Object=MibTableRow
mplsInterfacePerfEntry=_MplsInterfacePerfEntry_Object((1,3,6,1,2,1,10,166,2,1,2,1))
if mibBuilder.loadTexts:mplsInterfacePerfEntry.setStatus(_A)
_MplsInterfacePerfInLabelsInUse_Type=Gauge32
_MplsInterfacePerfInLabelsInUse_Object=MibTableColumn
mplsInterfacePerfInLabelsInUse=_MplsInterfacePerfInLabelsInUse_Object((1,3,6,1,2,1,10,166,2,1,2,1,1),_MplsInterfacePerfInLabelsInUse_Type())
mplsInterfacePerfInLabelsInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfacePerfInLabelsInUse.setStatus(_A)
_MplsInterfacePerfInLabelLookupFailures_Type=Counter32
_MplsInterfacePerfInLabelLookupFailures_Object=MibTableColumn
mplsInterfacePerfInLabelLookupFailures=_MplsInterfacePerfInLabelLookupFailures_Object((1,3,6,1,2,1,10,166,2,1,2,1,2),_MplsInterfacePerfInLabelLookupFailures_Type())
mplsInterfacePerfInLabelLookupFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfacePerfInLabelLookupFailures.setStatus(_A)
_MplsInterfacePerfOutLabelsInUse_Type=Gauge32
_MplsInterfacePerfOutLabelsInUse_Object=MibTableColumn
mplsInterfacePerfOutLabelsInUse=_MplsInterfacePerfOutLabelsInUse_Object((1,3,6,1,2,1,10,166,2,1,2,1,3),_MplsInterfacePerfOutLabelsInUse_Type())
mplsInterfacePerfOutLabelsInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfacePerfOutLabelsInUse.setStatus(_A)
_MplsInterfacePerfOutFragmentedPkts_Type=Counter32
_MplsInterfacePerfOutFragmentedPkts_Object=MibTableColumn
mplsInterfacePerfOutFragmentedPkts=_MplsInterfacePerfOutFragmentedPkts_Object((1,3,6,1,2,1,10,166,2,1,2,1,4),_MplsInterfacePerfOutFragmentedPkts_Type())
mplsInterfacePerfOutFragmentedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInterfacePerfOutFragmentedPkts.setStatus(_A)
_MplsInSegmentIndexNext_Type=MplsIndexNextType
_MplsInSegmentIndexNext_Object=MibScalar
mplsInSegmentIndexNext=_MplsInSegmentIndexNext_Object((1,3,6,1,2,1,10,166,2,1,3),_MplsInSegmentIndexNext_Type())
mplsInSegmentIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentIndexNext.setStatus(_A)
_MplsInSegmentTable_Object=MibTable
mplsInSegmentTable=_MplsInSegmentTable_Object((1,3,6,1,2,1,10,166,2,1,4))
if mibBuilder.loadTexts:mplsInSegmentTable.setStatus(_A)
_MplsInSegmentEntry_Object=MibTableRow
mplsInSegmentEntry=_MplsInSegmentEntry_Object((1,3,6,1,2,1,10,166,2,1,4,1))
mplsInSegmentEntry.setIndexNames((0,_B,_c))
if mibBuilder.loadTexts:mplsInSegmentEntry.setStatus(_A)
_MplsInSegmentIndex_Type=MplsIndexType
_MplsInSegmentIndex_Object=MibTableColumn
mplsInSegmentIndex=_MplsInSegmentIndex_Object((1,3,6,1,2,1,10,166,2,1,4,1,1),_MplsInSegmentIndex_Type())
mplsInSegmentIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsInSegmentIndex.setStatus(_A)
_MplsInSegmentInterface_Type=InterfaceIndexOrZero
_MplsInSegmentInterface_Object=MibTableColumn
mplsInSegmentInterface=_MplsInSegmentInterface_Object((1,3,6,1,2,1,10,166,2,1,4,1,2),_MplsInSegmentInterface_Type())
mplsInSegmentInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentInterface.setStatus(_A)
_MplsInSegmentLabel_Type=MplsLabel
_MplsInSegmentLabel_Object=MibTableColumn
mplsInSegmentLabel=_MplsInSegmentLabel_Object((1,3,6,1,2,1,10,166,2,1,4,1,3),_MplsInSegmentLabel_Type())
mplsInSegmentLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentLabel.setStatus(_A)
class _MplsInSegmentLabelPtr_Type(RowPointer):defaultValue=0,0
_MplsInSegmentLabelPtr_Type.__name__=_F
_MplsInSegmentLabelPtr_Object=MibTableColumn
mplsInSegmentLabelPtr=_MplsInSegmentLabelPtr_Object((1,3,6,1,2,1,10,166,2,1,4,1,4),_MplsInSegmentLabelPtr_Type())
mplsInSegmentLabelPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentLabelPtr.setStatus(_A)
class _MplsInSegmentNPop_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsInSegmentNPop_Type.__name__=_J
_MplsInSegmentNPop_Object=MibTableColumn
mplsInSegmentNPop=_MplsInSegmentNPop_Object((1,3,6,1,2,1,10,166,2,1,4,1,5),_MplsInSegmentNPop_Type())
mplsInSegmentNPop.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentNPop.setStatus(_A)
class _MplsInSegmentAddrFamily_Type(AddressFamilyNumbers):defaultValue=0
_MplsInSegmentAddrFamily_Type.__name__=_Z
_MplsInSegmentAddrFamily_Object=MibTableColumn
mplsInSegmentAddrFamily=_MplsInSegmentAddrFamily_Object((1,3,6,1,2,1,10,166,2,1,4,1,6),_MplsInSegmentAddrFamily_Type())
mplsInSegmentAddrFamily.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentAddrFamily.setStatus(_A)
_MplsInSegmentXCIndex_Type=MplsIndexType
_MplsInSegmentXCIndex_Object=MibTableColumn
mplsInSegmentXCIndex=_MplsInSegmentXCIndex_Object((1,3,6,1,2,1,10,166,2,1,4,1,7),_MplsInSegmentXCIndex_Type())
mplsInSegmentXCIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentXCIndex.setStatus(_A)
_MplsInSegmentOwner_Type=MplsOwner
_MplsInSegmentOwner_Object=MibTableColumn
mplsInSegmentOwner=_MplsInSegmentOwner_Object((1,3,6,1,2,1,10,166,2,1,4,1,8),_MplsInSegmentOwner_Type())
mplsInSegmentOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentOwner.setStatus(_A)
class _MplsInSegmentTrafficParamPtr_Type(RowPointer):defaultValue=0,0
_MplsInSegmentTrafficParamPtr_Type.__name__=_F
_MplsInSegmentTrafficParamPtr_Object=MibTableColumn
mplsInSegmentTrafficParamPtr=_MplsInSegmentTrafficParamPtr_Object((1,3,6,1,2,1,10,166,2,1,4,1,9),_MplsInSegmentTrafficParamPtr_Type())
mplsInSegmentTrafficParamPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentTrafficParamPtr.setStatus(_A)
_MplsInSegmentRowStatus_Type=RowStatus
_MplsInSegmentRowStatus_Object=MibTableColumn
mplsInSegmentRowStatus=_MplsInSegmentRowStatus_Object((1,3,6,1,2,1,10,166,2,1,4,1,10),_MplsInSegmentRowStatus_Type())
mplsInSegmentRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentRowStatus.setStatus(_A)
class _MplsInSegmentStorageType_Type(StorageType):defaultValue=2
_MplsInSegmentStorageType_Type.__name__=_I
_MplsInSegmentStorageType_Object=MibTableColumn
mplsInSegmentStorageType=_MplsInSegmentStorageType_Object((1,3,6,1,2,1,10,166,2,1,4,1,11),_MplsInSegmentStorageType_Type())
mplsInSegmentStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsInSegmentStorageType.setStatus(_A)
_MplsInSegmentPerfTable_Object=MibTable
mplsInSegmentPerfTable=_MplsInSegmentPerfTable_Object((1,3,6,1,2,1,10,166,2,1,5))
if mibBuilder.loadTexts:mplsInSegmentPerfTable.setStatus(_A)
_MplsInSegmentPerfEntry_Object=MibTableRow
mplsInSegmentPerfEntry=_MplsInSegmentPerfEntry_Object((1,3,6,1,2,1,10,166,2,1,5,1))
if mibBuilder.loadTexts:mplsInSegmentPerfEntry.setStatus(_A)
_MplsInSegmentPerfOctets_Type=Counter32
_MplsInSegmentPerfOctets_Object=MibTableColumn
mplsInSegmentPerfOctets=_MplsInSegmentPerfOctets_Object((1,3,6,1,2,1,10,166,2,1,5,1,1),_MplsInSegmentPerfOctets_Type())
mplsInSegmentPerfOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentPerfOctets.setStatus(_A)
_MplsInSegmentPerfPackets_Type=Counter32
_MplsInSegmentPerfPackets_Object=MibTableColumn
mplsInSegmentPerfPackets=_MplsInSegmentPerfPackets_Object((1,3,6,1,2,1,10,166,2,1,5,1,2),_MplsInSegmentPerfPackets_Type())
mplsInSegmentPerfPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentPerfPackets.setStatus(_A)
_MplsInSegmentPerfErrors_Type=Counter32
_MplsInSegmentPerfErrors_Object=MibTableColumn
mplsInSegmentPerfErrors=_MplsInSegmentPerfErrors_Object((1,3,6,1,2,1,10,166,2,1,5,1,3),_MplsInSegmentPerfErrors_Type())
mplsInSegmentPerfErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentPerfErrors.setStatus(_A)
_MplsInSegmentPerfDiscards_Type=Counter32
_MplsInSegmentPerfDiscards_Object=MibTableColumn
mplsInSegmentPerfDiscards=_MplsInSegmentPerfDiscards_Object((1,3,6,1,2,1,10,166,2,1,5,1,4),_MplsInSegmentPerfDiscards_Type())
mplsInSegmentPerfDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentPerfDiscards.setStatus(_A)
_MplsInSegmentPerfHCOctets_Type=Counter64
_MplsInSegmentPerfHCOctets_Object=MibTableColumn
mplsInSegmentPerfHCOctets=_MplsInSegmentPerfHCOctets_Object((1,3,6,1,2,1,10,166,2,1,5,1,5),_MplsInSegmentPerfHCOctets_Type())
mplsInSegmentPerfHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentPerfHCOctets.setStatus(_A)
_MplsInSegmentPerfDiscontinuityTime_Type=TimeStamp
_MplsInSegmentPerfDiscontinuityTime_Object=MibTableColumn
mplsInSegmentPerfDiscontinuityTime=_MplsInSegmentPerfDiscontinuityTime_Object((1,3,6,1,2,1,10,166,2,1,5,1,6),_MplsInSegmentPerfDiscontinuityTime_Type())
mplsInSegmentPerfDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentPerfDiscontinuityTime.setStatus(_A)
_MplsOutSegmentIndexNext_Type=MplsIndexNextType
_MplsOutSegmentIndexNext_Object=MibScalar
mplsOutSegmentIndexNext=_MplsOutSegmentIndexNext_Object((1,3,6,1,2,1,10,166,2,1,6),_MplsOutSegmentIndexNext_Type())
mplsOutSegmentIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentIndexNext.setStatus(_A)
_MplsOutSegmentTable_Object=MibTable
mplsOutSegmentTable=_MplsOutSegmentTable_Object((1,3,6,1,2,1,10,166,2,1,7))
if mibBuilder.loadTexts:mplsOutSegmentTable.setStatus(_A)
_MplsOutSegmentEntry_Object=MibTableRow
mplsOutSegmentEntry=_MplsOutSegmentEntry_Object((1,3,6,1,2,1,10,166,2,1,7,1))
mplsOutSegmentEntry.setIndexNames((0,_B,_d))
if mibBuilder.loadTexts:mplsOutSegmentEntry.setStatus(_A)
_MplsOutSegmentIndex_Type=MplsIndexType
_MplsOutSegmentIndex_Object=MibTableColumn
mplsOutSegmentIndex=_MplsOutSegmentIndex_Object((1,3,6,1,2,1,10,166,2,1,7,1,1),_MplsOutSegmentIndex_Type())
mplsOutSegmentIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsOutSegmentIndex.setStatus(_A)
_MplsOutSegmentInterface_Type=InterfaceIndexOrZero
_MplsOutSegmentInterface_Object=MibTableColumn
mplsOutSegmentInterface=_MplsOutSegmentInterface_Object((1,3,6,1,2,1,10,166,2,1,7,1,2),_MplsOutSegmentInterface_Type())
mplsOutSegmentInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentInterface.setStatus(_A)
class _MplsOutSegmentPushTopLabel_Type(TruthValue):defaultValue=1
_MplsOutSegmentPushTopLabel_Type.__name__=_N
_MplsOutSegmentPushTopLabel_Object=MibTableColumn
mplsOutSegmentPushTopLabel=_MplsOutSegmentPushTopLabel_Object((1,3,6,1,2,1,10,166,2,1,7,1,3),_MplsOutSegmentPushTopLabel_Type())
mplsOutSegmentPushTopLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentPushTopLabel.setStatus(_A)
class _MplsOutSegmentTopLabel_Type(MplsLabel):defaultValue=0
_MplsOutSegmentTopLabel_Type.__name__=_a
_MplsOutSegmentTopLabel_Object=MibTableColumn
mplsOutSegmentTopLabel=_MplsOutSegmentTopLabel_Object((1,3,6,1,2,1,10,166,2,1,7,1,4),_MplsOutSegmentTopLabel_Type())
mplsOutSegmentTopLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentTopLabel.setStatus(_A)
class _MplsOutSegmentTopLabelPtr_Type(RowPointer):defaultValue=0,0
_MplsOutSegmentTopLabelPtr_Type.__name__=_F
_MplsOutSegmentTopLabelPtr_Object=MibTableColumn
mplsOutSegmentTopLabelPtr=_MplsOutSegmentTopLabelPtr_Object((1,3,6,1,2,1,10,166,2,1,7,1,5),_MplsOutSegmentTopLabelPtr_Type())
mplsOutSegmentTopLabelPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentTopLabelPtr.setStatus(_A)
_MplsOutSegmentNextHopAddrType_Type=InetAddressType
_MplsOutSegmentNextHopAddrType_Object=MibTableColumn
mplsOutSegmentNextHopAddrType=_MplsOutSegmentNextHopAddrType_Object((1,3,6,1,2,1,10,166,2,1,7,1,6),_MplsOutSegmentNextHopAddrType_Type())
mplsOutSegmentNextHopAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentNextHopAddrType.setStatus(_A)
_MplsOutSegmentNextHopAddr_Type=InetAddress
_MplsOutSegmentNextHopAddr_Object=MibTableColumn
mplsOutSegmentNextHopAddr=_MplsOutSegmentNextHopAddr_Object((1,3,6,1,2,1,10,166,2,1,7,1,7),_MplsOutSegmentNextHopAddr_Type())
mplsOutSegmentNextHopAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentNextHopAddr.setStatus(_A)
_MplsOutSegmentXCIndex_Type=MplsIndexType
_MplsOutSegmentXCIndex_Object=MibTableColumn
mplsOutSegmentXCIndex=_MplsOutSegmentXCIndex_Object((1,3,6,1,2,1,10,166,2,1,7,1,8),_MplsOutSegmentXCIndex_Type())
mplsOutSegmentXCIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentXCIndex.setStatus(_A)
_MplsOutSegmentOwner_Type=MplsOwner
_MplsOutSegmentOwner_Object=MibTableColumn
mplsOutSegmentOwner=_MplsOutSegmentOwner_Object((1,3,6,1,2,1,10,166,2,1,7,1,9),_MplsOutSegmentOwner_Type())
mplsOutSegmentOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentOwner.setStatus(_A)
class _MplsOutSegmentTrafficParamPtr_Type(RowPointer):defaultValue=0,0
_MplsOutSegmentTrafficParamPtr_Type.__name__=_F
_MplsOutSegmentTrafficParamPtr_Object=MibTableColumn
mplsOutSegmentTrafficParamPtr=_MplsOutSegmentTrafficParamPtr_Object((1,3,6,1,2,1,10,166,2,1,7,1,10),_MplsOutSegmentTrafficParamPtr_Type())
mplsOutSegmentTrafficParamPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentTrafficParamPtr.setStatus(_A)
_MplsOutSegmentRowStatus_Type=RowStatus
_MplsOutSegmentRowStatus_Object=MibTableColumn
mplsOutSegmentRowStatus=_MplsOutSegmentRowStatus_Object((1,3,6,1,2,1,10,166,2,1,7,1,11),_MplsOutSegmentRowStatus_Type())
mplsOutSegmentRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentRowStatus.setStatus(_A)
class _MplsOutSegmentStorageType_Type(StorageType):defaultValue=2
_MplsOutSegmentStorageType_Type.__name__=_I
_MplsOutSegmentStorageType_Object=MibTableColumn
mplsOutSegmentStorageType=_MplsOutSegmentStorageType_Object((1,3,6,1,2,1,10,166,2,1,7,1,12),_MplsOutSegmentStorageType_Type())
mplsOutSegmentStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOutSegmentStorageType.setStatus(_A)
_MplsOutSegmentPerfTable_Object=MibTable
mplsOutSegmentPerfTable=_MplsOutSegmentPerfTable_Object((1,3,6,1,2,1,10,166,2,1,8))
if mibBuilder.loadTexts:mplsOutSegmentPerfTable.setStatus(_A)
_MplsOutSegmentPerfEntry_Object=MibTableRow
mplsOutSegmentPerfEntry=_MplsOutSegmentPerfEntry_Object((1,3,6,1,2,1,10,166,2,1,8,1))
if mibBuilder.loadTexts:mplsOutSegmentPerfEntry.setStatus(_A)
_MplsOutSegmentPerfOctets_Type=Counter32
_MplsOutSegmentPerfOctets_Object=MibTableColumn
mplsOutSegmentPerfOctets=_MplsOutSegmentPerfOctets_Object((1,3,6,1,2,1,10,166,2,1,8,1,1),_MplsOutSegmentPerfOctets_Type())
mplsOutSegmentPerfOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentPerfOctets.setStatus(_A)
_MplsOutSegmentPerfPackets_Type=Counter32
_MplsOutSegmentPerfPackets_Object=MibTableColumn
mplsOutSegmentPerfPackets=_MplsOutSegmentPerfPackets_Object((1,3,6,1,2,1,10,166,2,1,8,1,2),_MplsOutSegmentPerfPackets_Type())
mplsOutSegmentPerfPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentPerfPackets.setStatus(_A)
_MplsOutSegmentPerfErrors_Type=Counter32
_MplsOutSegmentPerfErrors_Object=MibTableColumn
mplsOutSegmentPerfErrors=_MplsOutSegmentPerfErrors_Object((1,3,6,1,2,1,10,166,2,1,8,1,3),_MplsOutSegmentPerfErrors_Type())
mplsOutSegmentPerfErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentPerfErrors.setStatus(_A)
_MplsOutSegmentPerfDiscards_Type=Counter32
_MplsOutSegmentPerfDiscards_Object=MibTableColumn
mplsOutSegmentPerfDiscards=_MplsOutSegmentPerfDiscards_Object((1,3,6,1,2,1,10,166,2,1,8,1,4),_MplsOutSegmentPerfDiscards_Type())
mplsOutSegmentPerfDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentPerfDiscards.setStatus(_A)
_MplsOutSegmentPerfHCOctets_Type=Counter64
_MplsOutSegmentPerfHCOctets_Object=MibTableColumn
mplsOutSegmentPerfHCOctets=_MplsOutSegmentPerfHCOctets_Object((1,3,6,1,2,1,10,166,2,1,8,1,5),_MplsOutSegmentPerfHCOctets_Type())
mplsOutSegmentPerfHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentPerfHCOctets.setStatus(_A)
_MplsOutSegmentPerfDiscontinuityTime_Type=TimeStamp
_MplsOutSegmentPerfDiscontinuityTime_Object=MibTableColumn
mplsOutSegmentPerfDiscontinuityTime=_MplsOutSegmentPerfDiscontinuityTime_Object((1,3,6,1,2,1,10,166,2,1,8,1,6),_MplsOutSegmentPerfDiscontinuityTime_Type())
mplsOutSegmentPerfDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOutSegmentPerfDiscontinuityTime.setStatus(_A)
_MplsXCIndexNext_Type=MplsIndexNextType
_MplsXCIndexNext_Object=MibScalar
mplsXCIndexNext=_MplsXCIndexNext_Object((1,3,6,1,2,1,10,166,2,1,9),_MplsXCIndexNext_Type())
mplsXCIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsXCIndexNext.setStatus(_A)
_MplsXCTable_Object=MibTable
mplsXCTable=_MplsXCTable_Object((1,3,6,1,2,1,10,166,2,1,10))
if mibBuilder.loadTexts:mplsXCTable.setStatus(_A)
_MplsXCEntry_Object=MibTableRow
mplsXCEntry=_MplsXCEntry_Object((1,3,6,1,2,1,10,166,2,1,10,1))
mplsXCEntry.setIndexNames((0,_B,_e),(0,_B,_f),(0,_B,_g))
if mibBuilder.loadTexts:mplsXCEntry.setStatus(_A)
_MplsXCIndex_Type=MplsIndexType
_MplsXCIndex_Object=MibTableColumn
mplsXCIndex=_MplsXCIndex_Object((1,3,6,1,2,1,10,166,2,1,10,1,1),_MplsXCIndex_Type())
mplsXCIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsXCIndex.setStatus(_A)
_MplsXCInSegmentIndex_Type=MplsIndexType
_MplsXCInSegmentIndex_Object=MibTableColumn
mplsXCInSegmentIndex=_MplsXCInSegmentIndex_Object((1,3,6,1,2,1,10,166,2,1,10,1,2),_MplsXCInSegmentIndex_Type())
mplsXCInSegmentIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsXCInSegmentIndex.setStatus(_A)
_MplsXCOutSegmentIndex_Type=MplsIndexType
_MplsXCOutSegmentIndex_Object=MibTableColumn
mplsXCOutSegmentIndex=_MplsXCOutSegmentIndex_Object((1,3,6,1,2,1,10,166,2,1,10,1,3),_MplsXCOutSegmentIndex_Type())
mplsXCOutSegmentIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsXCOutSegmentIndex.setStatus(_A)
_MplsXCLspId_Type=MplsLSPID
_MplsXCLspId_Object=MibTableColumn
mplsXCLspId=_MplsXCLspId_Object((1,3,6,1,2,1,10,166,2,1,10,1,4),_MplsXCLspId_Type())
mplsXCLspId.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCLspId.setStatus(_A)
_MplsXCLabelStackIndex_Type=MplsIndexType
_MplsXCLabelStackIndex_Object=MibTableColumn
mplsXCLabelStackIndex=_MplsXCLabelStackIndex_Object((1,3,6,1,2,1,10,166,2,1,10,1,5),_MplsXCLabelStackIndex_Type())
mplsXCLabelStackIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCLabelStackIndex.setStatus(_A)
_MplsXCOwner_Type=MplsOwner
_MplsXCOwner_Object=MibTableColumn
mplsXCOwner=_MplsXCOwner_Object((1,3,6,1,2,1,10,166,2,1,10,1,6),_MplsXCOwner_Type())
mplsXCOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsXCOwner.setStatus(_A)
_MplsXCRowStatus_Type=RowStatus
_MplsXCRowStatus_Object=MibTableColumn
mplsXCRowStatus=_MplsXCRowStatus_Object((1,3,6,1,2,1,10,166,2,1,10,1,7),_MplsXCRowStatus_Type())
mplsXCRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCRowStatus.setStatus(_A)
class _MplsXCStorageType_Type(StorageType):defaultValue=2
_MplsXCStorageType_Type.__name__=_I
_MplsXCStorageType_Object=MibTableColumn
mplsXCStorageType=_MplsXCStorageType_Object((1,3,6,1,2,1,10,166,2,1,10,1,8),_MplsXCStorageType_Type())
mplsXCStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCStorageType.setStatus(_A)
class _MplsXCAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_h,3)))
_MplsXCAdminStatus_Type.__name__=_J
_MplsXCAdminStatus_Object=MibTableColumn
mplsXCAdminStatus=_MplsXCAdminStatus_Object((1,3,6,1,2,1,10,166,2,1,10,1,9),_MplsXCAdminStatus_Type())
mplsXCAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCAdminStatus.setStatus(_A)
class _MplsXCOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('up',1),('down',2),(_h,3),('unknown',4),('dormant',5),('notPresent',6),('lowerLayerDown',7)))
_MplsXCOperStatus_Type.__name__=_J
_MplsXCOperStatus_Object=MibTableColumn
mplsXCOperStatus=_MplsXCOperStatus_Object((1,3,6,1,2,1,10,166,2,1,10,1,10),_MplsXCOperStatus_Type())
mplsXCOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsXCOperStatus.setStatus(_A)
class _MplsMaxLabelStackDepth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsMaxLabelStackDepth_Type.__name__=_M
_MplsMaxLabelStackDepth_Object=MibScalar
mplsMaxLabelStackDepth=_MplsMaxLabelStackDepth_Object((1,3,6,1,2,1,10,166,2,1,11),_MplsMaxLabelStackDepth_Type())
mplsMaxLabelStackDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsMaxLabelStackDepth.setStatus(_A)
_MplsLabelStackIndexNext_Type=MplsIndexNextType
_MplsLabelStackIndexNext_Object=MibScalar
mplsLabelStackIndexNext=_MplsLabelStackIndexNext_Object((1,3,6,1,2,1,10,166,2,1,12),_MplsLabelStackIndexNext_Type())
mplsLabelStackIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLabelStackIndexNext.setStatus(_A)
_MplsLabelStackTable_Object=MibTable
mplsLabelStackTable=_MplsLabelStackTable_Object((1,3,6,1,2,1,10,166,2,1,13))
if mibBuilder.loadTexts:mplsLabelStackTable.setStatus(_A)
_MplsLabelStackEntry_Object=MibTableRow
mplsLabelStackEntry=_MplsLabelStackEntry_Object((1,3,6,1,2,1,10,166,2,1,13,1))
mplsLabelStackEntry.setIndexNames((0,_B,_i),(0,_B,_j))
if mibBuilder.loadTexts:mplsLabelStackEntry.setStatus(_A)
_MplsLabelStackIndex_Type=MplsIndexType
_MplsLabelStackIndex_Object=MibTableColumn
mplsLabelStackIndex=_MplsLabelStackIndex_Object((1,3,6,1,2,1,10,166,2,1,13,1,1),_MplsLabelStackIndex_Type())
mplsLabelStackIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsLabelStackIndex.setStatus(_A)
class _MplsLabelStackLabelIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsLabelStackLabelIndex_Type.__name__=_M
_MplsLabelStackLabelIndex_Object=MibTableColumn
mplsLabelStackLabelIndex=_MplsLabelStackLabelIndex_Object((1,3,6,1,2,1,10,166,2,1,13,1,2),_MplsLabelStackLabelIndex_Type())
mplsLabelStackLabelIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsLabelStackLabelIndex.setStatus(_A)
_MplsLabelStackLabel_Type=MplsLabel
_MplsLabelStackLabel_Object=MibTableColumn
mplsLabelStackLabel=_MplsLabelStackLabel_Object((1,3,6,1,2,1,10,166,2,1,13,1,3),_MplsLabelStackLabel_Type())
mplsLabelStackLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLabelStackLabel.setStatus(_A)
class _MplsLabelStackLabelPtr_Type(RowPointer):defaultValue=0,0
_MplsLabelStackLabelPtr_Type.__name__=_F
_MplsLabelStackLabelPtr_Object=MibTableColumn
mplsLabelStackLabelPtr=_MplsLabelStackLabelPtr_Object((1,3,6,1,2,1,10,166,2,1,13,1,4),_MplsLabelStackLabelPtr_Type())
mplsLabelStackLabelPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLabelStackLabelPtr.setStatus(_A)
_MplsLabelStackRowStatus_Type=RowStatus
_MplsLabelStackRowStatus_Object=MibTableColumn
mplsLabelStackRowStatus=_MplsLabelStackRowStatus_Object((1,3,6,1,2,1,10,166,2,1,13,1,5),_MplsLabelStackRowStatus_Type())
mplsLabelStackRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLabelStackRowStatus.setStatus(_A)
class _MplsLabelStackStorageType_Type(StorageType):defaultValue=2
_MplsLabelStackStorageType_Type.__name__=_I
_MplsLabelStackStorageType_Object=MibTableColumn
mplsLabelStackStorageType=_MplsLabelStackStorageType_Object((1,3,6,1,2,1,10,166,2,1,13,1,6),_MplsLabelStackStorageType_Type())
mplsLabelStackStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLabelStackStorageType.setStatus(_A)
_MplsInSegmentMapTable_Object=MibTable
mplsInSegmentMapTable=_MplsInSegmentMapTable_Object((1,3,6,1,2,1,10,166,2,1,14))
if mibBuilder.loadTexts:mplsInSegmentMapTable.setStatus(_A)
_MplsInSegmentMapEntry_Object=MibTableRow
mplsInSegmentMapEntry=_MplsInSegmentMapEntry_Object((1,3,6,1,2,1,10,166,2,1,14,1))
mplsInSegmentMapEntry.setIndexNames((0,_B,_k),(0,_B,_l),(0,_B,_m))
if mibBuilder.loadTexts:mplsInSegmentMapEntry.setStatus(_A)
_MplsInSegmentMapInterface_Type=InterfaceIndexOrZero
_MplsInSegmentMapInterface_Object=MibTableColumn
mplsInSegmentMapInterface=_MplsInSegmentMapInterface_Object((1,3,6,1,2,1,10,166,2,1,14,1,1),_MplsInSegmentMapInterface_Type())
mplsInSegmentMapInterface.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsInSegmentMapInterface.setStatus(_A)
_MplsInSegmentMapLabel_Type=MplsLabel
_MplsInSegmentMapLabel_Object=MibTableColumn
mplsInSegmentMapLabel=_MplsInSegmentMapLabel_Object((1,3,6,1,2,1,10,166,2,1,14,1,2),_MplsInSegmentMapLabel_Type())
mplsInSegmentMapLabel.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsInSegmentMapLabel.setStatus(_A)
_MplsInSegmentMapLabelPtrIndex_Type=RowPointer
_MplsInSegmentMapLabelPtrIndex_Object=MibTableColumn
mplsInSegmentMapLabelPtrIndex=_MplsInSegmentMapLabelPtrIndex_Object((1,3,6,1,2,1,10,166,2,1,14,1,3),_MplsInSegmentMapLabelPtrIndex_Type())
mplsInSegmentMapLabelPtrIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsInSegmentMapLabelPtrIndex.setStatus(_A)
_MplsInSegmentMapIndex_Type=MplsIndexType
_MplsInSegmentMapIndex_Object=MibTableColumn
mplsInSegmentMapIndex=_MplsInSegmentMapIndex_Object((1,3,6,1,2,1,10,166,2,1,14,1,4),_MplsInSegmentMapIndex_Type())
mplsInSegmentMapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsInSegmentMapIndex.setStatus(_A)
class _MplsXCNotificationsEnable_Type(TruthValue):defaultValue=2
_MplsXCNotificationsEnable_Type.__name__=_N
_MplsXCNotificationsEnable_Object=MibScalar
mplsXCNotificationsEnable=_MplsXCNotificationsEnable_Object((1,3,6,1,2,1,10,166,2,1,15),_MplsXCNotificationsEnable_Type())
mplsXCNotificationsEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:mplsXCNotificationsEnable.setStatus(_A)
_MplsLsrConformance_ObjectIdentity=ObjectIdentity
mplsLsrConformance=_MplsLsrConformance_ObjectIdentity((1,3,6,1,2,1,10,166,2,2))
_MplsLsrGroups_ObjectIdentity=ObjectIdentity
mplsLsrGroups=_MplsLsrGroups_ObjectIdentity((1,3,6,1,2,1,10,166,2,2,1))
_MplsLsrCompliances_ObjectIdentity=ObjectIdentity
mplsLsrCompliances=_MplsLsrCompliances_ObjectIdentity((1,3,6,1,2,1,10,166,2,2,2))
mplsInterfaceEntry.registerAugmentions((_B,_n))
mplsInterfacePerfEntry.setIndexNames(*mplsInterfaceEntry.getIndexNames())
mplsInSegmentEntry.registerAugmentions((_B,_o))
mplsInSegmentPerfEntry.setIndexNames(*mplsInSegmentEntry.getIndexNames())
mplsOutSegmentEntry.registerAugmentions((_B,_p))
mplsOutSegmentPerfEntry.setIndexNames(*mplsOutSegmentEntry.getIndexNames())
mplsInterfaceGroup=ObjectGroup((1,3,6,1,2,1,10,166,2,2,1,1))
mplsInterfaceGroup.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:mplsInterfaceGroup.setStatus(_A)
mplsInSegmentGroup=ObjectGroup((1,3,6,1,2,1,10,166,2,2,1,2))
mplsInSegmentGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:mplsInSegmentGroup.setStatus(_A)
mplsOutSegmentGroup=ObjectGroup((1,3,6,1,2,1,10,166,2,2,1,3))
mplsOutSegmentGroup.setObjects(*((_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_O),(_B,_P),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:mplsOutSegmentGroup.setStatus(_A)
mplsXCGroup=ObjectGroup((1,3,6,1,2,1,10,166,2,2,1,4))
mplsXCGroup.setObjects(*((_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_G),(_B,_AS),(_B,_AT)))
if mibBuilder.loadTexts:mplsXCGroup.setStatus(_A)
mplsPerfGroup=ObjectGroup((1,3,6,1,2,1,10,166,2,2,1,5))
mplsPerfGroup.setObjects(*((_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_O),(_B,_AZ),(_B,_P),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae)))
if mibBuilder.loadTexts:mplsPerfGroup.setStatus(_A)
mplsHCInSegmentPerfGroup=ObjectGroup((1,3,6,1,2,1,10,166,2,2,1,6))
mplsHCInSegmentPerfGroup.setObjects((_B,_Af))
if mibBuilder.loadTexts:mplsHCInSegmentPerfGroup.setStatus(_A)
mplsHCOutSegmentPerfGroup=ObjectGroup((1,3,6,1,2,1,10,166,2,2,1,7))
mplsHCOutSegmentPerfGroup.setObjects((_B,_Ag))
if mibBuilder.loadTexts:mplsHCOutSegmentPerfGroup.setStatus(_A)
mplsLabelStackGroup=ObjectGroup((1,3,6,1,2,1,10,166,2,2,1,8))
mplsLabelStackGroup.setObjects(*((_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am)))
if mibBuilder.loadTexts:mplsLabelStackGroup.setStatus(_A)
mplsXCUp=NotificationType((1,3,6,1,2,1,10,166,2,0,1))
mplsXCUp.setObjects(*((_B,_G),(_B,_G)))
if mibBuilder.loadTexts:mplsXCUp.setStatus(_A)
mplsXCDown=NotificationType((1,3,6,1,2,1,10,166,2,0,2))
mplsXCDown.setObjects(*((_B,_G),(_B,_G)))
if mibBuilder.loadTexts:mplsXCDown.setStatus(_A)
mplsLsrNotificationGroup=NotificationGroup((1,3,6,1,2,1,10,166,2,2,1,9))
mplsLsrNotificationGroup.setObjects(*((_B,'mplsXCUp'),(_B,_An)))
if mibBuilder.loadTexts:mplsLsrNotificationGroup.setStatus(_A)
mplsLsrModuleFullCompliance=ModuleCompliance((1,3,6,1,2,1,10,166,2,2,2,1))
mplsLsrModuleFullCompliance.setObjects(*((_H,_L),(_H,_K),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:mplsLsrModuleFullCompliance.setStatus(_A)
mplsLsrModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,10,166,2,2,2,2))
mplsLsrModuleReadOnlyCompliance.setObjects(*((_H,_L),(_H,_K),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:mplsLsrModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'MplsIndexType':MplsIndexType,'MplsIndexNextType':MplsIndexNextType,'mplsLsrStdMIB':mplsLsrStdMIB,'mplsLsrNotifications':mplsLsrNotifications,'mplsXCUp':mplsXCUp,_An:mplsXCDown,'mplsLsrObjects':mplsLsrObjects,'mplsInterfaceTable':mplsInterfaceTable,'mplsInterfaceEntry':mplsInterfaceEntry,_b:mplsInterfaceIndex,_q:mplsInterfaceLabelMinIn,_r:mplsInterfaceLabelMaxIn,_s:mplsInterfaceLabelMinOut,_t:mplsInterfaceLabelMaxOut,_u:mplsInterfaceTotalBandwidth,_v:mplsInterfaceAvailableBandwidth,_w:mplsInterfaceLabelParticipationType,'mplsInterfacePerfTable':mplsInterfacePerfTable,_n:mplsInterfacePerfEntry,_Ab:mplsInterfacePerfInLabelsInUse,_Ac:mplsInterfacePerfInLabelLookupFailures,_Ae:mplsInterfacePerfOutLabelsInUse,_Ad:mplsInterfacePerfOutFragmentedPkts,_x:mplsInSegmentIndexNext,'mplsInSegmentTable':mplsInSegmentTable,'mplsInSegmentEntry':mplsInSegmentEntry,_c:mplsInSegmentIndex,_y:mplsInSegmentInterface,_z:mplsInSegmentLabel,_A0:mplsInSegmentLabelPtr,_A1:mplsInSegmentNPop,_A2:mplsInSegmentAddrFamily,_A3:mplsInSegmentXCIndex,_A4:mplsInSegmentOwner,_A7:mplsInSegmentTrafficParamPtr,_A5:mplsInSegmentRowStatus,_A6:mplsInSegmentStorageType,'mplsInSegmentPerfTable':mplsInSegmentPerfTable,_o:mplsInSegmentPerfEntry,_AU:mplsInSegmentPerfOctets,_AV:mplsInSegmentPerfPackets,_AW:mplsInSegmentPerfErrors,_AX:mplsInSegmentPerfDiscards,_Af:mplsInSegmentPerfHCOctets,_AY:mplsInSegmentPerfDiscontinuityTime,_A9:mplsOutSegmentIndexNext,'mplsOutSegmentTable':mplsOutSegmentTable,'mplsOutSegmentEntry':mplsOutSegmentEntry,_d:mplsOutSegmentIndex,_AA:mplsOutSegmentInterface,_AB:mplsOutSegmentPushTopLabel,_AC:mplsOutSegmentTopLabel,_AD:mplsOutSegmentTopLabelPtr,_AE:mplsOutSegmentNextHopAddrType,_AF:mplsOutSegmentNextHopAddr,_AG:mplsOutSegmentXCIndex,_AH:mplsOutSegmentOwner,_AL:mplsOutSegmentTrafficParamPtr,_AJ:mplsOutSegmentRowStatus,_AK:mplsOutSegmentStorageType,'mplsOutSegmentPerfTable':mplsOutSegmentPerfTable,_p:mplsOutSegmentPerfEntry,_O:mplsOutSegmentPerfOctets,_AZ:mplsOutSegmentPerfPackets,_AI:mplsOutSegmentPerfErrors,_P:mplsOutSegmentPerfDiscards,_Ag:mplsOutSegmentPerfHCOctets,_Aa:mplsOutSegmentPerfDiscontinuityTime,_AM:mplsXCIndexNext,'mplsXCTable':mplsXCTable,'mplsXCEntry':mplsXCEntry,_e:mplsXCIndex,_f:mplsXCInSegmentIndex,_g:mplsXCOutSegmentIndex,_AN:mplsXCLspId,_AO:mplsXCLabelStackIndex,_AP:mplsXCOwner,_AS:mplsXCRowStatus,_AQ:mplsXCStorageType,_AR:mplsXCAdminStatus,_G:mplsXCOperStatus,_Al:mplsMaxLabelStackDepth,_Am:mplsLabelStackIndexNext,'mplsLabelStackTable':mplsLabelStackTable,'mplsLabelStackEntry':mplsLabelStackEntry,_i:mplsLabelStackIndex,_j:mplsLabelStackLabelIndex,_Ah:mplsLabelStackLabel,_Ai:mplsLabelStackLabelPtr,_Aj:mplsLabelStackRowStatus,_Ak:mplsLabelStackStorageType,'mplsInSegmentMapTable':mplsInSegmentMapTable,'mplsInSegmentMapEntry':mplsInSegmentMapEntry,_k:mplsInSegmentMapInterface,_l:mplsInSegmentMapLabel,_m:mplsInSegmentMapLabelPtrIndex,_A8:mplsInSegmentMapIndex,_AT:mplsXCNotificationsEnable,'mplsLsrConformance':mplsLsrConformance,'mplsLsrGroups':mplsLsrGroups,_Q:mplsInterfaceGroup,_R:mplsInSegmentGroup,_S:mplsOutSegmentGroup,_T:mplsXCGroup,_U:mplsPerfGroup,_W:mplsHCInSegmentPerfGroup,_X:mplsHCOutSegmentPerfGroup,_V:mplsLabelStackGroup,_Y:mplsLsrNotificationGroup,'mplsLsrCompliances':mplsLsrCompliances,'mplsLsrModuleFullCompliance':mplsLsrModuleFullCompliance,'mplsLsrModuleReadOnlyCompliance':mplsLsrModuleReadOnlyCompliance})