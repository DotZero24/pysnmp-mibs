_u='fcRouteFlowRowStatus'
_t='fcRouteFlowCreationTime'
_s='fcRouteFlowBytes'
_r='fcRouteFlowFrames'
_q='fcRouteFlowPort'
_p='fcRouteFlowMask'
_o='fcRouteFlowSrcId'
_n='fcRouteFlowDestId'
_m='fcRouteFlowVsanId'
_l='fcRouteFlowType'
_k='fcRouteRowStatus'
_j='fcRoutePermanent'
_i='fcRouteType'
_h='fcRouteMetric'
_g='fcRouteDomainId'
_f='fcRouteVerifyLock'
_e='fcRouteVerifyResult'
_d='fcRouteVerifyRouteType'
_c='fcRouteVerifyVsanID'
_b='fcRouteVerifyModule'
_a='fcRouteVerifyType'
_Z='fcRouteVerifyAction'
_Y='fcRoutePreference'
_X='fcRouteLastChangeTime'
_W='fcRouteFlowIndex'
_V='fcRouteInterface'
_U='fcRouteProto'
_T='fcRouteDestMask'
_S='fcRouteDestAddrId'
_R='multicast'
_Q='TruthValue'
_P='entPhysicalIndex'
_O='ENTITY-MIB'
_N='vsanIndex'
_M='CISCO-VSAN-MIB'
_L='fcRouteStatGroup'
_K='fcRouteTableGroup'
_J='fcRouteGroup'
_I='VsanIndex'
_H='not-accessible'
_G='read-only'
_F='Unsigned32'
_E='Integer32'
_D='read-write'
_C='read-create'
_B='CISCO-FC-ROUTE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
FcAddressId,VsanIndex=mibBuilder.importSymbols('CISCO-ST-TC','FcAddressId',_I)
vsanIndex,=mibBuilder.importSymbols(_M,_N)
PhysicalIndex,entPhysicalIndex=mibBuilder.importSymbols(_O,'PhysicalIndex',_P)
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TestAndIncr','TimeStamp',_Q)
ciscoFcRouteMIB=ModuleIdentity((1,3,6,1,4,1,9,9,284))
if mibBuilder.loadTexts:ciscoFcRouteMIB.setRevisions(('2003-09-04 00:00','2002-11-01 00:00','2002-10-02 00:00'))
_CiscoFcRouteMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFcRouteMIBObjects=_CiscoFcRouteMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,284,1))
_FcRouteConfig_ObjectIdentity=ObjectIdentity
fcRouteConfig=_FcRouteConfig_ObjectIdentity((1,3,6,1,4,1,9,9,284,1,1))
_FcRouteLastChangeTime_Type=TimeStamp
_FcRouteLastChangeTime_Object=MibScalar
fcRouteLastChangeTime=_FcRouteLastChangeTime_Object((1,3,6,1,4,1,9,9,284,1,1,1),_FcRouteLastChangeTime_Type())
fcRouteLastChangeTime.setMaxAccess(_G)
if mibBuilder.loadTexts:fcRouteLastChangeTime.setStatus(_A)
class _FcRoutePreference_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FcRoutePreference_Type.__name__=_F
_FcRoutePreference_Object=MibScalar
fcRoutePreference=_FcRoutePreference_Object((1,3,6,1,4,1,9,9,284,1,1,2),_FcRoutePreference_Type())
fcRoutePreference.setMaxAccess(_D)
if mibBuilder.loadTexts:fcRoutePreference.setStatus(_A)
class _FcRouteVerifyAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('verify',2)))
_FcRouteVerifyAction_Type.__name__=_E
_FcRouteVerifyAction_Object=MibScalar
fcRouteVerifyAction=_FcRouteVerifyAction_Object((1,3,6,1,4,1,9,9,284,1,1,3),_FcRouteVerifyAction_Type())
fcRouteVerifyAction.setMaxAccess(_D)
if mibBuilder.loadTexts:fcRouteVerifyAction.setStatus(_A)
class _FcRouteVerifyType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('pss',1),('fibShadow',2),('fibHardware',3)))
_FcRouteVerifyType_Type.__name__=_E
_FcRouteVerifyType_Object=MibScalar
fcRouteVerifyType=_FcRouteVerifyType_Object((1,3,6,1,4,1,9,9,284,1,1,4),_FcRouteVerifyType_Type())
fcRouteVerifyType.setMaxAccess(_D)
if mibBuilder.loadTexts:fcRouteVerifyType.setStatus(_A)
_FcRouteVerifyModule_Type=PhysicalIndex
_FcRouteVerifyModule_Object=MibScalar
fcRouteVerifyModule=_FcRouteVerifyModule_Object((1,3,6,1,4,1,9,9,284,1,1,5),_FcRouteVerifyModule_Type())
fcRouteVerifyModule.setMaxAccess(_D)
if mibBuilder.loadTexts:fcRouteVerifyModule.setStatus(_A)
class _FcRouteVerifyVsanID_Type(VsanIndex):subtypeSpec=VsanIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4093))
_FcRouteVerifyVsanID_Type.__name__=_I
_FcRouteVerifyVsanID_Object=MibScalar
fcRouteVerifyVsanID=_FcRouteVerifyVsanID_Object((1,3,6,1,4,1,9,9,284,1,1,6),_FcRouteVerifyVsanID_Type())
fcRouteVerifyVsanID.setMaxAccess(_D)
if mibBuilder.loadTexts:fcRouteVerifyVsanID.setStatus(_A)
class _FcRouteVerifyRouteType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unicast',1),(_R,2),('label',3)))
_FcRouteVerifyRouteType_Type.__name__=_E
_FcRouteVerifyRouteType_Object=MibScalar
fcRouteVerifyRouteType=_FcRouteVerifyRouteType_Object((1,3,6,1,4,1,9,9,284,1,1,7),_FcRouteVerifyRouteType_Type())
fcRouteVerifyRouteType.setMaxAccess(_D)
if mibBuilder.loadTexts:fcRouteVerifyRouteType.setStatus(_A)
_FcRouteVerifyResult_Type=SnmpAdminString
_FcRouteVerifyResult_Object=MibScalar
fcRouteVerifyResult=_FcRouteVerifyResult_Object((1,3,6,1,4,1,9,9,284,1,1,8),_FcRouteVerifyResult_Type())
fcRouteVerifyResult.setMaxAccess(_G)
if mibBuilder.loadTexts:fcRouteVerifyResult.setStatus(_A)
_FcRouteVerifyLock_Type=TestAndIncr
_FcRouteVerifyLock_Object=MibScalar
fcRouteVerifyLock=_FcRouteVerifyLock_Object((1,3,6,1,4,1,9,9,284,1,1,9),_FcRouteVerifyLock_Type())
fcRouteVerifyLock.setMaxAccess(_D)
if mibBuilder.loadTexts:fcRouteVerifyLock.setStatus(_A)
_FcRouteTable_Object=MibTable
fcRouteTable=_FcRouteTable_Object((1,3,6,1,4,1,9,9,284,1,1,10))
if mibBuilder.loadTexts:fcRouteTable.setStatus(_A)
_FcRouteEntry_Object=MibTableRow
fcRouteEntry=_FcRouteEntry_Object((1,3,6,1,4,1,9,9,284,1,1,10,1))
fcRouteEntry.setIndexNames((0,_M,_N),(0,_B,_S),(0,_B,_T),(0,_B,_U),(0,_B,_V))
if mibBuilder.loadTexts:fcRouteEntry.setStatus(_A)
_FcRouteDestAddrId_Type=FcAddressId
_FcRouteDestAddrId_Object=MibTableColumn
fcRouteDestAddrId=_FcRouteDestAddrId_Object((1,3,6,1,4,1,9,9,284,1,1,10,1,1),_FcRouteDestAddrId_Type())
fcRouteDestAddrId.setMaxAccess(_H)
if mibBuilder.loadTexts:fcRouteDestAddrId.setStatus(_A)
_FcRouteDestMask_Type=FcAddressId
_FcRouteDestMask_Object=MibTableColumn
fcRouteDestMask=_FcRouteDestMask_Object((1,3,6,1,4,1,9,9,284,1,1,10,1,2),_FcRouteDestMask_Type())
fcRouteDestMask.setMaxAccess(_H)
if mibBuilder.loadTexts:fcRouteDestMask.setStatus(_A)
class _FcRouteProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('local',2),('netmgmt',3),('fspf',4),('mpls',5),(_R,6)))
_FcRouteProto_Type.__name__=_E
_FcRouteProto_Object=MibTableColumn
fcRouteProto=_FcRouteProto_Object((1,3,6,1,4,1,9,9,284,1,1,10,1,3),_FcRouteProto_Type())
fcRouteProto.setMaxAccess(_H)
if mibBuilder.loadTexts:fcRouteProto.setStatus(_A)
_FcRouteInterface_Type=InterfaceIndex
_FcRouteInterface_Object=MibTableColumn
fcRouteInterface=_FcRouteInterface_Object((1,3,6,1,4,1,9,9,284,1,1,10,1,4),_FcRouteInterface_Type())
fcRouteInterface.setMaxAccess(_H)
if mibBuilder.loadTexts:fcRouteInterface.setStatus(_A)
class _FcRouteDomainId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,239))
_FcRouteDomainId_Type.__name__=_F
_FcRouteDomainId_Object=MibTableColumn
fcRouteDomainId=_FcRouteDomainId_Object((1,3,6,1,4,1,9,9,284,1,1,10,1,5),_FcRouteDomainId_Type())
fcRouteDomainId.setMaxAccess(_C)
if mibBuilder.loadTexts:fcRouteDomainId.setStatus(_A)
class _FcRouteMetric_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_FcRouteMetric_Type.__name__=_F
_FcRouteMetric_Object=MibTableColumn
fcRouteMetric=_FcRouteMetric_Object((1,3,6,1,4,1,9,9,284,1,1,10,1,6),_FcRouteMetric_Type())
fcRouteMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:fcRouteMetric.setStatus(_A)
class _FcRouteType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
_FcRouteType_Type.__name__=_E
_FcRouteType_Object=MibTableColumn
fcRouteType=_FcRouteType_Object((1,3,6,1,4,1,9,9,284,1,1,10,1,7),_FcRouteType_Type())
fcRouteType.setMaxAccess(_C)
if mibBuilder.loadTexts:fcRouteType.setStatus(_A)
class _FcRoutePermanent_Type(TruthValue):defaultValue=1
_FcRoutePermanent_Type.__name__=_Q
_FcRoutePermanent_Object=MibTableColumn
fcRoutePermanent=_FcRoutePermanent_Object((1,3,6,1,4,1,9,9,284,1,1,10,1,8),_FcRoutePermanent_Type())
fcRoutePermanent.setMaxAccess(_C)
if mibBuilder.loadTexts:fcRoutePermanent.setStatus(_A)
_FcRouteRowStatus_Type=RowStatus
_FcRouteRowStatus_Object=MibTableColumn
fcRouteRowStatus=_FcRouteRowStatus_Object((1,3,6,1,4,1,9,9,284,1,1,10,1,9),_FcRouteRowStatus_Type())
fcRouteRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fcRouteRowStatus.setStatus(_A)
_FcRouteStatistics_ObjectIdentity=ObjectIdentity
fcRouteStatistics=_FcRouteStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,284,1,2))
_FcRouteFlowStatTable_Object=MibTable
fcRouteFlowStatTable=_FcRouteFlowStatTable_Object((1,3,6,1,4,1,9,9,284,1,2,1))
if mibBuilder.loadTexts:fcRouteFlowStatTable.setStatus(_A)
_FcRouteFlowStatEntry_Object=MibTableRow
fcRouteFlowStatEntry=_FcRouteFlowStatEntry_Object((1,3,6,1,4,1,9,9,284,1,2,1,1))
fcRouteFlowStatEntry.setIndexNames((0,_O,_P),(0,_B,_W))
if mibBuilder.loadTexts:fcRouteFlowStatEntry.setStatus(_A)
class _FcRouteFlowIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FcRouteFlowIndex_Type.__name__=_F
_FcRouteFlowIndex_Object=MibTableColumn
fcRouteFlowIndex=_FcRouteFlowIndex_Object((1,3,6,1,4,1,9,9,284,1,2,1,1,1),_FcRouteFlowIndex_Type())
fcRouteFlowIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:fcRouteFlowIndex.setStatus(_A)
class _FcRouteFlowType_Type(Bits):namedValues=NamedValues(*(('vsanId',0),('destId',1),('srcId',2),('port',3)))
_FcRouteFlowType_Type.__name__='Bits'
_FcRouteFlowType_Object=MibTableColumn
fcRouteFlowType=_FcRouteFlowType_Object((1,3,6,1,4,1,9,9,284,1,2,1,1,2),_FcRouteFlowType_Type())
fcRouteFlowType.setMaxAccess(_C)
if mibBuilder.loadTexts:fcRouteFlowType.setStatus(_A)
class _FcRouteFlowVsanId_Type(VsanIndex):subtypeSpec=VsanIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4093))
_FcRouteFlowVsanId_Type.__name__=_I
_FcRouteFlowVsanId_Object=MibTableColumn
fcRouteFlowVsanId=_FcRouteFlowVsanId_Object((1,3,6,1,4,1,9,9,284,1,2,1,1,3),_FcRouteFlowVsanId_Type())
fcRouteFlowVsanId.setMaxAccess(_C)
if mibBuilder.loadTexts:fcRouteFlowVsanId.setStatus(_A)
_FcRouteFlowDestId_Type=FcAddressId
_FcRouteFlowDestId_Object=MibTableColumn
fcRouteFlowDestId=_FcRouteFlowDestId_Object((1,3,6,1,4,1,9,9,284,1,2,1,1,4),_FcRouteFlowDestId_Type())
fcRouteFlowDestId.setMaxAccess(_C)
if mibBuilder.loadTexts:fcRouteFlowDestId.setStatus(_A)
_FcRouteFlowSrcId_Type=FcAddressId
_FcRouteFlowSrcId_Object=MibTableColumn
fcRouteFlowSrcId=_FcRouteFlowSrcId_Object((1,3,6,1,4,1,9,9,284,1,2,1,1,5),_FcRouteFlowSrcId_Type())
fcRouteFlowSrcId.setMaxAccess(_C)
if mibBuilder.loadTexts:fcRouteFlowSrcId.setStatus(_A)
_FcRouteFlowMask_Type=FcAddressId
_FcRouteFlowMask_Object=MibTableColumn
fcRouteFlowMask=_FcRouteFlowMask_Object((1,3,6,1,4,1,9,9,284,1,2,1,1,6),_FcRouteFlowMask_Type())
fcRouteFlowMask.setMaxAccess(_C)
if mibBuilder.loadTexts:fcRouteFlowMask.setStatus(_A)
_FcRouteFlowPort_Type=InterfaceIndex
_FcRouteFlowPort_Object=MibTableColumn
fcRouteFlowPort=_FcRouteFlowPort_Object((1,3,6,1,4,1,9,9,284,1,2,1,1,7),_FcRouteFlowPort_Type())
fcRouteFlowPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fcRouteFlowPort.setStatus(_A)
_FcRouteFlowFrames_Type=Counter64
_FcRouteFlowFrames_Object=MibTableColumn
fcRouteFlowFrames=_FcRouteFlowFrames_Object((1,3,6,1,4,1,9,9,284,1,2,1,1,8),_FcRouteFlowFrames_Type())
fcRouteFlowFrames.setMaxAccess(_G)
if mibBuilder.loadTexts:fcRouteFlowFrames.setStatus(_A)
_FcRouteFlowBytes_Type=Counter64
_FcRouteFlowBytes_Object=MibTableColumn
fcRouteFlowBytes=_FcRouteFlowBytes_Object((1,3,6,1,4,1,9,9,284,1,2,1,1,9),_FcRouteFlowBytes_Type())
fcRouteFlowBytes.setMaxAccess(_G)
if mibBuilder.loadTexts:fcRouteFlowBytes.setStatus(_A)
_FcRouteFlowCreationTime_Type=TimeStamp
_FcRouteFlowCreationTime_Object=MibTableColumn
fcRouteFlowCreationTime=_FcRouteFlowCreationTime_Object((1,3,6,1,4,1,9,9,284,1,2,1,1,11),_FcRouteFlowCreationTime_Type())
fcRouteFlowCreationTime.setMaxAccess(_G)
if mibBuilder.loadTexts:fcRouteFlowCreationTime.setStatus(_A)
_FcRouteFlowRowStatus_Type=RowStatus
_FcRouteFlowRowStatus_Object=MibTableColumn
fcRouteFlowRowStatus=_FcRouteFlowRowStatus_Object((1,3,6,1,4,1,9,9,284,1,2,1,1,12),_FcRouteFlowRowStatus_Type())
fcRouteFlowRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fcRouteFlowRowStatus.setStatus(_A)
_FcRouteNotification_ObjectIdentity=ObjectIdentity
fcRouteNotification=_FcRouteNotification_ObjectIdentity((1,3,6,1,4,1,9,9,284,1,3))
_FcRouteNotifications_ObjectIdentity=ObjectIdentity
fcRouteNotifications=_FcRouteNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,284,1,3,0))
_FcRouteMIBConformance_ObjectIdentity=ObjectIdentity
fcRouteMIBConformance=_FcRouteMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,284,2))
_FcRouteMIBCompliances_ObjectIdentity=ObjectIdentity
fcRouteMIBCompliances=_FcRouteMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,284,2,1))
_FcRouteMIBGroups_ObjectIdentity=ObjectIdentity
fcRouteMIBGroups=_FcRouteMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,284,2,2))
fcRouteGroup=ObjectGroup((1,3,6,1,4,1,9,9,284,2,2,1))
fcRouteGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:fcRouteGroup.setStatus(_A)
fcRouteTableGroup=ObjectGroup((1,3,6,1,4,1,9,9,284,2,2,2))
fcRouteTableGroup.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:fcRouteTableGroup.setStatus(_A)
fcRouteStatGroup=ObjectGroup((1,3,6,1,4,1,9,9,284,2,2,3))
fcRouteStatGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:fcRouteStatGroup.setStatus(_A)
fcRouteMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,284,2,1,1))
fcRouteMIBCompliance.setObjects(*((_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:fcRouteMIBCompliance.setStatus('deprecated')
fcRouteMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,9,9,284,2,1,2))
fcRouteMIBCompliance1.setObjects(*((_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:fcRouteMIBCompliance1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoFcRouteMIB':ciscoFcRouteMIB,'ciscoFcRouteMIBObjects':ciscoFcRouteMIBObjects,'fcRouteConfig':fcRouteConfig,_X:fcRouteLastChangeTime,_Y:fcRoutePreference,_Z:fcRouteVerifyAction,_a:fcRouteVerifyType,_b:fcRouteVerifyModule,_c:fcRouteVerifyVsanID,_d:fcRouteVerifyRouteType,_e:fcRouteVerifyResult,_f:fcRouteVerifyLock,'fcRouteTable':fcRouteTable,'fcRouteEntry':fcRouteEntry,_S:fcRouteDestAddrId,_T:fcRouteDestMask,_U:fcRouteProto,_V:fcRouteInterface,_g:fcRouteDomainId,_h:fcRouteMetric,_i:fcRouteType,_j:fcRoutePermanent,_k:fcRouteRowStatus,'fcRouteStatistics':fcRouteStatistics,'fcRouteFlowStatTable':fcRouteFlowStatTable,'fcRouteFlowStatEntry':fcRouteFlowStatEntry,_W:fcRouteFlowIndex,_l:fcRouteFlowType,_m:fcRouteFlowVsanId,_n:fcRouteFlowDestId,_o:fcRouteFlowSrcId,_p:fcRouteFlowMask,_q:fcRouteFlowPort,_r:fcRouteFlowFrames,_s:fcRouteFlowBytes,_t:fcRouteFlowCreationTime,_u:fcRouteFlowRowStatus,'fcRouteNotification':fcRouteNotification,'fcRouteNotifications':fcRouteNotifications,'fcRouteMIBConformance':fcRouteMIBConformance,'fcRouteMIBCompliances':fcRouteMIBCompliances,'fcRouteMIBCompliance':fcRouteMIBCompliance,'fcRouteMIBCompliance1':fcRouteMIBCompliance1,'fcRouteMIBGroups':fcRouteMIBGroups,_J:fcRouteGroup,_K:fcRouteTableGroup,_L:fcRouteStatGroup})