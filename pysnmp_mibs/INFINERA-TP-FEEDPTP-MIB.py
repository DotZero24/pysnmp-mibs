_G='feedPtpGroup'
_F='feedPtpPmHistStatsEnable'
_E='Integer32'
_D='ifIndex'
_C='IF-MIB'
_B='INFINERA-TP-FEEDPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
feedPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,52))
if mibBuilder.loadTexts:feedPtpMIB.setRevisions(('2008-10-20 00:00',))
_FeedPtpTable_Object=MibTable
feedPtpTable=_FeedPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,52,1))
if mibBuilder.loadTexts:feedPtpTable.setStatus(_A)
_FeedPtpEntry_Object=MibTableRow
feedPtpEntry=_FeedPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,52,1,1))
feedPtpEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:feedPtpEntry.setStatus(_A)
class _FeedPtpPmHistStatsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FeedPtpPmHistStatsEnable_Type.__name__=_E
_FeedPtpPmHistStatsEnable_Object=MibTableColumn
feedPtpPmHistStatsEnable=_FeedPtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,52,1,1,1),_FeedPtpPmHistStatsEnable_Type())
feedPtpPmHistStatsEnable.setMaxAccess('read-only')
if mibBuilder.loadTexts:feedPtpPmHistStatsEnable.setStatus(_A)
_FeedPtpConformance_ObjectIdentity=ObjectIdentity
feedPtpConformance=_FeedPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,52,3))
_FeedPtpCompliances_ObjectIdentity=ObjectIdentity
feedPtpCompliances=_FeedPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,52,3,1))
_FeedPtpGroups_ObjectIdentity=ObjectIdentity
feedPtpGroups=_FeedPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,52,3,2))
feedPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,52,3,2,1))
feedPtpGroup.setObjects((_B,_F))
if mibBuilder.loadTexts:feedPtpGroup.setStatus(_A)
feedPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,52,3,1,1))
feedPtpCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:feedPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'feedPtpMIB':feedPtpMIB,'feedPtpTable':feedPtpTable,'feedPtpEntry':feedPtpEntry,_F:feedPtpPmHistStatsEnable,'feedPtpConformance':feedPtpConformance,'feedPtpCompliances':feedPtpCompliances,'feedPtpCompliance':feedPtpCompliance,'feedPtpGroups':feedPtpGroups,_G:feedPtpGroup})