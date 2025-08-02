_P='discard'
_O='disable'
_N='enable'
_M='read-create'
_L='yes'
_K='almonly'
_J='off'
_I='none'
_H='ifIndex'
_G='IF-MIB'
_F='DisplayString'
_E='unknown'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
nnOme40G,=mibBuilder.importSymbols('NORTEL-OME40G-MIB','nnOme40G')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
nnOme40GFacilities=ModuleIdentity((1,3,6,1,4,1,562,68,11,3,1))
if mibBuilder.loadTexts:nnOme40GFacilities.setRevisions(('2007-08-10 00:00','2009-05-20 00:00','2014-08-18 00:00'))
class GccValues(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_E,0),(_I,1),('gcc0',2),('gcc1',3),('gcc2',4)))
class AdminState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('is',1),('oos',2)))
class PrimaryState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_E,0),('is',1),('is-anr',2),('oos-au',3),('oos-ma',4),('oos-auma',5),('oos-maanr',6)))
class LoopbackType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_E,0),(_I,1),('facility',2),('terminal',3),('efmremote',4)))
class Status(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('enabled',1),('disabled',2)))
class FecFormat(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_E,0),(_J,1),('rs8',2),('scfec',3),('bch20',4),('pfec',5)))
_NnOCn_ObjectIdentity=ObjectIdentity
nnOCn=_NnOCn_ObjectIdentity((1,3,6,1,4,1,562,68,11,3,1,1))
_NnOCnTable_Object=MibTable
nnOCnTable=_NnOCnTable_Object((1,3,6,1,4,1,562,68,11,3,1,1,1))
if mibBuilder.loadTexts:nnOCnTable.setStatus(_A)
_NnOCnEntry_Object=MibTableRow
nnOCnEntry=_NnOCnEntry_Object((1,3,6,1,4,1,562,68,11,3,1,1,1,1))
nnOCnEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:nnOCnEntry.setStatus(_A)
_OcnRowStatus_Type=RowStatus
_OcnRowStatus_Object=MibTableColumn
ocnRowStatus=_OcnRowStatus_Object((1,3,6,1,4,1,562,68,11,3,1,1,1,1,1),_OcnRowStatus_Type())
ocnRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ocnRowStatus.setStatus(_A)
class _StFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('num',1),('string',2)))
_StFormat_Type.__name__=_D
_StFormat_Object=MibTableColumn
stFormat=_StFormat_Object((1,3,6,1,4,1,562,68,11,3,1,1,1,1,2),_StFormat_Type())
stFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:stFormat.setStatus(_A)
_ExpSTrc_Type=DisplayString
_ExpSTrc_Object=MibTableColumn
expSTrc=_ExpSTrc_Object((1,3,6,1,4,1,562,68,11,3,1,1,1,1,3),_ExpSTrc_Type())
expSTrc.setMaxAccess(_C)
if mibBuilder.loadTexts:expSTrc.setStatus(_A)
class _StfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_J,1),(_K,2)))
_StfMode_Type.__name__=_D
_StfMode_Object=MibTableColumn
stfMode=_StfMode_Object((1,3,6,1,4,1,562,68,11,3,1,1,1,1,4),_StfMode_Type())
stfMode.setMaxAccess(_C)
if mibBuilder.loadTexts:stfMode.setStatus(_A)
_EBerTh_Type=Integer32
_EBerTh_Object=MibTableColumn
eBerTh=_EBerTh_Object((1,3,6,1,4,1,562,68,11,3,1,1,1,1,5),_EBerTh_Type())
eBerTh.setMaxAccess(_B)
if mibBuilder.loadTexts:eBerTh.setStatus(_A)
class _OcnPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('sonet',1),('sdh',2)))
_OcnPortMode_Type.__name__=_D
_OcnPortMode_Object=MibTableColumn
ocnPortMode=_OcnPortMode_Object((1,3,6,1,4,1,562,68,11,3,1,1,1,1,6),_OcnPortMode_Type())
ocnPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ocnPortMode.setStatus(_A)
_OcnLaserOffFarEndFail_Type=Status
_OcnLaserOffFarEndFail_Object=MibTableColumn
ocnLaserOffFarEndFail=_OcnLaserOffFarEndFail_Object((1,3,6,1,4,1,562,68,11,3,1,1,1,1,7),_OcnLaserOffFarEndFail_Type())
ocnLaserOffFarEndFail.setMaxAccess(_C)
if mibBuilder.loadTexts:ocnLaserOffFarEndFail.setStatus(_A)
_OChTxActOcnPwr_Type=DisplayString
_OChTxActOcnPwr_Object=MibTableColumn
oChTxActOcnPwr=_OChTxActOcnPwr_Object((1,3,6,1,4,1,562,68,11,3,1,1,1,1,8),_OChTxActOcnPwr_Type())
oChTxActOcnPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:oChTxActOcnPwr.setStatus(_A)
_OChTxMinOcnPwr_Type=DisplayString
_OChTxMinOcnPwr_Object=MibTableColumn
oChTxMinOcnPwr=_OChTxMinOcnPwr_Object((1,3,6,1,4,1,562,68,11,3,1,1,1,1,9),_OChTxMinOcnPwr_Type())
oChTxMinOcnPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:oChTxMinOcnPwr.setStatus(_A)
_OChTxMaxOcnPwr_Type=DisplayString
_OChTxMaxOcnPwr_Object=MibTableColumn
oChTxMaxOcnPwr=_OChTxMaxOcnPwr_Object((1,3,6,1,4,1,562,68,11,3,1,1,1,1,10),_OChTxMaxOcnPwr_Type())
oChTxMaxOcnPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:oChTxMaxOcnPwr.setStatus(_A)
_OChRxActOcnPwr_Type=DisplayString
_OChRxActOcnPwr_Object=MibTableColumn
oChRxActOcnPwr=_OChRxActOcnPwr_Object((1,3,6,1,4,1,562,68,11,3,1,1,1,1,11),_OChRxActOcnPwr_Type())
oChRxActOcnPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:oChRxActOcnPwr.setStatus(_A)
_OChRxMinOcnPwr_Type=DisplayString
_OChRxMinOcnPwr_Object=MibTableColumn
oChRxMinOcnPwr=_OChRxMinOcnPwr_Object((1,3,6,1,4,1,562,68,11,3,1,1,1,1,12),_OChRxMinOcnPwr_Type())
oChRxMinOcnPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:oChRxMinOcnPwr.setStatus(_A)
_OChRxMaxOcnPwr_Type=DisplayString
_OChRxMaxOcnPwr_Object=MibTableColumn
oChRxMaxOcnPwr=_OChRxMaxOcnPwr_Object((1,3,6,1,4,1,562,68,11,3,1,1,1,1,13),_OChRxMaxOcnPwr_Type())
oChRxMaxOcnPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:oChRxMaxOcnPwr.setStatus(_A)
_ExpSectionTraceMsg_Type=DisplayString
_ExpSectionTraceMsg_Object=MibTableColumn
expSectionTraceMsg=_ExpSectionTraceMsg_Object((1,3,6,1,4,1,562,68,11,3,1,1,1,1,14),_ExpSectionTraceMsg_Type())
expSectionTraceMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:expSectionTraceMsg.setStatus(_A)
_IncSectionTraceMsg_Type=DisplayString
_IncSectionTraceMsg_Object=MibTableColumn
incSectionTraceMsg=_IncSectionTraceMsg_Object((1,3,6,1,4,1,562,68,11,3,1,1,1,1,15),_IncSectionTraceMsg_Type())
incSectionTraceMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:incSectionTraceMsg.setStatus(_A)
_OcnLoopbackType_Type=LoopbackType
_OcnLoopbackType_Object=MibTableColumn
ocnLoopbackType=_OcnLoopbackType_Object((1,3,6,1,4,1,562,68,11,3,1,1,1,1,16),_OcnLoopbackType_Type())
ocnLoopbackType.setMaxAccess(_C)
if mibBuilder.loadTexts:ocnLoopbackType.setStatus(_A)
_OcnPrimaryState_Type=PrimaryState
_OcnPrimaryState_Object=MibTableColumn
ocnPrimaryState=_OcnPrimaryState_Object((1,3,6,1,4,1,562,68,11,3,1,1,1,1,17),_OcnPrimaryState_Type())
ocnPrimaryState.setMaxAccess(_B)
if mibBuilder.loadTexts:ocnPrimaryState.setStatus(_A)
_OcnSecondaryState_Type=DisplayString
_OcnSecondaryState_Object=MibTableColumn
ocnSecondaryState=_OcnSecondaryState_Object((1,3,6,1,4,1,562,68,11,3,1,1,1,1,18),_OcnSecondaryState_Type())
ocnSecondaryState.setMaxAccess(_B)
if mibBuilder.loadTexts:ocnSecondaryState.setStatus(_A)
_OcnAdminState_Type=AdminState
_OcnAdminState_Object=MibTableColumn
ocnAdminState=_OcnAdminState_Object((1,3,6,1,4,1,562,68,11,3,1,1,1,1,19),_OcnAdminState_Type())
ocnAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:ocnAdminState.setStatus(_A)
_OcnAID_Type=DisplayString
_OcnAID_Object=MibTableColumn
ocnAID=_OcnAID_Object((1,3,6,1,4,1,562,68,11,3,1,1,1,1,20),_OcnAID_Type())
ocnAID.setMaxAccess(_B)
if mibBuilder.loadTexts:ocnAID.setStatus(_A)
_NnOTMn_ObjectIdentity=ObjectIdentity
nnOTMn=_NnOTMn_ObjectIdentity((1,3,6,1,4,1,562,68,11,3,1,2))
_NnOTMnTable_Object=MibTable
nnOTMnTable=_NnOTMnTable_Object((1,3,6,1,4,1,562,68,11,3,1,2,1))
if mibBuilder.loadTexts:nnOTMnTable.setStatus(_A)
_NnOTMnEntry_Object=MibTableRow
nnOTMnEntry=_NnOTMnEntry_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1))
nnOTMnEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:nnOTMnEntry.setStatus(_A)
_OtmRowStatus_Type=RowStatus
_OtmRowStatus_Object=MibTableColumn
otmRowStatus=_OtmRowStatus_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,1),_OtmRowStatus_Type())
otmRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:otmRowStatus.setStatus(_A)
_Osid_Type=DisplayString
_Osid_Object=MibTableColumn
osid=_Osid_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,2),_Osid_Type())
osid.setMaxAccess(_C)
if mibBuilder.loadTexts:osid.setStatus(_A)
_OtuTxFecFmt_Type=FecFormat
_OtuTxFecFmt_Object=MibTableColumn
otuTxFecFmt=_OtuTxFecFmt_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,3),_OtuTxFecFmt_Type())
otuTxFecFmt.setMaxAccess(_C)
if mibBuilder.loadTexts:otuTxFecFmt.setStatus(_A)
_OtuRxFecFmt_Type=FecFormat
_OtuRxFecFmt_Object=MibTableColumn
otuRxFecFmt=_OtuRxFecFmt_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,4),_OtuRxFecFmt_Type())
otuRxFecFmt.setMaxAccess(_C)
if mibBuilder.loadTexts:otuRxFecFmt.setStatus(_A)
class _OduTerm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_L,1),('no',2)))
_OduTerm_Type.__name__=_D
_OduTerm_Object=MibTableColumn
oduTerm=_OduTerm_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,5),_OduTerm_Type())
oduTerm.setMaxAccess(_B)
if mibBuilder.loadTexts:oduTerm.setStatus(_A)
class _OtuTxTTI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_OtuTxTTI_Type.__name__=_F
_OtuTxTTI_Object=MibTableColumn
otuTxTTI=_OtuTxTTI_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,6),_OtuTxTTI_Type())
otuTxTTI.setMaxAccess(_C)
if mibBuilder.loadTexts:otuTxTTI.setStatus(_A)
class _OduTxTTI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_OduTxTTI_Type.__name__=_F
_OduTxTTI_Object=MibTableColumn
oduTxTTI=_OduTxTTI_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,7),_OduTxTTI_Type())
oduTxTTI.setMaxAccess(_C)
if mibBuilder.loadTexts:oduTxTTI.setStatus(_A)
class _OtuRxExpTTI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_OtuRxExpTTI_Type.__name__=_F
_OtuRxExpTTI_Object=MibTableColumn
otuRxExpTTI=_OtuRxExpTTI_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,8),_OtuRxExpTTI_Type())
otuRxExpTTI.setMaxAccess(_C)
if mibBuilder.loadTexts:otuRxExpTTI.setStatus(_A)
class _OduRxExpTTI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_OduRxExpTTI_Type.__name__=_F
_OduRxExpTTI_Object=MibTableColumn
oduRxExpTTI=_OduRxExpTTI_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,9),_OduRxExpTTI_Type())
oduRxExpTTI.setMaxAccess(_C)
if mibBuilder.loadTexts:oduRxExpTTI.setStatus(_A)
class _TxPathId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TxPathId_Type.__name__=_D
_TxPathId_Object=MibTableColumn
txPathId=_TxPathId_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,10),_TxPathId_Type())
txPathId.setMaxAccess(_C)
if mibBuilder.loadTexts:txPathId.setStatus(_A)
_OChTxPwr_Type=DisplayString
_OChTxPwr_Object=MibTableColumn
oChTxPwr=_OChTxPwr_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,11),_OChTxPwr_Type())
oChTxPwr.setMaxAccess(_C)
if mibBuilder.loadTexts:oChTxPwr.setStatus(_A)
_OChTxActOtmPwr_Type=DisplayString
_OChTxActOtmPwr_Object=MibTableColumn
oChTxActOtmPwr=_OChTxActOtmPwr_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,12),_OChTxActOtmPwr_Type())
oChTxActOtmPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:oChTxActOtmPwr.setStatus(_A)
_OChTxMinOtmPwr_Type=DisplayString
_OChTxMinOtmPwr_Object=MibTableColumn
oChTxMinOtmPwr=_OChTxMinOtmPwr_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,13),_OChTxMinOtmPwr_Type())
oChTxMinOtmPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:oChTxMinOtmPwr.setStatus(_A)
_OChTxMaxOtmPwr_Type=DisplayString
_OChTxMaxOtmPwr_Object=MibTableColumn
oChTxMaxOtmPwr=_OChTxMaxOtmPwr_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,14),_OChTxMaxOtmPwr_Type())
oChTxMaxOtmPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:oChTxMaxOtmPwr.setStatus(_A)
_OChRxActOtmPwr_Type=DisplayString
_OChRxActOtmPwr_Object=MibTableColumn
oChRxActOtmPwr=_OChRxActOtmPwr_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,15),_OChRxActOtmPwr_Type())
oChRxActOtmPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:oChRxActOtmPwr.setStatus(_A)
_OChRxMinOtmPwr_Type=DisplayString
_OChRxMinOtmPwr_Object=MibTableColumn
oChRxMinOtmPwr=_OChRxMinOtmPwr_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,16),_OChRxMinOtmPwr_Type())
oChRxMinOtmPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:oChRxMinOtmPwr.setStatus(_A)
_OChRxMaxOtmPwr_Type=DisplayString
_OChRxMaxOtmPwr_Object=MibTableColumn
oChRxMaxOtmPwr=_OChRxMaxOtmPwr_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,17),_OChRxMaxOtmPwr_Type())
oChRxMaxOtmPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:oChRxMaxOtmPwr.setStatus(_A)
_OChTxWvlngthProv_Type=DisplayString
_OChTxWvlngthProv_Object=MibTableColumn
oChTxWvlngthProv=_OChTxWvlngthProv_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,18),_OChTxWvlngthProv_Type())
oChTxWvlngthProv.setMaxAccess(_C)
if mibBuilder.loadTexts:oChTxWvlngthProv.setStatus(_A)
_OChTxWvlngthMin_Type=DisplayString
_OChTxWvlngthMin_Object=MibTableColumn
oChTxWvlngthMin=_OChTxWvlngthMin_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,19),_OChTxWvlngthMin_Type())
oChTxWvlngthMin.setMaxAccess(_B)
if mibBuilder.loadTexts:oChTxWvlngthMin.setStatus(_A)
_OChTxWvlngthMax_Type=DisplayString
_OChTxWvlngthMax_Object=MibTableColumn
oChTxWvlngthMax=_OChTxWvlngthMax_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,20),_OChTxWvlngthMax_Type())
oChTxWvlngthMax.setMaxAccess(_B)
if mibBuilder.loadTexts:oChTxWvlngthMax.setStatus(_A)
_OChTxWvlngthSpacing_Type=DisplayString
_OChTxWvlngthSpacing_Object=MibTableColumn
oChTxWvlngthSpacing=_OChTxWvlngthSpacing_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,21),_OChTxWvlngthSpacing_Type())
oChTxWvlngthSpacing.setMaxAccess(_B)
if mibBuilder.loadTexts:oChTxWvlngthSpacing.setStatus(_A)
_OChRxActDisp_Type=DisplayString
_OChRxActDisp_Object=MibTableColumn
oChRxActDisp=_OChRxActDisp_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,22),_OChRxActDisp_Type())
oChRxActDisp.setMaxAccess(_B)
if mibBuilder.loadTexts:oChRxActDisp.setStatus(_A)
_OChRxActPmd_Type=DisplayString
_OChRxActPmd_Object=MibTableColumn
oChRxActPmd=_OChRxActPmd_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,23),_OChRxActPmd_Type())
oChRxActPmd.setMaxAccess(_B)
if mibBuilder.loadTexts:oChRxActPmd.setStatus(_A)
_OChRxPmdMax_Type=DisplayString
_OChRxPmdMax_Object=MibTableColumn
oChRxPmdMax=_OChRxPmdMax_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,24),_OChRxPmdMax_Type())
oChRxPmdMax.setMaxAccess(_B)
if mibBuilder.loadTexts:oChRxPmdMax.setStatus(_A)
_OChRxEchoTrace_Type=DisplayString
_OChRxEchoTrace_Object=MibTableColumn
oChRxEchoTrace=_OChRxEchoTrace_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,25),_OChRxEchoTrace_Type())
oChRxEchoTrace.setMaxAccess(_B)
if mibBuilder.loadTexts:oChRxEchoTrace.setStatus(_A)
_OChTxTrace_Type=DisplayString
_OChTxTrace_Object=MibTableColumn
oChTxTrace=_OChTxTrace_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,26),_OChTxTrace_Type())
oChTxTrace.setMaxAccess(_B)
if mibBuilder.loadTexts:oChTxTrace.setStatus(_A)
_OChTxAssocFarEndRx_Type=DisplayString
_OChTxAssocFarEndRx_Object=MibTableColumn
oChTxAssocFarEndRx=_OChTxAssocFarEndRx_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,27),_OChTxAssocFarEndRx_Type())
oChTxAssocFarEndRx.setMaxAccess(_B)
if mibBuilder.loadTexts:oChTxAssocFarEndRx.setStatus(_A)
class _OtmPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('sonet',1),('sdh',2)))
_OtmPortMode_Type.__name__=_D
_OtmPortMode_Object=MibTableColumn
otmPortMode=_OtmPortMode_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,28),_OtmPortMode_Type())
otmPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:otmPortMode.setStatus(_A)
class _TfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_E,0),(_J,1),(_K,2),('linefail',3)))
_TfMode_Type.__name__=_D
_TfMode_Object=MibTableColumn
tfMode=_TfMode_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,29),_TfMode_Type())
tfMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tfMode.setStatus(_A)
class _OduTfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_J,1),(_K,2)))
_OduTfMode_Type.__name__=_D
_OduTfMode_Object=MibTableColumn
oduTfMode=_OduTfMode_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,30),_OduTfMode_Type())
oduTfMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oduTfMode.setStatus(_A)
_OtmLaserOffFarEndFail_Type=Status
_OtmLaserOffFarEndFail_Object=MibTableColumn
otmLaserOffFarEndFail=_OtmLaserOffFarEndFail_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,31),_OtmLaserOffFarEndFail_Type())
otmLaserOffFarEndFail.setMaxAccess(_C)
if mibBuilder.loadTexts:otmLaserOffFarEndFail.setStatus(_A)
_PreFecSigFailThreshLevel_Type=DisplayString
_PreFecSigFailThreshLevel_Object=MibTableColumn
preFecSigFailThreshLevel=_PreFecSigFailThreshLevel_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,32),_PreFecSigFailThreshLevel_Type())
preFecSigFailThreshLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:preFecSigFailThreshLevel.setStatus(_A)
_OtuSignalDegradeThreshLevel_Type=Integer32
_OtuSignalDegradeThreshLevel_Object=MibTableColumn
otuSignalDegradeThreshLevel=_OtuSignalDegradeThreshLevel_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,33),_OtuSignalDegradeThreshLevel_Type())
otuSignalDegradeThreshLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:otuSignalDegradeThreshLevel.setStatus(_A)
class _OduMonitorEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_L,1),('no',2)))
_OduMonitorEnabled_Type.__name__=_D
_OduMonitorEnabled_Object=MibTableColumn
oduMonitorEnabled=_OduMonitorEnabled_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,34),_OduMonitorEnabled_Type())
oduMonitorEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:oduMonitorEnabled.setStatus(_A)
class _LineRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('rate-uknown',0),('rate-44G5',1),('rate-9G95',2),('rate-10G709',3),('rate-11G05',4),('rate-11G09',5)))
_LineRate_Type.__name__=_D
_LineRate_Object=MibTableColumn
lineRate=_LineRate_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,35),_LineRate_Type())
lineRate.setMaxAccess(_M)
if mibBuilder.loadTexts:lineRate.setStatus(_A)
_OtuExpTTI_Type=DisplayString
_OtuExpTTI_Object=MibTableColumn
otuExpTTI=_OtuExpTTI_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,36),_OtuExpTTI_Type())
otuExpTTI.setMaxAccess(_B)
if mibBuilder.loadTexts:otuExpTTI.setStatus(_A)
_OtuRxIncTTI_Type=DisplayString
_OtuRxIncTTI_Object=MibTableColumn
otuRxIncTTI=_OtuRxIncTTI_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,37),_OtuRxIncTTI_Type())
otuRxIncTTI.setMaxAccess(_B)
if mibBuilder.loadTexts:otuRxIncTTI.setStatus(_A)
_OduRxIncTTI_Type=DisplayString
_OduRxIncTTI_Object=MibTableColumn
oduRxIncTTI=_OduRxIncTTI_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,38),_OduRxIncTTI_Type())
oduRxIncTTI.setMaxAccess(_B)
if mibBuilder.loadTexts:oduRxIncTTI.setStatus(_A)
_OduMonitorMsg_Type=DisplayString
_OduMonitorMsg_Object=MibTableColumn
oduMonitorMsg=_OduMonitorMsg_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,39),_OduMonitorMsg_Type())
oduMonitorMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:oduMonitorMsg.setStatus(_A)
_OtmLoopbackType_Type=LoopbackType
_OtmLoopbackType_Object=MibTableColumn
otmLoopbackType=_OtmLoopbackType_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,40),_OtmLoopbackType_Type())
otmLoopbackType.setMaxAccess(_C)
if mibBuilder.loadTexts:otmLoopbackType.setStatus(_A)
class _Opu2reserved_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_L,1),('no',2)))
_Opu2reserved_Type.__name__=_D
_Opu2reserved_Object=MibTableColumn
opu2reserved=_Opu2reserved_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,41),_Opu2reserved_Type())
opu2reserved.setMaxAccess(_B)
if mibBuilder.loadTexts:opu2reserved.setStatus(_A)
class _ExpectedPayloadType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,2))
_ExpectedPayloadType_Type.__name__=_F
_ExpectedPayloadType_Object=MibTableColumn
expectedPayloadType=_ExpectedPayloadType_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,42),_ExpectedPayloadType_Type())
expectedPayloadType.setMaxAccess(_C)
if mibBuilder.loadTexts:expectedPayloadType.setStatus(_A)
class _TransmittedPayloadType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,2))
_TransmittedPayloadType_Type.__name__=_F
_TransmittedPayloadType_Object=MibTableColumn
transmittedPayloadType=_TransmittedPayloadType_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,43),_TransmittedPayloadType_Type())
transmittedPayloadType.setMaxAccess(_C)
if mibBuilder.loadTexts:transmittedPayloadType.setStatus(_A)
class _ReceivedPayloadType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,2))
_ReceivedPayloadType_Type.__name__=_F
_ReceivedPayloadType_Object=MibTableColumn
receivedPayloadType=_ReceivedPayloadType_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,44),_ReceivedPayloadType_Type())
receivedPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedPayloadType.setStatus(_A)
_OtmPrimaryState_Type=PrimaryState
_OtmPrimaryState_Object=MibTableColumn
otmPrimaryState=_OtmPrimaryState_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,45),_OtmPrimaryState_Type())
otmPrimaryState.setMaxAccess(_B)
if mibBuilder.loadTexts:otmPrimaryState.setStatus(_A)
_OtmSecondaryState_Type=DisplayString
_OtmSecondaryState_Object=MibTableColumn
otmSecondaryState=_OtmSecondaryState_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,46),_OtmSecondaryState_Type())
otmSecondaryState.setMaxAccess(_B)
if mibBuilder.loadTexts:otmSecondaryState.setStatus(_A)
_OtmAdminState_Type=AdminState
_OtmAdminState_Object=MibTableColumn
otmAdminState=_OtmAdminState_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,47),_OtmAdminState_Type())
otmAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:otmAdminState.setStatus(_A)
_OtmAID_Type=DisplayString
_OtmAID_Object=MibTableColumn
otmAID=_OtmAID_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,48),_OtmAID_Type())
otmAID.setMaxAccess(_B)
if mibBuilder.loadTexts:otmAID.setStatus(_A)
_OtmGCC_Type=GccValues
_OtmGCC_Object=MibTableColumn
otmGCC=_OtmGCC_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,49),_OtmGCC_Type())
otmGCC.setMaxAccess(_C)
if mibBuilder.loadTexts:otmGCC.setStatus(_A)
class _OspfCircuit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OspfCircuit_Type.__name__=_F
_OspfCircuit_Object=MibTableColumn
ospfCircuit=_OspfCircuit_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,50),_OspfCircuit_Type())
ospfCircuit.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfCircuit.setStatus(_A)
class _OChDifferentialEncoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_E,0),(_I,1),('hard',2),('soft',3)))
_OChDifferentialEncoding_Type.__name__=_D
_OChDifferentialEncoding_Object=MibTableColumn
oChDifferentialEncoding=_OChDifferentialEncoding_Object((1,3,6,1,4,1,562,68,11,3,1,2,1,1,51),_OChDifferentialEncoding_Type())
oChDifferentialEncoding.setMaxAccess(_C)
if mibBuilder.loadTexts:oChDifferentialEncoding.setStatus(_A)
_NnEth_ObjectIdentity=ObjectIdentity
nnEth=_NnEth_ObjectIdentity((1,3,6,1,4,1,562,68,11,3,1,3))
_NnEthTable_Object=MibTable
nnEthTable=_NnEthTable_Object((1,3,6,1,4,1,562,68,11,3,1,3,1))
if mibBuilder.loadTexts:nnEthTable.setStatus(_A)
_NnEthEntry_Object=MibTableRow
nnEthEntry=_NnEthEntry_Object((1,3,6,1,4,1,562,68,11,3,1,3,1,1))
nnEthEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:nnEthEntry.setStatus(_A)
_EthRowStatus_Type=RowStatus
_EthRowStatus_Object=MibTableColumn
ethRowStatus=_EthRowStatus_Object((1,3,6,1,4,1,562,68,11,3,1,3,1,1,1),_EthRowStatus_Type())
ethRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ethRowStatus.setStatus(_A)
_EthLaserOffFarEndFail_Type=Status
_EthLaserOffFarEndFail_Object=MibTableColumn
ethLaserOffFarEndFail=_EthLaserOffFarEndFail_Object((1,3,6,1,4,1,562,68,11,3,1,3,1,1,2),_EthLaserOffFarEndFail_Type())
ethLaserOffFarEndFail.setMaxAccess(_C)
if mibBuilder.loadTexts:ethLaserOffFarEndFail.setStatus(_A)
_OChTxActEthPwr_Type=DisplayString
_OChTxActEthPwr_Object=MibTableColumn
oChTxActEthPwr=_OChTxActEthPwr_Object((1,3,6,1,4,1,562,68,11,3,1,3,1,1,3),_OChTxActEthPwr_Type())
oChTxActEthPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:oChTxActEthPwr.setStatus(_A)
_OChTxMinEthPwr_Type=DisplayString
_OChTxMinEthPwr_Object=MibTableColumn
oChTxMinEthPwr=_OChTxMinEthPwr_Object((1,3,6,1,4,1,562,68,11,3,1,3,1,1,4),_OChTxMinEthPwr_Type())
oChTxMinEthPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:oChTxMinEthPwr.setStatus(_A)
_OChTxMaxEthPwr_Type=DisplayString
_OChTxMaxEthPwr_Object=MibTableColumn
oChTxMaxEthPwr=_OChTxMaxEthPwr_Object((1,3,6,1,4,1,562,68,11,3,1,3,1,1,5),_OChTxMaxEthPwr_Type())
oChTxMaxEthPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:oChTxMaxEthPwr.setStatus(_A)
_OChRxActEthPwr_Type=DisplayString
_OChRxActEthPwr_Object=MibTableColumn
oChRxActEthPwr=_OChRxActEthPwr_Object((1,3,6,1,4,1,562,68,11,3,1,3,1,1,6),_OChRxActEthPwr_Type())
oChRxActEthPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:oChRxActEthPwr.setStatus(_A)
_OChRxMinEthPwr_Type=DisplayString
_OChRxMinEthPwr_Object=MibTableColumn
oChRxMinEthPwr=_OChRxMinEthPwr_Object((1,3,6,1,4,1,562,68,11,3,1,3,1,1,7),_OChRxMinEthPwr_Type())
oChRxMinEthPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:oChRxMinEthPwr.setStatus(_A)
_OChRxMaxEthPwr_Type=DisplayString
_OChRxMaxEthPwr_Object=MibTableColumn
oChRxMaxEthPwr=_OChRxMaxEthPwr_Object((1,3,6,1,4,1,562,68,11,3,1,3,1,1,8),_OChRxMaxEthPwr_Type())
oChRxMaxEthPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:oChRxMaxEthPwr.setStatus(_A)
class _MaxTransUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('mtu-unknown',0),('mtu-1600',1),('mtu-9600',2)))
_MaxTransUnit_Type.__name__=_D
_MaxTransUnit_Object=MibTableColumn
maxTransUnit=_MaxTransUnit_Object((1,3,6,1,4,1,562,68,11,3,1,3,1,1,9),_MaxTransUnit_Type())
maxTransUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:maxTransUnit.setStatus(_A)
class _FlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_E,0),(_I,1),('asymmetric',2),('symmetric',3),('preeemptive',4)))
_FlowControl_Type.__name__=_D
_FlowControl_Object=MibTableColumn
flowControl=_FlowControl_Object((1,3,6,1,4,1,562,68,11,3,1,3,1,1,10),_FlowControl_Type())
flowControl.setMaxAccess(_C)
if mibBuilder.loadTexts:flowControl.setStatus(_A)
class _Equipment_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('xge-unknown',0),('xge-lan',1),('xge-wan',2)))
_Equipment_Type.__name__=_D
_Equipment_Object=MibTableColumn
equipment=_Equipment_Object((1,3,6,1,4,1,562,68,11,3,1,3,1,1,11),_Equipment_Type())
equipment.setMaxAccess(_C)
if mibBuilder.loadTexts:equipment.setStatus(_A)
class _EthMapping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_E,0),('prop237',1),('prop238',2),('gfp-mactr',3),('gfp-std',4),('gfp-mactr192',5),('gfp-std192',6),('gfp-mactr64',7),('gfp-std64',8),('gfp-macostr',9),('gfp-macostr192',10),('gfp-macostr64',11),('ull',12)))
_EthMapping_Type.__name__=_D
_EthMapping_Object=MibTableColumn
ethMapping=_EthMapping_Object((1,3,6,1,4,1,562,68,11,3,1,3,1,1,12),_EthMapping_Type())
ethMapping.setMaxAccess(_M)
if mibBuilder.loadTexts:ethMapping.setStatus(_A)
_EthLoopbackType_Type=LoopbackType
_EthLoopbackType_Object=MibTableColumn
ethLoopbackType=_EthLoopbackType_Object((1,3,6,1,4,1,562,68,11,3,1,3,1,1,13),_EthLoopbackType_Type())
ethLoopbackType.setMaxAccess(_C)
if mibBuilder.loadTexts:ethLoopbackType.setStatus(_A)
_EthPrimaryState_Type=PrimaryState
_EthPrimaryState_Object=MibTableColumn
ethPrimaryState=_EthPrimaryState_Object((1,3,6,1,4,1,562,68,11,3,1,3,1,1,14),_EthPrimaryState_Type())
ethPrimaryState.setMaxAccess(_B)
if mibBuilder.loadTexts:ethPrimaryState.setStatus(_A)
_EthSecondaryState_Type=DisplayString
_EthSecondaryState_Object=MibTableColumn
ethSecondaryState=_EthSecondaryState_Object((1,3,6,1,4,1,562,68,11,3,1,3,1,1,15),_EthSecondaryState_Type())
ethSecondaryState.setMaxAccess(_B)
if mibBuilder.loadTexts:ethSecondaryState.setStatus(_A)
_EthAdminState_Type=AdminState
_EthAdminState_Object=MibTableColumn
ethAdminState=_EthAdminState_Object((1,3,6,1,4,1,562,68,11,3,1,3,1,1,16),_EthAdminState_Type())
ethAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:ethAdminState.setStatus(_A)
_EthAID_Type=DisplayString
_EthAID_Object=MibTableColumn
ethAID=_EthAID_Object((1,3,6,1,4,1,562,68,11,3,1,3,1,1,17),_EthAID_Type())
ethAID.setMaxAccess(_B)
if mibBuilder.loadTexts:ethAID.setStatus(_A)
_NnWAN_ObjectIdentity=ObjectIdentity
nnWAN=_NnWAN_ObjectIdentity((1,3,6,1,4,1,562,68,11,3,1,4))
_NnWanTable_Object=MibTable
nnWanTable=_NnWanTable_Object((1,3,6,1,4,1,562,68,11,3,1,4,1))
if mibBuilder.loadTexts:nnWanTable.setStatus(_A)
_NnWanEntry_Object=MibTableRow
nnWanEntry=_NnWanEntry_Object((1,3,6,1,4,1,562,68,11,3,1,4,1,1))
nnWanEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:nnWanEntry.setStatus(_A)
class _FrameChecksum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(16,16),ValueRangeConstraint(32,32))
_FrameChecksum_Type.__name__=_D
_FrameChecksum_Object=MibTableColumn
frameChecksum=_FrameChecksum_Object((1,3,6,1,4,1,562,68,11,3,1,4,1,1,1),_FrameChecksum_Type())
frameChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:frameChecksum.setStatus(_A)
class _WanMapping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('gfp-f',1),('gfp-t',2)))
_WanMapping_Type.__name__=_D
_WanMapping_Object=MibTableColumn
wanMapping=_WanMapping_Object((1,3,6,1,4,1,562,68,11,3,1,4,1,1,2),_WanMapping_Type())
wanMapping.setMaxAccess(_C)
if mibBuilder.loadTexts:wanMapping.setStatus(_A)
class _GfpRfi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_N,1),(_O,2)))
_GfpRfi_Type.__name__=_D
_GfpRfi_Object=MibTableColumn
gfpRfi=_GfpRfi_Object((1,3,6,1,4,1,562,68,11,3,1,4,1,1,3),_GfpRfi_Type())
gfpRfi.setMaxAccess(_C)
if mibBuilder.loadTexts:gfpRfi.setStatus(_A)
class _GfpRtDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_N,1),(_O,2)))
_GfpRtDelay_Type.__name__=_D
_GfpRtDelay_Object=MibTableColumn
gfpRtDelay=_GfpRtDelay_Object((1,3,6,1,4,1,562,68,11,3,1,4,1,1,4),_GfpRtDelay_Type())
gfpRtDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:gfpRtDelay.setStatus(_A)
class _CondType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),('gfpcmf',1)))
_CondType_Type.__name__=_D
_CondType_Object=MibTableColumn
condType=_CondType_Object((1,3,6,1,4,1,562,68,11,3,1,4,1,1,5),_CondType_Type())
condType.setMaxAccess(_C)
if mibBuilder.loadTexts:condType.setStatus(_A)
class _Preamble_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('keep',1),(_P,2)))
_Preamble_Type.__name__=_D
_Preamble_Object=MibTableColumn
preamble=_Preamble_Object((1,3,6,1,4,1,562,68,11,3,1,4,1,1,6),_Preamble_Type())
preamble.setMaxAccess(_C)
if mibBuilder.loadTexts:preamble.setStatus(_A)
class _FcsErrFrames_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('keep',1),(_P,2)))
_FcsErrFrames_Type.__name__=_D
_FcsErrFrames_Object=MibTableColumn
fcsErrFrames=_FcsErrFrames_Object((1,3,6,1,4,1,562,68,11,3,1,4,1,1,7),_FcsErrFrames_Type())
fcsErrFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:fcsErrFrames.setStatus(_A)
class _TransmittedUPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,2))
_TransmittedUPI_Type.__name__=_F
_TransmittedUPI_Object=MibTableColumn
transmittedUPI=_TransmittedUPI_Object((1,3,6,1,4,1,562,68,11,3,1,4,1,1,8),_TransmittedUPI_Type())
transmittedUPI.setMaxAccess(_C)
if mibBuilder.loadTexts:transmittedUPI.setStatus(_A)
_WanPrimaryState_Type=PrimaryState
_WanPrimaryState_Object=MibTableColumn
wanPrimaryState=_WanPrimaryState_Object((1,3,6,1,4,1,562,68,11,3,1,4,1,1,9),_WanPrimaryState_Type())
wanPrimaryState.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPrimaryState.setStatus(_A)
_WanSecondaryState_Type=DisplayString
_WanSecondaryState_Object=MibTableColumn
wanSecondaryState=_WanSecondaryState_Object((1,3,6,1,4,1,562,68,11,3,1,4,1,1,10),_WanSecondaryState_Type())
wanSecondaryState.setMaxAccess(_B)
if mibBuilder.loadTexts:wanSecondaryState.setStatus(_A)
_WanAdminState_Type=AdminState
_WanAdminState_Object=MibTableColumn
wanAdminState=_WanAdminState_Object((1,3,6,1,4,1,562,68,11,3,1,4,1,1,11),_WanAdminState_Type())
wanAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:wanAdminState.setStatus(_A)
_WanAID_Type=DisplayString
_WanAID_Object=MibTableColumn
wanAID=_WanAID_Object((1,3,6,1,4,1,562,68,11,3,1,4,1,1,12),_WanAID_Type())
wanAID.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAID.setStatus(_A)
mibBuilder.exportSymbols('NORTEL-OME40G-FAC-MIB',**{'GccValues':GccValues,'AdminState':AdminState,'PrimaryState':PrimaryState,'LoopbackType':LoopbackType,'Status':Status,'FecFormat':FecFormat,'nnOme40GFacilities':nnOme40GFacilities,'nnOCn':nnOCn,'nnOCnTable':nnOCnTable,'nnOCnEntry':nnOCnEntry,'ocnRowStatus':ocnRowStatus,'stFormat':stFormat,'expSTrc':expSTrc,'stfMode':stfMode,'eBerTh':eBerTh,'ocnPortMode':ocnPortMode,'ocnLaserOffFarEndFail':ocnLaserOffFarEndFail,'oChTxActOcnPwr':oChTxActOcnPwr,'oChTxMinOcnPwr':oChTxMinOcnPwr,'oChTxMaxOcnPwr':oChTxMaxOcnPwr,'oChRxActOcnPwr':oChRxActOcnPwr,'oChRxMinOcnPwr':oChRxMinOcnPwr,'oChRxMaxOcnPwr':oChRxMaxOcnPwr,'expSectionTraceMsg':expSectionTraceMsg,'incSectionTraceMsg':incSectionTraceMsg,'ocnLoopbackType':ocnLoopbackType,'ocnPrimaryState':ocnPrimaryState,'ocnSecondaryState':ocnSecondaryState,'ocnAdminState':ocnAdminState,'ocnAID':ocnAID,'nnOTMn':nnOTMn,'nnOTMnTable':nnOTMnTable,'nnOTMnEntry':nnOTMnEntry,'otmRowStatus':otmRowStatus,'osid':osid,'otuTxFecFmt':otuTxFecFmt,'otuRxFecFmt':otuRxFecFmt,'oduTerm':oduTerm,'otuTxTTI':otuTxTTI,'oduTxTTI':oduTxTTI,'otuRxExpTTI':otuRxExpTTI,'oduRxExpTTI':oduRxExpTTI,'txPathId':txPathId,'oChTxPwr':oChTxPwr,'oChTxActOtmPwr':oChTxActOtmPwr,'oChTxMinOtmPwr':oChTxMinOtmPwr,'oChTxMaxOtmPwr':oChTxMaxOtmPwr,'oChRxActOtmPwr':oChRxActOtmPwr,'oChRxMinOtmPwr':oChRxMinOtmPwr,'oChRxMaxOtmPwr':oChRxMaxOtmPwr,'oChTxWvlngthProv':oChTxWvlngthProv,'oChTxWvlngthMin':oChTxWvlngthMin,'oChTxWvlngthMax':oChTxWvlngthMax,'oChTxWvlngthSpacing':oChTxWvlngthSpacing,'oChRxActDisp':oChRxActDisp,'oChRxActPmd':oChRxActPmd,'oChRxPmdMax':oChRxPmdMax,'oChRxEchoTrace':oChRxEchoTrace,'oChTxTrace':oChTxTrace,'oChTxAssocFarEndRx':oChTxAssocFarEndRx,'otmPortMode':otmPortMode,'tfMode':tfMode,'oduTfMode':oduTfMode,'otmLaserOffFarEndFail':otmLaserOffFarEndFail,'preFecSigFailThreshLevel':preFecSigFailThreshLevel,'otuSignalDegradeThreshLevel':otuSignalDegradeThreshLevel,'oduMonitorEnabled':oduMonitorEnabled,'lineRate':lineRate,'otuExpTTI':otuExpTTI,'otuRxIncTTI':otuRxIncTTI,'oduRxIncTTI':oduRxIncTTI,'oduMonitorMsg':oduMonitorMsg,'otmLoopbackType':otmLoopbackType,'opu2reserved':opu2reserved,'expectedPayloadType':expectedPayloadType,'transmittedPayloadType':transmittedPayloadType,'receivedPayloadType':receivedPayloadType,'otmPrimaryState':otmPrimaryState,'otmSecondaryState':otmSecondaryState,'otmAdminState':otmAdminState,'otmAID':otmAID,'otmGCC':otmGCC,'ospfCircuit':ospfCircuit,'oChDifferentialEncoding':oChDifferentialEncoding,'nnEth':nnEth,'nnEthTable':nnEthTable,'nnEthEntry':nnEthEntry,'ethRowStatus':ethRowStatus,'ethLaserOffFarEndFail':ethLaserOffFarEndFail,'oChTxActEthPwr':oChTxActEthPwr,'oChTxMinEthPwr':oChTxMinEthPwr,'oChTxMaxEthPwr':oChTxMaxEthPwr,'oChRxActEthPwr':oChRxActEthPwr,'oChRxMinEthPwr':oChRxMinEthPwr,'oChRxMaxEthPwr':oChRxMaxEthPwr,'maxTransUnit':maxTransUnit,'flowControl':flowControl,'equipment':equipment,'ethMapping':ethMapping,'ethLoopbackType':ethLoopbackType,'ethPrimaryState':ethPrimaryState,'ethSecondaryState':ethSecondaryState,'ethAdminState':ethAdminState,'ethAID':ethAID,'nnWAN':nnWAN,'nnWanTable':nnWanTable,'nnWanEntry':nnWanEntry,'frameChecksum':frameChecksum,'wanMapping':wanMapping,'gfpRfi':gfpRfi,'gfpRtDelay':gfpRtDelay,'condType':condType,'preamble':preamble,'fcsErrFrames':fcsErrFrames,'transmittedUPI':transmittedUPI,'wanPrimaryState':wanPrimaryState,'wanSecondaryState':wanSecondaryState,'wanAdminState':wanAdminState,'wanAID':wanAID})