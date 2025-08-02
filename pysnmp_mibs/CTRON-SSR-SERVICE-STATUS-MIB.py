_P='ssConfGroupV11'
_O='serviceStatusRmon'
_N='serviceStatusLfap'
_M='obsolete'
_L='serviceStatusIpxSap'
_K='serviceStatusIpxRip'
_J='serviceStatusStp'
_I='serviceStatusPim'
_H='serviceStatusIgmp'
_G='serviceStatusDvmrp'
_F='serviceStatusBgp'
_E='serviceStatusOspf'
_D='serviceStatusRip'
_C='read-only'
_B='current'
_A='CTRON-SSR-SERVICE-STATUS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ssrMibs,=mibBuilder.importSymbols('CTRON-SSR-SMI-MIB','ssrMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
serviceStatusMIB=ModuleIdentity((1,3,6,1,4,1,52,2501,1,700))
if mibBuilder.loadTexts:serviceStatusMIB.setRevisions(('2000-07-15 00:00','1998-08-04 00:00','1998-04-08 12:00'))
class ServiceStatus(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('started',1),('stopped',2),('notWorking',3)))
_ServiceStatusGroup_ObjectIdentity=ObjectIdentity
serviceStatusGroup=_ServiceStatusGroup_ObjectIdentity((1,3,6,1,4,1,52,2501,1,4))
_ServiceStatusRip_Type=ServiceStatus
_ServiceStatusRip_Object=MibScalar
serviceStatusRip=_ServiceStatusRip_Object((1,3,6,1,4,1,52,2501,1,4,1),_ServiceStatusRip_Type())
serviceStatusRip.setMaxAccess(_C)
if mibBuilder.loadTexts:serviceStatusRip.setStatus(_B)
_ServiceStatusOspf_Type=ServiceStatus
_ServiceStatusOspf_Object=MibScalar
serviceStatusOspf=_ServiceStatusOspf_Object((1,3,6,1,4,1,52,2501,1,4,2),_ServiceStatusOspf_Type())
serviceStatusOspf.setMaxAccess(_C)
if mibBuilder.loadTexts:serviceStatusOspf.setStatus(_B)
_ServiceStatusBgp_Type=ServiceStatus
_ServiceStatusBgp_Object=MibScalar
serviceStatusBgp=_ServiceStatusBgp_Object((1,3,6,1,4,1,52,2501,1,4,3),_ServiceStatusBgp_Type())
serviceStatusBgp.setMaxAccess(_C)
if mibBuilder.loadTexts:serviceStatusBgp.setStatus(_B)
_ServiceStatusDvmrp_Type=ServiceStatus
_ServiceStatusDvmrp_Object=MibScalar
serviceStatusDvmrp=_ServiceStatusDvmrp_Object((1,3,6,1,4,1,52,2501,1,4,4),_ServiceStatusDvmrp_Type())
serviceStatusDvmrp.setMaxAccess(_C)
if mibBuilder.loadTexts:serviceStatusDvmrp.setStatus(_B)
_ServiceStatusIgmp_Type=ServiceStatus
_ServiceStatusIgmp_Object=MibScalar
serviceStatusIgmp=_ServiceStatusIgmp_Object((1,3,6,1,4,1,52,2501,1,4,5),_ServiceStatusIgmp_Type())
serviceStatusIgmp.setMaxAccess(_C)
if mibBuilder.loadTexts:serviceStatusIgmp.setStatus(_B)
_ServiceStatusPim_Type=ServiceStatus
_ServiceStatusPim_Object=MibScalar
serviceStatusPim=_ServiceStatusPim_Object((1,3,6,1,4,1,52,2501,1,4,6),_ServiceStatusPim_Type())
serviceStatusPim.setMaxAccess(_C)
if mibBuilder.loadTexts:serviceStatusPim.setStatus(_B)
_ServiceStatusStp_Type=ServiceStatus
_ServiceStatusStp_Object=MibScalar
serviceStatusStp=_ServiceStatusStp_Object((1,3,6,1,4,1,52,2501,1,4,7),_ServiceStatusStp_Type())
serviceStatusStp.setMaxAccess(_C)
if mibBuilder.loadTexts:serviceStatusStp.setStatus(_B)
_ServiceStatusIpxRip_Type=ServiceStatus
_ServiceStatusIpxRip_Object=MibScalar
serviceStatusIpxRip=_ServiceStatusIpxRip_Object((1,3,6,1,4,1,52,2501,1,4,8),_ServiceStatusIpxRip_Type())
serviceStatusIpxRip.setMaxAccess(_C)
if mibBuilder.loadTexts:serviceStatusIpxRip.setStatus(_B)
_ServiceStatusIpxSap_Type=ServiceStatus
_ServiceStatusIpxSap_Object=MibScalar
serviceStatusIpxSap=_ServiceStatusIpxSap_Object((1,3,6,1,4,1,52,2501,1,4,9),_ServiceStatusIpxSap_Type())
serviceStatusIpxSap.setMaxAccess(_C)
if mibBuilder.loadTexts:serviceStatusIpxSap.setStatus(_B)
_ServiceStatusLfap_Type=ServiceStatus
_ServiceStatusLfap_Object=MibScalar
serviceStatusLfap=_ServiceStatusLfap_Object((1,3,6,1,4,1,52,2501,1,4,10),_ServiceStatusLfap_Type())
serviceStatusLfap.setMaxAccess(_C)
if mibBuilder.loadTexts:serviceStatusLfap.setStatus(_B)
_ServiceStatusRmon_Type=ServiceStatus
_ServiceStatusRmon_Object=MibScalar
serviceStatusRmon=_ServiceStatusRmon_Object((1,3,6,1,4,1,52,2501,1,4,11),_ServiceStatusRmon_Type())
serviceStatusRmon.setMaxAccess(_C)
if mibBuilder.loadTexts:serviceStatusRmon.setStatus(_B)
_SsConformance_ObjectIdentity=ObjectIdentity
ssConformance=_SsConformance_ObjectIdentity((1,3,6,1,4,1,52,2501,1,700,2))
_SsCompliances_ObjectIdentity=ObjectIdentity
ssCompliances=_SsCompliances_ObjectIdentity((1,3,6,1,4,1,52,2501,1,700,2,1))
_SsGroups_ObjectIdentity=ObjectIdentity
ssGroups=_SsGroups_ObjectIdentity((1,3,6,1,4,1,52,2501,1,700,2,2))
ssConfGroupV10=ObjectGroup((1,3,6,1,4,1,52,2501,1,700,2,2,1))
ssConfGroupV10.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ssConfGroupV10.setStatus(_M)
ssConfGroupV11=ObjectGroup((1,3,6,1,4,1,52,2501,1,700,2,2,2))
ssConfGroupV11.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ssConfGroupV11.setStatus(_B)
ssComplianceV10=ModuleCompliance((1,3,6,1,4,1,52,2501,1,700,2,2,1,1))
if mibBuilder.loadTexts:ssComplianceV10.setStatus(_M)
ssComplianceV11=ModuleCompliance((1,3,6,1,4,1,52,2501,1,700,2,2,1,2))
ssComplianceV11.setObjects((_A,_P))
if mibBuilder.loadTexts:ssComplianceV11.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ServiceStatus':ServiceStatus,'serviceStatusGroup':serviceStatusGroup,_D:serviceStatusRip,_E:serviceStatusOspf,_F:serviceStatusBgp,_G:serviceStatusDvmrp,_H:serviceStatusIgmp,_I:serviceStatusPim,_J:serviceStatusStp,_K:serviceStatusIpxRip,_L:serviceStatusIpxSap,_N:serviceStatusLfap,_O:serviceStatusRmon,'serviceStatusMIB':serviceStatusMIB,'ssConformance':ssConformance,'ssCompliances':ssCompliances,'ssGroups':ssGroups,'ssConfGroupV10':ssConfGroupV10,'ssComplianceV10':ssComplianceV10,'ssComplianceV11':ssComplianceV11,_P:ssConfGroupV11})