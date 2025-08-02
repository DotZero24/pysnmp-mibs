_m='bscExtAddressGroup'
_l='bscPortsGroupRev1'
_k='bscPortsGroup'
_j='bscExtSelectAddress'
_i='bscPortContentionDialTimeout'
_h='bscPortVirtualAddress'
_g='bscPortSpecPoll'
_f='bscPortHostTimeout'
_e='bscCUProtocolViolations'
_d='bscCUHardErrors'
_c='bscCUSoftErrors'
_b='bscCUDataFramesReceived'
_a='bscCUDataFramesSent'
_Z='bscCUTotalFramesReceived'
_Y='bscCUTotalFramesSent'
_X='bscCUBytesReceived'
_W='bscCUBytesSent'
_V='bscCUState'
_U='obsolete'
_T='bscExtPollAddress'
_S='not-accessible'
_R='bscCUAddress'
_Q='bscControlUnitsGroup'
_P='bscPortProtocolViolations'
_O='bscPortHardErrors'
_N='bscPortSoftErrors'
_M='bscPortUnknownControlUnitsReceived'
_L='bscPortRecoveryRetries'
_K='bscPortPollTimeout'
_J='bscPortServlim'
_I='bscPortPause'
_H='bscPortCodeSet'
_G='bscPortRole'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-BSC-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoBscMIB=ModuleIdentity((1,3,6,1,4,1,9,9,36))
if mibBuilder.loadTexts:ciscoBscMIB.setRevisions(('2004-08-25 00:00','1997-01-25 00:00','1995-08-21 00:00'))
_BscObjects_ObjectIdentity=ObjectIdentity
bscObjects=_BscObjects_ObjectIdentity((1,3,6,1,4,1,9,9,36,1))
_BscPorts_ObjectIdentity=ObjectIdentity
bscPorts=_BscPorts_ObjectIdentity((1,3,6,1,4,1,9,9,36,1,1))
_BscPortTable_Object=MibTable
bscPortTable=_BscPortTable_Object((1,3,6,1,4,1,9,9,36,1,1,1))
if mibBuilder.loadTexts:bscPortTable.setStatus(_B)
_BscPortEntry_Object=MibTableRow
bscPortEntry=_BscPortEntry_Object((1,3,6,1,4,1,9,9,36,1,1,1,1))
bscPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:bscPortEntry.setStatus(_B)
class _BscPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('primary',1),('secondary',2),('contention',3),('dialContention',4),('generic',5)))
_BscPortRole_Type.__name__=_D
_BscPortRole_Object=MibTableColumn
bscPortRole=_BscPortRole_Object((1,3,6,1,4,1,9,9,36,1,1,1,1,1),_BscPortRole_Type())
bscPortRole.setMaxAccess(_C)
if mibBuilder.loadTexts:bscPortRole.setStatus(_B)
class _BscPortCodeSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ebcdic',1),('ascii',2)))
_BscPortCodeSet_Type.__name__=_D
_BscPortCodeSet_Object=MibTableColumn
bscPortCodeSet=_BscPortCodeSet_Object((1,3,6,1,4,1,9,9,36,1,1,1,1,2),_BscPortCodeSet_Type())
bscPortCodeSet.setMaxAccess(_C)
if mibBuilder.loadTexts:bscPortCodeSet.setStatus(_B)
class _BscPortPause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BscPortPause_Type.__name__=_D
_BscPortPause_Object=MibTableColumn
bscPortPause=_BscPortPause_Object((1,3,6,1,4,1,9,9,36,1,1,1,1,3),_BscPortPause_Type())
bscPortPause.setMaxAccess(_C)
if mibBuilder.loadTexts:bscPortPause.setStatus(_B)
class _BscPortServlim_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_BscPortServlim_Type.__name__=_D
_BscPortServlim_Object=MibTableColumn
bscPortServlim=_BscPortServlim_Object((1,3,6,1,4,1,9,9,36,1,1,1,1,4),_BscPortServlim_Type())
bscPortServlim.setMaxAccess(_C)
if mibBuilder.loadTexts:bscPortServlim.setStatus(_B)
class _BscPortPollTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_BscPortPollTimeout_Type.__name__=_D
_BscPortPollTimeout_Object=MibTableColumn
bscPortPollTimeout=_BscPortPollTimeout_Object((1,3,6,1,4,1,9,9,36,1,1,1,1,5),_BscPortPollTimeout_Type())
bscPortPollTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:bscPortPollTimeout.setStatus(_B)
class _BscPortRecoveryRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_BscPortRecoveryRetries_Type.__name__=_D
_BscPortRecoveryRetries_Object=MibTableColumn
bscPortRecoveryRetries=_BscPortRecoveryRetries_Object((1,3,6,1,4,1,9,9,36,1,1,1,1,6),_BscPortRecoveryRetries_Type())
bscPortRecoveryRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:bscPortRecoveryRetries.setStatus(_B)
_BscPortUnknownControlUnitsReceived_Type=Counter32
_BscPortUnknownControlUnitsReceived_Object=MibTableColumn
bscPortUnknownControlUnitsReceived=_BscPortUnknownControlUnitsReceived_Object((1,3,6,1,4,1,9,9,36,1,1,1,1,7),_BscPortUnknownControlUnitsReceived_Type())
bscPortUnknownControlUnitsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:bscPortUnknownControlUnitsReceived.setStatus(_B)
_BscPortSoftErrors_Type=Counter32
_BscPortSoftErrors_Object=MibTableColumn
bscPortSoftErrors=_BscPortSoftErrors_Object((1,3,6,1,4,1,9,9,36,1,1,1,1,8),_BscPortSoftErrors_Type())
bscPortSoftErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:bscPortSoftErrors.setStatus(_B)
_BscPortHardErrors_Type=Counter32
_BscPortHardErrors_Object=MibTableColumn
bscPortHardErrors=_BscPortHardErrors_Object((1,3,6,1,4,1,9,9,36,1,1,1,1,9),_BscPortHardErrors_Type())
bscPortHardErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:bscPortHardErrors.setStatus(_B)
_BscPortProtocolViolations_Type=Counter32
_BscPortProtocolViolations_Object=MibTableColumn
bscPortProtocolViolations=_BscPortProtocolViolations_Object((1,3,6,1,4,1,9,9,36,1,1,1,1,10),_BscPortProtocolViolations_Type())
bscPortProtocolViolations.setMaxAccess(_C)
if mibBuilder.loadTexts:bscPortProtocolViolations.setStatus(_B)
class _BscPortHostTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3000))
_BscPortHostTimeout_Type.__name__=_D
_BscPortHostTimeout_Object=MibTableColumn
bscPortHostTimeout=_BscPortHostTimeout_Object((1,3,6,1,4,1,9,9,36,1,1,1,1,11),_BscPortHostTimeout_Type())
bscPortHostTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:bscPortHostTimeout.setStatus(_B)
if mibBuilder.loadTexts:bscPortHostTimeout.setUnits('deciseconds')
_BscPortSpecPoll_Type=TruthValue
_BscPortSpecPoll_Object=MibTableColumn
bscPortSpecPoll=_BscPortSpecPoll_Object((1,3,6,1,4,1,9,9,36,1,1,1,1,12),_BscPortSpecPoll_Type())
bscPortSpecPoll.setMaxAccess(_C)
if mibBuilder.loadTexts:bscPortSpecPoll.setStatus(_B)
class _BscPortVirtualAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_BscPortVirtualAddress_Type.__name__=_D
_BscPortVirtualAddress_Object=MibTableColumn
bscPortVirtualAddress=_BscPortVirtualAddress_Object((1,3,6,1,4,1,9,9,36,1,1,1,1,13),_BscPortVirtualAddress_Type())
bscPortVirtualAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:bscPortVirtualAddress.setStatus(_B)
class _BscPortContentionDialTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,30))
_BscPortContentionDialTimeout_Type.__name__=_D
_BscPortContentionDialTimeout_Object=MibTableColumn
bscPortContentionDialTimeout=_BscPortContentionDialTimeout_Object((1,3,6,1,4,1,9,9,36,1,1,1,1,14),_BscPortContentionDialTimeout_Type())
bscPortContentionDialTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:bscPortContentionDialTimeout.setStatus(_B)
if mibBuilder.loadTexts:bscPortContentionDialTimeout.setUnits('seconds')
_BscControlUnits_ObjectIdentity=ObjectIdentity
bscControlUnits=_BscControlUnits_ObjectIdentity((1,3,6,1,4,1,9,9,36,1,2))
_BscControlUnitTable_Object=MibTable
bscControlUnitTable=_BscControlUnitTable_Object((1,3,6,1,4,1,9,9,36,1,2,1))
if mibBuilder.loadTexts:bscControlUnitTable.setStatus(_B)
_BscCUEntry_Object=MibTableRow
bscCUEntry=_BscCUEntry_Object((1,3,6,1,4,1,9,9,36,1,2,1,1))
bscCUEntry.setIndexNames((0,_E,_F),(0,_A,_R))
if mibBuilder.loadTexts:bscCUEntry.setStatus(_B)
class _BscCUAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BscCUAddress_Type.__name__=_D
_BscCUAddress_Object=MibTableColumn
bscCUAddress=_BscCUAddress_Object((1,3,6,1,4,1,9,9,36,1,2,1,1,1),_BscCUAddress_Type())
bscCUAddress.setMaxAccess(_S)
if mibBuilder.loadTexts:bscCUAddress.setStatus(_B)
class _BscCUState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inactive',1),('active',2)))
_BscCUState_Type.__name__=_D
_BscCUState_Object=MibTableColumn
bscCUState=_BscCUState_Object((1,3,6,1,4,1,9,9,36,1,2,1,1,2),_BscCUState_Type())
bscCUState.setMaxAccess(_C)
if mibBuilder.loadTexts:bscCUState.setStatus(_B)
_BscCUBytesSent_Type=Counter32
_BscCUBytesSent_Object=MibTableColumn
bscCUBytesSent=_BscCUBytesSent_Object((1,3,6,1,4,1,9,9,36,1,2,1,1,3),_BscCUBytesSent_Type())
bscCUBytesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:bscCUBytesSent.setStatus(_B)
_BscCUBytesReceived_Type=Counter32
_BscCUBytesReceived_Object=MibTableColumn
bscCUBytesReceived=_BscCUBytesReceived_Object((1,3,6,1,4,1,9,9,36,1,2,1,1,4),_BscCUBytesReceived_Type())
bscCUBytesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:bscCUBytesReceived.setStatus(_B)
_BscCUTotalFramesSent_Type=Counter32
_BscCUTotalFramesSent_Object=MibTableColumn
bscCUTotalFramesSent=_BscCUTotalFramesSent_Object((1,3,6,1,4,1,9,9,36,1,2,1,1,5),_BscCUTotalFramesSent_Type())
bscCUTotalFramesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:bscCUTotalFramesSent.setStatus(_B)
_BscCUTotalFramesReceived_Type=Counter32
_BscCUTotalFramesReceived_Object=MibTableColumn
bscCUTotalFramesReceived=_BscCUTotalFramesReceived_Object((1,3,6,1,4,1,9,9,36,1,2,1,1,6),_BscCUTotalFramesReceived_Type())
bscCUTotalFramesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:bscCUTotalFramesReceived.setStatus(_B)
_BscCUDataFramesSent_Type=Counter32
_BscCUDataFramesSent_Object=MibTableColumn
bscCUDataFramesSent=_BscCUDataFramesSent_Object((1,3,6,1,4,1,9,9,36,1,2,1,1,7),_BscCUDataFramesSent_Type())
bscCUDataFramesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:bscCUDataFramesSent.setStatus(_B)
_BscCUDataFramesReceived_Type=Counter32
_BscCUDataFramesReceived_Object=MibTableColumn
bscCUDataFramesReceived=_BscCUDataFramesReceived_Object((1,3,6,1,4,1,9,9,36,1,2,1,1,8),_BscCUDataFramesReceived_Type())
bscCUDataFramesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:bscCUDataFramesReceived.setStatus(_B)
_BscCUSoftErrors_Type=Counter32
_BscCUSoftErrors_Object=MibTableColumn
bscCUSoftErrors=_BscCUSoftErrors_Object((1,3,6,1,4,1,9,9,36,1,2,1,1,9),_BscCUSoftErrors_Type())
bscCUSoftErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:bscCUSoftErrors.setStatus(_B)
_BscCUHardErrors_Type=Counter32
_BscCUHardErrors_Object=MibTableColumn
bscCUHardErrors=_BscCUHardErrors_Object((1,3,6,1,4,1,9,9,36,1,2,1,1,10),_BscCUHardErrors_Type())
bscCUHardErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:bscCUHardErrors.setStatus(_B)
_BscCUProtocolViolations_Type=Counter32
_BscCUProtocolViolations_Object=MibTableColumn
bscCUProtocolViolations=_BscCUProtocolViolations_Object((1,3,6,1,4,1,9,9,36,1,2,1,1,11),_BscCUProtocolViolations_Type())
bscCUProtocolViolations.setMaxAccess(_C)
if mibBuilder.loadTexts:bscCUProtocolViolations.setStatus(_B)
_BscExtAddresses_ObjectIdentity=ObjectIdentity
bscExtAddresses=_BscExtAddresses_ObjectIdentity((1,3,6,1,4,1,9,9,36,1,3))
_BscExtAddressTable_Object=MibTable
bscExtAddressTable=_BscExtAddressTable_Object((1,3,6,1,4,1,9,9,36,1,3,1))
if mibBuilder.loadTexts:bscExtAddressTable.setStatus(_B)
_BscExtAddressEntry_Object=MibTableRow
bscExtAddressEntry=_BscExtAddressEntry_Object((1,3,6,1,4,1,9,9,36,1,3,1,1))
bscExtAddressEntry.setIndexNames((0,_E,_F),(0,_A,_T))
if mibBuilder.loadTexts:bscExtAddressEntry.setStatus(_B)
class _BscExtPollAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BscExtPollAddress_Type.__name__=_D
_BscExtPollAddress_Object=MibTableColumn
bscExtPollAddress=_BscExtPollAddress_Object((1,3,6,1,4,1,9,9,36,1,3,1,1,1),_BscExtPollAddress_Type())
bscExtPollAddress.setMaxAccess(_S)
if mibBuilder.loadTexts:bscExtPollAddress.setStatus(_B)
class _BscExtSelectAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BscExtSelectAddress_Type.__name__=_D
_BscExtSelectAddress_Object=MibTableColumn
bscExtSelectAddress=_BscExtSelectAddress_Object((1,3,6,1,4,1,9,9,36,1,3,1,1,2),_BscExtSelectAddress_Type())
bscExtSelectAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:bscExtSelectAddress.setStatus(_B)
_BscMibConformance_ObjectIdentity=ObjectIdentity
bscMibConformance=_BscMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,36,3))
_BscMibCompliances_ObjectIdentity=ObjectIdentity
bscMibCompliances=_BscMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,36,3,1))
_BscMibGroups_ObjectIdentity=ObjectIdentity
bscMibGroups=_BscMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,36,3,2))
bscPortsGroup=ObjectGroup((1,3,6,1,4,1,9,9,36,3,2,1))
bscPortsGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:bscPortsGroup.setStatus(_U)
bscControlUnitsGroup=ObjectGroup((1,3,6,1,4,1,9,9,36,3,2,2))
bscControlUnitsGroup.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:bscControlUnitsGroup.setStatus(_B)
bscPortsGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,36,3,2,3))
bscPortsGroupRev1.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_f),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:bscPortsGroupRev1.setStatus(_B)
bscExtAddressGroup=ObjectGroup((1,3,6,1,4,1,9,9,36,3,2,4))
bscExtAddressGroup.setObjects((_A,_j))
if mibBuilder.loadTexts:bscExtAddressGroup.setStatus(_B)
bscMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,36,3,1,1))
bscMibCompliance.setObjects(*((_A,_k),(_A,_Q)))
if mibBuilder.loadTexts:bscMibCompliance.setStatus(_U)
bscMibComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,36,3,1,2))
bscMibComplianceRev1.setObjects(*((_A,_l),(_A,_Q),(_A,_m)))
if mibBuilder.loadTexts:bscMibComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoBscMIB':ciscoBscMIB,'bscObjects':bscObjects,'bscPorts':bscPorts,'bscPortTable':bscPortTable,'bscPortEntry':bscPortEntry,_G:bscPortRole,_H:bscPortCodeSet,_I:bscPortPause,_J:bscPortServlim,_K:bscPortPollTimeout,_L:bscPortRecoveryRetries,_M:bscPortUnknownControlUnitsReceived,_N:bscPortSoftErrors,_O:bscPortHardErrors,_P:bscPortProtocolViolations,_f:bscPortHostTimeout,_g:bscPortSpecPoll,_h:bscPortVirtualAddress,_i:bscPortContentionDialTimeout,'bscControlUnits':bscControlUnits,'bscControlUnitTable':bscControlUnitTable,'bscCUEntry':bscCUEntry,_R:bscCUAddress,_V:bscCUState,_W:bscCUBytesSent,_X:bscCUBytesReceived,_Y:bscCUTotalFramesSent,_Z:bscCUTotalFramesReceived,_a:bscCUDataFramesSent,_b:bscCUDataFramesReceived,_c:bscCUSoftErrors,_d:bscCUHardErrors,_e:bscCUProtocolViolations,'bscExtAddresses':bscExtAddresses,'bscExtAddressTable':bscExtAddressTable,'bscExtAddressEntry':bscExtAddressEntry,_T:bscExtPollAddress,_j:bscExtSelectAddress,'bscMibConformance':bscMibConformance,'bscMibCompliances':bscMibCompliances,'bscMibCompliance':bscMibCompliance,'bscMibComplianceRev1':bscMibComplianceRev1,'bscMibGroups':bscMibGroups,_k:bscPortsGroup,_Q:bscControlUnitsGroup,_l:bscPortsGroupRev1,_m:bscExtAddressGroup})