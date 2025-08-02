_F='osctCtpPmHistStatsEnable'
_E='INFINERA-TP-OSCTCTP-MIB'
_D='Integer32'
_C='ifIndex'
_B='IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_B,_C)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
osctCtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,11))
if mibBuilder.loadTexts:osctCtpMIB.setRevisions(('2009-03-25 00:00',))
_OsctCtpTable_Object=MibTable
osctCtpTable=_OsctCtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,11,1))
if mibBuilder.loadTexts:osctCtpTable.setStatus(_A)
_OsctCtpEntry_Object=MibTableRow
osctCtpEntry=_OsctCtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,11,1,1))
osctCtpEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:osctCtpEntry.setStatus(_A)
class _OsctCtpPmHistStatsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_OsctCtpPmHistStatsEnable_Type.__name__=_D
_OsctCtpPmHistStatsEnable_Object=MibTableColumn
osctCtpPmHistStatsEnable=_OsctCtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,11,1,1,1),_OsctCtpPmHistStatsEnable_Type())
osctCtpPmHistStatsEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:osctCtpPmHistStatsEnable.setStatus(_A)
_OsctCtpConformance_ObjectIdentity=ObjectIdentity
osctCtpConformance=_OsctCtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,11,3))
_OsctCtpCompliances_ObjectIdentity=ObjectIdentity
osctCtpCompliances=_OsctCtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,11,3,1))
_OsctCtpGroups_ObjectIdentity=ObjectIdentity
osctCtpGroups=_OsctCtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,11,3,2))
osctCtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,11,3,2,1))
osctCtpGroup.setObjects((_E,_F))
if mibBuilder.loadTexts:osctCtpGroup.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'osctCtpMIB':osctCtpMIB,'osctCtpTable':osctCtpTable,'osctCtpEntry':osctCtpEntry,_F:osctCtpPmHistStatsEnable,'osctCtpConformance':osctCtpConformance,'osctCtpCompliances':osctCtpCompliances,'osctCtpGroups':osctCtpGroups,'osctCtpGroup':osctCtpGroup})