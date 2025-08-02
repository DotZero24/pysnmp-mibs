_O='sfpsCallByTupleHashIndex'
_N='sfpsCallByTupleDstHash'
_M='sfpsCallByTupleSrcHash'
_L='sfpsCallByTupleInPort'
_K='sfpsSapTableHashIndex'
_J='sfpsSapTableHash'
_I='sfpsSapTableTag'
_H='read-write'
_G='other'
_F='enable'
_E='disable'
_D='CTRON-SFPS-CALL-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sfpsCallByTuple,sfpsCallTableStats,sfpsSap,sfpsSapAPI=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','sfpsCallByTuple','sfpsCallTableStats','sfpsSap','sfpsSapAPI')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class HexInteger(Integer32):0
_SfpsSapTable_Object=MibTable
sfpsSapTable=_SfpsSapTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,1))
if mibBuilder.loadTexts:sfpsSapTable.setStatus(_A)
_SfpsSapTableEntry_Object=MibTableRow
sfpsSapTableEntry=_SfpsSapTableEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,1,1))
sfpsSapTableEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:sfpsSapTableEntry.setStatus(_A)
_SfpsSapTableTag_Type=Integer32
_SfpsSapTableTag_Object=MibTableColumn
sfpsSapTableTag=_SfpsSapTableTag_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,1,1,1),_SfpsSapTableTag_Type())
sfpsSapTableTag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSapTableTag.setStatus(_A)
_SfpsSapTableHash_Type=Integer32
_SfpsSapTableHash_Object=MibTableColumn
sfpsSapTableHash=_SfpsSapTableHash_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,1,1,2),_SfpsSapTableHash_Type())
sfpsSapTableHash.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSapTableHash.setStatus(_A)
_SfpsSapTableHashIndex_Type=Integer32
_SfpsSapTableHashIndex_Object=MibTableColumn
sfpsSapTableHashIndex=_SfpsSapTableHashIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,1,1,3),_SfpsSapTableHashIndex_Type())
sfpsSapTableHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSapTableHashIndex.setStatus(_A)
_SfpsSapTableSourceCP_Type=DisplayString
_SfpsSapTableSourceCP_Object=MibTableColumn
sfpsSapTableSourceCP=_SfpsSapTableSourceCP_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,1,1,4),_SfpsSapTableSourceCP_Type())
sfpsSapTableSourceCP.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSapTableSourceCP.setStatus(_A)
_SfpsSapTableDestCP_Type=DisplayString
_SfpsSapTableDestCP_Object=MibTableColumn
sfpsSapTableDestCP=_SfpsSapTableDestCP_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,1,1,5),_SfpsSapTableDestCP_Type())
sfpsSapTableDestCP.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSapTableDestCP.setStatus(_A)
_SfpsSapTableSAP_Type=DisplayString
_SfpsSapTableSAP_Object=MibTableColumn
sfpsSapTableSAP=_SfpsSapTableSAP_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,1,1,6),_SfpsSapTableSAP_Type())
sfpsSapTableSAP.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSapTableSAP.setStatus(_A)
class _SfpsSapTableOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_E,2),(_F,3)))
_SfpsSapTableOperStatus_Type.__name__=_C
_SfpsSapTableOperStatus_Object=MibTableColumn
sfpsSapTableOperStatus=_SfpsSapTableOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,1,1,7),_SfpsSapTableOperStatus_Type())
sfpsSapTableOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSapTableOperStatus.setStatus(_A)
class _SfpsSapTableAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_E,2),(_F,3)))
_SfpsSapTableAdminStatus_Type.__name__=_C
_SfpsSapTableAdminStatus_Object=MibTableColumn
sfpsSapTableAdminStatus=_SfpsSapTableAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,1,1,8),_SfpsSapTableAdminStatus_Type())
sfpsSapTableAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSapTableAdminStatus.setStatus(_A)
_SfpsSapTableStateTime_Type=TimeTicks
_SfpsSapTableStateTime_Object=MibTableColumn
sfpsSapTableStateTime=_SfpsSapTableStateTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,1,1,9),_SfpsSapTableStateTime_Type())
sfpsSapTableStateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSapTableStateTime.setStatus(_A)
_SfpsSapTableDescription_Type=DisplayString
_SfpsSapTableDescription_Object=MibTableColumn
sfpsSapTableDescription=_SfpsSapTableDescription_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,1,1,10),_SfpsSapTableDescription_Type())
sfpsSapTableDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSapTableDescription.setStatus(_A)
_SfpsSapTableNumAccepted_Type=Integer32
_SfpsSapTableNumAccepted_Object=MibTableColumn
sfpsSapTableNumAccepted=_SfpsSapTableNumAccepted_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,1,1,11),_SfpsSapTableNumAccepted_Type())
sfpsSapTableNumAccepted.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSapTableNumAccepted.setStatus(_A)
_SfpsSapTableNumDropped_Type=Integer32
_SfpsSapTableNumDropped_Object=MibTableColumn
sfpsSapTableNumDropped=_SfpsSapTableNumDropped_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,1,1,12),_SfpsSapTableNumDropped_Type())
sfpsSapTableNumDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSapTableNumDropped.setStatus(_A)
_SfpsSapTableUnicastSap_Type=Integer32
_SfpsSapTableUnicastSap_Object=MibTableColumn
sfpsSapTableUnicastSap=_SfpsSapTableUnicastSap_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,1,1,13),_SfpsSapTableUnicastSap_Type())
sfpsSapTableUnicastSap.setMaxAccess(_H)
if mibBuilder.loadTexts:sfpsSapTableUnicastSap.setStatus(_A)
class _SfpsSapTableNVStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_E,2),(_F,3),('unset',4)))
_SfpsSapTableNVStatus_Type.__name__=_C
_SfpsSapTableNVStatus_Object=MibTableColumn
sfpsSapTableNVStatus=_SfpsSapTableNVStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,1,1,14),_SfpsSapTableNVStatus_Type())
sfpsSapTableNVStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSapTableNVStatus.setStatus(_A)
class _SfpsSapAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('getStatus',1),('next',2),('first',3),(_E,4),('disableInNvram',5),(_F,6),('enableInNvram',7),('clearFromNvram',8),('clearAllNvram',9),('resetStats',10),('resetAllStats',11)))
_SfpsSapAPIVerb_Type.__name__=_C
_SfpsSapAPIVerb_Object=MibScalar
sfpsSapAPIVerb=_SfpsSapAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,2,1),_SfpsSapAPIVerb_Type())
sfpsSapAPIVerb.setMaxAccess(_H)
if mibBuilder.loadTexts:sfpsSapAPIVerb.setStatus(_A)
_SfpsSapAPISourceCP_Type=DisplayString
_SfpsSapAPISourceCP_Object=MibScalar
sfpsSapAPISourceCP=_SfpsSapAPISourceCP_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,2,2),_SfpsSapAPISourceCP_Type())
sfpsSapAPISourceCP.setMaxAccess(_H)
if mibBuilder.loadTexts:sfpsSapAPISourceCP.setStatus(_A)
_SfpsSapAPIDestCP_Type=DisplayString
_SfpsSapAPIDestCP_Object=MibScalar
sfpsSapAPIDestCP=_SfpsSapAPIDestCP_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,2,3),_SfpsSapAPIDestCP_Type())
sfpsSapAPIDestCP.setMaxAccess(_H)
if mibBuilder.loadTexts:sfpsSapAPIDestCP.setStatus(_A)
_SfpsSapAPISAP_Type=DisplayString
_SfpsSapAPISAP_Object=MibScalar
sfpsSapAPISAP=_SfpsSapAPISAP_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,2,4),_SfpsSapAPISAP_Type())
sfpsSapAPISAP.setMaxAccess(_H)
if mibBuilder.loadTexts:sfpsSapAPISAP.setStatus(_A)
class _SfpsSapAPINVStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_E,2),(_F,3),('unset',4)))
_SfpsSapAPINVStatus_Type.__name__=_C
_SfpsSapAPINVStatus_Object=MibScalar
sfpsSapAPINVStatus=_SfpsSapAPINVStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,2,5),_SfpsSapAPINVStatus_Type())
sfpsSapAPINVStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSapAPINVStatus.setStatus(_A)
class _SfpsSapAPIAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_E,2),(_F,3)))
_SfpsSapAPIAdminStatus_Type.__name__=_C
_SfpsSapAPIAdminStatus_Object=MibScalar
sfpsSapAPIAdminStatus=_SfpsSapAPIAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,2,6),_SfpsSapAPIAdminStatus_Type())
sfpsSapAPIAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSapAPIAdminStatus.setStatus(_A)
class _SfpsSapAPIOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_E,2),(_F,3)))
_SfpsSapAPIOperStatus_Type.__name__=_C
_SfpsSapAPIOperStatus_Object=MibScalar
sfpsSapAPIOperStatus=_SfpsSapAPIOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,2,7),_SfpsSapAPIOperStatus_Type())
sfpsSapAPIOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSapAPIOperStatus.setStatus(_A)
_SfpsSapAPINvSet_Type=Integer32
_SfpsSapAPINvSet_Object=MibScalar
sfpsSapAPINvSet=_SfpsSapAPINvSet_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,2,8),_SfpsSapAPINvSet_Type())
sfpsSapAPINvSet.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSapAPINvSet.setStatus(_A)
_SfpsSapAPINVTotal_Type=Integer32
_SfpsSapAPINVTotal_Object=MibScalar
sfpsSapAPINVTotal=_SfpsSapAPINVTotal_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,2,9),_SfpsSapAPINVTotal_Type())
sfpsSapAPINVTotal.setMaxAccess(_H)
if mibBuilder.loadTexts:sfpsSapAPINVTotal.setStatus(_A)
_SfpsSapAPINumAccept_Type=Integer32
_SfpsSapAPINumAccept_Object=MibScalar
sfpsSapAPINumAccept=_SfpsSapAPINumAccept_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,2,10),_SfpsSapAPINumAccept_Type())
sfpsSapAPINumAccept.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSapAPINumAccept.setStatus(_A)
_SfpsSapAPINvDiscard_Type=Integer32
_SfpsSapAPINvDiscard_Object=MibScalar
sfpsSapAPINvDiscard=_SfpsSapAPINvDiscard_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,2,11),_SfpsSapAPINvDiscard_Type())
sfpsSapAPINvDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSapAPINvDiscard.setStatus(_A)
class _SfpsSapAPIDefaultStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_E,2),(_F,3)))
_SfpsSapAPIDefaultStatus_Type.__name__=_C
_SfpsSapAPIDefaultStatus_Object=MibScalar
sfpsSapAPIDefaultStatus=_SfpsSapAPIDefaultStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,2,2,12),_SfpsSapAPIDefaultStatus_Type())
sfpsSapAPIDefaultStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSapAPIDefaultStatus.setStatus(_A)
_SfpsCallByTupleTable_Object=MibTable
sfpsCallByTupleTable=_SfpsCallByTupleTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,5,1))
if mibBuilder.loadTexts:sfpsCallByTupleTable.setStatus(_A)
_SfpsCallByTupleEntry_Object=MibTableRow
sfpsCallByTupleEntry=_SfpsCallByTupleEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,5,1,1))
sfpsCallByTupleEntry.setIndexNames((0,_D,_L),(0,_D,_M),(0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:sfpsCallByTupleEntry.setStatus(_A)
_SfpsCallByTupleInPort_Type=Integer32
_SfpsCallByTupleInPort_Object=MibTableColumn
sfpsCallByTupleInPort=_SfpsCallByTupleInPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,5,1,1,1),_SfpsCallByTupleInPort_Type())
sfpsCallByTupleInPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallByTupleInPort.setStatus(_A)
_SfpsCallByTupleSrcHash_Type=Integer32
_SfpsCallByTupleSrcHash_Object=MibTableColumn
sfpsCallByTupleSrcHash=_SfpsCallByTupleSrcHash_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,5,1,1,2),_SfpsCallByTupleSrcHash_Type())
sfpsCallByTupleSrcHash.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallByTupleSrcHash.setStatus(_A)
_SfpsCallByTupleDstHash_Type=Integer32
_SfpsCallByTupleDstHash_Object=MibTableColumn
sfpsCallByTupleDstHash=_SfpsCallByTupleDstHash_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,5,1,1,3),_SfpsCallByTupleDstHash_Type())
sfpsCallByTupleDstHash.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallByTupleDstHash.setStatus(_A)
_SfpsCallByTupleHashIndex_Type=Integer32
_SfpsCallByTupleHashIndex_Object=MibTableColumn
sfpsCallByTupleHashIndex=_SfpsCallByTupleHashIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,5,1,1,4),_SfpsCallByTupleHashIndex_Type())
sfpsCallByTupleHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallByTupleHashIndex.setStatus(_A)
_SfpsCallByTupleBotSrcType_Type=DisplayString
_SfpsCallByTupleBotSrcType_Object=MibTableColumn
sfpsCallByTupleBotSrcType=_SfpsCallByTupleBotSrcType_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,5,1,1,5),_SfpsCallByTupleBotSrcType_Type())
sfpsCallByTupleBotSrcType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallByTupleBotSrcType.setStatus(_A)
_SfpsCallByTupleBotSrcAddress_Type=DisplayString
_SfpsCallByTupleBotSrcAddress_Object=MibTableColumn
sfpsCallByTupleBotSrcAddress=_SfpsCallByTupleBotSrcAddress_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,5,1,1,6),_SfpsCallByTupleBotSrcAddress_Type())
sfpsCallByTupleBotSrcAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallByTupleBotSrcAddress.setStatus(_A)
_SfpsCallByTupleBotDstType_Type=DisplayString
_SfpsCallByTupleBotDstType_Object=MibTableColumn
sfpsCallByTupleBotDstType=_SfpsCallByTupleBotDstType_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,5,1,1,7),_SfpsCallByTupleBotDstType_Type())
sfpsCallByTupleBotDstType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallByTupleBotDstType.setStatus(_A)
_SfpsCallByTupleBotDstAddress_Type=DisplayString
_SfpsCallByTupleBotDstAddress_Object=MibTableColumn
sfpsCallByTupleBotDstAddress=_SfpsCallByTupleBotDstAddress_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,5,1,1,8),_SfpsCallByTupleBotDstAddress_Type())
sfpsCallByTupleBotDstAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallByTupleBotDstAddress.setStatus(_A)
_SfpsCallByTupleTopSrcType_Type=DisplayString
_SfpsCallByTupleTopSrcType_Object=MibTableColumn
sfpsCallByTupleTopSrcType=_SfpsCallByTupleTopSrcType_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,5,1,1,9),_SfpsCallByTupleTopSrcType_Type())
sfpsCallByTupleTopSrcType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallByTupleTopSrcType.setStatus(_A)
_SfpsCallByTupleTopSrcAddress_Type=DisplayString
_SfpsCallByTupleTopSrcAddress_Object=MibTableColumn
sfpsCallByTupleTopSrcAddress=_SfpsCallByTupleTopSrcAddress_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,5,1,1,10),_SfpsCallByTupleTopSrcAddress_Type())
sfpsCallByTupleTopSrcAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallByTupleTopSrcAddress.setStatus(_A)
_SfpsCallByTupleTopDstType_Type=DisplayString
_SfpsCallByTupleTopDstType_Object=MibTableColumn
sfpsCallByTupleTopDstType=_SfpsCallByTupleTopDstType_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,5,1,1,11),_SfpsCallByTupleTopDstType_Type())
sfpsCallByTupleTopDstType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallByTupleTopDstType.setStatus(_A)
_SfpsCallByTupleTopDstAddress_Type=DisplayString
_SfpsCallByTupleTopDstAddress_Object=MibTableColumn
sfpsCallByTupleTopDstAddress=_SfpsCallByTupleTopDstAddress_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,5,1,1,12),_SfpsCallByTupleTopDstAddress_Type())
sfpsCallByTupleTopDstAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallByTupleTopDstAddress.setStatus(_A)
_SfpsCallByTupleCallProcName_Type=DisplayString
_SfpsCallByTupleCallProcName_Object=MibTableColumn
sfpsCallByTupleCallProcName=_SfpsCallByTupleCallProcName_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,5,1,1,13),_SfpsCallByTupleCallProcName_Type())
sfpsCallByTupleCallProcName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallByTupleCallProcName.setStatus(_A)
_SfpsCallByTupleCallTag_Type=HexInteger
_SfpsCallByTupleCallTag_Object=MibTableColumn
sfpsCallByTupleCallTag=_SfpsCallByTupleCallTag_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,5,1,1,14),_SfpsCallByTupleCallTag_Type())
sfpsCallByTupleCallTag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallByTupleCallTag.setStatus(_A)
_SfpsCallByTupleCallState_Type=DisplayString
_SfpsCallByTupleCallState_Object=MibTableColumn
sfpsCallByTupleCallState=_SfpsCallByTupleCallState_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,5,1,1,15),_SfpsCallByTupleCallState_Type())
sfpsCallByTupleCallState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallByTupleCallState.setStatus(_A)
_SfpsCallByTupleTimeRemaining_Type=TimeTicks
_SfpsCallByTupleTimeRemaining_Object=MibTableColumn
sfpsCallByTupleTimeRemaining=_SfpsCallByTupleTimeRemaining_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,5,1,1,16),_SfpsCallByTupleTimeRemaining_Type())
sfpsCallByTupleTimeRemaining.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallByTupleTimeRemaining.setStatus(_A)
_SfpsCallTableStatsRam_Type=Integer32
_SfpsCallTableStatsRam_Object=MibScalar
sfpsCallTableStatsRam=_SfpsCallTableStatsRam_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,6,1),_SfpsCallTableStatsRam_Type())
sfpsCallTableStatsRam.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallTableStatsRam.setStatus(_A)
_SfpsCallTableStatsSize_Type=Integer32
_SfpsCallTableStatsSize_Object=MibScalar
sfpsCallTableStatsSize=_SfpsCallTableStatsSize_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,6,2),_SfpsCallTableStatsSize_Type())
sfpsCallTableStatsSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallTableStatsSize.setStatus(_A)
_SfpsCallTableStatsInUse_Type=Integer32
_SfpsCallTableStatsInUse_Object=MibScalar
sfpsCallTableStatsInUse=_SfpsCallTableStatsInUse_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,6,3),_SfpsCallTableStatsInUse_Type())
sfpsCallTableStatsInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallTableStatsInUse.setStatus(_A)
_SfpsCallTableStatsMax_Type=Integer32
_SfpsCallTableStatsMax_Object=MibScalar
sfpsCallTableStatsMax=_SfpsCallTableStatsMax_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,6,4),_SfpsCallTableStatsMax_Type())
sfpsCallTableStatsMax.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallTableStatsMax.setStatus(_A)
_SfpsCallTableStatsTotMisses_Type=Integer32
_SfpsCallTableStatsTotMisses_Object=MibScalar
sfpsCallTableStatsTotMisses=_SfpsCallTableStatsTotMisses_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,6,5),_SfpsCallTableStatsTotMisses_Type())
sfpsCallTableStatsTotMisses.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallTableStatsTotMisses.setStatus(_A)
_SfpsCallTableStatsMissStart_Type=TimeTicks
_SfpsCallTableStatsMissStart_Object=MibScalar
sfpsCallTableStatsMissStart=_SfpsCallTableStatsMissStart_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,6,7),_SfpsCallTableStatsMissStart_Type())
sfpsCallTableStatsMissStart.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallTableStatsMissStart.setStatus(_A)
_SfpsCallTableStatsMissStop_Type=TimeTicks
_SfpsCallTableStatsMissStop_Object=MibScalar
sfpsCallTableStatsMissStop=_SfpsCallTableStatsMissStop_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,6,8),_SfpsCallTableStatsMissStop_Type())
sfpsCallTableStatsMissStop.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCallTableStatsMissStop.setStatus(_A)
_SfpsCallTableStatsLastMiss_Type=Integer32
_SfpsCallTableStatsLastMiss_Object=MibScalar
sfpsCallTableStatsLastMiss=_SfpsCallTableStatsLastMiss_Object((1,3,6,1,4,1,52,4,2,4,2,2,5,1,6,9),_SfpsCallTableStatsLastMiss_Type())
sfpsCallTableStatsLastMiss.setMaxAccess(_H)
if mibBuilder.loadTexts:sfpsCallTableStatsLastMiss.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'HexInteger':HexInteger,'sfpsSapTable':sfpsSapTable,'sfpsSapTableEntry':sfpsSapTableEntry,_I:sfpsSapTableTag,_J:sfpsSapTableHash,_K:sfpsSapTableHashIndex,'sfpsSapTableSourceCP':sfpsSapTableSourceCP,'sfpsSapTableDestCP':sfpsSapTableDestCP,'sfpsSapTableSAP':sfpsSapTableSAP,'sfpsSapTableOperStatus':sfpsSapTableOperStatus,'sfpsSapTableAdminStatus':sfpsSapTableAdminStatus,'sfpsSapTableStateTime':sfpsSapTableStateTime,'sfpsSapTableDescription':sfpsSapTableDescription,'sfpsSapTableNumAccepted':sfpsSapTableNumAccepted,'sfpsSapTableNumDropped':sfpsSapTableNumDropped,'sfpsSapTableUnicastSap':sfpsSapTableUnicastSap,'sfpsSapTableNVStatus':sfpsSapTableNVStatus,'sfpsSapAPIVerb':sfpsSapAPIVerb,'sfpsSapAPISourceCP':sfpsSapAPISourceCP,'sfpsSapAPIDestCP':sfpsSapAPIDestCP,'sfpsSapAPISAP':sfpsSapAPISAP,'sfpsSapAPINVStatus':sfpsSapAPINVStatus,'sfpsSapAPIAdminStatus':sfpsSapAPIAdminStatus,'sfpsSapAPIOperStatus':sfpsSapAPIOperStatus,'sfpsSapAPINvSet':sfpsSapAPINvSet,'sfpsSapAPINVTotal':sfpsSapAPINVTotal,'sfpsSapAPINumAccept':sfpsSapAPINumAccept,'sfpsSapAPINvDiscard':sfpsSapAPINvDiscard,'sfpsSapAPIDefaultStatus':sfpsSapAPIDefaultStatus,'sfpsCallByTupleTable':sfpsCallByTupleTable,'sfpsCallByTupleEntry':sfpsCallByTupleEntry,_L:sfpsCallByTupleInPort,_M:sfpsCallByTupleSrcHash,_N:sfpsCallByTupleDstHash,_O:sfpsCallByTupleHashIndex,'sfpsCallByTupleBotSrcType':sfpsCallByTupleBotSrcType,'sfpsCallByTupleBotSrcAddress':sfpsCallByTupleBotSrcAddress,'sfpsCallByTupleBotDstType':sfpsCallByTupleBotDstType,'sfpsCallByTupleBotDstAddress':sfpsCallByTupleBotDstAddress,'sfpsCallByTupleTopSrcType':sfpsCallByTupleTopSrcType,'sfpsCallByTupleTopSrcAddress':sfpsCallByTupleTopSrcAddress,'sfpsCallByTupleTopDstType':sfpsCallByTupleTopDstType,'sfpsCallByTupleTopDstAddress':sfpsCallByTupleTopDstAddress,'sfpsCallByTupleCallProcName':sfpsCallByTupleCallProcName,'sfpsCallByTupleCallTag':sfpsCallByTupleCallTag,'sfpsCallByTupleCallState':sfpsCallByTupleCallState,'sfpsCallByTupleTimeRemaining':sfpsCallByTupleTimeRemaining,'sfpsCallTableStatsRam':sfpsCallTableStatsRam,'sfpsCallTableStatsSize':sfpsCallTableStatsSize,'sfpsCallTableStatsInUse':sfpsCallTableStatsInUse,'sfpsCallTableStatsMax':sfpsCallTableStatsMax,'sfpsCallTableStatsTotMisses':sfpsCallTableStatsTotMisses,'sfpsCallTableStatsMissStart':sfpsCallTableStatsMissStart,'sfpsCallTableStatsMissStop':sfpsCallTableStatsMissStop,'sfpsCallTableStatsLastMiss':sfpsCallTableStatsLastMiss})