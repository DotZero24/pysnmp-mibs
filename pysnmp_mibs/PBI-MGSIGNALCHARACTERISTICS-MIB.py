_M='channelBAT'
_L='channelInputCAT'
_K='channelInputFilter'
_J='channelInputSDT'
_I='channelInputNIT'
_H='channelInputPMT'
_G='channelInputPAT'
_F='channelOutput'
_E='Integer32'
_D='PBI-MGSIGNALCHARACTERISTICS-MIB'
_C='DisplayString'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mg,=mibBuilder.importSymbols('PBI-MAIN-MIB','mg')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','RowStatus','TextualConvention')
mgSignalCharacteristics=ModuleIdentity((1,3,6,1,4,1,1070,3,2))
if mibBuilder.loadTexts:mgSignalCharacteristics.setRevisions(('2006-09-21 09:24',))
_TsOutTable_Object=MibTable
tsOutTable=_TsOutTable_Object((1,3,6,1,4,1,1070,3,2,1))
if mibBuilder.loadTexts:tsOutTable.setStatus(_A)
_TsOutEntry_Object=MibTableRow
tsOutEntry=_TsOutEntry_Object((1,3,6,1,4,1,1070,3,2,1,1))
tsOutEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:tsOutEntry.setStatus(_A)
_ChannelOutput_Type=Integer32
_ChannelOutput_Object=MibTableColumn
channelOutput=_ChannelOutput_Object((1,3,6,1,4,1,1070,3,2,1,1,1),_ChannelOutput_Type())
channelOutput.setMaxAccess(_B)
if mibBuilder.loadTexts:channelOutput.setStatus(_A)
_BitRate_Type=Integer32
_BitRate_Object=MibTableColumn
bitRate=_BitRate_Object((1,3,6,1,4,1,1070,3,2,1,1,2),_BitRate_Type())
bitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:bitRate.setStatus(_A)
_PacketSize_Type=Integer32
_PacketSize_Object=MibTableColumn
packetSize=_PacketSize_Object((1,3,6,1,4,1,1070,3,2,1,1,3),_PacketSize_Type())
packetSize.setMaxAccess(_B)
if mibBuilder.loadTexts:packetSize.setStatus(_A)
_TransportStreamID_Type=Integer32
_TransportStreamID_Object=MibTableColumn
transportStreamID=_TransportStreamID_Object((1,3,6,1,4,1,1070,3,2,1,1,4),_TransportStreamID_Type())
transportStreamID.setMaxAccess(_B)
if mibBuilder.loadTexts:transportStreamID.setStatus(_A)
_OtiginalNetworkID_Type=Integer32
_OtiginalNetworkID_Object=MibTableColumn
otiginalNetworkID=_OtiginalNetworkID_Object((1,3,6,1,4,1,1070,3,2,1,1,5),_OtiginalNetworkID_Type())
otiginalNetworkID.setMaxAccess(_B)
if mibBuilder.loadTexts:otiginalNetworkID.setStatus(_A)
_NetworkID_Type=Integer32
_NetworkID_Object=MibTableColumn
networkID=_NetworkID_Object((1,3,6,1,4,1,1070,3,2,1,1,6),_NetworkID_Type())
networkID.setMaxAccess(_B)
if mibBuilder.loadTexts:networkID.setStatus(_A)
_BitrateThreshosdPercent_Type=Integer32
_BitrateThreshosdPercent_Object=MibTableColumn
bitrateThreshosdPercent=_BitrateThreshosdPercent_Object((1,3,6,1,4,1,1070,3,2,1,1,7),_BitrateThreshosdPercent_Type())
bitrateThreshosdPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:bitrateThreshosdPercent.setStatus(_A)
_OutValidBitRate_Type=Integer32
_OutValidBitRate_Object=MibTableColumn
outValidBitRate=_OutValidBitRate_Object((1,3,6,1,4,1,1070,3,2,1,1,8),_OutValidBitRate_Type())
outValidBitRate.setMaxAccess('read-only')
if mibBuilder.loadTexts:outValidBitRate.setStatus(_A)
_MgPATTable_Object=MibTable
mgPATTable=_MgPATTable_Object((1,3,6,1,4,1,1070,3,2,2))
if mibBuilder.loadTexts:mgPATTable.setStatus(_A)
_MgPATEntry_Object=MibTableRow
mgPATEntry=_MgPATEntry_Object((1,3,6,1,4,1,1070,3,2,2,1))
mgPATEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:mgPATEntry.setStatus(_A)
class _ChannelInputPAT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_ChannelInputPAT_Type.__name__=_E
_ChannelInputPAT_Object=MibTableColumn
channelInputPAT=_ChannelInputPAT_Object((1,3,6,1,4,1,1070,3,2,2,1,1),_ChannelInputPAT_Type())
channelInputPAT.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInputPAT.setStatus(_A)
class _PatSection_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_PatSection_Type.__name__=_C
_PatSection_Object=MibTableColumn
patSection=_PatSection_Object((1,3,6,1,4,1,1070,3,2,2,1,2),_PatSection_Type())
patSection.setMaxAccess(_B)
if mibBuilder.loadTexts:patSection.setStatus(_A)
_MgPMTTable_Object=MibTable
mgPMTTable=_MgPMTTable_Object((1,3,6,1,4,1,1070,3,2,3))
if mibBuilder.loadTexts:mgPMTTable.setStatus(_A)
_MgPMTEntry_Object=MibTableRow
mgPMTEntry=_MgPMTEntry_Object((1,3,6,1,4,1,1070,3,2,3,1))
mgPMTEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:mgPMTEntry.setStatus(_A)
_ChannelInputPMT_Type=Integer32
_ChannelInputPMT_Object=MibTableColumn
channelInputPMT=_ChannelInputPMT_Object((1,3,6,1,4,1,1070,3,2,3,1,1),_ChannelInputPMT_Type())
channelInputPMT.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInputPMT.setStatus(_A)
_PmtProgramNumber_Type=Integer32
_PmtProgramNumber_Object=MibTableColumn
pmtProgramNumber=_PmtProgramNumber_Object((1,3,6,1,4,1,1070,3,2,3,1,2),_PmtProgramNumber_Type())
pmtProgramNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmtProgramNumber.setStatus(_A)
_PmtPID_Type=Integer32
_PmtPID_Object=MibTableColumn
pmtPID=_PmtPID_Object((1,3,6,1,4,1,1070,3,2,3,1,3),_PmtPID_Type())
pmtPID.setMaxAccess(_B)
if mibBuilder.loadTexts:pmtPID.setStatus(_A)
class _PmtSection_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_PmtSection_Type.__name__=_C
_PmtSection_Object=MibTableColumn
pmtSection=_PmtSection_Object((1,3,6,1,4,1,1070,3,2,3,1,4),_PmtSection_Type())
pmtSection.setMaxAccess(_B)
if mibBuilder.loadTexts:pmtSection.setStatus(_A)
_MgNITTable_Object=MibTable
mgNITTable=_MgNITTable_Object((1,3,6,1,4,1,1070,3,2,4))
if mibBuilder.loadTexts:mgNITTable.setStatus(_A)
_MgNITEntry_Object=MibTableRow
mgNITEntry=_MgNITEntry_Object((1,3,6,1,4,1,1070,3,2,4,1))
mgNITEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:mgNITEntry.setStatus(_A)
_ChannelInputNIT_Type=Integer32
_ChannelInputNIT_Object=MibTableColumn
channelInputNIT=_ChannelInputNIT_Object((1,3,6,1,4,1,1070,3,2,4,1,1),_ChannelInputNIT_Type())
channelInputNIT.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInputNIT.setStatus(_A)
_NetworkType_Type=Integer32
_NetworkType_Object=MibTableColumn
networkType=_NetworkType_Object((1,3,6,1,4,1,1070,3,2,4,1,2),_NetworkType_Type())
networkType.setMaxAccess(_B)
if mibBuilder.loadTexts:networkType.setStatus(_A)
class _NitActualSection_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_NitActualSection_Type.__name__=_C
_NitActualSection_Object=MibTableColumn
nitActualSection=_NitActualSection_Object((1,3,6,1,4,1,1070,3,2,4,1,3),_NitActualSection_Type())
nitActualSection.setMaxAccess(_B)
if mibBuilder.loadTexts:nitActualSection.setStatus(_A)
class _NitOhtersSection_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_NitOhtersSection_Type.__name__=_C
_NitOhtersSection_Object=MibTableColumn
nitOhtersSection=_NitOhtersSection_Object((1,3,6,1,4,1,1070,3,2,4,1,4),_NitOhtersSection_Type())
nitOhtersSection.setMaxAccess(_B)
if mibBuilder.loadTexts:nitOhtersSection.setStatus(_A)
_MgSDTTable_Object=MibTable
mgSDTTable=_MgSDTTable_Object((1,3,6,1,4,1,1070,3,2,5))
if mibBuilder.loadTexts:mgSDTTable.setStatus(_A)
_MgSDTEntry_Object=MibTableRow
mgSDTEntry=_MgSDTEntry_Object((1,3,6,1,4,1,1070,3,2,5,1))
mgSDTEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:mgSDTEntry.setStatus(_A)
_ChannelInputSDT_Type=Integer32
_ChannelInputSDT_Object=MibTableColumn
channelInputSDT=_ChannelInputSDT_Object((1,3,6,1,4,1,1070,3,2,5,1,1),_ChannelInputSDT_Type())
channelInputSDT.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInputSDT.setStatus(_A)
class _SdtSection_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_SdtSection_Type.__name__=_C
_SdtSection_Object=MibTableColumn
sdtSection=_SdtSection_Object((1,3,6,1,4,1,1070,3,2,5,1,2),_SdtSection_Type())
sdtSection.setMaxAccess(_B)
if mibBuilder.loadTexts:sdtSection.setStatus(_A)
_MgFilterTable_Object=MibTable
mgFilterTable=_MgFilterTable_Object((1,3,6,1,4,1,1070,3,2,6))
if mibBuilder.loadTexts:mgFilterTable.setStatus(_A)
_MgFilterEntry_Object=MibTableRow
mgFilterEntry=_MgFilterEntry_Object((1,3,6,1,4,1,1070,3,2,6,1))
mgFilterEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:mgFilterEntry.setStatus(_A)
_ChannelInputFilter_Type=Integer32
_ChannelInputFilter_Object=MibTableColumn
channelInputFilter=_ChannelInputFilter_Object((1,3,6,1,4,1,1070,3,2,6,1,1),_ChannelInputFilter_Type())
channelInputFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInputFilter.setStatus(_A)
class _OldPID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_OldPID_Type.__name__=_C
_OldPID_Object=MibTableColumn
oldPID=_OldPID_Object((1,3,6,1,4,1,1070,3,2,6,1,2),_OldPID_Type())
oldPID.setMaxAccess(_B)
if mibBuilder.loadTexts:oldPID.setStatus(_A)
class _NewPID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_NewPID_Type.__name__=_C
_NewPID_Object=MibTableColumn
newPID=_NewPID_Object((1,3,6,1,4,1,1070,3,2,6,1,3),_NewPID_Type())
newPID.setMaxAccess(_B)
if mibBuilder.loadTexts:newPID.setStatus(_A)
class _OldProgramNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_OldProgramNumber_Type.__name__=_C
_OldProgramNumber_Object=MibTableColumn
oldProgramNumber=_OldProgramNumber_Object((1,3,6,1,4,1,1070,3,2,6,1,4),_OldProgramNumber_Type())
oldProgramNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oldProgramNumber.setStatus(_A)
class _NewProgramNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_NewProgramNumber_Type.__name__=_C
_NewProgramNumber_Object=MibTableColumn
newProgramNumber=_NewProgramNumber_Object((1,3,6,1,4,1,1070,3,2,6,1,5),_NewProgramNumber_Type())
newProgramNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:newProgramNumber.setStatus(_A)
_MgCATTable_Object=MibTable
mgCATTable=_MgCATTable_Object((1,3,6,1,4,1,1070,3,2,7))
if mibBuilder.loadTexts:mgCATTable.setStatus(_A)
_MgCATEntry_Object=MibTableRow
mgCATEntry=_MgCATEntry_Object((1,3,6,1,4,1,1070,3,2,7,1))
mgCATEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:mgCATEntry.setStatus(_A)
class _ChannelInputCAT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_ChannelInputCAT_Type.__name__=_E
_ChannelInputCAT_Object=MibTableColumn
channelInputCAT=_ChannelInputCAT_Object((1,3,6,1,4,1,1070,3,2,7,1,1),_ChannelInputCAT_Type())
channelInputCAT.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInputCAT.setStatus(_A)
class _CatSection_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CatSection_Type.__name__=_C
_CatSection_Object=MibTableColumn
catSection=_CatSection_Object((1,3,6,1,4,1,1070,3,2,7,1,2),_CatSection_Type())
catSection.setMaxAccess(_B)
if mibBuilder.loadTexts:catSection.setStatus(_A)
_TsInput_ObjectIdentity=ObjectIdentity
tsInput=_TsInput_ObjectIdentity((1,3,6,1,4,1,1070,3,2,8))
_ChannelInput_Type=Integer32
_ChannelInput_Object=MibScalar
channelInput=_ChannelInput_Object((1,3,6,1,4,1,1070,3,2,8,1),_ChannelInput_Type())
channelInput.setMaxAccess(_B)
if mibBuilder.loadTexts:channelInput.setStatus(_A)
_StateLock_Type=Integer32
_StateLock_Object=MibScalar
stateLock=_StateLock_Object((1,3,6,1,4,1,1070,3,2,8,2),_StateLock_Type())
stateLock.setMaxAccess(_B)
if mibBuilder.loadTexts:stateLock.setStatus(_A)
_TsIdPreference_Type=Integer32
_TsIdPreference_Object=MibScalar
tsIdPreference=_TsIdPreference_Object((1,3,6,1,4,1,1070,3,2,8,3),_TsIdPreference_Type())
tsIdPreference.setMaxAccess(_B)
if mibBuilder.loadTexts:tsIdPreference.setStatus(_A)
_MgBATTable_Object=MibTable
mgBATTable=_MgBATTable_Object((1,3,6,1,4,1,1070,3,2,9))
if mibBuilder.loadTexts:mgBATTable.setStatus(_A)
_MgBATEntry_Object=MibTableRow
mgBATEntry=_MgBATEntry_Object((1,3,6,1,4,1,1070,3,2,9,1))
mgBATEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:mgBATEntry.setStatus(_A)
_ChannelBAT_Type=Integer32
_ChannelBAT_Object=MibTableColumn
channelBAT=_ChannelBAT_Object((1,3,6,1,4,1,1070,3,2,9,1,1),_ChannelBAT_Type())
channelBAT.setMaxAccess(_B)
if mibBuilder.loadTexts:channelBAT.setStatus(_A)
class _BatSection_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_BatSection_Type.__name__=_C
_BatSection_Object=MibTableColumn
batSection=_BatSection_Object((1,3,6,1,4,1,1070,3,2,9,1,2),_BatSection_Type())
batSection.setMaxAccess(_B)
if mibBuilder.loadTexts:batSection.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'mgSignalCharacteristics':mgSignalCharacteristics,'tsOutTable':tsOutTable,'tsOutEntry':tsOutEntry,_F:channelOutput,'bitRate':bitRate,'packetSize':packetSize,'transportStreamID':transportStreamID,'otiginalNetworkID':otiginalNetworkID,'networkID':networkID,'bitrateThreshosdPercent':bitrateThreshosdPercent,'outValidBitRate':outValidBitRate,'mgPATTable':mgPATTable,'mgPATEntry':mgPATEntry,_G:channelInputPAT,'patSection':patSection,'mgPMTTable':mgPMTTable,'mgPMTEntry':mgPMTEntry,_H:channelInputPMT,'pmtProgramNumber':pmtProgramNumber,'pmtPID':pmtPID,'pmtSection':pmtSection,'mgNITTable':mgNITTable,'mgNITEntry':mgNITEntry,_I:channelInputNIT,'networkType':networkType,'nitActualSection':nitActualSection,'nitOhtersSection':nitOhtersSection,'mgSDTTable':mgSDTTable,'mgSDTEntry':mgSDTEntry,_J:channelInputSDT,'sdtSection':sdtSection,'mgFilterTable':mgFilterTable,'mgFilterEntry':mgFilterEntry,_K:channelInputFilter,'oldPID':oldPID,'newPID':newPID,'oldProgramNumber':oldProgramNumber,'newProgramNumber':newProgramNumber,'mgCATTable':mgCATTable,'mgCATEntry':mgCATEntry,_L:channelInputCAT,'catSection':catSection,'tsInput':tsInput,'channelInput':channelInput,'stateLock':stateLock,'tsIdPreference':tsIdPreference,'mgBATTable':mgBATTable,'mgBATEntry':mgBATEntry,_M:channelBAT,'batSection':batSection})