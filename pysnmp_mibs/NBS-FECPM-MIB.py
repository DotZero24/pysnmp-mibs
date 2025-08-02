_X='nbsFecpmCurrentUncorWords'
_W='nbsFecpmCurrentCorBit1to0'
_V='nbsFecpmCurrentCorBit0to1'
_U='nbsFecpmCurrentByteErrCor'
_T='nbsFecpmCurrentBitErrCor'
_S='nbsFecStatsIfIndex'
_R='nbsFecpmRunningIfIndex'
_Q='not-accessible'
_P='nbsFecpmHistoricSample'
_O='nbsFecpmHistoricInterval'
_N='nbsFecpmHistoricIfIndex'
_M='nbsFecpmThresholdsInterval'
_L='nbsFecpmThresholdsIfIndex'
_K='twentyfourHour'
_J='quarterHour'
_I='Integer32'
_H='read-write'
_G='ifAlias'
_F='IF-MIB'
_E='nbsFecpmCurrentInterval'
_D='nbsFecpmCurrentIfIndex'
_C='NBS-FECPM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifAlias=mibBuilder.importSymbols(_F,'InterfaceIndex',_G)
WritableU64,nbs=mibBuilder.importSymbols('NBS-MIB','WritableU64','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nbsFecpmMib=ModuleIdentity((1,3,6,1,4,1,629,223))
_NbsFecpmThresholdsGrp_ObjectIdentity=ObjectIdentity
nbsFecpmThresholdsGrp=_NbsFecpmThresholdsGrp_ObjectIdentity((1,3,6,1,4,1,629,223,1))
if mibBuilder.loadTexts:nbsFecpmThresholdsGrp.setStatus(_A)
_NbsFecpmThresholdsTable_Object=MibTable
nbsFecpmThresholdsTable=_NbsFecpmThresholdsTable_Object((1,3,6,1,4,1,629,223,1,1))
if mibBuilder.loadTexts:nbsFecpmThresholdsTable.setStatus(_A)
_NbsFecpmThresholdsEntry_Object=MibTableRow
nbsFecpmThresholdsEntry=_NbsFecpmThresholdsEntry_Object((1,3,6,1,4,1,629,223,1,1,1))
nbsFecpmThresholdsEntry.setIndexNames((0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:nbsFecpmThresholdsEntry.setStatus(_A)
_NbsFecpmThresholdsIfIndex_Type=InterfaceIndex
_NbsFecpmThresholdsIfIndex_Object=MibTableColumn
nbsFecpmThresholdsIfIndex=_NbsFecpmThresholdsIfIndex_Object((1,3,6,1,4,1,629,223,1,1,1,1),_NbsFecpmThresholdsIfIndex_Type())
nbsFecpmThresholdsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmThresholdsIfIndex.setStatus(_A)
class _NbsFecpmThresholdsInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_NbsFecpmThresholdsInterval_Type.__name__=_I
_NbsFecpmThresholdsInterval_Object=MibTableColumn
nbsFecpmThresholdsInterval=_NbsFecpmThresholdsInterval_Object((1,3,6,1,4,1,629,223,1,1,1,2),_NbsFecpmThresholdsInterval_Type())
nbsFecpmThresholdsInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmThresholdsInterval.setStatus(_A)
_NbsFecpmThresholdsBitErrCor_Type=WritableU64
_NbsFecpmThresholdsBitErrCor_Object=MibTableColumn
nbsFecpmThresholdsBitErrCor=_NbsFecpmThresholdsBitErrCor_Object((1,3,6,1,4,1,629,223,1,1,1,10),_NbsFecpmThresholdsBitErrCor_Type())
nbsFecpmThresholdsBitErrCor.setMaxAccess(_H)
if mibBuilder.loadTexts:nbsFecpmThresholdsBitErrCor.setStatus(_A)
_NbsFecpmThresholdsByteErrCor_Type=WritableU64
_NbsFecpmThresholdsByteErrCor_Object=MibTableColumn
nbsFecpmThresholdsByteErrCor=_NbsFecpmThresholdsByteErrCor_Object((1,3,6,1,4,1,629,223,1,1,1,12),_NbsFecpmThresholdsByteErrCor_Type())
nbsFecpmThresholdsByteErrCor.setMaxAccess(_H)
if mibBuilder.loadTexts:nbsFecpmThresholdsByteErrCor.setStatus(_A)
_NbsFecpmThresholdsCorBit0to1_Type=WritableU64
_NbsFecpmThresholdsCorBit0to1_Object=MibTableColumn
nbsFecpmThresholdsCorBit0to1=_NbsFecpmThresholdsCorBit0to1_Object((1,3,6,1,4,1,629,223,1,1,1,14),_NbsFecpmThresholdsCorBit0to1_Type())
nbsFecpmThresholdsCorBit0to1.setMaxAccess(_H)
if mibBuilder.loadTexts:nbsFecpmThresholdsCorBit0to1.setStatus(_A)
_NbsFecpmThresholdsCorBit1to0_Type=WritableU64
_NbsFecpmThresholdsCorBit1to0_Object=MibTableColumn
nbsFecpmThresholdsCorBit1to0=_NbsFecpmThresholdsCorBit1to0_Object((1,3,6,1,4,1,629,223,1,1,1,16),_NbsFecpmThresholdsCorBit1to0_Type())
nbsFecpmThresholdsCorBit1to0.setMaxAccess(_H)
if mibBuilder.loadTexts:nbsFecpmThresholdsCorBit1to0.setStatus(_A)
_NbsFecpmThresholdsUncorWords_Type=WritableU64
_NbsFecpmThresholdsUncorWords_Object=MibTableColumn
nbsFecpmThresholdsUncorWords=_NbsFecpmThresholdsUncorWords_Object((1,3,6,1,4,1,629,223,1,1,1,18),_NbsFecpmThresholdsUncorWords_Type())
nbsFecpmThresholdsUncorWords.setMaxAccess(_H)
if mibBuilder.loadTexts:nbsFecpmThresholdsUncorWords.setStatus(_A)
_NbsFecpmCurrentGrp_ObjectIdentity=ObjectIdentity
nbsFecpmCurrentGrp=_NbsFecpmCurrentGrp_ObjectIdentity((1,3,6,1,4,1,629,223,2))
if mibBuilder.loadTexts:nbsFecpmCurrentGrp.setStatus(_A)
_NbsFecpmCurrentSysDate_Type=Integer32
_NbsFecpmCurrentSysDate_Object=MibScalar
nbsFecpmCurrentSysDate=_NbsFecpmCurrentSysDate_Object((1,3,6,1,4,1,629,223,2,1),_NbsFecpmCurrentSysDate_Type())
nbsFecpmCurrentSysDate.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmCurrentSysDate.setStatus(_A)
_NbsFecpmCurrentSysTime_Type=Integer32
_NbsFecpmCurrentSysTime_Object=MibScalar
nbsFecpmCurrentSysTime=_NbsFecpmCurrentSysTime_Object((1,3,6,1,4,1,629,223,2,2),_NbsFecpmCurrentSysTime_Type())
nbsFecpmCurrentSysTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmCurrentSysTime.setStatus(_A)
_NbsFecpmCurrentTable_Object=MibTable
nbsFecpmCurrentTable=_NbsFecpmCurrentTable_Object((1,3,6,1,4,1,629,223,2,3))
if mibBuilder.loadTexts:nbsFecpmCurrentTable.setStatus(_A)
_NbsFecpmCurrentEntry_Object=MibTableRow
nbsFecpmCurrentEntry=_NbsFecpmCurrentEntry_Object((1,3,6,1,4,1,629,223,2,3,1))
nbsFecpmCurrentEntry.setIndexNames((0,_C,_D),(0,_C,_E))
if mibBuilder.loadTexts:nbsFecpmCurrentEntry.setStatus(_A)
_NbsFecpmCurrentIfIndex_Type=InterfaceIndex
_NbsFecpmCurrentIfIndex_Object=MibTableColumn
nbsFecpmCurrentIfIndex=_NbsFecpmCurrentIfIndex_Object((1,3,6,1,4,1,629,223,2,3,1,1),_NbsFecpmCurrentIfIndex_Type())
nbsFecpmCurrentIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmCurrentIfIndex.setStatus(_A)
class _NbsFecpmCurrentInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_NbsFecpmCurrentInterval_Type.__name__=_I
_NbsFecpmCurrentInterval_Object=MibTableColumn
nbsFecpmCurrentInterval=_NbsFecpmCurrentInterval_Object((1,3,6,1,4,1,629,223,2,3,1,2),_NbsFecpmCurrentInterval_Type())
nbsFecpmCurrentInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmCurrentInterval.setStatus(_A)
_NbsFecpmCurrentDate_Type=Integer32
_NbsFecpmCurrentDate_Object=MibTableColumn
nbsFecpmCurrentDate=_NbsFecpmCurrentDate_Object((1,3,6,1,4,1,629,223,2,3,1,5),_NbsFecpmCurrentDate_Type())
nbsFecpmCurrentDate.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmCurrentDate.setStatus(_A)
_NbsFecpmCurrentTime_Type=Integer32
_NbsFecpmCurrentTime_Object=MibTableColumn
nbsFecpmCurrentTime=_NbsFecpmCurrentTime_Object((1,3,6,1,4,1,629,223,2,3,1,6),_NbsFecpmCurrentTime_Type())
nbsFecpmCurrentTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmCurrentTime.setStatus(_A)
_NbsFecpmCurrentBitErrCor_Type=Counter64
_NbsFecpmCurrentBitErrCor_Object=MibTableColumn
nbsFecpmCurrentBitErrCor=_NbsFecpmCurrentBitErrCor_Object((1,3,6,1,4,1,629,223,2,3,1,10),_NbsFecpmCurrentBitErrCor_Type())
nbsFecpmCurrentBitErrCor.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmCurrentBitErrCor.setStatus(_A)
_NbsFecpmCurrentByteErrCor_Type=Counter64
_NbsFecpmCurrentByteErrCor_Object=MibTableColumn
nbsFecpmCurrentByteErrCor=_NbsFecpmCurrentByteErrCor_Object((1,3,6,1,4,1,629,223,2,3,1,12),_NbsFecpmCurrentByteErrCor_Type())
nbsFecpmCurrentByteErrCor.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmCurrentByteErrCor.setStatus(_A)
_NbsFecpmCurrentCorBit0to1_Type=Counter64
_NbsFecpmCurrentCorBit0to1_Object=MibTableColumn
nbsFecpmCurrentCorBit0to1=_NbsFecpmCurrentCorBit0to1_Object((1,3,6,1,4,1,629,223,2,3,1,14),_NbsFecpmCurrentCorBit0to1_Type())
nbsFecpmCurrentCorBit0to1.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmCurrentCorBit0to1.setStatus(_A)
_NbsFecpmCurrentCorBit1to0_Type=Counter64
_NbsFecpmCurrentCorBit1to0_Object=MibTableColumn
nbsFecpmCurrentCorBit1to0=_NbsFecpmCurrentCorBit1to0_Object((1,3,6,1,4,1,629,223,2,3,1,16),_NbsFecpmCurrentCorBit1to0_Type())
nbsFecpmCurrentCorBit1to0.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmCurrentCorBit1to0.setStatus(_A)
_NbsFecpmCurrentUncorWords_Type=Counter64
_NbsFecpmCurrentUncorWords_Object=MibTableColumn
nbsFecpmCurrentUncorWords=_NbsFecpmCurrentUncorWords_Object((1,3,6,1,4,1,629,223,2,3,1,18),_NbsFecpmCurrentUncorWords_Type())
nbsFecpmCurrentUncorWords.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmCurrentUncorWords.setStatus(_A)
_NbsFecpmHistoricGrp_ObjectIdentity=ObjectIdentity
nbsFecpmHistoricGrp=_NbsFecpmHistoricGrp_ObjectIdentity((1,3,6,1,4,1,629,223,3))
if mibBuilder.loadTexts:nbsFecpmHistoricGrp.setStatus(_A)
_NbsFecpmHistoricTable_Object=MibTable
nbsFecpmHistoricTable=_NbsFecpmHistoricTable_Object((1,3,6,1,4,1,629,223,3,3))
if mibBuilder.loadTexts:nbsFecpmHistoricTable.setStatus(_A)
_NbsFecpmHistoricEntry_Object=MibTableRow
nbsFecpmHistoricEntry=_NbsFecpmHistoricEntry_Object((1,3,6,1,4,1,629,223,3,3,1))
nbsFecpmHistoricEntry.setIndexNames((0,_C,_N),(0,_C,_O),(0,_C,_P))
if mibBuilder.loadTexts:nbsFecpmHistoricEntry.setStatus(_A)
_NbsFecpmHistoricIfIndex_Type=InterfaceIndex
_NbsFecpmHistoricIfIndex_Object=MibTableColumn
nbsFecpmHistoricIfIndex=_NbsFecpmHistoricIfIndex_Object((1,3,6,1,4,1,629,223,3,3,1,1),_NbsFecpmHistoricIfIndex_Type())
nbsFecpmHistoricIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmHistoricIfIndex.setStatus(_A)
class _NbsFecpmHistoricInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_NbsFecpmHistoricInterval_Type.__name__=_I
_NbsFecpmHistoricInterval_Object=MibTableColumn
nbsFecpmHistoricInterval=_NbsFecpmHistoricInterval_Object((1,3,6,1,4,1,629,223,3,3,1,2),_NbsFecpmHistoricInterval_Type())
nbsFecpmHistoricInterval.setMaxAccess(_Q)
if mibBuilder.loadTexts:nbsFecpmHistoricInterval.setStatus(_A)
_NbsFecpmHistoricSample_Type=Integer32
_NbsFecpmHistoricSample_Object=MibTableColumn
nbsFecpmHistoricSample=_NbsFecpmHistoricSample_Object((1,3,6,1,4,1,629,223,3,3,1,4),_NbsFecpmHistoricSample_Type())
nbsFecpmHistoricSample.setMaxAccess(_Q)
if mibBuilder.loadTexts:nbsFecpmHistoricSample.setStatus(_A)
_NbsFecpmHistoricDate_Type=Integer32
_NbsFecpmHistoricDate_Object=MibTableColumn
nbsFecpmHistoricDate=_NbsFecpmHistoricDate_Object((1,3,6,1,4,1,629,223,3,3,1,5),_NbsFecpmHistoricDate_Type())
nbsFecpmHistoricDate.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmHistoricDate.setStatus(_A)
_NbsFecpmHistoricTime_Type=Integer32
_NbsFecpmHistoricTime_Object=MibTableColumn
nbsFecpmHistoricTime=_NbsFecpmHistoricTime_Object((1,3,6,1,4,1,629,223,3,3,1,6),_NbsFecpmHistoricTime_Type())
nbsFecpmHistoricTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmHistoricTime.setStatus(_A)
_NbsFecpmHistoricBitErrCor_Type=Counter64
_NbsFecpmHistoricBitErrCor_Object=MibTableColumn
nbsFecpmHistoricBitErrCor=_NbsFecpmHistoricBitErrCor_Object((1,3,6,1,4,1,629,223,3,3,1,10),_NbsFecpmHistoricBitErrCor_Type())
nbsFecpmHistoricBitErrCor.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmHistoricBitErrCor.setStatus(_A)
_NbsFecpmHistoricByteErrCor_Type=Counter64
_NbsFecpmHistoricByteErrCor_Object=MibTableColumn
nbsFecpmHistoricByteErrCor=_NbsFecpmHistoricByteErrCor_Object((1,3,6,1,4,1,629,223,3,3,1,12),_NbsFecpmHistoricByteErrCor_Type())
nbsFecpmHistoricByteErrCor.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmHistoricByteErrCor.setStatus(_A)
_NbsFecpmHistoricCorBit0to1_Type=Counter64
_NbsFecpmHistoricCorBit0to1_Object=MibTableColumn
nbsFecpmHistoricCorBit0to1=_NbsFecpmHistoricCorBit0to1_Object((1,3,6,1,4,1,629,223,3,3,1,14),_NbsFecpmHistoricCorBit0to1_Type())
nbsFecpmHistoricCorBit0to1.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmHistoricCorBit0to1.setStatus(_A)
_NbsFecpmHistoricCorBit1to0_Type=Counter64
_NbsFecpmHistoricCorBit1to0_Object=MibTableColumn
nbsFecpmHistoricCorBit1to0=_NbsFecpmHistoricCorBit1to0_Object((1,3,6,1,4,1,629,223,3,3,1,16),_NbsFecpmHistoricCorBit1to0_Type())
nbsFecpmHistoricCorBit1to0.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmHistoricCorBit1to0.setStatus(_A)
_NbsFecpmHistoricUncorWords_Type=Counter64
_NbsFecpmHistoricUncorWords_Object=MibTableColumn
nbsFecpmHistoricUncorWords=_NbsFecpmHistoricUncorWords_Object((1,3,6,1,4,1,629,223,3,3,1,18),_NbsFecpmHistoricUncorWords_Type())
nbsFecpmHistoricUncorWords.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmHistoricUncorWords.setStatus(_A)
_NbsFecpmRunningGrp_ObjectIdentity=ObjectIdentity
nbsFecpmRunningGrp=_NbsFecpmRunningGrp_ObjectIdentity((1,3,6,1,4,1,629,223,4))
if mibBuilder.loadTexts:nbsFecpmRunningGrp.setStatus(_A)
_NbsFecpmRunningTable_Object=MibTable
nbsFecpmRunningTable=_NbsFecpmRunningTable_Object((1,3,6,1,4,1,629,223,4,3))
if mibBuilder.loadTexts:nbsFecpmRunningTable.setStatus(_A)
_NbsFecpmRunningEntry_Object=MibTableRow
nbsFecpmRunningEntry=_NbsFecpmRunningEntry_Object((1,3,6,1,4,1,629,223,4,3,1))
nbsFecpmRunningEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:nbsFecpmRunningEntry.setStatus(_A)
_NbsFecpmRunningIfIndex_Type=InterfaceIndex
_NbsFecpmRunningIfIndex_Object=MibTableColumn
nbsFecpmRunningIfIndex=_NbsFecpmRunningIfIndex_Object((1,3,6,1,4,1,629,223,4,3,1,1),_NbsFecpmRunningIfIndex_Type())
nbsFecpmRunningIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmRunningIfIndex.setStatus(_A)
_NbsFecpmRunningDate_Type=Integer32
_NbsFecpmRunningDate_Object=MibTableColumn
nbsFecpmRunningDate=_NbsFecpmRunningDate_Object((1,3,6,1,4,1,629,223,4,3,1,5),_NbsFecpmRunningDate_Type())
nbsFecpmRunningDate.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmRunningDate.setStatus(_A)
_NbsFecpmRunningTime_Type=Integer32
_NbsFecpmRunningTime_Object=MibTableColumn
nbsFecpmRunningTime=_NbsFecpmRunningTime_Object((1,3,6,1,4,1,629,223,4,3,1,6),_NbsFecpmRunningTime_Type())
nbsFecpmRunningTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmRunningTime.setStatus(_A)
_NbsFecpmRunningBitErrCor_Type=Counter64
_NbsFecpmRunningBitErrCor_Object=MibTableColumn
nbsFecpmRunningBitErrCor=_NbsFecpmRunningBitErrCor_Object((1,3,6,1,4,1,629,223,4,3,1,10),_NbsFecpmRunningBitErrCor_Type())
nbsFecpmRunningBitErrCor.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmRunningBitErrCor.setStatus(_A)
_NbsFecpmRunningByteErrCor_Type=Counter64
_NbsFecpmRunningByteErrCor_Object=MibTableColumn
nbsFecpmRunningByteErrCor=_NbsFecpmRunningByteErrCor_Object((1,3,6,1,4,1,629,223,4,3,1,12),_NbsFecpmRunningByteErrCor_Type())
nbsFecpmRunningByteErrCor.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmRunningByteErrCor.setStatus(_A)
_NbsFecpmRunningCorBit0to1_Type=Counter64
_NbsFecpmRunningCorBit0to1_Object=MibTableColumn
nbsFecpmRunningCorBit0to1=_NbsFecpmRunningCorBit0to1_Object((1,3,6,1,4,1,629,223,4,3,1,14),_NbsFecpmRunningCorBit0to1_Type())
nbsFecpmRunningCorBit0to1.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmRunningCorBit0to1.setStatus(_A)
_NbsFecpmRunningCorBit1to0_Type=Counter64
_NbsFecpmRunningCorBit1to0_Object=MibTableColumn
nbsFecpmRunningCorBit1to0=_NbsFecpmRunningCorBit1to0_Object((1,3,6,1,4,1,629,223,4,3,1,16),_NbsFecpmRunningCorBit1to0_Type())
nbsFecpmRunningCorBit1to0.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmRunningCorBit1to0.setStatus(_A)
_NbsFecpmRunningUncorWords_Type=Counter64
_NbsFecpmRunningUncorWords_Object=MibTableColumn
nbsFecpmRunningUncorWords=_NbsFecpmRunningUncorWords_Object((1,3,6,1,4,1,629,223,4,3,1,18),_NbsFecpmRunningUncorWords_Type())
nbsFecpmRunningUncorWords.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecpmRunningUncorWords.setStatus(_A)
_NbsFecStatsGrp_ObjectIdentity=ObjectIdentity
nbsFecStatsGrp=_NbsFecStatsGrp_ObjectIdentity((1,3,6,1,4,1,629,223,90))
if mibBuilder.loadTexts:nbsFecStatsGrp.setStatus(_A)
_NbsFecStatsTable_Object=MibTable
nbsFecStatsTable=_NbsFecStatsTable_Object((1,3,6,1,4,1,629,223,90,3))
if mibBuilder.loadTexts:nbsFecStatsTable.setStatus(_A)
_NbsFecStatsEntry_Object=MibTableRow
nbsFecStatsEntry=_NbsFecStatsEntry_Object((1,3,6,1,4,1,629,223,90,3,1))
nbsFecStatsEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:nbsFecStatsEntry.setStatus(_A)
_NbsFecStatsIfIndex_Type=InterfaceIndex
_NbsFecStatsIfIndex_Object=MibTableColumn
nbsFecStatsIfIndex=_NbsFecStatsIfIndex_Object((1,3,6,1,4,1,629,223,90,3,1,1),_NbsFecStatsIfIndex_Type())
nbsFecStatsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecStatsIfIndex.setStatus(_A)
_NbsFecStatsDate_Type=Integer32
_NbsFecStatsDate_Object=MibTableColumn
nbsFecStatsDate=_NbsFecStatsDate_Object((1,3,6,1,4,1,629,223,90,3,1,5),_NbsFecStatsDate_Type())
nbsFecStatsDate.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecStatsDate.setStatus(_A)
_NbsFecStatsTime_Type=Integer32
_NbsFecStatsTime_Object=MibTableColumn
nbsFecStatsTime=_NbsFecStatsTime_Object((1,3,6,1,4,1,629,223,90,3,1,6),_NbsFecStatsTime_Type())
nbsFecStatsTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecStatsTime.setStatus(_A)
_NbsFecStatsSpan_Type=Integer32
_NbsFecStatsSpan_Object=MibTableColumn
nbsFecStatsSpan=_NbsFecStatsSpan_Object((1,3,6,1,4,1,629,223,90,3,1,7),_NbsFecStatsSpan_Type())
nbsFecStatsSpan.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecStatsSpan.setStatus(_A)
class _NbsFecStatsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notSupported',1),('counting',2),('clearing',3),('stopped',4)))
_NbsFecStatsState_Type.__name__=_I
_NbsFecStatsState_Object=MibTableColumn
nbsFecStatsState=_NbsFecStatsState_Object((1,3,6,1,4,1,629,223,90,3,1,8),_NbsFecStatsState_Type())
nbsFecStatsState.setMaxAccess(_H)
if mibBuilder.loadTexts:nbsFecStatsState.setStatus(_A)
_NbsFecStatsBitErrCor_Type=Counter64
_NbsFecStatsBitErrCor_Object=MibTableColumn
nbsFecStatsBitErrCor=_NbsFecStatsBitErrCor_Object((1,3,6,1,4,1,629,223,90,3,1,10),_NbsFecStatsBitErrCor_Type())
nbsFecStatsBitErrCor.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecStatsBitErrCor.setStatus(_A)
_NbsFecStatsByteErrCor_Type=Counter64
_NbsFecStatsByteErrCor_Object=MibTableColumn
nbsFecStatsByteErrCor=_NbsFecStatsByteErrCor_Object((1,3,6,1,4,1,629,223,90,3,1,12),_NbsFecStatsByteErrCor_Type())
nbsFecStatsByteErrCor.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecStatsByteErrCor.setStatus(_A)
_NbsFecStatsCorBit0to1_Type=Counter64
_NbsFecStatsCorBit0to1_Object=MibTableColumn
nbsFecStatsCorBit0to1=_NbsFecStatsCorBit0to1_Object((1,3,6,1,4,1,629,223,90,3,1,14),_NbsFecStatsCorBit0to1_Type())
nbsFecStatsCorBit0to1.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecStatsCorBit0to1.setStatus(_A)
_NbsFecStatsCorBit1to0_Type=Counter64
_NbsFecStatsCorBit1to0_Object=MibTableColumn
nbsFecStatsCorBit1to0=_NbsFecStatsCorBit1to0_Object((1,3,6,1,4,1,629,223,90,3,1,16),_NbsFecStatsCorBit1to0_Type())
nbsFecStatsCorBit1to0.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecStatsCorBit1to0.setStatus(_A)
_NbsFecStatsUncorWords_Type=Counter64
_NbsFecStatsUncorWords_Object=MibTableColumn
nbsFecStatsUncorWords=_NbsFecStatsUncorWords_Object((1,3,6,1,4,1,629,223,90,3,1,18),_NbsFecStatsUncorWords_Type())
nbsFecStatsUncorWords.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsFecStatsUncorWords.setStatus(_A)
_NbsFecpmEventsGrp_ObjectIdentity=ObjectIdentity
nbsFecpmEventsGrp=_NbsFecpmEventsGrp_ObjectIdentity((1,3,6,1,4,1,629,223,100))
if mibBuilder.loadTexts:nbsFecpmEventsGrp.setStatus(_A)
_NbsFecpmTraps_ObjectIdentity=ObjectIdentity
nbsFecpmTraps=_NbsFecpmTraps_ObjectIdentity((1,3,6,1,4,1,629,223,100,0))
if mibBuilder.loadTexts:nbsFecpmTraps.setStatus(_A)
nbsFecpmTrapsBitErrCor=NotificationType((1,3,6,1,4,1,629,223,100,0,10))
nbsFecpmTrapsBitErrCor.setObjects(*((_C,_D),(_F,_G),(_C,_E),(_C,_T)))
if mibBuilder.loadTexts:nbsFecpmTrapsBitErrCor.setStatus(_A)
nbsFecpmTrapsByteErrCor=NotificationType((1,3,6,1,4,1,629,223,100,0,12))
nbsFecpmTrapsByteErrCor.setObjects(*((_C,_D),(_F,_G),(_C,_E),(_C,_U)))
if mibBuilder.loadTexts:nbsFecpmTrapsByteErrCor.setStatus(_A)
nbsFecpmTrapsCorBit0to1=NotificationType((1,3,6,1,4,1,629,223,100,0,14))
nbsFecpmTrapsCorBit0to1.setObjects(*((_C,_D),(_F,_G),(_C,_E),(_C,_V)))
if mibBuilder.loadTexts:nbsFecpmTrapsCorBit0to1.setStatus(_A)
nbsFecpmTrapsCorBit1to0=NotificationType((1,3,6,1,4,1,629,223,100,0,16))
nbsFecpmTrapsCorBit1to0.setObjects(*((_C,_D),(_F,_G),(_C,_E),(_C,_W)))
if mibBuilder.loadTexts:nbsFecpmTrapsCorBit1to0.setStatus(_A)
nbsFecpmTrapsUncorWords=NotificationType((1,3,6,1,4,1,629,223,100,0,18))
nbsFecpmTrapsUncorWords.setObjects(*((_C,_D),(_F,_G),(_C,_E),(_C,_X)))
if mibBuilder.loadTexts:nbsFecpmTrapsUncorWords.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'nbsFecpmMib':nbsFecpmMib,'nbsFecpmThresholdsGrp':nbsFecpmThresholdsGrp,'nbsFecpmThresholdsTable':nbsFecpmThresholdsTable,'nbsFecpmThresholdsEntry':nbsFecpmThresholdsEntry,_L:nbsFecpmThresholdsIfIndex,_M:nbsFecpmThresholdsInterval,'nbsFecpmThresholdsBitErrCor':nbsFecpmThresholdsBitErrCor,'nbsFecpmThresholdsByteErrCor':nbsFecpmThresholdsByteErrCor,'nbsFecpmThresholdsCorBit0to1':nbsFecpmThresholdsCorBit0to1,'nbsFecpmThresholdsCorBit1to0':nbsFecpmThresholdsCorBit1to0,'nbsFecpmThresholdsUncorWords':nbsFecpmThresholdsUncorWords,'nbsFecpmCurrentGrp':nbsFecpmCurrentGrp,'nbsFecpmCurrentSysDate':nbsFecpmCurrentSysDate,'nbsFecpmCurrentSysTime':nbsFecpmCurrentSysTime,'nbsFecpmCurrentTable':nbsFecpmCurrentTable,'nbsFecpmCurrentEntry':nbsFecpmCurrentEntry,_D:nbsFecpmCurrentIfIndex,_E:nbsFecpmCurrentInterval,'nbsFecpmCurrentDate':nbsFecpmCurrentDate,'nbsFecpmCurrentTime':nbsFecpmCurrentTime,_T:nbsFecpmCurrentBitErrCor,_U:nbsFecpmCurrentByteErrCor,_V:nbsFecpmCurrentCorBit0to1,_W:nbsFecpmCurrentCorBit1to0,_X:nbsFecpmCurrentUncorWords,'nbsFecpmHistoricGrp':nbsFecpmHistoricGrp,'nbsFecpmHistoricTable':nbsFecpmHistoricTable,'nbsFecpmHistoricEntry':nbsFecpmHistoricEntry,_N:nbsFecpmHistoricIfIndex,_O:nbsFecpmHistoricInterval,_P:nbsFecpmHistoricSample,'nbsFecpmHistoricDate':nbsFecpmHistoricDate,'nbsFecpmHistoricTime':nbsFecpmHistoricTime,'nbsFecpmHistoricBitErrCor':nbsFecpmHistoricBitErrCor,'nbsFecpmHistoricByteErrCor':nbsFecpmHistoricByteErrCor,'nbsFecpmHistoricCorBit0to1':nbsFecpmHistoricCorBit0to1,'nbsFecpmHistoricCorBit1to0':nbsFecpmHistoricCorBit1to0,'nbsFecpmHistoricUncorWords':nbsFecpmHistoricUncorWords,'nbsFecpmRunningGrp':nbsFecpmRunningGrp,'nbsFecpmRunningTable':nbsFecpmRunningTable,'nbsFecpmRunningEntry':nbsFecpmRunningEntry,_R:nbsFecpmRunningIfIndex,'nbsFecpmRunningDate':nbsFecpmRunningDate,'nbsFecpmRunningTime':nbsFecpmRunningTime,'nbsFecpmRunningBitErrCor':nbsFecpmRunningBitErrCor,'nbsFecpmRunningByteErrCor':nbsFecpmRunningByteErrCor,'nbsFecpmRunningCorBit0to1':nbsFecpmRunningCorBit0to1,'nbsFecpmRunningCorBit1to0':nbsFecpmRunningCorBit1to0,'nbsFecpmRunningUncorWords':nbsFecpmRunningUncorWords,'nbsFecStatsGrp':nbsFecStatsGrp,'nbsFecStatsTable':nbsFecStatsTable,'nbsFecStatsEntry':nbsFecStatsEntry,_S:nbsFecStatsIfIndex,'nbsFecStatsDate':nbsFecStatsDate,'nbsFecStatsTime':nbsFecStatsTime,'nbsFecStatsSpan':nbsFecStatsSpan,'nbsFecStatsState':nbsFecStatsState,'nbsFecStatsBitErrCor':nbsFecStatsBitErrCor,'nbsFecStatsByteErrCor':nbsFecStatsByteErrCor,'nbsFecStatsCorBit0to1':nbsFecStatsCorBit0to1,'nbsFecStatsCorBit1to0':nbsFecStatsCorBit1to0,'nbsFecStatsUncorWords':nbsFecStatsUncorWords,'nbsFecpmEventsGrp':nbsFecpmEventsGrp,'nbsFecpmTraps':nbsFecpmTraps,'nbsFecpmTrapsBitErrCor':nbsFecpmTrapsBitErrCor,'nbsFecpmTrapsByteErrCor':nbsFecpmTrapsByteErrCor,'nbsFecpmTrapsCorBit0to1':nbsFecpmTrapsCorBit0to1,'nbsFecpmTrapsCorBit1to0':nbsFecpmTrapsCorBit1to0,'nbsFecpmTrapsUncorWords':nbsFecpmTrapsUncorWords})