_T='fxPort'
_S='flPort'
_R='fcQxPortStatusIndex'
_Q='fcQxPortStatusModule'
_P='testing'
_O='offline'
_N='online'
_M='fcQxPortPhysIndex'
_L='fcQxPortPhysModule'
_K='connUnitId'
_J='FCMGMT-MIB'
_I='fcQxPortPhysOperStatus'
_H='fcQxPortPhysAdminStatus'
_G='down'
_F='read-write'
_E='read-only'
_D='not-accessible'
_C='Integer32'
_B='QLOGIC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
connUnitId,=mibBuilder.importSymbols(_J,_K)
ancorOidTree,=mibBuilder.importSymbols('QLOGIC-SMI','ancorOidTree')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ancorPortModule=ModuleIdentity((1,3,6,1,4,1,1663,1,3))
if mibBuilder.loadTexts:ancorPortModule.setRevisions(('2009-09-29 00:00','2006-10-11 00:00'))
class FcQlModuleIndex(TextualConvention,Unsigned32):status=_A
class FcQxPortIndex(TextualConvention,Unsigned32):status=_A
_QlSB2PortControl_ObjectIdentity=ObjectIdentity
qlSB2PortControl=_QlSB2PortControl_ObjectIdentity((1,3,6,1,4,1,1663,1,3,10))
_FcQxPortPhysTable_Object=MibTable
fcQxPortPhysTable=_FcQxPortPhysTable_Object((1,3,6,1,4,1,1663,1,3,10,1))
if mibBuilder.loadTexts:fcQxPortPhysTable.setStatus(_A)
_FcQxPortPhysEntry_Object=MibTableRow
fcQxPortPhysEntry=_FcQxPortPhysEntry_Object((1,3,6,1,4,1,1663,1,3,10,1,1))
fcQxPortPhysEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:fcQxPortPhysEntry.setStatus(_A)
_FcQxPortPhysModule_Type=FcQlModuleIndex
_FcQxPortPhysModule_Object=MibTableColumn
fcQxPortPhysModule=_FcQxPortPhysModule_Object((1,3,6,1,4,1,1663,1,3,10,1,1,1),_FcQxPortPhysModule_Type())
fcQxPortPhysModule.setMaxAccess(_D)
if mibBuilder.loadTexts:fcQxPortPhysModule.setStatus(_A)
_FcQxPortPhysIndex_Type=FcQxPortIndex
_FcQxPortPhysIndex_Object=MibTableColumn
fcQxPortPhysIndex=_FcQxPortPhysIndex_Object((1,3,6,1,4,1,1663,1,3,10,1,1,2),_FcQxPortPhysIndex_Type())
fcQxPortPhysIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fcQxPortPhysIndex.setStatus(_A)
class _FcQxPortPhysAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3)))
_FcQxPortPhysAdminStatus_Type.__name__=_C
_FcQxPortPhysAdminStatus_Object=MibTableColumn
fcQxPortPhysAdminStatus=_FcQxPortPhysAdminStatus_Object((1,3,6,1,4,1,1663,1,3,10,1,1,3),_FcQxPortPhysAdminStatus_Type())
fcQxPortPhysAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fcQxPortPhysAdminStatus.setStatus(_A)
class _FcQxPortPhysOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),('linkFailure',4)))
_FcQxPortPhysOperStatus_Type.__name__=_C
_FcQxPortPhysOperStatus_Object=MibTableColumn
fcQxPortPhysOperStatus=_FcQxPortPhysOperStatus_Object((1,3,6,1,4,1,1663,1,3,10,1,1,4),_FcQxPortPhysOperStatus_Type())
fcQxPortPhysOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fcQxPortPhysOperStatus.setStatus(_A)
class _FcQxQuailPortPhysAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_G,2)))
_FcQxQuailPortPhysAdminStatus_Type.__name__=_C
_FcQxQuailPortPhysAdminStatus_Object=MibTableColumn
fcQxQuailPortPhysAdminStatus=_FcQxQuailPortPhysAdminStatus_Object((1,3,6,1,4,1,1663,1,3,10,1,1,5),_FcQxQuailPortPhysAdminStatus_Type())
fcQxQuailPortPhysAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fcQxQuailPortPhysAdminStatus.setStatus(_A)
class _FcQxQuailPortPhysOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_G,2)))
_FcQxQuailPortPhysOperStatus_Type.__name__=_C
_FcQxQuailPortPhysOperStatus_Object=MibTableColumn
fcQxQuailPortPhysOperStatus=_FcQxQuailPortPhysOperStatus_Object((1,3,6,1,4,1,1663,1,3,10,1,1,6),_FcQxQuailPortPhysOperStatus_Type())
fcQxQuailPortPhysOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fcQxQuailPortPhysOperStatus.setStatus(_A)
class _FcQxQuailPortPhysReasonCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('unknown',1),('up',2),(_G,3),('notConnected',4),('sfpAbsent',5),('sfpUnsupported',6),('hardwareFailure',7),('isolated',8)))
_FcQxQuailPortPhysReasonCode_Type.__name__=_C
_FcQxQuailPortPhysReasonCode_Object=MibTableColumn
fcQxQuailPortPhysReasonCode=_FcQxQuailPortPhysReasonCode_Object((1,3,6,1,4,1,1663,1,3,10,1,1,7),_FcQxQuailPortPhysReasonCode_Type())
fcQxQuailPortPhysReasonCode.setMaxAccess(_E)
if mibBuilder.loadTexts:fcQxQuailPortPhysReasonCode.setStatus(_A)
_QlSB2PortStatus_ObjectIdentity=ObjectIdentity
qlSB2PortStatus=_QlSB2PortStatus_ObjectIdentity((1,3,6,1,4,1,1663,1,3,11))
_FcQxPortStatusTable_Object=MibTable
fcQxPortStatusTable=_FcQxPortStatusTable_Object((1,3,6,1,4,1,1663,1,3,11,1))
if mibBuilder.loadTexts:fcQxPortStatusTable.setStatus(_A)
_FcQxPortStatusEntry_Object=MibTableRow
fcQxPortStatusEntry=_FcQxPortStatusEntry_Object((1,3,6,1,4,1,1663,1,3,11,1,1))
fcQxPortStatusEntry.setIndexNames((0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:fcQxPortStatusEntry.setStatus(_A)
_FcQxPortStatusModule_Type=FcQlModuleIndex
_FcQxPortStatusModule_Object=MibTableColumn
fcQxPortStatusModule=_FcQxPortStatusModule_Object((1,3,6,1,4,1,1663,1,3,11,1,1,1),_FcQxPortStatusModule_Type())
fcQxPortStatusModule.setMaxAccess(_D)
if mibBuilder.loadTexts:fcQxPortStatusModule.setStatus(_A)
_FcQxPortStatusIndex_Type=FcQxPortIndex
_FcQxPortStatusIndex_Object=MibTableColumn
fcQxPortStatusIndex=_FcQxPortStatusIndex_Object((1,3,6,1,4,1,1663,1,3,11,1,1,2),_FcQxPortStatusIndex_Type())
fcQxPortStatusIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fcQxPortStatusIndex.setStatus(_A)
class _FcQxQuailPortOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,6)));namedValues=NamedValues(*(('auto',1),('fPort',2),(_S,3),('ePort',4),(_T,6)))
_FcQxQuailPortOperMode_Type.__name__=_C
_FcQxQuailPortOperMode_Object=MibTableColumn
fcQxQuailPortOperMode=_FcQxQuailPortOperMode_Object((1,3,6,1,4,1,1663,1,3,11,1,1,3),_FcQxQuailPortOperMode_Type())
fcQxQuailPortOperMode.setMaxAccess(_E)
if mibBuilder.loadTexts:fcQxQuailPortOperMode.setStatus(_A)
class _FcQxQuailPortAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,6)));namedValues=NamedValues(*(('auto',1),('fPort',2),(_S,3),('ePort',4),(_T,6)))
_FcQxQuailPortAdminMode_Type.__name__=_C
_FcQxQuailPortAdminMode_Object=MibTableColumn
fcQxQuailPortAdminMode=_FcQxQuailPortAdminMode_Object((1,3,6,1,4,1,1663,1,3,11,1,1,4),_FcQxQuailPortAdminMode_Type())
fcQxQuailPortAdminMode.setMaxAccess(_F)
if mibBuilder.loadTexts:fcQxQuailPortAdminMode.setStatus(_A)
qlSB2PortLinkDown=NotificationType((1,3,6,1,4,1,1663,1,3,0,10))
qlSB2PortLinkDown.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:qlSB2PortLinkDown.setStatus(_A)
qlSB2PortLinkUp=NotificationType((1,3,6,1,4,1,1663,1,3,0,11))
qlSB2PortLinkUp.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:qlSB2PortLinkUp.setStatus(_A)
qlconnUnitAddedTrap=NotificationType((1,3,6,1,4,1,1663,1,3,0,12))
qlconnUnitAddedTrap.setObjects((_J,_K))
if mibBuilder.loadTexts:qlconnUnitAddedTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'FcQlModuleIndex':FcQlModuleIndex,'FcQxPortIndex':FcQxPortIndex,'ancorPortModule':ancorPortModule,'qlSB2PortLinkDown':qlSB2PortLinkDown,'qlSB2PortLinkUp':qlSB2PortLinkUp,'qlconnUnitAddedTrap':qlconnUnitAddedTrap,'qlSB2PortControl':qlSB2PortControl,'fcQxPortPhysTable':fcQxPortPhysTable,'fcQxPortPhysEntry':fcQxPortPhysEntry,_L:fcQxPortPhysModule,_M:fcQxPortPhysIndex,_H:fcQxPortPhysAdminStatus,_I:fcQxPortPhysOperStatus,'fcQxQuailPortPhysAdminStatus':fcQxQuailPortPhysAdminStatus,'fcQxQuailPortPhysOperStatus':fcQxQuailPortPhysOperStatus,'fcQxQuailPortPhysReasonCode':fcQxQuailPortPhysReasonCode,'qlSB2PortStatus':qlSB2PortStatus,'fcQxPortStatusTable':fcQxPortStatusTable,'fcQxPortStatusEntry':fcQxPortStatusEntry,_Q:fcQxPortStatusModule,_R:fcQxPortStatusIndex,'fcQxQuailPortOperMode':fcQxQuailPortOperMode,'fcQxQuailPortAdminMode':fcQxQuailPortAdminMode})