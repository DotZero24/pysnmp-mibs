_M='zxAnMacPoolIndex'
_L='zxAnMacForwardingAddr'
_K='zxAnMacForwardingVlanId'
_J='zxAnMacForwardingIfIndex'
_I='zxAnMacForwardingAddrType'
_H='read-write'
_G='read-create'
_F='percent'
_E='not-accessible'
_D='ZTE-AN-MAC-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
ZxAnIfindex,zxAn=mibBuilder.importSymbols('ZTE-AN-TC-MIB','ZxAnIfindex','zxAn')
zxAnMacMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,6))
_ZxAnMacObjects_ObjectIdentity=ObjectIdentity
zxAnMacObjects=_ZxAnMacObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,6,1))
_ZxAnMacGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnMacGlobalObjects=_ZxAnMacGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,6,1,1))
_ZxAnMacTableCapacity_Type=Integer32
_ZxAnMacTableCapacity_Object=MibScalar
zxAnMacTableCapacity=_ZxAnMacTableCapacity_Object((1,3,6,1,4,1,3902,1015,6,1,1,1),_ZxAnMacTableCapacity_Type())
zxAnMacTableCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnMacTableCapacity.setStatus(_A)
_ZxAnMacTableCurrUtilization_Type=Integer32
_ZxAnMacTableCurrUtilization_Object=MibScalar
zxAnMacTableCurrUtilization=_ZxAnMacTableCurrUtilization_Object((1,3,6,1,4,1,3902,1015,6,1,1,2),_ZxAnMacTableCurrUtilization_Type())
zxAnMacTableCurrUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnMacTableCurrUtilization.setStatus(_A)
if mibBuilder.loadTexts:zxAnMacTableCurrUtilization.setUnits(_F)
class _ZxAnMacTableUtilizationThreshold_Type(Integer32):defaultValue=70
_ZxAnMacTableUtilizationThreshold_Type.__name__=_C
_ZxAnMacTableUtilizationThreshold_Object=MibScalar
zxAnMacTableUtilizationThreshold=_ZxAnMacTableUtilizationThreshold_Object((1,3,6,1,4,1,3902,1015,6,1,1,3),_ZxAnMacTableUtilizationThreshold_Type())
zxAnMacTableUtilizationThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnMacTableUtilizationThreshold.setStatus(_A)
if mibBuilder.loadTexts:zxAnMacTableUtilizationThreshold.setUnits(_F)
_ZxAnMacTableCurrMaxUtilization_Type=Integer32
_ZxAnMacTableCurrMaxUtilization_Object=MibScalar
zxAnMacTableCurrMaxUtilization=_ZxAnMacTableCurrMaxUtilization_Object((1,3,6,1,4,1,3902,1015,6,1,1,4),_ZxAnMacTableCurrMaxUtilization_Type())
zxAnMacTableCurrMaxUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnMacTableCurrMaxUtilization.setStatus(_A)
if mibBuilder.loadTexts:zxAnMacTableCurrMaxUtilization.setUnits(_F)
_ZxAnMacTableHisMaxUtilization_Type=Integer32
_ZxAnMacTableHisMaxUtilization_Object=MibScalar
zxAnMacTableHisMaxUtilization=_ZxAnMacTableHisMaxUtilization_Object((1,3,6,1,4,1,3902,1015,6,1,1,5),_ZxAnMacTableHisMaxUtilization_Type())
zxAnMacTableHisMaxUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnMacTableHisMaxUtilization.setStatus(_A)
if mibBuilder.loadTexts:zxAnMacTableHisMaxUtilization.setUnits(_F)
class _ZxAnMacTableMonitorInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,1440))
_ZxAnMacTableMonitorInterval_Type.__name__=_C
_ZxAnMacTableMonitorInterval_Object=MibScalar
zxAnMacTableMonitorInterval=_ZxAnMacTableMonitorInterval_Object((1,3,6,1,4,1,3902,1015,6,1,1,6),_ZxAnMacTableMonitorInterval_Type())
zxAnMacTableMonitorInterval.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnMacTableMonitorInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnMacTableMonitorInterval.setUnits('minute')
_ZxAnMacTableMonitorElapsedTime_Type=Integer32
_ZxAnMacTableMonitorElapsedTime_Object=MibScalar
zxAnMacTableMonitorElapsedTime=_ZxAnMacTableMonitorElapsedTime_Object((1,3,6,1,4,1,3902,1015,6,1,1,7),_ZxAnMacTableMonitorElapsedTime_Type())
zxAnMacTableMonitorElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnMacTableMonitorElapsedTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnMacTableMonitorElapsedTime.setUnits('second')
class _ZxAnMacAgingTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000000))
_ZxAnMacAgingTime_Type.__name__=_C
_ZxAnMacAgingTime_Object=MibScalar
zxAnMacAgingTime=_ZxAnMacAgingTime_Object((1,3,6,1,4,1,3902,1015,6,1,1,8),_ZxAnMacAgingTime_Type())
zxAnMacAgingTime.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnMacAgingTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnMacAgingTime.setUnits('seconds')
_ZxAnMacTableCurrTotalMacAddress_Type=Integer32
_ZxAnMacTableCurrTotalMacAddress_Object=MibScalar
zxAnMacTableCurrTotalMacAddress=_ZxAnMacTableCurrTotalMacAddress_Object((1,3,6,1,4,1,3902,1015,6,1,1,9),_ZxAnMacTableCurrTotalMacAddress_Type())
zxAnMacTableCurrTotalMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnMacTableCurrTotalMacAddress.setStatus(_A)
class _ZxAnMacCapabilities_Type(Bits):namedValues=NamedValues(*(('macForwardingTableIndexChanged',0),('supportPermanentMac',1)))
_ZxAnMacCapabilities_Type.__name__='Bits'
_ZxAnMacCapabilities_Object=MibScalar
zxAnMacCapabilities=_ZxAnMacCapabilities_Object((1,3,6,1,4,1,3902,1015,6,1,1,50),_ZxAnMacCapabilities_Type())
zxAnMacCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnMacCapabilities.setStatus(_A)
_ZxAnMacForwardingTable_Object=MibTable
zxAnMacForwardingTable=_ZxAnMacForwardingTable_Object((1,3,6,1,4,1,3902,1015,6,1,3))
if mibBuilder.loadTexts:zxAnMacForwardingTable.setStatus(_A)
_ZxAnMacForwardingEntry_Object=MibTableRow
zxAnMacForwardingEntry=_ZxAnMacForwardingEntry_Object((1,3,6,1,4,1,3902,1015,6,1,3,1))
zxAnMacForwardingEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:zxAnMacForwardingEntry.setStatus(_A)
class _ZxAnMacForwardingAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dynamic',1),('permanent',2),('static',3)))
_ZxAnMacForwardingAddrType_Type.__name__=_C
_ZxAnMacForwardingAddrType_Object=MibTableColumn
zxAnMacForwardingAddrType=_ZxAnMacForwardingAddrType_Object((1,3,6,1,4,1,3902,1015,6,1,3,1,1),_ZxAnMacForwardingAddrType_Type())
zxAnMacForwardingAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnMacForwardingAddrType.setStatus(_A)
_ZxAnMacForwardingIfIndex_Type=ZxAnIfindex
_ZxAnMacForwardingIfIndex_Object=MibTableColumn
zxAnMacForwardingIfIndex=_ZxAnMacForwardingIfIndex_Object((1,3,6,1,4,1,3902,1015,6,1,3,1,2),_ZxAnMacForwardingIfIndex_Type())
zxAnMacForwardingIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnMacForwardingIfIndex.setStatus(_A)
_ZxAnMacForwardingVlanId_Type=Integer32
_ZxAnMacForwardingVlanId_Object=MibTableColumn
zxAnMacForwardingVlanId=_ZxAnMacForwardingVlanId_Object((1,3,6,1,4,1,3902,1015,6,1,3,1,3),_ZxAnMacForwardingVlanId_Type())
zxAnMacForwardingVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnMacForwardingVlanId.setStatus(_A)
_ZxAnMacForwardingAddr_Type=MacAddress
_ZxAnMacForwardingAddr_Object=MibTableColumn
zxAnMacForwardingAddr=_ZxAnMacForwardingAddr_Object((1,3,6,1,4,1,3902,1015,6,1,3,1,4),_ZxAnMacForwardingAddr_Type())
zxAnMacForwardingAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnMacForwardingAddr.setStatus(_A)
_ZxAnMacFwdConfRowStatus_Type=RowStatus
_ZxAnMacFwdConfRowStatus_Object=MibTableColumn
zxAnMacFwdConfRowStatus=_ZxAnMacFwdConfRowStatus_Object((1,3,6,1,4,1,3902,1015,6,1,3,1,5),_ZxAnMacFwdConfRowStatus_Type())
zxAnMacFwdConfRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnMacFwdConfRowStatus.setStatus(_A)
_ZxAnMacPoolTable_Object=MibTable
zxAnMacPoolTable=_ZxAnMacPoolTable_Object((1,3,6,1,4,1,3902,1015,6,1,4))
if mibBuilder.loadTexts:zxAnMacPoolTable.setStatus(_A)
_ZxAnMacPoolEntry_Object=MibTableRow
zxAnMacPoolEntry=_ZxAnMacPoolEntry_Object((1,3,6,1,4,1,3902,1015,6,1,4,1))
zxAnMacPoolEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:zxAnMacPoolEntry.setStatus(_A)
class _ZxAnMacPoolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ZxAnMacPoolIndex_Type.__name__=_C
_ZxAnMacPoolIndex_Object=MibTableColumn
zxAnMacPoolIndex=_ZxAnMacPoolIndex_Object((1,3,6,1,4,1,3902,1015,6,1,4,1,1),_ZxAnMacPoolIndex_Type())
zxAnMacPoolIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnMacPoolIndex.setStatus(_A)
_ZxAnMacPoolStartMac_Type=MacAddress
_ZxAnMacPoolStartMac_Object=MibTableColumn
zxAnMacPoolStartMac=_ZxAnMacPoolStartMac_Object((1,3,6,1,4,1,3902,1015,6,1,4,1,2),_ZxAnMacPoolStartMac_Type())
zxAnMacPoolStartMac.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnMacPoolStartMac.setStatus(_A)
class _ZxAnMacPoolSize_Type(Integer32):defaultValue=256;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_ZxAnMacPoolSize_Type.__name__=_C
_ZxAnMacPoolSize_Object=MibTableColumn
zxAnMacPoolSize=_ZxAnMacPoolSize_Object((1,3,6,1,4,1,3902,1015,6,1,4,1,3),_ZxAnMacPoolSize_Type())
zxAnMacPoolSize.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnMacPoolSize.setStatus(_A)
class _ZxAnMacPoolAvailableSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_ZxAnMacPoolAvailableSize_Type.__name__=_C
_ZxAnMacPoolAvailableSize_Object=MibTableColumn
zxAnMacPoolAvailableSize=_ZxAnMacPoolAvailableSize_Object((1,3,6,1,4,1,3902,1015,6,1,4,1,4),_ZxAnMacPoolAvailableSize_Type())
zxAnMacPoolAvailableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnMacPoolAvailableSize.setStatus(_A)
_ZxAnMacPoolRowStatus_Type=RowStatus
_ZxAnMacPoolRowStatus_Object=MibTableColumn
zxAnMacPoolRowStatus=_ZxAnMacPoolRowStatus_Object((1,3,6,1,4,1,3902,1015,6,1,4,1,5),_ZxAnMacPoolRowStatus_Type())
zxAnMacPoolRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnMacPoolRowStatus.setStatus(_A)
_ZxAnMacTrapObjects_ObjectIdentity=ObjectIdentity
zxAnMacTrapObjects=_ZxAnMacTrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,6,2))
_ZxAnMacPerfObjects_ObjectIdentity=ObjectIdentity
zxAnMacPerfObjects=_ZxAnMacPerfObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,6,3))
_ZxAnMacUsageRateGroupPerf_Type=Counter64
_ZxAnMacUsageRateGroupPerf_Object=MibScalar
zxAnMacUsageRateGroupPerf=_ZxAnMacUsageRateGroupPerf_Object((1,3,6,1,4,1,3902,1015,6,3,1),_ZxAnMacUsageRateGroupPerf_Type())
zxAnMacUsageRateGroupPerf.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnMacUsageRateGroupPerf.setStatus(_A)
_ZxAnMacMaxUsageRatePerf_Type=Counter64
_ZxAnMacMaxUsageRatePerf_Object=MibScalar
zxAnMacMaxUsageRatePerf=_ZxAnMacMaxUsageRatePerf_Object((1,3,6,1,4,1,3902,1015,6,3,2),_ZxAnMacMaxUsageRatePerf_Type())
zxAnMacMaxUsageRatePerf.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnMacMaxUsageRatePerf.setStatus(_A)
_ZxAnMacMinUsageRatePerf_Type=Counter64
_ZxAnMacMinUsageRatePerf_Object=MibScalar
zxAnMacMinUsageRatePerf=_ZxAnMacMinUsageRatePerf_Object((1,3,6,1,4,1,3902,1015,6,3,3),_ZxAnMacMinUsageRatePerf_Type())
zxAnMacMinUsageRatePerf.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnMacMinUsageRatePerf.setStatus(_A)
_ZxAnMacAverageUsageRatePerf_Type=Counter64
_ZxAnMacAverageUsageRatePerf_Object=MibScalar
zxAnMacAverageUsageRatePerf=_ZxAnMacAverageUsageRatePerf_Object((1,3,6,1,4,1,3902,1015,6,3,4),_ZxAnMacAverageUsageRatePerf_Type())
zxAnMacAverageUsageRatePerf.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnMacAverageUsageRatePerf.setStatus(_A)
zxAnMacTableUsageOverThreshTrap=NotificationType((1,3,6,1,4,1,3902,1015,6,2,1))
zxAnMacTableUsageOverThreshTrap.setObjects(*((_D,'zxAnMacTableCurrentUsage'),(_D,'zxAnMacTableUsageThreshold')))
if mibBuilder.loadTexts:zxAnMacTableUsageOverThreshTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zxAnMacMib':zxAnMacMib,'zxAnMacObjects':zxAnMacObjects,'zxAnMacGlobalObjects':zxAnMacGlobalObjects,'zxAnMacTableCapacity':zxAnMacTableCapacity,'zxAnMacTableCurrUtilization':zxAnMacTableCurrUtilization,'zxAnMacTableUtilizationThreshold':zxAnMacTableUtilizationThreshold,'zxAnMacTableCurrMaxUtilization':zxAnMacTableCurrMaxUtilization,'zxAnMacTableHisMaxUtilization':zxAnMacTableHisMaxUtilization,'zxAnMacTableMonitorInterval':zxAnMacTableMonitorInterval,'zxAnMacTableMonitorElapsedTime':zxAnMacTableMonitorElapsedTime,'zxAnMacAgingTime':zxAnMacAgingTime,'zxAnMacTableCurrTotalMacAddress':zxAnMacTableCurrTotalMacAddress,'zxAnMacCapabilities':zxAnMacCapabilities,'zxAnMacForwardingTable':zxAnMacForwardingTable,'zxAnMacForwardingEntry':zxAnMacForwardingEntry,_I:zxAnMacForwardingAddrType,_J:zxAnMacForwardingIfIndex,_K:zxAnMacForwardingVlanId,_L:zxAnMacForwardingAddr,'zxAnMacFwdConfRowStatus':zxAnMacFwdConfRowStatus,'zxAnMacPoolTable':zxAnMacPoolTable,'zxAnMacPoolEntry':zxAnMacPoolEntry,_M:zxAnMacPoolIndex,'zxAnMacPoolStartMac':zxAnMacPoolStartMac,'zxAnMacPoolSize':zxAnMacPoolSize,'zxAnMacPoolAvailableSize':zxAnMacPoolAvailableSize,'zxAnMacPoolRowStatus':zxAnMacPoolRowStatus,'zxAnMacTrapObjects':zxAnMacTrapObjects,'zxAnMacTableUsageOverThreshTrap':zxAnMacTableUsageOverThreshTrap,'zxAnMacPerfObjects':zxAnMacPerfObjects,'zxAnMacUsageRateGroupPerf':zxAnMacUsageRateGroupPerf,'zxAnMacMaxUsageRatePerf':zxAnMacMaxUsageRatePerf,'zxAnMacMinUsageRatePerf':zxAnMacMinUsageRatePerf,'zxAnMacAverageUsageRatePerf':zxAnMacAverageUsageRatePerf})