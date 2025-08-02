_O='ciscoSlogEventExtStatsGroup'
_N='ciscoSlogEventExtConfigGroup'
_M='cslogEventDispositionCount'
_L='cslogEventDisposition'
_K='cslogEventSeverityDispHtmlConsol'
_J='cslogEventSeverityDispHtmlGUI'
_I='cslogEventSeverityDispConsole'
_H='cslogEventDetailDefault'
_G='CslogEventDisposition'
_F='cslogEventDispositionSeverity'
_E='Integer32'
_D='SyslogSeverity'
_C='read-write'
_B='CISCO-SYSLOG-EVENT-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SyslogSeverity,=mibBuilder.importSymbols('CISCO-SYSLOG-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoSyslogEventExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,270))
if mibBuilder.loadTexts:ciscoSyslogEventExtMIB.setRevisions(('2002-02-12 00:00',))
class CslogEventDisposition(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('none',0),('count',1),('display',2),('notify',3)))
_CiscoSyslogEventExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSyslogEventExtMIBObjects=_CiscoSyslogEventExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,270,1))
_CslogEventConfig_ObjectIdentity=ObjectIdentity
cslogEventConfig=_CslogEventConfig_ObjectIdentity((1,3,6,1,4,1,9,9,270,1,1))
class _CslogEventDetailDefault_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('noDisplay',1),('sparseDetail',2),('normalDetail',3),('verboseDetail',4),('exhaustiveDetail',5)))
_CslogEventDetailDefault_Type.__name__=_E
_CslogEventDetailDefault_Object=MibScalar
cslogEventDetailDefault=_CslogEventDetailDefault_Object((1,3,6,1,4,1,9,9,270,1,1,1),_CslogEventDetailDefault_Type())
cslogEventDetailDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:cslogEventDetailDefault.setStatus(_A)
class _CslogEventSeverityDispConsole_Type(SyslogSeverity):defaultValue=7
_CslogEventSeverityDispConsole_Type.__name__=_D
_CslogEventSeverityDispConsole_Object=MibScalar
cslogEventSeverityDispConsole=_CslogEventSeverityDispConsole_Object((1,3,6,1,4,1,9,9,270,1,1,2),_CslogEventSeverityDispConsole_Type())
cslogEventSeverityDispConsole.setMaxAccess(_C)
if mibBuilder.loadTexts:cslogEventSeverityDispConsole.setStatus(_A)
class _CslogEventSeverityDispHtmlGUI_Type(SyslogSeverity):defaultValue=7
_CslogEventSeverityDispHtmlGUI_Type.__name__=_D
_CslogEventSeverityDispHtmlGUI_Object=MibScalar
cslogEventSeverityDispHtmlGUI=_CslogEventSeverityDispHtmlGUI_Object((1,3,6,1,4,1,9,9,270,1,1,3),_CslogEventSeverityDispHtmlGUI_Type())
cslogEventSeverityDispHtmlGUI.setMaxAccess(_C)
if mibBuilder.loadTexts:cslogEventSeverityDispHtmlGUI.setStatus(_A)
class _CslogEventSeverityDispHtmlConsol_Type(SyslogSeverity):defaultValue=7
_CslogEventSeverityDispHtmlConsol_Type.__name__=_D
_CslogEventSeverityDispHtmlConsol_Object=MibScalar
cslogEventSeverityDispHtmlConsol=_CslogEventSeverityDispHtmlConsol_Object((1,3,6,1,4,1,9,9,270,1,1,4),_CslogEventSeverityDispHtmlConsol_Type())
cslogEventSeverityDispHtmlConsol.setMaxAccess(_C)
if mibBuilder.loadTexts:cslogEventSeverityDispHtmlConsol.setStatus(_A)
_CslogEventDispositionTable_Object=MibTable
cslogEventDispositionTable=_CslogEventDispositionTable_Object((1,3,6,1,4,1,9,9,270,1,1,5))
if mibBuilder.loadTexts:cslogEventDispositionTable.setStatus(_A)
_CslogEventDispositionEntry_Object=MibTableRow
cslogEventDispositionEntry=_CslogEventDispositionEntry_Object((1,3,6,1,4,1,9,9,270,1,1,5,1))
cslogEventDispositionEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cslogEventDispositionEntry.setStatus(_A)
_CslogEventDispositionSeverity_Type=SyslogSeverity
_CslogEventDispositionSeverity_Object=MibTableColumn
cslogEventDispositionSeverity=_CslogEventDispositionSeverity_Object((1,3,6,1,4,1,9,9,270,1,1,5,1,1),_CslogEventDispositionSeverity_Type())
cslogEventDispositionSeverity.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cslogEventDispositionSeverity.setStatus(_A)
class _CslogEventDisposition_Type(CslogEventDisposition):defaultBinValue='1'
_CslogEventDisposition_Type.__name__=_G
_CslogEventDisposition_Object=MibTableColumn
cslogEventDisposition=_CslogEventDisposition_Object((1,3,6,1,4,1,9,9,270,1,1,5,1,2),_CslogEventDisposition_Type())
cslogEventDisposition.setMaxAccess(_C)
if mibBuilder.loadTexts:cslogEventDisposition.setStatus(_A)
_CslogEventDispositionCount_Type=Counter32
_CslogEventDispositionCount_Object=MibTableColumn
cslogEventDispositionCount=_CslogEventDispositionCount_Object((1,3,6,1,4,1,9,9,270,1,1,5,1,3),_CslogEventDispositionCount_Type())
cslogEventDispositionCount.setMaxAccess('read-only')
if mibBuilder.loadTexts:cslogEventDispositionCount.setStatus(_A)
_CiscoSlogEventExtMIBConformance_ObjectIdentity=ObjectIdentity
ciscoSlogEventExtMIBConformance=_CiscoSlogEventExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,270,2))
_CiscoSlogEventExtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSlogEventExtMIBCompliances=_CiscoSlogEventExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,270,2,1))
_CiscoSlogEventExtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSlogEventExtMIBGroups=_CiscoSlogEventExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,270,2,2))
ciscoSlogEventExtConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,270,2,2,1))
ciscoSlogEventExtConfigGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:ciscoSlogEventExtConfigGroup.setStatus(_A)
ciscoSlogEventExtStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,270,2,2,2))
ciscoSlogEventExtStatsGroup.setObjects((_B,_M))
if mibBuilder.loadTexts:ciscoSlogEventExtStatsGroup.setStatus(_A)
ciscoSlogEventExtCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,270,2,1,1))
ciscoSlogEventExtCompliance.setObjects(*((_B,_N),(_B,_O)))
if mibBuilder.loadTexts:ciscoSlogEventExtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_G:CslogEventDisposition,'ciscoSyslogEventExtMIB':ciscoSyslogEventExtMIB,'ciscoSyslogEventExtMIBObjects':ciscoSyslogEventExtMIBObjects,'cslogEventConfig':cslogEventConfig,_H:cslogEventDetailDefault,_I:cslogEventSeverityDispConsole,_J:cslogEventSeverityDispHtmlGUI,_K:cslogEventSeverityDispHtmlConsol,'cslogEventDispositionTable':cslogEventDispositionTable,'cslogEventDispositionEntry':cslogEventDispositionEntry,_F:cslogEventDispositionSeverity,_L:cslogEventDisposition,_M:cslogEventDispositionCount,'ciscoSlogEventExtMIBConformance':ciscoSlogEventExtMIBConformance,'ciscoSlogEventExtMIBCompliances':ciscoSlogEventExtMIBCompliances,'ciscoSlogEventExtCompliance':ciscoSlogEventExtCompliance,'ciscoSlogEventExtMIBGroups':ciscoSlogEventExtMIBGroups,_N:ciscoSlogEventExtConfigGroup,_O:ciscoSlogEventExtStatsGroup})