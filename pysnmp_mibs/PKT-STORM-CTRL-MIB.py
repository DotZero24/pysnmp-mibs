_I='read-only'
_H='minutes'
_G='disabled'
_F='enabled'
_E='swPktStormCtrlPortIndex'
_D='PKT-STORM-CTRL-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
swPktStormMIB=ModuleIdentity((1,3,6,1,4,1,171,12,25))
class PortList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwPktStormCtrl_ObjectIdentity=ObjectIdentity
swPktStormCtrl=_SwPktStormCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,25,1))
_SwPktStormRecover_Type=PortList
_SwPktStormRecover_Object=MibScalar
swPktStormRecover=_SwPktStormRecover_Object((1,3,6,1,4,1,171,12,25,1,1),_SwPktStormRecover_Type())
swPktStormRecover.setMaxAccess(_C)
if mibBuilder.loadTexts:swPktStormRecover.setStatus(_A)
class _SwPktStormTrapCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('stormOccurred',2),('stormCleared',3),('both',4)))
_SwPktStormTrapCtrl_Type.__name__=_B
_SwPktStormTrapCtrl_Object=MibScalar
swPktStormTrapCtrl=_SwPktStormTrapCtrl_Object((1,3,6,1,4,1,171,12,25,1,2),_SwPktStormTrapCtrl_Type())
swPktStormTrapCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:swPktStormTrapCtrl.setStatus(_A)
class _SwPktStormLogCtrl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwPktStormLogCtrl_Type.__name__=_B
_SwPktStormLogCtrl_Object=MibScalar
swPktStormLogCtrl=_SwPktStormLogCtrl_Object((1,3,6,1,4,1,171,12,25,1,3),_SwPktStormLogCtrl_Type())
swPktStormLogCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:swPktStormLogCtrl.setStatus(_A)
class _SwPktStormAutoRecoverTime_Type(Integer32):defaultValue=0
_SwPktStormAutoRecoverTime_Type.__name__=_B
_SwPktStormAutoRecoverTime_Object=MibScalar
swPktStormAutoRecoverTime=_SwPktStormAutoRecoverTime_Object((1,3,6,1,4,1,171,12,25,1,4),_SwPktStormAutoRecoverTime_Type())
swPktStormAutoRecoverTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swPktStormAutoRecoverTime.setStatus(_A)
if mibBuilder.loadTexts:swPktStormAutoRecoverTime.setUnits(_H)
_SwPktStormInfo_ObjectIdentity=ObjectIdentity
swPktStormInfo=_SwPktStormInfo_ObjectIdentity((1,3,6,1,4,1,171,12,25,2))
_SwPktStormMgmt_ObjectIdentity=ObjectIdentity
swPktStormMgmt=_SwPktStormMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,25,3))
_SwPktStormCtrlTable_Object=MibTable
swPktStormCtrlTable=_SwPktStormCtrlTable_Object((1,3,6,1,4,1,171,12,25,3,1))
if mibBuilder.loadTexts:swPktStormCtrlTable.setStatus(_A)
_SwPktStormCtrlEntry_Object=MibTableRow
swPktStormCtrlEntry=_SwPktStormCtrlEntry_Object((1,3,6,1,4,1,171,12,25,3,1,1))
swPktStormCtrlEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:swPktStormCtrlEntry.setStatus(_A)
class _SwPktStormCtrlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwPktStormCtrlPortIndex_Type.__name__=_B
_SwPktStormCtrlPortIndex_Object=MibTableColumn
swPktStormCtrlPortIndex=_SwPktStormCtrlPortIndex_Object((1,3,6,1,4,1,171,12,25,3,1,1,1),_SwPktStormCtrlPortIndex_Type())
swPktStormCtrlPortIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:swPktStormCtrlPortIndex.setStatus(_A)
class _SwPktStormCtrlthreshold_Type(Integer32):defaultValue=131072
_SwPktStormCtrlthreshold_Type.__name__=_B
_SwPktStormCtrlthreshold_Object=MibTableColumn
swPktStormCtrlthreshold=_SwPktStormCtrlthreshold_Object((1,3,6,1,4,1,171,12,25,3,1,1,2),_SwPktStormCtrlthreshold_Type())
swPktStormCtrlthreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:swPktStormCtrlthreshold.setStatus('obsolete')
class _SwPktStormCtrlBroadcastStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwPktStormCtrlBroadcastStatus_Type.__name__=_B
_SwPktStormCtrlBroadcastStatus_Object=MibTableColumn
swPktStormCtrlBroadcastStatus=_SwPktStormCtrlBroadcastStatus_Object((1,3,6,1,4,1,171,12,25,3,1,1,3),_SwPktStormCtrlBroadcastStatus_Type())
swPktStormCtrlBroadcastStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swPktStormCtrlBroadcastStatus.setStatus(_A)
class _SwPktStormCtrlMulticastStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwPktStormCtrlMulticastStatus_Type.__name__=_B
_SwPktStormCtrlMulticastStatus_Object=MibTableColumn
swPktStormCtrlMulticastStatus=_SwPktStormCtrlMulticastStatus_Object((1,3,6,1,4,1,171,12,25,3,1,1,4),_SwPktStormCtrlMulticastStatus_Type())
swPktStormCtrlMulticastStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swPktStormCtrlMulticastStatus.setStatus(_A)
class _SwPktStormCtrlUnicastStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwPktStormCtrlUnicastStatus_Type.__name__=_B
_SwPktStormCtrlUnicastStatus_Object=MibTableColumn
swPktStormCtrlUnicastStatus=_SwPktStormCtrlUnicastStatus_Object((1,3,6,1,4,1,171,12,25,3,1,1,5),_SwPktStormCtrlUnicastStatus_Type())
swPktStormCtrlUnicastStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swPktStormCtrlUnicastStatus.setStatus(_A)
class _SwPktStormCtrlActionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('shutdown',1),('drop',2)))
_SwPktStormCtrlActionStatus_Type.__name__=_B
_SwPktStormCtrlActionStatus_Object=MibTableColumn
swPktStormCtrlActionStatus=_SwPktStormCtrlActionStatus_Object((1,3,6,1,4,1,171,12,25,3,1,1,6),_SwPktStormCtrlActionStatus_Type())
swPktStormCtrlActionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swPktStormCtrlActionStatus.setStatus(_A)
class _SwPktStormCtrlCountDown_Type(Integer32):defaultValue=0
_SwPktStormCtrlCountDown_Type.__name__=_B
_SwPktStormCtrlCountDown_Object=MibTableColumn
swPktStormCtrlCountDown=_SwPktStormCtrlCountDown_Object((1,3,6,1,4,1,171,12,25,3,1,1,7),_SwPktStormCtrlCountDown_Type())
swPktStormCtrlCountDown.setMaxAccess(_C)
if mibBuilder.loadTexts:swPktStormCtrlCountDown.setStatus(_A)
if mibBuilder.loadTexts:swPktStormCtrlCountDown.setUnits(_H)
class _SwPktStormCtrlTimeinterval_Type(Integer32):defaultValue=5
_SwPktStormCtrlTimeinterval_Type.__name__=_B
_SwPktStormCtrlTimeinterval_Object=MibTableColumn
swPktStormCtrlTimeinterval=_SwPktStormCtrlTimeinterval_Object((1,3,6,1,4,1,171,12,25,3,1,1,8),_SwPktStormCtrlTimeinterval_Type())
swPktStormCtrlTimeinterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swPktStormCtrlTimeinterval.setStatus(_A)
if mibBuilder.loadTexts:swPktStormCtrlTimeinterval.setUnits('seconds')
class _SwPktStormCtrlShutdownForever_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_SwPktStormCtrlShutdownForever_Type.__name__=_B
_SwPktStormCtrlShutdownForever_Object=MibTableColumn
swPktStormCtrlShutdownForever=_SwPktStormCtrlShutdownForever_Object((1,3,6,1,4,1,171,12,25,3,1,1,9),_SwPktStormCtrlShutdownForever_Type())
swPktStormCtrlShutdownForever.setMaxAccess(_I)
if mibBuilder.loadTexts:swPktStormCtrlShutdownForever.setStatus(_A)
class _SwPktStormCtrlBCastThreshold_Type(Integer32):defaultValue=131072
_SwPktStormCtrlBCastThreshold_Type.__name__=_B
_SwPktStormCtrlBCastThreshold_Object=MibTableColumn
swPktStormCtrlBCastThreshold=_SwPktStormCtrlBCastThreshold_Object((1,3,6,1,4,1,171,12,25,3,1,1,10),_SwPktStormCtrlBCastThreshold_Type())
swPktStormCtrlBCastThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:swPktStormCtrlBCastThreshold.setStatus(_A)
class _SwPktStormCtrlMCastThreshold_Type(Integer32):defaultValue=131072
_SwPktStormCtrlMCastThreshold_Type.__name__=_B
_SwPktStormCtrlMCastThreshold_Object=MibTableColumn
swPktStormCtrlMCastThreshold=_SwPktStormCtrlMCastThreshold_Object((1,3,6,1,4,1,171,12,25,3,1,1,11),_SwPktStormCtrlMCastThreshold_Type())
swPktStormCtrlMCastThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:swPktStormCtrlMCastThreshold.setStatus(_A)
class _SwPktStormCtrlUnicastThreshold_Type(Integer32):defaultValue=131072
_SwPktStormCtrlUnicastThreshold_Type.__name__=_B
_SwPktStormCtrlUnicastThreshold_Object=MibTableColumn
swPktStormCtrlUnicastThreshold=_SwPktStormCtrlUnicastThreshold_Object((1,3,6,1,4,1,171,12,25,3,1,1,12),_SwPktStormCtrlUnicastThreshold_Type())
swPktStormCtrlUnicastThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:swPktStormCtrlUnicastThreshold.setStatus(_A)
_SwPktStormNotify_ObjectIdentity=ObjectIdentity
swPktStormNotify=_SwPktStormNotify_ObjectIdentity((1,3,6,1,4,1,171,12,25,5))
_SwPktStormNotifyPrefix_ObjectIdentity=ObjectIdentity
swPktStormNotifyPrefix=_SwPktStormNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,171,12,25,5,0))
swPktStormOccurred=NotificationType((1,3,6,1,4,1,171,12,25,5,0,1))
swPktStormOccurred.setObjects((_D,_E))
if mibBuilder.loadTexts:swPktStormOccurred.setStatus(_A)
swPktStormCleared=NotificationType((1,3,6,1,4,1,171,12,25,5,0,2))
swPktStormCleared.setObjects((_D,_E))
if mibBuilder.loadTexts:swPktStormCleared.setStatus(_A)
swPktStormDisablePort=NotificationType((1,3,6,1,4,1,171,12,25,5,0,3))
swPktStormDisablePort.setObjects((_D,_E))
if mibBuilder.loadTexts:swPktStormDisablePort.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'PortList':PortList,'swPktStormMIB':swPktStormMIB,'swPktStormCtrl':swPktStormCtrl,'swPktStormRecover':swPktStormRecover,'swPktStormTrapCtrl':swPktStormTrapCtrl,'swPktStormLogCtrl':swPktStormLogCtrl,'swPktStormAutoRecoverTime':swPktStormAutoRecoverTime,'swPktStormInfo':swPktStormInfo,'swPktStormMgmt':swPktStormMgmt,'swPktStormCtrlTable':swPktStormCtrlTable,'swPktStormCtrlEntry':swPktStormCtrlEntry,_E:swPktStormCtrlPortIndex,'swPktStormCtrlthreshold':swPktStormCtrlthreshold,'swPktStormCtrlBroadcastStatus':swPktStormCtrlBroadcastStatus,'swPktStormCtrlMulticastStatus':swPktStormCtrlMulticastStatus,'swPktStormCtrlUnicastStatus':swPktStormCtrlUnicastStatus,'swPktStormCtrlActionStatus':swPktStormCtrlActionStatus,'swPktStormCtrlCountDown':swPktStormCtrlCountDown,'swPktStormCtrlTimeinterval':swPktStormCtrlTimeinterval,'swPktStormCtrlShutdownForever':swPktStormCtrlShutdownForever,'swPktStormCtrlBCastThreshold':swPktStormCtrlBCastThreshold,'swPktStormCtrlMCastThreshold':swPktStormCtrlMCastThreshold,'swPktStormCtrlUnicastThreshold':swPktStormCtrlUnicastThreshold,'swPktStormNotify':swPktStormNotify,'swPktStormNotifyPrefix':swPktStormNotifyPrefix,'swPktStormOccurred':swPktStormOccurred,'swPktStormCleared':swPktStormCleared,'swPktStormDisablePort':swPktStormDisablePort})