_m='hwMplsLdpEntityFailedInitSessionThreshold'
_l='hwMplsLdpEntityStatsEntry'
_k='hwMplsLdpCrlspErHopIndex'
_j='bits per second'
_i='hwMplsLdpHelloAdjacencyIndex'
_h='hwMplsLdpPeerConfAtmLabelRangeLowerBoundVCI'
_g='hwMplsLdpPeerConfAtmLabelRangeLowerBoundVPI'
_f='hwMplsLdpEntityConfAtmLabelRangeLowerBoundVCI'
_e='hwMplsLdpEntityConfAtmLabelRangeLowerBoundVPI'
_d='downstreamUnsolicited'
_c='downstreamOnDemand'
_b='AtmVcIdentifier'
_a='AtmVpIdentifier'
_Z='accessible-for-notify'
_Y='disabled'
_X='enabled'
_W='PhysAddress'
_V='DisplayString'
_U='hwMplsLdpSessionState'
_T='hwMplsLdpSessionID'
_S='bytes'
_R='BitRate'
_Q='hwMplsLdpSessionIndex'
_P='seconds'
_O='BurstSize'
_N='TruthValue'
_M='hwMplsLdpPeerIndex'
_L='Unsigned32'
_K='hwMplsLdpCrlspTnlIndex'
_J='hwMplsLdpEntityID'
_I='hwMplsLdpEntityIfIndex'
_H='not-accessible'
_G='read-only'
_F='read-write'
_E='hwMplsLdpLsrIncarnID'
_D='Integer32'
_C='read-create'
_B='HUAWEI-MPLS-LDP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hwMpls,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','hwMpls')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_V,_W,'RowStatus','TextualConvention','TimeInterval',_N)
hwMplsLdp=ModuleIdentity((1,3,6,1,4,1,2011,5,12,2))
if mibBuilder.loadTexts:hwMplsLdp.setRevisions(('1996-11-08 21:55',))
class DisplayString(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class PhysAddress(OctetString):0
class BitRate(Integer32):0
class BurstSize(Integer32):0
class MplsLsrIdentifier(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class MplsLdpGenAddr(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
class MplsLdpIdentifier(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class AtmVpIdentifier(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
class AtmVcIdentifier(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class AddressFamilyNumbers(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('other',0),('ipv4',1),('ipv6',2),('nsap',3),('hdlc',4),('bbn1822',5),('ieee802',6),('e163',7),('e164',8),('f69',9),('x121',10),('ipx',11),('appleTalk',12),('decnetIV',13),('banyanVines',14),('e164WithNsap',15)))
class MplsLabel(TextualConvention,Integer32):status=_A
class MplsTunnelIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwMplsLdpObjects_ObjectIdentity=ObjectIdentity
hwMplsLdpObjects=_HwMplsLdpObjects_ObjectIdentity((1,3,6,1,4,1,2011,5,12,2,1))
_HwMplsLdpLsrObjects_ObjectIdentity=ObjectIdentity
hwMplsLdpLsrObjects=_HwMplsLdpLsrObjects_ObjectIdentity((1,3,6,1,4,1,2011,5,12,2,1,1))
_HwMplsLdpLsrIncarnTable_Object=MibTable
hwMplsLdpLsrIncarnTable=_HwMplsLdpLsrIncarnTable_Object((1,3,6,1,4,1,2011,5,12,2,1,1,1))
if mibBuilder.loadTexts:hwMplsLdpLsrIncarnTable.setStatus(_A)
_HwMplsLdpLsrIncarnEntry_Object=MibTableRow
hwMplsLdpLsrIncarnEntry=_HwMplsLdpLsrIncarnEntry_Object((1,3,6,1,4,1,2011,5,12,2,1,1,1,1))
hwMplsLdpLsrIncarnEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:hwMplsLdpLsrIncarnEntry.setStatus(_A)
_HwMplsLdpLsrID_Type=MplsLsrIdentifier
_HwMplsLdpLsrID_Object=MibTableColumn
hwMplsLdpLsrID=_HwMplsLdpLsrID_Object((1,3,6,1,4,1,2011,5,12,2,1,1,1,1,1),_HwMplsLdpLsrID_Type())
hwMplsLdpLsrID.setMaxAccess(_F)
if mibBuilder.loadTexts:hwMplsLdpLsrID.setStatus(_A)
class _HwMplsLdpLsrLoopDetectionPresent_Type(TruthValue):defaultValue=1
_HwMplsLdpLsrLoopDetectionPresent_Type.__name__=_N
_HwMplsLdpLsrLoopDetectionPresent_Object=MibTableColumn
hwMplsLdpLsrLoopDetectionPresent=_HwMplsLdpLsrLoopDetectionPresent_Object((1,3,6,1,4,1,2011,5,12,2,1,1,1,1,2),_HwMplsLdpLsrLoopDetectionPresent_Type())
hwMplsLdpLsrLoopDetectionPresent.setMaxAccess(_G)
if mibBuilder.loadTexts:hwMplsLdpLsrLoopDetectionPresent.setStatus(_A)
class _HwMplsLdpLsrLoopDetectionAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_HwMplsLdpLsrLoopDetectionAdminStatus_Type.__name__=_D
_HwMplsLdpLsrLoopDetectionAdminStatus_Object=MibTableColumn
hwMplsLdpLsrLoopDetectionAdminStatus=_HwMplsLdpLsrLoopDetectionAdminStatus_Object((1,3,6,1,4,1,2011,5,12,2,1,1,1,1,3),_HwMplsLdpLsrLoopDetectionAdminStatus_Type())
hwMplsLdpLsrLoopDetectionAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hwMplsLdpLsrLoopDetectionAdminStatus.setStatus(_A)
class _HwMplsLdpLsrPathVectorLimit_Type(Integer32):defaultValue=32
_HwMplsLdpLsrPathVectorLimit_Type.__name__=_D
_HwMplsLdpLsrPathVectorLimit_Object=MibTableColumn
hwMplsLdpLsrPathVectorLimit=_HwMplsLdpLsrPathVectorLimit_Object((1,3,6,1,4,1,2011,5,12,2,1,1,1,1,4),_HwMplsLdpLsrPathVectorLimit_Type())
hwMplsLdpLsrPathVectorLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:hwMplsLdpLsrPathVectorLimit.setStatus(_A)
class _HwMplsLdpLsrHopCountLimit_Type(Integer32):defaultValue=32
_HwMplsLdpLsrHopCountLimit_Type.__name__=_D
_HwMplsLdpLsrHopCountLimit_Object=MibTableColumn
hwMplsLdpLsrHopCountLimit=_HwMplsLdpLsrHopCountLimit_Object((1,3,6,1,4,1,2011,5,12,2,1,1,1,1,5),_HwMplsLdpLsrHopCountLimit_Type())
hwMplsLdpLsrHopCountLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:hwMplsLdpLsrHopCountLimit.setStatus(_A)
class _HwMplsLdpLsrLoopPreventionPresent_Type(TruthValue):defaultValue=2
_HwMplsLdpLsrLoopPreventionPresent_Type.__name__=_N
_HwMplsLdpLsrLoopPreventionPresent_Object=MibTableColumn
hwMplsLdpLsrLoopPreventionPresent=_HwMplsLdpLsrLoopPreventionPresent_Object((1,3,6,1,4,1,2011,5,12,2,1,1,1,1,6),_HwMplsLdpLsrLoopPreventionPresent_Type())
hwMplsLdpLsrLoopPreventionPresent.setMaxAccess(_G)
if mibBuilder.loadTexts:hwMplsLdpLsrLoopPreventionPresent.setStatus(_A)
class _HwMplsLdpLsrLoopPreventionAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_HwMplsLdpLsrLoopPreventionAdminStatus_Type.__name__=_D
_HwMplsLdpLsrLoopPreventionAdminStatus_Object=MibTableColumn
hwMplsLdpLsrLoopPreventionAdminStatus=_HwMplsLdpLsrLoopPreventionAdminStatus_Object((1,3,6,1,4,1,2011,5,12,2,1,1,1,1,7),_HwMplsLdpLsrLoopPreventionAdminStatus_Type())
hwMplsLdpLsrLoopPreventionAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hwMplsLdpLsrLoopPreventionAdminStatus.setStatus(_A)
class _HwMplsLdpLsrLabelRetentionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('conservative',1),('liberal',2)))
_HwMplsLdpLsrLabelRetentionMode_Type.__name__=_D
_HwMplsLdpLsrLabelRetentionMode_Object=MibTableColumn
hwMplsLdpLsrLabelRetentionMode=_HwMplsLdpLsrLabelRetentionMode_Object((1,3,6,1,4,1,2011,5,12,2,1,1,1,1,8),_HwMplsLdpLsrLabelRetentionMode_Type())
hwMplsLdpLsrLabelRetentionMode.setMaxAccess(_F)
if mibBuilder.loadTexts:hwMplsLdpLsrLabelRetentionMode.setStatus(_A)
_HwMplsLdpLsrIncarnID_Type=Integer32
_HwMplsLdpLsrIncarnID_Object=MibTableColumn
hwMplsLdpLsrIncarnID=_HwMplsLdpLsrIncarnID_Object((1,3,6,1,4,1,2011,5,12,2,1,1,1,1,9),_HwMplsLdpLsrIncarnID_Type())
hwMplsLdpLsrIncarnID.setMaxAccess(_G)
if mibBuilder.loadTexts:hwMplsLdpLsrIncarnID.setStatus(_A)
class _HwMplsLdpLsrMaxLdpEntities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_HwMplsLdpLsrMaxLdpEntities_Type.__name__=_D
_HwMplsLdpLsrMaxLdpEntities_Object=MibTableColumn
hwMplsLdpLsrMaxLdpEntities=_HwMplsLdpLsrMaxLdpEntities_Object((1,3,6,1,4,1,2011,5,12,2,1,1,1,1,10),_HwMplsLdpLsrMaxLdpEntities_Type())
hwMplsLdpLsrMaxLdpEntities.setMaxAccess(_F)
if mibBuilder.loadTexts:hwMplsLdpLsrMaxLdpEntities.setStatus(_A)
class _HwMplsLdpLsrMaxLocalPeers_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_HwMplsLdpLsrMaxLocalPeers_Type.__name__=_D
_HwMplsLdpLsrMaxLocalPeers_Object=MibTableColumn
hwMplsLdpLsrMaxLocalPeers=_HwMplsLdpLsrMaxLocalPeers_Object((1,3,6,1,4,1,2011,5,12,2,1,1,1,1,11),_HwMplsLdpLsrMaxLocalPeers_Type())
hwMplsLdpLsrMaxLocalPeers.setMaxAccess(_F)
if mibBuilder.loadTexts:hwMplsLdpLsrMaxLocalPeers.setStatus(_A)
class _HwMplsLdpLsrMaxRemotePeers_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_HwMplsLdpLsrMaxRemotePeers_Type.__name__=_D
_HwMplsLdpLsrMaxRemotePeers_Object=MibTableColumn
hwMplsLdpLsrMaxRemotePeers=_HwMplsLdpLsrMaxRemotePeers_Object((1,3,6,1,4,1,2011,5,12,2,1,1,1,1,12),_HwMplsLdpLsrMaxRemotePeers_Type())
hwMplsLdpLsrMaxRemotePeers.setMaxAccess(_F)
if mibBuilder.loadTexts:hwMplsLdpLsrMaxRemotePeers.setStatus(_A)
_HwMplsLdpLsrMaxIfaces_Type=Integer32
_HwMplsLdpLsrMaxIfaces_Object=MibTableColumn
hwMplsLdpLsrMaxIfaces=_HwMplsLdpLsrMaxIfaces_Object((1,3,6,1,4,1,2011,5,12,2,1,1,1,1,13),_HwMplsLdpLsrMaxIfaces_Type())
hwMplsLdpLsrMaxIfaces.setMaxAccess(_F)
if mibBuilder.loadTexts:hwMplsLdpLsrMaxIfaces.setStatus(_A)
_HwMplsLdpLsrMaxLsps_Type=Integer32
_HwMplsLdpLsrMaxLsps_Object=MibTableColumn
hwMplsLdpLsrMaxLsps=_HwMplsLdpLsrMaxLsps_Object((1,3,6,1,4,1,2011,5,12,2,1,1,1,1,14),_HwMplsLdpLsrMaxLsps_Type())
hwMplsLdpLsrMaxLsps.setMaxAccess(_F)
if mibBuilder.loadTexts:hwMplsLdpLsrMaxLsps.setStatus(_A)
_HwMplsLdpLsrMaxCrlspTnls_Type=Integer32
_HwMplsLdpLsrMaxCrlspTnls_Object=MibTableColumn
hwMplsLdpLsrMaxCrlspTnls=_HwMplsLdpLsrMaxCrlspTnls_Object((1,3,6,1,4,1,2011,5,12,2,1,1,1,1,15),_HwMplsLdpLsrMaxCrlspTnls_Type())
hwMplsLdpLsrMaxCrlspTnls.setMaxAccess(_F)
if mibBuilder.loadTexts:hwMplsLdpLsrMaxCrlspTnls.setStatus(_A)
_HwMplsLdpLsrMaxErhopPerCrlspTnl_Type=Integer32
_HwMplsLdpLsrMaxErhopPerCrlspTnl_Object=MibTableColumn
hwMplsLdpLsrMaxErhopPerCrlspTnl=_HwMplsLdpLsrMaxErhopPerCrlspTnl_Object((1,3,6,1,4,1,2011,5,12,2,1,1,1,1,16),_HwMplsLdpLsrMaxErhopPerCrlspTnl_Type())
hwMplsLdpLsrMaxErhopPerCrlspTnl.setMaxAccess(_F)
if mibBuilder.loadTexts:hwMplsLdpLsrMaxErhopPerCrlspTnl.setStatus(_A)
_HwMplsLdpLsrRowStatus_Type=RowStatus
_HwMplsLdpLsrRowStatus_Object=MibTableColumn
hwMplsLdpLsrRowStatus=_HwMplsLdpLsrRowStatus_Object((1,3,6,1,4,1,2011,5,12,2,1,1,1,1,17),_HwMplsLdpLsrRowStatus_Type())
hwMplsLdpLsrRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpLsrRowStatus.setStatus(_A)
_HwMplsLdpLsrMaxVcmCapability_Type=Integer32
_HwMplsLdpLsrMaxVcmCapability_Object=MibTableColumn
hwMplsLdpLsrMaxVcmCapability=_HwMplsLdpLsrMaxVcmCapability_Object((1,3,6,1,4,1,2011,5,12,2,1,1,1,1,18),_HwMplsLdpLsrMaxVcmCapability_Type())
hwMplsLdpLsrMaxVcmCapability.setMaxAccess(_F)
if mibBuilder.loadTexts:hwMplsLdpLsrMaxVcmCapability.setStatus(_A)
_HwMplsLdpLsrVcmPathVecInAllLblMapPresent_Type=TruthValue
_HwMplsLdpLsrVcmPathVecInAllLblMapPresent_Object=MibTableColumn
hwMplsLdpLsrVcmPathVecInAllLblMapPresent=_HwMplsLdpLsrVcmPathVecInAllLblMapPresent_Object((1,3,6,1,4,1,2011,5,12,2,1,1,1,1,19),_HwMplsLdpLsrVcmPathVecInAllLblMapPresent_Type())
hwMplsLdpLsrVcmPathVecInAllLblMapPresent.setMaxAccess(_F)
if mibBuilder.loadTexts:hwMplsLdpLsrVcmPathVecInAllLblMapPresent.setStatus(_A)
_HwMplsLdpLsrRequestRetrytimerValue_Type=Integer32
_HwMplsLdpLsrRequestRetrytimerValue_Object=MibTableColumn
hwMplsLdpLsrRequestRetrytimerValue=_HwMplsLdpLsrRequestRetrytimerValue_Object((1,3,6,1,4,1,2011,5,12,2,1,1,1,1,20),_HwMplsLdpLsrRequestRetrytimerValue_Type())
hwMplsLdpLsrRequestRetrytimerValue.setMaxAccess(_F)
if mibBuilder.loadTexts:hwMplsLdpLsrRequestRetrytimerValue.setStatus(_A)
_HwMplsLdpLsrNumOfRequestRetryAttempts_Type=Integer32
_HwMplsLdpLsrNumOfRequestRetryAttempts_Object=MibTableColumn
hwMplsLdpLsrNumOfRequestRetryAttempts=_HwMplsLdpLsrNumOfRequestRetryAttempts_Object((1,3,6,1,4,1,2011,5,12,2,1,1,1,1,21),_HwMplsLdpLsrNumOfRequestRetryAttempts_Type())
hwMplsLdpLsrNumOfRequestRetryAttempts.setMaxAccess(_F)
if mibBuilder.loadTexts:hwMplsLdpLsrNumOfRequestRetryAttempts.setStatus(_A)
_HwMplsLdpEntityObjects_ObjectIdentity=ObjectIdentity
hwMplsLdpEntityObjects=_HwMplsLdpEntityObjects_ObjectIdentity((1,3,6,1,4,1,2011,5,12,2,1,2))
_HwMplsLdpEntityTable_Object=MibTable
hwMplsLdpEntityTable=_HwMplsLdpEntityTable_Object((1,3,6,1,4,1,2011,5,12,2,1,2,1))
if mibBuilder.loadTexts:hwMplsLdpEntityTable.setStatus(_A)
_HwMplsLdpEntityEntry_Object=MibTableRow
hwMplsLdpEntityEntry=_HwMplsLdpEntityEntry_Object((1,3,6,1,4,1,2011,5,12,2,1,2,1,1))
hwMplsLdpEntityEntry.setIndexNames((0,_B,_E),(0,_B,_I))
if mibBuilder.loadTexts:hwMplsLdpEntityEntry.setStatus(_A)
_HwMplsLdpEntityID_Type=MplsLdpIdentifier
_HwMplsLdpEntityID_Object=MibTableColumn
hwMplsLdpEntityID=_HwMplsLdpEntityID_Object((1,3,6,1,4,1,2011,5,12,2,1,2,1,1,1),_HwMplsLdpEntityID_Type())
hwMplsLdpEntityID.setMaxAccess(_Z)
if mibBuilder.loadTexts:hwMplsLdpEntityID.setStatus(_A)
class _HwMplsLdpEntityLabelSpaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('perInterface',2),('perPlatform',3)))
_HwMplsLdpEntityLabelSpaceType_Type.__name__=_D
_HwMplsLdpEntityLabelSpaceType_Object=MibTableColumn
hwMplsLdpEntityLabelSpaceType=_HwMplsLdpEntityLabelSpaceType_Object((1,3,6,1,4,1,2011,5,12,2,1,2,1,1,2),_HwMplsLdpEntityLabelSpaceType_Type())
hwMplsLdpEntityLabelSpaceType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpEntityLabelSpaceType.setStatus(_A)
_HwMplsLdpEntityDefVpi_Type=AtmVpIdentifier
_HwMplsLdpEntityDefVpi_Object=MibTableColumn
hwMplsLdpEntityDefVpi=_HwMplsLdpEntityDefVpi_Object((1,3,6,1,4,1,2011,5,12,2,1,2,1,1,3),_HwMplsLdpEntityDefVpi_Type())
hwMplsLdpEntityDefVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpEntityDefVpi.setStatus(_A)
_HwMplsLdpEntityDefVci_Type=AtmVcIdentifier
_HwMplsLdpEntityDefVci_Object=MibTableColumn
hwMplsLdpEntityDefVci=_HwMplsLdpEntityDefVci_Object((1,3,6,1,4,1,2011,5,12,2,1,2,1,1,4),_HwMplsLdpEntityDefVci_Type())
hwMplsLdpEntityDefVci.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpEntityDefVci.setStatus(_A)
class _HwMplsLdpEntityUnlabTrafVpi_Type(AtmVpIdentifier):defaultValue=0
_HwMplsLdpEntityUnlabTrafVpi_Type.__name__=_a
_HwMplsLdpEntityUnlabTrafVpi_Object=MibTableColumn
hwMplsLdpEntityUnlabTrafVpi=_HwMplsLdpEntityUnlabTrafVpi_Object((1,3,6,1,4,1,2011,5,12,2,1,2,1,1,5),_HwMplsLdpEntityUnlabTrafVpi_Type())
hwMplsLdpEntityUnlabTrafVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpEntityUnlabTrafVpi.setStatus(_A)
class _HwMplsLdpEntityUnlabTrafVci_Type(AtmVcIdentifier):defaultValue=32
_HwMplsLdpEntityUnlabTrafVci_Type.__name__=_b
_HwMplsLdpEntityUnlabTrafVci_Object=MibTableColumn
hwMplsLdpEntityUnlabTrafVci=_HwMplsLdpEntityUnlabTrafVci_Object((1,3,6,1,4,1,2011,5,12,2,1,2,1,1,6),_HwMplsLdpEntityUnlabTrafVci_Type())
hwMplsLdpEntityUnlabTrafVci.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpEntityUnlabTrafVci.setStatus(_A)
class _HwMplsLdpEntityMergeCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noMerge',0),('vpMerge',1),('vcMerge',2),('vpVcMerge',3)))
_HwMplsLdpEntityMergeCapability_Type.__name__=_D
_HwMplsLdpEntityMergeCapability_Object=MibTableColumn
hwMplsLdpEntityMergeCapability=_HwMplsLdpEntityMergeCapability_Object((1,3,6,1,4,1,2011,5,12,2,1,2,1,1,7),_HwMplsLdpEntityMergeCapability_Type())
hwMplsLdpEntityMergeCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpEntityMergeCapability.setStatus(_A)
class _HwMplsLdpEntityVcDirectionality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bidirectional',1),('unidirectional',2)))
_HwMplsLdpEntityVcDirectionality_Type.__name__=_D
_HwMplsLdpEntityVcDirectionality_Object=MibTableColumn
hwMplsLdpEntityVcDirectionality=_HwMplsLdpEntityVcDirectionality_Object((1,3,6,1,4,1,2011,5,12,2,1,2,1,1,8),_HwMplsLdpEntityVcDirectionality_Type())
hwMplsLdpEntityVcDirectionality.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpEntityVcDirectionality.setStatus(_A)
_HwMplsLdpEntityWellKnownDiscoveryPort_Type=Integer32
_HwMplsLdpEntityWellKnownDiscoveryPort_Object=MibTableColumn
hwMplsLdpEntityWellKnownDiscoveryPort=_HwMplsLdpEntityWellKnownDiscoveryPort_Object((1,3,6,1,4,1,2011,5,12,2,1,2,1,1,9),_HwMplsLdpEntityWellKnownDiscoveryPort_Type())
hwMplsLdpEntityWellKnownDiscoveryPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpEntityWellKnownDiscoveryPort.setStatus(_A)
class _HwMplsLdpEntityMtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwMplsLdpEntityMtu_Type.__name__=_D
_HwMplsLdpEntityMtu_Object=MibTableColumn
hwMplsLdpEntityMtu=_HwMplsLdpEntityMtu_Object((1,3,6,1,4,1,2011,5,12,2,1,2,1,1,10),_HwMplsLdpEntityMtu_Type())
hwMplsLdpEntityMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpEntityMtu.setStatus(_A)
class _HwMplsLdpEntityKeepAliveHoldTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HwMplsLdpEntityKeepAliveHoldTimer_Type.__name__=_D
_HwMplsLdpEntityKeepAliveHoldTimer_Object=MibTableColumn
hwMplsLdpEntityKeepAliveHoldTimer=_HwMplsLdpEntityKeepAliveHoldTimer_Object((1,3,6,1,4,1,2011,5,12,2,1,2,1,1,11),_HwMplsLdpEntityKeepAliveHoldTimer_Type())
hwMplsLdpEntityKeepAliveHoldTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpEntityKeepAliveHoldTimer.setStatus(_A)
if mibBuilder.loadTexts:hwMplsLdpEntityKeepAliveHoldTimer.setUnits(_P)
_HwMplsLdpEntityFailedInitSessionThreshold_Type=Integer32
_HwMplsLdpEntityFailedInitSessionThreshold_Object=MibTableColumn
hwMplsLdpEntityFailedInitSessionThreshold=_HwMplsLdpEntityFailedInitSessionThreshold_Object((1,3,6,1,4,1,2011,5,12,2,1,2,1,1,12),_HwMplsLdpEntityFailedInitSessionThreshold_Type())
hwMplsLdpEntityFailedInitSessionThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpEntityFailedInitSessionThreshold.setStatus(_A)
class _HwMplsLdpEntityLabelDistributionMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_HwMplsLdpEntityLabelDistributionMethod_Type.__name__=_D
_HwMplsLdpEntityLabelDistributionMethod_Object=MibTableColumn
hwMplsLdpEntityLabelDistributionMethod=_HwMplsLdpEntityLabelDistributionMethod_Object((1,3,6,1,4,1,2011,5,12,2,1,2,1,1,13),_HwMplsLdpEntityLabelDistributionMethod_Type())
hwMplsLdpEntityLabelDistributionMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpEntityLabelDistributionMethod.setStatus(_A)
class _HwMplsLdpEntityLabelAllocationMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ordered',1),('independent',2)))
_HwMplsLdpEntityLabelAllocationMethod_Type.__name__=_D
_HwMplsLdpEntityLabelAllocationMethod_Object=MibTableColumn
hwMplsLdpEntityLabelAllocationMethod=_HwMplsLdpEntityLabelAllocationMethod_Object((1,3,6,1,4,1,2011,5,12,2,1,2,1,1,14),_HwMplsLdpEntityLabelAllocationMethod_Type())
hwMplsLdpEntityLabelAllocationMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpEntityLabelAllocationMethod.setStatus(_A)
class _HwMplsLdpEntityHelloHoldTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HwMplsLdpEntityHelloHoldTimer_Type.__name__=_D
_HwMplsLdpEntityHelloHoldTimer_Object=MibTableColumn
hwMplsLdpEntityHelloHoldTimer=_HwMplsLdpEntityHelloHoldTimer_Object((1,3,6,1,4,1,2011,5,12,2,1,2,1,1,15),_HwMplsLdpEntityHelloHoldTimer_Type())
hwMplsLdpEntityHelloHoldTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpEntityHelloHoldTimer.setStatus(_A)
if mibBuilder.loadTexts:hwMplsLdpEntityHelloHoldTimer.setUnits(_P)
_HwMplsLdpEntityRowStatus_Type=RowStatus
_HwMplsLdpEntityRowStatus_Object=MibTableColumn
hwMplsLdpEntityRowStatus=_HwMplsLdpEntityRowStatus_Object((1,3,6,1,4,1,2011,5,12,2,1,2,1,1,16),_HwMplsLdpEntityRowStatus_Type())
hwMplsLdpEntityRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpEntityRowStatus.setStatus(_A)
_HwMplsLdpEntityIfTable_Object=MibTable
hwMplsLdpEntityIfTable=_HwMplsLdpEntityIfTable_Object((1,3,6,1,4,1,2011,5,12,2,1,2,2))
if mibBuilder.loadTexts:hwMplsLdpEntityIfTable.setStatus(_A)
_HwMplsLdpEntityIfEntry_Object=MibTableRow
hwMplsLdpEntityIfEntry=_HwMplsLdpEntityIfEntry_Object((1,3,6,1,4,1,2011,5,12,2,1,2,2,1))
hwMplsLdpEntityIfEntry.setIndexNames((0,_B,_E),(0,_B,_I))
if mibBuilder.loadTexts:hwMplsLdpEntityIfEntry.setStatus(_A)
class _HwMplsLdpEntityIfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HwMplsLdpEntityIfIndex_Type.__name__=_L
_HwMplsLdpEntityIfIndex_Object=MibTableColumn
hwMplsLdpEntityIfIndex=_HwMplsLdpEntityIfIndex_Object((1,3,6,1,4,1,2011,5,12,2,1,2,2,1,1),_HwMplsLdpEntityIfIndex_Type())
hwMplsLdpEntityIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hwMplsLdpEntityIfIndex.setStatus(_A)
_HwMplsLdpEntityIfIpv4Address_Type=IpAddress
_HwMplsLdpEntityIfIpv4Address_Object=MibTableColumn
hwMplsLdpEntityIfIpv4Address=_HwMplsLdpEntityIfIpv4Address_Object((1,3,6,1,4,1,2011,5,12,2,1,2,2,1,2),_HwMplsLdpEntityIfIpv4Address_Type())
hwMplsLdpEntityIfIpv4Address.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpEntityIfIpv4Address.setStatus(_A)
_HwMplsLdpEntityIfRowStatus_Type=RowStatus
_HwMplsLdpEntityIfRowStatus_Object=MibTableColumn
hwMplsLdpEntityIfRowStatus=_HwMplsLdpEntityIfRowStatus_Object((1,3,6,1,4,1,2011,5,12,2,1,2,2,1,3),_HwMplsLdpEntityIfRowStatus_Type())
hwMplsLdpEntityIfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpEntityIfRowStatus.setStatus(_A)
_HwMplsLdpEntityConfAtmLabelRangeTable_Object=MibTable
hwMplsLdpEntityConfAtmLabelRangeTable=_HwMplsLdpEntityConfAtmLabelRangeTable_Object((1,3,6,1,4,1,2011,5,12,2,1,2,3))
if mibBuilder.loadTexts:hwMplsLdpEntityConfAtmLabelRangeTable.setStatus(_A)
_HwMplsLdpEntityConfAtmLabelRangeEntry_Object=MibTableRow
hwMplsLdpEntityConfAtmLabelRangeEntry=_HwMplsLdpEntityConfAtmLabelRangeEntry_Object((1,3,6,1,4,1,2011,5,12,2,1,2,3,1))
hwMplsLdpEntityConfAtmLabelRangeEntry.setIndexNames((0,_B,_E),(0,_B,_I),(0,_B,_e),(0,_B,_f))
if mibBuilder.loadTexts:hwMplsLdpEntityConfAtmLabelRangeEntry.setStatus(_A)
_HwMplsLdpEntityConfAtmLabelRangeLowerBoundVPI_Type=AtmVpIdentifier
_HwMplsLdpEntityConfAtmLabelRangeLowerBoundVPI_Object=MibTableColumn
hwMplsLdpEntityConfAtmLabelRangeLowerBoundVPI=_HwMplsLdpEntityConfAtmLabelRangeLowerBoundVPI_Object((1,3,6,1,4,1,2011,5,12,2,1,2,3,1,1),_HwMplsLdpEntityConfAtmLabelRangeLowerBoundVPI_Type())
hwMplsLdpEntityConfAtmLabelRangeLowerBoundVPI.setMaxAccess(_H)
if mibBuilder.loadTexts:hwMplsLdpEntityConfAtmLabelRangeLowerBoundVPI.setStatus(_A)
_HwMplsLdpEntityConfAtmLabelRangeLowerBoundVCI_Type=AtmVcIdentifier
_HwMplsLdpEntityConfAtmLabelRangeLowerBoundVCI_Object=MibTableColumn
hwMplsLdpEntityConfAtmLabelRangeLowerBoundVCI=_HwMplsLdpEntityConfAtmLabelRangeLowerBoundVCI_Object((1,3,6,1,4,1,2011,5,12,2,1,2,3,1,2),_HwMplsLdpEntityConfAtmLabelRangeLowerBoundVCI_Type())
hwMplsLdpEntityConfAtmLabelRangeLowerBoundVCI.setMaxAccess(_H)
if mibBuilder.loadTexts:hwMplsLdpEntityConfAtmLabelRangeLowerBoundVCI.setStatus(_A)
_HwMplsLdpEntityConfAtmLabelRangeUpperBoundVPI_Type=AtmVpIdentifier
_HwMplsLdpEntityConfAtmLabelRangeUpperBoundVPI_Object=MibTableColumn
hwMplsLdpEntityConfAtmLabelRangeUpperBoundVPI=_HwMplsLdpEntityConfAtmLabelRangeUpperBoundVPI_Object((1,3,6,1,4,1,2011,5,12,2,1,2,3,1,3),_HwMplsLdpEntityConfAtmLabelRangeUpperBoundVPI_Type())
hwMplsLdpEntityConfAtmLabelRangeUpperBoundVPI.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpEntityConfAtmLabelRangeUpperBoundVPI.setStatus(_A)
_HwMplsLdpEntityConfAtmLabelRangeUpperBoundVCI_Type=AtmVcIdentifier
_HwMplsLdpEntityConfAtmLabelRangeUpperBoundVCI_Object=MibTableColumn
hwMplsLdpEntityConfAtmLabelRangeUpperBoundVCI=_HwMplsLdpEntityConfAtmLabelRangeUpperBoundVCI_Object((1,3,6,1,4,1,2011,5,12,2,1,2,3,1,4),_HwMplsLdpEntityConfAtmLabelRangeUpperBoundVCI_Type())
hwMplsLdpEntityConfAtmLabelRangeUpperBoundVCI.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpEntityConfAtmLabelRangeUpperBoundVCI.setStatus(_A)
_HwMplsLdpEntityConfAtmLabelRangeRowStatus_Type=RowStatus
_HwMplsLdpEntityConfAtmLabelRangeRowStatus_Object=MibTableColumn
hwMplsLdpEntityConfAtmLabelRangeRowStatus=_HwMplsLdpEntityConfAtmLabelRangeRowStatus_Object((1,3,6,1,4,1,2011,5,12,2,1,2,3,1,5),_HwMplsLdpEntityConfAtmLabelRangeRowStatus_Type())
hwMplsLdpEntityConfAtmLabelRangeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpEntityConfAtmLabelRangeRowStatus.setStatus(_A)
_HwMplsLdpEntityStatsTable_Object=MibTable
hwMplsLdpEntityStatsTable=_HwMplsLdpEntityStatsTable_Object((1,3,6,1,4,1,2011,5,12,2,1,2,4))
if mibBuilder.loadTexts:hwMplsLdpEntityStatsTable.setStatus(_A)
_HwMplsLdpEntityStatsEntry_Object=MibTableRow
hwMplsLdpEntityStatsEntry=_HwMplsLdpEntityStatsEntry_Object((1,3,6,1,4,1,2011,5,12,2,1,2,4,1))
if mibBuilder.loadTexts:hwMplsLdpEntityStatsEntry.setStatus(_A)
_HwMplsLdpAttemptedSessions_Type=Counter32
_HwMplsLdpAttemptedSessions_Object=MibTableColumn
hwMplsLdpAttemptedSessions=_HwMplsLdpAttemptedSessions_Object((1,3,6,1,4,1,2011,5,12,2,1,2,4,1,1),_HwMplsLdpAttemptedSessions_Type())
hwMplsLdpAttemptedSessions.setMaxAccess(_G)
if mibBuilder.loadTexts:hwMplsLdpAttemptedSessions.setStatus(_A)
_HwMplsLdpPeerObjects_ObjectIdentity=ObjectIdentity
hwMplsLdpPeerObjects=_HwMplsLdpPeerObjects_ObjectIdentity((1,3,6,1,4,1,2011,5,12,2,1,3))
_HwMplsLdpPeerTable_Object=MibTable
hwMplsLdpPeerTable=_HwMplsLdpPeerTable_Object((1,3,6,1,4,1,2011,5,12,2,1,3,1))
if mibBuilder.loadTexts:hwMplsLdpPeerTable.setStatus(_A)
_HwMplsLdpPeerEntry_Object=MibTableRow
hwMplsLdpPeerEntry=_HwMplsLdpPeerEntry_Object((1,3,6,1,4,1,2011,5,12,2,1,3,1,1))
hwMplsLdpPeerEntry.setIndexNames((0,_B,_E),(0,_B,_I),(0,_B,_M))
if mibBuilder.loadTexts:hwMplsLdpPeerEntry.setStatus(_A)
class _HwMplsLdpPeerIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HwMplsLdpPeerIndex_Type.__name__=_L
_HwMplsLdpPeerIndex_Object=MibTableColumn
hwMplsLdpPeerIndex=_HwMplsLdpPeerIndex_Object((1,3,6,1,4,1,2011,5,12,2,1,3,1,1,1),_HwMplsLdpPeerIndex_Type())
hwMplsLdpPeerIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hwMplsLdpPeerIndex.setStatus(_A)
_HwMplsLdpPeerID_Type=MplsLdpIdentifier
_HwMplsLdpPeerID_Object=MibTableColumn
hwMplsLdpPeerID=_HwMplsLdpPeerID_Object((1,3,6,1,4,1,2011,5,12,2,1,3,1,1,2),_HwMplsLdpPeerID_Type())
hwMplsLdpPeerID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpPeerID.setStatus(_A)
_HwMplsLdpPeerInternetworkAddrType_Type=AddressFamilyNumbers
_HwMplsLdpPeerInternetworkAddrType_Object=MibTableColumn
hwMplsLdpPeerInternetworkAddrType=_HwMplsLdpPeerInternetworkAddrType_Object((1,3,6,1,4,1,2011,5,12,2,1,3,1,1,3),_HwMplsLdpPeerInternetworkAddrType_Type())
hwMplsLdpPeerInternetworkAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpPeerInternetworkAddrType.setStatus(_A)
_HwMplsLdpPeerInternetworkAddr_Type=MplsLdpGenAddr
_HwMplsLdpPeerInternetworkAddr_Object=MibTableColumn
hwMplsLdpPeerInternetworkAddr=_HwMplsLdpPeerInternetworkAddr_Object((1,3,6,1,4,1,2011,5,12,2,1,3,1,1,4),_HwMplsLdpPeerInternetworkAddr_Type())
hwMplsLdpPeerInternetworkAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpPeerInternetworkAddr.setStatus(_A)
class _HwMplsLdpPeerDefaultMtu_Type(Integer32):defaultValue=9180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwMplsLdpPeerDefaultMtu_Type.__name__=_D
_HwMplsLdpPeerDefaultMtu_Object=MibTableColumn
hwMplsLdpPeerDefaultMtu=_HwMplsLdpPeerDefaultMtu_Object((1,3,6,1,4,1,2011,5,12,2,1,3,1,1,5),_HwMplsLdpPeerDefaultMtu_Type())
hwMplsLdpPeerDefaultMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpPeerDefaultMtu.setStatus(_A)
class _HwMplsLdpPeerKeepAliveHoldTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HwMplsLdpPeerKeepAliveHoldTimer_Type.__name__=_D
_HwMplsLdpPeerKeepAliveHoldTimer_Object=MibTableColumn
hwMplsLdpPeerKeepAliveHoldTimer=_HwMplsLdpPeerKeepAliveHoldTimer_Object((1,3,6,1,4,1,2011,5,12,2,1,3,1,1,6),_HwMplsLdpPeerKeepAliveHoldTimer_Type())
hwMplsLdpPeerKeepAliveHoldTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpPeerKeepAliveHoldTimer.setStatus(_A)
if mibBuilder.loadTexts:hwMplsLdpPeerKeepAliveHoldTimer.setUnits(_P)
class _HwMplsLdpPeerLabelDistributionMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_HwMplsLdpPeerLabelDistributionMethod_Type.__name__=_D
_HwMplsLdpPeerLabelDistributionMethod_Object=MibTableColumn
hwMplsLdpPeerLabelDistributionMethod=_HwMplsLdpPeerLabelDistributionMethod_Object((1,3,6,1,4,1,2011,5,12,2,1,3,1,1,7),_HwMplsLdpPeerLabelDistributionMethod_Type())
hwMplsLdpPeerLabelDistributionMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpPeerLabelDistributionMethod.setStatus(_A)
class _HwMplsLdpPeerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
_HwMplsLdpPeerType_Type.__name__=_D
_HwMplsLdpPeerType_Object=MibTableColumn
hwMplsLdpPeerType=_HwMplsLdpPeerType_Object((1,3,6,1,4,1,2011,5,12,2,1,3,1,1,8),_HwMplsLdpPeerType_Type())
hwMplsLdpPeerType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpPeerType.setStatus(_A)
_HwMplsLdpPeerRowStatus_Type=RowStatus
_HwMplsLdpPeerRowStatus_Object=MibTableColumn
hwMplsLdpPeerRowStatus=_HwMplsLdpPeerRowStatus_Object((1,3,6,1,4,1,2011,5,12,2,1,3,1,1,9),_HwMplsLdpPeerRowStatus_Type())
hwMplsLdpPeerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpPeerRowStatus.setStatus(_A)
_HwMplsLdpPeerConfAtmLabelRangeTable_Object=MibTable
hwMplsLdpPeerConfAtmLabelRangeTable=_HwMplsLdpPeerConfAtmLabelRangeTable_Object((1,3,6,1,4,1,2011,5,12,2,1,3,2))
if mibBuilder.loadTexts:hwMplsLdpPeerConfAtmLabelRangeTable.setStatus(_A)
_HwMplsLdpPeerConfAtmLabelRangeEntry_Object=MibTableRow
hwMplsLdpPeerConfAtmLabelRangeEntry=_HwMplsLdpPeerConfAtmLabelRangeEntry_Object((1,3,6,1,4,1,2011,5,12,2,1,3,2,1))
hwMplsLdpPeerConfAtmLabelRangeEntry.setIndexNames((0,_B,_E),(0,_B,_I),(0,_B,_M),(0,_B,_g),(0,_B,_h))
if mibBuilder.loadTexts:hwMplsLdpPeerConfAtmLabelRangeEntry.setStatus(_A)
_HwMplsLdpPeerConfAtmLabelRangeLowerBoundVPI_Type=AtmVpIdentifier
_HwMplsLdpPeerConfAtmLabelRangeLowerBoundVPI_Object=MibTableColumn
hwMplsLdpPeerConfAtmLabelRangeLowerBoundVPI=_HwMplsLdpPeerConfAtmLabelRangeLowerBoundVPI_Object((1,3,6,1,4,1,2011,5,12,2,1,3,2,1,1),_HwMplsLdpPeerConfAtmLabelRangeLowerBoundVPI_Type())
hwMplsLdpPeerConfAtmLabelRangeLowerBoundVPI.setMaxAccess(_H)
if mibBuilder.loadTexts:hwMplsLdpPeerConfAtmLabelRangeLowerBoundVPI.setStatus(_A)
_HwMplsLdpPeerConfAtmLabelRangeLowerBoundVCI_Type=AtmVcIdentifier
_HwMplsLdpPeerConfAtmLabelRangeLowerBoundVCI_Object=MibTableColumn
hwMplsLdpPeerConfAtmLabelRangeLowerBoundVCI=_HwMplsLdpPeerConfAtmLabelRangeLowerBoundVCI_Object((1,3,6,1,4,1,2011,5,12,2,1,3,2,1,2),_HwMplsLdpPeerConfAtmLabelRangeLowerBoundVCI_Type())
hwMplsLdpPeerConfAtmLabelRangeLowerBoundVCI.setMaxAccess(_H)
if mibBuilder.loadTexts:hwMplsLdpPeerConfAtmLabelRangeLowerBoundVCI.setStatus(_A)
_HwMplsLdpPeerConfAtmLabelRangeUpperBoundVPI_Type=AtmVpIdentifier
_HwMplsLdpPeerConfAtmLabelRangeUpperBoundVPI_Object=MibTableColumn
hwMplsLdpPeerConfAtmLabelRangeUpperBoundVPI=_HwMplsLdpPeerConfAtmLabelRangeUpperBoundVPI_Object((1,3,6,1,4,1,2011,5,12,2,1,3,2,1,3),_HwMplsLdpPeerConfAtmLabelRangeUpperBoundVPI_Type())
hwMplsLdpPeerConfAtmLabelRangeUpperBoundVPI.setMaxAccess(_G)
if mibBuilder.loadTexts:hwMplsLdpPeerConfAtmLabelRangeUpperBoundVPI.setStatus(_A)
_HwMplsLdpPeerConfAtmLabelRangeUpperBoundVCI_Type=AtmVcIdentifier
_HwMplsLdpPeerConfAtmLabelRangeUpperBoundVCI_Object=MibTableColumn
hwMplsLdpPeerConfAtmLabelRangeUpperBoundVCI=_HwMplsLdpPeerConfAtmLabelRangeUpperBoundVCI_Object((1,3,6,1,4,1,2011,5,12,2,1,3,2,1,4),_HwMplsLdpPeerConfAtmLabelRangeUpperBoundVCI_Type())
hwMplsLdpPeerConfAtmLabelRangeUpperBoundVCI.setMaxAccess(_G)
if mibBuilder.loadTexts:hwMplsLdpPeerConfAtmLabelRangeUpperBoundVCI.setStatus(_A)
_HwMplsLdpSessionObjects_ObjectIdentity=ObjectIdentity
hwMplsLdpSessionObjects=_HwMplsLdpSessionObjects_ObjectIdentity((1,3,6,1,4,1,2011,5,12,2,1,4))
_HwMplsLdpSessionTable_Object=MibTable
hwMplsLdpSessionTable=_HwMplsLdpSessionTable_Object((1,3,6,1,4,1,2011,5,12,2,1,4,1))
if mibBuilder.loadTexts:hwMplsLdpSessionTable.setStatus(_A)
_HwMplsLdpSessionEntry_Object=MibTableRow
hwMplsLdpSessionEntry=_HwMplsLdpSessionEntry_Object((1,3,6,1,4,1,2011,5,12,2,1,4,1,1))
hwMplsLdpSessionEntry.setIndexNames((0,_B,_E),(0,_B,_I),(0,_B,_M),(0,_B,_Q))
if mibBuilder.loadTexts:hwMplsLdpSessionEntry.setStatus(_A)
class _HwMplsLdpSessionIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HwMplsLdpSessionIndex_Type.__name__=_L
_HwMplsLdpSessionIndex_Object=MibTableColumn
hwMplsLdpSessionIndex=_HwMplsLdpSessionIndex_Object((1,3,6,1,4,1,2011,5,12,2,1,4,1,1,1),_HwMplsLdpSessionIndex_Type())
hwMplsLdpSessionIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hwMplsLdpSessionIndex.setStatus(_A)
_HwMplsLdpSessionID_Type=MplsLdpIdentifier
_HwMplsLdpSessionID_Object=MibTableColumn
hwMplsLdpSessionID=_HwMplsLdpSessionID_Object((1,3,6,1,4,1,2011,5,12,2,1,4,1,1,2),_HwMplsLdpSessionID_Type())
hwMplsLdpSessionID.setMaxAccess(_G)
if mibBuilder.loadTexts:hwMplsLdpSessionID.setStatus(_A)
class _HwMplsLdpSessionProtocolVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwMplsLdpSessionProtocolVersion_Type.__name__=_D
_HwMplsLdpSessionProtocolVersion_Object=MibTableColumn
hwMplsLdpSessionProtocolVersion=_HwMplsLdpSessionProtocolVersion_Object((1,3,6,1,4,1,2011,5,12,2,1,4,1,1,3),_HwMplsLdpSessionProtocolVersion_Type())
hwMplsLdpSessionProtocolVersion.setMaxAccess(_G)
if mibBuilder.loadTexts:hwMplsLdpSessionProtocolVersion.setStatus(_A)
_HwMplsLdpSessionKeepAliveHoldTimeRemaining_Type=TimeInterval
_HwMplsLdpSessionKeepAliveHoldTimeRemaining_Object=MibTableColumn
hwMplsLdpSessionKeepAliveHoldTimeRemaining=_HwMplsLdpSessionKeepAliveHoldTimeRemaining_Object((1,3,6,1,4,1,2011,5,12,2,1,4,1,1,4),_HwMplsLdpSessionKeepAliveHoldTimeRemaining_Type())
hwMplsLdpSessionKeepAliveHoldTimeRemaining.setMaxAccess(_G)
if mibBuilder.loadTexts:hwMplsLdpSessionKeepAliveHoldTimeRemaining.setStatus(_A)
class _HwMplsLdpSessionRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('passive',2)))
_HwMplsLdpSessionRole_Type.__name__=_D
_HwMplsLdpSessionRole_Object=MibTableColumn
hwMplsLdpSessionRole=_HwMplsLdpSessionRole_Object((1,3,6,1,4,1,2011,5,12,2,1,4,1,1,5),_HwMplsLdpSessionRole_Type())
hwMplsLdpSessionRole.setMaxAccess(_G)
if mibBuilder.loadTexts:hwMplsLdpSessionRole.setStatus(_A)
class _HwMplsLdpSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('nonexistent',1),('initialized',2),('openrec',3),('opensent',4),('operational',5)))
_HwMplsLdpSessionState_Type.__name__=_D
_HwMplsLdpSessionState_Object=MibTableColumn
hwMplsLdpSessionState=_HwMplsLdpSessionState_Object((1,3,6,1,4,1,2011,5,12,2,1,4,1,1,6),_HwMplsLdpSessionState_Type())
hwMplsLdpSessionState.setMaxAccess(_G)
if mibBuilder.loadTexts:hwMplsLdpSessionState.setStatus(_A)
_HwMplsLdpSessionAtmLabelRangeLowerBoundVPI_Type=AtmVpIdentifier
_HwMplsLdpSessionAtmLabelRangeLowerBoundVPI_Object=MibTableColumn
hwMplsLdpSessionAtmLabelRangeLowerBoundVPI=_HwMplsLdpSessionAtmLabelRangeLowerBoundVPI_Object((1,3,6,1,4,1,2011,5,12,2,1,4,1,1,7),_HwMplsLdpSessionAtmLabelRangeLowerBoundVPI_Type())
hwMplsLdpSessionAtmLabelRangeLowerBoundVPI.setMaxAccess(_G)
if mibBuilder.loadTexts:hwMplsLdpSessionAtmLabelRangeLowerBoundVPI.setStatus(_A)
_HwMplsLdpSessionAtmLabelRangeLowerBoundVCI_Type=AtmVcIdentifier
_HwMplsLdpSessionAtmLabelRangeLowerBoundVCI_Object=MibTableColumn
hwMplsLdpSessionAtmLabelRangeLowerBoundVCI=_HwMplsLdpSessionAtmLabelRangeLowerBoundVCI_Object((1,3,6,1,4,1,2011,5,12,2,1,4,1,1,8),_HwMplsLdpSessionAtmLabelRangeLowerBoundVCI_Type())
hwMplsLdpSessionAtmLabelRangeLowerBoundVCI.setMaxAccess(_G)
if mibBuilder.loadTexts:hwMplsLdpSessionAtmLabelRangeLowerBoundVCI.setStatus(_A)
_HwMplsLdpSessionAtmLabelRangeUpperBoundVPI_Type=AtmVpIdentifier
_HwMplsLdpSessionAtmLabelRangeUpperBoundVPI_Object=MibTableColumn
hwMplsLdpSessionAtmLabelRangeUpperBoundVPI=_HwMplsLdpSessionAtmLabelRangeUpperBoundVPI_Object((1,3,6,1,4,1,2011,5,12,2,1,4,1,1,9),_HwMplsLdpSessionAtmLabelRangeUpperBoundVPI_Type())
hwMplsLdpSessionAtmLabelRangeUpperBoundVPI.setMaxAccess(_G)
if mibBuilder.loadTexts:hwMplsLdpSessionAtmLabelRangeUpperBoundVPI.setStatus(_A)
_HwMplsLdpSessionAtmLabelRangeUpperBoundVCI_Type=AtmVcIdentifier
_HwMplsLdpSessionAtmLabelRangeUpperBoundVCI_Object=MibTableColumn
hwMplsLdpSessionAtmLabelRangeUpperBoundVCI=_HwMplsLdpSessionAtmLabelRangeUpperBoundVCI_Object((1,3,6,1,4,1,2011,5,12,2,1,4,1,1,10),_HwMplsLdpSessionAtmLabelRangeUpperBoundVCI_Type())
hwMplsLdpSessionAtmLabelRangeUpperBoundVCI.setMaxAccess(_G)
if mibBuilder.loadTexts:hwMplsLdpSessionAtmLabelRangeUpperBoundVCI.setStatus(_A)
_HwMplsLdpHelloAdjacencyObjects_ObjectIdentity=ObjectIdentity
hwMplsLdpHelloAdjacencyObjects=_HwMplsLdpHelloAdjacencyObjects_ObjectIdentity((1,3,6,1,4,1,2011,5,12,2,1,5))
_HwMplsLdpHelloAdjacencyTable_Object=MibTable
hwMplsLdpHelloAdjacencyTable=_HwMplsLdpHelloAdjacencyTable_Object((1,3,6,1,4,1,2011,5,12,2,1,5,1))
if mibBuilder.loadTexts:hwMplsLdpHelloAdjacencyTable.setStatus(_A)
_HwMplsLdpHelloAdjacencyEntry_Object=MibTableRow
hwMplsLdpHelloAdjacencyEntry=_HwMplsLdpHelloAdjacencyEntry_Object((1,3,6,1,4,1,2011,5,12,2,1,5,1,1))
hwMplsLdpHelloAdjacencyEntry.setIndexNames((0,_B,_E),(0,_B,_I),(0,_B,_M),(0,_B,_Q),(0,_B,_i))
if mibBuilder.loadTexts:hwMplsLdpHelloAdjacencyEntry.setStatus(_A)
class _HwMplsLdpHelloAdjacencyIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HwMplsLdpHelloAdjacencyIndex_Type.__name__=_L
_HwMplsLdpHelloAdjacencyIndex_Object=MibTableColumn
hwMplsLdpHelloAdjacencyIndex=_HwMplsLdpHelloAdjacencyIndex_Object((1,3,6,1,4,1,2011,5,12,2,1,5,1,1,1),_HwMplsLdpHelloAdjacencyIndex_Type())
hwMplsLdpHelloAdjacencyIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hwMplsLdpHelloAdjacencyIndex.setStatus(_A)
_HwMplsLdpHelloAdjacencyHoldTimeRemaining_Type=TimeInterval
_HwMplsLdpHelloAdjacencyHoldTimeRemaining_Object=MibTableColumn
hwMplsLdpHelloAdjacencyHoldTimeRemaining=_HwMplsLdpHelloAdjacencyHoldTimeRemaining_Object((1,3,6,1,4,1,2011,5,12,2,1,5,1,1,2),_HwMplsLdpHelloAdjacencyHoldTimeRemaining_Type())
hwMplsLdpHelloAdjacencyHoldTimeRemaining.setMaxAccess(_G)
if mibBuilder.loadTexts:hwMplsLdpHelloAdjacencyHoldTimeRemaining.setStatus(_A)
_HwMplsLdpCrlspTnlObjects_ObjectIdentity=ObjectIdentity
hwMplsLdpCrlspTnlObjects=_HwMplsLdpCrlspTnlObjects_ObjectIdentity((1,3,6,1,4,1,2011,5,12,2,1,6))
_HwMplsLdpCrlspTnlTable_Object=MibTable
hwMplsLdpCrlspTnlTable=_HwMplsLdpCrlspTnlTable_Object((1,3,6,1,4,1,2011,5,12,2,1,6,1))
if mibBuilder.loadTexts:hwMplsLdpCrlspTnlTable.setStatus(_A)
_HwMplsLdpCrlspTnlEntry_Object=MibTableRow
hwMplsLdpCrlspTnlEntry=_HwMplsLdpCrlspTnlEntry_Object((1,3,6,1,4,1,2011,5,12,2,1,6,1,1))
hwMplsLdpCrlspTnlEntry.setIndexNames((0,_B,_E),(0,_B,_K))
if mibBuilder.loadTexts:hwMplsLdpCrlspTnlEntry.setStatus(_A)
_HwMplsLdpCrlspTnlIndex_Type=MplsTunnelIndex
_HwMplsLdpCrlspTnlIndex_Object=MibTableColumn
hwMplsLdpCrlspTnlIndex=_HwMplsLdpCrlspTnlIndex_Object((1,3,6,1,4,1,2011,5,12,2,1,6,1,1,1),_HwMplsLdpCrlspTnlIndex_Type())
hwMplsLdpCrlspTnlIndex.setMaxAccess(_Z)
if mibBuilder.loadTexts:hwMplsLdpCrlspTnlIndex.setStatus(_A)
_HwMplsLdpCrlspTnlName_Type=DisplayString
_HwMplsLdpCrlspTnlName_Object=MibTableColumn
hwMplsLdpCrlspTnlName=_HwMplsLdpCrlspTnlName_Object((1,3,6,1,4,1,2011,5,12,2,1,6,1,1,2),_HwMplsLdpCrlspTnlName_Type())
hwMplsLdpCrlspTnlName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpCrlspTnlName.setStatus(_A)
class _HwMplsLdpCrlspTnlDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('in',1),('out',2),('inOut',3)))
_HwMplsLdpCrlspTnlDirection_Type.__name__=_D
_HwMplsLdpCrlspTnlDirection_Object=MibTableColumn
hwMplsLdpCrlspTnlDirection=_HwMplsLdpCrlspTnlDirection_Object((1,3,6,1,4,1,2011,5,12,2,1,6,1,1,3),_HwMplsLdpCrlspTnlDirection_Type())
hwMplsLdpCrlspTnlDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpCrlspTnlDirection.setStatus(_A)
class _HwMplsLdpCrlspTnlSignallingProto_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('ldp',2),('rsvp',3)))
_HwMplsLdpCrlspTnlSignallingProto_Type.__name__=_D
_HwMplsLdpCrlspTnlSignallingProto_Object=MibTableColumn
hwMplsLdpCrlspTnlSignallingProto=_HwMplsLdpCrlspTnlSignallingProto_Object((1,3,6,1,4,1,2011,5,12,2,1,6,1,1,4),_HwMplsLdpCrlspTnlSignallingProto_Type())
hwMplsLdpCrlspTnlSignallingProto.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpCrlspTnlSignallingProto.setStatus(_A)
class _HwMplsLdpCrlspTnlSetupPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HwMplsLdpCrlspTnlSetupPrio_Type.__name__=_D
_HwMplsLdpCrlspTnlSetupPrio_Object=MibTableColumn
hwMplsLdpCrlspTnlSetupPrio=_HwMplsLdpCrlspTnlSetupPrio_Object((1,3,6,1,4,1,2011,5,12,2,1,6,1,1,5),_HwMplsLdpCrlspTnlSetupPrio_Type())
hwMplsLdpCrlspTnlSetupPrio.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpCrlspTnlSetupPrio.setStatus(_A)
class _HwMplsLdpCrlspTnlHoldingPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HwMplsLdpCrlspTnlHoldingPrio_Type.__name__=_D
_HwMplsLdpCrlspTnlHoldingPrio_Object=MibTableColumn
hwMplsLdpCrlspTnlHoldingPrio=_HwMplsLdpCrlspTnlHoldingPrio_Object((1,3,6,1,4,1,2011,5,12,2,1,6,1,1,6),_HwMplsLdpCrlspTnlHoldingPrio_Type())
hwMplsLdpCrlspTnlHoldingPrio.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpCrlspTnlHoldingPrio.setStatus(_A)
class _HwMplsLdpCrlspTnlPeakDataRate_Type(BitRate):defaultValue=0
_HwMplsLdpCrlspTnlPeakDataRate_Type.__name__=_R
_HwMplsLdpCrlspTnlPeakDataRate_Object=MibTableColumn
hwMplsLdpCrlspTnlPeakDataRate=_HwMplsLdpCrlspTnlPeakDataRate_Object((1,3,6,1,4,1,2011,5,12,2,1,6,1,1,7),_HwMplsLdpCrlspTnlPeakDataRate_Type())
hwMplsLdpCrlspTnlPeakDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpCrlspTnlPeakDataRate.setStatus(_A)
if mibBuilder.loadTexts:hwMplsLdpCrlspTnlPeakDataRate.setUnits(_j)
class _HwMplsLdpCrlspTnlPeakBurstSize_Type(BurstSize):defaultValue=0
_HwMplsLdpCrlspTnlPeakBurstSize_Type.__name__=_O
_HwMplsLdpCrlspTnlPeakBurstSize_Object=MibTableColumn
hwMplsLdpCrlspTnlPeakBurstSize=_HwMplsLdpCrlspTnlPeakBurstSize_Object((1,3,6,1,4,1,2011,5,12,2,1,6,1,1,8),_HwMplsLdpCrlspTnlPeakBurstSize_Type())
hwMplsLdpCrlspTnlPeakBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpCrlspTnlPeakBurstSize.setStatus(_A)
if mibBuilder.loadTexts:hwMplsLdpCrlspTnlPeakBurstSize.setUnits(_S)
class _HwMplsLdpCrlspTnlCommittedDataRate_Type(BitRate):defaultValue=0
_HwMplsLdpCrlspTnlCommittedDataRate_Type.__name__=_R
_HwMplsLdpCrlspTnlCommittedDataRate_Object=MibTableColumn
hwMplsLdpCrlspTnlCommittedDataRate=_HwMplsLdpCrlspTnlCommittedDataRate_Object((1,3,6,1,4,1,2011,5,12,2,1,6,1,1,9),_HwMplsLdpCrlspTnlCommittedDataRate_Type())
hwMplsLdpCrlspTnlCommittedDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpCrlspTnlCommittedDataRate.setStatus(_A)
if mibBuilder.loadTexts:hwMplsLdpCrlspTnlCommittedDataRate.setUnits(_j)
class _HwMplsLdpCrlspTnlCommittedBurstSize_Type(BurstSize):defaultValue=0
_HwMplsLdpCrlspTnlCommittedBurstSize_Type.__name__=_O
_HwMplsLdpCrlspTnlCommittedBurstSize_Object=MibTableColumn
hwMplsLdpCrlspTnlCommittedBurstSize=_HwMplsLdpCrlspTnlCommittedBurstSize_Object((1,3,6,1,4,1,2011,5,12,2,1,6,1,1,10),_HwMplsLdpCrlspTnlCommittedBurstSize_Type())
hwMplsLdpCrlspTnlCommittedBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpCrlspTnlCommittedBurstSize.setStatus(_A)
if mibBuilder.loadTexts:hwMplsLdpCrlspTnlCommittedBurstSize.setUnits(_S)
class _HwMplsLdpCrlspTnlExcessBurstSize_Type(BurstSize):defaultValue=0
_HwMplsLdpCrlspTnlExcessBurstSize_Type.__name__=_O
_HwMplsLdpCrlspTnlExcessBurstSize_Object=MibTableColumn
hwMplsLdpCrlspTnlExcessBurstSize=_HwMplsLdpCrlspTnlExcessBurstSize_Object((1,3,6,1,4,1,2011,5,12,2,1,6,1,1,11),_HwMplsLdpCrlspTnlExcessBurstSize_Type())
hwMplsLdpCrlspTnlExcessBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpCrlspTnlExcessBurstSize.setStatus(_A)
if mibBuilder.loadTexts:hwMplsLdpCrlspTnlExcessBurstSize.setUnits(_S)
class _HwMplsLdpCrlspTnlIsPinned_Type(TruthValue):defaultValue=2
_HwMplsLdpCrlspTnlIsPinned_Type.__name__=_N
_HwMplsLdpCrlspTnlIsPinned_Object=MibTableColumn
hwMplsLdpCrlspTnlIsPinned=_HwMplsLdpCrlspTnlIsPinned_Object((1,3,6,1,4,1,2011,5,12,2,1,6,1,1,12),_HwMplsLdpCrlspTnlIsPinned_Type())
hwMplsLdpCrlspTnlIsPinned.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpCrlspTnlIsPinned.setStatus(_A)
class _HwMplsLdpCrlspTnlFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HwMplsLdpCrlspTnlFrequency_Type.__name__=_D
_HwMplsLdpCrlspTnlFrequency_Object=MibTableColumn
hwMplsLdpCrlspTnlFrequency=_HwMplsLdpCrlspTnlFrequency_Object((1,3,6,1,4,1,2011,5,12,2,1,6,1,1,13),_HwMplsLdpCrlspTnlFrequency_Type())
hwMplsLdpCrlspTnlFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpCrlspTnlFrequency.setStatus(_A)
class _HwMplsLdpCrlspTnlWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HwMplsLdpCrlspTnlWeight_Type.__name__=_D
_HwMplsLdpCrlspTnlWeight_Object=MibTableColumn
hwMplsLdpCrlspTnlWeight=_HwMplsLdpCrlspTnlWeight_Object((1,3,6,1,4,1,2011,5,12,2,1,6,1,1,14),_HwMplsLdpCrlspTnlWeight_Type())
hwMplsLdpCrlspTnlWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpCrlspTnlWeight.setStatus(_A)
_HwMplsLdpCrlspTnlRowStatus_Type=RowStatus
_HwMplsLdpCrlspTnlRowStatus_Object=MibTableColumn
hwMplsLdpCrlspTnlRowStatus=_HwMplsLdpCrlspTnlRowStatus_Object((1,3,6,1,4,1,2011,5,12,2,1,6,1,1,15),_HwMplsLdpCrlspTnlRowStatus_Type())
hwMplsLdpCrlspTnlRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpCrlspTnlRowStatus.setStatus(_A)
_HwMplsLdpCrlspErHopTable_Object=MibTable
hwMplsLdpCrlspErHopTable=_HwMplsLdpCrlspErHopTable_Object((1,3,6,1,4,1,2011,5,12,2,1,6,2))
if mibBuilder.loadTexts:hwMplsLdpCrlspErHopTable.setStatus(_A)
_HwMplsLdpCrlspErHopEntry_Object=MibTableRow
hwMplsLdpCrlspErHopEntry=_HwMplsLdpCrlspErHopEntry_Object((1,3,6,1,4,1,2011,5,12,2,1,6,2,1))
hwMplsLdpCrlspErHopEntry.setIndexNames((0,_B,_E),(0,_B,_K),(0,_B,_k))
if mibBuilder.loadTexts:hwMplsLdpCrlspErHopEntry.setStatus(_A)
_HwMplsLdpCrlspErHopIndex_Type=Integer32
_HwMplsLdpCrlspErHopIndex_Object=MibTableColumn
hwMplsLdpCrlspErHopIndex=_HwMplsLdpCrlspErHopIndex_Object((1,3,6,1,4,1,2011,5,12,2,1,6,2,1,1),_HwMplsLdpCrlspErHopIndex_Type())
hwMplsLdpCrlspErHopIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hwMplsLdpCrlspErHopIndex.setStatus(_A)
class _HwMplsLdpCrlspErHopAddrType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('ipV4',1))
_HwMplsLdpCrlspErHopAddrType_Type.__name__=_D
_HwMplsLdpCrlspErHopAddrType_Object=MibTableColumn
hwMplsLdpCrlspErHopAddrType=_HwMplsLdpCrlspErHopAddrType_Object((1,3,6,1,4,1,2011,5,12,2,1,6,2,1,2),_HwMplsLdpCrlspErHopAddrType_Type())
hwMplsLdpCrlspErHopAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpCrlspErHopAddrType.setStatus(_A)
_HwMplsLdpCrlspErHopIpv4Addr_Type=IpAddress
_HwMplsLdpCrlspErHopIpv4Addr_Object=MibTableColumn
hwMplsLdpCrlspErHopIpv4Addr=_HwMplsLdpCrlspErHopIpv4Addr_Object((1,3,6,1,4,1,2011,5,12,2,1,6,2,1,3),_HwMplsLdpCrlspErHopIpv4Addr_Type())
hwMplsLdpCrlspErHopIpv4Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpCrlspErHopIpv4Addr.setStatus(_A)
class _HwMplsLdpCrlspErHopIpv4PrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_HwMplsLdpCrlspErHopIpv4PrefixLen_Type.__name__=_D
_HwMplsLdpCrlspErHopIpv4PrefixLen_Object=MibTableColumn
hwMplsLdpCrlspErHopIpv4PrefixLen=_HwMplsLdpCrlspErHopIpv4PrefixLen_Object((1,3,6,1,4,1,2011,5,12,2,1,6,2,1,4),_HwMplsLdpCrlspErHopIpv4PrefixLen_Type())
hwMplsLdpCrlspErHopIpv4PrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpCrlspErHopIpv4PrefixLen.setStatus(_A)
class _HwMplsLdpCrlspErHopStrictOrLoose_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('strict',1),('loose',2)))
_HwMplsLdpCrlspErHopStrictOrLoose_Type.__name__=_D
_HwMplsLdpCrlspErHopStrictOrLoose_Object=MibTableColumn
hwMplsLdpCrlspErHopStrictOrLoose=_HwMplsLdpCrlspErHopStrictOrLoose_Object((1,3,6,1,4,1,2011,5,12,2,1,6,2,1,5),_HwMplsLdpCrlspErHopStrictOrLoose_Type())
hwMplsLdpCrlspErHopStrictOrLoose.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpCrlspErHopStrictOrLoose.setStatus(_A)
_HwMplsLdpCrlspErHopRowStatus_Type=RowStatus
_HwMplsLdpCrlspErHopRowStatus_Object=MibTableColumn
hwMplsLdpCrlspErHopRowStatus=_HwMplsLdpCrlspErHopRowStatus_Object((1,3,6,1,4,1,2011,5,12,2,1,6,2,1,6),_HwMplsLdpCrlspErHopRowStatus_Type())
hwMplsLdpCrlspErHopRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMplsLdpCrlspErHopRowStatus.setStatus(_A)
_HwMplsLdpNotifications_ObjectIdentity=ObjectIdentity
hwMplsLdpNotifications=_HwMplsLdpNotifications_ObjectIdentity((1,3,6,1,4,1,2011,5,12,2,2))
_HwMplsLdpNotificationPrefix_ObjectIdentity=ObjectIdentity
hwMplsLdpNotificationPrefix=_HwMplsLdpNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,2011,5,12,2,2,0))
hwMplsLdpEntityEntry.registerAugmentions((_B,_l))
hwMplsLdpEntityStatsEntry.setIndexNames(*hwMplsLdpEntityEntry.getIndexNames())
hwMplsLdpFailedInitSessionThresholdExceeded=NotificationType((1,3,6,1,4,1,2011,5,12,2,2,0,1))
hwMplsLdpFailedInitSessionThresholdExceeded.setObjects(*((_B,_E),(_B,_J),(_B,_m)))
if mibBuilder.loadTexts:hwMplsLdpFailedInitSessionThresholdExceeded.setStatus(_A)
hwMplsLdpCrlspTunnelUp=NotificationType((1,3,6,1,4,1,2011,5,12,2,2,0,2))
hwMplsLdpCrlspTunnelUp.setObjects(*((_B,_E),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:hwMplsLdpCrlspTunnelUp.setStatus(_A)
hwMplsLdpCrlspTunnelDown=NotificationType((1,3,6,1,4,1,2011,5,12,2,2,0,3))
hwMplsLdpCrlspTunnelDown.setObjects(*((_B,_E),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:hwMplsLdpCrlspTunnelDown.setStatus(_A)
hwMplsLdpCrlspTunnelSetupFailure=NotificationType((1,3,6,1,4,1,2011,5,12,2,2,0,4))
hwMplsLdpCrlspTunnelSetupFailure.setObjects(*((_B,_E),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:hwMplsLdpCrlspTunnelSetupFailure.setStatus(_A)
hwMplsLdpIncarnUpEventFailure=NotificationType((1,3,6,1,4,1,2011,5,12,2,2,0,11))
hwMplsLdpIncarnUpEventFailure.setObjects((_B,_E))
if mibBuilder.loadTexts:hwMplsLdpIncarnUpEventFailure.setStatus(_A)
hwMplsLdpIncarnDownEventFailure=NotificationType((1,3,6,1,4,1,2011,5,12,2,2,0,12))
hwMplsLdpIncarnDownEventFailure.setObjects((_B,_E))
if mibBuilder.loadTexts:hwMplsLdpIncarnDownEventFailure.setStatus(_A)
hwMplsLdpEntityUpEventFailure=NotificationType((1,3,6,1,4,1,2011,5,12,2,2,0,13))
hwMplsLdpEntityUpEventFailure.setObjects(*((_B,_E),(_B,_J)))
if mibBuilder.loadTexts:hwMplsLdpEntityUpEventFailure.setStatus(_A)
hwMplsLdpEntityDownEventFailure=NotificationType((1,3,6,1,4,1,2011,5,12,2,2,0,14))
hwMplsLdpEntityDownEventFailure.setObjects(*((_B,_E),(_B,_J)))
if mibBuilder.loadTexts:hwMplsLdpEntityDownEventFailure.setStatus(_A)
hwMplsLdpSessionUpEventFailure=NotificationType((1,3,6,1,4,1,2011,5,12,2,2,0,15))
hwMplsLdpSessionUpEventFailure.setObjects(*((_B,_T),(_B,_U)))
if mibBuilder.loadTexts:hwMplsLdpSessionUpEventFailure.setStatus(_A)
hwMplsLdpSessionDownEventFailure=NotificationType((1,3,6,1,4,1,2011,5,12,2,2,0,16))
hwMplsLdpSessionDownEventFailure.setObjects(*((_B,_T),(_B,_U)))
if mibBuilder.loadTexts:hwMplsLdpSessionDownEventFailure.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_V:DisplayString,_W:PhysAddress,_R:BitRate,_O:BurstSize,'MplsLsrIdentifier':MplsLsrIdentifier,'MplsLdpGenAddr':MplsLdpGenAddr,'MplsLdpIdentifier':MplsLdpIdentifier,_a:AtmVpIdentifier,_b:AtmVcIdentifier,'AddressFamilyNumbers':AddressFamilyNumbers,'MplsLabel':MplsLabel,'MplsTunnelIndex':MplsTunnelIndex,'hwMplsLdp':hwMplsLdp,'hwMplsLdpObjects':hwMplsLdpObjects,'hwMplsLdpLsrObjects':hwMplsLdpLsrObjects,'hwMplsLdpLsrIncarnTable':hwMplsLdpLsrIncarnTable,'hwMplsLdpLsrIncarnEntry':hwMplsLdpLsrIncarnEntry,'hwMplsLdpLsrID':hwMplsLdpLsrID,'hwMplsLdpLsrLoopDetectionPresent':hwMplsLdpLsrLoopDetectionPresent,'hwMplsLdpLsrLoopDetectionAdminStatus':hwMplsLdpLsrLoopDetectionAdminStatus,'hwMplsLdpLsrPathVectorLimit':hwMplsLdpLsrPathVectorLimit,'hwMplsLdpLsrHopCountLimit':hwMplsLdpLsrHopCountLimit,'hwMplsLdpLsrLoopPreventionPresent':hwMplsLdpLsrLoopPreventionPresent,'hwMplsLdpLsrLoopPreventionAdminStatus':hwMplsLdpLsrLoopPreventionAdminStatus,'hwMplsLdpLsrLabelRetentionMode':hwMplsLdpLsrLabelRetentionMode,_E:hwMplsLdpLsrIncarnID,'hwMplsLdpLsrMaxLdpEntities':hwMplsLdpLsrMaxLdpEntities,'hwMplsLdpLsrMaxLocalPeers':hwMplsLdpLsrMaxLocalPeers,'hwMplsLdpLsrMaxRemotePeers':hwMplsLdpLsrMaxRemotePeers,'hwMplsLdpLsrMaxIfaces':hwMplsLdpLsrMaxIfaces,'hwMplsLdpLsrMaxLsps':hwMplsLdpLsrMaxLsps,'hwMplsLdpLsrMaxCrlspTnls':hwMplsLdpLsrMaxCrlspTnls,'hwMplsLdpLsrMaxErhopPerCrlspTnl':hwMplsLdpLsrMaxErhopPerCrlspTnl,'hwMplsLdpLsrRowStatus':hwMplsLdpLsrRowStatus,'hwMplsLdpLsrMaxVcmCapability':hwMplsLdpLsrMaxVcmCapability,'hwMplsLdpLsrVcmPathVecInAllLblMapPresent':hwMplsLdpLsrVcmPathVecInAllLblMapPresent,'hwMplsLdpLsrRequestRetrytimerValue':hwMplsLdpLsrRequestRetrytimerValue,'hwMplsLdpLsrNumOfRequestRetryAttempts':hwMplsLdpLsrNumOfRequestRetryAttempts,'hwMplsLdpEntityObjects':hwMplsLdpEntityObjects,'hwMplsLdpEntityTable':hwMplsLdpEntityTable,'hwMplsLdpEntityEntry':hwMplsLdpEntityEntry,_J:hwMplsLdpEntityID,'hwMplsLdpEntityLabelSpaceType':hwMplsLdpEntityLabelSpaceType,'hwMplsLdpEntityDefVpi':hwMplsLdpEntityDefVpi,'hwMplsLdpEntityDefVci':hwMplsLdpEntityDefVci,'hwMplsLdpEntityUnlabTrafVpi':hwMplsLdpEntityUnlabTrafVpi,'hwMplsLdpEntityUnlabTrafVci':hwMplsLdpEntityUnlabTrafVci,'hwMplsLdpEntityMergeCapability':hwMplsLdpEntityMergeCapability,'hwMplsLdpEntityVcDirectionality':hwMplsLdpEntityVcDirectionality,'hwMplsLdpEntityWellKnownDiscoveryPort':hwMplsLdpEntityWellKnownDiscoveryPort,'hwMplsLdpEntityMtu':hwMplsLdpEntityMtu,'hwMplsLdpEntityKeepAliveHoldTimer':hwMplsLdpEntityKeepAliveHoldTimer,_m:hwMplsLdpEntityFailedInitSessionThreshold,'hwMplsLdpEntityLabelDistributionMethod':hwMplsLdpEntityLabelDistributionMethod,'hwMplsLdpEntityLabelAllocationMethod':hwMplsLdpEntityLabelAllocationMethod,'hwMplsLdpEntityHelloHoldTimer':hwMplsLdpEntityHelloHoldTimer,'hwMplsLdpEntityRowStatus':hwMplsLdpEntityRowStatus,'hwMplsLdpEntityIfTable':hwMplsLdpEntityIfTable,'hwMplsLdpEntityIfEntry':hwMplsLdpEntityIfEntry,_I:hwMplsLdpEntityIfIndex,'hwMplsLdpEntityIfIpv4Address':hwMplsLdpEntityIfIpv4Address,'hwMplsLdpEntityIfRowStatus':hwMplsLdpEntityIfRowStatus,'hwMplsLdpEntityConfAtmLabelRangeTable':hwMplsLdpEntityConfAtmLabelRangeTable,'hwMplsLdpEntityConfAtmLabelRangeEntry':hwMplsLdpEntityConfAtmLabelRangeEntry,_e:hwMplsLdpEntityConfAtmLabelRangeLowerBoundVPI,_f:hwMplsLdpEntityConfAtmLabelRangeLowerBoundVCI,'hwMplsLdpEntityConfAtmLabelRangeUpperBoundVPI':hwMplsLdpEntityConfAtmLabelRangeUpperBoundVPI,'hwMplsLdpEntityConfAtmLabelRangeUpperBoundVCI':hwMplsLdpEntityConfAtmLabelRangeUpperBoundVCI,'hwMplsLdpEntityConfAtmLabelRangeRowStatus':hwMplsLdpEntityConfAtmLabelRangeRowStatus,'hwMplsLdpEntityStatsTable':hwMplsLdpEntityStatsTable,_l:hwMplsLdpEntityStatsEntry,'hwMplsLdpAttemptedSessions':hwMplsLdpAttemptedSessions,'hwMplsLdpPeerObjects':hwMplsLdpPeerObjects,'hwMplsLdpPeerTable':hwMplsLdpPeerTable,'hwMplsLdpPeerEntry':hwMplsLdpPeerEntry,_M:hwMplsLdpPeerIndex,'hwMplsLdpPeerID':hwMplsLdpPeerID,'hwMplsLdpPeerInternetworkAddrType':hwMplsLdpPeerInternetworkAddrType,'hwMplsLdpPeerInternetworkAddr':hwMplsLdpPeerInternetworkAddr,'hwMplsLdpPeerDefaultMtu':hwMplsLdpPeerDefaultMtu,'hwMplsLdpPeerKeepAliveHoldTimer':hwMplsLdpPeerKeepAliveHoldTimer,'hwMplsLdpPeerLabelDistributionMethod':hwMplsLdpPeerLabelDistributionMethod,'hwMplsLdpPeerType':hwMplsLdpPeerType,'hwMplsLdpPeerRowStatus':hwMplsLdpPeerRowStatus,'hwMplsLdpPeerConfAtmLabelRangeTable':hwMplsLdpPeerConfAtmLabelRangeTable,'hwMplsLdpPeerConfAtmLabelRangeEntry':hwMplsLdpPeerConfAtmLabelRangeEntry,_g:hwMplsLdpPeerConfAtmLabelRangeLowerBoundVPI,_h:hwMplsLdpPeerConfAtmLabelRangeLowerBoundVCI,'hwMplsLdpPeerConfAtmLabelRangeUpperBoundVPI':hwMplsLdpPeerConfAtmLabelRangeUpperBoundVPI,'hwMplsLdpPeerConfAtmLabelRangeUpperBoundVCI':hwMplsLdpPeerConfAtmLabelRangeUpperBoundVCI,'hwMplsLdpSessionObjects':hwMplsLdpSessionObjects,'hwMplsLdpSessionTable':hwMplsLdpSessionTable,'hwMplsLdpSessionEntry':hwMplsLdpSessionEntry,_Q:hwMplsLdpSessionIndex,_T:hwMplsLdpSessionID,'hwMplsLdpSessionProtocolVersion':hwMplsLdpSessionProtocolVersion,'hwMplsLdpSessionKeepAliveHoldTimeRemaining':hwMplsLdpSessionKeepAliveHoldTimeRemaining,'hwMplsLdpSessionRole':hwMplsLdpSessionRole,_U:hwMplsLdpSessionState,'hwMplsLdpSessionAtmLabelRangeLowerBoundVPI':hwMplsLdpSessionAtmLabelRangeLowerBoundVPI,'hwMplsLdpSessionAtmLabelRangeLowerBoundVCI':hwMplsLdpSessionAtmLabelRangeLowerBoundVCI,'hwMplsLdpSessionAtmLabelRangeUpperBoundVPI':hwMplsLdpSessionAtmLabelRangeUpperBoundVPI,'hwMplsLdpSessionAtmLabelRangeUpperBoundVCI':hwMplsLdpSessionAtmLabelRangeUpperBoundVCI,'hwMplsLdpHelloAdjacencyObjects':hwMplsLdpHelloAdjacencyObjects,'hwMplsLdpHelloAdjacencyTable':hwMplsLdpHelloAdjacencyTable,'hwMplsLdpHelloAdjacencyEntry':hwMplsLdpHelloAdjacencyEntry,_i:hwMplsLdpHelloAdjacencyIndex,'hwMplsLdpHelloAdjacencyHoldTimeRemaining':hwMplsLdpHelloAdjacencyHoldTimeRemaining,'hwMplsLdpCrlspTnlObjects':hwMplsLdpCrlspTnlObjects,'hwMplsLdpCrlspTnlTable':hwMplsLdpCrlspTnlTable,'hwMplsLdpCrlspTnlEntry':hwMplsLdpCrlspTnlEntry,_K:hwMplsLdpCrlspTnlIndex,'hwMplsLdpCrlspTnlName':hwMplsLdpCrlspTnlName,'hwMplsLdpCrlspTnlDirection':hwMplsLdpCrlspTnlDirection,'hwMplsLdpCrlspTnlSignallingProto':hwMplsLdpCrlspTnlSignallingProto,'hwMplsLdpCrlspTnlSetupPrio':hwMplsLdpCrlspTnlSetupPrio,'hwMplsLdpCrlspTnlHoldingPrio':hwMplsLdpCrlspTnlHoldingPrio,'hwMplsLdpCrlspTnlPeakDataRate':hwMplsLdpCrlspTnlPeakDataRate,'hwMplsLdpCrlspTnlPeakBurstSize':hwMplsLdpCrlspTnlPeakBurstSize,'hwMplsLdpCrlspTnlCommittedDataRate':hwMplsLdpCrlspTnlCommittedDataRate,'hwMplsLdpCrlspTnlCommittedBurstSize':hwMplsLdpCrlspTnlCommittedBurstSize,'hwMplsLdpCrlspTnlExcessBurstSize':hwMplsLdpCrlspTnlExcessBurstSize,'hwMplsLdpCrlspTnlIsPinned':hwMplsLdpCrlspTnlIsPinned,'hwMplsLdpCrlspTnlFrequency':hwMplsLdpCrlspTnlFrequency,'hwMplsLdpCrlspTnlWeight':hwMplsLdpCrlspTnlWeight,'hwMplsLdpCrlspTnlRowStatus':hwMplsLdpCrlspTnlRowStatus,'hwMplsLdpCrlspErHopTable':hwMplsLdpCrlspErHopTable,'hwMplsLdpCrlspErHopEntry':hwMplsLdpCrlspErHopEntry,_k:hwMplsLdpCrlspErHopIndex,'hwMplsLdpCrlspErHopAddrType':hwMplsLdpCrlspErHopAddrType,'hwMplsLdpCrlspErHopIpv4Addr':hwMplsLdpCrlspErHopIpv4Addr,'hwMplsLdpCrlspErHopIpv4PrefixLen':hwMplsLdpCrlspErHopIpv4PrefixLen,'hwMplsLdpCrlspErHopStrictOrLoose':hwMplsLdpCrlspErHopStrictOrLoose,'hwMplsLdpCrlspErHopRowStatus':hwMplsLdpCrlspErHopRowStatus,'hwMplsLdpNotifications':hwMplsLdpNotifications,'hwMplsLdpNotificationPrefix':hwMplsLdpNotificationPrefix,'hwMplsLdpFailedInitSessionThresholdExceeded':hwMplsLdpFailedInitSessionThresholdExceeded,'hwMplsLdpCrlspTunnelUp':hwMplsLdpCrlspTunnelUp,'hwMplsLdpCrlspTunnelDown':hwMplsLdpCrlspTunnelDown,'hwMplsLdpCrlspTunnelSetupFailure':hwMplsLdpCrlspTunnelSetupFailure,'hwMplsLdpIncarnUpEventFailure':hwMplsLdpIncarnUpEventFailure,'hwMplsLdpIncarnDownEventFailure':hwMplsLdpIncarnDownEventFailure,'hwMplsLdpEntityUpEventFailure':hwMplsLdpEntityUpEventFailure,'hwMplsLdpEntityDownEventFailure':hwMplsLdpEntityDownEventFailure,'hwMplsLdpSessionUpEventFailure':hwMplsLdpSessionUpEventFailure,'hwMplsLdpSessionDownEventFailure':hwMplsLdpSessionDownEventFailure})