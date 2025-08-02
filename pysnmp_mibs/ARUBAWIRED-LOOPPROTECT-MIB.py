_Y='arubaWiredLoopProtectVLANGroup'
_X='arubaWiredLoopProtectNotificationsGroup'
_W='arubaWiredLoopProtectBaseGroup'
_V='arubaWiredLoopProtectVlanLoopDetectedNotification'
_U='arubaWiredLoopProtectLoopDetectedNotification'
_T='arubaWiredLoopProtectPortVlanList'
_S='arubaWiredLoopProtectVIDList'
_R='arubaWiredLoopProtectMode'
_Q='arubaWiredLoopProtectPortLastLoopTime'
_P='arubaWiredLoopProtectPortLoopDetected'
_O='arubaWiredLoopProtectPortEnable'
_N='arubaWiredLoopProtectTrapLoopDetectEnable'
_M='arubaWiredLoopProtectEnableTimer'
_L='arubaWiredLoopProtectInterval'
_K='arubaWiredLoopProtectPortInterfaceIndex'
_J='arubaWiredLoopProtectLoopDetectedVlan'
_I='ifIndex'
_H='IF-MIB'
_G='arubaWiredLoopProtectPortReceiverAction'
_F='arubaWiredLoopProtectPortLoopCount'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='ARUBAWIRED-LOOPPROTECT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wndFeatures,=mibBuilder.importSymbols('ARUBAWIRED-NETWORKING-OID','wndFeatures')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_H,'InterfaceIndex',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
arubaWiredLoopProtectMIB=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,1))
if mibBuilder.loadTexts:arubaWiredLoopProtectMIB.setRevisions(('2017-11-02 00:00',))
class ConfigStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('notInService',2),('notReady',3)))
class VidList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
class LoopProtectReceiverAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disableTx',1),('noDisable',2),('disableTxRx',3)))
_ArubaWiredLoopProtectObjects_ObjectIdentity=ObjectIdentity
arubaWiredLoopProtectObjects=_ArubaWiredLoopProtectObjects_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,1,1))
_ArubaWiredLoopProtect_ObjectIdentity=ObjectIdentity
arubaWiredLoopProtect=_ArubaWiredLoopProtect_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,1,1,5))
_ArubaWiredLoopProtectNotifications_ObjectIdentity=ObjectIdentity
arubaWiredLoopProtectNotifications=_ArubaWiredLoopProtectNotifications_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,0))
_ArubaWiredLoopProtectBase_ObjectIdentity=ObjectIdentity
arubaWiredLoopProtectBase=_ArubaWiredLoopProtectBase_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,1))
class _ArubaWiredLoopProtectInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_ArubaWiredLoopProtectInterval_Type.__name__=_D
_ArubaWiredLoopProtectInterval_Object=MibScalar
arubaWiredLoopProtectInterval=_ArubaWiredLoopProtectInterval_Object((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,1,1),_ArubaWiredLoopProtectInterval_Type())
arubaWiredLoopProtectInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLoopProtectInterval.setStatus(_A)
_ArubaWiredLoopProtectTrapLoopDetectEnable_Type=TruthValue
_ArubaWiredLoopProtectTrapLoopDetectEnable_Object=MibScalar
arubaWiredLoopProtectTrapLoopDetectEnable=_ArubaWiredLoopProtectTrapLoopDetectEnable_Object((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,1,2),_ArubaWiredLoopProtectTrapLoopDetectEnable_Type())
arubaWiredLoopProtectTrapLoopDetectEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLoopProtectTrapLoopDetectEnable.setStatus(_A)
class _ArubaWiredLoopProtectEnableTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ArubaWiredLoopProtectEnableTimer_Type.__name__=_D
_ArubaWiredLoopProtectEnableTimer_Object=MibScalar
arubaWiredLoopProtectEnableTimer=_ArubaWiredLoopProtectEnableTimer_Object((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,1,3),_ArubaWiredLoopProtectEnableTimer_Type())
arubaWiredLoopProtectEnableTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLoopProtectEnableTimer.setStatus(_A)
class _ArubaWiredLoopProtectMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('port',1),('vlan',2)))
_ArubaWiredLoopProtectMode_Type.__name__=_D
_ArubaWiredLoopProtectMode_Object=MibScalar
arubaWiredLoopProtectMode=_ArubaWiredLoopProtectMode_Object((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,1,4),_ArubaWiredLoopProtectMode_Type())
arubaWiredLoopProtectMode.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLoopProtectMode.setStatus(_A)
_ArubaWiredLoopProtectVIDList_Type=VidList
_ArubaWiredLoopProtectVIDList_Object=MibScalar
arubaWiredLoopProtectVIDList=_ArubaWiredLoopProtectVIDList_Object((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,1,5),_ArubaWiredLoopProtectVIDList_Type())
arubaWiredLoopProtectVIDList.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLoopProtectVIDList.setStatus(_A)
_ArubaWiredLoopProtectPort_ObjectIdentity=ObjectIdentity
arubaWiredLoopProtectPort=_ArubaWiredLoopProtectPort_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,2))
_ArubaWiredLoopProtectPortTable_Object=MibTable
arubaWiredLoopProtectPortTable=_ArubaWiredLoopProtectPortTable_Object((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,2,1))
if mibBuilder.loadTexts:arubaWiredLoopProtectPortTable.setStatus(_A)
_ArubaWiredLoopProtectPortEntry_Object=MibTableRow
arubaWiredLoopProtectPortEntry=_ArubaWiredLoopProtectPortEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,2,1,1))
arubaWiredLoopProtectPortEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:arubaWiredLoopProtectPortEntry.setStatus(_A)
_ArubaWiredLoopProtectPortInterfaceIndex_Type=InterfaceIndex
_ArubaWiredLoopProtectPortInterfaceIndex_Object=MibTableColumn
arubaWiredLoopProtectPortInterfaceIndex=_ArubaWiredLoopProtectPortInterfaceIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,2,1,1,1),_ArubaWiredLoopProtectPortInterfaceIndex_Type())
arubaWiredLoopProtectPortInterfaceIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:arubaWiredLoopProtectPortInterfaceIndex.setStatus(_A)
_ArubaWiredLoopProtectPortEnable_Type=TruthValue
_ArubaWiredLoopProtectPortEnable_Object=MibTableColumn
arubaWiredLoopProtectPortEnable=_ArubaWiredLoopProtectPortEnable_Object((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,2,1,1,2),_ArubaWiredLoopProtectPortEnable_Type())
arubaWiredLoopProtectPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLoopProtectPortEnable.setStatus(_A)
_ArubaWiredLoopProtectPortLoopDetected_Type=TruthValue
_ArubaWiredLoopProtectPortLoopDetected_Object=MibTableColumn
arubaWiredLoopProtectPortLoopDetected=_ArubaWiredLoopProtectPortLoopDetected_Object((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,2,1,1,3),_ArubaWiredLoopProtectPortLoopDetected_Type())
arubaWiredLoopProtectPortLoopDetected.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredLoopProtectPortLoopDetected.setStatus(_A)
_ArubaWiredLoopProtectPortLastLoopTime_Type=TimeStamp
_ArubaWiredLoopProtectPortLastLoopTime_Object=MibTableColumn
arubaWiredLoopProtectPortLastLoopTime=_ArubaWiredLoopProtectPortLastLoopTime_Object((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,2,1,1,4),_ArubaWiredLoopProtectPortLastLoopTime_Type())
arubaWiredLoopProtectPortLastLoopTime.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredLoopProtectPortLastLoopTime.setStatus(_A)
_ArubaWiredLoopProtectPortLoopCount_Type=Counter32
_ArubaWiredLoopProtectPortLoopCount_Object=MibTableColumn
arubaWiredLoopProtectPortLoopCount=_ArubaWiredLoopProtectPortLoopCount_Object((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,2,1,1,5),_ArubaWiredLoopProtectPortLoopCount_Type())
arubaWiredLoopProtectPortLoopCount.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredLoopProtectPortLoopCount.setStatus(_A)
_ArubaWiredLoopProtectPortReceiverAction_Type=LoopProtectReceiverAction
_ArubaWiredLoopProtectPortReceiverAction_Object=MibTableColumn
arubaWiredLoopProtectPortReceiverAction=_ArubaWiredLoopProtectPortReceiverAction_Object((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,2,1,1,6),_ArubaWiredLoopProtectPortReceiverAction_Type())
arubaWiredLoopProtectPortReceiverAction.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLoopProtectPortReceiverAction.setStatus(_A)
class _ArubaWiredLoopProtectLoopDetectedVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_ArubaWiredLoopProtectLoopDetectedVlan_Type.__name__=_D
_ArubaWiredLoopProtectLoopDetectedVlan_Object=MibTableColumn
arubaWiredLoopProtectLoopDetectedVlan=_ArubaWiredLoopProtectLoopDetectedVlan_Object((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,2,1,1,7),_ArubaWiredLoopProtectLoopDetectedVlan_Type())
arubaWiredLoopProtectLoopDetectedVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredLoopProtectLoopDetectedVlan.setStatus(_A)
_ArubaWiredLoopProtectPortVlanList_Type=VidList
_ArubaWiredLoopProtectPortVlanList_Object=MibTableColumn
arubaWiredLoopProtectPortVlanList=_ArubaWiredLoopProtectPortVlanList_Object((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,2,1,1,8),_ArubaWiredLoopProtectPortVlanList_Type())
arubaWiredLoopProtectPortVlanList.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLoopProtectPortVlanList.setStatus(_A)
_ArubaWiredLoopProtectConformance_ObjectIdentity=ObjectIdentity
arubaWiredLoopProtectConformance=_ArubaWiredLoopProtectConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,3))
_ArubaWiredLoopProtectGroups_ObjectIdentity=ObjectIdentity
arubaWiredLoopProtectGroups=_ArubaWiredLoopProtectGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,3,1))
_ArubaWiredLoopProtectCompliances_ObjectIdentity=ObjectIdentity
arubaWiredLoopProtectCompliances=_ArubaWiredLoopProtectCompliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,3,2))
arubaWiredLoopProtectBaseGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,3,1,4))
arubaWiredLoopProtectBaseGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:arubaWiredLoopProtectBaseGroup.setStatus(_A)
arubaWiredLoopProtectVLANGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,3,1,10))
arubaWiredLoopProtectVLANGroup.setObjects(*((_B,_R),(_B,_S),(_B,_J),(_B,_T)))
if mibBuilder.loadTexts:arubaWiredLoopProtectVLANGroup.setStatus(_A)
arubaWiredLoopProtectLoopDetectedNotification=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,0,1))
arubaWiredLoopProtectLoopDetectedNotification.setObjects(*((_H,_I),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:arubaWiredLoopProtectLoopDetectedNotification.setStatus(_A)
arubaWiredLoopProtectVlanLoopDetectedNotification=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,0,2))
arubaWiredLoopProtectVlanLoopDetectedNotification.setObjects(*((_H,_I),(_B,_F),(_B,_G),(_B,_J)))
if mibBuilder.loadTexts:arubaWiredLoopProtectVlanLoopDetectedNotification.setStatus(_A)
arubaWiredLoopProtectNotificationsGroup=NotificationGroup((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,3,1,11))
arubaWiredLoopProtectNotificationsGroup.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:arubaWiredLoopProtectNotificationsGroup.setStatus(_A)
arubaWiredLoopProtectCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,1,1,5,3,2,5))
arubaWiredLoopProtectCompliance.setObjects(*((_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:arubaWiredLoopProtectCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ConfigStatus':ConfigStatus,'VidList':VidList,'LoopProtectReceiverAction':LoopProtectReceiverAction,'arubaWiredLoopProtectMIB':arubaWiredLoopProtectMIB,'arubaWiredLoopProtectObjects':arubaWiredLoopProtectObjects,'arubaWiredLoopProtect':arubaWiredLoopProtect,'arubaWiredLoopProtectNotifications':arubaWiredLoopProtectNotifications,_U:arubaWiredLoopProtectLoopDetectedNotification,_V:arubaWiredLoopProtectVlanLoopDetectedNotification,'arubaWiredLoopProtectBase':arubaWiredLoopProtectBase,_L:arubaWiredLoopProtectInterval,_N:arubaWiredLoopProtectTrapLoopDetectEnable,_M:arubaWiredLoopProtectEnableTimer,_R:arubaWiredLoopProtectMode,_S:arubaWiredLoopProtectVIDList,'arubaWiredLoopProtectPort':arubaWiredLoopProtectPort,'arubaWiredLoopProtectPortTable':arubaWiredLoopProtectPortTable,'arubaWiredLoopProtectPortEntry':arubaWiredLoopProtectPortEntry,_K:arubaWiredLoopProtectPortInterfaceIndex,_O:arubaWiredLoopProtectPortEnable,_P:arubaWiredLoopProtectPortLoopDetected,_Q:arubaWiredLoopProtectPortLastLoopTime,_F:arubaWiredLoopProtectPortLoopCount,_G:arubaWiredLoopProtectPortReceiverAction,_J:arubaWiredLoopProtectLoopDetectedVlan,_T:arubaWiredLoopProtectPortVlanList,'arubaWiredLoopProtectConformance':arubaWiredLoopProtectConformance,'arubaWiredLoopProtectGroups':arubaWiredLoopProtectGroups,_W:arubaWiredLoopProtectBaseGroup,_Y:arubaWiredLoopProtectVLANGroup,_X:arubaWiredLoopProtectNotificationsGroup,'arubaWiredLoopProtectCompliances':arubaWiredLoopProtectCompliances,'arubaWiredLoopProtectCompliance':arubaWiredLoopProtectCompliance})