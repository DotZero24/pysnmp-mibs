_P='programEntryPIDIndex'
_O='programEntryPIDPEIndex'
_N='reserved'
_M='unknown'
_L='programEntryStatusIndex'
_K='programEntryControlIndex'
_J='Unsigned32'
_I='read-write'
_H='yes'
_G='no'
_F='not-accessible'
_E='CISCO-DMN-DSG-PRGMENTRY-MIB'
_D='DisplayString'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
ciscoDSGProgramEntry=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,4))
if mibBuilder.loadTexts:ciscoDSGProgramEntry.setRevisions(('2010-10-13 08:00','2010-08-30 11:00','2010-06-17 06:00','2010-05-25 16:30','2010-05-07 06:30','2010-03-22 05:00','2010-02-12 15:00','2009-11-22 15:00'))
_ProgramEntryTable_ObjectIdentity=ObjectIdentity
programEntryTable=_ProgramEntryTable_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,4,2))
_ProgramEntryControlTable_Object=MibTable
programEntryControlTable=_ProgramEntryControlTable_Object((1,3,6,1,4,1,1429,2,2,5,4,2,1))
if mibBuilder.loadTexts:programEntryControlTable.setStatus(_A)
_ProgramEntryControlEntry_Object=MibTableRow
programEntryControlEntry=_ProgramEntryControlEntry_Object((1,3,6,1,4,1,1429,2,2,5,4,2,1,1))
programEntryControlEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:programEntryControlEntry.setStatus(_A)
class _ProgramEntryControlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_ProgramEntryControlIndex_Type.__name__=_B
_ProgramEntryControlIndex_Object=MibTableColumn
programEntryControlIndex=_ProgramEntryControlIndex_Object((1,3,6,1,4,1,1429,2,2,5,4,2,1,1,1),_ProgramEntryControlIndex_Type())
programEntryControlIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:programEntryControlIndex.setStatus(_A)
class _ProgramEntryControlChNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ProgramEntryControlChNum_Type.__name__=_B
_ProgramEntryControlChNum_Object=MibTableColumn
programEntryControlChNum=_ProgramEntryControlChNum_Object((1,3,6,1,4,1,1429,2,2,5,4,2,1,1,2),_ProgramEntryControlChNum_Type())
programEntryControlChNum.setMaxAccess(_I)
if mibBuilder.loadTexts:programEntryControlChNum.setStatus(_A)
class _ProgramEntryControlChCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('switch',1),('up',2),('down',3),('last',4),('writeOnly',5)))
_ProgramEntryControlChCmd_Type.__name__=_B
_ProgramEntryControlChCmd_Object=MibTableColumn
programEntryControlChCmd=_ProgramEntryControlChCmd_Object((1,3,6,1,4,1,1429,2,2,5,4,2,1,1,4),_ProgramEntryControlChCmd_Type())
programEntryControlChCmd.setMaxAccess(_I)
if mibBuilder.loadTexts:programEntryControlChCmd.setStatus(_A)
class _ProgramEntryControlResourceId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_ProgramEntryControlResourceId_Type.__name__=_J
_ProgramEntryControlResourceId_Object=MibTableColumn
programEntryControlResourceId=_ProgramEntryControlResourceId_Object((1,3,6,1,4,1,1429,2,2,5,4,2,1,1,5),_ProgramEntryControlResourceId_Type())
programEntryControlResourceId.setMaxAccess(_I)
if mibBuilder.loadTexts:programEntryControlResourceId.setStatus(_A)
_ProgramEntryStatusTable_Object=MibTable
programEntryStatusTable=_ProgramEntryStatusTable_Object((1,3,6,1,4,1,1429,2,2,5,4,2,2))
if mibBuilder.loadTexts:programEntryStatusTable.setStatus(_A)
_ProgramEntryStatusEntry_Object=MibTableRow
programEntryStatusEntry=_ProgramEntryStatusEntry_Object((1,3,6,1,4,1,1429,2,2,5,4,2,2,1))
programEntryStatusEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:programEntryStatusEntry.setStatus(_A)
class _ProgramEntryStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_ProgramEntryStatusIndex_Type.__name__=_B
_ProgramEntryStatusIndex_Object=MibTableColumn
programEntryStatusIndex=_ProgramEntryStatusIndex_Object((1,3,6,1,4,1,1429,2,2,5,4,2,2,1,1),_ProgramEntryStatusIndex_Type())
programEntryStatusIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:programEntryStatusIndex.setStatus(_A)
class _ProgramEntryStatusChName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_ProgramEntryStatusChName_Type.__name__=_D
_ProgramEntryStatusChName_Object=MibTableColumn
programEntryStatusChName=_ProgramEntryStatusChName_Object((1,3,6,1,4,1,1429,2,2,5,4,2,2,1,2),_ProgramEntryStatusChName_Type())
programEntryStatusChName.setMaxAccess(_C)
if mibBuilder.loadTexts:programEntryStatusChName.setStatus(_A)
class _ProgramEntryStatusCAAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ProgramEntryStatusCAAuth_Type.__name__=_B
_ProgramEntryStatusCAAuth_Object=MibTableColumn
programEntryStatusCAAuth=_ProgramEntryStatusCAAuth_Object((1,3,6,1,4,1,1429,2,2,5,4,2,2,1,3),_ProgramEntryStatusCAAuth_Type())
programEntryStatusCAAuth.setMaxAccess(_C)
if mibBuilder.loadTexts:programEntryStatusCAAuth.setStatus(_A)
class _ProgramEntryStatusCAEncry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),('unkn',3)))
_ProgramEntryStatusCAEncry_Type.__name__=_B
_ProgramEntryStatusCAEncry_Object=MibTableColumn
programEntryStatusCAEncry=_ProgramEntryStatusCAEncry_Object((1,3,6,1,4,1,1429,2,2,5,4,2,2,1,4),_ProgramEntryStatusCAEncry_Type())
programEntryStatusCAEncry.setMaxAccess(_C)
if mibBuilder.loadTexts:programEntryStatusCAEncry.setStatus(_A)
class _ProgramEntryStatusCAScram_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ProgramEntryStatusCAScram_Type.__name__=_B
_ProgramEntryStatusCAScram_Object=MibTableColumn
programEntryStatusCAScram=_ProgramEntryStatusCAScram_Object((1,3,6,1,4,1,1429,2,2,5,4,2,2,1,5),_ProgramEntryStatusCAScram_Type())
programEntryStatusCAScram.setMaxAccess(_C)
if mibBuilder.loadTexts:programEntryStatusCAScram.setStatus(_A)
class _ProgramEntryStatusCAID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63)));namedValues=NamedValues(*((_M,1),('fta',2),('powervu',3),('biss1',4),('biss2',5),('biss3',6),('standardized',7),('canalplus',8),('ccett',9),('deutscheTel',10),('eurodec',11),('franceTel',12),('iredeto',13),('jerroldGi',14),('matraComm',15),('nds',16),('nokia',17),('norwegianTel',18),('ntl',19),('philips',20),('sony',21),('tandbergTv',22),('thomson',23),('tvCom',24),('hptCroatian',25),('hrtCroatian',26),('ibm',27),('nera',28),('betaTechnik',29),('kudelski',30),('titanIS',31),('telefonica',32),('stentor',33),('tadiranScopus',34),('barco',35),('starguideDN',36),('mentorDS',37),('european',38),('polycipher',39),('generalIns',40),('telemann',41),('cryptoworks',42),('tsinghua',43),('easycas',44),('alphacrypt',45),('dvnHoldings',46),('shanghaiADT',47),('shenzhenKing',48),('sky',49),('dreamcrypt',50),('thalescrypt',51),('runcom',52),('sidsa',53),('beijingCom',54),('latens',55),('xcrypt',56),('beijingDig',57),('widevineTec',58),('skTel',59),('enigmaSys',60),(_N,61),('ruscrypt',62),('other',63)))
_ProgramEntryStatusCAID_Type.__name__=_B
_ProgramEntryStatusCAID_Object=MibTableColumn
programEntryStatusCAID=_ProgramEntryStatusCAID_Object((1,3,6,1,4,1,1429,2,2,5,4,2,2,1,6),_ProgramEntryStatusCAID_Type())
programEntryStatusCAID.setMaxAccess(_C)
if mibBuilder.loadTexts:programEntryStatusCAID.setStatus(_A)
class _ProgramEntryStatusSRStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notStarted',1),('primary',2),('alternate',3)))
_ProgramEntryStatusSRStatus_Type.__name__=_B
_ProgramEntryStatusSRStatus_Object=MibTableColumn
programEntryStatusSRStatus=_ProgramEntryStatusSRStatus_Object((1,3,6,1,4,1,1429,2,2,5,4,2,2,1,7),_ProgramEntryStatusSRStatus_Type())
programEntryStatusSRStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:programEntryStatusSRStatus.setStatus(_A)
class _ProgramEntryStatusSRType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('scheduled',2),('ca',3),('cuetrigger',4)))
_ProgramEntryStatusSRType_Type.__name__=_B
_ProgramEntryStatusSRType_Object=MibTableColumn
programEntryStatusSRType=_ProgramEntryStatusSRType_Object((1,3,6,1,4,1,1429,2,2,5,4,2,2,1,8),_ProgramEntryStatusSRType_Type())
programEntryStatusSRType.setMaxAccess(_C)
if mibBuilder.loadTexts:programEntryStatusSRType.setStatus(_A)
class _ProgramEntryStatusSRStartTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ProgramEntryStatusSRStartTime_Type.__name__=_D
_ProgramEntryStatusSRStartTime_Object=MibTableColumn
programEntryStatusSRStartTime=_ProgramEntryStatusSRStartTime_Object((1,3,6,1,4,1,1429,2,2,5,4,2,2,1,9),_ProgramEntryStatusSRStartTime_Type())
programEntryStatusSRStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:programEntryStatusSRStartTime.setStatus(_A)
class _ProgramEntryStatusSREndTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ProgramEntryStatusSREndTime_Type.__name__=_D
_ProgramEntryStatusSREndTime_Object=MibTableColumn
programEntryStatusSREndTime=_ProgramEntryStatusSREndTime_Object((1,3,6,1,4,1,1429,2,2,5,4,2,2,1,10),_ProgramEntryStatusSREndTime_Type())
programEntryStatusSREndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:programEntryStatusSREndTime.setStatus(_A)
class _ProgramEntryStatusPRGMStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_ProgramEntryStatusPRGMStatus_Type.__name__=_B
_ProgramEntryStatusPRGMStatus_Object=MibTableColumn
programEntryStatusPRGMStatus=_ProgramEntryStatusPRGMStatus_Object((1,3,6,1,4,1,1429,2,2,5,4,2,2,1,11),_ProgramEntryStatusPRGMStatus_Type())
programEntryStatusPRGMStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:programEntryStatusPRGMStatus.setStatus(_A)
class _ProgramEntryStatusPMTPID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ProgramEntryStatusPMTPID_Type.__name__=_D
_ProgramEntryStatusPMTPID_Object=MibTableColumn
programEntryStatusPMTPID=_ProgramEntryStatusPMTPID_Object((1,3,6,1,4,1,1429,2,2,5,4,2,2,1,12),_ProgramEntryStatusPMTPID_Type())
programEntryStatusPMTPID.setMaxAccess(_C)
if mibBuilder.loadTexts:programEntryStatusPMTPID.setStatus(_A)
class _ProgramEntryStatusPCRPID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ProgramEntryStatusPCRPID_Type.__name__=_D
_ProgramEntryStatusPCRPID_Object=MibTableColumn
programEntryStatusPCRPID=_ProgramEntryStatusPCRPID_Object((1,3,6,1,4,1,1429,2,2,5,4,2,2,1,13),_ProgramEntryStatusPCRPID_Type())
programEntryStatusPCRPID.setMaxAccess(_C)
if mibBuilder.loadTexts:programEntryStatusPCRPID.setStatus(_A)
_ProgramEntryPIDTable_Object=MibTable
programEntryPIDTable=_ProgramEntryPIDTable_Object((1,3,6,1,4,1,1429,2,2,5,4,2,3))
if mibBuilder.loadTexts:programEntryPIDTable.setStatus(_A)
_ProgramEntryPIDEntry_Object=MibTableRow
programEntryPIDEntry=_ProgramEntryPIDEntry_Object((1,3,6,1,4,1,1429,2,2,5,4,2,3,1))
programEntryPIDEntry.setIndexNames((0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:programEntryPIDEntry.setStatus(_A)
class _ProgramEntryPIDPEIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,138))
_ProgramEntryPIDPEIndex_Type.__name__=_B
_ProgramEntryPIDPEIndex_Object=MibTableColumn
programEntryPIDPEIndex=_ProgramEntryPIDPEIndex_Object((1,3,6,1,4,1,1429,2,2,5,4,2,3,1,1),_ProgramEntryPIDPEIndex_Type())
programEntryPIDPEIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:programEntryPIDPEIndex.setStatus(_A)
class _ProgramEntryPIDIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,138))
_ProgramEntryPIDIndex_Type.__name__=_B
_ProgramEntryPIDIndex_Object=MibTableColumn
programEntryPIDIndex=_ProgramEntryPIDIndex_Object((1,3,6,1,4,1,1429,2,2,5,4,2,3,1,2),_ProgramEntryPIDIndex_Type())
programEntryPIDIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:programEntryPIDIndex.setStatus(_A)
class _ProgramEntryPIDTypeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ProgramEntryPIDTypeName_Type.__name__=_D
_ProgramEntryPIDTypeName_Object=MibTableColumn
programEntryPIDTypeName=_ProgramEntryPIDTypeName_Object((1,3,6,1,4,1,1429,2,2,5,4,2,3,1,3),_ProgramEntryPIDTypeName_Type())
programEntryPIDTypeName.setMaxAccess(_C)
if mibBuilder.loadTexts:programEntryPIDTypeName.setStatus(_A)
class _ProgramEntryPIDTypeDetail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42)));namedValues=NamedValues(*(('pcr',1),('mpg1Vid',2),('mpg2Vid',3),('hdVid',4),('mpg4Vid',5),('iso422Vid',6),('h264Vid',7),('mpgAudL1',8),('mpg2AudL1',9),('mpgAudL2',10),('mpg2AudL2',11),('mpg4Aud',12),('dvbDolbyDigital',13),('dvbDolbyDigitalPlus',14),('atscDolbyDigital',15),('atscDolbyDigitalPlus',16),('aacLsAud',17),('haacLoAud',18),('haacAdAud',19),('dbeAud',20),('dtsAud',21),('dvbSubt',22),('saSubt',23),('dvbVbi',24),('saVbi',25),('dvbTtx',26),('scteDpi',27),('dvbMpe',28),('dvbAsyn',29),('dvbSyns',30),('dvbSynd',31),('dvbDcar',32),('dvbOcar',33),('saUtld',34),('saHsd',35),('saWbd',36),('saCddl',37),('ecm',38),('emm',39),('pmt',40),(_M,41),(_N,42)))
_ProgramEntryPIDTypeDetail_Type.__name__=_B
_ProgramEntryPIDTypeDetail_Object=MibTableColumn
programEntryPIDTypeDetail=_ProgramEntryPIDTypeDetail_Object((1,3,6,1,4,1,1429,2,2,5,4,2,3,1,4),_ProgramEntryPIDTypeDetail_Type())
programEntryPIDTypeDetail.setMaxAccess(_C)
if mibBuilder.loadTexts:programEntryPIDTypeDetail.setStatus(_A)
class _ProgramEntryPIDValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ProgramEntryPIDValue_Type.__name__=_D
_ProgramEntryPIDValue_Object=MibTableColumn
programEntryPIDValue=_ProgramEntryPIDValue_Object((1,3,6,1,4,1,1429,2,2,5,4,2,3,1,5),_ProgramEntryPIDValue_Type())
programEntryPIDValue.setMaxAccess(_C)
if mibBuilder.loadTexts:programEntryPIDValue.setStatus(_A)
class _ProgramEntryPIDPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ProgramEntryPIDPresent_Type.__name__=_B
_ProgramEntryPIDPresent_Object=MibTableColumn
programEntryPIDPresent=_ProgramEntryPIDPresent_Object((1,3,6,1,4,1,1429,2,2,5,4,2,3,1,6),_ProgramEntryPIDPresent_Type())
programEntryPIDPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:programEntryPIDPresent.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ciscoDSGProgramEntry':ciscoDSGProgramEntry,'programEntryTable':programEntryTable,'programEntryControlTable':programEntryControlTable,'programEntryControlEntry':programEntryControlEntry,_K:programEntryControlIndex,'programEntryControlChNum':programEntryControlChNum,'programEntryControlChCmd':programEntryControlChCmd,'programEntryControlResourceId':programEntryControlResourceId,'programEntryStatusTable':programEntryStatusTable,'programEntryStatusEntry':programEntryStatusEntry,_L:programEntryStatusIndex,'programEntryStatusChName':programEntryStatusChName,'programEntryStatusCAAuth':programEntryStatusCAAuth,'programEntryStatusCAEncry':programEntryStatusCAEncry,'programEntryStatusCAScram':programEntryStatusCAScram,'programEntryStatusCAID':programEntryStatusCAID,'programEntryStatusSRStatus':programEntryStatusSRStatus,'programEntryStatusSRType':programEntryStatusSRType,'programEntryStatusSRStartTime':programEntryStatusSRStartTime,'programEntryStatusSREndTime':programEntryStatusSREndTime,'programEntryStatusPRGMStatus':programEntryStatusPRGMStatus,'programEntryStatusPMTPID':programEntryStatusPMTPID,'programEntryStatusPCRPID':programEntryStatusPCRPID,'programEntryPIDTable':programEntryPIDTable,'programEntryPIDEntry':programEntryPIDEntry,_O:programEntryPIDPEIndex,_P:programEntryPIDIndex,'programEntryPIDTypeName':programEntryPIDTypeName,'programEntryPIDTypeDetail':programEntryPIDTypeDetail,'programEntryPIDValue':programEntryPIDValue,'programEntryPIDPresent':programEntryPIDPresent})