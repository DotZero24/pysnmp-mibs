_BT='mplsLspGroupV5'
_BS='mplsNodeGroupV5'
_BR='mplsLspGroupV2'
_BQ='mplsNodeGroupV2'
_BP='mplsLspGroupV1'
_BO='mplsNodeGroupV1'
_BN='mplsLspCreateBFDAdvanced'
_BM='mplsNodeCreateXCAdvanced'
_BL='mplsNodeCreateBfdTemplate'
_BK='mplsNodeCreatePwEnet'
_BJ='mplsNodeCreatePwMpls'
_BI='mplsNodeCreatePwGeneric'
_BH='mplsNodeCreateLspAdvanced'
_BG='mplsNodeCreateTunnelAdvanced'
_BF='mplsIfLagId'
_BE='mplsIfResourceType'
_BD='mplsIfIfNo'
_BC='mplsTunnelDescr'
_BB='mplsTnlXLspRowStatus'
_BA='mplsTnlXLspLspId'
_B9='mplsTnlXLspTunnelId'
_B8='mplsTnlXLspInternalReference'
_B7='mplsTnlXLspName'
_B6='mplsXCRowStatus'
_B5='mplsXCOutSegmentLabel'
_B4='mplsXCOutSegmentIfName'
_B3='mplsXCOutSegmentIfIndex'
_B2='mplsXCInSegmentLabel'
_B1='mplsXCInSegmentIfName'
_B0='mplsXCInSegmentIfIndex'
_A_='mplsXCIdentifier'
_Az='mplsXCInternalReference'
_Ay='mplsXCName'
_Ax='mplsGeneralMplsTnlXLspTableSize'
_Aw='mplsGeneralMplsLspTableSize'
_Av='mplsGeneralMplsTunnelTableSize'
_Au='mplsGeneralMplsXCTableSize'
_At='mplsGeneralMplsIfTableSize'
_As='mplsGeneralStateLastChangeTime'
_Ar='mplsGeneralLastChangeTime'
_Aq='MgmtNameString'
_Ap='OctetString'
_Ao='mplsIfGroupV2'
_An='mplsLspGroupV4'
_Am='mplsNodeGroupV3'
_Al='mplsTunnelGroupV2'
_Ak='mplsLspDescr'
_Aj='mplsNodeCreateLsp2'
_Ai='mplsTunnelBookedBW'
_Ah='mplsTunnelReservedBW'
_Ag='mplsIfRowStatus'
_Af='mplsIfVlan'
_Ae='mplsIfInterfaceMacAddress'
_Ad='mplsIfNextHopMacAddress'
_Ac='mplsIfIdentifier'
_Ab='mplsIfAdminStatus'
_Aa='mplsIfInternalReference'
_AZ='mplsIfPortName'
_AY='mplsIfPortIndex'
_AX='mplsIfTxPort'
_AW='mplsIfSlot'
_AV='mplsIfSubrack'
_AU='mplsIfName'
_AT='mplsTnlXLspIndex'
_AS='MplsIdentifier'
_AR='unknown'
_AQ='mplsXCIndex'
_AP='PortNumber'
_AO='mplsTunnelGroupV4'
_AN='mplsNodeGroupV4'
_AM='mplsLspGroupV3'
_AL='mplsTunnelGroupV3'
_AK='mplsLspReservedBW'
_AJ='mplsNodeCreateMsPw'
_AI='mplsTunnelProtectionLSP'
_AH='mplsTunnelWorkingLSP'
_AG='mplsTunnelDestGlobalId'
_AF='mplsTunnelGlobalId'
_AE='mplsTunnelAssociateLinearProt'
_AD='mplsTunnelProtectionState'
_AC='mplsTunnelLinearProtection'
_AB='mplsIfIndex'
_AA='mplsLspDestGlobalId'
_A9='mplsLspGlobalId'
_A8='mplsLspTrafficClass'
_A7='mplsLspCreateBFD'
_A6='mplsLspBFDSession'
_A5='mplsNodeLPRapidMsgInterval'
_A4='mplsNodeLPContMsgInterval'
_A3='mplsNodeLinearProtWtrTimer'
_A2='mplsNodeLinearProtMode'
_A1='mplsTunnelRowStatus'
_A0='mplsTunnelAssociateLSP'
_z='mplsTunnelExtId'
_y='mplsTunnelDestTunnelId'
_x='mplsTunnelDestNodeId'
_w='mplsTunnelSrcTunnelId'
_v='mplsTunnelSrcNodeId'
_u='mplsTunnelActiveLspIndex'
_t='mplsTunnelActiveLSP'
_s='mplsTunnelName'
_r='mplsTunnelIdentifier'
_q='mplsTunnelInternalReference'
_p='mplsLspRowStatus'
_o='mplsLspIntTunnelId'
_n='mplsLspExtId'
_m='mplsLspLspId'
_l='mplsLspDestTunnelId'
_k='mplsLspSrcTunnelId'
_j='mplsLspDestNodeId'
_i='mplsLspSrcNodeId'
_h='mplsLspPriority'
_g='mplsLspReverseXCId'
_f='mplsLspForwardXCId'
_e='mplsLspRole'
_d='mplsLspState'
_c='mplsLspIdentifier'
_b='mplsLspInternalReference'
_a='mplsLspName'
_Z='mplsNodeCreateIf'
_Y='mplsNodeCreatePw'
_X='mplsNodeCreateLsp'
_W='mplsNodeCreateTunnel'
_V='mplsNodeCreateXC'
_U='mplsNodeIdNum'
_T='mplsNodeIccIdStr'
_S='mplsNodeSlot'
_R='mplsNodeSubrack'
_Q='mplsNodeName'
_P='mplsTunnelIndex'
_O='mplsIfGroupV1'
_N='mplsLspIndex'
_M='mplsNodeIndex'
_L='mplsTnlXLspV1'
_K='mplsXCGroupV1'
_J='mplsGeneralGroupV1'
_I='Integer32'
_H='DisplayString'
_G='deprecated'
_F='read-write'
_E='Unsigned32'
_D='read-create'
_C='read-only'
_B='current'
_A='LUM-MPLS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Ap,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumModules,lumMplsMIB=mibBuilder.importSymbols('LUM-REG','lumModules','lumMplsMIB')
CommandString,MgmtNameString,MplsLabel,PortNumber=mibBuilder.importSymbols('LUM-TC','CommandString',_Aq,'MplsLabel',_AP)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_H,'MacAddress','PhysAddress','RowStatus','TextualConvention')
lumMplsMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,40))
if mibBuilder.loadTexts:lumMplsMIBModule.setRevisions(('2017-06-15 00:00','2016-11-30 00:00','2015-01-23 00:00','2013-10-11 00:00','2013-04-01 00:00','2012-12-20 00:00','2012-03-01 00:00','2011-12-20 00:00'))
class MplsIdentifier(TextualConvention,Unsigned32):status=_B;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LumMplsConfs_ObjectIdentity=ObjectIdentity
lumMplsConfs=_LumMplsConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,40,1))
_LumMplsGroups_ObjectIdentity=ObjectIdentity
lumMplsGroups=_LumMplsGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,40,1,1))
_LumMplsCompl_ObjectIdentity=ObjectIdentity
lumMplsCompl=_LumMplsCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,40,1,2))
_LumMplsMIBObjects_ObjectIdentity=ObjectIdentity
lumMplsMIBObjects=_LumMplsMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,40,2))
_MplsGeneral_ObjectIdentity=ObjectIdentity
mplsGeneral=_MplsGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,40,2,1))
_MplsGeneralLastChangeTime_Type=DateAndTime
_MplsGeneralLastChangeTime_Object=MibScalar
mplsGeneralLastChangeTime=_MplsGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,40,2,1,1),_MplsGeneralLastChangeTime_Type())
mplsGeneralLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsGeneralLastChangeTime.setStatus(_B)
_MplsGeneralStateLastChangeTime_Type=DateAndTime
_MplsGeneralStateLastChangeTime_Object=MibScalar
mplsGeneralStateLastChangeTime=_MplsGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,40,2,1,2),_MplsGeneralStateLastChangeTime_Type())
mplsGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsGeneralStateLastChangeTime.setStatus(_B)
_MplsGeneralMplsIfTableSize_Type=Unsigned32
_MplsGeneralMplsIfTableSize_Object=MibScalar
mplsGeneralMplsIfTableSize=_MplsGeneralMplsIfTableSize_Object((1,3,6,1,4,1,8708,2,40,2,1,3),_MplsGeneralMplsIfTableSize_Type())
mplsGeneralMplsIfTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsGeneralMplsIfTableSize.setStatus(_B)
_MplsGeneralMplsXCTableSize_Type=Unsigned32
_MplsGeneralMplsXCTableSize_Object=MibScalar
mplsGeneralMplsXCTableSize=_MplsGeneralMplsXCTableSize_Object((1,3,6,1,4,1,8708,2,40,2,1,4),_MplsGeneralMplsXCTableSize_Type())
mplsGeneralMplsXCTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsGeneralMplsXCTableSize.setStatus(_B)
_MplsGeneralMplsTunnelTableSize_Type=Unsigned32
_MplsGeneralMplsTunnelTableSize_Object=MibScalar
mplsGeneralMplsTunnelTableSize=_MplsGeneralMplsTunnelTableSize_Object((1,3,6,1,4,1,8708,2,40,2,1,5),_MplsGeneralMplsTunnelTableSize_Type())
mplsGeneralMplsTunnelTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsGeneralMplsTunnelTableSize.setStatus(_B)
_MplsGeneralMplsNodeTableSize_Type=Unsigned32
_MplsGeneralMplsNodeTableSize_Object=MibScalar
mplsGeneralMplsNodeTableSize=_MplsGeneralMplsNodeTableSize_Object((1,3,6,1,4,1,8708,2,40,2,1,6),_MplsGeneralMplsNodeTableSize_Type())
mplsGeneralMplsNodeTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsGeneralMplsNodeTableSize.setStatus(_B)
_MplsGeneralMplsLspTableSize_Type=Unsigned32
_MplsGeneralMplsLspTableSize_Object=MibScalar
mplsGeneralMplsLspTableSize=_MplsGeneralMplsLspTableSize_Object((1,3,6,1,4,1,8708,2,40,2,1,7),_MplsGeneralMplsLspTableSize_Type())
mplsGeneralMplsLspTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsGeneralMplsLspTableSize.setStatus(_B)
_MplsGeneralMplsTnlXLspTableSize_Type=Unsigned32
_MplsGeneralMplsTnlXLspTableSize_Object=MibScalar
mplsGeneralMplsTnlXLspTableSize=_MplsGeneralMplsTnlXLspTableSize_Object((1,3,6,1,4,1,8708,2,40,2,1,8),_MplsGeneralMplsTnlXLspTableSize_Type())
mplsGeneralMplsTnlXLspTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsGeneralMplsTnlXLspTableSize.setStatus(_B)
_MplsIfList_ObjectIdentity=ObjectIdentity
mplsIfList=_MplsIfList_ObjectIdentity((1,3,6,1,4,1,8708,2,40,2,2))
_MplsIfTable_Object=MibTable
mplsIfTable=_MplsIfTable_Object((1,3,6,1,4,1,8708,2,40,2,2,1))
if mibBuilder.loadTexts:mplsIfTable.setStatus(_B)
_MplsIfEntry_Object=MibTableRow
mplsIfEntry=_MplsIfEntry_Object((1,3,6,1,4,1,8708,2,40,2,2,1,1))
mplsIfEntry.setIndexNames((0,_A,_AB))
if mibBuilder.loadTexts:mplsIfEntry.setStatus(_B)
class _MplsIfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsIfIndex_Type.__name__=_E
_MplsIfIndex_Object=MibTableColumn
mplsIfIndex=_MplsIfIndex_Object((1,3,6,1,4,1,8708,2,40,2,2,1,1,1),_MplsIfIndex_Type())
mplsIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsIfIndex.setStatus(_B)
_MplsIfName_Type=MgmtNameString
_MplsIfName_Object=MibTableColumn
mplsIfName=_MplsIfName_Object((1,3,6,1,4,1,8708,2,40,2,2,1,1,2),_MplsIfName_Type())
mplsIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsIfName.setStatus(_B)
class _MplsIfSubrack_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsIfSubrack_Type.__name__=_E
_MplsIfSubrack_Object=MibTableColumn
mplsIfSubrack=_MplsIfSubrack_Object((1,3,6,1,4,1,8708,2,40,2,2,1,1,3),_MplsIfSubrack_Type())
mplsIfSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsIfSubrack.setStatus(_B)
class _MplsIfSlot_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsIfSlot_Type.__name__=_E
_MplsIfSlot_Object=MibTableColumn
mplsIfSlot=_MplsIfSlot_Object((1,3,6,1,4,1,8708,2,40,2,2,1,1,4),_MplsIfSlot_Type())
mplsIfSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsIfSlot.setStatus(_B)
class _MplsIfTxPort_Type(PortNumber):defaultValue=0
_MplsIfTxPort_Type.__name__=_AP
_MplsIfTxPort_Object=MibTableColumn
mplsIfTxPort=_MplsIfTxPort_Object((1,3,6,1,4,1,8708,2,40,2,2,1,1,5),_MplsIfTxPort_Type())
mplsIfTxPort.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsIfTxPort.setStatus(_B)
class _MplsIfPortIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsIfPortIndex_Type.__name__=_E
_MplsIfPortIndex_Object=MibTableColumn
mplsIfPortIndex=_MplsIfPortIndex_Object((1,3,6,1,4,1,8708,2,40,2,2,1,1,6),_MplsIfPortIndex_Type())
mplsIfPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsIfPortIndex.setStatus(_B)
_MplsIfPortName_Type=DisplayString
_MplsIfPortName_Object=MibTableColumn
mplsIfPortName=_MplsIfPortName_Object((1,3,6,1,4,1,8708,2,40,2,2,1,1,7),_MplsIfPortName_Type())
mplsIfPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsIfPortName.setStatus(_B)
class _MplsIfInternalReference_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsIfInternalReference_Type.__name__=_E
_MplsIfInternalReference_Object=MibTableColumn
mplsIfInternalReference=_MplsIfInternalReference_Object((1,3,6,1,4,1,8708,2,40,2,2,1,1,8),_MplsIfInternalReference_Type())
mplsIfInternalReference.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsIfInternalReference.setStatus(_B)
class _MplsIfAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
_MplsIfAdminStatus_Type.__name__=_I
_MplsIfAdminStatus_Object=MibTableColumn
mplsIfAdminStatus=_MplsIfAdminStatus_Object((1,3,6,1,4,1,8708,2,40,2,2,1,1,9),_MplsIfAdminStatus_Type())
mplsIfAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsIfAdminStatus.setStatus(_B)
class _MplsIfIdentifier_Type(DisplayString):defaultValue=OctetString('')
_MplsIfIdentifier_Type.__name__=_H
_MplsIfIdentifier_Object=MibTableColumn
mplsIfIdentifier=_MplsIfIdentifier_Object((1,3,6,1,4,1,8708,2,40,2,2,1,1,10),_MplsIfIdentifier_Type())
mplsIfIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsIfIdentifier.setStatus(_B)
_MplsIfNextHopMacAddress_Type=MacAddress
_MplsIfNextHopMacAddress_Object=MibTableColumn
mplsIfNextHopMacAddress=_MplsIfNextHopMacAddress_Object((1,3,6,1,4,1,8708,2,40,2,2,1,1,11),_MplsIfNextHopMacAddress_Type())
mplsIfNextHopMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsIfNextHopMacAddress.setStatus(_B)
_MplsIfInterfaceMacAddress_Type=MacAddress
_MplsIfInterfaceMacAddress_Object=MibTableColumn
mplsIfInterfaceMacAddress=_MplsIfInterfaceMacAddress_Object((1,3,6,1,4,1,8708,2,40,2,2,1,1,12),_MplsIfInterfaceMacAddress_Type())
mplsIfInterfaceMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsIfInterfaceMacAddress.setStatus(_B)
class _MplsIfVlan_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_MplsIfVlan_Type.__name__=_E
_MplsIfVlan_Object=MibTableColumn
mplsIfVlan=_MplsIfVlan_Object((1,3,6,1,4,1,8708,2,40,2,2,1,1,13),_MplsIfVlan_Type())
mplsIfVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsIfVlan.setStatus(_B)
_MplsIfRowStatus_Type=RowStatus
_MplsIfRowStatus_Object=MibTableColumn
mplsIfRowStatus=_MplsIfRowStatus_Object((1,3,6,1,4,1,8708,2,40,2,2,1,1,14),_MplsIfRowStatus_Type())
mplsIfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsIfRowStatus.setStatus(_B)
class _MplsIfIfNo_Type(PortNumber):defaultValue=1
_MplsIfIfNo_Type.__name__=_AP
_MplsIfIfNo_Object=MibTableColumn
mplsIfIfNo=_MplsIfIfNo_Object((1,3,6,1,4,1,8708,2,40,2,2,1,1,15),_MplsIfIfNo_Type())
mplsIfIfNo.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsIfIfNo.setStatus(_B)
class _MplsIfResourceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('port',1),('lag',2)))
_MplsIfResourceType_Type.__name__=_I
_MplsIfResourceType_Object=MibTableColumn
mplsIfResourceType=_MplsIfResourceType_Object((1,3,6,1,4,1,8708,2,40,2,2,1,1,16),_MplsIfResourceType_Type())
mplsIfResourceType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsIfResourceType.setStatus(_B)
class _MplsIfLagId_Type(MgmtNameString):defaultValue=OctetString('')
_MplsIfLagId_Type.__name__=_Aq
_MplsIfLagId_Object=MibTableColumn
mplsIfLagId=_MplsIfLagId_Object((1,3,6,1,4,1,8708,2,40,2,2,1,1,17),_MplsIfLagId_Type())
mplsIfLagId.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsIfLagId.setStatus(_B)
_MplsXCList_ObjectIdentity=ObjectIdentity
mplsXCList=_MplsXCList_ObjectIdentity((1,3,6,1,4,1,8708,2,40,2,3))
_MplsXCTable_Object=MibTable
mplsXCTable=_MplsXCTable_Object((1,3,6,1,4,1,8708,2,40,2,3,1))
if mibBuilder.loadTexts:mplsXCTable.setStatus(_B)
_MplsXCEntry_Object=MibTableRow
mplsXCEntry=_MplsXCEntry_Object((1,3,6,1,4,1,8708,2,40,2,3,1,1))
mplsXCEntry.setIndexNames((0,_A,_AQ))
if mibBuilder.loadTexts:mplsXCEntry.setStatus(_B)
class _MplsXCIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsXCIndex_Type.__name__=_E
_MplsXCIndex_Object=MibTableColumn
mplsXCIndex=_MplsXCIndex_Object((1,3,6,1,4,1,8708,2,40,2,3,1,1,1),_MplsXCIndex_Type())
mplsXCIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsXCIndex.setStatus(_B)
_MplsXCName_Type=MgmtNameString
_MplsXCName_Object=MibTableColumn
mplsXCName=_MplsXCName_Object((1,3,6,1,4,1,8708,2,40,2,3,1,1,2),_MplsXCName_Type())
mplsXCName.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsXCName.setStatus(_B)
class _MplsXCInternalReference_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsXCInternalReference_Type.__name__=_E
_MplsXCInternalReference_Object=MibTableColumn
mplsXCInternalReference=_MplsXCInternalReference_Object((1,3,6,1,4,1,8708,2,40,2,3,1,1,3),_MplsXCInternalReference_Type())
mplsXCInternalReference.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCInternalReference.setStatus(_B)
class _MplsXCIdentifier_Type(DisplayString):defaultValue=OctetString('')
_MplsXCIdentifier_Type.__name__=_H
_MplsXCIdentifier_Object=MibTableColumn
mplsXCIdentifier=_MplsXCIdentifier_Object((1,3,6,1,4,1,8708,2,40,2,3,1,1,4),_MplsXCIdentifier_Type())
mplsXCIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCIdentifier.setStatus(_B)
class _MplsXCInSegmentIfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsXCInSegmentIfIndex_Type.__name__=_E
_MplsXCInSegmentIfIndex_Object=MibTableColumn
mplsXCInSegmentIfIndex=_MplsXCInSegmentIfIndex_Object((1,3,6,1,4,1,8708,2,40,2,3,1,1,5),_MplsXCInSegmentIfIndex_Type())
mplsXCInSegmentIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCInSegmentIfIndex.setStatus(_B)
_MplsXCInSegmentIfName_Type=DisplayString
_MplsXCInSegmentIfName_Object=MibTableColumn
mplsXCInSegmentIfName=_MplsXCInSegmentIfName_Object((1,3,6,1,4,1,8708,2,40,2,3,1,1,6),_MplsXCInSegmentIfName_Type())
mplsXCInSegmentIfName.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCInSegmentIfName.setStatus(_B)
_MplsXCInSegmentLabel_Type=MplsLabel
_MplsXCInSegmentLabel_Object=MibTableColumn
mplsXCInSegmentLabel=_MplsXCInSegmentLabel_Object((1,3,6,1,4,1,8708,2,40,2,3,1,1,7),_MplsXCInSegmentLabel_Type())
mplsXCInSegmentLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCInSegmentLabel.setStatus(_B)
class _MplsXCOutSegmentIfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsXCOutSegmentIfIndex_Type.__name__=_E
_MplsXCOutSegmentIfIndex_Object=MibTableColumn
mplsXCOutSegmentIfIndex=_MplsXCOutSegmentIfIndex_Object((1,3,6,1,4,1,8708,2,40,2,3,1,1,8),_MplsXCOutSegmentIfIndex_Type())
mplsXCOutSegmentIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCOutSegmentIfIndex.setStatus(_B)
_MplsXCOutSegmentIfName_Type=DisplayString
_MplsXCOutSegmentIfName_Object=MibTableColumn
mplsXCOutSegmentIfName=_MplsXCOutSegmentIfName_Object((1,3,6,1,4,1,8708,2,40,2,3,1,1,9),_MplsXCOutSegmentIfName_Type())
mplsXCOutSegmentIfName.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCOutSegmentIfName.setStatus(_B)
_MplsXCOutSegmentLabel_Type=MplsLabel
_MplsXCOutSegmentLabel_Object=MibTableColumn
mplsXCOutSegmentLabel=_MplsXCOutSegmentLabel_Object((1,3,6,1,4,1,8708,2,40,2,3,1,1,10),_MplsXCOutSegmentLabel_Type())
mplsXCOutSegmentLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCOutSegmentLabel.setStatus(_B)
_MplsXCRowStatus_Type=RowStatus
_MplsXCRowStatus_Object=MibTableColumn
mplsXCRowStatus=_MplsXCRowStatus_Object((1,3,6,1,4,1,8708,2,40,2,3,1,1,11),_MplsXCRowStatus_Type())
mplsXCRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsXCRowStatus.setStatus(_B)
_MplsTunnelList_ObjectIdentity=ObjectIdentity
mplsTunnelList=_MplsTunnelList_ObjectIdentity((1,3,6,1,4,1,8708,2,40,2,4))
_MplsTunnelTable_Object=MibTable
mplsTunnelTable=_MplsTunnelTable_Object((1,3,6,1,4,1,8708,2,40,2,4,1))
if mibBuilder.loadTexts:mplsTunnelTable.setStatus(_B)
_MplsTunnelEntry_Object=MibTableRow
mplsTunnelEntry=_MplsTunnelEntry_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1))
mplsTunnelEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:mplsTunnelEntry.setStatus(_B)
class _MplsTunnelIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsTunnelIndex_Type.__name__=_E
_MplsTunnelIndex_Object=MibTableColumn
mplsTunnelIndex=_MplsTunnelIndex_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1,1),_MplsTunnelIndex_Type())
mplsTunnelIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelIndex.setStatus(_B)
class _MplsTunnelInternalReference_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsTunnelInternalReference_Type.__name__=_E
_MplsTunnelInternalReference_Object=MibTableColumn
mplsTunnelInternalReference=_MplsTunnelInternalReference_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1,2),_MplsTunnelInternalReference_Type())
mplsTunnelInternalReference.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelInternalReference.setStatus(_B)
class _MplsTunnelIdentifier_Type(DisplayString):defaultValue=OctetString('')
_MplsTunnelIdentifier_Type.__name__=_H
_MplsTunnelIdentifier_Object=MibTableColumn
mplsTunnelIdentifier=_MplsTunnelIdentifier_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1,3),_MplsTunnelIdentifier_Type())
mplsTunnelIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelIdentifier.setStatus(_B)
_MplsTunnelName_Type=MgmtNameString
_MplsTunnelName_Object=MibTableColumn
mplsTunnelName=_MplsTunnelName_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1,4),_MplsTunnelName_Type())
mplsTunnelName.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelName.setStatus(_B)
class _MplsTunnelActiveLSP_Type(DisplayString):defaultValue=OctetString('')
_MplsTunnelActiveLSP_Type.__name__=_H
_MplsTunnelActiveLSP_Object=MibTableColumn
mplsTunnelActiveLSP=_MplsTunnelActiveLSP_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1,5),_MplsTunnelActiveLSP_Type())
mplsTunnelActiveLSP.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelActiveLSP.setStatus(_B)
class _MplsTunnelActiveLspIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsTunnelActiveLspIndex_Type.__name__=_E
_MplsTunnelActiveLspIndex_Object=MibTableColumn
mplsTunnelActiveLspIndex=_MplsTunnelActiveLspIndex_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1,6),_MplsTunnelActiveLspIndex_Type())
mplsTunnelActiveLspIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelActiveLspIndex.setStatus(_B)
class _MplsTunnelState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('down',1),('up',2),(_AR,3)))
_MplsTunnelState_Type.__name__=_I
_MplsTunnelState_Object=MibTableColumn
mplsTunnelState=_MplsTunnelState_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1,7),_MplsTunnelState_Type())
mplsTunnelState.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelState.setStatus(_B)
class _MplsTunnelSrcNodeId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MplsTunnelSrcNodeId_Type.__name__=_E
_MplsTunnelSrcNodeId_Object=MibTableColumn
mplsTunnelSrcNodeId=_MplsTunnelSrcNodeId_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1,8),_MplsTunnelSrcNodeId_Type())
mplsTunnelSrcNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelSrcNodeId.setStatus(_B)
class _MplsTunnelSrcTunnelId_Type(MplsIdentifier):defaultValue=0
_MplsTunnelSrcTunnelId_Type.__name__=_AS
_MplsTunnelSrcTunnelId_Object=MibTableColumn
mplsTunnelSrcTunnelId=_MplsTunnelSrcTunnelId_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1,9),_MplsTunnelSrcTunnelId_Type())
mplsTunnelSrcTunnelId.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsTunnelSrcTunnelId.setStatus(_B)
class _MplsTunnelDestNodeId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MplsTunnelDestNodeId_Type.__name__=_E
_MplsTunnelDestNodeId_Object=MibTableColumn
mplsTunnelDestNodeId=_MplsTunnelDestNodeId_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1,10),_MplsTunnelDestNodeId_Type())
mplsTunnelDestNodeId.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsTunnelDestNodeId.setStatus(_B)
class _MplsTunnelDestTunnelId_Type(MplsIdentifier):defaultValue=0
_MplsTunnelDestTunnelId_Type.__name__=_AS
_MplsTunnelDestTunnelId_Object=MibTableColumn
mplsTunnelDestTunnelId=_MplsTunnelDestTunnelId_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1,11),_MplsTunnelDestTunnelId_Type())
mplsTunnelDestTunnelId.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsTunnelDestTunnelId.setStatus(_B)
_MplsTunnelExtId_Type=DisplayString
_MplsTunnelExtId_Object=MibTableColumn
mplsTunnelExtId=_MplsTunnelExtId_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1,12),_MplsTunnelExtId_Type())
mplsTunnelExtId.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelExtId.setStatus(_B)
_MplsTunnelAssociateLSP_Type=CommandString
_MplsTunnelAssociateLSP_Object=MibTableColumn
mplsTunnelAssociateLSP=_MplsTunnelAssociateLSP_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1,13),_MplsTunnelAssociateLSP_Type())
mplsTunnelAssociateLSP.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelAssociateLSP.setStatus(_B)
_MplsTunnelRowStatus_Type=RowStatus
_MplsTunnelRowStatus_Object=MibTableColumn
mplsTunnelRowStatus=_MplsTunnelRowStatus_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1,14),_MplsTunnelRowStatus_Type())
mplsTunnelRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelRowStatus.setStatus(_B)
class _MplsTunnelLinearProtection_Type(DisplayString):defaultValue=OctetString('none')
_MplsTunnelLinearProtection_Type.__name__=_H
_MplsTunnelLinearProtection_Object=MibTableColumn
mplsTunnelLinearProtection=_MplsTunnelLinearProtection_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1,15),_MplsTunnelLinearProtection_Type())
mplsTunnelLinearProtection.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTunnelLinearProtection.setStatus(_B)
class _MplsTunnelProtectionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('fullyworking',1),('degraded',2),('failed',3),(_AR,4)))
_MplsTunnelProtectionState_Type.__name__=_I
_MplsTunnelProtectionState_Object=MibTableColumn
mplsTunnelProtectionState=_MplsTunnelProtectionState_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1,16),_MplsTunnelProtectionState_Type())
mplsTunnelProtectionState.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelProtectionState.setStatus(_B)
_MplsTunnelAssociateLinearProt_Type=CommandString
_MplsTunnelAssociateLinearProt_Object=MibTableColumn
mplsTunnelAssociateLinearProt=_MplsTunnelAssociateLinearProt_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1,17),_MplsTunnelAssociateLinearProt_Type())
mplsTunnelAssociateLinearProt.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelAssociateLinearProt.setStatus(_B)
class _MplsTunnelGlobalId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MplsTunnelGlobalId_Type.__name__=_E
_MplsTunnelGlobalId_Object=MibTableColumn
mplsTunnelGlobalId=_MplsTunnelGlobalId_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1,18),_MplsTunnelGlobalId_Type())
mplsTunnelGlobalId.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelGlobalId.setStatus(_B)
class _MplsTunnelDestGlobalId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MplsTunnelDestGlobalId_Type.__name__=_E
_MplsTunnelDestGlobalId_Object=MibTableColumn
mplsTunnelDestGlobalId=_MplsTunnelDestGlobalId_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1,19),_MplsTunnelDestGlobalId_Type())
mplsTunnelDestGlobalId.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsTunnelDestGlobalId.setStatus(_B)
_MplsTunnelWorkingLSP_Type=DisplayString
_MplsTunnelWorkingLSP_Object=MibTableColumn
mplsTunnelWorkingLSP=_MplsTunnelWorkingLSP_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1,20),_MplsTunnelWorkingLSP_Type())
mplsTunnelWorkingLSP.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelWorkingLSP.setStatus(_B)
_MplsTunnelProtectionLSP_Type=DisplayString
_MplsTunnelProtectionLSP_Object=MibTableColumn
mplsTunnelProtectionLSP=_MplsTunnelProtectionLSP_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1,21),_MplsTunnelProtectionLSP_Type())
mplsTunnelProtectionLSP.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelProtectionLSP.setStatus(_B)
class _MplsTunnelReservedBW_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MplsTunnelReservedBW_Type.__name__=_E
_MplsTunnelReservedBW_Object=MibTableColumn
mplsTunnelReservedBW=_MplsTunnelReservedBW_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1,22),_MplsTunnelReservedBW_Type())
mplsTunnelReservedBW.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsTunnelReservedBW.setStatus(_B)
_MplsTunnelBookedBW_Type=Counter64
_MplsTunnelBookedBW_Object=MibTableColumn
mplsTunnelBookedBW=_MplsTunnelBookedBW_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1,23),_MplsTunnelBookedBW_Type())
mplsTunnelBookedBW.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTunnelBookedBW.setStatus(_B)
class _MplsTunnelDescr_Type(DisplayString):defaultValue=OctetString('')
_MplsTunnelDescr_Type.__name__=_H
_MplsTunnelDescr_Object=MibTableColumn
mplsTunnelDescr=_MplsTunnelDescr_Object((1,3,6,1,4,1,8708,2,40,2,4,1,1,24),_MplsTunnelDescr_Type())
mplsTunnelDescr.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsTunnelDescr.setStatus(_B)
_MplsNodeList_ObjectIdentity=ObjectIdentity
mplsNodeList=_MplsNodeList_ObjectIdentity((1,3,6,1,4,1,8708,2,40,2,5))
_MplsNodeTable_Object=MibTable
mplsNodeTable=_MplsNodeTable_Object((1,3,6,1,4,1,8708,2,40,2,5,1))
if mibBuilder.loadTexts:mplsNodeTable.setStatus(_B)
_MplsNodeEntry_Object=MibTableRow
mplsNodeEntry=_MplsNodeEntry_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1))
mplsNodeEntry.setIndexNames((0,_A,_M))
if mibBuilder.loadTexts:mplsNodeEntry.setStatus(_B)
class _MplsNodeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsNodeIndex_Type.__name__=_E
_MplsNodeIndex_Object=MibTableColumn
mplsNodeIndex=_MplsNodeIndex_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,1),_MplsNodeIndex_Type())
mplsNodeIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsNodeIndex.setStatus(_B)
_MplsNodeName_Type=MgmtNameString
_MplsNodeName_Object=MibTableColumn
mplsNodeName=_MplsNodeName_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,2),_MplsNodeName_Type())
mplsNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsNodeName.setStatus(_B)
class _MplsNodeSubrack_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsNodeSubrack_Type.__name__=_E
_MplsNodeSubrack_Object=MibTableColumn
mplsNodeSubrack=_MplsNodeSubrack_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,3),_MplsNodeSubrack_Type())
mplsNodeSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsNodeSubrack.setStatus(_B)
class _MplsNodeSlot_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsNodeSlot_Type.__name__=_E
_MplsNodeSlot_Object=MibTableColumn
mplsNodeSlot=_MplsNodeSlot_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,4),_MplsNodeSlot_Type())
mplsNodeSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsNodeSlot.setStatus(_B)
class _MplsNodeIccIdStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,6))
_MplsNodeIccIdStr_Type.__name__=_Ap
_MplsNodeIccIdStr_Object=MibTableColumn
mplsNodeIccIdStr=_MplsNodeIccIdStr_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,5),_MplsNodeIccIdStr_Type())
mplsNodeIccIdStr.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsNodeIccIdStr.setStatus(_B)
class _MplsNodeIdNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MplsNodeIdNum_Type.__name__=_E
_MplsNodeIdNum_Object=MibTableColumn
mplsNodeIdNum=_MplsNodeIdNum_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,6),_MplsNodeIdNum_Type())
mplsNodeIdNum.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsNodeIdNum.setStatus(_B)
_MplsNodeCreateXC_Type=CommandString
_MplsNodeCreateXC_Object=MibTableColumn
mplsNodeCreateXC=_MplsNodeCreateXC_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,7),_MplsNodeCreateXC_Type())
mplsNodeCreateXC.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsNodeCreateXC.setStatus(_B)
_MplsNodeCreateTunnel_Type=CommandString
_MplsNodeCreateTunnel_Object=MibTableColumn
mplsNodeCreateTunnel=_MplsNodeCreateTunnel_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,8),_MplsNodeCreateTunnel_Type())
mplsNodeCreateTunnel.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsNodeCreateTunnel.setStatus(_B)
_MplsNodeCreateLsp_Type=CommandString
_MplsNodeCreateLsp_Object=MibTableColumn
mplsNodeCreateLsp=_MplsNodeCreateLsp_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,9),_MplsNodeCreateLsp_Type())
mplsNodeCreateLsp.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsNodeCreateLsp.setStatus(_B)
_MplsNodeCreatePw_Type=CommandString
_MplsNodeCreatePw_Object=MibTableColumn
mplsNodeCreatePw=_MplsNodeCreatePw_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,10),_MplsNodeCreatePw_Type())
mplsNodeCreatePw.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsNodeCreatePw.setStatus(_B)
_MplsNodeCreateIf_Type=CommandString
_MplsNodeCreateIf_Object=MibTableColumn
mplsNodeCreateIf=_MplsNodeCreateIf_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,11),_MplsNodeCreateIf_Type())
mplsNodeCreateIf.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsNodeCreateIf.setStatus(_B)
class _MplsNodeLinearProtMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonRevertive',1),('revertive',2)))
_MplsNodeLinearProtMode_Type.__name__=_I
_MplsNodeLinearProtMode_Object=MibTableColumn
mplsNodeLinearProtMode=_MplsNodeLinearProtMode_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,12),_MplsNodeLinearProtMode_Type())
mplsNodeLinearProtMode.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsNodeLinearProtMode.setStatus(_B)
class _MplsNodeLinearProtWtrTimer_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,720))
_MplsNodeLinearProtWtrTimer_Type.__name__=_E
_MplsNodeLinearProtWtrTimer_Object=MibTableColumn
mplsNodeLinearProtWtrTimer=_MplsNodeLinearProtWtrTimer_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,13),_MplsNodeLinearProtWtrTimer_Type())
mplsNodeLinearProtWtrTimer.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsNodeLinearProtWtrTimer.setStatus(_B)
class _MplsNodeLPContMsgInterval_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_MplsNodeLPContMsgInterval_Type.__name__=_E
_MplsNodeLPContMsgInterval_Object=MibTableColumn
mplsNodeLPContMsgInterval=_MplsNodeLPContMsgInterval_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,14),_MplsNodeLPContMsgInterval_Type())
mplsNodeLPContMsgInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsNodeLPContMsgInterval.setStatus(_B)
class _MplsNodeLPRapidMsgInterval_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_MplsNodeLPRapidMsgInterval_Type.__name__=_E
_MplsNodeLPRapidMsgInterval_Object=MibTableColumn
mplsNodeLPRapidMsgInterval=_MplsNodeLPRapidMsgInterval_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,15),_MplsNodeLPRapidMsgInterval_Type())
mplsNodeLPRapidMsgInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsNodeLPRapidMsgInterval.setStatus(_B)
class _MplsNodeGlobalId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MplsNodeGlobalId_Type.__name__=_E
_MplsNodeGlobalId_Object=MibTableColumn
mplsNodeGlobalId=_MplsNodeGlobalId_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,16),_MplsNodeGlobalId_Type())
mplsNodeGlobalId.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsNodeGlobalId.setStatus(_B)
_MplsNodeCreateMsPw_Type=CommandString
_MplsNodeCreateMsPw_Object=MibTableColumn
mplsNodeCreateMsPw=_MplsNodeCreateMsPw_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,17),_MplsNodeCreateMsPw_Type())
mplsNodeCreateMsPw.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsNodeCreateMsPw.setStatus(_B)
_MplsNodeCreateLsp2_Type=CommandString
_MplsNodeCreateLsp2_Object=MibTableColumn
mplsNodeCreateLsp2=_MplsNodeCreateLsp2_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,18),_MplsNodeCreateLsp2_Type())
mplsNodeCreateLsp2.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsNodeCreateLsp2.setStatus(_B)
_MplsNodeCreateTunnelAdvanced_Type=CommandString
_MplsNodeCreateTunnelAdvanced_Object=MibTableColumn
mplsNodeCreateTunnelAdvanced=_MplsNodeCreateTunnelAdvanced_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,19),_MplsNodeCreateTunnelAdvanced_Type())
mplsNodeCreateTunnelAdvanced.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsNodeCreateTunnelAdvanced.setStatus(_B)
_MplsNodeCreateLspAdvanced_Type=CommandString
_MplsNodeCreateLspAdvanced_Object=MibTableColumn
mplsNodeCreateLspAdvanced=_MplsNodeCreateLspAdvanced_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,20),_MplsNodeCreateLspAdvanced_Type())
mplsNodeCreateLspAdvanced.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsNodeCreateLspAdvanced.setStatus(_B)
_MplsNodeCreatePwGeneric_Type=CommandString
_MplsNodeCreatePwGeneric_Object=MibTableColumn
mplsNodeCreatePwGeneric=_MplsNodeCreatePwGeneric_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,21),_MplsNodeCreatePwGeneric_Type())
mplsNodeCreatePwGeneric.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsNodeCreatePwGeneric.setStatus(_B)
_MplsNodeCreatePwMpls_Type=CommandString
_MplsNodeCreatePwMpls_Object=MibTableColumn
mplsNodeCreatePwMpls=_MplsNodeCreatePwMpls_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,22),_MplsNodeCreatePwMpls_Type())
mplsNodeCreatePwMpls.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsNodeCreatePwMpls.setStatus(_B)
_MplsNodeCreatePwEnet_Type=CommandString
_MplsNodeCreatePwEnet_Object=MibTableColumn
mplsNodeCreatePwEnet=_MplsNodeCreatePwEnet_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,23),_MplsNodeCreatePwEnet_Type())
mplsNodeCreatePwEnet.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsNodeCreatePwEnet.setStatus(_B)
_MplsNodeCreateBfdTemplate_Type=CommandString
_MplsNodeCreateBfdTemplate_Object=MibTableColumn
mplsNodeCreateBfdTemplate=_MplsNodeCreateBfdTemplate_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,24),_MplsNodeCreateBfdTemplate_Type())
mplsNodeCreateBfdTemplate.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsNodeCreateBfdTemplate.setStatus(_B)
_MplsNodeCreateXCAdvanced_Type=CommandString
_MplsNodeCreateXCAdvanced_Object=MibTableColumn
mplsNodeCreateXCAdvanced=_MplsNodeCreateXCAdvanced_Object((1,3,6,1,4,1,8708,2,40,2,5,1,1,25),_MplsNodeCreateXCAdvanced_Type())
mplsNodeCreateXCAdvanced.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsNodeCreateXCAdvanced.setStatus(_B)
_MplsLspList_ObjectIdentity=ObjectIdentity
mplsLspList=_MplsLspList_ObjectIdentity((1,3,6,1,4,1,8708,2,40,2,6))
_MplsLspTable_Object=MibTable
mplsLspTable=_MplsLspTable_Object((1,3,6,1,4,1,8708,2,40,2,6,1))
if mibBuilder.loadTexts:mplsLspTable.setStatus(_B)
_MplsLspEntry_Object=MibTableRow
mplsLspEntry=_MplsLspEntry_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1))
mplsLspEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:mplsLspEntry.setStatus(_B)
class _MplsLspIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsLspIndex_Type.__name__=_E
_MplsLspIndex_Object=MibTableColumn
mplsLspIndex=_MplsLspIndex_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,1),_MplsLspIndex_Type())
mplsLspIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLspIndex.setStatus(_B)
_MplsLspName_Type=MgmtNameString
_MplsLspName_Object=MibTableColumn
mplsLspName=_MplsLspName_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,2),_MplsLspName_Type())
mplsLspName.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLspName.setStatus(_B)
class _MplsLspInternalReference_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsLspInternalReference_Type.__name__=_E
_MplsLspInternalReference_Object=MibTableColumn
mplsLspInternalReference=_MplsLspInternalReference_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,3),_MplsLspInternalReference_Type())
mplsLspInternalReference.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLspInternalReference.setStatus(_B)
class _MplsLspIdentifier_Type(DisplayString):defaultValue=OctetString('')
_MplsLspIdentifier_Type.__name__=_H
_MplsLspIdentifier_Object=MibTableColumn
mplsLspIdentifier=_MplsLspIdentifier_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,4),_MplsLspIdentifier_Type())
mplsLspIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLspIdentifier.setStatus(_B)
class _MplsLspState_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_AR,3)))
_MplsLspState_Type.__name__=_I
_MplsLspState_Object=MibTableColumn
mplsLspState=_MplsLspState_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,5),_MplsLspState_Type())
mplsLspState.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLspState.setStatus(_B)
class _MplsLspRole_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('edge',1),('transit',2)))
_MplsLspRole_Type.__name__=_I
_MplsLspRole_Object=MibTableColumn
mplsLspRole=_MplsLspRole_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,6),_MplsLspRole_Type())
mplsLspRole.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLspRole.setStatus(_B)
class _MplsLspForwardXCId_Type(DisplayString):defaultValue=OctetString('')
_MplsLspForwardXCId_Type.__name__=_H
_MplsLspForwardXCId_Object=MibTableColumn
mplsLspForwardXCId=_MplsLspForwardXCId_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,7),_MplsLspForwardXCId_Type())
mplsLspForwardXCId.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLspForwardXCId.setStatus(_B)
class _MplsLspReverseXCId_Type(DisplayString):defaultValue=OctetString('')
_MplsLspReverseXCId_Type.__name__=_H
_MplsLspReverseXCId_Object=MibTableColumn
mplsLspReverseXCId=_MplsLspReverseXCId_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,8),_MplsLspReverseXCId_Type())
mplsLspReverseXCId.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLspReverseXCId.setStatus(_B)
class _MplsLspPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_MplsLspPriority_Type.__name__=_I
_MplsLspPriority_Object=MibTableColumn
mplsLspPriority=_MplsLspPriority_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,9),_MplsLspPriority_Type())
mplsLspPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLspPriority.setStatus(_B)
class _MplsLspSrcNodeId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MplsLspSrcNodeId_Type.__name__=_E
_MplsLspSrcNodeId_Object=MibTableColumn
mplsLspSrcNodeId=_MplsLspSrcNodeId_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,10),_MplsLspSrcNodeId_Type())
mplsLspSrcNodeId.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLspSrcNodeId.setStatus(_B)
class _MplsLspDestNodeId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MplsLspDestNodeId_Type.__name__=_E
_MplsLspDestNodeId_Object=MibTableColumn
mplsLspDestNodeId=_MplsLspDestNodeId_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,11),_MplsLspDestNodeId_Type())
mplsLspDestNodeId.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLspDestNodeId.setStatus(_B)
class _MplsLspSrcTunnelId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MplsLspSrcTunnelId_Type.__name__=_E
_MplsLspSrcTunnelId_Object=MibTableColumn
mplsLspSrcTunnelId=_MplsLspSrcTunnelId_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,12),_MplsLspSrcTunnelId_Type())
mplsLspSrcTunnelId.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLspSrcTunnelId.setStatus(_B)
class _MplsLspDestTunnelId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MplsLspDestTunnelId_Type.__name__=_E
_MplsLspDestTunnelId_Object=MibTableColumn
mplsLspDestTunnelId=_MplsLspDestTunnelId_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,13),_MplsLspDestTunnelId_Type())
mplsLspDestTunnelId.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLspDestTunnelId.setStatus(_B)
class _MplsLspLspId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MplsLspLspId_Type.__name__=_E
_MplsLspLspId_Object=MibTableColumn
mplsLspLspId=_MplsLspLspId_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,14),_MplsLspLspId_Type())
mplsLspLspId.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsLspLspId.setStatus(_B)
class _MplsLspExtId_Type(DisplayString):defaultValue=OctetString('')
_MplsLspExtId_Type.__name__=_H
_MplsLspExtId_Object=MibTableColumn
mplsLspExtId=_MplsLspExtId_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,15),_MplsLspExtId_Type())
mplsLspExtId.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLspExtId.setStatus(_B)
class _MplsLspIntTunnelId_Type(DisplayString):defaultValue=OctetString('')
_MplsLspIntTunnelId_Type.__name__=_H
_MplsLspIntTunnelId_Object=MibTableColumn
mplsLspIntTunnelId=_MplsLspIntTunnelId_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,16),_MplsLspIntTunnelId_Type())
mplsLspIntTunnelId.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLspIntTunnelId.setStatus(_B)
_MplsLspRowStatus_Type=RowStatus
_MplsLspRowStatus_Object=MibTableColumn
mplsLspRowStatus=_MplsLspRowStatus_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,17),_MplsLspRowStatus_Type())
mplsLspRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLspRowStatus.setStatus(_B)
class _MplsLspBFDSession_Type(DisplayString):defaultValue=OctetString('')
_MplsLspBFDSession_Type.__name__=_H
_MplsLspBFDSession_Object=MibTableColumn
mplsLspBFDSession=_MplsLspBFDSession_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,18),_MplsLspBFDSession_Type())
mplsLspBFDSession.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLspBFDSession.setStatus(_B)
_MplsLspCreateBFD_Type=CommandString
_MplsLspCreateBFD_Object=MibTableColumn
mplsLspCreateBFD=_MplsLspCreateBFD_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,19),_MplsLspCreateBFD_Type())
mplsLspCreateBFD.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLspCreateBFD.setStatus(_B)
class _MplsLspTrafficClass_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_MplsLspTrafficClass_Type.__name__=_E
_MplsLspTrafficClass_Object=MibTableColumn
mplsLspTrafficClass=_MplsLspTrafficClass_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,20),_MplsLspTrafficClass_Type())
mplsLspTrafficClass.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLspTrafficClass.setStatus(_G)
class _MplsLspGlobalId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MplsLspGlobalId_Type.__name__=_E
_MplsLspGlobalId_Object=MibTableColumn
mplsLspGlobalId=_MplsLspGlobalId_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,21),_MplsLspGlobalId_Type())
mplsLspGlobalId.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLspGlobalId.setStatus(_B)
class _MplsLspDestGlobalId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MplsLspDestGlobalId_Type.__name__=_E
_MplsLspDestGlobalId_Object=MibTableColumn
mplsLspDestGlobalId=_MplsLspDestGlobalId_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,22),_MplsLspDestGlobalId_Type())
mplsLspDestGlobalId.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsLspDestGlobalId.setStatus(_B)
class _MplsLspReservedBW_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MplsLspReservedBW_Type.__name__=_E
_MplsLspReservedBW_Object=MibTableColumn
mplsLspReservedBW=_MplsLspReservedBW_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,23),_MplsLspReservedBW_Type())
mplsLspReservedBW.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsLspReservedBW.setStatus(_B)
class _MplsLspDescr_Type(DisplayString):defaultValue=OctetString('')
_MplsLspDescr_Type.__name__=_H
_MplsLspDescr_Object=MibTableColumn
mplsLspDescr=_MplsLspDescr_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,24),_MplsLspDescr_Type())
mplsLspDescr.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsLspDescr.setStatus(_B)
_MplsLspCreateBFDAdvanced_Type=CommandString
_MplsLspCreateBFDAdvanced_Object=MibTableColumn
mplsLspCreateBFDAdvanced=_MplsLspCreateBFDAdvanced_Object((1,3,6,1,4,1,8708,2,40,2,6,1,1,25),_MplsLspCreateBFDAdvanced_Type())
mplsLspCreateBFDAdvanced.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLspCreateBFDAdvanced.setStatus(_B)
_MplsTnlXLspList_ObjectIdentity=ObjectIdentity
mplsTnlXLspList=_MplsTnlXLspList_ObjectIdentity((1,3,6,1,4,1,8708,2,40,2,7))
_MplsTnlXLspTable_Object=MibTable
mplsTnlXLspTable=_MplsTnlXLspTable_Object((1,3,6,1,4,1,8708,2,40,2,7,1))
if mibBuilder.loadTexts:mplsTnlXLspTable.setStatus(_B)
_MplsTnlXLspEntry_Object=MibTableRow
mplsTnlXLspEntry=_MplsTnlXLspEntry_Object((1,3,6,1,4,1,8708,2,40,2,7,1,1))
mplsTnlXLspEntry.setIndexNames((0,_A,_AT))
if mibBuilder.loadTexts:mplsTnlXLspEntry.setStatus(_B)
class _MplsTnlXLspIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsTnlXLspIndex_Type.__name__=_E
_MplsTnlXLspIndex_Object=MibTableColumn
mplsTnlXLspIndex=_MplsTnlXLspIndex_Object((1,3,6,1,4,1,8708,2,40,2,7,1,1,1),_MplsTnlXLspIndex_Type())
mplsTnlXLspIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTnlXLspIndex.setStatus(_B)
_MplsTnlXLspName_Type=MgmtNameString
_MplsTnlXLspName_Object=MibTableColumn
mplsTnlXLspName=_MplsTnlXLspName_Object((1,3,6,1,4,1,8708,2,40,2,7,1,1,2),_MplsTnlXLspName_Type())
mplsTnlXLspName.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsTnlXLspName.setStatus(_B)
class _MplsTnlXLspInternalReference_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsTnlXLspInternalReference_Type.__name__=_E
_MplsTnlXLspInternalReference_Object=MibTableColumn
mplsTnlXLspInternalReference=_MplsTnlXLspInternalReference_Object((1,3,6,1,4,1,8708,2,40,2,7,1,1,3),_MplsTnlXLspInternalReference_Type())
mplsTnlXLspInternalReference.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTnlXLspInternalReference.setStatus(_B)
class _MplsTnlXLspTunnelId_Type(DisplayString):defaultValue=OctetString('')
_MplsTnlXLspTunnelId_Type.__name__=_H
_MplsTnlXLspTunnelId_Object=MibTableColumn
mplsTnlXLspTunnelId=_MplsTnlXLspTunnelId_Object((1,3,6,1,4,1,8708,2,40,2,7,1,1,4),_MplsTnlXLspTunnelId_Type())
mplsTnlXLspTunnelId.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTnlXLspTunnelId.setStatus(_B)
class _MplsTnlXLspLspId_Type(DisplayString):defaultValue=OctetString('')
_MplsTnlXLspLspId_Type.__name__=_H
_MplsTnlXLspLspId_Object=MibTableColumn
mplsTnlXLspLspId=_MplsTnlXLspLspId_Object((1,3,6,1,4,1,8708,2,40,2,7,1,1,5),_MplsTnlXLspLspId_Type())
mplsTnlXLspLspId.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTnlXLspLspId.setStatus(_B)
_MplsTnlXLspRowStatus_Type=RowStatus
_MplsTnlXLspRowStatus_Object=MibTableColumn
mplsTnlXLspRowStatus=_MplsTnlXLspRowStatus_Object((1,3,6,1,4,1,8708,2,40,2,7,1,1,6),_MplsTnlXLspRowStatus_Type())
mplsTnlXLspRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsTnlXLspRowStatus.setStatus(_B)
mplsGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,40,1,1,1))
mplsGeneralGroupV1.setObjects(*((_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax)))
if mibBuilder.loadTexts:mplsGeneralGroupV1.setStatus(_B)
mplsIfGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,40,1,1,2))
mplsIfGroupV1.setObjects(*((_A,_AB),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag)))
if mibBuilder.loadTexts:mplsIfGroupV1.setStatus(_G)
mplsXCGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,40,1,1,3))
mplsXCGroupV1.setObjects(*((_A,_AQ),(_A,_Ay),(_A,_Az),(_A,_A_),(_A,_B0),(_A,_B1),(_A,_B2),(_A,_B3),(_A,_B4),(_A,_B5),(_A,_B6)))
if mibBuilder.loadTexts:mplsXCGroupV1.setStatus(_B)
mplsTunnelGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,40,1,1,4))
mplsTunnelGroupV1.setObjects(*((_A,_P),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:mplsTunnelGroupV1.setStatus(_G)
mplsNodeGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,40,1,1,5))
mplsNodeGroupV1.setObjects(*((_A,_M),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:mplsNodeGroupV1.setStatus(_G)
mplsLspGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,40,1,1,6))
mplsLspGroupV1.setObjects(*((_A,_N),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:mplsLspGroupV1.setStatus(_G)
mplsTnlXLspV1=ObjectGroup((1,3,6,1,4,1,8708,2,40,1,1,7))
mplsTnlXLspV1.setObjects(*((_A,_AT),(_A,_B7),(_A,_B8),(_A,_B9),(_A,_BA),(_A,_BB)))
if mibBuilder.loadTexts:mplsTnlXLspV1.setStatus(_B)
mplsTunnelGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,40,1,1,8))
mplsTunnelGroupV2.setObjects(*((_A,_P),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:mplsTunnelGroupV2.setStatus(_G)
mplsNodeGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,40,1,1,9))
mplsNodeGroupV2.setObjects(*((_A,_M),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:mplsNodeGroupV2.setStatus(_G)
mplsLspGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,40,1,1,10))
mplsLspGroupV2.setObjects(*((_A,_N),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:mplsLspGroupV2.setStatus(_G)
mplsNodeGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,40,1,1,11))
mplsNodeGroupV3.setObjects(*((_A,_M),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_AJ)))
if mibBuilder.loadTexts:mplsNodeGroupV3.setStatus(_G)
mplsTunnelGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,40,1,1,12))
mplsTunnelGroupV3.setObjects(*((_A,_P),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_Ah),(_A,_Ai)))
if mibBuilder.loadTexts:mplsTunnelGroupV3.setStatus(_G)
mplsLspGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,40,1,1,13))
mplsLspGroupV3.setObjects(*((_A,_N),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AK)))
if mibBuilder.loadTexts:mplsLspGroupV3.setStatus(_G)
mplsNodeGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,40,1,1,14))
mplsNodeGroupV4.setObjects(*((_A,_M),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_AJ),(_A,_Aj)))
if mibBuilder.loadTexts:mplsNodeGroupV4.setStatus(_G)
mplsLspGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,40,1,1,15))
mplsLspGroupV4.setObjects(*((_A,_N),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AK),(_A,_Ak)))
if mibBuilder.loadTexts:mplsLspGroupV4.setStatus(_G)
mplsTunnelGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,40,1,1,16))
mplsTunnelGroupV4.setObjects(*((_A,_P),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_Ah),(_A,_Ai),(_A,_BC)))
if mibBuilder.loadTexts:mplsTunnelGroupV4.setStatus(_B)
mplsIfGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,40,1,1,17))
mplsIfGroupV2.setObjects(*((_A,_AB),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_BD),(_A,_BE),(_A,_BF)))
if mibBuilder.loadTexts:mplsIfGroupV2.setStatus(_B)
mplsNodeGroupV5=ObjectGroup((1,3,6,1,4,1,8708,2,40,1,1,18))
mplsNodeGroupV5.setObjects(*((_A,_M),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_AJ),(_A,_Aj),(_A,_BG),(_A,_BH),(_A,_BI),(_A,_BJ),(_A,_BK),(_A,_BL),(_A,_BM)))
if mibBuilder.loadTexts:mplsNodeGroupV5.setStatus(_B)
mplsLspGroupV5=ObjectGroup((1,3,6,1,4,1,8708,2,40,1,1,19))
mplsLspGroupV5.setObjects(*((_A,_N),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AK),(_A,_Ak),(_A,_BN)))
if mibBuilder.loadTexts:mplsLspGroupV5.setStatus(_B)
lumMplsBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,40,1,2,1))
lumMplsBasicComplV1.setObjects(*((_A,_J),(_A,_O),(_A,_K),(_A,_Al),(_A,_BO),(_A,_BP),(_A,_L)))
if mibBuilder.loadTexts:lumMplsBasicComplV1.setStatus(_G)
lumMplsBasicComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,40,1,2,2))
lumMplsBasicComplV2.setObjects(*((_A,_J),(_A,_O),(_A,_K),(_A,_Al),(_A,_BQ),(_A,_BR),(_A,_L)))
if mibBuilder.loadTexts:lumMplsBasicComplV2.setStatus(_G)
lumMplsBasicComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,40,1,2,3))
lumMplsBasicComplV3.setObjects(*((_A,_J),(_A,_O),(_A,_K),(_A,_AL),(_A,_Am),(_A,_AM),(_A,_L)))
if mibBuilder.loadTexts:lumMplsBasicComplV3.setStatus(_G)
lumMplsBasicComplV4=ModuleCompliance((1,3,6,1,4,1,8708,2,40,1,2,4))
lumMplsBasicComplV4.setObjects(*((_A,_J),(_A,_O),(_A,_K),(_A,_AL),(_A,_Am),(_A,_AM),(_A,_L)))
if mibBuilder.loadTexts:lumMplsBasicComplV4.setStatus(_G)
lumMplsBasicComplV5=ModuleCompliance((1,3,6,1,4,1,8708,2,40,1,2,5))
lumMplsBasicComplV5.setObjects(*((_A,_J),(_A,_O),(_A,_K),(_A,_AL),(_A,_AN),(_A,_AM),(_A,_L)))
if mibBuilder.loadTexts:lumMplsBasicComplV5.setStatus(_G)
lumMplsBasicComplV6=ModuleCompliance((1,3,6,1,4,1,8708,2,40,1,2,6))
lumMplsBasicComplV6.setObjects(*((_A,_J),(_A,_O),(_A,_K),(_A,_AO),(_A,_AN),(_A,_An),(_A,_L)))
if mibBuilder.loadTexts:lumMplsBasicComplV6.setStatus(_G)
lumMplsBasicComplV7=ModuleCompliance((1,3,6,1,4,1,8708,2,40,1,2,7))
lumMplsBasicComplV7.setObjects(*((_A,_J),(_A,_Ao),(_A,_K),(_A,_AO),(_A,_AN),(_A,_An),(_A,_L)))
if mibBuilder.loadTexts:lumMplsBasicComplV7.setStatus(_G)
lumMplsBasicComplV8=ModuleCompliance((1,3,6,1,4,1,8708,2,40,1,2,8))
lumMplsBasicComplV8.setObjects(*((_A,_J),(_A,_Ao),(_A,_K),(_A,_AO),(_A,_BS),(_A,_BT),(_A,_L)))
if mibBuilder.loadTexts:lumMplsBasicComplV8.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_AS:MplsIdentifier,'lumMplsMIBModule':lumMplsMIBModule,'lumMplsConfs':lumMplsConfs,'lumMplsGroups':lumMplsGroups,_J:mplsGeneralGroupV1,_O:mplsIfGroupV1,_K:mplsXCGroupV1,'mplsTunnelGroupV1':mplsTunnelGroupV1,_BO:mplsNodeGroupV1,_BP:mplsLspGroupV1,_L:mplsTnlXLspV1,_Al:mplsTunnelGroupV2,_BQ:mplsNodeGroupV2,_BR:mplsLspGroupV2,_Am:mplsNodeGroupV3,_AL:mplsTunnelGroupV3,_AM:mplsLspGroupV3,_AN:mplsNodeGroupV4,_An:mplsLspGroupV4,_AO:mplsTunnelGroupV4,_Ao:mplsIfGroupV2,_BS:mplsNodeGroupV5,_BT:mplsLspGroupV5,'lumMplsCompl':lumMplsCompl,'lumMplsBasicComplV1':lumMplsBasicComplV1,'lumMplsBasicComplV2':lumMplsBasicComplV2,'lumMplsBasicComplV3':lumMplsBasicComplV3,'lumMplsBasicComplV4':lumMplsBasicComplV4,'lumMplsBasicComplV5':lumMplsBasicComplV5,'lumMplsBasicComplV6':lumMplsBasicComplV6,'lumMplsBasicComplV7':lumMplsBasicComplV7,'lumMplsBasicComplV8':lumMplsBasicComplV8,'lumMplsMIBObjects':lumMplsMIBObjects,'mplsGeneral':mplsGeneral,_Ar:mplsGeneralLastChangeTime,_As:mplsGeneralStateLastChangeTime,_At:mplsGeneralMplsIfTableSize,_Au:mplsGeneralMplsXCTableSize,_Av:mplsGeneralMplsTunnelTableSize,'mplsGeneralMplsNodeTableSize':mplsGeneralMplsNodeTableSize,_Aw:mplsGeneralMplsLspTableSize,_Ax:mplsGeneralMplsTnlXLspTableSize,'mplsIfList':mplsIfList,'mplsIfTable':mplsIfTable,'mplsIfEntry':mplsIfEntry,_AB:mplsIfIndex,_AU:mplsIfName,_AV:mplsIfSubrack,_AW:mplsIfSlot,_AX:mplsIfTxPort,_AY:mplsIfPortIndex,_AZ:mplsIfPortName,_Aa:mplsIfInternalReference,_Ab:mplsIfAdminStatus,_Ac:mplsIfIdentifier,_Ad:mplsIfNextHopMacAddress,_Ae:mplsIfInterfaceMacAddress,_Af:mplsIfVlan,_Ag:mplsIfRowStatus,_BD:mplsIfIfNo,_BE:mplsIfResourceType,_BF:mplsIfLagId,'mplsXCList':mplsXCList,'mplsXCTable':mplsXCTable,'mplsXCEntry':mplsXCEntry,_AQ:mplsXCIndex,_Ay:mplsXCName,_Az:mplsXCInternalReference,_A_:mplsXCIdentifier,_B0:mplsXCInSegmentIfIndex,_B1:mplsXCInSegmentIfName,_B2:mplsXCInSegmentLabel,_B3:mplsXCOutSegmentIfIndex,_B4:mplsXCOutSegmentIfName,_B5:mplsXCOutSegmentLabel,_B6:mplsXCRowStatus,'mplsTunnelList':mplsTunnelList,'mplsTunnelTable':mplsTunnelTable,'mplsTunnelEntry':mplsTunnelEntry,_P:mplsTunnelIndex,_q:mplsTunnelInternalReference,_r:mplsTunnelIdentifier,_s:mplsTunnelName,_t:mplsTunnelActiveLSP,_u:mplsTunnelActiveLspIndex,'mplsTunnelState':mplsTunnelState,_v:mplsTunnelSrcNodeId,_w:mplsTunnelSrcTunnelId,_x:mplsTunnelDestNodeId,_y:mplsTunnelDestTunnelId,_z:mplsTunnelExtId,_A0:mplsTunnelAssociateLSP,_A1:mplsTunnelRowStatus,_AC:mplsTunnelLinearProtection,_AD:mplsTunnelProtectionState,_AE:mplsTunnelAssociateLinearProt,_AF:mplsTunnelGlobalId,_AG:mplsTunnelDestGlobalId,_AH:mplsTunnelWorkingLSP,_AI:mplsTunnelProtectionLSP,_Ah:mplsTunnelReservedBW,_Ai:mplsTunnelBookedBW,_BC:mplsTunnelDescr,'mplsNodeList':mplsNodeList,'mplsNodeTable':mplsNodeTable,'mplsNodeEntry':mplsNodeEntry,_M:mplsNodeIndex,_Q:mplsNodeName,_R:mplsNodeSubrack,_S:mplsNodeSlot,_T:mplsNodeIccIdStr,_U:mplsNodeIdNum,_V:mplsNodeCreateXC,_W:mplsNodeCreateTunnel,_X:mplsNodeCreateLsp,_Y:mplsNodeCreatePw,_Z:mplsNodeCreateIf,_A2:mplsNodeLinearProtMode,_A3:mplsNodeLinearProtWtrTimer,_A4:mplsNodeLPContMsgInterval,_A5:mplsNodeLPRapidMsgInterval,'mplsNodeGlobalId':mplsNodeGlobalId,_AJ:mplsNodeCreateMsPw,_Aj:mplsNodeCreateLsp2,_BG:mplsNodeCreateTunnelAdvanced,_BH:mplsNodeCreateLspAdvanced,_BI:mplsNodeCreatePwGeneric,_BJ:mplsNodeCreatePwMpls,_BK:mplsNodeCreatePwEnet,_BL:mplsNodeCreateBfdTemplate,_BM:mplsNodeCreateXCAdvanced,'mplsLspList':mplsLspList,'mplsLspTable':mplsLspTable,'mplsLspEntry':mplsLspEntry,_N:mplsLspIndex,_a:mplsLspName,_b:mplsLspInternalReference,_c:mplsLspIdentifier,_d:mplsLspState,_e:mplsLspRole,_f:mplsLspForwardXCId,_g:mplsLspReverseXCId,_h:mplsLspPriority,_i:mplsLspSrcNodeId,_j:mplsLspDestNodeId,_k:mplsLspSrcTunnelId,_l:mplsLspDestTunnelId,_m:mplsLspLspId,_n:mplsLspExtId,_o:mplsLspIntTunnelId,_p:mplsLspRowStatus,_A6:mplsLspBFDSession,_A7:mplsLspCreateBFD,_A8:mplsLspTrafficClass,_A9:mplsLspGlobalId,_AA:mplsLspDestGlobalId,_AK:mplsLspReservedBW,_Ak:mplsLspDescr,_BN:mplsLspCreateBFDAdvanced,'mplsTnlXLspList':mplsTnlXLspList,'mplsTnlXLspTable':mplsTnlXLspTable,'mplsTnlXLspEntry':mplsTnlXLspEntry,_AT:mplsTnlXLspIndex,_B7:mplsTnlXLspName,_B8:mplsTnlXLspInternalReference,_B9:mplsTnlXLspTunnelId,_BA:mplsTnlXLspLspId,_BB:mplsTnlXLspRowStatus})