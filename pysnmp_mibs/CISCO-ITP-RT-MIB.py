_j='cItpRtScalarGroupRev1'
_i='cItpRtNotificationsGroup'
_h='cItpRouteStateChange'
_g='cItpRtChangeNotifMaxPerWindow'
_f='cItpRtChangeNotifWindowTime'
_e='cItpRtMaxDynamicRoutes'
_d='cItpRtChangeNotifDelayTime'
_c='cItpRtStateChangeNotifEnabled'
_b='cItpRtConfigLoadStatus'
_a='cItpRtConfigLoad'
_Z='cItpRouteNonAdjStatus'
_Y='cItpRouteStatus'
_X='cItpRouteQos'
_W='cItpRtConfigLastChanged'
_V='restricted'
_U='unknown'
_T='cItpRouteDestLinkset'
_S='cItpRouteDestLsCost'
_R='cItpRouteMask'
_Q='cItpRouteDpc'
_P='cItpRouteTableName'
_O='seconds'
_N='TruthValue'
_M='OctetString'
_L='cItpRouteGroup'
_K='cItpRtScalarGroup'
_J='cItpRtNotifInfoStateChanges'
_I='cItpRtNotifInfoSuppressedFlag'
_H='cItpRtStateChangeCount'
_G='Unsigned32'
_F='not-accessible'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='deprecated'
_A='CISCO-ITP-RT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CItpTcLinksetId,CItpTcPointCode,CItpTcQos,CItpTcRouteTableName,CItpTcTableLoadStatus=mibBuilder.importSymbols('CISCO-ITP-TC-MIB','CItpTcLinksetId','CItpTcPointCode','CItpTcQos','CItpTcRouteTableName','CItpTcTableLoadStatus')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_N)
ciscoItpRtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,228))
if mibBuilder.loadTexts:ciscoItpRtMIB.setRevisions(('2003-07-10 00:00','2002-01-07 00:00','2001-08-29 00:00'))
_CItpRouteNotifications_ObjectIdentity=ObjectIdentity
cItpRouteNotifications=_CItpRouteNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,228,0))
_CItpRtMIBObjects_ObjectIdentity=ObjectIdentity
cItpRtMIBObjects=_CItpRtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,228,1))
_CItpRtScalars_ObjectIdentity=ObjectIdentity
cItpRtScalars=_CItpRtScalars_ObjectIdentity((1,3,6,1,4,1,9,9,228,1,1))
_CItpRtConfigLastChanged_Type=TimeStamp
_CItpRtConfigLastChanged_Object=MibScalar
cItpRtConfigLastChanged=_CItpRtConfigLastChanged_Object((1,3,6,1,4,1,9,9,228,1,1,1),_CItpRtConfigLastChanged_Type())
cItpRtConfigLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpRtConfigLastChanged.setStatus(_B)
_CItpRtConfigLoad_Type=TimeStamp
_CItpRtConfigLoad_Object=MibScalar
cItpRtConfigLoad=_CItpRtConfigLoad_Object((1,3,6,1,4,1,9,9,228,1,1,2),_CItpRtConfigLoad_Type())
cItpRtConfigLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpRtConfigLoad.setStatus(_B)
_CItpRtConfigLoadStatus_Type=CItpTcTableLoadStatus
_CItpRtConfigLoadStatus_Object=MibScalar
cItpRtConfigLoadStatus=_CItpRtConfigLoadStatus_Object((1,3,6,1,4,1,9,9,228,1,1,3),_CItpRtConfigLoadStatus_Type())
cItpRtConfigLoadStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpRtConfigLoadStatus.setStatus(_B)
_CItpRtStateChangeCount_Type=Counter32
_CItpRtStateChangeCount_Object=MibScalar
cItpRtStateChangeCount=_CItpRtStateChangeCount_Object((1,3,6,1,4,1,9,9,228,1,1,4),_CItpRtStateChangeCount_Type())
cItpRtStateChangeCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpRtStateChangeCount.setStatus(_B)
class _CItpRtStateChangeNotifEnabled_Type(TruthValue):defaultValue=2
_CItpRtStateChangeNotifEnabled_Type.__name__=_N
_CItpRtStateChangeNotifEnabled_Object=MibScalar
cItpRtStateChangeNotifEnabled=_CItpRtStateChangeNotifEnabled_Object((1,3,6,1,4,1,9,9,228,1,1,5),_CItpRtStateChangeNotifEnabled_Type())
cItpRtStateChangeNotifEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:cItpRtStateChangeNotifEnabled.setStatus(_B)
class _CItpRtChangeNotifDelayTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_CItpRtChangeNotifDelayTime_Type.__name__=_G
_CItpRtChangeNotifDelayTime_Object=MibScalar
cItpRtChangeNotifDelayTime=_CItpRtChangeNotifDelayTime_Object((1,3,6,1,4,1,9,9,228,1,1,6),_CItpRtChangeNotifDelayTime_Type())
cItpRtChangeNotifDelayTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cItpRtChangeNotifDelayTime.setStatus(_B)
if mibBuilder.loadTexts:cItpRtChangeNotifDelayTime.setUnits(_O)
class _CItpRtMaxDynamicRoutes_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_CItpRtMaxDynamicRoutes_Type.__name__=_D
_CItpRtMaxDynamicRoutes_Object=MibScalar
cItpRtMaxDynamicRoutes=_CItpRtMaxDynamicRoutes_Object((1,3,6,1,4,1,9,9,228,1,1,7),_CItpRtMaxDynamicRoutes_Type())
cItpRtMaxDynamicRoutes.setMaxAccess(_E)
if mibBuilder.loadTexts:cItpRtMaxDynamicRoutes.setStatus(_B)
class _CItpRtChangeNotifWindowTime_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,900))
_CItpRtChangeNotifWindowTime_Type.__name__=_D
_CItpRtChangeNotifWindowTime_Object=MibScalar
cItpRtChangeNotifWindowTime=_CItpRtChangeNotifWindowTime_Object((1,3,6,1,4,1,9,9,228,1,1,8),_CItpRtChangeNotifWindowTime_Type())
cItpRtChangeNotifWindowTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cItpRtChangeNotifWindowTime.setStatus(_B)
if mibBuilder.loadTexts:cItpRtChangeNotifWindowTime.setUnits(_O)
class _CItpRtChangeNotifMaxPerWindow_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,9000))
_CItpRtChangeNotifMaxPerWindow_Type.__name__=_D
_CItpRtChangeNotifMaxPerWindow_Object=MibScalar
cItpRtChangeNotifMaxPerWindow=_CItpRtChangeNotifMaxPerWindow_Object((1,3,6,1,4,1,9,9,228,1,1,9),_CItpRtChangeNotifMaxPerWindow_Type())
cItpRtChangeNotifMaxPerWindow.setMaxAccess(_E)
if mibBuilder.loadTexts:cItpRtChangeNotifMaxPerWindow.setStatus(_B)
_CItpRtTables_ObjectIdentity=ObjectIdentity
cItpRtTables=_CItpRtTables_ObjectIdentity((1,3,6,1,4,1,9,9,228,1,2))
_CItpRouteTable_Object=MibTable
cItpRouteTable=_CItpRouteTable_Object((1,3,6,1,4,1,9,9,228,1,2,1))
if mibBuilder.loadTexts:cItpRouteTable.setStatus(_B)
_CItpRouteTableEntry_Object=MibTableRow
cItpRouteTableEntry=_CItpRouteTableEntry_Object((1,3,6,1,4,1,9,9,228,1,2,1,1))
cItpRouteTableEntry.setIndexNames((0,_A,_P),(0,_A,_Q),(0,_A,_R),(0,_A,_S),(0,_A,_T))
if mibBuilder.loadTexts:cItpRouteTableEntry.setStatus(_B)
_CItpRouteTableName_Type=CItpTcRouteTableName
_CItpRouteTableName_Object=MibTableColumn
cItpRouteTableName=_CItpRouteTableName_Object((1,3,6,1,4,1,9,9,228,1,2,1,1,1),_CItpRouteTableName_Type())
cItpRouteTableName.setMaxAccess(_F)
if mibBuilder.loadTexts:cItpRouteTableName.setStatus(_B)
_CItpRouteDpc_Type=CItpTcPointCode
_CItpRouteDpc_Object=MibTableColumn
cItpRouteDpc=_CItpRouteDpc_Object((1,3,6,1,4,1,9,9,228,1,2,1,1,2),_CItpRouteDpc_Type())
cItpRouteDpc.setMaxAccess(_F)
if mibBuilder.loadTexts:cItpRouteDpc.setStatus(_B)
class _CItpRouteDestLsCost_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_CItpRouteDestLsCost_Type.__name__=_G
_CItpRouteDestLsCost_Object=MibTableColumn
cItpRouteDestLsCost=_CItpRouteDestLsCost_Object((1,3,6,1,4,1,9,9,228,1,2,1,1,3),_CItpRouteDestLsCost_Type())
cItpRouteDestLsCost.setMaxAccess(_F)
if mibBuilder.loadTexts:cItpRouteDestLsCost.setStatus(_B)
_CItpRouteDestLinkset_Type=CItpTcLinksetId
_CItpRouteDestLinkset_Object=MibTableColumn
cItpRouteDestLinkset=_CItpRouteDestLinkset_Object((1,3,6,1,4,1,9,9,228,1,2,1,1,4),_CItpRouteDestLinkset_Type())
cItpRouteDestLinkset.setMaxAccess(_F)
if mibBuilder.loadTexts:cItpRouteDestLinkset.setStatus(_B)
class _CItpRouteMask_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CItpRouteMask_Type.__name__=_G
_CItpRouteMask_Object=MibTableColumn
cItpRouteMask=_CItpRouteMask_Object((1,3,6,1,4,1,9,9,228,1,2,1,1,5),_CItpRouteMask_Type())
cItpRouteMask.setMaxAccess(_F)
if mibBuilder.loadTexts:cItpRouteMask.setStatus(_B)
_CItpRouteQos_Type=CItpTcQos
_CItpRouteQos_Object=MibTableColumn
cItpRouteQos=_CItpRouteQos_Object((1,3,6,1,4,1,9,9,228,1,2,1,1,6),_CItpRouteQos_Type())
cItpRouteQos.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpRouteQos.setStatus(_B)
class _CItpRouteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),('available',2),(_V,3),('unavailable',4)))
_CItpRouteStatus_Type.__name__=_D
_CItpRouteStatus_Object=MibTableColumn
cItpRouteStatus=_CItpRouteStatus_Object((1,3,6,1,4,1,9,9,228,1,2,1,1,7),_CItpRouteStatus_Type())
cItpRouteStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpRouteStatus.setStatus(_B)
class _CItpRouteNonAdjStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),('allowed',2),(_V,3),('prohibited',4)))
_CItpRouteNonAdjStatus_Type.__name__=_D
_CItpRouteNonAdjStatus_Object=MibTableColumn
cItpRouteNonAdjStatus=_CItpRouteNonAdjStatus_Object((1,3,6,1,4,1,9,9,228,1,2,1,1,8),_CItpRouteNonAdjStatus_Type())
cItpRouteNonAdjStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpRouteNonAdjStatus.setStatus(_B)
_CItpRtNotificationsInfo_ObjectIdentity=ObjectIdentity
cItpRtNotificationsInfo=_CItpRtNotificationsInfo_ObjectIdentity((1,3,6,1,4,1,9,9,228,1,3))
_CItpRtNotifInfoSuppressedFlag_Type=TruthValue
_CItpRtNotifInfoSuppressedFlag_Object=MibScalar
cItpRtNotifInfoSuppressedFlag=_CItpRtNotifInfoSuppressedFlag_Object((1,3,6,1,4,1,9,9,228,1,3,1),_CItpRtNotifInfoSuppressedFlag_Type())
cItpRtNotifInfoSuppressedFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpRtNotifInfoSuppressedFlag.setStatus(_B)
class _CItpRtNotifInfoStateChanges_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,480))
_CItpRtNotifInfoStateChanges_Type.__name__=_M
_CItpRtNotifInfoStateChanges_Object=MibScalar
cItpRtNotifInfoStateChanges=_CItpRtNotifInfoStateChanges_Object((1,3,6,1,4,1,9,9,228,1,3,2),_CItpRtNotifInfoStateChanges_Type())
cItpRtNotifInfoStateChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpRtNotifInfoStateChanges.setStatus(_B)
_CItpRtMIBConformance_ObjectIdentity=ObjectIdentity
cItpRtMIBConformance=_CItpRtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,228,2))
_CItpRtMIBCompliances_ObjectIdentity=ObjectIdentity
cItpRtMIBCompliances=_CItpRtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,228,2,1))
_CItpRtMIBGroups_ObjectIdentity=ObjectIdentity
cItpRtMIBGroups=_CItpRtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,228,2,2))
cItpRtScalarGroup=ObjectGroup((1,3,6,1,4,1,9,9,228,2,2,1))
cItpRtScalarGroup.setObjects((_A,_W))
if mibBuilder.loadTexts:cItpRtScalarGroup.setStatus(_B)
cItpRouteGroup=ObjectGroup((1,3,6,1,4,1,9,9,228,2,2,2))
cItpRouteGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:cItpRouteGroup.setStatus(_B)
cItpRtScalarGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,228,2,2,4))
cItpRtScalarGroupRev1.setObjects(*((_A,_a),(_A,_b),(_A,_H),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:cItpRtScalarGroupRev1.setStatus(_B)
cItpRouteStateChange=NotificationType((1,3,6,1,4,1,9,9,228,0,1))
cItpRouteStateChange.setObjects(*((_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:cItpRouteStateChange.setStatus(_B)
cItpRtNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,228,2,2,3))
cItpRtNotificationsGroup.setObjects((_A,_h))
if mibBuilder.loadTexts:cItpRtNotificationsGroup.setStatus(_B)
cItpRtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,228,2,1,1))
cItpRtMIBCompliance.setObjects(*((_A,_K),(_A,_L)))
if mibBuilder.loadTexts:cItpRtMIBCompliance.setStatus(_B)
cItpRtMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,228,2,1,2))
cItpRtMIBComplianceRev1.setObjects(*((_A,_K),(_A,_L),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:cItpRtMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoItpRtMIB':ciscoItpRtMIB,'cItpRouteNotifications':cItpRouteNotifications,_h:cItpRouteStateChange,'cItpRtMIBObjects':cItpRtMIBObjects,'cItpRtScalars':cItpRtScalars,_W:cItpRtConfigLastChanged,_a:cItpRtConfigLoad,_b:cItpRtConfigLoadStatus,_H:cItpRtStateChangeCount,_c:cItpRtStateChangeNotifEnabled,_d:cItpRtChangeNotifDelayTime,_e:cItpRtMaxDynamicRoutes,_f:cItpRtChangeNotifWindowTime,_g:cItpRtChangeNotifMaxPerWindow,'cItpRtTables':cItpRtTables,'cItpRouteTable':cItpRouteTable,'cItpRouteTableEntry':cItpRouteTableEntry,_P:cItpRouteTableName,_Q:cItpRouteDpc,_S:cItpRouteDestLsCost,_T:cItpRouteDestLinkset,_R:cItpRouteMask,_X:cItpRouteQos,_Y:cItpRouteStatus,_Z:cItpRouteNonAdjStatus,'cItpRtNotificationsInfo':cItpRtNotificationsInfo,_I:cItpRtNotifInfoSuppressedFlag,_J:cItpRtNotifInfoStateChanges,'cItpRtMIBConformance':cItpRtMIBConformance,'cItpRtMIBCompliances':cItpRtMIBCompliances,'cItpRtMIBCompliance':cItpRtMIBCompliance,'cItpRtMIBComplianceRev1':cItpRtMIBComplianceRev1,'cItpRtMIBGroups':cItpRtMIBGroups,_K:cItpRtScalarGroup,_L:cItpRouteGroup,_i:cItpRtNotificationsGroup,_j:cItpRtScalarGroupRev1})