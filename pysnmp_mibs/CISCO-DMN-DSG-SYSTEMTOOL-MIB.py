_E='yes'
_D='writeOnly'
_C='current'
_B='read-write'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoDSGSystemTool=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,8))
if mibBuilder.loadTexts:ciscoDSGSystemTool.setRevisions(('2010-08-03 09:00','2009-12-20 15:00'))
_SystemTool_ObjectIdentity=ObjectIdentity
systemTool=_SystemTool_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,8,1))
class _SystemToolBanner_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_SystemToolBanner_Type.__name__=_A
_SystemToolBanner_Object=MibScalar
systemToolBanner=_SystemToolBanner_Object((1,3,6,1,4,1,1429,2,2,5,8,1,1),_SystemToolBanner_Type())
systemToolBanner.setMaxAccess(_B)
if mibBuilder.loadTexts:systemToolBanner.setStatus(_C)
class _SystemToolReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_SystemToolReboot_Type.__name__=_A
_SystemToolReboot_Object=MibScalar
systemToolReboot=_SystemToolReboot_Object((1,3,6,1,4,1,1429,2,2,5,8,1,2),_SystemToolReboot_Type())
systemToolReboot.setMaxAccess(_B)
if mibBuilder.loadTexts:systemToolReboot.setStatus(_C)
class _SystemToolFactoryReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_SystemToolFactoryReset_Type.__name__=_A
_SystemToolFactoryReset_Object=MibScalar
systemToolFactoryReset=_SystemToolFactoryReset_Object((1,3,6,1,4,1,1429,2,2,5,8,1,3),_SystemToolFactoryReset_Type())
systemToolFactoryReset.setMaxAccess(_B)
if mibBuilder.loadTexts:systemToolFactoryReset.setStatus(_C)
class _SystemToolCleanUnusedTables_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_SystemToolCleanUnusedTables_Type.__name__=_A
_SystemToolCleanUnusedTables_Object=MibScalar
systemToolCleanUnusedTables=_SystemToolCleanUnusedTables_Object((1,3,6,1,4,1,1429,2,2,5,8,1,4),_SystemToolCleanUnusedTables_Type())
systemToolCleanUnusedTables.setMaxAccess(_B)
if mibBuilder.loadTexts:systemToolCleanUnusedTables.setStatus(_C)
class _SystemToolCAMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('standard',1),('open',2)))
_SystemToolCAMode_Type.__name__=_A
_SystemToolCAMode_Object=MibScalar
systemToolCAMode=_SystemToolCAMode_Object((1,3,6,1,4,1,1429,2,2,5,8,1,5),_SystemToolCAMode_Type())
systemToolCAMode.setMaxAccess(_B)
if mibBuilder.loadTexts:systemToolCAMode.setStatus(_C)
class _SystemToolClearLogs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_SystemToolClearLogs_Type.__name__=_A
_SystemToolClearLogs_Object=MibScalar
systemToolClearLogs=_SystemToolClearLogs_Object((1,3,6,1,4,1,1429,2,2,5,8,1,6),_SystemToolClearLogs_Type())
systemToolClearLogs.setMaxAccess(_B)
if mibBuilder.loadTexts:systemToolClearLogs.setStatus(_C)
mibBuilder.exportSymbols('CISCO-DMN-DSG-SYSTEMTOOL-MIB',**{'ciscoDSGSystemTool':ciscoDSGSystemTool,'systemTool':systemTool,'systemToolBanner':systemToolBanner,'systemToolReboot':systemToolReboot,'systemToolFactoryReset':systemToolFactoryReset,'systemToolCleanUnusedTables':systemToolCleanUnusedTables,'systemToolCAMode':systemToolCAMode,'systemToolClearLogs':systemToolClearLogs})