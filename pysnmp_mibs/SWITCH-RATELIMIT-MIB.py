_M='rcRateLimitVlanStatisticsEntry'
_L='rcRateLimitVlanSPVlanID'
_K='rcRateLimitVlanCVlanID'
_J='rcRateLimitVlanType'
_I='rcRateLimitPortIndex'
_H='read-write'
_G='not-accessible'
_F='kbps'
_E='read-only'
_D='SWITCH-RATELIMIT-MIB'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
EnableVar,=mibBuilder.importSymbols('SWITCH-TC','EnableVar')
rcRateLimit=ModuleIdentity((1,3,6,1,4,1,8886,6,1,2))
_RcUplinkPort_Type=Integer32
_RcUplinkPort_Object=MibScalar
rcUplinkPort=_RcUplinkPort_Object((1,3,6,1,4,1,8886,6,1,2,1),_RcUplinkPort_Type())
rcUplinkPort.setMaxAccess(_H)
if mibBuilder.loadTexts:rcUplinkPort.setStatus('deprecated')
_RcRateLimitPortTable_Object=MibTable
rcRateLimitPortTable=_RcRateLimitPortTable_Object((1,3,6,1,4,1,8886,6,1,2,2))
if mibBuilder.loadTexts:rcRateLimitPortTable.setStatus(_A)
_RcRateLimitPortEntry_Object=MibTableRow
rcRateLimitPortEntry=_RcRateLimitPortEntry_Object((1,3,6,1,4,1,8886,6,1,2,2,1))
rcRateLimitPortEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:rcRateLimitPortEntry.setStatus(_A)
_RcRateLimitPortIndex_Type=Integer32
_RcRateLimitPortIndex_Object=MibTableColumn
rcRateLimitPortIndex=_RcRateLimitPortIndex_Object((1,3,6,1,4,1,8886,6,1,2,2,1,1),_RcRateLimitPortIndex_Type())
rcRateLimitPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rcRateLimitPortIndex.setStatus(_A)
class _RcRateLimitPortRule_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('ingress',1),('egress',2),('both',3)))
_RcRateLimitPortRule_Type.__name__=_B
_RcRateLimitPortRule_Object=MibTableColumn
rcRateLimitPortRule=_RcRateLimitPortRule_Object((1,3,6,1,4,1,8886,6,1,2,2,1,2),_RcRateLimitPortRule_Type())
rcRateLimitPortRule.setMaxAccess(_C)
if mibBuilder.loadTexts:rcRateLimitPortRule.setStatus('obsolete')
class _RcRateLimitPortIngressRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048576))
_RcRateLimitPortIngressRate_Type.__name__=_B
_RcRateLimitPortIngressRate_Object=MibTableColumn
rcRateLimitPortIngressRate=_RcRateLimitPortIngressRate_Object((1,3,6,1,4,1,8886,6,1,2,2,1,3),_RcRateLimitPortIngressRate_Type())
rcRateLimitPortIngressRate.setMaxAccess(_C)
if mibBuilder.loadTexts:rcRateLimitPortIngressRate.setStatus(_A)
if mibBuilder.loadTexts:rcRateLimitPortIngressRate.setUnits(_F)
class _RcRateLimitPortIngressBurst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512))
_RcRateLimitPortIngressBurst_Type.__name__=_B
_RcRateLimitPortIngressBurst_Object=MibTableColumn
rcRateLimitPortIngressBurst=_RcRateLimitPortIngressBurst_Object((1,3,6,1,4,1,8886,6,1,2,2,1,4),_RcRateLimitPortIngressBurst_Type())
rcRateLimitPortIngressBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:rcRateLimitPortIngressBurst.setStatus(_A)
if mibBuilder.loadTexts:rcRateLimitPortIngressBurst.setUnits('kB')
class _RcRateLimitPortEgressRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048576))
_RcRateLimitPortEgressRate_Type.__name__=_B
_RcRateLimitPortEgressRate_Object=MibTableColumn
rcRateLimitPortEgressRate=_RcRateLimitPortEgressRate_Object((1,3,6,1,4,1,8886,6,1,2,2,1,5),_RcRateLimitPortEgressRate_Type())
rcRateLimitPortEgressRate.setMaxAccess(_C)
if mibBuilder.loadTexts:rcRateLimitPortEgressRate.setStatus(_A)
if mibBuilder.loadTexts:rcRateLimitPortEgressRate.setUnits(_F)
class _RcRateLimitPortEgressBurst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512))
_RcRateLimitPortEgressBurst_Type.__name__=_B
_RcRateLimitPortEgressBurst_Object=MibTableColumn
rcRateLimitPortEgressBurst=_RcRateLimitPortEgressBurst_Object((1,3,6,1,4,1,8886,6,1,2,2,1,6),_RcRateLimitPortEgressBurst_Type())
rcRateLimitPortEgressBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:rcRateLimitPortEgressBurst.setStatus(_A)
if mibBuilder.loadTexts:rcRateLimitPortEgressBurst.setUnits('kB')
_RcRateLimitVlanTable_Object=MibTable
rcRateLimitVlanTable=_RcRateLimitVlanTable_Object((1,3,6,1,4,1,8886,6,1,2,3))
if mibBuilder.loadTexts:rcRateLimitVlanTable.setStatus(_A)
_RcRateLimitVlanEntry_Object=MibTableRow
rcRateLimitVlanEntry=_RcRateLimitVlanEntry_Object((1,3,6,1,4,1,8886,6,1,2,3,1))
rcRateLimitVlanEntry.setIndexNames((0,_D,_J),(0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:rcRateLimitVlanEntry.setStatus(_A)
class _RcRateLimitVlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('single',1),('double',2)))
_RcRateLimitVlanType_Type.__name__=_B
_RcRateLimitVlanType_Object=MibTableColumn
rcRateLimitVlanType=_RcRateLimitVlanType_Object((1,3,6,1,4,1,8886,6,1,2,3,1,1),_RcRateLimitVlanType_Type())
rcRateLimitVlanType.setMaxAccess(_G)
if mibBuilder.loadTexts:rcRateLimitVlanType.setStatus(_A)
class _RcRateLimitVlanCVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcRateLimitVlanCVlanID_Type.__name__=_B
_RcRateLimitVlanCVlanID_Object=MibTableColumn
rcRateLimitVlanCVlanID=_RcRateLimitVlanCVlanID_Object((1,3,6,1,4,1,8886,6,1,2,3,1,2),_RcRateLimitVlanCVlanID_Type())
rcRateLimitVlanCVlanID.setMaxAccess(_G)
if mibBuilder.loadTexts:rcRateLimitVlanCVlanID.setStatus(_A)
class _RcRateLimitVlanSPVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcRateLimitVlanSPVlanID_Type.__name__=_B
_RcRateLimitVlanSPVlanID_Object=MibTableColumn
rcRateLimitVlanSPVlanID=_RcRateLimitVlanSPVlanID_Object((1,3,6,1,4,1,8886,6,1,2,3,1,3),_RcRateLimitVlanSPVlanID_Type())
rcRateLimitVlanSPVlanID.setMaxAccess(_G)
if mibBuilder.loadTexts:rcRateLimitVlanSPVlanID.setStatus(_A)
class _RcRateLimitVlanRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048576))
_RcRateLimitVlanRate_Type.__name__=_B
_RcRateLimitVlanRate_Object=MibTableColumn
rcRateLimitVlanRate=_RcRateLimitVlanRate_Object((1,3,6,1,4,1,8886,6,1,2,3,1,4),_RcRateLimitVlanRate_Type())
rcRateLimitVlanRate.setMaxAccess(_C)
if mibBuilder.loadTexts:rcRateLimitVlanRate.setStatus(_A)
if mibBuilder.loadTexts:rcRateLimitVlanRate.setUnits(_F)
class _RcRateLimitVlanBurst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512))
_RcRateLimitVlanBurst_Type.__name__=_B
_RcRateLimitVlanBurst_Object=MibTableColumn
rcRateLimitVlanBurst=_RcRateLimitVlanBurst_Object((1,3,6,1,4,1,8886,6,1,2,3,1,5),_RcRateLimitVlanBurst_Type())
rcRateLimitVlanBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:rcRateLimitVlanBurst.setStatus(_A)
if mibBuilder.loadTexts:rcRateLimitVlanBurst.setUnits('kB')
_RcRateLimitVlanRowStatus_Type=RowStatus
_RcRateLimitVlanRowStatus_Object=MibTableColumn
rcRateLimitVlanRowStatus=_RcRateLimitVlanRowStatus_Object((1,3,6,1,4,1,8886,6,1,2,3,1,6),_RcRateLimitVlanRowStatus_Type())
rcRateLimitVlanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcRateLimitVlanRowStatus.setStatus(_A)
_RcRateLimitVlanStatsEnable_Type=EnableVar
_RcRateLimitVlanStatsEnable_Object=MibTableColumn
rcRateLimitVlanStatsEnable=_RcRateLimitVlanStatsEnable_Object((1,3,6,1,4,1,8886,6,1,2,3,1,7),_RcRateLimitVlanStatsEnable_Type())
rcRateLimitVlanStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcRateLimitVlanStatsEnable.setStatus(_A)
_RcRateLimitVlanStatHwStatus_Type=EnableVar
_RcRateLimitVlanStatHwStatus_Object=MibTableColumn
rcRateLimitVlanStatHwStatus=_RcRateLimitVlanStatHwStatus_Object((1,3,6,1,4,1,8886,6,1,2,3,1,8),_RcRateLimitVlanStatHwStatus_Type())
rcRateLimitVlanStatHwStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcRateLimitVlanStatHwStatus.setStatus(_A)
_RcRateLimitVlanStatisticsTable_Object=MibTable
rcRateLimitVlanStatisticsTable=_RcRateLimitVlanStatisticsTable_Object((1,3,6,1,4,1,8886,6,1,2,4))
if mibBuilder.loadTexts:rcRateLimitVlanStatisticsTable.setStatus(_A)
_RcRateLimitVlanStatisticsEntry_Object=MibTableRow
rcRateLimitVlanStatisticsEntry=_RcRateLimitVlanStatisticsEntry_Object((1,3,6,1,4,1,8886,6,1,2,4,1))
if mibBuilder.loadTexts:rcRateLimitVlanStatisticsEntry.setStatus(_A)
_RcRateLimitVlanCounterReset_Type=EnableVar
_RcRateLimitVlanCounterReset_Object=MibTableColumn
rcRateLimitVlanCounterReset=_RcRateLimitVlanCounterReset_Object((1,3,6,1,4,1,8886,6,1,2,4,1,1),_RcRateLimitVlanCounterReset_Type())
rcRateLimitVlanCounterReset.setMaxAccess(_H)
if mibBuilder.loadTexts:rcRateLimitVlanCounterReset.setStatus(_A)
_RcRateLimitVlanCounterInprofilePkt64_Type=Counter64
_RcRateLimitVlanCounterInprofilePkt64_Object=MibTableColumn
rcRateLimitVlanCounterInprofilePkt64=_RcRateLimitVlanCounterInprofilePkt64_Object((1,3,6,1,4,1,8886,6,1,2,4,1,2),_RcRateLimitVlanCounterInprofilePkt64_Type())
rcRateLimitVlanCounterInprofilePkt64.setMaxAccess(_E)
if mibBuilder.loadTexts:rcRateLimitVlanCounterInprofilePkt64.setStatus(_A)
_RcRateLimitVlanCounterInprofileByte64_Type=Counter64
_RcRateLimitVlanCounterInprofileByte64_Object=MibTableColumn
rcRateLimitVlanCounterInprofileByte64=_RcRateLimitVlanCounterInprofileByte64_Object((1,3,6,1,4,1,8886,6,1,2,4,1,3),_RcRateLimitVlanCounterInprofileByte64_Type())
rcRateLimitVlanCounterInprofileByte64.setMaxAccess(_E)
if mibBuilder.loadTexts:rcRateLimitVlanCounterInprofileByte64.setStatus(_A)
_RcRateLimitVlanCounterOutprofilePkt64_Type=Counter64
_RcRateLimitVlanCounterOutprofilePkt64_Object=MibTableColumn
rcRateLimitVlanCounterOutprofilePkt64=_RcRateLimitVlanCounterOutprofilePkt64_Object((1,3,6,1,4,1,8886,6,1,2,4,1,4),_RcRateLimitVlanCounterOutprofilePkt64_Type())
rcRateLimitVlanCounterOutprofilePkt64.setMaxAccess(_E)
if mibBuilder.loadTexts:rcRateLimitVlanCounterOutprofilePkt64.setStatus(_A)
_RcRateLimitVlanCounterOutprofileByte64_Type=Counter64
_RcRateLimitVlanCounterOutprofileByte64_Object=MibTableColumn
rcRateLimitVlanCounterOutprofileByte64=_RcRateLimitVlanCounterOutprofileByte64_Object((1,3,6,1,4,1,8886,6,1,2,4,1,5),_RcRateLimitVlanCounterOutprofileByte64_Type())
rcRateLimitVlanCounterOutprofileByte64.setMaxAccess(_E)
if mibBuilder.loadTexts:rcRateLimitVlanCounterOutprofileByte64.setStatus(_A)
_RcRateLimitVlanCounterStatisticUnit_Type=Integer32
_RcRateLimitVlanCounterStatisticUnit_Object=MibTableColumn
rcRateLimitVlanCounterStatisticUnit=_RcRateLimitVlanCounterStatisticUnit_Object((1,3,6,1,4,1,8886,6,1,2,4,1,6),_RcRateLimitVlanCounterStatisticUnit_Type())
rcRateLimitVlanCounterStatisticUnit.setMaxAccess(_E)
if mibBuilder.loadTexts:rcRateLimitVlanCounterStatisticUnit.setStatus(_A)
rcRateLimitVlanEntry.registerAugmentions((_D,_M))
rcRateLimitVlanStatisticsEntry.setIndexNames(*rcRateLimitVlanEntry.getIndexNames())
mibBuilder.exportSymbols(_D,**{'rcRateLimit':rcRateLimit,'rcUplinkPort':rcUplinkPort,'rcRateLimitPortTable':rcRateLimitPortTable,'rcRateLimitPortEntry':rcRateLimitPortEntry,_I:rcRateLimitPortIndex,'rcRateLimitPortRule':rcRateLimitPortRule,'rcRateLimitPortIngressRate':rcRateLimitPortIngressRate,'rcRateLimitPortIngressBurst':rcRateLimitPortIngressBurst,'rcRateLimitPortEgressRate':rcRateLimitPortEgressRate,'rcRateLimitPortEgressBurst':rcRateLimitPortEgressBurst,'rcRateLimitVlanTable':rcRateLimitVlanTable,'rcRateLimitVlanEntry':rcRateLimitVlanEntry,_J:rcRateLimitVlanType,_K:rcRateLimitVlanCVlanID,_L:rcRateLimitVlanSPVlanID,'rcRateLimitVlanRate':rcRateLimitVlanRate,'rcRateLimitVlanBurst':rcRateLimitVlanBurst,'rcRateLimitVlanRowStatus':rcRateLimitVlanRowStatus,'rcRateLimitVlanStatsEnable':rcRateLimitVlanStatsEnable,'rcRateLimitVlanStatHwStatus':rcRateLimitVlanStatHwStatus,'rcRateLimitVlanStatisticsTable':rcRateLimitVlanStatisticsTable,_M:rcRateLimitVlanStatisticsEntry,'rcRateLimitVlanCounterReset':rcRateLimitVlanCounterReset,'rcRateLimitVlanCounterInprofilePkt64':rcRateLimitVlanCounterInprofilePkt64,'rcRateLimitVlanCounterInprofileByte64':rcRateLimitVlanCounterInprofileByte64,'rcRateLimitVlanCounterOutprofilePkt64':rcRateLimitVlanCounterOutprofilePkt64,'rcRateLimitVlanCounterOutprofileByte64':rcRateLimitVlanCounterOutprofileByte64,'rcRateLimitVlanCounterStatisticUnit':rcRateLimitVlanCounterStatisticUnit})