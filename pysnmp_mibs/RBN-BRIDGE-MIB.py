_a='rbnBridgeBaseObjectGroup'
_Z='rbnBridgeStateNotifyGroup'
_Y='rbnBridgeStateNotifyObjectGroup'
_X='rbnBridgeTopologyChangeEvent'
_W='rbnBridgeNewRootEvent'
_V='rbnBridgeCctStateEvent'
_U='rbnBridgePortCctDescr'
_T='rbnBridgeNotifyEnable'
_S='rbnBridgePortCctDescrEntry'
_R='read-only'
_Q='rbnBridgeName'
_P='TruthValue'
_O='rbnBridgeNotifyGroup'
_N='rbnBridgeNotifyObjectGroup'
_M='rbnBridgePortPreviousState'
_L='rbnBridgeGroupContextName'
_K='rbnBridgeCircuitStatus'
_J='rbnBridgeCircuitDescriptor'
_I='rbnBridgeGroupName'
_H='dot1dStpPortState'
_G='BRIDGE-MIB'
_F='rbnBridgeId'
_E='Integer32'
_D='accessible-for-notify'
_C='SnmpAdminString'
_B='current'
_A='RBN-BRIDGE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePortEntry,dot1dStpPortState=mibBuilder.importSymbols(_G,'dot1dBasePortEntry',_H)
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_C)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_P)
rbnBridgeMib=ModuleIdentity((1,3,6,1,4,1,2352,2,42))
if mibBuilder.loadTexts:rbnBridgeMib.setRevisions(('2008-08-27 00:00','2008-02-25 00:00','2007-06-20 00:00'))
_RbnBridgeNotifications_ObjectIdentity=ObjectIdentity
rbnBridgeNotifications=_RbnBridgeNotifications_ObjectIdentity((1,3,6,1,4,1,2352,2,42,0))
_RbnBridgeObjects_ObjectIdentity=ObjectIdentity
rbnBridgeObjects=_RbnBridgeObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,42,1))
_RbnBridgeNotify_ObjectIdentity=ObjectIdentity
rbnBridgeNotify=_RbnBridgeNotify_ObjectIdentity((1,3,6,1,4,1,2352,2,42,1,1))
class _RbnBridgeNotifyEnable_Type(TruthValue):defaultValue=1
_RbnBridgeNotifyEnable_Type.__name__=_P
_RbnBridgeNotifyEnable_Object=MibScalar
rbnBridgeNotifyEnable=_RbnBridgeNotifyEnable_Object((1,3,6,1,4,1,2352,2,42,1,1,1),_RbnBridgeNotifyEnable_Type())
rbnBridgeNotifyEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:rbnBridgeNotifyEnable.setStatus(_B)
class _RbnBridgeGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RbnBridgeGroupName_Type.__name__=_C
_RbnBridgeGroupName_Object=MibScalar
rbnBridgeGroupName=_RbnBridgeGroupName_Object((1,3,6,1,4,1,2352,2,42,1,1,2),_RbnBridgeGroupName_Type())
rbnBridgeGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnBridgeGroupName.setStatus(_B)
class _RbnBridgeCircuitDescriptor_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_RbnBridgeCircuitDescriptor_Type.__name__=_C
_RbnBridgeCircuitDescriptor_Object=MibScalar
rbnBridgeCircuitDescriptor=_RbnBridgeCircuitDescriptor_Object((1,3,6,1,4,1,2352,2,42,1,1,3),_RbnBridgeCircuitDescriptor_Type())
rbnBridgeCircuitDescriptor.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnBridgeCircuitDescriptor.setStatus(_B)
class _RbnBridgeCircuitStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('blocked',1),('cleared',2)))
_RbnBridgeCircuitStatus_Type.__name__=_E
_RbnBridgeCircuitStatus_Object=MibScalar
rbnBridgeCircuitStatus=_RbnBridgeCircuitStatus_Object((1,3,6,1,4,1,2352,2,42,1,1,4),_RbnBridgeCircuitStatus_Type())
rbnBridgeCircuitStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnBridgeCircuitStatus.setStatus(_B)
class _RbnBridgeGroupContextName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RbnBridgeGroupContextName_Type.__name__=_C
_RbnBridgeGroupContextName_Object=MibScalar
rbnBridgeGroupContextName=_RbnBridgeGroupContextName_Object((1,3,6,1,4,1,2352,2,42,1,1,5),_RbnBridgeGroupContextName_Type())
rbnBridgeGroupContextName.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnBridgeGroupContextName.setStatus(_B)
class _RbnBridgePortPreviousState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('disabled',1),('blocking',2),('listening',3),('learning',4),('forwarding',5),('broken',6)))
_RbnBridgePortPreviousState_Type.__name__=_E
_RbnBridgePortPreviousState_Object=MibScalar
rbnBridgePortPreviousState=_RbnBridgePortPreviousState_Object((1,3,6,1,4,1,2352,2,42,1,1,6),_RbnBridgePortPreviousState_Type())
rbnBridgePortPreviousState.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnBridgePortPreviousState.setStatus(_B)
_RbnBridgeBase_ObjectIdentity=ObjectIdentity
rbnBridgeBase=_RbnBridgeBase_ObjectIdentity((1,3,6,1,4,1,2352,2,42,1,2))
_RbnBridgeIdTable_Object=MibTable
rbnBridgeIdTable=_RbnBridgeIdTable_Object((1,3,6,1,4,1,2352,2,42,1,2,1))
if mibBuilder.loadTexts:rbnBridgeIdTable.setStatus(_B)
_RbnBridgeIdEntry_Object=MibTableRow
rbnBridgeIdEntry=_RbnBridgeIdEntry_Object((1,3,6,1,4,1,2352,2,42,1,2,1,1))
rbnBridgeIdEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:rbnBridgeIdEntry.setStatus(_B)
class _RbnBridgeName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RbnBridgeName_Type.__name__=_C
_RbnBridgeName_Object=MibTableColumn
rbnBridgeName=_RbnBridgeName_Object((1,3,6,1,4,1,2352,2,42,1,2,1,1,1),_RbnBridgeName_Type())
rbnBridgeName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rbnBridgeName.setStatus(_B)
class _RbnBridgeId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RbnBridgeId_Type.__name__=_E
_RbnBridgeId_Object=MibTableColumn
rbnBridgeId=_RbnBridgeId_Object((1,3,6,1,4,1,2352,2,42,1,2,1,1,2),_RbnBridgeId_Type())
rbnBridgeId.setMaxAccess(_R)
if mibBuilder.loadTexts:rbnBridgeId.setStatus(_B)
_RbnBridgePortCctDescrTable_Object=MibTable
rbnBridgePortCctDescrTable=_RbnBridgePortCctDescrTable_Object((1,3,6,1,4,1,2352,2,42,1,2,2))
if mibBuilder.loadTexts:rbnBridgePortCctDescrTable.setStatus(_B)
_RbnBridgePortCctDescrEntry_Object=MibTableRow
rbnBridgePortCctDescrEntry=_RbnBridgePortCctDescrEntry_Object((1,3,6,1,4,1,2352,2,42,1,2,2,1))
if mibBuilder.loadTexts:rbnBridgePortCctDescrEntry.setStatus(_B)
class _RbnBridgePortCctDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_RbnBridgePortCctDescr_Type.__name__=_C
_RbnBridgePortCctDescr_Object=MibTableColumn
rbnBridgePortCctDescr=_RbnBridgePortCctDescr_Object((1,3,6,1,4,1,2352,2,42,1,2,2,1,1),_RbnBridgePortCctDescr_Type())
rbnBridgePortCctDescr.setMaxAccess(_R)
if mibBuilder.loadTexts:rbnBridgePortCctDescr.setStatus(_B)
_RbnBridgeConformance_ObjectIdentity=ObjectIdentity
rbnBridgeConformance=_RbnBridgeConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,42,2))
_RbnBridgeCompliances_ObjectIdentity=ObjectIdentity
rbnBridgeCompliances=_RbnBridgeCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,42,2,1))
_RbnBridgeGroups_ObjectIdentity=ObjectIdentity
rbnBridgeGroups=_RbnBridgeGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,42,2,2))
dot1dBasePortEntry.registerAugmentions((_A,_S))
rbnBridgePortCctDescrEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
rbnBridgeNotifyObjectGroup=ObjectGroup((1,3,6,1,4,1,2352,2,42,2,2,1))
rbnBridgeNotifyObjectGroup.setObjects(*((_A,_T),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:rbnBridgeNotifyObjectGroup.setStatus(_B)
rbnBridgeStateNotifyObjectGroup=ObjectGroup((1,3,6,1,4,1,2352,2,42,2,2,2))
rbnBridgeStateNotifyObjectGroup.setObjects((_A,_M))
if mibBuilder.loadTexts:rbnBridgeStateNotifyObjectGroup.setStatus(_B)
rbnBridgeBaseObjectGroup=ObjectGroup((1,3,6,1,4,1,2352,2,42,2,2,5))
rbnBridgeBaseObjectGroup.setObjects(*((_A,_F),(_A,_U)))
if mibBuilder.loadTexts:rbnBridgeBaseObjectGroup.setStatus(_B)
rbnBridgeCctStateEvent=NotificationType((1,3,6,1,4,1,2352,2,42,0,1))
rbnBridgeCctStateEvent.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:rbnBridgeCctStateEvent.setStatus(_B)
rbnBridgeNewRootEvent=NotificationType((1,3,6,1,4,1,2352,2,42,0,2))
rbnBridgeNewRootEvent.setObjects(*((_A,_F),(_G,_H)))
if mibBuilder.loadTexts:rbnBridgeNewRootEvent.setStatus(_B)
rbnBridgeTopologyChangeEvent=NotificationType((1,3,6,1,4,1,2352,2,42,0,3))
rbnBridgeTopologyChangeEvent.setObjects(*((_A,_F),(_G,_H),(_A,_M)))
if mibBuilder.loadTexts:rbnBridgeTopologyChangeEvent.setStatus(_B)
rbnBridgeNotifyGroup=NotificationGroup((1,3,6,1,4,1,2352,2,42,2,2,3))
rbnBridgeNotifyGroup.setObjects((_A,_V))
if mibBuilder.loadTexts:rbnBridgeNotifyGroup.setStatus(_B)
rbnBridgeStateNotifyGroup=NotificationGroup((1,3,6,1,4,1,2352,2,42,2,2,4))
rbnBridgeStateNotifyGroup.setObjects(*((_A,_W),(_A,_X)))
if mibBuilder.loadTexts:rbnBridgeStateNotifyGroup.setStatus(_B)
rbnBridgeCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,42,2,1,1))
rbnBridgeCompliance.setObjects(*((_A,_N),(_A,_O)))
if mibBuilder.loadTexts:rbnBridgeCompliance.setStatus('deprecated')
rbnBridgeCompliance2=ModuleCompliance((1,3,6,1,4,1,2352,2,42,2,1,2))
rbnBridgeCompliance2.setObjects(*((_A,_N),(_A,_Y),(_A,_O),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:rbnBridgeCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'rbnBridgeMib':rbnBridgeMib,'rbnBridgeNotifications':rbnBridgeNotifications,_V:rbnBridgeCctStateEvent,_W:rbnBridgeNewRootEvent,_X:rbnBridgeTopologyChangeEvent,'rbnBridgeObjects':rbnBridgeObjects,'rbnBridgeNotify':rbnBridgeNotify,_T:rbnBridgeNotifyEnable,_I:rbnBridgeGroupName,_J:rbnBridgeCircuitDescriptor,_K:rbnBridgeCircuitStatus,_L:rbnBridgeGroupContextName,_M:rbnBridgePortPreviousState,'rbnBridgeBase':rbnBridgeBase,'rbnBridgeIdTable':rbnBridgeIdTable,'rbnBridgeIdEntry':rbnBridgeIdEntry,_Q:rbnBridgeName,_F:rbnBridgeId,'rbnBridgePortCctDescrTable':rbnBridgePortCctDescrTable,_S:rbnBridgePortCctDescrEntry,_U:rbnBridgePortCctDescr,'rbnBridgeConformance':rbnBridgeConformance,'rbnBridgeCompliances':rbnBridgeCompliances,'rbnBridgeCompliance':rbnBridgeCompliance,'rbnBridgeCompliance2':rbnBridgeCompliance2,'rbnBridgeGroups':rbnBridgeGroups,_N:rbnBridgeNotifyObjectGroup,_Y:rbnBridgeStateNotifyObjectGroup,_O:rbnBridgeNotifyGroup,_Z:rbnBridgeStateNotifyGroup,_a:rbnBridgeBaseObjectGroup})