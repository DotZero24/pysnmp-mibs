_i='swDoSNotifyVarPortNumber'
_h='swDoSNotifyVarIpAddr'
_g='accessible-for-notify'
_f='disabled'
_e='enabled'
_d='winnuke-attack'
_c='tracert-attack'
_b='tcpudp-port-zero'
_a='tcp-tiny-frag-attack'
_Z='tcp-syn-with-data'
_Y='tcp-over-mac-mcbc'
_X='tcp-flag-synrst'
_W='ping-death-attack'
_V='ip-source-route-attack'
_U='ip-route-record-attac'
_T='icmp-unreachable-attack'
_S='icmp-redirect-attack'
_R='fraggle-attack'
_Q='arp-mac-sa-mismatch'
_P='tcp-syn-srcport-less-1024'
_O='tcp-synfin'
_N='tcp-xmascan'
_M='tcp-null-scan'
_L='smurf-attack'
_K='blat-attack'
_J='land-attack'
_I='disable'
_H='enable'
_G='DisplayString'
_F='read-only'
_E='swDoSCtrlType'
_D='DOS-PREV-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
swDoSMgmtMIB=ModuleIdentity((1,3,6,1,4,1,171,12,59))
_SwDoSCtrl_ObjectIdentity=ObjectIdentity
swDoSCtrl=_SwDoSCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,59,1))
class _SwDoSTrapLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),('other',3)))
_SwDoSTrapLog_Type.__name__=_B
_SwDoSTrapLog_Object=MibScalar
swDoSTrapLog=_SwDoSTrapLog_Object((1,3,6,1,4,1,171,12,59,1,1),_SwDoSTrapLog_Type())
swDoSTrapLog.setMaxAccess(_C)
if mibBuilder.loadTexts:swDoSTrapLog.setStatus(_A)
class _SwDoSClearCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7),('all',8),('other',9),(_Q,10),(_R,11),(_S,12),(_T,13),(_U,14),(_V,15),(_W,16),(_X,17),(_Y,18),(_Z,19),(_a,20),(_b,21),(_c,22),(_d,23)))
_SwDoSClearCounters_Type.__name__=_B
_SwDoSClearCounters_Object=MibScalar
swDoSClearCounters=_SwDoSClearCounters_Object((1,3,6,1,4,1,171,12,59,1,2),_SwDoSClearCounters_Type())
swDoSClearCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:swDoSClearCounters.setStatus(_A)
_SwDoSCtrlTable_Object=MibTable
swDoSCtrlTable=_SwDoSCtrlTable_Object((1,3,6,1,4,1,171,12,59,1,3))
if mibBuilder.loadTexts:swDoSCtrlTable.setStatus(_A)
_SwDoSCtrlEntry_Object=MibTableRow
swDoSCtrlEntry=_SwDoSCtrlEntry_Object((1,3,6,1,4,1,171,12,59,1,3,1))
swDoSCtrlEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:swDoSCtrlEntry.setStatus(_A)
class _SwDoSCtrlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7),(_Q,10),(_R,11),(_S,12),(_T,13),(_U,14),(_V,15),(_W,16),(_X,17),(_Y,18),(_Z,19),(_a,20),(_b,21),(_c,22),(_d,23)))
_SwDoSCtrlType_Type.__name__=_B
_SwDoSCtrlType_Object=MibTableColumn
swDoSCtrlType=_SwDoSCtrlType_Object((1,3,6,1,4,1,171,12,59,1,3,1,1),_SwDoSCtrlType_Type())
swDoSCtrlType.setMaxAccess(_F)
if mibBuilder.loadTexts:swDoSCtrlType.setStatus(_A)
class _SwDoSCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SwDoSCtrlState_Type.__name__=_B
_SwDoSCtrlState_Object=MibTableColumn
swDoSCtrlState=_SwDoSCtrlState_Object((1,3,6,1,4,1,171,12,59,1,3,1,2),_SwDoSCtrlState_Type())
swDoSCtrlState.setMaxAccess(_C)
if mibBuilder.loadTexts:swDoSCtrlState.setStatus(_A)
class _SwDoSCtrlActionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('drop',1),('mirror',2)))
_SwDoSCtrlActionType_Type.__name__=_B
_SwDoSCtrlActionType_Object=MibTableColumn
swDoSCtrlActionType=_SwDoSCtrlActionType_Object((1,3,6,1,4,1,171,12,59,1,3,1,3),_SwDoSCtrlActionType_Type())
swDoSCtrlActionType.setMaxAccess(_C)
if mibBuilder.loadTexts:swDoSCtrlActionType.setStatus(_A)
class _SwDoSCtrlMirrorPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwDoSCtrlMirrorPort_Type.__name__=_B
_SwDoSCtrlMirrorPort_Object=MibTableColumn
swDoSCtrlMirrorPort=_SwDoSCtrlMirrorPort_Object((1,3,6,1,4,1,171,12,59,1,3,1,4),_SwDoSCtrlMirrorPort_Type())
swDoSCtrlMirrorPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swDoSCtrlMirrorPort.setStatus(_A)
class _SwDoSCtrlMirrorPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_SwDoSCtrlMirrorPriority_Type.__name__=_B
_SwDoSCtrlMirrorPriority_Object=MibTableColumn
swDoSCtrlMirrorPriority=_SwDoSCtrlMirrorPriority_Object((1,3,6,1,4,1,171,12,59,1,3,1,5),_SwDoSCtrlMirrorPriority_Type())
swDoSCtrlMirrorPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:swDoSCtrlMirrorPriority.setStatus(_A)
class _SwDoSCtrlMirrorRxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024000))
_SwDoSCtrlMirrorRxRate_Type.__name__=_B
_SwDoSCtrlMirrorRxRate_Object=MibTableColumn
swDoSCtrlMirrorRxRate=_SwDoSCtrlMirrorRxRate_Object((1,3,6,1,4,1,171,12,59,1,3,1,6),_SwDoSCtrlMirrorRxRate_Type())
swDoSCtrlMirrorRxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:swDoSCtrlMirrorRxRate.setStatus(_A)
_SwDoSCtrlFrameCount_Type=Integer32
_SwDoSCtrlFrameCount_Object=MibTableColumn
swDoSCtrlFrameCount=_SwDoSCtrlFrameCount_Object((1,3,6,1,4,1,171,12,59,1,3,1,7),_SwDoSCtrlFrameCount_Type())
swDoSCtrlFrameCount.setMaxAccess(_F)
if mibBuilder.loadTexts:swDoSCtrlFrameCount.setStatus(_A)
class _SwDoSTrapState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),(_f,2)))
_SwDoSTrapState_Type.__name__=_B
_SwDoSTrapState_Object=MibScalar
swDoSTrapState=_SwDoSTrapState_Object((1,3,6,1,4,1,171,12,59,1,4),_SwDoSTrapState_Type())
swDoSTrapState.setMaxAccess(_C)
if mibBuilder.loadTexts:swDoSTrapState.setStatus(_A)
class _SwDoSLogState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),(_f,2)))
_SwDoSLogState_Type.__name__=_B
_SwDoSLogState_Object=MibScalar
swDoSLogState=_SwDoSLogState_Object((1,3,6,1,4,1,171,12,59,1,5),_SwDoSLogState_Type())
swDoSLogState.setMaxAccess(_C)
if mibBuilder.loadTexts:swDoSLogState.setStatus(_A)
class _SwDoSFunctionVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwDoSFunctionVersion_Type.__name__=_G
_SwDoSFunctionVersion_Object=MibScalar
swDoSFunctionVersion=_SwDoSFunctionVersion_Object((1,3,6,1,4,1,171,12,59,1,6),_SwDoSFunctionVersion_Type())
swDoSFunctionVersion.setMaxAccess(_F)
if mibBuilder.loadTexts:swDoSFunctionVersion.setStatus(_A)
_SwDoSNotify_ObjectIdentity=ObjectIdentity
swDoSNotify=_SwDoSNotify_ObjectIdentity((1,3,6,1,4,1,171,12,59,4))
_SwDoSNotifyPrefix_ObjectIdentity=ObjectIdentity
swDoSNotifyPrefix=_SwDoSNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,171,12,59,4,0))
_SwDoSNotifyVarBindings_ObjectIdentity=ObjectIdentity
swDoSNotifyVarBindings=_SwDoSNotifyVarBindings_ObjectIdentity((1,3,6,1,4,1,171,12,59,4,1))
_SwDoSNotifyVarIpAddr_Type=IpAddress
_SwDoSNotifyVarIpAddr_Object=MibScalar
swDoSNotifyVarIpAddr=_SwDoSNotifyVarIpAddr_Object((1,3,6,1,4,1,171,12,59,4,1,1),_SwDoSNotifyVarIpAddr_Type())
swDoSNotifyVarIpAddr.setMaxAccess(_g)
if mibBuilder.loadTexts:swDoSNotifyVarIpAddr.setStatus(_A)
_SwDoSNotifyVarPortNumber_Type=DisplayString
_SwDoSNotifyVarPortNumber_Object=MibScalar
swDoSNotifyVarPortNumber=_SwDoSNotifyVarPortNumber_Object((1,3,6,1,4,1,171,12,59,4,1,2),_SwDoSNotifyVarPortNumber_Type())
swDoSNotifyVarPortNumber.setMaxAccess(_g)
if mibBuilder.loadTexts:swDoSNotifyVarPortNumber.setStatus(_A)
swDoSAttackDetected=NotificationType((1,3,6,1,4,1,171,12,59,4,0,1))
swDoSAttackDetected.setObjects(*((_D,_E),(_D,_h),(_D,_i)))
if mibBuilder.loadTexts:swDoSAttackDetected.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'swDoSMgmtMIB':swDoSMgmtMIB,'swDoSCtrl':swDoSCtrl,'swDoSTrapLog':swDoSTrapLog,'swDoSClearCounters':swDoSClearCounters,'swDoSCtrlTable':swDoSCtrlTable,'swDoSCtrlEntry':swDoSCtrlEntry,_E:swDoSCtrlType,'swDoSCtrlState':swDoSCtrlState,'swDoSCtrlActionType':swDoSCtrlActionType,'swDoSCtrlMirrorPort':swDoSCtrlMirrorPort,'swDoSCtrlMirrorPriority':swDoSCtrlMirrorPriority,'swDoSCtrlMirrorRxRate':swDoSCtrlMirrorRxRate,'swDoSCtrlFrameCount':swDoSCtrlFrameCount,'swDoSTrapState':swDoSTrapState,'swDoSLogState':swDoSLogState,'swDoSFunctionVersion':swDoSFunctionVersion,'swDoSNotify':swDoSNotify,'swDoSNotifyPrefix':swDoSNotifyPrefix,'swDoSAttackDetected':swDoSAttackDetected,'swDoSNotifyVarBindings':swDoSNotifyVarBindings,_h:swDoSNotifyVarIpAddr,_i:swDoSNotifyVarPortNumber})