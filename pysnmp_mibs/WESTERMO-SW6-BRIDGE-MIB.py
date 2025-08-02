_U='groupConfigRstp'
_T='cfgRstpPortAutoEdge'
_S='cfgRstpPortPathCost'
_R='cfgRstpPortPriority'
_Q='cfgRstpPortName'
_P='cfgRstpPortEnabled'
_O='cfgRstpBridgeTransmitHoldCount'
_N='cfgRstpBridgeMaxAge'
_M='cfgRstpBridgeForwardDelay'
_L='cfgRstpBridgeHelloTime'
_K='cfgRstpBridgePriority'
_J='cfgRstpBridgeEnabled'
_I='cfgRstpPortIndex'
_H='read-only'
_G='DisplayString'
_F='enabled'
_E='disabled'
_D='read-write'
_C='Integer32'
_B='WESTERMO-SW6-BRIDGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
rstp=ModuleIdentity((1,3,6,1,4,1,16177,1,400,2,8))
if mibBuilder.loadTexts:rstp.setRevisions(('2019-09-06 00:00',))
_Configuration_ObjectIdentity=ObjectIdentity
configuration=_Configuration_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,8,1))
_CfgRstpBridge_ObjectIdentity=ObjectIdentity
cfgRstpBridge=_CfgRstpBridge_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,8,1,1))
class _CfgRstpBridgeEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CfgRstpBridgeEnabled_Type.__name__=_C
_CfgRstpBridgeEnabled_Object=MibScalar
cfgRstpBridgeEnabled=_CfgRstpBridgeEnabled_Object((1,3,6,1,4,1,16177,1,400,2,8,1,1,1),_CfgRstpBridgeEnabled_Type())
cfgRstpBridgeEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgRstpBridgeEnabled.setStatus(_A)
class _CfgRstpBridgePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_CfgRstpBridgePriority_Type.__name__=_C
_CfgRstpBridgePriority_Object=MibScalar
cfgRstpBridgePriority=_CfgRstpBridgePriority_Object((1,3,6,1,4,1,16177,1,400,2,8,1,1,2),_CfgRstpBridgePriority_Type())
cfgRstpBridgePriority.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgRstpBridgePriority.setStatus(_A)
class _CfgRstpBridgeHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,2))
_CfgRstpBridgeHelloTime_Type.__name__=_C
_CfgRstpBridgeHelloTime_Object=MibScalar
cfgRstpBridgeHelloTime=_CfgRstpBridgeHelloTime_Object((1,3,6,1,4,1,16177,1,400,2,8,1,1,3),_CfgRstpBridgeHelloTime_Type())
cfgRstpBridgeHelloTime.setMaxAccess(_H)
if mibBuilder.loadTexts:cfgRstpBridgeHelloTime.setStatus(_A)
class _CfgRstpBridgeForwardDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_CfgRstpBridgeForwardDelay_Type.__name__=_C
_CfgRstpBridgeForwardDelay_Object=MibScalar
cfgRstpBridgeForwardDelay=_CfgRstpBridgeForwardDelay_Object((1,3,6,1,4,1,16177,1,400,2,8,1,1,4),_CfgRstpBridgeForwardDelay_Type())
cfgRstpBridgeForwardDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgRstpBridgeForwardDelay.setStatus(_A)
class _CfgRstpBridgeMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_CfgRstpBridgeMaxAge_Type.__name__=_C
_CfgRstpBridgeMaxAge_Object=MibScalar
cfgRstpBridgeMaxAge=_CfgRstpBridgeMaxAge_Object((1,3,6,1,4,1,16177,1,400,2,8,1,1,5),_CfgRstpBridgeMaxAge_Type())
cfgRstpBridgeMaxAge.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgRstpBridgeMaxAge.setStatus(_A)
class _CfgRstpBridgeTransmitHoldCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CfgRstpBridgeTransmitHoldCount_Type.__name__=_C
_CfgRstpBridgeTransmitHoldCount_Object=MibScalar
cfgRstpBridgeTransmitHoldCount=_CfgRstpBridgeTransmitHoldCount_Object((1,3,6,1,4,1,16177,1,400,2,8,1,1,6),_CfgRstpBridgeTransmitHoldCount_Type())
cfgRstpBridgeTransmitHoldCount.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgRstpBridgeTransmitHoldCount.setStatus(_A)
_CfgRstpPort_ObjectIdentity=ObjectIdentity
cfgRstpPort=_CfgRstpPort_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,8,1,2))
_CfgRstpPortTable_Object=MibTable
cfgRstpPortTable=_CfgRstpPortTable_Object((1,3,6,1,4,1,16177,1,400,2,8,1,2,1))
if mibBuilder.loadTexts:cfgRstpPortTable.setStatus(_A)
_CfgRstpPortTableEntry_Object=MibTableRow
cfgRstpPortTableEntry=_CfgRstpPortTableEntry_Object((1,3,6,1,4,1,16177,1,400,2,8,1,2,1,1))
cfgRstpPortTableEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:cfgRstpPortTableEntry.setStatus(_A)
class _CfgRstpPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,18))
_CfgRstpPortIndex_Type.__name__=_C
_CfgRstpPortIndex_Object=MibTableColumn
cfgRstpPortIndex=_CfgRstpPortIndex_Object((1,3,6,1,4,1,16177,1,400,2,8,1,2,1,1,1),_CfgRstpPortIndex_Type())
cfgRstpPortIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cfgRstpPortIndex.setStatus(_A)
class _CfgRstpPortEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CfgRstpPortEnabled_Type.__name__=_C
_CfgRstpPortEnabled_Object=MibTableColumn
cfgRstpPortEnabled=_CfgRstpPortEnabled_Object((1,3,6,1,4,1,16177,1,400,2,8,1,2,1,1,2),_CfgRstpPortEnabled_Type())
cfgRstpPortEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgRstpPortEnabled.setStatus(_A)
class _CfgRstpPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CfgRstpPortName_Type.__name__=_G
_CfgRstpPortName_Object=MibTableColumn
cfgRstpPortName=_CfgRstpPortName_Object((1,3,6,1,4,1,16177,1,400,2,8,1,2,1,1,3),_CfgRstpPortName_Type())
cfgRstpPortName.setMaxAccess(_H)
if mibBuilder.loadTexts:cfgRstpPortName.setStatus(_A)
class _CfgRstpPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_CfgRstpPortPriority_Type.__name__=_C
_CfgRstpPortPriority_Object=MibTableColumn
cfgRstpPortPriority=_CfgRstpPortPriority_Object((1,3,6,1,4,1,16177,1,400,2,8,1,2,1,1,4),_CfgRstpPortPriority_Type())
cfgRstpPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgRstpPortPriority.setStatus(_A)
class _CfgRstpPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,5000000))
_CfgRstpPortPathCost_Type.__name__=_C
_CfgRstpPortPathCost_Object=MibTableColumn
cfgRstpPortPathCost=_CfgRstpPortPathCost_Object((1,3,6,1,4,1,16177,1,400,2,8,1,2,1,1,5),_CfgRstpPortPathCost_Type())
cfgRstpPortPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgRstpPortPathCost.setStatus(_A)
class _CfgRstpPortAutoEdge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CfgRstpPortAutoEdge_Type.__name__=_C
_CfgRstpPortAutoEdge_Object=MibTableColumn
cfgRstpPortAutoEdge=_CfgRstpPortAutoEdge_Object((1,3,6,1,4,1,16177,1,400,2,8,1,2,1,1,6),_CfgRstpPortAutoEdge_Type())
cfgRstpPortAutoEdge.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgRstpPortAutoEdge.setStatus(_A)
_Conformance_ObjectIdentity=ObjectIdentity
conformance=_Conformance_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,8,10000))
_Groups_ObjectIdentity=ObjectIdentity
groups=_Groups_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,8,10000,1))
_GroupConfiguration_ObjectIdentity=ObjectIdentity
groupConfiguration=_GroupConfiguration_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,8,10000,1,1))
_Compliances_ObjectIdentity=ObjectIdentity
compliances=_Compliances_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,8,10000,2))
groupConfigRstp=ObjectGroup((1,3,6,1,4,1,16177,1,400,2,8,10000,1,1,1))
groupConfigRstp.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:groupConfigRstp.setStatus(_A)
compliance=ModuleCompliance((1,3,6,1,4,1,16177,1,400,2,8,10000,2,1))
compliance.setObjects((_B,_U))
if mibBuilder.loadTexts:compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rstp':rstp,'configuration':configuration,'cfgRstpBridge':cfgRstpBridge,_J:cfgRstpBridgeEnabled,_K:cfgRstpBridgePriority,_L:cfgRstpBridgeHelloTime,_M:cfgRstpBridgeForwardDelay,_N:cfgRstpBridgeMaxAge,_O:cfgRstpBridgeTransmitHoldCount,'cfgRstpPort':cfgRstpPort,'cfgRstpPortTable':cfgRstpPortTable,'cfgRstpPortTableEntry':cfgRstpPortTableEntry,_I:cfgRstpPortIndex,_P:cfgRstpPortEnabled,_Q:cfgRstpPortName,_R:cfgRstpPortPriority,_S:cfgRstpPortPathCost,_T:cfgRstpPortAutoEdge,'conformance':conformance,'groups':groups,'groupConfiguration':groupConfiguration,_U:groupConfigRstp,'compliances':compliances,'compliance':compliance})