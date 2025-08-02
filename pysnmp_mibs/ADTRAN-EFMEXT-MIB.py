_AJ='adGenEfmExtGroupSecondaryUpstreamBandwidthAct'
_AI='adGenEfmExtGroupSecondaryUpstreamBandwidthClr'
_AH='adGenEfmExtGroupSecondaryDownstreamBandwidthAct'
_AG='adGenEfmExtGroupSecondaryDownstreamBandwidthClr'
_AF='adGenEfmExtGroupLocalLoopbackAct'
_AE='adGenEfmExtGroupLocalLoopbackClr'
_AD='adGenEfmExtGroupRemoteLoopbackAct'
_AC='adGenEfmExtGroupRemoteLoopbackClr'
_AB='adGenEfmExtLinkRemovedFarEndLbkDetectedAct'
_AA='adGenEfmExtLinkRemovedFarEndLbkDetectedClr'
_A9='adGenEfmExtLinkRemovedXCVThreshExceededAct'
_A8='adGenEfmExtLinkRemovedXCVThreshExceededClr'
_A7='adGenEfmExtLinkXCVThreshExceededAct'
_A6='adGenEfmExtLinkXCVThreshExceededClr'
_A5='adGenEfmExtLink24HrRxCodingErrorsAct'
_A4='adGenEfmExtLink24HrRxFcsErrorsAct'
_A3='adGenEfmExtLink24HrRxDiscardedFragmentsAct'
_A2='adGenEfmExtLink24HrRxLargeFragmentsAct'
_A1='adGenEfmExtLink24HrRxSmallFragmentsAct'
_A0='adGenEfmExtLink24HrRxErroredFragmentsAct'
_z='adGenEfmExtLink15MinRxCodingErrorsAct'
_y='adGenEfmExtLink15MinRxFcsErrorsAct'
_x='adGenEfmExtLink15MinRxDiscardedFragmentsAct'
_w='adGenEfmExtLink15MinRxLargeFragmentsAct'
_v='adGenEfmExtLink15MinRxSmallFragmentsAct'
_u='adGenEfmExtLink15MinRxErroredFragmentsAct'
_t='adGenEfmExtGroup24HrRxLostEndsAct'
_s='adGenEfmExtGroup24HrRxLostStartsAct'
_r='adGenEfmExtGroup24HrRxLostFragmentsAct'
_q='adGenEfmExtGroup24HrRxBadFragmentsAct'
_p='adGenEfmExtGroup15MinRxLostEndsAct'
_o='adGenEfmExtGroup15MinRxLostStartsAct'
_n='adGenEfmExtGroup15MinRxLostFragmentsAct'
_m='adGenEfmExtGroup15MinRxBadFragmentsAct'
_l='adGenEfmExtGroupUpstream4xRateViolationAct'
_k='adGenEfmExtGroupUpstream4xRateViolationClr'
_j='adGenEfmExtGroupDownstream4xRateViolationAct'
_i='adGenEfmExtGroupDownstream4xRateViolationClr'
_h='adGenEfmExtGroupUpstreamBandwidthAct'
_g='adGenEfmExtGroupUpstreamBandwidthClr'
_f='adGenEfmExtGroupDownstreamBandwidthAct'
_e='adGenEfmExtGroupDownstreamBandwidthClr'
_d='adGenEfmExtGroupUpPartialAct'
_c='adGenEfmExtGroupUpPartialClr'
_b='adGenEfmExtLinkDownAct'
_a='adGenEfmExtLinkDownClr'
_Z='adGenEfmExtGroupDownAct'
_Y='adGenEfmExtGroupDownClr'
_X='adGenEfmExtStatLinkSkew'
_W='adGenEfmExtStatLinkFeTcSync'
_V='adGenEfmExtStatLinkNeTcSync'
_U='adGenEfmExtStatGroupFailures'
_T='adGenEfmExtStatGroupUAS'
_S='adGenEfmExtStatGroupNumActiveLinks'
_R='adGenEfmExtStatGroupSize'
_Q='adGenEfmExtStatGroupStatus'
_P='adGenEfmExtPerfPort24HrIntNumber'
_O='adGenEfmExtPerfPort15MinIntNumber'
_N='read-write'
_M='Integer32'
_L='read-only'
_K='sysName'
_J='SNMPv2-MIB'
_I='ifDescr'
_H='adTrapInformSeqNum'
_G='ADTRAN-GENTRAPINFORM-MIB'
_F='adGenSlotInfoIndex'
_E='ADTRAN-GENSLOT-MIB'
_D='ADTRAN-EFMEXT-MIB'
_C='ifIndex'
_B='current'
_A='IF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_E,_F)
adTrapInformSeqNum,=mibBuilder.importSymbols(_G,_H)
adGenEfmExt,adGenEfmExtID=mibBuilder.importSymbols('ADTRAN-SHARED-EFM-MIB','adGenEfmExt','adGenEfmExtID')
ifDescr,ifIndex=mibBuilder.importSymbols(_A,_I,_C)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols(_J,_K)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenEfmExtMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,66,3,1))
if mibBuilder.loadTexts:adGenEfmExtMIB.setRevisions(('2011-09-28 00:00','2011-08-10 00:00','2011-04-14 00:00','2008-03-24 00:00'))
_AdGenEfmExtStatus_ObjectIdentity=ObjectIdentity
adGenEfmExtStatus=_AdGenEfmExtStatus_ObjectIdentity((1,3,6,1,4,1,664,5,66,3,1))
_AdGenEfmExtStatGroupTable_Object=MibTable
adGenEfmExtStatGroupTable=_AdGenEfmExtStatGroupTable_Object((1,3,6,1,4,1,664,5,66,3,1,1))
if mibBuilder.loadTexts:adGenEfmExtStatGroupTable.setStatus(_B)
_AdGenEfmExtStatGroupEntry_Object=MibTableRow
adGenEfmExtStatGroupEntry=_AdGenEfmExtStatGroupEntry_Object((1,3,6,1,4,1,664,5,66,3,1,1,1))
adGenEfmExtStatGroupEntry.setIndexNames((0,_A,_C))
if mibBuilder.loadTexts:adGenEfmExtStatGroupEntry.setStatus(_B)
class _AdGenEfmExtStatGroupStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3),('noLinksInGroup',4),('upPartial',5)))
_AdGenEfmExtStatGroupStatus_Type.__name__=_M
_AdGenEfmExtStatGroupStatus_Object=MibTableColumn
adGenEfmExtStatGroupStatus=_AdGenEfmExtStatGroupStatus_Object((1,3,6,1,4,1,664,5,66,3,1,1,1,1),_AdGenEfmExtStatGroupStatus_Type())
adGenEfmExtStatGroupStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtStatGroupStatus.setStatus(_B)
_AdGenEfmExtStatGroupSize_Type=Integer32
_AdGenEfmExtStatGroupSize_Object=MibTableColumn
adGenEfmExtStatGroupSize=_AdGenEfmExtStatGroupSize_Object((1,3,6,1,4,1,664,5,66,3,1,1,1,2),_AdGenEfmExtStatGroupSize_Type())
adGenEfmExtStatGroupSize.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtStatGroupSize.setStatus(_B)
_AdGenEfmExtStatGroupNumActiveLinks_Type=Integer32
_AdGenEfmExtStatGroupNumActiveLinks_Object=MibTableColumn
adGenEfmExtStatGroupNumActiveLinks=_AdGenEfmExtStatGroupNumActiveLinks_Object((1,3,6,1,4,1,664,5,66,3,1,1,1,3),_AdGenEfmExtStatGroupNumActiveLinks_Type())
adGenEfmExtStatGroupNumActiveLinks.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtStatGroupNumActiveLinks.setStatus(_B)
_AdGenEfmExtStatGroupUAS_Type=Gauge32
_AdGenEfmExtStatGroupUAS_Object=MibTableColumn
adGenEfmExtStatGroupUAS=_AdGenEfmExtStatGroupUAS_Object((1,3,6,1,4,1,664,5,66,3,1,1,1,4),_AdGenEfmExtStatGroupUAS_Type())
adGenEfmExtStatGroupUAS.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtStatGroupUAS.setStatus(_B)
_AdGenEfmExtStatGroupFailures_Type=Gauge32
_AdGenEfmExtStatGroupFailures_Object=MibTableColumn
adGenEfmExtStatGroupFailures=_AdGenEfmExtStatGroupFailures_Object((1,3,6,1,4,1,664,5,66,3,1,1,1,5),_AdGenEfmExtStatGroupFailures_Type())
adGenEfmExtStatGroupFailures.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtStatGroupFailures.setStatus(_B)
_AdGenEfmExtStatLinkTable_Object=MibTable
adGenEfmExtStatLinkTable=_AdGenEfmExtStatLinkTable_Object((1,3,6,1,4,1,664,5,66,3,1,2))
if mibBuilder.loadTexts:adGenEfmExtStatLinkTable.setStatus(_B)
_AdGenEfmExtStatLinkEntry_Object=MibTableRow
adGenEfmExtStatLinkEntry=_AdGenEfmExtStatLinkEntry_Object((1,3,6,1,4,1,664,5,66,3,1,2,1))
adGenEfmExtStatLinkEntry.setIndexNames((0,_A,_C))
if mibBuilder.loadTexts:adGenEfmExtStatLinkEntry.setStatus(_B)
class _AdGenEfmExtStatLinkNeTcSync_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_AdGenEfmExtStatLinkNeTcSync_Type.__name__=_M
_AdGenEfmExtStatLinkNeTcSync_Object=MibTableColumn
adGenEfmExtStatLinkNeTcSync=_AdGenEfmExtStatLinkNeTcSync_Object((1,3,6,1,4,1,664,5,66,3,1,2,1,1),_AdGenEfmExtStatLinkNeTcSync_Type())
adGenEfmExtStatLinkNeTcSync.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtStatLinkNeTcSync.setStatus(_B)
class _AdGenEfmExtStatLinkFeTcSync_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_AdGenEfmExtStatLinkFeTcSync_Type.__name__=_M
_AdGenEfmExtStatLinkFeTcSync_Object=MibTableColumn
adGenEfmExtStatLinkFeTcSync=_AdGenEfmExtStatLinkFeTcSync_Object((1,3,6,1,4,1,664,5,66,3,1,2,1,2),_AdGenEfmExtStatLinkFeTcSync_Type())
adGenEfmExtStatLinkFeTcSync.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtStatLinkFeTcSync.setStatus(_B)
_AdGenEfmExtStatLinkSkew_Type=Integer32
_AdGenEfmExtStatLinkSkew_Object=MibTableColumn
adGenEfmExtStatLinkSkew=_AdGenEfmExtStatLinkSkew_Object((1,3,6,1,4,1,664,5,66,3,1,2,1,3),_AdGenEfmExtStatLinkSkew_Type())
adGenEfmExtStatLinkSkew.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtStatLinkSkew.setStatus(_B)
_AdGenEfmExtStatLinkStatus_Type=DisplayString
_AdGenEfmExtStatLinkStatus_Object=MibTableColumn
adGenEfmExtStatLinkStatus=_AdGenEfmExtStatLinkStatus_Object((1,3,6,1,4,1,664,5,66,3,1,2,1,4),_AdGenEfmExtStatLinkStatus_Type())
adGenEfmExtStatLinkStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtStatLinkStatus.setStatus(_B)
_AdGenEfmExtStatLinkFeId_Type=Integer32
_AdGenEfmExtStatLinkFeId_Object=MibTableColumn
adGenEfmExtStatLinkFeId=_AdGenEfmExtStatLinkFeId_Object((1,3,6,1,4,1,664,5,66,3,1,2,1,5),_AdGenEfmExtStatLinkFeId_Type())
adGenEfmExtStatLinkFeId.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtStatLinkFeId.setStatus(_B)
_AdGenEfmExtMibConformance_ObjectIdentity=ObjectIdentity
adGenEfmExtMibConformance=_AdGenEfmExtMibConformance_ObjectIdentity((1,3,6,1,4,1,664,5,66,3,2))
_AdGenEfmExtMibGroups_ObjectIdentity=ObjectIdentity
adGenEfmExtMibGroups=_AdGenEfmExtMibGroups_ObjectIdentity((1,3,6,1,4,1,664,5,66,3,2,1))
_AdGenEfmExtPerformance_ObjectIdentity=ObjectIdentity
adGenEfmExtPerformance=_AdGenEfmExtPerformance_ObjectIdentity((1,3,6,1,4,1,664,5,66,3,3))
_AdGenEfmExtPerfPortCurr15MinTable_Object=MibTable
adGenEfmExtPerfPortCurr15MinTable=_AdGenEfmExtPerfPortCurr15MinTable_Object((1,3,6,1,4,1,664,5,66,3,3,1))
if mibBuilder.loadTexts:adGenEfmExtPerfPortCurr15MinTable.setStatus(_B)
_AdGenEfmExtPerfPortCurr15MinEntry_Object=MibTableRow
adGenEfmExtPerfPortCurr15MinEntry=_AdGenEfmExtPerfPortCurr15MinEntry_Object((1,3,6,1,4,1,664,5,66,3,3,1,1))
adGenEfmExtPerfPortCurr15MinEntry.setIndexNames((0,_A,_C))
if mibBuilder.loadTexts:adGenEfmExtPerfPortCurr15MinEntry.setStatus(_B)
_AdGenEfmExtPerfPort15MinValidIntervals_Type=Integer32
_AdGenEfmExtPerfPort15MinValidIntervals_Object=MibTableColumn
adGenEfmExtPerfPort15MinValidIntervals=_AdGenEfmExtPerfPort15MinValidIntervals_Object((1,3,6,1,4,1,664,5,66,3,3,1,1,1),_AdGenEfmExtPerfPort15MinValidIntervals_Type())
adGenEfmExtPerfPort15MinValidIntervals.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtPerfPort15MinValidIntervals.setStatus(_B)
_AdGenEfmExtPerfPortCurr15MinTxOctets_Type=Gauge32
_AdGenEfmExtPerfPortCurr15MinTxOctets_Object=MibTableColumn
adGenEfmExtPerfPortCurr15MinTxOctets=_AdGenEfmExtPerfPortCurr15MinTxOctets_Object((1,3,6,1,4,1,664,5,66,3,3,1,1,2),_AdGenEfmExtPerfPortCurr15MinTxOctets_Type())
adGenEfmExtPerfPortCurr15MinTxOctets.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtPerfPortCurr15MinTxOctets.setStatus(_B)
_AdGenEfmExtPerfPortCurr15MinTxFrames_Type=Gauge32
_AdGenEfmExtPerfPortCurr15MinTxFrames_Object=MibTableColumn
adGenEfmExtPerfPortCurr15MinTxFrames=_AdGenEfmExtPerfPortCurr15MinTxFrames_Object((1,3,6,1,4,1,664,5,66,3,3,1,1,3),_AdGenEfmExtPerfPortCurr15MinTxFrames_Type())
adGenEfmExtPerfPortCurr15MinTxFrames.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtPerfPortCurr15MinTxFrames.setStatus(_B)
_AdGenEfmExtPerfPortCurr15MinRxOctets_Type=Gauge32
_AdGenEfmExtPerfPortCurr15MinRxOctets_Object=MibTableColumn
adGenEfmExtPerfPortCurr15MinRxOctets=_AdGenEfmExtPerfPortCurr15MinRxOctets_Object((1,3,6,1,4,1,664,5,66,3,3,1,1,4),_AdGenEfmExtPerfPortCurr15MinRxOctets_Type())
adGenEfmExtPerfPortCurr15MinRxOctets.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtPerfPortCurr15MinRxOctets.setStatus(_B)
_AdGenEfmExtPerfPortCurr15MinRxFrames_Type=Gauge32
_AdGenEfmExtPerfPortCurr15MinRxFrames_Object=MibTableColumn
adGenEfmExtPerfPortCurr15MinRxFrames=_AdGenEfmExtPerfPortCurr15MinRxFrames_Object((1,3,6,1,4,1,664,5,66,3,3,1,1,5),_AdGenEfmExtPerfPortCurr15MinRxFrames_Type())
adGenEfmExtPerfPortCurr15MinRxFrames.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtPerfPortCurr15MinRxFrames.setStatus(_B)
_AdGenEfmExtPerfPortCurr15MinRxCodingErrors_Type=Gauge32
_AdGenEfmExtPerfPortCurr15MinRxCodingErrors_Object=MibTableColumn
adGenEfmExtPerfPortCurr15MinRxCodingErrors=_AdGenEfmExtPerfPortCurr15MinRxCodingErrors_Object((1,3,6,1,4,1,664,5,66,3,3,1,1,6),_AdGenEfmExtPerfPortCurr15MinRxCodingErrors_Type())
adGenEfmExtPerfPortCurr15MinRxCodingErrors.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtPerfPortCurr15MinRxCodingErrors.setStatus(_B)
_AdGenEfmExtPerfPort15MinIntTable_Object=MibTable
adGenEfmExtPerfPort15MinIntTable=_AdGenEfmExtPerfPort15MinIntTable_Object((1,3,6,1,4,1,664,5,66,3,3,2))
if mibBuilder.loadTexts:adGenEfmExtPerfPort15MinIntTable.setStatus(_B)
_AdGenEfmExtPerfPort15MinIntEntry_Object=MibTableRow
adGenEfmExtPerfPort15MinIntEntry=_AdGenEfmExtPerfPort15MinIntEntry_Object((1,3,6,1,4,1,664,5,66,3,3,2,1))
adGenEfmExtPerfPort15MinIntEntry.setIndexNames((0,_A,_C),(0,_D,_O))
if mibBuilder.loadTexts:adGenEfmExtPerfPort15MinIntEntry.setStatus(_B)
_AdGenEfmExtPerfPort15MinIntNumber_Type=Integer32
_AdGenEfmExtPerfPort15MinIntNumber_Object=MibTableColumn
adGenEfmExtPerfPort15MinIntNumber=_AdGenEfmExtPerfPort15MinIntNumber_Object((1,3,6,1,4,1,664,5,66,3,3,2,1,1),_AdGenEfmExtPerfPort15MinIntNumber_Type())
adGenEfmExtPerfPort15MinIntNumber.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtPerfPort15MinIntNumber.setStatus(_B)
_AdGenEfmExtPerfPort15MinIntTxOctets_Type=Gauge32
_AdGenEfmExtPerfPort15MinIntTxOctets_Object=MibTableColumn
adGenEfmExtPerfPort15MinIntTxOctets=_AdGenEfmExtPerfPort15MinIntTxOctets_Object((1,3,6,1,4,1,664,5,66,3,3,2,1,2),_AdGenEfmExtPerfPort15MinIntTxOctets_Type())
adGenEfmExtPerfPort15MinIntTxOctets.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtPerfPort15MinIntTxOctets.setStatus(_B)
_AdGenEfmExtPerfPort15MinIntTxFrames_Type=Gauge32
_AdGenEfmExtPerfPort15MinIntTxFrames_Object=MibTableColumn
adGenEfmExtPerfPort15MinIntTxFrames=_AdGenEfmExtPerfPort15MinIntTxFrames_Object((1,3,6,1,4,1,664,5,66,3,3,2,1,3),_AdGenEfmExtPerfPort15MinIntTxFrames_Type())
adGenEfmExtPerfPort15MinIntTxFrames.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtPerfPort15MinIntTxFrames.setStatus(_B)
_AdGenEfmExtPerfPort15MinIntRxOctets_Type=Gauge32
_AdGenEfmExtPerfPort15MinIntRxOctets_Object=MibTableColumn
adGenEfmExtPerfPort15MinIntRxOctets=_AdGenEfmExtPerfPort15MinIntRxOctets_Object((1,3,6,1,4,1,664,5,66,3,3,2,1,4),_AdGenEfmExtPerfPort15MinIntRxOctets_Type())
adGenEfmExtPerfPort15MinIntRxOctets.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtPerfPort15MinIntRxOctets.setStatus(_B)
_AdGenEfmExtPerfPort15MinIntRxFrames_Type=Gauge32
_AdGenEfmExtPerfPort15MinIntRxFrames_Object=MibTableColumn
adGenEfmExtPerfPort15MinIntRxFrames=_AdGenEfmExtPerfPort15MinIntRxFrames_Object((1,3,6,1,4,1,664,5,66,3,3,2,1,5),_AdGenEfmExtPerfPort15MinIntRxFrames_Type())
adGenEfmExtPerfPort15MinIntRxFrames.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtPerfPort15MinIntRxFrames.setStatus(_B)
_AdGenEfmExtPerfPort15MinIntRxCodingErrors_Type=Gauge32
_AdGenEfmExtPerfPort15MinIntRxCodingErrors_Object=MibTableColumn
adGenEfmExtPerfPort15MinIntRxCodingErrors=_AdGenEfmExtPerfPort15MinIntRxCodingErrors_Object((1,3,6,1,4,1,664,5,66,3,3,2,1,6),_AdGenEfmExtPerfPort15MinIntRxCodingErrors_Type())
adGenEfmExtPerfPort15MinIntRxCodingErrors.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtPerfPort15MinIntRxCodingErrors.setStatus(_B)
_AdGenEfmExtPerfPortCurr24HrTable_Object=MibTable
adGenEfmExtPerfPortCurr24HrTable=_AdGenEfmExtPerfPortCurr24HrTable_Object((1,3,6,1,4,1,664,5,66,3,3,3))
if mibBuilder.loadTexts:adGenEfmExtPerfPortCurr24HrTable.setStatus(_B)
_AdGenEfmExtPerfPortCurr24HrEntry_Object=MibTableRow
adGenEfmExtPerfPortCurr24HrEntry=_AdGenEfmExtPerfPortCurr24HrEntry_Object((1,3,6,1,4,1,664,5,66,3,3,3,1))
adGenEfmExtPerfPortCurr24HrEntry.setIndexNames((0,_A,_C))
if mibBuilder.loadTexts:adGenEfmExtPerfPortCurr24HrEntry.setStatus(_B)
_AdGenEfmExtPerfPort24HrValidIntervals_Type=Integer32
_AdGenEfmExtPerfPort24HrValidIntervals_Object=MibTableColumn
adGenEfmExtPerfPort24HrValidIntervals=_AdGenEfmExtPerfPort24HrValidIntervals_Object((1,3,6,1,4,1,664,5,66,3,3,3,1,1),_AdGenEfmExtPerfPort24HrValidIntervals_Type())
adGenEfmExtPerfPort24HrValidIntervals.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtPerfPort24HrValidIntervals.setStatus(_B)
_AdGenEfmExtPerfPortCurr24HrTxOctets_Type=Gauge32
_AdGenEfmExtPerfPortCurr24HrTxOctets_Object=MibTableColumn
adGenEfmExtPerfPortCurr24HrTxOctets=_AdGenEfmExtPerfPortCurr24HrTxOctets_Object((1,3,6,1,4,1,664,5,66,3,3,3,1,2),_AdGenEfmExtPerfPortCurr24HrTxOctets_Type())
adGenEfmExtPerfPortCurr24HrTxOctets.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtPerfPortCurr24HrTxOctets.setStatus(_B)
_AdGenEfmExtPerfPortCurr24HrTxFrames_Type=Gauge32
_AdGenEfmExtPerfPortCurr24HrTxFrames_Object=MibTableColumn
adGenEfmExtPerfPortCurr24HrTxFrames=_AdGenEfmExtPerfPortCurr24HrTxFrames_Object((1,3,6,1,4,1,664,5,66,3,3,3,1,3),_AdGenEfmExtPerfPortCurr24HrTxFrames_Type())
adGenEfmExtPerfPortCurr24HrTxFrames.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtPerfPortCurr24HrTxFrames.setStatus(_B)
_AdGenEfmExtPerfPortCurr24HrRxOctets_Type=Gauge32
_AdGenEfmExtPerfPortCurr24HrRxOctets_Object=MibTableColumn
adGenEfmExtPerfPortCurr24HrRxOctets=_AdGenEfmExtPerfPortCurr24HrRxOctets_Object((1,3,6,1,4,1,664,5,66,3,3,3,1,4),_AdGenEfmExtPerfPortCurr24HrRxOctets_Type())
adGenEfmExtPerfPortCurr24HrRxOctets.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtPerfPortCurr24HrRxOctets.setStatus(_B)
_AdGenEfmExtPerfPortCurr24HrRxFrames_Type=Gauge32
_AdGenEfmExtPerfPortCurr24HrRxFrames_Object=MibTableColumn
adGenEfmExtPerfPortCurr24HrRxFrames=_AdGenEfmExtPerfPortCurr24HrRxFrames_Object((1,3,6,1,4,1,664,5,66,3,3,3,1,5),_AdGenEfmExtPerfPortCurr24HrRxFrames_Type())
adGenEfmExtPerfPortCurr24HrRxFrames.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtPerfPortCurr24HrRxFrames.setStatus(_B)
_AdGenEfmExtPerfPortCurr24HrRxCodingErrors_Type=Gauge32
_AdGenEfmExtPerfPortCurr24HrRxCodingErrors_Object=MibTableColumn
adGenEfmExtPerfPortCurr24HrRxCodingErrors=_AdGenEfmExtPerfPortCurr24HrRxCodingErrors_Object((1,3,6,1,4,1,664,5,66,3,3,3,1,6),_AdGenEfmExtPerfPortCurr24HrRxCodingErrors_Type())
adGenEfmExtPerfPortCurr24HrRxCodingErrors.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtPerfPortCurr24HrRxCodingErrors.setStatus(_B)
_AdGenEfmExtPerfPort24HrIntTable_Object=MibTable
adGenEfmExtPerfPort24HrIntTable=_AdGenEfmExtPerfPort24HrIntTable_Object((1,3,6,1,4,1,664,5,66,3,3,4))
if mibBuilder.loadTexts:adGenEfmExtPerfPort24HrIntTable.setStatus(_B)
_AdGenEfmExtPerfPort24HrIntEntry_Object=MibTableRow
adGenEfmExtPerfPort24HrIntEntry=_AdGenEfmExtPerfPort24HrIntEntry_Object((1,3,6,1,4,1,664,5,66,3,3,4,1))
adGenEfmExtPerfPort24HrIntEntry.setIndexNames((0,_A,_C),(0,_D,_P))
if mibBuilder.loadTexts:adGenEfmExtPerfPort24HrIntEntry.setStatus(_B)
_AdGenEfmExtPerfPort24HrIntNumber_Type=Integer32
_AdGenEfmExtPerfPort24HrIntNumber_Object=MibTableColumn
adGenEfmExtPerfPort24HrIntNumber=_AdGenEfmExtPerfPort24HrIntNumber_Object((1,3,6,1,4,1,664,5,66,3,3,4,1,1),_AdGenEfmExtPerfPort24HrIntNumber_Type())
adGenEfmExtPerfPort24HrIntNumber.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtPerfPort24HrIntNumber.setStatus(_B)
_AdGenEfmExtPerfPort24HrIntTxOctets_Type=Gauge32
_AdGenEfmExtPerfPort24HrIntTxOctets_Object=MibTableColumn
adGenEfmExtPerfPort24HrIntTxOctets=_AdGenEfmExtPerfPort24HrIntTxOctets_Object((1,3,6,1,4,1,664,5,66,3,3,4,1,2),_AdGenEfmExtPerfPort24HrIntTxOctets_Type())
adGenEfmExtPerfPort24HrIntTxOctets.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtPerfPort24HrIntTxOctets.setStatus(_B)
_AdGenEfmExtPerfPort24HrIntTxFrames_Type=Gauge32
_AdGenEfmExtPerfPort24HrIntTxFrames_Object=MibTableColumn
adGenEfmExtPerfPort24HrIntTxFrames=_AdGenEfmExtPerfPort24HrIntTxFrames_Object((1,3,6,1,4,1,664,5,66,3,3,4,1,3),_AdGenEfmExtPerfPort24HrIntTxFrames_Type())
adGenEfmExtPerfPort24HrIntTxFrames.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtPerfPort24HrIntTxFrames.setStatus(_B)
_AdGenEfmExtPerfPort24HrIntRxOctets_Type=Gauge32
_AdGenEfmExtPerfPort24HrIntRxOctets_Object=MibTableColumn
adGenEfmExtPerfPort24HrIntRxOctets=_AdGenEfmExtPerfPort24HrIntRxOctets_Object((1,3,6,1,4,1,664,5,66,3,3,4,1,4),_AdGenEfmExtPerfPort24HrIntRxOctets_Type())
adGenEfmExtPerfPort24HrIntRxOctets.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtPerfPort24HrIntRxOctets.setStatus(_B)
_AdGenEfmExtPerfPort24HrIntRxFrames_Type=Gauge32
_AdGenEfmExtPerfPort24HrIntRxFrames_Object=MibTableColumn
adGenEfmExtPerfPort24HrIntRxFrames=_AdGenEfmExtPerfPort24HrIntRxFrames_Object((1,3,6,1,4,1,664,5,66,3,3,4,1,5),_AdGenEfmExtPerfPort24HrIntRxFrames_Type())
adGenEfmExtPerfPort24HrIntRxFrames.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtPerfPort24HrIntRxFrames.setStatus(_B)
_AdGenEfmExtPerfPort24HrIntRxCodingErrors_Type=Gauge32
_AdGenEfmExtPerfPort24HrIntRxCodingErrors_Object=MibTableColumn
adGenEfmExtPerfPort24HrIntRxCodingErrors=_AdGenEfmExtPerfPort24HrIntRxCodingErrors_Object((1,3,6,1,4,1,664,5,66,3,3,4,1,6),_AdGenEfmExtPerfPort24HrIntRxCodingErrors_Type())
adGenEfmExtPerfPort24HrIntRxCodingErrors.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenEfmExtPerfPort24HrIntRxCodingErrors.setStatus(_B)
_AdGenEfmExtPerfPort15MinThreshTable_Object=MibTable
adGenEfmExtPerfPort15MinThreshTable=_AdGenEfmExtPerfPort15MinThreshTable_Object((1,3,6,1,4,1,664,5,66,3,3,5))
if mibBuilder.loadTexts:adGenEfmExtPerfPort15MinThreshTable.setStatus(_B)
_AdGenEfmExtPerfPort15MinThreshEntry_Object=MibTableRow
adGenEfmExtPerfPort15MinThreshEntry=_AdGenEfmExtPerfPort15MinThreshEntry_Object((1,3,6,1,4,1,664,5,66,3,3,5,1))
adGenEfmExtPerfPort15MinThreshEntry.setIndexNames((0,_A,_C))
if mibBuilder.loadTexts:adGenEfmExtPerfPort15MinThreshEntry.setStatus(_B)
_AdGenEfmExtPerfPort15MinThreshRxCodingErrors_Type=Unsigned32
_AdGenEfmExtPerfPort15MinThreshRxCodingErrors_Object=MibTableColumn
adGenEfmExtPerfPort15MinThreshRxCodingErrors=_AdGenEfmExtPerfPort15MinThreshRxCodingErrors_Object((1,3,6,1,4,1,664,5,66,3,3,5,1,6),_AdGenEfmExtPerfPort15MinThreshRxCodingErrors_Type())
adGenEfmExtPerfPort15MinThreshRxCodingErrors.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenEfmExtPerfPort15MinThreshRxCodingErrors.setStatus(_B)
_AdGenEfmExtPerfPort24HrThreshTable_Object=MibTable
adGenEfmExtPerfPort24HrThreshTable=_AdGenEfmExtPerfPort24HrThreshTable_Object((1,3,6,1,4,1,664,5,66,3,3,6))
if mibBuilder.loadTexts:adGenEfmExtPerfPort24HrThreshTable.setStatus(_B)
_AdGenEfmExtPerfPort24HrThreshEntry_Object=MibTableRow
adGenEfmExtPerfPort24HrThreshEntry=_AdGenEfmExtPerfPort24HrThreshEntry_Object((1,3,6,1,4,1,664,5,66,3,3,6,1))
adGenEfmExtPerfPort24HrThreshEntry.setIndexNames((0,_A,_C))
if mibBuilder.loadTexts:adGenEfmExtPerfPort24HrThreshEntry.setStatus(_B)
_AdGenEfmExtPerfPort24HrThreshRxCodingErrors_Type=Unsigned32
_AdGenEfmExtPerfPort24HrThreshRxCodingErrors_Object=MibTableColumn
adGenEfmExtPerfPort24HrThreshRxCodingErrors=_AdGenEfmExtPerfPort24HrThreshRxCodingErrors_Object((1,3,6,1,4,1,664,5,66,3,3,6,1,6),_AdGenEfmExtPerfPort24HrThreshRxCodingErrors_Type())
adGenEfmExtPerfPort24HrThreshRxCodingErrors.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenEfmExtPerfPort24HrThreshRxCodingErrors.setStatus(_B)
_AdGenEfmExtPerfPortResetTable_Object=MibTable
adGenEfmExtPerfPortResetTable=_AdGenEfmExtPerfPortResetTable_Object((1,3,6,1,4,1,664,5,66,3,3,7))
if mibBuilder.loadTexts:adGenEfmExtPerfPortResetTable.setStatus(_B)
_AdGenEfmExtPerfPortResetEntry_Object=MibTableRow
adGenEfmExtPerfPortResetEntry=_AdGenEfmExtPerfPortResetEntry_Object((1,3,6,1,4,1,664,5,66,3,3,7,1))
adGenEfmExtPerfPortResetEntry.setIndexNames((0,_A,_C))
if mibBuilder.loadTexts:adGenEfmExtPerfPortResetEntry.setStatus(_B)
class _AdGenEfmExtPerfPortResetData_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_AdGenEfmExtPerfPortResetData_Type.__name__=_M
_AdGenEfmExtPerfPortResetData_Object=MibTableColumn
adGenEfmExtPerfPortResetData=_AdGenEfmExtPerfPortResetData_Object((1,3,6,1,4,1,664,5,66,3,3,7,1,1),_AdGenEfmExtPerfPortResetData_Type())
adGenEfmExtPerfPortResetData.setMaxAccess(_N)
if mibBuilder.loadTexts:adGenEfmExtPerfPortResetData.setStatus(_B)
_AdGenEfmExtAlarmsPrefix_ObjectIdentity=ObjectIdentity
adGenEfmExtAlarmsPrefix=_AdGenEfmExtAlarmsPrefix_ObjectIdentity((1,3,6,1,4,1,664,5,66,3,10))
_AdGenEfmExtAlarms_ObjectIdentity=ObjectIdentity
adGenEfmExtAlarms=_AdGenEfmExtAlarms_ObjectIdentity((1,3,6,1,4,1,664,5,66,3,10,0))
adGenEfmExtStatGroup=ObjectGroup((1,3,6,1,4,1,664,5,66,3,2,1,1))
adGenEfmExtStatGroup.setObjects(*((_D,_Q),(_D,_R),(_D,_S),(_D,_T),(_D,_U),(_D,_V),(_D,_W),(_D,_X)))
if mibBuilder.loadTexts:adGenEfmExtStatGroup.setStatus(_B)
adGenEfmExtGroupDownClr=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,2))
adGenEfmExtGroupDownClr.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroupDownClr.setStatus(_B)
adGenEfmExtGroupDownAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,3))
adGenEfmExtGroupDownAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroupDownAct.setStatus(_B)
adGenEfmExtLinkDownClr=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,4))
adGenEfmExtLinkDownClr.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtLinkDownClr.setStatus(_B)
adGenEfmExtLinkDownAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,5))
adGenEfmExtLinkDownAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtLinkDownAct.setStatus(_B)
adGenEfmExtGroupUpPartialClr=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,6))
adGenEfmExtGroupUpPartialClr.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroupUpPartialClr.setStatus(_B)
adGenEfmExtGroupUpPartialAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,7))
adGenEfmExtGroupUpPartialAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroupUpPartialAct.setStatus(_B)
adGenEfmExtGroupDownstreamBandwidthClr=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,8))
adGenEfmExtGroupDownstreamBandwidthClr.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroupDownstreamBandwidthClr.setStatus(_B)
adGenEfmExtGroupDownstreamBandwidthAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,9))
adGenEfmExtGroupDownstreamBandwidthAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroupDownstreamBandwidthAct.setStatus(_B)
adGenEfmExtGroupUpstreamBandwidthClr=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,10))
adGenEfmExtGroupUpstreamBandwidthClr.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroupUpstreamBandwidthClr.setStatus(_B)
adGenEfmExtGroupUpstreamBandwidthAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,11))
adGenEfmExtGroupUpstreamBandwidthAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroupUpstreamBandwidthAct.setStatus(_B)
adGenEfmExtGroupDownstream4xRateViolationClr=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,12))
adGenEfmExtGroupDownstream4xRateViolationClr.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroupDownstream4xRateViolationClr.setStatus(_B)
adGenEfmExtGroupDownstream4xRateViolationAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,13))
adGenEfmExtGroupDownstream4xRateViolationAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroupDownstream4xRateViolationAct.setStatus(_B)
adGenEfmExtGroupUpstream4xRateViolationClr=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,14))
adGenEfmExtGroupUpstream4xRateViolationClr.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroupUpstream4xRateViolationClr.setStatus(_B)
adGenEfmExtGroupUpstream4xRateViolationAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,15))
adGenEfmExtGroupUpstream4xRateViolationAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroupUpstream4xRateViolationAct.setStatus(_B)
adGenEfmExtGroupRemoteLoopbackClr=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,16))
adGenEfmExtGroupRemoteLoopbackClr.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroupRemoteLoopbackClr.setStatus(_B)
adGenEfmExtGroupRemoteLoopbackAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,17))
adGenEfmExtGroupRemoteLoopbackAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroupRemoteLoopbackAct.setStatus(_B)
adGenEfmExtGroupLocalLoopbackClr=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,18))
adGenEfmExtGroupLocalLoopbackClr.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroupLocalLoopbackClr.setStatus(_B)
adGenEfmExtGroupLocalLoopbackAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,19))
adGenEfmExtGroupLocalLoopbackAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroupLocalLoopbackAct.setStatus(_B)
adGenEfmExtGroup15MinRxBadFragmentsAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,20))
adGenEfmExtGroup15MinRxBadFragmentsAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroup15MinRxBadFragmentsAct.setStatus(_B)
adGenEfmExtGroup15MinRxLostFragmentsAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,21))
adGenEfmExtGroup15MinRxLostFragmentsAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroup15MinRxLostFragmentsAct.setStatus(_B)
adGenEfmExtGroup15MinRxLostStartsAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,22))
adGenEfmExtGroup15MinRxLostStartsAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroup15MinRxLostStartsAct.setStatus(_B)
adGenEfmExtGroup15MinRxLostEndsAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,23))
adGenEfmExtGroup15MinRxLostEndsAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroup15MinRxLostEndsAct.setStatus(_B)
adGenEfmExtGroup24HrRxBadFragmentsAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,24))
adGenEfmExtGroup24HrRxBadFragmentsAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroup24HrRxBadFragmentsAct.setStatus(_B)
adGenEfmExtGroup24HrRxLostFragmentsAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,25))
adGenEfmExtGroup24HrRxLostFragmentsAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroup24HrRxLostFragmentsAct.setStatus(_B)
adGenEfmExtGroup24HrRxLostStartsAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,26))
adGenEfmExtGroup24HrRxLostStartsAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroup24HrRxLostStartsAct.setStatus(_B)
adGenEfmExtGroup24HrRxLostEndsAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,27))
adGenEfmExtGroup24HrRxLostEndsAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroup24HrRxLostEndsAct.setStatus(_B)
adGenEfmExtLink15MinRxErroredFragmentsAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,28))
adGenEfmExtLink15MinRxErroredFragmentsAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtLink15MinRxErroredFragmentsAct.setStatus(_B)
adGenEfmExtLink15MinRxSmallFragmentsAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,29))
adGenEfmExtLink15MinRxSmallFragmentsAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtLink15MinRxSmallFragmentsAct.setStatus(_B)
adGenEfmExtLink15MinRxLargeFragmentsAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,30))
adGenEfmExtLink15MinRxLargeFragmentsAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtLink15MinRxLargeFragmentsAct.setStatus(_B)
adGenEfmExtLink15MinRxDiscardedFragmentsAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,31))
adGenEfmExtLink15MinRxDiscardedFragmentsAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtLink15MinRxDiscardedFragmentsAct.setStatus(_B)
adGenEfmExtLink15MinRxFcsErrorsAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,32))
adGenEfmExtLink15MinRxFcsErrorsAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtLink15MinRxFcsErrorsAct.setStatus(_B)
adGenEfmExtLink15MinRxCodingErrorsAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,33))
adGenEfmExtLink15MinRxCodingErrorsAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtLink15MinRxCodingErrorsAct.setStatus(_B)
adGenEfmExtLink24HrRxErroredFragmentsAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,34))
adGenEfmExtLink24HrRxErroredFragmentsAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtLink24HrRxErroredFragmentsAct.setStatus(_B)
adGenEfmExtLink24HrRxSmallFragmentsAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,35))
adGenEfmExtLink24HrRxSmallFragmentsAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtLink24HrRxSmallFragmentsAct.setStatus(_B)
adGenEfmExtLink24HrRxLargeFragmentsAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,36))
adGenEfmExtLink24HrRxLargeFragmentsAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtLink24HrRxLargeFragmentsAct.setStatus(_B)
adGenEfmExtLink24HrRxDiscardedFragmentsAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,37))
adGenEfmExtLink24HrRxDiscardedFragmentsAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtLink24HrRxDiscardedFragmentsAct.setStatus(_B)
adGenEfmExtLink24HrRxFcsErrorsAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,38))
adGenEfmExtLink24HrRxFcsErrorsAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtLink24HrRxFcsErrorsAct.setStatus(_B)
adGenEfmExtLink24HrRxCodingErrorsAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,39))
adGenEfmExtLink24HrRxCodingErrorsAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtLink24HrRxCodingErrorsAct.setStatus(_B)
adGenEfmExtLinkXCVThreshExceededClr=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,50))
adGenEfmExtLinkXCVThreshExceededClr.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtLinkXCVThreshExceededClr.setStatus(_B)
adGenEfmExtLinkXCVThreshExceededAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,51))
adGenEfmExtLinkXCVThreshExceededAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtLinkXCVThreshExceededAct.setStatus(_B)
adGenEfmExtLinkRemovedXCVThreshExceededClr=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,52))
adGenEfmExtLinkRemovedXCVThreshExceededClr.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtLinkRemovedXCVThreshExceededClr.setStatus(_B)
adGenEfmExtLinkRemovedXCVThreshExceededAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,53))
adGenEfmExtLinkRemovedXCVThreshExceededAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtLinkRemovedXCVThreshExceededAct.setStatus(_B)
adGenEfmExtLinkRemovedFarEndLbkDetectedClr=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,54))
adGenEfmExtLinkRemovedFarEndLbkDetectedClr.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtLinkRemovedFarEndLbkDetectedClr.setStatus(_B)
adGenEfmExtLinkRemovedFarEndLbkDetectedAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,55))
adGenEfmExtLinkRemovedFarEndLbkDetectedAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtLinkRemovedFarEndLbkDetectedAct.setStatus(_B)
adGenEfmExtPortDownClr=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,80))
adGenEfmExtPortDownClr.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtPortDownClr.setStatus(_B)
adGenEfmExtPortDownAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,81))
adGenEfmExtPortDownAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtPortDownAct.setStatus(_B)
adGenEfmExtPort15MinRxCodingErrorsAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,91))
adGenEfmExtPort15MinRxCodingErrorsAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtPort15MinRxCodingErrorsAct.setStatus(_B)
adGenEfmExtPort24HrRxCodingErrorsAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,92))
adGenEfmExtPort24HrRxCodingErrorsAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtPort24HrRxCodingErrorsAct.setStatus(_B)
adGenEfmExtGroupSecondaryDownstreamBandwidthClr=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,93))
adGenEfmExtGroupSecondaryDownstreamBandwidthClr.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroupSecondaryDownstreamBandwidthClr.setStatus(_B)
adGenEfmExtGroupSecondaryDownstreamBandwidthAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,94))
adGenEfmExtGroupSecondaryDownstreamBandwidthAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroupSecondaryDownstreamBandwidthAct.setStatus(_B)
adGenEfmExtGroupSecondaryUpstreamBandwidthClr=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,95))
adGenEfmExtGroupSecondaryUpstreamBandwidthClr.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroupSecondaryUpstreamBandwidthClr.setStatus(_B)
adGenEfmExtGroupSecondaryUpstreamBandwidthAct=NotificationType((1,3,6,1,4,1,664,5,66,3,10,0,96))
adGenEfmExtGroupSecondaryUpstreamBandwidthAct.setObjects(*((_G,_H),(_J,_K),(_E,_F),(_A,_I),(_A,_C)))
if mibBuilder.loadTexts:adGenEfmExtGroupSecondaryUpstreamBandwidthAct.setStatus(_B)
adGenEfmExtEventGroup=NotificationGroup((1,3,6,1,4,1,664,5,66,3,2,1,2))
adGenEfmExtEventGroup.setObjects(*((_D,_Y),(_D,_Z),(_D,_a),(_D,_b),(_D,_c),(_D,_d),(_D,_e),(_D,_f),(_D,_g),(_D,_h),(_D,_i),(_D,_j),(_D,_k),(_D,_l),(_D,_m),(_D,_n),(_D,_o),(_D,_p),(_D,_q),(_D,_r),(_D,_s),(_D,_t),(_D,_u),(_D,_v),(_D,_w),(_D,_x),(_D,_y),(_D,_z),(_D,_A0),(_D,_A1),(_D,_A2),(_D,_A3),(_D,_A4),(_D,_A5),(_D,_A6),(_D,_A7),(_D,_A8),(_D,_A9),(_D,_AA),(_D,_AB),(_D,_AC),(_D,_AD),(_D,_AE),(_D,_AF),(_D,_AG),(_D,_AH),(_D,_AI),(_D,_AJ)))
if mibBuilder.loadTexts:adGenEfmExtEventGroup.setStatus(_B)
mibBuilder.exportSymbols(_D,**{'adGenEfmExtStatus':adGenEfmExtStatus,'adGenEfmExtStatGroupTable':adGenEfmExtStatGroupTable,'adGenEfmExtStatGroupEntry':adGenEfmExtStatGroupEntry,_Q:adGenEfmExtStatGroupStatus,_R:adGenEfmExtStatGroupSize,_S:adGenEfmExtStatGroupNumActiveLinks,_T:adGenEfmExtStatGroupUAS,_U:adGenEfmExtStatGroupFailures,'adGenEfmExtStatLinkTable':adGenEfmExtStatLinkTable,'adGenEfmExtStatLinkEntry':adGenEfmExtStatLinkEntry,_V:adGenEfmExtStatLinkNeTcSync,_W:adGenEfmExtStatLinkFeTcSync,_X:adGenEfmExtStatLinkSkew,'adGenEfmExtStatLinkStatus':adGenEfmExtStatLinkStatus,'adGenEfmExtStatLinkFeId':adGenEfmExtStatLinkFeId,'adGenEfmExtMibConformance':adGenEfmExtMibConformance,'adGenEfmExtMibGroups':adGenEfmExtMibGroups,'adGenEfmExtStatGroup':adGenEfmExtStatGroup,'adGenEfmExtEventGroup':adGenEfmExtEventGroup,'adGenEfmExtPerformance':adGenEfmExtPerformance,'adGenEfmExtPerfPortCurr15MinTable':adGenEfmExtPerfPortCurr15MinTable,'adGenEfmExtPerfPortCurr15MinEntry':adGenEfmExtPerfPortCurr15MinEntry,'adGenEfmExtPerfPort15MinValidIntervals':adGenEfmExtPerfPort15MinValidIntervals,'adGenEfmExtPerfPortCurr15MinTxOctets':adGenEfmExtPerfPortCurr15MinTxOctets,'adGenEfmExtPerfPortCurr15MinTxFrames':adGenEfmExtPerfPortCurr15MinTxFrames,'adGenEfmExtPerfPortCurr15MinRxOctets':adGenEfmExtPerfPortCurr15MinRxOctets,'adGenEfmExtPerfPortCurr15MinRxFrames':adGenEfmExtPerfPortCurr15MinRxFrames,'adGenEfmExtPerfPortCurr15MinRxCodingErrors':adGenEfmExtPerfPortCurr15MinRxCodingErrors,'adGenEfmExtPerfPort15MinIntTable':adGenEfmExtPerfPort15MinIntTable,'adGenEfmExtPerfPort15MinIntEntry':adGenEfmExtPerfPort15MinIntEntry,_O:adGenEfmExtPerfPort15MinIntNumber,'adGenEfmExtPerfPort15MinIntTxOctets':adGenEfmExtPerfPort15MinIntTxOctets,'adGenEfmExtPerfPort15MinIntTxFrames':adGenEfmExtPerfPort15MinIntTxFrames,'adGenEfmExtPerfPort15MinIntRxOctets':adGenEfmExtPerfPort15MinIntRxOctets,'adGenEfmExtPerfPort15MinIntRxFrames':adGenEfmExtPerfPort15MinIntRxFrames,'adGenEfmExtPerfPort15MinIntRxCodingErrors':adGenEfmExtPerfPort15MinIntRxCodingErrors,'adGenEfmExtPerfPortCurr24HrTable':adGenEfmExtPerfPortCurr24HrTable,'adGenEfmExtPerfPortCurr24HrEntry':adGenEfmExtPerfPortCurr24HrEntry,'adGenEfmExtPerfPort24HrValidIntervals':adGenEfmExtPerfPort24HrValidIntervals,'adGenEfmExtPerfPortCurr24HrTxOctets':adGenEfmExtPerfPortCurr24HrTxOctets,'adGenEfmExtPerfPortCurr24HrTxFrames':adGenEfmExtPerfPortCurr24HrTxFrames,'adGenEfmExtPerfPortCurr24HrRxOctets':adGenEfmExtPerfPortCurr24HrRxOctets,'adGenEfmExtPerfPortCurr24HrRxFrames':adGenEfmExtPerfPortCurr24HrRxFrames,'adGenEfmExtPerfPortCurr24HrRxCodingErrors':adGenEfmExtPerfPortCurr24HrRxCodingErrors,'adGenEfmExtPerfPort24HrIntTable':adGenEfmExtPerfPort24HrIntTable,'adGenEfmExtPerfPort24HrIntEntry':adGenEfmExtPerfPort24HrIntEntry,_P:adGenEfmExtPerfPort24HrIntNumber,'adGenEfmExtPerfPort24HrIntTxOctets':adGenEfmExtPerfPort24HrIntTxOctets,'adGenEfmExtPerfPort24HrIntTxFrames':adGenEfmExtPerfPort24HrIntTxFrames,'adGenEfmExtPerfPort24HrIntRxOctets':adGenEfmExtPerfPort24HrIntRxOctets,'adGenEfmExtPerfPort24HrIntRxFrames':adGenEfmExtPerfPort24HrIntRxFrames,'adGenEfmExtPerfPort24HrIntRxCodingErrors':adGenEfmExtPerfPort24HrIntRxCodingErrors,'adGenEfmExtPerfPort15MinThreshTable':adGenEfmExtPerfPort15MinThreshTable,'adGenEfmExtPerfPort15MinThreshEntry':adGenEfmExtPerfPort15MinThreshEntry,'adGenEfmExtPerfPort15MinThreshRxCodingErrors':adGenEfmExtPerfPort15MinThreshRxCodingErrors,'adGenEfmExtPerfPort24HrThreshTable':adGenEfmExtPerfPort24HrThreshTable,'adGenEfmExtPerfPort24HrThreshEntry':adGenEfmExtPerfPort24HrThreshEntry,'adGenEfmExtPerfPort24HrThreshRxCodingErrors':adGenEfmExtPerfPort24HrThreshRxCodingErrors,'adGenEfmExtPerfPortResetTable':adGenEfmExtPerfPortResetTable,'adGenEfmExtPerfPortResetEntry':adGenEfmExtPerfPortResetEntry,'adGenEfmExtPerfPortResetData':adGenEfmExtPerfPortResetData,'adGenEfmExtAlarmsPrefix':adGenEfmExtAlarmsPrefix,'adGenEfmExtAlarms':adGenEfmExtAlarms,_Y:adGenEfmExtGroupDownClr,_Z:adGenEfmExtGroupDownAct,_a:adGenEfmExtLinkDownClr,_b:adGenEfmExtLinkDownAct,_c:adGenEfmExtGroupUpPartialClr,_d:adGenEfmExtGroupUpPartialAct,_e:adGenEfmExtGroupDownstreamBandwidthClr,_f:adGenEfmExtGroupDownstreamBandwidthAct,_g:adGenEfmExtGroupUpstreamBandwidthClr,_h:adGenEfmExtGroupUpstreamBandwidthAct,_i:adGenEfmExtGroupDownstream4xRateViolationClr,_j:adGenEfmExtGroupDownstream4xRateViolationAct,_k:adGenEfmExtGroupUpstream4xRateViolationClr,_l:adGenEfmExtGroupUpstream4xRateViolationAct,_AC:adGenEfmExtGroupRemoteLoopbackClr,_AD:adGenEfmExtGroupRemoteLoopbackAct,_AE:adGenEfmExtGroupLocalLoopbackClr,_AF:adGenEfmExtGroupLocalLoopbackAct,_m:adGenEfmExtGroup15MinRxBadFragmentsAct,_n:adGenEfmExtGroup15MinRxLostFragmentsAct,_o:adGenEfmExtGroup15MinRxLostStartsAct,_p:adGenEfmExtGroup15MinRxLostEndsAct,_q:adGenEfmExtGroup24HrRxBadFragmentsAct,_r:adGenEfmExtGroup24HrRxLostFragmentsAct,_s:adGenEfmExtGroup24HrRxLostStartsAct,_t:adGenEfmExtGroup24HrRxLostEndsAct,_u:adGenEfmExtLink15MinRxErroredFragmentsAct,_v:adGenEfmExtLink15MinRxSmallFragmentsAct,_w:adGenEfmExtLink15MinRxLargeFragmentsAct,_x:adGenEfmExtLink15MinRxDiscardedFragmentsAct,_y:adGenEfmExtLink15MinRxFcsErrorsAct,_z:adGenEfmExtLink15MinRxCodingErrorsAct,_A0:adGenEfmExtLink24HrRxErroredFragmentsAct,_A1:adGenEfmExtLink24HrRxSmallFragmentsAct,_A2:adGenEfmExtLink24HrRxLargeFragmentsAct,_A3:adGenEfmExtLink24HrRxDiscardedFragmentsAct,_A4:adGenEfmExtLink24HrRxFcsErrorsAct,_A5:adGenEfmExtLink24HrRxCodingErrorsAct,_A6:adGenEfmExtLinkXCVThreshExceededClr,_A7:adGenEfmExtLinkXCVThreshExceededAct,_A8:adGenEfmExtLinkRemovedXCVThreshExceededClr,_A9:adGenEfmExtLinkRemovedXCVThreshExceededAct,_AA:adGenEfmExtLinkRemovedFarEndLbkDetectedClr,_AB:adGenEfmExtLinkRemovedFarEndLbkDetectedAct,'adGenEfmExtPortDownClr':adGenEfmExtPortDownClr,'adGenEfmExtPortDownAct':adGenEfmExtPortDownAct,'adGenEfmExtPort15MinRxCodingErrorsAct':adGenEfmExtPort15MinRxCodingErrorsAct,'adGenEfmExtPort24HrRxCodingErrorsAct':adGenEfmExtPort24HrRxCodingErrorsAct,_AG:adGenEfmExtGroupSecondaryDownstreamBandwidthClr,_AH:adGenEfmExtGroupSecondaryDownstreamBandwidthAct,_AI:adGenEfmExtGroupSecondaryUpstreamBandwidthClr,_AJ:adGenEfmExtGroupSecondaryUpstreamBandwidthAct,'adGenEfmExtMIB':adGenEfmExtMIB})