_c='rlCdpCacheEntry'
_b='rlCdpSecondaryCacheRequestedPowerIndex'
_a='rlCdpSecondaryCacheAddressIndex'
_Z='rlCdpTlvPowerRequestPowerLevelIndex'
_Y='rlCdpInterfaceId'
_X='operationalState'
_W='desiredState'
_V='detectionClassificationRequired'
_U='supported'
_T='RlCdpPduActionTypes'
_S='rlCdpCountersName'
_R='InterfaceIndexOrZero'
_Q='rlCdpTlvIfIndex'
_P='Bits'
_O='OctetString'
_N='rndErrorSeverity'
_M='rndErrorDesc'
_L='cdpCacheIfIndex'
_K='cdpCacheDeviceIndex'
_J='not-accessible'
_I='TruthValue'
_H='Integer32'
_G='NETGEAR-RADLAN-DEVICEPARAMS-MIB'
_F='CISCO-CDP-MIB'
_E='NETGEAR-RADLAN-CDP-MIB'
_D='Unsigned32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cdpCacheDeviceIndex,cdpCacheEntry,cdpCacheIfIndex=mibBuilder.importSymbols(_F,_K,'cdpCacheEntry',_L)
CiscoNetworkAddress,CiscoNetworkProtocol=mibBuilder.importSymbols('CISCO-TC','CiscoNetworkAddress','CiscoNetworkProtocol')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex',_R)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
rndErrorDesc,rndErrorSeverity=mibBuilder.importSymbols(_G,_M,_N)
rnd,rndNotifications=mibBuilder.importSymbols('NETGEAR-RADLAN-MIB','rnd','rndNotifications')
PortList,VlanId=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_P,'Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_I)
rlCdp=ModuleIdentity((1,3,6,1,4,1,4526,17,137))
if mibBuilder.loadTexts:rlCdp.setRevisions(('2008-09-14 00:00','2010-08-11 00:00','2010-10-25 00:00','2010-11-10 00:00','2010-11-14 00:00','2011-01-09 00:00','2011-02-15 00:00','2012-02-14 00:00','2015-03-04 00:00'))
class RlCdpVersionTypes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('version-v1',1),('version-v2',2)))
class RlCdpCounterTypes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('totalInputPackets',1),('v1InputPackets',2),('v2InputPackets',3),('totalOutputPackets',4),('v1OutputPackets',5),('v2OutputPackets',6),('illegalChksum',7),('errorPackets',8),('maxNeighborsExceededInMainCache',9),('maxNeighborsExceededInSecondaryCache',10)))
class RlCdpPduActionTypes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('filtering',1),('bridging',2),('flooding',3)))
_RlCdpVersionAdvertised_Type=RlCdpVersionTypes
_RlCdpVersionAdvertised_Object=MibScalar
rlCdpVersionAdvertised=_RlCdpVersionAdvertised_Object((1,3,6,1,4,1,4526,17,137,1),_RlCdpVersionAdvertised_Type())
rlCdpVersionAdvertised.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCdpVersionAdvertised.setStatus(_A)
class _RlCdpSourceInterface_Type(InterfaceIndexOrZero):defaultValue=0
_RlCdpSourceInterface_Type.__name__=_R
_RlCdpSourceInterface_Object=MibScalar
rlCdpSourceInterface=_RlCdpSourceInterface_Object((1,3,6,1,4,1,4526,17,137,2),_RlCdpSourceInterface_Type())
rlCdpSourceInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCdpSourceInterface.setStatus(_A)
_RlCdpLogMismatchDuplexEnable_Type=PortList
_RlCdpLogMismatchDuplexEnable_Object=MibScalar
rlCdpLogMismatchDuplexEnable=_RlCdpLogMismatchDuplexEnable_Object((1,3,6,1,4,1,4526,17,137,3),_RlCdpLogMismatchDuplexEnable_Type())
rlCdpLogMismatchDuplexEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCdpLogMismatchDuplexEnable.setStatus(_A)
_RlCdpCountersTable_Object=MibTable
rlCdpCountersTable=_RlCdpCountersTable_Object((1,3,6,1,4,1,4526,17,137,4))
if mibBuilder.loadTexts:rlCdpCountersTable.setStatus(_A)
_RlCdpCountersEntry_Object=MibTableRow
rlCdpCountersEntry=_RlCdpCountersEntry_Object((1,3,6,1,4,1,4526,17,137,4,1))
rlCdpCountersEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:rlCdpCountersEntry.setStatus(_A)
_RlCdpCountersName_Type=RlCdpCounterTypes
_RlCdpCountersName_Object=MibTableColumn
rlCdpCountersName=_RlCdpCountersName_Object((1,3,6,1,4,1,4526,17,137,4,1,1),_RlCdpCountersName_Type())
rlCdpCountersName.setMaxAccess(_J)
if mibBuilder.loadTexts:rlCdpCountersName.setStatus(_A)
_RlCdpCountersValue_Type=Counter32
_RlCdpCountersValue_Object=MibTableColumn
rlCdpCountersValue=_RlCdpCountersValue_Object((1,3,6,1,4,1,4526,17,137,4,1,2),_RlCdpCountersValue_Type())
rlCdpCountersValue.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpCountersValue.setStatus(_A)
_RlCdpCountersClear_Type=TruthValue
_RlCdpCountersClear_Object=MibScalar
rlCdpCountersClear=_RlCdpCountersClear_Object((1,3,6,1,4,1,4526,17,137,5),_RlCdpCountersClear_Type())
rlCdpCountersClear.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCdpCountersClear.setStatus(_A)
_RlCdpCacheClear_Type=TruthValue
_RlCdpCacheClear_Object=MibScalar
rlCdpCacheClear=_RlCdpCacheClear_Object((1,3,6,1,4,1,4526,17,137,6),_RlCdpCacheClear_Type())
rlCdpCacheClear.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCdpCacheClear.setStatus(_A)
class _RlCdpVoiceVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_RlCdpVoiceVlanId_Type.__name__=_H
_RlCdpVoiceVlanId_Object=MibScalar
rlCdpVoiceVlanId=_RlCdpVoiceVlanId_Object((1,3,6,1,4,1,4526,17,137,7),_RlCdpVoiceVlanId_Type())
rlCdpVoiceVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCdpVoiceVlanId.setStatus('obsolete')
_RlCdpCacheTable_Object=MibTable
rlCdpCacheTable=_RlCdpCacheTable_Object((1,3,6,1,4,1,4526,17,137,8))
if mibBuilder.loadTexts:rlCdpCacheTable.setStatus(_A)
_RlCdpCacheEntry_Object=MibTableRow
rlCdpCacheEntry=_RlCdpCacheEntry_Object((1,3,6,1,4,1,4526,17,137,8,1))
if mibBuilder.loadTexts:rlCdpCacheEntry.setStatus(_A)
_RlCdpCacheVersionExt_Type=DisplayString
_RlCdpCacheVersionExt_Object=MibTableColumn
rlCdpCacheVersionExt=_RlCdpCacheVersionExt_Object((1,3,6,1,4,1,4526,17,137,8,1,1),_RlCdpCacheVersionExt_Type())
rlCdpCacheVersionExt.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpCacheVersionExt.setStatus(_A)
_RlCdpCacheTimeToLive_Type=Integer32
_RlCdpCacheTimeToLive_Object=MibTableColumn
rlCdpCacheTimeToLive=_RlCdpCacheTimeToLive_Object((1,3,6,1,4,1,4526,17,137,8,1,2),_RlCdpCacheTimeToLive_Type())
rlCdpCacheTimeToLive.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpCacheTimeToLive.setStatus(_A)
_RlCdpCacheCdpVersion_Type=RlCdpVersionTypes
_RlCdpCacheCdpVersion_Object=MibTableColumn
rlCdpCacheCdpVersion=_RlCdpCacheCdpVersion_Object((1,3,6,1,4,1,4526,17,137,8,1,3),_RlCdpCacheCdpVersion_Type())
rlCdpCacheCdpVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpCacheCdpVersion.setStatus(_A)
class _RlCdpPduAction_Type(RlCdpPduActionTypes):defaultValue=2
_RlCdpPduAction_Type.__name__=_T
_RlCdpPduAction_Object=MibScalar
rlCdpPduAction=_RlCdpPduAction_Object((1,3,6,1,4,1,4526,17,137,9),_RlCdpPduAction_Type())
rlCdpPduAction.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCdpPduAction.setStatus(_A)
_RlCdpLogMismatchVoiceVlanEnable_Type=PortList
_RlCdpLogMismatchVoiceVlanEnable_Object=MibScalar
rlCdpLogMismatchVoiceVlanEnable=_RlCdpLogMismatchVoiceVlanEnable_Object((1,3,6,1,4,1,4526,17,137,10),_RlCdpLogMismatchVoiceVlanEnable_Type())
rlCdpLogMismatchVoiceVlanEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCdpLogMismatchVoiceVlanEnable.setStatus(_A)
_RlCdpLogMismatchNativeVlanEnable_Type=PortList
_RlCdpLogMismatchNativeVlanEnable_Object=MibScalar
rlCdpLogMismatchNativeVlanEnable=_RlCdpLogMismatchNativeVlanEnable_Object((1,3,6,1,4,1,4526,17,137,11),_RlCdpLogMismatchNativeVlanEnable_Type())
rlCdpLogMismatchNativeVlanEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCdpLogMismatchNativeVlanEnable.setStatus(_A)
_RlCdpSecondaryCacheTable_Object=MibTable
rlCdpSecondaryCacheTable=_RlCdpSecondaryCacheTable_Object((1,3,6,1,4,1,4526,17,137,12))
if mibBuilder.loadTexts:rlCdpSecondaryCacheTable.setStatus(_A)
_RlCdpSecondaryCacheEntry_Object=MibTableRow
rlCdpSecondaryCacheEntry=_RlCdpSecondaryCacheEntry_Object((1,3,6,1,4,1,4526,17,137,12,1))
rlCdpSecondaryCacheEntry.setIndexNames((0,_F,_L),(0,_F,_K))
if mibBuilder.loadTexts:rlCdpSecondaryCacheEntry.setStatus(_A)
_RlCdpSecondaryCacheMacAddress_Type=MacAddress
_RlCdpSecondaryCacheMacAddress_Object=MibTableColumn
rlCdpSecondaryCacheMacAddress=_RlCdpSecondaryCacheMacAddress_Object((1,3,6,1,4,1,4526,17,137,12,1,3),_RlCdpSecondaryCacheMacAddress_Type())
rlCdpSecondaryCacheMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpSecondaryCacheMacAddress.setStatus(_A)
_RlCdpSecondaryCachePlatform_Type=DisplayString
_RlCdpSecondaryCachePlatform_Object=MibTableColumn
rlCdpSecondaryCachePlatform=_RlCdpSecondaryCachePlatform_Object((1,3,6,1,4,1,4526,17,137,12,1,4),_RlCdpSecondaryCachePlatform_Type())
rlCdpSecondaryCachePlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpSecondaryCachePlatform.setStatus(_A)
class _RlCdpSecondaryCacheCapabilities_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_RlCdpSecondaryCacheCapabilities_Type.__name__=_O
_RlCdpSecondaryCacheCapabilities_Object=MibTableColumn
rlCdpSecondaryCacheCapabilities=_RlCdpSecondaryCacheCapabilities_Object((1,3,6,1,4,1,4526,17,137,12,1,5),_RlCdpSecondaryCacheCapabilities_Type())
rlCdpSecondaryCacheCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpSecondaryCacheCapabilities.setStatus(_A)
class _RlCdpSecondaryCacheVoiceVlanID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_RlCdpSecondaryCacheVoiceVlanID_Type.__name__=_D
_RlCdpSecondaryCacheVoiceVlanID_Object=MibTableColumn
rlCdpSecondaryCacheVoiceVlanID=_RlCdpSecondaryCacheVoiceVlanID_Object((1,3,6,1,4,1,4526,17,137,12,1,6),_RlCdpSecondaryCacheVoiceVlanID_Type())
rlCdpSecondaryCacheVoiceVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpSecondaryCacheVoiceVlanID.setStatus(_A)
_RlCdpSecondaryCacheTimeToLive_Type=Integer32
_RlCdpSecondaryCacheTimeToLive_Object=MibTableColumn
rlCdpSecondaryCacheTimeToLive=_RlCdpSecondaryCacheTimeToLive_Object((1,3,6,1,4,1,4526,17,137,12,1,7),_RlCdpSecondaryCacheTimeToLive_Type())
rlCdpSecondaryCacheTimeToLive.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpSecondaryCacheTimeToLive.setStatus(_A)
_RlCdpSecondaryCachePowerAvailable_Type=Unsigned32
_RlCdpSecondaryCachePowerAvailable_Object=MibTableColumn
rlCdpSecondaryCachePowerAvailable=_RlCdpSecondaryCachePowerAvailable_Object((1,3,6,1,4,1,4526,17,137,12,1,8),_RlCdpSecondaryCachePowerAvailable_Type())
rlCdpSecondaryCachePowerAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpSecondaryCachePowerAvailable.setStatus(_A)
_RlCdpSecondaryCachePowerConsumption_Type=Unsigned32
_RlCdpSecondaryCachePowerConsumption_Object=MibTableColumn
rlCdpSecondaryCachePowerConsumption=_RlCdpSecondaryCachePowerConsumption_Object((1,3,6,1,4,1,4526,17,137,12,1,9),_RlCdpSecondaryCachePowerConsumption_Type())
rlCdpSecondaryCachePowerConsumption.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpSecondaryCachePowerConsumption.setStatus(_A)
class _RlCdpSecondaryCacheSparePairPoECapabilities_Type(Bits):namedValues=NamedValues(*((_U,0),(_V,1),(_W,2),(_X,3)))
_RlCdpSecondaryCacheSparePairPoECapabilities_Type.__name__=_P
_RlCdpSecondaryCacheSparePairPoECapabilities_Object=MibTableColumn
rlCdpSecondaryCacheSparePairPoECapabilities=_RlCdpSecondaryCacheSparePairPoECapabilities_Object((1,3,6,1,4,1,4526,17,137,12,1,10),_RlCdpSecondaryCacheSparePairPoECapabilities_Type())
rlCdpSecondaryCacheSparePairPoECapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpSecondaryCacheSparePairPoECapabilities.setStatus(_A)
_RlCdpSecondaryCacheDeviceId_Type=DisplayString
_RlCdpSecondaryCacheDeviceId_Object=MibTableColumn
rlCdpSecondaryCacheDeviceId=_RlCdpSecondaryCacheDeviceId_Object((1,3,6,1,4,1,4526,17,137,12,1,11),_RlCdpSecondaryCacheDeviceId_Type())
rlCdpSecondaryCacheDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpSecondaryCacheDeviceId.setStatus(_A)
_RlCdpSecondaryCachePortId_Type=DisplayString
_RlCdpSecondaryCachePortId_Object=MibTableColumn
rlCdpSecondaryCachePortId=_RlCdpSecondaryCachePortId_Object((1,3,6,1,4,1,4526,17,137,12,1,12),_RlCdpSecondaryCachePortId_Type())
rlCdpSecondaryCachePortId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpSecondaryCachePortId.setStatus(_A)
class _RlCdpGlobalLogMismatchDuplexEnable_Type(TruthValue):defaultValue=1
_RlCdpGlobalLogMismatchDuplexEnable_Type.__name__=_I
_RlCdpGlobalLogMismatchDuplexEnable_Object=MibScalar
rlCdpGlobalLogMismatchDuplexEnable=_RlCdpGlobalLogMismatchDuplexEnable_Object((1,3,6,1,4,1,4526,17,137,13),_RlCdpGlobalLogMismatchDuplexEnable_Type())
rlCdpGlobalLogMismatchDuplexEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCdpGlobalLogMismatchDuplexEnable.setStatus(_A)
class _RlCdpGlobalLogMismatchVoiceVlanEnable_Type(TruthValue):defaultValue=1
_RlCdpGlobalLogMismatchVoiceVlanEnable_Type.__name__=_I
_RlCdpGlobalLogMismatchVoiceVlanEnable_Object=MibScalar
rlCdpGlobalLogMismatchVoiceVlanEnable=_RlCdpGlobalLogMismatchVoiceVlanEnable_Object((1,3,6,1,4,1,4526,17,137,14),_RlCdpGlobalLogMismatchVoiceVlanEnable_Type())
rlCdpGlobalLogMismatchVoiceVlanEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCdpGlobalLogMismatchVoiceVlanEnable.setStatus(_A)
class _RlCdpGlobalLogMismatchNativeVlanEnable_Type(TruthValue):defaultValue=1
_RlCdpGlobalLogMismatchNativeVlanEnable_Type.__name__=_I
_RlCdpGlobalLogMismatchNativeVlanEnable_Object=MibScalar
rlCdpGlobalLogMismatchNativeVlanEnable=_RlCdpGlobalLogMismatchNativeVlanEnable_Object((1,3,6,1,4,1,4526,17,137,15),_RlCdpGlobalLogMismatchNativeVlanEnable_Type())
rlCdpGlobalLogMismatchNativeVlanEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCdpGlobalLogMismatchNativeVlanEnable.setStatus(_A)
_RlCdpTlvTable_Object=MibTable
rlCdpTlvTable=_RlCdpTlvTable_Object((1,3,6,1,4,1,4526,17,137,16))
if mibBuilder.loadTexts:rlCdpTlvTable.setStatus(_A)
_RlCdpTlvEntry_Object=MibTableRow
rlCdpTlvEntry=_RlCdpTlvEntry_Object((1,3,6,1,4,1,4526,17,137,16,1))
rlCdpTlvEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:rlCdpTlvEntry.setStatus(_A)
class _RlCdpTlvIfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlCdpTlvIfIndex_Type.__name__=_D
_RlCdpTlvIfIndex_Object=MibTableColumn
rlCdpTlvIfIndex=_RlCdpTlvIfIndex_Object((1,3,6,1,4,1,4526,17,137,16,1,1),_RlCdpTlvIfIndex_Type())
rlCdpTlvIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:rlCdpTlvIfIndex.setStatus(_A)
class _RlCdpTlvDeviceIdFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('serialNumber',1),('macAddress',2),('other',3)))
_RlCdpTlvDeviceIdFormat_Type.__name__=_H
_RlCdpTlvDeviceIdFormat_Object=MibTableColumn
rlCdpTlvDeviceIdFormat=_RlCdpTlvDeviceIdFormat_Object((1,3,6,1,4,1,4526,17,137,16,1,2),_RlCdpTlvDeviceIdFormat_Type())
rlCdpTlvDeviceIdFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvDeviceIdFormat.setStatus(_A)
_RlCdpTlvDeviceId_Type=DisplayString
_RlCdpTlvDeviceId_Object=MibTableColumn
rlCdpTlvDeviceId=_RlCdpTlvDeviceId_Object((1,3,6,1,4,1,4526,17,137,16,1,3),_RlCdpTlvDeviceId_Type())
rlCdpTlvDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvDeviceId.setStatus(_A)
_RlCdpTlvAddress1Type_Type=InetAddressType
_RlCdpTlvAddress1Type_Object=MibTableColumn
rlCdpTlvAddress1Type=_RlCdpTlvAddress1Type_Object((1,3,6,1,4,1,4526,17,137,16,1,4),_RlCdpTlvAddress1Type_Type())
rlCdpTlvAddress1Type.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvAddress1Type.setStatus(_A)
_RlCdpTlvAddress1_Type=InetAddress
_RlCdpTlvAddress1_Object=MibTableColumn
rlCdpTlvAddress1=_RlCdpTlvAddress1_Object((1,3,6,1,4,1,4526,17,137,16,1,5),_RlCdpTlvAddress1_Type())
rlCdpTlvAddress1.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvAddress1.setStatus(_A)
_RlCdpTlvAddress2Type_Type=InetAddressType
_RlCdpTlvAddress2Type_Object=MibTableColumn
rlCdpTlvAddress2Type=_RlCdpTlvAddress2Type_Object((1,3,6,1,4,1,4526,17,137,16,1,6),_RlCdpTlvAddress2Type_Type())
rlCdpTlvAddress2Type.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvAddress2Type.setStatus(_A)
_RlCdpTlvAddress2_Type=InetAddress
_RlCdpTlvAddress2_Object=MibTableColumn
rlCdpTlvAddress2=_RlCdpTlvAddress2_Object((1,3,6,1,4,1,4526,17,137,16,1,7),_RlCdpTlvAddress2_Type())
rlCdpTlvAddress2.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvAddress2.setStatus(_A)
_RlCdpTlvAddress3Type_Type=InetAddressType
_RlCdpTlvAddress3Type_Object=MibTableColumn
rlCdpTlvAddress3Type=_RlCdpTlvAddress3Type_Object((1,3,6,1,4,1,4526,17,137,16,1,8),_RlCdpTlvAddress3Type_Type())
rlCdpTlvAddress3Type.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvAddress3Type.setStatus(_A)
_RlCdpTlvAddress3_Type=InetAddress
_RlCdpTlvAddress3_Object=MibTableColumn
rlCdpTlvAddress3=_RlCdpTlvAddress3_Object((1,3,6,1,4,1,4526,17,137,16,1,9),_RlCdpTlvAddress3_Type())
rlCdpTlvAddress3.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvAddress3.setStatus(_A)
_RlCdpTlvPortId_Type=DisplayString
_RlCdpTlvPortId_Object=MibTableColumn
rlCdpTlvPortId=_RlCdpTlvPortId_Object((1,3,6,1,4,1,4526,17,137,16,1,10),_RlCdpTlvPortId_Type())
rlCdpTlvPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvPortId.setStatus(_A)
class _RlCdpTlvCapabilities_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_RlCdpTlvCapabilities_Type.__name__=_O
_RlCdpTlvCapabilities_Object=MibTableColumn
rlCdpTlvCapabilities=_RlCdpTlvCapabilities_Object((1,3,6,1,4,1,4526,17,137,16,1,11),_RlCdpTlvCapabilities_Type())
rlCdpTlvCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvCapabilities.setStatus(_A)
_RlCdpTlvVersion_Type=DisplayString
_RlCdpTlvVersion_Object=MibTableColumn
rlCdpTlvVersion=_RlCdpTlvVersion_Object((1,3,6,1,4,1,4526,17,137,16,1,12),_RlCdpTlvVersion_Type())
rlCdpTlvVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvVersion.setStatus(_A)
_RlCdpTlvPlatform_Type=DisplayString
_RlCdpTlvPlatform_Object=MibTableColumn
rlCdpTlvPlatform=_RlCdpTlvPlatform_Object((1,3,6,1,4,1,4526,17,137,16,1,13),_RlCdpTlvPlatform_Type())
rlCdpTlvPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvPlatform.setStatus(_A)
class _RlCdpTlvNativeVLAN_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_RlCdpTlvNativeVLAN_Type.__name__=_D
_RlCdpTlvNativeVLAN_Object=MibTableColumn
rlCdpTlvNativeVLAN=_RlCdpTlvNativeVLAN_Object((1,3,6,1,4,1,4526,17,137,16,1,14),_RlCdpTlvNativeVLAN_Type())
rlCdpTlvNativeVLAN.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvNativeVLAN.setStatus(_A)
class _RlCdpTlvDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('halfduplex',2),('fullduplex',3)))
_RlCdpTlvDuplex_Type.__name__=_H
_RlCdpTlvDuplex_Object=MibTableColumn
rlCdpTlvDuplex=_RlCdpTlvDuplex_Object((1,3,6,1,4,1,4526,17,137,16,1,15),_RlCdpTlvDuplex_Type())
rlCdpTlvDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvDuplex.setStatus(_A)
class _RlCdpTlvApplianceID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RlCdpTlvApplianceID_Type.__name__=_D
_RlCdpTlvApplianceID_Object=MibTableColumn
rlCdpTlvApplianceID=_RlCdpTlvApplianceID_Object((1,3,6,1,4,1,4526,17,137,16,1,16),_RlCdpTlvApplianceID_Type())
rlCdpTlvApplianceID.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvApplianceID.setStatus(_A)
class _RlCdpTlvApplianceVlanID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_RlCdpTlvApplianceVlanID_Type.__name__=_D
_RlCdpTlvApplianceVlanID_Object=MibTableColumn
rlCdpTlvApplianceVlanID=_RlCdpTlvApplianceVlanID_Object((1,3,6,1,4,1,4526,17,137,16,1,17),_RlCdpTlvApplianceVlanID_Type())
rlCdpTlvApplianceVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvApplianceVlanID.setStatus(_A)
class _RlCdpTlvExtendedTrust_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('untrusted',0),('trusted',1)))
_RlCdpTlvExtendedTrust_Type.__name__=_H
_RlCdpTlvExtendedTrust_Object=MibTableColumn
rlCdpTlvExtendedTrust=_RlCdpTlvExtendedTrust_Object((1,3,6,1,4,1,4526,17,137,16,1,18),_RlCdpTlvExtendedTrust_Type())
rlCdpTlvExtendedTrust.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvExtendedTrust.setStatus(_A)
class _RlCdpTlvCosForUntrustedPorts_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RlCdpTlvCosForUntrustedPorts_Type.__name__=_D
_RlCdpTlvCosForUntrustedPorts_Object=MibTableColumn
rlCdpTlvCosForUntrustedPorts=_RlCdpTlvCosForUntrustedPorts_Object((1,3,6,1,4,1,4526,17,137,16,1,19),_RlCdpTlvCosForUntrustedPorts_Type())
rlCdpTlvCosForUntrustedPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvCosForUntrustedPorts.setStatus(_A)
class _RlCdpTlvPowerAvailableRequestId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RlCdpTlvPowerAvailableRequestId_Type.__name__=_D
_RlCdpTlvPowerAvailableRequestId_Object=MibTableColumn
rlCdpTlvPowerAvailableRequestId=_RlCdpTlvPowerAvailableRequestId_Object((1,3,6,1,4,1,4526,17,137,16,1,20),_RlCdpTlvPowerAvailableRequestId_Type())
rlCdpTlvPowerAvailableRequestId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvPowerAvailableRequestId.setStatus(_A)
class _RlCdpTlvPowerAvailablePowerManagementId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RlCdpTlvPowerAvailablePowerManagementId_Type.__name__=_D
_RlCdpTlvPowerAvailablePowerManagementId_Object=MibTableColumn
rlCdpTlvPowerAvailablePowerManagementId=_RlCdpTlvPowerAvailablePowerManagementId_Object((1,3,6,1,4,1,4526,17,137,16,1,21),_RlCdpTlvPowerAvailablePowerManagementId_Type())
rlCdpTlvPowerAvailablePowerManagementId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvPowerAvailablePowerManagementId.setStatus(_A)
_RlCdpTlvPowerAvailable_Type=Unsigned32
_RlCdpTlvPowerAvailable_Object=MibTableColumn
rlCdpTlvPowerAvailable=_RlCdpTlvPowerAvailable_Object((1,3,6,1,4,1,4526,17,137,16,1,22),_RlCdpTlvPowerAvailable_Type())
rlCdpTlvPowerAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvPowerAvailable.setStatus(_A)
_RlCdpTlvPowerAvailableManagementPowerLevel_Type=Unsigned32
_RlCdpTlvPowerAvailableManagementPowerLevel_Object=MibTableColumn
rlCdpTlvPowerAvailableManagementPowerLevel=_RlCdpTlvPowerAvailableManagementPowerLevel_Object((1,3,6,1,4,1,4526,17,137,16,1,23),_RlCdpTlvPowerAvailableManagementPowerLevel_Type())
rlCdpTlvPowerAvailableManagementPowerLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvPowerAvailableManagementPowerLevel.setStatus(_A)
_RlCdpTlvSysName_Type=DisplayString
_RlCdpTlvSysName_Object=MibTableColumn
rlCdpTlvSysName=_RlCdpTlvSysName_Object((1,3,6,1,4,1,4526,17,137,16,1,24),_RlCdpTlvSysName_Type())
rlCdpTlvSysName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvSysName.setStatus(_A)
_RlCdpTlvPowerConsumption_Type=Unsigned32
_RlCdpTlvPowerConsumption_Object=MibTableColumn
rlCdpTlvPowerConsumption=_RlCdpTlvPowerConsumption_Object((1,3,6,1,4,1,4526,17,137,16,1,25),_RlCdpTlvPowerConsumption_Type())
rlCdpTlvPowerConsumption.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvPowerConsumption.setStatus(_A)
_RlCdpTlvPowerRequestedRequestId_Type=Unsigned32
_RlCdpTlvPowerRequestedRequestId_Object=MibTableColumn
rlCdpTlvPowerRequestedRequestId=_RlCdpTlvPowerRequestedRequestId_Object((1,3,6,1,4,1,4526,17,137,16,1,26),_RlCdpTlvPowerRequestedRequestId_Type())
rlCdpTlvPowerRequestedRequestId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvPowerRequestedRequestId.setStatus(_A)
_RlCdpTlvPowerRequestedPowerManagementId_Type=Unsigned32
_RlCdpTlvPowerRequestedPowerManagementId_Object=MibTableColumn
rlCdpTlvPowerRequestedPowerManagementId=_RlCdpTlvPowerRequestedPowerManagementId_Object((1,3,6,1,4,1,4526,17,137,16,1,27),_RlCdpTlvPowerRequestedPowerManagementId_Type())
rlCdpTlvPowerRequestedPowerManagementId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvPowerRequestedPowerManagementId.setStatus(_A)
class _RlCdpTlvSparePairPoECapabilities_Type(Bits):namedValues=NamedValues(*((_U,0),(_V,1),(_W,2),(_X,3)))
_RlCdpTlvSparePairPoECapabilities_Type.__name__=_P
_RlCdpTlvSparePairPoECapabilities_Object=MibTableColumn
rlCdpTlvSparePairPoECapabilities=_RlCdpTlvSparePairPoECapabilities_Object((1,3,6,1,4,1,4526,17,137,16,1,28),_RlCdpTlvSparePairPoECapabilities_Type())
rlCdpTlvSparePairPoECapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvSparePairPoECapabilities.setStatus(_A)
class _RlCdpAdvertiseApplianceTlv_Type(TruthValue):defaultValue=1
_RlCdpAdvertiseApplianceTlv_Type.__name__=_I
_RlCdpAdvertiseApplianceTlv_Object=MibScalar
rlCdpAdvertiseApplianceTlv=_RlCdpAdvertiseApplianceTlv_Object((1,3,6,1,4,1,4526,17,137,17),_RlCdpAdvertiseApplianceTlv_Type())
rlCdpAdvertiseApplianceTlv.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCdpAdvertiseApplianceTlv.setStatus(_A)
class _RlCdpValidateMandatoryTlvs_Type(TruthValue):defaultValue=1
_RlCdpValidateMandatoryTlvs_Type.__name__=_I
_RlCdpValidateMandatoryTlvs_Object=MibScalar
rlCdpValidateMandatoryTlvs=_RlCdpValidateMandatoryTlvs_Object((1,3,6,1,4,1,4526,17,137,18),_RlCdpValidateMandatoryTlvs_Type())
rlCdpValidateMandatoryTlvs.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCdpValidateMandatoryTlvs.setStatus(_A)
_RlCdpInterfaceCountersTable_Object=MibTable
rlCdpInterfaceCountersTable=_RlCdpInterfaceCountersTable_Object((1,3,6,1,4,1,4526,17,137,19))
if mibBuilder.loadTexts:rlCdpInterfaceCountersTable.setStatus(_A)
_RlCdpInterfaceCountersEntry_Object=MibTableRow
rlCdpInterfaceCountersEntry=_RlCdpInterfaceCountersEntry_Object((1,3,6,1,4,1,4526,17,137,19,1))
rlCdpInterfaceCountersEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:rlCdpInterfaceCountersEntry.setStatus(_A)
_RlCdpInterfaceId_Type=InterfaceIndex
_RlCdpInterfaceId_Object=MibTableColumn
rlCdpInterfaceId=_RlCdpInterfaceId_Object((1,3,6,1,4,1,4526,17,137,19,1,1),_RlCdpInterfaceId_Type())
rlCdpInterfaceId.setMaxAccess(_J)
if mibBuilder.loadTexts:rlCdpInterfaceId.setStatus(_A)
_RlCdpInterfaceTotalInputPackets_Type=Counter32
_RlCdpInterfaceTotalInputPackets_Object=MibTableColumn
rlCdpInterfaceTotalInputPackets=_RlCdpInterfaceTotalInputPackets_Object((1,3,6,1,4,1,4526,17,137,19,1,2),_RlCdpInterfaceTotalInputPackets_Type())
rlCdpInterfaceTotalInputPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpInterfaceTotalInputPackets.setStatus(_A)
_RlCdpInterfaceV1InputPackets_Type=Counter32
_RlCdpInterfaceV1InputPackets_Object=MibTableColumn
rlCdpInterfaceV1InputPackets=_RlCdpInterfaceV1InputPackets_Object((1,3,6,1,4,1,4526,17,137,19,1,3),_RlCdpInterfaceV1InputPackets_Type())
rlCdpInterfaceV1InputPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpInterfaceV1InputPackets.setStatus(_A)
_RlCdpInterfaceV2InputPackets_Type=Counter32
_RlCdpInterfaceV2InputPackets_Object=MibTableColumn
rlCdpInterfaceV2InputPackets=_RlCdpInterfaceV2InputPackets_Object((1,3,6,1,4,1,4526,17,137,19,1,4),_RlCdpInterfaceV2InputPackets_Type())
rlCdpInterfaceV2InputPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpInterfaceV2InputPackets.setStatus(_A)
_RlCdpInterfaceTotalOutputPackets_Type=Counter32
_RlCdpInterfaceTotalOutputPackets_Object=MibTableColumn
rlCdpInterfaceTotalOutputPackets=_RlCdpInterfaceTotalOutputPackets_Object((1,3,6,1,4,1,4526,17,137,19,1,5),_RlCdpInterfaceTotalOutputPackets_Type())
rlCdpInterfaceTotalOutputPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpInterfaceTotalOutputPackets.setStatus(_A)
_RlCdpInterfaceV1OutputPackets_Type=Counter32
_RlCdpInterfaceV1OutputPackets_Object=MibTableColumn
rlCdpInterfaceV1OutputPackets=_RlCdpInterfaceV1OutputPackets_Object((1,3,6,1,4,1,4526,17,137,19,1,6),_RlCdpInterfaceV1OutputPackets_Type())
rlCdpInterfaceV1OutputPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpInterfaceV1OutputPackets.setStatus(_A)
_RlCdpInterfaceV2OutputPackets_Type=Counter32
_RlCdpInterfaceV2OutputPackets_Object=MibTableColumn
rlCdpInterfaceV2OutputPackets=_RlCdpInterfaceV2OutputPackets_Object((1,3,6,1,4,1,4526,17,137,19,1,7),_RlCdpInterfaceV2OutputPackets_Type())
rlCdpInterfaceV2OutputPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpInterfaceV2OutputPackets.setStatus(_A)
_RlCdpInterfaceIllegalChksum_Type=Counter32
_RlCdpInterfaceIllegalChksum_Object=MibTableColumn
rlCdpInterfaceIllegalChksum=_RlCdpInterfaceIllegalChksum_Object((1,3,6,1,4,1,4526,17,137,19,1,8),_RlCdpInterfaceIllegalChksum_Type())
rlCdpInterfaceIllegalChksum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpInterfaceIllegalChksum.setStatus(_A)
_RlCdpInterfaceErrorPackets_Type=Counter32
_RlCdpInterfaceErrorPackets_Object=MibTableColumn
rlCdpInterfaceErrorPackets=_RlCdpInterfaceErrorPackets_Object((1,3,6,1,4,1,4526,17,137,19,1,9),_RlCdpInterfaceErrorPackets_Type())
rlCdpInterfaceErrorPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpInterfaceErrorPackets.setStatus(_A)
_RlCdpInterfaceMaxNeighborsExceededInMainCache_Type=Counter32
_RlCdpInterfaceMaxNeighborsExceededInMainCache_Object=MibTableColumn
rlCdpInterfaceMaxNeighborsExceededInMainCache=_RlCdpInterfaceMaxNeighborsExceededInMainCache_Object((1,3,6,1,4,1,4526,17,137,19,1,10),_RlCdpInterfaceMaxNeighborsExceededInMainCache_Type())
rlCdpInterfaceMaxNeighborsExceededInMainCache.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpInterfaceMaxNeighborsExceededInMainCache.setStatus(_A)
_RlCdpInterfaceMaxNeighborsExceededInSecondaryCache_Type=Counter32
_RlCdpInterfaceMaxNeighborsExceededInSecondaryCache_Object=MibTableColumn
rlCdpInterfaceMaxNeighborsExceededInSecondaryCache=_RlCdpInterfaceMaxNeighborsExceededInSecondaryCache_Object((1,3,6,1,4,1,4526,17,137,19,1,11),_RlCdpInterfaceMaxNeighborsExceededInSecondaryCache_Type())
rlCdpInterfaceMaxNeighborsExceededInSecondaryCache.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpInterfaceMaxNeighborsExceededInSecondaryCache.setStatus(_A)
_RlCdpInterfaceCountersClear_Type=InterfaceIndexOrZero
_RlCdpInterfaceCountersClear_Object=MibScalar
rlCdpInterfaceCountersClear=_RlCdpInterfaceCountersClear_Object((1,3,6,1,4,1,4526,17,137,20),_RlCdpInterfaceCountersClear_Type())
rlCdpInterfaceCountersClear.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCdpInterfaceCountersClear.setStatus(_A)
_RlCdpTlvPowerRequestTable_Object=MibTable
rlCdpTlvPowerRequestTable=_RlCdpTlvPowerRequestTable_Object((1,3,6,1,4,1,4526,17,137,21))
if mibBuilder.loadTexts:rlCdpTlvPowerRequestTable.setStatus(_A)
_RlCdpTlvPowerRequestEntry_Object=MibTableRow
rlCdpTlvPowerRequestEntry=_RlCdpTlvPowerRequestEntry_Object((1,3,6,1,4,1,4526,17,137,21,1))
rlCdpTlvPowerRequestEntry.setIndexNames((0,_E,_Q),(0,_E,_Z))
if mibBuilder.loadTexts:rlCdpTlvPowerRequestEntry.setStatus(_A)
class _RlCdpTlvPowerRequestPowerLevelIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlCdpTlvPowerRequestPowerLevelIndex_Type.__name__=_D
_RlCdpTlvPowerRequestPowerLevelIndex_Object=MibTableColumn
rlCdpTlvPowerRequestPowerLevelIndex=_RlCdpTlvPowerRequestPowerLevelIndex_Object((1,3,6,1,4,1,4526,17,137,21,1,2),_RlCdpTlvPowerRequestPowerLevelIndex_Type())
rlCdpTlvPowerRequestPowerLevelIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:rlCdpTlvPowerRequestPowerLevelIndex.setStatus(_A)
class _RlCdpTlvPowerRequestPowerLevel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlCdpTlvPowerRequestPowerLevel_Type.__name__=_D
_RlCdpTlvPowerRequestPowerLevel_Object=MibTableColumn
rlCdpTlvPowerRequestPowerLevel=_RlCdpTlvPowerRequestPowerLevel_Object((1,3,6,1,4,1,4526,17,137,21,1,3),_RlCdpTlvPowerRequestPowerLevel_Type())
rlCdpTlvPowerRequestPowerLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpTlvPowerRequestPowerLevel.setStatus(_A)
_RlCdpSecondaryCacheAddressTable_Object=MibTable
rlCdpSecondaryCacheAddressTable=_RlCdpSecondaryCacheAddressTable_Object((1,3,6,1,4,1,4526,17,137,22))
if mibBuilder.loadTexts:rlCdpSecondaryCacheAddressTable.setStatus(_A)
_RlCdpSecondaryCacheAddressEntry_Object=MibTableRow
rlCdpSecondaryCacheAddressEntry=_RlCdpSecondaryCacheAddressEntry_Object((1,3,6,1,4,1,4526,17,137,22,1))
rlCdpSecondaryCacheAddressEntry.setIndexNames((0,_F,_L),(0,_F,_K),(0,_E,_a))
if mibBuilder.loadTexts:rlCdpSecondaryCacheAddressEntry.setStatus(_A)
class _RlCdpSecondaryCacheAddressIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlCdpSecondaryCacheAddressIndex_Type.__name__=_H
_RlCdpSecondaryCacheAddressIndex_Object=MibTableColumn
rlCdpSecondaryCacheAddressIndex=_RlCdpSecondaryCacheAddressIndex_Object((1,3,6,1,4,1,4526,17,137,22,1,3),_RlCdpSecondaryCacheAddressIndex_Type())
rlCdpSecondaryCacheAddressIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:rlCdpSecondaryCacheAddressIndex.setStatus(_A)
_RlCdpSecondaryCacheAddressType_Type=CiscoNetworkProtocol
_RlCdpSecondaryCacheAddressType_Object=MibTableColumn
rlCdpSecondaryCacheAddressType=_RlCdpSecondaryCacheAddressType_Object((1,3,6,1,4,1,4526,17,137,22,1,4),_RlCdpSecondaryCacheAddressType_Type())
rlCdpSecondaryCacheAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpSecondaryCacheAddressType.setStatus(_A)
_RlCdpSecondaryCacheAddress_Type=CiscoNetworkAddress
_RlCdpSecondaryCacheAddress_Object=MibTableColumn
rlCdpSecondaryCacheAddress=_RlCdpSecondaryCacheAddress_Object((1,3,6,1,4,1,4526,17,137,22,1,5),_RlCdpSecondaryCacheAddress_Type())
rlCdpSecondaryCacheAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpSecondaryCacheAddress.setStatus(_A)
_RlCdpSecondaryCacheRequestedPowerTable_Object=MibTable
rlCdpSecondaryCacheRequestedPowerTable=_RlCdpSecondaryCacheRequestedPowerTable_Object((1,3,6,1,4,1,4526,17,137,23))
if mibBuilder.loadTexts:rlCdpSecondaryCacheRequestedPowerTable.setStatus(_A)
_RlCdpSecondaryCacheRequestedPowerEntry_Object=MibTableRow
rlCdpSecondaryCacheRequestedPowerEntry=_RlCdpSecondaryCacheRequestedPowerEntry_Object((1,3,6,1,4,1,4526,17,137,23,1))
rlCdpSecondaryCacheRequestedPowerEntry.setIndexNames((0,_F,_L),(0,_F,_K),(0,_E,_b))
if mibBuilder.loadTexts:rlCdpSecondaryCacheRequestedPowerEntry.setStatus(_A)
class _RlCdpSecondaryCacheRequestedPowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlCdpSecondaryCacheRequestedPowerIndex_Type.__name__=_H
_RlCdpSecondaryCacheRequestedPowerIndex_Object=MibTableColumn
rlCdpSecondaryCacheRequestedPowerIndex=_RlCdpSecondaryCacheRequestedPowerIndex_Object((1,3,6,1,4,1,4526,17,137,23,1,3),_RlCdpSecondaryCacheRequestedPowerIndex_Type())
rlCdpSecondaryCacheRequestedPowerIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:rlCdpSecondaryCacheRequestedPowerIndex.setStatus(_A)
class _RlCdpSecondaryCacheRequestedPowerLevel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RlCdpSecondaryCacheRequestedPowerLevel_Type.__name__=_D
_RlCdpSecondaryCacheRequestedPowerLevel_Object=MibTableColumn
rlCdpSecondaryCacheRequestedPowerLevel=_RlCdpSecondaryCacheRequestedPowerLevel_Object((1,3,6,1,4,1,4526,17,137,23,1,4),_RlCdpSecondaryCacheRequestedPowerLevel_Type())
rlCdpSecondaryCacheRequestedPowerLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCdpSecondaryCacheRequestedPowerLevel.setStatus(_A)
cdpCacheEntry.registerAugmentions((_E,_c))
rlCdpCacheEntry.setIndexNames(*cdpCacheEntry.getIndexNames())
rlCdpLogMismatchDuplexTrap=NotificationType((1,3,6,1,4,1,4526,17,0,224))
rlCdpLogMismatchDuplexTrap.setObjects(*((_G,_M),(_G,_N)))
if mibBuilder.loadTexts:rlCdpLogMismatchDuplexTrap.setStatus(_A)
rlCdpLogMismatchVoiceVlanTrap=NotificationType((1,3,6,1,4,1,4526,17,0,225))
rlCdpLogMismatchVoiceVlanTrap.setObjects(*((_G,_M),(_G,_N)))
if mibBuilder.loadTexts:rlCdpLogMismatchVoiceVlanTrap.setStatus(_A)
rlCdpLogMismatchNativeVlanTrap=NotificationType((1,3,6,1,4,1,4526,17,0,226))
rlCdpLogMismatchNativeVlanTrap.setObjects(*((_G,_M),(_G,_N)))
if mibBuilder.loadTexts:rlCdpLogMismatchNativeVlanTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'RlCdpVersionTypes':RlCdpVersionTypes,'RlCdpCounterTypes':RlCdpCounterTypes,_T:RlCdpPduActionTypes,'rlCdpLogMismatchDuplexTrap':rlCdpLogMismatchDuplexTrap,'rlCdpLogMismatchVoiceVlanTrap':rlCdpLogMismatchVoiceVlanTrap,'rlCdpLogMismatchNativeVlanTrap':rlCdpLogMismatchNativeVlanTrap,'rlCdp':rlCdp,'rlCdpVersionAdvertised':rlCdpVersionAdvertised,'rlCdpSourceInterface':rlCdpSourceInterface,'rlCdpLogMismatchDuplexEnable':rlCdpLogMismatchDuplexEnable,'rlCdpCountersTable':rlCdpCountersTable,'rlCdpCountersEntry':rlCdpCountersEntry,_S:rlCdpCountersName,'rlCdpCountersValue':rlCdpCountersValue,'rlCdpCountersClear':rlCdpCountersClear,'rlCdpCacheClear':rlCdpCacheClear,'rlCdpVoiceVlanId':rlCdpVoiceVlanId,'rlCdpCacheTable':rlCdpCacheTable,_c:rlCdpCacheEntry,'rlCdpCacheVersionExt':rlCdpCacheVersionExt,'rlCdpCacheTimeToLive':rlCdpCacheTimeToLive,'rlCdpCacheCdpVersion':rlCdpCacheCdpVersion,'rlCdpPduAction':rlCdpPduAction,'rlCdpLogMismatchVoiceVlanEnable':rlCdpLogMismatchVoiceVlanEnable,'rlCdpLogMismatchNativeVlanEnable':rlCdpLogMismatchNativeVlanEnable,'rlCdpSecondaryCacheTable':rlCdpSecondaryCacheTable,'rlCdpSecondaryCacheEntry':rlCdpSecondaryCacheEntry,'rlCdpSecondaryCacheMacAddress':rlCdpSecondaryCacheMacAddress,'rlCdpSecondaryCachePlatform':rlCdpSecondaryCachePlatform,'rlCdpSecondaryCacheCapabilities':rlCdpSecondaryCacheCapabilities,'rlCdpSecondaryCacheVoiceVlanID':rlCdpSecondaryCacheVoiceVlanID,'rlCdpSecondaryCacheTimeToLive':rlCdpSecondaryCacheTimeToLive,'rlCdpSecondaryCachePowerAvailable':rlCdpSecondaryCachePowerAvailable,'rlCdpSecondaryCachePowerConsumption':rlCdpSecondaryCachePowerConsumption,'rlCdpSecondaryCacheSparePairPoECapabilities':rlCdpSecondaryCacheSparePairPoECapabilities,'rlCdpSecondaryCacheDeviceId':rlCdpSecondaryCacheDeviceId,'rlCdpSecondaryCachePortId':rlCdpSecondaryCachePortId,'rlCdpGlobalLogMismatchDuplexEnable':rlCdpGlobalLogMismatchDuplexEnable,'rlCdpGlobalLogMismatchVoiceVlanEnable':rlCdpGlobalLogMismatchVoiceVlanEnable,'rlCdpGlobalLogMismatchNativeVlanEnable':rlCdpGlobalLogMismatchNativeVlanEnable,'rlCdpTlvTable':rlCdpTlvTable,'rlCdpTlvEntry':rlCdpTlvEntry,_Q:rlCdpTlvIfIndex,'rlCdpTlvDeviceIdFormat':rlCdpTlvDeviceIdFormat,'rlCdpTlvDeviceId':rlCdpTlvDeviceId,'rlCdpTlvAddress1Type':rlCdpTlvAddress1Type,'rlCdpTlvAddress1':rlCdpTlvAddress1,'rlCdpTlvAddress2Type':rlCdpTlvAddress2Type,'rlCdpTlvAddress2':rlCdpTlvAddress2,'rlCdpTlvAddress3Type':rlCdpTlvAddress3Type,'rlCdpTlvAddress3':rlCdpTlvAddress3,'rlCdpTlvPortId':rlCdpTlvPortId,'rlCdpTlvCapabilities':rlCdpTlvCapabilities,'rlCdpTlvVersion':rlCdpTlvVersion,'rlCdpTlvPlatform':rlCdpTlvPlatform,'rlCdpTlvNativeVLAN':rlCdpTlvNativeVLAN,'rlCdpTlvDuplex':rlCdpTlvDuplex,'rlCdpTlvApplianceID':rlCdpTlvApplianceID,'rlCdpTlvApplianceVlanID':rlCdpTlvApplianceVlanID,'rlCdpTlvExtendedTrust':rlCdpTlvExtendedTrust,'rlCdpTlvCosForUntrustedPorts':rlCdpTlvCosForUntrustedPorts,'rlCdpTlvPowerAvailableRequestId':rlCdpTlvPowerAvailableRequestId,'rlCdpTlvPowerAvailablePowerManagementId':rlCdpTlvPowerAvailablePowerManagementId,'rlCdpTlvPowerAvailable':rlCdpTlvPowerAvailable,'rlCdpTlvPowerAvailableManagementPowerLevel':rlCdpTlvPowerAvailableManagementPowerLevel,'rlCdpTlvSysName':rlCdpTlvSysName,'rlCdpTlvPowerConsumption':rlCdpTlvPowerConsumption,'rlCdpTlvPowerRequestedRequestId':rlCdpTlvPowerRequestedRequestId,'rlCdpTlvPowerRequestedPowerManagementId':rlCdpTlvPowerRequestedPowerManagementId,'rlCdpTlvSparePairPoECapabilities':rlCdpTlvSparePairPoECapabilities,'rlCdpAdvertiseApplianceTlv':rlCdpAdvertiseApplianceTlv,'rlCdpValidateMandatoryTlvs':rlCdpValidateMandatoryTlvs,'rlCdpInterfaceCountersTable':rlCdpInterfaceCountersTable,'rlCdpInterfaceCountersEntry':rlCdpInterfaceCountersEntry,_Y:rlCdpInterfaceId,'rlCdpInterfaceTotalInputPackets':rlCdpInterfaceTotalInputPackets,'rlCdpInterfaceV1InputPackets':rlCdpInterfaceV1InputPackets,'rlCdpInterfaceV2InputPackets':rlCdpInterfaceV2InputPackets,'rlCdpInterfaceTotalOutputPackets':rlCdpInterfaceTotalOutputPackets,'rlCdpInterfaceV1OutputPackets':rlCdpInterfaceV1OutputPackets,'rlCdpInterfaceV2OutputPackets':rlCdpInterfaceV2OutputPackets,'rlCdpInterfaceIllegalChksum':rlCdpInterfaceIllegalChksum,'rlCdpInterfaceErrorPackets':rlCdpInterfaceErrorPackets,'rlCdpInterfaceMaxNeighborsExceededInMainCache':rlCdpInterfaceMaxNeighborsExceededInMainCache,'rlCdpInterfaceMaxNeighborsExceededInSecondaryCache':rlCdpInterfaceMaxNeighborsExceededInSecondaryCache,'rlCdpInterfaceCountersClear':rlCdpInterfaceCountersClear,'rlCdpTlvPowerRequestTable':rlCdpTlvPowerRequestTable,'rlCdpTlvPowerRequestEntry':rlCdpTlvPowerRequestEntry,_Z:rlCdpTlvPowerRequestPowerLevelIndex,'rlCdpTlvPowerRequestPowerLevel':rlCdpTlvPowerRequestPowerLevel,'rlCdpSecondaryCacheAddressTable':rlCdpSecondaryCacheAddressTable,'rlCdpSecondaryCacheAddressEntry':rlCdpSecondaryCacheAddressEntry,_a:rlCdpSecondaryCacheAddressIndex,'rlCdpSecondaryCacheAddressType':rlCdpSecondaryCacheAddressType,'rlCdpSecondaryCacheAddress':rlCdpSecondaryCacheAddress,'rlCdpSecondaryCacheRequestedPowerTable':rlCdpSecondaryCacheRequestedPowerTable,'rlCdpSecondaryCacheRequestedPowerEntry':rlCdpSecondaryCacheRequestedPowerEntry,_b:rlCdpSecondaryCacheRequestedPowerIndex,'rlCdpSecondaryCacheRequestedPowerLevel':rlCdpSecondaryCacheRequestedPowerLevel})