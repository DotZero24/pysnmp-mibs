_S='zxAnQosDscp2CosMappingDscp'
_R='zxAnQosCos2DscpMappingCos'
_Q='trustDscpMap'
_P='remark'
_O='disable'
_N='enable'
_M='zxAnBrgPortConfProfileName'
_L='zxAnQosConfProfileName'
_K='ifIndex'
_J='IF-MIB'
_I='override'
_H='trust'
_G='not-accessible'
_F='read-write'
_E='ZTE-AN-QOS-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_J,_K)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention')
zxAn,=mibBuilder.importSymbols('ZTE-AN-TC-MIB','zxAn')
zxAnQosMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,21))
_ZxAnQosObjects_ObjectIdentity=ObjectIdentity
zxAnQosObjects=_ZxAnQosObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,21,1))
_ZxAnQosGlobal_ObjectIdentity=ObjectIdentity
zxAnQosGlobal=_ZxAnQosGlobal_ObjectIdentity((1,3,6,1,4,1,3902,1015,21,1,1))
_ZxAnInterfaceQosConfTable_Object=MibTable
zxAnInterfaceQosConfTable=_ZxAnInterfaceQosConfTable_Object((1,3,6,1,4,1,3902,1015,21,1,2))
if mibBuilder.loadTexts:zxAnInterfaceQosConfTable.setStatus(_A)
_ZxAnInterfaceQosConfEntry_Object=MibTableRow
zxAnInterfaceQosConfEntry=_ZxAnInterfaceQosConfEntry_Object((1,3,6,1,4,1,3902,1015,21,1,2,1))
zxAnInterfaceQosConfEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:zxAnInterfaceQosConfEntry.setStatus(_A)
class _ZxAnIfQosConfProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnIfQosConfProfileName_Type.__name__=_D
_ZxAnIfQosConfProfileName_Object=MibTableColumn
zxAnIfQosConfProfileName=_ZxAnIfQosConfProfileName_Object((1,3,6,1,4,1,3902,1015,21,1,2,1,1),_ZxAnIfQosConfProfileName_Type())
zxAnIfQosConfProfileName.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIfQosConfProfileName.setStatus(_A)
_ZxAnPortQosConfProfileTable_Object=MibTable
zxAnPortQosConfProfileTable=_ZxAnPortQosConfProfileTable_Object((1,3,6,1,4,1,3902,1015,21,1,3))
if mibBuilder.loadTexts:zxAnPortQosConfProfileTable.setStatus(_A)
_ZxAnPortQosConfProfileEntry_Object=MibTableRow
zxAnPortQosConfProfileEntry=_ZxAnPortQosConfProfileEntry_Object((1,3,6,1,4,1,3902,1015,21,1,3,1))
zxAnPortQosConfProfileEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:zxAnPortQosConfProfileEntry.setStatus(_A)
class _ZxAnQosConfProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnQosConfProfileName_Type.__name__=_D
_ZxAnQosConfProfileName_Object=MibTableColumn
zxAnQosConfProfileName=_ZxAnQosConfProfileName_Object((1,3,6,1,4,1,3902,1015,21,1,3,1,1),_ZxAnQosConfProfileName_Type())
zxAnQosConfProfileName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnQosConfProfileName.setStatus(_A)
class _ZxAnQosQueuesNumber_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2),ValueRangeConstraint(4,4),ValueRangeConstraint(8,8))
_ZxAnQosQueuesNumber_Type.__name__=_C
_ZxAnQosQueuesNumber_Object=MibTableColumn
zxAnQosQueuesNumber=_ZxAnQosQueuesNumber_Object((1,3,6,1,4,1,3902,1015,21,1,3,1,2),_ZxAnQosQueuesNumber_Type())
zxAnQosQueuesNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosQueuesNumber.setStatus(_A)
_ZxAnQosQueuesMaxSize_Type=ObjectIdentifier
_ZxAnQosQueuesMaxSize_Object=MibTableColumn
zxAnQosQueuesMaxSize=_ZxAnQosQueuesMaxSize_Object((1,3,6,1,4,1,3902,1015,21,1,3,1,3),_ZxAnQosQueuesMaxSize_Type())
zxAnQosQueuesMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosQueuesMaxSize.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosQueuesMaxSize.setUnits('bytes')
class _ZxAnQosQueueSchedAlgorithm_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sp',1),('wrr',2),('spAndWrr',3)))
_ZxAnQosQueueSchedAlgorithm_Type.__name__=_C
_ZxAnQosQueueSchedAlgorithm_Object=MibTableColumn
zxAnQosQueueSchedAlgorithm=_ZxAnQosQueueSchedAlgorithm_Object((1,3,6,1,4,1,3902,1015,21,1,3,1,4),_ZxAnQosQueueSchedAlgorithm_Type())
zxAnQosQueueSchedAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosQueueSchedAlgorithm.setStatus(_A)
_ZxAnQosQueuesWeight_Type=ObjectIdentifier
_ZxAnQosQueuesWeight_Object=MibTableColumn
zxAnQosQueuesWeight=_ZxAnQosQueuesWeight_Object((1,3,6,1,4,1,3902,1015,21,1,3,1,5),_ZxAnQosQueuesWeight_Type())
zxAnQosQueuesWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosQueuesWeight.setStatus(_A)
_ZxAnQosPriority2queue_Type=ObjectIdentifier
_ZxAnQosPriority2queue_Object=MibTableColumn
zxAnQosPriority2queue=_ZxAnQosPriority2queue_Object((1,3,6,1,4,1,3902,1015,21,1,3,1,6),_ZxAnQosPriority2queue_Type())
zxAnQosPriority2queue.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosPriority2queue.setStatus(_A)
_ZxAnQosPvc2Priority_Type=ObjectIdentifier
_ZxAnQosPvc2Priority_Object=MibTableColumn
zxAnQosPvc2Priority=_ZxAnQosPvc2Priority_Object((1,3,6,1,4,1,3902,1015,21,1,3,1,7),_ZxAnQosPvc2Priority_Type())
zxAnQosPvc2Priority.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosPvc2Priority.setStatus(_A)
_ZxAnQosPriorityRemarking_Type=ObjectIdentifier
_ZxAnQosPriorityRemarking_Object=MibTableColumn
zxAnQosPriorityRemarking=_ZxAnQosPriorityRemarking_Object((1,3,6,1,4,1,3902,1015,21,1,3,1,8),_ZxAnQosPriorityRemarking_Type())
zxAnQosPriorityRemarking.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosPriorityRemarking.setStatus(_A)
_ZxAnQosConfPrfRowStatus_Type=RowStatus
_ZxAnQosConfPrfRowStatus_Object=MibTableColumn
zxAnQosConfPrfRowStatus=_ZxAnQosConfPrfRowStatus_Object((1,3,6,1,4,1,3902,1015,21,1,3,1,9),_ZxAnQosConfPrfRowStatus_Type())
zxAnQosConfPrfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosConfPrfRowStatus.setStatus(_A)
_ZxAnBridgePortConfTable_Object=MibTable
zxAnBridgePortConfTable=_ZxAnBridgePortConfTable_Object((1,3,6,1,4,1,3902,1015,21,1,4))
if mibBuilder.loadTexts:zxAnBridgePortConfTable.setStatus(_A)
_ZxAnBridgePortConfEntry_Object=MibTableRow
zxAnBridgePortConfEntry=_ZxAnBridgePortConfEntry_Object((1,3,6,1,4,1,3902,1015,21,1,4,1))
zxAnBridgePortConfEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:zxAnBridgePortConfEntry.setStatus(_A)
class _ZxAnBridgePortConfProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnBridgePortConfProfileName_Type.__name__=_D
_ZxAnBridgePortConfProfileName_Object=MibTableColumn
zxAnBridgePortConfProfileName=_ZxAnBridgePortConfProfileName_Object((1,3,6,1,4,1,3902,1015,21,1,4,1,1),_ZxAnBridgePortConfProfileName_Type())
zxAnBridgePortConfProfileName.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnBridgePortConfProfileName.setStatus(_A)
_ZxAnBridgePortConfProfileTable_Object=MibTable
zxAnBridgePortConfProfileTable=_ZxAnBridgePortConfProfileTable_Object((1,3,6,1,4,1,3902,1015,21,1,5))
if mibBuilder.loadTexts:zxAnBridgePortConfProfileTable.setStatus(_A)
_ZxAnBridgePortConfProfileEntry_Object=MibTableRow
zxAnBridgePortConfProfileEntry=_ZxAnBridgePortConfProfileEntry_Object((1,3,6,1,4,1,3902,1015,21,1,5,1))
zxAnBridgePortConfProfileEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:zxAnBridgePortConfProfileEntry.setStatus(_A)
class _ZxAnBrgPortConfProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnBrgPortConfProfileName_Type.__name__=_D
_ZxAnBrgPortConfProfileName_Object=MibTableColumn
zxAnBrgPortConfProfileName=_ZxAnBrgPortConfProfileName_Object((1,3,6,1,4,1,3902,1015,21,1,5,1,1),_ZxAnBrgPortConfProfileName_Type())
zxAnBrgPortConfProfileName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnBrgPortConfProfileName.setStatus(_A)
class _ZxAnBrgPortDefaultPriorityCvlan_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnBrgPortDefaultPriorityCvlan_Type.__name__=_C
_ZxAnBrgPortDefaultPriorityCvlan_Object=MibTableColumn
zxAnBrgPortDefaultPriorityCvlan=_ZxAnBrgPortDefaultPriorityCvlan_Object((1,3,6,1,4,1,3902,1015,21,1,5,1,2),_ZxAnBrgPortDefaultPriorityCvlan_Type())
zxAnBrgPortDefaultPriorityCvlan.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgPortDefaultPriorityCvlan.setStatus(_A)
class _ZxAnBrgPortPriorityOvrideCvlan_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnBrgPortPriorityOvrideCvlan_Type.__name__=_C
_ZxAnBrgPortPriorityOvrideCvlan_Object=MibTableColumn
zxAnBrgPortPriorityOvrideCvlan=_ZxAnBrgPortPriorityOvrideCvlan_Object((1,3,6,1,4,1,3902,1015,21,1,5,1,3),_ZxAnBrgPortPriorityOvrideCvlan_Type())
zxAnBrgPortPriorityOvrideCvlan.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgPortPriorityOvrideCvlan.setStatus(_A)
class _ZxAnBrgPortPriorityOvrideSvlan_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnBrgPortPriorityOvrideSvlan_Type.__name__=_C
_ZxAnBrgPortPriorityOvrideSvlan_Object=MibTableColumn
zxAnBrgPortPriorityOvrideSvlan=_ZxAnBrgPortPriorityOvrideSvlan_Object((1,3,6,1,4,1,3902,1015,21,1,5,1,4),_ZxAnBrgPortPriorityOvrideSvlan_Type())
zxAnBrgPortPriorityOvrideSvlan.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgPortPriorityOvrideSvlan.setStatus(_A)
class _ZxAnBrgPortPriorityTrustCvlan_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('mapToDscp',2),(_I,3),('mapFromDscp',4)))
_ZxAnBrgPortPriorityTrustCvlan_Type.__name__=_C
_ZxAnBrgPortPriorityTrustCvlan_Object=MibTableColumn
zxAnBrgPortPriorityTrustCvlan=_ZxAnBrgPortPriorityTrustCvlan_Object((1,3,6,1,4,1,3902,1015,21,1,5,1,5),_ZxAnBrgPortPriorityTrustCvlan_Type())
zxAnBrgPortPriorityTrustCvlan.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgPortPriorityTrustCvlan.setStatus(_A)
class _ZxAnBrgPortPriorityTrustSvlan_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),('copyFromCvlan',2)))
_ZxAnBrgPortPriorityTrustSvlan_Type.__name__=_C
_ZxAnBrgPortPriorityTrustSvlan_Object=MibTableColumn
zxAnBrgPortPriorityTrustSvlan=_ZxAnBrgPortPriorityTrustSvlan_Object((1,3,6,1,4,1,3902,1015,21,1,5,1,6),_ZxAnBrgPortPriorityTrustSvlan_Type())
zxAnBrgPortPriorityTrustSvlan.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgPortPriorityTrustSvlan.setStatus(_A)
class _ZxAnBrgPortPriorityRemarkEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_ZxAnBrgPortPriorityRemarkEnable_Type.__name__=_C
_ZxAnBrgPortPriorityRemarkEnable_Object=MibTableColumn
zxAnBrgPortPriorityRemarkEnable=_ZxAnBrgPortPriorityRemarkEnable_Object((1,3,6,1,4,1,3902,1015,21,1,5,1,7),_ZxAnBrgPortPriorityRemarkEnable_Type())
zxAnBrgPortPriorityRemarkEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgPortPriorityRemarkEnable.setStatus(_A)
class _ZxAnBrgPortPriorityFilterEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_ZxAnBrgPortPriorityFilterEnable_Type.__name__=_C
_ZxAnBrgPortPriorityFilterEnable_Object=MibTableColumn
zxAnBrgPortPriorityFilterEnable=_ZxAnBrgPortPriorityFilterEnable_Object((1,3,6,1,4,1,3902,1015,21,1,5,1,8),_ZxAnBrgPortPriorityFilterEnable_Type())
zxAnBrgPortPriorityFilterEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgPortPriorityFilterEnable.setStatus(_A)
class _ZxAnBrgPortRateLimitUp_Type(Integer32):defaultValue=12200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12200))
_ZxAnBrgPortRateLimitUp_Type.__name__=_C
_ZxAnBrgPortRateLimitUp_Object=MibTableColumn
zxAnBrgPortRateLimitUp=_ZxAnBrgPortRateLimitUp_Object((1,3,6,1,4,1,3902,1015,21,1,5,1,9),_ZxAnBrgPortRateLimitUp_Type())
zxAnBrgPortRateLimitUp.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgPortRateLimitUp.setStatus(_A)
if mibBuilder.loadTexts:zxAnBrgPortRateLimitUp.setUnits('kbps')
class _ZxAnBrgPortRateLimitDown_Type(Integer32):defaultValue=32640;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32640))
_ZxAnBrgPortRateLimitDown_Type.__name__=_C
_ZxAnBrgPortRateLimitDown_Object=MibTableColumn
zxAnBrgPortRateLimitDown=_ZxAnBrgPortRateLimitDown_Object((1,3,6,1,4,1,3902,1015,21,1,5,1,10),_ZxAnBrgPortRateLimitDown_Type())
zxAnBrgPortRateLimitDown.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgPortRateLimitDown.setStatus(_A)
if mibBuilder.loadTexts:zxAnBrgPortRateLimitDown.setUnits('kbps')
_ZxAnBrgPortConfPrfRowStatus_Type=RowStatus
_ZxAnBrgPortConfPrfRowStatus_Object=MibTableColumn
zxAnBrgPortConfPrfRowStatus=_ZxAnBrgPortConfPrfRowStatus_Object((1,3,6,1,4,1,3902,1015,21,1,5,1,11),_ZxAnBrgPortConfPrfRowStatus_Type())
zxAnBrgPortConfPrfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgPortConfPrfRowStatus.setStatus(_A)
class _ZxAnBrgPortDefaultPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnBrgPortDefaultPriority_Type.__name__=_C
_ZxAnBrgPortDefaultPriority_Object=MibTableColumn
zxAnBrgPortDefaultPriority=_ZxAnBrgPortDefaultPriority_Object((1,3,6,1,4,1,3902,1015,21,1,5,1,12),_ZxAnBrgPortDefaultPriority_Type())
zxAnBrgPortDefaultPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgPortDefaultPriority.setStatus(_A)
class _ZxAnBrgPortPrioritySetMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_I,2),(_P,3),(_Q,4)))
_ZxAnBrgPortPrioritySetMode_Type.__name__=_C
_ZxAnBrgPortPrioritySetMode_Object=MibTableColumn
zxAnBrgPortPrioritySetMode=_ZxAnBrgPortPrioritySetMode_Object((1,3,6,1,4,1,3902,1015,21,1,5,1,13),_ZxAnBrgPortPrioritySetMode_Type())
zxAnBrgPortPrioritySetMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgPortPrioritySetMode.setStatus(_A)
class _ZxAnBrgPortPrioritySetModeCvlan_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_I,2),(_P,3),(_Q,4)))
_ZxAnBrgPortPrioritySetModeCvlan_Type.__name__=_C
_ZxAnBrgPortPrioritySetModeCvlan_Object=MibTableColumn
zxAnBrgPortPrioritySetModeCvlan=_ZxAnBrgPortPrioritySetModeCvlan_Object((1,3,6,1,4,1,3902,1015,21,1,5,1,14),_ZxAnBrgPortPrioritySetModeCvlan_Type())
zxAnBrgPortPrioritySetModeCvlan.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgPortPrioritySetModeCvlan.setStatus(_A)
class _ZxAnBrgPortDSCPSetMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('trustQosMap',2)))
_ZxAnBrgPortDSCPSetMode_Type.__name__=_C
_ZxAnBrgPortDSCPSetMode_Object=MibTableColumn
zxAnBrgPortDSCPSetMode=_ZxAnBrgPortDSCPSetMode_Object((1,3,6,1,4,1,3902,1015,21,1,5,1,15),_ZxAnBrgPortDSCPSetMode_Type())
zxAnBrgPortDSCPSetMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBrgPortDSCPSetMode.setStatus(_A)
_ZxAnQosCos2DscpMappingTable_Object=MibTable
zxAnQosCos2DscpMappingTable=_ZxAnQosCos2DscpMappingTable_Object((1,3,6,1,4,1,3902,1015,21,1,6))
if mibBuilder.loadTexts:zxAnQosCos2DscpMappingTable.setStatus(_A)
_ZxAnQosCos2DscpMappingEntry_Object=MibTableRow
zxAnQosCos2DscpMappingEntry=_ZxAnQosCos2DscpMappingEntry_Object((1,3,6,1,4,1,3902,1015,21,1,6,1))
zxAnQosCos2DscpMappingEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:zxAnQosCos2DscpMappingEntry.setStatus(_A)
class _ZxAnQosCos2DscpMappingCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnQosCos2DscpMappingCos_Type.__name__=_C
_ZxAnQosCos2DscpMappingCos_Object=MibTableColumn
zxAnQosCos2DscpMappingCos=_ZxAnQosCos2DscpMappingCos_Object((1,3,6,1,4,1,3902,1015,21,1,6,1,1),_ZxAnQosCos2DscpMappingCos_Type())
zxAnQosCos2DscpMappingCos.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnQosCos2DscpMappingCos.setStatus(_A)
class _ZxAnQosCos2DscpMappingDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_ZxAnQosCos2DscpMappingDscp_Type.__name__=_C
_ZxAnQosCos2DscpMappingDscp_Object=MibTableColumn
zxAnQosCos2DscpMappingDscp=_ZxAnQosCos2DscpMappingDscp_Object((1,3,6,1,4,1,3902,1015,21,1,6,1,2),_ZxAnQosCos2DscpMappingDscp_Type())
zxAnQosCos2DscpMappingDscp.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnQosCos2DscpMappingDscp.setStatus(_A)
_ZxAnQosDscp2CosMappingTable_Object=MibTable
zxAnQosDscp2CosMappingTable=_ZxAnQosDscp2CosMappingTable_Object((1,3,6,1,4,1,3902,1015,21,1,7))
if mibBuilder.loadTexts:zxAnQosDscp2CosMappingTable.setStatus(_A)
_ZxAnQosDscp2CosMappingEntry_Object=MibTableRow
zxAnQosDscp2CosMappingEntry=_ZxAnQosDscp2CosMappingEntry_Object((1,3,6,1,4,1,3902,1015,21,1,7,1))
zxAnQosDscp2CosMappingEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:zxAnQosDscp2CosMappingEntry.setStatus(_A)
class _ZxAnQosDscp2CosMappingDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_ZxAnQosDscp2CosMappingDscp_Type.__name__=_C
_ZxAnQosDscp2CosMappingDscp_Object=MibTableColumn
zxAnQosDscp2CosMappingDscp=_ZxAnQosDscp2CosMappingDscp_Object((1,3,6,1,4,1,3902,1015,21,1,7,1,1),_ZxAnQosDscp2CosMappingDscp_Type())
zxAnQosDscp2CosMappingDscp.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnQosDscp2CosMappingDscp.setStatus(_A)
class _ZxAnQosDscp2CosMappingCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnQosDscp2CosMappingCos_Type.__name__=_C
_ZxAnQosDscp2CosMappingCos_Object=MibTableColumn
zxAnQosDscp2CosMappingCos=_ZxAnQosDscp2CosMappingCos_Object((1,3,6,1,4,1,3902,1015,21,1,7,1,2),_ZxAnQosDscp2CosMappingCos_Type())
zxAnQosDscp2CosMappingCos.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnQosDscp2CosMappingCos.setStatus(_A)
_ZxAnQosTrapObjects_ObjectIdentity=ObjectIdentity
zxAnQosTrapObjects=_ZxAnQosTrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,21,2))
mibBuilder.exportSymbols(_E,**{'zxAnQosMib':zxAnQosMib,'zxAnQosObjects':zxAnQosObjects,'zxAnQosGlobal':zxAnQosGlobal,'zxAnInterfaceQosConfTable':zxAnInterfaceQosConfTable,'zxAnInterfaceQosConfEntry':zxAnInterfaceQosConfEntry,'zxAnIfQosConfProfileName':zxAnIfQosConfProfileName,'zxAnPortQosConfProfileTable':zxAnPortQosConfProfileTable,'zxAnPortQosConfProfileEntry':zxAnPortQosConfProfileEntry,_L:zxAnQosConfProfileName,'zxAnQosQueuesNumber':zxAnQosQueuesNumber,'zxAnQosQueuesMaxSize':zxAnQosQueuesMaxSize,'zxAnQosQueueSchedAlgorithm':zxAnQosQueueSchedAlgorithm,'zxAnQosQueuesWeight':zxAnQosQueuesWeight,'zxAnQosPriority2queue':zxAnQosPriority2queue,'zxAnQosPvc2Priority':zxAnQosPvc2Priority,'zxAnQosPriorityRemarking':zxAnQosPriorityRemarking,'zxAnQosConfPrfRowStatus':zxAnQosConfPrfRowStatus,'zxAnBridgePortConfTable':zxAnBridgePortConfTable,'zxAnBridgePortConfEntry':zxAnBridgePortConfEntry,'zxAnBridgePortConfProfileName':zxAnBridgePortConfProfileName,'zxAnBridgePortConfProfileTable':zxAnBridgePortConfProfileTable,'zxAnBridgePortConfProfileEntry':zxAnBridgePortConfProfileEntry,_M:zxAnBrgPortConfProfileName,'zxAnBrgPortDefaultPriorityCvlan':zxAnBrgPortDefaultPriorityCvlan,'zxAnBrgPortPriorityOvrideCvlan':zxAnBrgPortPriorityOvrideCvlan,'zxAnBrgPortPriorityOvrideSvlan':zxAnBrgPortPriorityOvrideSvlan,'zxAnBrgPortPriorityTrustCvlan':zxAnBrgPortPriorityTrustCvlan,'zxAnBrgPortPriorityTrustSvlan':zxAnBrgPortPriorityTrustSvlan,'zxAnBrgPortPriorityRemarkEnable':zxAnBrgPortPriorityRemarkEnable,'zxAnBrgPortPriorityFilterEnable':zxAnBrgPortPriorityFilterEnable,'zxAnBrgPortRateLimitUp':zxAnBrgPortRateLimitUp,'zxAnBrgPortRateLimitDown':zxAnBrgPortRateLimitDown,'zxAnBrgPortConfPrfRowStatus':zxAnBrgPortConfPrfRowStatus,'zxAnBrgPortDefaultPriority':zxAnBrgPortDefaultPriority,'zxAnBrgPortPrioritySetMode':zxAnBrgPortPrioritySetMode,'zxAnBrgPortPrioritySetModeCvlan':zxAnBrgPortPrioritySetModeCvlan,'zxAnBrgPortDSCPSetMode':zxAnBrgPortDSCPSetMode,'zxAnQosCos2DscpMappingTable':zxAnQosCos2DscpMappingTable,'zxAnQosCos2DscpMappingEntry':zxAnQosCos2DscpMappingEntry,_R:zxAnQosCos2DscpMappingCos,'zxAnQosCos2DscpMappingDscp':zxAnQosCos2DscpMappingDscp,'zxAnQosDscp2CosMappingTable':zxAnQosDscp2CosMappingTable,'zxAnQosDscp2CosMappingEntry':zxAnQosDscp2CosMappingEntry,_S:zxAnQosDscp2CosMappingDscp,'zxAnQosDscp2CosMappingCos':zxAnQosDscp2CosMappingCos,'zxAnQosTrapObjects':zxAnQosTrapObjects})