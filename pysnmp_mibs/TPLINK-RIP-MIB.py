_N='tpRipIpAddressMask'
_M='tpRipInterfaceID'
_L='read-create'
_K='tpRipNetworkAddress'
_J='ripv2'
_I='ripv1'
_H='TPLINK-RIP-MIB'
_G='OctetString'
_F='read-only'
_E='enable'
_D='disable'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkRipMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,40))
if mibBuilder.loadTexts:tplinkRipMIB.setRevisions(('2012-12-13 09:30',))
_TplinkRipMIBObjects_ObjectIdentity=ObjectIdentity
tplinkRipMIBObjects=_TplinkRipMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,40,1))
_TpRipBasicConfig_ObjectIdentity=ObjectIdentity
tpRipBasicConfig=_TpRipBasicConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,40,1,1))
class _TpRipProtocolCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpRipProtocolCtrl_Type.__name__=_B
_TpRipProtocolCtrl_Object=MibScalar
tpRipProtocolCtrl=_TpRipProtocolCtrl_Object((1,3,6,1,4,1,11863,6,40,1,1,1),_TpRipProtocolCtrl_Type())
tpRipProtocolCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:tpRipProtocolCtrl.setStatus(_A)
class _TpRipProtocolVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('default',0),(_I,1),(_J,2)))
_TpRipProtocolVersion_Type.__name__=_B
_TpRipProtocolVersion_Object=MibScalar
tpRipProtocolVersion=_TpRipProtocolVersion_Object((1,3,6,1,4,1,11863,6,40,1,1,2),_TpRipProtocolVersion_Type())
tpRipProtocolVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:tpRipProtocolVersion.setStatus(_A)
class _TpRipDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TpRipDistance_Type.__name__=_B
_TpRipDistance_Object=MibScalar
tpRipDistance=_TpRipDistance_Object((1,3,6,1,4,1,11863,6,40,1,1,3),_TpRipDistance_Type())
tpRipDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:tpRipDistance.setStatus(_A)
class _TpRipAutoSumm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpRipAutoSumm_Type.__name__=_B
_TpRipAutoSumm_Object=MibScalar
tpRipAutoSumm=_TpRipAutoSumm_Object((1,3,6,1,4,1,11863,6,40,1,1,4),_TpRipAutoSumm_Type())
tpRipAutoSumm.setMaxAccess(_C)
if mibBuilder.loadTexts:tpRipAutoSumm.setStatus(_A)
class _TpRipDefaultMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_TpRipDefaultMetric_Type.__name__=_B
_TpRipDefaultMetric_Object=MibScalar
tpRipDefaultMetric=_TpRipDefaultMetric_Object((1,3,6,1,4,1,11863,6,40,1,1,5),_TpRipDefaultMetric_Type())
tpRipDefaultMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:tpRipDefaultMetric.setStatus(_A)
class _TpRipRedistriStatic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpRipRedistriStatic_Type.__name__=_B
_TpRipRedistriStatic_Object=MibScalar
tpRipRedistriStatic=_TpRipRedistriStatic_Object((1,3,6,1,4,1,11863,6,40,1,1,6),_TpRipRedistriStatic_Type())
tpRipRedistriStatic.setMaxAccess(_C)
if mibBuilder.loadTexts:tpRipRedistriStatic.setStatus(_A)
class _TpRipRedistriOspf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpRipRedistriOspf_Type.__name__=_B
_TpRipRedistriOspf_Object=MibScalar
tpRipRedistriOspf=_TpRipRedistriOspf_Object((1,3,6,1,4,1,11863,6,40,1,1,7),_TpRipRedistriOspf_Type())
tpRipRedistriOspf.setMaxAccess(_C)
if mibBuilder.loadTexts:tpRipRedistriOspf.setStatus(_A)
class _TpRipRedistStaticMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_TpRipRedistStaticMetric_Type.__name__=_B
_TpRipRedistStaticMetric_Object=MibScalar
tpRipRedistStaticMetric=_TpRipRedistStaticMetric_Object((1,3,6,1,4,1,11863,6,40,1,1,8),_TpRipRedistStaticMetric_Type())
tpRipRedistStaticMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:tpRipRedistStaticMetric.setStatus(_A)
class _TpRipRedistOspfMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_TpRipRedistOspfMetric_Type.__name__=_B
_TpRipRedistOspfMetric_Object=MibScalar
tpRipRedistOspfMetric=_TpRipRedistOspfMetric_Object((1,3,6,1,4,1,11863,6,40,1,1,9),_TpRipRedistOspfMetric_Type())
tpRipRedistOspfMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:tpRipRedistOspfMetric.setStatus(_A)
class _TpRipUpdateTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_TpRipUpdateTimer_Type.__name__=_B
_TpRipUpdateTimer_Object=MibScalar
tpRipUpdateTimer=_TpRipUpdateTimer_Object((1,3,6,1,4,1,11863,6,40,1,1,10),_TpRipUpdateTimer_Type())
tpRipUpdateTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:tpRipUpdateTimer.setStatus(_A)
class _TpRipTimeOutTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_TpRipTimeOutTimer_Type.__name__=_B
_TpRipTimeOutTimer_Object=MibScalar
tpRipTimeOutTimer=_TpRipTimeOutTimer_Object((1,3,6,1,4,1,11863,6,40,1,1,11),_TpRipTimeOutTimer_Type())
tpRipTimeOutTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:tpRipTimeOutTimer.setStatus(_A)
class _TpRipGarbageTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,500))
_TpRipGarbageTimer_Type.__name__=_B
_TpRipGarbageTimer_Object=MibScalar
tpRipGarbageTimer=_TpRipGarbageTimer_Object((1,3,6,1,4,1,11863,6,40,1,1,12),_TpRipGarbageTimer_Type())
tpRipGarbageTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:tpRipGarbageTimer.setStatus(_A)
_TpRipNetworkConfig_ObjectIdentity=ObjectIdentity
tpRipNetworkConfig=_TpRipNetworkConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,40,1,2))
_TpRipNetworkTable_Object=MibTable
tpRipNetworkTable=_TpRipNetworkTable_Object((1,3,6,1,4,1,11863,6,40,1,2,1))
if mibBuilder.loadTexts:tpRipNetworkTable.setStatus(_A)
_TpRipNetworkEntry_Object=MibTableRow
tpRipNetworkEntry=_TpRipNetworkEntry_Object((1,3,6,1,4,1,11863,6,40,1,2,1,1))
tpRipNetworkEntry.setIndexNames((0,_H,_K))
if mibBuilder.loadTexts:tpRipNetworkEntry.setStatus(_A)
_TpRipNetworkAddress_Type=IpAddress
_TpRipNetworkAddress_Object=MibTableColumn
tpRipNetworkAddress=_TpRipNetworkAddress_Object((1,3,6,1,4,1,11863,6,40,1,2,1,1,1),_TpRipNetworkAddress_Type())
tpRipNetworkAddress.setMaxAccess(_L)
if mibBuilder.loadTexts:tpRipNetworkAddress.setStatus(_A)
_TpRipNetworkStatus_Type=TPRowStatus
_TpRipNetworkStatus_Object=MibTableColumn
tpRipNetworkStatus=_TpRipNetworkStatus_Object((1,3,6,1,4,1,11863,6,40,1,2,1,1,2),_TpRipNetworkStatus_Type())
tpRipNetworkStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:tpRipNetworkStatus.setStatus(_A)
_TpRipInterfaceConfig_ObjectIdentity=ObjectIdentity
tpRipInterfaceConfig=_TpRipInterfaceConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,40,1,3))
_TpRipInterfaceTable_Object=MibTable
tpRipInterfaceTable=_TpRipInterfaceTable_Object((1,3,6,1,4,1,11863,6,40,1,3,1))
if mibBuilder.loadTexts:tpRipInterfaceTable.setStatus(_A)
_TpRipInterfaceEntry_Object=MibTableRow
tpRipInterfaceEntry=_TpRipInterfaceEntry_Object((1,3,6,1,4,1,11863,6,40,1,3,1,1))
tpRipInterfaceEntry.setIndexNames((0,_H,_M))
if mibBuilder.loadTexts:tpRipInterfaceEntry.setStatus(_A)
class _TpRipInterfaceID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_TpRipInterfaceID_Type.__name__=_G
_TpRipInterfaceID_Object=MibTableColumn
tpRipInterfaceID=_TpRipInterfaceID_Object((1,3,6,1,4,1,11863,6,40,1,3,1,1,1),_TpRipInterfaceID_Type())
tpRipInterfaceID.setMaxAccess(_F)
if mibBuilder.loadTexts:tpRipInterfaceID.setStatus(_A)
class _TpRipInterfaceStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_TpRipInterfaceStatus_Type.__name__=_G
_TpRipInterfaceStatus_Object=MibTableColumn
tpRipInterfaceStatus=_TpRipInterfaceStatus_Object((1,3,6,1,4,1,11863,6,40,1,3,1,1,2),_TpRipInterfaceStatus_Type())
tpRipInterfaceStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:tpRipInterfaceStatus.setStatus(_A)
class _TpRipInterfaceSendVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),('rip-1c',3)))
_TpRipInterfaceSendVersion_Type.__name__=_B
_TpRipInterfaceSendVersion_Object=MibTableColumn
tpRipInterfaceSendVersion=_TpRipInterfaceSendVersion_Object((1,3,6,1,4,1,11863,6,40,1,3,1,1,3),_TpRipInterfaceSendVersion_Type())
tpRipInterfaceSendVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:tpRipInterfaceSendVersion.setStatus(_A)
class _TpRipInterfaceRecvVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),('both',3)))
_TpRipInterfaceRecvVersion_Type.__name__=_B
_TpRipInterfaceRecvVersion_Object=MibTableColumn
tpRipInterfaceRecvVersion=_TpRipInterfaceRecvVersion_Object((1,3,6,1,4,1,11863,6,40,1,3,1,1,4),_TpRipInterfaceRecvVersion_Type())
tpRipInterfaceRecvVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:tpRipInterfaceRecvVersion.setStatus(_A)
class _TpRipInterfaceRIPv2Broad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpRipInterfaceRIPv2Broad_Type.__name__=_B
_TpRipInterfaceRIPv2Broad_Object=MibTableColumn
tpRipInterfaceRIPv2Broad=_TpRipInterfaceRIPv2Broad_Object((1,3,6,1,4,1,11863,6,40,1,3,1,1,5),_TpRipInterfaceRIPv2Broad_Type())
tpRipInterfaceRIPv2Broad.setMaxAccess(_C)
if mibBuilder.loadTexts:tpRipInterfaceRIPv2Broad.setStatus(_A)
class _TpRipInterfaceAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('simple',2),('md5',3)))
_TpRipInterfaceAuthMode_Type.__name__=_B
_TpRipInterfaceAuthMode_Object=MibTableColumn
tpRipInterfaceAuthMode=_TpRipInterfaceAuthMode_Object((1,3,6,1,4,1,11863,6,40,1,3,1,1,6),_TpRipInterfaceAuthMode_Type())
tpRipInterfaceAuthMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tpRipInterfaceAuthMode.setStatus(_A)
class _TpRipInterfaceKeyID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TpRipInterfaceKeyID_Type.__name__=_B
_TpRipInterfaceKeyID_Object=MibTableColumn
tpRipInterfaceKeyID=_TpRipInterfaceKeyID_Object((1,3,6,1,4,1,11863,6,40,1,3,1,1,7),_TpRipInterfaceKeyID_Type())
tpRipInterfaceKeyID.setMaxAccess(_C)
if mibBuilder.loadTexts:tpRipInterfaceKeyID.setStatus(_A)
class _TpRipInterfaceKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_TpRipInterfaceKey_Type.__name__=_G
_TpRipInterfaceKey_Object=MibTableColumn
tpRipInterfaceKey=_TpRipInterfaceKey_Object((1,3,6,1,4,1,11863,6,40,1,3,1,1,8),_TpRipInterfaceKey_Type())
tpRipInterfaceKey.setMaxAccess(_C)
if mibBuilder.loadTexts:tpRipInterfaceKey.setStatus(_A)
class _TpRipInterfaceSplitHorizon_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpRipInterfaceSplitHorizon_Type.__name__=_B
_TpRipInterfaceSplitHorizon_Object=MibTableColumn
tpRipInterfaceSplitHorizon=_TpRipInterfaceSplitHorizon_Object((1,3,6,1,4,1,11863,6,40,1,3,1,1,9),_TpRipInterfaceSplitHorizon_Type())
tpRipInterfaceSplitHorizon.setMaxAccess(_C)
if mibBuilder.loadTexts:tpRipInterfaceSplitHorizon.setStatus(_A)
class _TpRipInterfacePoisonReverse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpRipInterfacePoisonReverse_Type.__name__=_B
_TpRipInterfacePoisonReverse_Object=MibTableColumn
tpRipInterfacePoisonReverse=_TpRipInterfacePoisonReverse_Object((1,3,6,1,4,1,11863,6,40,1,3,1,1,10),_TpRipInterfacePoisonReverse_Type())
tpRipInterfacePoisonReverse.setMaxAccess(_C)
if mibBuilder.loadTexts:tpRipInterfacePoisonReverse.setStatus(_A)
_TpRipRouteItems_ObjectIdentity=ObjectIdentity
tpRipRouteItems=_TpRipRouteItems_ObjectIdentity((1,3,6,1,4,1,11863,6,40,1,4))
_TpRipRouteTable_Object=MibTable
tpRipRouteTable=_TpRipRouteTable_Object((1,3,6,1,4,1,11863,6,40,1,4,1))
if mibBuilder.loadTexts:tpRipRouteTable.setStatus(_A)
_TpRipRouteEntry_Object=MibTableRow
tpRipRouteEntry=_TpRipRouteEntry_Object((1,3,6,1,4,1,11863,6,40,1,4,1,1))
tpRipRouteEntry.setIndexNames((0,_H,_N))
if mibBuilder.loadTexts:tpRipRouteEntry.setStatus(_A)
class _TpRipIpAddressMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_TpRipIpAddressMask_Type.__name__=_G
_TpRipIpAddressMask_Object=MibTableColumn
tpRipIpAddressMask=_TpRipIpAddressMask_Object((1,3,6,1,4,1,11863,6,40,1,4,1,1,1),_TpRipIpAddressMask_Type())
tpRipIpAddressMask.setMaxAccess(_F)
if mibBuilder.loadTexts:tpRipIpAddressMask.setStatus(_A)
_TpRipGateway_Type=IpAddress
_TpRipGateway_Object=MibTableColumn
tpRipGateway=_TpRipGateway_Object((1,3,6,1,4,1,11863,6,40,1,4,1,1,2),_TpRipGateway_Type())
tpRipGateway.setMaxAccess(_F)
if mibBuilder.loadTexts:tpRipGateway.setStatus(_A)
class _TpRipMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_TpRipMetric_Type.__name__=_B
_TpRipMetric_Object=MibTableColumn
tpRipMetric=_TpRipMetric_Object((1,3,6,1,4,1,11863,6,40,1,4,1,1,3),_TpRipMetric_Type())
tpRipMetric.setMaxAccess(_F)
if mibBuilder.loadTexts:tpRipMetric.setStatus(_A)
class _TpRipInterfaceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_TpRipInterfaceName_Type.__name__=_G
_TpRipInterfaceName_Object=MibTableColumn
tpRipInterfaceName=_TpRipInterfaceName_Object((1,3,6,1,4,1,11863,6,40,1,4,1,1,4),_TpRipInterfaceName_Type())
tpRipInterfaceName.setMaxAccess(_F)
if mibBuilder.loadTexts:tpRipInterfaceName.setStatus(_A)
class _TpRipTimers_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_TpRipTimers_Type.__name__=_B
_TpRipTimers_Object=MibTableColumn
tpRipTimers=_TpRipTimers_Object((1,3,6,1,4,1,11863,6,40,1,4,1,1,5),_TpRipTimers_Type())
tpRipTimers.setMaxAccess(_F)
if mibBuilder.loadTexts:tpRipTimers.setStatus(_A)
_TplinkRipNotifications_ObjectIdentity=ObjectIdentity
tplinkRipNotifications=_TplinkRipNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,40,2))
mibBuilder.exportSymbols(_H,**{'tplinkRipMIB':tplinkRipMIB,'tplinkRipMIBObjects':tplinkRipMIBObjects,'tpRipBasicConfig':tpRipBasicConfig,'tpRipProtocolCtrl':tpRipProtocolCtrl,'tpRipProtocolVersion':tpRipProtocolVersion,'tpRipDistance':tpRipDistance,'tpRipAutoSumm':tpRipAutoSumm,'tpRipDefaultMetric':tpRipDefaultMetric,'tpRipRedistriStatic':tpRipRedistriStatic,'tpRipRedistriOspf':tpRipRedistriOspf,'tpRipRedistStaticMetric':tpRipRedistStaticMetric,'tpRipRedistOspfMetric':tpRipRedistOspfMetric,'tpRipUpdateTimer':tpRipUpdateTimer,'tpRipTimeOutTimer':tpRipTimeOutTimer,'tpRipGarbageTimer':tpRipGarbageTimer,'tpRipNetworkConfig':tpRipNetworkConfig,'tpRipNetworkTable':tpRipNetworkTable,'tpRipNetworkEntry':tpRipNetworkEntry,_K:tpRipNetworkAddress,'tpRipNetworkStatus':tpRipNetworkStatus,'tpRipInterfaceConfig':tpRipInterfaceConfig,'tpRipInterfaceTable':tpRipInterfaceTable,'tpRipInterfaceEntry':tpRipInterfaceEntry,_M:tpRipInterfaceID,'tpRipInterfaceStatus':tpRipInterfaceStatus,'tpRipInterfaceSendVersion':tpRipInterfaceSendVersion,'tpRipInterfaceRecvVersion':tpRipInterfaceRecvVersion,'tpRipInterfaceRIPv2Broad':tpRipInterfaceRIPv2Broad,'tpRipInterfaceAuthMode':tpRipInterfaceAuthMode,'tpRipInterfaceKeyID':tpRipInterfaceKeyID,'tpRipInterfaceKey':tpRipInterfaceKey,'tpRipInterfaceSplitHorizon':tpRipInterfaceSplitHorizon,'tpRipInterfacePoisonReverse':tpRipInterfacePoisonReverse,'tpRipRouteItems':tpRipRouteItems,'tpRipRouteTable':tpRipRouteTable,'tpRipRouteEntry':tpRipRouteEntry,_N:tpRipIpAddressMask,'tpRipGateway':tpRipGateway,'tpRipMetric':tpRipMetric,'tpRipInterfaceName':tpRipInterfaceName,'tpRipTimers':tpRipTimers,'tplinkRipNotifications':tplinkRipNotifications})