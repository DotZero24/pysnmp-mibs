_N='swPortSecVID'
_M='swPortSecMac'
_L='not-accessible'
_K='read-only'
_J='swPortSecVLANID'
_I='swPortSecPortIndex'
_H='start'
_G='disabled'
_F='enabled'
_E='other'
_D='DLINK-PORT-SECURITY-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
swPortSecMIB=ModuleIdentity((1,3,6,1,4,1,171,12,63))
_SwPortSecCtrl_ObjectIdentity=ObjectIdentity
swPortSecCtrl=_SwPortSecCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,63,1))
class _SwPortSecTrapLogState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwPortSecTrapLogState_Type.__name__=_C
_SwPortSecTrapLogState_Object=MibScalar
swPortSecTrapLogState=_SwPortSecTrapLogState_Object((1,3,6,1,4,1,171,12,63,1,1),_SwPortSecTrapLogState_Type())
swPortSecTrapLogState.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortSecTrapLogState.setStatus(_A)
_SwPortSecSysMaxLernAddr_Type=Integer32
_SwPortSecSysMaxLernAddr_Object=MibScalar
swPortSecSysMaxLernAddr=_SwPortSecSysMaxLernAddr_Object((1,3,6,1,4,1,171,12,63,1,2),_SwPortSecSysMaxLernAddr_Type())
swPortSecSysMaxLernAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortSecSysMaxLernAddr.setStatus(_A)
class _SwPortSecTrapState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwPortSecTrapState_Type.__name__=_C
_SwPortSecTrapState_Object=MibScalar
swPortSecTrapState=_SwPortSecTrapState_Object((1,3,6,1,4,1,171,12,63,1,3),_SwPortSecTrapState_Type())
swPortSecTrapState.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortSecTrapState.setStatus(_A)
class _SwPortSecLogState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwPortSecLogState_Type.__name__=_C
_SwPortSecLogState_Object=MibScalar
swPortSecLogState=_SwPortSecLogState_Object((1,3,6,1,4,1,171,12,63,1,4),_SwPortSecLogState_Type())
swPortSecLogState.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortSecLogState.setStatus(_A)
_SwPortSecInfo_ObjectIdentity=ObjectIdentity
swPortSecInfo=_SwPortSecInfo_ObjectIdentity((1,3,6,1,4,1,171,12,63,2))
_SwPortSecMgmt_ObjectIdentity=ObjectIdentity
swPortSecMgmt=_SwPortSecMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,63,3))
_SwPortSecMgmtByPort_ObjectIdentity=ObjectIdentity
swPortSecMgmtByPort=_SwPortSecMgmtByPort_ObjectIdentity((1,3,6,1,4,1,171,12,63,3,1))
_SwPortSecPortTable_Object=MibTable
swPortSecPortTable=_SwPortSecPortTable_Object((1,3,6,1,4,1,171,12,63,3,1,1))
if mibBuilder.loadTexts:swPortSecPortTable.setStatus(_A)
_SwPortSecPortEntry_Object=MibTableRow
swPortSecPortEntry=_SwPortSecPortEntry_Object((1,3,6,1,4,1,171,12,63,3,1,1,1))
swPortSecPortEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:swPortSecPortEntry.setStatus(_A)
_SwPortSecPortIndex_Type=Integer32
_SwPortSecPortIndex_Object=MibTableColumn
swPortSecPortIndex=_SwPortSecPortIndex_Object((1,3,6,1,4,1,171,12,63,3,1,1,1,1),_SwPortSecPortIndex_Type())
swPortSecPortIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:swPortSecPortIndex.setStatus(_A)
_SwPortSecPortMaxLernAddr_Type=Integer32
_SwPortSecPortMaxLernAddr_Object=MibTableColumn
swPortSecPortMaxLernAddr=_SwPortSecPortMaxLernAddr_Object((1,3,6,1,4,1,171,12,63,3,1,1,1,2),_SwPortSecPortMaxLernAddr_Type())
swPortSecPortMaxLernAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortSecPortMaxLernAddr.setStatus(_A)
class _SwPortSecPortLockAddrMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('permanent',1),('deleteOnTimeout',2),('deleteOnReset',3)))
_SwPortSecPortLockAddrMode_Type.__name__=_C
_SwPortSecPortLockAddrMode_Object=MibTableColumn
swPortSecPortLockAddrMode=_SwPortSecPortLockAddrMode_Object((1,3,6,1,4,1,171,12,63,3,1,1,1,3),_SwPortSecPortLockAddrMode_Type())
swPortSecPortLockAddrMode.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortSecPortLockAddrMode.setStatus(_A)
class _SwPortSecPortAdmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwPortSecPortAdmState_Type.__name__=_C
_SwPortSecPortAdmState_Object=MibTableColumn
swPortSecPortAdmState=_SwPortSecPortAdmState_Object((1,3,6,1,4,1,171,12,63,3,1,1,1,4),_SwPortSecPortAdmState_Type())
swPortSecPortAdmState.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortSecPortAdmState.setStatus(_A)
class _SwPortSecPortClearCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_H,2)))
_SwPortSecPortClearCtrl_Type.__name__=_C
_SwPortSecPortClearCtrl_Object=MibTableColumn
swPortSecPortClearCtrl=_SwPortSecPortClearCtrl_Object((1,3,6,1,4,1,171,12,63,3,1,1,1,5),_SwPortSecPortClearCtrl_Type())
swPortSecPortClearCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortSecPortClearCtrl.setStatus(_A)
class _SwPortSecPortViolationAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('drop',1),('shutdown',2)))
_SwPortSecPortViolationAction_Type.__name__=_C
_SwPortSecPortViolationAction_Object=MibTableColumn
swPortSecPortViolationAction=_SwPortSecPortViolationAction_Object((1,3,6,1,4,1,171,12,63,3,1,1,1,6),_SwPortSecPortViolationAction_Type())
swPortSecPortViolationAction.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortSecPortViolationAction.setStatus(_A)
_SwPortSecMgmtByVLAN_ObjectIdentity=ObjectIdentity
swPortSecMgmtByVLAN=_SwPortSecMgmtByVLAN_ObjectIdentity((1,3,6,1,4,1,171,12,63,3,2))
_SwPortSecVLANTable_Object=MibTable
swPortSecVLANTable=_SwPortSecVLANTable_Object((1,3,6,1,4,1,171,12,63,3,2,1))
if mibBuilder.loadTexts:swPortSecVLANTable.setStatus(_A)
_SwPortSecVLANEntry_Object=MibTableRow
swPortSecVLANEntry=_SwPortSecVLANEntry_Object((1,3,6,1,4,1,171,12,63,3,2,1,1))
swPortSecVLANEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:swPortSecVLANEntry.setStatus(_A)
class _SwPortSecVLANID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwPortSecVLANID_Type.__name__=_C
_SwPortSecVLANID_Object=MibTableColumn
swPortSecVLANID=_SwPortSecVLANID_Object((1,3,6,1,4,1,171,12,63,3,2,1,1,1),_SwPortSecVLANID_Type())
swPortSecVLANID.setMaxAccess(_L)
if mibBuilder.loadTexts:swPortSecVLANID.setStatus(_A)
_SwPortSecVLANMaxLernAddr_Type=Integer32
_SwPortSecVLANMaxLernAddr_Object=MibTableColumn
swPortSecVLANMaxLernAddr=_SwPortSecVLANMaxLernAddr_Object((1,3,6,1,4,1,171,12,63,3,2,1,1,2),_SwPortSecVLANMaxLernAddr_Type())
swPortSecVLANMaxLernAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortSecVLANMaxLernAddr.setStatus(_A)
class _SwPortSecVLANClearCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_H,2)))
_SwPortSecVLANClearCtrl_Type.__name__=_C
_SwPortSecVLANClearCtrl_Object=MibTableColumn
swPortSecVLANClearCtrl=_SwPortSecVLANClearCtrl_Object((1,3,6,1,4,1,171,12,63,3,2,1,1,3),_SwPortSecVLANClearCtrl_Type())
swPortSecVLANClearCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortSecVLANClearCtrl.setStatus(_A)
_SwPortSecMgmtByVLANOnPort_ObjectIdentity=ObjectIdentity
swPortSecMgmtByVLANOnPort=_SwPortSecMgmtByVLANOnPort_ObjectIdentity((1,3,6,1,4,1,171,12,63,3,3))
_SwPortSecVLANOnPortTable_Object=MibTable
swPortSecVLANOnPortTable=_SwPortSecVLANOnPortTable_Object((1,3,6,1,4,1,171,12,63,3,3,1))
if mibBuilder.loadTexts:swPortSecVLANOnPortTable.setStatus(_A)
_SwPortSecVLANOnPortEntry_Object=MibTableRow
swPortSecVLANOnPortEntry=_SwPortSecVLANOnPortEntry_Object((1,3,6,1,4,1,171,12,63,3,3,1,1))
swPortSecVLANOnPortEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:swPortSecVLANOnPortEntry.setStatus(_A)
_SwPortSecVLANOnPortMaxLernAddr_Type=Integer32
_SwPortSecVLANOnPortMaxLernAddr_Object=MibTableColumn
swPortSecVLANOnPortMaxLernAddr=_SwPortSecVLANOnPortMaxLernAddr_Object((1,3,6,1,4,1,171,12,63,3,3,1,1,1),_SwPortSecVLANOnPortMaxLernAddr_Type())
swPortSecVLANOnPortMaxLernAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortSecVLANOnPortMaxLernAddr.setStatus(_A)
class _SwPortSecVLANOnPortAddCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),('add',2)))
_SwPortSecVLANOnPortAddCtrl_Type.__name__=_C
_SwPortSecVLANOnPortAddCtrl_Object=MibTableColumn
swPortSecVLANOnPortAddCtrl=_SwPortSecVLANOnPortAddCtrl_Object((1,3,6,1,4,1,171,12,63,3,3,1,1,2),_SwPortSecVLANOnPortAddCtrl_Type())
swPortSecVLANOnPortAddCtrl.setMaxAccess('read-create')
if mibBuilder.loadTexts:swPortSecVLANOnPortAddCtrl.setStatus(_A)
_SwPortSecMgmtByVLANOnPortClearCtrl_ObjectIdentity=ObjectIdentity
swPortSecMgmtByVLANOnPortClearCtrl=_SwPortSecMgmtByVLANOnPortClearCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,63,3,3,2))
_SwPortSecMgmtByVLANOnPortClearPort_Type=Integer32
_SwPortSecMgmtByVLANOnPortClearPort_Object=MibScalar
swPortSecMgmtByVLANOnPortClearPort=_SwPortSecMgmtByVLANOnPortClearPort_Object((1,3,6,1,4,1,171,12,63,3,3,2,1),_SwPortSecMgmtByVLANOnPortClearPort_Type())
swPortSecMgmtByVLANOnPortClearPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortSecMgmtByVLANOnPortClearPort.setStatus(_A)
_SwPortSecMgmtByVLANOnPortClearVID_Type=Integer32
_SwPortSecMgmtByVLANOnPortClearVID_Object=MibScalar
swPortSecMgmtByVLANOnPortClearVID=_SwPortSecMgmtByVLANOnPortClearVID_Object((1,3,6,1,4,1,171,12,63,3,3,2,2),_SwPortSecMgmtByVLANOnPortClearVID_Type())
swPortSecMgmtByVLANOnPortClearVID.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortSecMgmtByVLANOnPortClearVID.setStatus(_A)
class _SwPortSecMgmtByVLANOnPortClearAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_H,2)))
_SwPortSecMgmtByVLANOnPortClearAction_Type.__name__=_C
_SwPortSecMgmtByVLANOnPortClearAction_Object=MibScalar
swPortSecMgmtByVLANOnPortClearAction=_SwPortSecMgmtByVLANOnPortClearAction_Object((1,3,6,1,4,1,171,12,63,3,3,2,3),_SwPortSecMgmtByVLANOnPortClearAction_Type())
swPortSecMgmtByVLANOnPortClearAction.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortSecMgmtByVLANOnPortClearAction.setStatus(_A)
_SwPortSecEntriesTable_Object=MibTable
swPortSecEntriesTable=_SwPortSecEntriesTable_Object((1,3,6,1,4,1,171,12,63,3,4))
if mibBuilder.loadTexts:swPortSecEntriesTable.setStatus(_A)
_SwPortSecEntriesEntry_Object=MibTableRow
swPortSecEntriesEntry=_SwPortSecEntriesEntry_Object((1,3,6,1,4,1,171,12,63,3,4,1))
swPortSecEntriesEntry.setIndexNames((0,_D,_M),(0,_D,_N))
if mibBuilder.loadTexts:swPortSecEntriesEntry.setStatus(_A)
_SwPortSecMac_Type=MacAddress
_SwPortSecMac_Object=MibTableColumn
swPortSecMac=_SwPortSecMac_Object((1,3,6,1,4,1,171,12,63,3,4,1,1),_SwPortSecMac_Type())
swPortSecMac.setMaxAccess(_K)
if mibBuilder.loadTexts:swPortSecMac.setStatus(_A)
class _SwPortSecVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwPortSecVID_Type.__name__=_C
_SwPortSecVID_Object=MibTableColumn
swPortSecVID=_SwPortSecVID_Object((1,3,6,1,4,1,171,12,63,3,4,1,2),_SwPortSecVID_Type())
swPortSecVID.setMaxAccess(_K)
if mibBuilder.loadTexts:swPortSecVID.setStatus(_A)
_SwPortSecPort_Type=Integer32
_SwPortSecPort_Object=MibTableColumn
swPortSecPort=_SwPortSecPort_Object((1,3,6,1,4,1,171,12,63,3,4,1,3),_SwPortSecPort_Type())
swPortSecPort.setMaxAccess(_K)
if mibBuilder.loadTexts:swPortSecPort.setStatus(_A)
class _SwPortSecDelCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_H,2)))
_SwPortSecDelCtrl_Type.__name__=_C
_SwPortSecDelCtrl_Object=MibTableColumn
swPortSecDelCtrl=_SwPortSecDelCtrl_Object((1,3,6,1,4,1,171,12,63,3,4,1,4),_SwPortSecDelCtrl_Type())
swPortSecDelCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortSecDelCtrl.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'swPortSecMIB':swPortSecMIB,'swPortSecCtrl':swPortSecCtrl,'swPortSecTrapLogState':swPortSecTrapLogState,'swPortSecSysMaxLernAddr':swPortSecSysMaxLernAddr,'swPortSecTrapState':swPortSecTrapState,'swPortSecLogState':swPortSecLogState,'swPortSecInfo':swPortSecInfo,'swPortSecMgmt':swPortSecMgmt,'swPortSecMgmtByPort':swPortSecMgmtByPort,'swPortSecPortTable':swPortSecPortTable,'swPortSecPortEntry':swPortSecPortEntry,_I:swPortSecPortIndex,'swPortSecPortMaxLernAddr':swPortSecPortMaxLernAddr,'swPortSecPortLockAddrMode':swPortSecPortLockAddrMode,'swPortSecPortAdmState':swPortSecPortAdmState,'swPortSecPortClearCtrl':swPortSecPortClearCtrl,'swPortSecPortViolationAction':swPortSecPortViolationAction,'swPortSecMgmtByVLAN':swPortSecMgmtByVLAN,'swPortSecVLANTable':swPortSecVLANTable,'swPortSecVLANEntry':swPortSecVLANEntry,_J:swPortSecVLANID,'swPortSecVLANMaxLernAddr':swPortSecVLANMaxLernAddr,'swPortSecVLANClearCtrl':swPortSecVLANClearCtrl,'swPortSecMgmtByVLANOnPort':swPortSecMgmtByVLANOnPort,'swPortSecVLANOnPortTable':swPortSecVLANOnPortTable,'swPortSecVLANOnPortEntry':swPortSecVLANOnPortEntry,'swPortSecVLANOnPortMaxLernAddr':swPortSecVLANOnPortMaxLernAddr,'swPortSecVLANOnPortAddCtrl':swPortSecVLANOnPortAddCtrl,'swPortSecMgmtByVLANOnPortClearCtrl':swPortSecMgmtByVLANOnPortClearCtrl,'swPortSecMgmtByVLANOnPortClearPort':swPortSecMgmtByVLANOnPortClearPort,'swPortSecMgmtByVLANOnPortClearVID':swPortSecMgmtByVLANOnPortClearVID,'swPortSecMgmtByVLANOnPortClearAction':swPortSecMgmtByVLANOnPortClearAction,'swPortSecEntriesTable':swPortSecEntriesTable,'swPortSecEntriesEntry':swPortSecEntriesEntry,_M:swPortSecMac,_N:swPortSecVID,'swPortSecPort':swPortSecPort,'swPortSecDelCtrl':swPortSecDelCtrl})