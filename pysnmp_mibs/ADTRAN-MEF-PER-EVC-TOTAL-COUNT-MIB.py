_K='adMefPerEvcTotalCountGroup'
_J='adMefPerEvcTotalIngressRedFrames'
_I='adMefPerEvcTotalIngressYellowFrames'
_H='adMefPerEvcTotalIngressYellowOctets'
_G='adMefPerEvcTotalIngressGreenFrames'
_F='adMefPerEvcTotalIngressGreenOctets'
_E='adMefPerEvcTcEvcNameFixedLen'
_D='OctetString'
_C='read-only'
_B='ADTRAN-MEF-PER-EVC-TOTAL-COUNT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenAOSConformance,adGenAOSMef=mibBuilder.importSymbols('ADTRAN-AOS','adGenAOSConformance','adGenAOSMef')
adIdentity,=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity')
HCPerfCurrentCount,HCPerfIntervalCount,HCPerfInvalidIntervals,HCPerfTimeElapsed,HCPerfTotalCount,HCPerfValidIntervals=mibBuilder.importSymbols('HC-PerfHist-TC-MIB','HCPerfCurrentCount','HCPerfIntervalCount','HCPerfInvalidIntervals','HCPerfTimeElapsed','HCPerfTotalCount','HCPerfValidIntervals')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenAosMefPerEvcTotalCountMib=ModuleIdentity((1,3,6,1,4,1,664,6,10000,53,9,7))
if mibBuilder.loadTexts:adGenAosMefPerEvcTotalCountMib.setRevisions(('2017-10-14 00:00',))
_AdGenAosMefPerEvcTotalCount_ObjectIdentity=ObjectIdentity
adGenAosMefPerEvcTotalCount=_AdGenAosMefPerEvcTotalCount_ObjectIdentity((1,3,6,1,4,1,664,5,53,9,7))
_AdMefPerEvcTcTable_Object=MibTable
adMefPerEvcTcTable=_AdMefPerEvcTcTable_Object((1,3,6,1,4,1,664,5,53,9,7,1))
if mibBuilder.loadTexts:adMefPerEvcTcTable.setStatus(_A)
_AdMefPerEvcTcEntry_Object=MibTableRow
adMefPerEvcTcEntry=_AdMefPerEvcTcEntry_Object((1,3,6,1,4,1,664,5,53,9,7,1,1))
adMefPerEvcTcEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:adMefPerEvcTcEntry.setStatus(_A)
class _AdMefPerEvcTcEvcNameFixedLen_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(50,50));fixedLength=50
_AdMefPerEvcTcEvcNameFixedLen_Type.__name__=_D
_AdMefPerEvcTcEvcNameFixedLen_Object=MibTableColumn
adMefPerEvcTcEvcNameFixedLen=_AdMefPerEvcTcEvcNameFixedLen_Object((1,3,6,1,4,1,664,5,53,9,7,1,1,1),_AdMefPerEvcTcEvcNameFixedLen_Type())
adMefPerEvcTcEvcNameFixedLen.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:adMefPerEvcTcEvcNameFixedLen.setStatus(_A)
_AdMefPerEvcTotalIngressGreenOctets_Type=HCPerfCurrentCount
_AdMefPerEvcTotalIngressGreenOctets_Object=MibTableColumn
adMefPerEvcTotalIngressGreenOctets=_AdMefPerEvcTotalIngressGreenOctets_Object((1,3,6,1,4,1,664,5,53,9,7,1,1,2),_AdMefPerEvcTotalIngressGreenOctets_Type())
adMefPerEvcTotalIngressGreenOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:adMefPerEvcTotalIngressGreenOctets.setStatus(_A)
_AdMefPerEvcTotalIngressGreenFrames_Type=HCPerfCurrentCount
_AdMefPerEvcTotalIngressGreenFrames_Object=MibTableColumn
adMefPerEvcTotalIngressGreenFrames=_AdMefPerEvcTotalIngressGreenFrames_Object((1,3,6,1,4,1,664,5,53,9,7,1,1,3),_AdMefPerEvcTotalIngressGreenFrames_Type())
adMefPerEvcTotalIngressGreenFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:adMefPerEvcTotalIngressGreenFrames.setStatus(_A)
_AdMefPerEvcTotalIngressYellowOctets_Type=HCPerfCurrentCount
_AdMefPerEvcTotalIngressYellowOctets_Object=MibTableColumn
adMefPerEvcTotalIngressYellowOctets=_AdMefPerEvcTotalIngressYellowOctets_Object((1,3,6,1,4,1,664,5,53,9,7,1,1,4),_AdMefPerEvcTotalIngressYellowOctets_Type())
adMefPerEvcTotalIngressYellowOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:adMefPerEvcTotalIngressYellowOctets.setStatus(_A)
_AdMefPerEvcTotalIngressYellowFrames_Type=HCPerfCurrentCount
_AdMefPerEvcTotalIngressYellowFrames_Object=MibTableColumn
adMefPerEvcTotalIngressYellowFrames=_AdMefPerEvcTotalIngressYellowFrames_Object((1,3,6,1,4,1,664,5,53,9,7,1,1,5),_AdMefPerEvcTotalIngressYellowFrames_Type())
adMefPerEvcTotalIngressYellowFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:adMefPerEvcTotalIngressYellowFrames.setStatus(_A)
_AdMefPerEvcTotalIngressRedFrames_Type=HCPerfCurrentCount
_AdMefPerEvcTotalIngressRedFrames_Object=MibTableColumn
adMefPerEvcTotalIngressRedFrames=_AdMefPerEvcTotalIngressRedFrames_Object((1,3,6,1,4,1,664,5,53,9,7,1,1,6),_AdMefPerEvcTotalIngressRedFrames_Type())
adMefPerEvcTotalIngressRedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:adMefPerEvcTotalIngressRedFrames.setStatus(_A)
_AdGenAosMefPerEvcTotalCountConformance_ObjectIdentity=ObjectIdentity
adGenAosMefPerEvcTotalCountConformance=_AdGenAosMefPerEvcTotalCountConformance_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,29))
_AdMefPerEvcTotalCountGroups_ObjectIdentity=ObjectIdentity
adMefPerEvcTotalCountGroups=_AdMefPerEvcTotalCountGroups_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,29,1))
_AdGenAosMefPerEvcTotalCountCompliances_ObjectIdentity=ObjectIdentity
adGenAosMefPerEvcTotalCountCompliances=_AdGenAosMefPerEvcTotalCountCompliances_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,29,2))
adMefPerEvcTotalCountGroup=ObjectGroup((1,3,6,1,4,1,664,5,53,99,29,1,1))
adMefPerEvcTotalCountGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:adMefPerEvcTotalCountGroup.setStatus(_A)
adGenAosMefPerEvcTotalCountCompliance=ModuleCompliance((1,3,6,1,4,1,664,5,53,99,29,2,1))
adGenAosMefPerEvcTotalCountCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:adGenAosMefPerEvcTotalCountCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adGenAosMefPerEvcTotalCount':adGenAosMefPerEvcTotalCount,'adMefPerEvcTcTable':adMefPerEvcTcTable,'adMefPerEvcTcEntry':adMefPerEvcTcEntry,_E:adMefPerEvcTcEvcNameFixedLen,_F:adMefPerEvcTotalIngressGreenOctets,_G:adMefPerEvcTotalIngressGreenFrames,_H:adMefPerEvcTotalIngressYellowOctets,_I:adMefPerEvcTotalIngressYellowFrames,_J:adMefPerEvcTotalIngressRedFrames,'adGenAosMefPerEvcTotalCountConformance':adGenAosMefPerEvcTotalCountConformance,'adMefPerEvcTotalCountGroups':adMefPerEvcTotalCountGroups,_K:adMefPerEvcTotalCountGroup,'adGenAosMefPerEvcTotalCountCompliances':adGenAosMefPerEvcTotalCountCompliances,'adGenAosMefPerEvcTotalCountCompliance':adGenAosMefPerEvcTotalCountCompliance,'adGenAosMefPerEvcTotalCountMib':adGenAosMefPerEvcTotalCountMib})