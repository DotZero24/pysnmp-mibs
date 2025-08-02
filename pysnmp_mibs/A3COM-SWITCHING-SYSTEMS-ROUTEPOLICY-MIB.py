_I='a3ComRoutePolicyIpIfAddressIndex'
_H='a3ComRoutePolicyIpIfIndex'
_G='a3ComRoutePolicyIndex'
_F='read-only'
_E='A3COM-SWITCHING-SYSTEMS-ROUTEPOLICY-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
class RowStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('active',1),('notInService',2),('notReady',3),('createAndGo',4),('createAndWait',5),('destroy',6)))
_A3Com_ObjectIdentity=ObjectIdentity
a3Com=_A3Com_ObjectIdentity((1,3,6,1,4,1,43))
_SwitchingSystemsMibs_ObjectIdentity=ObjectIdentity
switchingSystemsMibs=_SwitchingSystemsMibs_ObjectIdentity((1,3,6,1,4,1,43,29))
_A3ComSwitchingSystemsMib_ObjectIdentity=ObjectIdentity
a3ComSwitchingSystemsMib=_A3ComSwitchingSystemsMib_ObjectIdentity((1,3,6,1,4,1,43,29,4))
_A3ComRoutePolicy_ObjectIdentity=ObjectIdentity
a3ComRoutePolicy=_A3ComRoutePolicy_ObjectIdentity((1,3,6,1,4,1,43,29,4,23))
_A3ComRoutePolicyTable_Object=MibTable
a3ComRoutePolicyTable=_A3ComRoutePolicyTable_Object((1,3,6,1,4,1,43,29,4,23,1))
if mibBuilder.loadTexts:a3ComRoutePolicyTable.setStatus(_A)
_A3ComRoutePolicyEntry_Object=MibTableRow
a3ComRoutePolicyEntry=_A3ComRoutePolicyEntry_Object((1,3,6,1,4,1,43,29,4,23,1,1))
a3ComRoutePolicyEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:a3ComRoutePolicyEntry.setStatus(_A)
class _A3ComRoutePolicyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_A3ComRoutePolicyIndex_Type.__name__=_C
_A3ComRoutePolicyIndex_Object=MibTableColumn
a3ComRoutePolicyIndex=_A3ComRoutePolicyIndex_Object((1,3,6,1,4,1,43,29,4,23,1,1,1),_A3ComRoutePolicyIndex_Type())
a3ComRoutePolicyIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:a3ComRoutePolicyIndex.setStatus(_A)
class _A3ComRoutePolicyProtocolType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('undefined',1),('ip-rip',2),('ip-ospf',3),('ip-bgp4',4),('ipx-rip',5),('ipx-sap',6),('at-rtmp',7),('at-kip',8),('at-aurp',9)))
_A3ComRoutePolicyProtocolType_Type.__name__=_C
_A3ComRoutePolicyProtocolType_Object=MibTableColumn
a3ComRoutePolicyProtocolType=_A3ComRoutePolicyProtocolType_Object((1,3,6,1,4,1,43,29,4,23,1,1,2),_A3ComRoutePolicyProtocolType_Type())
a3ComRoutePolicyProtocolType.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComRoutePolicyProtocolType.setStatus(_A)
class _A3ComRoutePolicyType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('import',1),('export',2)))
_A3ComRoutePolicyType_Type.__name__=_C
_A3ComRoutePolicyType_Object=MibTableColumn
a3ComRoutePolicyType=_A3ComRoutePolicyType_Object((1,3,6,1,4,1,43,29,4,23,1,1,3),_A3ComRoutePolicyType_Type())
a3ComRoutePolicyType.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComRoutePolicyType.setStatus(_A)
class _A3ComRoutePolicyOriginProtocol_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_A3ComRoutePolicyOriginProtocol_Type.__name__=_C
_A3ComRoutePolicyOriginProtocol_Object=MibTableColumn
a3ComRoutePolicyOriginProtocol=_A3ComRoutePolicyOriginProtocol_Object((1,3,6,1,4,1,43,29,4,23,1,1,4),_A3ComRoutePolicyOriginProtocol_Type())
a3ComRoutePolicyOriginProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComRoutePolicyOriginProtocol.setStatus(_A)
class _A3ComRoutePolicySourceAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_A3ComRoutePolicySourceAddress_Type.__name__=_D
_A3ComRoutePolicySourceAddress_Object=MibTableColumn
a3ComRoutePolicySourceAddress=_A3ComRoutePolicySourceAddress_Object((1,3,6,1,4,1,43,29,4,23,1,1,5),_A3ComRoutePolicySourceAddress_Type())
a3ComRoutePolicySourceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComRoutePolicySourceAddress.setStatus(_A)
class _A3ComRoutePolicyRouteAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_A3ComRoutePolicyRouteAddress_Type.__name__=_D
_A3ComRoutePolicyRouteAddress_Object=MibTableColumn
a3ComRoutePolicyRouteAddress=_A3ComRoutePolicyRouteAddress_Object((1,3,6,1,4,1,43,29,4,23,1,1,6),_A3ComRoutePolicyRouteAddress_Type())
a3ComRoutePolicyRouteAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComRoutePolicyRouteAddress.setStatus(_A)
class _A3ComRoutePolicyRouteMask_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_A3ComRoutePolicyRouteMask_Type.__name__=_D
_A3ComRoutePolicyRouteMask_Object=MibTableColumn
a3ComRoutePolicyRouteMask=_A3ComRoutePolicyRouteMask_Object((1,3,6,1,4,1,43,29,4,23,1,1,7),_A3ComRoutePolicyRouteMask_Type())
a3ComRoutePolicyRouteMask.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComRoutePolicyRouteMask.setStatus(_A)
class _A3ComRoutePolicyAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('accept',1),('reject',2)))
_A3ComRoutePolicyAction_Type.__name__=_C
_A3ComRoutePolicyAction_Object=MibTableColumn
a3ComRoutePolicyAction=_A3ComRoutePolicyAction_Object((1,3,6,1,4,1,43,29,4,23,1,1,8),_A3ComRoutePolicyAction_Type())
a3ComRoutePolicyAction.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComRoutePolicyAction.setStatus(_A)
class _A3ComRoutePolicyAdjustMetric_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noop',1),('add',2),('subtract',3),('multiply',4),('divide',5),('module',6)))
_A3ComRoutePolicyAdjustMetric_Type.__name__=_C
_A3ComRoutePolicyAdjustMetric_Object=MibTableColumn
a3ComRoutePolicyAdjustMetric=_A3ComRoutePolicyAdjustMetric_Object((1,3,6,1,4,1,43,29,4,23,1,1,9),_A3ComRoutePolicyAdjustMetric_Type())
a3ComRoutePolicyAdjustMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComRoutePolicyAdjustMetric.setStatus(_A)
class _A3ComRoutePolicyMetric_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_A3ComRoutePolicyMetric_Type.__name__=_C
_A3ComRoutePolicyMetric_Object=MibTableColumn
a3ComRoutePolicyMetric=_A3ComRoutePolicyMetric_Object((1,3,6,1,4,1,43,29,4,23,1,1,10),_A3ComRoutePolicyMetric_Type())
a3ComRoutePolicyMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComRoutePolicyMetric.setStatus(_A)
class _A3ComRoutePolicyWeight_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_A3ComRoutePolicyWeight_Type.__name__=_C
_A3ComRoutePolicyWeight_Object=MibTableColumn
a3ComRoutePolicyWeight=_A3ComRoutePolicyWeight_Object((1,3,6,1,4,1,43,29,4,23,1,1,11),_A3ComRoutePolicyWeight_Type())
a3ComRoutePolicyWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComRoutePolicyWeight.setStatus(_A)
class _A3ComRoutePolicyExportType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ip-ospf-type1',1),('ip-ospf-type2',2),('default',3)))
_A3ComRoutePolicyExportType_Type.__name__=_C
_A3ComRoutePolicyExportType_Object=MibTableColumn
a3ComRoutePolicyExportType=_A3ComRoutePolicyExportType_Object((1,3,6,1,4,1,43,29,4,23,1,1,12),_A3ComRoutePolicyExportType_Type())
a3ComRoutePolicyExportType.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComRoutePolicyExportType.setStatus(_A)
_A3ComRoutePolicyRowStatus_Type=RowStatus
_A3ComRoutePolicyRowStatus_Object=MibTableColumn
a3ComRoutePolicyRowStatus=_A3ComRoutePolicyRowStatus_Object((1,3,6,1,4,1,43,29,4,23,1,1,13),_A3ComRoutePolicyRowStatus_Type())
a3ComRoutePolicyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComRoutePolicyRowStatus.setStatus(_A)
class _A3ComRoutePolicyNextFreeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_A3ComRoutePolicyNextFreeIndex_Type.__name__=_C
_A3ComRoutePolicyNextFreeIndex_Object=MibScalar
a3ComRoutePolicyNextFreeIndex=_A3ComRoutePolicyNextFreeIndex_Object((1,3,6,1,4,1,43,29,4,23,2),_A3ComRoutePolicyNextFreeIndex_Type())
a3ComRoutePolicyNextFreeIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:a3ComRoutePolicyNextFreeIndex.setStatus(_A)
_A3ComRoutePolicyIpIfTable_Object=MibTable
a3ComRoutePolicyIpIfTable=_A3ComRoutePolicyIpIfTable_Object((1,3,6,1,4,1,43,29,4,23,3))
if mibBuilder.loadTexts:a3ComRoutePolicyIpIfTable.setStatus(_A)
_A3ComRoutePolicyIpIfEntry_Object=MibTableRow
a3ComRoutePolicyIpIfEntry=_A3ComRoutePolicyIpIfEntry_Object((1,3,6,1,4,1,43,29,4,23,3,1))
a3ComRoutePolicyIpIfEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:a3ComRoutePolicyIpIfEntry.setStatus(_A)
class _A3ComRoutePolicyIpIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_A3ComRoutePolicyIpIfIndex_Type.__name__=_C
_A3ComRoutePolicyIpIfIndex_Object=MibTableColumn
a3ComRoutePolicyIpIfIndex=_A3ComRoutePolicyIpIfIndex_Object((1,3,6,1,4,1,43,29,4,23,3,1,1),_A3ComRoutePolicyIpIfIndex_Type())
a3ComRoutePolicyIpIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:a3ComRoutePolicyIpIfIndex.setStatus(_A)
_A3ComRoutePolicyIpIfAddressIndex_Type=IpAddress
_A3ComRoutePolicyIpIfAddressIndex_Object=MibTableColumn
a3ComRoutePolicyIpIfAddressIndex=_A3ComRoutePolicyIpIfAddressIndex_Object((1,3,6,1,4,1,43,29,4,23,3,1,2),_A3ComRoutePolicyIpIfAddressIndex_Type())
a3ComRoutePolicyIpIfAddressIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:a3ComRoutePolicyIpIfAddressIndex.setStatus(_A)
_A3ComRoutePolicyIpIfRowStatus_Type=RowStatus
_A3ComRoutePolicyIpIfRowStatus_Object=MibTableColumn
a3ComRoutePolicyIpIfRowStatus=_A3ComRoutePolicyIpIfRowStatus_Object((1,3,6,1,4,1,43,29,4,23,3,1,3),_A3ComRoutePolicyIpIfRowStatus_Type())
a3ComRoutePolicyIpIfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComRoutePolicyIpIfRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'RowStatus':RowStatus,'a3Com':a3Com,'switchingSystemsMibs':switchingSystemsMibs,'a3ComSwitchingSystemsMib':a3ComSwitchingSystemsMib,'a3ComRoutePolicy':a3ComRoutePolicy,'a3ComRoutePolicyTable':a3ComRoutePolicyTable,'a3ComRoutePolicyEntry':a3ComRoutePolicyEntry,_G:a3ComRoutePolicyIndex,'a3ComRoutePolicyProtocolType':a3ComRoutePolicyProtocolType,'a3ComRoutePolicyType':a3ComRoutePolicyType,'a3ComRoutePolicyOriginProtocol':a3ComRoutePolicyOriginProtocol,'a3ComRoutePolicySourceAddress':a3ComRoutePolicySourceAddress,'a3ComRoutePolicyRouteAddress':a3ComRoutePolicyRouteAddress,'a3ComRoutePolicyRouteMask':a3ComRoutePolicyRouteMask,'a3ComRoutePolicyAction':a3ComRoutePolicyAction,'a3ComRoutePolicyAdjustMetric':a3ComRoutePolicyAdjustMetric,'a3ComRoutePolicyMetric':a3ComRoutePolicyMetric,'a3ComRoutePolicyWeight':a3ComRoutePolicyWeight,'a3ComRoutePolicyExportType':a3ComRoutePolicyExportType,'a3ComRoutePolicyRowStatus':a3ComRoutePolicyRowStatus,'a3ComRoutePolicyNextFreeIndex':a3ComRoutePolicyNextFreeIndex,'a3ComRoutePolicyIpIfTable':a3ComRoutePolicyIpIfTable,'a3ComRoutePolicyIpIfEntry':a3ComRoutePolicyIpIfEntry,_H:a3ComRoutePolicyIpIfIndex,_I:a3ComRoutePolicyIpIfAddressIndex,'a3ComRoutePolicyIpIfRowStatus':a3ComRoutePolicyIpIfRowStatus})