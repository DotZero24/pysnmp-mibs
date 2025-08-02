_V='pmvoaCfgLabellineIndex'
_U='pmvoaCfgLabelclientIndex'
_T='pmvoaCfgLinexr1StartupIndex'
_S='pmvoaRinvLineIndex'
_R='pmvoaMesrlineEstPinIndex'
_Q='pmvoaMesrlinePoutIndex'
_P='pmvoaMesrlineSfpTempIndex'
_O='pmvoaAlmlineAlmIndex'
_N='pmvoaAlmsynthAlmLineIndex'
_M='pmvoaAlmDefFuseA'
_L='pmvoaAlmDefFuseB'
_K='pmvoatrapLineNumber'
_J='pmvoaAlmLineHwFailPortn'
_I='pmvoaAlmLineFailPortn'
_H='DisplayString'
_G='pmvoatrapBoardNumber'
_F='Unsigned32'
_E='Integer32'
_D='EKINOPS-Pmvoa-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EkiApiState,EkiMeasureType,EkiMode,EkiOnOff,EkiProtocol,EkiState,EkiSynchroMode,ekinops=mibBuilder.importSymbols('EKINOPS-MIB','EkiApiState','EkiMeasureType','EkiMode','EkiOnOff','EkiProtocol','EkiState','EkiSynchroMode','ekinops')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
modulePmvoa=ModuleIdentity((1,3,6,1,4,1,20044,84))
if mibBuilder.loadTexts:modulePmvoa.setRevisions(('2016-12-21 00:00',))
class PmvoaMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('attenuationctrl',0),('powerctrl',1)))
_Pmvoaalarms_ObjectIdentity=ObjectIdentity
pmvoaalarms=_Pmvoaalarms_ObjectIdentity((1,3,6,1,4,1,20044,84,2))
_PmvoaAlmOther_ObjectIdentity=ObjectIdentity
pmvoaAlmOther=_PmvoaAlmOther_ObjectIdentity((1,3,6,1,4,1,20044,84,2,1))
_PmvoaAlmOtherNurg_ObjectIdentity=ObjectIdentity
pmvoaAlmOtherNurg=_PmvoaAlmOtherNurg_ObjectIdentity((1,3,6,1,4,1,20044,84,2,1,1))
_PmvoaAlmsynthAlm2_ObjectIdentity=ObjectIdentity
pmvoaAlmsynthAlm2=_PmvoaAlmsynthAlm2_ObjectIdentity((1,3,6,1,4,1,20044,84,2,1,1,2))
_PmvoaAlmConfTableSave_Type=EkiOnOff
_PmvoaAlmConfTableSave_Object=MibScalar
pmvoaAlmConfTableSave=_PmvoaAlmConfTableSave_Object((1,3,6,1,4,1,20044,84,2,1,1,2,1),_PmvoaAlmConfTableSave_Type())
pmvoaAlmConfTableSave.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaAlmConfTableSave.setStatus(_A)
_PmvoaAlmInvUpload_Type=EkiOnOff
_PmvoaAlmInvUpload_Object=MibScalar
pmvoaAlmInvUpload=_PmvoaAlmInvUpload_Object((1,3,6,1,4,1,20044,84,2,1,1,2,2),_PmvoaAlmInvUpload_Type())
pmvoaAlmInvUpload.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaAlmInvUpload.setStatus(_A)
_PmvoaAlmConfTableLoad_Type=EkiOnOff
_PmvoaAlmConfTableLoad_Object=MibScalar
pmvoaAlmConfTableLoad=_PmvoaAlmConfTableLoad_Object((1,3,6,1,4,1,20044,84,2,1,1,2,3),_PmvoaAlmConfTableLoad_Type())
pmvoaAlmConfTableLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaAlmConfTableLoad.setStatus(_A)
_PmvoaAlmCorrelatOff_Type=EkiOnOff
_PmvoaAlmCorrelatOff_Object=MibScalar
pmvoaAlmCorrelatOff=_PmvoaAlmCorrelatOff_Object((1,3,6,1,4,1,20044,84,2,1,1,2,4),_PmvoaAlmCorrelatOff_Type())
pmvoaAlmCorrelatOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaAlmCorrelatOff.setStatus(_A)
_PmvoaAlmOtherUrg_ObjectIdentity=ObjectIdentity
pmvoaAlmOtherUrg=_PmvoaAlmOtherUrg_ObjectIdentity((1,3,6,1,4,1,20044,84,2,1,2))
_PmvoaAlmOtherCrit_ObjectIdentity=ObjectIdentity
pmvoaAlmOtherCrit=_PmvoaAlmOtherCrit_ObjectIdentity((1,3,6,1,4,1,20044,84,2,1,3))
_PmvoaAlmsynthAlm0_ObjectIdentity=ObjectIdentity
pmvoaAlmsynthAlm0=_PmvoaAlmsynthAlm0_ObjectIdentity((1,3,6,1,4,1,20044,84,2,1,3,0))
_PmvoaAlmModGlobFail_Type=EkiOnOff
_PmvoaAlmModGlobFail_Object=MibScalar
pmvoaAlmModGlobFail=_PmvoaAlmModGlobFail_Object((1,3,6,1,4,1,20044,84,2,1,3,0,9),_PmvoaAlmModGlobFail_Type())
pmvoaAlmModGlobFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaAlmModGlobFail.setStatus(_A)
_PmvoaAlmDefFuseA_Type=EkiOnOff
_PmvoaAlmDefFuseA_Object=MibScalar
pmvoaAlmDefFuseA=_PmvoaAlmDefFuseA_Object((1,3,6,1,4,1,20044,84,2,1,3,0,15),_PmvoaAlmDefFuseA_Type())
pmvoaAlmDefFuseA.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaAlmDefFuseA.setStatus(_A)
_PmvoaAlmDefFuseB_Type=EkiOnOff
_PmvoaAlmDefFuseB_Object=MibScalar
pmvoaAlmDefFuseB=_PmvoaAlmDefFuseB_Object((1,3,6,1,4,1,20044,84,2,1,3,0,16),_PmvoaAlmDefFuseB_Type())
pmvoaAlmDefFuseB.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaAlmDefFuseB.setStatus(_A)
_PmvoaAlmClient_ObjectIdentity=ObjectIdentity
pmvoaAlmClient=_PmvoaAlmClient_ObjectIdentity((1,3,6,1,4,1,20044,84,2,2))
_PmvoaAlmClientNurg_ObjectIdentity=ObjectIdentity
pmvoaAlmClientNurg=_PmvoaAlmClientNurg_ObjectIdentity((1,3,6,1,4,1,20044,84,2,2,1))
_PmvoaAlmClientUrg_ObjectIdentity=ObjectIdentity
pmvoaAlmClientUrg=_PmvoaAlmClientUrg_ObjectIdentity((1,3,6,1,4,1,20044,84,2,2,2))
_PmvoaAlmClientCrit_ObjectIdentity=ObjectIdentity
pmvoaAlmClientCrit=_PmvoaAlmClientCrit_ObjectIdentity((1,3,6,1,4,1,20044,84,2,2,3))
_PmvoaAlmLine_ObjectIdentity=ObjectIdentity
pmvoaAlmLine=_PmvoaAlmLine_ObjectIdentity((1,3,6,1,4,1,20044,84,2,3))
_PmvoaAlmLineNurg_ObjectIdentity=ObjectIdentity
pmvoaAlmLineNurg=_PmvoaAlmLineNurg_ObjectIdentity((1,3,6,1,4,1,20044,84,2,3,1))
_PmvoaAlmLineUrg_ObjectIdentity=ObjectIdentity
pmvoaAlmLineUrg=_PmvoaAlmLineUrg_ObjectIdentity((1,3,6,1,4,1,20044,84,2,3,2))
_PmvoaAlmLineCrit_ObjectIdentity=ObjectIdentity
pmvoaAlmLineCrit=_PmvoaAlmLineCrit_ObjectIdentity((1,3,6,1,4,1,20044,84,2,3,3))
_PmvoaAlmsynthAlmLineTable_Object=MibTable
pmvoaAlmsynthAlmLineTable=_PmvoaAlmsynthAlmLineTable_Object((1,3,6,1,4,1,20044,84,2,3,3,24))
if mibBuilder.loadTexts:pmvoaAlmsynthAlmLineTable.setStatus(_A)
_PmvoaAlmsynthAlmLineEntry_Object=MibTableRow
pmvoaAlmsynthAlmLineEntry=_PmvoaAlmsynthAlmLineEntry_Object((1,3,6,1,4,1,20044,84,2,3,3,24,1))
pmvoaAlmsynthAlmLineEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:pmvoaAlmsynthAlmLineEntry.setStatus(_A)
class _PmvoaAlmsynthAlmLineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmvoaAlmsynthAlmLineIndex_Type.__name__=_E
_PmvoaAlmsynthAlmLineIndex_Object=MibTableColumn
pmvoaAlmsynthAlmLineIndex=_PmvoaAlmsynthAlmLineIndex_Object((1,3,6,1,4,1,20044,84,2,3,3,24,1,1),_PmvoaAlmsynthAlmLineIndex_Type())
pmvoaAlmsynthAlmLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaAlmsynthAlmLineIndex.setStatus(_A)
_PmvoaAlmLineSfpVoaAbsentPortn_Type=EkiOnOff
_PmvoaAlmLineSfpVoaAbsentPortn_Object=MibTableColumn
pmvoaAlmLineSfpVoaAbsentPortn=_PmvoaAlmLineSfpVoaAbsentPortn_Object((1,3,6,1,4,1,20044,84,2,3,3,24,1,2),_PmvoaAlmLineSfpVoaAbsentPortn_Type())
pmvoaAlmLineSfpVoaAbsentPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaAlmLineSfpVoaAbsentPortn.setStatus(_A)
_PmvoaAlmLineHwFailPortn_Type=EkiOnOff
_PmvoaAlmLineHwFailPortn_Object=MibTableColumn
pmvoaAlmLineHwFailPortn=_PmvoaAlmLineHwFailPortn_Object((1,3,6,1,4,1,20044,84,2,3,3,24,1,5),_PmvoaAlmLineHwFailPortn_Type())
pmvoaAlmLineHwFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaAlmLineHwFailPortn.setStatus(_A)
_PmvoaAlmLineOosPortn_Type=EkiOnOff
_PmvoaAlmLineOosPortn_Object=MibTableColumn
pmvoaAlmLineOosPortn=_PmvoaAlmLineOosPortn_Object((1,3,6,1,4,1,20044,84,2,3,3,24,1,7),_PmvoaAlmLineOosPortn_Type())
pmvoaAlmLineOosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaAlmLineOosPortn.setStatus(_A)
_PmvoaAlmLineFailPortn_Type=EkiOnOff
_PmvoaAlmLineFailPortn_Object=MibTableColumn
pmvoaAlmLineFailPortn=_PmvoaAlmLineFailPortn_Object((1,3,6,1,4,1,20044,84,2,3,3,24,1,13),_PmvoaAlmLineFailPortn_Type())
pmvoaAlmLineFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaAlmLineFailPortn.setStatus(_A)
_PmvoaAlmlineAlmTable_Object=MibTable
pmvoaAlmlineAlmTable=_PmvoaAlmlineAlmTable_Object((1,3,6,1,4,1,20044,84,2,3,3,40))
if mibBuilder.loadTexts:pmvoaAlmlineAlmTable.setStatus(_A)
_PmvoaAlmlineAlmEntry_Object=MibTableRow
pmvoaAlmlineAlmEntry=_PmvoaAlmlineAlmEntry_Object((1,3,6,1,4,1,20044,84,2,3,3,40,1))
pmvoaAlmlineAlmEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:pmvoaAlmlineAlmEntry.setStatus(_A)
class _PmvoaAlmlineAlmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmvoaAlmlineAlmIndex_Type.__name__=_E
_PmvoaAlmlineAlmIndex_Object=MibTableColumn
pmvoaAlmlineAlmIndex=_PmvoaAlmlineAlmIndex_Object((1,3,6,1,4,1,20044,84,2,3,3,40,1,1),_PmvoaAlmlineAlmIndex_Type())
pmvoaAlmlineAlmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaAlmlineAlmIndex.setStatus(_A)
_PmvoaAlmOutputErrorPortn_Type=EkiOnOff
_PmvoaAlmOutputErrorPortn_Object=MibTableColumn
pmvoaAlmOutputErrorPortn=_PmvoaAlmOutputErrorPortn_Object((1,3,6,1,4,1,20044,84,2,3,3,40,1,2),_PmvoaAlmOutputErrorPortn_Type())
pmvoaAlmOutputErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaAlmOutputErrorPortn.setStatus(_A)
_PmvoaAlmLossOutputPowerPortn_Type=EkiOnOff
_PmvoaAlmLossOutputPowerPortn_Object=MibTableColumn
pmvoaAlmLossOutputPowerPortn=_PmvoaAlmLossOutputPowerPortn_Object((1,3,6,1,4,1,20044,84,2,3,3,40,1,3),_PmvoaAlmLossOutputPowerPortn_Type())
pmvoaAlmLossOutputPowerPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaAlmLossOutputPowerPortn.setStatus(_A)
_PmvoaAlmTempHighAlarmPortn_Type=EkiOnOff
_PmvoaAlmTempHighAlarmPortn_Object=MibTableColumn
pmvoaAlmTempHighAlarmPortn=_PmvoaAlmTempHighAlarmPortn_Object((1,3,6,1,4,1,20044,84,2,3,3,40,1,4),_PmvoaAlmTempHighAlarmPortn_Type())
pmvoaAlmTempHighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaAlmTempHighAlarmPortn.setStatus(_A)
_PmvoaAlmTempLowAlarmPortn_Type=EkiOnOff
_PmvoaAlmTempLowAlarmPortn_Object=MibTableColumn
pmvoaAlmTempLowAlarmPortn=_PmvoaAlmTempLowAlarmPortn_Object((1,3,6,1,4,1,20044,84,2,3,3,40,1,5),_PmvoaAlmTempLowAlarmPortn_Type())
pmvoaAlmTempLowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaAlmTempLowAlarmPortn.setStatus(_A)
_PmvoaAlmLossInputPowerPortn_Type=EkiOnOff
_PmvoaAlmLossInputPowerPortn_Object=MibTableColumn
pmvoaAlmLossInputPowerPortn=_PmvoaAlmLossInputPowerPortn_Object((1,3,6,1,4,1,20044,84,2,3,3,40,1,6),_PmvoaAlmLossInputPowerPortn_Type())
pmvoaAlmLossInputPowerPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaAlmLossInputPowerPortn.setStatus(_A)
_Pmvoameasures_ObjectIdentity=ObjectIdentity
pmvoameasures=_Pmvoameasures_ObjectIdentity((1,3,6,1,4,1,20044,84,3))
_PmvoaMesrOther_ObjectIdentity=ObjectIdentity
pmvoaMesrOther=_PmvoaMesrOther_ObjectIdentity((1,3,6,1,4,1,20044,84,3,1))
_PmvoaMesrClient_ObjectIdentity=ObjectIdentity
pmvoaMesrClient=_PmvoaMesrClient_ObjectIdentity((1,3,6,1,4,1,20044,84,3,2))
_PmvoaMesrLine_ObjectIdentity=ObjectIdentity
pmvoaMesrLine=_PmvoaMesrLine_ObjectIdentity((1,3,6,1,4,1,20044,84,3,3))
_PmvoaMesrlineSfpTempTable_Object=MibTable
pmvoaMesrlineSfpTempTable=_PmvoaMesrlineSfpTempTable_Object((1,3,6,1,4,1,20044,84,3,3,16))
if mibBuilder.loadTexts:pmvoaMesrlineSfpTempTable.setStatus(_A)
_PmvoaMesrlineSfpTempEntry_Object=MibTableRow
pmvoaMesrlineSfpTempEntry=_PmvoaMesrlineSfpTempEntry_Object((1,3,6,1,4,1,20044,84,3,3,16,1))
pmvoaMesrlineSfpTempEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:pmvoaMesrlineSfpTempEntry.setStatus(_A)
class _PmvoaMesrlineSfpTempIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmvoaMesrlineSfpTempIndex_Type.__name__=_E
_PmvoaMesrlineSfpTempIndex_Object=MibTableColumn
pmvoaMesrlineSfpTempIndex=_PmvoaMesrlineSfpTempIndex_Object((1,3,6,1,4,1,20044,84,3,3,16,1,1),_PmvoaMesrlineSfpTempIndex_Type())
pmvoaMesrlineSfpTempIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaMesrlineSfpTempIndex.setStatus(_A)
class _PmvoaMesrlineSfpTempPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmvoaMesrlineSfpTempPortn_Type.__name__=_E
_PmvoaMesrlineSfpTempPortn_Object=MibTableColumn
pmvoaMesrlineSfpTempPortn=_PmvoaMesrlineSfpTempPortn_Object((1,3,6,1,4,1,20044,84,3,3,16,1,2),_PmvoaMesrlineSfpTempPortn_Type())
pmvoaMesrlineSfpTempPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaMesrlineSfpTempPortn.setStatus(_A)
_PmvoaMesrlinePoutTable_Object=MibTable
pmvoaMesrlinePoutTable=_PmvoaMesrlinePoutTable_Object((1,3,6,1,4,1,20044,84,3,3,48))
if mibBuilder.loadTexts:pmvoaMesrlinePoutTable.setStatus(_A)
_PmvoaMesrlinePoutEntry_Object=MibTableRow
pmvoaMesrlinePoutEntry=_PmvoaMesrlinePoutEntry_Object((1,3,6,1,4,1,20044,84,3,3,48,1))
pmvoaMesrlinePoutEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:pmvoaMesrlinePoutEntry.setStatus(_A)
class _PmvoaMesrlinePoutIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmvoaMesrlinePoutIndex_Type.__name__=_E
_PmvoaMesrlinePoutIndex_Object=MibTableColumn
pmvoaMesrlinePoutIndex=_PmvoaMesrlinePoutIndex_Object((1,3,6,1,4,1,20044,84,3,3,48,1,1),_PmvoaMesrlinePoutIndex_Type())
pmvoaMesrlinePoutIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaMesrlinePoutIndex.setStatus(_A)
class _PmvoaMesrlinePoutPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmvoaMesrlinePoutPortn_Type.__name__=_E
_PmvoaMesrlinePoutPortn_Object=MibTableColumn
pmvoaMesrlinePoutPortn=_PmvoaMesrlinePoutPortn_Object((1,3,6,1,4,1,20044,84,3,3,48,1,2),_PmvoaMesrlinePoutPortn_Type())
pmvoaMesrlinePoutPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaMesrlinePoutPortn.setStatus(_A)
_PmvoaMesrlineEstPinTable_Object=MibTable
pmvoaMesrlineEstPinTable=_PmvoaMesrlineEstPinTable_Object((1,3,6,1,4,1,20044,84,3,3,64))
if mibBuilder.loadTexts:pmvoaMesrlineEstPinTable.setStatus(_A)
_PmvoaMesrlineEstPinEntry_Object=MibTableRow
pmvoaMesrlineEstPinEntry=_PmvoaMesrlineEstPinEntry_Object((1,3,6,1,4,1,20044,84,3,3,64,1))
pmvoaMesrlineEstPinEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:pmvoaMesrlineEstPinEntry.setStatus(_A)
class _PmvoaMesrlineEstPinIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmvoaMesrlineEstPinIndex_Type.__name__=_E
_PmvoaMesrlineEstPinIndex_Object=MibTableColumn
pmvoaMesrlineEstPinIndex=_PmvoaMesrlineEstPinIndex_Object((1,3,6,1,4,1,20044,84,3,3,64,1,1),_PmvoaMesrlineEstPinIndex_Type())
pmvoaMesrlineEstPinIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaMesrlineEstPinIndex.setStatus(_A)
class _PmvoaMesrlineEstPinPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmvoaMesrlineEstPinPortn_Type.__name__=_E
_PmvoaMesrlineEstPinPortn_Object=MibTableColumn
pmvoaMesrlineEstPinPortn=_PmvoaMesrlineEstPinPortn_Object((1,3,6,1,4,1,20044,84,3,3,64,1,2),_PmvoaMesrlineEstPinPortn_Type())
pmvoaMesrlineEstPinPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaMesrlineEstPinPortn.setStatus(_A)
_PmvoacontrolsWrite_ObjectIdentity=ObjectIdentity
pmvoacontrolsWrite=_PmvoacontrolsWrite_ObjectIdentity((1,3,6,1,4,1,20044,84,6))
_PmvoaCtrlOther_ObjectIdentity=ObjectIdentity
pmvoaCtrlOther=_PmvoaCtrlOther_ObjectIdentity((1,3,6,1,4,1,20044,84,6,1))
_PmvoaCtrlconfMgnt1_ObjectIdentity=ObjectIdentity
pmvoaCtrlconfMgnt1=_PmvoaCtrlconfMgnt1_ObjectIdentity((1,3,6,1,4,1,20044,84,6,1,1))
_PmvoaCtrlConf1Load1_Type=EkiOnOff
_PmvoaCtrlConf1Load1_Object=MibScalar
pmvoaCtrlConf1Load1=_PmvoaCtrlConf1Load1_Object((1,3,6,1,4,1,20044,84,6,1,1,1),_PmvoaCtrlConf1Load1_Type())
pmvoaCtrlConf1Load1.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCtrlConf1Load1.setStatus(_A)
_PmvoaCtrlConf2Load1_Type=EkiOnOff
_PmvoaCtrlConf2Load1_Object=MibScalar
pmvoaCtrlConf2Load1=_PmvoaCtrlConf2Load1_Object((1,3,6,1,4,1,20044,84,6,1,1,2),_PmvoaCtrlConf2Load1_Type())
pmvoaCtrlConf2Load1.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCtrlConf2Load1.setStatus(_A)
_PmvoaCtrlConf2Flash1_Type=EkiOnOff
_PmvoaCtrlConf2Flash1_Object=MibScalar
pmvoaCtrlConf2Flash1=_PmvoaCtrlConf2Flash1_Object((1,3,6,1,4,1,20044,84,6,1,1,10),_PmvoaCtrlConf2Flash1_Type())
pmvoaCtrlConf2Flash1.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCtrlConf2Flash1.setStatus(_A)
_PmvoaCtrlConf2Clear1_Type=EkiOnOff
_PmvoaCtrlConf2Clear1_Object=MibScalar
pmvoaCtrlConf2Clear1=_PmvoaCtrlConf2Clear1_Object((1,3,6,1,4,1,20044,84,6,1,1,14),_PmvoaCtrlConf2Clear1_Type())
pmvoaCtrlConf2Clear1.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCtrlConf2Clear1.setStatus(_A)
_PmvoaCtrlsynth4_ObjectIdentity=ObjectIdentity
pmvoaCtrlsynth4=_PmvoaCtrlsynth4_ObjectIdentity((1,3,6,1,4,1,20044,84,6,1,4))
_PmvoaCtrlCorrelatOn_Type=EkiOnOff
_PmvoaCtrlCorrelatOn_Object=MibScalar
pmvoaCtrlCorrelatOn=_PmvoaCtrlCorrelatOn_Object((1,3,6,1,4,1,20044,84,6,1,4,1),_PmvoaCtrlCorrelatOn_Type())
pmvoaCtrlCorrelatOn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCtrlCorrelatOn.setStatus(_A)
_PmvoaCtrlCorrelatOff_Type=EkiOnOff
_PmvoaCtrlCorrelatOff_Object=MibScalar
pmvoaCtrlCorrelatOff=_PmvoaCtrlCorrelatOff_Object((1,3,6,1,4,1,20044,84,6,1,4,2),_PmvoaCtrlCorrelatOff_Type())
pmvoaCtrlCorrelatOff.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCtrlCorrelatOff.setStatus(_A)
_PmvoaCtrlswMgnt_ObjectIdentity=ObjectIdentity
pmvoaCtrlswMgnt=_PmvoaCtrlswMgnt_ObjectIdentity((1,3,6,1,4,1,20044,84,6,1,5))
_PmvoaCtrlColdReset_Type=EkiOnOff
_PmvoaCtrlColdReset_Object=MibScalar
pmvoaCtrlColdReset=_PmvoaCtrlColdReset_Object((1,3,6,1,4,1,20044,84,6,1,5,2),_PmvoaCtrlColdReset_Type())
pmvoaCtrlColdReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCtrlColdReset.setStatus(_A)
_PmvoaCtrlWarmReset_Type=EkiOnOff
_PmvoaCtrlWarmReset_Object=MibScalar
pmvoaCtrlWarmReset=_PmvoaCtrlWarmReset_Object((1,3,6,1,4,1,20044,84,6,1,5,3),_PmvoaCtrlWarmReset_Type())
pmvoaCtrlWarmReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCtrlWarmReset.setStatus(_A)
_PmvoaCtrlLoadSwBank1_Type=EkiOnOff
_PmvoaCtrlLoadSwBank1_Object=MibScalar
pmvoaCtrlLoadSwBank1=_PmvoaCtrlLoadSwBank1_Object((1,3,6,1,4,1,20044,84,6,1,5,5),_PmvoaCtrlLoadSwBank1_Type())
pmvoaCtrlLoadSwBank1.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCtrlLoadSwBank1.setStatus(_A)
_PmvoaCtrlLoadSwBank2_Type=EkiOnOff
_PmvoaCtrlLoadSwBank2_Object=MibScalar
pmvoaCtrlLoadSwBank2=_PmvoaCtrlLoadSwBank2_Object((1,3,6,1,4,1,20044,84,6,1,5,6),_PmvoaCtrlLoadSwBank2_Type())
pmvoaCtrlLoadSwBank2.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCtrlLoadSwBank2.setStatus(_A)
_PmvoaCtrlgwMgnt_ObjectIdentity=ObjectIdentity
pmvoaCtrlgwMgnt=_PmvoaCtrlgwMgnt_ObjectIdentity((1,3,6,1,4,1,20044,84,6,1,6))
_PmvoaCtrlCurrentGwReset_Type=EkiOnOff
_PmvoaCtrlCurrentGwReset_Object=MibScalar
pmvoaCtrlCurrentGwReset=_PmvoaCtrlCurrentGwReset_Object((1,3,6,1,4,1,20044,84,6,1,6,1),_PmvoaCtrlCurrentGwReset_Type())
pmvoaCtrlCurrentGwReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCtrlCurrentGwReset.setStatus(_A)
_PmvoaCtrlLoadGwBank1_Type=EkiOnOff
_PmvoaCtrlLoadGwBank1_Object=MibScalar
pmvoaCtrlLoadGwBank1=_PmvoaCtrlLoadGwBank1_Object((1,3,6,1,4,1,20044,84,6,1,6,5),_PmvoaCtrlLoadGwBank1_Type())
pmvoaCtrlLoadGwBank1.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCtrlLoadGwBank1.setStatus(_A)
_PmvoaCtrlLoadGwBank2_Type=EkiOnOff
_PmvoaCtrlLoadGwBank2_Object=MibScalar
pmvoaCtrlLoadGwBank2=_PmvoaCtrlLoadGwBank2_Object((1,3,6,1,4,1,20044,84,6,1,6,6),_PmvoaCtrlLoadGwBank2_Type())
pmvoaCtrlLoadGwBank2.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCtrlLoadGwBank2.setStatus(_A)
_PmvoaCtrlLoadGwBank3_Type=EkiOnOff
_PmvoaCtrlLoadGwBank3_Object=MibScalar
pmvoaCtrlLoadGwBank3=_PmvoaCtrlLoadGwBank3_Object((1,3,6,1,4,1,20044,84,6,1,6,7),_PmvoaCtrlLoadGwBank3_Type())
pmvoaCtrlLoadGwBank3.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCtrlLoadGwBank3.setStatus(_A)
_PmvoaCtrlLoadGwBank4_Type=EkiOnOff
_PmvoaCtrlLoadGwBank4_Object=MibScalar
pmvoaCtrlLoadGwBank4=_PmvoaCtrlLoadGwBank4_Object((1,3,6,1,4,1,20044,84,6,1,6,8),_PmvoaCtrlLoadGwBank4_Type())
pmvoaCtrlLoadGwBank4.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCtrlLoadGwBank4.setStatus(_A)
_PmvoaCtrlledTest_ObjectIdentity=ObjectIdentity
pmvoaCtrlledTest=_PmvoaCtrlledTest_ObjectIdentity((1,3,6,1,4,1,20044,84,6,1,72))
_PmvoaCtrlGreenLed_Type=EkiOnOff
_PmvoaCtrlGreenLed_Object=MibScalar
pmvoaCtrlGreenLed=_PmvoaCtrlGreenLed_Object((1,3,6,1,4,1,20044,84,6,1,72,1),_PmvoaCtrlGreenLed_Type())
pmvoaCtrlGreenLed.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCtrlGreenLed.setStatus(_A)
_PmvoaCtrlRedLed_Type=EkiOnOff
_PmvoaCtrlRedLed_Object=MibScalar
pmvoaCtrlRedLed=_PmvoaCtrlRedLed_Object((1,3,6,1,4,1,20044,84,6,1,72,2),_PmvoaCtrlRedLed_Type())
pmvoaCtrlRedLed.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCtrlRedLed.setStatus(_A)
_PmvoaCtrlLedOff_Type=EkiOnOff
_PmvoaCtrlLedOff_Object=MibScalar
pmvoaCtrlLedOff=_PmvoaCtrlLedOff_Object((1,3,6,1,4,1,20044,84,6,1,72,3),_PmvoaCtrlLedOff_Type())
pmvoaCtrlLedOff.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCtrlLedOff.setStatus(_A)
_PmvoaCtrlClient_ObjectIdentity=ObjectIdentity
pmvoaCtrlClient=_PmvoaCtrlClient_ObjectIdentity((1,3,6,1,4,1,20044,84,6,2))
_PmvoaCtrlLine_ObjectIdentity=ObjectIdentity
pmvoaCtrlLine=_PmvoaCtrlLine_ObjectIdentity((1,3,6,1,4,1,20044,84,6,3))
_Pmvoari_ObjectIdentity=ObjectIdentity
pmvoari=_Pmvoari_ObjectIdentity((1,3,6,1,4,1,20044,84,7))
_PmvoariTable_ObjectIdentity=ObjectIdentity
pmvoariTable=_PmvoariTable_ObjectIdentity((1,3,6,1,4,1,20044,84,7,1))
_PmvoaRinvLineTable_Object=MibTable
pmvoaRinvLineTable=_PmvoaRinvLineTable_Object((1,3,6,1,4,1,20044,84,7,1,2))
if mibBuilder.loadTexts:pmvoaRinvLineTable.setStatus(_A)
_PmvoaRinvLineEntry_Object=MibTableRow
pmvoaRinvLineEntry=_PmvoaRinvLineEntry_Object((1,3,6,1,4,1,20044,84,7,1,2,1))
pmvoaRinvLineEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:pmvoaRinvLineEntry.setStatus(_A)
class _PmvoaRinvLineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PmvoaRinvLineIndex_Type.__name__=_E
_PmvoaRinvLineIndex_Object=MibTableColumn
pmvoaRinvLineIndex=_PmvoaRinvLineIndex_Object((1,3,6,1,4,1,20044,84,7,1,2,1,1),_PmvoaRinvLineIndex_Type())
pmvoaRinvLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaRinvLineIndex.setStatus(_A)
_PmvoaRinvxfpLine_Type=DisplayString
_PmvoaRinvxfpLine_Object=MibTableColumn
pmvoaRinvxfpLine=_PmvoaRinvxfpLine_Object((1,3,6,1,4,1,20044,84,7,1,2,1,2),_PmvoaRinvxfpLine_Type())
pmvoaRinvxfpLine.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaRinvxfpLine.setStatus(_A)
_PmvoaRinvReloadInventory_Type=EkiOnOff
_PmvoaRinvReloadInventory_Object=MibScalar
pmvoaRinvReloadInventory=_PmvoaRinvReloadInventory_Object((1,3,6,1,4,1,20044,84,7,2),_PmvoaRinvReloadInventory_Type())
pmvoaRinvReloadInventory.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaRinvReloadInventory.setStatus(_A)
_PmvoaRinvHwPlatform_Type=DisplayString
_PmvoaRinvHwPlatform_Object=MibScalar
pmvoaRinvHwPlatform=_PmvoaRinvHwPlatform_Object((1,3,6,1,4,1,20044,84,7,3),_PmvoaRinvHwPlatform_Type())
pmvoaRinvHwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaRinvHwPlatform.setStatus(_A)
_PmvoaRinvModulePlatform_Type=DisplayString
_PmvoaRinvModulePlatform_Object=MibScalar
pmvoaRinvModulePlatform=_PmvoaRinvModulePlatform_Object((1,3,6,1,4,1,20044,84,7,4),_PmvoaRinvModulePlatform_Type())
pmvoaRinvModulePlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaRinvModulePlatform.setStatus(_A)
_PmvoaRinvSwPlatform_Type=DisplayString
_PmvoaRinvSwPlatform_Object=MibScalar
pmvoaRinvSwPlatform=_PmvoaRinvSwPlatform_Object((1,3,6,1,4,1,20044,84,7,5),_PmvoaRinvSwPlatform_Type())
pmvoaRinvSwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaRinvSwPlatform.setStatus(_A)
_PmvoaRinvGwPlatform_Type=DisplayString
_PmvoaRinvGwPlatform_Object=MibScalar
pmvoaRinvGwPlatform=_PmvoaRinvGwPlatform_Object((1,3,6,1,4,1,20044,84,7,6),_PmvoaRinvGwPlatform_Type())
pmvoaRinvGwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaRinvGwPlatform.setStatus(_A)
_Pmvoadownload_ObjectIdentity=ObjectIdentity
pmvoadownload=_Pmvoadownload_ObjectIdentity((1,3,6,1,4,1,20044,84,8))
_PmvoaDwlOther_ObjectIdentity=ObjectIdentity
pmvoaDwlOther=_PmvoaDwlOther_ObjectIdentity((1,3,6,1,4,1,20044,84,8,1))
_PmvoaDwlrestartProcess_ObjectIdentity=ObjectIdentity
pmvoaDwlrestartProcess=_PmvoaDwlrestartProcess_ObjectIdentity((1,3,6,1,4,1,20044,84,8,1,0))
_PmvoaDwlWarmRestartProcessed_Type=EkiOnOff
_PmvoaDwlWarmRestartProcessed_Object=MibScalar
pmvoaDwlWarmRestartProcessed=_PmvoaDwlWarmRestartProcessed_Object((1,3,6,1,4,1,20044,84,8,1,0,1),_PmvoaDwlWarmRestartProcessed_Type())
pmvoaDwlWarmRestartProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaDwlWarmRestartProcessed.setStatus(_A)
_PmvoaDwlColdRestartProcessed_Type=EkiOnOff
_PmvoaDwlColdRestartProcessed_Object=MibScalar
pmvoaDwlColdRestartProcessed=_PmvoaDwlColdRestartProcessed_Object((1,3,6,1,4,1,20044,84,8,1,0,2),_PmvoaDwlColdRestartProcessed_Type())
pmvoaDwlColdRestartProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaDwlColdRestartProcessed.setStatus(_A)
_PmvoaDwlswBanksUsed_ObjectIdentity=ObjectIdentity
pmvoaDwlswBanksUsed=_PmvoaDwlswBanksUsed_ObjectIdentity((1,3,6,1,4,1,20044,84,8,1,1))
_PmvoaDwlSwBank1Used_Type=EkiOnOff
_PmvoaDwlSwBank1Used_Object=MibScalar
pmvoaDwlSwBank1Used=_PmvoaDwlSwBank1Used_Object((1,3,6,1,4,1,20044,84,8,1,1,1),_PmvoaDwlSwBank1Used_Type())
pmvoaDwlSwBank1Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaDwlSwBank1Used.setStatus(_A)
_PmvoaDwlSwBank2Used_Type=EkiOnOff
_PmvoaDwlSwBank2Used_Object=MibScalar
pmvoaDwlSwBank2Used=_PmvoaDwlSwBank2Used_Object((1,3,6,1,4,1,20044,84,8,1,1,2),_PmvoaDwlSwBank2Used_Type())
pmvoaDwlSwBank2Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaDwlSwBank2Used.setStatus(_A)
_PmvoaDwlSwBank1Notempty_Type=EkiOnOff
_PmvoaDwlSwBank1Notempty_Object=MibScalar
pmvoaDwlSwBank1Notempty=_PmvoaDwlSwBank1Notempty_Object((1,3,6,1,4,1,20044,84,8,1,1,5),_PmvoaDwlSwBank1Notempty_Type())
pmvoaDwlSwBank1Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaDwlSwBank1Notempty.setStatus(_A)
_PmvoaDwlSwBank2Notempty_Type=EkiOnOff
_PmvoaDwlSwBank2Notempty_Object=MibScalar
pmvoaDwlSwBank2Notempty=_PmvoaDwlSwBank2Notempty_Object((1,3,6,1,4,1,20044,84,8,1,1,6),_PmvoaDwlSwBank2Notempty_Type())
pmvoaDwlSwBank2Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaDwlSwBank2Notempty.setStatus(_A)
_PmvoaDwlgwBanksUsed_ObjectIdentity=ObjectIdentity
pmvoaDwlgwBanksUsed=_PmvoaDwlgwBanksUsed_ObjectIdentity((1,3,6,1,4,1,20044,84,8,1,2))
_PmvoaDwlGwBank1Used_Type=EkiOnOff
_PmvoaDwlGwBank1Used_Object=MibScalar
pmvoaDwlGwBank1Used=_PmvoaDwlGwBank1Used_Object((1,3,6,1,4,1,20044,84,8,1,2,1),_PmvoaDwlGwBank1Used_Type())
pmvoaDwlGwBank1Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaDwlGwBank1Used.setStatus(_A)
_PmvoaDwlGwBank2Used_Type=EkiOnOff
_PmvoaDwlGwBank2Used_Object=MibScalar
pmvoaDwlGwBank2Used=_PmvoaDwlGwBank2Used_Object((1,3,6,1,4,1,20044,84,8,1,2,2),_PmvoaDwlGwBank2Used_Type())
pmvoaDwlGwBank2Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaDwlGwBank2Used.setStatus(_A)
_PmvoaDwlGwBank3Used_Type=EkiOnOff
_PmvoaDwlGwBank3Used_Object=MibScalar
pmvoaDwlGwBank3Used=_PmvoaDwlGwBank3Used_Object((1,3,6,1,4,1,20044,84,8,1,2,3),_PmvoaDwlGwBank3Used_Type())
pmvoaDwlGwBank3Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaDwlGwBank3Used.setStatus(_A)
_PmvoaDwlGwBank4Used_Type=EkiOnOff
_PmvoaDwlGwBank4Used_Object=MibScalar
pmvoaDwlGwBank4Used=_PmvoaDwlGwBank4Used_Object((1,3,6,1,4,1,20044,84,8,1,2,4),_PmvoaDwlGwBank4Used_Type())
pmvoaDwlGwBank4Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaDwlGwBank4Used.setStatus(_A)
_PmvoaDwlGwBank1Notempty_Type=EkiOnOff
_PmvoaDwlGwBank1Notempty_Object=MibScalar
pmvoaDwlGwBank1Notempty=_PmvoaDwlGwBank1Notempty_Object((1,3,6,1,4,1,20044,84,8,1,2,5),_PmvoaDwlGwBank1Notempty_Type())
pmvoaDwlGwBank1Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaDwlGwBank1Notempty.setStatus(_A)
_PmvoaDwlGwBank2Notempty_Type=EkiOnOff
_PmvoaDwlGwBank2Notempty_Object=MibScalar
pmvoaDwlGwBank2Notempty=_PmvoaDwlGwBank2Notempty_Object((1,3,6,1,4,1,20044,84,8,1,2,6),_PmvoaDwlGwBank2Notempty_Type())
pmvoaDwlGwBank2Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaDwlGwBank2Notempty.setStatus(_A)
_PmvoaDwlGwBank3Notempty_Type=EkiOnOff
_PmvoaDwlGwBank3Notempty_Object=MibScalar
pmvoaDwlGwBank3Notempty=_PmvoaDwlGwBank3Notempty_Object((1,3,6,1,4,1,20044,84,8,1,2,7),_PmvoaDwlGwBank3Notempty_Type())
pmvoaDwlGwBank3Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaDwlGwBank3Notempty.setStatus(_A)
_PmvoaDwlGwBank4Notempty_Type=EkiOnOff
_PmvoaDwlGwBank4Notempty_Object=MibScalar
pmvoaDwlGwBank4Notempty=_PmvoaDwlGwBank4Notempty_Object((1,3,6,1,4,1,20044,84,8,1,2,8),_PmvoaDwlGwBank4Notempty_Type())
pmvoaDwlGwBank4Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaDwlGwBank4Notempty.setStatus(_A)
_PmvoaDwlClient_ObjectIdentity=ObjectIdentity
pmvoaDwlClient=_PmvoaDwlClient_ObjectIdentity((1,3,6,1,4,1,20044,84,8,2))
_PmvoaDwlLine_ObjectIdentity=ObjectIdentity
pmvoaDwlLine=_PmvoaDwlLine_ObjectIdentity((1,3,6,1,4,1,20044,84,8,3))
_PmvoaConfig_ObjectIdentity=ObjectIdentity
pmvoaConfig=_PmvoaConfig_ObjectIdentity((1,3,6,1,4,1,20044,84,9))
_PmvoaCfgStartup_ObjectIdentity=ObjectIdentity
pmvoaCfgStartup=_PmvoaCfgStartup_ObjectIdentity((1,3,6,1,4,1,20044,84,9,1))
_PmvoaCfgLinexr1StartupTable_Object=MibTable
pmvoaCfgLinexr1StartupTable=_PmvoaCfgLinexr1StartupTable_Object((1,3,6,1,4,1,20044,84,9,1,1))
if mibBuilder.loadTexts:pmvoaCfgLinexr1StartupTable.setStatus(_A)
_PmvoaCfgLinexr1StartupEntry_Object=MibTableRow
pmvoaCfgLinexr1StartupEntry=_PmvoaCfgLinexr1StartupEntry_Object((1,3,6,1,4,1,20044,84,9,1,1,1))
pmvoaCfgLinexr1StartupEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:pmvoaCfgLinexr1StartupEntry.setStatus(_A)
class _PmvoaCfgLinexr1StartupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmvoaCfgLinexr1StartupIndex_Type.__name__=_E
_PmvoaCfgLinexr1StartupIndex_Object=MibTableColumn
pmvoaCfgLinexr1StartupIndex=_PmvoaCfgLinexr1StartupIndex_Object((1,3,6,1,4,1,20044,84,9,1,1,1,1),_PmvoaCfgLinexr1StartupIndex_Type())
pmvoaCfgLinexr1StartupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaCfgLinexr1StartupIndex.setStatus(_A)
class _PmvoaCfgSfpModePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmvoaCfgSfpModePortn_Type.__name__=_F
_PmvoaCfgSfpModePortn_Object=MibTableColumn
pmvoaCfgSfpModePortn=_PmvoaCfgSfpModePortn_Object((1,3,6,1,4,1,20044,84,9,1,1,1,3),_PmvoaCfgSfpModePortn_Type())
pmvoaCfgSfpModePortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCfgSfpModePortn.setStatus(_A)
class _PmvoaCfgAttenuationCtrlPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmvoaCfgAttenuationCtrlPortn_Type.__name__=_F
_PmvoaCfgAttenuationCtrlPortn_Object=MibTableColumn
pmvoaCfgAttenuationCtrlPortn=_PmvoaCfgAttenuationCtrlPortn_Object((1,3,6,1,4,1,20044,84,9,1,1,1,4),_PmvoaCfgAttenuationCtrlPortn_Type())
pmvoaCfgAttenuationCtrlPortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCfgAttenuationCtrlPortn.setStatus(_A)
class _PmvoaCfgPowerCtrlPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmvoaCfgPowerCtrlPortn_Type.__name__=_F
_PmvoaCfgPowerCtrlPortn_Object=MibTableColumn
pmvoaCfgPowerCtrlPortn=_PmvoaCfgPowerCtrlPortn_Object((1,3,6,1,4,1,20044,84,9,1,1,1,5),_PmvoaCfgPowerCtrlPortn_Type())
pmvoaCfgPowerCtrlPortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCfgPowerCtrlPortn.setStatus(_A)
class _PmvoaCfgLosInputThresholdPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmvoaCfgLosInputThresholdPortn_Type.__name__=_F
_PmvoaCfgLosInputThresholdPortn_Object=MibTableColumn
pmvoaCfgLosInputThresholdPortn=_PmvoaCfgLosInputThresholdPortn_Object((1,3,6,1,4,1,20044,84,9,1,1,1,6),_PmvoaCfgLosInputThresholdPortn_Type())
pmvoaCfgLosInputThresholdPortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCfgLosInputThresholdPortn.setStatus(_A)
class _PmvoaCfgInsertionLossValuePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmvoaCfgInsertionLossValuePortn_Type.__name__=_F
_PmvoaCfgInsertionLossValuePortn_Object=MibTableColumn
pmvoaCfgInsertionLossValuePortn=_PmvoaCfgInsertionLossValuePortn_Object((1,3,6,1,4,1,20044,84,9,1,1,1,7),_PmvoaCfgInsertionLossValuePortn_Type())
pmvoaCfgInsertionLossValuePortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCfgInsertionLossValuePortn.setStatus(_A)
_PmvoaCfgLabels_ObjectIdentity=ObjectIdentity
pmvoaCfgLabels=_PmvoaCfgLabels_ObjectIdentity((1,3,6,1,4,1,20044,84,9,2))
_PmvoaCfgLabelclientTable_Object=MibTable
pmvoaCfgLabelclientTable=_PmvoaCfgLabelclientTable_Object((1,3,6,1,4,1,20044,84,9,2,1))
if mibBuilder.loadTexts:pmvoaCfgLabelclientTable.setStatus(_A)
_PmvoaCfgLabelclientEntry_Object=MibTableRow
pmvoaCfgLabelclientEntry=_PmvoaCfgLabelclientEntry_Object((1,3,6,1,4,1,20044,84,9,2,1,1))
pmvoaCfgLabelclientEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:pmvoaCfgLabelclientEntry.setStatus(_A)
class _PmvoaCfgLabelclientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmvoaCfgLabelclientIndex_Type.__name__=_E
_PmvoaCfgLabelclientIndex_Object=MibTableColumn
pmvoaCfgLabelclientIndex=_PmvoaCfgLabelclientIndex_Object((1,3,6,1,4,1,20044,84,9,2,1,1,1),_PmvoaCfgLabelclientIndex_Type())
pmvoaCfgLabelclientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaCfgLabelclientIndex.setStatus(_A)
class _PmvoaCfgLabelclientPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_PmvoaCfgLabelclientPortn_Type.__name__=_H
_PmvoaCfgLabelclientPortn_Object=MibTableColumn
pmvoaCfgLabelclientPortn=_PmvoaCfgLabelclientPortn_Object((1,3,6,1,4,1,20044,84,9,2,1,1,3),_PmvoaCfgLabelclientPortn_Type())
pmvoaCfgLabelclientPortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCfgLabelclientPortn.setStatus(_A)
_PmvoaCfgLabellineTable_Object=MibTable
pmvoaCfgLabellineTable=_PmvoaCfgLabellineTable_Object((1,3,6,1,4,1,20044,84,9,2,2))
if mibBuilder.loadTexts:pmvoaCfgLabellineTable.setStatus(_A)
_PmvoaCfgLabellineEntry_Object=MibTableRow
pmvoaCfgLabellineEntry=_PmvoaCfgLabellineEntry_Object((1,3,6,1,4,1,20044,84,9,2,2,1))
pmvoaCfgLabellineEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:pmvoaCfgLabellineEntry.setStatus(_A)
class _PmvoaCfgLabellineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmvoaCfgLabellineIndex_Type.__name__=_E
_PmvoaCfgLabellineIndex_Object=MibTableColumn
pmvoaCfgLabellineIndex=_PmvoaCfgLabellineIndex_Object((1,3,6,1,4,1,20044,84,9,2,2,1,1),_PmvoaCfgLabellineIndex_Type())
pmvoaCfgLabellineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoaCfgLabellineIndex.setStatus(_A)
class _PmvoaCfgLabellinePortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_PmvoaCfgLabellinePortn_Type.__name__=_H
_PmvoaCfgLabellinePortn_Object=MibTableColumn
pmvoaCfgLabellinePortn=_PmvoaCfgLabellinePortn_Object((1,3,6,1,4,1,20044,84,9,2,2,1,3),_PmvoaCfgLabellinePortn_Type())
pmvoaCfgLabellinePortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCfgLabellinePortn.setStatus(_A)
_PmvoaCfgWriteConfiguration_Type=EkiOnOff
_PmvoaCfgWriteConfiguration_Object=MibScalar
pmvoaCfgWriteConfiguration=_PmvoaCfgWriteConfiguration_Object((1,3,6,1,4,1,20044,84,9,257),_PmvoaCfgWriteConfiguration_Type())
pmvoaCfgWriteConfiguration.setMaxAccess(_C)
if mibBuilder.loadTexts:pmvoaCfgWriteConfiguration.setStatus(_A)
_Pmvoatraps_ObjectIdentity=ObjectIdentity
pmvoatraps=_Pmvoatraps_ObjectIdentity((1,3,6,1,4,1,20044,84,10))
class _PmvoatrapPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_PmvoatrapPortNumber_Type.__name__=_E
_PmvoatrapPortNumber_Object=MibScalar
pmvoatrapPortNumber=_PmvoatrapPortNumber_Object((1,3,6,1,4,1,20044,84,10,2),_PmvoatrapPortNumber_Type())
pmvoatrapPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoatrapPortNumber.setStatus(_A)
class _PmvoatrapLineNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_PmvoatrapLineNumber_Type.__name__=_E
_PmvoatrapLineNumber_Object=MibScalar
pmvoatrapLineNumber=_PmvoatrapLineNumber_Object((1,3,6,1,4,1,20044,84,10,3),_PmvoatrapLineNumber_Type())
pmvoatrapLineNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoatrapLineNumber.setStatus(_A)
class _PmvoatrapBoardNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_PmvoatrapBoardNumber_Type.__name__=_E
_PmvoatrapBoardNumber_Object=MibScalar
pmvoatrapBoardNumber=_PmvoatrapBoardNumber_Object((1,3,6,1,4,1,20044,84,10,4),_PmvoatrapBoardNumber_Type())
pmvoatrapBoardNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmvoatrapBoardNumber.setStatus(_A)
pmvoaLineTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,84,10,34))
pmvoaLineTrapCritGoesOn.setObjects(*((_D,_I),(_D,_J),(_D,_K),(_D,_G)))
if mibBuilder.loadTexts:pmvoaLineTrapCritGoesOn.setStatus(_A)
pmvoaLineTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,84,10,35))
pmvoaLineTrapCritGoesOff.setObjects(*((_D,_I),(_D,_J),(_D,_K),(_D,_G)))
if mibBuilder.loadTexts:pmvoaLineTrapCritGoesOff.setStatus(_A)
pmvoaPowerTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,84,10,50))
pmvoaPowerTrapUrgentGoesOn.setObjects(*((_D,_L),(_D,_M),(_D,_G)))
if mibBuilder.loadTexts:pmvoaPowerTrapUrgentGoesOn.setStatus(_A)
pmvoaPowerTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,84,10,51))
pmvoaPowerTrapUrgentGoesOff.setObjects(*((_D,_L),(_D,_M),(_D,_G)))
if mibBuilder.loadTexts:pmvoaPowerTrapUrgentGoesOff.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'PmvoaMode':PmvoaMode,'modulePmvoa':modulePmvoa,'pmvoaalarms':pmvoaalarms,'pmvoaAlmOther':pmvoaAlmOther,'pmvoaAlmOtherNurg':pmvoaAlmOtherNurg,'pmvoaAlmsynthAlm2':pmvoaAlmsynthAlm2,'pmvoaAlmConfTableSave':pmvoaAlmConfTableSave,'pmvoaAlmInvUpload':pmvoaAlmInvUpload,'pmvoaAlmConfTableLoad':pmvoaAlmConfTableLoad,'pmvoaAlmCorrelatOff':pmvoaAlmCorrelatOff,'pmvoaAlmOtherUrg':pmvoaAlmOtherUrg,'pmvoaAlmOtherCrit':pmvoaAlmOtherCrit,'pmvoaAlmsynthAlm0':pmvoaAlmsynthAlm0,'pmvoaAlmModGlobFail':pmvoaAlmModGlobFail,_M:pmvoaAlmDefFuseA,_L:pmvoaAlmDefFuseB,'pmvoaAlmClient':pmvoaAlmClient,'pmvoaAlmClientNurg':pmvoaAlmClientNurg,'pmvoaAlmClientUrg':pmvoaAlmClientUrg,'pmvoaAlmClientCrit':pmvoaAlmClientCrit,'pmvoaAlmLine':pmvoaAlmLine,'pmvoaAlmLineNurg':pmvoaAlmLineNurg,'pmvoaAlmLineUrg':pmvoaAlmLineUrg,'pmvoaAlmLineCrit':pmvoaAlmLineCrit,'pmvoaAlmsynthAlmLineTable':pmvoaAlmsynthAlmLineTable,'pmvoaAlmsynthAlmLineEntry':pmvoaAlmsynthAlmLineEntry,_N:pmvoaAlmsynthAlmLineIndex,'pmvoaAlmLineSfpVoaAbsentPortn':pmvoaAlmLineSfpVoaAbsentPortn,_J:pmvoaAlmLineHwFailPortn,'pmvoaAlmLineOosPortn':pmvoaAlmLineOosPortn,_I:pmvoaAlmLineFailPortn,'pmvoaAlmlineAlmTable':pmvoaAlmlineAlmTable,'pmvoaAlmlineAlmEntry':pmvoaAlmlineAlmEntry,_O:pmvoaAlmlineAlmIndex,'pmvoaAlmOutputErrorPortn':pmvoaAlmOutputErrorPortn,'pmvoaAlmLossOutputPowerPortn':pmvoaAlmLossOutputPowerPortn,'pmvoaAlmTempHighAlarmPortn':pmvoaAlmTempHighAlarmPortn,'pmvoaAlmTempLowAlarmPortn':pmvoaAlmTempLowAlarmPortn,'pmvoaAlmLossInputPowerPortn':pmvoaAlmLossInputPowerPortn,'pmvoameasures':pmvoameasures,'pmvoaMesrOther':pmvoaMesrOther,'pmvoaMesrClient':pmvoaMesrClient,'pmvoaMesrLine':pmvoaMesrLine,'pmvoaMesrlineSfpTempTable':pmvoaMesrlineSfpTempTable,'pmvoaMesrlineSfpTempEntry':pmvoaMesrlineSfpTempEntry,_P:pmvoaMesrlineSfpTempIndex,'pmvoaMesrlineSfpTempPortn':pmvoaMesrlineSfpTempPortn,'pmvoaMesrlinePoutTable':pmvoaMesrlinePoutTable,'pmvoaMesrlinePoutEntry':pmvoaMesrlinePoutEntry,_Q:pmvoaMesrlinePoutIndex,'pmvoaMesrlinePoutPortn':pmvoaMesrlinePoutPortn,'pmvoaMesrlineEstPinTable':pmvoaMesrlineEstPinTable,'pmvoaMesrlineEstPinEntry':pmvoaMesrlineEstPinEntry,_R:pmvoaMesrlineEstPinIndex,'pmvoaMesrlineEstPinPortn':pmvoaMesrlineEstPinPortn,'pmvoacontrolsWrite':pmvoacontrolsWrite,'pmvoaCtrlOther':pmvoaCtrlOther,'pmvoaCtrlconfMgnt1':pmvoaCtrlconfMgnt1,'pmvoaCtrlConf1Load1':pmvoaCtrlConf1Load1,'pmvoaCtrlConf2Load1':pmvoaCtrlConf2Load1,'pmvoaCtrlConf2Flash1':pmvoaCtrlConf2Flash1,'pmvoaCtrlConf2Clear1':pmvoaCtrlConf2Clear1,'pmvoaCtrlsynth4':pmvoaCtrlsynth4,'pmvoaCtrlCorrelatOn':pmvoaCtrlCorrelatOn,'pmvoaCtrlCorrelatOff':pmvoaCtrlCorrelatOff,'pmvoaCtrlswMgnt':pmvoaCtrlswMgnt,'pmvoaCtrlColdReset':pmvoaCtrlColdReset,'pmvoaCtrlWarmReset':pmvoaCtrlWarmReset,'pmvoaCtrlLoadSwBank1':pmvoaCtrlLoadSwBank1,'pmvoaCtrlLoadSwBank2':pmvoaCtrlLoadSwBank2,'pmvoaCtrlgwMgnt':pmvoaCtrlgwMgnt,'pmvoaCtrlCurrentGwReset':pmvoaCtrlCurrentGwReset,'pmvoaCtrlLoadGwBank1':pmvoaCtrlLoadGwBank1,'pmvoaCtrlLoadGwBank2':pmvoaCtrlLoadGwBank2,'pmvoaCtrlLoadGwBank3':pmvoaCtrlLoadGwBank3,'pmvoaCtrlLoadGwBank4':pmvoaCtrlLoadGwBank4,'pmvoaCtrlledTest':pmvoaCtrlledTest,'pmvoaCtrlGreenLed':pmvoaCtrlGreenLed,'pmvoaCtrlRedLed':pmvoaCtrlRedLed,'pmvoaCtrlLedOff':pmvoaCtrlLedOff,'pmvoaCtrlClient':pmvoaCtrlClient,'pmvoaCtrlLine':pmvoaCtrlLine,'pmvoari':pmvoari,'pmvoariTable':pmvoariTable,'pmvoaRinvLineTable':pmvoaRinvLineTable,'pmvoaRinvLineEntry':pmvoaRinvLineEntry,_S:pmvoaRinvLineIndex,'pmvoaRinvxfpLine':pmvoaRinvxfpLine,'pmvoaRinvReloadInventory':pmvoaRinvReloadInventory,'pmvoaRinvHwPlatform':pmvoaRinvHwPlatform,'pmvoaRinvModulePlatform':pmvoaRinvModulePlatform,'pmvoaRinvSwPlatform':pmvoaRinvSwPlatform,'pmvoaRinvGwPlatform':pmvoaRinvGwPlatform,'pmvoadownload':pmvoadownload,'pmvoaDwlOther':pmvoaDwlOther,'pmvoaDwlrestartProcess':pmvoaDwlrestartProcess,'pmvoaDwlWarmRestartProcessed':pmvoaDwlWarmRestartProcessed,'pmvoaDwlColdRestartProcessed':pmvoaDwlColdRestartProcessed,'pmvoaDwlswBanksUsed':pmvoaDwlswBanksUsed,'pmvoaDwlSwBank1Used':pmvoaDwlSwBank1Used,'pmvoaDwlSwBank2Used':pmvoaDwlSwBank2Used,'pmvoaDwlSwBank1Notempty':pmvoaDwlSwBank1Notempty,'pmvoaDwlSwBank2Notempty':pmvoaDwlSwBank2Notempty,'pmvoaDwlgwBanksUsed':pmvoaDwlgwBanksUsed,'pmvoaDwlGwBank1Used':pmvoaDwlGwBank1Used,'pmvoaDwlGwBank2Used':pmvoaDwlGwBank2Used,'pmvoaDwlGwBank3Used':pmvoaDwlGwBank3Used,'pmvoaDwlGwBank4Used':pmvoaDwlGwBank4Used,'pmvoaDwlGwBank1Notempty':pmvoaDwlGwBank1Notempty,'pmvoaDwlGwBank2Notempty':pmvoaDwlGwBank2Notempty,'pmvoaDwlGwBank3Notempty':pmvoaDwlGwBank3Notempty,'pmvoaDwlGwBank4Notempty':pmvoaDwlGwBank4Notempty,'pmvoaDwlClient':pmvoaDwlClient,'pmvoaDwlLine':pmvoaDwlLine,'pmvoaConfig':pmvoaConfig,'pmvoaCfgStartup':pmvoaCfgStartup,'pmvoaCfgLinexr1StartupTable':pmvoaCfgLinexr1StartupTable,'pmvoaCfgLinexr1StartupEntry':pmvoaCfgLinexr1StartupEntry,_T:pmvoaCfgLinexr1StartupIndex,'pmvoaCfgSfpModePortn':pmvoaCfgSfpModePortn,'pmvoaCfgAttenuationCtrlPortn':pmvoaCfgAttenuationCtrlPortn,'pmvoaCfgPowerCtrlPortn':pmvoaCfgPowerCtrlPortn,'pmvoaCfgLosInputThresholdPortn':pmvoaCfgLosInputThresholdPortn,'pmvoaCfgInsertionLossValuePortn':pmvoaCfgInsertionLossValuePortn,'pmvoaCfgLabels':pmvoaCfgLabels,'pmvoaCfgLabelclientTable':pmvoaCfgLabelclientTable,'pmvoaCfgLabelclientEntry':pmvoaCfgLabelclientEntry,_U:pmvoaCfgLabelclientIndex,'pmvoaCfgLabelclientPortn':pmvoaCfgLabelclientPortn,'pmvoaCfgLabellineTable':pmvoaCfgLabellineTable,'pmvoaCfgLabellineEntry':pmvoaCfgLabellineEntry,_V:pmvoaCfgLabellineIndex,'pmvoaCfgLabellinePortn':pmvoaCfgLabellinePortn,'pmvoaCfgWriteConfiguration':pmvoaCfgWriteConfiguration,'pmvoatraps':pmvoatraps,'pmvoatrapPortNumber':pmvoatrapPortNumber,_K:pmvoatrapLineNumber,_G:pmvoatrapBoardNumber,'pmvoaLineTrapCritGoesOn':pmvoaLineTrapCritGoesOn,'pmvoaLineTrapCritGoesOff':pmvoaLineTrapCritGoesOff,'pmvoaPowerTrapUrgentGoesOn':pmvoaPowerTrapUrgentGoesOn,'pmvoaPowerTrapUrgentGoesOff':pmvoaPowerTrapUrgentGoesOff})