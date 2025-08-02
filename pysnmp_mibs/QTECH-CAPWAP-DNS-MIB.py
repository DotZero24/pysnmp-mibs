_F='qtechCapwapDnsMIBGroup'
_E='qtechLDnsSecondServer'
_D='qtechLDnsFirstServer'
_C='read-write'
_B='QTECH-CAPWAP-DNS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechIfIndex,=mibBuilder.importSymbols('QTECH-INTERFACE-MIB','qtechIfIndex')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
qtechCapwapDnsMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,88))
if mibBuilder.loadTexts:qtechCapwapDnsMIB.setRevisions(('2010-07-09 00:00',))
_QtechCapwapDnsMIBObjects_ObjectIdentity=ObjectIdentity
qtechCapwapDnsMIBObjects=_QtechCapwapDnsMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,88,0))
_QtechCapwapDnsGlobalConfig_ObjectIdentity=ObjectIdentity
qtechCapwapDnsGlobalConfig=_QtechCapwapDnsGlobalConfig_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,88,0,1))
_QtechLDnsFirstServer_Type=IpAddress
_QtechLDnsFirstServer_Object=MibScalar
qtechLDnsFirstServer=_QtechLDnsFirstServer_Object((1,3,6,1,4,1,27514,1,1,10,2,88,0,1,1),_QtechLDnsFirstServer_Type())
qtechLDnsFirstServer.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLDnsFirstServer.setStatus(_A)
_QtechLDnsSecondServer_Type=IpAddress
_QtechLDnsSecondServer_Object=MibScalar
qtechLDnsSecondServer=_QtechLDnsSecondServer_Object((1,3,6,1,4,1,27514,1,1,10,2,88,0,1,2),_QtechLDnsSecondServer_Type())
qtechLDnsSecondServer.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLDnsSecondServer.setStatus(_A)
_QtechCapwapDnsMIBConformance_ObjectIdentity=ObjectIdentity
qtechCapwapDnsMIBConformance=_QtechCapwapDnsMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,88,2))
_QtechCapwapDnsMIBCompliances_ObjectIdentity=ObjectIdentity
qtechCapwapDnsMIBCompliances=_QtechCapwapDnsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,88,2,1))
_QtechCapwapDnsMIBGroups_ObjectIdentity=ObjectIdentity
qtechCapwapDnsMIBGroups=_QtechCapwapDnsMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,88,2,2))
qtechCapwapDnsMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,88,2,2,1))
qtechCapwapDnsMIBGroup.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:qtechCapwapDnsMIBGroup.setStatus(_A)
qtechCapwapDnsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,88,2,1,1))
qtechCapwapDnsMIBCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:qtechCapwapDnsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechCapwapDnsMIB':qtechCapwapDnsMIB,'qtechCapwapDnsMIBObjects':qtechCapwapDnsMIBObjects,'qtechCapwapDnsGlobalConfig':qtechCapwapDnsGlobalConfig,_D:qtechLDnsFirstServer,_E:qtechLDnsSecondServer,'qtechCapwapDnsMIBConformance':qtechCapwapDnsMIBConformance,'qtechCapwapDnsMIBCompliances':qtechCapwapDnsMIBCompliances,'qtechCapwapDnsMIBCompliance':qtechCapwapDnsMIBCompliance,'qtechCapwapDnsMIBGroups':qtechCapwapDnsMIBGroups,_F:qtechCapwapDnsMIBGroup})