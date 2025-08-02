_O='read-only'
_N='cleared'
_M='detected'
_L='one-minute'
_K='one-second'
_J='dot1agCfmMaMepListIdentifier'
_I='disabled'
_H='enabled'
_G='dot1agCfmMepIdentifier'
_F='dot1agCfmMdIndex'
_E='dot1agCfmMaIndex'
_D='read-write'
_C='Integer32'
_B='current'
_A='IEEE8021-CFM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
Dot1agCfmMDLevel,Dot1agCfmMepId,dot1agCfmMaIndex,dot1agCfmMaMepListIdentifier,dot1agCfmMdIndex,dot1agCfmMepIdentifier=mibBuilder.importSymbols(_A,'Dot1agCfmMDLevel','Dot1agCfmMepId',_E,_J,_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
swCFMExtensionMIB=ModuleIdentity((1,3,6,1,4,1,171,12,86))
_SwCFMExtFaultMgmt_ObjectIdentity=ObjectIdentity
swCFMExtFaultMgmt=_SwCFMExtFaultMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,86,1))
_SwCFMExtMgmtTable_Object=MibTable
swCFMExtMgmtTable=_SwCFMExtMgmtTable_Object((1,3,6,1,4,1,171,12,86,1,1))
if mibBuilder.loadTexts:swCFMExtMgmtTable.setStatus(_B)
_SwCFMExtMgmtEntry_Object=MibTableRow
swCFMExtMgmtEntry=_SwCFMExtMgmtEntry_Object((1,3,6,1,4,1,171,12,86,1,1,1))
swCFMExtMgmtEntry.setIndexNames((0,_A,_F),(0,_A,_E),(0,_A,_G))
if mibBuilder.loadTexts:swCFMExtMgmtEntry.setStatus(_B)
class _SwCFMExtMgmtAISState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SwCFMExtMgmtAISState_Type.__name__=_C
_SwCFMExtMgmtAISState_Object=MibTableColumn
swCFMExtMgmtAISState=_SwCFMExtMgmtAISState_Object((1,3,6,1,4,1,171,12,86,1,1,1,1),_SwCFMExtMgmtAISState_Type())
swCFMExtMgmtAISState.setMaxAccess(_D)
if mibBuilder.loadTexts:swCFMExtMgmtAISState.setStatus(_B)
class _SwCFMExtMgmtAISPeriod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_SwCFMExtMgmtAISPeriod_Type.__name__=_C
_SwCFMExtMgmtAISPeriod_Object=MibTableColumn
swCFMExtMgmtAISPeriod=_SwCFMExtMgmtAISPeriod_Object((1,3,6,1,4,1,171,12,86,1,1,1,2),_SwCFMExtMgmtAISPeriod_Type())
swCFMExtMgmtAISPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:swCFMExtMgmtAISPeriod.setStatus(_B)
_SwCFMExtMgmtAISLevel_Type=Dot1agCfmMDLevel
_SwCFMExtMgmtAISLevel_Object=MibTableColumn
swCFMExtMgmtAISLevel=_SwCFMExtMgmtAISLevel_Object((1,3,6,1,4,1,171,12,86,1,1,1,3),_SwCFMExtMgmtAISLevel_Type())
swCFMExtMgmtAISLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:swCFMExtMgmtAISLevel.setStatus(_B)
class _SwCFMExtMgmtAISStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SwCFMExtMgmtAISStatus_Type.__name__=_C
_SwCFMExtMgmtAISStatus_Object=MibTableColumn
swCFMExtMgmtAISStatus=_SwCFMExtMgmtAISStatus_Object((1,3,6,1,4,1,171,12,86,1,1,1,4),_SwCFMExtMgmtAISStatus_Type())
swCFMExtMgmtAISStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:swCFMExtMgmtAISStatus.setStatus(_B)
class _SwCFMExtMgmtLockState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SwCFMExtMgmtLockState_Type.__name__=_C
_SwCFMExtMgmtLockState_Object=MibTableColumn
swCFMExtMgmtLockState=_SwCFMExtMgmtLockState_Object((1,3,6,1,4,1,171,12,86,1,1,1,5),_SwCFMExtMgmtLockState_Type())
swCFMExtMgmtLockState.setMaxAccess(_D)
if mibBuilder.loadTexts:swCFMExtMgmtLockState.setStatus(_B)
class _SwCFMExtMgmtLockPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_SwCFMExtMgmtLockPeriod_Type.__name__=_C
_SwCFMExtMgmtLockPeriod_Object=MibTableColumn
swCFMExtMgmtLockPeriod=_SwCFMExtMgmtLockPeriod_Object((1,3,6,1,4,1,171,12,86,1,1,1,6),_SwCFMExtMgmtLockPeriod_Type())
swCFMExtMgmtLockPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:swCFMExtMgmtLockPeriod.setStatus(_B)
_SwCFMExtMgmtLockLevel_Type=Dot1agCfmMDLevel
_SwCFMExtMgmtLockLevel_Object=MibTableColumn
swCFMExtMgmtLockLevel=_SwCFMExtMgmtLockLevel_Object((1,3,6,1,4,1,171,12,86,1,1,1,7),_SwCFMExtMgmtLockLevel_Type())
swCFMExtMgmtLockLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:swCFMExtMgmtLockLevel.setStatus(_B)
class _SwCFMExtMgmtLockStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SwCFMExtMgmtLockStatus_Type.__name__=_C
_SwCFMExtMgmtLockStatus_Object=MibTableColumn
swCFMExtMgmtLockStatus=_SwCFMExtMgmtLockStatus_Object((1,3,6,1,4,1,171,12,86,1,1,1,8),_SwCFMExtMgmtLockStatus_Type())
swCFMExtMgmtLockStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:swCFMExtMgmtLockStatus.setStatus(_B)
_SwCFMExtMgmtLockCtrlTable_Object=MibTable
swCFMExtMgmtLockCtrlTable=_SwCFMExtMgmtLockCtrlTable_Object((1,3,6,1,4,1,171,12,86,1,2))
if mibBuilder.loadTexts:swCFMExtMgmtLockCtrlTable.setStatus(_B)
_SwCFMExtMgmtLockCtrlEntry_Object=MibTableRow
swCFMExtMgmtLockCtrlEntry=_SwCFMExtMgmtLockCtrlEntry_Object((1,3,6,1,4,1,171,12,86,1,2,1))
swCFMExtMgmtLockCtrlEntry.setIndexNames((0,_A,_F),(0,_A,_E),(0,_A,_G),(0,_A,_J))
if mibBuilder.loadTexts:swCFMExtMgmtLockCtrlEntry.setStatus(_B)
class _SwCFMExtMgmtLockCtrlAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
_SwCFMExtMgmtLockCtrlAction_Type.__name__=_C
_SwCFMExtMgmtLockCtrlAction_Object=MibTableColumn
swCFMExtMgmtLockCtrlAction=_SwCFMExtMgmtLockCtrlAction_Object((1,3,6,1,4,1,171,12,86,1,2,1,1),_SwCFMExtMgmtLockCtrlAction_Type())
swCFMExtMgmtLockCtrlAction.setMaxAccess(_D)
if mibBuilder.loadTexts:swCFMExtMgmtLockCtrlAction.setStatus(_B)
_SwCFMExtNotify_ObjectIdentity=ObjectIdentity
swCFMExtNotify=_SwCFMExtNotify_ObjectIdentity((1,3,6,1,4,1,171,12,86,100))
_SwCFMExtNotifyPrefix_ObjectIdentity=ObjectIdentity
swCFMExtNotifyPrefix=_SwCFMExtNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,171,12,86,100,0))
_SwCFMExtNotifyMgmt_ObjectIdentity=ObjectIdentity
swCFMExtNotifyMgmt=_SwCFMExtNotifyMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,86,100,1))
class _SwCFMExtAISNotifyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SwCFMExtAISNotifyState_Type.__name__=_C
_SwCFMExtAISNotifyState_Object=MibScalar
swCFMExtAISNotifyState=_SwCFMExtAISNotifyState_Object((1,3,6,1,4,1,171,12,86,100,1,1),_SwCFMExtAISNotifyState_Type())
swCFMExtAISNotifyState.setMaxAccess(_D)
if mibBuilder.loadTexts:swCFMExtAISNotifyState.setStatus(_B)
class _SwCFMExtLockNotifyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SwCFMExtLockNotifyState_Type.__name__=_C
_SwCFMExtLockNotifyState_Object=MibScalar
swCFMExtLockNotifyState=_SwCFMExtLockNotifyState_Object((1,3,6,1,4,1,171,12,86,100,1,2),_SwCFMExtLockNotifyState_Type())
swCFMExtLockNotifyState.setMaxAccess(_D)
if mibBuilder.loadTexts:swCFMExtLockNotifyState.setStatus(_B)
swCFMExtAISOccurred=NotificationType((1,3,6,1,4,1,171,12,86,100,0,1))
swCFMExtAISOccurred.setObjects(*((_A,_F),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:swCFMExtAISOccurred.setStatus(_B)
swCFMExtAISCleared=NotificationType((1,3,6,1,4,1,171,12,86,100,0,2))
swCFMExtAISCleared.setObjects(*((_A,_F),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:swCFMExtAISCleared.setStatus(_B)
swCFMExtLockOccurred=NotificationType((1,3,6,1,4,1,171,12,86,100,0,3))
swCFMExtLockOccurred.setObjects(*((_A,_F),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:swCFMExtLockOccurred.setStatus(_B)
swCFMExtLockCleared=NotificationType((1,3,6,1,4,1,171,12,86,100,0,4))
swCFMExtLockCleared.setObjects(*((_A,_F),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:swCFMExtLockCleared.setStatus(_B)
mibBuilder.exportSymbols('CFMEXTENSION-MIB',**{'swCFMExtensionMIB':swCFMExtensionMIB,'swCFMExtFaultMgmt':swCFMExtFaultMgmt,'swCFMExtMgmtTable':swCFMExtMgmtTable,'swCFMExtMgmtEntry':swCFMExtMgmtEntry,'swCFMExtMgmtAISState':swCFMExtMgmtAISState,'swCFMExtMgmtAISPeriod':swCFMExtMgmtAISPeriod,'swCFMExtMgmtAISLevel':swCFMExtMgmtAISLevel,'swCFMExtMgmtAISStatus':swCFMExtMgmtAISStatus,'swCFMExtMgmtLockState':swCFMExtMgmtLockState,'swCFMExtMgmtLockPeriod':swCFMExtMgmtLockPeriod,'swCFMExtMgmtLockLevel':swCFMExtMgmtLockLevel,'swCFMExtMgmtLockStatus':swCFMExtMgmtLockStatus,'swCFMExtMgmtLockCtrlTable':swCFMExtMgmtLockCtrlTable,'swCFMExtMgmtLockCtrlEntry':swCFMExtMgmtLockCtrlEntry,'swCFMExtMgmtLockCtrlAction':swCFMExtMgmtLockCtrlAction,'swCFMExtNotify':swCFMExtNotify,'swCFMExtNotifyPrefix':swCFMExtNotifyPrefix,'swCFMExtAISOccurred':swCFMExtAISOccurred,'swCFMExtAISCleared':swCFMExtAISCleared,'swCFMExtLockOccurred':swCFMExtLockOccurred,'swCFMExtLockCleared':swCFMExtLockCleared,'swCFMExtNotifyMgmt':swCFMExtNotifyMgmt,'swCFMExtAISNotifyState':swCFMExtAISNotifyState,'swCFMExtLockNotifyState':swCFMExtLockNotifyState})