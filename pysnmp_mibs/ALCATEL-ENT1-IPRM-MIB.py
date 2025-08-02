_r='alaIprmConfigMIBGroup'
_q='alaIprmExportToAllVrfsRouteMap'
_p='alaIprmImportIsidRowStatus'
_o='alaIprmImportIsidRouteMap'
_n='alaIprmImportVrfRowStatus'
_m='alaIprmImportVrfRouteMap'
_l='alaIprmExportRouteMap'
_k='alaIprmRtPrefEntryValue'
_j='alaIprmRouteTargetRowStatus'
_i='alaIprmRouteTargetType'
_h='alaIprmRouteDistinguisher'
_g='alaIprmRouterId'
_f='alaIprmPrimaryAddress'
_e='alaIprmStaticAllBfd'
_d='alaIprmStaticRouteName'
_c='alaIprmStaticRouteTag'
_b='alaIprmStaticRouteType'
_a='alaIprmStaticRouteBfdStatus'
_Z='alaIprmStaticRouteStatus'
_Y='alaIprmStaticRouteMetric'
_X='alaIprmRoutePriority'
_W='alaIprmRouteMetric'
_V='alaIprmRouteProto'
_U='alaIprmImportIsid'
_T='alaIprmImportVrfName'
_S='alaIprmRtPrefEntryType'
_R='alaIprmRouteTarget'
_Q='AlaIprmAdminStatus'
_P='alaIprmStaticRouteNextHop'
_O='alaIprmStaticRouteMask'
_N='alaIprmStaticRouteDest'
_M='alaIprmRouteNextHop'
_L='alaIprmRouteTos'
_K='alaIprmRouteMask'
_J='alaIprmRouteDest'
_I='import'
_H='read-only'
_G='Integer32'
_F='SnmpAdminString'
_E='read-write'
_D='not-accessible'
_C='read-create'
_B='ALCATEL-ENT1-IPRM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
routingIND1Iprm,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','routingIND1Iprm')
IANAipRouteProtocol,=mibBuilder.importSymbols('IANA-RTPROTO-MIB','IANAipRouteProtocol')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
alcatelIND1IPRMMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,2,1))
if mibBuilder.loadTexts:alcatelIND1IPRMMIB.setRevisions(('2010-02-22 00:00',))
class AlaIprmAdminStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
class AlaIprmStaticRouteTypes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('regular',1),('recursive',2),('bfdEnabled',3),('interface',4)))
class AlaMplsL3VpnRouteType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('export',2),('both',3)))
class AlaIprmRtPrefType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('local',1),('static',2),('ospf',3),('rip',4),('bgpExternal',5),('bgpInternal',6),('isisl1',7),('isisl2',8),(_I,9)))
_AlcatelIND1IPRMMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1IPRMMIBObjects=_AlcatelIND1IPRMMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1))
_AlaIprmConfig_ObjectIdentity=ObjectIdentity
alaIprmConfig=_AlaIprmConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1))
_AlaIprmRouteTable_Object=MibTable
alaIprmRouteTable=_AlaIprmRouteTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,1))
if mibBuilder.loadTexts:alaIprmRouteTable.setStatus(_A)
_AlaIprmRouteEntry_Object=MibTableRow
alaIprmRouteEntry=_AlaIprmRouteEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,1,1))
alaIprmRouteEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:alaIprmRouteEntry.setStatus(_A)
_AlaIprmRouteDest_Type=IpAddress
_AlaIprmRouteDest_Object=MibTableColumn
alaIprmRouteDest=_AlaIprmRouteDest_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,1,1,1),_AlaIprmRouteDest_Type())
alaIprmRouteDest.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmRouteDest.setStatus(_A)
_AlaIprmRouteMask_Type=IpAddress
_AlaIprmRouteMask_Object=MibTableColumn
alaIprmRouteMask=_AlaIprmRouteMask_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,1,1,2),_AlaIprmRouteMask_Type())
alaIprmRouteMask.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmRouteMask.setStatus(_A)
class _AlaIprmRouteTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AlaIprmRouteTos_Type.__name__=_G
_AlaIprmRouteTos_Object=MibTableColumn
alaIprmRouteTos=_AlaIprmRouteTos_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,1,1,3),_AlaIprmRouteTos_Type())
alaIprmRouteTos.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmRouteTos.setStatus(_A)
_AlaIprmRouteNextHop_Type=IpAddress
_AlaIprmRouteNextHop_Object=MibTableColumn
alaIprmRouteNextHop=_AlaIprmRouteNextHop_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,1,1,4),_AlaIprmRouteNextHop_Type())
alaIprmRouteNextHop.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmRouteNextHop.setStatus(_A)
_AlaIprmRouteProto_Type=IANAipRouteProtocol
_AlaIprmRouteProto_Object=MibTableColumn
alaIprmRouteProto=_AlaIprmRouteProto_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,1,1,5),_AlaIprmRouteProto_Type())
alaIprmRouteProto.setMaxAccess(_H)
if mibBuilder.loadTexts:alaIprmRouteProto.setStatus(_A)
_AlaIprmRouteMetric_Type=Integer32
_AlaIprmRouteMetric_Object=MibTableColumn
alaIprmRouteMetric=_AlaIprmRouteMetric_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,1,1,6),_AlaIprmRouteMetric_Type())
alaIprmRouteMetric.setMaxAccess(_H)
if mibBuilder.loadTexts:alaIprmRouteMetric.setStatus(_A)
_AlaIprmRoutePriority_Type=Integer32
_AlaIprmRoutePriority_Object=MibTableColumn
alaIprmRoutePriority=_AlaIprmRoutePriority_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,1,1,7),_AlaIprmRoutePriority_Type())
alaIprmRoutePriority.setMaxAccess(_H)
if mibBuilder.loadTexts:alaIprmRoutePriority.setStatus(_A)
_AlaIprmStaticRouteTable_Object=MibTable
alaIprmStaticRouteTable=_AlaIprmStaticRouteTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,2))
if mibBuilder.loadTexts:alaIprmStaticRouteTable.setStatus(_A)
_AlaIprmStaticRouteEntry_Object=MibTableRow
alaIprmStaticRouteEntry=_AlaIprmStaticRouteEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,2,1))
alaIprmStaticRouteEntry.setIndexNames((0,_B,_N),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:alaIprmStaticRouteEntry.setStatus(_A)
_AlaIprmStaticRouteDest_Type=IpAddress
_AlaIprmStaticRouteDest_Object=MibTableColumn
alaIprmStaticRouteDest=_AlaIprmStaticRouteDest_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,2,1,1),_AlaIprmStaticRouteDest_Type())
alaIprmStaticRouteDest.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmStaticRouteDest.setStatus(_A)
_AlaIprmStaticRouteMask_Type=IpAddress
_AlaIprmStaticRouteMask_Object=MibTableColumn
alaIprmStaticRouteMask=_AlaIprmStaticRouteMask_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,2,1,2),_AlaIprmStaticRouteMask_Type())
alaIprmStaticRouteMask.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmStaticRouteMask.setStatus(_A)
_AlaIprmStaticRouteNextHop_Type=IpAddress
_AlaIprmStaticRouteNextHop_Object=MibTableColumn
alaIprmStaticRouteNextHop=_AlaIprmStaticRouteNextHop_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,2,1,3),_AlaIprmStaticRouteNextHop_Type())
alaIprmStaticRouteNextHop.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmStaticRouteNextHop.setStatus(_A)
_AlaIprmStaticRouteMetric_Type=Integer32
_AlaIprmStaticRouteMetric_Object=MibTableColumn
alaIprmStaticRouteMetric=_AlaIprmStaticRouteMetric_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,2,1,4),_AlaIprmStaticRouteMetric_Type())
alaIprmStaticRouteMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIprmStaticRouteMetric.setStatus(_A)
_AlaIprmStaticRouteStatus_Type=RowStatus
_AlaIprmStaticRouteStatus_Object=MibTableColumn
alaIprmStaticRouteStatus=_AlaIprmStaticRouteStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,2,1,5),_AlaIprmStaticRouteStatus_Type())
alaIprmStaticRouteStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIprmStaticRouteStatus.setStatus(_A)
_AlaIprmStaticRouteBfdStatus_Type=AlaIprmAdminStatus
_AlaIprmStaticRouteBfdStatus_Object=MibTableColumn
alaIprmStaticRouteBfdStatus=_AlaIprmStaticRouteBfdStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,2,1,6),_AlaIprmStaticRouteBfdStatus_Type())
alaIprmStaticRouteBfdStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIprmStaticRouteBfdStatus.setStatus(_A)
_AlaIprmStaticRouteType_Type=AlaIprmStaticRouteTypes
_AlaIprmStaticRouteType_Object=MibTableColumn
alaIprmStaticRouteType=_AlaIprmStaticRouteType_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,2,1,7),_AlaIprmStaticRouteType_Type())
alaIprmStaticRouteType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIprmStaticRouteType.setStatus(_A)
_AlaIprmStaticRouteTag_Type=Unsigned32
_AlaIprmStaticRouteTag_Object=MibTableColumn
alaIprmStaticRouteTag=_AlaIprmStaticRouteTag_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,2,1,8),_AlaIprmStaticRouteTag_Type())
alaIprmStaticRouteTag.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIprmStaticRouteTag.setStatus(_A)
class _AlaIprmStaticRouteName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AlaIprmStaticRouteName_Type.__name__=_F
_AlaIprmStaticRouteName_Object=MibTableColumn
alaIprmStaticRouteName=_AlaIprmStaticRouteName_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,2,1,9),_AlaIprmStaticRouteName_Type())
alaIprmStaticRouteName.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIprmStaticRouteName.setStatus(_A)
class _AlaIprmStaticAllBfd_Type(AlaIprmAdminStatus):defaultValue=2
_AlaIprmStaticAllBfd_Type.__name__=_Q
_AlaIprmStaticAllBfd_Object=MibScalar
alaIprmStaticAllBfd=_AlaIprmStaticAllBfd_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,3),_AlaIprmStaticAllBfd_Type())
alaIprmStaticAllBfd.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIprmStaticAllBfd.setStatus(_A)
_AlaIprmPrimaryAddress_Type=IpAddress
_AlaIprmPrimaryAddress_Object=MibScalar
alaIprmPrimaryAddress=_AlaIprmPrimaryAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,4),_AlaIprmPrimaryAddress_Type())
alaIprmPrimaryAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIprmPrimaryAddress.setStatus(_A)
_AlaIprmRouterId_Type=IpAddress
_AlaIprmRouterId_Object=MibScalar
alaIprmRouterId=_AlaIprmRouterId_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,5),_AlaIprmRouterId_Type())
alaIprmRouterId.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIprmRouterId.setStatus(_A)
class _AlaIprmRouteDistinguisher_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,32))
_AlaIprmRouteDistinguisher_Type.__name__=_F
_AlaIprmRouteDistinguisher_Object=MibScalar
alaIprmRouteDistinguisher=_AlaIprmRouteDistinguisher_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,6),_AlaIprmRouteDistinguisher_Type())
alaIprmRouteDistinguisher.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIprmRouteDistinguisher.setStatus(_A)
_AlaIprmRouteTargetTable_Object=MibTable
alaIprmRouteTargetTable=_AlaIprmRouteTargetTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,7))
if mibBuilder.loadTexts:alaIprmRouteTargetTable.setStatus(_A)
_AlaIprmRouteTargetEntry_Object=MibTableRow
alaIprmRouteTargetEntry=_AlaIprmRouteTargetEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,7,1))
alaIprmRouteTargetEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:alaIprmRouteTargetEntry.setStatus(_A)
class _AlaIprmRouteTarget_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,32))
_AlaIprmRouteTarget_Type.__name__=_F
_AlaIprmRouteTarget_Object=MibTableColumn
alaIprmRouteTarget=_AlaIprmRouteTarget_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,7,1,1),_AlaIprmRouteTarget_Type())
alaIprmRouteTarget.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmRouteTarget.setStatus(_A)
_AlaIprmRouteTargetType_Type=AlaMplsL3VpnRouteType
_AlaIprmRouteTargetType_Object=MibTableColumn
alaIprmRouteTargetType=_AlaIprmRouteTargetType_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,7,1,2),_AlaIprmRouteTargetType_Type())
alaIprmRouteTargetType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIprmRouteTargetType.setStatus(_A)
_AlaIprmRouteTargetRowStatus_Type=RowStatus
_AlaIprmRouteTargetRowStatus_Object=MibTableColumn
alaIprmRouteTargetRowStatus=_AlaIprmRouteTargetRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,7,1,3),_AlaIprmRouteTargetRowStatus_Type())
alaIprmRouteTargetRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIprmRouteTargetRowStatus.setStatus(_A)
_AlaIprmRtPrefTable_Object=MibTable
alaIprmRtPrefTable=_AlaIprmRtPrefTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,8))
if mibBuilder.loadTexts:alaIprmRtPrefTable.setStatus(_A)
_AlaIprmRtPrefTableEntry_Object=MibTableRow
alaIprmRtPrefTableEntry=_AlaIprmRtPrefTableEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,8,1))
alaIprmRtPrefTableEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:alaIprmRtPrefTableEntry.setStatus(_A)
_AlaIprmRtPrefEntryType_Type=AlaIprmRtPrefType
_AlaIprmRtPrefEntryType_Object=MibTableColumn
alaIprmRtPrefEntryType=_AlaIprmRtPrefEntryType_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,8,1,1),_AlaIprmRtPrefEntryType_Type())
alaIprmRtPrefEntryType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmRtPrefEntryType.setStatus(_A)
class _AlaIprmRtPrefEntryValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AlaIprmRtPrefEntryValue_Type.__name__=_G
_AlaIprmRtPrefEntryValue_Object=MibTableColumn
alaIprmRtPrefEntryValue=_AlaIprmRtPrefEntryValue_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,8,1,2),_AlaIprmRtPrefEntryValue_Type())
alaIprmRtPrefEntryValue.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIprmRtPrefEntryValue.setStatus(_A)
_AlaIprmExportRouteMap_Type=Integer32
_AlaIprmExportRouteMap_Object=MibScalar
alaIprmExportRouteMap=_AlaIprmExportRouteMap_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,9),_AlaIprmExportRouteMap_Type())
alaIprmExportRouteMap.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIprmExportRouteMap.setStatus(_A)
_AlaIprmImportVrfTable_Object=MibTable
alaIprmImportVrfTable=_AlaIprmImportVrfTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,10))
if mibBuilder.loadTexts:alaIprmImportVrfTable.setStatus(_A)
_AlaIprmImportVrfEntry_Object=MibTableRow
alaIprmImportVrfEntry=_AlaIprmImportVrfEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,10,1))
alaIprmImportVrfEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:alaIprmImportVrfEntry.setStatus(_A)
class _AlaIprmImportVrfName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AlaIprmImportVrfName_Type.__name__=_F
_AlaIprmImportVrfName_Object=MibTableColumn
alaIprmImportVrfName=_AlaIprmImportVrfName_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,10,1,1),_AlaIprmImportVrfName_Type())
alaIprmImportVrfName.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmImportVrfName.setStatus(_A)
_AlaIprmImportVrfRouteMap_Type=Integer32
_AlaIprmImportVrfRouteMap_Object=MibTableColumn
alaIprmImportVrfRouteMap=_AlaIprmImportVrfRouteMap_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,10,1,2),_AlaIprmImportVrfRouteMap_Type())
alaIprmImportVrfRouteMap.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIprmImportVrfRouteMap.setStatus(_A)
_AlaIprmImportVrfRowStatus_Type=RowStatus
_AlaIprmImportVrfRowStatus_Object=MibTableColumn
alaIprmImportVrfRowStatus=_AlaIprmImportVrfRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,10,1,3),_AlaIprmImportVrfRowStatus_Type())
alaIprmImportVrfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIprmImportVrfRowStatus.setStatus(_A)
_AlaIprmImportIsidTable_Object=MibTable
alaIprmImportIsidTable=_AlaIprmImportIsidTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,11))
if mibBuilder.loadTexts:alaIprmImportIsidTable.setStatus(_A)
_AlaIprmImportIsidEntry_Object=MibTableRow
alaIprmImportIsidEntry=_AlaIprmImportIsidEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,11,1))
alaIprmImportIsidEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:alaIprmImportIsidEntry.setStatus(_A)
_AlaIprmImportIsid_Type=Unsigned32
_AlaIprmImportIsid_Object=MibTableColumn
alaIprmImportIsid=_AlaIprmImportIsid_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,11,1,1),_AlaIprmImportIsid_Type())
alaIprmImportIsid.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIprmImportIsid.setStatus(_A)
_AlaIprmImportIsidRouteMap_Type=Integer32
_AlaIprmImportIsidRouteMap_Object=MibTableColumn
alaIprmImportIsidRouteMap=_AlaIprmImportIsidRouteMap_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,11,1,2),_AlaIprmImportIsidRouteMap_Type())
alaIprmImportIsidRouteMap.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIprmImportIsidRouteMap.setStatus(_A)
_AlaIprmImportIsidRowStatus_Type=RowStatus
_AlaIprmImportIsidRowStatus_Object=MibTableColumn
alaIprmImportIsidRowStatus=_AlaIprmImportIsidRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,11,1,3),_AlaIprmImportIsidRowStatus_Type())
alaIprmImportIsidRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIprmImportIsidRowStatus.setStatus(_A)
_AlaIprmExportToAllVrfsRouteMap_Type=Integer32
_AlaIprmExportToAllVrfsRouteMap_Object=MibScalar
alaIprmExportToAllVrfsRouteMap=_AlaIprmExportToAllVrfsRouteMap_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,1,1,12),_AlaIprmExportToAllVrfsRouteMap_Type())
alaIprmExportToAllVrfsRouteMap.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIprmExportToAllVrfsRouteMap.setStatus(_A)
_AlcatelIND1IPRMMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1IPRMMIBConformance=_AlcatelIND1IPRMMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,2))
_AlcatelIND1IPRMMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1IPRMMIBCompliances=_AlcatelIND1IPRMMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,2,1))
_AlcatelIND1IPRMMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1IPRMMIBGroups=_AlcatelIND1IPRMMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,2,2))
alaIprmConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,2,2,1))
alaIprmConfigMIBGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:alaIprmConfigMIBGroup.setStatus(_A)
alaIprmCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,10,2,1,2,1,1))
alaIprmCompliance.setObjects((_B,_r))
if mibBuilder.loadTexts:alaIprmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_Q:AlaIprmAdminStatus,'AlaIprmStaticRouteTypes':AlaIprmStaticRouteTypes,'AlaMplsL3VpnRouteType':AlaMplsL3VpnRouteType,'AlaIprmRtPrefType':AlaIprmRtPrefType,'alcatelIND1IPRMMIB':alcatelIND1IPRMMIB,'alcatelIND1IPRMMIBObjects':alcatelIND1IPRMMIBObjects,'alaIprmConfig':alaIprmConfig,'alaIprmRouteTable':alaIprmRouteTable,'alaIprmRouteEntry':alaIprmRouteEntry,_J:alaIprmRouteDest,_K:alaIprmRouteMask,_L:alaIprmRouteTos,_M:alaIprmRouteNextHop,_V:alaIprmRouteProto,_W:alaIprmRouteMetric,_X:alaIprmRoutePriority,'alaIprmStaticRouteTable':alaIprmStaticRouteTable,'alaIprmStaticRouteEntry':alaIprmStaticRouteEntry,_N:alaIprmStaticRouteDest,_O:alaIprmStaticRouteMask,_P:alaIprmStaticRouteNextHop,_Y:alaIprmStaticRouteMetric,_Z:alaIprmStaticRouteStatus,_a:alaIprmStaticRouteBfdStatus,_b:alaIprmStaticRouteType,_c:alaIprmStaticRouteTag,_d:alaIprmStaticRouteName,_e:alaIprmStaticAllBfd,_f:alaIprmPrimaryAddress,_g:alaIprmRouterId,_h:alaIprmRouteDistinguisher,'alaIprmRouteTargetTable':alaIprmRouteTargetTable,'alaIprmRouteTargetEntry':alaIprmRouteTargetEntry,_R:alaIprmRouteTarget,_i:alaIprmRouteTargetType,_j:alaIprmRouteTargetRowStatus,'alaIprmRtPrefTable':alaIprmRtPrefTable,'alaIprmRtPrefTableEntry':alaIprmRtPrefTableEntry,_S:alaIprmRtPrefEntryType,_k:alaIprmRtPrefEntryValue,_l:alaIprmExportRouteMap,'alaIprmImportVrfTable':alaIprmImportVrfTable,'alaIprmImportVrfEntry':alaIprmImportVrfEntry,_T:alaIprmImportVrfName,_m:alaIprmImportVrfRouteMap,_n:alaIprmImportVrfRowStatus,'alaIprmImportIsidTable':alaIprmImportIsidTable,'alaIprmImportIsidEntry':alaIprmImportIsidEntry,_U:alaIprmImportIsid,_o:alaIprmImportIsidRouteMap,_p:alaIprmImportIsidRowStatus,_q:alaIprmExportToAllVrfsRouteMap,'alcatelIND1IPRMMIBConformance':alcatelIND1IPRMMIBConformance,'alcatelIND1IPRMMIBCompliances':alcatelIND1IPRMMIBCompliances,'alaIprmCompliance':alaIprmCompliance,'alcatelIND1IPRMMIBGroups':alcatelIND1IPRMMIBGroups,_r:alaIprmConfigMIBGroup})