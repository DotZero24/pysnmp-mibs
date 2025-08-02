_K='adMefPerUniTotalCountGroup'
_J='adMefPerUniTotalIngressRedFrames'
_I='adMefPerUniTotalIngressYellowFrames'
_H='adMefPerUniTotalIngressYellowOctets'
_G='adMefPerUniTotalIngressGreenFrames'
_F='adMefPerUniTotalIngressGreenOctets'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='ADTRAN-MEF-PER-UNI-TOTAL-COUNT-MIB'
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
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenAosMefPerUniTotalCountMib=ModuleIdentity((1,3,6,1,4,1,664,6,10000,53,9,5))
if mibBuilder.loadTexts:adGenAosMefPerUniTotalCountMib.setRevisions(('2017-10-14 00:00',))
_AdGenAosMefPerUniTotalCount_ObjectIdentity=ObjectIdentity
adGenAosMefPerUniTotalCount=_AdGenAosMefPerUniTotalCount_ObjectIdentity((1,3,6,1,4,1,664,5,53,9,5))
_AdMefPerUniTcTable_Object=MibTable
adMefPerUniTcTable=_AdMefPerUniTcTable_Object((1,3,6,1,4,1,664,5,53,9,5,1))
if mibBuilder.loadTexts:adMefPerUniTcTable.setStatus(_A)
_AdMefPerUniTcEntry_Object=MibTableRow
adMefPerUniTcEntry=_AdMefPerUniTcEntry_Object((1,3,6,1,4,1,664,5,53,9,5,1,1))
adMefPerUniTcEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:adMefPerUniTcEntry.setStatus(_A)
_AdMefPerUniTotalIngressGreenOctets_Type=HCPerfCurrentCount
_AdMefPerUniTotalIngressGreenOctets_Object=MibTableColumn
adMefPerUniTotalIngressGreenOctets=_AdMefPerUniTotalIngressGreenOctets_Object((1,3,6,1,4,1,664,5,53,9,5,1,1,1),_AdMefPerUniTotalIngressGreenOctets_Type())
adMefPerUniTotalIngressGreenOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:adMefPerUniTotalIngressGreenOctets.setStatus(_A)
_AdMefPerUniTotalIngressGreenFrames_Type=HCPerfCurrentCount
_AdMefPerUniTotalIngressGreenFrames_Object=MibTableColumn
adMefPerUniTotalIngressGreenFrames=_AdMefPerUniTotalIngressGreenFrames_Object((1,3,6,1,4,1,664,5,53,9,5,1,1,2),_AdMefPerUniTotalIngressGreenFrames_Type())
adMefPerUniTotalIngressGreenFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:adMefPerUniTotalIngressGreenFrames.setStatus(_A)
_AdMefPerUniTotalIngressYellowOctets_Type=HCPerfCurrentCount
_AdMefPerUniTotalIngressYellowOctets_Object=MibTableColumn
adMefPerUniTotalIngressYellowOctets=_AdMefPerUniTotalIngressYellowOctets_Object((1,3,6,1,4,1,664,5,53,9,5,1,1,3),_AdMefPerUniTotalIngressYellowOctets_Type())
adMefPerUniTotalIngressYellowOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:adMefPerUniTotalIngressYellowOctets.setStatus(_A)
_AdMefPerUniTotalIngressYellowFrames_Type=HCPerfCurrentCount
_AdMefPerUniTotalIngressYellowFrames_Object=MibTableColumn
adMefPerUniTotalIngressYellowFrames=_AdMefPerUniTotalIngressYellowFrames_Object((1,3,6,1,4,1,664,5,53,9,5,1,1,4),_AdMefPerUniTotalIngressYellowFrames_Type())
adMefPerUniTotalIngressYellowFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:adMefPerUniTotalIngressYellowFrames.setStatus(_A)
_AdMefPerUniTotalIngressRedFrames_Type=HCPerfCurrentCount
_AdMefPerUniTotalIngressRedFrames_Object=MibTableColumn
adMefPerUniTotalIngressRedFrames=_AdMefPerUniTotalIngressRedFrames_Object((1,3,6,1,4,1,664,5,53,9,5,1,1,5),_AdMefPerUniTotalIngressRedFrames_Type())
adMefPerUniTotalIngressRedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:adMefPerUniTotalIngressRedFrames.setStatus(_A)
_AdGenAosMefPerUniTotalCountConformance_ObjectIdentity=ObjectIdentity
adGenAosMefPerUniTotalCountConformance=_AdGenAosMefPerUniTotalCountConformance_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,27))
_AdMefPerUniTotalCountGroups_ObjectIdentity=ObjectIdentity
adMefPerUniTotalCountGroups=_AdMefPerUniTotalCountGroups_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,27,1))
_AdGenAosMefPerUniTotalCountCompliances_ObjectIdentity=ObjectIdentity
adGenAosMefPerUniTotalCountCompliances=_AdGenAosMefPerUniTotalCountCompliances_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,27,2))
adMefPerUniTotalCountGroup=ObjectGroup((1,3,6,1,4,1,664,5,53,99,27,1,1))
adMefPerUniTotalCountGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:adMefPerUniTotalCountGroup.setStatus(_A)
adGenAosMefPerUniTotalCountCompliance=ModuleCompliance((1,3,6,1,4,1,664,5,53,99,27,2,1))
adGenAosMefPerUniTotalCountCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:adGenAosMefPerUniTotalCountCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adGenAosMefPerUniTotalCount':adGenAosMefPerUniTotalCount,'adMefPerUniTcTable':adMefPerUniTcTable,'adMefPerUniTcEntry':adMefPerUniTcEntry,_F:adMefPerUniTotalIngressGreenOctets,_G:adMefPerUniTotalIngressGreenFrames,_H:adMefPerUniTotalIngressYellowOctets,_I:adMefPerUniTotalIngressYellowFrames,_J:adMefPerUniTotalIngressRedFrames,'adGenAosMefPerUniTotalCountConformance':adGenAosMefPerUniTotalCountConformance,'adMefPerUniTotalCountGroups':adMefPerUniTotalCountGroups,_K:adMefPerUniTotalCountGroup,'adGenAosMefPerUniTotalCountCompliances':adGenAosMefPerUniTotalCountCompliances,'adGenAosMefPerUniTotalCountCompliance':adGenAosMefPerUniTotalCountCompliance,'adGenAosMefPerUniTotalCountMib':adGenAosMefPerUniTotalCountMib})