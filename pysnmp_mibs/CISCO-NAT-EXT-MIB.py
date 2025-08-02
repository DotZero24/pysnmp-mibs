_L='ciscoNatExtAddrTransStatsGroup'
_K='cneAddrTranslation5min'
_J='cneAddrTranslation1min'
_I='cneAddrTranslationNumPeak'
_H='cneAddrTranslationNumActive'
_G='Address translation entries per second'
_F='Number of address translation entries'
_E='entPhysicalIndex'
_D='ENTITY-MIB'
_C='read-only'
_B='CISCO-NAT-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoNATExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,532))
if mibBuilder.loadTexts:ciscoNATExtMIB.setRevisions(('2006-06-05 00:00',))
_CiscoNatExtMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoNatExtMIBNotifs=_CiscoNatExtMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,532,0))
_CiscoNatExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoNatExtMIBObjects=_CiscoNatExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,532,1))
_CneAddrTranslationStatsTable_Object=MibTable
cneAddrTranslationStatsTable=_CneAddrTranslationStatsTable_Object((1,3,6,1,4,1,9,9,532,1,1))
if mibBuilder.loadTexts:cneAddrTranslationStatsTable.setStatus(_A)
_CneAddrTranslationStatsEntry_Object=MibTableRow
cneAddrTranslationStatsEntry=_CneAddrTranslationStatsEntry_Object((1,3,6,1,4,1,9,9,532,1,1,1))
cneAddrTranslationStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cneAddrTranslationStatsEntry.setStatus(_A)
_CneAddrTranslationNumActive_Type=Gauge32
_CneAddrTranslationNumActive_Object=MibTableColumn
cneAddrTranslationNumActive=_CneAddrTranslationNumActive_Object((1,3,6,1,4,1,9,9,532,1,1,1,1),_CneAddrTranslationNumActive_Type())
cneAddrTranslationNumActive.setMaxAccess(_C)
if mibBuilder.loadTexts:cneAddrTranslationNumActive.setStatus(_A)
if mibBuilder.loadTexts:cneAddrTranslationNumActive.setUnits(_F)
_CneAddrTranslationNumPeak_Type=Unsigned32
_CneAddrTranslationNumPeak_Object=MibTableColumn
cneAddrTranslationNumPeak=_CneAddrTranslationNumPeak_Object((1,3,6,1,4,1,9,9,532,1,1,1,2),_CneAddrTranslationNumPeak_Type())
cneAddrTranslationNumPeak.setMaxAccess(_C)
if mibBuilder.loadTexts:cneAddrTranslationNumPeak.setStatus(_A)
if mibBuilder.loadTexts:cneAddrTranslationNumPeak.setUnits(_F)
_CneAddrTranslation1min_Type=Gauge32
_CneAddrTranslation1min_Object=MibTableColumn
cneAddrTranslation1min=_CneAddrTranslation1min_Object((1,3,6,1,4,1,9,9,532,1,1,1,3),_CneAddrTranslation1min_Type())
cneAddrTranslation1min.setMaxAccess(_C)
if mibBuilder.loadTexts:cneAddrTranslation1min.setStatus(_A)
if mibBuilder.loadTexts:cneAddrTranslation1min.setUnits(_G)
_CneAddrTranslation5min_Type=Gauge32
_CneAddrTranslation5min_Object=MibTableColumn
cneAddrTranslation5min=_CneAddrTranslation5min_Object((1,3,6,1,4,1,9,9,532,1,1,1,4),_CneAddrTranslation5min_Type())
cneAddrTranslation5min.setMaxAccess(_C)
if mibBuilder.loadTexts:cneAddrTranslation5min.setStatus(_A)
if mibBuilder.loadTexts:cneAddrTranslation5min.setUnits(_G)
_CiscoNatExtMIBConformance_ObjectIdentity=ObjectIdentity
ciscoNatExtMIBConformance=_CiscoNatExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,532,2))
_CiscoNatExtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoNatExtMIBCompliances=_CiscoNatExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,532,2,1))
_CiscoNatExtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoNatExtMIBGroups=_CiscoNatExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,532,2,2))
ciscoNatExtAddrTransStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,532,2,2,1))
ciscoNatExtAddrTransStatsGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:ciscoNatExtAddrTransStatsGroup.setStatus(_A)
ciscoNatExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,532,2,1,1))
ciscoNatExtMIBCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:ciscoNatExtMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoNATExtMIB':ciscoNATExtMIB,'ciscoNatExtMIBNotifs':ciscoNatExtMIBNotifs,'ciscoNatExtMIBObjects':ciscoNatExtMIBObjects,'cneAddrTranslationStatsTable':cneAddrTranslationStatsTable,'cneAddrTranslationStatsEntry':cneAddrTranslationStatsEntry,_H:cneAddrTranslationNumActive,_I:cneAddrTranslationNumPeak,_J:cneAddrTranslation1min,_K:cneAddrTranslation5min,'ciscoNatExtMIBConformance':ciscoNatExtMIBConformance,'ciscoNatExtMIBCompliances':ciscoNatExtMIBCompliances,'ciscoNatExtMIBCompliance':ciscoNatExtMIBCompliance,'ciscoNatExtMIBGroups':ciscoNatExtMIBGroups,_L:ciscoNatExtAddrTransStatsGroup})