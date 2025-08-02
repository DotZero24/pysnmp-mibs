_F='rcmcVlanPortIndex'
_E='CONVERTOR-VLAN-MIB'
_D='EnableVar'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomMediaConvertor,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomMediaConvertor')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
EnableVar,PortList=mibBuilder.importSymbols('SWITCH-TC',_D,'PortList')
rcmcVlanConfig=ModuleIdentity((1,3,6,1,4,1,8886,16,1,2))
class _RcmcVlanCoreTagType_Type(Integer32):defaultValue=37120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RcmcVlanCoreTagType_Type.__name__=_C
_RcmcVlanCoreTagType_Object=MibScalar
rcmcVlanCoreTagType=_RcmcVlanCoreTagType_Object((1,3,6,1,4,1,8886,16,1,2,1),_RcmcVlanCoreTagType_Type())
rcmcVlanCoreTagType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcmcVlanCoreTagType.setStatus(_A)
class _RcmcVlanSwitchMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('transparent',1),('dot1q-vlan',2),('double-tagged-vlan',3)))
_RcmcVlanSwitchMode_Type.__name__=_C
_RcmcVlanSwitchMode_Object=MibScalar
rcmcVlanSwitchMode=_RcmcVlanSwitchMode_Object((1,3,6,1,4,1,8886,16,1,2,2),_RcmcVlanSwitchMode_Type())
rcmcVlanSwitchMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcmcVlanSwitchMode.setStatus(_A)
_RcmcVlanPortConfigTable_Object=MibTable
rcmcVlanPortConfigTable=_RcmcVlanPortConfigTable_Object((1,3,6,1,4,1,8886,16,1,2,3))
if mibBuilder.loadTexts:rcmcVlanPortConfigTable.setStatus(_A)
_RcmcVlanPortConfigEntry_Object=MibTableRow
rcmcVlanPortConfigEntry=_RcmcVlanPortConfigEntry_Object((1,3,6,1,4,1,8886,16,1,2,3,1))
rcmcVlanPortConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:rcmcVlanPortConfigEntry.setStatus(_A)
_RcmcVlanPortIndex_Type=Integer32
_RcmcVlanPortIndex_Object=MibTableColumn
rcmcVlanPortIndex=_RcmcVlanPortIndex_Object((1,3,6,1,4,1,8886,16,1,2,3,1,1),_RcmcVlanPortIndex_Type())
rcmcVlanPortIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rcmcVlanPortIndex.setStatus(_A)
class _RcmcVlanNative_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcmcVlanNative_Type.__name__=_C
_RcmcVlanNative_Object=MibTableColumn
rcmcVlanNative=_RcmcVlanNative_Object((1,3,6,1,4,1,8886,16,1,2,3,1,2),_RcmcVlanNative_Type())
rcmcVlanNative.setMaxAccess(_B)
if mibBuilder.loadTexts:rcmcVlanNative.setStatus(_A)
class _RcmcVlanNativeOverride_Type(EnableVar):defaultValue=2
_RcmcVlanNativeOverride_Type.__name__=_D
_RcmcVlanNativeOverride_Object=MibTableColumn
rcmcVlanNativeOverride=_RcmcVlanNativeOverride_Object((1,3,6,1,4,1,8886,16,1,2,3,1,3),_RcmcVlanNativeOverride_Type())
rcmcVlanNativeOverride.setMaxAccess(_B)
if mibBuilder.loadTexts:rcmcVlanNativeOverride.setStatus(_A)
class _RcmcVlanDoubleTagEnable_Type(EnableVar):defaultValue=2
_RcmcVlanDoubleTagEnable_Type.__name__=_D
_RcmcVlanDoubleTagEnable_Object=MibTableColumn
rcmcVlanDoubleTagEnable=_RcmcVlanDoubleTagEnable_Object((1,3,6,1,4,1,8886,16,1,2,3,1,4),_RcmcVlanDoubleTagEnable_Type())
rcmcVlanDoubleTagEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcmcVlanDoubleTagEnable.setStatus(_A)
class _RcmcVlanIngressFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('notmember',2),('unkown',3)))
_RcmcVlanIngressFilter_Type.__name__=_C
_RcmcVlanIngressFilter_Object=MibTableColumn
rcmcVlanIngressFilter=_RcmcVlanIngressFilter_Object((1,3,6,1,4,1,8886,16,1,2,3,1,5),_RcmcVlanIngressFilter_Type())
rcmcVlanIngressFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcmcVlanIngressFilter.setStatus(_A)
class _RcmcVlanAcceptFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('all',1),('tag',2),('untag',3)))
_RcmcVlanAcceptFrameType_Type.__name__=_C
_RcmcVlanAcceptFrameType_Object=MibTableColumn
rcmcVlanAcceptFrameType=_RcmcVlanAcceptFrameType_Object((1,3,6,1,4,1,8886,16,1,2,3,1,6),_RcmcVlanAcceptFrameType_Type())
rcmcVlanAcceptFrameType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcmcVlanAcceptFrameType.setStatus(_A)
class _RcmcVlanEgressDefault_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unmodify',1),('tag',2),('untag',3),('disable',4)))
_RcmcVlanEgressDefault_Type.__name__=_C
_RcmcVlanEgressDefault_Object=MibTableColumn
rcmcVlanEgressDefault=_RcmcVlanEgressDefault_Object((1,3,6,1,4,1,8886,16,1,2,3,1,7),_RcmcVlanEgressDefault_Type())
rcmcVlanEgressDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:rcmcVlanEgressDefault.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'rcmcVlanConfig':rcmcVlanConfig,'rcmcVlanCoreTagType':rcmcVlanCoreTagType,'rcmcVlanSwitchMode':rcmcVlanSwitchMode,'rcmcVlanPortConfigTable':rcmcVlanPortConfigTable,'rcmcVlanPortConfigEntry':rcmcVlanPortConfigEntry,_F:rcmcVlanPortIndex,'rcmcVlanNative':rcmcVlanNative,'rcmcVlanNativeOverride':rcmcVlanNativeOverride,'rcmcVlanDoubleTagEnable':rcmcVlanDoubleTagEnable,'rcmcVlanIngressFilter':rcmcVlanIngressFilter,'rcmcVlanAcceptFrameType':rcmcVlanAcceptFrameType,'rcmcVlanEgressDefault':rcmcVlanEgressDefault})