_K='mirror'
_J='normal-transmit'
_I='rcPort'
_H='rcStaticMacAddress'
_G='rcStaticMacVlan'
_F='not-accessible'
_E='SWITCH-MACCONFIG-MIB'
_D='read-write'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
rcMacConfig=ModuleIdentity((1,3,6,1,4,1,8886,6,1,3))
class EnableVar(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_RcStaticMacTable_Object=MibTable
rcStaticMacTable=_RcStaticMacTable_Object((1,3,6,1,4,1,8886,6,1,3,1))
if mibBuilder.loadTexts:rcStaticMacTable.setStatus(_A)
_RcStaticMacEntry_Object=MibTableRow
rcStaticMacEntry=_RcStaticMacEntry_Object((1,3,6,1,4,1,8886,6,1,3,1,1))
rcStaticMacEntry.setIndexNames((0,_E,_G),(0,_E,_H))
if mibBuilder.loadTexts:rcStaticMacEntry.setStatus(_A)
class _RcStaticMacVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcStaticMacVlan_Type.__name__=_B
_RcStaticMacVlan_Object=MibTableColumn
rcStaticMacVlan=_RcStaticMacVlan_Object((1,3,6,1,4,1,8886,6,1,3,1,1,1),_RcStaticMacVlan_Type())
rcStaticMacVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:rcStaticMacVlan.setStatus(_A)
_RcStaticMacAddress_Type=MacAddress
_RcStaticMacAddress_Object=MibTableColumn
rcStaticMacAddress=_RcStaticMacAddress_Object((1,3,6,1,4,1,8886,6,1,3,1,1,2),_RcStaticMacAddress_Type())
rcStaticMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:rcStaticMacAddress.setStatus(_A)
_RcStaticMacPort_Type=Integer32
_RcStaticMacPort_Object=MibTableColumn
rcStaticMacPort=_RcStaticMacPort_Object((1,3,6,1,4,1,8886,6,1,3,1,1,3),_RcStaticMacPort_Type())
rcStaticMacPort.setMaxAccess(_C)
if mibBuilder.loadTexts:rcStaticMacPort.setStatus(_A)
_RcStaticMacRowStatus_Type=RowStatus
_RcStaticMacRowStatus_Object=MibTableColumn
rcStaticMacRowStatus=_RcStaticMacRowStatus_Object((1,3,6,1,4,1,8886,6,1,3,1,1,4),_RcStaticMacRowStatus_Type())
rcStaticMacRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcStaticMacRowStatus.setStatus(_A)
class _RcStaticMacPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,7))
_RcStaticMacPriority_Type.__name__=_B
_RcStaticMacPriority_Object=MibTableColumn
rcStaticMacPriority=_RcStaticMacPriority_Object((1,3,6,1,4,1,8886,6,1,3,1,1,5),_RcStaticMacPriority_Type())
rcStaticMacPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:rcStaticMacPriority.setStatus(_A)
_RcStaticMacPolicyEnable_Type=EnableVar
_RcStaticMacPolicyEnable_Object=MibTableColumn
rcStaticMacPolicyEnable=_RcStaticMacPolicyEnable_Object((1,3,6,1,4,1,8886,6,1,3,1,1,6),_RcStaticMacPolicyEnable_Type())
rcStaticMacPolicyEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcStaticMacPolicyEnable.setStatus(_A)
_RcStaticMacNrlEnable_Type=EnableVar
_RcStaticMacNrlEnable_Object=MibTableColumn
rcStaticMacNrlEnable=_RcStaticMacNrlEnable_Object((1,3,6,1,4,1,8886,6,1,3,1,1,7),_RcStaticMacNrlEnable_Type())
rcStaticMacNrlEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcStaticMacNrlEnable.setStatus(_A)
_RcStaticMacBhEnable_Type=EnableVar
_RcStaticMacBhEnable_Object=MibTableColumn
rcStaticMacBhEnable=_RcStaticMacBhEnable_Object((1,3,6,1,4,1,8886,6,1,3,1,1,8),_RcStaticMacBhEnable_Type())
rcStaticMacBhEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcStaticMacBhEnable.setStatus(_A)
_RcMacCountGroup_ObjectIdentity=ObjectIdentity
rcMacCountGroup=_RcMacCountGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,3,2))
_RcQueryMacCountPort_Type=Integer32
_RcQueryMacCountPort_Object=MibScalar
rcQueryMacCountPort=_RcQueryMacCountPort_Object((1,3,6,1,4,1,8886,6,1,3,2,1),_RcQueryMacCountPort_Type())
rcQueryMacCountPort.setMaxAccess(_D)
if mibBuilder.loadTexts:rcQueryMacCountPort.setStatus(_A)
class _RcQueryMacCountVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_RcQueryMacCountVlan_Type.__name__=_B
_RcQueryMacCountVlan_Object=MibScalar
rcQueryMacCountVlan=_RcQueryMacCountVlan_Object((1,3,6,1,4,1,8886,6,1,3,2,2),_RcQueryMacCountVlan_Type())
rcQueryMacCountVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:rcQueryMacCountVlan.setStatus(_A)
_RcQueryMacCount_Type=Integer32
_RcQueryMacCount_Object=MibScalar
rcQueryMacCount=_RcQueryMacCount_Object((1,3,6,1,4,1,8886,6,1,3,2,3),_RcQueryMacCount_Type())
rcQueryMacCount.setMaxAccess(_D)
if mibBuilder.loadTexts:rcQueryMacCount.setStatus(_A)
_RcQueryMacTable_Type=Integer32
_RcQueryMacTable_Object=MibScalar
rcQueryMacTable=_RcQueryMacTable_Object((1,3,6,1,4,1,8886,6,1,3,2,4),_RcQueryMacTable_Type())
rcQueryMacTable.setMaxAccess(_D)
if mibBuilder.loadTexts:rcQueryMacTable.setStatus(_A)
_RcStaticMacPortTable_Object=MibTable
rcStaticMacPortTable=_RcStaticMacPortTable_Object((1,3,6,1,4,1,8886,6,1,3,3))
if mibBuilder.loadTexts:rcStaticMacPortTable.setStatus(_A)
_RcStaticMacPortEntry_Object=MibTableRow
rcStaticMacPortEntry=_RcStaticMacPortEntry_Object((1,3,6,1,4,1,8886,6,1,3,3,1))
rcStaticMacPortEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:rcStaticMacPortEntry.setStatus(_A)
_RcPort_Type=Integer32
_RcPort_Object=MibTableColumn
rcPort=_RcPort_Object((1,3,6,1,4,1,8886,6,1,3,3,1,1),_RcPort_Type())
rcPort.setMaxAccess(_F)
if mibBuilder.loadTexts:rcPort.setStatus(_A)
class _RcStaticSmacPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('drop',1),(_K,2)))
_RcStaticSmacPolicy_Type.__name__=_B
_RcStaticSmacPolicy_Object=MibTableColumn
rcStaticSmacPolicy=_RcStaticSmacPolicy_Object((1,3,6,1,4,1,8886,6,1,3,3,1,2),_RcStaticSmacPolicy_Type())
rcStaticSmacPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:rcStaticSmacPolicy.setStatus(_A)
class _RcStaticDmacPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('drop',1),(_K,2)))
_RcStaticDmacPolicy_Type.__name__=_B
_RcStaticDmacPolicy_Object=MibTableColumn
rcStaticDmacPolicy=_RcStaticDmacPolicy_Object((1,3,6,1,4,1,8886,6,1,3,3,1,3),_RcStaticDmacPolicy_Type())
rcStaticDmacPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:rcStaticDmacPolicy.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'EnableVar':EnableVar,'rcMacConfig':rcMacConfig,'rcStaticMacTable':rcStaticMacTable,'rcStaticMacEntry':rcStaticMacEntry,_G:rcStaticMacVlan,_H:rcStaticMacAddress,'rcStaticMacPort':rcStaticMacPort,'rcStaticMacRowStatus':rcStaticMacRowStatus,'rcStaticMacPriority':rcStaticMacPriority,'rcStaticMacPolicyEnable':rcStaticMacPolicyEnable,'rcStaticMacNrlEnable':rcStaticMacNrlEnable,'rcStaticMacBhEnable':rcStaticMacBhEnable,'rcMacCountGroup':rcMacCountGroup,'rcQueryMacCountPort':rcQueryMacCountPort,'rcQueryMacCountVlan':rcQueryMacCountVlan,'rcQueryMacCount':rcQueryMacCount,'rcQueryMacTable':rcQueryMacTable,'rcStaticMacPortTable':rcStaticMacPortTable,'rcStaticMacPortEntry':rcStaticMacPortEntry,_I:rcPort,'rcStaticSmacPolicy':rcStaticSmacPolicy,'rcStaticDmacPolicy':rcStaticDmacPolicy})