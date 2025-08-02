_m='hpnicfMplsLdpEntityFailedInitSessionThreshold'
_l='hpnicfMplsLdpEntityStatsEntry'
_k='hpnicfMplsLdpCrlspErHopIndex'
_j='bits per second'
_i='hpnicfMplsLdpHelloAdjacencyIndex'
_h='hpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVCI'
_g='hpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVPI'
_f='hpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVCI'
_e='hpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVPI'
_d='downstreamUnsolicited'
_c='downstreamOnDemand'
_b='AtmVcIdentifier'
_a='AtmVpIdentifier'
_Z='accessible-for-notify'
_Y='disabled'
_X='enabled'
_W='PhysAddress'
_V='DisplayString'
_U='hpnicfMplsLdpSessionState'
_T='hpnicfMplsLdpSessionID'
_S='bytes'
_R='BitRate'
_Q='hpnicfMplsLdpSessionIndex'
_P='seconds'
_O='BurstSize'
_N='TruthValue'
_M='hpnicfMplsLdpPeerIndex'
_L='Unsigned32'
_K='hpnicfMplsLdpCrlspTnlIndex'
_J='hpnicfMplsLdpEntityID'
_I='hpnicfMplsLdpEntityIfIndex'
_H='not-accessible'
_G='read-only'
_F='read-write'
_E='hpnicfMplsLdpLsrIncarnID'
_D='Integer32'
_C='read-create'
_B='HPN-ICF-MPLS-LDP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfMpls,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfMpls')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_V,_W,'RowStatus','TextualConvention','TimeInterval',_N)
hpnicfMplsLdp=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,12,2))
if mibBuilder.loadTexts:hpnicfMplsLdp.setRevisions(('1996-11-08 21:55',))
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
_HpnicfMplsLdpObjects_ObjectIdentity=ObjectIdentity
hpnicfMplsLdpObjects=_HpnicfMplsLdpObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1))
_HpnicfMplsLdpLsrObjects_ObjectIdentity=ObjectIdentity
hpnicfMplsLdpLsrObjects=_HpnicfMplsLdpLsrObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,1))
_HpnicfMplsLdpLsrIncarnTable_Object=MibTable
hpnicfMplsLdpLsrIncarnTable=_HpnicfMplsLdpLsrIncarnTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,1,1))
if mibBuilder.loadTexts:hpnicfMplsLdpLsrIncarnTable.setStatus(_A)
_HpnicfMplsLdpLsrIncarnEntry_Object=MibTableRow
hpnicfMplsLdpLsrIncarnEntry=_HpnicfMplsLdpLsrIncarnEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,1,1,1))
hpnicfMplsLdpLsrIncarnEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:hpnicfMplsLdpLsrIncarnEntry.setStatus(_A)
_HpnicfMplsLdpLsrID_Type=MplsLsrIdentifier
_HpnicfMplsLdpLsrID_Object=MibTableColumn
hpnicfMplsLdpLsrID=_HpnicfMplsLdpLsrID_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,1,1,1,1),_HpnicfMplsLdpLsrID_Type())
hpnicfMplsLdpLsrID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMplsLdpLsrID.setStatus(_A)
class _HpnicfMplsLdpLsrLoopDetectionPresent_Type(TruthValue):defaultValue=1
_HpnicfMplsLdpLsrLoopDetectionPresent_Type.__name__=_N
_HpnicfMplsLdpLsrLoopDetectionPresent_Object=MibTableColumn
hpnicfMplsLdpLsrLoopDetectionPresent=_HpnicfMplsLdpLsrLoopDetectionPresent_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,1,1,1,2),_HpnicfMplsLdpLsrLoopDetectionPresent_Type())
hpnicfMplsLdpLsrLoopDetectionPresent.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMplsLdpLsrLoopDetectionPresent.setStatus(_A)
class _HpnicfMplsLdpLsrLoopDetectionAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_HpnicfMplsLdpLsrLoopDetectionAdminStatus_Type.__name__=_D
_HpnicfMplsLdpLsrLoopDetectionAdminStatus_Object=MibTableColumn
hpnicfMplsLdpLsrLoopDetectionAdminStatus=_HpnicfMplsLdpLsrLoopDetectionAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,1,1,1,3),_HpnicfMplsLdpLsrLoopDetectionAdminStatus_Type())
hpnicfMplsLdpLsrLoopDetectionAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMplsLdpLsrLoopDetectionAdminStatus.setStatus(_A)
class _HpnicfMplsLdpLsrPathVectorLimit_Type(Integer32):defaultValue=32
_HpnicfMplsLdpLsrPathVectorLimit_Type.__name__=_D
_HpnicfMplsLdpLsrPathVectorLimit_Object=MibTableColumn
hpnicfMplsLdpLsrPathVectorLimit=_HpnicfMplsLdpLsrPathVectorLimit_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,1,1,1,4),_HpnicfMplsLdpLsrPathVectorLimit_Type())
hpnicfMplsLdpLsrPathVectorLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMplsLdpLsrPathVectorLimit.setStatus(_A)
class _HpnicfMplsLdpLsrHopCountLimit_Type(Integer32):defaultValue=32
_HpnicfMplsLdpLsrHopCountLimit_Type.__name__=_D
_HpnicfMplsLdpLsrHopCountLimit_Object=MibTableColumn
hpnicfMplsLdpLsrHopCountLimit=_HpnicfMplsLdpLsrHopCountLimit_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,1,1,1,5),_HpnicfMplsLdpLsrHopCountLimit_Type())
hpnicfMplsLdpLsrHopCountLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMplsLdpLsrHopCountLimit.setStatus(_A)
class _HpnicfMplsLdpLsrLoopPreventionPresent_Type(TruthValue):defaultValue=2
_HpnicfMplsLdpLsrLoopPreventionPresent_Type.__name__=_N
_HpnicfMplsLdpLsrLoopPreventionPresent_Object=MibTableColumn
hpnicfMplsLdpLsrLoopPreventionPresent=_HpnicfMplsLdpLsrLoopPreventionPresent_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,1,1,1,6),_HpnicfMplsLdpLsrLoopPreventionPresent_Type())
hpnicfMplsLdpLsrLoopPreventionPresent.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMplsLdpLsrLoopPreventionPresent.setStatus(_A)
class _HpnicfMplsLdpLsrLoopPreventionAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_HpnicfMplsLdpLsrLoopPreventionAdminStatus_Type.__name__=_D
_HpnicfMplsLdpLsrLoopPreventionAdminStatus_Object=MibTableColumn
hpnicfMplsLdpLsrLoopPreventionAdminStatus=_HpnicfMplsLdpLsrLoopPreventionAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,1,1,1,7),_HpnicfMplsLdpLsrLoopPreventionAdminStatus_Type())
hpnicfMplsLdpLsrLoopPreventionAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMplsLdpLsrLoopPreventionAdminStatus.setStatus(_A)
class _HpnicfMplsLdpLsrLabelRetentionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('conservative',1),('liberal',2)))
_HpnicfMplsLdpLsrLabelRetentionMode_Type.__name__=_D
_HpnicfMplsLdpLsrLabelRetentionMode_Object=MibTableColumn
hpnicfMplsLdpLsrLabelRetentionMode=_HpnicfMplsLdpLsrLabelRetentionMode_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,1,1,1,8),_HpnicfMplsLdpLsrLabelRetentionMode_Type())
hpnicfMplsLdpLsrLabelRetentionMode.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMplsLdpLsrLabelRetentionMode.setStatus(_A)
_HpnicfMplsLdpLsrIncarnID_Type=Integer32
_HpnicfMplsLdpLsrIncarnID_Object=MibTableColumn
hpnicfMplsLdpLsrIncarnID=_HpnicfMplsLdpLsrIncarnID_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,1,1,1,9),_HpnicfMplsLdpLsrIncarnID_Type())
hpnicfMplsLdpLsrIncarnID.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMplsLdpLsrIncarnID.setStatus(_A)
class _HpnicfMplsLdpLsrMaxLdpEntities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_HpnicfMplsLdpLsrMaxLdpEntities_Type.__name__=_D
_HpnicfMplsLdpLsrMaxLdpEntities_Object=MibTableColumn
hpnicfMplsLdpLsrMaxLdpEntities=_HpnicfMplsLdpLsrMaxLdpEntities_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,1,1,1,10),_HpnicfMplsLdpLsrMaxLdpEntities_Type())
hpnicfMplsLdpLsrMaxLdpEntities.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMplsLdpLsrMaxLdpEntities.setStatus(_A)
class _HpnicfMplsLdpLsrMaxLocalPeers_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_HpnicfMplsLdpLsrMaxLocalPeers_Type.__name__=_D
_HpnicfMplsLdpLsrMaxLocalPeers_Object=MibTableColumn
hpnicfMplsLdpLsrMaxLocalPeers=_HpnicfMplsLdpLsrMaxLocalPeers_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,1,1,1,11),_HpnicfMplsLdpLsrMaxLocalPeers_Type())
hpnicfMplsLdpLsrMaxLocalPeers.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMplsLdpLsrMaxLocalPeers.setStatus(_A)
class _HpnicfMplsLdpLsrMaxRemotePeers_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_HpnicfMplsLdpLsrMaxRemotePeers_Type.__name__=_D
_HpnicfMplsLdpLsrMaxRemotePeers_Object=MibTableColumn
hpnicfMplsLdpLsrMaxRemotePeers=_HpnicfMplsLdpLsrMaxRemotePeers_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,1,1,1,12),_HpnicfMplsLdpLsrMaxRemotePeers_Type())
hpnicfMplsLdpLsrMaxRemotePeers.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMplsLdpLsrMaxRemotePeers.setStatus(_A)
_HpnicfMplsLdpLsrMaxIfaces_Type=Integer32
_HpnicfMplsLdpLsrMaxIfaces_Object=MibTableColumn
hpnicfMplsLdpLsrMaxIfaces=_HpnicfMplsLdpLsrMaxIfaces_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,1,1,1,13),_HpnicfMplsLdpLsrMaxIfaces_Type())
hpnicfMplsLdpLsrMaxIfaces.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMplsLdpLsrMaxIfaces.setStatus(_A)
_HpnicfMplsLdpLsrMaxLsps_Type=Integer32
_HpnicfMplsLdpLsrMaxLsps_Object=MibTableColumn
hpnicfMplsLdpLsrMaxLsps=_HpnicfMplsLdpLsrMaxLsps_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,1,1,1,14),_HpnicfMplsLdpLsrMaxLsps_Type())
hpnicfMplsLdpLsrMaxLsps.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMplsLdpLsrMaxLsps.setStatus(_A)
_HpnicfMplsLdpLsrMaxCrlspTnls_Type=Integer32
_HpnicfMplsLdpLsrMaxCrlspTnls_Object=MibTableColumn
hpnicfMplsLdpLsrMaxCrlspTnls=_HpnicfMplsLdpLsrMaxCrlspTnls_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,1,1,1,15),_HpnicfMplsLdpLsrMaxCrlspTnls_Type())
hpnicfMplsLdpLsrMaxCrlspTnls.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMplsLdpLsrMaxCrlspTnls.setStatus(_A)
_HpnicfMplsLdpLsrMaxErhopPerCrlspTnl_Type=Integer32
_HpnicfMplsLdpLsrMaxErhopPerCrlspTnl_Object=MibTableColumn
hpnicfMplsLdpLsrMaxErhopPerCrlspTnl=_HpnicfMplsLdpLsrMaxErhopPerCrlspTnl_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,1,1,1,16),_HpnicfMplsLdpLsrMaxErhopPerCrlspTnl_Type())
hpnicfMplsLdpLsrMaxErhopPerCrlspTnl.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMplsLdpLsrMaxErhopPerCrlspTnl.setStatus(_A)
_HpnicfMplsLdpLsrRowStatus_Type=RowStatus
_HpnicfMplsLdpLsrRowStatus_Object=MibTableColumn
hpnicfMplsLdpLsrRowStatus=_HpnicfMplsLdpLsrRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,1,1,1,17),_HpnicfMplsLdpLsrRowStatus_Type())
hpnicfMplsLdpLsrRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpLsrRowStatus.setStatus(_A)
_HpnicfMplsLdpLsrMaxVcmCapability_Type=Integer32
_HpnicfMplsLdpLsrMaxVcmCapability_Object=MibTableColumn
hpnicfMplsLdpLsrMaxVcmCapability=_HpnicfMplsLdpLsrMaxVcmCapability_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,1,1,1,18),_HpnicfMplsLdpLsrMaxVcmCapability_Type())
hpnicfMplsLdpLsrMaxVcmCapability.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMplsLdpLsrMaxVcmCapability.setStatus(_A)
_HpnicfMplsLdpLsrVcmPathVecInAllLblMapPresent_Type=TruthValue
_HpnicfMplsLdpLsrVcmPathVecInAllLblMapPresent_Object=MibTableColumn
hpnicfMplsLdpLsrVcmPathVecInAllLblMapPresent=_HpnicfMplsLdpLsrVcmPathVecInAllLblMapPresent_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,1,1,1,19),_HpnicfMplsLdpLsrVcmPathVecInAllLblMapPresent_Type())
hpnicfMplsLdpLsrVcmPathVecInAllLblMapPresent.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMplsLdpLsrVcmPathVecInAllLblMapPresent.setStatus(_A)
_HpnicfMplsLdpLsrRequestRetrytimerValue_Type=Integer32
_HpnicfMplsLdpLsrRequestRetrytimerValue_Object=MibTableColumn
hpnicfMplsLdpLsrRequestRetrytimerValue=_HpnicfMplsLdpLsrRequestRetrytimerValue_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,1,1,1,20),_HpnicfMplsLdpLsrRequestRetrytimerValue_Type())
hpnicfMplsLdpLsrRequestRetrytimerValue.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMplsLdpLsrRequestRetrytimerValue.setStatus(_A)
_HpnicfMplsLdpLsrNumOfRequestRetryAttempts_Type=Integer32
_HpnicfMplsLdpLsrNumOfRequestRetryAttempts_Object=MibTableColumn
hpnicfMplsLdpLsrNumOfRequestRetryAttempts=_HpnicfMplsLdpLsrNumOfRequestRetryAttempts_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,1,1,1,21),_HpnicfMplsLdpLsrNumOfRequestRetryAttempts_Type())
hpnicfMplsLdpLsrNumOfRequestRetryAttempts.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMplsLdpLsrNumOfRequestRetryAttempts.setStatus(_A)
_HpnicfMplsLdpEntityObjects_ObjectIdentity=ObjectIdentity
hpnicfMplsLdpEntityObjects=_HpnicfMplsLdpEntityObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2))
_HpnicfMplsLdpEntityTable_Object=MibTable
hpnicfMplsLdpEntityTable=_HpnicfMplsLdpEntityTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,1))
if mibBuilder.loadTexts:hpnicfMplsLdpEntityTable.setStatus(_A)
_HpnicfMplsLdpEntityEntry_Object=MibTableRow
hpnicfMplsLdpEntityEntry=_HpnicfMplsLdpEntityEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,1,1))
hpnicfMplsLdpEntityEntry.setIndexNames((0,_B,_E),(0,_B,_I))
if mibBuilder.loadTexts:hpnicfMplsLdpEntityEntry.setStatus(_A)
_HpnicfMplsLdpEntityID_Type=MplsLdpIdentifier
_HpnicfMplsLdpEntityID_Object=MibTableColumn
hpnicfMplsLdpEntityID=_HpnicfMplsLdpEntityID_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,1,1,1),_HpnicfMplsLdpEntityID_Type())
hpnicfMplsLdpEntityID.setMaxAccess(_Z)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityID.setStatus(_A)
class _HpnicfMplsLdpEntityLabelSpaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('perInterface',2),('perPlatform',3)))
_HpnicfMplsLdpEntityLabelSpaceType_Type.__name__=_D
_HpnicfMplsLdpEntityLabelSpaceType_Object=MibTableColumn
hpnicfMplsLdpEntityLabelSpaceType=_HpnicfMplsLdpEntityLabelSpaceType_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,1,1,2),_HpnicfMplsLdpEntityLabelSpaceType_Type())
hpnicfMplsLdpEntityLabelSpaceType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityLabelSpaceType.setStatus(_A)
_HpnicfMplsLdpEntityDefVpi_Type=AtmVpIdentifier
_HpnicfMplsLdpEntityDefVpi_Object=MibTableColumn
hpnicfMplsLdpEntityDefVpi=_HpnicfMplsLdpEntityDefVpi_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,1,1,3),_HpnicfMplsLdpEntityDefVpi_Type())
hpnicfMplsLdpEntityDefVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityDefVpi.setStatus(_A)
_HpnicfMplsLdpEntityDefVci_Type=AtmVcIdentifier
_HpnicfMplsLdpEntityDefVci_Object=MibTableColumn
hpnicfMplsLdpEntityDefVci=_HpnicfMplsLdpEntityDefVci_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,1,1,4),_HpnicfMplsLdpEntityDefVci_Type())
hpnicfMplsLdpEntityDefVci.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityDefVci.setStatus(_A)
class _HpnicfMplsLdpEntityUnlabTrafVpi_Type(AtmVpIdentifier):defaultValue=0
_HpnicfMplsLdpEntityUnlabTrafVpi_Type.__name__=_a
_HpnicfMplsLdpEntityUnlabTrafVpi_Object=MibTableColumn
hpnicfMplsLdpEntityUnlabTrafVpi=_HpnicfMplsLdpEntityUnlabTrafVpi_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,1,1,5),_HpnicfMplsLdpEntityUnlabTrafVpi_Type())
hpnicfMplsLdpEntityUnlabTrafVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityUnlabTrafVpi.setStatus(_A)
class _HpnicfMplsLdpEntityUnlabTrafVci_Type(AtmVcIdentifier):defaultValue=32
_HpnicfMplsLdpEntityUnlabTrafVci_Type.__name__=_b
_HpnicfMplsLdpEntityUnlabTrafVci_Object=MibTableColumn
hpnicfMplsLdpEntityUnlabTrafVci=_HpnicfMplsLdpEntityUnlabTrafVci_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,1,1,6),_HpnicfMplsLdpEntityUnlabTrafVci_Type())
hpnicfMplsLdpEntityUnlabTrafVci.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityUnlabTrafVci.setStatus(_A)
class _HpnicfMplsLdpEntityMergeCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noMerge',0),('vpMerge',1),('vcMerge',2),('vpVcMerge',3)))
_HpnicfMplsLdpEntityMergeCapability_Type.__name__=_D
_HpnicfMplsLdpEntityMergeCapability_Object=MibTableColumn
hpnicfMplsLdpEntityMergeCapability=_HpnicfMplsLdpEntityMergeCapability_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,1,1,7),_HpnicfMplsLdpEntityMergeCapability_Type())
hpnicfMplsLdpEntityMergeCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityMergeCapability.setStatus(_A)
class _HpnicfMplsLdpEntityVcDirectionality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bidirectional',1),('unidirectional',2)))
_HpnicfMplsLdpEntityVcDirectionality_Type.__name__=_D
_HpnicfMplsLdpEntityVcDirectionality_Object=MibTableColumn
hpnicfMplsLdpEntityVcDirectionality=_HpnicfMplsLdpEntityVcDirectionality_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,1,1,8),_HpnicfMplsLdpEntityVcDirectionality_Type())
hpnicfMplsLdpEntityVcDirectionality.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityVcDirectionality.setStatus(_A)
_HpnicfMplsLdpEntityWellKnownDiscoveryPort_Type=Integer32
_HpnicfMplsLdpEntityWellKnownDiscoveryPort_Object=MibTableColumn
hpnicfMplsLdpEntityWellKnownDiscoveryPort=_HpnicfMplsLdpEntityWellKnownDiscoveryPort_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,1,1,9),_HpnicfMplsLdpEntityWellKnownDiscoveryPort_Type())
hpnicfMplsLdpEntityWellKnownDiscoveryPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityWellKnownDiscoveryPort.setStatus(_A)
class _HpnicfMplsLdpEntityMtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfMplsLdpEntityMtu_Type.__name__=_D
_HpnicfMplsLdpEntityMtu_Object=MibTableColumn
hpnicfMplsLdpEntityMtu=_HpnicfMplsLdpEntityMtu_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,1,1,10),_HpnicfMplsLdpEntityMtu_Type())
hpnicfMplsLdpEntityMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityMtu.setStatus(_A)
class _HpnicfMplsLdpEntityKeepAliveHoldTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfMplsLdpEntityKeepAliveHoldTimer_Type.__name__=_D
_HpnicfMplsLdpEntityKeepAliveHoldTimer_Object=MibTableColumn
hpnicfMplsLdpEntityKeepAliveHoldTimer=_HpnicfMplsLdpEntityKeepAliveHoldTimer_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,1,1,11),_HpnicfMplsLdpEntityKeepAliveHoldTimer_Type())
hpnicfMplsLdpEntityKeepAliveHoldTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityKeepAliveHoldTimer.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityKeepAliveHoldTimer.setUnits(_P)
_HpnicfMplsLdpEntityFailedInitSessionThreshold_Type=Integer32
_HpnicfMplsLdpEntityFailedInitSessionThreshold_Object=MibTableColumn
hpnicfMplsLdpEntityFailedInitSessionThreshold=_HpnicfMplsLdpEntityFailedInitSessionThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,1,1,12),_HpnicfMplsLdpEntityFailedInitSessionThreshold_Type())
hpnicfMplsLdpEntityFailedInitSessionThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityFailedInitSessionThreshold.setStatus(_A)
class _HpnicfMplsLdpEntityLabelDistributionMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_HpnicfMplsLdpEntityLabelDistributionMethod_Type.__name__=_D
_HpnicfMplsLdpEntityLabelDistributionMethod_Object=MibTableColumn
hpnicfMplsLdpEntityLabelDistributionMethod=_HpnicfMplsLdpEntityLabelDistributionMethod_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,1,1,13),_HpnicfMplsLdpEntityLabelDistributionMethod_Type())
hpnicfMplsLdpEntityLabelDistributionMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityLabelDistributionMethod.setStatus(_A)
class _HpnicfMplsLdpEntityLabelAllocationMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ordered',1),('independent',2)))
_HpnicfMplsLdpEntityLabelAllocationMethod_Type.__name__=_D
_HpnicfMplsLdpEntityLabelAllocationMethod_Object=MibTableColumn
hpnicfMplsLdpEntityLabelAllocationMethod=_HpnicfMplsLdpEntityLabelAllocationMethod_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,1,1,14),_HpnicfMplsLdpEntityLabelAllocationMethod_Type())
hpnicfMplsLdpEntityLabelAllocationMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityLabelAllocationMethod.setStatus(_A)
class _HpnicfMplsLdpEntityHelloHoldTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfMplsLdpEntityHelloHoldTimer_Type.__name__=_D
_HpnicfMplsLdpEntityHelloHoldTimer_Object=MibTableColumn
hpnicfMplsLdpEntityHelloHoldTimer=_HpnicfMplsLdpEntityHelloHoldTimer_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,1,1,15),_HpnicfMplsLdpEntityHelloHoldTimer_Type())
hpnicfMplsLdpEntityHelloHoldTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityHelloHoldTimer.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityHelloHoldTimer.setUnits(_P)
_HpnicfMplsLdpEntityRowStatus_Type=RowStatus
_HpnicfMplsLdpEntityRowStatus_Object=MibTableColumn
hpnicfMplsLdpEntityRowStatus=_HpnicfMplsLdpEntityRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,1,1,16),_HpnicfMplsLdpEntityRowStatus_Type())
hpnicfMplsLdpEntityRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityRowStatus.setStatus(_A)
_HpnicfMplsLdpEntityIfTable_Object=MibTable
hpnicfMplsLdpEntityIfTable=_HpnicfMplsLdpEntityIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,2))
if mibBuilder.loadTexts:hpnicfMplsLdpEntityIfTable.setStatus(_A)
_HpnicfMplsLdpEntityIfEntry_Object=MibTableRow
hpnicfMplsLdpEntityIfEntry=_HpnicfMplsLdpEntityIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,2,1))
hpnicfMplsLdpEntityIfEntry.setIndexNames((0,_B,_E),(0,_B,_I))
if mibBuilder.loadTexts:hpnicfMplsLdpEntityIfEntry.setStatus(_A)
class _HpnicfMplsLdpEntityIfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfMplsLdpEntityIfIndex_Type.__name__=_L
_HpnicfMplsLdpEntityIfIndex_Object=MibTableColumn
hpnicfMplsLdpEntityIfIndex=_HpnicfMplsLdpEntityIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,2,1,1),_HpnicfMplsLdpEntityIfIndex_Type())
hpnicfMplsLdpEntityIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityIfIndex.setStatus(_A)
_HpnicfMplsLdpEntityIfIpv4Address_Type=IpAddress
_HpnicfMplsLdpEntityIfIpv4Address_Object=MibTableColumn
hpnicfMplsLdpEntityIfIpv4Address=_HpnicfMplsLdpEntityIfIpv4Address_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,2,1,2),_HpnicfMplsLdpEntityIfIpv4Address_Type())
hpnicfMplsLdpEntityIfIpv4Address.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityIfIpv4Address.setStatus(_A)
_HpnicfMplsLdpEntityIfRowStatus_Type=RowStatus
_HpnicfMplsLdpEntityIfRowStatus_Object=MibTableColumn
hpnicfMplsLdpEntityIfRowStatus=_HpnicfMplsLdpEntityIfRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,2,1,3),_HpnicfMplsLdpEntityIfRowStatus_Type())
hpnicfMplsLdpEntityIfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityIfRowStatus.setStatus(_A)
_HpnicfMplsLdpEntityConfAtmLabelRangeTable_Object=MibTable
hpnicfMplsLdpEntityConfAtmLabelRangeTable=_HpnicfMplsLdpEntityConfAtmLabelRangeTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,3))
if mibBuilder.loadTexts:hpnicfMplsLdpEntityConfAtmLabelRangeTable.setStatus(_A)
_HpnicfMplsLdpEntityConfAtmLabelRangeEntry_Object=MibTableRow
hpnicfMplsLdpEntityConfAtmLabelRangeEntry=_HpnicfMplsLdpEntityConfAtmLabelRangeEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,3,1))
hpnicfMplsLdpEntityConfAtmLabelRangeEntry.setIndexNames((0,_B,_E),(0,_B,_I),(0,_B,_e),(0,_B,_f))
if mibBuilder.loadTexts:hpnicfMplsLdpEntityConfAtmLabelRangeEntry.setStatus(_A)
_HpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVPI_Type=AtmVpIdentifier
_HpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVPI_Object=MibTableColumn
hpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVPI=_HpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVPI_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,3,1,1),_HpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVPI_Type())
hpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVPI.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVPI.setStatus(_A)
_HpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVCI_Type=AtmVcIdentifier
_HpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVCI_Object=MibTableColumn
hpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVCI=_HpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVCI_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,3,1,2),_HpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVCI_Type())
hpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVCI.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVCI.setStatus(_A)
_HpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVPI_Type=AtmVpIdentifier
_HpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVPI_Object=MibTableColumn
hpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVPI=_HpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVPI_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,3,1,3),_HpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVPI_Type())
hpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVPI.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVPI.setStatus(_A)
_HpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVCI_Type=AtmVcIdentifier
_HpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVCI_Object=MibTableColumn
hpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVCI=_HpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVCI_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,3,1,4),_HpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVCI_Type())
hpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVCI.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVCI.setStatus(_A)
_HpnicfMplsLdpEntityConfAtmLabelRangeRowStatus_Type=RowStatus
_HpnicfMplsLdpEntityConfAtmLabelRangeRowStatus_Object=MibTableColumn
hpnicfMplsLdpEntityConfAtmLabelRangeRowStatus=_HpnicfMplsLdpEntityConfAtmLabelRangeRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,3,1,5),_HpnicfMplsLdpEntityConfAtmLabelRangeRowStatus_Type())
hpnicfMplsLdpEntityConfAtmLabelRangeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpEntityConfAtmLabelRangeRowStatus.setStatus(_A)
_HpnicfMplsLdpEntityStatsTable_Object=MibTable
hpnicfMplsLdpEntityStatsTable=_HpnicfMplsLdpEntityStatsTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,4))
if mibBuilder.loadTexts:hpnicfMplsLdpEntityStatsTable.setStatus(_A)
_HpnicfMplsLdpEntityStatsEntry_Object=MibTableRow
hpnicfMplsLdpEntityStatsEntry=_HpnicfMplsLdpEntityStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,4,1))
if mibBuilder.loadTexts:hpnicfMplsLdpEntityStatsEntry.setStatus(_A)
_HpnicfMplsLdpAttemptedSessions_Type=Counter32
_HpnicfMplsLdpAttemptedSessions_Object=MibTableColumn
hpnicfMplsLdpAttemptedSessions=_HpnicfMplsLdpAttemptedSessions_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,2,4,1,1),_HpnicfMplsLdpAttemptedSessions_Type())
hpnicfMplsLdpAttemptedSessions.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMplsLdpAttemptedSessions.setStatus(_A)
_HpnicfMplsLdpPeerObjects_ObjectIdentity=ObjectIdentity
hpnicfMplsLdpPeerObjects=_HpnicfMplsLdpPeerObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,3))
_HpnicfMplsLdpPeerTable_Object=MibTable
hpnicfMplsLdpPeerTable=_HpnicfMplsLdpPeerTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,3,1))
if mibBuilder.loadTexts:hpnicfMplsLdpPeerTable.setStatus(_A)
_HpnicfMplsLdpPeerEntry_Object=MibTableRow
hpnicfMplsLdpPeerEntry=_HpnicfMplsLdpPeerEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,3,1,1))
hpnicfMplsLdpPeerEntry.setIndexNames((0,_B,_E),(0,_B,_I),(0,_B,_M))
if mibBuilder.loadTexts:hpnicfMplsLdpPeerEntry.setStatus(_A)
class _HpnicfMplsLdpPeerIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfMplsLdpPeerIndex_Type.__name__=_L
_HpnicfMplsLdpPeerIndex_Object=MibTableColumn
hpnicfMplsLdpPeerIndex=_HpnicfMplsLdpPeerIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,3,1,1,1),_HpnicfMplsLdpPeerIndex_Type())
hpnicfMplsLdpPeerIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfMplsLdpPeerIndex.setStatus(_A)
_HpnicfMplsLdpPeerID_Type=MplsLdpIdentifier
_HpnicfMplsLdpPeerID_Object=MibTableColumn
hpnicfMplsLdpPeerID=_HpnicfMplsLdpPeerID_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,3,1,1,2),_HpnicfMplsLdpPeerID_Type())
hpnicfMplsLdpPeerID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpPeerID.setStatus(_A)
_HpnicfMplsLdpPeerInternetworkAddrType_Type=AddressFamilyNumbers
_HpnicfMplsLdpPeerInternetworkAddrType_Object=MibTableColumn
hpnicfMplsLdpPeerInternetworkAddrType=_HpnicfMplsLdpPeerInternetworkAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,3,1,1,3),_HpnicfMplsLdpPeerInternetworkAddrType_Type())
hpnicfMplsLdpPeerInternetworkAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpPeerInternetworkAddrType.setStatus(_A)
_HpnicfMplsLdpPeerInternetworkAddr_Type=MplsLdpGenAddr
_HpnicfMplsLdpPeerInternetworkAddr_Object=MibTableColumn
hpnicfMplsLdpPeerInternetworkAddr=_HpnicfMplsLdpPeerInternetworkAddr_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,3,1,1,4),_HpnicfMplsLdpPeerInternetworkAddr_Type())
hpnicfMplsLdpPeerInternetworkAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpPeerInternetworkAddr.setStatus(_A)
class _HpnicfMplsLdpPeerDefaultMtu_Type(Integer32):defaultValue=9180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfMplsLdpPeerDefaultMtu_Type.__name__=_D
_HpnicfMplsLdpPeerDefaultMtu_Object=MibTableColumn
hpnicfMplsLdpPeerDefaultMtu=_HpnicfMplsLdpPeerDefaultMtu_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,3,1,1,5),_HpnicfMplsLdpPeerDefaultMtu_Type())
hpnicfMplsLdpPeerDefaultMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpPeerDefaultMtu.setStatus(_A)
class _HpnicfMplsLdpPeerKeepAliveHoldTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfMplsLdpPeerKeepAliveHoldTimer_Type.__name__=_D
_HpnicfMplsLdpPeerKeepAliveHoldTimer_Object=MibTableColumn
hpnicfMplsLdpPeerKeepAliveHoldTimer=_HpnicfMplsLdpPeerKeepAliveHoldTimer_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,3,1,1,6),_HpnicfMplsLdpPeerKeepAliveHoldTimer_Type())
hpnicfMplsLdpPeerKeepAliveHoldTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpPeerKeepAliveHoldTimer.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMplsLdpPeerKeepAliveHoldTimer.setUnits(_P)
class _HpnicfMplsLdpPeerLabelDistributionMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_HpnicfMplsLdpPeerLabelDistributionMethod_Type.__name__=_D
_HpnicfMplsLdpPeerLabelDistributionMethod_Object=MibTableColumn
hpnicfMplsLdpPeerLabelDistributionMethod=_HpnicfMplsLdpPeerLabelDistributionMethod_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,3,1,1,7),_HpnicfMplsLdpPeerLabelDistributionMethod_Type())
hpnicfMplsLdpPeerLabelDistributionMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpPeerLabelDistributionMethod.setStatus(_A)
class _HpnicfMplsLdpPeerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
_HpnicfMplsLdpPeerType_Type.__name__=_D
_HpnicfMplsLdpPeerType_Object=MibTableColumn
hpnicfMplsLdpPeerType=_HpnicfMplsLdpPeerType_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,3,1,1,8),_HpnicfMplsLdpPeerType_Type())
hpnicfMplsLdpPeerType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpPeerType.setStatus(_A)
_HpnicfMplsLdpPeerRowStatus_Type=RowStatus
_HpnicfMplsLdpPeerRowStatus_Object=MibTableColumn
hpnicfMplsLdpPeerRowStatus=_HpnicfMplsLdpPeerRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,3,1,1,9),_HpnicfMplsLdpPeerRowStatus_Type())
hpnicfMplsLdpPeerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpPeerRowStatus.setStatus(_A)
_HpnicfMplsLdpPeerConfAtmLabelRangeTable_Object=MibTable
hpnicfMplsLdpPeerConfAtmLabelRangeTable=_HpnicfMplsLdpPeerConfAtmLabelRangeTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,3,2))
if mibBuilder.loadTexts:hpnicfMplsLdpPeerConfAtmLabelRangeTable.setStatus(_A)
_HpnicfMplsLdpPeerConfAtmLabelRangeEntry_Object=MibTableRow
hpnicfMplsLdpPeerConfAtmLabelRangeEntry=_HpnicfMplsLdpPeerConfAtmLabelRangeEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,3,2,1))
hpnicfMplsLdpPeerConfAtmLabelRangeEntry.setIndexNames((0,_B,_E),(0,_B,_I),(0,_B,_M),(0,_B,_g),(0,_B,_h))
if mibBuilder.loadTexts:hpnicfMplsLdpPeerConfAtmLabelRangeEntry.setStatus(_A)
_HpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVPI_Type=AtmVpIdentifier
_HpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVPI_Object=MibTableColumn
hpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVPI=_HpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVPI_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,3,2,1,1),_HpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVPI_Type())
hpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVPI.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVPI.setStatus(_A)
_HpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVCI_Type=AtmVcIdentifier
_HpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVCI_Object=MibTableColumn
hpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVCI=_HpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVCI_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,3,2,1,2),_HpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVCI_Type())
hpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVCI.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVCI.setStatus(_A)
_HpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVPI_Type=AtmVpIdentifier
_HpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVPI_Object=MibTableColumn
hpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVPI=_HpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVPI_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,3,2,1,3),_HpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVPI_Type())
hpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVPI.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVPI.setStatus(_A)
_HpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVCI_Type=AtmVcIdentifier
_HpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVCI_Object=MibTableColumn
hpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVCI=_HpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVCI_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,3,2,1,4),_HpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVCI_Type())
hpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVCI.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVCI.setStatus(_A)
_HpnicfMplsLdpSessionObjects_ObjectIdentity=ObjectIdentity
hpnicfMplsLdpSessionObjects=_HpnicfMplsLdpSessionObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,4))
_HpnicfMplsLdpSessionTable_Object=MibTable
hpnicfMplsLdpSessionTable=_HpnicfMplsLdpSessionTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,4,1))
if mibBuilder.loadTexts:hpnicfMplsLdpSessionTable.setStatus(_A)
_HpnicfMplsLdpSessionEntry_Object=MibTableRow
hpnicfMplsLdpSessionEntry=_HpnicfMplsLdpSessionEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,4,1,1))
hpnicfMplsLdpSessionEntry.setIndexNames((0,_B,_E),(0,_B,_I),(0,_B,_M),(0,_B,_Q))
if mibBuilder.loadTexts:hpnicfMplsLdpSessionEntry.setStatus(_A)
class _HpnicfMplsLdpSessionIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfMplsLdpSessionIndex_Type.__name__=_L
_HpnicfMplsLdpSessionIndex_Object=MibTableColumn
hpnicfMplsLdpSessionIndex=_HpnicfMplsLdpSessionIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,4,1,1,1),_HpnicfMplsLdpSessionIndex_Type())
hpnicfMplsLdpSessionIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfMplsLdpSessionIndex.setStatus(_A)
_HpnicfMplsLdpSessionID_Type=MplsLdpIdentifier
_HpnicfMplsLdpSessionID_Object=MibTableColumn
hpnicfMplsLdpSessionID=_HpnicfMplsLdpSessionID_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,4,1,1,2),_HpnicfMplsLdpSessionID_Type())
hpnicfMplsLdpSessionID.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMplsLdpSessionID.setStatus(_A)
class _HpnicfMplsLdpSessionProtocolVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfMplsLdpSessionProtocolVersion_Type.__name__=_D
_HpnicfMplsLdpSessionProtocolVersion_Object=MibTableColumn
hpnicfMplsLdpSessionProtocolVersion=_HpnicfMplsLdpSessionProtocolVersion_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,4,1,1,3),_HpnicfMplsLdpSessionProtocolVersion_Type())
hpnicfMplsLdpSessionProtocolVersion.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMplsLdpSessionProtocolVersion.setStatus(_A)
_HpnicfMplsLdpSessionKeepAliveHoldTimeRemaining_Type=TimeInterval
_HpnicfMplsLdpSessionKeepAliveHoldTimeRemaining_Object=MibTableColumn
hpnicfMplsLdpSessionKeepAliveHoldTimeRemaining=_HpnicfMplsLdpSessionKeepAliveHoldTimeRemaining_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,4,1,1,4),_HpnicfMplsLdpSessionKeepAliveHoldTimeRemaining_Type())
hpnicfMplsLdpSessionKeepAliveHoldTimeRemaining.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMplsLdpSessionKeepAliveHoldTimeRemaining.setStatus(_A)
class _HpnicfMplsLdpSessionRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('passive',2)))
_HpnicfMplsLdpSessionRole_Type.__name__=_D
_HpnicfMplsLdpSessionRole_Object=MibTableColumn
hpnicfMplsLdpSessionRole=_HpnicfMplsLdpSessionRole_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,4,1,1,5),_HpnicfMplsLdpSessionRole_Type())
hpnicfMplsLdpSessionRole.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMplsLdpSessionRole.setStatus(_A)
class _HpnicfMplsLdpSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('nonexistent',1),('initialized',2),('openrec',3),('opensent',4),('operational',5)))
_HpnicfMplsLdpSessionState_Type.__name__=_D
_HpnicfMplsLdpSessionState_Object=MibTableColumn
hpnicfMplsLdpSessionState=_HpnicfMplsLdpSessionState_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,4,1,1,6),_HpnicfMplsLdpSessionState_Type())
hpnicfMplsLdpSessionState.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMplsLdpSessionState.setStatus(_A)
_HpnicfMplsLdpSessionAtmLabelRangeLowerBoundVPI_Type=AtmVpIdentifier
_HpnicfMplsLdpSessionAtmLabelRangeLowerBoundVPI_Object=MibTableColumn
hpnicfMplsLdpSessionAtmLabelRangeLowerBoundVPI=_HpnicfMplsLdpSessionAtmLabelRangeLowerBoundVPI_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,4,1,1,7),_HpnicfMplsLdpSessionAtmLabelRangeLowerBoundVPI_Type())
hpnicfMplsLdpSessionAtmLabelRangeLowerBoundVPI.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMplsLdpSessionAtmLabelRangeLowerBoundVPI.setStatus(_A)
_HpnicfMplsLdpSessionAtmLabelRangeLowerBoundVCI_Type=AtmVcIdentifier
_HpnicfMplsLdpSessionAtmLabelRangeLowerBoundVCI_Object=MibTableColumn
hpnicfMplsLdpSessionAtmLabelRangeLowerBoundVCI=_HpnicfMplsLdpSessionAtmLabelRangeLowerBoundVCI_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,4,1,1,8),_HpnicfMplsLdpSessionAtmLabelRangeLowerBoundVCI_Type())
hpnicfMplsLdpSessionAtmLabelRangeLowerBoundVCI.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMplsLdpSessionAtmLabelRangeLowerBoundVCI.setStatus(_A)
_HpnicfMplsLdpSessionAtmLabelRangeUpperBoundVPI_Type=AtmVpIdentifier
_HpnicfMplsLdpSessionAtmLabelRangeUpperBoundVPI_Object=MibTableColumn
hpnicfMplsLdpSessionAtmLabelRangeUpperBoundVPI=_HpnicfMplsLdpSessionAtmLabelRangeUpperBoundVPI_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,4,1,1,9),_HpnicfMplsLdpSessionAtmLabelRangeUpperBoundVPI_Type())
hpnicfMplsLdpSessionAtmLabelRangeUpperBoundVPI.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMplsLdpSessionAtmLabelRangeUpperBoundVPI.setStatus(_A)
_HpnicfMplsLdpSessionAtmLabelRangeUpperBoundVCI_Type=AtmVcIdentifier
_HpnicfMplsLdpSessionAtmLabelRangeUpperBoundVCI_Object=MibTableColumn
hpnicfMplsLdpSessionAtmLabelRangeUpperBoundVCI=_HpnicfMplsLdpSessionAtmLabelRangeUpperBoundVCI_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,4,1,1,10),_HpnicfMplsLdpSessionAtmLabelRangeUpperBoundVCI_Type())
hpnicfMplsLdpSessionAtmLabelRangeUpperBoundVCI.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMplsLdpSessionAtmLabelRangeUpperBoundVCI.setStatus(_A)
_HpnicfMplsLdpHelloAdjacencyObjects_ObjectIdentity=ObjectIdentity
hpnicfMplsLdpHelloAdjacencyObjects=_HpnicfMplsLdpHelloAdjacencyObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,5))
_HpnicfMplsLdpHelloAdjacencyTable_Object=MibTable
hpnicfMplsLdpHelloAdjacencyTable=_HpnicfMplsLdpHelloAdjacencyTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,5,1))
if mibBuilder.loadTexts:hpnicfMplsLdpHelloAdjacencyTable.setStatus(_A)
_HpnicfMplsLdpHelloAdjacencyEntry_Object=MibTableRow
hpnicfMplsLdpHelloAdjacencyEntry=_HpnicfMplsLdpHelloAdjacencyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,5,1,1))
hpnicfMplsLdpHelloAdjacencyEntry.setIndexNames((0,_B,_E),(0,_B,_I),(0,_B,_M),(0,_B,_Q),(0,_B,_i))
if mibBuilder.loadTexts:hpnicfMplsLdpHelloAdjacencyEntry.setStatus(_A)
class _HpnicfMplsLdpHelloAdjacencyIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfMplsLdpHelloAdjacencyIndex_Type.__name__=_L
_HpnicfMplsLdpHelloAdjacencyIndex_Object=MibTableColumn
hpnicfMplsLdpHelloAdjacencyIndex=_HpnicfMplsLdpHelloAdjacencyIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,5,1,1,1),_HpnicfMplsLdpHelloAdjacencyIndex_Type())
hpnicfMplsLdpHelloAdjacencyIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfMplsLdpHelloAdjacencyIndex.setStatus(_A)
_HpnicfMplsLdpHelloAdjacencyHoldTimeRemaining_Type=TimeInterval
_HpnicfMplsLdpHelloAdjacencyHoldTimeRemaining_Object=MibTableColumn
hpnicfMplsLdpHelloAdjacencyHoldTimeRemaining=_HpnicfMplsLdpHelloAdjacencyHoldTimeRemaining_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,5,1,1,2),_HpnicfMplsLdpHelloAdjacencyHoldTimeRemaining_Type())
hpnicfMplsLdpHelloAdjacencyHoldTimeRemaining.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMplsLdpHelloAdjacencyHoldTimeRemaining.setStatus(_A)
_HpnicfMplsLdpCrlspTnlObjects_ObjectIdentity=ObjectIdentity
hpnicfMplsLdpCrlspTnlObjects=_HpnicfMplsLdpCrlspTnlObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6))
_HpnicfMplsLdpCrlspTnlTable_Object=MibTable
hpnicfMplsLdpCrlspTnlTable=_HpnicfMplsLdpCrlspTnlTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,1))
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTnlTable.setStatus(_A)
_HpnicfMplsLdpCrlspTnlEntry_Object=MibTableRow
hpnicfMplsLdpCrlspTnlEntry=_HpnicfMplsLdpCrlspTnlEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,1,1))
hpnicfMplsLdpCrlspTnlEntry.setIndexNames((0,_B,_E),(0,_B,_K))
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTnlEntry.setStatus(_A)
_HpnicfMplsLdpCrlspTnlIndex_Type=MplsTunnelIndex
_HpnicfMplsLdpCrlspTnlIndex_Object=MibTableColumn
hpnicfMplsLdpCrlspTnlIndex=_HpnicfMplsLdpCrlspTnlIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,1,1,1),_HpnicfMplsLdpCrlspTnlIndex_Type())
hpnicfMplsLdpCrlspTnlIndex.setMaxAccess(_Z)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTnlIndex.setStatus(_A)
_HpnicfMplsLdpCrlspTnlName_Type=DisplayString
_HpnicfMplsLdpCrlspTnlName_Object=MibTableColumn
hpnicfMplsLdpCrlspTnlName=_HpnicfMplsLdpCrlspTnlName_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,1,1,2),_HpnicfMplsLdpCrlspTnlName_Type())
hpnicfMplsLdpCrlspTnlName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTnlName.setStatus(_A)
class _HpnicfMplsLdpCrlspTnlDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('in',1),('out',2),('inOut',3)))
_HpnicfMplsLdpCrlspTnlDirection_Type.__name__=_D
_HpnicfMplsLdpCrlspTnlDirection_Object=MibTableColumn
hpnicfMplsLdpCrlspTnlDirection=_HpnicfMplsLdpCrlspTnlDirection_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,1,1,3),_HpnicfMplsLdpCrlspTnlDirection_Type())
hpnicfMplsLdpCrlspTnlDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTnlDirection.setStatus(_A)
class _HpnicfMplsLdpCrlspTnlSignallingProto_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('ldp',2),('rsvp',3)))
_HpnicfMplsLdpCrlspTnlSignallingProto_Type.__name__=_D
_HpnicfMplsLdpCrlspTnlSignallingProto_Object=MibTableColumn
hpnicfMplsLdpCrlspTnlSignallingProto=_HpnicfMplsLdpCrlspTnlSignallingProto_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,1,1,4),_HpnicfMplsLdpCrlspTnlSignallingProto_Type())
hpnicfMplsLdpCrlspTnlSignallingProto.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTnlSignallingProto.setStatus(_A)
class _HpnicfMplsLdpCrlspTnlSetupPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfMplsLdpCrlspTnlSetupPrio_Type.__name__=_D
_HpnicfMplsLdpCrlspTnlSetupPrio_Object=MibTableColumn
hpnicfMplsLdpCrlspTnlSetupPrio=_HpnicfMplsLdpCrlspTnlSetupPrio_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,1,1,5),_HpnicfMplsLdpCrlspTnlSetupPrio_Type())
hpnicfMplsLdpCrlspTnlSetupPrio.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTnlSetupPrio.setStatus(_A)
class _HpnicfMplsLdpCrlspTnlHoldingPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfMplsLdpCrlspTnlHoldingPrio_Type.__name__=_D
_HpnicfMplsLdpCrlspTnlHoldingPrio_Object=MibTableColumn
hpnicfMplsLdpCrlspTnlHoldingPrio=_HpnicfMplsLdpCrlspTnlHoldingPrio_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,1,1,6),_HpnicfMplsLdpCrlspTnlHoldingPrio_Type())
hpnicfMplsLdpCrlspTnlHoldingPrio.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTnlHoldingPrio.setStatus(_A)
class _HpnicfMplsLdpCrlspTnlPeakDataRate_Type(BitRate):defaultValue=0
_HpnicfMplsLdpCrlspTnlPeakDataRate_Type.__name__=_R
_HpnicfMplsLdpCrlspTnlPeakDataRate_Object=MibTableColumn
hpnicfMplsLdpCrlspTnlPeakDataRate=_HpnicfMplsLdpCrlspTnlPeakDataRate_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,1,1,7),_HpnicfMplsLdpCrlspTnlPeakDataRate_Type())
hpnicfMplsLdpCrlspTnlPeakDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTnlPeakDataRate.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTnlPeakDataRate.setUnits(_j)
class _HpnicfMplsLdpCrlspTnlPeakBurstSize_Type(BurstSize):defaultValue=0
_HpnicfMplsLdpCrlspTnlPeakBurstSize_Type.__name__=_O
_HpnicfMplsLdpCrlspTnlPeakBurstSize_Object=MibTableColumn
hpnicfMplsLdpCrlspTnlPeakBurstSize=_HpnicfMplsLdpCrlspTnlPeakBurstSize_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,1,1,8),_HpnicfMplsLdpCrlspTnlPeakBurstSize_Type())
hpnicfMplsLdpCrlspTnlPeakBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTnlPeakBurstSize.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTnlPeakBurstSize.setUnits(_S)
class _HpnicfMplsLdpCrlspTnlCommittedDataRate_Type(BitRate):defaultValue=0
_HpnicfMplsLdpCrlspTnlCommittedDataRate_Type.__name__=_R
_HpnicfMplsLdpCrlspTnlCommittedDataRate_Object=MibTableColumn
hpnicfMplsLdpCrlspTnlCommittedDataRate=_HpnicfMplsLdpCrlspTnlCommittedDataRate_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,1,1,9),_HpnicfMplsLdpCrlspTnlCommittedDataRate_Type())
hpnicfMplsLdpCrlspTnlCommittedDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTnlCommittedDataRate.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTnlCommittedDataRate.setUnits(_j)
class _HpnicfMplsLdpCrlspTnlCommittedBurstSize_Type(BurstSize):defaultValue=0
_HpnicfMplsLdpCrlspTnlCommittedBurstSize_Type.__name__=_O
_HpnicfMplsLdpCrlspTnlCommittedBurstSize_Object=MibTableColumn
hpnicfMplsLdpCrlspTnlCommittedBurstSize=_HpnicfMplsLdpCrlspTnlCommittedBurstSize_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,1,1,10),_HpnicfMplsLdpCrlspTnlCommittedBurstSize_Type())
hpnicfMplsLdpCrlspTnlCommittedBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTnlCommittedBurstSize.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTnlCommittedBurstSize.setUnits(_S)
class _HpnicfMplsLdpCrlspTnlExcessBurstSize_Type(BurstSize):defaultValue=0
_HpnicfMplsLdpCrlspTnlExcessBurstSize_Type.__name__=_O
_HpnicfMplsLdpCrlspTnlExcessBurstSize_Object=MibTableColumn
hpnicfMplsLdpCrlspTnlExcessBurstSize=_HpnicfMplsLdpCrlspTnlExcessBurstSize_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,1,1,11),_HpnicfMplsLdpCrlspTnlExcessBurstSize_Type())
hpnicfMplsLdpCrlspTnlExcessBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTnlExcessBurstSize.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTnlExcessBurstSize.setUnits(_S)
class _HpnicfMplsLdpCrlspTnlIsPinned_Type(TruthValue):defaultValue=2
_HpnicfMplsLdpCrlspTnlIsPinned_Type.__name__=_N
_HpnicfMplsLdpCrlspTnlIsPinned_Object=MibTableColumn
hpnicfMplsLdpCrlspTnlIsPinned=_HpnicfMplsLdpCrlspTnlIsPinned_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,1,1,12),_HpnicfMplsLdpCrlspTnlIsPinned_Type())
hpnicfMplsLdpCrlspTnlIsPinned.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTnlIsPinned.setStatus(_A)
class _HpnicfMplsLdpCrlspTnlFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HpnicfMplsLdpCrlspTnlFrequency_Type.__name__=_D
_HpnicfMplsLdpCrlspTnlFrequency_Object=MibTableColumn
hpnicfMplsLdpCrlspTnlFrequency=_HpnicfMplsLdpCrlspTnlFrequency_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,1,1,13),_HpnicfMplsLdpCrlspTnlFrequency_Type())
hpnicfMplsLdpCrlspTnlFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTnlFrequency.setStatus(_A)
class _HpnicfMplsLdpCrlspTnlWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfMplsLdpCrlspTnlWeight_Type.__name__=_D
_HpnicfMplsLdpCrlspTnlWeight_Object=MibTableColumn
hpnicfMplsLdpCrlspTnlWeight=_HpnicfMplsLdpCrlspTnlWeight_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,1,1,14),_HpnicfMplsLdpCrlspTnlWeight_Type())
hpnicfMplsLdpCrlspTnlWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTnlWeight.setStatus(_A)
_HpnicfMplsLdpCrlspTnlRowStatus_Type=RowStatus
_HpnicfMplsLdpCrlspTnlRowStatus_Object=MibTableColumn
hpnicfMplsLdpCrlspTnlRowStatus=_HpnicfMplsLdpCrlspTnlRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,1,1,15),_HpnicfMplsLdpCrlspTnlRowStatus_Type())
hpnicfMplsLdpCrlspTnlRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTnlRowStatus.setStatus(_A)
_HpnicfMplsLdpCrlspErHopTable_Object=MibTable
hpnicfMplsLdpCrlspErHopTable=_HpnicfMplsLdpCrlspErHopTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,2))
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspErHopTable.setStatus(_A)
_HpnicfMplsLdpCrlspErHopEntry_Object=MibTableRow
hpnicfMplsLdpCrlspErHopEntry=_HpnicfMplsLdpCrlspErHopEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,2,1))
hpnicfMplsLdpCrlspErHopEntry.setIndexNames((0,_B,_E),(0,_B,_K),(0,_B,_k))
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspErHopEntry.setStatus(_A)
_HpnicfMplsLdpCrlspErHopIndex_Type=Integer32
_HpnicfMplsLdpCrlspErHopIndex_Object=MibTableColumn
hpnicfMplsLdpCrlspErHopIndex=_HpnicfMplsLdpCrlspErHopIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,2,1,1),_HpnicfMplsLdpCrlspErHopIndex_Type())
hpnicfMplsLdpCrlspErHopIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspErHopIndex.setStatus(_A)
class _HpnicfMplsLdpCrlspErHopAddrType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('ipV4',1))
_HpnicfMplsLdpCrlspErHopAddrType_Type.__name__=_D
_HpnicfMplsLdpCrlspErHopAddrType_Object=MibTableColumn
hpnicfMplsLdpCrlspErHopAddrType=_HpnicfMplsLdpCrlspErHopAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,2,1,2),_HpnicfMplsLdpCrlspErHopAddrType_Type())
hpnicfMplsLdpCrlspErHopAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspErHopAddrType.setStatus(_A)
_HpnicfMplsLdpCrlspErHopIpv4Addr_Type=IpAddress
_HpnicfMplsLdpCrlspErHopIpv4Addr_Object=MibTableColumn
hpnicfMplsLdpCrlspErHopIpv4Addr=_HpnicfMplsLdpCrlspErHopIpv4Addr_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,2,1,3),_HpnicfMplsLdpCrlspErHopIpv4Addr_Type())
hpnicfMplsLdpCrlspErHopIpv4Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspErHopIpv4Addr.setStatus(_A)
class _HpnicfMplsLdpCrlspErHopIpv4PrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_HpnicfMplsLdpCrlspErHopIpv4PrefixLen_Type.__name__=_D
_HpnicfMplsLdpCrlspErHopIpv4PrefixLen_Object=MibTableColumn
hpnicfMplsLdpCrlspErHopIpv4PrefixLen=_HpnicfMplsLdpCrlspErHopIpv4PrefixLen_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,2,1,4),_HpnicfMplsLdpCrlspErHopIpv4PrefixLen_Type())
hpnicfMplsLdpCrlspErHopIpv4PrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspErHopIpv4PrefixLen.setStatus(_A)
class _HpnicfMplsLdpCrlspErHopStrictOrLoose_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('strict',1),('loose',2)))
_HpnicfMplsLdpCrlspErHopStrictOrLoose_Type.__name__=_D
_HpnicfMplsLdpCrlspErHopStrictOrLoose_Object=MibTableColumn
hpnicfMplsLdpCrlspErHopStrictOrLoose=_HpnicfMplsLdpCrlspErHopStrictOrLoose_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,2,1,5),_HpnicfMplsLdpCrlspErHopStrictOrLoose_Type())
hpnicfMplsLdpCrlspErHopStrictOrLoose.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspErHopStrictOrLoose.setStatus(_A)
_HpnicfMplsLdpCrlspErHopRowStatus_Type=RowStatus
_HpnicfMplsLdpCrlspErHopRowStatus_Object=MibTableColumn
hpnicfMplsLdpCrlspErHopRowStatus=_HpnicfMplsLdpCrlspErHopRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,2,1,6,2,1,6),_HpnicfMplsLdpCrlspErHopRowStatus_Type())
hpnicfMplsLdpCrlspErHopRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspErHopRowStatus.setStatus(_A)
_HpnicfMplsLdpNotifications_ObjectIdentity=ObjectIdentity
hpnicfMplsLdpNotifications=_HpnicfMplsLdpNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,12,2,2))
_HpnicfMplsLdpNotificationPrefix_ObjectIdentity=ObjectIdentity
hpnicfMplsLdpNotificationPrefix=_HpnicfMplsLdpNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,12,2,2,0))
hpnicfMplsLdpEntityEntry.registerAugmentions((_B,_l))
hpnicfMplsLdpEntityStatsEntry.setIndexNames(*hpnicfMplsLdpEntityEntry.getIndexNames())
hpnicfMplsLdpFailedInitSessionThresholdExceeded=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,12,2,2,0,1))
hpnicfMplsLdpFailedInitSessionThresholdExceeded.setObjects(*((_B,_E),(_B,_J),(_B,_m)))
if mibBuilder.loadTexts:hpnicfMplsLdpFailedInitSessionThresholdExceeded.setStatus(_A)
hpnicfMplsLdpCrlspTunnelUp=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,12,2,2,0,2))
hpnicfMplsLdpCrlspTunnelUp.setObjects(*((_B,_E),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTunnelUp.setStatus(_A)
hpnicfMplsLdpCrlspTunnelDown=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,12,2,2,0,3))
hpnicfMplsLdpCrlspTunnelDown.setObjects(*((_B,_E),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTunnelDown.setStatus(_A)
hpnicfMplsLdpCrlspTunnelSetupFailure=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,12,2,2,0,4))
hpnicfMplsLdpCrlspTunnelSetupFailure.setObjects(*((_B,_E),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:hpnicfMplsLdpCrlspTunnelSetupFailure.setStatus(_A)
hpnicfMplsLdpIncarnUpEventFailure=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,12,2,2,0,11))
hpnicfMplsLdpIncarnUpEventFailure.setObjects((_B,_E))
if mibBuilder.loadTexts:hpnicfMplsLdpIncarnUpEventFailure.setStatus(_A)
hpnicfMplsLdpIncarnDownEventFailure=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,12,2,2,0,12))
hpnicfMplsLdpIncarnDownEventFailure.setObjects((_B,_E))
if mibBuilder.loadTexts:hpnicfMplsLdpIncarnDownEventFailure.setStatus(_A)
hpnicfMplsLdpEntityUpEventFailure=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,12,2,2,0,13))
hpnicfMplsLdpEntityUpEventFailure.setObjects(*((_B,_E),(_B,_J)))
if mibBuilder.loadTexts:hpnicfMplsLdpEntityUpEventFailure.setStatus(_A)
hpnicfMplsLdpEntityDownEventFailure=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,12,2,2,0,14))
hpnicfMplsLdpEntityDownEventFailure.setObjects(*((_B,_E),(_B,_J)))
if mibBuilder.loadTexts:hpnicfMplsLdpEntityDownEventFailure.setStatus(_A)
hpnicfMplsLdpSessionUpEventFailure=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,12,2,2,0,15))
hpnicfMplsLdpSessionUpEventFailure.setObjects(*((_B,_T),(_B,_U)))
if mibBuilder.loadTexts:hpnicfMplsLdpSessionUpEventFailure.setStatus(_A)
hpnicfMplsLdpSessionDownEventFailure=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,12,2,2,0,16))
hpnicfMplsLdpSessionDownEventFailure.setObjects(*((_B,_T),(_B,_U)))
if mibBuilder.loadTexts:hpnicfMplsLdpSessionDownEventFailure.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_V:DisplayString,_W:PhysAddress,_R:BitRate,_O:BurstSize,'MplsLsrIdentifier':MplsLsrIdentifier,'MplsLdpGenAddr':MplsLdpGenAddr,'MplsLdpIdentifier':MplsLdpIdentifier,_a:AtmVpIdentifier,_b:AtmVcIdentifier,'AddressFamilyNumbers':AddressFamilyNumbers,'MplsLabel':MplsLabel,'MplsTunnelIndex':MplsTunnelIndex,'hpnicfMplsLdp':hpnicfMplsLdp,'hpnicfMplsLdpObjects':hpnicfMplsLdpObjects,'hpnicfMplsLdpLsrObjects':hpnicfMplsLdpLsrObjects,'hpnicfMplsLdpLsrIncarnTable':hpnicfMplsLdpLsrIncarnTable,'hpnicfMplsLdpLsrIncarnEntry':hpnicfMplsLdpLsrIncarnEntry,'hpnicfMplsLdpLsrID':hpnicfMplsLdpLsrID,'hpnicfMplsLdpLsrLoopDetectionPresent':hpnicfMplsLdpLsrLoopDetectionPresent,'hpnicfMplsLdpLsrLoopDetectionAdminStatus':hpnicfMplsLdpLsrLoopDetectionAdminStatus,'hpnicfMplsLdpLsrPathVectorLimit':hpnicfMplsLdpLsrPathVectorLimit,'hpnicfMplsLdpLsrHopCountLimit':hpnicfMplsLdpLsrHopCountLimit,'hpnicfMplsLdpLsrLoopPreventionPresent':hpnicfMplsLdpLsrLoopPreventionPresent,'hpnicfMplsLdpLsrLoopPreventionAdminStatus':hpnicfMplsLdpLsrLoopPreventionAdminStatus,'hpnicfMplsLdpLsrLabelRetentionMode':hpnicfMplsLdpLsrLabelRetentionMode,_E:hpnicfMplsLdpLsrIncarnID,'hpnicfMplsLdpLsrMaxLdpEntities':hpnicfMplsLdpLsrMaxLdpEntities,'hpnicfMplsLdpLsrMaxLocalPeers':hpnicfMplsLdpLsrMaxLocalPeers,'hpnicfMplsLdpLsrMaxRemotePeers':hpnicfMplsLdpLsrMaxRemotePeers,'hpnicfMplsLdpLsrMaxIfaces':hpnicfMplsLdpLsrMaxIfaces,'hpnicfMplsLdpLsrMaxLsps':hpnicfMplsLdpLsrMaxLsps,'hpnicfMplsLdpLsrMaxCrlspTnls':hpnicfMplsLdpLsrMaxCrlspTnls,'hpnicfMplsLdpLsrMaxErhopPerCrlspTnl':hpnicfMplsLdpLsrMaxErhopPerCrlspTnl,'hpnicfMplsLdpLsrRowStatus':hpnicfMplsLdpLsrRowStatus,'hpnicfMplsLdpLsrMaxVcmCapability':hpnicfMplsLdpLsrMaxVcmCapability,'hpnicfMplsLdpLsrVcmPathVecInAllLblMapPresent':hpnicfMplsLdpLsrVcmPathVecInAllLblMapPresent,'hpnicfMplsLdpLsrRequestRetrytimerValue':hpnicfMplsLdpLsrRequestRetrytimerValue,'hpnicfMplsLdpLsrNumOfRequestRetryAttempts':hpnicfMplsLdpLsrNumOfRequestRetryAttempts,'hpnicfMplsLdpEntityObjects':hpnicfMplsLdpEntityObjects,'hpnicfMplsLdpEntityTable':hpnicfMplsLdpEntityTable,'hpnicfMplsLdpEntityEntry':hpnicfMplsLdpEntityEntry,_J:hpnicfMplsLdpEntityID,'hpnicfMplsLdpEntityLabelSpaceType':hpnicfMplsLdpEntityLabelSpaceType,'hpnicfMplsLdpEntityDefVpi':hpnicfMplsLdpEntityDefVpi,'hpnicfMplsLdpEntityDefVci':hpnicfMplsLdpEntityDefVci,'hpnicfMplsLdpEntityUnlabTrafVpi':hpnicfMplsLdpEntityUnlabTrafVpi,'hpnicfMplsLdpEntityUnlabTrafVci':hpnicfMplsLdpEntityUnlabTrafVci,'hpnicfMplsLdpEntityMergeCapability':hpnicfMplsLdpEntityMergeCapability,'hpnicfMplsLdpEntityVcDirectionality':hpnicfMplsLdpEntityVcDirectionality,'hpnicfMplsLdpEntityWellKnownDiscoveryPort':hpnicfMplsLdpEntityWellKnownDiscoveryPort,'hpnicfMplsLdpEntityMtu':hpnicfMplsLdpEntityMtu,'hpnicfMplsLdpEntityKeepAliveHoldTimer':hpnicfMplsLdpEntityKeepAliveHoldTimer,_m:hpnicfMplsLdpEntityFailedInitSessionThreshold,'hpnicfMplsLdpEntityLabelDistributionMethod':hpnicfMplsLdpEntityLabelDistributionMethod,'hpnicfMplsLdpEntityLabelAllocationMethod':hpnicfMplsLdpEntityLabelAllocationMethod,'hpnicfMplsLdpEntityHelloHoldTimer':hpnicfMplsLdpEntityHelloHoldTimer,'hpnicfMplsLdpEntityRowStatus':hpnicfMplsLdpEntityRowStatus,'hpnicfMplsLdpEntityIfTable':hpnicfMplsLdpEntityIfTable,'hpnicfMplsLdpEntityIfEntry':hpnicfMplsLdpEntityIfEntry,_I:hpnicfMplsLdpEntityIfIndex,'hpnicfMplsLdpEntityIfIpv4Address':hpnicfMplsLdpEntityIfIpv4Address,'hpnicfMplsLdpEntityIfRowStatus':hpnicfMplsLdpEntityIfRowStatus,'hpnicfMplsLdpEntityConfAtmLabelRangeTable':hpnicfMplsLdpEntityConfAtmLabelRangeTable,'hpnicfMplsLdpEntityConfAtmLabelRangeEntry':hpnicfMplsLdpEntityConfAtmLabelRangeEntry,_e:hpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVPI,_f:hpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVCI,'hpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVPI':hpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVPI,'hpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVCI':hpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVCI,'hpnicfMplsLdpEntityConfAtmLabelRangeRowStatus':hpnicfMplsLdpEntityConfAtmLabelRangeRowStatus,'hpnicfMplsLdpEntityStatsTable':hpnicfMplsLdpEntityStatsTable,_l:hpnicfMplsLdpEntityStatsEntry,'hpnicfMplsLdpAttemptedSessions':hpnicfMplsLdpAttemptedSessions,'hpnicfMplsLdpPeerObjects':hpnicfMplsLdpPeerObjects,'hpnicfMplsLdpPeerTable':hpnicfMplsLdpPeerTable,'hpnicfMplsLdpPeerEntry':hpnicfMplsLdpPeerEntry,_M:hpnicfMplsLdpPeerIndex,'hpnicfMplsLdpPeerID':hpnicfMplsLdpPeerID,'hpnicfMplsLdpPeerInternetworkAddrType':hpnicfMplsLdpPeerInternetworkAddrType,'hpnicfMplsLdpPeerInternetworkAddr':hpnicfMplsLdpPeerInternetworkAddr,'hpnicfMplsLdpPeerDefaultMtu':hpnicfMplsLdpPeerDefaultMtu,'hpnicfMplsLdpPeerKeepAliveHoldTimer':hpnicfMplsLdpPeerKeepAliveHoldTimer,'hpnicfMplsLdpPeerLabelDistributionMethod':hpnicfMplsLdpPeerLabelDistributionMethod,'hpnicfMplsLdpPeerType':hpnicfMplsLdpPeerType,'hpnicfMplsLdpPeerRowStatus':hpnicfMplsLdpPeerRowStatus,'hpnicfMplsLdpPeerConfAtmLabelRangeTable':hpnicfMplsLdpPeerConfAtmLabelRangeTable,'hpnicfMplsLdpPeerConfAtmLabelRangeEntry':hpnicfMplsLdpPeerConfAtmLabelRangeEntry,_g:hpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVPI,_h:hpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVCI,'hpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVPI':hpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVPI,'hpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVCI':hpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVCI,'hpnicfMplsLdpSessionObjects':hpnicfMplsLdpSessionObjects,'hpnicfMplsLdpSessionTable':hpnicfMplsLdpSessionTable,'hpnicfMplsLdpSessionEntry':hpnicfMplsLdpSessionEntry,_Q:hpnicfMplsLdpSessionIndex,_T:hpnicfMplsLdpSessionID,'hpnicfMplsLdpSessionProtocolVersion':hpnicfMplsLdpSessionProtocolVersion,'hpnicfMplsLdpSessionKeepAliveHoldTimeRemaining':hpnicfMplsLdpSessionKeepAliveHoldTimeRemaining,'hpnicfMplsLdpSessionRole':hpnicfMplsLdpSessionRole,_U:hpnicfMplsLdpSessionState,'hpnicfMplsLdpSessionAtmLabelRangeLowerBoundVPI':hpnicfMplsLdpSessionAtmLabelRangeLowerBoundVPI,'hpnicfMplsLdpSessionAtmLabelRangeLowerBoundVCI':hpnicfMplsLdpSessionAtmLabelRangeLowerBoundVCI,'hpnicfMplsLdpSessionAtmLabelRangeUpperBoundVPI':hpnicfMplsLdpSessionAtmLabelRangeUpperBoundVPI,'hpnicfMplsLdpSessionAtmLabelRangeUpperBoundVCI':hpnicfMplsLdpSessionAtmLabelRangeUpperBoundVCI,'hpnicfMplsLdpHelloAdjacencyObjects':hpnicfMplsLdpHelloAdjacencyObjects,'hpnicfMplsLdpHelloAdjacencyTable':hpnicfMplsLdpHelloAdjacencyTable,'hpnicfMplsLdpHelloAdjacencyEntry':hpnicfMplsLdpHelloAdjacencyEntry,_i:hpnicfMplsLdpHelloAdjacencyIndex,'hpnicfMplsLdpHelloAdjacencyHoldTimeRemaining':hpnicfMplsLdpHelloAdjacencyHoldTimeRemaining,'hpnicfMplsLdpCrlspTnlObjects':hpnicfMplsLdpCrlspTnlObjects,'hpnicfMplsLdpCrlspTnlTable':hpnicfMplsLdpCrlspTnlTable,'hpnicfMplsLdpCrlspTnlEntry':hpnicfMplsLdpCrlspTnlEntry,_K:hpnicfMplsLdpCrlspTnlIndex,'hpnicfMplsLdpCrlspTnlName':hpnicfMplsLdpCrlspTnlName,'hpnicfMplsLdpCrlspTnlDirection':hpnicfMplsLdpCrlspTnlDirection,'hpnicfMplsLdpCrlspTnlSignallingProto':hpnicfMplsLdpCrlspTnlSignallingProto,'hpnicfMplsLdpCrlspTnlSetupPrio':hpnicfMplsLdpCrlspTnlSetupPrio,'hpnicfMplsLdpCrlspTnlHoldingPrio':hpnicfMplsLdpCrlspTnlHoldingPrio,'hpnicfMplsLdpCrlspTnlPeakDataRate':hpnicfMplsLdpCrlspTnlPeakDataRate,'hpnicfMplsLdpCrlspTnlPeakBurstSize':hpnicfMplsLdpCrlspTnlPeakBurstSize,'hpnicfMplsLdpCrlspTnlCommittedDataRate':hpnicfMplsLdpCrlspTnlCommittedDataRate,'hpnicfMplsLdpCrlspTnlCommittedBurstSize':hpnicfMplsLdpCrlspTnlCommittedBurstSize,'hpnicfMplsLdpCrlspTnlExcessBurstSize':hpnicfMplsLdpCrlspTnlExcessBurstSize,'hpnicfMplsLdpCrlspTnlIsPinned':hpnicfMplsLdpCrlspTnlIsPinned,'hpnicfMplsLdpCrlspTnlFrequency':hpnicfMplsLdpCrlspTnlFrequency,'hpnicfMplsLdpCrlspTnlWeight':hpnicfMplsLdpCrlspTnlWeight,'hpnicfMplsLdpCrlspTnlRowStatus':hpnicfMplsLdpCrlspTnlRowStatus,'hpnicfMplsLdpCrlspErHopTable':hpnicfMplsLdpCrlspErHopTable,'hpnicfMplsLdpCrlspErHopEntry':hpnicfMplsLdpCrlspErHopEntry,_k:hpnicfMplsLdpCrlspErHopIndex,'hpnicfMplsLdpCrlspErHopAddrType':hpnicfMplsLdpCrlspErHopAddrType,'hpnicfMplsLdpCrlspErHopIpv4Addr':hpnicfMplsLdpCrlspErHopIpv4Addr,'hpnicfMplsLdpCrlspErHopIpv4PrefixLen':hpnicfMplsLdpCrlspErHopIpv4PrefixLen,'hpnicfMplsLdpCrlspErHopStrictOrLoose':hpnicfMplsLdpCrlspErHopStrictOrLoose,'hpnicfMplsLdpCrlspErHopRowStatus':hpnicfMplsLdpCrlspErHopRowStatus,'hpnicfMplsLdpNotifications':hpnicfMplsLdpNotifications,'hpnicfMplsLdpNotificationPrefix':hpnicfMplsLdpNotificationPrefix,'hpnicfMplsLdpFailedInitSessionThresholdExceeded':hpnicfMplsLdpFailedInitSessionThresholdExceeded,'hpnicfMplsLdpCrlspTunnelUp':hpnicfMplsLdpCrlspTunnelUp,'hpnicfMplsLdpCrlspTunnelDown':hpnicfMplsLdpCrlspTunnelDown,'hpnicfMplsLdpCrlspTunnelSetupFailure':hpnicfMplsLdpCrlspTunnelSetupFailure,'hpnicfMplsLdpIncarnUpEventFailure':hpnicfMplsLdpIncarnUpEventFailure,'hpnicfMplsLdpIncarnDownEventFailure':hpnicfMplsLdpIncarnDownEventFailure,'hpnicfMplsLdpEntityUpEventFailure':hpnicfMplsLdpEntityUpEventFailure,'hpnicfMplsLdpEntityDownEventFailure':hpnicfMplsLdpEntityDownEventFailure,'hpnicfMplsLdpSessionUpEventFailure':hpnicfMplsLdpSessionUpEventFailure,'hpnicfMplsLdpSessionDownEventFailure':hpnicfMplsLdpSessionDownEventFailure})