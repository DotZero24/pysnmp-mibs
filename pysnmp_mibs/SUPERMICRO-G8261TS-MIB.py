_F='fsG8261TsDirection'
_E='SUPERMICRO-G8261TS-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsG8261Ts=ModuleIdentity((1,3,6,1,4,1,10876,101,2,72))
if mibBuilder.loadTexts:fsG8261Ts.setRevisions(('2012-09-05 00:00',))
_FsG8261TsSystem_ObjectIdentity=ObjectIdentity
fsG8261TsSystem=_FsG8261TsSystem_ObjectIdentity((1,3,6,1,4,1,10876,101,2,72,1))
class _FsG8261TsModuleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_FsG8261TsModuleStatus_Type.__name__=_C
_FsG8261TsModuleStatus_Object=MibScalar
fsG8261TsModuleStatus=_FsG8261TsModuleStatus_Object((1,3,6,1,4,1,10876,101,2,72,1,1),_FsG8261TsModuleStatus_Type())
fsG8261TsModuleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsG8261TsModuleStatus.setStatus(_A)
_FsG8261TsParams_ObjectIdentity=ObjectIdentity
fsG8261TsParams=_FsG8261TsParams_ObjectIdentity((1,3,6,1,4,1,10876,101,2,72,2))
_FsG8261TsParamsTable_Object=MibTable
fsG8261TsParamsTable=_FsG8261TsParamsTable_Object((1,3,6,1,4,1,10876,101,2,72,2,1))
if mibBuilder.loadTexts:fsG8261TsParamsTable.setStatus(_A)
_FsG8261TsParamsEntry_Object=MibTableRow
fsG8261TsParamsEntry=_FsG8261TsParamsEntry_Object((1,3,6,1,4,1,10876,101,2,72,2,1,1))
fsG8261TsParamsEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:fsG8261TsParamsEntry.setStatus(_A)
class _FsG8261TsDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forward',1),('reverse',2)))
_FsG8261TsDirection_Type.__name__=_C
_FsG8261TsDirection_Object=MibTableColumn
fsG8261TsDirection=_FsG8261TsDirection_Object((1,3,6,1,4,1,10876,101,2,72,2,1,1,1),_FsG8261TsDirection_Type())
fsG8261TsDirection.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fsG8261TsDirection.setStatus(_A)
_FsG8261TsSwitchCount_Type=Unsigned32
_FsG8261TsSwitchCount_Object=MibTableColumn
fsG8261TsSwitchCount=_FsG8261TsSwitchCount_Object((1,3,6,1,4,1,10876,101,2,72,2,1,1,2),_FsG8261TsSwitchCount_Type())
fsG8261TsSwitchCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsG8261TsSwitchCount.setStatus(_A)
_FsG8261TsPacketSize_Type=Unsigned32
_FsG8261TsPacketSize_Object=MibTableColumn
fsG8261TsPacketSize=_FsG8261TsPacketSize_Object((1,3,6,1,4,1,10876,101,2,72,2,1,1,3),_FsG8261TsPacketSize_Type())
fsG8261TsPacketSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fsG8261TsPacketSize.setStatus(_A)
_FsG8261TsLoad_Type=Unsigned32
_FsG8261TsLoad_Object=MibTableColumn
fsG8261TsLoad=_FsG8261TsLoad_Object((1,3,6,1,4,1,10876,101,2,72,2,1,1,4),_FsG8261TsLoad_Type())
fsG8261TsLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:fsG8261TsLoad.setStatus(_A)
_FsG8261TsNetworkDisturbance_Type=Unsigned32
_FsG8261TsNetworkDisturbance_Object=MibTableColumn
fsG8261TsNetworkDisturbance=_FsG8261TsNetworkDisturbance_Object((1,3,6,1,4,1,10876,101,2,72,2,1,1,5),_FsG8261TsNetworkDisturbance_Type())
fsG8261TsNetworkDisturbance.setMaxAccess(_B)
if mibBuilder.loadTexts:fsG8261TsNetworkDisturbance.setStatus(_A)
_FsG8261TsDuration_Type=Unsigned32
_FsG8261TsDuration_Object=MibTableColumn
fsG8261TsDuration=_FsG8261TsDuration_Object((1,3,6,1,4,1,10876,101,2,72,2,1,1,6),_FsG8261TsDuration_Type())
fsG8261TsDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:fsG8261TsDuration.setStatus(_A)
class _FsG8261TsFlowVariationFactor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('constant',1),('incremental',2),('decremental',3)))
_FsG8261TsFlowVariationFactor_Type.__name__=_C
_FsG8261TsFlowVariationFactor_Object=MibTableColumn
fsG8261TsFlowVariationFactor=_FsG8261TsFlowVariationFactor_Object((1,3,6,1,4,1,10876,101,2,72,2,1,1,7),_FsG8261TsFlowVariationFactor_Type())
fsG8261TsFlowVariationFactor.setMaxAccess(_B)
if mibBuilder.loadTexts:fsG8261TsFlowVariationFactor.setStatus(_A)
_FsG8261TsFlowInterval_Type=Unsigned32
_FsG8261TsFlowInterval_Object=MibTableColumn
fsG8261TsFlowInterval=_FsG8261TsFlowInterval_Object((1,3,6,1,4,1,10876,101,2,72,2,1,1,8),_FsG8261TsFlowInterval_Type())
fsG8261TsFlowInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fsG8261TsFlowInterval.setStatus(_A)
_FsG8261TsFrequency_Type=Unsigned32
_FsG8261TsFrequency_Object=MibTableColumn
fsG8261TsFrequency=_FsG8261TsFrequency_Object((1,3,6,1,4,1,10876,101,2,72,2,1,1,9),_FsG8261TsFrequency_Type())
fsG8261TsFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:fsG8261TsFrequency.setStatus(_A)
_FsG8261TsOutput_ObjectIdentity=ObjectIdentity
fsG8261TsOutput=_FsG8261TsOutput_ObjectIdentity((1,3,6,1,4,1,10876,101,2,72,3))
_FsG8261TsMeanVariance_Type=DisplayString
_FsG8261TsMeanVariance_Object=MibScalar
fsG8261TsMeanVariance=_FsG8261TsMeanVariance_Object((1,3,6,1,4,1,10876,101,2,72,3,1),_FsG8261TsMeanVariance_Type())
fsG8261TsMeanVariance.setMaxAccess(_D)
if mibBuilder.loadTexts:fsG8261TsMeanVariance.setStatus(_A)
_FsG8261TsAccuracy_Type=Integer32
_FsG8261TsAccuracy_Object=MibScalar
fsG8261TsAccuracy=_FsG8261TsAccuracy_Object((1,3,6,1,4,1,10876,101,2,72,3,2),_FsG8261TsAccuracy_Type())
fsG8261TsAccuracy.setMaxAccess(_D)
if mibBuilder.loadTexts:fsG8261TsAccuracy.setStatus(_A)
_FsG8261TsDelay_Type=DisplayString
_FsG8261TsDelay_Object=MibScalar
fsG8261TsDelay=_FsG8261TsDelay_Object((1,3,6,1,4,1,10876,101,2,72,3,3),_FsG8261TsDelay_Type())
fsG8261TsDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:fsG8261TsDelay.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'fsG8261Ts':fsG8261Ts,'fsG8261TsSystem':fsG8261TsSystem,'fsG8261TsModuleStatus':fsG8261TsModuleStatus,'fsG8261TsParams':fsG8261TsParams,'fsG8261TsParamsTable':fsG8261TsParamsTable,'fsG8261TsParamsEntry':fsG8261TsParamsEntry,_F:fsG8261TsDirection,'fsG8261TsSwitchCount':fsG8261TsSwitchCount,'fsG8261TsPacketSize':fsG8261TsPacketSize,'fsG8261TsLoad':fsG8261TsLoad,'fsG8261TsNetworkDisturbance':fsG8261TsNetworkDisturbance,'fsG8261TsDuration':fsG8261TsDuration,'fsG8261TsFlowVariationFactor':fsG8261TsFlowVariationFactor,'fsG8261TsFlowInterval':fsG8261TsFlowInterval,'fsG8261TsFrequency':fsG8261TsFrequency,'fsG8261TsOutput':fsG8261TsOutput,'fsG8261TsMeanVariance':fsG8261TsMeanVariance,'fsG8261TsAccuracy':fsG8261TsAccuracy,'fsG8261TsDelay':fsG8261TsDelay})