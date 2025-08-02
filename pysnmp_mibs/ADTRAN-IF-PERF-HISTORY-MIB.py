_AH='adIfPh1DayIntervalGroup'
_AG='adIfPh15MinIntervalGroup'
_AF='adIfPhCurGroup'
_AE='adIfPh1DayOutErrors'
_AD='adIfPh1DayOutDiscards'
_AC='adIfPh1DayOutBcastPkts'
_AB='adIfPh1DayOutMcastPkts'
_AA='adIfPh1DayOutUcastPkts'
_A9='adIfPh1DayOutOctets'
_A8='adIfPh1DayInUnknownProtos'
_A7='adIfPh1DayInErrors'
_A6='adIfPh1DayInDiscards'
_A5='adIfPh1DayInBcastPkts'
_A4='adIfPh1DayInMcastPkts'
_A3='adIfPh1DayInUcastPkts'
_A2='adIfPh1DayInOctets'
_A1='adIfPh15MinOutErrors'
_A0='adIfPh15MinOutDiscards'
_z='adIfPh15MinOutBcastPkts'
_y='adIfPh15MinOutMcastPkts'
_x='adIfPh15MinOutUcastPkts'
_w='adIfPh15MinOutOctets'
_v='adIfPh15MinInUnknownProtos'
_u='adIfPh15MinInErrors'
_t='adIfPh15MinInDiscards'
_s='adIfPh15MinInBcastPkts'
_r='adIfPh15MinInMcastPkts'
_q='adIfPh15MinInUcastPkts'
_p='adIfPh15MinInOctets'
_o='adIfPhCurOutErrors1Day'
_n='adIfPhCurOutDiscards1Day'
_m='adIfPhCurOutBcastPkts1Day'
_l='adIfPhCurOutMcastPkts1Day'
_k='adIfPhCurOutUcastPkts1Day'
_j='adIfPhCurOutOctets1Day'
_i='adIfPhCurInUnknownProtos1Day'
_h='adIfPhCurInErrors1Day'
_g='adIfPhCurInDiscards1Day'
_f='adIfPhCurInBcastPkts1Day'
_e='adIfPhCurInMcastPkts1Day'
_d='adIfPhCurInUcastPkts1Day'
_c='adIfPhCurInOctets1Day'
_b='adIfPhCurInvalidIntervals1Day'
_a='adIfPhCurValidIntervals1Day'
_Z='adIfPhCurTimeElapsed1Day'
_Y='adIfPhCurOutErrors15Min'
_X='adIfPhCurOutDiscards15Min'
_W='adIfPhCurOutBcastPkts15Min'
_V='adIfPhCurOutMcastPkts15Min'
_U='adIfPhCurOutUcastPkts15Min'
_T='adIfPhCurOutOctets15Min'
_S='adIfPhCurInUnknownProtos15Min'
_R='adIfPhCurInErrors15Min'
_Q='adIfPhCurInDiscards15Min'
_P='adIfPhCurInBcastPkts15Min'
_O='adIfPhCurInMcastPkts15Min'
_N='adIfPhCurInUcastPkts15Min'
_M='adIfPhCurInOctets15Min'
_L='adIfPhCurInvalidIntervals15Min'
_K='adIfPhCurValidIntervals15Min'
_J='adIfPhCurTimeElapsed15Min'
_I='adIfPh1DayIntervalNumber'
_H='not-accessible'
_G='adIfPh15MinIntervalNumber'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='ADTRAN-IF-PERF-HISTORY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenAOSCommon,adGenAOSConformance=mibBuilder.importSymbols('ADTRAN-AOS','adGenAOSCommon','adGenAOSConformance')
adIdentity,=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity')
HCPerfCurrentCount,HCPerfIntervalCount,HCPerfInvalidIntervals,HCPerfTimeElapsed,HCPerfTotalCount,HCPerfValidIntervals=mibBuilder.importSymbols('HC-PerfHist-TC-MIB','HCPerfCurrentCount','HCPerfIntervalCount','HCPerfInvalidIntervals','HCPerfTimeElapsed','HCPerfTotalCount','HCPerfValidIntervals')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenAosIfPerfHistoryMib=ModuleIdentity((1,3,6,1,4,1,664,6,10000,53,1,7))
if mibBuilder.loadTexts:adGenAosIfPerfHistoryMib.setRevisions(('2013-08-23 00:00',))
_AdGenAosIfPerfHistory_ObjectIdentity=ObjectIdentity
adGenAosIfPerfHistory=_AdGenAosIfPerfHistory_ObjectIdentity((1,3,6,1,4,1,664,5,53,1,7))
_AdIfPhCurTable_Object=MibTable
adIfPhCurTable=_AdIfPhCurTable_Object((1,3,6,1,4,1,664,5,53,1,7,1))
if mibBuilder.loadTexts:adIfPhCurTable.setStatus(_A)
_AdIfPhCurEntry_Object=MibTableRow
adIfPhCurEntry=_AdIfPhCurEntry_Object((1,3,6,1,4,1,664,5,53,1,7,1,1))
adIfPhCurEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:adIfPhCurEntry.setStatus(_A)
_AdIfPhCurTimeElapsed15Min_Type=HCPerfTimeElapsed
_AdIfPhCurTimeElapsed15Min_Object=MibTableColumn
adIfPhCurTimeElapsed15Min=_AdIfPhCurTimeElapsed15Min_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,1),_AdIfPhCurTimeElapsed15Min_Type())
adIfPhCurTimeElapsed15Min.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurTimeElapsed15Min.setStatus(_A)
_AdIfPhCurValidIntervals15Min_Type=HCPerfValidIntervals
_AdIfPhCurValidIntervals15Min_Object=MibTableColumn
adIfPhCurValidIntervals15Min=_AdIfPhCurValidIntervals15Min_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,2),_AdIfPhCurValidIntervals15Min_Type())
adIfPhCurValidIntervals15Min.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurValidIntervals15Min.setStatus(_A)
_AdIfPhCurInvalidIntervals15Min_Type=HCPerfInvalidIntervals
_AdIfPhCurInvalidIntervals15Min_Object=MibTableColumn
adIfPhCurInvalidIntervals15Min=_AdIfPhCurInvalidIntervals15Min_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,3),_AdIfPhCurInvalidIntervals15Min_Type())
adIfPhCurInvalidIntervals15Min.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurInvalidIntervals15Min.setStatus(_A)
_AdIfPhCurInOctets15Min_Type=HCPerfCurrentCount
_AdIfPhCurInOctets15Min_Object=MibTableColumn
adIfPhCurInOctets15Min=_AdIfPhCurInOctets15Min_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,4),_AdIfPhCurInOctets15Min_Type())
adIfPhCurInOctets15Min.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurInOctets15Min.setStatus(_A)
_AdIfPhCurInUcastPkts15Min_Type=HCPerfCurrentCount
_AdIfPhCurInUcastPkts15Min_Object=MibTableColumn
adIfPhCurInUcastPkts15Min=_AdIfPhCurInUcastPkts15Min_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,5),_AdIfPhCurInUcastPkts15Min_Type())
adIfPhCurInUcastPkts15Min.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurInUcastPkts15Min.setStatus(_A)
_AdIfPhCurInMcastPkts15Min_Type=HCPerfCurrentCount
_AdIfPhCurInMcastPkts15Min_Object=MibTableColumn
adIfPhCurInMcastPkts15Min=_AdIfPhCurInMcastPkts15Min_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,6),_AdIfPhCurInMcastPkts15Min_Type())
adIfPhCurInMcastPkts15Min.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurInMcastPkts15Min.setStatus(_A)
_AdIfPhCurInBcastPkts15Min_Type=HCPerfCurrentCount
_AdIfPhCurInBcastPkts15Min_Object=MibTableColumn
adIfPhCurInBcastPkts15Min=_AdIfPhCurInBcastPkts15Min_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,7),_AdIfPhCurInBcastPkts15Min_Type())
adIfPhCurInBcastPkts15Min.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurInBcastPkts15Min.setStatus(_A)
_AdIfPhCurInDiscards15Min_Type=HCPerfCurrentCount
_AdIfPhCurInDiscards15Min_Object=MibTableColumn
adIfPhCurInDiscards15Min=_AdIfPhCurInDiscards15Min_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,8),_AdIfPhCurInDiscards15Min_Type())
adIfPhCurInDiscards15Min.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurInDiscards15Min.setStatus(_A)
_AdIfPhCurInErrors15Min_Type=HCPerfCurrentCount
_AdIfPhCurInErrors15Min_Object=MibTableColumn
adIfPhCurInErrors15Min=_AdIfPhCurInErrors15Min_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,9),_AdIfPhCurInErrors15Min_Type())
adIfPhCurInErrors15Min.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurInErrors15Min.setStatus(_A)
_AdIfPhCurInUnknownProtos15Min_Type=HCPerfCurrentCount
_AdIfPhCurInUnknownProtos15Min_Object=MibTableColumn
adIfPhCurInUnknownProtos15Min=_AdIfPhCurInUnknownProtos15Min_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,10),_AdIfPhCurInUnknownProtos15Min_Type())
adIfPhCurInUnknownProtos15Min.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurInUnknownProtos15Min.setStatus(_A)
_AdIfPhCurOutOctets15Min_Type=HCPerfCurrentCount
_AdIfPhCurOutOctets15Min_Object=MibTableColumn
adIfPhCurOutOctets15Min=_AdIfPhCurOutOctets15Min_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,11),_AdIfPhCurOutOctets15Min_Type())
adIfPhCurOutOctets15Min.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurOutOctets15Min.setStatus(_A)
_AdIfPhCurOutUcastPkts15Min_Type=HCPerfCurrentCount
_AdIfPhCurOutUcastPkts15Min_Object=MibTableColumn
adIfPhCurOutUcastPkts15Min=_AdIfPhCurOutUcastPkts15Min_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,12),_AdIfPhCurOutUcastPkts15Min_Type())
adIfPhCurOutUcastPkts15Min.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurOutUcastPkts15Min.setStatus(_A)
_AdIfPhCurOutMcastPkts15Min_Type=HCPerfCurrentCount
_AdIfPhCurOutMcastPkts15Min_Object=MibTableColumn
adIfPhCurOutMcastPkts15Min=_AdIfPhCurOutMcastPkts15Min_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,13),_AdIfPhCurOutMcastPkts15Min_Type())
adIfPhCurOutMcastPkts15Min.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurOutMcastPkts15Min.setStatus(_A)
_AdIfPhCurOutBcastPkts15Min_Type=HCPerfCurrentCount
_AdIfPhCurOutBcastPkts15Min_Object=MibTableColumn
adIfPhCurOutBcastPkts15Min=_AdIfPhCurOutBcastPkts15Min_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,14),_AdIfPhCurOutBcastPkts15Min_Type())
adIfPhCurOutBcastPkts15Min.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurOutBcastPkts15Min.setStatus(_A)
_AdIfPhCurOutDiscards15Min_Type=HCPerfCurrentCount
_AdIfPhCurOutDiscards15Min_Object=MibTableColumn
adIfPhCurOutDiscards15Min=_AdIfPhCurOutDiscards15Min_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,15),_AdIfPhCurOutDiscards15Min_Type())
adIfPhCurOutDiscards15Min.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurOutDiscards15Min.setStatus(_A)
_AdIfPhCurOutErrors15Min_Type=HCPerfCurrentCount
_AdIfPhCurOutErrors15Min_Object=MibTableColumn
adIfPhCurOutErrors15Min=_AdIfPhCurOutErrors15Min_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,16),_AdIfPhCurOutErrors15Min_Type())
adIfPhCurOutErrors15Min.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurOutErrors15Min.setStatus(_A)
_AdIfPhCurTimeElapsed1Day_Type=HCPerfTimeElapsed
_AdIfPhCurTimeElapsed1Day_Object=MibTableColumn
adIfPhCurTimeElapsed1Day=_AdIfPhCurTimeElapsed1Day_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,17),_AdIfPhCurTimeElapsed1Day_Type())
adIfPhCurTimeElapsed1Day.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurTimeElapsed1Day.setStatus(_A)
_AdIfPhCurValidIntervals1Day_Type=HCPerfValidIntervals
_AdIfPhCurValidIntervals1Day_Object=MibTableColumn
adIfPhCurValidIntervals1Day=_AdIfPhCurValidIntervals1Day_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,18),_AdIfPhCurValidIntervals1Day_Type())
adIfPhCurValidIntervals1Day.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurValidIntervals1Day.setStatus(_A)
_AdIfPhCurInvalidIntervals1Day_Type=HCPerfInvalidIntervals
_AdIfPhCurInvalidIntervals1Day_Object=MibTableColumn
adIfPhCurInvalidIntervals1Day=_AdIfPhCurInvalidIntervals1Day_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,19),_AdIfPhCurInvalidIntervals1Day_Type())
adIfPhCurInvalidIntervals1Day.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurInvalidIntervals1Day.setStatus(_A)
_AdIfPhCurInOctets1Day_Type=HCPerfCurrentCount
_AdIfPhCurInOctets1Day_Object=MibTableColumn
adIfPhCurInOctets1Day=_AdIfPhCurInOctets1Day_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,20),_AdIfPhCurInOctets1Day_Type())
adIfPhCurInOctets1Day.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurInOctets1Day.setStatus(_A)
_AdIfPhCurInUcastPkts1Day_Type=HCPerfCurrentCount
_AdIfPhCurInUcastPkts1Day_Object=MibTableColumn
adIfPhCurInUcastPkts1Day=_AdIfPhCurInUcastPkts1Day_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,21),_AdIfPhCurInUcastPkts1Day_Type())
adIfPhCurInUcastPkts1Day.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurInUcastPkts1Day.setStatus(_A)
_AdIfPhCurInMcastPkts1Day_Type=HCPerfCurrentCount
_AdIfPhCurInMcastPkts1Day_Object=MibTableColumn
adIfPhCurInMcastPkts1Day=_AdIfPhCurInMcastPkts1Day_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,22),_AdIfPhCurInMcastPkts1Day_Type())
adIfPhCurInMcastPkts1Day.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurInMcastPkts1Day.setStatus(_A)
_AdIfPhCurInBcastPkts1Day_Type=HCPerfCurrentCount
_AdIfPhCurInBcastPkts1Day_Object=MibTableColumn
adIfPhCurInBcastPkts1Day=_AdIfPhCurInBcastPkts1Day_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,23),_AdIfPhCurInBcastPkts1Day_Type())
adIfPhCurInBcastPkts1Day.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurInBcastPkts1Day.setStatus(_A)
_AdIfPhCurInDiscards1Day_Type=HCPerfCurrentCount
_AdIfPhCurInDiscards1Day_Object=MibTableColumn
adIfPhCurInDiscards1Day=_AdIfPhCurInDiscards1Day_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,24),_AdIfPhCurInDiscards1Day_Type())
adIfPhCurInDiscards1Day.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurInDiscards1Day.setStatus(_A)
_AdIfPhCurInErrors1Day_Type=HCPerfCurrentCount
_AdIfPhCurInErrors1Day_Object=MibTableColumn
adIfPhCurInErrors1Day=_AdIfPhCurInErrors1Day_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,25),_AdIfPhCurInErrors1Day_Type())
adIfPhCurInErrors1Day.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurInErrors1Day.setStatus(_A)
_AdIfPhCurInUnknownProtos1Day_Type=HCPerfCurrentCount
_AdIfPhCurInUnknownProtos1Day_Object=MibTableColumn
adIfPhCurInUnknownProtos1Day=_AdIfPhCurInUnknownProtos1Day_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,26),_AdIfPhCurInUnknownProtos1Day_Type())
adIfPhCurInUnknownProtos1Day.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurInUnknownProtos1Day.setStatus(_A)
_AdIfPhCurOutOctets1Day_Type=HCPerfCurrentCount
_AdIfPhCurOutOctets1Day_Object=MibTableColumn
adIfPhCurOutOctets1Day=_AdIfPhCurOutOctets1Day_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,27),_AdIfPhCurOutOctets1Day_Type())
adIfPhCurOutOctets1Day.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurOutOctets1Day.setStatus(_A)
_AdIfPhCurOutUcastPkts1Day_Type=HCPerfCurrentCount
_AdIfPhCurOutUcastPkts1Day_Object=MibTableColumn
adIfPhCurOutUcastPkts1Day=_AdIfPhCurOutUcastPkts1Day_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,28),_AdIfPhCurOutUcastPkts1Day_Type())
adIfPhCurOutUcastPkts1Day.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurOutUcastPkts1Day.setStatus(_A)
_AdIfPhCurOutMcastPkts1Day_Type=HCPerfCurrentCount
_AdIfPhCurOutMcastPkts1Day_Object=MibTableColumn
adIfPhCurOutMcastPkts1Day=_AdIfPhCurOutMcastPkts1Day_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,29),_AdIfPhCurOutMcastPkts1Day_Type())
adIfPhCurOutMcastPkts1Day.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurOutMcastPkts1Day.setStatus(_A)
_AdIfPhCurOutBcastPkts1Day_Type=HCPerfCurrentCount
_AdIfPhCurOutBcastPkts1Day_Object=MibTableColumn
adIfPhCurOutBcastPkts1Day=_AdIfPhCurOutBcastPkts1Day_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,30),_AdIfPhCurOutBcastPkts1Day_Type())
adIfPhCurOutBcastPkts1Day.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurOutBcastPkts1Day.setStatus(_A)
_AdIfPhCurOutDiscards1Day_Type=HCPerfCurrentCount
_AdIfPhCurOutDiscards1Day_Object=MibTableColumn
adIfPhCurOutDiscards1Day=_AdIfPhCurOutDiscards1Day_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,31),_AdIfPhCurOutDiscards1Day_Type())
adIfPhCurOutDiscards1Day.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurOutDiscards1Day.setStatus(_A)
_AdIfPhCurOutErrors1Day_Type=HCPerfCurrentCount
_AdIfPhCurOutErrors1Day_Object=MibTableColumn
adIfPhCurOutErrors1Day=_AdIfPhCurOutErrors1Day_Object((1,3,6,1,4,1,664,5,53,1,7,1,1,32),_AdIfPhCurOutErrors1Day_Type())
adIfPhCurOutErrors1Day.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPhCurOutErrors1Day.setStatus(_A)
_AdIfPh15MinIntervalTable_Object=MibTable
adIfPh15MinIntervalTable=_AdIfPh15MinIntervalTable_Object((1,3,6,1,4,1,664,5,53,1,7,2))
if mibBuilder.loadTexts:adIfPh15MinIntervalTable.setStatus(_A)
_AdIfPh15MinIntervalEntry_Object=MibTableRow
adIfPh15MinIntervalEntry=_AdIfPh15MinIntervalEntry_Object((1,3,6,1,4,1,664,5,53,1,7,2,1))
adIfPh15MinIntervalEntry.setIndexNames((0,_D,_E),(0,_B,_G))
if mibBuilder.loadTexts:adIfPh15MinIntervalEntry.setStatus(_A)
class _AdIfPh15MinIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_AdIfPh15MinIntervalNumber_Type.__name__=_F
_AdIfPh15MinIntervalNumber_Object=MibTableColumn
adIfPh15MinIntervalNumber=_AdIfPh15MinIntervalNumber_Object((1,3,6,1,4,1,664,5,53,1,7,2,1,1),_AdIfPh15MinIntervalNumber_Type())
adIfPh15MinIntervalNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:adIfPh15MinIntervalNumber.setStatus(_A)
_AdIfPh15MinInOctets_Type=HCPerfIntervalCount
_AdIfPh15MinInOctets_Object=MibTableColumn
adIfPh15MinInOctets=_AdIfPh15MinInOctets_Object((1,3,6,1,4,1,664,5,53,1,7,2,1,2),_AdIfPh15MinInOctets_Type())
adIfPh15MinInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh15MinInOctets.setStatus(_A)
_AdIfPh15MinInUcastPkts_Type=HCPerfIntervalCount
_AdIfPh15MinInUcastPkts_Object=MibTableColumn
adIfPh15MinInUcastPkts=_AdIfPh15MinInUcastPkts_Object((1,3,6,1,4,1,664,5,53,1,7,2,1,3),_AdIfPh15MinInUcastPkts_Type())
adIfPh15MinInUcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh15MinInUcastPkts.setStatus(_A)
_AdIfPh15MinInMcastPkts_Type=HCPerfIntervalCount
_AdIfPh15MinInMcastPkts_Object=MibTableColumn
adIfPh15MinInMcastPkts=_AdIfPh15MinInMcastPkts_Object((1,3,6,1,4,1,664,5,53,1,7,2,1,4),_AdIfPh15MinInMcastPkts_Type())
adIfPh15MinInMcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh15MinInMcastPkts.setStatus(_A)
_AdIfPh15MinInBcastPkts_Type=HCPerfIntervalCount
_AdIfPh15MinInBcastPkts_Object=MibTableColumn
adIfPh15MinInBcastPkts=_AdIfPh15MinInBcastPkts_Object((1,3,6,1,4,1,664,5,53,1,7,2,1,5),_AdIfPh15MinInBcastPkts_Type())
adIfPh15MinInBcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh15MinInBcastPkts.setStatus(_A)
_AdIfPh15MinInDiscards_Type=HCPerfIntervalCount
_AdIfPh15MinInDiscards_Object=MibTableColumn
adIfPh15MinInDiscards=_AdIfPh15MinInDiscards_Object((1,3,6,1,4,1,664,5,53,1,7,2,1,6),_AdIfPh15MinInDiscards_Type())
adIfPh15MinInDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh15MinInDiscards.setStatus(_A)
_AdIfPh15MinInErrors_Type=HCPerfIntervalCount
_AdIfPh15MinInErrors_Object=MibTableColumn
adIfPh15MinInErrors=_AdIfPh15MinInErrors_Object((1,3,6,1,4,1,664,5,53,1,7,2,1,7),_AdIfPh15MinInErrors_Type())
adIfPh15MinInErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh15MinInErrors.setStatus(_A)
_AdIfPh15MinInUnknownProtos_Type=HCPerfIntervalCount
_AdIfPh15MinInUnknownProtos_Object=MibTableColumn
adIfPh15MinInUnknownProtos=_AdIfPh15MinInUnknownProtos_Object((1,3,6,1,4,1,664,5,53,1,7,2,1,8),_AdIfPh15MinInUnknownProtos_Type())
adIfPh15MinInUnknownProtos.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh15MinInUnknownProtos.setStatus(_A)
_AdIfPh15MinOutOctets_Type=HCPerfIntervalCount
_AdIfPh15MinOutOctets_Object=MibTableColumn
adIfPh15MinOutOctets=_AdIfPh15MinOutOctets_Object((1,3,6,1,4,1,664,5,53,1,7,2,1,9),_AdIfPh15MinOutOctets_Type())
adIfPh15MinOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh15MinOutOctets.setStatus(_A)
_AdIfPh15MinOutUcastPkts_Type=HCPerfIntervalCount
_AdIfPh15MinOutUcastPkts_Object=MibTableColumn
adIfPh15MinOutUcastPkts=_AdIfPh15MinOutUcastPkts_Object((1,3,6,1,4,1,664,5,53,1,7,2,1,10),_AdIfPh15MinOutUcastPkts_Type())
adIfPh15MinOutUcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh15MinOutUcastPkts.setStatus(_A)
_AdIfPh15MinOutMcastPkts_Type=HCPerfIntervalCount
_AdIfPh15MinOutMcastPkts_Object=MibTableColumn
adIfPh15MinOutMcastPkts=_AdIfPh15MinOutMcastPkts_Object((1,3,6,1,4,1,664,5,53,1,7,2,1,11),_AdIfPh15MinOutMcastPkts_Type())
adIfPh15MinOutMcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh15MinOutMcastPkts.setStatus(_A)
_AdIfPh15MinOutBcastPkts_Type=HCPerfIntervalCount
_AdIfPh15MinOutBcastPkts_Object=MibTableColumn
adIfPh15MinOutBcastPkts=_AdIfPh15MinOutBcastPkts_Object((1,3,6,1,4,1,664,5,53,1,7,2,1,12),_AdIfPh15MinOutBcastPkts_Type())
adIfPh15MinOutBcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh15MinOutBcastPkts.setStatus(_A)
_AdIfPh15MinOutDiscards_Type=HCPerfIntervalCount
_AdIfPh15MinOutDiscards_Object=MibTableColumn
adIfPh15MinOutDiscards=_AdIfPh15MinOutDiscards_Object((1,3,6,1,4,1,664,5,53,1,7,2,1,13),_AdIfPh15MinOutDiscards_Type())
adIfPh15MinOutDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh15MinOutDiscards.setStatus(_A)
_AdIfPh15MinOutErrors_Type=HCPerfIntervalCount
_AdIfPh15MinOutErrors_Object=MibTableColumn
adIfPh15MinOutErrors=_AdIfPh15MinOutErrors_Object((1,3,6,1,4,1,664,5,53,1,7,2,1,14),_AdIfPh15MinOutErrors_Type())
adIfPh15MinOutErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh15MinOutErrors.setStatus(_A)
_AdIfPh1DayIntervalTable_Object=MibTable
adIfPh1DayIntervalTable=_AdIfPh1DayIntervalTable_Object((1,3,6,1,4,1,664,5,53,1,7,3))
if mibBuilder.loadTexts:adIfPh1DayIntervalTable.setStatus(_A)
_AdIfPh1DayIntervalEntry_Object=MibTableRow
adIfPh1DayIntervalEntry=_AdIfPh1DayIntervalEntry_Object((1,3,6,1,4,1,664,5,53,1,7,3,1))
adIfPh1DayIntervalEntry.setIndexNames((0,_D,_E),(0,_B,_I))
if mibBuilder.loadTexts:adIfPh1DayIntervalEntry.setStatus(_A)
class _AdIfPh1DayIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_AdIfPh1DayIntervalNumber_Type.__name__=_F
_AdIfPh1DayIntervalNumber_Object=MibTableColumn
adIfPh1DayIntervalNumber=_AdIfPh1DayIntervalNumber_Object((1,3,6,1,4,1,664,5,53,1,7,3,1,1),_AdIfPh1DayIntervalNumber_Type())
adIfPh1DayIntervalNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:adIfPh1DayIntervalNumber.setStatus(_A)
_AdIfPh1DayInOctets_Type=HCPerfTotalCount
_AdIfPh1DayInOctets_Object=MibTableColumn
adIfPh1DayInOctets=_AdIfPh1DayInOctets_Object((1,3,6,1,4,1,664,5,53,1,7,3,1,2),_AdIfPh1DayInOctets_Type())
adIfPh1DayInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh1DayInOctets.setStatus(_A)
_AdIfPh1DayInUcastPkts_Type=HCPerfTotalCount
_AdIfPh1DayInUcastPkts_Object=MibTableColumn
adIfPh1DayInUcastPkts=_AdIfPh1DayInUcastPkts_Object((1,3,6,1,4,1,664,5,53,1,7,3,1,3),_AdIfPh1DayInUcastPkts_Type())
adIfPh1DayInUcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh1DayInUcastPkts.setStatus(_A)
_AdIfPh1DayInMcastPkts_Type=HCPerfTotalCount
_AdIfPh1DayInMcastPkts_Object=MibTableColumn
adIfPh1DayInMcastPkts=_AdIfPh1DayInMcastPkts_Object((1,3,6,1,4,1,664,5,53,1,7,3,1,4),_AdIfPh1DayInMcastPkts_Type())
adIfPh1DayInMcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh1DayInMcastPkts.setStatus(_A)
_AdIfPh1DayInBcastPkts_Type=HCPerfTotalCount
_AdIfPh1DayInBcastPkts_Object=MibTableColumn
adIfPh1DayInBcastPkts=_AdIfPh1DayInBcastPkts_Object((1,3,6,1,4,1,664,5,53,1,7,3,1,5),_AdIfPh1DayInBcastPkts_Type())
adIfPh1DayInBcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh1DayInBcastPkts.setStatus(_A)
_AdIfPh1DayInDiscards_Type=HCPerfTotalCount
_AdIfPh1DayInDiscards_Object=MibTableColumn
adIfPh1DayInDiscards=_AdIfPh1DayInDiscards_Object((1,3,6,1,4,1,664,5,53,1,7,3,1,6),_AdIfPh1DayInDiscards_Type())
adIfPh1DayInDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh1DayInDiscards.setStatus(_A)
_AdIfPh1DayInErrors_Type=HCPerfTotalCount
_AdIfPh1DayInErrors_Object=MibTableColumn
adIfPh1DayInErrors=_AdIfPh1DayInErrors_Object((1,3,6,1,4,1,664,5,53,1,7,3,1,7),_AdIfPh1DayInErrors_Type())
adIfPh1DayInErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh1DayInErrors.setStatus(_A)
_AdIfPh1DayInUnknownProtos_Type=HCPerfTotalCount
_AdIfPh1DayInUnknownProtos_Object=MibTableColumn
adIfPh1DayInUnknownProtos=_AdIfPh1DayInUnknownProtos_Object((1,3,6,1,4,1,664,5,53,1,7,3,1,8),_AdIfPh1DayInUnknownProtos_Type())
adIfPh1DayInUnknownProtos.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh1DayInUnknownProtos.setStatus(_A)
_AdIfPh1DayOutOctets_Type=HCPerfTotalCount
_AdIfPh1DayOutOctets_Object=MibTableColumn
adIfPh1DayOutOctets=_AdIfPh1DayOutOctets_Object((1,3,6,1,4,1,664,5,53,1,7,3,1,9),_AdIfPh1DayOutOctets_Type())
adIfPh1DayOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh1DayOutOctets.setStatus(_A)
_AdIfPh1DayOutUcastPkts_Type=HCPerfTotalCount
_AdIfPh1DayOutUcastPkts_Object=MibTableColumn
adIfPh1DayOutUcastPkts=_AdIfPh1DayOutUcastPkts_Object((1,3,6,1,4,1,664,5,53,1,7,3,1,10),_AdIfPh1DayOutUcastPkts_Type())
adIfPh1DayOutUcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh1DayOutUcastPkts.setStatus(_A)
_AdIfPh1DayOutMcastPkts_Type=HCPerfTotalCount
_AdIfPh1DayOutMcastPkts_Object=MibTableColumn
adIfPh1DayOutMcastPkts=_AdIfPh1DayOutMcastPkts_Object((1,3,6,1,4,1,664,5,53,1,7,3,1,11),_AdIfPh1DayOutMcastPkts_Type())
adIfPh1DayOutMcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh1DayOutMcastPkts.setStatus(_A)
_AdIfPh1DayOutBcastPkts_Type=HCPerfTotalCount
_AdIfPh1DayOutBcastPkts_Object=MibTableColumn
adIfPh1DayOutBcastPkts=_AdIfPh1DayOutBcastPkts_Object((1,3,6,1,4,1,664,5,53,1,7,3,1,12),_AdIfPh1DayOutBcastPkts_Type())
adIfPh1DayOutBcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh1DayOutBcastPkts.setStatus(_A)
_AdIfPh1DayOutDiscards_Type=HCPerfTotalCount
_AdIfPh1DayOutDiscards_Object=MibTableColumn
adIfPh1DayOutDiscards=_AdIfPh1DayOutDiscards_Object((1,3,6,1,4,1,664,5,53,1,7,3,1,13),_AdIfPh1DayOutDiscards_Type())
adIfPh1DayOutDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh1DayOutDiscards.setStatus(_A)
_AdIfPh1DayOutErrors_Type=HCPerfTotalCount
_AdIfPh1DayOutErrors_Object=MibTableColumn
adIfPh1DayOutErrors=_AdIfPh1DayOutErrors_Object((1,3,6,1,4,1,664,5,53,1,7,3,1,14),_AdIfPh1DayOutErrors_Type())
adIfPh1DayOutErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:adIfPh1DayOutErrors.setStatus(_A)
_AdGenAosIfPerfHistoryConformance_ObjectIdentity=ObjectIdentity
adGenAosIfPerfHistoryConformance=_AdGenAosIfPerfHistoryConformance_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,16))
_AdGenAosIfPerfHistoryGroups_ObjectIdentity=ObjectIdentity
adGenAosIfPerfHistoryGroups=_AdGenAosIfPerfHistoryGroups_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,16,1))
_AdGenAosIfPerfHistoryCompliances_ObjectIdentity=ObjectIdentity
adGenAosIfPerfHistoryCompliances=_AdGenAosIfPerfHistoryCompliances_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,16,2))
adIfPhCurGroup=ObjectGroup((1,3,6,1,4,1,664,5,53,99,16,1,1))
adIfPhCurGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:adIfPhCurGroup.setStatus(_A)
adIfPh15MinIntervalGroup=ObjectGroup((1,3,6,1,4,1,664,5,53,99,16,1,2))
adIfPh15MinIntervalGroup.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:adIfPh15MinIntervalGroup.setStatus(_A)
adIfPh1DayIntervalGroup=ObjectGroup((1,3,6,1,4,1,664,5,53,99,16,1,3))
adIfPh1DayIntervalGroup.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:adIfPh1DayIntervalGroup.setStatus(_A)
adGenAosIfPerfHistoryCompliance=ModuleCompliance((1,3,6,1,4,1,664,5,53,99,16,2,1))
adGenAosIfPerfHistoryCompliance.setObjects(*((_B,_AF),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:adGenAosIfPerfHistoryCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adGenAosIfPerfHistory':adGenAosIfPerfHistory,'adIfPhCurTable':adIfPhCurTable,'adIfPhCurEntry':adIfPhCurEntry,_J:adIfPhCurTimeElapsed15Min,_K:adIfPhCurValidIntervals15Min,_L:adIfPhCurInvalidIntervals15Min,_M:adIfPhCurInOctets15Min,_N:adIfPhCurInUcastPkts15Min,_O:adIfPhCurInMcastPkts15Min,_P:adIfPhCurInBcastPkts15Min,_Q:adIfPhCurInDiscards15Min,_R:adIfPhCurInErrors15Min,_S:adIfPhCurInUnknownProtos15Min,_T:adIfPhCurOutOctets15Min,_U:adIfPhCurOutUcastPkts15Min,_V:adIfPhCurOutMcastPkts15Min,_W:adIfPhCurOutBcastPkts15Min,_X:adIfPhCurOutDiscards15Min,_Y:adIfPhCurOutErrors15Min,_Z:adIfPhCurTimeElapsed1Day,_a:adIfPhCurValidIntervals1Day,_b:adIfPhCurInvalidIntervals1Day,_c:adIfPhCurInOctets1Day,_d:adIfPhCurInUcastPkts1Day,_e:adIfPhCurInMcastPkts1Day,_f:adIfPhCurInBcastPkts1Day,_g:adIfPhCurInDiscards1Day,_h:adIfPhCurInErrors1Day,_i:adIfPhCurInUnknownProtos1Day,_j:adIfPhCurOutOctets1Day,_k:adIfPhCurOutUcastPkts1Day,_l:adIfPhCurOutMcastPkts1Day,_m:adIfPhCurOutBcastPkts1Day,_n:adIfPhCurOutDiscards1Day,_o:adIfPhCurOutErrors1Day,'adIfPh15MinIntervalTable':adIfPh15MinIntervalTable,'adIfPh15MinIntervalEntry':adIfPh15MinIntervalEntry,_G:adIfPh15MinIntervalNumber,_p:adIfPh15MinInOctets,_q:adIfPh15MinInUcastPkts,_r:adIfPh15MinInMcastPkts,_s:adIfPh15MinInBcastPkts,_t:adIfPh15MinInDiscards,_u:adIfPh15MinInErrors,_v:adIfPh15MinInUnknownProtos,_w:adIfPh15MinOutOctets,_x:adIfPh15MinOutUcastPkts,_y:adIfPh15MinOutMcastPkts,_z:adIfPh15MinOutBcastPkts,_A0:adIfPh15MinOutDiscards,_A1:adIfPh15MinOutErrors,'adIfPh1DayIntervalTable':adIfPh1DayIntervalTable,'adIfPh1DayIntervalEntry':adIfPh1DayIntervalEntry,_I:adIfPh1DayIntervalNumber,_A2:adIfPh1DayInOctets,_A3:adIfPh1DayInUcastPkts,_A4:adIfPh1DayInMcastPkts,_A5:adIfPh1DayInBcastPkts,_A6:adIfPh1DayInDiscards,_A7:adIfPh1DayInErrors,_A8:adIfPh1DayInUnknownProtos,_A9:adIfPh1DayOutOctets,_AA:adIfPh1DayOutUcastPkts,_AB:adIfPh1DayOutMcastPkts,_AC:adIfPh1DayOutBcastPkts,_AD:adIfPh1DayOutDiscards,_AE:adIfPh1DayOutErrors,'adGenAosIfPerfHistoryConformance':adGenAosIfPerfHistoryConformance,'adGenAosIfPerfHistoryGroups':adGenAosIfPerfHistoryGroups,_AF:adIfPhCurGroup,_AG:adIfPh15MinIntervalGroup,_AH:adIfPh1DayIntervalGroup,'adGenAosIfPerfHistoryCompliances':adGenAosIfPerfHistoryCompliances,'adGenAosIfPerfHistoryCompliance':adGenAosIfPerfHistoryCompliance,'adGenAosIfPerfHistoryMib':adGenAosIfPerfHistoryMib})