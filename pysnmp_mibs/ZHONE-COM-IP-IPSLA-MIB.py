_AQ='zhoneIpSLAPathStatByIntervalGroup'
_AP='zhoneIpSLANotificationGroup'
_AO='zhoneIpSLAPathStatByCOSGroup'
_AN='zhoneIpSLAPathConnectGroup'
_AM='zhoneIpSLAStaticPathGroup'
_AL='zhoneIpSLACOSMapGroup'
_AK='zhoneIpSLACosActionGroup'
_AJ='zhoneIpSLAGlobalsGroup'
_AI='zhoneIpSLAJitterClearTrap'
_AH='zhoneIpSLALatencyClearTrap'
_AG='zhoneIpSLATimeoutClearTrap'
_AF='zhoneIpSLAJitterTrap'
_AE='zhoneIpSLALatencyTrap'
_AD='zhoneIpSLATimeoutTrap'
_AC='zhoneIpSLAPathStatByIntervalDroppedResp'
_AB='zhoneIpSLAPathStatByIntervalMaxRTT'
_AA='zhoneIpSLAPathStatByIntervalAvgRTT'
_A9='zhoneIpSLAPathStatByIntervalMinRTT'
_A8='zhoneIpSLAPathStatByIntervalStatus'
_A7='zhoneIpSLAPathStatByIntervalDateTime'
_A6='zhoneIpSLAPathStatByCOSLastRTT'
_A5='zhoneIpSLAPathStatByCOSStatus'
_A4='zhoneIpSLAPathConnectLastCosActionIndex'
_A3='zhoneIpSLAPathConnectCosMismatch'
_A2='zhoneIpSLAPathConnectPollType'
_A1='zhoneIpSLAPathConnectUpTime'
_A0='zhoneIpSLAPathConnectDiscoveryType'
_z='zhoneIpSLAPathConnectStatus'
_y='zhoneIpSLAPathConnectDevType'
_x='zhoneIpSLAPathConnectDevName'
_w='zhoneIpSLAStaticPathRowstatus'
_v='zhoneIpSLAStaticPathState'
_u='zhoneIpSLAStaticPathForwarding'
_t='zhoneIpSLACosMapCosActionIndex'
_s='zhoneIpSLACosActionPacketSize'
_r='zhoneIpSLACosActionMetrics'
_q='zhoneIpSLACosActionJitterClrThresh'
_p='zhoneIpSLACosActionLatencyClrThresh'
_o='zhoneIpSLACosActionTimeoutClrThresh'
_n='zhoneIpSLACosActionTrapOnError'
_m='zhoneIpSLAGlobalPollInterval'
_l='zhoneIpSLAGlobalEnable'
_k='zhoneIpSLAPathStatByIntervalTargetIP'
_j='zhoneIpSLAPathStatByIntervalRdIndex'
_i='zhoneIpSLAPathStatByIntervalCosActIndex'
_h='zhoneIpSLAPathStatByIntervalIndex'
_g='inactive'
_f='active'
_e='zhoneIpSLAPathStatByCOSCosActIndex'
_d='zhoneIpSLAPathConnectEndpointIP'
_c='zhoneIpSLAStaticPathTargetIP'
_b='zhoneIpSLAStaticPathRdIndex'
_a='zhoneIpSLACosMapDscpIndex'
_Z='zhoneIpSLACosActionIndex'
_Y='seconds'
_X='zhoneIpSLAPathStatByCOSDroppedResp'
_W='zhoneIpSLAPathStatByCOSMaxRTT'
_V='zhoneIpSLAPathStatByCOSAvgRTT'
_U='zhoneIpSLAPathStatByCOSMinRTT'
_T='zhoneIpSLACosActionJitterErrThresh'
_S='zhoneIpSLACosActionLatencyErrThresh'
_R='zhoneIpSLACosActionTimeoutErrThresh'
_Q='read-create'
_P='rdIndex'
_O='ZhoneRDIndex'
_N='ZHONE-COM-IP-RD-MIB'
_M='OctetString'
_L='disabled'
_K='enabled'
_J='zhoneIpSLAPathConnectSrcIP'
_I='zhoneIpSLACosActionName'
_H='zhoneIpSLAPathStatByCOSTargetIP'
_G='milliseconds'
_F='not-accessible'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='current'
_A='ZHONE-COM-IP-IPSLA-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifName,=mibBuilder.importSymbols('IF-MIB','ifName')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention')
ZhoneRDIndex,rdIndex=mibBuilder.importSymbols(_N,_O,_P)
zhoneIp,=mibBuilder.importSymbols('Zhone','zhoneIp')
zhoneIpSLA=ModuleIdentity((1,3,6,1,4,1,5504,4,1,21))
if mibBuilder.loadTexts:zhoneIpSLA.setRevisions(('2007-06-05 07:16','2006-11-16 10:48','2006-11-03 07:57'))
_ZhoneIpSLAMibObjects_ObjectIdentity=ObjectIdentity
zhoneIpSLAMibObjects=_ZhoneIpSLAMibObjects_ObjectIdentity((1,3,6,1,4,1,5504,4,1,21,1))
class _ZhoneIpSLAGlobalEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_ZhoneIpSLAGlobalEnable_Type.__name__=_C
_ZhoneIpSLAGlobalEnable_Object=MibScalar
zhoneIpSLAGlobalEnable=_ZhoneIpSLAGlobalEnable_Object((1,3,6,1,4,1,5504,4,1,21,1,1),_ZhoneIpSLAGlobalEnable_Type())
zhoneIpSLAGlobalEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneIpSLAGlobalEnable.setStatus(_B)
class _ZhoneIpSLAGlobalPollInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,3600))
_ZhoneIpSLAGlobalPollInterval_Type.__name__=_C
_ZhoneIpSLAGlobalPollInterval_Object=MibScalar
zhoneIpSLAGlobalPollInterval=_ZhoneIpSLAGlobalPollInterval_Object((1,3,6,1,4,1,5504,4,1,21,1,2),_ZhoneIpSLAGlobalPollInterval_Type())
zhoneIpSLAGlobalPollInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneIpSLAGlobalPollInterval.setStatus(_B)
if mibBuilder.loadTexts:zhoneIpSLAGlobalPollInterval.setUnits(_Y)
_ZhoneIpSLACosActionTable_Object=MibTable
zhoneIpSLACosActionTable=_ZhoneIpSLACosActionTable_Object((1,3,6,1,4,1,5504,4,1,21,1,3))
if mibBuilder.loadTexts:zhoneIpSLACosActionTable.setStatus(_B)
_ZhoneIpSLACosActionEntry_Object=MibTableRow
zhoneIpSLACosActionEntry=_ZhoneIpSLACosActionEntry_Object((1,3,6,1,4,1,5504,4,1,21,1,3,1))
zhoneIpSLACosActionEntry.setIndexNames((0,_A,_Z))
if mibBuilder.loadTexts:zhoneIpSLACosActionEntry.setStatus(_B)
class _ZhoneIpSLACosActionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ZhoneIpSLACosActionIndex_Type.__name__=_C
_ZhoneIpSLACosActionIndex_Object=MibTableColumn
zhoneIpSLACosActionIndex=_ZhoneIpSLACosActionIndex_Object((1,3,6,1,4,1,5504,4,1,21,1,3,1,1),_ZhoneIpSLACosActionIndex_Type())
zhoneIpSLACosActionIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneIpSLACosActionIndex.setStatus(_B)
class _ZhoneIpSLACosActionName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_ZhoneIpSLACosActionName_Type.__name__=_M
_ZhoneIpSLACosActionName_Object=MibTableColumn
zhoneIpSLACosActionName=_ZhoneIpSLACosActionName_Object((1,3,6,1,4,1,5504,4,1,21,1,3,1,2),_ZhoneIpSLACosActionName_Type())
zhoneIpSLACosActionName.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneIpSLACosActionName.setStatus(_B)
class _ZhoneIpSLACosActionTrapOnError_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_ZhoneIpSLACosActionTrapOnError_Type.__name__=_C
_ZhoneIpSLACosActionTrapOnError_Object=MibTableColumn
zhoneIpSLACosActionTrapOnError=_ZhoneIpSLACosActionTrapOnError_Object((1,3,6,1,4,1,5504,4,1,21,1,3,1,3),_ZhoneIpSLACosActionTrapOnError_Type())
zhoneIpSLACosActionTrapOnError.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneIpSLACosActionTrapOnError.setStatus(_B)
class _ZhoneIpSLACosActionTimeoutErrThresh_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_ZhoneIpSLACosActionTimeoutErrThresh_Type.__name__=_C
_ZhoneIpSLACosActionTimeoutErrThresh_Object=MibTableColumn
zhoneIpSLACosActionTimeoutErrThresh=_ZhoneIpSLACosActionTimeoutErrThresh_Object((1,3,6,1,4,1,5504,4,1,21,1,3,1,4),_ZhoneIpSLACosActionTimeoutErrThresh_Type())
zhoneIpSLACosActionTimeoutErrThresh.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneIpSLACosActionTimeoutErrThresh.setStatus(_B)
class _ZhoneIpSLACosActionTimeoutClrThresh_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_ZhoneIpSLACosActionTimeoutClrThresh_Type.__name__=_C
_ZhoneIpSLACosActionTimeoutClrThresh_Object=MibTableColumn
zhoneIpSLACosActionTimeoutClrThresh=_ZhoneIpSLACosActionTimeoutClrThresh_Object((1,3,6,1,4,1,5504,4,1,21,1,3,1,5),_ZhoneIpSLACosActionTimeoutClrThresh_Type())
zhoneIpSLACosActionTimeoutClrThresh.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneIpSLACosActionTimeoutClrThresh.setStatus(_B)
class _ZhoneIpSLACosActionLatencyErrThresh_Type(Integer32):defaultValue=10000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,10000))
_ZhoneIpSLACosActionLatencyErrThresh_Type.__name__=_C
_ZhoneIpSLACosActionLatencyErrThresh_Object=MibTableColumn
zhoneIpSLACosActionLatencyErrThresh=_ZhoneIpSLACosActionLatencyErrThresh_Object((1,3,6,1,4,1,5504,4,1,21,1,3,1,6),_ZhoneIpSLACosActionLatencyErrThresh_Type())
zhoneIpSLACosActionLatencyErrThresh.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneIpSLACosActionLatencyErrThresh.setStatus(_B)
if mibBuilder.loadTexts:zhoneIpSLACosActionLatencyErrThresh.setUnits(_G)
class _ZhoneIpSLACosActionLatencyClrThresh_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_ZhoneIpSLACosActionLatencyClrThresh_Type.__name__=_C
_ZhoneIpSLACosActionLatencyClrThresh_Object=MibTableColumn
zhoneIpSLACosActionLatencyClrThresh=_ZhoneIpSLACosActionLatencyClrThresh_Object((1,3,6,1,4,1,5504,4,1,21,1,3,1,7),_ZhoneIpSLACosActionLatencyClrThresh_Type())
zhoneIpSLACosActionLatencyClrThresh.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneIpSLACosActionLatencyClrThresh.setStatus(_B)
class _ZhoneIpSLACosActionJitterErrThresh_Type(Integer32):defaultValue=10000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,10000))
_ZhoneIpSLACosActionJitterErrThresh_Type.__name__=_C
_ZhoneIpSLACosActionJitterErrThresh_Object=MibTableColumn
zhoneIpSLACosActionJitterErrThresh=_ZhoneIpSLACosActionJitterErrThresh_Object((1,3,6,1,4,1,5504,4,1,21,1,3,1,8),_ZhoneIpSLACosActionJitterErrThresh_Type())
zhoneIpSLACosActionJitterErrThresh.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneIpSLACosActionJitterErrThresh.setStatus(_B)
if mibBuilder.loadTexts:zhoneIpSLACosActionJitterErrThresh.setUnits(_G)
class _ZhoneIpSLACosActionJitterClrThresh_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_ZhoneIpSLACosActionJitterClrThresh_Type.__name__=_C
_ZhoneIpSLACosActionJitterClrThresh_Object=MibTableColumn
zhoneIpSLACosActionJitterClrThresh=_ZhoneIpSLACosActionJitterClrThresh_Object((1,3,6,1,4,1,5504,4,1,21,1,3,1,9),_ZhoneIpSLACosActionJitterClrThresh_Type())
zhoneIpSLACosActionJitterClrThresh.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneIpSLACosActionJitterClrThresh.setStatus(_B)
class _ZhoneIpSLACosActionMetrics_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_ZhoneIpSLACosActionMetrics_Type.__name__=_C
_ZhoneIpSLACosActionMetrics_Object=MibTableColumn
zhoneIpSLACosActionMetrics=_ZhoneIpSLACosActionMetrics_Object((1,3,6,1,4,1,5504,4,1,21,1,3,1,10),_ZhoneIpSLACosActionMetrics_Type())
zhoneIpSLACosActionMetrics.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneIpSLACosActionMetrics.setStatus(_B)
class _ZhoneIpSLACosActionPacketSize_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,2048))
_ZhoneIpSLACosActionPacketSize_Type.__name__=_C
_ZhoneIpSLACosActionPacketSize_Object=MibTableColumn
zhoneIpSLACosActionPacketSize=_ZhoneIpSLACosActionPacketSize_Object((1,3,6,1,4,1,5504,4,1,21,1,3,1,11),_ZhoneIpSLACosActionPacketSize_Type())
zhoneIpSLACosActionPacketSize.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneIpSLACosActionPacketSize.setStatus(_B)
if mibBuilder.loadTexts:zhoneIpSLACosActionPacketSize.setUnits('octets')
_ZhoneIpSLACosMapTable_Object=MibTable
zhoneIpSLACosMapTable=_ZhoneIpSLACosMapTable_Object((1,3,6,1,4,1,5504,4,1,21,1,4))
if mibBuilder.loadTexts:zhoneIpSLACosMapTable.setStatus(_B)
_ZhoneIpSLACosMapEntry_Object=MibTableRow
zhoneIpSLACosMapEntry=_ZhoneIpSLACosMapEntry_Object((1,3,6,1,4,1,5504,4,1,21,1,4,1))
zhoneIpSLACosMapEntry.setIndexNames((0,_A,_a))
if mibBuilder.loadTexts:zhoneIpSLACosMapEntry.setStatus(_B)
class _ZhoneIpSLACosMapDscpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_ZhoneIpSLACosMapDscpIndex_Type.__name__=_C
_ZhoneIpSLACosMapDscpIndex_Object=MibTableColumn
zhoneIpSLACosMapDscpIndex=_ZhoneIpSLACosMapDscpIndex_Object((1,3,6,1,4,1,5504,4,1,21,1,4,1,1),_ZhoneIpSLACosMapDscpIndex_Type())
zhoneIpSLACosMapDscpIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneIpSLACosMapDscpIndex.setStatus(_B)
class _ZhoneIpSLACosMapCosActionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_ZhoneIpSLACosMapCosActionIndex_Type.__name__=_C
_ZhoneIpSLACosMapCosActionIndex_Object=MibTableColumn
zhoneIpSLACosMapCosActionIndex=_ZhoneIpSLACosMapCosActionIndex_Object((1,3,6,1,4,1,5504,4,1,21,1,4,1,2),_ZhoneIpSLACosMapCosActionIndex_Type())
zhoneIpSLACosMapCosActionIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneIpSLACosMapCosActionIndex.setStatus(_B)
_ZhoneIpSLAStaticPathTable_Object=MibTable
zhoneIpSLAStaticPathTable=_ZhoneIpSLAStaticPathTable_Object((1,3,6,1,4,1,5504,4,1,21,1,5))
if mibBuilder.loadTexts:zhoneIpSLAStaticPathTable.setStatus(_B)
_ZhoneIpSLAStaticPathEntry_Object=MibTableRow
zhoneIpSLAStaticPathEntry=_ZhoneIpSLAStaticPathEntry_Object((1,3,6,1,4,1,5504,4,1,21,1,5,1))
zhoneIpSLAStaticPathEntry.setIndexNames((0,_A,_b),(0,_A,_c))
if mibBuilder.loadTexts:zhoneIpSLAStaticPathEntry.setStatus(_B)
class _ZhoneIpSLAStaticPathRdIndex_Type(ZhoneRDIndex):subtypeSpec=ZhoneRDIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_ZhoneIpSLAStaticPathRdIndex_Type.__name__=_O
_ZhoneIpSLAStaticPathRdIndex_Object=MibTableColumn
zhoneIpSLAStaticPathRdIndex=_ZhoneIpSLAStaticPathRdIndex_Object((1,3,6,1,4,1,5504,4,1,21,1,5,1,1),_ZhoneIpSLAStaticPathRdIndex_Type())
zhoneIpSLAStaticPathRdIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneIpSLAStaticPathRdIndex.setStatus(_B)
_ZhoneIpSLAStaticPathTargetIP_Type=IpAddress
_ZhoneIpSLAStaticPathTargetIP_Object=MibTableColumn
zhoneIpSLAStaticPathTargetIP=_ZhoneIpSLAStaticPathTargetIP_Object((1,3,6,1,4,1,5504,4,1,21,1,5,1,2),_ZhoneIpSLAStaticPathTargetIP_Type())
zhoneIpSLAStaticPathTargetIP.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneIpSLAStaticPathTargetIP.setStatus(_B)
class _ZhoneIpSLAStaticPathForwarding_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_ZhoneIpSLAStaticPathForwarding_Type.__name__=_C
_ZhoneIpSLAStaticPathForwarding_Object=MibTableColumn
zhoneIpSLAStaticPathForwarding=_ZhoneIpSLAStaticPathForwarding_Object((1,3,6,1,4,1,5504,4,1,21,1,5,1,3),_ZhoneIpSLAStaticPathForwarding_Type())
zhoneIpSLAStaticPathForwarding.setMaxAccess(_Q)
if mibBuilder.loadTexts:zhoneIpSLAStaticPathForwarding.setStatus(_B)
class _ZhoneIpSLAStaticPathState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_ZhoneIpSLAStaticPathState_Type.__name__=_C
_ZhoneIpSLAStaticPathState_Object=MibTableColumn
zhoneIpSLAStaticPathState=_ZhoneIpSLAStaticPathState_Object((1,3,6,1,4,1,5504,4,1,21,1,5,1,4),_ZhoneIpSLAStaticPathState_Type())
zhoneIpSLAStaticPathState.setMaxAccess(_Q)
if mibBuilder.loadTexts:zhoneIpSLAStaticPathState.setStatus(_B)
_ZhoneIpSLAStaticPathRowstatus_Type=RowStatus
_ZhoneIpSLAStaticPathRowstatus_Object=MibTableColumn
zhoneIpSLAStaticPathRowstatus=_ZhoneIpSLAStaticPathRowstatus_Object((1,3,6,1,4,1,5504,4,1,21,1,5,1,5),_ZhoneIpSLAStaticPathRowstatus_Type())
zhoneIpSLAStaticPathRowstatus.setMaxAccess(_Q)
if mibBuilder.loadTexts:zhoneIpSLAStaticPathRowstatus.setStatus(_B)
_ZhoneIpSLAPathConnectTable_Object=MibTable
zhoneIpSLAPathConnectTable=_ZhoneIpSLAPathConnectTable_Object((1,3,6,1,4,1,5504,4,1,21,1,6))
if mibBuilder.loadTexts:zhoneIpSLAPathConnectTable.setStatus(_B)
_ZhoneIpSLAPathConnectEntry_Object=MibTableRow
zhoneIpSLAPathConnectEntry=_ZhoneIpSLAPathConnectEntry_Object((1,3,6,1,4,1,5504,4,1,21,1,6,1))
zhoneIpSLAPathConnectEntry.setIndexNames((0,_N,_P),(0,_A,_d))
if mibBuilder.loadTexts:zhoneIpSLAPathConnectEntry.setStatus(_B)
_ZhoneIpSLAPathConnectEndpointIP_Type=IpAddress
_ZhoneIpSLAPathConnectEndpointIP_Object=MibTableColumn
zhoneIpSLAPathConnectEndpointIP=_ZhoneIpSLAPathConnectEndpointIP_Object((1,3,6,1,4,1,5504,4,1,21,1,6,1,1),_ZhoneIpSLAPathConnectEndpointIP_Type())
zhoneIpSLAPathConnectEndpointIP.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneIpSLAPathConnectEndpointIP.setStatus(_B)
class _ZhoneIpSLAPathConnectDevName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ZhoneIpSLAPathConnectDevName_Type.__name__=_M
_ZhoneIpSLAPathConnectDevName_Object=MibTableColumn
zhoneIpSLAPathConnectDevName=_ZhoneIpSLAPathConnectDevName_Object((1,3,6,1,4,1,5504,4,1,21,1,6,1,2),_ZhoneIpSLAPathConnectDevName_Type())
zhoneIpSLAPathConnectDevName.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIpSLAPathConnectDevName.setStatus(_B)
class _ZhoneIpSLAPathConnectDevType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_ZhoneIpSLAPathConnectDevType_Type.__name__=_M
_ZhoneIpSLAPathConnectDevType_Object=MibTableColumn
zhoneIpSLAPathConnectDevType=_ZhoneIpSLAPathConnectDevType_Object((1,3,6,1,4,1,5504,4,1,21,1,6,1,3),_ZhoneIpSLAPathConnectDevType_Type())
zhoneIpSLAPathConnectDevType.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIpSLAPathConnectDevType.setStatus(_B)
class _ZhoneIpSLAPathConnectStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_ZhoneIpSLAPathConnectStatus_Type.__name__=_C
_ZhoneIpSLAPathConnectStatus_Object=MibTableColumn
zhoneIpSLAPathConnectStatus=_ZhoneIpSLAPathConnectStatus_Object((1,3,6,1,4,1,5504,4,1,21,1,6,1,4),_ZhoneIpSLAPathConnectStatus_Type())
zhoneIpSLAPathConnectStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIpSLAPathConnectStatus.setStatus(_B)
_ZhoneIpSLAPathConnectSrcIP_Type=IpAddress
_ZhoneIpSLAPathConnectSrcIP_Object=MibTableColumn
zhoneIpSLAPathConnectSrcIP=_ZhoneIpSLAPathConnectSrcIP_Object((1,3,6,1,4,1,5504,4,1,21,1,6,1,5),_ZhoneIpSLAPathConnectSrcIP_Type())
zhoneIpSLAPathConnectSrcIP.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIpSLAPathConnectSrcIP.setStatus(_B)
class _ZhoneIpSLAPathConnectDiscoveryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_ZhoneIpSLAPathConnectDiscoveryType_Type.__name__=_C
_ZhoneIpSLAPathConnectDiscoveryType_Object=MibTableColumn
zhoneIpSLAPathConnectDiscoveryType=_ZhoneIpSLAPathConnectDiscoveryType_Object((1,3,6,1,4,1,5504,4,1,21,1,6,1,6),_ZhoneIpSLAPathConnectDiscoveryType_Type())
zhoneIpSLAPathConnectDiscoveryType.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIpSLAPathConnectDiscoveryType.setStatus(_B)
_ZhoneIpSLAPathConnectUpTime_Type=Counter32
_ZhoneIpSLAPathConnectUpTime_Object=MibTableColumn
zhoneIpSLAPathConnectUpTime=_ZhoneIpSLAPathConnectUpTime_Object((1,3,6,1,4,1,5504,4,1,21,1,6,1,7),_ZhoneIpSLAPathConnectUpTime_Type())
zhoneIpSLAPathConnectUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIpSLAPathConnectUpTime.setStatus(_B)
if mibBuilder.loadTexts:zhoneIpSLAPathConnectUpTime.setUnits(_Y)
class _ZhoneIpSLAPathConnectPollType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('initiator',1),('responder',2)))
_ZhoneIpSLAPathConnectPollType_Type.__name__=_C
_ZhoneIpSLAPathConnectPollType_Object=MibTableColumn
zhoneIpSLAPathConnectPollType=_ZhoneIpSLAPathConnectPollType_Object((1,3,6,1,4,1,5504,4,1,21,1,6,1,8),_ZhoneIpSLAPathConnectPollType_Type())
zhoneIpSLAPathConnectPollType.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIpSLAPathConnectPollType.setStatus(_B)
_ZhoneIpSLAPathConnectCosMismatch_Type=Counter32
_ZhoneIpSLAPathConnectCosMismatch_Object=MibTableColumn
zhoneIpSLAPathConnectCosMismatch=_ZhoneIpSLAPathConnectCosMismatch_Object((1,3,6,1,4,1,5504,4,1,21,1,6,1,9),_ZhoneIpSLAPathConnectCosMismatch_Type())
zhoneIpSLAPathConnectCosMismatch.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIpSLAPathConnectCosMismatch.setStatus(_B)
class _ZhoneIpSLAPathConnectLastCosActionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ZhoneIpSLAPathConnectLastCosActionIndex_Type.__name__=_C
_ZhoneIpSLAPathConnectLastCosActionIndex_Object=MibTableColumn
zhoneIpSLAPathConnectLastCosActionIndex=_ZhoneIpSLAPathConnectLastCosActionIndex_Object((1,3,6,1,4,1,5504,4,1,21,1,6,1,10),_ZhoneIpSLAPathConnectLastCosActionIndex_Type())
zhoneIpSLAPathConnectLastCosActionIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIpSLAPathConnectLastCosActionIndex.setStatus(_B)
_ZhoneIpSLAPathStatByCOSTable_Object=MibTable
zhoneIpSLAPathStatByCOSTable=_ZhoneIpSLAPathStatByCOSTable_Object((1,3,6,1,4,1,5504,4,1,21,1,7))
if mibBuilder.loadTexts:zhoneIpSLAPathStatByCOSTable.setStatus(_B)
_ZhoneIpSLAPathStatByCOSEntry_Object=MibTableRow
zhoneIpSLAPathStatByCOSEntry=_ZhoneIpSLAPathStatByCOSEntry_Object((1,3,6,1,4,1,5504,4,1,21,1,7,1))
zhoneIpSLAPathStatByCOSEntry.setIndexNames((0,_A,_e),(0,_N,_P),(0,_A,_H))
if mibBuilder.loadTexts:zhoneIpSLAPathStatByCOSEntry.setStatus(_B)
class _ZhoneIpSLAPathStatByCOSCosActIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ZhoneIpSLAPathStatByCOSCosActIndex_Type.__name__=_C
_ZhoneIpSLAPathStatByCOSCosActIndex_Object=MibTableColumn
zhoneIpSLAPathStatByCOSCosActIndex=_ZhoneIpSLAPathStatByCOSCosActIndex_Object((1,3,6,1,4,1,5504,4,1,21,1,7,1,1),_ZhoneIpSLAPathStatByCOSCosActIndex_Type())
zhoneIpSLAPathStatByCOSCosActIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneIpSLAPathStatByCOSCosActIndex.setStatus(_B)
_ZhoneIpSLAPathStatByCOSTargetIP_Type=IpAddress
_ZhoneIpSLAPathStatByCOSTargetIP_Object=MibTableColumn
zhoneIpSLAPathStatByCOSTargetIP=_ZhoneIpSLAPathStatByCOSTargetIP_Object((1,3,6,1,4,1,5504,4,1,21,1,7,1,2),_ZhoneIpSLAPathStatByCOSTargetIP_Type())
zhoneIpSLAPathStatByCOSTargetIP.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:zhoneIpSLAPathStatByCOSTargetIP.setStatus(_B)
class _ZhoneIpSLAPathStatByCOSStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),(_g,2)))
_ZhoneIpSLAPathStatByCOSStatus_Type.__name__=_C
_ZhoneIpSLAPathStatByCOSStatus_Object=MibTableColumn
zhoneIpSLAPathStatByCOSStatus=_ZhoneIpSLAPathStatByCOSStatus_Object((1,3,6,1,4,1,5504,4,1,21,1,7,1,3),_ZhoneIpSLAPathStatByCOSStatus_Type())
zhoneIpSLAPathStatByCOSStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneIpSLAPathStatByCOSStatus.setStatus(_B)
_ZhoneIpSLAPathStatByCOSLastRTT_Type=Counter32
_ZhoneIpSLAPathStatByCOSLastRTT_Object=MibTableColumn
zhoneIpSLAPathStatByCOSLastRTT=_ZhoneIpSLAPathStatByCOSLastRTT_Object((1,3,6,1,4,1,5504,4,1,21,1,7,1,4),_ZhoneIpSLAPathStatByCOSLastRTT_Type())
zhoneIpSLAPathStatByCOSLastRTT.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIpSLAPathStatByCOSLastRTT.setStatus(_B)
if mibBuilder.loadTexts:zhoneIpSLAPathStatByCOSLastRTT.setUnits(_G)
_ZhoneIpSLAPathStatByCOSMinRTT_Type=Counter32
_ZhoneIpSLAPathStatByCOSMinRTT_Object=MibTableColumn
zhoneIpSLAPathStatByCOSMinRTT=_ZhoneIpSLAPathStatByCOSMinRTT_Object((1,3,6,1,4,1,5504,4,1,21,1,7,1,5),_ZhoneIpSLAPathStatByCOSMinRTT_Type())
zhoneIpSLAPathStatByCOSMinRTT.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIpSLAPathStatByCOSMinRTT.setStatus(_B)
if mibBuilder.loadTexts:zhoneIpSLAPathStatByCOSMinRTT.setUnits(_G)
_ZhoneIpSLAPathStatByCOSAvgRTT_Type=Counter32
_ZhoneIpSLAPathStatByCOSAvgRTT_Object=MibTableColumn
zhoneIpSLAPathStatByCOSAvgRTT=_ZhoneIpSLAPathStatByCOSAvgRTT_Object((1,3,6,1,4,1,5504,4,1,21,1,7,1,6),_ZhoneIpSLAPathStatByCOSAvgRTT_Type())
zhoneIpSLAPathStatByCOSAvgRTT.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIpSLAPathStatByCOSAvgRTT.setStatus(_B)
if mibBuilder.loadTexts:zhoneIpSLAPathStatByCOSAvgRTT.setUnits(_G)
_ZhoneIpSLAPathStatByCOSMaxRTT_Type=Counter32
_ZhoneIpSLAPathStatByCOSMaxRTT_Object=MibTableColumn
zhoneIpSLAPathStatByCOSMaxRTT=_ZhoneIpSLAPathStatByCOSMaxRTT_Object((1,3,6,1,4,1,5504,4,1,21,1,7,1,7),_ZhoneIpSLAPathStatByCOSMaxRTT_Type())
zhoneIpSLAPathStatByCOSMaxRTT.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIpSLAPathStatByCOSMaxRTT.setStatus(_B)
if mibBuilder.loadTexts:zhoneIpSLAPathStatByCOSMaxRTT.setUnits(_G)
_ZhoneIpSLAPathStatByCOSDroppedResp_Type=Counter32
_ZhoneIpSLAPathStatByCOSDroppedResp_Object=MibTableColumn
zhoneIpSLAPathStatByCOSDroppedResp=_ZhoneIpSLAPathStatByCOSDroppedResp_Object((1,3,6,1,4,1,5504,4,1,21,1,7,1,8),_ZhoneIpSLAPathStatByCOSDroppedResp_Type())
zhoneIpSLAPathStatByCOSDroppedResp.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIpSLAPathStatByCOSDroppedResp.setStatus(_B)
_ZhoneIpSLAPathStatByIntervalTable_Object=MibTable
zhoneIpSLAPathStatByIntervalTable=_ZhoneIpSLAPathStatByIntervalTable_Object((1,3,6,1,4,1,5504,4,1,21,1,8))
if mibBuilder.loadTexts:zhoneIpSLAPathStatByIntervalTable.setStatus(_B)
_ZhoneIpSLAPathStatByIntervalEntry_Object=MibTableRow
zhoneIpSLAPathStatByIntervalEntry=_ZhoneIpSLAPathStatByIntervalEntry_Object((1,3,6,1,4,1,5504,4,1,21,1,8,1))
zhoneIpSLAPathStatByIntervalEntry.setIndexNames((0,_A,_h),(0,_A,_i),(0,_A,_j),(0,_A,_k))
if mibBuilder.loadTexts:zhoneIpSLAPathStatByIntervalEntry.setStatus(_B)
class _ZhoneIpSLAPathStatByIntervalIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_ZhoneIpSLAPathStatByIntervalIndex_Type.__name__=_C
_ZhoneIpSLAPathStatByIntervalIndex_Object=MibTableColumn
zhoneIpSLAPathStatByIntervalIndex=_ZhoneIpSLAPathStatByIntervalIndex_Object((1,3,6,1,4,1,5504,4,1,21,1,8,1,1),_ZhoneIpSLAPathStatByIntervalIndex_Type())
zhoneIpSLAPathStatByIntervalIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneIpSLAPathStatByIntervalIndex.setStatus(_B)
class _ZhoneIpSLAPathStatByIntervalCosActIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ZhoneIpSLAPathStatByIntervalCosActIndex_Type.__name__=_C
_ZhoneIpSLAPathStatByIntervalCosActIndex_Object=MibTableColumn
zhoneIpSLAPathStatByIntervalCosActIndex=_ZhoneIpSLAPathStatByIntervalCosActIndex_Object((1,3,6,1,4,1,5504,4,1,21,1,8,1,2),_ZhoneIpSLAPathStatByIntervalCosActIndex_Type())
zhoneIpSLAPathStatByIntervalCosActIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneIpSLAPathStatByIntervalCosActIndex.setStatus(_B)
class _ZhoneIpSLAPathStatByIntervalRdIndex_Type(ZhoneRDIndex):subtypeSpec=ZhoneRDIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_ZhoneIpSLAPathStatByIntervalRdIndex_Type.__name__=_O
_ZhoneIpSLAPathStatByIntervalRdIndex_Object=MibTableColumn
zhoneIpSLAPathStatByIntervalRdIndex=_ZhoneIpSLAPathStatByIntervalRdIndex_Object((1,3,6,1,4,1,5504,4,1,21,1,8,1,3),_ZhoneIpSLAPathStatByIntervalRdIndex_Type())
zhoneIpSLAPathStatByIntervalRdIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneIpSLAPathStatByIntervalRdIndex.setStatus(_B)
_ZhoneIpSLAPathStatByIntervalTargetIP_Type=IpAddress
_ZhoneIpSLAPathStatByIntervalTargetIP_Object=MibTableColumn
zhoneIpSLAPathStatByIntervalTargetIP=_ZhoneIpSLAPathStatByIntervalTargetIP_Object((1,3,6,1,4,1,5504,4,1,21,1,8,1,4),_ZhoneIpSLAPathStatByIntervalTargetIP_Type())
zhoneIpSLAPathStatByIntervalTargetIP.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneIpSLAPathStatByIntervalTargetIP.setStatus(_B)
_ZhoneIpSLAPathStatByIntervalDateTime_Type=DateAndTime
_ZhoneIpSLAPathStatByIntervalDateTime_Object=MibTableColumn
zhoneIpSLAPathStatByIntervalDateTime=_ZhoneIpSLAPathStatByIntervalDateTime_Object((1,3,6,1,4,1,5504,4,1,21,1,8,1,5),_ZhoneIpSLAPathStatByIntervalDateTime_Type())
zhoneIpSLAPathStatByIntervalDateTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIpSLAPathStatByIntervalDateTime.setStatus(_B)
class _ZhoneIpSLAPathStatByIntervalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),(_g,2)))
_ZhoneIpSLAPathStatByIntervalStatus_Type.__name__=_C
_ZhoneIpSLAPathStatByIntervalStatus_Object=MibTableColumn
zhoneIpSLAPathStatByIntervalStatus=_ZhoneIpSLAPathStatByIntervalStatus_Object((1,3,6,1,4,1,5504,4,1,21,1,8,1,6),_ZhoneIpSLAPathStatByIntervalStatus_Type())
zhoneIpSLAPathStatByIntervalStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIpSLAPathStatByIntervalStatus.setStatus(_B)
_ZhoneIpSLAPathStatByIntervalMinRTT_Type=Counter32
_ZhoneIpSLAPathStatByIntervalMinRTT_Object=MibTableColumn
zhoneIpSLAPathStatByIntervalMinRTT=_ZhoneIpSLAPathStatByIntervalMinRTT_Object((1,3,6,1,4,1,5504,4,1,21,1,8,1,7),_ZhoneIpSLAPathStatByIntervalMinRTT_Type())
zhoneIpSLAPathStatByIntervalMinRTT.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIpSLAPathStatByIntervalMinRTT.setStatus(_B)
if mibBuilder.loadTexts:zhoneIpSLAPathStatByIntervalMinRTT.setUnits(_G)
_ZhoneIpSLAPathStatByIntervalAvgRTT_Type=Counter32
_ZhoneIpSLAPathStatByIntervalAvgRTT_Object=MibTableColumn
zhoneIpSLAPathStatByIntervalAvgRTT=_ZhoneIpSLAPathStatByIntervalAvgRTT_Object((1,3,6,1,4,1,5504,4,1,21,1,8,1,8),_ZhoneIpSLAPathStatByIntervalAvgRTT_Type())
zhoneIpSLAPathStatByIntervalAvgRTT.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIpSLAPathStatByIntervalAvgRTT.setStatus(_B)
if mibBuilder.loadTexts:zhoneIpSLAPathStatByIntervalAvgRTT.setUnits(_G)
_ZhoneIpSLAPathStatByIntervalMaxRTT_Type=Counter32
_ZhoneIpSLAPathStatByIntervalMaxRTT_Object=MibTableColumn
zhoneIpSLAPathStatByIntervalMaxRTT=_ZhoneIpSLAPathStatByIntervalMaxRTT_Object((1,3,6,1,4,1,5504,4,1,21,1,8,1,9),_ZhoneIpSLAPathStatByIntervalMaxRTT_Type())
zhoneIpSLAPathStatByIntervalMaxRTT.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIpSLAPathStatByIntervalMaxRTT.setStatus(_B)
if mibBuilder.loadTexts:zhoneIpSLAPathStatByIntervalMaxRTT.setUnits(_G)
_ZhoneIpSLAPathStatByIntervalDroppedResp_Type=Counter32
_ZhoneIpSLAPathStatByIntervalDroppedResp_Object=MibTableColumn
zhoneIpSLAPathStatByIntervalDroppedResp=_ZhoneIpSLAPathStatByIntervalDroppedResp_Object((1,3,6,1,4,1,5504,4,1,21,1,8,1,10),_ZhoneIpSLAPathStatByIntervalDroppedResp_Type())
zhoneIpSLAPathStatByIntervalDroppedResp.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIpSLAPathStatByIntervalDroppedResp.setStatus(_B)
_ZhoneIpSLATraps_ObjectIdentity=ObjectIdentity
zhoneIpSLATraps=_ZhoneIpSLATraps_ObjectIdentity((1,3,6,1,4,1,5504,4,1,21,2))
_ZhoneIpSLATrapsPrefix_ObjectIdentity=ObjectIdentity
zhoneIpSLATrapsPrefix=_ZhoneIpSLATrapsPrefix_ObjectIdentity((1,3,6,1,4,1,5504,4,1,21,2,0))
if mibBuilder.loadTexts:zhoneIpSLATrapsPrefix.setStatus(_B)
_ZhoneIpSLAConformance_ObjectIdentity=ObjectIdentity
zhoneIpSLAConformance=_ZhoneIpSLAConformance_ObjectIdentity((1,3,6,1,4,1,5504,4,1,21,3))
_ZhoneIpSLAMIBGroups_ObjectIdentity=ObjectIdentity
zhoneIpSLAMIBGroups=_ZhoneIpSLAMIBGroups_ObjectIdentity((1,3,6,1,4,1,5504,4,1,21,3,1))
_ZhoneIpSLACompliances_ObjectIdentity=ObjectIdentity
zhoneIpSLACompliances=_ZhoneIpSLACompliances_ObjectIdentity((1,3,6,1,4,1,5504,4,1,21,3,2))
zhoneIpSLAGlobalsGroup=ObjectGroup((1,3,6,1,4,1,5504,4,1,21,3,1,1))
zhoneIpSLAGlobalsGroup.setObjects(*((_A,_l),(_A,_m)))
if mibBuilder.loadTexts:zhoneIpSLAGlobalsGroup.setStatus(_B)
zhoneIpSLACosActionGroup=ObjectGroup((1,3,6,1,4,1,5504,4,1,21,3,1,2))
zhoneIpSLACosActionGroup.setObjects(*((_A,_I),(_A,_n),(_A,_R),(_A,_o),(_A,_S),(_A,_p),(_A,_T),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:zhoneIpSLACosActionGroup.setStatus(_B)
zhoneIpSLACOSMapGroup=ObjectGroup((1,3,6,1,4,1,5504,4,1,21,3,1,3))
zhoneIpSLACOSMapGroup.setObjects((_A,_t))
if mibBuilder.loadTexts:zhoneIpSLACOSMapGroup.setStatus(_B)
zhoneIpSLAStaticPathGroup=ObjectGroup((1,3,6,1,4,1,5504,4,1,21,3,1,4))
zhoneIpSLAStaticPathGroup.setObjects(*((_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:zhoneIpSLAStaticPathGroup.setStatus(_B)
zhoneIpSLAPathConnectGroup=ObjectGroup((1,3,6,1,4,1,5504,4,1,21,3,1,5))
zhoneIpSLAPathConnectGroup.setObjects(*((_A,_x),(_A,_y),(_A,_z),(_A,_J),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:zhoneIpSLAPathConnectGroup.setStatus(_B)
zhoneIpSLAPathStatByCOSGroup=ObjectGroup((1,3,6,1,4,1,5504,4,1,21,3,1,6))
zhoneIpSLAPathStatByCOSGroup.setObjects(*((_A,_H),(_A,_A5),(_A,_A6),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:zhoneIpSLAPathStatByCOSGroup.setStatus(_B)
zhoneIpSLAPathStatByIntervalGroup=ObjectGroup((1,3,6,1,4,1,5504,4,1,21,3,1,7))
zhoneIpSLAPathStatByIntervalGroup.setObjects(*((_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:zhoneIpSLAPathStatByIntervalGroup.setStatus(_B)
zhoneIpSLATimeoutTrap=NotificationType((1,3,6,1,4,1,5504,4,1,21,2,0,1))
zhoneIpSLATimeoutTrap.setObjects(*((_A,_J),(_A,_H),(_A,_I),(_A,_X),(_A,_R)))
if mibBuilder.loadTexts:zhoneIpSLATimeoutTrap.setStatus(_B)
zhoneIpSLALatencyTrap=NotificationType((1,3,6,1,4,1,5504,4,1,21,2,0,2))
zhoneIpSLALatencyTrap.setObjects(*((_A,_J),(_A,_H),(_A,_I),(_A,_V),(_A,_S)))
if mibBuilder.loadTexts:zhoneIpSLALatencyTrap.setStatus(_B)
zhoneIpSLAJitterTrap=NotificationType((1,3,6,1,4,1,5504,4,1,21,2,0,3))
zhoneIpSLAJitterTrap.setObjects(*((_A,_J),(_A,_H),(_A,_I),(_A,_U),(_A,_W),(_A,_T)))
if mibBuilder.loadTexts:zhoneIpSLAJitterTrap.setStatus(_B)
zhoneIpSLATimeoutClearTrap=NotificationType((1,3,6,1,4,1,5504,4,1,21,2,0,4))
zhoneIpSLATimeoutClearTrap.setObjects(*((_A,_J),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:zhoneIpSLATimeoutClearTrap.setStatus(_B)
zhoneIpSLALatencyClearTrap=NotificationType((1,3,6,1,4,1,5504,4,1,21,2,0,5))
zhoneIpSLALatencyClearTrap.setObjects(*((_A,_J),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:zhoneIpSLALatencyClearTrap.setStatus(_B)
zhoneIpSLAJitterClearTrap=NotificationType((1,3,6,1,4,1,5504,4,1,21,2,0,6))
zhoneIpSLAJitterClearTrap.setObjects(*((_A,_J),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:zhoneIpSLAJitterClearTrap.setStatus(_B)
zhoneIpSLANotificationGroup=NotificationGroup((1,3,6,1,4,1,5504,4,1,21,3,1,8))
zhoneIpSLANotificationGroup.setObjects(*((_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:zhoneIpSLANotificationGroup.setStatus(_B)
zhoneIpSLACompliance=ModuleCompliance((1,3,6,1,4,1,5504,4,1,21,3,2,1))
zhoneIpSLACompliance.setObjects(*((_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ)))
if mibBuilder.loadTexts:zhoneIpSLACompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'zhoneIpSLA':zhoneIpSLA,'zhoneIpSLAMibObjects':zhoneIpSLAMibObjects,_l:zhoneIpSLAGlobalEnable,_m:zhoneIpSLAGlobalPollInterval,'zhoneIpSLACosActionTable':zhoneIpSLACosActionTable,'zhoneIpSLACosActionEntry':zhoneIpSLACosActionEntry,_Z:zhoneIpSLACosActionIndex,_I:zhoneIpSLACosActionName,_n:zhoneIpSLACosActionTrapOnError,_R:zhoneIpSLACosActionTimeoutErrThresh,_o:zhoneIpSLACosActionTimeoutClrThresh,_S:zhoneIpSLACosActionLatencyErrThresh,_p:zhoneIpSLACosActionLatencyClrThresh,_T:zhoneIpSLACosActionJitterErrThresh,_q:zhoneIpSLACosActionJitterClrThresh,_r:zhoneIpSLACosActionMetrics,_s:zhoneIpSLACosActionPacketSize,'zhoneIpSLACosMapTable':zhoneIpSLACosMapTable,'zhoneIpSLACosMapEntry':zhoneIpSLACosMapEntry,_a:zhoneIpSLACosMapDscpIndex,_t:zhoneIpSLACosMapCosActionIndex,'zhoneIpSLAStaticPathTable':zhoneIpSLAStaticPathTable,'zhoneIpSLAStaticPathEntry':zhoneIpSLAStaticPathEntry,_b:zhoneIpSLAStaticPathRdIndex,_c:zhoneIpSLAStaticPathTargetIP,_u:zhoneIpSLAStaticPathForwarding,_v:zhoneIpSLAStaticPathState,_w:zhoneIpSLAStaticPathRowstatus,'zhoneIpSLAPathConnectTable':zhoneIpSLAPathConnectTable,'zhoneIpSLAPathConnectEntry':zhoneIpSLAPathConnectEntry,_d:zhoneIpSLAPathConnectEndpointIP,_x:zhoneIpSLAPathConnectDevName,_y:zhoneIpSLAPathConnectDevType,_z:zhoneIpSLAPathConnectStatus,_J:zhoneIpSLAPathConnectSrcIP,_A0:zhoneIpSLAPathConnectDiscoveryType,_A1:zhoneIpSLAPathConnectUpTime,_A2:zhoneIpSLAPathConnectPollType,_A3:zhoneIpSLAPathConnectCosMismatch,_A4:zhoneIpSLAPathConnectLastCosActionIndex,'zhoneIpSLAPathStatByCOSTable':zhoneIpSLAPathStatByCOSTable,'zhoneIpSLAPathStatByCOSEntry':zhoneIpSLAPathStatByCOSEntry,_e:zhoneIpSLAPathStatByCOSCosActIndex,_H:zhoneIpSLAPathStatByCOSTargetIP,_A5:zhoneIpSLAPathStatByCOSStatus,_A6:zhoneIpSLAPathStatByCOSLastRTT,_U:zhoneIpSLAPathStatByCOSMinRTT,_V:zhoneIpSLAPathStatByCOSAvgRTT,_W:zhoneIpSLAPathStatByCOSMaxRTT,_X:zhoneIpSLAPathStatByCOSDroppedResp,'zhoneIpSLAPathStatByIntervalTable':zhoneIpSLAPathStatByIntervalTable,'zhoneIpSLAPathStatByIntervalEntry':zhoneIpSLAPathStatByIntervalEntry,_h:zhoneIpSLAPathStatByIntervalIndex,_i:zhoneIpSLAPathStatByIntervalCosActIndex,_j:zhoneIpSLAPathStatByIntervalRdIndex,_k:zhoneIpSLAPathStatByIntervalTargetIP,_A7:zhoneIpSLAPathStatByIntervalDateTime,_A8:zhoneIpSLAPathStatByIntervalStatus,_A9:zhoneIpSLAPathStatByIntervalMinRTT,_AA:zhoneIpSLAPathStatByIntervalAvgRTT,_AB:zhoneIpSLAPathStatByIntervalMaxRTT,_AC:zhoneIpSLAPathStatByIntervalDroppedResp,'zhoneIpSLATraps':zhoneIpSLATraps,'zhoneIpSLATrapsPrefix':zhoneIpSLATrapsPrefix,_AD:zhoneIpSLATimeoutTrap,_AE:zhoneIpSLALatencyTrap,_AF:zhoneIpSLAJitterTrap,_AG:zhoneIpSLATimeoutClearTrap,_AH:zhoneIpSLALatencyClearTrap,_AI:zhoneIpSLAJitterClearTrap,'zhoneIpSLAConformance':zhoneIpSLAConformance,'zhoneIpSLAMIBGroups':zhoneIpSLAMIBGroups,_AJ:zhoneIpSLAGlobalsGroup,_AK:zhoneIpSLACosActionGroup,_AL:zhoneIpSLACOSMapGroup,_AM:zhoneIpSLAStaticPathGroup,_AN:zhoneIpSLAPathConnectGroup,_AO:zhoneIpSLAPathStatByCOSGroup,_AQ:zhoneIpSLAPathStatByIntervalGroup,_AP:zhoneIpSLANotificationGroup,'zhoneIpSLACompliances':zhoneIpSLACompliances,'zhoneIpSLACompliance':zhoneIpSLACompliance})