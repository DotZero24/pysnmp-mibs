_K='extremeNetFlowCollectorId'
_J='extremeNetFlowGroupNumber'
_I='extremeNetFlowPortConfigFilterNumber'
_H='extremeNetFlowPortConfigFilterEgress'
_G='extremeNetFlowPortConfigPortNumber'
_F='extremeNetFlowPortConfigPortIndex'
_E='not-accessible'
_D='EXTREME-NETFLOW-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
extremeNetFlow=ModuleIdentity((1,3,6,1,4,1,1916,1,22))
_ExtremeNetFlowConfigPort_ObjectIdentity=ObjectIdentity
extremeNetFlowConfigPort=_ExtremeNetFlowConfigPort_ObjectIdentity((1,3,6,1,4,1,1916,1,22,1))
_ExtremeNetFlowPortConfigTable_Object=MibTable
extremeNetFlowPortConfigTable=_ExtremeNetFlowPortConfigTable_Object((1,3,6,1,4,1,1916,1,22,1,1))
if mibBuilder.loadTexts:extremeNetFlowPortConfigTable.setStatus(_A)
_ExtremeNetFlowPortConfigEntry_Object=MibTableRow
extremeNetFlowPortConfigEntry=_ExtremeNetFlowPortConfigEntry_Object((1,3,6,1,4,1,1916,1,22,1,1,1))
extremeNetFlowPortConfigEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:extremeNetFlowPortConfigEntry.setStatus(_A)
class _ExtremeNetFlowPortConfigPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeNetFlowPortConfigPortIndex_Type.__name__=_C
_ExtremeNetFlowPortConfigPortIndex_Object=MibTableColumn
extremeNetFlowPortConfigPortIndex=_ExtremeNetFlowPortConfigPortIndex_Object((1,3,6,1,4,1,1916,1,22,1,1,1,1),_ExtremeNetFlowPortConfigPortIndex_Type())
extremeNetFlowPortConfigPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeNetFlowPortConfigPortIndex.setStatus(_A)
_ExtremeNetFlowPortConfigEnabled_Type=TruthValue
_ExtremeNetFlowPortConfigEnabled_Object=MibTableColumn
extremeNetFlowPortConfigEnabled=_ExtremeNetFlowPortConfigEnabled_Object((1,3,6,1,4,1,1916,1,22,1,1,1,2),_ExtremeNetFlowPortConfigEnabled_Type())
extremeNetFlowPortConfigEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowPortConfigEnabled.setStatus(_A)
class _ExtremeNetFlowPortConfigTimout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeNetFlowPortConfigTimout_Type.__name__=_C
_ExtremeNetFlowPortConfigTimout_Object=MibTableColumn
extremeNetFlowPortConfigTimout=_ExtremeNetFlowPortConfigTimout_Object((1,3,6,1,4,1,1916,1,22,1,1,1,3),_ExtremeNetFlowPortConfigTimout_Type())
extremeNetFlowPortConfigTimout.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowPortConfigTimout.setStatus(_A)
class _ExtremeNetFlowPortOverFlowPackets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeNetFlowPortOverFlowPackets_Type.__name__=_C
_ExtremeNetFlowPortOverFlowPackets_Object=MibTableColumn
extremeNetFlowPortOverFlowPackets=_ExtremeNetFlowPortOverFlowPackets_Object((1,3,6,1,4,1,1916,1,22,1,1,1,4),_ExtremeNetFlowPortOverFlowPackets_Type())
extremeNetFlowPortOverFlowPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowPortOverFlowPackets.setStatus(_A)
_ExtremeNetFlowPortFilterConfigTable_Object=MibTable
extremeNetFlowPortFilterConfigTable=_ExtremeNetFlowPortFilterConfigTable_Object((1,3,6,1,4,1,1916,1,22,1,2))
if mibBuilder.loadTexts:extremeNetFlowPortFilterConfigTable.setStatus(_A)
_ExtremeNetFlowPortFilterConfigEntry_Object=MibTableRow
extremeNetFlowPortFilterConfigEntry=_ExtremeNetFlowPortFilterConfigEntry_Object((1,3,6,1,4,1,1916,1,22,1,2,1))
extremeNetFlowPortFilterConfigEntry.setIndexNames((0,_D,_G),(0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:extremeNetFlowPortFilterConfigEntry.setStatus(_A)
class _ExtremeNetFlowPortConfigPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeNetFlowPortConfigPortNumber_Type.__name__=_C
_ExtremeNetFlowPortConfigPortNumber_Object=MibTableColumn
extremeNetFlowPortConfigPortNumber=_ExtremeNetFlowPortConfigPortNumber_Object((1,3,6,1,4,1,1916,1,22,1,2,1,1),_ExtremeNetFlowPortConfigPortNumber_Type())
extremeNetFlowPortConfigPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeNetFlowPortConfigPortNumber.setStatus(_A)
_ExtremeNetFlowPortConfigFilterEgress_Type=TruthValue
_ExtremeNetFlowPortConfigFilterEgress_Object=MibTableColumn
extremeNetFlowPortConfigFilterEgress=_ExtremeNetFlowPortConfigFilterEgress_Object((1,3,6,1,4,1,1916,1,22,1,2,1,2),_ExtremeNetFlowPortConfigFilterEgress_Type())
extremeNetFlowPortConfigFilterEgress.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeNetFlowPortConfigFilterEgress.setStatus(_A)
class _ExtremeNetFlowPortConfigFilterNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ExtremeNetFlowPortConfigFilterNumber_Type.__name__=_C
_ExtremeNetFlowPortConfigFilterNumber_Object=MibTableColumn
extremeNetFlowPortConfigFilterNumber=_ExtremeNetFlowPortConfigFilterNumber_Object((1,3,6,1,4,1,1916,1,22,1,2,1,3),_ExtremeNetFlowPortConfigFilterNumber_Type())
extremeNetFlowPortConfigFilterNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeNetFlowPortConfigFilterNumber.setStatus(_A)
_ExtremeNetFlowPortEnabled_Type=TruthValue
_ExtremeNetFlowPortEnabled_Object=MibTableColumn
extremeNetFlowPortEnabled=_ExtremeNetFlowPortEnabled_Object((1,3,6,1,4,1,1916,1,22,1,2,1,4),_ExtremeNetFlowPortEnabled_Type())
extremeNetFlowPortEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowPortEnabled.setStatus(_A)
_ExtremeNetFlowFilterEnabled_Type=TruthValue
_ExtremeNetFlowFilterEnabled_Object=MibTableColumn
extremeNetFlowFilterEnabled=_ExtremeNetFlowFilterEnabled_Object((1,3,6,1,4,1,1916,1,22,1,2,1,5),_ExtremeNetFlowFilterEnabled_Type())
extremeNetFlowFilterEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowFilterEnabled.setStatus(_A)
_ExtremeNetFlowDestIpAddress_Type=IpAddress
_ExtremeNetFlowDestIpAddress_Object=MibTableColumn
extremeNetFlowDestIpAddress=_ExtremeNetFlowDestIpAddress_Object((1,3,6,1,4,1,1916,1,22,1,2,1,6),_ExtremeNetFlowDestIpAddress_Type())
extremeNetFlowDestIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowDestIpAddress.setStatus(_A)
_ExtremeNetFlowDestIpAddressMask_Type=IpAddress
_ExtremeNetFlowDestIpAddressMask_Object=MibTableColumn
extremeNetFlowDestIpAddressMask=_ExtremeNetFlowDestIpAddressMask_Object((1,3,6,1,4,1,1916,1,22,1,2,1,7),_ExtremeNetFlowDestIpAddressMask_Type())
extremeNetFlowDestIpAddressMask.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowDestIpAddressMask.setStatus(_A)
_ExtremeNetFlowSourceIpAddress_Type=IpAddress
_ExtremeNetFlowSourceIpAddress_Object=MibTableColumn
extremeNetFlowSourceIpAddress=_ExtremeNetFlowSourceIpAddress_Object((1,3,6,1,4,1,1916,1,22,1,2,1,8),_ExtremeNetFlowSourceIpAddress_Type())
extremeNetFlowSourceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowSourceIpAddress.setStatus(_A)
_ExtremeNetFlowSourceIpAddressMask_Type=IpAddress
_ExtremeNetFlowSourceIpAddressMask_Object=MibTableColumn
extremeNetFlowSourceIpAddressMask=_ExtremeNetFlowSourceIpAddressMask_Object((1,3,6,1,4,1,1916,1,22,1,2,1,9),_ExtremeNetFlowSourceIpAddressMask_Type())
extremeNetFlowSourceIpAddressMask.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowSourceIpAddressMask.setStatus(_A)
class _ExtremeNetFlowDestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeNetFlowDestPort_Type.__name__=_C
_ExtremeNetFlowDestPort_Object=MibTableColumn
extremeNetFlowDestPort=_ExtremeNetFlowDestPort_Object((1,3,6,1,4,1,1916,1,22,1,2,1,10),_ExtremeNetFlowDestPort_Type())
extremeNetFlowDestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowDestPort.setStatus(_A)
class _ExtremeNetFlowDestPortMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeNetFlowDestPortMask_Type.__name__=_C
_ExtremeNetFlowDestPortMask_Object=MibTableColumn
extremeNetFlowDestPortMask=_ExtremeNetFlowDestPortMask_Object((1,3,6,1,4,1,1916,1,22,1,2,1,11),_ExtremeNetFlowDestPortMask_Type())
extremeNetFlowDestPortMask.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowDestPortMask.setStatus(_A)
class _ExtremeNetFlowSourcePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeNetFlowSourcePort_Type.__name__=_C
_ExtremeNetFlowSourcePort_Object=MibTableColumn
extremeNetFlowSourcePort=_ExtremeNetFlowSourcePort_Object((1,3,6,1,4,1,1916,1,22,1,2,1,12),_ExtremeNetFlowSourcePort_Type())
extremeNetFlowSourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowSourcePort.setStatus(_A)
class _ExtremeNetFlowSourcePortMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeNetFlowSourcePortMask_Type.__name__=_C
_ExtremeNetFlowSourcePortMask_Object=MibTableColumn
extremeNetFlowSourcePortMask=_ExtremeNetFlowSourcePortMask_Object((1,3,6,1,4,1,1916,1,22,1,2,1,13),_ExtremeNetFlowSourcePortMask_Type())
extremeNetFlowSourcePortMask.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowSourcePortMask.setStatus(_A)
class _ExtremeNetFlowProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeNetFlowProtocol_Type.__name__=_C
_ExtremeNetFlowProtocol_Object=MibTableColumn
extremeNetFlowProtocol=_ExtremeNetFlowProtocol_Object((1,3,6,1,4,1,1916,1,22,1,2,1,14),_ExtremeNetFlowProtocol_Type())
extremeNetFlowProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowProtocol.setStatus(_A)
class _ExtremeNetFlowProtocolMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeNetFlowProtocolMask_Type.__name__=_C
_ExtremeNetFlowProtocolMask_Object=MibTableColumn
extremeNetFlowProtocolMask=_ExtremeNetFlowProtocolMask_Object((1,3,6,1,4,1,1916,1,22,1,2,1,15),_ExtremeNetFlowProtocolMask_Type())
extremeNetFlowProtocolMask.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowProtocolMask.setStatus(_A)
class _ExtremeNetFlowFilterGroupNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_ExtremeNetFlowFilterGroupNumber_Type.__name__=_C
_ExtremeNetFlowFilterGroupNumber_Object=MibTableColumn
extremeNetFlowFilterGroupNumber=_ExtremeNetFlowFilterGroupNumber_Object((1,3,6,1,4,1,1916,1,22,1,2,1,16),_ExtremeNetFlowFilterGroupNumber_Type())
extremeNetFlowFilterGroupNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowFilterGroupNumber.setStatus(_A)
_ExtremeNetFlowMatchAllFlag_Type=TruthValue
_ExtremeNetFlowMatchAllFlag_Object=MibTableColumn
extremeNetFlowMatchAllFlag=_ExtremeNetFlowMatchAllFlag_Object((1,3,6,1,4,1,1916,1,22,1,2,1,17),_ExtremeNetFlowMatchAllFlag_Type())
extremeNetFlowMatchAllFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowMatchAllFlag.setStatus(_A)
_ExtremeNetFlowMatchNoneFlag_Type=TruthValue
_ExtremeNetFlowMatchNoneFlag_Object=MibTableColumn
extremeNetFlowMatchNoneFlag=_ExtremeNetFlowMatchNoneFlag_Object((1,3,6,1,4,1,1916,1,22,1,2,1,18),_ExtremeNetFlowMatchNoneFlag_Type())
extremeNetFlowMatchNoneFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowMatchNoneFlag.setStatus(_A)
_ExtremeNetFlowConfigGroup_ObjectIdentity=ObjectIdentity
extremeNetFlowConfigGroup=_ExtremeNetFlowConfigGroup_ObjectIdentity((1,3,6,1,4,1,1916,1,22,2))
_ExtremeNetFlowGroupCollectorTable_Object=MibTable
extremeNetFlowGroupCollectorTable=_ExtremeNetFlowGroupCollectorTable_Object((1,3,6,1,4,1,1916,1,22,2,2))
if mibBuilder.loadTexts:extremeNetFlowGroupCollectorTable.setStatus(_A)
_ExtremeNetFlowGroupCollectorEntry_Object=MibTableRow
extremeNetFlowGroupCollectorEntry=_ExtremeNetFlowGroupCollectorEntry_Object((1,3,6,1,4,1,1916,1,22,2,2,1))
extremeNetFlowGroupCollectorEntry.setIndexNames((0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:extremeNetFlowGroupCollectorEntry.setStatus(_A)
class _ExtremeNetFlowGroupNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_ExtremeNetFlowGroupNumber_Type.__name__=_C
_ExtremeNetFlowGroupNumber_Object=MibTableColumn
extremeNetFlowGroupNumber=_ExtremeNetFlowGroupNumber_Object((1,3,6,1,4,1,1916,1,22,2,2,1,1),_ExtremeNetFlowGroupNumber_Type())
extremeNetFlowGroupNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeNetFlowGroupNumber.setStatus(_A)
class _ExtremeNetFlowCollectorId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ExtremeNetFlowCollectorId_Type.__name__=_C
_ExtremeNetFlowCollectorId_Object=MibTableColumn
extremeNetFlowCollectorId=_ExtremeNetFlowCollectorId_Object((1,3,6,1,4,1,1916,1,22,2,2,1,2),_ExtremeNetFlowCollectorId_Type())
extremeNetFlowCollectorId.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeNetFlowCollectorId.setStatus(_A)
_ExtremeNetFlowGroupPingEnabled_Type=TruthValue
_ExtremeNetFlowGroupPingEnabled_Object=MibTableColumn
extremeNetFlowGroupPingEnabled=_ExtremeNetFlowGroupPingEnabled_Object((1,3,6,1,4,1,1916,1,22,2,2,1,3),_ExtremeNetFlowGroupPingEnabled_Type())
extremeNetFlowGroupPingEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowGroupPingEnabled.setStatus(_A)
_ExtremeNetFlowGroupSourceIp_Type=IpAddress
_ExtremeNetFlowGroupSourceIp_Object=MibTableColumn
extremeNetFlowGroupSourceIp=_ExtremeNetFlowGroupSourceIp_Object((1,3,6,1,4,1,1916,1,22,2,2,1,4),_ExtremeNetFlowGroupSourceIp_Type())
extremeNetFlowGroupSourceIp.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowGroupSourceIp.setStatus(_A)
_ExtremeNetFlowCollectorIpAddress_Type=IpAddress
_ExtremeNetFlowCollectorIpAddress_Object=MibTableColumn
extremeNetFlowCollectorIpAddress=_ExtremeNetFlowCollectorIpAddress_Object((1,3,6,1,4,1,1916,1,22,2,2,1,5),_ExtremeNetFlowCollectorIpAddress_Type())
extremeNetFlowCollectorIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowCollectorIpAddress.setStatus(_A)
class _ExtremeNetFlowCollectorUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeNetFlowCollectorUdpPort_Type.__name__=_C
_ExtremeNetFlowCollectorUdpPort_Object=MibTableColumn
extremeNetFlowCollectorUdpPort=_ExtremeNetFlowCollectorUdpPort_Object((1,3,6,1,4,1,1916,1,22,2,2,1,6),_ExtremeNetFlowCollectorUdpPort_Type())
extremeNetFlowCollectorUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowCollectorUdpPort.setStatus(_A)
_ExtremeNetFlowCollectorStatusUp_Type=TruthValue
_ExtremeNetFlowCollectorStatusUp_Object=MibTableColumn
extremeNetFlowCollectorStatusUp=_ExtremeNetFlowCollectorStatusUp_Object((1,3,6,1,4,1,1916,1,22,2,2,1,7),_ExtremeNetFlowCollectorStatusUp_Type())
extremeNetFlowCollectorStatusUp.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowCollectorStatusUp.setStatus(_A)
class _ExtremeNetFlowCollectorDowntime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeNetFlowCollectorDowntime_Type.__name__=_C
_ExtremeNetFlowCollectorDowntime_Object=MibTableColumn
extremeNetFlowCollectorDowntime=_ExtremeNetFlowCollectorDowntime_Object((1,3,6,1,4,1,1916,1,22,2,2,1,8),_ExtremeNetFlowCollectorDowntime_Type())
extremeNetFlowCollectorDowntime.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowCollectorDowntime.setStatus(_A)
class _ExtremeNetFlowCollectorPacketsTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeNetFlowCollectorPacketsTx_Type.__name__=_C
_ExtremeNetFlowCollectorPacketsTx_Object=MibTableColumn
extremeNetFlowCollectorPacketsTx=_ExtremeNetFlowCollectorPacketsTx_Object((1,3,6,1,4,1,1916,1,22,2,2,1,9),_ExtremeNetFlowCollectorPacketsTx_Type())
extremeNetFlowCollectorPacketsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNetFlowCollectorPacketsTx.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'extremeNetFlow':extremeNetFlow,'extremeNetFlowConfigPort':extremeNetFlowConfigPort,'extremeNetFlowPortConfigTable':extremeNetFlowPortConfigTable,'extremeNetFlowPortConfigEntry':extremeNetFlowPortConfigEntry,_F:extremeNetFlowPortConfigPortIndex,'extremeNetFlowPortConfigEnabled':extremeNetFlowPortConfigEnabled,'extremeNetFlowPortConfigTimout':extremeNetFlowPortConfigTimout,'extremeNetFlowPortOverFlowPackets':extremeNetFlowPortOverFlowPackets,'extremeNetFlowPortFilterConfigTable':extremeNetFlowPortFilterConfigTable,'extremeNetFlowPortFilterConfigEntry':extremeNetFlowPortFilterConfigEntry,_G:extremeNetFlowPortConfigPortNumber,_H:extremeNetFlowPortConfigFilterEgress,_I:extremeNetFlowPortConfigFilterNumber,'extremeNetFlowPortEnabled':extremeNetFlowPortEnabled,'extremeNetFlowFilterEnabled':extremeNetFlowFilterEnabled,'extremeNetFlowDestIpAddress':extremeNetFlowDestIpAddress,'extremeNetFlowDestIpAddressMask':extremeNetFlowDestIpAddressMask,'extremeNetFlowSourceIpAddress':extremeNetFlowSourceIpAddress,'extremeNetFlowSourceIpAddressMask':extremeNetFlowSourceIpAddressMask,'extremeNetFlowDestPort':extremeNetFlowDestPort,'extremeNetFlowDestPortMask':extremeNetFlowDestPortMask,'extremeNetFlowSourcePort':extremeNetFlowSourcePort,'extremeNetFlowSourcePortMask':extremeNetFlowSourcePortMask,'extremeNetFlowProtocol':extremeNetFlowProtocol,'extremeNetFlowProtocolMask':extremeNetFlowProtocolMask,'extremeNetFlowFilterGroupNumber':extremeNetFlowFilterGroupNumber,'extremeNetFlowMatchAllFlag':extremeNetFlowMatchAllFlag,'extremeNetFlowMatchNoneFlag':extremeNetFlowMatchNoneFlag,'extremeNetFlowConfigGroup':extremeNetFlowConfigGroup,'extremeNetFlowGroupCollectorTable':extremeNetFlowGroupCollectorTable,'extremeNetFlowGroupCollectorEntry':extremeNetFlowGroupCollectorEntry,_J:extremeNetFlowGroupNumber,_K:extremeNetFlowCollectorId,'extremeNetFlowGroupPingEnabled':extremeNetFlowGroupPingEnabled,'extremeNetFlowGroupSourceIp':extremeNetFlowGroupSourceIp,'extremeNetFlowCollectorIpAddress':extremeNetFlowCollectorIpAddress,'extremeNetFlowCollectorUdpPort':extremeNetFlowCollectorUdpPort,'extremeNetFlowCollectorStatusUp':extremeNetFlowCollectorStatusUp,'extremeNetFlowCollectorDowntime':extremeNetFlowCollectorDowntime,'extremeNetFlowCollectorPacketsTx':extremeNetFlowCollectorPacketsTx})