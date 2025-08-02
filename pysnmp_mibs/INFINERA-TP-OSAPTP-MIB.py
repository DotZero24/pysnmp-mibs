_G='osaPtpGroup'
_F='osaPtpPmHistStatsEnable'
_E='Integer32'
_D='ifIndex'
_C='IF-MIB'
_B='INFINERA-TP-OSAPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatTenths,InfnServiceType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths','InfnServiceType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
osaPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,21))
if mibBuilder.loadTexts:osaPtpMIB.setRevisions(('2008-10-20 00:00',))
_OsaPtpTable_Object=MibTable
osaPtpTable=_OsaPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,21,1))
if mibBuilder.loadTexts:osaPtpTable.setStatus(_A)
_OsaPtpEntry_Object=MibTableRow
osaPtpEntry=_OsaPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,21,1,1))
osaPtpEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:osaPtpEntry.setStatus(_A)
class _OsaPtpPmHistStatsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_OsaPtpPmHistStatsEnable_Type.__name__=_E
_OsaPtpPmHistStatsEnable_Object=MibTableColumn
osaPtpPmHistStatsEnable=_OsaPtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,21,1,1,1),_OsaPtpPmHistStatsEnable_Type())
osaPtpPmHistStatsEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:osaPtpPmHistStatsEnable.setStatus(_A)
_OsaPtpConformance_ObjectIdentity=ObjectIdentity
osaPtpConformance=_OsaPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,21,3))
_OsaPtpCompliances_ObjectIdentity=ObjectIdentity
osaPtpCompliances=_OsaPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,21,3,1))
_OsaPtpGroups_ObjectIdentity=ObjectIdentity
osaPtpGroups=_OsaPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,21,3,2))
osaPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,21,3,2,1))
osaPtpGroup.setObjects((_B,_F))
if mibBuilder.loadTexts:osaPtpGroup.setStatus(_A)
osaPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,21,3,1,1))
osaPtpCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:osaPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'osaPtpMIB':osaPtpMIB,'osaPtpTable':osaPtpTable,'osaPtpEntry':osaPtpEntry,_F:osaPtpPmHistStatsEnable,'osaPtpConformance':osaPtpConformance,'osaPtpCompliances':osaPtpCompliances,'osaPtpCompliance':osaPtpCompliance,'osaPtpGroups':osaPtpGroups,_G:osaPtpGroup})