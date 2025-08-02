_o='alaIprmConfigMIBGroup'
_n='alaIprmStaticRouteName'
_m='alaIprmStaticRouteTag'
_l='alaIprmImportVrfRowStatus'
_k='alaIprmImportVrfRouteMap'
_j='alaIprmExportRouteMap'
_i='alaIprmStaticRouteType'
_h='alaIprmStaticRouteBfdStatus'
_g='alaIprmStaticAllBfd'
_f='alaIprmRtPrefIsisL2'
_e='alaIprmRtPrefIsisL1'
_d='alaIprmRtPrefImport'
_c='alaIprmRtPrefIbgp'
_b='alaIprmRtPrefEbgp'
_a='alaIprmRtPrefBgp'
_Z='alaIprmRtPrefRip'
_Y='alaIprmRtPrefOspf'
_X='alaIprmRtPrefStatic'
_W='alaIprmRtPrefLocal'
_V='alaIprmStaticRouteStatus'
_U='alaIprmStaticRouteMetric'
_T='alaIprmRoutePriority'
_S='alaIprmRouteMetric'
_R='alaIprmRouteProto'
_Q='alaIprmImportVrfName'
_P='AdminStatus'
_O='alaIprmStaticRouteNextHop'
_N='alaIprmStaticRouteMask'
_M='alaIprmStaticRouteDest'
_L='alaIprmRouteNextHop'
_K='alaIprmRouteTos'
_J='alaIprmRouteMask'
_I='alaIprmRouteDest'
_H='SnmpAdminString'
_G='read-only'
_F='read-create'
_E='not-accessible'
_D='read-write'
_C='Integer32'
_B='ALCATEL-IND1-IPRM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
routingIND1Iprm,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','routingIND1Iprm')
IANAipRouteProtocol,=mibBuilder.importSymbols('IANA-RTPROTO-MIB','IANAipRouteProtocol')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
alcatelIND1IPRMMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,2,1))
if mibBuilder.loadTexts:alcatelIND1IPRMMIB.setRevisions(('2007-04-03 00:00',))
class AdminStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
class StaticRouteType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('regular',1),('recursive',2),('bfdEnabled',3)))
_AlcatelIND1IPRMMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1IPRMMIBObjects=_AlcatelIND1IPRMMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1))
_AlaIprmConfig_ObjectIdentity=ObjectIdentity
alaIprmConfig=_AlaIprmConfig_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1))
_AlaIprmRouteTable_Object=MibTable
alaIprmRouteTable=_AlaIprmRouteTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,1))
if mibBuilder.loadTexts:alaIprmRouteTable.setStatus(_A)
_AlaIprmRouteEntry_Object=MibTableRow
alaIprmRouteEntry=_AlaIprmRouteEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,1,1))
alaIprmRouteEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:alaIprmRouteEntry.setStatus(_A)
_AlaIprmRouteDest_Type=IpAddress
_AlaIprmRouteDest_Object=MibTableColumn
alaIprmRouteDest=_AlaIprmRouteDest_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,1,1,1),_AlaIprmRouteDest_Type())
alaIprmRouteDest.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIprmRouteDest.setStatus(_A)
_AlaIprmRouteMask_Type=IpAddress
_AlaIprmRouteMask_Object=MibTableColumn
alaIprmRouteMask=_AlaIprmRouteMask_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,1,1,2),_AlaIprmRouteMask_Type())
alaIprmRouteMask.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIprmRouteMask.setStatus(_A)
class _AlaIprmRouteTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AlaIprmRouteTos_Type.__name__=_C
_AlaIprmRouteTos_Object=MibTableColumn
alaIprmRouteTos=_AlaIprmRouteTos_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,1,1,3),_AlaIprmRouteTos_Type())
alaIprmRouteTos.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIprmRouteTos.setStatus(_A)
_AlaIprmRouteNextHop_Type=IpAddress
_AlaIprmRouteNextHop_Object=MibTableColumn
alaIprmRouteNextHop=_AlaIprmRouteNextHop_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,1,1,4),_AlaIprmRouteNextHop_Type())
alaIprmRouteNextHop.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIprmRouteNextHop.setStatus(_A)
_AlaIprmRouteProto_Type=IANAipRouteProtocol
_AlaIprmRouteProto_Object=MibTableColumn
alaIprmRouteProto=_AlaIprmRouteProto_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,1,1,5),_AlaIprmRouteProto_Type())
alaIprmRouteProto.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIprmRouteProto.setStatus(_A)
_AlaIprmRouteMetric_Type=Integer32
_AlaIprmRouteMetric_Object=MibTableColumn
alaIprmRouteMetric=_AlaIprmRouteMetric_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,1,1,6),_AlaIprmRouteMetric_Type())
alaIprmRouteMetric.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIprmRouteMetric.setStatus(_A)
_AlaIprmRoutePriority_Type=Integer32
_AlaIprmRoutePriority_Object=MibTableColumn
alaIprmRoutePriority=_AlaIprmRoutePriority_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,1,1,7),_AlaIprmRoutePriority_Type())
alaIprmRoutePriority.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIprmRoutePriority.setStatus(_A)
_AlaIprmStaticRouteTable_Object=MibTable
alaIprmStaticRouteTable=_AlaIprmStaticRouteTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,2))
if mibBuilder.loadTexts:alaIprmStaticRouteTable.setStatus(_A)
_AlaIprmStaticRouteEntry_Object=MibTableRow
alaIprmStaticRouteEntry=_AlaIprmStaticRouteEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,2,1))
alaIprmStaticRouteEntry.setIndexNames((0,_B,_M),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:alaIprmStaticRouteEntry.setStatus(_A)
_AlaIprmStaticRouteDest_Type=IpAddress
_AlaIprmStaticRouteDest_Object=MibTableColumn
alaIprmStaticRouteDest=_AlaIprmStaticRouteDest_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,2,1,1),_AlaIprmStaticRouteDest_Type())
alaIprmStaticRouteDest.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIprmStaticRouteDest.setStatus(_A)
_AlaIprmStaticRouteMask_Type=IpAddress
_AlaIprmStaticRouteMask_Object=MibTableColumn
alaIprmStaticRouteMask=_AlaIprmStaticRouteMask_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,2,1,2),_AlaIprmStaticRouteMask_Type())
alaIprmStaticRouteMask.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIprmStaticRouteMask.setStatus(_A)
_AlaIprmStaticRouteNextHop_Type=IpAddress
_AlaIprmStaticRouteNextHop_Object=MibTableColumn
alaIprmStaticRouteNextHop=_AlaIprmStaticRouteNextHop_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,2,1,3),_AlaIprmStaticRouteNextHop_Type())
alaIprmStaticRouteNextHop.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIprmStaticRouteNextHop.setStatus(_A)
_AlaIprmStaticRouteMetric_Type=Integer32
_AlaIprmStaticRouteMetric_Object=MibTableColumn
alaIprmStaticRouteMetric=_AlaIprmStaticRouteMetric_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,2,1,4),_AlaIprmStaticRouteMetric_Type())
alaIprmStaticRouteMetric.setMaxAccess(_F)
if mibBuilder.loadTexts:alaIprmStaticRouteMetric.setStatus(_A)
_AlaIprmStaticRouteStatus_Type=RowStatus
_AlaIprmStaticRouteStatus_Object=MibTableColumn
alaIprmStaticRouteStatus=_AlaIprmStaticRouteStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,2,1,5),_AlaIprmStaticRouteStatus_Type())
alaIprmStaticRouteStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alaIprmStaticRouteStatus.setStatus(_A)
_AlaIprmStaticRouteBfdStatus_Type=AdminStatus
_AlaIprmStaticRouteBfdStatus_Object=MibTableColumn
alaIprmStaticRouteBfdStatus=_AlaIprmStaticRouteBfdStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,2,1,6),_AlaIprmStaticRouteBfdStatus_Type())
alaIprmStaticRouteBfdStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alaIprmStaticRouteBfdStatus.setStatus(_A)
_AlaIprmStaticRouteType_Type=StaticRouteType
_AlaIprmStaticRouteType_Object=MibTableColumn
alaIprmStaticRouteType=_AlaIprmStaticRouteType_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,2,1,7),_AlaIprmStaticRouteType_Type())
alaIprmStaticRouteType.setMaxAccess(_F)
if mibBuilder.loadTexts:alaIprmStaticRouteType.setStatus(_A)
_AlaIprmStaticRouteTag_Type=Unsigned32
_AlaIprmStaticRouteTag_Object=MibTableColumn
alaIprmStaticRouteTag=_AlaIprmStaticRouteTag_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,2,1,8),_AlaIprmStaticRouteTag_Type())
alaIprmStaticRouteTag.setMaxAccess(_F)
if mibBuilder.loadTexts:alaIprmStaticRouteTag.setStatus(_A)
class _AlaIprmStaticRouteName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AlaIprmStaticRouteName_Type.__name__=_H
_AlaIprmStaticRouteName_Object=MibTableColumn
alaIprmStaticRouteName=_AlaIprmStaticRouteName_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,2,1,9),_AlaIprmStaticRouteName_Type())
alaIprmStaticRouteName.setMaxAccess(_F)
if mibBuilder.loadTexts:alaIprmStaticRouteName.setStatus(_A)
class _AlaIprmRtPrefLocal_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AlaIprmRtPrefLocal_Type.__name__=_C
_AlaIprmRtPrefLocal_Object=MibScalar
alaIprmRtPrefLocal=_AlaIprmRtPrefLocal_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,3),_AlaIprmRtPrefLocal_Type())
alaIprmRtPrefLocal.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIprmRtPrefLocal.setStatus(_A)
class _AlaIprmRtPrefStatic_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AlaIprmRtPrefStatic_Type.__name__=_C
_AlaIprmRtPrefStatic_Object=MibScalar
alaIprmRtPrefStatic=_AlaIprmRtPrefStatic_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,4),_AlaIprmRtPrefStatic_Type())
alaIprmRtPrefStatic.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmRtPrefStatic.setStatus(_A)
class _AlaIprmRtPrefOspf_Type(Integer32):defaultValue=110;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AlaIprmRtPrefOspf_Type.__name__=_C
_AlaIprmRtPrefOspf_Object=MibScalar
alaIprmRtPrefOspf=_AlaIprmRtPrefOspf_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,5),_AlaIprmRtPrefOspf_Type())
alaIprmRtPrefOspf.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmRtPrefOspf.setStatus(_A)
class _AlaIprmRtPrefRip_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AlaIprmRtPrefRip_Type.__name__=_C
_AlaIprmRtPrefRip_Object=MibScalar
alaIprmRtPrefRip=_AlaIprmRtPrefRip_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,6),_AlaIprmRtPrefRip_Type())
alaIprmRtPrefRip.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmRtPrefRip.setStatus(_A)
class _AlaIprmRtPrefBgp_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AlaIprmRtPrefBgp_Type.__name__=_C
_AlaIprmRtPrefBgp_Object=MibScalar
alaIprmRtPrefBgp=_AlaIprmRtPrefBgp_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,7),_AlaIprmRtPrefBgp_Type())
alaIprmRtPrefBgp.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmRtPrefBgp.setStatus('deprecated')
class _AlaIprmRtPrefEbgp_Type(Integer32):defaultValue=190;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AlaIprmRtPrefEbgp_Type.__name__=_C
_AlaIprmRtPrefEbgp_Object=MibScalar
alaIprmRtPrefEbgp=_AlaIprmRtPrefEbgp_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,8),_AlaIprmRtPrefEbgp_Type())
alaIprmRtPrefEbgp.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmRtPrefEbgp.setStatus(_A)
class _AlaIprmRtPrefIbgp_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AlaIprmRtPrefIbgp_Type.__name__=_C
_AlaIprmRtPrefIbgp_Object=MibScalar
alaIprmRtPrefIbgp=_AlaIprmRtPrefIbgp_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,9),_AlaIprmRtPrefIbgp_Type())
alaIprmRtPrefIbgp.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmRtPrefIbgp.setStatus(_A)
class _AlaIprmRtPrefIsisL1_Type(Integer32):defaultValue=115;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AlaIprmRtPrefIsisL1_Type.__name__=_C
_AlaIprmRtPrefIsisL1_Object=MibScalar
alaIprmRtPrefIsisL1=_AlaIprmRtPrefIsisL1_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,10),_AlaIprmRtPrefIsisL1_Type())
alaIprmRtPrefIsisL1.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmRtPrefIsisL1.setStatus(_A)
class _AlaIprmRtPrefIsisL2_Type(Integer32):defaultValue=118;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AlaIprmRtPrefIsisL2_Type.__name__=_C
_AlaIprmRtPrefIsisL2_Object=MibScalar
alaIprmRtPrefIsisL2=_AlaIprmRtPrefIsisL2_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,11),_AlaIprmRtPrefIsisL2_Type())
alaIprmRtPrefIsisL2.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmRtPrefIsisL2.setStatus(_A)
class _AlaIprmStaticAllBfd_Type(AdminStatus):defaultValue=2
_AlaIprmStaticAllBfd_Type.__name__=_P
_AlaIprmStaticAllBfd_Object=MibScalar
alaIprmStaticAllBfd=_AlaIprmStaticAllBfd_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,12),_AlaIprmStaticAllBfd_Type())
alaIprmStaticAllBfd.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmStaticAllBfd.setStatus(_A)
class _AlaIprmRtPrefImport_Type(Integer32):defaultValue=210;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AlaIprmRtPrefImport_Type.__name__=_C
_AlaIprmRtPrefImport_Object=MibScalar
alaIprmRtPrefImport=_AlaIprmRtPrefImport_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,13),_AlaIprmRtPrefImport_Type())
alaIprmRtPrefImport.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmRtPrefImport.setStatus(_A)
_AlaIprmExportRouteMap_Type=Integer32
_AlaIprmExportRouteMap_Object=MibScalar
alaIprmExportRouteMap=_AlaIprmExportRouteMap_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,14),_AlaIprmExportRouteMap_Type())
alaIprmExportRouteMap.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmExportRouteMap.setStatus(_A)
_AlaIprmImportVrfTable_Object=MibTable
alaIprmImportVrfTable=_AlaIprmImportVrfTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,15))
if mibBuilder.loadTexts:alaIprmImportVrfTable.setStatus(_A)
_AlaIprmImportVrfEntry_Object=MibTableRow
alaIprmImportVrfEntry=_AlaIprmImportVrfEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,15,1))
alaIprmImportVrfEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:alaIprmImportVrfEntry.setStatus(_A)
class _AlaIprmImportVrfName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AlaIprmImportVrfName_Type.__name__=_H
_AlaIprmImportVrfName_Object=MibTableColumn
alaIprmImportVrfName=_AlaIprmImportVrfName_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,15,1,1),_AlaIprmImportVrfName_Type())
alaIprmImportVrfName.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIprmImportVrfName.setStatus(_A)
_AlaIprmImportVrfRouteMap_Type=Integer32
_AlaIprmImportVrfRouteMap_Object=MibTableColumn
alaIprmImportVrfRouteMap=_AlaIprmImportVrfRouteMap_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,15,1,2),_AlaIprmImportVrfRouteMap_Type())
alaIprmImportVrfRouteMap.setMaxAccess(_F)
if mibBuilder.loadTexts:alaIprmImportVrfRouteMap.setStatus(_A)
_AlaIprmImportVrfRowStatus_Type=RowStatus
_AlaIprmImportVrfRowStatus_Object=MibTableColumn
alaIprmImportVrfRowStatus=_AlaIprmImportVrfRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,1,1,15,1,3),_AlaIprmImportVrfRowStatus_Type())
alaIprmImportVrfRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alaIprmImportVrfRowStatus.setStatus(_A)
_AlcatelIND1IPRMMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1IPRMMIBConformance=_AlcatelIND1IPRMMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,2))
_AlcatelIND1IPRMMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1IPRMMIBCompliances=_AlcatelIND1IPRMMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,2,1))
_AlcatelIND1IPRMMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1IPRMMIBGroups=_AlcatelIND1IPRMMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,2,2))
alaIprmConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,2,2,1))
alaIprmConfigMIBGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:alaIprmConfigMIBGroup.setStatus(_A)
alaIprmCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,10,2,1,2,1,1))
alaIprmCompliance.setObjects((_B,_o))
if mibBuilder.loadTexts:alaIprmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_P:AdminStatus,'StaticRouteType':StaticRouteType,'alcatelIND1IPRMMIB':alcatelIND1IPRMMIB,'alcatelIND1IPRMMIBObjects':alcatelIND1IPRMMIBObjects,'alaIprmConfig':alaIprmConfig,'alaIprmRouteTable':alaIprmRouteTable,'alaIprmRouteEntry':alaIprmRouteEntry,_I:alaIprmRouteDest,_J:alaIprmRouteMask,_K:alaIprmRouteTos,_L:alaIprmRouteNextHop,_R:alaIprmRouteProto,_S:alaIprmRouteMetric,_T:alaIprmRoutePriority,'alaIprmStaticRouteTable':alaIprmStaticRouteTable,'alaIprmStaticRouteEntry':alaIprmStaticRouteEntry,_M:alaIprmStaticRouteDest,_N:alaIprmStaticRouteMask,_O:alaIprmStaticRouteNextHop,_U:alaIprmStaticRouteMetric,_V:alaIprmStaticRouteStatus,_h:alaIprmStaticRouteBfdStatus,_i:alaIprmStaticRouteType,_m:alaIprmStaticRouteTag,_n:alaIprmStaticRouteName,_W:alaIprmRtPrefLocal,_X:alaIprmRtPrefStatic,_Y:alaIprmRtPrefOspf,_Z:alaIprmRtPrefRip,_a:alaIprmRtPrefBgp,_b:alaIprmRtPrefEbgp,_c:alaIprmRtPrefIbgp,_e:alaIprmRtPrefIsisL1,_f:alaIprmRtPrefIsisL2,_g:alaIprmStaticAllBfd,_d:alaIprmRtPrefImport,_j:alaIprmExportRouteMap,'alaIprmImportVrfTable':alaIprmImportVrfTable,'alaIprmImportVrfEntry':alaIprmImportVrfEntry,_Q:alaIprmImportVrfName,_k:alaIprmImportVrfRouteMap,_l:alaIprmImportVrfRowStatus,'alcatelIND1IPRMMIBConformance':alcatelIND1IPRMMIBConformance,'alcatelIND1IPRMMIBCompliances':alcatelIND1IPRMMIBCompliances,'alaIprmCompliance':alaIprmCompliance,'alcatelIND1IPRMMIBGroups':alcatelIND1IPRMMIBGroups,_o:alaIprmConfigMIBGroup})