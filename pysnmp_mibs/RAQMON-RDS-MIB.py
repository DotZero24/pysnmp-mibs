_u='raqmonDsPayloadGroup'
_t='raqmonDsNotificationGroup'
_s='raqmonDsByeNotification'
_r='raqmonDsDynamicNotification'
_q='raqmonDsStaticNotification'
_p='raqmonDsMemoryUtilization'
_o='raqmonDsCpuUtilization'
_n='raqmonDsDestinationDscp'
_m='raqmonDsDestinationLayer2Priority'
_l='raqmonDsSourceDscp'
_k='raqmonDsSourceLayer2Priority'
_j='raqmonDsReceiverPayloadType'
_i='raqmonDsSourcePayloadType'
_h='raqmonDsDiscardsFraction'
_g='raqmonDsCumulativeDiscards'
_f='raqmonDsPacketLossFraction'
_e='raqmonDsCumulativePacketLoss'
_d='raqmonDsTotalOctetsSent'
_c='raqmonDsTotalOctetsReceived'
_b='raqmonDsTotalPacketsSent'
_a='raqmonDsIPPacketDelayVariation'
_Z='raqmonDsInterArrivalJitter'
_Y='raqmonDsApplicationDelay'
_X='raqmonDsOneWayEndToEndNetDelay'
_W='raqmonDsRoundTripEndToEndNetDelay'
_V='raqmonDsSessionSetupStatus'
_U='raqmonDsSessionDuration'
_T='raqmonDsSessionSetupDelay'
_S='raqmonDsSessionSetupDateTime'
_R='raqmonDsReceiverDevicePort'
_Q='raqmonDsDataSourceDevicePort'
_P='percent'
_O='percentage of packets sent'
_N='octets'
_M='raqmonDsPeerAddr'
_L='raqmonDsPeerAddrType'
_K='raqmonDsRCN'
_J='raqmonDsDSRC'
_I='raqmonDsTotalPacketsReceived'
_H='raqmonDsAppName'
_G='packets'
_F='not-accessible'
_E='milliseconds'
_D='Unsigned32'
_C='accessible-for-notify'
_B='current'
_A='RAQMON-RDS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Dscp,=mibBuilder.importSymbols('DIFFSERV-DSCP-TC','Dscp')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
rmon,=mibBuilder.importSymbols('RMON-MIB','rmon')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
raqmonDsMIB=ModuleIdentity((1,3,6,1,2,1,16,32))
if mibBuilder.loadTexts:raqmonDsMIB.setRevisions(('2006-10-10 00:00',))
_RaqmonDsNotifications_ObjectIdentity=ObjectIdentity
raqmonDsNotifications=_RaqmonDsNotifications_ObjectIdentity((1,3,6,1,2,1,16,32,0))
_RaqmonDsMIBObjects_ObjectIdentity=ObjectIdentity
raqmonDsMIBObjects=_RaqmonDsMIBObjects_ObjectIdentity((1,3,6,1,2,1,16,32,1))
_RaqmonDsNotificationTable_Object=MibTable
raqmonDsNotificationTable=_RaqmonDsNotificationTable_Object((1,3,6,1,2,1,16,32,1,1))
if mibBuilder.loadTexts:raqmonDsNotificationTable.setStatus(_B)
_RaqmonDsNotificationEntry_Object=MibTableRow
raqmonDsNotificationEntry=_RaqmonDsNotificationEntry_Object((1,3,6,1,2,1,16,32,1,1,1))
raqmonDsNotificationEntry.setIndexNames((0,_A,_J),(0,_A,_K),(0,_A,_L),(0,_A,_M))
if mibBuilder.loadTexts:raqmonDsNotificationEntry.setStatus(_B)
_RaqmonDsDSRC_Type=Unsigned32
_RaqmonDsDSRC_Object=MibTableColumn
raqmonDsDSRC=_RaqmonDsDSRC_Object((1,3,6,1,2,1,16,32,1,1,1,1),_RaqmonDsDSRC_Type())
raqmonDsDSRC.setMaxAccess(_F)
if mibBuilder.loadTexts:raqmonDsDSRC.setStatus(_B)
class _RaqmonDsRCN_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_RaqmonDsRCN_Type.__name__=_D
_RaqmonDsRCN_Object=MibTableColumn
raqmonDsRCN=_RaqmonDsRCN_Object((1,3,6,1,2,1,16,32,1,1,1,2),_RaqmonDsRCN_Type())
raqmonDsRCN.setMaxAccess(_F)
if mibBuilder.loadTexts:raqmonDsRCN.setStatus(_B)
_RaqmonDsPeerAddrType_Type=InetAddressType
_RaqmonDsPeerAddrType_Object=MibTableColumn
raqmonDsPeerAddrType=_RaqmonDsPeerAddrType_Object((1,3,6,1,2,1,16,32,1,1,1,3),_RaqmonDsPeerAddrType_Type())
raqmonDsPeerAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:raqmonDsPeerAddrType.setStatus(_B)
_RaqmonDsPeerAddr_Type=InetAddress
_RaqmonDsPeerAddr_Object=MibTableColumn
raqmonDsPeerAddr=_RaqmonDsPeerAddr_Object((1,3,6,1,2,1,16,32,1,1,1,4),_RaqmonDsPeerAddr_Type())
raqmonDsPeerAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:raqmonDsPeerAddr.setStatus(_B)
_RaqmonDsAppName_Type=SnmpAdminString
_RaqmonDsAppName_Object=MibTableColumn
raqmonDsAppName=_RaqmonDsAppName_Object((1,3,6,1,2,1,16,32,1,1,1,5),_RaqmonDsAppName_Type())
raqmonDsAppName.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsAppName.setStatus(_B)
_RaqmonDsDataSourceDevicePort_Type=InetPortNumber
_RaqmonDsDataSourceDevicePort_Object=MibTableColumn
raqmonDsDataSourceDevicePort=_RaqmonDsDataSourceDevicePort_Object((1,3,6,1,2,1,16,32,1,1,1,6),_RaqmonDsDataSourceDevicePort_Type())
raqmonDsDataSourceDevicePort.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsDataSourceDevicePort.setStatus(_B)
_RaqmonDsReceiverDevicePort_Type=InetPortNumber
_RaqmonDsReceiverDevicePort_Object=MibTableColumn
raqmonDsReceiverDevicePort=_RaqmonDsReceiverDevicePort_Object((1,3,6,1,2,1,16,32,1,1,1,7),_RaqmonDsReceiverDevicePort_Type())
raqmonDsReceiverDevicePort.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsReceiverDevicePort.setStatus(_B)
_RaqmonDsSessionSetupDateTime_Type=DateAndTime
_RaqmonDsSessionSetupDateTime_Object=MibTableColumn
raqmonDsSessionSetupDateTime=_RaqmonDsSessionSetupDateTime_Object((1,3,6,1,2,1,16,32,1,1,1,8),_RaqmonDsSessionSetupDateTime_Type())
raqmonDsSessionSetupDateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsSessionSetupDateTime.setStatus(_B)
class _RaqmonDsSessionSetupDelay_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RaqmonDsSessionSetupDelay_Type.__name__=_D
_RaqmonDsSessionSetupDelay_Object=MibTableColumn
raqmonDsSessionSetupDelay=_RaqmonDsSessionSetupDelay_Object((1,3,6,1,2,1,16,32,1,1,1,9),_RaqmonDsSessionSetupDelay_Type())
raqmonDsSessionSetupDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsSessionSetupDelay.setStatus(_B)
if mibBuilder.loadTexts:raqmonDsSessionSetupDelay.setUnits(_E)
_RaqmonDsSessionDuration_Type=Unsigned32
_RaqmonDsSessionDuration_Object=MibTableColumn
raqmonDsSessionDuration=_RaqmonDsSessionDuration_Object((1,3,6,1,2,1,16,32,1,1,1,10),_RaqmonDsSessionDuration_Type())
raqmonDsSessionDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsSessionDuration.setStatus(_B)
if mibBuilder.loadTexts:raqmonDsSessionDuration.setUnits('seconds')
_RaqmonDsSessionSetupStatus_Type=SnmpAdminString
_RaqmonDsSessionSetupStatus_Object=MibTableColumn
raqmonDsSessionSetupStatus=_RaqmonDsSessionSetupStatus_Object((1,3,6,1,2,1,16,32,1,1,1,11),_RaqmonDsSessionSetupStatus_Type())
raqmonDsSessionSetupStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsSessionSetupStatus.setStatus(_B)
_RaqmonDsRoundTripEndToEndNetDelay_Type=Unsigned32
_RaqmonDsRoundTripEndToEndNetDelay_Object=MibTableColumn
raqmonDsRoundTripEndToEndNetDelay=_RaqmonDsRoundTripEndToEndNetDelay_Object((1,3,6,1,2,1,16,32,1,1,1,12),_RaqmonDsRoundTripEndToEndNetDelay_Type())
raqmonDsRoundTripEndToEndNetDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsRoundTripEndToEndNetDelay.setStatus(_B)
if mibBuilder.loadTexts:raqmonDsRoundTripEndToEndNetDelay.setUnits(_E)
_RaqmonDsOneWayEndToEndNetDelay_Type=Unsigned32
_RaqmonDsOneWayEndToEndNetDelay_Object=MibTableColumn
raqmonDsOneWayEndToEndNetDelay=_RaqmonDsOneWayEndToEndNetDelay_Object((1,3,6,1,2,1,16,32,1,1,1,13),_RaqmonDsOneWayEndToEndNetDelay_Type())
raqmonDsOneWayEndToEndNetDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsOneWayEndToEndNetDelay.setStatus(_B)
if mibBuilder.loadTexts:raqmonDsOneWayEndToEndNetDelay.setUnits(_E)
class _RaqmonDsApplicationDelay_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RaqmonDsApplicationDelay_Type.__name__=_D
_RaqmonDsApplicationDelay_Object=MibTableColumn
raqmonDsApplicationDelay=_RaqmonDsApplicationDelay_Object((1,3,6,1,2,1,16,32,1,1,1,14),_RaqmonDsApplicationDelay_Type())
raqmonDsApplicationDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsApplicationDelay.setStatus(_B)
if mibBuilder.loadTexts:raqmonDsApplicationDelay.setUnits(_E)
class _RaqmonDsInterArrivalJitter_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RaqmonDsInterArrivalJitter_Type.__name__=_D
_RaqmonDsInterArrivalJitter_Object=MibTableColumn
raqmonDsInterArrivalJitter=_RaqmonDsInterArrivalJitter_Object((1,3,6,1,2,1,16,32,1,1,1,15),_RaqmonDsInterArrivalJitter_Type())
raqmonDsInterArrivalJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsInterArrivalJitter.setStatus(_B)
if mibBuilder.loadTexts:raqmonDsInterArrivalJitter.setUnits(_E)
class _RaqmonDsIPPacketDelayVariation_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RaqmonDsIPPacketDelayVariation_Type.__name__=_D
_RaqmonDsIPPacketDelayVariation_Object=MibTableColumn
raqmonDsIPPacketDelayVariation=_RaqmonDsIPPacketDelayVariation_Object((1,3,6,1,2,1,16,32,1,1,1,16),_RaqmonDsIPPacketDelayVariation_Type())
raqmonDsIPPacketDelayVariation.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsIPPacketDelayVariation.setStatus(_B)
if mibBuilder.loadTexts:raqmonDsIPPacketDelayVariation.setUnits(_E)
_RaqmonDsTotalPacketsReceived_Type=Counter32
_RaqmonDsTotalPacketsReceived_Object=MibTableColumn
raqmonDsTotalPacketsReceived=_RaqmonDsTotalPacketsReceived_Object((1,3,6,1,2,1,16,32,1,1,1,17),_RaqmonDsTotalPacketsReceived_Type())
raqmonDsTotalPacketsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsTotalPacketsReceived.setStatus(_B)
if mibBuilder.loadTexts:raqmonDsTotalPacketsReceived.setUnits(_G)
_RaqmonDsTotalPacketsSent_Type=Counter32
_RaqmonDsTotalPacketsSent_Object=MibTableColumn
raqmonDsTotalPacketsSent=_RaqmonDsTotalPacketsSent_Object((1,3,6,1,2,1,16,32,1,1,1,18),_RaqmonDsTotalPacketsSent_Type())
raqmonDsTotalPacketsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsTotalPacketsSent.setStatus(_B)
if mibBuilder.loadTexts:raqmonDsTotalPacketsSent.setUnits(_G)
_RaqmonDsTotalOctetsReceived_Type=Counter32
_RaqmonDsTotalOctetsReceived_Object=MibTableColumn
raqmonDsTotalOctetsReceived=_RaqmonDsTotalOctetsReceived_Object((1,3,6,1,2,1,16,32,1,1,1,19),_RaqmonDsTotalOctetsReceived_Type())
raqmonDsTotalOctetsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsTotalOctetsReceived.setStatus(_B)
if mibBuilder.loadTexts:raqmonDsTotalOctetsReceived.setUnits(_N)
_RaqmonDsTotalOctetsSent_Type=Counter32
_RaqmonDsTotalOctetsSent_Object=MibTableColumn
raqmonDsTotalOctetsSent=_RaqmonDsTotalOctetsSent_Object((1,3,6,1,2,1,16,32,1,1,1,20),_RaqmonDsTotalOctetsSent_Type())
raqmonDsTotalOctetsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsTotalOctetsSent.setStatus(_B)
if mibBuilder.loadTexts:raqmonDsTotalOctetsSent.setUnits(_N)
_RaqmonDsCumulativePacketLoss_Type=Counter32
_RaqmonDsCumulativePacketLoss_Object=MibTableColumn
raqmonDsCumulativePacketLoss=_RaqmonDsCumulativePacketLoss_Object((1,3,6,1,2,1,16,32,1,1,1,21),_RaqmonDsCumulativePacketLoss_Type())
raqmonDsCumulativePacketLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsCumulativePacketLoss.setStatus(_B)
if mibBuilder.loadTexts:raqmonDsCumulativePacketLoss.setUnits(_G)
class _RaqmonDsPacketLossFraction_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RaqmonDsPacketLossFraction_Type.__name__=_D
_RaqmonDsPacketLossFraction_Object=MibTableColumn
raqmonDsPacketLossFraction=_RaqmonDsPacketLossFraction_Object((1,3,6,1,2,1,16,32,1,1,1,22),_RaqmonDsPacketLossFraction_Type())
raqmonDsPacketLossFraction.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsPacketLossFraction.setStatus(_B)
if mibBuilder.loadTexts:raqmonDsPacketLossFraction.setUnits(_O)
_RaqmonDsCumulativeDiscards_Type=Counter32
_RaqmonDsCumulativeDiscards_Object=MibTableColumn
raqmonDsCumulativeDiscards=_RaqmonDsCumulativeDiscards_Object((1,3,6,1,2,1,16,32,1,1,1,23),_RaqmonDsCumulativeDiscards_Type())
raqmonDsCumulativeDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsCumulativeDiscards.setStatus(_B)
if mibBuilder.loadTexts:raqmonDsCumulativeDiscards.setUnits(_G)
class _RaqmonDsDiscardsFraction_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RaqmonDsDiscardsFraction_Type.__name__=_D
_RaqmonDsDiscardsFraction_Object=MibTableColumn
raqmonDsDiscardsFraction=_RaqmonDsDiscardsFraction_Object((1,3,6,1,2,1,16,32,1,1,1,24),_RaqmonDsDiscardsFraction_Type())
raqmonDsDiscardsFraction.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsDiscardsFraction.setStatus(_B)
if mibBuilder.loadTexts:raqmonDsDiscardsFraction.setUnits(_O)
class _RaqmonDsSourcePayloadType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_RaqmonDsSourcePayloadType_Type.__name__=_D
_RaqmonDsSourcePayloadType_Object=MibTableColumn
raqmonDsSourcePayloadType=_RaqmonDsSourcePayloadType_Object((1,3,6,1,2,1,16,32,1,1,1,25),_RaqmonDsSourcePayloadType_Type())
raqmonDsSourcePayloadType.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsSourcePayloadType.setStatus(_B)
class _RaqmonDsReceiverPayloadType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_RaqmonDsReceiverPayloadType_Type.__name__=_D
_RaqmonDsReceiverPayloadType_Object=MibTableColumn
raqmonDsReceiverPayloadType=_RaqmonDsReceiverPayloadType_Object((1,3,6,1,2,1,16,32,1,1,1,26),_RaqmonDsReceiverPayloadType_Type())
raqmonDsReceiverPayloadType.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsReceiverPayloadType.setStatus(_B)
class _RaqmonDsSourceLayer2Priority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RaqmonDsSourceLayer2Priority_Type.__name__=_D
_RaqmonDsSourceLayer2Priority_Object=MibTableColumn
raqmonDsSourceLayer2Priority=_RaqmonDsSourceLayer2Priority_Object((1,3,6,1,2,1,16,32,1,1,1,27),_RaqmonDsSourceLayer2Priority_Type())
raqmonDsSourceLayer2Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsSourceLayer2Priority.setStatus(_B)
_RaqmonDsSourceDscp_Type=Dscp
_RaqmonDsSourceDscp_Object=MibTableColumn
raqmonDsSourceDscp=_RaqmonDsSourceDscp_Object((1,3,6,1,2,1,16,32,1,1,1,28),_RaqmonDsSourceDscp_Type())
raqmonDsSourceDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsSourceDscp.setStatus(_B)
class _RaqmonDsDestinationLayer2Priority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RaqmonDsDestinationLayer2Priority_Type.__name__=_D
_RaqmonDsDestinationLayer2Priority_Object=MibTableColumn
raqmonDsDestinationLayer2Priority=_RaqmonDsDestinationLayer2Priority_Object((1,3,6,1,2,1,16,32,1,1,1,29),_RaqmonDsDestinationLayer2Priority_Type())
raqmonDsDestinationLayer2Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsDestinationLayer2Priority.setStatus(_B)
_RaqmonDsDestinationDscp_Type=Dscp
_RaqmonDsDestinationDscp_Object=MibTableColumn
raqmonDsDestinationDscp=_RaqmonDsDestinationDscp_Object((1,3,6,1,2,1,16,32,1,1,1,30),_RaqmonDsDestinationDscp_Type())
raqmonDsDestinationDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsDestinationDscp.setStatus(_B)
class _RaqmonDsCpuUtilization_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RaqmonDsCpuUtilization_Type.__name__=_D
_RaqmonDsCpuUtilization_Object=MibTableColumn
raqmonDsCpuUtilization=_RaqmonDsCpuUtilization_Object((1,3,6,1,2,1,16,32,1,1,1,31),_RaqmonDsCpuUtilization_Type())
raqmonDsCpuUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsCpuUtilization.setStatus(_B)
if mibBuilder.loadTexts:raqmonDsCpuUtilization.setUnits(_P)
class _RaqmonDsMemoryUtilization_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RaqmonDsMemoryUtilization_Type.__name__=_D
_RaqmonDsMemoryUtilization_Object=MibTableColumn
raqmonDsMemoryUtilization=_RaqmonDsMemoryUtilization_Object((1,3,6,1,2,1,16,32,1,1,1,32),_RaqmonDsMemoryUtilization_Type())
raqmonDsMemoryUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:raqmonDsMemoryUtilization.setStatus(_B)
if mibBuilder.loadTexts:raqmonDsMemoryUtilization.setUnits(_P)
_RaqmonDsConformance_ObjectIdentity=ObjectIdentity
raqmonDsConformance=_RaqmonDsConformance_ObjectIdentity((1,3,6,1,2,1,16,32,2))
_RaqmonDsCompliance_ObjectIdentity=ObjectIdentity
raqmonDsCompliance=_RaqmonDsCompliance_ObjectIdentity((1,3,6,1,2,1,16,32,2,1))
_RaqmonDsGroups_ObjectIdentity=ObjectIdentity
raqmonDsGroups=_RaqmonDsGroups_ObjectIdentity((1,3,6,1,2,1,16,32,2,2))
raqmonDsPayloadGroup=ObjectGroup((1,3,6,1,2,1,16,32,2,2,2))
raqmonDsPayloadGroup.setObjects(*((_A,_H),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_I),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:raqmonDsPayloadGroup.setStatus(_B)
raqmonDsStaticNotification=NotificationType((1,3,6,1,2,1,16,32,0,1))
raqmonDsStaticNotification.setObjects((_A,_H))
if mibBuilder.loadTexts:raqmonDsStaticNotification.setStatus(_B)
raqmonDsDynamicNotification=NotificationType((1,3,6,1,2,1,16,32,0,2))
raqmonDsDynamicNotification.setObjects((_A,_I))
if mibBuilder.loadTexts:raqmonDsDynamicNotification.setStatus(_B)
raqmonDsByeNotification=NotificationType((1,3,6,1,2,1,16,32,0,3))
raqmonDsByeNotification.setObjects((_A,_H))
if mibBuilder.loadTexts:raqmonDsByeNotification.setStatus(_B)
raqmonDsNotificationGroup=NotificationGroup((1,3,6,1,2,1,16,32,2,2,1))
raqmonDsNotificationGroup.setObjects(*((_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:raqmonDsNotificationGroup.setStatus(_B)
raqmonDsBasicCompliance=ModuleCompliance((1,3,6,1,2,1,16,32,2,1,1))
raqmonDsBasicCompliance.setObjects(*((_A,_t),(_A,_u)))
if mibBuilder.loadTexts:raqmonDsBasicCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'raqmonDsMIB':raqmonDsMIB,'raqmonDsNotifications':raqmonDsNotifications,_q:raqmonDsStaticNotification,_r:raqmonDsDynamicNotification,_s:raqmonDsByeNotification,'raqmonDsMIBObjects':raqmonDsMIBObjects,'raqmonDsNotificationTable':raqmonDsNotificationTable,'raqmonDsNotificationEntry':raqmonDsNotificationEntry,_J:raqmonDsDSRC,_K:raqmonDsRCN,_L:raqmonDsPeerAddrType,_M:raqmonDsPeerAddr,_H:raqmonDsAppName,_Q:raqmonDsDataSourceDevicePort,_R:raqmonDsReceiverDevicePort,_S:raqmonDsSessionSetupDateTime,_T:raqmonDsSessionSetupDelay,_U:raqmonDsSessionDuration,_V:raqmonDsSessionSetupStatus,_W:raqmonDsRoundTripEndToEndNetDelay,_X:raqmonDsOneWayEndToEndNetDelay,_Y:raqmonDsApplicationDelay,_Z:raqmonDsInterArrivalJitter,_a:raqmonDsIPPacketDelayVariation,_I:raqmonDsTotalPacketsReceived,_b:raqmonDsTotalPacketsSent,_c:raqmonDsTotalOctetsReceived,_d:raqmonDsTotalOctetsSent,_e:raqmonDsCumulativePacketLoss,_f:raqmonDsPacketLossFraction,_g:raqmonDsCumulativeDiscards,_h:raqmonDsDiscardsFraction,_i:raqmonDsSourcePayloadType,_j:raqmonDsReceiverPayloadType,_k:raqmonDsSourceLayer2Priority,_l:raqmonDsSourceDscp,_m:raqmonDsDestinationLayer2Priority,_n:raqmonDsDestinationDscp,_o:raqmonDsCpuUtilization,_p:raqmonDsMemoryUtilization,'raqmonDsConformance':raqmonDsConformance,'raqmonDsCompliance':raqmonDsCompliance,'raqmonDsBasicCompliance':raqmonDsBasicCompliance,'raqmonDsGroups':raqmonDsGroups,_t:raqmonDsNotificationGroup,_u:raqmonDsPayloadGroup})