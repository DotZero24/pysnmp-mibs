_N='adMefPerCosPerEvcTotalCountGroup'
_M='adMefPerCosPerEvcTotalIngressRedFrames'
_L='adMefPerCosPerEvcTotalIngressYellowFrames'
_K='adMefPerCosPerEvcTotalIngressYellowOctets'
_J='adMefPerCosPerEvcTotalIngressGreenFrames'
_I='adMefPerCosPerEvcTotalIngressGreenOctets'
_H='not-accessible'
_G='adMefPerCosPerEvcTcQueueNumber'
_F='adMefPerCosPerEvcTcEvcNameFixedLen'
_E='Unsigned32'
_D='OctetString'
_C='read-only'
_B='ADTRAN-MEF-PER-COS-PER-EVC-TOTAL-COUNT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenAOSConformance,adGenAOSMef=mibBuilder.importSymbols('ADTRAN-AOS','adGenAOSConformance','adGenAOSMef')
adIdentity,=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity')
HCPerfCurrentCount,HCPerfIntervalCount,HCPerfInvalidIntervals,HCPerfTimeElapsed,HCPerfTotalCount,HCPerfValidIntervals=mibBuilder.importSymbols('HC-PerfHist-TC-MIB','HCPerfCurrentCount','HCPerfIntervalCount','HCPerfInvalidIntervals','HCPerfTimeElapsed','HCPerfTotalCount','HCPerfValidIntervals')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenAosMefPerCosPerEvcTotalCountMib=ModuleIdentity((1,3,6,1,4,1,664,6,10000,53,9,8))
if mibBuilder.loadTexts:adGenAosMefPerCosPerEvcTotalCountMib.setRevisions(('2017-10-14 00:00',))
_AdGenAosMefPerCosPerEvcTotalCount_ObjectIdentity=ObjectIdentity
adGenAosMefPerCosPerEvcTotalCount=_AdGenAosMefPerCosPerEvcTotalCount_ObjectIdentity((1,3,6,1,4,1,664,5,53,9,8))
_AdMefPerCosPerEvcTcTable_Object=MibTable
adMefPerCosPerEvcTcTable=_AdMefPerCosPerEvcTcTable_Object((1,3,6,1,4,1,664,5,53,9,8,1))
if mibBuilder.loadTexts:adMefPerCosPerEvcTcTable.setStatus(_A)
_AdMefPerCosPerEvcTcEntry_Object=MibTableRow
adMefPerCosPerEvcTcEntry=_AdMefPerCosPerEvcTcEntry_Object((1,3,6,1,4,1,664,5,53,9,8,1,1))
adMefPerCosPerEvcTcEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:adMefPerCosPerEvcTcEntry.setStatus(_A)
class _AdMefPerCosPerEvcTcEvcNameFixedLen_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(50,50));fixedLength=50
_AdMefPerCosPerEvcTcEvcNameFixedLen_Type.__name__=_D
_AdMefPerCosPerEvcTcEvcNameFixedLen_Object=MibTableColumn
adMefPerCosPerEvcTcEvcNameFixedLen=_AdMefPerCosPerEvcTcEvcNameFixedLen_Object((1,3,6,1,4,1,664,5,53,9,8,1,1,1),_AdMefPerCosPerEvcTcEvcNameFixedLen_Type())
adMefPerCosPerEvcTcEvcNameFixedLen.setMaxAccess(_H)
if mibBuilder.loadTexts:adMefPerCosPerEvcTcEvcNameFixedLen.setStatus(_A)
class _AdMefPerCosPerEvcTcQueueNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdMefPerCosPerEvcTcQueueNumber_Type.__name__=_E
_AdMefPerCosPerEvcTcQueueNumber_Object=MibTableColumn
adMefPerCosPerEvcTcQueueNumber=_AdMefPerCosPerEvcTcQueueNumber_Object((1,3,6,1,4,1,664,5,53,9,8,1,1,2),_AdMefPerCosPerEvcTcQueueNumber_Type())
adMefPerCosPerEvcTcQueueNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:adMefPerCosPerEvcTcQueueNumber.setStatus(_A)
_AdMefPerCosPerEvcTotalIngressGreenOctets_Type=HCPerfCurrentCount
_AdMefPerCosPerEvcTotalIngressGreenOctets_Object=MibTableColumn
adMefPerCosPerEvcTotalIngressGreenOctets=_AdMefPerCosPerEvcTotalIngressGreenOctets_Object((1,3,6,1,4,1,664,5,53,9,8,1,1,3),_AdMefPerCosPerEvcTotalIngressGreenOctets_Type())
adMefPerCosPerEvcTotalIngressGreenOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:adMefPerCosPerEvcTotalIngressGreenOctets.setStatus(_A)
_AdMefPerCosPerEvcTotalIngressGreenFrames_Type=HCPerfCurrentCount
_AdMefPerCosPerEvcTotalIngressGreenFrames_Object=MibTableColumn
adMefPerCosPerEvcTotalIngressGreenFrames=_AdMefPerCosPerEvcTotalIngressGreenFrames_Object((1,3,6,1,4,1,664,5,53,9,8,1,1,4),_AdMefPerCosPerEvcTotalIngressGreenFrames_Type())
adMefPerCosPerEvcTotalIngressGreenFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:adMefPerCosPerEvcTotalIngressGreenFrames.setStatus(_A)
_AdMefPerCosPerEvcTotalIngressYellowOctets_Type=HCPerfCurrentCount
_AdMefPerCosPerEvcTotalIngressYellowOctets_Object=MibTableColumn
adMefPerCosPerEvcTotalIngressYellowOctets=_AdMefPerCosPerEvcTotalIngressYellowOctets_Object((1,3,6,1,4,1,664,5,53,9,8,1,1,5),_AdMefPerCosPerEvcTotalIngressYellowOctets_Type())
adMefPerCosPerEvcTotalIngressYellowOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:adMefPerCosPerEvcTotalIngressYellowOctets.setStatus(_A)
_AdMefPerCosPerEvcTotalIngressYellowFrames_Type=HCPerfCurrentCount
_AdMefPerCosPerEvcTotalIngressYellowFrames_Object=MibTableColumn
adMefPerCosPerEvcTotalIngressYellowFrames=_AdMefPerCosPerEvcTotalIngressYellowFrames_Object((1,3,6,1,4,1,664,5,53,9,8,1,1,6),_AdMefPerCosPerEvcTotalIngressYellowFrames_Type())
adMefPerCosPerEvcTotalIngressYellowFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:adMefPerCosPerEvcTotalIngressYellowFrames.setStatus(_A)
_AdMefPerCosPerEvcTotalIngressRedFrames_Type=HCPerfCurrentCount
_AdMefPerCosPerEvcTotalIngressRedFrames_Object=MibTableColumn
adMefPerCosPerEvcTotalIngressRedFrames=_AdMefPerCosPerEvcTotalIngressRedFrames_Object((1,3,6,1,4,1,664,5,53,9,8,1,1,7),_AdMefPerCosPerEvcTotalIngressRedFrames_Type())
adMefPerCosPerEvcTotalIngressRedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:adMefPerCosPerEvcTotalIngressRedFrames.setStatus(_A)
_AdGenAosMefPerCosPerEvcTotalCountConformance_ObjectIdentity=ObjectIdentity
adGenAosMefPerCosPerEvcTotalCountConformance=_AdGenAosMefPerCosPerEvcTotalCountConformance_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,30))
_AdMefPerCosPerEvcTotalCountGroups_ObjectIdentity=ObjectIdentity
adMefPerCosPerEvcTotalCountGroups=_AdMefPerCosPerEvcTotalCountGroups_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,30,1))
_AdGenAosMefPerCosPerEvcTotalCountCompliances_ObjectIdentity=ObjectIdentity
adGenAosMefPerCosPerEvcTotalCountCompliances=_AdGenAosMefPerCosPerEvcTotalCountCompliances_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,30,2))
adMefPerCosPerEvcTotalCountGroup=ObjectGroup((1,3,6,1,4,1,664,5,53,99,30,1,1))
adMefPerCosPerEvcTotalCountGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:adMefPerCosPerEvcTotalCountGroup.setStatus(_A)
adGenAosMefPerUniTotalCountCompliance=ModuleCompliance((1,3,6,1,4,1,664,5,53,99,30,2,1))
adGenAosMefPerUniTotalCountCompliance.setObjects((_B,_N))
if mibBuilder.loadTexts:adGenAosMefPerUniTotalCountCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adGenAosMefPerCosPerEvcTotalCount':adGenAosMefPerCosPerEvcTotalCount,'adMefPerCosPerEvcTcTable':adMefPerCosPerEvcTcTable,'adMefPerCosPerEvcTcEntry':adMefPerCosPerEvcTcEntry,_F:adMefPerCosPerEvcTcEvcNameFixedLen,_G:adMefPerCosPerEvcTcQueueNumber,_I:adMefPerCosPerEvcTotalIngressGreenOctets,_J:adMefPerCosPerEvcTotalIngressGreenFrames,_K:adMefPerCosPerEvcTotalIngressYellowOctets,_L:adMefPerCosPerEvcTotalIngressYellowFrames,_M:adMefPerCosPerEvcTotalIngressRedFrames,'adGenAosMefPerCosPerEvcTotalCountConformance':adGenAosMefPerCosPerEvcTotalCountConformance,'adMefPerCosPerEvcTotalCountGroups':adMefPerCosPerEvcTotalCountGroups,_N:adMefPerCosPerEvcTotalCountGroup,'adGenAosMefPerCosPerEvcTotalCountCompliances':adGenAosMefPerCosPerEvcTotalCountCompliances,'adGenAosMefPerUniTotalCountCompliance':adGenAosMefPerUniTotalCountCompliance,'adGenAosMefPerCosPerEvcTotalCountMib':adGenAosMefPerCosPerEvcTotalCountMib})