_G='pdnIgmpProxyGroup'
_F='pdnIgmpProxyReportSummaryEnableDisable'
_E='pdnIgmpProxyEnableDisable'
_D='read-write'
_C='SwitchState'
_B='PDN-IP-MULTICAST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pdn_common,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-common')
SwitchState,=mibBuilder.importSymbols('PDN-TC',_C)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pdnIpMcastMIB=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,48))
if mibBuilder.loadTexts:pdnIpMcastMIB.setRevisions(('2003-05-01 00:00',))
_PdnIpMcastNotifications_ObjectIdentity=ObjectIdentity
pdnIpMcastNotifications=_PdnIpMcastNotifications_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,48,0))
_PdnIpMcastObjects_ObjectIdentity=ObjectIdentity
pdnIpMcastObjects=_PdnIpMcastObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,48,1))
_PdnIgmpProxy_ObjectIdentity=ObjectIdentity
pdnIgmpProxy=_PdnIgmpProxy_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,48,1,1))
class _PdnIgmpProxyEnableDisable_Type(SwitchState):defaultValue=2
_PdnIgmpProxyEnableDisable_Type.__name__=_C
_PdnIgmpProxyEnableDisable_Object=MibScalar
pdnIgmpProxyEnableDisable=_PdnIgmpProxyEnableDisable_Object((1,3,6,1,4,1,1795,2,24,2,48,1,1,1),_PdnIgmpProxyEnableDisable_Type())
pdnIgmpProxyEnableDisable.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnIgmpProxyEnableDisable.setStatus(_A)
class _PdnIgmpProxyReportSummaryEnableDisable_Type(SwitchState):defaultValue=2
_PdnIgmpProxyReportSummaryEnableDisable_Type.__name__=_C
_PdnIgmpProxyReportSummaryEnableDisable_Object=MibScalar
pdnIgmpProxyReportSummaryEnableDisable=_PdnIgmpProxyReportSummaryEnableDisable_Object((1,3,6,1,4,1,1795,2,24,2,48,1,1,2),_PdnIgmpProxyReportSummaryEnableDisable_Type())
pdnIgmpProxyReportSummaryEnableDisable.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnIgmpProxyReportSummaryEnableDisable.setStatus(_A)
_PdnIpMcastStats_ObjectIdentity=ObjectIdentity
pdnIpMcastStats=_PdnIpMcastStats_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,48,1,2))
_PdnIpMcastAFNs_ObjectIdentity=ObjectIdentity
pdnIpMcastAFNs=_PdnIpMcastAFNs_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,48,2))
_PdnIpMcastConformance_ObjectIdentity=ObjectIdentity
pdnIpMcastConformance=_PdnIpMcastConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,48,3))
_PdnIpMcastCompliances_ObjectIdentity=ObjectIdentity
pdnIpMcastCompliances=_PdnIpMcastCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,48,3,1))
_PdnIpMcastGroups_ObjectIdentity=ObjectIdentity
pdnIpMcastGroups=_PdnIpMcastGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,48,3,2))
_PdnIpMcaseObjGroups_ObjectIdentity=ObjectIdentity
pdnIpMcaseObjGroups=_PdnIpMcaseObjGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,48,3,2,1))
_PdnIpMcastAfnGroups_ObjectIdentity=ObjectIdentity
pdnIpMcastAfnGroups=_PdnIpMcastAfnGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,48,3,2,2))
_PdnIpMcaseNtfyGroups_ObjectIdentity=ObjectIdentity
pdnIpMcaseNtfyGroups=_PdnIpMcaseNtfyGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,48,3,2,3))
pdnIgmpProxyGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,48,3,2,1,1))
pdnIgmpProxyGroup.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:pdnIgmpProxyGroup.setStatus(_A)
pdnIpMcastMIBCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,48,3,1,1))
pdnIpMcastMIBCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:pdnIpMcastMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pdnIpMcastMIB':pdnIpMcastMIB,'pdnIpMcastNotifications':pdnIpMcastNotifications,'pdnIpMcastObjects':pdnIpMcastObjects,'pdnIgmpProxy':pdnIgmpProxy,_E:pdnIgmpProxyEnableDisable,_F:pdnIgmpProxyReportSummaryEnableDisable,'pdnIpMcastStats':pdnIpMcastStats,'pdnIpMcastAFNs':pdnIpMcastAFNs,'pdnIpMcastConformance':pdnIpMcastConformance,'pdnIpMcastCompliances':pdnIpMcastCompliances,'pdnIpMcastMIBCompliance':pdnIpMcastMIBCompliance,'pdnIpMcastGroups':pdnIpMcastGroups,'pdnIpMcaseObjGroups':pdnIpMcaseObjGroups,_G:pdnIgmpProxyGroup,'pdnIpMcastAfnGroups':pdnIpMcastAfnGroups,'pdnIpMcaseNtfyGroups':pdnIpMcaseNtfyGroups})