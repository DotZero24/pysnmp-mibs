_M='adMefPerCosPerUniTotalCountGroup'
_L='adMefPerCosPerUniTotalIngressRedFrames'
_K='adMefPerCosPerUniTotalIngressYellowFrames'
_J='adMefPerCosPerUniTotalIngressYellowOctets'
_I='adMefPerCosPerUniTotalIngressGreenFrames'
_H='adMefPerCosPerUniTotalIngressGreenOctets'
_G='adMefPerCosPerUniTcQueueNumber'
_F='Unsigned32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='ADTRAN-MEF-PER-COS-PER-UNI-TOTAL-COUNT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenAOSConformance,adGenAOSMef=mibBuilder.importSymbols('ADTRAN-AOS','adGenAOSConformance','adGenAOSMef')
adIdentity,=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity')
HCPerfCurrentCount,HCPerfIntervalCount,HCPerfInvalidIntervals,HCPerfTimeElapsed,HCPerfTotalCount,HCPerfValidIntervals=mibBuilder.importSymbols('HC-PerfHist-TC-MIB','HCPerfCurrentCount','HCPerfIntervalCount','HCPerfInvalidIntervals','HCPerfTimeElapsed','HCPerfTotalCount','HCPerfValidIntervals')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenAosMefPerCosPerUniTotalCountMib=ModuleIdentity((1,3,6,1,4,1,664,6,10000,53,9,6))
if mibBuilder.loadTexts:adGenAosMefPerCosPerUniTotalCountMib.setRevisions(('2017-10-14 00:00',))
_AdGenAosMefPerCosPerUniTotalCount_ObjectIdentity=ObjectIdentity
adGenAosMefPerCosPerUniTotalCount=_AdGenAosMefPerCosPerUniTotalCount_ObjectIdentity((1,3,6,1,4,1,664,5,53,9,6))
_AdMefPerCosPerUniTcTable_Object=MibTable
adMefPerCosPerUniTcTable=_AdMefPerCosPerUniTcTable_Object((1,3,6,1,4,1,664,5,53,9,6,1))
if mibBuilder.loadTexts:adMefPerCosPerUniTcTable.setStatus(_A)
_AdMefPerCosPerUniTcEntry_Object=MibTableRow
adMefPerCosPerUniTcEntry=_AdMefPerCosPerUniTcEntry_Object((1,3,6,1,4,1,664,5,53,9,6,1,1))
adMefPerCosPerUniTcEntry.setIndexNames((0,_D,_E),(0,_B,_G))
if mibBuilder.loadTexts:adMefPerCosPerUniTcEntry.setStatus(_A)
class _AdMefPerCosPerUniTcQueueNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdMefPerCosPerUniTcQueueNumber_Type.__name__=_F
_AdMefPerCosPerUniTcQueueNumber_Object=MibTableColumn
adMefPerCosPerUniTcQueueNumber=_AdMefPerCosPerUniTcQueueNumber_Object((1,3,6,1,4,1,664,5,53,9,6,1,1,1),_AdMefPerCosPerUniTcQueueNumber_Type())
adMefPerCosPerUniTcQueueNumber.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:adMefPerCosPerUniTcQueueNumber.setStatus(_A)
_AdMefPerCosPerUniTotalIngressGreenOctets_Type=HCPerfCurrentCount
_AdMefPerCosPerUniTotalIngressGreenOctets_Object=MibTableColumn
adMefPerCosPerUniTotalIngressGreenOctets=_AdMefPerCosPerUniTotalIngressGreenOctets_Object((1,3,6,1,4,1,664,5,53,9,6,1,1,2),_AdMefPerCosPerUniTotalIngressGreenOctets_Type())
adMefPerCosPerUniTotalIngressGreenOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:adMefPerCosPerUniTotalIngressGreenOctets.setStatus(_A)
_AdMefPerCosPerUniTotalIngressGreenFrames_Type=HCPerfCurrentCount
_AdMefPerCosPerUniTotalIngressGreenFrames_Object=MibTableColumn
adMefPerCosPerUniTotalIngressGreenFrames=_AdMefPerCosPerUniTotalIngressGreenFrames_Object((1,3,6,1,4,1,664,5,53,9,6,1,1,3),_AdMefPerCosPerUniTotalIngressGreenFrames_Type())
adMefPerCosPerUniTotalIngressGreenFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:adMefPerCosPerUniTotalIngressGreenFrames.setStatus(_A)
_AdMefPerCosPerUniTotalIngressYellowOctets_Type=HCPerfCurrentCount
_AdMefPerCosPerUniTotalIngressYellowOctets_Object=MibTableColumn
adMefPerCosPerUniTotalIngressYellowOctets=_AdMefPerCosPerUniTotalIngressYellowOctets_Object((1,3,6,1,4,1,664,5,53,9,6,1,1,4),_AdMefPerCosPerUniTotalIngressYellowOctets_Type())
adMefPerCosPerUniTotalIngressYellowOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:adMefPerCosPerUniTotalIngressYellowOctets.setStatus(_A)
_AdMefPerCosPerUniTotalIngressYellowFrames_Type=HCPerfCurrentCount
_AdMefPerCosPerUniTotalIngressYellowFrames_Object=MibTableColumn
adMefPerCosPerUniTotalIngressYellowFrames=_AdMefPerCosPerUniTotalIngressYellowFrames_Object((1,3,6,1,4,1,664,5,53,9,6,1,1,5),_AdMefPerCosPerUniTotalIngressYellowFrames_Type())
adMefPerCosPerUniTotalIngressYellowFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:adMefPerCosPerUniTotalIngressYellowFrames.setStatus(_A)
_AdMefPerCosPerUniTotalIngressRedFrames_Type=HCPerfCurrentCount
_AdMefPerCosPerUniTotalIngressRedFrames_Object=MibTableColumn
adMefPerCosPerUniTotalIngressRedFrames=_AdMefPerCosPerUniTotalIngressRedFrames_Object((1,3,6,1,4,1,664,5,53,9,6,1,1,6),_AdMefPerCosPerUniTotalIngressRedFrames_Type())
adMefPerCosPerUniTotalIngressRedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:adMefPerCosPerUniTotalIngressRedFrames.setStatus(_A)
_AdGenAosMefPerCosPerUniTotalCountConformance_ObjectIdentity=ObjectIdentity
adGenAosMefPerCosPerUniTotalCountConformance=_AdGenAosMefPerCosPerUniTotalCountConformance_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,28))
_AdMefPerCosPerUniTotalCountGroups_ObjectIdentity=ObjectIdentity
adMefPerCosPerUniTotalCountGroups=_AdMefPerCosPerUniTotalCountGroups_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,28,1))
_AdGenAosMefPerCosPerUniTotalCountCompliances_ObjectIdentity=ObjectIdentity
adGenAosMefPerCosPerUniTotalCountCompliances=_AdGenAosMefPerCosPerUniTotalCountCompliances_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,28,2))
adMefPerCosPerUniTotalCountGroup=ObjectGroup((1,3,6,1,4,1,664,5,53,99,28,1,1))
adMefPerCosPerUniTotalCountGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:adMefPerCosPerUniTotalCountGroup.setStatus(_A)
adGenAosMefPerUniTotalCountCompliance=ModuleCompliance((1,3,6,1,4,1,664,5,53,99,28,2,1))
adGenAosMefPerUniTotalCountCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:adGenAosMefPerUniTotalCountCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adGenAosMefPerCosPerUniTotalCount':adGenAosMefPerCosPerUniTotalCount,'adMefPerCosPerUniTcTable':adMefPerCosPerUniTcTable,'adMefPerCosPerUniTcEntry':adMefPerCosPerUniTcEntry,_G:adMefPerCosPerUniTcQueueNumber,_H:adMefPerCosPerUniTotalIngressGreenOctets,_I:adMefPerCosPerUniTotalIngressGreenFrames,_J:adMefPerCosPerUniTotalIngressYellowOctets,_K:adMefPerCosPerUniTotalIngressYellowFrames,_L:adMefPerCosPerUniTotalIngressRedFrames,'adGenAosMefPerCosPerUniTotalCountConformance':adGenAosMefPerCosPerUniTotalCountConformance,'adMefPerCosPerUniTotalCountGroups':adMefPerCosPerUniTotalCountGroups,_M:adMefPerCosPerUniTotalCountGroup,'adGenAosMefPerCosPerUniTotalCountCompliances':adGenAosMefPerCosPerUniTotalCountCompliances,'adGenAosMefPerUniTotalCountCompliance':adGenAosMefPerUniTotalCountCompliance,'adGenAosMefPerCosPerUniTotalCountMib':adGenAosMefPerCosPerUniTotalCountMib})