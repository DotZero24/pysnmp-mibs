_O='s5EnSStatSrcIndx'
_N='s5EnPStatSrcIndx'
_M='s5EnBStatSrcIndx'
_L='s5EnPortExtIndx'
_K='s5EnPortExtBrdIndx'
_J='s5EnPortIndx'
_I='s5EnPortBrdIndx'
_H='unknown'
_G='other'
_F='read-write'
_E='OctetString'
_D='S5-ETHERNET-COMMON-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
s5EnCfg,s5EnStat=mibBuilder.importSymbols('S5-ETHERNET-MIB','s5EnCfg','s5EnStat')
AttId,SrcIndx,TimeIntervalSec=mibBuilder.importSymbols('S5-TCS-MIB','AttId','SrcIndx','TimeIntervalSec')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
s5EthernetCommonMib=ModuleIdentity((1,3,6,1,4,1,45,1,6,6,1,0))
if mibBuilder.loadTexts:s5EthernetCommonMib.setRevisions(('2004-07-20 00:00',))
_S5EnPortTable_Object=MibTable
s5EnPortTable=_S5EnPortTable_Object((1,3,6,1,4,1,45,1,6,6,1,1))
if mibBuilder.loadTexts:s5EnPortTable.setStatus(_A)
_S5EnPortEntry_Object=MibTableRow
s5EnPortEntry=_S5EnPortEntry_Object((1,3,6,1,4,1,45,1,6,6,1,1,1))
s5EnPortEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:s5EnPortEntry.setStatus(_A)
class _S5EnPortBrdIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_S5EnPortBrdIndx_Type.__name__=_C
_S5EnPortBrdIndx_Object=MibTableColumn
s5EnPortBrdIndx=_S5EnPortBrdIndx_Object((1,3,6,1,4,1,45,1,6,6,1,1,1,1),_S5EnPortBrdIndx_Type())
s5EnPortBrdIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnPortBrdIndx.setStatus(_A)
class _S5EnPortIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_S5EnPortIndx_Type.__name__=_C
_S5EnPortIndx_Object=MibTableColumn
s5EnPortIndx=_S5EnPortIndx_Object((1,3,6,1,4,1,45,1,6,6,1,1,1,2),_S5EnPortIndx_Type())
s5EnPortIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnPortIndx.setStatus(_A)
class _S5EnPortPartStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),('enabled',2),('partition',3),('autoPartition',4),('timedPartition',5)))
_S5EnPortPartStatus_Type.__name__=_C
_S5EnPortPartStatus_Object=MibTableColumn
s5EnPortPartStatus=_S5EnPortPartStatus_Object((1,3,6,1,4,1,45,1,6,6,1,1,1,3),_S5EnPortPartStatus_Type())
s5EnPortPartStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:s5EnPortPartStatus.setStatus(_A)
_S5EnPortPartTime_Type=TimeIntervalSec
_S5EnPortPartTime_Object=MibTableColumn
s5EnPortPartTime=_S5EnPortPartTime_Object((1,3,6,1,4,1,45,1,6,6,1,1,1,4),_S5EnPortPartTime_Type())
s5EnPortPartTime.setMaxAccess(_F)
if mibBuilder.loadTexts:s5EnPortPartTime.setStatus(_A)
class _S5EnPortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('off',2),('on',3)))
_S5EnPortLinkStatus_Type.__name__=_C
_S5EnPortLinkStatus_Object=MibTableColumn
s5EnPortLinkStatus=_S5EnPortLinkStatus_Object((1,3,6,1,4,1,45,1,6,6,1,1,1,5),_S5EnPortLinkStatus_Type())
s5EnPortLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnPortLinkStatus.setStatus(_A)
class _S5EnPortJabberStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('jabbering',2),('ok',3)))
_S5EnPortJabberStatus_Type.__name__=_C
_S5EnPortJabberStatus_Object=MibTableColumn
s5EnPortJabberStatus=_S5EnPortJabberStatus_Object((1,3,6,1,4,1,45,1,6,6,1,1,1,6),_S5EnPortJabberStatus_Type())
s5EnPortJabberStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnPortJabberStatus.setStatus(_A)
_S5EnPortExtTable_Object=MibTable
s5EnPortExtTable=_S5EnPortExtTable_Object((1,3,6,1,4,1,45,1,6,6,1,3))
if mibBuilder.loadTexts:s5EnPortExtTable.setStatus(_A)
_S5EnPortExtEntry_Object=MibTableRow
s5EnPortExtEntry=_S5EnPortExtEntry_Object((1,3,6,1,4,1,45,1,6,6,1,3,1))
s5EnPortExtEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:s5EnPortExtEntry.setStatus(_A)
class _S5EnPortExtBrdIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_S5EnPortExtBrdIndx_Type.__name__=_C
_S5EnPortExtBrdIndx_Object=MibTableColumn
s5EnPortExtBrdIndx=_S5EnPortExtBrdIndx_Object((1,3,6,1,4,1,45,1,6,6,1,3,1,1),_S5EnPortExtBrdIndx_Type())
s5EnPortExtBrdIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnPortExtBrdIndx.setStatus(_A)
class _S5EnPortExtIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_S5EnPortExtIndx_Type.__name__=_C
_S5EnPortExtIndx_Object=MibTableColumn
s5EnPortExtIndx=_S5EnPortExtIndx_Object((1,3,6,1,4,1,45,1,6,6,1,3,1,2),_S5EnPortExtIndx_Type())
s5EnPortExtIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnPortExtIndx.setStatus(_A)
class _S5EnPortExtHwCapability_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_S5EnPortExtHwCapability_Type.__name__=_E
_S5EnPortExtHwCapability_Object=MibTableColumn
s5EnPortExtHwCapability=_S5EnPortExtHwCapability_Object((1,3,6,1,4,1,45,1,6,6,1,3,1,3),_S5EnPortExtHwCapability_Type())
s5EnPortExtHwCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnPortExtHwCapability.setStatus(_A)
class _S5EnPortExtAutoNegAdv_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_S5EnPortExtAutoNegAdv_Type.__name__=_E
_S5EnPortExtAutoNegAdv_Object=MibTableColumn
s5EnPortExtAutoNegAdv=_S5EnPortExtAutoNegAdv_Object((1,3,6,1,4,1,45,1,6,6,1,3,1,4),_S5EnPortExtAutoNegAdv_Type())
s5EnPortExtAutoNegAdv.setMaxAccess(_F)
if mibBuilder.loadTexts:s5EnPortExtAutoNegAdv.setStatus(_A)
class _S5EnPortExtAutoNegRcvd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_S5EnPortExtAutoNegRcvd_Type.__name__=_E
_S5EnPortExtAutoNegRcvd_Object=MibTableColumn
s5EnPortExtAutoNegRcvd=_S5EnPortExtAutoNegRcvd_Object((1,3,6,1,4,1,45,1,6,6,1,3,1,5),_S5EnPortExtAutoNegRcvd_Type())
s5EnPortExtAutoNegRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnPortExtAutoNegRcvd.setStatus(_A)
_S5EnPortExt10MbSegAttCfg_Type=AttId
_S5EnPortExt10MbSegAttCfg_Object=MibTableColumn
s5EnPortExt10MbSegAttCfg=_S5EnPortExt10MbSegAttCfg_Object((1,3,6,1,4,1,45,1,6,6,1,3,1,6),_S5EnPortExt10MbSegAttCfg_Type())
s5EnPortExt10MbSegAttCfg.setMaxAccess(_F)
if mibBuilder.loadTexts:s5EnPortExt10MbSegAttCfg.setStatus(_A)
_S5EnPortExt100MbSegAttCfg_Type=AttId
_S5EnPortExt100MbSegAttCfg_Object=MibTableColumn
s5EnPortExt100MbSegAttCfg=_S5EnPortExt100MbSegAttCfg_Object((1,3,6,1,4,1,45,1,6,6,1,3,1,7),_S5EnPortExt100MbSegAttCfg_Type())
s5EnPortExt100MbSegAttCfg.setMaxAccess(_F)
if mibBuilder.loadTexts:s5EnPortExt100MbSegAttCfg.setStatus(_A)
class _S5EnPortExt10MbSegConnCapability_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_S5EnPortExt10MbSegConnCapability_Type.__name__=_E
_S5EnPortExt10MbSegConnCapability_Object=MibTableColumn
s5EnPortExt10MbSegConnCapability=_S5EnPortExt10MbSegConnCapability_Object((1,3,6,1,4,1,45,1,6,6,1,3,1,8),_S5EnPortExt10MbSegConnCapability_Type())
s5EnPortExt10MbSegConnCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnPortExt10MbSegConnCapability.setStatus(_A)
class _S5EnPortExt100MbSegConnCapability_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_S5EnPortExt100MbSegConnCapability_Type.__name__=_E
_S5EnPortExt100MbSegConnCapability_Object=MibTableColumn
s5EnPortExt100MbSegConnCapability=_S5EnPortExt100MbSegConnCapability_Object((1,3,6,1,4,1,45,1,6,6,1,3,1,9),_S5EnPortExt100MbSegConnCapability_Type())
s5EnPortExt100MbSegConnCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnPortExt100MbSegConnCapability.setStatus(_A)
class _S5EnPortExtActiveSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('bps10M',2),('bps100M',3)))
_S5EnPortExtActiveSpeed_Type.__name__=_C
_S5EnPortExtActiveSpeed_Object=MibTableColumn
s5EnPortExtActiveSpeed=_S5EnPortExtActiveSpeed_Object((1,3,6,1,4,1,45,1,6,6,1,3,1,10),_S5EnPortExtActiveSpeed_Type())
s5EnPortExtActiveSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnPortExtActiveSpeed.setStatus(_A)
class _S5EnPortExtCurDuplexMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('halfDuplex',2),('fullDuplex',3)))
_S5EnPortExtCurDuplexMode_Type.__name__=_C
_S5EnPortExtCurDuplexMode_Object=MibTableColumn
s5EnPortExtCurDuplexMode=_S5EnPortExtCurDuplexMode_Object((1,3,6,1,4,1,45,1,6,6,1,3,1,11),_S5EnPortExtCurDuplexMode_Type())
s5EnPortExtCurDuplexMode.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnPortExtCurDuplexMode.setStatus(_A)
_S5EnBStatTable_Object=MibTable
s5EnBStatTable=_S5EnBStatTable_Object((1,3,6,1,4,1,45,1,6,6,2,1))
if mibBuilder.loadTexts:s5EnBStatTable.setStatus(_A)
_S5EnBStatEntry_Object=MibTableRow
s5EnBStatEntry=_S5EnBStatEntry_Object((1,3,6,1,4,1,45,1,6,6,2,1,1))
s5EnBStatEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:s5EnBStatEntry.setStatus(_A)
_S5EnBStatSrcIndx_Type=SrcIndx
_S5EnBStatSrcIndx_Object=MibTableColumn
s5EnBStatSrcIndx=_S5EnBStatSrcIndx_Object((1,3,6,1,4,1,45,1,6,6,2,1,1,1),_S5EnBStatSrcIndx_Type())
s5EnBStatSrcIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnBStatSrcIndx.setStatus(_A)
_S5EnBStatGoodOctets_Type=Counter32
_S5EnBStatGoodOctets_Object=MibTableColumn
s5EnBStatGoodOctets=_S5EnBStatGoodOctets_Object((1,3,6,1,4,1,45,1,6,6,2,1,1,2),_S5EnBStatGoodOctets_Type())
s5EnBStatGoodOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnBStatGoodOctets.setStatus(_A)
_S5EnBStatGoodFrms_Type=Counter32
_S5EnBStatGoodFrms_Object=MibTableColumn
s5EnBStatGoodFrms=_S5EnBStatGoodFrms_Object((1,3,6,1,4,1,45,1,6,6,2,1,1,3),_S5EnBStatGoodFrms_Type())
s5EnBStatGoodFrms.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnBStatGoodFrms.setStatus(_A)
_S5EnBStatBcastFrms_Type=Counter32
_S5EnBStatBcastFrms_Object=MibTableColumn
s5EnBStatBcastFrms=_S5EnBStatBcastFrms_Object((1,3,6,1,4,1,45,1,6,6,2,1,1,4),_S5EnBStatBcastFrms_Type())
s5EnBStatBcastFrms.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnBStatBcastFrms.setStatus(_A)
_S5EnBStatMcastFrms_Type=Counter32
_S5EnBStatMcastFrms_Object=MibTableColumn
s5EnBStatMcastFrms=_S5EnBStatMcastFrms_Object((1,3,6,1,4,1,45,1,6,6,2,1,1,5),_S5EnBStatMcastFrms_Type())
s5EnBStatMcastFrms.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnBStatMcastFrms.setStatus(_A)
_S5EnBStatAlignErrors_Type=Counter32
_S5EnBStatAlignErrors_Object=MibTableColumn
s5EnBStatAlignErrors=_S5EnBStatAlignErrors_Object((1,3,6,1,4,1,45,1,6,6,2,1,1,6),_S5EnBStatAlignErrors_Type())
s5EnBStatAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnBStatAlignErrors.setStatus(_A)
_S5EnBStatFcsErrors_Type=Counter32
_S5EnBStatFcsErrors_Object=MibTableColumn
s5EnBStatFcsErrors=_S5EnBStatFcsErrors_Object((1,3,6,1,4,1,45,1,6,6,2,1,1,7),_S5EnBStatFcsErrors_Type())
s5EnBStatFcsErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnBStatFcsErrors.setStatus(_A)
_S5EnBStatRunts_Type=Counter32
_S5EnBStatRunts_Object=MibTableColumn
s5EnBStatRunts=_S5EnBStatRunts_Object((1,3,6,1,4,1,45,1,6,6,2,1,1,8),_S5EnBStatRunts_Type())
s5EnBStatRunts.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnBStatRunts.setStatus(_A)
_S5EnBStatTooLongFrms_Type=Counter32
_S5EnBStatTooLongFrms_Object=MibTableColumn
s5EnBStatTooLongFrms=_S5EnBStatTooLongFrms_Object((1,3,6,1,4,1,45,1,6,6,2,1,1,9),_S5EnBStatTooLongFrms_Type())
s5EnBStatTooLongFrms.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnBStatTooLongFrms.setStatus(_A)
_S5EnBStatFragments_Type=Counter32
_S5EnBStatFragments_Object=MibTableColumn
s5EnBStatFragments=_S5EnBStatFragments_Object((1,3,6,1,4,1,45,1,6,6,2,1,1,10),_S5EnBStatFragments_Type())
s5EnBStatFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnBStatFragments.setStatus(_A)
_S5EnBStatVeryLongEvents_Type=Counter32
_S5EnBStatVeryLongEvents_Object=MibTableColumn
s5EnBStatVeryLongEvents=_S5EnBStatVeryLongEvents_Object((1,3,6,1,4,1,45,1,6,6,2,1,1,11),_S5EnBStatVeryLongEvents_Type())
s5EnBStatVeryLongEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnBStatVeryLongEvents.setStatus(_A)
_S5EnBStatColls_Type=Counter32
_S5EnBStatColls_Object=MibTableColumn
s5EnBStatColls=_S5EnBStatColls_Object((1,3,6,1,4,1,45,1,6,6,2,1,1,12),_S5EnBStatColls_Type())
s5EnBStatColls.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnBStatColls.setStatus(_A)
_S5EnBStatLateColls_Type=Counter32
_S5EnBStatLateColls_Object=MibTableColumn
s5EnBStatLateColls=_S5EnBStatLateColls_Object((1,3,6,1,4,1,45,1,6,6,2,1,1,13),_S5EnBStatLateColls_Type())
s5EnBStatLateColls.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnBStatLateColls.setStatus(_A)
_S5EnBStatShortEvents_Type=Counter32
_S5EnBStatShortEvents_Object=MibTableColumn
s5EnBStatShortEvents=_S5EnBStatShortEvents_Object((1,3,6,1,4,1,45,1,6,6,2,1,1,14),_S5EnBStatShortEvents_Type())
s5EnBStatShortEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnBStatShortEvents.setStatus(_A)
_S5EnBStatRateMismatches_Type=Counter32
_S5EnBStatRateMismatches_Object=MibTableColumn
s5EnBStatRateMismatches=_S5EnBStatRateMismatches_Object((1,3,6,1,4,1,45,1,6,6,2,1,1,15),_S5EnBStatRateMismatches_Type())
s5EnBStatRateMismatches.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnBStatRateMismatches.setStatus(_A)
_S5EnBStatBackOffFailures_Type=Counter32
_S5EnBStatBackOffFailures_Object=MibTableColumn
s5EnBStatBackOffFailures=_S5EnBStatBackOffFailures_Object((1,3,6,1,4,1,45,1,6,6,2,1,1,16),_S5EnBStatBackOffFailures_Type())
s5EnBStatBackOffFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnBStatBackOffFailures.setStatus(_A)
_S5EnBStatAutoPartitions_Type=Counter32
_S5EnBStatAutoPartitions_Object=MibTableColumn
s5EnBStatAutoPartitions=_S5EnBStatAutoPartitions_Object((1,3,6,1,4,1,45,1,6,6,2,1,1,17),_S5EnBStatAutoPartitions_Type())
s5EnBStatAutoPartitions.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnBStatAutoPartitions.setStatus(_A)
_S5EnBStatShortIPGs_Type=Counter32
_S5EnBStatShortIPGs_Object=MibTableColumn
s5EnBStatShortIPGs=_S5EnBStatShortIPGs_Object((1,3,6,1,4,1,45,1,6,6,2,1,1,18),_S5EnBStatShortIPGs_Type())
s5EnBStatShortIPGs.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnBStatShortIPGs.setStatus(_A)
_S5EnBStatNullFrames_Type=Counter32
_S5EnBStatNullFrames_Object=MibTableColumn
s5EnBStatNullFrames=_S5EnBStatNullFrames_Object((1,3,6,1,4,1,45,1,6,6,2,1,1,19),_S5EnBStatNullFrames_Type())
s5EnBStatNullFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnBStatNullFrames.setStatus(_A)
_S5EnPStatTable_Object=MibTable
s5EnPStatTable=_S5EnPStatTable_Object((1,3,6,1,4,1,45,1,6,6,2,2))
if mibBuilder.loadTexts:s5EnPStatTable.setStatus(_A)
_S5EnPStatEntry_Object=MibTableRow
s5EnPStatEntry=_S5EnPStatEntry_Object((1,3,6,1,4,1,45,1,6,6,2,2,1))
s5EnPStatEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:s5EnPStatEntry.setStatus(_A)
_S5EnPStatSrcIndx_Type=SrcIndx
_S5EnPStatSrcIndx_Object=MibTableColumn
s5EnPStatSrcIndx=_S5EnPStatSrcIndx_Object((1,3,6,1,4,1,45,1,6,6,2,2,1,1),_S5EnPStatSrcIndx_Type())
s5EnPStatSrcIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnPStatSrcIndx.setStatus(_A)
_S5EnPStatSourceAddrChngs_Type=Counter32
_S5EnPStatSourceAddrChngs_Object=MibTableColumn
s5EnPStatSourceAddrChngs=_S5EnPStatSourceAddrChngs_Object((1,3,6,1,4,1,45,1,6,6,2,2,1,2),_S5EnPStatSourceAddrChngs_Type())
s5EnPStatSourceAddrChngs.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnPStatSourceAddrChngs.setStatus(_A)
_S5EnPStatLinkStatusChngs_Type=Counter32
_S5EnPStatLinkStatusChngs_Object=MibTableColumn
s5EnPStatLinkStatusChngs=_S5EnPStatLinkStatusChngs_Object((1,3,6,1,4,1,45,1,6,6,2,2,1,3),_S5EnPStatLinkStatusChngs_Type())
s5EnPStatLinkStatusChngs.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnPStatLinkStatusChngs.setStatus(_A)
class _S5EnPStatLastSourceAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_S5EnPStatLastSourceAddr_Type.__name__=_E
_S5EnPStatLastSourceAddr_Object=MibTableColumn
s5EnPStatLastSourceAddr=_S5EnPStatLastSourceAddr_Object((1,3,6,1,4,1,45,1,6,6,2,2,1,4),_S5EnPStatLastSourceAddr_Type())
s5EnPStatLastSourceAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnPStatLastSourceAddr.setStatus(_A)
_S5EnSStatTable_Object=MibTable
s5EnSStatTable=_S5EnSStatTable_Object((1,3,6,1,4,1,45,1,6,6,2,3))
if mibBuilder.loadTexts:s5EnSStatTable.setStatus(_A)
_S5EnSStatEntry_Object=MibTableRow
s5EnSStatEntry=_S5EnSStatEntry_Object((1,3,6,1,4,1,45,1,6,6,2,3,1))
s5EnSStatEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:s5EnSStatEntry.setStatus(_A)
_S5EnSStatSrcIndx_Type=SrcIndx
_S5EnSStatSrcIndx_Object=MibTableColumn
s5EnSStatSrcIndx=_S5EnSStatSrcIndx_Object((1,3,6,1,4,1,45,1,6,6,2,3,1,1),_S5EnSStatSrcIndx_Type())
s5EnSStatSrcIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnSStatSrcIndx.setStatus(_A)
_S5EnSStatSegColls_Type=Counter32
_S5EnSStatSegColls_Object=MibTableColumn
s5EnSStatSegColls=_S5EnSStatSegColls_Object((1,3,6,1,4,1,45,1,6,6,2,3,1,2),_S5EnSStatSegColls_Type())
s5EnSStatSegColls.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnSStatSegColls.setStatus(_A)
class _S5EnSStatSegRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('bps10m',2),('bps100m',3)))
_S5EnSStatSegRate_Type.__name__=_C
_S5EnSStatSegRate_Object=MibTableColumn
s5EnSStatSegRate=_S5EnSStatSegRate_Object((1,3,6,1,4,1,45,1,6,6,2,3,1,3),_S5EnSStatSegRate_Type())
s5EnSStatSegRate.setMaxAccess(_B)
if mibBuilder.loadTexts:s5EnSStatSegRate.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'s5EthernetCommonMib':s5EthernetCommonMib,'s5EnPortTable':s5EnPortTable,'s5EnPortEntry':s5EnPortEntry,_I:s5EnPortBrdIndx,_J:s5EnPortIndx,'s5EnPortPartStatus':s5EnPortPartStatus,'s5EnPortPartTime':s5EnPortPartTime,'s5EnPortLinkStatus':s5EnPortLinkStatus,'s5EnPortJabberStatus':s5EnPortJabberStatus,'s5EnPortExtTable':s5EnPortExtTable,'s5EnPortExtEntry':s5EnPortExtEntry,_K:s5EnPortExtBrdIndx,_L:s5EnPortExtIndx,'s5EnPortExtHwCapability':s5EnPortExtHwCapability,'s5EnPortExtAutoNegAdv':s5EnPortExtAutoNegAdv,'s5EnPortExtAutoNegRcvd':s5EnPortExtAutoNegRcvd,'s5EnPortExt10MbSegAttCfg':s5EnPortExt10MbSegAttCfg,'s5EnPortExt100MbSegAttCfg':s5EnPortExt100MbSegAttCfg,'s5EnPortExt10MbSegConnCapability':s5EnPortExt10MbSegConnCapability,'s5EnPortExt100MbSegConnCapability':s5EnPortExt100MbSegConnCapability,'s5EnPortExtActiveSpeed':s5EnPortExtActiveSpeed,'s5EnPortExtCurDuplexMode':s5EnPortExtCurDuplexMode,'s5EnBStatTable':s5EnBStatTable,'s5EnBStatEntry':s5EnBStatEntry,_M:s5EnBStatSrcIndx,'s5EnBStatGoodOctets':s5EnBStatGoodOctets,'s5EnBStatGoodFrms':s5EnBStatGoodFrms,'s5EnBStatBcastFrms':s5EnBStatBcastFrms,'s5EnBStatMcastFrms':s5EnBStatMcastFrms,'s5EnBStatAlignErrors':s5EnBStatAlignErrors,'s5EnBStatFcsErrors':s5EnBStatFcsErrors,'s5EnBStatRunts':s5EnBStatRunts,'s5EnBStatTooLongFrms':s5EnBStatTooLongFrms,'s5EnBStatFragments':s5EnBStatFragments,'s5EnBStatVeryLongEvents':s5EnBStatVeryLongEvents,'s5EnBStatColls':s5EnBStatColls,'s5EnBStatLateColls':s5EnBStatLateColls,'s5EnBStatShortEvents':s5EnBStatShortEvents,'s5EnBStatRateMismatches':s5EnBStatRateMismatches,'s5EnBStatBackOffFailures':s5EnBStatBackOffFailures,'s5EnBStatAutoPartitions':s5EnBStatAutoPartitions,'s5EnBStatShortIPGs':s5EnBStatShortIPGs,'s5EnBStatNullFrames':s5EnBStatNullFrames,'s5EnPStatTable':s5EnPStatTable,'s5EnPStatEntry':s5EnPStatEntry,_N:s5EnPStatSrcIndx,'s5EnPStatSourceAddrChngs':s5EnPStatSourceAddrChngs,'s5EnPStatLinkStatusChngs':s5EnPStatLinkStatusChngs,'s5EnPStatLastSourceAddr':s5EnPStatLastSourceAddr,'s5EnSStatTable':s5EnSStatTable,'s5EnSStatEntry':s5EnSStatEntry,_O:s5EnSStatSrcIndx,'s5EnSStatSegColls':s5EnSStatSegColls,'s5EnSStatSegRate':s5EnSStatSegRate})