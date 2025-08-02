_A1='l2vmBgpADGroup'
_A0='l2vmBgpRTCfgRT'
_z='l2vmBgpRTCfgType'
_y='l2vmBgpRTCfgOperStatus'
_x='l2vmBgpRTCfgAdminStatus'
_w='l2vmBgpRTCfgRowStatus'
_v='l2vmSjJoinStatus'
_u='l2vmMjJoinStatus'
_t='l2vmMjOperStatus'
_s='l2vmMjAdminStatus'
_r='l2vmMjRowStatus'
_q='l2vmEntityBdpiBufferPoolSize'
_p='l2vmEntitySupportVpls'
_o='l2vmEntityVpnNotifBufferPoolSize'
_n='l2vmEntityVpnNotifEnable'
_m='l2vmEntityRetryInterval'
_l='l2vmEntityRpiFailTimeout'
_k='l2vmEntityRpiBufferPoolSize'
_j='l2vmEntityPvpiBufferPoolSize'
_i='l2vmEntityRescheduleLimit'
_h='l2vmEntityRestartDuration'
_g='l2vmEntityTimerGranularity'
_f='l2vmEntityNbasePriority'
_e='l2vmEntityVpwsIndexNext'
_d='l2vmEntityVplsIndexNext'
_c='l2vmEntityOperStatus'
_b='l2vmEntityAdminStatus'
_a='l2vmEntityRowStatus'
_Z='BgpExtendedCommunity'
_Y='BgpRouteTargetType'
_X='l2vmBgpRTCfgIndex'
_W='l2vmBgpRTCfgVpnIndex'
_V='l2vmBgpRTCfgVpnType'
_U='l2vmSjSubIndex'
_T='l2vmSjPartnerIndex'
_S='l2vmSjPartnerType'
_R='l2vmSjInterfaceId'
_Q='l2vmMjSubIndex'
_P='l2vmMjPartnerIndex'
_O='l2vmMjPartnerType'
_N='l2vmMjInterfaceId'
_M='l2vpnFrameworkGroup'
_L='none'
_K='TruthValue'
_J='Unsigned32'
_I='TimeTicks'
_H='AdminStatus'
_G='l2vmEntityIndex'
_F='read-only'
_E='Integer32'
_D='not-accessible'
_C='read-create'
_B='DC-L2VPN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AdminStatus,MjStatus,NpgOperStatus,NumericIndex,OperStatus,SjStatus=mibBuilder.importSymbols('DC-MASTER-TC',_H,'MjStatus','NpgOperStatus','NumericIndex','OperStatus','SjStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_I,_J,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_K)
l2vpnMib=ModuleIdentity((1,2,826,0,1,1578918,5,94,2,1))
class L2vmMjIfId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(696844288,697761792,1921384448)));namedValues=NamedValues(*(('ifAtgI3',696844288),('ifAtgBdpi',697761792),('ifAtgPvpi',1921384448)))
class L2vmSjIfId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1031864320));namedValues=NamedValues(('ifAtgRpi',1031864320))
class L2vpnADType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('bgp',2)))
class L2vpnSigType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('ldp',2),('bgp',3)))
class L2vpnPwBindType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pwMibIndex',1),('lclRmtVeId',2)))
class L2vpnType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),('vpls',1),('vpws',2)))
class L2vpnSiteId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class L2vpnVeIdOrZero(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class BgpRouteDistinguisher(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class BgpExtendedCommunity(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class BgpRouteTargetType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('import',1),('export',2),('both',3)))
_L2vpnObjects_ObjectIdentity=ObjectIdentity
l2vpnObjects=_L2vpnObjects_ObjectIdentity((1,2,826,0,1,1578918,5,94,2,1,1))
_L2vmEntityTable_Object=MibTable
l2vmEntityTable=_L2vmEntityTable_Object((1,2,826,0,1,1578918,5,94,2,1,1,1))
if mibBuilder.loadTexts:l2vmEntityTable.setStatus(_A)
_L2vmEntityEntry_Object=MibTableRow
l2vmEntityEntry=_L2vmEntityEntry_Object((1,2,826,0,1,1578918,5,94,2,1,1,1,1))
l2vmEntityEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:l2vmEntityEntry.setStatus(_A)
_L2vmEntityIndex_Type=NumericIndex
_L2vmEntityIndex_Object=MibTableColumn
l2vmEntityIndex=_L2vmEntityIndex_Object((1,2,826,0,1,1578918,5,94,2,1,1,1,1,1),_L2vmEntityIndex_Type())
l2vmEntityIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:l2vmEntityIndex.setStatus(_A)
_L2vmEntityRowStatus_Type=RowStatus
_L2vmEntityRowStatus_Object=MibTableColumn
l2vmEntityRowStatus=_L2vmEntityRowStatus_Object((1,2,826,0,1,1578918,5,94,2,1,1,1,1,2),_L2vmEntityRowStatus_Type())
l2vmEntityRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:l2vmEntityRowStatus.setStatus(_A)
class _L2vmEntityAdminStatus_Type(AdminStatus):defaultValue=1
_L2vmEntityAdminStatus_Type.__name__=_H
_L2vmEntityAdminStatus_Object=MibTableColumn
l2vmEntityAdminStatus=_L2vmEntityAdminStatus_Object((1,2,826,0,1,1578918,5,94,2,1,1,1,1,3),_L2vmEntityAdminStatus_Type())
l2vmEntityAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:l2vmEntityAdminStatus.setStatus(_A)
_L2vmEntityOperStatus_Type=NpgOperStatus
_L2vmEntityOperStatus_Object=MibTableColumn
l2vmEntityOperStatus=_L2vmEntityOperStatus_Object((1,2,826,0,1,1578918,5,94,2,1,1,1,1,4),_L2vmEntityOperStatus_Type())
l2vmEntityOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:l2vmEntityOperStatus.setStatus(_A)
_L2vmEntityVplsIndexNext_Type=NumericIndex
_L2vmEntityVplsIndexNext_Object=MibTableColumn
l2vmEntityVplsIndexNext=_L2vmEntityVplsIndexNext_Object((1,2,826,0,1,1578918,5,94,2,1,1,1,1,5),_L2vmEntityVplsIndexNext_Type())
l2vmEntityVplsIndexNext.setMaxAccess(_F)
if mibBuilder.loadTexts:l2vmEntityVplsIndexNext.setStatus(_A)
_L2vmEntityVpwsIndexNext_Type=NumericIndex
_L2vmEntityVpwsIndexNext_Object=MibTableColumn
l2vmEntityVpwsIndexNext=_L2vmEntityVpwsIndexNext_Object((1,2,826,0,1,1578918,5,94,2,1,1,1,1,6),_L2vmEntityVpwsIndexNext_Type())
l2vmEntityVpwsIndexNext.setMaxAccess(_F)
if mibBuilder.loadTexts:l2vmEntityVpwsIndexNext.setStatus(_A)
class _L2vmEntityNbasePriority_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_L2vmEntityNbasePriority_Type.__name__=_E
_L2vmEntityNbasePriority_Object=MibTableColumn
l2vmEntityNbasePriority=_L2vmEntityNbasePriority_Object((1,2,826,0,1,1578918,5,94,2,1,1,1,1,7),_L2vmEntityNbasePriority_Type())
l2vmEntityNbasePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:l2vmEntityNbasePriority.setStatus(_A)
class _L2vmEntityTimerGranularity_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_L2vmEntityTimerGranularity_Type.__name__=_E
_L2vmEntityTimerGranularity_Object=MibTableColumn
l2vmEntityTimerGranularity=_L2vmEntityTimerGranularity_Object((1,2,826,0,1,1578918,5,94,2,1,1,1,1,8),_L2vmEntityTimerGranularity_Type())
l2vmEntityTimerGranularity.setMaxAccess(_C)
if mibBuilder.loadTexts:l2vmEntityTimerGranularity.setStatus(_A)
class _L2vmEntityRestartDuration_Type(TimeTicks):defaultValue=18000
_L2vmEntityRestartDuration_Type.__name__=_I
_L2vmEntityRestartDuration_Object=MibTableColumn
l2vmEntityRestartDuration=_L2vmEntityRestartDuration_Object((1,2,826,0,1,1578918,5,94,2,1,1,1,1,9),_L2vmEntityRestartDuration_Type())
l2vmEntityRestartDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:l2vmEntityRestartDuration.setStatus(_A)
class _L2vmEntityRescheduleLimit_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_L2vmEntityRescheduleLimit_Type.__name__=_E
_L2vmEntityRescheduleLimit_Object=MibTableColumn
l2vmEntityRescheduleLimit=_L2vmEntityRescheduleLimit_Object((1,2,826,0,1,1578918,5,94,2,1,1,1,1,10),_L2vmEntityRescheduleLimit_Type())
l2vmEntityRescheduleLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:l2vmEntityRescheduleLimit.setStatus(_A)
class _L2vmEntityPvpiBufferPoolSize_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_L2vmEntityPvpiBufferPoolSize_Type.__name__=_E
_L2vmEntityPvpiBufferPoolSize_Object=MibTableColumn
l2vmEntityPvpiBufferPoolSize=_L2vmEntityPvpiBufferPoolSize_Object((1,2,826,0,1,1578918,5,94,2,1,1,1,1,11),_L2vmEntityPvpiBufferPoolSize_Type())
l2vmEntityPvpiBufferPoolSize.setMaxAccess(_C)
if mibBuilder.loadTexts:l2vmEntityPvpiBufferPoolSize.setStatus(_A)
class _L2vmEntityRpiBufferPoolSize_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_L2vmEntityRpiBufferPoolSize_Type.__name__=_E
_L2vmEntityRpiBufferPoolSize_Object=MibTableColumn
l2vmEntityRpiBufferPoolSize=_L2vmEntityRpiBufferPoolSize_Object((1,2,826,0,1,1578918,5,94,2,1,1,1,1,12),_L2vmEntityRpiBufferPoolSize_Type())
l2vmEntityRpiBufferPoolSize.setMaxAccess(_C)
if mibBuilder.loadTexts:l2vmEntityRpiBufferPoolSize.setStatus(_A)
class _L2vmEntityRpiFailTimeout_Type(TimeTicks):defaultValue=3000
_L2vmEntityRpiFailTimeout_Type.__name__=_I
_L2vmEntityRpiFailTimeout_Object=MibTableColumn
l2vmEntityRpiFailTimeout=_L2vmEntityRpiFailTimeout_Object((1,2,826,0,1,1578918,5,94,2,1,1,1,1,13),_L2vmEntityRpiFailTimeout_Type())
l2vmEntityRpiFailTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:l2vmEntityRpiFailTimeout.setStatus(_A)
class _L2vmEntityRetryInterval_Type(TimeTicks):defaultValue=1000
_L2vmEntityRetryInterval_Type.__name__=_I
_L2vmEntityRetryInterval_Object=MibTableColumn
l2vmEntityRetryInterval=_L2vmEntityRetryInterval_Object((1,2,826,0,1,1578918,5,94,2,1,1,1,1,14),_L2vmEntityRetryInterval_Type())
l2vmEntityRetryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:l2vmEntityRetryInterval.setStatus(_A)
class _L2vmEntityVpnNotifEnable_Type(TruthValue):defaultValue=2
_L2vmEntityVpnNotifEnable_Type.__name__=_K
_L2vmEntityVpnNotifEnable_Object=MibTableColumn
l2vmEntityVpnNotifEnable=_L2vmEntityVpnNotifEnable_Object((1,2,826,0,1,1578918,5,94,2,1,1,1,1,15),_L2vmEntityVpnNotifEnable_Type())
l2vmEntityVpnNotifEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:l2vmEntityVpnNotifEnable.setStatus(_A)
class _L2vmEntityVpnNotifBufferPoolSize_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_L2vmEntityVpnNotifBufferPoolSize_Type.__name__=_E
_L2vmEntityVpnNotifBufferPoolSize_Object=MibTableColumn
l2vmEntityVpnNotifBufferPoolSize=_L2vmEntityVpnNotifBufferPoolSize_Object((1,2,826,0,1,1578918,5,94,2,1,1,1,1,16),_L2vmEntityVpnNotifBufferPoolSize_Type())
l2vmEntityVpnNotifBufferPoolSize.setMaxAccess(_C)
if mibBuilder.loadTexts:l2vmEntityVpnNotifBufferPoolSize.setStatus(_A)
class _L2vmEntitySupportVpls_Type(TruthValue):defaultValue=2
_L2vmEntitySupportVpls_Type.__name__=_K
_L2vmEntitySupportVpls_Object=MibTableColumn
l2vmEntitySupportVpls=_L2vmEntitySupportVpls_Object((1,2,826,0,1,1578918,5,94,2,1,1,1,1,17),_L2vmEntitySupportVpls_Type())
l2vmEntitySupportVpls.setMaxAccess(_C)
if mibBuilder.loadTexts:l2vmEntitySupportVpls.setStatus(_A)
class _L2vmEntityBdpiBufferPoolSize_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_L2vmEntityBdpiBufferPoolSize_Type.__name__=_E
_L2vmEntityBdpiBufferPoolSize_Object=MibTableColumn
l2vmEntityBdpiBufferPoolSize=_L2vmEntityBdpiBufferPoolSize_Object((1,2,826,0,1,1578918,5,94,2,1,1,1,1,18),_L2vmEntityBdpiBufferPoolSize_Type())
l2vmEntityBdpiBufferPoolSize.setMaxAccess(_C)
if mibBuilder.loadTexts:l2vmEntityBdpiBufferPoolSize.setStatus(_A)
_L2vmMjTable_Object=MibTable
l2vmMjTable=_L2vmMjTable_Object((1,2,826,0,1,1578918,5,94,2,1,1,2))
if mibBuilder.loadTexts:l2vmMjTable.setStatus(_A)
_L2vmMjEntry_Object=MibTableRow
l2vmMjEntry=_L2vmMjEntry_Object((1,2,826,0,1,1578918,5,94,2,1,1,2,1))
l2vmMjEntry.setIndexNames((0,_B,_G),(0,_B,_N),(0,_B,_O),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:l2vmMjEntry.setStatus(_A)
_L2vmMjInterfaceId_Type=L2vmMjIfId
_L2vmMjInterfaceId_Object=MibTableColumn
l2vmMjInterfaceId=_L2vmMjInterfaceId_Object((1,2,826,0,1,1578918,5,94,2,1,1,2,1,2),_L2vmMjInterfaceId_Type())
l2vmMjInterfaceId.setMaxAccess(_D)
if mibBuilder.loadTexts:l2vmMjInterfaceId.setStatus(_A)
_L2vmMjPartnerType_Type=Unsigned32
_L2vmMjPartnerType_Object=MibTableColumn
l2vmMjPartnerType=_L2vmMjPartnerType_Object((1,2,826,0,1,1578918,5,94,2,1,1,2,1,3),_L2vmMjPartnerType_Type())
l2vmMjPartnerType.setMaxAccess(_D)
if mibBuilder.loadTexts:l2vmMjPartnerType.setStatus(_A)
class _L2vmMjPartnerIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_L2vmMjPartnerIndex_Type.__name__=_J
_L2vmMjPartnerIndex_Object=MibTableColumn
l2vmMjPartnerIndex=_L2vmMjPartnerIndex_Object((1,2,826,0,1,1578918,5,94,2,1,1,2,1,4),_L2vmMjPartnerIndex_Type())
l2vmMjPartnerIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:l2vmMjPartnerIndex.setStatus(_A)
_L2vmMjSubIndex_Type=Unsigned32
_L2vmMjSubIndex_Object=MibTableColumn
l2vmMjSubIndex=_L2vmMjSubIndex_Object((1,2,826,0,1,1578918,5,94,2,1,1,2,1,5),_L2vmMjSubIndex_Type())
l2vmMjSubIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:l2vmMjSubIndex.setStatus(_A)
_L2vmMjRowStatus_Type=RowStatus
_L2vmMjRowStatus_Object=MibTableColumn
l2vmMjRowStatus=_L2vmMjRowStatus_Object((1,2,826,0,1,1578918,5,94,2,1,1,2,1,6),_L2vmMjRowStatus_Type())
l2vmMjRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:l2vmMjRowStatus.setStatus(_A)
class _L2vmMjAdminStatus_Type(AdminStatus):defaultValue=1
_L2vmMjAdminStatus_Type.__name__=_H
_L2vmMjAdminStatus_Object=MibTableColumn
l2vmMjAdminStatus=_L2vmMjAdminStatus_Object((1,2,826,0,1,1578918,5,94,2,1,1,2,1,7),_L2vmMjAdminStatus_Type())
l2vmMjAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:l2vmMjAdminStatus.setStatus(_A)
_L2vmMjOperStatus_Type=OperStatus
_L2vmMjOperStatus_Object=MibTableColumn
l2vmMjOperStatus=_L2vmMjOperStatus_Object((1,2,826,0,1,1578918,5,94,2,1,1,2,1,8),_L2vmMjOperStatus_Type())
l2vmMjOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:l2vmMjOperStatus.setStatus(_A)
_L2vmMjJoinStatus_Type=MjStatus
_L2vmMjJoinStatus_Object=MibTableColumn
l2vmMjJoinStatus=_L2vmMjJoinStatus_Object((1,2,826,0,1,1578918,5,94,2,1,1,2,1,9),_L2vmMjJoinStatus_Type())
l2vmMjJoinStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:l2vmMjJoinStatus.setStatus(_A)
_L2vmSjTable_Object=MibTable
l2vmSjTable=_L2vmSjTable_Object((1,2,826,0,1,1578918,5,94,2,1,1,3))
if mibBuilder.loadTexts:l2vmSjTable.setStatus(_A)
_L2vmSjEntry_Object=MibTableRow
l2vmSjEntry=_L2vmSjEntry_Object((1,2,826,0,1,1578918,5,94,2,1,1,3,1))
l2vmSjEntry.setIndexNames((0,_B,_G),(0,_B,_R),(0,_B,_S),(0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:l2vmSjEntry.setStatus(_A)
_L2vmSjInterfaceId_Type=L2vmSjIfId
_L2vmSjInterfaceId_Object=MibTableColumn
l2vmSjInterfaceId=_L2vmSjInterfaceId_Object((1,2,826,0,1,1578918,5,94,2,1,1,3,1,2),_L2vmSjInterfaceId_Type())
l2vmSjInterfaceId.setMaxAccess(_D)
if mibBuilder.loadTexts:l2vmSjInterfaceId.setStatus(_A)
_L2vmSjPartnerType_Type=Unsigned32
_L2vmSjPartnerType_Object=MibTableColumn
l2vmSjPartnerType=_L2vmSjPartnerType_Object((1,2,826,0,1,1578918,5,94,2,1,1,3,1,3),_L2vmSjPartnerType_Type())
l2vmSjPartnerType.setMaxAccess(_D)
if mibBuilder.loadTexts:l2vmSjPartnerType.setStatus(_A)
class _L2vmSjPartnerIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_L2vmSjPartnerIndex_Type.__name__=_J
_L2vmSjPartnerIndex_Object=MibTableColumn
l2vmSjPartnerIndex=_L2vmSjPartnerIndex_Object((1,2,826,0,1,1578918,5,94,2,1,1,3,1,4),_L2vmSjPartnerIndex_Type())
l2vmSjPartnerIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:l2vmSjPartnerIndex.setStatus(_A)
_L2vmSjSubIndex_Type=Unsigned32
_L2vmSjSubIndex_Object=MibTableColumn
l2vmSjSubIndex=_L2vmSjSubIndex_Object((1,2,826,0,1,1578918,5,94,2,1,1,3,1,5),_L2vmSjSubIndex_Type())
l2vmSjSubIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:l2vmSjSubIndex.setStatus(_A)
_L2vmSjJoinStatus_Type=SjStatus
_L2vmSjJoinStatus_Object=MibTableColumn
l2vmSjJoinStatus=_L2vmSjJoinStatus_Object((1,2,826,0,1,1578918,5,94,2,1,1,3,1,6),_L2vmSjJoinStatus_Type())
l2vmSjJoinStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:l2vmSjJoinStatus.setStatus(_A)
_L2vmBgpRTCfgTable_Object=MibTable
l2vmBgpRTCfgTable=_L2vmBgpRTCfgTable_Object((1,2,826,0,1,1578918,5,94,2,1,1,4))
if mibBuilder.loadTexts:l2vmBgpRTCfgTable.setStatus(_A)
_L2vmBgpRTCfgEntry_Object=MibTableRow
l2vmBgpRTCfgEntry=_L2vmBgpRTCfgEntry_Object((1,2,826,0,1,1578918,5,94,2,1,1,4,1))
l2vmBgpRTCfgEntry.setIndexNames((0,_B,_G),(0,_B,_V),(0,_B,_W),(0,_B,_X))
if mibBuilder.loadTexts:l2vmBgpRTCfgEntry.setStatus(_A)
_L2vmBgpRTCfgVpnType_Type=L2vpnType
_L2vmBgpRTCfgVpnType_Object=MibTableColumn
l2vmBgpRTCfgVpnType=_L2vmBgpRTCfgVpnType_Object((1,2,826,0,1,1578918,5,94,2,1,1,4,1,2),_L2vmBgpRTCfgVpnType_Type())
l2vmBgpRTCfgVpnType.setMaxAccess(_D)
if mibBuilder.loadTexts:l2vmBgpRTCfgVpnType.setStatus(_A)
_L2vmBgpRTCfgVpnIndex_Type=NumericIndex
_L2vmBgpRTCfgVpnIndex_Object=MibTableColumn
l2vmBgpRTCfgVpnIndex=_L2vmBgpRTCfgVpnIndex_Object((1,2,826,0,1,1578918,5,94,2,1,1,4,1,3),_L2vmBgpRTCfgVpnIndex_Type())
l2vmBgpRTCfgVpnIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:l2vmBgpRTCfgVpnIndex.setStatus(_A)
_L2vmBgpRTCfgIndex_Type=NumericIndex
_L2vmBgpRTCfgIndex_Object=MibTableColumn
l2vmBgpRTCfgIndex=_L2vmBgpRTCfgIndex_Object((1,2,826,0,1,1578918,5,94,2,1,1,4,1,4),_L2vmBgpRTCfgIndex_Type())
l2vmBgpRTCfgIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:l2vmBgpRTCfgIndex.setStatus(_A)
_L2vmBgpRTCfgRowStatus_Type=RowStatus
_L2vmBgpRTCfgRowStatus_Object=MibTableColumn
l2vmBgpRTCfgRowStatus=_L2vmBgpRTCfgRowStatus_Object((1,2,826,0,1,1578918,5,94,2,1,1,4,1,5),_L2vmBgpRTCfgRowStatus_Type())
l2vmBgpRTCfgRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:l2vmBgpRTCfgRowStatus.setStatus(_A)
class _L2vmBgpRTCfgAdminStatus_Type(AdminStatus):defaultValue=1
_L2vmBgpRTCfgAdminStatus_Type.__name__=_H
_L2vmBgpRTCfgAdminStatus_Object=MibTableColumn
l2vmBgpRTCfgAdminStatus=_L2vmBgpRTCfgAdminStatus_Object((1,2,826,0,1,1578918,5,94,2,1,1,4,1,6),_L2vmBgpRTCfgAdminStatus_Type())
l2vmBgpRTCfgAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:l2vmBgpRTCfgAdminStatus.setStatus(_A)
_L2vmBgpRTCfgOperStatus_Type=NpgOperStatus
_L2vmBgpRTCfgOperStatus_Object=MibTableColumn
l2vmBgpRTCfgOperStatus=_L2vmBgpRTCfgOperStatus_Object((1,2,826,0,1,1578918,5,94,2,1,1,4,1,7),_L2vmBgpRTCfgOperStatus_Type())
l2vmBgpRTCfgOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:l2vmBgpRTCfgOperStatus.setStatus(_A)
class _L2vmBgpRTCfgType_Type(BgpRouteTargetType):defaultValue=3
_L2vmBgpRTCfgType_Type.__name__=_Y
_L2vmBgpRTCfgType_Object=MibTableColumn
l2vmBgpRTCfgType=_L2vmBgpRTCfgType_Object((1,2,826,0,1,1578918,5,94,2,1,1,4,1,8),_L2vmBgpRTCfgType_Type())
l2vmBgpRTCfgType.setMaxAccess(_C)
if mibBuilder.loadTexts:l2vmBgpRTCfgType.setStatus(_A)
class _L2vmBgpRTCfgRT_Type(BgpExtendedCommunity):defaultHexValue='0000000000000000'
_L2vmBgpRTCfgRT_Type.__name__=_Z
_L2vmBgpRTCfgRT_Object=MibTableColumn
l2vmBgpRTCfgRT=_L2vmBgpRTCfgRT_Object((1,2,826,0,1,1578918,5,94,2,1,1,4,1,9),_L2vmBgpRTCfgRT_Type())
l2vmBgpRTCfgRT.setMaxAccess(_C)
if mibBuilder.loadTexts:l2vmBgpRTCfgRT.setStatus(_A)
_L2vpnConformance_ObjectIdentity=ObjectIdentity
l2vpnConformance=_L2vpnConformance_ObjectIdentity((1,2,826,0,1,1578918,5,94,2,1,2))
_L2vpnCompliances_ObjectIdentity=ObjectIdentity
l2vpnCompliances=_L2vpnCompliances_ObjectIdentity((1,2,826,0,1,1578918,5,94,2,1,2,1))
_L2vpnGroups_ObjectIdentity=ObjectIdentity
l2vpnGroups=_L2vpnGroups_ObjectIdentity((1,2,826,0,1,1578918,5,94,2,1,2,2))
l2vpnFrameworkGroup=ObjectGroup((1,2,826,0,1,1578918,5,94,2,1,2,2,1))
l2vpnFrameworkGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:l2vpnFrameworkGroup.setStatus(_A)
l2vmBgpADGroup=ObjectGroup((1,2,826,0,1,1578918,5,94,2,1,2,2,2))
l2vmBgpADGroup.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:l2vmBgpADGroup.setStatus(_A)
l2vpnFrameworkCompliance=ModuleCompliance((1,2,826,0,1,1578918,5,94,2,1,2,1,1))
l2vpnFrameworkCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:l2vpnFrameworkCompliance.setStatus(_A)
l2vmBgpADCompliance=ModuleCompliance((1,2,826,0,1,1578918,5,94,2,1,2,1,2))
l2vmBgpADCompliance.setObjects(*((_B,_M),(_B,_A1)))
if mibBuilder.loadTexts:l2vmBgpADCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'L2vmMjIfId':L2vmMjIfId,'L2vmSjIfId':L2vmSjIfId,'L2vpnADType':L2vpnADType,'L2vpnSigType':L2vpnSigType,'L2vpnPwBindType':L2vpnPwBindType,'L2vpnType':L2vpnType,'L2vpnSiteId':L2vpnSiteId,'L2vpnVeIdOrZero':L2vpnVeIdOrZero,'BgpRouteDistinguisher':BgpRouteDistinguisher,_Z:BgpExtendedCommunity,_Y:BgpRouteTargetType,'l2vpnMib':l2vpnMib,'l2vpnObjects':l2vpnObjects,'l2vmEntityTable':l2vmEntityTable,'l2vmEntityEntry':l2vmEntityEntry,_G:l2vmEntityIndex,_a:l2vmEntityRowStatus,_b:l2vmEntityAdminStatus,_c:l2vmEntityOperStatus,_d:l2vmEntityVplsIndexNext,_e:l2vmEntityVpwsIndexNext,_f:l2vmEntityNbasePriority,_g:l2vmEntityTimerGranularity,_h:l2vmEntityRestartDuration,_i:l2vmEntityRescheduleLimit,_j:l2vmEntityPvpiBufferPoolSize,_k:l2vmEntityRpiBufferPoolSize,_l:l2vmEntityRpiFailTimeout,_m:l2vmEntityRetryInterval,_n:l2vmEntityVpnNotifEnable,_o:l2vmEntityVpnNotifBufferPoolSize,_p:l2vmEntitySupportVpls,_q:l2vmEntityBdpiBufferPoolSize,'l2vmMjTable':l2vmMjTable,'l2vmMjEntry':l2vmMjEntry,_N:l2vmMjInterfaceId,_O:l2vmMjPartnerType,_P:l2vmMjPartnerIndex,_Q:l2vmMjSubIndex,_r:l2vmMjRowStatus,_s:l2vmMjAdminStatus,_t:l2vmMjOperStatus,_u:l2vmMjJoinStatus,'l2vmSjTable':l2vmSjTable,'l2vmSjEntry':l2vmSjEntry,_R:l2vmSjInterfaceId,_S:l2vmSjPartnerType,_T:l2vmSjPartnerIndex,_U:l2vmSjSubIndex,_v:l2vmSjJoinStatus,'l2vmBgpRTCfgTable':l2vmBgpRTCfgTable,'l2vmBgpRTCfgEntry':l2vmBgpRTCfgEntry,_V:l2vmBgpRTCfgVpnType,_W:l2vmBgpRTCfgVpnIndex,_X:l2vmBgpRTCfgIndex,_w:l2vmBgpRTCfgRowStatus,_x:l2vmBgpRTCfgAdminStatus,_y:l2vmBgpRTCfgOperStatus,_z:l2vmBgpRTCfgType,_A0:l2vmBgpRTCfgRT,'l2vpnConformance':l2vpnConformance,'l2vpnCompliances':l2vpnCompliances,'l2vpnFrameworkCompliance':l2vpnFrameworkCompliance,'l2vmBgpADCompliance':l2vmBgpADCompliance,'l2vpnGroups':l2vpnGroups,_M:l2vpnFrameworkGroup,_A1:l2vmBgpADGroup})