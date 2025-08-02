_F='cfgCommonHmsSnmpAccessIndex'
_E='ELECTROLINE-COMMON-CONFIG-MIB'
_D='OctetString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
commonConfiguration,=mibBuilder.importSymbols('ELECTROLINE-COMMON-ROOT-MIB','commonConfiguration')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
_CfgTimers_ObjectIdentity=ObjectIdentity
cfgTimers=_CfgTimers_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,4,2,1))
if mibBuilder.loadTexts:cfgTimers.setStatus(_A)
class _CfgCommonSnmpTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10080))
_CfgCommonSnmpTimeout_Type.__name__=_C
_CfgCommonSnmpTimeout_Object=MibScalar
cfgCommonSnmpTimeout=_CfgCommonSnmpTimeout_Object((1,3,6,1,4,1,5802,1,3,1,4,2,1,1),_CfgCommonSnmpTimeout_Type())
cfgCommonSnmpTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgCommonSnmpTimeout.setStatus(_A)
_CfgIpInterfaces_ObjectIdentity=ObjectIdentity
cfgIpInterfaces=_CfgIpInterfaces_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,4,2,2))
if mibBuilder.loadTexts:cfgIpInterfaces.setStatus(_A)
class _CfgIpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('singleIp',1),('dualIp',2)))
_CfgIpMode_Type.__name__=_C
_CfgIpMode_Object=MibScalar
cfgIpMode=_CfgIpMode_Object((1,3,6,1,4,1,5802,1,3,1,4,2,2,1),_CfgIpMode_Type())
cfgIpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgIpMode.setStatus(_A)
_CfgCommonHmsSnmpAgent_ObjectIdentity=ObjectIdentity
cfgCommonHmsSnmpAgent=_CfgCommonHmsSnmpAgent_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,4,2,2,50))
if mibBuilder.loadTexts:cfgCommonHmsSnmpAgent.setStatus(_A)
_CfgCommonHmsSnmpManagerCommunity_Type=DisplayString
_CfgCommonHmsSnmpManagerCommunity_Object=MibScalar
cfgCommonHmsSnmpManagerCommunity=_CfgCommonHmsSnmpManagerCommunity_Object((1,3,6,1,4,1,5802,1,3,1,4,2,2,50,1),_CfgCommonHmsSnmpManagerCommunity_Type())
cfgCommonHmsSnmpManagerCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgCommonHmsSnmpManagerCommunity.setStatus(_A)
_CfgCommonHmsSnmpMonitorCommunity_Type=DisplayString
_CfgCommonHmsSnmpMonitorCommunity_Object=MibScalar
cfgCommonHmsSnmpMonitorCommunity=_CfgCommonHmsSnmpMonitorCommunity_Object((1,3,6,1,4,1,5802,1,3,1,4,2,2,50,2),_CfgCommonHmsSnmpMonitorCommunity_Type())
cfgCommonHmsSnmpMonitorCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgCommonHmsSnmpMonitorCommunity.setStatus(_A)
_CfgCommonHmsSnmpAccess_ObjectIdentity=ObjectIdentity
cfgCommonHmsSnmpAccess=_CfgCommonHmsSnmpAccess_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,4,2,2,50,3))
if mibBuilder.loadTexts:cfgCommonHmsSnmpAccess.setStatus(_A)
_CfgCommonHmsSnmpAccessTable_Object=MibTable
cfgCommonHmsSnmpAccessTable=_CfgCommonHmsSnmpAccessTable_Object((1,3,6,1,4,1,5802,1,3,1,4,2,2,50,3,1))
if mibBuilder.loadTexts:cfgCommonHmsSnmpAccessTable.setStatus(_A)
_CfgCommonHmsSnmpAccessEntry_Object=MibTableRow
cfgCommonHmsSnmpAccessEntry=_CfgCommonHmsSnmpAccessEntry_Object((1,3,6,1,4,1,5802,1,3,1,4,2,2,50,3,1,1))
cfgCommonHmsSnmpAccessEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cfgCommonHmsSnmpAccessEntry.setStatus(_A)
_CfgCommonHmsSnmpAccessIndex_Type=Integer32
_CfgCommonHmsSnmpAccessIndex_Object=MibTableColumn
cfgCommonHmsSnmpAccessIndex=_CfgCommonHmsSnmpAccessIndex_Object((1,3,6,1,4,1,5802,1,3,1,4,2,2,50,3,1,1,1),_CfgCommonHmsSnmpAccessIndex_Type())
cfgCommonHmsSnmpAccessIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:cfgCommonHmsSnmpAccessIndex.setStatus(_A)
_CfgCommonHmsSnmpAccessIP_Type=IpAddress
_CfgCommonHmsSnmpAccessIP_Object=MibTableColumn
cfgCommonHmsSnmpAccessIP=_CfgCommonHmsSnmpAccessIP_Object((1,3,6,1,4,1,5802,1,3,1,4,2,2,50,3,1,1,2),_CfgCommonHmsSnmpAccessIP_Type())
cfgCommonHmsSnmpAccessIP.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgCommonHmsSnmpAccessIP.setStatus(_A)
_CfgCommonHmsSnmpAccessIPMask_Type=IpAddress
_CfgCommonHmsSnmpAccessIPMask_Object=MibTableColumn
cfgCommonHmsSnmpAccessIPMask=_CfgCommonHmsSnmpAccessIPMask_Object((1,3,6,1,4,1,5802,1,3,1,4,2,2,50,3,1,1,3),_CfgCommonHmsSnmpAccessIPMask_Type())
cfgCommonHmsSnmpAccessIPMask.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgCommonHmsSnmpAccessIPMask.setStatus(_A)
class _CfgVendorInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CfgVendorInfo_Type.__name__=_D
_CfgVendorInfo_Object=MibScalar
cfgVendorInfo=_CfgVendorInfo_Object((1,3,6,1,4,1,5802,1,3,1,4,2,3),_CfgVendorInfo_Type())
cfgVendorInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgVendorInfo.setStatus(_A)
class _CfgHmsTimeReference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('utc',2)))
_CfgHmsTimeReference_Type.__name__=_C
_CfgHmsTimeReference_Object=MibScalar
cfgHmsTimeReference=_CfgHmsTimeReference_Object((1,3,6,1,4,1,5802,1,3,1,4,2,4),_CfgHmsTimeReference_Type())
cfgHmsTimeReference.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgHmsTimeReference.setStatus(_A)
class _CfgResetToFactory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_CfgResetToFactory_Type.__name__=_C
_CfgResetToFactory_Object=MibScalar
cfgResetToFactory=_CfgResetToFactory_Object((1,3,6,1,4,1,5802,1,3,1,4,2,5),_CfgResetToFactory_Type())
cfgResetToFactory.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgResetToFactory.setStatus(_A)
class _CfgLocalInterfaceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('disable',0),('cpe',1),('craft',2)))
_CfgLocalInterfaceMode_Type.__name__=_C
_CfgLocalInterfaceMode_Object=MibScalar
cfgLocalInterfaceMode=_CfgLocalInterfaceMode_Object((1,3,6,1,4,1,5802,1,3,1,4,2,6),_CfgLocalInterfaceMode_Type())
cfgLocalInterfaceMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgLocalInterfaceMode.setStatus(_A)
_CfgChannelBondingEnable_Type=TruthValue
_CfgChannelBondingEnable_Object=MibScalar
cfgChannelBondingEnable=_CfgChannelBondingEnable_Object((1,3,6,1,4,1,5802,1,3,1,4,2,7),_CfgChannelBondingEnable_Type())
cfgChannelBondingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgChannelBondingEnable.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'cfgTimers':cfgTimers,'cfgCommonSnmpTimeout':cfgCommonSnmpTimeout,'cfgIpInterfaces':cfgIpInterfaces,'cfgIpMode':cfgIpMode,'cfgCommonHmsSnmpAgent':cfgCommonHmsSnmpAgent,'cfgCommonHmsSnmpManagerCommunity':cfgCommonHmsSnmpManagerCommunity,'cfgCommonHmsSnmpMonitorCommunity':cfgCommonHmsSnmpMonitorCommunity,'cfgCommonHmsSnmpAccess':cfgCommonHmsSnmpAccess,'cfgCommonHmsSnmpAccessTable':cfgCommonHmsSnmpAccessTable,'cfgCommonHmsSnmpAccessEntry':cfgCommonHmsSnmpAccessEntry,_F:cfgCommonHmsSnmpAccessIndex,'cfgCommonHmsSnmpAccessIP':cfgCommonHmsSnmpAccessIP,'cfgCommonHmsSnmpAccessIPMask':cfgCommonHmsSnmpAccessIPMask,'cfgVendorInfo':cfgVendorInfo,'cfgHmsTimeReference':cfgHmsTimeReference,'cfgResetToFactory':cfgResetToFactory,'cfgLocalInterfaceMode':cfgLocalInterfaceMode,'cfgChannelBondingEnable':cfgChannelBondingEnable})