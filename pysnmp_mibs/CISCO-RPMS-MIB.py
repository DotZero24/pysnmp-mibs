_A1='crpmsThresholdNotifGroup'
_A0='crpmsNotifGroup'
_z='crpmsVpdnGroup'
_y='crpmsCpGroup'
_x='crpmsSystemGroup'
_w='crpmsFallingAlarm'
_v='crpmsRisingAlarm'
_u='crpmsVpdnGroupCpEntryStatus'
_t='crpmsVpdnEntryStatus'
_s='crpmsVpdnLimitThreshold'
_r='crpmsVpdnSizeRejections'
_q='crpmsVpdnRejections'
_p='crpmsVpdnActiveOverflowCalls'
_o='crpmsVpdnActiveCalls'
_n='crpmsVpdnBundles'
_m='crpmsVpdnLinksPerBundleLimit'
_l='crpmsVpdnMlpBundleLimit'
_k='crpmsVpdnOverflowLimit'
_j='crpmsVpdnLimit'
_i='crpmsVpdnTunnelProtocol'
_h='crpmsVpdnTunnelId'
_g='crpmsCpEntryStatus'
_f='crpmsCpOverflowRejectThreshold'
_e='crpmsCpCallRejectionThreshold'
_d='crpmsCpOverflowLimitThreshold'
_c='crpmsCpLimitThreshold'
_b='crpmsCpOverflowRejections'
_a='crpmsCpRejections'
_Z='crpmsCpAttemptedOverflowCalls'
_Y='crpmsCpAttemptedCalls'
_X='crpmsCpActiveOverflowCalls'
_W='crpmsCpActiveCalls'
_V='crpmsCpOverflowLimit'
_U='crpmsCpLimit'
_T='crpmsSubsystemUptime'
_S='crpmsSubsystemName'
_R='crpmsVpdnGroupCpCpName'
_Q='crpmsVpdnGroupCpVpdnGroupName'
_P='crpmsVpdnGroupName'
_O='crpmsCpName'
_N='crpmsSubsystemIndex'
_M='Integer32'
_L='accessible-for-notify'
_K='crpmsAlarmThresholdObject'
_J='crpmsAlarmValue'
_I='crpmsAlarmObject'
_H='percent'
_G='not-accessible'
_F='SnmpAdminString'
_E='Unsigned32'
_D='read-only'
_C='read-create'
_B='CISCO-RPMS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
ciscoRpmsMIB=ModuleIdentity((1,3,6,1,4,1,9,10,84))
if mibBuilder.loadTexts:ciscoRpmsMIB.setRevisions(('2002-04-17 00:00','2001-11-01 00:00'))
_CiscoRpmsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoRpmsMIBObjects=_CiscoRpmsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,84,1))
_CrpmsSystem_ObjectIdentity=ObjectIdentity
crpmsSystem=_CrpmsSystem_ObjectIdentity((1,3,6,1,4,1,9,10,84,1,1))
_CrpmsSubsystemTable_Object=MibTable
crpmsSubsystemTable=_CrpmsSubsystemTable_Object((1,3,6,1,4,1,9,10,84,1,1,1))
if mibBuilder.loadTexts:crpmsSubsystemTable.setStatus(_A)
_CrpmsSubsystemEntry_Object=MibTableRow
crpmsSubsystemEntry=_CrpmsSubsystemEntry_Object((1,3,6,1,4,1,9,10,84,1,1,1,1))
crpmsSubsystemEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:crpmsSubsystemEntry.setStatus(_A)
class _CrpmsSubsystemIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_CrpmsSubsystemIndex_Type.__name__=_E
_CrpmsSubsystemIndex_Object=MibTableColumn
crpmsSubsystemIndex=_CrpmsSubsystemIndex_Object((1,3,6,1,4,1,9,10,84,1,1,1,1,1),_CrpmsSubsystemIndex_Type())
crpmsSubsystemIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:crpmsSubsystemIndex.setStatus(_A)
class _CrpmsSubsystemName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_CrpmsSubsystemName_Type.__name__=_F
_CrpmsSubsystemName_Object=MibTableColumn
crpmsSubsystemName=_CrpmsSubsystemName_Object((1,3,6,1,4,1,9,10,84,1,1,1,1,2),_CrpmsSubsystemName_Type())
crpmsSubsystemName.setMaxAccess(_D)
if mibBuilder.loadTexts:crpmsSubsystemName.setStatus(_A)
_CrpmsSubsystemUptime_Type=TimeStamp
_CrpmsSubsystemUptime_Object=MibTableColumn
crpmsSubsystemUptime=_CrpmsSubsystemUptime_Object((1,3,6,1,4,1,9,10,84,1,1,1,1,3),_CrpmsSubsystemUptime_Type())
crpmsSubsystemUptime.setMaxAccess(_D)
if mibBuilder.loadTexts:crpmsSubsystemUptime.setStatus(_A)
_CrpmsCustomerProfile_ObjectIdentity=ObjectIdentity
crpmsCustomerProfile=_CrpmsCustomerProfile_ObjectIdentity((1,3,6,1,4,1,9,10,84,1,2))
_CrpmsCpTable_Object=MibTable
crpmsCpTable=_CrpmsCpTable_Object((1,3,6,1,4,1,9,10,84,1,2,1))
if mibBuilder.loadTexts:crpmsCpTable.setStatus(_A)
_CrpmsCpEntry_Object=MibTableRow
crpmsCpEntry=_CrpmsCpEntry_Object((1,3,6,1,4,1,9,10,84,1,2,1,1))
crpmsCpEntry.setIndexNames((1,_B,_O))
if mibBuilder.loadTexts:crpmsCpEntry.setStatus(_A)
class _CrpmsCpName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_CrpmsCpName_Type.__name__=_F
_CrpmsCpName_Object=MibTableColumn
crpmsCpName=_CrpmsCpName_Object((1,3,6,1,4,1,9,10,84,1,2,1,1,1),_CrpmsCpName_Type())
crpmsCpName.setMaxAccess(_G)
if mibBuilder.loadTexts:crpmsCpName.setStatus(_A)
class _CrpmsCpLimit_Type(Unsigned32):defaultValue=0
_CrpmsCpLimit_Type.__name__=_E
_CrpmsCpLimit_Object=MibTableColumn
crpmsCpLimit=_CrpmsCpLimit_Object((1,3,6,1,4,1,9,10,84,1,2,1,1,2),_CrpmsCpLimit_Type())
crpmsCpLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:crpmsCpLimit.setStatus(_A)
class _CrpmsCpOverflowLimit_Type(Unsigned32):defaultValue=0
_CrpmsCpOverflowLimit_Type.__name__=_E
_CrpmsCpOverflowLimit_Object=MibTableColumn
crpmsCpOverflowLimit=_CrpmsCpOverflowLimit_Object((1,3,6,1,4,1,9,10,84,1,2,1,1,3),_CrpmsCpOverflowLimit_Type())
crpmsCpOverflowLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:crpmsCpOverflowLimit.setStatus(_A)
_CrpmsCpActiveCalls_Type=Gauge32
_CrpmsCpActiveCalls_Object=MibTableColumn
crpmsCpActiveCalls=_CrpmsCpActiveCalls_Object((1,3,6,1,4,1,9,10,84,1,2,1,1,4),_CrpmsCpActiveCalls_Type())
crpmsCpActiveCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:crpmsCpActiveCalls.setStatus(_A)
_CrpmsCpActiveOverflowCalls_Type=Gauge32
_CrpmsCpActiveOverflowCalls_Object=MibTableColumn
crpmsCpActiveOverflowCalls=_CrpmsCpActiveOverflowCalls_Object((1,3,6,1,4,1,9,10,84,1,2,1,1,5),_CrpmsCpActiveOverflowCalls_Type())
crpmsCpActiveOverflowCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:crpmsCpActiveOverflowCalls.setStatus(_A)
_CrpmsCpAttemptedCalls_Type=Counter32
_CrpmsCpAttemptedCalls_Object=MibTableColumn
crpmsCpAttemptedCalls=_CrpmsCpAttemptedCalls_Object((1,3,6,1,4,1,9,10,84,1,2,1,1,6),_CrpmsCpAttemptedCalls_Type())
crpmsCpAttemptedCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:crpmsCpAttemptedCalls.setStatus(_A)
_CrpmsCpAttemptedOverflowCalls_Type=Counter32
_CrpmsCpAttemptedOverflowCalls_Object=MibTableColumn
crpmsCpAttemptedOverflowCalls=_CrpmsCpAttemptedOverflowCalls_Object((1,3,6,1,4,1,9,10,84,1,2,1,1,7),_CrpmsCpAttemptedOverflowCalls_Type())
crpmsCpAttemptedOverflowCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:crpmsCpAttemptedOverflowCalls.setStatus(_A)
_CrpmsCpRejections_Type=Counter32
_CrpmsCpRejections_Object=MibTableColumn
crpmsCpRejections=_CrpmsCpRejections_Object((1,3,6,1,4,1,9,10,84,1,2,1,1,8),_CrpmsCpRejections_Type())
crpmsCpRejections.setMaxAccess(_D)
if mibBuilder.loadTexts:crpmsCpRejections.setStatus(_A)
_CrpmsCpOverflowRejections_Type=Counter32
_CrpmsCpOverflowRejections_Object=MibTableColumn
crpmsCpOverflowRejections=_CrpmsCpOverflowRejections_Object((1,3,6,1,4,1,9,10,84,1,2,1,1,9),_CrpmsCpOverflowRejections_Type())
crpmsCpOverflowRejections.setMaxAccess(_D)
if mibBuilder.loadTexts:crpmsCpOverflowRejections.setStatus(_A)
class _CrpmsCpLimitThreshold_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CrpmsCpLimitThreshold_Type.__name__=_E
_CrpmsCpLimitThreshold_Object=MibTableColumn
crpmsCpLimitThreshold=_CrpmsCpLimitThreshold_Object((1,3,6,1,4,1,9,10,84,1,2,1,1,10),_CrpmsCpLimitThreshold_Type())
crpmsCpLimitThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:crpmsCpLimitThreshold.setStatus(_A)
if mibBuilder.loadTexts:crpmsCpLimitThreshold.setUnits(_H)
class _CrpmsCpOverflowLimitThreshold_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CrpmsCpOverflowLimitThreshold_Type.__name__=_E
_CrpmsCpOverflowLimitThreshold_Object=MibTableColumn
crpmsCpOverflowLimitThreshold=_CrpmsCpOverflowLimitThreshold_Object((1,3,6,1,4,1,9,10,84,1,2,1,1,11),_CrpmsCpOverflowLimitThreshold_Type())
crpmsCpOverflowLimitThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:crpmsCpOverflowLimitThreshold.setStatus(_A)
if mibBuilder.loadTexts:crpmsCpOverflowLimitThreshold.setUnits(_H)
class _CrpmsCpCallRejectionThreshold_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CrpmsCpCallRejectionThreshold_Type.__name__=_E
_CrpmsCpCallRejectionThreshold_Object=MibTableColumn
crpmsCpCallRejectionThreshold=_CrpmsCpCallRejectionThreshold_Object((1,3,6,1,4,1,9,10,84,1,2,1,1,12),_CrpmsCpCallRejectionThreshold_Type())
crpmsCpCallRejectionThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:crpmsCpCallRejectionThreshold.setStatus(_A)
if mibBuilder.loadTexts:crpmsCpCallRejectionThreshold.setUnits(_H)
class _CrpmsCpOverflowRejectThreshold_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CrpmsCpOverflowRejectThreshold_Type.__name__=_E
_CrpmsCpOverflowRejectThreshold_Object=MibTableColumn
crpmsCpOverflowRejectThreshold=_CrpmsCpOverflowRejectThreshold_Object((1,3,6,1,4,1,9,10,84,1,2,1,1,13),_CrpmsCpOverflowRejectThreshold_Type())
crpmsCpOverflowRejectThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:crpmsCpOverflowRejectThreshold.setStatus(_A)
if mibBuilder.loadTexts:crpmsCpOverflowRejectThreshold.setUnits(_H)
_CrpmsCpEntryStatus_Type=RowStatus
_CrpmsCpEntryStatus_Object=MibTableColumn
crpmsCpEntryStatus=_CrpmsCpEntryStatus_Object((1,3,6,1,4,1,9,10,84,1,2,1,1,14),_CrpmsCpEntryStatus_Type())
crpmsCpEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:crpmsCpEntryStatus.setStatus(_A)
_CrpmsVpdn_ObjectIdentity=ObjectIdentity
crpmsVpdn=_CrpmsVpdn_ObjectIdentity((1,3,6,1,4,1,9,10,84,1,3))
_CrpmsVpdnGroupTable_Object=MibTable
crpmsVpdnGroupTable=_CrpmsVpdnGroupTable_Object((1,3,6,1,4,1,9,10,84,1,3,1))
if mibBuilder.loadTexts:crpmsVpdnGroupTable.setStatus(_A)
_CrpmsVpdnGroupEntry_Object=MibTableRow
crpmsVpdnGroupEntry=_CrpmsVpdnGroupEntry_Object((1,3,6,1,4,1,9,10,84,1,3,1,1))
crpmsVpdnGroupEntry.setIndexNames((1,_B,_P))
if mibBuilder.loadTexts:crpmsVpdnGroupEntry.setStatus(_A)
class _CrpmsVpdnGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_CrpmsVpdnGroupName_Type.__name__=_F
_CrpmsVpdnGroupName_Object=MibTableColumn
crpmsVpdnGroupName=_CrpmsVpdnGroupName_Object((1,3,6,1,4,1,9,10,84,1,3,1,1,1),_CrpmsVpdnGroupName_Type())
crpmsVpdnGroupName.setMaxAccess(_G)
if mibBuilder.loadTexts:crpmsVpdnGroupName.setStatus(_A)
_CrpmsVpdnTunnelId_Type=SnmpAdminString
_CrpmsVpdnTunnelId_Object=MibTableColumn
crpmsVpdnTunnelId=_CrpmsVpdnTunnelId_Object((1,3,6,1,4,1,9,10,84,1,3,1,1,2),_CrpmsVpdnTunnelId_Type())
crpmsVpdnTunnelId.setMaxAccess(_D)
if mibBuilder.loadTexts:crpmsVpdnTunnelId.setStatus(_A)
class _CrpmsVpdnTunnelProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('l2f',1),('l2tp',2)))
_CrpmsVpdnTunnelProtocol_Type.__name__=_M
_CrpmsVpdnTunnelProtocol_Object=MibTableColumn
crpmsVpdnTunnelProtocol=_CrpmsVpdnTunnelProtocol_Object((1,3,6,1,4,1,9,10,84,1,3,1,1,3),_CrpmsVpdnTunnelProtocol_Type())
crpmsVpdnTunnelProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:crpmsVpdnTunnelProtocol.setStatus(_A)
class _CrpmsVpdnLimit_Type(Unsigned32):defaultValue=0
_CrpmsVpdnLimit_Type.__name__=_E
_CrpmsVpdnLimit_Object=MibTableColumn
crpmsVpdnLimit=_CrpmsVpdnLimit_Object((1,3,6,1,4,1,9,10,84,1,3,1,1,4),_CrpmsVpdnLimit_Type())
crpmsVpdnLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:crpmsVpdnLimit.setStatus(_A)
class _CrpmsVpdnOverflowLimit_Type(Unsigned32):defaultValue=0
_CrpmsVpdnOverflowLimit_Type.__name__=_E
_CrpmsVpdnOverflowLimit_Object=MibTableColumn
crpmsVpdnOverflowLimit=_CrpmsVpdnOverflowLimit_Object((1,3,6,1,4,1,9,10,84,1,3,1,1,5),_CrpmsVpdnOverflowLimit_Type())
crpmsVpdnOverflowLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:crpmsVpdnOverflowLimit.setStatus(_A)
class _CrpmsVpdnMlpBundleLimit_Type(Unsigned32):defaultValue=0
_CrpmsVpdnMlpBundleLimit_Type.__name__=_E
_CrpmsVpdnMlpBundleLimit_Object=MibTableColumn
crpmsVpdnMlpBundleLimit=_CrpmsVpdnMlpBundleLimit_Object((1,3,6,1,4,1,9,10,84,1,3,1,1,6),_CrpmsVpdnMlpBundleLimit_Type())
crpmsVpdnMlpBundleLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:crpmsVpdnMlpBundleLimit.setStatus(_A)
class _CrpmsVpdnLinksPerBundleLimit_Type(Unsigned32):defaultValue=0
_CrpmsVpdnLinksPerBundleLimit_Type.__name__=_E
_CrpmsVpdnLinksPerBundleLimit_Object=MibTableColumn
crpmsVpdnLinksPerBundleLimit=_CrpmsVpdnLinksPerBundleLimit_Object((1,3,6,1,4,1,9,10,84,1,3,1,1,7),_CrpmsVpdnLinksPerBundleLimit_Type())
crpmsVpdnLinksPerBundleLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:crpmsVpdnLinksPerBundleLimit.setStatus(_A)
_CrpmsVpdnBundles_Type=Gauge32
_CrpmsVpdnBundles_Object=MibTableColumn
crpmsVpdnBundles=_CrpmsVpdnBundles_Object((1,3,6,1,4,1,9,10,84,1,3,1,1,8),_CrpmsVpdnBundles_Type())
crpmsVpdnBundles.setMaxAccess(_D)
if mibBuilder.loadTexts:crpmsVpdnBundles.setStatus(_A)
_CrpmsVpdnActiveCalls_Type=Gauge32
_CrpmsVpdnActiveCalls_Object=MibTableColumn
crpmsVpdnActiveCalls=_CrpmsVpdnActiveCalls_Object((1,3,6,1,4,1,9,10,84,1,3,1,1,9),_CrpmsVpdnActiveCalls_Type())
crpmsVpdnActiveCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:crpmsVpdnActiveCalls.setStatus(_A)
_CrpmsVpdnActiveOverflowCalls_Type=Gauge32
_CrpmsVpdnActiveOverflowCalls_Object=MibTableColumn
crpmsVpdnActiveOverflowCalls=_CrpmsVpdnActiveOverflowCalls_Object((1,3,6,1,4,1,9,10,84,1,3,1,1,10),_CrpmsVpdnActiveOverflowCalls_Type())
crpmsVpdnActiveOverflowCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:crpmsVpdnActiveOverflowCalls.setStatus(_A)
_CrpmsVpdnRejections_Type=Counter32
_CrpmsVpdnRejections_Object=MibTableColumn
crpmsVpdnRejections=_CrpmsVpdnRejections_Object((1,3,6,1,4,1,9,10,84,1,3,1,1,11),_CrpmsVpdnRejections_Type())
crpmsVpdnRejections.setMaxAccess(_D)
if mibBuilder.loadTexts:crpmsVpdnRejections.setStatus(_A)
_CrpmsVpdnSizeRejections_Type=Counter32
_CrpmsVpdnSizeRejections_Object=MibTableColumn
crpmsVpdnSizeRejections=_CrpmsVpdnSizeRejections_Object((1,3,6,1,4,1,9,10,84,1,3,1,1,12),_CrpmsVpdnSizeRejections_Type())
crpmsVpdnSizeRejections.setMaxAccess(_D)
if mibBuilder.loadTexts:crpmsVpdnSizeRejections.setStatus(_A)
class _CrpmsVpdnLimitThreshold_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CrpmsVpdnLimitThreshold_Type.__name__=_E
_CrpmsVpdnLimitThreshold_Object=MibTableColumn
crpmsVpdnLimitThreshold=_CrpmsVpdnLimitThreshold_Object((1,3,6,1,4,1,9,10,84,1,3,1,1,13),_CrpmsVpdnLimitThreshold_Type())
crpmsVpdnLimitThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:crpmsVpdnLimitThreshold.setStatus(_A)
if mibBuilder.loadTexts:crpmsVpdnLimitThreshold.setUnits(_H)
_CrpmsVpdnEntryStatus_Type=RowStatus
_CrpmsVpdnEntryStatus_Object=MibTableColumn
crpmsVpdnEntryStatus=_CrpmsVpdnEntryStatus_Object((1,3,6,1,4,1,9,10,84,1,3,1,1,14),_CrpmsVpdnEntryStatus_Type())
crpmsVpdnEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:crpmsVpdnEntryStatus.setStatus(_A)
_CrpmsVpdnGroupCpTable_Object=MibTable
crpmsVpdnGroupCpTable=_CrpmsVpdnGroupCpTable_Object((1,3,6,1,4,1,9,10,84,1,3,2))
if mibBuilder.loadTexts:crpmsVpdnGroupCpTable.setStatus(_A)
_CrpmsVpdnGroupCpEntry_Object=MibTableRow
crpmsVpdnGroupCpEntry=_CrpmsVpdnGroupCpEntry_Object((1,3,6,1,4,1,9,10,84,1,3,2,1))
crpmsVpdnGroupCpEntry.setIndexNames((0,_B,_Q),(1,_B,_R))
if mibBuilder.loadTexts:crpmsVpdnGroupCpEntry.setStatus(_A)
class _CrpmsVpdnGroupCpVpdnGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_CrpmsVpdnGroupCpVpdnGroupName_Type.__name__=_F
_CrpmsVpdnGroupCpVpdnGroupName_Object=MibTableColumn
crpmsVpdnGroupCpVpdnGroupName=_CrpmsVpdnGroupCpVpdnGroupName_Object((1,3,6,1,4,1,9,10,84,1,3,2,1,1),_CrpmsVpdnGroupCpVpdnGroupName_Type())
crpmsVpdnGroupCpVpdnGroupName.setMaxAccess(_G)
if mibBuilder.loadTexts:crpmsVpdnGroupCpVpdnGroupName.setStatus(_A)
class _CrpmsVpdnGroupCpCpName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_CrpmsVpdnGroupCpCpName_Type.__name__=_F
_CrpmsVpdnGroupCpCpName_Object=MibTableColumn
crpmsVpdnGroupCpCpName=_CrpmsVpdnGroupCpCpName_Object((1,3,6,1,4,1,9,10,84,1,3,2,1,2),_CrpmsVpdnGroupCpCpName_Type())
crpmsVpdnGroupCpCpName.setMaxAccess(_G)
if mibBuilder.loadTexts:crpmsVpdnGroupCpCpName.setStatus(_A)
_CrpmsVpdnGroupCpEntryStatus_Type=RowStatus
_CrpmsVpdnGroupCpEntryStatus_Object=MibTableColumn
crpmsVpdnGroupCpEntryStatus=_CrpmsVpdnGroupCpEntryStatus_Object((1,3,6,1,4,1,9,10,84,1,3,2,1,3),_CrpmsVpdnGroupCpEntryStatus_Type())
crpmsVpdnGroupCpEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:crpmsVpdnGroupCpEntryStatus.setStatus(_A)
_CrpmsNotif_ObjectIdentity=ObjectIdentity
crpmsNotif=_CrpmsNotif_ObjectIdentity((1,3,6,1,4,1,9,10,84,1,4))
_CrpmsAlarmObject_Type=ObjectIdentifier
_CrpmsAlarmObject_Object=MibScalar
crpmsAlarmObject=_CrpmsAlarmObject_Object((1,3,6,1,4,1,9,10,84,1,4,1),_CrpmsAlarmObject_Type())
crpmsAlarmObject.setMaxAccess(_L)
if mibBuilder.loadTexts:crpmsAlarmObject.setStatus(_A)
_CrpmsAlarmValue_Type=Unsigned32
_CrpmsAlarmValue_Object=MibScalar
crpmsAlarmValue=_CrpmsAlarmValue_Object((1,3,6,1,4,1,9,10,84,1,4,2),_CrpmsAlarmValue_Type())
crpmsAlarmValue.setMaxAccess(_L)
if mibBuilder.loadTexts:crpmsAlarmValue.setStatus(_A)
_CrpmsAlarmThresholdObject_Type=ObjectIdentifier
_CrpmsAlarmThresholdObject_Object=MibScalar
crpmsAlarmThresholdObject=_CrpmsAlarmThresholdObject_Object((1,3,6,1,4,1,9,10,84,1,4,3),_CrpmsAlarmThresholdObject_Type())
crpmsAlarmThresholdObject.setMaxAccess(_L)
if mibBuilder.loadTexts:crpmsAlarmThresholdObject.setStatus(_A)
_CiscoRpmsMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoRpmsMIBNotificationPrefix=_CiscoRpmsMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,84,2))
_CiscoRpmsMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoRpmsMIBNotifications=_CiscoRpmsMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,84,2,0))
_CiscoRpmsMIBConformance_ObjectIdentity=ObjectIdentity
ciscoRpmsMIBConformance=_CiscoRpmsMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,84,3))
_CiscoRpmsMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoRpmsMIBCompliances=_CiscoRpmsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,84,3,1))
_CiscoRpmsMIBGroups_ObjectIdentity=ObjectIdentity
ciscoRpmsMIBGroups=_CiscoRpmsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,84,3,2))
crpmsSystemGroup=ObjectGroup((1,3,6,1,4,1,9,10,84,3,2,1))
crpmsSystemGroup.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:crpmsSystemGroup.setStatus(_A)
crpmsCpGroup=ObjectGroup((1,3,6,1,4,1,9,10,84,3,2,2))
crpmsCpGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:crpmsCpGroup.setStatus(_A)
crpmsVpdnGroup=ObjectGroup((1,3,6,1,4,1,9,10,84,3,2,3))
crpmsVpdnGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:crpmsVpdnGroup.setStatus(_A)
crpmsNotifGroup=ObjectGroup((1,3,6,1,4,1,9,10,84,3,2,4))
crpmsNotifGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:crpmsNotifGroup.setStatus(_A)
crpmsRisingAlarm=NotificationType((1,3,6,1,4,1,9,10,84,2,0,1))
crpmsRisingAlarm.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:crpmsRisingAlarm.setStatus(_A)
crpmsFallingAlarm=NotificationType((1,3,6,1,4,1,9,10,84,2,0,2))
crpmsFallingAlarm.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:crpmsFallingAlarm.setStatus(_A)
crpmsThresholdNotifGroup=NotificationGroup((1,3,6,1,4,1,9,10,84,3,2,5))
crpmsThresholdNotifGroup.setObjects(*((_B,_v),(_B,_w)))
if mibBuilder.loadTexts:crpmsThresholdNotifGroup.setStatus(_A)
ciscoRpmsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,84,3,1,1))
ciscoRpmsMIBCompliance.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:ciscoRpmsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoRpmsMIB':ciscoRpmsMIB,'ciscoRpmsMIBObjects':ciscoRpmsMIBObjects,'crpmsSystem':crpmsSystem,'crpmsSubsystemTable':crpmsSubsystemTable,'crpmsSubsystemEntry':crpmsSubsystemEntry,_N:crpmsSubsystemIndex,_S:crpmsSubsystemName,_T:crpmsSubsystemUptime,'crpmsCustomerProfile':crpmsCustomerProfile,'crpmsCpTable':crpmsCpTable,'crpmsCpEntry':crpmsCpEntry,_O:crpmsCpName,_U:crpmsCpLimit,_V:crpmsCpOverflowLimit,_W:crpmsCpActiveCalls,_X:crpmsCpActiveOverflowCalls,_Y:crpmsCpAttemptedCalls,_Z:crpmsCpAttemptedOverflowCalls,_a:crpmsCpRejections,_b:crpmsCpOverflowRejections,_c:crpmsCpLimitThreshold,_d:crpmsCpOverflowLimitThreshold,_e:crpmsCpCallRejectionThreshold,_f:crpmsCpOverflowRejectThreshold,_g:crpmsCpEntryStatus,'crpmsVpdn':crpmsVpdn,'crpmsVpdnGroupTable':crpmsVpdnGroupTable,'crpmsVpdnGroupEntry':crpmsVpdnGroupEntry,_P:crpmsVpdnGroupName,_h:crpmsVpdnTunnelId,_i:crpmsVpdnTunnelProtocol,_j:crpmsVpdnLimit,_k:crpmsVpdnOverflowLimit,_l:crpmsVpdnMlpBundleLimit,_m:crpmsVpdnLinksPerBundleLimit,_n:crpmsVpdnBundles,_o:crpmsVpdnActiveCalls,_p:crpmsVpdnActiveOverflowCalls,_q:crpmsVpdnRejections,_r:crpmsVpdnSizeRejections,_s:crpmsVpdnLimitThreshold,_t:crpmsVpdnEntryStatus,'crpmsVpdnGroupCpTable':crpmsVpdnGroupCpTable,'crpmsVpdnGroupCpEntry':crpmsVpdnGroupCpEntry,_Q:crpmsVpdnGroupCpVpdnGroupName,_R:crpmsVpdnGroupCpCpName,_u:crpmsVpdnGroupCpEntryStatus,'crpmsNotif':crpmsNotif,_I:crpmsAlarmObject,_J:crpmsAlarmValue,_K:crpmsAlarmThresholdObject,'ciscoRpmsMIBNotificationPrefix':ciscoRpmsMIBNotificationPrefix,'ciscoRpmsMIBNotifications':ciscoRpmsMIBNotifications,_v:crpmsRisingAlarm,_w:crpmsFallingAlarm,'ciscoRpmsMIBConformance':ciscoRpmsMIBConformance,'ciscoRpmsMIBCompliances':ciscoRpmsMIBCompliances,'ciscoRpmsMIBCompliance':ciscoRpmsMIBCompliance,'ciscoRpmsMIBGroups':ciscoRpmsMIBGroups,_x:crpmsSystemGroup,_y:crpmsCpGroup,_z:crpmsVpdnGroup,_A0:crpmsNotifGroup,_A1:crpmsThresholdNotifGroup})