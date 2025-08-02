_I='swVlanLoopDetectVID'
_H='read-only'
_G='disabled'
_F='enabled'
_E='swLoopDetectPortIndex'
_D='read-write'
_C='LOOPBACK-DETECT-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
swLoopDetectMIB=ModuleIdentity((1,3,6,1,4,1,171,12,41))
_SwLoopDetectCtrl_ObjectIdentity=ObjectIdentity
swLoopDetectCtrl=_SwLoopDetectCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,41,1))
class _SwLoopDetectAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwLoopDetectAdminState_Type.__name__=_B
_SwLoopDetectAdminState_Object=MibScalar
swLoopDetectAdminState=_SwLoopDetectAdminState_Object((1,3,6,1,4,1,171,12,41,1,1),_SwLoopDetectAdminState_Type())
swLoopDetectAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:swLoopDetectAdminState.setStatus(_A)
class _SwLoopDetectInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_SwLoopDetectInterval_Type.__name__=_B
_SwLoopDetectInterval_Object=MibScalar
swLoopDetectInterval=_SwLoopDetectInterval_Object((1,3,6,1,4,1,171,12,41,1,2),_SwLoopDetectInterval_Type())
swLoopDetectInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:swLoopDetectInterval.setStatus(_A)
class _SwLoopDetectRecoverTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_SwLoopDetectRecoverTime_Type.__name__=_B
_SwLoopDetectRecoverTime_Object=MibScalar
swLoopDetectRecoverTime=_SwLoopDetectRecoverTime_Object((1,3,6,1,4,1,171,12,41,1,3),_SwLoopDetectRecoverTime_Type())
swLoopDetectRecoverTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swLoopDetectRecoverTime.setStatus(_A)
class _SwLoopDetectMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlan-based',1),('port-based',2)))
_SwLoopDetectMode_Type.__name__=_B
_SwLoopDetectMode_Object=MibScalar
swLoopDetectMode=_SwLoopDetectMode_Object((1,3,6,1,4,1,171,12,41,1,4),_SwLoopDetectMode_Type())
swLoopDetectMode.setMaxAccess(_D)
if mibBuilder.loadTexts:swLoopDetectMode.setStatus(_A)
class _SwLoopDetectTrapMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('loop-detected',2),('loop-cleared',3),('both',4)))
_SwLoopDetectTrapMode_Type.__name__=_B
_SwLoopDetectTrapMode_Object=MibScalar
swLoopDetectTrapMode=_SwLoopDetectTrapMode_Object((1,3,6,1,4,1,171,12,41,1,5),_SwLoopDetectTrapMode_Type())
swLoopDetectTrapMode.setMaxAccess(_D)
if mibBuilder.loadTexts:swLoopDetectTrapMode.setStatus(_A)
class _SwLoopDetectLogState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwLoopDetectLogState_Type.__name__=_B
_SwLoopDetectLogState_Object=MibScalar
swLoopDetectLogState=_SwLoopDetectLogState_Object((1,3,6,1,4,1,171,12,41,1,6),_SwLoopDetectLogState_Type())
swLoopDetectLogState.setMaxAccess(_D)
if mibBuilder.loadTexts:swLoopDetectLogState.setStatus(_A)
_SwLoopDetectInfo_ObjectIdentity=ObjectIdentity
swLoopDetectInfo=_SwLoopDetectInfo_ObjectIdentity((1,3,6,1,4,1,171,12,41,2))
_SwLoopDetectPortMgmt_ObjectIdentity=ObjectIdentity
swLoopDetectPortMgmt=_SwLoopDetectPortMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,41,3))
_SwLoopDetectPortTable_Object=MibTable
swLoopDetectPortTable=_SwLoopDetectPortTable_Object((1,3,6,1,4,1,171,12,41,3,1))
if mibBuilder.loadTexts:swLoopDetectPortTable.setStatus(_A)
_SwLoopDetectPortEntry_Object=MibTableRow
swLoopDetectPortEntry=_SwLoopDetectPortEntry_Object((1,3,6,1,4,1,171,12,41,3,1,1))
swLoopDetectPortEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:swLoopDetectPortEntry.setStatus(_A)
class _SwLoopDetectPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwLoopDetectPortIndex_Type.__name__=_B
_SwLoopDetectPortIndex_Object=MibTableColumn
swLoopDetectPortIndex=_SwLoopDetectPortIndex_Object((1,3,6,1,4,1,171,12,41,3,1,1,1),_SwLoopDetectPortIndex_Type())
swLoopDetectPortIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:swLoopDetectPortIndex.setStatus(_A)
class _SwLoopDetectPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwLoopDetectPortState_Type.__name__=_B
_SwLoopDetectPortState_Object=MibTableColumn
swLoopDetectPortState=_SwLoopDetectPortState_Object((1,3,6,1,4,1,171,12,41,3,1,1,2),_SwLoopDetectPortState_Type())
swLoopDetectPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:swLoopDetectPortState.setStatus(_A)
_SwLoopDetectPortLoopVLAN_Type=DisplayString
_SwLoopDetectPortLoopVLAN_Object=MibTableColumn
swLoopDetectPortLoopVLAN=_SwLoopDetectPortLoopVLAN_Object((1,3,6,1,4,1,171,12,41,3,1,1,3),_SwLoopDetectPortLoopVLAN_Type())
swLoopDetectPortLoopVLAN.setMaxAccess(_H)
if mibBuilder.loadTexts:swLoopDetectPortLoopVLAN.setStatus(_A)
class _SwLoopDetectPortLoopStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('loop',2),('error',3)))
_SwLoopDetectPortLoopStatus_Type.__name__=_B
_SwLoopDetectPortLoopStatus_Object=MibTableColumn
swLoopDetectPortLoopStatus=_SwLoopDetectPortLoopStatus_Object((1,3,6,1,4,1,171,12,41,3,1,1,4),_SwLoopDetectPortLoopStatus_Type())
swLoopDetectPortLoopStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:swLoopDetectPortLoopStatus.setStatus(_A)
_SwLoopDetectNotify_ObjectIdentity=ObjectIdentity
swLoopDetectNotify=_SwLoopDetectNotify_ObjectIdentity((1,3,6,1,4,1,171,12,41,10))
_SwLoopDetectNotifyPrefix_ObjectIdentity=ObjectIdentity
swLoopDetectNotifyPrefix=_SwLoopDetectNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,171,12,41,10,0))
_SwLoopDetectNotificationBidings_ObjectIdentity=ObjectIdentity
swLoopDetectNotificationBidings=_SwLoopDetectNotificationBidings_ObjectIdentity((1,3,6,1,4,1,171,12,41,10,1))
_SwVlanLoopDetectVID_Type=Integer32
_SwVlanLoopDetectVID_Object=MibScalar
swVlanLoopDetectVID=_SwVlanLoopDetectVID_Object((1,3,6,1,4,1,171,12,41,10,1,1),_SwVlanLoopDetectVID_Type())
swVlanLoopDetectVID.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:swVlanLoopDetectVID.setStatus(_A)
swPortLoopOccurred=NotificationType((1,3,6,1,4,1,171,12,41,10,0,1))
swPortLoopOccurred.setObjects((_C,_E))
if mibBuilder.loadTexts:swPortLoopOccurred.setStatus(_A)
swPortLoopRestart=NotificationType((1,3,6,1,4,1,171,12,41,10,0,2))
swPortLoopRestart.setObjects((_C,_E))
if mibBuilder.loadTexts:swPortLoopRestart.setStatus(_A)
swVlanLoopOccurred=NotificationType((1,3,6,1,4,1,171,12,41,10,0,3))
swVlanLoopOccurred.setObjects(*((_C,_E),(_C,_I)))
if mibBuilder.loadTexts:swVlanLoopOccurred.setStatus(_A)
swVlanLoopRestart=NotificationType((1,3,6,1,4,1,171,12,41,10,0,4))
swVlanLoopRestart.setObjects(*((_C,_E),(_C,_I)))
if mibBuilder.loadTexts:swVlanLoopRestart.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'swLoopDetectMIB':swLoopDetectMIB,'swLoopDetectCtrl':swLoopDetectCtrl,'swLoopDetectAdminState':swLoopDetectAdminState,'swLoopDetectInterval':swLoopDetectInterval,'swLoopDetectRecoverTime':swLoopDetectRecoverTime,'swLoopDetectMode':swLoopDetectMode,'swLoopDetectTrapMode':swLoopDetectTrapMode,'swLoopDetectLogState':swLoopDetectLogState,'swLoopDetectInfo':swLoopDetectInfo,'swLoopDetectPortMgmt':swLoopDetectPortMgmt,'swLoopDetectPortTable':swLoopDetectPortTable,'swLoopDetectPortEntry':swLoopDetectPortEntry,_E:swLoopDetectPortIndex,'swLoopDetectPortState':swLoopDetectPortState,'swLoopDetectPortLoopVLAN':swLoopDetectPortLoopVLAN,'swLoopDetectPortLoopStatus':swLoopDetectPortLoopStatus,'swLoopDetectNotify':swLoopDetectNotify,'swLoopDetectNotifyPrefix':swLoopDetectNotifyPrefix,'swPortLoopOccurred':swPortLoopOccurred,'swPortLoopRestart':swPortLoopRestart,'swVlanLoopOccurred':swVlanLoopOccurred,'swVlanLoopRestart':swVlanLoopRestart,'swLoopDetectNotificationBidings':swLoopDetectNotificationBidings,_I:swVlanLoopDetectVID})