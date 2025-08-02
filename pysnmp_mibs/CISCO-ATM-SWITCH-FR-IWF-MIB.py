_Aq='ciscoAtmSFrIwfMappingGroup'
_Ap='ciscoAtmSFrIwfVcIwStatsGroup'
_Ao='ciscoAtmSFrIwfVcStatsGroup'
_An='ciscoAtmSFrIwfConfIfGroup'
_Am='ciscoAtmSFrIwfLmiGroup'
_Al='ciscoAtmSFrIwfConfConnGroup'
_Ak='casfAFMapFrDlci'
_Aj='casfAFMapFrIndex'
_Ai='casfFAMapInternalAtmVci'
_Ah='casfFAMapInternalAtmVpi'
_Ag='casfFAMapInternalAtmInterface'
_Af='casfVcIwfCountTotalDiscardFrames'
_Ae='casfVcIwfCountCrcErrors'
_Ad='casfVcIwfCountLengthErrors'
_Ac='casfVcIwfCountReassemblyTimeouts'
_Ab='casfVcIwfCountOutUnknownProts'
_Aa='casfVcIwfCountInUnknownProts'
_AZ='casfVcCountTaggedDEs'
_AY='casfVcCountTaggedBECNs'
_AX='casfVcCountTaggedFECNs'
_AW='casfVcCountSentDEs'
_AV='casfVcCountSentBECNs'
_AU='casfVcCountSentFECNs'
_AT='casfVcCountSentOctets'
_AS='casfVcCountSentFrames'
_AR='casfVcCountOutDiscards'
_AQ='casfVcCountInDiscards'
_AP='casfVcCountReceivedDEs'
_AO='casfVcCountReceivedBECNs'
_AN='casfVcCountReceivedFECNs'
_AM='casfVcCountReceivedOctets'
_AL='casfVcCountReceivedFrames'
_AK='casfConfIfCledSpvcClpModeDef'
_AJ='casfConfIfCledSpvcDeModeDef'
_AI='casfConfIfBcDefault'
_AH='casfConfIfUpcIntent'
_AG='casfConfIfAtmAddress'
_AF='casfFrLmiStatusEnqTimeouts'
_AE='casfFrLmiStatusTimeouts'
_AD='casfFrLmiStatusOuts'
_AC='casfFrLmiStatusIns'
_AB='casfFrLmiEnquiryOuts'
_AA='casfFrLmiEnquiryIns'
_A9='casfFrLmiNetT392'
_A8='casfFrLmiNetN393'
_A7='casfFrLmiNetN392'
_A6='casfFrLmiUserT391'
_A5='casfFrLmiUserN393'
_A4='casfFrLmiUserN392'
_A3='casfFrLmiUserN391'
_A2='casfFrLmiType'
_A1='casfFrLmiProtocol'
_A0='casfVcSignalStandardCalledIe'
_z='casfVcEndptRowStatus'
_y='casfVcEndptSpvcRemoteVci'
_x='casfVcEndptSpvcRemoteVpi'
_w='casfVcEndptSpvcRemoteDlci'
_v='casfVcEndptSpvcRemoteType'
_u='casfVcEndptSpvcRemoteAddr'
_t='casfVcEndptRcvdSigStatus'
_s='casfVcEndptCreationTime'
_r='casfVcEndptUpcMode'
_q='casfVcEndptEfciMode'
_p='casfVcEndptDeMode'
_o='casfVcEndptClpMode'
_n='casfVcEndptIwfType'
_m='casfVcEndptConnKind'
_l='casfVcEndptTxNegTrafficDescrRow'
_k='casfVcEndptRxNegTrafficDescrRow'
_j='casfVcEndptTxTrafficDescrRow'
_i='casfVcEndptRxTrafficDescrRow'
_h='casfTrafficDescrRowStatus'
_g='casfTrafficDescrAtmIndex'
_f='casfTrafficDescrServCategory'
_e='casfTrafficDescrPIR'
_d='casfTrafficDescrBe'
_c='casfTrafficDescrBc'
_b='casfTrafficDescrCIR'
_a='casfAFMapAtmVci'
_Z='casfAFMapAtmVpi'
_Y='casfFAMapDlci'
_X='octets'
_W='seconds'
_V='tagDrop'
_U='deIfFrsscsDe'
_T='deIfClpOrFrsscsDe'
_S='clpIfDe'
_R='ConnectionKind'
_Q='bits/sec'
_P='casfTrafficDescrIndex'
_O='TruthValue'
_N='Unsigned32'
_M='bits'
_L='messages'
_K='casfVcEndptDlci'
_J='not-accessible'
_I='ifIndex'
_H='IF-MIB'
_G='frames'
_F='read-write'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='CISCO-ATM-SWITCH-FR-IWF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AtmTrafficDescrParamIndex,=mibBuilder.importSymbols('ATM-MIB','AtmTrafficDescrParamIndex')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
Unsigned32,=mibBuilder.importSymbols('CISCO-TC',_N)
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_H,'InterfaceIndex',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_O)
ciscoAtmSwitchFrIwfMIB=ModuleIdentity((1,3,6,1,4,1,9,9,112))
if mibBuilder.loadTexts:ciscoAtmSwitchFrIwfMIB.setRevisions(('2001-05-20 00:00','2000-02-29 00:00','1998-07-09 00:00'))
class CasfTrafficDescrRow(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class DlciValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4194303))
class ConnectionKind(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('pvc',1),('svcIncoming',2),('svcOutgoing',3),('spvcInitiator',4),('spvcTarget',5)))
class AtmAddr(TextualConvention,OctetString):status=_A;displayHint='1x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_CiscoAtmSwitchFrIwfMIBObjects_ObjectIdentity=ObjectIdentity
ciscoAtmSwitchFrIwfMIBObjects=_CiscoAtmSwitchFrIwfMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,112,1))
_CasfFrTraffic_ObjectIdentity=ObjectIdentity
casfFrTraffic=_CasfFrTraffic_ObjectIdentity((1,3,6,1,4,1,9,9,112,1,1))
_CasfTrafficDescrTable_Object=MibTable
casfTrafficDescrTable=_CasfTrafficDescrTable_Object((1,3,6,1,4,1,9,9,112,1,1,1))
if mibBuilder.loadTexts:casfTrafficDescrTable.setStatus(_A)
_CasfTrafficDescrEntry_Object=MibTableRow
casfTrafficDescrEntry=_CasfTrafficDescrEntry_Object((1,3,6,1,4,1,9,9,112,1,1,1,1))
casfTrafficDescrEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:casfTrafficDescrEntry.setStatus(_A)
_CasfTrafficDescrIndex_Type=CasfTrafficDescrRow
_CasfTrafficDescrIndex_Object=MibTableColumn
casfTrafficDescrIndex=_CasfTrafficDescrIndex_Object((1,3,6,1,4,1,9,9,112,1,1,1,1,1),_CasfTrafficDescrIndex_Type())
casfTrafficDescrIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:casfTrafficDescrIndex.setStatus(_A)
_CasfTrafficDescrCIR_Type=Unsigned32
_CasfTrafficDescrCIR_Object=MibTableColumn
casfTrafficDescrCIR=_CasfTrafficDescrCIR_Object((1,3,6,1,4,1,9,9,112,1,1,1,1,2),_CasfTrafficDescrCIR_Type())
casfTrafficDescrCIR.setMaxAccess(_E)
if mibBuilder.loadTexts:casfTrafficDescrCIR.setStatus(_A)
if mibBuilder.loadTexts:casfTrafficDescrCIR.setUnits(_Q)
_CasfTrafficDescrBc_Type=Unsigned32
_CasfTrafficDescrBc_Object=MibTableColumn
casfTrafficDescrBc=_CasfTrafficDescrBc_Object((1,3,6,1,4,1,9,9,112,1,1,1,1,3),_CasfTrafficDescrBc_Type())
casfTrafficDescrBc.setMaxAccess(_E)
if mibBuilder.loadTexts:casfTrafficDescrBc.setStatus(_A)
if mibBuilder.loadTexts:casfTrafficDescrBc.setUnits(_M)
_CasfTrafficDescrBe_Type=Unsigned32
_CasfTrafficDescrBe_Object=MibTableColumn
casfTrafficDescrBe=_CasfTrafficDescrBe_Object((1,3,6,1,4,1,9,9,112,1,1,1,1,4),_CasfTrafficDescrBe_Type())
casfTrafficDescrBe.setMaxAccess(_E)
if mibBuilder.loadTexts:casfTrafficDescrBe.setStatus(_A)
if mibBuilder.loadTexts:casfTrafficDescrBe.setUnits(_M)
_CasfTrafficDescrPIR_Type=Unsigned32
_CasfTrafficDescrPIR_Object=MibTableColumn
casfTrafficDescrPIR=_CasfTrafficDescrPIR_Object((1,3,6,1,4,1,9,9,112,1,1,1,1,5),_CasfTrafficDescrPIR_Type())
casfTrafficDescrPIR.setMaxAccess(_E)
if mibBuilder.loadTexts:casfTrafficDescrPIR.setStatus(_A)
if mibBuilder.loadTexts:casfTrafficDescrPIR.setUnits(_Q)
class _CasfTrafficDescrServCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('vbrNrt',1),('abr',2),('ubr',3),('vbrRt',4)))
_CasfTrafficDescrServCategory_Type.__name__=_D
_CasfTrafficDescrServCategory_Object=MibTableColumn
casfTrafficDescrServCategory=_CasfTrafficDescrServCategory_Object((1,3,6,1,4,1,9,9,112,1,1,1,1,6),_CasfTrafficDescrServCategory_Type())
casfTrafficDescrServCategory.setMaxAccess(_E)
if mibBuilder.loadTexts:casfTrafficDescrServCategory.setStatus(_A)
_CasfTrafficDescrAtmIndex_Type=AtmTrafficDescrParamIndex
_CasfTrafficDescrAtmIndex_Object=MibTableColumn
casfTrafficDescrAtmIndex=_CasfTrafficDescrAtmIndex_Object((1,3,6,1,4,1,9,9,112,1,1,1,1,7),_CasfTrafficDescrAtmIndex_Type())
casfTrafficDescrAtmIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:casfTrafficDescrAtmIndex.setStatus(_A)
_CasfTrafficDescrRowStatus_Type=RowStatus
_CasfTrafficDescrRowStatus_Object=MibTableColumn
casfTrafficDescrRowStatus=_CasfTrafficDescrRowStatus_Object((1,3,6,1,4,1,9,9,112,1,1,1,1,8),_CasfTrafficDescrRowStatus_Type())
casfTrafficDescrRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:casfTrafficDescrRowStatus.setStatus(_A)
_CasfFrVC_ObjectIdentity=ObjectIdentity
casfFrVC=_CasfFrVC_ObjectIdentity((1,3,6,1,4,1,9,9,112,1,2))
_CasfVcEndptTable_Object=MibTable
casfVcEndptTable=_CasfVcEndptTable_Object((1,3,6,1,4,1,9,9,112,1,2,1))
if mibBuilder.loadTexts:casfVcEndptTable.setStatus(_A)
_CasfVcEndptEntry_Object=MibTableRow
casfVcEndptEntry=_CasfVcEndptEntry_Object((1,3,6,1,4,1,9,9,112,1,2,1,1))
casfVcEndptEntry.setIndexNames((0,_H,_I),(0,_B,_K))
if mibBuilder.loadTexts:casfVcEndptEntry.setStatus(_A)
_CasfVcEndptDlci_Type=DlciValue
_CasfVcEndptDlci_Object=MibTableColumn
casfVcEndptDlci=_CasfVcEndptDlci_Object((1,3,6,1,4,1,9,9,112,1,2,1,1,1),_CasfVcEndptDlci_Type())
casfVcEndptDlci.setMaxAccess(_J)
if mibBuilder.loadTexts:casfVcEndptDlci.setStatus(_A)
_CasfVcEndptRxTrafficDescrRow_Type=CasfTrafficDescrRow
_CasfVcEndptRxTrafficDescrRow_Object=MibTableColumn
casfVcEndptRxTrafficDescrRow=_CasfVcEndptRxTrafficDescrRow_Object((1,3,6,1,4,1,9,9,112,1,2,1,1,2),_CasfVcEndptRxTrafficDescrRow_Type())
casfVcEndptRxTrafficDescrRow.setMaxAccess(_E)
if mibBuilder.loadTexts:casfVcEndptRxTrafficDescrRow.setStatus(_A)
_CasfVcEndptTxTrafficDescrRow_Type=CasfTrafficDescrRow
_CasfVcEndptTxTrafficDescrRow_Object=MibTableColumn
casfVcEndptTxTrafficDescrRow=_CasfVcEndptTxTrafficDescrRow_Object((1,3,6,1,4,1,9,9,112,1,2,1,1,3),_CasfVcEndptTxTrafficDescrRow_Type())
casfVcEndptTxTrafficDescrRow.setMaxAccess(_E)
if mibBuilder.loadTexts:casfVcEndptTxTrafficDescrRow.setStatus(_A)
_CasfVcEndptRxNegTrafficDescrRow_Type=CasfTrafficDescrRow
_CasfVcEndptRxNegTrafficDescrRow_Object=MibTableColumn
casfVcEndptRxNegTrafficDescrRow=_CasfVcEndptRxNegTrafficDescrRow_Object((1,3,6,1,4,1,9,9,112,1,2,1,1,4),_CasfVcEndptRxNegTrafficDescrRow_Type())
casfVcEndptRxNegTrafficDescrRow.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcEndptRxNegTrafficDescrRow.setStatus(_A)
_CasfVcEndptTxNegTrafficDescrRow_Type=CasfTrafficDescrRow
_CasfVcEndptTxNegTrafficDescrRow_Object=MibTableColumn
casfVcEndptTxNegTrafficDescrRow=_CasfVcEndptTxNegTrafficDescrRow_Object((1,3,6,1,4,1,9,9,112,1,2,1,1,5),_CasfVcEndptTxNegTrafficDescrRow_Type())
casfVcEndptTxNegTrafficDescrRow.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcEndptTxNegTrafficDescrRow.setStatus(_A)
class _CasfVcEndptConnKind_Type(ConnectionKind):defaultValue=1
_CasfVcEndptConnKind_Type.__name__=_R
_CasfVcEndptConnKind_Object=MibTableColumn
casfVcEndptConnKind=_CasfVcEndptConnKind_Object((1,3,6,1,4,1,9,9,112,1,2,1,1,6),_CasfVcEndptConnKind_Type())
casfVcEndptConnKind.setMaxAccess(_E)
if mibBuilder.loadTexts:casfVcEndptConnKind.setStatus(_A)
class _CasfVcEndptIwfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('network',1),('serviceTransparent',2),('serviceTranslation',3),('rfc1973',4)))
_CasfVcEndptIwfType_Type.__name__=_D
_CasfVcEndptIwfType_Object=MibTableColumn
casfVcEndptIwfType=_CasfVcEndptIwfType_Object((1,3,6,1,4,1,9,9,112,1,2,1,1,7),_CasfVcEndptIwfType_Type())
casfVcEndptIwfType.setMaxAccess(_E)
if mibBuilder.loadTexts:casfVcEndptIwfType.setStatus(_A)
class _CasfVcEndptClpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),('clpIsZero',2),('clpIsOne',3)))
_CasfVcEndptClpMode_Type.__name__=_D
_CasfVcEndptClpMode_Object=MibTableColumn
casfVcEndptClpMode=_CasfVcEndptClpMode_Object((1,3,6,1,4,1,9,9,112,1,2,1,1,8),_CasfVcEndptClpMode_Type())
casfVcEndptClpMode.setMaxAccess(_E)
if mibBuilder.loadTexts:casfVcEndptClpMode.setStatus(_A)
class _CasfVcEndptDeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_T,1),(_U,2),('deIfClp',3),('deIsZero',4),('deIsOne',5)))
_CasfVcEndptDeMode_Type.__name__=_D
_CasfVcEndptDeMode_Object=MibTableColumn
casfVcEndptDeMode=_CasfVcEndptDeMode_Object((1,3,6,1,4,1,9,9,112,1,2,1,1,9),_CasfVcEndptDeMode_Type())
casfVcEndptDeMode.setMaxAccess(_E)
if mibBuilder.loadTexts:casfVcEndptDeMode.setStatus(_A)
class _CasfVcEndptEfciMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('efciIfFecn',1),('efciIsZero',2)))
_CasfVcEndptEfciMode_Type.__name__=_D
_CasfVcEndptEfciMode_Object=MibTableColumn
casfVcEndptEfciMode=_CasfVcEndptEfciMode_Object((1,3,6,1,4,1,9,9,112,1,2,1,1,10),_CasfVcEndptEfciMode_Type())
casfVcEndptEfciMode.setMaxAccess(_E)
if mibBuilder.loadTexts:casfVcEndptEfciMode.setStatus(_A)
class _CasfVcEndptUpcMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('pass',1),(_V,2),('tag',3),('drop',4)))
_CasfVcEndptUpcMode_Type.__name__=_D
_CasfVcEndptUpcMode_Object=MibTableColumn
casfVcEndptUpcMode=_CasfVcEndptUpcMode_Object((1,3,6,1,4,1,9,9,112,1,2,1,1,11),_CasfVcEndptUpcMode_Type())
casfVcEndptUpcMode.setMaxAccess(_E)
if mibBuilder.loadTexts:casfVcEndptUpcMode.setStatus(_A)
_CasfVcEndptSpvcRemoteAddr_Type=AtmAddr
_CasfVcEndptSpvcRemoteAddr_Object=MibTableColumn
casfVcEndptSpvcRemoteAddr=_CasfVcEndptSpvcRemoteAddr_Object((1,3,6,1,4,1,9,9,112,1,2,1,1,12),_CasfVcEndptSpvcRemoteAddr_Type())
casfVcEndptSpvcRemoteAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:casfVcEndptSpvcRemoteAddr.setStatus(_A)
class _CasfVcEndptSpvcRemoteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('frameRelay',2),('atm',3)))
_CasfVcEndptSpvcRemoteType_Type.__name__=_D
_CasfVcEndptSpvcRemoteType_Object=MibTableColumn
casfVcEndptSpvcRemoteType=_CasfVcEndptSpvcRemoteType_Object((1,3,6,1,4,1,9,9,112,1,2,1,1,13),_CasfVcEndptSpvcRemoteType_Type())
casfVcEndptSpvcRemoteType.setMaxAccess(_E)
if mibBuilder.loadTexts:casfVcEndptSpvcRemoteType.setStatus(_A)
_CasfVcEndptSpvcRemoteDlci_Type=DlciValue
_CasfVcEndptSpvcRemoteDlci_Object=MibTableColumn
casfVcEndptSpvcRemoteDlci=_CasfVcEndptSpvcRemoteDlci_Object((1,3,6,1,4,1,9,9,112,1,2,1,1,14),_CasfVcEndptSpvcRemoteDlci_Type())
casfVcEndptSpvcRemoteDlci.setMaxAccess(_E)
if mibBuilder.loadTexts:casfVcEndptSpvcRemoteDlci.setStatus(_A)
class _CasfVcEndptSpvcRemoteVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CasfVcEndptSpvcRemoteVpi_Type.__name__=_D
_CasfVcEndptSpvcRemoteVpi_Object=MibTableColumn
casfVcEndptSpvcRemoteVpi=_CasfVcEndptSpvcRemoteVpi_Object((1,3,6,1,4,1,9,9,112,1,2,1,1,15),_CasfVcEndptSpvcRemoteVpi_Type())
casfVcEndptSpvcRemoteVpi.setMaxAccess(_E)
if mibBuilder.loadTexts:casfVcEndptSpvcRemoteVpi.setStatus(_A)
class _CasfVcEndptSpvcRemoteVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CasfVcEndptSpvcRemoteVci_Type.__name__=_D
_CasfVcEndptSpvcRemoteVci_Object=MibTableColumn
casfVcEndptSpvcRemoteVci=_CasfVcEndptSpvcRemoteVci_Object((1,3,6,1,4,1,9,9,112,1,2,1,1,16),_CasfVcEndptSpvcRemoteVci_Type())
casfVcEndptSpvcRemoteVci.setMaxAccess(_E)
if mibBuilder.loadTexts:casfVcEndptSpvcRemoteVci.setStatus(_A)
_CasfVcEndptCreationTime_Type=TimeStamp
_CasfVcEndptCreationTime_Object=MibTableColumn
casfVcEndptCreationTime=_CasfVcEndptCreationTime_Object((1,3,6,1,4,1,9,9,112,1,2,1,1,17),_CasfVcEndptCreationTime_Type())
casfVcEndptCreationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcEndptCreationTime.setStatus(_A)
class _CasfVcEndptRcvdSigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('deleted',1),('active',2),('inactive',3),('none',4)))
_CasfVcEndptRcvdSigStatus_Type.__name__=_D
_CasfVcEndptRcvdSigStatus_Object=MibTableColumn
casfVcEndptRcvdSigStatus=_CasfVcEndptRcvdSigStatus_Object((1,3,6,1,4,1,9,9,112,1,2,1,1,18),_CasfVcEndptRcvdSigStatus_Type())
casfVcEndptRcvdSigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcEndptRcvdSigStatus.setStatus(_A)
_CasfVcEndptRowStatus_Type=RowStatus
_CasfVcEndptRowStatus_Object=MibTableColumn
casfVcEndptRowStatus=_CasfVcEndptRowStatus_Object((1,3,6,1,4,1,9,9,112,1,2,1,1,19),_CasfVcEndptRowStatus_Type())
casfVcEndptRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:casfVcEndptRowStatus.setStatus(_A)
class _CasfVcSignalStandardCalledIe_Type(TruthValue):defaultValue=2
_CasfVcSignalStandardCalledIe_Type.__name__=_O
_CasfVcSignalStandardCalledIe_Object=MibTableColumn
casfVcSignalStandardCalledIe=_CasfVcSignalStandardCalledIe_Object((1,3,6,1,4,1,9,9,112,1,2,1,1,20),_CasfVcSignalStandardCalledIe_Type())
casfVcSignalStandardCalledIe.setMaxAccess(_E)
if mibBuilder.loadTexts:casfVcSignalStandardCalledIe.setStatus(_A)
_CasfFrInterface_ObjectIdentity=ObjectIdentity
casfFrInterface=_CasfFrInterface_ObjectIdentity((1,3,6,1,4,1,9,9,112,1,3))
_CasfFrLmiTable_Object=MibTable
casfFrLmiTable=_CasfFrLmiTable_Object((1,3,6,1,4,1,9,9,112,1,3,1))
if mibBuilder.loadTexts:casfFrLmiTable.setStatus(_A)
_CasfFrLmiEntry_Object=MibTableRow
casfFrLmiEntry=_CasfFrLmiEntry_Object((1,3,6,1,4,1,9,9,112,1,3,1,1))
casfFrLmiEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:casfFrLmiEntry.setStatus(_A)
class _CasfFrLmiProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('lmi',2),('ansiT1617D',3),('ansiT1617B',4),('ccittQ933A',5)))
_CasfFrLmiProtocol_Type.__name__=_D
_CasfFrLmiProtocol_Object=MibTableColumn
casfFrLmiProtocol=_CasfFrLmiProtocol_Object((1,3,6,1,4,1,9,9,112,1,3,1,1,1),_CasfFrLmiProtocol_Type())
casfFrLmiProtocol.setMaxAccess(_F)
if mibBuilder.loadTexts:casfFrLmiProtocol.setStatus(_A)
class _CasfFrLmiType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dte',1),('dce',2),('nni',3)))
_CasfFrLmiType_Type.__name__=_D
_CasfFrLmiType_Object=MibTableColumn
casfFrLmiType=_CasfFrLmiType_Object((1,3,6,1,4,1,9,9,112,1,3,1,1,2),_CasfFrLmiType_Type())
casfFrLmiType.setMaxAccess(_F)
if mibBuilder.loadTexts:casfFrLmiType.setStatus(_A)
class _CasfFrLmiUserN391_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CasfFrLmiUserN391_Type.__name__=_D
_CasfFrLmiUserN391_Object=MibTableColumn
casfFrLmiUserN391=_CasfFrLmiUserN391_Object((1,3,6,1,4,1,9,9,112,1,3,1,1,3),_CasfFrLmiUserN391_Type())
casfFrLmiUserN391.setMaxAccess(_F)
if mibBuilder.loadTexts:casfFrLmiUserN391.setStatus(_A)
class _CasfFrLmiUserN392_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CasfFrLmiUserN392_Type.__name__=_D
_CasfFrLmiUserN392_Object=MibTableColumn
casfFrLmiUserN392=_CasfFrLmiUserN392_Object((1,3,6,1,4,1,9,9,112,1,3,1,1,4),_CasfFrLmiUserN392_Type())
casfFrLmiUserN392.setMaxAccess(_F)
if mibBuilder.loadTexts:casfFrLmiUserN392.setStatus(_A)
class _CasfFrLmiUserN393_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CasfFrLmiUserN393_Type.__name__=_D
_CasfFrLmiUserN393_Object=MibTableColumn
casfFrLmiUserN393=_CasfFrLmiUserN393_Object((1,3,6,1,4,1,9,9,112,1,3,1,1,5),_CasfFrLmiUserN393_Type())
casfFrLmiUserN393.setMaxAccess(_F)
if mibBuilder.loadTexts:casfFrLmiUserN393.setStatus(_A)
class _CasfFrLmiUserT391_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_CasfFrLmiUserT391_Type.__name__=_D
_CasfFrLmiUserT391_Object=MibTableColumn
casfFrLmiUserT391=_CasfFrLmiUserT391_Object((1,3,6,1,4,1,9,9,112,1,3,1,1,6),_CasfFrLmiUserT391_Type())
casfFrLmiUserT391.setMaxAccess(_F)
if mibBuilder.loadTexts:casfFrLmiUserT391.setStatus(_A)
if mibBuilder.loadTexts:casfFrLmiUserT391.setUnits(_W)
class _CasfFrLmiNetN392_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CasfFrLmiNetN392_Type.__name__=_D
_CasfFrLmiNetN392_Object=MibTableColumn
casfFrLmiNetN392=_CasfFrLmiNetN392_Object((1,3,6,1,4,1,9,9,112,1,3,1,1,7),_CasfFrLmiNetN392_Type())
casfFrLmiNetN392.setMaxAccess(_F)
if mibBuilder.loadTexts:casfFrLmiNetN392.setStatus(_A)
class _CasfFrLmiNetN393_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_CasfFrLmiNetN393_Type.__name__=_D
_CasfFrLmiNetN393_Object=MibTableColumn
casfFrLmiNetN393=_CasfFrLmiNetN393_Object((1,3,6,1,4,1,9,9,112,1,3,1,1,8),_CasfFrLmiNetN393_Type())
casfFrLmiNetN393.setMaxAccess(_F)
if mibBuilder.loadTexts:casfFrLmiNetN393.setStatus(_A)
class _CasfFrLmiNetT392_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_CasfFrLmiNetT392_Type.__name__=_D
_CasfFrLmiNetT392_Object=MibTableColumn
casfFrLmiNetT392=_CasfFrLmiNetT392_Object((1,3,6,1,4,1,9,9,112,1,3,1,1,9),_CasfFrLmiNetT392_Type())
casfFrLmiNetT392.setMaxAccess(_F)
if mibBuilder.loadTexts:casfFrLmiNetT392.setStatus(_A)
if mibBuilder.loadTexts:casfFrLmiNetT392.setUnits(_W)
_CasfFrLmiEnquiryIns_Type=Counter32
_CasfFrLmiEnquiryIns_Object=MibTableColumn
casfFrLmiEnquiryIns=_CasfFrLmiEnquiryIns_Object((1,3,6,1,4,1,9,9,112,1,3,1,1,10),_CasfFrLmiEnquiryIns_Type())
casfFrLmiEnquiryIns.setMaxAccess(_C)
if mibBuilder.loadTexts:casfFrLmiEnquiryIns.setStatus(_A)
if mibBuilder.loadTexts:casfFrLmiEnquiryIns.setUnits(_L)
_CasfFrLmiEnquiryOuts_Type=Counter32
_CasfFrLmiEnquiryOuts_Object=MibTableColumn
casfFrLmiEnquiryOuts=_CasfFrLmiEnquiryOuts_Object((1,3,6,1,4,1,9,9,112,1,3,1,1,11),_CasfFrLmiEnquiryOuts_Type())
casfFrLmiEnquiryOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:casfFrLmiEnquiryOuts.setStatus(_A)
if mibBuilder.loadTexts:casfFrLmiEnquiryOuts.setUnits(_L)
_CasfFrLmiStatusIns_Type=Counter32
_CasfFrLmiStatusIns_Object=MibTableColumn
casfFrLmiStatusIns=_CasfFrLmiStatusIns_Object((1,3,6,1,4,1,9,9,112,1,3,1,1,12),_CasfFrLmiStatusIns_Type())
casfFrLmiStatusIns.setMaxAccess(_C)
if mibBuilder.loadTexts:casfFrLmiStatusIns.setStatus(_A)
if mibBuilder.loadTexts:casfFrLmiStatusIns.setUnits(_L)
_CasfFrLmiStatusOuts_Type=Counter32
_CasfFrLmiStatusOuts_Object=MibTableColumn
casfFrLmiStatusOuts=_CasfFrLmiStatusOuts_Object((1,3,6,1,4,1,9,9,112,1,3,1,1,13),_CasfFrLmiStatusOuts_Type())
casfFrLmiStatusOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:casfFrLmiStatusOuts.setStatus(_A)
if mibBuilder.loadTexts:casfFrLmiStatusOuts.setUnits(_L)
_CasfFrLmiStatusTimeouts_Type=Counter32
_CasfFrLmiStatusTimeouts_Object=MibTableColumn
casfFrLmiStatusTimeouts=_CasfFrLmiStatusTimeouts_Object((1,3,6,1,4,1,9,9,112,1,3,1,1,14),_CasfFrLmiStatusTimeouts_Type())
casfFrLmiStatusTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:casfFrLmiStatusTimeouts.setStatus(_A)
_CasfFrLmiStatusEnqTimeouts_Type=Counter32
_CasfFrLmiStatusEnqTimeouts_Object=MibTableColumn
casfFrLmiStatusEnqTimeouts=_CasfFrLmiStatusEnqTimeouts_Object((1,3,6,1,4,1,9,9,112,1,3,1,1,15),_CasfFrLmiStatusEnqTimeouts_Type())
casfFrLmiStatusEnqTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:casfFrLmiStatusEnqTimeouts.setStatus(_A)
_CasfConfIfTable_Object=MibTable
casfConfIfTable=_CasfConfIfTable_Object((1,3,6,1,4,1,9,9,112,1,3,2))
if mibBuilder.loadTexts:casfConfIfTable.setStatus(_A)
_CasfConfIfEntry_Object=MibTableRow
casfConfIfEntry=_CasfConfIfEntry_Object((1,3,6,1,4,1,9,9,112,1,3,2,1))
casfConfIfEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:casfConfIfEntry.setStatus(_A)
_CasfConfIfAtmAddress_Type=AtmAddr
_CasfConfIfAtmAddress_Object=MibTableColumn
casfConfIfAtmAddress=_CasfConfIfAtmAddress_Object((1,3,6,1,4,1,9,9,112,1,3,2,1,1),_CasfConfIfAtmAddress_Type())
casfConfIfAtmAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:casfConfIfAtmAddress.setStatus(_A)
class _CasfConfIfUpcIntent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('pass',1),(_V,2),('tag',3),('drop',4)))
_CasfConfIfUpcIntent_Type.__name__=_D
_CasfConfIfUpcIntent_Object=MibTableColumn
casfConfIfUpcIntent=_CasfConfIfUpcIntent_Object((1,3,6,1,4,1,9,9,112,1,3,2,1,2),_CasfConfIfUpcIntent_Type())
casfConfIfUpcIntent.setMaxAccess(_F)
if mibBuilder.loadTexts:casfConfIfUpcIntent.setStatus(_A)
class _CasfConfIfBcDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32768))
_CasfConfIfBcDefault_Type.__name__=_D
_CasfConfIfBcDefault_Object=MibTableColumn
casfConfIfBcDefault=_CasfConfIfBcDefault_Object((1,3,6,1,4,1,9,9,112,1,3,2,1,3),_CasfConfIfBcDefault_Type())
casfConfIfBcDefault.setMaxAccess(_F)
if mibBuilder.loadTexts:casfConfIfBcDefault.setStatus(_A)
if mibBuilder.loadTexts:casfConfIfBcDefault.setUnits(_M)
class _CasfConfIfCledSpvcDeModeDef_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_CasfConfIfCledSpvcDeModeDef_Type.__name__=_D
_CasfConfIfCledSpvcDeModeDef_Object=MibTableColumn
casfConfIfCledSpvcDeModeDef=_CasfConfIfCledSpvcDeModeDef_Object((1,3,6,1,4,1,9,9,112,1,3,2,1,4),_CasfConfIfCledSpvcDeModeDef_Type())
casfConfIfCledSpvcDeModeDef.setMaxAccess(_F)
if mibBuilder.loadTexts:casfConfIfCledSpvcDeModeDef.setStatus(_A)
class _CasfConfIfCledSpvcClpModeDef_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),('clpIfIsZero',2),('clpIfIsOne',3)))
_CasfConfIfCledSpvcClpModeDef_Type.__name__=_D
_CasfConfIfCledSpvcClpModeDef_Object=MibTableColumn
casfConfIfCledSpvcClpModeDef=_CasfConfIfCledSpvcClpModeDef_Object((1,3,6,1,4,1,9,9,112,1,3,2,1,5),_CasfConfIfCledSpvcClpModeDef_Type())
casfConfIfCledSpvcClpModeDef.setMaxAccess(_F)
if mibBuilder.loadTexts:casfConfIfCledSpvcClpModeDef.setStatus(_A)
_CasfFrCounts_ObjectIdentity=ObjectIdentity
casfFrCounts=_CasfFrCounts_ObjectIdentity((1,3,6,1,4,1,9,9,112,1,4))
_CasfVcCountTable_Object=MibTable
casfVcCountTable=_CasfVcCountTable_Object((1,3,6,1,4,1,9,9,112,1,4,1))
if mibBuilder.loadTexts:casfVcCountTable.setStatus(_A)
_CasfVcCountEntry_Object=MibTableRow
casfVcCountEntry=_CasfVcCountEntry_Object((1,3,6,1,4,1,9,9,112,1,4,1,1))
casfVcCountEntry.setIndexNames((0,_H,_I),(0,_B,_K))
if mibBuilder.loadTexts:casfVcCountEntry.setStatus(_A)
_CasfVcCountReceivedFrames_Type=Counter32
_CasfVcCountReceivedFrames_Object=MibTableColumn
casfVcCountReceivedFrames=_CasfVcCountReceivedFrames_Object((1,3,6,1,4,1,9,9,112,1,4,1,1,1),_CasfVcCountReceivedFrames_Type())
casfVcCountReceivedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcCountReceivedFrames.setStatus(_A)
if mibBuilder.loadTexts:casfVcCountReceivedFrames.setUnits(_G)
_CasfVcCountReceivedOctets_Type=Counter32
_CasfVcCountReceivedOctets_Object=MibTableColumn
casfVcCountReceivedOctets=_CasfVcCountReceivedOctets_Object((1,3,6,1,4,1,9,9,112,1,4,1,1,2),_CasfVcCountReceivedOctets_Type())
casfVcCountReceivedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcCountReceivedOctets.setStatus(_A)
if mibBuilder.loadTexts:casfVcCountReceivedOctets.setUnits(_X)
_CasfVcCountReceivedFECNs_Type=Counter32
_CasfVcCountReceivedFECNs_Object=MibTableColumn
casfVcCountReceivedFECNs=_CasfVcCountReceivedFECNs_Object((1,3,6,1,4,1,9,9,112,1,4,1,1,3),_CasfVcCountReceivedFECNs_Type())
casfVcCountReceivedFECNs.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcCountReceivedFECNs.setStatus(_A)
if mibBuilder.loadTexts:casfVcCountReceivedFECNs.setUnits(_G)
_CasfVcCountReceivedBECNs_Type=Counter32
_CasfVcCountReceivedBECNs_Object=MibTableColumn
casfVcCountReceivedBECNs=_CasfVcCountReceivedBECNs_Object((1,3,6,1,4,1,9,9,112,1,4,1,1,4),_CasfVcCountReceivedBECNs_Type())
casfVcCountReceivedBECNs.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcCountReceivedBECNs.setStatus(_A)
if mibBuilder.loadTexts:casfVcCountReceivedBECNs.setUnits(_G)
_CasfVcCountReceivedDEs_Type=Counter32
_CasfVcCountReceivedDEs_Object=MibTableColumn
casfVcCountReceivedDEs=_CasfVcCountReceivedDEs_Object((1,3,6,1,4,1,9,9,112,1,4,1,1,5),_CasfVcCountReceivedDEs_Type())
casfVcCountReceivedDEs.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcCountReceivedDEs.setStatus(_A)
if mibBuilder.loadTexts:casfVcCountReceivedDEs.setUnits(_G)
_CasfVcCountInDiscards_Type=Counter32
_CasfVcCountInDiscards_Object=MibTableColumn
casfVcCountInDiscards=_CasfVcCountInDiscards_Object((1,3,6,1,4,1,9,9,112,1,4,1,1,6),_CasfVcCountInDiscards_Type())
casfVcCountInDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcCountInDiscards.setStatus(_A)
if mibBuilder.loadTexts:casfVcCountInDiscards.setUnits(_G)
_CasfVcCountOutDiscards_Type=Counter32
_CasfVcCountOutDiscards_Object=MibTableColumn
casfVcCountOutDiscards=_CasfVcCountOutDiscards_Object((1,3,6,1,4,1,9,9,112,1,4,1,1,7),_CasfVcCountOutDiscards_Type())
casfVcCountOutDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcCountOutDiscards.setStatus(_A)
if mibBuilder.loadTexts:casfVcCountOutDiscards.setUnits(_G)
_CasfVcCountSentFrames_Type=Counter32
_CasfVcCountSentFrames_Object=MibTableColumn
casfVcCountSentFrames=_CasfVcCountSentFrames_Object((1,3,6,1,4,1,9,9,112,1,4,1,1,8),_CasfVcCountSentFrames_Type())
casfVcCountSentFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcCountSentFrames.setStatus(_A)
if mibBuilder.loadTexts:casfVcCountSentFrames.setUnits(_G)
_CasfVcCountSentOctets_Type=Counter32
_CasfVcCountSentOctets_Object=MibTableColumn
casfVcCountSentOctets=_CasfVcCountSentOctets_Object((1,3,6,1,4,1,9,9,112,1,4,1,1,9),_CasfVcCountSentOctets_Type())
casfVcCountSentOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcCountSentOctets.setStatus(_A)
if mibBuilder.loadTexts:casfVcCountSentOctets.setUnits(_X)
_CasfVcCountSentFECNs_Type=Counter32
_CasfVcCountSentFECNs_Object=MibTableColumn
casfVcCountSentFECNs=_CasfVcCountSentFECNs_Object((1,3,6,1,4,1,9,9,112,1,4,1,1,10),_CasfVcCountSentFECNs_Type())
casfVcCountSentFECNs.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcCountSentFECNs.setStatus(_A)
if mibBuilder.loadTexts:casfVcCountSentFECNs.setUnits(_G)
_CasfVcCountSentBECNs_Type=Counter32
_CasfVcCountSentBECNs_Object=MibTableColumn
casfVcCountSentBECNs=_CasfVcCountSentBECNs_Object((1,3,6,1,4,1,9,9,112,1,4,1,1,11),_CasfVcCountSentBECNs_Type())
casfVcCountSentBECNs.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcCountSentBECNs.setStatus(_A)
if mibBuilder.loadTexts:casfVcCountSentBECNs.setUnits(_G)
_CasfVcCountSentDEs_Type=Counter32
_CasfVcCountSentDEs_Object=MibTableColumn
casfVcCountSentDEs=_CasfVcCountSentDEs_Object((1,3,6,1,4,1,9,9,112,1,4,1,1,12),_CasfVcCountSentDEs_Type())
casfVcCountSentDEs.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcCountSentDEs.setStatus(_A)
if mibBuilder.loadTexts:casfVcCountSentDEs.setUnits(_G)
_CasfVcCountTaggedFECNs_Type=Counter32
_CasfVcCountTaggedFECNs_Object=MibTableColumn
casfVcCountTaggedFECNs=_CasfVcCountTaggedFECNs_Object((1,3,6,1,4,1,9,9,112,1,4,1,1,13),_CasfVcCountTaggedFECNs_Type())
casfVcCountTaggedFECNs.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcCountTaggedFECNs.setStatus(_A)
if mibBuilder.loadTexts:casfVcCountTaggedFECNs.setUnits(_G)
_CasfVcCountTaggedBECNs_Type=Counter32
_CasfVcCountTaggedBECNs_Object=MibTableColumn
casfVcCountTaggedBECNs=_CasfVcCountTaggedBECNs_Object((1,3,6,1,4,1,9,9,112,1,4,1,1,14),_CasfVcCountTaggedBECNs_Type())
casfVcCountTaggedBECNs.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcCountTaggedBECNs.setStatus(_A)
if mibBuilder.loadTexts:casfVcCountTaggedBECNs.setUnits(_G)
_CasfVcCountTaggedDEs_Type=Counter32
_CasfVcCountTaggedDEs_Object=MibTableColumn
casfVcCountTaggedDEs=_CasfVcCountTaggedDEs_Object((1,3,6,1,4,1,9,9,112,1,4,1,1,15),_CasfVcCountTaggedDEs_Type())
casfVcCountTaggedDEs.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcCountTaggedDEs.setStatus(_A)
if mibBuilder.loadTexts:casfVcCountTaggedDEs.setUnits(_G)
_CasfVcIwfCountTable_Object=MibTable
casfVcIwfCountTable=_CasfVcIwfCountTable_Object((1,3,6,1,4,1,9,9,112,1,4,2))
if mibBuilder.loadTexts:casfVcIwfCountTable.setStatus(_A)
_CasfVcIwfCountEntry_Object=MibTableRow
casfVcIwfCountEntry=_CasfVcIwfCountEntry_Object((1,3,6,1,4,1,9,9,112,1,4,2,1))
casfVcIwfCountEntry.setIndexNames((0,_H,_I),(0,_B,_K))
if mibBuilder.loadTexts:casfVcIwfCountEntry.setStatus(_A)
_CasfVcIwfCountInUnknownProts_Type=Counter32
_CasfVcIwfCountInUnknownProts_Object=MibTableColumn
casfVcIwfCountInUnknownProts=_CasfVcIwfCountInUnknownProts_Object((1,3,6,1,4,1,9,9,112,1,4,2,1,1),_CasfVcIwfCountInUnknownProts_Type())
casfVcIwfCountInUnknownProts.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcIwfCountInUnknownProts.setStatus(_A)
_CasfVcIwfCountOutUnknownProts_Type=Counter32
_CasfVcIwfCountOutUnknownProts_Object=MibTableColumn
casfVcIwfCountOutUnknownProts=_CasfVcIwfCountOutUnknownProts_Object((1,3,6,1,4,1,9,9,112,1,4,2,1,2),_CasfVcIwfCountOutUnknownProts_Type())
casfVcIwfCountOutUnknownProts.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcIwfCountOutUnknownProts.setStatus(_A)
_CasfVcIwfCountReassemblyTimeouts_Type=Counter32
_CasfVcIwfCountReassemblyTimeouts_Object=MibTableColumn
casfVcIwfCountReassemblyTimeouts=_CasfVcIwfCountReassemblyTimeouts_Object((1,3,6,1,4,1,9,9,112,1,4,2,1,3),_CasfVcIwfCountReassemblyTimeouts_Type())
casfVcIwfCountReassemblyTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcIwfCountReassemblyTimeouts.setStatus(_A)
_CasfVcIwfCountLengthErrors_Type=Counter32
_CasfVcIwfCountLengthErrors_Object=MibTableColumn
casfVcIwfCountLengthErrors=_CasfVcIwfCountLengthErrors_Object((1,3,6,1,4,1,9,9,112,1,4,2,1,4),_CasfVcIwfCountLengthErrors_Type())
casfVcIwfCountLengthErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcIwfCountLengthErrors.setStatus(_A)
_CasfVcIwfCountCrcErrors_Type=Counter32
_CasfVcIwfCountCrcErrors_Object=MibTableColumn
casfVcIwfCountCrcErrors=_CasfVcIwfCountCrcErrors_Object((1,3,6,1,4,1,9,9,112,1,4,2,1,5),_CasfVcIwfCountCrcErrors_Type())
casfVcIwfCountCrcErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcIwfCountCrcErrors.setStatus(_A)
_CasfVcIwfCountTotalDiscardFrames_Type=Counter32
_CasfVcIwfCountTotalDiscardFrames_Object=MibTableColumn
casfVcIwfCountTotalDiscardFrames=_CasfVcIwfCountTotalDiscardFrames_Object((1,3,6,1,4,1,9,9,112,1,4,2,1,6),_CasfVcIwfCountTotalDiscardFrames_Type())
casfVcIwfCountTotalDiscardFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:casfVcIwfCountTotalDiscardFrames.setStatus(_A)
_CasfMapping_ObjectIdentity=ObjectIdentity
casfMapping=_CasfMapping_ObjectIdentity((1,3,6,1,4,1,9,9,112,1,5))
_CasfFAMapTable_Object=MibTable
casfFAMapTable=_CasfFAMapTable_Object((1,3,6,1,4,1,9,9,112,1,5,1))
if mibBuilder.loadTexts:casfFAMapTable.setStatus(_A)
_CasfFAMapEntry_Object=MibTableRow
casfFAMapEntry=_CasfFAMapEntry_Object((1,3,6,1,4,1,9,9,112,1,5,1,1))
casfFAMapEntry.setIndexNames((0,_H,_I),(0,_B,_Y))
if mibBuilder.loadTexts:casfFAMapEntry.setStatus(_A)
_CasfFAMapDlci_Type=DlciValue
_CasfFAMapDlci_Object=MibTableColumn
casfFAMapDlci=_CasfFAMapDlci_Object((1,3,6,1,4,1,9,9,112,1,5,1,1,1),_CasfFAMapDlci_Type())
casfFAMapDlci.setMaxAccess(_J)
if mibBuilder.loadTexts:casfFAMapDlci.setStatus(_A)
_CasfFAMapInternalAtmInterface_Type=InterfaceIndex
_CasfFAMapInternalAtmInterface_Object=MibTableColumn
casfFAMapInternalAtmInterface=_CasfFAMapInternalAtmInterface_Object((1,3,6,1,4,1,9,9,112,1,5,1,1,2),_CasfFAMapInternalAtmInterface_Type())
casfFAMapInternalAtmInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:casfFAMapInternalAtmInterface.setStatus(_A)
class _CasfFAMapInternalAtmVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CasfFAMapInternalAtmVpi_Type.__name__=_D
_CasfFAMapInternalAtmVpi_Object=MibTableColumn
casfFAMapInternalAtmVpi=_CasfFAMapInternalAtmVpi_Object((1,3,6,1,4,1,9,9,112,1,5,1,1,3),_CasfFAMapInternalAtmVpi_Type())
casfFAMapInternalAtmVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:casfFAMapInternalAtmVpi.setStatus(_A)
class _CasfFAMapInternalAtmVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CasfFAMapInternalAtmVci_Type.__name__=_D
_CasfFAMapInternalAtmVci_Object=MibTableColumn
casfFAMapInternalAtmVci=_CasfFAMapInternalAtmVci_Object((1,3,6,1,4,1,9,9,112,1,5,1,1,4),_CasfFAMapInternalAtmVci_Type())
casfFAMapInternalAtmVci.setMaxAccess(_C)
if mibBuilder.loadTexts:casfFAMapInternalAtmVci.setStatus(_A)
_CasfAFMapTable_Object=MibTable
casfAFMapTable=_CasfAFMapTable_Object((1,3,6,1,4,1,9,9,112,1,5,2))
if mibBuilder.loadTexts:casfAFMapTable.setStatus(_A)
_CasfAFMapEntry_Object=MibTableRow
casfAFMapEntry=_CasfAFMapEntry_Object((1,3,6,1,4,1,9,9,112,1,5,2,1))
casfAFMapEntry.setIndexNames((0,_H,_I),(0,_B,_Z),(0,_B,_a))
if mibBuilder.loadTexts:casfAFMapEntry.setStatus(_A)
class _CasfAFMapAtmVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CasfAFMapAtmVpi_Type.__name__=_D
_CasfAFMapAtmVpi_Object=MibTableColumn
casfAFMapAtmVpi=_CasfAFMapAtmVpi_Object((1,3,6,1,4,1,9,9,112,1,5,2,1,1),_CasfAFMapAtmVpi_Type())
casfAFMapAtmVpi.setMaxAccess(_J)
if mibBuilder.loadTexts:casfAFMapAtmVpi.setStatus(_A)
class _CasfAFMapAtmVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CasfAFMapAtmVci_Type.__name__=_D
_CasfAFMapAtmVci_Object=MibTableColumn
casfAFMapAtmVci=_CasfAFMapAtmVci_Object((1,3,6,1,4,1,9,9,112,1,5,2,1,2),_CasfAFMapAtmVci_Type())
casfAFMapAtmVci.setMaxAccess(_J)
if mibBuilder.loadTexts:casfAFMapAtmVci.setStatus(_A)
_CasfAFMapFrIndex_Type=InterfaceIndex
_CasfAFMapFrIndex_Object=MibTableColumn
casfAFMapFrIndex=_CasfAFMapFrIndex_Object((1,3,6,1,4,1,9,9,112,1,5,2,1,3),_CasfAFMapFrIndex_Type())
casfAFMapFrIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:casfAFMapFrIndex.setStatus(_A)
_CasfAFMapFrDlci_Type=DlciValue
_CasfAFMapFrDlci_Object=MibTableColumn
casfAFMapFrDlci=_CasfAFMapFrDlci_Object((1,3,6,1,4,1,9,9,112,1,5,2,1,4),_CasfAFMapFrDlci_Type())
casfAFMapFrDlci.setMaxAccess(_C)
if mibBuilder.loadTexts:casfAFMapFrDlci.setStatus(_A)
_CiscoAtmSFrIwfMIBConformance_ObjectIdentity=ObjectIdentity
ciscoAtmSFrIwfMIBConformance=_CiscoAtmSFrIwfMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,112,3))
_CiscoAtmSFrIwfMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoAtmSFrIwfMIBCompliances=_CiscoAtmSFrIwfMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,112,3,1))
_CiscoAtmSFrIwfMIBGroups_ObjectIdentity=ObjectIdentity
ciscoAtmSFrIwfMIBGroups=_CiscoAtmSFrIwfMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,112,3,2))
ciscoAtmSFrIwfConfConnGroup=ObjectGroup((1,3,6,1,4,1,9,9,112,3,2,1))
ciscoAtmSFrIwfConfConnGroup.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:ciscoAtmSFrIwfConfConnGroup.setStatus(_A)
ciscoAtmSFrIwfLmiGroup=ObjectGroup((1,3,6,1,4,1,9,9,112,3,2,2))
ciscoAtmSFrIwfLmiGroup.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF)))
if mibBuilder.loadTexts:ciscoAtmSFrIwfLmiGroup.setStatus(_A)
ciscoAtmSFrIwfConfIfGroup=ObjectGroup((1,3,6,1,4,1,9,9,112,3,2,3))
ciscoAtmSFrIwfConfIfGroup.setObjects(*((_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK)))
if mibBuilder.loadTexts:ciscoAtmSFrIwfConfIfGroup.setStatus(_A)
ciscoAtmSFrIwfVcStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,112,3,2,4))
ciscoAtmSFrIwfVcStatsGroup.setObjects(*((_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ)))
if mibBuilder.loadTexts:ciscoAtmSFrIwfVcStatsGroup.setStatus(_A)
ciscoAtmSFrIwfVcIwStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,112,3,2,5))
ciscoAtmSFrIwfVcIwStatsGroup.setObjects(*((_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af)))
if mibBuilder.loadTexts:ciscoAtmSFrIwfVcIwStatsGroup.setStatus(_A)
ciscoAtmSFrIwfMappingGroup=ObjectGroup((1,3,6,1,4,1,9,9,112,3,2,6))
ciscoAtmSFrIwfMappingGroup.setObjects(*((_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak)))
if mibBuilder.loadTexts:ciscoAtmSFrIwfMappingGroup.setStatus(_A)
ciscoAtmSFrIwfMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,112,3,1,1))
ciscoAtmSFrIwfMIBCompliance.setObjects(*((_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq)))
if mibBuilder.loadTexts:ciscoAtmSFrIwfMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CasfTrafficDescrRow':CasfTrafficDescrRow,'DlciValue':DlciValue,_R:ConnectionKind,'AtmAddr':AtmAddr,'ciscoAtmSwitchFrIwfMIB':ciscoAtmSwitchFrIwfMIB,'ciscoAtmSwitchFrIwfMIBObjects':ciscoAtmSwitchFrIwfMIBObjects,'casfFrTraffic':casfFrTraffic,'casfTrafficDescrTable':casfTrafficDescrTable,'casfTrafficDescrEntry':casfTrafficDescrEntry,_P:casfTrafficDescrIndex,_b:casfTrafficDescrCIR,_c:casfTrafficDescrBc,_d:casfTrafficDescrBe,_e:casfTrafficDescrPIR,_f:casfTrafficDescrServCategory,_g:casfTrafficDescrAtmIndex,_h:casfTrafficDescrRowStatus,'casfFrVC':casfFrVC,'casfVcEndptTable':casfVcEndptTable,'casfVcEndptEntry':casfVcEndptEntry,_K:casfVcEndptDlci,_i:casfVcEndptRxTrafficDescrRow,_j:casfVcEndptTxTrafficDescrRow,_k:casfVcEndptRxNegTrafficDescrRow,_l:casfVcEndptTxNegTrafficDescrRow,_m:casfVcEndptConnKind,_n:casfVcEndptIwfType,_o:casfVcEndptClpMode,_p:casfVcEndptDeMode,_q:casfVcEndptEfciMode,_r:casfVcEndptUpcMode,_u:casfVcEndptSpvcRemoteAddr,_v:casfVcEndptSpvcRemoteType,_w:casfVcEndptSpvcRemoteDlci,_x:casfVcEndptSpvcRemoteVpi,_y:casfVcEndptSpvcRemoteVci,_s:casfVcEndptCreationTime,_t:casfVcEndptRcvdSigStatus,_z:casfVcEndptRowStatus,_A0:casfVcSignalStandardCalledIe,'casfFrInterface':casfFrInterface,'casfFrLmiTable':casfFrLmiTable,'casfFrLmiEntry':casfFrLmiEntry,_A1:casfFrLmiProtocol,_A2:casfFrLmiType,_A3:casfFrLmiUserN391,_A4:casfFrLmiUserN392,_A5:casfFrLmiUserN393,_A6:casfFrLmiUserT391,_A7:casfFrLmiNetN392,_A8:casfFrLmiNetN393,_A9:casfFrLmiNetT392,_AA:casfFrLmiEnquiryIns,_AB:casfFrLmiEnquiryOuts,_AC:casfFrLmiStatusIns,_AD:casfFrLmiStatusOuts,_AE:casfFrLmiStatusTimeouts,_AF:casfFrLmiStatusEnqTimeouts,'casfConfIfTable':casfConfIfTable,'casfConfIfEntry':casfConfIfEntry,_AG:casfConfIfAtmAddress,_AH:casfConfIfUpcIntent,_AI:casfConfIfBcDefault,_AJ:casfConfIfCledSpvcDeModeDef,_AK:casfConfIfCledSpvcClpModeDef,'casfFrCounts':casfFrCounts,'casfVcCountTable':casfVcCountTable,'casfVcCountEntry':casfVcCountEntry,_AL:casfVcCountReceivedFrames,_AM:casfVcCountReceivedOctets,_AN:casfVcCountReceivedFECNs,_AO:casfVcCountReceivedBECNs,_AP:casfVcCountReceivedDEs,_AQ:casfVcCountInDiscards,_AR:casfVcCountOutDiscards,_AS:casfVcCountSentFrames,_AT:casfVcCountSentOctets,_AU:casfVcCountSentFECNs,_AV:casfVcCountSentBECNs,_AW:casfVcCountSentDEs,_AX:casfVcCountTaggedFECNs,_AY:casfVcCountTaggedBECNs,_AZ:casfVcCountTaggedDEs,'casfVcIwfCountTable':casfVcIwfCountTable,'casfVcIwfCountEntry':casfVcIwfCountEntry,_Aa:casfVcIwfCountInUnknownProts,_Ab:casfVcIwfCountOutUnknownProts,_Ac:casfVcIwfCountReassemblyTimeouts,_Ad:casfVcIwfCountLengthErrors,_Ae:casfVcIwfCountCrcErrors,_Af:casfVcIwfCountTotalDiscardFrames,'casfMapping':casfMapping,'casfFAMapTable':casfFAMapTable,'casfFAMapEntry':casfFAMapEntry,_Y:casfFAMapDlci,_Ag:casfFAMapInternalAtmInterface,_Ah:casfFAMapInternalAtmVpi,_Ai:casfFAMapInternalAtmVci,'casfAFMapTable':casfAFMapTable,'casfAFMapEntry':casfAFMapEntry,_Z:casfAFMapAtmVpi,_a:casfAFMapAtmVci,_Aj:casfAFMapFrIndex,_Ak:casfAFMapFrDlci,'ciscoAtmSFrIwfMIBConformance':ciscoAtmSFrIwfMIBConformance,'ciscoAtmSFrIwfMIBCompliances':ciscoAtmSFrIwfMIBCompliances,'ciscoAtmSFrIwfMIBCompliance':ciscoAtmSFrIwfMIBCompliance,'ciscoAtmSFrIwfMIBGroups':ciscoAtmSFrIwfMIBGroups,_Al:ciscoAtmSFrIwfConfConnGroup,_Am:ciscoAtmSFrIwfLmiGroup,_An:ciscoAtmSFrIwfConfIfGroup,_Ao:ciscoAtmSFrIwfVcStatsGroup,_Ap:ciscoAtmSFrIwfVcIwStatsGroup,_Aq:ciscoAtmSFrIwfMappingGroup})