_E='corNetDebugGroupVer1'
_D='corNetDebugToMSecTraceLevel'
_C='Integer32'
_B='MX-CORNET-DEBUG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixExperimental,=mibBuilder.importSymbols('MX-SMI','mediatrixExperimental')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
corNetDebugMIB=ModuleIdentity((1,3,6,1,4,1,4935,99,110))
if mibBuilder.loadTexts:corNetDebugMIB.setRevisions(('2005-05-18 00:00',))
_CorNetDebugMIBObjects_ObjectIdentity=ObjectIdentity
corNetDebugMIBObjects=_CorNetDebugMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,99,110,1))
class _CorNetDebugToMSecTraceLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10,20,30,40,50,1000)));namedValues=NamedValues(*(('disabled',0),('error',10),('warning',20),('highPriorityInfo',30),('mediumPriorityInfo',40),('lowPriorityInfo',50),('all',1000)))
_CorNetDebugToMSecTraceLevel_Type.__name__=_C
_CorNetDebugToMSecTraceLevel_Object=MibScalar
corNetDebugToMSecTraceLevel=_CorNetDebugToMSecTraceLevel_Object((1,3,6,1,4,1,4935,99,110,1,50),_CorNetDebugToMSecTraceLevel_Type())
corNetDebugToMSecTraceLevel.setMaxAccess('read-write')
if mibBuilder.loadTexts:corNetDebugToMSecTraceLevel.setStatus(_A)
_CorNetDebugConformance_ObjectIdentity=ObjectIdentity
corNetDebugConformance=_CorNetDebugConformance_ObjectIdentity((1,3,6,1,4,1,4935,99,110,2))
_CorNetDebugCompliances_ObjectIdentity=ObjectIdentity
corNetDebugCompliances=_CorNetDebugCompliances_ObjectIdentity((1,3,6,1,4,1,4935,99,110,2,1))
_CorNetDebugGroups_ObjectIdentity=ObjectIdentity
corNetDebugGroups=_CorNetDebugGroups_ObjectIdentity((1,3,6,1,4,1,4935,99,110,2,2))
corNetDebugGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,99,110,2,2,5))
corNetDebugGroupVer1.setObjects((_B,_D))
if mibBuilder.loadTexts:corNetDebugGroupVer1.setStatus(_A)
corNetDebugBasicComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,99,110,2,1,5))
corNetDebugBasicComplVer1.setObjects((_B,_E))
if mibBuilder.loadTexts:corNetDebugBasicComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'corNetDebugMIB':corNetDebugMIB,'corNetDebugMIBObjects':corNetDebugMIBObjects,_D:corNetDebugToMSecTraceLevel,'corNetDebugConformance':corNetDebugConformance,'corNetDebugCompliances':corNetDebugCompliances,'corNetDebugBasicComplVer1':corNetDebugBasicComplVer1,'corNetDebugGroups':corNetDebugGroups,_E:corNetDebugGroupVer1})