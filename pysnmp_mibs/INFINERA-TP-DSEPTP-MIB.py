_H='dsePtpGroup'
_G='dsePtpPmHistStatsEnable'
_F='dsePtpProvisionedRemoteTP'
_E='Integer32'
_D='ifIndex'
_C='IF-MIB'
_B='INFINERA-TP-DSEPTP-MIB'
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
dsePtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,22))
if mibBuilder.loadTexts:dsePtpMIB.setRevisions(('2008-10-20 00:00',))
_DsePtpTable_Object=MibTable
dsePtpTable=_DsePtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,22,1))
if mibBuilder.loadTexts:dsePtpTable.setStatus(_A)
_DsePtpEntry_Object=MibTableRow
dsePtpEntry=_DsePtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,22,1,1))
dsePtpEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:dsePtpEntry.setStatus(_A)
_DsePtpProvisionedRemoteTP_Type=DisplayString
_DsePtpProvisionedRemoteTP_Object=MibTableColumn
dsePtpProvisionedRemoteTP=_DsePtpProvisionedRemoteTP_Object((1,3,6,1,4,1,21296,2,2,2,2,22,1,1,1),_DsePtpProvisionedRemoteTP_Type())
dsePtpProvisionedRemoteTP.setMaxAccess('read-only')
if mibBuilder.loadTexts:dsePtpProvisionedRemoteTP.setStatus(_A)
class _DsePtpPmHistStatsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_DsePtpPmHistStatsEnable_Type.__name__=_E
_DsePtpPmHistStatsEnable_Object=MibTableColumn
dsePtpPmHistStatsEnable=_DsePtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,22,1,1,2),_DsePtpPmHistStatsEnable_Type())
dsePtpPmHistStatsEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:dsePtpPmHistStatsEnable.setStatus(_A)
_DsePtpConformance_ObjectIdentity=ObjectIdentity
dsePtpConformance=_DsePtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,22,3))
_DsePtpCompliances_ObjectIdentity=ObjectIdentity
dsePtpCompliances=_DsePtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,22,3,1))
_DsePtpGroups_ObjectIdentity=ObjectIdentity
dsePtpGroups=_DsePtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,22,3,2))
dsePtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,22,3,2,1))
dsePtpGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:dsePtpGroup.setStatus(_A)
dsePtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,22,3,1,1))
dsePtpCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:dsePtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dsePtpMIB':dsePtpMIB,'dsePtpTable':dsePtpTable,'dsePtpEntry':dsePtpEntry,_F:dsePtpProvisionedRemoteTP,_G:dsePtpPmHistStatsEnable,'dsePtpConformance':dsePtpConformance,'dsePtpCompliances':dsePtpCompliances,'dsePtpCompliance':dsePtpCompliance,'dsePtpGroups':dsePtpGroups,_H:dsePtpGroup})