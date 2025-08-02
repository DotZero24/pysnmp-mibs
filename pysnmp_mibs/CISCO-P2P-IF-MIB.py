_N='ciscoP2PIfMIBGeneralGroup'
_M='cp2pIfStatsInCrcErrors'
_L='cp2pIfCfgTransmitDelay'
_K='cp2pIfCfgScramblingMode'
_J='cp2pIfCfgCrcMode'
_I='cp2pIfStatsEntry'
_H='Cp2pIfScramblingMode'
_G='Cp2pIfCrcMode'
_F='Unsigned32'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='CISCO-P2P-IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoP2PIfMIB=ModuleIdentity((1,3,6,1,4,1,9,9,668))
if mibBuilder.loadTexts:ciscoP2PIfMIB.setRevisions(('2008-08-12 00:00',))
class Cp2pIfCrcMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('crc16',1),('crc32',2)))
class Cp2pIfScramblingMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_CiscoP2PIfMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoP2PIfMIBNotifs=_CiscoP2PIfMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,668,0))
_CiscoP2PIfMIBObjects_ObjectIdentity=ObjectIdentity
ciscoP2PIfMIBObjects=_CiscoP2PIfMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,668,1))
_Cp2pIfGeneralObjects_ObjectIdentity=ObjectIdentity
cp2pIfGeneralObjects=_Cp2pIfGeneralObjects_ObjectIdentity((1,3,6,1,4,1,9,9,668,1,1))
_Cp2pIfCfgTable_Object=MibTable
cp2pIfCfgTable=_Cp2pIfCfgTable_Object((1,3,6,1,4,1,9,9,668,1,1,1))
if mibBuilder.loadTexts:cp2pIfCfgTable.setStatus(_A)
_Cp2pIfCfgEntry_Object=MibTableRow
cp2pIfCfgEntry=_Cp2pIfCfgEntry_Object((1,3,6,1,4,1,9,9,668,1,1,1,1))
cp2pIfCfgEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cp2pIfCfgEntry.setStatus(_A)
class _Cp2pIfCfgCrcMode_Type(Cp2pIfCrcMode):defaultValue=2
_Cp2pIfCfgCrcMode_Type.__name__=_G
_Cp2pIfCfgCrcMode_Object=MibTableColumn
cp2pIfCfgCrcMode=_Cp2pIfCfgCrcMode_Object((1,3,6,1,4,1,9,9,668,1,1,1,1,1),_Cp2pIfCfgCrcMode_Type())
cp2pIfCfgCrcMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cp2pIfCfgCrcMode.setStatus(_A)
class _Cp2pIfCfgScramblingMode_Type(Cp2pIfScramblingMode):defaultValue=2
_Cp2pIfCfgScramblingMode_Type.__name__=_H
_Cp2pIfCfgScramblingMode_Object=MibTableColumn
cp2pIfCfgScramblingMode=_Cp2pIfCfgScramblingMode_Object((1,3,6,1,4,1,9,9,668,1,1,1,1,2),_Cp2pIfCfgScramblingMode_Type())
cp2pIfCfgScramblingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cp2pIfCfgScramblingMode.setStatus(_A)
class _Cp2pIfCfgTransmitDelay_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,18000))
_Cp2pIfCfgTransmitDelay_Type.__name__=_F
_Cp2pIfCfgTransmitDelay_Object=MibTableColumn
cp2pIfCfgTransmitDelay=_Cp2pIfCfgTransmitDelay_Object((1,3,6,1,4,1,9,9,668,1,1,1,1,3),_Cp2pIfCfgTransmitDelay_Type())
cp2pIfCfgTransmitDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cp2pIfCfgTransmitDelay.setStatus(_A)
if mibBuilder.loadTexts:cp2pIfCfgTransmitDelay.setUnits('microseconds')
_Cp2pIfStatsTable_Object=MibTable
cp2pIfStatsTable=_Cp2pIfStatsTable_Object((1,3,6,1,4,1,9,9,668,1,1,2))
if mibBuilder.loadTexts:cp2pIfStatsTable.setStatus(_A)
_Cp2pIfStatsEntry_Object=MibTableRow
cp2pIfStatsEntry=_Cp2pIfStatsEntry_Object((1,3,6,1,4,1,9,9,668,1,1,2,1))
if mibBuilder.loadTexts:cp2pIfStatsEntry.setStatus(_A)
_Cp2pIfStatsInCrcErrors_Type=Counter32
_Cp2pIfStatsInCrcErrors_Object=MibTableColumn
cp2pIfStatsInCrcErrors=_Cp2pIfStatsInCrcErrors_Object((1,3,6,1,4,1,9,9,668,1,1,2,1,1),_Cp2pIfStatsInCrcErrors_Type())
cp2pIfStatsInCrcErrors.setMaxAccess('read-only')
if mibBuilder.loadTexts:cp2pIfStatsInCrcErrors.setStatus(_A)
_CiscoP2PIfMIBConformance_ObjectIdentity=ObjectIdentity
ciscoP2PIfMIBConformance=_CiscoP2PIfMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,668,3))
_CiscoP2PIfMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoP2PIfMIBCompliances=_CiscoP2PIfMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,668,3,1))
_CiscoP2PIfMIBGroups_ObjectIdentity=ObjectIdentity
ciscoP2PIfMIBGroups=_CiscoP2PIfMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,668,3,2))
cp2pIfCfgEntry.registerAugmentions((_B,_I))
cp2pIfStatsEntry.setIndexNames(*cp2pIfCfgEntry.getIndexNames())
ciscoP2PIfMIBGeneralGroup=ObjectGroup((1,3,6,1,4,1,9,9,668,3,2,1))
ciscoP2PIfMIBGeneralGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:ciscoP2PIfMIBGeneralGroup.setStatus(_A)
ciscoP2PIfMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,668,3,1,1))
ciscoP2PIfMIBCompliance.setObjects((_B,_N))
if mibBuilder.loadTexts:ciscoP2PIfMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_G:Cp2pIfCrcMode,_H:Cp2pIfScramblingMode,'ciscoP2PIfMIB':ciscoP2PIfMIB,'ciscoP2PIfMIBNotifs':ciscoP2PIfMIBNotifs,'ciscoP2PIfMIBObjects':ciscoP2PIfMIBObjects,'cp2pIfGeneralObjects':cp2pIfGeneralObjects,'cp2pIfCfgTable':cp2pIfCfgTable,'cp2pIfCfgEntry':cp2pIfCfgEntry,_J:cp2pIfCfgCrcMode,_K:cp2pIfCfgScramblingMode,_L:cp2pIfCfgTransmitDelay,'cp2pIfStatsTable':cp2pIfStatsTable,_I:cp2pIfStatsEntry,_M:cp2pIfStatsInCrcErrors,'ciscoP2PIfMIBConformance':ciscoP2PIfMIBConformance,'ciscoP2PIfMIBCompliances':ciscoP2PIfMIBCompliances,'ciscoP2PIfMIBCompliance':ciscoP2PIfMIBCompliance,'ciscoP2PIfMIBGroups':ciscoP2PIfMIBGroups,_N:ciscoP2PIfMIBGeneralGroup})