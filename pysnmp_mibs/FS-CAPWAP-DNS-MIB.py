_F='fsCapwapDnsMIBGroup'
_E='fsLDnsSecondServer'
_D='fsLDnsFirstServer'
_C='read-write'
_B='FS-CAPWAP-DNS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsIfIndex,=mibBuilder.importSymbols('FS-INTERFACE-MIB','fsIfIndex')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
fsCapwapDnsMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,88))
if mibBuilder.loadTexts:fsCapwapDnsMIB.setRevisions(('2010-07-09 00:00',))
_FsCapwapDnsMIBObjects_ObjectIdentity=ObjectIdentity
fsCapwapDnsMIBObjects=_FsCapwapDnsMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,88,0))
_FsCapwapDnsGlobalConfig_ObjectIdentity=ObjectIdentity
fsCapwapDnsGlobalConfig=_FsCapwapDnsGlobalConfig_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,88,0,1))
_FsLDnsFirstServer_Type=IpAddress
_FsLDnsFirstServer_Object=MibScalar
fsLDnsFirstServer=_FsLDnsFirstServer_Object((1,3,6,1,4,1,52642,1,1,10,2,88,0,1,1),_FsLDnsFirstServer_Type())
fsLDnsFirstServer.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLDnsFirstServer.setStatus(_A)
_FsLDnsSecondServer_Type=IpAddress
_FsLDnsSecondServer_Object=MibScalar
fsLDnsSecondServer=_FsLDnsSecondServer_Object((1,3,6,1,4,1,52642,1,1,10,2,88,0,1,2),_FsLDnsSecondServer_Type())
fsLDnsSecondServer.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLDnsSecondServer.setStatus(_A)
_FsCapwapDnsMIBConformance_ObjectIdentity=ObjectIdentity
fsCapwapDnsMIBConformance=_FsCapwapDnsMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,88,2))
_FsCapwapDnsMIBCompliances_ObjectIdentity=ObjectIdentity
fsCapwapDnsMIBCompliances=_FsCapwapDnsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,88,2,1))
_FsCapwapDnsMIBGroups_ObjectIdentity=ObjectIdentity
fsCapwapDnsMIBGroups=_FsCapwapDnsMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,88,2,2))
fsCapwapDnsMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,88,2,2,1))
fsCapwapDnsMIBGroup.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:fsCapwapDnsMIBGroup.setStatus(_A)
fsCapwapDnsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,88,2,1,1))
fsCapwapDnsMIBCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:fsCapwapDnsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsCapwapDnsMIB':fsCapwapDnsMIB,'fsCapwapDnsMIBObjects':fsCapwapDnsMIBObjects,'fsCapwapDnsGlobalConfig':fsCapwapDnsGlobalConfig,_D:fsLDnsFirstServer,_E:fsLDnsSecondServer,'fsCapwapDnsMIBConformance':fsCapwapDnsMIBConformance,'fsCapwapDnsMIBCompliances':fsCapwapDnsMIBCompliances,'fsCapwapDnsMIBCompliance':fsCapwapDnsMIBCompliance,'fsCapwapDnsMIBGroups':fsCapwapDnsMIBGroups,_F:fsCapwapDnsMIBGroup})