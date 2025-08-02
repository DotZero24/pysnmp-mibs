_A9='juniRouterVrfGroup4'
_A8='juniRouterGroup3'
_A7='juniRouterVrfGroup'
_A6='juniRouterGroup2'
_A5='juniRouterGroup'
_A4='juniRouterVrfIpv6UnicastGlobalImportMaxRoutes'
_A3='juniRouterVrfIpv6UnicastGlobalImportRouteMap'
_A2='juniRouterVrfIpv4UnicastGlobalImportMaxRoutes'
_A1='juniRouterVrfIpv4UnicastGlobalImportRouteMap'
_A0='juniRouterVrfIpv6UnicastExportRouteMapFilter'
_z='juniRouterVrfIpv6UnicastGlobalExportRouteMap'
_y='juniRouterVrfIpv6UnicastExportRouteMap'
_x='juniRouterVrfIpv6UnicastImportRouteMap'
_w='juniRouterSummaryTotalConfigured'
_v='juniRouterSummaryVRFsConfigured'
_u='juniRouterSummaryParentVRsConfigured'
_t='juniRouterSummaryNonParentVRsConfigured'
_s='juniRouterSummaryVRFCount'
_r='juniRouterVrfRouteTargetRouteTarget'
_q='juniRouterVrfRouteTargetAddrFormat'
_p='juniRouterVrfRouteTargetRouterVrfIndex'
_o='juniRouterVrfRouteTargetRouterIndex'
_n='juniRouterVrfRouterVrfIndex'
_m='juniRouterVrfRouterIndex'
_l='juniRouterProtocolProtocolIndex'
_k='juniRouterProtocolRouterIndex'
_j='juniRouterIndex'
_i='DisplayString'
_h='JuniIpPolicyExtendedCommunity'
_g='OctetString'
_f='juniRouterSummaryScalarsGroup'
_e='juniRouterGroup5'
_d='juniRouterVrfGroup3'
_c='juniRouterGroup4'
_b='juniRouterVrfGroup2'
_a='juniRouterVrfIpv4UnicastExportRouteMapFilter'
_Z='juniRouterVrfIpv4UnicastGlobalExportRouteMap'
_Y='juniRouterContextEngineID'
_X='TruthValue'
_W='Unsigned32'
_V='Integer32'
_U='juniRouterVrfRouterDescription'
_T='juniRouterContextName'
_S='juniRouterVrfRouteTargetRowStatus'
_R='juniRouterVrfRouteTargetType'
_Q='juniRouterVrfRouterName'
_P='juniRouterVrfRowStatus'
_O='juniRouterVrfRouteDistinguisher'
_N='juniRouterVrfIpv4UnicastExportRouteMap'
_M='juniRouterVrfIpv4UnicastImportRouteMap'
_L='juniRouterVrf'
_K='juniRouterProtocolRowStatus'
_J='juniRouterRowStatus'
_I='juniRouterName'
_H='juniRouterNextRouterIndex'
_G='not-accessible'
_F='read-only'
_E='JuniIpPolicyName'
_D='obsolete'
_C='read-create'
_B='current'
_A='Juniper-ROUTER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_g,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
JuniIpPolicyExtendedCommunity,JuniIpPolicyName=mibBuilder.importSymbols('Juniper-IP-POLICY-MIB',_h,_E)
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniName,=mibBuilder.importSymbols('Juniper-TC','JuniName')
SnmpEngineID,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpEngineID')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_V,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_W,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_i,'PhysAddress','RowStatus','TextualConvention',_X)
juniRouterMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,32))
if mibBuilder.loadTexts:juniRouterMIB.setRevisions(('2004-05-06 20:30','2003-09-24 17:31','2003-05-22 15:52','2003-05-10 20:54','2003-04-24 13:25','2002-05-10 18:16','2001-01-24 18:25','2000-01-21 00:00'))
class JuniNextRouterIndex(TextualConvention,Unsigned32):status=_B
class JuniRouterProtocolIndex(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32)));namedValues=NamedValues(*(('ip',1),('osi',2),('icmp',3),('igmp',4),('tcp',5),('udp',6),('bgp',7),('ospf',8),('isis',9),('rip',10),('snmp',11),('ntp',12),('generator',13),('localAddressServer',14),('dhcpProxy',15),('dhcpRelay',16),('nameResolver',17),('policyManager',18),('sscClient',19),('cops',20),('mgtm',21),('dvmrp',22),('pim',23),('msdp',24),('mpls',25),('radius',26),('mplsMgr',27),('dhcpLocalServer',28),('tacacsPlus',29),('radiusDisconnect',30),('dhcpv6LocalServer',31),('radiusProxy',32)))
_JuniRouterObjects_ObjectIdentity=ObjectIdentity
juniRouterObjects=_JuniRouterObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,32,1))
_JuniRouterNextRouterIndex_Type=JuniNextRouterIndex
_JuniRouterNextRouterIndex_Object=MibScalar
juniRouterNextRouterIndex=_JuniRouterNextRouterIndex_Object((1,3,6,1,4,1,4874,2,2,32,1,1),_JuniRouterNextRouterIndex_Type())
juniRouterNextRouterIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:juniRouterNextRouterIndex.setStatus(_B)
_JuniRouterTable_Object=MibTable
juniRouterTable=_JuniRouterTable_Object((1,3,6,1,4,1,4874,2,2,32,1,2))
if mibBuilder.loadTexts:juniRouterTable.setStatus(_B)
_JuniRouterEntry_Object=MibTableRow
juniRouterEntry=_JuniRouterEntry_Object((1,3,6,1,4,1,4874,2,2,32,1,2,1))
juniRouterEntry.setIndexNames((0,_A,_j))
if mibBuilder.loadTexts:juniRouterEntry.setStatus(_B)
_JuniRouterIndex_Type=Unsigned32
_JuniRouterIndex_Object=MibTableColumn
juniRouterIndex=_JuniRouterIndex_Object((1,3,6,1,4,1,4874,2,2,32,1,2,1,1),_JuniRouterIndex_Type())
juniRouterIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:juniRouterIndex.setStatus(_B)
_JuniRouterName_Type=JuniName
_JuniRouterName_Object=MibTableColumn
juniRouterName=_JuniRouterName_Object((1,3,6,1,4,1,4874,2,2,32,1,2,1,2),_JuniRouterName_Type())
juniRouterName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRouterName.setStatus(_B)
_JuniRouterRowStatus_Type=RowStatus
_JuniRouterRowStatus_Object=MibTableColumn
juniRouterRowStatus=_JuniRouterRowStatus_Object((1,3,6,1,4,1,4874,2,2,32,1,2,1,3),_JuniRouterRowStatus_Type())
juniRouterRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRouterRowStatus.setStatus(_B)
_JuniRouterVrf_Type=TruthValue
_JuniRouterVrf_Object=MibTableColumn
juniRouterVrf=_JuniRouterVrf_Object((1,3,6,1,4,1,4874,2,2,32,1,2,1,4),_JuniRouterVrf_Type())
juniRouterVrf.setMaxAccess(_F)
if mibBuilder.loadTexts:juniRouterVrf.setStatus(_B)
class _JuniRouterContextName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,14))
_JuniRouterContextName_Type.__name__=_g
_JuniRouterContextName_Object=MibTableColumn
juniRouterContextName=_JuniRouterContextName_Object((1,3,6,1,4,1,4874,2,2,32,1,2,1,5),_JuniRouterContextName_Type())
juniRouterContextName.setMaxAccess(_F)
if mibBuilder.loadTexts:juniRouterContextName.setStatus(_B)
_JuniRouterContextEngineID_Type=SnmpEngineID
_JuniRouterContextEngineID_Object=MibTableColumn
juniRouterContextEngineID=_JuniRouterContextEngineID_Object((1,3,6,1,4,1,4874,2,2,32,1,2,1,6),_JuniRouterContextEngineID_Type())
juniRouterContextEngineID.setMaxAccess(_F)
if mibBuilder.loadTexts:juniRouterContextEngineID.setStatus(_B)
_JuniRouterSummaryVRFCount_Type=Counter32
_JuniRouterSummaryVRFCount_Object=MibTableColumn
juniRouterSummaryVRFCount=_JuniRouterSummaryVRFCount_Object((1,3,6,1,4,1,4874,2,2,32,1,2,1,7),_JuniRouterSummaryVRFCount_Type())
juniRouterSummaryVRFCount.setMaxAccess(_F)
if mibBuilder.loadTexts:juniRouterSummaryVRFCount.setStatus(_B)
_JuniRouterProtocolTable_Object=MibTable
juniRouterProtocolTable=_JuniRouterProtocolTable_Object((1,3,6,1,4,1,4874,2,2,32,1,3))
if mibBuilder.loadTexts:juniRouterProtocolTable.setStatus(_B)
_JuniRouterProtocolEntry_Object=MibTableRow
juniRouterProtocolEntry=_JuniRouterProtocolEntry_Object((1,3,6,1,4,1,4874,2,2,32,1,3,1))
juniRouterProtocolEntry.setIndexNames((0,_A,_k),(0,_A,_l))
if mibBuilder.loadTexts:juniRouterProtocolEntry.setStatus(_B)
_JuniRouterProtocolRouterIndex_Type=Unsigned32
_JuniRouterProtocolRouterIndex_Object=MibTableColumn
juniRouterProtocolRouterIndex=_JuniRouterProtocolRouterIndex_Object((1,3,6,1,4,1,4874,2,2,32,1,3,1,1),_JuniRouterProtocolRouterIndex_Type())
juniRouterProtocolRouterIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:juniRouterProtocolRouterIndex.setStatus(_B)
_JuniRouterProtocolProtocolIndex_Type=JuniRouterProtocolIndex
_JuniRouterProtocolProtocolIndex_Object=MibTableColumn
juniRouterProtocolProtocolIndex=_JuniRouterProtocolProtocolIndex_Object((1,3,6,1,4,1,4874,2,2,32,1,3,1,2),_JuniRouterProtocolProtocolIndex_Type())
juniRouterProtocolProtocolIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:juniRouterProtocolProtocolIndex.setStatus(_B)
_JuniRouterProtocolRowStatus_Type=RowStatus
_JuniRouterProtocolRowStatus_Object=MibTableColumn
juniRouterProtocolRowStatus=_JuniRouterProtocolRowStatus_Object((1,3,6,1,4,1,4874,2,2,32,1,3,1,3),_JuniRouterProtocolRowStatus_Type())
juniRouterProtocolRowStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:juniRouterProtocolRowStatus.setStatus(_B)
_JuniRouterVrfTable_Object=MibTable
juniRouterVrfTable=_JuniRouterVrfTable_Object((1,3,6,1,4,1,4874,2,2,32,1,4))
if mibBuilder.loadTexts:juniRouterVrfTable.setStatus(_B)
_JuniRouterVrfEntry_Object=MibTableRow
juniRouterVrfEntry=_JuniRouterVrfEntry_Object((1,3,6,1,4,1,4874,2,2,32,1,4,1))
juniRouterVrfEntry.setIndexNames((0,_A,_m),(0,_A,_n))
if mibBuilder.loadTexts:juniRouterVrfEntry.setStatus(_B)
_JuniRouterVrfRouterIndex_Type=Unsigned32
_JuniRouterVrfRouterIndex_Object=MibTableColumn
juniRouterVrfRouterIndex=_JuniRouterVrfRouterIndex_Object((1,3,6,1,4,1,4874,2,2,32,1,4,1,1),_JuniRouterVrfRouterIndex_Type())
juniRouterVrfRouterIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:juniRouterVrfRouterIndex.setStatus(_B)
_JuniRouterVrfRouterVrfIndex_Type=Unsigned32
_JuniRouterVrfRouterVrfIndex_Object=MibTableColumn
juniRouterVrfRouterVrfIndex=_JuniRouterVrfRouterVrfIndex_Object((1,3,6,1,4,1,4874,2,2,32,1,4,1,2),_JuniRouterVrfRouterVrfIndex_Type())
juniRouterVrfRouterVrfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:juniRouterVrfRouterVrfIndex.setStatus(_B)
class _JuniRouterVrfIpv4UnicastImportRouteMap_Type(JuniIpPolicyName):defaultValue=OctetString('')
_JuniRouterVrfIpv4UnicastImportRouteMap_Type.__name__=_E
_JuniRouterVrfIpv4UnicastImportRouteMap_Object=MibTableColumn
juniRouterVrfIpv4UnicastImportRouteMap=_JuniRouterVrfIpv4UnicastImportRouteMap_Object((1,3,6,1,4,1,4874,2,2,32,1,4,1,3),_JuniRouterVrfIpv4UnicastImportRouteMap_Type())
juniRouterVrfIpv4UnicastImportRouteMap.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRouterVrfIpv4UnicastImportRouteMap.setStatus(_B)
class _JuniRouterVrfIpv4UnicastExportRouteMap_Type(JuniIpPolicyName):defaultValue=OctetString('')
_JuniRouterVrfIpv4UnicastExportRouteMap_Type.__name__=_E
_JuniRouterVrfIpv4UnicastExportRouteMap_Object=MibTableColumn
juniRouterVrfIpv4UnicastExportRouteMap=_JuniRouterVrfIpv4UnicastExportRouteMap_Object((1,3,6,1,4,1,4874,2,2,32,1,4,1,4),_JuniRouterVrfIpv4UnicastExportRouteMap_Type())
juniRouterVrfIpv4UnicastExportRouteMap.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRouterVrfIpv4UnicastExportRouteMap.setStatus(_B)
class _JuniRouterVrfRouteDistinguisher_Type(JuniIpPolicyExtendedCommunity):defaultValue=OctetString('')
_JuniRouterVrfRouteDistinguisher_Type.__name__=_h
_JuniRouterVrfRouteDistinguisher_Object=MibTableColumn
juniRouterVrfRouteDistinguisher=_JuniRouterVrfRouteDistinguisher_Object((1,3,6,1,4,1,4874,2,2,32,1,4,1,5),_JuniRouterVrfRouteDistinguisher_Type())
juniRouterVrfRouteDistinguisher.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRouterVrfRouteDistinguisher.setStatus(_B)
_JuniRouterVrfRowStatus_Type=RowStatus
_JuniRouterVrfRowStatus_Object=MibTableColumn
juniRouterVrfRowStatus=_JuniRouterVrfRowStatus_Object((1,3,6,1,4,1,4874,2,2,32,1,4,1,7),_JuniRouterVrfRowStatus_Type())
juniRouterVrfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRouterVrfRowStatus.setStatus(_B)
_JuniRouterVrfRouterName_Type=JuniName
_JuniRouterVrfRouterName_Object=MibTableColumn
juniRouterVrfRouterName=_JuniRouterVrfRouterName_Object((1,3,6,1,4,1,4874,2,2,32,1,4,1,8),_JuniRouterVrfRouterName_Type())
juniRouterVrfRouterName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRouterVrfRouterName.setStatus(_B)
class _JuniRouterVrfRouterDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_JuniRouterVrfRouterDescription_Type.__name__=_i
_JuniRouterVrfRouterDescription_Object=MibTableColumn
juniRouterVrfRouterDescription=_JuniRouterVrfRouterDescription_Object((1,3,6,1,4,1,4874,2,2,32,1,4,1,9),_JuniRouterVrfRouterDescription_Type())
juniRouterVrfRouterDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRouterVrfRouterDescription.setStatus(_B)
class _JuniRouterVrfIpv4UnicastGlobalExportRouteMap_Type(JuniIpPolicyName):defaultValue=OctetString('')
_JuniRouterVrfIpv4UnicastGlobalExportRouteMap_Type.__name__=_E
_JuniRouterVrfIpv4UnicastGlobalExportRouteMap_Object=MibTableColumn
juniRouterVrfIpv4UnicastGlobalExportRouteMap=_JuniRouterVrfIpv4UnicastGlobalExportRouteMap_Object((1,3,6,1,4,1,4874,2,2,32,1,4,1,10),_JuniRouterVrfIpv4UnicastGlobalExportRouteMap_Type())
juniRouterVrfIpv4UnicastGlobalExportRouteMap.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRouterVrfIpv4UnicastGlobalExportRouteMap.setStatus(_B)
class _JuniRouterVrfIpv4UnicastExportRouteMapFilter_Type(TruthValue):defaultValue=2
_JuniRouterVrfIpv4UnicastExportRouteMapFilter_Type.__name__=_X
_JuniRouterVrfIpv4UnicastExportRouteMapFilter_Object=MibTableColumn
juniRouterVrfIpv4UnicastExportRouteMapFilter=_JuniRouterVrfIpv4UnicastExportRouteMapFilter_Object((1,3,6,1,4,1,4874,2,2,32,1,4,1,11),_JuniRouterVrfIpv4UnicastExportRouteMapFilter_Type())
juniRouterVrfIpv4UnicastExportRouteMapFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRouterVrfIpv4UnicastExportRouteMapFilter.setStatus(_B)
class _JuniRouterVrfIpv6UnicastImportRouteMap_Type(JuniIpPolicyName):defaultValue=OctetString('')
_JuniRouterVrfIpv6UnicastImportRouteMap_Type.__name__=_E
_JuniRouterVrfIpv6UnicastImportRouteMap_Object=MibTableColumn
juniRouterVrfIpv6UnicastImportRouteMap=_JuniRouterVrfIpv6UnicastImportRouteMap_Object((1,3,6,1,4,1,4874,2,2,32,1,4,1,12),_JuniRouterVrfIpv6UnicastImportRouteMap_Type())
juniRouterVrfIpv6UnicastImportRouteMap.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRouterVrfIpv6UnicastImportRouteMap.setStatus(_B)
class _JuniRouterVrfIpv6UnicastExportRouteMap_Type(JuniIpPolicyName):defaultValue=OctetString('')
_JuniRouterVrfIpv6UnicastExportRouteMap_Type.__name__=_E
_JuniRouterVrfIpv6UnicastExportRouteMap_Object=MibTableColumn
juniRouterVrfIpv6UnicastExportRouteMap=_JuniRouterVrfIpv6UnicastExportRouteMap_Object((1,3,6,1,4,1,4874,2,2,32,1,4,1,13),_JuniRouterVrfIpv6UnicastExportRouteMap_Type())
juniRouterVrfIpv6UnicastExportRouteMap.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRouterVrfIpv6UnicastExportRouteMap.setStatus(_B)
class _JuniRouterVrfIpv6UnicastGlobalExportRouteMap_Type(JuniIpPolicyName):defaultValue=OctetString('')
_JuniRouterVrfIpv6UnicastGlobalExportRouteMap_Type.__name__=_E
_JuniRouterVrfIpv6UnicastGlobalExportRouteMap_Object=MibTableColumn
juniRouterVrfIpv6UnicastGlobalExportRouteMap=_JuniRouterVrfIpv6UnicastGlobalExportRouteMap_Object((1,3,6,1,4,1,4874,2,2,32,1,4,1,14),_JuniRouterVrfIpv6UnicastGlobalExportRouteMap_Type())
juniRouterVrfIpv6UnicastGlobalExportRouteMap.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRouterVrfIpv6UnicastGlobalExportRouteMap.setStatus(_B)
class _JuniRouterVrfIpv6UnicastExportRouteMapFilter_Type(TruthValue):defaultValue=2
_JuniRouterVrfIpv6UnicastExportRouteMapFilter_Type.__name__=_X
_JuniRouterVrfIpv6UnicastExportRouteMapFilter_Object=MibTableColumn
juniRouterVrfIpv6UnicastExportRouteMapFilter=_JuniRouterVrfIpv6UnicastExportRouteMapFilter_Object((1,3,6,1,4,1,4874,2,2,32,1,4,1,15),_JuniRouterVrfIpv6UnicastExportRouteMapFilter_Type())
juniRouterVrfIpv6UnicastExportRouteMapFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRouterVrfIpv6UnicastExportRouteMapFilter.setStatus(_B)
class _JuniRouterVrfIpv4UnicastGlobalImportRouteMap_Type(JuniIpPolicyName):defaultValue=OctetString('')
_JuniRouterVrfIpv4UnicastGlobalImportRouteMap_Type.__name__=_E
_JuniRouterVrfIpv4UnicastGlobalImportRouteMap_Object=MibTableColumn
juniRouterVrfIpv4UnicastGlobalImportRouteMap=_JuniRouterVrfIpv4UnicastGlobalImportRouteMap_Object((1,3,6,1,4,1,4874,2,2,32,1,4,1,16),_JuniRouterVrfIpv4UnicastGlobalImportRouteMap_Type())
juniRouterVrfIpv4UnicastGlobalImportRouteMap.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRouterVrfIpv4UnicastGlobalImportRouteMap.setStatus(_B)
class _JuniRouterVrfIpv4UnicastGlobalImportMaxRoutes_Type(Unsigned32):defaultValue=100
_JuniRouterVrfIpv4UnicastGlobalImportMaxRoutes_Type.__name__=_W
_JuniRouterVrfIpv4UnicastGlobalImportMaxRoutes_Object=MibTableColumn
juniRouterVrfIpv4UnicastGlobalImportMaxRoutes=_JuniRouterVrfIpv4UnicastGlobalImportMaxRoutes_Object((1,3,6,1,4,1,4874,2,2,32,1,4,1,17),_JuniRouterVrfIpv4UnicastGlobalImportMaxRoutes_Type())
juniRouterVrfIpv4UnicastGlobalImportMaxRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRouterVrfIpv4UnicastGlobalImportMaxRoutes.setStatus(_B)
class _JuniRouterVrfIpv6UnicastGlobalImportRouteMap_Type(JuniIpPolicyName):defaultValue=OctetString('')
_JuniRouterVrfIpv6UnicastGlobalImportRouteMap_Type.__name__=_E
_JuniRouterVrfIpv6UnicastGlobalImportRouteMap_Object=MibTableColumn
juniRouterVrfIpv6UnicastGlobalImportRouteMap=_JuniRouterVrfIpv6UnicastGlobalImportRouteMap_Object((1,3,6,1,4,1,4874,2,2,32,1,4,1,18),_JuniRouterVrfIpv6UnicastGlobalImportRouteMap_Type())
juniRouterVrfIpv6UnicastGlobalImportRouteMap.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRouterVrfIpv6UnicastGlobalImportRouteMap.setStatus(_B)
class _JuniRouterVrfIpv6UnicastGlobalImportMaxRoutes_Type(Unsigned32):defaultValue=100
_JuniRouterVrfIpv6UnicastGlobalImportMaxRoutes_Type.__name__=_W
_JuniRouterVrfIpv6UnicastGlobalImportMaxRoutes_Object=MibTableColumn
juniRouterVrfIpv6UnicastGlobalImportMaxRoutes=_JuniRouterVrfIpv6UnicastGlobalImportMaxRoutes_Object((1,3,6,1,4,1,4874,2,2,32,1,4,1,19),_JuniRouterVrfIpv6UnicastGlobalImportMaxRoutes_Type())
juniRouterVrfIpv6UnicastGlobalImportMaxRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRouterVrfIpv6UnicastGlobalImportMaxRoutes.setStatus(_B)
_JuniRouterVrfRouteTargetTable_Object=MibTable
juniRouterVrfRouteTargetTable=_JuniRouterVrfRouteTargetTable_Object((1,3,6,1,4,1,4874,2,2,32,1,5))
if mibBuilder.loadTexts:juniRouterVrfRouteTargetTable.setStatus(_B)
_JuniRouterVrfRouteTargetEntry_Object=MibTableRow
juniRouterVrfRouteTargetEntry=_JuniRouterVrfRouteTargetEntry_Object((1,3,6,1,4,1,4874,2,2,32,1,5,1))
juniRouterVrfRouteTargetEntry.setIndexNames((0,_A,_o),(0,_A,_p),(0,_A,_q),(0,_A,_r))
if mibBuilder.loadTexts:juniRouterVrfRouteTargetEntry.setStatus(_B)
_JuniRouterVrfRouteTargetRouterIndex_Type=Unsigned32
_JuniRouterVrfRouteTargetRouterIndex_Object=MibTableColumn
juniRouterVrfRouteTargetRouterIndex=_JuniRouterVrfRouteTargetRouterIndex_Object((1,3,6,1,4,1,4874,2,2,32,1,5,1,1),_JuniRouterVrfRouteTargetRouterIndex_Type())
juniRouterVrfRouteTargetRouterIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:juniRouterVrfRouteTargetRouterIndex.setStatus(_B)
_JuniRouterVrfRouteTargetRouterVrfIndex_Type=Unsigned32
_JuniRouterVrfRouteTargetRouterVrfIndex_Object=MibTableColumn
juniRouterVrfRouteTargetRouterVrfIndex=_JuniRouterVrfRouteTargetRouterVrfIndex_Object((1,3,6,1,4,1,4874,2,2,32,1,5,1,2),_JuniRouterVrfRouteTargetRouterVrfIndex_Type())
juniRouterVrfRouteTargetRouterVrfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:juniRouterVrfRouteTargetRouterVrfIndex.setStatus(_B)
class _JuniRouterVrfRouteTargetAddrFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('routeTargetFormatAsn',0),('routeTargetFormateIp',1)))
_JuniRouterVrfRouteTargetAddrFormat_Type.__name__=_V
_JuniRouterVrfRouteTargetAddrFormat_Object=MibTableColumn
juniRouterVrfRouteTargetAddrFormat=_JuniRouterVrfRouteTargetAddrFormat_Object((1,3,6,1,4,1,4874,2,2,32,1,5,1,3),_JuniRouterVrfRouteTargetAddrFormat_Type())
juniRouterVrfRouteTargetAddrFormat.setMaxAccess(_G)
if mibBuilder.loadTexts:juniRouterVrfRouteTargetAddrFormat.setStatus(_B)
_JuniRouterVrfRouteTargetRouteTarget_Type=JuniIpPolicyExtendedCommunity
_JuniRouterVrfRouteTargetRouteTarget_Object=MibTableColumn
juniRouterVrfRouteTargetRouteTarget=_JuniRouterVrfRouteTargetRouteTarget_Object((1,3,6,1,4,1,4874,2,2,32,1,5,1,4),_JuniRouterVrfRouteTargetRouteTarget_Type())
juniRouterVrfRouteTargetRouteTarget.setMaxAccess(_G)
if mibBuilder.loadTexts:juniRouterVrfRouteTargetRouteTarget.setStatus(_B)
class _JuniRouterVrfRouteTargetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('routeTargetInvalid',0),('routeTargetImport',1),('routeTargetExport',2),('routeTargetBoth',3)))
_JuniRouterVrfRouteTargetType_Type.__name__=_V
_JuniRouterVrfRouteTargetType_Object=MibTableColumn
juniRouterVrfRouteTargetType=_JuniRouterVrfRouteTargetType_Object((1,3,6,1,4,1,4874,2,2,32,1,5,1,5),_JuniRouterVrfRouteTargetType_Type())
juniRouterVrfRouteTargetType.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRouterVrfRouteTargetType.setStatus(_B)
_JuniRouterVrfRouteTargetRowStatus_Type=RowStatus
_JuniRouterVrfRouteTargetRowStatus_Object=MibTableColumn
juniRouterVrfRouteTargetRowStatus=_JuniRouterVrfRouteTargetRowStatus_Object((1,3,6,1,4,1,4874,2,2,32,1,5,1,6),_JuniRouterVrfRouteTargetRowStatus_Type())
juniRouterVrfRouteTargetRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRouterVrfRouteTargetRowStatus.setStatus(_B)
_JuniRouterSummaryCounts_ObjectIdentity=ObjectIdentity
juniRouterSummaryCounts=_JuniRouterSummaryCounts_ObjectIdentity((1,3,6,1,4,1,4874,2,2,32,1,6))
_JuniRouterSummaryScalars_ObjectIdentity=ObjectIdentity
juniRouterSummaryScalars=_JuniRouterSummaryScalars_ObjectIdentity((1,3,6,1,4,1,4874,2,2,32,1,6,1))
_JuniRouterSummaryNonParentVRsConfigured_Type=Counter32
_JuniRouterSummaryNonParentVRsConfigured_Object=MibScalar
juniRouterSummaryNonParentVRsConfigured=_JuniRouterSummaryNonParentVRsConfigured_Object((1,3,6,1,4,1,4874,2,2,32,1,6,1,1),_JuniRouterSummaryNonParentVRsConfigured_Type())
juniRouterSummaryNonParentVRsConfigured.setMaxAccess(_F)
if mibBuilder.loadTexts:juniRouterSummaryNonParentVRsConfigured.setStatus(_B)
_JuniRouterSummaryParentVRsConfigured_Type=Counter32
_JuniRouterSummaryParentVRsConfigured_Object=MibScalar
juniRouterSummaryParentVRsConfigured=_JuniRouterSummaryParentVRsConfigured_Object((1,3,6,1,4,1,4874,2,2,32,1,6,1,2),_JuniRouterSummaryParentVRsConfigured_Type())
juniRouterSummaryParentVRsConfigured.setMaxAccess(_F)
if mibBuilder.loadTexts:juniRouterSummaryParentVRsConfigured.setStatus(_B)
_JuniRouterSummaryVRFsConfigured_Type=Counter32
_JuniRouterSummaryVRFsConfigured_Object=MibScalar
juniRouterSummaryVRFsConfigured=_JuniRouterSummaryVRFsConfigured_Object((1,3,6,1,4,1,4874,2,2,32,1,6,1,3),_JuniRouterSummaryVRFsConfigured_Type())
juniRouterSummaryVRFsConfigured.setMaxAccess(_F)
if mibBuilder.loadTexts:juniRouterSummaryVRFsConfigured.setStatus(_B)
_JuniRouterSummaryTotalConfigured_Type=Counter32
_JuniRouterSummaryTotalConfigured_Object=MibScalar
juniRouterSummaryTotalConfigured=_JuniRouterSummaryTotalConfigured_Object((1,3,6,1,4,1,4874,2,2,32,1,6,1,4),_JuniRouterSummaryTotalConfigured_Type())
juniRouterSummaryTotalConfigured.setMaxAccess(_F)
if mibBuilder.loadTexts:juniRouterSummaryTotalConfigured.setStatus(_B)
_JuniRouterConformance_ObjectIdentity=ObjectIdentity
juniRouterConformance=_JuniRouterConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,32,4))
_JuniRouterCompliances_ObjectIdentity=ObjectIdentity
juniRouterCompliances=_JuniRouterCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,32,4,1))
_JuniRouterGroups_ObjectIdentity=ObjectIdentity
juniRouterGroups=_JuniRouterGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,32,4,2))
juniRouterGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,32,4,2,1))
juniRouterGroup.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:juniRouterGroup.setStatus(_D)
juniRouterGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,32,4,2,2))
juniRouterGroup2.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_L),(_A,_K)))
if mibBuilder.loadTexts:juniRouterGroup2.setStatus(_D)
juniRouterVrfGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,32,4,2,3))
juniRouterVrfGroup.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:juniRouterVrfGroup.setStatus(_D)
juniRouterGroup3=ObjectGroup((1,3,6,1,4,1,4874,2,2,32,4,2,4))
juniRouterGroup3.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_L),(_A,_K),(_A,_T)))
if mibBuilder.loadTexts:juniRouterGroup3.setStatus(_D)
juniRouterVrfGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,32,4,2,5))
juniRouterVrfGroup2.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_U),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:juniRouterVrfGroup2.setStatus(_D)
juniRouterGroup4=ObjectGroup((1,3,6,1,4,1,4874,2,2,32,4,2,6))
juniRouterGroup4.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_L),(_A,_K),(_A,_T),(_A,_Y)))
if mibBuilder.loadTexts:juniRouterGroup4.setStatus(_D)
juniRouterVrfGroup3=ObjectGroup((1,3,6,1,4,1,4874,2,2,32,4,2,7))
juniRouterVrfGroup3.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_U),(_A,_Z),(_A,_a),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:juniRouterVrfGroup3.setStatus(_D)
juniRouterGroup5=ObjectGroup((1,3,6,1,4,1,4874,2,2,32,4,2,8))
juniRouterGroup5.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_L),(_A,_K),(_A,_T),(_A,_Y),(_A,_s)))
if mibBuilder.loadTexts:juniRouterGroup5.setStatus(_B)
juniRouterSummaryScalarsGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,32,4,2,9))
juniRouterSummaryScalarsGroup.setObjects(*((_A,_t),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:juniRouterSummaryScalarsGroup.setStatus(_B)
juniRouterVrfGroup4=ObjectGroup((1,3,6,1,4,1,4874,2,2,32,4,2,10))
juniRouterVrfGroup4.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_U),(_A,_Z),(_A,_a),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:juniRouterVrfGroup4.setStatus(_B)
juniRouterCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,32,4,1,1))
juniRouterCompliance.setObjects((_A,_A5))
if mibBuilder.loadTexts:juniRouterCompliance.setStatus(_D)
juniRouterCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,32,4,1,2))
juniRouterCompliance2.setObjects(*((_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:juniRouterCompliance2.setStatus(_D)
juniRouterCompliance3=ModuleCompliance((1,3,6,1,4,1,4874,2,2,32,4,1,3))
juniRouterCompliance3.setObjects(*((_A,_A8),(_A,_b)))
if mibBuilder.loadTexts:juniRouterCompliance3.setStatus(_D)
juniRouterCompliance4=ModuleCompliance((1,3,6,1,4,1,4874,2,2,32,4,1,4))
juniRouterCompliance4.setObjects(*((_A,_c),(_A,_b)))
if mibBuilder.loadTexts:juniRouterCompliance4.setStatus(_D)
juniRouterCompliance5=ModuleCompliance((1,3,6,1,4,1,4874,2,2,32,4,1,5))
juniRouterCompliance5.setObjects(*((_A,_c),(_A,_d)))
if mibBuilder.loadTexts:juniRouterCompliance5.setStatus(_D)
juniRouterCompliance6=ModuleCompliance((1,3,6,1,4,1,4874,2,2,32,4,1,7))
juniRouterCompliance6.setObjects(*((_A,_e),(_A,_f),(_A,_d)))
if mibBuilder.loadTexts:juniRouterCompliance6.setStatus(_D)
juniRouterCompliance7=ModuleCompliance((1,3,6,1,4,1,4874,2,2,32,4,1,8))
juniRouterCompliance7.setObjects(*((_A,_e),(_A,_f),(_A,_A9)))
if mibBuilder.loadTexts:juniRouterCompliance7.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'JuniNextRouterIndex':JuniNextRouterIndex,'JuniRouterProtocolIndex':JuniRouterProtocolIndex,'juniRouterMIB':juniRouterMIB,'juniRouterObjects':juniRouterObjects,_H:juniRouterNextRouterIndex,'juniRouterTable':juniRouterTable,'juniRouterEntry':juniRouterEntry,_j:juniRouterIndex,_I:juniRouterName,_J:juniRouterRowStatus,_L:juniRouterVrf,_T:juniRouterContextName,_Y:juniRouterContextEngineID,_s:juniRouterSummaryVRFCount,'juniRouterProtocolTable':juniRouterProtocolTable,'juniRouterProtocolEntry':juniRouterProtocolEntry,_k:juniRouterProtocolRouterIndex,_l:juniRouterProtocolProtocolIndex,_K:juniRouterProtocolRowStatus,'juniRouterVrfTable':juniRouterVrfTable,'juniRouterVrfEntry':juniRouterVrfEntry,_m:juniRouterVrfRouterIndex,_n:juniRouterVrfRouterVrfIndex,_M:juniRouterVrfIpv4UnicastImportRouteMap,_N:juniRouterVrfIpv4UnicastExportRouteMap,_O:juniRouterVrfRouteDistinguisher,_P:juniRouterVrfRowStatus,_Q:juniRouterVrfRouterName,_U:juniRouterVrfRouterDescription,_Z:juniRouterVrfIpv4UnicastGlobalExportRouteMap,_a:juniRouterVrfIpv4UnicastExportRouteMapFilter,_x:juniRouterVrfIpv6UnicastImportRouteMap,_y:juniRouterVrfIpv6UnicastExportRouteMap,_z:juniRouterVrfIpv6UnicastGlobalExportRouteMap,_A0:juniRouterVrfIpv6UnicastExportRouteMapFilter,_A1:juniRouterVrfIpv4UnicastGlobalImportRouteMap,_A2:juniRouterVrfIpv4UnicastGlobalImportMaxRoutes,_A3:juniRouterVrfIpv6UnicastGlobalImportRouteMap,_A4:juniRouterVrfIpv6UnicastGlobalImportMaxRoutes,'juniRouterVrfRouteTargetTable':juniRouterVrfRouteTargetTable,'juniRouterVrfRouteTargetEntry':juniRouterVrfRouteTargetEntry,_o:juniRouterVrfRouteTargetRouterIndex,_p:juniRouterVrfRouteTargetRouterVrfIndex,_q:juniRouterVrfRouteTargetAddrFormat,_r:juniRouterVrfRouteTargetRouteTarget,_R:juniRouterVrfRouteTargetType,_S:juniRouterVrfRouteTargetRowStatus,'juniRouterSummaryCounts':juniRouterSummaryCounts,'juniRouterSummaryScalars':juniRouterSummaryScalars,_t:juniRouterSummaryNonParentVRsConfigured,_u:juniRouterSummaryParentVRsConfigured,_v:juniRouterSummaryVRFsConfigured,_w:juniRouterSummaryTotalConfigured,'juniRouterConformance':juniRouterConformance,'juniRouterCompliances':juniRouterCompliances,'juniRouterCompliance':juniRouterCompliance,'juniRouterCompliance2':juniRouterCompliance2,'juniRouterCompliance3':juniRouterCompliance3,'juniRouterCompliance4':juniRouterCompliance4,'juniRouterCompliance5':juniRouterCompliance5,'juniRouterCompliance6':juniRouterCompliance6,'juniRouterCompliance7':juniRouterCompliance7,'juniRouterGroups':juniRouterGroups,_A5:juniRouterGroup,_A6:juniRouterGroup2,_A7:juniRouterVrfGroup,_A8:juniRouterGroup3,_b:juniRouterVrfGroup2,_c:juniRouterGroup4,_d:juniRouterVrfGroup3,_e:juniRouterGroup5,_f:juniRouterSummaryScalarsGroup,_A9:juniRouterVrfGroup4})