_S='ctsmtmibSmtIndex'
_R='unimplemented'
_Q='ctsmtmibAttachmentIndex'
_P='ctsmtmibAttachmentSMTIndex'
_O='ctsmtmibMacIndex'
_N='ctsmtmibMacSmtIndex'
_M='concentrator'
_L='ctsmtmibRingMacAddr'
_K='ctsmtmibRingNodeIndex'
_J='ctsmtmibRingMacIndex'
_I='ctsmtmibRingSmtIndex'
_H='OctetString'
_G='read-write'
_F='false'
_E='true'
_D='CTSMTMIB-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctsmtmib,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctsmtmib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtsmtmibRingTable_Object=MibTable
ctsmtmibRingTable=_CtsmtmibRingTable_Object((1,3,6,1,4,1,52,4,1,2,2,1))
if mibBuilder.loadTexts:ctsmtmibRingTable.setStatus(_A)
_CtsmtmibRingEntry_Object=MibTableRow
ctsmtmibRingEntry=_CtsmtmibRingEntry_Object((1,3,6,1,4,1,52,4,1,2,2,1,1))
ctsmtmibRingEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:ctsmtmibRingEntry.setStatus(_A)
_CtsmtmibRingSmtIndex_Type=Integer32
_CtsmtmibRingSmtIndex_Object=MibTableColumn
ctsmtmibRingSmtIndex=_CtsmtmibRingSmtIndex_Object((1,3,6,1,4,1,52,4,1,2,2,1,1,1),_CtsmtmibRingSmtIndex_Type())
ctsmtmibRingSmtIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibRingSmtIndex.setStatus(_A)
_CtsmtmibRingMacIndex_Type=Integer32
_CtsmtmibRingMacIndex_Object=MibTableColumn
ctsmtmibRingMacIndex=_CtsmtmibRingMacIndex_Object((1,3,6,1,4,1,52,4,1,2,2,1,1,2),_CtsmtmibRingMacIndex_Type())
ctsmtmibRingMacIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibRingMacIndex.setStatus(_A)
_CtsmtmibRingNodeIndex_Type=Integer32
_CtsmtmibRingNodeIndex_Object=MibTableColumn
ctsmtmibRingNodeIndex=_CtsmtmibRingNodeIndex_Object((1,3,6,1,4,1,52,4,1,2,2,1,1,3),_CtsmtmibRingNodeIndex_Type())
ctsmtmibRingNodeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibRingNodeIndex.setStatus(_A)
_CtsmtmibRingMacAddr_Type=OctetString
_CtsmtmibRingMacAddr_Object=MibTableColumn
ctsmtmibRingMacAddr=_CtsmtmibRingMacAddr_Object((1,3,6,1,4,1,52,4,1,2,2,1,1,4),_CtsmtmibRingMacAddr_Type())
ctsmtmibRingMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibRingMacAddr.setStatus(_A)
class _CtsmtmibRingUpStreamAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_CtsmtmibRingUpStreamAddr_Type.__name__=_H
_CtsmtmibRingUpStreamAddr_Object=MibTableColumn
ctsmtmibRingUpStreamAddr=_CtsmtmibRingUpStreamAddr_Object((1,3,6,1,4,1,52,4,1,2,2,1,1,5),_CtsmtmibRingUpStreamAddr_Type())
ctsmtmibRingUpStreamAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibRingUpStreamAddr.setStatus(_A)
class _CtsmtmibRingNodeClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('station',1),(_M,2)))
_CtsmtmibRingNodeClass_Type.__name__=_C
_CtsmtmibRingNodeClass_Object=MibTableColumn
ctsmtmibRingNodeClass=_CtsmtmibRingNodeClass_Object((1,3,6,1,4,1,52,4,1,2,2,1,1,6),_CtsmtmibRingNodeClass_Type())
ctsmtmibRingNodeClass.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibRingNodeClass.setStatus(_A)
_CtsmtmibRingMacCount_Type=Integer32
_CtsmtmibRingMacCount_Object=MibTableColumn
ctsmtmibRingMacCount=_CtsmtmibRingMacCount_Object((1,3,6,1,4,1,52,4,1,2,2,1,1,7),_CtsmtmibRingMacCount_Type())
ctsmtmibRingMacCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibRingMacCount.setStatus(_A)
_CtsmtmibRingNonMasterCount_Type=Integer32
_CtsmtmibRingNonMasterCount_Object=MibTableColumn
ctsmtmibRingNonMasterCount=_CtsmtmibRingNonMasterCount_Object((1,3,6,1,4,1,52,4,1,2,2,1,1,8),_CtsmtmibRingNonMasterCount_Type())
ctsmtmibRingNonMasterCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibRingNonMasterCount.setStatus(_A)
class _CtsmtmibRingMasterCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CtsmtmibRingMasterCount_Type.__name__=_C
_CtsmtmibRingMasterCount_Object=MibTableColumn
ctsmtmibRingMasterCount=_CtsmtmibRingMasterCount_Object((1,3,6,1,4,1,52,4,1,2,2,1,1,9),_CtsmtmibRingMasterCount_Type())
ctsmtmibRingMasterCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibRingMasterCount.setStatus(_A)
_CtsmtmibRingTopology_Type=Integer32
_CtsmtmibRingTopology_Object=MibTableColumn
ctsmtmibRingTopology=_CtsmtmibRingTopology_Object((1,3,6,1,4,1,52,4,1,2,2,1,1,10),_CtsmtmibRingTopology_Type())
ctsmtmibRingTopology.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibRingTopology.setStatus(_A)
class _CtsmtmibRingDuplicate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_CtsmtmibRingDuplicate_Type.__name__=_C
_CtsmtmibRingDuplicate_Object=MibTableColumn
ctsmtmibRingDuplicate=_CtsmtmibRingDuplicate_Object((1,3,6,1,4,1,52,4,1,2,2,1,1,11),_CtsmtmibRingDuplicate_Type())
ctsmtmibRingDuplicate.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibRingDuplicate.setStatus(_A)
_CtsmtmibMacTable_Object=MibTable
ctsmtmibMacTable=_CtsmtmibMacTable_Object((1,3,6,1,4,1,52,4,1,2,2,2))
if mibBuilder.loadTexts:ctsmtmibMacTable.setStatus(_A)
_CtsmtmibMacEntry_Object=MibTableRow
ctsmtmibMacEntry=_CtsmtmibMacEntry_Object((1,3,6,1,4,1,52,4,1,2,2,2,1))
ctsmtmibMacEntry.setIndexNames((0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:ctsmtmibMacEntry.setStatus(_A)
_CtsmtmibMacSmtIndex_Type=Integer32
_CtsmtmibMacSmtIndex_Object=MibTableColumn
ctsmtmibMacSmtIndex=_CtsmtmibMacSmtIndex_Object((1,3,6,1,4,1,52,4,1,2,2,2,1,1),_CtsmtmibMacSmtIndex_Type())
ctsmtmibMacSmtIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibMacSmtIndex.setStatus(_A)
_CtsmtmibMacIndex_Type=Integer32
_CtsmtmibMacIndex_Object=MibTableColumn
ctsmtmibMacIndex=_CtsmtmibMacIndex_Object((1,3,6,1,4,1,52,4,1,2,2,2,1,2),_CtsmtmibMacIndex_Type())
ctsmtmibMacIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibMacIndex.setStatus(_A)
_CtsmtmibMacNifTxCts_Type=Counter32
_CtsmtmibMacNifTxCts_Object=MibTableColumn
ctsmtmibMacNifTxCts=_CtsmtmibMacNifTxCts_Object((1,3,6,1,4,1,52,4,1,2,2,2,1,3),_CtsmtmibMacNifTxCts_Type())
ctsmtmibMacNifTxCts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibMacNifTxCts.setStatus(_A)
_CtsmtmibMacNifRxCts_Type=Counter32
_CtsmtmibMacNifRxCts_Object=MibTableColumn
ctsmtmibMacNifRxCts=_CtsmtmibMacNifRxCts_Object((1,3,6,1,4,1,52,4,1,2,2,2,1,4),_CtsmtmibMacNifRxCts_Type())
ctsmtmibMacNifRxCts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibMacNifRxCts.setStatus(_A)
_CtsmtmibMacSifTxCts_Type=Counter32
_CtsmtmibMacSifTxCts_Object=MibTableColumn
ctsmtmibMacSifTxCts=_CtsmtmibMacSifTxCts_Object((1,3,6,1,4,1,52,4,1,2,2,2,1,5),_CtsmtmibMacSifTxCts_Type())
ctsmtmibMacSifTxCts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibMacSifTxCts.setStatus(_A)
_CtsmtmibMacSifRxCts_Type=Counter32
_CtsmtmibMacSifRxCts_Object=MibTableColumn
ctsmtmibMacSifRxCts=_CtsmtmibMacSifRxCts_Object((1,3,6,1,4,1,52,4,1,2,2,2,1,6),_CtsmtmibMacSifRxCts_Type())
ctsmtmibMacSifRxCts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibMacSifRxCts.setStatus(_A)
_CtsmtmibMacEcfTxCts_Type=Counter32
_CtsmtmibMacEcfTxCts_Object=MibTableColumn
ctsmtmibMacEcfTxCts=_CtsmtmibMacEcfTxCts_Object((1,3,6,1,4,1,52,4,1,2,2,2,1,7),_CtsmtmibMacEcfTxCts_Type())
ctsmtmibMacEcfTxCts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibMacEcfTxCts.setStatus(_A)
_CtsmtmibMacEcfRxCts_Type=Counter32
_CtsmtmibMacEcfRxCts_Object=MibTableColumn
ctsmtmibMacEcfRxCts=_CtsmtmibMacEcfRxCts_Object((1,3,6,1,4,1,52,4,1,2,2,2,1,8),_CtsmtmibMacEcfRxCts_Type())
ctsmtmibMacEcfRxCts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibMacEcfRxCts.setStatus(_A)
_CtsmtmibMacPmfTxCts_Type=Counter32
_CtsmtmibMacPmfTxCts_Object=MibTableColumn
ctsmtmibMacPmfTxCts=_CtsmtmibMacPmfTxCts_Object((1,3,6,1,4,1,52,4,1,2,2,2,1,9),_CtsmtmibMacPmfTxCts_Type())
ctsmtmibMacPmfTxCts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibMacPmfTxCts.setStatus(_A)
_CtsmtmibMacPmfRxCts_Type=Counter32
_CtsmtmibMacPmfRxCts_Object=MibTableColumn
ctsmtmibMacPmfRxCts=_CtsmtmibMacPmfRxCts_Object((1,3,6,1,4,1,52,4,1,2,2,2,1,10),_CtsmtmibMacPmfRxCts_Type())
ctsmtmibMacPmfRxCts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibMacPmfRxCts.setStatus(_A)
_CtsmtmibMacRdfTxCts_Type=Counter32
_CtsmtmibMacRdfTxCts_Object=MibTableColumn
ctsmtmibMacRdfTxCts=_CtsmtmibMacRdfTxCts_Object((1,3,6,1,4,1,52,4,1,2,2,2,1,11),_CtsmtmibMacRdfTxCts_Type())
ctsmtmibMacRdfTxCts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibMacRdfTxCts.setStatus(_A)
_CtsmtmibMacRdfRxCts_Type=Counter32
_CtsmtmibMacRdfRxCts_Object=MibTableColumn
ctsmtmibMacRdfRxCts=_CtsmtmibMacRdfRxCts_Object((1,3,6,1,4,1,52,4,1,2,2,2,1,12),_CtsmtmibMacRdfRxCts_Type())
ctsmtmibMacRdfRxCts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibMacRdfRxCts.setStatus(_A)
_CtsmtmibMacRingOpCts_Type=Counter32
_CtsmtmibMacRingOpCts_Object=MibTableColumn
ctsmtmibMacRingOpCts=_CtsmtmibMacRingOpCts_Object((1,3,6,1,4,1,52,4,1,2,2,2,1,13),_CtsmtmibMacRingOpCts_Type())
ctsmtmibMacRingOpCts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibMacRingOpCts.setStatus(_A)
_CtsmtmibMacTxCts_Type=Counter32
_CtsmtmibMacTxCts_Object=MibTableColumn
ctsmtmibMacTxCts=_CtsmtmibMacTxCts_Object((1,3,6,1,4,1,52,4,1,2,2,2,1,14),_CtsmtmibMacTxCts_Type())
ctsmtmibMacTxCts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibMacTxCts.setStatus(_A)
_CtsmtmibMacRingMapUpdateCts_Type=Counter32
_CtsmtmibMacRingMapUpdateCts_Object=MibTableColumn
ctsmtmibMacRingMapUpdateCts=_CtsmtmibMacRingMapUpdateCts_Object((1,3,6,1,4,1,52,4,1,2,2,2,1,15),_CtsmtmibMacRingMapUpdateCts_Type())
ctsmtmibMacRingMapUpdateCts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibMacRingMapUpdateCts.setStatus(_A)
class _CtsmtmibMacAutoNegotiation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_CtsmtmibMacAutoNegotiation_Type.__name__=_C
_CtsmtmibMacAutoNegotiation_Object=MibTableColumn
ctsmtmibMacAutoNegotiation=_CtsmtmibMacAutoNegotiation_Object((1,3,6,1,4,1,52,4,1,2,2,2,1,16),_CtsmtmibMacAutoNegotiation_Type())
ctsmtmibMacAutoNegotiation.setMaxAccess(_G)
if mibBuilder.loadTexts:ctsmtmibMacAutoNegotiation.setStatus(_A)
class _CtsmtmibAttachmentNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CtsmtmibAttachmentNumber_Type.__name__=_C
_CtsmtmibAttachmentNumber_Object=MibScalar
ctsmtmibAttachmentNumber=_CtsmtmibAttachmentNumber_Object((1,3,6,1,4,1,52,4,1,2,2,3),_CtsmtmibAttachmentNumber_Type())
ctsmtmibAttachmentNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibAttachmentNumber.setStatus(_A)
_CtsmtmibAttachmentTable_Object=MibTable
ctsmtmibAttachmentTable=_CtsmtmibAttachmentTable_Object((1,3,6,1,4,1,52,4,1,2,2,4))
if mibBuilder.loadTexts:ctsmtmibAttachmentTable.setStatus(_A)
_CtsmtmibAttachmentEntry_Object=MibTableRow
ctsmtmibAttachmentEntry=_CtsmtmibAttachmentEntry_Object((1,3,6,1,4,1,52,4,1,2,2,4,1))
ctsmtmibAttachmentEntry.setIndexNames((0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:ctsmtmibAttachmentEntry.setStatus(_A)
class _CtsmtmibAttachmentSMTIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtsmtmibAttachmentSMTIndex_Type.__name__=_C
_CtsmtmibAttachmentSMTIndex_Object=MibTableColumn
ctsmtmibAttachmentSMTIndex=_CtsmtmibAttachmentSMTIndex_Object((1,3,6,1,4,1,52,4,1,2,2,4,1,1),_CtsmtmibAttachmentSMTIndex_Type())
ctsmtmibAttachmentSMTIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibAttachmentSMTIndex.setStatus(_A)
class _CtsmtmibAttachmentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtsmtmibAttachmentIndex_Type.__name__=_C
_CtsmtmibAttachmentIndex_Object=MibTableColumn
ctsmtmibAttachmentIndex=_CtsmtmibAttachmentIndex_Object((1,3,6,1,4,1,52,4,1,2,2,4,1,2),_CtsmtmibAttachmentIndex_Type())
ctsmtmibAttachmentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibAttachmentIndex.setStatus(_A)
class _CtsmtmibAttachmentClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('single-attachment',1),('dual-attachment',2),(_M,3)))
_CtsmtmibAttachmentClass_Type.__name__=_C
_CtsmtmibAttachmentClass_Object=MibTableColumn
ctsmtmibAttachmentClass=_CtsmtmibAttachmentClass_Object((1,3,6,1,4,1,52,4,1,2,2,4,1,3),_CtsmtmibAttachmentClass_Type())
ctsmtmibAttachmentClass.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibAttachmentClass.setStatus(_A)
class _CtsmtmibAttachmentOpticalBypassPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_CtsmtmibAttachmentOpticalBypassPresent_Type.__name__=_C
_CtsmtmibAttachmentOpticalBypassPresent_Object=MibTableColumn
ctsmtmibAttachmentOpticalBypassPresent=_CtsmtmibAttachmentOpticalBypassPresent_Object((1,3,6,1,4,1,52,4,1,2,2,4,1,4),_CtsmtmibAttachmentOpticalBypassPresent_Type())
ctsmtmibAttachmentOpticalBypassPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibAttachmentOpticalBypassPresent.setStatus(_A)
class _CtsmtmibAttachmentIMaxExpiration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CtsmtmibAttachmentIMaxExpiration_Type.__name__=_C
_CtsmtmibAttachmentIMaxExpiration_Object=MibTableColumn
ctsmtmibAttachmentIMaxExpiration=_CtsmtmibAttachmentIMaxExpiration_Object((1,3,6,1,4,1,52,4,1,2,2,4,1,5),_CtsmtmibAttachmentIMaxExpiration_Type())
ctsmtmibAttachmentIMaxExpiration.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibAttachmentIMaxExpiration.setStatus(_A)
class _CtsmtmibAttachmentInsertedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_R,3)))
_CtsmtmibAttachmentInsertedStatus_Type.__name__=_C
_CtsmtmibAttachmentInsertedStatus_Object=MibTableColumn
ctsmtmibAttachmentInsertedStatus=_CtsmtmibAttachmentInsertedStatus_Object((1,3,6,1,4,1,52,4,1,2,2,4,1,6),_CtsmtmibAttachmentInsertedStatus_Type())
ctsmtmibAttachmentInsertedStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibAttachmentInsertedStatus.setStatus(_A)
class _CtsmtmibAttachmentInsertPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_R,3)))
_CtsmtmibAttachmentInsertPolicy_Type.__name__=_C
_CtsmtmibAttachmentInsertPolicy_Object=MibTableColumn
ctsmtmibAttachmentInsertPolicy=_CtsmtmibAttachmentInsertPolicy_Object((1,3,6,1,4,1,52,4,1,2,2,4,1,7),_CtsmtmibAttachmentInsertPolicy_Type())
ctsmtmibAttachmentInsertPolicy.setMaxAccess(_G)
if mibBuilder.loadTexts:ctsmtmibAttachmentInsertPolicy.setStatus(_A)
_CtsmtmibSMTTable_Object=MibTable
ctsmtmibSMTTable=_CtsmtmibSMTTable_Object((1,3,6,1,4,1,52,4,1,2,2,5))
if mibBuilder.loadTexts:ctsmtmibSMTTable.setStatus(_A)
_CtsmtmibSMTEntry_Object=MibTableRow
ctsmtmibSMTEntry=_CtsmtmibSMTEntry_Object((1,3,6,1,4,1,52,4,1,2,2,5,1))
ctsmtmibSMTEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:ctsmtmibSMTEntry.setStatus(_A)
class _CtsmtmibSMTDualHomeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notDualHomed',1),('linkAorB',2),('linkAandB',3)))
_CtsmtmibSMTDualHomeStatus_Type.__name__=_C
_CtsmtmibSMTDualHomeStatus_Object=MibTableColumn
ctsmtmibSMTDualHomeStatus=_CtsmtmibSMTDualHomeStatus_Object((1,3,6,1,4,1,52,4,1,2,2,5,1,1),_CtsmtmibSMTDualHomeStatus_Type())
ctsmtmibSMTDualHomeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibSMTDualHomeStatus.setStatus(_A)
class _CtsmtmibSMTDualHomeWrpLEDStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_CtsmtmibSMTDualHomeWrpLEDStatus_Type.__name__=_C
_CtsmtmibSMTDualHomeWrpLEDStatus_Object=MibTableColumn
ctsmtmibSMTDualHomeWrpLEDStatus=_CtsmtmibSMTDualHomeWrpLEDStatus_Object((1,3,6,1,4,1,52,4,1,2,2,5,1,2),_CtsmtmibSMTDualHomeWrpLEDStatus_Type())
ctsmtmibSMTDualHomeWrpLEDStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ctsmtmibSMTDualHomeWrpLEDStatus.setStatus(_A)
_CtsmtmibSmtIndex_Type=Integer32
_CtsmtmibSmtIndex_Object=MibTableColumn
ctsmtmibSmtIndex=_CtsmtmibSmtIndex_Object((1,3,6,1,4,1,52,4,1,2,2,5,1,3),_CtsmtmibSmtIndex_Type())
ctsmtmibSmtIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctsmtmibSmtIndex.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ctsmtmibRingTable':ctsmtmibRingTable,'ctsmtmibRingEntry':ctsmtmibRingEntry,_I:ctsmtmibRingSmtIndex,_J:ctsmtmibRingMacIndex,_K:ctsmtmibRingNodeIndex,_L:ctsmtmibRingMacAddr,'ctsmtmibRingUpStreamAddr':ctsmtmibRingUpStreamAddr,'ctsmtmibRingNodeClass':ctsmtmibRingNodeClass,'ctsmtmibRingMacCount':ctsmtmibRingMacCount,'ctsmtmibRingNonMasterCount':ctsmtmibRingNonMasterCount,'ctsmtmibRingMasterCount':ctsmtmibRingMasterCount,'ctsmtmibRingTopology':ctsmtmibRingTopology,'ctsmtmibRingDuplicate':ctsmtmibRingDuplicate,'ctsmtmibMacTable':ctsmtmibMacTable,'ctsmtmibMacEntry':ctsmtmibMacEntry,_N:ctsmtmibMacSmtIndex,_O:ctsmtmibMacIndex,'ctsmtmibMacNifTxCts':ctsmtmibMacNifTxCts,'ctsmtmibMacNifRxCts':ctsmtmibMacNifRxCts,'ctsmtmibMacSifTxCts':ctsmtmibMacSifTxCts,'ctsmtmibMacSifRxCts':ctsmtmibMacSifRxCts,'ctsmtmibMacEcfTxCts':ctsmtmibMacEcfTxCts,'ctsmtmibMacEcfRxCts':ctsmtmibMacEcfRxCts,'ctsmtmibMacPmfTxCts':ctsmtmibMacPmfTxCts,'ctsmtmibMacPmfRxCts':ctsmtmibMacPmfRxCts,'ctsmtmibMacRdfTxCts':ctsmtmibMacRdfTxCts,'ctsmtmibMacRdfRxCts':ctsmtmibMacRdfRxCts,'ctsmtmibMacRingOpCts':ctsmtmibMacRingOpCts,'ctsmtmibMacTxCts':ctsmtmibMacTxCts,'ctsmtmibMacRingMapUpdateCts':ctsmtmibMacRingMapUpdateCts,'ctsmtmibMacAutoNegotiation':ctsmtmibMacAutoNegotiation,'ctsmtmibAttachmentNumber':ctsmtmibAttachmentNumber,'ctsmtmibAttachmentTable':ctsmtmibAttachmentTable,'ctsmtmibAttachmentEntry':ctsmtmibAttachmentEntry,_P:ctsmtmibAttachmentSMTIndex,_Q:ctsmtmibAttachmentIndex,'ctsmtmibAttachmentClass':ctsmtmibAttachmentClass,'ctsmtmibAttachmentOpticalBypassPresent':ctsmtmibAttachmentOpticalBypassPresent,'ctsmtmibAttachmentIMaxExpiration':ctsmtmibAttachmentIMaxExpiration,'ctsmtmibAttachmentInsertedStatus':ctsmtmibAttachmentInsertedStatus,'ctsmtmibAttachmentInsertPolicy':ctsmtmibAttachmentInsertPolicy,'ctsmtmibSMTTable':ctsmtmibSMTTable,'ctsmtmibSMTEntry':ctsmtmibSMTEntry,'ctsmtmibSMTDualHomeStatus':ctsmtmibSMTDualHomeStatus,'ctsmtmibSMTDualHomeWrpLEDStatus':ctsmtmibSMTDualHomeWrpLEDStatus,_S:ctsmtmibSmtIndex})