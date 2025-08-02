_c='ccdsStreamingStatsGeneralGroup'
_b='ccdsStreamingStatsConcurrentRequests'
_a='ccdsStreamingStatsBandwidthRate'
_Z='ccdsStreamingStatsBandwidthUnit'
_Y='ccdsStreamingStatsHCServedBytes'
_X='ccdsStreamingStatsServedBytes'
_W='ccdsStreamingStatsHCVODBytes'
_V='ccdsStreamingStatsVODBytes'
_U='ccdsStreamingStatsVODRequests'
_T='ccdsStreamingStatsHCLiveBytes'
_S='ccdsStreamingStatsLiveBytes'
_R='ccdsStreamingStatsLiveRequests'
_Q='ccdsStreamingStatsMissRequests'
_P='ccdsStreamingStatsCacheHitRequests'
_O='ccdsStreamingStatsPrepHitRequests'
_N='ccdsStreamingStatsBlockedRequests'
_M='ccdsStreamingStatsServerErrors'
_L='ccdsStreamingStatsClientErrors'
_K='ccdsStreamingStatsRequests'
_J='ccdsStreamingStatsModuleType'
_I='ccdsStreamingStatsDescr'
_H='ccdsStreamingStatsIndex'
_G='Unsigned32'
_F='Integer32'
_E='Gauge32'
_D='Bytes'
_C='read-only'
_B='CISCO-CONTENT-DELIVERY-STREAMING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_E,_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoContentDeliveryStreamingMIB=ModuleIdentity((1,3,6,1,4,1,9,9,708))
if mibBuilder.loadTexts:ciscoContentDeliveryStreamingMIB.setRevisions(('2009-09-30 00:00',))
class CiscoCdsBandwidthUnitType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('bytesPerSec',1),('kiloBytesPerSec',2),('megaBytesPerSec',3),('gigaBytesPerSec',4)))
_CiscoCdsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCdsMIBObjects=_CiscoCdsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,708,1))
_CcdsStreamingModule_ObjectIdentity=ObjectIdentity
ccdsStreamingModule=_CcdsStreamingModule_ObjectIdentity((1,3,6,1,4,1,9,9,708,1,1))
_CcdsStreamingStatsTable_Object=MibTable
ccdsStreamingStatsTable=_CcdsStreamingStatsTable_Object((1,3,6,1,4,1,9,9,708,1,1,1))
if mibBuilder.loadTexts:ccdsStreamingStatsTable.setStatus(_A)
_CcdsStreamingStatsEntry_Object=MibTableRow
ccdsStreamingStatsEntry=_CcdsStreamingStatsEntry_Object((1,3,6,1,4,1,9,9,708,1,1,1,1))
ccdsStreamingStatsEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:ccdsStreamingStatsEntry.setStatus(_A)
class _CcdsStreamingStatsIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CcdsStreamingStatsIndex_Type.__name__=_G
_CcdsStreamingStatsIndex_Object=MibTableColumn
ccdsStreamingStatsIndex=_CcdsStreamingStatsIndex_Object((1,3,6,1,4,1,9,9,708,1,1,1,1,1),_CcdsStreamingStatsIndex_Type())
ccdsStreamingStatsIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ccdsStreamingStatsIndex.setStatus(_A)
_CcdsStreamingStatsDescr_Type=SnmpAdminString
_CcdsStreamingStatsDescr_Object=MibTableColumn
ccdsStreamingStatsDescr=_CcdsStreamingStatsDescr_Object((1,3,6,1,4,1,9,9,708,1,1,1,1,2),_CcdsStreamingStatsDescr_Type())
ccdsStreamingStatsDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsStreamingStatsDescr.setStatus(_A)
class _CcdsStreamingStatsModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unknown',1),('http',2),('wmt',3),('ms',4),('fms',5)))
_CcdsStreamingStatsModuleType_Type.__name__=_F
_CcdsStreamingStatsModuleType_Object=MibTableColumn
ccdsStreamingStatsModuleType=_CcdsStreamingStatsModuleType_Object((1,3,6,1,4,1,9,9,708,1,1,1,1,3),_CcdsStreamingStatsModuleType_Type())
ccdsStreamingStatsModuleType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsStreamingStatsModuleType.setStatus(_A)
_CcdsStreamingStatsRequests_Type=Counter32
_CcdsStreamingStatsRequests_Object=MibTableColumn
ccdsStreamingStatsRequests=_CcdsStreamingStatsRequests_Object((1,3,6,1,4,1,9,9,708,1,1,1,1,4),_CcdsStreamingStatsRequests_Type())
ccdsStreamingStatsRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsStreamingStatsRequests.setStatus(_A)
_CcdsStreamingStatsLiveRequests_Type=Counter32
_CcdsStreamingStatsLiveRequests_Object=MibTableColumn
ccdsStreamingStatsLiveRequests=_CcdsStreamingStatsLiveRequests_Object((1,3,6,1,4,1,9,9,708,1,1,1,1,5),_CcdsStreamingStatsLiveRequests_Type())
ccdsStreamingStatsLiveRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsStreamingStatsLiveRequests.setStatus(_A)
_CcdsStreamingStatsVODRequests_Type=Counter32
_CcdsStreamingStatsVODRequests_Object=MibTableColumn
ccdsStreamingStatsVODRequests=_CcdsStreamingStatsVODRequests_Object((1,3,6,1,4,1,9,9,708,1,1,1,1,6),_CcdsStreamingStatsVODRequests_Type())
ccdsStreamingStatsVODRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsStreamingStatsVODRequests.setStatus(_A)
_CcdsStreamingStatsPrepHitRequests_Type=Counter32
_CcdsStreamingStatsPrepHitRequests_Object=MibTableColumn
ccdsStreamingStatsPrepHitRequests=_CcdsStreamingStatsPrepHitRequests_Object((1,3,6,1,4,1,9,9,708,1,1,1,1,7),_CcdsStreamingStatsPrepHitRequests_Type())
ccdsStreamingStatsPrepHitRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsStreamingStatsPrepHitRequests.setStatus(_A)
_CcdsStreamingStatsCacheHitRequests_Type=Counter32
_CcdsStreamingStatsCacheHitRequests_Object=MibTableColumn
ccdsStreamingStatsCacheHitRequests=_CcdsStreamingStatsCacheHitRequests_Object((1,3,6,1,4,1,9,9,708,1,1,1,1,8),_CcdsStreamingStatsCacheHitRequests_Type())
ccdsStreamingStatsCacheHitRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsStreamingStatsCacheHitRequests.setStatus(_A)
_CcdsStreamingStatsMissRequests_Type=Counter32
_CcdsStreamingStatsMissRequests_Object=MibTableColumn
ccdsStreamingStatsMissRequests=_CcdsStreamingStatsMissRequests_Object((1,3,6,1,4,1,9,9,708,1,1,1,1,9),_CcdsStreamingStatsMissRequests_Type())
ccdsStreamingStatsMissRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsStreamingStatsMissRequests.setStatus(_A)
_CcdsStreamingStatsClientErrors_Type=Counter32
_CcdsStreamingStatsClientErrors_Object=MibTableColumn
ccdsStreamingStatsClientErrors=_CcdsStreamingStatsClientErrors_Object((1,3,6,1,4,1,9,9,708,1,1,1,1,10),_CcdsStreamingStatsClientErrors_Type())
ccdsStreamingStatsClientErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsStreamingStatsClientErrors.setStatus(_A)
_CcdsStreamingStatsServerErrors_Type=Counter32
_CcdsStreamingStatsServerErrors_Object=MibTableColumn
ccdsStreamingStatsServerErrors=_CcdsStreamingStatsServerErrors_Object((1,3,6,1,4,1,9,9,708,1,1,1,1,11),_CcdsStreamingStatsServerErrors_Type())
ccdsStreamingStatsServerErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsStreamingStatsServerErrors.setStatus(_A)
_CcdsStreamingStatsBlockedRequests_Type=Counter32
_CcdsStreamingStatsBlockedRequests_Object=MibTableColumn
ccdsStreamingStatsBlockedRequests=_CcdsStreamingStatsBlockedRequests_Object((1,3,6,1,4,1,9,9,708,1,1,1,1,12),_CcdsStreamingStatsBlockedRequests_Type())
ccdsStreamingStatsBlockedRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsStreamingStatsBlockedRequests.setStatus(_A)
_CcdsStreamingStatsServedBytes_Type=Counter32
_CcdsStreamingStatsServedBytes_Object=MibTableColumn
ccdsStreamingStatsServedBytes=_CcdsStreamingStatsServedBytes_Object((1,3,6,1,4,1,9,9,708,1,1,1,1,13),_CcdsStreamingStatsServedBytes_Type())
ccdsStreamingStatsServedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsStreamingStatsServedBytes.setStatus(_A)
if mibBuilder.loadTexts:ccdsStreamingStatsServedBytes.setUnits(_D)
_CcdsStreamingStatsHCServedBytes_Type=Counter64
_CcdsStreamingStatsHCServedBytes_Object=MibTableColumn
ccdsStreamingStatsHCServedBytes=_CcdsStreamingStatsHCServedBytes_Object((1,3,6,1,4,1,9,9,708,1,1,1,1,14),_CcdsStreamingStatsHCServedBytes_Type())
ccdsStreamingStatsHCServedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsStreamingStatsHCServedBytes.setStatus(_A)
if mibBuilder.loadTexts:ccdsStreamingStatsHCServedBytes.setUnits(_D)
_CcdsStreamingStatsLiveBytes_Type=Counter32
_CcdsStreamingStatsLiveBytes_Object=MibTableColumn
ccdsStreamingStatsLiveBytes=_CcdsStreamingStatsLiveBytes_Object((1,3,6,1,4,1,9,9,708,1,1,1,1,15),_CcdsStreamingStatsLiveBytes_Type())
ccdsStreamingStatsLiveBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsStreamingStatsLiveBytes.setStatus(_A)
if mibBuilder.loadTexts:ccdsStreamingStatsLiveBytes.setUnits(_D)
_CcdsStreamingStatsHCLiveBytes_Type=Counter64
_CcdsStreamingStatsHCLiveBytes_Object=MibTableColumn
ccdsStreamingStatsHCLiveBytes=_CcdsStreamingStatsHCLiveBytes_Object((1,3,6,1,4,1,9,9,708,1,1,1,1,16),_CcdsStreamingStatsHCLiveBytes_Type())
ccdsStreamingStatsHCLiveBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsStreamingStatsHCLiveBytes.setStatus(_A)
if mibBuilder.loadTexts:ccdsStreamingStatsHCLiveBytes.setUnits(_D)
_CcdsStreamingStatsVODBytes_Type=Counter32
_CcdsStreamingStatsVODBytes_Object=MibTableColumn
ccdsStreamingStatsVODBytes=_CcdsStreamingStatsVODBytes_Object((1,3,6,1,4,1,9,9,708,1,1,1,1,17),_CcdsStreamingStatsVODBytes_Type())
ccdsStreamingStatsVODBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsStreamingStatsVODBytes.setStatus(_A)
if mibBuilder.loadTexts:ccdsStreamingStatsVODBytes.setUnits(_D)
_CcdsStreamingStatsHCVODBytes_Type=Counter64
_CcdsStreamingStatsHCVODBytes_Object=MibTableColumn
ccdsStreamingStatsHCVODBytes=_CcdsStreamingStatsHCVODBytes_Object((1,3,6,1,4,1,9,9,708,1,1,1,1,18),_CcdsStreamingStatsHCVODBytes_Type())
ccdsStreamingStatsHCVODBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsStreamingStatsHCVODBytes.setStatus(_A)
if mibBuilder.loadTexts:ccdsStreamingStatsHCVODBytes.setUnits(_D)
_CcdsStreamingStatsBandwidthUnit_Type=CiscoCdsBandwidthUnitType
_CcdsStreamingStatsBandwidthUnit_Object=MibTableColumn
ccdsStreamingStatsBandwidthUnit=_CcdsStreamingStatsBandwidthUnit_Object((1,3,6,1,4,1,9,9,708,1,1,1,1,19),_CcdsStreamingStatsBandwidthUnit_Type())
ccdsStreamingStatsBandwidthUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsStreamingStatsBandwidthUnit.setStatus(_A)
class _CcdsStreamingStatsBandwidthRate_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CcdsStreamingStatsBandwidthRate_Type.__name__=_E
_CcdsStreamingStatsBandwidthRate_Object=MibTableColumn
ccdsStreamingStatsBandwidthRate=_CcdsStreamingStatsBandwidthRate_Object((1,3,6,1,4,1,9,9,708,1,1,1,1,20),_CcdsStreamingStatsBandwidthRate_Type())
ccdsStreamingStatsBandwidthRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsStreamingStatsBandwidthRate.setStatus(_A)
_CcdsStreamingStatsConcurrentRequests_Type=Gauge32
_CcdsStreamingStatsConcurrentRequests_Object=MibTableColumn
ccdsStreamingStatsConcurrentRequests=_CcdsStreamingStatsConcurrentRequests_Object((1,3,6,1,4,1,9,9,708,1,1,1,1,21),_CcdsStreamingStatsConcurrentRequests_Type())
ccdsStreamingStatsConcurrentRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsStreamingStatsConcurrentRequests.setStatus(_A)
_CiscoCdsMIBConformance_ObjectIdentity=ObjectIdentity
ciscoCdsMIBConformance=_CiscoCdsMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,708,2))
_CiscoCdsMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCdsMIBCompliances=_CiscoCdsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,708,2,1))
_CiscoCdsMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCdsMIBGroups=_CiscoCdsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,708,2,2))
ccdsStreamingStatsGeneralGroup=ObjectGroup((1,3,6,1,4,1,9,9,708,2,2,1))
ccdsStreamingStatsGeneralGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:ccdsStreamingStatsGeneralGroup.setStatus(_A)
ciscoCdsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,708,2,1,1))
ciscoCdsMIBCompliance.setObjects((_B,_c))
if mibBuilder.loadTexts:ciscoCdsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CiscoCdsBandwidthUnitType':CiscoCdsBandwidthUnitType,'ciscoContentDeliveryStreamingMIB':ciscoContentDeliveryStreamingMIB,'ciscoCdsMIBObjects':ciscoCdsMIBObjects,'ccdsStreamingModule':ccdsStreamingModule,'ccdsStreamingStatsTable':ccdsStreamingStatsTable,'ccdsStreamingStatsEntry':ccdsStreamingStatsEntry,_H:ccdsStreamingStatsIndex,_I:ccdsStreamingStatsDescr,_J:ccdsStreamingStatsModuleType,_K:ccdsStreamingStatsRequests,_R:ccdsStreamingStatsLiveRequests,_U:ccdsStreamingStatsVODRequests,_O:ccdsStreamingStatsPrepHitRequests,_P:ccdsStreamingStatsCacheHitRequests,_Q:ccdsStreamingStatsMissRequests,_L:ccdsStreamingStatsClientErrors,_M:ccdsStreamingStatsServerErrors,_N:ccdsStreamingStatsBlockedRequests,_X:ccdsStreamingStatsServedBytes,_Y:ccdsStreamingStatsHCServedBytes,_S:ccdsStreamingStatsLiveBytes,_T:ccdsStreamingStatsHCLiveBytes,_V:ccdsStreamingStatsVODBytes,_W:ccdsStreamingStatsHCVODBytes,_Z:ccdsStreamingStatsBandwidthUnit,_a:ccdsStreamingStatsBandwidthRate,_b:ccdsStreamingStatsConcurrentRequests,'ciscoCdsMIBConformance':ciscoCdsMIBConformance,'ciscoCdsMIBCompliances':ciscoCdsMIBCompliances,'ciscoCdsMIBCompliance':ciscoCdsMIBCompliance,'ciscoCdsMIBGroups':ciscoCdsMIBGroups,_c:ccdsStreamingStatsGeneralGroup})