_Y='groupSwIcl'
_X='groupSetIcl'
_W='groupRpcIcl'
_V='groupCfgIcl'
_U='swIclStatus'
_T='setIclSuspended'
_S='rpcIclClearBlacklist'
_R='rpcIclForceDisconnect'
_Q='cfgIclSuspended'
_P='cfgIclBlacklistTime'
_O='cfgIclCycleTime'
_N='cfgIclInterfaceName'
_M='cfgIclDisconnectionThreshold'
_L='cfgIclDisconnectionDelay'
_K='cfgIclConnectionThreshold'
_J='cfgIclConnectionDelay'
_I='cfgIclEnabled'
_H='resumed'
_G='disabled'
_F='DisplayString'
_E='suspended'
_D='read-write'
_C='Integer32'
_B='WESTERMO-SW6-ICL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
icl=ModuleIdentity((1,3,6,1,4,1,16177,1,400,2,5))
if mibBuilder.loadTexts:icl.setRevisions(('2019-09-06 00:00',))
_Configuration_ObjectIdentity=ObjectIdentity
configuration=_Configuration_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,5,1))
_CfgIcl_ObjectIdentity=ObjectIdentity
cfgIcl=_CfgIcl_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,5,1,1))
class _CfgIclEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),('enabled',1)))
_CfgIclEnabled_Type.__name__=_C
_CfgIclEnabled_Object=MibScalar
cfgIclEnabled=_CfgIclEnabled_Object((1,3,6,1,4,1,16177,1,400,2,5,1,1,1),_CfgIclEnabled_Type())
cfgIclEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgIclEnabled.setStatus(_A)
class _CfgIclConnectionDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_CfgIclConnectionDelay_Type.__name__=_C
_CfgIclConnectionDelay_Object=MibScalar
cfgIclConnectionDelay=_CfgIclConnectionDelay_Object((1,3,6,1,4,1,16177,1,400,2,5,1,1,2),_CfgIclConnectionDelay_Type())
cfgIclConnectionDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgIclConnectionDelay.setStatus(_A)
class _CfgIclConnectionThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-90,0))
_CfgIclConnectionThreshold_Type.__name__=_C
_CfgIclConnectionThreshold_Object=MibScalar
cfgIclConnectionThreshold=_CfgIclConnectionThreshold_Object((1,3,6,1,4,1,16177,1,400,2,5,1,1,3),_CfgIclConnectionThreshold_Type())
cfgIclConnectionThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgIclConnectionThreshold.setStatus(_A)
class _CfgIclDisconnectionDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_CfgIclDisconnectionDelay_Type.__name__=_C
_CfgIclDisconnectionDelay_Object=MibScalar
cfgIclDisconnectionDelay=_CfgIclDisconnectionDelay_Object((1,3,6,1,4,1,16177,1,400,2,5,1,1,4),_CfgIclDisconnectionDelay_Type())
cfgIclDisconnectionDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgIclDisconnectionDelay.setStatus(_A)
class _CfgIclDisconnectionThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-90,0))
_CfgIclDisconnectionThreshold_Type.__name__=_C
_CfgIclDisconnectionThreshold_Object=MibScalar
cfgIclDisconnectionThreshold=_CfgIclDisconnectionThreshold_Object((1,3,6,1,4,1,16177,1,400,2,5,1,1,5),_CfgIclDisconnectionThreshold_Type())
cfgIclDisconnectionThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgIclDisconnectionThreshold.setStatus(_A)
class _CfgIclInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CfgIclInterfaceName_Type.__name__=_F
_CfgIclInterfaceName_Object=MibScalar
cfgIclInterfaceName=_CfgIclInterfaceName_Object((1,3,6,1,4,1,16177,1,400,2,5,1,1,6),_CfgIclInterfaceName_Type())
cfgIclInterfaceName.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgIclInterfaceName.setStatus(_A)
class _CfgIclCycleTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,60))
_CfgIclCycleTime_Type.__name__=_C
_CfgIclCycleTime_Object=MibScalar
cfgIclCycleTime=_CfgIclCycleTime_Object((1,3,6,1,4,1,16177,1,400,2,5,1,1,7),_CfgIclCycleTime_Type())
cfgIclCycleTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgIclCycleTime.setStatus(_A)
class _CfgIclBlacklistTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_CfgIclBlacklistTime_Type.__name__=_C
_CfgIclBlacklistTime_Object=MibScalar
cfgIclBlacklistTime=_CfgIclBlacklistTime_Object((1,3,6,1,4,1,16177,1,400,2,5,1,1,8),_CfgIclBlacklistTime_Type())
cfgIclBlacklistTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgIclBlacklistTime.setStatus(_A)
class _CfgIclSuspended_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_E,1)))
_CfgIclSuspended_Type.__name__=_C
_CfgIclSuspended_Object=MibScalar
cfgIclSuspended=_CfgIclSuspended_Object((1,3,6,1,4,1,16177,1,400,2,5,1,1,9),_CfgIclSuspended_Type())
cfgIclSuspended.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgIclSuspended.setStatus(_A)
_Rpc_ObjectIdentity=ObjectIdentity
rpc=_Rpc_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,5,3))
_RpcIcl_ObjectIdentity=ObjectIdentity
rpcIcl=_RpcIcl_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,5,3,1))
class _RpcIclForceDisconnect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('nop',0),('disconnect',1)))
_RpcIclForceDisconnect_Type.__name__=_C
_RpcIclForceDisconnect_Object=MibScalar
rpcIclForceDisconnect=_RpcIclForceDisconnect_Object((1,3,6,1,4,1,16177,1,400,2,5,3,1,1),_RpcIclForceDisconnect_Type())
rpcIclForceDisconnect.setMaxAccess(_D)
if mibBuilder.loadTexts:rpcIclForceDisconnect.setStatus(_A)
class _RpcIclClearBlacklist_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('nop',0),('clear',1)))
_RpcIclClearBlacklist_Type.__name__=_C
_RpcIclClearBlacklist_Object=MibScalar
rpcIclClearBlacklist=_RpcIclClearBlacklist_Object((1,3,6,1,4,1,16177,1,400,2,5,3,1,2),_RpcIclClearBlacklist_Type())
rpcIclClearBlacklist.setMaxAccess(_D)
if mibBuilder.loadTexts:rpcIclClearBlacklist.setStatus(_A)
_Settings_ObjectIdentity=ObjectIdentity
settings=_Settings_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,5,4))
_SetIcl_ObjectIdentity=ObjectIdentity
setIcl=_SetIcl_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,5,4,1))
class _SetIclSuspended_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_E,1)))
_SetIclSuspended_Type.__name__=_C
_SetIclSuspended_Object=MibScalar
setIclSuspended=_SetIclSuspended_Object((1,3,6,1,4,1,16177,1,400,2,5,4,1,1),_SetIclSuspended_Type())
setIclSuspended.setMaxAccess(_D)
if mibBuilder.loadTexts:setIclSuspended.setStatus(_A)
_Software_ObjectIdentity=ObjectIdentity
software=_Software_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,5,6))
_SwIcl_ObjectIdentity=ObjectIdentity
swIcl=_SwIcl_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,5,6,1))
class _SwIclStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),('scanning',1),('connected',2),(_E,3)))
_SwIclStatus_Type.__name__=_C
_SwIclStatus_Object=MibScalar
swIclStatus=_SwIclStatus_Object((1,3,6,1,4,1,16177,1,400,2,5,6,1,1),_SwIclStatus_Type())
swIclStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:swIclStatus.setStatus(_A)
_Conformance_ObjectIdentity=ObjectIdentity
conformance=_Conformance_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,5,10000))
_Groups_ObjectIdentity=ObjectIdentity
groups=_Groups_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,5,10000,1))
_GroupConfiguration_ObjectIdentity=ObjectIdentity
groupConfiguration=_GroupConfiguration_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,5,10000,1,1))
_GroupRpc_ObjectIdentity=ObjectIdentity
groupRpc=_GroupRpc_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,5,10000,1,2))
_GroupSettings_ObjectIdentity=ObjectIdentity
groupSettings=_GroupSettings_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,5,10000,1,3))
_GroupSoftware_ObjectIdentity=ObjectIdentity
groupSoftware=_GroupSoftware_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,5,10000,1,4))
_Compliances_ObjectIdentity=ObjectIdentity
compliances=_Compliances_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,5,10000,2))
groupCfgIcl=ObjectGroup((1,3,6,1,4,1,16177,1,400,2,5,10000,1,1,1))
groupCfgIcl.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:groupCfgIcl.setStatus(_A)
groupRpcIcl=ObjectGroup((1,3,6,1,4,1,16177,1,400,2,5,10000,1,2,1))
groupRpcIcl.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:groupRpcIcl.setStatus(_A)
groupSetIcl=ObjectGroup((1,3,6,1,4,1,16177,1,400,2,5,10000,1,3,1))
groupSetIcl.setObjects((_B,_T))
if mibBuilder.loadTexts:groupSetIcl.setStatus(_A)
groupSwIcl=ObjectGroup((1,3,6,1,4,1,16177,1,400,2,5,10000,1,4,1))
groupSwIcl.setObjects((_B,_U))
if mibBuilder.loadTexts:groupSwIcl.setStatus(_A)
compliance=ModuleCompliance((1,3,6,1,4,1,16177,1,400,2,5,10000,2,1))
compliance.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'icl':icl,'configuration':configuration,'cfgIcl':cfgIcl,_I:cfgIclEnabled,_J:cfgIclConnectionDelay,_K:cfgIclConnectionThreshold,_L:cfgIclDisconnectionDelay,_M:cfgIclDisconnectionThreshold,_N:cfgIclInterfaceName,_O:cfgIclCycleTime,_P:cfgIclBlacklistTime,_Q:cfgIclSuspended,'rpc':rpc,'rpcIcl':rpcIcl,_R:rpcIclForceDisconnect,_S:rpcIclClearBlacklist,'settings':settings,'setIcl':setIcl,_T:setIclSuspended,'software':software,'swIcl':swIcl,_U:swIclStatus,'conformance':conformance,'groups':groups,'groupConfiguration':groupConfiguration,_V:groupCfgIcl,'groupRpc':groupRpc,_W:groupRpcIcl,'groupSettings':groupSettings,_X:groupSetIcl,'groupSoftware':groupSoftware,_Y:groupSwIcl,'compliances':compliances,'compliance':compliance})